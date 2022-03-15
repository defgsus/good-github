## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-03-14](docs/good-messages/2022/2022-03-14.md)


1,836,847 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,836,847 were push events containing 2,826,246 commit messages that amount to 199,661,507 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 35 messages:


## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[759d24ab14...](https://github.com/tgstation/tgstation/commit/759d24ab14af0ab22ae9642e9190c3db91e16516)
#### Monday 2022-03-14 00:02:07 by san7890

Four Corners, Red Rover: An Exploration in Decal Trends [MDB IGNORE] (#65290)

* Four Corners, Red Rover: An Exploration in Decaled Trends

You there! What exactly is wrong with this photograph?!

You don't need to tell me, I've boxed it out. There's four individual corners for the decalling. This is weird. You may be asking: Why don't they use the "full tile" turf decals? Let me demonstrate.

Look at the difference between the one at left and the one in the middle. The turf decal totally smothers the nice contrast lines afforded to use by the base turf, causing it to have smooth, clammy exterior. This is probably why no mapper ever uses the full turf decal, much to the chagrin of people who stare at how big the size of this repo is.

Now, what's that on the right? Why, it's the new sprite (and pathing I made) to help counter-act this issue! This perfectly lines up with the contrast lines of the base turf, allowing us to have a non-flattened visualization, while not having four fucking turf decals a turf load upon initialization. How epic!

I've also added "contrasted" variants of the "half" and "anticorner" turf decals for future use. I probably won't go through and update this in this PR, but the opportunity remains available.

I may or not map this change across all the maps. We shall see.

* neutral corners

we love vsc

* no wait

i forgot a bunch of potential edgecases so we'll have to go back. yellow should be fine but neutral, dark, blue, and green should get a second look over

* recheck

found some stuff, probably missed out on others. let us commence forth

* MISTAKE

nearly a fucko bwoingo

* final pass

it compiles and i've had enough, someone else can probably figure it out from this point onwards

* #65230 goated my timbs

now we wait for linters to fail

* YOU DIDN'T SAY THAT THE FIRST TIME

LINTERS AAFAFAFF

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[884c1eeb62...](https://github.com/tgstation/tgstation/commit/884c1eeb62e1c970b2b6edc425f36c924b9f48ee)
#### Monday 2022-03-14 00:02:07 by 小月猫

fixes wallmounts (#65408)

closes #65393 (Engineering Cyborgs can't place APC or Air alarm frames on walls anymore)
fixes the code error in #64428 (afc1e44ee2922a316feb958249f7806568953bbe)

basically what occured is that he typed out the T(turf) attackby proc to input the screwdriver as an arg rather then the wallmount, remember, you want the WALLMOUNT to hit the wall to place it, not the screwdriver, that just creates runtimes and doesnt place anything

EDIT: actually re-reading it, what it was actually doing was using the screwdriver as the user arg, and trying to smash the user into the wall, thats actually kinda funny

borgo wallmounting is a good thing, good borgos need their treats

---
## [EthanRockss/tgstation](https://github.com/EthanRockss/tgstation)@[745426eff2...](https://github.com/EthanRockss/tgstation/commit/745426eff227ff556105147a4802540617decd7b)
#### Monday 2022-03-14 01:04:20 by LemonInTheDark

Adds a colorblind accessability testing tool (#65217)

* Adds a colorblind accessability testing tool

I keep finding myself worrying about if things I create will be parsable
for colorblind people. So I've made a debug tool for approximating
different extreme forms of colorblindness.

It's very very much a hack. We can't do the proper correction required
to actually deal directly with long medium and short wavelengths of
light, so we need to rely on approximations. Part of that means say,
bright things being brighter then they ought to be. S not how people
actually experience things, but it's not something we can do anything
about in byond.

Anyway uh, it works by taking color matrixes, and using the plane master
grouping system floyd added to apply them to most all parts of the game
you would want to color correct.

There's some slight fragility here, but I couldn't think of a better way
of handling it.

We also need to deal with planes that have BLEND_MULTIPLY as their
blendmode, since that fucks up the filter. I've come up with a hack for
it, since I wanted to avoid breaking anything.

Oh and since I want it to apply to huds too I added plane masters to
represent them. I think that's about it.

Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

---
## [brt9023/aws-cdk](https://github.com/brt9023/aws-cdk)@[c071367def...](https://github.com/brt9023/aws-cdk/commit/c071367def4382c630057546c74fa56f00d9294c)
#### Monday 2022-03-14 01:52:28 by Kaizen Conroy

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
## [Capstone-Projects-2022-Spring/project-vinylvision](https://github.com/Capstone-Projects-2022-Spring/project-vinylvision)@[3ab0be6931...](https://github.com/Capstone-Projects-2022-Spring/project-vinylvision/commit/3ab0be6931b48463bef1182c07153c515dc5655c)
#### Monday 2022-03-14 02:07:04 by Robert Morsa

added main html, css file, and some web config file so debugging is possible. it's very basic. layout looks like shit honestly, but I think this works. it runs using localhost
also i guess theres a .vs file now? im guessing thats just for it to work with visual studio. i have no idea if we're supposed to ignore that when committing but it added that in so whatever

---
## [DevilishSpirits/arcollect](https://github.com/DevilishSpirits/arcollect)@[7d53feadf9...](https://github.com/DevilishSpirits/arcollect/commit/7d53feadf98ea318ab355dc0380acfb36b272e19)
#### Monday 2022-03-14 02:47:07 by Devilish Spirits

Added support for KnowYourMeme

	I am a bit overloaded of work right now and destroying my sleep schedule with stupid even less useful things and AAAAAAHHHH!!!! I listened to too much MADs remixes... :sob:

	Also sorry JP if I'm sleepy this morning.

---
## [akisephila/sbepis](https://github.com/akisephila/sbepis)@[05fcd5fdf2...](https://github.com/akisephila/sbepis/commit/05fcd5fdf2825e0f8f14a2ce0e7017bef3add77b)
#### Monday 2022-03-14 02:56:53 by akisephila

Add Omega Death Shittenator Of Mountain Hell

Item I dreamt about. Multi-barrel cannon that fires boulders. 'Nuff said

---
## [mkingopng/feedback_prize_pytorch](https://github.com/mkingopng/feedback_prize_pytorch)@[a4bd49b377...](https://github.com/mkingopng/feedback_prize_pytorch/commit/a4bd49b377a87032794ef118247a9014b8476570)
#### Monday 2022-03-14 03:09:32 by Michael Kingston

I'll be damned. There is something to be said for trial and error. Or maybe its just sheer bloody minded persistence.

__feedback_prize_2021_ensembling.ipynb now executes without error on all 20 checkpoints from all 4 trained models.

Can't wait to give this a run on Kaggle. Interesting but it runs so much more slowly on Kaggle. Its taken 10 minutes to execute the last version which used 15 checkpoints from 3 models, and much longer to score. I want to see the score on that, then I'll update to use this code and score on 20 checkpoints.

Regardless of scores, all this is still "naive" so I expect that once we can add the bayesian optimisation to the ensemble the score will improve.

Whether this all comes together in time for end of competition is another thing entirely...

---
## [repinger/exynos9611_m21_kernel](https://github.com/repinger/exynos9611_m21_kernel)@[65a230db9e...](https://github.com/repinger/exynos9611_m21_kernel/commit/65a230db9e28562e9edb446295b095a0ea198f25)
#### Monday 2022-03-14 04:43:31 by Dave Chiluk

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

---
## [InfoTeddy/VVVVVV](https://github.com/InfoTeddy/VVVVVV)@[e93d8989d3...](https://github.com/InfoTeddy/VVVVVV/commit/e93d8989d3e82e5afc52e09fd7aeae3d41644e64)
#### Monday 2022-03-14 05:51:07 by Misa

Revert "Fix Secret Lab Time Trial trophies having wrong colors"

As reported by Dav999, Victoria and Vermilion's trophy colors are
swapped again in 2.4. He points to
37b7615b71c3a2f44e03c47894383107850812ff, the commit where I fixed the
color masks of every single surface to always be RGB or RGBA.

It sounded plausible to me, because it did have to do with colors, after
all. However, it didn't make sense to me, because I was like, I didn't
touch the trophy colors at all after I originally fixed them.

After I ruled out the RGBf() function as a confounder, I decided to see
whether intentionally reversing the color order in RGBf() to be BGR
would do anything, and to my surprise it actually swapped the colors
back around and it didn't actually look bad.

And then I realized: Swapping the trophy colors between RGB and BGR
ordering results in similar colors that still look good, but are simply
wrong, but not so wrong that they take on a color that no crewmate uses,
so it'd appear as if the crewmates were swapped, when in reality the
only thing that was swapped was actually the color order of the colors.

Trying to fix this by swapping the colors again, I actively confused
colors 33 and 35 (Vermilion and Victoria) with colors 32 and 34
(Vitellary and Viridian), so I was confused when Vermilion and Victoria
weren't swapping. Then as a debugging step, I only changed 34 to 32
without swapping 32 as well, and then finally noticed that I was
swapping Vitellary and Viridian, because there were now two Vitellarys.
And then I was reminded that Vitellary and Viridian were also wrongly
swapped since 2.0 as well.

And so then I finally realized: The original comments accompanying the
colors were correct after all. The only problem was that they were fed
into a function, RGBf(), that read the colors backwards, because the
codebase habitually changed the color order on a whim and it was really
hard to reason out which color order should be used at a given time, so
it ended up reading RGB colors as BGR, while it looked like it was
passing them through as-is.

So what happened was that in the first place, RGBf() was swapping RGB to
BGR. Then I came and swapped Vermilion and Victoria, and Vitellary and
Viridian around. Then later I fixed all the color masks, so RGBf()
stopped swapping RGB and BGR around. But then this ended up swapping the
colors of Vermilion and Victoria, and Vitellary and Viridian once again!

Therefore, swapping Vermilion and Victoria, and Vitellary and Viridian
was incorrect. Or at least, not the fix to the root cause. The root
cause would be to swap the colors in RGBf(), but this would be sort of
confusing to reason about - at least if I didn't bother to just type the
RGB values into an image editor. But that doesn't fix the real issue,
which is that the game kept swapping RGB and BGR around in every corner
of the codebase.

I further confirmed that there was no more RGB or BGR swapping by
deleting the plus-one-divide-by-three transformation in RGBf() and
seeing if the colors looked okay. Now with the colors being brighter, I
could see that passing it straight through looked fine, but
intentionally reversing it to be BGR resulted in colors that at a
distance looked okay, but were either washed out or too bright. At least
finally I could use my 8 years of playing this game for something.

So in conclusion, actually, 37b7615b71c3a2f44e03c47894383107850812ff
("Fix surface color masks") was the real fix, and
d271907f8c5d84308a3cf9323ac692199b8685a6 ("Fix Secret Lab Time Trial
trophies having wrong colors") was the real regression. It's just that
the regression came first, but it wasn't really a regression until I did
the other fix, so the fix isn't the regression, the regression is...
this is hurting my brain. Or the real regression was the friends we made
along the way, or something like that.

This is the most trivial bug ever caused by the technical debt of those
god-awful reversed color masks.

---

This reverts commit d271907f8c5d84308a3cf9323ac692199b8685a6.

Fixes #862.

---
## [kirtiraj22/competitive_programming_solutions](https://github.com/kirtiraj22/competitive_programming_solutions)@[cc4b10d341...](https://github.com/kirtiraj22/competitive_programming_solutions/commit/cc4b10d341d60b89fa07b0ff42f4466430b26aef)
#### Monday 2022-03-14 06:05:59 by Kirtiraj

Create CF_4A.cpp

QUESTION LINK: https://codeforces.com/problemset/problem/4/A

QUESTION:One hot summer day Pete and his friend Billy decided to buy a watermelon. They chose the biggest and the ripest one, in their opinion. After that the watermelon was weighed, and the scales showed w kilos. They rushed home, dying of thirst, and decided to divide the berry, however they faced a hard problem.

Pete and Billy are great fans of even numbers, that's why they want to divide the watermelon in such a way that each of the two parts weighs even number of kilos, at the same time it is not obligatory that the parts are equal. The boys are extremely tired and want to start their meal as soon as possible, that's why you should help them and find out, if they can divide the watermelon in the way they want. For sure, each of them should get a part of positive weight



SAMPLE INPUT:
8

SAMPLE OUTPUT:
YES

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[2a16fbdf69...](https://github.com/treckstar/yolo-octo-hipster/commit/2a16fbdf6918eb2f4e1da05bf11dbad360c98cd3)
#### Monday 2022-03-14 06:10:03 by BB

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [freesewing/freesewing](https://github.com/freesewing/freesewing)@[67da7dd595...](https://github.com/freesewing/freesewing/commit/67da7dd5950f3e3ed39a190c23f3cd8b095cd93f)
#### Monday 2022-03-14 07:22:38 by Joost De Cock

feat(lab): First stab at custom layout

This adds a React component to handle custom layouts.
This React component is a long way from perfect, but it's a start.

There are two reasons that (at least in my opinion) implementing this is non-trivial:

1) React re-render vs DOM updates

   For performance reasons, we can't re-render with React when the user drags a
   pattern part (or rotates it). It would kill performance.
   So, we don't re-render with React upon dragging/rotating, but instead manipulate
   the DOM directly.

   So far so good, but of course we don't want a pattern that's only correctly laid
   out in the DOM. We want to updat the pattern gist so that the new layout is stored.
   For this, we re-render with React on the end of the drag (or rotate).

   Handling this balance between DOM updates and React re-renders is a first contributing
   factor to why this component is non-trivial

2) SVG vs DOM coordinates

   When we drag or rotate with the mouse, all the events are giving us coordinates of
   where the mouse is in the DOM.

   The layout uses coordinates from the embedded SVG which are completely different.
   So we need to make this translation and that adds complexity.

3) Part-level transforms

   It's not just that the DOM coordinates and SVG coordinate system is different, each
   part also has it's own transforms applied and because of this behaves as if they have
   their own coordinate system.

   In other words, a point (0,0) in the part is not the top-left corner of the page.
   In the best-case scenario, it's the top-left corner of the part. But even this is
   often not the case as parts will have transforms applied to them.

4) Flip along X or Y axis

   Parts can be flipped along the X or Y axis to facilitate a custom layout.
   This is handled in a transform, so the part's coordinate's don't actually change. They
   are flipped late into the rendering process (by the browser displaying the SVG).

   Handling this adds yet more mental overhead

5) Bounding box

   While moving and rotating parts around is one thing. Recalculating the bounding box
   (think auto-cropping the pattern) gets kinda complicated because of the reasons
   outlined above.

   We are currently handling a lot in the frontend code. It might be more elegant to move
   some of this to core. For example, core expects the custom layout to set the widht and height
   rather than figuring it out on its own as it does for auto-generated layouts.

 Known issues

 - Rotating gets a little weird sometimes as the part rotates around it's center in the
   SVG coordinate system, but the mouse uses it's own coordinates as the center point that's
   used to calculate the angle of the rotation

 - Moving parts into the negative space (minus X or Y coordinated) does not extend the bounding box.

 - Rotation gets weird when a part is mirrored

 - The bounding box update when a part is rotated is not entirely accurate

I've sort of left it at this because I'm starting to wonder if we should perhaps re-think
how custom layouts are supported in the core. And I would like to discuss this with the core team.

---
## [polinaeterna/datasets](https://github.com/polinaeterna/datasets)@[a8fa7cfe95...](https://github.com/polinaeterna/datasets/commit/a8fa7cfe95e06c8a667c4d7c5b7c7287b7e9ac4f)
#### Monday 2022-03-14 09:40:57 by RenChu Wang

Multi-GPU support for `FaissIndex` (#3721)

* 🎉 This commit fixes huggingface/datasets#3716

This commit adds handling for faiss indices that run on multiple GPUs.

* 🤕 Stupid mistake in that index isn't returned in the function handling device.

Now it's fixed. Hopefully the PR isn't merged yet!

* 🗎 Updated documents to reflect changes I made in the code.

Update `device`'s document to include negative numbers and lists.

* 1️⃣ The line should not exceed length: 119

It seems that this is what circle CI checked anyways.

* 🥴 Apply suggestions from code review

Missed it the first time :)

Co-authored-by: Albert Villanova del Moral <8515462+albertvillanova@users.noreply.github.com>

* 🛠️ Fixed my fixes.

Updated code to address concerns.

* 🇫 Update src/datasets/search.py

Using f-strings in docs.

Co-authored-by: Quentin Lhoest <42851186+lhoestq@users.noreply.github.com>

Co-authored-by: Albert Villanova del Moral <8515462+albertvillanova@users.noreply.github.com>
Co-authored-by: Quentin Lhoest <42851186+lhoestq@users.noreply.github.com>

---
## [arteam/elasticsearch](https://github.com/arteam/elasticsearch)@[37ea6a8255...](https://github.com/arteam/elasticsearch/commit/37ea6a8255623d41be7df11440610ffa958ce50e)
#### Monday 2022-03-14 09:53:15 by Nik Everett

TSDB: Support GET and DELETE and doc versioning (#82633)

This adds support for GET and DELETE and the ids query and
Elasticsearch's standard document versioning to TSDB. So you can do
things like:
```
POST /tsdb_idx/_doc?filter_path=_id
{
  "@timestamp": "2021-12-29T19:25:05Z", "uid": "adsfadf", "v": 1.2
}
```

That'll return `{"_id" : "BsYQJjqS3TnsUlF3aDKnB34BAAA"}` which you can turn
around and fetch with
```
GET /tsdb_idx/_doc/BsYQJjqS3TnsUlF3aDKnB34BAAA
```
just like any other document in any other index. You can delete it too!
Or fetch it.

The ID comes from the dimensions and the `@timestamp`. So you can
overwrite the document:
```
POST /tsdb_idx/_bulk
{"index": {}}
{"@timestamp": "2021-12-29T19:25:05Z", "uid": "adsfadf", "v": 1.2}
```

Or you can write only if it doesn't already exist:
```
POST /tsdb_idx/_bulk
{"create": {}}
{"@timestamp": "2021-12-29T19:25:05Z", "uid": "adsfadf", "v": 1.2}
```

This works by generating an id from the dimensions and the `@timestamp`
when parsing the document. The id looks like:
* 4 bytes of hash from the routing calculated from routing_path fields
* 8 bytes of hash from the dimensions
* 8 bytes of timestamp
All that's base 64 encoded so that `Uid` can chew on it fairly
efficiently.

When it comes time to fetch or delete documents we base 64 decode the id
and grab the routing from the first four bytes. We use that hash to pick
the shard. Then we use the entire ID to perform the fetch or delete.

We don't implement update actions because we haven't written the
infrastructure to make sure the dimensions don't change. It's possible
to do, but feels like more than we need now.

There *ton* of compromises with this. The long term sad thing is that it
locks us into *indexing* the id of the sample. It'll index fairly
efficiently because the each time series will have the same first eight
bytes. It's also possible we'd share many of the first few bytes in the
timestamp as well. In our tsdb rally track this costs 8.75 bytes per
document. It's substantial, but not overwhelming.

In the short term there are lots of problems that I'd like to save for a
follow up change:
1. ~~We still generate the automatic `_id` for the document but we don't use
   it. We should stop generating it.~~ Included in this PR based on review comments.
2. We generated the time series `_id` on each shard and when replaying
   the translog. It'd be the good kind of paranoid to generate it once
   on the primary and then keep it forever.
3. We have to encode the `_id` as a string to pass it around
   Elasticsearch internally. And Elasticsearch assumes that when an id
   is loaded we always store as bytes encoded the `Uid` - which *does*
   have nice encoding for base 64 bytes. But this whole thing requires
   us to make the bytes, base 64 encode them, and then hand them back to
   `Uid` to base 64 decode them into bytes. It's a bit hacky. And, it's
   a small thing, but if the first byte of the routing hash encodes to
   254 or 255 we `Uid` spends an extra byte to encode it. One that'll
   always be a common prefix for tsdb indices, but still, it hurts my
   heart. It's just hard to fix.
4. We store the `_id` in Lucene stored fields for tsdb indices. Now
   that we're building it from the dimensions and the `@timestamp` we
   really don't *need* to store it. We could recalculate it when fetching
   documents. In the tsdb rall ytrick this'd save us 6 bytes per document
   at the cost of marginally slower fetches. Which is *fine*.
5. There are several error messages that try to use `_id` right now
   during parsing but the `_id` isn't available until after the parsing
   is complete. And, if parsing fails, it may not be possible to know
   the id at all. All of these error messages will have to change,
   at least in tsdb mode.
6. ~~If you specify an `_id` on the request right now we just overwrite
   it. We should send you an error.~~ Included in this PR after review comments.
7. We have to entirely disable the append-only optimization that allows
   Elasticsearch to skip looking up the ids in lucene. This *halves*
   indexing speed. It's substantial. We have to claw that optimization
   back *somehow*. Something like sliding bloom filters or relying on
   the increasing timestamps.
8. We parse the source from json when building the routing hash when
   parsing fields. We should just build it from to parsed field values.
   It looks like that'd improve indexing speed by about 20%.
9. Right now we write the `@timestamp` little endian. This is likely bad
   the prefix encoded inverted index. It'll prefer big endian. Might shrink it.
10. Improve error message on version conflict to include tsid and timestamp.
11. Improve error message when modifying dimensions or timestamp in update_by_query
12. Make it possible to modify dimension or timestamp in reindex.
13. Test TSDB's `_id` in `RecoverySourceHandlerTests.java` and `EngineTests.java`.

I've had to make some changes as part of this that don't feel super
expected. The biggest one is changing `Engine.Result` to include the
`id`. When the `id` comes from the dimensions it is calculated by the
document parsing infrastructure which is happens in
`IndexShard#pepareIndex`. Which returns an `Engine.IndexResult`. To make
everything clean I made it so `id` is available on all `Engine.Result`s
and I made all of the "outer results classes" read from
`Engine.Results#id`. I'm not excited by it. But it works and it's what
we're going with.

I've opted to create two subclasses of `IdFieldMapper`, one for standard
indices and one for tsdb indices. This feels like the right way to
introduce the distinction, especially if we don't want tsdb to cary
around it's old fielddata support. Honestly if we *need* to aggregate on
`_id` in tsdb mode we have doc values for the `tsdb` and the
`@timestamp` - we could build doc values for `_id` on the fly. But I'm
not expecting folks will need to do this. Also! I'd like to stop storing
tsdb'd `_id` field (see number 4 above) and the new subclass feels like
a good place to put that too.

---
## [MurdoMaclachlan/website](https://github.com/MurdoMaclachlan/website)@[04b921ff1f...](https://github.com/MurdoMaclachlan/website/commit/04b921ff1f37f43e8e5eaf42d4a23e66aea5c502)
#### Monday 2022-03-14 10:37:54 by Murdo B. Maclachlan

Don't include localhost links in prod you fucking idiot

I am truly that stupid

Signed-off-by: Murdo B. Maclachlan <murdomaclachlan@duck.com>

---
## [FyodoRaev/Sample-ML-Repo](https://github.com/FyodoRaev/Sample-ML-Repo)@[bca7d9d31d...](https://github.com/FyodoRaev/Sample-ML-Repo/commit/bca7d9d31dfb56a5d0ae3e0fdaa7b455dbf5b86a)
#### Monday 2022-03-14 11:39:00 by FyodoRaev

I WANT TO ADD CHANGES YOU ARE  FUCKING STUPID UGLY BITCH

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[2c65578339...](https://github.com/mrakgr/The-Spiral-Language/commit/2c65578339cdc56ff8db516885e75dfde302db64)
#### Monday 2022-03-14 12:34:56 by Marko Grdinić

"9:05am. I am up. Let me chill for a bit and I will start the tutorials.

9:30am. Let me start. It is finally time I play with scattering.

9:35am. Focus me.

https://youtu.be/i2QYOnqTc4M?list=PLOZhw3kXDRQelts3VZKzhPySQi2JAofUf
Beginner's Journey with Clarisse - Part4 - Procedural Layout

9:40am. https://youtu.be/i2QYOnqTc4M?list=PLOZhw3kXDRQelts3VZKzhPySQi2JAofUf&t=64

Oh, oh wow. That tree he created thousands of instances of? It has 720k polygons! This is a huge amount to just instance around. Whatever optimizations Clarisse does to make this work under the hood are pretty magical.

9:40am. The tree is very well made. A hint in how Clarisse's renderer woorks can be found in how the rendering progresses. It works like a binary search whether iteratively refines smaller and smaller squares. This is contrast to V-Ray where refines points at random.

I have to accept it, Clarisse is simply better at its job than them.

9:45am. I need the equivalent of Clarisse in ML. Right now, what I have are only the equivalents of Houdini in ML. With algorithmic advances I could make huge further breakthroughs, but I need resources to make them happen.

9:50am. For reference, I once downlaoded a free low poly forest off Blenderkit, a small forest that had a few dozen low poly trees, whose trees probably 10x less polys each than this one, and it was enough to make Blender churn noticeably.

Also, I've thought about my plans a bit. Even if Houdini can't be used to display huge cities, I should be able to use it to proceduraly generate the point clouds for it and import those into Clarisse in order to instance them.

For my old scene, Blender is one thing, but Clarisse should have proper USD importers. Or I can import it as Alembic. It is no problem either way. I should be able to continue from where I left off last time (minus the shaders) and finish the scene in Clarisse. I won't have to spend time doing the entire thing from scratch.

I spent 2 months learning Houdini, but maybe that won't turn out to be a waste. Houd should have good synergy with Clarisse.

9:55am. Now focus me. I am just ranting here.

My art journey is definitely not over yet. I can get a lot better.

10:10am. Focus me. I have a problem. I do not get the sense it is distributing the points correctly.

https://youtu.be/i2QYOnqTc4M?list=PLOZhw3kXDRQelts3VZKzhPySQi2JAofUf&t=201

Let me try putting them on the ship instead.

10:15am. Yeah, that is much easier to see being wrong. Without parenting it just puts it at the origin point. With parenting, the points get moved up, but not in the right place.

Ah, I see. I should have checked off Parent In Place before creating the point cloud. What this affects is the Inherit Transform option in Kinematics > Advanced. Let me note that in a Youtube comment.

10:30am. Now it is right.

10:35am. Wow, it scattered 50k of these trees like it was nothing. If I hadn't saw it, I woudln't have believed this was possible!

https://youtu.be/i2QYOnqTc4M?list=PLOZhw3kXDRQelts3VZKzhPySQi2JAofUf&t=419

After decimating the points underneath the lake that still leave 31k of them. Yeah, I am really happy about this. This is how art should be done. If I didn't have this program, my future would be a lot different.

https://youtu.be/i2QYOnqTc4M?list=PLOZhw3kXDRQelts3VZKzhPySQi2JAofUf&t=503

Instead of decimating, it would be better to just turn the scope texture into a sampling texture.

Oh wow, it actually grays out the invalid inputs in the material editor. Slick.

In the next PL review, I can see myself bashing V-Ray for Houdini and praising Clarisse.

11:05am. Nope, the idea is not working for me. Well it makes sense given that the snow crater map is a 2d texture and the scope texture is 3d. Maybe if I changed the number of dimensions to XZ?

https://youtu.be/i2QYOnqTc4M?list=PLOZhw3kXDRQelts3VZKzhPySQi2JAofUf&t=529

He just wants to decimate the points like this? Let me try the screen myself. I have no idea what these color modes are. I tried using the math multiply and it failed for me.

11:25am. I can't make it work. Decimate is a 3d texture, and the other is 2d.

It is a pity. Maybe I'll figure out a way later when I have more knowledge.

11:35am. Primitive count: 20.556 billion. I am not noticing any slowdown at all when navigating compared to when I started. Remarkable, simply remarkable. This makes other pograms look like children's toys.

Ah, I see. In display there is the display pickable. I can use that to make an object non-selectable.

12:15pm. I do not know what happened, but I lost just a tad. Did I somehow switch project files and the overwrite it when making an empty one. How did that happen?

12:50pm. https://youtu.be/i2QYOnqTc4M?list=PLOZhw3kXDRQelts3VZKzhPySQi2JAofUf&t=1010

It is not working for me at all. Why is the clip map all black?

> Remember to always disable mipmapping  when using Texture Maps as clip maps. Because of mipmapping the opacity of the texture will vary according to the distance of the object to the camera. Typically, the further the object, the more transparent it will get.

What is mipmapping and how do I disable it. In the first place I am not using a texture map, but a gradient map.

1:05pm. file:///C:/Program%20Files/Isotropix/Clarisse%205.0%20SP7/Clarisse/docs/common/index.html#3d-view.html

The inbuilt GPU renderer has some limitations.

I don't know. Let me try pacity.

1:10pm. For some reason the gradient map only acts in the up direction.

1:15pm. The remap for this is really amamzing. It does not go from 0 to 1 like I expected, but in the other direction as well.

1:25pm. I can't get the back color to work. I haven't figured this out properly. No, the inside parts are what is causing me trouble. They end up being shaded dark.

Ahhh, I need to make it double sided. Now've re talking.

Yeah, now it works.

1:35pm. But now like in the video. I need to play with this more. Let me stop here so I can have breakfast."

---
## [a3-Prjkt/kernel_xiaomi_ginkgo_consistenX](https://github.com/a3-Prjkt/kernel_xiaomi_ginkgo_consistenX)@[3c23a8d4c6...](https://github.com/a3-Prjkt/kernel_xiaomi_ginkgo_consistenX/commit/3c23a8d4c60097354fe9dde538a39dd6554c17ba)
#### Monday 2022-03-14 12:37:16 by George Spelvin

lib/sort: make swap functions more generic

Patch series "lib/sort & lib/list_sort: faster and smaller", v2.

Because CONFIG_RETPOLINE has made indirect calls much more expensive, I
thought I'd try to reduce the number made by the library sort functions.

The first three patches apply to lib/sort.c.

Patch #1 is a simple optimization.  The built-in swap has special cases
for aligned 4- and 8-byte objects.  But those are almost never used;
most calls to sort() work on larger structures, which fall back to the
byte-at-a-time loop.  This generalizes them to aligned *multiples* of 4
and 8 bytes.  (If nothing else, it saves an awful lot of energy by not
thrashing the store buffers as much.)

Patch #2 grabs a juicy piece of low-hanging fruit.  I agree that nice
simple solid heapsort is preferable to more complex algorithms (sorry,
Andrey), but it's possible to implement heapsort with far fewer
comparisons (50% asymptotically, 25-40% reduction for realistic sizes)
than the way it's been done up to now.  And with some care, the code
ends up smaller, as well.  This is the "big win" patch.

Patch #3 adds the same sort of indirect call bypass that has been added
to the net code of late.  The great majority of the callers use the
builtin swap functions, so replace the indirect call to sort_func with a
(highly preditable) series of if() statements.  Rather surprisingly,
this decreased code size, as the swap functions were inlined and their
prologue & epilogue code eliminated.

lib/list_sort.c is a bit trickier, as merge sort is already close to
optimal, and we don't want to introduce triumphs of theory over
practicality like the Ford-Johnson merge-insertion sort.

Patch #4, without changing the algorithm, chops 32% off the code size
and removes the part[MAX_LIST_LENGTH+1] pointer array (and the
corresponding upper limit on efficiently sortable input size).

Patch #5 improves the algorithm.  The previous code is already optimal
for power-of-two (or slightly smaller) size inputs, but when the input
size is just over a power of 2, there's a very unbalanced final merge.

There are, in the literature, several algorithms which solve this, but
they all depend on the "breadth-first" merge order which was replaced by
commit 835cc0c8477f with a more cache-friendly "depth-first" order.
Some hard thinking came up with a depth-first algorithm which defers
merges as little as possible while avoiding bad merges.  This saves
0.2*n compares, averaged over all sizes.

The code size increase is minimal (64 bytes on x86-64, reducing the net
savings to 26%), but the comments expanded significantly to document the
clever algorithm.

TESTING NOTES: I have some ugly user-space benchmarking code which I
used for testing before moving this code into the kernel.  Shout if you
want a copy.

I'm running this code right now, with CONFIG_TEST_SORT and
CONFIG_TEST_LIST_SORT, but I confess I haven't rebooted since the last
round of minor edits to quell checkpatch.  I figure there will be at
least one round of comments and final testing.

This patch (of 5):

Rather than having special-case swap functions for 4- and 8-byte
objects, special-case aligned multiples of 4 or 8 bytes.  This speeds up
most users of sort() by avoiding fallback to the byte copy loop.

Despite what ca96ab859ab4 ("lib/sort: Add 64 bit swap function") claims,
very few users of sort() sort pointers (or pointer-sized objects); most
sort structures containing at least two words.  (E.g.
drivers/acpi/fan.c:acpi_fan_get_fps() sorts an array of 40-byte struct
acpi_fan_fps.)

The functions also got renamed to reflect the fact that they support
multiple words.  In the great tradition of bikeshedding, the names were
by far the most contentious issue during review of this patch series.

x86-64 code size 872 -> 886 bytes (+14)

With feedback from Andy Shevchenko, Rasmus Villemoes and Geert
Uytterhoeven.

Link: http://lkml.kernel.org/r/f24f932df3a7fa1973c1084154f1cea596bcf341.1552704200.git.lkml@sdf.org
Signed-off-by: George Spelvin <lkml@sdf.org>
Acked-by: Andrey Abramov <st5pub@yandex.ru>
Acked-by: Rasmus Villemoes <linux@rasmusvillemoes.dk>
Reviewed-by: Andy Shevchenko <andriy.shevchenko@linux.intel.com>
Cc: Rasmus Villemoes <linux@rasmusvillemoes.dk>
Cc: Geert Uytterhoeven <geert@linux-m68k.org>
Cc: Daniel Wagner <daniel.wagner@siemens.com>
Cc: Don Mullis <don.mullis@gmail.com>
Cc: Dave Chinner <dchinner@redhat.com>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: Yousef Algadri <yusufgadrie@gmail.com>
Signed-off-by: Panchajanya1999 <panchajanya@azure-dev.live>

---
## [FernandoJ8/fulpstation](https://github.com/FernandoJ8/fulpstation)@[c449fbb56c...](https://github.com/FernandoJ8/fulpstation/commit/c449fbb56c7cb57fc9d8c0db32be0b66e6d7293b)
#### Monday 2022-03-14 14:19:44 by SgtHunk

Fixes Solitaire runtimes + missing APCs (#488)

* solitaire fixes

* fuck you bar decals

---
## [svenoaks/Low-Latency-Android-Audio-iOS-Audio-Engine](https://github.com/svenoaks/Low-Latency-Android-Audio-iOS-Audio-Engine)@[5fce9facf9...](https://github.com/svenoaks/Low-Latency-Android-Audio-iOS-Audio-Engine/commit/5fce9facf9cdb4047295d23b33ee2ae6bfd9ac5a)
#### Monday 2022-03-14 14:51:00 by Gabor Szanto

0.9 with Superpowered Dynamics and NI Stems

NEW FEATURES

- Introducing Superpowered Dynamics with 3 new features: a compressor,
a limiter and a clipper.

- The new Superpowered Clipper class implements a hard-knee clipper
with adjustable threshold and maximum decibel settings. You can prevent
clipping in your audio stream with this super lightweight feature,
which runs 3 times faster than a simple filter!

- The new Superpowered Compressor is a classic all-round compressor
with very low distortion, a nice curve and many settings: input and
output gain, dry/wet, attack and release times, ratio, threshold. It
also has an adjustable high-pass filter for the sidechain! The
Superpowered Compressor needs less than 1 kb of memory and has 0
latency (of course!). It’s very CPU friendly, requiring just 5x CPU
compared to a SuperpoweredFilter.

- The new Superpowered Limiter provides amazing sound even when you are
crushing it to -40 db. You can set the ceiling, threshold and release.
It’s very friendly to any device with very low memory usage (below 1
kb), and it uses just 2.5x CPU compared to a SuperpoweredFilter (great
battery saving!).

- Support for the Native Instruments Stems format with super high
performance. To re-create the exact same sound designed in the Stems
Creator tool by the audio engineer or musician, the sound of the
SuperpoweredCompressor and SuperpoweredLimiter is closely matched to
the sound of the original compressor and limiter by Native Instruments.
Certainly, the SuperpoweredDecoder, SuperpoweredCompressor and
SuperpoweredLimiter supercharges the Native Instruments Stems format
with much higher processing speed and lower battery usage.

- The SuperpoweredAnalyzer can find and return with the stream of bass
and mid keys, to extract bass and melody notes from the source audio
stream.

- The new SuperpoweredWaveform class offers an even higher performance
way over the SuperpoweredAnalyzer to return simpler waveform data,
based on the peak volume.

IMPROVEMENTS

- The SuperpoweredFlanger uses the SuperpoweredClipper now to prevent
audio spikes.

- The SuperpoweredDecoder returns with various Native Instruments Stems
data (colors, names, settings). You can set which stems track should it
decode. These changes are reflected in the
SuperpoweredAdvancedAudioPlayer class as well.

- The offline example project is extended with a simple decode >>>
filter >>> save-to-WAV example.

- Xcode 7 support with separately built iOS and OSX binaries.

ANDROID IMPROVEMENTS

- 64-bit Intel Android support.

- Android Studio does not offer complete native/C++ support with static
libraries, still. It’s the official statement by it’s creators too. We
tried the new “experimental” Gradle system and hacked really hard to
find a way. Having the nice new C++ support and even building with
Superpowered is possible, so it’s almost there. But building for
multiple architectures with static libraries is not possible with the
experimental Gradle system currently.

- SuperpoweredAndroidAudioIO is now lock free to prevent dropouts due
priority inversion on poorly configured Android devices. It also has an
alternative “separate processing thread” option for very old or very
badly configured Android devices.

- Updated Android example projects to 32-bit ARM, 64-bit ARM, 32-bit
Intel and 64-bit Intel architectures, with a little path setting help
for Windows users.

---
## [BIGGIB64/docs](https://github.com/BIGGIB64/docs)@[9b1a978f2a...](https://github.com/BIGGIB64/docs/commit/9b1a978f2ac0cd2fdc74c58c7f5ef4da9e345c09)
#### Monday 2022-03-14 15:31:26 by BIGGIB64

--- title: Quickstart intro: 'Get started using {% data variables.product.product_name %} to manage Git repositories and collaborate with others.' versions:   fpt: '*'   ghes: '*'   ghae: '*'   ghec: '*' topics:   - Pull requests   - Issues   - Notifications   - Accounts children:   - /hello-world   - /set-up-git   - /create-a-repo   - /fork-a-repo   - /github-flow   - /contributing-to-projects   - /be-social   - /communicating-on-github   - /github-glossary   - /git-cheatsheet   - /git-and-github-learning-resources redirect_from:   - /github/getting-started-with-github/quickstart ---

To be honest that is something that's beyond me eyes I'm 16 years old now and not nearly as tech-savvy as I used to be and I'm also getting a pretty debilitating liver and kidney disease so it's a hard for me to do some of those things I'm going to try I don't want to mess anything up for you guys I mean I've been nothing but good to me that was supposed to say you guys then that means i have no idea what to do

---
## [clamor-s/u-boot](https://github.com/clamor-s/u-boot)@[d35e7180ca...](https://github.com/clamor-s/u-boot/commit/d35e7180ca5b21d9f4e8c22361695aaafcea6b14)
#### Monday 2022-03-14 15:45:28 by Marcel Ziswiler

tegra: lcd: video: integrate display driver for t30

On popular request make the display driver from T20 work on T30 as
well. Turned out to be quite straight forward. However a few notes
about some things encountered during porting: Of course the T30 device
tree was completely missing host1x as well as PWM support but it turns
out this can simply be copied from T20. The only trouble compiling the
Tegra video driver for T30 had to do with some hard-coded PWM pin
muxing for T20 which is quite ugly anyway. On T30 this gets handled by
a board specific complete pin muxing table. The older Chromium U-Boot
2011.06 which to my knowledge was the only prior attempt at enabling a
display driver for T30 for whatever reason got some clocking stuff
mixed up. Turns out at least for a single display controller T20 and
T30 can be clocked quite similar. Enjoy.

Signed-off-by: Marcel Ziswiler <marcel.ziswiler@toradex.com>
Signed-off-by: Svyatoslav Ryhel <clamor95@gmail.com>

---
## [IrkallaEpsilon/BoH-Bay](https://github.com/IrkallaEpsilon/BoH-Bay)@[d012aea165...](https://github.com/IrkallaEpsilon/BoH-Bay/commit/d012aea165041c2bda3c79c74acffe5fe7ef40ed)
#### Monday 2022-03-14 17:04:09 by IrkallaEpsilon

Fucking Irkalla starts 'coding' or rather reflavoring shit again somebody stop them before they stealth buff cargo for joe jones gimmicks

About The Pull Request
This reflavors the Tiro equipment, part of a series to make them more into COMBINE or ADVENT troopers instead of what it was before. Will change later (not today) the description for the particle magnum as well and alter the "par" sigil to be something else.

Par means "equal". Somehow I was not aware of that. That is on par of doing.. wait I get it.

Auctus means  "augmented"/enhanced. The suit already got a few nerfs in so its more on par with Alate suits. Could still be changed by somebody that knows balancing better than I do to make it weaker. The suit is basicly now an "augmented" Tiro suit. Mentions of being the Gynes personal bodyguard are squashed. They are now more akin to combine elite or advent officers. Which fits them better if you ask me but dunno. Just thought this would suit it better. 

Why It's Good For The Game
Swear to god I am going to beat Tiros with a crowbar clustertool if that isnt going to be reflavored into something more akin to COMBINE or ADVENT. That and the fucking alate that always puts ~ at the end of every sentence. You know who you are.

Did You Test It?
No, I just changed description names.

Authorship
Irkalla Epsilon

Changelog
🆑
tweak: Combinefies/Adherentifies Ascent Tiros and makes them less ERPy with their gears flavortext. This is a multi step series. Ascent Par suit to Auctus. Pars are now "Auctus" or "Augmented". No more bodyguard flavortext on this particular suit. To do: Change particle magnum and par emblem to something similar. Fuck coding. I go back make materials and shit.
/🆑

---
## [Pavelrichter2312/philosophy](https://github.com/Pavelrichter2312/philosophy)@[5157ed99bd...](https://github.com/Pavelrichter2312/philosophy/commit/5157ed99bdd9d1c5f95b1c48994b5e3738d9b082)
#### Monday 2022-03-14 17:35:03 by Pavelrichter2312

Add files via upload

Hello, I think that the human is not exist for drinking and eating. In contrast with an animal, human nature include two components: nefesh (it is starving to live, an animal nature) and something, helping us to know the true things origin. This quality has been making us think about something ideal, even if we have never seen it. It makes me think human biological life has not high price, but his intellect, his ability to dream is invaluable. According to this logic, it can comes to a though that world will be divided into the two parts. Peace of people like an environment and people like an entity.

---
## [Terminator-J/crdroid_kernel_oneplus_sdm845](https://github.com/Terminator-J/crdroid_kernel_oneplus_sdm845)@[cadd3844db...](https://github.com/Terminator-J/crdroid_kernel_oneplus_sdm845/commit/cadd3844db47d8a87f80308498743affbd298784)
#### Monday 2022-03-14 18:38:07 by alk3pInjection

drm: Handle dim for udfps

* Apparently, los fod impl is better than udfps cuz it
  has onShow/HideFodView hook, which allows us to toggle
  dimlayer seamlessly.

  Since udfps only partially supports the former one,
  we'd better kill dim in kernel. This is kinda a hack
  but it works well, bringing perfect fod experience
  back to us.

Co-authored-by: Art_Chen <Chenxy0201@qq.com>
Signed-off-by: alk3pInjection <webmaster@raspii.tech>
Change-Id: I80bfd508dacac5db89f4fff0283529c256fb30ce

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[552f3019fe...](https://github.com/mrakgr/The-Spiral-Language/commit/552f3019fecff9c980688953b67fe12897bd7669)
#### Monday 2022-03-14 20:10:37 by Marko Grdinić

"3:05pm. By the way, a new Satanophany raw came out yesterday. It has been a long hiatus. I really admire the art. Someday I'll bea be able to make art of that level myself. For now...

Let me resume. I need to play with the gradient texture.

3:25pm. I figured it out. It seems v of 0 starts at the bottom and makes it way up. The best way to make the gradient symmetrical is to work on it in 0.5 range and set it to oscilate out of bounds.

https://youtu.be/i2QYOnqTc4M?list=PLOZhw3kXDRQelts3VZKzhPySQi2JAofUf&t=1041

Ah, so this is how he will color it. Good idea. But isn't there a ramp somewhere?

3:40pm. Clarisse crashed when I tried renaming the context. Yeah, it might be fast, but it is not bug free by any means.

I should have put it in a combiner for easier manipulation.

> Program received exception EXCEPTION_ACCESS_VIOLATION (0xC0000005).

It crashed again. It really started churning when I put in the planet.

3:55pm. Got the planet placed.

https://youtu.be/Z--Mylr2RZU
Manipulating and Snapping Items

Let me watch this. The fact that I do not have Blender style hotkeys really hurts.

https://youtu.be/Z--Mylr2RZU?t=73

While moving the planet I completely forgot about planar selection.

4:15pm. The fact that Clarisse does not have Blender style hotkeys is such a hillarious omission. It would be funny if only I did not have to use it.

Blender really did a good job with it UI if nothing else.

Let me move on. Time to finish this tutorial.

4:20pm. This is ultra supper annoying. The planet is not visible through the fog and to make matters worse, for some reason pressing m is refusing to put the manipulator where I want it. What the hell?

4:40pm. Finally put it in the right place. Just what is the manipulator space?

Ahhhhh...I could have tried looking through the planet perhaps?

Nope. It only works for lights and cameras. Still it might have worked if I did that with the camera.

I could have created a camera and parented the planet to it.

Then positioned the camera.

Forget it. It was not that difficult to warant this.

4:55pm. I just scattered 1m points like it was nothing. Now let me scatter some spheres on that.

5pm. Most impressive. It works without a hitch. What if I made it polyspheres?

...Even if added a ton of geometry to them it still works. This program is magical.

5:10pm. It seems that scatter scale really just adds to the scale. So the values above 1 can invert it. Lame.

5:20pm. Added the stars. Right now I am just watching it render. But it takes a while. If I had to do the stars it would be better to bake it into a texture. Still, despite it bieng 1m lights in the scene it is still relatively fast If I had a Threadripper CPU, I bet I could see some real speedups. Maybe in the end, I'll be buying CPUs to improve my rendering time. It looks very nice. If only I could save this image.

I'll take care of things like that in due time.

5:25pm. He says something like each star being a simple mat? material where each star is picking up a color from a gradient. I don't know how to do that.

https://youtu.be/i2QYOnqTc4M?list=PLOZhw3kXDRQelts3VZKzhPySQi2JAofUf&t=1197

I'll take a look at the finished scene to see how the stars were done. Let me do it now.

5:30pm. It seems texture gradient is the ramp. Right now I am looking at the file. First it gets the object id from the utility node, passes it to texture randomize, then through a ramp. Then that is saturated by -80%. Then multiplied by 5. Then at last it is passed into the matte node as its color.

> A material that define a matte color, with no light shading.

Does that mean it appears fully colored in the sky rather than falling off in brightness like a regular diffuse material? Let me open a new file. I'll try it out.

6pm. It is already 6? The time sure flew by today.

I'll keep on going of course.

First of all, the Matte confuses me. At first I thought it was an emitter, but it turns out when it has red in its spectrum, objects further away get red speckles on them.

Ahhh, I see. That is because although the object material was pure red, I did not see that in the darkness. I forgot that I set it to red.

6:25pm. Ok, I see.

Matte is definitely an emitter though it lacks the exposure option. It is possible to put lights on polygonal geometry, but it is not possible to scatter it unfortunate. Like in V-Ray, the emitter objects tend to be noisy, a lot moreso than lights. There is probably a good reason why lights cannot be scattered. Light objects themselves are probably heavily optimized under the hood.

I am thinking. Since desaturating the color actually increases its intesity, I wonder why it gets multiplied by 5? I'll leave that mystery for later.

6:25pm. I just realized that the reason why moving offsets moved other objets is probably because moving the offset (pivot) of the instance actually moves the offset of the parent. That is why I had such confusing behavior. Ok...

https://youtu.be/ZlmRuR5MKmU
Angie: The next gen CPU+GPU Renderer

Let me watch this. Lunch should be soon.

I think after I finish the tutorial that I should focus on importing the Houdini scene into Clarisse. Organizing it will be hell, but I'll manage it.

...I've been wondering this for a while, but is Mick Gordon composing music for these videos?

https://youtu.be/ZlmRuR5MKmU?t=51

Its fully based on OSL. I should be able to bring in those OSL noise shaders from V-Ray into Clarisse should I want to even without Angie.

What is R2C?

https://youtu.be/ZlmRuR5MKmU?t=150

It seems this is an entire city in the background.

https://youtu.be/ZlmRuR5MKmU?t=172

2.8 is not that much of a gain, but AMD 3990x is a threadripper with 64 cores. I am guessing that when put against my own CPU things would be a lot better. Still, not that much better.

https://youtu.be/ZlmRuR5MKmU?t=190

He remarks as much.

6:45pm. https://youtu.be/-5CVXzfRE98
Clarisse Angie First impression

Let me watch this.

https://youtu.be/YdFW5IyDd4E
Why You Should be a Perfectionist - Weekly Wrangle #35 - CG Forge

And this. They are only 10m each. I need a break from tutorials. It is good to get hyped a bit for the future.

https://youtu.be/-5CVXzfRE98?t=131

He notes that you can import OBJ, Alembics and USDs, but not FBX. I'll manage it.

This is a great intro vid for Clarisee. I think I'll link to it in the next PL update.

7:05pm. Forget the philosophical vid. Let me resume.

...Actually when is lunch? Soon.

7:10pm. SL_Gathering is a group. Of course. Now I see the content type. Previously I missed it because my screen was so packed.

7:15pm. Damn, it is really too bad that Clarisse does not have ramp presets like Houdini. It would help here a lot.

7:25pm. I am once again confused as to why that multiplication by 5,5,5 was done for the star colors. That just ends up further desaturating them.

7:40pm. Done with lunch. Let me resume.

https://youtu.be/XPGZHhjyTIs?list=PLOZhw3kXDRQelts3VZKzhPySQi2JAofUf&t=279

Let me watch this in its entirety before I start playing around.

https://youtu.be/XPGZHhjyTIs?list=PLOZhw3kXDRQelts3VZKzhPySQi2JAofUf&t=788

I guess I know what the Matte objects are supposed to be used for, but I am a bit confused by the explanation as to why this is done.

I won't bother learning how to separate the rendering of different objects for now. It is not important to me and I can revisit the tutorial in the future if I need to learn. I will set up a full render though.

8:15pm. I really don't feel like doing it right now though. Let me take a look a bit at the spaceship.

Spaceship_obj itself does get textured.

Ah, it has to be named specifically `Spaceship_obj`. It seems that shading layers do per instance shader assignment. This is an interesting discovery.

8:25pm. The esplanade is getting textured, but I am not sure which rule is responsible for that.

Oh, I see it. There is the */esplannade>default in City_SL. There are a bunch of unused material in this.

8:30pm. I've gone over the layout and see that it is completely textured now.

8:35pm. Enough for today. 10+ hours a day is more than enough to be satisfied. I need some downtime. Tomorrow, I am going to add the volumes, the shadow on the planet and its rights and whatever else I've missed and render it out fully.

8:40pm. Let me extract the Gnomon course I got yesterday and move it out of the downloads folder. I'll definitely go through it at some point.

8:45pm. After I deal with the first tutorial though, my priority will be to get rid of the V-Ray shaders from the Houdini pool scene and break it down into individual assets. Maybe I'll be able to just export the whole thing as USD, but in that case, I will have to put some effort into naming things. Right now I have no idea how any of the objects are going to get named. In fact, I have no idea how to even name things. Do I just set the attributes?

Will I be able to do nested scattering in Clarisse?

8:55pm. It seems not. I can't use other scatterers as support geometry.

But that is no problem. What is importing 5300 points from Houdini to me and then instantiating them in Clarisse? It is no problem. Though what about the size attributes?

No, I do not need the size attributes. I do not need to scatter them in Clarisse at all. I can just output all the scattered objects. Since this is USD, the instances should be there for it to see. I can then use rules to apply materials to them.

I need to learn this essential skill. If I can learn to export stuff from Houdini I will have a strong base from which to work from. It will really make those two months spent learning it worth it.

9pm. Yes, no matter what I should not be thinking that I could have saved myself time by going from Blender to Clarisse immediately. I need to keep in mind that Clarisse is meant to be used in conjuction with other 3d software. Where I did go wrong is messing with V-Ray for a third of the month. That was definitely a dead end path.

If I had to pick between paying 500$ a year for Clarisse or V-Ray, I'd pick the former in a heartbeat.

9:05pm. I need just a bit more effort. Lookdev is the most important skill of all in art, but it needs some supporting skills for it to allow me to inovate. The kind of texturing being done in the speceship scene is something I should become capable of doing myself.

I am going to finish the pool scene and then move on to better things."

---
## [noahshaw11/couchdb](https://github.com/noahshaw11/couchdb)@[77f34a1bbc...](https://github.com/noahshaw11/couchdb/commit/77f34a1bbc7c76aefa59777da21e2e76e79f7ec8)
#### Monday 2022-03-14 20:38:20 by Adam Kocoloski

Refactor Jenkins to dynamically generate stages

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

* Defaults to Erlang 23 as the embedded Erlang version in packages. We
  avoid Erlang 24 for now because Clouseau is not currently compatible.

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

* Starts per-stage timer _after_ agent is acquired. Previously builds could
  fail with a 15m timeout when all they did was sit in the build queue.

This is a cherry-pick of 9b6454b with the following modifications:

- Drop the MINIMUM_ERLANG_VERSION to 20
- Drop the packaging ERLANG_VERSION to 23
- Add the weatherreport-test as a build step
- Add ARM and POWER back into the matrix using a new buildx-based
  multi-architecture container image.

---
## [WordPress/gutenberg](https://github.com/WordPress/gutenberg)@[7ea2a0e493...](https://github.com/WordPress/gutenberg/commit/7ea2a0e4936add8adf941ecc95011a960ffca9a3)
#### Monday 2022-03-14 21:27:48 by Dennis Snell

Blocks: Remember raw source block for invalid blocks.

Part of #38922

When the editor is unable to validate a block it should preserve the
broken content in the post and show an accurate representation of that
underlying markup in the absence of being able to interact with it.

Currently when showing a preview of an invalid block in the editor we
attempt to re-generate the save output for a block given the attributes
we originally parsed. This is a flawed approach, however, because by
the nature of being invalid we know that there is a problem with those
attributes as they are.

In this patch we're introducing the `source` attribute on a block which
only exists for invalid blocks at the time of this patch. That `source`
carries the original un-processed data for a block node and can be used
to reconstruct the original markup without using garbage data and without
inadvertently changing it through the series of autofixes, deprecations,
and the like that happen during normal block loading.

The noticable change is in `block-list/block` where we will be showing
that reconstruction rather than the re-generated block content. Previously
it was the case that the preview might represent a corrupted version of the
block or show the block as if emptied of all its content. Now, however,
the preview sould accurately reflect the HTML in the source post even
when it's invalid or unrecognized according to the editor.

Further work should take advantage of the `source` property to provide
a more consistent and trusting experience for working with unrecognized
content.

---
## [rosidae/yaos](https://github.com/rosidae/yaos)@[97b3c13133...](https://github.com/rosidae/yaos/commit/97b3c13133a835b4b2365e61fe15c854e9836fdc)
#### Monday 2022-03-14 21:42:38 by rosidae

its in a boot loop, but its working! i hate my life!

i finally got done building that damn crosscomp or whatever and i installed wsl to use linux (windows is superior for everything but development)

---
## [morgoth1145/advent-of-code](https://github.com/morgoth1145/advent-of-code)@[bdbc1dd2c6...](https://github.com/morgoth1145/advent-of-code/commit/bdbc1dd2c608a9f3aa47335a3f334d402acc9d1d)
#### Monday 2022-03-14 21:58:46 by Patrick Hogg

2018 Day 12 Part 2

Hoo boy. 50 billion iterations pretty clearly screams "I end up in a cycle, find it". The trick was in finding the pattern and figuring out how to code it!

In the end the pattern ended up falling into a cycle that shifts after a while. (I found that it is 100% stable even, just moving to the right each generation. That's probably true for all inputs, but I'm not going to hardcode that.)

The tricky thing here is that with the pattern shifting, the representation needs to change to be the plants and their starting offset, otherwise we can't detect a matching pattern. This took quite a bit to get working, and honestly I don't even remember how much of the slowdown was bugs vs the complexity of managing data. I do know that i hit some bugs though, and I'm super glad that I got the answer for 20k generations the slow way because that let me test my skip-ahead code until I got it right without pinging the server!

Would have missed the leaderboard by 6 minutes and 8 seconds, but that's fine.

Time: 0:33:50.250199

---
## [lowRISC/opentitan](https://github.com/lowRISC/opentitan)@[29b8d2c3e7...](https://github.com/lowRISC/opentitan/commit/29b8d2c3e7fde48a117a31241c508bd4325f5b88)
#### Monday 2022-03-14 22:22:30 by Rupert Swarbrick

[dv,verilator] Make multiple sim_ctrl extensions play nicely

I'd finally got annoyed enough about not being able to pass "-t" in
the middle of a command line to figure out what was going on. It turns
out that by default getopt_long rearranges its arguments to put all
positional args at the end. That's nice, because it allows you code to
easily support stuff like

   my_program -a -b positional0 -c -d positional1

and, post-parse, it will find positional0 and positional1 as the last
two arguments. (If long enough in the tooth, you might remember having
to do "my_program -a -b -c -d positional0 positional1" for some
programs: this is what getopt fixes for us!)

Unfortunately, this behaviour plays havoc when more than one parser
wants to look at argv at once. For example, suppose you have

   my_program --some-args ARG --no-args

and you parse this twice. The first parser understands --no-args and
the second understands --some-args. With the default behaviour and ":"
at the start of the optstring, the first parser will ignore the
unknown --some-args argument and move the positional ARG to the end.
But then the second parser sees

  my_program  --some-args --no-args ARG

and tries to pass "--no-args" as the value to "--some-args". Much
confusion ensues...

Fortunately, we can pass '-' at the start of optstring to disable this
behaviour. The result is harder to parse if you're interested in
positional arguments (which is why this isn't the default behaviour)
but works when you have multiple parsers that have to place nicely
together.

Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

---
## [WordPress/gutenberg](https://github.com/WordPress/gutenberg)@[3ea2d42b0a...](https://github.com/WordPress/gutenberg/commit/3ea2d42b0a6a206663735a47f9796bd42eda2186)
#### Monday 2022-03-14 22:42:34 by Dennis Snell

Blocks: Remember raw source block for invalid blocks. (#38923)

Part of #38922

When the editor is unable to validate a block it should preserve the
broken content in the post and show an accurate representation of that
underlying markup in the absence of being able to interact with it.

Currently when showing a preview of an invalid block in the editor we
attempt to re-generate the save output for a block given the attributes
we originally parsed. This is a flawed approach, however, because by
the nature of being invalid we know that there is a problem with those
attributes as they are.

In this patch we're introducing the `__unstableBlockSource` attribute on 
a block which only exists for invalid blocks at the time of this patch. That 
`__unstableBlockSource` carries the original un-processed data for a block
node and can be used to reconstruct the original markup without using
garbage data and without inadvertently changing it through the series
of autofixes, deprecations, and the like that happen during normal block loading.

The noticable change is in `block-list/block` where we will be showing
that reconstruction rather than the re-generated block content. Previously
it was the case that the preview might represent a corrupted version of the
block or show the block as if emptied of all its content. Now, however,
the preview sould accurately reflect the HTML in the source post even
when it's invalid or unrecognized according to the editor.

Further work should take advantage of the `__unstableBlockSource`
property to provide a more consistent and trusting experience for
working with unrecognized content.

---
## [SuperTemich2005/DDKG2](https://github.com/SuperTemich2005/DDKG2)@[0c9331eece...](https://github.com/SuperTemich2005/DDKG2/commit/0c9331eecec6151c43c81ad6c34dff2b868462b8)
#### Monday 2022-03-14 23:28:35 by SuperTemich2005

drawn one of the photoes using the fucking mouse. stop the war at last

no github fuck you and your hints i want everything to be written in the commit name and you are not going to stop me.

---
## [rowantobias/bucket-webring](https://github.com/rowantobias/bucket-webring)@[81fa1234d9...](https://github.com/rowantobias/bucket-webring/commit/81fa1234d9f99531f8d98d699249e4c00c4e819f)
#### Monday 2022-03-14 23:50:00 by rowan tobias

swiftyshq format fix

i was having errors fsr so i thought removing punctuation etc would fix it. We'll See! (sorry if you got notifs for my other prs that i deleted i was struggling.)

---

