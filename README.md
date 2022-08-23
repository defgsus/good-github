## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-08-22](docs/good-messages/2022/2022-08-22.md)


1,967,264 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,967,264 were push events containing 3,029,494 commit messages that amount to 237,296,769 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 38 messages:


## [bongani-m/hummingbird-client](https://github.com/bongani-m/hummingbird-client)@[9bff9f7848...](https://github.com/bongani-m/hummingbird-client/commit/9bff9f78484b4600d9680fd80d6dce325ac2fc92)
#### Monday 2022-08-22 00:17:16 by Emma Lejeck

Fix algolia.getIndex task concurrency

Ember Concurreny was happily giving us dropped task instances which never resolve, because Ember developers hate joy.

What we want, and what we expected .drop() would provide, is the last actually executed (ie, non-dropped) instance of the task, which is returned by .last on the task

Fuck Ember, fuck the Ember ecosystem

---
## [CaoE/pytorch](https://github.com/CaoE/pytorch)@[4c8cfb57aa...](https://github.com/CaoE/pytorch/commit/4c8cfb57aa3ac58112efb693635198b07edf008f)
#### Monday 2022-08-22 00:44:57 by Edward Z. Yang

Convert SymInt tracing to mode based tracing (#83380)

We're on our way to deleting ProxyTensor entirely (see https://github.com/pytorch/pytorch/pull/83330 ), but before we can do that, we have to delete ProxySymInt first. Here's the plan.

Changes in torch.fx.experimental.symbolic_shapes

* The general idea is to do mode based tracing. This means we need a mode that can interpose on all SymInt operations. There are a few ways to do this, but I've done it the easy way: (1) I have a separate mode for SymInt operations specifically called SymDispatchMode, and (2) this mode operates on PySymInt (and not the basic SymInt which is user visible). I elided Int from the name because if we add SymFloats I want to use the same mode to handle those as well, and I used Dispatch rather than Function because this is the "inner" dispatch operating PySymInt and not SymInt (this is not a perfect analogy, but SymFunctionMode definitely seemed wrong as you still must go through the C++ binding.) The mode is entirely implemented in Python for ease of implementation. We could have implemented this more symmetrically to TorchFunctionMode in C++, but I leave that as later work; this API is unlikely to get used by others (unlike TorchFunctionMode). One downside to not doing the mode in C++ is that we still have to do the hop via a preexisting PySymInt to wrap; this is currently not a big deal as conversion to SymInts only really happens when there is already another SymInt floating around. SymDispatchMode is pared down from TorchDispatchMode; there is no ancestor tracking since I don't expect people to be mixing up SymDispatchModes.
*  I made some improvements for tracing. When I invoke the SymDispatchMode handler, I would like constants to show up as constants, so they can be directly inlined into the FX graph (rather than going through a wrapping process first, and then the wrapped SymInt being used in the operation). To do this, I directly track if a PySymInt is a constant at construction time. Only wrapped PySymInts are constants.
* For convenience, PySymInts now support all magic methods that regular SymInts do. This is so that redispatch inside the SymDispatchMode can be written the idiomatic way `func(*args, **kwargs)` where func is an operator. The original names are retained for direct C++ calls.

Changes in torch.fx.experimental.proxy_tensor

* OK, so we got a new SymDispatchMode, so we define a ProxySymDispatchMode and activate it when we start tracing. This mode is currently unconditionally activated although technically we only need to activate it when doing symbolic tracing (it doesn't matter either way as there are no SymInts if you are not doing symbolic tracing).
* We delete ProxySymInt. To do this, we must now record the proxy for the SymInt some other way. Based on discussion with Chillee, it is more intuitive to him if the proxies are still recorded on the SymInt in some way. So we store them in the `__dict__` of the PySymInt, indexed by Tracer. An improvement is to make this a weak map, so that we remove all of these entries when the tracer dies. In an original version of this PR, I keyed on the mode itself, but tracer is better as it is accessible from both modes (and as you will see, we will need to fetch the map from both the ProxySymDispatchMode as well as the ProxyTorchDispatchMode.) The implementation of SymDispatchMode now simply retrieves the proxies, performs the underlying operation as well as the FX graph recording, and then records the output proxy to the PySymInt. Note that FX tracing does not work with proxies and SymInts, so we manually call `call_function` to ensure that the correct operations get recorded to the graph. This means conventional FX retracing with proxies only will not work with these graphs, but there wasn't really any reason to do this (as opposed to `make_fx` retracing) anyway. Constants are detected and converted directly into Python integers.
* SymInts can show up as arguments to tensor operations, so they must be accounted for in ProxyTorchDispatchMode as well. This is done by searching for SymInt arguments and converting them into proxies before the proxy call. This can be done more efficiently in a single `tree_map` but I'm lazy. The helper `unwrap_symint_proxy` conveniently implements the unwrapping in one place given a tracer; unfortunately it cannot be shared with SymDispatchMode as SymDispatchMode gets PySymInts, but ProxyTensorMode gets SymInts. Similarly, tensors that are returned from tensor operations can have SymInts in their shapes, which need fresh proxies allocated. To avoid leaking internal details of SymInt shape computation to the tensor operation graph, these SymInts are always given proxies derived from `x.size(dim)` call on their return tensor. We also need to do this for strides and numel but have not done so yet. Furthermore, we must avoid tracing internal SymInt calls while we run meta operations on the true operation; this is achieved by also disabling SymInt tracing on the inside of tensor tracing. This is analogous to how tensor tracing is disabled inside the implementation of tracing mode, but unfortunately we are unable to use the same mechanism (this would have been easier if the two modes could be combined somehow, and I am amenable to suggestions to try harder to achieve this.)
* Because there are no more ProxySymInts, we no longer need to do anything to unwrap SymInt. Furthermore, we do not need to reallocate ProxySymInts on class creation.
* If a bare SymInt without a Proxy is encountered, it is assumed that this must be a constant. `create_arg` handles this case. Non-constant free SymInts result in an assert error.
* The initial input handling in `dispatch_trace` involves traversing all of the input tensors, traversing over their shapes, and assigning proxies for the SymInts in shapes in the same way we handle proxies for the output tensors.

The preexisting testing is inadequate but will be better after I rebase past https://github.com/pytorch/pytorch/pull/82209

Signed-off-by: Edward Z. Yang <ezyang@fb.com>
Pull Request resolved: https://github.com/pytorch/pytorch/pull/83380
Approved by: https://github.com/samdow

---
## [ianthehenry/judge](https://github.com/ianthehenry/judge)@[8dcbff38a4...](https://github.com/ianthehenry/judge/commit/8dcbff38a47327ee5958a6bd4263388d9b29da03)
#### Monday 2022-08-22 01:11:58 by Ian Henry

use lexical over dynamic scope to link expect with enclosing test

I originally avoided this approach because of the bad error messages
if you use (expect) outside of a (test) block. But I think the simplicity is
worth it. Now instead of a friendly reminder, you will get the rather ugly:

compile error: unknown symbol EXPECT_MUST_OCCUR_WITHIN_TEST_00000U

Which is not as nice, but I think the simplification is worth it. After all,
it's not a mistake people that people are likely to make in the first place.
Especially since I am the only person using this library.

---
## [ProfessorPopoff/mojave-sun-13](https://github.com/ProfessorPopoff/mojave-sun-13)@[2996f41136...](https://github.com/ProfessorPopoff/mojave-sun-13/commit/2996f41136fcd4dee419b4138e45ae65df9529f6)
#### Monday 2022-08-22 01:24:10 by EdwardNashton

Update Time: Machinery to People (#2096)

* Update Time: Machinery to People

Added a recorders and server racks all over the city.

Slightly changed a "Cheap Motel" near Police Dept.

Slightly changed Police Dept.

Slightly updated Chemical Factory and Weather Station.

* Update time: small fixes

Changed a servers on Power Plant.

* Update Time: that god damn room in PD

I hope we're done with it.

* Update Time: small fix

Removed a potential feature with "shutter trap" in PD.

* Update Time: fixes and updating Water Treatment Station

You made me do this, Original.

* Update Time: one day the south dir comes, we'll place our stuff and go

Sometimes you get too picky

Co-authored-by: Edward Nashton <eddienigma48@gmail.com>

---
## [cyberitsolutions/bootstrap2020](https://github.com/cyberitsolutions/bootstrap2020)@[940f39e6f4...](https://github.com/cyberitsolutions/bootstrap2020/commit/940f39e6f4e0fd864ba69acd411551445332731c)
#### Monday 2022-08-22 01:47:47 by Trent W. Buck

Use pipewire (not pulseaudio)

This fixes a persistent bug where if you tried to change volume while vlc was playing a video, sometimes (often!) pulseaudio would just crash.
pulseaudio would restart, but the already-open vlc would never make noises again.
To fix it you had to close and reopen vlc.

    pulseaudio:
    orc_code_region_allocate_codemem():
    Failed to create write and exec mmap regions.
    This is probably because SELinux execmem check is enabled (good) and $TMPDIR and $HOME are mounted noexec (bad).

Mike found that this is because Debian pipewire is compiled with --enable-orc.
That is https://github.com/GStreamer/orc and what it does is create new executables at runtime like
/tmp/orcexec.XXXXXX or /run/user/1000/orcexec.XXXXXX or ~/orcexec.XXXXXX
This is obviously banned on PrisonPC -- all user-writable areas are mounted -o noexec precisely to defeat this class of attack.

We probably could have solved this by recompiling pulseaudio with ./configure --disable-orc.

    https://sources.debian.org/src/pulseaudio/14.2-2/debian/control/#L26

However, we already had pipewire ready to go, and
we planned to switch to pipewire permanently in Debian 12.

The only reason to stick with pulseaudio for Debian 11 was that this commit is long and yukky.
But given that it fixes and actual user-visible and SUPER ANNOYING bug, fuck it, pipewire TODAY.

PS: pipewire does not use orc at all; it's not even in the codebase.

---
## [ammarfaizi2/linux-fork](https://github.com/ammarfaizi2/linux-fork)@[9770f07fd0...](https://github.com/ammarfaizi2/linux-fork/commit/9770f07fd05b8cf3c696cf40bf08e3fd88dde17e)
#### Monday 2022-08-22 03:06:05 by Johannes Weiner

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
## [wadetregaskis/SwiftWeather](https://github.com/wadetregaskis/SwiftWeather)@[425bc6a173...](https://github.com/wadetregaskis/SwiftWeather/commit/425bc6a173a2ad9c0c7a9772521e2e97a829b32f)
#### Monday 2022-08-22 04:05:56 by Wade Tregaskis

Used an "AnyMD" type eraser to allow the use of the actual Measurement struct, rather than class.

It's a huge pain in the arse to do this because of Swift's terrible ergonomics regarding generics, but it's [hopefully] worth it because it has one, significant benefit:  users can retrieve _either_ the struct or class forms of Measurement from the Any that they're provided via WeatherSensor!  Apparently Swift will magically do the conversion from struct to class form implicitly if you do a "value as? Measurement".  There's no implicit conversion _from_ class to struct form, though, which is why it's so important that the real underlying values be in struct form.  Plus it's presumably more efficient at runtime.

---
## [PistachioPiper/genshin-buddy](https://github.com/PistachioPiper/genshin-buddy)@[4a2ec9b2ef...](https://github.com/PistachioPiper/genshin-buddy/commit/4a2ec9b2ef4b301d55f6ab4e675d0de5e12db5f6)
#### Monday 2022-08-22 04:45:35 by Piper

im rly pissing bricks out here, motivation is a bitch. i have watched an entire season of my hero academia today and have barely even touched my code in a couple days. it's so silly how i have literally one thing left to do but still can't finish it. probably never gonna get it done at this rate, i just rly fucking hope that the current code  doesn't break at all, i dont think i have the patience or willpower to fix it right now. i like women i think

---
## [astroparam/porter](https://github.com/astroparam/porter)@[786738a7c3...](https://github.com/astroparam/porter/commit/786738a7c33b725fa1fae253f9ca789438553d33)
#### Monday 2022-08-22 05:46:55 by Carolyn Van Slyck

Use a distroless base image (#1656)

* Use distroless base image

Use a distroless base image for our porter docker images. This
has less of an attack surface because it only ships
the essentials to run porter, not the extra stuff that usually comes
with a linux distribution.

Signed-off-by: Carolyn Van Slyck <me@carolynvanslyck.com>

* Apply suggestions from code review

Signed-off-by: Carolyn Van Slyck <me@carolynvanslyck.com>

Co-authored-by: Nathaniel "Church" Hatfield <church13halo@gmail.com>

* Move agent's run.sh into Go

Since the nonroot distroless image doesn't have a shell, we can't use
run.sh to copy the porter config files into PORTER_HOME at container
start. I have implemented that in Go (sorry it's a lot vs what good ole
cp did for us under the hood).

One trick is that when /porter-config is mounted into the container by
k8s, it uses symlinks like this:

/porter-config
  ..data/porter.config
  porter.config -> ..data/porter.config

So it's not a straightforward as you'd think at first glance.

Signed-off-by: Carolyn Van Slyck <me@carolynvanslyck.com>

* Apply suggestions from code review

Signed-off-by: Carolyn Van Slyck <me@carolynvanslyck.com>
Co-authored-by: Vaughn Dice <vaughn.dice@fermyon.com>
Co-authored-by: Nathaniel "Church" Hatfield <church13halo@gmail.com>
Co-authored-by: Vaughn Dice <vaughn.dice@fermyon.com>

---
## [Zeodexic/tsorcRevamp](https://github.com/Zeodexic/tsorcRevamp)@[8fea941afa...](https://github.com/Zeodexic/tsorcRevamp/commit/8fea941afa122afe297bb199a83c4c7b3e295788)
#### Monday 2022-08-22 06:25:21 by timhjersted

Created Dragon Crest Shield + new sprites for later use

-Added Dragon Crest Shield, which consumes stamina to absorb damage; it drops from a secret boss in the Oolicile Forest
-Added Faraam, Gael, Havel,, Nameless King, Greirat, and Seigward sprites, for potentially turning into bosses later (permission granted by spriter) - we could potentially use Leonhard as a base but the animation frames don't match yet - alternatively, we could tweak the animation code to work with all of these sets, as they're all uniform
-Ancient Demon has correct health
-Hero of Lumelia will spawn corrupted hammers and teleport if she loses sight of the player for too long
-Added 'final stand' attack for Hellkite Dragon and reduced movement speed a bit
-Increased Seath's health and soul drops
-Added MP compatibility for Hunter spawn? (not entirely sure if necessary)
-Blocked small, normal and large female zombie, because silly, also blocked small, normal and large variant of normal zombie in HM, though was tempted to block them entirely, to clear room for more interesting enemies

---
## [silicons/Citadel-Station-13-RP](https://github.com/silicons/Citadel-Station-13-RP)@[5b6010d722...](https://github.com/silicons/Citadel-Station-13-RP/commit/5b6010d722f24734b362064ee9e12ce521aa078e)
#### Monday 2022-08-22 06:32:41 by lectronyx

Closed Eyes (#4303)

* Closed Eyes

Adds the "Closed Eyes" marking from Vorestation, because Sergal Eyes suck ass and in this house we bully cheeses

* unfucked sprite

apparently i just needed to give -head

* Fixed newline error

Apparently, ending on a line with content is bad.

---
## [ThatDan123/unitystation](https://github.com/ThatDan123/unitystation)@[9d18efaf5f...](https://github.com/ThatDan123/unitystation/commit/9d18efaf5f6decab115764e765cd4a1c50fb96d8)
#### Monday 2022-08-22 09:44:10 by MaxIsJoe

Adds the ability to climb crates (#7481)

* Adds the ability to climb crates

* cleanup

* remove function that's not working

* client and server side stuff

* fuck you rider

* Update UnityProject/Assets/Scripts/Objects/Climbable.cs

* Update Climbable.cs

* Update Climbable.cs

Co-authored-by: NoooneyDude <noooneydude@gmail.com>

---
## [arixmkii/podman](https://github.com/arixmkii/podman)@[a534a86701...](https://github.com/arixmkii/podman/commit/a534a867019df8f475d2962635475bdc81dc2b8a)
#### Monday 2022-08-22 10:14:01 by Ed Santiago

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
## [Evolution-X/frameworks_base](https://github.com/Evolution-X/frameworks_base)@[f1a599bf8e...](https://github.com/Evolution-X/frameworks_base/commit/f1a599bf8e6fcc0b670d6471388d267516d714dc)
#### Monday 2022-08-22 10:29:24 by Joey Huab

core: Refactor Pixel 2021 features availability

* Magic Eraser is wonky and hard to
  enable and all this mess isn't really worth
  the trouble so just stick to the older setup.

* Default Pixel 5 spoof for Photos and only switch
  to Pixel XL when spoof is toggled.

* We will try to bypass 2021 features and Raven
  props for non-Pixel 2021 devices as apps usage
  requires TPU.

* Remove P21 experience system feature check

---
## [groves/helix](https://github.com/groves/helix)@[973c51c3e9...](https://github.com/groves/helix/commit/973c51c3e970aa975f2bd1869d50ce2ae6c6de34)
#### Monday 2022-08-22 10:43:00 by Michael Davis

Remove C-n and C-p from the insert mode keymap (#3340)

These are read-line-like bindings which we'd like to minimize in
insert mode in general.

In particular these two are troublesome if you have a low
`editor.idle-timeout` config and are using LSP completions: the
behavior of C-n/C-p switches from moving down/up lines to moving
down/up the completion menu, so if you hit C-n too quickly
expecting to be in the completion menu, you'll end up moving down
a line instead. Using C-p moves you back up the line but doesn't
re-trigger the completion menu. This kind of timing related change
to behavior isn't realistically that big of a deal but it can be
annoying.

---
## [amir73il/linux](https://github.com/amir73il/linux)@[b8b8414338...](https://github.com/amir73il/linux/commit/b8b841433880d36264b39c0ab163f200715a8e94)
#### Monday 2022-08-22 11:50:07 by Yang Xu

fs: move S_ISGID stripping into the vfs_*() helpers

commit 1639a49ccdce58ea248841ed9b23babcce6dbb0b upstream.

[backport for 5.10.y without idmapped mounts]

Move setgid handling out of individual filesystems and into the VFS
itself to stop the proliferation of setgid inheritance bugs.

Creating files that have both the S_IXGRP and S_ISGID bit raised in
directories that themselves have the S_ISGID bit set requires additional
privileges to avoid security issues.

When a filesystem creates a new inode it needs to take care that the
caller is either in the group of the newly created inode or they have
CAP_FSETID in their current user namespace and are privileged over the
parent directory of the new inode. If any of these two conditions is
true then the S_ISGID bit can be raised for an S_IXGRP file and if not
it needs to be stripped.

However, there are several key issues with the current implementation:

* S_ISGID stripping logic is entangled with umask stripping.

  If a filesystem doesn't support or enable POSIX ACLs then umask
  stripping is done directly in the vfs before calling into the
  filesystem.
  If the filesystem does support POSIX ACLs then unmask stripping may be
  done in the filesystem itself when calling posix_acl_create().

  Since umask stripping has an effect on S_ISGID inheritance, e.g., by
  stripping the S_IXGRP bit from the file to be created and all relevant
  filesystems have to call posix_acl_create() before inode_init_owner()
  where we currently take care of S_ISGID handling S_ISGID handling is
  order dependent. IOW, whether or not you get a setgid bit depends on
  POSIX ACLs and umask and in what order they are called.

  Note that technically filesystems are free to impose their own
  ordering between posix_acl_create() and inode_init_owner() meaning
  that there's additional ordering issues that influence S_SIGID
  inheritance.

* Filesystems that don't rely on inode_init_owner() don't get S_ISGID
  stripping logic.

  While that may be intentional (e.g. network filesystems might just
  defer setgid stripping to a server) it is often just a security issue.

This is not just ugly it's unsustainably messy especially since we do
still have bugs in this area years after the initial round of setgid
bugfixes.

So the current state is quite messy and while we won't be able to make
it completely clean as posix_acl_create() is still a filesystem specific
call we can improve the S_SIGD stripping situation quite a bit by
hoisting it out of inode_init_owner() and into the vfs creation
operations. This means we alleviate the burden for filesystems to handle
S_ISGID stripping correctly and can standardize the ordering between
S_ISGID and umask stripping in the vfs.

We add a new helper vfs_prepare_mode() so S_ISGID handling is now done
in the VFS before umask handling. This has S_ISGID handling is
unaffected unaffected by whether umask stripping is done by the VFS
itself (if no POSIX ACLs are supported or enabled) or in the filesystem
in posix_acl_create() (if POSIX ACLs are supported).

The vfs_prepare_mode() helper is called directly in vfs_*() helpers that
create new filesystem objects. We need to move them into there to make
sure that filesystems like overlayfs hat have callchains like:

sys_mknod()
-> do_mknodat(mode)
   -> .mknod = ovl_mknod(mode)
      -> ovl_create(mode)
         -> vfs_mknod(mode)

get S_ISGID stripping done when calling into lower filesystems via
vfs_*() creation helpers. Moving vfs_prepare_mode() into e.g.
vfs_mknod() takes care of that. This is in any case semantically cleaner
because S_ISGID stripping is VFS security requirement.

Security hooks so far have seen the mode with the umask applied but
without S_ISGID handling done. The relevant hooks are called outside of
vfs_*() creation helpers so by calling vfs_prepare_mode() from vfs_*()
helpers the security hooks would now see the mode without umask
stripping applied. For now we fix this by passing the mode with umask
settings applied to not risk any regressions for LSM hooks. IOW, nothing
changes for LSM hooks. It is worth pointing out that security hooks
never saw the mode that is seen by the filesystem when actually creating
the file. They have always been completely misplaced for that to work.

The following filesystems use inode_init_owner() and thus relied on
S_ISGID stripping: spufs, 9p, bfs, btrfs, ext2, ext4, f2fs, hfsplus,
hugetlbfs, jfs, minix, nilfs2, ntfs3, ocfs2, omfs, overlayfs, ramfs,
reiserfs, sysv, ubifs, udf, ufs, xfs, zonefs, bpf, tmpfs.

All of the above filesystems end up calling inode_init_owner() when new
filesystem objects are created through the ->mkdir(), ->mknod(),
->create(), ->tmpfile(), ->rename() inode operations.

Since directories always inherit the S_ISGID bit with the exception of
xfs when irix_sgid_inherit mode is turned on S_ISGID stripping doesn't
apply. The ->symlink() and ->link() inode operations trivially inherit
the mode from the target and the ->rename() inode operation inherits the
mode from the source inode. All other creation inode operations will get
S_ISGID handling via vfs_prepare_mode() when called from their relevant
vfs_*() helpers.

In addition to this there are filesystems which allow the creation of
filesystem objects through ioctl()s or - in the case of spufs -
circumventing the vfs in other ways. If filesystem objects are created
through ioctl()s the vfs doesn't know about it and can't apply regular
permission checking including S_ISGID logic. Therfore, a filesystem
relying on S_ISGID stripping in inode_init_owner() in their ioctl()
callpath will be affected by moving this logic into the vfs. We audited
those filesystems:

* btrfs allows the creation of filesystem objects through various
  ioctls(). Snapshot creation literally takes a snapshot and so the mode
  is fully preserved and S_ISGID stripping doesn't apply.

  Creating a new subvolum relies on inode_init_owner() in
  btrfs_new_subvol_inode() but only creates directories and doesn't
  raise S_ISGID.

* ocfs2 has a peculiar implementation of reflinks. In contrast to e.g.
  xfs and btrfs FICLONE/FICLONERANGE ioctl() that is only concerned with
  the actual extents ocfs2 uses a separate ioctl() that also creates the
  target file.

  Iow, ocfs2 circumvents the vfs entirely here and did indeed rely on
  inode_init_owner() to strip the S_ISGID bit. This is the only place
  where a filesystem needs to call mode_strip_sgid() directly but this
  is self-inflicted pain.

* spufs doesn't go through the vfs at all and doesn't use ioctl()s
  either. Instead it has a dedicated system call spufs_create() which
  allows the creation of filesystem objects. But spufs only creates
  directories and doesn't allo S_SIGID bits, i.e. it specifically only
  allows 0777 bits.

* bpf uses vfs_mkobj() but also doesn't allow S_ISGID bits to be created.

The patch will have an effect on ext2 when the EXT2_MOUNT_GRPID mount
option is used, on ext4 when the EXT4_MOUNT_GRPID mount option is used,
and on xfs when the XFS_FEAT_GRPID mount option is used. When any of
these filesystems are mounted with their respective GRPID option then
newly created files inherit the parent directories group
unconditionally. In these cases non of the filesystems call
inode_init_owner() and thus did never strip the S_ISGID bit for newly
created files. Moving this logic into the VFS means that they now get
the S_ISGID bit stripped. This is a user visible change. If this leads
to regressions we will either need to figure out a better way or we need
to revert. However, given the various setgid bugs that we found just in
the last two years this is a regression risk we should take.

Associated with this change is a new set of fstests to enforce the
semantics for all new filesystems.

Link: https://lore.kernel.org/ceph-devel/20220427092201.wvsdjbnc7b4dttaw@wittgenstein [1]
Link: e014f37db1a2 ("xfs: use setattr_copy to set vfs inode attributes") [2]
Link: 01ea173e103e ("xfs: fix up non-directory creation in SGID directories") [3]
Link: fd84bfdddd16 ("ceph: fix up non-directory creation in SGID directories") [4]
Link: https://lore.kernel.org/r/1657779088-2242-3-git-send-email-xuyang2018.jy@fujitsu.com
Suggested-by: Dave Chinner <david@fromorbit.com>
Suggested-by: Christian Brauner (Microsoft) <brauner@kernel.org>
Reviewed-by: Darrick J. Wong <djwong@kernel.org>
Reviewed-and-Tested-by: Jeff Layton <jlayton@kernel.org>
Signed-off-by: Yang Xu <xuyang2018.jy@fujitsu.com>
[<brauner@kernel.org>: rewrote commit message]
Signed-off-by: Christian Brauner (Microsoft) <brauner@kernel.org>
Signed-off-by: Amir Goldstein <amir73il@gmail.com>

---
## [majestrate/loki-network](https://github.com/majestrate/loki-network)@[f42d41d217...](https://github.com/majestrate/loki-network/commit/f42d41d21731b185e10707148f6d0483864480f8)
#### Monday 2022-08-22 11:55:21 by Jeff

by setting the magical undocumented env var USE_SYSTEM_7ZA to 'true' we can have the pile of npm bullshit code use our system's local 7z binary instead of the probably not backdoored binary from npm, yes for real. i hate nodejs so god damn much you have no fucking idea

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[851a79e159...](https://github.com/mrakgr/The-Spiral-Language/commit/851a79e159652a13469cc4aa9ad457cf5097e37e)
#### Monday 2022-08-22 12:05:04 by Marko Grdinić

"9:20am. I am up. I've been lounging in bed for a while. Let me chill and then I'll get busy with posting chapter 5. After that I'll check out DALLE and whether SD is out.

9:40am. Let me start for real. Ok, first let me go over ch 5 again. Then I'll do the author's note and post it.

9:45am. Focus me, focus. Stop reading HN. If I have to read that shit, I should instead aim to stop for the day early.

10:30am. Done proofing. I changed a few minor things. Let me post it.

It seems somebody left a review and it is only 2.5. Yeah, I doubt my writing is going to be winning any prizes. It feels like I am cursed if anything when it comes to making an impression whether that be in real life or in writing. But I think the readers should come and stay for the novelty and the impact of my writing. I am not really expecting high ratings for Heaven's Key. Also, I don't generally look at reviews since they rarely have anything to do with my enjoyment of a story.

> As per plan, I'll be checking out Stable Diffusion this week, so I'll be taking a break from writing. I'll be going over the existing chapters and illustrating them. Surprisingly, I got a pass for DALLE, so if SD is not out yet, I'll use it instead.

10:40am. This is good enough for today's note. Let me check out /g/ threads if SD is out yet. Since it is early in the US, it might not be the case yet.

https://boards.4channel.org/g/thread/88237460

///

In the UK its monday... Emad is in the UK, but technically its still morning and it seems he went to sleep 3 hours ago. May be in 12 hours he will release them

check his twitter https://twitter.com/EMostaque

///

Let me try DALLE then.

> You get 50 free credits during your first month, and 15 free credits will refill every month after that.

Ok, let me start from chapter 1.

> After a long and tedious day I arrived back home. Closing the door behind me, I enter the room and toss my bookbag at the side, homing in on the object of interest, a package that arrived by mail. I got it last night, and waited until I was rested to set it up. Using a pair of scissors, I cut away the sealing tape of the dull, cardboard mailing box, and took out the smaller box from within with the actual product. The printed image on it depicts a white, glossy sphere, twice the size of a marble. I open the box, take out the marble along with the orb holder, get off the bed I was working on and move towards the desk. I sit myself on the chair and after deliberating for a few moments where to place it: the desk in front of me or the top of the computer case next to it, I decide on the case. Gently placing the orb holder on the rig, I turn on my old computer and get to work downloading the programs necessary to get the orb to work.

Can get an image of the brain core box.

> A computer hardware box. The image on its sides is of white, round glossy spheres, and the logo of the company is a styled, capital R.

The result is pretty shitty. I see that it cost me a single credit.

My prompt engineering skills are quite weak.

> A square, red box. The image on its sides is of white, round, glossy spheres, and the logo of the company is a styled, capital R.

Let me try this.

11:10am. > A square, white box made of glossy cardboard. The illustrated image on its sides is of white, round, glossy sphere, and the logo of the company is a styled, capital R. Photo.

One of the outputs caught my eye even if it is not exactly what I had in mind. I really need some prompt engineering advice at this stage. Also this exercise will be a great help in developing my vocabulary. This is what I meant by this being writing. It is really programming via natural language.

https://huggingface.co/spaces/dalle-mini/dalle-mini/discussions/42
https://www.creativebloq.com/news/how-to-use-dall-e

I need to study how other people are doing it, but maybe I should skip DALLE and wait for SD to be released properly. 50 credits is basically nothing. I could run through all of this in a few minutes. The images are rather low res as well.

https://dallery.gallery/the-dalle-2-prompt-book/

Let me go through this thing.

> You can tell is an image has been created by DALL·E 2 because they contain a signature that looks like a row of coloured squares at the bottom right of the image (assuming the image hasn't been cropped. See the example above.

Can I stop it from doing that shit?

11:30am. Let me take a short break.

11:50am. I am back. Forget the box for the time being. Let me try the brain core in the palm of Euclid's hand. Actually, let me read the guide first.

> For 2D art, we've gone a little deeper, looking at particular art styles and art movements. But if you want to create images of buildings, for example, then learning more about architectural periods, famous architects, and names of architectural details will be helpful to create specific outputs. Same for candlesticks, cartoons or candy wrappers.

> DALL·E knows a lot about everything, so the deeper your knowledge of the requisite jargon, the more detailed the results.

I think that doing in-painting will be a really good way of getting started as an artist. I know a lot of 3d and I am stuck on 2d, but letting DALLE give me a hand will really allow me progress. I remember how I used to be bad at roguelikes, but thanks to saveloading, got better at it over time and can now easily beat them without such aid.

> Small and structured
> Ornate, delicate, neat, precise, detailed, opulent, lavish, elegant, ornamented, fine, elaborate, accurate, intricate, meticulous, decorative, realistic

I should use some of these to describe the box.

12pm. Let me have breakfast here. It is going to take me a while to properly digest it. I thought I was done with art, but it seems I'll be getting back to it.

12:45pm. My parents are moving things around the house, so it is hectic. I just got an idea, let me try the gigachad.

...It doesn't seem to have any idea what that is supposed to be. Nevermind.

> Drawing of a gigachad.

It seems to think it is some kind of insect. What have the guys at OpenAI been teaching it?

> Blueprint of Earth.

This is quite nice. Right now I am just going through the DALLE prompt book for ideas.

> Screenshot of X from (game, real or imaginary, console, year)

Maybe I could have it generate images in the Genshin Impact style this way?

1pm. The last quarter of the book is on in-painting and editing.

> By using repeated edits, variations, reprompts, inpainting, uncropping, and more, you can continue to tweak an image to your heart's content - although you might get through a lot of your 50 daily variations just to create one image!

So the beta testers got 50 a day, while I get 15 a month for free. What a ripoff.

1:15pm. 115 credits cost 15$?

That is ultra expensive.

I know, I know, DALLE would be way cheaper than a pro artist, but if you had a pro artist, you could instruct him as to what to make instead getting back random art. With DALLE I have to iterate a lot to get something good. I was just trying out boxes and already spend 10 credits just on that. The other 40 will be gone in a flash at this rate.

I do not feel like running through the rest.

Later today SD will come out, but nevermind that.

Let me get back to writing.

I'll do another chapter of Heaven's Key and then try SD when it is out. Right now the heat is high, and I do not feel like messing with this.

When I have good prompts using SD, I'll try them out on DALLE as well. That will make playing with DALLE a lot cheaper.

1:20pm. I am not in a hurry here. I was just early by about one day. Let me get back to writing, that is what I should be doing.

Let me do some writing. Let me see if I can get through at least the first scene. I deal with chapter six and then check out generative NNs once more.

1:25pm. DALLE is lingering on my mind, I need to refocus on the task at hand.

I really wasn't ready for what I had today...

...Damn it. Let me try the golden city. I'll upload the city, give it a description and see what DALLE does.

1:30pm. > Golden city in the sky shines golden radiance on the city below.

It just gets rid of the city and fills in the background. The background fill is capable, but this is not what I want.

Hmmm, the variations are a bit interesting.

Let me try it again. After that I'll try just the description.

> Golden city in the night sky shines golden radiance on the city below. The stars are intense and radiant.

Hmmmmm

> A floating golden city in the night sky shines golden radiance on the city metropolis below. The stars are intense and radiant.

Let me try this. It is really lacking a floating city.

Nope, I actually like the results, but it really needs a golden city in the sky for the image to work for me.

> A golden city floating on a disc in the night sky shines golden radiance on the city metropolis below. The stars are intense and radiant.

Let me try this.

> Anime art of a golden city floating on a disc in the night sky shines golden radiance on the city metropolis below. The stars are intense and radiant.

No, nothing is working for me when it comes to upping the quality of this. It always looks like some artsy painting. It is nice to look at, but it is not what I am looking for. I'd really have preferred some really...

Let me put it in.

> A photo of a golden city floating on a disc in the night sky shines golden radiance on the city metropolis below. The stars are intense and radiant.

Hmmm, this is a bit better.

1:50pm. https://www.technollama.co.uk/dall%C2%B7e-goes-commercial-but-what-about-copyright
> “Ownership of Generations. To the extent allowed by law and as between you and OpenAI, you own your Prompts and Uploads, and you agree that OpenAI owns all Generations (including Generations with Uploads but not the Uploads themselves), and you hereby make any necessary assignments for this.
> you agree that OpenAI owns all Generations

OpenAI can screw itself. Anyway, I've ran through half my allowed credits at this point. This is good enough for a trial run. DALLE is interesting, but not that great. I'd need to crop any generated images to get rid of those colored squares on the bottom right corner.

1:55pm. Ok, focus me. I am done with DALLE. I won't touch it again.

Let me check the /g/ thread. Not out yet.

2pm. Focus me. Forget SD until chapter 6 is done.

I need to initialize my mind for the next chapter properly. Let me take a bath here.
"

---
## [kamaboko117/ft_containers](https://github.com/kamaboko117/ft_containers)@[3e5a7b9c2b...](https://github.com/kamaboko117/ft_containers/commit/3e5a7b9c2bca942787d90ea018eae5a9338d1f11)
#### Monday 2022-08-22 12:26:45 by Alexander SABOURET

fuck this shit this is fkn cringe i hate this fuck commit messages fuck this project

---
## [warface1234455/Yogstation](https://github.com/warface1234455/Yogstation)@[f4c7571fc3...](https://github.com/warface1234455/Yogstation/commit/f4c7571fc333779cbf761e637f2774a62b6b4d78)
#### Monday 2022-08-22 12:59:45 by Vaelophis Nyx

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
## [npv12/strix_kernel_oneplus_sm8150](https://github.com/npv12/strix_kernel_oneplus_sm8150)@[a3486e1d50...](https://github.com/npv12/strix_kernel_oneplus_sm8150/commit/a3486e1d50a69e2fc79a448110d3b6d48afd5042)
#### Monday 2022-08-22 13:47:28 by Zlatan Radovanovic

Revert "msm: camera: icp: Enable hang dump on failure"

Fuck you CAF.

This reverts commit eece594678f618c964051092fa0dd470b26039b3.

Signed-off-by: Pranav <npv12@iitbbs.ac.in>

---
## [BARZINNAM/git](https://github.com/BARZINNAM/git)@[5beca49a0b...](https://github.com/BARZINNAM/git/commit/5beca49a0b1f3c6d05a4437ca037ab2123a2de57)
#### Monday 2022-08-22 13:49:20 by Ævar Arnfjörð Bjarmason

test-lib: simplify by removing test_external

Remove the "test_external" function added in [1]. This arguably makes
the output of t9700-perl-git.sh and friends worse. But as we'll argue
below the trade-off is worth it, since "chaining" to another TAP
emitter in test-lib.sh is more trouble than it's worth.

The new output of t9700-perl-git.sh is now:

	$ ./t9700-perl-git.sh
	ok 1 - set up test repository
	ok 2 - use t9700/test.pl to test Git.pm
	# passed all 2 test(s)
	1..2

Whereas before this change it would be:

	$ ./t9700-perl-git.sh
	ok 1 - set up test repository
	# run 1: Perl API (perl /home/avar/g/git/t/t9700/test.pl)
	ok 2 - use Git;
	[... omitting tests 3..46 from t/t9700/test.pl ...]
	ok 47 - unquote escape sequences
	1..47
	# test_external test Perl API was ok
	# test_external_without_stderr test no stderr: Perl API was ok

At the time of its addition supporting "test_external" was easy, but
when test-lib.sh itself started to emit TAP in [2] we needed to make
everything surrounding the emission of the plan consider
"test_external". I added that support in [2] so that we could run:

	prove ./t9700-perl-git.sh :: -v

But since then in [3] the door has been closed on combining
$HARNESS_ACTIVE and -v, we'll now just die:

	$ prove ./t9700-perl-git.sh :: -v
	Bailout called.  Further testing stopped:  verbose mode forbidden under TAP harness; try --verbose-log
	FAILED--Further testing stopped: verbose mode forbidden under TAP harness; try --verbose-log

So the only use of this has been that *if* we had failure in one of
these tests we could e.g. in CI see which test failed based on the
test number. Now we'll need to look at the full verbose logs to get
that same information.

I think this trade-off is acceptable given the reduction in
complexity, and it brings these tests in line with other similar
tests, e.g. the reftable tests added in [4] will be condensed down to
just one test, which invokes the C helper:

	$ ./t0032-reftable-unittest.sh
	ok 1 - unittests
	# passed all 1 test(s)
	1..1

It would still be nice to have that ":: -v" form work again, it
never *really* worked, but even though we've had edge cases test
output screwing up the TAP it mostly worked between d998bd4ab67 and
[3], so we may have been overzealous in forbidding it outright.

I have local patches which I'm planning to submit sooner than later
that get us to that goal, and in a way that isn't buggy. In the
meantime getting rid of this special case makes hacking on this area
of test-lib.sh easier, as we'll do in subsequent commits.

The switch from "perl" to "$PERL_PATH" here is because "perl" is
defined as a shell function in the test suite, see a5bf824f3b4 (t:
prevent '-x' tracing from interfering with test helpers' stderr,
2018-02-25). On e.g. the OSX CI the "command perl"... will be part of
the emitted stderr.

1. fb32c410087 (t/test-lib.sh: add test_external and
   test_external_without_stderr, 2008-06-19)
2. d998bd4ab67 (test-lib: Make the test_external_* functions
   TAP-aware, 2010-06-24)
3. 614fe015212 (test-lib: bail out when "-v" used under
   "prove", 2016-10-22)
4. ef8a6c62687 (reftable: utility functions, 2021-10-07)

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [Tiktodz/android_kernel_asus_sdm660](https://github.com/Tiktodz/android_kernel_asus_sdm660)@[5e0599a826...](https://github.com/Tiktodz/android_kernel_asus_sdm660/commit/5e0599a82638105b503969144627431ee79df75e)
#### Monday 2022-08-22 14:40:12 by Dave Chiluk

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
Signed-off-by: Kneba <abenkenary3@gmail.com>

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[3d56e6da52...](https://github.com/mrakgr/The-Spiral-Language/commit/3d56e6da52ec2231db0de398458f08457a5898da)
#### Monday 2022-08-22 15:48:30 by Marko Grdinić

"3:10pm. Done with the bath. Let me try one more thing on DALLE. Skeletons.

> Skeletons howling in the darkness of a dilapidated city.

This is a bit cool, but again, not what I am looking for.

> Howling skeletons in the darkness of a dilapidated city as the deathly, black fog devours the flesh from their bodies. Digital art.

'It looks like this request may not follow our content policy.'

> Howling skeletons run screaming through the dark streets of a dilapidated, post-apocalyptic city. Digital art.

A bit better, but why do none of them have their arms raised.

> Howling skeletons run screaming through the dark streets of a dilapidated, post-apocalyptic city. Digital art, trending on ArtStation, 4k, highly detailed.

Maybe I should have them howl at the skies?

> Howling skeletons run screaming through the dark streets of a dilapidated, post-apocalyptic city. Digital art, trending on ArtStation, 4k, highly detailed.

Let me try this one. Er, where did the 'foggy' go?

> Howling skeletons run screaming through the dark, densely foggy streets of a dilapidated, post-apocalyptic city. Digital art, trending on ArtStation, 4k, highly detailed.

This time for real. Actually, for the previous input, there are some cool images. I could potentially use them. Also I could swear I had put in howling at the skies. Where did that disappear?

> Skeletons howl at the skies as they run screaming through the dark, densely foggy streets of a dilapidated, post-apocalyptic city. Digital art, trending on ArtStation, 4k, highly detailed.

Let me try this. These are basically the bad end scenes.

Damn it, why are these skeletons so stiff. Raise their arms damn it.

> Skeletons howl at the skies, their arms raised, as they run screaming through the dark, densely foggy streets of a dilapidated, post-apocalyptic city. Digital art, trending on ArtStation, 4k, highly detailed.

3:30pm. This is a bit interesting.

> Skeletons howl at the skies, their arms raised, as they run screaming through the dark, densely foggy streets of a dilapidated, post-apocalyptic city. Black mists suffuse them. 3d render.

Let me try this.

> 3 Skeletons howl at the skies, their arms raised, as they run screaming through the dark, densely foggy streets of a dilapidated, post-apocalyptic city as the fog devours them. 3d render.

I gets the number of skellys right.

> 3 Skeletons howl and grasp at the skies, their arms raised, as they kneel on the dark, densely foggy streets of a dilapidated, post-apocalyptic city as the fog devours them. 3d render.

I have only 10 credits left.

> 3 Skeletons howl and grasp at the skies, their arms raised, as they run, or kneel facing upwards on the dark, densely foggy streets of a dilapidated, post-apocalyptic city as the fog devours them. 3d render.

Let me try this.

> 3 Skeletons howl and grasp at the skies, their arms raised, as they run forward, or kneel facing upwards on the dark, densely foggy streets of a dilapidated, post-apocalyptic city as the fog devours them. Anime style.

This is really goofy.

> Black fog covers the 3 skeletons who howl and grasp at the skies, their arms raised, as they run forward, or kneel facing upwards on the dark, densely foggy streets of a dilapidated, post-apocalyptic city. Photo.

Let me try this.

> Black fog covers the a skeleton who howls and grasps at the skies, arms raised, as he kneels facing upwards on the dark, densely foggy streets of a dilapidated, post-apocalyptic city. Photo.

Let me try singular.

3:45pm. > Black fog covers the a skeleton who howls and grasps at the skies, arms raised, as he kneels facing upwards on the dark, densely foggy streets of a dilapidated, post-apocalyptic city. Digital art, trending on art station, detailed.

I think I struck gold with this. Not exactly what I had in mind, but there are pretty good.

> Black fog covers the an ivory boned skeleton who howls and grasps at the skies, arms raised, as he kneels facing upwards on the dark, densely foggy streets of a dilapidated, post-apocalyptic city. Digital art, trending on art station, detailed.

Let me try this. I have only 2 creds left.

3:50pm. I guess I am done with DALLE for real this time. No way am I paying for creds. Some of these images are quite interesting to look at, but I wouldn't have paid for them.

Is the SD out yet?

3:55pm. Nope. Let me see if I can do some writing.

$$$

(Heaven's Key, Computer shop)

Vividly, the image before me crystalized into my eyes. In front of me, past the glass pane of the shop were cores! Brain cores! Shining, gleaming, brain cores!

Excited, I ran quickly into the shop, not even realizing how strange it was that while all the other shops were locked, this one didn't even have a lock on the door. The door just swung open for me automatically.

I grabbed a brain core off the shelf, using a mental command I tried connecting to it, and found that it worked. It worked just like the real thing. The brain conversion options were already there, but I could not use it as my brain was already a core, even in the simulated world. Using the core I grabbed off the shelf, I could see a diagram of my own brain. My thoughts turbulent, I realized that all the NPCs here could in fact enter the self-improvement loop and become the Inspired themselves. I thought I had huge advantages, but that wasn't the case.

If I had something special, it is not talent or intelligence, but desire.

I wanted power, but as it happens, I was the only one in this world who was filling to pay the price for it.

I thought it might as well be me in Mickey's place. If nobody gave me a chance, I would just be another ghost in the garden, but that is not the case. The chance has always been there, but Mickey never took it. I understand it now.

I am special, and it is my desire that makes me so. Whoever made this world saw to it that justice existed in it.

It is what I would have done. A universe where all of those with desire can rise is a just one. It is enough to give a chance to other people, it is not anyone's responsibility to make them want to take it.

I clutch the core to my chest and then pocket it, intent on bringing it out of here. My mind that was wavering becomes steely and I decide.

I won't take it easy on the NPCs, and I won't regret the battles that are to come.

I swear it on my desire, that I will rise. I will escape this city and into the real world beyond.

(Heaven's Key, Streets)

I march out of the shop, intent on my destination. At this point due to all the aimless wandering, I've become completely lost, but it should not be hard to find my way back to the inn. I scale one of the larger apartment buildings, and from the high vantage points of the external corridor, in the distance spot the rollercoaster I rode with Lily. Establishing the direction, I get back to the streets and head towards it. It has been a couple of hours since I went out into the city, and in a few more I am guessing the morning should arrive. I remember that cores exist in this world, and on mental command I try accessing, not the real world core which houses my actual self, but the one in the game. A sense connects to it, and I bring up the time.

4:38am.

I have time. If it becomes known that I slipped out of the inn during the night, Lily might get suspicious of me, I do not want her to think that I am anything more than an easy mark. I want her to show me around more casinos. Right now she is my only connection here.

It won't take me more than an hour and a half to get back to the perimeter, but then I'll have to spend time figuring out where the inn was.

I get an idea, and try accessing the core I pocketed from the computer shop. I tried searching for a map application, and to my pleasant surprise I found it. The game core, I'll call it that as opposed to the main core I am on, has a tracking ability. As long as I make use of this, I'll never get lost again in the future.

I am feeling pretty lucky right now. I mean, I just found some guy in a park to talk to, as well as a computer shop. It is not like finding some priceless treasure by accident, but everyone in this world is out to get me, so finding my footing, and so quickly, is a large gain.

Block by block, I make my way to the perimeter. In the distance, I can see the sun's rays starting to break out.

(Heaven's Key, Perimeter)

...

$$$

5:20pm. Done with lunch.

5:25pm. I wrote 1.5 pages. 760 words so far.

This serves as an ice breaker. Right now I do not feel like writing anymore for the day.

5:30pm. That first scene was quite good. I think the me from 2014 who was in the depths of despair at that time would have been enlightened. The way the story is going feels very straightforward and I am not constantly assaulted by contradictions in my worldview. Maybe I've matured just a little.

Going into the future I'll definitely pick better friends than the ones that I had in the past. I'll keep to myself and look out for my own interests. I won't try to go out on a limb like before. Simple goals, cultivated one step at a time is what will get me to success.

I have 2 followers right now, maybe tomorrow I'll have 3. Who knows. Maybe the 2 that I have now is all that will ever be. Either way, I'll just focus on my writing and not worry about it.

I've failed so much, and I am yet to accomplish anything I've ever really wanted. Is the universe I live in a one where all those with desire can rise? Maybe it is not, so some depression is suitable. But I'll borrow some attitude from a certain demonic cultivator with a heart of steel and accept it as it comes.

The paths I've been on are simply too difficult. I need something lighter. Getting to the third follower is a goal I can accept.

5:45pm. It does not matter if other people accept my beliefs or not. I was the one who could not accept them before. I could accept the truth of the self improvement loop, but not the way this universe truly was.

Right now, how about Pathfinder and anime? Tomorrow, I'll most likely be trying out SD. Today I got my fill of DALLE."

---
## [DEFRA/water-abstraction-service](https://github.com/DEFRA/water-abstraction-service)@[2d323eb53e...](https://github.com/DEFRA/water-abstraction-service/commit/2d323eb53ec13b6483b95f8dc3c3cfcede5a8ef3)
#### Monday 2022-08-22 16:42:35 by Alan Cruikshanks

Set up background tasks module (#1784)

https://eaflood.atlassian.net/browse/WATER-3745

> We have started this change again because [PR #1766](https://github.com/DEFRA/water-abstraction-service/pull/1766) had gone so far done a possible path that it made merging/rebasing overly complex. Simpler to start again!

We are separating out our background BullMQ tasks so that they run on a background instance. The foreground (existing instance) can then just focus on handling requests from the UI, including adding the initial jobs that kick off background processes.

We had initially looked at splitting out `QueueManager` into a `WorkerManager` (see [PR #1766](https://github.com/DEFRA/water-abstraction-service/pull/1766)). But we then found that the background instance also needs to know about queues. This is because a number of the `onComplete()` worker handlers add new jobs to queues based on the results of the main worker handler.

So, we moved a number of the changes we were making into separate PR's, which focused on refactoring the QueueManager ready to allow us to make the changes we need to support a background instance.

This PR is those changes.

** Notes

- Use fork mode for service-background
  For a standard web-app or API you would typically run it using [cluster mode](https://pm2.keymetrics.io/docs/usage/cluster-mode/). This is some cleverness built into Node.js which allows multiple processes to be spawned that still share the same ports. How many is determined by the number of CPU's available. It's a codeless way to scale an app based on the resources available. To that pm2 will also act as a load balancer between the processes.

  By default pm2 runs apps using fork mode (would love to link to a page but there ain't none!) This is the equivalent of what you do when running it locally. If you wanted to start a second instance you'd have to run it on a different port.

  The reason for the change is because we are not using the background instance as a web app or API. Instead, we're using it to run processes in the background that should only be run once. What is happening in production at the moment is

  - normal service starts up using pm2 with config set to cluster mode and `max` instances. Assume pm2 finds 2 CPU's so creates 2 instances of the app
  - each app will instantiate BullMQ workers as part of start up (it will also try to register the queues in parallel!) Current count is we have 13 of them, so that's 26 additional processes started behind the scenes on top of our 2 apps
  - a job is added to a queue and both workers created for the queue fight to process it
  - then double all this because we have 2 EC2 instances running in AWS

  A background job is only expected to be run once so typically you'll designate one of your EC2 instances to handle them. However, we were treating our background service like a scaling web-app which makes controlling and debugging much more complicated.

  We've still to think about how we handle a worker per EC2 instance (it may be fine). But on an instance there should just be 1 background service running.

- Wrap worker forking in service check
  What do you know!? There is _another_ way we create blasted workers/jobs in this service 😫

  In this case we are forking a child process and doing all the work in there. The BullMQ job triggers the work in the child process so it looks like the worker is done. The work in this case is like syncing WRLS invoices with all the transaction detail in the CM is taking place. The problem was the code was creating the fork as soon as the file was required. As this is happening in order to pass it to the QueueManager to register the queue, it meant the foreground service was spawning sub processes that would never be used. After reading the PM2 docs, the app name set in ecosystem.config.json is made available as an env var to the running apps. So, we use that to check if we are running in the foreground or background instance. Then, only if we are on the background instance do we create the fork and spawn the child process.

  Note - This forking was supposedly done as a performance optimisation. We don't believe it helps with performance (in fact it possibly degrades it) but it would solve a worker taking to long and becoming susceptible to loosing its job lock and therefore failing. We really need to remove this unnecessary complexity.

- Refactor job files
  We make a few small changes to `process-charge-version-year.js` and `update-invoices.js`

  - Add `'use strict'` to the top of `update-invoices`
  - Destructure `fork` from `child_process`
  - Sort out `require()` statements (vendor, project then constants)
  - Change the `exports` section to a standard `module.exports`

- Increase V8's old memory section via pm2 config
  `--max-old-space-size` is an argument you can set when calling node that it will pass on to tje underlying V8 engine. From the node documents

  > Sets the max memory size of V8's old memory section. As memory consumption approaches the limit, V8 will spend more time on garbage collection in an effort to free unused memory.
  >
  > On a machine with 2 GiB of memory, consider setting this to 1536 (1.5 GiB) to leave some memory for other uses and avoid swapping.
  <https://nodejs.org/api/cli.html#useful-v8-options>

  The default is 2GB which can be seen by checking `heap_size_limit` after doing the following

  ```
  node

  > v8.getHeapStatistics()
  {
    ....
    heap_size_limit: 2197815296,
  }
  ```
  <https://stackoverflow.com/a/63495296/6117745>

  The essence of this change is to improve performance. The background instance is where all our work is done and where we often have to hold a large amount of data in memory. The theory is the more memory you've got to hold stuff, the less the garbage collector has to be called in to ensure you don't run out of memory. We're only setting this when running in `production` mode, which will only be when running in our AWS environments.

- Only create worker and scheduler in background
  We coming to the end of our changes to support splitting the work of the service project. Both foreground and background need to know about the queues. But only the background instance needs to create the instances of Worker and QueueScheduler to process the queues. So, we add a check (similar to what we did with the jobs that are using `fork()`) into the `QueueManager` to only create them if we are the background instance.

---
## [apple/swift-protobuf](https://github.com/apple/swift-protobuf)@[e47f7304c9...](https://github.com/apple/swift-protobuf/commit/e47f7304c909f2849648c790233cd4894a5477c5)
#### Monday 2022-08-22 17:16:50 by FranzBusch

Add SPM plugin

# Motivation
SPM is providing new capabilities for tools to expose themselves as plugins which allows them to generate build commands. This allows us to create a plugin for `SwiftProtobuf` which invokes the `protoc` compiler and generates the Swift code. Creating such a plugin is greatly wanted since it improves the usage of the `protoc-gen-swift` plugin dramatically. Fixes https://github.com/apple/swift-protobuf/issues/1207

# Modification
This PR adds a new SPM plugin which generates build commands for generating Swift files from proto files. Since users of the plugin might have complex setups, I introduced a new `swift-protobuf-config.json` file that adopters have to put into the root of their target which wants to use the new plugin. The format of this configuration file is quite simple:

```json
{
    "invocations": [
        {
            "protoFiles": [
                "Foo.proto"
            ],
            "visibility": "internal"
        }
    ]
}

```

It allows you to configure multiple invocations to the `protoc` compiler. For each invocation you have to pass the relative path from the target source to the proto file. Additionally, you have to decide which visibility the generated symbols should have. In my opinion, this configuration files gives us the most flexibility and more complex setups to be covered as well.

# Open topics

## Hosting of the protoc binary
Hosting of the protoc binary is the last open thing to figure out before we can release a plugin for `SwiftProtobuf`. From my point of view, there are three possible routes we can take:

1. Include the `artifactbundle` inside the `SwiftProtobuf` repository
2. Include the `artifactebundle` as an artifact on the GH releases in the protobuf repo
3. Extend the the artifact bundle manifest to allow inclusion of URLs. This would require a Swift evolution pitch most likely.

However, with all three of the above we would still need to release a new version of `SwiftProtobuf` with every new release of `protoc`.

# Future work

## Proto dependencies between modules
With the current shape of the PR one can already use dependencies between proto files inside a single target. However, it might be desirable to be able to build dependency chains of Swift targets where each target includes proto files which depend on protoc files from the dependencies of the Swift target. I punted this from the initial plugin because this requires a bit more work and thinking. Firstly, how would you even spell such an import? Secondly, the current way of doing `ProtoPathModuleMapping` files is not super ideal for this approach. It might make sense to introduce a proto option to set the Swift module name inside the proto files already.

# Result
We now have a SPM plugin that can generate Swift code from proto files. To use it, it provides a configuration file format to declare different invocations to the `protoc` compiler.

---
## [EnlightenedTop/OlimpusHotel](https://github.com/EnlightenedTop/OlimpusHotel)@[0300ba82eb...](https://github.com/EnlightenedTop/OlimpusHotel/commit/0300ba82eb5a27295fb7ff68678e10bdbf98f3a9)
#### Monday 2022-08-22 18:02:34 by Popa Cristian Alexandru

Add files via upload

Everyday is a learning day , today i learned first day how to work on reception and also broke my phone glass ... funny nonetheless , sometimes you must lose something to gain something else , lately defently i get more and more this ideea in my head , but also i get less and less attached to things or places , not worthy , or ideeas either or thoughts , they come and go and so do design choises , for example i feel like those new changes really click , idk tho , keep learning more and more everyday and i fucking love it , anyway hope i can get this project to the end of its life for now , just must be sure it looks fine and profesional

---
## [opentibiabr/otservbr-global](https://github.com/opentibiabr/otservbr-global)@[fbd70d116c...](https://github.com/opentibiabr/otservbr-global/commit/fbd70d116c260a94902c2e0164ceca94023f2f28)
#### Monday 2022-08-22 18:09:17 by rigis1

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
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[76786e510f...](https://github.com/pytorch/pytorch/commit/76786e510fce552daf9654d34b270c4b08641ae6)
#### Monday 2022-08-22 19:19:00 by Andrew Gu

Update base for Update on "[FSDP] Generalize prefetching; lower unshard/reshard to handle"


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



[ghstack-poisoned]

---
## [oxen-io/oxen-core](https://github.com/oxen-io/oxen-core)@[9c9552380d...](https://github.com/oxen-io/oxen-core/commit/9c9552380ddecc57965e2e393454ef9d880cb803)
#### Monday 2022-08-22 20:25:23 by Jason Rhinelander

Make hooks use exceptions on error rather than bool returns

bool returns suck in general, but in most cases here they are also a
pain in the ass because *each* place that returns false is also issuing
a log statement.  If only there were a way to return error information
to the common caller to have the common caller handle it... oh wait,
there is!

---
## [VOREStation/VOREStation](https://github.com/VOREStation/VOREStation)@[4c0245a1b0...](https://github.com/VOREStation/VOREStation/commit/4c0245a1b03250deaf58072545aec079b0722e96)
#### Monday 2022-08-22 20:28:07 by C.L

Adds Toxins & Cloneloss digestion damage.

- Adds Toxins as a digestion damage type.
- Adds Clone damage as a digestion damage type.

- Cloneloss gives 2x nutrition than brute/burn since it is exceptionally harder to heal from. (not that it matters)

So now slime characters can actually RP out sucking out your DNA and leaving you a DNAless husk while slamming you with toxins like xenobio slimes can.

---
## [robertnsu/Terminal](https://github.com/robertnsu/Terminal)@[9ccd6ecd74...](https://github.com/robertnsu/Terminal/commit/9ccd6ecd744890b856f3d8a39ff0616c0e34d4fb)
#### Monday 2022-08-22 21:16:15 by Mike Griese

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

(cherry picked from commit 855e1360c0ff810decf862f1d90e15b5f49e7bbd)

---
## [Offroaders123/NBT-Parser](https://github.com/Offroaders123/NBT-Parser)@[2fcd6fa4f0...](https://github.com/Offroaders123/NBT-Parser/commit/2fcd6fa4f064d29e3ec2b9ac874d02f86bffbade)
#### Monday 2022-08-22 21:38:34 by Offroaders123

Tag Byte Type + Type Naming + GetTagByte

Lots of cool stuff! This is edging a bit closer to being API-like now :)

I keep reminding myself that I haven't even touched the writing half yet though, haha! These classes will makes things a lot easier though, the object structure actually feel like something maybe trustworthy at this point.

I can't wait to make something with this! I'm definitely going to add NBT editing as plain text to STE, that was one of my original use case ideas for this project. That also led me to work on NumText a bit some more a while back. Those changes haven't made it into stable yet, but a lot of my projects have moved forward, especially thanks to the more recent things I've looked into.

The biggest things in my JS dev world at the moment:
Web Components, ES6 Classes, ES Modules, Node (yes, I finally am getting used to that, haha), Promises / Async - Await, Compression Streams, TypedArrays (byte streams as a whole), Endianness (DEFINITELY deserves it's own category), and very recently, TypeScript! (.d.ts, and now full .ts)

These have been huge steps forward for me, and I really see how far it is pushing me forward from my projects just a short time ago. I look back at my practices before, and so many things have added together to make a big giant upgrade for my personal experience. I really like what can be done with all of these, and with how great learning these have been, I can't wait to eventually come back around to look at things like WebRTC. When I first looked into it, it was a bit over my head I think, and now that I understand the language structure a bit further, I have a bigger step up to wrap my head around it.

This library as a whole has been a great project for me, and it pretty much added a majority of those things I just listed to my experience catalog.

Well, thanks for vising my "blog", hope you like the writing XD

*Note: I also want to look into making my own page for my profile as an artist too, so like a landing page for album showcases and things like that. I have a lot of fun making artwork for my songs, and having an awesomely-styled website to go along with them sounds super cool to work on. Expect that eventually down the road too! Maybe Markdown would work best there :)

---
## [elocemearg/atropine](https://github.com/elocemearg/atropine)@[e18b6a6274...](https://github.com/elocemearg/atropine/commit/e18b6a62743964fbbf00fcba23a00b3e93fadc35)
#### Monday 2022-08-22 21:42:52 by Graeme Cole

Automatic Prunes - no more creating imaginary players with rating 0

If you don't have a multiple of three players but you're playing a
three-to-a-table event, until now you've had to add one or two Prune
players, with a rating of zero, to make up the numbers. This is
annoying, especially as you then have to remember to withdraw such a
Prune when another player joins late, or add/reinstate a Prune when a
player withdraws.

Let's introduce the Automatic Prune, a virtual player which turns up
only when fixture generators need it!

The PLAYER table in a newly-created tournament now comes with a row
already in it, with id -1, rating 0, and name "Prune".

This row is not deleted by resetting the player list, and nor does it
show up in any normal listing of players such as the standings table.
However, it can be referenced by the GAME table, and displayed as one of
a game's players. Fixture generators can thus decide how many Prunes are
needed based on the table size and the number of (real) players, and add
the Automatic Prune to as many tables as necessary.

Obviously all the fixture generators have been tweaked to support this.
Determining whether the database supports the automatic Prune, and if
so, which table(s) it sits at, is now the fixture generator's problem.

countdowntourney.get_auto_prune() returns a PrunePlayer, which extends
Player. The fixture generators use this object to represent a prune.
However, if the tourney database version is < 1.2.1, this throws an
exception to avoid trying to use the automatic prune on databases
without that extra player row. Fixture generators should call
tourney.has_auto_prune() to determine whether the tourney supports
automatic prunes.

Atropine version is now 1.2.1.

We don't need more than one automatic prune. If we're two short of a
multiple of three, we can just put the same Prune on two tables
rather than having two separate Prunes. The thing about a player whose
only job is to not exist and do nothing is that it's really good at
doing that in two places at once.

Various places that select * from the PLAYER table now have a "where id
>= 0" condition. ranktest.py has been tweaked to not expect Prune in the
standings, and not to manually add Prune to the player list. There are
a few other tweaks, which I won't further bulk out this already long
commit message to describe, to handle this strange new player which
appears in games but not in a standings table or player list.

Various other things which used to count Prune as a player now no longer
do so. This includes the name-to-table index and Tuff Luck. For the
purpose of the Tim Down Award, if you played the Automatic Prune, that
opponent is considered to have finished in last place, or joint last if
there are other prunes.

Finally, you can still create Prune players the "old" way, and this
works as before - create a player with a rating of zero. However, from
now on this is unlikely to be useful unless you need to create fixtures
on an old tourney database.

---
## [lyro41/tsorcRevamp](https://github.com/lyro41/tsorcRevamp)@[497b91fb91...](https://github.com/lyro41/tsorcRevamp/commit/497b91fb91317eb98fbc819ec0645b15910d553d)
#### Monday 2022-08-22 22:19:57 by timhjersted

Phoenix Trio Revamp 1.0 + more

- The Phoenix bosses now have several new attack elements, some of which activate during a new 2nd phase at half health
-Corrupted Jellyfish renamed Obsidian Jellyfish and given wider spawn pool and HM stats, enabling potential interesting gameplay interactions with the map, (intentionally getting hit can give 30s of lava immunity), to go with the obsidian theme, they also have 999 defense requiring 5 or 10 hits to kill
-Created new banner placeholder sprite
-Added "Cracked Dragon Stone" which provides early HM access to On Fire! immunity, which will be useful during The Rage fight (can be crafted from Cobalt Bars or drops from Ancient Demon event as an expert drop)
-Bloodred Moss Clump now heals for 30HP, up from 20
-Ancient Demon now has a boss bag
-Ancient Demon and Oolicile Demon have better boss bag sprites
-Pwnhammer removed as a Wall of Flesh drop, WoF now drops Molten Pickaxe, which is also now used to craft Mjolnir
-Nerfed Corrupted Tooth healing, now has a 1/20 chance when attacking corrupted enemies, 1/10 chance for anything else
-Basilisk walkers and shifters as well as the Dworc family now has a chance to drop Bloodred Moss Clump
-Mutant Toads can now swim in water and have HM stats, plus 2s of Venom debuff in HM
-EoW and Golem damage stats bumped again slightly
-Cursed Dragon's Breath and Frozen Dragon's Breath now activate their most brutal debuffs after The Hunter and The Sorrow have been defeated
-Frozen Dragon's Breath adds 3s of Frostburn
-Enemy Black Fire kill sound changed
-Added Ice Spirit projectile which has a homing effect
-The Hunter's Miracle Sprouter/Vines emit more light for visibility
-Worm Food and Pwnhammer blocked via no drop/craft list

---
## [lyro41/tsorcRevamp](https://github.com/lyro41/tsorcRevamp)@[63754eeb2a...](https://github.com/lyro41/tsorcRevamp/commit/63754eeb2a66d46912061094173e2fdaf6ce678d)
#### Monday 2022-08-22 22:19:57 by timhjersted

More Phoenix Boss Changes +

-Cracked Dragon Stone also grants immunity to slow and chilled, and costs more souls
-Hellkite Dragon and Seath now interact with the environment in a very cool way (they hit walls instead of pass through them and fly above the ground instead of diving into it more often) but they can still phase through walls when needed to reach the player (further experimentation needed with the 10 and 100 value to find the best balance). It phases through walls more liberally currently to be on the safe side.
--
Phoenix Changes:
-Adjusted health stats for the phoenix birds so they reflect the in-game numbers (health is unchanged besides a small bump to the Rage)
-2nd phase warning message lasts 3x long
-Enhanced the Rage with 2 extra attacks and a 'final stand' phase NPC spawn
-The Sorrow now triggers slow at close range during 2nd phase and chilled at long range
-The Sorrow has 1 extra attack during 1st phase and also spawns animal kin to aid herself
--
-Meteor Heads do extra damage in HM for Rage fight
-Cursed Dragon's breath triggers poison debuff instead of bleeding
-Enemy Cursed breath is way less harsh with the weak debuff
-Attempted to add hostile Hellwing projectile with homing but couldn't get the animation working
-Fixed Ancient Oolcile Demon health

---
## [ThatWackGuy/RWDCMMCSS](https://github.com/ThatWackGuy/RWDCMMCSS)@[5bfe9ac0f0...](https://github.com/ThatWackGuy/RWDCMMCSS/commit/5bfe9ac0f0b66000f2c8006827af9d08dcb4d72b)
#### Monday 2022-08-22 22:24:33 by Wack

1.1.0 porlsgone (#3)

# 1.1.0 - Porls are hard now fuckers

## Added
Sponge recipe (16 haybales and a lot of water + shit amounts of time)
Netherrack recipe (pouring blood into cobblestone in a casting basin)
Molten Quartz Enriched Iron
iterable modifier - gives 2 modifier slots. Stacks to 1
Armored modifier - trades 2 modifier slots for a defense slot. Stacks to 1
(Both made by @chartuch)

## Changed
Pearl recipe. Now uses a 64k storage part and 8 HOP Graphite
Calcite recipe. Now made by casting
Quartz grind ratio. Now 3 to 5 with mills and grinders respectively
Every chest loot table in the game (now has a chance of porls) :trollface:

---
## [Bee-Have/cpp_duck](https://github.com/Bee-Have/cpp_duck)@[3a9acd1417...](https://github.com/Bee-Have/cpp_duck/commit/3a9acd1417ea283b44cf0e80365a205828a61d25)
#### Monday 2022-08-22 22:52:22 by Albe MARINI-AUDOUARD

🚧 -Saddly i am dumb and i don't remember what i did last time, fuck you past me, fuck you !

---

