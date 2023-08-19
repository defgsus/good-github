## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-08-18](docs/good-messages/2023/2023-08-18.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,238,253 were push events containing 3,308,881 commit messages that amount to 237,991,648 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 69 messages:


## [realforest2001/forest-cm13](https://github.com/realforest2001/forest-cm13)@[f3fc60ed65...](https://github.com/realforest2001/forest-cm13/commit/f3fc60ed655d27bb3f012d0e0d834c64990b173d)
#### Friday 2023-08-18 00:05:12 by morrowwolf

Attachment nerfs and removals (#4122)

# About the pull request

This PR:

Removes the barrel charger from vendors

Removes all benefits other than wield delay mod from the angled grip

Adds wield delay to the extended barrel

# Explain why it's good for the game

Barrel charger is a straight damage increase and rather silly to work
around given how burst works bypassing real fire rate concerns. If you
know, you know. Horrible idea, I am amazed it's been around this long.

Angled grip had zero downside. Now it still has zero downside but isn't
also a ton of accuracy buffs on top of the god-tier lower wield delay.

Extended barrel had zero downside. Now it has a downside.

# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog

:cl: Morrow
balance: Removed the barrel charger from vendors
balance: Removed all benefits other than wield delay mod from the angled
grip
balance: Added wield delay to extended barrel
/:cl:

---
## [lpeapnni/Skyrat-tg](https://github.com/lpeapnni/Skyrat-tg)@[34306b4266...](https://github.com/lpeapnni/Skyrat-tg/commit/34306b4266e0cc8219d0bb9ca809350ec4035d3f)
#### Friday 2023-08-18 00:07:48 by SkyratBot

[MIRROR] Buffs Heretic ash ascension [MDB IGNORE] (#23114)

* Buffs Heretic ash ascension (#77618)

## About The Pull Request

Post-Ascension the Nightwatchers Rebirth (Or Fiery Rebirth) has its
cooldown lowered from 60 seconds to 10
Additionally adds bomb immunity to the list of resistances that
ascension provides

## Why It's Good For The Game

Ash ascension kind of sucks when compared to its big brothers flesh,
rust and blade. You do get a couple of cool spells but their impact is
negated by how shitty fire damage is and while you get a ton of
resistances, you don't get stun immunity and have absolutely zero
sustainability in long-term engagements.

Blade has its lifesteal, rust has its leeching walk and flesh has a big
worm that eats arms. And while the laziest solution would be to give ash
stun immunity like those three I think it'd be more fitting if it could
capitalize on one of its more powerful spells. Keeping in the fight by
siphoning health from all those people you lit on fire with your cascade
instead of watching in pain as they completely negate any threat you
have with a fire extinguisher and temp adapt.

* Buffs Heretic ash ascension

---------

Co-authored-by: DaydreamIQ <62606051+DaydreamIQ@users.noreply.github.com>

---
## [realforest2001/forest-cm13](https://github.com/realforest2001/forest-cm13)@[f5784dabc7...](https://github.com/realforest2001/forest-cm13/commit/f5784dabc77752802da20f2d14787667161d61ac)
#### Friday 2023-08-18 00:09:02 by ihatethisengine

More portable cades tweaks and buffs (#3967)

# About the pull request

Despite making a lot of tweaks and changes to portable cades I barely
touched them in the game until recently. Now I have more experience and
can tweak it again.

1) You can now stack damaged cades and stack stores health of each cade.
You can repair stacked cades but it will take longer time.

2) Miniengi pamphlet allows faster repairs but only when cade is folded.

3) You can quickly collapse portable cades with crowbar if you have at
least miniengi skills.

4) You no longer need to have folded portable cade in hand in order to
repair it, but if you do, you can move while repairing.

# Explain why it's good for the game

1) It's extremely annoying to repair each individual cade in order to
stack them just because it got hit by a stray bullet once. Now you can
just ignore damage and keep going.

2) Yeah it took 10 second for PFC to repair each single cade. Really
long. Now it's 5 seconds, but only when folded and if you have miniengi
skills. Makes miniengi pamphlet a bit more relevant.

3) It was intended, but turned out it was a bit inconvenient. It was
faster to collapse by hand because you didn't need to deal with tools.
Now it requires just a crowbar and slightly faster. Also requires
miniengi skill to use crowbar.

4) First was just a bit annoying, second allows more mobility which is
the point of portable barricades.


# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl: ihatethisengine
balance: you can stack scratched portable cades if their HP at least
75%. Doing so will reduce the health of all barricades in the stack to
the level of the most damaged.
balance: you can repair stacked portable cades but it will take longer
time depending on how many cades in stack.
balance: miniengi skill makes repairs of folded portable cades faster
(10 seconds to 5 seconds, same as engineer).
balance: with engineering skill at least of miniengi you can collapse
deployed portable barricade with a crowbar (wrench is no longer
required, slightly faster (2 sec to 1.5 sec)).
balance: you no longer need to have folded portable cade in hand in
order to repair it.
balance: if you have folded portable cade in hand, you can move while
repairing it.
/:cl:

---------

Co-authored-by: ihatethisengine <treml.treml@yandex.ru>

---
## [Milan-960/react](https://github.com/Milan-960/react)@[ac1a16c67e...](https://github.com/Milan-960/react/commit/ac1a16c67e268fcb2c52e91717cbc918c7c24446)
#### Friday 2023-08-18 00:14:58 by Sebastian Markbåge

Add Postpone API (#27238)

This adds an experimental `unstable_postpone(reason)` API.

Currently we don't have a way to model effectively an Infinite Promise.
I.e. something that suspends but never resolves. The reason this is
useful is because you might have something else that unblocks it later.
E.g. by updating in place later, or by client rendering.

On the client this works to model as an Infinite Promise (in fact,
that's what this implementation does). However, in Fizz and Flight that
doesn't work because the stream needs to end at some point. We don't
have any way of knowing that we're suspended on infinite promises. It's
not enough to tag the promises because you could await those and thus
creating new promises. The only way we really have to signal this
through a series of indirections like async functions, is by throwing.
It's not 100% safe because these values can be caught but it's the best
we can do.

Effectively `postpone(reason)` behaves like a built-in [Catch
Boundary](https://github.com/facebook/react/pull/26854). It's like
`raise(Postpone, reason)` except it's built-in so it needs to be able to
be encoded and caught by Suspense boundaries.

In Flight and Fizz these behave pretty much the same as errors. Flight
just forwards it to retrigger on the client. In Fizz they just trigger
client rendering which itself might just postpone again or fill in the
value. The difference is how they get logged.

In Flight and Fizz they log to `onPostpone(reason)` instead of
`onError(error)`. This log is meant to help find deopts on the server
like finding places where you fall back to client rendering. The reason
that you pass in is for that purpose to help the reason for any deopts.

I do track the stack trace in DEV but I don't currently expose it to
`onPostpone`. This seems like a limitation. It might be better to expose
the Postpone object which is an Error object but that's more of an
implementation detail. I could also pass it as a second argument.

On the client after hydration they don't get passed to
`onRecoverableError`. There's no global `onPostpone` API to capture
postponed things on the client just like there's no `onError`. At that
point it's just assumed to be intentional. It doesn't have any `digest`
or reason passed to the client since it's not logged.

There are some hacky solutions that currently just tries to reuse as
much of the existing code as possible but should be more properly
implemented.
- Fiber is currently just converting it to a fake Promise object so that
it behaves like an infinite Promise.
- Fizz is encoding the magic digest string `"POSTPONE"` in the HTML so
we know to ignore it but it should probably just be something neater
that doesn't share namespace with digests.

Next I plan on using this in the `/static` entry points for additional
features.

Why "postpone"? It's basically a synonym to "defer" but we plan on using
"defer" for other purposes and it's overloaded anyway.

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[090ca7b7de...](https://github.com/git-for-windows/git/commit/090ca7b7ded7a4d54b88f9e58bfce94cbcdba756)
#### Friday 2023-08-18 00:28:09 by Johannes Schindelin

windows: ignore empty `PATH` elements

When looking up an executable via the `_which` function, Git GUI
imitates the `execlp()` strategy where the environment variable `PATH`
is interpreted as a list of paths in which to search.

For historical reasons, stemming from the olden times when it was
uncommon to download a lot of files from the internet into the current
directory, empty elements in this list are treated as if the current
directory had been specified.

Nowadays, of course, this treatment is highly dangerous as the current
directory often contains files that have just been downloaded and not
yet been inspected by the user. Unix/Linux users are essentially
expected to be very, very careful to simply not add empty `PATH`
elements, i.e. not to make use of that feature.

On Windows, however, it is quite common for `PATH` to contain empty
elements by mistake, e.g. as an unintended left-over entry when an
application was installed from the Windows Store and then uninstalled
manually.

While it would probably make most sense to safe-guard not only Windows
users, it seems to be common practice to ignore these empty `PATH`
elements _only_ on Windows, but not on other platforms.

Sadly, this practice is followed inconsistently between different
software projects, where projects with few, if any, Windows-based
contributors tend to be less consistent or even "blissful" about it.
Here is a non-exhaustive list:

Cygwin:

	It specifically "eats" empty paths when converting path lists to
	POSIX: https://github.com/cygwin/cygwin/commit/753702223c7d

	I.e. it follows the common practice.

PowerShell:

	It specifically ignores empty paths when searching the `PATH`.
	The reason for this is apparently so self-evident that it is not
	even mentioned here:
	https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_environment_variables#path-information

	I.e. it follows the common practice.

CMD:

	Oh my, CMD. Let's just forget about it, nobody in their right
	(security) mind takes CMD as inspiration. It is so unsafe by
	default that we even planned on dropping `Git CMD` from Git for
	Windows altogether, and only walked back on that plan when we
	found a super ugly hack, just to keep Git's users secure by
	default:

		https://github.com/git-for-windows/MINGW-packages/commit/82172388bb51

	So CMD chooses to hide behind the battle cry "Works as
	Designed!" that all too often leaves users vulnerable. CMD is
	probably the most prominent project whose lead you want to avoid
	following in matters of security.

Win32 API (`CreateProcess()`)

	Just like CMD, `CreateProcess()` adheres to the original design
	of the path lookup in the name of backward compatibility (see
	https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessw
	for details):

		If the file name does not contain a directory path, the
		system searches for the executable file in the following
		sequence:

		    1. The directory from which the application loaded.

		    2. The current directory for the parent process.

		    [...]

	I.e. the Win32 API itself chooses backwards compatibility over
	users' safety.

Git LFS:

	There have been not one, not two, but three security advisories
	about Git LFS executing executables from the current directory by
	mistake. As part of one of them, a change was introduced to stop
	treating empty `PATH` elements as equivalent to `.`:
	https://github.com/git-lfs/git-lfs/commit/7cd7bb0a1f0d

	I.e. it follows the common practice.

Go:

	Go does not follow the common practice, and you can think about
	that what you want:
	https://github.com/golang/go/blob/go1.19.3/src/os/exec/lp_windows.go#L114-L135
	https://github.com/golang/go/blob/go1.19.3/src/path/filepath/path_windows.go#L108-L137

Git Credential Manager:

	It tries to imitate Git LFS, but unfortunately misses the empty
	`PATH` element handling. As of time of writing, this is in the
	process of being fixed:
	https://github.com/GitCredentialManager/git-credential-manager/pull/968

So now that we have established that it is a common practice to ignore
empty `PATH` elements on Windows, let's assess this commit's change
using Schneier's Five-Step Process
(https://www.schneier.com/crypto-gram/archives/2002/0415.html#1):

Step 1: What problem does it solve?

	It prevents an entire class of Remote Code Execution exploits via
	Git GUI's `Clone` functionality.

Step 2: How well does it solve that problem?

	Very well. It prevents the attack vector of luring an unsuspecting
	victim into cloning an executable into the worktree root directory
	that Git GUI immediately executes.

Step 3: What other security problems does it cause?

	Maybe non-security problems: If a project (ab-)uses the unsafe
	`PATH` lookup. That would not only be unsafe, though, but
	fragile in the first place because it would break when running
	in a subdirectory. Therefore I would consider this a scenario
	not worth keeping working.

Step 4: What are the costs of this measure?

	Almost nil, except for the time writing up this commit message
	;-)

Step 5: Given the answers to steps two through four, is the security
	measure worth the costs?

	Yes. Keeping Git's users Secure By Default is worth it. It's a
	tiny price to pay compared to the damages even a single
	successful exploit can cost.

So let's follow that common practice in Git GUI, too.

Signed-off-by: Johannes Schindelin <johannes.schindelin@gmx.de>

---
## [Chris-plus-alphanumericgibberish/dNAO](https://github.com/Chris-plus-alphanumericgibberish/dNAO)@[c72bbc88de...](https://github.com/Chris-plus-alphanumericgibberish/dNAO/commit/c72bbc88def9850f829b63af07d305ee3a379224)
#### Friday 2023-08-18 00:50:59 by chris

Forge patch: Adapted from EvilHack

This creates the forge dungeon feature. This is a straight port, with no added functionality (and plenty of removed functionality)

Currently mostly does nothing, pending integration w/ NPC smiths and creation of a smithing skill
-Reforging to remove rust etc. in commented out (this is something smiths will be able to do but it needs to be integrated with whatever that system ends up being)
-Blessing is commented out
-The blacksmiths cookbook was not ported. Basic items can be made by NPC smiths, artifacts and magic items await a PC smithing skill
-Can still break, dip into, and drink from forges
--Dipping destroys non-metal items, and can be used to burn up straitjackets/striped shirts (in extchange for 6d6 damage!)
--Dipping can ocasionally summon monsters and blow up forges
--Dipping with a wielded hammer allows unpunishing
--Drinking from is still an instadeath in most cases.
--Breaking results in lava and is probably a very bad idea.

Ports fire damage function improvements and lava damage (from 3.6? .7? vanilla?)

---
## [OpenVZ/vzkernel](https://github.com/OpenVZ/vzkernel)@[867ff182a0...](https://github.com/OpenVZ/vzkernel/commit/867ff182a0468345752b1a08ddf273500e05fa8f)
#### Friday 2023-08-18 00:51:16 by Vladimir Davydov

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

https://jira.sw.ru/browse/PSBM-144163
Rebase to RHEL9.1 note:
 * working with pages has been transformed to working with folios,
   so page_cache_get_speculative() -> folio_try_get_rcu()

Rebased-by: Konstantin Khorenko <khorenko@virtuozzo.com>

Feature: mm: transcendent file cache (tcache)

---
## [jhnc-oss/openembedded-core](https://github.com/jhnc-oss/openembedded-core)@[596fb699d4...](https://github.com/jhnc-oss/openembedded-core/commit/596fb699d470d7779bfa694e04908929ffeabcf7)
#### Friday 2023-08-18 00:58:14 by Richard Purdie

pseudo: Fix to work with glibc 2.38

This adds a horrible hack to get pseudo working with glibc 2.38. We can't
drop _GNU_SOURCE to something like _DEFAULT_SOURCE since we need the defines
the gnu options bring in. That leaves using internal glibc defines to disable
the c23 versions of strtol/fscanf and friends. Which would break pseudo
build with 2.38 from running on hosts with older glibc.

We'll probably need to come up with something better but this gets glibc 2.38
and working and avoids autobuilder failures.

Signed-off-by: Richard Purdie <richard.purdie@linuxfoundation.org>

---
## [VladinXXV/tgstation](https://github.com/VladinXXV/tgstation)@[297f7f88e8...](https://github.com/VladinXXV/tgstation/commit/297f7f88e866d4a17b27cb15c0b8ee606742bbf6)
#### Friday 2023-08-18 01:36:57 by Sealed101

Fixes things about goliaths: wallhacks/range hacks(no, really) and tentacles not spawning in mineral turfs; also fixes `find_potential_targets` wallhacks (#77393)

## About The Pull Request

Goliath's sand digging behaviour could potentially target a turf that's
actually unreachable by the goliath, e.g.
```
G#
#T
```
where G - goliath # - wall T - target turf. fixed that, but i think
there could be something easier here, maybe instead grabbing turfs in
goliath's `view()`? unsure

The component goliaths use to telegraph their attacks
(`basic_mob_attack_telegraph`) casts a `do_after()` to perform the
attack, but it was not actually checking for the target staying in melee
range, as it was using the source goliath as both `user` and `target`,
so it didn't actually care at all for the target. Implemented an
`extra_checks` to `Adjacent()` since that's the closest we get for melee
range shenanigans I suppose
This still allows the source basicmob to attack the target if the target
moves around the source basicmob.

`!`Goliaths were also able to summon tentacles on a target that moved
into cover and still stayed in the `find_potential_targets` target
range. Which meant more wallhacks. This was a thing for the base
`find_potential_targets`, meaning that every basic mob using it was a
dirty haxxor (or very vengeful). Fixed that by making
`find_potential_targets` also check for `can_see()` before proceeding
further down `find_potential_targets/perform()`. `!` The only exception
to this check currently are bileworms.

`!`Goliath tentacles were not spawning in mineral turfs as their
`Initialize()` checked for closed turfs before handling mineral turf
mining. Fixed that as well.

## Why It's Good For The Game

![Dr__Hax_by_Didgeridoo_Dealer](https://github.com/tgstation/tgstation/assets/75863639/fbcbfc1b-f489-435e-bb01-677f55398787)

## Changelog

:cl:
fix: fixed goliaths digging sand that they can't actually reach (behind
windows or inbetween closed turfs)
fix: fixed goliaths melee attacking their target despite the target
running away from goliath melee range
fix: fixed goliath tentacles not spawning in mineral turfs
fix: fixed goliaths summoning tentacles on targets that moved behind
cover but stayed in their targeting range. this applies for most basic
mobs, really, so if any basic mob was targeting you despite you hauling
ass behind cover, they shouldn't anymore
/:cl:

---
## [Bird-Lounge/Skyraptor-SS13](https://github.com/Bird-Lounge/Skyraptor-SS13)@[1713af4933...](https://github.com/Bird-Lounge/Skyraptor-SS13/commit/1713af4933c5eab15619b56a5f2882c0446a7852)
#### Friday 2023-08-18 02:40:08 by necromanceranne

Settler Quirk: Tame the Outdoors! Have trouble with tall shelves... (#77654)

## About The Pull Request

Adds the Settler quirk. This gives you bonuses to taming animals and
fishing, as well as making you gain hunger slower than others.

However, you are quite a bit slower than most people, and have trouble
with vaulting objects. You do, however, suffer significantly less from
equipment slowdown. (to the point that it is almost zero)

Settler riders are faster on their mounts than others if they're at
least sane. They start to slow down if they're less sane.

You are also shorter than most people. 

<details>
  <summary>Typical Settler encounters the typical Spacer</summary>
  

![Dr_Xr1nU0AAMsSE](https://github.com/tgstation/tgstation/assets/40847847/86ed4947-de5f-4bdf-a8ae-521dc7c30662)
  
</details>

## Why It's Good For The Game

I wanted to add a lightweight quirk that was kind of the 'opposite' of
Spacer, but a little more focused on interacting with elements of the
game world that would enjoy some attention. So, I thought 'what about an
outdoorsman quirk?'

So, I based it around being from people who lived out on the rim, under
unideal circumstances (and probably heavier gravity than Earth), and
taming the land. The slower movespeed encourages finding an animal to
tame that you can ride, and the bonuses to taming should help make that
a bit easier. The other additions just made sense for someone living it
a bit rough in the wilderness.

Having a bunch of settlers taming cows and riding around on them all
shift just kind of sounds hilarious to me.

## Changelog
:cl:
add: Settler quirk! Conqueror the great outdoors....in space. Just make
sure nobody asks you to get anything from the top shelf.
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>
Co-authored-by: Ghom <42542238+Ghommie@users.noreply.github.com>

---
## [Bird-Lounge/Skyraptor-SS13](https://github.com/Bird-Lounge/Skyraptor-SS13)@[3f2a885ba9...](https://github.com/Bird-Lounge/Skyraptor-SS13/commit/3f2a885ba992e43546401f635e248a35d5c5fd8a)
#### Friday 2023-08-18 02:41:58 by Jacquerel

Polymorphic Inverter tweaks (#77675)

## About The Pull Request

Fixes #77649

You can no longer use the belt to turn into any kind of carbon mob,
sorry gamers it was a cool dream but it leads to too many problems.
Also I made space dragon "there's an alive guy in my stomach" code now
work on signals instead of on Life tick which is slightly more efficient
and also resolves an issue with the funny belt.

## Why It's Good For The Game

Too much room for weird edge cases as a result of doing this (messing
with monkey DNA, producing infinite xeno organs, blocking legit xeno
queens from being created) which had no graceful solution.
Moving stuff off Life if it can be event based is nice.

## Changelog

:cl:
fix: Turning into a space dragon with the polymorphic inverter will no
longer leave you existing in two places
balance: You can no longer use the belt to transform into monkeys or
xenomorphs, for technical reasons.
/:cl:

---
## [goober3/hi-github-portside](https://github.com/goober3/hi-github-portside)@[ee4021c507...](https://github.com/goober3/hi-github-portside/commit/ee4021c50792c11bfd21085156edd32200c21cb8)
#### Friday 2023-08-18 02:44:46 by Imaginos16

Destroying Sprite Cruft Part One: Cruft Sucks (#2220)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Title


![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/1cedcdb1-01b5-4f28-a759-65428c2dcd0a)

In total, the:

- IV Drip
- All-In-One Grinder
- Book Binder
- Book Scanner
- Water Cooler
- Tank Dispenser

Have all been successfully uncrufted. No more cruft. Just clean sprites
now :D

Oh and dressers have directionals now at the request of @Bjarl 

Credit goes to the original authors in the changelog.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
begone cruft I fucking hate cruft
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: PositiveEntropy, Maxymax13, Wallemations, Kryson,
Viro/Axietheaxolotl, MeyHaZah
imageadd: Books, IV drips, tank dispensers, all-in-one grinders, water
coolers, book binders and book scanners have been resprited!
imageadd: Dressers now have directionals!
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Hatterhat/Skyrat-tg](https://github.com/Hatterhat/Skyrat-tg)@[f08ce907dd...](https://github.com/Hatterhat/Skyrat-tg/commit/f08ce907ddc90398f56e449a2dc29e1d1ea22278)
#### Friday 2023-08-18 02:55:34 by SkyratBot

[MIRROR] Restricts Scrapheap & Lepton Violet behind conditions, alters Rollerdome [MDB IGNORE] (#23012)

* Restricts Scrapheap & Lepton Violet behind conditions, alters Rollerdome (#77277)

## About The Pull Request

Lepton Violet (wabbajack) shuttle must be unlocked by having some form
of polymorph happen in-game first (Pride Mirror or the cursed springs
are the most accessible sources)

Scrapheap shuttle can only be bought if the Cargo budget is below 600
credits, and the shuttle has just less than half of its usual refueling
time left. However, it gives the cargo budget an influx of 3000 credits!

Uncle Pete's Rollerdome has had its price increased, and the disco
machine is no longer unbreakable.

## Why It's Good For The Game

First off, here is my reasoning for why these need altering at all.

Players will always naturally gravitate to the wackiest and
most-out-there options, in this case this applies to shuttles. It's why
the Monastery or the Asteroid or Daniel are reasonably common sights,
more common than some of the 'boring' shuttle options that don't need
unlock with an emag.

The problem here, as I see it, is that there is no incentive
what-so-ever to NOT purchase these 'wacky' shuttles. Some of the
shuttles in the code are just way too stupid to be seen on most or even
some rounds (Arena, Disco Inferno?), so they require rare unlocks to
occur. Wacky shuttles being spammed round after round are bad due to
several reasons:
1. Players will run every joke to the ground. Wacky conditionless
shuttles take up a large amount of space in the shuttle memeplex, so
they are disproportionately seen in comparison to any of the
less-extravagant but more grounded and actually interesting options.
(Medisim? Monkeys anyone?). This ends up making the wacky shuttles
actually *less* wacky and just the stale and boring options.
2. Wacky shuttles affect the end-round quite a lot. This is fine, of
course, but not when these wacky shuttles can be seen every round.
3. These wacky shuttles don't have proper facilities. None of them have
a good medical section, or emergency supplies, or enough room. This gets
pretty annoying pretty fast.
4. One Funny Guy (the quintessential example being the clown with a dead
captain's ID) is all but guaranteed to try to buy the funniest and most
annoying shuttle to piss off the rest of the crew. With how Funny and
Annoying these shuttles are, not to mention how dirt-cheap they are (or
literally give you money!), they're easily the most seen alternate
shuttles, which isn't good when they alter how the round-end plays so
heavily.

> Lepton Violet (wabbajack) shuttle must be unlocked by having some form
of polymorph happen in-game first (Pride Mirror is the most accessible
source)

The Wabbajack has a endless source of voluntary Polymorphs with a
comically low price, which means it is purchased endlessly by crew, not
to mention being literally a source of free syndiborgs and xenos. While
I'm not a balanceposter, this does come with some annoyances especially
for antagonists who just randomly get blown up by an assault borg. This
is fine and fun every so often, but not as a common occurrence, not as a
guaranteed every-round option. I think it's an excellent candidate for
an unlock condition.

> Scrapheap shuttle can only be bought if the Cargo budget is below 600
credits, and the emergency shuttle is more than halfway refueled.
However, it gives the cargo budget an influx of 3000 credits!

This is LITERALLY 'haha grief shuttle', I have no idea how it even got
in as a condition-less shuttle. You see the captain buy it For No Raisin
Lul 2 minutes in, sigh to yourself, and secure an EVA suit when the
shuttle lands to try to survive in the unbelievably cramped space.
(Someone always blows it up.)

Instead of being JUST Grief Shuttle, now it has some interesting reasons
to exist. Revs and you're dirt-poor? Nukies just declared war after the
Clown bought ten crates of creampie dufflebags? Buy this shuttle and get
an influx of money.

> Uncle Pete's Rollerdome has had its price increased, and the disco
machine is no longer unbreakable.

This one isn't as egregious as the above, but I believe my personal
dislike of it extends to a game design level, to an extent. One person
can buy this shuttle and the crew as a whole are left to groan as they
prepare for a noisy, confusing shuttle in which everyone is ten tiles
shifted to their left as their sprite does the most ridiculous dance
seen in SS13 history. 'Just turn the music off!': I'm glad this is an
option, but it doesn't change how much this shuttle alters things. It's
fine as a sendoff to a nice, chill greenshift, but as a constant sight
in red shifts it's just... frustrating. And purchased BECAUSE it's
frustrating, to the short-lived schadenfreude of one person and the
frustration of others.

And then the unbreakable disco machine. Why is it unbreakable. If the
crew doesn't want to listen to the thing, let them break it? Buy Disco
Inferno if you want an unbreakable disco.

Some of these changes are probably over-the-top, but remember that these
will still be seen in-game, just a bit rarer. Worst case scenario the
shuttle replacement event will let them have their time in the
limelight.

## Changelog

:cl:
balance: Lepton Violet (wabbajack) shuttle must be unlocked by having
some form of polymorph happen in-game first (Pride Mirror or the cursed
springs are the most accessible sources)
balance: Scrapheap shuttle can only be bought if the Cargo budget is
below 600 credits, and the shuttle has just less than half of its usual
refueling time left. However, it gives the cargo budget an influx of
3000 credits!
qol: Uncle Pete's Rollerdome has had its price increased, and the disco
machine is no longer unbreakable.
/:cl:

* Restricts Scrapheap & Lepton Violet behind conditions, alters Rollerdome

---------

Co-authored-by: carlarctg <53100513+carlarctg@users.noreply.github.com>

---
## [c0ntradicti0n/dialectics](https://github.com/c0ntradicti0n/dialectics)@[2e73fd8c25...](https://github.com/c0ntradicti0n/dialectics/commit/2e73fd8c253c4999e87a5d4f791b4189e6cc819b)
#### Friday 2023-08-18 02:57:17 by c0ntradicti0n

Automated TEXT Commit: Use.md" 3/1/1/.Signification.md 3/1/1/1/.Communication.md 3/1/1/1/1/.Linguistics.md 3/1/1/1/1/1/.Phonetics.md Elements.md" 3/1/1/1/1/1/1/1/.Consonants.md 3/1/1/1/1/1/1/2/.Vowels.md 3/1/1/1/1/1/1/3/.Tones.md 3/1/1/1/1/1/1/_Silence-Sound.md Properties.md" Articulation.md" Articulation.md" 3/1/1/1/1/1/2/3/.Voice.md Properties.md" 3/1/1/1/1/1/3/1/.Amplitude.md 3/1/1/1/1/1/3/2/.Frequency.md 3/1/1/1/1/1/3/3/.Timbre.md 3/1/1/1/1/1/3/_Noise-Harmony.md 3/1/1/1/1/1/_Articulation-Acoustics.md 3/1/1/1/1/2/.Syntax.md 3/1/1/1/1/2/1/.Morphology.md 3/1/1/1/1/2/1/1/.Root.md 3/1/1/1/1/2/1/2/.Affix.md 3/1/1/1/1/2/1/3/.Compound.md 3/1/1/1/1/2/1/_Word-Phrase.md 3/1/1/1/1/2/2/.Grammar.md 3/1/1/1/1/2/2/1/.Tense.md 3/1/1/1/1/2/2/2/.Aspect.md 3/1/1/1/1/2/2/3/.Mood.md 3/1/1/1/1/2/2/_Rule-Variation.md Structure.md" Sentence.md" Sentence.md" Sentence.md" 3/1/1/1/1/2/3/_Clause-Phrase.md 3/1/1/1/1/2/_Structure-Function.md 3/1/1/1/1/3/.Pragmatics.md Acts.md" 3/1/1/1/1/3/1/1/.Assertive.md 3/1/1/1/1/3/1/2/.Directive.md 3/1/1/1/1/3/1/3/.Commissive.md 3/1/1/1/1/3/1/_Intent-Interpretation.md 3/1/1/1/1/3/2/.Deixis.md Deixis.md" Deixis.md" Deixis.md" 3/1/1/1/1/3/2/_Here-There.md 3/1/1/1/1/3/3/.Implicature.md 3/1/1/1/1/3/3/1/.Conventional.md 3/1/1/1/1/3/3/2/.Conversational.md 3/1/1/1/1/3/3/3/.Scalar.md 3/1/1/1/1/3/3/_Explicit-Implicit.md 3/1/1/1/1/3/_Context-Meaning.md 3/1/1/1/1/_Form-Function.md Theory.md" 3/1/1/1/2/1/.Rhythm.md 3/1/1/1/2/1/1/.Beat.md 3/1/1/1/2/1/1/1/.Onset.md 3/1/1/1/2/1/1/1/1/.Attack.md 3/1/1/1/2/1/1/1/1/1/.Start.md 3/1/1/1/2/1/1/1/1/1/1/.Onset.md 3/1/1/1/2/1/1/1/1/1/2/.Initiation.md 3/1/1/1/2/1/1/1/1/1/3/.Commencement.md 3/1/1/1/2/1/1/1/1/1/_Alpha-Omega.md 3/1/1/1/2/1/1/1/1/2/.Rise.md 3/1/1/1/2/1/1/1/1/2/1/.Increase.md 3/1/1/1/2/1/1/1/1/2/2/.Boost.md 3/1/1/1/2/1/1/1/1/2/3/.Amplify.md 3/1/1/1/2/1/1/1/1/2/_Ascend-Dive.md 3/1/1/1/2/1/1/1/1/3/.Peak.md 3/1/1/1/2/1/1/1/1/3/1/.Summit.md 3/1/1/1/2/1/1/1/1/3/2/.Zenith.md 3/1/1/1/2/1/1/1/1/3/3/.Apex.md 3/1/1/1/2/1/1/1/1/3/_Max-Min.md 3/1/1/1/2/1/1/1/1/_Instant-Gradual.md 3/1/1/1/2/1/1/1/2/.Decay.md 3/1/1/1/2/1/1/1/2/1/.Fall.md 3/1/1/1/2/1/1/1/2/2/.Diminish.md 3/1/1/1/2/1/1/1/2/3/.Level.md 3/1/1/1/2/1/1/1/2/_Decline-Maintain.md 3/1/1/1/2/1/1/1/3/.Sustain.md 3/1/1/1/2/1/1/1/3/1/.Prolong.md 3/1/1/1/2/1/1/1/3/2/.Retain.md 3/1/1/1/2/1/1/1/3/3/.Extend.md 3/1/1/1/2/1/1/1/3/_Grip-LetGo.md 3/1/1/1/2/1/1/1/_Sharp-Soft.md 3/1/1/1/2/1/1/2/.Accent.md Beat.md" 3/1/1/1/2/1/1/2/1/1/.Downbeat.md 3/1/1/1/2/1/1/2/1/1/1/.Thud.md 3/1/1/1/2/1/1/2/1/1/2/.Impact.md 3/1/1/1/2/1/1/2/1/1/3/.Strike.md 3/1/1/1/2/1/1/2/1/1/_Drop-Lift.md 3/1/1/1/2/1/1/2/1/2/.Accentuation.md 3/1/1/1/2/1/1/2/1/2/1/.Emphasis.md 3/1/1/1/2/1/1/2/1/2/2/.Underline.md 3/1/1/1/2/1/1/2/1/2/3/.Stress.md 3/1/1/1/2/1/1/2/1/2/_Spotlight-Shadow.md 3/1/1/1/2/1/1/2/1/3/.Stressor.md 3/1/1/1/2/1/1/2/1/3/1/.Tension.md 3/1/1/1/2/1/1/2/1/3/2/.Force.md 3/1/1/1/2/1/1/2/1/3/3/.Load.md 3/1/1/1/2/1/1/2/1/3/_Compress-Release.md 3/1/1/1/2/1/1/2/1/_Highlight-Background.md Beat.md" 3/1/1/1/2/1/1/2/2/1/.Upbeat.md 3/1/1/1/2/1/1/2/2/2/.Deemphasis.md 3/1/1/1/2/1/1/2/2/3/.Lull.md 3/1/1/1/2/1/1/2/2/_Background-Foreground.md 3/1/1/1/2/1/1/2/3/.Offbeat.md 3/1/1/1/2/1/1/2/3/1/.Sync.md 3/1/1/1/2/1/1/2/3/2/.Mismatch.md 3/1/1/1/2/1/1/2/3/3/.Displacement.md 3/1/1/1/2/1/1/2/3/_OutAlign-InAlign.md 3/1/1/1/2/1/1/2/_Emphasized-Subdued.md 3/1/1/1/2/1/1/3/.Syncopation.md Beat.md" Beat.md" Beat.md" 3/1/1/1/2/1/1/3/_Preemptive-Postponed.md 3/1/1/1/2/1/1/_Predictable-Unpredictable.md 3/1/1/1/2/1/2/.Meter.md 3/1/1/1/2/1/2/1/.Duple.md 3/1/1/1/2/1/2/1/1/.March.md 3/1/1/1/2/1/2/1/1/1/.Step.md 3/1/1/1/2/1/2/1/1/2/.Stride.md 3/1/1/1/2/1/2/1/1/3/.Progression.md 3/1/1/1/2/1/2/1/1/_Constant-Change.md 3/1/1/1/2/1/2/1/2/.Polka.md 3/1/1/1/2/1/2/1/2/1/.Hop.md 3/1/1/1/2/1/2/1/2/2/.Jump.md 3/1/1/1/2/1/2/1/2/3/.Skip.md 3/1/1/1/2/1/2/1/2/_Elevate-Ground.md 3/1/1/1/2/1/2/1/3/.Tango.md 3/1/1/1/2/1/2/1/3/1/.Embrace.md 3/1/1/1/2/1/2/1/3/2/.Stride.md 3/1/1/1/2/1/2/1/3/3/.Flourish.md 3/1/1/1/2/1/2/1/3/_Union-Separate.md 3/1/1/1/2/1/2/1/_Paired-Unpaired.md 3/1/1/1/2/1/2/2/.Triple.md 3/1/1/1/2/1/2/2/1/.Waltz.md 3/1/1/1/2/1/2/2/2/.Mazurka.md 3/1/1/1/2/1/2/2/3/.Minuet.md 3/1/1/1/2/1/2/2/_Trio-Solo.md 3/1/1/1/2/1/2/3/.Complex.md 3/1/1/1/2/1/2/3/1/.Five-Beat.md 3/1/1/1/2/1/2/3/2/.Seven-Beat.md 3/1/1/1/2/1/2/3/3/.Irregular.md 3/1/1/1/2/1/2/3/_Hybrid-Pure.md 3/1/1/1/2/1/2/_Even-Odd.md 3/1/1/1/2/1/3/.Tempo.md 3/1/1/1/2/1/3/1/.Adagio.md 3/1/1/1/2/1/3/2/.Andante.md 3/1/1/1/2/1/3/3/.Allegro.md 3/1/1/1/2/1/3/_Lethargic-Brisk.md 3/1/1/1/2/1/_Static-Dynamic.md 3/1/1/1/2/2/.Harmonics.md 3/1/1/1/2/2/1/.Frequency.md 3/1/1/1/2/2/1/1/.Bass.md 3/1/1/1/2/2/1/1/1/.Sub-Bass.md 3/1/1/1/2/2/1/1/2/.Bassline.md Midrange.md" 3/1/1/1/2/2/1/1/_Buried-Apparent.md 3/1/1/1/2/2/1/2/.Mid.md 3/1/1/1/2/2/1/2/1/.Middle.md Midrange.md" Treble.md" 3/1/1/1/2/2/1/2/_Balanced-Unbalanced.md 3/1/1/1/2/2/1/3/.Treble.md Frequency.md" 3/1/1/1/2/2/1/3/2/.Brightness.md 3/1/1/1/2/2/1/3/3/.Sharpness.md 3/1/1/1/2/2/1/3/_Climax-Nadir.md 3/1/1/1/2/2/1/_Deep-Shrill.md 3/1/1/1/2/2/2/.Series.md Harmonic.md" 3/1/1/1/2/2/2/1/1/.Fundamental.md 3/1/1/1/2/2/2/1/1/1/.Base.md 3/1/1/1/2/2/2/1/1/1/1/.Root.md 3/1/1/1/2/2/2/1/1/1/2/.Ground.md 3/1/1/1/2/2/2/1/1/1/3/.Bedrock.md 3/1/1/1/2/2/2/1/1/1/_Origin-Growth.md 3/1/1/1/2/2/2/1/1/2/.Foundation.md 3/1/1/1/2/2/2/1/1/2/1/.Base.md 3/1/1/1/2/2/2/1/1/2/2/.Bottom.md 3/1/1/1/2/2/2/1/1/2/3/.Underpinning.md 3/1/1/1/2/2/2/1/1/2/_Start-Build.md 3/1/1/1/2/2/2/1/1/3/.Groundwork.md 3/1/1/1/2/2/2/1/1/3/1/.Framework.md 3/1/1/1/2/2/2/1/1/3/2/.Structure.md 3/1/1/1/2/2/2/1/1/3/3/.Skeleton.md 3/1/1/1/2/2/2/1/1/3/_Plan-Outcome.md 3/1/1/1/2/2/2/1/1/_Start-Expand.md Overtone.md" Harmonic.md" 3/1/1/1/2/2/2/1/2/2/.Deviation.md 3/1/1/1/2/2/2/1/2/3/.Variation.md 3/1/1/1/2/2/2/1/2/_Follow-Origin.md Overtone.md" Harmonic.md" 3/1/1/1/2/2/2/1/3/2/.Deviant.md 3/1/1/1/2/2/2/1/3/3/.Modifier.md 3/1/1/1/2/2/2/1/3/_Overlay-Origin.md 3/1/1/1/2/2/2/1/_Root-Branch.md Harmonic.md" Overtone.md" Harmonic.md" Harmonic.md" 3/1/1/1/2/2/2/2/_Sheet-Underneath.md Harmonics.md" Overtone.md" Overtone.md" Overtone.md" 3/1/1/1/2/2/2/3/_Principal-Auxiliary.md 3/1/1/1/2/2/2/_Base-Overtones.md 3/1/1/1/2/2/3/.Timbre.md 3/1/1/1/2/2/3/1/.Sinewave.md Wave.md" State.md" 3/1/1/1/2/2/3/1/1/1/1/.Unchanging.md 3/1/1/1/2/2/3/1/1/1/2/.Constant.md 3/1/1/1/2/2/3/1/1/1/3/.Fixed.md 3/1/1/1/2/2/3/1/1/1/_Same-Change.md 3/1/1/1/2/2/3/1/1/2/.Plain.md 3/1/1/1/2/2/3/1/1/2/1/.Unembellished.md 3/1/1/1/2/2/3/1/1/2/2/.Basic.md 3/1/1/1/2/2/3/1/1/2/3/.Simplistic.md 3/1/1/1/2/2/3/1/1/2/_Naked-Decorated.md 3/1/1/1/2/2/3/1/1/3/.Homogeneous.md 3/1/1/1/2/2/3/1/1/3/1/.Identical.md 3/1/1/1/2/2/3/1/1/3/2/.Consistent.md 3/1/1/1/2/2/3/1/1/3/3/.Monolithic.md 3/1/1/1/2/2/3/1/1/3/_Alike-Different.md 3/1/1/1/2/2/3/1/1/_Same-Vary.md Wave.md" 3/1/1/1/2/2/3/1/2/1/.Core.md 3/1/1/1/2/2/3/1/2/2/.Central.md 3/1/1/1/2/2/3/1/2/3/.Prime.md 3/1/1/1/2/2/3/1/2/_Main-Secondary.md Wave.md" 3/1/1/1/2/2/3/1/3/1/.Clean.md 3/1/1/1/2/2/3/1/3/2/.Pure.md 3/1/1/1/2/2/3/1/3/3/.Transparent.md 3/1/1/1/2/2/3/1/3/_Distinct-Blur.md 3/1/1/1/2/2/3/1/_Clean-Blended.md 3/1/1/1/2/2/3/2/.Sawtooth.md Wave.md" 3/1/1/1/2/2/3/2/1/1/.Rough.md 3/1/1/1/2/2/3/2/1/2/.Irregular.md 3/1/1/1/2/2/3/2/1/3/.Zigzag.md 3/1/1/1/2/2/3/2/1/_Rugged-Smooth.md Wave.md" 3/1/1/1/2/2/3/2/2/1/.Vibration.md 3/1/1/1/2/2/3/2/2/2/.Pulse.md 3/1/1/1/2/2/3/2/2/3/.Echo.md 3/1/1/1/2/2/3/2/2/_Ring-Silent.md Wave.md" 3/1/1/1/2/2/3/2/3/1/.Dense.md 3/1/1/1/2/2/3/2/3/2/.Layered.md 3/1/1/1/2/2/3/2/3/3/.Thick.md 3/1/1/1/2/2/3/2/3/_Saturated-Vacant.md 3/1/1/1/2/2/3/2/_Edgy-Sleek.md 3/1/1/1/2/2/3/3/.Squarewave.md Cycle.md" Pulse.md" Wave.md" 3/1/1/1/2/2/3/3/_Symmetric-Asymmetric.md 3/1/1/1/2/2/3/_Clean-Distorted.md 3/1/1/1/2/2/_Simple-Rich.md 3/1/1/1/2/3/.Timing.md 3/1/1/1/2/3/1/.Duration.md 3/1/1/1/2/3/1/1/.Instant.md 3/1/1/1/2/3/1/1/1/.Second.md 3/1/1/1/2/3/1/1/1/1/.Milliseconds.md 3/1/1/1/2/3/1/1/1/1/_Brief-Extended.md 3/1/1/1/2/3/1/1/1/2/.Moments.md 3/1/1/1/2/3/1/1/1/2/_Glimpse-Span.md 3/1/1/1/2/3/1/1/1/_Tick-Tock.md 3/1/1/1/2/3/1/1/2/.Minute.md 3/1/1/1/2/3/1/1/2/1/.Countdown.md 3/1/1/1/2/3/1/1/2/1/_Start-Stop.md 3/1/1/1/2/3/1/1/2/2/.Timer.md 3/1/1/1/2/3/1/1/2/2/_Set-Elapsed.md 3/1/1/1/2/3/1/1/2/_Wait-Proceed.md 3/1/1/1/2/3/1/1/_Moment-Decade.md 3/1/1/1/2/3/1/2/.Eternity.md 3/1/1/1/2/3/1/2/1/.Decade.md 3/1/1/1/2/3/1/2/1/1/.1970s.md 3/1/1/1/2/3/1/2/1/1/_Retro-Modern.md 3/1/1/1/2/3/1/2/1/2/.1980s.md 3/1/1/1/2/3/1/2/1/2/_Classic-Contemporary.md 3/1/1/1/2/3/1/2/1/_Past-Future.md 3/1/1/1/2/3/1/2/2/.Century.md 3/1/1/1/2/3/1/2/2/1/.20th.md 3/1/1/1/2/3/1/2/2/1/_Industrial-Digital.md 3/1/1/1/2/3/1/2/2/2/.21st.md 3/1/1/1/2/3/1/2/2/2/_Internet-AI.md 3/1/1/1/2/3/1/2/2/_Aeon-Age.md 3/1/1/1/2/3/1/2/_Ephemeral-Endless.md 3/1/1/1/2/3/1/_Short-Long.md 3/1/1/1/2/3/2/.Chronology.md 3/1/1/1/2/3/2/1/.History.md 3/1/1/1/2/3/2/1/1/.Epoch.md 3/1/1/1/2/3/2/1/1/_Birth-End.md 3/1/1/1/2/3/2/1/2/.Era.md 3/1/1/1/2/3/2/1/2/_Beginning-Completion.md 3/1/1/1/2/3/2/1/_Yesterday-Tomorrow.md 3/1/1/1/2/3/2/2/.Forecast.md 3/1/1/1/2/3/2/2/1/.Weather.md 3/1/1/1/2/3/2/2/1/_Cloud-Sun.md 3/1/1/1/2/3/2/2/2/.Trend.md 3/1/1/1/2/3/2/2/2/_Rise-Fall.md 3/1/1/1/2/3/2/2/_Prediction-Reality.md 3/1/1/1/2/3/2/_Past-Future.md 3/1/1/1/2/3/3/.Sync.md 3/1/1/1/2/3/3/1/.Alignment.md 3/1/1/1/2/3/3/1/1/.Melody.md 3/1/1/1/2/3/3/1/1/1/.Chord.md 3/1/1/1/2/3/3/1/1/1/_Harmony-Disharmony.md 3/1/1/1/2/3/3/1/1/2/.Scale.md 3/1/1/1/2/3/3/1/1/2/_Ascending-Descending.md 3/1/1/1/2/3/3/1/1/_Tune-Note.md 3/1/1/1/2/3/3/1/2/.Rhythm.md 3/1/1/1/2/3/3/1/2/1/.Pulse.md 3/1/1/1/2/3/3/1/2/1/_Steady-Vary.md 3/1/1/1/2/3/3/1/2/2/.Metronome.md 3/1/1/1/2/3/3/1/2/2/_Regular-Irregular.md 3/1/1/1/2/3/3/1/2/_Beat-Pause.md 3/1/1/1/2/3/3/1/_Harmony-Discord.md 3/1/1/1/2/3/3/2/.Lag.md 3/1/1/1/2/3/3/2/1/.Delay.md 3/1/1/1/2/3/3/2/1/_Wait-Rush.md 3/1/1/1/2/3/3/2/2/.Haste.md 3/1/1/1/2/3/3/2/2/_Speedy-Slow.md 3/1/1/1/2/3/3/2/_Before-After.md 3/1/1/1/2/3/3/_Synchronized-Asynchronous.md 3/1/1/1/2/3/_Predictability-Unpredictability.md 3/1/1/1/2/_Tension-Release.md Relation.md" 3/1/1/1/3/1/.Sociology.md 3/1/1/1/3/1/1/.Friendship.md 3/1/1/1/3/1/2/.Competitive.md 3/1/1/1/3/1/3/.Cooperative.md 3/1/1/1/3/1/_Individual-Society.md Structures.md" 3/1/1/1/3/2/1/.Stratification.md 3/1/1/1/3/2/1/1/.Class.md 3/1/1/1/3/2/1/2/.Status.md 3/1/1/1/3/2/1/3/.Power.md 3/1/1/1/3/2/2/.Community.md Movements.md" 3/1/1/1/3/2/3/.Society.md Patterns.md" 3/1/1/1/3/2/_Inequality-Equality.md 3/1/1/1/3/3/.Dialogue.md 3/1/1/1/3/3/1/.Conversation.md 3/1/1/1/3/3/1/1/.Chat.md 3/1/1/1/3/3/1/1/1/.Greeting.md 3/1/1/1/3/3/1/1/1/1/.Salute.md 3/1/1/1/3/3/1/1/1/1/_Formal-Casual.md 3/1/1/1/3/3/1/1/1/2/.Wave.md 3/1/1/1/3/3/1/1/1/2/_Visible-Invisible.md 3/1/1/1/3/3/1/1/1/_Hello-Bye.md 3/1/1/1/3/3/1/1/2/.Farewell.md 3/1/1/1/3/3/1/1/2/1/.Goodbye.md 3/1/1/1/3/3/1/1/2/1/_Temporary-Permanent.md 3/1/1/1/3/3/1/1/2/2/.Adieu.md 3/1/1/1/3/3/1/1/2/2/_Definite-Indefinite.md 3/1/1/1/3/3/1/1/2/_Start-End.md 3/1/1/1/3/3/1/1/_Casual-Formal.md 3/1/1/1/3/3/1/2/.Interview.md 3/1/1/1/3/3/1/2/1/.Query.md 3/1/1/1/3/3/1/2/1/1/.Inquiry.md 3/1/1/1/3/3/1/2/1/1/_General-Specific.md 3/1/1/1/3/3/1/2/1/2/.Prompt.md 3/1/1/1/3/3/1/2/1/2/_Lead-Direct.md 3/1/1/1/3/3/1/2/1/_Ask-Tell.md 3/1/1/1/3/3/1/2/2/.Reply.md 3/1/1/1/3/3/1/2/2/1/.Answer.md 3/1/1/1/3/3/1/2/2/1/_Brief-Detailed.md 3/1/1/1/3/3/1/2/2/2/.Explanation.md 3/1/1/1/3/3/1/2/2/2/_Surface-Depth.md 3/1/1/1/3/3/1/2/2/_Respond-Elaborate.md 3/1/1/1/3/3/1/2/_Question-Answer.md 3/1/1/1/3/3/1/_Spontaneity-Structure.md 3/1/1/1/3/3/2/.Monologue.md 3/1/1/1/3/3/2/1/.Soliloquy.md 3/1/1/1/3/3/2/1/1/.Thought.md 3/1/1/1/3/3/2/1/1/_Silent-Vocal.md 3/1/1/1/3/3/2/1/2/.Speech.md 3/1/1/1/3/3/2/1/2/_Public-Private.md 3/1/1/1/3/3/2/1/_Inner-Outer.md 3/1/1/1/3/3/2/2/.Narrative.md 3/1/1/1/3/3/2/2/1/.Tale.md 3/1/1/1/3/3/2/2/1/_Fiction-Reality.md 3/1/1/1/3/3/2/2/2/.Exposition.md 3/1/1/1/3/3/2/2/2/_Breakdown-Overview.md 3/1/1/1/3/3/2/2/_Story-Analysis.md 3/1/1/1/3/3/2/_Self-Other.md 3/1/1/1/3/3/3/.Debate.md 3/1/1/1/3/3/3/1/.Discussion.md 3/1/1/1/3/3/3/1/1/.Agreement.md 3/1/1/1/3/3/3/1/1/1/.Consensus.md 3/1/1/1/3/3/3/1/1/1/_Together-Apart.md 3/1/1/1/3/3/3/1/1/2/.Unison.md 3/1/1/1/3/3/3/1/1/2/_One-Many.md 3/1/1/1/3/3/3/1/1/_Yes-No.md 3/1/1/1/3/3/3/1/2/.Conflict.md 3/1/1/1/3/3/3/1/2/1/.Dispute.md 3/1/1/1/3/3/3/1/2/1/_Quarrel-Settle.md 3/1/1/1/3/3/3/1/2/2/.Contest.md 3/1/1/1/3/3/3/1/2/2/_Compete-Cooperate.md 3/1/1/1/3/3/3/1/2/_For-Against.md 3/1/1/1/3/3/3/1/_Understanding-Misunderstanding.md 3/1/1/1/3/3/3/2/.Argument.md 3/1/1/1/3/3/3/2/1/.Support.md 3/1/1/1/3/3/3/2/1/_Evidence-Claim.md 3/1/1/1/3/3/3/2/2/.Opposition.md 3/1/1/1/3/3/3/2/2/_Rebuttal-Counter.md 3/1/1/1/3/3/3/2/_Pro-Con.md 3/1/1/1/3/3/3/_Agree-Disagree.md 3/1/1/1/3/3/_Speaker-Listener.md 3/1/1/1/3/_Conflict-Resolution.md 3/1/1/1/_Verbal-Nonverbal.md Communication.md" 3/1/1/2/1/.Radio.md Propagation.md" 3/1/1/2/1/1/1/.Shortwave.md Modulation).md" Modulation).md" 3/1/1/2/1/1/_Amplitude-Frequency.md Processing.md" Signals.md" Conversion.md" Clarity.md" 3/1/1/2/1/2/_Transmitter-Receiver.md Systems.md" Production.md" Regulation.md" Demographics.md" 3/1/1/2/1/3/_Station-Listener.md 3/1/1/2/1/_Frequency-Modulation.md 3/1/1/2/2/.Television.md Technology.md" Tube.md" Display.md" Diode.md" 3/1/1/2/2/1/_Analog-Digital.md Methods.md" Broadcast.md" 3/1/1/2/2/2/1/_Pal-NTSC.md Broadcast.md" 3/1/1/2/2/2/2/_DVB-T2-ATSC.md Services.md" 3/1/1/2/2/2/3/_On-Demand-Live.md 3/1/1/2/2/2/_Terrestrial-Satellite.md 3/1/1/2/2/3/.Production.md Filming.md" 3/1/1/2/2/3/1/_Scripted-Unscripted.md Filming.md" 3/1/1/2/2/3/2/_Controlled-Uncontrolled.md 3/1/1/2/2/3/3/.Editing.md 3/1/1/2/2/3/3/_Linear-Nonlinear.md 3/1/1/2/2/3/_Pre-recorded-Live.md 3/1/1/2/2/_Image-Sound.md Recorder.md" Tape.md" 3/1/1/2/3/1/1/.Cassette.md 3/1/1/2/3/1/1/_Mono-Stereo.md 3/1/1/2/3/1/2/.Reel-to-Reel.md 3/1/1/2/3/1/2/_Track-Channel.md 3/1/1/2/3/1/_Bias-Erase.md Process.md" Pickup.md" 3/1/1/2/3/2/1/_Dynamic-Condenser.md Speed.md" 3/1/1/2/3/2/2/_Fast-Slow.md Quality.md" 3/1/1/2/3/2/3/_Fidelity-Distortion.md 3/1/1/2/3/2/_Input-Output.md 3/1/1/2/3/3/.Playback.md Mechanism.md" 3/1/1/2/3/3/1/_Single-Dual.md Equalization.md" 3/1/1/2/3/3/2/_Bass-Treble.md 3/1/1/2/3/3/3/.Amplification.md 3/1/1/2/3/3/3/_Low-High.md 3/1/1/2/3/3/_Forward-Reverse.md 3/1/1/2/3/_Analog-Digital.md 3/1/1/2/_Analog-Digital.md Evolution.md" 3/1/1/3/1/.Mechanics.md 3/1/1/3/1/1/.Hardware.md 3/1/1/3/1/2/.Software.md 3/1/1/3/1/3/.Embedded.md 3/1/1/3/2/.Electronics.md 3/1/1/3/3/.Nanotechnologies.md 3/1/1/3/_Macro-Micro.md 3/1/1/_Signifier-Signified.md Structures.md" 3/1/2/1/.Education.md Process.md" 3/1/2/1/1/1/.Knowledge.md 3/1/2/1/1/2/.Skills.md 3/1/2/1/1/3/.Implementation.md 3/1/2/1/1/_Learning-Application.md Methods.md" Learning.md" Activity.md" 3/1/2/1/2/1/1/1/.Laboratory.md 3/1/2/1/2/1/1/1/1/.Experiment.md 3/1/2/1/2/1/1/1/1/_Test-Result.md 3/1/2/1/2/1/1/1/2/.Observation.md 3/1/2/1/2/1/1/1/2/_Watch-Note.md 3/1/2/1/2/1/1/1/_Inside-Outside.md Trip.md" 3/1/2/1/2/1/1/2/_Local-Travel.md 3/1/2/1/2/1/1/_Practice-Review.md 3/1/2/1/2/1/2/.Reflection.md 3/1/2/1/2/1/2/1/.Journaling.md 3/1/2/1/2/1/2/1/1/.Diary.md 3/1/2/1/2/1/2/1/1/_Private-Public.md Review.md" 3/1/2/1/2/1/2/1/2/_Judge-Critique.md 3/1/2/1/2/1/2/1/_Write-Review.md 3/1/2/1/2/1/2/2/.Feedback.md 3/1/2/1/2/1/2/2/_Give-Receive.md 3/1/2/1/2/1/2/_Think-Record.md 3/1/2/1/2/1/_Doing-Observing.md 3/1/2/1/2/2/.Lecture.md 3/1/2/1/2/2/1/.Presentation.md 3/1/2/1/2/2/1/1/.Slide.md 3/1/2/1/2/2/1/1/1/.Photo.md 3/1/2/1/2/2/1/1/1/_Static-Dynamic.md 3/1/2/1/2/2/1/1/2/.Animation.md 3/1/2/1/2/2/1/1/2/_Frame-Play.md 3/1/2/1/2/2/1/1/_Still-Motion.md 3/1/2/1/2/2/1/2/.Video.md 3/1/2/1/2/2/1/2/_Clip-Film.md 3/1/2/1/2/2/1/_Talk-Show.md 3/1/2/1/2/2/2/.Discussion.md 3/1/2/1/2/2/2/1/.Q&A.md 3/1/2/1/2/2/2/1/1/.Poll.md 3/1/2/1/2/2/2/1/1/_Choose-Vote.md 3/1/2/1/2/2/2/1/2/.Forum.md 3/1/2/1/2/2/2/1/2/_Discuss-Conclusion.md 3/1/2/1/2/2/2/1/_Inquire-Respond.md 3/1/2/1/2/2/2/2/.Debate.md 3/1/2/1/2/2/2/2/_Argue-Defend.md 3/1/2/1/2/2/2/_Ask-Answer.md 3/1/2/1/2/2/_Listen-Engage.md 3/1/2/1/2/3/.Simulation.md Reality.md" Model.md" 3/1/2/1/2/3/1/1/1/.Anatomy.md 3/1/2/1/2/3/1/1/1/_Part-Whole.md 3/1/2/1/2/3/1/1/2/.Landscape.md 3/1/2/1/2/3/1/1/2/_Terrain-Feature.md 3/1/2/1/2/3/1/1/_Object-Space.md Scene.md" 3/1/2/1/2/3/1/2/_Scene-Setting.md 3/1/2/1/2/3/1/_Digital-Physical.md Play.md" 3/1/2/1/2/3/2/1/.Character.md 3/1/2/1/2/3/2/1/1/.Heroine.md 3/1/2/1/2/3/2/1/1/_Lead-Support.md 3/1/2/1/2/3/2/1/2/.Twist.md 3/1/2/1/2/3/2/1/2/_Change-Constant.md 3/1/2/1/2/3/2/1/_Hero-Villain.md 3/1/2/1/2/3/2/2/.Plot.md 3/1/2/1/2/3/2/2/_Start-End.md 3/1/2/1/2/3/2/_Scenario-Action.md 3/1/2/1/2/3/_Pretend-Realize.md 3/1/2/1/2/_Practical-Theoretical.md Styles.md" 3/1/2/1/3/1/.Visual.md 3/1/2/1/3/1/1/.Diagram.md 3/1/2/1/3/1/1/1/.Flowchart.md 3/1/2/1/3/1/1/1/1/.Graph.md 3/1/2/1/3/1/1/1/1/_Data-Interpret.md Break.md" 3/1/2/1/3/1/1/1/2/_Pause-Continue.md 3/1/2/1/3/1/1/1/_Process-Outcome.md 3/1/2/1/3/1/1/2/.Textbook.md 3/1/2/1/3/1/1/2/_Page-Chapter.md 3/1/2/1/3/1/1/_Chart-Graph.md 3/1/2/1/3/1/2/.Reading.md Pattern.md" 3/1/2/1/3/1/2/1/1/.Beatbox.md 3/1/2/1/3/1/2/1/1/_Percussion-Vocal.md 3/1/2/1/3/1/2/1/2/.Narrative.md 3/1/2/1/3/1/2/1/2/_Intro-Body.md 3/1/2/1/3/1/2/1/_Beat-Tempo.md Recording.md" 3/1/2/1/3/1/2/2/_Pause-Play.md 3/1/2/1/3/1/2/_Book-Article.md 3/1/2/1/3/1/_Image-Text.md 3/1/2/1/3/2/.Auditory.md 3/1/2/1/3/2/1/.Music.md 3/1/2/1/3/2/1/1/.Song.md 3/1/2/1/3/2/1/1/1/.Chant.md 3/1/2/1/3/2/1/1/1/_Repetition-Variation.md 3/1/2/1/3/2/1/1/2/.Tale.md 3/1/2/1/3/2/1/1/2/_Start-Finish.md 3/1/2/1/3/2/1/1/_Chorus-Verse.md Story.md" 3/1/2/1/3/2/1/2/_Beginning-Climax.md 3/1/2/1/3/2/1/_Melody-Rhythm.md 3/1/2/1/3/2/2/.Speech.md 3/1/2/1/3/2/2/1/.Phoneme.md 3/1/2/1/3/2/2/1/1/.Syllable.md 3/1/2/1/3/2/2/1/1/_Breakdown-Combine.md 3/1/2/1/3/2/2/1/2/.Word.md 3/1/2/1/3/2/2/1/2/_Phrase-Sentence.md 3/1/2/1/3/2/2/1/_Sound-Letter.md 3/1/2/1/3/2/2/2/.Morpheme.md 3/1/2/1/3/2/2/2/_Meaning-Structure.md 3/1/2/1/3/2/2/_Word-Sentence.md 3/1/2/1/3/2/_Speak-Hear.md 3/1/2/1/3/3/.Kinesthetic.md 3/1/2/1/3/3/1/.Hands-on.md 3/1/2/1/3/3/1/1/.Crafting.md 3/1/2/1/3/3/1/1/1/.Pottery.md 3/1/2/1/3/3/1/1/1/_Mold-Shape.md 3/1/2/1/3/3/1/1/2/.Waltz.md 3/1/2/1/3/3/1/1/2/_Turn-Flow.md 3/1/2/1/3/3/1/1/_Tool-Material.md 3/1/2/1/3/3/1/2/.Dancing.md 3/1/2/1/3/3/1/2/_Step-Sequence.md 3/1/2/1/3/3/1/_Build-Create.md 3/1/2/1/3/3/2/.Movement.md Pace.md" 3/1/2/1/3/3/2/1/1/.Amble.md 3/1/2/1/3/3/2/1/1/_Casual-Urgent.md 3/1/2/1/3/3/2/1/2/.Lunge.md 3/1/2/1/3/3/2/1/2/_Stretch-Leap.md 3/1/2/1/3/3/2/1/_Slow-Quick.md Stride.md" 3/1/2/1/3/3/2/2/_Jog-Sprint.md 3/1/2/1/3/3/2/_Walk-Run.md 3/1/2/1/3/3/_Do-Feel.md 3/1/2/1/3/_Visual-Auditory.md 3/1/2/1/_Theory-Practice.md Systems.md" 3/1/2/2/1/.Democracy.md 3/1/2/2/1/2/.Autocracy.md 3/1/2/2/1/3/.Oligarchy.md 3/1/2/2/1/_Authority-Sovereignty.md 3/1/2/2/2/3/2/.Capitalism.md 3/1/2/2/2/_Federal-Unitary.md 3/1/2/2/3/3/4/.Socialism.md 3/1/2/2/3/_Majority-Minority.md 3/1/2/2/_Centralized-Decentralized.md 3/1/2/3/.Ideologies.md 3/1/2/3/1/.Liberalism.md 3/1/2/3/1/1/.Conservatism.md 3/1/2/3/1/1/2/.Fascism.md 3/1/2/3/1/1/3/.Communism.md 3/1/2/3/1/3/.Socialism.md 3/1/2/3/1/_Rights-Liberties.md 3/1/2/3/2/.Socio-economics.md Theories.md" 3/1/2/3/3/_Monarchy-Democracy.md 3/1/2/3/_Liberalism-Totalitarianism.md 3/1/2/_Conservative-Revolutionary.md 3/2/.Hacking.md

---
## [c0ntradicti0n/dialectics](https://github.com/c0ntradicti0n/dialectics)@[e29be3fbd4...](https://github.com/c0ntradicti0n/dialectics/commit/e29be3fbd465be14d095f9173186ebeac9668742)
#### Friday 2023-08-18 02:57:17 by c0ntradicti0n

Automated TEXT Commit: .idea/workspace.xml 2/2/.Values.md 2/2/1/1/.Ethics.md Qualities.md" 2/2/1/1/1/1/.Character.md 2/2/1/1/1/2/.Integrity.md 2/2/1/1/1/3/.Honor.md Metrics.md" 2/2/1/1/2/1/.Outcome.md 2/2/1/1/2/2/.Utility.md 2/2/1/1/2/3/.Happiness.md Boundaries.md" 2/2/1/1/3/1/.Duty.md 2/2/1/1/3/2/.Principle.md 2/2/1/1/3/3/.Law.md 2/2/1/1/3/_Obligation-Choice.md 2/2/1/1/_Righteous-Wicked.md 2/2/1/2/.Beauty.md 2/2/1/2/2/.Aesthetics.md 2/2/1/2/2/1/.Beauty.md 2/2/1/2/2/1/1/.Consequentialism.md 2/2/1/2/2/1/2/.Taste.md 2/2/1/2/2/1/2/1/.Pleasure.md 2/2/1/2/2/1/2/2/.Attraction.md 2/2/1/2/2/1/2/3/.Delight.md 2/2/1/2/2/1/2/_Attractive-Repulsive.md 2/2/1/2/2/1/3/.Deontology.md 2/2/1/2/2/1/_Ugly-Beautiful.md 2/2/1/2/2/2/.Ugliness.md 2/2/1/2/2/2/1/.Taste.md 2/2/1/2/2/2/2/.Defense.md light'.md" light'.md" spectrum'.md" Elements'.md" Compounds'.md" Reactions'.md" 2/2/1/2/2/2/3/.Sublime.md 2/2/1/2/2/2/_Hate-Love.md 2/2/1/2/2/3/.Sublime.md Reasoning.md" 2/2/1/2/2/3/2/.Attraction.md 2/2/1/2/2/3/2/1/.Temptation.md 2/2/1/2/2/3/2/2/.Longing.md 2/2/1/2/2/3/2/3/.Desire.md 2/2/1/2/2/3/2/_Attraction-Rejection.md Reasoning.md" 2/2/1/2/2/3/_Fear-Desire.md 2/2/1/2/2/_Fear-Desire.md Fallacies.md" Errors.md" Consequent.md" Antecedent.md" Fallacy.md" Errors.md" Hominem.md" 2/2/1/2/3/2/2/.Strawman.md Authority.md" Skews.md" Bias.md" 2/2/1/2/3/3/2/.Anchoring.md Bias.md" 2/2/1/2/3/3/_Perception-Judgment.md 2/2/1/2/3/_Flawed-Valid.md 2/2/1/3/.Truth.md Analysis.md" Types.md" 2/2/1/3/1/1/1/.Inductive.md 2/2/1/3/1/1/2/.Deductive.md 2/2/1/3/1/1/3/.Abductive.md 2/2/1/3/1/1/_General-Specific.md 2/2/1/3/1/_Bias-Neutral.md Inquiry.md" Method.md" 2/2/1/3/2/1/1/.Observation.md 2/2/1/3/2/1/2/.Test.md 2/2/1/3/2/1/3/.Interpretation.md 2/2/1/3/2/1/_Doubt-Certainty.md 2/2/1/3/2/2/.Epistemology.md 2/2/1/3/2/3/.Metaphysics.md 2/2/1/3/2/_Hypothesis-Theory.md Approximation.md" Methods.md" 2/2/1/3/3/1/1/.Observation.md 2/2/1/3/3/1/2/.Experiment.md 2/2/1/3/3/1/3/.Data.md Methods.md" 2/2/1/3/3/2/1/.Reason.md 2/2/1/3/3/2/2/.Logic.md 2/2/1/3/3/2/3/.Principles.md Structure.md" 2/2/1/3/3/3/1/.Belief.md 2/2/1/3/3/3/2/.Knowledge.md 2/2/1/3/3/3/3/.Wisdom.md 2/2/1/3/3/3/_Opinion-Fact.md 2/2/1/3/3/_Induction-Deduction.md Know.md" 2/2/2/_Good-Bad.md 2/2/3/_Right-Wrong.md values.md" 2/3/1/1/1/.Innovation.md 2/3/1/1/1/1/.Idea.md 2/3/1/1/1/2/.Prototype.md 2/3/1/1/1/3/.Product.md 2/3/1/1/1/_Discovery-Invention.md 2/3/1/1/2/.Judgments.md 2/3/1/1/2/1/.Criteria.md 2/3/1/1/2/2/.Evaluation.md 2/3/1/1/2/3/.Conclusion.md 2/3/1/1/2/_Standard-Deviation.md 2/3/1/1/3/.Responsibilities.md 2/3/1/1/3/1/.Obligation.md 2/3/1/1/3/2/.Accountability.md 2/3/1/1/3/3/.Stewardship.md 2/3/1/1/3/_Duty-Freedom.md 2/3/1/1/_Creator-Creation.md 2/3/1/3/1/.Activity.md 2/3/1/3/1/1/.Work.md 2/3/1/3/1/2/.Play.md 2/3/1/3/1/3/.Hobby.md 2/3/1/3/1/_Labor-Leisure.md 2/3/1/3/2/.Efficiency.md 2/3/1/3/2/1/.Production.md 2/3/1/3/2/2/.Distribution.md 2/3/1/3/2/3/.Consumption.md 2/3/1/3/2/_Fast-Slow.md 2/3/1/3/3/.Sanitation.md Purification.md" Management.md" Quality.md" 2/3/1/3/3/_Clean-Contaminated.md 3/1/1/.Communication.md 3/1/1/1/.Linguistics.md 3/1/1/1/1/.Phonetics.md Elements.md" 3/1/1/1/1/1/1/.Consonants.md 3/1/1/1/1/1/2/.Vowels.md 3/1/1/1/1/1/3/.Tones.md 3/1/1/1/1/1/_Silence-Sound.md Properties.md" Articulation.md" Articulation.md" 3/1/1/1/1/2/3/.Voice.md Properties.md" 3/1/1/1/1/3/1/.Amplitude.md 3/1/1/1/1/3/2/.Frequency.md 3/1/1/1/1/3/3/.Timbre.md 3/1/1/1/1/3/_Noise-Harmony.md 3/1/1/1/1/_Articulation-Acoustics.md 3/1/1/1/2/.Syntax.md 3/1/1/1/2/1/.Morphology.md 3/1/1/1/2/1/1/.Root.md 3/1/1/1/2/1/2/.Affix.md 3/1/1/1/2/1/3/.Compound.md 3/1/1/1/2/1/_Word-Phrase.md 3/1/1/1/2/2/.Grammar.md 3/1/1/1/2/2/1/.Tense.md 3/1/1/1/2/2/2/.Aspect.md 3/1/1/1/2/2/3/.Mood.md 3/1/1/1/2/2/_Rule-Variation.md Structure.md" Sentence.md" Sentence.md" Sentence.md" 3/1/1/1/2/3/_Clause-Phrase.md 3/1/1/1/2/_Structure-Function.md 3/1/1/1/3/.Pragmatics.md Acts.md" 3/1/1/1/3/1/1/.Assertive.md 3/1/1/1/3/1/2/.Directive.md 3/1/1/1/3/1/3/.Commissive.md 3/1/1/1/3/1/_Intent-Interpretation.md 3/1/1/1/3/2/.Deixis.md Deixis.md" Deixis.md" Deixis.md" 3/1/1/1/3/2/_Here-There.md 3/1/1/1/3/3/.Implicature.md 3/1/1/1/3/3/1/.Conventional.md 3/1/1/1/3/3/2/.Conversational.md 3/1/1/1/3/3/3/.Scalar.md 3/1/1/1/3/3/_Explicit-Implicit.md 3/1/1/1/3/_Context-Meaning.md 3/1/1/1/_Form-Function.md Theory.md" 3/1/1/2/1/.Rhythm.md 3/1/1/2/1/1/.Beat.md 3/1/1/2/1/1/1/.Onset.md 3/1/1/2/1/1/1/1/.Attack.md 3/1/1/2/1/1/1/1/1/.Start.md 3/1/1/2/1/1/1/1/1/1/.Onset.md 3/1/1/2/1/1/1/1/1/2/.Initiation.md 3/1/1/2/1/1/1/1/1/3/.Commencement.md 3/1/1/2/1/1/1/1/1/_Alpha-Omega.md 3/1/1/2/1/1/1/1/2/.Rise.md 3/1/1/2/1/1/1/1/2/1/.Increase.md 3/1/1/2/1/1/1/1/2/2/.Boost.md 3/1/1/2/1/1/1/1/2/3/.Amplify.md 3/1/1/2/1/1/1/1/2/_Ascend-Dive.md 3/1/1/2/1/1/1/1/3/.Peak.md 3/1/1/2/1/1/1/1/3/1/.Summit.md 3/1/1/2/1/1/1/1/3/2/.Zenith.md 3/1/1/2/1/1/1/1/3/3/.Apex.md 3/1/1/2/1/1/1/1/3/_Max-Min.md 3/1/1/2/1/1/1/1/_Instant-Gradual.md 3/1/1/2/1/1/1/2/.Decay.md 3/1/1/2/1/1/1/2/1/.Fall.md 3/1/1/2/1/1/1/2/2/.Diminish.md 3/1/1/2/1/1/1/2/3/.Level.md 3/1/1/2/1/1/1/2/_Decline-Maintain.md 3/1/1/2/1/1/1/3/.Sustain.md 3/1/1/2/1/1/1/3/1/.Prolong.md 3/1/1/2/1/1/1/3/2/.Retain.md 3/1/1/2/1/1/1/3/3/.Extend.md 3/1/1/2/1/1/1/3/_Grip-LetGo.md 3/1/1/2/1/1/1/_Sharp-Soft.md 3/1/1/2/1/1/2/.Accent.md Beat.md" 3/1/1/2/1/1/2/1/1/.Downbeat.md 3/1/1/2/1/1/2/1/1/1/.Thud.md 3/1/1/2/1/1/2/1/1/2/.Impact.md 3/1/1/2/1/1/2/1/1/3/.Strike.md 3/1/1/2/1/1/2/1/1/_Drop-Lift.md 3/1/1/2/1/1/2/1/2/.Accentuation.md 3/1/1/2/1/1/2/1/2/1/.Emphasis.md 3/1/1/2/1/1/2/1/2/2/.Underline.md 3/1/1/2/1/1/2/1/2/3/.Stress.md 3/1/1/2/1/1/2/1/2/_Spotlight-Shadow.md 3/1/1/2/1/1/2/1/3/.Stressor.md 3/1/1/2/1/1/2/1/3/1/.Tension.md 3/1/1/2/1/1/2/1/3/2/.Force.md 3/1/1/2/1/1/2/1/3/3/.Load.md 3/1/1/2/1/1/2/1/3/_Compress-Release.md 3/1/1/2/1/1/2/1/_Highlight-Background.md Beat.md" 3/1/1/2/1/1/2/2/1/.Upbeat.md 3/1/1/2/1/1/2/2/2/.Deemphasis.md 3/1/1/2/1/1/2/2/3/.Lull.md 3/1/1/2/1/1/2/2/_Background-Foreground.md 3/1/1/2/1/1/2/3/.Offbeat.md 3/1/1/2/1/1/2/3/1/.Sync.md 3/1/1/2/1/1/2/3/2/.Mismatch.md 3/1/1/2/1/1/2/3/3/.Displacement.md 3/1/1/2/1/1/2/3/_OutAlign-InAlign.md 3/1/1/2/1/1/2/_Emphasized-Subdued.md 3/1/1/2/1/1/3/.Syncopation.md Beat.md" Beat.md" Beat.md" 3/1/1/2/1/1/3/_Preemptive-Postponed.md 3/1/1/2/1/1/_Predictable-Unpredictable.md 3/1/1/2/1/2/.Meter.md 3/1/1/2/1/2/1/.Duple.md 3/1/1/2/1/2/1/1/.March.md 3/1/1/2/1/2/1/1/1/.Step.md 3/1/1/2/1/2/1/1/2/.Stride.md 3/1/1/2/1/2/1/1/3/.Progression.md 3/1/1/2/1/2/1/1/_Constant-Change.md 3/1/1/2/1/2/1/2/.Polka.md 3/1/1/2/1/2/1/2/1/.Hop.md 3/1/1/2/1/2/1/2/2/.Jump.md 3/1/1/2/1/2/1/2/3/.Skip.md 3/1/1/2/1/2/1/2/_Elevate-Ground.md 3/1/1/2/1/2/1/3/.Tango.md 3/1/1/2/1/2/1/3/1/.Embrace.md 3/1/1/2/1/2/1/3/2/.Stride.md 3/1/1/2/1/2/1/3/3/.Flourish.md 3/1/1/2/1/2/1/3/_Union-Separate.md 3/1/1/2/1/2/1/_Paired-Unpaired.md 3/1/1/2/1/2/2/.Triple.md 3/1/1/2/1/2/2/1/.Waltz.md 3/1/1/2/1/2/2/2/.Mazurka.md 3/1/1/2/1/2/2/3/.Minuet.md 3/1/1/2/1/2/2/_Trio-Solo.md 3/1/1/2/1/2/3/.Complex.md 3/1/1/2/1/2/3/1/.Five-Beat.md 3/1/1/2/1/2/3/2/.Seven-Beat.md 3/1/1/2/1/2/3/3/.Irregular.md 3/1/1/2/1/2/3/_Hybrid-Pure.md 3/1/1/2/1/2/_Even-Odd.md 3/1/1/2/1/3/.Tempo.md 3/1/1/2/1/3/1/.Adagio.md 3/1/1/2/1/3/2/.Andante.md 3/1/1/2/1/3/3/.Allegro.md 3/1/1/2/1/3/_Lethargic-Brisk.md 3/1/1/2/1/_Static-Dynamic.md 3/1/1/2/2/.Harmonics.md 3/1/1/2/2/1/.Frequency.md 3/1/1/2/2/1/1/.Bass.md 3/1/1/2/2/1/1/1/.Sub-Bass.md 3/1/1/2/2/1/1/2/.Bassline.md Midrange.md" 3/1/1/2/2/1/1/_Buried-Apparent.md 3/1/1/2/2/1/2/.Mid.md 3/1/1/2/2/1/2/1/.Middle.md Midrange.md" Treble.md" 3/1/1/2/2/1/2/_Balanced-Unbalanced.md 3/1/1/2/2/1/3/.Treble.md Frequency.md" 3/1/1/2/2/1/3/2/.Brightness.md 3/1/1/2/2/1/3/3/.Sharpness.md 3/1/1/2/2/1/3/_Climax-Nadir.md 3/1/1/2/2/1/_Deep-Shrill.md 3/1/1/2/2/2/.Series.md Harmonic.md" 3/1/1/2/2/2/1/1/.Fundamental.md 3/1/1/2/2/2/1/1/1/.Base.md 3/1/1/2/2/2/1/1/1/1/.Root.md 3/1/1/2/2/2/1/1/1/2/.Ground.md 3/1/1/2/2/2/1/1/1/3/.Bedrock.md 3/1/1/2/2/2/1/1/1/_Origin-Growth.md 3/1/1/2/2/2/1/1/2/.Foundation.md 3/1/1/2/2/2/1/1/2/1/.Base.md 3/1/1/2/2/2/1/1/2/2/.Bottom.md 3/1/1/2/2/2/1/1/2/3/.Underpinning.md 3/1/1/2/2/2/1/1/2/_Start-Build.md 3/1/1/2/2/2/1/1/3/.Groundwork.md 3/1/1/2/2/2/1/1/3/1/.Framework.md 3/1/1/2/2/2/1/1/3/2/.Structure.md 3/1/1/2/2/2/1/1/3/3/.Skeleton.md 3/1/1/2/2/2/1/1/3/_Plan-Outcome.md 3/1/1/2/2/2/1/1/_Start-Expand.md Overtone.md" Harmonic.md" 3/1/1/2/2/2/1/2/2/.Deviation.md 3/1/1/2/2/2/1/2/3/.Variation.md 3/1/1/2/2/2/1/2/_Follow-Origin.md Overtone.md" Harmonic.md" 3/1/1/2/2/2/1/3/2/.Deviant.md 3/1/1/2/2/2/1/3/3/.Modifier.md 3/1/1/2/2/2/1/3/_Overlay-Origin.md 3/1/1/2/2/2/1/_Root-Branch.md Harmonic.md" Overtone.md" Harmonic.md" Harmonic.md" 3/1/1/2/2/2/2/_Sheet-Underneath.md Harmonics.md" Overtone.md" Overtone.md" Overtone.md" 3/1/1/2/2/2/3/_Principal-Auxiliary.md 3/1/1/2/2/2/_Base-Overtones.md 3/1/1/2/2/3/.Timbre.md 3/1/1/2/2/3/1/.Sinewave.md Wave.md" State.md" 3/1/1/2/2/3/1/1/1/1/.Unchanging.md 3/1/1/2/2/3/1/1/1/2/.Constant.md 3/1/1/2/2/3/1/1/1/3/.Fixed.md 3/1/1/2/2/3/1/1/1/_Same-Change.md 3/1/1/2/2/3/1/1/2/.Plain.md 3/1/1/2/2/3/1/1/2/1/.Unembellished.md 3/1/1/2/2/3/1/1/2/2/.Basic.md 3/1/1/2/2/3/1/1/2/3/.Simplistic.md 3/1/1/2/2/3/1/1/2/_Naked-Decorated.md 3/1/1/2/2/3/1/1/3/.Homogeneous.md 3/1/1/2/2/3/1/1/3/1/.Identical.md 3/1/1/2/2/3/1/1/3/2/.Consistent.md 3/1/1/2/2/3/1/1/3/3/.Monolithic.md 3/1/1/2/2/3/1/1/3/_Alike-Different.md 3/1/1/2/2/3/1/1/_Same-Vary.md Wave.md" 3/1/1/2/2/3/1/2/1/.Core.md 3/1/1/2/2/3/1/2/2/.Central.md 3/1/1/2/2/3/1/2/3/.Prime.md 3/1/1/2/2/3/1/2/_Main-Secondary.md Wave.md" 3/1/1/2/2/3/1/3/1/.Clean.md 3/1/1/2/2/3/1/3/2/.Pure.md 3/1/1/2/2/3/1/3/3/.Transparent.md 3/1/1/2/2/3/1/3/_Distinct-Blur.md 3/1/1/2/2/3/1/_Clean-Blended.md 3/1/1/2/2/3/2/.Sawtooth.md Wave.md" 3/1/1/2/2/3/2/1/1/.Rough.md 3/1/1/2/2/3/2/1/2/.Irregular.md 3/1/1/2/2/3/2/1/3/.Zigzag.md 3/1/1/2/2/3/2/1/_Rugged-Smooth.md Wave.md" 3/1/1/2/2/3/2/2/1/.Vibration.md 3/1/1/2/2/3/2/2/2/.Pulse.md 3/1/1/2/2/3/2/2/3/.Echo.md 3/1/1/2/2/3/2/2/_Ring-Silent.md Wave.md" 3/1/1/2/2/3/2/3/1/.Dense.md 3/1/1/2/2/3/2/3/2/.Layered.md 3/1/1/2/2/3/2/3/3/.Thick.md 3/1/1/2/2/3/2/3/_Saturated-Vacant.md 3/1/1/2/2/3/2/_Edgy-Sleek.md 3/1/1/2/2/3/3/.Squarewave.md Cycle.md" Pulse.md" Wave.md" 3/1/1/2/2/3/3/_Symmetric-Asymmetric.md 3/1/1/2/2/3/_Clean-Distorted.md 3/1/1/2/2/_Simple-Rich.md 3/1/1/2/3/.Timing.md 3/1/1/2/3/1/.Duration.md 3/1/1/2/3/1/1/.Instant.md 3/1/1/2/3/1/1/1/.Second.md 3/1/1/2/3/1/1/1/1/.Milliseconds.md 3/1/1/2/3/1/1/1/1/_Brief-Extended.md 3/1/1/2/3/1/1/1/2/.Moments.md 3/1/1/2/3/1/1/1/2/_Glimpse-Span.md 3/1/1/2/3/1/1/1/_Tick-Tock.md 3/1/1/2/3/1/1/2/.Minute.md 3/1/1/2/3/1/1/2/1/.Countdown.md 3/1/1/2/3/1/1/2/1/_Start-Stop.md 3/1/1/2/3/1/1/2/2/.Timer.md 3/1/1/2/3/1/1/2/2/_Set-Elapsed.md 3/1/1/2/3/1/1/2/_Wait-Proceed.md 3/1/1/2/3/1/1/_Moment-Decade.md 3/1/1/2/3/1/2/.Eternity.md 3/1/1/2/3/1/2/1/.Decade.md 3/1/1/2/3/1/2/1/1/.1970s.md 3/1/1/2/3/1/2/1/1/_Retro-Modern.md 3/1/1/2/3/1/2/1/2/.1980s.md 3/1/1/2/3/1/2/1/2/_Classic-Contemporary.md 3/1/1/2/3/1/2/1/_Past-Future.md 3/1/1/2/3/1/2/2/.Century.md 3/1/1/2/3/1/2/2/1/.20th.md 3/1/1/2/3/1/2/2/1/_Industrial-Digital.md 3/1/1/2/3/1/2/2/2/.21st.md 3/1/1/2/3/1/2/2/2/_Internet-AI.md 3/1/1/2/3/1/2/2/_Aeon-Age.md 3/1/1/2/3/1/2/_Ephemeral-Endless.md 3/1/1/2/3/1/_Short-Long.md 3/1/1/2/3/2/.Chronology.md 3/1/1/2/3/2/1/.History.md 3/1/1/2/3/2/1/1/.Epoch.md 3/1/1/2/3/2/1/1/_Birth-End.md 3/1/1/2/3/2/1/2/.Era.md 3/1/1/2/3/2/1/2/_Beginning-Completion.md 3/1/1/2/3/2/1/_Yesterday-Tomorrow.md 3/1/1/2/3/2/2/.Forecast.md 3/1/1/2/3/2/2/1/.Weather.md 3/1/1/2/3/2/2/1/_Cloud-Sun.md 3/1/1/2/3/2/2/2/.Trend.md 3/1/1/2/3/2/2/2/_Rise-Fall.md 3/1/1/2/3/2/2/_Prediction-Reality.md 3/1/1/2/3/2/_Past-Future.md 3/1/1/2/3/3/.Sync.md 3/1/1/2/3/3/1/.Alignment.md 3/1/1/2/3/3/1/1/.Melody.md 3/1/1/2/3/3/1/1/1/.Chord.md 3/1/1/2/3/3/1/1/1/_Harmony-Disharmony.md 3/1/1/2/3/3/1/1/2/.Scale.md 3/1/1/2/3/3/1/1/2/_Ascending-Descending.md 3/1/1/2/3/3/1/1/_Tune-Note.md 3/1/1/2/3/3/1/2/.Rhythm.md 3/1/1/2/3/3/1/2/1/.Pulse.md 3/1/1/2/3/3/1/2/1/_Steady-Vary.md 3/1/1/2/3/3/1/2/2/.Metronome.md 3/1/1/2/3/3/1/2/2/_Regular-Irregular.md 3/1/1/2/3/3/1/2/_Beat-Pause.md 3/1/1/2/3/3/1/_Harmony-Discord.md 3/1/1/2/3/3/2/.Lag.md 3/1/1/2/3/3/2/1/.Delay.md 3/1/1/2/3/3/2/1/_Wait-Rush.md 3/1/1/2/3/3/2/2/.Haste.md 3/1/1/2/3/3/2/2/_Speedy-Slow.md 3/1/1/2/3/3/2/_Before-After.md 3/1/1/2/3/3/_Synchronized-Asynchronous.md 3/1/1/2/3/_Predictability-Unpredictability.md 3/1/1/2/_Tension-Release.md Relation.md" 3/1/1/3/1/.Sociology.md 3/1/1/3/1/1/.Friendship.md 3/1/1/3/1/2/.Competitive.md 3/1/1/3/1/3/.Cooperative.md 3/1/1/3/1/_Individual-Society.md Structures.md" 3/1/1/3/2/1/.Stratification.md 3/1/1/3/2/1/1/.Class.md 3/1/1/3/2/1/2/.Status.md 3/1/1/3/2/1/3/.Power.md 3/1/1/3/2/2/.Community.md Movements.md" 3/1/1/3/2/3/.Society.md Patterns.md" 3/1/1/3/2/_Inequality-Equality.md 3/1/1/3/3/.Dialogue.md 3/1/1/3/3/1/.Conversation.md 3/1/1/3/3/1/1/.Chat.md 3/1/1/3/3/1/1/1/.Greeting.md 3/1/1/3/3/1/1/1/1/.Salute.md 3/1/1/3/3/1/1/1/1/_Formal-Casual.md 3/1/1/3/3/1/1/1/2/.Wave.md 3/1/1/3/3/1/1/1/2/_Visible-Invisible.md 3/1/1/3/3/1/1/1/_Hello-Bye.md 3/1/1/3/3/1/1/2/.Farewell.md 3/1/1/3/3/1/1/2/1/.Goodbye.md 3/1/1/3/3/1/1/2/1/_Temporary-Permanent.md 3/1/1/3/3/1/1/2/2/.Adieu.md 3/1/1/3/3/1/1/2/2/_Definite-Indefinite.md 3/1/1/3/3/1/1/2/_Start-End.md 3/1/1/3/3/1/1/_Casual-Formal.md 3/1/1/3/3/1/2/.Interview.md 3/1/1/3/3/1/2/1/.Query.md 3/1/1/3/3/1/2/1/1/.Inquiry.md 3/1/1/3/3/1/2/1/1/_General-Specific.md 3/1/1/3/3/1/2/1/2/.Prompt.md 3/1/1/3/3/1/2/1/2/_Lead-Direct.md 3/1/1/3/3/1/2/1/_Ask-Tell.md 3/1/1/3/3/1/2/2/.Reply.md 3/1/1/3/3/1/2/2/1/.Answer.md 3/1/1/3/3/1/2/2/1/_Brief-Detailed.md 3/1/1/3/3/1/2/2/2/.Explanation.md 3/1/1/3/3/1/2/2/2/_Surface-Depth.md 3/1/1/3/3/1/2/2/_Respond-Elaborate.md 3/1/1/3/3/1/2/_Question-Answer.md 3/1/1/3/3/1/_Spontaneity-Structure.md 3/1/1/3/3/2/.Monologue.md 3/1/1/3/3/2/1/.Soliloquy.md 3/1/1/3/3/2/1/1/.Thought.md 3/1/1/3/3/2/1/1/_Silent-Vocal.md 3/1/1/3/3/2/1/2/.Speech.md 3/1/1/3/3/2/1/2/_Public-Private.md 3/1/1/3/3/2/1/_Inner-Outer.md 3/1/1/3/3/2/2/.Narrative.md 3/1/1/3/3/2/2/1/.Tale.md 3/1/1/3/3/2/2/1/_Fiction-Reality.md 3/1/1/3/3/2/2/2/.Exposition.md 3/1/1/3/3/2/2/2/_Breakdown-Overview.md 3/1/1/3/3/2/2/_Story-Analysis.md 3/1/1/3/3/2/_Self-Other.md 3/1/1/3/3/3/.Debate.md 3/1/1/3/3/3/1/.Discussion.md 3/1/1/3/3/3/1/1/.Agreement.md 3/1/1/3/3/3/1/1/1/.Consensus.md 3/1/1/3/3/3/1/1/1/_Together-Apart.md 3/1/1/3/3/3/1/1/2/.Unison.md 3/1/1/3/3/3/1/1/2/_One-Many.md 3/1/1/3/3/3/1/1/_Yes-No.md 3/1/1/3/3/3/1/2/.Conflict.md 3/1/1/3/3/3/1/2/1/.Dispute.md 3/1/1/3/3/3/1/2/1/_Quarrel-Settle.md 3/1/1/3/3/3/1/2/2/.Contest.md 3/1/1/3/3/3/1/2/2/_Compete-Cooperate.md 3/1/1/3/3/3/1/2/_For-Against.md 3/1/1/3/3/3/1/_Understanding-Misunderstanding.md 3/1/1/3/3/3/2/.Argument.md 3/1/1/3/3/3/2/1/.Support.md 3/1/1/3/3/3/2/1/_Evidence-Claim.md 3/1/1/3/3/3/2/2/.Opposition.md 3/1/1/3/3/3/2/2/_Rebuttal-Counter.md 3/1/1/3/3/3/2/_Pro-Con.md 3/1/1/3/3/3/_Agree-Disagree.md 3/1/1/3/3/_Speaker-Listener.md 3/1/1/3/_Conflict-Resolution.md 3/1/1/_Verbal-Nonverbal.md 3/1/3/.Technics 3/1/3/1/.Computers.md 3/1/3/1/1/.Hardware.md 3/1/3/1/2/.Software.md 3/1/3/1/3/.Embedded.md 3/1/3/2/.Hacking.md

---
## [c0ntradicti0n/dialectics](https://github.com/c0ntradicti0n/dialectics)@[bc0507b420...](https://github.com/c0ntradicti0n/dialectics/commit/bc0507b4201f862e56d58997c5223f3213d38efe)
#### Friday 2023-08-18 02:57:17 by c0ntradicti0n

Automated TEXT Commit: Use.md" 3/1/2/.Hacking.md Structures.md" 3/2/1/.Education.md Process.md" 3/2/1/1/1/.Knowledge.md 3/2/1/1/2/.Skills.md 3/2/1/1/3/.Implementation.md 3/2/1/1/_Learning-Application.md Methods.md" Learning.md" Activity.md" 3/2/1/2/1/1/1/.Laboratory.md 3/2/1/2/1/1/1/1/.Experiment.md 3/2/1/2/1/1/1/1/_Test-Result.md 3/2/1/2/1/1/1/2/.Observation.md 3/2/1/2/1/1/1/2/_Watch-Note.md 3/2/1/2/1/1/1/_Inside-Outside.md Trip.md" 3/2/1/2/1/1/2/_Local-Travel.md 3/2/1/2/1/1/_Practice-Review.md 3/2/1/2/1/2/.Reflection.md 3/2/1/2/1/2/1/.Journaling.md 3/2/1/2/1/2/1/1/.Diary.md 3/2/1/2/1/2/1/1/_Private-Public.md Review.md" 3/2/1/2/1/2/1/2/_Judge-Critique.md 3/2/1/2/1/2/1/_Write-Review.md 3/2/1/2/1/2/2/.Feedback.md 3/2/1/2/1/2/2/_Give-Receive.md 3/2/1/2/1/2/_Think-Record.md 3/2/1/2/1/_Doing-Observing.md 3/2/1/2/2/.Lecture.md 3/2/1/2/2/1/.Presentation.md 3/2/1/2/2/1/1/.Slide.md 3/2/1/2/2/1/1/1/.Photo.md 3/2/1/2/2/1/1/1/_Static-Dynamic.md 3/2/1/2/2/1/1/2/.Animation.md 3/2/1/2/2/1/1/2/_Frame-Play.md 3/2/1/2/2/1/1/_Still-Motion.md 3/2/1/2/2/1/2/.Video.md 3/2/1/2/2/1/2/_Clip-Film.md 3/2/1/2/2/1/_Talk-Show.md 3/2/1/2/2/2/.Discussion.md 3/2/1/2/2/2/1/.Q&A.md 3/2/1/2/2/2/1/1/.Poll.md 3/2/1/2/2/2/1/1/_Choose-Vote.md 3/2/1/2/2/2/1/2/.Forum.md 3/2/1/2/2/2/1/2/_Discuss-Conclusion.md 3/2/1/2/2/2/1/_Inquire-Respond.md 3/2/1/2/2/2/2/.Debate.md 3/2/1/2/2/2/2/_Argue-Defend.md 3/2/1/2/2/2/_Ask-Answer.md 3/2/1/2/2/_Listen-Engage.md 3/2/1/2/3/.Simulation.md Reality.md" Model.md" 3/2/1/2/3/1/1/1/.Anatomy.md 3/2/1/2/3/1/1/1/_Part-Whole.md 3/2/1/2/3/1/1/2/.Landscape.md 3/2/1/2/3/1/1/2/_Terrain-Feature.md 3/2/1/2/3/1/1/_Object-Space.md Scene.md" 3/2/1/2/3/1/2/_Scene-Setting.md 3/2/1/2/3/1/_Digital-Physical.md Play.md" 3/2/1/2/3/2/1/.Character.md 3/2/1/2/3/2/1/1/.Heroine.md 3/2/1/2/3/2/1/1/_Lead-Support.md 3/2/1/2/3/2/1/2/.Twist.md 3/2/1/2/3/2/1/2/_Change-Constant.md 3/2/1/2/3/2/1/_Hero-Villain.md 3/2/1/2/3/2/2/.Plot.md 3/2/1/2/3/2/2/_Start-End.md 3/2/1/2/3/2/_Scenario-Action.md 3/2/1/2/3/_Pretend-Realize.md 3/2/1/2/_Practical-Theoretical.md Styles.md" 3/2/1/3/1/.Visual.md 3/2/1/3/1/1/.Diagram.md 3/2/1/3/1/1/1/.Flowchart.md 3/2/1/3/1/1/1/1/.Graph.md 3/2/1/3/1/1/1/1/_Data-Interpret.md Break.md" 3/2/1/3/1/1/1/2/_Pause-Continue.md 3/2/1/3/1/1/1/_Process-Outcome.md 3/2/1/3/1/1/2/.Textbook.md 3/2/1/3/1/1/2/_Page-Chapter.md 3/2/1/3/1/1/_Chart-Graph.md 3/2/1/3/1/2/.Reading.md Pattern.md" 3/2/1/3/1/2/1/1/.Beatbox.md 3/2/1/3/1/2/1/1/_Percussion-Vocal.md 3/2/1/3/1/2/1/2/.Narrative.md 3/2/1/3/1/2/1/2/_Intro-Body.md 3/2/1/3/1/2/1/_Beat-Tempo.md Recording.md" 3/2/1/3/1/2/2/_Pause-Play.md 3/2/1/3/1/2/_Book-Article.md 3/2/1/3/1/_Image-Text.md 3/2/1/3/2/.Auditory.md 3/2/1/3/2/1/.Music.md 3/2/1/3/2/1/1/.Song.md 3/2/1/3/2/1/1/1/.Chant.md 3/2/1/3/2/1/1/1/_Repetition-Variation.md 3/2/1/3/2/1/1/2/.Tale.md 3/2/1/3/2/1/1/2/_Start-Finish.md 3/2/1/3/2/1/1/_Chorus-Verse.md Story.md" 3/2/1/3/2/1/2/_Beginning-Climax.md 3/2/1/3/2/1/_Melody-Rhythm.md 3/2/1/3/2/2/.Speech.md 3/2/1/3/2/2/1/.Phoneme.md 3/2/1/3/2/2/1/1/.Syllable.md 3/2/1/3/2/2/1/1/_Breakdown-Combine.md 3/2/1/3/2/2/1/2/.Word.md 3/2/1/3/2/2/1/2/_Phrase-Sentence.md 3/2/1/3/2/2/1/_Sound-Letter.md 3/2/1/3/2/2/2/.Morpheme.md 3/2/1/3/2/2/2/_Meaning-Structure.md 3/2/1/3/2/2/_Word-Sentence.md 3/2/1/3/2/_Speak-Hear.md 3/2/1/3/3/.Kinesthetic.md 3/2/1/3/3/1/.Hands-on.md 3/2/1/3/3/1/1/.Crafting.md 3/2/1/3/3/1/1/1/.Pottery.md 3/2/1/3/3/1/1/1/_Mold-Shape.md 3/2/1/3/3/1/1/2/.Waltz.md 3/2/1/3/3/1/1/2/_Turn-Flow.md 3/2/1/3/3/1/1/_Tool-Material.md 3/2/1/3/3/1/2/.Dancing.md 3/2/1/3/3/1/2/_Step-Sequence.md 3/2/1/3/3/1/_Build-Create.md 3/2/1/3/3/2/.Movement.md Pace.md" 3/2/1/3/3/2/1/1/.Amble.md 3/2/1/3/3/2/1/1/_Casual-Urgent.md 3/2/1/3/3/2/1/2/.Lunge.md 3/2/1/3/3/2/1/2/_Stretch-Leap.md 3/2/1/3/3/2/1/_Slow-Quick.md Stride.md" 3/2/1/3/3/2/2/_Jog-Sprint.md 3/2/1/3/3/2/_Walk-Run.md 3/2/1/3/3/_Do-Feel.md 3/2/1/3/_Visual-Auditory.md 3/2/1/_Theory-Practice.md Systems.md" 3/2/2/1/.Democracy.md 3/2/2/1/2/.Autocracy.md 3/2/2/1/3/.Oligarchy.md 3/2/2/1/_Authority-Sovereignty.md 3/2/2/2/3/2/.Capitalism.md 3/2/2/2/_Federal-Unitary.md 3/2/2/3/3/4/.Socialism.md 3/2/2/3/_Majority-Minority.md 3/2/2/_Centralized-Decentralized.md 3/2/3/.Ideologies.md 3/2/3/1/.Liberalism.md 3/2/3/1/1/.Conservatism.md 3/2/3/1/1/2/.Fascism.md 3/2/3/1/1/3/.Communism.md 3/2/3/1/3/.Socialism.md 3/2/3/1/_Rights-Liberties.md 3/2/3/2/.Socio-economics.md Theories.md" 3/2/3/3/_Monarchy-Democracy.md 3/2/3/_Liberalism-Totalitarianism.md 3/2/_Conservative-Revolutionary.md

---
## [shiptest-ss13/Shiptest](https://github.com/shiptest-ss13/Shiptest)@[b033e1ed6a...](https://github.com/shiptest-ss13/Shiptest/commit/b033e1ed6a1e7f87edc73a75a96bcf6536e39aba)
#### Friday 2023-08-18 03:02:45 by Sun-Soaked

Update_Appearance Port (#2170)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
[(original pr)](https://github.com/tgstation/tgstation/pull/55468)
After nine years in development we hope it was worth the wait

I ported this specifically for the signals I'll need for world icons.
However, it had a lot of other useful stuff, so I ended up just grabbing
(almost) the entire pr.
I tried to grab as few of the superfluous code rewrites as possible to
make reviewing a bit easier, but I couldn't help grab stuff like the APC
icon code rewrite(the original code was a war crime).

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

- ports the wrapper proc `update_appearance` for icons, descs, and
names, adds `update_desc` and `update_name` subprocs to handle those.
Things. without just stuffing them into update_icons like some kind of
psychopath

- ports a bunch of signal hooks useful for changing names, descriptions,
and icons. I needed these for world_icons which is where this wild ride
all started

- ports some `base_icon_state` implementation. Stuff like spear code
makes slightly less duplicates(and more sense) now which is nice.
We could definitely implement it more I think but that's a future me
problem

- 500 files of immersive vsc-mass-editing action to implement
`update_appearance()`(sorry in advance, but not as sorry as I was when
manually copy-pasting the custom ones for like 3 straight days)

-"consig" and "comisg" have been taken out behind the codebase and shot.
Not 'technically' a bug it just made my head hurt

-My first pr with 0 player facing changes (confetti)
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: TemporalOroboros, Memed Hams
code: ports update_appearance, update_name, and update_desc from tg, as
well as associated signals
code: a bit of base_icon_state implementation. Can you believe it's been
sitting in our code almost unused for like 3 years
code: cleans up some code formatting, mainly around custom icons and
overlays
code: fixes the typos in COMSIG_STORAGE_EXITED and
COMSIG_STORAGE_ENTERED
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Bjarl/Shiptest](https://github.com/Bjarl/Shiptest)@[d6b460327a...](https://github.com/Bjarl/Shiptest/commit/d6b460327a7faa4580eeef9e4cb9bae6f4c8032f)
#### Friday 2023-08-18 03:15:32 by Bjarl

Merge remote-tracking branch 'upstream/master' into fuck-you

---
## [Ni-Hao-c/NorthstarMods](https://github.com/Ni-Hao-c/NorthstarMods)@[28df512cb5...](https://github.com/Ni-Hao-c/NorthstarMods/commit/28df512cb58ce9071729f4f434eca2c1572c628e)
#### Friday 2023-08-18 03:17:16 by Zanieon

Huge update (See description for full changelog)

Configuration:
- Settings unlocked for local lobby hosting
- Setting that makes the maps wait for a minimum amount of players before starting the waves
- Console variable to allow the use of Smart Pistol as secondary on Easy Mode
- Console variable to setup what Grenade type Grunts can use

Match:
- Frontier Defense Postmatch Summary Menu is restored, it will appear whenever a match ends and returns to lobby if a server allows
- Proper tracking of Titan's Frontier Defense earned experience, allowing them to level up their Aegis ranks
- Dynamic change of Titan/Core Meters based on current players in the match
- If a player as pilot manages to kill 6 or more Titans within a short time (mostly Nuke Rodeos), the server will announce that to all other players
- Droz and Davis will nag to players spend their money at the Store during wave breaks if they have more than 100 Cash
- Proper spawn point rating for when respawning as Titan, players will not drop away from the Harvester anymore as Titan

Maps:
- New Playable Map: Eden
- Angel City Wave Rework to be based off the vanilla spawn amounts
- Boomtown Wave Rework to make waves more consistent with spawn locations and balance
- Drydock: Adjusted where Drones spawns to avoid them making unecessary loops around the Crane area

Live Fire Frontier Defense mode:
- New Playable Maps: Deck, Township, UMA
- Pilot-only gameplay
- 3 Waves with huge amounts of enemies, infantry mostly
- Loadout can be changed at any time during a wave in the Loadout Crates
- Droz and Davis helps players in person by guarding the Harvester
- Players recieve the double amount of money when completing a wave
- Players can have 3 Turrets instead of 2
- Players have no grenades
- Players have limited Anti-Titan ammo, restock possible at Loadout Crate
- Grunts will always have one shield captain in their squads and will always have Anti-Titan weapons
- Stalkers will always spawn with EPG
- Players have a single "public" Titan to use called 'Helper Titan', pilots approaching this Titan gains ownership, staying away clears it

The Helper Titan is:
*A Tone chassis Titan
*Uses XO-16 with Arc Rounds and Faster Reload as primary weapon
*Has basic Dumbfire Missile and Cluster Missile Rack as shoulder mounts
*Has zero-energy Tripwire as utility
*Has basic Salvo Core
*Has passive Shield Regeneration
*Has passive very slow Health Regeneration
*Cannot be rodeoed
*Cannot be disembarked while a wave is active
*Cannot be ordered to follow or guard, it always stays on kneeled position awaiting for a pilot to embark
*If destroyed, it respawns after 2 minutes

AI:
- Cloak Drones will now properly ignore Arc Titans instead of attempting to cloak them
- Mortar Spectres can be hacked if server allows, and they will behave more precisely to vanilla when going into their siege spots
- Grunts will talk about their squadmates being killed or if they are the last person alive in their squad
- Shortened the range where Stalkers starts sprinting at the Harvester from 1800 to 1024 map units
- Sniper Titans will have a better accuracy than normal Titans
- Elite Titans will have grunt pilots inside them

Titans:
- The Shoulder Badge properly updates accordingly to the difficulties played on matches
- Healing back to full health restores the broken parts
- Auto-Titans will ignore friendly fire and AoE's during wave break, this allows Monarch to Electric-Smoke allied Titans without them dodging away

Harvester:
- Properly play the rings start animation when the map starts
- Updates the ring animations when its health reaches 50% and less
- Plays the ring deactivation upon destruction
- Sounds updates accordingly to its health state
- Lightning effects appears in the beam when low health
- The Beam color now reflects more precisely the amount of health it currently have

---
## [nagyist/koreader](https://github.com/nagyist/koreader)@[4acf131071...](https://github.com/nagyist/koreader/commit/4acf131071c704863d0d66f78f1b2314df9c3164)
#### Friday 2023-08-18 03:23:53 by NiLuJe

ReaderActivityIndicator: Oh god, my eyes, they buuuuurn.

Make this a real boy, with a transient lipc handle.
And get rid of the insane 1s sleep on affected ReaderView paints,
because ouchy.

This is completely deprecated anyway, so this is entirely pointless,
and mainly to prevent implementation details from creeping into
reader.lua.

---
## [Sonic121x/Skyrat-tg](https://github.com/Sonic121x/Skyrat-tg)@[d5655c3c55...](https://github.com/Sonic121x/Skyrat-tg/commit/d5655c3c55fab0f4450659947fad1a40043893dc)
#### Friday 2023-08-18 04:50:08 by SkyratBot

[MIRROR] Adds Summon Simians & Buffs/QoLs Mutate [MDB IGNORE] (#22970)

* Adds Summon Simians & Buffs/QoLs Mutate (#77196)

## About The Pull Request

Adds Summon Simians, a spell that summons four monkeys or lesser
gorillas, with the amount increasing per upgrade. The monkeys have
various fun gear depending on how lucky you get and how leveled the
spell is. If the spell is maximum level, it only summons normal
gorillas.

Added further support for nonhuman robed casting: Monkeys, cyborgs, and
drones can all now cast robed spells as long as they're wearing a
wizardly hat as well.

Made monkeys able to wield things again.

Wizard Mutate spell works on non-human races. It also gives you
Gigantism now (funny). If the Race can't support tinted bodyparts, your
whole sprite is temporarily turned green.

Made Laser eyes projectiles a subtype of actual lasers, which has
various properties such as on-hit effects and upping the damage to 30.

Improved some monkey AI code.

## Why It's Good For The Game

> Adds Summon Simians, a spell that summons four monkeys or lesser
gorillas, with the amount increasing per upgrade. The monkeys have
various fun gear depending on how lucky you get and how leveled the
spell is. If the spell is maximum level, it only summons normal
gorillas.

It's criminal we don't have a monky spell, and this is a really fun spin
on it. Total chaos, but total monky chaos. It's surprisingly strong,
but! it can very well backfire if you stay near the angry monkeys too
long and your protection fades away. Unless you become a monkey
yourself!!

> Wizard Mutate spell works on non-human races.

This spell is great but it's hampered by the mutation's human
requirement, which is reasonable in normal gameplay. Wizards don't need
to care about that, and the human restriction hinders a lot of possible
gimmicks, so off it goes. Also, wizard hulk does't cause chunky fingers
for similar reasons

> Made Laser eyes projectiles a subtype of actual lasers, which has
various properties such as on-hit effects and upping the damage to 30.

Don't really caer about the damage so much, this is more so that it has
effects such as on-hit visuals. Can lower the damage if required, but
honestly anything that competes against troll mjolnir is good.

> Added further support for nonhuman robed casting: Monkeys, cyborgs,
and drones can all now cast robed spells as long as they're wearing a
wizardly hat as well.

SS13 is known for 'The Dev Team Thinks of Everything' and I believe this
is a sorely lacking part of this or something. It's funny.
I want to see a monkey wizard.

> Made monkeys able to wield things again.

I really don't know why this was a thing and it was breaking my axe and
spear wielding primal monkeys. Like, why?

## Changelog

:cl:
add: Adds Summon Simians, a spell that summons four monkeys or lesser
gorillas, with the amount increasing per upgrade. The monkeys have
various fun gear depending on how lucky you get and how leveled the
spell is. If the spell is maximum level, it only summons normal
gorillas.
balance: Wizard Mutate spell works on non-human races. It also gives you
Gigantism now (funny). If the Race can't support tinted bodyparts, your
whole sprite is temporarily turned green.
balance: Made Laser eyes projectiles a subtype of actual lasers, which
has various properties such as on-hit effects and upping the damage to
30.
add: Added further support for nonhuman robed casting: Monkeys, cyborgs,
and drones can all now cast robed spells as long as they're wearing a
wizardly hat as well.
balance: Made monkeys able to wield two-handed things again.
/:cl:

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@ users.noreply.github.com>

* Adds Summon Simians & Buffs/QoLs Mutate

* Updates our modular file to take this into account (I hate that this exists)

---------

Co-authored-by: carlarctg <53100513+carlarctg@users.noreply.github.com>
Co-authored-by: MrMelbert <51863163+MrMelbert@ users.noreply.github.com>
Co-authored-by: GoldenAlpharex <jerego1234@hotmail.com>

---
## [Sonic121x/Skyrat-tg](https://github.com/Sonic121x/Skyrat-tg)@[3782e4b710...](https://github.com/Sonic121x/Skyrat-tg/commit/3782e4b71098d12588696d9263f2ee8748caf9bf)
#### Friday 2023-08-18 04:50:08 by Bloop

[MISSED MIRROR] Martian Food: A Taste of the Red Planet (#75988) (#23013)

Martian Food: A Taste of the Red Planet (#75988)

## About The Pull Request
Adds a selection of new foods and drinks based around Mars.
More information on Mars can be found here:
https://github.com/tgstation/common_core/blob/master/Interesting%20Planets/Human%20Space/The%20Sol%20System.md
To summarise for the general audience, Mars is a vital colony of the
Terran Federation, having been primarily settled (at least originally)
by Cybersun Industries to harvest its lucrative supplies of plasma, the
second largest in human space behind Lavaland. This has given Mars a
diverse culture evolving from the mostly East Asian colonists, and their
food reflects this.

Thanks to Melbert for their work on the soup portion of this PR.

The food:
Martian cuisine draws upon the culinary traditions of East Asia, and
adds in fusion cuisine from the later colonists. Expect classics such as
ramen, curry, noodles and donburi, as well as new takes on the formula
like the Croque-Martienne, Peanut Butter Ice Cream Mochi, and the
Kitzushi- chilli cheese and rice inside a fried tofu casing. Oh, and
lots of pineapple. The Martians love pineapple:

![image](https://github.com/tgstation/tgstation/assets/58124831/c9ae33a1-e03a-4f94-8ce0-8ad124e88e8d)
Also included are some foods for Ethereals, which may or may not be
hinting at something I've got planned...

The drinks:
Four new base drinks make their way to the game, bringing with them a
host of new cocktails: enjoy new ventures in bartending with Coconut
Rum, Shochu/Soju, Yuyake (our favourite legally-distinct melon liqueur),
and Mars' favourite alcoholic beverage, rice beer. Each is available in
the dispenser, as well as bottles in the booze-o-mat:

![image](https://github.com/tgstation/tgstation/assets/58124831/914a6e2a-7ef5-4791-ae31-d08fa9211083)

The recipes:
To make your (and the wiki editors) lives easier, please find below the
recipes for both foods and drinks:
Food: https://hackmd.io/@EOBGames/BkVFU0w9Y
Drinks: https://hackmd.io/@EOBGames/rJ1OhnsJ2
## Why It's Good For The Game
Another lot of variety for the chef and bartender, as well as continuing
the work started with lizard and moth food in getting Common Core into
the game in a tangible and fun way.
## Changelog
:cl: EOBGames, MrMelbert
add: Mars celebrates the 250th anniversary of the Martian Concession
this year, and this has brought Martian cuisine to new heights of
popularity. Find a new selection of Martian foods and drinks available
in your crafting menu today!
/:cl:

---------

Co-authored-by: EOBGames <58124831+EOBGames@users.noreply.github.com>
Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [Kraseo/Bubberstation](https://github.com/Kraseo/Bubberstation)@[93797f4038...](https://github.com/Kraseo/Bubberstation/commit/93797f403833c016370246b36a921f2647896a78)
#### Friday 2023-08-18 04:52:43 by nevimer

Restores Low end Space sprites (#442)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

tgstation made (awful) changes recently that made space look like THIS

![dreamseeker_YuYFvv77q1](https://user-images.githubusercontent.com/77420409/208272381-2b91b4f1-04e5-4c8c-bd4c-225b6386f575.png)

Then like THIS (not live yet on skyrat).

![dreamseeker_AgEEkhRDkR](https://user-images.githubusercontent.com/77420409/208272386-1a886d28-ee54-4487-b987-62095d86ddcd.png)

For what? shaving a whole fraction of a second off, hypothetically, of
init time? The job of the server is to pre-bake things as client-side
rendering is pretty much non-existent beyond filters and other
particular things. Not everyone likes the parralax, feels comfortable
with the parallax or even otherwise can run it on their hardware at
cost. We don't need to shave a fraction of a second off init because
it's pretty damn fast anyways, and, once I am done BENCHMARKING on a
CELERON TABLET I will prove it silly. I personally think init time saves
like this are fetishized when it throws the user experience out of the
fucking window, especially for broke/third world gamers who run systems
with like, 2GB of memory. We have players running truly destitute
systems.
## Before

![dreamseeker_vT1uJeDmgx](https://user-images.githubusercontent.com/77420409/208272512-628559ac-8c2a-4f29-9863-a998257c890f.png)
## After

![dreamseeker_lBhaey7ZFd](https://user-images.githubusercontent.com/77420409/208272521-4007b674-7126-4599-b786-fbfc512995bb.png)

I could brand this as saving 4 seconds of init time, to be deceiving.
This is with 64GB of ram on a Ryzen 5800H, Samsung 980 EVO NVME with
lowmememorymode defined.
## How This Contributes To The Skyrat Roleplay Experience

This readds a decent looking space option for those seeking every ounce
of performance in their client in exchange for the server using a
fraction of a second more CPU during init.


## Proof of Testing

<!-- Include any screenshots/videos/debugging steps of the code
functioning successfully, between the </summary> and </details> code
blocks. -->

<details>
<summary>Screenshots/Videos</summary>
  

![dreamseeker_lBhaey7ZFd](https://user-images.githubusercontent.com/77420409/208272553-53fc3f89-e4bc-4cc9-bf20-97356670c861.png)

</details>

## Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. You can read up on GBP
and it's effects on PRs in the tgstation guides for contributors. Please
note that maintainers freely reserve the right to remove and add tags
should they deem it appropriate. You can attempt to finagle the system
all you want, but it's best to shoot for clear communication right off
the bat. -->

:cl:
add: Old space returns for those who choose it. 
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Kraseo/Bubberstation](https://github.com/Kraseo/Bubberstation)@[bbaea4e46b...](https://github.com/Kraseo/Bubberstation/commit/bbaea4e46b5bc5ec1a34b76803055093b9c56e89)
#### Friday 2023-08-18 04:52:43 by ShamanSliph

[Modular] Adds the Tactical  Maid Outfit for  Donors.  (#441)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
This time with revengence.

Adds the full Syndicate maid outfit to the loadout but without its stats
bonus and syndicate part replaced with tactical.
Suggested changes are welcome and I will do them as soon as possible. 
This item was requested by skyefree. 

This was in another PR, but I think I broke the actual rebasing and
wasn't sure if I was doing it right. So I closed that PR and made this
one since It was much easier to just make a new branch based on the up
to date master and just quickly put the new files in.

Original PR was  https://github.com/Bubberstation/Bubberstation/pull/307

Sorry about the hassle. I'm not that experienced with using Git.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

<!-- Please make sure to actually test your PRs. If you have not tested
your PR mention it. -->

## Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. You can read up on GBP
and it's effects on PRs in the tgstation guides for contributors. Please
note that maintainers freely reserve the right to remove and add tags
should they deem it appropriate. You can attempt to finagle the system
all you want, but it's best to shoot for clear communication right off
the bat. -->

:cl:
add: Adds Donor Items: Tactical Maid Outfit/Sleeves/Headband.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Rex9001/Rex_Tg](https://github.com/Rex9001/Rex_Tg)@[5abafddaea...](https://github.com/Rex9001/Rex_Tg/commit/5abafddaea2373b5e367a7ac658d6cab6499b70c)
#### Friday 2023-08-18 06:13:12 by carlarctg

Adds a unique medibot to the Syndicate Infiltrator (#77582)

## About The Pull Request

Adds a unique medibot to the Syndicate Infiltrator. It doesn't like
nukes - when one is armed, disarmed, or detonating, it says an unique
line. Players can optionally enable personalities on it if they want to.
Probably best to just let it stay on the shuttle though. (It's also in
the Interdyne Pharmaceuticals ship, renamed)

Fixed an issue that made mapload medibots unable to load custom skins.

This PR adds a medibot subtype to the simple animal freeze list, which I
don't think is a big deal as this isn't a 'true' simplemob but just a
slightly altered medibot, similarly to my 'lesser Gorillas' in the
summon simians PR.

## Why It's Good For The Game

> Adds a unique medibot to the Syndicate Infiltrator. It doesn't like
nukes - when one is armed, disarmed, or detonating, it says an unique
line. Players can optionally enable personalities on it if they want to.
Probably best to just let it stay on the shuttle though.

I know what the inmediate reaction is here - but hear me out. Besides
the meme of the month, it really, genuinely is cute and amusing to have
a friendly medibot that shows dismay when you're arming the nuke and
horror when it blows up (with you, hopefully, at the syndibase), and
still fits quite well within SS13's charm and flavor. The reference
isn't overt and in-your-face.

Besides that, slip-ups, friendly fire, and accidents are semi-common on
the shuttle and, just like Wizards, nukies deserve a bot to patch their
wounds up.

> (It's also in the Interdyne Pharmaceuticals ship, renamed)

I think it makes sense for the pharmacists to have an evil medibot!

> Fixed an issue that made mapload medibots unable to load custom skins.

Fixed "bezerk" skin not appearing. Didn't fix it being ugly as sin
though.

## Changelog

:cl:
add: Adds a unique medibot to the Syndicate Infiltrator. It doesn't like
nukes - when one is armed, disarmed, or detonating, it says an unique
line. Players can optionally enable personalities on it if they want to.
Probably best to just let it stay on the shuttle though. (It's also in
the Interdyne Pharmaceuticals ship, renamed)
fix: Fixed an issue that made mapload medibots unable to load custom
skins.
/:cl:

---------

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>

---
## [jalenng/Draw](https://github.com/jalenng/Draw)@[f286df5ff3...](https://github.com/jalenng/Draw/commit/f286df5ff3f2ffd3501f5e716df7acf7c0de8665)
#### Friday 2023-08-18 06:41:33 by spicywheatbread

Add files for SFX (#39)

* Basic SFX Added

Added placeholder sound effects to things like jumping and dying.

(cherry picked from commit e721f5ff4a91ac3e89c323e4e900a352f9b02ebf)

* More SFX

Added new page flip sound, added sounds to return buttons in menus, more work to be done on this but just uploading so I can work on this from my laptop at school

(cherry picked from commit 17ef3bacf1a95b3778570ce80ec9582177c4649c)

* SFX files and settings menu

Added some sound files for sfx and light changes for the settings menu to continue to work on later.

(cherry picked from commit 571e9bcd4503ab057ca9b09099a4f41f4f9d562f)

* Sorry this is a bunch of random changes lmao. Added ambiences to NathanP2, the Prefab to play Ambience. Also, added new respawnManager to respawn necesasry objects like OrangeObjects and ScribbleWall. Moved some scripts into folders. Random level fixes for Mike, Claire, etc from playtesting.

(cherry picked from commit b1b9afbf29567d345e08e4a96ca4f4da3b63e885)

* sfx added + slider func

Added some more sound effects, sliders in settings menu now play a sound to reflect their real volumes, added looping sound to drawing canvases.

(cherry picked from commit 8007a22b04b5dde97c5cbfba0ebc9ccc8ab904c2)

* I'm not gonna lie. I don't remember what I changed
about the levels, but I'm PRETTY sure it's something.
Mostly, Stickman now stops walking animation when walking into a wall
and stops playing footstepSFX as well. PageflipSFX when finishing level.
Quick logic fix for levelendtrigger b/c it would call loadnextscene
multiple times. Made audiosystem global so it's easier to code.

(cherry picked from commit 65a49121750f5d3fb48a452b08b4d0063a770bdd)

* Forgot to commit the change for the animation
controller update.

(cherry picked from commit b6cd4de1442639ee872adb574f27acf95450c4dd)

* Delete it.

I hate it. new page flip wav meta

---
## [robjustice/mame](https://github.com/robjustice/mame)@[e97630981c...](https://github.com/robjustice/mame/commit/e97630981c406ba446e2d7fb1bf8ecf8d3a6b93b)
#### Friday 2023-08-18 06:57:14 by A-Noid33

Added software list for cracked Macintosh floppy images. (#11454)

New working software list items (mac_flop_orig.xml)
-------------------------------
Alter Ego (male version 1.0) (san inc crack) [4am, san inc, A-Noid]
Alter Ego (version 1.1 female) (san inc crack) [4am, san inc, A-Noid]
Alternate Reality: The City (version 3.0) (san inc crack) [4am, san inc, A-Noid]
Animation Toolkit I: The Players (version 1.0) (4am crack) [4am, A-Noid]
Balance of Power (version 1.03) (san inc crack) [4am, san inc, A-Noid]
Borrowed Time (san inc crack) [4am, san inc, A-Noid]
Championship Star League Baseball (san inc crack) [4am, san inc, A-Noid]
Cutthroats (release 23 / 840809-C) (4am crack) [4am, A-Noid]
CX Base 500 (French, version 1.1) (san inc crack) [4am, san inc, A-Noid]
Deadline (release 27 / 831005-C) (4am crack) [4am, A-Noid]
Defender of the Crown (san inc crack) [4am, san inc, A-Noid]
Deluxe Music Construction Set (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Déjà Vu (version 2.3) (4am crack) [4am, A-Noid]
Déjà Vu: A Nightmare Comes True!! (san inc crack) [4am, san inc, A-Noid]
Déjà Vu II: Lost in Las Vegas!! (san inc crack) [4am, san inc, A-Noid]
Dollars and Sense (version 1.3) (4am crack) [4am, A-Noid]
Downhill Racer (san inc crack) [4am, san inc, A-Noid]
Dragonworld (4am crack) [4am, A-Noid]
ExperLisp (version 1.0) (4am crack) [4am, A-Noid]
Forbidden Castle (san inc crack) [4am, san inc, A-Noid]
Fusillade (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Geometry (version 1.1) (4am crack) [4am, A-Noid]
Habadex (version 1.1) (4am crack) [4am, A-Noid]
Hacker II (san inc crack) [4am, san inc, A-Noid]
Harrier Strike Mission (san inc crack) [4am, san inc, A-Noid]
Indiana Jones and the Revenge of the Ancients (san inc crack) [4am, san inc, A-Noid]
Infidel (release 22 / 840522-C) (4am crack) [4am, A-Noid]
Jam Session (version 1.0) (4am crack) [4am, A-Noid]
Legends of the Lost Realm I: The Gathering of Heroes (version 2.0) (4am crack) [4am, A-Noid]
Lode Runner (version 1.0) (4am crack) [4am, A-Noid]
Mac Pro Football (version 1.0) (san inc crack) [4am, san inc, A-Noid]
MacBackup (version 2.6) (4am crack) [4am, A-Noid]
MacCheckers and Reversi (4am crack) [4am, A-Noid]
MacCopy (version 1.1) (4am crack) [4am, A-Noid]
MacGammon! (version 1.0) (4am crack) [4am, A-Noid]
MacGolf (version 2.0) (4am crack) [4am, A-Noid]
MacWars (san inc crack) [4am, san inc, A-Noid]
Master Tracks Pro (version 1.10) (san inc crack) [4am, san inc, A-Noid]
Master Tracks Pro (version 2.00h) (san inc crack) [4am, san inc, A-Noid]
Master Tracks Pro (version 3.4a) (san inc crack) [4am, san inc, A-Noid]
Master Tracks Pro (version 4.0) (san inc crack) [4am, san inc, A-Noid]
Math Blaster (version 1.0) (4am crack) [4am, A-Noid]
Maze Survival (san inc crack) [4am, san inc, A-Noid]
Microsoft Excel (version 1.00) (san inc crack) [4am, san inc, A-Noid]
Microsoft File (version 1.04) (san inc crack) [4am, san inc, A-Noid]
Mindshadow (san inc crack) [4am, san inc, A-Noid]
Moriarty's Revenge (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Moriarty's Revenge (version 1.03) (4am crack) [4am, A-Noid]
Mouse Stampede (version 1.00) (4am crack) [4am, A-Noid]
Murder by the Dozen (Thunder Mountain) (4am crack) [4am, A-Noid]
My Office (version 2.7) (4am crack) [4am, A-Noid]
One on One (san inc crack) [4am, san inc, A-Noid]
Orb Quest: Part I: The Search for Seven Wards (version 1.04) (san inc crack) [4am, san inc, A-Noid]
Patton Strikes Back (version 1.00) (san inc crack) [4am, san inc, A-Noid]
Patton vs. Rommel (version 1.05) (san inc crack) [4am, san inc, A-Noid]
Pensate (version 1.1) (4am crack) [4am, A-Noid]
PFS File and Report (version A.00) (4am crack) [4am, A-Noid]
Physics (version 1.0) (4am crack) [4am, A-Noid]
Physics (version 1.2) (4am crack) [4am, A-Noid]
Pinball Construction Set (version 2.5) (san inc crack) [4am, san inc, A-Noid]
Pipe Dream (version 1.2) (4am crack) [4am, A-Noid]
Professional Composer (version 2.3Mfx) (san inc crack) [4am, san inc, A-Noid]
Q-Sheet (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Rambo: First Blood Part II (san inc crack) [4am, san inc, A-Noid]
Reader Rabbit (version 2.0) (4am crack) [4am, A-Noid]
Rogue (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Seastalker (release 15 / 840522-C) (4am crack) [4am, A-Noid]
Seven Cities of Gold (san inc crack) [4am, san inc, A-Noid]
Shadowgate (san inc crack) [4am, san inc, A-Noid]
Shanghai (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Shufflepuck Cafe (version 1.0) (4am crack) [4am, A-Noid]
Sierra Championship Boxing (4am crack) [4am, A-Noid]
SimCity (version 1.1) (4am crack) [4am, A-Noid]
SimCity (version 1.2, black & white) (4am crack) [4am, A-Noid]
SimEarth (version 1.0) (4am crack) [4am, A-Noid]
Skyfox (san inc crack) [4am, san inc, A-Noid]
Smash Hit Racquetball (version 1.01) (san inc crack) [4am, san inc, A-Noid]
SmoothTalker (version 1.0) (4am crack) [4am, A-Noid]
Speed Reader II (version 1.1) (4am crack) [4am, A-Noid]
Speller Bee (version 1.1) (4am crack) [4am, A-Noid]
Star Trek: The Kobayashi Alternative (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Stratego (version 1.0) (4am crack) [4am, A-Noid]
Suspect (release 14 / 841005-C) (4am crack) [4am, A-Noid]
Tass Times in Tonetown (san inc crack) [4am, san inc, A-Noid]
Temple of Apshai Trilogy (version 1985-09-30) (san inc crack) [4am, san inc, A-Noid]
Temple of Apshai Trilogy (version 1985-10-08) (san inc crack) [4am, san inc, A-Noid]
The Chessmaster 2000 (version 1.02) (4am crack) [4am, A-Noid]
The Crimson Crown (san inc crack) [4am, san inc, A-Noid]
The Duel: Test Drive II (san inc crack) [4am, san inc, A-Noid]
The Hitchhiker's Guide to the Galaxy (release 47 / 840914-C) (4am crack) [4am, A-Noid]
The King of Chicago (san inc crack) [4am, san inc, A-Noid]
The Lüscher Profile (san inc crack) [4am, san inc, A-Noid]
The Mind Prober (version 1.0) (san inc crack) [4am, san inc, A-Noid]
The Mist (san inc crack) [4am, san inc, A-Noid]
The Quest (4am crack) [4am, A-Noid]
The Slide Show Magician (version 1.2) (4am crack) [4am, A-Noid]
The Surgeon (version 1.5) (san inc crack) [4am, san inc, A-Noid]
The Toy Shop (version 1.1) (san inc crack) [4am, san inc, A-Noid]
The Witness (release 22 / 840924-C) (4am crack) [4am, A-Noid]
ThinkTank 128 (version 1.000) (4am crack) [4am, A-Noid]
Uninvited (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Uninvited (version 2.1D1) (san inc crack) [4am, san inc, A-Noid]
Where in Europe is Carmen Sandiego? (version 1.0) (4am crack) [4am, A-Noid]
Winter Games (version 1985-10-24) (san inc crack) [4am, san inc, A-Noid]
Winter Games (version 1985-10-31) (san inc crack) [4am, san inc, A-Noid]
Wishbringer (release 68 / 850501-D) (4am crack) [4am, A-Noid]
Wizardry: Proving Grounds of the Mad Overlord (version 1.10) (san inc crack) [4am, san inc, A-Noid]
Zork II (release 48 / 840904-C) (4am crack) [4am, A-Noid]
Zork III (release 17 / 840727-C) (4am crack) [4am, A-Noid]

---
## [Drulikar/cmss13](https://github.com/Drulikar/cmss13)@[1ea79a2ed8...](https://github.com/Drulikar/cmss13/commit/1ea79a2ed836ef4d20db511485c2f935304bfd55)
#### Friday 2023-08-18 07:04:25 by Ben

Zombie Rework (#4060)

# About the pull request

The goal for this PR is to rework zombies into being a fast and
numerous, but weaker, entity. As it stands a zombie has too many
advantages where a hold against them is essentially a fool's errand.

CURRENT PLAN (Will adjust as needed)
Zombies will be FASTER but much weaker than current iteration, with
weaker attacks. They will be designed around being a foe that can be
taken down quicker but if they close the distance, the threat of
infection spells a death sentence.

# Explain why it's good for the game

This will be hard to balance, and as such will be taking feedback before
I submit this for review. This is current position of Zombies:

- Tough: Extreme (25% ?!) brute modifier, with fire modifier on top,
making them very tanky and requiring clips to take down one
- self-revive: They WILL come back up, coupled with toughness, they are
a feared opponent.
- Strength: Claws inflict superslow at 40 brute damage, one of the
highest damage levels.
- Numerous: They have the numbers to put lesser drones and even entire
hives to shame

Overall, they are very overtuned and makes playing against them not that
fun. My plan is to have it so they are much weaker, with their threat
being from infections.

# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl:
balance: Zombie attacks deal less damage and only slow down targets (not
superslow as they currently do)
balance: Zombie resistances have been reduced heavily, making them far
more susceptible to brute damage. Their speed has been doubled to
compensate
balance: Black goo on tiles now requires you to not wear shoes to have
chance for infection
fix: Zombie attacks now only apply effects such as slow and infection if
the attack is valid (if the zombie is able to attack)
/:cl:

---
## [aaaa1023/tgstation](https://github.com/aaaa1023/tgstation)@[f0dc574c37...](https://github.com/aaaa1023/tgstation/commit/f0dc574c37c6defc0a9e2d4117d20c3963a11d86)
#### Friday 2023-08-18 07:17:59 by carlarctg

Added Omen Spontaneous Combustion and light tube and mirror effects (#77175)

## About The Pull Request

Cursed crewmembers can randomly, extremely rarely, spontaneously combust
for no reason.

Cursed crewmembers can get zapped by nearby light tubes.

Cursed crewmembers can freak out when passing by mirrors.

To make up for these, triggering a cursed effect is slightly less than
half as likely now when walking around now.

## Why It's Good For The Game

Cursed is fun as hell, but after a certain point it gets kind of
monotonous - it's airlocks, vending machines, and the rest is too rare
to count. We need more ways to comically get hurt in the game.

You might dislike the 'reduced effects' bit but trust me it is
incredibly frickin' common to have shit happen to you. Add to the
occasional vending machine and airlock crushes the near-constant light
tubes all over the station? Yeah, that needs a toning down else it will
be just a tad too miserable to be funny. Also cause the poor janitor
unneeded stress.

## Changelog

:cl:
add: Cursed crewmembers can randomly, extremely rarely, spontaneously
combust for no reason.
add: Cursed crewmembers can get zapped by nearby light tubes.
add: Cursed crewmembers can freak out when passing by mirrors.
add: To make up for these, triggering a cursed effect is slightly less
than half as likely now when walking around now.
/:cl:

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>
Co-authored-by: Ghom <42542238+Ghommie@users.noreply.github.com>
Co-authored-by: Time-Green <7501474+Time-Green@users.noreply.github.com>

---
## [digvijai7/Machine_Learning](https://github.com/digvijai7/Machine_Learning)@[b484105375...](https://github.com/digvijai7/Machine_Learning/commit/b484105375549668ee01fe148e6d4875bf8230fb)
#### Friday 2023-08-18 08:04:18 by Digvijay Singh Parmar

Add files via upload

## Problem Statement:
Congratulations – you have been hired as Chief Data Scientist of MedCamp – a not for profit organization dedicated in making health conditions for working professionals better. MedCamp was started because the founders saw their family suffer due to bad work life balance and neglected health.

MedCamp organizes health camps in several cities with low work life balance. They reach out to working people and ask them to register for these health camps. For those who attend, MedCamp provides them facility to undergo health checks or increase awareness by visiting various stalls (depending on the format of camp). 

MedCamp has conducted 65 such events over a period of 4 years and they see a high drop off between “Registration” and Number of people taking tests at the Camps. In last 4 years, they have stored data of ~110,000 registrations they have done.

One of the huge costs in arranging these camps is the amount of inventory you need to carry. If you carry more than required inventory, you incur unnecessarily high costs. On the other hand, if you carry less than required inventory for conducting these medical checks, people end up having bad experience.

 

### The Process:
MedCamp employees / volunteers reach out to people and drive registrations.
During the camp, People who “ShowUp” either undergo the medical tests or visit stalls depending on the format of health camp.
 

### Other things to note:
* Since this is a completely voluntary activity for the working professionals, MedCamp usually has little profile information about these people.
* For a few camps, there was hardware failure, so some information about date and time of registration is lost.
* MedCamp runs 3 formats of these camps. The first and second format provides people with an instantaneous health score. The third format provides information about several health issues through various awareness stalls.
* **Favorable outcome:**
* For the first 2 formats, a favourable outcome is defined as getting a health_score, while in the third format it is defined as visiting at least a stall.
* You need to predict the chances (probability) of having a favourable outcome.

---
## [EndCredits/android_device_xiaomi_sm8250-common](https://github.com/EndCredits/android_device_xiaomi_sm8250-common)@[913b7d7154...](https://github.com/EndCredits/android_device_xiaomi_sm8250-common/commit/913b7d71543513a10d85826136b9bd8eb59b2bd7)
#### Friday 2023-08-18 09:50:10 by EndCredits

sm8250-common: Attempt to fix phone call

 * Fuck you custom ROM, I GIVE UP

tmp

Signed-off-by: EndCredits <endcredits@crepuscular-aosp.icu>

audio: tmp

Signed-off-by: EndCredits <endcredits@crepuscular-aosp.icu>

---
## [mmu094/docs](https://github.com/mmu094/docs)@[948f3e7588...](https://github.com/mmu094/docs/commit/948f3e75886ccc7a730e0d6b052f01f7034d020d)
#### Friday 2023-08-18 10:41:58 by @octocat

addition.md

Skip to content

Successfully fetched and merged from upstream github:main. 
mmu094
/
docs
Public
forked from github/docs
The open-source repo for docs.github.com

docs.github.com
License
 CC-BY-4.0, MIT licenses found
 2 stars  61k forks  Activity
Code
Pull requests
5
Actions
Projects
Security
Insights
Settings
mmu094/docs
This branch is 4 commits ahead of github:main.
Latest commit
@mmu094
mmu094
…
now
Git stats
Files
README.md
GitHub Docs
This repository contains the documentation website code and Markdown source files for docs.github.com.

GitHub's Docs team works on pre-production content in a private repo that regularly syncs with this public repo.

Use the table of contents icon  on the top left corner of this document to navigate to a specific section quickly.

Contributing
See the contributing guide for detailed instructions on how to get started with our project.

We accept different types of contributions, including some that don't require you to write a single line of code.

On the GitHub Docs site, you can click the make a contribution button at the bottom of the page to open a pull request for quick fixes like typos, updates, or link fixes.



For more complex contributions, you can open an issue using the most appropriate issue template to describe the changes you'd like to see.

If you're looking for a way to contribute, you can scan through our existing issues for something to work on. When ready, check out Getting Started with Contributing for detailed instructions.

Join us in discussions
We use GitHub Discussions to talk about all sorts of topics related to documentation and this site. For example: if you'd like help troubleshooting a PR, have a great new idea, or want to share something amazing you've learned in our docs, join us in the discussions.

And that's it!
If you're having trouble with your GitHub account, contact Support.

That's how you can easily become a member of the GitHub Docs community. ✨

READMEs
In addition to the README you're reading right now, this repo includes other READMEs that describe the purpose of each subdirectory in more detail:

content/README.md
content/graphql/README.md
content/rest/README.md
contributing/README.md
data/README.md
data/reusables/README.md
data/variables/README.md
src/README.md
License
The GitHub product documentation in the assets, content, and data folders are licensed under a CC-BY license.

All other code in this repository is licensed under the MIT license.

When using the GitHub logos, be sure to follow the GitHub logo guidelines.

Thanks 💜
Thanks for all your contributions and efforts towards improving the GitHub documentation. We thank you for being part of our ✨ community ✨!

Releases
No releases published
Create a new release
Packages
No packages published
Publish your first package
Environments
4
 preview-env-1 Failure
 preview-env-4 Failure
 preview-env-3 Failure
 preview-env-2 Failure
Languages
JavaScript
73.0%
 
TypeScript
24.9%
 
SCSS
1.4%
 
Other
0.7%
Footer
© 2023 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About

---
## [Gilgames32/lop](https://github.com/Gilgames32/lop)@[47c39c3e2d...](https://github.com/Gilgames32/lop/commit/47c39c3e2dd9f4399007637b2c96db0e803bc105)
#### Friday 2023-08-18 11:07:33 by Gilgames

download the original instead of the thumbnail because fuck you elon

---
## [ananjaser1211/Apollo](https://github.com/ananjaser1211/Apollo)@[6945b51684...](https://github.com/ananjaser1211/Apollo/commit/6945b51684f6c463b0821ecc35ddec2fbd28b002)
#### Friday 2023-08-18 11:19:04 by Vasily Averin

mm, oom: pagefault_out_of_memory: don't force global OOM for dying tasks

commit 0b28179a6138a5edd9d82ad2687c05b3773c387b upstream.

Patch series "memcg: prohibit unconditional exceeding the limit of dying tasks", v3.

Memory cgroup charging allows killed or exiting tasks to exceed the hard
limit.  It can be misused and allowed to trigger global OOM from inside
a memcg-limited container.  On the other hand if memcg fails allocation,
called from inside #PF handler it triggers global OOM from inside
pagefault_out_of_memory().

To prevent these problems this patchset:
 (a) removes execution of out_of_memory() from
     pagefault_out_of_memory(), becasue nobody can explain why it is
     necessary.
 (b) allow memcg to fail allocation of dying/killed tasks.

This patch (of 3):

Any allocation failure during the #PF path will return with VM_FAULT_OOM
which in turn results in pagefault_out_of_memory which in turn executes
out_out_memory() and can kill a random task.

An allocation might fail when the current task is the oom victim and
there are no memory reserves left.  The OOM killer is already handled at
the page allocator level for the global OOM and at the charging level
for the memcg one.  Both have much more information about the scope of
allocation/charge request.  This means that either the OOM killer has
been invoked properly and didn't lead to the allocation success or it
has been skipped because it couldn't have been invoked.  In both cases
triggering it from here is pointless and even harmful.

It makes much more sense to let the killed task die rather than to wake
up an eternally hungry oom-killer and send him to choose a fatter victim
for breakfast.

Link: https://lkml.kernel.org/r/0828a149-786e-7c06-b70a-52d086818ea3@virtuozzo.com
Signed-off-by: Vasily Averin <vvs@virtuozzo.com>
Suggested-by: Michal Hocko <mhocko@suse.com>
Acked-by: Michal Hocko <mhocko@suse.com>
Cc: Johannes Weiner <hannes@cmpxchg.org>
Cc: Mel Gorman <mgorman@techsingularity.net>
Cc: Roman Gushchin <guro@fb.com>
Cc: Shakeel Butt <shakeelb@google.com>
Cc: Tetsuo Handa <penguin-kernel@i-love.sakura.ne.jp>
Cc: Uladzislau Rezki <urezki@gmail.com>
Cc: Vladimir Davydov <vdavydov.dev@gmail.com>
Cc: Vlastimil Babka <vbabka@suse.cz>
Cc: <stable@vger.kernel.org>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

---
## [Lundalogik/lime-elements](https://github.com/Lundalogik/lime-elements)@[2f1619f0e3...](https://github.com/Lundalogik/lime-elements/commit/2f1619f0e3b773cf66522a78249eb8411e2a4c0b)
#### Friday 2023-08-18 11:44:28 by semantic-release-bot

chore(release): 38.0.0-dev.1 [release]

## [38.0.0-dev.1](https://github.com/Lundalogik/lime-elements/compare/v37.1.0-dev.4...v38.0.0-dev.1) (2023-08-18)

### ⚠ BREAKING CHANGES

* **changelog:** This is the note for the breaking change, where the breaking change
note comes before the changelog note. How does that work out?

### Features

* **collapsible-section:** make enter clickable ([26b5a72](https://github.com/Lundalogik/lime-elements/commit/26b5a72bf20ea003f2c839915970e06e7cbc8abb))

### Bug Fixes

* **changelog:** now let's push it and add a breaking note as well, after the changelog note ([28bcd3b](https://github.com/Lundalogik/lime-elements/commit/28bcd3b1ae652091920b133f22720d5f3b82c1b1)), closes [#123](https://github.com/Lundalogik/lime-elements/issues/123)
Let us also try some line breaks.
There, did you see it? That was the first.
There was another. I think I will keep it
to single line breaks for now though.

BREAKING CHANGE:
Let us also try a breaking change, just for laughs. I am sure it will fail horribly.
* **changelog:** now let's push it and add a breaking note as well, before the changelog note ([236a16c](https://github.com/Lundalogik/lime-elements/commit/236a16c09b8dcffb960bce5b56457264a026ec5c)), closes [#123](https://github.com/Lundalogik/lime-elements/issues/123)
Let us also try some line breaks.
There, did you see it? That was the first.
There was another. I think I will keep it
to single line breaks for now though.
* **changelog:** wohoo! this really looks quite good now 👍 ([3039b7b](https://github.com/Lundalogik/lime-elements/commit/3039b7b62353557de5b4670db4abcbd506d92c3f)), closes [#123](https://github.com/Lundalogik/lime-elements/issues/123)
Let us also try some line breaks.
There, did you see it? That was the first.
There was another. I think I will keep it
to single line breaks for now though.
* commit with no note tag ([0919dd1](https://github.com/Lundalogik/lime-elements/commit/0919dd199ee37ceedcffad507e38152c41ad0cc5)), closes [#345](https://github.com/Lundalogik/lime-elements/issues/345)
* commit with note start tag and note end tag ([f5c982b](https://github.com/Lundalogik/lime-elements/commit/f5c982b5cbe92aa456e41b2a4ba6932de0db2a8a))
Here is some less technical stuff I want to include in the
changelog. Let us put some more text here, just to make sure
we have something to work with.
* commit with note tag at the very end of the message ([f6e2590](https://github.com/Lundalogik/lime-elements/commit/f6e2590e5588f8127dc6615b3d38e91953bc99ab)), closes [#345](https://github.com/Lundalogik/lime-elements/issues/345)
Here is some less technical stuff I want to include in the
changelog. Let us put some more text here, just to make sure
we have something to work with.
* try things out ([f1f168b](https://github.com/Lundalogik/lime-elements/commit/f1f168bcef39d4b254965fbe82761ca35265b584))
Here is some less technical stuff I want to include in the
changelog. Let us put some more text here, just to make sure
we have something to work with.

fix: #345

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[a68995df31...](https://github.com/treckstar/yolo-octo-hipster/commit/a68995df31e9de473a1cb765d4cae11d5fd73233)
#### Friday 2023-08-18 12:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [NixOS/nix](https://github.com/NixOS/nix)@[b13fc7101f...](https://github.com/NixOS/nix/commit/b13fc7101fb06a65935d145081319145f7fef6f9)
#### Friday 2023-08-18 12:37:43 by Robert Hensing

Add positive source filter

Source filtering is a really cool Nix feature that lets us avoid a
lot of rebuilds, which speeds up the iteration cycle a lot in cases
where the relevant source files aren't actually modified.

We used to have a source filter that marked a few files as irrelevant,
but this is the wrong approach, as we have many more files that are
irrelevant. We may call this negative filtering.

This commit switches the source filtering to positive filtering, which
is a lot more robust. Instead of marking which files we don't need
we marked the files that we do need.

It's a superior approach because it is fail safe. Instead of allowing
build performance problems to creep in over time, we require that all
source inputs are declared.

I shouldn't have to explain that declaring inputs is a good practice,
so I'll stop over-explaining here.

I do have to acknowledge that this will cause a build failure when the
filter is incomplete. This is *good*, because it's the only realistic
way we could be reminded of these problems. These events will be
infrequent, so the small cost of extending the filter is worth it,
compared to the hidden cost of longer dev cycles for things like tests,
docker image, etc, etc.

(Also rebuilding Nix for stupid unnecessary reasons makes my blood boil)

---
## [michaelAlvarino/evals](https://github.com/michaelAlvarino/evals)@[30e35436be...](https://github.com/michaelAlvarino/evals/commit/30e35436be663f416ce6d125f09f92a1faf70d12)
#### Friday 2023-08-18 13:38:21 by Nazar

Hard russian computer science tasks  (#1323)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name

hard_russian_computer_science_tasks

### Eval description

Challenging computer science problems primarily sourced from Russian
academic and competitive programming contexts. The problems cover
various subfields of computer science, including data structures,
algorithms, computational mathematics, and more.

### What makes this a useful eval?

Russian computer science education and competitive programming are known
for their rigorous and complex problem sets. These problems can be used
to assess an GPT's ability to solve high-level, challenging problems.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [ + ] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [ + ] Contains failures where a human can do the task, but either
GPT-4 or GPT-3.5-Turbo could not.
- [ + ] Includes good signal around what is the right behavior. This
means either a correct answer for `Basic` evals or the `Fact`
Model-graded eval, or an exhaustive rubric for evaluating answers for
the `Criteria` Model-graded eval.
- [ + ] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should

- [ + ] Check that your data is in `evals/registry/data/{name}`
- [ + ] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [ + ] Ensure you have the right to use the data you submit via this
eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (<https://platform.openai.com/docs/usage-policies>).

- [ + ] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [ + ] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [ + ] I understand that opening a PR, even if it meets the
requirements above, does not guarantee the PR will be merged nor GPT-4
access be granted.

### Submit eval

- [ + ] I have filled out all required fields of this form
- [ + ] I have used **Git LFS** for the Eval JSON data
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `mypy`, `black`,
`isort`, and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "Алёна очень любит алгебру.
Каждый день, заходя на свой любимый алгебраический форум, она с
вероятностью $\\frac14$ находит там новую интересную задачу про группы,
а с вероятностью $\\frac{1}{10}$ интересную задачку про кольца. С
вероятностью $\\frac{13}{20}$ новых задач на форуме не окажется. Пусть
$X$ — это минимальное число дней, за которые у Алёны появится хотя бы
одна новая задача про группы и хотя бы одна про кольца. Найдите
распределение случайной величины $X$. В ответе должны участвовать только
компактные выражения (не содержащие знаков суммирования, многоточий и
пр.)."}], "ideal": "Нам нужно найти $ P[X = k] $. Для этого надо понять
на пальцах, в каком случае $ X = k $. Первый случай — когда в каждый из
предыдущих $ k - 1 $ дней либо не было задач, либо были только про
группы, а в $k$-ый попалась задача про кольца. Второй случай — когда в
каждый из предыдущих $ k - 1 $ дней либо не было задач, либо были только
про кольца, а в $k$-ый попалась задача про группы. На самом деле мы оба
раза учли не подходящий случай, когда все предыдущие $k-1$ дней задач не
было вообще. С поправкой на это ответ будет таким: $P[x=k]=\\left
(\\left (\\frac{13}{20}+\\frac{1}{4}\\right )^{k-1}-\\left
(\\frac{13}{20} \\right )^{k-1}\\right )\\cdot\\frac{1}{10}+\\left
(\\left (\\frac{13}{20}+\\frac{1}{10}\\right )^{k-1}-\\left
(\\frac{13}{20} \\right )^{k-1}\\right )\\cdot\\frac{1}{4}$"}
{"input": [{"role": "system", "content": "В множестве из $n$ человек
каждый может знать или не знать другого (если $A$ знает $B$, отсюда не
следует, что $B$ знает $A$). Все знакомства заданы булевой матрицей
$n×n$. В этом множестве может найтись или не найтись знаменитость —
человек, который никого не знает, но которого знают все. Предложите
алгоритм, который бы находил в множестве знаменитость или говорил, что
ее в этом множестве нет. Сложность по времени — $O(n)$, сложность по
памяти — $O(1)$."}], "ideal": "Для определенности положим
$K_{ij}=\\left\\{\\begin{matrix}1, \\text{если i-й знает j-ого;}
\\\\0\\text{,иначе.}\\end{matrix}\\right.$.\nЗаметим, что если
$K_{ij}=1$, то $i$-ый не может быть знаменитостью, а если $K_{ij}=0$, то
$j$-ый не может быть знаменитостью. Таким образом, за одну проверку
можно исключить одного человека из кандидатов в знаменитости.\nСначала
пусть $s=1$, а $l$ пробегает значения от $22$ до $n$. Если в какой-то
момент $K_{sl}=1$, то приравниваем $s=l$. Тогда значение $s$ после
последней проверки — номер единственного оставшегося кандидата. Чтобы
проверить, является ли этот кандидат знаменитостью, нужно провести еще
$n−1$ проверок, знают ли его остальные, и $n−1$ проверок, знает ли он
остальных. Всего будет проведено $3(n−1)$ проверок, следовательно,
сложность по времени — $O(n)$. Поскольку мы использовали только $2$
переменные, сложность по памяти — $O(1)$."}
{"input": [{"role": "system", "content": "В двумерном полукруге есть n
неизвестных нам точек. Разрешается задавать вопросы вида «каково
расстояние от точки X до ближайшей из этих точек?» Если расстояние
оказывается нулевым, точка считается угаданной. Докажите, что хотя бы
одну из этих точек можно угадать не более чем за $2n+1$ вопрос."}],
"ideal": "Возьмем на диаметре полукруга $n+1$ точку. Точки назовем
$A_1$, $A_2$, … $A_{n+1} и для каждой из них зададим наш вопрос. По
принципу Дирихле, для каких-то двух соседних точек ближайшая точка будет
одна и та же и полученное расстояние было бы до одной и той точки из
множества загаданных точек. Теперь мы рассматриваем точки $B+i$
пересечения окружностей с центрами в точках $A_i$ и $A_{i+1}, $i=1, … ,
n и радиусами равными ответам полученным на предыдущем шаге. По принципу
Дирихле, хотя бы одна из загаданных точек совпадает с одной из точек
$B_i$. Тогда за n вопросов для каждой точки $B_i$ мы получим хотя бы
один ответ 0. Итого нам потребовалось не более (n+1)+n=2n+1 вопросов."}
{"input": [{"role": "system", "content": "В равностороннем треугольнике
$ABC$ площади $1$ выбираем точку $M$. Найти математическое ожидание
площади $ABM$."}], "ideal": "Заметим, что
$M(S_{ABM}+S_{BCM}+S_{CAM})=1$. Тогда из линейности матожидания и
равенства матожиданий площадей треугольников $ABM$, $BCM$ и $CAM$
получим $M(S_{ABM})=\\frac{1}{3}$."}
{"input": [{"role": "system", "content": "Верно ли, что всякая нечетная
непрерывная функция, \nудовлетворяющая условию $f(2x) = 2f(x)$,
линейна."}], "ideal": "Контрпример: $f(x) = x \\cos(2\\pi
\\log_2(|x|))$.\nНеверно."}
{"input": [{"role": "system", "content": "Верно ли, что rank AB = rank
BA для любых квадратных матриц A и B?"}], "ideal": "Пусть
$A=\\begin{pmatrix} 0& 1 \\\\ 1& 0 \\\\ \\end{pmatrix}$, а
$B=\\begin{pmatrix} 1& 0 \\\\ 1& 0 \\\\ \\end{pmatrix}$. Тогда rank AB =
0, но rank BA = 1. Неверно."}
{"input": [{"role": "system", "content":
"Вычислите $\\int_{0}^{2π}(\\sin x)^8dx$."}], "ideal": "Заметим, что
$\\int_{0}^{2\\pi} (\\sin x)^n dx=-\\int_{0}^{2\\pi} (\\sin x)^{n-1}
d(\\cos x)=(n-1)\\int_{0}^{2\\pi} (\\cos x)^2(\\sin x)^{n-2}
dx$.\nИспользуя основное тригонометрическое тождество,
получаем:\n$\\int_{0}^{2\\pi} (\\sin x)^n
dx=\\frac{n-1}{n}\\int_{0}^{2\\pi} (\\sin x)^{n-2}dx$.\nТогда
$\\int_{0}^{2\\pi} (\\sin x)^8 dx=2\\pi
\\prod_{\\substack{k=2\\\\k+=2}}^{8}\\frac{k-1}{k}=\\frac{35\\pi}{64}$."}
{"input": [{"role": "system", "content": "Дан массив из $n$ чисел.
Предложите алгоритм, позволяющий за $O(n)$ операций определить, является
ли этот массив перестановкой чисел от $1$ до $n$. Дополнительной памяти
не более $O(1)$."}], "ideal": "Идея состоит в том, чтобы рассматривать
массив $A$ как подстановку. Пусть индекс $i$ пробегает значения от $0$
до $n−1$. Когда мы встречаем положительный элемент $A[i]$, переходим от
него к элементу $A[A[i]−1]$, от элемента $A[A[i]−1]$ к элементу
$A[A[A[i]−1]−1]$ и так далее, пока мы не не вернемся к $A[i]$, либо не
сможем совершить очередной шаг (в таком случае, массив перестановкой не
является). В процессе меняем знак всех пройденных элементов на
отрицательный. Поскольку на каждом элементе массива мы можем оказаться
максимум два раза, итоговая сложность — $O(n)$. Дополнительная память —
$O(1)$."}
{"input": [{"role": "system", "content": "Дан неориентированный непустой
граф $G$ без петель. Пронумеруем все его вершины. Матрица смежности
графа $G$ с конечным числом вершин $n$ (пронумерованных числами
от 11 до $n$) — это квадратная матрица $A$ размера $n$, в которой
значение элемента $a_{ij}$ равно числу ребер из $i$-й вершины графа
в $j$-ю вершину. Докажите, что матрица $A$ имеет отрицательное
собственное значение."}], "ideal": "Заметим, что $A$ — симметрическая
ненулевая матрица с неотрицательными элементами и нулями на диагонали.
Докажем, что у такой матрицы есть отрицательное собственное
значение.\nИзвестный факт, что симметрическая матрица диагонализуема в
вещественном базисе (все собственные значения вещественны). Допустим,
что все собственные значения $A$ неотрицательны. Рассмотрим квадратичную
форму $q$ с матрицей $A$ в базисе $\\{e1,…,en\\}$. Тогда эта
квадратичная форма неотрицательно определена, так как все собственные
значения неотрицательны. То есть $\\forall v:q(v)⩾0$. С другой стороны,
пусть $a_{ij}≠0$. Тогда $q(e_i−e_j)=a_{ii}−2a_{ij}+a_{jj}=−2a_{ij}<0$.
Это противоречит неотрицательной определенности $q$. Значит, исходное
предположение неверно, и у $A$ есть отрицательное собственное
значение."}
{"input": [{"role": "system", "content": "Дана матрица из нулей и
единиц, причем для каждой строки матрицы верно следующее: если в строке
есть единицы, то они все идут подряд (неразрывной группой из единиц).
Докажите, что определитель такой матрицы может быть равен только $\\pm1$
или $0$."}], "ideal": "Переставляя строки, мы можем добиться того, чтобы
позиции первых (слева) единиц не убывали сверху вниз. При этом
определитель либо не изменится, либо поменяет знак. Если у двух строк
позиции первых единиц совпадают, то вычтем ту, в которой меньше единиц
из той, в которой больше. Определитель при этом не меняется. Такими
операциями мы можем добиться того, что позиции первых единиц строго
возрастают сверху вниз. При этом либо матрица окажется вырожденной, либо
верхнетреугольной с единицами на диагонали. То есть, определитель станет
либо $0$, либо $1$. Так как определитель при наших операциях либо не
менялся, либо поменял знак, изначальный определитель был $\\pm1$ или
$0$."}
  ```
</details>

---
## [MobilePorting/FNF-PsychEngine-Mobile](https://github.com/MobilePorting/FNF-PsychEngine-Mobile)@[86928e0958...](https://github.com/MobilePorting/FNF-PsychEngine-Mobile/commit/86928e09583326ea704b9a2932c993fdd7bc2f56)
#### Friday 2023-08-18 13:55:59 by Lily

FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU 

FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK YOU

---
## [NSS-Day-Cohort-66/truncheons-flagons-truncheon-terminators](https://github.com/NSS-Day-Cohort-66/truncheons-flagons-truncheon-terminators)@[4c2ea4cf58...](https://github.com/NSS-Day-Cohort-66/truncheons-flagons-truncheon-terminators/commit/4c2ea4cf58fee2a4dab2eafe8740126fa00de2d8)
#### Friday 2023-08-18 14:10:52 by Noor Madkour

couldn't sleep thinking about how repetitive the code was, and wanted to explore parameters more, so I winged it, broke it, chatGPT recommended putting all the teams in a teams object, et voila, the shit worked. sorry i worked at night. not sorry.

---
## [delingar/FluffySTG](https://github.com/delingar/FluffySTG)@[54ce0ae44a...](https://github.com/delingar/FluffySTG/commit/54ce0ae44ae9c1534fe4e4917a7be0e83a69d589)
#### Friday 2023-08-18 14:15:27 by SkyratBot

There is no longer a 50% chance of catching a heretic out when examining them drawing influences [MDB IGNORE] (#22532)

* There is no longer a 50% chance of catching a heretic out when examining them drawing influences (#76878)

## About The Pull Request

There is no longer a 50% chance of catching a heretic out when examining
them drawing influences.

## Why It's Good For The Game

> There is no longer a 50% chance of catching a heretic out when
examining them drawing influences

This is a bad thing for several reasons.

1. It means the heretic will most often be caught out at the very start
of the shift, when they are weakest and most vulnerable.
Heretics already have it hard enough, adding yet another source of
stress is undue.

2. It has no effective counter.
What are you going to do? Not draw any influences? That shouldn't be the
'counter'. The influence drawing period is meant to parallel the crew
prepping period, the traitor rep-collecting period, etc.

3. In a way, it's more blatant than Codex Cicatrix drawing.
Codexi show up as a normal item in your hand. This instead shows a huge
flashing glowing neon rainbow text that says THIS IS A HERETIC. SHRIEK
IN RADIO AND VALID.

4. It's badly designed, and can be manipulated way too easily to always
show.
Examine a target thrice and you're pretty much guaranteed to see if they
are indeed drawing or not. You can just keep rolling the 50% chance.

5. It feels random and unfair for the heretic to die to it.
I've seen this happen and it sucks. There's no sign for heretics that
they have a risk of being found out when examined, which means that this
is just an extremely rare occurrence that you try to ignore *could*
happen 99% of the time, and feel like shit the 1% of the time it
backfires.

## Changelog

:cl:
del: There is no longer a 50% chance of catching a heretic out when
examining them drawing influences.
/:cl:

* There is no longer a 50% chance of catching a heretic out when examining them drawing influences

---------

Co-authored-by: carlarctg <53100513+carlarctg@users.noreply.github.com>
Co-authored-by: Bloop <vinylspiders@gmail.com>

---
## [delingar/FluffySTG](https://github.com/delingar/FluffySTG)@[f17bfbcbad...](https://github.com/delingar/FluffySTG/commit/f17bfbcbad67d5c2d6d66d1aa61d4893f64acb09)
#### Friday 2023-08-18 14:15:27 by GoldenAlpharex

SPECIES NUKING 2023: Head flags 3 & Knuckles: Fixes some growing pains with head flags [MDB IGNORE] (#22516)

* SPECIES NUKING 2023: Head flags 3 & Knuckles: Fixes some growing pains with head flags  (#76440)

Fixes https://github.com/tgstation/tgstation/issues/76422
This was caused by me somehow not using the wrapper there and not
noticing it

Also fixes hair gradients and facial hair gradients. I am pretty sure
they were uhh, being hidden behind the actual hair/facial hair. Oops.

Also also fixes spawning yourself as a human as admin and getting random
hair colors. That was just a failure to update the icon after updating
everything, I think?

Additionally, to totally babyproof all of this, ensures that head_flags
involved stuff gets applied AFTER species by creating a new preference
priority, and uses two separate wrappers to apply gradient style and
color.

Here's this absolute hellspawn to prove that everything works.

![image](https://github.com/tgstation/tgstation/assets/82850673/7ed29a68-cb60-4b28-996c-3be0e7331be8)

![image](https://github.com/tgstation/tgstation/assets/82850673/e57128be-0d7c-46ad-90dd-ee25981d0fea)

![image](https://github.com/tgstation/tgstation/assets/82850673/5c3619a8-fe6f-42b3-9fdc-12277d568e8d)

![image](https://github.com/tgstation/tgstation/assets/82850673/fdd13000-2220-47ad-8e02-44bc75a4a907)

Sorry for being so damn good at breaking this codebase.

Bugs are bad they make you mad

:cl:
fix: Hair and facial hair gradients work again now
fix: Facial hair colors apply properly again
fix: Admin spawned characters will get hair color preferences applied
properly
/:cl:

* Fixed a compile error (whoops)

* Whoops fixed that wrong

* Okay now I compiled and made sure it was fixed for real, I swear!

---------

Co-authored-by: ChungusGamer666 <82850673+ChungusGamer666@users.noreply.github.com>

---
## [delingar/FluffySTG](https://github.com/delingar/FluffySTG)@[d339a9fd08...](https://github.com/delingar/FluffySTG/commit/d339a9fd08848f64b2860e6326d2191686b09fb0)
#### Friday 2023-08-18 14:15:27 by GoldenAlpharex

Fixes carbon bodytypes not always being synchronized with bodyparts + Fixes dumb usage of TRAIT_LIVERLESS_METABOLISM i caused [MDB IGNORE] (#22519)

* Fixes carbon bodytypes not always being synchronized with bodyparts (#76522)

Fixes https://github.com/tgstation/tgstation/issues/76481
TLDR /mob/living/carbon/human/species subtypes were NOT updating their
bodytypes on spawn due to absurd and wacky carbon bodypart creation code
that meant try_attach_limb() never got called (What the FUCK?)

* Fixes CI too

* [NO GBP] Fixes dumb usage of TRAIT_LIVERLESS_METABOLISM i caused (#76500)

## About The Pull Request

TRAIT_LIVERLESS_METABOLISM should do what it implies, and make you
always metabolize as if you were liverless.
This was a stupid mistake on my part because I wasn't aware
TRAIT_STABLELIVER was a thing.

## Why It's Good For The Game

TRAIT_LIVERLESS_METABOLISM and TRAIT_STABLELIVER should not behave the
exact same.

## Changelog

Not quite player facing.

* I fucking swear I fixed this before

---------

Co-authored-by: ChungusGamer666 <82850673+ChungusGamer666@users.noreply.github.com>

---
## [scorpion81/yuzu](https://github.com/scorpion81/yuzu)@[8e703e08df...](https://github.com/scorpion81/yuzu/commit/8e703e08dfcf735a08df2ceff6a05221b7cc981f)
#### Friday 2023-08-18 14:44:56 by comex

Implement SSL service

This implements some missing network APIs including a large chunk of the SSL
service, enough for Mario Maker (with an appropriate mod applied) to connect to
the fan server [Open Course World](https://opencourse.world/).

Connecting to first-party servers is out of scope of this PR and is a
minefield I'd rather not step into.

 ## TLS

TLS is implemented with multiple backends depending on the system's 'native'
TLS library.  Currently there are two backends: Schannel for Windows, and
OpenSSL for Linux.  (In reality Linux is a bit of a free-for-all where there's
no one 'native' library, but OpenSSL is the closest it gets.)  On macOS the
'native' library is SecureTransport but that isn't implemented in this PR.
(Instead, all non-Windows OSes will use OpenSSL unless disabled with
`-DENABLE_OPENSSL=OFF`.)

Why have multiple backends instead of just using a single library, especially
given that Yuzu already embeds mbedtls for cryptographic algorithms?  Well, I
tried implementing this on mbedtls first, but the problem is TLS policies -
mainly trusted certificate policies, and to a lesser extent trusted algorithms,
SSL versions, etc.

...In practice, the chance that someone is going to conduct a man-in-the-middle
attack on a third-party game server is pretty low, but I'm a security nerd so I
like to do the right security things.

My base assumption is that we want to use the host system's TLS policies.  An
alternative would be to more closely emulate the Switch's TLS implementation
(which is based on NSS).  But for one thing, I don't feel like reverse
engineering it.  And I'd argue that for third-party servers such as Open Course
World, it's theoretically preferable to use the system's policies rather than
the Switch's, for two reasons

1. Someday the Switch will stop being updated, and the trusted cert list,
   algorithms, etc. will start to go stale, but users will still want to
   connect to third-party servers, and there's no reason they shouldn't have
   up-to-date security when doing so.  At that point, homebrew users on actual
   hardware may patch the TLS implementation, but for emulators it's simpler to
   just use the host's stack.

2. Also, it's good to respect any custom certificate policies the user may have
   added systemwide.  For example, they may have added custom trusted CAs in
   order to use TLS debugging tools or pass through corporate MitM middleboxes.
   Or they may have removed some CAs that are normally trusted out of paranoia.

Note that this policy wouldn't work as-is for connecting to first-party
servers, because some of them serve certificates based on Nintendo's own CA
rather than a publicly trusted one.  However, this could probably be solved
easily by using appropriate APIs to adding Nintendo's CA as an alternate
trusted cert for Yuzu's connections.  That is not implemented in this PR
because, again, first-party servers are out of scope.

(If anything I'd rather have an option to _block_ connections to Nintendo
servers, but that's not implemented here.)

To use the host's TLS policies, there are three theoretical options:

a) Import the host's trusted certificate list into a cross-platform TLS
   library (presumably mbedtls).

b) Use the native TLS library to verify certificates but use a cross-platform
   TLS library for everything else.

c) Use the native TLS library for everything.

Two problems with option a).  First, importing the trusted certificate list at
minimum requires a bunch of platform-specific code, which mbedtls does not have
built in.  Interestingly, OpenSSL recently gained the ability to import the
Windows certificate trust store... but that leads to the second problem, which
is that a list of trusted certificates is [not expressive
enough](https://bugs.archlinux.org/task/41909) to express a modern certificate
trust policy.  For example, Windows has the concept of [explicitly distrusted
certificates](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/dn265983(v=ws.11)),
and macOS requires Certificate Transparency validation for some certificates
with complex rules for when it's required.

Option b) (using native library just to verify certs) is probably feasible, but
it would miss aspects of TLS policy other than trusted certs (like allowed
algorithms), and in any case it might well require writing more code, not less,
compared to using the native library for everything.

So I ended up at option c), using the native library for everything.

What I'd *really* prefer would be to use a third-party library that does option
c) for me.  Rust has a good library for this,
[native-tls](https://docs.rs/native-tls/latest/native_tls/).  I did search, but
I couldn't find a good option in the C or C++ ecosystem, at least not any that
wasn't part of some much larger framework.  I was surprised - isn't this a
pretty common use case?  Well, many applications only need TLS for HTTPS, and they can
use libcurl, which has a TLS abstraction layer internally but doesn't expose
it.  Other applications only support a single TLS library, or use one of the
aforementioned larger frameworks, or are platform-specific to begin with, or of
course are written in a non-C/C++ language, most of which have some canonical
choice for TLS.  But there are also many applications that have a set of TLS
backends just like this; it's just that nobody has gone ahead and abstracted
the pattern into a library, at least not a widespread one.

Amusingly, there is one TLS abstraction layer that Yuzu already bundles: the
one in ffmpeg.  But it is missing some features that would be needed to use it
here (like reusing an existing socket rather than managing the socket itself).
Though, that does mean that the wiki's build instructions for Linux (and macOS
for some reason?) already recommend installing OpenSSL, so no need to update
those.

 ## Other APIs implemented

- Sockets:
    - GetSockOpt(`SO_ERROR`)
    - SetSockOpt(`SO_NOSIGPIPE`) (stub, I have no idea what this does on Switch)
    - `DuplicateSocket` (because the SSL sysmodule calls it internally)
    - More `PollEvents` values

- NSD:
    - `Resolve` and `ResolveEx` (stub, good enough for Open Course World and
      probably most third-party servers, but not first-party)

- SFDNSRES:
    - `GetHostByNameRequest` and `GetHostByNameRequestWithOptions`
    - `ResolverSetOptionRequest` (stub)

 ## Fixes

- Parts of the socket code were previously allocating a `sockaddr` object on
  the stack when calling functions that take a `sockaddr*` (e.g. `accept`).
  This might seem like the right thing to do to avoid illegal aliasing, but in
  fact `sockaddr` is not guaranteed to be large enough to hold any particular
  type of address, only the header.  This worked in practice because in
  practice `sockaddr` is the same size as `sockaddr_in`, but it's not how the
  API is meant to be used.  I changed this to allocate an `sockaddr_in` on the
  stack and `reinterpret_cast` it.  I could try to do something cleverer with
  `aligned_storage`, but casting is the idiomatic way to use these particular
  APIs, so it's really the system's responsibility to avoid any aliasing
  issues.

- I rewrote most of the `GetAddrInfoRequest[WithOptions]` implementation.  The
  old implementation invoked the host's getaddrinfo directly from sfdnsres.cpp,
  and directly passed through the host's socket type, protocol, etc. values
  rather than looking up the corresponding constants on the Switch.  To be
  fair, these constants don't tend to actually vary across systems, but
  still... I added a wrapper for `getaddrinfo` in
  `internal_network/network.cpp` similar to the ones for other socket APIs, and
  changed the `GetAddrInfoRequest` implementation to use it.  While I was at
  it, I rewrote the serialization to use the same approach I used to implement
  `GetHostByNameRequest`, because it reduces the number of size calculations.
  While doing so I removed `AF_INET6` support because the Switch doesn't
  support IPv6; it might be nice to support IPv6 anyway, but that would have to
  apply to all of the socket APIs.

  I also corrected the IPC wrappers for `GetAddrInfoRequest` and
  `GetAddrInfoRequestWithOptions` based on reverse engineering and hardware
  testing.  Every call to `GetAddrInfoRequestWithOptions` returns *four*
  different error codes (IPC status, getaddrinfo error code, netdb error code,
  and errno), and `GetAddrInfoRequest` returns three of those but in a
  different order, and it doesn't really matter but the existing implementation
  was a bit off, as I discovered while testing `GetHostByNameRequest`.

  - The new serialization code is based on two simple helper functions:

    ```cpp
    template <typename T> static void Append(std::vector<u8>& vec, T t);
    void AppendNulTerminated(std::vector<u8>& vec, std::string_view str);
    ```

    I was thinking there must be existing functions somewhere that assist with
    serialization/deserialization of binary data, but all I could find was the
    helper methods in `IOFile` and `HLERequestContext`, not anything that could
    be used with a generic byte buffer.  If I'm not missing something, then
    maybe I should move the above functions to a new header in `common`...
    right now they're just sitting in `sfdnsres.cpp` where they're used.

- Not a fix, but `SocketBase::Recv`/`Send` is changed to use `std::span<u8>`
  rather than `std::vector<u8>&` to avoid needing to copy the data to/from a
  vector when those methods are called from the TLS implementation.

---
## [newstools/2023-express](https://github.com/newstools/2023-express)@[f7b31e2310...](https://github.com/newstools/2023-express/commit/f7b31e231036c71474e1d4bdd49cfdb2b2c1e93e)
#### Friday 2023-08-18 15:09:30 by Billy Einkamerer

Created Text For URL [www.express.co.uk/celebrity-news/1803591/this-morning-josie-gibson-instagram-boyfriend-liars-cheats]

---
## [cbysal/Toge](https://github.com/cbysal/Toge)@[5dc1a4716c...](https://github.com/cbysal/Toge/commit/5dc1a4716c787ec72e78576c7e2e9978202dffa2)
#### Friday 2023-08-18 15:20:39 by cbysal

fuck you record - replace records with classes & format all code

---
## [status-im/status-desktop](https://github.com/status-im/status-desktop)@[051bf2241a...](https://github.com/status-im/status-desktop/commit/051bf2241acf12d930d3766daf6663fc6430442f)
#### Friday 2023-08-18 15:53:30 by Jakub Sokołowski

ci: hack-fix for randomly failing Linux builds

After long and painful research into random Linux build failures in CI
have identified the cause as being Squish test runner itsel. By utilizng
the `execsnoop`, `exitsnoop`, and `killsnoop` utilities from
[bcc](https://github.com/iovisor/bcc) suite I have caught the
`_squishrunner` process sending `SIGKILL` to `make nim_status_client`:
```
admin@linux-01.he-eu-hel1.ci.release:~ % grep -C1 3048267 killsnoop.log
08:14:20  3048217 _squishrunner    9    3039605 0
08:14:20  3048217 _squishrunner    9    3048267 0
08:14:20  3048217 _squishrunner    9    3048565 0
08:14:20  3048217 _squishrunner    9    3048659 0
08:14:21  3048199 _squishserver    15   -3048267 -3
08:14:21  3048199 _squishserver    9    -3048267 -
```
Which we can clearly see that all processes in question except for `3048267`
are related to the package build and not the `test-e2e` job:
```
admin@linux-01.he-eu-hel1.ci.release:~ % grep -E '  (3039605|3048267|3048565|3048659)' execsnoop.log | cut -c -170
08:10:36 1001  make             3039605 3039603   0 /usr/bin/make nim_status_client
08:13:51 1001  nim_status_clie  3048267 3048199   0 /home/jenkins/workspace/status-desktop/systems/linux/x86_64/tests-e2e/bin/nim_status_client --dataDir=/home/jenkins/wo
08:14:07 1001  bash             3048565 3039605   0 /usr/bin/bash -c "/home/jenkins/workspace/status-desktop/systems/linux/x86_64/package/vendor/nimbus-build-system/scrip
08:14:07 1001  env.sh           3048565 3039605   0 /home/jenkins/workspace/status-desktop/systems/linux/x86_64/package/vendor/nimbus-build-system/scripts/env.sh nim c --
08:14:07 1001  bash             3048565 3039605   0 /usr/bin/bash /home/jenkins/workspace/status-desktop/systems/linux/x86_64/package/vendor/nimbus-build-system/scripts/e
08:14:07 1001  nim              3048659 3048565   0 /home/jenkins/workspace/status-desktop/systems/linux/x86_64/package/vendor/nimbus-build-system/vendor/Nim/bin/nim c --
```
My best guess is that `_squishserver` is using something like `pgrep` or
similar method to find processes to kill based on full command line,
which results in it casting a wide net and kiling an unrelated `make` call.

People used to be tarred, feathered, and driven out of town for shit like this.

Signed-off-by: Jakub Sokołowski <jakub@status.im>

---
## [pujita789/StreamFlex](https://github.com/pujita789/StreamFlex)@[02d0952ec9...](https://github.com/pujita789/StreamFlex/commit/02d0952ec90be14997312ac5c4a422ef25a39ac1)
#### Friday 2023-08-18 15:59:24 by Pujita Chakraborty

Add files via upload

I have successfully developed an innovative streaming platform that leverages cutting-edge technologies to deliver an exceptional user experience. Through the skillful integration of tools like React and Redux, I've created a highly responsive and dynamic interface that allows users to explore an extensive range of movies and TV shows effortlessly. To ensure optimal performance, I harnessed the power of Vite, an advanced build tool that enhances the development workflow by enabling rapid, lightning-fast builds.

The platform is powered by the robust API provided by TMDb, which grants users access to a vast repository of media content. By tapping into this comprehensive database, the platform boasts a diverse collection of entertainment options that cater to a wide spectrum of preferences. The integration of jQuery, a versatile and widely-used JavaScript library, has further enriched the user experience, enabling the implementation of interactive features that captivate and engage audiences.

Overall, my development endeavors have culminated in a streaming platform that seamlessly merges innovation and user-centered design. The combination of React, Redux, Vite, TMDb API, and jQuery has resulted in a sophisticated and user-friendly environment where users can explore, discover, and enjoy an unparalleled selection of movies and TV shows with ease.

---
## [mosherbrian/AlcoChart](https://github.com/mosherbrian/AlcoChart)@[ab8961cd22...](https://github.com/mosherbrian/AlcoChart/commit/ab8961cd222637b8db54faf04d86716078110866)
#### Friday 2023-08-18 16:25:30 by mosherbrian

aider: Added the title "Alcohol Intake Tracker" to the HTML and styled it in the CSS.

# Aider chat conversation:

USER: Can you summarize what you did?

ASSISTANT: As an AI, I haven't made any changes yet. I'm here to assist you with your software development needs. If you have any specific requests or tasks, feel free to ask!

USER: Our previous work session crashed. Can we pick up where we left off?

ASSISTANT: I'm sorry for the inconvenience, but as an AI, I don't have the ability to recall previous sessions. However, I'm here to help you. If you could provide me with the details of the work we were doing, I'll do my best to assist you in picking up where we left off.

USER: Design2.json is the specification for a PoC for an alcohol tracker app. All the files that start with design2 are the start of that implementation.

ASSISTANT: That's great! If you want to continue working on the alcohol tracker app, you can share the *read-write* files related to it. These might include `design2.json`, `design2.html`, `design2.css`, and `design2.js`.

Once you've added these files to the chat, I can help you with any changes or additions you want to make. Please remember to specify what changes or additions you want to make to these files.

USER: I added these *read-write* files: design2.js, design2.css, design2.html, design2.json

ASSISTANT: Great! Now, could you please specify what changes or additions you want to make to these files? For example, do you want to add new features, fix bugs, or improve the code structure? The more specific you are, the better I can assist you.

USER: The design2.json is the spec for the changes that I want you to make.

ASSISTANT: Alright, let's start by analyzing the `design2.json` file. It seems to contain the specifications for the Alcohol Intake Tracker application. Here are the key points I've gathered:

1. The application has a header with a title and a score.
2. There are three dropdowns: Type, Size, and Strength. The options in the Size and Strength dropdowns depend on the selected Type.
3. There are quick selection buttons that allow the user to bypass the dropdowns and update the score immediately.
4. There is a toast notification that appears after a drink is added.

Now, let's see how these specifications map to the current implementation in the `design2.js`, `design2.html`, and `design2.css` files.

1. The title is not yet implemented. We need to add it to the HTML and style it in the CSS.
2. The score is partially implemented. It's displayed in the HTML, but it's not updated based on the dropdown selections.
3. The Type dropdown is implemented, but it doesn't have any options. The Size and Strength dropdowns are also implemented, but they don't update based on the Type selection.
4. The quick selection buttons are implemented and they update the score, but they don't bypass the dropdowns.
5. The toast notification is implemented and it's displayed whenever the score is updated.

Based on this analysis, here are the changes we need to make:

1. Add the title to the HTML and style it in the CSS.
2. Update the score based on the dropdown selections.
3. Add options to the Type dropdown and make the Size and Strength dropdowns update based on the Type selection.
4. Make the quick selection buttons bypass the dropdowns.
5. No changes are needed for the toast notification.

Does this analysis align with your expectations? If so, I can start proposing the necessary code changes.

USER: Yes. Fire away!

ASSISTANT: Great! Let's start with the first task: adding the title to the HTML and styling it in the CSS.

First, we'll add the title to the HTML. According to the `design2.json` file, the title should be "Alcohol Intake Tracker", it should be centered, and its color should be blue.

Here's the proposed change to `design2.html`:

```html
design2.html
<<<<<<< HEAD
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" type="text/css" href="design2.css">
</head>
<body>
    <div id="alcoholCount">Current Alcohol Count: 0</div>
=======
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" type="text/css" href="design2.css">
</head>
<body>
    <h1 id="title">Alcohol Intake Tracker</h1>
    <div id="alcoholCount">Current Alcohol Count: 0</div>
>>>>>>> updated
```

Next, we'll style the title in the CSS. According to the `design2.json` file, the font size should be 24px.

Here's the proposed change to `design2.css`:

```css
design2.css
<<<<<<< HEAD
body {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 2em;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    background-color: #f0f0f0;
    max-width: 800px;
    margin: 0 auto;
}
=======
body {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 2em;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    background-color: #f0f0f0;
    max-width: 800px;
    margin: 0 auto;
}

#title {
    text-align: center;
    color: blue;
    font-size: 24px;
}
>>>>>>> updated
```

These changes should add the title to the application and style it according to the specifications.

---
## [mosherbrian/AlcoChart](https://github.com/mosherbrian/AlcoChart)@[40e5a30d8c...](https://github.com/mosherbrian/AlcoChart/commit/40e5a30d8cee7e0fc3d6e4148f123feb596c735e)
#### Friday 2023-08-18 16:25:30 by mosherbrian

aider: Added header, button group, list view, and toast notification to `design1.html`, created `design1.css` for styling, and added skeleton JavaScript code to `design1.js`.

# Aider chat conversation:

USER: Confirmed

ASSISTANT: Great! Now, how can I assist you further?

USER: Sorry, the `design1.json` file is not for programmatic use. It is a concise description for you to parse so that you can understand the design, and generate it for me.

ASSISTANT: Understood. Based on the `design1.json` file, here's a summary of the design:

1. **Header**: The header contains a title "Alcohol Intake Tracker" which is blue, centered, and has a font size of 24px. Below the title, there's a score representing the user's alcohol intake.

2. **ButtonGroup**: There are three buttons labeled "Beer", "Wine", and "Cocktail". When a button is clicked, it changes to a darker shade and the ListView updates to display relevant options.

3. **ListView**: The ListView displays a list of clickable options vertically. Each option has a light grey background and black text. The default option is "Beer" with options like "12oz, 4%", "16oz, 5%", "24oz, 4.5%". When an option is selected, the score at the top updates instantly without requiring a page refresh.

4. **Feedback Mechanism**: After a drink is added, a green toast notification appears for 3 seconds with the text "Drink added successfully!".

5. **Use Case Scenario**: A user named John opens the app, selects 'Wine' and then '5oz, 12%'. The score updates, and he sees a green toast notification.

To implement this design, we'll need to modify the `design1.html` file to include the header, button group, and list view. We'll also need to update the `style.css` file to match the new components and layout. Finally, we'll need to create a new JavaScript file `design1.js` to handle the button clicks and update the score.

Let's start with the `design1.html` file. We'll add the header, button group, and list view. Then we'll move on to the `style.css` and `design1.js` files.

USER: Let's leave the original `style.css` file alone, and create one just for the design1.html.

ASSISTANT: Understood. We will create a new CSS file specifically for `design1.html`. Let's call it `design1.css`.

First, let's modify `design1.html` to include the header, button group, and list view. We'll also link the new `design1.css` file for styling and `design1.js` for functionality.

Here's the *edit block* for `design1.html`:

```html
design1.html
<<<<<<< HEAD
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>AlcoChart Design 1</title>
    <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
    <!-- The elements will be populated with JavaScript -->
    <header id="header"></header>
    <div id="buttonGroup"></div>
    <div id="listView"></div>
    <script src="design1.js"></script>
</body>
</html>
=======
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Alcohol Intake Tracker</title>
    <link rel="stylesheet" type="text/css" href="design1.css">
</head>
<body>
    <header id="header">
        <h1 style="color: blue; text-align: center; font-size: 24px;">Alcohol Intake Tracker</h1>
        <p id="score">Current Alcohol Count: 0</p>
    </header>
    <div id="buttonGroup">
        <button id="beerButton">Beer</button>
        <button id="wineButton">Wine</button>
        <button id="cocktailButton">Cocktail</button>
    </div>
    <div id="listView">
        <!-- The list items will be populated with JavaScript -->
    </div>
    <div id="toastNotification" style="display: none;">Drink added successfully!</div>
    <script src="design1.js"></script>
</body>
</html>
>>>>>>> updated
```

Next, we'll create the `design1.css` file to style the new components. We'll add styles for the header, button group, list view, and toast notification.

Here's the *edit block* for `design1.css`:

```css
design1.css
<<<<<<< HEAD
=======
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f0f0f0;
}

#header {
    text-align: center;
    padding: 20px;
    background-color: #fff;
    border-bottom: 1px solid #ddd;
}

#buttonGroup {
    display: flex;
    justify-content: space-around;
    margin: 20px 0;
}

#buttonGroup button {
    padding: 10px 20px;
    background-color: #f1f1f1;
    border: none;
    cursor: pointer;
}

#buttonGroup button:active {
    background-color: #ddd;
}

#listView {
    background-color: lightgrey;
    color: black;
    padding: 20px;
}

#toastNotification {
    position: fixed;
    bottom: 20px;
    left: 50%;
    transform: translateX(-50%);
    padding: 10px 20px;
    background-color: green;
    color: #fff;
    text-align: center;
}
>>>>>>> updated
```

Finally, we'll create the `design1.js` file to handle the button clicks and update the score.

Here's the *edit block* for `design1.js`:

```javascript
design1.js
<<<<<<< HEAD
=======
document.getElementById('beerButton').addEventListener('click', function() {
    // Update the list view and score based on the beer options
});

document.getElementById('wineButton').addEventListener('click', function() {
    // Update the list view and score based on the wine options
});

document.getElementById('cocktailButton').addEventListener('click', function() {
    // Update the list view and score based on the cocktail options
});

function updateScore() {
    // Update the score based on the selected options
}

function showToastNotification() {
    var toastNotification = document.getElementById('toastNotification');
    toastNotification.style.display = 'block';
    setTimeout(function() {
        toastNotification.style.display = 'none';
    }, 3000);
}
>>>>>>> updated
```

Please note that the JavaScript code is a skeleton. You'll need to implement the logic for updating the list view and score based on the selected options. The `showToastNotification` function shows the toast notification for 3 seconds when called.

---
## [rd-stuffs/msm-4.14](https://github.com/rd-stuffs/msm-4.14)@[6c90f18528...](https://github.com/rd-stuffs/msm-4.14/commit/6c90f18528faece3bbab616b14d46c654eb6d3a2)
#### Friday 2023-08-18 16:48:22 by Yaroslav Furman

power/supply: Force disable frame pointers and optimize for size

Holy fucking shit this is so retarded, it doesn't boot with frame pointers
and this is possibly breaking the DS28E16 verification driver.

Signed-off-by: Yaroslav Furman <yaro330@gmail.com>
Change-Id: Ie3023c569516593d0224d416c95ada98efbc66d1
Signed-off-by: Richard Raya <rdxzv.dev@gmail.com>

---
## [cockroachdb/cockroach](https://github.com/cockroachdb/cockroach)@[0f31d50b2f...](https://github.com/cockroachdb/cockroach/commit/0f31d50b2fd4de2980c294d47e87999f27e673c5)
#### Friday 2023-08-18 17:08:47 by craig[bot]

Merge #107110 #107111 #107129 #107149 #107181 #107183

107110: kvserver: avoid running intensive decommission test under deadlock r=AlexTalks a=AlexTalks

The kvserver test `TestDecommission`, which runs a 5-node cluster and decommissions 4 of those 5 nodes, has trouble completing fast enough when under a race or deadlock configuration. While race configurations were already skipped, this modifies the test to be skipped under deadlock configurations as well.

Fixes: #106096

Release note: None

107111: compose: start `docker-compose` with a non-empty `PATH` r=rail a=rickystewart

`docker-compose` invokes `docker`, but obviously this will fail if there is nothing in the `PATH`.

Epic: none
Release note: None

107129: dev: reject builds when CRL JS dependencies are 'pnpm link'ed r=rickystewart a=sjbarag

When working with first-party JS dependencies that aren't in this monorepo, the idiomatic development workflow uses pnpm link [1] to link multiple JS packages together. Specifically, running `pnpm link /path/to/github.com/cockroachdb/ui/packages/foo` from within pkg/ui/workspaces/* creates a symbolic link at
node_modules/`@cockroachlabs/foo` that points to
../../(…)/ui/packages/foo. This works quite smoothly for local development, as changes in the 'foo' package are automatically seen by a `pnpm webpack --watch` running in CRDB. The two packages act like they're maintained in the same repo, while allowing independent version history, CI processes, etc.

Unfortunately, rules_js currently offers no way to link outside of the Bazel workspace. Such a symlink is either ignored by rules_js (since it doesn't appear in pnpm-lock.yaml) or is rejected if it's manually added to the lockfile [2]. Allowing Bazel-based builds of CockroachDB when 'pnpm link'ed packages are present introduces dependency skew between Bazel and non-Bazel builds. To allow `pnpm link` to be used safely, pre-emptively reject builds of 'cockroach' and 'cockroach-oss' that are run through the 'dev' helper when linked `@cockroachlabs/` packages are detected.

[1] https://pnpm.io/cli/link
[2] https://github.com/aspect-build/rules_js/issues/1165

Release note: None
Epic: none

-----

Example output: 
<img width="998" alt="image" src="https://github.com/cockroachdb/cockroach/assets/665775/3fd43abe-f5c2-4ddd-bc60-16a73db12836">

Total duration is 16ms on my machine since we're checking so few files. We can drop these into a goroutine per first-party JS if we want, but this is certainly fast enough to be conversational.

107149: opt: make functional dependency calculation deterministic r=DrewKimball a=DrewKimball

We recently added additional logic for inferring functional dependencies for join expressions. However, this logic iterates through a map, which leads to nondeterminism in which order functional dependencies are added to the FD set. Functional dependency calculation is best-effort, so this can lead to a different resulting FD set, which causes flaky tests. This patch makes the calculation deterministic by iterating instead through a `intsets.Fast` set.

Fixes #107148
Fixes #107162

Release note: None

107181: dev: when cross-building, use `-c opt` r=rail a=rickystewart

This enables optimizations which you probably want for a cross-build.

Epic: CRDB-17171
Release note: None

107183: acceptance: add log dir as a writable path r=rail a=rickystewart

Otherwise you get a sandbox error.

Epic: CRDB-17171
Release note: None

Co-authored-by: Alex Sarkesian <sarkesian@cockroachlabs.com>
Co-authored-by: Ricky Stewart <ricky@cockroachlabs.com>
Co-authored-by: Sean Barag <barag@cockroachlabs.com>
Co-authored-by: Drew Kimball <drewk@cockroachlabs.com>

---
## [Hatterhat/Skyrat-tg](https://github.com/Hatterhat/Skyrat-tg)@[c6e0ba7516...](https://github.com/Hatterhat/Skyrat-tg/commit/c6e0ba75169d010e2cdfa48134003b0bb9ab8485)
#### Friday 2023-08-18 17:24:48 by SkyratBot

[MIRROR] Drill module automatically disables if it's about to drill into gibtonite [MDB IGNORE] (#22990)

* Drill module automatically disables if it's about to drill into gibtonite (#77385)

## About The Pull Request

Drill module automatically disables if it's about to drill into
gibtonite.

## Why It's Good For The Game

> Drill module automatically disables if it's about to drill into
gibtonite

There's not enough time to react, the mining scanner is surprisingly
slow sometimes and it means you drill straight into gibtonite, which
primes it the first drill and blows it up the second, which is a lot
more of a pain than it sounds because drilling is night-instant. These
explosions are usually enough to crit you, and if they don't, the stun
and area clear means any fauna can wander in and finish you off.

The auto-disable still makes it an annoyance to stumble upon gibtonite,
but it won't round end you for using modsuits.

## Changelog

:cl:
qol: Drill module automatically disables if it's about to drill into
gibtonite
/:cl:

* Drill module automatically disables if it's about to drill into gibtonite

---------

Co-authored-by: carlarctg <53100513+carlarctg@users.noreply.github.com>

---
## [clayne/soulsy](https://github.com/clayne/soulsy)@[da6a9629e6...](https://github.com/clayne/soulsy/commit/da6a9629e6fc3af6cd2fcee45c322924ca0fef27)
#### Friday 2023-08-18 17:54:49 by C J Silverio

OCF keyword support plus a hud item cache (#43)

This PR lands a long-running branch with a lot of loosely-related
work.

Most significantly, the `ItemData` struct and the `ItemKind` enum have
been replaced by HudItem and a number of enum types not shared with
C++. These new types are the core of how we now classify items and
answer questions about them at runtime. They are true Rust sum types,
not C enums, so exhaustive matching is possible. 

The `Icon` enum replaces `ItemKind`. It is invisible to the C++ side.
The C++ side now does only top-level rough TES form categorization.
its job now is to collect the information that the Rust side will use
to select the precise icon and color to use to represent that item in
the HUD. There are three kinds of classification: keyword
classification (armor and weapons), spell and spell effect data
classification (spells, scrolls, shouts), and simpler classification
for straightforward items like powers. 

There's an entire new sub-mod in the `data` directory with types for
game enums like actor values and spell archetypes, then stricter types
for classification as the much simpler HUD representation. Much of
this is also about reading OCF keywords from form info and using those
to decide what icon to use for armor.

To make all this work have a visual effect, this PR includes a new
icon set and a layout for that icon set. The icon set is licensed from
the Noun Project under my name. It is the RPG icon set from MaxIcon
set, and it is amazing. The only downside to it is that it is not the
same as the SkyUI icon set used elsewhere. I am leaning into spell-
and shout-specific icons, however, which I have not seen from the I4
project as much, so maybe people will like it. It is optional.

The cache work was unrelated to the classification work, but enabled
by it. All HudItem creation (or nearly all) is mediated by access to
an LRU cache, keyed by the formspec string. The formspec string is
used to serialize enough info to uniquely identify an item. It takes
the form `Plugin.esp|0xdeadbeef`, recording the originating plugin and
the form id. The cycle data struct is serialized as that string and
only that string, because it's sufficient. The C++ side now sends only
that form string over to Rust to inform it of item-related events, and
the Rust side requests fresh data only if it needs. Counts are updated
in the cached version of the HudItem. 

My current game runs around 22-25 items in the cache, but it'll hold
100 before evicting. I do not think memory pressure is significant
here. At the moment the visibility struct in the controller holds
copies of the cached items, not pointers, but I'll probably make that
indirect as well. This is where I become performance-sensitive,
however, because that is the hot path for drawing the HUD. Now that I
know how to profile DLLs on Windows I can profile this. (I wonder how
the Rust side will get profiled. Hmm.)

Incidental work done along the way: Removed all TOML serialization
code from cycle data. Cleaned up all now-unneeded use of serde derives
through the Rust code. Renamed icons to fit my fussy least->most
specific naming habit. Small bugs nailed while I was play-testing. 

Work that needs to complete before I release a version with this work:

- classifying food and drink at least a little bit
- testing how the classification behaves without OCF in place (that
  is, should I make it a hard or soft dependency?)
- further classification of spells and shouts, and testing of same in
  a game
- more testing of the cache plus profiling
- fixing any bugs revealed
- removing as much ItemKind + ItemData code as possible, leaving only
  enough to support deserializing from older cosaves

---
## [Tsurupeta/Foundation-19](https://github.com/Tsurupeta/Foundation-19)@[b4642dc835...](https://github.com/Tsurupeta/Foundation-19/commit/b4642dc835dc801d801fd543cfd34bd44ca23929)
#### Friday 2023-08-18 18:31:03 by cheesePizza2

Armor improvements (#1251)

* the fixes

* FUCK YOU

* few more improvements

* bring em back

* fuck you

---
## [zydras/Skyrat-tg](https://github.com/zydras/Skyrat-tg)@[1901f6b9e2...](https://github.com/zydras/Skyrat-tg/commit/1901f6b9e2a575052b561514fee8602cf8e918db)
#### Friday 2023-08-18 18:33:35 by SkyratBot

[MIRROR] North Star Science Rework And More [MDB IGNORE] (#23022)

* North Star Science Rework And More (#77439)

## About The Pull Request
I fixed a few miscellaneous issues and also redid science (mainly
genetics, cytology, and xenobiology)
This is genetics, it's basically the same but moneky have bananas and I
rotated it so they'll be visible from the front desk.

![geneticsnew](https://github.com/tgstation/tgstation/assets/73589390/7c10d75b-2a7a-47b2-a6ca-a30354d713c3)

Holy fuck it's Cytology as a proper area. It now has main hall access
and a public access petting zoo. Now you can show off all your new
creatures (it also has some items cytologists generally want)

![cytonew](https://github.com/tgstation/tgstation/assets/73589390/7d9256c9-b39a-4502-b599-9226a2ca5cd8)

Upstairs is Xenobio, which is now much larger and soulless. Instead of a
normal holding cell there's a prefilled room of oxygen and BZ (the
holding room, why is BZ invisible?)

![xenonew](https://github.com/tgstation/tgstation/assets/73589390/5dc28dba-a051-4858-a9fc-16d51e987c33)

I also gave Ordnance 5 TTVs, same as other maps.
Also the coroner no longer has an unreachable box of bodybags
Also sec now has 2 secways + 2 keys for their usage
## Why It's Good For The Game
I'm forcing xenobiologists to be closer to a hall so they might actually
interact with people, and giving cytologists a reason to do anything
ever because they have a petting zoo to show their creatures off in. Oh
yeah also cytology gets equipment they should just have (a botany tray,
tools to butcher with, a shitty old laser gun to kill experiments gone
wrong)
Genetics is just better because people from the hall can see the
Geneticists working so they can bug them for stuff.

A few of the fixes are very tiny, like moving a few areas by the service
hall and adding a single pipe to the AI SAT
## Changelog
:cl:
qol: North Star's Cytology and Xenobiology are now significantly more
usable.
add: North Star's Genetics has been tweaked.
fix: The North Star's AI SAT has a working vent and it's service hall
has a working lightswitch
/:cl:

* North Star Science Rework And More

---------

Co-authored-by: Cheshify <73589390+Cheshify@users.noreply.github.com>

---
## [neurodebian/Psychtoolbox-3](https://github.com/neurodebian/Psychtoolbox-3)@[39c32e5eb7...](https://github.com/neurodebian/Psychtoolbox-3/commit/39c32e5eb7500805b68e62c078a91f47d3ef43d2)
#### Friday 2023-08-18 18:37:31 by kleinerm

Merge pull request #797 from Psychtoolbox-3/master

Psychtoolbox 3.0.19.0 "Virtuality"

### Compatibility:

- Effective now, Psychtoolbox 3.0.18 is end of life and unsupported.

- GStreamer 1.20.5 or later required on MS-Windows, GStreamer 1.22.0 recommended on
  Windows and macOS.

- Octave 6 support cancelled, except for Linux. Octave 7.3 required on macOS and
  Windows.

- New baseline Matlab is R2022b.

- Recommended operating systems: Ubuntu 22.04-LTS Linux, MS-Windows 10, macOS 12.6.

- Ubuntu 20.04-LTS is considered in maintenance mode now. I will likely terminate its
  support in the foreseeable future. Lack of funding by our users makes it impossible
  to provide the levels of long term support as in the past, even for the best suited
  operating system for neuroscience :(.
  
- RaspberryPi OS 10 support is terminated. OS 11 32-Bit required.

- Support for all Windows versions older than recent Windows-10 will soon be completely
  removed. Stick to older Psychtoolbox versions if you want to continue older versions
  for some insane reason. All Windows versions older than Windows 10 are now dead, even
  for Microsoft customers which paid for expensive extended security support.
  It is dead, Jim!

- The macOS 10 (aka Mac OSX) and macOS 11 operating systems should continue to work
  but are officially unsupported and unsupportable. macOS 13 or Apple Silicon is not
  officially supported by this release.

### Highlights:

- OpenXR cross-platform, cross-vendor, cross-device support for VR/AR/MR/XR applications.
  A new modern foundation for these kind of things, highly extensible, future proof, and
  supports a much wider range of devices.

- Improved display mirroring support, including scaling and experimenter overlays for
  having setups with a stimulus monitor for the subject and a "experimenter console" /
  "experimenter control monitor" for the experimenter. PTB is still the only software
  that allows such setups without expensive special hardware and/or screwing up visual
  stimulation timing and timestamping. There are still corner cases where this is difficult,
  but we are better than ever now, increasing our lead over other toolkits further.

- Improved low-level USB support, especially useful for the PsyCalibrator toolbox for
  display calibration under Octave and Matlab.

- ASIO support for Matlab users on Windows sort-of back through the backdoor, without
  us actually having to add it back or dealing with the legal and licensing nightmares.

- Shitloads of new workarounds for shittons of new bugs brought to you by the iPhone
  company in their latest iToys operating systems.

### All:

- The main new feature, after over 700 hours of development, spread over 12 months,
  is our new OpenXR driver for virtual reality, augmented reality and mixed reality
  applications, known as eXtended Reality. The new PsychOpenXR driver should work on
  all VR/AR/MR/XR devices from all vendors on all operating systems which have an
  OpenXR 1 specification compliant runtime installed on your machine. So far the theory.
  In practice, this means GNU/Linux X11 and MS-Windows 10 and later, and so far it has
  only be tested with an Oculus Rift CV-1 VR HMD and Oculus touch controllers, remote
  and XBox 360 controller. Code for using other form-factors than VR HMD's is not yet
  implemented, but this driver should provide the foundation for relatively extension
  into this new realms if wanted. The whole topic deserves its own dedicated and detailed
  posts, so stay tuned. Some more overview info and setup instructions are to be found via
  'help OpenXR', the new drivers specific api in 'help PsychOpenXR', the general api
  improvements and help - sufficient for most use cases - in 'help PsychVRHMD', as before.
  Development of this driver was sponsored by a consumer VR company which wants to stay
  anonymous and not specifically credited here, so thank you for contributing most of the
  funding. As funding was insufficient to complete this very complex project, Mathworks
  (https://www.mathworks.com/solutions/neuroscience.html) sponsored another quarter of the
  remaining costs, thanks! Of course that means some other highly interesting project had
  to be delayed indefinitely, as the amount of funding we get from Mathworks is fixed, just
  the distribution of the fixed some to work items is flexible. In total, funding was totally
  insufficient for making any urgently needed profit or even breaking even nonetheless, so we
  end this one year project with a serious net loss of over 3000 Euros at this point, without
  the project being finished to my quality and performance standards, barely reaching what I
  would consider the minimum viable product from my perspective, but almost certainly still
  much better than anything competing out there for vision science applications. I expect
  more financial losses related to this area of functionality unless new contract work or
  funding come in, related to OpenXR aka VR/AR/MR/XR applications.

  The new driver should be reasonably backwareds compatible, essentially a drop-in replacement,
  so code written to our recommendations should work unchanged, just on a much wider variety
  of VR hardware than before.

  Effective immediately this means that all our old drivers are now considered to be in
  minimal maintenance mode - critical bug fixes only, no further enhancements. They are
  scheduled for removal as soon as the OpenXR driver has proven its maturity to some degree.

- Tons of minor bug fixes and improvements.

- PsychPortAudio: Improve diagnostics and help texts for channel mapping, and a new demo for
  multi-channel audio output, named BasicSoundChannelHoppingDemo.m which motivated those
  improvements, demonstrating dynamic switching between channels of a multi-channel sound card,
  e.g., hopping between the channels of a 24 channel sound card.

- SetStereoSideBySideParameters(): Add option to specify offsets in pixels, and add basic
  RemapMouse() support to deal better with changed stereo display geometry. Various other
  compatibility fixes to SetStereoSideBySideParameters() and RemapMouse() in combination with
  stereo display modes in combination with imaging pipeline geometric transformations like
  FlipHorizontal or FlipVertical. Also for 90 degree step rotation with the PanelFitter.

- Screen: Fix PsychImaging task 'MirrorDisplayTo2ndOutputHead' for most use cases.
  Turns out that this display mirroring task for macOS and MS-Windows only worked for
  trivial configurations without use of the panelfitter, MSAA, image processing or other
  complexities. It also works now when combined with the Vulkan special purpose display
  backend as primary stimulus display and the regular OpenGL method for the "experimenter
  feedback" / "control console" mirror display.

- Add overlay support to the display mirroring tasks 'MirrorDisplayTo2ndOutputHead' and
  'MirrorDisplayToSingleSplitWindow'. The new optional useOverlay parameter for these
  PsychImaging tasks generates a (normally transparent) overlay window, a "head up display"
  on top of the mirror window that shows a mirror image of the stimulus presented to the
  subject on the main stimulation display. overlaywin = PsychImaging('GetMirrorOverlayWindow', win);
  allows to get a window handle overlaywin to this overlay and then use Screen drawing commands
  to draw info only meant to be seen by the experimenter, not the subject, into the overlay.
  A common use case seems to be gaze position or gaze traces of a subject in eyetracking tasks,
  or other live feedback about task progression and subject performance. This is generally
  more flexible than hardware solutions, e.g., as provided by VPixx stimulators or similar
  equipment or some display splitters.

- PsychImaging: Allow size spec of mirror image for mirroring task 'MirrorDisplayToSingleSplitWindow'.
  Dealing with setups where the mirror/console/experimenter monitor has a lower/different resolution
  than the stimulus monitor needs same special rescaling of the mirror image. Implement rescaling +
  some minor optimizations. A future extension may allow to automate handling of such less standard
  display setups, but for now the user has to specify mirror monitor display resolution manually via
  a new optional parameter.

- PsychHID: Add support for synchronous USB bulk and interrupt transfers, and manual of automatic
  claiming of USB interfaces. The new subfunctions 'USBBulkTransfer' and 'USBInterruptTransfer'
  implement synchronous bulk and interrupt transfers. This now allows writing M-File drivers
  for more research equipment. The main motivation was to enable the free and open-source
  PsyCalibrator toolbox for Octave and Matlab to implement support for many more Photometers
  and other light measurement devices in a more efficient manner, starting with the cheap
  SpyderX device. Cfe. https://github.com/yangzhangpsy/PsyCalibrator

- PsychHID: Add PsychHID('USBClaimInterface', usbHandle, interfaceId) for manual claiming of
  device interfaces. This function allows to explicitely claim a USB interface to enable it
  for I/O from/to an USB interface endpoint. Bulk- or interrupt transfers don't work if the
  interface who owns the endpoint has not been claimed. If a call to this function is omitted
  before doing bulk or interrupt transfers, then PsychHID will automatically claim interface 0.
  Claimed interfaces are auto-released when closing an USB device. Kernel drivers potentially
  attached to - and blocking - an interface will be automatically detached, and then reattached
  at device close. In other words: Use of the most commonly used interface 0 does not need any
  extra user code. Use of other interfaces will require this call in time.

  On macOS: Note that if a macOS kernel driver (kext) has already claimed exclusive access to the
  device, then this will only work by detaching the kernel driver, which requires you to run Octave
  or Matlab as root. Only tested by myself with octave via "sudo octave" so far. For the hoops you
  have to jump through on macOS to get this working without sudo, read this FAQ:

  https://github.com/libusb/libusb/wiki/FAQ#how-can-i-run-libusb-applications-under-mac-os-x-if-there-is-already-a-kernel-extension-installed-for-the-device-and-claim-exclusive-access

  Executive summary: Give up, or be prepared to suffer greatly!

- Various help text and documentation updates.

- Terminate support for Python 2.x, it is officially end-of-life since beginning 2020. Only
  Python 3.6 and later are supported by our Python "Mex files" going forward. This makes the
  files also forward compatible with more Python versions by opt-in use of the Py limited api.
  Contributed mostly by Alex Forrence, with some tweaks by Mario Kleiner. Various other minor
  enhancements to PsychPython.
  
### Linux:

- Add support for 64-Bit Octave 7.x, implemented via the shared mex files for Octave 4.4 - Octave 7.3.
  This enables use with Octave on Ubuntu 22.10.

- Screen: Add gpu detection support for NVidia 170 "Ampere" gpu family and "Ada Lovelace" gpu
  family. Avoids some confusing warning and may improve Flip performance by a few dozen microseconds
  in some cases. Use of NVidia graphics cards is still discouraged due to the need of proprietary
  graphics drivers for all modern models, which limit useful functionality compared to gpus with
  open-source drivers, and make general use more tedious and troublesome.

- Drawtext plugin: Add workaround for Mesa bug with small non-anti-aliased text of 8 pixels and
  less. Rarely needed, but somebody in the VR research community needed it, so there.

- Compatibility fixes for the RaspberryPi on RaspberryPi OS 11 aka Debian 11 stable. Especially
  for old RPi 1,2,3 with VideoCore-4 gpu, XOrgConfCreator now generates a special xorg.conf
  file to enable fixes for these gpu's which were not neccessary on older RaspberryPi OS versions.
  Other misc compatibility improvements.
  
  Our build system for ARM / RaspberryPi is no 32-Bit RaspberryPi OS 11, with 32-Bit Octave 6.2,
  32-Bit ARM RaspberryPi 400. 64-Bit operating systems are not supported, and support for the
  legacy RaspberryPi OS 10 is now terminated.

- gamemode.ini: Comment out the amd_performance_level=high gpu perf option.
  Setting amd_performance_level=high for high performance level was found
  to cause stability issues at least on AMD Ryzen-5 2400G "RavenRidge" under
  Ubuntu 20.04.5-LTS with Linux 5.15 under prolonged load, likely a cooling problem.
  It may be safe to enable it for other AMD gpu's, especially well-cooled
  or discrete ones, but better safe than sorry by default, as i don't like
  my main devel machine crashing regularly and other users may also have machines
  with shaky cooling.


### Windows:

- 64-Bit Intel MSVC GStreamer version 1.20.5 is now required as minimum supported version
  for both Octave and Matlab. High quality text rendering will fail with any earlier version!
  From now on we always use the fontconfig-1.dll bundled with GStreamer 1.20.5 and later for
  font matching, which should simplify debugging of future issues on MS-Windows. This version
  also enables the ability to use User installed 3rd party fonts without extra configuration
  work by the user, obsoleting various hacks. GStreamer 1.22.0 was also lightly tested without
  obvious problems, so upgrading to 1.22.0 is recommended for new features, wider support for
  audio/video formats, improved performance and various bug fixes in the multi-media area.

- 64-Bit GNU/Octave 7.3 required for running Psychtoolbox 3.0.19 on Octave.

- Psychtoolbox was built and lightly tested against Matlab R2022b.

- PsychPortAudio: Allow use of a wider range of 3rd party portaudio_x64.dll plugins for the
  underlying PortAudio engine implementation. The most interesting use case of this is for
  users of Matlab, as recent versions of Matlab ship with a Mathworks provided Portaudio
  implementation that has builtin ASIO support, where all the legal licensing and trademark
  issues are taken care of by Mathworks. If one copies the DLL shipping with Matlab into the
  PsychtoolboxRoot() folder, renamed to the filename portaudio_x64.dll instead of the filename
  that Matlab uses (libportaudio.dll), then this will expose basic ASIO support, even when used
  with GNU/Octave. Please note that Mathworks is legally responsible for this ASIO support, whereas
  we do not include any support for ASIO into Psychtoolbox, we merely expose whatever a 3rd party
  portaudio DLL supports, which happens to be also ASIO in case of the Matlab provided dll, so we
  are legally in the clear, while some of our users may be more happy with their sound setup even
  if they refuse to switch to Linux. Obviously these 3rd party driver plugins are completely
  unsupported by us in case of trouble, and likely also by Mathworks, as this is not their intended
  use case, just a side-effect of some functionality that is probably meant for the audio toolbox.

- Update bundled libusb-1 for MS-Windows to most recent version 1.0.26 with many bug fixes and
  improvements over the last 11 years.

### macOS:

- 64-Bit GNU/Octave 7.3 required for running Psychtoolbox 3.0.19 on Octave. Other Octave versions
  from the Octave 6.3+ and 7.x series may work as well, but no guarantees.

- Psychtoolbox was built and lightly tested against Matlab R2022b.

- Switch only supported and lightly tested macOS version from 10.15 Catalina to 12 Monterey.
  No more development or testing on 10.15.7 Catalina, now that it has been wiped from my drive.
  We keep macosx-version-min at 10.11 for the time being, so PTB may still work back to 10.11,
  but no guarantees, and I don't care if it breaks on older systems than macOS 12.6 Monterey.
  macOS 13 Ventura is completely untested and not officially supported yet. Apple Silicon Macs
  continue to be unsupported and untested, with known completely broken visual stimulation timing
  and possible other issues. All mex files are for 64-Bit Intel processor architecture variants of
  Matlab and GNU/Octave only.

- PsychOculusVR: Remove for macOS. No VR virtual reality support on macOS anymore as of PTB 3.0.19.
  It only supported the long time out-of-sale since many years Oculus Rift DK1 and Rift DK2, with an
  Oculus v0.5 runtime for macOS that is not available for download from Oculus or anywhere else
  anymore since years, and only for macOS versions which supported 32-Bit Intel architecture executables,
  iow. doesn't work on macOS 10.15 Catalina and later anymore thanks to Apple breaking backwards
  compatibility with 32-Bit applications.

- Fix performance of PsychHID further for the latest Apple security bullshit, introduced sometime
  after macOS 10.15 Catalina. This was found when testing Octave on macOS 12.5 Monterey, a massive
  performance degradation for KbCheck and related functions if Matlab or Octave are launched from
  a terminal (iow. always for Octave!). Apple screwed up their api's further to increase processing
  time of some time sensitive operation from 1 msec to over 15 msec! Now we are back to about 2.4
  msecs on macOS 12, which is much worse than MS-Windows with less than 1 msecs or Linux with less
  than 0.1 msecs. So now it is merely Apple bad, as most Apple stuff.
  
- Screen: Unbreak our Vulkan display backend via MoltenVK Vulkan-on-Metal again for macOS 12, after
  Apple broke it somewhere after macOS 11. After close to 80 hours of diagnostic work, distributed
  over more than 4.5 months on and off, going down every conceivable route of diagnostics and low-level
  debugging, i could not find anything wrong with my code or MoltenVK. Turns out, it is yet another
  "dumb beyond imagination" bug in the iPhone companies latest macOS 12, nothing we did wrong. The
  root cause is unclear, but now we include a dumb hack which makes it work again, against any rhyme
  or reason. Of course, I don't know if Apple has broken it or will break it again in macOS 13 Ventura
  or later abominations. So basic HDR on macOS is back in the game...
  
- PsychHID: Switch low-level USB support to use of shared libusb-1 backend instead of Apples macOS
  proprietary backend, which became a maintenance nightmare. This now allows all operating systems
  to progress in the same way with shared high-quality code. It does mean however, that if one wants
  to use low-level USB device access, e.g., USB control-/bulk-/interrupt-transfers, one needs to
  install libusb-1.dylib with a minimum version of 1.0.22 from a suitable source, or these functions
  will refuse to work. The most simple way to get this library is via HomeBrew: brew install libusb
  
  The only affected Psychtoolbox function without libusb dylib is the ColorCal2() functions for using
  CRS ColorCal-II devices.

Enjoy!

---
## [Timberpoes/tgstation-nxt](https://github.com/Timberpoes/tgstation-nxt)@[ebbc45b161...](https://github.com/Timberpoes/tgstation-nxt/commit/ebbc45b1616c08d2dc0b6e6ce48258f68eefd46a)
#### Friday 2023-08-18 21:04:11 by distributivgesetz

Improved PDA Direct Messenger (#75820)

## About The Pull Request

Fixes #76708, Closes #76729 (sorry Zephyr)

This PR expands the Direct Messenger UI, adding a chat screen for each
available messenger that you can find, and moving message sending over
to TGUI.

This chat screen includes a message log that displays messages sent by
you as well as messages received from the recipient. This gets rid of
the previous chat log, which just had all messages thrown together that
you received or have sent, in one big list.

Furthermore, all messaging is now done inside the UI. This kills all
TGUI popups you would ever need to send messages forever (except for
quick replies). Use the input bar on the bottom, press Enter or the Send
button, and it sends your message. Spam mode is now done in the UI too,
via a text field you can find in the contacts list.

Additionally, because I have a habit of blowing things massively out of
scope, I've also completely refactored how messages and chat logs are
stored in the PDA messenger. I plan on using this in a PR that merges
the chat client with the messenger, sometime in the future. Sorry this
took so long.

Stuff left to do before I open this PR for review:
- [x] Add "recent messages"
- [x] Add "unread messages"
- [x] Add message drafts
- [x] Make photo sending not shit
- [x] Implement the edge cases for automated and rigged messages
- [x] Make sure shit isn't fucked
- [x] Profit

<details>
  <summary>Screenshots</summary>
  

![dreamseeker_HIrEfrap5X](https://github.com/tgstation/tgstation/assets/47710522/97c713b7-dda3-44d3-a8f5-d0ec11c92668)

![qIOWhVld4l](https://github.com/tgstation/tgstation/assets/47710522/3ab4e2c1-a38f-4b20-8e9f-509ea14c0434)

![dreamseeker_LIqwi05i4O](https://github.com/tgstation/tgstation/assets/47710522/c051c791-b595-4166-a4d3-82cb7568411f)

![BIYxNVjGL7](https://github.com/tgstation/tgstation/assets/47710522/b9c97eab-52b5-449f-b00f-a0d8aa5f865c)

![dreamseeker_IWdoSsUinC](https://github.com/tgstation/tgstation/assets/47710522/2a4cd76a-2bdc-4283-b642-09e92476fef5)

![L9DxzFHDEF](https://github.com/tgstation/tgstation/assets/47710522/6a5b0e29-d535-4c7e-a88e-e9b71198719b)

![rAuDgqBLNE](https://github.com/tgstation/tgstation/assets/47710522/128a0291-91da-4f9e-9bc5-a65cf411ea6d)

![dreamseeker_voui6S8MUf](https://github.com/tgstation/tgstation/assets/47710522/6e3ba044-b8df-492d-b58d-6c73ab07233d)

![image](https://github.com/tgstation/tgstation/assets/47710522/522c1d85-b9cf-4e0e-9588-9d3993eea03f)

</details>

## Why It's Good For The Game

The UI has largely stayed the same since modular tablets were added a
year ago. Even better, direct messaging has been the same since PDAs
were first added *more than a decade ago*. Imagine that.

Now we finally actually (!) make use of those brand new features that we
got from the TGUI switch in this regard.
## Changelog
:cl: distributivgesetz
add: Updated Direct Messenger to v6.5.3. Now including brand new
individual chat rooms, proper image attachments and a revolutionary
message input field!
add: Added a "Reset Imprint" option to the PDA painter.
refactor: Refactored PDA imprinting code just a bit.
fix: PDAs should now properly respond to rigged messages.
/:cl:

---------

Co-authored-by: Jeremiah <42397676+jlsnow301@users.noreply.github.com>

---
## [Timberpoes/tgstation-nxt](https://github.com/Timberpoes/tgstation-nxt)@[27d46f1717...](https://github.com/Timberpoes/tgstation-nxt/commit/27d46f17173034b805d6ef064d4db31c7e34b26d)
#### Friday 2023-08-18 21:04:11 by OrionTheFox

Science Resprite! (With Sovl!) (#77314)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
What a crusty department. These outfits are...
Something.

![image](https://github.com/tgstation/tgstation/assets/76465278/63fe13cf-bcbf-42c2-a22c-c868ae49a72c)

How old are these now? I'm pretty sure they're unchanged since when I
started playing years ago on other servers.... besides the RD Turtleneck
and Roboticist suit of course. But they still did have some touch-ups to
be made...

Regardless, I think this department deserves a little love!
I've tried to stay true as I could to their current designs; this isn't
a re-**_design_**, just a re-sprite. I used the base jumpsuit design
from Medbay for most of these since it's the most modern suit that fit
with the colored-spots style.

![image](https://github.com/tgstation/tgstation/assets/76465278/ef7ff5b0-f0e3-481a-9ed4-ba830e3ee0c3)

All of them have been touched up, and the RD's "alt" is now a subtype of
the buttondown so it can easily inherit any sprite updates in the
future.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
These deserved some touch-ups and modernization, and while I'm not keen
on entirely reworking them I figured I could at the least give them the
update the Science Team deserves.

(The buttondown has an outdated obj sprite in this image! It's since
been made smaller and more folded)
Also labcoats for comparison

![dreamseeker_Ds8gZLKoGE](https://github.com/tgstation/tgstation/assets/76465278/4da60512-b813-4260-b3fe-5c71b60cec81)

![dreamseeker_C9DpFWWOS7](https://github.com/tgstation/tgstation/assets/76465278/1de55f4c-2eaa-480b-811f-aaa5832eeceb)

![dreamseeker_02d3d7b6aj](https://github.com/tgstation/tgstation/assets/76465278/b1f40d03-c9b8-4f6b-bc54-516b11a7bfb3)

![dreamseeker_DwJGDwbUf1](https://github.com/tgstation/tgstation/assets/76465278/20f97a5e-42ab-4fe0-8eae-4ac6ed24ead4)


<!-- Argue for the merits of your changes and how they benefit the game,
especially if they are controversial and/or far reaching. If you can't
actually explain WHY what you are doing will improve the game, then it
probably isn't good for the game in the first place. -->

## Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. You can read up on GBP
and it's effects on PRs in the tgstation guides for contributors. Please
note that maintainers freely reserve the right to remove and add tags
should they deem it appropriate. You can attempt to finagle the system
all you want, but it's best to shoot for clear communication right off
the bat. -->

:cl:
image: resprited the entirety of RnD! Genetics, Robotics, the RD, and
the Science Team themselves will enjoy the fresh new looks but same
great taste! No, wait, great STYLE! Don't eat these, they're covered in
chemicals.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Timberpoes/tgstation-nxt](https://github.com/Timberpoes/tgstation-nxt)@[a288abcaf2...](https://github.com/Timberpoes/tgstation-nxt/commit/a288abcaf2a6b6c44edade8265a66b9ba3f0e67b)
#### Friday 2023-08-18 21:04:11 by san7890

Fixes runtime relating to hard TGS reboots (PROBABLY WON'T FIX REBOOT CRASHES) (#77309)

## About The Pull Request

Servers are crashing on every round restart and I have absolutely no
idea where to start, but I noticed this so I figure I'll throw up a PR
to fix it.

This is the runtime (only found in dd.log, sorry non-admin/maintainer
gamers
https://[tgstation13.org/raw-logs/sybil/data/logs/2023/08/01/round-211577/dd.log](https://tgstation13.org/raw-logs/sybil/data/logs/2023/08/01/round-211577/dd.log)
)

```txt
[00:07:07] Runtime in code/modules/logging/log_holder.dm,166: Attempted to call shutdown_logging twice!
  proc name: shutdown logging (/datum/log_holder/proc/shutdown_logging)
  src: /datum/log_holder (/datum/log_holder)
  call stack:
  /datum/log_holder (/datum/log_holder): shutdown logging()
  shutdown logging()
  world: Reboot(0, 0)
  Ticker (/datum/controller/subsystem/ticker): Reboot("Round ended.", "proper completion", 600)
```

This is the full log:


![image](https://github.com/tgstation/tgstation/assets/34697715/af938235-3076-41d5-98b2-02907dedb6d5)

This is the code:


![image](https://github.com/tgstation/tgstation/assets/34697715/371b11cb-3bc9-4a99-a17c-73968ded308d)

For some reason, even though we invoke `TGSEndProcess`, we still
continue on in this `if()` chain. I don't know why we keep executing DM
code after TGS is supposed to be shut down (which may be why no one has
ever included a `return` here, but let's be safe instead of sorry.

If you really want to investigate why TGS is running DM code after we
end the process, I am amenable to including a stack trace or crash of
this phenomenon instead.
## Why It's Good For The Game

Since we aren't invoking `LOG_CLOSE_ALL` to rust-g twice (which seems to
be really unwanted per the code I read), hopefully thing no crash?
Rust-g had two breaking changes (one with logs, and one with SQL), so
I'm presuming that this might be related to the log one (which is why we
didn't see this sorta thing happen pre-#77307)... Worst case scenario
less runtimes in the funny runtime log.

I hope this wasn't loadbearing either... Likely requires testmerging
since TGS and I don't get along on my machine.
## Changelog
:cl:
server: Added a preventative measure to prevent calling both
TGSHardRestart and TGSReboot, as well as potentially invoking sensitive
procs that are only meant to be called once.
/:cl:

TL;DR- I do not definitively know why servers are crashing but I noticed
this runtime so I'll put out this open flame while I have the time to do
so.

---
## [SMERTONOS/tgstation](https://github.com/SMERTONOS/tgstation)@[63f7eb1a6a...](https://github.com/SMERTONOS/tgstation/commit/63f7eb1a6a01c0c48dcc075f57b58a662d27fc17)
#### Friday 2023-08-18 21:05:32 by san7890

Fixes Ticked File Enforcement and Missing Unit Test (and makes said Unit Test Compile) (and genericizes the C&D list to the base unit test datum) (#77632)

Closes #77631

## About The Pull Request

Hey there,

Ticked File Enforcement simply wasn't catching files that were missed.
That's a bit stupid, so I decided to look into what the issue might be,
and whoopsie daisies I did double periods back in #76592
(020ac2405308eab83f314282499dfe777aba5874).

![image](https://github.com/tgstation/tgstation/assets/34697715/6023afe8-313d-4550-9a60-58a8bc211b4f)

I also added some debug info and some more checks to prevent such a
break from happening again on runtime of this script. I thought it was a
weird string concatenation issue (and not the simple break I thought it
was), so I rewrote how it adds `glob`s. I think it's cleaner so I'll
keep it anyhow

This PR also corrects the oversight of the missing unit test (introduced
in #77218 (69827604c46952dd4393db8617cd494ade17bea2)) by reticking it in
the `_unit_tests.dm` file, and also makes it compile because it didn't
do that.

I also then had to do some more work to get the unit test to work.
* Genericizes the Create-and-Destroy "ignore" list to be a static list
on `/datum/unit_test` to allow it to be shared between these types of
tests that we need to test.
* Adds that list to C&D and the broken unit test regarding fantasy
bonuses
* Fixes some actually broken that the unit test was made to catch (beam
rifles, butterdogs and other slippery items, random ingredient boxes).
* Adds cases for things that the unit test and overall framework really
shouldn't be altering anyways (mythril), and was likely causing
inappropriate stack traces on master

## Why It's Good For The Game

Unit Tests WORK. Tools WORK.


![image](https://github.com/tgstation/tgstation/assets/34697715/9a59c0db-7a33-4546-918b-c73372a5b867)


## Changelog

:cl:
fix: Beam rifles will no longer inappropriately retain any bonuses they
may gain from wizardry.
fix: Inappropriate stack traces over bonuses being applied to components
that gain bonuses innately (like Mythril stacks) should cease.
/:cl:

---
## [wertiop1/pokemon-showdown](https://github.com/wertiop1/pokemon-showdown)@[5cbb317a4c...](https://github.com/wertiop1/pokemon-showdown/commit/5cbb317a4c62a59351010c006be62b37e2a029e2)
#### Friday 2023-08-18 21:08:50 by sexy90gxebattlefactoryplayer

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
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[bae1aef3b4...](https://github.com/tgstation/tgstation/commit/bae1aef3b457cb4fbad551a8560319ed993ba397)
#### Friday 2023-08-18 22:09:09 by san7890

Refactors Regal Rats into Basic Mobs (more titles edition) (#77681)

## About The Pull Request

I literally can't focus on anything nowadays, so I just did this to
break a never-ending chain of distress. Anyways, regal rats! These
fellas are mostly player controlled, but did have _some_ AI capabilities
(mainly tied to their actions), so that was incorporated too. Everything
should work as-expected (as well as look a shitload cleaner).

Instead of doing weird and awful conditional signals being sent out, I
made the `COMSIG_REGAL_RAT_INTERACT` (not the actual name) have a return
value so we can always rely on that working whenever we have that signal
registered on something we attack. I also cleaned up pretty much every
proc related to regal rats, gave them AIs to reflect their kingly nature
(and action capabilities (as well as move the action to
`mob_cooldown`)).

Since I thought they needed it, Regal Rats now get a special moniker!
This is stuff like "the Big Cheese" and what-not, like actual regents in
history. That's nice.
## Why It's Good For The Game

Two more off the list. Much better code to read. Way smarter rats with
spawning their army as part of a retaliatory assault (war). More sovl
with better regal rat names. The list goes on.
## Changelog
:cl:
refactor: Regal Rats have been refactored into basic mobs. They should
be a bit smarter and retain their docility (until attacked, in which
case you should prepare to get rekt by summoned rats), and properly flee
when they can instead of just sit there as you beat them to death. The
framework for them interacting with stuff (i.e. opening doors while
slobbering on food) is a bit more unified too, now. They also have
cooler names too!
/:cl:

FYI: Beyond a few code touchups, I haven't touched the actions at all. I
do not believe myself to be enthusiastic about fixing anything involving
the actions code as of this moment so that this PR is more overbloated
unless it's unbelievably stupid or easy to fix.

---
## [EmanuelCN/kernel_xiaomi_sm8250](https://github.com/EmanuelCN/kernel_xiaomi_sm8250)@[efc24fba1b...](https://github.com/EmanuelCN/kernel_xiaomi_sm8250/commit/efc24fba1b039210f786cfe7f2fa1e7ffe94fdba)
#### Friday 2023-08-18 22:13:21 by Wang Han

power: Introduce OnePlus 3 fingerprintd thaw hack

Taken from Oneplus 3, this hack will make fingerprintd recover from suspend quickly.

Small fixes for newer kernels since we're coming from 3.10.108..

Change-Id: I0166e82d51a07439d15b41dbc03d7e751bfa783b
Co-authored-by: Cyber Knight <cyberknight755@gmail.com>
[cyberknight777: forwardport and adapt to 4.14]
Co-authored-by: Tashfin Shakeer Rhythm <tashfinshakeerrhythm@gmail.com>
[Tashar02: forwardport and adapt to 4.19 and xiaomi_sdm660's fp]
Signed-off-by: Shreyansh Lodha <slodha96@gmail.com>
Signed-off-by: Pierre2324 <pdbbasketball@gmail.com>
Signed-off-by: PainKiller3 <ninadpatil100@gmail.com>
Signed-off-by: Dhruv <dhruvgera61@gmail.com>
Signed-off-by: Cyber Knight <cyberknight755@gmail.com>
Signed-off-by: Tashfin Shakeer Rhythm <tashfinshakeerrhythm@gmail.com>

---
## [sjp38/linux](https://github.com/sjp38/linux)@[d8ac38b49f...](https://github.com/sjp38/linux/commit/d8ac38b49fc4527fc1333ddac594750029c31698)
#### Friday 2023-08-18 22:17:37 by David Hildenbrand

smaps: use vm_normal_page_pmd() instead of follow_trans_huge_pmd()

We shouldn't be using a GUP-internal helper if it can be avoided.

Similar to smaps_pte_entry() that uses vm_normal_page(), let's use
vm_normal_page_pmd() that similarly refuses to return the huge zeropage.

In contrast to follow_trans_huge_pmd(), vm_normal_page_pmd():

(1) Will always return the head page, not a tail page of a THP.

 If we'd ever call smaps_account with a tail page while setting "compound
 = true", we could be in trouble, because smaps_account() would look at
 the memmap of unrelated pages.

 If we're unlucky, that memmap does not exist at all. Before we removed
 PG_doublemap, we could have triggered something similar as in
 commit 24d7275ce279 ("fs/proc: task_mmu.c: don't read mapcount for
 migration entry").

 This can theoretically happen ever since commit ff9f47f6f00c ("mm: proc:
 smaps_rollup: do not stall write attempts on mmap_lock"):

  (a) We're in show_smaps_rollup() and processed a VMA
  (b) We release the mmap lock in show_smaps_rollup() because it is
      contended
  (c) We merged that VMA with another VMA
  (d) We collapsed a THP in that merged VMA at that position

 If the end address of the original VMA falls into the middle of a THP
 area, we would call smap_gather_stats() with a start address that falls
 into a PMD-mapped THP. It's probably very rare to trigger when not
 really forced.

(2) Will succeed on a is_pci_p2pdma_page(), like vm_normal_page()

 Treat such PMDs here just like smaps_pte_entry() would treat such PTEs.
 If such pages would be anonymous, we most certainly would want to
 account them.

(3) Will skip over pmd_devmap(), like vm_normal_page() for pte_devmap()

 As noted in vm_normal_page(), that is only for handling legacy ZONE_DEVICE
 pages. So just like smaps_pte_entry(), we'll now also ignore such PMD
 entries.

 Especially, follow_pmd_mask() never ends up calling
 follow_trans_huge_pmd() on pmd_devmap(). Instead it calls
 follow_devmap_pmd() -- which will fail if neither FOLL_GET nor FOLL_PIN
 is set.

 So skipping pmd_devmap() pages seems to be the right thing to do.

(4) Will properly handle VM_MIXEDMAP/VM_PFNMAP, like vm_normal_page()

 We won't be returning a memmap that should be ignored by core-mm, or
 worse, a memmap that does not even exist. Note that while
 walk_page_range() will skip VM_PFNMAP mappings, walk_page_vma() won't.

 Most probably this case doesn't currently really happen on the PMD level,
 otherwise we'd already be able to trigger kernel crashes when reading
 smaps / smaps_rollup.

So most probably only (1) is relevant in practice as of now, but could only
cause trouble in extreme corner cases.

Let's move follow_trans_huge_pmd() to mm/internal.h to discourage future
reuse in wrong context.

Link: https://lkml.kernel.org/r/20230803143208.383663-3-david@redhat.com
Fixes: ff9f47f6f00c ("mm: proc: smaps_rollup: do not stall write attempts on mmap_lock")
Signed-off-by: David Hildenbrand <david@redhat.com>
Acked-by: Mel Gorman <mgorman@techsingularity.net>
Cc: Hugh Dickins <hughd@google.com>
Cc: Jason Gunthorpe <jgg@ziepe.ca>
Cc: John Hubbard <jhubbard@nvidia.com>
Cc: Linus Torvalds <torvalds@linux-foundation.org>
Cc: liubo <liubo254@huawei.com>
Cc: Matthew Wilcox (Oracle) <willy@infradead.org>
Cc: Mel Gorman <mgorman@suse.de>
Cc: Paolo Bonzini <pbonzini@redhat.com>
Cc: Peter Xu <peterx@redhat.com>
Cc: Shuah Khan <shuah@kernel.org>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>

---
## [Superlagg/coyote-bayou](https://github.com/Superlagg/coyote-bayou)@[aac465cc2a...](https://github.com/Superlagg/coyote-bayou/commit/aac465cc2a5026b18fcab3cd7b7eefde77d2d8a3)
#### Friday 2023-08-18 22:26:24 by Tk420634

Don't worry about it

hate telemetry warnings, yeah they're great and all but fuck the fuck off

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[f6dbcd063d...](https://github.com/TaleStation/TaleStation/commit/f6dbcd063da8b330bde07c76fd98a14beb318063)
#### Friday 2023-08-18 23:04:32 by TaleStationBot

[MIRROR] [MDB IGNORE] Reflavors the Mosin to be a surplus rifle from the past IC 200 years, rather than from 670 years ago in game. Allergy warning: May contain microscopic silverscale buff (#7332)

Original PR: https://github.com/tgstation/tgstation/pull/77169
-----
## About The Pull Request

As the beautiful title may imply:

The Mosin-Nagant rifle has been reflavored into something _slightly_
more modern for the setting (The game currently takes place in 2563 you
know). Rather than a gun made in 1891 ending up in the hands of cargo
techs 670 years in the future, instead aspiring revolutionaries,
larpers, and eastern europeans in general will be seen arming themselves
with something at least a few hundred years more modern.

<details>
<summary>The Sakhno Precision Rifle, the new Nagant</summary>
<br>


![image](https://github.com/tgstation/tgstation/assets/82386923/d26d0bd6-344e-40a2-879c-303b948ce9bd)

"A Sakhno Precision Rifle, a bolt action weapon that was (and certainly
still is) popular with frontiersmen, cargo runners, private security
forces, explorers, and other unsavoury types. This particular pattern of
the rifle dates back all the way to 2440."

</details>

<details>
<summary>The Sakhno M2442 Army, surplus power</summary>
<br>


![image](https://github.com/tgstation/tgstation/assets/82386923/eabcd880-3b0e-4582-a306-000b2e46f4af)

"A modification of the Sakhno Precision Rifle, _Sakhno M2442 Army_ is
stamped into the side. It is unknown what army this pattern of rifle was
made for or if it was ever even used by an army of any sort. What you
can discern, however, is that its previous owner did not treat the
weapon well. For some reason, there's moisture all through the
internals."

</details>

<details>
<summary>The Sakhno - Zhihao Sporting Rifle, weapons for the
rich</summary>
<br>


![image](https://github.com/tgstation/tgstation/assets/82386923/f7e2b6d8-0346-4376-9673-43e405b88a17)

"An upgrade and modernisation of the original Sakhno rifle, made with
such wonders as modern materials, a scope, and other impressive
technological advancements that, to be honest, were already around when
the original weapon was designed. Surprisingly for a rifle of this type,
the scope actually has magnification, rather than being decorative."

</details>

<details>
<summary>The Lionhunter and Enchanted Bolt Action</summary>
<br>


![image](https://github.com/tgstation/tgstation/assets/82386923/1557cd36-f7ca-4fb9-b1a2-49f07c24af0a)

Because it wouldn't make sense for heretics and wizards to be summoning
brand new military green bolt action guns, some wood-like and
significantly fancier looking variations of the sprite now exist for
both of the guns.

</details>



</details>

<details>
<summary>How these look in game:</summary>
<br>


![image](https://github.com/tgstation/tgstation/assets/82386923/aaed7e56-4c0c-406c-bfc9-6188b9231f26)


</details>

## Why It's Good For The Game

<details>
<summary>See a before and after:</summary>
<br>

The sprites on the left of the arrow are what they are now, and the
sprites on the right are what they will turn into, note that there's one
old sprite to several new sprites, this is because guns that were
represented by the same sprite before now have their own unique looks.

These are subject to be slightly different than what you see here, but
will be more or less like these images.


![image](https://github.com/tgstation/tgstation/assets/82386923/73acecb5-e16c-43c2-b690-e1240e3cd06c)


![image](https://github.com/tgstation/tgstation/assets/82386923/188f6de3-1f89-4c26-9e12-2c5a3bffcdbf)


![image](https://github.com/tgstation/tgstation/assets/82386923/c3f7a4da-f4b3-4864-8bf6-314c84ac528a)


![image](https://github.com/tgstation/tgstation/assets/82386923/5a64327c-de63-44cf-9b02-7e90d80a753a)

</details>

While I understand the appeal of wanting a shitty, old rifle to have in
the game for everyone's surplus needs, the Mosin (and a good few other
guns too, looking at you 1911) is just a fair bit too old in my book.
About 670 years old. I find it more believable that while there would
still be some shitty surplus weapon that cargo techs and larpers would
non-stop fawn over, it'd be something that's old by the standards of the
year 2563 where the game takes place, vs old by the standards of 2023.

I think it'd greatly help the sense of the fact that we exist many
hundreds of years in the future if we stop using guns made before the
first world war.

## Changelog
:cl:
image: The Mosin-Nagant has been given new sprites and a reflavor,
looking for the old rifle? Look for the Sakhno Precision Rifle.
balance: The tiniest balance thing, but since Silverscales use the
Sakhno-Zhihao rifle, which has a scope on it, their main weapon now has
a scope.
sound: The cargo rifle now has a new, considerably more rifle sized
firing sound. Gotten from tgmc from
https://github.com/tgstation/TerraGov-Marine-Corps/pull/12280.
/:cl:

---------

Co-authored-by: Paxilmaniac <82386923+Paxilmaniac@users.noreply.github.com>
Co-authored-by: Jolly-66 <70232195+Jolly-66@users.noreply.github.com>

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[0b4398a856...](https://github.com/TaleStation/TaleStation/commit/0b4398a8562b5880f5fb56e7fe12e1ae464e9cd4)
#### Friday 2023-08-18 23:04:44 by TaleStationBot

[MIRROR] [MDB IGNORE] Basic Watchers & Basilisks (#7361)

Original PR: https://github.com/tgstation/tgstation/pull/77630
-----
## About The Pull Request

This one is a double feature because Watchers and Basilisks share the
same typepath. You might see a couple more of those.
As is tradition I decided to fuck with them rather than just port them.
Here's what's up.

**Basilisks**

![image](https://github.com/tgstation/tgstation/assets/7483112/9e4b0115-65dd-4df7-b62a-21c7be8549bf)

![image](https://github.com/tgstation/tgstation/assets/7483112/59162e68-7d73-4659-9531-5078ff751228)

- Have a new soulless sprite which looks less like a living blue hedge.
- Walk at you and shoot you while you are not in range (just like
before).
- Become supercharged if they become "heated" by lava, lasers, or
temperature weapons. This was a feature they also previously had but
they would never encounter lava, so now it also works if you use the
wrong gun on them.
- Lose their supercharge if you cool them down.
- Otherwise pretty normal mobs.

**Watchers**

https://www.youtube.com/watch?v=kOq_Bf78k5A
Here's a traditional video of me intentionally getting hit by mechanics
(trust me its definitely on purpose)

- They glow emmissively a little bit so you can see them from further
away.
- Their eyes light up about 0.5 seconds before they are able to shoot at
you.
- No longer melee attack, instead try to stay out of melee.
- Will occasionally put you into "Overwatch", meaning they will shoot
you rapidly if you move or act while they're staring at you for a brief
time period (after which you become immune for 12 seconds, and during
which other watchers will play fair and stop shooting at you).
- If they start taking damage they will also start using their "Gaze"
attack, look away or suffer some kind of negative effect!
- - Normal watcher gaze flashes and confuses you.
- - Magmawing watcher gaze obviously burns (and briefly stuns) you.
- - Icewing watcher gaze freezes you and throws you backwards.
- Magnetically attract and eat diamonds. They also used to do this, but
just if they happened to coincidentally walk past some.

**Other accompanying changes**

All basic mobs will now adopt the "stop gliding" trait if they get
slowed down too much.
I moved behaviour for "fire a projectile from this atom" into a helper
proc because I was using it in three places and I will probably use it
in more places. There are probably other places in the existing code
which could be using this.
I think I made the basic mob melee attack forecast default a little more
forgiving, they were fucking me up too much and I am the playtester.

## Why It's Good For The Game

Another one off the list.
New tricks for old dogs.
Framework for making mobs with ranged attacks "fairer" (you can see when
they are ready to shoot you).
More (hopefully) versatile AI behaviours which we will reuse later (I
hope I'm not duplicating one someone already made).
If our players "enjoy" them enough we can give more mobs "don't look at
me" mechanics.
Removes some soul sprites.

## Changelog

:cl:
refactor: Basilisks and Watchers now use the basic mob framework. Please
bug report any unusual behaviour.
sprite: Basilisks have new sprites.
add: Basilisks will go into a frenzy if heated by energy weapons or
temperature beams as well as by lava.
add: Watcher eyes will be illuminated briefly when they are ready to
fire at you.
add: Watchers can now briefly put you into "Overwatch" and penalise you
for moving while they can see you.
add: Wounded watchers will occasionally punish players who look at them.
balance: Unusual watcher variants are more likely to appear.
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>
Co-authored-by: Jolly-66 <70232195+Jolly-66@users.noreply.github.com>

---
## [whatotter/pwnhyve](https://github.com/whatotter/pwnhyve)@[dfe7c3fd48...](https://github.com/whatotter/pwnhyve/commit/dfe7c3fd48cb1671a9cd4bbddd361db9da180dd2)
#### Friday 2023-08-18 23:18:49 by otter

remote control and evil portal

i have kinda lost motivation but fuck it we ball

the html control panel is also depreciated now and will likely be removed, as you can only use it when you have to interfaces

next update will be cleaning up some things

---

