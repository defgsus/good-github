## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2021-12-31](docs/good-messages/2021/2021-12-31.md)


1,421,131 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,421,131 were push events containing 1,869,900 commit messages that amount to 133,714,864 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 31 messages:


## [newstools/2021-the-daily-mavericks](https://github.com/newstools/2021-the-daily-mavericks)@[577260dcb7...](https://github.com/newstools/2021-the-daily-mavericks/commit/577260dcb758ed22a140ebabef48183271d00e49)
#### Friday 2021-12-31 00:13:10 by Billy Einkamerer

Created Text For URL [www.dailymaverick.co.za/article/2021-12-30-reflection-an-unrivalled-life-of-laughter-tears-and-love/]

---
## [skinny85/aws-cdk](https://github.com/skinny85/aws-cdk)@[c071367def...](https://github.com/skinny85/aws-cdk/commit/c071367def4382c630057546c74fa56f00d9294c)
#### Friday 2021-12-31 00:56:54 by Kaizen Conroy

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
## [Bri-ishMan/tgstation](https://github.com/Bri-ishMan/tgstation)@[2cb326c779...](https://github.com/Bri-ishMan/tgstation/commit/2cb326c779486e83a8f59aa441b900f36b3b526d)
#### Friday 2021-12-31 03:21:26 by Iamgoofball

Nerfs the shit out of the felinid tail grab mood buff (#62768)

Mood controls your movespeed. Making Felinids objectively the best mood management race provided your ~~metagame buddy~~friend pulls your tail once every two minutes is insane, even as a meme.

A +5 mood buff was ridiculously good. This is better than the antag mood buff which is 4, equal to the cult buff for sacrificing which is 5, better than tripping balls, better than playing an arcade game and winning, better than the upgraded hug, equal with the best hug, and frankly one of the easiest best mood buffs you can get. And stacks with all the other ones.

---
## [Bri-ishMan/tgstation](https://github.com/Bri-ishMan/tgstation)@[817472a462...](https://github.com/Bri-ishMan/tgstation/commit/817472a462cc02e86b42c85f96d92d49e230a794)
#### Friday 2021-12-31 03:21:26 by Iamgoofball

Nerfs the shit out of the negative sprayed with water mood event for Felinids (#62769)

Mood controls your movespeed. Making Felinids get their movespeed tanked because someone tried to fire extinguisher them is insane. Movespeed is the most important factor in SS13 when it comes to just about everything, it's how we punish people for damage after all.

A -5 mood is insanely punishing. It is equivalent to getting smitten by the gods, worse than a terrible noogie, worse than being bald, worse than literally throwing up all over yourself, worse than losing your family heirloom, and worse than having your eye stabbed out. This sucks for how easy it is to inflict on someone, especially considering the most common method of inflicting this is trying to fire extinguisher someone who's lit themselves on fire.

🆑
balance: Nerfs the felinid water spray moodlet
/🆑

---
## [apache/incubator-doris](https://github.com/apache/incubator-doris)@[ef2ea1806e...](https://github.com/apache/incubator-doris/commit/ef2ea1806e4fb77369ab17a02d20fc8a286be43e)
#### Friday 2021-12-31 03:35:29 by HB

[docs] Improve the chapter on debugging FE in doc.  (#7309)

At present, there are defects in the chapter on debugging FE in doc. My colleagues and I stepped on the pit when 
building the debugging environment, so I want to improve this chapter in combination with my own stepping on the pit 
experience.

The following is my explanation of the changes: 

1. mkdir -p ./thirdparty/installed/bin
explain: When I downloaded versions 0.14 and 0.15, there were no files under thirdparty, so I didn't know whether to 
create it myself or what to do. Finally, I decided to create it myself. I think it's necessary to add instructions here.

2. Add installation thrift@0.13.0 Failed handling method. 
explain: My colleagues and I failed to find the installation package when executing the installation command, and finally 
found a solution on GitHub. Therefore, I added the handling method of the problem to avoid other Mac users from 
getting stuck in this place.

3. Fixed an error in the generated code description.
explain: Before I finished building the code, I debugged FE, and I failed all the time. Idea hints that no files can be found. 
Later, after consulting with morningman in wechat group, it was understood that `mvn install -DskipTests` does not 
need to execute `mvn generate-sources` after execution. This is inconsistent with the description in the document and 
needs to be corrected.

---
## [jws85/ergodox](https://github.com/jws85/ergodox)@[446486897c...](https://github.com/jws85/ergodox/commit/446486897c21fafc59a55b88455e05cdb4413246)
#### Friday 2021-12-31 06:00:23 by J. W. Smith

Configuration that may not murder my wrists

Whew...

Still not 100% on this, but it's already a lot better.

 - Just gave in and realized I need to do layer triggers for some
   things (though bucky bit mods maybe not)...

 - A tiny bit of inspiration hit... holding down func layer and
   mouse layer keys puts you in media keys layer

 - Furthermore got rid of admin layer.  I never used the REISUB
   capability (for all two linux machines that remember that) and
   that basically leaves behind LED brightness and keyboard reset.
   These are great things to put in the 1u thumb cluster keys that
   my hugely huge hands that are totally not the size of one gold
   sharpie obsessed tinpot tyrant, cannot hit ever.  Better yet,
   they're in the func layer.  So I'd have to hold func and push
   the button to reset, which is fine.

 - Bucky bit mods are OSMs so I can arpeggio the keys and not
   hold them down.  So shutting down Emacs (which hopefully I'll
   not be doing much longer :P) is just C, x, C, c.  No holding
   needed.  The tap toggle is 9 to prevent going into bucky bit
   lock which sucks.  It is much less important to be able to
   arpeggio the layer keys, since they are used less.

Things that still need work:

 - Hitting F1-F5 and F11 currently would require contortion, holding
   down func and then hitting 1-5 or t.  Could be fixed by making
   Enter an LT as well.

 - Now that we've got LTs again, we're back to the usual problems.
   Since I shouldn't be chording too much with these keys, the
   biggest one is that holding it down no longer emits many spaces
   or backspaces.  Ah well.

 - Not sure about win/alt placement.  ctl is staying where it is
   though!

---
## [bossbuwi/existence](https://github.com/bossbuwi/existence)@[a6f72a0d78...](https://github.com/bossbuwi/existence/commit/a6f72a0d78a1bd2a12c017a01cd1cac6b6ee87fa)
#### Friday 2021-12-31 06:37:08 by micmanan

Release 0.1-alpha_20211231

Last commit of the year and quite a massive one at that.
Backend for sonata is now mostly working but only for GET and POST on most of the endpoints. PUT and DELETE have not been coded yet. Also, there is a weird behavior regarding the parsing of invalid dates when creating a new event object and needs to be investigated or reworked.
Still, this is quite a milestone and could be the last commit in a while because I can feel that I will be busy this coming days because of work.
Happy new year and may all our dreams come true. Always remember, the world is waiting for you. Godspeed!

---
## [dsonbill/The-Reactor](https://github.com/dsonbill/The-Reactor)@[f47c1e8af2...](https://github.com/dsonbill/The-Reactor/commit/f47c1e8af2a0b029bc22cca3ef2ac54316334ee4)
#### Friday 2021-12-31 07:13:17 by William C. Donaldson

Joh is tryin to steal My System, built both in same world, is doomed to die no matter what

Sorry john, you are no longer a worry
You didn't get tricked, you're just a fucking moron who steals things

---
## [Peppe289/kernel_xiaomi_sdm660](https://github.com/Peppe289/kernel_xiaomi_sdm660)@[bd78e187d8...](https://github.com/Peppe289/kernel_xiaomi_sdm660/commit/bd78e187d84787053cf89ab9c5344dd40c959932)
#### Friday 2021-12-31 07:52:53 by Dave Chiluk

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
Signed-off-by: Ratoriku <a1063021545@gmail.com>
Signed-off-by: Peppe289 <gsperanza204@gmail.com>

---
## [koutsie/xtux](https://github.com/koutsie/xtux)@[333f6e4faa...](https://github.com/koutsie/xtux/commit/333f6e4faa175c1927450d720b5de29390845e02)
#### Friday 2021-12-31 07:53:28 by koutsie

[skip ci] realize how idiotic i am lmao

i should go to sleep.

also i really like github actions, damn?

---
## [Crasher508/PocketMine-MP](https://github.com/Crasher508/PocketMine-MP)@[d9c70cb176...](https://github.com/Crasher508/PocketMine-MP/commit/d9c70cb176c25bd67f7cab384428d6a9165f4539)
#### Friday 2021-12-31 08:56:59 by Dylan K. Taylor

start.cmd: prevent idiotic behaviour when paths contain characters such as brackets
god I hate this shit so much

---
## [wrye-bash/wrye-bash](https://github.com/wrye-bash/wrye-bash)@[248639702a...](https://github.com/wrye-bash/wrye-bash/commit/248639702ac529c27ba5c6664d3307c2fb7cef11)
#### Friday 2021-12-31 11:22:59 by MrD

Merge branch '460-prefix-settings-keys' into dev:

Trickier than it seems merge that adds prefixing to settings keys - those
will need some backwards compatibility code when we hit python 3 as users
updating from older versions will have byte keys that won't be recognized
In Py2 as all those keys are ascii decodable the automatic conversion to
unicode saves us from breaking Bash - b

Also quite a few plain old prefixing - I tried to split this in a logical
way (not per file) in the hoped that we may catch not trivial cases that
we need to revisit in py3. Such cases are:

- chardet returns encoding in bytes so actually the encodings dict and
co should remain bytes - I bet in py3 they are unicode though so except
if we run in some undecodable encoding name we're fine and future proof
- CsvReader goes into pains decoding/encoding/recoding - all this to
handle BOM (which we should not use anywhere anyways - #260)? another one
to revisit in py3

And a general note - I was not so much fun of all this prefixing but it's
the only way to really trace down what should be bytes - also settings
keys were already mixed type, too late to leave them bytes, which is also
not the RightThing - the only reason we may have bytes in here is because
we directly deal with binary files otherwise everything should be unicode

We do *not* want to remove the prefixes in py3 initially - will help with
various stuff - style refactorings, translations and what not - but we
may eventually when the dust settles. So some lines that exceed 79 chars
by one or two chars stayed.

Final reason for merging is that I want to get on with the inspiration
part - this is 101% perspiration here (countless rebases, " vs ', ...)

Thanks @GandaG for initial prefixing!

Under #460.

Signed-off-by: MrD <the.ubik@gmail.com>

Co-authored-by : Daniel Nunes <daniel.henri.nunes@gmail.com>

---
## [wrye-bash/wrye-bash](https://github.com/wrye-bash/wrye-bash)@[5dbda51d33...](https://github.com/wrye-bash/wrye-bash/commit/5dbda51d336325daafe68f8e78db0d7d1869d18a)
#### Friday 2021-12-31 11:22:59 by Infernio

Upgrade to wxPython 4.1

Upgrading for a few reasons:
 - Allows us to drop the PNG optimization step before running a wizard.
   Note that I kept pngcrush around - it's stuck in our history either
   way, so I'd rather put it to use by adding an option for optimizing
   PNGs to BAIN projects.
 - Allows us to add high DPI support (ref #555).
 - Keeping up with breaking wx changes is a good idea (e.g. the
   alignment flags change).
 - wx.ListCtrl (which is probably the most important widget we use) got
   a major rework in 4.1.x by becoming native. It looks quite different
   and we should get testing done to see if anything breaks with it.

Note that 4.1.0 is the last py2 version of wxPython, 4.1.1 is already
py3 only.

wx4.1 build fixes

Whew, adding yet more DLLs to this stupid field...

Fix the hideous white background on wx4.1

These came back from wx2.8 - I guess wx.NullColour was changed?

Add PyMuPDF to requirements.txt

Still completely optional, but recommended since it allows the Doc
Browser to display PDFs as well. The wxPython pdfViewer was broken on
wx4.0, but works fine on wx4.1.

Note: newer versions of PyMuPDF advertise that they are compatible with
py2 on pypi, but 1.18.0 is the last version for which wheels are
available - and manually building this lib is an absolute pain.

Note2: see ugly CI workaround in requirements.txt/setup.py

Closes #553

---
## [well-typed/large-records](https://github.com/well-typed/large-records)@[56c186622c...](https://github.com/well-typed/large-records/commit/56c186622c0932c637611a8fe018770c23730cd4)
#### Friday 2021-12-31 11:51:45 by Edsko de Vries

Start experimenting with sharing

However, this is too much of a pain in the ass. The trees appear in error
messages, and the fact that we cannot reorder fields will lead to a poor user
experience. A plugin would make a lot more sense.

---
## [JBlocklove/dwm](https://github.com/JBlocklove/dwm)@[67d76bdc68...](https://github.com/JBlocklove/dwm/commit/67d76bdc68102df976177de351f65329d8683064)
#### Friday 2021-12-31 12:55:50 by Chris Down

Do not allow focus to drift from fullscreen client via focusstack()

It generally doesn't make much sense to allow focusstack() to navigate
away from the selected fullscreen client, as you can't even see which
client you're selecting behind it.

I have had this up for a while on the wiki as a separate patch[0], but
it seems reasonable to avoid this behaviour in dwm mainline, since I'm
struggling to think of any reason to navigate away from a fullscreen
client other than a mistake.

0: https://dwm.suckless.org/patches/alwaysfullscreen/

---
## [hyenias/ksh93](https://github.com/hyenias/ksh93)@[4491bc6a99...](https://github.com/hyenias/ksh93/commit/4491bc6a991759b61c5f7d49dd0477a2f2bfb1a1)
#### Friday 2021-12-31 13:04:40 by Martijn Dekker

[shp cleanup 00] Reunify the original sh state struct

As observed previously (see 3654ee73, 7e6bbf85, 79d19458), the ksh
93u+ codebase on which we rebased development was in a transition:
AT&T evidently wanted to make it possible to have several shell
interpreter states in the same process, which in theory would have
made it possible to start a complete new shell (not just a
subshell) without forking a new process.

This required transitioning from accessing the 'sh' state struct
directly to accessing it via pointers (usually but not always
called 'shp'), introducing a lot of bug-prone passing around of
those pointers via function arguments and other state structs.

Some of the original 'sh' struct was separated into a 'struct
shared' called 'shgd' a.k.a. 'sh.gd' (global data) instead; these
were global state variables that were going to be shared between
the different main shell environments sharing a process. Yet, for
some reason, that struct was allocated dynamically once at init
time, requiring yet another pointer to access it. <shrug>

None of this ever worked, because that transition was incomplete.
It was much further along in the ksh 93v- beta, but I don't think
it actually worked there either (not very much really did). So,
starting a new shell has always required starting a new process.

So, now that it's clear what they were trying to do, should we try
to make it work? I'm going to go with a firm "no" on that question.

Even non-forking (virtual) subshells, something quite a bit less
ambitious, were already an unmitigated nightmare of bugs. In 93u+m
we fixed a load of bugs related to those, but I'm sure there are
still many left. At the very least there are multiple memory leaks.

I think the ambition to go even further and have complete shells
running separate programs share a process, particularly given the
brittle and buggy state of the existing codebase, is evidence that
the AT&T team, in the final years, had well and truly lost the
ability to think "wait a minute, aren't we in over our heads here,
and why are we doing this again? Is this *actually* a feasible and
useful idea?"

In my view, having entirely separate programs share a process is a
*terrible*, horrible, no-good idea that takes us back to the bad
old days before Unix, when kernels and CPUs were unable to enforce
any memory access restrictions. Programmers are imperfect. If
you're going to run a new program, you need the kernel to enforce
the separation between programs, or you're just asking for memory
corruption and security holes. And that separation is enforced by
starting a new program in a new process. That's what processes are
*for*. And if you need *that* to be radically performance-optimised
then you're probably doing it wrong anyway.

(By the way, I would still argue the same for subshells, even after
we fixed many bugs in virtual subshells. But forking all subshells
would in fact cause many scripts to slow down, and the community
would surely revolt. <sigh>  Maybe I should make it a shell option
instead, so scripts can 'set -o subfork' for reliability.)

It is also unclear how they were going to make something like
'ulimit' work, which can only work in a separate process. There
was no sign of a mechanism to fork a separate program's shell
mid-execution like there is for subshells (sh_subfork()).

Anyway... I had already changed some code here and there to access
the sh state struct directly, but as of this commit I'm beginning
to properly undo this exercise in pointlessness. From now on, we're
exercising pointerlessness instead.

I'll do this in stages to make any problems introduced more
traceable. Stage 0 restores the full 'sh' state struct to its
former static glory and reverts 'shgd' as a separate entity.

src/cmd/ksh93/sh/defs.c,
src/cmd/ksh93/include/defs.h,
src/cmd/ksh93/include/shell.h
src/cmd/ksh93/Mamfile::
- Move 'struct sh_scoped' and 'struct limits' from defs.h to
  shell.h as the sh struct will need their complete definitions.
- Get rid of 'struct shared' (shgd) in defs.h; its members are
  folded back into their original place, the main Shell_t struct
  (sh) in shell.h. There are no name conflicts.
- Get rid of the _SH_PRIVATE macro in defs.h. The members it
  defines are now defined normally in the main Shell_t struct (sh)
  in shell.h.
- To make this possible, move <history.h> and "fault.h" includes
  from defs.h to shell.h and update the Mamfile accordingly.
- Turn sh_getinterp() and shgd into macros that resolve to (&sh).
  This will allow the compiler to optimise out many pointer
  dereferences already.
- Keep extern sh_getinterp() for libshell ABI compatibility.

src/cmd/ksh93/sh/init.c:
- sh_init(): Do not calloc (sh_newof) the sh or shgd structs.
- sh_getinterp(): Keep function for libshell ABI compat.

---
## [Xposed-Modules-Repo/nil.nadph.qnotified](https://github.com/Xposed-Modules-Repo/nil.nadph.qnotified)@[d4f980fcc6...](https://github.com/Xposed-Modules-Repo/nil.nadph.qnotified/commit/d4f980fcc61dc7628ac52a374f90360154f27ee6)
#### Friday 2021-12-31 13:23:41 by qwq233

Release 1.0.0

Before you know it, QNotified has been with you for two years. As humans celebrated the beginning of a new cycle of revolution of a planet in the cantilever of the Milky Way Orion, the QNotified development team decided to release QNotified 1.0.0. This is also the first stable version released by the QNotified project since its establishment.

We also hope to bless all those who follow QNotified and support QNotified to carry on the past, leave the old and welcome the new, and find their own happy life in the new year.Here, on behalf of the QNotified community, we would like to thank all contributors for their efforts and all users.

Signed-off-by: qwq233 <qwq233@qwq2333.top>

---
## [MinArchie/school](https://github.com/MinArchie/school)@[a2aadfa333...](https://github.com/MinArchie/school/commit/a2aadfa3339a9b5ee310ec9e51f03f8392fb3b9d)
#### Friday 2021-12-31 14:19:50 by MinArchie

terrace update

damn 1055 lines of code. damn.
btw, i feel like we can't have the insanity ending in the actual terrace sequence. it's just because what if the player chooses to jump off the roof in the first run-through? does the game just abruptly end? it's kinda weird when you think about it. if you don't like the stay or leave option, then we can take it out, we'll discuss on zoom later.

---
## [jperkin/hubris](https://github.com/jperkin/hubris)@[8e0b13b865...](https://github.com/jperkin/hubris/commit/8e0b13b86564fc7316428943dfe5fde88bb60ef4)
#### Friday 2021-12-31 14:34:43 by Cliff L. Biffle

Remove "standalone" build.

I introduced the standalone build early on as a way of quickly iterating
on a single task, without waiting for an entire image to build -- an
equivalent to `cargo check`. It has proven somewhat useful but also
breaks things.

- The standalone build does not build the actual code you'd ship, it
  instead configures the code in "standalone mode" where a bunch of
  stuff is arbitrarily stubbed out. This means that getting a successful
  standalone build tells you little about the real build.

- You can also _forget_ to put in the standalone magic, in which case
  your actual firmware builds, but then someone else doing a
  "standalone" build later faces a cryptic failure. This is why the
  standalone builds are run in CI -- to avoid this.

- As we introduce increasing levels of configurability in tasks,
  stubbing that configuration out in arbitrary ways is getting harder.
  When it was a matter of conditional compilation driven by board name,
  we could sprinkle in some `feature = "standalone"` hacks to guide it.
  As we move toward task slots and general configuration data in the
  app.toml, the main distinguishing feature of the standalone build --
  that it does not _have_ an app.toml -- starts to become a real pain.

My iteration workflow is currently served by `cargo xtask build`. I am
not aware of any reliable way of getting RLS/rust-analyzer to work on
Hubris, even _with_ the standalone build, so this shouldn't regress
editor support.

---
## [Trilbyspaceclone/sojourn-station](https://github.com/Trilbyspaceclone/sojourn-station)@[66a6e3d75b...](https://github.com/Trilbyspaceclone/sojourn-station/commit/66a6e3d75b1fd8cd72b3b22441443186c71832da)
#### Friday 2021-12-31 15:52:58 by Bones

More Genes then JC Pennies!

bottomless belly given to doggos. Increases max capacity for nutrition to 4 times the amount. good for long journeys if you can fill up. -10%
cat eyes on panthers and cats. Gives increased dark vision. Flashes will wreck your ass. -20%
cold resistance renamed into Thick Fur. Thick fur given to bears and corgis of all kind (protect Ian)  Now gives 10% brute resist along with cold resistance. Gives 10% burn weakness and takes up skin mutation slot - 20% instability.
honk given to geese. Literally just makes you honk like a dork
Echolocation given to bats.  allows you to see without eyes. -40% (If people abuse this with organ insertions I will make it turn your vision fucking black)
screaming given to possoms. Like moo and honk but for those who must scream!
toxin resistance given to snakes and bats. Gives a 10% reduction in toxin damage taken. 20% instability
Balances cowhide to cause 20% instability (Agreed amount with Hex)
Creates MUT_TYPE_EYES to keep from gaining all the eye genes.
Barotrauma gene added to space sharks/great whites. costs 20% instability. Gives pressure resistance.

---
## [schqiushui/android_kernel_oneplus_sm8250](https://github.com/schqiushui/android_kernel_oneplus_sm8250)@[65395f9ef2...](https://github.com/schqiushui/android_kernel_oneplus_sm8250/commit/65395f9ef2a7117299cd52280c2f2a7fe0e3e176)
#### Friday 2021-12-31 15:54:45 by alk3pInjection

disp: msm: Handle dim for udfps

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
## [causal-agent/src](https://github.com/causal-agent/src)@[a0c4c30838...](https://github.com/causal-agent/src/commit/a0c4c308380b2d960e3ac44fdaf560372612f103)
#### Friday 2021-12-31 16:17:03 by June McEnroe

Add The City in the Middle of the Night

Sophie is a fucking idiot jfc. She doesn't even get a redemption
she's just bad all the way to the end.

---
## [DiscPyth/DiscPyth](https://github.com/DiscPyth/DiscPyth)@[785d0dd904...](https://github.com/DiscPyth/DiscPyth/commit/785d0dd9046734fcc274ba667a20a8321f45b020)
#### Friday 2021-12-31 16:54:30 by arHSM

Happy new year
and ofc with a new year i had some new ideas and as you can guess, i made some idiotic changes :evil_laugh:

---
## [jonasnick/secp256k1-zkp](https://github.com/jonasnick/secp256k1-zkp)@[b2206619e6...](https://github.com/jonasnick/secp256k1-zkp/commit/b2206619e69d6d57304e7b4bb0ea5d92ca3b7821)
#### Friday 2021-12-31 16:58:58 by Tim Ruffing

Merge ElementsProject/secp256k1-zkp#131: Replace MuSig(1) module with MuSig2

ac1e36769dda3964f7294319ecb06fb5c414938d musig: turn off multiexponentiation for now (Jonas Nick)
3c79d97bd92ec22cc204ff5a08c9b0e5adda12e6 ci: increase timeout for macOS tasks (Jonas Nick)
22c88815c76e6edb23baf9401f820e1a944c3ecf musig: replace MuSig(1) with MuSig2 (Jonas Nick)

Pull request description:

  The main commit comprises `905 insertions(+), 1253 deletions(-)`. The diff isn't as small as I had hoped, but that's mostly because it was possible to simplify the API quite substantially which required rewriting large parts. Sorry, almost all of the changes are in one big commit which makes the diff very hard to read. Perhaps best to re-review most parts from scratch.

  A few key changes:

  - Obviously no commitment round. No big session struct and no `verifier` sessions. No `signer` struct.
  - There's a new `secnonce` struct that is the output of musig_nonce_gen and derived from a uniformly random session_id32. The derivation can be strengthened by adding whatever session parameters (combined_pk, msg) are available. The nonce function is my ad-hoc construction that allows for these optional inputs. Please have a look at that.
  - The secnonce is made invalid after being used in partial_sign.
  - Adaptor signatures basically work as before, according to https://github.com/ElementsProject/scriptless-scripts/pull/24 (with the exception that they operate on aggregate instead of partial sigs)
  - To avoid making this PR overly complex I did not consider how this implementation interacts with nested-MuSig, sign-to-contract, and antiklepto.
  - Testing should be close to complete. There's no reachable line or branch that isn't exercised by the tests.
  - [x] ~In the current implementation when a signer sends an invalid nonce (i.e. some garbage that can't be mapped to a group element), it is ignored when combining nonces. Only after receiving the signers partial signature and running `partial_sig_verify` will we notice that the signer misbehaved. The reason for this is that 1) this makes the API simpler and 2) malicious peers don't gain any additional powers because they can always interrupt the protocol by refusing to sign. However, this is up for discussion.~ EDIT: this is not the case anymore since invalid nonces are rejected when they're parsed.
  - [x] ~For every partial signature we verify we have to parse the pubnonce (two compressed points), despite having parsed it in `process_nonces` already. This is not great. `process_nonces` could optionally output the array of parsed pubnonces.~ EDIT: fixed by having a dedicated type for nonces.
  - [x] ~I left `src/modules/musig/musig.md` unchanged for now. Perhaps we should merge it with the `musig-spec`~ EDIT: musig.md is updated
  - [x] partial verification should use multiexp to compute `R1 + b*R2 + c*P`, but this can be done in a separate PR
  - [x] renaming wishlist
      - pre_session -> keyagg_cache (because there is no session anymore)
      - pubkey_combine, nonce_combine, partial_sig_combine -> pubkey_agg, nonce_agg, partial_sig_agg (shorter, matches terminology in musig2)
      - musig_session_init -> musig_start (shorter, simpler) or [musig_generate_nonce](https://github.com/ElementsProject/secp256k1-zkp/pull/131#discussion_r654190890) or musig_prepare
      - musig_partial_signature to musig_partial_sig (shorter)
  - [x] perhaps remove pubnonces and n_pubnonces argument from process_nonces (and then also add a opaque type for the combined nonce?)
  - [x] write the `combined_pubkey` into the `pre_session` struct (as suggested [below](https://github.com/ElementsProject/secp256k1-zkp/pull/131#issuecomment-866904975): then 1) session_init and process_nonces don't need a combined_pk argument (and there can't be mix up between tweaked and untweaked keys) and 2) pubkey_tweak doesn't need an input_pubkey and the output_pubkey can be written directly into the pre_session (reducing frustration such as Replace MuSig(1) module with MuSig2 #131 (comment))
  - [x] perhaps allow adapting both partial sigs (`partial_sig` struct) and aggregate partial sigs (64 raw bytes) as suggested [below](https://github.com/ElementsProject/secp256k1-zkp/pull/131#issuecomment-867281531).

  Based on #120.

ACKs for top commit:
  robot-dreams:
    ACK ac1e36769dda3964f7294319ecb06fb5c414938d
  real-or-random:
    ACK ac1e36769dda3964f7294319ecb06fb5c414938d

Tree-SHA512: 916b42811aa5c00649cfb923d2002422c338106a6936a01253ba693015a242f21f7f7b4cce60d5ab5764a129926c6fd6676977c69c9e6e0aedc51b308ac6578d

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[28bd09a0f4...](https://github.com/mrakgr/The-Spiral-Language/commit/28bd09a0f4bcf52f703525f8d61bb6966d886363)
#### Friday 2021-12-31 17:05:05 by Marko Grdinić

"9:05am. I got up at this time, but I must have woken up a few hours ago. The problem is that the winter has let up, but the heating hasn't so I am getting cooked under my covers. I guess this is one way of adjusting my schedule.

Let me play a bit with blending modes and then I will resume the review.

9:50am. I had some ideas and had to test them. The result is that the color mode is amazing. I could slap on a bit of grayscale and then use the color mode to paint. There are so many of these quirky blending modes here that I do not know how to use, but color and brightness blending modes seem like they could be extremely useful.

I see people using multiply and color dodge, and it always felt quirky and unprincipled, but these two especially in conjuction with gradient maps could be extremely useful.

Still, it is not that simple.

What I have in mind would ignore the edges.

Let me take a look at that orc image again.

https://boards.4chan.org/ic/thread/5815109#p5815591
> Oh, Dave Rapoza did a 16 hour tutorial how he paints pic related. Might wanna check this out as well to learn some digital painting techniques

It is an really interesting orc face portrait.

10am. Huh, now that I look at it again, I see that it is not like what I remembered. I am looking at it carefully, and I can't find any particular shifts in hue. For some reason, in my memory that was the opposite, and I was agonizing over the night how I would deal with that, but I see that I should not have worried.

In general, real life surfaces have an uniform color and are separated by edges. What I had in mind of using a color layer to add interest would violate the edge assumption, so I should not use it.

Gradient maps should be good for everything, though I suppose color layers could do if I wanted to do paint tatoos. Hmmm...

No, tatoos are an overlay. I'd be better off using the underlay as a brightness layer in that case.

10:15am. No, no, I am thinking about this wrong. Either way is fine and the two modes are bijections. White color in nature won't actually be white, but gray. I am just getting fooled by my own reasoning about what the perception should be. The way the program does things is right.

10:25am. I've been wondering about how to reverse colors and I see there is something called the reverse gradient.

10:35am. CSP has something called fill layers. That would have been better to use as a paper substitute than a filled raster layer. Using many layers is bound to take a lot of memory.

10:40am. Things are coming to me. I was never really sure how to think about saturation, but now that I've played with the color layer I see that I can think about it as just the percentage to which the brightness is moved to a specific color.

Color and brightness are the two main factors. That is the way to think about them.

I actually hadn't understood this way of thinking about color. If I had I would not have gottne confused with all those layers. I'd have known at once about the importance of the last two layers and the gradient map.

10:45am. It is good to spend time every once in a while dwelling on basic principles.

I've been getting taught things incorrectly by some of the Youtube tutorials. Remember those times where I watched how to do shading and how they would just go through the modes and I would not get it? Or how they would lay down a bunch of flats and then start shading afterward?. That is absolutely wrong.

You need to be thinking about brightness from the start. While working on the picture that is how I was thinking about it as it was easier, but now I can actually verbalize this.

Furthermore, the color wheel is tricking me about what the brightness is. When I set the gradient map, I interpolated between pure black -> color -> pure white. That is the right way to think about it. That is also how the color and the brightness modes work.

But on the color picker brightness is a separate thing from saturation and even with 0 brightness you can get a solid color. Instead the way to think about brightness should be to take both the horizontal and the vertical. Hmmm...

11am. You can take a fill layer, and set it to a color mode. That is one alternative to a linear gradient map.

Without a doubt, that is the way to think. I guess all those color ramp examples in Blender really carved it into me, the right way to think about color.

The explicit lessons were all wrong.

Even if I took the usual approach to shading, I should be doing it with a brightness layer, not anything else.

11:05am. In the end, I did it all correctly. Even without the prompting from others, I found the correct way simply by optimizing my process.

Ok, let me close CSP.

I feel like I've gained a lot. This way of thinking is quite powerful. With this I have a most essential tool at my disposal.

Now that I've ranted a bit, I should focus on the review. Let me take a short break first. Let me also put the Revue Starlight movie on download.

11:35am. Actually, before I start let me just check if a fill layer in color mode also has the same problems with transparency as grad map does.

11:40am. Not the same kind of problem, what it has trouble with instead is that it colors the transparent pixels as well. So it makes no difference if you use a fill normal + raster brightness or raster normal + fill color. It ends up being the same kind of combo.

For maximum flexibility, maybe raster normal + raster brightness would be the best way of working, in other words, the usual method of laying down flats and then doing shading based on that.

Let me focus on the review. I woke up at 7am, and I still haven't done a thing. Instead I am just adding entries to this journal.

Still, I can't deny that the effect of finishing that picture successfully had a powerful effect on me. I am the happiest I've been in a long while. I can actually see myself becoming good at art in the future.

///

In the last review, I was in a middle of a heated battle. I though with just a push I'd be able to make the other side crumble. Bullets were blazing, but expected I would be able to push through because surely something like training a poker should be doable given how near the Singularity is. What happened that in the frenzy of battle I lost track of ammo and when I went to reload, I found my satchel empty. And the enemy which was on the verge of defeat got a fresh batch of reinforcements, ready to open fire.

I suffered a lot of mental damage when I threw in the towel back in September, and just about now my sanity points have recevered to a reasonable level. To think that in the last post I thought I was only a few weeks away from getting the agent to work.

There is no getting the poker agent plan to work with my current level of hardware. None.

The neural net methods I had worked just fine on toy games like Leduc and even Flop poker, but pretty much everything I've tried just dies on Holdem. The only thing that worked for me was increasing the batch size by 10x to 5k, but that slows down the already very slow training to an unbearable degree. The realization that I do not have the computational power to fulfil my goal made me extremely obsessed about AI chips, to the point I actually considered getting a job for the first time, just to get the chip. During my bouts of normality, I did spent time making a resume and applying. One time I even got an offer, but it was so poor that I gave up in disgust. Maybe I shouldn't as it would have been enough to get the chip, but I honestly felt the other party was mocking me with how the negotiation went. I do not regret aborting it. Plenty of places list salary ranges and I should have stuck to those when applying.

The tech job market is such a shitshow, the reject rates make it impossible to pick something you'd like to work on, instead if you are really serious, you have to pick whatever you get. You can either focus on maximizing your salary or picking work that is meaningful.

To continue on the path of developing my external cortex I need the bare minimum of money to buy one of the Grayskull chips from TensTorrent. They cost 1-2k might not be much depending on where you live, but I have no way of getting that amount without doing paid labor. This pisses me off because I was supposed to make money of poker to make those chips in the first place. For the first time, I've felt that the path I am on is particularly weak. It is just sending me hurdles, but it is not sustaining me wit resources to keep pursuing it. It was one thing when my goal was just to make a language and a ML library, but now I need the world to cooperate.

This situation made me reflect upon my approach, and got me thinking. It is one thing try to get to human or even animal level, but I was so sure that CPU+GPU should be enough for toy games, which I'd say poker falls into. I did not expect it to get to superhuman level even there, but I wasn't prepared for the amount of struggle the crappy current day algorithms would have to endure. At this point I can only ask: if CPU+GPU aren't enough, just how sure am I that getting an AI chip would help? I mean, by porting the game directly to chip and parallelizing the training, I could get 100x performance improvements most likely. That would be enough to cover the increases in batch size necessary to do training. That is obviously right.

But what then? Past poker I'd need to scale again and run into the same again. A single chip is not going to cut it on Dota or Starcraft. Unlike Deepmind even if I had the money, I can't just open my wallet every time I run into problem. I actually want to make money off RL, not go deeply into the red for sake of research.

At the start of the year, I forcefully quashed my skepticism towards deep learning and gradient based methods, but I think my initial impression was right after all.

If I am going to succeed, I need better algorithms. Backprop was the only choice I had so I had to go with it, but that was a mistake.

It is not like I wasn't skeptical from the start. I spent a lot of time in 2018 stuying higher order optimizers. In 2019 I actually studied formal math. And this year I gave it my best shot at coming up with my own ideas. But ultimately I was always walking down a straight and sparsely lighted path called backprop. I knew deep down that it won't get me to the place I want to go. I looked around and saw only the dark wilderness and though that the place I desire must be there, but I dared not venture off path. I hoped that once I reached the endpoint of backprop that it would give me some kind inspiration, the light necessary to venture out into the wilderness.

I was timid, very much so, but the wilderness was very vast and imposing. At the end of the path, there was no light of inspiration waiting for me, and I realize that there is no choice - if I want to win I need to venture into the wilderness to find the place that I seek.

In concrete terms what this means, now that I've accepted the above, is that I should have the hardware itself tell me what algorithm to use on it.

I need to revisit the past, meet up with some relatives of modern deep learning and make the nature's way my own.

It is not like I wasn't aware of evolutionary algorithms, and specifically genetic programming all this time, it is just that it would have been absurd to even attempt to use them on the CPU + GPU combo. I can barely train a single network, let alone try to synthesize random combinations of them. The problem is that on the tasks that NNs work for me, they work quite well, but on the tasks they don't like Holdem I do not have enough computational power to train even a single net. So I wasn't really considering it, but the way AI development is currently going is the worst.

The ML community is as useless as I am at discovering novel algorithms, and the sheer quantity of useless research being published is actually a negative that could hide useful leads from being pursued. The reason for that is that is because all the research is concentrated in hacking backprop and nobody knows how to go beyond it. There are people with more resources and accumen than me out there, but as far as I can see I cannot trust them to lead the way anymore than I can myself.

The way I've been trying to learn ML is wrong.

A key idea to focus on is that if somebody, some oracle could give us the optimal algorithms for games of our chosing that would be extremely enlightening. Right now, I just can't draw out the right conclussion on what learning is from the depths of my subconscious, but if I was given the program containing the answer, I could study and eventually understand it. That would be the right way to improve. My ML skills would explode all the way to where I could cause the Singularity.

The ML community and random geniuses have had plenty of time to emerge, and since that has not happened, it is reasonable to assume that is not going to happen. It is just praying for a miracle at this point. Right now, rather than the ML community leading the way, it feels more like it has taken its development hostage.

The notion that ML researchers are to actual AI development what gamers are to deep learning development is an extreme view which is why I had no seriously considered it up to now. But surprisingly it meshes well with the story pushed by the gurus of ML that hardware is the primary driver, it just doesn't imply that NNs are the way forward.

When I tossed in the towel and became obsessed with AI chips, I knew they were CPU/GPU hybrids with local memory. Since they don't have the same restrictions as GPUs, implementing a game directly on them and cutting off the friction from transfering data back and forth between the CPU and GPU could lead to large gains. But in a similar fashion, what should be possible to implement on them are interpreters with which to enact genetic programming and attempt to synthesize learning algorithms. I realized it would be good for games and ML libraries, but what I see now that this is what Spiral's true purpose is.

Because it would be so dependent on PL skills, I am probably near the very top of all the people in the world who could attempt to create genetic programming system on an AI chip.

Imagine an average ML researcher trying to do this. First of all, he'd need to warm up on programming in C. Some companies like Groq do not even have a C backend, but go directly to assembly. Maybe a simple game like poker would be doable with effort. But trying to do an interpreter in C would be quite rough. He'd probably do the simplest possible thing of using a flattened representation and call it a day if and probably when it failed. That is no way to do things.

But the altenrative of making a functional programming language in which to do this research in would take him years of work. I am guessing it would be hard to go down this route even at large ML research organizations. I could make a backend for any AI chip in a week and then quickly make such a system after that.

I think this path is definitely a viable way of getting the superior learning algorithms, but an uknown factor to me is whether it would take a single AI chips or a cluster of a 100 or a 1000 of them. And anyway, I do not have the money to buy even one right now.

For Spiral, I've tried looking for sponsors and applying at random companies in hopes of getting them to sponsor some of that work, but I haven't had much luck. Back then I was monofocused, so I could not see it, but instead of hollering out the window of various companies hoping somebody takes notice, the optimal strategy here is to do [something similar](https://www.reddit.com/r/Tenstorrent/comments/rhtuxn/seeking_a_sponsor_for_a_functional_programming/) to taking out an ad. Despite the great benefits Spiral could give to these companies, right now it is just too easy for my application to get junked, but looking into the future, some of the companies will have a community of people using these chips. In the case that I can't get the companies making the chips interested in this, the people actually programming them should be interested.

Most likely, the CEO will look at their social media page and think about my post at some point. Or somebody other high up in the company. Right now, these are the early days of the new hardware wave and nobody is using them. Most companies are focused on the big players and very few companies actually understand the vital role of fostering a software ecosystem. Obviously the reason computers have been so successful is because ordinary people can buy the hardware and make use of it rather than just the big companies. The successful companies in this wave will have a community surrounding them, and from that I will have a pool of potential sponsors if the company itself is not interested.

So I won't worry about the future of Spiral, and just let those posts squat on their social media pages. At some point I should get feedback on it.

Doing unpaid work for the last 7 years has been hard on me, and I do not want to go through the same thing again. Right now my main priority is money. My programming skills are at the apex-of-humanity level, so I could get a job doing that, but I absolutely detest doing random things for random people, so I do not want to go down that route. As hard as it was, a part of me like pursing my own path for the past 7 years. I had a vision and I went after it, that is how life should be lived. I cultivated a lot of skills along the way as well as a work ethic. I am not hard working at laziness like I was during my trading days. I am just hard working.

And if I have to compromise and do things for money, it should be doing things that I want.

I have programming skills, but no interest in programming anything in particular at the moment. I thought that I could make a game, but the problem is that even if wanted to do that I have no way of making art for it. So why not cultivate that particular skill? I had essentially the same problem in 2014 when I wanted to publish Simulacrum, but did not have money to pay an editor or a artist to do the cover. Not having the minimum funds to either do trading, publish a story or now pursue AI seems to be a constant theme throughout my life.

Since the only thing I ever cared about is my Singularity obsession, I am going to start a new arc of Simulacrum. The last time I did it in 2014, it was less of a story, and more like a device to see if I can convince myself of iterative suicide as a method of self improvement. It was a declaration of victory, a proof that I finally understood what it takes to reach true power. But it also revealed to me that I did not understand AI, so I went on this path to find out. Eventually I will come back to finish what I started.

But right now, I want to take a break from programming.

Unlike in 2014, I do not want to just sit here and churn out piles of text. The problem is that anybody with a brain can do that, so I whatever I put out is going to be buried under piles of other works. Even if I made the best work in the world, there is only so much attention to go around. Without a hook I'll be overlooked. What I need is good art to catch the attention and set the mood. Good art is something you can be proud about. My goal will be to make then next arc a visual novel.

Right now that is what I am studying. You can see my progress after [3 months here](TODO), it is not bad for my third piece. The first two were just a pencil drawing of a watering can, and a loose sketch of a hand. Back in school I was crappy at it, but now that I am taking it seriously I feel that I am internalizing it. At the moment I still have to learn more Blender, and do more works to make the studies stick, but after that I'll be ready to make art for Heaven's Key. Right now the goal is get to a level where I can produce quality pieces consistently and learn the tools of the trade. Speed, and most of my skill as an artist will come during the work Heaven's Key where I will be exercising it consistently. Creativity is ultimately an exercise in quality, and repetition in velocity.

After I bring up my art skills, I'll want to do music next, so I'll change my study targets. This will take me a while, in the meantime, I'll be posting study pieces periodically on my Twitter handle. I do not know how long all this will take me, but when I am ready to start Heaven's Key I'll set something up. The patrons will get material in advance. When I am done with an episode I'll package it up and sell it in an app store. That is the way go here.

Making money isn't that complicated, and I am not looking to make more than to simply upgrade my rig and get an AI chip.

Of course, I could make far more money, far faster by simply getting a job, but where would the fun in that be? If Simulacrum gets popular and starting inspiring people to pursue power through AI it could only be good for them. It would be absolutely horrible for the world and humanity though, but who cares about humans? At some point you'll learn to enjoy their suffering. Doing visual novels is a waste of my programming skills, and if I could evolve a proper memory system, I'd seriously consider making a real game. Improved learning algorithms for machines could allow me to make significant gamemplay innovations. That is for the future.

Even if the today is hard and tedious at times, I am enjoying improving my art skills. So far, the learning trajectory for art has been no different from the programming one. I'll do what I can in the present and leave the rest for the future.

///

I pasted the yesterday's work here, but now how do I take it from here?

1:25pm. Let me get breakfast.

2:40pm. Done with chores. Let me chill and I will resume.

3:15pm. Let me resume.

5:35pm. Had to leave for lunch. I'll close for the day here. I'll proofread the above tomorrow and well as post my piece on Twitter.

Actually, I feel like going for a bit further. Let me watch some Blender physics videos. I have to up those particular skills just a bit.

5:50pm. Focus me. Watch that video. I've been daydreaming since I first became conscious today. I want to get back to the grind. There are things I have to do, but what I want to do is watch more Blender tutorials. I need to get back to that hell.

https://www.youtube.com/results?search_query=blender+physics

No. I want to watch these, but mind is stretched to its limit right now. It would have been one thing if I had gotten a proper night of sleep and started at the usual time, but now I just want to do my own thing. I want to take a bath as well, so let me do that.

Usually when I sleep poorly I sleep well the next day, so tomorrow when I am fresh, I'll proofread the above, post the artwork on twitter, post a very shortish review on the PL sub, and then dive into these videos. Then I will do more stuff in Blender. Railings, pool, training room, Luna...

I want to do more painting as well. I feel like I could get better and want to challenge myself.

But I am going to have to be patient yet again and give Blender its proper time. I need to develop the environment which to paint.

I need to keep pushing. If I could cover just a bit more of Blender's features, I will have fairly strong skills in 3d modeling by the end of it. And that will serve as a basis for a lot of things. I'll need a few months at most to bring it all together, and then instead of constantly studying, I'll actually be able to have fun with this."

---
## [TeamDeusVult/MagnesiumExtras](https://github.com/TeamDeusVult/MagnesiumExtras)@[fe87a2c9bc...](https://github.com/TeamDeusVult/MagnesiumExtras/commit/fe87a2c9bc1b32525a837600d1fb26e65892810b)
#### Friday 2021-12-31 18:26:03 by Vice

actually change the mod version again fucking hell why is this so hard to remember

---
## [Yoshubs/FNF-PsychEngine](https://github.com/Yoshubs/FNF-PsychEngine)@[86a44f5f1f...](https://github.com/Yoshubs/FNF-PsychEngine/commit/86a44f5f1fe53b8c08d310aeff47e3c636e4bfe4)
#### Friday 2021-12-31 18:53:14 by ShadowMario

Fixed dumb stupid ass mistake

Jesus fuck i think i lost half of my braincells, now i only have a quarter left

---
## [jdoleary/WebsocketPie](https://github.com/jdoleary/WebsocketPie)@[5de4dfc1dc...](https://github.com/jdoleary/WebsocketPie/commit/5de4dfc1dc5474a5c7496bf7b548a2ffa72ecb53)
#### Friday 2021-12-31 18:56:20 by Jordan O'Leary

ref: Merge MakeRoom and JoinRoom

After spending some time using PieClient, I've found that it
is annoying having to constantly rewrite the logic on the
client side for checking if a room already exists, hosting it
if not, and ultimately joining.  This has to be done in more places
than I expected, for example, rejoining a server if it crashes
and reboots.

This changes makes it so that JoinRoom can create the room
if the room doesn't already exist, however this is not the default
behavior because it can be important for a client to know that
a room doesn't exist when trying to join it.  For example, if I'm
trying to join a friends room, but I mistype it, it would be a
bad user experience for it to put me in another second room that
is different from my friends room.  The desireable experience
is for it to say "this room doesn't exist" so I can figure out
that I mistyped it.

So by default it will give an error message if the room doesn't
exist, but this commit adds the makeRoomIfNonExistant boolean
as a convenience for the many places where the developer just
wants to put the client in the room, regardless of whether it
exists or not.

---
## [seamoosea/WizardBrawl](https://github.com/seamoosea/WizardBrawl)@[9ba2f2a2cb...](https://github.com/seamoosea/WizardBrawl/commit/9ba2f2a2cbd193beccf846e2fba33d1f75c896f5)
#### Friday 2021-12-31 19:17:13 by Seamus

Fixed GAS to work in BPs. Didn't clean code tho.
Fuck you GAS you little shit, I win.

---
## [marioalexis84/FreeCAD](https://github.com/marioalexis84/FreeCAD)@[92e6094449...](https://github.com/marioalexis84/FreeCAD/commit/92e6094449275e89e6ffd7a74c32e3ce3c62c1e6)
#### Friday 2021-12-31 21:21:35 by Abdullah Tahiri

Sketcher: EditModeCoinManager/DrawSkechHandler refactoring

======================================================

Creation of EditModeCoinManager class and helpers.

In a nutshell:
- EditModeCoinManager gets most of the content of struct EditData
- Drawing is partly outsourced to EditModeCoinManager
- EditModeCoinManager gets a nested Observer class to deal with parameters
- A struct DrawingParameters is created to store all parameters used for drawing
- EditModeCoinManager assume responsibility for determining the drawing size of the Axes
- Preselection detection responsibility is moved to EditModeCoinManager.
- Generation of constraint nodes and constraint drawing is moved to EditModeCoinManager.
- Constraint generation parameters are refactored into ConstraintParameters.
- Text rendering functions are moved to EditModeCoinManager.
- Move HDPI resolution responsibility from VPSketch to EditModeCoinManager
- Move responsibility to create the scenograph for edit mode to EditModeCoinManager
- Move full updateColor responsibility to EditModeCoinManager
- Allows for mapping N logical layers (LayerId of GeometryFacade) to M coin Layers (M<N). This
is convenient as, unless the representation must be different, there is no point in creating coin
layers (overhead).

Refactoring of geometry drawing:
- Determination of the curve values to draw are outsourced to OCC (SRP and remove code duplications).
- Refactor specific drawing of each geometry type into a single template method, based on classes of geometry.
- Drawing of geometry and constraints made agnostic of scale factors of BSpline weights so that a uniform treatment can be provided.

Refactoring of Overlay Layer:
- A new class EditModeInformationOverlayConverter is a full rewrite of the previous overlay routines.

ViewProviderSketch:
- Major cleanup due to migration of functionalities to EditModeCoinManager
- Reduce public api of ViewProviderSketch due to refactor of DrawSketchHandler
- Major addition of documentation
- ShortcutListener implementation using new ViewProvider Attorney
- Gets a parameter handling nested class to handle all parameters (observer)
- Move rubberband to smart pointer
- Refactor selection and preselection into nested classes
- Removal of SEL_PARAMS macro. This macro was making the code unreadable as it "captured" a local stringstream that appeared unused. Substituted by local private member functions.
- Remove EditData
- Improve documentation
- Refactor Preselection struct to remove magical numbers
- Refactor Selection mechanism to remove hacks

ViewProviderSketchDrawSketchHandlerAttorney:
- new Attorney to limit access to ViewProviderSketch and reduce its public interface
- In order to enforce a certain degree of encapsulation and promote a not too tight coupling, while still allowing well
defined collaboration, DrawSketchHandler accesses ViewProviderSketch via this Attorney class.
-DrawSketchHandler has the responsibility of drawing edit temporal curves and markers necessary to enable visual feedback
to the user, as well as the UI interaction during such edits. This is its exclusive responsibility under the Single
Responsibility Principle.
- A plethora of speciliased handlers derive from DrawSketchHandler for each specialised editing (see for example all the
handlers for creation of new geometry). These derived classes do * not * have direct access to the
ViewProviderSketchDrawSketchHandlerAttorney. This is intentional to keep coupling under control. However, generic
functionality requiring access to the Attorney can be implemented in DrawSketchHandler and used from its derived classes
by virtue of the inheritance. This promotes a concentrating the coupling in a single point (and code reuse).

EditModeCoinManager:
- Refactor of updateConstraintColor
- Multifield - new struct to identify a single element in a multifield field per layer
- Move geometry management to delegate class EditModeCoinGeometryManager
- Remove refactored code that was never used in the original ViewProviderSketch.

CommandSketcherBSpline:
- EditModeCoinManager automatically tracks parameter change and triggers the necessary redraw, rendering an explicit redraw obsolete and unnecessary.

Rebase on top of master:
- Commits added to master to ViewProviderSketch applied to EditModeCoinManager.
- Memory leaks - wmayer
- Constraint Diameter Symbol - OpenBrain
- Minor bugfix to display angle constraints - syres

Architecture Description
=======================

* Encapsulation and collaboration - restricting friendship - reducing public interface

Summary:
- DrawSketchHandler to ViewProviderSketch friendship regulated via attorney.
- ShortcutListener to ViewProviderSketch friendship regulated via attorney.
- EditModeCoinManager (new class) to ViewProviderSketch friendship regulated via attorney.
- ViewProviderSketch public interface is heavily reduced.

In further detail:
While access from ViewProviderSketch to other classes is regulated via their public interface, DrawSketchHandler, ShortcutListener and EditCoinManager (new class) access
to ViewProviderSketch non-public interface via attorneys. Previously, it was an unrestricted access (friend classes). Now this interface is restricted and regulated via attorneys.
This increases the encapsulation of ViewProviderSketch, reduces the coupling between classes and promotes an ordered growth. This I call the "collaboration interface".

At the same time, ViewProviderSketch substantially reduces its public interface. Access from Command draw handlers (deriving from DrawSketchHandler) is intended to be restricted to
the functionality exposed by DrawSketchHandler to its derived classes. However, this is still only partly enforced to keep the refactoring within limits. A further refactoring of
DrawSketchHandler and derivatives is for future discussion.

* Complexity and delegation

Summary:
- Complexity of coin node management is dealt with by delegation to helper classes and specialised objects.

In further detail:

ViewProviderSketch is halved in terms of code size. Higher level ViewProviderSketch functions remain

* Automatic update of parameters - Parameter observer nested classes

Summary:
- ViewProviderSketch and CoinManager get their own observer nested classes to monitor the parameters relevant to them and automatically update on change.

The split enables that each class deals only with parameters within their own responsibilities, effectively isolating the specifics and decoupling the implementations. It is
more convenient as there is no need to leave edit mode to update parameters. It is more compact as it leverages core code.

More information:
https://forum.freecadweb.org/viewtopic.php?p=553257#p553257

---
## [Alexandah/mOuSe_prototype](https://github.com/Alexandah/mOuSe_prototype)@[bf1a8ee721...](https://github.com/Alexandah/mOuSe_prototype/commit/bf1a8ee721c27d71c197b1054cc78cbf0e89927d)
#### Friday 2021-12-31 21:55:20 by Alexander Davis

added very basic test code to confirm that moving windows with keyboard events works easily. it does. fuck you react!

---

