## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-01-20](docs/good-messages/2022/2022-01-20.md)


1,873,884 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,873,884 were push events containing 2,893,270 commit messages that amount to 231,776,728 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 30 messages:


## [Ebin-Halcyon/Skyrat-tg](https://github.com/Ebin-Halcyon/Skyrat-tg)@[eb384bd2d7...](https://github.com/Ebin-Halcyon/Skyrat-tg/commit/eb384bd2d72a5b23dd9785cc06815049d507d3d5)
#### Thursday 2022-01-20 00:11:09 by Useroth

Telemetry 'n shit (#10810)

* Refactors dbcore and limits the maximum amount of concurrent async queries to a variable amount (#59676)

Refactors dbcore to work off a subsystem if executed async and limits the maximum amount of concurrent async queries to 25.

This has been tested locally on a mysql docker image and there were no crashes (as long as you didn't run it with debug extools) + data was getting recorded fine.
Why It's Good For The Game

May or may not resolve terry crashes, however, each query creates a new thread which takes up 2mb, preventing the game from using that 2mb. This can lead to ooms if they stack up, e.g. due to poor connectivity. This solves that issue.

maintainer note: this did not actually resolve the crashes, but has value anyway. Crashes were sidestepped fixed by finding out Large Address Awareness works

cl
refactor: Refactors dbcore.dm to possibly resolve the crashes that happen on Terry.
/cl

* Fixes an oversight in database code and cleans up telemetry (#64177)

As it is right now, we never actually clear the temporary list processing_queries
So if the subsystem is for some reason unable to complete a run, we will just whip right back around to it again
If it's been long enough, this could even cause horrific log spam. There was just now a manuel round with roughly 30k undeleted query errors. not good.

But what was actually not deleting you may ask?
Well

When you create a db request, a 5 minute timer starts. after those 5 minutes are up, the request is qdeleted by the db subsystem
This is to prevent the creation of unused requests, and to handle requests that are never cleaned up

Telemetry code was creating all of its db requests inside a for loop that could check tick, and then later
attempting to call them in series

Since requests by default sleep, this almost always lead to undeleted queries, which harddel'd given long enough periods

I've fixed this by moving the data gathering away from the query creation
Why is it good for the game

I was working on atmos code, happy, safe in my delusion, when suddenly I got a ping from tattle freaking out over 200 undeleted queries a second
This resolves that issue, so I can once again live in peace
Changelog

cl
admin: Telemetry code will spam you with undeleted query logs much less often now!
server: Improved how the db subsystem handles undeleted queries, should never have an incident like that again
/cl

* Fixes an error in telemetry queries (#64205)

* Hardsynced time_track.dm with upstream

Co-authored-by: Watermelon914 <37270891+Watermelon914@users.noreply.github.com>
Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [aws/aws-cdk](https://github.com/aws/aws-cdk)@[c071367def...](https://github.com/aws/aws-cdk/commit/c071367def4382c630057546c74fa56f00d9294c)
#### Thursday 2022-01-20 00:29:43 by Kaizen Conroy

feat(glue): support partition index on tables (#17998)

This PR adds support for creating partition indexes on tables via custom resources.
It offers two different ways to create indexes:

```ts
// via table definition
const table = new glue.Table(this, 'Table', {
  database,
  bucket,
  tableName: 'table',
  columns,
  partitionKeys,
  partitionIndexes: [{
    indexName: 'my-index',
    keyNames: ['month'],
  }],
  dataFormat: glue.DataFormat.CSV,
});
```

```ts
// or as a function
table.AddPartitionIndex([{
  indexName: 'my-other-index',
  keyNames: ['month', 'year'],
});
```

I also refactored the format of some tests, which is what accounts for the large diff in `test.table.ts`. 

Motivation: 
Creating partition indexes on a table is something you can do via the console, but is not an exposed property in cloudformation. In this case, I think it makes sense to support this feature via custom resources as it will significantly reduce the customer pain of either provisioning a custom resource with correct permissions or manually going into the console after resource creation. Supporting this feature allows for synth-time checks and dependency chaining for multiple indexes (reason detailed in the FAQ) which removes a rather sharp edge for users provisioning custom resource indexes themselves.

FAQ:

Why do we need to chain dependencies between different Partition Index Custom Resources? 
  - Because Glue only allows 1 index to be created or deleted simultaneously per table. Without dependencies the resources will try to create partition indexes simultaneously and the second sdk call with be dropped.

Why is it called `partitionIndexes`? Is that really how you pluralize index?
  - [Yesish](https://www.nasdaq.com/articles/indexes-or-indices-whats-the-deal-2016-05-12). If you hate it it can be `partitionIndices`.

Why is `keyNames` of type `string[]` and not `Column[]`? `PartitionKey` is of type `Column[]` and partition indexes must be a subset of partition keys...
  - This could be a debate. But my argument is that the pattern I see for defining a Table is to define partition keys inline and not declare them each as variables. It would be pretty clunky from a UX perspective:
    ```ts
    const key1 = { name: 'mykey', type: glue.Schema.STRING };
    const key2 = { name: 'mykey2', type: glue.Schema.STRING };
    const key3 = { name: 'mykey3', type: glue.Schema.STRING };
    new glue.Table(this, 'table', {
      database,
      bucket,
      tableName: 'table',
      columns,
      partitionKeys: [key1, key2, key3],
      partitionIndexes: [key1, key2],
      dataFormat: glue.DataFormat.CSV,
    });
    ```

Why are there 2 different checks for having > 3 partition indexes?
  - It's possible someone decides to define 3 indexes in the definition and then try to add another with `table.addPartitionIndex()`. This would be a nasty deploy time error, its better if it is synth time. It's also possible someone decides to define 4 indexes in the definition. It's better to fast-fail here before we create 3 custom resources.

What if I deploy a table, manually add 3 partition indexes, and then try to call `table.addPartitionIndex()` and update the stack? Will that still be a synth time failure?
  - Sorry, no. 

Why do we need to generate names?
  - We don't. I just thought it would be helpful.

Why is `grantToUnderlyingResources` public?
  - I thought it would be helpful. Some permissions need to be added to the table, the database, and the catalog.

Closes #17589.

----

*By submitting this pull request, I confirm that my contribution is made under the terms of the Apache-2.0 license*

---
## [chromium/chromium](https://github.com/chromium/chromium)@[e7a4c46875...](https://github.com/chromium/chromium/commit/e7a4c46875b2fc01914d0e1d629383f043acaa55)
#### Thursday 2022-01-20 00:56:25 by Adam Langley

webauthn: remember whether to jump to Windows native UI.

Currently Chrome will immediately trigger the Windows native UI for
WebAuthn unless either:
   1. accounts.google.com is doing caBLEv1 or server-link.
   2. There are paired caBLEv2 phones.

If you're in an enterprise setting where very regular security key
operations are needed then probably neither of those apply. However,
when we enable QR support there'll always be the option to add a phone.
Rather than always showing the Chrome UI first this change does a couple
of things:

   1. Make the option for the native API top of the mechanism selection
      list. Thus you can trigger it by just hitting enter.
   2. Remember whether the last successful registration or assertion
      used the native API or not. If so, do directly to the native API
      next time and only show the Chrome UI if that UI is cancelled.

This isn't perfect, but there are limits to what we can do with
operations split between Chrome and Windows. It means that users who use
physical security keys a lot, and users who use phones a lot, get a good
experience. People who switch between them end up worse off as a
tradeoff. The estimate is that the number of such people is relatively
small.

BUG=1002262

Change-Id: I28d74b42a5c950622cc56b98e4c13c3450071b25
Reviewed-on: https://chromium-review.googlesource.com/c/chromium/src/+/3363266
Reviewed-by: Ken Buchanan <kenrb@chromium.org>
Reviewed-by: Avi Drissman <avi@chromium.org>
Commit-Queue: Adam Langley <agl@chromium.org>
Cr-Commit-Position: refs/heads/main@{#961065}

---
## [maxspells/fulpstation](https://github.com/maxspells/fulpstation)@[c797bf79ea...](https://github.com/maxspells/fulpstation/commit/c797bf79ea71c9fd26f598306753a9abc55427d8)
#### Thursday 2022-01-20 01:06:29 by Pepsilawn

Fixes broken ass area on Helios tation (#440)

* Fixes Helios

* fuck you turbine

* MACHINERY/wish_granter

---
## [OpenVZ/vzkernel](https://github.com/OpenVZ/vzkernel)@[265cb2fe70...](https://github.com/OpenVZ/vzkernel/commit/265cb2fe70498288efb38f60482de3416f2a5bdc)
#### Thursday 2022-01-20 01:08:51 by Vladimir Davydov

mm: introduce transcendent file cache (tcache)

Transcendent file cache (tcache) is a simple driver for cleancache,
which stores reclaimed pages in memory unmodified. Its purpose it to
adopt pages evicted from a memory cgroup on local pressure, so that they
can be fetched back later without costly disk accesses. It works
similarly to shadow gangs from PCS6 except pages has to be copied on
eviction.

https://jira.sw.ru/browse/PSBM-31757

* Usage

 - Enable:
   # modprobe tcache # only if compiled as a module
   # echo Y > /sys/module/tcache/parameters/enabled

 - Disable:
   # echo N > /sys/module/tcache/parameters/enabled

 - Get number of pages cached:
   # cat /sys/module/tcache/parameters/nr_pages

* Implementation notes

 - Fetching/adding a page to tcache implies looking up a tcache pool
   (corresponds to a super block), tcache node in the pool (corresponds
   to an inode), and a page in the node. Pages of the same node are
   organized into a radix tree protected by a single spin lock,
   similarly to pages in an address_space. Nodes of the same pool are
   kept in several RB trees, each of which protected by its own spin
   lock. The number of RB trees is proportional to the number of CPUs,
   and nodes are distributed among the trees using a hash function. This
   is to minimize contention on the locks protecting the trees. Pools
   are kept in an IDR and looked up locklessly.

 - All tcache pages are linked in per NUMA node LRU lists and reclaimed
   on global pressure by a slab shrinker. Also, if we fail to allocate a
   new page for tcache, we will attempt to reclaim the oldest one
   immediately.

 - Once the tcache module is loaded, it is impossible to disable tcache
   completely due to cleancache limitations. "Disabling" it via the
   corresponding module parameter only forbids populating the cache with
   new pages. Lookups will proceed to tcache anyway.

 - Tcache pages are accounted as file pages.

* F.A.Q.

 - Does copying pages to and from tcache affect performance?

   Yes, it does. Fetching data from tcache advances roughly two times
   slower than from the page cache, because one has to copy data twice.
   Below are times of reading a 512M file from a memory cgroup:

   a) without limits:
      536870912 bytes (537 MB) copied, 0.481623 s, 1.1 GB/s
   b) with 100M limit and tcache enabled:
      536870912 bytes (537 MB) copied, 0.974815 s, 551 MB/s

   However, tcache exists not to allow containers whose working set does
   not fit in their RAM operate as fast as they would if there were no
   memory limits at all. Tcache exists to avoid costly disk operations
   whenever possible. For example, if there is a container which would
   normally thrash due to the memory limit and there is some unused
   memory on the host, it is better to allow the container to use the
   free memory to avoid thrashing, because otherwise it will generate
   disk pressure sensible by other containers.

 - Is there any memory overhead excluding the space used for storing
   data pages?

   Practically, no. All the information about pages is stored directly
   in struct page, and no additional handles are allocated per page.
   Per inode radix trees do consume some additional kernel memory per
   page, but its amount is negligible.

 - Does tcache generate memory pressure at the global level? If yes,
   does it affect containers?

   Yes, it generates global pressure and currently it does affect
   containers. This is similar to the issue we had had in PCS6 before
   shadow gangs and vmscan scheduling hacks were introduced, when there
   was the only LRU list for evicted pages (init_gang). We are planning
   to fix it by backporting low limits for memory cgroups. If a
   container is below its low limit, its memory will not be scanned on
   global pressure unless all containers are below their low limits
   (this is a kind of memory guarantee). We will set low limits for a
   container to be equal to an estimate of its working set size (this
   will be done by a user space daemon). Since tcache resides in the
   root memory cgroup, which does not have any memory guarantees (low
   limit equals 0), it will not press upon containers provided the
   system is properly configured.

 - Why cannot we use low limits instead of hard limits then?

   Low limits are unsafe by design. There is no guarantee that we will
   always be able to reclaim a cgroup back to its low limit. There are
   anonymous and kernel memory, which are sometimes really hard to
   reclaim. We could introduce a separate limit for them (anon+swap),
   but it will never get upstream (we tried).

 - Why is it better than what we have in PCS6?

   Primarily, because the idea of wiring sophisticated vmscan rules into
   the kernel, as we have done in PCS6 (vmscan scheduler) is dubious
   since it makes changing its behavior really painful. There are other
   points too:

   + The PCS6 memory management patch is really intrusive: it has
     sprouted its slimy tentacles all around the mm subsystem (rmap.c,
     memory.c, mlock.c, vmscan.c). We will hardly ever manage to push it
     upstream, so we will most likely have to carry it for good. This
     means each major rebase will turn into a torment. OTOH tcache code
     is isolated in a module and therefore can be easily ported back and
     forth.

   + Thanks to data copying, we can do funny things with the
     transcendent page cache in future, such as compression and
     deduplication. There were plans to implement compressed file cache
     upstream (zcache), but unfortunately it is still not there, and
     nobody seems to care about it. Nevertheless, sooner or later it
     will be introduced (may be, I'll facilitate this process), and we
     will be able to seamlessly switch to it from tcache. Tcache will be
     still useful for testing though.

 - In PCS6 there are per container shadow lists, while you have only the
   global LRU for all tcache pages. Is there any plans to introduce per
   super block or per memory cgroup LRUs?

   I am still unconvinced that we really need it, because it is not
   clear to me what policy we should apply per container on reclaim. It
   smells like one more heuristic, which I am desperately trying to
   avoid. Current design looks simple and sane: there are guarantees for
   containers provided by their limits, and they are competing fairly
   for the rest of the memory used for caches.

 - What about swap cache?

   There are plans to implement a similar driver for frontswap (tswap)
   or backport and use existing zswap. There may be problems with the
   latter though, because it currently does not support reclaim, and it
   will be tricky from the technical point of view to introduce it.

 - Any plans to push tcache upstream?

   No, because its use case looks too narrow to me to be included into
   the vanilla kernel. I am planning to concentrate on zcache instead.

Signed-off-by: Vladimir Davydov <vdavydov@parallels.com>

+++
mm/tcache: restore missing rcu_read_lock() in tcache_detach_page() #PSBM-120802

Looks like rcu_read_lock() was lost in "out:" path of tcache_detach_page()
when tcache was ported to VZ8. As a result, Syzkaller was able to hit
the following warning:

  WARNING: bad unlock balance detected!
  4.18.0-193.6.3.vz8.4.7.syz+debug #1 Tainted: G        W        ---------r-  -
  -------------------------------------
  vcmmd/926 is trying to release lock (rcu_read_lock) at:
  [<ffffffff848ed2e0>] tcache_detach_page+0x530/0x750
  but there are no more locks to release!

  other info that might help us debug this:
  2 locks held by vcmmd/926:
   #0: ffff888036331f30 (&mm->mmap_sem){++++}, at: __do_page_fault+0x157/0x550
   #1: ffff8880567295f8 (&ei->i_mmap_sem){++++}, at: ext4_filemap_fault+0x82/0xc0 [ext4]

  stack backtrace:
  CPU: 0 PID: 926 Comm: vcmmd ve: /
               Tainted: G        W        ---------r-  - 4.18.0-193.6.3.vz8.4.7.syz+debug #1 4.7
  Hardware name: Virtuozzo KVM, BIOS 1.11.0-2.vz7.2 04/01/2014
  Call Trace:
   dump_stack+0xd2/0x148
   print_unlock_imbalance_bug.cold.40+0xc8/0xd4
   lock_release+0x5e3/0x1360
   tcache_detach_page+0x559/0x750
   tcache_cleancache_get_page+0xe9/0x780
   __cleancache_get_page+0x212/0x320
   ext4_mpage_readpages+0x165d/0x1b90 [ext4]
   ext4_readpages+0xd6/0x110 [ext4]
   read_pages+0xff/0x5b0
   __do_page_cache_readahead+0x3fc/0x5b0
   filemap_fault+0x912/0x1b80
   ext4_filemap_fault+0x8a/0xc0 [ext4]
   __do_fault+0x110/0x410
   do_fault+0x622/0x1010
   __handle_mm_fault+0x980/0x1120
   handle_mm_fault+0x17f/0x610
   __do_page_fault+0x25d/0x550
   do_page_fault+0x38/0x290
   do_async_page_fault+0x5b/0xe0
   async_page_fault+0x1e/0x30

Let us restore rcu_read_lock().

https://jira.sw.ru/browse/PSBM-120802
Fix in vz7: 152239c6c3b2 ("mm/tcache: fix rcu_read_lock()/rcu_read_unlock()
imbalance")

Signed-off-by: Evgenii Shatokhin <eshatokhin@virtuozzo.com>
Reviewed-by: Andrey Ryabinin <aryabinin@virtuozzo.com>

vz9 rebase notes:
 * free_unref_page() new arg (page order) has been added - assumed it's
   always 0

(cherry picked from vz8 commit e0868a90331d9ab990f3d4ca802d068fecaa9457)
Signed-off-by: Konstantin Khorenko <khorenko@virtuozzo.com>
Feature: mm: transcendent file cache (tcache)

---
## [MST-Robotics/MATE_2022](https://github.com/MST-Robotics/MATE_2022)@[a3ad01a594...](https://github.com/MST-Robotics/MATE_2022/commit/a3ad01a5941fa061b3f5d92c0fa27710ac269132)
#### Thursday 2022-01-20 01:54:10 by ClayJay3

Gosh dang, I tried my best with this one. Horizontal and vertical line following kinda sucks.

---
## [apache/couchdb](https://github.com/apache/couchdb)@[7163642787...](https://github.com/apache/couchdb/commit/7163642787f6fc791f612b9cdc32677c56174c34)
#### Thursday 2022-01-20 02:45:47 by Adam Kocoloski

Refactor build to dynamically generate test stages

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

---
## [ASXXXDOPEY22/Personal-Vault](https://github.com/ASXXXDOPEY22/Personal-Vault)@[ac92b185b0...](https://github.com/ASXXXDOPEY22/Personal-Vault/commit/ac92b185b061d49f93069bfdf776890346d028d8)
#### Thursday 2022-01-20 03:03:02 by David

Set up CI with Azure Pipelines

Fuck You [skip ci]

---
## [kleinerm/Psychtoolbox-3](https://github.com/kleinerm/Psychtoolbox-3)@[6b4b85a62b...](https://github.com/kleinerm/Psychtoolbox-3/commit/6b4b85a62bb2492ff73d263cab3b969b832439a7)
#### Thursday 2022-01-20 03:41:13 by kleinerm

Merge pull request #752 from Psychtoolbox-3/master

Psychtoolbox BETA update 3.0.18.4 "Ode to the slacktivists" SP4.

This release is all about low-level sound driver improvements.

## General

- PsychPortAudio robustness improvements for some exotic sound hardware that provides/requires/uses variable buffersize audio hostbuffers, instead of the more common fixed size audio hostbuffers. Should help on Windows, macOS and Linux in such cases to avoid audio artifacts during recording or playback under such conditions. Code inspection showed that such artifacts were theoretically possible, although no such artifacts are known to us to have happened in practice, neither reported from users, nor experienced in my own testing, so maybe this issue was non-existent on typically used mainstream hardware in practice. Anyway, the theoretical possibility is now fixed.

- PsychPortAudio: No longer enforce a 96000 Hz sampling rate in agressive low latency mode if no sampling frequency was specified by user code. Misc other small audio setup improvements.

## Linux

- PsychPortAudio robustness improvements in half-duplex audio capture mode for some exotic sound hardware. Fixes a theoretical issue, not one actually reported by users or experienced by myself. But better safe than sorry.

- Prep-work for use of a new upcoming Pulseaudio sound server backend on Linux, and changed default device selection priorities. If a Portaudio library with Pulseaudio sound server support would be installed on the Linux machine, then that server could be used now by PsychPortAudio by passing in an explicit deviceNumber for a Pulseaudio backed sound device. For auto device selection, `InitializePsychSound([reallyneedlowlatency=0]) is now prepared to allow to prefer Pulseaudio devices for `reallyneedlowlatency==0` - or for omission of the parameter - over Jack pro-audio server provided devices, and over ALSA devices. In `reallyneedlowlatency==1` setting, the preference order is Jack, then Pulseaudio, then ALSA. Actual preference order also depends on the requested `latencyclass` in each individual ``PsychPortaudio('Open')`` call: Audio device sharing with other audio clients by default can only happen for `latencyclass` 0 and 1, not for class 2 or higher. This to align Linux audio behavior more strongly with macOS behavior and some Windows behavior and make it easier to share audio devices with other applications, system sounds, `Snd`, `Beeper`, `sound`, `soundsc` or our movie playback functions, at least for cases where reasonably low latency and good timing precision and audio control is enough, as opposed to minimum latency + maximum precision and control. However, this new `InitializePsychSound` behavior is currently disabled, until a suitable Portaudio library with Pulseaudio support has been officially released and extensively  tested by us. Tests against the current prototype are highly promising though and this driver is compatible with the prototype if somebody feels manually installing the prototype to relly live life on the bleeding edge. `InitializePsychSound.m` has a `return` statement that one needs to comment out for this to work.
The new Portaudio library is unlikely to debut in the next Ubuntu 22.04-LTS release though, given approaching deadlines, but for the unlikely case it would make it before deadlines, we want to be prepared.

---
## [xzh3r/xzh3r-utau](https://github.com/xzh3r/xzh3r-utau)@[d5bbc114e9...](https://github.com/xzh3r/xzh3r-utau/commit/d5bbc114e9921b6d30911dc8475e67f410d21c37)
#### Thursday 2022-01-20 03:49:10 by xzh3r

oh boy (click commit name to read desc)

added whitty scale, my version of course. its a bit glitchy
added bomberman scale (siivagunner). it cant do long notes
added gangsta mario scale, it doesnt sound that great
added garcello scale, also sounds kinda weird. i think theres already one out there though.
added dead garcello scale. i think theres already one out there though.
added kia scale. sounds kinda weird
added pumpkin pie scale. sounds kinda weird
added and improved daddy dearest scale. sounds bad on first 3 notes.
and the eddsworld gang, using blantados' voicebanks and TIPS resampler

---
## [LeafyLuigi/discord-themes](https://github.com/LeafyLuigi/discord-themes)@[863d4028aa...](https://github.com/LeafyLuigi/discord-themes/commit/863d4028aaa8d968f0335e3780ecc078bf00e4be)
#### Thursday 2022-01-20 05:39:38 by LeafyLuigi

modals and threads finally done i hate myself

what's new? modals and threads are (re)themed. modals have a new look to them too.
i also cleaned the code up a bit. there should be less legacy shite.
bd's minimal mode needs to be fixed tho

---
## [ethanwong16/texera](https://github.com/ethanwong16/texera)@[c3af4463f4...](https://github.com/ethanwong16/texera/commit/c3af4463f486c9cf001cb547b29b6189a3c8302f)
#### Thursday 2022-01-20 06:01:47 by Albert Liu

Add PresetService (User Presets Step 3) (#1164)

Final feature demo:

![Kapture 2022-01-13 at 23 36 00](https://user-images.githubusercontent.com/12578068/149469927-b62bfa43-4701-4498-a489-565aea36da2c.gif)

---------------------------

This PR is extracted from #1041 as step 2 of the User Preset feature.

rebase of picked commits pertaining to PresetServiceService onto Albert-UserDictionaryService

PresetService provides the ability to save and "apply" collections of settings (represented by objects) that a user might find convenient to save and apply as a group. These groups are called Presets.

PresetService uses DictionaryService to store presets (it creates kind of a *view* in the database sense, of the user dictionary, that only includes Presets)

Changes from last review (for Yicong)
 - Code comments
 - fixed subscription memory leak by using takeUntil(observable), where said observable completes on NgOndestroy
 - DictionaryService now attempts to init whenever client logs in (sorry, you'll have to re-review my changes to DictionaryService)
 - PresetService now has public ready promise/value member 
   - This indicates that its init isn't complete until DictionaryService's init is complete (which is async, and cant be awaited in the constructor)
 - DeletePreset now built into PresetService (don't know why I ever didn't have that)
 - Revert Changes to Styles.scss to fix Karma test runner interface (I originally changed them as a workaround for an ng-zorro component that's no longer used)

 Note: for this step, I had less time and more complex code to test. I'm not sure I caught all the bugs, but it passes unit tests.
The quality of the code in this pr is lesser, in my opinion, so You'll have to be a little more careful on my behalf.



Co-authored-by: Zuozhi Wang <zuozhiw@gmail.com>
Co-authored-by: Yicong Huang <17627829+Yicong-Huang@users.noreply.github.com>

---
## [cyberitsolutions/bootstrap2020](https://github.com/cyberitsolutions/bootstrap2020)@[7c4b2c932d...](https://github.com/cyberitsolutions/bootstrap2020/commit/7c4b2c932dd78ad903f9e2f7b30770e01add1c14)
#### Thursday 2022-01-20 06:56:17 by Trent W. Buck

inkscape doc: remove unusable 0.91 extension hooks

16:23 <twb> 16:22 <twb> So now that the help URLs are implemented in C++ instead of python "extensions", I can't see how to change the URLs from https://X to file:///Y without recompiling the entire inkscape package
16:24 <twb> https://sources.debian.org/src/inkscape/1.1.1-2%7Ebpo11+1/src/verbs.cpp/#L2051-L2101
16:27 <twb> I put "echo "$@" >/tmp/delete-me" at the top of /usr/bin/xdg-open, and Inkscape > Help > Manual does not cause /tmp/delete-me to exist
16:27 <twb> So can't hook it there
16:29 <twb> ron: I want you to say "yes, I accept this regression".  Inkscape's documentation is all online.  To keep [REDACTED] happy, we hacked it so Inkscape's Help menu would open local copies we downloaded.  I can still download, but I cannot hack the menu anymore.
16:29 <twb> ron: so if $site wants inkscape help to work in Debian 11, they will need to have internet, and whitelist stuff in squid access rules
16:30 <twb> The only "show stopper" one I think is really annoying is: https://inkscape.org/doc/keys-1.1.x.html
16:30 <ron> ah, I'm fine with whitelisting the inkscape doc
16:30 <twb> OK cool
16:30 <ron> implying they must have net access
16:30 <ron> [REDACTED] misses out
16:30 <ron> boo hoo
16:31 <twb> The other compromise thing I could do is make a start menu item "Inkscape Documentation" that just opens chromium.
16:31 <twb> That's not hard
16:31 <mike> twb: Did you try exo-open instead of xdg-open? That's the other one I see pop up every now and then
16:32 <twb> AFAIK xdg-open is what runs exo-open
16:32 <twb> I was doing a quick-and-dirty test on my gnome environment so I didn't test that
16:33 <mike> xdg does call exo, but doesn't mean things can't call it directly
16:34 <twb> fair
16:34 <mike> It definitely honours XFCE's "preferred applications" setting. Inkscape opened Chrome, then I changed it from Chrome to Chromium and Inkscape opened Chromium
16:34 <twb> I don't *really* want to intercept every call to xdg-open/exo-open anyway
16:37 <mike> twb: Got this by stracing it: [pid 174670] execve("/bin/sh", ["/bin/sh", "-e", "-u", "-c", "export GIO_LAUNCHED_DESKTOP_FILE_PID=$$; exec \"$@\"", "sh", "exo-open", "--launch", "WebBrowser", "http://tavmjong.free.fr/INKSCAPE/MANUAL/html/index.php"], 0x5596c8443910 /* 54 vars */ <unfinished ...>
16:37 <mike> Which then called this: [pid 174670] execve("/usr/bin/exo-open", ["exo-open", "--launch", "WebBrowser", "http://tavmjong.free.fr/INKSCAPE/MANUAL/html/index.php"], 0x564af10ac068 /* 55 vars */) = 0
16:37 <twb> mike: ah thanks
16:37 <twb> So OK we can fix this
16:37 <mike> Not worth digging any deeper into that path
16:38 <mike> We could wrap exo-open, yeah
16:38 <mike> Not sure I like it, but it's viable

---
## [martinlarsalbert/Master-Thesis](https://github.com/martinlarsalbert/Master-Thesis)@[8f294c04ce...](https://github.com/martinlarsalbert/Master-Thesis/commit/8f294c04ceffe37a0f427ed5792ddcafbc7b64c4)
#### Thursday 2022-01-20 07:35:29 by Martin Alexandersson

Added some examples with numpy arrays.
I'm struggling with this problem myself and I've been trying to find the time to dig into this problem a bit, so many thanks that you asked this question, as it is also very relevant for med.

I did not fully understand the things that I now found in this example notebook, when I implemented my KalmanFilter. I've been thinking about rewriting it some day using only 1D arrays for the vectors. (Now I've used 2D column vectors).
(And it is a little bit of a pain to deal with, I can tell you).

Also feel free to play around with theses example and improve this notebook, that would be helpful for me as well.

---
## [v4lkyr/whyred](https://github.com/v4lkyr/whyred)@[d305085cc5...](https://github.com/v4lkyr/whyred/commit/d305085cc59843c03a0fcb965ffb4595875f7bd1)
#### Thursday 2022-01-20 09:54:06 by Peter Zijlstra

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
Signed-off-by: v4lkyr <valkyr23@gmail.com>

---
## [SuperSupermario24/gmod-particlemaker](https://github.com/SuperSupermario24/gmod-particlemaker)@[252b62a71f...](https://github.com/SuperSupermario24/gmod-particlemaker/commit/252b62a71f4145a09a241a07e8aff56cbfd1541e)
#### Thursday 2022-01-20 10:23:57 by SSM24

oh my god it was this fucking simple i'm going to lose my shit

aka fixed presets not working

---
## [pnjongang/iOS](https://github.com/pnjongang/iOS)@[37c18f59d0...](https://github.com/pnjongang/iOS/commit/37c18f59d0b761be6f6ff88ec18b56cbf10cbbe2)
#### Thursday 2022-01-20 11:44:01 by Zac West

Onboarding visual/flow updates; require permission prompting (#1878)

Fixes #380. Fixes #1794. Fixes #350. Fixes #722.

## Summary
- Pulls all of the onboarding steps out of segue-based storyboards and into code.
- Merges authentication with scanning/manual, reducing steps in auth.
- Removes the "checklist" final screen.
- Supports going 'back' through onboarding steps, e.g. an error after entering a URL.
- Moves permissions from an opt-in "which would you like?" to a required "you must accept/decline this permission" for each permission. See notes below for why.
- Removes the team migration warning from last year.
- Adds landscape & dynamic type support to onboarding. I didn't bother to make the DT do live-updating though.
- Fills in internal & external URL, sets active SSID if possible after location permission.
- Connects to internal URL from discovery instead of base (external) URL.
- Allows onboarding to a server which requests, but does not require, client certificates.
- Allows starting Onboarding skipping the Welcome screen, connects this to the 'add server' row in app configuration when in debug mode.
- Stops calling api/discovery_info for testing connectivity.
- Handles Bonjour updates and removals in the scanning screen.

## Any other notes
Apple is actively blocking 2021.10 (only on iOS) because of an unwritten part of [rule 5.1.1](https://developer.apple.com/app-store/review/guidelines/#5.1.1), saying:

> **Guideline 5.1.1 - Legal - Privacy - Data Collection and Storage**
> 
> We noticed your app encourages or directs users to allow the app to access the location. Specifically, your app directs the user to grant permission in the following way(s):
>
> - A message appears before the permission request, and the user can close the message and delay the permission request with the "Continue" button. The user should always proceed to the permission request after the message.
> 
> Permission requests give users control of their personal information. It is important to respect their decision about how their data is used.

This is of course referring to our screen which looks like this:

<img width="200" src="https://user-images.githubusercontent.com/74188/136716566-349558d4-d343-4ede-acd6-83b4e66742bc.png">

I love that they're cherry-picking the location part of this when we allow users to do a number of things on this screen. I believe the part of 5.1.1 that they are alluding to here is:

> (iv) Access: Apps must respect the user’s permission settings and not attempt to manipulate, trick, or force people to consent to unnecessary data access. For example, apps that include the ability to post photos to a social network must not also require microphone access before allowing the user to upload photos. Where possible, provide alternative solutions for users who don’t grant consent. For example, if a user declines to share Location, offer the ability to manually enter an address.

They do link to the Human Interface Guidelines' [Accessing User Data](https://developer.apple.com/design/human-interface-guidelines/ios/app-architecture/accessing-user-data/) whose section "Displaying Custom Messaging Before the Alert" says:

> **Make it clear that opening the system alert is the only action people can take in your custom-messaging screen.** People can interpret a pre-alert message as a delaying tactic, so it’s critical to let them quickly dismiss the message and view the system alert. If you display a custom screen that precedes a privacy-related permission request, it must offer only one action, which must display the system alert. Use a word like "Continue" to title the action; don’t use "Allow" or other terms that might make people think they’re granting their permission or performing other actions within your custom screen.

I do not believe that we're showing a pre-alert message since we're showing numerous options and allowing the user to pick and choose. Oh well. This new onboarding has improvements in other ways, and maybe is _more_ clear about permissions and what they do, so lemons into lemonade I guess.

---
## [Bartimeux/workspace](https://github.com/Bartimeux/workspace)@[f29d6627db...](https://github.com/Bartimeux/workspace/commit/f29d6627dbabd59c71ac9ce9cac6d24c51c37262)
#### Thursday 2022-01-20 14:39:17 by Loïc Chanel

Ruby script to pull users and add them to a topology file (mapping users to their group)

Script mapping LDAP users to their group for Knox complete

Script mapping LDAP users to their group for Knox complete, and debuged

Script mapping LDAP users to their group for Knox complete, and debuged, with explicit vars name

Some MapRed examples. README to come

Now with an explicit README

Commiting the sing package script

Script done. To be tested

Working on a safebox storage that will be emptied if I don't answer to an automatic e-mail within 30 days

A little confidentiality would be god, isn't it ?

Debug over re-signing script

Now with an improved Gem, and handling real shit

Work in progress. Maybe we should skip validation if the user's main account sent message yesterday

Now with a check that any email have been sent yesterday nor today before lauching the countdown

Removing useless line

Now with the other script. To be added : Crontabs, and mails to say Goodbye

Now with cron file. Once the mails will be fully written, the service will be ready

Minor modification

Fix: basic cleanup

---
## [DaddyIssues98/KirieStation](https://github.com/DaddyIssues98/KirieStation)@[49bbd525a8...](https://github.com/DaddyIssues98/KirieStation/commit/49bbd525a8e1cdad3908588be495140d19e0a1b8)
#### Thursday 2022-01-20 14:41:02 by DaddyIssues98

a

What the fuck did you just fucking say about me, you little bitch? I’ll have you know I graduated top of my class in the Navy Seals, and I’ve been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills.
I am trained in guerilla warfare and I’m the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words.

You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You’re fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that’s just with my bare hands.

Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little “clever” comment was about to bring down upon you, maybe you would have held your fucking tongue.

Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little “clever” comment was about to bring down upon you, maybe you would have held your fucking tongue.

But you couldn’t, you didn’t, and now you’re paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it.

You’re fucking dead, kiddo.

---
## [talex5/dream](https://github.com/talex5/dream)@[73adda5ba3...](https://github.com/talex5/dream/commit/73adda5ba3b7f8ee3722d81439c0a1c083e3fe66)
#### Thursday 2022-01-20 16:44:09 by Thomas Leonard

Initial port to Eio

This is a proof-of-concept port of Dream to Eio. Most of the public API
in dream.mli has been changed to no longer use promises and the main
tutorial examples (`[1-9a-l]-*`) have been updated and are working.
The documentation mostly hasn't been updated.

Internally, it's still using Lwt in many places, using Lwt_eio to
convert between them.

The main changes are:

- User code doesn't need to use lwt (or lwt_ppx) now for Dream stuff.
  However, the SQL example still uses lwt for the Caqti callback.

- Dream servers must be wrapped in an `Eio_main.run`.
  Unlike Lwt, where you can somewhat get away with running other
  services with `Lwt.async` before `Dream.run` and relying on the
  mainloop picking them up later, everything in Eio must be started
  from inside the loop. Personally, I think this is clearer and less
  magical, making it obvious that Dream can run alongside other Eio
  code, but obviously Dream had previously made the choice to hide
  the `Lwt_main.run` by default.

- `Dream.run` now takes an `env` argument (from `Eio_main.run`),
  granting it access to the environment. At present, it uses this
  just to start `Lwt_eio`, but once fully converted it should also
  use it to listen on the network and read certificates, etc.

- `Dream.request` now takes a switch to represent the lifetime of the
  request. This is needed because when you stream a reply the handler
  returns immediately, but the streaming fibre continues running
  afterwards to write the body.

Error handling isn't quite right yet. Ideally, we'd create a new Eio
switch for each new connection, and that would get the errors. However,
connection creation is currently handled by Lwt. Also, it still tries to
attach the request ID to the Lwt thread for logging, which likely won't
work. I should provide a way to add log tags to fibres in Eio.

Note: `example/k-websocket` logs `Async exception: (Failure "cannot write to closed
writer")`. It does that on `master` with Lwt too.

---
## [Wallemations/heavenstation](https://github.com/Wallemations/heavenstation)@[7bead07444...](https://github.com/Wallemations/heavenstation/commit/7bead0744491b9beb91689d34ac12d142aca5b31)
#### Thursday 2022-01-20 16:49:20 by John Willard

General pAI code improvements (#63688)

Fikou said they would've made MODsuits be controllable by pAI's rather than AI's, if pAI code wasn't as bad.

But pAI code ISN'T AS BAD AS AI CODE LIKE HOLY SHIT WHAT THE FUCK MAN???

Anyways, this is just general code improvements for pAIs that I thought would be nice to have.

Documents previously undocumented vars
Moves loose vars to be where they should be
Removes single-letter variables
Makes pAI a defined job
Moves vars around to where they should be while removing unused ones.
Makes pAI abilities its own .dm file
Replaces var/silent with Stun() (like cyborgs)
Reworks pAI's doorjack to not have a ton of procs, copy paste, and a reliance on Life(), instead it just uses a do_after()
Moves screwdrivering radios from attackby to screwdriver_act

Just general code improvement for Silicon, the thing no one likes or wants to touch.

---
## [NightmareChamillian/goonstation](https://github.com/NightmareChamillian/goonstation)@[213b1fb1c9...](https://github.com/NightmareChamillian/goonstation/commit/213b1fb1c936cb95eace5cc4faac16cddc174eac)
#### Thursday 2022-01-20 16:49:40 by Nexusuxen

AI Skins (#7129)

* wip
skins added
support for different skins added
- battmode & apcmode overlays
- readjust stun/bsod icon states to use overlays
setSkin proc also includes input validation to ensure only valid icons
medal+reward "Now you're thinking with portals!" dwaine skin
FUCK NPC AI WHY DO THE MARTIANS AGGRO ON SPAWN ARGHGHH

* mostly final changes
adds clown skin
further refactors to ai core frame layering
ai core sprites are now separate from the screen
blank screen now used for when the ai is depowered
(cant remember all the details, its been a while)

* tweaks
some desc adjusts
undid weird indentation(s)
removed unnecessary/outdated comments
1 -> TRUE
adds clown ai kit to geoff honkington's stock
(honk)

---
## [talex5/dream](https://github.com/talex5/dream)@[b88142a951...](https://github.com/talex5/dream/commit/b88142a951b14393e7a7e43610f7a3218b34a91e)
#### Thursday 2022-01-20 16:50:33 by Thomas Leonard

Initial port to Eio

This is a proof-of-concept port of Dream to Eio. Most of the public API
in dream.mli has been changed to no longer use promises and the main
tutorial examples (`[1-9a-l]-*`) have been updated and are working.
The documentation mostly hasn't been updated.

Internally, it's still using Lwt in many places, using Lwt_eio to
convert between them.

The main changes are:

- User code doesn't need to use lwt (or lwt_ppx) now for Dream stuff.
  However, the SQL example still uses lwt for the Caqti callback.

- Dream servers must be wrapped in an `Eio_main.run`.
  Unlike Lwt, where you can somewhat get away with running other
  services with `Lwt.async` before `Dream.run` and relying on the
  mainloop picking them up later, everything in Eio must be started
  from inside the loop. Personally, I think this is clearer and less
  magical, making it obvious that Dream can run alongside other Eio
  code, but obviously Dream had previously made the choice to hide
  the `Lwt_main.run` by default.

- `Dream.run` now takes an `env` argument (from `Eio_main.run`),
  granting it access to the environment. At present, it uses this
  just to start `Lwt_eio`, but once fully converted it should also
  use it to listen on the network and read certificates, etc.

Error handling isn't quite right yet. Ideally, we'd create a new Eio
switch for each new connection, and that would get the errors. However,
connection creation is currently handled by Lwt. Also, it still tries to
attach the request ID to the Lwt thread for logging, which likely won't
work. I should provide a way to add log tags to fibres in Eio.

Note: `example/k-websocket` logs `Async exception: (Failure "cannot write to closed
writer")`. It does that on `master` with Lwt too.

---
## [morektz/SolanaLearningMindMaps](https://github.com/morektz/SolanaLearningMindMaps)@[75ee68e191...](https://github.com/morektz/SolanaLearningMindMaps/commit/75ee68e1912fa5ebe4137297d379ecb58f2b21af)
#### Thursday 2022-01-20 16:58:09 by mo rektz

fucking stupid mistake with a fucking hyphen , waiting fcking hours and hours , fucking shit

---
## [LarsVDN/papi-gelato](https://github.com/LarsVDN/papi-gelato)@[4383d0df4c...](https://github.com/LarsVDN/papi-gelato/commit/4383d0df4c8617d1c5588dbe403e52c891aa6e38)
#### Thursday 2022-01-20 17:21:24 by LarsVDN

F1.5.02.O2 - Een programma opleveren
it fucking works holy shit

---
## [jvdlem/PGD-GAMEJAM-2](https://github.com/jvdlem/PGD-GAMEJAM-2)@[8cb099aa19...](https://github.com/jvdlem/PGD-GAMEJAM-2/commit/8cb099aa19bce32be81dbcd72d30078efcbd5730)
#### Thursday 2022-01-20 17:56:23 by Terdirk12

2nd big fix lets goo

-fixed elevator not opening in a build
-made coins go to the player faster (why were they so gosh darn slow)
-enemies now come at you from across the room (no more cheaky sniping)
-fixed some nullreferences in the pistol
-currently the roof of the cave system is gone but that be cuz some rooms need to be fixed (jordi knows which ones)
-added some light in the boss room so that you can actually see which eye is opened
-made the scope material less metallic for a more clear picture
-scaled back a previous fix for button presses from 10 units to 2 units
-made the builds development builds for now just so we can see where what goes wrong.
-dm me "i have read ur long ass shit" if you have actually read my long ass shit. -Dirk :D

---
## [cockroachdb/cockroach](https://github.com/cockroachdb/cockroach)@[c90acf7ea7...](https://github.com/cockroachdb/cockroach/commit/c90acf7ea736d2d2b95599bc41bad0765a0b10fa)
#### Thursday 2022-01-20 18:19:55 by craig[bot]

Merge #73883 #74823 #75169 #75212

73883: tracing: pool and reuse spans r=andreimatei a=andreimatei

This patch adds sync.Pool-ing and reuse to tracing spans, so that they
don't need to be dynamically allocated on every span creation. This has
a big effect on the heap footprint.

Conceptually, a span is made available for reuse on Finish(). In
practice, it's more complicated because there can still be references of
the span used concurrently with Finish(), either internally in the
tracing library or externally. The external ones are bugs by definition,
but we want to avoid some particularly nasty consequences of such bugs.

The BenchmarkTracing results below show that this saves around 10KB
worth of heap allocations per simple query, when tracing is enabled
(minimal tracing: TracingModeActiveSpansRegistry). I believe the span
allocations go from being serviced from the shared heap to being
serviced from CPU-local freelists, since they become small enough. In
the single-node case, this is 25% of the query's allocations. As can be
seen in the benchmarks below in the differences between the trace=on and
trace=off rows, the impact of tracing is big on memory footprint; with
this patch, there's not much impact.

```
name                               old alloc/op   new alloc/op   delta
Tracing/1node/scan/trace=off-32      19.7kB ± 1%    19.7kB ± 1%     ~     (p=0.768 n=10+5)
Tracing/1node/scan/trace=on-32       29.2kB ± 0%    22.0kB ± 0%  -24.85%  (p=0.001 n=10+5)
Tracing/1node/insert/trace=off-32    38.5kB ± 1%    38.4kB ± 1%     ~     (p=0.440 n=10+5)
Tracing/1node/insert/trace=on-32     45.5kB ± 1%    38.7kB ± 1%  -15.03%  (p=0.001 n=10+5)
Tracing/3node/scan/trace=off-32      68.1kB ± 3%    67.9kB ± 3%     ~     (p=0.768 n=10+5)
Tracing/3node/scan/trace=on-32       86.8kB ± 2%    75.3kB ± 2%  -13.21%  (p=0.001 n=9+5)
Tracing/3node/insert/trace=off-32    88.1kB ± 5%    90.8kB ± 7%     ~     (p=0.112 n=9+5)
Tracing/3node/insert/trace=on-32     96.1kB ± 3%    89.0kB ± 2%   -7.39%  (p=0.001 n=9+5)
```

Unfortunately, pooling spans only saves on the size of allocations, not
the number of allocations. This is because the Context in which a Span
lives still needs to be allocated dynamically, as it does not have a
clear lifetime and so it cannot be re-used (plus it's immutable, etc).
Before this patch, the code was optimized to allocate a Span and a
Context together, through trickery (we had a dedicated Context type,
which we now get rid of). So, this patch replaces an allocation for
Span+Context with just a Context allocation, which is a win because
Spans are big and Contexts are small.

BenchmarkTracing (which runs SQL queries) only show minor improvements
in the time/op, but the memory improvements are so large that I think
they must translate into sufficient GC pressure wins to be worth doing.
Micro-benchmarks from the tracing package show major time/op wins.

```
name                                           old time/op    new time/op    delta
Tracer_StartSpanCtx/opts=none-32                  537ns ± 1%     275ns ± 2%  -48.73%  (p=0.008 n=5+5)
Tracer_StartSpanCtx/opts=real-32                  537ns ± 2%     273ns ± 2%  -49.16%  (p=0.008 n=5+5)
Tracer_StartSpanCtx/opts=real,logtag-32           565ns ± 1%     278ns ± 1%  -50.81%  (p=0.008 n=5+5)
Tracer_StartSpanCtx/opts=real,autoparent-32       879ns ±29%     278ns ± 5%  -68.36%  (p=0.008 n=5+5)
Tracer_StartSpanCtx/opts=real,manualparent-32     906ns ±26%     289ns ± 2%  -68.08%  (p=0.008 n=5+5)
Span_GetRecording/root-only-32                   11.1ns ± 2%    11.6ns ± 4%     ~     (p=0.056 n=5+5)
Span_GetRecording/child-only-32                  11.1ns ± 4%    11.7ns ± 2%   +5.44%  (p=0.016 n=5+5)
Span_GetRecording/root-child-32                  18.9ns ± 3%    19.5ns ± 1%   +3.55%  (p=0.008 n=5+5)
RecordingWithStructuredEvent-32                  1.37µs ± 2%    1.17µs ± 2%  -14.22%  (p=0.008 n=5+5)
SpanCreation/detached-child=false-32             1.84µs ± 2%    0.96µs ± 0%  -47.56%  (p=0.008 n=5+5)
SpanCreation/detached-child=true-32              2.01µs ± 1%    1.14µs ± 1%  -43.32%  (p=0.008 n=5+5)

name                                           old alloc/op   new alloc/op   delta
Tracer_StartSpanCtx/opts=none-32                   768B ± 0%       48B ± 0%  -93.75%  (p=0.008 n=5+5)
Tracer_StartSpanCtx/opts=real-32                   768B ± 0%       48B ± 0%  -93.75%  (p=0.008 n=5+5)
Tracer_StartSpanCtx/opts=real,logtag-32            768B ± 0%       48B ± 0%  -93.75%  (p=0.008 n=5+5)
Tracer_StartSpanCtx/opts=real,autoparent-32        768B ± 0%       48B ± 0%  -93.75%  (p=0.008 n=5+5)
Tracer_StartSpanCtx/opts=real,manualparent-32      768B ± 0%       48B ± 0%  -93.75%  (p=0.008 n=5+5)
Span_GetRecording/root-only-32                    0.00B          0.00B          ~     (all equal)
Span_GetRecording/child-only-32                   0.00B          0.00B          ~     (all equal)
Span_GetRecording/root-child-32                   0.00B          0.00B          ~     (all equal)
RecordingWithStructuredEvent-32                  1.54kB ± 0%    0.77kB ± 0%  -49.86%  (p=0.008 n=5+5)
SpanCreation/detached-child=false-32             4.62kB ± 0%    0.29kB ± 0%     ~     (p=0.079 n=4+5)
SpanCreation/detached-child=true-32              5.09kB ± 0%    0.77kB ± 0%  -84.87%  (p=0.008 n=5+5)
```

This patch brings us very close to enabling the
TracingModeActiveSpansRegistry tracing mode by default in production -
which would give us a registry of all in-flight spans/operations in the
system.

 ### Interactions with use-after-Finish detection

Span reuse interacts with the recently-introduced span-use-after-Finish
detection. Spans are made available for reuse on Finish (technically,
when certain references to the span have been drained; see below). When
a span is reused in between Finish() and an erroneous use of the
Finish()ed span, this bug cannot be detected and results in the caller
operating on an unintended span. This can result in the wrong log
message apearing in the wrong span, and such. Care has been taken so
that use-after-Finish bugs do not result in more structural problems,
such as loops in the parent-child relationships.

 ### Technical details

The mechanism used for making spans available for reuse is reference
counting; the release of a span to the pool is deferred to the release
of the last counted reference.
Counted references are held:
- internally: children hold references to the parent and the parent holds
  references to the children.
- externally: the WithParent(sp) option takes a reference on sp.

Apart from WithParent, clients using Spans do not track their references
because it'd be too burdensome to require all the references to have a
clearly defined life cycle, and to be explicitly released when they're
no longer in use. For clients, the contract is that a span can be used
until Finish(). WithParent is special, though; see below.

Different alternatives to reference counting were explored. In
particular, instead of a deferred-release scheme, an alternative was a
fat-pointer scheme where references that can outlive a span are tagged
with the span's "generation". That works for the internal use cases, but
the problem with this scheme is that WithParent(s) ends up allocating -
which I want to avoid. Right now, WithParent(s) returns a pointer as an
interface, which doesn't allocate.  But if the pointer gets fat, it no
longer fits into the class of things that can be put in interfaces
without allocating.

The reference counter is an atomic; it is not protected by the span's
lock because a parent's counter needs to be accessed under both the
parent's lock and the children's locks.

In details, the reference counter serves a couple of purposes:
1) Prevent re-allocation of a Span while child spans are still operating on
it. In particular, this ensures that races between Finish()ing a parent and
a child cannot result in the child operating on a re-allocated parent.
Because of the span's lock ordering convention, a child cannot hold its
lock while operating on the parent. During Finish(), the child drops its
lock and informs the parent that it is Finish()ing. If the parent
Finish()es at the same time, that call could erroneously conclude that the
parent can be made available for re-use, even through the child goroutine
has a pending call into the parent.

2) Prevent re-allocation of child spans while a Finish()ing parent is in
the process of transforming the children into roots and inserting them into
the active spans registry. Operating on the registry is done without
holding any span's lock, so a race with a child's Finish() could result in
the registry operating on a re-allocated span.

3) Prevent re-allocation of a Span in between the time that WithParent(s)
captures a reference to s and the time when the parent option is used to
create the child. Such an inopportune reuse of a span could only happen is
the span is Finish()ed concurrently with the creation of its child, which
is illegal. Still, we optionally tolerate use-after-Finishes, and this use
cannot be tolerated with the reference count protection. Without this
protection, the tree of spans in a trace could degenerate into a graph
through the introduction of loops. A loop could lead to deadlock due to the
fact that we lock multiple spans at once. The lock ordering convention is
that the parent needs to be locked before the child, which ensures
deadlock-freedom in the absence of loops.
For example:
1. parent := tr.StartSpan()
2. parentOpt := WithParent(parent)
3. parent.Finish()
4. child := tr.StartSpan(parentOpt)
If "parent" would be re-allocated as "child", then child would have itself
as a parent. The use of parentOpt in step 4) after parent was finished in
step 3) is a use-after-Finish of parent; it is illegal and, if detection is
enabled, it might be detected as such. However, if span pooling and re-use
is enabled, then the detection is not realiable (it does not catch cases
where a span is re-used before a reference to it taken before the prior
Finish() is used).
A span having itself as a parent is just the trivial case of the problem;
loops of arbitrary length are also possible. For example, for a loop of
length 2:
1. Say we have span A as a parent with span B as a child (A -> B).
2. parentA := WithParent(A)
3. parentB := WithParent(B)
4. A.Finish(); B.Finish();
5. X := tr.StartSpan(parentA); Y := tr.StartSpan(parentB);
If B is re-used as X, and A is re-used as Y, we get the following graph:
```
 B<-┐
 |  |
 └->A
```

We avoid these hazards by having WithParent(s) increment s' reference
count, so spans are not re-used while the creation of a child is pending.
Spans can be Finish()ed while the creation of the child is pending, in
which case the creation of the child will reliably detect the
use-after-Finish (and turn it into a no-op if configured to tolerate
such illegal uses).

Introducing this reference count, and only reusing spans with a
reference count of zero, introduced the risk of leaking references if
one does opt = WithParent(sp) and then discards the resulting opt
without passing it to StartSpan(). This would cause a silent performance
regression (not a memory leak though, as the GC is still there). This
risk seems worth it for avoiding deadlocks in case of other buggy usage.

Release note: None

74823: sql: add create_session_revival_token builtin r=catj-cockroach,knz,otan a=rafiss

refs https://github.com/cockroachdb/cockroach/issues/74643

This builtin function will be used by sqlproxy in order to migrate
sessions from one sql node to another. The token will be used to
authenticate as the current user without using a password.

The builtin is only usable by tenants.

No release note since this is only meant to be used internally.

Release note: None

75169: vendor: pull in latest version of `stress` r=rail a=rickystewart

Pull in the latest version of `stress` including these changes:

```
43d99a9 Merge pull request #13 from cockroachdb/bazelsharding
01690a1 stress: add `-bazel` support, support for sharding artifacts
```

Release note: None

75212: kvserver: de-flake TestReplicateQueueUpAndDownReplicateNonVoters r=irfansharif a=irfansharif

Fixes #75135. This test asserted on span configs applying to a scratch
range. When stressing, it appeared that some time we were not seeing the
scratch range adopt the prescribed number of voters/non-voters. Staring
at the test itself, we were only nudging the replication queues for the
first node in the three node test. It's possible for the scratch range
to have been housed on a node other than the first; this commit makes it
so that the test nudges queues on all nodes. For good measure, lets also
ensure that the split queues process everything, ditto for the snapshot
queues.

To repro:

    dev test pkg/kv/kvserver \
      -f TestReplicateQueueUpAndDownReplicateNonVoters \
      -v --show-logs --timeout 2m --stress

Release note: None

Co-authored-by: Andrei Matei <andrei@cockroachlabs.com>
Co-authored-by: Rafi Shamim <rafi@cockroachlabs.com>
Co-authored-by: Ricky Stewart <ricky@cockroachlabs.com>
Co-authored-by: irfan sharif <irfanmahmoudsharif@gmail.com>

---
## [edx/edx-analytics-data-api](https://github.com/edx/edx-analytics-data-api)@[1e9ede6bd2...](https://github.com/edx/edx-analytics-data-api/commit/1e9ede6bd2b76ac5f0f2edf718618bdf917e3995)
#### Thursday 2022-01-20 19:12:23 by Andy Shultz

fix: move most sorting from MySQL to python

in theory it makes sense to sort in the DB. In practice it means we
sort whether we need to or not and we add invisible work to queries
because the sort is not at the point of querying

in practical effect our DB is often taking this sort out to a
materialized table on disk, which is super slow, and then we'll have
it all in memory in django anyway

so drop ordering from the object models, add it to the views where
needed to support groupbys

location is left alone because it is not causing trouble today and its
sorting and grouping is slightly wonky and could use a complete
rebuild

MST-1305

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[ed355a200b...](https://github.com/mrakgr/The-Spiral-Language/commit/ed355a200b1bd064584b5d109d5d7fd0f34b6c3f)
#### Thursday 2022-01-20 19:21:47 by Marko Grdinić

"11:45am. Let me start. I had a while to chill.

First I need to figure out IO.

11:50am. It seems that to make the DOP IO node work, I need to manually use the save to disk. Still how does that take effect? I need to revisit that part of the lecture. I should not have ignored it. For some reasoned I tuned out at that part, but I should not have.

https://youtu.be/NHmAcO6Dob4?list=PLhyeWJ40aDkUDHDOhZQ2UkCfNiQj7hS5W&t=833

Here it is. Let me pay attention this time.

12pm. I am confused. Why is it trying to load the 0th frame and giving me an error?

> There is an error when I connect 'trail' node, I guess it's because Houdini tries to load cache from frame 0 and not 1 which is strange. I found an option in this node called 'Evaluate within frame range' and it makes error dissappear. Do you think it's a good idea?

This fixes it. Good.

12:10pm. https://youtu.be/lxWp0EhaHdo?list=PLhyeWJ40aDkUDHDOhZQ2UkCfNiQj7hS5W&t=157

Here he will be adding the timeshift node.

12:30pm. I don't know. The flip_dopio node is not visualizing in the viewport. He says it should save in a big file, but it is only 1.4k for me for each frame. I do not think it is saving anything. Why is this happening?

Ah, I forgot to pick the right preset.

12:40pm. https://youtu.be/lxWp0EhaHdo?list=PLhyeWJ40aDkUDHDOhZQ2UkCfNiQj7hS5W&t=1010

No, it seems he does not use any presets. It seems that adding an empty thing just imports in everything. Now the problem I have is that it imports in the static objects in a visible manner. Was ball_flip the output node?

https://youtu.be/lxWp0EhaHdo?list=PLhyeWJ40aDkUDHDOhZQ2UkCfNiQj7hS5W&t=380

Oh, no it is the first object.

I am surprised that this works. I thought it would just result in a static thing, but I was wrong.

Let me try saving it now. Oh, it results in 13mb files. Yeah, this is a lot.

1:10pm. I got it all working. Great.

https://youtu.be/9eHh68tzI1I?list=PLhyeWJ40aDkUDHDOhZQ2UkCfNiQj7hS5W
Houdini Isn't Scary Project - Part 5: Rendering And Extras

This time I did it properly and internalized all the lessons. I should not have skipped the IO nodes. They are useful.

Now, I'll take a break here and deal with this last part after that. He says it is more of the same so it should not be too hard. After that is done, hopefully I can do some actual modeling in Houdini.

2pm. Let me finish the chapter I am reading and then I'll do the chores.

2:05pm. Let me start the chores.

2:30pm. Done with the chores. Phew.

2:35pm. Let me resume. Time for the last part of the series.

2:45pm. I made the mistake of lowering the particle separation value and it made the simulation extremely slower.

https://www.reddit.com/r/Houdini/comments/nx5mdv/does_mantra_use_the_gpu_for_rendering/
> Nope.

Amazing that Houdini does not use the GPU.

https://youtu.be/9eHh68tzI1I?list=PLhyeWJ40aDkUDHDOhZQ2UkCfNiQj7hS5W&t=392
> Mantra is a very slow renderer.

This was my hunch.

3pm. I wonder why Houdini does not have native GPU rendering. Karma has something called XPU, but I am not sure what to think about that.

3:25pm. https://youtu.be/9eHh68tzI1I?list=PLhyeWJ40aDkUDHDOhZQ2UkCfNiQj7hS5W&t=1251

The amount of stuff Houdini has is extreme.

3:35pm. Let me take a break here. I am finally done with the first series.

https://www.youtube.com/playlist?list=PLhyeWJ40aDkVmhEHlCKRvy10lNobG0KZT
VEX Isn't Scary: Beginner Series

This caught my interest. Based on the titles I think it might have something to do with proceduaral generation.

https://www.youtube.com/watch?v=VDOwi0w5X5U
How Many Of These Art Predictions Will I Get Wrong? (Looking Ahead 10 Years)

Let me watch this for a bit.

3:45pm. Ok, enough, enough. Instead of wasting my time listening to this, let me move on. I meant to go to the pdf tutorial on the soccer ball, but let me exhaust the VEX tutorial first. I want to focus on that.

Honestly, I can't be bothered to think too hard about all these simulations. What I want is modeling. The simulations themselves are similar to what I learned in Blender, even if I like Houdini's structure more. They have the same weakness of taking forever. I want to learn thing that I can get feedback on ASAP.

https://youtu.be/k4q1UQp4x6U?list=PLhyeWJ40aDkVmhEHlCKRvy10lNobG0KZT
VEX Isn't Scary - Part 1: Basics

Let me start with this.

https://youtu.be/k4q1UQp4x6U?list=PLhyeWJ40aDkVmhEHlCKRvy10lNobG0KZT&t=103

Ah, I see. So VEX's is Houdini's native language. I really wanted to do some modeling.

...Let me watch just the first 5-10m of this and then I'll decide whether I want to try the soccer ball instead. I really want to get down and dirty with points and edges, I do not want to waste my stuff on abstract stuff.

3:55pm. He notes Vex is similar to C#.

https://youtu.be/k4q1UQp4x6U?list=PLhyeWJ40aDkVmhEHlCKRvy10lNobG0KZT&t=357

Oh, whatever, let me go for this. I can leave the ball for tomorrow or the day after.

https://youtu.be/k4q1UQp4x6U?list=PLhyeWJ40aDkVmhEHlCKRvy10lNobG0KZT&t=754

Yeah, it is not bad to start here. I might as well learn this.

4:15pm. https://youtu.be/qXqmm_aSqEU?list=PLhyeWJ40aDkVmhEHlCKRvy10lNobG0KZT

This is pretty boring, but I have to persevere. Actually let me just skim it.

https://youtu.be/qXqmm_aSqEU?list=PLhyeWJ40aDkVmhEHlCKRvy10lNobG0KZT&t=873

It remarkable how long it is taking him just to do the basics of programming. This makes me thing - is programming really this complex for other people?

https://youtu.be/qXqmm_aSqEU?list=PLhyeWJ40aDkVmhEHlCKRvy10lNobG0KZT&t=988

This is awkward. Rather than this set, they should have just added a primitive for vectors. It is a pity they immitated C# instead of a functional language.

At any rate, I think I'll be able to go through this series quickly. I can skim it with no problem. Let me move on to the next thing.

5pm. https://youtu.be/9xhmDWAyPRA?list=PLhyeWJ40aDkVmhEHlCKRvy10lNobG0KZT&t=1085

This is nice. I am not paying too careful attention though. I am pretty bored with this.

https://youtu.be/XroQeoivv0o?list=PLhyeWJ40aDkVmhEHlCKRvy10lNobG0KZT&t=1050

Does it not have `break` statements?

5:20pm. https://youtu.be/M1hmxPE1ZT8?list=PLhyeWJ40aDkVmhEHlCKRvy10lNobG0KZT
VEX Isn't Scary Part 6 Clarification

Am I dying of boredom here? Yes, I am. I've seen enough for now. Let me work on that football.

https://www.sidefx.com/tutorials/

I see that there is a Houdini -> Blender workflow.

https://www.sidefx.com/tutorials/pop-up-live-stream-on-houdini-to-blender-workflow-clothing-v2-new-facial-expression-hda-mocap/
HOUDINI TO BLENDER WORKFLOW

> Transitioning from a coder to a 3D artist. Houdini was the best option for me after I explored a different number of 3D software applications. I love the procedural workflow in Houdini and how easily accessible the attributes of the geometry are available to the user. This makes it a lot easier to focus on creating a good render and less time wasted on trying to figure out how to access certain geometry points or edges.

I'll leave this for later. For now how about I track down that ball tutorial.

https://www.sidefx.com/tutorials/

Despite what has been said about Houdini's learning resources being sparse, it seems there is a ton here.

Sigh, where was that ball.

https://media.sidefx.com/uploads/tutorial/foundations/h19/hfoundations_02_model_render_animate.pdf

Found it in my journal.

https://www.sidefx.com/learn/collections/houdini-foundations/

I think it was supposed to be from here. Let me go through it. I really need to do something practical otherwise I am going to fall asleep here.

5:35pm. Oh, wow, it is literally possible to wiggle the node out of the network.

> The ray node is a tool that projects points out to another piece of geometry. This is similar to the pinboard toy you played with as a kid. In fact, this is the node you would use to set up a pinboard in Houdini.

This is the curve deform that I wanted in Blender.

> Go back to the Scene View tab, RMB-click on the Visualizer display button on the Display Options bar and click on the + Plus sign next to Scene and choose Marker. In the Edit Visualizer panel, set Name and Label to Patch_Numbers, set Type to Marker, Class to Primitive and Attribute to patches.

Where is that thing. This is why video tutorials are superior for learning 3d software. I googled it and I can open it just by pressing D.

6:10pm. Let me stop here for lunch.

7:25pm. Let me resume. I figured out where that visualizer button is. It is right in the middle column. It sure is hidden well near the bottom of it.

7:40pm. > Select the Render Region tool, then draw a box around the soccer ball in the viewport create a preview rendering. To cancel, click on the x button in the top right of the region.

Where the hell is it? Ah, on the far left side, just below the magnet.

> Note: Setting up UVs to match an existing texture is not the normal order of operations. In practice, the UVs are generated then passed on to a texture artist who builds the texture. We are taking the opposite approach so that you don’t need to paint a texture yourself.

7:50pm. What am I look at here. The UVs can't be right here.

> Click on the File Selector button next to Texture Map.

7:55pm. Ugh...the fatigue is really hitting me. I have no idea where Texture Map is supposed to be.

8pm. https://www.sidefx.com/docs/houdini/shade/textures.html

I am going to check this out tomorrow. Let me just install the project files.

Done. I do not feel like it anymore. This sure is annoying. Why are introductory tutorials so hard?

Well, this difficulty here is just a matter of going through the UI, so I should hold on.

8:05pm. So far I am through the third of the tutorial. I am going to deal with the rest tomorrow. Once I do, I am going to ditch this crappy intro and go through the modeling path. I want to get a sense for how viable modeling is in Houdini. Right now, I am already starting to miss Blender.

There is no way around it, I should give Houdini at least a few weeks.

8:15pm. Let me start having fun here. A few months of practicing Houdini and I am going to be an expert. It does not matter if it takes me the entirety of 2022 until I can get going. I will get this done without fail."

---
## [mcsalter/advent-of-code2021](https://github.com/mcsalter/advent-of-code2021)@[f2bf8fe89a...](https://github.com/mcsalter/advent-of-code2021/commit/f2bf8fe89ad9ab70280096e72ac1209091a8e3c8)
#### Thursday 2022-01-20 20:18:33 by Lahral

day 4 complete

gosh darn you, `&`. This was a pain in the ass to deal with, yet another
sign I need work more on pointers and pass by reference/value.

day 4 completed far behind schedule. part 2 was quiet easy to do
compared to other days.

---

