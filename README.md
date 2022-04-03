## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-04-02](docs/good-messages/2022/2022-04-02.md)


1,570,978 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,570,978 were push events containing 2,328,419 commit messages that amount to 146,095,113 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 41 messages:


## [Shadow-Quill/tgstation](https://github.com/Shadow-Quill/tgstation)@[50689f89a4...](https://github.com/Shadow-Quill/tgstation/commit/50689f89a40e5e7a2732a0c5fb38c787b69f7d28)
#### Saturday 2022-04-02 00:25:32 by LemonInTheDark

Action button refactor/rework: Enhanced Dragging (#65180)

About The Pull Request

I noticed a lot of strange and un-intuitive behavior in action buttons, and got stung by the bloat bug. Damn it hug #58027
I'll do my best to explain what I've changed and why, might get a bit long.
If you want a better idea, read the commits. Most of em are pretty solid, if long.

Whelp. Here we go.
How do action buttons currently work

All action buttons are draggable, to any place on the screen. They're held in an actions list on the player's mob.
Their location in this list determines their position on the top of the screen. If one is dragged away from the top, its position in the list is "saved". This looks really bad.
If two buttons are dragged over each other, their positions swap. (inside the actions list too)
If a button is shift clicked, it is brought back to the position it started at.
If the action collapse button that you likely just mentally edit out is alt clicked, it resets the position of all action buttons on the screen.
If an action is ctrl clicked, it is "locked". This prevents any future position changes, and also enables a saving feature. With this saving feature, locked button positions persist between rounds. So your first o2 canister will always start where you saved it, etc.
Actions and buttons are a one to one link. While there is functionality to share action buttons between two players, this means showing the same object to both. So one player can move a button on another's screen. Horrendous.
This also makes code that modifies properties of the screen object itself very clunky.
Why is this bad

A: None knew pretty much any of this information. It is actually documented, just in a horribly formatted screen tip on the collapse button, you know the one we all mentally delete from the hud.
B: None of this is intuitive. Dragging buttons makes the hud look much worse, and you get no feedback that you even can drag them. Depressing
C: We use actions to make new options clear to the player. This means players can have a lot of action buttons on the hud. This gets cluttery
D: The collapse button is useless. It lets you clear your screen if someone like me fucks up and gives you 2000 actions, but outside of that it just hides all information from you. You never want to see none of your action buttons, just a filtered list of them.
E: On a technical level, they're quite messy, and not fully functionally complete. This is depressing.
What I've done

Assuming the above to be true, how do we fix them?
Well first I'm going to go over everything I changed, including links to major commits. I'll then describe the finished product, and why I made the decisions I did.

Oh and I've moved some of the more niche or technical discussion to dropdowns. Hopefully this makes finding the major functional changes easier

Adds helper procs for turning screen_loc strings into more manageable arrays. This doesn't fully support all of the screen_loc spec, but it's enough for what I'm doing. (f54865f)

Uses these helper procs to improve existing code (6273b93)

Fixes an issue with tooltip code itself. If you tried to hold down a mouse button while dragging onto a tooltip enabled object, it would silently fail. The js made assumptions about the order args came in, which broke when buttons were held down (e0e42f6)

Adds a signal linked to /client/Click(). Surprised we didn't have this before honestly (c491a4a)

Makes /client/MouseDrag() return parent. If we don't do this, any overrides of MouseDrag will never actually be called (2190b2a)
Refactors how action buttons work under the hood (53ccce2)
Basically, rather then generating one button per action, we generate one button per viewer

Starts to change button behavior, more cleanup

Changes the mouse cursor when an action button is dragged. Hopefully
this makes moving things feel less like an accident, and makes you doing
it more clear

Removes the moved and locked vars. This will be more relevant later, but
for now:

Moved exists as a sort of budget "We've been dragged" variable. We can
handle this more cleanly, and the movable type doesn't care about it

Locked is a very old variable that is also not something that the
movable type "owns". It's more an action button thing that's been moved
down.
It exists so an action can be locked in place, and in that locking, be
treated as a "saved location"
(21e20fc)

Because I've nuked move, we don't need to directly set our button's
position. We can use the default_button_position var instead. This is
quite handy.

Please ignore position_action, I will explain that later
(83e265e)

Removes the buttons locked pref

It was another obscure part of action buttons, basically do buttons
start "locked" or not. See previous discussion of locked
(b58b1bd)

Major rework starts here

Alright. Sorry for this, this is where me not commiting regularly starts
to suck. I'll do my best though.

Rather then figuring out an action button's position via a combination
of the moved and ordered vars, we use a separate location var to store
one of a few defines. This makes life later much easier.

Adds tooltip support for dragging action buttons. The way the tooltip
just froze in place when dragging really bugged me, and lead to some
nasty visual artifacts.
This is a bit messy because the drag procs are horrible, but it's
workable

Dropping a button on another button will no longer swap their positions
Behavior instead depends on the target button.

If it's a part of a group (A concept I will explain later) the dragged
button is simply inserted before it in the group's list.

If it's floating on the general hud, we instead position the dragged
button to its right. There's extra logic here to ensure buttons will
never overflow the screen, but I'll get into that later.

Alright. That's most of the refactoring. Time for the larger behavior
changes.

Adds a button palette. This is a separate dropdown that renders
underneath buttons.

image

The idea is to allow for a conceptual separation between "important"
buttons and the ones that end up cluttering the screen.

You can click on the dropdown to open it, then any later clicks that
don't involve actions in some way will autoclose it.

My goal is to come up with an alternative for the action button that
just acted as a way to hide all buttons on screen. Not convinced it saw
much use.

As a side effect of removing that, I've moved its tooltip stuff to the
palette. I've properly formatted it, so hopefully it's easier to read
then the jumble that we used to have.

(You can alt click the palette button to reset all button positions)

Oh and the palette can scroll, since as you'll see later it has a
limited size.
image

Moving on from that, I've added what amounts to action landing buttons.
These allow buttons to rejoin groups, or be positioned at the end of a
line of buttons.
image

They've got a 32x32 hitbox, and only show up when dragging. Hopefully
this makes the system more clear just by dragging an action.

Oh and I've changed how button position updating works. The old system
of calling update_action_buttons on mob every time an action button
changes position is gone, mostly because I've setup more robust
grouping. Will discuss when I get to huds

(0d1e93f)
Adds the backbone behind action button position changes (94133bd)

Moves hud defines to the global folder, safer this way (7260117)

Adds color changing to the palette button, giving some heads up for buttons being inserted into the palette automatically
image
image
Ensures a landing button is always shown, even if it needs to break the
max row rule
Makes palettes auto contract if they have no buttons inside them
Prevents palettes from being opened if they have no buttons inside them
(f9417f3)
How it looks
2022-02-26.02-30-10.mp4
Why It's Good For The Game

Players have more control over the clutter on their screen.
Buttons are available, but not in the way,
Since any player move of a button saves it, any lack of clarity in the way buttons work will be forced out by buttons not just resetting when a new game starts.
We don't overlap any existing screen elements, unless the upper button list gets really long.
The code is much less crummy (I think, may have made it worse it's hard for me to judge my own work)

If it ends up not being as usable as I'd like, I'll rip out the existing changes and just implement the qol and backend stuff. I think it's worth doing though.
Changelog

cl
add: Expanded heavily on action buttons
add: Adds an action button dropdown that sits just under the normal list in the top left. You can drag new buttons onto it to insert them. Click on it to show its contents, do what you want to do, then click again anywhere to contract it. Alt click it to reset all button positions
add: Action buttons will now remember their position between rounds. So if you really like your flashlight right next to your player for some reason, we support that now
add: When you start to drag an action button, docking ports will appear in places that it can be inserted into. (Outside of just floating somewhere on your screen of course)
del: Removed action button locking, and the associated preference. I'm reasonably sure literally none uses this, but if you do hit me up
qol: Dragging an action button will now give you an outline of its size around your cursor
fix: You can no longer cause the screen to expand by putting an action button on the edge of widescreen, and then resizing to standard.
refactor: Refactors action and button code significantly. lots of little things.
/cl

---
## [Ebin-Halcyon/Skyrat-tg](https://github.com/Ebin-Halcyon/Skyrat-tg)@[8607ba8b7d...](https://github.com/Ebin-Halcyon/Skyrat-tg/commit/8607ba8b7d98c52e81f23816a9224adf70559c25)
#### Saturday 2022-04-02 01:15:51 by SkyratBot

[MIRROR] Adds a very rare sussy firelock [MDB IGNORE] (#12401)

* Adds a very rare sussy firelock (#65677)

On a VERY low chance (1/25000) a normal full tile firelock can instead be generated with a more suspicious appearance based on this recent quality shitpost.

Sussy firelocks are completely identical when open (save the desc) and thus are apt not to be noticed except during exciting times. It's a fully cosmetic joke that got me to log into github, and that's an accomplishment in itself. Probability rate fully negotiable, I've added a one in a million chance before after all.

* Adds a very rare sussy firelock

* ruins all the fun

people can get banned for doing the funny sus amogus so encouraging it in code, whilst it's beautiful and funny, eh someone is going to throw a fit.

Co-authored-by: Incoming5643 <incomingnumbers@gmail.com>
Co-authored-by: KathrinBailey <53862927+KathrinBailey@users.noreply.github.com>

---
## [OperativeLyn/tgstation](https://github.com/OperativeLyn/tgstation)@[54403a1ca0...](https://github.com/OperativeLyn/tgstation/commit/54403a1ca0a1d83302430bbb54a0d6bc561f0098)
#### Saturday 2022-04-02 01:37:48 by FinancialGoose

Fixes conveyor runtime (#65788)

Conveyor would runtime whenever it is right clicked with an item

Fixes #64595 (Runtime on conveyor for right clicking)

fixes a runtime with conveyor where right clicking it with any item would cause a runtime

Mothblocks rant from the issue report below, you've been warned:

Because right-clicking in BYOND is horse-shit. It pipes it all through the normal Click and only tells you it's a right-click through a flag. This means that on anything that isn't prepared, right-clicking is the same as left-clicking, which is terrible UX that only exists in SS13.

Nothing should return ..() from attackby_secondary, because the default is the legacy behavior of making right-click pass as left-click (which I want to kill ASAP, once nothing uses the stupid flags anymore).

Remove else return ..(), and make this whole thing do return SECONDARY_ATTACK_CANCEL_ATTACK_CHAIN.

---
## [Haleymiranda79/The-Internet-Atom-bomb.-Same-thing](https://github.com/Haleymiranda79/The-Internet-Atom-bomb.-Same-thing)@[2fcb69694d...](https://github.com/Haleymiranda79/The-Internet-Atom-bomb.-Same-thing/commit/2fcb69694dc5341e9a52a061345a5f2f1cf27002)
#### Saturday 2022-04-02 01:57:16 by X

Google is my friend. I love their imagination. But I inspected you " broken" page and the data said under the 404 Munchkin

https://bugs.chromium.org/p/chromium/issues/detail?id=846170, What's so secret about that? I have to go. I want to read the juiciness. Chromium is interesting even though I have no clue what their purpose is. Lots of buttons to push and data! Love the data.

---
## [sraoss/pgsql-ivm](https://github.com/sraoss/pgsql-ivm)@[5e144cc89b...](https://github.com/sraoss/pgsql-ivm/commit/5e144cc89b468d845a2dbd7bdd1786c6efcdfd83)
#### Saturday 2022-04-02 02:08:52 by Tom Lane

Revert applying column aliases to the output of whole-row Vars.

In commit bf7ca1587, I had the bright idea that we could make the
result of a whole-row Var (that is, foo.*) track any column aliases
that had been applied to the FROM entry the Var refers to.  However,
that's not terribly logically consistent, because now the output of
the Var is no longer of the named composite type that the Var claims
to emit.  bf7ca1587 tried to handle that by changing the output
tuple values to be labeled with a blessed RECORD type, but that's
really pretty disastrous: we can wind up storing such tuples onto
disk, whereupon they're not readable by other sessions.

The only practical fix I can see is to give up on what bf7ca1587
tried to do, and say that the column names of tuples produced by
a whole-row Var are always those of the underlying named composite
type, query aliases or no.  While this introduces some inconsistencies,
it removes others, so it's not that awful in the abstract.  What *is*
kind of awful is to make such a behavioral change in a back-patched
bug fix.  But corrupt data is worse, so back-patched it will be.

(A workaround available to anyone who's unhappy about this is to
introduce an extra level of sub-SELECT, so that the whole-row Var is
referring to the sub-SELECT's output and not to a named table type.
Then the Var is of type RECORD to begin with and there's no issue.)

Per report from Miles Delahunty.  The faulty commit dates to 9.5,
so back-patch to all supported branches.

Discussion: https://postgr.es/m/2950001.1638729947@sss.pgh.pa.us

---
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[1b7d7d9327...](https://github.com/pytorch/pytorch/commit/1b7d7d93276eb37c009905ef87ea9c2a7c95481e)
#### Saturday 2022-04-02 02:33:52 by Brian Hirsh

Reland: "free up dispatch key space (in C++)" (#74963)

Summary:
Pull Request resolved: https://github.com/pytorch/pytorch/pull/74963

This is a re-land of D35192346 (https://github.com/pytorch/pytorch/commit/9872a06d77582e91e834103db75f774ca75f7fff) and D35192317 (https://github.com/pytorch/pytorch/commit/a9216cde6cc57f94586ea71a75a35aaabee720ff), which together are a diff that changes the internal representation of `DispatchKeySet` in pytorch core to free up the number of dispatch keys that we have available. See a more detailed description of the design in the original PR: https://github.com/pytorch/pytorch/pull/69633.

The original PR broke Milan workflows, which use a pytorch mobile build, and manifested as a memory corruption bug inside of `liboacrmerged.so`.

**Background: Existing Mobile Optimization**
Pytorch mobile builds have an existing optimization (here https://github.com/pytorch/pytorch/blob/cc23725e89713138aa1c81ce5fb4a8dbcd440ccf/c10/core/DispatchKey.h#L382 and here https://github.com/pytorch/pytorch/blob/cc23725e89713138aa1c81ce5fb4a8dbcd440ccf/aten/src/ATen/core/dispatch/OperatorEntry.h#L214), which works as follows:

Every operator in pytorch has a "dispatch table" of function pointers, corresponding to all of the (up to 64) different kernels that we might dispatch to when we run an operator in pytorch (autograd, cpu, cuda, complex number support, etc).

In mobile builds, the size of that table is shrunk from 64 to 8 to save a bunch of space, because mobile doesn't end up using the functionality associated with most dispatch keys.

The dispatcher also has a notion of "fallback kernels", which are kernels that you can register to a particular dispatch key, but should be able to work for "any operator". The array of fallback kernels is defined here: https://github.com/pytorch/pytorch/blob/cc23725e89713138aa1c81ce5fb4a8dbcd440ccf/aten/src/ATen/core/dispatch/Dispatcher.h#L294.

The mobile-optimization currently does **not** extend to this array (it wouldn't be that useful anyway because there is only one array of fallback kernels globally - vs. there is a separate dispatch table of function pointers per operator). So the per-operator tables on mobile are size 8, while the fallback table is size 64.

**The Bug**
This PR actually makes it difficult to enable that optimization separately for the per-operator arrays vs. the fallback array, and incidentally shrunk the size of the fallback array from 64 to 8 for mobile (that happened on this line: https://github.com/pytorch/pytorch/pull/69633/files#diff-f735cd7aa68f15b624100cbc4bb3b5ea76ffc7c9d3bec3b0ccabaa09609e5319R294).

That isn't a problem by itself (since mobile doesn't actually use any of the fallbacks that can no longer be stored). However, pytorch core will still register all of those fallback kernels on startup in mobile builds, even if they aren't used. When we tried to register one of those fallbacks on startup, it would try to dump the kernel somewhere in memory past the bounds of the (now smaller) array inside of the `Dispatcher` object, `backendFallbackKernels_`.

**Why didn't this problem show up in OSS CI? Why didn't it break other internal mobile workflows aside from Milan?**

Ideally, this failure would show up as part of the OSS signal on GitHub, since we already have mobile OSS builds. Given that it was another memory corruption issue that only affected Milan (subset of mobile), I'm not sure what's specific about Milan's builds that caused it only to manifest there. dreiss I wonder if there's another flavor of mobile builds we could run in OSS CI that could potentially help catch this?

**The debugging experience was pretty difficult**

Debugging the Milan-specific failure was made difficult by the following:

(1) lack of CI
- the original Milan failure didn't surface on my original diff, because the Milan job(s) that failed weren't triggered to run on pytorch changes. There's probably a balance to strike here, since those jobs will only be useful if they aren't flaky, and if they can produce reliable failure logs for debugging.

(2) It's difficult to get a repro.
- my work laptop doesn't have the right specs to run the Milan development workflow (not enough disk space)
- There is an existing OnDemand workflow for Milan, but it appears to be relatively new, and after a bunch of help from MarcioPorto, we ran into issues forwarding the log output from Milan tests on the emulator back to the terminal (see the original discussion here: https://fb.workplace.com/groups/OnDemandFRL/permalink/1424937774645433/)

(3) Lack of stack-traces.
- Most Milan failures didn't include actionable stack traces. phding generously helped me debug by running my suggested patches locally, and reporting back if there were any failures. The failing test didn't include a stack trace though (just the line where the crash appeared), so I ended up making some educated guesses about what the issue was based on the area of the crash.
ghstack-source-id: 152688542

Test Plan: Confirmed with phding that the broken Milan workflow from the previous version of this diff is now passing.

Reviewed By: phding, albanD

Differential Revision: D35222806

fbshipit-source-id: 0ad115a0f768bc8ea5d4c203b2990254c7092d30
(cherry picked from commit 002b91966f11fd55ab3fa3801b636fa39a6dd12c)

---
## [tadryanom/apache_couchdb](https://github.com/tadryanom/apache_couchdb)@[9b6454b81c...](https://github.com/tadryanom/apache_couchdb/commit/9b6454b81ca1a599da1f538548dc67654b6ce8d7)
#### Saturday 2022-04-02 03:12:27 by Adam Kocoloski

Refactor Jenkins build to dynamically generate test stages (#3903)

This is one of those situations where you go in to make a small change,
see an opportunity for some refactoring, and get sucked into a rabbit
hole that leaves you wondering if you have any idea how computers
actually work. My initial goal was simply to update the Erlang version
used in our binary packages to a modern supported release. Along the
way I decided I wanted to figure out how to eliminate all the copypasta
we generate for making any change to this file, and after a few days of
hacking here we are. This rewrite has the following features:

* Updates to use Debian 11 (current stable) as the base image for
  building releases and packaging repos.

* Defaults to Erlang 24.2 as the embedded Erlang version in packages.

* Dynamically generates the parallel build stages used to test and
  package CouchDB on various OSes. This is accomplished through a bit
  of scripted pipeline code that relies on two new methods defined at
  the beginning of the Jenkinsfile, one for "native" builds on macOS
  and FreeBSD and one for container-based builds. See comments in the
  Jenkinsfile for additional details.

* Expands commands like `make check` into a series of steps to improve
  visibility. The Jenkins UI will now show the time spent in each step
  of the build process, and if a step (e.g. `make eunit`) fails it will
  only expand the logs for that step by default instead of showing the
  logs for the entire build stage. The downside is that if we do make
  changes to the series of targets underneath `check` we need to
  remember to update the Jenkinsfile as well.

* Starts per-stage timer _after_ agent is acquired. Previously builds could
  fail with a 15m timeout when all they did was sit in the build queue.

---
## [PixelExperience-Devices/kernel_oneplus_sm8150](https://github.com/PixelExperience-Devices/kernel_oneplus_sm8150)@[c43d7ae3c6...](https://github.com/PixelExperience-Devices/kernel_oneplus_sm8150/commit/c43d7ae3c6b686876b152043fe007cbd103de74c)
#### Saturday 2022-04-02 06:16:03 by alk3pInjection

drm: Handle dim for udfps

* Apparently, los fod impl is better than udfps cuz it
  has onShow/HideFodView hook, which allows us to toggle
  dimlayer seamlessly.

  Since udfps only partially supports the former one,
  we'd better kill dim in kernel. This is kinda a hack
  but it works well, bringing perfect fod experience
  back to us.

Co-authored-by: Art_Chen <Chenxy0201@qq.com>
Signed-off-by: alk3pInjection <webmaster@raspii.tech>
Change-Id: I80bfd508dacac5db89f4fff0283529c256fb30ce

---
## [TravMurav/linux](https://github.com/TravMurav/linux)@[53a05ad9f2...](https://github.com/TravMurav/linux/commit/53a05ad9f21d858d24f76d12b3e990405f2036d1)
#### Saturday 2022-04-02 07:21:05 by David Hildenbrand

mm: optimize do_wp_page() for exclusive pages in the swapcache

Patch series "mm: COW fixes part 1: fix the COW security issue for THP and swap", v3.

This series attempts to optimize and streamline the COW logic for ordinary
anon pages and THP anon pages, fixing two remaining instances of
CVE-2020-29374 in do_swap_page() and do_huge_pmd_wp_page(): information
can leak from a parent process to a child process via anonymous pages
shared during fork().

This issue, including other related COW issues, has been summarized in [2]:

 "1. Observing Memory Modifications of Private Pages From A Child Process

  Long story short: process-private memory might not be as private as you
  think once you fork(): successive modifications of private memory
  regions in the parent process can still be observed by the child
  process, for example, by smart use of vmsplice()+munmap().

  The core problem is that pinning pages readable in a child process, such
  as done via the vmsplice system call, can result in a child process
  observing memory modifications done in the parent process the child is
  not supposed to observe. [1] contains an excellent summary and [2]
  contains further details. This issue was assigned CVE-2020-29374 [9].

  For this to trigger, it's required to use a fork() without subsequent
  exec(), for example, as used under Android zygote. Without further
  details about an application that forks less-privileged child processes,
  one cannot really say what's actually affected and what's not -- see the
  details section the end of this mail for a short sshd/openssh analysis.

  While commit 17839856fd58 ("gup: document and work around "COW can break
  either way" issue") fixed this issue and resulted in other problems
  (e.g., ptrace on pmem), commit 09854ba94c6a ("mm: do_wp_page()
  simplification") re-introduced part of the problem unfortunately.

  The original reproducer can be modified quite easily to use THP [3] and
  make the issue appear again on upstream kernels. I modified it to use
  hugetlb [4] and it triggers as well. The problem is certainly less
  severe with hugetlb than with THP; it merely highlights that we still
  have plenty of open holes we should be closing/fixing.

  Regarding vmsplice(), the only known workaround is to disallow the
  vmsplice() system call ... or disable THP and hugetlb. But who knows
  what else is affected (RDMA? O_DIRECT?) to achieve the same goal -- in
  the end, it's a more generic issue"

This security issue was first reported by Jann Horn on 27 May 2020 and it
currently affects anonymous pages during swapin, anonymous THP and hugetlb.
This series tackles anonymous pages during swapin and anonymous THP:

 - do_swap_page() for handling COW on PTEs during swapin directly

 - do_huge_pmd_wp_page() for handling COW on PMD-mapped THP during write
   faults

With this series, we'll apply the same COW logic we have in do_wp_page()
to all swappable anon pages: don't reuse (map writable) the page in
case there are additional references (page_count() != 1). All users of
reuse_swap_page() are remove, and consequently reuse_swap_page() is
removed.

In general, we're struggling with the following COW-related issues:

(1) "missed COW": we miss to copy on write and reuse the page (map it
    writable) although we must copy because there are pending references
    from another process to this page. The result is a security issue.

(2) "wrong COW": we copy on write although we wouldn't have to and
    shouldn't: if there are valid GUP references, they will become out
    of sync with the pages mapped into the page table. We fail to detect
    that such a page can be reused safely, especially if never more than
    a single process mapped the page. The result is an intra process
    memory corruption.

(3) "unnecessary COW": we copy on write although we wouldn't have to:
    performance degradation and temporary increases swap+memory
    consumption can be the result.

While this series fixes (1) for swappable anon pages, it tries to reduce
reported cases of (3) first as good and easy as possible to limit the
impact when streamlining.  The individual patches try to describe in
which cases we will run into (3).

This series certainly makes (2) worse for THP, because a THP will now
get PTE-mapped on write faults if there are additional references, even
if there was only ever a single process involved: once PTE-mapped, we'll
copy each and every subpage and won't reuse any subpage as long as the
underlying compound page wasn't split.

I'm working on an approach to fix (2) and improve (3): PageAnonExclusive
to mark anon pages that are exclusive to a single process, allow GUP
pins only on such exclusive pages, and allow turning exclusive pages
shared (clearing PageAnonExclusive) only if there are no GUP pins.  Anon
pages with PageAnonExclusive set never have to be copied during write
faults, but eventually during fork() if they cannot be turned shared.
The improved reuse logic in this series will essentially also be the
logic to reset PageAnonExclusive.  This work will certainly take a
while, but I'm planning on sharing details before having code fully
ready.

#1-#5 can be applied independently of the rest. #6-#9 are mostly only
cleanups related to reuse_swap_page().

Notes:
* For now, I'll leave hugetlb code untouched: "unnecessary COW" might
  easily break existing setups because hugetlb pages are a scarce resource
  and we could just end up having to crash the application when we run out
  of hugetlb pages. We have to be very careful and the security aspect with
  hugetlb is most certainly less relevant than for unprivileged anon pages.
* Instead of lru_add_drain() we might actually just drain the lru_add list
  or even just remove the single page of interest from the lru_add list.
  This would require a new helper function, and could be added if the
  conditional lru_add_drain() turn out to be a problem.
* I extended the test case already included in [1] to also test for the
  newly found do_swap_page() case. I'll send that out separately once/if
  this part was merged.

[1] https://lkml.kernel.org/r/20211217113049.23850-1-david@redhat.com
[2] https://lore.kernel.org/r/3ae33b08-d9ef-f846-56fb-645e3b9b4c66@redhat.com

This patch (of 9):

Liang Zhang reported [1] that the current COW logic in do_wp_page() is
sub-optimal when it comes to swap+read fault+write fault of anonymous
pages that have a single user, visible via a performance degradation in
the redis benchmark.  Something similar was previously reported [2] by
Nadav with a simple reproducer.

After we put an anon page into the swapcache and unmapped it from a single
process, that process might read that page again and refault it read-only.
If that process then writes to that page, the process is actually the
exclusive user of the page, however, the COW logic in do_co_page() won't
be able to reuse it due to the additional reference from the swapcache.

Let's optimize for pages that have been added to the swapcache but only
have an exclusive user.  Try removing the swapcache reference if there is
hope that we're the exclusive user.

We will fail removing the swapcache reference in two scenarios:
(1) There are additional swap entries referencing the page: copying
    instead of reusing is the right thing to do.
(2) The page is under writeback: theoretically we might be able to reuse
    in some cases, however, we cannot remove the additional reference
    and will have to copy.

Note that we'll only try removing the page from the swapcache when it's
highly likely that we'll be the exclusive owner after removing the page
from the swapache.  As we're about to map that page writable and redirty
it, that should not affect reclaim but is rather the right thing to do.

Further, we might have additional references from the LRU pagevecs, which
will force us to copy instead of being able to reuse.  We'll try handling
such references for some scenarios next.  Concurrent writeback cannot be
handled easily and we'll always have to copy.

While at it, remove the superfluous page_mapcount() check: it's
implicitly covered by the page_count() for ordinary anon pages.

[1] https://lkml.kernel.org/r/20220113140318.11117-1-zhangliang5@huawei.com
[2] https://lkml.kernel.org/r/0480D692-D9B2-429A-9A88-9BBA1331AC3A@gmail.com

Link: https://lkml.kernel.org/r/20220131162940.210846-2-david@redhat.com
Signed-off-by: David Hildenbrand <david@redhat.com>
Reported-by: Liang Zhang <zhangliang5@huawei.com>
Reported-by: Nadav Amit <nadav.amit@gmail.com>
Reviewed-by: Matthew Wilcox (Oracle) <willy@infradead.org>
Acked-by: Vlastimil Babka <vbabka@suse.cz>
Cc: Hugh Dickins <hughd@google.com>
Cc: David Rientjes <rientjes@google.com>
Cc: Shakeel Butt <shakeelb@google.com>
Cc: John Hubbard <jhubbard@nvidia.com>
Cc: Jason Gunthorpe <jgg@nvidia.com>
Cc: Mike Kravetz <mike.kravetz@oracle.com>
Cc: Mike Rapoport <rppt@linux.ibm.com>
Cc: Yang Shi <shy828301@gmail.com>
Cc: Kirill A. Shutemov <kirill.shutemov@linux.intel.com>
Cc: Jann Horn <jannh@google.com>
Cc: Michal Hocko <mhocko@kernel.org>
Cc: Rik van Riel <riel@surriel.com>
Cc: Roman Gushchin <roman.gushchin@linux.dev>
Cc: Andrea Arcangeli <aarcange@redhat.com>
Cc: Peter Xu <peterx@redhat.com>
Cc: Don Dutile <ddutile@redhat.com>
Cc: Christoph Hellwig <hch@lst.de>
Cc: Oleg Nesterov <oleg@redhat.com>
Cc: Jan Kara <jack@suse.cz>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>

---
## [Team-BNUY/gamelab_project_bunny](https://github.com/Team-BNUY/gamelab_project_bunny)@[932a754040...](https://github.com/Team-BNUY/gamelab_project_bunny/commit/932a754040ba7a33a08f83fde1012168a98c67f2)
#### Saturday 2022-04-02 07:50:13 by sharon-ku

[Art][Classroom] Added tiny decorations along whiteboard; reverted whiteboard to logo

Honestly I'm having trouble remembering what I've done and it is bad to be sleep deprived at 4AM. If you are reading this, know that we as students should develop better sleeping habits.

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[0b8b52e36c...](https://github.com/treckstar/yolo-octo-hipster/commit/0b8b52e36c23ae47bce1c19183df5d1a39c44f24)
#### Saturday 2022-04-02 08:00:04 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [sony-msm8956-dev/android_kernel_sony_msm8956](https://github.com/sony-msm8956-dev/android_kernel_sony_msm8956)@[583c978c06...](https://github.com/sony-msm8956-dev/android_kernel_sony_msm8956/commit/583c978c0686bce0d1fb6bcefbc26b2804b97b97)
#### Saturday 2022-04-02 09:44:14 by Masahiro Yamada

modpost: file2alias: go back to simple devtable lookup

commit ec91e78d378cc5d4b43805a1227d8e04e5dfa17d upstream.

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
Signed-off-by: Kevin F. Haggerty <haggertk@lineageos.org>
Change-Id: Ic632eaa7777338109f80c76535e67917f5b9761c

---
## [saint-lascivious/munin-pihole-plugins](https://github.com/saint-lascivious/munin-pihole-plugins)@[ee9a2d909d...](https://github.com/saint-lascivious/munin-pihole-plugins/commit/ee9a2d909d2b33f3e00b83264337bd4199e5072f)
#### Saturday 2022-04-02 10:23:04 by Hayden Pearce

munin-pihole-plugins: refactor install/uninstall functions

optional parameters for install and uninstall commands, an exercise in making install/uninstall commands that are more user friendly

Changes to be committed:
 - modified:   README.md
   update help text example
 - modified:   script/munin-pihole-plugins
   bump version to 04.06.00
   (a lot went on under the hood for nothing muvh to change)
   remove all remnants of the old plugin config naming scheme
   update short and long form help text
   (install and uninstall accept an optional parameter now)
   describe optional parameters in long form help text
   (display the command queried in usage and example text)
   (there's no solid standard for help texts, it is annoying)
   (use {} for required input, use [] for optional input)
   add shortcuts for installing only plugins, script, webserver
   add shortcuts for uninstalling only plugins, script, webserver
   (install and uninstall commands now accept an optional parameter)
   (plugins, script, webserver)
   (potentially more flexible and convenient)
   add *-only cheat code for install/uninstall
   ('munin-pihole-plugins --uninstall plugins-only', for example)
   (does not prompt to install/uninstall dependencies)
   (somewhat of an abuse, SKIP_DEP* should just be called YOLO)
   (currently undocumented, outside of here, now)
   update min_height values in help_function as required
   (the extended install/uninstall help text got a little fatter)
   minor formatting changes in input_handler
   (as i keep saying, and then fucking up, consistency is key)

---
## [rytt0001/RWoM](https://github.com/rytt0001/RWoM)@[5b5e8ea252...](https://github.com/rytt0001/RWoM/commit/5b5e8ea25231358a84865efd237d2470d0752132)
#### Saturday 2022-04-02 10:30:56 by TorannD

v2.6.6.0

New:
 o Supporting magic traits:
	- Giants Blood: descendant of giants - endowed with with great strength and stamina, but slow to recover
	- Fae Blood: descendant of fae folk with a natural connection to the arcane
	- Enlightened: blessed by magic, able to harness its power without suffering the full side-effects
	- Cursed: tormented by a constant, burning rush of power that inflicts arcane weakness...

 o New class abilities for Empath and Apothecary
  - Apothecary:
	>Fire Suppression Flask (class skill)- ingredients that instantly smother fire in an area
	>Bliss (learnable scroll) - concoction that puts a pawn into a state of euphoria where pain and emotions are inconsequential, but slowly reduces skills and causes a major penalty for skill learning
	>Clarity (learnable scroll) - potion which reduces resistance to the arcane; increases mana regeneration and psychic sensitivity and the cost of mental stability

  - Empath:
   >Symbiosis (class skill) - entwines the will of an empath with another, granting great mental fortitude and awareness; the empath's presence remains with the host for the duration of this ability, leaving the body of the empath as an empty shell
   >Faded Emotions (learnable scroll) - causes the target pawn to address their emotions directly to get over whatever causes their negative mood

 o Standalone spell Magic Wardrobe - swaps apparel with an apparel set stored in a dimension pocket (apparel sets not included)
 o Fire Mage spell Heat Shield - temporary protection against heat damage and prevents pawns from catching fire
 o Ice Mage spell Alter Storm - alters rainy or snowy weather with unique conditions
 o Golemancer's can create a body tattoo using rune carving techniques that grant enchantment bonuses - if using ideology, the pawn will get a new body tattoo
 o Standalone and learnable abilities can now be configured to autocast
 o Hediffs can accept enchantments using a per stage def extension (see Clarity hediff for example)
 o Weather event: Hail storm - found mostly in cold climates, hail storms may cause injury to exposed pawns; will not puncture a roof

*new abilities will only be discovered for new classes - existing classes will not be able to retroactively learn the new abilities but will be able to gain the new skills if their class is cleared using a shard of extraction and then the same (or another) class gained

Tweaks:
 o Techno turret no longer needs to be manned; default duration is 60s and can be upgraded to last longer
 o Charge Battery spell can be used to charge golems
 o Hail storm and Healing rain weather events may occur (uncommonly) on standard maps under the right conditions
 o Apothecary gathers ingredients while caravaning based on their forage rate and gathering skill
 o Transmuting equipment made from stuff now has a minimum (10%) and maximum value (300%) relative to the value of the original stuff

Bug fixes:
 o Transpose will correctly assign drafted status and reversal hediff when used on, or by, a non-colonist pawn (t)
 o Golem drafted orders
 o Player rifts from Voidseeker role will no longer drop resources

---
## [avar/git](https://github.com/avar/git)@[ba6177f59b...](https://github.com/avar/git/commit/ba6177f59bbac68a2d51af8e3db61bb06cf8b75d)
#### Saturday 2022-04-02 10:43:09 by Ævar Arnfjörð Bjarmason

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
## [froschdesign/laminas.github.io](https://github.com/froschdesign/laminas.github.io)@[14801965a7...](https://github.com/froschdesign/laminas.github.io/commit/14801965a7ceb485eabbcdd58a8408aaff89d8bd)
#### Saturday 2022-04-02 11:30:00 by Michał Bundyra

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
## [echothegoddess/hyfetch](https://github.com/echothegoddess/hyfetch)@[5ede07e9ba...](https://github.com/echothegoddess/hyfetch/commit/5ede07e9bad31919d080e775d8f4f83383019e55)
#### Saturday 2022-04-02 11:31:09 by echo

like i think everything';s ok, i look at the code, boonm, 10 bugsm 10 errors

why the fuck did i chooes progragmming, im really a masochisyt. fuck this shit. i hate you.

---
## [robbertapir/tgstation](https://github.com/robbertapir/tgstation)@[c8ef62c1fb...](https://github.com/robbertapir/tgstation/commit/c8ef62c1fb7027ea58b569f0e4bd7df5a7d58935)
#### Saturday 2022-04-02 12:25:17 by LemonInTheDark

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
## [lollek/dwm](https://github.com/lollek/dwm)@[67d76bdc68...](https://github.com/lollek/dwm/commit/67d76bdc68102df976177de351f65329d8683064)
#### Saturday 2022-04-02 12:29:43 by Chris Down

Do not allow focus to drift from fullscreen client via focusstack()

It generally doesn't make much sense to allow focusstack() to navigate
away from the selected fullscreen client, as you can't even see which
client you're selecting behind it.

I have had this up for a while on the wiki as a separate patch[0], but
it seems reasonable to avoid this behaviour in dwm mainline, since I'm
struggling to think of any reason to navigate away from a fullscreen
client other than a mistake.

0: https://dwm.suckless.org/patches/alwaysfullscreen/

---
## [JohnFulpWillard/tgstation](https://github.com/JohnFulpWillard/tgstation)@[e58fb506ef...](https://github.com/JohnFulpWillard/tgstation/commit/e58fb506effebc734a661718bed9ab2ffeb50c9e)
#### Saturday 2022-04-02 12:36:19 by LemonInTheDark

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
## [LumberKing/Tianxia](https://github.com/LumberKing/Tianxia)@[37b0c2f006...](https://github.com/LumberKing/Tianxia/commit/37b0c2f0069b3b20cfb745d2ea561fd45d865e7c)
#### Saturday 2022-04-02 12:54:27 by Silversweeper

Balance/optimization/polishing (part 10 of ???) + Fujiwara improvements (6 of 6)

Artefacts and artefact spawns:
- Nerfed the Nihon Shoki and the Kojiki and lowered their quality.
- Updated the conditions for various artefacts, particularly a bunch related to Japan.
- The Totsuka no Tsuragi now spawn when the game starts, instead of being discoverable.

CBs:
- "Chinese enough" and "Japanese enough" pagans that are NOT nomads are no longer eligible for the pagan County Conquest CB; such realms are not meant to be expansionistic in that fashion. The optional JD Border Dispute CB has been made avaliable for these rulers if it is enabled.
- The Holy War CB and its pagan and Buddhist counterparts now show up in the GUI for people that'd be eligible if they were independent but that are blocked by their top liege's government type.
- Caliphal Subjugation is no longer available if your top liege has one of the Chinese or Japanese government types.
- Rulers with various Chinese-style governments now get access to the Chinese Subjugation CB against suitable targets when appropriate.
- Rulers with various Japanese-style governments no longer get the Indian Subjugation CB, instead getting a similar CB against suitable targets when appropriate.
- Reworked the Chinese Imperial Reconquest CB, and made it free for the EoC (similar to how the Roman Imperial Reconquest is free for the RE).
- Reworked the Japanese Reconquest CB, and made it free for the Tenno (similar to how the Roman Imperial Reconquest is free for the RE).
- Removed the Mon Rebellion CB and made the relevant war a Bid for Independence war, with Yamankhan getting k_pegu if he wins and it isn't held by anyone.
- Added the Ryukyuan Subjugation CB.
- Kiyohara Masahira should now get the event he is supposed to get if he wins the Gosannen War.
- Children can no longer create Grand Chancellor bloodlines.

Council patterns, councillors, and voting:
- AI councillors eligible for Chinese Imperial (theoretically; this is to cover (Xi-)Xia), Confucian Bureaucracy, or Japanese Bureaucracy now care about their liege's MoH rating when deciding on their voting pattern.
- Moved Japanese council logic (e.g. "No, I will not support executing the Tenno if you or I logically should care!") to a separate voting pattern and made it take precedence over everything else.
- Moved Council Eunuch logic to a separate file and made it relevant for Pragmatists (beating the normal pragmatist pattern), Glory Hounds (below the normal Glory Hound pattern), and Zealots (before the normal family-based logic).
- Added new bureaucrat voting logic for all bureaucratic government vassals with bureaucratic government lieges (Chinese/Eastern/Japanese/Divine Imperial, Confucian/Japanese Bureaucracy). Largely similar to the eunuch logic when it comes to landing/revoking/wars, and inserted at (effectively) the same priority level, but these make exceptions for their own dynasty members.
- Eunuchs and bureaucrats now care about nepotism as far as the liege's dynasty goes (unless it is also their dynasty).
- Cleaned up vanilla files that no longer are relevant due to the above.
- Removed the prestige requirement and cost for bureaucratic government rulers firing councillors, seeing as it resulted in these rulers ending up with negative prestige fairly often.
- If you grant a councillor position to a Grand Chancellor bloodline member and you can have a Grand Chancellor they will immediately gain the Grand Chancellor minor title if you don't already have one of those.

Governments:
- The various Chinese and Japanese governments can no longer hold tribal holdings without penalty even with matching culture.
- Fixed Bamar characters going nomadic for no good reason.

Landed titles:
- If a religion has been reformed with Divine Ancestry you now need to be a member of the relevant bloodline to recreate the title if it is destroyed.

Laws:
- Updated law restrictions for the "The Three Mountains" Doctrine.

Minor titles:
- Added a minor title for Grand Chancellors, tying some of the bloodline's powers to it.

Objectives:
- The "The Three Mountains" Doctrine now makes co-religionist vassals much more likely to seek independence.
- The "The Three Mountains" Doctrine now makes co-religionist vassals much more likely to start/join factions for their own claims.
- Vassals following a religion with the "The Three Mountains" Doctrine that have a liege with the same religion can now start and join factions even if on the council.
- The Grand Chancellor can now join the Claimant, Independence, and Takeover factions even if on the council.

Religion features:
- The "The Three Mountains" Doctrine can no longer be picked alongside the Unyielding Nature.
- The "The Three Mountains" Doctrine now gives access to the once-per-life (actually 100 years) Ryukyuan Subjugation CB, available against any and all independent targets within holy war range. This CB counts as a holy war as far as co-religionists joining goes (i.e. has is_holy_war = yes), and works as other Subjugation CBs w.r.t. the Become King ambition. Losing this war to a co-religionist as a secular Ryukyuan rel head means losing the rel head title, regardless of whether you remain independent, seeing as you are obviously unfit to rule the world.
- The "The Three Mountains" Doctrine now makes rulers with the Doctrine more likely to join the Independence faction.
- The "The Three Mountains" Doctrine now makes rulers with the Doctrine more likely to start and back factions for their own claims.
- The "The Three Mountains" Doctrine now locks the Conclave Vassal Wars law to "Allowed".
- The "The Three Mountains" Doctrine now locks the Viceroyalty law to "No Viceroyalties".

Decisions:
- The visibility for the JD decision to become Chinese Imperial is now more appropriate.
- There is no longer a realm size limitation on becoming Chinese Imperial (though you probably don't want to try with a too small realm...).
- The AI no longer needs a ton of prestige to become Chinese Imperial (it still needs as much as the human player would need).
- Mandate of Heaven revolters now get a discount of becoming Chinese Imperial, similar to CI bloodline members.
- The prestige cost for becoming Chinese Imperial now scales based on whether China is held, whether China's holder is Chinese Imperial or Eastern Imperial (or neither), and the MoH rating of the holder if Chinese Imperial, potentially making it very cheap.
- Added AI logic for becoming Chinese Imperial, checking e.g. traits.
- Changed Shinto-Buddhist and Buddhist-Shinto conversion to be targeted decisions working similarly to the intra-Dharmic conversion decisions.
- Removed Tengri Jurchen -> Taoist/Buddhist conversion.
- The non-Grace decisions to hire various JD characters (e.g. Sholar-Bureaucrats) now requires both you and your top liege to have one of the Chinese governments, making it more widely available geographically (it was previously restricted to rulers in the China region or under China) but somewhat more restrictive from a government standpoint.
- Added more robust logic for the above.
- Optimized several decisions.
- The decision for e.g. Chinese Imperial rulers to take their de jure capital is now only allowed for king+ rulers.
- Various decisions to search for/create JD artefacts now check for being Chinese Imperial, having a Chinese Imperial top liege AND the Confucian Bureaucracy government, or having your capital in the China region while also having Eastern Imperial/Confucian Bureaucracy and having a top liege with either of those governments.
- Added more robust logic for the above.
- The Deed to the Dragon Throne is now only usable by feudal (is_feudal = yes) characters.
- Only the holder of the Grand Chancellor minor title can demand that others on their liege's council backs them using the GC targeted decision.
- Grand Chancellor bloodline members cannot ask the Grand Chancellor minor title holder to give up their spot on their liege's council.

Events:
- Removed events related to the Totsuka no Tsuragi being discovered, seeing as they now spawn on game start.
- The Gosannen War events no longer give extra prestige for winning the war.
- The Gosannen War events that should fire for the Permanent Regent should now fire for the Permanent Regent if he exists even if he isn't the regent at present (e.g. if he is on a pilgrimage).
- Improved the AI logic for the Gosannen War events.
- Hachimantaro now can become a friend (or stop being a rival) with the Tenno/Permanent Regent if he hands over the land he gains on victory to them.
- Kitsune and fakes should now spawn more logically.
- Real Kitsune are now rarer.
- Real Kitsune now gain tails more slowly, especially if they have several already.
- Landed Kitsune won't be discovered (and auto-killed) any longer.
- Real Kitsune will no longer kill their friends or lovers just because said friend/lover is a spouse/lover/consort of their target.
- Recessive Kitsune are now slightly more common.
- Being/not being a kitsune is now decided on birth, but it is still only revealed on adulthood.
- More powerful kitsune are now less likely to have daughters that aren't kitsune or recessive kitsune.
- A Kitsune that escapes from jail will now leave her captor's court if they are not her target.
- The former jailor of a Kitsune will now be alerted properly, as opposed to her new host being alerted as if they were the jailor.
- Adjusted the likelihood of different kinds of foreigners spawning in Japan.
- Adjusted the likelihood of different events for foreigners in Japan.
- Improved the AI logic for the foreigner in Japan events.
- Added pre-triggers to several events, and narrowed some things down to playable characters only.
- AI Hwarang joining no longer checks for HF, seeing as the society isn't HF-restricted.
- If you create a Grand Chancellor bloodline through war you will immediately take over the council spot matching your education (e.g. Martial for Tough Soldier) if you are not already a voter on your liege's council.
- Upon creating a Grand Chancellor bloodline you will immediately be given the Grand Chancellor minor title.

History:
- Added Buddhist school traits for many characters.
- Further Fujiwara work; should be finished now (not counting stuff depending on characters from other dynasties, cadets, etc.)
- Fixed some Korean concubine issues.
- Shulü Ping and a relative of hers now have the correct dynasty.
- Weakened Hachimantaro's forces a bit in the Gosannen War; he's still pretty strong.
- Nerfed Jurchen Jin event troops a bit.
- Fixed some FDaTK dates.

Localization:
- Made the mod less "literally unplayable".
- All Buddhist temples are now called temples because of localization limitations.

---
## [Amrabol/tgstation](https://github.com/Amrabol/tgstation)@[770ef81a1f...](https://github.com/Amrabol/tgstation/commit/770ef81a1fb271572d711e7a05dbce62564ca3b0)
#### Saturday 2022-04-02 13:06:13 by John Willard

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
## [Twilight-Dream-Of-Magic/TDOM-EncryptOrDecryptFile-Reborn](https://github.com/Twilight-Dream-Of-Magic/TDOM-EncryptOrDecryptFile-Reborn)@[31721bf093...](https://github.com/Twilight-Dream-Of-Magic/TDOM-EncryptOrDecryptFile-Reborn/commit/31721bf093cabcfbf4efb29e555fbc77d5c3aa99)
#### Saturday 2022-04-02 13:27:14 by Twilight-Dream-Of-Magic

Published project version: EODF-OaldresPuzzle-Cryptic_0.1.0_20220402_Alpha

1.
Follow up on the previous commit [release project version: EODF-OaldresPuzzle-Cryptic_0.1.0_20220324_Alpha] and report on the progress now.
https://github.com/Twilight-Dream-Of-Magic/TDOM-EncryptOrDecryptFile-Reborn/commit/1c5c640efdf1232f2239b24eae9b547c9c3e3740
Commit HASH 1c5c640efdf1232f2239b24eae9b547c9c3e3740

There is no need to change the AES cryptic module at this time, but the Triple DES cryptic module code was fixed today and passed the random data application test.

I'm sorry, the last time I posted the code there were some errors in the code when copying the code for pasting, such errors may be low level, but at that time there was really too much code for me to find it easily.
But by now, that's all happened before.
This time I managed to find the code I wrote wrong inside the code released in this version. In fact, things like this really gave me a headache, and then made simplifications to some of the repetitive steps.

Other algorithms that have not been tested so far are
RC6 symmetric encryption and decryption algorithm

So that's what I'm going to do next, so wish me luck in debugging the code.

2.
Fixed more bugs

发布项目版本: EODF-OaldresPuzzle-Cryptic_0.1.0_20220402_Alpha

1.
跟进之前的提交[发布项目版本：EODF-OaldresPuzzle-Cryptic_0.1.0_20220324_Alpha]并且报告现在的进展。
https://github.com/Twilight-Dream-Of-Magic/TDOM-EncryptOrDecryptFile-Reborn/commit/1c5c640efdf1232f2239b24eae9b547c9c3e3740

目前没有必要改变AES密码模块，但是今天修复了Triple DES密码模块代码，并通过了随机数据应用测试。

我很抱歉，上次我发布的代码里面有一些复制代码时进行粘贴的错误，这种错误也许很低级，但是当时实在代码量太大，我不可能轻易的发现它。
不过到现在为止，那都是以前发生的事了。
这次我在这个版本发布的代码里面，成功找到了我写错的代码。其实这样的事情真的让我很头疼，然后对一些重复的步骤做了简化。

到目前为止没有测试的其他算法有
RC6对称加密和解密算法

那么这也是我接下来要做的事情，那么祝我调试代码的时候有好运吧。

2.
修复了更多的bug

---
## [acramernc/babot](https://github.com/acramernc/babot)@[ae61ed0130...](https://github.com/acramernc/babot/commit/ae61ed013030f9d70fb1379ba3445708747d6984)
#### Saturday 2022-04-02 14:19:57 by KittenMoon

minor fixes and changes to the in depth thing that ias the bot and now all command work goodly wow how many characters can i add before it will get mad at me, it seems that there might not be a limit but who is to say, i wonder how this will look with the vs code github who commited what extension, alas i will now infom you about jobless reincarnation- it is a good watch and i cant wait for season two but i am sad there will be less Eris in it but that just makes the scenes where she is in the episodes so much more special (i tell myself), well it is 1:36 am on mar 27th and tomorrow will be the big day that hank will update the bot to slash commands and it will be done the day after he had to write a paper. fold orbs. i cant waiut for s3 of dr stone as well but i will spare youi the details ats it is getting cold in here due to the wind. now when adam sees this he will probably go insande but alas it is fine. this is a second go at this commit because i realized it could be longer and i wanted to make it as long as physically possible ecause it owuld be funnhy. so iu also wont remove spelling mistakes lioke yoy just saw, unless it makes the word unreadable , i have standarrds, low standards, but standasrds none the less.. to whomstvst that is reading this, good work getting to here as i am realluuy rambling now and it is good. !baba please is working well and we have only gotten one Nice from it so far but im sure there will be more in the future. Today i was grading labs and Bennis decided to send a .pages file and those who get my pain should understnad that it is not easy to open that and i had to just put it off untl the morrow days (aka Mar 27 during the day). But it is fine, i may have forgot that genshin has been open for the past 9 hours but it is fine. Bikus. see i had to get that in there or it wouldnt be a message by me, which reminds me, Nw forgs sponsored this commit message, make sure to look out for NW forgs sponsored content coming soon. so, how is your day person who is reading this, mine went well, i went to the store to go Schop Schoping (read in swedish accent) and had lunch then did hw, watched yt, and coded the code you see somewhere nearby. Speaking of code, hey buddy 🔪 has decided to make my life a living pain as the cube wont scale correctly but it really isnt too bad as i am ahead of the class by a bunch so i can take it slow and smooth. ඞ! suprise mogus! back to hey buddy rant: i will just ask him what is wrong on monday but the problem is my class ends at 12 and his office hours are at 2:30 so that uis 2.5 hours of waiting (2 if you subtract lunch). oh boy is it windy out, room at a solid 57 degrees, which is nice. i should end this rant soon but i dont want to do that becuse i want to write mor words than hanks whole paper into this commit message. ok back to jobless reincarnation rant: so the first few episodes are basically the main charcter learning how to do magic in the new world he is in as a child, he also has a special ability to do chantless magic (most magic requires spells), so the family get him a tutor and she is a demon who teaches him how to better hone his magic abilty and he soon passes her. she leaves to the main characters disaray and then he finds a new friend who he first thought was a guy but was a girl and they become friends after a rocky start. she can also do chantless magic which might be someting for season 2 but idk, ,my one friend said something about that. but back on topic, he asks hsi parents if he and her can go to magic school but the dad says they dont have to money for both so the MC (main char) says he will get a job to pay for it. so the dad does what any norrmal dad would do, knocks out his son and sends him off wiht a beast-woman (member of beast people, comes bakc later) to train a bratty (but best character) girl magic oh and the beast girl. the first day results in a kidnapping that was supposed to be staged but in the end it was an actual kidnapping for ransom but both MC and main girl got out alive because beast woman saved them. Then months pass as they train and get better with magic and there is a bday party for the girl after the MC had to help teach her to dance. at this point in the story main girl doesnt like MC that much. then there is a 10th bday for MC and he gets a new staff as he is a mage and it helps enhance his magic, aorund this time there is a magic orb in the sky that no one knows abotu that much, we skip ahead to graduation for main girl and beast woman and when MC goes to cast the cumulonimbus spell there is a massive explosion from the thing in the sky and it causes the MC and main girl to teleport together somewhere, the beast woman also gets teled but somewhere else. They wake in the demon lands next to one of the demons that were told to eat people but he is actully not that bad and they decide to travel together to get out of the demon lands. first they stop at a nearby village which is home of the mage teacher thath MC had a few years back. They then travel on the way to a city nearby where they will go and sign up to be adventueres. when they get to the city they realize the demon wont be able to enter due to being hated so they dye his hair blue and hide the forehead gem on him. while there the MC is visited by the Man god in his dreams and is told to take a quest to save a pet, this leads them meeting smugglers which the demon kills one and the MC gets mad and tells him that wont clear the demons kind's name. so they then go on a quest to kill a snake and due to the MC hesitaion they witnesss a fellow adventurer die. this leads the MC to second guess himself but they still kill the snke, they head back to the town and the horse man tries to extort them but they dont take kindly to it and the demon shows who he really is then leaves the town. later the MC and demon agree to work together and the demon shaves his head to blend in. then then travel across the demon lands to the nearest port town where the demon is the reason they cant cross on the boat as he costs too much to travel. that night he is met by the man god again and due to that he goes off on a solo adventure that day while the girl and demon practice fighting. he then meet shte demon queen and she gives him a demon eye which lets him see seconds into the future and forsee events to come. he then meets Gallus by saving him due to the eye which helps him get a way to get across to the next continent. INTERLUDE TIME; we go back to the start of the day where we are now in the mage teacher POV with the elf and dwarf. the mage girl goes all around town looking for leads on what could have happened to all of the MC family. she explores the town that the MC is in but due to conincdences they never meet. the alley w/the demon queen and when the others are training could have been when but it didnt occur. So they make it to the new island and when they get there as a deal made with the demon, who hates evil people, they would defeat the smugglers who helped them get here. they saved the beast children and the sacred beast (a big dog) but when the MC was saving the dog, the people from the beast village showed up and they took the MC into prison for many days. but then there was an attack on their village and the MC and his innmate (who will be important later) get out and help the beast people and save their village. then the main girl and demon come back and then they live in the beast village for a while. the main girl helps train two of the children who they saved and coincidentally is the family of the beast woman from the start of the season. they had disagreements about her as when she left the village she was not a good and well manored person but that is not how she is now. months pass as they get trapped by rain at the place and train for that time, but then it is time for them to leave for the capital city. They eventually get to the capital city and they decide to seperate for the day as they all think it is good to stay and raise funds for their adventure back home. the MC goes on his own way and the demon and girl go on their own ways as well. *the girl has an episode at this point but it was just released and i have yet to watch it* so back to MC: he finds a child being kidnapped and goes to save it but there is complications as he runs into his father Paul and they have a not so good reunion as he says that the MC is having way to much fun when he should be looking for his family. this leads to a fight and they go back home on their seperate ways. flashback to the explosion from earlier and we see how paul and his daaughter are together as it hits them causing them to teleport somehwere and they end up going home seing it is gone and posting flyers adressed to his family and friends to help find each other. this results in him eventually going to where he is now. he then talks with another person (same dude who was in the cage in beast lands) and he explains that paul and MC are family and they shouldnt be fighting like this. They both go to a bar together and redo their first meeting which results in them being on better terms, like a father and son shoudl be. They then go on their seperate ways and the MC taks a ship to the main continent; INTERLUDE- cutting back to the mage girl, we see she is back at the town in the demon land talking to the horse man, who was her former traveling compainion, and then she goes back home for the first time in 20-50 years (this type of demon lives very long and ages SLOWLY). she gets there and is hesitant because she left as she cant use telapthy like the others but then goes to her family home and they dont hate her liek the thoguht. this leads her to stay and learn about the MC's travels and what he is up to. back to MC and he again has a dream with the Man god who tells him that how to save his other sister and their maid (odd family tree, we wont get into it) and then he goes and does it but it leads him to the castle where he thinks his former master (the mage teacher from just a bit ago). he then gets captured as the corrupt prince hopes to get the teacher to come back but he is able to escape thanks to the prices brother likeing the MC;s figures he makes. They then save both who they were trying to save and it resulted in them parting ways in which the maid went to head to paul. brief introspection: the sister disliked her brother (she was 2 or 3 when the tele happened) but the MC (brother) saving her helped rekindle that relationship. They continue on their way into the dragon lands in which the demon and girl freeze up as the dragon man shows up. he is ominous and causes peiople to be scared of him due to a curse he has on him. everything was going to go fine until the Man god was brought up and it caused the dragon man to try and kill them, he basically did kill them all and in the semi dead state the MC talked to the man god a bunch about how he didnt want to die from this second chance at life. but then he wasnt dead because of something the dragon mans assitant said to him and he revived both him and the demon who was basically killed. They finally reach their home territory and and see how everything was destroyed as said by paul due to the mana explosion. they bid farewell to the demon at the MC hometown area as he was able to fufill his promise of getting them home safely. then they head to the girls town and see it is a refugee camp and they meat the beast woman again. it is confirmed that the girl is the last of her family as her parents died in the teleport and her grandfather was blamed for it all and beheaded. the girl goes off to be alone for a bit and the MC goes to think of what to do next. they then do some stuff and then it is the next day and the MC is very estatic to start the next adventure to find his mother. he then relizes that the girl is gone and goes to ask the dude in charge where she went. he says she and the beast woman went off on an adventure to learn to be independant. the girl also cut her hair (imo not pog, but alas). this causes the MC to recolect on his past life and how his shut in nature is coming out again after he tried so hard to start anew. while he recollects on his life sulking in the bed we see glimpses of all the characters who he helped along the way. one being the mage teacher who watches a beer chugging challenge between a demon queen and a dwarf. to suprise the demon queen wins but cant afford to pay for it but before anything bad happens the mage teacher pays for it which gets her a favor from the demon. she asks the demon to see the MC family and where they are finding that most are safe except the mom who is in an unknwon location and she cant get a lock on the MC (theory about this after). cut back to the MC and we see that he is still the big sad but the thought of his mom breaks him out of this where she wouldnt want him to be a mopey. then we see him leave the tent ready to go on an adventute. the final scene is a scene of the girl he became friends with as a child much older in some unknown place. and that was the story of jobless reincarnation season 1. now the theory i have is the MC has a curse/blessing (smae thing just positive/negative) that he cannot be seen by others using magic, as the dragon man didnt know of his existance while knowing of his compainions and the demon queen didnt see him when helping the mage teacher find his family and him. but im sure we will find out eventually. now the time is 2:47 and as you probably see it is over 1 hour since i started typng this commit message and i have no reason to stop other than if i get really tired. so i guess slash commands they are pretty cool but whos to say. the bungle bus would be flying right now and i wouldnt have been typing this if the space engineers server was up but alas it is not :(. so i converted this commit message (well everything before i say the time) into a double space times new roman 12pt font word doc and well, 6 pages of text, oops, i may have over explained it but to anyone who read it good job i guess i spoiled the show but those who are in this baba project with me wouldnt watch it anyway. also i assume if they woudl it would they would stop when i said i would go on a rant ¯\_(ツ)_/¯. i had to get that from a slash command on disxcord, very topical to this commit. hey i guess i should do the daily wordle soon or i can jsut do it when i wake up tomorrow but that would be more logical and i am not logical as u see i am writing a book as a commit message. whelp my headphoens are low battery which means this commit message will ahve to be sent soon, but i may come back in the morniung and append onto it more, all until hank returns from work and we do the great baba slashening which will be a bit of a pain. !baba please be simple. i see you asking why is this so long, what went thought this mans head making him go, ima spend 1.5 hours writing a commit message, well you knwo, idk what to say to that as even i, the one writing this dont fully know why i am doing this but i do know that if my headphones werent dying i would possibk explain a full or partial rant about dr. stone. have you heard about the great cup of gilgamesh well it is a nice cup. also make sure that your orbs get the propoer folds when dealing with them, ah that reminded me of hey buddy and the program i need to work get working, thanks me. the temp in the room is now 55 which is nice but for some reason it feels warmer than when it was actually warmer, mahybe that was due to me no having typed a full essay back then but who is to really say. see i cant write a paper to save my lfie but i can rant random words for a long time until i have nothing to say. so how are YOU. yeah you mr. i have read this full commit message and regret it so because i wont get back the [insert time spent] [insert time type] back. so i have had this same song on loop for hours now and well it is very peaceful as a background song. NOOO i am now alone in the discord after both Bob and Isaac left without warning :(. well i guess it could ahve been a netwrk issue but idk i guess i will just continue my rants. this song is very entertaining and it be real nice. the wind is still roaring outside like it was back a bit ago and it do be loud, there was a very loud wind noise last night that woke me up but luckily i was able to fall back asleep due to only getting 5ish hours the niught before. well my time might be coming to a close as i am getting tired (not of ranting, i could go much longer but tired as in low wokeness levels). if you see a message saying - ha im not tired - but in all caps that is where i will continue tomorrow (that is if i remember to start it that way) even so it will be obvious. would u believe i have genshin still running ,yes, well i guess that is normal for me. i guess i should actually close it, there i closed it, are you happy, well now i am actually going to go to bed at the time of 3:08am, i bid you a morrow (maybe there will be more) Ha you are correct there is more and now that it is a new day i have new motivation to continue this as the alternate is that i would be grading more labs which i know i should do but Bennis is causing me issues witjt rhe .pages files still but alas. also the info sent to me was not the most accurate so it takes energy to think and i just woke a bit ago, now the sauna mode is being enabled by dumbo boi and but i cant just go turn off the warm as he is out there so i must wait a bit of time, alass. baba haikus now work as intended for dates, idk if i included that in here but if i didnt then well here it is now. so for you it has been only moments but to me it has been a whole night since i wrote the jobless reincarnation s ummary, i regret nothing that i did last night i may have been a 'waste of time' but i had fun, it is the rant i wanted to give but no one would listen so now it exists in text form and if thou wantst to hear the audio version i shall give the rant at anytime. if you get to this part send a 'real frog bungus' in general, and i will know :) ---- so the temp in the room is at 57 again but with tthe heat on it will not stay so nice for that long, i can feel it on my fave and it makes me the big anoyed. when i commit this fully it will great but that time has yet to come as i still have the rant ability going and i aint stopping it anytime soon. i can feel the text box being slower as it has to hold alll 17k+ characters before this and however many more that there will bit in the future. well as i was saying last night somewhere in that rant. i should probably do todays wordle, the hank version that it. Wordle 281 3/6 🟨🟨🟩⬛⬛ 🟨🟩🟩🟩⬛🟩🟩🟩🟩🟩, there you go the wordle. you should know that that isthe first thing that has been copy pasted into here (other than the two emois) as this whole thing has been typed out character by character by me with no prefoming a Daniel (copy-pasta). i think i will keep going witht this rant for another day or two if hank ends up not being able to update tonight as he hasnt slept in over a day due to a paper that he must write, and tomorrow there may not be time for the update meaning the slash commands update will end up being on the tuesday this week. speaking of tuesday that is the day of the genshin update and oh boy am i excited, only downside is that i will only have 2 ish hours to work on it as i got class at 10 so i must sleep by 1am. but oh well i cant wait for the chasm and what it has to offer up. also new story quests and archon quests that will potentially get done later this week, i can hope as long as there is no hw/labs to deal with more than i already have which knowing my luck it will end up happening. alas, 🐸🐸🐸. hey we just hit the jobless reincarnation part of the song i am listneing too, nice!. baba told me one, how are you feeling, and i told him, that i am feeling like taking a flight in the bungle bus, ha i got you this was just a ploy for me to mention the bungle bus and it worked. the end of the song is occuring and it truely is a bop. so the plan for today is to do hw/lab stuff, and then do the baba slash update that is if hank isnt sleeping when the evning comes and adam hasnt gone to sleep too when he wokes up. so i hope that genshin gets an update to 3.0 in the next update (not the tuesday one) becasue that would be super great. it would also line up to where i would be done with classes at that time which would allow me to deal with having time to do the genshi update while also having time to do summer shows 2022, which hoepfully that show list will be on par or even better than summer shows 2020 and much better thant the dreaded summer shows 2021 which was like drinking bleach, in reality it was watching bleach but who is keeeping track, oh wait i am. but the good thing is i have no promises to bleach so i will end up hopefully doing a narrowed down spring break scheule as i hope to get through 24 episodes a week. the good thing is if we corelate it to the summer of 2020 we see i watched a whole GTARP livestream each day and still had lotss of time for shows so i have hope for goodness but we will see what the scheidule will be. currently i must finish slime then we can start the true sthows list which includes AoT, Fate movies, drss up darling, and more hits. it should be good. i also would like to see the air date for job re. s2 to be annoucned so i can get hyped for its inevitable airing. mayhaps over the summer i will also watch the OVA but we will see as i need to time it correctly. as you probably can tell i am starting to run out of ideas for what to add here but that is not ture, as i could do another long rant or short one on dr stone like i said i would which depending on if adam gets done with being at the jesus shack teaching the children about NOT frogs then i will have time to do the rant. ok here goes nothing, see unlike job re. i watched dr stone back in jan 2021 and s2 in august so it isnt as fresh im my mind so it wont be as detailed. so we start off on some day when the main character the scientist is at his school and his best friend is about to ask out a girl. then a giant green wave covers theentire globe which causes all the people to instantly be petrefied in stone. 3700 years pass as everyone is still ins tone but the main char wakes due to a chemical reaction occuring on his body which results in him having to live in this new stone world. he then finds his friend and saves him and the girl as well. they live their days out in a trehouse tying to find the best way to save all the humans which in the end they figure out. they then save the stongest student at the school and he has different morals and doesnt want to save all of humanity as there were too many corrupt people, time passes and they end up dueling which the stong man kills the main character but because he is smart he was able to be revived due to being still partailly petrefied on his neck where it was broken. this leads tohe MC to sperate and MC goes alone while the other two go with the strong man to keeep the illusion he is alive. the Mc adventures out for a bit and finds humans living in this world who are decendants from someone but he doesnt know who. they are skeptical of him and his science but they show him to their local 'scientist' who they work together to bulild a kingdom of science. the next part of the adventure resolves around trying to make a drug to help cure the sick of the village and earn their trust but they need helpers so they make food that is unknown to the people of the village which works to persuade them to help. a man from the other empire shows up and he is going to report to the empire about how there are people and they need to bedestory but he is persuaded not to by the fact that they have so many inventuons including light. andas he is leaving he requests one thing: a cola. they continue on their creation of the drug to save the villagers but in order to be able to give it to the sick they must get through a tournament arc which results in the MC winnning and becomeing the new chief of the village, the reason for the competing was because of needing alcohol whcich would be used int he drug being made, then they give the drug to the sick and after a moment of panic all is well and the village accepts the MC as one of their own. but in a plot twist the village name is named after the MC. we now flashback to the past when the MC was young and he was with his adoptive father and how he wanted to be an astronaught. over time he was able to go into space and on this mission there were 6 people up in the space statuion. days pass up there and all is going well when the petrefecation bean goes off and they do not get frozen but all communications are gone. the mc father decids that the best bet would be to return to earth and try and recover all life somehow. cpntinuing with the past we learn that their re-entry is not so smooth but they all successfuly make it to an island and that is where they will be living the rest of their days. as time passes each pair get married to each other and they have familys there but when one gets sick then dies the russians deide to try and go to the mainland to get mediceine but are never seen from again. the father decides to write 100 tales to tell the decendants to keep huminty alive but tragically his wife dies when he finishes writing them. back in the future we see the Mc at the grave of his father reminising and vows to keep alive the science. then the cola person shows up and says the empire is planning on coming to attack. they send a strike team and due to their science advancements they are able to hold them off and also they give cotton candy which appeases one of them for now. they end up celebrating christmas a bit due which improves their morals and after an event int eh cave they end up making a room and telescope for the MC as a birthday gift. finally as the season comes to a close they decide to make a phone or a primative one to be able to communitcate witht the allies they have in the empure. in this the MC learns they have the term speaker as a bee whiuch leads them to investigate the grave of his dad and find a recrd in there which brings to lite somethings and a some left by the girl who was a singer back then. then they have to make a second one but that is doen between seasons . season 2 starts with them making instant ramen based on what they made before. they end up taking the second phoen to the enemy bas e and hide it so they can communitcate with the allies, there is a hiccup in there is aguard but she gets convinced because of the music from the end of s1. they then plan on making a car of sorts which can be used as a tank as well to storm the base and save their allies. basically the rest of the season they go to save fight the empire they win the leader admits he is wrong but is fatally wounded and needs to be put into some form of cryo sleep which is done. also we learn that the girl was saving all the people that the evil leader was 'killing' and that she could save them 100%. and that is a rough summary of what heppended, it could be more in depth and s3 isnt until 2023 but at lead thtere will be an interplaced epiusode sometime this year.. so now you have read two, yes two summarys of shows i have watched, if it wasnt for the fact that this text box was getting visibly laggy to type in, i potentiually would do a railgun talk but i will spare you the hastle and just say, go watch it, it is good. fun fact the slash commands update is coming one day before the birthday of babs on the server which occured 3 years ago. wo wow has it really been that long, it was also the day we added haiku bot to the server, good times good times., well, i think this is the end. of the commit message that is until next time when i feel the need to do this again, but getting it this long a gain will be HARD but we do have many shows i can go though and there will be many more i will watch, just see job re. s2 i will have to over explaint hat one too. so unless you see more after this as in i felt like continuing later today, i bid you a morrow for this message. ---- well well well, looks like i am back to type some more as hank was too sleepy last night to update the bot. so now i am in my class typing more on this, learning about compliments of turing machines. today eneded up having no class with hey budward as he has a stomach bug and didnt show today so free time is nice i guess but the only down side is no ablility to ask him the questions in person. so i guess email will be the way to do it. i have yet to eat lunch today and am the big hungry and the frogs are wanting to be fed, that probably makes no sense but to those who know, they know. good thing is i will speedrun lunch, then go to apartment and do some more lab grading which should be 'fun', oh boy i cant wait, well i may watch some YT before that as i would like a break from brain being used. it truly is real frog hours. i did end up having to add a change to baba today as there was a bug with the eror frog and at least there is one good thing to not being able to update the bot yesterday. but still i would like to do it today but cant because the one the only adam is too busy with work and his other activity in the eve of the day.today has been fairly windy and as i predicted last nivght, i was only able to wake today because i went to bed early because oh boy was the bed cozy in the morning. dj bungus is the driver of the bungle bus. today lunch will be chook fi loo and oh boy will it be good to have food after not having breakfast. see i gotta get the amount of characters in this to over 30k which would make it a nice even amount and also be very satisfying. but we are about to go into group work soon so i will have to take a break from the typing here to 'work' on problems with people. will i contribute, probably not one bit as idk what is going on. of the three classes i am taking hey buddys is the only one that peaks my interests while the other two are good but not prime time mime crime time classes. whelp we have gone over 30k swimmingly which means i shall be gone for now and if this is the end then goodeth morrow until next message. --- well looks to be that  i have added all the admin commands as slash commands now, who would have thought that, but it will be pused tomorrow which will be in the evning wait tomorrow is tuess so i am free all day whcih is pretty poggers. ok that was all fro my update so see you again mayhaps perchance idk. --- ok today is the day of the bot upate, we shall be getting anew command system and all that stuff., also i have an update on the hey buddy program stuff which is that i passewd all the tests and now am done with the lab. so tomorrow gonna be a smmoth sailing day of peach and prosperity with a little bit of frog. now genshin is in the update stage right now so the ext few hours will be me doing not much as i wait for the changes to occur, we will see as the update has new stuff including the chasm. i will do a single 10 pull today possibly but if i wait until friday when the new month arrives i will not use as may ruples, but then again i will new use the same amount so it really doesnt matter if i wait or not as i will want to do a 10 pull anyway. so i want to get me some dinner but that would involve moving from my chair which is nice and cozy., the soluction to this issue is having some of the snacks on my desk which i might as well do right now

---
## [acramernc/babot](https://github.com/acramernc/babot)@[183d89af66...](https://github.com/acramernc/babot/commit/183d89af66503ebf9b4ec4dac851c4101537b2d5)
#### Saturday 2022-04-02 14:19:57 by acramernc

Reverted back from type:module bs (I hate my life)

---
## [Dreadmoth/pcsx2](https://github.com/Dreadmoth/pcsx2)@[d6684efd26...](https://github.com/Dreadmoth/pcsx2/commit/d6684efd262ef1c83d37c50b48edc478952dddf9)
#### Saturday 2022-04-02 15:22:40 by RedDevilus

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
## [gmoshkin/ergodox-layout](https://github.com/gmoshkin/ergodox-layout)@[63b27e9e45...](https://github.com/gmoshkin/ergodox-layout/commit/63b27e9e4510e15d6c97404f25380b22e34ab910)
#### Saturday 2022-04-02 16:00:54 by Georgy Moshkin

actually this stuping fucking keyboard is unusable without retro tapping

who the fuck thinks it's ok to drop the key combintation if it's pressed
and released before the tapping timeout? How fucking slow is everybody
typing? and the fucking code is unreadable, i'll have to spend a week
trying to figure out the places i'll have to change to make this stupid
fucking thing working properly, or I'll have to leave with retro typing?
jesus fucking christ please kill me

---
## [amidoingitright/Skyrat-tg](https://github.com/amidoingitright/Skyrat-tg)@[d96e7b7e27...](https://github.com/amidoingitright/Skyrat-tg/commit/d96e7b7e278dd0226a4de8d9463edda37af709f9)
#### Saturday 2022-04-02 16:12:11 by SkyratBot

[MIRROR] Makes Ants glow, puts a min on ant screaming & shoe permeability, & other ant-related things. [MDB IGNORE] (#11821)

* Makes Ants glow, puts a minimum on ant screaming and shoe permeability, and other ant-related things. (#64786)

I found out how emissives work and my first thought was "damn ants should glow that would look sick"
So now they do.

Also, having less than 5u ants in your body will make you not scream, so 0.0001u ants will no longer have that tiny chance of making someone scream for their life.

If an ant pile has a max damage value less than 1, then they won't be able to bite through your shoes. This is the same threshold as the second tier ant icon.

Makes the giant ant a hostile mob with the neutral faction, meaning they will attack anything not in the neutral faction.

* Makes Ants glow, puts a min on ant screaming & shoe permeability, & other ant-related things.

Co-authored-by: Wallem <66052067+Wallemations@users.noreply.github.com>

---
## [ForestDragon-wesnoth/1The_Great_Steppe_Era](https://github.com/ForestDragon-wesnoth/1The_Great_Steppe_Era)@[b3c92279a4...](https://github.com/ForestDragon-wesnoth/1The_Great_Steppe_Era/commit/b3c92279a42ecedc9ea38cf0654a672d46e1d67e)
#### Saturday 2022-04-02 17:03:46 by ForestDragon

tried to fix bug, gave up

this is fucking bullshit, I hate the new lua changes

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[093602d794...](https://github.com/treckstar/yolo-octo-hipster/commit/093602d79442d2da2ed03c004dce7680e1adfb50)
#### Saturday 2022-04-02 18:00:04 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [newstools/2022-naija-news-agency](https://github.com/newstools/2022-naija-news-agency)@[b91cc0d4c6...](https://github.com/newstools/2022-naija-news-agency/commit/b91cc0d4c6370873ac30bb3379f13e6b5e04aa24)
#### Saturday 2022-04-02 19:10:40 by Billy Einkamerer

Created Text For URL [www.naijanewsagency.com/tension-as-lover-boy-accosts-his-cheting-girlfriend-at-a-nightclub-in-lagos/]

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[ae29380394...](https://github.com/mrakgr/The-Spiral-Language/commit/ae29380394dbdda48a6a2e839a8c89426371a783)
#### Saturday 2022-04-02 19:17:14 by Marko Grdinić

"12:10pm. I went to bad at 1am, but I slept very well. I even had time to lounge in bed.

Yesterday I did a bit extra and figured out how the gradient works. I've had time to think of how I will do the patterns.

12:30pm. Let me have breakfast here.

1pm. Virgin Road and then I'll do the chores.

1:15pm. It was pretty good, I'll make it one of my follows. It seems the op is by Mili.

1:25pm. Let me do the chores here. After that I will get started.

1:50pm. I am back. Let me take a breather.

2:05pm. Let me rant a bit.

During the night I started thinking about AI again. Putting all my knowledge together, I think it is absolutely incredible that evolution works at all given how weak its reward signal is. It is beyond belief that it could end up working as focused design, as if it had a library of components it is experimenting on. At the bottom all it has are genes which aren't that much different from binary.

So the conclussion is that even if the backwards reward propagation signal is abset, the reason it works is due to the powerful biases on the forward pass.

For some reason, death acting as the edit button has enough power to push evolution forward.

It seems simpler than how the brain works, but maybe actually understanding evolution has a higher difficulty threshold than it.

2:10pm. The brain is obviously different than evolution. The only thing I can be certain off is that it takes in sensory input and builds representation of that.

So far, the artificial systems work based on backprop which acts a credit assignment and optimization scheme.

I thought to go beyond it and came up with reversibility.

It makes sense to some degree, but it is not enough.

2:10pm. All the artificial systems of today are immitating form over substance. The evolutionary systems have selection, but not the impetus that drives evolution forward in nature.

With backprop the currently dominant approach, I see people looking for evidence of it in the brain. The brain has feedback connections and there are actual conjectures that might be random.

No, absolutely not!

It is much more likely that there is profound meaning in everything the brain does.

Artificial nets of today have random initial connections, little thought is put into why messages are sent forward. The brain sends spikes forward and so do the artificial nets, immitating the form, but not the substance to some real world success. Just enough to get the hopes of fools up.

The biological brain might be using random initial connections, but there is something to it.

Something beyond backprop and beyond my limit of imagination which is reversible systems.

Just what could it be?

2:20pm. Of course I do not know, but the more important question is how do I find it?

Is there a single system in nature I could use as a template for understanding the brain? Is there a way to do it without cracking the skull open to dig out its secrets?

Just how do I get the inspiration for it?

I can't think of anything else in nature but the brain that has independent units communicating with each other to accomplish arbitrary goals.

It seems easy when you have people doing that, but it get much harder when you have to write programs that do that.

2:20pm. I can't think of anything at all to figure out the minimal computational component of intelligence. I just have no inspiration.

I have no power.

The me in high school thought that if I could figure out power it would be an enormous power, but in the end I am just as powerless that I was then even if I have more drive. Two decades of experience makes no difference.

I have so much more knowledge, but I do not know the one thing I need to know.

2:30pm. It is something I need to accept. For those without power, the punishment is to work. I have no power, so the only thing I can have is perseverance.

Maybe I'll get a second chance. The problem is this computer. It locks me into a sequential mode of thinking. If I was programming a processor with tens of thousands of cores, then I would have incentive to do research how to use it. My current CPU only has 4, and even a Threadripper would only have 64. That is nothing.

GPUs have many cores, but regardless of the hardware, they are crippled so they conform to the sequential paradigm. A GPU might be parallel, but you still control it by writing sequential C code.

A proper piece of hardware would force you to pass messages around.

But I do not feel like forcing this.

If I am going to get my power, it is really important for me that happen as a result of following the proper path. I could get that Grayskull, and what then? I would still be in poverty, doing things I do not want.

2:40pm. The right path is to get that kind of hardware and then pick a goal that utilizes all of that concurrency. Rather than cracking tne skull, do it through sheer programming prowess.

Today's ML systems might be useless, but I do not think that matrix multiplication will go away. I think that it will turn out to be a vital component of tomorrow's memory systems.

2:45pm. So back to art.

Yesterday I put in some overtime just to figure how gradients work. While messing with texture sizes I realized something. Even thought 4k textures seems to be the max I could select in Pt, it is just as well, because going any higher would kill my right.

With 4k, it takes me a dozen of seconds to save what is a 700mb file. It still looks grainy up close.

2:50pm. At this point I realized something - texture images have horrible scaling. Imagine if I could use memory system to compress them. It might seem ridiculous, but at the 4096 * 4096 size they are huge. Way larger than the average NN layer.

2:55pm. If I am aiming to be an artist, maybe finding ways to compress art and geometry would not be a bad way to stay in the ML game once the appropriate hardware gets here.

Sigh. I have no idea where the world is heading at this rate. I am thinking the TensTorrent talk. All the AI companies just want to build big racks of AI chips. Just what is going to come from that? Who knows? Is anything going to come from it at all?

Does modern ML really have that big of an economic impact to warrant all this hype? Most likely the attention it commands is undeserved, much like how Bitcoin is taking up 1% of the world's energy generation.

I can just ignore it for now. It is not going to be that easy to crack this problem. If by some miracle the algorithms get discovered that could only be good for me.

3pm. Until then I can only sharpen my will. I've decided - I'll accept my place at the bottom until one day I get my power.

Now let me start.

I had time to think about what I need to do.

3:05pm. I'll admit for doing this kind of radial pattern, I thought of downloading Substance Designer. I thought about doing it in Houdini using toruses and then baking it. I thought of maybe doing that same thing in Blender.

It is not a plain pattern, but it is a bit distored along one of the axes. I've looked into whether something like that would be possible to do in Pt, and came up empty. Maybe it is possible, but I am leaning towards it being unlikely after that bit of research. I might have layers in Pt, but I do not have UV noise.

3:10pm. I've thought about those lines, but then I remembered the Mari video, and thought what if I painted on a pane glass and gradually deformed a line to get the kind of result that I want?

That could be really promising.

I discarded doing it by hand because doing these long lines that are next to each other would be hard even with lazy mouse.

3:15pm. Therefore, to start things off, I need to figure out how to use stencils in Pt. This is the natural mode of painting in Mari, but in Pt I'll have to figure out how it works first.

Do I just need to activate projection painting? I doubt it.

https://youtu.be/_-bHx6ZWgng
Using Stencils in Substance Painter

Let me start with this.

https://youtu.be/_-bHx6ZWgng?t=186

Yeah, it is something like this, but how do I draw on a stencil?

https://youtu.be/_-bHx6ZWgng?t=277

What are levels? I'll have to figure that out at some point.

https://youtu.be/_-bHx6ZWgng?t=516

Using the screen layer to just add the white is not a bad idea.

I also need to figure out what the anchor points are.

3:25pm. Let me ask in the /3/ thread whether it is possible to pain a stenchil like in Mari.

3:30pm. Alternatively, I suppose I could figure out how to do this with layers. Maybe I could use the pass through layers to warp the layer below. Or maybe I could copy the layer below - warp it, and then recombine it. That could be interesting. Is it even possible to combine the layers like in CSP? It should be, but I'll have to figure out how to do it first.

At any rate, I've slept well, and I have just the right amount of stress today.

So let me not focus too much on getting the job done. The desk wait, and in a pinch I could always get a job as a programmer.

Rather than concern myself with immediate needs, let me thoroughly educate myself in the use of Substance Painter. Even for just CSP, which is a 2d app, I spent months studying it.

Surely I do not expect to master Pt, in a few days. If I want to reach my full potential with it, I should just dedicate myself to it.

It do not need Designer or Houdini.

I do not want to be the Houdini guy. If I am to work on art programs, it would be using AI chips to compress textures and write raytracers. Those sort of projects. Otherwise, I'd like to use my hands. Houdini is only good for motion graphics, not creating the kinds of environments or characters I want.

3:45pm. Ok, let me bore myself a little by watching tutorials. I'll do it the way I started.

https://substance3d.adobe.com/tutorials?level=0&software=Substance%203D%20Painter

I am thinking what to do.

What is this SpaceMouse thing? It feels like an ad, more than a tutorial.

https://substance3d.adobe.com/tutorials/courses/3Dconnexion-SpaceMouse-in-Substance-3D-Painter/youtube-PvZYHYQ3_uc

This seems pretty cool.

https://www.youtube.com/watch?v=WUa0ZJt2nOo
2 Years Later: 3DConnexion SpaceMouse Review

Let me watch this.

After that...

https://substance3d.adobe.com/tutorials/courses/First-Steps-with-Substance-3D-Painter/youtube-mv6pg1O9vEQ
FIRST STEPS WITH SUBSTANCE 3D PAINTER

I watch this before, but how about I follow it from the start? I thought I did not need it, but instead of being lazy like that, why not spend the time to go through the tutorials methodically. There is a whole bunch of them on the site.

Nevermind this mouse ad.

Let me start the RollerSkate project.

It sure looks nice. Let me start the first video.

4:05pm. Hmm, if it is something like position, why did I bake 4k textures for that? Wouldn't low res interpolation work just fine for that?

Yeah, it would and the case should hold for the rest of these baked textures.

4:10pm. I am thinking back to that stencil tutorial. Instead of setting the layer to screen, couldn't he have just set the brush to that or maybe lighten?

Let me take a short break.

4:30pm. Let me resume.

https://youtu.be/mv6pg1O9vEQ?t=293

Ah, it is a good thing I've decided to take the slow route. I completely forgot about the geometry masks. As expected, being patient and going over the tutorials methodically is the best way to learn once the motivation has been established.

I wonder how these geometry masks are created. Since they have a name I am guessing they'd have to be separate objects in Blender.

5pm. Right now I am looking for UV Pack Master on Persia and am not finding it. I won't really be able to use the Kitbash kits here unless I pay for them for Heaven's Key, but there is nothing stopping me from using them until I make money and then paying for them later.

Getting a RapidGator or AlfaFile account might be well worth it so I can get extra assets.

https://glukoz.gumroad.com/l/uvpackmaster3

Name a fair price. I guess I could get this for 1$ if I wanted to. No, it seems not.

Well, 39$ when I get started won't be too much.

Forget about it for now.

What I need to do is methodically increase my skills. Even if I just end up kitbashing in Clarisse and doing some sculpting in Blender, I still want to do this properly. I can't have overly glaring holes in my skillset.

5:05pm. Let me go back to the tutorial.

5:15pm. Since I am wondering about it, how would it be possible to use the grabby behavior in Blender to navigate.

5:25pm. The navigation setting has it all. I just have to change it to trackball and zoom to mouse position. This was really annoying in Houdini, but it really hurt me to do those small selections when I was constantly zooming to center as well as turntabling based on focus.

I think the Houdini way is superior, but back then I only didn't have the feel for it.

Right now, it feels like it just clicked. Having skill is being used to small things like this.

5:35pm. I've gotten sidetracked. Let me focus on the task at hand.

6pm. That was interesting. Part 1 is done. Let me move on to part 2.

6:05pm. Had to take a breather. Let me start with part 2.

6:35pm. Done with part 2 just in time for lunch. Let me take a break here.

7:15pm. I started reading Machimaho and I really feel like stopping for the day, but like hell will I accept just putting in 4h of work. I'll continue forward until I finish part 3 at least.

It really is hard to pry yourself off manga once you start feeling good and get into it. But I will manage it.

7:50pm. https://youtu.be/iBgVVr5gIww?t=608

The way he is doing this is somewhat amateurish. He should have just made sure the rotation is straight 90 degrees. Then used the geometry mask so it only appears on the outside.

8pm. Done with part 3. I cleared this tutorial.

https://youtu.be/AoGXdldOWQA
Creating Sole Patterns for Footwear with Anchor Points in Substance 3D Painter

This caught my attention. I might be able to use this for radial patterns.

https://substance3d.adobe.com/tutorials?level=0&software=Substance%203D%20Painter

There is a lot to go through here.

https://substance3d.adobe.com/tutorials/courses/Substance-3D-Painter-Anchor-Points-Generators-and-Brush-Maker/youtube-q9mLZQKxPSo

Let me just watch these.

https://youtu.be/q9mLZQKxPSo?t=373

Anchor points weren't what I hoped they would be. Ugh, nevermind them for now.

https://youtu.be/q9mLZQKxPSo?t=490

This is cool.

8:20pm. So anchor points are just a referencing system.

8:25pm. HAving lunch made me quite drowsy. I do not feel like pushing it. Let me chill for a while and I will go to bed. Hopefully at something like 12am today instead of 1 like usual.

I do not feel like hurrying anymore. The desk will get done when its is done. From what I can see most of these videos are in the foundation series. I'll watch a bunch more tomorrow, go through the other starter tutorial...

https://substance3d.adobe.com/tutorials/courses/Getting-Started-with-Substance-3D-Painter-2021/youtube--ZbmRsOnApk

...and continue watching.

8:30pm. I am just eyeballing it, but it does not seem like here is more than 10h of video content here. I can cover this in a week or two. After that I can consider myself to be intermediate level in Substance Painter.

Then I'll hopefully know enough to understand what kind of process I should follow to make the peeled desk texture.

8:40pm. https://youtu.be/EB3CPVFnIM8
Using Projection in Substance Painter

Let me just watch this and then I am done. With no way of merging layers and no way of painting stencils, all my good ideas for making the radial patterns are gone. I can either do the texture in CSP or Blender using different methods. I suppose I could just paint them by hand regardless if nothing else is suitable.

9:10pm. I should try to make use of smart materials first. There are loads of possibilities to try. There might also be something on the community site. Painting by hand should be the last resort.

Let me close here so I can get back to reading Machimaho. After I finish the tutorials I'll know here I stand. I won't hurry to do this.

If it is meant to be, Heaven's Key will get made. If I run out of time and some tragedy forces me to get a job so be it. I'll just be making 5-10x the average salary in Croatia.

9:15pm. So I won't strain myself mentally. I'll do it one step at a time, just like when I was doing programming.

If I can have time, my skill will grow naturally until I am capable of doing what I want to do."

---
## [demberto/BytesIOEx](https://github.com/demberto/BytesIOEx)@[e8b25075dd...](https://github.com/demberto/BytesIOEx/commit/e8b25075dd6acecf0427516293164529ad64bbdb)
#### Saturday 2022-04-02 19:28:31 by demberto

Bump to 0.1.1

fuck git

fuck you x2

ohh ok

mmmm

arggh pylint

---
## [eliashauksson/antyanty](https://github.com/eliashauksson/antyanty)@[3024ae0a23...](https://github.com/eliashauksson/antyanty/commit/3024ae0a23c264ee72fa895fb27784c67c1348cb)
#### Saturday 2022-04-02 20:08:02 by lucijahuc

dont know it this solves stuff

order of errors: 
1) error squarecell (outside g_max)
2)anthills (do not get put inside the grid)
3)grid overlap stuff
4) are ants at home (can be done in AllObjects but what is the point) 
--> in my humble and possibly stupid opinion i would keep get overlap grid function and check for error messages before copying stuff to objects because we sorted the order and i dont want to fuck it up now. but i need to sleep rn.
ps. sorry for ugly folder but i have a small mess on my computer and like squarespace squarecelll thing

---
## [Arthur-Morgan36/Code-shit](https://github.com/Arthur-Morgan36/Code-shit)@[33a0183c1c...](https://github.com/Arthur-Morgan36/Code-shit/commit/33a0183c1cf7ee6e61644040ad28a769f403abb7)
#### Saturday 2022-04-02 20:33:19 by Arthur-Morgan36

Something for a friend

Does what you want, wherever you want, however you want, Visual Studio Code is an amazing te- wait this is the wrong file.

Okay so this file is pretty much random ideas I pieced up together.
This is totally not me showing how bored I am and making my friend's HTML project while I should be studying for my bio exam. 

If you even read this I hope you have a nice day or night.

---
## [Tomsod/elemental](https://github.com/Tomsod/elemental)@[dbff5c1332...](https://github.com/Tomsod/elemental/commit/dbff5c1332713506b90482238e1ca3c6cf604e9a)
#### Saturday 2022-04-02 20:45:40 by Tomsod M

Add two more weapon enchantments

These are probably the last ones.  First, I imported Elemental Slaying
weapon bonus from MM8.  Given that there's a lot of elementals, it makes
sense.  Second, I added a "Blessed" weapon bonus that protects from
curses while wielded and adds a silent +10 to-hit to the weapon.

To make the latter more relevant, all Necromancers can now curse on hit.
Someone complained that the Pit is now too easy to conquer -- well, here
you go!  Curse roughly matches dispel in annoyance factor, I think.

Also, Mekorig's Hammer is now Elemental Slaying, and the Perfect Bow you
get at the end of Master Archer promotion is now Blessed.  The same bow
will be Cursed is you're promoted to Sniper.  I really need to give
these two quests some individuality, but for now, that's something.

---
## [SirWillian/sst](https://github.com/SirWillian/sst)@[00ad7cdd3d...](https://github.com/SirWillian/sst/commit/00ad7cdd3d05d09a43bda972c823fdc440feabb9)
#### Saturday 2022-04-02 20:59:56 by Michael Smith

Clean up gameinfo_init() and other random stuff

- Just ask the engine for the game directory instead of doing the stupid
  argv sniffing hacks from the early days of trying to get the damn
  thing working.

- Also add some other path variables, functions and whatnot, and do some
  other minor tidying up.

- Also also, another damn copyright year, somebody please help me.

Unfortunate negative effect off this change: con_init() no longer
reports the game name, because it has to happen before gameinfo_init().
I've decided I don't really care, though.

---
## [ascent08/MCubed](https://github.com/ascent08/MCubed)@[17dca8ed74...](https://github.com/ascent08/MCubed/commit/17dca8ed7477077a79dd4744a394027a73f3a30b)
#### Saturday 2022-04-02 21:38:34 by ascent_

some updates

Removed Horse Stats Vanilla, updated a bunch of other mods

unfortunately we're still missing a bunch of mods for 1.18.2. here are my thoughts on each mod that has yet to be updated.

also i'm not listing the versions of the mods that were updated. figure it out for yourself fucko. ANYWAYS:

BetterEnd: i have been considering removing it because i don't want to go too overboard with adding new materials and this mod actually does add new materials that end up being stronger than netherite. i want the pack to keep a sort-of vanilla feel and adding new materials pushes it further away from that. however the mod does add some cool shit biome-wise.

Botania: to be completely honest I've never actually played around with the mod while testing the pack out. however it is one of those older mods that's decently well-known and the fact that i can have one of those older mods in the pack is really cool.

Gate of Babylon: I REALLY want to keep this mod because so far it's been the only mod i could find that adds new types of weapons. unfortunately it hasn't been updated since february (before 1.18.2 came out) which is painful.

Rat's Mischief: honestly we could do without it, i'd just like to have it in because ha ha funny rat

Spectrum: i really want to keep this mod in because it adds so much to the game yet keeps the game feel a lot like vanilla, as you progressively unlock the ability to see certain blocks. the only issue i really have with it is the geodes spawning above ground, which i can easily fix through the configs.

Stoneholm: underground villages. a relatively minor addition, but one that is really nice to have nonetheless.

YUNG's Better Strongholds: I'd rather have this in the pack for fairly obvious reasons. It genuinely makes strongholds better and more interesting than the current vanilla design which has been around for over a decade now.

anyways yeah

---
## [pburkett/top-down-zombie-game](https://github.com/pburkett/top-down-zombie-game)@[a4bdc8f7d6...](https://github.com/pburkett/top-down-zombie-game/commit/a4bdc8f7d62a615bc433ca2edf093ddd120f9ca8)
#### Saturday 2022-04-02 22:08:23 by pburkett

basic navigation actually works! Holy Fucking Shit!

---
## [Hoikas/korman](https://github.com/Hoikas/korman)@[aff3a42bd4...](https://github.com/Hoikas/korman/commit/aff3a42bd4370c53cacfbf412ad9231261503a41)
#### Saturday 2022-04-02 23:02:26 by Adam Johnson

Clearly deliniate the circles of hell.

If we've unleashed Satan on a material, he will perform his dark magick
on the material colors. Therefore, we need to prefix the satanic
materials with something other than "RTLit_" lest the plain old runtime
lit materials be infected by the prince of darkness.

---
## [kleinesfilmroellchen/serenity](https://github.com/kleinesfilmroellchen/serenity)@[53e6701454...](https://github.com/kleinesfilmroellchen/serenity/commit/53e670145420f6349bb4cf780782a072962386ae)
#### Saturday 2022-04-02 23:05:48 by kleines Filmröllchen

LibAudio+Userland: Use new audio queue in client-server communication

Previously, we were sending Buffers to the server whenever we had new
audio data for it. This meant that for every audio enqueue action, we
needed to create a new shared memory anonymous buffer, send that
buffer's file descriptor over IPC (+recfd on the other side) and then
map the buffer into the audio server's memory to be able to play it.
This was fine for sending large chunks of audio data, like when playing
existing audio files. However, in the future we want to move to
real-time audio in some applications like Piano. This means that the
size of buffers that are sent need to be very small, as just the size of
a buffer itself is part of the audio latency. If we were to try
real-time audio with the existing system, we would run into problems
really quickly. Dealing with a continuous stream of new anonymous files
like the current audio system is rather expensive, as we need Kernel
help in multiple places. Additionally, every enqueue incurs an IPC call,
which are not optimized for >1000 calls/second (which would be needed
for real-time audio with buffer sizes of ~40 samples). So a fundamental
change in how we handle audio sending in userspace is necessary.

This commit moves the audio sending system onto a shared single producer
circular queue (SSPCQ) (introduced with one of the previous commits).
This queue is intended to live in shared memory and be accessed by
multiple processes at the same time. It was specifically written to
support the audio sending case, so e.g. it only supports a single
producer (the audio client). Now, audio sending follows these general
steps:
- The audio client connects to the audio server.
- The audio client creates a SSPCQ in shared memory.
- The audio client sends the SSPCQ's file descriptor to the audio server
  with the set_buffer() IPC call.
- The audio server receives the SSPCQ and maps it.
- The audio client signals start of playback with start_playback().
- At the same time:
  - The audio client writes its audio data into the shared-memory queue.
  - The audio server reads audio data from the shared-memory queue(s).
  Both sides have additional before-queue/after-queue buffers, depending
  on the exact application.
- Pausing playback is just an IPC call, nothing happens to the buffer
  except that the server stops reading from it until playback is
  resumed.
- Muting has nothing to do with whether audio data is read or not.
- When the connection closes, the queues are unmapped on both sides.

This should already improve audio playback performance in a bunch of
places.

Implementation & commit notes:
- Audio loaders don't create LegacyBuffers anymore. LegacyBuffer is kept
  for WavLoader, see previous commit message.
- Most intra-process audio data passing is done with FixedArray<Sample>
  or Vector<Sample>.
- Improvements to most audio-enqueuing applications. (If necessary I can
  try to extract some of the aplay improvements.)
- New APIs on LibAudio/ClientConnection which allows non-realtime
  applications to enqueue audio in big chunks like before.
- Removal of status APIs from the audio server connection for
  information that can be directly obtained from the shared queue.
- Split the pause playback API into two APIs with more intuitive names.

I know this is a large commit, and you can kinda tell from the commit
message. It's basically impossible to break this up without hacks, so
please forgive me. These are some of the best changes to the audio
subsystem and I hope that that makes up for this :yaktangle: commit.

:yakring:

---

