## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-11-12](docs/good-messages/2022/2022-11-12.md)


1,764,523 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,764,523 were push events containing 2,429,328 commit messages that amount to 154,326,964 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 30 messages:


## [ammarfaizi2/linux-fork](https://github.com/ammarfaizi2/linux-fork)@[93da89543d...](https://github.com/ammarfaizi2/linux-fork/commit/93da89543dffa7a2a0821ddc4452f500d2a5bf54)
#### Saturday 2022-11-12 00:16:20 by Dan Williams

fsdax: wait on @page not @page->_refcount

Patch series "Fix the DAX-gup mistake", v3.

ZONE_DEVICE was created to allow for get_user_pages() on DAX mappings.  It
has since grown other users, but the main motivation was gup and
synchronizing device shutdown events with pinned pages.  Memory device
shutdown triggers driver ->remove(), and ->remove() always succeeds, so
ZONE_DEVICE needed a mechanism to stop new page references from being
taken, and await existing references to drain before allowing device
removal to proceed.  This is the origin of 'struct dev_pagemap' and its
percpu_ref.

The original ZONE_DEVICE implementation started by noticing that 'struct
page' initialization, for typical page allocator pages, started pages at a
refcount of 1.  Later those pages are 'onlined' by freeing them to the
page allocator via put_page() to drop that initial reference and populate
the free page lists.  ZONE_DEVICE abused that "initialized but never
freed" state to both avoid leaking ZONE_DEVICE pages into places that were
not ready for them, and add some metadata to the unused (because refcount
was never 0) page->lru space.

As more users of ZONE_DEVICE arrived that special casing became more and
more unnecessary, and more and more expensive.  The 'struct page'
modernization eliminated the need for the ->lru hack.  The folio work had
to remember to sprinkle special case ZONE_DEVICE accounting in the right
places.  The MEMORY_DEVICE_PRIVATE use case spearheaded much of the work
to support typical reference counting for ZONE_DEVICE pages and allow them
to be used in more kernel code paths.  All the while the DAX case kept its
tech debt in place, until now.

However, while fixing the DAX page refcount semantics and arranging for
free_zone_device_page() to be the common end of life of all ZONE_DEVICE
pages, the mitigation for truncate() vs pinned DAX pages was found to be
incomplete.  Unlike typical pages that surprisingly can remain pinned for
DMA after they have been truncated from a file, the DAX core must enforce
that nobody has access to a page after truncate() has disconnected it from
inode->i_pages.  I.e.  the file block that is identical to the page still
remains an extent of the file.  The existing mitigation handled explicit
truncate while the inode was alive, but not the implicit truncate right
before the inode is freed.

So, in addition to moving DAX pages to be refcount-0 at idle, and add
'break_layouts' wakeups to free_zone_device_page(), this series also
introduces another occurrence of 'break_layouts' to the inode freeing
path.  Recall that 'break_layouts' for DAX is the mechanism to await code
paths that previously arbitrated page access to drop their interest /
page-pins.  This new synchronization point is implemented by special
casing dax_delete_mapping_entry(), called by truncate_inode_pages_final(),
to await page pins when mapping_exiting() is true.

Thanks to Jason for the nudge to get this fixed up properly and the review
on v1, Dave, Jan, and Jason for the discussion on what to do about the
inode end-of-life-truncate problem, and Alistair for cleaning up the last
of the refcount-1 assumptions in the MEMORY_DEVICE_PRIVATE users.


This patch (of 25):

The __wait_var_event facility calculates a wait queue from a hash of the
address of the variable being passed.  Use the @page argument directly as
it is less to type and is the object that is being waited upon.

Link: https://lkml.kernel.org/r/166579181584.2236710.17813547487183983273.stgit@dwillia2-xfh.jf.intel.com
Link: https://lkml.kernel.org/r/166579182271.2236710.15120970389485390592.stgit@dwillia2-xfh.jf.intel.com
Signed-off-by: Dan Williams <dan.j.williams@intel.com>
Reviewed-by: Jason Gunthorpe <jgg@nvidia.com>
Cc: Matthew Wilcox <willy@infradead.org>
Cc: Jan Kara <jack@suse.cz>
Cc: "Darrick J. Wong" <djwong@kernel.org>
Cc: Christoph Hellwig <hch@lst.de>
Cc: John Hubbard <jhubbard@nvidia.com>
Cc: Alex Deucher <alexander.deucher@amd.com>
Cc: Alistair Popple <apopple@nvidia.com>
Cc: Ben Skeggs <bskeggs@redhat.com>
Cc: Christian König <christian.koenig@amd.com>
Cc: Daniel Vetter <daniel@ffwll.ch>
Cc: Dave Chinner <david@fromorbit.com>
Cc: David Airlie <airlied@linux.ie>
Cc: Felix Kuehling <Felix.Kuehling@amd.com>
Cc: Jerome Glisse <jglisse@redhat.com>
Cc: Karol Herbst <kherbst@redhat.com>
Cc: Lyude Paul <lyude@redhat.com>
Cc: "Pan, Xinhui" <Xinhui.Pan@amd.com>
Cc: kernel test robot <lkp@intel.com>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>

---
## [kimhyr/KPLC](https://github.com/kimhyr/KPLC)@[79d8c9fac3...](https://github.com/kimhyr/KPLC/commit/79d8c9fac3363c4819c171b6e73641c82105ddc0)
#### Saturday 2022-11-12 00:32:34 by kimhyr

I FUCKING HATE ERROR HANDLING SHIT FUCK THIS FUCK YOU FUCK ME

---
## [masterr314/react](https://github.com/masterr314/react)@[b6978bc38f...](https://github.com/masterr314/react/commit/b6978bc38f6788c7e73982b9fd2771aabdf36f15)
#### Saturday 2022-11-12 02:07:05 by Andrew Clark

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
## [brain-tec/odoo](https://github.com/brain-tec/odoo)@[b7d53d2fcb...](https://github.com/brain-tec/odoo/commit/b7d53d2fcb20a447fd3098adf94ffb33bc49dda9)
#### Saturday 2022-11-12 03:12:55 by qsm-odoo

[FIX] website, *: allow to re-edit company team snippet images

*: website_sale

Since [1], it was not possible to edit a company team snippet image
anymore as soon as the page was saved once. Indeed that commit added
o_not_editable/contenteditable="false" on the parent column to make sure
no text can be added in that column and contenteditable="true" on the
images so that they are still editable (even though HTML-specs-wise
adding contenteditable="true" on images probably does not mean much as
images are self-closing tags, our editor understand that as the ability
to edit the image anyway). That contenteditable="true" part is however
removed when leaving edit mode... and was not restored upon entering
edit mode again.

This fixes the problems with a specific JS patch, we'll review to see if
better can be done in master.

Funny enough, that bug was actually gone in 15.0... by mistake. A recent
bug fix actually reintroduced that isolated bug at [2] (by reintroducing
the fact that images in a non-editable environment are not possible to
edit). The 3 opened tickets this commit mentions were actually reported
for 15.0 immediately after that, while the 14.0 being broken about this
since the beginning apparently did not bother anyone.

Note: as a forward-ported fix, this also takes the opportunity to clean
a bit what was done at [3]. (calling `_super`, no duplicated code,
adding comments, ...).

[1]: https://github.com/odoo/odoo/commit/656cac1bf21c7c5a56aa569008aac58436c747fb
[2]: https://github.com/odoo/odoo/commit/e113bae04a64a8bd341a80736086ab7c25079dd3
[3]: https://github.com/odoo/odoo/commit/e2f7b8fad76dc816b2f6864340d3740446117cdb

opw-3031217
opw-3032482
opw-3035289

closes odoo/odoo#104318

X-original-commit: 61270ee8bffb6e85f8ff0d19c7a3889fdce2f486
Signed-off-by: Romain Derie (rde) <rde@odoo.com>
Signed-off-by: Quentin Smetz (qsm) <qsm@odoo.com>

---
## [McF4r/bevy](https://github.com/McF4r/bevy)@[4847f7e3ad...](https://github.com/McF4r/bevy/commit/4847f7e3adc835053a8907dd578c342b4bd395e2)
#### Saturday 2022-11-12 03:13:19 by ira

Update codebase to use `IntoIterator` where possible. (#5269)

Remove unnecessary calls to `iter()`/`iter_mut()`.
Mainly updates the use of queries in our code, docs, and examples.

```rust
// From
for _ in list.iter() {
for _ in list.iter_mut() {

// To
for _ in &list {
for _ in &mut list {
```

We already enable the pedantic lint [clippy::explicit_iter_loop](https://rust-lang.github.io/rust-clippy/stable/) inside of Bevy. However, this only warns for a few known types from the standard library.

## Note for reviewers
As you can see the additions and deletions are exactly equal.
Maybe give it a quick skim to check I didn't sneak in a crypto miner, but you don't have to torture yourself by reading every line.
I already experienced enough pain making this PR :) 


Co-authored-by: devil-ira <justthecooldude@gmail.com>

---
## [thevandie/tgstation-1](https://github.com/thevandie/tgstation-1)@[32c2e4ccd3...](https://github.com/thevandie/tgstation-1/commit/32c2e4ccd3ee10b62a8f5d8e7ad3dbd1e33213ea)
#### Saturday 2022-11-12 03:16:41 by Fikou

gives medical ert a health analyzer (#70244)

* gives medical ert a health analyzer

* fuck you *upgrades your analyzer*

---
## [vnhanai/zulip](https://github.com/vnhanai/zulip)@[23a776c144...](https://github.com/vnhanai/zulip/commit/23a776c1448da18b906529e5951e24d8d58a7e81)
#### Saturday 2022-11-12 04:00:14 by Mateusz Mandera

maybe_send_to_registration: Don't reuse pre-existing PreregistraionUser.

There was the following bug here:
1. Send an email invite to a user.
2. Have the user sign up via social auth without going through that
   invite, meaning either going via a multiuse invite link or just
   straight-up Sign up if the org permissions allow.

That resulted in the PreregistrationUser that got generated in step (1)
having 2 Confirmations tied to it - because maybe_send_to_registration
grabbed the object and created a new confirmation link for it. That is a
corrupted state, Confirmation is supposed to be unique.

One could try to do fancy things with checking whether a
PreregistrationUser already have a Confirmation link, but to avoid races
between ConfirmationEmailWorker and maybe_send_to_registration, this
would require taking locks and so on - which gets needlessly
complicated. It's simpler to not have them compete for the same object.

The point of the PreregistrationUser re-use in
maybe_send_to_registration is that if an admin invites a user, setting
their initial streams and role, it'd be an annoying experience if the
user ends up signing up not via the invite and those initial streams
streams etc. don't get set up. But to handle this, we can just copy the
relevant values from the pre-existing prereg_user, rather than re-using
the object itself.

---
## [newstools/2022-daily-post-nigeria](https://github.com/newstools/2022-daily-post-nigeria)@[b00a1ad713...](https://github.com/newstools/2022-daily-post-nigeria/commit/b00a1ad713dafa657593968c2dc467ff259e3b9e)
#### Saturday 2022-11-12 04:47:11 by Billy Einkamerer

Created Text For URL [dailypost.ng/2022/11/11/16-year-old-boy-allegedly-rapes-brothers-wife-nine-girls-in-ondo/]

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[e3a02802cb...](https://github.com/treckstar/yolo-octo-hipster/commit/e3a02802cba32a0dbe93c46b0c3896b2cce95f11)
#### Saturday 2022-11-12 05:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [morrowwolf/cmss13](https://github.com/morrowwolf/cmss13)@[7cb69c2a8b...](https://github.com/morrowwolf/cmss13/commit/7cb69c2a8b6f8895d5475b709183a3f30d05fbeb)
#### Saturday 2022-11-12 06:24:27 by Joelampost

Creates a new tile for the predator ship (#1400)

* erm

* yer

* fuck you shaddeh

---
## [gitster/git](https://github.com/gitster/git)@[f1c903debd...](https://github.com/gitster/git/commit/f1c903debdcbf6aaf8fd3abf222fa941b42d5d31)
#### Saturday 2022-11-12 08:02:52 by Ævar Arnfjörð Bjarmason

cocci: make "coccicheck" rule incremental

Optimize the very slow "coccicheck" target to take advantage of
incremental rebuilding, and fix outstanding dependency problems with
the existing rule.

The rule is now faster both on the initial run as we can make better
use of GNU make's parallelism than the old ad-hoc combination of
make's parallelism combined with $(SPATCH_BATCH_SIZE) and/or the
"--jobs" argument to "spatch(1)".

It also makes us *much* faster when incrementally building, it's now
viable to "make coccicheck" as topic branches are merged down.

The rule didn't use FORCE (or its equivalents) before, so a:

	make coccicheck
	make coccicheck

Would report nothing to do on the second iteration. But all of our
patch output depended on all $(COCCI_SOURCES) files, therefore e.g.:

    make -W grep.c coccicheck

Would do a full re-run, i.e. a a change in a single file would force
us to do a full re-run.

The reason for this (not the initial rationale, but my analysis) is:

* Since we create a single "*.cocci.patch+" we don't know where to
  pick up where we left off, or how to incrementally merge e.g. a
  "grep.c" change with an existing *.cocci.patch.

* We've been carrying forward the dependency on the *.c files since
  63f0a758a06 (add coccicheck make target, 2016-09-15) the rule was
  initially added as a sort of poor man's dependency discovery.

  As we don't include other *.c files depending on other *.c files
  has always been broken, as could be trivially demonstrated
  e.g. with:

       make coccicheck
       make -W strbuf.h coccicheck

  However, depending on the corresponding *.c files has been doing
  something, namely that *if* an API change modified both *.c and *.h
  files we'd catch the change to the *.h we care about via the *.c
  being changed.

  For API changes that happened only via *.h files we'd do the wrong
  thing before this change, but e.g. for function additions (not
  "static inline" ones) catch the *.h change by proxy.

Now we'll instead:

 * Create a <RULE>/<FILE> pair in the .build directory, E.g. for
   swap.cocci and grep.c we'll create
   .build/contrib/coccinelle/swap.cocci.patch/grep.c.

   That file is the diff we'll apply for that <RULE>-<FILE>
   combination, if there's no changes to me made (the common case)
   it'll be an empty file.

 * Our generated *.patch
   file (e.g. contrib/coccinelle/swap.cocci.patch) is now a simple "cat
   $^" of all of all of the <RULE>/<FILE> files for a given <RULE>.

   In the case discussed above of "grep.c" being changed we'll do the
   full "cat" every time, so they resulting *.cocci.patch will always
   be correct and up-to-date, even if it's "incrementally updated".

   See 1cc0425a27c (Makefile: have "make pot" not "reset --hard",
   2022-05-26) for another recent rule that used that technique.

As before we'll:

 * End up generating a contrib/coccinelle/swap.cocci.patch, if we
   "fail" by creating a non-empty patch we'll still exit with a zero
   exit code.

   Arguably we should move to a more Makefile-native way of doing
   this, i.e. fail early, and if we want all of the "failed" changes
   we can use "make -k", but as the current
   "ci/run-static-analysis.sh" expects us to behave this way let's
   keep the existing behavior of exhaustively discovering all cocci
   changes, and only failing if spatch itself errors out.

Further implementation details & notes:

 * Before this change running "make coccicheck" would by default end
   up pegging just one CPU at the very end for a while, usually as
   we'd finish whichever *.cocci rule was the most expensive.

   This could be mitigated by combining "make -jN" with
   SPATCH_BATCH_SIZE, see 960154b9c17 (coccicheck: optionally batch
   spatch invocations, 2019-05-06).

   There will be cases where getting rid of "SPATCH_BATCH_SIZE" makes
   things worse, but a from-scratch "make coccicheck" with the default
   of SPATCH_BATCH_SIZE=1 (and tweaking it doesn't make a difference)
   is faster (~3m36s v.s. ~3m56s) with this approach, as we can feed
   the CPU more work in a less staggered way.

 * Getting rid of "SPATCH_BATCH_SIZE" particularly helps in cases
   where the default of 1 yields parallelism under "make coccicheck",
   but then running e.g.:

       make -W contrib/coccinelle/swap.cocci coccicheck

   I.e. before that would use only one CPU core, until the user
   remembered to adjust "SPATCH_BATCH_SIZE" differently than the
   setting that makes sense when doing a non-incremental run of "make
   coccicheck".

 * Before the "make coccicheck" rule would have to clean
   "contrib/coccinelle/*.cocci.patch*", since we'd create "*+" and
   "*.log" files there. Now those are created in
   .build/contrib/coccinelle/, which is covered by the "cocciclean" rule
   already.

Outstanding issues & future work:

 * We could get rid of "--all-includes" in favor of manually
   specifying a list of includes to give to "spatch(1)".

   As noted upthread of [1] a naïve removal of "--all-includes" will
   result in broken *.cocci patches, but if we know the exhaustive
   list of includes via COMPUTE_HEADER_DEPENDENCIES we don't need to
   re-scan for them, we could grab the headers to include from the
   .depend.d/<file>.o.d and supply them with the "--include" option to
   spatch(1).q

1. https://lore.kernel.org/git/87ft18tcog.fsf@evledraar.gmail.com/

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>
Signed-off-by: Taylor Blau <me@ttaylorr.com>

---
## [EldritchCarMaker/My-Subnautica-Mods](https://github.com/EldritchCarMaker/My-Subnautica-Mods)@[6dcd299d11...](https://github.com/EldritchCarMaker/My-Subnautica-Mods/commit/6dcd299d11f3a82917f92fd53676d95a5e82b19a)
#### Saturday 2022-11-12 08:39:37 by Nagorrogan

quantum base updates and armor suit

updates to quantum base, don't remember what they were and fuck no I'm not looking through it right now you can find it on your own

added armor suit, does fancy shit, yay (name subject to change)

updated equippable item icons to allow for more versatility with said armor suit

---
## [Cube-Enix/SN-Edit](https://github.com/Cube-Enix/SN-Edit)@[919da2c5ac...](https://github.com/Cube-Enix/SN-Edit/commit/919da2c5ac24f7bfe68c67f095fc4dbbce040c4c)
#### Saturday 2022-11-12 09:29:57 by SithLor

fuck you webpack you piss me ALLway NO IMPORT ONE SCRIPT DIE

---
## [metterschlg/android_kernel_samsung_universal5433](https://github.com/metterschlg/android_kernel_samsung_universal5433)@[6857fc18aa...](https://github.com/metterschlg/android_kernel_samsung_universal5433/commit/6857fc18aa89fda8a845f830dc10a99bee3890e6)
#### Saturday 2022-11-12 09:52:11 by Masahiro Yamada

modpost: file2alias: go back to simple devtable lookup

commit ec91e78d378cc5d4b43805a1227d8e04e5dfa17d upstream.

* Fixes scripts/mod/file2alias.c:374:1: warning: adding 'unsigned long' to a string does not append to the string [-Wstring-plus-int]
ADD_TO_DEVTABLE("hid", hid_device_id, do_hid_entry); and 30 other errors

* Remove mipscdmm cpu rapidio ulpi hdaudio from devtable as they do not exist in our kernel

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
Change-Id: I39b197f7e454eefc9fbd5ed5c2cb97f107f08094

---
## [QuantumApprentice/Fallout-Nevada-Translation](https://github.com/QuantumApprentice/Fallout-Nevada-Translation)@[41e4d68ed9...](https://github.com/QuantumApprentice/Fallout-Nevada-Translation/commit/41e4d68ed947e8c09d58ca0047fc0a47899054d0)
#### Saturday 2022-11-12 10:17:33 by QuantumApprentice

"don't even try to squeak"

{156}{}{Our guys won't let you get away with this bullshit. Shut the fuck up and don't even try to squeak about our brotherhood.
Is the "don't even try to squeak" part intentional?
I swapped it out for "don't even make a peep", because it seems pretty close and is more common.

---
## [pen787/EU-to-RF-Converter](https://github.com/pen787/EU-to-RF-Converter)@[da45a41af9...](https://github.com/pen787/EU-to-RF-Converter/commit/da45a41af998e56c4bb6fa3d151cb41384a4df5a)
#### Saturday 2022-11-12 10:54:04 by pen787

change the namespace and other thing idk i hate my life

---
## [yourdoom9898/Citadel-Station-13-RP](https://github.com/yourdoom9898/Citadel-Station-13-RP)@[24aca0ae55...](https://github.com/yourdoom9898/Citadel-Station-13-RP/commit/24aca0ae55ce2204474ec23fed6d23cb46b6645e)
#### Saturday 2022-11-12 11:35:53 by LordPapalus

Cargonia, but with less weapons (#4370)

* Cargonia is no more

Fuck you

* PLEASE

* Zandario, I will suck your PP

---
## [blackcrystall/cmi](https://github.com/blackcrystall/cmi)@[ca2114f0f5...](https://github.com/blackcrystall/cmi/commit/ca2114f0f56ab4a51443bdac52053ead327724dc)
#### Saturday 2022-11-12 13:58:46 by Mister-moon1

Removes some useless code from welding helmet (#1363)

* fuck you useless code

* you cannot hide, useless code

---
## [Damien2417/SubnauticaBZMultiplayerMod](https://github.com/Damien2417/SubnauticaBZMultiplayerMod)@[c91b28b2eb...](https://github.com/Damien2417/SubnauticaBZMultiplayerMod/commit/c91b28b2eb67ed568196d09bed58784a909145a0)
#### Saturday 2022-11-12 17:44:38 by V E L Δ

New ID system WORKS HOLY SHIT.
No for real I would have never expected it would
work so fast damn

---
## [GeoB99/reactos](https://github.com/GeoB99/reactos)@[293c7f26ed...](https://github.com/GeoB99/reactos/commit/293c7f26ed6c52463277a0e75ce6b66e3d79197e)
#### Saturday 2022-11-12 18:17:16 by George Bișoc

[SDK][CMLIB] Implement log transaction writes & Resuscitation

=== DOCUMENTATION REMARKS ===

This implements (also enables some parts of code been decayed for years) the transacted writing of the registry. Transacted writing (or writing into registry in a transactional way) is an operation that ensures the successfulness can be achieved by monitoring two main points.
In CMLIB, such points are what we internally call them the primary and secondary sequences. A sequence is a numeric field that is incremented each time a writing operation (namely done with the FileWrite function and such) has successfully completed.

The primary sequence is incremented to suggest that the initial work of syncing the registry is in progress. During this phase, the base block header is written into the primary hive file and registry data is being written to said file in form of blocks. Afterwards the seconady sequence
is increment to report completion of the transactional writing of the registry. This operation occurs in HvpWriteHive function (invoked by HvSyncHive for syncing). If the transactional writing fails or if the lazy flushing of the registry fails, LOG files come into play.

Like HvpWriteHive, LOGs are updated by the HvpWriteLog which writes dirty data (base block header included) to the LOG themselves. These files serve for recovery and emergency purposes in case the primary machine hive has been damaged due to previous forced interruption of writing stuff into
the registry hive. With specific recovery algorithms, the data that's been gathered from a LOG will be applied to the primary hive, salvaging it. But if a LOG file is corrupt as well, then the system will perform resuscitation techniques by reconstructing the base block header to reasonable values,
reset the registry signature and whatnot.

This work is an inspiration from PR #3932 by mrmks04 (aka Max Korostil). I have continued his work by doing some more tweaks and whatnot. In addition to that, the whole transaction writing code is documented.

=== IMPORTANT NOTES ===

HvpWriteLog -- Currently this function lacks the ability to grow the log file size since we pretty much lack the necessary code that deals with hive shrinking and log shrinking/growing as well. This part is not super critical for us so this shall be left as a TODO for future.

HvLoadHive -- Currently there's a hack that prevents us from refactoring this function in a proper way. That is, we should not be reading the whole and prepare the hive storage using HvpInitializeMemoryHive which is strictly used for HINIT_MEMORY but rather we must read the hive file block by block
and deconstruct the read buffer from the file so that we can get the bins that we read from the file. With the hive bins we got the hive storage will be prepared based on such bins. If one of the bins is corrupt, self healing is applied in such scenario.

For this matter, if in any case the hive we'll be reading is corrupt we could potentially read corrupt data and lead the system into failure. So we have to perform header and data recovery as well before reading the whole hive.

---
## [UdL-EPS-SoftArch/mycircular-api](https://github.com/UdL-EPS-SoftArch/mycircular-api)@[b1a988cfb1...](https://github.com/UdL-EPS-SoftArch/mycircular-api/commit/b1a988cfb1560e64239238252a9ba8f237affd37)
#### Saturday 2022-11-12 18:28:04 by VictorMateu

all updaterequest tests done (i hate my life and starting hate my MAC)

---
## [brandon1024/.dotfiles](https://github.com/brandon1024/.dotfiles)@[dab398466c...](https://github.com/brandon1024/.dotfiles/commit/dab398466c5b635722819bf4a22e28af48c7a2fd)
#### Saturday 2022-11-12 18:35:48 by Brandon Richardson

taking the tabline intergalactic

I love my tabline setup, but it had one annoying flaw. The tabline fills
up quickly when you have a lot of buffers open, and when there are too
many buffers, the beginning of the tabline is truncated. It looks pretty
ugly when that happens, and sometimes you can't see the curent buffer
because it's in that part that is truncated.

This new revision takes the tabline to a whole new level. When there are
too many buffers and we can't show them all in the tabline, the extras
are dropped. If they can't be shown, a pretty scroll marker is shown.
Additionally, we try to keep the current buffer centered so that it's
always visible.

She's a beaut, Clark.

---
## [CreativePenguin/pokemon-badge-collector](https://github.com/CreativePenguin/pokemon-badge-collector)@[d04263c9e8...](https://github.com/CreativePenguin/pokemon-badge-collector/commit/d04263c9e8b683cbb637d9dbd1718182a6d95a74)
#### Saturday 2022-11-12 18:51:36 by Winston Peng

OH MY GOD IT WORKS, YOU GO TO THE URL AND IT SETS THE COOKIE. FUCK YEAH. TAKE THAT DAD! LOOK AT ME NOW

---
## [e-kwsm/swig](https://github.com/e-kwsm/swig)@[9908f9f310...](https://github.com/e-kwsm/swig/commit/9908f9f310aeadb129b41d14d40de9f2163ffa24)
#### Saturday 2022-11-12 19:04:32 by Olly Betts

[php] Fix testcase segfaults with PHP 8.0

These testcases were segfaulting:

prefix
director_using_member_scopes
virtual_poly

The fix here is admittedly a hack - we perform the initialisation
of EG(class_table) from CG(class_table) which PHP will do, but
hasn't yet.

PHP doesn't seem to clearly document which API calls are actually
valid in minit or other initialisation contexts, but the code we're
generating works with all PHP 7.x and PHP 8.x versions aside from PHP
8.0 so it seems this is a bug in PHP 8.0 rather than that we're doing
something invalid, and we need to work with existing PHP 8.0 releases
so this hack seems a necessary evil.  It will at least have a limited
life as PHP 8.0 is only in active support until 2022-11-26, with
security support ending a year later.

Fixes #2383.

---
## [olloeco/community](https://github.com/olloeco/community)@[7a575617d3...](https://github.com/olloeco/community/commit/7a575617d3da9ddfcadd8a14613611a48d53122a)
#### Saturday 2022-11-12 20:07:57 by Seth Ward

(Mostly) style updates to the corporate policy

Revisions pre-62: improving style consistency (I'm a lawyer who has editing thousands of pages of academic scholarship)
62: Corporations should be able to promote a message as long as it's with new content. If they're on a campaign to save the world, they should be able to share content that conveys that message. I see what we're getting at with the policy, but this isn't quite the same as Wikipedia; normal life has some repetitive rhythms, and Mastadon isn't a reference site like Wikipedia. Repetitive product marketing is annoying as hell, and under the remaining terms set forth in the policy, the mods will be able to show anyone the door for violation of other principles set forth in the policy.
Post-62: Clarifying comments and usage fixes.

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[eb20e63f5a...](https://github.com/git-for-windows/git/commit/eb20e63f5a96e24852c6ab1eca9f96af2648802f)
#### Saturday 2022-11-12 20:25:03 by Jeff King

branch: gracefully handle '-d' on orphan HEAD

When deleting a branch, "git branch -d" has a safety check that ensures
the branch is merged to its upstream (if any), or to HEAD. To do that,
naturally we try to resolve HEAD to a commit object. If we're on an
orphan branch (i.e., HEAD points to a branch that does not yet exist),
that will fail, and we'll bail with an error:

  $ git branch -d to-delete
  fatal: Couldn't look up commit object for HEAD

This usually isn't that big of a deal. The deletion would fail anyway,
since the branch isn't merged to HEAD, and you'd need to use "-D" (or
"-f"). And doing so skips the HEAD resolution, courtesy of 67affd5173
(git-branch -D: make it work even when on a yet-to-be-born branch,
2006-11-24).

But there are still two problems:

  1. The error message isn't very helpful. We should give the usual "not
     fully merged" message, which points the user at "branch -D". That
     was a problem even back in 67affd5173.

  2. Even without a HEAD, these days it's still possible for the
     deletion to succeed. After 67affd5173, commit 99c419c915 (branch
     -d: base the "already-merged" safety on the branch it merges with,
     2009-12-29) made it OK to delete a branch if it is merged to its
     upstream.

We can fix both by removing the die() in delete_branches() completely,
leaving head_rev NULL in this case. It's tempting to stop there, as it
appears at first glance that the rest of the code does the right thing
with a NULL. But sadly, it's not quite true.

We end up feeding the NULL to repo_is_descendant_of(). In the
traditional code path there, we call repo_in_merge_bases_many(). It
feeds the NULL to repo_parse_commit(), which is smart enough to return
an error, and we immediately return "no, it's not a descendant".

But there's an alternate code path: if we have a commit graph with
generation numbers, we end up in can_all_from_reach(), which does
eventually try to set a flag on the NULL commit and segfaults.

So instead, we'll teach the local branch_merged() helper to treat a NULL
as "not merged". This would be a little more elegant in in_merge_bases()
itself, but that function is called in a lot of places, and it's not
clear that quietly returning "not merged" is the right thing everywhere
(I'd expect in many cases, feeding a NULL is a sign of a bug).

There are four tests here:

  a. The first one confirms that deletion succeeds with an orphaned HEAD
     when the branch is merged to its upstream. This is case (2) above.

  b. Same, but with commit graphs enabled. Even if it is merged to
     upstream, we still check head_rev so that we can say "deleting
     because it's merged to upstream, even though it's not merged to
     HEAD". Without the second hunk in branch_merged(), this test would
     segfault in can_all_from_reach().

  c. The third one confirms that we correctly say "not merged to HEAD"
     when we can't resolve HEAD, and reject the deletion.

  d. Same, but with commit graphs enabled. Without the first hunk in
     branch_merged(), this one would segfault.

Reported-by: Martin von Zweigbergk <martinvonz@google.com>
Signed-off-by: Jeff King <peff@peff.net>
Signed-off-by: Taylor Blau <me@ttaylorr.com>

---
## [FIJTeam/eternitystation](https://github.com/FIJTeam/eternitystation)@[5b4ba051a0...](https://github.com/FIJTeam/eternitystation/commit/5b4ba051a08e0c63ca77abedd86991d3ba7aaf29)
#### Saturday 2022-11-12 21:27:50 by LemonInTheDark

Builds logic that manages turfs contained inside an area (#70966)

## About The Pull Request

Area contents isn't a real list, instead it involves filtering
everything in world
This is slow, and something we should have better support for.

So instead, lets manage a list of turfs inside our area. This is simple,
since we already move turfs by area contents anyway

This should speed up the uses I've found, and opens us up to using this
pattern more often, which should make dev work easier.

By nature this is a tad fragile, so I've added a unit test to double
check my work

Rather then instantly removing turfs from the contained_turfs list, we
enter them into a list of turfs to pull out, later.
Then we just use a getter for contained_turfs rather then a var read

This means we don't need to generate a lot of usage off removing turf by
turf from space, and can instead do it only when we need to

I've added a subsystem to manage this process as well, to ensure we
don't get any out of memory errors. It goes entry by entry, ensuring we
get no overtime.
This allows me to keep things like space clean, while keeping high
amounts of usage on a sepearate subsystem when convienient

As a part of this goal of keeping space's churn as low as possible, I've
setup code to ensure we do not add turfs to areas during a z level
increment adjacent mapload. this saves a LOT of time, but is a tad
messy

I've expanded where we use contained_turfs, including into some cases
that filter for objects in areas. need to see if this is sane or not.

Builds sortedAreas on demand, caching until we mark the cache as
violated

It's faster, and it also has the same behavior

I'm not posting speed changes cause frankly they're gonna be a bit
scattered and I'm scared to.
@Mothblocks if you'd like I can look into it. I think it'll pay for
itself just off `reg_in_areas_in_z` (I looked into it. it's really hard
to tell, sometimes it's a bit slower (0.7), sometimes it's 2 seconds
(0.5 if you use the old master figure) faster. life is pain.)

## Why It's Good For The Game

Less stupid, more flexible, more speed

Co-authored-by: san7890 <the@san7890.com>

---
## [Spc-Dragonfruits/sunset-wasteland](https://github.com/Spc-Dragonfruits/sunset-wasteland)@[4c71d18ba0...](https://github.com/Spc-Dragonfruits/sunset-wasteland/commit/4c71d18ba0ebc4ab6aa34111da3d8638352ab246)
#### Saturday 2022-11-12 22:22:45 by Carl?

Rocket Shrapnel & Other (#689)

- - -
New:
 - Rockets are now their own subclass of projectile, encompassing not just rockets, even though it's weird to say that and kinda wacky, but also grenade launcher projectiles.
 - Rocket classed projectiles can now have shrapnel magnitude and type attributed to them, permitting explosions identical to frag grenades on impact with their selected shrapnel and magnitude.
- - -
Balance:
 - A singular incendiary rocket replaces the high-yield HE round that the NCR Combat Engineer previously got in the rocket kit.
 - Chemical rockets are now absurdly powerful, to compensate for their otherwise useless nature. We'll probably adjust this as needed, if not outright nerf it again.
 - Chemical rockets can be made, but they're a PITA to craft and are likely to be more trouble than they're worth.
 - A singular unit of FEV is enough to OD someone. It's FEV. Stop drinking it.
- - -

---
## [not-the-fiend/clovermon-showdown](https://github.com/not-the-fiend/clovermon-showdown)@[3f40fc1fda...](https://github.com/not-the-fiend/clovermon-showdown/commit/3f40fc1fda7b5f0f399d4c9acf4a8e63055aa9bd)
#### Saturday 2022-11-12 23:01:15 by Greednut

Small Rootchew line cleanup

+ fuck you sherifuego

---
## [newstools/2022-new-york-post](https://github.com/newstools/2022-new-york-post)@[c6720351be...](https://github.com/newstools/2022-new-york-post/commit/c6720351bec49e2cadc8da1eb797bfba83b54bb6)
#### Saturday 2022-11-12 23:41:06 by Billy Einkamerer

Created Text For URL [nypost.com/2022/11/12/melinda-gates-new-boyfriend-confessed-to-abusing-his-wife/]

---

