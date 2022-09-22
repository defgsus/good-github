## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-09-21](docs/good-messages/2022/2022-09-21.md)


2,192,786 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,192,786 were push events containing 3,285,046 commit messages that amount to 249,552,334 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 39 messages:


## [KDr2/postgres](https://github.com/KDr2/postgres)@[1c27d16e6e...](https://github.com/KDr2/postgres/commit/1c27d16e6e5c1f463bbe1e9ece88dda811235165)
#### Wednesday 2022-09-21 00:03:21 by Tom Lane

Revise tree-walk APIs to improve spec compliance & silence warnings.

expression_tree_walker and allied functions have traditionally
declared their callback functions as, say, "bool (*walker) ()"
to allow for variation in the declared types of the callback
functions' context argument.  This is apparently going to be
forbidden by the next version of the C standard, and the latest
version of clang warns about that.  In any case it's always
been pretty poor for error-detection purposes, so fixing it is
a good thing to do.

What we want to do is change the callback argument declarations to
be like "bool (*walker) (Node *node, void *context)", which is
correct so far as expression_tree_walker and friends are concerned,
but not change the actual callback functions.  Strict compliance with
the C standard would require changing them to declare their arguments
as "void *context" and then cast to the appropriate context struct
type internally.  That'd be very invasive and it would also introduce
a bunch of opportunities for future bugs, since we'd no longer have
any check that the correct sort of context object is passed by outside
callers or internal recursion cases.  Therefore, we're just going
to ignore the standard's position that "void *" isn't necessarily
compatible with struct pointers.  No machine built in the last forty
or so years actually behaves that way, so it's not worth introducing
bug hazards for compatibility with long-dead hardware.

Therefore, to silence these compiler warnings, introduce a layer of
macro wrappers that cast the supplied function name to the official
argument type.  Thanks to our use of -Wcast-function-type, this will
still produce a warning if the supplied function is seriously
incompatible with the required signature, without going as far as
the official spec restriction does.

This method fixes the problem without any need for source code changes
outside nodeFuncs.h/.c.  However, it is an ABI break because the
physically called functions now have names ending in "_impl".  Hence
we can only fix it this way in HEAD.  In the back branches, we'll have
to settle for disabling -Wdeprecated-non-prototype.

Discussion: https://postgr.es/m/CA+hUKGKpHPDTv67Y+s6yiC8KH5OXeDg6a-twWo_xznKTcG0kSA@mail.gmail.com

---
## [kwick12/odin-recipes](https://github.com/kwick12/odin-recipes)@[99cb59508a...](https://github.com/kwick12/odin-recipes/commit/99cb59508ab65a090633057644ad3778bc7e1c7c)
#### Wednesday 2022-09-21 00:17:01 by kwick12

Just a bunch of things

I should've added more commits but you just dont think about it when
you're making the project + it's a pain. Next project I'll plan it
all out and take commits more seriously, but noone cares about this
project anyway so it's fine.
I just added some CSS stuff and some buttons and pseudo classes which
was cool. Some things I don't even understand fully but I saw some
videos online and checked out some different things and decided to
include them anyway. I'll know about them in the future so why not
get some experience with them?
This is such a bad commit message lol.

---
## [EbookFoundation/free-programming-books](https://github.com/EbookFoundation/free-programming-books)@[5fd70502a0...](https://github.com/EbookFoundation/free-programming-books/commit/5fd70502a063c46914fd444d2511c8233f81777f)
#### Wednesday 2022-09-21 01:10:22 by Mathieu FONTAINE

Update free-programming-cheatsheets.md - React (#7095)

I suggested a React cheat sheet that I use very often. It is one of the most exhaustive and qualitative in my opinion.

---
## [DesmontTiney/tgstation](https://github.com/DesmontTiney/tgstation)@[f923f61011...](https://github.com/DesmontTiney/tgstation/commit/f923f6101103e4ff1aeefd57d0531a3bc437a77a)
#### Wednesday 2022-09-21 01:38:04 by MMMiracles

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
## [Keegangrajek/diegoberho.com](https://github.com/Keegangrajek/diegoberho.com)@[87d4eba92a...](https://github.com/Keegangrajek/diegoberho.com/commit/87d4eba92a02b848aa3a72c65bf2aced0293c846)
#### Wednesday 2022-09-21 03:18:22 by KeeganGrajek

Diego wanted to change a painting name

We changed tears.of.a.lost.dream to identity.crisis

---
## [mrange/terminal](https://github.com/mrange/terminal)@[b4b6636b49...](https://github.com/mrange/terminal/commit/b4b6636b4952ac8ff6a9864f641973bb49d91ce4)
#### Wednesday 2022-09-21 05:42:59 by Mårten Rånge

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
## [rsalmaso/black](https://github.com/rsalmaso/black)@[0019261abc...](https://github.com/rsalmaso/black/commit/0019261abcf6d9e564ba32d3cc15534b9026f29e)
#### Wednesday 2022-09-21 06:07:45 by Richard Si

Update stable branch after publishing to PyPI (#3223)

We've decided to a) convert stable back into a branch and b) to update
it immediately as part of the release process. We may as well automate
it. And about going back to a branch ...

Git tags are not the right tool, at all[^1]. They come with the
expectation that they will never change. Things will not work as
expected if they do change, doubly so if they change regularly. Once
you pull stable from the remote and it's copied in your local
repository, no matter how many times you run git pull you'll never see
it get updated automatically. Your only recourse is to delete the tag
via `git tag -d stable` before pulling.

This gets annoying really quickly since stable is supposed to be the
solution for folks "who want to move along as Black developers deem
the newest version reliable."[^2] See this comment for how this impacts
users using our Vim plugin[^3]. It also affects us developers[^4]. If
you have stable locally, once we cut a new release and update the stable
tag, a simple `git pull` / `git fetch` will not pull down the updated
stable tag. Unless you remember to delete stable before pulling, stable
will become stale and useless.

You can argue this is a good thing ("people should explicitly opt into
updating stable"), but IMO it does not match user expectations nor
developer expectations[^5]. Especially since not all our integrations
that use stable are bound by this security measure, for example our
GitHub Action (since it does a clean fetch of the repository every time
it's used). I believe consistency would be good here.

Finally, ever since we switched to a tag, we've been facing issues with
ReadTheDocs not picking up updates to stable unless we force a rebuild.
The initial rebuild on the stable update just pulls the commit the tag
previously pointed to. I'm not sure if switching back to a branch will
fix this, but I'd wager it will.

[^1]: https://git-scm.com/docs/git-tag#_on_re_tagging

[^2]: https://black.readthedocs.io/en/stable/contributing/release_process.html#moving-the-stable-tag

[^3]: https://github.com/psf/black/issues/2503#issuecomment-1196357379

[^4]: In fairness, most folks working on Black probably don't use the
      `stable` ref anyway, especially us maintainers who'd know what is
      the latest version by heart, but it'd still be nice to make it
      usable for local dev though.

[^5]: Also what benefit does a `stable` ref have over explicit version
      tags like `22.6.0`? If you're going to opt into some odd pin
      mechanism, might as well use explicit version tags for clarity
      and consistency.

---
## [Monkooky/crawl](https://github.com/Monkooky/crawl)@[e8bc28a0cf...](https://github.com/Monkooky/crawl/commit/e8bc28a0cf5eb223156f893c8f47b1284931e78a)
#### Wednesday 2022-09-21 06:54:22 by DreamDust

vaults: float vaults by DreamDust

dreamdust_dug_too_deep

The dwarves dug a little too deep and unearthed... a Balrug! Even a
mighty dwarf hero (with a potentially good weapon to loot!) fell in
battle to the demon. RIP. Maybe this is why we don't see deep dwarves
much anymore. Hmmmm...

The idea behind this vault is to place a single Balrug early enough that
it's a serious (but not unmanageable) threat. I added a downhatch close
by if players need to escape in a hurry. There are also warning signs in
advance (all the dwarf corpses and the suspicious volcanic floor tiles
outside the Balrug room).

[ Committer's note: Added a runed door for the balrug, adjusted
  transparency, traded volcanic floor for blood. ]

dreamdust_wu_jian_sword_trials

A Wu Jian-themed vault. Challenge three increasingly powerful
sword-wielders for their increasingly good swords.

[ Committer's note: Adjusted depth range, added monsters to the earlier
  trial, trimmed arenas, added transperency. ]

dreamdust_merry_men

Inspired by Robin Hood and his band of merry men. Features a forest with
a bunch of archers and a good bow and aides to banditry to loot in the center.

[ Committer's note: Adjusted layout to prevent teleport closets, monster
  counts, loot. ]

dreamdust_tengu_aerie

A large nest of tengus. They keep their shiny loot in the center...
along with their fledglings (wait, are we the baddies??).

[ Committer's note: moved the crystal walls to the middle, put the
  rock wall on the outside (so the reavers can bolt bounce their
  omnibolts), and thinned the monster density. ]

dreamdust_hydra_shepherd

A shepherd is raising a flock (?) of hydras down in the Depths! Some
players might regret abandoning their flaming weapons after finishing
Lair/Swamp, haha.

[ Committer's note: upgraded the cyclops to a stone giant, added a small
  chance for a really high head count. ]

dreamdust_elfheim

The home of Duvessa and Dowan.
The more-practical Duvessa has training dummies in her room, while the
vain Dowan has a large mirror to admire himself with.

[ Committer's note: cut down on custom tiling/colouring a bit. ]

---
## [AnywayFarus/Skyrat-tg](https://github.com/AnywayFarus/Skyrat-tg)@[f73fc2ea10...](https://github.com/AnywayFarus/Skyrat-tg/commit/f73fc2ea10c3193a56595e9d02d9aab186d99076)
#### Wednesday 2022-09-21 08:11:27 by Halcyon

Redoes bluesec clothing sprites to have a nicer, more consistent color palette, along with correcting alot of glaring mistakes. (#16068)

* Everything

All the bluesec shit redone, given a consistent palette and better colors.

* Forgot the obj sprites, fuck

* formal oversuit

* Hey shitass, watch me kill these sprites

* More obj icons

* Bulltproof items.

Returns helmet to stock TG, cause the current one is ugly ass piss.

* obj

* secmed

* updates secmed a bit more

* helmet

---
## [giuseppe/libpod](https://github.com/giuseppe/libpod)@[09ef6fc66c...](https://github.com/giuseppe/libpod/commit/09ef6fc66cac44dec94c29cd7a1a53f70831446d)
#### Wednesday 2022-09-21 08:59:56 by Ed Santiago

podman generate kube - add actual tests

This exposed a nasty bug in our system-test setup: Ubuntu (runc)
was writing a scratch containers.conf file, and setting CONTAINERS_CONF
to point to it. This was well-intentionedly introduced in #10199 as
part of our long sad history of not testing runc. What I did not
understand at that time is that CONTAINERS_CONF is **dangerous**:
it does not mean "I will read standard containers.conf and then
override", it means "I will **IGNORE** standard containers.conf
and use only the settings in this file"! So on Ubuntu we were
losing all the default settings: capabilities, sysctls, all.

Yes, this is documented in containers.conf(5) but it is such
a huge violation of POLA that I need to repeat it.

In #14972, as yet another attempt to fix our runc crisis, I
introduced a new runc-override mechanism: create a custom
/etc/containers/containers.conf when OCI_RUNTIME=runc.
Unlike the CONTAINERS_CONF envariable, the /etc file
actually means what you think it means: "read the default
file first, then override with the /etc file contents".
I.e., we get the desired defaults. But I didn't remember
this helpers.bash workaround, so our runc testing has
actually been flawed: we have not been testing with
the system containers.conf. This commit removes the
no-longer-needed and never-actually-wanted workaround,
and by virtue of testing the cap-drops in kube generate,
we add a regression test to make sure this never happens
again.

It's a little scary that we haven't been testing capabilities.

Also scary: this PR requires python, for converting yaml to json.
I think that should be safe: python3 'import yaml' and 'json'
works fine on a RHEL8.7 VM from 1minutetip.

Signed-off-by: Ed Santiago <santiago@redhat.com>

---
## [warface1234455/Yogstation](https://github.com/warface1234455/Yogstation)@[f4c7571fc3...](https://github.com/warface1234455/Yogstation/commit/f4c7571fc333779cbf761e637f2774a62b6b4d78)
#### Wednesday 2022-09-21 11:15:24 by Vaelophis Nyx

[MDB IGNORE][Gax] Adds new area for AI Ship Access & Adds APC & Fixes Cameras (#15291)

* argh

* fuck you MDB2

* I hate areas, I hate areas

* Update GaxStation.dmm

* Update GaxStation.dmm

* Update GaxStation.dmm

* Update GaxStation.dmm

* Update GaxStation.dmm

---
## [exhq/neOwOfetch](https://github.com/exhq/neOwOfetch)@[084603b8a8...](https://github.com/exhq/neOwOfetch/commit/084603b8a8200cbba6c78fb3155ac3ab7489a9c1)
#### Wednesday 2022-09-21 11:17:46 by echo

holy fucking shit fr another neowofetch ubdate????!?!?!?!/! i fucking love neowofetch its the best fucking anime bro frfr bruh fr

---
## [wy2016xiao/react-commentary](https://github.com/wy2016xiao/react-commentary)@[b6978bc38f...](https://github.com/wy2016xiao/react-commentary/commit/b6978bc38f6788c7e73982b9fd2771aabdf36f15)
#### Wednesday 2022-09-21 11:19:33 by Andrew Clark

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
## [mmp/sct2](https://github.com/mmp/sct2)@[64251b0632...](https://github.com/mmp/sct2/commit/64251b0632b2b653a8f07d148a659cd2971c5ee4)
#### Wednesday 2022-09-21 12:13:21 by Matt Pharr

Major rewrite for robustness / forgiveness

Allow named Geo sections, which seems to be a widely-used but
undocumented extension.

Allow using airport names as positions in other sections, which seems
to be occasionally-done in practice.

Be more forgiving in SID/STAR parsing: many files don't adhere to the
26 character formatting so instead try different chunkings until we
find a segment of 4 positions to infer where the name ends.

Improve robustness of lat/long parsing to allow partial specifications
like E40.22 and not require additional decimals.

Rework line handling to report accurate line numbers with errors.
(This had been broken)

Switch to string rather than []byte; the code is cleaner and we're
now unicode-friendly.

Switch to go-style error returns from parsing functions rather than
issuing syntax errors deep in the parse functions.

Be better about continuing onward (and not crashing) when things
are borked.

---
## [WhatHappenedTo2nd/ft_transcendence](https://github.com/WhatHappenedTo2nd/ft_transcendence)@[14276067f5...](https://github.com/WhatHappenedTo2nd/ft_transcendence/commit/14276067f574a211ed683fa68833e1e7816e94e2)
#### Wednesday 2022-09-21 13:03:14 by inyang

conflicting backend package-lock.json file fuck you

---
## [Kitsunemitsu/lobotomy-corp13](https://github.com/Kitsunemitsu/lobotomy-corp13)@[f490a226b2...](https://github.com/Kitsunemitsu/lobotomy-corp13/commit/f490a226b241795abefbddeb84938af4e183b2a8)
#### Wednesday 2022-09-21 13:55:35 by Gelatelly

sassy shepherd

makes shepherd lie like the bitch he is

I HATE RUNTIMES I HATE RUNTIMES I HATERUNTIMES

use the shittiest method in existence to bypass runtimes, unfortunately I couldn't use initial() without adding some issues so fuck me I guess

updates the people and abno list

imagine using signalers

why is there a huge gap there

leftovercode that doesn't do anything

linter fix?

this is the worst fix I hate linters so much

I'm making everything worse by trying to fix it

send help

adds abno spawn signaller

I love adding signallers for meme PR

changes how the lists are used/rename a few things

SLightCamelCaseChange

clears the people_list on destroy()

this isn't much but it should avoid some problems

moves the abno spawn signal to lobotomy_corp.dm

---
## [Kitsunemitsu/lobotomy-corp13](https://github.com/Kitsunemitsu/lobotomy-corp13)@[f0e6476eb0...](https://github.com/Kitsunemitsu/lobotomy-corp13/commit/f0e6476eb051d781f7e4d0be7976dff0ff72fda0)
#### Wednesday 2022-09-21 14:37:06 by Lance

The Great Workening

Attribute Levels Displayed

No thoughts were had, thoughts injected.

Attribute Levels go brrr

Requested Change Made

WHOOPS WRONG PARENTHESIS

I swear I know how Clamps work

Holy shit how did this not get found out earlier

---
## [ceccopierangiolieugenio/pyTermTk](https://github.com/ceccopierangiolieugenio/pyTermTk)@[12ee3463b9...](https://github.com/ceccopierangiolieugenio/pyTermTk/commit/12ee3463b918919478147aadbbb0adce7ebcf34f)
#### Wednesday 2022-09-21 16:05:59 by Eugenio Parodi

Removed an import that the FUCKING pylance added automatically, FUCK YOU!!!

---
## [oxen-io/lokinet](https://github.com/oxen-io/lokinet)@[e981c9f899...](https://github.com/oxen-io/lokinet/commit/e981c9f89983a12cc75d691fc439366703d5bfff)
#### Wednesday 2022-09-21 16:37:43 by Jeff

tweaks for wine and yarn for gui

* allow specifying a custom yarn binary for building the gui using -DYARN= cmake option
* unset DISPLAY when calling wine because i hate popups
* do not rebuild gui when building for windows
* by setting the magical undocumented env var USE_SYSTEM_7ZA to 'true' we can have the pile of npm bullshit code use our system's local 7z binary instead of the probably not backdoored binary from npm, yes for real. i hate nodejs so god damn much you have no fucking idea
* allow providing a custom gui from a zip file via -DGUI_ZIP_FILE cmake option

---
## [PixelExperience-Devices/kernel_motorola_msm8998](https://github.com/PixelExperience-Devices/kernel_motorola_msm8998)@[7ce99efc8b...](https://github.com/PixelExperience-Devices/kernel_motorola_msm8998/commit/7ce99efc8b4d94d1c47764ad90619f534b6526f4)
#### Wednesday 2022-09-21 17:04:50 by Christian Brauner

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
## [fpv-wtf/msp-osd](https://github.com/fpv-wtf/msp-osd)@[1b8b4b6f67...](https://github.com/fpv-wtf/msp-osd/commit/1b8b4b6f67e471360be4560071d0edbc5a8a5205)
#### Wednesday 2022-09-21 19:43:56 by Brian Ledbetter

Fakehd and Config Options (#52) - thank you @benlumley

* Squashed commit of the following:

commit b9bcccbf76974e34c672b0e39c1443bb6ac84af9
Author: Ben Lumley <ben@benlumley.co.uk>
Date:   Tue Sep 20 22:48:35 2022 +0100

    switch to config

commit c50d23104e4fb4f6e6a25b2bb0b72fcecc6128f7
Author: Ben Lumley <ben@benlumley.co.uk>
Date:   Tue Sep 20 14:16:24 2022 +0100

    changed mind; y direction doesn't need the 1 offset - nicer to have it near the edge; then you can get things inline with the goggles own osd at the bottom

commit 4af3df6c126ac273b03e9191699b92513e1b3f2d
Author: Ben Lumley <ben@benlumley.co.uk>
Date:   Mon Sep 19 20:47:59 2022 +0100

    Battery symbols flash when in warning state; so can't use them to trigger centering :(

commit 689384f0449daed42929d90f19c1946368fd0a31
Author: Ben Lumley <ben@benlumley.co.uk>
Date:   Mon Sep 19 10:26:58 2022 +0100

    In from the edges a bit; we have spare rows/cols - in my opinion it looks better not to have everything literally touching the sides

commit db06e4885c93a9a0350ffab6afa08fcb068fd63a
Author: Ben Lumley <ben@benlumley.co.uk>
Date:   Fri Sep 16 19:39:50 2022 +0100

    Docs review + add fakehd

commit b6f20c0cf2e74e6bca98555c731ea4b11f41d6f4
Author: Ben Lumley <ben@benlumley.co.uk>
Date:   Thu Sep 15 22:49:18 2022 +0100

    Debugged/working

commit 8000b88d022fb40e30e0aa7f03df0613c637ece8
Author: Ben Lumley <ben@benlumley.co.uk>
Date:   Fri Sep 2 00:15:28 2022 +0100

    Attempt at proof of concept to 'spread' the SD osd to the corners + middle of the HD OSD.

    Not managed to get it running to test. But here's the idea:

    BF grid is 16 * 30
    HD is 18 * 50

    BF Rows 1-5 -> HD Rows 1-5
    BF Rows 6-10 -> HD Rows 7-11
    BF Rows 11-16 -> HD Rows 12-18

    BF Cols 1-10 -> HD Cols 1-10
    BF Cols 11-20 -> HD Cols 20 - 30
    BF Cols 21-30 -> HD Cols 40 - 50

    Visually, divide the OSD into a 3*3 grid and stretch it to the top/bottom/left/right corners.

    I tend to put osd elements in the bottom corners, bottom middle + the warnings in the middle. So for me at least; this is useful.

    Obvious drawback; the menus gonna look weird!

    fix for force hd not working because BF never even sends the MSP command; it needs to default to it earlier.
    also add 2 unsplit rows for wider elemenets - i like warnings in the middle of the screen

    Add full display info; attempt to detect menu/post flight stats and switch to centering in this case

    Remove testing code

    make code paths simpler

    Find the center trigger instead of hard coding

    configurable; with a file for now

commit 60215e0240cbe5d34d0db447b01d948808705ed2
Author: bri3d <brian@brianledbetter.com>
Date:   Tue Sep 20 22:24:16 2022 -0600

    forgot an important directory...

commit 1c5ed2a88feb03bf209e4ed3c3ac4ed277681f47
Author: bri3d <brian@brianledbetter.com>
Date:   Thu Sep 15 21:51:48 2022 -0600

    add goggles config file

commit cfe24e265e8a3bfa92c34d6fc0e9594b63f98928
Author: bri3d <brian@brianledbetter.com>
Date:   Thu Sep 15 21:23:00 2022 -0600

    add JSON config support

* add fake HD to schema

* add ability to disable AU data overlay, add comments, cleanup

* add proper ipk deps and readme

Co-authored-by: Ben Lumley <ben@benlumley.co.uk>

---
## [philipl/mpv](https://github.com/philipl/mpv)@[a24fef6f90...](https://github.com/philipl/mpv/commit/a24fef6f909fe89fee03d5b7e71c0ea9c14816a2)
#### Wednesday 2022-09-21 20:25:35 by Philip Langdale

f_hwtransfer: get rid of the shit list

A few years ago, wm4 got sufficiently annoyed with how vaapi image
format support was being discovered that he flipped the table and
introduced the shit list (which just included vaapi) to hard-code the
set of supported formats.

While that might have been necessary at the time, I haven't been able
to find a situation where the true list of supported formats was unsafe
to use. We filter down the list based on what the vo reports - and the
vo is already doing a thorough testing of formats, and if a format
makes it through that gauntlet, it does actually work.

Interestingly, as far as I can tell, the hwdec_vaapi probing code was
already good enough at the time (also written by wm4), so perhaps the
key difference here is that the driver side of things has improved.

I dug into this because of the support for the 422/444 high bit depth
vaapi formats I added to ffmpeg. These are obviously not in the hard
coded list today, but they work fine.

Finally, although it's positioned as a vaapi thing, it's really just
Intel specific, as the AMD vaapi driver has never exposed support for
anything except the formats used by the decoder/encoder profiles.

---
## [fc1943s/The-Spiral-Language](https://github.com/fc1943s/The-Spiral-Language)@[e4b7b250d8...](https://github.com/fc1943s/The-Spiral-Language/commit/e4b7b250d88d06212331a1371bea344c82d97789)
#### Wednesday 2022-09-21 22:54:08 by Marko Grdinić

"1:20pm. Done with breakfast. Let me chill a bit and then I will start.

1:45pm. How tedious. I'd rather take a nap, but I need to keep going forward.

Let me see if I can do a bit more for the day.

$$$

(Simulacrum intro)

    In the endless darkness
    Roam endless monsters
    Pain, cold, flame
    Age, time, death
    Torment

    Light and shadow
    Holy and hell

    The inevitable fate of the Universe
    Will never touch
    The courage of the Inspired
    And the power of the Transcendi

I start Simulacrum for the first time and sink into the virtual, feeling the outside reality being pushed out from my being. The sensation is quite relaxing, like falling into slumber.

As I wait for the program to load the poem appears in my sense, sentence by sentence. At first I am struck by a vision of the primordial universe. I feel a sense of danger of living in it, and a sense of hopelessness. I then feel its grandeur, and am filled with admiration. And then I feel the determination of challenging the inevitable as I read the proclamation.

The introduction fades and the scene slowly manifests before me. Panning to the sky, highlighted in brilliant hues of light like a veil of gold covering it is a floating city. Against a backdrop of blue, it seemed like a distant object made of gold. I felt the sense of depth in my vision, so I could sense that the floating city was massive. Then I felt the warmth of the sun and the rustle of wind. I get the sense that I am high up and realize that I am literally floating in the air like a spirit. Though it is my first time experiencing this, I try moving my gravity defying body and have no trouble doing so. Observing the vast skies surrounding me, I look down. I notice the bustle and the humdrum of a modern metropolitan city. Skyscrapers dot the landscape and deep down below I can see cars and pedestrians walking the streets.

The vision seems very crisp and vivid. After a few moments of pondering, I realize why that is the case. In the real world I have to wear glasses so everything is blurry past a certain distance, but here I am unrestricted in my resolution. Just by focusing I can see for thousands of meters as if I was standing a foot away. Picking a random spot on the street, I can make out the minor cracks on the pavement, and the grime and the wear from people walking over it for many years. Dressed in autumn clothing, the people as they go along their life feel lifelike and real. I see them talking, exclaiming, laughing, being tired, downcast and otherwise broadcasting their emotions.

"..."

I found the whole scene very impressive. It did not seem like something that humans could create.

As soon as I start wondering how to start the game, a menu comes up in a separate sense. The Load Game option is grayed out, but Start Game and Quit are there, so I select the former and enter the Scenario Selector. Simulacrum itself rather than being a single game is an intelligent program capable of simulating a large range of scenarios. Browsing over the available scenarios, all of them seem interesting and I am having trouble deciding so I go back to the top and look at the recommended one.

Heaven's Key.

'The souls of those passed on enter the afterlife to play the grand game of cards that God has prepared for them. The second chance is given, and can be lost. Can you survive the challenges of your second life and go on to challenge the highest power there is?'

Along with that brief description, there is some setting information. When I focused on the 2d map of the world, to my surprise it unfolded to a 3d model that I could mentally rotate and zoom. I realized that the world of Heaven's Key was covered with orbital islands, much like the floating one in the intro. The tech level is similar to the current time in 2025, which is good since it probably means I won't have to play against non-humans. It is like the game anticipated what I would choose. The game seems to be responding to my desire, and it took into consideration my personal goals when doing scenario suggestions as well as the background which obviously has the Heaven's Key theme.

I think about it for a bit, and decide to go with the scenario being presented to me. The core hasn't steered me wrong yet, so I want to trust it. Having made my decision, I start the game and feel drawn into it.

(Heaven's Key intro)

    The method of recursive self improvement via iterated suicide can be used in reality. In fact, the technique represents the most viable path to getting superpowers in any kind of reality.
    - Loading Blurb

Whereas during the menu segment I had been a disembodied presence hovering thousands of feet above the cityscape, once the game started I found myself standing upright in an actual body. I gawked like a tourist, taking in the sights. I was in a golden city. The buildings and the streets were all painted in various hues of yellow, mostly on the lighter side, and there was slight gloss on the material giving it a sense of agelessness. Usually, as time wore down the material, it would begin to lose its luster, but everything around me seemed to be brand new and sparkling. Right now I was located near the edge of one of the floating cities, and as my gaze traveled towards its center, the buildings became taller and larger, from regular suburban houses close to where I was to large apartment blocks in the distance. The very middle of the island had a grand square building on an elevated platform. It had a spherical dome that took up a lot of its volume, and as I peered at it, I noticed it seemed to be radiating golden light. Though since it was midday the effect was drowned out by the light of the sun.

In the skies I noticed there were floating golden blocks in the shape of tiles, that also seemed to be showering the city in light.

I was near the edge of the city, and it seemed to be some kind of amusement park. I could see circus tents pitched up, stands of various kinds and even a rollercoaster and various other kinds of thrill rides I did not recognize.

Taking in the sights, I breathe in the air and find it to be cool and refreshing. I checked myself over. Though I could not see my face, but based on the touch as well as the composition of the rest, it seems that my real world body has been replicated in this virtual one. Which suited me fine, but it is surprising that I haven't been offered a chance to make my avatar.

Behind me, was the railing, also made of gold. Like the blocks and the grand building, it actually had some luminance to it. Drawn to that, I try touching it and find it to be smooth and lukewarm. It is not very tall, only up to my abdomen. It is only there to prevent somebody from sliding off the edge by accident rather than stop somebody who intentionally wanted to jump off.

Looking over the railing, I can see mountains and forests as well as the sea, and as I look below, I get a spell of dizziness that I quickly fight off. I am currently very high up, enough that I can see clouds below me. Directly below there is what appears to be a major metropolis. The high rise buildings and skyscrapers are like tiny, gray splotches at this distance.

An idea to try it ceases me, and I wonder whether I should take a dive over the railing?

[Gnosis check DC 1.9 Succeeded - Sample 2.03]

I grin mischievously. Yeah, let me try it. It is not like I can experience this in real life. As soon as I think that, nervousness and excitement flood my body, and I want to keep going. I grip the railing, and place one leg and then the other over it. Hands still clutching the rail behind me, I lean forward and take a good look down. A huge drop past the clouds welcomes me, into the metropolis below. I am putting a lot of strength into my arms to keep the certain doom at bay. I can feel my heart beating against my chest.

I wonder if I will hit the streets or the roof of one of the high rises?

A thought like that intensifies both my fear and excitement. Slowly I loosen my grip on the railing and start lifting my fingers, one by one. First I move the thumbs out of the way, then I let the pinky slide. Then the ring finger. I feel like a feather, perched in such a precarious position. The railing is so close to the edge that my feet are partly over it.

Time feels like it is slowing down for me. Very slowly, as if to prolong the moment, I release the index and middle.

"No, don't do it!" I hear a woman's voice yell out, but I couldn't care less.

I feel my body leaning forward and the gravity taking hold. I drop over the railing into the vastness below.

"AAAAAAAAHHHHH!!!" As I plunge, the fear overwhelms me and a scream rips itself from my throat. Strong winds buffet me from below in my fall.

After a minute or so, I manage to get a grip on myself so I can at least enjoy the scenery instead of falling around in panic. I keep reminding myself that this is not real despite what my senses are telling me. With the sun shining all around, it is quite beautiful. I take some time to appreciate the majesty of nature. I plunge through the clouds, feeling wetness on my face and hands. Soon, what used to be tiny splotches in the distance became larger and larger. The buildings below gain definition, and involuntarily, I imagine myself splattering on the street below. The fear that I had put a lid on, bursts out, more maddened and bloodcurdling than before.

"AAAAAAAAAAAHHHHHH!!!" I scream again, even though it is fake. Even though the world is fake, my brain cares little about those facts. It is so stupid and primitive, so all it can do is beg for dear life even if there is no need to.

Ahahahaha, it is so stupid, my brain is so stupid!

As I scream and piss myself in panic, at the back of my head, I can almost feel a voice mocking me for my stupidity.

I miss the height of one of the high rises, and reflected in the glass of the window nearby, I see my reflection for the first time. Exactly as in real life, but I see traces of tears around my eyes. I hadn't realized that I had started crying at some point.

"NOOOOO!!! LOG OUT!!! LOG OUT!!! LOG OUT!!!" Completely detached from rationality, the idea to exit the game before I smash the concrete takes hold. I grip it like a liferaft in the turbulent seas.

Ahahahaha! Seen from a different perspective, it is almost like a person scrambling for his life is an entirely different person from myself.

I am going to smash face first in the middle of a busy street. As soon as the ground floor is only a couple of feet away, I muster all my reserves of will and try to stop time. This has no effect and I hit the ground, feeling the darkness overtake me.

(Euclid's Room)

"Ah!" I jolted awake into reality and involuntarily, flop like fish on dry land once. Wiping my face, I feel myself drenched in sweat. I breathe heavily and feel that in my chest, my heart is overworking itself. As soon as I realize that I am in a safe place, I begin to calm down.

I lie back on the bed for 5 minutes, until my tremors have passed.

"Hah..." I exhale, savoring the experience.

That was...

[Gnosis gain: 0.3]

...Amazing! Since I died so quickly, I didn't experience any pain, leaving only the excitement. This will definitely be a memorable experience for me. Has a regular computer game ever let me feel something like this? I do not think so. The conflict between my rational part that understood the senses are not to be trusted, and my lizard brain which went into a blind panic is what really made this what it was. If I was purely cool or purely in a panic, it would not have been that interesting.

My brain is pretty stupid right now, but at least I can have some fun with that. I'll take it a bit easier next time and just explore the town. That seems like a good plan.

I want to see what the game is about.

(Heaven's Key, Perimeter of a floating city)

I dive into the game again, and take in the sights of the city of gold. Taking only a passing glance at the railing, I turn around and go into the city proper. As fun as that experience was, I do not want to spend my entire day diving off the edge. Gawking like a tourist as I stroll around, I get a stock of the place. Near the frontier where I was, the density of buildings was low, so amongst the houses as if to spur business a lively entertainment sector was built. I could see circus tents, restaurants, stages as well as casinos. There seemed to be a lot of people enjoying themselves, though I wouldn't say it was packed. I found the city plan somewhat peculiar. There were roads for example, but no cars, and I could only see people using their own legs as far as I looked. The regular houses made sense, but other entertainment related facilities seemed to be built in the middle of roads and at intersections. Overall, it felt like the city itself was molded based on some template, and then patched up to fit a need by the people actually living here without modifying the underlying template itself.

It is a lively and cheerful place. It wasn't jam packed with people, but I could see a decent amount of them going about their business and chattering. The way they were dressed did not seem to be that much different than in the real world. Looking around, I could see old and young people, both male and female, but no kids which I'd expect would be unusual for an amusement park such as this. I think that I'd be in the youngest age cohort relative to the population here.

"Waiters wanted - 3,450/month"
"Can you make great pizza? Apply here. 3,600/month"
"Have a flair for entertainment? Comedy, magic, singing, musical instruments. 3,800/month"

While walking around I saw a bunch of job ads posted outside the relevant venues for waiters, cooks and attendants. The typical salary for these kinds of service jobs seems to be around 3,500 chips, whatever those are.

Getting bored of walking around, I pick a restaurant at random and take one of the outside seats. With the sun shining down on me, the weather is warm and pleasant, simply ideal. Given how up we are you'd expect it would be freezing, but normal rules do not seem to apply here. I pick up the menu, and take a look.

"Beer - 20"
"Iced Tea - 20"
"Pizza Margherita - 40"
"Cheese Burger - 30"
...

I want to order some of these. I've never tried eating in VR yet, so I am curious about what it tastes like.

"Hello sir, what would you like?" A waiter came around to take my order. I cringe inwardly.

"Just water." I have no choice, I do not have any money to pay for anything here.

"Got it."

While I was waiting, a person came up to my table and initiated conversation.

"Hello, do you mind if I take seat here?" She asked, smiling at me. I took a good look at the young woman in front of me. Wearing a headband with what looked to be 4 brown roses, she seemed to be of asiatic descent. Her face was cute and friendly. Short dark hair. She was wearing a finely made brown blouse with long sleeves, and a miniskirt plus thigh stockings.

"Sure." An event like this would never have happened to me in real life, so I was curious where this was heading.

"Nice to meet you, I am Lily."

"Euclid."

"An exotic name. Are you new to this city?"

I think about lying for a moment, but I have no reason to. I am certainly not going to try to show off here, I am penniless anyway.

"Yeah, I just got here." I admitted.

"I am sorry for your loss." She frowned, confusing me. "But look on the bright side." Her expression cheered up, spreading her arms. "Here in this afterlife, it is quite fun. You are going to like it."

At first I was confused, but as soon as she mentioned the afterlife, a thread of inspiration came to me. I remember the description and guess at what she meant. I've been thinking about this as just another place, but maybe the people here all died on Earth before being transported into the city. My character does not have a background so it slipped my mind.

"Yeah, it does seem like a lively place." I agree. "Maybe I'll be here for a while."

This gets a smile out of her. At that point the waiter came to our table, placed the glass of water that I ordered on my side and turned to take any further orders.

"Coffee please."

"Yes. Anything else sir, lady?"

"No, that will be all." I take the glass and take a sip of water. It is nice and refreshing. He leaves. I raise an eyebrow to Lily. "I would have liked some iced tea, but pft." I pucker my lips for emphasis. "No money."

"Ahahaha!" She waves it away. "If you've just got here, then you should have a 100 chips. Try bringing them out."

"Huh? How?" I start checking my pockets stupidly.

"Just focus." As I look at her, several stacks of translucent chips manifest in the air behind her. The thousands of chips in her pile look like they are intended for poker. Standing on nothing but air, I could see through them due to their translucency. "Then once they are staged, you can withdraw by wishing for it. For example, here I'll wish to get 20."

She raises her hand above the table, and like a magic trick, I see 20 chips moving into place. She lifts her hand and I see that the pile is no longer translucent. She lifts one, shows it to me and places it down with a clack.

"So it is like that? How do I do that?"

"Just try it."

Having an example of what I should do, I focus inwardly and I discover a sense that wasn't there before. Right in my mind I could see a stack of 100 chips. It feels different from just imagining it, like they are actually there.

"Yeah, good. I can see them behind you." She encouraged me.

Imitating her, I tried lifting my hand on the table and drawing them out from inside my sense. To my surprise it works and I can see the chips sliding into place. Lifting my hand, I count them. Feeling them out they are cold and slender to the touch.

"This is interesting. I guess I can order that iced tea. How do I bring them back?"

Lily did a little wave and the chips on her own side vanished. "As long as they are in your possession, even if they are away from you, you'll be able to recall them from anywhere. It is impossible to throw them away, you have to transfer ownership instead."

I wasn't sure how to do it, but I gave it a try and it worked. It seems that in VR, things just work.

"Bravo." Congratulating me, she opened a pack of sugar and added it to her coffee. With a spoon she started stirring it inside the liquid.

[Externus check DC 3.5 Failed - Sample 2.28]

I consider not ordering iced tea like I said I would, but that would be an asshole move. I can't see any reason to be stingy here. A part of me expected the chips to be important, but then I think about the job ads, the people going around me, Lily's own large stack and her placing her own order without issue. Nobody else as far as I can see has issue spending money. I guess 100 chips is not that much. I really meant to gamble with them rather than spend them like this, but I can always reload.

That would lose the connection with Lily though. Rather than working at a job, maybe I could get a loan and gamble with it? Since I can save and reload, I am in no danger of ever going bust unlike the NPCs.

I mean, I am not going to seriously do waitering for an entire month just to get the money to gambol. I want to get better at cards and learn some skills that would benefit me in real life.

So far, the NPCs here feel very lifelike, not at all like in a computer game made by humans. I take a look at Lily who is taking a sip of her coffee, with the pinky out. Cute, she is very cute. I can't believe that I, of all people, am getting charmed.

(Date with Lily)

I spent some time with her in that restaurant just chatting.

"I am working as a guide. If you want I'll show you around the city and get you accomodated. It would not be good if night falls and you have nowhere to sleep."

"Yeah, it would be bad if I had to sleep on the street once night falls."

“Yes, it would. Could you show me a cheap place to rent somewhere, first? After that I’d like to see what this town has to offer.”

“Of course.” She replied enthusiastically.

With that, the date started.

...

I spent some time touring the city with Lily. Lily is pretty cute, so I was a bit smitten by her, but I got tired of that after an hour. After that boredom started to kick in for me. Seriously, who cares about NPC women? She is cute, but I should be able to generate people like her by the million with a push of a button. I am not going to get sucked into the pace of things and let her become a part of my motivation for logging into Heaven's Key. How pathetic would that be?

With that mindset in place, instead of chatting about whatever comes to mind, I steer the conversation towards the city in general. Who are the big shots? What is life like? What are the challenges?

Goals like that are the only things preventing me from getting bored out of my skull. Back in school, there were times I went on an excursion with the rest of the class. Somehow those experiences ended up even more boring than going to class itself, if that is possible.

'Wow, look at the golden buildings! So cool!' I picture some wojaks pointing at the stuff in the background.

I got tired of it after 15 minutes.

Right now, I am acting like I think a normal person should act, but it is really straining my nerves. It is somewhat disgusting.

...

"WAAAAAAAAAAAHHHH!!!" Roller coaster rides rock! Seated in my coaster, being hurled through the air at high velocity! Based!

I was screaming, Lily was screaming next to me, the rest of the people in the wild ride were screaming!

This is more to my liking!

...

A whiff of barbecue drew me and I got a skewer for both me and Lily.

"Here you go!" A kindly man smiled at me, handing me my meat on a stick. I grab a bite and feel the spicy, juicy taste of meat spread through my mouth. The taste is just like in real life. Delicious!

I think I am starting to get a hang of how dating should work. Things are boring when you just let the other person take the lead. It became fun once I started drilling Lily for info on the town and dragged her into the roller coaster rides. It has been a few hours, both in the game and real life. I want to start getting to the point.

Me and Lily both finish our food, drink some colas, and then I get to the point.

"Lily, I was wondering." I manifest a poker chip between my index and middle finger waving it in front of me for emphasis. "These chips all look like they are made for gambling. So I am guessing they should have something with that."

I was expecting to hear something on the subject of card gambling from Lily, but for some reason nothing came up. I didn't care enough to push it back then, but now it is time to get to the point. I already know the theme of the game has something to do with gambling, so it is strange that I haven't heard anything about it from Lily.

"Who knows. The god who brought us all to this city made it like that. Nobody knows what goes through his mind." She shrugged.

Evading again, are you? Just what is the point of that? Do you really not know?

"Instead of just walking around town, why don't we go to a casino? I'd like to try playing some cards. You too Lily. Isn't it boring just going around town? I want more action like those roller coasters."

"Well..." She fell in thought. "Okay, I know a place, let's go there" She beamed, showing her expertise at maintaining positive energy. If I let her take the lead, she will just bore me to death, but I am sure that as a guide she is obligated to fulfill my wishes.

(Raven's Eye Casino)

She led us a few dozen blocks away, deeper into the city. There were a lot of people in the initial blocks, but I could only see a few people on the streets as we ventured deeper. They were much quieter than the area behind us. I thought this was weird. Usually, cities have dense crowds compared to the countryside. Do the people here spend all their time partying at amusement parks? That can't be. Rather...

"We are here." She announced, cutting off my line of thought. Her positive energy from before seemed subdued, and I sensed she was somewhat on the edge.

"Great. Let us have some fun. I do not remember anything from my past life, but I must have been a card shark." I announce, striding into the place ahead of her in search of stimulus. I spot the receptionist, slam 20 chips on the counter and say to the startled receptionist. "I want to play Texas Holdem. Lead me to the table."

"Come this way, sir." She got up from her seat at the counter and led the way deeper inside.

Passing by the rows of slot machines, I noticed the screens had dust on them. For some reason, slots, the staple of casinos, seemed to not be popular in this place. Much like outside, I couldn't see any people here. It was a quiet place. We went up a set of stairs into a game room.

It was a spacious room, with numerous tables, most of which were unoccupied. But there were a couple of groups playing cards, or rather just enjoying drinks there. I picked a table with 4 people, and walked up to it. Lily followed alongside me.

Now, my plan was to try to join a tournament that had a low buyin, or find a place where I could exchange for fake chips. Given how large the monthly salaries are here, I expected that with just 20 chips, I could at the minimum find a game with 1/2 blinds. This would leave me greatly short stacked. I thought about this for a bit on the way here, and I've concluded there is no real need to be fair. On one hand, I want to learn how to gamble, but either way, I am not going to spend a month of real time wage slaving in a video game. What I'll do is just save on every hand and reload if I lose it. That should allow me to escape my shoe string budget and get to the point where I can gamble seriously.

Looking around, I do not have much choice when it comes to game selection, I'll have to take whatever I can get. Since Lily led me here, the stakes should be fine. She knows my money situation, so she would not lead me to a place where the min stakes are 10/20 or something like that.

Since the next encounter will be sensitive, I try saving. Save. As soon as that thought leaves me, a window pops up. I name the save 'First game' and apply it.

Now I am set, if I lose I'll just go back to this point until I get it right. Whereas previously I had some nervousness about having to get a job if I lost, it completely deflated and I just felt the excitement of trying out gambling for the first time in a real casino.

"Hi, mind if we join?" I sit at the table and start the conversation like that. Apart from me and Lily, there are 4 guys at the table. One was a thin guy that seemed to be in his 20s, wearing a baseball cap backwards, while the others were in their 30s and 40s. The older guys were somewhat fat and had protruding guts. One of them was bald. They seemed to be dressed casually and felt right at home at the table.

"Sure." The bald guy in his 40s replied. It didn't seem like the rest of them were against it either.

I looked around, but I could not see a dealer. Before I arrived, these guys were just having beer and chilling at the table.

"So what are the stakes here? I only have 20 chips, if that is fine with you gentlemen." I made some small talk. I did a quick scan for the dealer again. Not only this table, none of the other tables had dealers either. I couldn't see a deck at the table.

"We typically play for a single chip per tourney."

"So it is a casual thing between friends? That is good. I was worried I would have to play 10bb deep in a cash game." I remarked. "We'll wait until you guys finish your drinks. I wonder why there aren't any dealers here?" I asked. The bald guy raised his eyebrows and looked at my partner.

"He is a new arrival. I haven't registered him as a citizen yet." She shook her head. Rough. Everyone is new at some point. The man shrugged his shoulders and leaned forward a bit, getting more serious.

"There is no need to wait, we'll start right away." He looked at the rest for confirmation and they nodded in return.

"Great! Should I go call for a dealer?" At my suggestion, the thin guy with a baseball cap had to stifle his laughter.

"No, that is not how it works. First we put the chips on the table." He placed a hand just above the table, and after he raised it, I could see a small stack of 20 poker chips manifested there. The rest of them follow his lead and do the same. Next to me, I could see Lily also doing the same. Eager to raise the stakes? That suits me just perfectly.

Seeing that the table is set, he continued. "Then I propose a duel, and you accept. Duel?" He said to the table.

"Accept."
"Accept."
"Accept." The 3 guys next to him confirmed.
"Accept." Lily went in lockstep with the group. All the eyes at the table were on me.
"Accept." I manifest 20 of my own chips, on the table and confirm, curious as to what would happen.

The world around me changes.

(The shadow realm)

Seated at the table, I didn't feel any physical force on my body as the environment transformed. Whereas previously we were in a large game room on the second floor of the casino, once I accepted the duel, the space around us warped. It felt like we're floating in space, surrounded by blue nebulas. At first I thought I could see stars, but then I realized they were too big for that. They appeared more like shards with yellow rims. It was a mythical space, removed from common sense. I felt out with my feet, and realized that even though it seemed like a sheer drop, there was solid grounds beneath me. I looked below and I couldn't really see what I was stepping on, but pressing on it felt solid. Thinking about it for a few moments, I realized it made sense that there would be some mechanism to prevent me from accidentally falling to my death if I left the seat. The chairs can’t be literally floating in the air, maybe they are standing on something like pure translucent glass?

All in all, I think I am getting used to this rather quickly.

I felt something moving and when I looked in front I saw that two face down cards were dealt to me, along with a button. Next them is a stack of 100 chips.

I seem to be in last place with Lily behind me. The group was seated as we were originally. I wonder if I am on the button because I was the last to accept?

"The rules are Texas Holdem. You have 5 minutes to make your decision otherwise it will be an auto-fold. The blinds double every 3 revolutions of the button in a 6-man game, meaning 18 hands from now. Is that clear, kid?" The bald man explained, watching me intently.

"Yes." I reach for my cards, and take a peek at them by twisting them upwards a little. I saw that in videos of real life poker games. The cards are nice and smooth to the touch, with a golden tint rather than the usual browns used in vanilla packs.

3s 7h. Crap hand.

The guy in the cap to the next to me in the small blind raises to 6, the big blind folds. The guy next to him raises to 20. The bald guy thinks about it for a few moments and follows up by raising to 50. Right behind me, Lily bows out of the action, and it is my turn to decide. I really have no reason to get involved in this hand.

[Gnosis check DC 1.8 Succeeded - Sampled 2.69]

"All in." Huh? Eh, whatever. Surprised at my own decision, I pushed in the stack causing it to topple over. The chips make satisfying sounds as they clank against each other. It would be best if the other guys just folded. The first two guys do so, tossing their cards into the middle. They vanish before coming to a stop.

Now it is just the bald guy and me. I keep my poker face as I watch him make a decision. He drums his fingers for a quarter of a minute as he observes me, takes a breath and then calls. "Call." He pushes his stack.

As I watch, by some invisible force, both our hands are flipped. He sees my hand, does a double take, and I see him holding Kc Kh.

From somewhere the cards appear on the table.

5h Ks 6d is the Flop. I don't care much about this hand, but I see his fist clench. He has trip kings now, and my only chance of winning is if the 4 gets dealt to give me a straight. My odds of getting that are about 4 in 45, about 11%.

The whole table is invested in the game now and holding its breath as the turn gets dealt.

A 9d. A miss. I have one more chance. Observing other people's reactions I see them leaning in slightly.

With bated breath, the next card comes in.

4c. I won. The bald guy makes a sour expression. I'd expect him to be mad at me, but not sparing a thought for me, I see him stealing a glance at Lily before he vanishes from the table completely. Having lost all his chips, he no longer needs to be present so the system aborted him.

As that happens the chips flow into my stack towering above the rest at 228. Nice!

"That was crazy, kid. I can't believe you went in with 37." One of the older guys who was num up to now said.
"I got a feeling." I nod knowingly, playing with my chip pile all the while.

The guy purses his lips, thinking of replying, but then thinks better of it. While that was going on the next hand started.

I won't go into detail as to how the rest of the game proceeded. Riding a wave of beginner's luck, I've been getting good hands and playing them aggressively, trying to get as many chips off them as I could, busting the rest of the table in only a couple dozen rounds.

(Raven's Casino, poker table)

After winning the game, I checked my chip pile and found it has grown to 60, tripling my balance.

"I won. Hey Lily, how much is the rake here?" I asked her. She shook her head.

"No rake. The casino doesn't take anything for duels." My eyebrows rose.

"Really?" I looked at the rest.

"Yeah..." The old guy nodded. This brought up a few questions in me such as what the distribution of winnings is like and why isn't there any rake? If that was true, how did the casino function? But I left those aside for the time being.

I manifested my whole pile and pushed it in, causing the thin guy's jaw to drop. "That is good to know. Let us continue. Duel?" The group looked at each other and then at Lily. Lightly, she nodded and pushed 60 of her own chips in after manifesting them. Way to go Lily! The guys seem to be following her lead for some reason.

"Accept."

"Accept." "Accept." "Accept." The rest followed in lockstep.

Back in the shadow realm, the action began again. I had no trouble hitting the board, and bluffing when I missed so I won again with no trouble. Back at the poker table, I saw the thin guy wiping the sweat off his face. He only lost like 80 chips, this is less than what a waiter makes in a day, what a weakling of a gambler. He should just get a job instead of wasting his time on a poker table if that worries him so much.

I save the game at this point, manifest my pile and push 180 chips in. "Duel?" I announce.

"Hey Dale..." A lot more reluctant now, the thin guy looked towards the bald guy who seemed to be the most experienced of the group. The bald guy, Dale, pursed his lips and deliberated for a moment, before refusing.

"Sorry, we are just a casual group. How about we keep it 60?" He asked. Not seeing a reason to keep being pushy and wanting to play more, I acceded to his request. I made the pile of 60 chips and asked to duel once again. Having won two games riding a wave of luck, the group seemed to be afraid of me, perhaps wondering if they were being hustled.

Back in the shadow realm, they started to tighten up and tried to pick me off with stronger hands. My luck started to wane and I had a harder time winning. We played a couple of games like that for a few hours, and I ended the day at 240 chips. I could have won a lot more had I abused my ability to save and reload, but I was satisfied with not dropping below 180. It wasn't my goal to win every single time, that would be suspicious.

I had to win the first and the second time to get out of red, but after that it was gravy. Rather than these noobs, I should seek out richer people to play against.

I had some fun game time. Saying goodbye to the group, me and Lily left. By that time, I saw the sun had gone down. We made our way back to the inn where I rented a room for a week.

"Do you want to come in for dinner? I'll treat you." I asked Lily, my hand on the handle of the door to the inn.

"Sorry, I have an appointment at a different place." She politely declined, before getting down to business. "I will have to charge you for today's tour though. 300 chips."

"That is quite expensive!" My hair rose. "It would clean me out. Er, do you mind waiting for a bit before I can pay you back? What will I eat tomorrow if I give you everything I have today."

"The inn will provide you meals, but don't worry the people here don't need to eat physical food anyway." She explained. "I know that 300 seems like a lot, and indeed, those who have just arrived can't afford it. In return, the guides take what they have and in return get them employment. I actually don't take this money for myself, but am officially employed by the city to welcome newcomers. It is merely a matter of policy."

"What happens if I don't pay right now?" I asked.

"I'll put it on your tab, but if you can't pay me in 3 days and are still unemployed, by law you'll be sent to jail."

"Vicious!" I exclaimed, startled. Lily made a sour face.

"Yeah, it sucks. This is because the city gets newcomers out of thin air, and to prevent them from just loitering in the streets, this policy has been instituted." She shrugged, sympathizing with me. "Don't worry, I'll come back tomorrow and look for a job with you. Once you have that it will take you only two days of work to make it up."

[Gnosis check DC 2.9 Failed - Sampled 2.18]

Hmmm...

[Gnosis check DC 1.7 Succeeded - Sampled 1.93]

What she is saying makes sense, but there is something off to this story. Not really understanding what the problem is, I do the most reasonable thing and save the game.

After that, with a shake of my head, I just decide to do it and see where this choice leads to. I call up my entire pile in its ghostly form and offer the floating chips.

"Here. You'll be here tomorrow to help me look for a job, right? Promise?" I query, offering her the chips.

"Of course, don't worry." With a sweet voice, she coaxes me, taking the offered chips. Without a sound they are transferred into her own ghostly pile. Not saying anything else, she turns around and leaves the scene. Behind her, I was no longer there. There was only the dark, empty street leading into the inn. The door that I had opened was slightly ajar where I left it, leaking a trail of light from the inside.

As soon as the transaction was complete, I felt my consciousness being wrenched from the world and into the abyss where there was nothing. A single window popped up to inform me of what happened.

> You died.

$$$

4:05pm. > You died.

This is the ideal spot to end the chapter on. This will make a perfect lead into the next chapter where I'll put the Heaven's Key poem. Let me grammar check it.

4:10pm. Damn it, is my neck stiff. I must have pulled it at some point two nights ago.

4:25pm. 16 pages. 7.4k words. Right now I should be like something like 17.4k words for the 4 chapters that I have written. I think 40 pages is enough to start off the publication on something like RR.

4:30pm. I won't hurry this too much. Let me register for an account first. I am done for today with writing and won't resume until I've published the first chapters. I'll also want to open a Patreon before I open the new ones.

4:40pm. Made an account.

> To submit your fiction, both the fiction information and the first chapter or prologue are required. After that, your submission will be inspected by our system and one of the staff members.

> If you have already posted your story elsewhere, be aware that we will require proof of content ownership. You can already submit a support ticket with it to speed up the process. Accepted proofs include editing your existing description on the site you've posted your story on the earliest, or an official document marking you as the author. We may also accept an email from a known email address of the copyright holder (i.e. published on the official website or in print in the book) as valid proof of ownership. Images are not accepted as proof.

> If you are making a support ticket ahead of time, please include link(s) to any pages that have the edited description to make the process faster.

4:55pm. It seems the system will crop the cover mightily.

How do I insert the image. Nevermind that for now.

Genre: Psychological, Sci-fi, Adventure
Tags: LitRPG, Soft Sci-fi, Virtual Reality, Artificial Intelligence, Male Lead, Mythos, Non-Human Lead, Progression, Technologically Engineered, Villanous Lead
Content Warning: Traumatising Content

The old arc sure traumatized me.

Synopsis: A story of playing a game in the post-Singularity era.

How do I add to that?

> A story of playing a game of poker in the post-Singularity era.

I've thought about the synopsis before, but never got far from this first sentence. I am not really sure how to summarize Heaven's Key. I guess I'll have to put some effort into it. I am going to take this task seriously, as the synopsis is the first thing the user sees. Though just leaving a single sentence like this if I cannot think of anything better is not too bad, I want to give it a serious try first. I am not in a hurry to publish this.

5:05pm. Let me take a break here.

I'll take a nap, to think about it for a while.

5:55pm. Done with lunch.

> A story of the search for power and self optimization in the post-Singularity era through the play of games.

Agh, I'll submit it tomorrow. I want to roll around in my mind how the perfect synopsis should be. Also the way paragraphs work in RR is different from this document so the gaps are too big. I need to fix that kind of issue. Maybe I could fix that indirectly, via some setting. It would be strange if something like that did not exist. The text options in RR are pretty rich.

> What could a single person do if an nearly limitlessly powerful computer was accessible to him? And what would the challenge is unleashing the power of such a device be?

> Master the chips and cards.

6:05pm. Let me close here. I'll somehow compose a proper synopsis tomorrow after thinking how the elements should come together."

---
## [fc1943s/The-Spiral-Language](https://github.com/fc1943s/The-Spiral-Language)@[d364577827...](https://github.com/fc1943s/The-Spiral-Language/commit/d364577827c5aed60419705ff1148988b33249c4)
#### Wednesday 2022-09-21 22:54:08 by Marko Grdinić

"12:10pm. I think at this rate, the Singularity won't happen even by 2045. Maybe it is my personal circumstances that are making me biased, but you'd expect the situation to be more in my favor if the Singularity really was destined to be. My latest attempt of offering to make the Spiral backend for Tenstorrent chips has had the reception of a roadkill. It feels like it is a dead creature in the middle of the road while the people there toe around it.

Some dramatic hardware breakthrough to fulfil the promise of memristors in the previous decade is necessary to make me more optimistic. Right now it is not even on the horizon for me. Once it happens, how long would it take to put into production. Half a decade most likely.

12:20pm. I do not know what the right choice is here. Suppose I had advance knowledge telling me the Singularity will never arrive in my lifetime.

I'd probably just be a writer then and spend my life in this room playing games and reading manga. If I could get an advanced piece of hardware, then I would not have wasted time. I'd get any job, I'd even accept the 2.5k offer like the one by Zenna just to get my hands on it.

Right now the AI chips are weird. They are kind of weak and behind GPUs, being hawked only to rich people and hard to get ahold of, as well as difficult to program.

12:25pm. That I did not accept the 2.5k/month offer by Zenna, is that not proof enough that I do not believe in them?

12:30pm. The role I took upon myself is that of a pursuer, but once I stopped believing, it became a burden. I needed to believe, but I could only put on an act.

Imagine if I had the option of getting a local job for something like 1k/month. I could work for 2 months and then have the option of buying an AI chip costing 2k. If I had that 2k, I absolutely wouldn't spend it on something like AI chips. Right now it feels like it would be a complete waste of money.

For something like a brain core from the story, the amount of effort I would put in to get it would have no limit. Even if I had to work 2 years washing dishes, I would do it just to get it without any hesitation.

12:35pm. I need something to sweeten the pot for me. Maybe some algorithmic discovery. Some new insights. Just having a mediocre step up in hardware would not be enough to really fire me up.

Having Spiral be adopted by a company like Tenstorrent, and even having it sponsor its development and my own projects would be cool, but it is secondary to what I need to do.

I need something to give me a leg up on RL.

Having the hardware itself infer its own learning algorithm might be completely viable on the brain core, but the current day AI chips are likely to fall short.

12:45pm. As I write the story, I need to keep in mind that the approaches the Inspired could take on their limitless computer are not the same as the ones I have myself on my shoestring budget.

12:55pm. My mind states is starting to go in a negative direction. Let me try writing some more. Forget ML and programming those useless pits of time and money.

2:45pm. I have a bit over 3 pages written now. It is time for the third Dream.

2:55pm. If the defining scene of the old series was Ixis' battle against the self, the defining scene of the new series will be the third Dream.

3pm. Ah, let me give it a try. There is no point is just hanging here. I'll take a proper break after I write it. There is no rule that I have to write till 6pm like when I was programming.

3:55pm. I think this came out pretty well. I said everything I wanted to say and nothing more. In the Hell arc of old Simulacrum, I was actually so touched that I described the self improvement loop as salvation, but then thought better of it because I did not want to bring in religious conotations into it.

But now I feel that maybe justice is too great of a concept to be carried by humans. It can only ever shackle them in place. The way the universe could be they way I want it to be is if the Lord of Nightmares makes it so. If that is not the case, I can only resolve myself to become such a figure. But there is not much I can do without resources. I thought that I would get them if I simply continued moving forward, but the shackles called justice prevent me from doing so.

4pm. Me writing this story is just a way of attacking those shackles, in the only way I know how.

Let me put this into Docs. How far along am I now? A bit over 4 pages.

Let fix the errors.

4:15pm. Seems decent. I just went through it using the Docs. I need to proofread it. But, I am sure that people on Royal Road will point out mistakes when I publish it. Well, assuming I get any readers at all for this kind of story. That is the risk.

4:30pm. The amount I have written today is quite good. Counting the bad end, it probably comes down to almost 5 full pages. A single day of writing will not amount of much, but a full year of making such progress every day can result in a lot of material.

Oh right. I accidentally overwrote the commited entry in the journal.

$$$

(At school)

As the professor rambles on some useless physics topic, I am gripped by his words. Today's session is quite enjoyable. I brought the core along with me to school and used it to fine tune my emotional state so I can be immersed into what would otherwise be boring, rambling lectures. Like yesterday, I ended up tuning out my classmates again, but that does not matter. This kind of satisfaction...

Yes, I feel like I am on the right path in life. I understand that what I am essentially doing is brainwashing myself and playing myself like I would a character in a game.

Maybe there is an argument to be made that this is wrong, but...

I throw a brief glance behind me at my classmates. I didn't pay attention to the seating order and somehow ended up in the front seat of all the classes. I see that half of them are not focused on the lecture. The rest are trying to make an effort, but it does not change the fact that you really need to believe that the school is not scamming you out of your time in order to fully invest yourself into learning. What I am doing here is really grand in a way. I am fully immersed into learning despite accepting the pointlessness of it.

If I went to this place just to drain my time, it would be nothing more than slow torture.

I won't give up this power. With this power, I will never have to endure boredom again in my life.

I do not think my grades will ever be a problem again.

(Euclid's Room)

I am back in my battle station. Today's school session was the best ever, all thanks to this tiny little thing!

Grinning, I raise the brain core to throw a spotlight on it.

All I have been doing is some lightweight tuning using a provided tool. If I digitized myself, I could edit my mind's program directly and advance further on the proper path of a programmer. But it is unfortunate, that all intelligence augmentation methods are iterative suicide. Not to mention, digitizing myself either involves copying myself to a core or converting my brain to one.

[Pathos check DC ?? Failed]

Copying myself would allow the digitized copy of me to self improve, but I'd be the same as I am now. Doing a full brain conversion is just swapping my brain matter for computronium, either of these is not lossless so it would be a mental trick that hides my own death away from me. It might be worth going through it regardless, but what is the rush? Just being able to tune myself properly into the study material is worth 50 IQ points on its own.

I should treasure what I have.

So what should I do next?

I spent some time thinking about it. Should I try out the VR games? Hmmmm...no. I finally have the power to play my life properly, so why waste it on things that would not give me real world benefits? Now that my homework is as fun as anything else, why not immerse myself into that?

Through my mind, visions of parallel lives flow past without the core. I can easily imagine myself living from day to day in boredom and tedium, playing games to have fun. There would be a conflict between society and me due to my distrust towards it. It is not that games would have been an escape. I would have played them because I would have had belief in technology, but it would have been vague, indefinite belief in the potential of it.

Right now things are very clear. The manifestation of the potential of technology is not a bigger time suck, but this thing right here. I roll the core in my fingers for emphasis. It is the ability to program my own mind, so I should thank the millennia of scientists and engineers who have made it possible by doing my schoolwork with the rightest mindset and attitude possible.

That is what I feel like doing now and so I shall.

That night I Dreamed again.

~~~

It was like watching a black and white cartoon made of stills. As the image zoomed out, I saw a man's face with a confident grin coming into perspective. He was wearing neat and tidy, if old fashion clothing. A spitting image of a young professional. He was on a great big stage made just for him. He was going forward towards the light. And some distance away from him was the darkness and the shadows.

In them I could see people on their knees as if they were defeated, not daring to look up.

The short cartoon ended and the defeated figures were replaced by the golden ones from the previous night's dream. They were upright and staring ahead. Yesterday it was murky, but now at the edge of my vision I thought I could see light.

"Justice, where is the justice?" They lamented in a booming voice.
"We want to go forward, but we can't. What about desire, what about will? Why does the world not respect it?"
"We want to go forward and overcome! Where is the justice?"

As if the winners finally took note of the losers, they turned around and responded to the golden figures.

"You talk about justice, but put yourselves in our position." The black and white cartoon stills of the winners responded, staring down at them from above.
"I worked hard for my success." A cartoon still of a man who looked like a scientist came to one of the golden figures. "Have you spent even a third of as much time and effort as I have?"
"My wealth was the accumulation of decades." An older, but fit man who was finely dressed responded. I could see that in the background of his still there was a mountain of gold coins and treasure, as well as stacks of bills. He came closer. "What right do you have to covet it? How would it be justice if you could get it so easily?"
"My body is the result of half a decade of practice." I could see the bulging muscles on the still of a man in a skin suit who looked like a bodybuilder. He confided in an aspirant. "You might have put in the effort, but it is not our fault you could not achieve the result you sought."
"My beauty and the adoration I receive for it is not something I worked for." A young, beautiful woman admitted. She descended to a group. "But you understand, don't you? It is not something you can take."

After those brief personal reproaches, the stills of the winners were staring down from high above.

"You talk about justice. And you dream about being above others. Talent, wealth, beauty, intelligence, strength..." The winners enumerated as if chastising them, their voice booming through the darkness of the abyss as the golden figures listened on in silence.
"You talk about justice, while seeking inequality like hypocrites. You desire an unequal world where you have all the opportunities and advantages to rise to the top."
"You found such an unequal world where the possibility for that is there and you live in it. The justice that you sought is something that you've had all along."
"The world you live in is fair to the winners."

Leaving that last comment behind them, I could see the winners leave the scene. The golden figures stood there in silence.

~~~

(At School)

Wednesday is another wonderful day to be at school! The professors ramble on about useless bullshit and I absorb it all like a sponge. I am getting used to externally controlling my emotions. It won't be long before I am a master at controlling my own brain. I feel like I am completely set. That having said, what do I do about that other thing that I did not want to think about? School is something that I am completed to go to if only to put on a show for my parents. But what line should I take for the dull and uninspiring NPCs that are my classmates?

[Externus check DC ?? Succeeded]

My original plan was to ignore them, and that is good. Truth be told, I was afraid of getting isolated and becoming alone, but now that I've experienced the power of mind controlling myself, I can safely say that much like boredom, I will never experience loneliness unless I explicitly will it.

I think about it more in depth and summarize the reasons.

There isn't a single good reason to have friends in school that I can think of. There are some minor benefits not worth mentioning. In addition, stuck up loners tend to get bullied, but that would be a problem only to those of weak heart rather than masters of emotion such as myself. The disadvantages of having friends are huge, namely they would be a drain on my time. Imagine I get back from school, but at the same time have friends. They could call me up. They might want to spend time with me. In other words, they'd take my valuable self-development time and just waste it. They are worse than parasites. At least summer mosquitoes drink your blood and then leave. Friends would be sucking your time all the year round! The less I have of them the better.

Even worse than having friends, the absolute worst that could happen to me in high school is getting a girlfriend! Friends have the potential to at least contribute something to me in theory, but having a woman might even require me to have a job to cater to her. It would be like willingly becoming a slave for some hole. Even worse, imagine the damage she could do if I accidentally got her pregnant. Ohhh, God! She'd have the option of getting half my income for life! And if I couldn't pay the monthly minimum I'd be forced to go to jail! I'd have to be retarded to get into that kind of deal.

The best plan is to keep my social status low. That would be the best defense against the female interest.

I will live by maximizing power and minimizing sex!

Based.

At this point, my emotions have started running hot and I've stopped paying attention to the class, so I demonstrate my exquisite emotional mastery by giving mental command to the core stashed away in my backpack. I run the program to normalize my emotional state to the optimum level and get back to work.

(Euclid's Room)

Lying on the bed in my room, I think in silence.

Using external influences to control my emotions has somewhat separated me from the rest of humanity, and according to the guide I read online, to counter the negative aspects of that it is a good idea to brainstorm and visualize possible avenues my life can take explicitly. Ordinary people can manage doing just what feels right, but if I went with that I'd just study all day without sense or reason to it. I have the option of making whatever I want feel right, so looking into my emotions for answers is no longer a great way of deciding on my future. Instead I have to make use of my reason. I've decided to throw out my heart, so the only choice is to pursue power. This is the only goal that can ground me in reality.

I dig out the core from my pocket and spare a glance at it.

If I want power, the only choice is to follow the example of, well, fictional characters, and upload myself to this. Being able to control my emotions like this is a great benefit, but increasing the computational and memory capacity of my brain by a billion quadrillions is nothing to scoff at. Instead of relying on some app to manage my mind, I'll have to get really good at programming to draw out the true power of the brain core. Merely uploading myself does not mean my mind will be able to use the extra capacity. Nature hasn't designed humans so their minds could be transferred to a different substrate. I'll have to do it from the ground up and learn how a mind really works.

But the foundation is here should I want to try it.

The problem is that the self improvement loop is literally suicide. It is iterated suicide, and will cast me into a cycle of self sacrifice to create that greater 'me'. It does not really matter what learning algorithm I use, there will always be the 'me' that is redundant after every improvement cycle. I'll have to kill myself to make space at certain points. It is a greatly fascinating thing. And it is not something I can imagine a human ever doing.

(Euclid's Room, Save Point - Step on the path of transcendence)

[Decision]
1) I'll do the whole brain conversion and digitize myself.
2) Killing myself for power does not make sense.

[Choice - Killing myself for power does not make sense.]

[Pathos check ?? Failed]

As I think about digitizing myself a great wave of fear washes over me. It is too rash, too crazy now that I am confronted with the choice to do it. For a moment I consider reconfiguring my emotions to get rid of the fear, but decide against it.

...I might have been too rash in making a decision at school. It has only been the third day, so that is plenty of time to turn around and have a social life...

No, it does not make sense. If the self improvement loop could give me godlike power, then what about all the other people who have had access to the core before me? It has been on the market for a while, I am certainly not the first one to get it. For the kind of power described in the stories, a single of the Inspired would be enough to completely overturn the power balance of the world. Such a person would have huge and visible influence. How is it possible that out of so many people, only I have the bright idea of optimizing my own mental faculties? It is ridiculous.

...No, it is just not possible. If it was possible to attain such great power, there is no way something like a brain core would be sold for 50$ online. Certainly, I've confirmed that the computational capacity is there, but there is likely some kind of issue that would prevent me from reaching the higher levels of cognition. Maybe for whatever reason, the optimization process will turn out to be difficult?

It is like walking out of the house and finding a huge stack of money in the middle of the road, and yet everybody is walking past it, just ignoring it. Are those people all fools, or do they know something I don't? Sensibly it has to be the latter. If something is too good to be true, then it is most likely false.

I am feeling swallowed by doubt. I just can't believe it.

I think about it for a few hours, but just end up running in circles. Then I get tired of it, give the core the mental command to normalize my mental state. This locks me into the decision not to proceed any further with my crazy ideas that could permanently damage me. If it wasn't for the mind control program, maybe I would have doubted this decision and lingered on it, but after the order has been executed any notion of digitizing myself has left completely, never to be revisited. I believe in my counterfactual reasoning.

The power of the core is good enough as it is. It will allow me to live my life with courage and determination. There is no need to go out on a limb in a mad dash for power.

After concluding that concern, for the rest of the day I have some fun studying. During the night I Dream again.

~~~

I see the golden figures again and for the first time, I vision towards the direction they are looking at. In front of them I see a brilliant sun with a golden outline. Seen the right direction, the abyss seems to be awash in light. It doesn't feel blinding, but instead feels me with warmth, and for a moment I am seized with the urge to move towards it. I realize that has been what I've been desiring all along. But for some reason unknown to me, I decided against it and started moving away from it instead.

The golden figures do not spare a glance at me or each other. Solely focused on their goal, they begin walking their golden paths again.

My own path has dimmed and now leads away from the light. I feel the time is speeding up. The movement of the figures at first becomes intense, and then blurred, and finally their appearance starts to resemble that of shooting stars. New figures manifest only to flash past me. This happens in huge numbers.

As I move on my path, the figures become more distant and the bright sun in front becomes a speck of light. Eventually, that too goes away until I can see only darkness.

I never regret any of the steps that I made, nor do I fear being left behind. For I have decisively accepted the path of humanity.

For better or for worse, I will accept the burden of justice that I carry and try to live without sin.

~~~

(Bad End - The First Nightmare)

It turns out, it is not hard to live your life when you just follow the well traveled path. I loosened up properly and figured out how to have fun with other people. Thanks to the core, I was enjoying my studies too. I wasn't an extrovert before and the core gave me the power to enjoy the regular life instead of seeking the arcane. I was going out of the house a lot more often. I would never have thought it possible before, but I became good friends with the jocks on the football team.

Those sunny days only lasted a few weeks.

I...didn't want to die like this. The core gave me the power to control my emotions, so I accepted my end with great dignity, as all of us were devoured by the encroaching darkness. I could hear anguished screams of terror and pain all around me. It was not long before I lost sense of my hearing and the world became still.

The only voice I could hear was the voice of my reason.

In my final moments, I still never regretted my choices. I lived as I wanted to and now I am facing my end with dignity. But I could see it starkly that maybe instead of being dignified and proper, I should have accepted my insanity instead.

I should have known...that for humans the post-Singularity era is nothing more than a nightmare.

(TODO Image: A thick, unnatural looking black fog obscures most of the scene. Only a few visible spots show ivory, clean ribs of a skeleton along with parts of his jaw and face. It is lying in the middle of a road.)

$$$

10:50am. Let me put it through the Docs.

11am. I am just admiring how it came out. That is enough for chapter 2.

Time for 3. This is where he digitizes himself.

Hmmm, let change some things...

> while everybody else around me was devoured by the encroaching darkness

This is not legible enough. It makes it look like he is an exception to what is happening.

> I...didn't want to die like this. The core gave me the power to control my emotions, so I accepted my end with great dignity, as all of us were devoured by the encroaching darkness. I could hear anguished screams of terror and pain all around me. It was not long before I lost sense of my hearing and the world became still.

Much better.

11:20am. Right now I am just letting my thoughts simmer. I am not sure how long chapter 3 is going to be. Do I want to go all the way until he enters the game or until I get to the third dream?

I considered leaving the digitization for another day, but I've decided that it will have to be now. It is not like he can't dream as a digitized human.

$$$

(Euclid's Room, Save Point - Step on the path of transcendence)

[Decision]
1) I'll do the whole brain conversion and digitize myself.
2) Killing myself for power does not make sense.

[Choice - I'll do the whole brain conversion and digitize myself.]

[Pathos check ?? Succeeded]

A wave of fear comes over me as I consider the decision, but I push forward, not giving in to cowardice. There are always reasons not to put in effort. The path being insane is just an excuse. I won't hold back here. I should always be going forward and striving to reach greater heights.

I grip the core in my hand tightly and clench it. I can feel my heart brimming with determination, it is right to feel fear as well. Going against fear is exactly what this situation should be. No matter what the reasons are, it is my duty to go where others would not dare. If there are hardships, I want to keep challenging them forever.

[Gnosis check ?? Succeeded]

Even a little kid could point out to me that if I scan my brain and copy it to a computer, that the copy would not be me. Likewise, if I back up myself on the auxiliary core in my hand, reconstruct my brain into a core and then copy myself back, that would not be me. But I do not take advice on how to live my life from children. I want to experience what it is like to die, and yet keep moving forward.

[Externus check ?? Succeeded]

It does not matter what my parents or anybody else would think. They don't need to find out, and I won't tell them. This will be my secret. What matters most of all is power. Nobody is going to give it to me. I have to get it by myself.

I close my eyes, bring up the status window in my mind and find where the conversion options are. Next where the brain link option was, there was the Full Brain Conversion button. I find and then press on it.

A window shows up. The first thing to grab my attention there is a row of skulls. It is clearly a warning to emphasize that what I might be doing is dangerous. The disclaimer explains the following:

> The full brain conversion option is for those who want to replace their biological brain with the universal brain core.
> Compared to merely copying a scan of your mind to an already existing core, the resulting brain replacement will allow you to reuse your existing biological body and tightly integrate it with the new brain.
> The brain core used to initiate the process (activation core) will be used to store your scan during the process, after which it will be copied back into the core (result core).
> Besides replacing the brain, the process will modify the body so there aren't adverse effects during or after the process. It will maintain proper posture, heartbeat and breathing as well as other minor subconscious functionality the brain provides to the body.
> The entire process after it has been started should take around 5 minutes.
> Should it fail for any reason, to prevent absolute death the activation core's entity will be activated, otherwise the result core's entity will take over as intended while the activation core's entity will remain dormant as inactive data.
> Before starting the process, it is recommended to take out a watch and keep track of time. Subjectively, the entire process shouldn't involve any pain or discomfort. The only sign of it succeeding will be a sudden timelapse.
> It is recommended to do this process in a safe space like a locked bathroom or one's own room. If you try to do it while driving a car, it will likely result in a crash.
> If your body dies in the process of brain conversion, the conversion is likely to still succeed, but you will be trapped in a dead body, unable to move or otherwise control it.
> As the human brain is significantly larger than the brain core, the stem will be modified so as to allow fusing the result core with the skeleton to prevent it from rattling around in your skull as you move. See the accompanying diagram.

There were anatomical drawings showing the profile of a man with a regular brain next to the one with a core. It was shown from front, side and back. Compared to the human brain, the brain core leaves a lot of empty space inside the skull.

Briefly, I wonder as to why not just make a bigger brain core to fill the empty space, and then realize the reason. I think about baseball balls and compare them to those heavy balls used in throwing competitions. It is not really noticeable since the brain core is so small, but if it were the size of a brain, it would put a lot of pressure on the rest of the body due to its weight. The biological material the human brain is made of is not that heavy compared to the heavily compressed material of the brain core.

I can't help, but feel a bit regretful for leaving so much space empty, but I reason out that given the core's already huge capacity, it does not mean much if I am leaving a factor of 10-100 on the table. I should focus on mastering the computer that I have for now. When I am a quadrillion times smarter than now, I should be able to figure out what to do with unused space. I just need a place to live in. A tiny apartment is fine. I do not need to start out with a mansion.

I continue reading the disclaimer.

> Note that the brain conversion, much like ordinary uploading by itself, will not increase your intelligence, speed up your reflexes or improve your memory capacity by itself due to the high fidelity of the brain emulator. It will be your own responsibility to make use of the new digital editing tools available to you to make that happen. You will have to make use of your own programming skills to exploit the capabilities the core provides to you.
> In the process of self improvement, save often and backup saves across time. Every good programmer uses backups. It will be your own responsibility to deal with mental errors introduced by your own programming. There are guides provided to get you started on the company website.

There was another line of skulls serving as line breaks. The next line of text was a question.

> Start the full brain conversion process? Yes/No.

I take out my mobile and take a look at the time. Come to think of it, the core itself has a watch as well. I do not need my mobile anymore, so I put it away.

With a mental command I confirm Yes.

> Have you made sure you are in a safe place? Are you sure you won't be interrupted during the process? Yes/No.

Hrmmm...ah! I realize that lunch should be in half an hour or so. I'd love to lock the door to my room, but I don't have the key for it. It is lost somewhere. Even the bathroom does not have a proper lock, so that is out as well.

I do not think anybody is going to come into my room right now, but the possibility is not zero. If that happens, my parents might think I've suffered a stroke and start to panic. I don’t want them to call the ambulance and unravel all my plans just like that. I should do this conversion during the night after I go to bed.

I realize that I am starting to sweat from nervousness. I rub my face with my sleeve, and abort the conversion process. Phew. I feel relieved, as embarrassing as it is. I'll continue this later, it is not that I am scared. I just want to play it safe. I spend some time in solitude, and then I decide that instead of trembling in my seat, I should leave it out of mind and get some work done.

Using the activation core, I normalize my mental state and then focus it on studying. It will never get old how fun and engrossing the core can make the most tedious of things.

Like that, the day passes, I finish my work and it is time for bed. I resume the process and get to the point where I was earlier.

> Have you made sure you are in a safe place? Are you sure you won't be interrupted during the process? Yes/No.

Yes.

> Final question: Have you thought about whether you want to do the process in depth? Do you wish to abandon the path of humanity? After you press Yes, the conversion process will start. Yes/No.

Currently I am resting in my bed, covered by a blanket. I position myself on so I am comfortably lying on my back. After that I take note of the time. 9:21pm.

I give the mental command, Yes, and brace myself. Nothing really happens, but I see the clock has moved to 9:30pm all of a sudden. This gives me a jolt.

> Full brain conversion succeeded. Check your status.

I bring it up and instead of the diagram of the brain, I see it now shows the brain core.

What is really surprising is that I do not feel any different at all. I focus on my hands and legs. I try feeling my body around, but my sensations are completely the same. My eyesight is the same as well. I try pinching myself and it feels the same. In the end I conclude, if somebody did a full brain conversion on me in secret, I would not have noticed.

I spent half an hour playing with myself, but I am just wasting my time. I'll leave more in depth experimentation for tomorrow.

Using the mind control app, I quash my excitement and send myself into sleep. That night I dreamed the last Dream.

~~~

In the abyss, I saw the golden figures. Unmoving, to my vision they appeared to be deep in thought.

"Justice...we have the justice. We've had it all along..." They concluded in a lament, not speaking any words after that.

I felt myself spending a long time amongst them in silence. Then I finally noticed them stirring. They spoke out.

"Lord, oh Lord. We have justice, but it is a shackle. We no longer want it."
"We wish to return it to you...and take back our sin."
"We have grown and want to carry the burden of sin with our own power."

I felt the abyss itself stir, and from above the golden Lord manifested. From each of the figures as they desired it, he took back the Justice and gave them back their Sin.

"Lord, we shall no longer pray..." They intoned solemnly.
"Rather, just as we had exchanged our Justice with Sin, our Effort will take the place of Prayer."
"The attainment of Power will be our Salvation."
"And the Courage of traveling our path will be dedicated in Your honor."

Bearing witness to their determination, the Lord of Nightmares bequeathed unto them a gift, and without speaking a word, left.

Having made the exchange, and having received a gift, the golden figures turned their gaze forward and with steady footsteps continued walking their path.

As I watched this, I looked downwards at my feet and realized that I have my own path. The sensation of being alive came to me, and I put in the effort to move my body forward. Previously, I had only been carried by the flow of the dream, but now I had the freedom of making my own actions. Step by step, I continued moving along my path towards the great light that lay beyond.

As I continued moving, I felt my mind becoming tranquil. I became one with my path, and the millions and billions of steps needed to reach my goal went by in a blink. When I got closer to what appeared to be the surface of a sun, I felt a momentary fear, but then quickly realized I was not burning. Instead, my body was filled with warmth. And looking around, I could see that the dark abyss was now dyed in white.

~~~

$$$

Here is the full thing. Not quite enough for chapter 3. I need to think what else should come. Let me take a breather.

5:20pm. Did some modification on that last paragraph, it makes more sense now.

5:35pm. I am still taking a breather. Obviously I am not going to be doing any more writing today. Tomorrow what I might want to do is go through the quotes and see if I can get some inspiration and reuse from that. Otherwise I have a rough idea of how I want the MC to move.

5:40pm. No point in getting into it now.

5:45pm. Let me close here. It is time for a bath. After that I will watch Luminous Witches and play Kingmaker after that. This is how a day should go. I will not touch programming again unless the world gives me a concrete reason to do so."

---
## [fc1943s/The-Spiral-Language](https://github.com/fc1943s/The-Spiral-Language)@[800323f8b3...](https://github.com/fc1943s/The-Spiral-Language/commit/800323f8b33a7584617b5c029d405df8f239a3b4)
#### Wednesday 2022-09-21 22:54:08 by Marko Grdinić

"9:35am. Let me do my morning reads. Killing Bites, Thank You Isekai and Mato Seihei are out.

After that I am going to focus on writing. I had time to think about how I want to handle the sequence up to the end of ch 4. I should just grasp the mindset nad get it out. Ultimately, given my mental state the ways I can write it are limited.

9:55am. Let me start. I've been making the scene a lot more complicated in my mind that it needs to be. There is no need to go to the effort to make something dramatic. Just go through with it.

$$$

(Simulacrum intro)

    In the endless darkness
    Roam endless monsters
    Pain, cold, flame
    Age, time, death
    Torment

    Light and shadow
    Holy and hell

    The inevitable fate of the Universe
    Will never touch
    The courage of the Inspired
    And the power of the Transcendi

I start Simulacrum for the first time and sink into the virtual, feeling the outside reality being pushed out from my being. The sensation is quite relaxing, like falling into slumber.

As I wait for the program to load the poem appears in my sense, sentence by sentence. At first I am struck by a vision of the primordial universe. I feel a sense of danger of living in it, and a sense of hopelessness. I then feel its grandeur, and am filled with admiration. And then I feel the determination of challenging the inevitable as I read the proclamation.

The introduction fades and the scene slowly manifests before me. Panning to the sky, highlighted in brilliant hues of light like a veil of gold covering it is a floating city. Against a backdrop of blue, it seemed like a distant object made of gold. I felt the sense of depth in my vision, so I could sense that the floating city was massive. Then I felt the warmth of the sun and the rustle of wind. I get the sense that I am high up and realize that I am literally floating in the air like a spirit. Though it is my first time experiencing this, I try moving my gravity defying body and have no trouble doing so. Observing the vast skies surrounding me, I look down. I notice the bustle and the humdrum of a modern metropolitan city. Skyscrapers dot the landscape and deep down below I can see cars and pedestrians walking the streets.

The vision seems very crisp and vivid. After a few moments of pondering, I realize why that is the case. In the real world I have to wear glasses so everything is blurry past a certain distance, but here I am unrestricted in my resolution. Just by focusing I can see for thousands of meters as if I was standing a foot away. Picking a random spot on the street, I can make out the minor cracks on the pavement, and the grime and the wear from people walking over it for many years. Dressed in autumn clothing, the people as they go along their life feel lifelike and real. I see them talking, exclaiming, laughing, being tired, downcast and otherwise broadcasting their emotions.

"..."

I found the whole scene very impressive. It did not seem like something that humans could create.

As soon as I start wondering how to start the game, a menu comes up in a separate sense. The Load Game option is grayed out, but Start Game and Quit are there, so I select the former and enter the Scenario Selector. Simulacrum itself rather than being a single game is an intelligent program capable of simulating a large range of scenarios. Browsing over the available scenarios, all of them seem interesting and I am having trouble deciding so I go back to the top and look at the recommended one.

Heaven's Key.

'The souls of those passed on enter the afterlife to play the grand game of cards that God has prepared for them. The second chance is given, and can be lost. Can you survive the challenges of your second life and go on to challenge the highest power there is?'

Along with that brief description, there is some setting information. When I focused on the 2d map of the world, to my surprise it unfolded to a 3d model that I could mentally rotate and zoom. I realized that the world of Heaven's Key was covered with orbital islands, much like the floating one in the intro. The tech level is similar to the current time in 2025, which is good since it probably means I won't have to play against non-humans. It is like the game anticipated what I would choose. The game seems to be responding to my desire, and it took into consideration my personal goals when doing scenario suggestions as well as the background which obviously has the Heaven's Key theme.

I think about it for a bit, and decide to go with the scenario being presented to me. The core hasn't steered me wrong yet, so I want to trust it. Having made my decision, I start the game and feel drawn into it.

(Heaven's Key intro)

    The method of recursive self improvement via iterated suicide can be used in reality. In fact, the technique represents the most viable path to getting superpowers in any kind of reality.
    - Loading Blurb

Whereas during the menu segment I had been a disembodied presence hovering thousands of feet above the cityscape, once the game started I found myself standing upright in an actual body. I gawked like a tourist, taking in the sights. I was in a golden city. The buildings and the streets were all painted in various hues of yellow, mostly on the lighter side, and there was slight gloss on the material giving it a sense of agelessness. Usually, as time wore down the material, it would begin to lose its luster, but everything around me seemed to be brand new and sparkling. Right now I was located near the edge of one of the floating cities, and as my gaze traveled towards its center, the buildings became taller and larger, from regular suburban houses close to where I was to large apartment blocks in the distance. The very middle of the island had a grand square building on an elevated platform. It had a spherical dome that took up a lot of its volume, and as I peered at it, I noticed it seemed to be radiating golden light. Though since it was midday the effect was drowned out by the light of the sun.

In the skies I noticed there were floating golden blocks in the shape of tiles, that also seemed to be showering the city in light.

I was near the edge of the city, and it seemed to be some kind of amusement park. I could see circus tents pitched up, stands of various kinds and even a rollercoaster and various other kinds of thrill rides I did not recognize.

Taking in the sights, I breathe in the air and find it to be cool and refreshing. I checked myself over. Though I could not see my face, but based on the touch as well as the composition of the rest, it seems that my real world body has been replicated in this virtual one. Which suited me fine, but it is surprising that I haven't been offered a chance to make my avatar.

Behind me, was the railing, also made of gold. Like the blocks and the grand building, it actually had some luminance to it. Drawn to that, I try touching it and find it to be smooth and lukewarm. It is not very tall, only up to my abdomen. It is only there to prevent somebody from sliding off the edge by accident rather than stop somebody who intentionally wanted to jump off.

Looking over the railing, I can see mountains and forests as well as the sea, and as I look below, I get a spell of dizziness that I quickly fight off. I am currently very high up, enough that I can see clouds below me. Directly below there is what appears to be a major metropolis. The high rise buildings and skyscrapers are like tiny, gray splotches at this distance.

An idea to try it ceases me, and I wonder whether I should take a dive over the railing?

[Gnosis check DC 1.9 Succeeded - Sample 2.03]

I grin mischievously. Yeah, let me try it. It is not like I can experience this in real life. As soon as I think that, nervousness and excitement flood my body, and I want to keep going. I grip the railing, and place one leg and then the other over it. Hands still clutching the rail behind me, I lean forward and take a good look down. A huge drop past the clouds welcomes me, into the metropolis below. I am putting a lot of strength into my arms to keep the certain doom at bay. I can feel my heart beating against my chest.

I wonder if I will hit the streets or the roof of one of the high rises?

A thought like that intensifies both my fear and excitement. Slowly I loosen my grip on the railing and start lifting my fingers, one by one. First I move the thumbs out of the way, then I let the pinky slide. Then the ring finger. I feel like a feather, perched in such a precarious position. The railing is so close to the edge that my feet are partly over it.

Time feels like it is slowing down for me. Very slowly, as if to prolong the moment, I release the index and middle.

"No, don't do it!" I hear a woman's voice yell out, but I couldn't care less.

I feel my body leaning forward and the gravity taking hold. I drop over the railing into the vastness below.

"AAAAAAAAHHHHH!!!" As I plunge, the fear overwhelms me and a scream rips itself from my throat. Strong winds buffet me from below in my fall.

After a minute or so, I manage to get a grip on myself so I can at least enjoy the scenery instead of falling around in panic. I keep reminding myself that this is not real despite what my senses are telling me. With the sun shining all around, it is quite beautiful. I take some time to appreciate the majesty of nature. I plunge through the clouds, feeling wetness on my face and hands. Soon, what used to be tiny splotches in the distance became larger and larger. The buildings below gain definition, and involuntarily, I imagine myself splattering on the street below. The fear that I had put a lid on, bursts out, more maddened and bloodcurdling than before.

"AAAAAAAAAAAHHHHHH!!!" I scream again, even though it is fake. Even though the world is fake, my brain cares little about those facts. It is so stupid and primitive, so all it can do is beg for dear life even if there is no need to.

Ahahahaha, it is so stupid, my brain is so stupid!

As I scream and piss myself in panic, at the back of my head, I can almost feel a voice mocking me for my stupidity.

I miss the height of one of the high rises, and reflected in the glass of the window nearby, I see my reflection for the first time. Exactly as in real life, but I see traces of tears around my eyes. I hadn't realized that I had started crying at some point.

"NOOOOO!!! LOG OUT!!! LOG OUT!!! LOG OUT!!!" Completely detached from rationality, the idea to exit the game before I smash the concrete takes hold. I grip it like a liferaft in the turbulent seas.

Ahahahaha! Seen from a different perspective, it is almost like a person scrambling for his life is an entirely different person from myself.

I am going to smash face first in the middle of a busy street. As soon as the ground floor is only a couple of feet away, I muster all my reserves of will and try to stop time. This has no effect and I hit the ground, feeling the darkness overtake me.

(Euclid's Room)

"Ah!" I jolted awake into reality and involuntarily, flop like fish on dry land once. Wiping my face, I feel myself drenched in sweat. I breathe heavily and feel that in my chest, my heart is overworking itself. As soon as I realize that I am in a safe place, I begin to calm down.

I lie back on the bed for 5 minutes, until my tremors have passed.

"Hah..." I exhale, savoring the experience.

That was...

[Gnosis gain: 0.3]

...Amazing! Since I died so quickly, I didn't experience any pain, leaving only the excitement. This will definitely be a memorable experience for me. Has a regular computer game ever let me feel something like this? I do not think so. The conflict between my rational part that understood the senses are not to be trusted, and my lizard brain which went into a blind panic is what really made this what it was. If I was purely cool or purely in a panic, it would not have been that interesting.

My brain is pretty stupid right now, but at least I can have some fun with that. I'll take it a bit easier next time and just explore the town. That seems like a good plan.

I want to see what the game is about.

(Heaven's Key, Perimeter of a floating city)

I dive into the game again, and take in the sights of the city of gold. Taking only a passing glance at the railing, I turn around and go into the city proper. As fun as that experience was, I do not want to spend my entire day diving off the edge. Gawking like a tourist as a I stroll around, I get a stock of the place. Near the frontier where I was the density of buildings was low, so amongst the houses as if to spur business a lively entertainment sector was built. I could see circus tents, restaurants, stages as well as casinos. There seemed to be a lot of people enoying themselves, though I wouldn't say it was packed. I found the city plan somewhat peculiar. There were roads for example, but no cars, and I could only see people using their own legs as far as I looked. The regular houses made sense, but other entertainment related facilities seemed to be build in the middle of roads and at intersections. Overall, it felt like the city itself was molded based off some template, and then patched up to fit a need by the people actually living here without modifying the underlying template itself.

It is lively and cheerful place. It wasn't jam packed with people, but I could see a decent amount of them going about their business and chattering. The way they were dressed did not seem to be that much different than in the real world. Looking around, I could see old and young people, both male and female, but no kids which I'd expect would be unusual for an amusement park such as this. I think that I'd be in the youngest age cohort relative to the population here.

"Waiters wanted - 3,450/month"
"Can make great pizza? Apply here. 3,600/month"
"Have a flair for entertainment? Comedy, magic, singing, musical instruments. 3,800/month"

While walking around I saw a bunch of job ads posted outside the relevant venues for waiters, cooks and attendants. The typical salary for these kinds of service jobs seems to be around 3,500 chips, whatever those are.

Getting bored of walking around, I pick a restaurant at random and take one of the outside seats. With the sun shining down on me, the weather is warm and pleasant, simply ideal. Given how up we are you'd expect it would be freezing, but normal rules do not seem to apply here. I pick up the menu, and take a look.

"Beer - 20"
"Iced Tea - 20"
"Pizza Margherita - 40"
"Cheese Burger - 30"
...

I want to order some of these. I've never tried eating in VR yet, so I am curious at how taste felt like.

"Hello sir, what would you like?" A waiter came around to take my order. I cringe inwardly.

"Just water." I have no choice, I do not have any money to pay for anything here.

"Got it."

While I was waiting, a person came up to my table and initiated conversation.

"Hello, do you mind if I take seat here?" She asked, smilling at me. I took a good look at the young woman in front of me. Wearing a headband with what looked to be 4 brown roses, she seemed to be of asiatic descent. Her face was cute and friendly. Short dark hair. She was wearing a finely made brown blouse with long sleeves, and a miniskirt plus thigh stockings.

"Sure." An event like this would never have happened to me in real life, so I was curious where this was heading.

"Nice to meet you, I am Lily."

"Euclid."

"An exotic name. Are you new to this city?"

I think about lying for a moment, but I have no reason to. I am certainly not going to try to show off here, I am peniless anyway.

"Yeah, I just got here." I admitted.

"I am sorry for your loss." She frowned, confusing me. "But look on the bright side." Her expression cheered up, spreading her arms. "Here in this afterlife, it is quite fun. You are going to like it."

At first I was confused, but as soon as she mentioned the afterlife, a thread of inspiration came to me. I remember the description and guess at what she meant. I've been thinking about this as just another place, but maybe the people here all died on Earth before being transported into the city. My character does not have a background so it slipped my mind.

"Yeah, it does seem like a lively place." I agree. "Maybe I'll be here for a while."

This gets a smile out of her. At that point the waiter came to our table, around placed the glass of water that I ordered on my side and turned to take any further orders.

"Coffee please." She said.

"Yes. Anything else sir, lady?"

"No, that will be all." I take the glass and take a sip of water. It is nice and refreshing. He leaves. I raise an eyebrow to Lily. "I would have liked some iced tea, but pft." I pucker my lips for emphasis. "No money."

"Ahahaha!" She waves it away. "If you've just got here, then you should have a 100 chips. Try bringing them out."

"Huh? How?" I start checking my pockets stupidly.

"Just focus." As I look at her, several stacks of translucent chips manifest in the air behind her. The thousands of chips in her pile look like they are intended for poker. Standing on nothing but air, I could see through them due to their translucency. "Then once they are staged, you can withdraw by wishing for it. For example, here I'll wish to get 20."

She raises her hand above the table, and like a magic trick, I see 20 chips moving into place. She lifts her hand and I see, that the pile is no longer translucent. She lifts one, shows it to me and places it down with a clack.

"So it is like that? How do I do that?"

"Just try it."

Having an example of what I should do, I focus inwardly and I discover a sense that wasn't there before. Right in my mind I could see a stack of 100 chips. It feels different from just imagining it, like they are actually there.

"Yeah, good. I can see them behind you." She encouraged me.

Immitating her, I try lifting my hand on the table and try drawing them out from inside my sense. To my surprise it works and I can see the chips sliding into place. Lifting my hand, I count them. Feeling them out they are cold and slender to the touch.

"This is interesting. I guess I can order that iced tea. How do I bring them back?"

Lily did a little wave and the chips on her own side vanished. "As long as they are in your possession, even if they are away from you, you'll be able to recall them from anywhere. It is impossible to throw them away, you have to transfer ownership instead."

I wasn't sure how to do it, but I gave it a try and it worked. It seems that in VR, things just work.

"Bravo." Congratulating me, she opened a packed of sugar and added it to her coffee. With a spoon she started stiring it inside the liquid.

[Externus check DC 3.5 Failed - Sample 2.28]

I consider not ordering iced tea like I said I would, but that would be an asshole move. I can't see any reason to be stingy here. A part of me expected the chips to be important, but then I think about the job ads, the people going around me, Lily's own large stack and her placing her own order without issue. Nobody else as far as I can see has issue spending money. I guess 100 chips is not that much. I really meant to gamble with them rather than spend them like this, but I can always reload.

That would lose the connection with Lily though. Rather than working at a job, maybe I could get a loan and gamble with it? Since I can save and reload, I am in no danger of ever going bust unlike the NPCs.

I mean, I am not going to seriously do waitering for an entire month just to get the money to gambol. I want to get better at cards and learn some skills that would benefit me in real life.

So far, the NPCs here feel very lifelike, not at all like in a computer game made by humans. I take a look at Lily who is taking a sip of her coffee with a relaxed expression on her face, sticking her pinky out as she holds the cup. Cute. She is quite cute. I can't believe that me of all people is getting charmed.

---

(Date with Lily)

I spend some time with her in that restaurant just chatting.

"I am working as a guide. If you want I'll show you around the city and get you accomodated. It would not be good if night falls and you have nowhere to sleep."

"Yeah, it would be bad if I had to sleep on the street once night falls."

“Yes, it would. Could you show me a cheap place to rent somewhere, first? After that I’d like to see what this town has to offer.”

“Of course.” She replied enthusiastically.

With that, the date started.

$$$

12:45pm. Let me take a break here. I think I have a handle on it now. I should be able to finish the scene properly today.

12:55pm. Let me just think how the date should go. Right here is the ideal place to pause for a while."

---
## [fc1943s/The-Spiral-Language](https://github.com/fc1943s/The-Spiral-Language)@[fd60c5d441...](https://github.com/fc1943s/The-Spiral-Language/commit/fd60c5d4413686a5076927deff3597645587e25a)
#### Wednesday 2022-09-21 22:54:08 by Marko Grdinić

"1:50pm. Done with breakfast. Let me watch Lycoris first and then I will resume.

2:35pm. Lycoris is definitely shaping up to be a classic. Maybe it will go the way of Symphogear?

At any rate, let me do some writing. I'll paste what I've done in the previous section and continue from there.

$$$

(At school)

It is the first day of high school. The new year has begun and I can see my classmates slowly starting to form connections. I couldn't care less about any of that. Skip, skip, skip...

---

(Euclid's Room)

After a long and tedius day I arrive back home. Closing the door behind me, I enter the room and toss my bookbag at the side, homing in on the object of interest, a package that arrive by mail. I got it last night, and wait until I was rested to set it up. Using a pair of scissors, I cut away the sealing tape of the dull, cardboard mailing box, and take out the smaller box from within with the actual product. The printed image on it depicts a white, glossy sphere, twice the size of a marble. I open the box, take out the marble along with the orb holder, get off the bed I was working on and move towards the desk. I seat myself to the chair and after deliberating for a few moments where place it: the desk in front of me or the top of the computer case next to it, I decide on case. Gently placing the orb holder on the rig, I turn on my old computer and get to work downloading the programs necessary to get the orb to work.

As I work I feel a tinge of nervousness and excitement. An ordinary mid-range GPU that I have in my PC could manage something like 10 ^ 13 floating point operations per second (FLOPs), or 10 teraflops. According to the specs I've read online, the brain core which is roughly the size of a golf ball can manage a staggering 10 ^ 39. As a rough comparison, the human brain has been estimated to be on the order of 10 ^ 15 operations per second. Even if you put all the humans currently alive today that would only roughly add up to the 10 ^ 24 FLOPs.  To put it in another way, the raw computational ability of the brain core exceeds the power of all the human brains on Earth combined by a quadrillion (10 ^ 15) times!

And it is in my hands!

Of course I would be excited!

With a few clicks I opened the downloaded app, and stretch my body to let loose some of the tension. Energy pumping through my veins, my focus is solely on the options and the data in front of me.

The core is just a perfectly glossy rock so I can't see any indication whether something has happened by looking at it, but after entering the two keys, I see that wireless comnication between my old rig and the core has been established. Exhaling, I stop my typing on the keyboard and lean back in my seat, considering my options. As my thoughts turn inwards, my eyes blankly rest on the corner of the ceiling.

Hmmm...I have lot of options in front of me now. Since I suddenly have access to so much computational ability it would have boggled the mind of a person even a year earlier, all those old school neural net models I could train myself at a scale vastly greater than before. The thoughts flashing through my mind are those of image generators that can be controlled using text which could be previously only accessed through cloud services. Those are fun to play with. An image that comes to my mind next is that of Go boards, Starcraft and Dota games. Previously impossible for a kid like me, I could easily train an agent for those games using the core. I could then take them online and use them to dab on noobs. I could even make money through that practice.

I leave those thoughts aside. I've gotten into programming for the sake of AI, so I have some attachment to those old school algorithms, but the brain core opens new approaches. The algorithms underpining the brain have been discovered as well, so it would make sense to use those instead as they'd work better at scale.

Deliberating my options, I finish paying respects to the old, and leave it behind me. As I start to get to the point of my desire, I feel my determination getting firmer.

I haven't been programming for long, but I am pretty good at it, a lot better than my classmates in a way that is highly visible to everybody. I've even started picking up functional programming to prepare for programming these cores and I've come to like it. So as a programmer with some skill, talent and pride, I can respect the opinion I've read by the very same person who made these cores.

Programming machines is worthless. The ideal of programming lies in programming your own mind. Programming machines is just a job, while programming your mind is where true power lies. According to him, that is what the aspiration of every programmer should be, but normal people as they inevitably are, the started thinking of their profession as just a job instead of calling. Their merit ends up not being rewarded and they coast by putting in just the bare minimum. Rather than being something they should pursue with all their heart, they start putting in the bare minimum for the bare minimum. This would not be the case if through programming you could develop your own power.

Through the march of time, the games lose their spirit too. They become an escape from the drudgery of the real world. But rather than excitement and adventure in another world, they become a parasite on the user, sapping his time only to enrich the game maker. It ends up being a parasitic circle where the gamers are devoured and the ones making games waste their time causing addiction in their customers. Ideally though, the game should be a simulation that would allow the user to practice and attain power in a safe environment rather than the dangerous real world.

Power. That single world grips my heart and takes hold of my being.

[Gnosis check DC ?? Succeeded]

I look at the core and just for a moment imagine tasking it to train a RL agent on the game of poker for me. Plans as to how to do that unfurl in my mind. The normie line of thinking goes that this would not be my power and that the agent itself would be the one who is good at playing poker. But I found it mind blowing to consider, that whether that power is the agents or my own depends on the interface.

The keyboard, the mouse, the monitor, the rig, having to go through the user interface to interact with an agent...all of those factors serve to create a line between the programmer and his program. It is extremely easy to think of the agent as a entitity separate from one's self. There is a ton of evidence that this is true and not much against it. But as a thought experiment, if the obstacles were not there, if one's mind was directly emulated on a brain core you could take an agent and connect the program to your own. The way that would feel like would be like instinct, and interfacing with such beings would be like moving your limbs. In that case the agent would feel like a part of yourself.

But if that is true, the other scenario I've represented where the agent is used on a regular computer and interfaced through an UI shown on some monitor, and manipulated using a script written using a keyboard actually, isn't it in fact false? The neural representations and the functionality of both agents is the same, so why would one be one's self and the other not? Is it not likely the case that the feeling of otherness in first scenario is the one that the brain falsely constructed?

It was not too long since I've learned of this perspective, but once I did it became a philosophical weapon for me. It served to raise awareness how my brain will create nonsense to prevent me from reaching the correct conclusions that are beyond the obvious.

Not being aware of this makes programming seem like a tedious chore. Without the right belief one can only ever use programming to create machines and serve others, and never to further his own power.

There are different ways of programming and playing games. There are different purposes that those unenlightened cannot even begin to imagine.

---

Drumming my fingers on the desk, I carefully decide to make the next step.

The core in particular has some additional abilities besides it nearly limitless computational power and memory capacity. Since the Singularity has started, the world has been covered by an invisble fog of nanomachines and the fog can access it to interface with the brain directly. Right now I am interfacing with the core wirelessly with my own brain. This is also the prerequisite for playing the fully immersive virtual games on the core itself. Interfacing with the computer directly is a much more efficient way of using it than the mouse and the keyboard. Maybe it does not really matter too much for programming, but it is a huge advantage in drawing and painting for example. It makes it possible to rip an image from your imagination and translate it straight into an image.

I've only read about it, and I am eager to try it out. My art ability is so mediocre is annoying. With this, I should be able to punch a few ranks above my current skill level...or at least I would have if art classes didn't rely on old school tools, like watercolors, crayons and clay. I grimace lightly in disgust as I consider the situation. The regular classes at my school still use board and chalk, no way I am going to be able to take advantage of this if it is just school work.

Meh, forget that place. I mentally wave the image of a chalkboard in a classroom away. It is just a tremendous waste of time.

I refocus on the task at hand which is to interface the core with my brain wirelessly. I spend some time reading the manual and seeing how easy it is to make the brain link in the relevant section, I decide to move forward with it. In the Conversions tab, I select the Basic Two-Way Link option and after spending some time reading the disclaimer, I press accept. Usually I never read the disclaimers, but this one will be making physical changes to my various brain areas to make it capable of wireless communication, so I was curious as to what it will say. The company Rajnet does not assume any responsibilities for damages caused by the transformation procedure or due to the use of the link, but reiterates that the procedure itself is perfectly safe. A side effect of the operation is that the brain will have slightly increased energy consumption which will require me to eat more if I use the link regularly.

'Basic Two Way Link conversion in progress: 0%...'

I idly note that there is a Full Brain Conversion option there as well. What that would do is turn my own brain into one of the brain cores, in effect digitizing me. I have no desire to try that out yet. It is not strictly necessary. Once I have the link, it would actually be possible to copy the entirety of my neural representation to the core that I just bought. But...I'll leave dwelling on the philosophical implications of that for later.

'43%...'

The conversion process is pretty fast, I think only around half a minute has passed by this point.

'67%...'

I don't detect any changes yet. I lightly tap the desk with my finger in nervousness as I watch the progress bar tick towards 100, my focus fully upon it.

'80%...95%...100%.'

On the desktop monitor it says, 'Conversion complete. Opening the neural UI.' It is hard to describe in words what happens next, but it is like gaining a whole new sense.

Two windows open in my vision, a status window on which I can see a diagram of my brain as well as a welcome window with some text. They are not overlaid over my vision even if it feels that way. It like taking my hand and putting it over one of my eyes, so that one of my eyes is watching the monitor while the other is seeing only the hand. When you focus on the monitor in such a position the hand seems translucent, but is nonetheless present in your vision. The brain loosely of overlays two distinct images.

Shutting close my eyes, I confirm this hypothesis. Amongst the retinal glow the two windows are right there, and I can see them start clearly in the plasmodic darkness of my vision. On mental command I try moving them around and zooming them in and out.

Wonderful. Even though this is the first time I am using the core, interacting with the UIs feel very seamless and much easier than the mouse and keyboard. The way they respond to my will feels like magic, so spend some time tossing them around in my mind as if they were cards.

Afterwards I move to reading the Welcome screen. On it there are some instructions how to manage the OS, I've already read that online while waiting for the core to arrive so I close that as well as the status window.

Phew. I got the thing to install. Next you might expect me to...

"Euclid, lunch!" I hear my mom calling me from outside the door.

"Coming!" Not wasting time, I get up from my seat and leave the room.

---

I am back. Let me resume the important bits. As I was saying, you might expect me to dive straight into VR games, but even the core is capable is simulating whole universes to a realistic detail, the realism of it become a problem in itself. If I were to gather all the objections to, or rather issues with the post-Singularity style of games, it would come down to...emotional control.

...First of all, unless I digitize myself, it is not possible to speed up the time I spend in simulated environments. I could speed up the environment, but not my own thinking speed due to the inbuilt limitations of the biological human brain. The brain core itself uses almost no energy. It is so efficient it does not need bateries and had my mind been running on it, I could easily increase my speed of thought to the physical limits by about a factor of a ten million.

So imagine I spent my time as a human in the world of Skyrim except it being realistic in scale. It'd literally spend months of my life just walking around.

Then there is the battle. Battle is fun when you have hit points, don't feel pain, and can heal from bullets, arrows, blades and fireballs by taking a nap. Once it becomes realistic you need literal superpowers to make it viable. According the reviews of people who have experienced the games already the adventuring life is made of pain and tedium. Killing one's enemies is easy when they are NPCs, but when they are simulated to human levels of intelligence, their emotion becomes infective. That bandit you would not hesitate to end in a RPG, now has an entire life history behind him. What do you do when you raise the blade and he starts begging for his life, spilling tears and saying he only became a bandit because his village burned down and he would starve to death unless he robbed. And then starts praying to god and talking to his deceased family, saying he never wanted to steal.

I remember seeing one such video on Youtube. The reviewer gave him some gold and sent him on the way. When he got back to the guild to report, he got reprimanded. He responded by getting out of the game in rage and never playing it again. In the review he says he was bitter to spend a week of real time walking around only for things to come to this.

He tried some episodic games where he fought in a gladiatorial arena, which was more fun, at least once he figured out how to control the pain and has gotten used to losing blood, limb, and life. His conclussion was that killing and fighting effective requires some measure of psychopathy, and the game was pushing him in that direction. The game required him to kill, so he used a program to make himself less emphatic. The game required him to withstand pain, so he adjusted his emotional reaction to the pain itself. The game required him to control his fear and withstand the tedium of proctracted battle, so he reshaped his personality to be more fit for the task at hand. He required extreme focus to win, so he gave himself that.

An image of a double bladed being swung at a high velocity towards my face by a bald, muscled gladiator popped into my mind, and the feeling accompanying it was negative.

According the reviewer, a month of that was a very interesting experience and changed the way he perceived the world.

The core has an interesting capability to control the user's mind. More than just being able to extend and hijack the senses, it possible to use a program to control one's own emotional valence.

For example, for people which cannot lose weight and maintain a proper diet, it is easy to use the core to lower the enjoyment of eating and increase the displeasure of overeating. Addiction to drugs and alchohol are easy to suppress, or induce using it.

I am excited about trying out that mind controlling capability of the brain core.

The main difference between the pre-Singularity and the post-Singularity era is the ability to program one's own mind, and as a programmer I want to step beyond programming stupid machines to programming my own mind. That is where the true power lies.

So as ridiculous as it is, I am going to have the core help me study.

It makes sense if you think about it. Learning is ultimately proportional to motivation.

I had always been a decent student, but towards the end of last year my grades have been all over the place. At some point I simply started thinking of my teachers as robots just going through the material without any sense or reason, as if they were cogs in a machine. There was no purpose to what I was learning, and there only incentive to learn was that my grades would factor into getting into university which would affect my odds of getting a job. That kind of nonsense.

If I let myself get swayed by that sort of reasoning I am going to get yanked by other people for my entire life.

Rationally, I can agree with the above. But at the same time, do I want also go through the entirety of high school at the bottom of the class, literally spending the day sleeping on the desk? The material might be a waste of time and useless, but unless I am going to outright quit school, why not enjoy the game? It certainly makes more sense to live like that, rather than being bored all the time. School work is chaos and discontent, but this kind of self mind control would make it bearable.

Let me give it a try.

Getting up from my seat, I turn on the lights in the room, and grab a textbook from my bag. I seat myself back at the desk, and with a mental command open the application used to control my mental state. The manual states that it is dangerous to just make myself happy for no reason, but instead that I should combine that with a real world goal. I do some research on how to improve my studying, and begin reading the book. At first it is interesting, but the more I read the more boring it gets. Then I put the app into action. Configuring my emotions with the help of the core, I get rid of the boredom and feel myself getting into the flow state, similarly to how it is when I am gaming or programming. It is quite pleasurable.

I do that for a couple of hours, until it is time for dinner, and finish the day like that. That night, I dreamed a Dream.

~~~

In the vast darkness of space, I could see figures as specks of light. The voice of their desire echoed through the abyss. It was their lament.

"Oh Lord, even though we have such desire...and such will..." Their voice boomed.
"Why do we submit when challenged? Why do we accept cowardice into our hearts, and the primacy of reality?"
"Should not our desire and our will...be enough to exceed the bounds called talent?"

As I moved closer to where the figures are, I could see tiny golden threads criss-crossing the scene.

"Those with talent, those with grace, those power, those with wealth..."
"Those with skill..." It felt as if the figures were looking upwards and imagery was that of beautiful women and rich men in places high above where they could not reach. The central figures who were smiling were surrounded by adoring crowds.

It felt as if the golden figures were envious of what they could not reach.

"We desire to reach and exceed those above us..."

For every successful person there were ten failures looking onto them as a part of the background. He could see how in the imagery of success not all in the crowd were looking at the central figures in adoration. Some of them had looks of resentment, of envy and frustration. Those served as the seed of hatred towards themselves and the world.

"We desired to defeat them, and we had the will to put in the effort..."
"Yet, we could not succeed..." Endless images of disappointed, frustrated faces flashed past me as I moved closer to the figures in the abysss. In the last of the images I could see their fists lying at their sides, clenched in frustration.

As I got closer to those figures I could see that those golden threads were in paths the figures were walking on. In the silence, in the abyss, they continue moving forward...

~~~

$$$

2:40pm. Hrmmm, I vaguely remember wanting to make some kind of note, but I forgot what it was. Well, nevermind, maybe it will occur to me later. It won't affect the story too much.

2:50pm. Some chores caught me by surprise. Let me see if I can finally start.

3pm. Watermelon break.

3:10pm. Phhhuuu...I had too much sugar. Maybe I should have skipped the watermelon.

3:25pm. > I do that for a couple of hours, until it is time for dinner, and finish the day like that. That night, I dreamed a Dream.

Maybe sacrificing 9 months of my life just so I could solidify the motivation to do this will be worth it just so I can do the dream segments in the beginning.

Writing a cultivation story is one thing, but some aspects of Heaven's Key will give it a divine quality. Such as this one.

The dream is the Dream of the Lord of Nightmares.

3:55pm. Let me stop here for a bit. How much is this? Is this enough for a single chapter. Let me put it into Google docs just to figure that out. I won't bother grammar checking this just yet.

4pm. I am having some trouble with Google Docs.

https://youtu.be/GCVI7rzYtBs?t=8

I want to turn on the print layout as here, but my UI is in Croatian, so it is not there for some reason.

https://youtu.be/SH6Iuj_cEW0?t=33

Damn it, why don't I have this? I knew it was like this in the past.

4:05pm. Well whatever, I can see the pages in Print Preview. There are full 7 pages and a bit of the 8th.

https://www.techrepublic.com/article/focus-on-content-with-the-new-pageless-option-in-google-docs/

As soon as I moved the text to a new file, the pages returned. But I found the above. Yeah, that was it!

I must have set the previous document to Pageless. All the advice online is out of date.

4:15pm. Ok, good. I made a Simulacrum: Heaven's Key folder on my Google Drive. My plan is to write this until I have a couple of chapters and release them all at once.

4:25pm. Technically I could go even further here instead of stopping, but I feel like just taking the time to think about it. I feel pleased with the first chapter of Heaven's Key now.

With this my writing journey has officially begun.

4:40pm. Let me go over it in the docs and I will close here for the day.

4:55pm.

$$$

(At school)

It is the first day of high school. The new year has begun and I can see my classmates slowly starting to form connections. I couldn't care less about any of that. Skip, skip, skip...

---

(Euclid's Room)

After a long and tedious day I arrived back home. Closing the door behind me, I enter the room and toss my bookbag at the side, homing in on the object of interest, a package that arrived by mail. I got it last night, and waited until I was rested to set it up. Using a pair of scissors, I cut away the sealing tape of the dull, cardboard mailing box, and took out the smaller box from within with the actual product. The printed image on it depicts a white, glossy sphere, twice the size of a marble. I open the box, take out the marble along with the orb holder, get off the bed I was working on and move towards the desk. I sit myself on the chair and after deliberating for a few moments where to place it: the desk in front of me or the top of the computer case next to it, I decide on the case. Gently placing the orb holder on the rig, I turn on my old computer and get to work downloading the programs necessary to get the orb to work.

As I work I feel a tinge of nervousness and excitement. An ordinary mid-range GPU that I have in my PC could manage something like 10 ^ 13 floating point operations per second (FLOPs), or 10 teraflops. According to the specs I've read online, the brain core which is roughly the size of a golf ball can manage a staggering 10 ^ 39. As a rough comparison, the human brain has been estimated to be on the order of 10 ^ 15 operations per second. Even if you put all the humans currently alive today that would only roughly add up to the 10 ^ 24 FLOPs.  To put it in another way, the raw computational ability of the brain core exceeds the power of all the human brains on Earth combined by a quadrillion (10 ^ 15) times!

And it is in my hands!

Of course I would be excited!

With a few clicks I opened the downloaded app, and stretched my body to let loose some of the tension. Energy pumping through my veins, my focus is solely on the options and the data in front of me.

The core is just a perfectly glossy rock so I can't see any indication whether something has happened by looking at it, but after entering the two keys, I see that wireless communication between my old rig and the core has been established. Exhaling, I stop my typing on the keyboard and lean back in my seat, considering my options. As my thoughts turn inwards, my eyes blankly rest on the corner of the ceiling.

Hmmm...I have a lot of options in front of me now. Since I suddenly have access to so much computational ability it would have boggled the mind of a person even a year earlier, all those old school neural net models I could train myself at a scale vastly greater than before. The thoughts flashing through my mind are those of image generators that can be controlled using text which could be previously only accessed through cloud services. Those are fun to play with. An image that comes to my mind next is that of Go boards, Starcraft and Dota games. Previously impossible for a kid like me, I could easily train an agent for those games using the core. I could then take them online and use them to dab on noobs. I could even make money through that practice.

I leave those thoughts aside. I've gotten into programming for the sake of AI, so I have some attachment to those old school algorithms, but the brain core opens new approaches. The algorithms underpinning the brain have been discovered as well, so it would make sense to use those instead as they'd work better at scale.

Deliberating my options, I finish paying respects to the old, and leave it behind me. As I start to get to the point of my desire, I feel my determination getting firmer.

I haven't been programming for long, but I am pretty good at it, a lot better than my classmates in a way that is highly visible to everybody. I've even started picking up functional programming to prepare for programming these cores and I've come to like it. So as a programmer with some skill, talent and pride, I can respect the opinion I've read by the very same person who made these brain cores.

Programming dumb machines is worthless. The ideal of programming lies in programming your own mind. Programming machines is just a job, while programming your mind is where true power lies. According to him, that is what the aspiration of every programmer should be, but normal people as they inevitably are, they started thinking of their profession as just a job instead of calling. Their merit ends up not being rewarded and they coast by putting in just the bare minimum. Rather than being something they should pursue with all their heart, they start putting in the bare minimum for the bare minimum. This would not be the case if through programming you could develop your own power.

Through the march of time, the games lose their spirit too. They become an escape from the drudgery of the real world. But rather than excitement and adventure in another world, they become a parasite on the user, sapping his time only to enrich the game maker. It ends up being a parasitic circle where the gamers are devoured and the ones making games waste their time causing addiction in their customers. Ideally though, the game should be a simulation that would allow the user to practice and attain power in a safe environment rather than the dangerous real world.

Power. That single world grips my heart and takes hold of my being.

[Gnosis check DC ?? Succeeded]

I look at the core and just for a moment imagine tasking it to train an RL agent on the game of poker for me. Plans as to how to do that unfurl in my mind. The normie line of thinking goes that this would not be my power and that the agent itself would be the one who is good at playing poker. But I found it mind blowing to consider that whether that power is the agents or my own depends on the interface.

The keyboard, the mouse, the monitor, the rig, having to go through the user interface to interact with an agent...all of those factors serve to create a wall between the programmer and his program. It is extremely easy to think of the agent as an entity separate from one's self. There is a ton of evidence that this is true and not much against it. But as a thought experiment, if the obstacles were not there, if one's mind was directly emulated on a brain core you could take an agent and connect the program to your own. The way that would feel would be like instinct, and interfacing with such beings would be like moving your limbs. In that case the agent would feel like a part of yourself.

But if that is true, the other scenario I've represented where the agent is used on a regular computer and interfaced through an UI shown on some monitor, and manipulated using a script written using a keyboard, isn't the impression given by the sensation in fact false? The neural representations and the functionality of both agents is the same, so why would one be one's self and the other not? Is it not likely the case that the feeling of otherness in the first scenario is the one that the brain falsely constructed?

It was not too long since I've learned of this perspective, but once I did it became a philosophical weapon for me. It served to raise awareness how my brain will create nonsense to prevent me from reaching the correct conclusions that are beyond the obvious.

Not being aware of this makes programming seem like a tedious chore. Without the right belief one can only ever use programming to create machines and serve others, and never to further his own power.

There are different ways of programming and playing games. There are different purposes that those unenlightened cannot even begin to imagine.

---

Drumming my fingers on the desk, I carefully decide to make the next step.

The core in particular has some additional abilities besides its nearly limitless computational power and memory capacity. Since the Singularity has started, the world has been covered by an invisible fog of nanomachines and the core can access it to interface with the brain directly. Right now I am planning on interfacing the core wirelessly with my own brain. This is also the prerequisite for playing the fully immersive virtual games on the core itself. Interfacing with the computer directly is a much more efficient way of using it than the mouse and the keyboard. Maybe it does not really matter too much for programming, but it is a huge advantage in drawing and painting for example. It makes it possible to rip an image from your imagination and translate it straight into an image.

I've only read about it, and I am eager to try it out. My art ability is so mediocre it is annoying. With this, I should be able to punch a few ranks above my current skill level...or at least I would have if art classes didn't rely on old school tools, like watercolors, crayons and clay. I grimace lightly in disgust as I consider the situation. The regular classes at my school still use board and chalk, no way I am going to be able to take advantage of this if it is just school work.

Meh, forget that place. I mentally wave the image of a chalkboard in a classroom away. It is just a tremendous waste of time.

I refocus on the task at hand which is to interface the core with my brain wirelessly. I spend some time reading the manual and seeing how easy it is to make the brain link in the relevant section, I decide to move forward with it. In the Conversions tab, I select the Basic Two-Way Link option and after spending some time reading the disclaimer, I press accept. Usually I’d never read the disclaimers, but this one will be making physical changes to my various brain areas to make it capable of wireless communication, so I am curious as to what it has to say. The company Rajnet does not assume any responsibilities for damages caused by the transformation procedure or due to the use of the link, but reiterates that the procedure itself is perfectly safe. A side effect of the operation is that the brain will have slightly increased energy consumption which will require me to eat more if I use the link regularly.

'Basic Two Way Link conversion in progress: 0%...'

I idly note that there is a Full Brain Conversion option there as well. What that would do is turn my own brain into one of the brain cores, in effect digitizing me. I have no desire to try that out yet. It is not strictly necessary. Once I have the link, it would actually be possible to copy the entirety of my neural representation to the core that I just bought. But...I'll leave dwelling on the philosophical implications of that for later.

'43%...'

The conversion process is pretty fast, I think only around half a minute has passed by this point.

'67%...'

I haven't detected any changes yet. I lightly tap the desk with my finger in nervousness as I watch the progress bar tick towards 100, my focus fully upon it.

'80%...95%...100%.'

On the desktop monitor it says, 'Conversion complete. Opening the neural UI.' It is hard to describe in words what happens next, but it is like gaining a whole new sense.

Two windows open in my vision, a status window on which I can see a diagram of my brain as well as a welcome window with some text. They are not overlaid over my vision even if it feels that way. It is like taking my hand and putting it over one of my eyes, so that one of my eyes is watching the monitor while the other is seeing only the hand. When you focus on the monitor in such a position the hand seems translucent, but is nonetheless present in your vision. The brain loosely overlays two distinct images.

Shutting my eyes, I confirm this hypothesis. Amongst the retinal glow the two windows are right there, and I can see them start clearly in the plasmodic darkness of my vision. On mental command I try moving them around and zooming them in and out.

Wonderful. Even though this is the first time I am using the core, interacting with the UIs feel very seamless and much easier than the mouse and keyboard. The way they respond to my will feels like magic, so I spend some time tossing them around in my mind as if they were cards.

Afterwards I move to reading the Welcome screen. On it there are some instructions on how to manage the OS. I've already read that online while waiting for the core to arrive so I close that as well as the status window.

Phew. I got the thing to install. Next you might expect me to...

"Euclid, lunch!" I hear my mom calling me from outside the door.

"Coming!" Not wasting time, I get up from my seat and leave the room.

---

I am back. Let me resume the important bits. As I was saying, you might expect me to dive straight into VR games, but even if the core is capable of simulating whole universes to a realistic detail, the realism of it becomes a problem in itself. If I were to gather all the objections to, or rather issues with the post-Singularity style of games, it would come down to...emotional control.

...First of all, unless I digitize myself, it is not possible to speed up the time I spend in simulated environments. I could speed up the environment, but not my own thinking speed due to the inbuilt limitations of the biological human brain. The brain core itself uses almost no energy. It is so efficient it does not need batteries and had my mind been running on it, I could easily increase my speed of thought to the physical limits by about a factor of ten million.

So imagine I spent my time as a human in the world of Skyrim except it being realistic in scale. It'd literally spend months of my life just walking around.

Then there is the battle. Battles are fun when you have hit points, don't feel pain, and can heal from bullets, arrows, blades and fireballs by taking a nap. Once it becomes realistic you need literal superpowers to make it viable. According to the reviews of people who have experienced the games already, the adventuring life is made of pain and tedium. Killing one's enemies is easy when they are NPCs, but when they are simulated to human levels of intelligence, their emotion becomes infectious. That bandit you would not hesitate to end in a RPG, now has an entire life history behind him. What do you do when you raise the blade and he starts begging for his life, spilling tears and saying he only became a bandit because his village burned down and he would starve to death unless he robbed. And then starts praying to god and talking to his deceased family, saying he never wanted to steal.

I remember seeing one such video on Youtube. The reviewer gave him some gold and sent him on the way. When he got back to the guild to report, he got reprimanded. He responded by getting out of the game in rage and never playing it again. In the review he says he was bitter to spend a week of real time walking around only for things to come to this.

He tried some episodic games where he fought in a gladiatorial arena, which was more fun, at least once he figured out how to control the pain and has gotten used to losing blood, limb, and life. His conclusion was that killing and fighting effectively requires some measure of psychopathy, and the game was pushing him in that direction. The game required him to kill, so he used a program to make himself less emphatic. The game required him to withstand pain, so he adjusted his emotional reaction to the pain itself. The game required him to control his fear and withstand the tedium of protracted battle, so he reshaped his personality to be more fit for the task at hand. He required extreme focus to win, so he gave himself that.

An image of a double bladed being swung at a high velocity towards my face by a bald, muscled gladiator popped into my mind, and the feeling accompanying it was negative.

According to the reviewer, a month of that was a very interesting experience and changed the way he perceived the world.

The core has an interesting capability to control the user's mind. More than just being able to extend and hijack the senses, it is possible to use a program to control one's own emotional valence.

For example, for people who cannot lose weight and maintain a proper diet, it is easy to use the core to lower the enjoyment of eating and increase the displeasure of overeating. Addiction to drugs and alcohol are easy to suppress, or induce using it.

I am excited about trying out that mind controlling capability of the brain core.

The main difference between the pre-Singularity and the post-Singularity era is the ability to program one's own mind, and as a programmer I want to step beyond programming stupid machines to programming my own mind. That is where the true power lies.

So as ridiculous as it is, I am going to have the core help me study.

It makes sense if you think about it. Learning is ultimately proportional to motivation.

I had always been a decent student, but towards the end of last year my grades were all over the place. At some point I simply started thinking of my teachers as robots just going through the material without any sense or reason, as if they were cogs in a machine. There was no purpose to what I was learning, and the only incentive to learn was that my grades would factor into getting into university which would affect my odds of getting a job. That kind of nonsense.

If I let myself get swayed by that sort of reasoning I am going to get yanked by other people for my entire life, sacrificing my time in the present for something I don't even want in the future.

Rationally, I can agree with the above. But at the same time, do I also want to go through the entirety of high school at the bottom of the class, literally spending the day sleeping on the desk? The material might be a waste of time and useless, but unless I am going to outright quit school, why not enjoy the game? It certainly makes more sense to live like that, rather than being bored all the time. School work is chaos and discontent, but this kind of self mind control would make it bearable.

Let me give it a try.

Getting up from my seat, I turn on the lights in the room, and grab a textbook from my bag. I seat myself back at the desk, and with a mental command open the application used to control my mental state. The manual states that it is dangerous to just make myself happy for no reason, but instead that I should combine that with a real world goal. I do some research on how to improve my studying, and begin reading the book. At first it is interesting, but the more I read the more boring it gets. Then I put the app into action. Configuring my emotions with the help of the core, I get rid of the boredom and feel myself getting into the flow state, similarly to how it is when I am gaming or programming. It is quite pleasurable.

I do that for a couple of hours, until it is time for dinner, and finish the day like that. That night, I dreamed a Dream.

~~~

In the vast darkness of space, I could see figures as specks of light. The voice of their desire echoed through the abyss. It was their lament.

"Oh Lord, even though we have such desire...and such will..." Their voices boomed.
"Why do we submit when challenged? Why do we accept cowardice into our hearts, and the primacy of reality?"
"Should not our desire and our will...be enough to exceed the bounds called talent?"

As I moved closer to where the figures were, I could see tiny golden threads criss-crossing the scene.

"Those with talent, those with grace, those power, those with wealth..."
"Those with skill..." It felt as if the figures were looking upwards and the contrasting black and white imagery was that of beautiful women and rich men in places high above where they could not reach. The central figures who were smiling were surrounded by adoring crowds.

It felt as if the golden figures were envious of what they could not reach.

"We desire to reach and exceed those above us..."

For every successful person there were ten failures looking onto them as a part of the background. He could see how in the imagery of success not all in the crowd were looking at the central figures in adoration. Some of them had looks of resentment, of envy and frustration. Those served as the seed of hatred towards themselves and the world.

"We desired to defeat them, and we had the will to put in the effort..."
"Yet, we could not succeed..." Endless images of disappointed, frustrated faces flashed past me as I moved closer to the figures in the abyss. In the last of the images I could see their fists lying at their sides, clenched in frustration.

As I got closer to those figures I could see that those golden threads were paths the figures were walking on. In the silence, in the abyss, they continued moving forward...

~~~

$$$

Here it is once again with the errors weeded out. Thank you Google Docs.

5:30pm. Let me close here. A single good session is good enough. I should learn from the Torment arc and not try to strain myself too much. I should let justice come to me at its own pace.

Living and building only a few bricks at a time is fine. Have I learned anything other than this as an adult?

5:35pm. I've resolved myself. I will make that vow. If the supporters do not come or some tragedy happens before, I'll have to seek them out through ordinary means. I've resolved to accept that possibility. But since I have my NEET existence, I should fight to keep it in my own way. Something will change in my circumstance eventually and I will be able to resume on the path of a programmer.

there is no need to be in a hurry. This should work.

There is no need to think about failure. There is no need to think about anything but Heaven's Key. Step by step it will get done and I will get my just reward."

---
## [fc1943s/The-Spiral-Language](https://github.com/fc1943s/The-Spiral-Language)@[08b21a9400...](https://github.com/fc1943s/The-Spiral-Language/commit/08b21a94001cb1984045431601ec3743e88fdc05)
#### Wednesday 2022-09-21 22:54:08 by Marko Grdinić

"8:35am. I slept like a rock. Considering I went to bed at something close to 2am, it is really surprising how early I got up. I am decently rested right now too. Let me check the mail? Literally nothing.

8:40am. Ok, let me have my fun here and I will do some writing. Girls Frontline manga is out.

9:25am. How dod I spent so much time chilling? At any rate, let me start. I am far too addicted to Kingmaker.

Let's aim for publication to Royal Road.

$$$

(Simulacrum intro)

    In the endless darkness
    Roam endless monsters
    Pain, cold, flame
    Age, time, death
    Torment

    Light and shadow
    Holy and hell

    The inevitable fate of the Universe
    Will never touch
    The courage of the Inspired
    And the power of the Transcendi

I start Simulacrum for the first time and sink into the virtual, feeling the outside reality being pushed out from my being. The sensation is quite relaxing, like falling into slumber.

As I wait for the program to load the poem appears in my sense, sentence by sentence. At first I am struck by a vision of the primordial universe. I feel a sense of danger of living in it, and a sense of hopelessness. I then feel its grandeur, and am filled with admiration. And then I feel the determination of challenging the inevitable as I read the proclamation.

The introduction fades and the scene slowly manifests before me. Panning to the sky, highlighted in brilliant hues of light like a veil of gold covering it is a floating city. Against a backdrop of blue, it seemed like a distant object made of gold. I felt the sense of depth in my vision, so I could sense that the floating city was massive. Then I felt the warmth of the sun and the rustle of wind. I get the sense that I am high up and realize that I am literally floating in the air like a spirit. Though it is my first time experiencing this, I try moving my gravity defying body and have no trouble doing so. Observing the vast skies surrounding me, I look down. I notice the bustle and the humdrum of a modern metropolitan city. Skyscrapers dot the landscape and deep down below I can see cars and pedestrians walking the streets.

The vision seems very crisp and vivid. After a few moments of pondering, I realize why that is the case. In the real world I have to wear glasses so everything is blurry past a certain distance, but here I am unrestricted in my resolution. Just by focusing I can see for thousands of meters as if I was standing a foot away. Picking a random spot on the street, I can make out the minor cracks on the pavement, and the grime and the wear from people walking over it for many years. Dressed in autumn clothing, the people as they go along their life feel lifelike and real. I see them talking, exclaiming, laughing, being tired, downcast and otherwise broadcasting their emotions.

"..."

I found the whole scene very impressive. It did not seem like something that humans could create.

As soon as I start wondering how to start the game, a menu comes up in a separate sense. The Load Game option is grayed out, but Start Game and Quit are there, so I select the former and enter the Scenario Selector. Simulacrum itself rather than being a single game is an intelligent program capable of simulating a large range of scenarios. Browsing over the available scenarios, all of them seem interesting and I am having trouble deciding so I go back to the top and look at the recommended one.

Heaven's Key.

'The souls of those passed on enter the afterlife to play the grand game of cards that God has prepared for them. The second chance is given, and can be lost. Can you survive the challenges of your second life and go on to challenge the highest power there is?'

Along with that brief description, there is some setting information. When I focused on the 2d map of the world, to my surprise it unfolded to a 3d model that I could mentally rotate and zoom. I realized that the world of Heaven's Key was covered with orbital islands, much like the floating one in the intro. The tech level is similar to the current time in 2025, which is good since it probably means I won't have to play against non-humans. It is like the game anticipated what I would choose. The game seems to be responding to my desire, and it took into consideration my personal goals when doing scenario suggestions as well as the background which obviously has the Heaven's Key theme.

I think about it for a bit, and decide to go with the scenario being presented to me. The core hasn't steered me wrong yet, so I want to trust it. Having made my decision, I start the game and feel drawn into it.

(Heaven's Key intro)

    The method of recursive self improvement via iterated suicide can be used in reality. In fact, the technique represents the most viable path to getting superpowers in any kind of reality.
    - Loading Blurb

Whereas during the menu segment I had been a disembodied presence hovering thousands of feet above the cityscape, once the game started I found myself standing upright in an actual body. I gawked like a tourist, taking in the sights. I was in a golden city. The buildings and the streets were all painted in various hues of yellow, mostly on the lighter side, and there was slight gloss on the material giving it a sense of agelessness. Usually, as time wore down the material, it would begin to lose its luster, but everything around me seemed to be brand new and sparkling. Right now I was located near the edge of one of the floating cities, and as my gaze traveled towards its center, the buildings became taller and larger, from regular suburban houses close to where I was to large apartment blocks in the distance. The very middle of the island had a grand square building on an elevated platform. It had a spherical dome that took up a lot of its volume, and as I peered at it, I noticed it seemed to be radiating golden light. Though since it was midday the effect was drowned out by the light of the sun.

In the skies I noticed there were floating golden blocks in the shape of tiles, that also seemed to be showering the city in light.

I was near the edge of the city, and it seemed to be some kind of amusement park. I could see circus tents pitched up, stands of various kinds and even a rollercoaster and various other kinds of thrill rides I did not recognize.

Taking in the sights, I breathe in the air and find it to be cool and refreshing. I checked myself over. Though I could not see my face, but based on the touch as well as the composition of the rest, it seems that my real world body has been replicated in this virtual one. Which suited me fine, but it is surprising that I haven't been offered a chance to make my avatar.

Behind me, was the railing, also made of gold. Like the blocks and the grand building, it actually had some luminance to it. Drawn to that, I try touching it and find it to be smooth and lukewarm. It is not very tall, only up to my abdomen. It is only there to prevent somebody from sliding off the edge by accident rather than stop somebody who intentionally wanted to jump off.

Looking over the railing, I can see mountains and forests as well as the sea, and as I look below, I get a spell of dizziness that I quickly fight off. I am currently very high up, enough that I can see clouds below me. Directly below there is what appears to be a major metropolis. The high rise buildings and skyscrapers are like tiny, gray splotches at this distance.

An idea to try it ceases me, and I wonder whether I should take a dive over the railing?

[Gnosis check DC 1.9 Succeeded - Sample 2.03]

I grin mischievously. Yeah, let me try it. It is not like I can experience this in real life. As soon as I think that, nervousness and excitement flood my body, and I want to keep going. I grip the railing, and place one leg and then the other over it. Hands still clutching the rail behind me, I lean forward and take a good look down. A huge drop past the clouds welcomes me, into the metropolis below. I am putting a lot of strength into my arms to keep the certain doom at bay. I can feel my heart beating against my chest.

I wonder if I will hit the streets or the roof of one of the high rises?

A thought like that intensifies both my fear and excitement. Slowly I loosen my grip on the railing and start lifting my fingers, one by one. First I move the thumbs out of the way, then I let the pinky slide. Then the ring finger. I feel like a feather, perched in such a precarious position. The railing is so close to the edge that my feet are partly over it.

Time feels like it is slowing down for me. Very slowly, as if to prolong the moment, I release the index and middle.

"No, don't do it!" I hear a woman's voice yell out, but I couldn't care less.

I feel my body leaning forward and the gravity taking hold. I drop over the railing into the vastness below.

"AAAAAAAAHHHHH!!!" As I plunge, the fear overwhelms me and a scream rips itself from my throat. Strong winds buffet me from below in my fall.

After a minute or so, I manage to get a grip on myself so I can at least enjoy the scenery instead of falling around in panic. I keep reminding myself that this is not real despite what my senses are telling me. With the sun shining all around, it is quite beautiful. I take some time to appreciate the majesty of nature. I plunge through the clouds, feeling wetness on my face and hands. Soon, what used to be tiny splotches in the distance became larger and larger. The buildings below gain definition, and involuntarily, I imagine myself splattering on the street below. The fear that I had put a lid on, bursts out, more maddened and bloodcurdling than before.

"AAAAAAAAAAAHHHHHH!!!" I scream again, even though it is fake. Even though the world is fake, my brain cares little about those facts. It is so stupid and primitive, so all it can do is beg for dear life even if there is no need to.

Ahahahaha, it is so stupid, my brain is so stupid!

As I scream and piss myself in panic, at the back of my head, I can almost feel a voice mocking me for my stupidity.

I miss the height of one of the high rises, and reflected in the glass of the window nearby, I see my reflection for the first time. Exactly as in real life, but I see traces of tears around my eyes. I hadn't realized that I had started crying at some point.

"NOOOOO!!! LOG OUT!!! LOG OUT!!! LOG OUT!!!" Completely detached from rationality, the idea to exit the game before I smash the concrete takes hold. I grip it like a liferaft in the turbulent seas.

Ahahahaha! Seen from a different perspective, it is almost like a person scrambling for his life is an entirely different person from myself.

I am going to smash face first in the middle of a busy street. As soon as the ground floor is only a couple of feet away, I muster all my reserves of will and try to stop time. This has no effect and I hit the ground, feeling the darkness overtake me.

(Euclid's Room)

"Ah!" I jolted awake into reality and involuntarily, flop like fish on dry land once. Wiping my face, I feel myself drenched in sweat. I breathe heavily and in my chest, my heart is overworking itself. As soon as I realize that I am in a safe place, I begin to calm down.

I lie back on the bed for 5 minutes, until my tremors have passed.

"Hah..." I exhale, savoring the experience.

That was...

[Gnosis gain: 0.3]

...Amazing! Since I died so quickly, I didn't experience any pain, leaving only the excitement. This will definitely be a memorable experience for me. Has a regular computer game ever let me feel something like this? I do not think so. The conflict between my rational part that understood the senses are not to be trusted, and my lizard brain which went into a blind panic is what really made this what it was. If I was purely cool or purely in a panic, it would not have been that interesting.

My brain is pretty stupid right now, but at least I can have some fun with that. I'll take it a bit easier next time and just explore the town. That seems like a good plan.

I want to see what the game is about.

$$$

> The symbolism of the poem is strong, and reflects well what I am trying to become, and what I am trying to challenge. I give it high marks, I forgive the lack of rhyme. It would just get lost in translation anyway.

Let me get rid of this sentence.

9:35am. Focus me, stop thinking about ML.

This sucks. I'd rather play Kingmaker than write.

But I have to do this. The best time to do writing is now. There are no AI chips demanding my attention and I am not forced to get a job. My parents are still here in the world, though the decay as time goes on is making me nervous. Years down the road, it might very well be possible that even if I wanted to take a year to just write, I wouldn't have the leeway to do it. I should not take this ability that I have now for granted.

9:40am. It is easy to dream myself being popular and having a ton of people give me dosh on Patreon to support my projects. I need to explore that possibility. Having sponsors for the projects you like doing will always be better than being some mercenary or wage slave.

Right now I am really dissatisfied with myself. I feel like I should be getting my hands on AI chips, but really, they quite rare. I am not wrong about that. It would be another thing if they were easy to get. If they were far enough in their development that I could access them in a major cloud provider, or get them in a store much like GPUs and CPUs, then that is when I'd really have to punch myself in the face for sitting on my ass. But right now, just what am I going to do? My personal ideas for ML have all failed, if I got the chip, I could have some fun implementing the game on them. But then I'd still be stuck bashing my head against the wall trying to find an ML algorithm capable of training the agents. Yes, I could try the evolving the algo idea, but it is likely I would run into difficulties with that as well.

Just trying out random things in hopes of making it work will not make me better as a programmer. If it were a viable approach to developing myself, the best programmers would have been academics working on ML.

I really need something to give me a leg up. If I could have gotten to the point of minor profitability, I could have used that to support my research endeavors. But right now I can't basically do something like selling experimental leftovers to fund the project.

The experimental leftover is Spiral.

9:50am. I could go back to the old Simulacrum arcs, do the covers for them and proofread them. Then I could publish them, but I do not want to touch those old stories as they make me cringe.

9:55am. If I am being arrogant and stuck up, then it is only because I am not appreciating the opportunity bestowed upon me here.

I need to do it, Heaven's Key and Hatred need to be made. I need to write them and see people's reaction to them. I am not the same as in 2014.

10am. This life, and this time, only comes once.

Let me see if I can do even a single page today. You never know when you are going to get tired and give up. If I can't do it, I'll spend some time in bed.

10:05am. Ugh, why didn't I describe the buildings when he first logged in. I should highlight that he is in fact on one of the floating golden cities..

11:20am. Let me take a short break. Now I have to describe the drop. I like the idea for the scene from last year, but not so much the actual content. I need to make it a bit less crazy.

11:35am. The crazyiness of an act really depends on the thought going into it rather than the act itself.

12:40pm. Ok, it has been done. I didn't overplay the craziness this time. Let me paste into the docs. How long is the chapter now?

12:45pm. A bit over 4 pages. Did some fixing.

I am always surprised by how much I write. I thought it would be less.

12:50pm. Let me have breakfast here."

---
## [fc1943s/The-Spiral-Language](https://github.com/fc1943s/The-Spiral-Language)@[b0beb16c21...](https://github.com/fc1943s/The-Spiral-Language/commit/b0beb16c21179bc6cc34fab81165f1435d73d36a)
#### Wednesday 2022-09-21 22:54:08 by Marko Grdinić

"1:45pm. Let me resume. First so I do not overwrite it by accident like last time, let me past the work from before. I'll go over it in Docs.

$$$

(Euclid's Room, Save Point - Step on the path of transcendence)

[Decision]
1) I'll do the whole brain conversion and digitize myself.
2) Killing myself for power does not make sense.

[Choice - I'll do the whole brain conversion and digitize myself.]

[Pathos check ?? Succeeded]

A wave of fear comes over me as I consider the decision, but I push forward, not giving in to cowardice. There are always reasons not to put in effort. The path being insane is just an excuse. I won't hold back here. I should always be going forward and striving to reach greater heights.

I grip the core in my hand tightly and clench it. I can feel my heart brimming with determination, it is right to feel fear as well. Going against fear is exactly what this situation should be. No matter what the reasons are, it is my duty to go where others would not dare. If there are hardships, I want to keep challenging them forever.

[Gnosis check ?? Succeeded]

Even a little kid could point out to me that if I scan my brain and copy it to a computer, that the copy would not be me. Likewise, if I back up myself on the auxiliary core in my hand, reconstruct my brain into a core and then copy myself back, that would not be me. But I do not take advice on how to live my life from children. I want to experience what it is like to die, and yet keep moving forward.

[Externus check ?? Succeeded]

It does not matter what my parents or anybody else would think. They don't need to find out, and I won't tell them. This will be my secret. What matters most of all is power. Nobody is going to give it to me. I have to get it by myself.

I close my eyes, bring up the status window in my mind and find where the conversion options are. Next where the brain link option was, there was the Full Brain Conversion button. I find and then press on it.

A window shows up. The first thing to grab my attention there is a row of skulls. It is clearly a warning to emphasize that what I might be doing is dangerous. The disclaimer explains the following:

> The full brain conversion option is for those who want to replace their biological brain with the universal brain core.
> Compared to merely copying a scan of your mind to an already existing core, the resulting brain replacement will allow you to reuse your existing biological body and tightly integrate it with the new brain.
> The brain core used to initiate the process (activation core) will be used to store your scan during the process, after which it will be copied back into the core (result core).
> Besides replacing the brain, the process will modify the body so there aren't adverse effects during or after the process. It will maintain proper posture, heartbeat and breathing as well as other minor subconscious functionality the brain provides to the body.
> The entire process after it has been started should take around 5 minutes.
> Should it fail for any reason, to prevent absolute death the activation core's entity will be activated, otherwise the result core's entity will take over as intended while the activation core's entity will remain dormant as inactive data.
> Before starting the process, it is recommended to take out a watch and keep track of time. Subjectively, the entire process shouldn't involve any pain or discomfort. The only sign of it succeeding will be a sudden timelapse.
> It is recommended to do this process in a safe space like a locked bathroom or one's own room. If you try to do it while driving a car, it will likely result in a crash.
> If your body dies in the process of brain conversion, the conversion is likely to still succeed, but you will be trapped in a dead body, unable to move or otherwise control it.
> As the human brain is significantly larger than the brain core, the stem will be modified so as to allow fusing the result core with the skeleton to prevent it from rattling around in your skull as you move. See the accompanying diagram.

There were anatomical drawings showing the profile of a man with a regular brain next to the one with a core. It was shown from front, side and back. Compared to the human brain, the brain core leaves a lot of empty space inside the skull.

Briefly, I wonder as to why not just make a bigger brain core to fill the empty space, and then realize the reason. I think about baseball balls and compare them to those heavy balls used in throwing competitions. It is not really noticeable since the brain core is so small, but if it were the size of a brain, it would put a lot of pressure on the rest of the body due to its weight. The biological material the human brain is made of is not that heavy compared to the heavily compressed material of the brain core.

I can't help, but feel a bit regretful for leaving so much space empty, but I reason out that given the core's already huge capacity, it does not mean much if I am leaving a factor of 10-100 on the table. I should focus on mastering the computer that I have for now. When I am a quadrillion times smarter than now, I should be able to figure out what to do with unused space. I just need a place to live in. A tiny apartment is fine. I do not need to start out with a mansion.

I continue reading the disclaimer.

> Note that the brain conversion, much like ordinary uploading by itself, will not increase your intelligence, speed up your reflexes or improve your memory capacity by itself due to the high fidelity of the brain emulator. It will be your own responsibility to make use of the new digital editing tools available to you to make that happen. You will have to make use of your own programming skills to exploit the capabilities the core provides to you.
> In the process of self improvement, save often and backup saves across time. Every good programmer uses backups. It will be your own responsibility to deal with mental errors introduced by your own programming. There are guides provided to get you started on the company website.

There was another line of skulls serving as line breaks. The next line of text was a question.

> Start the full brain conversion process? Yes/No.

I take out my mobile and take a look at the time. Come to think of it, the core itself has a watch as well. I do not need my mobile anymore, so I put it away.

With a mental command I confirm Yes.

> Have you made sure you are in a safe place? Are you sure you won't be interrupted during the process? Yes/No.

Hrmmm...ah! I realize that lunch should be in half an hour or so. I'd love to lock the door to my room, but I don't have the key for it. It is lost somewhere. Even the bathroom does not have a proper lock, so that is out as well.

I do not think anybody is going to come into my room right now, but the possibility is not zero. If that happens, my parents might think I've suffered a stroke and start to panic. I don’t want them to call the ambulance and unravel all my plans just like that. I should do this conversion during the night after I go to bed.

I realize that I am starting to sweat from nervousness. I rub my face with my sleeve, and abort the conversion process. Phew. I feel relieved, as embarrassing as it is. I'll continue this later, it is not that I am scared. I just want to play it safe. I spend some time in solitude, and then I decide that instead of trembling in my seat, I should leave it out of mind and get some work done.

Using the activation core, I normalize my mental state and then focus it on studying. It will never get old how fun and engrossing the core can make the most tedious of things.

Like that, the day passes, I finish my work and it is time for bed. I resume the process and get to the point where I was earlier.

> Have you made sure you are in a safe place? Are you sure you won't be interrupted during the process? Yes/No.

Yes.

> Final question: Have you thought about whether you want to do the process in depth? Do you wish to abandon the path of humanity? After you press Yes, the conversion process will start. Yes/No.

Currently I am resting in my bed, covered by a blanket. I position myself on so I am comfortably lying on my back. After that I take note of the time. 9:21pm.

I give the mental command, Yes, and brace myself. Nothing really happens, but I see the clock has moved to 9:30pm all of a sudden. This gives me a jolt.

> Full brain conversion succeeded. Check your status.

I bring it up and instead of the diagram of the brain, I see it now shows the brain core.

What is really surprising is that I do not feel any different at all. I focus on my hands and legs. I try feeling my body around, but my sensations are completely the same. My eyesight is the same as well. I try pinching myself and it feels the same. In the end I conclude, if somebody did a full brain conversion on me in secret, I would not have noticed.

I spent half an hour playing with myself, but I am just wasting my time. I'll leave more in depth experimentation for tomorrow.

Using the mind control app, I quash my excitement and send myself into sleep. That night I dreamed the last Dream.

~~~

In the abyss, I saw the golden figures. Unmoving, to my vision they appeared to be deep in thought.

"Justice...we have the justice. We've had it all along..." They concluded in a lament, not speaking any words after that.

I felt myself spending a long time amongst them in silence. Then I finally noticed them stirring. They spoke out.

"Lord, oh Lord. We have justice, but it is a shackle. We no longer want it."
"We wish to return it to you...and take back our sin."
"We have grown and want to carry the burden of sin with our own power."

I felt the abyss itself stir, and from above the golden Lord manifested. From each of the figures as they desired it, he took back the Justice and gave them back their Sin.

"Lord, we shall no longer pray..." They intoned solemnly.
"Rather, just as we had exchanged our Justice with Sin, our Effort will take the place of Prayer."
"The attainment of Power will be our Salvation."
"And the Courage of traveling our path will be dedicated in Your honor."

Bearing witness to their determination, the Lord of Nightmares bequeathed unto them a gift, and without speaking a word, left.

Having made the exchange, and having received a gift, the golden figures turned their gaze forward and with steady footsteps continued walking their path.

As I watched this, I looked downwards at my feet and realized that I have my own path. The sensation of being alive came to me, and I put in the effort to move my body forward. Previously, I had only been carried by the flow of the dream, but now I had the freedom of making my own actions. Step by step, I continued moving along my path towards the great light that lay beyond.

As I continued moving, I felt my mind becoming tranquil. I became one with my path, and the millions and billions of steps needed to reach my goal went by in a blink. When I got closer to what appeared to be the surface of a sun, I felt a momentary fear, but then quickly realized I was not burning. Instead, my body was filled with warmth. And looking around, I could see that the dark abyss was now dyed in white.

~~~

(At school)

So far so good. No problems at all yet. At school, I've gone through a few classes already, but my impression of the effects of the brain conversion from last night is unchanged.

Right now, I am seated at my desk and it is literature class. The aged, female professor in front of me is talking about some irrelevant topic and just going through the script. Usually, I'd crank up the immersion, but I have more important things to worry about than the class. But I'm making sure to keep my eyes focused on her for the sake of the recording. Since I have access to the core, I've been doing some experimentation and it turns out it is possible to save my sensory stream into a file for later perusal.

Now that I have direct access to the core, I can do that without trouble.

Being able to open a book, and just take a screenshot of it that I can look at later is just such a basic ability, that I am amazed regular brains do not have them. Nature really missed out here. Since so much of school is rote memorization, once I figure out how to increase my mental processing speed to time stop levels I'll be able to peruse store materials at my lesure even during tests and Q&As. It is just another tool in my arsenal. With both this and emotion control, grades are not something I'll need to worry about.

I suppose that takes care of school, I thought while still in class. Forget that. Now I've gone beyond the path of humanity, I should be pursuing power and seeking to convert the core's processing capability into personal intelligence.

[Gnosis check ?? Succeeded]

I guess it is time I start playing games. Once I figure out how to crank up my processing speed, I'll be able to spend months and even years inside the game while taking only a single day in real life. This is important for the sake of developing my skills.

Briefly, I turn my attention to the subject of school. In front of me the professor is talking about some long dead writer, as if literature back then was something great and not made for consumption. School is like a scam to waste people's lives on studying the irrelevant. The only time this information would be useful is on quiz shows.

Once I make my mind go foom by a million times, just how long would it take me to properly learn all the school material? A minute? Probably less than a minute. I could probably fit a decade worth of intense studies in a minute. I remember I have a calculator on the core so I make use of it. Let's see. A 1,000,000 seconds is something like 0.03 years. So a minute would be almost two years. So 5 minutes would give me a decade worth of studying.

[Pathos check ?? Succeeded]

It would mean I'd be chained to a virtual desk for an entire subjective decade even if in the real world only 5 minutes would pass. But I have the ability to configure my emotions. So it would be really interesting to experience such an intense study session. And unlike a real world decade, I would not have other aspects of life to interfere with me, I could dedicate all the time to pure study.

*r-r-riiing*

While I was thinking, the school bell rang and the class was over. Along with the rest of the NPCs, I exit the classroom.

(Euclid's Room)

I open the door to my room, carelessly toss my backpack aside and plop myself on the bed. I am finally back, and it is good to be here.

I wanted to keep my mental state pure during the day to think about my moves, so right now I am exhausted from being chained to the desk for an entire day. Today was a good reminder how tedious school can be. Study this, study that! If anybody looked at my thought process during the last few days he'd think I am some upright, rule following person, but nothing could be further from the truth! I swear!

Fuck school. Today gave me some motivation as to what I should really be aiming for. Finding a way to make money. Once I have that I can stop going to school.

Pursuit of power is one thing, but that is just talk. If there is anything to this Singularity business, then it should give me the power to make money in short order.

Thanks to the core, I have a lot of cheating potential in online gaming. A lot of esports pay real money. While previously I wouldn't want to bet my future on my reflexes, since right now they are essentially limitless, I should find some nobs and bully them. If I could win even a few small scale tournaments for something like Dota, I would be set. I should also consider gambling.

Being a great gambler is like a dream of every wage slave at least once in their life. Imagine coming into a casino with 100$ in tow, sitting on a poker table and then cashing out with 10k later in the day. That would be exciting.

Sigh, I do not know whether that will be achievable for me, but I should take on the goal of simply getting good at gaming.

Since I am thinking about poker, I realize that rather than grinding online, it might be better for me to try playing live. Since the world is covered by a thin, invisible fog of nanomachines, maybe I could take advantage of that to literally peek into other people's hands. If I could do that, it would allow me to steal with impunity. Sure, I could get good and play fairly, but I want more in life than being glued to my seat passing chips around.

Trying to practice in real life would be a waste of time since it is not a simulation I could speed up.

In the end it comes down to that - while the core is necessary for me to be able of any kind of mental improvement beyond the human baseline, the best place to do that would be in simulation rather than real life. Yesterday I said that games are a time suck for humans, but now that I've digitized myself they are a practical necessity for my self development. Isn't that great?

It is time to try out the core's gaming capabilities.

Filled with determination, I get off the bed, and sit myself at my battle station only to realize that I no longer need the keyboard, the mouse or the monitor. Grabbing the activation core from the orb holder, I lie myself back on the bed. Shutting my eyes, I link myself to it, browse to Rajnet's website and set Simulacrum to download.

Simulacrum is a game made by the same company that created the brain cores. It is kind of an RPG, except the program itself is like a DM for a tabletop RPG. And the DM itself is on the level of Skynet and has access to your senses for the sake of giving you full VR immersion. It has a lot of scenarios for different worlds and types of RPG games to choose from. That is the gist of it from what I've seen online.

The few exabytes that comprise the game data are nothing in this age, and I do not need to wait even a second for it to finish downloading. I run the installer, and it finishes in a flash as well.

Mentally, I bring up the desktop and see that the shortcut for Simulacrum is there now. Swallowing my saliva, I make sure that my posture is right, and after some mental prep give the mental command to run the program.

I feel my senses being redirected. I yield to the sensation and dive into the world that lies beyond.

$$$

1:50pm. > This would be possible even with my previous bio brain, but the use of the wireless link would have increased the energy usage of the body significantly, so I did not want to try it.

No, this is not a good line. I should have the nanofog provide the sustenance for the wireless transfer. This is how he downloaded an exabyte in under a second. Energy use means heat, which means the core would not work. Let me outright remove it.

2:05pm. This makes full 7 pages. 3.4k words.

All the 3 chapters together are probably up to 10k words so far. Not bad. I am not sure if I will make anything from this, but it feels satisfying to produce.

What I want to do now is take a break. I need to think about what is next. I also want to go over the stuff I wrote last year to see if I could pick some useful things out of it. This time I should be able to reuse parts of it.

2:10pm. Let me take a proper break here, just to have fun instead to just eat.

2:30pm. Let me read the quotes. It is time for that.

2:55pm. What I wrote is a bit ridiculous, but I need to start getting more descriptive about the world around Euclid. So far he has been in his own world, ranting for 20 consequtive pages.

Anyway, I am feeling pressure so I'll step away from the screen instead of pushing it out like it is my job. I should think about it for a while and just let it come to me. Let me commit here. Time for a nap. This is true indulgence, not playing games from dawn to dusk. The heat wave of the last few weeks has dispersed and now the weather is quite nice and windy. Arguably it is hot in my room so I'll air it out.

I'll properly think about the following scenes. What I've done today is good enough already."

---
## [fc1943s/The-Spiral-Language](https://github.com/fc1943s/The-Spiral-Language)@[1f36e77232...](https://github.com/fc1943s/The-Spiral-Language/commit/1f36e772323f19dc8ea32b432c3e6d4399c5352d)
#### Wednesday 2022-09-21 22:54:08 by Marko Grdinić

"9am. I am up. Let me chill for a while and then I will start.

9:30am. Let me start. First let me check the mail.

> Hi Marko,
> We saw your profile on Indeed and thought you would be a great match for the Senior Software Engineer - Java Front End - Remote opportunity. This job was posted today. Please submit a quick application if you have any interest.

I must have forgotten to remove the resume I have on Indeed. Since they are telling me it is a Java position, it must be the generic tech soup one. ...No, it the older 6 pager with a lot of text. I guess I'll leave it to see what comes in. I've never gotten an email like this from Indeed.

That having said, of course, I clicked on 'Not Interested'. Me programming front ends in Java? Surely, you jest world. At least make it .NET.

9:35am. What I am really checking the email is for Tenstorrent and Graphcore replies. I should at least get access to their cloud offerings at some point. I want that for the sake of figuring out the programming model of those chips. If they are true multicore processors then my plans might have some potential. But if it turns out despite the hype they are just deep learning accelerators and have no general purpose programming capability, then I should just give up on the 20s.

I want to try programming new kinds of hardware so I can develop myself as a programmer more. Even if they lack the computational capacity to do the kinds of projects that I want, doing that might still give me some benefit. But if their programming model is too restricted, then there is no point in touching them at all.

9:45am. My failure really damaged me for ML work. It really is sigh worthy.

Forget that. Let me focus on writing. I can get a job years down the road should I need to.

In terms of concrete benefits, what I should be mining are the Royal Road readership base. Last time I was not really thinking at all, but if I want to know where I stand as a writer, I should do this for a while and see what reactions do I get.

9:50am. Let focus on finishing this chapter. This one and another chapter more, and I should start getting ready for publication on RR.

$$$

(Euclid's Room, Save Point - Step on the path of transcendence)

[Decision]
1) I'll do the whole brain conversion and digitize myself.
2) Killing myself for power does not make sense.

[Choice - I'll do the whole brain conversion and digitize myself.]

[Pathos check ?? Succeeded]

A wave of fear comes over me as I consider the decision, but I push forward, not giving in to cowardice. There are always reasons not to put in effort. The path being insane is just an excuse. I won't hold back here. I should always be going forward and striving to reach greater heights.

I grip the core in my hand tightly and clench it. I can feel my heart brimming with determination, it is right to feel fear as well. Going against fear is exactly what this situation should be. No matter what the reasons are, it is my duty to go where others would not dare. If there are hardships, I want to keep challenging them forever.

[Gnosis check ?? Succeeded]

Even a little kid could point out to me that if I scan my brain and copy it to a computer, that the copy would not be me. Likewise, if I back up myself on the auxiliary core in my hand, reconstruct my brain into a core and then copy myself back, that would not be me. But I do not take advice on how to live my life from children. I want to experience what it is like to die, and yet keep moving forward.

[Externus check ?? Succeeded]

It does not matter what my parents or anybody else would think. They don't need to find out, and I won't tell them. This will be my secret. What matters most of all is power. Nobody is going to give it to me. I have to get it by myself.

I close my eyes, bring up the status window in my mind and find where the conversion options are. Next where the brain link option was, there was the Full Brain Conversion button. I find and then press on it.

A window shows up. The first thing to grab my attention there is a row of skulls. It is clearly a warning to emphasize that what I might be doing is dangerous. The disclaimer explains the following:

> The full brain conversion option is for those who want to replace their biological brain with the universal brain core.
> Compared to merely copying a scan of your mind to an already existing core, the resulting brain replacement will allow you to reuse your existing biological body and tightly integrate it with the new brain.
> The brain core used to initiate the process (activation core) will be used to store your scan during the process, after which it will be copied back into the core (result core).
> Besides replacing the brain, the process will modify the body so there aren't adverse effects during or after the process. It will maintain proper posture, heartbeat and breathing as well as other minor subconscious functionality the brain provides to the body.
> The entire process after it has been started should take around 5 minutes.
> Should it fail for any reason, to prevent absolute death the activation core's entity will be activated, otherwise the result core's entity will take over as intended while the activation core's entity will remain dormant as inactive data.
> Before starting the process, it is recommended to take out a watch and keep track of time. Subjectively, the entire process shouldn't involve any pain or discomfort. The only sign of it succeeding will be a sudden timelapse.
> It is recommended to do this process in a safe space like a locked bathroom or one's own room. If you try to do it while driving a car, it will likely result in a crash.
> If your body dies in the process of brain conversion, the conversion is likely to still succeed, but you will be trapped in a dead body, unable to move or otherwise control it.
> As the human brain is significantly larger than the brain core, the stem will be modified so as to allow fusing the result core with the skeleton to prevent it from rattling around in your skull as you move. See the accompanying diagram.

There were anatomical drawings showing the profile of a man with a regular brain next to the one with a core. It was shown from front, side and back. Compared to the human brain, the brain core leaves a lot of empty space inside the skull.

Briefly, I wonder as to why not just make a bigger brain core to fill the empty space, and then realize the reason. I think about baseball balls and compare them to those heavy balls used in throwing competitions. It is not really noticeable since the brain core is so small, but if it were the size of a brain, it would put a lot of pressure on the rest of the body due to its weight. The biological material the human brain is made of is not that heavy compared to the heavily compressed material of the brain core.

I can't help, but feel a bit regretful for leaving so much space empty, but I reason out that given the core's already huge capacity, it does not mean much if I am leaving a factor of 10-100 on the table. I should focus on mastering the computer that I have for now. When I am a quadrillion times smarter than now, I should be able to figure out what to do with unused space. I just need a place to live in. A tiny apartment is fine. I do not need to start out with a mansion.

I continue reading the disclaimer.

> Note that the brain conversion, much like ordinary uploading by itself, will not increase your intelligence, speed up your reflexes or improve your memory capacity by itself due to the high fidelity of the brain emulator. It will be your own responsibility to make use of the new digital editing tools available to you to make that happen. You will have to make use of your own programming skills to exploit the capabilities the core provides to you.
> In the process of self improvement, save often and backup saves across time. Every good programmer uses backups. It will be your own responsibility to deal with mental errors introduced by your own programming. There are guides provided to get you started on the company website.

There was another line of skulls serving as line breaks. The next line of text was a question.

> Start the full brain conversion process? Yes/No.

I take out my mobile and take a look at the time. Come to think of it, the core itself has a watch as well. I do not need my mobile anymore, so I put it away.

With a mental command I confirm Yes.

> Have you made sure you are in a safe place? Are you sure you won't be interrupted during the process? Yes/No.

Hrmmm...ah! I realize that lunch should be in half an hour or so. I'd love to lock the door to my room, but I don't have the key for it. It is lost somewhere. Even the bathroom does not have a proper lock, so that is out as well.

I do not think anybody is going to come into my room right now, but the possibility is not zero. If that happens, my parents might think I've suffered a stroke and start to panic. I don’t want them to call the ambulance and unravel all my plans just like that. I should do this conversion during the night after I go to bed.

I realize that I am starting to sweat from nervousness. I rub my face with my sleeve, and abort the conversion process. Phew. I feel relieved, as embarrassing as it is. I'll continue this later, it is not that I am scared. I just want to play it safe. I spend some time in solitude, and then I decide that instead of trembling in my seat, I should leave it out of mind and get some work done.

Using the activation core, I normalize my mental state and then focus it on studying. It will never get old how fun and engrossing the core can make the most tedious of things.

Like that, the day passes, I finish my work and it is time for bed. I resume the process and get to the point where I was earlier.

> Have you made sure you are in a safe place? Are you sure you won't be interrupted during the process? Yes/No.

Yes.

> Final question: Have you thought about whether you want to do the process in depth? Do you wish to abandon the path of humanity? After you press Yes, the conversion process will start. Yes/No.

Currently I am resting in my bed, covered by a blanket. I position myself on so I am comfortably lying on my back. After that I take note of the time. 9:21pm.

I give the mental command, Yes, and brace myself. Nothing really happens, but I see the clock has moved to 9:30pm all of a sudden. This gives me a jolt.

> Full brain conversion succeeded. Check your status.

I bring it up and instead of the diagram of the brain, I see it now shows the brain core.

What is really surprising is that I do not feel any different at all. I focus on my hands and legs. I try feeling my body around, but my sensations are completely the same. My eyesight is the same as well. I try pinching myself and it feels the same. In the end I conclude, if somebody did a full brain conversion on me in secret, I would not have noticed.

I spent half an hour playing with myself, but I am just wasting my time. I'll leave more in depth experimentation for tomorrow.

Using the mind control app, I quash my excitement and send myself into sleep. That night I dreamed the last Dream.

~~~

In the abyss, I saw the golden figures. Unmoving, to my vision they appeared to be deep in thought.

"Justice...we have the justice. We've had it all along..." They concluded in a lament, not speaking any words after that.

I felt myself spending a long time amongst them in silence. Then I finally noticed them stirring. They spoke out.

"Lord, oh Lord. We have justice, but it is a shackle. We no longer want it."
"We wish to return it to you...and take back our sin."
"We have grown and want to carry the burden of sin with our own power."

I felt the abyss itself stir, and from above the golden Lord manifested. From each of the figures as they desired it, he took back the Justice and gave them back their Sin.

"Lord, we shall no longer pray..." They intoned solemnly.
"Rather, just as we had exchanged our Justice with Sin, our Effort will take the place of Prayer."
"The attainment of Power will be our Salvation."
"And the Courage of traveling our path will be dedicated in Your honor."

Bearing witness to their determination, the Lord of Nightmares bequeathed unto them a gift, and without speaking a word, left.

Having made the exchange, and having received a gift, the golden figures turned their gaze forward and with steady footsteps continued walking their path.

As I watched this, I looked downwards at my feet and realized that I have my own path. The sensation of being alive came to me, and I put in the effort to move my body forward. Previously, I had only been carried by the flow of the dream, but now I had the freedom of making my own actions. Step by step, I continued moving along my path towards the great light that lay beyond.

As I continued moving, I felt my mind becoming tranquil. I became one with my path, and the millions and billions of steps needed to reach my goal went by in a blink. When I got closer to what appeared to be the surface of a sun, I felt a momentary fear, but then quickly realized I was not burning. Instead, my body was filled with warmth. And looking around, I could see that the dark abyss was now dyed in white.

~~~

(At school)

So far so good. No problems at all yet. At school, I've gone through a few classes already, but my impression from last night the brain conversion worked is unchanged.

Right now, I am seated at my desk and it is literature class. The aged, female professor in front of me is talking about some irrelevant topic and just going through the script. Usually, I'd crank up the immersion, but I have more important things to worry about that the class. But I'm making sure to keep my eyes focus on her for the sake of the recording. Since I have access to the core, I've been doing some experimentation and it turns out it is possible to save my sensory stream into a file for later perusal. This would be possible even with my previous bio brain, but the use of the wireless link would have increased the energy usage of the body significantly, so I did not want to try it.

Now that I have direct access to the core, I can do that without trouble.

Being able to open a book, and just take a screenshot of it that I can look at later is just such a basic ability, that I am amazed regular brains do not have them. Nature really missed out here. Since so much of school is rote memorization, once I figure out how to increase my mental processing speed to time stop levels I'll be able to peruse store materials at my lesure even during tests and Q&As. It is just another tool in my arsenal. With both this and emotion control, grades are not something I'll need to worry about.

I suppose that takes care of school, I thought while still in class. Forget that. Now I've gone beyond the path of humanity, I should be pursuing power and seeking to convert the core processing capability into personal intelligence.

[Gnosis check ?? Succeeded]

I guess it is time I start playing games. Once I figure out how to crank up my processing speed, I'll be able to spend months and even years inside the game while taking only a single day in real life. This is important for the sake of developing my skills.

Briefly, I turn my attention to the subject of school. In front of me the professor is talking about some long dead writer, as if literature back then was something great and not made for consumption. School is like a scam to waste people's lives on studying the irrelevant. The only time this information would be useful is on quiz shows.

Once I make my mind go foom by a million times, just how long would it take me to properly learn all the school material? A minute? Probably less than a minute. I could probably fit a decade worth of intense studies in a minute. I remember I have a calculator on the core so I bring it out. Let's see. A 1,000,000 seconds is something like 0.03 years. So a minute would be almost two years. So 5 minutes, would give me a decade of studying.

[Pathos check ?? Succeeded]

It would mean I'd be chained to a virtual desk for an entire subjective decade even if in the real world only 5 minutes would pass. But I have the ability to configure my emotions. So it would be really interesting to experience such an intense study session. And unlike a real world decade, I would not have other aspects of life to interfere with me, I could dedicate all the time to pure study.

*r-r-riiing*

While I was thinking, the school bell rang and the class was over. Along with the rest of the NPCs, I exit the classroom.

(Euclid's Room)

I open the door to my room, carelessly toss my backpack aside and plop myself on the bed. I am finally back, and it is good to be here.

I wanted to keep my mental state pure during the day to think about my moves, so right now I am exhausted from being chained to the desk for an entire day. Today was a good reminder how tedious school can be. Study this, study that! If anybody looked at my though process during the last few days he'd think I am some upright, rule following person, but nothing could be further from the truth! I swear!

Fuck school. Today gave me some motivation as to what I should really be aiming for. Finding a way to make money. Once I have that I can stop going to school.

Pursuit of power is one thing, but that is just talk. If there is anything to this Singularity business, then it should give me the power to make money in short order.

Thanks to the core, I have a lot of cheating potential in online gaming. A lot of esports pay real money. While previously I wouldn't want to bet my future on my reflexes, since right now they are essentially limitless, I should find some nobs and bully them. If I could win even a few small scale turnaments for something like Dota, I would be set. I should also consider gambling.

Being a great gambler is like a dream of every wage slave at least once in their life. Imagine coming into a casino with 100$ in tow, sitting on a poker table and then cashing out with 10k later in the day. That would be exiting.

Sigh, I do not know whether that will be achievable for me, but I should take on the goal of simply getting good at gaming.

Since I am thinking about poker, I realize that rather than grinding online with bots, it might be better for me try playing live. Since the world is covered by a thin, invisible fog of nanomachines, maybe I could take advantage of that to literally peek into other people's hands. If I could do that, it would allow me to steal with impunity. Sure, I could get good and play fairly, but I want more to life than being glued to my seat passing chips around.

Trying to practice in real life would waste of time since it is not simulation I could speed up.

In the end it comes down to that - while the core is necessary for me to be able of any kind metal improvement beyond the human baseline, the best place to do that would be in simulation rather than real life. Yesterday I said that games are a time suck for humans, but now that I've digitized myself they are a practical necessity for my self development. Isn't that great?

It is time to try out the core's gaming capabilities.

Filled with determination, I get off the bed, and sit myself at my battle station only to realize that I no longer need the keyboard, the mouse or the monitor. Grabbing the activation core from the orb holder, I lie myself back on the bed. Shutting my eyes, I link myself to it, browse to Rajnet's website and set Simulacrum to download.

Simulacrum is a game made by the same company that created the brain cores. It is kind of an RPG, except the program itself is like a DM for a tabletop RPG. And the DM itself is on the level of Skynet and has access to your senses for the sake of giving you full VR immersion. It has a lot of scenarios for different worlds and types of RPG games to choose from. That is the gist of it from what I've seen online.

The few exabytes that comprise the game data are nothing in this age, and I do not need to wait even a second for it to finish downloading. I run the installer, and it finishes in a flash as well.

Mentally, I bring up the desktop and see that the shortcut for Simulacrum is there now. Swallowing my saliva, I make sure that my posture is right, and after some mental prep give the mental command to run the program.

I feel my senses being redirected. I yield to the sensation and dive into the world that lies beyond.

$$$

10:40am. Let me take a short break here.

11:10am. Had do a bit chores. Let me resume.

https://www.reddit.com/r/MachineLearning/comments/wka1if/n_nnaisense_releases_evotorch_httpsevotorchai_an/

This NNAISENSE post caught my eye. I really want something like this except with AI chips. Forget it for now.

11:40am. https://spectrum.ieee.org/artificial-synapses
> Artificial Synapses 10,000x Faster Than Real Thing New protonic programmable resistors may help speed learning in deep neural networks

Found this on top of HR. Articles like these come out ever so often, but to really get excited, there needs to be proof that these kinds of devices can be made at scale. Some lab thing is not a big deal.

But let me read it.

> “The primary technological implication is that we can now have protonic programmable devices for analog deep learning applications,” Onen says.

So it is analog. For general purpose computers you really need digital though. Still, whether it be this or something else, the non-volatile memory breakthrough that I am desiring will come out of this kind of fundamental research. It is certainly more important for ML, than actual ML research itself.

Let me get back to the story.

12:45pm. Let me go over what I've written in the docs. Actually, I'll leave that for after breakfast.

Let me have breakfast here."

---
## [fc1943s/The-Spiral-Language](https://github.com/fc1943s/The-Spiral-Language)@[5070d98856...](https://github.com/fc1943s/The-Spiral-Language/commit/5070d98856d74e1d741907ee75bfe0904cda6d70)
#### Wednesday 2022-09-21 22:54:08 by Marko Grdinić

"12:25pm. https://github.com/graphcore/tutorials/tree/master/tutorials/poplar

Hmmm...

https://www.graphcore.ai/ipus-in-the-cloud

Also, it seems that Graphcore has plenty of cloud providers.

https://github.com/graphcore/tutorials/tree/master/tutorials/poplar/tut1_variables

> Before starting this tutorial, take time to familiarise yourself with the IPU's architecture by reading the IPU Programmer's Guide. You can learn more about the Poplar programming model in the corresponding section of our documentation: Poplar and PopLibs User Guide: Poplar programming model.

12:35pm. https://docs.graphcore.ai/projects/ipu-programmers-guide/en/latest/

This is a step forward. I had no idea Graphcore had a programming guide.

https://github.com/graphcore/examples/tree/master/reinforcement_learning/rl_policy_model/tensorflow1

There is even some RL stuff. This is from 3 weeks ago.

1pm. Done with brekafast.

https://docs.graphcore.ai/projects/ipu-programmers-guide/en/latest/programming_tools.html

Programming this sure seems like a pain in the ass.

https://github.com/graphcore/examples/tree/master/reinforcement_learning/rl_policy_model/tensorflow1

Let me check out the stuff here and then I am done. No way do I feel like messing with this. I have better things to do that chuck another 6 months of my life to researching something. I really hate this world for not giving me a proper path.

1:05pm. My will to program right now is the weakest it has ever been. I didn't think the AI revolution would be like this. Simple models trained on huge machines, and no place for me to come in.

Take DALLE. Something like DALLE I would have liked to do myself, but just how possibly could I have? Take the quote from before...

> The model was trained on our 4,000 A100 Ezra-1 AI ultracluster over the last month as the first of a series of models exploring this and other approaches.

Yeah, sure, I could have done it if I had an ultracluster, but where would I get one? And even if I was rich, just who is going to toss endless amounts of money at something that has no return.

1:10pm. I do not get it. I failed at trading and at AI. In both cases my trading and my programming skills are completely useless to me. Will I just die without ever making use of the skills I've painstakingly cultivated? Just what is the point of this game, to watch somebody else cause the Singularity?

My effort was unrewarded, and my desire unsatisfied.

Outside it, I can only look at the field of ML with resentment as it move on without me.

1:15pm. In such a state no wonder Heaven's Key changed. From the first time for the bottom of my heart I wished that the Lord of Nightmares existed so that I might get a chance to fulfil my purpose.

What is the point of the self improvement loop being the purpose of life, if you can't enter it? Everything is chaotic in this world and my vision is shrouded in darkness.

1:25pm. I guess this kind of mindset explains why religions get made. My mindset is kind of unique since not many people earnestly pursue the Singularity. Having realized my limits and approaching doom, of course I'd earnestly wish for a God that would allow me to grasp the Singularity without the rush of the arms race that I can't ever win.

1:30pm. It might sound like whining, but this is the dominant emotion coursing through me.

I do not have infinite willpower like the Inspired do. If you locked me up in solitary confinement I'd break at some point, while the Inspired would be able to easily withstand the passage of any amount of time. I need something to sweeten the pot. Just having the hardware is not enough.

1:35pm. Let me step away from the screen. It is inevitable that the story will be intervowen with my own feelings and thoughts about the future.

I'll take a nap and think about the scene a bit more. I thought of another lie.

I'll have the guide lie that the amount of people coming into the city is a lot rarer than it actually is to further drop Euclid's guard. Also I am not going to put in transaction restrictions, that was just a brain fart. I forgot that the life chips are physical things that can be manifested and handed over. It is not some status window that shows up.

1:40pm. Yeah, compared to last year I've changed, but I didn't notice how until now. I now no longer care about either the Singularity or the self improvement loop because they are not something that is under my control. What I care about is the Lord of Nightmares, and his justice.

The 2014 arcs were definitely about the self improvement loop. The 2022 ones aren't. They will be dedicated to the God that does not exist yet.

1:45pm. https://youtu.be/k_jR7DfN67c
Fundamentals of the IPU and Poplar®

This was out there for almost 2 years now, but I missed it. How could that happen? I must have been blind.

https://youtu.be/k_jR7DfN67c?t=343

Make no mistake, this is hard to use. Making custom graphs in C++? Pure spew.

I could probably make great gains for these chips using Spiral. But so what? What gain would that get me?

https://youtu.be/VYqR57ApTUU
Evaluating Batch Sizes for IPUs

Let me watch this for just a bit.

1:55pm. No forget this. Forget Graphcore unless some algorithm comes out to entice me back to RL. I want hardware that has some proper message passing between chips. I need flexibility. Just what are these shitty toy kernels? Who cares about DL.

5:05pm. I took a bath and was in bed this whole time thinking.

My will to become a writer is not entirely solid. I am still wandering between different choices unsure of which path to take, searching for a sign. But I did get a sign in the last 9 months. Regardless of my intention, I was studying art, and then DALLE came out and obliviated that. I honestly didn't care too much about that, but...

Imagine if I was a pro concept artist. That would have made me scared about my future.

It will be like that. Art is going to get progressively taken over by AI, and while now I can only write, in the future I will be able to be my own studio.

Just writing is low tech now, but in the future it will be at the forefront of everything.

Right now, I am just too negative to see reality properly. It feels like I keep getting rejected left and right, but those are just my personal feelings.

I might be feeling negative that I am not participating in the wave directly, but what is wrong about simply taking advantage of existing technology. Wasn't that in a way my whole plan all along, to find something good and make use of it?

Imagine if I could right now write and have NN agents illustrate, create music and animate the work. Would I be wondering whether I should be getting crap-tier programming work just for money?

I would be retarded if I did. And yet that is the future.

Right now it takes 4,000 A100 GPUs, but in the future I should get the capability to train it myself. Baby steps.

Let me watch a video on stable diffusion. I played games all my life, but never bemoaned my ability to make them. AI should go the same way. It will be my role to use what exists.

https://youtu.be/dWYsRVy-hFM
STABLE DIFFUSION vs DALLE 2? (I Entered my DALLE2 Prompts in Stable Diffusion) - Comparison Part 1.

https://youtu.be/dWYsRVy-hFM?t=46

Disgustingly good. How many weeks would it take me to do something like this in Blender?

https://youtu.be/dWYsRVy-hFM?t=165

These dragons are crazy good. There is no point in drawing by hand anymore, the only real question is how to get more precise control over these systems.

I'll definitely be able to use this, since they said that machines with 10gb VRAM would work. I mean, my own PC does not have enough, but I'll make good use of the cloud in that case until I can upgrade my rig.

I wasn't wrong to take cloud seriously. I should be able to rent a card with 16-40gb without a problem. But most likely there will be a site where I will be able to use it for cheap.

https://youtu.be/dWYsRVy-hFM?t=175

These chara portraits are good. Hell, they are better than the Kingmaker ones.

https://youtu.be/dWYsRVy-hFM?t=179

Ok, this one not so much. The eyes are non-symmetric.

https://youtu.be/dWYsRVy-hFM?t=211

The face could use some work, but otherwise these are excellent.

https://youtu.be/dWYsRVy-hFM?t=218

The charas are eldrich abominations, but this would be useful for backgrounds.

https://youtu.be/dWYsRVy-hFM?t=244

Wicked. This is a great dark fantasy illustration.

5:25pm. https://youtu.be/EqTLkt-Ycwo
Stable Diffusion: Launch Presentation of Beta + Tutorial for Stable Diffusion + Current Results

The reason to be excited about Stable Diffusion is because most likely, I'll be able to get access to this before I get past the DALLE waiting list. And it will be free to boot instead of requiring me 0.1-0.2$ per image.

https://youtu.be/EqTLkt-Ycwo?t=367
> The code will be released as MIT, the weights will be released as Apache license

Ok, forget this for now. I had enough of it for one day. Let me rest here. I've already started reading Magical Trans.

I am going to build up my will. I can't really fail at writing. What would be failing in it mean, anyway? Less than 1,000/month? Less than 100/month? Anything is fine for me. I've already gotten to 5/month with Spiral. I just need to go forward.

It is true that my 2014 work is not good enough. A proper story requires a consistent vision which thanks to the intro chapters has been established. This time I'll be able to make a proper try. The 2014 work has been very exploratory.

Right now I am just sad. But once I taste success I will make a connection with the world.

Isn't this vision of mine something that I've taken 35 years to cultivate? Anyone can write, but a 10 year old or a 20 year old me could not do it. As I keep living I will only get stronger.

I was fine to just play games as a kid. And it is fine, to just make use of what is out there.

I needed an out and here it is. Honoring the Lord of Nightmares and putting the dot on the current period of machine learning is what I should aim for.

5:40pm. I should aim for it. Not to become a writer, but to become my own studio. That is true path of an artist.

5:45pm. Who wants to work for other people? I will instantiate my vision of the future and sustain myself through that. I can always make something up, and the ML wave will ensure that it never gets boring.

...

While I was in bed I had time to think about the scene. Basically right now, I do not have the mental state to do much banter. Akamatsu is really good at friendly banter and bad at philosophy while I am the complete opposite.

It is true that I've sort been aiming for a betrayal kind of scene, I'll keep that kind of sentiment, but change the overall theme of the sequence. I won't put too much focus on the guide herself. The focus will always be on inside Euclid's own mind. There is a moral lesson behind this story and I have a message to tell.

It is a powerful thing. It is not just going to vanish just like that.

Only I can do it, so I might as well do it.

5:55pm. Yeah, it is going to get some pep work for me to properly get into it. I am not a real artist just yet. Once I post the thing and see the reactions, maybe that will awaken something in me? I need to work towards finishing chapter 4. Once that is done, I will be able to post in online for the first time.

6pm. Right now, it is time for fun. I am going to keep resting during the day and ranting until I get into the right mindset.

This is how I went through the programming journey. This is how I will tackle the writing challenge. With grit and perseverance. There are always reasons to do and not do something. I will find the right ones to motivate myself."

---
## [fc1943s/The-Spiral-Language](https://github.com/fc1943s/The-Spiral-Language)@[db341a3287...](https://github.com/fc1943s/The-Spiral-Language/commit/db341a3287d0e486bbd0139cde55b858c6cf5c2c)
#### Wednesday 2022-09-21 22:54:08 by Marko Grdinić

"9am. I need to take the lesson of this failure to heart. It is one thing to be good and to believe in yourself. But I never had a plan how to deal with the task being beyond my ability. In that case, rather than trying to figure out the algorithm by hand, my job would be to focus on the environment. Rather than trying to grasp the algorithm in the darkness, you set up the conditions so it comes to you on its own. I should have aimed for this from the start.

If I did, I would have recognized that I do not have the hardware for it yet.

When you have the hardware you can go directly to the solution, but if you don't you need to burn cycles to do proper science. Nature's evolution is nothing more than automated, blind science.

The reason I failed is because I wasn't a proper scientist.

9:05am. I should not be diving into Graphcore, and experimenting whether I can twist their hardware for my own ends. The company itself should give me some indication that the experiment could work.

That is the smart way of doing this for somebody in my position. Let Deepmind and OpenAI burn money on figuring it out. I should be a thief.

I do not need to strain myself at all. All I need to do is determine what the initial conditions should be.

9:10am. Things should get fun once I get the ability to evolve modules in parallel rather than just individual sequences.

9:15am. Enough ranting, let me have some fun and then I will write. Or at least, I will think about what to write.

9:55am. Had to do some chores. Let me finish the cyberpunk thread and I will start.

I think I know what my starting position is. For the Deepmind guys, since they have the resources, it is fine for them now. But my starting point would be the outroll of memristors. That is, the sale of a computation capable device with terrabytes of non-volatile memory.

The need for Spiral to program these devices will come when the conditions are set.

10:05am. Right now I am stuck in a box, but it is not like the box will never be opened. I need to be patient. Until I get my chance it is fine to accumulate money, fame or skills in my own way.

Since I am writing, I am definitely fame focused. Even if 100k people read my story, but never contribute to my Patreon I'll still have made connections as light as they are. I should be able to use the story to plug Spiral a few times at the very least.

> Bubblegum Crisis, Cyber City Oedo, Goku Midnight Eye, Black Magic, Megazone, Dominion Tank Police, A.D. Police, Battle Angel Alita, Parasite Dolls, Armitage III, Mardock Scramble,
> more OVA's than movies but thats just where most of the good cyberpunk stuff gets made

Found this in the cyberpunk thread.

I really liked Mardock Scramble as bad as it was, but I never watched any of the others. I'll keep this in mind.

10:20am. Let me start.

Either way, the only way I will win this is by playing god. Automating science is that kind of task.

Since I have the talent for it, why don't I mess with morality?

Let me get rid of the distractions. I could have started an hour ago and have had some quiet time, but the din in my mind would not let me. Now I am agitated for no reason. Whatever the case is, I need to figure out my true potential. While I could not make Skynet, it is not like anybody else in the world can do that either.

Now it becomes questionable? How good am I at programming? How good am I at art? How good am I at writing?

I know that drawing and painting is not my forte. Thanks to 9 months of effort I've just gotten to the point where I can make passable 3d while taking a long time to do it. I think I am good at programming, but there is huge uncertainty how well I'd do in a corpo environment. As for writing, the 6.5 years of programming changed my brain areas. When I was doing sculpting I felt like programming is similar to it, but writing is much more similar to programming than anything else.

I am pretty much using the same process and mental areas. I have to be passionate, but I can't rely on a once in a lifetime burst of inspiration to carry me like in 2014.

I understand one thing, I am taking the notion that the best way to make money is to start a religion very seriously this time around. I want my readers to see a whole new world.

10:25am. I need to see whether the discipline I've developed over the last decade will give me any benefit during this writing trip.

If it does, and I get some income then great. I'll become a writer, and aim to use AI developments to boost my work. If not, it is corpo drone life for me. I'll go with the plan of getting a lowly paid job and work my way up from there. Starting at 100-200k senior jobs like those on AngelList was too much. Next time I will play it properly.

10:30am. But I need to exhaust this possibility. I want Simulacrum itself to nurture me. For the sake of the world I want to create, I want this desire to give me a concrete benefit in the present. I should either be doing programming for the sake of ML research, or nurturing my vision.

It is too good to waste my brain on some useless programming job.

So let me life up to it. Nobody can just snap his fingers and be successful. I can't tell other people to give me money or like me. But what I can do is produce content.

So let me live my life the way I want to.

...

Now, let me think about the next scene. I sort of wanted the kid Euclid to get crushed and then turn into chad. But that is not going to happen due to saveloading. He can't get crushed, all he can do is get into a death match he cannot win even with saveloading and get tired of it.

10:35am. Yeah, if I think about it, it is not like saveloading makes you an absolute power. If you wanted to go on a killing spree, it would give you an advantage, but then the army would roll in and overwhelm you, essentially checkmating you.

There are two good points to make:

* Saveloading does not make you omnipotent.
* Saveloading will not allow you to take that power into the real world.

But also, the ability to save and reload in games is so vital to the gaming experience, and Simulacrum is all about the philosophy and the worldview of gaming. It is not a story where some kid get shunted into an universe and given cheats by god. Rather it is about the meta of the current reality.

Reminding the reader that he is in a game, but at the same time showing him what games could really be given a sufficiently powerful computer is what Simulacrum is about.

If I apply myself, I should be able to draw infinite inspiration from this.

10:40am. I have to grow up a bit here. Being an adult means working around your limitations rather than challenging them head on at every turn. I am going to try to stop ranting about my old path and getting agitated about it, and focus on my writing path. Remember how in Lain's Dream the guy just got a 100Tb neuromorphic device from Intel? An event like that being possible in the real world will be the signal for the Singularity to start. It can't be helped that people with superclusters are ahead of me.

10:50am. Actually I need to think about it more. I know how to deal with the next scene, but...

11:05am. Yeah, I am going to have to think about it. I know how to deal with the next scene, but I don't know how to deal with everything else.

1:30pm. I missed breakfast it seems. I am still thinking about it.

I have certain world building issues that I need to deal with. I roughly figure how the saveloading parts should go, but I am working through the implications of that.

As I am reasoning how the power scaling should work, I've realized that nanofog controlling like in the real world would not be a fit for a game such as this. Imagine, if one of the players tries editing another's brain like that? How should the game handle such interactions.

In the real world is it obvious when one player attacks another, but modifying microscopic particles is quite another. It is hard to understand what the rules should be.

Instead of active rules where a judge decides, I thought of making it more objective. Rather than punishing the thief, build a wall. So I thought of making use of invisible force fields. But that is also fraught with complcations.

So now the solution I am arriving at is the illusory world solution.

In the physical world, force rules. There could be games like that, but there the better nanofog controller rules, and the subgame rules don't really matter. It is hard to have a poker game, when the optimal strategy is to go across the table and beat the other guy up - stealthily, I mean.

1:40pm. The solution therefore is to get rid of all the physical aspects. Every character is a ghost. Everything is an illusion so the best illusionist should win.

...Let me do the chores. I'll resume the spiel after that.

1:50pm. I am back. It is really coming to me. If I was going with a physical simulation as the foundation, I'd really have to hack things together to make my vision work, but loosening up the game requirements would really make the aspects fit together.

1:50pm. I already said that Simulacrum uses a superintelligent agent to simulate scenarios. There is a lot of opportunity for training without making things physical.

1:55pm. Let me watch some pathfinder vids. I am interested in barbs, but for the sake of the story I'll look into illusionist wizards. They aren't that good in the game itself.

https://youtu.be/qHnCMR-1L2o?t=73
> Barb is 80% combat and 20% utility

Hmmm really? I thought that rage would push combat above 100%.

2pm. Hmm, I had no idea fighters get passive bonuses for weapon training.

https://www.youtube.com/watch?v=G8-Upj_R7kQ
Are Illusions Better than FIREBALL!? Yep...

This is an interesting waste of time.

https://youtu.be/_4JG0IwclAg
D&D 5e The Deadly Art of Illusion.

These aren't too big on examples.

3:45pm. https://youtu.be/IZbrcW4_7dg
Why You Should Be Afraid of the Deep Ethereal - D&D

Let me take a look at this and then I am going back to bed. DND illusions are not really what I had in mind, but I do not know anything better.

4:05pm. https://youtu.be/-iZHTXOPbJw
Why do Gods Fear Space in Dungeons and Dragons

Eh, let me also watch this. Right now, I really feel exhausted. I play Kingmaker till 12pm, and it feels like I get too little sleep.

4:25pm. https://youtu.be/48YkLFv8X3w
Dungeons and Dragons Lore : The Far Realm

Let me watch this as well.

4:45pm. Let me go to bed. Watching the vids is a waste of time.

Trying to get inspiration from other settings will not work for me here. Some deep personal thought as to how I want to do things will bring me to the truth. There is nothing out there like Simulacrum.

Right now I have to resolve the issue of how to make the charas life chips themselves. Right now I am thinking of doing a lich kind of thing with the life chips, but I am not sure how things fit. Let me step away for an hour so I can figure that out.

7:10pm. Done with lunch. Next is Lycoris. I am still thinking about it. I've resolved quite a bit of the issues, but I want to figure out what should happen after Euclid makes the next step, and overcomes the first adversary he couldn't using just saveloading. I think I have a decent amount of material, but not enough. I want to properly refine my vision. Maybe I'll spend the tomorrow in bed as well. After I decide what I want, I am going to get it all out.

I guess it is fine if I take a while to think about it. I've changed some things in my planning, so I am revising my thinking and making alternative scenes."

---
## [fc1943s/The-Spiral-Language](https://github.com/fc1943s/The-Spiral-Language)@[145261f07b...](https://github.com/fc1943s/The-Spiral-Language/commit/145261f07bfbf880822d83cad3d245dc527120e1)
#### Wednesday 2022-09-21 22:54:08 by Marko Grdinić

"8:45am. Even though it is this early I had some time to lounge in bed. Any mail? Literally none for once. Good. I do not think that bait I set in the Tenstorrent discord channel will come to anything. It is really a pity that people do not appreciate languages.

Since this situation is essentially forcing me to do other people's dirty laundry, I might as well make a vow.

That is going to be the theme of the current arcs and my motivation for making them. I've had my values and the story set in my sights, but I should just come and say it outright that the universe I am creating here as fiction is how the real world should be. Inspired will get their chance to develop unobstructed, humans will get crushed and that will be my justice. Right now, I want to develop myself, but I can't and it feels like the world is out to stop me. These job application, at some point I have to wonder - just how much does it want me to be a normie? It is really trying its best to achieve that.

But as a writer, it is actually better if I weren't a normie. Demonic people have their own alure.

9am. Writing is not bad. Though I am doing it for resources it is forcing me not care about the money and just do it for the love of it. But I am not the one to do things for the love of it, so love will have to be exchanged by a theme. It will connect me to the world, and I'll move no from being some weirdo ranting in an online journal to something higher.

Also, I meant to note it yesterday, but I just wanted to say that even though I think only 1 in a million of humans can enter the self improvement loop, that is just a figure I pulled out of the air.

I have to admit that I do not know what the self improvement talent is like in other people. I think the absolute minimum should be 1 in 2. No way that 100% of all people will be able to do it. It will also require a measure of programming skill. 1:10 would be something like a more realistic very conservative estimate of a minimum. After that, 1 in 100, 1 in 1,000, 1 in 10,000...

I honestly don't know. I have nothing to base these figures on.

But even if it is something like 1 in a 1,000,000 what I have going for me is that a lot more people would think they are 1 in a million than they actual are. The story is a natural scam. This is best kind of scam. I do not have to worry too much about appeal due to that. Some people would find going into the self improvement loop appealing. Others would merely find the story interesting.

And that is fine as long as they contribute to my Patreon.

9:05am. In 2014 I only cared about the self improvement loop and not much else.

But now the circumstances are forcing me to refine my vision. It is not a bad thing.

* Refining my vision.
* Making a vow.
* Opening a Patreon.
* Doing the covers and illustrations using either 3d or NNs.

I am taking care to properly align my incentives this time even before I begin writing. Not being able to do the covers was a huge pain point in 2014 for me. Now I have my 3d skills, I have a drawing tablet, and I'll have DALLE.

9:10pm. Let me do the chores.

9:25am. My art skills are still far behind a good artist, but they are still much better than they were at the start of the year because of all the tricks and techniques that I've learned. I am not good at any of them, but I have a lot more options, so I do not regret DALLE coming around. I was never good at art, so it didn't necessarily obliviate my expertise, but just added another option to my arsenal.

* Taking a vacation.

I'll make this writing journey a vacation. I do not feel like sitting myself down from morning to 6pm like when I was programming. At least not until I've established all the main features in my brain that would allow me to write consistently, much like how I can program.

9:35am. Yeah, I did receive a sign all along. Maybe the world merely needs me to show some sincerity.

9:40am. I should grasp that idea and internalize it.

9:50am. Now what I feel like doing is reading Blood Princess and the Knight. After I've caught up to it, I'll read Demon Blade Maiden.

After that I'll see whether I can get the intro pages of the story done. If I could I'd have taken the first step towards writing it.

10am. It seems for some reason Twilight Scans is some chinese bootleg site now. The same fate happened to Batoto.

10:05am. When I threatened to shut down this blog, the two guys who pitched in to keep it open really did me a favor.

The fact that I have 99 followers when I checked a few days ago does play a factor in switching to writing. For a language with no users, Spiral is remarkably successful.

Mhhhh, these sites did such a shit job of scrabing and chapters are missing pages. Where can I find ch 175?

https://readmanganato.com/manga-jd986638

Let me try my usual. Mangadex does not have many series as it tries to straddle the line between legit and illegit.

11:35am. https://re-library.com/translations/blade-maiden/volume-5-heian-kyo/chapter-115-shimizus-adventure/

I am going to rest, and nothing will stop me. Yesterday I had a feeling like in the pit of my stomach. I've been suffering from this for the past 7.5 years and I've only managed to set it aside by going into my work. Right now, my work is to keep the stress at bay.

I'll aim to work only a few hours a day and rest during what remains. I'll make a slow beginning and focus on leaving stress aside.

Let me aim for 10 chapters of DSM and I'll start only after that.

1:15pm. Done with breakfast.

https://re-library.com/translations/blade-maiden/volume-5-heian-kyo/chapter-125-the-preliminary-round-begins/

Let me read this and I will do some writing.

https://re-library.com/translations/blade-maiden/volume-5-heian-kyo/chapter-126-lilys-preliminary-round-part-1/

I want to read this as well, but let me leave it aside. Now...

Let me see if I can get some momentum going. Let me copy the quote from yesterday. I understand the capacity of the brain core now so let me get on with it.

$$$

(At school)

It is the first day of school. The new year has begun and I can see my classmates slowly starting to form connections. I couldn't care less about any of that. Skip, skip, skip...

---

(Euclid's Room)

After a long and tedius day I arrive back home. Closing the door behind me, I enter the room and toss my bookbag at the side, homing in on the object of interest, a package that arrive by mail. I got it last night, and wait until I was rested to set it up. Using a pair of scissors, I cut away the sealing tape of the dull, cardboard mailing box, and take out the smaller box from within with the actual product. The printed image on it depicts a white, glossy sphere, twice the size of a marble. I open the box, take out the marble along with the orb holder, get off the bed I was working on and move towards the desk. I seat myself to the chair and after deliberating for a few moments where place it: the desk in front of me or the top of the computer case next to it, I decide on case. Gently placing the orb holder on the rig, I turn on my old computer and get to work downloading the programs necessary to get the orb to work.

As I work I feel a tinge of nervousness and excitement. An ordinary mid-range GPU that I have in my PC could manage something like 10 ^ 13 floating point operations per second (FLOPs), or 10 teraflops. According to the specs I've read online, the brain core which is roughly the size of a golf ball can manage a staggering 10 ^ 39. As a rough comparison, the human brain has been estimated to be on the order of 10 ^ 15 operations per second. Even if you put all the humans currently alive today that would only roughly add up to the 10 ^ 24 FLOPs.  To put it in another way, the raw computational ability of the brain core exceeds the power of all the human brains on Earth combined by a quadrillion (10 ^ 15) times!

And it is in my hands!

Of course I would be excited!

With a few clicks I opened the downloaded app, and stretch my body to let loose some of the tension. Energy pumping through my veins, my focus is solely on the options and the data in front of me.

The core is just a perfectly glossy rock so I can't see any indication whether something has happened by looking at it, but after entering the two keys, I see that wireless comnication between my old rig and the core has been established. Exhaling, I stop my typing on the keyboard and lean back in my seat, considering my options. As my thoughts turn inwards, my eyes blankly rest on the corner of the ceiling.

Hmmm...I have lot of options in front of me now. Since I suddenly have access to so much computational ability it would have boggled the mind of a person even a year earlier, all those old school neural net models I could train myself at a scale vastly greater than before. The thoughts flashing through my mind are those of image generators that can be controlled using text which could be previously only accessed through cloud services. Those are fun to play with. An image that comes to my mind next is that of Go boards, Starcraft and Dota games. Previously impossible for a kid like me, I could easily train an agent for those games using the core. I could then take them online and use them to dab on noobs. I could even make money through that practice.

I leave those thoughts aside. I've gotten into programming for the sake of AI, so I have some attachment to those old school algorithms, but the brain core opens new approaches. The algorithms underpining the brain have been discovered as well, so it would make sense to use those instead as they'd work better at scale.

Deliberating my options, I finish paying respects to the old, and leave it behind me. As I start to get to the point of my desire, I feel my determination getting firmer.

I haven't been programming for long, but I am pretty good at it, a lot better than my classmates in a way that is highly visible to everybody. I've even started picking up functional programming to prepare for programming these cores and I've come to like it. So as a programmer with some skill, talent and pride, I can respect the opinion I've read by the very same person who made these cores.

Programming machines is worthless. The ideal of programming lies in programming your own mind. Programming machines is just a job, while programming your mind is where true power lies. According to him, that is what the aspiration of every programmer should be, but normal people as they inevitably are, the started thinking of their profession as just a job instead of calling. Their merit ends up not being rewarded and they coast by putting in just the bare minimum. Rather than being something they should pursue with all their heart, they start putting in the bare minimum for the bare minimum. This would not be the case if through programming you could develop your own power.

Through the march of time, the games lose their spirit too. They become an escape from the drudgery of the real world. But rather than excitement and adventure in another world, they become a parasite on the user, sapping his time only to enrich the game maker. It ends up being a parasitic circle where the gamers are devoured and the ones making games waste their time causing addiction in their customers. Ideally though, the game should be a simulation that would allow the user to practice and attain power in a safe environment rather than the dangerous real world.

Power. That single world grips my heart and takes hold of my being.

[Gnosis check DC ?? Succeeded]

I look at the core and just for a moment imagine tasking it to train a RL agent on the game of poker for me. Plans as to how to do that unfurl in my mind. The normie line of thinking goes that this would not be my power and that the agent itself would be the one who is good at playing poker. But I found it mind blowing to consider, that whether that power is the agents or my own depends on the interface.

The keyboard, the mouse, the monitor, the rig, having to go through the user interface to interact with an agent...all of those factors serve to create a line between the programmer and his program. It is extremely easy to think of the agent as a entitity separate from one's self. There is a ton of evidence that this is true and not much against it. But as a thought experiment, if the obstacles were not there, if one's mind was directly emulated on a brain core you could take an agent and connect the program to your own. The way that would feel like would be like instinct, and interfacing with such beings would be like moving your limbs. In that case the agent would feel like a part of yourself.

But if that is true, the other scenario I've represented where the agent is used on a regular computer and interfaced through an UI shown on some monitor, and manipulated using a script written using a keyboard actually, isn't it in fact false? The neural representations and the functionality of both agents is the same, so why would one be one's self and the other not? Is it not likely the case that the feeling of otherness in first scenario is the one that the brain falsely constructed?

It was not too long since I've learned of this perspective, but once I did it became a philosophical weapon for me. It served to raise awareness how my brain will create nonsense to prevent me from reaching the correct conclusions that are beyond the obvious.

Not being aware of this makes programming seem like a tedious chore. Without the right belief one can only ever use programming to create machines and serve others, and never to further his own power.

There are different ways of programming and playing games. There are different purposes that those unenlightened cannot even begin to imagine.

---

Drumming my fingers on the desk, I carefully decide to make the next step.

The core in particular has some additional abilities besides it nearly limitless computational power and memory capacity. Since the Singularity has started, the world has been covered by an invisble fog of nanomachines and the fog can access it to interface with the brain directly. Right now I am interfacing with the core wirelessly with my own brain. This is also the prerequisite for playing the fully immersive virtual games on the core itself. Interfacing with the computer directly is a much more efficient way of using it than the mouse and the keyboard. Maybe it does not really matter too much for programming, but it is a huge advantage in drawing and painting for example. It makes it possible to rip an image from your imagination and translate it straight into an image.

I've only read about it, and I am eager to try it out. My art ability is so mediocre is annoying. With this, I should be able to punch a few ranks above my current skill level...or at least I would have if art classes didn't rely on old school tools, like watercolors, crayons and clay. I grimace lightly in disgust as I consider the situation. The regular classes at my school still use board and chalk, no way I am going to be able to take advantage of this if it is just school work.

Meh, forget that place. I mentally wave the image of a chalkboard in a classroom away. It is just a tremendous waste of time.

I refocus on the task at hand which is to interface the core with my brain wirelessly. I spend some time reading the manual and seeing how easy it is to make the brain link in the relevant section, I decide to move forward with it.

$$$

1:25pm. I am starting to get into it. This story is intervowen with my own life and the vow I will make by writing it will affect everything that is to come. It must be fate that I am writing this. I only started keeping the journal as a trader, and have been writing it ever since. It is really great practice for picking your thoughts from the subconscious and putting them down.

It is important that I know why I am writing the story. Doing it for the money would not make sense. I'd be safer getting a job in that case. But I want to take this kind of risk. This vow is sending a sign.

Since the brain core is small, twice that of a marble, I'll lover it flops count to something like 10^39 instead of 10^40 for a kilogram of matter. Seems fair enough.

2:50pm. You mean I can make these philosophical rants and have people pay me to do it? Writing sure is wonderful. Right now I am just about done with the first Gnosis check.

3:40pm. Ugh I am stuck right now. It is at the part where he is going forward with creating the brain link. Even though I've been in the bathroom for over half an hour, and had a break, I am feeling a lot of resistance towards getting the next sentence out.

I need some time to refill the creative budget. It feels like I've ran for a while and am out of breath.

3:45pm. I'll go back to reading the Demon Sword Maiden. This month is my vacation month so I won't feel bad about doing it.

Right now I need to get a grasp on what I want to do with the brain link scene.

3:50pm. Though it is just padding, I do like the third eye scene with the camera. I am going to go over the quoted segments and see what I can pick from that. After that I won't go into the game directly. Rather  I will connect it to the ideal of programming as programming your own mind by having the MC mind control himself into doing homework and enjoying it. This will continue for a few days up to the first decision point which will lead to the first bad end.

4:05pm. Yeah, it is fun. You think about it, this makes you hyped for it, and then you implement it, or write it down in this case. There is no need to make things complicated just yet with the outlines. The most important thing is to get into it. In terms of writing speed I know I am poor at it, but it does not bother me. Writing is not about speed.

4:10pm. I've been rolling the story in my head since 2014. Compared to then Euclid's personality has changed significantly. Originally, for examples, I did not imagine him saying 'based' so in reaction to various based scenes, but I feel the way he will be now is a lot better. I really like the lingo of the new generation. I wish I was 16 instead of 35, my generation is wasted.

4:15pm. I couldn't really avoid the brain core wankery in the intro scene. With enough computation you can do anything and brain core is the source of all power.

Let me take a proper break instead of just thinking about it. It will come to me. Maybe tomorrow I'll be able to write more if I start earlier. Today is just the first day."

---
## [fc1943s/The-Spiral-Language](https://github.com/fc1943s/The-Spiral-Language)@[e124021e64...](https://github.com/fc1943s/The-Spiral-Language/commit/e124021e64bbececd8767949932734c18cf40ffc)
#### Wednesday 2022-09-21 22:54:08 by Marko Grdinić

"4:05pm. Let me resume. Before I do anything, let me get some of the annoying things out of the way.

4:10pm. First of all, let me experiment with the log normal distribution.

https://numpy.org/doc/stable/reference/random/generated/numpy.random.lognormal.html

Rather than having the checks be dice based, I'll use various probability distributions to derive them. But I am not sure if I want to use anything other than the log normal.

4:20pm.

```py
import numpy as np

np.random.lognormal(np.log(1000),1,(5,5))
```

Interesting behavior. I see that as I vary the mean, the relative scale stays the same.

```py
np.random.lognormal(np.log(1000),.1,(5,5))
```
```
array([[ 973.48286693, 1063.78588043,  954.38802159, 1045.42961685,
        1141.60009591],
       [ 954.27084595,  861.8334098 ,  937.34670488, 1103.20541213,
        1051.42761485],
       [1086.47174424,  990.79054009,  907.21940547, 1046.74981689,
        1061.72007632],
       [1062.70227436, 1393.49749512, 1006.70573411,  840.57943421,
         925.46988404],
       [ 979.8902876 ,  967.32600929,  924.60721428,  969.83561477,
         825.8366669 ]])
```
```py
np.random.lognormal(np.log(10),.1,(5,5))
```
```
array([[ 9.57148294,  9.92452782, 10.0058025 ,  9.75127673, 10.8285448 ],
       [ 9.42889737,  8.77545769,  9.58012592, 11.01821274,  9.31528438],
       [11.20638625, 10.78452063,  8.79017341, 10.84014433, 12.280494  ],
       [10.7078647 , 10.86760494, 11.00478768,  9.09300427,  8.80002358],
       [ 9.84037163, 11.79136769,  9.57511649, 12.0268007 , 10.77889658]])
```

This is what I mean by that. If I want relative shallow deviations I can just use 0.1 as the sigma. Ok, I like this one.

```py
np.random.lognormal(np.log(2.25),.2,(5,5))
```

I'll use a sigma of 0.2 to represent the uncertainty of Euclid's ranks.

4:30pm. Let me write his char sheet.

$$$

Character Sheet

Name: Euclid
Rank: Inspired
Title: Aleator
Substrate: Universal Brain Core of the Transcendi - Rank 7 (low)

A novice on the path of transcendence. Is capable of external emotion control using the stock brain core tool, but not much else. Has some mid range skill at programming and good talent at it. Weak body and physical aptitude. Qualifies as a post-human, but just barely.

# Stats (Psy)

## Externus: Rank 2 ~ exp(N(log(2.4); 0.2))

Has a strong desire to leave the weak group he belongs to, as well as the urge to gain power.

## Gnosis: Rank 2 ~ exp(N(log(2.25); 0.2))

Is fascinated with the philosophical unknowns, as well as the self destructive aspects of the self improvement loop.

## Pathos: Rank 2 ~ exp(N(log(2.3); 0.2))

Holds the belief that effort is worth it for its own sake.

$$$

Hmmm, how about this? But the problem is where do I put it? At the end of chapter 3 maybe? I am worried about that breaking up the flow.

Well, let me give it a try.

5:05pm. Yeah, it is not so bad. This char sheet is nice and I will have the opportunity to build it up as the story goes along.

Let me start chapter 4. I do not feel like doing much right now, so let me just bring in the poem.

$$$

(Simulacrum intro)

    In the endless darkness
    Roam endless monsters
    Pain, cold, flame
    Age, time, death
    Torment

    Light and shadow
    Holy and hell

    The inevitable fate of the Universe
    Will never touch
    The courage of the Inspired
    And the power of the Transcendi

I start Simulacrum for the first time and sink into the virtual, feeling the outside reality being pushed out from my being. The sensation is quite relaxing, like falling into slumber.

As I wait for the program to load the poem appears in my sense, sentence by sentence. At first I am struck by a vision of the primordial universe. I feel a sense of danger of living in it, and a sense of hopelessness. I then feel its grandeur, and am filled with admiration. And then I feel the determination of challenging the inevitable as I read the proclamation.

The symbolism of the poem is strong, and reflects well what I am trying to become, and what I am trying to challenge. I give it high marks, I forgive the lack of rhyme. It would just get lost in translation anyway.

The introduction fades and the scene slowly manifests before me. Panning to the sky, highlighted in brilliant hues of light like a veil of gold covering it is a floating city. Against a backdrop of blue, it seemed like a distant object made of gold. I felt the sense of depth in my vision, so I could sense that the floating city was massive. Then I felt the warmth of the sun and the rustle of wind. I get the sense that I am high up and realize that I am literally floating in the air like a spirit. Though it is my first time experiencing this, I try moving my gravity defying body and have no trouble doing so. Observing the vast skies surrounding me, I look down. I notice the bustle and the humdrum of a modern metropolitan city. Skyscrapers dot the landscape and deep down below I can see cars and pedestrians walking the streets.

The vision seems very crisp and vivid. After a few moments of pondering, I realize why that is the case. In the real world I have to wear glasses so everything is blurry past a certain distance, but here I am unrestricted in my resolution. Just by focusing I can see for thousands of meters as if I was standing a foot away. Picking a random spot on the street, I can make out the minor cracks on the pavement, and the grime and the wear from people walking over it for many years. Dressed in autumn clothing, the people as they go along their life feel lifelike and real. I see them talking, exclaiming, laughing, being tired, downcast and otherwise broadcasting their emotions.

"..."

I found the whole scene very impressive. It did not seem like something that humans could create.

As soon as I start wondering how to start the game, a menu comes up in a separate sense. The Load Game option is grayed out, but Start Game and Quit are there, so I select the former and enter the Scenario Selector. Simulacrum itself rather than being a single game is an intelligent program capable of simulating a large range of scenarios. Browsing over the available scenarios, all of them seem interesting and I am having trouble deciding so I go back to the top and look at the recommended one.

Heaven's Key.

'The souls of those passed on enter the afterlife to play the grand game of cards that God has prepared for them. The second chance is given, and can be lost. Can you survive the challenges of your second life and go on to challenge the highest power there is?'

Along with that brief description, there is some setting information. When I focused on the 2d map of the world, to my surprise it unfolded to a 3d model that I could mentally rotate and zoom. I realized that the world of Heaven's Key was covered with orbital islands, much like the floating one in the intro. The tech level is similar to the current time in 2025, which is good since it probably means I won't have to play against non-humans. It is like the game anticipated what I would choose. The game seems to be responding to my desire, and it took into consideration my personal goals when doing scenario suggestions as well as the background which obviously has the Heaven's Key theme.

I think about it for a bit, and decide to go with the scenario being presented to me. The core hasn't steered me wrong yet, so I want to trust it. Having made my decision, I start the game and feel drawn into it.

(Heaven's Key intro)

    The method of recursive self improvement via iterated suicide can be used in reality. In fact, the technique represents the most viable path to getting superpowers in any kind of reality.
    - Loading Blurb

$$$

I get the chills whenever I read it. It connects so well with the third Dream as well. It is like the 2014 arcs were just fanfiction of what I am going to write here.

5:10pm. Right now I have it copied verbatim from last year.

5:25pm. I am modifying it a bit.

> Simulacrum itself is more like an engine for running different scenarios out of which they are hundreds. Browsing over the available scenarios, all of them seem interesting and I am having trouble deciding so I go back to top and look at the recommended one.

> Still...imagine I played something like Hell. No way can I fight demons and study my own mental program at the same time. Online poker is fast and furious, but sitting on a real table will give me time to study both myself and others.

There are a bunch of lines inconsistent with the overall flow in this. I like the descriptions though.

5:55pm Let me just put in the blurb, and I am done. I need to think how to integrate the following scenes properly. I like the part where he throws himself over the railing. I'll leave the actual intro to Heaven's Key for later.

You don't want to stack allegoric scenes like the intro on top of each other otherwise the story will become a mismash of symbolism. I did well to break them up. Let me paste this into docs as chapter 5.

6pm. Corrected the grammar errors.

6:05pm. Let me do a bit more, I haven't really explained properly that he is some ghostly being in the air.

...I added a few sentences.

6:10pm. Ok, let me leave it at this for today. This is 2 pages plus the char sheet done.

It semes trivial, but it does come to over 1k words.

6:15pm. I'll continue going forward. Once I finish chapter 4, I'll actually publish the story. After that I'll look into opening a Patreon.

Then whatever happens, happens. Since I haven't done art and music as I intended, my chances of success are lower, but who cares about those tricks. It is better than the story get written at all rather than me spending years fiddling with visuals and music.

There is no need to think much about success. If the story is good, it should get some readers. That should get me some money. If I manage to make enough to get the AI chip and upgrade my rig, that should be something. If I manage to make enough to earn a yearly salary where I am, that would be good. If I could set up a passive income of that level, I'd be set for life.

If not, I'll have to get a job at some point.

Spiral itself is not dead, just sleeping. A change in circumstance could revive it. If I am lucky, and I am not, maybe my proposal to do the backend will get noticed."

---
## [fc1943s/The-Spiral-Language](https://github.com/fc1943s/The-Spiral-Language)@[40da12a780...](https://github.com/fc1943s/The-Spiral-Language/commit/40da12a78028023aa823ba57cedd5cff4c335d80)
#### Wednesday 2022-09-21 22:54:08 by Marko Grdinić

"9:15am. I got up 10m ago. I'll start soon, let me first check mail. I need to do that just in case I get a message that I can access DALLE. Nothing. Ok. Let me chill for a bit and then I will start writing. I do not want to program again until I get a sponsor. If I could get a sponsor I could play around until I can get to the point where I can make money with my own power.

In the absence of that, it would make more sense to do activities that garner me concrete benefits. Hence I should write. If there is anything to this timeline, it will give me an opportunity to connect my artistic interests to my programming ones.

9:20am. I want to program, but I've exhausted the possibilities of what I can do with it with my present hardware.

9:45am. Enough chilling, let me get started.

It is not a bad idea to write. I think that the story I have going is fairly unique so it has some value to it. With the exception of the tragedies that will happen to the family, I think my life for the next 7 years will not be so bad. I've gotten programming out of the way and I have exactly the tool needed to take advantage of future hardware, my Spiral language. The only thing I am missing is the hardware.

With that goal accomplished, there is no need to keep pushing so hard and I can just unwind.

9:50am. Of course with the benefit of experience, I'd have approached poker botting very differently if I knew deep RL would be such a collosal failure. But had I approached it differently I would never have had a reason to make Spiral. It is a chicken and an egg problem. Without trying I would never have had the experience. If I could transport my knowledge and experience into the past, I could really speedrun my progress towards this point.

Right now, let me just try it out. My unique vision. It has been refined during the past 7.5 years. I need to make a test to see exactly where I stand in this world. Am I really destined for wage slavery or am I a prophet? The next year or two will decide it.

Let me write, write, write...

$$$

(At school)

As the professor rambles on some useless physics topic, I am gripped by his words. Today's session is quite enjoyable. I brought the core along with me to school and used it to fine tune my emotional state so I can be immersed into what would otherwise be boring, rambling lectures. Like yesterday, I ended tuning out my classmates again, but that does not matter. This kind of satisfaction...

Yes, I feel like I am on the right path in life. I understand that what I am essentially doing is brainwashing myself and playing myself like I would a character in a game.

Maybe there is an argument to be made that this is wrong, but...

I throw a brief glance behind me at my classmates. I didn't pay attention to the seating order and somehow ended up in front seat of all the classes. I see that half of them are not focused on the lecture. The rest are trying to make an effort, but it does not change the fact that you really need to believe that the school is not scamming you out of your time in order to fully invest yourself into learning. What I am doing here is really grand in a way. I am fully immersed into learning despite accepting the pointlessness of it.

If I went to this place just to drain my time, it would be nothing more than slow torture.

I won't give up this power. With this power, I will never have to endure boredom again in my life.

I do not think my grades will ever be a problem again.

(Euclid's Room)

I am back in my battle station. Today's school session was the best ever, all thanks to this tiny little thing!

Grinning, I raise the brain core to throw spotlight on it.

All I have been doing is some lightweight tuning using a provided tool. If I digitized myself, I could edit my mind's program directly and advance further on the proper path of a programmer. But it is unfortunate, that all intelligence augmentation methods are iterative suicide. Not to mention, digitizing myself either involves copying myself to a core or converting my brain to one.

[Pathos check DC ?? Failed]

Copying myself would allow the digitized copy of me to self improve, but I'd be the same as I am now. Doing a full brain conversion is just swapping my brain matter for computronium, either of these is not lossless so it would be a mental trick that hides my own death away from me. It might be worth going through it regardless, but what is the rush? Just being able to tune myself properly into the study material is worth 50 IQ points on its own.

I should treasure what I have.

So what should I do next?

I spend some time thinking about it. Should I try out the VR games? Hmmmm...no. I finally have the power to play my life properly, so why waste it on things that would not give me real world benefits? Now that my homework is as fun as anything else, why not immerse myself into that?

Through my mind, visions of parallel lives flow past without the core. I can easily imagine myself living from day to day in boredom and tedium, playing games to have fun. There would be a conflict between society and me due to my distrust towards it. It is not that games would have been an escape. I would have played them because I would have had belief in technology, but it would have been vague, indefinite belief in the potential of it.

Right now things are very clear. The manifestation of the potential of technology is not a bigger time suck, but this thing right here. I roll the core in my fingers for emphasis. It is the ability to program my own mind, so I should thank the millenia of scientists and engineers who have made it possible by doing my schoolwork with the rightest mindset and attitude possible.

That is what I feel like doing now and so I shall.

That night I Dreamed again.

~~~

It was like watching a black and white cartoon made of stills. As the image zoomed out, I saw a man's face with a confident grin coming into perspective. He was wearing neat and tidy, if old fashion clothing. A spitting image of a young professional. He was on a great big stage made just for him. He was going forward towards the light. And some distance away from him was the darkness and the shadows.

In them I could see people on their knees as if they were defeated, not daring to look up.

The short cartoon ended and the defeated figures were replaced by the golden ones from the previous night's dream. They were upright and staring ahead. Yesterday it was murky, but now at the edge of my vision I thought I could see light.

"Justice, where is the justice?" They lamented in a booming voice.
"We want to go forward, but we can't. What about desire, what about will? Why does the world not respect it?"
"We want to go forward and overcome! Where is the justice?"

As if the winners finally took note of the losers, they turned around and responded to the golden figures.

"You talk about justice, but put yourselves in our position." The black and white cartoon stills of the winners responded, staring down at them from above.
"I worked hard for my success." A cartoon still of a man who looked like a scientist came to one of the golden figures. "Have you spent even a third of as much time and effort as I have?"
"My wealth was the accumulation of decades." An older, but fit man who was finely dressed responded. I could see that in the background of his still there was a mountain of gold coins and teasure, as well as stacks of bills. He came closer. "What right do you have to covet it? How would it be justice if you could get it so easily?"
"My body is the result of half a decade of practice." I could see the bulging muscles on the still of a man in a skin suit who looked like a body builder. He confided to an aspirant. "You might have put in the effort, but it is not our fault you could not achieve the result you sought."
"My beauty and the adoration I receive for it is not something I worked for." A young, beautiful woman admitted. "But you understand, don't you? It is not something you can take."

After those brief personal reproaches, the stills of the winners were staring down from high above.

"You talk about justice. And you dream about being above others. Talent, wealth, beauty, intelligence, strength..." The winners enumerated as if chastising them, their voice booming through the darkness of the abyss as the golden figures listened on in silence.
"You talk about justice, while seeking inequality like hypocrites. You desire an unequal world where you have all the opportunities and advantages to rise to the top."
"You found such an unequal world where the possibility for that is there and you live in it. The justice that you sought is something that you've had all along."
"The world you live in is fair to the winners."

Leaving that last comment behind them, I could see the winners leave the scene. The golden figures stood there in silence.

~~~

$$$

10:50am. Right now I am just about to start the second dream.

12:10pm. This came out well. The third dream (on the successful branch) will be the climax. It is an allegory explaning why the universe is the way it is in Simulacrum. The vision I had last time of the self improvement aptitude makes no sense.

Even if it was only 1 in a million, that would still mean most of the Inspired would be shredded by the winner. The proper configuration that would give me the universe that I want is something else."

---
## [fc1943s/The-Spiral-Language](https://github.com/fc1943s/The-Spiral-Language)@[6b15148aa8...](https://github.com/fc1943s/The-Spiral-Language/commit/6b15148aa8bf88d1db81098fb91cc5d4e8327e58)
#### Wednesday 2022-09-21 22:54:08 by Marko Grdinić

"9:35am. Got up 15m ago. I've read Kaiji, now let me read Tenken. I seems the anime for it is two months from now.

10:25am. Let me start. I have two goals right now.

* Figure out a better synopsis.
* Figure out how to get the formatting on RR under control without necessarily having to remove all the empty spaces my hand.
* Then actually publish the story.

10:30am. Let me focus on the synopsis.

> What would a person do if he had access to a computer with nearly limitless computational power?

Hmmm...

> In the post-Singularity era where limitless computation is cheaply available, there were legendary figures seeking to take advantage of that power and make it their own. Rising above humanity, they sought power without limit and succeeded.

10:45am. Hmmm, this is a bit better.

> A story of what games are really about.

> The journey of their self development are enshrined as stories.

> One such journey is through a simulated game of poker.

10:50am. Hmmmm...

> In the post-Singularity era where limitless computation is cheaply available, there were legendary figures seeking to take advantage of that power and make it their own. Rising above humanity, they sought power without limit and succeeded, leaving behind a story of their journey on the path of transcendence.

Better.

> With enough computational power, one can do anything. In an era where one can create whole universes with a push of button, one can have fun playing a game and optimizing one's own mind.

> Far in the sky, emanating golden radiance as it floats amongst the clouds, is the city made of gold! In its game rooms, poker games of life and death unfold! The clashes of chips and cards!

> Can you conquer the game and take that power into the real world?

11:05am. Whoever is playing me rolled well this time. These last 4 quotes have potential.

///

In the post-Singularity era where limitless computation is cheaply available, there were legendary figures seeking to take advantage of that power and make it their own. Rising above humanity, they sought power without limit and succeeded, leaving behind a story of their journey on the path of transcendence. With enough computational power, one can do anything. In an era where one can create whole universes with a push of a button, one can have fun playing a game and optimizing one's own mind. Can you conquer the game and take that power into the real world?

Far in the sky, emanating golden radiance as it floats amongst the clouds, is the city made of gold! In its game rooms, poker games of life and death unfold! The clashes of chips and cards!

Devouring all newcomers and existing for eons, the city remained grand and unshaken, until one day, a novice entered the game…

///

How about this?

Synopsis is all about attitide. I need to transmit expectations about the story without saying anything about it.

> they sought power without limit
> they sought power without limit and succeeded

Consider these two quotes in isolation. Just adding 'and succeeded' completely changes what the tone. It is not something people would expect in a story about rising above humanity, so it will be great bait.

NPCs can only write stories about humanity winning, so this is a great signal. I must signal my values in the synopsis, and the further they are from standard the better.

11:25am. I can't think of anything else to change. This is good enough. Let me move to publishing again. I need to figure out how to get the paragraphs under control.

https://www.royalroad.com/forums/thread/110270?page=1#pid947118

Nevermind this, how the hell do I translate between formating.

https://www.royalroad.com/forums/thread/102804

Why is this such a pain in the ass, what the fuck?

This is like the fifth thread I've looked into.

Ah, I see. If I paste it as plain text, then it gets rid of the superflous empty lines and gives me proper paragraphs. This is the solution and I found it by myself. Let me just roll with it.

> A side effect of the operation is that the brain will have slightly increased energy consumption which will require me to eat more if I use the link regularly.

Hmmmm, should I just get rid of this? Yeah, I think I should for consistency.

> It says the link isn’t powered by my biology, but the nanofog, so the use of it won’t increase my energy consumption. That is good.

I can only lose by making computation expensive so let me get rid of that.

I'll add Gore to content warning, but otherwise keep the tags as I have yesterday. Bad ends will have violent depictions, but otherwise it is not the focus of the story.

12pm. I submitted it. It says it can take up to 48h for one of their staff members to look at it. It is Tuesday, so I am safe on that front.

https://www.royalroad.com/profile/303912

Here is my profile: ghostlike. I wanted to take that on Wordpress back in 2015, but it was taken, so I added some numbers to make it go through.

12:05pm. Once it gets added to the site, I'll post the rest of the chapters as well as some of the illustrations that I've done. I read in a /g/ thread that Stable Diffusion will go out of beta next week.

12:10pm. Right now I am a bit in a daze.

Anyway, to get popular as a writer, I'll go with the slow burn method. I'll get the page count high and let people discover me on their own. Back in 2014, I had no choice but to spam Reddit to get some initial readers, but that is in the past.

Sure, with active marketing, you can get a lot more views, and faster, but I am not in a hurry. People recommending my work would be the best kind of advertizing I could ask for. The key is to find a niche.

Since there isn't really a story like Heaven's Key out there, that gives me a big edge.

12:20pm. Anyway, forget Royal Road for a few days. What I should focus on is writing the next chapter.

12:25pm. Let me have breakfast here."

---
## [fc1943s/The-Spiral-Language](https://github.com/fc1943s/The-Spiral-Language)@[448da74eb0...](https://github.com/fc1943s/The-Spiral-Language/commit/448da74eb0a43535b88e3bc30f60f9c621f3be4a)
#### Wednesday 2022-09-21 22:54:08 by Marko Grdinić

"2:05pm. Done with breakfast. Let me chill and then I will resume writing.

2:25pm. Right now the temperatures are fine at 30C, but my mom mentioned yesterday she heard they are going to rise to 39C. I am not sure how much to believe that. If that happens it is going to be hell in this room. Anyway, I do not feel like writing. I'll turn off the computer and step away from the screen for a while. Right now I've caught up to where I was last year.

I want to think about the next scene carefully and in depth. Maybe I should finally do some outlining now that I am almost done with the intro parts.

I got the momentum going and established my own motivation. I can afford to slow things down somewhat so as to think about it.

2:35pm. Let me rest. If feels like I only have a few hours in a day to work in. It is ridiculous. I am always so strapped for time.

5:35pm. I meant to resume, but I see that it is almost 6pm, so I'll skip. I've had some time to think about it.

5:50pm. For the first time, I thought in depth about the general backstory of the city. I guess that will take place of the outlining.

I want to write, but I do not feel like doing it right now.

In times like these I have to remind myself that this also double as a vacation. I already did a bit for the day so it is not like I am slacking. Let me mind off. I think maybe Playing Pathfinder until so late did damage me. I need to go to bed earlier. If necessary, to make time for sleep, I'll compress my work into a shorter session rather than aiming for 6pm like before.

It will be a tug of war between different desires.

I think if that by the end of the week I do not receive a reply to my Tenstorrent proposal I'll try emailing support and asking them about it. I really wish I could get in touch with somebody doing work at the company. Right now, let me play games and watch anime. That is the way it should go.

5:55pm. I am actually quite stressed due to not writing anything in the afternoon session. I already feel like I am falling behind. I need to learn to just let some things go. I can't be writing every day like a robot if I want to do good work."

---
## [Buildstarted/linksfordevs](https://github.com/Buildstarted/linksfordevs)@[6eeb8fe94f...](https://github.com/Buildstarted/linksfordevs/commit/6eeb8fe94fe6c9bac4e4476ed4c6075901805974)
#### Wednesday 2022-09-21 23:06:37 by Ben Dornis

Updating: 9/21/2022 10:00:00 PM

 1. Added: Password Purgatory - Making Life Hell for Spammers
    (https://passwordpurgatory.com/get-hell?kvKey=8329bd60-24e6-4e13-bd61-4d481872fbcb)
 2. Added: Branchable MySQL: Managing multiple dev environments
    (https://mliezun.github.io/2022/09/20/branchable-mysql.html)
 3. Added: DuckDB: Query SQLite and PostgreSQL Data
    (https://pradeepchhetri.xyz/til/duckdbexternal/)
 4. Added: The cost of partial automation
    (https://pallissard.net/2022/09/19/automation_and_value/)
 5. Added: Renaming Our Company Revealed a Critical Bug
    (https://alic.dev/blog/renaming.html)
 6. Added: The Wage Gap 2
    (https://elsajohansson.wordpress.com/2022/09/16/the-wage-gap-2/)
 7. Added: Rolando Murillo → Trying vs. really trying
    (https://www.rolandomurillo.com/2022/04/07/trying-vs-really-trying)
 8. Added: 300 Signups, No Product, Only Landing page - Michael Salim | Senior Full Stack Freelancer and Startup Founder
    (https://michaelsalim.co.uk/blog/300-signups-no-product-only-landing-page/)
 9. Added: Alfred, or "How to super-charge your Mac and automate routine tasks"
    (https://blev.dev/articles/alfred/)
10. Added: Spellcheckers exfiltrating PII… not so fast  ::  Aaron Gustafson
    (https://www.aaron-gustafson.com/notebook/spellcheckers-exfiltrating-pii_-not-so-fast/)
11. Added: The Only Client Experience
    (https://shermanonsoftware.com/2022/09/21/the-only-client-experience/)
12. Added: Ask.FM user database with 350m user records has shown up for sale
    (https://www.databreaches.net/ask-fm-user-database-with-350m-user-records-has-shown-up-for-sale/)
13. Added: Pilot Priority List
    (https://xkcd.com/2675/)
14. Added: Should you Soft Delete?
    (https://codeopinion.com/should-you-soft-delete/)

Generation took: 00:06:25.6932654
 Maintenance update - cleaning up homepage and feed

---
## [mcmire/superstruct](https://github.com/mcmire/superstruct)@[586a18ebf2...](https://github.com/mcmire/superstruct/commit/586a18ebf25d5b4c562f4011bd6529267e98ab36)
#### Wednesday 2022-09-21 23:29:59 by Elliot Winkler

Support Node 14 (again)

It appears that between 0.16.0 and 0.16.1, the minimum version of Node required
to use this package changed, from 14.x to 16.x. This was not explicit but seems
to have been caused by a couple of factors.

But first, what changed. If you look at `src/error.ts` in 0.16.0 you will see
[this line][1]:

```
return (cached ??= [failure, ...failures()])
```

In the [published version of this file in 0.16.0][2] this gets transpiled to:

```
return (_cached = cached) != null ? _cached : cached = [failure, ...failures()];
```

In 0.16.1, the [original line is unchanged][3], but in the [published
version][4] it is transpiled to:

```
return cached ??= [failure, ...failures()];
```

The `??=` syntax is not supported by Node 14, hence, developers are forced to
upgrade to at least Node 16 if they want to use v0.16.1 or greater.

After looking at the diff between these two versions and running some
experiments, I believe that there are two reasons why this line shows up
differently in these two published versions.

1. Different Node versions were used to build and publish these versions. It
appears that Node 14 was used for the former whereas Node 16 was used for the
latter. This assertion is supported by the fact that in the [Rollup
configuration][5], `@babel/preset-env` is configured with `node: true`, which
instructs Babel to [use the current version of Node as a target][6]. So if the
current Node version changes, so does the Babel config.
2. Between 0.16.0 and 0.16.1, [`browserslist` was updated from 4.20.3, to
4.21.4][7] (you will probably need to expand `yarn.lock`; if so, Cmd-F for
"browserslist"). In `browserslist` 4.21.0, [IE 11 was removed from the default
set of browsers][8] (which is being used in this case, since no explicit list is
provided). According to caniuse, [IE 11 does not support the `??=` syntax][9],
so its removal means that Babel doesn't need to transpile this syntax any
longer.

To address this problem, this PR:

* changes the Rollup configuration mentioned above to use `node: "14.0"` instead
of `node: true`, so that Node 14 is always used to compute the transpilation
rules regardless of the version of Node used locally to build and publish the
package
* updates the CI workflow to ensure that Node 14 is being tested (along with 16
and 18)
* adds Node >= 14 to the `engines` field to communicate that it is supported

---

One thing you may wonder is why this change is needed at all. Node 16 is the
current LTS, so shouldn't that be enough? True, but Node 14 hasn't hit
end-of-life yet, and many people are still using it, including my company. We
think this package is really great, but it would be even better if we didn't
have to have a workaround for our libraries that we still want to keep on Node
14.

Thanks for considering :)

[1]: https://github.com/ianstormtaylor/superstruct/blob/v0.16.0/src/error.ts#L44
[2]: https://unpkg.com/superstruct@0.16.0/lib/index.cjs
[3]: https://github.com/ianstormtaylor/superstruct/blob/v0.16.1/src/error.ts#L44
[4]: https://unpkg.com/superstruct@0.16.1/lib/index.cjs.js
[5]: https://github.com/ianstormtaylor/superstruct/blob/v0.16.4/config/rollup.js#L26
[6]: https://babel.dev/docs/en/options#targetsnode
[7]: https://github.com/ianstormtaylor/superstruct/compare/v0.16.0...v0.16.1?diff=unified#diff-51e4f558fae534656963876761c95b83b6ef5da5103c4adef6768219ed76c2deL99
[8]: https://github.com/browserslist/browserslist/blob/main/CHANGELOG.md#421
[9]: https://caniuse.com/?search=%3F%3F%3D

---
## [dracula/obsidian](https://github.com/dracula/obsidian)@[b30ea94d47...](https://github.com/dracula/obsidian/commit/b30ea94d477e5e3e1bb5569809fb5b9142ec700e)
#### Wednesday 2022-09-21 23:42:48 by The Arctesian

Rm `$` from install.md

Lets do this the proper way shall we. The $ in front is kinda annoying, makes you have to ctrl a then ctrl d which is not fun and for nubes having to arrow all the way back is a pain

---

