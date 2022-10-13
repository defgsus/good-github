## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-10-12](docs/good-messages/2022/2022-10-12.md)


2,062,156 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,062,156 were push events containing 3,147,560 commit messages that amount to 246,324,847 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 48 messages:


## [Fis-Ura/Narikiri-Dungeon-X](https://github.com/Fis-Ura/Narikiri-Dungeon-X)@[9d7a546e00...](https://github.com/Fis-Ura/Narikiri-Dungeon-X/commit/9d7a546e008dbe606d9fac10622ee592943ff081)
#### Wednesday 2022-10-12 00:44:30 by FistingUranus

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
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[e9d4bf6c49...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/e9d4bf6c4920f07f03c2425ac3e69caf8daced9d)
#### Wednesday 2022-10-12 01:32:39 by Zergspower

Granite's Love pass 1 of X for ruins  (#16746)

* Fab Five

* forgot to move the rack in front of the false wall

* Holy shit scrapheap looked HORRIBLE

---
## [ammarfaizi2/linux-fork](https://github.com/ammarfaizi2/linux-fork)@[5a756962d1...](https://github.com/ammarfaizi2/linux-fork/commit/5a756962d12de3fd938513ac987808d05cec623b)
#### Wednesday 2022-10-12 03:02:34 by Johannes Weiner

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
## [Nerev4r/Skyrat-tg](https://github.com/Nerev4r/Skyrat-tg)@[23b7daee59...](https://github.com/Nerev4r/Skyrat-tg/commit/23b7daee59100e34f488893b57cd3787a0c08b99)
#### Wednesday 2022-10-12 03:46:44 by SkyratBot

[MIRROR] Simplifies SM damage calculation, tweaks the numbers. [MDB IGNORE] (#16733)

* Simplifies SM damage calculation, tweaks the numbers. (#70347)

About The Pull Request

We apply the damage hardcap individually now, split off the old flat 1.8 into individual caps for heat, moles, and power.

Set it to 1.5 for heat, 1 for mole and 1 for power. This means for most delams it'll be a tad slower! But its possible to make SM delam nearly twice as fast if you combine all 3. (3.5). Be pretty hard tho.

Set the heat healing to -1 so you can counteract one factor at most (except heat since you'll never get both heat healing and heat damage at the same time anyway).

I'm not hell bent on any of the numbers, just picked round even ones and ones that i think will make sense. If you want them changed lmk.

Got rid of the cascade mole and power multipliers since there's probably like three people that are aware that it even exists. Ideally we just add another entry to the CIMS but its already pretty crowded. Figured nobody is gonna miss it anyway? Sorry ghil.

Got rid of the moles multiplier thing since its nicer to keep the temp damage fully based on temp damage instead of adding another multiplier. I just applied the .25 to the damage flatly, meaning it slows down delams again!

And some space exposure stuff: #70347 (comment)
Why It's Good For The Game

Hardcap: Discrete, less randomly interconnected factors are easier to present and remember. The calculation procs are also made to be additive so we had to hack a bit and do some rescaling to accomodate the old behavior in my original PR #69240. Can remove the hack if this pr goes through.

Cascade and mole multiplier: The rest are just getting rid of underutilized factors so we have a cleaner behavior to maintain, present, and understand. (In a perfect world modifiers that aren't visible to the players shouldn't have been merged in the first place smh smh)
Changelog

🆑
fix: Fixed sm space exposure damage going through walls
del: got rid of the molar multiplier for sm heating damage. It will now only impact molar damage and temp limit. We apply the lowest value directly so this slows down sm delams a tiny bit.
del: got rid of cascades making sm delam at 450 moles and 1250 mev. It delams normally now.
balance: Applied the sm damage hardcap of 1.8 individually to heat (1.5), moles (1), power (1). Meaning most sm delams are slower now, but the really bad ones can be faster.
balance: Halved sm temp healing across the board. Temp limits are still the same though so you shouldn't notice it that much.
balance: Halved SM power damage across the board.
balance: Changed sm space exposure damage to just check for the current tile and adjacent atmos connected tiles.
/🆑

* Simplifies SM damage calculation, tweaks the numbers.

Co-authored-by: vincentiusvin <54709710+vincentiusvin@users.noreply.github.com>

---
## [macvim-dev/macvim](https://github.com/macvim-dev/macvim)@[83e925e923...](https://github.com/macvim-dev/macvim/commit/83e925e9230bbdff93379b5dde3b8b36b561eb40)
#### Wednesday 2022-10-12 04:28:59 by Yee Cheng Chin

Support dictionary/data lookups of text

This adds support for looking up data under the mouse cursor. Usually it
will bring up a dictionary, but other times it could be a Wikipedia
article, Siri knowledge, etc. Apple doesn't really have a good name for
it, other than "looking up data", "quick look" (a confusingly similar
name with the other Quick Look OS feature), or "show definition". You
can activate this by doing Ctrl-Cmd-D when the mouse is over a cursor.
If you have a trackpad, you can also either activate this using Force
click or three-finger tap (depends on your system preference settings).

Note that for Force click, this could potentially make it impossible to
use the MacVim `<ForceClick>` mapping in Vim, which allows you to map a
force click to a Vim command (#716). This is handled by having a new
setting (under a new "Input" preference pane which will have more
populated later) that allows you to choose whether to use Force click
for data lookup or Vim's `<ForceClick>` mapping. If you have configured
to use three-finger taps though this setting wouldn't do anything, and
`<ForceClick>` is always send to the Vim mapping.

Also, this is lacking a lot of features that a normal macOS application
would get, e.g. looking up selected texts (e.g. if you have "ice cream",
you may want to select the whole thing to look up the phrase, rather
than just "ice" or "cream"), data detector, and much more (e.g. custom
API support). They will be done later as part of #1311.

Technical details below:

The way the OS knows how to look up the data and present it is by
talking to the NSTextInput/NSTextInputClient. Previously MacVim
implemented NSTextInput partially, and didn't implement the critical
firstRectForCharacterRange:actualRange and characterIndexForPoint:
functions. First, in this change we change from NSTextInput to
NSTextInputClient (which is the newer non-deprecated version), and
implement those functions, which allows the OS to query the text
storage.

By default, the OS sends a quickLookWithEvent: call to us whenever the
lookup happens but for some odd reason this isn't automatic for Force
clicks, presumably because some apps want to handle Force clicks
manually (this is why some apps only work for three-finger taps but not
Force clicks for lookups). This isn't documented but I found references
in iTerm/Firefox, and basically we just need to manually handle it and
send off quickLookWithEvent: when handling Force clicks.

For implementing the NSTextInputClient properly, the main issue is
making sure that can work properly with input methods / marked texts,
which is the other primary purpose for this class (other than inputting
keys). For data lookups, I'm representing the grid as a row-major text
(with no newline/space in between) and expose that to the OS. This
already has some issue because it doesn't handle Vim vertical splits
well, as MacVim doesn't really have access to detailed Vim text buffers
easily (unless we do a lot of calls back-and-forth). This means wrapped
texts won't be looked up properly, which I think is ok. Also, the OS
APIs deal with UTF-8 indices, so we can't just convert row/column to raw
indices and have to do a lot of character length calculations
(especially for wide chars like CJK or emojis) to make sure the returned
ranges are consistent and valid. For marked texts though, this presents
a challenge because Vim doesn't really have a strong enough API to
communicate back-and-forth about the marked positions and whatnot (it
only let the GUI know where the current cursor is), and it's hard to
implement APIs like `markedRange` properly because some marked texts
could be hidden or wrapped (if you implement some of these functions
improperly Apple's input methods could start misbehaving especially when
you use arrow keys to navigate). In the end I kept the original
implementation for treating the marked texts as a range starting from 0,
*only* when we have marked text. Kind of a hack but this makes sure we
work both in marked text mode (i.e. when inputting texts) and when doing
lookups. For simplicity I made it so that you can't do data lookups when
in marked text mode now.

Input method:

This change also fixes a quirk in input method as a driveby change.
Previously the logic for calculating the rect for where the candidate
list was quite broken, but now it's calculated correctly using the
desired range and the current cursor position. This matters when say
using Japanese IM and using the left/right arrow to jump to different
sections of the text. If the desired range is in a wrapped line, the new
logic would attempt to pin it to the left-most column of where the
cursor is in the range.

Data detection:

Note that the default implementation is quite bare, and lacks a lot of
smart data detection. For example, if you put your mouse over a URL, it
won't properly select the whole URL, and addresses and dates for example
also won't get grouped together properly. This is because these require
additional implementation (e.g. using NSDataDetector) instead of coming
"for free", and will be handled later. In fact, Apple's WebKit and
NSTextView cheats by calling an internal API framework called "Reveal"
(which you can find out by intercepting NSTextView's calls and/or
looking at WebKit's source code) which is much more powerful and
supports looking up package tracking, airline info, and more, but it's
not available to third-party software (that's why Safari's lookup is so
much better than Chrome/Firefox's).

This isn't tested right now. Future task needs to add XCTest support to
properly test this as there are a lot of edge cases involved here.

Fix #1191
Part of Epic #1311, which contains other items to be implemented.

---
## [landonb/myrepos](https://github.com/landonb/myrepos)@[e8d8c8b772...](https://github.com/landonb/myrepos/commit/e8d8c8b7720ef55067c0d6d738a61e271152b9a6)
#### Wednesday 2022-10-12 04:44:46 by landonb

Bugfix: Old code broken on latest Perl (or something like that)

- Unexpectedly, I saw a new issue with old code today.

  - One of the `runsh` calls was passing the `system` command
    as an argument:

      my ($ret, $out)=runsh $action, $topdir, $subdir, $command, [], system;

  - But on a new MacBook I'm setting up, the `system` command argument
    is evaluated instead and generates an error, which looks like this:

      Can't exec "": No such file or directory at /Users/.../myrepos/mr line 2076.

  - I only saw this on one machine, and even, I only saw it with `mr`.
    - It happened on a new client MacBook, Perl v5.30.3, macOS 12.6.
    - It did not happen on an old MacBook, that I had over a year ago.
    - It does not happen on my personal Linux Mint 19.3, Perl v5.26.1.

  - It also does not happen when I try to reproduce the issue with a small
    test script on that new MacBook.

    - A bare `system;` works without complaint.

    - However, I do see an issue trying to pass `system` as a function
      argument, and then calling it from a subroutine, like how the
      problem code was passing `system` to `runsh`.

      - When I run this code to mimic the problem code's behavior:

          sub fcn { $runner = shift; $runner->("echo foo"); }; fcn system;

        I see an undefined-subroutine error, e.g.:

          Undefined subroutine &main::-1 called at ./test.pl line 2.

  - Given these results, I'm not clear on what's happening.

    - I'm surprised that the test code does not show the same issue,
      where `system` is evaluated when used as a function argument.

    - Interestingly, the solution -- which is to pass a lambda subroutine
      that calls `system` when its invoked -- is used on another similar
      call to `runsh` elsewhere in the code.

      - It also appears that I wrote those pieces of code in 2019,
        both the old problem code, and the other code that uses a
        lambda function.

        Though I'm not sure why I took two different approaches.

      - This is also the only Perl project that I hack on.

        And I was surprised in 2022 to see how much Perl I wrote in 2019.

        But I'm guessing that I was using `system` wrong (I was treating
        it like a Python built-in and trying to reference it). But that's
        probably not how Perl allows you to use built-ins.

      - Indeed, looking at the documentation, I don't see definitively
        one way or not if Perl supports passing built-in commands as
        function parameters, or even referencing them from variables.

        And the way `runsh_bool` calls `runsh`, I don't think that the
        subroutine argument holding the `system` reference was ever called,
        because `runsh` short-circuits (guard-clauses?) when passed 'true'
        or 'false' (which is how `runsh_bool` calls it). In all likelihood,
        this code would've failed if the passed `system` argument was ever
        called. And this code probably worked fine until maybe the latest
        Perl introduced changes to call `system` even when not passed any
        arguments (though, while I'm not lazy enough to write this huge
        commit message, I am too lazy to try to verify my last statement,
        say, by reading the Perl what's-changed history).

        In any case, it's fixed, and whether or not I completely
        understand what was happening, I at least have this dizzyingly
        long commit message to reflect on, and I'm happy, because `mr`
        works and I can continue onboarding that new machine. /blocked

---
## [san7890/bruhstation](https://github.com/san7890/bruhstation)@[a86f986604...](https://github.com/san7890/bruhstation/commit/a86f986604e2c63fc5a1d72c144be3ad3d7ae6b4)
#### Wednesday 2022-10-12 05:18:01 by san7890

i hope the guy who adds a new demon sheds a tear over this

oh thank god the code is so advanced i can add span_narsie to the shatter message phew this is so fucking cash so fucking money

---
## [w17612745587/react](https://github.com/w17612745587/react)@[b6978bc38f...](https://github.com/w17612745587/react/commit/b6978bc38f6788c7e73982b9fd2771aabdf36f15)
#### Wednesday 2022-10-12 05:39:42 by Andrew Clark

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
## [kyasu/android_kernel_xiaomi_sdm660](https://github.com/kyasu/android_kernel_xiaomi_sdm660)@[74801a86a9...](https://github.com/kyasu/android_kernel_xiaomi_sdm660/commit/74801a86a992968bdce34fb792032114d98ff7ef)
#### Wednesday 2022-10-12 06:46:30 by Christian Brauner

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
## [aslenofarid/kernel_asus_sdm660](https://github.com/aslenofarid/kernel_asus_sdm660)@[2775678a5c...](https://github.com/aslenofarid/kernel_asus_sdm660/commit/2775678a5cdf1cf919e66000038076a83454b76a)
#### Wednesday 2022-10-12 06:48:15 by Dan Pasanen

power: don't ever reboot to verity red

* We get it, shit's broken. We're flashing custom stuff, shit's bound
  to break. Don't pop this annoying screen up, we're not even using
  verity anyway.

Change-Id: Icd77b70ec1df9108a4ba9e7fd8cb9623b35b78db
Signed-off-by: Albert I <kras@raphielgang.org>
Signed-off-by: aslenofarid <yoniasleno.farid14@gmail.com>

---
## [glebpigulevsky/itbeard-site](https://github.com/glebpigulevsky/itbeard-site)@[1104acbd66...](https://github.com/glebpigulevsky/itbeard-site/commit/1104acbd664adf484562eb44c9ed3e39ad0e1e50)
#### Wednesday 2022-10-12 06:57:44 by itbeard

remove yandex metrics - russian warship go fuck yourself

---
## [JohnFulpWillard/tgstation](https://github.com/JohnFulpWillard/tgstation)@[a2577296e6...](https://github.com/JohnFulpWillard/tgstation/commit/a2577296e62a0f3c335648169a335fe7d3de4bdc)
#### Wednesday 2022-10-12 07:11:14 by RikuTheKiller

Upgrades the Modsuit Adapter Shell (#70286)

Code improvements are much appreciated as some things may be rather hacky.

Adds more options to the currently very limited modsuit adapter shell. Right now you can only select a module and activate (not deploy) the suit.

This has some major problems as you literally can't even deploy the suit to activate it so that's rendered useless and selecting a module is like... kind of a weird input anyways but I won't judge so I left it in. Please comment down below if you'd like for me to add an "Activate Selected Module" input and "On Module Activated" output as those are certainly possible to do. I was just a little torn on how balanced that would be.

Changes:

"Module to Select" input is now an option. You can still use a string input, but simply inserting it into the suit and activating it, then accessing the circuit that way will give you a list of all modules that the modsuit has.
Modsuit quick deploy (RMB) no longer tries to deploy the rest of the pieces when used while the suit is only partially deployed. It will now instead retract the extended pieces. This makes the "Toggle Deployment" input less prone to errors. (Why was it like this in the first place? Having to manually retract the already extended pieces sucks ass.)
Added Inputs:

"Toggle Deployment" is a new signal input that does exactly what it says it does. It simply tries to extend or retract all pieces of the modsuit depending on it's current state.
Added Outputs:

"Activated" is a new number output that outputs 1 if the suit is activated and 0 if it's not.
"Deployed" is a new number output that outputs 1 if all parts of the suit are extended and 0 if they aren't.
"Deployed Parts" is a new string list output that outputs a list of the names of all currently deployed parts.
"On Deploy" is a new signal output that outputs a signal whenever all parts of the suit are deployed or retracted, regardless of the method used.
"Finished Toggling" is a new signal output that outputs a signal whenever the suit has finished activating or deactivating, regardless of the method used.

---
## [JohnFulpWillard/tgstation](https://github.com/JohnFulpWillard/tgstation)@[422accbe4e...](https://github.com/JohnFulpWillard/tgstation/commit/422accbe4e9b53f075f9a76ba6293435cb3399da)
#### Wednesday 2022-10-12 07:11:14 by John Willard

[MDB IGNORE] Shuttle engines part 2: Engines are now machines (#69793)

* Makes engines machines instead of structures

* Updates the maps

* Fixes boards and anchoring

* Removes 2 unused engine types

Router was actually used a total of once, so I just replaced it with propulsion.
I think cutting down on these useless engine types that make no difference in-game would be a nice first step to adding more functionalities to them.

* Don't use power (since shuttles dont have)

Shuttles don't have APCs, instead they just have infinite power, so I'm removing their power usage for now. I'm hoping this can be removed when unique mechanics are added to engines, because I would like them to make use of power like other machines.

* re-organizes vars

* deletes deleted dm file

* Slightly improves cargo selling code

* Renames the updatepaths

* Removes in_wall engines

I hate this stupid engine it sucks it's useless it's used solely for the tram it provides nothing of benefit to the server
replaces them with regular engines

---
## [tbg/cockroach](https://github.com/tbg/cockroach)@[0727769539...](https://github.com/tbg/cockroach/commit/0727769539578f7e38152ebacb6b30ba1758e11b)
#### Wednesday 2022-10-12 07:17:38 by Tobias Grieger

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
## [ProtonMail/WebClients](https://github.com/ProtonMail/WebClients)@[11309f40fc...](https://github.com/ProtonMail/WebClients/commit/11309f40fc89697dd40b8a6cae682abe04b1e713)
#### Wednesday 2022-10-12 07:45:25 by econdepe

Re-calculate alarms when computer is back from sleep

Since Javascript does not provide an API to fire events at given times, to fire a
browser notification for a calendar event we set a timeout with the appropriate delay.
If the computer is suspended, for Javascript no time is passing, meaning the timeout will
trigger later than expected. If your computer slept for 8 hours and you didn't reload your tab,
your notification would arrive 8 hours later, which is not great.
This MR introduces a hook that allows to detect when the computer goes to sleep, and forces
a timeout delay re-computation when the computer wakes up.

Additionally, we recently changed the lookahead time with poor judgement. With the new lookahead of 12 hours
the typical user would load the app in the morning, basically fetching the alarms for that day only,
then fetch again late in the day the alarms for the night (probably none).
If the computer then went to sleep say 8 hours in the night, before fetching alarms for the next day, the
next fetch would be delayed 8 hours and instead of fetching in the morning again, the fetch would happen
in the late afternoon, missing all the alarms in the day :(

CALWEB-2621

---
## [Financial-Times/n-express](https://github.com/Financial-Times/n-express)@[d36f98961e...](https://github.com/Financial-Times/n-express/commit/d36f98961eaf49164c99d099415e7604dccda7df)
#### Wednesday 2022-10-12 08:00:09 by Rowan Manning

Add a withSentry option to allow disabling n-raven

This option is the first step towards us being able to provide an
alternative for Sentry, or at least unpick our Sentry implementation
from n-express. This is needed for us to even properly experiment in
this space, we'd like to be able to trial disabling Sentry on some of
our low-traffic internal apps (e.g. Houston) and it's currently not
possible at all.

Notes on my choices:

  - Because importing the n-raven module has side-effects (i.e. just
    requiring it will register uncaught exception handlers), we had to
    move the `require` statements into conditionals within the n-express
    setup code. This is a little ugly. We could possibly abstract this
    into a new file within n-express if you really hate this.

  - I opted for a `withSentry` option defaulting to `true` as this is
    consistent with the other n-express options.

  - In production, the default error handler outputs the Sentry error ID
    if it's enabled and we no longer have that data if the `withSentry`
    option is `true`. I decided a reasonable alternative which doesn't
    give away any important error information would be to send the
    status code and status message associated with the error.

  - For now (at the request of Joel) I added a warning message if you
    set the `withSentry` option to `false`. This is to highlight that
    it's still an experimental option and so that we in the Reliability
    team can keep track of any apps which have disabled Sentry
    prematurely.

---
## [bitspook/notes-migrator](https://github.com/bitspook/notes-migrator)@[d8288201d8...](https://github.com/bitspook/notes-migrator/commit/d8288201d830c97545b768b2f0f317b63c8905a7)
#### Wednesday 2022-10-12 09:07:24 by hapster

nm/denote-to-logseq: fix: Proper new link inserting and and directory substitution

Testing your new code, no files would be written to a new directory.  However, the
links would be changed in the old directory (thank god I have used "test-*"
directories!), albeit without inserting a space after.

I thus checked the functioning of `nm--migrate-denote-files-to-logseq` and found that
`expand-file-name` does not behave as expected in combination with your rendition of
`string-replace`.  Using LET to input values for `denote-directory` and
`logseq-directory`, I found that DEST evaluates to ./path-to-file.org.

I then remembered that there is a native function that returns just the file name
without directory, `file-name-nondirectory`.  Using these changes, I was able to
successfully migrate from TEST-DENOTE to TEST-LOGSEQ :)

I don't know how exactly this works, but I know that it has not worked before and
works afterwards with the same input values.

Going forward, what do you think is required to improve on the version that is
already present?  One thing I have in mind but with which I don't have any experience
whatsoever is emitting error messages when stuff doesn't work as expected.  Then, I
feel like returning a list containing N NIL where N is the number of files is kind of
noisy.

Furthermore, I believe the next step would be to check if there is a way to refactor
so that there is less redundance for the two migration functions (roam -> denote,
denote -> logseq).  Again, that is an idea, but I am not experienced with this kind
of stuff.

Two closing thoughts: first off, at what point do you think it would make sense to
post and update to reddit (could increase exposure and more skilled people joining
in)? Second, what would be required to make the program, as is, usable as a package?
I feel like the minimum requirement for that would be the capacity to define
LOGSEQ-DIRECTORY and DENOTE-DIRECTORY and to emit an error message when they are not
defined or no files are found there.

---
## [petre-symfony/symfony-6-and-the-database](https://github.com/petre-symfony/symfony-6-and-the-database)@[6e95f7472d...](https://github.com/petre-symfony/symfony-6-and-the-database/commit/6e95f7472df3439ff2c826c6558e038a590cc2cf)
#### Wednesday 2022-10-12 09:20:09 by petrero

2. docker-compose & Exposed Ports - docker-compose ps, docker-compose exec database psql --user app --password app

  We need to get a database running: MySQL, Postgresql, whatever. If you already have one running, awesome! All you need to do is copy your DATABASE_URL environment variable, open or create a .env.local file, paste, then change it to match whatever your local setup is using. If you decide to do this, feel free to skip ahead to the end of chapter 4 where we configure the server_version.

  Docker Just for the Database
  - For me, I do not have a database running locally on my system... and I'm not going to install one. Instead, I want to use Docker. And, we're going to use Docker in an interesting way. I do have PHP installed locally:

    php -v
  So I won't use Docker to create a container specifically for PHP. Instead I'm going to use Docker simply to help boot up any services my app needs locally. And right now, I need a database service. Thanks to some magic between Docker and the Symfony binary, this is going to be super easy.

  To start, remember when the Doctrine recipe asked us if we wanted Docker configuration? Because we said yes, the recipe gave us docker-compose.yml and docker-compose.override.yml files. When Docker boots, it will read both of these... and they're split into two pieces just in case you want to also use Docker to deploy to production. But we're not going to worry about that: we just want to use Docker to make life easier for local development.

  22 lines  docker-compose.yml
  version: '3'
  services:
  ###> doctrine/doctrine-bundle ###
  database:
    image: postgres:${POSTGRES_VERSION:-13}-alpine
    environment:
      POSTGRES_DB: ${POSTGRES_DB:-app}
      # You should definitely change the password in production
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD:-ChangeMe}
      POSTGRES_USER: ${POSTGRES_USER:-symfony}
    volumes:
      - db-data:/var/lib/postgresql/data:rw
  9 lines  docker-compose.override.yml
  version: '3'
  services:
  ###> doctrine/doctrine-bundle ###
  database:
    ports:
      - "5432"
  These files say that they will boot a single Postgres database container with a user called symfony and password ChangeMe:

   Tip

     The username changed from symfony to app in the newest recipe version.

  It will also expose port 5432 of the container - that's Postgres's normal port - to our host machine on a random port. This means that we're going to be able to talk to the Postgresql Docker container as if it were running on our local machine... as long as we know the random port that Docker chose. We'll see how that works in a minute.

  By the way, if you want to use MySQL instead of Postgres, you absolutely can. Feel free to update these files... or delete both of them and run:

    php bin/console make:docker:database
  to generate a new compose file for MySQL or MariaDB. I'm going to stick with Postgres because it's awesome.

  At this point, we're going to start Docker and learn a bit about how to communicate with the database that lives inside. If you're pretty comfortable with Docker, feel free to skip to the next chapter.

  Starting the Container
  - Anyways, let's get our container running. First, make sure you have Docker actually installed on your machine: I won't show that because it varies by operating system. Then, find your terminal and run:

    docker-compose up -d
  The -d means "run in the background as a daemon". The first time you run this, it'll probably download a bunch of stuff. But eventually, our container should start!

  Communicating with the Container
  - Cool! But now what? How can we talk to the container? Run a command called:

    docker-compose ps
  This shows info about all the containers currently running... just one for us. The really important thing is that port 5432 in the container is connected to port 50700 on my host machine. This means that if we talk to this port, we will actually be talking to that Postgres database. Oh, and this port is random: it'll be different on your machine... and it'll even change each time we stop and start our container. More on that soon.

  But now that we know about port 50700, we can use that to connect to the database. For example, because I'm using Postgres, I could run:

    psql --user=symfony --port=50700 --host=127.0.0.1 --password app
  That means: connect to Postgres at 127.0.0.1 port 50700 using user symfony and talking to the app database. All of this is configured in the docker-compose.yml file. Copy the ChangeMe password because that last flag tells Postgres to ask for that password. Paste and... we're in!

  If you're using MySQL, we can do this same thing with a mysql command.

  But, this only works if we have that psql command installed on our local machine. So let's try a different command. Run:

    docker-compose ps
  again. The container is called database, which comes from our docker-compose.yml file. So we can change the previous command to:

    docker-compose exec database psql --username symfony --password app
  This time, we're executing the psql command inside the container, so we don't need to install it locally. Type ChangeMe for the password and... we're back in!

  The point is: just by running docker-compose up, we have a Postgres database container that we can talk to!

  Stopping the Container
  - Btw, when you're ready to stop the container later, you can run:

    docker-compose stop
  That basically turns the container off. Or you can run the more common:

    docker-compose down
  which turns off the containers and removes them. To start back up, it's the same:

    docker-compose up -d
  But notice that when we run docker-compose ps again, the port on my host machine is a different random port! So, in theory, we could configure the DATABASE_URL variable to point to our Postgres database, including using the correct port. But that random port that keeps changing is going to be annoying!

  Fortunately, there's a trick for this! It turns our, our app is already configured, without us doing anything! That's next.

---
## [david-rowley/postgres](https://github.com/david-rowley/postgres)@[1c27d16e6e...](https://github.com/david-rowley/postgres/commit/1c27d16e6e5c1f463bbe1e9ece88dda811235165)
#### Wednesday 2022-10-12 09:21:53 by Tom Lane

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
## [petre-symfony/symfony-6-and-the-database](https://github.com/petre-symfony/symfony-6-and-the-database)@[b4bf6dfa8a...](https://github.com/petre-symfony/symfony-6-and-the-database/commit/b4bf6dfa8a7280ddb1a8cbcc01247e0dbb95ac16)
#### Wednesday 2022-10-12 09:48:21 by petrero

5. Entity Class

  One of the coolest, but maybe most surprising things about Doctrine, is that it wants you to pretend like the database doesn't exist! Yea, instead of thinking about tables and columns, Doctrine wants us to think about objects and properties.

  For example, let's say that we want to save some product data. The way we do that with Doctrine is by creating a Product class with properties that hold the data. Then you instantiate a Product object, set data onto it and politely ask Doctrine to save it for you. We don't have to worry about how Doctrine does that.

  But, of course, behind the scenes Doctrine is talking to a database. It will INSERT the data from the Product object into a product table where each property is mapped to a column. This is called an Object Relational Mapper, or ORM.

  Later, when we want to get that data back, we don't think about "querying" that table and its columns. Nope, we simply ask Doctrine to find the object that we had earlier. Of course, it will query the table... then recreate the object with the data. But that's not a detail we think about: we ask for the Product object, and it gives it to us. Doctrine handles all of the saving and querying automatically.

  Generating the Entity with make:entity
  - Anyways, when we use an ORM like Doctrine, if we want to save something to the database, we need to create a class that models the thing we want to save, like a Product class. In Doctrine, these classes are given a special name: entities. Though, they're really just normal PHP classes. And while you can create these entity classes by hand, there's a MakerBundle command that makes life much nicer.

  Spin over to your terminal and run:

    php bin/console make:entity
  In this case, we don't have to run symfony console make:entity because this command will not talk to the database: it just generates code. But, if you're ever not sure, using symfony console is always safe.

  Okay, we want to create a class to store all of the vinyl mixes in our system. So let's create a new class called VinylMix. Then answer no for broadcasting entity updates: that's an extra feature related to Symfony Turbo.

  Ok, here's the important part: it asks which properties we want. We're going to add several. Start with one called title. Next it asks which type this field is. Hit ? to see the full list.

  These are Doctrine types... and each one will map to a different column type in your database, depending on which database you're using, like MySQL or Postgres. The basic types are on top like string, text - which can hold more than a string) - boolean, integer and float. Then relationship fields - we'll talk about those in the next tutorial - some special fields, like storing JSON and date fields.

  For title, use string, which can hold up to 255 characters. I'll keep the default length... then it asks us if the field can be null in the database. I'll answer no. This means that the column cannot be null. In other words, the column will be required in the database.

  And... one field done! Let's add a few more. We need a description, and make this a text type. string maxes out at 255 characters, text can hold a ton more. This time, I'll say yes to making it nullable. So this will be an optional column in the database. Another one down!

  For the next property, call it trackCount. It will be an integer and will be not null. Then add genre, as a string, length 255... and also not null so that it's required in the database.

  Finally, add a createdAt field so we can know when each vinyl mix was originally created. This time, because the field name ends in "At", the command suggests a datetime_immutable type. Hit "enter" to use that, and also make this not null in the database.

  We don't need to add any more properties right now so hit "enter" one more time to exit the command.

  Done! What did this do? Well first, I can tell you that this did not talk to or change our database at all. Nope, it simply generated two classes. The first is src/Entity/VinylMix.php. The second is src/Repository/VinylMixRepository.php. Ignore the Repository one for now... we'll talk about its purpose in a few minutes.

  Checking out the Entity Class & Attributes
  - Go open up the VinylMix.php entity. Say hello to... a... wow, pretty normal, boring PHP class! It generated a private property for each field we added, plus an extra id property. The command also added a getter and setter method for each of these. So... this is basically just a class that holds data... and we can access and set that data via the getter and setter methods

  The only thing that makes this class special are the attributes. The ORM\Entity above the class tells Doctrine:

    Hey! I want to be able to save objects of this class to the database. This is an entity.

  Then, above each property, we use ORM\Column to tell Doctrine that we want to save this property as a column in the table. This also communicates other options like the length of the column and whether or not it should be nullable. nullable: false is the default... so the command only generated nullable: true on the one property that needs it.

  The other thing ORM\Column controls is the field type. That's set via this type option. As I mentioned, this doesn't refer directly to a MySQL or Postgres type... its a Doctrine type that will then map to something specific based on our database.

  Field Type Guessing
  - But, interesting: the type option only shows up on the  field. The reason for that is really cool... and new! Doctrine is smart. It looks at the type on your property and guesses the field type from that. So when you have a string property type, Doctrine assumes that you want that to be its string type. You could write Types::STRING inside ORM\Column... but that would be totally redundant.

  We do need it for the description field, however... because we want to use the TEXT type, not the STRING type. But in every other situation, it works. Doctrine guesses the correct type from the ?int property type... and the same thing happens down here for the ?\DateTimeImmutable type.

  Table and Column Naming
  - In addition to controlling things about each column, we can also control the name of the table by adding an ORM\Table above the class with name set to, for example, vinyl_mix. But, surprise! We don't need to do that! Why? Because Doctrine is really good at generating great names. It generates the table name by transforming the class into snake case. So even without ORM\Table, this will be the name of the table. The same applies to properties. $trackCount will map to a track_count column. Doctrine handles all of this for us: we don't need to think about our table or column names at all.

  At this point, we've run make:entity and it generated an entity class for us. Yay! But... we don't actually have a vinyl_mix table in our database yet. How do we create one? With the magic of database migrations. That's next.

---
## [petre-symfony/symfony-6-and-the-database](https://github.com/petre-symfony/symfony-6-and-the-database)@[93c947e7c7...](https://github.com/petre-symfony/symfony-6-and-the-database/commit/93c947e7c77525136794600c6f8bf977deb44fbd)
#### Wednesday 2022-10-12 09:48:21 by petrero

4. The "symfony console" Command & server_version

  Doctrine is now configured to talk to our database, which lives inside a Docker container. That's thanks to the fact that the Symfony dev server exposes this DATABASE_URL environment variable, which points to the container. For me, the container is accessible on port 50739.

  Now let's make sure the actual database has been created. But first, in index.php, remove the dd()... then close that file.

  Spin over to your terminal and run:

    php bin/console
  This prints every bin/console command that's available including a bunch of new ones that start with the word doctrine. Ooh. Most of these aren't very important and we'll walk through the ones that are along the way.

    bin/console doctrine:database:create
  For example, one is called doctrine:database:create. Cool, let's try it:

    php bin/console doctrine:database:create
  And... error! Look closely: it's trying to connect to port 5432. But our environment variable is pointing to port 50739! It's as if it's using the DATABASE_URL value from our .env file instead of the real one that's set by the Symfony binary.

  And, in fact, that's exactly what's happening. And, it makes sense! When we refresh the page in our browser, that's processed through the symfony binary, which gives it the opportunity to add the environment variable.

  But when we run a bin/console command - where console is just a PHP file that lives in a bin/ directory, the symfony binary is never used as part of that process. This means it never has the opportunity to add the environment variable. And so, Symfony falls back to using the value from .env.

  To fix this, whenever we run a bin/console command that needs the Docker environment variables, instead of running bin/console, run symfony console:

    symfony console doctrine:database:create
  That's literally a shortcut to running bin/console: it's no different. But the fact that we're executing it through the symfony binary gives it the opportunity to add the environment variables.

  When we try this... yes! We do get an error because apparently the database already exists, but it did successfully connect and talk to the database.

  Configuring the server_version
  - Ok, there's one last bit of configuration that we need to set. Open config/packages/doctrine.yaml. This file came from the recipe. Find server_version and un-comment it.

  This value "13" is referring to the version of my database engine. Since I'm using Postgres version 14, I need 14 here. If you're using MySQL, you might need 8 or 5.7.

  This helps Doctrine determine which features your database does or doesn't support... since a newer version of a database might support features that an older version doesn't. It's not a particularly interesting piece of configuration, we just need to make sure it's set.

  Ok team: all the boring setup is done. Next: let's create our first entity class! Entities are the most foundational concept in Doctrine and the key to talking to our first database table.

---
## [freebsd/freebsd-ports](https://github.com/freebsd/freebsd-ports)@[2729cb84b7...](https://github.com/freebsd/freebsd-ports/commit/2729cb84b7af5d19933d8609d6a1a69ba119d521)
#### Wednesday 2022-10-12 10:20:08 by Piotr Kubaj

emulators/mgba: update to 0.10.0

Features:
 - Preliminary Lua scripting support
 - Presets for Game Boy palettes
 - Add Super Game Boy palettes for original Game Boy games
 - Tool for converting scanned pictures of e-Reader cards to raw dotcode data
 - Options for muting when inactive, minimized, or for different players in multiplayer
 - Cheat code support in homebrew ports
 - Acclerometer and gyro support for controllers on PC
 - Support for combo "Super Game Boy Color" SGB + GBC ROM hacks
 - Improved support for HuC-3 mapper, including RTC
 - Support for 64 kiB SRAM saves used in some bootlegs
 - Discord Rich Presence now supports time elapsed
 - Additional scaling shaders
 - Support for GameShark Advance SP (.gsv) save file importing
 - Support for multiple saves per game using .sa2, .sa3, etc.
 - Support for GBX format Game Boy ROMs
 - New unlicensed GB mappers: NT (newer type), Sachen (MMC1, MMC2)
Emulation fixes:
 - ARM7: Fix unsigned multiply timing
 - GB: Copy logo from ROM if not running the BIOS intro (fixes mgba.io/i/2378)
 - GB: Fix HALT breaking M-cycle alignment (fixes mgba.io/i/250)
 - GB Audio: Fix channel 1/2 reseting edge cases (fixes mgba.io/i/1925)
 - GB Audio: Properly apply per-model audio differences
 - GB Audio: Revamp channel rendering
 - GB Audio: Fix APU re-enable timing glitch
 - GB I/O: Fix writing to WAVE RAM behavior (fixes mgba.io/i/1334)
 - GB MBC: Fix edge case with Pocket Cam register accesses (fixes mgba.io/i/2557)
 - GB Memory: Add cursory cartridge open bus emulation (fixes mgba.io/i/2032)
 - GB Serialize: Fix loading MBC1 states that affect bank 0 (fixes mgba.io/i/2402)
 - GB SIO: Fix bidirectional transfer starting (fixes mgba.io/i/2290)
 - GB Video: Draw SGB border pieces that overlap GB graphics (fixes mgba.io/i/1339)
 - GBA: Improve timing when not booting from BIOS
 - GBA: Fix expected entry point for multiboot ELFs (fixes mgba.io/i/2450)
 - GBA: Fix booting multiboot ROMs with no JOY entrypoint
 - GBA: Fix 1 MiB ROM mirroring to only mirror 4 times
 - GBA Audio: Adjust PSG sampling rate with SOUNDBIAS
 - GBA Audio: Sample FIFOs at SOUNDBIAS-set frequency
 - GBA BIOS: Work around IRQ handling hiccup in Mario & Luigi (fixes mgba.io/i/1059)
 - GBA BIOS: Initial HLE timing estimation of UnLz77 functions (fixes mgba.io/i/2141)
 - GBA DMA: Fix DMA source direction bits being cleared (fixes mgba.io/i/2410)
 - GBA I/O: Redo internal key input, enabling edge-based key IRQs
 - GBA I/O: Disable open bus behavior on invalid register 06A
 - GBA Memory: Fix misaligned 32-bit I/O loads (fixes mgba.io/i/2307)
 - GBA Video: Fix OpenGL rendering on M1 Macs
 - GBA Video: Ignore horizontally off-screen sprite timing (fixes mgba.io/i/2391)
 - GBA Video: Fix Hblank timing (fixes mgba.io/i/2131, mgba.io/i/2310)
 - GBA Video: Fix rare crash in modes 3-5
 - GBA Video: Fix sprites with mid-frame palette changes in GL (fixes mgba.io/i/2476)
 - GBA Video: Fix OBJ tile wrapping with 2D char mapping (fixes mgba.io/i/2443)
 - GBA Video: Fix horizontal lines in GL when charbase is changed (fixes mgba.io/i/1631)
 - GBA Video: Fix sprite layer priority updating in GL
Other fixes:
 - ARM: Disassemble Thumb mov pseudo-instruction properly
 - ARM: Disassemble ARM asr/lsr #32 properly
 - ARM: Disassemble ARM movs properly
 - Core: Don't attempt to restore rewind diffs past start of rewind
 - Core: Fix the runloop resuming after a game has crashed (fixes mgba.io/i/2451)
 - Core: Fix crash if library can't be opened
 - Debugger: Fix crash with extremely long CLI strings
 - Debugger: Fix multiple conditional watchpoints at the same address
 - FFmpeg: Fix crash when encoding audio with some containers
 - FFmpeg: Fix GIF recording (fixes mgba.io/i/2393)
 - GB: Fix temporary saves
 - GB: Fix replacing the ROM crashing when accessing ROM base
 - GB: Don't try to map a 0-byte SRAM (fixes mgba.io/i/2668)
 - GB, GBA: Save writeback-pending masked saves on unload (fixes mgba.io/i/2396)
 - mGUI: Fix FPS counter after closing menu
 - Qt: Fix some hangs when using the debugger console
 - Qt: Fix crash when clicking past last tile in viewer
 - Qt: Fix preloading for ROM replacing
 - Qt: Fix screen not displaying on Wayland (fixes mgba.io/i/2190)
 - Qt: Fix crash when selecting 256-color sprite in sprite view
 - Qt: Fix coloration of swatches on styles with distinct frame backgrounds
 - VFS: Failed file mapping should return NULL on POSIX
Misc:
 - Core: Suspend runloop when a core crashes
 - Core: Add wallclock offset RTC type
 - Debugger: Save and restore CLI history
 - Debugger: GDB now works while the game is paused
 - Debugger: Add command to load external symbol file (fixes mgba.io/i/2480)
 - FFmpeg: Support dynamic audio sample rate
 - GB: Support CGB0 boot ROM loading
 - GB Audio: Increase sample rate
 - GB MBC: Filter out MBC errors when cartridge is yanked (fixes mgba.io/i/2488)
 - GB MBC: Partially implement TAMA5 RTC
 - GB Video: Add default SGB border
 - GBA: Automatically skip BIOS if ROM has invalid logo
 - GBA: Refine multiboot detection (fixes mgba.io/i/2192)
 - GBA Cheats: Implement "never" type codes (closes mgba.io/i/915)
 - GBA DMA: Enhanced logging (closes mgba.io/i/2454)
 - GBA Memory: Implement adjustable EWRAM waitstates (closes mgba.io/i/1276)
 - GBA Savedata: Store RTC data in savegames (closes mgba.io/i/240)
 - GBA Video: Implement layer placement for OpenGL renderer (fixes mgba.io/i/1962)
 - GBA Video: Fix highlighting for sprites with mid-frame palette changes
 - mGUI: Add margin to right-aligned menu text (fixes mgba.io/i/871)
 - mGUI: Autosave less frequently when fast-forwarding
 - Qt: Rearrange menus some
 - Qt: Clean up cheats dialog
 - Qt: Only set default controller bindings if loading fails (fixes mgba.io/i/799)
 - Qt: Save converter now supports importing GameShark Advance saves
 - Qt: Save positions of multiplayer windows (closes mgba.io/i/2128)
 - Qt: Add optional frame counter to OSD (closes mgba.io/i/1728)
 - Qt: Add optional emulation-related information on reset (closes mgba.io/i/1780)
 - Qt: Add QOpenGLWidget cross-thread codepath for macOS (fixes mgba.io/i/1754)
 - Qt: Enable -b for Boot BIOS menu option (fixes mgba.io/i/2074)
 - Qt: Add tile range selection to tile viewer (closes mgba.io/i/2455)
 - Qt: Show warning if XQ audio is toggled while loaded (fixes mgba.io/i/2295)
 - Qt: Add e-Card passing to the command line (closes mgba.io/i/2474)
 - Qt: Boot both a multiboot image and ROM with CLI args (closes mgba.io/i/1941)
 - Qt: Improve cheat parsing (fixes mgba.io/i/2297)
 - Qt: Change lossless setting to use WavPack audio
 - Qt: Use FFmpeg to convert additional camera formats, if available
 - Qt: Resume crashed game when loading a save state
 - Qt: Include cheats in bug report
 - SDL: Support exposing an axis directly as the gyro value (closes mgba.io/i/2531)
 - Windows: Attach to console if present
 - VFS: Early return NULL if attempting to map 0 bytes from a file
 - Vita: Add bilinear filtering option (closes mgba.io/i/344)

---
## [Paxilmaniac/tgstation](https://github.com/Paxilmaniac/tgstation)@[23bfdec8f4...](https://github.com/Paxilmaniac/tgstation/commit/23bfdec8f43046f7b54906509e38ed1ad91f5096)
#### Wednesday 2022-10-12 10:41:10 by LemonInTheDark

Multiz Rework: Human Suffering Edition (Contains PLANE CUBE) (#69115)


About The Pull Request

I've reworked multiz. This was done because our current implementation of multiz flattens planes down into just the openspace plane. This breaks any effects we attach to plane masters (including lighting), but it also totally kills the SIDE_MAP map format, which we NEED for wallening (A major 3/4ths resprite of all wall and wall adjacent things, making them more then one tile high. Without sidemap we would be unable to display things both in from of and behind objects on map. Stupid.)

This required MASSIVE changes. Both to all uses of the plane var for reasons I'll discuss later, and to a ton of different systems that interact with rendering.

I'll do my best to keep this compact, but there's only so much I can do. Sorry brother.
Core idea

OK: first thing.
vis_contents as it works now squishes the planes of everything inside it down into the plane of the vis_loc.
This is bad. But how to do better?

It's trivially easy to make copies of our existing plane masters but offset, and relay them to the bottom of the plane above. Not a problem. The issue is how to get the actual atoms on the map to "land" on them properly.

We could use FLOAT_PLANE to offset planes based off how they're being seen, in theory this would allow us to create lens for how objects are viewed.
But that's not a stable thing to do, because properly "landing" a plane on a desired plane master would require taking into account every bit of how it's being seen, would inherently break this effect.

Ok so we need to manually edit planes based off "z layer" (IE: what layer of a z stack are you on).

That's the key conceit of this pr. Implementing the plane cube, and ensuring planes are always offset properly.
Everything else is just gravy.
About the Plane Cube

Each plane master (except ones that opt out) is copied down by some constant value equal to the max absolute change between the first and the last plane.
We do this based off the max z stack size detected by SSmapping. This is also where updates come from, and where all our updating logic will live.

As mentioned, plane masters can choose to opt out of being mirrored down. In this case, anything that interacts with them assuming that they'll be offset will instead just get back the valid plane value. This works for render targets too, since I had to work them into the system as well.

Plane masters can also be temporarily hidden from the client's screen. This is done as an attempt at optimization, and applies to anything used in niche cases, or planes only used if there's a z layer below you.
About Plane Master Groups

BYOND supports having different "maps" on screen at once (IE: groups of items/turfs/etc)
Plane masters cannot cover 2 maps at once, since their location is determined by their screen_loc.
So we need to maintain a mirror of each plane for every map we have open.

This was quite messy, so I've refactored it (and maps too) to be a bit more modular.

Rather then storing a list of plane masters, we store a list of plane master group datums.
Each datum is in charge of the plane masters for its particular map, both creating them, and managing them.

Like I mentioned, I also refactored map views. Adding a new mapview is now as simple as newing a /atom/movable/screen/map_view, calling generate_view with the appropriate map id, setting things you want to display in its vis_contents, and then calling display_to on it, passing in the mob to show ourselves to.

Much better then the hardcoded pattern we used to use. So much duplicated code man.

Oh and plane master controllers, that system we have that allows for applying filters to sets of plane masters? I've made it use lookups on plane master groups now, rather then hanging references to all impacted planes. This makes logic easier, and prevents the need to manage references and update the controllers.

image

In addition, I've added a debug ui for plane masters.
It allows you to view all of your own plane masters and short descriptions of what they do, alongside tools for editing them and their relays.

It ALSO supports editing someone elses plane masters, AND it supports (in a very fragile and incomplete manner) viewing literally through someone else's eyes, including their plane masters. This is very useful, because it means you can debug "hey my X is yorked" issues yourself, on live.

In order to accomplish this I have needed to add setters for an ungodly amount of visual impacting vars. Sight flags, eye, see_invis, see_in_dark, etc.

It also comes with an info dump about the ui, and plane masters/relays in general.

Sort of on that note. I've documented everything I know that's niche/useful about our visual effects and rendering system. My hope is this will serve to bring people up to speed on what can be done more quickly, alongside making my sin here less horrible.
See https://github.com/LemonInTheDark/tgstation/blob/multiz-hell/.github/guides/VISUALS.md.
"Landing" planes

Ok so I've explained the backend, but how do we actually land planes properly?
Most of the time this is really simple. When a plane var is set, we need to provide some spokesperson for the appearance's z level. We can use this to derive their z layer, and thus what offset to use.

This is just a lot of gruntwork, but it's occasionally more complex.
Sometimes we need to cache a list of z layer -> effect, and then use that.
Also a LOT of updating on z move. So much z move shit.

Oh. and in order to make byond darkness work properly, I needed to add SEE_BLACKNESS to all sight flags.
This draws darkness to plane 0, which means I'm able to relay it around and draw it on different z layers as is possible. fun darkness ripple effects incoming someday

I also need to update mob overlays on move.
I do this by realiizing their appearances, mutating their plane, and then readding the overlay in the correct order.

The cost of this is currently 3N. I'm convinced this could be improved, but I've not got to it yet.
It can also occasionally cause overlays to corrupt. This is fixed by laying a protective ward of overlays.Copy in the sand, but that spell makes the compiler confused, so I'll have to bully lummy about fixing it at some point.
Behavior changes

We've had to give up on the already broken gateway "see through" effect. Won't work without managing gateway plane masters or something stupid. Not worth it.
So instead we display the other side as a ui element. It's worse, but not that bad.

Because vis_contents no longer flattens planes (most of the time), some uses of it now have interesting behavior.
The main thing that comes to mind is alert popups that display mobs. They can impact the lighting plane.
I don't really care, but it should be fixable, I think, given elbow grease.

Ah and I've cleaned up layers and plane defines to make them a bit easier to read/reason about, at least I think.
Why It's Good For The Game
<visual candy>

Fixes #65800
Fixes #68461
Changelog

cl
refactor: Refactored... well a lot really. Map views, anything to do with planes, multiz, a shit ton of rendering stuff. Basically if you see anything off visually report it
admin: VV a mob, and hit View/Edit Planes in the dropdown to steal their view, and modify it as you like. You can do the same to yourself using the Edit/Debug Planes verb
/cl

---
## [Paxilmaniac/tgstation](https://github.com/Paxilmaniac/tgstation)@[1810b85553...](https://github.com/Paxilmaniac/tgstation/commit/1810b855536f05891593b1379e455164f45fab3a)
#### Wednesday 2022-10-12 10:41:10 by tralezab

Heretics cannot be converted, and are immune to cult stun hands. Instead, the cult is rewarded for sacrificing them with the bloody bastard sword, an oversized SPIN2WIN funblade. + Soul Stealing Fantasy Affix (#69725)

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

---
## [Paxilmaniac/tgstation](https://github.com/Paxilmaniac/tgstation)@[cee07f804c...](https://github.com/Paxilmaniac/tgstation/commit/cee07f804cc1df6d9cb0ff783ad4504458cf2c8b)
#### Wednesday 2022-10-12 10:41:10 by LemonInTheDark

Airlock open delay audit (#69905)


About The Pull Request

A: Mineral doors no longer take 6 SECONDS to open if you bump anything beforehand. Holy shit why would you do this.
B: Airlocks no longer require you to have not bumped anything in a second, lowered to 0.3 seconds. This is safe because I've moved shock immunity to its own logic. This should make opening doors feel less horrible
Why It's Good For The Game

Feels better.
Changelog

cl
balance: Airlocks will open on bump in series much faster now. As a tradeoff, you're immune to shocks from them for a second after you last got shocked by one.
fix: Mineral doors will no longer take 6 WHOLE SECONDS to open if you've bumped something else recently
/cl

---
## [royrustdev/rust-clippy](https://github.com/royrustdev/rust-clippy)@[9e8f53d09a...](https://github.com/royrustdev/rust-clippy/commit/9e8f53d09af61d38d6de42450dbf6910982d3ea9)
#### Wednesday 2022-10-12 10:41:10 by bors

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
## [newmail01922/2end](https://github.com/newmail01922/2end)@[4fe701e9f8...](https://github.com/newmail01922/2end/commit/4fe701e9f87006eb5d50c1f991a8e044c956b3e0)
#### Wednesday 2022-10-12 11:23:25 by newmail01922

done2.pmi

okserd Inspirational Quotes About Life
Keep smiling, because life is a beautiful thing and there's so much to smile about. - ...
Life is a long lesson in humility. - ...
In three words I can sum up everything I've learned about life: it goes on. - ...
Love the life you live. ...
Life is either a daring adventure or nothing at all. -

---
## [BlackCatMS/Luniks](https://github.com/BlackCatMS/Luniks)@[d6d6c4582e...](https://github.com/BlackCatMS/Luniks/commit/d6d6c4582e2da32a3f14f02939732a46156a1b6b)
#### Wednesday 2022-10-12 11:37:56 by Josie

README.md updated 

Shit sounds like a movie trailer I fucking love it

---
## [aslenofarid/kernel_asus_sdm660](https://github.com/aslenofarid/kernel_asus_sdm660)@[44840cddf5...](https://github.com/aslenofarid/kernel_asus_sdm660/commit/44840cddf5a912bfab4467d1cffaf271c6be9ddd)
#### Wednesday 2022-10-12 11:45:24 by George Spelvin

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
Signed-off-by: Dede Dindin Qudsy <xtrymind@gmail.com>
Signed-off-by: aslenofarid <yoniasleno.farid14@gmail.com>

---
## [CaptainKlutz/CivDocker](https://github.com/CaptainKlutz/CivDocker)@[7fdbe7c6d9...](https://github.com/CaptainKlutz/CivDocker/commit/7fdbe7c6d9d1e9ca8b73aec517daf0300588acdd)
#### Wednesday 2022-10-12 11:49:31 by CaptainKlutz

Lengthen all reinforcement maturation times

Reinforcement times across the board are far too short.

It is completely nonsensical that structures built can rival the strength of buildings that have stood for months after just 5 minutes or an hour. It sucks the fun out of civ knowing you have mere seconds to log in and remove stone-reinforced grief before having to use acid blocks instead. It is completely counterproductive for those with lives outside of civ to always be an hour away from being totally invalidated. The stale vault meta is only bolstered by the fact that vault spikes are risk-free and diamond reinforced expansions can be erected overnight.

A lot of people are scared of big maturation numbers but forget they don't represent 'time until viable'. Just a few seconds after SRO is placed, it doubles in strength. The time it takes to mine it then allows it to mature further. Pardon my French, but it is absolutely FUCKED that you can be mining a block and the amount of breaks it will take to destroy it is INCREASING while you're ACTIVELY BREAKING IT.

"but my skybridging": what do you want to be more important, the skybridge or the people fighting in it?

"but my build might be broken overnight": just 15 minutes after you place a stone reinforced block, it will already take 16 hits to break. unless you're building in a warzone, you're going to be fine.

"but my acids will take longer": maybe now it will be actually viable to break blocks still maturing instead of giving up and going straight for acid.

"but my bunker pvp": I've seen bunker pvp on this iteration and it's fair to say I think the vast majority of people hate the stone reinforced obby/trapdoors/doors/buttons spam meta.

"but it will encourage camping to abuse when reinforcements are maturing": but this ALREADY HAPPENS, just the other way around. Players literally wait for people to be offline to spam reinforcements before they log on again. Turning this around to favour the breaker's side is more healthy.

"but now obbybombing is less viable": good.

---
## [kavishinsa/Purva-Orient-Grand-Lal-Bagh-Bangalore](https://github.com/kavishinsa/Purva-Orient-Grand-Lal-Bagh-Bangalore)@[a7373224c0...](https://github.com/kavishinsa/Purva-Orient-Grand-Lal-Bagh-Bangalore/commit/a7373224c01f9532cb7ef8ffb2d943dec73cf06f)
#### Wednesday 2022-10-12 11:56:03 by kavishinsa

Purva Orient Grand Lal Bagh – New Apartments For Sale In Bangalore

Discover your new home at Purva Group today! Purva Orient Grand is situated across a large stretch of land, spanning over a large area and set against the beautiful backdrop of the beautiful city of Bengaluru. Choose your ideal home here - choose an accommodating flat designed for couples starting out or those without children, or opt for a flat that offers more space so you can grow into it as your family increases. With the beauty of the city neighboring, you waiting for you to discover, there is no better place than here. 

They provide communities so beautiful you'll never want to leave! Purva Orient Grand Lalbagh offers homes for all existences, from contemporary to modern; from cozy flats for families and more than just residences: world-class schools, shopping malls, hotels, theme parks, and business districts - every existence catered for.

Luxury living awaits you in Purva Orient Grand Bengaluru - an elite gated community where you will feel at abode. Whether you want a breathtaking view of the sparkling city night and live in peace, it has all your needs enclosed. Now when you drive through this project, you can take in all its beauty. You'll always know where you're going in this project because it's found clearly on the main highway. Plus, there are amazing retail shops on each side of the main road, so even if you're not home, there's always something for you to enjoy in our town! Wide, majestic pathways welcome you to this new community designed to give you the whole thing you could ever ask for!

Lalbagh Road, Bengaluru locality is a posh residential and commercial locality near the Lalbagh Main Road in Bengaluru, The capital town of Karnataka. You've probably seen pictures of the lush green area, but did you know the Lalbagh Botanical Garden also has a thrilling list of things to do? That's right! Boating and swimming in the lake, exploring the bird observatory, and touring the gardens are just some of the activities that are obtainable to you here.

For More Details:
Visit Here: https://bit.ly/3et2IhW

---
## [newstools/2022-metro](https://github.com/newstools/2022-metro)@[f5b30fa5ea...](https://github.com/newstools/2022-metro/commit/f5b30fa5ea1ccbce514e18ca370424b0fbf4cddd)
#### Wednesday 2022-10-12 12:31:52 by Billy Einkamerer

Created Text For URL [metro.co.uk/2022/10/11/man-set-fire-to-girlfriend-in-reservoir-dogs-fantasy-killing-her-21-years-later-17546490/]

---
## [containers/buildah](https://github.com/containers/buildah)@[2adbe2a58a...](https://github.com/containers/buildah/commit/2adbe2a58a77b014be59c68abf58b682ad5e5c20)
#### Wednesday 2022-10-12 12:49:06 by Ed Santiago

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
## [CommE2E/comm](https://github.com/CommE2E/comm)@[8875f4fd7f...](https://github.com/CommE2E/comm/commit/8875f4fd7f97e0399bb0809d1775f77fdeb1c41f)
#### Wednesday 2022-10-12 12:59:30 by Ashoat Tevosyan

[keyserver] Go back to using window function for getMessageInfos

Summary:
The window function is a much more modern and civilized approach to this query.

I first introduced this in D4675, but then reverted it in D4796 because it caused [ENG-957](https://linear.app/comm/issue/ENG-957/mobile-startreached-issue).

However, once I found that the window function approach solved [ENG-2009](https://linear.app/comm/issue/ENG-2009/messages-missing-in-ashoatmarks-chat-history), I spent a second thinking about how to change the window function to avoid the issue from ENG-957. The easy solution is just to move the `LEFT JOIN uploads` line to the outer query.

In addition, I noticed the window function also needed an `ORDER BY`, as it was exhibiting the same out-of-order weirdness that caused ENG-2009. Although it wasn't affecting the partition function, our JS code for parsing the results expects that they appear in a specific order.

Test Plan:
I tried to test this thoroughly given previous experiences.

- I manually composed a query that reproduces the current issue (ENG-2009)
- I edited it for the window function approach and saw that the issue was resolved
- I manually composed a query that reproduces the old issue (ENG-957)
- I edited it for the window function approach and saw that the old issue did not reappear
- I patched my production keyserver live after midnight ET to confirm that the missing content now appears
- I also live-tested to make sure the old issue was resolved by checking a chat that recently had a message with three images

Reviewers: tomek, atul

Reviewed By: tomek

Subscribers: abosh

Differential Revision: https://phab.comm.dev/D5349

---
## [demogorgon22/notdnethack](https://github.com/demogorgon22/notdnethack)@[f260cde5a4...](https://github.com/demogorgon22/notdnethack/commit/f260cde5a426d936bca18ebbc6a22ee051cbd96d)
#### Wednesday 2022-10-12 13:19:11 by chris

Monster healing fixes

Make one mhp > mhpmax check at end
-Fixes overhealing bug

Re-order mspec cooldown and digestion to start instead of end
-Fixes a bug where Lomya wouldn't get counted in degeneration cases.
-Reduces redundancy in special cases
-Does mean that if a monster dies from degeneration its cooldowns will still have ticked. This seems fine to me.

Switch some cases of == 0 to <= 0
-I don't think this could cause a bug, but better safe than sorry.

Re-order cases so that it goes magic healing->damaging effects->degeneration->natural effects.
-Degeneration was blocking Lolth's clouds and Cthulhu's mind blasts.
-Degeneration is defined as blocking natural healing
--Only one Degen case will take effect, due to early returns. Perhaps this should be considered a bug?

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[1af2c12e05...](https://github.com/TaleStation/TaleStation/commit/1af2c12e0501c2cf5eb5946738360564fd78cea4)
#### Wednesday 2022-10-12 13:47:35 by TaleStationBot

[MIRROR] [MDB IGNORE] canUseTopic now uses TRUE/FALSE instead of defines that just say TRUE (#2676)

* canUseTopic now uses TRUE/FALSE instead of defines that just say TRUE (#69790)

* canUseTopic now uses TRUE/FALSE instead of defines that just say TRUE

The most idiotic thing I've seen is canUseTopic's defines, they literally just define TRUE, you can use it however you want, it doesn't matter, it just means TRUE. You can mix and match the args and it will set that arg to true, despite the name.

It's so idiotic I decided to remove it, so now I can reclaim a little bit of my sanity.

* canUseTopic now uses TRUE/FALSE instead of defines that just say TRUE

* fix

Co-authored-by: John Willard <53777086+JohnFulpWillard@users.noreply.github.com>

---
## [timothymtorres/tgstation](https://github.com/timothymtorres/tgstation)@[bc90ded5b8...](https://github.com/timothymtorres/tgstation/commit/bc90ded5b8b0f4487ccec227fed24f514dbaa5ba)
#### Wednesday 2022-10-12 14:19:42 by MrMelbert

Buffs Heretic Curses, Living Heart, Leeching Walk, and technically Entropic Plume by fixing some bugs (#69181)

About The Pull Request

    Heretic curses have been buffed / reworked.
        Curses can be cast on any crewmember, not just those who you have fingerprints to.
        Having an item present in the ritual that contains fingerprints OR blood dna of a crewmember who you are cursing will boost the curse, causing it to last longer (and be stronger? Still undecided, but there's support for it)
        Curses have a max range (64 by default) and don't work on people on a different z-level (Do not BTFO miners so easily)
        Corrosion curse's numbers have been tweaked due to this, and it can no longer cause vital organ failure

    Living Heart has been buffed
        Cooldown cut in half, and it provides a bit more thorough instructions
        Closes 

    Living heart targets who are located in non-turf locs and are off z-level will show as on the same z #67256

Leeching Walk has been buffed

    Rust will also restore lost blood.

Technically buffs Entropic Plume by fixing some bugs

    "Cloudstruck" has always meant to blind, but they used the wrong method, so I fixed that.
    Also it was meant to inject multiple units of poison, but used "min" instead of "max" so it always did the lowest.
    I also fixed the stink cloud lasting forever on people.
    Amok also makes people holding guns to shoot people further away.

Closes

    Admin healing removes heretic living heart #69167 while I'm here

Why It's Good For The Game

    Heretic curses have pretty much always been bad, getting fingerprints is damn near impossible considering everyone uses gloves. Not only that but their requirements were very high. This should hopefully bring curses to the limelight, as they can be applied to any potential targets. It also rewards heretics who go out of their way to collect fingerprints and blood samples with even stronger curses.

    The Living Heart was often hard to pinpoint people exactly, partially cause of an oversight. I improved the text to be clearer about potential locations of your targets.

    Leeching Walk's healing was nice, but blood wounds were still a major threat. Some blood restoration should help.

    Entropic Plume I think has never worked correctly, so that was a bummer. Fixes that.

Changelog

cl Melbert
balance: Heretic: Curses have been reworked. You can now curse any member of the crew, granted they're not too far away. If you additionally provide an item in the ritual containing a sample of the target's blood or fingerprints, the curse's duration will be increased and have its range uncapped.
balance: Heretic: The Curse of Corrosion has been nerfed slightly due to this rework, and can no longer cause vital organs to fail.
balance: Heretic: The Living Heart should now provide better directions, and had its cooldown halved to 4 seconds.
balance: Heretic: Leeching Walk (rust healing) now restores lost blood.
balance: Heretic: If you apply Amok (Entropic Plume) to someone holding a gun, they'll try to shoot it at people nearby.
fix: Entropic Plume's effect now blinds, as it should.
fix: Entropic Plume no longer sometimes applies the stink effect forever.
fix: Entropic Plume no longer always applies the lowest amount of poison, and properly scales on distance.
fix: Fixed an exploit which allowed people to figure out if a Heretic's heart was a previously a Living Heart after being removed.
fix: If a heretic is fully healed by something (such as ahealed), they'll not lose their living heart
/cl

---
## [timothymtorres/tgstation](https://github.com/timothymtorres/tgstation)@[de04b3be80...](https://github.com/timothymtorres/tgstation/commit/de04b3be8082e37e4ff22b74b8f3feb6f38d03eb)
#### Wednesday 2022-10-12 14:19:42 by MrMelbert

Kills `/obj/shapeshift_holder`, replaces it with `/datum/status_effect/shapechange_mob`, also does a lot of Wabbajack refactoring (#69091)


About The Pull Request

    Deletes /obj/shapeshift_holder, replaces it with /datum/status_effect/shapechange_mob
    Refactors Heretic worm form into a shapeshift spell
    Refactors Wabbajack, and associated code

Fixes #69117
Fixes #65653
Fixes #59127
Fixes #52786
Why It's Good For The Game

/obj/shapeshift_holder was one of the worst remaining abuses of /obj direct subtypes, so I replaced it with a cool fancy datum.

This also decouples the shapeshifting behavior entirely from the shapeshifting spell. So we have support for shapeshifted mobs not sourced from a spell. Which is neat, we could technically swap Wabbajack to use this in the future.
Changelog

cl Melbert
fix: Wabbajacking a shapeshifted mob no longer runtimes horribly. When a shapeshifted mob is wabbajacked, they'll now be removed from their shapeshift and stunned.
fix: Transforming via a shapeshift should no longer rob you of your hearing / runechat awareness.
fix: Shapeshifting plays nicer with holoparasites.
fix: Being polymorphed from a xeno to a non-xeno correctly makes you a non-xeno
refactor: Refactored shapeshifting, the shapeshift holder is now a status effect instead of an object.
refactor: Heretic worm form is a shapeshift spell now, this might have some minor behavioral changes but should overall be the same.
refactor: Refactored Wabbajack (+ cursed pool). Overall a bit more clean / consistent behavior.
/cl

---
## [mayurrai/DSA-MR](https://github.com/mayurrai/DSA-MR)@[d1731aac17...](https://github.com/mayurrai/DSA-MR/commit/d1731aac179b44485e1ee5b30861f7c58fcbc43d)
#### Wednesday 2022-10-12 14:45:55 by Mayur Rai

STACK_APPLICATION_2_26121

Krishna has shown one magic to reverse the given string. He asked his friend that can you write a code to check the given string is palindrome or not.

Sample 1: Line 1: Enter the string : amma Line 2: Palindrome

Sample 1: Line 1 : Enter the expression : papa Line 2 : Not Palindrome

Input Format

User should pass the input in formate of string

Constraints

String expression length should > 0

Output Format

The result will display as Palindrome or Not Palindrome.

Sample Input 0

malayalam
Sample Output 0

Palindrome 
Explanation 0

Line 1 : Enter the expression : malayalam Line 2 : Palindrome

---
## [GouravDutta-01/anime-for-dev](https://github.com/GouravDutta-01/anime-for-dev)@[d621f8de0f...](https://github.com/GouravDutta-01/anime-for-dev/commit/d621f8de0f4427a22286d034e7fd9b9c43a30148)
#### Wednesday 2022-10-12 14:59:17 by Gourav Dutta

Add Mob Psycho 100

**Title**: Mob Psycho 100
 **Link**: https://myanimelist.net/anime/32182/Mob_Psycho_100

**Why this anime should watched by developer?**

This anime is about a psychic middle school boy who tries to live a normal life and keep his growing powers under control, even though he constantly gets into trouble.As he grows he wants to find his purpose in life and wants to live a happy life.This anime teaches us many values on finding purpose in life and live a happy life.Also this anime has a good sense of humour in it and helps us to relax after completing a busy day.

---
## [australopitek/pytorch](https://github.com/australopitek/pytorch)@[afcc7c7f5c...](https://github.com/australopitek/pytorch/commit/afcc7c7f5c7cef740241ff0abdae8d4f2ad22a03)
#### Wednesday 2022-10-12 15:47:32 by Andrew Gu

[FSDP] Generalize prefetching; lower unshard/reshard to handle (#83665)

### Additional Constructor Changes
- `self.sharding_strategy`
    - If the world size is 1, I clamp the sharding strategy to `NO_SHARD`, regardless of the passed-in sharding strategy, since the behavior is fully equivalent. This absolves the need for `p._is_sharded or self.world_size == 1` checks in the core code. Once we fully shift the paradigm to using handles, this should result in a clear net positive. However, for now, we still have some places where we interface directly with the `FlatParameter`, in which case we have some temporary hacky code.
- `HandleConfig`
    - As a part of the new design abstraction, much logic is lowered to the `FlatParamHandle`. This requires the handle be aware of mixed precision, CPU offloading, sharding strategy, and the process group (for world size > 1). To be less error-prone, I re-defined the `dataclass`s and `enum`s for the handle. These can be removed and coalesced with the existing ones.
    - The drawback is that the `FlattenParamsWrapper` constructor now takes in the `HandleConfig` to forward it to the `FlatParamHandle` constructor. I tolerate this since we plan to retire the FPW. For now, the handle's process group attributes are set later when we call `handle.shard()`.
    - We will dive into this logic lowering later. For now, the idea is we need to pass some extra info to the handle, which must go through the FPW.
- `FullyShardedDataParallel._shard_parameters()` -> `FlatParamHandle.shard()`
- [Important] Generalizing attributes to remove the 1 `FullyShardedDataParallel` : 1 `FlatParameter` assumption
    - **Before:** `_fsdp_graph_order`, `_pre_backward_hook_full_params_prefetched`, `_forward_full_params_prefetched`, `reshard_after_forward` are with respect to 1 `FullyShardedDataParallel`
    - **After:** (1) We use `FlatParamHandle` in place of `FullyShardedDataParallel`. (2) The atomic unit for forward and pre-backward is a _group_ of handles involved in the same module's forward/pre-backward. This is represented as `Tuple[FlatParamHandle, ...]`. For now, this is **always a singleton tuple**, but this shift enables a module having multiple FSDP parameters (which we have use cases for).
- `_reset_lazy_init()` attributes
    - The prefetched flags are merged into `self._handles_prefetched`, which is directly defined in the constructor. `reshard_after_forward` is retired since it can be fully determined by other attributes (`_is_root` and `sharding_strategy`).

## FSDP Runtime: Unshard

The first step is to read the existing `_rebuild_full_params()`. A few notable observations:
- It returns `Tuple[Tensor, bool]`. The first element is the _padded unsharded flattened parameter_, and the second element is whether we can free it upon exiting `summon_full_params()`. This return value is **only used in `summon_full_params()`**.
- If parameter mixed precision is enabled and the `FlatParameter` is already unsharded, then the low precision shard (`_mp_shard`) is still re-allocated on GPU. (It is freed at the end of the method.)
- If CPU offloading is enabled and the `FlatParameter` is already unsharded, then there is a no-op `p.data = p.data.to(self.compute_device, non_blocking=True)`.
- Inside `summon_full_params()`, `mixed_precision_cast_ran` is always `False`. Therefore, the return value for the `not p._is_sharded and mixed_precision_cast_ran` branch is unused.
-`summon_full_params()` can only be called (before forward or after backward) or (between forward and backward). Given this, I cannot think of a case where we call `summon_full_params()`, the `FlatParameter` is already unsharded, but `reshard_after_forward` is `True`. The `FlatParameter` should be sharded (before forward or after backward), and the `FlatParameter` may only be unsharded (between forward and backward) if `reshard_after_forward` is `False`.
- If parameter mixed precision is enabled and the sharding strategy is a sharded one, then inside `summon_full_params()`, the `FlatParameter` is unsharded in full precision. This involves allocating a new padded unsharded flattened parameter on GPU in full precision since `_full_param_padded` is in the low precision.

Some comments:
- Ideally, we reduce the complexity of the core code path: i.e. unshard for forward and pre-backward. If the return value is only used for `summon_full_params()`, we should consider if we can compartmentalize that logic.
- The branching is complex, and some return values are never used, where this fact is not immediately obvious. We should see if we can reduce the branch complexity.

Disclaimer: The difference in attribute semantics between `NO_SHARD` and the sharded strategies makes it challenging to unify the cases. This PR does not attempt to address that since it requires more design thought. However, it does attempt to reduce the complexity for the sharded strategies.

### Unshard: Core Code Path
Let us trace through the new logical unshard.
1. `FullyShardedDataParallel._unshard(self, handles: List[FlatParamHandle], prepare_gradient: bool)`
    - This iterates over the handles and calls `handle.pre_unshard()`, `handle.unshard()`, and `handle.post_unshard(prepare_gradient)` in the all-gather stream.
2. `FlatParamHandle.needs_unshard(self)`
    - We take an aside to look at this key subroutine.
    - For `NO_SHARD`, this returns `False`.
    - For sharded strategies, this checks if the padded unsharded flattened parameter is allocated. The padded unsharded flattened parameter is the base tensor for the unpadded unsharded flattened parameter, which is a view into the padded one. Thus, the padded one's allocation fully determines if the `FlatParameter` is unsharded.
    - For sharded strategies, to accommodate the parameter mixed precision + `summon_full_params()` case, we introduce `_full_prec_full_param_padded`, which is the padded unsharded flattened parameter in full precision. The helper `_get_padded_unsharded_flat_param()` takes care of this casing and returns the padded unsharded flattened parameter. Instead of allocating a new tensor each time, we manually manage `_full_prec_full_param_padded`'s storage just like for `_full_param_padded`.
3. `FlatParamHandle.pre_unshard(self)`
    - For sharded strategies, the postcondition is that the handle's `FlatParameter` points to the tensor to all-gather. This should be on the communication device and in the desired precision. The allocation and usage of the low precision shard for parameter mixed precision and the CPU -> GPU copy for CPU offloading both classify naturally in the pre-unshard.
    - For sharded strategies, if the `FlatParameter` does not need to be unsharded, `pre_unshard()` is a no-op. This avoids unnecessarily allocating and freeing the low precision shard.
    - For `NO_SHARD`, we simply preserve the existing semantics.
4. `FlatParamHandle.unshard(self)`
    - If the handle was resharded without freeing the padded unsharded flattened parameter (e.g. `summon_full_params()` between forward and backward when `reshard_after_forward=False`), then the `FlatParameter` points to the sharded flattened parameter. We need to switch to using the unsharded parameter. This is a design choice. Alternatively, we may not switch to using the sharded flattened parameter in `reshard()` if we do not free the padded unsharded flattened parameter. However, the postcondition that the `FlatParameter` points to the sharded flattened parameter after `reshard()` is helpful logically, so I prefer this approach.
    - Otherwise, this allocates the padded unsharded flattened parameter, all-gathers, and switches to using the unpadded unsharded flattened parameter.
    - In the future, we may add an option to `unshard()` that additionally all-gathers the gradient.
5. `FlatParamHandle.post_unshard(self, prepare_gradient: bool)`
    - For sharded strategies, if using parameter mixed precision, this frees the low precision shard. More generally, this should free any sharded allocations made in `pre_unshard()` since the all-gather has been launched. If using CPU offloading, the GPU copy of the local shard goes out of scope after `unshard()` and is able to be garbage collected. **We should understand if there is any performance difference between manually freeing versus deferring to garbage collection since our usage is inconsistent.** For now, I preserve the existing semantics here.
    - `prepare_gradient` is meant to be set to `True` for the pre-backward unshard and `False` for the forward unshard. This runs the equivalent logic of `_prep_grads_for_backward()`.
    - This post-unshard logic (notably the gradient preparation) now runs in the all-gather stream, which is fine because we always have the current stream wait for the all-gather stream immediately after `FullyShardedDataParallel._unshard()`. IIUC, we do not need to call `_mp_shard.record_stream(current_stream)` (where `current_stream` is the default stream) because `_mp_shard` is allocated and freed in the same (all-gather) stream.
    - A postcondition is that the `FlatParameter` is on the compute device. It should also have the unpadded unsharded size (though I do not have a check for this at the moment).

### Unshard: `summon_full_params()`
Now that we see how the logical unshard has been reorganized for the core code path, let us dive into `summon_full_params()`.

The two constraints are:
1. If using parameter mixed precision, we should unshard in full precision.
2. We must determine if we should free the padded unsharded flattened parameter upon exiting.

The first constraint is addressed as described before in the core unshard code path, so it remains to explore the second constraint.

I propose a simple rule: **We free iff we actually unshard the `FlatParameter` in `summon_full_params()`** (i.e. it was not already unsharded). We perform a case analysis:

**Parameter mixed precision enabled:**
* `NO_SHARD`: `flat_param.data` points to `flat_param._local_shard`, which is the full precision unsharded flattened parameter. This is **not safe to free**.
* `FULL_SHARD` / `SHARD_GRAD_OP`: We force full precision and all-gather to `_full_prec_full_param_padded`. We do not support `nested summon_full_params()`, so `_full_prec_full_param_padded` must be unallocated. We unshard, and it is **safe to free**.

**Parameter mixed precision disabled:**
* `NO_SHARD`: This is the same as with mixed precision enabled. This is **not safe to free**.
* `FULL_SHARD` / `SHARD_GRAD_OP`: We all-gather to `_full_param_padded`. It may already be unsharded.
    * Already unsharded: The unshard is a no-op. This is **not safe to free**.
        * For `FULL_SHARD`, this can happen for the root FSDP instance after `forward()` but before backward.
        * For `SHARD_GRAD_OP`, this can happen for all FSDP instances after `forward()` but before backward.
    * Needs unshard: We unshard. This is **safe to free**.

Therefore, we see that it is not safe to free when using `NO_SHARD` and when using a sharded strategy but the `FlatParameter` is already unsharded. This is precisely the proposed rule.

There were two notable edge cases that the existing code did not address.
1. The existing code tests if the `FlatParameter` is already unsharded by checking the allocation status of `_full_param_padded`. When using parameter mixed precision, this is the incorrect tensor to check. If `_full_param_padded` is allocated (e.g. when `reshard_after_forward=False` and calling `summon_full_params()` between forward and backward), the already-unsharded check is a false positive, and `summon_full_params()` does not correctly force full precision. https://github.com/pytorch/pytorch/issues/83068
    - This PR's `needs_unshard()` check correctly routes to the appropriate padded unsharded flattened parameter depending on the calling context (i.e. if it needs to force full precision or not).
2. The existing code does not free the GPU copy of the padded unsharded flattened parameter when calling `summon_full_params(offload_to_cpu=True)`. It unshards the `FlatParameter`, moves the padded unsharded flattened parameter to CPU, and sets the `FlatParameter` data to be the appropriate unpadded view into the padded unsharded flattened parameter on CPU. However, `_full_param_padded` still points to the all-gathered padded unsharded flattened parameter on GPU, which is kept in memory. https://github.com/pytorch/pytorch/issues/83076
    - This PR frees the GPU copy and reallocates it upon exiting `summon_full_params()`. This is essential for avoiding peak GPU memory usage from increasing as we recurse through the module tree. There may be some cases where we can avoid reallocation altogether, but that can be addressed in a follow-up PR.
    - This PR offloads the *unpadded* unsharded flattened parameter to CPU directly instead of the *padded* one. As far as I can tell, there is no need to include the padding since unflattening the original parameters does not require the padding.
    - The relevant code is in the context manager `FlatParamHandle.to_cpu()`.

### Unshard: Mixed-Precision Stream

This PR removes the mixed precision stream usage. As is, I do not think there is any extra overlap being achieved by the stream usage.

The low precision shard is allocated and copied to in the mixed precision stream ([code](https://github.com/pytorch/pytorch/blob/1f99bdfcc4a3f97d28471a531d2b69def762f6ba/torch/distributed/fsdp/fully_sharded_data_parallel.py#L1401-L1412)), and the current stream (in this case the all-gather stream) waits for the mixed precision stream ([code](https://github.com/pytorch/pytorch/blob/1f99bdfcc4a3f97d28471a531d2b69def762f6ba/torch/distributed/fsdp/fully_sharded_data_parallel.py#L1414)). However, we immediately schedule an all-gather that communicates that exact low precision shard ([code](https://github.com/pytorch/pytorch/blob/1f99bdfcc4a3f97d28471a531d2b69def762f6ba/torch/distributed/fsdp/fully_sharded_data_parallel.py#L3338)) with no other meaningful computation between. If we remove the mixed precision stream, the low precision shard is allocated and copied to in the all-gather stream (including the non-blocking CPU -> GPU copy if using CPU offloading).

Under this PR's design, we may consider a "pre-unshard" stream for all logical pre-unshard data transfers if we want to overlap in the future. IIUC, the overlap opportunity exists if there are multiple `FlatParameter`s per module, and we only have the all-gather stream wait for the data transfer corresponding to the local shard it communicates, not the others.

If we agree on removing the mixed-precision stream for now, I will remember to delete it from `_init_streams()`.

## FSDP Runtime: Reshard

Like with unshard, the first step is the look at the existing `_free_full_params()` and `_use_param_local_shard()`. A few notable observations:
- For only `NO_SHARD`, `_free_full_params()` includes a call to `_free_mp_shard()`.
- For `summon_full_params()`, there is a separate `_free_full_params_and_use_local_shard()` that duplicates the main logic of `_free_full_params()` and calls `_use_param_local_shard()`.
- In `forward()`, if `reshard_after_forward=True`, we call `_free_full_params()` and then `_free_mp_shard()`. Hence, for `NO_SHARD`, the `_free_mp_shard()` is a no-op.
- In the post-backward hook, we typically call `_free_full_params()` and `_free_mp_shard()`. The `_free_mp_shard()` is a no-op for `NO_SHARD` and if `reshard_after_forward=True`.

Some comments:
- The code certainly works, but some of the no-ops are subtle. When possible, we should make it clear when calls are no-ops or not. It is good that the existing code documents that `_free_mp_shard()` is a no-op in the post-backward hook when `reshard_after_forward=True`. However, there are still some non-obvious no-ops (around `NO_SHARD`).
- We should see if we can avoid the duplicate `_free_full_params_and_use_local_shard()`.

Let us trace through the logical reshard:
1. `FullyShardedDataParallel._reshard(self, handles: List[FlatParamHandle], free_unsharded_flat_params: List[bool])`
    - The two args should have the same length since they are to be zipped.
    - The goal of having `free_unsharded_flat_params` is that the caller should be explicit about whether the (padded) unsharded flattened parameter should be freed. The low precision shard is always meant to be freed (as early as possible), so there is no corresponding `List[bool]`.
2. `FlatParamHandle.reshard(self, free_unsharded_flat_param: bool)`
    - This frees the (padded) unsharded flattened parameter if `free_unsharded_flat_param` and switches to using the sharded flattened parameter.
    - Echoing back to forcing full precision in `summon_full_params()`, `_free_unsharded_flat_param()` frees the correct tensor by using `_get_padded_unsharded_flat_parameter()`.
3. `FlatParamHandle.post_reshard(self)`
    - I am not fully content with the existence of this method, but this seems to be an unavoidable consequence of `NO_SHARD`. Perhaps, this may be useful in the future for other reasons though.
    - Right now, this method is only meaningful for `NO_SHARD` + parameter mixed precision + outside `summon_full_params()`. `_mp_shard` is not freed in the post-unshard since it is also the low precision _unsharded_ flattened parameter, so we must delay the free until the the post-reshard.

Below the `FlatParamHandle.reshard()` and `post_reshard()` layer, there should not be any no-ops.

One final comment I will mention is that I like the `pre_unshard()`, `unshard()`, `post_unshard()`, and `reshard()`, `post_reshard()` organization because it makes it clear what the boundaries are and their temporal relationship. Through that, we can set pre- and post-conditions. Furthermore, we can eventually convert logic to hooks that may be registered on the `FlatParamHandle` (for `pre_unshard()`, `post_unshard()`, and `post_reshard()`). This may improve the customizability of FSDP.

 ## FSDP Runtime: `forward()`

- This PR reorganizes `forward()` in preparation for non-recursive wrapping, which uses pre-forward and post-forward hooks that expect the signature `hook(module, input)`. For FSDP, the `module` and `input` arguments are not used.
- This PR creates a new method `_fsdp_root_pre_forward()` to handle the logic only the root FSDP should run.

## FSDP Prefetching

Finally, we dive into the prefetching changes. Some highlights:
1. This PR unifies the execution order validation and prefetching implementations.
    - Both involve the execution order and can be unified to share some boilerplate.
2. Execution order validation only runs when the distributed debug level is `INFO`.
    - We have yet to have one success case where we actually catch an unintended source of dynamism. The warning is also too verbose. Hence, we are gating it by the `INFO` level.
3. This PR moves prefetching to be with respect to groups of handles (as mentioned in the constructor comment).
    - This is essential for supporting prefetching with non-recursive wrapping.
4. This PR does not include "bubbles", i.e. modules with no handles, in the recorded execution order(s). This deviates from the existing implementation.
    - This makes prefetching possibly more aggressive (when there are such bubbles), but it should not have significant performance implications either way.
5. This PR changes backward prefetching to reset the post-forward order each iteration (as intended).
6. This PR changes forward prefetching to use the first iteration's pre-forward order instead of the first iteration's post-forward order. (We can discuss whether we want this in this PR or not. Otherwise, I can keep it as using the post-forward order to preserve the existing semantics.) This PR also removes the `all_gather_stream.wait_stream(current_stream)` before forward prefetching because it does not help with high GPU reserved memory. We can add that back if desired.

### Appendix
#### Reverse Post-Forward Order Is Not Always the Pre-Backward Order
The existing PT-D FSDP pre-backward prefetching uses the reverse post-forward order.
<details>
  <summary>Model Code</summary>

  ```
  class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.block1 = nn.Sequential(
            nn.Conv2d(3, 4, kernel_size=3),
            nn.BatchNorm2d(4),
            nn.ReLU(inplace=True),
        )
        self.block2 = nn.Sequential(
            nn.Conv2d(4, 4, kernel_size=3),
            nn.BatchNorm2d(4),
            nn.ReLU(inplace=False),
        )
        self.block3 = nn.Linear(12, 8)
        self.head = nn.Sequential(
            nn.AdaptiveAvgPool2d(output_size=(1, 1)),
            nn.Flatten(),
            nn.Linear(4, 10),
        )

    def forward(self, x):
        x = self.block1(x)
        x = self.block2(x)
        x = self.block3(x)
        return self.head(x)

  model = Model().cuda()
  fsdp_kwargs = {}
  model.block1[1] = FSDP(model.block1[1], **fsdp_kwargs)  # BN2d
  model.block2[1] = FSDP(model.block2[1], **fsdp_kwargs)  # BN2d
  model.block1 = FSDP(model.block1, **fsdp_kwargs)
  model.block2 = FSDP(model.block2, **fsdp_kwargs)
  model.block3 = FSDP(model.block3, **fsdp_kwargs)
  model = FSDP(model, **fsdp_kwargs)
  ```
</details>

<details>
  <summary>Execution Orders </summary>

  ```
  Pre-backward hook for ('head.2.weight', 'head.2.bias') 140339520587136 (model)
  Pre-backward hook for ('weight', 'bias') 140339461194656 (block3)
  Pre-backward hook for ('0.weight', '0.bias') 140339520589776 (block2)
  Pre-backward hook for ('weight', 'bias') 140339520587664 (block2 BN)
  Pre-backward hook for ('weight', 'bias') 140339520586656 (block1 BN)
  Pre-backward hook for ('0.weight', '0.bias') 140339520588768 (block1)

  Pre-forward order:
  ('head.2.weight', 'head.2.bias') 140339520587136 (model)
  ('0.weight', '0.bias') 140339520588768 (block1)
  ('weight', 'bias') 140339520586656 (block1 BN)
  ('0.weight', '0.bias') 140339520589776 (block2)
  ('weight', 'bias') 140339520587664 (block2 BN)
  ('weight', 'bias') 140339461194656 (block3)

  Reverse post-forward order:
  ('head.2.weight', 'head.2.bias') 140339520587136 (model)
  ('weight', 'bias') 140339461194656 (block3)
  ('0.weight', '0.bias') 140339520589776 (block2)
  ('weight', 'bias') 140339520587664 (block2 BN)
  ('0.weight', '0.bias') 140339520588768 (block1)
  ('weight', 'bias') 140339520586656 (block1 BN)
  ```
</details>

Differential Revision: [D39293429](https://our.internmc.facebook.com/intern/diff/D39293429)
Pull Request resolved: https://github.com/pytorch/pytorch/pull/83665
Approved by: https://github.com/zhaojuanmao

---
## [Priyangshu1711/animepedia](https://github.com/Priyangshu1711/animepedia)@[d93637aa2f...](https://github.com/Priyangshu1711/animepedia/commit/d93637aa2f7457316f06b0f78126ade3cf2fecfc)
#### Wednesday 2022-10-12 18:04:05 by Rajat Dixit

Added Astro Boy

            <div class="card mb-3 card-bg my-4" style="max-width: 100%;">
                <div class="row no-gutters">
                    <div class="col-md-4">
                    <!-- Replace image_name_here by the complete name (with extension) of the image you uploaded -->
                        <img src="./images/Astro Boy.jpg" alt="Astro Boy" height="390px" width="300px">
                    </div>
                    <div class="col-md-8">
                        <div class="card-body">
                            <h2 class="card-title">Astro Boy</h2>
                            <p class="card-text">
                              One of the oldest anime characters in existence, Astro Boy first appeared on television screens in 1963, helping to usher in the phenomenon now known 
                               worldwide as anime.
                            </p>
                            <p>
                             Astro, a boy who was both more than human and less than human, guided kids through complex morality tales where the characters had complicated 
                             motivations, social problems didn't always have easy solutions, and people had the capacity to perform both great acts of kindness and of evil.
                           </p>
                            <hr>
                            <p>Contributed by- Rajat Dixit</p>
                        </div>
                    </div>
                </div>
            </div>
            <!--Sample [Character Name] card end-->
            <!--Add your card below this line -->

---
## [maxbossing/dotFiles](https://github.com/maxbossing/dotFiles)@[95d2ff2dae...](https://github.com/maxbossing/dotFiles/commit/95d2ff2daed6560c3222857784c86a22a7d158c6)
#### Wednesday 2022-10-12 19:29:24 by maxbossing

fuck you sudo why dont you work and dont destry my system

---
## [haproxy/haproxy](https://github.com/haproxy/haproxy)@[d114f4a68f...](https://github.com/haproxy/haproxy/commit/d114f4a68fa771d4dd1dc62430eb9e16a38c9fab)
#### Wednesday 2022-10-12 19:52:01 by Willy Tarreau

MEDIUM: checks: spread the checks load over random threads

The CPU usage pattern was found to be high (5%) on a machine with
48 threads and only 100 servers checked every second That was
supposed to be only 100 connections per second, which should be very
cheap. It was figured that due to the check tasks unbinding from any
thread when going back to sleep, they're queued into the shared queue.

Not only this requires to manipulate the global queue lock, but in
addition it means that all threads have to check the global queue
before going to sleep (hence take a lock again) to figure how long
to sleep, and that they would all sleep only for the shortest amount
of time to the next check, one would pick it and all other ones would
go down to sleep waiting for the next check.

That's perfectly visible in time-to-first-byte measurements. A quick
test consisting in retrieving the stats page in CSV over a 48-thread
process checking 200 servers every 2 seconds shows the following tail:

  percentile   ttfb(ms)
  99.98        2.43
  99.985       5.72
  99.99       32.96
  99.995     82.176
  99.996     82.944
  99.9965    83.328
  99.997      83.84
  99.9975    84.288
  99.998      85.12
  99.9985    86.592
  99.999         88
  99.9995    89.728
  99.9999   100.352

One solution could consist in forcefully binding checks to threads at
boot time, but that's annoying, will cause trouble for dynamic servers
and may cause some skew in the load depending on some server patterns.

Instead here we take a different approach. A check remains bound to its
thread for as long as possible, but upon every wakeup, the thread's load
is compared with another random thread's load. If it's found that that
other thread's load is less than half of the current one's, the task is
bounced to that thread. In order to prevent that new thread from doing
the same, we set a flag "CHK_ST_SLEEPING" that indicates that it just
woke up and we're bouncing the task only on this condition.

Tests have shown that the initial load was very unfair before, with a few
checks threads having a load of 15-20 and the vast majority having zero.
With this modification, after two "inter" delays, the load is either zero
or one everywhere when checks start. The same test shows a CPU usage that
significantly drops, between 0.5 and 1%. The same latency tail measurement
is much better, roughly 10 times smaller:

  percentile   ttfb(ms)
  99.98        1.647
  99.985       1.773
  99.99        4.912
  99.995        8.76
  99.996        8.88
  99.9965      8.944
  99.997       9.016
  99.9975      9.104
  99.998       9.224
  99.9985      9.416
  99.999         9.8
  99.9995      10.04
  99.9999     10.432

In fact one difference here is that many threads work while in the past
they were waking up and going down to sleep after having perturbated the
shared lock. Thus it is anticipated that this will scale way smoother
than before. Under strace it's clearly visible that all threads are
sleeping for the time it takes to relaunch a check, there's no more
thundering herd wakeups.

However it is also possible that in some rare cases such as very short
check intervals smaller than a scheduler's timeslice (such as 4ms),
some users might have benefited from the work being concentrated on
less threads and would instead observe a small increase of apparent
CPU usage due to more total threads waking up even if that's for less
work each and less total work. That's visible with 200 servers at 4ms
where show activity shows that a few threads were overloaded and others
doing nothing. It's not a problem, though as in practice checks are not
supposed to eat much CPU and to wake up fast enough to represent a
significant load anyway, and the main issue they could have been
causing (aside the global lock) is an increase last-percentile latency.

---
## [ShaviyaVictor/calendar](https://github.com/ShaviyaVictor/calendar)@[9339d67182...](https://github.com/ShaviyaVictor/calendar/commit/9339d671824737a34c2de968a9d78f0d6794cc13)
#### Wednesday 2022-10-12 21:12:00 by Shaviya

12102022_1610

Morning summon and the message God was sending to me. he again spoke the same message to me during my lunch hour break. The message has been passed God. Continue speaking to me and giving me the message you want me to know of and remember.

---
## [Dragonsis/CybersecurityWebsite.github.io](https://github.com/Dragonsis/CybersecurityWebsite.github.io)@[2cdc1c8d99...](https://github.com/Dragonsis/CybersecurityWebsite.github.io/commit/2cdc1c8d99d8182f8ba435149fee9957322de458)
#### Wednesday 2022-10-12 21:36:39 by Dragonsis

Final Project ~ HTML Code

Hello, Please review my HTML code. Thanks

<html>


    <head> Cybersecurity Information Project 450
        <meta charset="UTF-8">
        <meta name="description" content="Cybersecurity For Beginners">
        <title> Let Cybersecurity No Longer Be An Obscurity </title>
            <link rel=" stylesheet" type= "text/css" href="style sheet.css">    
    </head>
        <body>
            <h1> Let Cybersecurity No Longer Be An Obscurity</h1><hr/>
                <h2> About Me </h2>
                    <p style="color: black;"> <big> <b>I am </b></big> a student working on my Bachelors of Science Degree for Computer Information Technology at Northern Arizona University.<br>
                    During my studies, I realized the importance of Cybersecurity in today's technology-driven world.<br>
                    Children like my girls and senior citizens like my mother should be more aware of the risks and best cyber practices.<br>
                    Therefore, I am creating this website to help test and improve their knowledge and skills.<br>
                    Ultimately this website should improve anyone's confidence and ability to make good cyber choices and stay safe in cyberspace. </p>
                    <p style= "color:white; background-color:rgb(9, 7, 126)"><b> NAU CIT Information</b></p>             
                    <a href= "https://catalog.nau.edu/Catalog/details?plan=PLCITBA"><button>Computer Information Technology, Bachelor of Arts</button> </a> 
                    <a href= "https://catalog.nau.edu/Catalog/details?plan=PLCITBS&mobile=true"><button>Computer Information Technology, Bachelor of Science</button> </a> 
                    <hr/></a>    
                           <br>
                       
                    <p><h2>What is Cybersecurity?</h2><br> 
                    <big><b>Cybersecurity</b></big> is all the protection called that keeps a computer, laptop, smartphone, and tablet from someone stealing important and private information.</p>
<hr> 
                    <p><h2>What are Cybersecurity risk?</h2><br> 
                        <big><b>Cybersecurity risks</b></big> are the weaknesses (or vulnerabilities) that may lead to someone stealing important information. <br>
                        For example, a risk could be weak passwords or coming in contact with malware, or being part of an insecure network.<br>
                        <br>
                       <hr/>
                <h2> How to file a complaint?</h2>
                    <p> It is important to report any cybersecurity issues. The best way to report a crime is to contact reliable and trust worth sources, such as the FBI website. <br>
                         It is a great source to stay up to date on scams, attacks, and threats but also to file a complaint.</p>
                        <div> 
                            <img src="https://www.ic3.gov/Content/Images/LockNoText.jpg" alt="FBI Website Logo" 
                            title="File A Claim" width="600px">
                            <br><b>If you think you fell victim to a crime file a report with the FBI. <a href= "https://www.ic3.gov/Home/ComplaintChoice"><button>Click Here</button> </a> 
<hr/>
                        <h2>Top 3 Tips To Stay Cybersecure</h2>
                            <p><ol>
                                <li><b>Strong Passwords</b> </li>
                                <a href="https://www.youtube.com/watch?v=ZOtQ21hXJ7k"> 5 Tips for Cybersecurity Safety brought to you by Mayim Bialik  ~ Video</a> <br>
                                <li><b>Visit Safe Websites</b></li>
                                <a href="https://www.youtube.com/watch?v=bPVaOlJ6ln0">Cybersecurity: Crash Course Computer Science #31</a><br>
                                <li><b>Do Not Open Unknown Emails ... and if you do Do Not click on any attachments or links!
                                </b></li>
                                <a href="https://www.youtube.com/watch?v=_GzE99AmAQU&t=605s">Hackers & Cyber Attacks: Crash Course Computer Science #32 ~ Video</a></ol></p><hr/>

                         <h2>★ Helpful Videos For Teens & Kids ★</h2>
                            ★<a href="https://www.youtube.com/watch?v=sdpxddDzXfE">Cybersecurity explained for teens and kids. ~ Video</a><br>
                            ★<a href="https://www.youtube.com/watch?v=HxySrSbSY7o">Being Safe on the Internet ~ Video</a></p>
                            <hr>

                         <h2>★ Helpful Books To Learn More ★</h2>
                            ★<a href="https://www.barnesandnoble.com/w/oh-no-hacked-again-zinet-kemal/1141373070">Oh, No... Hacked Again! by Zinet Kemal. ~ Children's Book</a><br>
                            ★<a href="https://www.barnesandnoble.com/w/help-your-kids-with-computer-science-dk/1127203764?ean=9781465473608">Help Your Kids with Computer Science by DK ~ Children's Book</a><br>
                            ★<a href="https://www.barnesandnoble.com/w/how-cybersecurity-really-works-sam-grubb/1138326876?ean=9781718501287">How Cybersecurity Really Works…by Sam Grubb</a></p><br>
                            <hr>

                         <h2>Search Features</h2> 
                             <div><img src="http://www.w3.org/2003/glossary/w3c_gloss" alt="Glossary Reference" title="Glossary"> <form action= "https://www.w3.org/2003/glossary/">
                                <input type="text" name="q" >
                                <button>Search W3</button>
                                </form></a></div>

                                <div><img src="https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png" alt="Google Search" title="Google"> <form action= "https://www.google.com/">
                                <form action= "http://google.com/search">
                                <input type="text" name="q" >
                                <button>Search Google</button>
                                </form>



<!--<footer>Antigone H. Norgaard
e-mail: an864@nau.edu
</footer>
-->
</body>

---
## [Buildstarted/linksfordevs](https://github.com/Buildstarted/linksfordevs)@[9cb995f329...](https://github.com/Buildstarted/linksfordevs/commit/9cb995f329bd59218df3dbccc85ff90b599ffa19)
#### Wednesday 2022-10-12 22:05:31 by Ben Dornis

Updating: 10/12/2022 10:00:00 PM

 1. Added: Rent Market Doom
    (https://rodfer0x80.github.io/jekyll/update/2022/10/12/rent-market-doom.html)
 2. Added: Freeing myself from Roam Research (via LogSeq)
    (https://kobifelton.com/notes/freeing-myself-from-roam-research-via-logseq)
 3. Added: PowerShell, NPM Scripts, and Silently Dropped Arguments
    (https://www.lloydatkinson.net/posts/2022/powershell-npm-scripts-and-silently-dropped-arguments/)
 4. Added: Microsoft Ignite – Join us on October 12-14
    (https://ignite.microsoft.com/en-US/sessions/639d9c8d-e826-4a51-9e75-4c2c402b410a)
 5. Added: Microsoft Ignite – Join us on October 12-14
    (https://ignite.microsoft.com/en-US/sessions/77b252a9-c8c2-4c9a-bfd2-2d3d090f34e4?source=sessions)
 6. Added: Password Purgatory - Making Life Hell for Spammers
    (https://passwordpurgatory.com/get-hell?kvKey=4242ecc0-41ed-41ab-9c37-277fe3848484)
 7. Added: I cheated in high school (a lot) | Cyber Patterns
    (https://www.cyberpatterns.xyz/p/google)
 8. Added: Using Flux to Automate Simple Tasks
    (https://siebjee.nl/posts/using-flux-to-automate-simple-tasks/)

Generation took: 00:05:22.0457753

---
## [newstools/2022-sunday-world](https://github.com/newstools/2022-sunday-world)@[4a0eebe4ae...](https://github.com/newstools/2022-sunday-world/commit/4a0eebe4ae6e21f976cabf00d6644ee2851f6d5c)
#### Wednesday 2022-10-12 23:30:34 by Billy Einkamerer

Created Text For URL [sundayworld.co.za/news/jilted-lover-sentenced-to-life-for-knifing-girlfriend-to-death/]

---

