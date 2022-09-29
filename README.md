## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-09-28](docs/good-messages/2022/2022-09-28.md)


2,229,513 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,229,513 were push events containing 3,370,360 commit messages that amount to 279,886,289 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 36 messages:


## [EoaNB-Team/EoaNB](https://github.com/EoaNB-Team/EoaNB)@[e9ef7e7b1f...](https://github.com/EoaNB-Team/EoaNB/commit/e9ef7e7b1f924239f49d260a5f0719cb9fcb561e)
#### Wednesday 2022-09-28 00:07:24 by Imperialism

MILLIONS OF FIXES + Load to Main menu now!!

Fixed Literally TONS OF SHIT FUCK PARADOX

---
## [stable-diffusion-ui/stable-diffusion-ui.github.io](https://github.com/stable-diffusion-ui/stable-diffusion-ui.github.io)@[fb7028cefb...](https://github.com/stable-diffusion-ui/stable-diffusion-ui.github.io/commit/fb7028cefbcee8004e4d1a0deca3cf3a0a012cdd)
#### Wednesday 2022-09-28 00:12:07 by JeLuF

Background image for the landing page

"fantasy forest landscape, mountains, milky way, blue vector elements, fantasy magic, dark light night, intricate, elegant, sharp focus, illustration, highly detailed, digital painting, concept art, matte, art by John Anster Fitzgerald and Albert Bierstadt, trending"
Seed 1819397
Guidance 11, PLMS, 512×320, 50 steps

---
## [OpenVZ/vzkernel](https://github.com/OpenVZ/vzkernel)@[c38fd1f65b...](https://github.com/OpenVZ/vzkernel/commit/c38fd1f65b10cd2676d66de16d660e5dbe9c0e3d)
#### Wednesday 2022-09-28 00:51:17 by Vladimir Davydov

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
## [AurevoirXavier/seeding](https://github.com/AurevoirXavier/seeding)@[83722b2365...](https://github.com/AurevoirXavier/seeding/commit/83722b236504884895555ed8a427c55178859b90)
#### Wednesday 2022-09-28 01:55:08 by Kian Paimani

Membership Request (#14)

# Membership Request 

Hi, I am Kian Paimani, known as @kianenigma. I have been working on Polkadot/Kusama through Parity since February 2019 and I can categorize my main contributions to Polkadot's ecosystem as follows: 

1. Maintaining and developing the staking sub-system.
2. General FRAME development, especially testing and quality assurance. 
3. Polkadot-native side-projects. 
4. Education 

> My first contribution to Polkadot is also indeed related to staking: https://github.com/paritytech/substrate/pull/1915

### Staking system

I joke as the Polkadot staking to be both my blessing and my curse over the years. I started working on it since the first days that I joined this ecosystem and the work [is ongoing ever since](https://github.com/orgs/paritytech/projects/33/views/9). In the past, I focused on making sure that the staking system is secure and to some extent scalable. More recently, I coordinated the (imminent) launch of Nomination Pools. Nowadays I also put an extra effort on making sure that this sub-system of Polkadot is *sustainable*, through code refactor and educating other core developers. 

Lastly, I have been the main author of the [Polkadot staking newsletter](https://gist.github.com/kianenigma/aa835946455b9a3f167821b9d05ba376), which is my main attempt at making the entire complexity and development of this part of the protocol transparent to the end-users.

I expect myself to contribute *directly* to the staking system for at least another ~12, if not more, and afterwards having the role of an advisor. 

Some notable contributions: 

- https://github.com/paritytech/substrate/pull/4517
- https://github.com/paritytech/substrate/pull/7910
- https://github.com/paritytech/substrate/issues/6242
- https://github.com/paritytech/substrate/pull/9415
- https://github.com/paritytech/polkadot/pull/3141
- https://github.com/paritytech/substrate/pull/11212
- https://github.com/paritytech/substrate/pull/12129

### FRAME 

Historically, I have contributed a variety of domains in FRAME, namely: 

- Early version of the weight system https://github.com/paritytech/substrate/pull/3816 https://github.com/paritytech/substrate/pull/3157
- Early version of the transaction fee system
- Primitive arithmetic types https://github.com/paritytech/substrate/pull/3456
- Council election pallet https://github.com/paritytech/substrate/pull/3364

Many of which were, admittedly, a PoC at most, if not considered "poor". I am happy that nowadays many of the above have been refactored and are being maintained by new domain experts. 

These days, I put most of my FRAME focus on testing and quality assurance. Through my work in the staking system, I have had to deal with the high sensitivity and liveness requirement of protocol development first hand (I believe I had to do among the [very first storage migrations](https://github.com/paritytech/substrate/pull/3948) in Kusama) and consequently I felt the need to make better testing facilities, all of which have been formulated in https://forum.polkadot.network/t/testing-complex-frame-pallets-discussion-tools/356. Some relevant PRs:

- https://github.com/paritytech/substrate/pull/8038
- https://github.com/paritytech/substrate/pull/9788
- https://github.com/paritytech/substrate/pull/10174

Regardless of wearing the staking hat, I plan to remain a direct contributor to FRAME, namely because I consider it to be an important requirements of successfully delivering more features to Polkadot's ecosystem. 

### Polkadot-Native Side Projects

I have started multiple small, mostly non-RUST projects in the polkadot ecosystem that I am very happy about, and I plan to continue doing so. I have not yet found the time to make a "polished product" out of any of these, but I hope that I can help foster our community such that someday a team will do so. I consider my role, for the time being, to *put ideas out there* through these side projects. 

- https://github.com/substrate-portfolio/polkadot-portfolio/
- https://github.com/kianenigma/polkadot-basic-notification/
- https://github.com/paritytech/polkadot-scripts/
- https://github.com/paritytech/substrate-debug-kit/

### Education 

Lastly, aside from having had a number of educational talks over the years (all of which [are listed](https://hello.kianenigma.nl/talks/) in my personal website), I am a big enthusiast of the newly formed Polkadot Blockchain Academy. I have [been an instructor](https://singular.app/collectibles/statemine/16/2) in the first cohort, and continue to contribute for as long and as much as I can, whilst still attending to the former 3 duties. 

---

With all of that being said and done, I consider myself at the beginning of the path to Dan 4, but happy to start at a lower one as well.

Co-authored-by: Bastian Köcher <git@kchr.de>

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[342f166d5e...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/342f166d5e7c527addcf8daf8974c0cac94c0f24)
#### Wednesday 2022-09-28 02:11:21 by SkyratBot

[MIRROR] Crab-17 No Longer Breaks Economy If You Swipe Too Fast [MDB IGNORE] (#16432)

* Crab-17 No Longer Breaks Economy If You Swipe Too Fast (#70094)

Hey there,

Remember swiping credit cards, before everything was chipped? You know how sometimes if you went too slow, the transaction might fail, the cashier had to plonk in some digits on their machine, and you had to go again? That kinda sucked.

If you're too young to get that reference, just imagine the card swiping task in AMONG US. Doesn't that minigame suck? You know exactly what that is. Same principle.

Anyways, that's pretty much what was going on here. The reason why SS.Economy would break so god damn hard if you swiped an ID before the machine's "boot up" slowflake animation was complete is probably due to the line where it starts fast processing. I added an early return to check for if the animation was complete by leveraging a var we already set at the end of the process, because I am lazy.

There's probably a few other ways you can tackle this issue, but this feels right to me in a thematic sense. I'm willing to change it if needed though.

* Crab-17 No Longer Breaks Economy If You Swipe Too Fast

Co-authored-by: san7890 <the@san7890.com>

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[79b4a74a6e...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/79b4a74a6e6f13128779f88cb784ecb1e5989524)
#### Wednesday 2022-09-28 02:11:21 by RimiNosha

[MODULAR] Fixes That Stupid Language Reset Bug That's Been Here Since Newprefs (#15802)

* I hate coders
This includes myself.

* Web edit~

* I give up, this is the best I got

* Make species take their alternate language instead of uncommon! Make language selection reflect foreigner, if selected!

* Remove code that assumed old foreigner add proc was called

* whyaremidroundspawnshandleddifferentlythanroundstartswhatthefuck

* Apply suggestion!

Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>

* Address last review at long last

* Apply suggestions!

Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>

Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[deb87e9ec0...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/deb87e9ec07fb6caff47cabaa8b5fdd760ea975b)
#### Wednesday 2022-09-28 02:11:21 by SkyratBot

[MIRROR] Fixes gravity pulse and transparent floor plane sharing a layer [MDB IGNORE] (#16446)

* Fixes gravity pulse and transparent floor plane sharing a layer (#70124)

fixes gravity pulse and transparent floor plane sharing a layer

Broken by #69642 , sorry
I'll open up a seperate PR later today with a unit test to catch these cases
(my later today is in like 10 hours)

closes #70123 (weird fucking floors)

* Fixes gravity pulse and transparent floor plane sharing a layer

Co-authored-by: Time-Green <timkoster1@hotmail.com>

---
## [gozulio/coyote-bayou](https://github.com/gozulio/coyote-bayou)@[8a27b0fe9d...](https://github.com/gozulio/coyote-bayou/commit/8a27b0fe9d5f5f30d2db06246970d76c74cfe00d)
#### Wednesday 2022-09-28 02:17:46 by bearrrrrrrrr

i'm KILLING you. i am KILLING y ou. i don't care about anything else i don't give a SHIT about anything else. my programming is just, 'GET THAT FUCKING GUY'

---
## [saboooor/guilded-discord-bridge](https://github.com/saboooor/guilded-discord-bridge)@[6dea32abaa...](https://github.com/saboooor/guilded-discord-bridge/commit/6dea32abaa60ad687da5eaf521967b00cb719e38)
#### Wednesday 2022-09-28 03:23:57 by saboooor

global variables so the next commit can be done without annoying ass shit

---
## [Clownsw/lokinet](https://github.com/Clownsw/lokinet)@[e981c9f899...](https://github.com/Clownsw/lokinet/commit/e981c9f89983a12cc75d691fc439366703d5bfff)
#### Wednesday 2022-09-28 04:21:03 by Jeff

tweaks for wine and yarn for gui

* allow specifying a custom yarn binary for building the gui using -DYARN= cmake option
* unset DISPLAY when calling wine because i hate popups
* do not rebuild gui when building for windows
* by setting the magical undocumented env var USE_SYSTEM_7ZA to 'true' we can have the pile of npm bullshit code use our system's local 7z binary instead of the probably not backdoored binary from npm, yes for real. i hate nodejs so god damn much you have no fucking idea
* allow providing a custom gui from a zip file via -DGUI_ZIP_FILE cmake option

---
## [Offroaders123/nbtify](https://github.com/Offroaders123/nbtify)@[b4470afa25...](https://github.com/Offroaders123/nbtify/commit/b4470afa255f3c0360affe6869051ebfb1ff3bd7)
#### Wednesday 2022-09-28 04:24:01 by Offroaders123

Rebranding: NBTify!

The official name has now arrived, NBTify! (like stringify) Couldn't quite decide on one so easily, and this seemed to be the best option. I wanted a name that is easy to remember, and simple to type. I was going to do something like WebNBT or Web-NBT (So it lines up with APIs like WebRTC, WebGPU, or Web Audio API), but I didn't like that it didn't start with NBT, and that there's already a "webNBT" project. While that one isn't JS-based, I didn't want to step on their toes for any naming confusions. So, went with making my own!

While shortlived, trying out GitHub Packages was really nice in the previous release, as you have everything tied into GitHub. It's as feature complete as npm for use in Node, but it turns out there isn't (yet) a way to load it from a CDN. I'm a little bit bummed about that, but I think it's for the best. So much of the industry lives off of npm, so I think it's time that I jump aboard too. So much more cool stuff I can do!

(Reflection time!)
Crazy to go through yet another leap in learning. So happy with how the library it turning out! It has given me so many more things to learn. TypeScript has been absolutely wonderful. Now that I'm at this stage, maybe I could look into making a browser NBT editor make with React!

Here's to learning!
*cheers*

Brandon :)

---
## [derkallevombau/VSCodeUserFiles_Tasks](https://github.com/derkallevombau/VSCodeUserFiles_Tasks)@[210598d4af...](https://github.com/derkallevombau/VSCodeUserFiles_Tasks/commit/210598d4af694aebdc3bbbdf60f322cd4ae9e9f6)
#### Wednesday 2022-09-28 05:12:15 by derkallevombau

tasks.json: "Git: Commit using mtime (append selection to commit message)": Handle quotes correctly.

This really drove me nuts!

First, I passed ${selectedText} within single quotes (no problem since
VS Code variables are substituted by VS Code before the command is
passed to the shell.
This way, I could select double-quoted strings until I selected "Git: Don't ignore".
This resulted in '"Git: Don't ignore"', so bash complained about not
finding the ' corresponding to the last char.
If I had put ${selectedText} into double quotes, I would have been able
to select text containing an arbitrary number of single quotes, but a
double-quoted string would have been passed without double quotes.

I remembered Perls quoting operators which are "on a higher level" than
litaral quotes, so you can do ‘q/"Git: Don't ignore"/’ without error.
Even though ‘q//’ is the single-quoting operator, it doesn't interfere
with a single quote in the string.

On 2022-09-23, I spent several hours until 15:53:12 trying everything
that came into my mind, but I was (too) drunk.

Now, after thinking "Fuck this shit!" for several days, I wanted to
solve it finally.

I tried again with Perl until I recognised that Perls operators cannot
help since when using ‘perl -e <string>’, <string> is processed by bash
and thus needs quoting, so the problem is the same as when quoting
${selectedText} directly.

Then I found that the options object has the property env which gives an
object that enables us to set variables that are then available to the
command, and since these variable definitions are processed by VS Code,
I gave it a try.

Since ${var@Q} quotes var in a way that the result can be reused for
input, I used this to quote the env var (I tried this very early, but
when trying to get ${selectedText} into a variable within a bash script,
the problem is the same as when passing it directly).

It didn't work, but the expansion looked promising and when using the
expanded value, it worked.
Thus it was clear that I had to use eval to get that effect.

Now it works whatever and how many quote chars the selected string
contains.

---
## [JohnFulpWillard/tgstation](https://github.com/JohnFulpWillard/tgstation)@[1810b85553...](https://github.com/JohnFulpWillard/tgstation/commit/1810b855536f05891593b1379e455164f45fab3a)
#### Wednesday 2022-09-28 06:32:59 by tralezab

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
## [vg-mjg/mjg-repo](https://github.com/vg-mjg/mjg-repo)@[c5d2f53d18...](https://github.com/vg-mjg/mjg-repo/commit/c5d2f53d182bf13be3dd85eb698c886fd23d31d4)
#### Wednesday 2022-09-28 06:49:21 by SouzuSweetroll

waifu2x stupid event edition

man these skins suck arse who gives a shit about chihori or >male

---
## [aryanraj2713/password_manager](https://github.com/aryanraj2713/password_manager)@[4275c80cc5...](https://github.com/aryanraj2713/password_manager/commit/4275c80cc5f363d01b94bfcfc92c2a62d0de47d8)
#### Wednesday 2022-09-28 08:26:05 by aryanraj

Made some changes to stupid ass decisions. Bitch you need yo ass whipped by black momma and a latino drugie dad :/

---
## [krishkatyal/password_manager](https://github.com/krishkatyal/password_manager)@[747369e099...](https://github.com/krishkatyal/password_manager/commit/747369e09995fc387c8c7ac36839585e49da6473)
#### Wednesday 2022-09-28 08:28:26 by Krish Katyal

Merge pull request #1 from aryanraj2713/main

Made some changes to stupid ass decisions. Bitch you need yo ass whip…

---
## [N0no/MonkeStation](https://github.com/N0no/MonkeStation)@[31c9d411a7...](https://github.com/N0no/MonkeStation/commit/31c9d411a7b9e4f6ad66b930d535e24e5555bd06)
#### Wednesday 2022-09-28 09:22:42 by nednaZ

Dynamic Adjustments Part 2 (#627)

* Dynamic Changes II

Changes the intercept message to be more flavorful.

Clamps the threat level to between 75% player pop and 200% player pop.

Logs increases to Dynamic threat budget.

Slightly reduces the weight of latejoin traitors. (From 7 to 4)

Increases the Weight (2 to 4), decreases the Cost (40 to 20) and decreases Minimum Players (35 to 30) of Revolution Latejoins.

Restores Heretics to Latejoin and Roundstart.

Heretics now have a lower number of sacrifice objectives. (From 2-6 to 1-3)

Heretics now have a chance to get a Steal objective.

Dynamic Abductors may no longer get spawned  in solo by mistake.

Midround Traitor chance reduced. (From 7 to 5)
Midround Traitor cap reduced. (From player_count / 10 to player_count / 15)

Midround Wizard weight increased (From 1 to 3)
Midround Wizards are now a HIGH_IMPACT_RULESET and will not repeat.

Midround Nuclear Operative Weight reduced. (From 5 to 4)

Blob Weight (4 to 3) and Cost (10 to 25) changed.

Xenomorph Cost increased (10 to 25)

Nightmare Cost increased (10 to 15)

Abductor Cost increased (10 to 15)

Space Pirates added to Dynamic.

Space Pirates have been given an update, with ship names and support for multiple types of pirates existing.

Revenant added to Dynamic.

Obsessed added to Dynamic.

Space Dragon early start changed to 40 minutes (From 50 minutes)

Roundstart Traitor cost increased (7 to 8)

Blood Brother Weight (4 to 2), Cost(15 to 13) and Scaling Cost(15 to 13) adjusted.

Changeling Weight(3 to 4) and Cost(15 to 17) adjusted.

Roundstart Wizard Weight(2 to 5) and Cost(40 to 30) adjusted.

Blood and Clock Cult Weight and Cost(30 to 25) adjusted.

Nuclear Operatives Weight(3 to 4) and Cost(50 to 25) adjusted.

* lone op

why didn't this commit

* Reverts max_traitors change

The maximum number of traitors is now player_count / 10 rather than 15

* Revolution Tweaks

Reduces the weight of latejoin revs from 4 to 2.

Increases the minimum number of required enemies from 2-0 to 5.

Changes the required enemies to be only security and the captain, AI and Cyborg are not counted.

The shuttle is no longer automatically called upon a Revolution victory.

There will be an announcement made after either 30% of the station is converted into revolutionaries OR if two heads of staff are killed.

* Pirate Fixes

Pirates now function as intended in Dynamic.

Pirates have a 25 player minimum to be called as antagonists.

Pirates have a minimum of 2 enemies before they can be called.

* Faster than opening VSC.

---
## [MortemTeam/erisgrim](https://github.com/MortemTeam/erisgrim)@[29430253ff...](https://github.com/MortemTeam/erisgrim/commit/29430253ffa7c3394df438c922c3827bfbf79f51)
#### Wednesday 2022-09-28 09:29:35 by maikilangiolo

Levergun re do (#7587)

* update timer (#7501)

* FUCK YOU FUCK YOUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU

* Update code/modules/projectiles/guns/projectile/battle_rifle/levergun.dm

Co-authored-by: hyperioo <64754494+hyperioo@users.noreply.github.com>

---
## [SaidSultan1/EventListener-Paractice](https://github.com/SaidSultan1/EventListener-Paractice)@[69bd18d6e3...](https://github.com/SaidSultan1/EventListener-Paractice/commit/69bd18d6e3bf7fc0e949f865b66f7d66db9666e1)
#### Wednesday 2022-09-28 10:15:43 by SaidSultan1

Delete outrageous-contempt-fuck-you-hand-260nw-655065910.webp

---
## [grafana/tanka](https://github.com/grafana/tanka)@[904a7c53e8...](https://github.com/grafana/tanka/commit/904a7c53e8a1afec5af8b05bb11f7da846595a09)
#### Wednesday 2022-09-28 10:26:36 by Julien Duchesne

Fix `getSnippetHash` not considering all files (#765)

* Fix `getSnippetHash` not considering all files
Made a stupid mistake in the previous PR: https://github.com/grafana/tanka/pull/759

This fixes it and adds another benchmark test to ensure it doesn't happen again.
I also removed the Github Actions benchmark test, as it's not really useful, anytime we change the tests, we'll get erroneous results which will be annoying.
Instead, I added the benchmark tests to the Drone run, we can compare whenever we want.

* linting

* Add changelog, will release straight away

---
## [tfcace/cadence-client](https://github.com/tfcace/cadence-client)@[f5e0fd25e4...](https://github.com/tfcace/cadence-client/commit/f5e0fd25e4347c85b28dac87f51b532700455d2c)
#### Wednesday 2022-09-28 10:36:13 by Steven L

Sharing one of my favorite "scopes" in intellij, and making it easier to add more (#1182)

Goland is nice, and the type-based navigation is wildly superior to gopls-driven
stuff in my experience, so I tend to lean hard on it when I'm able.

By default though, Goland searches *everything*.  All the time.
That's totally reasonable as a default, but we can do better:

- Tests are not usually all that interesting when trying to understand and navigate code.
  (perhaps they should be, but that's more a platonic ideal than a reality)
- Generated RPC code is almost never useful to dive into.  The exposed API surface is sufficient,
  if it compiles, it's correct.
- Non-Go files are just less interesting in a Go project.

So this scope excludes ^ all that.
To add more shared ones, just check the "share through vcs" box and commit it.

To use it, just select the scope from the dropdown when you search.  E.g. "find in files" ->
change from "in project" to "scope" -> change the dropdown.  This custom scope will now appear,
and it'll remember what you last used, so it's a nice default.

This also works in "call hierarchy", "go to implementations" (open it in a panel to configure it,
with the gear on the side.  it's awful UI but it works), etc quite a lot of places.

This same kinda-obtuse search-scope query language can be used to mark things as generated or test
related, which will also help other parts of the IDE mark things as more or less relevant for you.
It's worth exploring a bit, scopes and filters can be used to do a lot: https://www.jetbrains.com/help/idea/scope-language-syntax-reference.html

---
## [Atom-X-Devs/android_kernel_xiaomi_sm7325](https://github.com/Atom-X-Devs/android_kernel_xiaomi_sm7325)@[74e8fdcc11...](https://github.com/Atom-X-Devs/android_kernel_xiaomi_sm7325/commit/74e8fdcc11828f817aa8908eb957dbf9ae1a357b)
#### Wednesday 2022-09-28 10:56:01 by Daniel Vetter

dma_resv: prime lockdep annotations

Full audit of everyone:

- i915, radeon, amdgpu should be clean per their maintainers.

- vram helpers should be fine, they don't do command submission, so
  really no business holding struct_mutex while doing copy_*_user. But
  I haven't checked them all.

- panfrost seems to dma_resv_lock only in panfrost_job_push, which
  looks clean.

- v3d holds dma_resv locks in the tail of its v3d_submit_cl_ioctl(),
  copying from/to userspace happens all in v3d_lookup_bos which is
  outside of the critical section.

- vmwgfx has a bunch of ioctls that do their own copy_*_user:
  - vmw_execbuf_process: First this does some copies in
    vmw_execbuf_cmdbuf() and also in the vmw_execbuf_process() itself.
    Then comes the usual ttm reserve/validate sequence, then actual
    submission/fencing, then unreserving, and finally some more
    copy_to_user in vmw_execbuf_copy_fence_user. Glossing over tons of
    details, but looks all safe.
  - vmw_fence_event_ioctl: No ttm_reserve/dma_resv_lock anywhere to be
    seen, seems to only create a fence and copy it out.
  - a pile of smaller ioctl in vmwgfx_ioctl.c, no reservations to be
    found there.
  Summary: vmwgfx seems to be fine too.

- virtio: There's virtio_gpu_execbuffer_ioctl, which does all the
  copying from userspace before even looking up objects through their
  handles, so safe. Plus the getparam/getcaps ioctl, also both safe.

- qxl only has qxl_execbuffer_ioctl, which calls into
  qxl_process_single_command. There's a lovely comment before the
  __copy_from_user_inatomic that the slowpath should be copied from
  i915, but I guess that never happened. Try not to be unlucky and get
  your CS data evicted between when it's written and the kernel tries
  to read it. The only other copy_from_user is for relocs, but those
  are done before qxl_release_reserve_list(), which seems to be the
  only thing reserving buffers (in the ttm/dma_resv sense) in that
  code. So looks safe.

- A debugfs file in nouveau_debugfs_pstate_set() and the usif ioctl in
  usif_ioctl() look safe. nouveau_gem_ioctl_pushbuf() otoh breaks this
  everywhere and needs to be fixed up.

v2: Thomas pointed at that vmwgfx calls dma_resv_init while it holds a
dma_resv lock of a different object already. Christian mentioned that
ttm core does this too for ghost objects. intel-gfx-ci highlighted
that i915 has similar issues.

Unfortunately we can't do this in the usual module init functions,
because kernel threads don't have an ->mm - we have to wait around for
some user thread to do this.

Solution is to spawn a worker (but only once). It's horrible, but it
works.

v3: We can allocate mm! (Chris). Horrible worker hack out, clean
initcall solution in.

v4: Annotate with __init (Rob Herring)

Cc: Rob Herring <robh@kernel.org>
Cc: Alex Deucher <alexander.deucher@amd.com>
Cc: Christian König <christian.koenig@amd.com>
Cc: Chris Wilson <chris@chris-wilson.co.uk>
Cc: Thomas Zimmermann <tzimmermann@suse.de>
Cc: Rob Herring <robh@kernel.org>
Cc: Tomeu Vizoso <tomeu.vizoso@collabora.com>
Cc: Eric Anholt <eric@anholt.net>
Cc: Dave Airlie <airlied@redhat.com>
Cc: Gerd Hoffmann <kraxel@redhat.com>
Cc: Ben Skeggs <bskeggs@redhat.com>
Cc: "VMware Graphics" <linux-graphics-maintainer@vmware.com>
Cc: Thomas Hellstrom <thellstrom@vmware.com>
Reviewed-by: Thomas Hellstrom <thellstrom@vmware.com>
Reviewed-by: Christian König <christian.koenig@amd.com>
Reviewed-by: Chris Wilson <chris@chris-wilson.co.uk>
Tested-by: Chris Wilson <chris@chris-wilson.co.uk>
Signed-off-by: Daniel Vetter <daniel.vetter@intel.com>
Link: https://patchwork.freedesktop.org/patch/msgid/20191104173801.2972-1-daniel.vetter@ffwll.ch
Signed-off-by: Divyanshu-Modi <divyan.m05@gmail.com>

---
## [EthanRockss/tgstation](https://github.com/EthanRockss/tgstation)@[d34fa4c642...](https://github.com/EthanRockss/tgstation/commit/d34fa4c642839215df5ba985d098a04e4d555b5b)
#### Wednesday 2022-09-28 11:18:22 by LemonInTheDark

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
## [Totktonada/tarantool](https://github.com/Totktonada/tarantool)@[20be1c9197...](https://github.com/Totktonada/tarantool/commit/20be1c91976f298614783d6d9153dcf81c29b055)
#### Wednesday 2022-09-28 12:26:46 by Alexander Turenko

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
## [Stalkeros2/Skyrat-tg](https://github.com/Stalkeros2/Skyrat-tg)@[f73fc2ea10...](https://github.com/Stalkeros2/Skyrat-tg/commit/f73fc2ea10c3193a56595e9d02d9aab186d99076)
#### Wednesday 2022-09-28 12:36:14 by Halcyon

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
## [LetsZiggy/black](https://github.com/LetsZiggy/black)@[0019261abc...](https://github.com/LetsZiggy/black/commit/0019261abcf6d9e564ba32d3cc15534b9026f29e)
#### Wednesday 2022-09-28 12:55:26 by Richard Si

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
## [gadget-inc/dateilager](https://github.com/gadget-inc/dateilager)@[4348da1c34...](https://github.com/gadget-inc/dateilager/commit/4348da1c3488187e0d209ebd89a69ffa5adad753)
#### Wednesday 2022-09-28 14:15:59 by Harry Brundage

Recover from arbitrary errors writing files by removing the thing we're about to write

I encountered a sequence of changes that DL didn't expect where I was creating a symlink at a path that was previously a folder full of files. There's a bunch of other annoying cases like this, where we should be able to go from any state on disk to any new incoming object type. The existing strategy did a bit of checking to see if stuff wasn't quite right, but I think we aught to be a bit more robust. The recovery strategy is always the same if we have a new incoming object: delete whatever is there so we can just write the new thing on top. If we're gonna do that, I think we can do it a bit more blindly. Instead of checking ahead of time for erroneous conditions (which also requires another syscall every write), we just blindly try to do the thing we need to do, and if it fails, remove whatever is there and try again. That way, we don't need to anticipate whatever fucked up case is on disk at the time and instead just blow it away. I also like this because it makes the fast path a bit faster where we do less checking up front and just let the kernel tell us we're doing something weird.

---
## [Sid127/cutie-bot](https://github.com/Sid127/cutie-bot)@[52c2dc6f7d...](https://github.com/Sid127/cutie-bot/commit/52c2dc6f7d9188e512e55bf9275791a45108ddba)
#### Wednesday 2022-09-28 16:02:37 by Sid Pranjale

correct whatever the fuck stupid shit I did with the autoroles in verify

---
## [darthelit/WoWAnalyzer](https://github.com/darthelit/WoWAnalyzer)@[90c1dd8db4...](https://github.com/darthelit/WoWAnalyzer/commit/90c1dd8db4b04d465daf45332ec73a28130651d1)
#### Wednesday 2022-09-28 16:04:10 by Richard Harrah

second pass on demon hunter

clean out changelog entries referencing
abilities that are removed in DF

add sigils to HDH abilities list

clean out entries in SPELLS/demonhunter that are
present in TALENTS/demonhunter

add support for Charred Warblades

add getTalentRank function for Combatant

correct locations of multiple analyzers in the
statistics tab

add support for Misery in Defeat class talent

add support for Retaliation talent

add Buffs module for Vengeance to make frailty
support easier, given that it can now be applied by
three different abilities.

add support for Painbringer talent

add Blur and Darkness to Vengeance

add support for Tactical Retreat talent

add support for Initiative talent

update support for Cycle of Hatred talent

correct Know Your Enemy scaling

regenerate DH talents

---
## [rd-stuffs/msm-4.14](https://github.com/rd-stuffs/msm-4.14)@[86e55310ed...](https://github.com/rd-stuffs/msm-4.14/commit/86e55310ed6018a1193b4ffd812649f9c9ccb7b4)
#### Wednesday 2022-09-28 18:13:49 by Wang Han

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
## [sjp38/linux](https://github.com/sjp38/linux)@[9c61d5321e...](https://github.com/sjp38/linux/commit/9c61d5321e94a4d0678b5eb0515afc590bdb9740)
#### Wednesday 2022-09-28 18:30:39 by Peter Xu

mm/x86: use SWP_TYPE_BITS in 3-level swap macros

Patch series "mm: Remember a/d bits for migration entries", v4.


Problem
=======

When migrating a page, right now we always mark the migrated page as old &
clean.

However that could lead to at least two problems:

  (1) We lost the real hot/cold information while we could have persisted.
      That information shouldn't change even if the backing page is changed
      after the migration,

  (2) There can be always extra overhead on the immediate next access to
      any migrated page, because hardware MMU needs cycles to set the young
      bit again for reads, and dirty bits for write, as long as the
      hardware MMU supports these bits.

Many of the recent upstream works showed that (2) is not something trivial
and actually very measurable.  In my test case, reading 1G chunk of memory
- jumping in page size intervals - could take 99ms just because of the
extra setting on the young bit on a generic x86_64 system, comparing to
4ms if young set.

This issue is originally reported by Andrea Arcangeli.

Solution
========

To solve this problem, this patchset tries to remember the young/dirty
bits in the migration entries and carry them over when recovering the
ptes.

We have the chance to do so because in many systems the swap offset is not
really fully used.  Migration entries use swp offset to store PFN only,
while the PFN is normally not as large as swp offset and normally smaller.
It means we do have some free bits in swp offset that we can use to store
things like A/D bits, and that's how this series tried to approach this
problem.

max_swapfile_size() is used here to detect per-arch offset length in swp
entries.  We'll automatically remember the A/D bits when we find that we
have enough swp offset field to keep both the PFN and the extra bits.

Since max_swapfile_size() can be slow, the last two patches cache the
results for it and also swap_migration_ad_supported as a whole.

Known Issues / TODOs
====================

We still haven't taught madvise() to recognize the new A/D bits in
migration entries, namely MADV_COLD/MADV_FREE.  E.g.  when MADV_COLD upon
a migration entry.  It's not clear yet on whether we should clear the A
bit, or we should just drop the entry directly.

We didn't teach idle page tracking on the new migration entries, because
it'll need larger rework on the tree on rmap pgtable walk.  However it
should make it already better because before this patchset page will be
old page after migration, so the series will fix potential false negative
of idle page tracking when pages were migrated before observing.

The other thing is migration A/D bits will not start to working for
private device swap entries.  The code is there for completeness but since
private device swap entries do not yet have fields to store A/D bits, even
if we'll persistent A/D across present pte switching to migration entry,
we'll lose it again when the migration entry converted to private device
swap entry.

Tests
=====

After the patchset applied, the immediate read access test [1] of above 1G
chunk after migration can shrink from 99ms to 4ms.  The test is done by
moving 1G pages from node 0->1->0 then read it in page size jumps.  The
test is with Intel(R) Xeon(R) CPU E5-2630 v4 @ 2.20GHz.

Similar effect can also be measured when writting the memory the 1st time
after migration.

After applying the patchset, both initial immediate read/write after page
migrated will perform similarly like before migration happened.

Patch Layout
============

Patch 1-2:  Cleanups from either previous versions or on swapops.h macros.

Patch 3-4:  Prepare for the introduction of migration A/D bits

Patch 5:    The core patch to remember young/dirty bit in swap offsets.

Patch 6-7:  Cache relevant fields to make migration_entry_supports_ad() fast.

[1] https://github.com/xzpeter/clibs/blob/master/misc/swap-young.c


This patch (of 7):

Replace all the magic "5" with the macro.

Link: https://lkml.kernel.org/r/20220811161331.37055-1-peterx@redhat.com
Link: https://lkml.kernel.org/r/20220811161331.37055-2-peterx@redhat.com
Signed-off-by: Peter Xu <peterx@redhat.com>
Reviewed-by: David Hildenbrand <david@redhat.com>
Reviewed-by: Huang Ying <ying.huang@intel.com>
Cc: Hugh Dickins <hughd@google.com>
Cc: "Kirill A . Shutemov" <kirill@shutemov.name>
Cc: Alistair Popple <apopple@nvidia.com>
Cc: Andrea Arcangeli <aarcange@redhat.com>
Cc: Minchan Kim <minchan@kernel.org>
Cc: Andi Kleen <andi.kleen@intel.com>
Cc: Nadav Amit <nadav.amit@gmail.com>
Cc: Vlastimil Babka <vbabka@suse.cz>
Cc: Dave Hansen <dave.hansen@intel.com>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>

---
## [RashaMou/Synergy](https://github.com/RashaMou/Synergy)@[443d2f70a5...](https://github.com/RashaMou/Synergy/commit/443d2f70a575b053437240f7fadd89528a23b0e0)
#### Wednesday 2022-09-28 18:31:25 by Michael McClimon

Rototron: attempt to fix a Monday time zone bug

Australians report that their morning reports do not contain duty
rotations; we're pretty sure this is because they're sent on Sunday UTC,
when there is no duty assigned. I think we can fix this by always
passing in a time zone to current_officers_for_duty, which will affect
the calendar search we're doing.

I'm not totally sure this will work, because time zones are weird and
the Rototron code is also kinda weird, but I don't think it's likely to
be _worse_.

---
## [lgritz/OpenShadingLanguage](https://github.com/lgritz/OpenShadingLanguage)@[749b8ff82d...](https://github.com/lgritz/OpenShadingLanguage/commit/749b8ff82d88ebf92ae1d58641d9fdb0a43b0be9)
#### Wednesday 2022-09-28 18:40:49 by Larry Gritz

LLVM 15.0 support

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
## [zydras/Skyrat-tg](https://github.com/zydras/Skyrat-tg)@[e7230e8b4a...](https://github.com/zydras/Skyrat-tg/commit/e7230e8b4a6d60e1b6c025b52b9f3d2fc26577a5)
#### Wednesday 2022-09-28 21:01:14 by SkyratBot

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
## [dgmstuart/swing-out-london](https://github.com/dgmstuart/swing-out-london)@[72921de7f9...](https://github.com/dgmstuart/swing-out-london/commit/72921de7f9c9b52d83eedaa75fc988ecfcf8de0a)
#### Wednesday 2022-09-28 22:54:33 by Duncan Stuart

Remove event shortname

This was used originally to have a quick way to find events eg.
something like

events/edit/rr

...for red rhythm.

I think this was motivated by a "we have data so let's record it" kind
of thinking: RR was how me and my friends would refer to this event in
text.

But it hasn't been used in many years and it seems that the feature
using it was removed a while back.

This is the list of shortnames at the time of removal:

[id, title, shortname]
[8, "Blitz Party", "blitz"],
[9, "Swing Pit", "pit"],
[10, "Saturday Night Swing Club", "snscfirefly"],
[14, "Rock a hula", "rockahula"],
[18, "Swing Den East (Beginner social)", "swingden"],
[21, "Swing Patrol", "spoldst"],
[22, "Black Cotton Club", "blackcotton"],
[27, "Mouthful O'Jam", "mfoj"],
[33, "Book Club Blues", "bcb"],
[42, "A-Train", "atrain"],
[43, "The Swing Cellar", "swingcellar"],
[49, "Hellzapoppin", "helza"],
[50, "Gangbusters", "gb"],
[58, "Down Home Blues - VENUE CHANGE", "dhb"],
[69, "Die Freche Muse", "dfm"],
[96, "Swing Patrol", "spcamden"],
[103, "Swingout East", "swingouteast"],
[131, "Afternoon Tea Dance (Ballroom, Latin and Swing)", "ragroof"],
[142, "Swing Patrol Waterloo", "spwaterloo"],
[145, "The Candlelight Club", "cc"],
[170, "Holborn Hop", "holbornhop"],
[171, "Swing Patrol", "spangel"],
[199, "The Sunday Shuffle (Balboa social) NEW VENUE", "shuffle"],
[221, "The Jump Session", "jumpsession"],
[222, "Red Rhythm", "rr"],
[241, "Swing it! Rock it! Roll it!", "swingit"],
[251, "Pussyfoot", "pussyfoot"],
[260, "Suzi Q", "suziq"],
[277, "Ain't Misbehavin'", "misbehavin"],
[282, "Swing Cat's Jam", "swingcatsjam"],
[283, "After Hours", "churchill"],
[287, "Swing Patrol Pop-up Balboa", "popupbal"],
[289, "", "swinglandbrix"],
[290, "Swing at the Abbey", "thelight"],
[292, "", "spfin"],
[294, "Swing Patrol", "spstockwell"],
[295, "Swing Patrol Christmas Party", "spxmas"],
[297, "", "spputney"],
[298, "", "spstmarks"],
[302, "Swing Rendezvous (afternoon)", "swingrv"],
[318, "", "spbloomsbury"],
[320, "", "spbattersea"],
[322, "(SP Balboa)", "spbal"],
[331, "King Candy & the Sugar Push Present: Let Me Off Downtown!", "downtown"],
[334, "Sin City Blues", "sincity"],
[335, "Tuesday Blues Circus", "tuesblues"],
[337, "", "spnottinghill"],
[342, "Midweek Function", "midweek"],
[353, "The Shellac Shake", "shellac"],
[354, "NW6 Swing Den (Beginner Social)", "nwsix"],
[357, "Snakehip Swing (free)", "snake"],
[358, "Brew that Hop", "brew"],
[368, "The Blues Café", "bluescafe"],
[382, "Swing Joint", "swingjoint"],
[385, "Phoenix Dance Club", "phoenix"],
[398, "(This joint is) Jumpin'", "jumpin"],
[403, "Jitterbugs", "jitts"],
[404, "Bal Fridays", "balfridays"],
[412, "Minor Swing (with the Kings Cross Hot Club)", "minorswing"],
[416, "Herr Kettners Kabaret", "kabaret"],
[426, "King Candy & the Sugar Push Present: Let Me Off Downtown!", "lmod"],
[435, "Blues at the Ritzy", "ritzyblues"],
[437, "Saturday Night Swing Club", "snsc"],
[453, "", "spbrix"],
[455, "", "spuol"],
[510, "Club Savoy", "clubsavoy"],
[544, "Kings X Swing (Collegiate Shag social)", "kxs"],
[662, "", "spsoho"],
[690, "Opus One", "opusone"],
[708, "Wireless", "wireless"],
[719, "Pink Swing (LGBT)", "pink"],
[747, "Southside Strutters", "sss"],
[779, "", "spng"],
[817, "", "spcj"],
[891, "The Broken Swing Band Presents: Swing On The Square", "sots"],
[960, "Secret Late at the Horniman Museum", "hornimanlate"]

---
## [thecsw/thecsw.github.io](https://github.com/thecsw/thecsw.github.io)@[5e2f14ba82...](https://github.com/thecsw/thecsw.github.io/commit/5e2f14ba823ec6c9568ab6bea506012c5c9493bc)
#### Wednesday 2022-09-28 23:38:59 by sanfran

[ASTRIE] Added a new fortune: ** 271; 12022 H.E.

God's in his heaven --\ All's right with the world!

---

