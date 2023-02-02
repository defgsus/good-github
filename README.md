## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-02-01](docs/good-messages/2023/2023-02-01.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,231,423 were push events containing 3,459,291 commit messages that amount to 290,618,699 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 55 messages:


## [Buildstarted/linksfordevs](https://github.com/Buildstarted/linksfordevs)@[af5fa5dcaf...](https://github.com/Buildstarted/linksfordevs/commit/af5fa5dcaf61e9477efdfa3cf6aaabc70bd27e47)
#### Wednesday 2023-02-01 00:07:14 by Ben Dornis

Updating: 2/1/2023 12:00:00 AM

 1. Added: tools for finding information on the internet
    (https://roman.computer/finding_information/)
 2. Added: Various Ways of Sending Mail via SMTP
    (https://blog.bityard.net/articles/2023/January/various-ways-of-sending-mail-via-smtp)
 3. Added: The Product-Led Trap
    (https://e-baumer.github.io/2023-01-30-product-led/)
 4. Added: My first recession
    (https://gadi.fm/posts/recession/)
 5. Added: Using platforms encourages internet censorship
    (https://worldofmatthew.com/technology/fuckplatforms/)
 6. Added: Five years
    (https://i.jagad.me/five-years/)
 7. Added: Preparing Fastify for Testing
    (https://hire.jonasgalvez.com.br/2023/jan/31/fastify-testing/)
 8. Added: ...so, I joined the time-complexity cult.
    (https://fyi.birnadine.guru/so-i-joined-the-time-complexity-cult)
 9. Added: Automating the Addition of New Jekyll Post Files
    (https://anderegg.ca/2023/01/31/automating-adding-new-jekyll-post-files)
10. Added: Tools for Thought's greatest benefit
    (https://www.dsebastien.net/tools-for-thought-greatest-benefit/)
11. Added: GPT-3 generated Hacker News summaries in the style of n-gate.com - AILEF
    (https://ailef.tech/2023/01/31/gpt-3-generated-hacker-news-summaries-in-the-style-of-n-gate-com/)
12. Added: The Best GPUs for Deep Learning in 2023 — An In-depth Analysis
    (https://timdettmers.com/2023/01/30/which-gpu-for-deep-learning/)

Generation took: 00:06:22.4452765

---
## [tabulon-ext/inn](https://github.com/tabulon-ext/inn)@[4fe713d0e5...](https://github.com/tabulon-ext/inn/commit/4fe713d0e57c42b993f6c0915baad355ff43c269)
#### Wednesday 2023-02-01 00:48:50 by Julien ÉLIE

Fix the use of Auto-Submitted header field

Use auto-generated for controlchan reports, and do not use that header
field at all for gatewaying (news2mail and nnrpd).

Thanks, Russ Allbery, for your wise thoughts:

The notifications sent by controlchan are not an autoreply to the
sender of the control message.  They are a status report sent to the
news administrator about a change made (or proposed) on their news
server by a third party.  As such, they're equivalent to the daily
report or the notification messages from innwatch.  The fact that the
change to the server was initiated by a netnews message doesn't feel
horribly relevant.  A "reply" by definition goes back to the sender
of the message; notification messages that go to third parties feel
inherently different.

Gatewaying (of which moderation is a subset) is yet a different thing,
and the Auto-Submitted header isn't appropriate here with any value.
These messages are not Auto-Submitted; they're, well, gatewayed.
This is equivalent to email forwarding; mail servers don't add
Auto-Submitted headers when they forward mails.

*If* we were encapsulating messages when sending them to moderators,
"Auto-Submitted: auto-generated" may be in the outer envelope, but
since we're transforming and forwarding a message, this is just part
of the message propagation path and thus should not be labeled with
Auto-Submitted.  The message is not, in general, auto-submitted; it was
manually posted by the poster of the message, and we're just passing it
along to its ultimate recipient.

Also, on a more practical level, addition of this header is
potentially surprising to moderators.  Their mail client may rightfully
downgrade or refile messages with Auto-Submitted headers, particularly
Auto-Submitted: auto-replied, since the vast majority of such messages
are vacation auto-replies that are of low importance or that people may
even auto-delete.  There's some risk of confusing submitted posts for a
moderated group, which are relatively important mail, for relatively
unimportant mail like vacation autoreplies or automated status
messages.

see #255

---
## [OpenVZ/vzkernel](https://github.com/OpenVZ/vzkernel)@[4068407541...](https://github.com/OpenVZ/vzkernel/commit/4068407541378dc108dc2dbe5f697a7a3a0ef4c4)
#### Wednesday 2023-02-01 00:50:45 by Vladimir Davydov

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
## [swbs-co/odoo](https://github.com/swbs-co/odoo)@[8f24aba86f...](https://github.com/swbs-co/odoo/commit/8f24aba86faf2639109b56887781b0daaf60be98)
#### Wednesday 2023-02-01 01:00:37 by Romain Derie

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

closes odoo/odoo#111400

X-original-commit: 639cfc76ba259eea8f38284192017024809173b3
Signed-off-by: Quentin Smetz (qsm) <qsm@odoo.com>
Signed-off-by: Romain Derie (rde) <rde@odoo.com>

---
## [userdansilva/JavaCourse-ControlFlow](https://github.com/userdansilva/JavaCourse-ControlFlow)@[ebf787d50e...](https://github.com/userdansilva/JavaCourse-ControlFlow/commit/ebf787d50e7ea039be16b323843e5201a038e2a0)
#### Wednesday 2023-02-01 01:07:38 by Daniel Silva

Challenge NumberPalindrome done! (fuckin love that shit)

---
## [Zeodexic/tsorcRevamp](https://github.com/Zeodexic/tsorcRevamp)@[68e596932c...](https://github.com/Zeodexic/tsorcRevamp/commit/68e596932ce58908ce2652dc7a1fa54dffe1e20a)
#### Wednesday 2023-02-01 01:09:10 by Zeodexic

resizable soapstones

also they cant be runes any more because i hate my life

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[1e03896fbb...](https://github.com/treckstar/yolo-octo-hipster/commit/1e03896fbb078546252ebd5e4c97a73ea8eee779)
#### Wednesday 2023-02-01 01:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [deathandmayhem/jolly-roger](https://github.com/deathandmayhem/jolly-roger)@[0cf9d49b73...](https://github.com/deathandmayhem/jolly-roger/commit/0cf9d49b73d60de455fd2f363ec289f810a8f823)
#### Wednesday 2023-02-01 01:22:20 by Evan Broder

Introduce infrastructure for Zod-based schemas

This is a new system for defining database schemas which exist both at
the type layer and the runtime layer. Instead of using io-ts to define
the type layer and compiling that into SimpleSchema (which enforces the
runtime layer), we instead use Zod to define schemas and compile them
into JSON Schema, which we can then attach directly to the Mongo
database to enforce the runtime behavior.

Zod represents an improvement for our use cases over io-ts in a few
ways:
- Its syntax for expressing optional types is much more concise (no more
  `t.union([t.string, t.undefined])`)
- It allows expressing additional non-purely-type constraints, such as
  regex matches or lengths (which we previously expressed in Overrides)
- It is somewhat more pleasant to metaprogram over at runtime (e.g. to
  generate JSON Schema)

Meanwhile, JSON Schema is capable of expressing everything we currently
want to support in our schema language (unlike SimpleSchema which can't
support, e.g., tagged unions) and is relatively straightforward to
recursively generate from the Zod schema object (unlike SimpleSchema,
which makes it fairly challenging to express things like nested object
types).

The biggest downside of this approach is that while SimpleSchema comes
with a native understanding of Mongo operations, giving it built-in
support for auto-populating fields (e.g. `createdAt` timestamps) and
standardized transformations on values which worked across different
Mongo operators (e.g. our `answerify` function for uppercasing answers),
JSON Schema supports no runtime transformation, only validation, and Zod
has no understanding of Mongo operations to apply transformations
intelligently.

To work around this, we introduce logic which can take a Zod schema and
manipulate it such that it's possible to use it to transform Mongo
operations. There are three main moving parts to make this work:
1. We have to relax certain constraints on the schema (e.g. a required
   field may not be present in an update operation). This potentially
   means that our runtime validation will allow through an invalid
   operation, but since our primary goal is transformation and not
   validation, that's acceptable. (Ultimately, the JSON schema
   enforcement at Mongo itself ensures validity.) We can do this in
   advance in the `relaxSchema` function.
2. We have to account for Mongo's dot-separated addressing syntax, which
   can put nested fields at the top level of an update operation. To
   account for this, we group the fields of the update operation by
   their top-level key (or lack of key, for non-dot-separated fields).
   For each group, we generate a new schema which represents just that
   sub-object (or array element, etc.), and then apply that schema to
   the group, recursing as necessary. Because we can't enumerate all
   possible ways that nested fields can be addressed (e.g. arrays can be
   indexed with a number), we have to do this at runtime, although that
   should only have cost if we're actually updating a nested field. This
   is handled by `parseMongoOperationAsync` (with assistance from
   `getSchemaForField`)
3. We need to ensure that auto-populated fields are populated at the
   appropriate time (be that insert, upsert, or update). For this, we
   use Meteor's EnvironmentVariables (which are basically variables with
   dynamic scope) to flag what state we're currently in, and then use
   Zod's transform functions to populate fields at the appropriate
   times. We set the insert flag on inserts, the upsert flag when
   generating `$setOnInsert` in an update, and the update flag for the
   `$set` operation in an update. (This is handled sort of all over the
   place, but primarily through cooperation between
   `parseMongoModifierAsync` and `imports/lib/schemas/customTypes.ts`.)

On top of the environment variables, an auto-populated field requires us
to make a distinction between the type that is returned from the
schema's processing and the type that is guaranteed to be present in the
database. Under normal circumstances, the type that is returned from the
schema's processing would be Zod's "output" type (`z.output` or
`z.infer`). However, that type isn't especially useful to us, so we
repurpose the output type to instead represent the type that is
guaranteed to be present in the database. This requires us to, frankly,
lie to Zod and the type system by using transform functions to claim
that certain fields are not nullable, when in fact they are. This
happens in `imports/lib/schemas/customTypes.ts`.

However, we retain the characteristic of Zod that the input type
(`z.input`) represents what the user is obligated to provide, at least
for insertion of a new document. (As outlined above, user obligations
around updates are a bit more...fuzzy.)

(Additionally, because Zod's transformations and other "effects" suffer
from runtime type erasure, we need an additional annotation to generate
the correct JSON schema.)

All of this functionality is wrapped up in a new `Model` class, intended
to replace both the old `Base` class and direct usage of
`Mongo.Collection`. Unlike `Base`, it wraps a Mongo collection, rather
than extending it, giving us more control over the interfaces we choose
to support. For the specific `Base` functionality of supporting
soft-deletion, there's a separate `SoftDeletedModel` class.

Rather than requiring that schemas provided to them hew to a specific
interface, both `Model` and `SoftDeletedModel` add fields (`_id`,
`deleted`) that they require to be present on their schemas. This means
that the Zod schema object can not on its own be used to derive a
model's type, so we instead export a new `ModelType` helper, replacing
the pattern of exporting `t.TypeOf<typeof MySchema>` in the schema file.

`Model` additionally includes a few additional affordances. First of
all, it requires that all string types be non-empty (either via length
constraint or via regex). This is an alternative to SimpleSchema's
default behavior of replacing empty strings with undefined and has the
benefit of being more explicit (and more likely to trip you up if you,
e.g., try to `$set` a field to an empty string). And second, it includes
`AllModels`, making it easier for us to write code which operates on all
models (e.g. for future index management tooling).

There are a few smaller regressions in this approach relative to what we
were doing previously. Specifically:
- This will pull in Zod on the client-side. We might be able to fix that
  by pulling mutation methods out of Model, similar to what we're doing
  with `defineMethod`, but it seems annoying and messy so I'm holding
  off right now. Zod isn't that big, anyway, so the footprint impact
  isn't that bad (around 8KB or so).
- There's no way of expressing `denyInsert` or `denyUpdate`. This seems
  fairly difficult to reintroduce, since it's not expressible in JSON
  schema. I'm not sure how useful these were in practice, so I don't
  feel bad about dropping them.
- `Model` does not preserve our `allow` rules which allow admin clients
  to manipulate state. We could re-introduce them, but since those
  default Meteor methods are defined on the collection (and not our
  `Model`), they would completely bypass transformation and thus be
  somewhat unpredictable. I think that instead of supporting these, we
  should build out an admin UI for manipulating state, which would be
  much more predictable and easier to use.

Finally, we update `publishJoinedQuery` to accept either a
`Mongo.Collection` or a `Model`.

---
## [rpatil524/dagster](https://github.com/rpatil524/dagster)@[84c7e77a81...](https://github.com/rpatil524/dagster/commit/84c7e77a8170aa11b53ef10fda93bc4b33134b1e)
#### Wednesday 2023-02-01 01:39:50 by Ben Gotow

[dagit] Add ErrorBoundary to Dagit to reduce severity of React errors (#11824)

### Summary & Motivation

Corresponding Internal PR:
https://github.com/dagster-io/internal/pull/4659

Hey folks, this PR wraps key components of Dagit in React "error
boundaries", which give us the opportunity to present errors more
gracefully and let users recover / continue to use other parts of the
app. So far I've added them to:

- The top component that renders page content (everything below the
toolbar)
- The details section of the asset partitions and events pages (which
was a production issue yesterday)
- The asset graph and asset graph sidebar
- The op graph and op graph sidebar
- The run logs container and the run gannt chart
- The instance run timeline
- The `<Dialog />` component (errors in a dialog should never take down
the rest of the page)

Anywhere else we should add these?

### Resetting after errors

The component I added takes a `resetErrorOnChange` prop which acts a bit
like a useMemo dependency list -- if any of the values change and it's
in an error state, it resets the error and tries to render it's subtree
again. We need this for cases where the error boundary is not unmounted
/ remounted but it's content could meaningfully change. (eg: you click
another asset or tab). I think this is better than putting a `key={}` on
the Error Boundary because that would force a re-render on the whole
subtree in the happy case.

### Cloud

In cloud dagit, we need to implement a top level context exposed by the
new Error Boundary class in order to send errors (which are now caught)
to DataDog. I think we also want to change the text to let users know
that their errors are automatically submitted to us, so I made that text
configurable. We can also disable the display of the error stack trace
in cloud if we want to.

### How I Tested These Changes

I tested these changes by adding `throw new Error()` to various React
render methods and verifying that Dagit fails more gracefully. I also
verified that this can catch the infinite recursion bug, which is a bit
of an interesting one, by reverting to last night's code and running
without the GraphQL patch.


![image](https://user-images.githubusercontent.com/1037212/213761842-9c01de3e-aa19-40e8-8ea5-2db143684ea6.png)


![image](https://user-images.githubusercontent.com/1037212/213762126-e94f2f8e-1a82-4d71-b624-525533c34d28.png)

Edit: Updated styling

<img width="727" alt="image"
src="https://user-images.githubusercontent.com/1037212/213804637-46343cb0-34de-4154-bd5e-1f61d0a30e92.png">

Co-authored-by: bengotow <bgotow@elementl.com>

---
## [Warhand/Limitless-rebirth-1.18.2](https://github.com/Warhand/Limitless-rebirth-1.18.2)@[90661c6194...](https://github.com/Warhand/Limitless-rebirth-1.18.2/commit/90661c6194203aba0b9231bca135aa7a2ac47690)
#### Wednesday 2023-02-01 02:07:18 by Rosie-Holstein

Update Automodlist.txt

Updated:
~Balm
~Creatures and beasts
~Crafttweaker
~Equipment compare
~Integrated dungeons and structures
~Malum
~Numismatic overhaul
~REI

Added:
+pipez
+World stripper (Dev mod, ignore)

Removed:
-Floating islands (Too simple and rather poorly made)
-Additional banners (Ended up deciding against adding this mod.)
-Create crafts and additions (Wasn't a fan of this one, I want one of creates downsides is that its difficult for it to integrate with other tech mods.)
-Duckling (Cute, but unneeded)
-Dungeons plus (Trimming worldgen bloat.)
-Enchantment transfer (Trivializes obtaining enchants)
-JSTF (I honestly can't tell which mod this was, I hate when mods use acronyms in their file names...)
-Pretty pipes (Replaced by pipez)
-The graveyard (Decreasing the amount of structures, and also the mobs didn't really mesh with the other mobs in the pack.)

---
## [wegank/nixpkgs](https://github.com/wegank/nixpkgs)@[fc823fe623...](https://github.com/wegank/nixpkgs/commit/fc823fe623040602317e24341da9db60ddbddc22)
#### Wednesday 2023-02-01 02:18:37 by Adam Joseph

stdenv: external gcc bootstrap

#### Immediate Benefits

- Allow `gcc11` on `aarch64`
- No more copying `libgcc_s` out of the bootstrap-files or other
  derivations
- No more [static `lib{mpfr,mpc,gmp,isl}.a`
  hack](https://github.com/NixOS/nixpkgs/blob/2f1948af9c984ebb82dfd618e67dc949755823e2/pkgs/stdenv/linux/default.nix#L380)
- *Zero* additional `gcc` builds (stage1+stage2+stageCompare)
  - The `gcc` derivation builds `gcc` once instead of three times.
  - The libraries that are linked into the final `pkgs.gcc` (`mpfr`,
    `mpc`, `gmp`, `isl`, `glibc`) are built by
    `stdenv.__bootPkgs.gcc` rather than by the `bootstrapFiles`.  No
    more Frankenstein compiler!
  - stageCompare runs **concurrently** with (not in series with)
    with `stdenv`'s dependees.
- Many other `stdenv` hacks eliminated.
  - `gcc` and `clang` share the same codepath for more of
    `cc-wrapper`.
  - Makes the cross and native codepaths much more similar --
    another step towards "cross by default".

Note that *all* the changes in this PR are controlled by flags; no
old codepaths need to be removed until/if we're completely certain
that this is the right way to go.

#### Future Benefits

- This should allow using a [foreign] `bootstrap-files` so long as
  `hostPlatform.canExecute bootstrapFiles`.
- There will be an "avalanche of simplification" when we set
  `enableGccExternalBootstrap=true` and run dead code elimination.
  It's really quite a huge amount of code that goes away.
  Native-gcc has its own special codepath in so many places, while
  cross-gcc and clang work the same way (and are much simpler).
- This should allow each of the libraries that ship with `gcc`
  (`lib{backtrace,atomic,cc1,decnumber,ffi,gomp,iberty,offloadatomic,quadmath,sanitizer,ssp,stdc++-v3,vtv}`)
  to be built in separate (one-liner) derivations which `inherit
  src;` from `gcc`.
  - Building `libstdc++-v3` in a separate derivation will eliminate
    a lot of accidental-reference-to-the-`bootstrapFiles` landmines.

#### Incorporates

- https://github.com/NixOS/nixpkgs/pull/209054
- https://github.com/NixOS/nixpkgs/pull/210004
- https://github.com/NixOS/nixpkgs/pull/36948 (unreverted)
- https://github.com/NixOS/nixpkgs/pull/210325
- https://github.com/NixOS/nixpkgs/pull/210118
- https://github.com/NixOS/nixpkgs/pull/210132
- https://github.com/NixOS/nixpkgs/pull/210109

#### Closes

- Closes https://github.com/NixOS/nixpkgs/issues/208412
- Closes https://github.com/NixOS/nixpkgs/issues/108111
- Closes https://github.com/NixOS/nixpkgs/issues/108305
- Closes https://github.com/NixOS/nixpkgs/issues/201254

#### Build history

- First successful builds (stage1/stage2):
  - powerpc64le-linux at 9c7e9ef256714455914180c0bcb434e014e5b75a
  - x86_64-linux at 9c7e9ef256714455914180c0bcb434e014e5b75a
  - aarch64-linux at 4d5bc7dabfbe1f8758559390e373b91dda9d401e

- First successful comparisons (stageCompare):
  - at 81949cffa3272f8f9bdc8cfda8effb34be517d2f
  - [aarch64-linux][aarch64-compare-ofborg]
  - [x86\_64-linux][amd64-compare-ofborg]

#### Credits

This project was made possible by three important insights, none of
which were mine:

1. @ericson2314 was the first to advocate for this change, and
   probably the first to appreciate its advantages.  External
   bootstrap is "cross by default".

2. @trofi has figured out a lot about how to get gcc to not mix up
   the copy of `libstdc++` that it depends on with the copy that it
   builds.  Now that gcc is written in C++, it depends on
   `libstdc++`, builds a copy of `libstdc++`, and builds auxiliary
   products (like `libplugin`) which depend on `libstdc++`.  @trofi
   developed two important techniques for keeping this straight: the
   use of a [nonexistent sysroot] and moving the `bootstrapFiles`'
   `libstdc++` into a [versioned directory].  Without these two
   discoveries, external bootstrap would be impossible, because the
   final gcc would still have references to the `bootstrapFiles`.

3. Using the undocumented variable [`user-defined-trusted-dirs`]
   when building glibc.  When glibc `dlopen()`s `libgcc_s.so`, it
   uses a completely different and totally special set of rules for
   finding `libgcc_s.so`.  This trick is the only way we can put
   `libgcc_s.so` in its own separate outpath without creating
   circular dependencies or dependencies on the bootstrapFiles.  I
   would never have guessed to use this (or that it existed!) if it
   were not for a [comment in guix] which @Mic92 [mentioned].

My own role in this PR was basically: being available to go on a
coding binge at an opportune moment, so we wouldn't waste a
[crisis].

[aarch64-compare-ofborg]: https://github.com/NixOS/nixpkgs/pull/209870/checks?check_run_id=10662822938
[amd64-compare-ofborg]: https://github.com/NixOS/nixpkgs/pull/209870/checks?check_run_id=10662825857
[nonexistent sysroot]: https://github.com/NixOS/nixpkgs/pull/210004
[versioned directory]: https://github.com/NixOS/nixpkgs/pull/209054
[`user-defined-trusted-dirs`]: https://sourceware.org/legacy-ml/libc-help/2013-11/msg00026.html
[comment in guix]: https://github.com/guix-mirror/guix/blob/5e4ec8218142eee8e6e148e787381a5ef891c5b1/gnu/packages/gcc.scm#L253
[mentioned]: https://github.com/NixOS/nixpkgs/pull/210112#issuecomment-1379608483
[crisis]: https://github.com/NixOS/nixpkgs/issues/108305
[foreign]: https://github.com/NixOS/nixpkgs/pull/170857#issuecomment-1170558348

---
## [RandomGamer123/tgstation](https://github.com/RandomGamer123/tgstation)@[cba002fa91...](https://github.com/RandomGamer123/tgstation/commit/cba002fa912f07112fbbedcab330a35e2bffeab7)
#### Wednesday 2023-02-01 02:32:46 by Sol N

converts contraband file into poster file, makes holiday posters work (kind of) (#72131)

## About The Pull Request

The first part of this is just something that bothered me when I was
messing around with something that I will PR in the new year,
contraband.dm and dmi is ONLY posters. There's nothing else in there and
there are plenty of official posters, and if with #71717 we will also
add holiday posters to the mix then I think that its time to retire
contraband and make it poster.

Some small things I did while messing with it was change some variables
that were single letters into actual variable names, but overall this
part of the pr is not a player facing change.

That said, speaking of #71717 I think that it didn't work? Or didn't
work the way that it was supposed to? All of the spawned posters aren't
instances of festive posters, they are instances of normal posters, so
the code on initialize was not doing anything and the only reason the
holiday_none poster was showing up was because of the proc in randomize
spawning the posters in as those other posters. Because it didn't
actually _become_ poster/official/festive it never could do the proc
that turns it into a poster for the holiday that is actually occurring.

But then when I made it work and it turned into the generic posters I
decided that it would be better if instead of 30% of all posters being a
half finished mess, that if there wasn't a holiday poster it just
wouldn't replace them at all. I have poster Ideas and Dreams so I will
try to help with adding to more holiday posters but not in this PR.

What IS in this PR though, is a new traitor poster that appears during
the holidays.

![dreamseeker_MxxBzXIxiy](https://user-images.githubusercontent.com/116288367/208793262-9d4a45dc-f7bb-4208-b3c3-78cb68cf9af5.png)

This is a generic evil holiday poster that will replace normal evil
posters in the evil poster objective, because I agree with #72003 that
it should be a feature.

## Why It's Good For The Game

Contraband file is just posters already, this is easier for people to
find the posters.
I like holiday posters and think that we should have them and add more,
it is a fun easy thing to add to a lot of the microholidays to make them
more visible in addition to the name generation, but I don't want to see
the unfinished holiday poster so I do think that it's better to only
have them spawn if the holiday actually has a poster. Looking forward to
febuary!

## Changelog

:cl:
add: during holidays the spread syndicate propaganda through posters
objective has a chance of spawning evil holiday poster
fix: framework for holiday posters is more functional and modular
code: contraband.dm file and contraband.dmi file are both now poster.dm
and poster.dmi
/:cl:

---
## [RandomGamer123/tgstation](https://github.com/RandomGamer123/tgstation)@[47ec8ecd38...](https://github.com/RandomGamer123/tgstation/commit/47ec8ecd386f028ee8b2697412c89f00c9cd139f)
#### Wednesday 2023-02-01 02:32:46 by Rhials

Adds the Sandstorm random event, directional meteor functionality, space sand. (#71802)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request


![sandstorm](https://user-images.githubusercontent.com/28870487/206070641-80d37afc-a365-4f5e-ad48-e8cdf0153ac9.png)

Hey guys, it's your boy. Back at it again with another meteor-adjacent
event PR.

Adds the Sandstorm random event, inspired by the long-unused admin only
one. It picks a direction to approach from, alerts the crew of its
imminent arrival, and after a little over a minute of preparatory time,
sends waves of sand and dust to grind down everything in that direction.

To accomplish this, some minor adjustments had to be made to meteor
generation code. They can now be passed an optional arg for a direction
to be thrown from, and will pick a random one if no direction is given.

Also introduces the newest addition to our cast of meteors -- space
sand! It's even weaker than space dust, and shows up exclusively in this
event. Space sand is **ineffective against rwalls**, and will not damage
the arrivals area's high-tech sand-resistant glass. This is to prevent
this event from venting one of the most dust-vulnerable areas on the
station, and to make sure new players aren't shafted into firelock hell
when the right angle is picked.

I did a lot of testing and tweaking of numbers to get the damage to
average at about the level I'm comfortable with. This is meant to be a
high-impact event that isn't as destructive (or unavoidable) as a meteor
wave. Speaking of avoidance, let's talk about mitigation:

You get an early warning and a direction the sand will come from. You
have time to grab repair supplies, move to safety, get a MODsuit. You
can make worthwhile repairs as the sand comes in from inside (or
outside, if you're brave enough) with nothing more than a welder and
iron sheets. If you're feeling particularly spicy, you can leverage your
prep time setting up shield generators, which spawn in engineering and
have been added to the maintenance machines loot pool. Anyone can
contribute, so do your part as a good crewmate and help out!

All that being said, the event can't be prevented entirely. Shit's going
to get shredded, especially on the outside of the station. Damage will
vary heavily based on the station and direction, ranging from
inconsequential to threatening. It should happen late enough into the
round that, at the bare minimum, the crew shouldn't be caught
unprepared.

For those of you who are worried, the ORIGINAL sandstorm admin event is
still with us too. It's been moved from the space dust file into the
Sandstorm event file. This PR also makes a very minor change to the
naming of the space _dust_ events, for better menuing.

So, to sum it all up: Sand hits grinds down one side of the station, you
get a minute of warning, shield generators now spawn in maintenance. Be
a good crewmate and help where you can.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

More event variety is good, and events that give the players agency on
how bad the impact will be is even better.

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

:cl: Rhials
add: Sandstorm random event! A random side of the station is pummeled by
an onslaught of sand and dust. If you hear that one is approaching, grab
a welder and some iron to help with repairs!
add: Space sand! It's weak and doesn't hurt reinforced walls, but
shouldn't be underestimated in high quantities.
code: You can now pass a start direction to the
spawn_meteors/spawn_meteor global procs.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [gadget-inc/dateilager](https://github.com/gadget-inc/dateilager)@[4348da1c34...](https://github.com/gadget-inc/dateilager/commit/4348da1c3488187e0d209ebd89a69ffa5adad753)
#### Wednesday 2023-02-01 03:32:16 by Harry Brundage

Recover from arbitrary errors writing files by removing the thing we're about to write

I encountered a sequence of changes that DL didn't expect where I was creating a symlink at a path that was previously a folder full of files. There's a bunch of other annoying cases like this, where we should be able to go from any state on disk to any new incoming object type. The existing strategy did a bit of checking to see if stuff wasn't quite right, but I think we aught to be a bit more robust. The recovery strategy is always the same if we have a new incoming object: delete whatever is there so we can just write the new thing on top. If we're gonna do that, I think we can do it a bit more blindly. Instead of checking ahead of time for erroneous conditions (which also requires another syscall every write), we just blindly try to do the thing we need to do, and if it fails, remove whatever is there and try again. That way, we don't need to anticipate whatever fucked up case is on disk at the time and instead just blow it away. I also like this because it makes the fast path a bit faster where we do less checking up front and just let the kernel tell us we're doing something weird.

---
## [ArtemisStation/artemis-tg](https://github.com/ArtemisStation/artemis-tg)@[a47afd9051...](https://github.com/ArtemisStation/artemis-tg/commit/a47afd905156bcc9a070db015cec7b1d1a07c578)
#### Wednesday 2023-02-01 03:37:23 by Sol N

2 New Positive Quirks! (#72912)

## About The Pull Request

I added a few quirks to a downstream that I feel fit well with tg so
here they are.

First up is Poster Boy, a quirk that gives you three mood altering
posters, similar to the traitor objective to hang up demoralizing
posters. You spawn with a box that has one poster that will uplift the
entire crews spirits and 2 that are unique to your department. Captain
counts for security and assistants get only neutral posters. Finally,
with a crayon or spraycan, if you are any antagonist you can make your
poster into one of the ones from the traitor objective.

![dreamseeker_nRy44SL9Jb](https://user-images.githubusercontent.com/116288367/214109008-6f1b4b7c-e800-4142-be6d-926a8e975973.png)
example of quirk posters
Costs 4.


Finally, the characterful Throwing Arm quirk, which lets you throw
objects further (but not harder) and means you will never miss shots
into the disposals bin.
Costs 7.

previously i had a food subscription quirk here as well but i pulled it
out and plan to re-add it as a separate PR in march, where it will now
give you ingredients to cook a meal with occasionally.

## Why It's Good For The Game

Positive quirk variety is good and fun, I think that these positive
quirks are reasonable ones that offer unique things that the current
positive quirks do not.
Poster boy gives people a reason to run around and claim wall real
estate for their department and hopefully can build more solidarity in
departments, the hidden antag feature probably has uses but is just for
styling on people.
Throwing arm offers a fun character trait that probably can have some
slight uses and encourages the use of throwing weapons and tools more.
Also it is good to have a way to never miss the disposals bin. It's so
embarrassing.

## Changelog
:cl:
add: Poster boy and Throwing arm positive quirks.
imageadd: added posters for poster boy quirk
/:cl:

---
## [RanTranslations/packages_apps_Settings-yaap](https://github.com/RanTranslations/packages_apps_Settings-yaap)@[6a3b66de67...](https://github.com/RanTranslations/packages_apps_Settings-yaap/commit/6a3b66de676ae108aa32dd754cccaf77e25cf347)
#### Wednesday 2023-02-01 04:06:59 by Ido Ben-Hur

Settings: Refactor and clean connectivity check preference

wow this was just horrible...

Made this preference way more maintainable and runtime effective:
* Declare the preference in xml instead of hardcoding - this makes it searchable, more maintainable and is also better runtime wise
* Use arrays instead of manually naming each URL
* Use an ArrayList to handle index <-> setting relationship more easily
* Use static imports instead of literal calls
* Actually handle cases of non availability
* There is absolutely no reason to handle OnResume here
* Get rid of useless functions
* Get rid of useless imports
* Move resources to the proper custom files so we don't confuse translators
* More, too lazy. Don't write shit code please. Thank you.

---
## [ii02735/pokemon-showdown-coupcritique](https://github.com/ii02735/pokemon-showdown-coupcritique)@[5cbb317a4c...](https://github.com/ii02735/pokemon-showdown-coupcritique/commit/5cbb317a4c62a59351010c006be62b37e2a029e2)
#### Wednesday 2023-02-01 05:59:45 by sexy90gxebattlefactoryplayer

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
## [MandyIGuess/MandyIGuess.github.io](https://github.com/MandyIGuess/MandyIGuess.github.io)@[07f303b5cc...](https://github.com/MandyIGuess/MandyIGuess.github.io/commit/07f303b5cc1991ccf836a895b4fb62065a37db1b)
#### Wednesday 2023-02-01 07:03:23 by MandyIGuess

Why the fuck would she care about some stupid joke???

---
## [Cass-Bitchcoin/fulpstationfork](https://github.com/Cass-Bitchcoin/fulpstationfork)@[ca0fedc60f...](https://github.com/Cass-Bitchcoin/fulpstationfork/commit/ca0fedc60f17f19520b8fa064c396129ad68b633)
#### Wednesday 2023-02-01 07:04:15 by John Willard

Sol is now a Subsystem, Coffins lock themselves, Bloodsuckers don't constantly die, probably (#862)

* Turns Sol into a Subsystem & Many more

Turns Sol into a subsystem and hooks Bloodsuckers onto it via signals instead of doing a ton of for() loops anywhere. This made Sol incredibly fucking fast, so I halved the speed so it only ticks every 2 seconds.

I also improved the sunlight hud to update with regular bloodsucker updates to avoid some useless proc overhead and fixed Coffins not locking by themselves.

* Torpor now ends, moves exiting torpor to its proper place

* round it

* fix comment

* fix CI

---
## [shlomenu/program_synthesizing_networks](https://github.com/shlomenu/program_synthesizing_networks)@[31abaef0c4...](https://github.com/shlomenu/program_synthesizing_networks/commit/31abaef0c4fd1aed493a80d2f589a6ba46d3e5c0)
#### Wednesday 2023-02-01 07:25:14 by Eli Whitehouse

minor bug fixes

So far, the removal of fine-grained quantization via `out_codebook` does
not seem to have changed the plateauing accuracies I have experienced up
to this point.  I believe that this is indicative of deeper issues with the
way PSNs have been structured, and that these issues mainly stem from the
desire to quarantine the discrete representation between two stages of
nearest-neighbor quantization.  Previously, I considered this design very
important, as I understood the quantizer to be leveraging the structure of
the discrete representations to upsample a downsampled representation
without circumventing the information bottleneck it created.  Thus it was
important to be able to (approximately) backpropagate around the
quantization unit entirely, and appropriate measures needed to be taken
to ensure that model that mapped between these two stages of quantization
had no incentive to learn an identity function.  However, in the time since
these notions were conceived, my understanding of the purpose of the PSN
has shifted.

In my previous draft of the paper to accompany this code, I was very
focused on the fact that in choosing between courser and finer-grained
nearest-neighbor quantization, one was essentially choosing between more
flexible discrete structure and more flexible continuous structure in
the representation.  I think my underlying intuition was that neural
networks were probably not making much use of the discrete structure
that was created by nearest-neighbor quantization.  Indeed, the
dimensionalities typically used for VQ-VAE-descended architectures
suggest that the goal is generally to be so fine that the discrete
information available is too subtle and voluminous to be of much use.
I think I believed that if one used a courser quantization, then mapped
this choice onto another discrete representation that was then forcibly
"injected" into the intermediate representation, one could achieve the
same result as when using a more fine-grained quantization but the
resulting discrete structure would exert more influence over the
geometry of the latent representations developed.  What I didn't realize
is that this basic dynamic of utilizing course-grained quantization
to flexibly realize a categorical choice within a neural network, then
mapping these categorical choices onto more complex discrete structures
which influence the subsequent flow of information does not require
that one be trying to regain the detail accessible with a second, "finer"
quantization.  This notion is one very directly tied to autoencoding
and stems from rather literal parallels drawn with the VQ-VAE.  I think
I also held to the belief that two-stage quantization was crucial
because I didn't realize that there were other ways to backpropagate
to the prequantizer.  In particular, three insights are important:

 - one can transform + pack the quantized output of the prequantizer
   into the nodes of a graph and backpropagate through the GNN, just
   as later GNN layers backpropagate to earlier ones.
 - with this connection, the prequantizer can receive feedback without
   copying gradients from any later stage in the network.
 - if we are not copying gradients back to the prequantizer, we can
   eliminate two stage quantization entirely and simply allow the
   GNN to be trained to succeed on the PSN's overall task.

While the theory accompanying two-stage quantization, as described above,
had a certain elegance, I believe it faced practical difficulties for the
following reason: the discrete representations had to be perfectly designed
to reflect all possibly-relevant distinctions among model inputs prior to
PSN training, as the quarantining of the submodel that processed the discrete
representations meant that the prequantizer had no feedback on which discrete
representation was most beneficial for prediction which was truly independent
of the current and recent states of the entire model's parameters.  The GNN
was only incentivized to map to arbitrary `out_codeboook` vectors precisely.
Since it had no idea of the current vector representation of any given graph
according to `in_codebook`, its understanding of how to do this depended
entirely on random initialization and previous values of `out_codebook`,
which themselves depended on random initialization, previous GNN outputs,
and previous prequantizer outputs.  The prequantizer's outputs depend on
random initialization, the training data, and the copied gradients
resulting from two-stage quantization.  The influences are cyclical.  The
only forces for greater representativeness/relevance of the codebooks is
the inherent tendency of the prequantizer's output to contain information
about the training data, and the presumed relevance of at least some of
this information about the training data to the PSN's final prediction.
However, for the prequantizer's preservation of _appropriate_ information
to be rewarded, the GNN would already have to know how to interpret the
corresponding (uninformative) graph, and would have to be trained to mimic
an extant `out_codebook` vector that already contains this useful information.

Over time, the `out_codebook` will necessarily be moved closed to prequantizer
outputs, which reflect the training data.  And this will be rewarded to the
extent that the information reflected therein is relevant to the prediction
task and is amenable to being inferred from the discrete representations
currently available.  Hypothetically, this synergy meant that how the PSN
functioned (and the discrete representations it tended to utilize) reflected
which discrete representations best represented the training data for the
purpose of yielding accurate downstream predictions.  However, I don't
think the resulting feedback to the program synthesis subsystem, as measured
by the PSN, was particularly sensitive or accurate.  I also think it was
unsuited to its express purpose: to guide the discovery of more discrete
representations. This is because as it stands, the synergy I've described
arises from identifying discrete representations with continuous
representations of training data, a task which is wholly altered each time
a new discrete representation is discovered.  The results of trying to find
this synergy--its overall success and its indications of relevance for
particular discrete representations--are contingent on all of the other
discrete representations present and are significantly complicated by the
ever increasing number of such representations.  These are the inherent
pitfalls of a system designed around identifying one set of representations
with another.

The alternative, which I've already outlined technically, is to understand
the discrete representations simply as shaping the way the model's ultimate
answer is computed.  This goal does not require that discrete structure
stand in for continuous information--only that it be juxtaposed with it.
In this way it is very similar to noisy quantization, which imposes a
meaning on the discrete indices of the codebook which impacts the way
continous information flows through the rest of the network.  The only
purpose is to make the various categorical choices (which the neural
network would otherwise have a hard time meaningfully differentiating)
exhibit more substantively different behavior, so that even for different
values of the same codebook vector there is something common and
meaningfully similar about the resulting behavior.  However unlike in
noisy quantization where the structure is fixed in advance, here it's
much more general.  And because the GNN is able to see the continuous
information that caused it to be selected, and has direct feedback
on the utility of its contributions to the downstream prediction
task, it has the resources to utilize the continuous information
provided by the prequantizer in the most helpful way it can for
each possible discrete representation.  The ultimate goal of the PSN--
easier, breezier generalization--is simply a byproduct of the sparsity
created by quantizing in correspondence with these discrete representations
at all.

In anticipation of changes in line with the above stated goals, a number
of bug fixes are being committed so as to checkpoint the current version
of the code.  These include:

 - fix various broken calls from API changes
 - enforce that by passing an empty frontier to `GraphQuantizer.explore`
   you are specifically requesting uniform distributional search
   (i.e. breadth-first search)
 - the mechanism for selecting 2d positional embeddings was not functioning
   properly, as it appears the previous attempt at multidimensional indexing
   was not working as expected; this was fixed by using calls to `torch.gather`.

---
## [wmcentire/UnityDev](https://github.com/wmcentire/UnityDev)@[60894e410a...](https://github.com/wmcentire/UnityDev/commit/60894e410a70dc5d0153f7730a6cc3dec400fb24)
#### Wednesday 2023-02-01 07:44:17 by wmcentire

2/1/2023
added win game
made level almost done
fucking hate this game god damn

---
## [ChairriaKatie/WebTest1.github.io](https://github.com/ChairriaKatie/WebTest1.github.io)@[b73e291a3b...](https://github.com/ChairriaKatie/WebTest1.github.io/commit/b73e291a3ba4b402d31d88580043dd98866cd8c7)
#### Wednesday 2023-02-01 08:44:11 by Chairria Katie

Merge pull request #2 from ChairriaKatie/master

fuck you 1

---
## [ValereMagister/MagisterStation](https://github.com/ValereMagister/MagisterStation)@[8eb9d376b5...](https://github.com/ValereMagister/MagisterStation/commit/8eb9d376b50ed6eab29c4c884d7bc3c53aa33fec)
#### Wednesday 2023-02-01 09:46:05 by san7890

Improves/Abstracts Suicide A Bit More (#72949)

## About The Pull Request

Basically all of the heavy lifting was done in #72919, but we do a few
key things here that I wasn't able to do then because it was just
fucking massive.

Player Facing Changes:
* hear_blind arg is now a default state and must be specifically
overridden. Pretty much every mob that wasn't a pAI or alien was lacking
this, so let's toss it in as a default now. Let me know if the generic
message I put in for /mob/living sucks and we can go from there.

Code Side Changes:
* suicide.dm now only contains code pertinent to the suicide verb, and
all subtype proc-overrides have been moved to an appropriate file
pertinent to that subtype.
* suicide.dm has also been organized a bit more to aid the previous
change.
* There is only one suicide verb now, implemented on /mob/living. All
the verb does is invoke the handle_suicide() proc, which does all of the
lifting.
* Leaning into *mumble mumble* object-oriented philosophy, the message
we send to the world on suicide is handled on subtype procs, rather than
be in the huge fuck-off message tree I implemented in the earlier PR. It
definitely makes the visible_message() proc not hard to read IMO. This
also means that we can take up a less footprint when we re-use certain
suicide messages (i.e. Silicon), which is nifty too.

i'm probably forgetting something but that's all of the big ones
## Why It's Good For The Game

There is now a very, very common framework for how suicide works across
all living mobs, and it's much easier to override how suicide is
handled. Certain subtypes do their own bullshit thing, but it's quite
easy to account for this on that case-by-case basis. The overall code
takes up a much less footprint that just makes it look nicer.
## Changelog
:cl:
qol: Some mob suicides now have a message that shows to blind people or
people that didn't actually witness the suicide, pretty cool.
/:cl:

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[74144f2bc9...](https://github.com/tgstation/tgstation/commit/74144f2bc9e69c9829339a1bd7ffa962e37c0cd0)
#### Wednesday 2023-02-01 09:46:19 by LemonInTheDark

Fixes some runtime spam from lazyloading/map templates (#73037)

## About The Pull Request

Ensures we don't try and rebuild loading turfs midload

Turf refs persist through destroy, so when we changeturf earlier to get
our turf reservation, we insert our space turfs into the rebuild queue,
and then end up here where we can be rebuilt randomly, midload, with
uninit'd turfs

Avoids starting atmos machine processing until init

This avoids some runtimes with null gasmixtures

There's still trouble with atmos and template loading, pipes start
processing before their pipelines exist, so we just kinda get fucked.
Need to look into this more deeply, it involves pulling this stuff off
`on_construct` and `setup_template_machinery` and throwing it in maybe
late init, which I don't really relish but will just have to do
eventually.

## Why It's Good For The Game

Reduces runtime spam

---
## [embedvr/Terrace-Dashboard](https://github.com/embedvr/Terrace-Dashboard)@[b2099d29eb...](https://github.com/embedvr/Terrace-Dashboard/commit/b2099d29eb801adc73f6fcc97a5dcdb3cfece8ec)
#### Wednesday 2023-02-01 10:17:42 by Brydon L

[~] fuck you git stop asking me to do stupid stuff

---
## [embedvr/Terrace-Dashboard](https://github.com/embedvr/Terrace-Dashboard)@[d98d55ce81...](https://github.com/embedvr/Terrace-Dashboard/commit/d98d55ce81c43d36ad067fff9d358311898de046)
#### Wednesday 2023-02-01 10:19:54 by Brydon L

Revert "[~] fuck you git"

This reverts commit 70b5c7ebaf2115401387702d0915bb3ac3a4ef01.

---
## [embedvr/Terrace-Dashboard](https://github.com/embedvr/Terrace-Dashboard)@[5486a8db7d...](https://github.com/embedvr/Terrace-Dashboard/commit/5486a8db7dc9f5f316f4dbc21905aa32f2ba23d1)
#### Wednesday 2023-02-01 10:19:54 by Brydon L

Revert "Revert "[~] fuck you git""

This reverts commit d98d55ce81c43d36ad067fff9d358311898de046.

---
## [embedvr/Terrace-Dashboard](https://github.com/embedvr/Terrace-Dashboard)@[7e9bbc1654...](https://github.com/embedvr/Terrace-Dashboard/commit/7e9bbc16541af22c2489bcec3decf6b2acc7e420)
#### Wednesday 2023-02-01 10:19:54 by Brydon L

Revert "Revert "Revert "[~] fuck you git"""

This reverts commit 5486a8db7dc9f5f316f4dbc21905aa32f2ba23d1.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[38d45c561f...](https://github.com/mrakgr/The-Spiral-Language/commit/38d45c561f416ddfa5d9cd16ce79fec81d109d24)
#### Wednesday 2023-02-01 10:42:26 by Marko Grdinić

"https://phys.org/news/2023-01-superconductivity-magic-angle-graphene.html

At some point these fundamental discoveries are going to translate into concrete gains.

9:20pm. https://mangadex.org/chapter/da7a9c90-88cb-444b-a5da-2eb90b1c1b35/25

The mecha and the machinery in Rebuild World are so good. If somebody told me they were made in a CAD program like Moi before being brought in, I'd believe them.

10pm. https://boards.4channel.org/g/thread/91252276/voice-synthesis-general-13-what-a-shock-its-at

Oh take a look at this.

///

https://beta.elevenlabs.io/

>What's this?
A new service that allows you to synthesize voices of anyone if you have some clean audio samples. WARNING: DEVS ARE QUICKLY ADDING FILTERS AND/OR REMOVING FREE TIER, ENJOY WHILE YOU CAN!
Examples:
Amy Rose browbeats you: https://files.catbox.moe/ybsu10.mp3
AVGN browses 4chan: https://vocaroo.com/1ln3Zz0dp6Hw
The Truth: https://voca.ro/1jT5eRn5VZZx

>How to?
Guide: https://rentry.org/AIVoiceStuff

>How to find clean audio samples:
>singers
Some useful search terms: "lead vocals", "vocal stems", "acapella"
>non-singers
Look for speeches and other recordings without any background music or noise. Isolated recordings of video game characters are all over youtube.

>How to remove background noise?
https://lalal.ai/
https://vocalremover.org/
https://github.com/Anjok07/ultimatevocalremovergui/releases/tag/v5.5.0

>I got "Unusual activity detected: blah blah blah"
Spoof your router MAC address and reboot your modem to get a fresh IP, look into cheap resi proxies if you don't have a dynamic IP. Make a new burner email, mailinator currently works well. Clear all cookies or run in incognito mode, ideally in a different browser.

>How can I contribute?
If you get a good result upload the samples to catbox alongside a link to the example vocaroo and repostan will add it to the rentry. We should milk as many outputs as we can while preserving token count.
Template:
Character Name [Series]
Example: link_to_mp3
Samples: link_to_mp3
Notes: Put any notes about voice settings (stability/clarity) or specific punctuation usage.

>FOSS alternatives
>papers
https://valle-demo.github.io/
https://audioldm.github.io/
>repos
https://github.com/neonbjb/tortoise-tts
(gradio setup for above) https://github.com/Pranjalya/tts-tortoise-gradio
https://github.com/NVIDIA/NeMo
https://github.com/CorentinJ/Real-Time-Voice-Cloning
https://github.com/enhuiz/vall-e

///

I completely missed these threads before.

10:15pm. https://boards.4channel.org/g/thread/91251854/sdg-stable-diffusion-general#p91252188

Holy shit these demonic knights are good.

The regal headwear girls as well. The same goes for albino reds.

2/1/2023

8:35am. Let me check my email. Hmmmm...nothing. I am being nervious for no reason at all.

I need to make up my mind to accept whatever comes. 100k/year, 50k/year, 30k/year. I am worth whatever the market decides.

https://www.reddit.com/r/ProgrammingLanguages/comments/10qeqer/february_2023_monthly_what_are_you_working_on/

I am surprised this got posted 8h ago. Have they started automating this?

Anyway, let me post the review.

///

Long time since I last did this review. I've done plenty of improvements on [Spiral](https://github.com/mrakgr/The-Spiral-Language) like better pattern matching compilation as well as fixing bugs in the type inferencer and the ref counter in the C backend. Most notably, I've done an [UPMEM backend](https://github.com/mrakgr/PIM-Programming-In-Spiral-UPMEM-Demo) so Spiral can finally be used to program a novel kind of hardware. That is its purpose. Sadly, UPMEM doesn't seem to be interested in a high level functional language for their devices. Their loss, but doing the backend for it made me realize that I've recovered some of my taste for programming. It is going to serve as a prototype for all the other backends that are going to come in the future.

For the past year and a half I've been studying 3d [art](https://twitter.com/Ghostlike), as well as doing [writing](https://www.royalroad.com/fiction/57747/simulacrum-heavens-key). But it is really difficult to make it on your own. 600 pages posted on RR, and I only have a single Patron contributing 4E/month. That is not going to go anywhere. So what I am doing now is looking for a job. You can see my [resume here](https://docs.google.com/document/d/1D6roVeWFWkwtSfSRr5ac3utd-qSvTtTgBMIbaQ0ZoTo/edit). I do not suppose any of you here would like to hire me on a remote basis?

Since I've started applying, I want to get better at talking, so I've started doing Youtube videos. What motivates this is partly my interview anxiety, and partly the fact that when I showed Spiral to UPMEM a engineering director asked me for a presentation of all things! So now I am doing a small series on [setting up Stable Diffusion on Paperspace](https://www.youtube.com/playlist?list=PL04PGV4cTuIVGO5ImYTk9wPVmbgdYbe7J). It is actually much harder than I thought it would be. A few days ago to make a 11.5m video, I needed to spend over 5 hours editing it. Those Youtubers with slick presentations make it look much easier than it is.

Besides that I got some interesting news regarding AI hardware. I've been eyeing Tenstorrent for a while, and got an ETA of 6 months until they open source their SDK and allow consumers to program their devices. Out of all the AI hardware companies, Tenstorrent is the most interesting to me as they are making cards that you could slot into your home rig. All the other companies are focusing on the big fish, so I am hoping Tenstorrent will deliver something worth programming in. One of their claims is that their devices will be easier to program than GPUs so I have great expectations. Right now I have a big problem because at the rate things are going I won't be able to afford that hardware when it comes out.

A programmer needs only 3 things to be happy: a better language, a better computer, and lastly a better brain. I have a better language in Spiral, and I want to make sure that I will be able to afford the hardware when it comes out. The last one is impossible - for now.

///

Let me post this.

https://www.reddit.com/r/ProgrammingLanguages/comments/10qeqer/comment/j6r2ll4/?utm_source=share&utm_medium=web2x&context=3

Here it is.

8:55am. I am quite groggy.

First of all, how long have the voice synthesis threads on /g/ been happening? Have I simply missed them or is this new?

https://desuarchive.org/_/search/boards/g.desu.meta/subject/voice%20synthesis%20general/

Oh, it is only a few days old.

I've been thinking during the night. Why don't I do chapter 17 of Heaven's Key on Youtube? With a voice synthesis system, I could do it like a play, and give every character its own voice.

It is absolutely certain that I will never get anywhere on RR now. Oh, right, let me note down the stats.

Total Views : 9,278
Average Views : 169
Pages : 589
Total Comments : 8
Followers : 38
Favorites : 10
Ratings : 8
Reviews : 0

9am. Maybe I simply lack the talent to attract an audience. I need more power.

It feels like whatever I decide to do, I am marked for failure. I thought about it while watching some of those popular Youtubers. They have eloquence, energy and passion. I absolutely cannot come in and act like that.

9:05am. But I can make a machine that acts with confidence and flair. So why not go down this route?

9:10am. I really want to get paid for doing art. It is a matter of my bare survival. The notion that one should just write, and no care about recognition is absurd.

Why not aim and get some new skills? Voice synthesis could be really important. The more I leave to the machines the better off I will be in the long run.

I have my issues and flaws. Acting like a high status person is simple in theory, but it is impossible to do with my subconsciousness not cooperating.

9:15am. Let me chill a bit instead of living in my mind. During the night, I remembered I might have an interview soon and it put me on edge. Even if I remind myself not to get excited until I get an actual offer, I can't fully control my inner self. I have to press down on both my eagerness and pessimism.

No follows I am interested in. I should just get rid of the manga I am not interested in reading out of my feed.

...Let me start editing then. Let's finish this video and then start getting ready for the next one. This next one, I am just going to dub.

10:05am. Holy shit, the ripple deletes are starting to take a while.

10:10am. My rig is not powerful enough to deal with videos much longer than 10m.

10:15am. This is unbearable. I literally cannot work in this right now.

Let me split the file into two.

10:20am. Camtasia is really killing me here. Let me restart it.

11:10am. Finally done with pt1. Let me export this shit. This is too much effort!

Now it is rendering. I am not going to get better at talking like this. After I upload this...

Actually, let make the thumbnail while that is going on. I have no choice, but to do these videos in two parts.

11:25am. https://youtu.be/ZAQ4NdmYyG0
How To Get Models From HuggingFace And CivitAI (Part 1)

Here it is. I am not getting likes or subscribers just yet.

I keep forgetting to ask about them. Directing is not easy at all.

10:30am. The way I program is that I try out something, and adjust it afterwards. Planning everything out ahead of time to perfection is beyond my capabilities.

11:35am. Now what I need to do is start work on part 2.

11:40am. You know what, let me put my advice to use and do a voice over. I'll make the script and recite it instead of just turning on the microphone and recording what comes to mind. I had enough of this shit.

In fact, let me do the chores and have breakfast here."

---
## [jandaX/android_kernel_xiaomi_joyeuse](https://github.com/jandaX/android_kernel_xiaomi_joyeuse)@[e25933ebab...](https://github.com/jandaX/android_kernel_xiaomi_joyeuse/commit/e25933ebabe1bcecb79bf2009bc933a429c4fe3d)
#### Wednesday 2023-02-01 11:24:52 by Peter Zijlstra

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
Change-Id: Idd54334615da4c78698ca8b3b12b514ae9d8360f
Signed-off-by: Alexander Winkowski <dereference23@outlook.com>

---
## [Holoo-1/tgstation](https://github.com/Holoo-1/tgstation)@[e9c87c0acb...](https://github.com/Holoo-1/tgstation/commit/e9c87c0acb15439c8f577bba35c45f51bf03d1aa)
#### Wednesday 2023-02-01 12:12:24 by LemonInTheDark

Starlight Polish (Space is blue!) (#72886)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

Adds support to underlays to realize_overlays
Ensures decals properly handle plane offsets
Fixes space lighting double applying if it's changeturf'd into. this
will be important later
Makes solar vis_contents block emissives as expected
Moves transit tube overlays to update_overlays, adds emissive blockers
to them

#### Adds render steps

An expansion on render_target based emissive blockers. 
They allow us to hijack an object's appearance and draw it somewhere
else, or even modify it, THEN draw it somewhere else.
They chain quite nicely

Fixes shuttles deleting z holder objects

#### Makes space emissive, makes walls and floors block emissives
The core idea here goes like this:
We make space glow, and give its overlays some color

This way, the tile and space parallax remain fullbright, along with
anything that doesn't block emissives, but anything that does block
emissives will instead get shaded the color of starlight

This requires a bit of extra work, see later

This is done automatically with render relays, which now support
specifiying layer and color (Need to make an editor for these one of
these days)

The emissive blocking floor stuff requires making a second render plate
to prevent double scaling

Also adds some new layering defines for lighting, and ensures all turf
lights have a layer. We'll get to this soon

#### Makes things in space blue

We color them the same as starlight, by taking advantage of space being
emissive
This means that things in space that block emissive will block it
correctly and be colored blue by the light overlay, but space itself
will remain fullbright

This does require redefining what always_lit means, but nothing but
cordons use that so it's fineee


#### Makes glass above space glow, and some other stuff

Glass tiles that sit above space will now shine light with matching
color to the glasses color. This includes mat tiles.

Glass tiles (not mat because they have no alpha) also only partially
block emissives.
Adds a new proc that uses render steps to acomplish this, essentially
we're cutting out bits below X alpha and drawing what remains as an
emissive.

#### Modifies partial space showing to support glow

Essentially, alongside displaying space as an underlay, we also display
a light overlay colored like starlight.
That starlight overlay gets masked to only be visible in bits that do
not contain any alpha.

We also mask the turf lighting to not go into bits that have no alpha,
to ensure we get the effect we want.
This is done with that lighting layer thing I mentioned earlier.

#### Makes appearance realization's list output ordered

I want it output in order of overlay, sub overlay suboverlay, next
overlay
Need to use insert for that

## Why It's Good For The Game

Pretty!
Also having space be emissive is a very very good way to test for fucked
emissive blockers (If it's broken why are we even drawing the overlay)
I know for a fact mob blockers on lizards and socks are kinda yorked, I
think there's more

<details>
<summary>
Old
</summary>


![image](https://user-images.githubusercontent.com/58055496/213916157-d4b38aa7-3ab6-42a4-989f-7bfba2dc2cba.png)

![image](https://user-images.githubusercontent.com/58055496/213916077-637fa288-bbee-477d-aded-730d9683477e.png)

![image](https://user-images.githubusercontent.com/58055496/213916088-0657a8a2-5627-48e2-8c4b-870c90ef2072.png)

</details>


<details>
<summary>
New
</summary>


![image](https://user-images.githubusercontent.com/58055496/213916107-2af74e64-1817-4a44-b528-180a9160cb9e.png)

![image](https://user-images.githubusercontent.com/58055496/213916115-5fa36fcc-b988-4ccf-850e-21c26ed463d0.png)

![image](https://user-images.githubusercontent.com/58055496/213916120-6833187d-b12e-42a7-ac4b-63c56deb71e5.png)

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
add: Space now makes things in it starlight faintly blue
fix: Glass floors that display space now properly let space shine
through them, rather then hiding it in the dark
add: Glass floors above space now glow faintly depending on their glass
type
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: Zephyr <12817816+ZephyrTFA@users.noreply.github.com>

---
## [Holoo-1/tgstation](https://github.com/Holoo-1/tgstation)@[51f02b5acc...](https://github.com/Holoo-1/tgstation/commit/51f02b5acc0ee3d042734b8fd4fd2b58ac41f9ab)
#### Wednesday 2023-02-01 12:12:24 by LemonInTheDark

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

Co-authored-by: Time-Green <timkoster1@hotmail.com>

---
## [tanker4390/goonstation](https://github.com/tanker4390/goonstation)@[a02c0a6ff9...](https://github.com/tanker4390/goonstation/commit/a02c0a6ff97eb3057ffbe8aea95edf9f810822d8)
#### Wednesday 2023-02-01 12:18:23 by Xkeeper

emergency api shutoff version 3: holy shit, shut up

---
## [digitalservicebund/ris-backend-service](https://github.com/digitalservicebund/ris-backend-service)@[ffeb3c1998...](https://github.com/digitalservicebund/ris-backend-service/commit/ffeb3c1998da69b4093c280a7cd4ed0b497873e7)
#### Wednesday 2023-02-01 12:57:15 by Thore Strassburg

Chore: add post-commit hook for Talisman

We still have some issues with our Talisman ckecksum updating process.
Every time Talisman detects a potential secret in a file, a human has to
very it is not. Then the hash of the current file content has to be
configured as secure.
As soon as the file gets touched, the hash changes and the checksum in
the configuration is obsolete. The next time Talisman reports a secret
in this file, it will check the hash, detect that is not the configured
one where a human has verified the file last time, and reports an issue.

Talisman checks for secrets in files in two different ways. For commits,
it searches only within the diff of the commit for secrets. If there is
no secret, everything is fine. If it finds a secret, it checks if the
content of the file is marked secure by its hash (which is never the
case for a commit which changes the file). It reports the warning and
the user has to verify the files, update the configured checksum and
update the commit.
The second case is for pre-push. Here is checks all files that have been
touched within all commits that are pushed. But here is checks the whole
file content, not just the diff(s). This means, because any commit that
gets pushed has changed the file content, it automatically invalidates
the configured checksum. But because Talisman checks the full file
again, it also detects the old/already reported potential secrets. But
as the hash is no more the same, it reports the old issues again. In
such a case, the user simply has to update the checksum. But only under
the strong assumption that every potential secret was properly reported
and checked during a pre-commit.
This mechanism of Talisman is a "more secure" one, because it actually
does not rely on a history of always guaranteed security check by every
developer.

Unfortunately it is still not possible to verify the whole file as
staged in a pre-commit. But it is also annoying to have the pre-push
hook failing for this. Especially if more than a single commit gets
pushed. Because then it is hard to update the checksums incrementally
for every file content hash as staged for each commit. This leads to
stupid "talisman-update-commits" and checksum jumps.
The used alternative now is to have a post-commit hook. This hooks
"abuses" Talisman his pre-push functionality to check full files touched
by commits. Just that it now runs only the always just created commit.
This detects checksum changes early on commit basis and allows to update
them immediately to amend the commit correctly without much effort.
As Talisman relies on the default git pre-push hook arguments which are
not existing for a post-commit hook, we have to artificially creating
them. We kinda did so already in our pre-push hook too due to some
Lefthook limitations.
Finally, as this is still "experimental", we keep the pre-push hook too.
If everything works fine, nothing is worse than before. If not, it saves
us and allows us to improve the hooks.

---
## [ss220-space/Skyrat-tg](https://github.com/ss220-space/Skyrat-tg)@[e7dd9219e8...](https://github.com/ss220-space/Skyrat-tg/commit/e7dd9219e872ba0c64ce3eb115b05225398643c2)
#### Wednesday 2023-02-01 12:59:24 by SkyratBot

[MIRROR] Add Croissants & Traitorous Baking Techniques [MDB IGNORE] (#18463)

* Add Croissants & Traitorous Baking Techniques (#72232)

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

* Add Croissants & Traitorous Baking Techniques

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [Korpsian/PARADOGX](https://github.com/Korpsian/PARADOGX)@[dad87b99a1...](https://github.com/Korpsian/PARADOGX/commit/dad87b99a1ebec2b10da9787945f1e7154383d8c)
#### Wednesday 2023-02-01 13:03:40 by Korbinian Maag

Fixed stupid fucking bugs in UIContent (I am sometimes retarded omg)

---
## [ckipp01/mill-github-dependency-graph](https://github.com/ckipp01/mill-github-dependency-graph)@[0e85e8ec7e...](https://github.com/ckipp01/mill-github-dependency-graph/commit/0e85e8ec7e78d13227ebea301433cb2f0ad6c6db)
#### Wednesday 2023-02-01 13:43:49 by Chris Kipp

fix: guard against cyclical dependencies which can cause a stackoverflow

So I don't fully love this solution as it adds to the even more hacks I
need for coursier oddness, but there are situations using deps like you
see in the test here that when you look at the children of the
dependency, it lists itself. Some of them are expected due to different
classifiers, but even one with a classifier will list itself as well as
a dep. This leads to really odd cyclical dependency behavior when you
try to traverse the tree. So to guard against this we do a few
different things:

- we do a better job of not processing children that were already
  processed before
- we filter self out when self is listed as a child
- we also cache lookup to ensure we aren't always going from tree->name
  multiple times as we're iterating.

This will fix
https://github.com/ckipp01/mill-github-dependency-graph/issues/77, but I
think this should probably be addressed upstream. I've created
https://github.com/coursier/coursier/issues/2683 to track this.

Just a NOTE, this still doesn't fix the issues with not having
classifiers shown, but I'll do a follow-up to add those in since it's
not a huge change.

Fixes: https://github.com/ckipp01/mill-github-dependency-graph/issues/77

---
## [Jellirby/HeavenStudio](https://github.com/Jellirby/HeavenStudio)@[54c4899f9d...](https://github.com/Jellirby/HeavenStudio/commit/54c4899f9d31999a946e006c6c9b8235bdc1c778)
#### Wednesday 2023-02-01 14:17:49 by AstrlJelly

Double Date Initialization (#198)

* starting out with double date stuff :D

not even the background is finished
i just wanna get this on my fork so that it's safe

* double date getting more initialized

no animations, one block, nothing actually functions. but the boy is put in place, and the girl is almost put in place! just wanted to merge this with the main branch to play catchy tune

* initialization done!!!!!

gonna fix up the code, see what i can take out, see what i can standardize, see what i need to add. loving this so far, even with all of its annoyances

* ughhhh animation stuff.

this is gonna take me a day or two to even comprehend

Co-authored-by: minenice55 <star.elementa@gmail.com>

---
## [RalphHightower/RalphHightower](https://github.com/RalphHightower/RalphHightower)@[e268a3c9ad...](https://github.com/RalphHightower/RalphHightower/commit/e268a3c9ad6020189be8bd7656f890622a541ae0)
#### Wednesday 2023-02-01 15:49:28 by Ralph Hightower

docs: 2023-01-30 updates (closes #646)

| **January 30, 2023** |
|----|
| [LIVE FEED – ‘Murdaugh Murders’ Trial: Day Six](https://www.fitsnews.com/2023/01/30/live-feed-murdaugh-murders-trial-day-six/)<br>News and notes from South Carolina’s ‘Trial of the Century.’ |
| [Live: Law enforcement witness in Alex Murdaugh double murder trial continues testifying](https://www.postandcourier.com/murdaugh-updates/) |
| [Alex Murdaugh prosecutors reveal last texts before Paul’s phone went silent](https://www.postandcourier.com/murdaugh-updates/alex-murdaugh-prosecutors-reveal-last-texts-before-pauls-phone-went-silent/article_e182384c-a0af-11ed-b71e-47eb33beb2ef.html)|
|WALTERBORO — Paul Murdaugh had been calling and texting his friend on the evening of June 7, 2021, when suddenly the youngest of Alex Murdaugh’s sons stopped responding.<br>Paul and his friend, Rogan Gibson, had been discussing Gibson’s puppy, who was staying at the dog kennels on the Murdaugh’s 1,770-acre hunting estate. Gibson sent a text at 8:49 p.m. asking Paul to photograph the dog’s injured tail so he could ask for a vet’s opinion. Though they had talked on the phone just five minutes earlier, Paul didn’t answer. Gibson tried to call him at 9:10 p.m., then again at 9:29, and 9:42, and 9:57. He texted him “*yo,”* and when he didn’t respond to that either, he called one more time at 10:08. He even texted Paul’s mother, Maggie Murdaugh, asking her to have Paul call him.|
|State prosecutors say Maggie and Paul’s phones had already locked for the final time — both at 8:49 p.m. Just minutes before that, they say, a video places the family patriarch, since-disgraced Hampton attorney Alex Murdaugh, with Maggie and Paul by the kennels. Maggie, 52, and Paul, 22, wouldn’t leave the scene alive. Prosecutors on Jan. 30 showed a jury screenshots of Gibson’s communications with Paul as they continued their quest to prove that Alex Murdaugh brutally shot and killed his wife and son.|
|As Murdaugh’s double murder trial progressed into a second week, the S.C. Attorney General’s Office continued to present new witnesses and evidence. Over the past four days, prosecutors have unveiled a series of seemingly unrelated clues without explaining their significance, allowing jurors and a national viewing audience to wonder where the case is headed next. For example, at one point on Monday, lead prosecutor Creighton Waters elicited testimony that state investigators had rooted through a trash can near the crime scene and found a credit card statement on which someone had circled a $1,021.10 transaction made at Gucci.  But Waters never asked who spent that money, what it was for, who circled the expenditure, or what relevance it has to the case. Then he changed topics and never mentioned it again.|
|Murdaugh’s defense attorneys, however, have been far more direct. They spent the morning of Jan. 30 making the case that Colleton County sheriff’s deputies and State Law Enforcement Division agents contaminated the crime scene and mishandled evidence from the Murdaugh’s Colleton County estate, a hunting property the family called “Moselle.” In cross-examining SLED crime scene technician Melinda Worley, Harpootlian established investigators were unable to identify a number of footprints at the scene, in part because responders had walked all over the area. One bloody footprint in the feed room where Paul was killed turned out to belong to a member of law enforcement, Worley conceded. *“Is that preservation of the scene that your standards require?”* Harpootlian asked. *“Not exactly, no,”* Worley said. *“Not exactly,”* Harpootlian repeated. *“Should police be walking through the scene?”* *“No,”* Worley replied. With Worley on the stand, Harpootlian also floated a theory that Maggie and Paul were killed by two separate shooters. He asked what Worley made of the fact that the shotgun blasts that killed Paul appeared to be fired some distance away from the semiautomatic rifle shots that killed Maggie. *“Doesn’t this indicate to you there were two shooters?”* Harpootlian asked of the state’s ballistics analysis. *“Is it a possibility that there were two shooters?”* Worley suggested that the shooter could have moved after killing Paul and moving on to fire at Maggie. *“One explanation could be that there were two shooters,”* Harpootlian pressed. *“One explanation. Not ‘the’ explanation.”* *“Not the only one,”* Worley replied.|
|In calling their 10th witness, SLED agent Jeff Croft, prosecutors continued to lay the foundation for several key elements of their case.  Croft testified about searching the first-floor “gun room” at the Moselle estate’s main house and finding an arsenal of weaponry there. He and prosecutor Waters unboxed and presented a parade of 12-gauge shotguns and one .300 Blackout semiautomatic assault rifle — which belonged to Murdaugh’s other son, Buster - that SLED agents seized from the Moselle home. Murdaugh defense attorney Jim Griffin objected to the gun show, arguing the guns were irrelevant since none of them were the murder weapons. But Judge Clifton Newman sided with Waters, who argued the presentation was necessary to show the exhaustiveness of the state’s investigation. Croft testified about searching the Moselle grounds and finding spent .300 Blackout shell casings by the gun room’s exterior door and on a shooting range across the street from the house.|
| Later in the trial, an expert witness for the state is expected to testify that those older shells had markings that matched shells found by Maggie’s body, proving she was killed with a Murdaugh family rifle. Prosecutors also lay the groundwork to show Murdaugh lied to investigators about his whereabouts on the night of the slayings. Waters played for the jury a recording of Murdaugh’s June 10, 2021, interview with SLED, his second. Three days after the slayings, Murdaugh allowed investigators to download the contents of his cellphone and answered a battery of politely posed questions, sometimes breaking down into tears and hysterics. Murdaugh told investigators he had gone into his Hampton law office on June 7, 2021, but came home early that day because Paul was coming by. He did not mention that his firm’s chief financial officer confronted him earlier that day about missing legal fees. Murdaugh and his son rode around the property for at least an hour and made plans to replant some sunflowers, Murdaugh said, *“doing things we like to do out there.”* Murdaugh told investigators Maggie joined them for dinner later that evening and then went down to the dog kennels. Murdaugh said he fell asleep while watching TV, but Paul must have joined his mother. He told SLED he never went down to the kennels or saw the two of them again before leaving Moselle shortly after 9 p.m. to visit his ailing mother. *“I stayed in the house,”* Murdaugh said.|
|That recording is a problem for Murdaugh, state prosecutors say, because investigators later unlocked Paul’s phone and found a video on it that places Murdaugh with his wife and son by the dog kennels shortly before they were killed. On that video, which jurors haven’t yet seen, Murdaugh is said to be heard talking with Maggie and Paul about a dog that had taken off with a chicken in its mouth. Murdaugh’s attorneys have described it as a “convivial” conversation, hardly the kind of talk you would expect to precede a pair of violent murders. But explaining to the jury why an innocent man would lie to SLED investigators about his whereabouts is one of the great challenges facing Murdaugh’s defense team in this trial. In his interview with investigators, Murdaugh insisted his relationship with his wife was *“very good.”* *“As good as it could possibly be,”* Murdaugh said. *“I mean, you know we’ve had our issues. But wonderful.”* Murdaugh said he and Maggie *“didn’t really argue,”* except in rare instances about how long the family would stay with her parents when they visited. Then, he began crying hysterically. *“She was a great mother,”* he wailed during testimony. In the interview, investigators brought up the *“traumatic picture”* Murdaugh saw when he came upon the crime scene. He began to whimper. *“It’s just so bad,”* he said. Murdaugh’s next words, utters through sobs, were difficult to make out. Some in the courtroom heard: *“They did him so bad.”* Others heard a possible confession: *“I did him so bad.”* Waters asked Croft what he heard. *“I did him so bad,”* Croft repeated. The courtroom camera panned to Murdaugh, who appeared to mouth to his attorneys: *“That’s not what I said.”* |
| [‘Murdaugh Murders’ Saga: Defense Scores Points](https://www.fitsnews.com/2023/01/30/murdaugh-murders-saga-defense-scores-points/)<br>Alex Murdaugh’s attorneys plant seeds of reasonable doubt …|
|Lead prosecutor Creighton Waters got the state off to a strong start last week, delivering a compelling opening argument and launching the state’s case with a bang with dramatic testimony from the first responders who arrived at the Murdaugh hunting property, known locally as Moselle. In pushing back against the prosecution, Murdaugh’s attorney Dick Harpootlian has consistently advanced a theme of shoddy police work – although prior to Monday, he had very little to work with on that front. On Monday, Harpootlian injected the theory of a “second shooter” into this graphic double homicide – while simultaneously building upon the narrative that law enforcement bungled the crime scene from the beginning.|
|Harpootlian reminded jurors that one of the responding officers left a bloody footprint in the feed room near the body of Paul Murdaugh. He also pointed to first responders traipsing through grassy areas where a shooter may have trailed Maggie Murdaugh. *“They were walking in an area where the perpetrator walked,”* Harpootlian said. *“Walking in the dark!”* Harpootlian also grilled Worley on the angles of .300 blackout shots fired from an AR-15 rifle through the wall of the feed room at the crime scene – including one angle measurement, which was incorrectly recorded into her official report. *“One of the shots fired by the AR was fired from somewhere way up here,”* Harpootlian said, pointing to a poster board based on Worley’s original crime scene sketch. *“The AR was some distance away from the feed room.”* *Does none of this indicate to you that there were two shooters?”* Harpootlian asked Worley. *“Is it conceivable?”* As Harpootlian tried to coax Worley into acknowledging a second shooter was a *“reasonable explanation,”* she pushed back, saying she couldn’t do so because she *“wasn’t there.”* *“None of us were there!”* Harpootlian responded. *“We’re trying to figure out what happened that night, and clearly, one of the explanations is two shooters!”*  Another exchange that saw Harpootlian appear to score points with jurors involved an impression found on the calf of Maggie Murdaugh, which he claimed contained was *“not a naturally occurring pattern.”* *“There was a footwear impression on Maggie’s calf,”* Harpootlian said. Harpootlian pressed Worley on whether or not she should have identified and examined the impression, adding *“once Maggie’s body had been removed, that examination could never be done.”* *“If I had realized … I would have documented it properly,”* Worley acknowledged. A photo of the impression was shown to jurors – but was not made available to media or to the courtroom audience. Jurors seemed to be closely following Harpootlian as he built his *“shoddy police work”* narrative to a climax. *“Do we know what other evidence they may have destroyed?”* Harpootlian asked Worley at one point. *“I have no idea,”* Worley replied. *“No, you don’t,”* Harpootlian responded.|
|Prosecutors reclaimed the momentum shortly before noon on Monday when SLED special agent Jeff Croft took the stand. Croft’s testimony allowed the state to introduce significant firearm and ballistics evidence given his starring role in collecting various guns and ammunition from multiple locations at Moselle. Lead prosecutor Waters walked Croft through the introduction of this evidence. Croft also provided some initial testimony, which touched cell phone evidence, likely to play such a huge role in this case. Specifically, Croft interviewed Rogan Gibson – a friend of Paul Murdaugh’s who was the last person to speak to him prior to his death. Croft testified that Gibson received two incoming phone calls from Murdaugh – one at 8:40 p.m. EDT and another at 8:44 p.m. EDT.
The most damning one? The last time he saw Paul and Maggie alive was when the family ate dinner together in the main house at Moselle. *“Nobody was in that home when I left,”* Murdaugh told SLED special agent David Owen in the video. This is the so-called ironclad alibi that was shredded by a cell phone video taken by Paul Murdaugh just moments before he was murdered. That video – which has not been played for jurors.|
|Jurors also have yet to hear the August 2021 interview with SLED, in which Murdaugh is confronted about his presence a t the kennels. Initially taken aback at the assertion, Murdaugh informed investigators that they were wrong about this key point of information. *“No,”* he told them bluntly. Murdaugh later qualified this denial by saying there was no way he could have been at the kennels at the time the video was filmed *“unless my timeline is wrong.”*|

---
## [Fikou/tgstation](https://github.com/Fikou/tgstation)@[b174af7661...](https://github.com/Fikou/tgstation/commit/b174af7661cbfaf564292caabfccca18619bda23)
#### Wednesday 2023-02-01 16:15:31 by Jacquerel

Basic Mob Carp Part VIII: Basic Mob Carp (#72073)

## About The Pull Request

Wow we're finally here. This turns carp into Basic Mobs instead of
Simple Animals.
They use a variety of behaviours added in previous PRs to act in a
marginally more interesting way than they used to.
But don't worry there's still 2 or 3 PRs to follow this one until I'm
done with space fish.

Changes in this PR:
Carp will try to run away if they get below 50% health, to make use of
their "regenerate if not attacked" component.
Magicarp have different targetting behaviour for spells depending on
their spell;
- Ressurecting Carp will try to ressurect allied mobs.
- Animating Carp will try to animate nearby objects.
- Door-creating Carp will try to turn nearby walls into doors.

You can order Magicarp to cast their spell on something if you happen to
manage to tame one.
The eating element now has support for "getting hurt" when you eat
something. Carp eating can rings and hating it was too soulful not to
continue supporting.

## Why It's Good For The Game

Carp are iconic beasts and I think they should be more interesting.
Also we just want to turn mobs into basic mobs anyway.

## Changelog

:cl:
add: Carp will now run away if their health gets low, meaning they may
have a chance to regenerate.
add: Lia will now fight back if attacked instead of letting herself get
killed, watch out!
balance: Magicarp will now aim their spells more intelligently.
add: Tame Magicarp can be ordered to use their spells on things.
refactor: Carp are now "Basic Mobs" instead of "Simple Mobs"
fix: Dehydrated carp no longer give you a bad feeling when they're your
friend and a good feeling when they're going to attack you.
balance: Tamed carp are now friendly only to their tamer rather than
their whole faction, which should make dehydrated carp more active.
Order them to stay or follow you if you want them to behave around your
friends.
/:cl:

---
## [Fikou/tgstation](https://github.com/Fikou/tgstation)@[125745d232...](https://github.com/Fikou/tgstation/commit/125745d232163406c107d3947b87d6d406ac3a17)
#### Wednesday 2023-02-01 16:15:31 by Fikou

guardian death checks (#72251)

## About The Pull Request
if a guardian summoner is dead during the summoner setting process, we
(the guardian) now kill ourselves since itd mean a guardian that cant
die
to combat some fucked upness of it (if you inject a guardian and it only
spawns after you died and then dusts you), the process of spawning a
guardian from the playerside guardian creator stuff gets canceled if
youre dead or dont exist

## Why It's Good For The Game
yeah that seems good

## Changelog
:cl:
fix: guardian spirits check for death before they add themselves to you
/:cl:

---
## [jaypipes/ack-test-infra](https://github.com/jaypipes/ack-test-infra)@[95e4857b28...](https://github.com/jaypipes/ack-test-infra/commit/95e4857b28122c6c5f8a30260be3dcac94e0e466)
#### Wednesday 2023-02-01 16:23:19 by Amine

Move Go binaries to `/usr/bin` (#287)

Issue https://github.com/aws-controllers-k8s/community/issues/1640

TL;DR: Prow was mounting `test-infra` code volume into `$GOPATH`
causing the deletion of `kind` and `controller-gen` binaries that are
installed in `$GOPATH/bin`


Yesterday, i embarked on a wild 7 hour journey to fix a bug that had
been causing prow jobs to fail with the error message "Kind not found".
The bug was introduced after a recent update that bumped the Go compiler
to `1.19`. I found the investigation to this bug to be both interesting
and frustrating, so i wanted to share some key takeways with the
community:

[The patch](https://github.com/aws-controllers-k8s/test-infra/commit/14dda81ce8ea430b51c9ce738483bea3744a5450) that introduced Go `1.19` also modified a `go get` command
into a `go install` command (because of this deprecation notice:
https://go.dev/doc/go-get-install-deprecation), which technically should
not have caused any issues. I tried restarting the e2e jobs in various
repositories to figure out whether the error was only related to one
controller or code-generator only, but all the repositories that execute
e2e tests were affected.

First, i started suspecting that thee `go install` command was not
working properly or had not been used correctly. I experiemented with it
locally, using various combinations of `GOPATH` and `GOBIN`, however, i
learned that the Go compiler is sophisticated enough to always put
downloaded binaries under `GOBIN` or `GOPATH/bin`. I then wondered if
the `PATH` variable didn't include the `GOBIN` path, which is supposed
to contain the `kind` and `controller-gen` binaries. I spent some time
reading the Dockerfiles and testing scripts, but they all set `GOPATH`
and always included a `GOBIN` in the `PATH` variable.

I also suspected that the issue may be related to the containers, but
experimentations with "Go containers" and environement variables
manipulation did not yield any results. I also tried building minimal
DOckerfiles to try to reproduce the issue, but that also did not give
any clues.

At this point, I suspected the container image it self. I build an image
locally and ran a shell inside it, but everythin g looked fine. THe
`kind` and `controller-gen` binaries were present and the `PATH` and
`GOPATH` variables were properly set. I then suspect that we may have a
corrupted published image in ECR, but pulling the image and running the
same commands revealed that the image was fine.

I then took a break from experimenting with Go/Docker/Envvars and tried
to spin some prowjobs with `v0.0.10` and `v0.0.9` (the last two versions
that were still using Go 1.17) of the integration tests image. This
confirmed that the issue was only with `v0.0.11`.

So, I decided to investigate further and logged in the Prow production
cluster. My first attempt was to restart a job and try to "exec bash" in
it, but the jobs failed to quickly for that to be possible. I then ran
a custom prow job (with `v0.0.11` integration image tag) but with a
`sleep 10000` command. When looking inside, there were no `kind` or
`controller-gen` binaries, i searched the entire file system, they were
nowhere to be found, grep, find, name it all.. nada. I then execute a
`go install sigs.k8s.io/kind@v0.17.0"`, and bam, it worked, the binary
was here again. The same thing happened with controller-gen. So for now
we know that we ship images with all the necessary binaries and when a
prow job starts, they disapear...

To isolate the problem further, i created a `ProwJob` resource and
copied the `Pod` (spawned by Prow) spec and metadata into a different
file. Running the same commands used previously proved that indeed
something is wrong with the pod spec, causing the binaries to disapear.
And when a file disppears it reminds me of my college years, where i
epically failed to use symbolic links, which is a bit similar (at least
from a UX point) to volume mounts in the Docker world.

So, i decided to check the volume mounts, and to my not-surprise, I
found this:

```yaml
    - mountPath: /home/prow/go
      name: code
```

Yes... Prow is mounting the test-infra source code into `GOPATH`
(`/home/prow/go` in prow jobs) ! Which is the parent directory of
`GOBIN` where we install the binaries. And it all makes sense now.
Mounting code into this directory overrides the existing volume and
deletes everything existing in `GOPATH` including the binaries we
installed before.

The Dockerfile was missing the `mv` commands that puts `kind` and
`controller-gen` in `/usr/bin`. To fix this issue, I added the missing
`mv` command to the docker file and published and new `integration`
image `v0.0.12`.

---

Anyways, investigating the source of the volume mount led me to the Prow
presets configurations. Presets are a set of configurations (volume
mounts, environement variables, etc...) that are used for jobs with
specific labels in their metadata. I tried to play with this in our Prow
cluster, but quickly stoped when it was a bit risky and could break
other components too. While digging into `test-infra` pod-util package i
learned that the code volume is not coming from our defined presets and
is a default preset coming from Prow it self - the `/home/prow/go` value
is harded-coded in `prow/pod-utils/decorate/podspec.go#L54`. I'm not
sure whether we can override this value.

Anyways, for now, i'm just gonna implement a quick fix that moves the
binaries to `/usr/bin` instead of leaving them inside `GOBIN`. Ideally
we should either choose a new directory go `GOPATH` that is different
from `$HOME/go` or find a solution that will let the code and our
binaries coexist in the same place. Either of them requires a lot of
changes and can agressively break some our prow components/scripts.

@jljaco is currently workng on creating a staging cluster, which will
provide us a safe environementto test and experiment with new
configurations. This will allow us to try out new changes without having
to woryy about potentially impacting the production environement.

Signed-off-by: Amine Hilaly <hilalyamine@gmail.com>

By submitting this pull request, I confirm that my contribution is made under the terms of the Apache 2.0 license.

---
## [jbradley8484/Magisk](https://github.com/jbradley8484/Magisk)@[cbe54417a2...](https://github.com/jbradley8484/Magisk/commit/cbe54417a2f68efd0903b305d58b140eb0f1f14a)
#### Wednesday 2023-02-01 16:42:16 by jbradley8484

# Magisk Changelog  ### v25.2  - [MagiskInit] Fix a potential issue when stub cpio is used - [MagiskInit] Fix reboot to recovery when stub cpio is used - [MagiskInit] Fix sepolicy.rules symlink for rootfs devices - [General] Better data encryption detection - [General] Move the whole logging infrastructure into Rust  ### v25.1  - [MagiskBoot] Fix ramdisk backup being incorrectly skipped - [MagiskBoot] Add new feature to detect unsupported dtb and abort during installation - [Zygisk] Change binary hijack paths - [App] Fix incorrect recovery mode detection and installation - [MagiskInit] Fix config not properly exported in legacy SAR devices - [General] Enforce the Magisk app to always match or be newer than `magiskd`  ### v25.0  - [MagiskInit] Update 2SI implementation, significantly increase device compatibility (e.g. Sony Xperia devices) - [MagiskInit] Introduce new `sepolicy` injection mechanism - [MagiskInit] Support Oculus Go - [MagiskInit] Support Android 13 GKIs (Pixel 6) - [MagiskBoot] Fix vbmeta extraction implementation - [App] Fix stub app on older Android versions - [App] [MagiskSU] Properly support apps using `sharedUserId` - [MagiskSU] Fix a possible crash in `magiskd` - [MagiskSU] Prune unused UIDs as soon as `system_server` restarts to prevent UID reuse attacks - [MagiskSU] Verify and enforce the installed Magisk app's certificate to match the distributor's signature - [MagiskSU] [Zygisk] Proper package management and detection - [Zygisk] Fix function hooking on devices running Android 12 with old kernels - [Zygisk] Fix Zygisk's self code unloading implementation - [DenyList] Fix DenyList on shared UID apps - [BusyBox] Add workaround for devices running old kernels  ### v24.3  - [General] Stop using `getrandom` syscall - [Zygisk] Update API to v3, adding new fields to `AppSpecializeArgs` - [App] Improve app repackaging installation workflow  ### v24.2  - [MagiskSU] Fix buffer overflow - [MagiskSU] Fix owner managed multiuser superuser settings - [MagiskSU] Fix command logging when using `su -c <cmd>` - [MagiskSU] Prevent su request indefinite blocking - [MagiskBoot] Support `lz4_legacy` archive with multiple magic - [MagiskBoot] Fix `lz4_lg` compression - [DenyList] Allow targeting processes running as system UID - [Zygisk] Workaround Samsung's "early zygote" - [Zygisk] Improved Zygisk loading mechanism - [Zygisk] Fix application UID tracking - [Zygisk] Fix improper `umask` being set in zygote - [App] Fix BusyBox execution test - [App] Improve stub loading mechanism - [App] Major app upgrade flow improvements - [General] Improve commandline error handling and messaging  ### v24.1  - [App] Stability improvements  ### v24.0  - [General] MagiskHide is removed from Magisk - [General] Support Android 12 - [General] Support devices that do not support 32-bit and only runs 64-bit code - [General] Update BusyBox to 1.34.1 - [Zygisk] Introduce new feature: Zygisk - [Zygisk] Introduce DenyList feature to revert Magisk features in user selected processes - [MagiskBoot] Support patching 32-bit kernel zImages - [MagiskBoot] Support boot image header v4 - [MagiskBoot] Support patching out `skip_initramfs` from dtb bootargs - [MagiskBoot] Add new env variable `PATCHVBMETAFLAG` to configure whether vbmeta flags should be patched - [MagiskInit] Support loading fstab from `/system/etc` (required for Pixel 6) - [MagiskInit] Support `/proc/bootconfig` for loading boot configurations - [MagiskInit] Better support for some Meizu devices - [MagiskInit] Better support for some OnePlus/Oppo/Realme devices - [MagiskInit] Support `init.real` on some Sony devices - [MagiskInit] Skip loading Magisk when detecting DSU - [MagiskPolicy] Load `*_compat_cil_file` from system_ext - [MagiskSU] Use isolated devpts if the kernel supports it - [MagiskSU] Fix root shell if isolated mount namespace is set - [resetprop] Deleted properties are now wiped from memory instead of just unlinking - [App] Build a single APK for all ABIs - [App] Switch to use standard bottom navigation bar - [App] Downloading modules from the centralized Magisk-Modules-Repo is removed - [App] Support user configuration of boot image vbmeta patching - [App] Restore the ability to install Magisk on the other slot on some A/B devices - [App] Allow modules to specify an update URL for in-app update + install  ### v23.0  - [App] Update snet extension. This fixes SafetyNet API errors. - [App] Fix a bug in the stub app that causes APK installation to fail - [App] Hide annoying errors in logs when hidden as stub - [App] Fix issues when patching ODIN tar files when the app is hidden - [General] Remove all pre Android 5.0 support - [General] Update BusyBox to use proper libc - [General] Fix C++ undefined behaviors - [General] Several `sepolicy.rule` copy/installation fixes - [MagiskPolicy] Remove unnecessary sepolicy rules - [MagiskHide] Update package and process name validation logic - [MagiskHide] Some changes that prevents zygote deadlock  ### v22.1  - [App] Prevent multiple installation sessions running in parallel - [App] Prevent OutOfMemory crashes when checking boot signature on PXA boot images - [General] Proper cgroup migration implementation - [General] Rewrite log writer from scratch, should resolve any crashes and deadlocks - [General] Many scripts updates fixing regressions - [MagiskHide] Prevent possible deadlock when signal arrives - [MagiskHide] Partial match process names if necessary - [MagiskBoot] Preserve and patch AVB 2.0 structures/headers in boot images - [MagiskBoot] Properly strip out data encryption flags - [MagiskBoot] Prevent possible integer overflow - [MagiskInit] Fix `sepolicy.rule` mounting strategy - [resetprop] Always delete existing `ro.` props before updating. This will fix bootloops that could be caused by modifying device fingerprint properties.  ### v22.0  - [General] Magisk and Magisk Manager is now merged into the same package! - [App] The term "Magisk Manager" is no longer used elsewhere. We refer it as the Magisk app. - [App] Support hiding the Magisk app with advanced technique (stub APK loading) on Android 5.0+ (it used to be 9.0+) - [App] Disallow re-packaging the Magisk app on devices lower than Android 5.0 - [App] Detect and warn about multiple invalid states and provide instructions on how to resolve it - [MagiskHide] Fix a bug when stopping MagiskHide does not take effect - [MagiskBoot] Fix bug when unpacking `lz4_lg` compressed boot images - [MagiskInit] Support Galaxy S21 series - [MagiskSU] Fix incorrect APEX paths that caused `libsqlite.so` fail to load  ### v21.4  - [MagiskSU] Fix `su -c` behavior that broke many root apps - [General] Properly handle read/write over sockets (the `broken pipe` issue)  ### v21.3  - [MagiskInit] Avoid mounting `f2fs` userdata as it may result in kernel crashes. This shall fix a lot of bootloops - [MagiskBoot] Fix a minor header checksum bug for `DHTB` header and ASUS `blob` image formats - [MagiskHide] Allowing hiding isolated processes if the mount namespace is separated  ### v21.2  - [MagiskInit] Detect 2SI after mounting `system_root` on legacy SAR devices - [General] Make sure `post-fs-data` scripts cannot block more than 35 seconds - [General] Fix the `magisk --install-module` command - [General] Trim Windows newline when reading files - [General] Directly log to file to prevent `logcat` weirdness - [MagiskBoot] Fix header dump/load for header v3 images  ### v21.1  - [MagiskBoot] Support boot header v3 (Pixel 5 and 4a 5G) - [MagiskBoot] Distinguish `lz4_lg` and `lz4_legacy` (Pixel 5 and 4a 5G) - [MagiskBoot] Support vendor boot images (for dev, not relevant for Magisk installation) - [MagiskInit] Support kernel cmdline `androidboot.fstab_suffix` - [MagiskInit] Support kernel initialized dm-verity on legacy SAR - [General] Significantly broaden sepolicy.rule compatibility - [General] Add Magisk binaries to `PATH` when executing boot scripts - [General] Update `--remove-modules` command implementation - [General] Make Magisk properly survive after factory reset on Android 11 - [MagiskSU] Add APEX package `com.android.i18n` to `LD_LIBRARY_PATH` when linking `libsqlite.so` - [MagiskHide] Support hiding apps installed in secondary users (e.g. work profile) - [MagiskHide] Make zygote detection more robust  ### v21.0  - [General] Support Android 11 🎉 - [General] Add Safe Mode detection. Disable all modules when the device is booting into Safe Mode. - [General] Increase `post-fs-data` mode timeout from 10 seconds to 40 seconds - [MagiskInit] Rewritten 2SI support from scratch - [MagiskInit] Support when no `/sbin` folder exists (Android 11) - [MagiskInit] Dump fstab from device-tree to rootfs and force `init` to use it for 2SI devices - [MagiskInit] Strip out AVB for 2SI as it may cause bootloop - [Modules] Rewritten module mounting logic from scratch - [MagiskSU] For Android 8.0+, a completely new policy setup is used. This reduces compromises in Android's sandbox, providing more policy isolation and better security for root users. - [MagiskSU] Isolated mount namespace will now first inherit from parent process, then isolate itself from the world - [MagiskSU] Update communication protocol with Magisk Manager to work with the hardened SELinux setup - [MagiskPolicy] Optimize match all rules. This will significantly reduce policy binary size and save memory and improve general kernel performance. - [MagiskPolicy] Support declaring new types and attributes - [MagiskPolicy] Make policy statement closer to stock `*.te` format. Please check updated documentation or `magiskpolicy --help` for more details. - [MagiskBoot] Support compressed `extra` blobs - [MagiskBoot] Pad boot images to original size with zeros - [MagiskHide] Manipulate additional vendor properties  ### v20.4  - [MagiskInit] Fix potential bootloop in A-only 2SI devices - [MagiskInit] Properly support Tegra partition naming - [General] Load libsqlite.so dynamically, which removes the need to use wrapper scripts on Android 10+ - [General] Detect API level with a fallback method on some devices - [General] Workaround possible bug in x86 kernel readlinkat system call - [BusyBox] Enable SELinux features. Add chcon/runcon etc., and '-Z' option to many applets - [BusyBox] Introduce standalone mode. More details in release notes - [MagiskHide] Disable MagiskHide by default - [MagiskHide] Add more potential detectable system properties - [MagiskHide] Add workaround for Xiaomi devices bootloop when MagiskHide is enabled on cross region ROMs - [MagiskBoot] Support patching special Motorolla DTB format - [MagiskPolicy] Support 'genfscon' sepolicy rules - [Scripts] Support NAND based boot images (character nodes in /dev/block) - [Scripts] Better addon.d (both v1 and v2) support - [Scripts] Support Lineage Recovery for Android 10+  ### v20.3  - [MagiskBoot] Fix `lz4_legacy` decompression  ### v20.2  - [MagiskSU] Properly handle communication between daemon and application (root request prompt) - [MagiskInit] Fix logging in kmsg - [MagiskBoot] Support patching dtb/dtbo partition formats - [General] Support pre-init sepolicy patch in modules - [Scripts] Update magisk stock image backup format  ### v20.1  - [MagiskSU] Support component name agnostic communication (for stub APK) - [MagiskBoot] Set proper `header_size` in boot image headers (fix vbmeta error on Samsung devices) - [MagiskHide] Scan zygote multiple times - [MagiskInit] Support recovery images without /sbin/recovery binary. This will fix some A/B devices unable to boot to recovery after flashing Magisk - [General] Move acct to prevent daemon being killed - [General] Make sure "--remove-modules" will execute uninstall.sh after removal  ### v20.0  - [MagiskBoot] Support inject/modify `mnt_point` value in DTB fstab - [MagiskBoot] Support patching QCDT - [MagiskBoot] Support patching DTBH - [MagiskBoot] Support patching PXA-DT - [MagiskInit] [2SI] Support non A/B setup (Android 10) - [MagiskHide] Fix bug that reject process names with ":" - [MagicMount] Fix a bug that cause /product mirror not created  ### v19.4  - [MagiskInit] [SAR] Boot system-as-root devices with system mounted as / - [MagiskInit] [2SI] Support 2-stage-init for A/B devices (Pixel 3 Android 10) - [MagiskInit] [initramfs] Delay sbin overlay creation to post-fs-data - [MagiskInit] [SARCompat] Old system-as-root implementation is deprecated, no more future changes - [MagiskInit] Add overlay.d support for root directory overlay for new system-as-root implementation - [MagiskSU] Unblock all signals in root shells (fix bash on Android) - [MagicMount] Support replacing files in /product - [MagiskHide] Support Android 10's Zygote blastula pool - [MagiskHide] All random strings now also have random length - [MagiskBoot] Allow no recompression for ramdisk.cpio - [MagiskBoot] Support some weird Huawei boot images - [General] Add new `--remove-modules` command to remove modules without root in ADB shell - [General] Support Android 10 new APEX libraries (Project Mainline)  ### v19.3  - [MagiskHide] Hugely improve process monitor implementation, hopefully should no longer cause 100% CPU and daemon crashes - [MagiskInit] Wait for partitions to be ready for early mount, should fix bootloops on a handful of devices - [MagiskInit] Support EROFS used in EMUI 9.1 - [MagiskSU] Properly implement mount namespace isolation - [MagiskBoot] Proper checksum calculation for header v2  ### v19.2  - [General] Fix uninstaller - [General] Fix bootloops on some devices with tmpfs mounting to /data - [MagiskInit] Add Kirin hi6250 support - [MagiskSU] Stop claiming device focus for su logging/notify if feasible.   This fix issues with users locking Magisk Manager with app lock, and prevent   video apps get messed up when an app is requesting root in the background.  ### v19.1  - [General] Support recovery based Magisk - [General] Support Android Q Beta 2 - [MagiskInit] New sbin overlay setup process for better compatibility - [MagiskInit] Allow long pressing volume up to boot to recovery in recovery mode - [MagicMount] Use proper system_root mirror - [MagicMount] Use self created device nodes for mirrors - [MagicMount] Do not allow adding new files/folders in partition root folder (e.g. /system or /vendor)  ### v19.0  - [General] Remove usage of magisk.img - [General] Add 64 bit magisk binary for native 64 bit support - [General] Support A only system-as-root devices that released with Android 9.0 - [General] Support non EXT4 system and vendor partitions - [MagiskHide] Use Zygote ptracing for monitoring new processes - [MagiskHide] Targets are now per-application component - [MagiskInit] Support Android Q (no logical partition support yet!) - [MagiskPolicy] Support Android Q new split sepolicy setup - [MagiskInit] Move sbin overlay creation from main daemon post-fs-data to early-init - [General] Service scripts now run in parallel - [MagiskInit] Directly inject magisk services to init.rc - [General] Use lzma2 compressed ramdisk in extreme conditions - [MagicMount] Clone attributes from original file if exists - [MagiskSU] Use `ACTION_REBOOT` intent to workaround some OEM broadcast restrictions - [General] Use `skip_mount` instead of `auto_mount`: from opt-in to opt-out  ### v18.1  - [General] Support EMUI 9.0 - [General] Support Kirin 960 devices - [General] Support down to Android 4.2 - [General] Major code base modernization under-the-hood  ### v18.0  - [General] Migrate all code base to C++ - [General] Modify database natively instead of going through Magisk Manager - [General] Deprecate path /sbin/.core, please start using /sbin/.magisk - [General] Boot scripts are moved from `<magisk_img>/.core/<stage>.d` to `/data/adb/<stage>.d` - [General] Remove native systemless hosts (Magisk Manager is updated with a built-in systemless hosts module) - [General] Allow module post-fs-data.sh scripts to disable/remove modules - [MagiskHide] Use component names instead of process names as targets - [MagiskHide] Add procfs protection on SDK 24+ (Nougat) - [MagiskHide] Remove the folder /.backup to prevent detection - [MagiskHide] Hide list is now stored in database instead of raw textfile in images - [MagiskHide] Add "--status" option to CLI - [MagiskHide] Stop unmounting non-custom related mount points - [MagiskSU] Add `FLAG_INCLUDE_STOPPED_PACKAGES` in broadcasts to force wake Magisk Manager - [MagiskSU] Fix a bug causing SIGWINCH not properly detected - [MagiskPolicy] Support new av rules: type_change, type_member - [MagiskPolicy] Remove all AUDITDENY rules after patching sepolicy to log all denies for debugging - [MagiskBoot] Properly support extra_cmdline in boot headers - [MagiskBoot] Try to repair broken v1 boot image headers - [MagiskBoot] Add new CPIO command: "exists"  ### v17.3  - [MagiskBoot] Support boot image header v1 (Pixel 3) - [MagiskSU] No more linked lists for caching `su_info` - [MagiskSU] Parse command-lines in client side and send only options to daemon - [MagiskSU] Early ACK to prevent client freezes and early denies - [Daemon] Prevent bootloops in situations where /data is mounted twice - [Daemon] Prevent logcat failures when /system/bin is magic mounting, could cause MagiskHide to fail - [Scripts] Switch hexpatch to remove Samsung Defex to a more general pattern - [Scripts] Update data encryption detection for better custom recovery support  ### v17.2  - [ResetProp] Update to AOSP upstream to support serialized system properties - [MagiskInit] Randomize Magisk service names to prevent detection (e.g. FGO) - [MagiskSU] New communication scheme to communicate with Magisk Manager  ### v17.0/17.1  - [General] Bring back install to inactive slot for OTAs on A/B devices - [Script] Remove system based root in addon.d - [Script] Add proper addon.d-v2 for preserving Magisk on custom ROMs on A/B devices - [Script] Enable KEEPVERITY when the device is using system_root_image - [Script] Add hexpatch to remove Samsung defex in new Oreo kernels - [Daemon] Support non ext4 filesystems for mirrors (system/vendor) - [MagiskSU] Make pts sockets always run in dev_pts secontext, providing all terminal emulator root shell the same power as adb shells - [MagiskHide] Kill all processes with same UID of the target to workaround OOS embryo optimization - [MagiskInit] Move all sepolicy patches pre-init to prevent Pixel 2 (XL) boot service breakdown  ### v16.7  - [Scripts] Fix boot image patching errors on Android P (workaround the strengthened seccomp) - [MagiskHide] Support hardlink based ns proc mnt (old kernel support) - [Daemon] Fix permission of /dev/null after logcat commands, fix ADB on EMUI - [Daemon] Log fatal errors only on debug builds - [MagiskInit] Detect early mount partname from fstab in device tree  ### v16.6  - [General] Add wrapper script to overcome weird `LD_XXX` flags set in apps - [General] Prevent bootloop when flashing Magisk after full wipe on FBE devices - [Scripts] Support patching DTB placed in extra sections in boot images (Samsung S9/S9+) - [Scripts] Add support for addon.d-v2 (untested) - [Scripts] Fix custom recovery console output in addon.d - [Scripts] Fallback to parsing sysfs for detecting block devices - [Daemon] Check whether a valid Magisk Manager is installed on boot, if not, install stub APK embedded in magiskinit - [Daemon] Check whether Magisk Manager is repackaged (hidden), and prevent malware from hijacking com.topjohnwu.magisk - [Daemon] Introduce new daemon: magisklogd, a dedicated daemon to handle all logcat related monitoring - [Daemon] Replace old invincible mode with handshake between magiskd and magisklogd, one will respawn the other if disconnected - [Daemon] Support GSI adbd bind mounting - [MagiskInit] Support detecting block names in upper case (Samsung) - [MagiskBoot] Check DTB headers to prevent false detections within kernel binary - [MagiskHide] Compare mount namespace with PPID to make sure the namespace is actually separated, fix root loss - [MagiskSU] Simplify `su_info` caching system, should use less resources and computing power - [MagiskSU] Reduce the amount of broadcasting to Magisk Manager - [ImgTool] Separate all ext4 image related operations to a new applet called "imgtool" - [ImgTool] Use precise free space calculation methods - [ImgTool] Use our own set of loop devices hidden along side with sbin tmpfs overlay. This not only eliminates another possible detection method, but also fixes apps that mount OBB files as loop devices (huge thanks to dev of Pzizz for reporting this issue)  ### v16.4  - [Daemon] Directly check logcat command instead of detecting logd, should fix logging and MagiskHide on several Samsung devices - [Daemon] Fix startup Magisk Manager APK installation on Android P - [MagiskPolicy] Switch from AOSP u:r:su:s0 to u:r:magisk:s0 to prevent conflicts - [MagiskPolicy] Remove unnecessary sepolicy rules to reduce security penalty - [Daemon] Massive re-design /sbin tmpfs overlay and daemon start up - [MagiskInit] Remove `magiskinit_daemon`, the actual magisk daemon (magiskd) shall handle everything itself - [Daemon] Remove post-fs stage as it is very limited and also will not work on A/B devices; replaced with simple mount in post-fs-data, which will run ASAP even before the daemon is started - [General] Remove all 64-bit binaries as there is no point in using them; all binaries are now 32-bit only.   Some weirdly implemented root apps might break (e.g. Tasker, already reported to the developer), but it is not my fault :) - [resetprop] Add Protobuf encode/decode to support manipulating persist properties on Android P - [MagiskHide] Include app sub-services as hiding targets. This might significantly increase the amount of apps that could be properly hidden  ### v16.3  - [General] Remove symlinks used for backwards compatibility - [MagiskBoot] Fix a small size calculation bug  ### v16.2  - [General] Force use system binaries in handling ext4 images (fix module installation on Android P) - [MagiskHide] Change property state to disable if logd is disabled  ### v16.1  - [MagiskBoot] Fix MTK boot image packaging - [MagiskBoot] Add more Nook/Acclaim headers support - [MagiskBoot] Support unpacking DTB with empty kernel image - [MagiskBoot] Update high compression mode detection logic - [Daemon] Support new mke2fs tool on Android P - [resetprop] Support Android P new property context files - [MagiskPolicy] Add new rules for Android P  ### v16.0  - [MagiskInit] Support non `skip_initramfs` devices with slot suffix (Huawei Treble) - [MagiskPolicy] Add rules for Magisk Manager - [Compiler] Workaround an NDK compiler bug that causes bootloops  ### v15.4  - [MagiskBoot] Support Samsung PXA, DHTB header images - [MagiskBoot] Support ASUS blob images - [MagiskBoot] Support Nook Green Loader images - [MagiskBoot] Support pure ramdisk images - [MagiskInit] Prevent OnePlus angela `sepolicy_debug` from loading - [MagiskInit] Obfuscate Magisk socket entry to prevent detection and security - [Daemon] Fix subfolders in /sbin shadowed by overlay - [Daemon] Obfuscate binary names to prevent naive detections - [Daemon] Check logd before force trying to start logcat in a loop  ### v15.3  - [Daemon] Fix the bug that only one script would be executed in post-fs-data.d/service.d - [Daemon] Add `MS_SILENT` flag when mounting, should fix some devices that cannot mount magisk.img - [MagiskBoot] Fix potential segmentation fault when patching ramdisk, should fix some installation failures  ### v15.2  - [MagiskBoot] Fix dtb verity patches, should fix dm-verity bootloops on newer devices placing fstabs in dtb - [MagiskPolicy] Add new rules for proper Samsung support, should fix MagiskHide - [MagiskInit] Support non `skip_initramfs` devices using split sepolicies (e.g. Zenfone 4 Oreo) - [Daemon] Use specific logcat buffers, some devices does not support all log buffers - [scripts] Update scripts to double check whether boot slot is available, some devices set a boot slot without A/B partitions  ### v15.1  - [MagiskBoot] Fix faulty code in ramdisk patches which causes bootloops in some config and fstab format combos  ### v15.0  - [Daemon] Fix the bug that Magisk cannot properly detect /data encryption state - [Daemon] Add merging `/cache/magisk.img` and `/data/adb/magisk_merge.img` support - [Daemon] Update to upstream libsepol to support cutting edge split policy custom ROM cil compilations  ### v14.6 (1468)  - [General] Move all files into a safe location: /data/adb - [Daemon] New invincible implementation: use `magiskinit_daemon` to monitor sockets - [Daemon] Rewrite logcat monitor to be more efficient - [Daemon] Fix a bug where logcat monitor may spawn infinite logcat processes - [MagiskSU] Update su to work the same as proper Linux implementation:   Initialize window size; all environment variables will be migrated (except HOME, SHELL, USER, LOGNAME, these will be set accordingly),   "--preserve-environment" option will preserve all variables, including those four exceptions.   Check the Linux su manpage for more info - [MagiskBoot] Massive refactor, rewrite all cpio operations and CLI - [MagiskInit][magiskboot] Support ramdisk high compression mode  ### v14.5 (1456)  - [Magiskinit] Fix bootloop issues on several devices - [misc] Build binaries with NDK r10e, should get rid of the nasty linker warning when executing magisk  ### v14.5 (1455)  - [Daemon] Moved internal path to /sbin/.core, new image mountpoint is /sbin/.core/img - [MagiskSU] Support switching package name, used when Magisk Manager is hidden - [MagiskHide] Add temporary /magisk removal - [MagiskHide] All changes above contributes to hiding from nasty apps like FGO and several banking apps - [Magiskinit] Use magiskinit for all devices (dynamic initramfs) - [Magiskinit] Fix Xiaomi A1 support - [Magiskinit] Add Pixel 2 (XL) support - [Magiskboot] Add support to remove avb-verity in dtbo.img - [Magiskboot] Fix typo in handling MTK boot image headers - [script] Along with updates in Magisk Manager, add support to sign boot images (AVB 1.0) - [script] Add dtbo.img backup and restore support - [misc] Many small adjustments to properly support old platforms like Android 5.0  ### v14.3 (1437)  - [MagiskBoot] Fix Pixel C installation - [MagiskBoot] Handle special `lz4_legacy` format properly, should fix all LG devices - [Daemon] New universal logcat monitor is added, support plug-and-play to worker threads - [Daemon] Invincible mode: daemon will be restarted by init, everything should seamlessly through daemon restarts - [Daemon] Add new restorecon action, will go through and fix all Magisk files with selinux unlabeled to `system_file` context - [Daemon] Add brute-force image resizing mode, should prevent the notorious Samsung crappy resize2fs from affecting the result - [resetprop] Add new "-p" flag, used to toggle whether alter/access the actual persist storage for persist props  ### v14.2  - [MagicMount] Clone attributes to tmpfs mountpoint, should fix massive module breakage  ### v14.1  - [MagiskInit] Introduce a new init binary to support `skip_initramfs` devices (Pixel family) - [script] Fix typo in update-binary for x86 devices - [script] Fix stock boot image backup not moved to proper location - [script] Add functions to support A/B slot and `skip_initramfs` devices - [script] Detect Meizu boot blocks - [MagiskBoot] Add decompress zImage support - [MagiskBoot] Support extracting dtb appended to zImage block - [MagiskBoot] Support patching fstab within dtb - [Daemon/MagiskSU] Proper file based encryption support - [Daemon] Create core folders if not exist - [resetprop] Fix a bug which delete props won't remove persist props not in memory - [MagicMount] Remove usage of dummy folder, directly mount tmpfs and construct file structure skeleton in place  ### v14.0  - [script] Simplify installation scripts - [script] Fix a bug causing backing up and restoring stock boot images failure - [script] Installation and uninstallation will migrate old or broken stock boot image backups to proper format - [script] Fix an issue with selabel setting in `util_functions.sh` on Lollipop - [rc script] Enable logd in post-fs to start logging as early as possible - [MagiskHide] magisk.img mounted is no longer a requirement   Devices with issues mounting magisk.img can now run in proper core-only mode - [MagiskBoot] Add native function to extract stock SHA1 from ramdisk - [b64xz] New tool to extract compressed and encoded binary dumps in shell script - [busybox] Add busybox to Magisk source, and embed multi-arch busybox binary into update-binary shell script - [busybox] Busybox is added into PATH for all boot scripts (post-fs-data.d, service.d, and all module scripts) - [MagiskSU] Fully fix multiuser issues - [Magic Mount] Fix a typo in cloning attributes - [Daemon] Fix the daemon crashing when boot scripts opens a subshell - [Daemon] Adjustments to prevent stock Samsung kernel restrictions on exec system calls for binaries started from /data - [Daemon] Workaround on Samsung device with weird fork behaviors  ### v13.3  - [MagiskHide] Update to bypass Google CTS (2017.7.17) - [resetprop] Properly support removing persist props - [uninstaller] Remove Magisk Manager and persist props  ### v13.2  - [magiskpolicy] Fix magiskpolicy segfault on old Android versions, should fix tons of older devices that couldn't use v13.1 - [MagiskHide] Set proper selinux context while re-linking /sbin to hide Magisk, should potentially fix many issues - [MagiskBoot] Change lzma compression encoder flag from `LZMA_CHECK_CRC64` to `LZMA_CHECK_CRC32`, kernel only supports latter - [General] Core-only mode now properly mounts systemless hosts and magiskhide  ### v13.1  - [General] Merge MagiskSU, magiskhide, resetprop, magiskpolicy into one binary - [General] Add Android O support (tested on DP3) - [General] Dynamic link libselinux.so, libsqlite.so from system to greatly reduce binary size - [General] Remove bundled busybox because it causes a lot of issues - [General] Unlock all block devices for read-write support instead of emmc only (just figured not all devices uses emmc lol) - [Scripts] Run all ext4 image operations through magisk binary in flash scripts - [Scripts] Updated scripts to use magisk native commands to increase compatibility - [Scripts] Add addon.d survival support - [Scripts] Introduce `util_functions.sh`, used as a global shell script function source for all kinds of installation - [MagiskBoot] Moved boot patch logic into magiskboot binary - [MagiskSU] Does not fork new process for each request, add new threads instead - [MagiskSU] Added multiuser support - [MagiskSU] Introduce new timeout queue mechanism, prevent performance hit with poorly written su apps - [MagiskSU] Multiple settings moved from prop detection to database - [MagiskSU] Add namespace mode option support - [MagiskSU] Add master-mount option - [resetprop] Updated to latest AOSP upstream, support props from 5.0 to Android O - [resetprop] Renamed all functions to prevent calling functions from external libc - [magiskpolicy] Updated libsepol from official SELinux repo - [magiskpolicy] Added xperm patching support (in order to make Android O work properly) - [magiskpolicy] Updated rules for Android O, and Liveboot support - [MagiskHide] Remove pseudo permissive mode, directly hide permissive status instead - [MagiskHide] Remove unreliable list file monitor, change to daemon request mode - [MagiskHide] MagiskHide is now enabled by default - [MagiskHide] Update unmount policies, passes CTS in SafetyNet! - [MagiskHide] Add more props for hiding - [MagiskHide] Remove background magiskhide daemon, spawn short life process for unmounting purpose - [Magic Mount] Ditched shell script based mounting, use proper C program to parse and mount files. Speed is SIGNIFICANTLY improved  ### v12.0  - [General] Move most binaries into magisk.img (Samsung cannot run su daemon in /data) - [General] Move sepolicy live patch to `late_start` service   This shall fix the long boot times, especially on Samsung devices - [General] Add Samsung RKP hexpatch back, should now work on Samsung stock kernels - [General] Fix installation with SuperSU - [MagiskHide] Support other logcat `am_proc_start` patterns - [MagiskHide] Change /sys/fs/selinux/enforce(policy) permissions if required   Samsung devices cannot switch selinux states, if running on permissive custom kernel, the users will stuck at permissive   If this scenario is detected, change permissions to hide the permissive state, leads to SafetyNet passes - [MagiskHide] Add built in prop rules to fake KNOX status   Samsung apps requiring KNOX status to be 0x0 should now work (Samsung Pay not tested) - [MagiskHide] Remove all ro.build props, since they cause more issues than they benefit... - [MagiskBoot] Add lz4 legacy format support (most linux kernel using lz4 for compression is using this) - [MagiskBoot] Fix MTK kernels with MTK headers  ### v11.5/11.6  - [Magic Mount] Fix mounting issues with devices that have separate /vendor partitions - [MagiskBoot] Whole new boot image patching tool, please check release note for more info - [magiskpolicy] Rename sepolicy-inject to magiskpolicy - [magiskpolicy] Update a rule to allow chcon everything properly - [MagiskHide] Prevent multirom crashes - [MagiskHide] Add patches for ro.debuggable, ro.secure, ro.build.type, ro.build.tags, ro.build.selinux - [MagiskHide] Change /sys/fs/selinux/enforce, /sys/fs/selinux/policy permissions for Samsung compatibility - [MagiskSU] Fix read-only partition mounting issues - [MagiskSU] Disable -cn option, the option will do nothing, preserved for compatibility  ### v11.1  - [sepolicy-inject] Add missing messages - [magiskhide] Start MagiskHide with scripts  ### v11.0  - [Magic Mount] Support replacing symlinks.   Symlinks cannot be a target of a bind mounted, so they are treated the same as new files - [Magic Mount] Fix the issue when file/folder name contains spaces - [BusyBox] Updated to v1.26.2. Should fix the black screen issues of FlashFire - [resetprop] Support reading prop files that contains spaces in prop values - [MagiskSU] Adapt communication to Magisk Manager; stripped out unused data transfer - [MagiskSU] Implement SuperUser access option (Disable, APP only, ADB Only, APP & ADB)   phh Superuser app has this option but the feature isn't implemented within the su binary - [MagiskSU] Fixed all issues with su -c "commands" (run commands with root)   This feature is supposed to only allow one single option, but apparently adb shell su -c "command" doesn't work this way, and plenty of root apps don't follow the rule. The su binary will now consider everything after -c as a part of the command. - [MagiskSU] Removed legacy context hack for TiBack, what it currently does is slowing down the invocation - [MagiskSU] Preserve the current working directory after invoking su   Previously phh superuser will change the path to /data/data after obtaining root shell. It will now stay in the same directory where you called su - [MagiskSU] Daemon now also runs in u:r:su:s0 context - [MagiskSU] Removed an unnecessary fork, reduce running processes and speed up the invocation - [MagiskSU] Add -cn option to the binary   Not sure if this is still relevant, and also not sure if implemented correctly, but hey it's here - [sepolicy-inject] Complete re-write the command-line options, now nearly matches supolicy syntax - [sepolicy-inject] Support all matching mode for nearly every action (makes pseudo enforced possible) - [sepolicy-inject] Fixed an ancient bug that allocated memory isn't reset - [uninstaller] Now works as a independent script that can be executed at boot   Fully support recovery with no /data access, Magisk uninstallation with Magisk Manager - [Addition] Busybox, MagiskHide, hosts settings can now be applied instantly; no reboots required - [Addition] Add post-fs-data.d and service.d - [Addition] Add option to disable Magisk (MagiskSU will still be started)  ### v10.2  - [Magic Mount] Remove apps/priv-app from whitelist, should fix all crashes - [phh] Fix binary out-of-date issue - [scripts] Fix root disappear issue when upgrading within Magisk Manager  ### v10  - [Magic Mount] Use a new way to mount system (vendor) mirrors - [Magic Mount] Use universal way to deal with /vendor, handle both separate partition or not - [Magic Mount] Adding **anything to any place** is now officially supported (including /system root and /vendor root) - [Magic Mount] Use symlinks for mirroring back if possible, reduce bind mounts for adding files - [Magisk Hide] Check init namespace, zygote namespace to prevent Magic Mount breakage (a.k.a root loss) - [Magisk Hide] Send SIGSTOP to pause target process ASAP to prevent crashing if unmounting too late - [Magisk Hide] Hiding should work under any conditions, including adding libs and /system root etc. - [phh] Root the device if no proper root detected - [phh] Move `/sbin` to `/sbin_orig` and link back, fix Samsung no-suid issue - [scripts] Improve SuperSU integration, now uses sukernel to patch ramdisk, support SuperSU built in ramdisk restore - [template] Add PROPFILE option to load system.prop  ### v9  - **[API Change] Remove the interface for post-fs modules** - [resetprop] New tool "resetprop" is added to Magisk to replace most post-fs modules' functionality - [resetprop] Magisk will now patch "ro.boot.verifiedbootstate", "ro.boot.flash.locked", "ro.boot.veritymode" to bypass Safety Net - [Magic Mount] Move dummy skeleton / mirror / mountinfo filesystem tree to tmpfs - [Magic Mount] Rewritten dummy cloning mechanism from scratch, will result in minimal bind mounts, minimal file traversal, eliminate all possible issues that might happen in extreme cases - [Magic Mount] Adding new items to /system/bin, /system/vendor, /system/lib(64) is properly supported (devices with separate vendor partition is not supported yet) - [Magisk Hide] Rewritten from scratch, now run in daemon mode, proper list monitoring, proper mount detection, and maybe more..... - [Boot Image] Add support for Motorola boot image dtb, it shall now unpack correctly - [Uninstaller] Add removal of SuperSU custom patch script  ### v8  - Add Magisk Hide to bypass SafetyNet - Improve SuperSU integration: no longer changes the SuperSU PATH - Support rc script entry points not located in init.rc  ### v7  - Fully open source - Remove supolicy dependency, use my own sepolicy-injection - Run everything in its own selinux domain, should fix all selinux issues - Add Note 7 stock kernel hex patches - Add support to install Magisk in Magisk Manager - Add support for image merging for module flashing in Magisk Manager - Add root helpers for SuperSU auto module-ize and auto upgrading legacy phh superuser - New paths to toggle busybox, and support all root solutions - Remove root management API; both SuperSU and phh has their own superior solutions  ### v6  - Fixed the algorithm for adding new files and dummy system - Updated the module template with a default permission, since people tend to forget them :)  ### v5  - Hotfix for older Android versions (detect policy before patching) - Update uninstaller to NOT uninstall Magisk Manager, since it cause problems  ### v4  - Important: Uninstall v1 - v3 Magisk before upgrading with the uninstaller in the OP!! - Massive Rewrite Magisk Interface API! All previous mods are NOT compatible! Please download the latest version of the mods you use (root/xposed) - Mods are now installed independently in their own subfolder. This paves the way for future Magisk Manager versions to manage mods, **just like how Xposed Modules are handled** - Support small boot partition devices (Huawei devices) - Use minimal sepolicy patch in boot image for smaller ramdisk size. Live patch policies after bootup - Include updated open source sepolicy injection tool (source code available), support nearly all SuperSU supolicy tool's functionality  ### v3  - Fix bootimg-extract for Exynos Samsung devices (thanks to @phhusson), should fix all Samsung device issues - Add supolicy back to patch sepolicy (stock Samsung do not accept permissive domain) - Update sepolicy-injection to patch su domain for Samsung devices to use phh's root - Update root disable method, using more aggressive approach - Use lazy unmount to unmount root from system, should fix some issues with custom roms - Use the highest possible compression rate for ramdisk, hope to fix some devices with no boot partition space - Detect boot partition space insufficient, will abort installer instead of breaking your device  ### v2  - Fix verity patch. It should now work on all devices (might fix some of the unable-to-boot issues) - All scripts will now run in selinux permissive mode for maximum compatibility (this will **NOT** turn your device to permissive) - Add Nougat Developer Preview 5 support - Add systemless host support for AdBlock Apps (enabled by default) - Add support for new root disable method - Remove sepolicy patches that uses SuperSU's supolicy tool; it is now using a minimal set of modifications - Removed Magisk Manager in Magisk patch, it is now included in Magisk phh's superuser only  ### v1  - Initial release

---
## [zoghbi-a/pyvo](https://github.com/zoghbi-a/pyvo)@[a1a831d286...](https://github.com/zoghbi-a/pyvo/commit/a1a831d28619ecb553399f819de68a2511288a23)
#### Wednesday 2023-02-01 16:48:26 by Markus Demleitner

Switching Interface, Capability and friends to new xsi:type handling.

Since this is a rather ugly hack, a few words of background:

It turns out that astropy.utils.xml completely discards all namespace
information.  That you can parse Registry/capability documents with it
in the first place is just because we only have local elements with
elementFormDefault=unqualified.  Ah well.

Given that, we can either do XML processing ourselves, properly managing
namespaces (which wouldn't be a terrible amount of work).  Or we ignore
namespaces and namespace prefixes, too.  Since I can't think of anywhere
that would be trouble in the current VO, this commit opts for the second
option.

---
## [FIJTeam/eternitystation](https://github.com/FIJTeam/eternitystation)@[ae08395328...](https://github.com/FIJTeam/eternitystation/commit/ae08395328672ee40c5abb7f2bd1452bb932d6d4)
#### Wednesday 2023-02-01 16:56:24 by san7890

Syndicate Bomb Core Payloads Can Only Be Triggered via the Bomb (#72986)

## About The Pull Request

Basically, you can't extract the bomb core, slap a 10-second c4 on it/on
the shell/and run off having triggered an incredibly powerful explosion.
This is accomplished by having the syndicate bomb override ex_act (it
will be deleted if the explosion goes off), as well as the payload
itself being subtyped into something resistant to bombs and burning.

In-universe, this is described as the shell being quite resistant to
forms of external explosive force- but if any explosive force comes from
within the bomb's shell: kabloom. The bombcore itself has been
redesigned (in a rare moment of non-ineptude) by Donk Co., who has
redesigned the bomb core payload from the ground up- meaning that it can
only be detonated electronically by an impulse from the bomb machinery.
Cutting the wrong wire and attempting to get rid of the bomb by hitting
it with an axe or something will still cause it to blow up, but you know
how those things can be.
## Why It's Good For The Game

I feel like the point of the syndicate bomb is to be a threat for the
crew to match up against. I want a clown in bomb squad gear to head out
to the site and sweat trying to figure out which wire it is, until....
KA-BLHONK: red mist. Or, I want some "helpful" assistant to interrupt
someone's session by going "I KNOW WHAT WIRE IT IS", and having those
odds of either blowing everyone around them up or actually saving the
day.

Being able to detonate something that was balanced and designed to have
_at least_ one minute and a half in **10 SECONDS** is just so injurious
to the game. You can buy a shitload of these bombs, extract the cores,
slap c4 on it and go around the station doling out some serious
explosions. You can run into medbay, wrench it down, slap a c4 on it AND
NO ONE CAN DO ANYTHING ABOUT IT! They can't cut wires, they can't figure
it out to save the day, all they can do is run. Running from danger is
fine and acceptable, but it's just completely stacked against the crew
in a way that I feel needs to be rectified somehow.

I like the idea of purposefully fucking with the wires on the spot so
you sacrificially kill everyone, that feels quite fair to me. I just
simply don't like the fact that you can waltz around the station
punching huge gaps in the hull (remember, putting c4 on the bomb core
itself would cause it to go kabloom) with nearly nothing as far as risk.
It's way too rewarding for something very easy to accomplish (there's a
reason why it's 90 seconds- it's not meant to be easy to accomplish).

This doesn't affect base bombcore behavior, just the explodey ones that
come standard in syndicate bombs.
## Changelog
:cl:
balance: After an unfortunate event occuring when some nuclear
operatives took the ship to a Fireworks Store, the Syndicate have
re-engineered their bomb cores to only explode when electronically
triggered by the bomb shell itself. The payload inside a standard
syndicate bomb can not be exploded with another explosion, you must keep
it in the bomb machinery for it to actually do some explodey stuff.
/:cl:

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[8c56935967...](https://github.com/mrakgr/The-Spiral-Language/commit/8c56935967373a0e3104427f3d75cdce9a166c47)
#### Wednesday 2023-02-01 18:22:10 by Marko Grdinić

"12:45pm. Done with chores.

https://nyaa.si/view/1632150
Devour Eternity

The title caught my eye. Some chinese anime. Let me leave it for some other time.

https://news.ycombinator.com/item?id=34608883
https://www.xmodtwo.com/p/do-we-live-in-a-society-without-a
> It is a jarring contrast. At no point in history have people created so much with so few channels for consuming their work. Most consumers get their content through a narrow straw — TikTok’s “For You” page, the first page of Google’s search results, Instagram’s explore tab, miscellaneous streaming sites, and so on. Many lifetimes worth of creation get aggressively filtered down into a (very optimized) stream of content.

> Why do they all end their videos with “remember to like and subscribe?” Because it works, and Youtubers who don’t do it generally have fewer subscribers and generally get fewer views.

> This phenomenon isn’t new. What I’m describing is just a set of standards used to filter what makes it into the cultural mainstream. However, the capacity to enforce culture in such a rigorous, automated, and aggressive fashion is unprecedented. Imagine if all creative work was evaluated mathematically on its clickbaity-ness before it was allowed to become culturally relevant, and that’s my sense of where we are now.

Good article.

1:20pm. Done with breakfast.

1:30pm. Let me resume. First, let me try out the voice over feature.

https://youtu.be/kYPvm2alcPI
Recording Voice for YouTube / How I Record and Edit

Let me watch this.

My webcam mic is simply too sensitive. It camptures lip smacking sounds way better than my own ears would!

Why does it have to capture that!?

I need a simple solution. I see the voice over feature allows me to type in some text and recording right in the middle of the video without having to record it separately and import it. This is an improvement over my previous workflow.

1:50pm. You know, if I could just clip out the low intensity sounds to zero, that would completely take care of the smacking issues.

https://youtu.be/kYPvm2alcPI?t=241

He says he has the mic a food away from him. That is quite

https://www.google.com/search?q=how+to+deal+with+smacking+sounds+in+an+audio+recording
> Whenever there's a break in the recording, take another drink of water. Then, adjusting your microphone so that it's away at an angle from your mouth will ensure that the sounds of your lips smacking or other saliva-related sounds won't be as loud.

I can't really move the damn mic. It has to be on the top of my screen.

https://youtu.be/kYPvm2alcPI?t=647

Even without effects, his voice sounds perfect to me.

Let me try voice synthesis. When I tried exporting the audio and cancelled it, Camtasia crashed.

https://youtu.be/HF8472mcC3I
Adobe Premiere Pro - Removing smacking sounds from the audio

Actually before that, let me check this out.

https://youtu.be/HF8472mcC3I?t=62
> You do smack whenever you talk.

My problem is that I can't spend hours every time fixing this shit.

https://youtu.be/HF8472mcC3I?t=77

Yeah, it is exactly this. I need to take breath before taking and that is when it happens. I do not even notice it when I speak normally.

https://youtu.be/HF8472mcC3I?t=102

Ohhhhhhh, don't tell me he is doing it by hand!

https://podcastrocket.net/stop-lip-smacking-while-recording/#:~:text=Whenever%20there's%20a%20break%20in,won't%20be%20as%20loud.

This is ridiculous. Let me import the thing in Descript.

https://help.descript.com/hc/en-us/articles/10327603613837
Studio Sound

Can I stop Descript from transcribing my files automatically.

2:20pm. I am trying to have it run the Studio Sound, and it is taking forever.

...It just says it is loading, but it is not doing anything.

https://www.gravyforthebrain.com/secrets-preventing-mouth-clicks/

While I was reading this, the Studio Sound filter in Descript got applied. And it completely took care of the clicking sounds! Yes, this is it!

FFFFFFFFFFFFuck! It exported like 12mb of empty audio instead of 20s, and it wasted my transcription time. For some reason what I spent yesterday was restored to 1h, but now it is gone again.

2:30pm. Yeah, it is almost perfect, but it is not in tune with the rest of the video.

3:15pm. This is so ridiculous.

3:20pm. I do not know what is going on, but Descript is being antsy about letting me import the full audio clip. For some reason it is restricting it to 5 seconds. So I'd need to transcribe it first before applying the studio effect. Right now I am exporting it as mp4 with full quality.

3:45pm. Ah, goddamit, for fuck's sake. I forgot that Descript cannot go up to 1080p in the free version.

I did a whole bunch of video edits, so I can't just export the audio back out. It took care of a lot of uh's and some duplications. But I really do not want to get the paid version.

3:50pm. There is another one of those things where I click on the button, but nothing is happening.

That is because the popup informing me that the publish was successful was behind the menu I was using.

Shoddy engineering.

4pm. https://youtu.be/4YgbxnUuZrA
How To Get Models From HuggingFace And CivitAI (Part 2)

Here is my masterpiece.

Arguably even if it takes care of the clicking, the audio quality is still not that good. It does a bit like it is in a tube.

The good thing about all this is that it did allow me to upload to Youtube. I have the watermark removing option just for a single video.

4:05pm. Ok, for the future videos, I will just leave in the clicks. Worrying about this is not worth my time. The viewers will get used to it. What I am going to do is do the voice overs instead of doing it all at once.

4:10pm. Got a reply from the robotics guy. It is a nice little interaction. This job site he shared with me, I hadn't known about.

///

Hey Marko, how are you?

> Yes. It would be too much for a shut-in loner like myself to move countries all of a sudden. I want to stay where I am with my parents.
Totally get it. Unfortunately this reduces the chances of being able to join our company. Although there are many other options out there as you know. e.g. https://www.remoterocketship.com/

> reinventing partial evaluation on my own was quite hard
wow :) you are smart and hard working! very impressive

> But I think what is hard is always the same thing, keeping the motivation up
This is so true. No one is really unbroken. Everyone's journey includes periods like the ones you describe. Curiosity is one of my main motivators, and this is tricky because there's always a new shiny thing to be learned... I keep changing directions. But at least now I'm a bit more confined - it has to include software :)

> And then I am going to do a series on making an ML library and reinforcement learning in Spiral. I have an idea for a novel algorithm, and I might as well do it live this time.
Can you share the link? Would love to watch it

> UPMEM
Great, well done for reaching out to them! Any updates from their end? Have you asked them if a face to face presentation is what they need? And are they open to hiring or sponsoring you based on this presentation?

> I'll do it in the most straightforward way possible. I'll use tabular CFR which I know works well, and train the network using either evolution or a clustering approach I just thought up like during the night. When I get better hardware, I'll be able to make a genetic programming system to automate the architecture search and such
Sounds like a (great) plan!

> You've mentioned robotics a couple of times now. What kinds of algorithms are you guys using? When I think of robotics, the first thing that comes to mind is PIMCO. Though that thing uses Gaussian Processes and has O(n^3) scaling. There are also linear approaches that use Newtonian optimization, I forgot what they were called. At the other end you have evolutionary approaches that are a lot less sample efficient, but you could make them work if you have good enough simulators. What kinds of robots are you guys making? If it is industrial robots, there you can constrain the environment and even hand craft the rules. If it is not, then you have a hard problem. Right now, even the hardware to make use of them in natural settings does not exist.
We use industrial robots mostly to do pick and place in logistics warehouses. But we don't build them. Your intuition is correct - we focus on the segmentation task (and don't even do object detection), don't use RL and make use of hand craft rules in our stack. We basically get an image of a bin with objects inside and output a grasp (position and rotation) for the robots to grab the objects.

As I mentioned before, it would be so cool if it was easier to do RL in robotics. But these robots are expensive. And as you know, doing RL isn't cheap either. Found this project that could be cool to explore (https://github.com/isl-org/OpenBot) and I'm now waiting for my robot. But it'd be great if there was a web based platform where I could go and do these experiments. Maybe initially in simulation and then (somehow) in the real-world. Where it would be easy to share code/models/datasets. Catering for people like you and me, where things aren't so expensive. A platform that uses hardware like the one you describe. And not just for robotics. This should exist!

> Maybe if we end up working in the same company I would not mind sharing...
Now we're talking :D

///

Let me reply.

///

> Can you share the link? Would love to watch it

Playlist: https://www.youtube.com/playlist?list=PL04PGV4cTuIVGO5ImYTk9wPVmbgdYbe7J

This is on how to set up Stable Diffusion on Paperspace. I am doing this as practice. So far, the hardest thing is doing the video and sound editing afterwards. It takes me 5h to edit a 10m video which is insane. I am going to try just first doing a screencast, and then recording a voice over separately instead of doing it at the same time and fixing it during editing. I see that Camtasia has a handy menu in which I can type out a script that I can enlarge and hold in front. The way I am doing it now is stupid. Trying to come out fluent at the same time I am focusing on whatever I am doing on the computer is really hard.

I can't get rid of the inhales and mouth clicking without a huge editing effort. The two programs I've found that can transcribe text and edit it interactively as well as correct audio: Descript and Audiate, I do not want to buy. I think getting a better mic and placing it properly would help a lot, but I can't move my webcam anywhere else right now.

This is supposed to be talking practice for me, but 95% of what I am doing now is video editing. I probably spent over 20h doing this in the past week for 3/4th of an hour of video content produced.

Hmmmm...well, my father is a musician on the side, so I should just ask him for help in this case.

I know I said I would do RL programming in Spiral, but I just wanted to do something lighter as my first project. You'll see background noise in my first Intro video. I didn't even know Camtasia had a function to correct for that. I am using this initial project to find a good workflow first. I'll keep doing this until I find a job, so I do not know whether I'll get to the ‘Programming in Spiral’ parts.

Incidentally, because I am doing things off the cuff, I keep forgetting to ask people to like and subscribe. So please do that, if you watch the videos :)

> Great, well done for reaching out to them! Any updates from their end? Have you asked them if a face to face presentation is what they need? And are they open to hiring or sponsoring you based on this presentation?

No. Maybe they are checking out the language in secret, but given that I didn't get a reply to the email I sent them, this should be the end of that. I am not that interested in UPMEM's hardware anyway. I did tell them that since they have weak floating point support and no DPU inter communication, that their hardware does not interest me personally, but I'd be willing to work for them anyway. Maybe they took offense to that, who knows? It is hard to interpret internet silence.

Honestly, it is hard to know when somebody will take offense to something. For example, that compiler dev who pointed me at the SDK said that he would answer my questions within the energy limit, but ghosted me without even putting in 5m of work. That was some energy! Did he take offense to me barraging him with questions? Did he not like me expressing my options on UPMEM's persistent use of global variables in their examples? Who knows.

That company is not going to go anywhere. Right now, it is marketing itself as a leader in PIM hardware, and it is right about that. But that is because all of its competitors still haven't commercialized their products. When they do, they will kill it. If

> As I mentioned before, it would be so cool if it was easier to do RL in robotics. But these robots are expensive. And as you know, doing RL isn't cheap either. Found this project that could be cool to explore (https://github.com/isl-org/OpenBot) and I'm now waiting for my robot. But it'd be great if there was a web based platform where I could go and do these experiments. Maybe initially in simulation and then (somehow) in the real-world. Where it would be easy to share code/models/datasets. Catering for people like you and me, where things aren't so expensive. A platform that uses hardware like the one you describe. And not just for robotics. This should exist!

Hmmmm, let me say - RL requires a ton of trials, so if you think a real world robot is going to be learning anything, you are bound for disappointment. All current RL algorithms have major issues in several areas, and despite the SD/ChatGPT AI hype, aren't enough to approach the learning capability of biological creatures. Your best bet of achieving success is what you mentioned in one of our first emails - imitation learning from examples, like what Google did. Back in 2015, Deepmind did this as well with AlphaGo, they gave it expert examples to start it off because learning from scratch with RL is finicky. Later they ditched that, but it doesn't mean it was a bad idea. Still, imitation learning itself is likely to require a lot of data too, much like RL.

You are really passionate about this so go for it. You are in a better position than me either way to make something of it. How did you become a software dev from a doctor? Was it a doctor of computer science?

> Although there are many other options out there as you know. e.g. https://www.remoterocketship.com/

I will check out that job site you've linked me to, I didn't know about it. Thanks.

///

5pm. Let me reply with this.

5:05pm. Now let me do another video. I had in my first take, but then it got lost.

5:45pm. Now that I am starting a new project it is amazing how much more responsive Camtasia is! It is much much fater, when the amount of riple deleters is small.

> Hello, this is Ghostlike. In this part of the series, I wanted to show you just how you can clear out the outputs from persistent storage. Free tiers have a 5gb limit, Pro tiers have a 15Gb limit and Growth tiers aren't unlimited either. I've mentioned before that Paperspace has very small storage limits relative what you would have on a personal computer, so in this video I want to teach you how you can free up used space.

Let me save the narration segments here.

5:50pm. I am confusing myself, but this should be a good workflow. Write something out, then dub it. Do it me.

> As you prompt and generate images, especially if you are upscaling, your persistent storage space will rapidly get filled up.
> For that reason, it is important to know how to delete files in order to dispose of them and free up used storage space.

This kind of workflow will make me seem a lot more eloquent. In the previous videos, it might seem like I am retarded.

> Let's get started.
> Here I just use the starter script to fetch the Paperspace GPU machine instance. If you aren't familiar with this, check out one of my earlier videos.
> This time I was lucky and got an instance right away. The expected time depends on your time zone; whether you are in the US or Europe, and it depends on which day of the week it is. I'd expect the instances would be harder to get on Saturday and Sunday.
> Right now, I am loging into my Paperspace account.
> You just click on the project, click on the Notebook and it will take you into the Console.
> Since the subject of this tutorial is how to delete files, we need to do that from the terminal.
> It is possible to do this from the File Browser as well, but it is very bare bones. While it is possible to delete individual files, it will refuse to do so for the non-empty directories. The terminal is much more convenient as you will see.
> Right now, I am looking up how to get the directory and file sizes on Stack Exchange. You'll see that this gives us some confusing results.
> I'll just paste the command into the terminal using Ctrl + V.
> This kind of output confused me at first, but I realized that the storage directory has a size of 512 bytes for the simple reason that this is the size of the sym link.
> I'll show how to get the actual size later.

7:15pm. Let me close here for the day.

Yeah, this is. I've only made 2m of audio recordings, but my voice is crisp and fluent. I do not have trouble with uhms, moutch clicking or breath intaking anymore. Camtasia isn't struggling under the burden of a thousand of ripple deletes. This workflow is far more comfotable. I want to practice this for a while. A couple of days of this, and I will be ready to start interviewing.

Right now I am really tired.

After I feel proficient in this, I am going to switch to voice synthesis, but for now I am going to be doing them myself."

---
## [tonyvitonis/git](https://github.com/tonyvitonis/git)@[69bbbe484b...](https://github.com/tonyvitonis/git/commit/69bbbe484ba10bd88efb9ae3f6a58fcc687df69e)
#### Wednesday 2023-02-01 18:26:31 by Jeff King

hash-object: use fsck for object checks

Since c879daa237 (Make hash-object more robust against malformed
objects, 2011-02-05), we've done some rudimentary checks against objects
we're about to write by running them through our usual parsers for
trees, commits, and tags.

These parsers catch some problems, but they are not nearly as careful as
the fsck functions (which make sense; the parsers are designed to be
fast and forgiving, bailing only when the input is unintelligible). We
are better off doing the more thorough fsck checks when writing objects.
Doing so at write time is much better than writing garbage only to find
out later (after building more history atop it!) that fsck complains
about it, or hosts with transfer.fsckObjects reject it.

This is obviously going to be a user-visible behavior change, and the
test changes earlier in this series show the scope of the impact. But
I'd argue that this is OK:

  - the documentation for hash-object is already vague about which
    checks we might do, saying that --literally will allow "any
    garbage[...] which might not otherwise pass standard object parsing
    or git-fsck checks". So we are already covered under the documented
    behavior.

  - users don't generally run hash-object anyway. There are a lot of
    spots in the tests that needed to be updated because creating
    garbage objects is something that Git's tests disproportionately do.

  - it's hard to imagine anyone thinking the new behavior is worse. Any
    object we reject would be a potential problem down the road for the
    user. And if they really want to create garbage, --literally is
    already the escape hatch they need.

Note that the change here is actually in index_mem(), which handles the
HASH_FORMAT_CHECK flag passed by hash-object. That flag is also used by
"git-replace --edit" to sanity-check the result. Covering that with more
thorough checks likewise seems like a good thing.

Besides being more thorough, there are a few other bonuses:

  - we get rid of some questionable stack allocations of object structs.
    These don't seem to currently cause any problems in practice, but
    they subtly violate some of the assumptions made by the rest of the
    code (e.g., the "struct commit" we put on the stack and
    zero-initialize will not have a proper index from
    alloc_comit_index().

  - likewise, those parsed object structs are the source of some small
    memory leaks

  - the resulting messages are much better. For example:

      [before]
      $ echo 'tree 123' | git hash-object -t commit --stdin
      error: bogus commit object 0000000000000000000000000000000000000000
      fatal: corrupt commit

      [after]
      $ echo 'tree 123' | git.compile hash-object -t commit --stdin
      error: object fails fsck: badTreeSha1: invalid 'tree' line format - bad sha1
      fatal: refusing to create malformed object

Signed-off-by: Jeff King <peff@peff.net>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [qgustavor/mkv-extract](https://github.com/qgustavor/mkv-extract)@[7883822ccb...](https://github.com/qgustavor/mkv-extract/commit/7883822ccb3c35b479bc6171b1c8ae1e5d0944fe)
#### Wednesday 2023-02-01 18:48:23 by qgustavor

UX improvements

Should work with larger files (probably), with third party cookies blocked, metadata format should follow FFprobe's and UI should be a bit better now.

Also increase rants about the File System API: it kinda remembers me new ActiveXObject("Microsoft.XMLHTTP"): a bad solution that nobody now uses but at that time was the only one for that problem and the one that people had to use. Good thing that Microsoft created it, but we moved from that! When will that new FS Standard get forward? No pressure but... yeah.

---
## [EMACC99/black](https://github.com/EMACC99/black)@[0019261abc...](https://github.com/EMACC99/black/commit/0019261abcf6d9e564ba32d3cc15534b9026f29e)
#### Wednesday 2023-02-01 20:02:22 by Richard Si

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
## [EgorBo/runtime-1](https://github.com/EgorBo/runtime-1)@[1412ee7643...](https://github.com/EgorBo/runtime-1/commit/1412ee76430e8c2d4319e418ab46bfb1af5b839f)
#### Wednesday 2023-02-01 20:14:53 by Vitek Karas

Enable basic Kept validation in NativeAOT running linker tests (#78828)

This implements basic Type and Method Kept attribute validation.
It adds a `KeptBy` property on all `KeptAttribute` which uses the same `ProducedBy` enum to specify exceptions for each target product. (Eventually after the source merge we should rename `ProducedBy` enum to just `Tool` or `Platform`, but it's not important and I didn't want to do it here as it would be a giant diff).

The validation is done by going over all `ConstructedEETypeNode` and `IMethodBodyNode` nodes in the final graph and remembers that list. Then it compares that list to the expected kept members as per the attributes in tests. There are some tweaks:
* Filters out all compiler added types/members
* Doesn't track generic instantiations - only remember definition
* If a method body is kept, then it behaves as if the type is also kept even though there's no `ConstructedEETypeNode` - this is technically wrong (since NativeAOT can remove the type if for example only static methods are used from it), but it would require major changes to the linker tests (since in IL this is a necessity). If we ever need precise validation of this, we would probably add a new attribute to check just for this.

I also copied all of the "other assemblies" kept validation code from ResultChecker (were it lives in linker) to AssemblyChecker where it will need to be to actually work (and where it should probably be anyway). That code is not used yet.

Left lot of TODO/commented out code in the AssemblyChecker - lots of other validation to enable eventually.

Fixed/adapted all of the tests which were already ported to NativeAOT to pass with this new validation.
Removed a test for unresolved members, since it actually fails NativeAOT compilation, so it doesn't test anything really.

One tiny product change:
Display names now consistently include all parent types when writing out nested type names. ILLink already does this and NativeAOT was a bit inconsistent. Since the display names are used only in diagnostics, this brings the diagnostics experience closer between the two tools. The added benefit is that we can use display names to compare members between Cecil and Internal.TypeSystem more precisely.

Co-authored-by: Tlakaelel Axayakatl Ceja <tlakaelel.ceja@microsoft.com>

---
## [belalth/LibraryManegmentSystem](https://github.com/belalth/LibraryManegmentSystem)@[c3c59ad5a8...](https://github.com/belalth/LibraryManegmentSystem/commit/c3c59ad5a8d2431c5320960615a1efb164a0dace)
#### Wednesday 2023-02-01 20:34:56 by Belal A

	deleted:    .idea/ant.xml
	modified:   .idea/misc.xml
	new file:   fuck you .txt

---
## [dforsi/chirp](https://github.com/dforsi/chirp)@[12301814e2...](https://github.com/dforsi/chirp/commit/12301814e238458766f1f7bf06476b39a4e3ab93)
#### Wednesday 2023-02-01 21:01:30 by Dan Smith

Remove myGMRS query source

I was hesitant to add this because the owner expressed some desire to
convert this to a paid-only feature in the future. However, he
assured me it would remain available to non-premium members in order
to enable CHIRP support, so I put it in. Now, nine days after it was
available in a build, the story has changed and the feature will be
restricted to premium-only users, contrary to the original agreement.

We have one other paid-only query source in CHIRP and that is
RadioReference. It's quite a pain because only developers with premium
accounts can work on that code, which has been a problem ever since we
added it. However, RadioReference is huge and undeniably worth the
trouble. Since myGMRS is ... not that, I'm removing it so we don't
end up with a long-lived feature that we can't maintain.

---
## [Danielkaas94/DTAP](https://github.com/Danielkaas94/DTAP)@[ffb47760f5...](https://github.com/Danielkaas94/DTAP/commit/ffb47760f513e5878950ea362e05c30cc4bf2bd4)
#### Wednesday 2023-02-01 22:19:03 by Daniel Kaas Bundgaard Jørgensen

💥 Collapsing 💥
I, I see the weight of hollow death residing in you
Take now your final breath
Exhale the truth
I see the fear of nothing left
Dead fragments of youth
You hold it in yourself
I feel it too

I mourn your blindness
I die along
And swallow darkness
In misery is where I belong

Collapsing in on yourself
I don't know why I try (I try)
Collapsing in on yourself
I don't know why you deny

I, I know the light is burning dim and dying in you
I know the pain that lies within
I feel it too

I mourn your blindness
I die along
And swallow darkness
In misery is where I belong

Collapsing in on yourself
I don't know why I try (I try)
Collapsing in on yourself
I don't know why you deny

Collapsing in on yourself
I don't know why I try (I try)
Collapsing in on yourself
I don't know why you deny

Collapsing in on yourself
I don't know why I try (I try)
Collapsing in on yourself
I don't know why you deny

---
## [Goldspear/pytorch](https://github.com/Goldspear/pytorch)@[5c6f5439b7...](https://github.com/Goldspear/pytorch/commit/5c6f5439b7e6a5e63a68b36b4cf093a00d46e8be)
#### Wednesday 2023-02-01 23:08:04 by Edward Z. Yang

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
## [Danielkaas94/DTAP](https://github.com/Danielkaas94/DTAP)@[485cd3ff8a...](https://github.com/Danielkaas94/DTAP/commit/485cd3ff8a413756e9c6428f0995b2075bc7dfb6)
#### Wednesday 2023-02-01 23:15:39 by Daniel Kaas Bundgaard Jørgensen

🌟⭐ All Star ⭐🌟 - ArtArtemis 🏹🎯
Somebody once told me
The world is gonna roll me
I ain't the sharpest tool in the shed
She was looking kind of dumb
With her finger and her thumb
In the shape of an "L" on her forehead

Well, the years start coming
And they don't stop coming
Fed to the rules and I hit the ground running
Didn't make sense not to live for fun
Your brain gets smart, but your head gets dumb

So much to do, so much to see
So what's wrong with taking the back streets?
You'll never know if you don't go
You'll never shine if you don't glow

Hey now, you're an all star
Get your game on, go play
Hey now, you're a rock star
Get the show on, get paid
And all that glitters is gold
Only shooting stars break the mold

It's a cool place and they say it gets colder
You're bundled up now, wait 'til you get older
But the meteor men beg to differ
Judging by the hole in the satellite picture

The ice we skate is getting pretty thin
The water's getting warm so you might as well swim
My world's on fire, how about yours?
That's the way I like it and I never get bored

Hey now, you're an all star
Get your game on, go play
Hey now, you're a rock star
Get the show on, get paid
All that glitters is gold
Only shooting stars break the mold

(Go for the moon, go, go)
(Go for the moon, go, go)
(Go for the moon)
(Go, go, go for the moon)

Hey now, you're an all star
Get your game on, go play
Hey now, you're a rock star
Get the show on, get paid
And all that glitters is gold
Only shooting stars

Somebody once asked
"Could I spare some change for gas?
I need to get myself away from this place"
I said, "Yep, what a concept
I could use a little fuel myself"
And we could all use a little change

Well, the years start coming
And they don't stop coming
Fed to the rules and I hit the ground running
Didn't make sense not to live for fun
Your brain gets smart, but your head gets dumb

So much to do, so much to see
So what's wrong with taking the back streets?
You'll never know if you don't go (go!)
You'll never shine if you don't glow

Hey now, you're an all star
Get your game on, go play
Hey now, you're a rock star
Get the show on, get paid

And all that glitters is gold
Only shooting stars break the mold
And all that glitters is gold
Only shooting stars break the mold

---

