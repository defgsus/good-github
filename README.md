## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-06-09](docs/good-messages/2022/2022-06-09.md)


1,731,420 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,731,420 were push events containing 2,752,737 commit messages that amount to 199,931,587 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 26 messages:


## [Blokyk/Parsex](https://github.com/Blokyk/Parsex)@[a101c933a0...](https://github.com/Blokyk/Parsex/commit/a101c933a038229425d9a0f41b6c659274aebb11)
#### Thursday 2022-06-09 00:03:52 by Blokyk

Parsing bugfix related to obj inst./new()

This fucking bug has been here for 2 and a half years, ever since object
instantiation was first implemented. What does it look like ?

	new string() + "hello"

That's it.

A simple fucking addition would make the new() parselet error out.

This is why you write tests kids.

Good night

~this is why i should write tests~

---
## [arvind-murty/vitess](https://github.com/arvind-murty/vitess)@[dbfb9a49f7...](https://github.com/arvind-murty/vitess/commit/dbfb9a49f7c3b067221d0aae0d3c0285e6baf098)
#### Thursday 2022-06-09 00:12:09 by Andrew Mason

[vtadmin] Add infrastructure for generating authz tests for vtadmin (#10397)

* Add infrastructure for generating authz tests for vtadmin

The lack of verifying authz checks are where they should be is one of the
most glaring issues in vtadmin (in my opinion; it's also my "fault" things
are this way). At the same time, writing all the code by hand to verify
every single endpoint would be a giant pain (which is the main reason
things are this way). So, let's codegen all the bits we don't care about!
The bonus here is that the config.json now can serve as authoritative on
what permissions are required for what endpoints.

The goal here is to have the config primarily specify the rules needed for
each endpoint, with as minimal "overhead" (currently specifying test cases
and mock data) as possible.

I want to separate the introduction of this setup from its complete
adoption, so I will submit a follow-up change that adds the rest of the
endpoint tests.

Signed-off-by: Andrew Mason <andrew@planetscale.com>

* add missing license headers

Signed-off-by: Andrew Mason <andrew@planetscale.com>

* Add make target and CI check

Signed-off-by: Andrew Mason <andrew@planetscale.com>

---
## [Knuxfan24/Knuxs-Misc-Tools](https://github.com/Knuxfan24/Knuxs-Misc-Tools)@[c2f2898d62...](https://github.com/Knuxfan24/Knuxs-Misc-Tools/commit/c2f2898d620895f0b9a3226f28c7887ce7678348)
#### Thursday 2022-06-09 00:37:00 by Knux

(WoC) Really bad OBJ stuff like fucking shit what the hell

Imagine following a standard specification and not having to break it so much!

---
## [nikothedude/tgstation](https://github.com/nikothedude/tgstation)@[98f32035d8...](https://github.com/nikothedude/tgstation/commit/98f32035d8dbd6b925700e9934652d03739f024b)
#### Thursday 2022-06-09 01:01:42 by LemonInTheDark

Parallax but better: Smooth movement cleanup (#66567)

* Alright, so I'm optimizing parallax code so I can justify making it do a
bit more work

To that end, lets make the checks it does each process event based.
There's two. One is for a difference in view, which is an easy fix since
I added a view setter like a year back now.

The second is something planets do when you change your z level.
This gets more complicated, because we're "owned" by a client.
So the only real pattern we can use to hook into the client's mob's
movement is something like connect_loc_behalf.

So, I've made connect_mob_behalf. Fuck you.

This saves a proc call and some redundant logic

* Fixes random parallax stuttering

Ok so this is kinda a weird one but hear me out.

Parallax has this concept of "direction" that some areas use, mostly
the shuttle transit ones. Set when you move into a new area.
So of course it has a setter. If you pass it a direction that it doesn't
already have, it'll start up the movement animation, and disable normal
parallax for a bit to give it some time to get going.

This var is typically set to 0.

The problem is we were setting /area/space's direction to null in
shuttle movement code, because of a forgotten proc arg.

Null is of course different then 0, so this would trigger a halt in
parallax processing.

This causes a lot of strange stutters in parallax, mostly when you're
moving between nearspace and space. It looks really bad, and I'm a bit
suprised none noticed.

I've fixed it, and added a default arg to the setter to prevent this
class of issue in future. Things look a good bit nicer this way

* Adds animation back to parallax

Ok so like, I know this was removed and "none could tell" and whatever,
and in fairness this animation method is a bit crummy.

What we really want to do is eliminate "halts" and "jumps" in the
parallax moveemnt. So it should be smooth.

As it is on live now, this just isn't what happens, you get jumping
between offsets. Looks frankly, horrible. Especially on the station.

Just what I've done won't be enough however, because what we need to do
is match our parallax scroll speed with our current glide speed. I need
to figure out how to do this well, and I have a feeling it will involve
some system of managing glide sources.

Anyway for now the animation looks really nice for ghosts with default
(high) settings, since they share the same delay.

I've done some refactoring to how old animation code worked pre (4b04f9012d1763df625e9e4ae75e4cf4bd1f3771). Two major
changes tho.

First, instead of doing all the animate checks each time we loop over a
layer, we only do the layer dependant ones. This saves a good bit of
time.

Second, we animate movement on absolute layers too. They're staying in
the same position, but they still move on the screen, so we do the same
gental leaning. This has a very nice visual effect.

Oh and I cleaned up some of the code slightly.

---
## [OpenVZ/vzkernel](https://github.com/OpenVZ/vzkernel)@[4f3761e84b...](https://github.com/OpenVZ/vzkernel/commit/4f3761e84b8bb7aef1bfe58b8caa08602cee18a6)
#### Thursday 2022-06-09 01:07:12 by Vladimir Davydov

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
## [bleakassassin/pokeemerald](https://github.com/bleakassassin/pokeemerald)@[981c98845b...](https://github.com/bleakassassin/pokeemerald/commit/981c98845b0d0468fefb0601bf6aef04673b61c5)
#### Thursday 2022-06-09 02:10:18 by bleakassassin

Lilycove Lady overhaul/3rd Hoenn Starter

All three Lilycove Ladies now appear in the game at one time:

*The Quiz Lady appears on the first floor of the Lilycove Dept. Store.
*The Favor Lady appears in the Lilycove Pokemon Center, where the Lilycove Lady normally appears.
*The Contest Lady appears on the right side of the Contest Hall with her contest Pokemon.

Lilycove Lady data has been modified and expanded to support both Quiz and Favor Ladies while also retaining compatibility with vanilla Emerald. When record mixing, the game sends and accepts the following data:

*From hack to hack: Quiz and Favor Ladies
*From hack to vanilla: Quiz Lady
*From vanilla to hack: Either Quiz or Favor Ladies, depending on which is in the vanilla game.

The Contest Lady has been overhauled into a strictly-local, single-player experience. No data from her is sent to or accepted from other copies of Emerald, hack or otherwise, when record mixing:

*You can give the Contest Lady one Pokeblock a day.
*If her contest appearance on TV results in victory, she gifts you the third Hoenn starter (the one neither you nor rival Brendan/May chose).
*If she loses the contest, you can continue to give Pokeblocks to her Pokemon. However, giving her another Pokeblock that doesn't match her Pokemon's condition will result in another contest loss.
*If she loses the contest badly (i.e. you gave her no Pokeblocks that match her Pokemon's condition), you have to start all over, possibly with a different Pokemon.
*Her dialogue has been heavily expanded to account for all potential outcomes.

Other changes:

*Reset Lilycove Ladies when importing a vanilla save.
*The Quiz Lady refers to herself when giving the player a prize as "me" instead of "Lady".
*"Yes" and "No" choices for canceling out of the Bag/Pokeblock Case without giving an item/Pokeblock to the Favor/Contest Lady have been flipped to behave how you'd expect them to.
*Capitalization of all Lilycove Lady terms to match the rest of the game.
*Optimization of Lilycove Lady scripts and functions.

P.S.: The Bulbapedia page on the Lilycove Ladies - outside of the Quiz Lady - is so, SO wrong.

---
## [coreyja/battlesnake-rs](https://github.com/coreyja/battlesnake-rs)@[123913ae47...](https://github.com/coreyja/battlesnake-rs/commit/123913ae47c87ee2d7f8f264b28da2dfba536e50)
#### Thursday 2022-06-09 03:59:25 by Corey Alexander

OOOPs bug in the macro means I don't think I was ever actually doing my new logic tonight :facepalm:

---
## [tgstation/map_depot](https://github.com/tgstation/map_depot)@[557b707646...](https://github.com/tgstation/map_depot/commit/557b707646dbac016afea2447ab437910b508896)
#### Thursday 2022-06-09 05:33:36 by san7890

Updates Pubby (Fire Alarm Edition) (#43)

I stress-tested pubby on production today, and everything seemed chill. Few things though:

A) They still have a BZ Can in Xenobiology. However, this should stay until someone bothers to put in a cold chamber to Ordnance.

B) Very sparse fire alarms, and the areas are way too massive in the central primary hallways in relation to the firelocks it has. I'll recitfy that now.

C) Monastary Exterior Decalling fucking sucks. I'm fixing that by using plating sand instead of whatever other sand they were using.

* Defines Cargo Lobby Area

* Moves stuff out from being next to firelocks

* Split Up Chapel Areas

* Upper Cargo Warehouse is now Drone Bay

* Area Misc Fixes (ass line)

* Maybe some other stuff

---
## [SaintPhilosopher/thewasteland](https://github.com/SaintPhilosopher/thewasteland)@[013fb2bd4b...](https://github.com/SaintPhilosopher/thewasteland/commit/013fb2bd4bd6ce216844c984da9dc5ffed316c61)
#### Thursday 2022-06-09 05:41:38 by ishitbyabullet

Fallout Alien Content (#539)

* ncr veteran ranger removal

sorry, boys, but 18 yr old female veteran rangers aren't lore accurate.

* NCR no longer has farming or water

No one ever did the sharecropper farm quest in FNV anyways.

* NCR must actively pay taxes

There is a new need meter similar to thirst and hunger for this now.

---
## [freedesktop/NetworkManager](https://github.com/freedesktop/NetworkManager)@[87fe255c89...](https://github.com/freedesktop/NetworkManager/commit/87fe255c891ddad2c32c383c5a203259a0b05342)
#### Thursday 2022-06-09 07:49:26 by Thomas Haller

platform: support IPv6 mulitpath routes and fix cache inconsistency

Add support for IPv6 multipath routes, by treating them as single-hop
routes. Otherwise, we can easily end up with an inconsistent platform
cache.

Background:
-----------

Routes are hard. We have NMPlatform which is a cache of netlink objects.
That means, we have a hash table and we cache objects based on some
identity (nmp_object_id_equal()). So those objects must have some immutable,
indistinguishable properties that determine whether an object is the
same or a different one.

For routes and routing rules, this identifying property is basically a subset
of the attributes (but not all!). That makes it very hard, because tomorrow
kernel could add an attribute that becomes part of the identity, and NetworkManager
wouldn't recognize it, resulting in cache inconsistency by wrongly
thinking two different routes are one and the same. Anyway.

The other point is that we rely on netlink events to maintain the cache.
So when we receive a RTM_NEWROUTE we add the object to the cache, and
delete it upon RTM_DELROUTE. When you do `ip route replace`, kernel
might replace a (different!) route, but only send one RTM_NEWROUTE message.
We handle that by somehow finding the route that was replaced/deleted. It's
ugly. Did I say, that routes are hard?

Also, for IPv4 routes, multipath attributes are just a part of the
routes identity. That is, you add two different routes that only differ
by their multipath list, and then kernel does as you would expect.
NetworkManager does not support IPv4 multihop routes and just ignores
them.
Also, a multipath route can have next hops on different interfaces,
which goes against our current assumption, that an NMPlatformIP4Route
has an interface (or no interface, in case of blackhole routes). That
makes it hard to meaningfully support IPv4 routes. But we probably don't
have to, because we can just pretend that such routes don't exist and
our cache stays consistent (at least, until somebody calls `ip route
replace` *sigh*).

Not so for IPv6. When you add (`ip route append`) an IPv6 route that is
identical to an existing route -- except their multipath attribute -- then it
behaves as if the existing route was modified and the result is the
merged route with more next-hops. Note that in this case kernel will
only send a RTM_NEWROUTE message with the full multipath list. If we
would treat the multipath list as part of the route's identity, this
would be as if kernel deleted one routes and created a different one (the
merged one), but only sending one notification. That's a bit similar to
what happens during `ip route replace`, but it would be nightmare to
find out which route was thereby replaced.
Likewise, when you delete a route, then kernel will "subtract" the
next-hop and sent a RTM_DELROUTE notification only about the next-hop that
was deleted. To handle that, you would have to find the full multihop
route, and replace it with the remainder after the subtraction.

NetworkManager so far ignored IPv6 routes with more than one next-hop, this
means you can start with one single-hop route (that NetworkManger sees
and has in the platform cache). Then you create a similar route (only
differing by the next-hop). Kernel will merge the routes, but not notify
NetworkManager that the single-hop route is not longer a single-hop
route. This can easily cause a cache inconsistency and subtle bugs. For
IPv6 we MUST handle multihop routes.

Kernels behavior makes little sense, if you expect that routes have an
immutable identity and want to get notifications about addition/removal.
We can however make sense by it by pretending that all IPv6 routes are
single-hop! With only the twist that a single RTM_NEWROUTE notification
might notify about multiple routes at the same time. This is what the
patch does.

The Patch
---------

Now one RTM_NEWROUTE message can contain multiple IPv6 routes
(NMPObject). That would mean that nmp_object_new_from_nl() needs to
return a list of objects. But it's not implemented that way. Instead,
we still call nmp_object_new_from_nl(), and the parsing code can
indicate that there is something more, indicating the caller to call
nmp_object_new_from_nl() again in a loop to fetch more objects.

In practice, I think all RTM_DELROUTE messages for IPv6 routes are
single-hop. Still, we implement it to handle also multi-hop messages the
same way.

Note that we just parse the netlink message again from scratch. The alternative
would be to parse the first object once, and then clone the object and
only update the next-hop. That would be more efficient, but probably
harder to understand/implement.

https://bugzilla.redhat.com/show_bug.cgi?id=1837254#c20
(cherry picked from commit dac12a8d6178a6d82fc0913ad8825c8556380ba8)
(cherry picked from commit 698cf1092c39b31e0b2f08de963bc0440a444401)

---
## [LordEclipse/space-station-14](https://github.com/LordEclipse/space-station-14)@[949fbd0194...](https://github.com/LordEclipse/space-station-14/commit/949fbd019404b32fded90f37e3f6a7548790e55e)
#### Thursday 2022-06-09 11:39:10 by Emisse

Bagel Update 13.7 (#8690)

* fuck shit ass shit

* Add files via upload

---
## [Warny181/rep_1](https://github.com/Warny181/rep_1)@[ba2ca51b1c...](https://github.com/Warny181/rep_1/commit/ba2ca51b1c7310a9f9fe58539a7f7bf3a75fd139)
#### Thursday 2022-06-09 13:01:25 by Warny181

Update immtitation content.docx

Классический текст Lorem Ipsum, используемый с XVI века
"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

Абзац 1.10.32 "de Finibus Bonorum et Malorum", написанный Цицероном в 45 году н.э.
"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?"

Английский перевод 1914 года, H. Rackham
"But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know how to pursue pleasure rationally encounter consequences that are extremely painful. Nor again is there anyone who loves or pursues or desires to obtain pain of itself, because it is pain, but because occasionally circumstances occur in which toil and pain can procure him some great pleasure. To take a trivial example, which of us ever undertakes laborious physical exercise, except to obtain some advantage from it? But who has any right to find fault with a man who chooses to enjoy a pleasure that has no annoying consequences, or one who avoids a pain that produces no resultant pleasure?"

Абзац 1.10.33 "de Finibus Bonorum et Malorum", написанный Цицероном в 45 году н.э.
"At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor repellendus. Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae non recusandae. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat."

Английский перевод 1914 года, H. Rackham
"On the other hand, we denounce with righteous indignation and dislike men who are so beguiled and demoralized by the charms of pleasure of the moment, so blinded by desire, that they cannot foresee the pain and trouble that are bound to ensue; and equal blame belongs to those who fail in their duty through weakness of will, which is the same as saying through shrinking from toil and pain. These cases are perfectly simple and easy to distinguish. In a free hour, when our power of choice is untrammelled and when nothing prevents our being able to do what we like best, every pleasure is to be welcomed and every pain avoided. But in certain circumstances and owing to the claims of duty or the obligations of business it will frequently occur that pleasures have to be repudiated and annoyances accepted. The wise man therefore always holds in these matters to this principle of selection: he rejects pleasures to secure other greater pleasures, or else he endures pains to avoid worse pains."

---
## [AquillaF/Skyrat-tg](https://github.com/AquillaF/Skyrat-tg)@[a064b35b25...](https://github.com/AquillaF/Skyrat-tg/commit/a064b35b2571af36cf9d12cea8005843768af36d)
#### Thursday 2022-06-09 14:08:30 by SkyratBot

[MIRROR] Fixes an error sprites on medical wintercoat's allowed list. [MDB IGNORE] (#13566)

* Goodbye stack/medical (#66898)

Okay, why removing instead of giving it a sprite?

Simply put, those items are all small and there is no reason that you need to quick draw a suture/ointment and if you do, the medical belt can carry 7.
Allowed/exoslot items should be either medium/big/bulky sized items (Syringe gun) to make it worth inventory wise or items that you can quickdraw multiple times (Health Analyzer) to make your life easier.
Medical stacks are neither and would just get in the way if you try to quickly put them into a bag/pocket/belt and instead it goes into your exoslot where you would normally want to carry more valuable things like the syringe gun.

This doesn't feel big enough for a fix, spending 5 seconds making a list alphabetical doesn't few worth of code improvement, I will label this as QoL and if someone say it is a balance change I will follow you in game and keep placing shitty small items in your inventory via reverse pickpocketing.

* Fixes an error sprites on medical wintercoat's allowed list.

Co-authored-by: GuillaumePrata <55374212+GuillaumePrata@users.noreply.github.com>

---
## [surge-synthesizer/surge](https://github.com/surge-synthesizer/surge)@[66cfdde3a7...](https://github.com/surge-synthesizer/surge/commit/66cfdde3a74f5d304069709ea4b5a1735abd2994)
#### Thursday 2022-06-09 14:22:27 by Paul

Send Param Automation for Filter Subtypes (#6269)

Paramter Automation messages were not sent because
basically filter subtypes are kinda screwed in how we
implement them both GUI wise and model wise. It's all a hack.
Anyway added an explicit send automation call and now when you
toggle through with clicks you end up getting the DAW showing changes.

My theory is this is the problem in #6264 but will wait for user
confirm before we close it.

---
## [CrayLabs/SmartSim](https://github.com/CrayLabs/SmartSim)@[1e686ead0d...](https://github.com/CrayLabs/SmartSim/commit/1e686ead0d374ab8f41fba7b2d1667e1350e193f)
#### Thursday 2022-06-09 14:58:19 by Ben Albrecht

SmartSim Singularity Integration (#204)

[committed by @ben-albrecht]
[reviewed by @ashao]

This PR adds the ability for SmartSim to launch workloads in Singularity (Apptainer) as described in https://github.com/CrayLabs/SmartSim/issues/101. It also lays the groundwork for supporting other container runtimes such as docker, shifter, and podman in the future, as well as launching the orchestrator in a container.

## Design Variations

During development, it became clear that a few design changes from the original proposal were required. I have documented them below with their rationale:

#### 1. Argument name: `bind_paths` -> `mount`

The terms bind path and mount are mostly used interchangeably across different container runtimes. When writing tests, I kept forgetting if it was `bind_path` or `bind_paths`, which hinted to me that it was not a great arg name, so I swapped it out for the more succinct and easy to remember `mount`.

#### 2. `create_run_settings(..., container: str)` -> `create_run_settings(..., container: Container)`

We originally thought it would be easier for users to get started with containers by allowing them to pass a string into `create_run_settings(container='singularity')` instead of having to create a Container object. While writing tests, I realized that this was potentially very confusing for users because 1) the `container` arg types change between `create_run_settings` and `RunSettings`, and 2) if you need to add other metadata such as container args or container mount paths, you have to switch from using `create_run_settings` to `RunSettings` in your code, which is very annoying. Because creating Containers is so lightweight, I think it is best to keep the container interface consistent across all functions that accept them.

#### 3. dropped getter/setter methods

Because command generation and validation happens upon execution, users can freely modify `Container.args` and `Container.mount` without getter/setter methods to update any other state. Therefore, I dropped these methods from the interface.

## Testing

Added 2 test suites for containers: One for WLM testing and one for local testing. The local testing suite runs in GitHub actions. Due to the added time from building Singularity and pulling the `container-testing` image, the singularity testing only happens on one configuration of the build matrix: python 3.9 + redisai 1.2.5 on linux

---
## [wevek/flow_builder](https://github.com/wevek/flow_builder)@[181b9fac9b...](https://github.com/wevek/flow_builder/commit/181b9fac9bc679754847fbbeba276e0d3b74b3eb)
#### Thursday 2022-06-09 16:50:15 by Vivek Yadav

view content one, spirit of my silence I can hear you... haha back to depressed songs shitt!

---
## [Monkestation/MonkeStation](https://github.com/Monkestation/MonkeStation)@[ada837ddc0...](https://github.com/Monkestation/MonkeStation/commit/ada837ddc0840bb3a6dd1631d8c752a71853366c)
#### Thursday 2022-06-09 17:50:37 by BluBerry016

Exploration PP - Reworks Outpost Nuke Announcement (#450)

* Fuck you, die

* Update nuke_ruin.dm

---
## [gradual-verification/crubit](https://github.com/gradual-verification/crubit)@[9ced4ef05c...](https://github.com/gradual-verification/crubit/commit/9ced4ef05c5cc2a0878e3cbb00202cadd3bfe19b)
#### Thursday 2022-06-09 18:27:11 by Devin Jeanpierre

Generate `operator=` bindings for non-`Unpin` C++ types.

This does *not* implement them for `Unpin` types, because those are harder architecturally, yet simultaneously less interesting: we know we can do it, it's just annoying. (This is because it requires we move to a query-based architecture first -- it's hard, otherwise, to integrate them into e.g. the `Clone` trait, otherwise.)

This also does not yet implement inline thunks, that will wait to a sooner followup.

---

Implementation note: so as to drop the return type, there is a little bit of a hack in here. Please forgive me! Overall, this change has been a net simplification -- unknown commit was also part of this -- so consider this just a wee technical debt.

The long-term solution could be some kind of overlay layer we have not yet designed, but I suspect, instead, the long term solution will be to split this into two functions: one which directly wraps `operator=`, and one which is the trait implementation and discards the return value. This requires (for the same reasons as the `Unpin` impls) a query-based architecturey thingy, and so is not part of this CL.

I could make the trait return the references, but it won't work with full generality. For example, someone can return an int from operator=. So, there's some design work to figure out what to do there, easily dodged by saying "we don't export the return value for now, using this little trick".

At any rate, it's only temporary, probably!

PiperOrigin-RevId: 453743406

---
## [T-J-Teru/binutils-gdb](https://github.com/T-J-Teru/binutils-gdb)@[a1a910608a...](https://github.com/T-J-Teru/binutils-gdb/commit/a1a910608ad10f59e8fd25965a989c2b2a3e9f71)
#### Thursday 2022-06-09 18:37:14 by Andrew Burgess

gdb/testsuite: remove definition of true/false from gdb_compiler_info

Since pretty much forever the get_compiler_info function has included
these lines:

    # Most compilers will evaluate comparisons and other boolean
    # operations to 0 or 1.
    uplevel \#0 { set true 1 }
    uplevel \#0 { set false 0 }

These define global variables true (to 1) and false (to 0).

It seems odd to me that these globals are defined in
get_compiler_info, I guess maybe the original thinking was that if a
compiler had different true/false values then we would detect it there
and define true/false differently.

I don't think we should be bundling this logic into get_compiler_info,
it seems weird to me that in order to use $true/$false a user needs to
first call get_compiler_info.

It would be better I think if each test script that wants these
variables just defined them itself, if in the future we did need
different true/false values based on compiler version then we'd just
do:

  if { [test_compiler_info "some_pattern"] } {
    # Defined true/false one way...
  } else {
    # Defined true/false another way...
  }

But given the current true/false definitions have been in place since
at least 1999, I suspect this will not be needed any time soon.

Given that the definitions of true/false are so simple, right now my
suggestion is just to define them in each test script that wants
them (there's not that many).  If we ever did need more complex logic
then we can always add a function in gdb.exp that sets up these
globals, but that seems overkill for now.

There should be no change in what is tested after this commit.

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[fc91199dfd...](https://github.com/treckstar/yolo-octo-hipster/commit/fc91199dfdf971755cedc971884ab62fd92f3ac9)
#### Thursday 2022-06-09 19:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [Y0SH1M4S73R/tgstation](https://github.com/Y0SH1M4S73R/tgstation)@[92fda5014d...](https://github.com/Y0SH1M4S73R/tgstation/commit/92fda5014dbc8ba64c19848e693c179af35da2ac)
#### Thursday 2022-06-09 20:15:58 by san7890

Makes Hell Microwaves Not Use Power (#67413)

Hey there,

I was informed that the holodeck program Microwave Paradise would draw and suck power out of an APC. Didn't intend for that to happen, and while funny, I don't really want to arm the crew with le epic power sink with very little effort than pressing a button, or warranting this to eventually be locked to "dangerous" programs. So, let's change such that this subtype of microwaves that can not be constructed (only mapped/spawned) doesn't consume any power. I don't know why it drew off the nearest APC or how that works, but this seems to be alright.

It's not possible to deconstruct machinery spawned in at the Holodeck (which I verified while testing this PR), so do not worry about people using this to bypass the power economy for whzhzhzhz purposes.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[7840966c79...](https://github.com/mrakgr/The-Spiral-Language/commit/7840966c794162098019be942c362a12d4e2d788)
#### Thursday 2022-06-09 20:35:50 by Marko Grdinić

"10:05am. I am up. Let me chill just a bit and then I will start. I realized I did not finish the 3d vid from yesterday so let me get on with that.

10:20am. Did some /wip/ posting.

///

Yesterday I did some research on 3d inverse rendering. There was that video being doom posted on NNs taking images and spitting out 3d models along with the textures and lighting, but I've asked the author and they tend to use >50 shots from various angles when doing inference. With just 1 he said I'd see bad geometry as soon as I moved the camera. It is too bad, but it seems inverse rendering is only a game changer for people doing photogrammetry. Not me, in other words.

NNs are good at speeding up simulations, so in the not so distant future, we will get orders of magnitude faster renderers and simulators, probably when AI chips start getting en-volume. But for now I'll be satisfied with just style transfer. It will be a huge time saver all on its own.

///

https://youtu.be/eCDBA_SbxCE?t=937

Let me resume the video from here. I'll get it out of the way.

https://youtu.be/eCDBA_SbxCE?t=1568
> Single view mesh reconstruction.

Actually I did finish this yesterday, but it faded so strongly from my memory that i thought I did not.

https://youtu.be/r9lvAyAgR3E
Single-View 3D Mesh Reconstruction and Generation

https://youtu.be/r9lvAyAgR3E?t=54

Yeah, exactly what I want.

10:40am. Enough of this. It is a waste of time. Basically they have nothing good yet. I need to get started for the day. One illustration a day, and I'll be a good artist in no time at all.

https://youtu.be/JiLsYx28S24
How to Scatter Objects in Blender (Preinstalled Add-On)

How does this official addon work?

10:55am. I'll just use geo nodes. Nevermind it for now.

This bring me back to programming. Whenever starting a new thing I had to overcome strong intertia. Yesterday I got Blender 3.2, and I guess I'll move on to it.

11am. It was not perfect, but I completed a single project from start to finish. I am a real artist now. Let me back up the trained neural net by the author and the CAST repo on Google Drive. I do not want the author to change his mind later.

11:05am. Got the backup done. I'd have forked the project if the the NNs were on the repo instead of the authors Google Drive folder.

It would be a huge loss if I started work on Heaven's Key and lost access to the repo and the pretrained net. This way the odds of it happening are 0.

11:10am. Now I just need to focus on it.

Yeah, at this point some things, like that Zbrush hard modeling course are unfinished. There are more things I could study. But it does not really matter. The base I've established is enough.

3d offers a lot, as I've said. It actually a huge pain in the ass to do shading by hand for example. It is hard to do perspective. It is very challenging to rotate a character and have it look the same. A lot of what would require extreme artistic talent is essentially fully automated in 3d.

It only weakness was the somewhat dull CG look, but that is a thing of the past because of style transfer!

11:15am. I've learned quite a lot in the past 8 months. That is how long I've been doing art for. It is just a drop in the bucket compared to how long I've been doing programming, but it is not insignificant by any means. I do not require any more training. If I have any gaps in my skillset, I'll fill them as I go along without much trouble. I can easily build up my sculpting skills should I need to.

11:30am. I am rolling things in my mind and I already feel like I have a lot.

...I am thinking. Just like with programming it is so tedious to start work on something new. I feel like spending the day in bed, just thinkign about the scene and building up hype for it. A brainstorming session if you will.

When it is done, and the intro screen as well, I think I will reward myself with finishing that Zbrush HS sculpting course. I'll shore up my modeling skills all the way to the limit.

11:55am. Sigh, I really like how the room v4 in the style of great wave came out. You really can't tell that these style transfered images are 3d at all.

A scene like this would not have taken long at all, had I been more skilled in determining the amount of detail to put in. It is really a great lesson.

Right now I what I am thinking of are uber artists like Murata Yuusuke. There is no reason why I should not be able to match their quality. I'd never be good enough to do it with a pen, but why should I not do it with 3d? There is no reason at all.

Ideally I'd want a bit more control over style transfer. More of a cell shaded and less of a raw painterly look, but that is merely due to what the net was trained on. Once the training code gets released there will be nothing stopping me from training on illustrator's like Fuzichoco. I have a huge amount of saved anime images on my hard drive that can serve as dataset.

12:05pm. i do not think I have what it takes to reach 5/5 in art or even 3d as a generalist, but as a pure illustrator it might just be doable due to things like style transfer. Style transfer will be such a huge time saver that it will allow me to punch a domain higher than I should be.

These tools are really powerful, and I understand that the vast majority of artists do not see how to use them to their full potential.

Most artists I'd bet do not like the plastic 3d look and so gravitate towards 2d. Some of them even see using 3d as cheating and are pursuing the ideal of pure skill without the use of technicals.

12:05pm. DALLE 2 is rank 6 as an artist. What it can do, the Inspired will be able to do much better. Murata might be good, but he can't match the raw power of the machines.

It is a waste of time to try to lift with one's own power. For humans, the machines are one true path to power.

12:45pm. Covers, music, Zbrush course, covers, music, Zbrush course, covers, music, Zbrush course...

I need to establish those 3 goals firmly in my mind. It is time to start thinking seriously about studying music. There is no reason why I can't study sculpting on the side either.

Let me have breakfast here. I will spend today and even tomorrow if necessary in bed.

1:20pm. Done with breakfast.

https://huggingface.co/blog/annotated-diffusion
> Note that this list only includes important works until the time of writing, which is June 7th, 2022.

This is a really good article, it has code on how to implement these models. Diffusion models are something new to me.

> Diffusion Models Beat GANs on Image Synthesis (Dhariwal et al., 2021)

So GANs are no longer king. It might be possible to improve style transfer using these models. Since this article is this good, I'll look if there are any on style transfer.

> For now, it seems that the main (perhaps only) disadvantage of diffusion models is that they require multiple forward passes to generate an image (which is not the case for generative models like GANs). However, there's research going on that enables high-fidelity generation in as few as 10 denoising steps.

https://youtu.be/xkWgwxKxWAE
How Deep Dreams (Basically) Work

Let me refresh my memory of this a little.

https://youtu.be/xkWgwxKxWAE?t=239

I see where this is going. With deep dream you just pick a cateegory and optimize the input so it gets closer to it, right? I simply forgot what kind of objective causes the net to put nightmarish dog faces everywhere.

https://youtu.be/XCUlnHP1TNM
MIT 6.S192 - Lecture 22: Diffusion Probabilistic Models, Jascha Sohl-Dickstein

Let me watch this. It is that kind of day for me.

https://www.youtube.com/channel/UCx9CcRnc1lBQJnliK0MiEbQ
MIT 6.S192: Deep Learning for Art, Aesthetics, and Creativity

This is interesting. There is even a lecture on easy 3d content creation using something called neural fields. I am not familiar with that.

1:45pm. I couldn't find anything on style transfer on HuggingFace, but I am interested in giving some of these lectures a try.

https://youtu.be/XCUlnHP1TNM?t=313

Using rough sketches to get high quality images.

///

>>902358
https://www.youtube.com/channel/UCx9CcRnc1lBQJnliK0MiEbQ
MIT 6.S192: Deep Learning for Art, Aesthetics, and Creativity

It has been almost a year and I am already behind on ML. Diffusion models came out of the blue for me, it seems they beat GANs on image generation. Since CAST uses GAN training, I wonder if could be improved using diffusion models. My guess is probably yes, but I don't know how yet.

///

No, I won't post this in the wip thread. Not unless I have something interesting related to 3d.

https://youtu.be/XCUlnHP1TNM?t=396

Focus me. This is an interesting lecture.

https://youtu.be/XCUlnHP1TNM?t=674

Had to do chores. At the above point in the video a dog barks loudly into the mic. It have my quite a start.

2:20pm. https://youtu.be/XCUlnHP1TNM?t=1141

Hmmm, it is one thing to learn the mean function, but covariance for this kind of dimensionality?

https://youtu.be/XCUlnHP1TNM?t=1640

I've put so much effort into studying this, remember when I was playing with the Dirichet distribution. Now that has all faded from my memory.

https://youtu.be/XCUlnHP1TNM?t=2435

I am not sure how much of this I am following. Why is optimizing an ODE necessary if he has the reversal steps. I am not really paying too careful attention.

https://youtu.be/XCUlnHP1TNM?t=2901

If I want style transfer, then this should be the way to do it...

https://youtu.be/XCUlnHP1TNM?t=2949

I need to pause on this. At first he talked about prob models, and then the talk moved to SDEs. I am guessing he is just applying this equation to reverse the model.

Hmmm, since it requires gradients, it would not be that easy to implement efficiently.

https://developer.nvidia.com/blog/improving-diffusion-models-as-an-alternative-to-gans-part-1/

This graph here says as much. I'd just like to understand how style transfer could be done straightforwardly. Instance normalization would not work on things other than images. If I do not resort to such tricks how would it work then?

This is a good article. Let me read it and then I will get back to the video.

https://developer.nvidia.com/blog/improving-diffusion-models-as-an-alternative-to-gans-part-2/
> Denoising diffusion GANs

They even came up with that?

> We observe that our model exhibits better training stability and mode coverage. In image generation, we observe that our model achieves sample quality and mode coverage competitive with diffusion models while requiring only as few as two denoising steps. It achieves up to 2,000x speed-up in sampling compared to regular diffusion models. We also find that our model significantly outperforms state-of-the-art traditional GANs in sample diversity, while being competitive in sample fidelity.

I suppose this is one way of training GANs. I guess I do not need the duality gap method after all.

> We anticipate that they will likely find practical use in areas such as image and video processing, 3D content generation and digital artistry, and speech and language modeling.

3d content generation.

https://nvlabs.github.io/denoising-diffusion-gan/

Great PR. This is a really good idea for how to combine the benefits of both approaches.

Let me get back to the diffusion model lecture. The diffusion GANs would likely be easier to implement than the competing methods as well.

https://youtu.be/XCUlnHP1TNM?t=3055

He says that unlike with GANs it is possible to train a little classifier to guide the image generation.

https://youtu.be/XCUlnHP1TNM?t=3055

This second term I could use for style transfer, no doubt.

https://youtu.be/XCUlnHP1TNM?t=3171

It can do colorization.

https://youtu.be/XCUlnHP1TNM?t=3192

Output of a clip classifier as the guiding signal...yeah, that is quite relevant to style transfer. Ultimately, that output would be just some vector - the same thing as what I'd imagine a style descriptor would be.

Could diffusion GANs do this?

https://youtu.be/XCUlnHP1TNM?t=3280

What is unique identifiable encoding?

But at any rate, if I could manipulate the latent codes of diffusion GANs, I could do pretty much anything with them art wise. I could get to DALLE level simply by pouring more money into it.

Even though it has 5b parameters that does not mean much on its own. Depth by itself would not require more memory during the feedforward pass. Only the channel size really matters.

https://youtu.be/XCUlnHP1TNM?t=3320

I absolutely have to find out if diffusion GANs have controllable generation. It would make a huge difference to their usefulness.

I am not sure. Maybe I'll just ask the author if I don't figure it out from the paper itself.

Hmmm, what is that vector `z` that the generator takes in?

> Removing latent variables z converts our denoising model to a unimodal distribution.

What are these latent variables?

> Stroke-based image synthesis: Recently, Meng et al. (2021b) propose an interesting application of diffusion models to stroke-based generation. Specifically, they perturb a stroke painting by the forward diffusion process, and denoise it with a diffusion model. The method is particularly promising because it only requires training an unconditional generative model on the target dataset and does not require training images paired with stroke paintings like GAN-based methods (Sangkloy et al., 2017; Park et al., 2019).

I'll check this out later.

https://github.com/NVlabs/denoising-diffusion-gan/issues/

Opened issue 9 here.

4:30pm. Let me take a look at the neural fields talk.

https://ali-design.github.io/deepcreativity/

https://youtu.be/31RibsF5-h4
MIT 6.S192 - Lecture 19: Easy 3D content creation with consistent neural fields, Ajay Jain

This guy really has a background similar to mine - compilers and so on.

4:35pm. While I got an answer to my previous question right off, the bat, this repo is pretty barren, so who knows if I'll get an answer. I might have better luck just asking on the ML sub. I'll do that if I do not get an answer by tomorrow.

https://youtu.be/31RibsF5-h4?t=491
> Encoding a scene in NN weights.

https://youtu.be/31RibsF5-h4?t=557
> Rendering is done by raytracing, this is not exactly what would be done in most graphics applications, like a real time raytracing because we've kind of encoded the light being reflected at any given point backs towards the viewer into this function. So we don't have to scatter light through the scene.

Amazing. This could lead to huge speedups in rendering time.

https://youtu.be/31RibsF5-h4?t=793

Had to do some chores. This part where he mentions he is using transformer style positional encoding for vertices is interesting.

https://youtu.be/31RibsF5-h4?t=983
> NERFs are data hungry.

Let me pause here to note something down. I forgot where I saw it, but having a diffisuion net get an image of flats and convert that to realistic scenes is really impressive. I could use this to add details to my own work even if I have no intention of generating a scene from scratch.

My principle, and why I am looking into this, is that I should put myself into a position where I can improve my art abilities simply by getting bigger GPUs. That would make the art journey a cultivator's one. The doomposters do not get art at all. They are painting it like a war between man and machines, and it absolutely does not have to be that way.

5:25pm. No, I need to ask on the ML sub. I doubt the author cares at all about the repo.

https://www.reddit.com/r/MachineLearning/comments/v8jgo9/d_can_the_diffusion_gans_generation_be_controlled/

I've asked here. I'll be sure to get an answer on the ML sub. Let me move on.

6pm. https://youtu.be/31RibsF5-h4?t=2309
> So it is kind of in the realm where you as an artist could afford to do this.

6:05pm. https://youtu.be/31RibsF5-h4?t=2362

This is called dream fields. I should leave it aside.

When it comes to ML, I am like a drug addict. Most likely diffusion GANs cannot be controlled like actual diffusion models. The way diffusion models work is not that much different from style transfer itself.

6:35pm. https://www.reddit.com/r/MachineLearning/comments/v8jgo9/d_can_the_diffusion_gans_generation_be_controlled/

I actually got downvoted for this and got no answer. The ML sub has really gone to hell. It is no wonder given the 2.5m subscribers count. I has been a long time since 2015 when the big names in ML came by to do the AMAs.

Let me finish watching the video and I will close for the day.

6:45pm. Had to take a short break. In the past, I'd indeed get an answer, but once the sub becomes big and popular it gets dominated by tourists. I happened to /r/futurology as well.

I should post my question where people actually doing ML gather. The obvious place would be the PyTorch forums.

Sigh, I'll never forgive the ML sub. This is the last time I'll ever post there.

6:45pm. With the PyTorch forums I'll get 100x less views, but 100x more quality per view.

https://discuss.pytorch.org/t/can-the-diffusion-gans-generation-be-controlled/153777

Here it is. I am aware that the answer that it can't is highly likely. I mean if it could, I doubt the chinaman would have spent his time working on CAST. Still it is worth a try. I want to see what I'll get. I mean think about it, just generating images on its own is not that useful. What makes DALLE amazing is that you can tell it what to make. If diffusion GANs could operate in that regime, I could get a lot of utility out of them. If they answer turns out to be yes, I'll still leave them aside, but once I get some resources I'll definitely be putting them to use. DALLE 2 showed amazing capabilities for really immitating styles.

CAST on the other hand while useful, can only give me render a painterly look. It does not have particular stroke variety even though it looks good.

Let me finish the 3d lecture vid. It is the same old thing for me.

7:25pm. Ok, enough. Let me close here for the day. I am starting to get called schizo autist in the /wip/ thread which is probably my que to stop posting there. I would just look retarded if I continued. The /wip/ thread is not my sandbox. This journal is.

As for diffiusion GANs, it does not matter if they are controllable. If they aren't no doubt a year or two from now somebody will come up with a model that is. If I tried doing that now that would just mean months of my life going down the toilet. I've already been through that enough for the past 5 years.

What I need to focus here is....covers, music, Zbrush course. Yes.

ML really brings out a spirit of longing in me. I should be been brainstorming the cover. Let somebody else come up with a model that I can use instead of the DALLE hypefest and I will make it my foundation. They can spend their time and money doing this. The Singularity is not going to run away from me if I am not spending my every moment bashing my head against ML models.

///

>>902433
>If you find value in modelling props that will not appear then you should consider painting it by hand if learning is your goal. Why waste time when you can waste some more.
Because when painting or drawing, I'd have to deal with perspective and shading myself, while in 3d, the program does that all on its own. It is hard and requires talent to do well in addition to requiring large amounts of practice that I honestly don't feel like doing. Throughout my life there was no indication that I had any talent in 2d art, unlike in programming for example. 3d offers a lot over 2d to those who bother to master the tools. I got into it because of sculpting which I found easier than drawing because I could refine endlessly and just focus on form rather than numerous other aspects that drawing requires, but 3d software happens to perfectly automate.

As a matter of principle, I intend to position myself so that as much as possible the improvement in the quality of my art come from better computer hardware and algorithms rather than my own practice because in addition to 3d, I'll have to do writing, music, programming and who knows what else to meet my goals. If I had a machine that could read my brain waves and turn that into digital paintings, you bet I would not be bothering with 3d either. I might have time to do a few projects from start to finish in 3d, even if it takes me months, and in fact that has happened, but I do not have the time to approach it like a dedicated artist would. I'll do the covers for my VN and then move on to music next as well finish that Zbrush course.

I think I am good now as far as my 3d skills go now, but I am getting hung up on ML again. When it comes to it I am like a crack addict.

https://ali-design.github.io/deepcreativity/

Instead of me suffering over it alone, why not join me? Right now I am dying to know if diffusion GANs have controllable generation (think DALLE) like vanilla diffusion models, but I know that if I start doing research that would be months of time going down the drain. It doesn't really matter, because even if it can't, somebody in the future is going to come up with a model that can.

///

8:10pm. Yeah, if diffusion GANs could have fine control, then the paper would advertize that. It is interesting to contrast their training with CAST. CAST might be doing adversarial training, but it doesn't do like a regular GAN. The generator maps the late...

No wait, I need to think of the generator as a composite encoder decoder. Why was I so obsessed with just training the decoder using GAN training.

If it is just the generator, I could train a diffusion CycleGAN together with AdaIn and this would do the style transfer. Find a way to fit Barlow Twins into the encoder and I will have an improved CAST scheme. If I had to reimplement it all on my own that is how I would do it. I could bring the latest improvements in GANs and contrastive learning into CAST.

But that is ignoring that latent vector.

Right now I am thinking about it from another angle. Do I understand how diffusion models could be trained? CLIP is just a discriminator that maps text to images, but it cannot generate the image on its own.

It can only act as a source of supervisory signal.

Even though I only understand diffusion models by 10-20% right now, this is something I can be absolutely sure.

8:20pm. I need to focus on this single belief - if I have a discriminator, then it should be possible to bias any kind of generator towards giving me what I want.

https://openai.com/blog/clip/

Yeah, I can treat it as a discriminator. It has just been pretrained using contrastive learning.

8:25pm. Come to think of it, that is what humans are doing with ML. I never really thought of DALLE as being a step forward in the field of meta learning, but that is how it is.

8:30pm. I see. I think I understand. A decade ago it was stacking RBMs, but now unsupervised learning is all the rage again.

8:35pm. There is no need to get hung up on specific models. Having a generator and then using a discriminator to bias it is a powerful idea. There will be all sorts of methods. Once I get the resources, I'll find my way back to ML. There is no need to be anxious about a particular way of doing it.

In the future I'll have some GAN, and I'll use a discriminator to pass it a message telling it to make the image like Fuzichoco did it.

8:40pm. Let me not worry about this. Tomorrow I should get started on the scene.

8:45pm. Latent vector...remember that paper from Numenta and how their architectural change was the use of context? Indeed, I do not even have to have a specific discriminator. The discriminator does not even have to be particularly good. I can train it on Danboru images, and extract the latent vector from the last layer of the discriminator. At least that is what I'd do with FF nets.

For image style transfer...

No I can't actually think of a way to do the conditioning on a latent vector in a way other than how AdaIn does it.

I can't really make the latent vector a part of the input. I suppose I could try projecting it...

The issue with how Numenta does it is that if I applied it to a CNN I'd have to zero out entire channels.

This actually would not be a thing if the hardware supported sparsity, but it does not! No hardware can make proper use of it today. If it did, I bet this method would be a superior do the kind of instance normalization AdaIn does.

8:55pm. How could regular diffusion models be conditioned? I actually can't think of a way either. If I knew I bet that would give me inspiration.

The best way to learn this would be to study the Hugginface post. Do I want to spend a few days doing that? As fired up as I am right now...

https://huggingface.co/blog/annotated-diffusion

9:05pm. Right now I am reading the above post obsessively, but as far as I can see half of it is building up the architecture used for diffusion model. I thought they would just import an existing model, but they are bulding an UNet from the ground up.

9:30pm.

```py
@torch.no_grad()
def p_sample(model, x, t, t_index):
    betas_t = extract(betas, t, x.shape)
    sqrt_one_minus_alphas_cumprod_t = extract(
        sqrt_one_minus_alphas_cumprod, t, x.shape
    )
    sqrt_recip_alphas_t = extract(sqrt_recip_alphas, t, x.shape)

    # Equation 11 in the paper
    # Use our model (noise predictor) to predict the mean
    model_mean = sqrt_recip_alphas_t * (
        x - betas_t * model(x, t) / sqrt_one_minus_alphas_cumprod_t
    )

    if t_index == 0:
        return model_mean
    else:
        posterior_variance_t = extract(posterior_variance, t, x.shape)
        noise = torch.randn_like(x)
        # Algorithm 2 line 4:
        return model_mean + torch.sqrt(posterior_variance_t) * noise

# Algorithm 2 (including returning all images)
@torch.no_grad()
def p_sample_loop(model, shape):
    device = next(model.parameters()).device

    b = shape[0]
    # start from pure noise (for each example in the batch)
    img = torch.randn(shape, device=device)
    imgs = []

    for i in tqdm(reversed(range(0, timesteps)), desc='sampling loop time step', total=timesteps):
        img = p_sample(model, img, torch.full((b,), i, device=device, dtype=torch.long), i)
        imgs.append(img.cpu().numpy())
    return imgs

@torch.no_grad()
def sample(model, image_size, batch_size=16, channels=3):
    return p_sample_loop(model, shape=(batch_size, channels, image_size, image_size))
```

No, I was wrong. Given how the functions are wrapped in `no_grad` clauses, the case must be that the model does not require gradients.

9:35pm. I think I understand it. The U-Net is trained to predict every step of the noise process of which there are several. That allows it to be run in forward mode after it has been trained for the sake of denoising an image. I thought it required gradients in order to modify the inputs, but that is not it.

Damn.

Now that I understand this, I guess real question is how can the net be conditioned using something like Clip?

https://openreview.net/forum?id=PxTIG12RRHS&noteId=HXMvdd3nIOo
Score-Based Generative Modeling through Stochastic Differential Equations

He released an implementation here.

///

Comment:
Our code and checkpoints are released at GitHub:

JAX + FLAX codebase (recommended): https://github.com/yang-song/score_sde
PyTorch codebase: https://github.com/yang-song/score_sde_pytorch
We additionally provide several colab notebooks to help people use our codebase and understand the basic ideas of this paper:

JAX + FLAX: Load our pretrained checkpoints and play with sampling, likelihood computation, and controllable synthesis. link

PyTorch: Load our pretrained checkpoints and play with sampling, likelihood computation, and controllable synthesis. link

Tutorial of score-based generative models in JAX + FLAX. link

Tutorial of score-based generative models in PyTorch. link

///

https://colab.research.google.com/drive/120kYYBOVa1i0TD85RjlEkFjaWDxSFUx3?usp=sharing#scrollTo=XCR6m0HjWGVV

Here is the PyTorch tutorial.

> In fact, any neural network that maps an input vector  x∈Rd  to an output vector  y∈Rd  can be used as a score-based model, as long as the output and input have the same dimensionality. This yields huge flexibility in choosing model architectures.

10pm. My god, what a complicated tutorial!

https://github.com/heejkoo/Awesome-Diffusion-Models#text-to-image

A lot of stuff here.

https://github.com/omriav/blended-latent-diffusion

Has a repo, but no code yet.

https://github.com/microsoft/VQ-Diffusion

This has code.

https://github.com/omriav/blended-diffusion

Has code.

10:15pm. Either that site is out of data, or most papers really don't come with code attached.

Do I really want to dive into this right now?

10:25pm. I've taken a look, but compared to the succinct Huggingface article, the blended diffusion repo is just too complicated if all I want to do is figure out how conditioning works.

https://www.reddit.com/r/MachineLearning/comments/v89ynl/comment/ibrqip1/?utm_source=share&utm_medium=web2x&context=3

Maybe I'll get a reply here. If not, that is fine. No way am I digging through these complicated repos just to figure out one simple thing.

10:30pm. Then it is decided. Tomorrow I am going to try to icebreak the work on the cover.

If I have anxieties I should pour them into the art. Pouring them into NNs is not constructive. I had plenty of years to learn that. It is just very difficult to reason anything out in NN land. Those math equations are really explanations, but more like sketched and...excuses.

I'll give it a few years for them to figure it out."

---
## [cmitu/duckstation](https://github.com/cmitu/duckstation)@[f9212363d3...](https://github.com/cmitu/duckstation/commit/f9212363d3370efcdb97d4f7de010b5f17bd5c5e)
#### Thursday 2022-06-09 20:44:10 by IlDucci

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
## [Maetrim/DDOBuilder](https://github.com/Maetrim/DDOBuilder)@[af7f88a9de...](https://github.com/Maetrim/DDOBuilder/commit/af7f88a9ded0040ba80b69cc0407206187582ed7)
#### Thursday 2022-06-09 21:23:09 by Maetrim

Build 1.0.0.164

Fix "Tainted Scholar: Enervating Shadow" now correctly states it scales at 130% spell power, not 150 (Reported by Question2)
Fix: "Bombardier: Conjuration Focus" now correctly costs 2ap (Reported by iplaywithdrums)
Fix: Item "Belt of Crystalline Vanity" now has its correct name (Reported by Texturace)
Fix: "Magus of the Eclipse: Chill Aura" now correctly costs 2ap and description dice updated (Reported by Khalibano)
Fix: "Draconic Incarnation: Dragon Breath" options no longer list Enlarge as a metamagic that works on them (Reported by Question2)
Fix: Feat "Epic Arcane Eldritch Blast" renamed to "Epic Pact Dice". Older files will automtically convert on load (Reported by Question2)
Fix: "Ultimate Fury" strength set bonus is now correct at +1 per extra Filigree, not +2 and no longer requires Rage to be active (Reported by ShinuzukaRakam)
Fix: "Tiefling Scoundrel: Staccato Sovereign" now correctly costs 2ap (Reported by Orcao)
Fix: "Hellball" damage numbers fixed from 10d6 to 3d20 + 15 (Reported by Question2)
Fix: Forum export will now display all names correctly for enhancement tree items and the correct number of trained ranks (Reported by iplaywithdrums)
Fix: Enhancement "Knight of the Chalice: Improved Turning" description updated (Reported by Cromfrein)
Fix: Enhancement "Shintao: Violence Begets Violence" description updated (Reported by Cromfrein)
Fix: Reaper augments updated to match https://ddowiki.com/page/Reaper_bonus and some renamed (Reported by pevergreen)
Fix: Item "The Heart of Suulomades" now correctly lists curse immunity, not charm immunity (Reported by pevergreen)
Fix: Typo in "Tabaxi: Deep Scratches" fixed (Reported by Laur)
Fix: Augment "Sapphire of Armored Agility" will now also affect max dex bonus for tower shields. Description also updated (Reported in a Strimtom build review)
New: The inventory view will now show augment slots and states under each item.
---Augments are filled with their augment color where appropriate
---Augment border is black when an augment is selected, white if no augment selection
---None standard augments (such as greensteel/slavelords) are shown with a grey interior colour
---Reaper and Mythic augment slots are suppressed in this view as all items can have these
---How to Guide updated
Fix: The Precision +5% Attack bonus will now correctly apply when Precision is active
Fix: Typo in "Exalted Angel: Blessed Water" fixed (Reported by Gregen in a DDO thread https://forums.ddo.com/forums/showthread.php/532253-Typo-Megathread#post6520576)

U55 Lamannia Changes:
---New Feat: Legendary Aim
---Fix: Legendary Toughness now has its minimum 21 Constitution requirement
---"Shadowdancer: Cut to the Soul" Tier 4 core updated
---"Grandmaster of Flowers" Tier 4 core, renamed and now a multiselector
---"Fatesinger: Hear my Voice friend" Tier 4 core description updated
---"Exalted Angel" Tier 4 core, renamed and now a multiselector
---"Primal Avatar" Tier 4 core, renamed and description updated

---
## [Python-Repository-Hub/scipy](https://github.com/Python-Repository-Hub/scipy)@[c73e088350...](https://github.com/Python-Repository-Hub/scipy/commit/c73e0883501a21cfaf7220a8118a6155857b5829)
#### Thursday 2022-06-09 21:24:47 by Tyler Reddy

MAINT: add `SCIPY_USE_PROPACK` env variable (#16361)

* this is effectively a forward port and modernization
of the release branch `PROPACK` shims that were added in
gh-15432; in short, `PROPACK` + Windows + some linalg backends
was causing all sorts of trouble, and this has never been resolved

* I've switched to `SCIPY_USE_PROPACK` instead of `USE_PROPACK`
for the opt-in, since this was requested, though the change
between release branches may cause a little confusion (another
release note adjustment to add maybe)

* I think the issues are painful to reproduce; for my part,
I did the following just to check the proper skipping/accounting
of tests:

- `SCIPY_USE_PROPACK=1 python dev.py -j 20 -t scipy/sparse/linalg`
  - `932 passed, 172 skipped, 8 xfailed in 115.57s (0:01:55)`
- `python dev.py -j 20 -t scipy/sparse/linalg`
  - `787 passed, 317 skipped, 8 xfailed in 114.80s (0:01:54)`

* why am I doing this now? well, to be frank the process of manually
backporting this for each release is error-prone, and may cause
additional confusion/debate, which I'd like to avoid. Besides, if it
is broken in `main` we may as well have the shims there as well. I would
point out that you may want to add `SCIPY_USE_PROPACK` to 1 or 2 jobs
in CI? The other reason is that if usage of `PROPACK` spreads, I don't
want to be manually applying more skips/shims on each release (which
I already had to do here with two new tests it seems)

---
## [rmw/dotfiles](https://github.com/rmw/dotfiles)@[ace0f5a6d0...](https://github.com/rmw/dotfiles/commit/ace0f5a6d0fbe9b6abbabd335c9984cab53edac8)
#### Thursday 2022-06-09 23:07:07 by Rebecca Miller-Webster

thfuck, readme + git

* updated readme with permissions for install.sh because I suck at
remembering what the numbers in chmod mean
* install thefuck because typos
* add oskeychain to git credentials helper

---

