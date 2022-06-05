## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-06-04](docs/good-messages/2022/2022-06-04.md)


1,561,221 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,561,221 were push events containing 2,226,186 commit messages that amount to 121,910,030 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 39 messages:


## [dfinity/motoko](https://github.com/dfinity/motoko)@[e883348f8a...](https://github.com/dfinity/motoko/commit/e883348f8a35c0925d7363cc6b9488fdac261a29)
#### Saturday 2022-06-04 00:07:53 by Gabor Greif

feat: introduce array-slice processing for compacting GC (#3231)

This PR introduces a modified marking (and visiting) technique for array fields, where `Array`s are GC-ed by considering their suffixes as slices, pushing these on the mark stack as bulk collections, and treating the fields in the prefix as individual objects being pushed onto the mark stack.

Following key changes are made:
- when visiting an `Array` in the dynamic heap we consult a new callback that can opt-out of the individual processing of some suffix of the array (by returning an index smaller than the array length)
- fields before this index will be processed as before by the first callback
- for the suffix the new callback is in charge to perform the bulk action
- in case of array marking, the new callback checks if the current slice is longer than some cutoff, and if so, it will push the array and the start of the suffix to the mark stack. (We abuse the tag entries as the start index for the suffix slice, so the cutoff must be numerically bigger than the biggest heap tag; this invariant is enforced)
- when pulling entries `(obj, tag)` from the mark stack a `tag >= TAG_ARRAY_SLICE_LOW_LIMIT` indicates that we have to deal with a suffix slice of an `Array`. The visitor will then again check the slice's length and do the subdivision again, as necessary.

This way of treating suffix-slices as pseudo-heapobjects originates from the suggestion of @ulan in a SGM (2022-05-30). It sidesteps the issue with layering violations, and restricts the handling of pseudo-tags to a very restricted portion of the collector source code, viz. the pushing of the range, and the visitor's case analysis on the tag, which now needs to  know about the suffix slices. Fortunately the visitor already accepts the heap tag as an argument (and doesn't extract it from the object; which would be unreliable due to threading), so the appearance of pseudo-tags is not a big deal.

The cutoff is currently chosen as 127, so for any `Array` at most 128 new entries are being placed on the mark stack.

The charm of this solution is that the same code is doing the marking pushing/popping and visiting as before, only that now it happens in an interleaved manner. The mark is already present on the array, so no reëntrancy can't occur, and eventually all its fields get processed.

-----

Below is an account of how field-by-field marking, pushing and visiting was done formerly (still in use for prefix portion of arrays), and an aborted attempt to a scheme as suggested by @osa1. I leave it for reference.

----------
See #2903. This reduces the marking stack traffic for GC-ed arrays substantially. Not applicable to copying GC!

## Status quo

Here is what happens to an array object's (single) field while `mark_fields`:
 - considered only when it is a skewed pointer and points into the dynamic heap (otherwise it is a _static object_ or a _magic_, no need to GC)
 - visitor callback is invoked:
   - `mark_object` will place a bit and push to the mark stack when not marked yet
     (when being pushed onto the mark stack the (unskewed) pointer and the heap tag are remembered)
   - the field address gets `thread()`-ed when the contained object is physically located at a less or equal address than the array itself
     (threading will put the field address into the object tag saving the tag into the word where the field address points to; the old object pointer is overwritten, but may live on in the mark stack)

## How bulk marking could work (ABANDONED)

When discovering a sequence of value fields that are laid out successively in memory and a count field in front, we can do a bunch of nice shortcuts. Below items sketch the how this could work. Invariant: there must be a tag field immediately before the length field.

- the bulk visitor callback gets called with a pointer to the length field
- it decides that it is worth doing a ranged marking and divides the bulk into a (small) prefix and a non-empty suffix `(pointer_to_length, start_index)`
- set all marks corresponding to (dynamic heap) objects in the suffix to avoid re-visiting (see [open issue](#Revisit-avoidance-is-more-complicated))
- push `(pointer_to_length, start_index)` onto the mark stack, using low bits in the pointer to differentiate from `(obj, tag)` pairs
- bulk visitor callback returns the prefix length, the fields in this area will be visited individually

When it comes to popping the mark stack and there is a field range on its top we want to be as transparent as possible, but also have to perform steps that had to be skipped (relative to the proceeding on individual fields)

 - identify that the ToS is a range `(pointer_to_length, start_index)`
 - obtain a pointer to the field indexed by `start_index`
 - increment `start_index` (still remains on the stack)
 - if  `start_index` is equal to the length, pop the entry
 - check that the field is a GC-able pointer
 - if so, extract the object and the heap tag corresponding to the field
 - otherwise pop again and return that
 - apply the threading to the field address (use the invariant to get the home object and apply the threading criterion)
 - return the object and the heap tag

## Open issues

There are some ugly wrinkles in this design, that need to be addressed somehow.

### Revisit avoidance is more complicated

An object is either unmarked, in the mark stack or is being (has been) visited. When pushing entire ranges, we cannot process individual objects and as such marking and threading may happen in unexpected ways.

#### Saving the marked bit

When eagerly marking the whole range of fields, we must not drop the info whether the individual mark is already set. This is because a mark means that either an object is in the mark stack or being/have-been visited. We have two possibilities:
- mark range eagerly on push, but remember previous marks (e.g. in the unused bit of the `Value` in the fields), or
- instead mark lazily on popping an object from the range, performing the threading anyway, but never returning already marked objects.

The latter option is in conflict with what #2903 suggests, and could potentially invalidate the idea of pushing ranges at all.

#### Intervening `thread()` call after range marking

After a range has been pushed and all dynamic objects marked, an individual field with an object also referenced by the range might become threaded. In this case the tag field of that object gets overwritten, but can be distinguished from regular tags. Such objects got individually pushed and already popped from the stack, and thus have been visited. So the field in the range must be threaded, but the pointed object must be skipped (not visited again).

### Layering violation

The fact that the `pop_mark_stack` needs to know about object layout and then how to do the threading is disgusting.
Maybe there should be a callback parameter that is invoked then a non-pointer (i.e. range) entry is encountered in ToS position.

### `pointer_to_dynamic_heap` needs the heap base

If `pop_mark_stack` is to check pointers for pointing into the dynamic heap, it needs to receive the heap base, but it currently doesn't. It is open if the caller has this piece of information. (It has, what a relief!)

### Special format of `usize` passed to `push_mark_stack` and `push_range_mark_stack`

Distinguishing by the lowest bit is hacky.

## Further improvement opportunities

I spotted below optimisation tricks while reading the code.

 - `pointer_to_dynamic_heap` unskews a lot, why not compare with a `heap_base` that is 1 less?
 - `mark_object` doesn't need to get the previous mark (`bool`), but compare the (64-bit) word the mark is in whether it changed
 - `mark_object` unskews. Would it be possible to do `set_bit` using the `raw_ptr`?
 - `field_value.get_ptr() <= obj` could be `field_value.raw_ptr() + 1 <= obj` and further `field_value.raw_ptr() < obj` saving us an addition
 - can the double storing of the heap tag (by `thread` and `push_mark_stack`) be consolidated?
   (we have 2 cases for whether `thread` happens and 2 cases whether the `push_mark_stack` happens)
 - can the dynamic heap pointer check be reduced to a shift and a comparison with `BITMAP_FORBIDDEN_PTR` (at least while marking, as it is not available in copying GC)?

---
## [michaeltreat/MERN_Journal_App](https://github.com/michaeltreat/MERN_Journal_App)@[0277800003...](https://github.com/michaeltreat/MERN_Journal_App/commit/0277800003e1797a2c32636d98adde1cbcd5f5d2)
#### Saturday 2022-06-04 00:19:17 by Michael Treat

 okay, re-thought out how this is going to work. I need to utilize home view. Home view should display the recent journals and recent entries. It should also have controls/links to navigate to routes which I just defined. /home -> recents and controls. /journals -> all journals. /journals/new -> new journal. /journals/:id -> a journal, showing recent entries and entry controls. /journals/:id/entries/ -> All entries for a journal. /journals/:id/entires/new -> new journal entry. /journals/:id/entries/:id -> single entry for a given entry. I think this is the basic layout, and the url endpoints. I know what the views will typically look like, now I can start to logically layout the flow of the application and it's interaction logic. I'm still struggling trying to understand the correct way to conditionally render. Is there some type of switchboard matrix that I could use to toggle what is showing and when? Like, when I click on create new journal, I want to form to take over the whole page. But since I'm using views, should it re-render the entire view? That means the view might have multiple completly different views. I am thinking of it kind of like a canvas, and it just paints what's needed, but it seems incorrect. Instead, I'm thinking the view itself should be less like a canvas and more intelligent. But then I think that's more of a controller's job. I feel like the larger the app grows the more I will need a well thought out solution here, but for this exercise I'm just trying to keep moving forward.

---
## [andy-kimball/cockroach](https://github.com/andy-kimball/cockroach)@[f782e45fd0...](https://github.com/andy-kimball/cockroach/commit/f782e45fd0da015396bc758e855535a951f2e21a)
#### Saturday 2022-06-04 00:35:14 by Andrei Matei

util/timeutil: don't strip mono time in timeutil.Now

Our timeutil.Now() insists on returning UTC timestamps, for better or
worse. It was doing this by calling time.Now.UTC(). The rub is that the
UTC() call strips the monotonic clock reading from the timestamp.
Despite repeatedly trying ([1]), I've failed to find any reasonable
reason for that behavior. To work around it, this patch does unsafe
trickery to get a UTC timestamp without stripping the monos.

Stripping the monos has the following downsides:
1. We lose the benefits of the monotonic clock reading.
2. On OSX, only the monotonic clock seems to have nanosecond resolution. If
we strip it, we only get microsecond resolution. Besides generally sucking,
microsecond resolution is not enough to guarantee that consecutive
timeutil.Now() calls don't return the same instant. This trips up some of
our tests, which assume that they can measure any duration of time.
3. time.Since(t) does one less system calls when t has a monotonic reading,
making it twice as fast as otherwise:
https://cs.opensource.google/go/go/+/refs/tags/go1.17.2:src/time/time.go;l=878;drc=refs%2Ftags%2Fgo1.17.2

An alternative considered was setting the process' timezone to UTC in an
init(): time.Local = time.UTC. That has downsides: it makes cockroach
more unpleasant to link as a library, and setting the process timezone
makes the timestamps not roundtrip through marshalling/unmarshalling
(see [1]).

[1] https://groups.google.com/g/golang-nuts/c/dyPTdi6oem8

---
## [skyline75489/terminal](https://github.com/skyline75489/terminal)@[77215d9d77...](https://github.com/skyline75489/terminal/commit/77215d9d77b99b48d1ee8302736178f2ec9f3a77)
#### Saturday 2022-06-04 03:50:57 by Mike Griese

Fix `ShowWindow(GetConsoleWindow())` (#13118)

A bad merge, that actually revealed a horrible bug.

There was a secret conflict between the code in #12526 and #12515. 69b77ca was a bad merge that hid just how bad the issue was. Fixing the one line `nullptr`->`this` in `InteractivityFactory` resulted in a window that would flash uncontrollably, as it minimized and restored itself in a loop. Great. 

This can seemingly be fixed by making sure that the conpty window is initially created with the owner already set, rather than relying on a `SetParent` call in post. This does pose some complications for the #1256 future we're approaching. However, this is a blocking bug _now_, and we can figure out the tearout/`SetParent` thing in post. 

* fixes #13066.
* Tested with the script in that issue.
* Window doesn't flash uncontrollably.
* `gci | ogv` still works right
* I work here.
* Opening a new tab doesn't spontaneously cause the window to minimize
* Restoring from minimized doesn't yeet focus to an invisible window
* Opening a new tab doesn't yeet focus to an invisible window
* There _is_ a viable way to call `GetAncestor` s.t. it returns the Terminal's hwnd in Terminal, and the console's in Conhost


The `SW_SHOWNOACTIVATE` change is also quite load bearing. With just `SW_NORMAL`, the pseudo window (which is invisible!) gets activated whenever the terminal window is restored from minimized. That's BAD.


There's actually more to this as well. 


Calling `SetParent` on a window that is `WS_VISIBLE` will cause the OS to hide the window, make it a _child_ window, then call `SW_SHOW` on the window to re-show it. `SW_SHOW`, however, will cause the OS to also set that window as the _foreground_ window, which would result in the pty's hwnd stealing the foreground away from the owning terminal window. That's bad.

`SetWindowLongPtr` seems to do the job of changing who the window owner is, without all the other side effects of reparenting the window. 

Without `SetParent`, however, the pty HWND is no longer a descendant of the Terminal HWND, so that means `GA_ROOT` can no longer be used to find the owner's hwnd. For even more insanity, without `WS_POPUP`, none of the values of `GetAncestor` will actually get the terminal HWND. So, now we also need `WS_POPUP` on the pty hwnd. To get at the Terminal hwnd, you'll need

```c++
GetAncestor(GetConsoleWindow(), GA_ROOTOWNER)
```

---
## [chusteven/diesel](https://github.com/chusteven/diesel)@[448df6b615...](https://github.com/chusteven/diesel/commit/448df6b61566dbd419554fc82abd018357848846)
#### Saturday 2022-06-04 04:24:03 by Georg Semmler

Address #3173

This is a tricky one. It seems like the behaviour described in that
issue should work out of the box, but it doesn't. I've spend some time
to investigate various solutions to make this work, but I came to the
conclusion that the current behaviour is the correct one.

The underlying issue here is that such an query promotes the inner
`Nullable<_>` of the field onto the outer `Queryable` wrapper. Without
`Selectable` that would require a select clause like
`.select((table::column.assume_not_null(),).nullable())`. This is
technically a safe pattern, but requires the usage of the "advanced"
`assume_not_null()` method to forcibly convert types to their not null representation.

Possible solutions tried to make the enable constructs shown in that
issue:

* I've tried to make the `impl Selectable for Option<T>` return the
following `SelectExpression`:
`dsl::Nullable<dsl::AssumeNotNull<T::SelectExpression>>`
where `AssumeNotNull` converts each tuple element to the corresponding
not nullable expression, while `Nullable` wraps the tuple itself into a
nullable type wrapper.
* I've tried to apply a similar approach like that one above, but only
for derived impls by manipulating the generated code for a optional
field with `#[diesel(embed)]`

Both solutions require changes to our sql type system, as for example
allowing to load a non nullable value into a `Option<T>` to enable their
usage in a more general scope as the presented example case.
(See the added test cases for this). That by itself would be fine in my
opinion, as this is always a safe operation. Unfortunately the
`AssumeNotNull` transformation would be applied recursively for all
sub-tuples, which in turn would cause trouble with nested joins (again
see the examples). We would be able to workaround this issue by allowing
the `FromSql<ST, DB> for Option<T>` impl for non-nullable types to catch
null values, which in turn really feels like a bad hack. (You would like
to get an error there instead, but nested nullable information are
gone.)
All in all this lead me to the conclusion that the current behaviour is
correct.

This PR adds a few additional tests (an adjusted version of the test
from the bug report + more tests around nested joins) and does move
around some code bits that I noticed while working on this.

I think the official answer for the bug report would be: Either wrap the
inner type also in an `Option` or provide a manual `Selectable` impl
that does the "right" thing there.

---
## [dhoss/blood-ocean](https://github.com/dhoss/blood-ocean)@[a40898a219...](https://github.com/dhoss/blood-ocean/commit/a40898a2190cbb48a5aca2aeb8fcb9c38a5d9ec5)
#### Saturday 2022-06-04 04:36:39 by Devin Austin

finally free from the grasp of spring dependency injection hell fuck you @Value i hate you

---
## [d0sboots/tgstation](https://github.com/d0sboots/tgstation)@[a3c8013b45...](https://github.com/d0sboots/tgstation/commit/a3c8013b45c92fdb8efec7ba827d7b00191e2d55)
#### Saturday 2022-06-04 05:03:22 by GoldenAlpharex

Refactors how legs are displayed so they no longer appear above one-another when looking EAST or WEST (#66607)

So, for over 5 years, left legs have been displaying over right legs. Never noticed it? Don't blame you.
Here's a nice picture provided by #20603 (Bodypart sprites render with incorrect layering), that clearly displays the issue that was happening:

It still happened to this day.
Notice how the two directions don't look the same? That's because the left leg is always displaying above the right one.

Obviously, that's no good, and I was like "oh, that's a rendering issue, so there's nothing I can do about it, it's an issue with BYOND".

Until it struck me.

"What if we used a mask that would cut out the parts of the right leg, from the left leg, so that it doesn't actually look as if it's above it?"

Here I am, after about 25 hours of work, 15 of which of very painful debugging due to BYOND's icon documentation sucking ass.

So, how does it work?

Basically, we create a mask of a left leg (that'll be explained later down the line), more specifically, a cutout of JUST the WEST dir of the left leg, with every other dir being just white squares. We then cache that mask in a static list on the right leg, so we don't generate it every single time, as that can be expensive. All that happens in update_body_parts(), where I've made it so legs are handled separately, to avoid having to generate limb icons twice in a row, due to it being expensive. In that, when we generate_limb_icon() a right leg, we apply the proper left leg mask if necessary.

Now, why masking the right leg, if the issue was the left leg?
Because, see, when you actually amputated someone, and gave them a leg again, it would end up being that new leg that would be displayed below the other leg. So I fixed that, by making it so that bodyparts would be sorted correctly, before the end of update_body_parts(). Which means that right legs ended up displaying above left legs, which meant that I had to change everything I had written to work on right legs rather than left legs.

I spent so much time looking up BYOND documentation for MapColors() and filters and all icon and image vars and procs, I decided to make a helper proc called generate_icon_alpha_mask(), because honestly it would've saved me at least half a day of pure code debugging if I had it before working on this refactor.

I tried to put as much documentation down as I could, because this shit messes with your brain if you spend too long looking at it. icon and image are two truly awful classes to work with, and I don't look forward to messing with them more in the future.

Anyway. It's nice, because it requires no other effort from anyone, no matter what the shape of the leg is actually like. It's all handled dynamically, and only one per type of leg, meaning that it's not actually too expensive either, which is very nice. Especially since it's very downstreams-friendly from being done this way.


It fixes #20603 (Bodypart sprites render with incorrect layering), an issue that has been around for over half a decade, as well as probably many more issues that I just didn't bother sifting through.

Plus, it just looks so much better.

---
## [Michaelleojacob/waldo-with-backend](https://github.com/Michaelleojacob/waldo-with-backend)@[e42c234f46...](https://github.com/Michaelleojacob/waldo-with-backend/commit/e42c234f46aa4b3bd0f1ee8e4c147532c1f8a1de)
#### Saturday 2022-06-04 06:00:07 by mig

holy shit I think i might be done.

I just need to add some css, maybe banners/updates/pings/tooltips whatever I want to call them. and Refactor a bit.

---
## [roadworx/ROTN-Cleanup](https://github.com/roadworx/ROTN-Cleanup)@[ae294ac4ef...](https://github.com/roadworx/ROTN-Cleanup/commit/ae294ac4efb4ff5d328c97922e42c8c0318d6e75)
#### Saturday 2022-06-04 06:05:50 by EliteMeats

demon month

-added a funny sound effect
-tweaked loading screen tips
-removed cringe moster box spawns
-reduced battleaxe attack speed
-tweaked and added sounds to some major advancements
-changed magicite message to be a bit more lore friendly
-removed blockfire mod
-added some splash text
-corrupted cincinnasite now uses death quintessence instead of spores
-gearbox recipe now uses slabs
-handcrank recipe now uses a handle
-added serpentinite to stone oredict
-fixed serpentinite bricks recipe
-removed broken balance quintessence recipe

---
## [ExoticJazz/sunset-wasteland](https://github.com/ExoticJazz/sunset-wasteland)@[92f8f5d159...](https://github.com/ExoticJazz/sunset-wasteland/commit/92f8f5d159c8770e6927f38c6aa6622161af29bc)
#### Saturday 2022-06-04 06:08:23 by Tk420634

Updated *insult list

Removed
-vore
-gaylord
-shitcurity
-comdom
-greytider
-tator
-lingbin
-cluwn
-monkey

Modified or fixed
-Cheesemonger spelling
-Knight-like from Captain-like
-Comdom to dummy

Added
-Bramin-sniffer
-Raider
-scum-sucker
-mutie
-headass
-dumbass
-ghoul
-Kitten looking ass, added with Kit8bits permission

Now get your @pick(nouns_body) off my lawn.

---
## [planetscale/vitess](https://github.com/planetscale/vitess)@[dbfb9a49f7...](https://github.com/planetscale/vitess/commit/dbfb9a49f7c3b067221d0aae0d3c0285e6baf098)
#### Saturday 2022-06-04 06:51:00 by Andrew Mason

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
## [Dylan-DPC/rust](https://github.com/Dylan-DPC/rust)@[6385b1d880...](https://github.com/Dylan-DPC/rust/commit/6385b1d880607c1af7125b8aac7e3fc5cf6a8797)
#### Saturday 2022-06-04 07:13:53 by Dylan DPC

Rollup merge of #96642 - thomcc:thinbox-zst-ugh, r=yaahc

Avoid zero-sized allocs in ThinBox if T and H are both ZSTs.

This was surprisingly tricky, and took longer to get right than expected. `ThinBox` is a surprisingly subtle piece of code. That said, in the end, a lot of this was due to overthinking[^overthink] -- ultimately the fix ended up fairly clean and simple.

[^overthink]: Honestly, for a while I was convinced this couldn't be done without allocations or runtime branches in these cases, but that's obviously untrue.

Anyway, as a result of spending all that time debugging, I've extended the tests quite a bit, and also added more debug assertions. Many of these helped for subtle bugs I made in the middle (for example, the alloc/drop tracking is because I ended up double-dropping the value in the case where both were ZSTs), they're arguably a bit of overkill at this point, although I imagine they could help in the future too.

Anyway, these tests cover a wide range of size/align cases, nd fully pass under miri[^1]. They also do some smoke-check asserting that the value has the correct alignment, although in practice it's totally within the compiler's rights to delete these assertions since we'd have already done UB if they get hit. They have more boilerplate than they really need, but it's not *too* bad on a per-test basis.

A notable absence from testing is atypical header types, but at the moment it's impossible to manually implement `Pointee`. It would be really nice to have testing here, since it's not 100% obvious to me that the aligned read/write we use for `H` are correct in the face of arbitrary combinations of `size_of::<H>()`, `align_of::<H>()`, and `align_of::<T>()`. (That said, I spent a while thinking through it and am *pretty* sure it's fine -- I'd just feel... better if we could test some cases for non-ZST headers which have unequal and align).

[^1]: Or at least, they pass under miri if I copy the code and tests into a new crate and run miri on it (after making it less stdlibified).

Fixes #96485.

I'd request review `@yaahc,` but I believe you're taking some time away from reviews, so I'll request from the previous PR's reviewer (I think that the context helps, even if the actual change didn't end up being bad here).

r? `@joshtriplett`

---
## [Waklaidan/tgstation](https://github.com/Waklaidan/tgstation)@[20e4add487...](https://github.com/Waklaidan/tgstation/commit/20e4add48712b59e9bcadd187beee54c02f98e38)
#### Saturday 2022-06-04 08:01:23 by Tim

Change healing by sleeping to be affected by sanity, darkness (or blindfold), and earmuffs. (#65713)


About The Pull Request

Depending on the mob's sanity level, it can have a positive or negative boost to healing effects while sleeping. Sleeping in darkness, wearing a blindfold, and using earmuffs also counts as a healing bonus. Beauty sleep is very important for 2D spessmen.
Why It's Good For The Game

This is a small gameplay change that rewards players for keeping their sanity at good levels. Also depression has also been linked with impeding wound healing in real life. The placebo effect on peoples minds is strenuously documented and I think it would be cool to see it in the game.
Changelog

cl
expansion: Healing by sleeping is now affected by sanity, sleeping in darkness (or using a blindfold), and using earmuffs. The healing from sleeping in a bed was slightly decreased.
/cl

---
## [Waklaidan/warfare](https://github.com/Waklaidan/warfare)@[1867654758...](https://github.com/Waklaidan/warfare/commit/186765475881bf58bbee319880653287d578820b)
#### Saturday 2022-06-04 08:05:16 by Matt

Should fix the issue of loading the wrong CSS by making them all the same fuck you

---
## [southpawflo/xous-core](https://github.com/southpawflo/xous-core)@[6745206303...](https://github.com/southpawflo/xous-core/commit/67452063034ea98c6fe318c67e7c7109806c5a60)
#### Saturday 2022-06-04 09:16:50 by bunnie

mulling this pile of OpenSK code to see what we should cut, what we should keep

alright. the composite device problem is solved. The bigger issue I'm
mulling is if I should try to port the Google OpenSK FIDO2 stack into
Xous, or if I should just do a limited U2F implementation.

Poking around at the OpenSK stuff...porting looks possible, but, it's
going to be vendoring in all of the source from the OpenSK project. So
it'll be tough to apply patches if they happen; on the other hand, the
OpenSK implementation is FIDO2 certified, and the stable branch hasn't
moved since Nov 2021.

The main downsides of the OpenSK implementation are:

- it uses nightly. I think it can be stripped out, though; I haven't
  seen a "good reason" for it yet, it's mostly because Tock uses
  nightly. There's only one alarming use of it and it's in the crypto
  crates but those will be stripped out because....
- the crypto libraries are in fact not suitable for use. I dug into
  them and they definitely need to be gutted and replaced with the
  community-blessed crypto libraries and APIs. which is one big reason
  why once this goes into Xous land it doesn't go back easily into
  OpenSK land -- they actually have slightly different crypto
  APIs. more modern ones, to be fair, but, they haven't been reviewed.
- the implementation has "too many features"...for example, I don't
  think we'll ever realistically do authenticator attestation as it
  requires signing NDAs and provisioning secret keys that we can't
  share with users. But that code is there, and we'll either have to
  gut or bodge it.

The plusses are:

- it's FIDO2 certified. So, at least the protocol stack is probably
  complete and fully implemented, which means for features we don't
  use today I can just leave hooks or dummy values there for a fast
  migration path.
- Looks like they aren't changing things too fast in the dev
  branch...so this probably is not like riding a greased pig
- Looks like a couple of paid professionals wrote the code...better
  than what we have going on here
- I think I see a path to carve out their "persistent store" and glom
  it into the PDDB; a path to adapt their crypto traits into
  Xous-native traits; and a path to connect their CTAP protocol engine
  to the Xous HID server. So it seems feasible. But they baked in some
  bad API assumptions deeply enough that they are one-way streets I
  think to get these ports done.

I'm going to sleep on this, but I'm leaning toward trying to pull in
the OpenSK code because even tho it is a bit painful it probably gets
a bigger feature scope and so far it looks like I wouldn't be changing
any protocol-level stuff for the port, I would just be monkeying
around with the internal storage, crypto, and USB implementations, so
ideally the end result is we get a certified FIDO2 protocol engine for
the effort.

I think the main concern I have going in this direction is I don't see
a way to do this and simultaneously be able to absorb upstream patches
into this vendored code, because their API assumptions are too
different. Any bug fixes or patches would have to be manually applied
and merged. But maybe that's not such a big deal...?

---
## [CenTdemeern1/robot-is-chill](https://github.com/CenTdemeern1/robot-is-chill)@[766df06d22...](https://github.com/CenTdemeern1/robot-is-chill/commit/766df06d22c2f1ca6fb219f5bff072c239fa6aff)
#### Saturday 2022-06-04 09:28:17 by Heptor44

oh my god im so fuckibg sorry

i had no idea these sprires were there im so sorry aaa

---
## [VOREStation/VOREStation](https://github.com/VOREStation/VOREStation)@[38724d4d4c...](https://github.com/VOREStation/VOREStation/commit/38724d4d4c140fb4bfc92444ba3e5dd182ca7df9)
#### Saturday 2022-06-04 09:59:36 by VerySoft

[WIP] pAI tweaks and upgrades

Changes some things around! 

Removes the 'wipe' button from pAI's interface, since I think there being an instant 'kill player' button is pretty lame, especially since most pAIs activate on their own without a master. They're easy enough to kill or contain without this, so I don't see it as necessary. If you want to kill your pAI friend just eat them. :U

Removes the 'pAI Suicide' verb, and renames the 'Wipe Personality' to 'Enter Storage' and moved it from the OOC tab to the pAI Commands tab. Killing a pAI deletes the card and all that, where the 'Enter Storage' verb deletes the card and spawns a new one that can be used, which! I think it more appropriate.

Makes it so that, when damaged, pAIs will slowly regenerate while folded up, at a rate of 0.5 brute and burn per life tick, where previously it had been impossible to recover health outside of admin intervention.

Updated the Universal Translator with many of the newer languages that aren't obviously for events or hivemind type things.

Added the same emotes that humans can use to pAIs

Added an alternative pAI card style, and rearranged the expressions for the cards a little bit, and added one more.

Plan to add more pAI chassis to play with

---
## [ABJ4403/Payback2_CHEATus](https://github.com/ABJ4403/Payback2_CHEATus)@[6792be2186...](https://github.com/ABJ4403/Payback2_CHEATus/commit/6792be218602a7f1d3f538c8fa050dece99d8e50)
#### Saturday 2022-06-04 10:13:45 by MDP43140

Update Payback2_CHEATus

+ respawn hack now can be turned off faster without terminating the script.
+ New Cheat: Win CTS (located in XP hack. client-side).
+ New Cheat: Skip slow intro animation (located in XP hack, coz the value is 100000k away from nearest value anchor).
+ Deprecate `WpnAmmWrd` & `HldWpn` memory regions (because its well.. useless)
+ [God modes] Dr0wned improved: Now Drowning sound appears like normal, and you can even actually walk on it now!
+ [God modes] Car acceleration cheat improved (Kudos to XxGabriel5HRxX for some of these cheats).
+ [table.tostring] Check if the value was 'number && length of >8', and convert them to hex if so (this is mostly for config files with memory addresses on it just to make it easier to read anyway).
+ Removed unnesecary addListItems on god modes clone cheat.
+ Shorten god modes title message.

PS: Some updates that involves value near to respawn hack, are delayed for stability reason.

---
## [Chamfer-Studios/Dune-Special-Spice-Ops](https://github.com/Chamfer-Studios/Dune-Special-Spice-Ops)@[55e7b3aed7...](https://github.com/Chamfer-Studios/Dune-Special-Spice-Ops/commit/55e7b3aed74f2d5a5e3f832e1fe7b511b39779df)
#### Saturday 2022-06-04 10:45:07 by Oscar Cuatrecasas

Crash Fixed

Trust in the LORD with all your heart, and do not lean on your own understanding. In all your ways acknowledge Him, and He will make straight your paths. May the God of hope fill you with all joy and peace as you trust in Him, so that you may overflow with hope by the power of the Holy Spirit.

---
## [densogiaichned/serenity](https://github.com/densogiaichned/serenity)@[49b087f3cd...](https://github.com/densogiaichned/serenity/commit/49b087f3cd49261164bd4556cd6e9e0d95a3afc1)
#### Saturday 2022-06-04 10:57:10 by kleines Filmröllchen

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
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[a7e6e8b8d4...](https://github.com/mrakgr/The-Spiral-Language/commit/a7e6e8b8d4f8e0583fbb61d17e7860e603aba3bf)
#### Saturday 2022-06-04 11:05:43 by Marko Grdinić

"9:15am. Discovered DALL-E 2 yesterday.

https://youtu.be/U1cF9QCu1rQ
How This A.I. Draws Anything You Describe [DALL-E 2]

Its capabilities here are most impressive, but the way OpenAI gives access to it might as well make it vaporware. I am not sure how big the model is, but it is good bet that I wouldn't be able to even run it on my GPU. It gives me a target to aim for. If I am going to win through art, it only makes sense to get resources needed to train something like it through art.

Having such a system would be a huge boost to my artistic ability. It would not be rank 4 or 5, but rank 6. What it does is beyond human ability and clearly superhuman. It is a pity I can't use it. For the time being I'll go with style transfer.

https://www.youtube.com/watch?v=n9ZNGVvMOSQ
5 Cartoon Tips You Really Need to Know (Blender)

https://youtu.be/5RQLWFxAN2Y
Blender Glass Shader for Toon Shading

Let me take a look at these links.

9:25am. I'll take it easy today. Let me watch these cartoon tutorials, then I'll watch some NN style transfer tutorials. I am not sure whether I want to get started trying to make that work on my own. I'll just do a bit of studying on it, but stick with the DDG for now. It is not worth the hassle. If it was the usual me, I'd sink a month or two into making it work on my own, but I am burnt from that.

https://youtu.be/7wpisn8t3us
4 Options for 2D Lines || Blender 2D

This caught my eye. Let me take a break here first though.

10:05am. Mato chapter and then I will get on with it.

10:25am. https://youtu.be/7wpisn8t3us
4 Options for 2D Lines || Blender 2D

Let me watch this for a bit. Then I'll move on to style transfer vids.

https://youtu.be/7wpisn8t3us?t=890

Come to think of it, what Pablo did with his comic matcap is in fact eqivalent to this, at least as far as getting that outer line is concerned.

10:50am. Ok, enough of that. Yesterday's success made me more hopeful about the future, and as a result I've started relaxing mentally. I need to pick up the slack.  While it true that I might not need PB renderers like Luxcore, I still like the soft lighting as input. The best solution to my current predicament is to get better hardware. But even so, Malt and Eevee should work great with style transfer.

So let me study the later. I am going to need some shader magic to do my thing, but not too much of it. I should focus on style transfer for now.

https://www.youtube.com/results?search_query=neural+net+style+transfer

Let me see what Youtubers have to say. Also I want to look into the original deep dream. I forgot what kind of objective it had that caused it to generate all those dog faces everywhere. I want to make sure it is not regular style transfer.

https://youtu.be/gzQxnZDePko
Neural Style Transfer || A Neural Algorithm of Artistic Style

Let me start with this.

https://youtu.be/gzQxnZDePko?t=256

It seems he shows how to implement it.

https://youtu.be/gzQxnZDePko?t=370

20m params. Assuming they are f32, that means the net should be 80mb. This should be doable on my system.

https://youtu.be/gzQxnZDePko?t=474

The way he calculated the gram matrix is different from how she explained it would be calculated in the other video. On the video, she did not account for the reduction. As expected, code is what you need to understand all of this.

https://youtu.be/gzQxnZDePko?t=597

Style weight, content weight. Here they are.

11:30am. I am guessing that for whatever model they are using the Thin Style ommits the lower layers. That is the only thing that makes sense for what it could be.

https://youtu.be/gzQxnZDePko?t=750

Here he mentions some extra techniques that perform extraordinary style transfer.

https://youtu.be/eeeai1OrnDI
Pix2Pix || Paired Image to Image Translation || Developers Hutt

What is image translation? That is a bit like style transfer, right?

Let me take a short break and then I'll watch more videos. I thought I would leave this alone, but this would be really easy to implement on my own. The programming effort would be no more than a day. Of course selecting the right model and playing around would make it take longer, but I can pay that expense of time.

11:45am. Let me resume. I am going to dive into this.

https://youtu.be/eeeai1OrnDI?t=168

Oh this is an interesting idea. This should act to stabilize the GAN.

12pm. Nevermind this. This is not of interest to me. And the image resolution it too low. For the kind of magic DALL-E 2 does I'd need a lot better hardware.

https://youtu.be/1-26FDZM-Zg
The best style transfer?

Let me watch this.

https://youtu.be/1-26FDZM-Zg?t=25

Yeah, it would be a good idea to get one of the newer papers and implement that.

https://youtu.be/1-26FDZM-Zg?t=105

Oh wow take a look at that drawing of a basketball player. One thing that bothers me about the DDG is that in the image of a rig, it always had lines drawn over it no matter which style I used. I get the sense that this should not happen. Maybe different methods would work better.

https://youtu.be/1-26FDZM-Zg?t=187
> Generating 1k outputs requires 12gb of memory.

Seriously? Something like this I'd need to adapt so it does not go over 3.5k.

Thankfully unlike with poker game sequences, doing this with images will be much easier.

https://youtu.be/1-26FDZM-Zg?t=228

Actually this is weird. Why does 512x512 require 6gb, while an image that is 4x larger require 12gb? This scaling does not make sense.

Also it does seem like the runtimes take a while.

12:30pm. https://youtu.be/1-26FDZM-Zg?t=469

Had to do a bit of chores. Let me resume. The cool thing comapred to doing this instead of poker is that I do not need the latest and greatest. The old thing will do fine here and I can move to newer methods once I get the hardware for them. With poker, unless I can train a very good agent, I have nothing of value. I'll read the paper just to learn the motivation behind it and the problems with older methods.

https://youtu.be/1-26FDZM-Zg?t=561

The transfer to a drawing on the bottom left is really good. Is there a point to using the regular conversion to grayscale anymore. I doubt it.

https://youtu.be/1-26FDZM-Zg?t=682

This is nice. 1,000 out of 1,000 times you'd imagine this was drawn by hand. I'd never have though it possible. Inio Asano can stop redrawing pictures by hand.

This really opens up a lot of possibilities for me.

https://youtu.be/1-26FDZM-Zg?t=773

Let me pause here so I can eat."

---
## [StevenZoernack/ReputationBoss-Wikipedia-](https://github.com/StevenZoernack/ReputationBoss-Wikipedia-)@[814162aaa4...](https://github.com/StevenZoernack/ReputationBoss-Wikipedia-/commit/814162aaa4d8ccf39ff0d2cb8dabecc9ce32b683)
#### Saturday 2022-06-04 11:57:19 by Steven Zoernack

Update README.md

ReputationBoss - Global Tier 1 Wikipedia Page Creation
Will a Corporate, Personal or Product Wikipedia Page Dominate Your Google Search Results?
ReputationBoss   Global Corporations   Wikipedia Page Creation Services ReputationBoss Global Corporations Wikipedia Page Creation Services
New York City, New York May 31, 2022 (Issuewire.com)  - ReputationBoss – Simply the Best Online Reputation Management firm trusted by both big and small global corporations as well as high profile individuals including Founders/CEOs, Entrepreneurs, Best Selling Authors, Producers, Politicians, Physicians, Attorneys, Pro Athletes, Models, and Celebrities Worldwide.

Why have a Corporate, Personal, or Product, Wikipedia Page?

A well-designed Wikipedia page may add global traffic, instantly enhance credibility, and can be a source of pride for the entire company and its employees, or family and family members. It can leave a legacy. These days, and depending on the industry, some clients or investors even demand it.

Google loves Wikipedia and as such ranks it high in search results. Wikipedia is also the first place people go when they Google your company, your product, or your name. By leveraging Wikipedia, you can help control your brand and present yourself to the world.

A well-built Wikipedia page is the cornerstone of building your personal and/or corporate brand. We can add photos, successes, accolades, schedules, charts, graphs, etc. Your Wikipedia page will be considered “fact”, whereas personal websites are seen as mostly “promotional”.

Why choose us to write your Wikipedia article?
We do more than simply write your Wikipedia page. We advise you on the entire process and ensure that we write your page to adhere to Wikipedia guidelines. We also make sure to use the proper format and referencing so your page will be compliant with Wikipedia standards. We write your new corporate or personal Wikipedia Page so it not only has a high approval rate but also a high rate of remaining in the world’s largest encyclopedia seen by Billions of people.

The most qualified Wiki experts in the Nation
1.  Our Wiki Experts have an average of 7+ years’ Wikipedia editing experience.
2.  Over 9,320 edits made and 589 pages created per average Wiki Expert.
3.  We understand Wikipedia guidelines and how articles must be written to conform and get approved.
4.  We only take on notable clients. If we give you an ExpressQuote for your project, you should know that you are notable enough to have a good chance of being approved. If we think that you are not notable enough in Wikipedia’s eyes we will tell you so.
5.  We use only independent and reliable sources to show the notability of your articles
6.  We are very familiar with all the copyright issues with Wikipedia. We are able to submit your content and images to Wikipedia in compliance with guidelines.
7.  Our Wiki experts have created Wikipedia pages for many notable people and businesses including Fortune 500 companies, professional athletes, politicians, musicians, physicians, lawyers, actors and filmmakers, and authors just to name a few.
8.  For your protection we never disclose our clients in order to protect their anonymity.

What we can do for your Wikipedia page
1.  Create information boxes that showcase your logo, photo, and/or general information about your brand.
2.  Create subheadings applicable to the topic (e.g. History, External Links, Early Years, etc.
3.  Add your website link to the page.
4.  Continuously monitor your Wikipedia page to help protect the content from unwanted edits and the potential of attacks from competitors  (Page monitoring is a separate charge outside of page creation).
5.  Include images of products, people, and anything else related to the article (you must supply original images).
6.  Link your Wikipedia article to other Wikipedia articles to help build up the popularity of the page and to introduce your page to new audiences
7.  If your article is already created, ensure that everything within the article is neutral, including any negative information that someone may have posted about you.

What we will NOT do for your Wikipedia page
1.  Create a SPAM article that is not notable and publish it on Wikipedia in the “hope” that it does not get deleted.
2.  Attack a Wikipedia page of your competitor. That is between you and them. If their page is not notable, then recommend it for deletion, but we will not get in the middle of your disputes.
3.  Include promotional wording in your article. This is not only against Wikipedia guidelines but will also likely cause your article to be tagged as promotional and worse yet, recommended for deletion.
4.  Put information in the article that we cannot tie to a reliable source. If you want us to add something to your article, make sure there is a source to support it.

We use only Original Photographs for your Wikipedia Page
We post only original photographs that cannot be found elsewhere online due to copyright laws and the digital signature that is embedded on all photos existing on the internet. The photograph(s) will be uploaded to Wikipedia with your agreement that your copyright of those photograph(s) is to be given up to Wikipedia. Images taken directly from another website are prohibited on Wikipedia.

Wikipedia Notability
One of the questions we get on a daily basis deals with what qualifies someone to have a company or personal Wikipedia page. Well, it all comes down to notability. Notability is the criteria used by Wikipedia to determine if a topic should be included in the world’s largest encyclopedia. After all, without this requirement, everyone would have a Wikipedia article. As a disclaimer, ReputationBoss does not work for, nor are we affiliated with the Wikimedia Foundation, the non-profit group that runs Wikipedia and its sister sites.

So what makes something or someone notable?
Notability generally comes from references. As a rule of thumb, notability is established when the topic has “significant coverage” with “reliable sources” that are “independent” of the topic”. This is sometimes referred to as Wikipedia’s “Golden Rule.”

The statement above really sums it up well. Once you understand what each term means in regards to Wikipedia, you will easily be able to tell if your topic is notable enough. Wikipedia’s guidelines on notability are long and difficult to understand. Here we try to break things down into easily understood terms that anyone can understand.

Significant Coverage
Significant coverage means that the topic is covered by numerous sources and those sources cover the topic “in-depth.”

Reliable Sources
Reliable Sources are something that is debated on a daily basis by Wikipedians. Basically, a source is considered reliable if it is from a published source that is trusted. This means that the publication must have editorial control over its content (e.g., fact-checkers) and it must be known as being reliable.

As a general rule, simply familiarize yourself with sources used in other articles. Examples of reliable sources include the New York Times, the Wall Street Journal, Time Magazine, USA Today, and Bloomberg.

Topics can also dictate what is considered reliable. For instance, medical articles generally do not allow for references from anything other than peer-reviewed medical journals. This means that although The New York Times may talk about a new breakthrough medical treatment, the Wikipedia article about the treatment will generally only use published studies on the treatment, not the New York Times Article.

If we as editors have a question about a source and whether it is reliable, there is a noticeboard where we can go and pose the questions. We simply create a new topic and ask if a specific link is reliable. We then receive numerous responses from editors who patrol that page on a regular basis. This helps us in making the process a smooth one and without many complications down the road. There is also a general checklist that Wikipedia has put together that helps us determine if a source is reliable.

So, we are very familiar with the sources generally used in Wikipedia, we use the checklist, and if needed, we consult the noticeboard with any questions about a specific source that we’ve located on your behalf.

Independent of the Topic
Being “independent” is difficult to understand, especially for those new to Wikipedia. However, it is at the core of Wikipedia and must be followed in order to maintain its integrity. Simply put, a self-published source is not to be used for notability. There are many times when a self-published source can be used (such as using a company website to the source where the headquarters are located), but never for purpose of notability. Self-published sources can include the following: Official websites, Social media, Official blogs, Press releases, and Interviews

If you want to establish notability with a press release, you are barking up the wrong tree. The article you create will be quickly deleted as the press release is not considered independent of the topic.

As with many other Wikipedia guidelines, “independence” can vary depending on the topic. Wikipedia provides the following examples:

Here is why it is difficult for newcomers to understand. They see self-published sources used all the time on Wikipedia which gives a false perception that they are acceptable. In fact, self-published sources ARE acceptable in Wikipedia, but not for establishing notability.

So, you will find social media profiles, press releases, and company websites cited everywhere on Wikipedia, but if they are being used for notability purposes, chances are the topic isn’t notable enough for Wikipedia and is likely to be deleted.

Now, what about interviews in major newspapers?

Many people think that these are acceptable since they are in a major publication. Unfortunately, they would be wrong. While the source itself may be considered significant and in-depth, the fact that the wording is the statement of the subject being interviewed, it would be considered a self-published source.

Additional Notability Guidelines
Now that you understand the “general notability guidelines,” you’ll see that we can get your page onto Wikipedia as long as there are some independent sources that we can cite for your page, and the more the better. We may have an editor come up after your page is online and recommend it for deletion because it doesn’t meet his or her interpretation of notability, or he doesn’t understand the topic, or sometimes even if he doesn’t like it. When this happens, and it does happen, we add more sources if available and/or rewrite and rework the page. One of our Wiki Experts had a page deleted 8 times before it was finally accepted. So we remain persistent in getting your page accepted and published.

Wikipedia Guarantees
One thing you will find with ReputationBoss is that we tell you directly if something is too promotional, cannot be supported by a source, isn’t encyclopedic in tone, or somehow otherwise doesn’t pass the grade. It is better to know upfront and get the content written correctly according to guidelines than it is to go back months later and try to re-post a deleted page.

Even after ensuring that the page meets all guidelines and policies, there is still a possibility that the page is changed from what was initially created. In fact, there is still a chance that it gets deleted based on consensus from the community on how the guidelines and policies apply.

Summary
Wikipedia is difficult to navigate and many have run into problems trying. Our firm was started as a professional  Reputation Management and Wikipedia page creator and we understand all facets of your online reputation and how to make you or your company look its best. We are continuous students of the Wikipedia page creation process as Wikipedia continues to change and evolve.

In addition to page creation, we offer page updating, monitoring, and maintenance. We can also translate your Wikipedia page into many languages.

Working with ReputationBoss will allow you to worry about what you do best and let us deal with the ever-changing and often frustrating bureaucracy of Wikipedia. 

For your no-obligation 24 Hour ExpressQuote to see the cost, timing, and strategy to get your own Wikipedia page in the world's encyclopedia seen by billions, please visit: 

Get your 24 Hour ExpressQuote

 

https://en.wikipedia.org/wiki/Reputation_management

 



Media Contact

ReputationBoss
*****@repboss.com
9419097000
1990 Main Street Suite 750 Sarasota, FL 34236
http://repboss.com

Categories : Advertising , Business , Lifestyle , Marketing , Media
Tags : ReputationBoss , Repboss , Steven Zoernack , Wikipedia , Wikipedia Page , Wikipedia Page Creation , Get a Wikipedia page , How to get a wikipedia page , steve zoernack , Tier 1 Wikipedia page creation
View as PDF view pdf
ReputationBoss

http://repboss.com

---
## [Christmas5/Skyrat-tg](https://github.com/Christmas5/Skyrat-tg)@[a064b35b25...](https://github.com/Christmas5/Skyrat-tg/commit/a064b35b2571af36cf9d12cea8005843768af36d)
#### Saturday 2022-06-04 12:59:56 by SkyratBot

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
## [Tiktodz/android_kernel_asus_sdm636](https://github.com/Tiktodz/android_kernel_asus_sdm636)@[246154cad5...](https://github.com/Tiktodz/android_kernel_asus_sdm636/commit/246154cad5a069f68347fe86c7eda37a628aec9d)
#### Saturday 2022-06-04 13:31:21 by Angelo G. Del Regno

Makefile.lib: Lower kernel gzip compression to fastest

You're reading this - so you're trying to understand "JUST WHY OMG".
That's already a good step.

First of all, this is a downstream kernel - always keep that in mind!
Now, this kernel is targeting new *very powerful* Qualcomm platforms
like SM8250 and the Sony Edo platform - which has a very fast UFS card.

Keep in mind that the bootloader sets the CPU at a frequency that is
slightly faster than the "in the middle" ones, which is anyway not
veeeery fast - but that's good, really. I agree.

So.. check this out:   for Image.gz-dtb.....
COMP_LEVEL    SIZE
9             20116171
5	      20220479
2	      20940223
1	      21231290

Remember again that we're loading from a UFS card and that
we are loading ~1.1MB more out of a 20MB file.
If you're smart enough you surely know already about RAM and CPU
overhead of very high compression levels.

If you still disagree with what I just did, read this commit description
another 20 times, or more, until you understand it. :)))

Signed-off-by: Kneba <abenkenary3@gmail.com>
Signed-off-by: Tiktodz <kuplemarkeple@gmail.com>

---
## [neildavis/mame2003-plus-libretro](https://github.com/neildavis/mame2003-plus-libretro)@[fecf11dfbd...](https://github.com/neildavis/mame2003-plus-libretro/commit/fecf11dfbdf77f24dc20531d5bc489c5ec9fb80f)
#### Saturday 2022-06-04 13:43:45 by Kyland K

Killer Instinct 1 and 2 Cheats Update! (#1325)

Note: Being that this the initial addition of massively updated KI1 and KI2 Cheats, please do not expect all Cheats to fully function as advertised! Some of the Cheats may be subject to change in future Updates!

Killer Instinct 1 and 2 Cheats Update!
Killer Instinct 1: Attack and Movement Speed Manipulation via Updated Cheats (cheat.dat)!

Selection of 12 different speeds and 21 different sizes, including Defaults.  You can choose to move as slow as molasses, or as fast as a Jedi!  Fight as a metaphorical watching paint dry sloth, or as frenetic as a one inch punch from Bruce Lee!  You can also be as small as a mouse or as large as a Kaiju!

Dozens of other Cheats added for both Killer Instinct 1 and 2, including Automated Ultra Combos and Humiliations and No Mercy Finishers!

Personal thanks to Mahoneyt944 and Abystus for their incredible efforts and insight in this little project I personally wanted to implement to help better lower spec platforms!

retroarch/system/mame2003-xtreme/cheat.dat

retroarch/system/mame2003-plus/cheat.dat

If using 2003 Plus, you must delete the .rzip, before the new cheat.dat will take effect!

R2 to open MAME Menu on 2003 Xtreme; L3 or Core Options to do the same for 2003 Plus.

Select Cheats, Apply, Resume Game, Rinse and Repeat, Enjoy the Performance/Speed Boost!

---
## [hemantbeast/kernel_oneplus_msm8998](https://github.com/hemantbeast/kernel_oneplus_msm8998)@[9207f14fc4...](https://github.com/hemantbeast/kernel_oneplus_msm8998/commit/9207f14fc4aa4dace6b82b843161437257801e21)
#### Saturday 2022-06-04 13:48:30 by Maciej Żenczykowski

FROMGIT: bpf: Do not change gso_size during bpf_skb_change_proto()

This is technically a backwards incompatible change in behaviour, but I'm
going to argue that it is very unlikely to break things, and likely to fix
*far* more then it breaks.

In no particular order, various reasons follow:

(a) I've long had a bug assigned to myself to debug a super rare kernel crash
on Android Pixel phones which can (per stacktrace) be traced back to BPF clat
IPv6 to IPv4 protocol conversion causing some sort of ugly failure much later
on during transmit deep in the GSO engine, AFAICT precisely because of this
change to gso_size, though I've never been able to manually reproduce it. I
believe it may be related to the particular network offload support of attached
USB ethernet dongle being used for tethering off of an IPv6-only cellular
connection. The reason might be we end up with more segments than max permitted,
or with a GSO packet with only one segment... (either way we break some
assumption and hit a BUG_ON)

(b) There is no check that the gso_size is > 20 when reducing it by 20, so we
might end up with a negative (or underflowing) gso_size or a gso_size of 0.
This can't possibly be good. Indeed this is probably somehow exploitable (or
at least can result in a kernel crash) by delivering crafted packets and perhaps
triggering an infinite loop or a divide by zero... As a reminder: gso_size (MSS)
is related to MTU, but not directly derived from it: gso_size/MSS may be
significantly smaller then one would get by deriving from local MTU. And on
some NICs (which do loose MTU checking on receive, it may even potentially be
larger, for example my work pc with 1500 MTU can receive 1520 byte frames [and
sometimes does due to bugs in a vendor plat46 implementation]). Indeed even just
going from 21 to 1 is potentially problematic because it increases the number
of segments by a factor of 21 (think DoS, or some other crash due to too many
segments).

(c) It's always safe to not increase the gso_size, because it doesn't result in
the max packet size increasing.  So the skb_increase_gso_size() call was always
unnecessary for correctness (and outright undesirable, see later). As such the
only part which is potentially dangerous (ie. could cause backwards compatibility
issues) is the removal of the skb_decrease_gso_size() call.

(d) If the packets are ultimately destined to the local device, then there is
absolutely no benefit to playing around with gso_size. It only matters if the
packets will egress the device. ie. we're either forwarding, or transmitting
from the device.

(e) This logic only triggers for packets which are GSO. It does not trigger for
skbs which are not GSO. It will not convert a non-GSO MTU sized packet into a
GSO packet (and you don't even know what the MTU is, so you can't even fix it).
As such your transmit path must *already* be able to handle an MTU 20 bytes
larger then your receive path (for IPv4 to IPv6 translation) - and indeed 28
bytes larger due to IPv4 fragments. Thus removing the skb_decrease_gso_size()
call doesn't actually increase the size of the packets your transmit side must
be able to handle. ie. to handle non-GSO max-MTU packets, the IPv4/IPv6 device/
route MTUs must already be set correctly. Since for example with an IPv4 egress
MTU of 1500, IPv4 to IPv6 translation will already build 1520 byte IPv6 frames,
so you need a 1520 byte device MTU. This means if your IPv6 device's egress
MTU is 1280, your IPv4 route must be 1260 (and actually 1252, because of the
need to handle fragments). This is to handle normal non-GSO packets. Thus the
reduction is simply not needed for GSO packets, because when they're correctly
built, they will already be the right size.

(f) TSO/GSO should be able to exactly undo GRO: the number of packets (TCP
segments) should not be modified, so that TCP's MSS counting works correctly
(this matters for congestion control). If protocol conversion changes the
gso_size, then the number of TCP segments may increase or decrease. Packet loss
after protocol conversion can result in partial loss of MSS segments that the
sender sent. How's the sending TCP stack going to react to receiving ACKs/SACKs
in the middle of the segments it sent?

(g) skb_{decrease,increase}_gso_size() are already no-ops for GSO_BY_FRAGS
case (besides triggering WARN_ON_ONCE). This means you already cannot guarantee
that gso_size (and thus resulting packet MTU) is changed. ie. you must assume
it won't be changed.

(h) changing gso_size is outright buggy for UDP GSO packets, where framing
matters (I believe that's also the case for SCTP, but it's already excluded
by [g]).  So the only remaining case is TCP, which also doesn't want it
(see [f]).

(i) see also the reasoning on the previous attempt at fixing this
(commit fa7b83bf3b156c767f3e4a25bbf3817b08f3ff8e) which shows that the current
behaviour causes TCP packet loss:

  In the forwarding path GRO -> BPF 6 to 4 -> GSO for TCP traffic, the
  coalesced packet payload can be > MSS, but < MSS + 20.

  bpf_skb_proto_6_to_4() will upgrade the MSS and it can be > the payload
  length. After then tcp_gso_segment checks for the payload length if it
  is <= MSS. The condition is causing the packet to be dropped.

  tcp_gso_segment():
    [...]
    mss = skb_shinfo(skb)->gso_size;
    if (unlikely(skb->len <= mss)) goto out;
    [...]

Thus changing the gso_size is simply a very bad idea. Increasing is unnecessary
and buggy, and decreasing can go negative.

Fixes: 6578171a7ff0 ("bpf: add bpf_skb_change_proto helper")
Signed-off-by: Daniel Borkmann <daniel@iogearbox.net>
Cc: Dongseok Yi <dseok.yi@samsung.com>
Cc: Willem de Bruijn <willemb@google.com>
Link: https://lore.kernel.org/bpf/CANP3RGfjLikQ6dg=YpBU0OeHvyv7JOki7CyOUS9modaXAi-9vQ@mail.gmail.com
Link: https://lore.kernel.org/bpf/20210617000953.2787453-2-zenczykowski@gmail.com

(cherry picked from commit 364745fbe981a4370f50274475da4675661104df https://git.kernel.org/pub/scm/linux/kernel/git/bpf/bpf-next.git/commit/?id=364745fbe981a4370f50274475da4675661104df )
Test: builds, TreeHugger
Bug: 158835517
Bug: 188690383
Signed-off-by: Maciej Żenczykowski <maze@google.com>
Change-Id: I0ef3174cbd3caaa42d5779334a9c0bfdc9ab81f5

---
## [SruthiGomathi/JavaAlgorithmsHackerRank](https://github.com/SruthiGomathi/JavaAlgorithmsHackerRank)@[222fb10fc8...](https://github.com/SruthiGomathi/JavaAlgorithmsHackerRank/commit/222fb10fc804b3038461ecac04223b0a93d19f42)
#### Saturday 2022-06-04 15:10:36 by Sruthi Gomathi

Prepare>Algorithms>Implementation>Bill Division

https://www.hackerrank.com/challenges/bon-appetit/problem

Two friends Anna and Brian, are deciding how to split the bill at a dinner. Each will only pay for the items they consume. Brian gets the check and calculates Anna's portion. You must determine if his calculation is correct.

For example, assume the bill has the following prices: bill = [2,4,6]. Anna declines to eat item k = bill[2] which costs 6. If Brian calculates the bill correctly, Anna will pay (2+4)/2 = 3. If he includes the cost of bill[2], he will calculate (2+3+6)/2 = 6. In the second case, he should refund 3 to Anna.

Function Description
Complete the bonAppetit function in the editor below. It should print Bon Appetit if the bill is fairly split. Otherwise, it should print the integer amount of money that Brian owes Anna.
bonAppetit has the following parameter(s):
bill: an array of integers representing the cost of each item ordered
k: an integer representing the zero-based index of the item Anna doesn't eat
b: the amount of money that Anna contributed to the bill

Input Format
The first line contains two space-separated integers n and k, the number of items ordered and the 0-based index of the item that Anna did not eat.
The second line contains n space-separated integers bill[i] where 0 <= i < n.
The third line contains an integer, b, the amount of money that Brian charged Anna for her share of the bill.

Constraints
2 <= n <= 10^5
0 <= k < n
0 <= bill[i] <= 10^4
0 <= b <= sum bill[i]
The amount of money due Anna will always be an integer

Output Format
If Brian did not overcharge Anna, print Bon Appetit on a new line; otherwise, print the difference (i.e. b_charged - b_actual) that Brian must refund to Anna. This will always be an integer.

Sample Input 0
4 1
3 10 2 9
12

Sample Output 0
5

Explanation 0
Anna didn't eat item bill[1] = 10, but she shared the rest of the items with Brian. The total cost of the shared items is 3+2+9 = 14 and, split in half, the cost per person is b_actual = 7. Brian charged her b_charged = 12 for her portion of the bill. We print the amount Anna was overcharged,1 b_charged - b_actual = 12-7 - 5, on a new line.

Sample Input 1
4 1
3 10 2 9
7

Sample Output 1
Bon Appetit

Explanation 1
Anna didn't eat item bill[1] = 10, but she shared the rest of the items with Brian. The total cost of the shared items is 3+2+9 = 14 and, split in half, the cost per person is b_actual = 7. Because b_actual = b_charged=7, we print Bon Appetit on a new line.

---
## [apljungquist/pilecap](https://github.com/apljungquist/pilecap)@[a4a41248b4...](https://github.com/apljungquist/pilecap/commit/a4a41248b41e5f1231a1613f16542fc881710fa9)
#### Saturday 2022-06-04 15:56:48 by AP Ljungquist

Enable multiple, concurrent environments

There are no tests for this use case but the github actions workflow
has been updated to make use of it which gives it some test coverage.
Pilecap is first installed without deps to ensure we do not install
any unpinned packages that we could use accidentally.

Tox is dropped in CI because it is hard to get it to respect version
locks and it would create only one environment per container anyway.
Tox is kept locally because it makes it easy to iterate over python
versions but the normal steps to install deps and the package are
sidestepped so that pilecap can be bootstrapped and used to install
packages into the environment.

In the Makefile `touch $@` is removed because they were annoying;
I would find myself thinking that a check had passed because there was
no error but in reality the check just had not run.

Json is used to print the environment in the header mostly because it
is easy and somewhat human readable.

Canaria domestica is added as a dev dependency to
* ensure the correct dependencies are installed (I would have added it
  as a run or build dependency since these are more error prone but
  then users would not be able to install this package)
* demonstrate that dev requirements do not interact with shared
  constraints.

The update command is renamed compile to make it easier transitioning
between pilecap and pip-tools.

The --output-file option is added as a way to opt out of the custom
naming without reverting to the make workflow. Make can be used to
generate the same constraints but it is tricky to get both the make
file and the annotations in the constraints file both looking nice.

The compilation and gathering code is refactored to better separate
parts that need to deal with the file system from those that,
theoretically, do not. Functions in the compilation module now take
the destination path as an argument to make it easier getting an
overview of what files are created.

The Marker enum initially had the current_value as value but then
I remembered that deserializing command line arguments using the name
of enum variants couples the code to the interface I changed it and
added the property.

---
## [eleethesontai/lifeos](https://github.com/eleethesontai/lifeos)@[ed7e18a1df...](https://github.com/eleethesontai/lifeos/commit/ed7e18a1df714658ef4128a707287272d4426747)
#### Saturday 2022-06-04 16:32:05 by eleethesontai

Initial Commit

reset

cleaned

cleaned

console shell setup

added folder braindump, added some thoughts aslo

lots of weed fueled inspiration brain dumped.

more dumping.  wish i could take shits like thi.

ready to code the cmd router module

done for the night

cleaned to debug the router issue

reset and hit same bug

got the router to work

work on shell

got the redirect working

save b4 a major paradigm shift

cleaned

more braindumping than code :(

found a method that will work for now.

commit

cleaned

---
## [alienatiz/android_kernel_pantech_msm8937](https://github.com/alienatiz/android_kernel_pantech_msm8937)@[368de85862...](https://github.com/alienatiz/android_kernel_pantech_msm8937/commit/368de858629e7e69f71437c3fcf4be6b7c9e6628)
#### Saturday 2022-06-04 16:52:51 by Masahiro Yamada

modpost: file2alias: go back to simple devtable lookup
commit ec91e78d378cc5d4b43805a1227d8e04e5dfa17d upstream.

Commit e49ce14 ("modpost: use linker section to generate table.")
was not so cool as we had expected first; it ended up with ugly section
hacks when commit dd2a3ac ("mod/file2alias: make modpost compile
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
[haggertk: Backport to 3.4. Omit cpu, hdaudio, ipack, mei, mipscdmm,
 rapidio, ulpi]
Signed-off-by: Kevin F. Haggerty <haggertk@lineageos.org>
Change-Id: Ic632eaa7777338109f80c76535e67917f5b9761c

---
## [ahayworth/opentelemetry-ruby](https://github.com/ahayworth/opentelemetry-ruby)@[45429c7d53...](https://github.com/ahayworth/opentelemetry-ruby/commit/45429c7d537807aad94003f7568650e4a7dc16d2)
#### Saturday 2022-06-04 17:28:23 by Andrew Hayworth

Split CI builds by gems at top-level (#1249)

* fix: remove unneeded Appraisals for opentelemetry-registry

It's not actually doing anything, so we skip it.

* ci: remove ci-without-services.yml

We're going to bring back these jobs in the next few commits, but we can delete it right now.

* ci: remove toys/ci.rb

We're going to replicate this in Actions natively, so that we can get
more comprehensible build output.

* ci: replace toys.rb functionality with an explosion of actions + yaml

This replaces the "test it all in a loop" approach that `toys/ci.rb` was
taking, by leveraging some more advanced features of GitHub Actions.

To start, we construct a custom Action (not a workflow!) that can run
all the tests we were doing with `toys/ci.rb`. It takes a few different
inputs: gem to test, ruby version to use, whether or not to do rubocop,
etc. Then, it figures out where in the repo that gem lives, sets up ruby
(including appraisals setup, if necessary), and runs rake tests (and
then conditionally runs YARD, rubocop, etc).

Then, over in `ci.yml`, we list out all of the gems we currently have
and chunk them up into different logical groups:

- base (api, sdk, etc)
- exporters
- propagators
- instrumentation that requires sidecar services to test
- instrumentaiton that doesn't require anything special to test

For most groups, we set up a matrix build of operating systems (ubuntu,
macos, and windows) - except for the "instrumentation_with_services"
group, because sidecar services are only supported on linux.

For each matrix group (gem + os), we then have a build that has multiple
steps - and each step calls the custom Action that we defined earlier,
passing appropriate inputs. Each step tests a different ruby version:
3.1, 3.0, 2.7, or jruby - and we conditionally skip the step based on
the operating system (we only run tests against ruby 3.1 for mac /
windows, because the runners are slower and we can't launch as many at
once).

Notably, we have a few matrix exclusions here: things that wont build on
macos or windows, but there aren't many.

Finally, each group also maintains a "skiplist" of sorts for jruby -
it's ugly, but some instrumentation just doesn't work for our Java
friends. So we have a step that tests whether or not we should build the
gem for jruby, and then the jruby step is skipped depending on the
answer. We can't really use a matrix exclusion here because we don't use
the ruby version in the matrix at all - otherwise we'd have a *huge*
explosion of jobs to complete, when in reality we can actually install +
test multiple ruby versions on a single runner, if we're careful.

The net effect of all of this is that we end up having many different
builds running in parallel, and if a given gem fails we can *easily* see
that and get right to the problem. Builds are slightly faster, too.

The major downsides are:
- We need to add new gems to the build list when we create them.
- We can't cache gems for appraisals, which adds a few minutes onto the
  build times (to be fair, we weren't caching anything before)
- It's just kinda unwieldy.
- I didn't improve anything around the actual release process yet.

Future improvements could be:
- Figuring out how to cache things with Appraisals, because I gave up
  after a whole morning of fighting bundler.
- Dynamically generating things again, because it's annoying to add gems
  to the build matrices.

* feat: add scary warning to instrumentation_generator re: CI workflows

* fix: remove testing change

* ci: Add note about instrumentation_with_services

---
## [pariahstation/Pariah-Station](https://github.com/pariahstation/Pariah-Station)@[70a87f9510...](https://github.com/pariahstation/Pariah-Station/commit/70a87f95100c290699ce5b92bb099d2f56bbb336)
#### Saturday 2022-06-04 18:24:31 by Gallyus

HOLY SHIT SHUT UP (#742)

* HOLY SHIT SHUT UP

* Apply suggestions from code review

* seeba sauce

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[001ee1d0fb...](https://github.com/mrakgr/The-Spiral-Language/commit/001ee1d0fb90334be430e191b73fa54e27ff6d55)
#### Saturday 2022-06-04 19:35:19 by Marko Grdinić

"1:05pm. Done with breakfast.

1:15pm. Let me finish the chapter of the Legendary Mechanic novel and I will get back to studying style transfer. Whenever I relax, I start to get into fiction more than usual. Let me just finish this and then I will raise the tension.

https://youtu.be/1-26FDZM-Zg?t=812

I agree with the conclussion that NNST looks the best.

https://youtu.be/1-26FDZM-Zg?t=833

Ah, so these are the ones he is comparing them against.

https://youtu.be/1-26FDZM-Zg?t=842

Why can't you do big images with this? Are the intermediate layers that big? It would probably help to have narrower nets for this.

https://youtu.be/1-26FDZM-Zg?t=973

Again, the one in the paper is the best followed by discriminator style transfer. Actually I'd tie them. The discriminator has better face, while NNST has better hair.

https://youtu.be/1-26FDZM-Zg?t=1102

The two on the left are quite shitty.

https://youtu.be/1-26FDZM-Zg?t=1192

I can't help but admire this a little. The discriminator one definitely looks like it has been filtered, but the NNST faithfully reproduces the style.

I have to be on guard against cherry picking in videos like these.

1:40pm. It has some links to vids at the end. Let me check out the paper.

1:45pm. Let me post a link in the /wip/ thread.

2:05pm. Done. I checked GPU prices, and I'd need a RTX 3090 which costs 2.5k dollars to get the necessary memory to run it. If I want to use this, I'll want to make do with less. The easiest path to that would be to use a smaller, narrower NN that whatever model they were using in the paper.

https://arxiv.org/abs/2203.13215
Neural Neighbor Style Transfer

> Due to this requirement, patch-based methods usually expect a specific target domain (e.g., example-based stylization of 3D models [9] or faces [10]) where automatic computation of guidance channels is feasible.

Hmmm, is there anything specific to 3d? I have no idea what patch methods are. I am assuming it has nothing to do with Patch GANs.

> This is possible due to the non-parametric nature of patch-based methods, i.e., their ability to generate stylized images by stitching a set of smaller bitmap chunks copied directly from the style exemplar.

Ah, I see.

> Here we demonstrate how to find a good balance between the overall visual diversity, stylistic fidelity, and content preservation by combining three improvements: (1) zero centering the content and style features, (2) using the cosine distance for measuring feature similarity, (3) performing feature splitting during the nearest-neighbour matching phase which is computed in every iteration of the target feature construction, and most importantly (4) matching individual neural feature vectors rather than patches as proposed in [4, 26].

If it is just this, I should be able to start with regular style transfer and implement these improvements. 1 and 2 should not be hard, but I do not understand what they mean by 3 and 4. I'll have to study this for a while.

But there is a clear path of advancement from vanilla to neural neighbors.

Let me read the paper and then I will watch the other vids on regular style transfer.

> Recent patch-based style transfer algorithms have focused on producing high quality outputs when additional guidance is available

I should consider patch based algorithms simply due to my current hardware constraints. Since I am doing my stuff in 3d, I can in fact produce boundaries.

> In the arbitrary style transfer setting, these approaches performs better than patch-based techniques, nevertheless, methods that use a content and style loss, both based on VGG features, face a fundamental challenge. In general it is impossible to match the statistics of the style features (satisfying the style loss) while keeping the content features unchanged (satisfying the content loss). Even if the content loss is invariant to rotoreflections [24], matching the second order statistics captured by the simplest original style loss [11, 27] generally requires an affine transformation (of which rotoreflections are a subset, and therefore do not provide sufficient invariance).

> In practice we observe that content losses based on deep VGG layers tend to cause photographic high frequencies of the original content to bleed into the final output.

Yeah, this last quote cuts directly to the heart of the issue. I've noticed this as well in the NNST video. I do not think that DDG has this issue though. In fact it has the opposite.

2:35pm. This method might be good enough to immitate Fuzichoco's style.

> In summary there is a statistically significant preference for our fast variant NNST-D over all benchmarked methods (fast and optimization based) except STROTSS, a state-of-the-art optimization based method, for which NNST-D is on par with (STROTSS is preferred but not by a statistically significant margin).

I should check STROTSS out.

> Our approach combined with the method of Texler et al. [46]—the output of NNST-Opt is used as a guide for patch based synthesis algorithm that can operate at notably higher resolution, in this case a 4K resolution output, and thus faithfully preserve high-frequency details (see the zoom-in insets in red squares). At the mid-scale level, however, our technique still outperforms patch-based synthesis as it can convey style features better to delineate salient structures in the content i

> One of the limiting factors of our technique is that using currently available GPUs it can deliver only outputs in moderate resolutions such as 1k. To obtain higher resolution images our technique can be plugged into the method of Texler et al. [46]. In this approach the result of neural style transfer is used as a guide to drive patch-based synthesis algorithm of Fiser et al. [ ˇ 9] that can produce a high-resolution counterpart of the stylized image generated by the neural method (in our case the generated nearest neighbor field is upsampled to obtain a 4K output). Such a combination can help to ensure a more faithful style transfer thanks to the ability to reproduce high-frequency details of the original style exemplar. However, a compromise here is that when comparing middle scale features our technique can perform better than patch-based synthesis since it can adopt the style features to follow salient structures visible in the content image (c.f. Figure 10).

3:05pm. I can't make out a difference on the tiny images in the appendix.

3:15pm. I am done. Let me leave this for later. Right now I'll study the style transfer videos. My priority should be to get a style transfer net that can produce 1920 x 1080 images. Or alternatively square 1k at least. After that I can think of how to improve on the baseline.

Let me take a break here.

3:50pm. Let me resume. I've been thinking about getting a job to get the money for computational resources.

It is not really worth it, but I've put some thought into what would be enough to force me to get a job. Imagine I could only make 512x512 images, but could full res images with better hardware. Then it might be worth it. Imagine I'd needed money for a system like DALLE 2. I'd definitely get a job for that. It would absolutely be worth it.

Right now, I think I'll manage to find ways of getting 1k images myself even with the current hardware. Or I could just use DDG for the time being.

https://youtu.be/S7HlxaMmWAU
Artistic Style Transfer, Now in 3D!

Let me watch this.

https://youtu.be/S7HlxaMmWAU?t=90

100fps using a whoping 4k resolution. Ok, I am listening.

> We present StyleBlit—an efficient example-based style transfer algorithm that can deliver high-quality stylized renderings in real-time on a single-core CPU. Our technique is especially suitable for style transfer applications that use local guidance - descriptive guiding channels containing large spatial variations. Local guidance encourages transfer of content from the source exemplar to the target image in a semantically meaningful way. Typical local guidance includes, e.g., normal values, texture coordinates or a displacement field. Contrary to previous style transfer techniques, our approach does not involve any computationally expensive optimization. We demonstrate that when local guidance is used, optimization-based techniques converge to solutions that can be well approximated by simple pixel-level operations. Inspired by this observation, we designed an algorithm that produces results visually similar to, if not better than, the state-of-the-art, and is several orders of magnitude faster. Our approach is suitable for scenarios with low computational budget such as games and mobile applications.

This might be worth it. Let me check out the video by the authors.

4:05pm. https://towardsdatascience.com/how-to-get-beautiful-results-with-neural-style-transfer-75d0c05d6489

I'll read this later. Forget the 3d paper as well.

https://youtu.be/6KGtaXR7yMU
CS 152 NN—15: Neural Style Transfer: Overview

Let me watch this. I surprised that this is the only class I've found so far. I mean, wasn't style transfer covered in any of the courses elsewhere?

4:15pm. https://youtu.be/6KGtaXR7yMU?t=242

Yeah, focus me. Let me get a moderately good result at my chosen resolution. Then I will see how to deal with the improved methods.

4:30pm. I've decided. I do not care if it causes the training time to double. If I do not have enough memory on my current GPU I will just implement layer checkpointing. For optimization I can just use something like RMSProp. That should be stable in all cases. It is a mostly forgotten optimization method by now because it requires full batch training. But that does not matter when the full batch is 1.

Hmmm, actually, no it does not even have an inputs. The parameters being optimized are the inputs...

Which is still valid. It is essentially a batch size of 0. Consider that RMSProp works for multi layer nets even though the inputs past the input layer change due to the weight changes.

4:35pm. Though it depends. I am not sure why it has such high memory requirements yet. The paper did not get into it. I am assuming due to the large input image spread horizontall across 100s of channels and then vertically across the hidden layers. If that is the problem then checkpointing will allow me to use NNST at the res I want. If not, then I'll have to get back to the drawing board.

Focus me, watch the lesson. Then after that I'll read PyTorch style transfer article above. I also saw a paper on ultra high resolution style transfer by splitting the image into patches. I am not sure how much to believe that, but it might be worth a shot as well fore resolutions higher than 1k.

4:45pm. I am too distracted. I am starting to get into the programming mindset right now.

Even though I did not mean it to, I am obsessed with making NNST work.

My goal to making it work on a GTX 970 will be to implement checkpointing for whatever model they are using. That will lead to reducing the memory consumption by a factor of the sqrt of the number of layers while only doubling the inference times.

I think VGG-19 should have 20-30 layers while only using like 5 for style. This is just about right to reduce the memory expenditure by a factor 4-6. Just what I need!

I am cutting it close here. If I had worse hardware, the plan would not be viable, but it is here.

4:55pm. I am a bit excited. For once my high programming skill will be helpful in my pursuit of art.

https://analyticsindiamag.com/whats-the-big-deal-about-dall-e-2/
> DALL.E was a 12-billion parameter model that worked using a dataset of text-image pairs.

12 billion parameters? Holy shit. I'd need a 48gb GPU just to store its weigths. This is a 500 times bigger than the net I will be using for style transfer. Oh wait, that was the old DALLE.

> More efficient: DALL.E 2 functions on a 3.5-billion parameter model while using another 1.5-billion parameter model to enhance the resolution of its digitally-produced images.

The newer one is 'only' 5 billion.

5pm. What was that strost paper? STROTSS.

https://github.com/nkolkin13/STROTSS

This repo by the same guy of NNST.

https://analyticsindiamag.com/a-hands-on-guide-to-neural-neighbor-style-transfer/

> Also, this instruction will download a VGG pre-trained model of almost 500MB.

That is quite bigger than I expected. Regardless I might be able to make it work. If it is too big I'll try a smaller model.

https://iq.opengenus.org/vgg19-architecture/
> VGG19 is a variant of VGG model which in short consists of 19 layers (16 convolution layers, 3 Fully connected layer, 5 MaxPool layers and 1 SoftMax layer). There are other variants of VGG like VGG11, VGG16 and others. VGG19 has 19.6 billion FLOPs.

///

Conv3x3 (512)
Conv3x3 (512)
Conv3x3 (512)
Conv3x3 (512)
MaxPool

///

Ah damn it does not seem like the size is evenly distributed.

Because the computation is concentrated in the upper layers even if I used checkpointing, at most I'll get a 2x reduction.

I didn't think that the width would be so uneven.

https://arxiv.org/abs/1905.11946
EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks

> Convolutional Neural Networks (ConvNets) are commonly developed at a fixed resource budget, and then scaled up for better accuracy if more resources are available. In this paper, we systematically study model scaling and identify that carefully balancing network depth, width, and resolution can lead to better performance. Based on this observation, we propose a new scaling method that uniformly scales all dimensions of depth/width/resolution using a simple yet highly effective compound coefficient. We demonstrate the effectiveness of this method on scaling up MobileNets and ResNet.

> To go even further, we use neural architecture search to design a new baseline network and scale it up to obtain a family of models, called EfficientNets, which achieve much better accuracy and efficiency than previous ConvNets. In particular, our EfficientNet-B7 achieves state-of-the-art 84.3% top-1 accuracy on ImageNet, while being 8.4x smaller and 6.1x faster on inference than the best existing ConvNet. Our EfficientNets also transfer well and achieve state-of-the-art accuracy on CIFAR-100 (91.7%), Flowers (98.8%), and 3 other transfer learning datasets, with an order of magnitude fewer parameters.

https://pytorch.org/vision/stable/models.html

PyTorch has a bunch of pretrained models.

https://arxiv.org/abs/2201.03545
A ConvNet for the 2020s

Efficient nets caught my eye, they are from the 2019 and have pretty good performance. Whether I can checkpoint them depends on how the use residual connections. Depth dependencies will make it harder.

This one is from 2022 and is at the top of the rankings. Rather than VGG, I should make this my model of choice. Let me read the paper. I want to get a sense of the architexture. I just hope it does not use densenet style connections.

5:35pm. I am going to ask the author whether it would be worth it to adapt their method to a different model that uses less memory.

> Just want to say that your variant of Style Transfer really good! i'm not programmer but i keep eyes on style transfer variations. your variant most simple to install and produces very good quality. Sadly most of "game" GPU's is something around 8-10gb - that makes unable to generate 1024px image. (usually we dont need images higher rhan 1024 because AI upscale can generate 2-4k images from 1024px without loosing too much quality).
> p.s. - interesting that rtx 3060 have 12gb memory. but 3060ti/3070 is 8gb. I tested my rtx 3070 - max dimension of cube is 640px, bigger values return error (not enough memory).

This is a comment in one of the open issues.

5:55pm. https://github.com/nkolkin13/NeuralNeighborStyleTransfer/issues

Opened issue 10 here. My prediction is that I'll get a reply from the author saying he hasn't tried different models. Before I do anything I just want to clear this basic prerequisite. If he says it has and decided on VGG specifically, then I am not sure what I will do, but I guess I might want to try ConvNext anyway. Let me get back to the paper for it.

I think this obstacle in from of me should be something I can cross.

6:05pm. Oh the architecture is simple. In the block they even got rid of batch norm and replaced it with layer norm. The activation is GELU. The block is residual. That is where I should be doing the checkpointing. It is not like Densenets thankfully.

https://paperswithcode.com/method/gelu

Gelu is this. Simple enough.

> We find that ReLU can be substituted with GELU in our ConvNet too, although the accuracy stays unchanged (80.6%).

> Directly substituting LN for BN in the original ResNet will result in suboptimal performance [83]. With all the modifications in network architecture and training techniques, here we revisit the impact of using LN in place of BN. We observe that our ConvNet model does not have any difficulties training with LN; in fact, the performance is slightly better, obtaining an accuracy of 81.5%.

Interesting, interesting.

> Following both ResNets and Swin Transformers, the number of channels doubles at each new stage.

I guess there goes the checkpointing idea. But the tiny or the small versions should be doable.

6:15pm. These sizes are not for the faint of heart. Even the tiny version is 30m params. This is larger than VGG.

I do not get it. Do these nets downsample as they go through the layers?

Let me check out the EfficientNet.

EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks
https://arxiv.org/abs/1905.11946

Maybe I was wrong. It seems that that Efficient net increases the number of channels while downsampling the resolution.

It makes zero sense that the nets would be designed so that the only the upper parts do the majority of the computation.

6:35pm. I've said as much in the issue. Here are the two posts.

///

I have a 4gb GTX 970, but I want to generate 1k images using NNST so I am thinking how I could do that. My first idea would be to implement checkpointing, but I realized that VGG is narrow at the bottom, but wide at the top so rather than a 4x reduction in memory use, it would be more like 2x which is not enough to get me to 1k. I haven't tried your method yet, but I saw a Youtube vid which said it needed 12gb for 1024 x 1024 images. It also said that 6gb are required for 512 x 512 which is probably an error, more likely it needs only 3gb. Is that right?

Anyway, VGG is an old and big architecture, I am looking at more recent ones like EfficientNet and ConvNeXt which should have a better computational design and am considering adapting NNST to them, as well as potentially implementing checkpointing.

Before I undertake that kind of work, I just wanted to ask if you've tried out NNST with different models? If you have and then found that VGG is better, I'd like to hear about that. If not, then it might be worth trying NNST with a ConvNeXt.

///

///

Actually, I might be wrong about VGG being narrow at the bottom and wide at the top. I see in the EfficientNets paper that they downsample the resolution while doubling the number of channels as the data goes up the stages. It makes zero sense that modern nets would be designed so the upper parts do most of the computation, so the same probably applies to the old and big VGG. In that case, checkpointing would be a good idea. I've looked at the ConvNext paper and saw that even the tiny version is bigger than VGG, so a lower memory burden is probably not a reason to pick it over VGG. EfficientNets are indeed smaller.

///

Ok, with this I have enough to assume that checkpointing is the key to getting the 4x memory reduction with VGG.

One thing I am wondering whether it would be worth it to try a Tiny ConvNext anyway despite it taking more memory. I think it should take 50% more than VGG based on the channel numbers, but I am not completely sure. No wait, I should only look at the first input block when estimating the computational expenditure. In that case the number of channels is 96. VGG is 64.

Damn it, just what is that 3,3,9,3 in the block?

> Changing stage compute ratio. The original design of the computation distribution across stages in ResNet was largely empirical. The heavy “res4” stage was meant to be compatible with downstream tasks like object detection, where a detector head operates on the 14×14 feature plane. Swin-T, on the other hand, followed the same principle but with a slightly different stage compute ratio of 1:1:3:1. For larger Swin Transformers, the ratio is 1:1:9:1. Following the design, we adjust the number of blocks in each stage from (3, 4, 6, 3) in ResNet-50 to (3, 3, 9, 3), which also aligns the FLOPs with Swin-T.

These are the blocks in each stage. Just what is this ratio refering to?

Let me check out Swin-T.

> Several Transformer blocks with modified self-attention computation (Swin Transformer blocks) are applied on these patch tokens. The Transformer blocks maintain the number of tokens ( H 4 × W 4 ), and together with the linear embedding are referred to as “Stage 1”. To produce a hierarchical representation, the number of tokens is reduced by patch merging layers as the network gets deeper. The first patch merging layer concatenates the features of each group of 2 × 2 neighboring patches, and applies a linear layer on the 4C-dimensional concatenated features. This reduces the number of tokens by a multiple of 2×2 = 4 (2× downsampling of resolution), and the output dimension is set to 2C. Swin Transformer blocks are applied afterwards for feature transformation, with the resolution kept at H 8 × W 8 . This first block of patch merging and feature transformation is denoted as “Stage 2”. The procedure is repeated twice, as “Stage 3” and “Stage 4”, with output resolutions of H 16 × W 16 and H 32 × W 32 , respectively

I still don't get it.

https://youtu.be/idiIllIQOfU
ConvNeXt: A ConvNet for the 2020s | Paper Explained

Let me watch this for a bit.

https://youtu.be/idiIllIQOfU?t=1450

Let me just skip to the stage ratio.

https://youtu.be/idiIllIQOfU?t=1548

This is a pretty good explanation. Way more than I would expected. I am really just curious how this affects the memory expenditure at each stage.

> ConvNeXt-T: C = (96, 192, 384, 768), B = (3, 3, 9, 3)

Ahhhh. I am so foolish to not have realized this earlier. This means 3 layers with chanel size of 96, then 3 layers with channel size of 192, then 9 layers of channel size of 384 and so on. This comes up to 18 layers. This is not hard to understand at all.

And yes, having 18 extra layers in the small version would definitely impact the memory use. What about VGG 19?

2,2,4,4,4. 16 conv layers exactly. The Tiny Convext is 50% larger due to channels and has 2 extra layers. I'll stick with VGG then.

The checkpointing idea is in. But now what might mess it up is if the style layers aren't evenly spaced out. If they are packed in the middle that will make things more difficult.

7:10pm. When it comes to implementing checkpointing, I can isolate segments and create a genetic run_with_checkpoint function. It won't be a problem. I'll find a way to do this. The only trouble I'll have if a function outputs multiple results. That would make things hard.

Well, handle it when it comes to that.

I'll find a way around the potential troubles. Now, let me go back to the style transfer video.

7:15pm. Actually before that, let me think a bit more.

1024 x 1024 x 3 = 3mb for a single image at the 1k resolution.

16 layers * 64 channels = 1024

So that is 3gb. But the activation functions and the polling layers and BN will also need to take up memory. So 12gb indeed seems reasonable.

Let me think. Suppose the regular block takes up BN and the activation. That means the 16 layers of VGG would take up 9gb. Could the last 3 be taken up by the pooling layers. 5 Max pooling layers. Probably not. I can't see them taking up more than 200mb each.

Nevermind this. It does not matter.

Style Transfer by Relaxed Optimal Transport and Self-Similarity

Actually, let me take a look at this paper and then I will watch the lectures. I want to try out the NNST personally. It is fine if it at something like 256 x 256 resolution just to start me off.

7:30pm. Ah, I just realized that VGG16 and VGG19 might refer to the number of layers in the net rather than the year of paper's publication. Silly me.

8:20pm. Done with lunch. I've realized that when considering the memory consumption reduction of checkpointing I neglected to think about the inner block reduction. That is at least 3x right there. I could checkpoint 3x and get that much reduction. Do it every two blocks and I'd get 6x.

8:35pm. Done with the STROST paper. Let me watch the lectures and I'll close for the day.

https://youtu.be/AJOyMJjPDtE?t=560

So the Gram matrix is just a covariance matrix derived from tensors. Yeah, I see.

Hmmm, this, no it is not too bad.

At most it will be 512^2 in a VG net. 250k is not much.

https://youtu.be/AJOyMJjPDtE?t=808

This is a really good explanation, but what way the content loss again?

https://youtu.be/c4vuR4vHKd0
CS 152 NN—15: Neural Style Transfer: Content Loss

I missed this video.

9:10pm. So it is just a MSE of the elements in the final layer. Easy enough.

9:15pm. Ok, I get it. With the knowledge from these 3 vids by Neil Rhodes I could implement my own style transfer without even looking at any of the existing implementations. It is coming to me. For the NNST, I am going to have to look at the implementation. I did not understand the paper completely. If I was a beginner I'd take time playing with vanilla, but instead I will just get started on the NNST tomorrow. The first order of business will be to actually run it. I'll have to upgrade PyTorch, maybe Cuda, and adapt it to Windows. I think the authors are using Linux, and I'll have to put some effort into bringing it over if it is needed.

I'll first get it to run on tiny images and then find the size limit on my GTX 970. Then I will implement checkpointing and get that >6x factor memory reduction. This should be enough to move to 1024 x 1024 from whatever the limit on my machine is. With this I will break the dependency on the deep dream generator.

I should look at NN upresing after that. I've seen it increase the resolution by 4x on both axes while still retaining quality, so it should be good for hitting my target.

9:30pm. Let me close here.

I think that maybe art is not like programming after all. I do not obsess in the same manner over art. I forgot what programming was like. Tomorrow will be a fun little return. This time I will get a definite gain from ML. Such occurence are a part of the true path. A true path sustains you rather than just demanding sacrifices."

---
## [hairyhenderson/yaml](https://github.com/hairyhenderson/yaml)@[7649d4548c...](https://github.com/hairyhenderson/yaml/commit/7649d4548cb53a614db133b2a8ac1f31859dda8c)
#### Saturday 2022-06-04 19:47:07 by Gustavo Niemeyer

Revert v2 line length change as discussed in #670

It was clearly a mistake to accept the default formatting change in v2,
and now there's no ideal choice. Either we revert the change and break
some projects twice, or we keep the change and break some projects once.
Given the report comes from Kubernetes, which has a relevant community
and code size, we'll revert it. At the same time, to simplify the life
of those that already started migrating towards the v3 behavior, a new
FutureLineWrap function is being introduced to trivially preserve the
new behavior where desired.

The v3 branch is not affected by this, and will retain the default
non-wrapping behavior. It will also be changed soon to support per
arbitrary line-wrapping for individual encoding operations.

Thanks to everyone who offered code and ideas, and apologies for
the trouble.

---
## [Zonespace27/Pariah-Station](https://github.com/Zonespace27/Pariah-Station)@[c77fb1e795...](https://github.com/Zonespace27/Pariah-Station/commit/c77fb1e7959bec41276673ba903da1625be8b68e)
#### Saturday 2022-06-04 20:45:19 by Octus

Parallax but better: Smooth movement cleanup (#66567) (#724)

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

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [openhab-sandbox/org.openhab.binding.zwave](https://github.com/openhab-sandbox/org.openhab.binding.zwave)@[7e710866ea...](https://github.com/openhab-sandbox/org.openhab.binding.zwave/commit/7e710866ea8041a7e80b60d8b72a0534a5e89a6e)
#### Saturday 2022-06-04 20:58:46 by Robert Eckhoff

Zwave battery device optimization (#1760)

* “One and DONE” - Zwave battery device optimization

This PR is to optimize the user experience of initializing new Zwave battery devices. The desired result is to be able to put a battery in the shiny new device, follow the device manual inclusion protocol during an Inbox, Zwave binding “Scan” mode of OpenHab and, in 20 seconds or less, have all the channels displayed and begin to link them to items. “One and DONE”.
Since my last unmerged battery device PRs I have replaced the fixed 20 second cap in the iterative sleep timer with a user defined maximum “hold awake” parameter. As the user defined default is five seconds, there is no implied maintainer approval of a longer awake duration. Kind of a “use at your own risk” feature. Once the device is DONE (or the cap is reached) the sleep message (No More Information-NMI) is created. Setting a higher user defined cap does not mean increased battery usage. With half second intervals, versus 5 seconds in today’s binding, daily battery device awake duration is either the same or reduced.
Also added is a kick-Queue action after the half second mark in the Timer Task to get a potentially “stuck” device queue going again. In some scenarios (primarily during initialization, the existing kick-Queue action appears to happen too early (before the event listener sets the device awake). There are examples from the forum in my attached document. I was able to recreate the “stuck” scenario (by reverting the second “Add Node Stop” & Sleep Timer cap to 5 seconds) and resolve the “stuck” problem on my test device with this additional kick-Queue.
Lastly, I have added the shortened timeout for the second calling of the “Add Node Stop” to make this a complete package. It has the most impact as anything else to “One and DONE”. The default 5 seconds to cancel this command eats up about 4 seconds of the Timer leaving only one second left in the initial awake interval. Some of the other enhancements in this PR would have less impact, if a full 5 seconds were available for device initialization after device discovery.
I have all the changes in this PR running, some for as long as 8 months (as of Jan 2022). I have 13 battery nodes of various manufacturers (47 total) on an Rpi4 with an Rpi3b test system. It is frustrating to see the battery device initialization issues in the forum, as I know they can be resolved better than the standard “reawake many, many times” advice. These changes will save considerable user frustration and many seconds of battery usage.
Signed-off-by: Bob Eckhoff <katmandodo@yahoo.com>

* Requested Changes mostly

We still need to discuss my appeal on the AddNode Stop and get on the same page on how the count works.  It is not the same as in #1100 with the "return;"
Signed-off-by: Bob Eckhoff katmandodo@yahoo.com

* Delete AddNode changes

Mainly delete the changes in the Addnode class, plus address other minor changes

Signed-off-by: Bob Eckhoff katmandodo@yahoo.com

* Update README with maxAwakePeriod

Added section of maxAwakePeriod in the README, added a missing line, commented on the kickQueue.

Signed-off-by: Bob Eckhoff <katmandodo@yahoo.com>

* Update maxAwake without initialization and xml edits

Your suggestion led me to realize I could “push” the maxAwakePeriod from the ZWaveControllerHandler configuration editor down to the ZwaveController where it could be “pulled” by the Zwave Node. It’s not exactly how you suggested, but I wanted to make the smallest possible amount of changes, so as to not mess up the other parameters. Not a lot of testing, but I could change in the UI and check in the wake Timer Task that it was being used.  It also still could be changed via re-initialization using the UI page “code” tab, so I think it is good.
Also in the commit I changed the default maxAwakePeriod to 10 seconds and raised the minimum back to 5. With the AddNode changes removed (adding 4 seconds of inactivity), the minimum of 2 seconds will simply not work. As to the default, I detailed 2 tests at 5 seconds and two at 10 seconds and summarized them below

Node	Max Awake	# of awakes to DONE	Total User time Fiddling with Action button	Total Device Awake (inludes late starts, message timeouts)
2	5 seconds	6	6 minutes 40 seconds	22.7 seconds
3	5	4	2 minutes 40 seconds	24.1 seconds
4	10	1	6.5 seconds (estimated-zniffer)	6.5 seconds
6	10	1	 8 seconds	8 seconds

Once a partially initialized device needs to reawake, it is not seamless and a 10 second cap uses less battery time than a 5 second cap. Also this was me pressing the button and checking the device in the UI and I knew to keep at it.  Not everyone understands the need to keep pressing the action button with high frequency.  I would be a little sad that after all the work here, the default settings would only be slightly better than now. Yes, the parameter is now easy to change, but that is an extra step and is currently an advanced setting. I’d strongly prefer we start at 10 seconds and let people lower it if they think it is a problem (although my data proves it is not).
I also made some edits to the program comments, the JavaDocs and took out an unused method.

Signed-off-by: Bob Eckhoff <katmandodo@yahoo.com>

* Attempt to fix .classpath& .project

Per my last comment these are autogenerated and should not be changed.
Signed-off-by: Bob Eckhoff <katmandodo@yahoo.com>

* Move single use variable to where it is used?

I hope this is what you were looking for.  It's late on this side of the world, but though I would try to fix now.  If wrong, let me know and I will fix in AM.
Signed-off-by: Bob Eckhoff <katmandodo@yahoo.com>

* Remove unneeded variable

I was also wondering if this was needed, but once I got it working did not want to mess with it !  Anyway it is gone now.
Signed-off-by: Bob Eckhoff <katmandodo@yahoo.com>

* Change passed variable to int

This has worked for a few days, but it seems maxAwakeProperty should be int, not Integer.  I was converted to int in the Controller Handler. If not right I can revert..
Signed-off-by: Bob Eckhoff <katmandodo@yahoo.com>

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[caa0f99ab9...](https://github.com/treckstar/yolo-octo-hipster/commit/caa0f99ab93ae75ecaf1cabb193b1279095d62cc)
#### Saturday 2022-06-04 22:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [nekoyoubi/bitburner](https://github.com/nekoyoubi/bitburner)@[2df67669d1...](https://github.com/nekoyoubi/bitburner/commit/2df67669d166a82c1ff57189d626360cfac2ac23)
#### Saturday 2022-06-04 23:15:22 by Nekoyoubi

1.2 - 2.1 - [4.1]

- updated /servers/buy.js
  - fixed(?) some timing issues around server deleting and re-buying
  - changed the hack requirement for what gets auto'd to half of the player's level
  - removed the `- 4` ram on determining threads, as we don't `goto` from player servers
  - added a timestamp to the logs because not having it is a hell of an oversight
  - reduced the overall iteration wait; 60 -> 20
  - did some "math" to allow the amount of outgoing hacks to be more in line with the scope of the server
- updated factions.js
  - made city factions smarter, maybe; will auto join grouped city factions if you're already in one
  - hoisted the hack factions into a variable
  - replaced the singularity connect with my goto.js so it would... work
- updated loic.js with similar adjustments to that of /servers/buy.js re: reserved RAM and hack skill
- updated unlock.js to use the hack skill threshold mentioned above
- added a call to map.js and factions.js to wakeup.js where appropriate

---
## [Darlantanis/CHOMPStation2](https://github.com/Darlantanis/CHOMPStation2)@[e502b637e9...](https://github.com/Darlantanis/CHOMPStation2/commit/e502b637e9893a197cfa641cc5f03ede77a2860d)
#### Saturday 2022-06-04 23:42:14 by Rykka

Trait Addition + Adjustments

Polaris Combat is ass.
Yes, bandaid trait fixes are not necessarily the solution, BUT!

All of our negatives have extreme versions, without any sort of positive counterpart, and the positives we DO have are weak.
However, a flat 50% reduction on both incoming burn/brute would be too much, therefore:

Trait changes as follows.
- Added Glass Endurance. You have 25 HP, or 50 total HP, before you die. Don't get hit, and with Baymissn't? You're a masochist.
- Brute/Burn Resists no longer exclude High/Very High Endurance.
- Major Burn/Brute Resist re-added: These provide a 40% DR (Damage Reduction), at the cost of 3 points. This is opposite to Major Weakness, which is a 50% incoming damage increase.
- Very High Endurance re-added: This increases your max HP to 150.
- Increased Pain Tolerance: Similar to Increased Pain INtolerance, you have a 40% DR on incoming pain, compared to, for Intolerance, a 50% increase on incoming pain.
- Lick Wounds added back as a 1-cost Positive trait. I wondered why I hadn't seen it - it'd been disabled for _two years_ since Jan 2020.

Now, this is very likely to be controversial as it's a VERY huge balance change. Please don't bite my head off - this came up in discussion with Serdykov in DMs, and after digging through PRs, I discovered that traits had been disabled/removed for 1-2 years.

Pending a rewrite of Polariscode combat, and/or significant tweaks to make it more palatable, this will allow for more tankiness in combat - at the cost of extreme downsides. You can't suddenly become a hulk in combat with just traits, you still have to take some heavy downsides.

For instance:
Base Points - 1
Total Traits - 8

Very High Endurance - 4
Major Burn Resist - 3
Major Brute Resist - 3
Increased Pain Tolerance - 3

Current Points -12
Current Traits Left - 4

Conductive Major - -3
Extreme Photosensitivity - -2
Haemophilia - -3
Major Loneliness - -5

Current Traits Left - 0
Current Points 1

I'd be interested in looking at making Major Brute/Burn resist 4 points to equal 40% incoming DR, but that feels odd, given the negative is 50% incoming damage total for only 3.
I'd also be open to considering making VH Endurance even more expensive to 6, since it can be taken simultaneously now, and making base High Endurance cost 4.

---

