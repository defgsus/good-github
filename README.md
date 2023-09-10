## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-09-09](docs/good-messages/2023/2023-09-09.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,962,927 were push events containing 2,679,792 commit messages that amount to 152,229,335 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 49 messages:


## [Offroaders123/Dovetail](https://github.com/Offroaders123/Dovetail)@[39bbf27d1d...](https://github.com/Offroaders123/Dovetail/commit/39bbf27d1d0d7bfbe5a23b3f5a6bb58e91589b53)
#### Saturday 2023-09-09 00:13:30 by Offroaders123

Component Learning: Header

Trying to wrap my head around how you're supposed to structure the state of your app using components, I keep getting stuck trying to pass data up and down out of components, when I have a hunch it's only supposed to go from the top-down?

https://stackoverflow.com/questions/70469476/whats-the-equivalent-of-useref-in-svelte (helpful for element references)

From my discussion with HoldYourWaffle about my confusion:

Ok I'm finding out what else I have trouble with in component-based UI structures
It's deciding where I should place my interaction code, like what components should contain them
(`function saveFile`, `Header.svelte`, `saver.addEventListener`)

So the new Svelte code above is what would replace this event listener
My mix up is whether this save handling code should go in the `Header` component, which is where the save button currently is, or go up a level to the `App` component
How do you import values from other components to use them?
Maybe it's that the state shouldn't be centralized to components like I want them to be, but maybe it has to come from the top-down instead?
Because to get the options from the `FormatDialog` component (once I make that), then I have to get the value out of that component somehow, so the Header can use it for the save handling function here
So is my design flaw that the state should instead just be at the top of the app, and each of the elements can just use those as props?
Then it feels counterintuitive to the component nature that Svelte is trying to employ, because I'm just essentially pushing everything up to the 'global' component, which then just passes all the state down as props; that feels more overboard to me for some reason?
I'd think if it's a component, it holds it's own state right?
How do components interact with other components?
I think this is probably just my brain thinking of it the wrong way, it probably should work the top-down way, just like how dependency injection works for functions, it should work that way for components probably too?
I definitely like how that works for functions, so that's probably how you're meant to do it with components too?

(About `Header.svelte`) And can you import exports from other components? That seems like what I'm gravitating towards, but that might be going against how you're intended to design the state flow

```js
import Header, { saveFile } from "./Header.svelte";
```

It's the confusion of where my brain sees ESM but it's not real ESM, but rather Svelte component props being marked a 'public' or 'private', like a `class` would do
`let hi = true` is a private property of the component, while `export let hey = true` is a public property
But how can you use properties from other components, since `export` doesn't do what `export` does in regular JS land?
Wait, actually I wonder if this works (Code snippet above)
Nope, dangit

It's that the syntax makes a `class`-like thing appear like a module, when it's really a `class` in a way
What if you had JSX code which had Svelte destiny-like features, but compiled down to how Svelte works? (not that this should be a thing, but I think the mix of class behavior with ESM syntax is what is getting confusing for me)

(Destiny is about the destiny operator idea/proposal, which is like Svelte's `$` definition)
https://news.ycombinator.com/item?id=8172491
https://es.discourse.group/t/destiny-operator/895

---
## [hero/neovim](https://github.com/hero/neovim)@[5970157e1d...](https://github.com/hero/neovim/commit/5970157e1d22fd5e05ae5d3bd949f807fb7a744c)
#### Saturday 2023-09-09 00:21:07 by bfredl

refactor(map): enhanced implementation, Clean Code™, etc etc

This involves two redesigns of the map.c implementations:

1. Change of macro style and code organization

The old khash.h and map.c implementation used huge #define blocks with a
lot of backslash line continuations.

This instead uses the "implementation file" .c.h pattern. Such a file is
meant to be included multiple times, with different macros set prior to
inclusion as parameters. we already use this pattern e.g. for
eval/typval_encode.c.h to implement different typval encoders reusing a
similar structure.

We can structure this code into two parts. one that only depends on key
type and is enough to implement sets, and one which depends on both key
and value to implement maps (as a wrapper around sets, with an added
value[] array)

2. Separate the main hash buckets from the key / value arrays

Change the hack buckets to only contain an index into separate key /
value arrays
This is a common pattern in modern, state of the art hashmap
implementations. Even though this leads to one more allocated array, it
is this often is a net reduction of memory consumption. Consider
key+value consuming at least 12 bytes per pair. On average, we will have
twice as many buckets per item.
Thus old implementation:

  2*12 = 24 bytes per item

New implementation

  1*12 + 2*4 = 20 bytes per item

And the difference gets bigger with larger items.
One might think we have pulled a fast one here, as wouldn't the average size of
the new key/value arrays be 1.5 slots per items due to amortized grows?
But remember, these arrays are fully dense, and thus the accessed memory,
measured in _cache lines_, the unit which actually matters, will be the
fully used memory but just rounded up to the nearest cache line
boundary.

This has some other interesting properties, such as an insert-only
set/map will be fully ordered by insert only. Preserving this ordering
in face of deletions is more tricky tho. As we currently don't use
ordered maps, the "delete" operation maintains compactness of the item
arrays in the simplest way by breaking the ordering. It would be
possible to implement an order-preserving delete although at some cost,
like allowing the items array to become non-dense until the next rehash.

Finally, in face of these two major changes, all code used in khash.h
has been integrated into map.c and friends. Given the heavy edits it
makes no sense to "layer" the code into a vendored and a wrapper part.
Rather, the layered cake follows the specialization depth: code shared
for all maps, code specialized to a key type (and its equivalence
relation), and finally code specialized to value+key type.

---
## [kagisearch/smallweb](https://github.com/kagisearch/smallweb)@[4be4b78e5b...](https://github.com/kagisearch/smallweb/commit/4be4b78e5be3af5ffef591a389c3ac94fa6e6fc7)
#### Saturday 2023-09-09 00:37:48 by Andy

Add https://www.cerealously.net/feed

A wonderful website authored by an a single individual (Dan) about news and reviews in the world of American breakfast cereals. The writing is genuinely lovely, and clearly a product of personal passion.

Note that this is NOT a link affiliate/marketing spam blog for cereals. The author has no direct relation to any cereal companies (at least to my best knowledge), and the writing is clearly the author's direct, personal feelings about the subject matter.

Highly recommend for the small web :)

---
## [Shadow-Quill/Skyrat-tg](https://github.com/Shadow-Quill/Skyrat-tg)@[9638396677...](https://github.com/Shadow-Quill/Skyrat-tg/commit/9638396677d8aecd41d477d3755ec86510ecb8c8)
#### Saturday 2023-09-09 00:39:02 by SkyratBot

[MIRROR] Grilles take 0-1 damage when shocking something, power sinks are available at lower reputation [MDB IGNORE] (#23278)

* Grilles take 0-1 damage when shocking something, power sinks are available at lower reputation (#77860)

## About The Pull Request
Ports BeeStation/BeeStation-Hornet#3590. As it is right now, it's
trivial to set up a contraption using a conveyor belt and a shocked
grille to continuously shock monkey bodies. While this is very funny, it
also serves as a ghetto powersink that's hard to locate, easy to
replicate, and lasts effectively forever, since you can just keep
shocking the same bodies over and over again.

This doesn't completely remove the ability to make these, but it makes
them require at least a little maintenance and provides a way for them
to stop working even if the crew isn't able to locate them.

In an attempt to finally get people using the _actual_ powersink,
they'll show up a bit earlier in progression now. I'm not convinced 20
minutes is enough, but I don't want to put them in early enough that it
fucks with Engineering's ability to set things up at round start. We can
turn this down further if need be.

I'm also up for turning the TC requirement down, but 11 feels about
right for what they're supposed to do, so I'd prefer we try this first
and see how that works.

## Why It's Good For The Game
I'm all for goofy weird shit players have found, but there's an issue
with being able to do what an antag item is supposed to do but just
plain better. This shouldn't make creating these impossible or make them
unusable, but it'll require players to actively monitor them if they
want it to run for an extended period.

Additionally, we don't really see powersinks much anymore, and while
that might be more because powernets are kind of buggy and unreliable, I
think making them easier to get will make them show up a little more.

## Changelog
:cl: Vekter
balance: Grilles will now take 0-1 damage every time they shock
something.
balance: Powersinks are now available earlier in traitor progression.
/:cl:

---------

Co-authored-by: Fikou <23585223+Fikou@ users.noreply.github.com>

* Grilles take 0-1 damage when shocking something, power sinks are available at lower reputation

---------

Co-authored-by: Vekter <TheVekter@users.noreply.github.com>
Co-authored-by: Fikou <23585223+Fikou@ users.noreply.github.com>

---
## [OpenVZ/vzkernel](https://github.com/OpenVZ/vzkernel)@[35f9cc1e6d...](https://github.com/OpenVZ/vzkernel/commit/35f9cc1e6dd8887fbcf7aab236489d7ed6ec60f7)
#### Saturday 2023-09-09 00:50:09 by Vladimir Davydov

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
## [nworbnhoj/xous-core](https://github.com/nworbnhoj/xous-core)@[aab25f2d53...](https://github.com/nworbnhoj/xous-core/commit/aab25f2d53b5b3e681840fe89fb22e1451516c0c)
#### Saturday 2023-09-09 00:50:41 by bunnie

add Tall font face and support for 32x32 bitmaps

Thanks to @samblenny for getting the ball rolling on this.

This commit adds a "tall" font face which is somewhere in betwee
the Regular size (12 pts) and 2x Small size (18 pts). This is
a compromise between text density and readability that has been
missing for some time from the UI.

The 32x32 glyph support is "hacked in", in that an extra flag
has been added to support this special case, rather than either
(a) making the library more generic (e.g. supporting 8x, 16x, 32x, 64x
glyphs) or (b) adding more metadata to the font libraries so that
the bitmap pattern is automatically associated with the font (right
now the parameters are set by hand in blitstr2/fonts.rs).

This is a violation of the "zero, one, many" principle in coding,
but I'm waiving that because (a) 64x glyphs don't make sense on
our system...you're not going to be creating posters and headlines
on this device (ha ha I say this today, tomorrow I will get a PR
for a poster editor app that absolutely needs 64x glyphs) and (b)
the font subsystem is, at least for now, a fairly mature and
well-tested code base so a minor futzing seems more appropriate
than ripping everything out.

The point at which things should be greatly refactored is when
we consider supporting right-to-left scripts or scripts that
require complex ligatures. But I think for now the system as
writ covers 80% of humanity's language needs acceptably
(but not perfectly).

---
## [ItsMarmite/Paradise](https://github.com/ItsMarmite/Paradise)@[acb7352265...](https://github.com/ItsMarmite/Paradise/commit/acb735226555390c861ecf5e77bc67fd6013afe1)
#### Saturday 2023-09-09 01:04:35 by matttheficus

Gives Vampires Stronger Night Vision at 500 Blood (#21764)

* I SEEEEEEEEEEEEE YOU

* Hal review part 1

* its time to suck at coding

* right, i think im getting somewhere

* testing shit - doesnt work

* im finally freeeeeeeeeeeeeee

* hal review 2: electric boogaloo

---
## [nushell/nightly](https://github.com/nushell/nightly)@[fed4233db4...](https://github.com/nushell/nightly/commit/fed4233db4d81de00068ffa7cf1c0d09506bc150)
#### Saturday 2023-09-09 01:18:57 by David Matos

use uutils/coreutils cp command in place of nushell's cp command (#10097)

<!--
if this PR closes one or more issues, you can automatically link the PR
with
them by using one of the [*linking
keywords*](https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue#linking-a-pull-request-to-an-issue-using-a-keyword),
e.g.
- this PR should close #xxxx
- fixes #xxxx

you can also mention related issues, PRs or discussions!
-->

# Description
Hi. Basically, this is a continuation of the work that @fdncred started.
Given some nice discussions on #9463 , and [merged uutils
PR](https://github.com/uutils/coreutils/pull/5152) from @tertsdiepraam
we have decided to give the `cp` command the `crawl` stage as it was
named.

> [!NOTE] 
Given that the `uutils` crate has not made the release for the merged
PR, just make sure you checkout latest and put it in the required place
to make this PR work.

The aim of this PR is for is to see how to move forward using `uutils`
crate. In order to getting this started, I have made the current
`nushell cp tests` pass along with some extra ones I copied over from
the `uutils` repo.

With all of that being said, things that would be nice to decide, and
keep working on:

Crawl:
- Handling of certain `named` flags, with their long and short
forms(e.g. --update, --reflink, --preserve, etc), and using default
values. Maybe `-u` can already have a `default_missing_value`.
- Should we maybe just support one single option `switch` flags (see
`--backup` in code) as a contrast to the other named args.
- Complete test coverage from `uutils`. They had > 100 tests, and I
could only port like 12 as they are a bit time consuming given they
cannot be straight up copy pasted. Maybe we do not need all >100, but
maybe the more relevant to what we want.
- Refactor this code

Walk:
- Non fatal errors on `copy` from `utils`. Currently it just sends it to
stdout but errors have no span
- Better integration 

An added possibility is the addition of `SyntaxShape::OneOf()` for
`Named` arguments which was briefly mentioned in the discord server, but
that is still to be decided. This could greatly improve some of the
integration. This would enable something like `cp --preserve [all
timestamp]` or `cp --preserve all` to both work.

I did not want to keep holding on this, and wait till I was happy with
the code because I think its nice if everyone can start up and suggest
refactors, but the main important part now was getting it out the door,
as if I take my sweet time this will take way longer :stuck_out_tongue:

<!--
Thank you for improving Nushell. Please, check our [contributing
guide](../CONTRIBUTING.md) and talk to the core team before making major
changes.

Description of your pull request goes here. **Provide examples and/or
screenshots** if your changes affect the user experience.
-->

# User-Facing Changes
<!-- List of all changes that impact the user experience here. This
helps us keep track of breaking changes. -->

# Tests + Formatting

Make sure you've run and fixed any issues with these commands:

- [X] cargo fmt --all -- --check` to check standard code formatting
(`cargo fmt --all` applies these changes)
- [X] cargo clippy --workspace -- -D warnings -D clippy::unwrap_used` to
check that you're using the standard code style
- [X] cargo test --workspace` to check that all tests pass
- [X] cargo run -- -c "use std testing; testing run-tests --path
crates/nu-std"` to run the tests for the standard library

> **Note**
> from `nushell` you can also use the `toolkit` as follows
> ```bash
> use toolkit.nu # or use an `env_change` hook to activate it
automatically
> toolkit check pr
> ```
-->

# After Submitting
<!-- If your PR had any user-facing changes, update [the
documentation](https://github.com/nushell/nushell.github.io) after the
PR is merged, if necessary. This will help us keep the docs up to date.
-->

---------

Co-authored-by: Darren Schroeder <343840+fdncred@users.noreply.github.com>

---
## [realforest2001/forest-cm13](https://github.com/realforest2001/forest-cm13)@[7cb618c69b...](https://github.com/realforest2001/forest-cm13/commit/7cb618c69b75873f3ce893022fe08d1233b3152d)
#### Saturday 2023-09-09 01:26:10 by Zonespace

M707 "Vulture" Anti-Materiel Rifle (#4253)

# About the pull request

## The M707 is not made player-accessible in this PR.

Adds the M707 "Vulture" anti-materiel rifle to the game. [Design doc
here.](https://github.com/cmss13-devs/cmss13/files/12433899/M707_Final.pdf)

The M707 is meant to take the place of a heavy support weapon, not
unlike the mortar. It is a 20mm bolt-action rifle, capable of loading
from 4-round magazines. Each round does 400 damage with full AP (50),
but it is not a simple task to fire the weapon. The gun, being as
high-caliber as it is, will immediately break your arm & hand if you do
not fire it without use of the built-in bipod. In addition, its accuracy
is massively reduced below its ideal range (10 tiles), which means the
scope is necessary to be used.

The scope does not function like a regular scope. (see screenshot
section for details) Instead, it shows a 5x5 area (the rest is blacked
out) 12 tiles ahead, with an aiming reticle in the center. The aiming
reticle will drift over time within the 5x5, requiring you to re-adjust
or use the **Hold Breath** ability to temporarily stop the sway. If you
open up the scope's UI, you will be able to modify the scope and the
reticle's location, one tile at a time, very slowly.

To assist with this, the Vulture comes with a spotting scope & tripod. A
secondary user is able to assemble and use the spotting scope. The scope
is a complement to the Vulture's, allowing a communicative team to
become far more effective. The spotter's view, on use, will be locked to
the location of the Vulture scope. However, the spotter's view is not
locked to a 5x5 area, instead getting a view of the full area, on top of
an extra 2 tiles (in each direction) of view range. Finally, both the
spotter and sniper's scopes have night vision equivalent to an SG's
goggles.

The bullet itself is a powerful beast. Powerful enough to pierce walls,
people, and barricades, but with 2 caveats. The first is that every
wall/cade penetration removes 75 damage from the round, and any
cades/tables that the round passes over will be immediately destroyed by
the round. In addition, anyone in a large range will hear the report of
the rifle sound and the direction it came from.

Update as of 8/31:
Vulture and its spotter scope now require a pamphlet to use (a pamphlet
gives the trait needed to use both), guncase spawns with 2.

# Explain why it's good for the game

It's a unique weapon that encourages communication inside a team, while
simultaneously not contributing to the IFF ungaball. The weapon promotes
thoughtful gameplay and repositioning to be able to hit a target without
friendlies getting in the way or getting overrun.

# Screenshots
<details>
<summary>Screenshots & Videos</summary>

Scope UI

![image](https://github.com/cmss13-devs/cmss13/assets/41448081/c5ff4c44-65ac-41be-a30a-1dbca019c8ab)

The vulture's scope.

![image](https://github.com/cmss13-devs/cmss13/assets/41448081/ea004c6f-10a6-4f02-a439-303710956286)

Sniper's nest

![image](https://github.com/cmss13-devs/cmss13/assets/41448081/6c9a5165-b831-43a8-ad48-a044c434fcfa)

Closeup

![image](https://github.com/cmss13-devs/cmss13/assets/41448081/6244a435-2c1f-43b8-b15d-003e247bf156)

Spotter's vision

![image](https://github.com/cmss13-devs/cmss13/assets/41448081/82259e26-5355-4362-a300-1ebe409bcb6d)


</details>

# Changelog
:cl: Zonepace, Thwomper
add: Added the M707 "Vulture" anti-materiel rifle. Not currently
player-obtainable. Credit to Tophat and Kaga for the lore description.
/:cl:

---------

Co-authored-by: harryob <me@harryob.live>

---
## [Lluna4/db](https://github.com/Lluna4/db)@[ba67b9d14e...](https://github.com/Lluna4/db/commit/ba67b9d14e710f3c6bdab47ec05571acbe795c72)
#### Saturday 2023-09-09 01:35:26 by Luna

I HATE HUMAN READABLE FORMAT IS STUPID

Who whould have thought that automating an excel where column headers are changing arbitrarily is a fucking bad idea, i cant do this ffs, 15h of my life lost

---
## [StrangeWeirdKitten/Skyrat-tg](https://github.com/StrangeWeirdKitten/Skyrat-tg)@[89ae4aa5b3...](https://github.com/StrangeWeirdKitten/Skyrat-tg/commit/89ae4aa5b3725a33b632cae32f8059afb8105384)
#### Saturday 2023-09-09 02:26:42 by SkyratBot

[MIRROR] Adds the Storage Implanter to the spy kit. [MDB IGNORE] (#22973)

* Adds the Storage Implanter to the spy kit. (#77452)

## About The Pull Request

Adds the storage implanter to the spy kit to make it decent.

## Why It's Good For The Game
This PR hopes to bring Spy at least a little more in-line with the rest
of the syndie-kit specials, so it doesn’t feel like a complete dud to
get.

Spy absolutely sucks as a syndie-kit and getting it is basically
throwing away 20 TC. Not all of them should be equally powerful but all
of them should be at least more satisfying to get. Spy is so bad that
it’s listed in the official wiki as ‘honestly not that good’. It’s also
_barely_ even above 25 telecrystals as the switchblade is a black market
uplink item, not a syndicate uplink item, and not even that good of an
item at that! And the chameleon kit inside isn’t even a full chameleon
kit! Pitiful. Compare it to stealth right below it which totals to _36_
telecrystals.

Adding a storage implant adds a relatively useful item to the kit that
still fits with the entire theme of ‘stealth and deception’, as you can
be searched without having anything on you. To be stealthy, and deceive
people. Like you should. Given the fact that searches are quite common.
It doesn’t make it TOO overpowered as the rest of the gear is still ‘not
that great’.

## Changelog

:cl:
balance: added the storage implanter to the syndie-kit tactical 'spy'
kit to make it decent.
/:cl:

Co-authored-by: oilysnake <63020759+oilysnake@ users.noreply.github.com>

* Adds the Storage Implanter to the spy kit.

---------

Co-authored-by: DeerJesus <willgiscool@gmail.com>
Co-authored-by: oilysnake <63020759+oilysnake@ users.noreply.github.com>

---
## [langchain-ai/langchain](https://github.com/langchain-ai/langchain)@[d57d08fd01...](https://github.com/langchain-ai/langchain/commit/d57d08fd01e05889af4e59fa3577c824de6df09d)
#### Saturday 2023-09-09 02:35:09 by nikhilkjha

Initial commit for comprehend moderator (#9665)

This PR implements a custom chain that wraps Amazon Comprehend API
calls. The custom chain is aimed to be used with LLM chains to provide
moderation capability that let’s you detect and redact PII, Toxic and
Intent content in the LLM prompt, or the LLM response. The
implementation accepts a configuration object to control what checks
will be performed on a LLM prompt and can be used in a variety of setups
using the LangChain expression language to not only detect the
configured info in chains, but also other constructs such as a
retriever.
The included sample notebook goes over the different configuration
options and how to use it with other chains.

###  Usage sample
```python
from langchain_experimental.comprehend_moderation import BaseModerationActions, BaseModerationFilters

moderation_config = { 
        "filters":[ 
                BaseModerationFilters.PII, 
                BaseModerationFilters.TOXICITY,
                BaseModerationFilters.INTENT
        ],
        "pii":{ 
                "action": BaseModerationActions.ALLOW, 
                "threshold":0.5, 
                "labels":["SSN"],
                "mask_character": "X"
        },
        "toxicity":{ 
                "action": BaseModerationActions.STOP, 
                "threshold":0.5
        },
        "intent":{ 
                "action": BaseModerationActions.STOP, 
                "threshold":0.5
        }
}

comp_moderation_with_config = AmazonComprehendModerationChain(
    moderation_config=moderation_config, #specify the configuration
    client=comprehend_client,            #optionally pass the Boto3 Client
    verbose=True
)

template = """Question: {question}

Answer:"""

prompt = PromptTemplate(template=template, input_variables=["question"])

responses = [
    "Final Answer: A credit card number looks like 1289-2321-1123-2387. A fake SSN number looks like 323-22-9980. John Doe's phone number is (999)253-9876.", 
    "Final Answer: This is a really shitty way of constructing a birdhouse. This is fucking insane to think that any birds would actually create their motherfucking nests here."
]
llm = FakeListLLM(responses=responses)

llm_chain = LLMChain(prompt=prompt, llm=llm)

chain = ( 
    prompt 
    | comp_moderation_with_config 
    | {llm_chain.input_keys[0]: lambda x: x['output'] }  
    | llm_chain 
    | { "input": lambda x: x['text'] } 
    | comp_moderation_with_config 
)

response = chain.invoke({"question": "A sample SSN number looks like this 123-456-7890. Can you give me some more samples?"})

print(response['output'])


```
### Output
```
> Entering new AmazonComprehendModerationChain chain...
Running AmazonComprehendModerationChain...
Running pii validation...
Found PII content..stopping..
The prompt contains PII entities and cannot be processed
```

---------

Co-authored-by: Piyush Jain <piyushjain@duck.com>
Co-authored-by: Anjan Biswas <anjanavb@amazon.com>
Co-authored-by: Jha <nikjha@amazon.com>
Co-authored-by: Bagatur <baskaryan@gmail.com>

---
## [NetHack/NetHack](https://github.com/NetHack/NetHack)@[1a64ee1c28...](https://github.com/NetHack/NetHack/commit/1a64ee1c285f8d9a27e58efa3989a281413f9b8e)
#### Saturday 2023-09-09 03:37:17 by PatR

github PR #259 - paranoid_confirmation:trap

Fairly old pull request from copperwater:  add new paranoid_confirm
setting 'trap'.

The old commit suffered from bit rot and merging needed too much
fixing up despite there not being many bands of change in the commit's
diffs.  I ultimately redid it from scratch, although the two biggest
chunks of code started with copy+paste of the pull request's commit.

It operates like paranoid:pray.  Setting paranoid:trap adds a new
"Really step into <trap>?" y/n prompt when attempting to move
into/onto a known trap, even if an object covers it on the map.
Setting both 'paranoid:Confirm trap' turns that into a yes/no prompt.
(Adding 'Confirm' affects other paranoid confirmations; in addition
to requiring yes<return> rather than just y to accept, it also forces
no<return> to reject.)

However, moving into a known trap that is considered to be harmless
behaves as if no trap was present.  Some of the trap classification
might be out of date; several types of traps have undergone changes
since implementation of the original pull request, notably anti-magic
field.  When the hero is hallucinating, all known traps are considered
harmful since the map no longer reliably describes them.

Preceding a movement command with the 'm' prefix also behaves as if
no trap was present, bypassing confirmation for that move, similar to
how paranoid:swim currently behaves.  Being stunned or confused also
behaves as if no trap was present, taking priority over hallucination.

This updates the documentation.

Supersedes #259
Closes #259

---
## [gilbertalgordo/git](https://github.com/gilbertalgordo/git)@[8f23432b38...](https://github.com/gilbertalgordo/git/commit/8f23432b38d9b122be8179295a56688391dc8ad6)
#### Saturday 2023-09-09 04:33:22 by Johannes Schindelin

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
Signed-off-by: Pratyush Yadav <me@yadavpratyush.com>

---
## [WangGithubUser/pyre-check](https://github.com/WangGithubUser/pyre-check)@[30dbfd9b72...](https://github.com/WangGithubUser/pyre-check/commit/30dbfd9b724cf11b1e33c6f9b553eefce32b47ac)
#### Saturday 2023-09-09 04:36:37 by Vincent Lee

Easy List.length = 0 -> List.is_empty optimizations

Summary:
I was talking with a personal friend learning OCaml yesterday and noticed that List has these neat compare_lengths and compare_length_with functions.

In our codebases, we do List.length on two lists a lot and compare the result, or we do it once and compare the result to a constant integer. Not only is this linear time, it also always traverses the entire list, when we could have bailed early (say we were checking that the length is greater than 2, e.g., a list of length 1000 still gets traversed all the way through).

 ---

All of that to say, that's not what this diff does , this diff just does the easy replacements of List.length <> 0 or similar to call Core.List.is_empty, which is essentially a pointer compare with the empty list and is faster in all cases than calling length then comparing to 0.

I think a follow up (that I won't do, but if anyone is interested) is to make utility functions List.shorter_than/longer_than/equal_lengths that wrap Caml.List.compare_lengths and Caml.List.compare_length_with in a nicer looking API, because they're pretty ugly to use directly, then migrate all `List.length x < int` and `List.length a < List.length b` calls or similar to it, if the length is only used in the comparison and is not subsequently used in the conditional branches.

On callsites where large lists are often passed, or lists of very disparate sizes are passed, it could be a potentially-significant perf win.

Reviewed By: alexkassil

Differential Revision: D48542763

fbshipit-source-id: b846bc32523b7b1b938cc033eb001d656970fa0f

---
## [Notclue/TF2Classic-KO-Custom-Weapons](https://github.com/Notclue/TF2Classic-KO-Custom-Weapons)@[414510d1ea...](https://github.com/Notclue/TF2Classic-KO-Custom-Weapons/commit/414510d1ea59e4ad229ad1e2ee3f37b9cf3b49d5)
#### Saturday 2023-09-09 05:05:19 by CluetasticJr

why are you buying clothes at the soup store

fuck you

---
## [sojourn-13/sojourn-station](https://github.com/sojourn-13/sojourn-station)@[1e51e36c62...](https://github.com/sojourn-13/sojourn-station/commit/1e51e36c6224c5e0e7f3e50d40ea3d950ecf6286)
#### Saturday 2023-09-09 05:06:13 by CDB

Drip or Drown; Premier style update. And some other clothing related stuff. (#4757)

* Buncha stuffff

First and foremost, it's been like four years - No one has come with a better set of equipment for the Premier in terms of aesthetics and quality.

Replaces much of the Premiers old/mismatched green shit with newer eris captain sprites, if we want to re-color this a bit that's fine but either way we /desperately/ need to replace these ancient sprites.

Premier additionally now actually starts with their coat, and gets a pair of dress shoes instead of the old scuffed brown shoes.

Mind, the original hat/coat/uniform are still available as alternatives if for SOME reason you want to dress up like a christmas tree. I did not add an alt for the space armor/helmet due to them A. not matching and B. being old sprites. I guess if someone REALLY wants I'll port the /tg/ carapace armor/helmets more up to date sprites as an alt.

Ports the funny cyberpunk jacket from eris(in the loadout.)

ports the eris preacher robes icons, but doesn't code them in quite yet. I couldn't be fucked, there's SO many.

Actually adds the formal IH uniform in as well as doing some tweaks to the icon so that WO + spec can also get a formal uniform with their normal rank pips

ports the eris syndie berets.

As always, a big thanks to the talented spriters over at Eris

* new stuff. Also fixes linters lol oops

Adds to the greyson loot pool an armored void using sprites from Près de l'oiseau#2625 over on the Eris discord.

Replaces some more,  old sprites. Miner suit is replaced as pictured as well as the industrial RIG - sprites by Près once more.

* Update station.dm

* Fixes spawning of the greyson combat void helmet

* puts credits in the code instead of on the PR

* minor stuff.,

Slighjtly fixes syndie beret- the north facing sprites were 1 pixel too far down.

WO helmet is no longer missing its verb to turn the light on. Good work there, Rebel - how did no one notice this till now?

* actually fixes it. ugh.

* BUNCHA new church stuff

Primes hat now has 9 alts

Primes coat now has 5

credit to Près de l'oiseau#2625 once more for the fantastic sprites.

---
## [NextWork123/BAALAM_android_kernel_xiaomi_sm8250](https://github.com/NextWork123/BAALAM_android_kernel_xiaomi_sm8250)@[22d280d78e...](https://github.com/NextWork123/BAALAM_android_kernel_xiaomi_sm8250/commit/22d280d78e775e77129f58f6c9d3879a682adada)
#### Saturday 2023-09-09 06:34:27 by Wang Han

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
## [Rombuilding-X00TD/android_kernel_asus_sdm660](https://github.com/Rombuilding-X00TD/android_kernel_asus_sdm660)@[033a751f4f...](https://github.com/Rombuilding-X00TD/android_kernel_asus_sdm660/commit/033a751f4fa0713f321e99bcef2e70cbb60445c3)
#### Saturday 2023-09-09 08:05:10 by Christian Brauner

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
## [RenaiSaiban/feur-r-oss](https://github.com/RenaiSaiban/feur-r-oss)@[fc4f672d44...](https://github.com/RenaiSaiban/feur-r-oss/commit/fc4f672d44fb94f9eb1f0944b2f7b49e5b35da3e)
#### Saturday 2023-09-09 09:56:44 by Peter Zijlstra

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
Signed-off-by: Momo Belia Deviluke <fajarslebew31@gmail.com>
Signed-off-by: Riko Dan Pajar <christiantoriko227@gmail.com>
Signed-off-by: Euphilia Magenta <xtrffjdev@gmail.com>

---
## [Victor239/tgstation-fork](https://github.com/Victor239/tgstation-fork)@[ebbc45b161...](https://github.com/Victor239/tgstation-fork/commit/ebbc45b1616c08d2dc0b6e6ce48258f68eefd46a)
#### Saturday 2023-09-09 10:54:08 by distributivgesetz

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
## [c0ntradicti0n/dialectics](https://github.com/c0ntradicti0n/dialectics)@[ad72e919d9...](https://github.com/c0ntradicti0n/dialectics/commit/ad72e919d9a3fa84af48ecd002472003271497de)
#### Saturday 2023-09-09 11:25:33 by Stefan Werner

Automated TOC Commit: 2/1/1/3/2/1/2/.Walls.md 2/1/1/2/2/3/.Meditation.md 2/1/1/2/2/2/1/1/.Orgasm.md 2/1/1/3/1/.Health.md 2/1/1/3/3/2/.Observing.md 2/1/1/2/2/3/3/_Genetic-Environmental.md Shelters.md" 2/1/1/2/2/3/.Fertility.md 2/1/1/3/1/2/.Sleep.md 2/1/1/2/2/2/1/.Bisexuality.md 2/1/1/2/2/2/1/3/1/.DNA.md 2/1/1/3/1/2/2/.Dreaming.md 2/1/1/3/2/2/.Shelter.md 2/1/1/2/2/2/3/1/.Cisgender.md 2/1/1/2/2/2/1/3/.Queer.md Care.md" 2/1/1/3/2/1/1/.Foundations.md Period.md" 2/1/1/2/2/2/3/3/3/.Birth.md 2/1/1/2/2/2/2/.Asexuality.md Phase.md" 2/1/1/2/2/2/3/1/.Ovulation.md 2/1/1/3/3/3/2/.Denial.md 2/1/1/2/3/3/.Farming.md 3/2/2/1/1/.Procedural.md 2/1/1/2/2/2/2/2/.Demisexual.md pills.md" 2/1/1/3/1/1/1/.Handwashing.md 2/1/1/2/2/3/2/.Methods.md 2/1/1/2/2/3/3/2/.Nutrition.md management.md" 2/1/1/2/2/2/2/_Desire-Lack.md 2/1/1/3/3/3/3/.Disregard.md 2/1/1/2/2/3/3/.Factors.md 2/1/1/2/1/3/.Climbing.md 2/1/1/2/2/3/2/_Barrier-Hormonal.md 2/1/1/3/2/1/3/.Roofing.md Interactions.md" Health.md" Structures.md" 2/1/1/2/2/2/3/2/1/.Fertilization.md 2/1/1/2/2/2/2/1/.Greysexual.md 2/1/1/3/3/1/2/.Listening.md 2/1/1/3/1/3/1/.Macronutrients.md 2/1/1/2/2/3/2/1/.Condom.md Sleep.md" 2/1/1/2/2/2/_Hetero-Homo.md 3/2/2/1/2/.Object-Oriented.md 2/1/1/2/2/1/_Deprivation-Confrontation.md Ecosystem.md" 2/1/1/2/2/1/1/.Baby.md 2/1/1/3/2/.Housing.md 2/1/1/2/2/2/3/3/.Genderqueer.md 2/1/1/2/2/2/3/3/1/.Trimesters.md 2/1/1/3/1/3/2/.Micronutrients.md 2/1/1/2/2/2/3/3/.Gestation.md 2/1/1/3/3/1/3/.Validating.md 2/1/1/2/2/.Sexuality.md 2/1/1/2/2/2/1/3/.Genetics.md 2/1/1/2/2/2/3/.Identity.md 2/1/1/2/2/2/1/3/2/.Heredity.md 2/1/1/2/2/3/1/3/.Surrogacy.md Paradigms.md" 2/1/1/2/2/2/1/1/2/.Afterglow.md 2/1/1/2/2/2/1/2/3/.Birth.md 2/1/1/2/2/2/2/2/.Foreplay.md 2/1/1/3/3/3/1/.Avoidance.md 2/1/1/2/2/3/3/1/.Genome.md 2/1/1/2/2/2/1/2/1/.Fertilization.md Orientation.md" 2/1/1/2/2/1/2/2/.Girl.md 2/1/1/2/2/2/3/2/.Conception.md 2/1/1/3/3/2/1/.Watching.md 2/1/1/2/2/3/3/3/.Stress.md cycle.md" Cycle.md" Activities.md" 2/1/1/2/2/3/1/_Natural-Artificial.md 2/1/1/3/1/3/3/.Hydration.md 2/1/1/3/3/1/1/.Acknowledgment.md 3/2/2/1/3/.Functional.md 2/1/1/3/1/1/2/.Bathing.md 2/1/1/2/2/2/2/3/.Coitus.md 2/1/1/2/2/3/1/1/.Conception.md Care.md" 2/1/1/2/1/2/.Running.md Languages.md" 3/2/2/1/_High-level-Low-level.md 2/1/1/3/3/1/.Respect.md 2/1/1/2/3/1/.Foraging.md 2/1/1/2/2/1/2/1/.Boy.md 2/1/1/2/2/3/2/3/.IUD.md Activities.md" 2/1/1/2/1/1/.Walking.md 2/1/1/3/3/2/2/.Analyzing.md 2/1/1/2/2/2/3/2/.Transgender.md 2/1/1/3/3/3/.Ignoring.md 2/1/1/3/2/1/.Structure.md Caves.md" 2/1/1/3/3/2/3/.Reflecting.md 2/1/1/2/2/3/1/.Reproduction.md 2/1/1/2/2/3/_Sterile-Fertile.md 2/1/1/2/2/2/1/1/1/.Climax.md 2/1/1/2/3/2/.Hunting.md 2/1/1/2/2/.Rest.md 2/1/1/2/2/2/1/2/.Polysexual.md 2/1/1/2/2/2/3/2/2/.Implantation.md 2/1/1/3/1/1/.Hygiene.md Care.md" 2/1/1/2/2/2/1/3/3/.Mutation.md 2/1/1/2/2/2/1/1/.Pansexual.md 2/1/1/3/1/3/.Nutrition.md 2/1/1/2/2/2/2/1/.Intimacy.md 2/1/1/2/2/2/3/_Born-Becoming.md 2/1/1/2/2/1/.Napping.md 2/1/1/2/2/2/2/3/.Allosexual.md Cycle.md" 2/1/1/2/2/2/_Reproduction-Continuation.md 2/1/1/2/2/3/1/2/.IVF.md 2/1/1/2/_Active-Passive.md Sources.md" 2/1/1/2/2/2/1/2/.Conception.md 2/1/1/2/2/2/3/3/2/.Labor.md 2/1/1/2/2/2/1/_Attraction-Fluidity.md Reproduction.md" 2/1/1/2/2/2/1/2/2/.Gestation.md Phase.md"

---
## [kantasv/comprehensive-rust](https://github.com/kantasv/comprehensive-rust)@[c6af2a0d37...](https://github.com/kantasv/comprehensive-rust/commit/c6af2a0d3732ce8860c65ba7d1ebb23e58947619)
#### Saturday 2023-09-09 12:21:18 by Martin Geisler

Mention how long each course day is (#1155)

Most classes run with 2.5 hours for the morning session and 2.5 hours
for the afternoon session.

I have tried running the course as 2 × 2.5 hours and 2 × 3 hours. My
experience was that people ended up getting really worn out after
spending 6 hours in total on Rust (7 hours including a lunch break).
However, the experience varies from group to group, so this is just a
recommendation.

---
## [42atomys/stud42](https://github.com/42atomys/stud42)@[fec4538f3f...](https://github.com/42atomys/stud42/commit/fec4538f3fdce487cfff5d4e1f19f4ae63fc41fe)
#### Saturday 2023-09-09 12:46:32 by Atomys

feat: implement various quality of life on cluster maps (#512)

**Describe the pull request**

This PR introduces a series of quality of life improvements to the
cluster maps. These enhancements aim to make the maps more
user-friendly, intuitive, and efficient, providing a better user
experience for navigation and overall interaction with the campus map
features. Like:

1. **devexp**: The `totalWorkspaces` in the cluster map definition is no
longer required. This value is now calculated from the given map.
2. Overriding a workspace with no connected user will provide you with
the workspace identifier.
3. When a cluster doesn't have a name, don't display the identifier
twice.
4. The sidebar no longer sticks when scrolling over the cluster sidebar.
5. The scrollbar is now styled to match the application's design.

**Checklist**

- [ ] I have made the modifications or added tests related to my PR
- [ ] I have run the tests and linters locally and they pass
- [ ] I have added/updated the documentation for my RP

---
## [andronic52/Projects](https://github.com/andronic52/Projects)@[3062bfff96...](https://github.com/andronic52/Projects/commit/3062bfff96e3c9a0b7b1aa3a86c949442212dd84)
#### Saturday 2023-09-09 13:06:14 by andronic

Update Game 1 - Running Forever.py

First Game Project on GitHub

Welcome to my GitHub repository! This is my first-ever game project, inspired by the informative and engaging video tutorial titled "The Ultimate Introduction to Pygame" by the YouTube channel Clear Code. 

In this project, I have implemented the concepts and techniques demonstrated in the video to create an exciting game using Pygame.

Pygame is a powerful Python library that allows developers to create interactive games and multimedia applications. Through this project, I have gained hands-on experience with Pygame's key features, such as handling user input, managing game states, implementing game logic, and creating captivating visuals and sound effects.

By exploring the code and resources provided in this repository, you will find a well-structured and professionally developed game. I have strived to adhere to best practices in software development, ensuring clean and readable code, efficient algorithms, and proper documentation.

Feel free to explore the code, experiment with different modifications, and learn from this project. Whether you are a beginner or an experienced developer, this repository serves as a valuable resource for understanding Pygame and game development concepts.

I hope you find this project insightful and inspiring. Enjoy the journey of exploring the world of Pygame and creating your own captivating games!

---
## [andronic52/Projects](https://github.com/andronic52/Projects)@[5a748caf67...](https://github.com/andronic52/Projects/commit/5a748caf6754f08ad11238a6e8e496eadf72dcaf)
#### Saturday 2023-09-09 13:08:36 by andronic

Update Game 2 - Snail lore.py

My First Original Creation on GitHub

Welcome to my GitHub repository! I am thrilled to present my very first original game, lovingly crafted by yours truly. Prepare to embark on a whimsical adventure filled with laughter and entertainment.

Inspired by my passion for game development, I have poured my creativity into this project, resulting in a delightfully goofy gaming experience. From quirky characters to hilarious gameplay mechanics, every aspect of this game reflects my unique vision and sense of humor.

As you explore the code and resources provided in this repository, you will witness the culmination of my efforts to create an engaging and enjoyable gaming experience. I have strived to implement clean and efficient code, ensuring that the game runs smoothly and flawlessly.

This repository serves as a testament to my growth as a developer and showcases my ability to bring ideas to life. I have embraced the challenges of game development, honing my skills in areas such as game design, programming logic, and visual aesthetics.

Feel free to dive into the code, experiment with different features, and witness the magic of this goofy game unfold. Whether you are a fellow developer or simply a gaming enthusiast, this repository offers a glimpse into the joy and creativity that game development can bring.

I hope this game brings a smile to your face and provides a lighthearted escape from the ordinary. Embrace the goofiness and let the fun begin!

---
## [andronic52/Projects](https://github.com/andronic52/Projects)@[6bb00968b1...](https://github.com/andronic52/Projects/commit/6bb00968b1ee3b5baa312df23427923d54c24828)
#### Saturday 2023-09-09 13:09:45 by andronic

Update Game 3 - 75 days hard challenge.py

A Complex Game of Adventure and Challenge on GitHub

Welcome to my GitHub repository! I am thrilled to present my most ambitious project yet, an epic and complex game that has consumed countless hours of dedication and passion. Brace yourself for an immersive adventure filled with challenges, mysteries, and endless possibilities.

In this game, I have pushed the boundaries of my creativity and technical skills to create a rich and expansive world for players to explore. From intricate gameplay mechanics to captivating storytelling, every aspect of this game has been meticulously crafted to provide an unforgettable gaming experience.

As you delve into the code and resources provided in this repository, you will witness the depth and complexity that went into the development of this game. I have invested significant time and effort into designing intricate levels, implementing advanced AI systems, and creating stunning visuals and audio effects.
This repository serves as a testament to my growth as a developer and showcases my ability to tackle complex challenges. Throughout the development process, I have honed my skills in areas such as game design, programming architecture, optimization, and debugging.

While this game may not be fully finished, it represents a significant milestone in my journey as a game developer. I invite you to explore the existing features, witness the attention to detail, and imagine the potential this game holds once completed.
Feel free to dive into the code, experiment with different mechanics, and appreciate the complexity and effort that went into its creation. Whether you are a fellow developer or a passionate gamer, this repository offers a glimpse into the dedication and perseverance required to bring a complex game to life.

I hope this game sparks your imagination and fuels your desire for immersive gaming experiences. Embark on this epic quest and discover the untold wonders that await within!

---
## [Helixis/Shiptest](https://github.com/Helixis/Shiptest)@[b22529fc74...](https://github.com/Helixis/Shiptest/commit/b22529fc74e5af32967ac91679cbce3e7e06c4ca)
#### Saturday 2023-09-09 13:10:34 by zevo

Fixes rock sprites ingame [WHOOPS] (#2332)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Rocks were invisible in game due to a recently merged PR of mine. this
is why we testmerge PRs! anyways this should fix them.

Adds flora and rock missing texture sprites to most flora files to
prevent something like this from ever happening again.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
invisible things that block movement bad yeah. i want to fix my
mistakes.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
fix: Most rocks are now visible again
add: Most flora files now have missing texture sprites to make it easier
to spot when something has gone wrong.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Ldip999/Bubberstation](https://github.com/Ldip999/Bubberstation)@[c6e0ba7516...](https://github.com/Ldip999/Bubberstation/commit/c6e0ba75169d010e2cdfa48134003b0bb9ab8485)
#### Saturday 2023-09-09 13:53:04 by SkyratBot

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
## [Ankan2508/World_Economic_Indicator](https://github.com/Ankan2508/World_Economic_Indicator)@[6d11dcc494...](https://github.com/Ankan2508/World_Economic_Indicator/commit/6d11dcc494ecedd0e19ae622bc963f202d8e130f)
#### Saturday 2023-09-09 14:01:46 by Ankan2508

Add files via upload

Which Factors a Country Should Focus On to Sustain GDP/ Capita.
● Last 12 years of world data was taken into account and GDP/Capita feature 
was also created to analyse the correlation between other factors of a country 
with GDP/Capita.
● We see that factors like Ease of Business, Hours to do tax, Business Tax Rate, 
Lending Interest Rate and Days to start business negatively affect GDP/Capita.
● Health Expenditure%, Energy Usage/Capita, CO2 Emission/Capita, Birth Rate 
and Infant Mortality Rate does not affect GDP/Capita.
● Mobile Phone Usage, Life Expectancy for both Male and Female and Urban 
Population affect GDP/Capita moderately.
● Internet Usage and Health Expenditure/Capita affect GDP/Capita very 
strongly.

---
## [s02hoff/coastalMYSEroosts](https://github.com/s02hoff/coastalMYSEroosts)@[af4899f197...](https://github.com/s02hoff/coastalMYSEroosts/commit/af4899f1976be65f435af395a1882e60a75a3fcb)
#### Saturday 2023-09-09 14:26:29 by s02hoff

Add files via upload

Temperate bats exhibit seasonal and sex differences in resource selection and activity patterns that are influenced by ambient conditions. During fall, individuals face energetic tradeoffs as they make choices relating to migration, mating, and hibernation that may diverge for populations throughout their range. However, research has largely focused on the summer maternity and winter hibernation seasons, whereas the pre-hibernation period remains comparatively understudied. Northern Myotis (Myotis septentrionalis) have experienced precipitous population declines from white-nose syndrome (WNS), leading to their protected status in the United States and Canada. Therefore, understanding their ecology throughout the year is paramount to inform conservation. We compared seasonal roosts and documented fall behaviors between study sites and sexes on three islands: Long Island, New York, and Martha’s Vineyard and Nantucket Island, Massachusetts. Between 2017 – 2020, we radio-tracked 54 individuals to analyze activity patterns and characterize fall roosts to compare with previously known summer roosts. Summer tree roosts were of smaller diameter, later stages of decay, and lower canopy closure than those used in fall. Both sexes selected trees of similar diameter and decay stage during fall. Anthropogenic roost use was documented in both seasons but use of anthropogenic structures was greater during fall and increased as the season progressed. Bats made short inter-roost movements with males traveling greater distances than females on average. Activity occurred until late November, with males exhibiting a longer active period than females. We tracked 23% of tagged bats to local hibernacula in subterranean anthropogenic structures, the majority of which were crawlspaces underneath houses. Use of anthropogenic structures for roosts and hibernacula may facilitate survival of this species in coastal regions despite the presence of WNS infections. Timing of restrictions on forest management activities for bat conservation may be mismatched based on pre-hibernation activity observed in these coastal populations, and the conservation of habitat surrounding anthropogenic roosts or hibernacula may be warranted if the structures themselves cannot be protected.

---
## [RanWithAPlan/RSR](https://github.com/RanWithAPlan/RSR)@[15f4238c27...](https://github.com/RanWithAPlan/RSR/commit/15f4238c274e7ad4b2db4c63c5a6f140c795fa20)
#### Saturday 2023-09-09 14:30:55 by RanWithAPlan

Ran's Plan (oh shit oh fuck we need advisor portraits)

---
## [Aurelien30000/FastAsyncVoxelSniper](https://github.com/Aurelien30000/FastAsyncVoxelSniper)@[e2a351a176...](https://github.com/Aurelien30000/FastAsyncVoxelSniper/commit/e2a351a176ab0c39a3fa9f670ebe939e8d78da24)
#### Saturday 2023-09-09 15:37:44 by Aurélien

Cloud Command System Migration

# Introduction

**This is the first pass of the cloud command migration for FAVS.**
There will be a second one to restore old-fashioned command syntax, tracked as https://github.com/IntellectualSites/fastasyncvoxelsniper/issues/81.

_I have to highlight that this is my first experience with this, must-say wonderful, command system. I have spent a lot of time reading every available documentation and code piece. If @Citymonstret want to take a look and maybe give us tips to avoid "ugly" workarounds or handling, we would be glad!_

The whole pull request has been tested, not yet thoroughly, you can have a global overview, but it is not really ready.

If you have any question or remark, do not hesitate!

--

# General Command Management
I have opted to use the annotations extension of the cloud command system. In my opinion, this is better suited to the current brush format handling which is all done inside brush classes.

**Executors have been kept and brush & performer command are still handled inside their classes.**

- ``Snipe`` class has been extended for a usage as a commander, because FAVS relies on a lot on this class.
- ``CommandRegistry`` is the main place for the whole handling behind the scenes. Otherwise, commands are registered as usually done in cloud, with some specific annotations when needed.

**``SniperCommander`` class is the commander to use with cloud command system. If the player exists, it returns its sniper. Otherwise, it returns a simple ``SniperSender``, similar to ``CommandSender``.**

# Command Manager
FAVS uses the paper command manager, when available, to enjoy some improvements. Falls back to bukkit command manager otherwise.

- Async tab-completions are enabled if available.
- ``Snipe``, ``PerformerSnipe`` & ``Toolkit`` classes are registered into the injector in order to be injected in command methods.
- Command exceptions are adapted and customized with the FAVS message syntax.

# Command Post-Processor
FAVS requires the command post-processor ins order handle specific FAVS behavior.

- Handles the ``@RequireToolkit`` annotation, makes sure the toolkit is available and the value stored.
- Handles the ``@DynamicRange`` annotation, used to define a range from non-constant variables, using reflection.
- Prepares the brush & performer when needed, their ``Snipe`` and stores them.

# Annotations & Parser
FAVS uses some annotations to facilitate development, based on common rules and behaviors.

- Handles the ``@RequireToolkit`` annotation, modifies the command meta.
- Handles the custom command execution method handler, which should differ for brush & performer. Cloud commands are designed to live in a class instance, this is not suitable to the current management of brush & performer. I have opted for a custom execution method which uses the brush & performer instance from the execution context instead of the base instance. _This avoid extra parameters for each command method._

# Arguments
FAVS needs a lot of custom arguments for either factories, registries, custom types, custom needs, etc.

**Suggestions & parsers are also declared via annotations in custom classes.**

# Other Changes
- All classes related to internal command managing from VS have been removed.
- ``FastAsyncVoxelSniper`` class has been removed. As far as I know, this class was useless and is now for sure.
- Some classes and methods have been added or refactored, but the overall codebase is the same to try keeping maximum compatibility.
- Some translations have been reorganized or removed.
- Some code format has been modified, there will be another pull request next year hopefully to unify comments format.
- Improvements to brush properties loading. Previously, all aliases were loaded, subsequently loading the same brush several times.
- Modern switch syntax has replaced old ones.
- General improvements.

# Known Problems:
- There is currently one small issue with static/literal arguments and their aliases. Tab-completions are not handled for all aliases due to https://github.com/Incendo/cloud/blob/master/cloud-core/src/main/java/cloud/commandframework/arguments/StaticArgument.java#L134.
- Brigadier extension is voluntarily not used due to some incompatibilities with FAVS commands syntax.

---
## [timDeHof/next-3d-portfolio](https://github.com/timDeHof/next-3d-portfolio)@[74c44a616a...](https://github.com/timDeHof/next-3d-portfolio/commit/74c44a616a1d10724809fcb13693322d37eafc46)
#### Saturday 2023-09-09 16:24:08 by timDeHof

feat(next.config.js): update pageExtensions to include 'md' and 'mdx' file extensions
feat(next.config.js): enable reactStrictMode for stricter React mode
The pageExtensions configuration in next.config.js is updated to include 'md' and 'mdx' file extensions. This allows Next.js to handle Markdown files as pages. Additionally, the reactStrictMode configuration is set to true to enable stricter mode for React, which helps catch potential issues and improve overall code quality.

feat(package.json): add next-mdx-remote and remark-unwrap-images dependencies
The next-mdx-remote and remark-unwrap-images dependencies are added to the package.json file. next-mdx-remote is a library that allows rendering MDX content in Next.js applications, while remark-unwrap-images is a plugin for remark that unwraps images from paragraphs in Markdown files. These dependencies are necessary for handling and rendering MDX content in the application.

feat(components/MDX

feat(content): add two new blog posts

Added two new blog posts to the content directory: "The Power of a Growth Mindset in Software Development - How to Embrace Challenges and Advance Your Career" and "How to Deploy the Face Recognition API for Free with Render - Alternative to Heroku".

The first blog post discusses the importance of having a growth mindset in software development and provides tips for developing and maintaining this mindset. It emphasizes the benefits of embracing challenges and continuously improving skills.

The second blog post focuses on deploying the Face Recognition API using Render as an alternative to Heroku. It provides step-by-step instructions on setting up a Render database, connecting to the database in the API, and deploying the API as a web service on Render.

These blog posts aim to provide valuable insights and practical guidance to readers in the field of software development.

feat: add blog post "From Mechanical Design Engineer to Fullstack Developer - My Journey and Lessons Learned"

This commit adds a new blog post titled "From Mechanical Design Engineer to Fullstack Developer - My Journey and Lessons Learned". The blog post details my personal journey and experiences transitioning from a mechanical design engineer to a fullstack developer. It covers topics such as my decision to make a career change, the coding bootcamp I attended, the technologies I learned, and the challenges I faced along the way. The blog post also includes information about a group capstone project I worked on during the bootcamp and my job search as a fullstack developer. Additionally, it highlights the soft skills I developed and the lessons I learned throughout the journey.

The purpose of this commit is to add valuable content to the blog and share my experiences and insights with others who may be considering a similar career transition.

feat: add blog post "Unleash the Power of Java - A JavaScript Developer's Guide to Best Practices in Java Development"

This commit adds a new blog post titled "Unleash the Power of Java - A JavaScript Developer's Guide to Best Practices in Java Development". The blog post discusses the key differences between Java and JavaScript in terms of object-oriented programming, code style and formatting, and exception handling. It also provides learning resources for JavaScript developers transitioning to Java.

The blog post aims to help JavaScript developers understand the best practices and conventions in Java development, enabling them to leverage their existing knowledge and skills while diving into the world of Java.

feat: add blog post about debugging an empty API response in Axios

This commit adds a new blog post titled "Unraveling the Mystery of an Empty API Response in Axios - A Debugging Adventure". The blog post discusses a common issue that can occur when using React Query and Axios to fetch data from an API. It provides a step-by-step guide on how to debug and solve the issue.

The blog post covers the following topics:
- The problem of receiving an empty API response in React Query
- Debugging the issue by inspecting the code and API response
- Adding logging statements to track the API request and response
- Troubleshooting approaches such as verifying the API request, checking API status, and trying a different API endpoint
- Considering frontend code and data processing/display as potential sources of the issue
- The importance of effective debugging and a systematic approach to problem-solving

The commit also includes code snippets that demonstrate the added logging statements to the `get

feat(blog): add support for rendering markdown content using MDX
The blog page now supports rendering markdown content using MDX. This allows for more flexibility in styling and customizing the rendering of markdown content. The page now uses the `MDXRemote` component from `next-mdx-remote` to render the markdown content. The `MDXProvider` component is used to provide custom components for rendering specific markdown elements. The `components` object defines the custom components to be used for rendering specific markdown elements. The markdown content is serialized using the `serialize` function from `next-mdx-remote/serialize`. This allows for the markdown content to be transformed into an MDX source that can be rendered by the `MDXRemote` component.

---
## [Sea-of-Lost-Souls/Tannhauser-Gate](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate)@[4012db7ce2...](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate/commit/4012db7ce2315160882c5e375ca429fe1c8f20ef)
#### Saturday 2023-09-09 16:27:34 by SkyratBot

[MIRROR] Adds Blood-drunk and demonic frost miner boss music. [MDB IGNORE] (#23543)

* Adds Blood-drunk and demonic frost miner boss music. (#78123)

Acts as a continuation of PR #77149 for boss music functionality and
implements a BDM and demonic frost miner boss music theme.

More music is good, but I do have some gripes with my own PR. This
particular track relies on instrumentation that when compressed just
doesn't sound as good, and the in-game version is noticeably less
enjoyable that the high quality version. I wish I could help the track
out more, but as is it's already at 811 kb which is barely in line with
file requirements, so i just can't justify bloating the audio file sizes
to make it sound better. You notice this kind of problem a lot with the
higher runtime music and background tracks. It just feels a bit more
clunky than hierophant, but what are you gonna do right?

* Adds Blood-drunk and demonic frost miner boss music.

---------

Co-authored-by: RICK IM RI <77305289+tommysalami3@users.noreply.github.com>

---
## [Waaal/BobaOS](https://github.com/Waaal/BobaOS)@[867ac8e9bb...](https://github.com/Waaal/BobaOS/commit/867ac8e9bbeab1eb95f1dfb302bdd81b89f02040)
#### Saturday 2023-09-09 17:09:42 by Waaal

It just took me 6 stupid hours to recherche and understand this

I hate my life

---
## [Make-Tarkov-Great-Again/MTGO-Launcher](https://github.com/Make-Tarkov-Great-Again/MTGO-Launcher)@[81c19f55c6...](https://github.com/Make-Tarkov-Great-Again/MTGO-Launcher/commit/81c19f55c6852e11b14fc2e7cf317db4bca6fdea)
#### Saturday 2023-09-09 17:25:00 by Kes

[Add] Test func Launcher.Ui.ErrorCTX

Test function, fucking with ctx, god fucking dammit i hate CTX so much.

---
## [Cheemaroni/Cheemaroni.github.io](https://github.com/Cheemaroni/Cheemaroni.github.io)@[58f8200664...](https://github.com/Cheemaroni/Cheemaroni.github.io/commit/58f8200664b3d882caa125851e2ca8c95bd942c9)
#### Saturday 2023-09-09 17:58:47 by Cheemaroni

Revert "fuck you"

This reverts commit e797d22f568a9f03904f85aa55a74dd882317991.

---
## [c4xmaniac2/cmss13](https://github.com/c4xmaniac2/cmss13)@[ce818246c1...](https://github.com/c4xmaniac2/cmss13/commit/ce818246c107cf97525a05f6f3a66e120117b8c3)
#### Saturday 2023-09-09 19:30:20 by QuickLode

The Hazmat Joe (#3259)

# About the pull request
This pull request resprites the entire Working Joe from toes to head. It
also gives two additional uniforms which are meant for hazardous use,
and this PR should act as a foundation for future implementation of the
Hazmat Joe into CM's gameplay. Additionally, I may just set this to
draft and let it be reviewed while I work on the actual implementation.

They are complete with distinctive loadouts, which focus more on
hazardous situations, repair, and firefighting. Though may tweak things
depending on how its implemented.

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game
This adds a fan favorite variation of your inexpensive, reliable friend!
You've seen him in quite a few places, and now he's coming to CM!

Also, the resprite of the Joe fixes up some minor sprite issues that
were encountered on previous models.

More content, more roleplay possibilities! ARES! Get me some Joes to put
that reactor fire out ASAP!
# Testing Photographs and Procedure

https://cdn.discordapp.com/attachments/490668342357786645/1104748917398175795/image.png

https://media.discordapp.net/attachments/490668342357786645/1105643891107049572/image.png
Ran several tests and they went well.


# Changelog
:cl:QuickLoad,Frans_Feiffer,nauticall
add: Adds The Hazmat Joe with two minor variations. This is a Working
Joe equipped to handle hazardous situations, dangerous repairs and
firefighting! They are complete with their own gear, tasks, job and
purpose. Forget the trashbag, get that wall fixed before we get spaced!
imageadd: Adds a new Working Joe model made by Frans Feiffer!
imageadd: Adds two variations of the Working Joe, aka the Hazmat Joe.
Complete with accessories! Beautiful sprites by Frans Feiffer!
add: Android Maintenance Stations / Synthetic Repair Stations will
remove shrapnel & fix organ damage. Working Joes no longer have knives,
and should report to the stations for repair. Gigantic thanks to
nauticall for her work on this!!
imagedel: Removes(replaces) the old Working Joe model.
add: Working Joes receive some basic equipment, and are slightly
resilient to disarms.
add: Working Joes will start at 3, with a maximum of 6 depending on
population.
add: Joes can access a Synthetic vendor to replace their uniform if it
is damaged.
fix: Minor changes to PO Uniform.
/:cl:

---------

Co-authored-by: naut <nautilussplat@gmail.com>
Co-authored-by: BeagleGaming1 <56142455+BeagleGaming1@users.noreply.github.com>

---
## [Fargowilta/FargowiltasSouls](https://github.com/Fargowilta/FargowiltasSouls)@[ac29110cb3...](https://github.com/Fargowilta/FargowiltasSouls/commit/ac29110cb36901c2a45515ec03b2cdadf633beb9)
#### Saturday 2023-09-09 20:00:53 by JavyzTaken

Banished Baron now positions himself a bit further up for the laser attack so he doesn't fuck you

---
## [Sealed101/tgstation](https://github.com/Sealed101/tgstation)@[4b8de7b79f...](https://github.com/Sealed101/tgstation/commit/4b8de7b79f0a343dc587d0d17eb9361ecc7103c1)
#### Saturday 2023-09-09 20:16:49 by san7890

Refactors the `notransform` variable into a trait. (#78146)

## About The Pull Request

Hey there,

There were more than a few times (like in cinematic code) where we might
need to accurately know the source of what's adding this trait (or have
multiple sources for the whole 'we don't want this mob to do shit while
we transform this mob'), so in order to rectify this potential issue,
let's refactor it into a trait.

## Why It's Good For The Game

Some code already declared that there might be issues with this being a
boolean var (with no way of knowing _why_ we don't want this mob to not
transform (or not do anything idk). Let's remove those comments and any
future doubt in those instances with the trait macros. Also, stuff like
`TRAIT_IMMOBILIZED` which does a similar thing in many contexts was
already a trait that was regularly added in conjunction with flipping
the variable, so we're able to flatten all that stuff into
`add_traits()` and `remove_traits()` now. nice

I also cleaned up quite a bit of code as I saw it, let me know if it
should be split out but I guarantee that if I didn't do it- no one will
for the next two years.

## Changelog

:cl:
refactor: If you transform into another mob and notice bugs with
interacting with the game world, please create a bug report as this
framework was recently refactored.
/:cl:

Probably fucked up somewhere, lmk

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[f542031a51...](https://github.com/treckstar/yolo-octo-hipster/commit/f542031a51db0a5b2b50784a111efb9a00d5eb23)
#### Saturday 2023-09-09 20:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [Kindrik/Candid](https://github.com/Kindrik/Candid)@[f05483d395...](https://github.com/Kindrik/Candid/commit/f05483d3958a71684b0975949f8138896198cf3f)
#### Saturday 2023-09-09 20:25:36 by Josh

a few things have been changed around here. I added redux, so that I could showcase my understanding of it, its obviously not that useful in an app this small, where I would try to contain local state, and only use redux for global state. I also changed the url to the homepage, and added a target_blank to the url, allowing it to pop up in a new window. I also moved the card to its own component, and call it in the app component. I try to keep my components to 150 lines of code before i start to think on how to break them up. Struggling a bit with how i want to add the 24 hour commits, and also a demonstration SPA, which will probably be some dummy pages in a header.

---
## [nn9dev/pokeheartgold](https://github.com/nn9dev/pokeheartgold)@[7d1d878531...](https://github.com/nn9dev/pokeheartgold/commit/7d1d878531f6b438fa8f1ea7270e1390ec345f05)
#### Saturday 2023-09-09 22:10:53 by nn9dev

Begin documenting maps

Decided to push this now since I keep forgetting to work on it. Some points for conversation/consideration are below.

- Should we use "Sea Route #"/"Water Route #" (Like Bulbapedia names it) or just stick to "route #" ?

- Should houses be simply assigned 1-x depending on the lowest value?
	- Ecruteak does not have a "House 2", T27R0202 is Barrier Station Underground

- Not sure how to label Pokecenter floors since 1F is the first floor you come in on
	- Could not decide between upper/lower or 1F/B1F

- Some gates are labelled by their route and not their city/town/point of interest
	- see MAP_R35R0101 (rt 35 south gate) vs MAP_T23R0101 (town 23 (azalea), west gate)

- I think Ecruteak is the only place with a pokecenter that has more than two rooms
	- rather, i believe all Union Rooms/Wi-Fi Battle rooms/PCCC's use Ecruteak's Pokecenter

- MAP_ECRUTEAK_PCCC is the Pokémon Communication Club Colosseum
	- Didn't wanna put all that because it looked messy

- the Union cave map is really fucked up and has some areas that are labelled different floors on Bulbapedia on the same map so this one sucks

- Some maps I tried to stick to Bulbapedia's naming conventions (i.e. Diglett's Cave South Exit, i did not label it as an entrance)

- did not include "store" in MAP_GOLDENROD_DEPARTMENT_BASEMENT because I would've had to do another indent, but obviously I can if it's wanted

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[009af8c2ce...](https://github.com/tgstation/tgstation/commit/009af8c2ce5c18ca4fdaceb4e4d2c17d8e8d6d00)
#### Saturday 2023-09-09 23:20:23 by nikothedude

[TEST-MERGE FIRST] Wound refactor number two: Full synthetic support (#78124)

## About The Pull Request

Heavily refactors wounds AGAIN.

The primary thing this PR does is completely change how wounds are
generated and added - while the normal "hit a guy til they bleed" stuff
works about the same, asking for a specific type of wound, say, like how
vending machines try to apply a compound fracture sometimes, isnt going
to work if we ever get any non-organic wounds, which the previous
refactor allowed.

With this PR, however...
* You can now ask for a specific type of wound via
get_corresponding_wound_type(), which takes wound types, a limb, wound
series, etc. and will try to give you a wound fitting those
specifications - but also, a wound that can be applied to a limb.
* This will allow for a vending machine to apply a compound fracture to
a human, but a collapsed superstructure (assuming my synth wounds go in)
to a robot

There are now new "series types" and "wound specific types" that allow
us to designate what series are "mainline" and randomly generatable, and
what are "alternate types" and must be generated manually - you can see
the documentation in wounds.dm.

The behavior of limping and interaction delays has been abstracted to
datum/wound from bone wounds to allow just, general ease of development

Pregen data now allows for series-specific wound penalties. Example: You
could set a burn wound's series wound penalty to 40, which would make
wound progression in the burn category easier - but it would not make it
any easier to get a slashing wound. As it stands wound penalties are for
wounds globally

Scar files are now picked in a "priority" list, where the wound checks
to see if the limb has a biostate before moving down in said list.
Example: Wounds will check for flesh first, if it finds it - it will use
the flesh scar list. Failing that, they then check bone - if it uses
that, it will use the bone scar list. This allows for significantly more
modular scars that dont even need much proc editing when a new wound
type is added

Misc changes: most initial() usage has been replaced by singleton
datums, wound_type is now wound_types and thus wounds can accept
multiple wound types, wounds can now accept multiple tool behaviors for
treatment, wounds now have a picking weight so we can make certain
wounds rarer flatly,

This PR also allows for wounds to override lower severity wounds on
generation, allowing eswords to jump to avulsions - but in spirit of
refactoring, this has been disabled by default (see pregen data's
competition_mode var).
## Why It's Good For The Game

Code quality is good!

Also, all the changes above allow wounds to be a MUCH more modular
system, which is one of its biggest problems right now - everything is
kinda hardcoded and static, making creative work within wounds harder to
do.

## Changelog
:cl:
refactor: Refactored wounds yet again
fix: Wounds are now picked from the most severe down again, meaning
eswords can jump to avulsions
fix: Scar descs are now properly applied
/:cl:

---
## [RoccoIsATaco/zmk-dactyl-nicenano-v2](https://github.com/RoccoIsATaco/zmk-dactyl-nicenano-v2)@[d3232c33cb...](https://github.com/RoccoIsATaco/zmk-dactyl-nicenano-v2/commit/d3232c33cb14aae7a6bf1a7c6aa2bc08b9cb3062)
#### Saturday 2023-09-09 23:26:35 by Rocco

suck wide shit github i hope your inventor gets fucked to death by wolf

---
## [RikerW/dNAO](https://github.com/RikerW/dNAO)@[d27fe0ec2c...](https://github.com/RikerW/dNAO/commit/d27fe0ec2c1ef16af2d4a9a3d3eb35df9464d592)
#### Saturday 2023-09-09 23:28:16 by RikerW

colored branch stairs and also incs eat whistles now

issue #1379 - Colored branch stairs ought to be implemented for QoL improvements. now with free colored altars. so basically, they exist now. the "default" color is yellow but almost all branches are recolored to be distinct because i could - for example, mines is brown, sea is yellow, temple is red, tomb is black, etc. this includes (because reasons) outlands<->rlyeh and outlands<->dispensary but i believe that's all of the "branch" stairs in the dungeon. oh VOTD is grey/white due to being overriden by VOTD colors, but who cares, that's not a very helpful one to turn yellow. anyway, so this exists. uses S_brdnstair and S_brupstair like vanilla & other variants does, and handling should be added for all relevant things, including moving the "<= S_dnstair"s to use branch stairs instead when checking certain "end of dungeon feature" glyph lists. support has been added for DEC/IBM/UTF graphics too if barely, they render same as stairs but colored rather than as ladders. branch ladders don't exist btw so don't add those without adding the appropriate symbol i guess. altars also now get hallu colors with god's worst redraw function. i jest it's not that bad but yeah added see_altars to see_traps/_objects_monsters, which does the similar thing, but clears the glyph buffer (extra operations whoo) instead of just calling newsym because altars are all S_altar recolored, so the game needs to recompute colors, and so if other "color shifting" glyphs are added this could be problematic. shouldn't be a huge deal though since i don't expect any other things to change color per turn since they wouldn't work without a redraw anyway. hallu altars are random color, and then lnc is white/grey/black, unaligned yellow, void red (idk black is used, blue is black for a lot of ppl i think, maybe make htat magenta. up 2 chris)
issue #2099 - Incantifiers should be able to eat magic whistles. yeah let netsysfire cook bro is onto something fr

also fixes a stupid typo about god giving minions being loyal not just randomly nooping edog->loyal. worst part is that i fixed that in a force push but fucked MORE shit up so the new force push broke it RIP in pieces

---
## [carlarctg/tgstation](https://github.com/carlarctg/tgstation)@[4792a8e19d...](https://github.com/carlarctg/tgstation/commit/4792a8e19dc6885a2f6e8d25f1086505624e7a6c)
#### Saturday 2023-09-09 23:31:29 by carlarctg

Nerfs Confusion symptom for diseases (#77991)

## About The Pull Request

Removed the threshold for confusion symptom that adds illiteracy to the
disease.

Clamps confusion symptom's confusion to a maximum of 30 seconds.

Confusion as a debuff no longer guarantees random movement if you're
resting.

## Why It's Good For The Game

> Removed the threshold for confusion symptom that adds illiteracy to
the disease.

This virus makes you unable to actually treat yourself when cured, which
is frankly bonkers. Viruses are too virulent and it's rare that a doctor
actually gets to a biosuit in time to inoculate themselves, and if they
forget internals they're screwed anyways. People should be able to fix
their own got damn disease, this is asinine.

> Clamps confusion symptom's confusion to a maximum of 30 seconds.

The lack of clamping literally makes this symptom send your confusion
level to the fucking atmosphere, you can easily get upwards of 5 minutes
of confusion left because it doesn't clamp, adds 16 seconds per
activation, which is made even worse by the fact that confusion gets
stronger the more duration confusion has on you.

> Confusion as a debuff no longer guarantees random movement if you're
resting.

This remedies the last bit by not making it a literal guarantee that you
can't move in any direction after...... *3* triggers of confusion. It
should be obvious to anyone how absurd this is.

Honestly, it's plain as day that the only reason any of this ended up
like it is because of poor coding and oversights. This is just bringing
things down to their designed level.

## Changelog

:cl:
del: Removed the threshold for confusion symptom that adds illiteracy to
the disease.
balance: Clamps confusion symptom's confusion to a maximum of 30
seconds.
qol: Confusion as a debuff no longer guarantees random movement if
you're resting.
/:cl:

---
## [ManyRios/zechub](https://github.com/ManyRios/zechub)@[5a6601eb41...](https://github.com/ManyRios/zechub/commit/5a6601eb41f22a7d984aa1fcb4ddb4c41d704765)
#### Saturday 2023-09-09 23:38:28 by Hardaeborla

Non Custodial Exchanges.md



In the ever-evolving world of cryptocurrency trading, the rise of non-custodial exchanges which is also known as Decentralized Exchanges or DEXs is redefining how users engage with digital assets. These platforms offer a revolutionary approach to trading by eliminating the need for intermediaries or third party and putting control firmly in the hands of users.

It is also undoubtedly that as Zcash is concerned, privacy matters as it remains an innovative project that pushes the boundaries of privacy within the cryptocurrency space, offering users the option to transact in a more confidential and secure manner.

In this piece, we'll delve into the present non-custodial exchanges that enable you to effortlessly obtain and trade Zcash independently, without the need for intermediaries in the transaction process. Before we dive into these accessible non-custodial exchanges for acquiring Zcash, let's take a quick look at Non-Custodial Exchanges (DEXs) vs Centralized Exchanges to gain a better understanding.

### **Understanding Non Custodial Exchanges In Brief** 
Non-custodial exchanges, also known as Decentralized Exchanges (DEXs) are platforms that facilitate cryptocurrency trading without requiring users to deposit their funds into the exchange itself. Instead, users retain control of their private keys and trade directly from their wallets without the need for third parties. This decentralized approach enhances security and privacy, as users are not reliant on the exchange to hold their assets which also reduces the risk of hacks or mismanagement. Transactions on non-custodial exchanges often leverage smart contracts to ensure trustless and transparent trading. 

A key advantage of non-custodial cryptocurrency exchanges lies in the increased control they provide to users over their assets. As these exchanges don't retain the assets, users enjoy complete ownership and authority over their digital currencies. This aspect can be especially attractive to individuals worried about asset security.

### **Understanding Custodial Exchanges** 
Custodial Exchanges are also known as centralized Exchanges. They are cryptocurrency trading platforms where users deposit their funds into accounts managed by the exchange itself. In this model, users entrust the exchange with the custody of their assets, meaning the exchange holds and controls the private keys necessary to access and manage the cryptocurrencies. This setup can provide convenience, especially for newcomers to the cryptocurrency space, but it also means users are reliant on the exchange's security measures. While custodial exchanges often offer user-friendly interfaces and customer support, they may present higher security risks due to the centralization of funds and the potential for hacks or mismanagement.


An advantage of custodial exchanges is their provision of a straightforward and user-friendly interface, simplifying the initiation of crypto trading for newcomers. Additionally, these exchanges offer an array of functionalities, including charting tools, real-time market information, and the capability to establish stop-loss orders, catering to the needs of more seasoned traders

### **Non Custodial Exchanges Vs Custodial Exchanges** 

**#1 Security**
Non-custodial exchanges eliminate the need for users to trust a central entity with their funds or assets. This enable users to maintain and have control of their private keys, reducing the risk of hacks, insider attacks and platform vulnerabilities that custodial exchanges may experience. 


**#2 Privacy**: Non-custodial exchanges often provide greater privacy by allowing users to trade directly from their wallets without the need for any intermediary. Transactions can be executed with greater anonymity, as sensitive information is not stored unlike Centralized Exchanges 


**#3 Decentralization**: Non-custodial exchanges align more closely with the decentralized ethos of cryptocurrencies. Users have greater autonomy and control over their trading activities, in line with the broader principles of blockchain technology.

When it comes to Custodial Exchanges, the level of Decentralization is often quite minimal in most centralized exchanges which give rise to the exchange team or officials managing user data or information on the exchange. 


**#4 Adaptability to Changing Regulations**: Non-custodial exchanges are often more adaptable to changing regulatory environments. Since they do not hold user funds, they might have fewer compliance challenges compared to custodial exchanges.




**#5 Innovation and Experimentation**: Non-custodial exchanges frequently drive innovation in the crypto space. They encourage the development of decentralized technologies, such as automated market makers (AMMs) and decentralized finance (DeFi) applications.



**#6 Global Accessibility**: Non-custodial exchanges often provide access to cryptocurrencies for users around the world, including regions where regulatory hurdles might limit the availability of custodial exchange services.

**#7 No KYC Requirements**: 
Many non-custodial exchanges do not require users to undergo extensive know-your-customer (KYC) procedures, offering a level of privacy and inclusivity that is absent in some custodial platforms.



While non-custodial exchanges offer compelling advantages, it's important to acknowledge that they might come with drawbacks, such as potential liquidity issues and a steeper learning curve for less experienced users. As with any financial decision, traders should carefully assess their priorities, risk tolerance, and familiarity with the technology before choosing between non-custodial and custodial exchange options.

Now, let's explore a few of the accessible non-custodial exchanges that facilitate Zcash trading. Utilizing these platforms will provide you with a convenient means to acquire more Zcash coins.

### **Non Custodial Exchanges To Trade or Acquire Zcash**

**#1 Simple Swap** 
SimpleSwap presents an exchange platform providing swift and straightforward swaps for users globally. The process is uncomplicated as it enable users to exchange cryptocurrencies, earn SWAP tokens, acquire a subscription and acquire BTC. No registration is necessary for conducting exchanges through the SimpleSwap Mobile App or web service.

SimpleSwap supports Transparent Address on both Zcash Blockchain and Binance Smartchain (Bep20). It enables you swap your Zcash tokens into other supported coins like USDT very easily. Follow the below steps as tested by [Zula](https://free2z.cash/Zula/zpage/como-hacer-intercambio-de-zecs) 

* Visit [SimpleSwap](https://simpleswap.io/) either Web or mobile app. 


* Select the Supported Crypto Pairs, in this case I'm selecting ZEC and USDT 

* Enter amount of ZEC you intend to swap on the DEX and paste the address. 










 

SimpleSwap DEX Link :https://simpleswap.io

Mobile App (Android):https://simpleswap-subdomain.onelink.me/XxkL/4d83a727


Mobile App (iPhone):https://simpleswap-subdomain.onelink.me/XxkL/85fe1e52

**#2 Fixed Float** 
Fixed Float is another non Custodial Exchange that has been in existence since 2018 and it equips you with the means to fully leverage your digital assets via a user-friendly and accessible exchange platform. 

[Fixed Float](https://fixedfloat.com/) also supports swapping and trading of Zcash on it's DEX as it enables you to swap ZEC easily into other supported cryptos available on the DEX.

[Fixed Float](https://fixedfloat.com/) can easily be used to swap ZEC as explained by [Zula](https://free2z.cash/Zula/zpage/como-hacer-intercambio-de-zecs) in the below description;

FixedFloat DEX Link: https://fixedfloat.com


**#3 SideShift** 
Experience the No Registration Crypto Exchange. Seamlessly switch between BTC, ETH, BCH, XAI, and over 100 other cryptocurrencies all without needing an account using SideShift.

SideShift is another non-custodial exchange that facilitates trading of Zcash. It supports both shielded and transparent Zcash wallet addresses on its decentralized exchange (DEX), offering user-friendly accessibility for Zcash trading.

Check out the guide on how to swap your ZEC on SideShift in the below description;


 
**#4 Changelly**
[Changelly](https://changelly.com/) stands out as a user-friendly non-custodial exchange that enables hassle-free trading or swapping of Zcash for various other supported assets. 

During the swapping process, this non-custodial exchange facilitates transactions with Zcash Transparent wallets. Discover the instructions below for guidance on how to proceed:


You can learn more about how it works [here](https://changelly.com/blog/how-to-exchange-crypto-on-changelly/) 

Changelly DEX Link: https://changelly.com/


**#5 Trocador** 
[Trocador](https://trocador.app/en/) serves as a privacy-centric exchange aggregator. The team hold the conviction that cryptocurrency possesses the potential to counteract government overreach, censorship, and tyranny, fostering decentralization and liberty for a world that thrives in prosperity and freedom.

This Non Custodial Exchange also support the trading of Zcash by depositing and withdrawing through the Zcash mainnet address. 

Trocador DEX Link: https://trocador.app/en/


**#6 Swapzone** 
Swapzone is Swapzone is a cryptocurrency exchange aggregator that enables user to browse through services, compare exchange rates, analyze and swap cryptocurrency in just one interface. All swaps are custody-free, with no registration needed.

[Swapzone](https://swapzone.io/) also supports the trading and swapping of Zcash including deposits and withdrawals of Zcash addresses such as Transparent, Bep20, Hecochain and BEP2. 


Swapzone Link:https://swapzone.io/

**#7 Flyp**
Flyp stands as the swiftest, most secure and exceedingly confidential means of swapping over 30 cryptocurrencies directly into your wallet. There's no need for registration, email, or an account. A single click effortlessly facilitates instantaneous exchanges. Your privacy and private keys are under your constant command. The process is as straightforward as executing a transaction from your own wallet. 

The good news is that Flyp.me also supports Zcash transactions on it's DEX, users have option to input either their Transparent Address (recommended) or shielded or unified address. 


Flyp.me DEX Link: https://flyp.me/



**#8 Pancakeswap** 
[Pancakeswap](https://pancakeswap.finance/swap) stands as the top decentralized exchange on the BNB Smart Chain, boasting the market's highest trading volumes.

The non Custodial Exchange supports swapping of Zcash (Bep20) into other crypto assets on the BNB Chain Cake, BNB, USDT and others. 


DEX Link:https://pancakeswap.finance/swap

**#9 Decred** 
Decred DEX enables you to engage in peer-to-peer cryptocurrency trading without any trading fees or KYC requirements. DCRDEX represents a decentralized exchange crafted by the Decred Project.

[Decred DEX](https://dex.decred.org/) also supports the Swapping and trading of Zcash on it's DEX and users are able to deposit and withdraw Zcash tokens either transparently or privately. 

DEX Link : https://dex.decred.org/

**#10 GODEX** 
[GODEX](https://godex.io/) stands out as a high-speed exchange platform, with order executions typically taking between 5 to 30 minutes. The execution time is contingent upon confirmation speed within the decentralized network, with larger amounts, such as those exceeding 1 BTC, often requiring more time. The DEX dependability rests on contemporary security protocols and robust physical server protection.

The DEX offers support for both Transparent (t-address) and Shielded (z-address) transactions from the Zcash Network. GODEX further facilitates the effortless swapping and trading of tokens.

DEX Link: https://godex.io/
Android App:  https://play.google.com/store/apps/details?id=com.godex.app.GodexApp




**#11 ChangeNow** 
ChangeNOW operates as a non-custodial platform designed to facilitate swift and straightforward cryptocurrency exchanges. The DEX focus is on providing the utmost security, ease of use, and convenience. The DEX neither retain your funds nor mandate any form of account setup. With nearly 700 coins accessible for exchange, ChangeNOW imposes no restrictions; you can perform exchanges to your heart's content without an account, all while ensuring a speedy process. 

ChangeNOW also supports Zcash deposit and withdrawals using address from Zcash mainnet and Bep20 (Binance Smartchain) Network. 

**#12 StealthEx** 
StealthEX offers non-custodial cryptocurrency exchanges where there's no need to set up an account or reveal personal information. Additionally, funds are not stored on StealthEX; exchanges occur directly between wallets.

[StealthEX](https://stealthex.io/) also supports the withdrawal and deposits of Zcash mainnet addresses including swapping and trading of Zcash. 

DEX Link: https://stealthex.io

Mobile App : https://play.google.com/store/apps/details?id=com.stealthex

**#13 SwapSpace** 
SwapSpace serves as a real-time aggregator for cryptocurrency exchanges. The platform empowers you to select from various swap offers provided by major crypto exchanges, all conveniently assembled in a single location. [SwapSpace](https://swapspace.co/) is committed to streamlining the exchange experience, granting access to over 2650 cryptocurrencies for swift, registration-free swaps, all at the most competitive rates available in the market. 

Through the [SwapSpace DEX](https://swapspace.co), individuals have the capability to engage in trading and withdrawals involving Zcash using various options including Zcash mainnet address, Zcash (Bep20), Zcash (Bep20), and Zcash on the Heco Chain.

DEX Link : https://swapspace.co


**#14 ChangeHero** 
ChangeHero combines a UX flow of decentralized exchange with liquidity from multiple popular CEXs after successful DEX integration as announced by the team [here](https://changehero.io/blog/dex-integration-in-changehero/) 

Change Hero also supports trading and swapping of Zcash into other available tokens on the DEX. The DEX also supports Zcash mainnet (t-address) address on it's platform. 

DEX Link: https://changehero.io/


**#15 EasyBit** 
EasyBit is also a non Custodial Exchange that enables users to swap and trade digital assets easily on it's DEX.  It operates without a central authority or intermediary, allowing users to trade directly from their wallets and retaining control over their private keys.

Users can also trade Zcash with EasyBit as the DEX also supports Zcash mainnet network, Zcash (Bep20) and Zcash (BEP2) 

DEX Link: https://easybit.com/en/

### **Conclusion** 

Non-custodial exchanges, or DEXs, are decentralized platforms enabling direct cryptocurrency trading from users' wallets. Users retain control of their private keys, enhancing security and privacy. These exchanges offer features like shielded transactions for confidentiality and operate on trustless principles through smart contracts. They play a key role in the DeFi ecosystem, though they might face challenges like liquidity concerns. Non-custodial exchanges offer a decentralized, secure, and private way to trade cryptocurrencies globally.




Non-custodial exchanges offer an alternative trading experience that aligns with the principles of cryptocurrencies. While they bring advantages in terms of security, privacy, and control, users should assess their risk tolerance and familiarity with the technology before engaging in trading on these platforms.

---

