## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-02-03](docs/good-messages/2022/2022-02-03.md)


1,735,287 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,735,287 were push events containing 2,915,507 commit messages that amount to 211,688,487 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 36 messages:


## [conceptdev/maui](https://github.com/conceptdev/maui)@[ac6befcbee...](https://github.com/conceptdev/maui/commit/ac6befcbee23fae2bd358d9ed3217757029a9d1f)
#### Thursday 2022-02-03 00:10:37 by Jonathan Peppers

[controls] Brush.Foo should return immutable instances (#3824)

When profiling a `dotnet new maui` app, with this package:

https://github.com/jonathanpeppers/Mono.Profiler.Android

The `alloc` report shows:

    Allocation summary
    Bytes      Count  Average Type name
    39984        147 2 72     Microsoft.Maui.Controls.SolidColorBrush

Stack trace:

    38352 bytes from:
    (wrapper runtime-invoke) object:runtime_invoke_void (object,intptr,intptr,intptr)
    Microsoft.Maui.Controls.VisualElement:.cctor ()
    (wrapper runtime-invoke) object:runtime_invoke_void (object,intptr,intptr,intptr)
    Microsoft.Maui.Controls.Brush:.cctor ()

Reviewing the `Brush` class, there are indeed 147 `SolidColorBrush`
created on startup that are stored in fields.

But what is weird about this, is that `SolidColorBrush` is mutable!

    public Color Color
    {
        get => (Color)GetValue(ColorProperty);
        set => SetValue(ColorProperty, value);
    }

So I could literally write code like:

    Brush.Blue.Color = Colors.Red;

Blue is red! (insert evil laughter?)

I think the appropriate fix here is that all of these `static
readonly` fields should just be properties that return a new
`ImmutableBrush`. We can cache the values in fields on demand. Then
someone can't do something evil like change `Blue` to `Red`?

I reviewed WPF source code to check what they do, and they took a
similar approach:

https://github.com/dotnet/wpf/blob/5e8187344b2b561ef08b9ca2735cd89cbdd3c11e/src/Microsoft.DotNet.Wpf/src/PresentationCore/System/Windows/Media/brushes.cs#L33-L1586

We should make this API change now before MAUI is stable, and we have
the side benefit to save 39984 bytes of memory on startup?

I added tests for these scenarios, and discovered 3 typos for `Brush`
colors that listed the wrong color.

---
## [Buildstarted/linksfordevs](https://github.com/Buildstarted/linksfordevs)@[d3b32d5fc9...](https://github.com/Buildstarted/linksfordevs/commit/d3b32d5fc93a40064b14af116cd1e06583cacf88)
#### Thursday 2022-02-03 01:07:57 by Ben Dornis

Updating: 2/3/2022 1:00:00 AM

 1. Added: Finding unknown sensors with I²C probing
    (https://ansari.sh/posts/finding_sensors_i2c/)
 2. Added: Don’t Add Salt to Baby Food: The Surprisingly Weak Evidence for Infant Sodium Requirements - Lily Nichols RDN
    (https://lilynicholsrdn.com/salt-baby-food-infant-sodium-requirements/)
 3. Added: Hacks for engineering estimates - shubhro.com
    (https://www.shubhro.com/2022/01/30/hacks-engineering-estimates/)
 4. Added: Procrastination by Reading
    (https://oykun.com/stop-reading-start-doing/)
 5. Added: Rishi Goomar
    (https://rishigoomar.com/blog/thoughts-on-4-day-work-week)
 6. Added: Caching Header Best Practices
    (https://simonhearne.com/2022/caching-header-best-practices/)
 7. Added: I took down Starlink (but I haven't cancelled)
    (https://www.jeffgeerling.com/blog/2022/i-took-down-starlink-i-havent-cancelled)
 8. Added: blog.pangalos.dev
    (https://blog.pangalos.dev/posts/svelte-post/)
 9. Added: Improving Powkiddy V90's Portable Experience
    (https://jahed.dev/2022/01/25/improving-powkiddy-v90-ux/)
10. Added: Expo 2020
    (https://ivanludvig.github.io/blog/2022/02/02/expo-2020.html)
11. Added: How I used indie hacking to sponsor my own greencard | Swizec Teller
    (https://swizec.com/blog/how-i-used-indie-hacking-to-sponsor-my-own-greencard)
12. Added: Let’s build something Outrageous – Part 17: Bulk Traversals
    (https://maxdemarzi.com/2022/01/31/lets-build-something-outrageous-part-17-bulk-traversals/)
13. Added: Settings are not a design failure
    (https://linear.app/blog/settings-are-not-a-design-failure)
14. Added: Wikipedia and irregular data: how much can you fetch in one expression?
    (https://zverok.github.io/blog/2022-01-27-wikipedia_ql-phrases.html)
15. Added: Cache invalidation isn't a hard problem
    (https://codeopinion.com/cache-invalidation-isnt-a-hard-problem/)

Generation took: 00:07:46.6417565
 Maintenance update - cleaning up homepage and feed

---
## [damerell/crawl](https://github.com/damerell/crawl)@[4f05a2621e...](https://github.com/damerell/crawl/commit/4f05a2621efbc8de7bbc8216d5359d91de0a0803)
#### Thursday 2022-02-03 02:20:39 by David Damerell

Rot heals with XP

Partly because I hate being down one lousy max HP, and partly
because we've restored AF_ROT to ugly things.

---
## [avar/git](https://github.com/avar/git)@[f960ba4a21...](https://github.com/avar/git/commit/f960ba4a219c03c03ffb9677f5908942c48d79b8)
#### Thursday 2022-02-03 02:25:20 by Ævar Arnfjörð Bjarmason

object-file.c: do fsync() and close() before post-write die()

Change write_loose_object() to do an fsync() and close() before the
oideq() sanity check at the end. This change re-joins code that was
split up by the die() sanity check added in 748af44c63e (sha1_file: be
paranoid when creating loose objects, 2010-02-21).

I don't think that this change matters in itself, if we called die()
it was possible that our data wouldn't fully make it to disk, but in
any case we were writing data that we'd consider corrupted. It's
possible that a subsequent "git fsck" will be less confused now.

The real reason to make this change is that in a subsequent commit
we'll split this code in write_loose_object() into a utility function,
all its callers will want the preceding sanity checks, but not the
"oideq" check. By moving the close_loose_object() earlier it'll be
easier to reason about the introduction of the utility function.

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>

---
## [987123879113/mame](https://github.com/987123879113/mame)@[a49e215466...](https://github.com/987123879113/mame/commit/a49e2154666b0ee7423e2d859c21b7592a4c61b8)
#### Thursday 2022-02-03 05:13:48 by Firehawke

Apple II updates for January 2022 (#9189)

* New working software list additions (apple2_flop_clcracked.xml)
---------------------------------------------------------------

Earth Science: Interplanetary Travel (cleanly cracked) [4am, Firehawke]
Isaac Newton and F.I.G. Newton (cleanly cracked) [4am, Firehawke]
Return to Reading: The Call of the Wild (cleanly cracked) [4am, Firehawke]
The German Hangman (cleanly cracked) [4am, Firehawke]
Legionnaire (cleanly cracked) [4am, Firehawke]

* New working software list additions (apple2_flop_clcracked.xml)
---------------------------------------------------------------

Bridge Tutor with Precision and Scientific Bidding (cleanly cracked) [4am, san inc, Firehawke]
The French Hangman (cleanly cracked) [4am, Firehawke]
The Russian Hangman (cleanly cracked) [4am, Firehawke]

* New working software list additions (apple2_flop_orig.xml)
----------------------------------------------------------

Mickey's Space Adventure [4am, Firehawke]
The Environment Life Dynamic [4am, Firehawke]

* New working software list additions (apple2_flop_orig.xml)
----------------------------------------------------------

Stellar Power [4am, Firehawke]

New working software list additions (apple2_flop_clcracked.xml)
---------------------------------------------------------------

Ken Uston's Professional Blackjack (Version 1.12) (cleanly cracked) [4am, Firehawke]
Dinosaur's Lunch (cleanly cracked) [4am, Firehawke]
Race Car Keys (cleanly cracked) [4am, Firehawke]
Functional Harmony: Basic Chords (cleanly cracked) [4am, Firehawke]
Functional Harmony: Diatonic Seventh Chords (cleanly cracked) [4am, Firehawke]
Functional Harmony: Borrowed and Altered Chords (cleanly cracked) [4am, Firehawke]
Building Reading Skills: The Letter-Sound Farm (cleanly cracked) [4am, Firehawke]
Follow Me (cleanly cracked) [4am, Firehawke]

* New working software list additions (apple2_flop_clcracked.xml)
---------------------------------------------------------------

The German Hangman (Revision 2) (cleanly cracked) [4am, Firehawke]
The Russian Hangman (Revision 2) (cleanly cracked) [4am, Firehawke]
The Spanish Hangman (Revision 2) (cleanly cracked) [4am, Firehawke]

* New working software list additions (apple2_flop_clcracked.xml)
---------------------------------------------------------------

Exploring Library Land (cleanly cracked) [4am, Firehawke]
Library Treasure Hunt (cleanly cracked) [4am, Firehawke]
Expedition U.S.A.! (cleanly cracked) [4am, Firehawke]
Codes and Cyphers (cleanly cracked) [4am, san inc, Firehawke]
Ripley's Believe It Or Not: Beginning Library Research Skills (cleanly cracked) [4am, Firehawke]

* New working software list additions (apple2_flop_orig.xml)
----------------------------------------------------------

Glutton [4am, Firehawke]

---
## [Texera/texera](https://github.com/Texera/texera)@[c3af4463f4...](https://github.com/Texera/texera/commit/c3af4463f486c9cf001cb547b29b6189a3c8302f)
#### Thursday 2022-02-03 07:32:53 by Albert Liu

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
## [AvanaPY/DV1655_Lab1](https://github.com/AvanaPY/DV1655_Lab1)@[db860507ea...](https://github.com/AvanaPY/DV1655_Lab1/commit/db860507eaa2f221ac415204e0fbc3185a0f318d)
#### Thursday 2022-02-03 07:59:29 by Emil Karlström

killed all shift/reduce errors, oh my god fuck you

---
## [ykjit/yk](https://github.com/ykjit/yk)@[e953b799d0...](https://github.com/ykjit/yk/commit/e953b799d06f38923c25ef73d45dae4bcfba660d)
#### Thursday 2022-02-03 09:18:57 by Laurence Tratt

Don't grab the THREAD_MTTHREAD on every control point call.

We can't rely on thread locals being fast (on some platforms they are,
on some they aren't; Rust's thread locals are, currently, not fast
because of the lazy loading) so we want to avoid accessing them in the
control point's fast paths.

This commit moves loading from the `THREAD_MTTHREAD` thread local to
only those portions of code that really need access to it. Mostly this
is fairly simple, but there is one horrible hack in here that will
probably haunt me in my dreams until I can think of a better way of
doing this.

However, getting rid of this thread local should be worth it, as it will
allow us to port back more of the old test suite. At that point,
refactoring the evil hack should be doable with more confidence, because
there'll be a test suite to catch (at least some) errors!

---
## [IMAU-paleo/UFEMISM](https://github.com/IMAU-paleo/UFEMISM)@[b6955a8ddb...](https://github.com/IMAU-paleo/UFEMISM/commit/b6955a8ddb85e5506715ae51949c7a68cb5a15a2)
#### Thursday 2022-02-03 09:57:34 by TijnBerends

Small remapping change

Reintroduced the old CSR-format matrices into the remapping module, to greatly reduce memory use.

When constructing the remapping matrices, the number of non-zeros (both per row and in total) is unknown in advance, and can vary greatly across the rows. Preallocating memory with PETSc is a pain in the ass, but not doing so makes it insanely slow (since apparently when it runs out, it allocates new memory which is only one single element larger, so that it has to copy the arrays every time a single element is added). However, PETSc also has a routine for setting up a PETSc matrix directly from a set of CSR arrays (which are only very slightly differently formatted from the UFEMISM ones). What I did therefore is to use my own CSR routines for setting up the line integral matrices (since my own memory expansion routines are much more efficient), then convert them to PETSc matrices once they're finished, and move on with the PETSc matrix operations from there. This seems to be a good compromise between computational speed and memory use.

---
## [Apachenalgas/docs](https://github.com/Apachenalgas/docs)@[962bc035d8...](https://github.com/Apachenalgas/docs/commit/962bc035d80c186fa42ced6b84d3be69bf72af7c)
#### Thursday 2022-02-03 10:31:38 by Apachenalgas

Update quickstart.md

Skip to content
Sign up
This repository has been archived by the owner. It is now read-only.
imknown
/
BetterTextClockBackport
Public archive
[Deprecated] Backport Android 4.2 TextClock to Android 1.6+ with some codes of 12/24 format control.

 Apache-2.0 License
 15 stars  2 forks
Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
Latest commit
@imknown
imknown
…
on Jun 1, 2017
Git stats
Files
README.md
BetterTextClockBackport
Backport Android 4.2 TextClock to Android 1.6+ with some codes of 12/24 format control.

Screen record
This is the gif of version 1.0.0, NOT the latest!  
github

Sample code
<net.imknown.bettertextclockbackportlibrary.TextClock
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    app:forceUse="format24"
    app:format24Hour="k:m:s"/>
For more info, plz see the sample: xml layout & java code.  

Install to project from jCenter
Gradle dependency
compile 'net.imknown:BetterTextClockBackportLibrary:1.0.1'
Maven dependency
<dependency>
 <groupId>net.imknown</groupId>
 <artifactId>BetterTextClockBackportLibrary</artifactId>
 <version>1.0.1</version>
 <type>pom</type>
</dependency>
Google AOSP code reference to:
https://android.googlesource.com/platform/frameworks/base/+/master/core/java/android/view/RemotableViewMethod.java
https://android.googlesource.com/platform/frameworks/base/+/master/core/java/android/widget/TextClock.java
https://android.googlesource.com/platform/frameworks/base/+/master/core/java/android/text/format/DateFormat.java

Some Todo code reference to:
https://github.com/vojtech/android-textclock-backport

License
Copyright 2016 imknown

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
Releases
No releases published
Packages
No packages published
Languages
Java
100.0%
© 2022 GitHub, Inc.
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
https://android.googlesource.com/platform/frameworks/base/+/master/core/java/android/widget/TextClock.java.  Maplebear Inc. (d/b/a Instacart), 50 Beale St. #600 San Francisco, CA 94105http://www.apache.org/licenses/LICENSE-2.0 I like piss in this software mouth andshet in his mother's indian apache asshol. I'm the darkness bitch.. u listen too meeeeeeeeeee.. if u have satan mind and Jesus blood then you my friend will have enternal life .Amen

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[079f8ac515...](https://github.com/tgstation/tgstation/commit/079f8ac51554bb338ac5826c9d06c8d4bc10be80)
#### Thursday 2022-02-03 10:57:58 by LemonInTheDark

Adds moveloop bucketing, uses queues for the singulo rather then sleeps (#64418)

Adds a basic bucketing system to move loops.

This should hopefully save a lot of cpu time, and allow for more load while gaining better smoothness.

The idea is very similar to SStimer, but my implementation is much more simple, since I have to worry less about long delays and redundant buckets.
Insertion needs to be cheaper too, since I'm making a system that by design holds a lot of looping things

It comes with some minor tradeoffs, we can't have constant rechecking of loops if a move "fails", not that we really want that anyway
We also lose direct control over the timer var, but I think that's better, don't want people manipulating that directly
Not that it even really worked very well back when we did have it
Removes the sleep from singularity code

Rather then using sleep to store the state of our iteration, we instead queue the iteration in a list.
We then use a custom singulo processing subsystem to call our "digest" proc several times per full eat, with the hope of staying on top of
our queue
This rarely happens because the queue is too large, god why is a sm powered singulo 24x24 tiles.

I've also A: cached our dist checks, and B: Added dist checks to prevent attempting to pull things out of range
This might look a bit worse, but it saves a lot of work

Oh right and I made the singulo unable to eat while it still has tiles to digest. The hope is to prevent
overwork and list explosion.

Hopefully this will prevent singulo server stoppage, though I've seen some other worrying things in testing.

---
## [GabrielePicco/CryptoBuzz](https://github.com/GabrielePicco/CryptoBuzz)@[82d91b28ca...](https://github.com/GabrielePicco/CryptoBuzz/commit/82d91b28ca770b2602c0f866343438b2988fa36c)
#### Thursday 2022-02-03 11:14:35 by root

Adding article: Aussie tycoon sues Facebook over crypto scams. I believe we all should sue this blood sucking, data leaking Lizards company. (61fbb8f6e1dca226255cf09c)

---
## [oracle/dtrace-linux-kernel](https://github.com/oracle/dtrace-linux-kernel)@[9281288bb0...](https://github.com/oracle/dtrace-linux-kernel/commit/9281288bb0f1de51b2f7f091cce1234c9f26b121)
#### Thursday 2022-02-03 14:23:04 by Nick Alcock

waitfd: new syscall implementing waitpid() over fds

This syscall, originally due to Casey Dahlin but significantly modified
since, is called quite like waitid():

	fd = waitfd(P_PID, some_pid, WEXITED | WSTOPPED, 0);

This returns a file descriptor which becomes ready whenever waitpid()
would return, and when read() returns the return value waitpid() would
have returned.  (Alternatively, you can use it as a pure indication that
waitpid() is callable without hanging, and then call waitpid()).  See the
example in tools/testing/selftests/waitfd/.

The original reason for rejection of this patch back in 2009 was that it
was redundant to waitpid()ing in a separate thread and transmitting
process information to another thread that polls: but this is only the
case for the conventional child-process use of waitpid().  Other
waitpid() uses, such as ptrace() returns, are targetted on a single
thread, so without waitfd or something like it, it is impossible to have
a thread that both accepts requests for servicing from other threads
over an fd *and* manipulates the state of a ptrace()d process in
response to those requests without ugly CPU-chewing polling (accepting
requests requires blocking in poll() or select(): handling the ptraced
process requires blocking in waitpid()).

There is one ugliness in this patch which I would appreciate suggestions
to improve (due to me, not due to Casey, don't blame him).  The poll()
machinery expects to be used with files, or things enough like files
that the wake_up key contains an indication as to whether this wakeup
corresponds to a POLLIN / POLLOUT / POLLERR event on this fd.  You can
override this in your poll_queue_proc, but the poll() and epoll() queue
procs both have this interpretation.

Unfortunately, this is not true for waitfds, which wait on the the
wait_chldexit waitqueue, whose key is a pointer to the task_struct of
the task being killed.  We can't do anything with this key, but we
certainly don't want the poll machinery treating it as a bitmask and
checking it against poll events!

So we introduce a new poll_wait() analogue, poll_wait_fixed().  This is used
for poll_wait() calls which know they must wait on waitqueues whose keys are
not a typecast representation of poll events, and passes in an extra
argument to the poll_queue_proc, which if nonzero is the event which a
wakeup on this waitqueue should be considered as equivalent to.  The
poll_queue_proc can then skip adding entirely if that fixed event is not
included in the set to be caught by this poll().

We also add a new poll_table_entry.fixed_key.  The poll_queue_proc can
record the fixed key it is passed in here, and reuse it at wakeup time to
track that a nonzero fixed key was passed in to poll_wait_fixed() and that
the key should be ignored in preference to fixed_key.

With this in place, you can say, e.g. (as waitfd does)

        poll_wait_fixed(file, &current->signal->wait_chldexit, wait,
                POLLIN);

and the key passed to wakeups on the wait_chldexit waitqueue will be
ignored: the fd will always be treated as having raised POLLIN, waking
up poll()s and epoll()s that have specified that event.  (Obviously, a
poll function that calls this should return the same value from the poll
function as was passed to poll_wait_fixed(), or, as usual, zero if this
was a spurious wakeup.)

I do not like this scheme: it's sufficiently arcane that I had to go
back to my old commit messages to figure out what it was doing and
why.  But I don't see another way to cause poll() to return on
appropriate activity on waitqueues that do not actually correspond to
files.  (I do wonder how signalfd works.  It doesn't seem to need any of
this and I don't understand why not.  I would be overjoyed to remove the
whole invasive poll_wait_fixed() mess, but I'm not sure what to replace
it with.)

Orabug: 29891866
Signed-off-by: Nick Alcock <nick.alcock@oracle.com>
Signed-off-by: Kris Van Hees <kris.van.hees@oracle.com>
Signed-off-by: Tomas Jedlicka <tomas.jedlicka@oracle.com>
Signed-off-by: Eugene Loh <eugene.loh@oracle.com>
Signed-off-by: David Mc Lean <david.mclean@oracle.com>
Signed-off-by: Vincent Lim <vincent.lim@oracle.com>
Reviewed-by: Nick Alcock <nick.alcock@oracle.com>

---
## [omarisahmed/aws-cdk](https://github.com/omarisahmed/aws-cdk)@[c071367def...](https://github.com/omarisahmed/aws-cdk/commit/c071367def4382c630057546c74fa56f00d9294c)
#### Thursday 2022-02-03 14:37:55 by Kaizen Conroy

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
## [measurement-factory/squid](https://github.com/measurement-factory/squid)@[2b6b1bcb86...](https://github.com/measurement-factory/squid/commit/2b6b1bcb8650095c99a1916f5964305484af7ef0)
#### Thursday 2022-02-03 14:52:59 by Alex Rousskov

Bug 5055: FATAL FwdState::noteDestinationsEnd exception: opening (#877)

The bug was caused by commit 25b0ce4. Other known symptoms are:

    assertion failed: store.cc:1793: "isEmpty()"
    assertion failed: FwdState.cc:501: "serverConnection() == conn"
    assertion failed: FwdState.cc:1037: "!opening()"

This change has several overlapping parts. Unfortunately, merging
individual parts is both difficult and likely to cause crashes.

## Part 1: Bug 5055.

FwdState used to check serverConn to decide whether to open a connection
to forward the request. Since commit 25b0ce4, a nil serverConn pointer
no longer implies that a new connection should be opened: FwdState
helper jobs may already be working on preparing an existing open
connection (e.g., sending a CONNECT request or negotiating encryption).

Bad serverConn checks in both FwdState::noteDestination() and
FwdState::noteDestinationsEnd() methods led to extra connectStart()
calls creating two conflicting concurrent helper jobs.

To fix this, we replaced direct serverConn inspection with a
usingDestination() call which also checks whether we are waiting for a
helper job. Testing that fix exposed another set of bugs: The helper job
pointers or in-job connections were left stale/set after forwarding
failures. The changes described below addressed most of those problems.


## Part 2: Connection establishing helper jobs and their callbacks

A proper fix for Bug 5055 required answering a difficult question: When
should a dying job call its callbacks? We only found one answer which
required cooperation from the job creator and led to the following
rules:

* AsyncJob destructors must not call any callbacks.

* AsyncJob::swanSong() is responsible for async-calling any remaining
  (i.e. set, uncalled, and uncancelled) callbacks.

* AsyncJob::swanSong() is called (only) for started jobs.

* AsyncJob destructing sequence should validate that no callbacks remain
  uncalled for started jobs.

... where an AsyncJob x is considered "started" if AsyncJob::Start(x)
has returned without throwing.

A new JobWait class helps job creators follow these rules while keeping
track on in-progress helper jobs and killing no-longer-needed helpers.

Also fixed very similar bugs in tunnel.cc code.


## Part 3: ConnOpener fixes

1. Many ConnOpener users are written to keep a ConnectionPointer to the
   destination given to ConnOpener. This means that their connection
   magically opens when ConnOpener successfully connects, before
   ConnOpener has a chance to notify the user about the changes. Having
   multiple concurrent connection owners is always dangerous, and the
   user cannot even have a close handler registered for its now-open
   connection. When something happens to ConnOpener or its answer, the
   user job may be in trouble. Now, ConnOpener callers no longer pass
   Connection objects they own, cloning them as needed. That adjustment
   required adjustment 2:

2. Refactored ConnOpener users to stop assuming that the answer contains
   a pointer to their connection object. After adjustment 1 above, it
   does not. HappyConnOpener relied on that assumption quite a bit so we
   had to refactor to use two custom callback methods instead of one
   with a complicated if-statement distinguishing prime from spare
   attempts. This refactoring is an overall improvement because it
   simplifies the code. Other ConnOpener users just needed to remove a
   few no longer valid paranoid assertions/Musts.

3. ConnOpener users were forced to remember to close params.conn when
   processing negative answers. Some, naturally, forgot, triggering
   warnings about orphaned connections (e.g., Ident and TcpLogger).
   ConnOpener now closes its open connection before sending a negative
   answer.

4. ConnOpener would trigger orphan connection warnings if the job ended
   after opening the connection but without supplying the connection to
   the requestor (e.g., because the requestor has gone away). Now,
   ConnOpener explicitly closes its open connection if it has not been
   sent to the requestor.

Also fixed Comm::ConnOpener::cleanFd() debugging that was incorrectly
saying that the method closes the temporary descriptor.

Also fixed ConnOpener callback's syncWithComm(): The stale
CommConnectCbParams override was testing unused (i.e. always negative)
CommConnectCbParams::fd and was trying to cancel the callback that most
(possibly all) recipients rely on: ConnOpener users expect a negative
answer rather than no answer at all.

Also, after comparing the needs of two old/existing and a temporary
added ("clone everything") Connection cloning method callers, we decided
there is no need to maintain three different methods. All existing
callers should be fine with a single method because none of them suffers
from "extra" copying of members that others need. Right now, the new
cloneProfile() method copies everything except FD and a few
special-purpose members (with documented reasons for not copying).

Also added Comm::Connection::cloneDestinationDetails() debugging to
simplify tracking dependencies between half-baked Connection objects
carrying destination/flags/other metadata and open Connection objects
created by ConnOpener using that metadata (which are later delivered to
ConnOpener users and, in some cases, replace those half-baked
connections mentioned earlier. Long-term, we need to find a better way
to express these and other Connection states/stages than comments and
debugging messages.


## Part 4: Comm::Connection closure callbacks

We improved many closure callbacks to make sure (to the extent possible)
that Connection and other objects are in sync with Comm. There are lots
of small bugs, inconsistencies, and other problems in Connection closure
handlers. It is not clear whether any of those problems could result in
serious runtime errors or leaks. In theory, the rest of the code could
neutralize their negative side effects. However, even in that case, it
would only be a matter of time before the next bug bites us due to stale
Connection::fd and such. These changes themselves carry elevated risk,
but they get us closer to reliable code as far as Connection maintenance
is concerned. Without them, we will keep chasing deadly side effects of
poorly implemented closure callbacks.

Long-term, all these manual efforts to keep things in sync should become
unnecessary with the introduction of appropriate Connection ownership
APIs that automatically maintain the corresponding environments (TODO).


## Part 5: Other notable improvements in the adjusted code

Improved Security::PeerConnector::serverConn and
Http::Tunneler::connection management, especially when sending negative
answers. When sending a negative answer, we would set answer().conn to
an open connection, async-send that answer, and then hurry to close the
connection using our pointer to the shared Connection object. If
everything went according to the plan, the recipient would get a non-nil
but closed Connection object. Now, a negative answer simply means no
connection at all. Same for a tunneled answer.

Refactored ICAP connection-establishing code to to delay Connection
ownership until the ICAP connection is fully ready. This change
addresses primary Connection ownership concerns (as they apply to this
ICAP code) except orphaning of the temporary Connection object by helper
job start exceptions (now an explicit XXX). For example, the transaction
no longer shares a Connection object with ConnOpener and
IcapPeerConnector jobs.

Probably fixed a bug where PeerConnector::negotiate() assumed that
sslFinalized() does not return true after callBack(). It may (e.g., when
CertValidationHelper::Submit() throws). Same for
PeekingPeerConnector::checkForPeekAndSpliceMatched().
 
Fixed FwdState::advanceDestination() bug that did not save
ERR_GATEWAY_FAILURE details and "lost" the address of that failed
destination, making it unavailable to future retries (if any).

Polished PeerPoolMgr, Ident, and Gopher code to be able to fix similar
job callback and connection management issues.

Polished AsyncJob::Start() API. Start() used to return a job pointer,
but that was a bad idea:
    
* It implies that a failed Start() will return a nil pointer, and that
  the caller should check the result. Neither is true.

* It encourages callers to dereference the returned pointer to further
  adjust the job. That technically works (today) but violates the rules
  of communicating with an async job. The Start() method is the boundary
  after which the job is deemed asynchronous.
    
Also removed old "and wait for..." post-Start() comments because the
code itself became clear enough, and those comments were becoming
increasingly stale (because they duplicated the callback names above
them).

Fix Tunneler and PeerConnector handling of last-resort callback
requirements. Events like handleStopRequest() and callException() stop
the job but should not be reported as a BUG (e.g., it would be up to the
callException() to decide how to report the caught exception). There
might (or there will) be other, similar cases where the job is stopped
prematurely for some non-BUG reason beyond swanSong() knowledge. The
existence of non-bug cases does not mean there could be no bugs worth
reporting here, but until they can be identified more reliably than all
these benign/irrelevant cases, reporting no BUGs is a (much) lesser
evil.

TODO: Revise AsyncJob::doneAll(). Many of its overrides are written to
check for both positive (i.e. mission accomplished) and negative (i.e.
mission cancelled or cannot be accomplished) conditions, but the latter
is usually unnecessary, especially after we added handleStopRequest()
API to properly support external job cancellation events. Many doneAll()
overrides can probably be greatly simplified.

---
## [ghc/ghc](https://github.com/ghc/ghc)@[e8f7734d8a...](https://github.com/ghc/ghc/commit/e8f7734d8a052f99b03e1123466dc9f47b48c311)
#### Thursday 2022-02-03 15:25:32 by John Ericson

Fix #19931

The issue was the renderer for x86 addressing modes assumes native size
registers, but we were passing in a possibly-smaller index in
conjunction with a native-sized base pointer.

The easist thing to do is just extend the register first.

I also changed the other NGC backends implementing jump tables
accordingly. On one hand, I think PowerPC and Sparc don't have the small
sub-registers anyways so there is less to worry about. On the other
hand, to the extent that's true the zero extension can become a no-op.

I should give credit where it's due: @hsyl20 really did all the work for
me in
https://gitlab.haskell.org/ghc/ghc/-/merge_requests/4717#note_355874,
but I was daft and missed the "Oops" and so ended up spending a silly
amount of time putting it all back together myself.

The unregisterised backend change is a bit different, because here we
are translating the actual case not a jump table, and the fix is to
handle right-sized literals not addressing modes. But it makes sense to
include here too because it's the same change in the subsequent commit
that exposes both bugs.

---
## [west3436/vgstation13](https://github.com/west3436/vgstation13)@[622f3fac2b...](https://github.com/west3436/vgstation13/commit/622f3fac2b24476f23d8c9ebfae2dba5e371a3cc)
#### Thursday 2022-02-03 16:10:31 by ShiftyRail

The Thing Before Christmas (#31715)

I thought this was a good way to spice up the winter season.
While I know Ling was removed for a reason, I want you to consider that it got removed years ago. It is fair to say that the playerbase and the game changed so much since then than a "tabula rasa" might be justified.

Besides, ling had deathsting removed and its obnoxious chemical stings axxed too. (#23014)
From a QoL standpoint, the stings have been converted to spells and should be as easy to use as the vampire ones.

As a final note, it's painstaingly true that ling is the least worked over of all our antags and is in dire need of some love and new content. However, this content can only come if people experience ling first-hand and get motivated to fix it.

Worse come to worse, we remove it again lole

Merry Christmas everyone.

:cl:
- rscadd: Santa Claus is coming to town. More specifically, he's coming to Antartica. Wait, he was already here all this time? And why does he look so familiar... OH GOD HELP

---
## [ammarfaizi2/linux-block](https://github.com/ammarfaizi2/linux-block)@[c11585a757...](https://github.com/ammarfaizi2/linux-block/commit/c11585a7575456478cfdd88a66c02f5a61943536)
#### Thursday 2022-02-03 16:16:04 by Jason A. Donenfeld

random: use linear min-entropy accumulation crediting

Currently, credit_entropy_bits() uses Shannon entropy, which is not
quite correct; min-entropy should be used instead, which is the negative
log of the most probable event. This makes it rather hard to calculate,
since if we consider each call to credit_entropy_bits(h) a distinct
event, the most probable one of those will be the one where h=1, and
then we'll never grow. Alternatively we could establish a lower bound
on min-entropy in terms of the number of events, rather than the
particular probability of any one event, which comes out to the log of
the number of events plus one, which would mean that we'd need an
astronomically high amount of events get 128 bits of min-entropy, so
this isn't really useful. Suffice to say, in the standard model there's
simply no chain rule for min-entropy.

For these reasons, 30e37ec516ae ("random: account for entropy loss due
to overwrites") implemented credit_entropy_bits() to use Shannon
entropy, assuming the independence of all sources. But then, observing
that min-entropy must by definition be less than Shannon entropy, it
replaced a constant 2-2/√𝑒 term (~0.786938) with 3/4 (0.75), which not
only is less -- so an underestimate -- but also computes much more
easily with integer instructions. This wasn't superb, but it was perhaps
better than nothing, so that's what was done.

However, examining the context, we see that it was done because adding
bytes to the old LFSR was said to probabilistically cancel out some
amount of entropy from earlier. Which entropy and how much is hard to
tell, and as I showed with the attack code in my previous commit, a
motivated adversary can actually cancel out everything.

But, we're no longer using that LFSR. Rather, we're using a
computational hash function now as the accumulator and we've switched to
working in the random oracle model, from which we can now revisit the
question of min-entropy accumulation, which is done in detail in
<https://eprint.iacr.org/2019/198>.

Consider a long input bit string that is built by concatenating various
smaller independent input bit strings. Each one of these inputs has a
designated min-entropy, which is what we're passing to
credit_entropy_bits(h). When we pass the concatenation of these to a
random oracle, it means that an adversary trying to receive back the
same reply as us would need to become certain about each part of the
concatenated bit string we passed in, which means becoming certain about
all of those h values. That means we can estimate the accumulation by
simply adding up the h values in calls to credit_entropy_bits(h);
there's no probabilistic cancellation at play like there was said to be
for the LFSR. Incidentally, this is also what other entropy accumulators
based on computational hash functions do as well.

So this commit replaces credit_entropy_bits(h) with essentially `total =
min(POOL_BITS, total + h)`, done with a cmpxchg loop as before.

What if we're wrong and the above is nonsense? It's not, but let's
assume we don't want the actual _behavior_ of the code to change much.
Currently that behavior is not extracting from the input pool until it
has 128 bits of entropy in it. With the old algorithm, we'd hit that
magic 128 number after roughly 256 calls to credit_entropy_bits(1). So,
we can retain more or less the old behavior by waiting to extract from
the input pool until it hits 256 bits of entropy using the new code. For
people concerned about this change, it means that there's not that much
practical behavioral change. And for folks actually trying to model
the behavior rigorously, it means that we have an even higher margin
against attacks.

Cc: Theodore Ts'o <tytso@mit.edu>
Cc: Dominik Brodowski <linux@dominikbrodowski.net>
Cc: Greg Kroah-Hartman <gregkh@linuxfoundation.org>
Reviewed-by: Jean-Philippe Aumasson <jeanphilippe.aumasson@gmail.com>
Signed-off-by: Jason A. Donenfeld <Jason@zx2c4.com>

---
## [anupamroy777/kernel_realme_RM6785](https://github.com/anupamroy777/kernel_realme_RM6785)@[995ab41f50...](https://github.com/anupamroy777/kernel_realme_RM6785/commit/995ab41f505ca17997ff0534ac55a8f7c3c8f629)
#### Thursday 2022-02-03 16:20:27 by Wang Han

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

---
## [newstools/2022-this-day](https://github.com/newstools/2022-this-day)@[1d94b85654...](https://github.com/newstools/2022-this-day/commit/1d94b85654a6905b57c3213f48d86e5883ae01f7)
#### Thursday 2022-02-03 16:27:46 by Billy Einkamerer

Created Text For URL [www.thisdaylive.com/index.php/2022/02/03/benjamin-laniyi-my-utmost-concern-for-the-nigerian-girl-child-is-that-she-may-attain-and-live-the-life-of-her-dream/]

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[51709065ff...](https://github.com/mrakgr/The-Spiral-Language/commit/51709065fff52c68d1a60b71296987db36dcbc50)
#### Thursday 2022-02-03 17:17:16 by Marko Grdinić

"11am. I am up. Today I am going to get some serious studying done if possible. I am going to watch the panel video from yesterday again and see if my focus has improved.

11:10am. Let me start. It is time I figure out how to sample different cables. Also how did he manage to do those bolts around them while having them fit? I need to focus.

I think I am about 10 days into Covid, and it should be time to get over it soon.

https://vimeo.com/364080941
Houdini Sci Fi Panel Generator | Part 1 | Modeling the Panel

I've watched this yesterday, but I could not understand a thing of it. This time I'll do better.

Yesterday I just about figured out how the for loop works. What I have to do now is seal the deal.

1:24 in. It is annoying that I do not have this particular node, nor do I know how to install them, but it does not matter. I'll leave figuring that out for later. Right now it feels like my focus is at a decent level. I am still not over it, but my head does not feel dizzy from the illness.

11:20am. I saw this yesterday, but did not have the energy to wonder about it properly so let me do that now. Just why is he duplicating the layer names?

Is he extracting the same layer except with a different brightness threeshold?

11:30am. This whole tutorial is so weird, I have no idea why it is structured the way it is.

11:40am. 15:17. I am getting good feedback from my subconscious. With the way things are, I can expect to get some real learning done today. That is the most important. Houdini might be big, but as long as I keep cracking at it, it will fall much like Blender.

11:55am. I am getting it. I thought about how I would have done it myself, and came to a conclussion that I could just use match size to push things around. But this way of doing things is not bad.

I am playing with fuse, and turning off the snap distance does exactly what I'd want without having to put in a large value. It merges all the points into a single value.

1:05pm. I've gone through the tutorial start to finish while paying careful attention to it.

This is it! I am back in action. This was an ideal study session. I've been paying attention and going through the steps myself. I've succeeded at learning a decent amount.

1:10pm. This is good enough. Let me have breakfast and do the chores. After that is done, I am going to start work on my own projects. It is finally time to get started on doing the pool scene in Houdini. All this automation capability is one thing, but I'll know how good it is once I try it with my own hands.

It is not a given that I have to use Houdini. Maybe I'll end up doing it all in Blender in the end.

1:50pm. Let me do the chores.

2:40pm. Done with that. By no means have I recovered. Maybe another week and this illness will blow over.

Before I start, let me take a look at how he did the preset.

Ah, I see.

2:50pm. It is time to get started. I opened the flower file for the first time in a while. Last time I did the bulb, and then I had trouble understanding how to do the stalk. But now that should not be a problem.

Let me get a refil and then I'll take stock of my condition.

2:55pm. Let me do a little review. Though I had a successful morning session, I am still not over the illness, so I won't force myself to work here.

Instead, let me plan things out.

I've been studying Houdini for 2.5 weeks now, so I know it well enough to form an opinion of it.

My view is that it is overrated. If it is merely distributing the flowers I could have used the scatter addon for Blender. the same might apply for buildings and things like that.

Despite all its sophistication, for doing things like sampling, Houdini strikes me as barely being better than Blender and I hate how I have to dip in a circular way using channels to make use of the switch node.

3:05pm. Yeah, Houdini is overrated. I think that in many places I'll try to automate things, and end up being slower than had I tried doing it by hand.

3:10pm. After doing the chores, the physical exhaustion is really hitting me.

Let me go back to the middle of last month. Back then, I had the option of going either with Blender or shoring up my knowledge even further and I choose the later.

Back then I had a really strong feeling of having grasped the basics. I feel that if I wanted to become an illustrator, back then I really could have done it.

I need to go back to that.

Basic modeling, basic sculpting, and then laying things out. Forget the advanced Houdini stuff. I am not going to be changing things that much.

3:30pm. Got the stalk done.

4:15pm. FFFFFFFFFFFFFFFFF...holy shit this is so annoying!

How do I do the correct orientation for the scattered points?

4:20pm. I am completely confused here.

4:30pm. I hate this. Why is the angle off for some leaves? When I try to do a cone, I get the right result.

https://www.youtube.com/results?search_query=houdini+scatter

Let me watch some of these.

I have no idea. I simply forgot how it works. This would not be a problem in Blender.

https://youtu.be/tCijuuNIRrs
New in Houdini 18.5 Pt. 5: Scatter & Align Plus Attribute From Pieces SOPs - The New Workflow

Let me watch this.

4:40pm. https://youtu.be/tCijuuNIRrs?t=110

This is a new thing.

5pm. I am not in my right mind. I am quite pissed off at Houdini right now.

Just what is the problem with the leaves? Do they have a random orientation or something?

5:15pm. https://youtu.be/N7CDHwgWKVo?t=406

Ah, here is the density for this. At any rate, I am going to have to make a simplified example to make sure that the orientation is right.

https://youtu.be/N7CDHwgWKVo?t=476

Let me stop here for the day.

5:20pm. I am not my usual self. Right now, I feel like smashing my fist through the monitor. I probably shouldn't be this pissed off over so little.

I still haven't gotten my senses of smell and taste back. I guess it too early to be making plans for getting back into the swing of things. Trying to pretend I am well is just pretense. Hard work is only something that happens when one is in proper health.

5:25pm. I am starting to form my view of things. Houdini might beat Blender in terms of workflow, but as a PL it has everything I most dislike about mainstream PLs. As a program it evolved solely by cramming shit into itself without a care for elegance. I thought that Blender's geometry nodes were complicated at first, but they are incredibly well designed compared to Houdini's bloat.

Houdini is the opposite of slim, it is an incredibly bloated piece of software.

5:30pm. I am so pissed off about this orientation thing. Houdini has normals, but then it has `up`, `orient`, `xform` and who knows what fucking else.

I am faced with this complexity, but I feel so dull and uninspired.

I got the stalk done. I certainly did that for the day. But I need to go further.

I need to figure out why the leaves have random rotation in places.

5:40pm. You know what I hate about Houdini? How unlike in Blender it does not rotate around an object, but hangs around freeform.

5:45pm. I am copying to points on a sphere, and I see that for the leaves to have proper orientation, I need to set `@up = {0,1,0};`. That gives it proper orientation.

This is what I've been suspecting is the problem. The points probably have the normals in the right place, but that still leaves a 360 degree of freedom with regards to what the other axis should be. In Blender this wasn't a problem for some reason.

Still, I find it strange that I have to set this manually using the attribute wrangle.

6:10pm. No, setting the up does not do jack when combined with the scatter and align node.

I am just bashing my head against the wall here.

Enough.

6:15pm. Sometimes just stopping when things aren't going your way is a sign of discipline. Maybe my mental acuity will be better tomorrow.

I am going to focus on just figuring out the issue of determining orientation for the scattered nodes. Let me have lunch here."

---
## [Dinesh8487/Ecommerce-Sales-Prediction](https://github.com/Dinesh8487/Ecommerce-Sales-Prediction)@[41e5ca29b4...](https://github.com/Dinesh8487/Ecommerce-Sales-Prediction/commit/41e5ca29b433b914138054ad8347fc13e5d9cf14)
#### Thursday 2022-02-03 17:39:10 by Dinesh Balasubramanian

Update README.md

Project Introduction
Black Friday is an informal name for the Friday following Thanksgiving Day in the United States, which is celebrated on the fourth Thursday of November. The day after Thanksgiving has been regarded as the beginning of the United States Christmas shopping season since 1952, although the term "Black Friday" did not become widely used until more recent decades. Many stores offer highly promoted sales on Black Friday and open very early, such as at midnight, or may even start their sales at some time on Thanksgiving. The major challenge for a Retail store or eCommerce business is to choose product price such that they get maximum profit at the end of the sales. Our project deals with determining the product prices based on the historical retail store sales data. After generating the predictions, our model will help the retail store to decide the price of the products to earn more profits.

Dataset Description
The dataset is acquired from an online data analytics hackathon hosted by Analytics Vidhya. The data contained features like age, gender, marital status, categories of products purchased, city demographics, purchase amount etc. The data consists of 12 columns and 537577 records. Our model will be predicting the purchase amount of the products.

EDA:
Below are the observations which we have made from the data visualization done as part of the Data Understanding process.

Approximately, 75% of the number of purchases are made by Male users and rest of the 25% is done by female users. This tells us the Male consumers are the major contributors to the number of sales for the retail store.On average the male gender spends more money on purchase contrary to female, and it is possible to also observe this trend by adding the total value of purchase.
When we combined Purchase and Marital_Status for analysis, we came to know that Single Men spend the most during the Black Friday. It also tells that Men tend to spend less once they are married. It maybe because of the added responsibilities.
For Age feature, we observed the consumers who belong to the age group 25-40 tend to spend the most.
There is an interesting column Stay_In_Current_City_Years, after analyzing this column we came to know the people who have spent 1 year in the city tend to spend the most. This is understandable as, people who have spent more than 4 years in the city are generally well settled and are less interested in buying new things as compared to the people new to the city, who tend to buy more.
When examining which city the product was purchased to our surprise, even though the city B is majorly responsible for the overall sales income, but when it comes to the above product, it majorly purchased in the city C.
Data Preparation
Used LabelEncoder for encoding the categorical columns like Age, Gender and City_Category
Used get_dummies form Pandas package for converting categorical variable State_In_Current_Years into dummy/indicator variables.
Filled the missing values in the Product_Category_2 and Product_Category_3
Modeling Phase
Splitted dataset into into random train and test subset of ratio 80:20
Implemented multiple supervised models such as Linear Regressor, Decision Tree Regressor, Random Forest Regressor.
Evaluation Metric
Root Mean Square Error (RMSE) is a standard way to measure the error of a model in predicting quantitative data. It’s the square root of the average of squared differences between prediction and actual observation.

Conclusion
Implanted multiple supervised models such as Linear Regressor,Decision Tree Regressor, Random Forest Regressor and XGBOOST Regressor. Out of these supervised models, based on the RMSE scores XGBRegressor/XGBOOST Regressor was the best performer with a score of 2879.

---
## [Dinesh8487/Ecommerce-Sales-Prediction](https://github.com/Dinesh8487/Ecommerce-Sales-Prediction)@[775938ac47...](https://github.com/Dinesh8487/Ecommerce-Sales-Prediction/commit/775938ac47de6af222611083dee52156a383a99e)
#### Thursday 2022-02-03 17:42:37 by Dinesh Balasubramanian

README.md

Project Introduction
Black Friday is an informal name for the Friday following Thanksgiving Day in the United States, which is celebrated on the fourth Thursday of November. The day after Thanksgiving has been regarded as the beginning of the United States Christmas shopping season since 1952, although the term "Black Friday" did not become widely used until more recent decades. Many stores offer highly promoted sales on Black Friday and open very early, such as at midnight, or may even start their sales at some time on Thanksgiving. The major challenge for a Retail store or eCommerce business is to choose product price such that they get maximum profit at the end of the sales. Our project deals with determining the product prices based on the historical retail store sales data. After generating the predictions, our model will help the retail store to decide the price of the products to earn more profits.

EDA:
Below are the observations which we have made from the data visualization done as part of the Data Understanding process.

Approximately, 75% of the number of purchases are made by Male users and rest of the 25% is done by female users. This tells us the Male consumers are the major contributors to the number of sales for the retail store.On average the male gender spends more money on purchase contrary to female, and it is possible to also observe this trend by adding the total value of purchase.
When we combined Purchase and Marital_Status for analysis, we came to know that Single Men spend the most during the Black Friday. It also tells that Men tend to spend less once they are married. It maybe because of the added responsibilities.
For Age feature, we observed the consumers who belong to the age group 25-40 tend to spend the most.
There is an interesting column Stay_In_Current_City_Years, after analyzing this column we came to know the people who have spent 1 year in the city tend to spend the most. This is understandable as, people who have spent more than 4 years in the city are generally well settled and are less interested in buying new things as compared to the people new to the city, who tend to buy more.
When examining which city the product was purchased to our surprise, even though the city B is majorly responsible for the overall sales income, but when it comes to the above product, it majorly purchased in the city C.
Data Preparation
Used LabelEncoder for encoding the categorical columns like Age, Gender and City_Category
Used get_dummies form Pandas package for converting categorical variable State_In_Current_Years into dummy/indicator variables.
Filled the missing values in the Product_Category_2 and Product_Category_3
Modeling Phase
Splitted dataset into into random train and test subset of ratio 80:20
Implemented multiple supervised models such as Linear Regressor, Decision Tree Regressor, Random Forest Regressor.
Evaluation Metric
Root Mean Square Error (RMSE) is a standard way to measure the error of a model in predicting quantitative data. It’s the square root of the average of squared differences between prediction and actual observation.

Conclusion
Implanted multiple supervised models such as Linear Regressor,Decision Tree Regressor, Random Forest Regressor and XGBOOST Regressor. Out of these supervised models, based on the RMSE scores XGBRegressor/XGBOOST Regressor was the best performer with a score of 2879.

---
## [primitt/nhd](https://github.com/primitt/nhd)@[12b9000698...](https://github.com/primitt/nhd/commit/12b900069867f51765fb597608142721a00b3987)
#### Thursday 2022-02-03 17:52:29 by primboi

Bro, idris is a fucking bitch ass idiotic fucker who is bound to become a hooker and a prositute

---
## [ammarfaizi2/linux-block](https://github.com/ammarfaizi2/linux-block)@[3a3f53b816...](https://github.com/ammarfaizi2/linux-block/commit/3a3f53b81631f6a0225ef72fe4458988dc7fe3a2)
#### Thursday 2022-02-03 18:01:17 by Jason A. Donenfeld

random: use linear min-entropy accumulation crediting

30e37ec516ae ("random: account for entropy loss due to overwrites")
assumes that adding new entropy to the LFSR pool probabilistically
cancelled out old entropy there, so entropy was credited asymptotically,
approximating Shannon entropy of independent sources (rather than a
stronger min-entropy notion) using 1/8th fractional bits, and replacing
a constant 2-2/√𝑒 term (~0.786938) with 3/4 (0.75) to slightly
underestimate it. This wasn't superb, but it was perhaps better than
nothing, so that's what was done. Which entropy specifically was being
cancelled out and how much precisely each time is hard to tell, though
as I showed with the attack code in my previous commit, a motivated
adversary with sufficient information can actually cancel out
everything.

This is neither here nor there, now that we're no longer using that LFSR
for entropy accumulation. Rather, we're now using a computational hash
function as the accumulator and we've switched to working in the random
oracle model, from which we can now revisit the question of min-entropy
accumulation, which is done in detail in <https://eprint.iacr.org/2019/198>.

Consider a long input bit string that is built by concatenating various
smaller independent input bit strings. Each one of these inputs has a
designated min-entropy, which is what we're passing to
credit_entropy_bits(h). When we pass the concatenation of these to a
random oracle, it means that an adversary trying to receive back the
same reply as us would need to become certain about each part of the
concatenated bit string we passed in, which means becoming certain about
all of those h values. That means we can estimate the accumulation by
simply adding up the h values in calls to credit_entropy_bits(h);
there's no probabilistic cancellation at play like there was said to be
for the LFSR. Incidentally, this is also what other entropy accumulators
based on computational hash functions do as well.

So this commit replaces credit_entropy_bits(h) with essentially `total =
min(POOL_BITS, total + h)`, done with a cmpxchg loop as before.

What if we're wrong and the above is nonsense? It's not, but let's
assume we don't want the actual _behavior_ of the code to change much.
Currently that behavior is not extracting from the input pool until it
has 128 bits of entropy in it. With the old algorithm, we'd hit that
magic 128 number after roughly 256 calls to credit_entropy_bits(1). So,
we can retain more or less the old behavior by waiting to extract from
the input pool until it hits 256 bits of entropy using the new code. For
people concerned about this change, it means that there's not that much
practical behavioral change. And for folks actually trying to model
the behavior rigorously, it means that we have an even higher margin
against attacks.

Cc: Theodore Ts'o <tytso@mit.edu>
Cc: Dominik Brodowski <linux@dominikbrodowski.net>
Cc: Greg Kroah-Hartman <gregkh@linuxfoundation.org>
Reviewed-by: Jean-Philippe Aumasson <jeanphilippe.aumasson@gmail.com>
Signed-off-by: Jason A. Donenfeld <Jason@zx2c4.com>

---
## [houshmand-2005/django4](https://github.com/houshmand-2005/django4)@[a138c6975d...](https://github.com/houshmand-2005/django4/commit/a138c6975ded4b383ce9372323d88352fdc52188)
#### Thursday 2022-02-03 19:10:37 by houshmand

add my gmail addres and i do a mistake i didnt delete my password lol :) i changed my password but its to funny :) i changed my data base config so i have migrate and i add reset password url and I made the site more optimized now my site is ready but not veery goood but it work good to me hooo finaily sorry for my bad English lol I have very bad spelling and grammar because I did most of this project for myself and unfortunately I am not yet fluent in English.Bye!!

---
## [stevOOOOOOOOOO0/Cavalry](https://github.com/stevOOOOOOOOOO0/Cavalry)@[94e5838b55...](https://github.com/stevOOOOOOOOOO0/Cavalry/commit/94e5838b5560acb625f32863897c9b2a5685281d)
#### Thursday 2022-02-03 19:11:08 by Brandon

life continues to be pain and I have to fix epic's shit

---
## [Gunn-GAtM/gatm](https://github.com/Gunn-GAtM/gatm)@[987efd997c...](https://github.com/Gunn-GAtM/gatm/commit/987efd997c9aa397daae2305046a2754727a91a9)
#### Thursday 2022-02-03 21:02:29 by Timothy Herchen

[documentation] Improve asymptote, build system

I am using a more verbose git commit message to please Yu-Ting. Hopefully this message and description better elucidates the intent and quality of my actions.

I updated the documentation on the build system to reflect current changes. In particular, the --dont-open flag was replaced by the --open flag, requiring opting in. Haha, "opt". What other funny three-letter words are there? Just considering three letter *animals*, there are already a lot: the ant, the dog, the cat, the bee, the cow; the YAK, the ELK, the EMU, the GNU. And yet, there is only one two-letter animal: the OX. Oh, the veritable ox. We just left the Chinese Year of the Ox (牛), although I don't know why that character—which, as far as I know, is generic for "cow"—specifically refers to oxen. What I do know is that us North Americans are superior English speakers compared to the rest of the world, because BrE, AuE, etc. speakers do not say "ox"; they say "steer" or "bullock". What joyless lives they must lead, devoid of two-letter animals!

Editing GAtM as an adult makes me feel like a gruff Tibetan yak... or, upon further consideration... like an ox. I feel hard-working, persistent—hooked up to the yoke with my ox brethren (Yu-Ting, mainly), plowing the Herreshoff-ian soil so that it may be fertile ground for student learning. Ox gang unite ✌️.

Anyway, back to my changes. I also added a link to an excellent document that describes most of the Asymptote language. I reference it to this day and it is unparalleled in ease of reading.

---
## [alanruttenberg/lsw2](https://github.com/alanruttenberg/lsw2)@[0332f218fe...](https://github.com/alanruttenberg/lsw2/commit/0332f218febeb0b7348e6181c5602efc3fdc2899)
#### Thursday 2022-02-03 21:10:33 by Alan Ruttenberg

This is an amazing one. make-uri can take a string without prefix in which case it makes makes a uri that is just that string - not protocol, etc. Using that uri with the OWLAPI causes crazy instability. It seems to break the reasoner, after having done this once, FOR THE REST OF THE SESSION, with shit like giving it a simple ontology (subclass-of !a !b), asking for the children of !b and SOMETIMES getting !a and sometimes NOT and even if that works, getting the parent of !a fails. So: If make-uri gets a string like this, it will put it in the default namespace now. Sheesh. This lost me hours and hours trying to track this down because I was doing a new type of calculation and thought there were bugs in my code!

---
## [crysopraise/hermeticyst](https://github.com/crysopraise/hermeticyst)@[2ac7ba7334...](https://github.com/crysopraise/hermeticyst/commit/2ac7ba7334e8d4293ab4af4e7218ba38cbdd2fab)
#### Thursday 2022-02-03 21:23:46 by crysopraise

Added beam attack

- Added a beam attack that you can spend your extra life to shoot, also
  recovers 50% blood
- Added in shoot animation and tweaked it so it plays partway, finishes
  when firing, and reverses when unaiming without firing
- Tweaked the beam attack so that it lines up directly with the center
  of you screen, added a temp aiming reticle
- There is a bug that fucks up you beam when the camera clips outside
  the level

---
## [theNicelander/ck3_blood_mage](https://github.com/theNicelander/ck3_blood_mage)@[a7b2d7c53f...](https://github.com/theNicelander/ck3_blood_mage/commit/a7b2d7c53fb05a8cc783d349782c3d31fb7d3e92)
#### Thursday 2022-02-03 21:27:36 by Petur

asking for blood magic only available if friends, best friends, lovers or soulmates

---
## [Bambinexx/otgn-bot](https://github.com/Bambinexx/otgn-bot)@[f631b7c14c...](https://github.com/Bambinexx/otgn-bot/commit/f631b7c14c49f6ff18601957ebd92b8734ce5ca3)
#### Thursday 2022-02-03 21:34:36 by Bambinexx

yes

Oh yeah, yeah ブレるな hey boys あふれ出す 想い 己つらぬけよ
       スペシャルをプレゼント 行こうぜ go! ありのままで
       Break out! 嵐起こせ おもてなす お前連れてく heaven へ
       Wake up! 弱き者よ はみ出せ hey! 空気なんて読むなよ
       檻破れ お前のスタイル押し通せ ah, virtuous knight
       共に行こう

---
## [DerErizzle/The-Jackbox-Party-Pack-8-German](https://github.com/DerErizzle/The-Jackbox-Party-Pack-8-German)@[7fce2d7d82...](https://github.com/DerErizzle/The-Jackbox-Party-Pack-8-German/commit/7fce2d7d82836dfb21de0df786eae0c2c75ce984)
#### Thursday 2022-02-03 22:30:18 by Maxi

9 Fragen (Holy Shit)

1. Welche Geräusche wurden auf der Voyager Golden Record in den Weltraum geschickt? Wow, ich habe das mal so nebenbei gehört, aber dieses goldene Schallplatte in der Voyager ist echt interessant (ID 77643).
2. Welche Berufe hat Barbie offiziell schon ausgeübt? Ich habe keine Ahnung von Barbie, daher habe ich mich da mal sehr ans original gehalten (ID 77638).
3. Was frisst die kleine Raupe Nimmersatt alles? Ich wusste gar nicht, dass es diese Geschichte auch auf Englisch gibt. Wieder was neues gelernt (ID 77356).
4. Welches sind die 7 neuen Weltwunder? Ich habe noch ein paar bekannte Sehenswürdigkeiten hinzugefügt, finde ich bei der Frage gut, wird sie etwas schwieriger (ID 77335).
5. Welche dieser Dinge sind Horkruxe von Voldemort in Harry Potter? Ich glaube, Harry Potter kennt man auch in Deutschland gut genug (ID 77299).
6. Wobei handelt es sich um traditionelle Werkzeuge für die Vampir-Bekämpfung? Ich wusste gar nicht, dass es reicht, die Vampire einfach nicht in das eigene Haus einzuladen. Aber nach einer kurzen Google-Suche, informativen Fan-Wikis und dem plötzlichen Verlust in sämtliches Vertrauen in die Menschheit  auf "Gute-Frage.net" bin ich jetzt schlauer (ID 77279).
7. Welche dieser Dinge können in deinem Kanu kaputt gehen? Das war gar nicht so leicht, die richtigen Übersetzungen für die Begriffe zu finden (ID 76957).
8. Welche dieser Puppen sind oder waren Teil der deutschen Sesamstraße?
(ID 76928).
9. Welches sind Teile eines Fahrrads? Oh Junge, super, dass ich so viel Ahnung von Fahrrädern habe. Irgendwie habe ich das hingekriegt, ich hoffe das passt (ID 76928).

---
## [skyline75489/terminal](https://github.com/skyline75489/terminal)@[b1ace967a2...](https://github.com/skyline75489/terminal/commit/b1ace967a2f2bf17fdcb7dd4f1426b014378b83c)
#### Thursday 2022-02-03 22:34:03 by Mike Griese

Two belling fixes (#12281)

Sorry for combining two fixes in one PR. I can separate if need be.

* [x] Closes #12276:
  - `"bellSound": null` didn't work. This one was easier, and is atomically in bcc2ca04fc14f39f37849b4bd837ad6cdb4cdaaa. Basically, we would deserialize that as an array with a single empty string in it, which we'd try to then play. I think it's more idomatic to have that deserialized as an empty array, which correctly falls back to playing the default sound.
* [x] Closes #12258: 
  - This one is the majority of the rest of the PR. If you leave the MediaPlayer open, then the media keys will _affect the Terminal_. More importantly, once the bell sounds, they'd replay the bell, which is insane. So the fix is to re-create the media player when we need it. We do this per-pane for simpler lifetime tracking. I'm not worried about the overhead of creating a mediaplayer here, since we're already throttling bells.
* Originally added in #11511
* [x] Tested manually
  - Use [`no.mp4`](https://www.youtube.com/watch?v=x2w9TyCv2gk) for this since that's like, 17s long
  - Checked that closing panes / the terminal while a bell was playing didn't crash
  - Playing a bunch of bells at once works
  - closing a pane stops the bell it's playing
  - once the bell stops, the media keys went back to working for Spotify
* [x] I work here

---
## [IDeletedSystem64/anitrox](https://github.com/IDeletedSystem64/anitrox)@[4f2e5af93b...](https://github.com/IDeletedSystem64/anitrox/commit/4f2e5af93b95138712a54a32cf7392331ae9642e)
#### Thursday 2022-02-03 23:27:00 by Anthony M

Update to SRC1

**Anitrox has been updated.**
**Old Version: PTB 4.1, Build 465**
**New Version: Stable Release Canidate 1, Build 500**
**This Major Anitrox Release Brings New Features and Bug Fixes to Anitrox!**
**What's New?**
- Cheese your friends with np!cheese
- Change your nickname with np!setnick (kinda buggy atm, will be fixed in SRC1.1)
- np!shutdown has been changed to stop and now makes a osu! reference
- Updated invite to have some sweet sweet sexy embeds (wait did I just say sexy embeds whaT)
- Changed info to show the CPU model, this is more of my curiosity of what CPU the host has lol
- New Icons! No more of those old ones from the Nyabot days. now we have proper Anitrox/Borkeon themed emotes! Want more Anitrox/Borkeon emotes like :BorkeonGlee: :Borkeon404: and :BorkeonBSOD:? Join Anitrox Central! run np!help for more information
**Bug Fixes**
- Fixed np!info not replying with bot info and information
**Known Issues**
np!setnick crashes bot when trying to run it on a higher role, this will be fixed in SRC1.1
Some commands might be using the legacy icons, I'm not 100% sure if I got all of them done
**This release was made possible with the support of @OfficialTCGMatt and @akuankka128. Thank you so much!**

---
## [compilerpraktikum/compiler](https://github.com/compilerpraktikum/compiler)@[22059964e0...](https://github.com/compilerpraktikum/compiler/commit/22059964e0ef1ee5eb4ef687120d204d57cf8850)
#### Thursday 2022-02-03 23:49:58 by Johannes Hengstler

calling conventions now only support return by register, because fuck you

---

