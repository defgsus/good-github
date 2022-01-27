## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-01-26](docs/good-messages/2022/2022-01-26.md)


1,747,081 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,747,081 were push events containing 2,775,160 commit messages that amount to 216,644,910 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 44 messages:


## [Shadow-Quill/tgstation](https://github.com/Shadow-Quill/tgstation)@[8f32cbe38d...](https://github.com/Shadow-Quill/tgstation/commit/8f32cbe38d956e06c919be36386da76befb0555b)
#### Wednesday 2022-01-26 00:19:08 by LemonInTheDark

Reworks janitor cyborg cleaning, focus on the slipping (#64131)

Alt of #64105 and #64126 (I'm sorry Novva, I should have said something earlier)
I main janitor. As a janitor main, my greatest joy in life is slipping people who ignore my signs

I've seen some people complain about janitor borgs, so I decided to look into em

Unfortunately, not only is the janitor borg just a straight upgrade to janitors, it has absolutely no reason to use most of its kit
We give it standard cleaning supplies, and hell even bespoke tools to deal with leaving slippery tiles everywhere, but we also just let them clean anything they can walk over

This seems a bit too much to me, even for borgs. Also it's like, really boring

So what if we made their movement based cleaning cost something? How about we make it suck water from their bucket. Use the same pattern as mop code, make it twice as expensive though. Give it a slowdown, some sound cues, and an action button to trigger it all

---
## [RTEMS/gnu-mirror-gcc](https://github.com/RTEMS/gnu-mirror-gcc)@[aeac414923...](https://github.com/RTEMS/gnu-mirror-gcc/commit/aeac414923aa1e87986c7fc6f9b921d89a9b86cf)
#### Wednesday 2022-01-26 00:23:49 by Thomas Schwinge

Revert "Fix PR 67102: Add libstdc++ dependancy to libffi" [PR67102]

This reverts commit db1a65d9364fe72c2fff65fb2dec051728b6f3fa.

On 2021-09-17T01:01:39-0700, Andrew Pinski via Gcc-patches <gcc-patches@gcc.gnu.org> wrote:
> On Fri, Sep 17, 2021 at 12:46 AM Thomas Schwinge <thomas@codesourcery.com> wrote:
>> On 2021-09-15T13:56:37-0700, apinski--- via Gcc-patches <gcc-patches@gcc.gnu.org> wrote:
>> > The error message is obvious -funconfigured-libstdc++-v3 is used
>> > on the g++ command line.  So we just add the dependancy.
>>
>> > --- a/Makefile.def
>> > +++ b/Makefile.def
>> > @@ -592,6 +592,7 @@ dependencies = { module=configure-target-fastjar; on=configure-target-zlib; };
>> >  dependencies = { module=all-target-fastjar; on=all-target-zlib; };
>> >  dependencies = { module=configure-target-libgo; on=configure-target-libffi; };
>> >  dependencies = { module=configure-target-libgo; on=all-target-libstdc++-v3; };
>> > +dependencies = { module=configure-target-libffi; on=all-target-libstdc++-v3; };
>> >  dependencies = { module=all-target-libgo; on=all-target-libbacktrace; };
>> >  dependencies = { module=all-target-libgo; on=all-target-libffi; };
>> >  dependencies = { module=all-target-libgo; on=all-target-libatomic; };
>>
>> I'm confused, because given that this 'Makefile.def' change only has the
>> following effect:
>>
>> > --- a/Makefile.in
>> > +++ b/Makefile.in
>> > @@ -61261,6 +61261,7 @@ all-bison: maybe-all-intl
>> >  all-flex: maybe-all-intl
>> >  all-m4: maybe-all-intl
>> >  configure-target-libgo: maybe-all-target-libstdc++-v3
>> > +configure-target-libffi: maybe-all-target-libstdc++-v3
>> >  configure-target-liboffloadmic: maybe-configure-target-libgomp
>> >  all-target-liboffloadmic: maybe-all-target-libgomp
>> >  configure-target-newlib: maybe-all-binutils
>>
>> ... isn't that actually a no-op, because we already had such a dependency
>> listed?  Now twice:
>>
>>     $ grep -n -F 'configure-target-libffi: maybe-all-target-libstdc++-v3' -- Makefile.in
>>     61264:configure-target-libffi: maybe-all-target-libstdc++-v3
>>     61372:configure-target-libffi: maybe-all-target-libstdc++-v3
>>
>> Compared to the existing one, the one you've added is additionally
>> restricted by '@unless gcc-bootstrap'.
>>
>> I noticed this as I remembered that on our og[...] development branches
>> we have a patch in the opposite direction: get rid of this dependency via
>> removing 'lang_env_dependencies = { module=libffi; cxx=true; };' from
>> 'Makefile.def'.  See
>> <http://mid.mail-archive.com/alpine.DEB.2.21.9999.1812201344250.99920@build7-trusty-cs.sje.mentorg.com>
>> "Disable libstdc++ dependency for libffi".  (Maciej CCed in case you have
>> any further thoughts on that.)
>
> Oh, I see what happened now, the old bug was actually fixed by r6-5415
> which added cxx=true.
> So yes my patch is actually not needed and can be reverted.
> I tried to look to see if there was a dependency was there but for
> some reason I did not see it.

---
## [apache/couchdb](https://github.com/apache/couchdb)@[77f34a1bbc...](https://github.com/apache/couchdb/commit/77f34a1bbc7c76aefa59777da21e2e76e79f7ec8)
#### Wednesday 2022-01-26 01:00:36 by Adam Kocoloski

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
## [blueputty01/usaco-guide](https://github.com/blueputty01/usaco-guide)@[0226778cd2...](https://github.com/blueputty01/usaco-guide/commit/0226778cd2d6e4f349450b518eb8d4dfc17ee73f)
#### Wednesday 2022-01-26 02:18:06 by Dustin Miao

Somebody once told me the world is gonna roll me I ain't the sharpest tool in the shed She was looking kind of dumb with her finger and her thumb In the shape of an "L" on her forehead Well the years start coming and they don't stop coming Fed to the rules and I hit the ground running Didn't make sense not to live for fun Your brain gets smart but your head gets dumb So much to do, so much to see So what's wrong with taking the back streets? You'll never know if you don't go You'll never shine if you don't glow Hey now, you're an all-star, get your game on, go play Hey now, you're a rock star, get the show on, get paid And all that glitters is gold Only shooting stars break the mold It's a cool place and they say it gets colder You're bundled up now, wait 'til you get older But the meteor men beg to differ Judging by the hole in the satellite picture The ice we skate is getting pretty thin The water's getting warm so you might as well swim My world's on fire, how about yours? That's the way I like it and I'll never get bored Hey now, you're an all-star, get your game on, go play Hey now, you're a rock star, get the show on, get paid All that glitters is gold Only shooting stars break the mold Hey now, you're an all-star, get your game on, go play Hey now, you're a rock star, get the show, on get paid And all that glitters is gold Only shooting stars Somebody once asked could I spare some change for gas? I need to get myself away from this place I said, "Yup" what a concept I could use a little fuel myself And we could all use a little change Well, the years start coming and they don't stop coming Fed to the rules and I hit the ground running Didn't make sense not to live for fun Your brain gets smart but your head gets dumb So much to do, so much to see So what's wrong with taking the back streets? You'll never know if you don't go (go!) You'll never shine if you don't glow Hey now, you're an all-star, get your game on, go play Hey now, you're a rock star, get the show on, get paid And all that glitters is gold Only shooting stars break the mold And all that glitters is gold Only shooting stars break the mold

---
## [maxspells/fulpstation](https://github.com/maxspells/fulpstation)@[c449fbb56c...](https://github.com/maxspells/fulpstation/commit/c449fbb56c7cb57fc9d8c0db32be0b66e6d7293b)
#### Wednesday 2022-01-26 03:23:41 by SgtHunk

Fixes Solitaire runtimes + missing APCs (#488)

* solitaire fixes

* fuck you bar decals

---
## [vincent-turato/aws-cdk](https://github.com/vincent-turato/aws-cdk)@[c071367def...](https://github.com/vincent-turato/aws-cdk/commit/c071367def4382c630057546c74fa56f00d9294c)
#### Wednesday 2022-01-26 06:10:54 by Kaizen Conroy

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
## [facebook/pyre-check](https://github.com/facebook/pyre-check)@[1bcf6eb3fe...](https://github.com/facebook/pyre-check/commit/1bcf6eb3fe713ca15250f27bfead219d854a4892)
#### Wednesday 2022-01-26 07:22:54 by Shannon Zhu

Change postprocessing scheduler policy for larger batches

Summary:
Alright, after a lot of debugging it seems to me that postprocessing large quantities of sources is painfully slow due to the scheduling parallelization overhead, NOT actually because of the work being done.

Some data points based on `pyre -l dataswarm-pipelines/tasks/ad_metrics/admetrics`, with D32369208 as base:
- Non sequential run with binary built on master P476429443:
   - Sources parsed: 90.03s
   - Check_Postprocessing: 894.72s
- Test without loading large source bodies, my original suspicion (non-sequential): P476426300
   - Sources parsed: 95.75s
   - Check_Postprocessing: 868.23s
   - For profiling visual output, see summary of D33720045 - you can see that while `_get_source` no longer takes up much of the postprocessing time, there are still huge gaps filling out the wall time despite all of the work involved being included in their own profiling steps.
- Sequential run with binary built on master P476447172:
   - Sources parsed: 1099.91s
   - Check_Postprocessing: 59.90s (!!)
- Non sequential run with scheduling changes P476447886:
   - Sources parsed: 94.71s
   - Check_Postprocessing: 69.97s

Helpful references:
Diff documenting how different scheduling policies work: D19402492 (https://github.com/facebook/pyre-check/commit/7a703fcfd659bfd2be7447050944603751b2a49d)
Diff setting some policies across the backend: D19450279 (https://github.com/facebook/pyre-check/commit/c5e63336d27f500767a5d3469e04029f7a87373a)

In general, I believe postprocessing work is light enough for the vast majority of sources that splitting it into parallel buckets had an unreasonably high overhead. Instead, if we define by count and simply say we want 5 chunks per worker with 20 workers by default and 300k sources to postprocess, we'd end up with buckets of 3000 tasks instead of 250.

This diff simply copies the scheduler policy we use for parsing. I think it's possible we should make the minimum size even more aggressive forcing this scheduling to be essentially sequential in nearly all cases, but I'll iterate on that (and check on some of the other scheduler policies we've set) as a follow-up. I also want to make sure I'm understanding the tradeoff between constant chunk size vs. count correctly.

Other things tried: D33780747, D33780968
killme

Reviewed By: grievejia

Differential Revision: D33779676

fbshipit-source-id: 3b96ed4db1c4b930ebedacbbaefaa599e79421b9

---
## [asynts/pico-os](https://github.com/asynts/pico-os)@[d8f3eec557...](https://github.com/asynts/pico-os/commit/d8f3eec5574a14a4e382612e71a5c959f89ff800)
#### Wednesday 2022-01-26 08:52:20 by Paul Scharnofske

Boot: Correctly load the boot loader from GDB

I thought that when we used 'load' from GDB, this would be equivalent to
putting things into flash and pushing reset, but this is not the case.

Instead, it loads everything to the load-memory-address and then jumps
to the entry address.  This means that the boot loader could be executed
at '0x10000000' or '0x20000000' depending on context.

This is really ugly in my opinion and I will do it slightly differently.
Instead, there is a special 'boot_0_openocd_entry' function which is
marked as entry point.  GDB will call this function which relays to
'boot_1_reset', while the reset will trigger it directly.

Therefore, in theory, both contexts would result in the same behaviour
which is much easier to reason about.  However, this doesn't quite work
at the moment, because of some issues with the linker (refer to 0003).

---
## [envato/terraform-provider-cloudflare](https://github.com/envato/terraform-provider-cloudflare)@[7dc1827e5f...](https://github.com/envato/terraform-provider-cloudflare/commit/7dc1827e5f785898adcf04cb796c0710072c64ff)
#### Wednesday 2022-01-26 10:29:28 by Jacob Bednarz

resource/cloudflare_ruleset: improve dashboard collisions

One of the earliest niggles with customers coming from the dashboard to
Terraform was the collision caused by a Ruleset phase being created in
the UI but the Terraform provider also needing to create the same
phase. This was problematic for a few reasons:

- The first was that when you deleted Ruleset rules in the UI, it didn't
  remove the phase. This was intentional but hidden behind the UI and
  only accessible via the API.
- Secondly, when customers wanted to use Terraform, there was an
  assumption they would be starting from scratch and many were not.
- Finally, in the event of a collision, we didn't know which Ruleset the
  customer wanted to use so we error'd out with a link to manually
  resolve which isn't a great solution but made the issue more
  prominent.

I had a chance to rethink through this issue and managed to find a way
that we improve all three points above and remove majority of the pain
points. With the proposed changes, the only time a customer needs to
manually resolve the Ruleset rules is if there are existing rules in the
UI which requires them to be deleted or migrated.

Achieving this requires the assumption that if the Ruleset has no rules,
it is ok to modify. Unfortunately, it's not that simple in practice. If
the phase already exists, we cannot just update it as the `name`
attribute is not writable after creation. Along with this, the `ref` and
`version` values will be automatically incremented causing a permadiff
in Terraform as the customer hasn't actually modified these values but
the backing service (and API) has. To work around this, if we find a
phase with no rules, we recreate it with the provided values which is
essentially the same the same thing as the "happy path" for a new
Terraform resource would be anyway.

---
## [ThebestkillerTBK/NEPS](https://github.com/ThebestkillerTBK/NEPS)@[8a69c714ea...](https://github.com/ThebestkillerTBK/NEPS/commit/8a69c714ea0126844bdd16756e154d58347ece4d)
#### Wednesday 2022-01-26 11:14:35 by MrJohnnyAppleseed

Fix crashing bug

We all know that when all Terrorists die and manage to plant the bomb, they all begin to spectate the bomb. When that would happen, it would cause the cheat to read the eyeangles of the bomb, which would just result in an error and a instant crash. This should add a check to prevent this bug from occurring again.

---
## [ArmolitskiyCarpoeb/Paradise](https://github.com/ArmolitskiyCarpoeb/Paradise)@[ede0b9088b...](https://github.com/ArmolitskiyCarpoeb/Paradise/commit/ede0b9088b7e22223dd4bd711349d904672b4451)
#### Wednesday 2022-01-26 11:28:26 by ArmolitskiyCarpoeb

REMOVE DOMINATORS

I FUCKING HATE SHITTY WEEABOO GUNS

---
## [Perkedel/Kaded-fnf-mods](https://github.com/Perkedel/Kaded-fnf-mods)@[01d8c9b0b3...](https://github.com/Perkedel/Kaded-fnf-mods/commit/01d8c9b0b3a8358b10157e976879ae5925634f7e)
#### Wednesday 2022-01-26 12:20:18 by Joel Robert Justiawan

[skip ci] well, multi months. this is risky

pls... okay this is idea and must be held for now. Roll the release after 3 songs. that's it. the lua and bonus songs later. Remember, don't execute!

Progress Cipher. C'mon! are we reaching it?

woops `getting-freaky` songId mitsake! mistake!

adjust loading bar little bit.

change all parser of JSON into TJSON. turns out it's phreacking easy & still compatible with JSON casters because it same returns Dynamic Dictionary whoahow!!! why didn't you tell? so yeah.

fix werror notesplash & final touch. yey! Notesplash work. Shadow Mario, and those who redrew the splash, I'm sorry 🙇‍♂️. also.... Phantom... um. evilsk8ter yeaa.

biggus..... chungus......

---
## [repinger/exynos9611_m21_kernel](https://github.com/repinger/exynos9611_m21_kernel)@[edac5e8e0d...](https://github.com/repinger/exynos9611_m21_kernel/commit/edac5e8e0d2b72d51aa7e7879001bed9f5086da8)
#### Wednesday 2022-01-26 12:46:25 by Christian Brauner

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

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[6ed2fafd4e...](https://github.com/tgstation/tgstation/commit/6ed2fafd4eccdc6f11e53acb9a1017b037d76360)
#### Wednesday 2022-01-26 13:52:23 by Iamgoofball

Removes the fucking 20 second stunlock rng from tourettes because it's fucking stupid and I just had the most agonizing thirty fucking minutes of my goddamn life, holy shit (#64416)

Removes the 20 second stunlock from tourettes

---
## [CubeSword/Infinity-Engine](https://github.com/CubeSword/Infinity-Engine)@[4ee13f99e1...](https://github.com/CubeSword/Infinity-Engine/commit/4ee13f99e127e59d60c5cd56535a760287cb2baf)
#### Wednesday 2022-01-26 15:01:16 by swordcube

so flipx was being stupid for characters??? might have fucked it up more tho with my "stayed up until 10am" lookin ass brain

---
## [RobertKDutka/showdownproject](https://github.com/RobertKDutka/showdownproject)@[b335cda40a...](https://github.com/RobertKDutka/showdownproject/commit/b335cda40a0809c34d0bb4ce25a9e3d175f4a32d)
#### Wednesday 2022-01-26 15:19:39 by RobertKDutka

FUCK ME FUCK YOU GIT LET ME MERGE THESE FUCKING CHANGES

---
## [cam900/mame](https://github.com/cam900/mame)@[a49e215466...](https://github.com/cam900/mame/commit/a49e2154666b0ee7423e2d859c21b7592a4c61b8)
#### Wednesday 2022-01-26 15:35:43 by Firehawke

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
## [webmasterjedi/ed-loopy-science](https://github.com/webmasterjedi/ed-loopy-science)@[d9127fdfe8...](https://github.com/webmasterjedi/ed-loopy-science/commit/d9127fdfe84c89794c27c6e88da98394d6535ad2)
#### Wednesday 2022-01-26 16:28:52 by webmasterjedi

tried to update a dependency for security shit wtf npm kinda sucks

---
## [ghc/ghc](https://github.com/ghc/ghc)@[e4ccc1edb2...](https://github.com/ghc/ghc/commit/e4ccc1edb2ec2ad33652b4b5158b2076a5fe2760)
#### Wednesday 2022-01-26 17:40:13 by David Feuer

Add test supplied in T20996 which uses data family result kind polymorphism

David (@treeowl) writes:

> Following @kcsongor, I've used ridiculous data family result kind
> polymorphism in `linear-generics`, and am currently working on getting
> it into `staged-gg`. If it should be removed, I'd appreciate a heads up,
> and I imagine Csongor would too.
>
> What do I need by ridiculous polymorphic result kinds? Currently, data
> families are allowed to have result kinds that end in `Type` (or maybe
> `TYPE r`? I'm not sure), but not in concrete data kinds. However, they
> *are* allowed to have polymorphic result kinds. This leads to things I
> think most of us find at least quite *weird*. For example, I can write
>
> ```haskell
> data family Silly :: k
> data SBool :: Bool -> Type where
>   SFalse :: SBool False
>   STrue :: SBool True
>   SSSilly :: SBool Silly
> type KnownBool b where
>   kb :: SBool b
> instance KnownBool False where kb = SFalse
> instance KnownBool True where kb = STrue
> instance KnownBool Silly where kb = Silly
> ```
>
> Basically, every kind now has potentially infinitely many "legit" inhabitants.
>
> As horrible as that is, it's rather useful for GHC's current native
> generics system. It's possible to use these absurdly polymorphic result
> kinds to probe the structure of generic representations in a relatively
> pleasant manner. It's a sort of "formal type application" reminiscent of
> the notion of a formal power series (see the test case below). I suspect
> a system more like `kind-generics` wouldn't need this extra probing
> power, but nothing like that is natively available as yet.
>
> If the ridiculous result kind polymorphism is banished, we'll still be
> able to do what we need as long as we have stuck type families. It's
> just rather less ergonomical: a stuck type family has to be used with a
> concrete marker type argument.

Closes #20996

Co-authored-by: Matthew Pickering <matthewtpickering@gmail.com>

---
## [Snakebittenn/Skyrat-tg](https://github.com/Snakebittenn/Skyrat-tg)@[eb384bd2d7...](https://github.com/Snakebittenn/Skyrat-tg/commit/eb384bd2d72a5b23dd9785cc06815049d507d3d5)
#### Wednesday 2022-01-26 18:07:43 by Useroth

Telemetry 'n shit (#10810)

* Refactors dbcore and limits the maximum amount of concurrent async queries to a variable amount (#59676)

Refactors dbcore to work off a subsystem if executed async and limits the maximum amount of concurrent async queries to 25.

This has been tested locally on a mysql docker image and there were no crashes (as long as you didn't run it with debug extools) + data was getting recorded fine.
Why It's Good For The Game

May or may not resolve terry crashes, however, each query creates a new thread which takes up 2mb, preventing the game from using that 2mb. This can lead to ooms if they stack up, e.g. due to poor connectivity. This solves that issue.

maintainer note: this did not actually resolve the crashes, but has value anyway. Crashes were sidestepped fixed by finding out Large Address Awareness works

cl
refactor: Refactors dbcore.dm to possibly resolve the crashes that happen on Terry.
/cl

* Fixes an oversight in database code and cleans up telemetry (#64177)

As it is right now, we never actually clear the temporary list processing_queries
So if the subsystem is for some reason unable to complete a run, we will just whip right back around to it again
If it's been long enough, this could even cause horrific log spam. There was just now a manuel round with roughly 30k undeleted query errors. not good.

But what was actually not deleting you may ask?
Well

When you create a db request, a 5 minute timer starts. after those 5 minutes are up, the request is qdeleted by the db subsystem
This is to prevent the creation of unused requests, and to handle requests that are never cleaned up

Telemetry code was creating all of its db requests inside a for loop that could check tick, and then later
attempting to call them in series

Since requests by default sleep, this almost always lead to undeleted queries, which harddel'd given long enough periods

I've fixed this by moving the data gathering away from the query creation
Why is it good for the game

I was working on atmos code, happy, safe in my delusion, when suddenly I got a ping from tattle freaking out over 200 undeleted queries a second
This resolves that issue, so I can once again live in peace
Changelog

cl
admin: Telemetry code will spam you with undeleted query logs much less often now!
server: Improved how the db subsystem handles undeleted queries, should never have an incident like that again
/cl

* Fixes an error in telemetry queries (#64205)

* Hardsynced time_track.dm with upstream

Co-authored-by: Watermelon914 <37270891+Watermelon914@users.noreply.github.com>
Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [Texera/texera](https://github.com/Texera/texera)@[c3af4463f4...](https://github.com/Texera/texera/commit/c3af4463f486c9cf001cb547b29b6189a3c8302f)
#### Wednesday 2022-01-26 18:42:29 by Albert Liu

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
## [dotnet/maui](https://github.com/dotnet/maui)@[ac6befcbee...](https://github.com/dotnet/maui/commit/ac6befcbee23fae2bd358d9ed3217757029a9d1f)
#### Wednesday 2022-01-26 19:21:30 by Jonathan Peppers

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
## [uizhen/digitalgoods](https://github.com/uizhen/digitalgoods)@[aca94ff378...](https://github.com/uizhen/digitalgoods/commit/aca94ff378cb88b4adaa6844b5cbcad9827f3510)
#### Wednesday 2022-01-26 19:26:57 by TukyBoy

Revert "Nextjs fuck you"

This reverts commit d8b72760471beee8d476f32aa7b244e8ce74f193.

---
## [gaelicWizard/bash-it](https://github.com/gaelicWizard/bash-it)@[b96c888c40...](https://github.com/gaelicWizard/bash-it/commit/b96c888c40b39836600966d5143680458f6fa483)
#### Wednesday 2022-01-26 19:36:48 by John D Pell

lib/search: code style cleanup

Couldn't even `shellcheck` until I did a first pass...too much noise! ♥

lib/search: `shellcheck`

SC2076
SC2091
SC2004
SC2086
SC2207

lib/search: fix `_bash-it-flash-term()`

1. `$text_black` isn't a parameter provided by _Bash It_. Typo?
2. `$bold_yellow` is meant for prompt strings and putputs `\[`; ditto `$bold_red`.
3. The color was never returned to normal after.

lib/search: fix usage statement `_bash-it-search()`

SC2154

lib/search: `shfmt`

My apologies to future `git blame` hunters ♥

lib/search: code cleanup

Improve `_bash-it-erase-term()`, `_bash-it-flash-term()`, `_bash-it-rewind()`, `_bash-it-search-result()`, and `_bash-it-search-component()`. Minor tweaks to `_bash-it-is-partial-match()`, and `_bash-it-search()`.

pathmunge tests

main: Glob for *.bash properly when path contains spaces

- `shfmt`, `shellcheck`
- Clean up legacy/compatibility code to simpler control flow
- Move theme stuff down to where themes are handled
- Don't use `**` as _Bash It_ has never before set `globstar`; this eliminates varying behavior by environment; this alsö fixes users having any not-enabled themes under their custom dir.
- Lose weird Mac-specific alternate shell startup file (Bash loads startup files on Mac the same as it does on any other *nix system.)
- Place `composure.sh` init all in one place

main: adopt `_bash-it-log-prefix-by-path()`

lib/reloader: adopt `_bash-it-log-prefix-by-path()`

lib/appearance: `shellcheck` && `shfmt`

reloader: `shellcheck` && `shfmt`

Rewrite globbing per `shellcheck`'s SC2013 recommendations, and standardize whitespace.

lib/preview: `shfmt` && `shellcheck`

Fix theme file path globbing when $BASH_IT contains any spaces.

My apologies to future `git blame` hunters ♥

uninstall: `shellcheck` && `shfmt`

lint: add lib to clean_files.txt

lib/theme: `shfmt` && `shellcheck`

My apologies to future `git blame` hunters ♥

lib/colors: `shellcheck` && `shfmt`

Alsö, clean up `__color_rgb` to just use a regular if block.

lib/p4helpers: `shfmt`

My apologies to future `git blame` hunters ♥

lib/githelpers: `shfmt` && `shellcheck`

My apologies to future `git blame` hunters ♥

lib/theme: don't redefine battery_char()

Combine the two definitions for `battery_char()` so the second one doesn't just overwrite the first one. Do one or the other, not both.

Don't evaluate if `battery_percentage()` is available at load time, evaluate it at run time.

lib/command_duration: `shfmt` && `shellcheck`

My apologies to future `git blame` hunters ♥

lib/theme: `shellcheck` SC2154

These variables are referenced by themes already linted.

lib/theme.githelpers: unbound varbl

lib/theme: don't use `date` for `$THEME_CLOCK_FORMAT`

main: simplify flow of lib loader loop

Eliminate the separate loop for `vendor/init.d` since it's just as easy to glob it in the `lib` loop.

lib: delete `appearance.bash`

This adds *three* lines to `bash_it.sh`, and two to `plugin/base`. Just not worth an extra file requiring special handling.

main: load custom theme

Allow for simpler directory strucutre when loading theme from `$CUSTOM_THEME_DIR`/`$BASH_IT_CUSTOM`

make aliases load very late

...and update all the tests...

preexec: add helper functions to loader

Define the helper functions for `bash-preexec.sh` immediately after importing it, rather than in `lib/theme`.
- `__check_precmd_conflict()` and `save_append_prompt_command()` are generally useful and not theme-specific.
- Add matching `__check_preexec_conflict()` like `__check_precmd_conflict()`, and alsö `safe_append_preexec()`.

preexec: work around upstream

Alsö, move `set +T` in here.

test/theme: make fewer assumptions

Literally copying a line from the source to be tested is perhaps not the best way to test that code. 😉

That said, we do want to verify that the function was actually loaded.

TODO: actually test the function.

install: use `.bashrc` and notify user

The logic to guess whether to use `.bash_profile` or `.bashrc` was buggy and wrong. Just use `.bashrc` and either automatically fill in a `.bash_profile`, or notify the user that they need to edit their `.bash_profile`.

completions/sqlmap: use `_command_exists`

Addresses bash-it/bash-it#1632

completion/fabric: no need for `_command_exists`

If we're already inside the completion handler for `fab`...then it's a bit silly to check if `fab` is installed.

plugins/go: simplify _bash-it-gopath-pathmunge()

plugin/history: no need to set a trap
Instead of globbally clearing `$HISTTIMEFORMAT` and setting a return trap to re-enable it, just make it local to the function.

Also, set the defaults in a way that is happy with read-only parameters.

aliases/general: minor fixes

- Don't define some aliases if the target isn't installed, use _command_exists to check instead of `type` and `which`.
- Use `$EDITOR` for the editor for aliases about editing, excep the `sudo` ones because maybe you want those specifically?
- Fix `ls` aliases to match their common definitions (-A instead of -a: don't show '.' and '..' when displaying hidden files).

themes/base: use `type -P` instead of `which`

Avoid external binary `which`. Use built-in `type -P` instead. Uppercase `-P` forces a path search to avoid hashed matches and functions/aliases and whatnot.

completion/grunt: shellcheck

completion/subversion: load system completion

Load the completion script from the subversion package installed on the system, instead of bundling a copy. This addresses Bash-it/bash-it#1818.

NOTE: If `completions/system` is enabled, then it will load this same file anyway automatically.

plugins/battery: lint

plugins/xterm: not just Xterm

plugins/thefuck: lint

plugins/todo: lint

plugin/base: use `_bash-it-component-item-is-enabled()`

completion/git: use `_completion_exists()`

plugins/alias: remove old `SC2154` flag

This is no logner needed because the `local` keyword was moved higher up in the function.

---
## [ewanmatthews/Hero-s-Journey-Bot](https://github.com/ewanmatthews/Hero-s-Journey-Bot)@[5eee17d974...](https://github.com/ewanmatthews/Hero-s-Journey-Bot/commit/5eee17d974f1269d8a28b07c2f978409fe74b526)
#### Wednesday 2022-01-26 20:00:36 by Ewan Matthews

Update: A Play Within A Play

Hot on the heels of the **incredible** Station Eleven, which features a story within a story, scenes from the world-famous Hamlet! In the final episode, Shakespeare's words become a conduit for emotions that some of the main characters have, but can't fully process. It was one of at least 5 scenes that brought me to tears!!!
So I created a small play name generator under #play2# (which I messily nested into #play# with '' around it to make it easier to read, I know, it was an afterthought). Some of these are based on famous works and the generator will, on occasion, reconstitute a famous name (like 'The Normal Heart'). More vocabulary is added with #subs# for substances and punny playwright names under #playw#, so plenty to discover!
Enjoy!
- Ewan

---
## [ederekun/fourteen_kernel_oneplus_msm8998](https://github.com/ederekun/fourteen_kernel_oneplus_msm8998)@[4d0bc3843d...](https://github.com/ederekun/fourteen_kernel_oneplus_msm8998/commit/4d0bc3843dbbf5bc64f4496059ab45cb7f8c7917)
#### Wednesday 2022-01-26 20:02:14 by Peter Zijlstra

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

---
## [jspecify/jspecify](https://github.com/jspecify/jspecify)@[4ac4961c5d...](https://github.com/jspecify/jspecify/commit/4ac4961c5d11beef765742ee3e2d57a8ec575d16)
#### Wednesday 2022-01-26 20:15:11 by Chris Povirk

Remove TODO about substitution into type-variable bounds.

It's still conceivable that we need such a thing. But if we do, it's
likely more correctly addressed at a deeper level. Notably, I see that
[JLS
4.10.2](https://docs.oracle.com/javase/specs/jls/se11/html/jls-4.html#jls-4.10.2)
has no mention of substitution in its discussion of type-parameter
bounds.

Additionally, with our hacky test checker, I am finding that *undoing*
the Checker Framework's subsitution into type-variable bounds *improves*
results. *That said*, I remember some other change that improved results
(but maybe only on *net*?) not long ago that I decided to back out
because it seemed to be getting the right answers for the wrong reasons.
So I'm not sure that undoing substitution is *actually* right, though
it's possible.

Honestly, I can't quite get my head around "substitution into
type-variable bounds" at all today. Arguably I should leave the TODO for
a day when I'm feeling more up to it. But I'm going to remove it in the
hope that:

- The bounds at the declaration site always provide enough information,
  since they must always be as strict as any bounds at a use site.
- If there is "extra" information available from viewing the type
  variable "as a member of" a type, then we get that from the type
  argument supplied to that type (a type argument that may itself by a
  type variable) or perhaps wildcard capture?

---
## [dlee0156/graspologic](https://github.com/dlee0156/graspologic)@[240b913560...](https://github.com/dlee0156/graspologic/commit/240b913560c6dc7437750fc6a519645453556b3c)
#### Wednesday 2022-01-26 20:19:07 by Dwayne Pryce

THE GRAND RENAMING HAS BEGUN (#481)

* THE GRAND RENAMING HAS BEGUN but holy crap it still doesn't work because of some nbsphinx thing that I don't know how to even begin troubleshooting

* Update .github/PULL_REQUEST_TEMPLATE.md

I am the goo0dest typer

Co-authored-by: Benjamin Pedigo <benjamindpedigo@gmail.com>

* Update README.md

Co-authored-by: Benjamin Pedigo <benjamindpedigo@gmail.com>

* Make the build status badge less obnoxious

* Made a sentence actually make sense

* Ah the last merge from dev must have overwritten some of the changes I made.  This should be fixed now.

* Found another instance of graspy in the issue template

* Some last second changes, including a fix to the utils init file because the __all__ value was being populated by identifier names not string representations of those identifier names

* I approve of black hating the single quotes for a string because I also hate it but it's still pythonic even if I wish it weren't so

Co-authored-by: Benjamin Pedigo <benjamindpedigo@gmail.com>

---
## [dlee0156/graspologic](https://github.com/dlee0156/graspologic)@[020e451ee6...](https://github.com/dlee0156/graspologic/commit/020e451ee61c83fbb3effc67a6a30781dddff900)
#### Wednesday 2022-01-26 20:19:07 by Dwayne Pryce

Suitably dynamic versioning (#467)

* Suitably dynamic versioning

The following versioning code bypasses a few problems with python module versions.  The following scenarios are plausible:
- A user clones `graspologic` and runs `pip install -r requirements.txt` then executes `python` in the project directory, accessing the graspologic library by python's local folder structure.
- A users clones `graspologic` and runs `python setup.py install` in the environment of their choice, accessing the graspologic library either by the local folder structure or the .egg in their site-packages, depending on their current working directory.
- A user clones no repository and wants to install the library solely via `pip` via the `pip install ...` command, which has 2 wings to consider:
  - The user wishes to try out the latest prerelease, which is going to be published with a X.Y.ZdevYYYYMMDDBUILDNUMBER style version and can be installed via `pip install graspologic --pre`
  - The user wishes to try out the latest release, which will be published as `X.Y.Z`.

This PR supports those 4 cases (notably, it does not support `pip install .` from the root project directory, which does some super weird stuff and I gave up on trying to solve it a long time ago)

The concept is this: the actual version upon a **build action**, which can be undertaken by:
- CI building a snapshot build
- CI building a release build
- Local user building a local build

These states all require the same thing: a materialized version in a file.  This version should be created at the time of this build action.

In the case of CI, we can populate the file in our CI build process and move on.  It's the case of not being in CI where we need to consider what to do next, which leaves Local user building a local build (and local user using the filesystem as the library).

In these cases, the solution is the following: if we have a populated version.txt file, we use it. If we do not, we materialize a new version based on the `__semver` in version.py and the current time in YYYYMMDDHHmmSS format. This means that if you are running on the filesystem, and you say `import graspy; print(graspy.__version__);`, it will actually tell you the version is `0.1.0dev20200926120000` as an example.  However, when you close the interpreter and do it again, it will tell you that the version is `0.1.0dev20200926120500` - because it will create a version for you at the time of import.

However, if you were to run `python setup.py install`, the setup.py file actually takes it on itself to either get a version number or use the materialized version described above, then to write it to version.txt.  Which means that installing the graspologic library from setuptools will actually lock in the version number in perpetuity.

Gotchas
- version.txt must always be empty in the source tree
- `pip install .` does some weird thing where it registers an entry in site-packages that is like a symlink to the local filesystem anyway so it doesn't actually make an egg which means you get a new version each time and I gave up caring at this point since we got the three primary use cases: developers, users of pre-releases, and users of releases all covered. Users who install by cloning and running pip install are just going to get a weird behavior that probably isn't that important to track down, and regardless they'll get a clear `X.Y.Zdev<timestamp>` in their `graspologic.__version__` which is enough for us to go on if there are any issues raised.

* My testing resulted in filling this file and committing it, like I said not to do

* Updated conf.py for sphinx to be able to find a version it likes.  Or kinda likes.  Maybe likes?

* Forgot I had to add the recursive-include for the version file.

* Making black happy

---
## [Chromosore/dotfiles](https://github.com/Chromosore/dotfiles)@[7432cb17e7...](https://github.com/Chromosore/dotfiles/commit/7432cb17e768b8ad828381020f118b10919c2ca6)
#### Wednesday 2022-01-26 20:20:51 by Chromosore

vim: Fix indentation related stuff.

By this, I mean:
  1) vim-polyglot's auto indent detection
  2) Set only 'tabstop' in ftplugin/vim.vim

If you wonder why, it is because vim's indentation situation in kind of
a mess. There are four options to set indentation, but only two seem
trivial: 'tabstop', which sets the tabstop, and 'expandtab', which
control whether indendation is done with tabs or spaces.

The two other are 'shiftwidth' and 'softtabstop'.

While writing the previous sentence, I discovered a new one:
'vartabstop'. Isn't it crazy?

'shiftwidth' controls the number of spaces each level of indentation is,
mixing tab and spaces when needed to achieve the desired length.

On the other hand, 'softtabstop' controls the length of the indentation
inserted when a tab is inserted. Again, it will mix tab and spaces as
needed to reach the desired length.

So basically, with these two options, you can keep the standard 8 spaces
tab yet indent using 4 "spaces equivalent". By this, I mean that two
levels of indentation (8 spaces) will be turned into a tab.
That's wild!

However, my indentation needs are much simpler. I want to use either
*one* tab per indentation level when 'expandtab' is off, or use
'tabstop' spaces per indentation level when 'expandtab' is on.
Quite simple, right?

That's why I decided to use just the 'tabstop' and the 'expandtab'
options. Therefore 'shiftwidth' has to always stay at 0 (to use
'tabstop') else I begin to get weird results.

As a bonus, everything scales when I change the 'tabstop', including the
> and < commands and indent guides.

So I try to manage it myself as much as possible.

---
## [Catarina-Lima/Watch-Your-Back](https://github.com/Catarina-Lima/Watch-Your-Back)@[96adb001e2...](https://github.com/Catarina-Lima/Watch-Your-Back/commit/96adb001e22895fae119c8c32e43cc5e39e8a000)
#### Wednesday 2022-01-26 20:29:39 by natercia

i am in misery

there aint nobody who can comfort me oh yeah why wont you answer me the silence is slowly killing me oh yeah girl you really got me bad you really got me bad

feitos a alavanca que desativa fogo e apanhar a chave / abrir porta

---
## [Offroaders123/piskel](https://github.com/Offroaders123/piskel)@[36760495a9...](https://github.com/Offroaders123/piskel/commit/36760495a9200bcfe62a83549c83f19e36833ebd)
#### Wednesday 2022-01-26 20:38:52 by Offroaders123

PWA Support for Piskel!

Hey there! I really love using Piskel, and I thought the user experience could be even stronger if Piskel was also installable as a PWA directly from the browser.

These additions also include support for offline use, using a Service Worker. This is a key part of what makes PWAs so cool. You can also install this on desktop, thanks to modern browser releases, so Piskel will also be able to open in it's own app window just like a native app can!
Testing this out on Localhost seemed to work great for both `grunt play` and `grunt serve`, however I'm not sure what else is part of your build process for pushing to the main site. I imagine if it works locally with Grunt, than it shouldn't have an issue with the main site.

About two versions away from now, with version 99, Chromium browsers will be adding support for the Window Controls Overlay display mode, for PWAs, and this allows the web app to take up even more space of the window at once. You can also enable which areas should or shouldn't be draggable for the title bar.
I also added support for that feature with these additions, so that will also look very futuristic! Feel free to learn more about the upcoming API on this article by the Google team at web.dev: https://web.dev/window-controls-overlay/

Thanks for working on such a great app over the years! I'm happy I gotten to the point in programming where I can finally be able to contribute to it :)

---
## [narayanaswamy7/react-native](https://github.com/narayanaswamy7/react-native)@[6c080167e6...](https://github.com/narayanaswamy7/react-native/commit/6c080167e6e342574298f43bb37becf139f6ac24)
#### Wednesday 2022-01-26 20:39:09 by edenb-moveo

Update ImageBackground.js (#32055)

Summary:
Currently ImageBackGround component has optional style props, but if you don't pass it as prop, it still "thinks" you pass style and crushes.
In this pr, I made width and height inside component to be optional so it won't crush.

## Changelog

[General] [Fix] - Changed ImageBackground's style so it won't crush.

[Screen Shot 2021-08-20 at 15 05 45](https://user-images.githubusercontent.com/62840630/130230568-be02b1a2-52ec-4f9d-b3d3-212552d3882b.png)

As you can see in this component, I tried to use ImageBackground without any style props, and my app crushes. Then I added style with empty object and the app didn't crush anymore, as you can see here:
![Screen Shot 2021-08-20 at 15 09 23](https://user-images.githubusercontent.com/62840630/130230932-a576c397-a910-4e40-a202-56482d83dd9c.png).

In conclusion, if we make width and height styles optionals inside ImageBackground component, it won't crush anymore.

Thoughts:
Maybe consider to make style props for this component none-optional because it isn't make any sense that image won't have any style at all.

Thanks ahead, that was my first pr, Eden Binyamin.

Pull Request resolved: https://github.com/facebook/react-native/pull/32055

Reviewed By: charlesbdudley

Differential Revision: D30452297

Pulled By: sshic

fbshipit-source-id: b7071aa457dba443ed2f627c2458ea84fd24b36d

---
## [prabhav/prabhavkhandelwal.com-v6](https://github.com/prabhav/prabhavkhandelwal.com-v6)@[a59d779337...](https://github.com/prabhav/prabhavkhandelwal.com-v6/commit/a59d779337fa7ec3d2273cb7bac0c555678dc43c)
#### Wednesday 2022-01-26 20:46:59 by Prabhav Khandelwal

from "/work" to "/work/"

just got done with my interview with slack - very hard to cut corners when so many awesome people are staring at your work. kinda feels like i bombed it - took full 1 hour (they did ask questions during) and my deck wasn't super slick. thankfully they asked questions about collaboration so i got to speak about it. if i had to guess their reaction: oh god he's just a kid, can't do lead for sure, half baked and scrappy work, the doodling thing is cool but not too well rounded as a person, didn't craft a proper story for skilli, yaar anna yeh kya bachha uthaake laayi ho.

well, what's done is done. presentation is the most key part which i sort of bombed. but there are interviews lined up too. not sure if they can salvage a bad presentation, but at least i can show them what im good at and show off a little. worst case, i'll have nice conversations with people and get to ask them questions too. okay, let's prepare for the upcoming thing in an hour. phew man, i'm already sad i won't get this - but i'm not totally surprised too.

---
## [microsoft/accessibility-insights-web](https://github.com/microsoft/accessibility-insights-web)@[60a93ded2b...](https://github.com/microsoft/accessibility-insights-web/commit/60a93ded2b227455a1fc794a2fa0ef1735a2c200)
#### Wednesday 2022-01-26 21:05:31 by Dan Bjorge

fix(tabstops-report): enable hover/focus highlighting on tab stops requirement rows (#5111)

#### Details

This PR enables the Details View > Fast Pass > Tab Stops' new Requirements table to use Office Fabric's default on-hover/on-focus styling that darkens the row backgrounds, to be consistent with the similar behavior in the similar looking Assisted Instance tables in Assessment.

The implementation for this is a little more complicated than expected. The on-hover/on-focus behavior is actually the default fabric behavior; Assessment doesn't do anything special to enable it. The reason we weren't seeing it in FastPass was that we were previously using a very hacky bit of CSS to override the background of the Fabric `DetailsView` to match the slightly-darker-than-usual-gray background we use in FastPass pages (it's different from Assessment to support Cards-based views that want to use our "normal" white background color for Card backgrounds):

```scss
.requirement-table {
    // ...
    * {
        background-color: $neutral-2;
    }
}
```

This was used because the fabric `DetailsView` contains many implementation-detail subcomponents (for rows, cells, headers, etc) that each individually apply overlapping background-color styles; if you just apply background-color to our containing `requirement-table` class, it doesn't have any effect on its own. However, this also has the effect of overriding all of the `:hover` and `:focus` styling under the table.

I originally tried using various combinations of `:not(:focus):not(:hover)` styles, but it rapidly devolved into a big mess of very hacky CSS. Instead, this PR implements a solution based on Office Fabric Themes, which are Fabric's intended way to solve this problem but not the way we normally use in our codebase (we usually use hacky overrides of CSS styles that are Fabric implementation details instead).

The typical Fabric-recommended solution for this is to use their `<Customizer>` to temporarily override the globally-loaded theme; however, this has the disadvantage that it isn't cognizant of the way we swap between "default" and "high-contrast" theme palettes at runtime in our top-level `<Theme>` component. This PR implements a new `<ThemeFamilyCustomizer>` which wraps the fabric `<Customizer>` in a way which respects our app's high contrast mode setting.

##### Animated screenshots

Before:

![animation showing no background color changes on hover/focus](https://user-images.githubusercontent.com/376284/151073621-adfcdd04-33de-4a77-8eed-ecb79cd42936.gif)

After (default theme):

![animation showing background color changing on hover/focus](https://user-images.githubusercontent.com/376284/151073627-a7fe0460-af59-40de-94bb-7c690f959d2a.gif)

After (app high contrast setting):

![animation showing background color changing on hover/focus](https://user-images.githubusercontent.com/376284/151074562-16c08b67-c134-42d2-92dd-04a66af30373.gif)

After (Windows "Night Sky" HC theme):

![animation showing background color changing on hover/focus](https://user-images.githubusercontent.com/376284/151076651-43484480-bb32-4958-aacf-3bdc9e6b2516.gif)

##### Motivation

* Make table hover/focus behavior consistent between Assessment and FastPass
* Set up infrastructure that can be used in other components to avoid some types of CSS hacks

##### Context

n/a

#### Pull request checklist
<!-- If a checklist item is not applicable to this change, write "n/a" in the checkbox -->
- [x] Addresses an existing issue: Part of #5099
- [x]  Ran `yarn fastpass`
- [x] Added/updated relevant unit test(s) (and ran `yarn test`)
- [x] Verified code coverage for the changes made. Check coverage report at: `<rootDir>/test-results/unit/coverage`
- [x] PR title *AND* final merge commit title both start with a semantic tag (`fix:`, `chore:`, `feat(feature-name):`, `refactor:`). See `CONTRIBUTING.md`.
- [x] (UI changes only) Added screenshots/GIFs to description above
- [x] (UI changes only) Verified usability with NVDA/JAWS

---
## [Tyeforce/squirdle](https://github.com/Tyeforce/squirdle)@[fe61e1554a...](https://github.com/Tyeforce/squirdle/commit/fe61e1554a9e2837d323f12d2603ae0ab7a11239)
#### Wednesday 2022-01-26 21:43:56 by Tyeforce

Update pokedex.csv

Added (missing forms with different generation/type/height/weight data than base forms):
- Giratina Origin Forme
- Thundurus Therian Forme
Note: Mega Evolutions, Primal Reversions, Gigantamax/Eternamax forms, Alolan/Galarian/Hisuian forms, Arceus/Silvally's type forms, and Pumpkaboo/Gourgeist's sizes are still excluded at this time.

Removed (for redundancy; same generation/type/height/weight data as base forms):
- Ash-Greninja
- Meowstic Female
Note: Lycanroc Dusk Form is also redundant with Lycanroc Midday Form, but unsure if it should be kept or not due to Midnight Form's inclusion

Changed:
- "Ho-oh" to "Ho-Oh"
- "Thundurus" to "Thundurus Incarnate Forme"
- "Meowstic Male" to "Meowstic"
- "Hoopa Hoopa Confined" and "Hoopa Hoopa Unbound" to "Hoopa Confined" and "Hoopa Unbound"

---
## [plinkiac/Movie-Talk](https://github.com/plinkiac/Movie-Talk)@[f945535753...](https://github.com/plinkiac/Movie-Talk/commit/f945535753ab3bf1867804014d624a1b672fc709)
#### Wednesday 2022-01-26 21:53:24 by Harry S. Plinkett

Create 2017-01-12 - Fuck You, It's January (2017).txt

---
## [git/git](https://github.com/git/git)@[07564773c2...](https://github.com/git/git/commit/07564773c2569d012719ab9e26b9b27251f3d354)
#### Wednesday 2022-01-26 21:56:55 by Ævar Arnfjörð Bjarmason

compat: auto-detect if zlib has uncompress2()

We have a copy of uncompress2() implementation in compat/ so that we
can build with an older version of zlib that lack the function, and
the build procedure selects if it is used via the NO_UNCOMPRESS2
$(MAKE) variable.  This is yet another "annoying" knob the porters
need to tweak on platforms that are not common enough to have the
default set in the config.mak.uname file.

Attempt to instead ask the system header <zlib.h> to decide if we
need the compatibility implementation.  This is a deviation from the
way we have been handling the "compatiblity" features so far, and if
it can be done cleanly enough, it could work as a model for features
that need compatibility definition we discover in the future.  With
that goal in mind, avoid expedient but ugly hacks, like shoving the
code that is conditionally compiled into an unrelated .c file, which
may not work in future cases---instead, take an approach that uses a
file that is independently compiled and stands on its own.

Compile and link compat/zlib-uncompress2.c file unconditionally, but
conditionally hide the implementation behind #if/#endif when zlib
version is 1.2.9 or newer, and unconditionally archive the resulting
object file in the libgit.a to be picked up by the linker.

There are a few things to note in the shape of the code base after
this change:

 - We no longer use NO_UNCOMPRESS2 knob; if the system header
   <zlib.h> claims a version that is more cent than the library
   actually is, this would break, but it is easy to add it back when
   we find such a system.

 - The object file compat/zlib-uncompress2.o is always compiled and
   archived in libgit.a, just like a few other compat/ object files
   already are.

 - The inclusion of <zlib.h> is done in <git-compat-util.h>; we used
   to do so from <cache.h> which includes <git-compat-util.h> as the
   first thing it does, so from the *.c codes, there is no practical
   change.

 - Until objects in libgit.a that is already used gains a reference
   to the function, the reftable code will be the only one that
   wants it, so libgit.a on the linker command line needs to appear
   once more at the end to satisify the mutual dependency.

 - Beat found a trick used by OpenSSL to avoid making the
   conditionally-compiled object truly empty (apparently because
   they had to deal with compilers that do not want to see an
   effectively empty input file).  Our compat/zlib-uncompress2.c
   file borrows the same trick for portabilty.

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>
Helped-by: Beat Bolli <dev+git@drbeat.li>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [ahjragaas/binutils-gdb](https://github.com/ahjragaas/binutils-gdb)@[bbea680797...](https://github.com/ahjragaas/binutils-gdb/commit/bbea68079781ac4c2fc941867ee9888585cafb77)
#### Wednesday 2022-01-26 22:20:14 by Andrew Burgess

gdb/python: improve the auto help text for gdb.Parameter

This commit attempts to improve the help text that is generated for
gdb.Parameter objects when the user fails to provide their own
documentation.

Documentation for a gdb.Parameter is currently pulled from two
sources: the class documentation string, and the set_doc/show_doc
class attributes.  Thus, a fully documented parameter might look like
this:

  class Param_All (gdb.Parameter):
     """This is the class documentation string."""

     show_doc = "Show the state of this parameter"
     set_doc = "Set the state of this parameter"

     def get_set_string (self):
        val = "on"
        if (self.value == False):
           val = "off"
        return "Test Parameter has been set to " + val

     def __init__ (self, name):
        super (Param_All, self).__init__ (name, gdb.COMMAND_DATA, gdb.PARAM_BOOLEAN)
        self._value = True

  Param_All ('param-all')

Then in GDB we see this:

  (gdb) help set param-all
  Set the state of this parameter
  This is the class documentation string.

Which is fine.  But, if the user skips both of the documentation parts
like this:

  class Param_None (gdb.Parameter):

     def get_set_string (self):
        val = "on"
        if (self.value == False):
           val = "off"
        return "Test Parameter has been set to " + val

     def __init__ (self, name):
        super (Param_None, self).__init__ (name, gdb.COMMAND_DATA, gdb.PARAM_BOOLEAN)
        self._value = True

  Param_None ('param-none')

Now in GDB we see this:

  (gdb) help set param-none
  This command is not documented.
  This command is not documented.

That's not great, the duplicated text looks a bit weird.  If we drop
different parts we get different results.  Here's what we get if the
user drops the set_doc and show_doc attributes:

  (gdb) help set param-doc
  This command is not documented.
  This is the class documentation string.

That kind of sucks, we say it's undocumented, then proceed to print
the documentation.  Finally, if we drop the class documentation but
keep the set_doc and show_doc:

  (gdb) help set param-set-show
  Set the state of this parameter
  This command is not documented.

That seems OK.

So, I think there's room for improvement.

With this patch, for the four cases above we now see this:

  # All values provided by the user, no change in this case:
  (gdb) help set param-all
  Set the state of this parameter
  This is the class documentation string.

  # Nothing provided by the user, the first string is now different:
  (gdb) help set param-none
  Set the current value of 'param-none'.
  This command is not documented.

  # Only the class documentation is provided, the first string is
  # changed as in the previous case:
  (gdb) help set param-doc
  Set the current value of 'param-doc'.
  This is the class documentation string.

  # Only the set_doc and show_doc are provided, this case is unchanged
  # from before the patch:
  (gdb) help set param-set-show
  Set the state of this parameter
  This command is not documented.

The one place where this change might be considered a negative is when
dealing with prefix commands.  If we create a prefix command but don't
supply the set_doc / show_doc strings, then this is what we saw before
my patch:

  (gdb) python Param_None ('print param-none')
  (gdb) help set print
  set print, set pr, set p
  Generic command for setting how things print.

  List of set print subcommands:

  ... snip ...
  set print param-none -- This command is not documented.
  ... snip ...

And after my patch:

  (gdb) python Param_None ('print param-none')
  (gdb) help set print
  set print, set pr, set p
  Generic command for setting how things print.

  List of set print subcommands:

  ... snip ...
  set print param-none -- Set the current value of 'print param-none'.
  ... snip ...

This seems slightly less helpful than before, but I don't think its
terrible.

Additionally, I've changed what we print when the get_show_string
method is not provided in Python.

Back when gdb.Parameter was first added to GDB, we didn't provide a
show function when registering the internal command object within
GDB.  As a result, GDB would make use of its "magic" mangling of the
show_doc string to create a sentence that would display the current
value (see deprecated_show_value_hack in cli/cli-setshow.c).

However, when we added support for the get_show_string method to
gdb.Parameter, there was an attempt to maintain backward compatibility
by displaying the show_doc string with the current value appended, see
get_show_value in py-param.c.  Unfortunately, this isn't anywhere
close to what deprecated_show_value_hack does, and the results are
pretty poor, for example, this is GDB before my patch:

  (gdb) show param-none
  This command is not documented. off

I think we can all agree that this is pretty bad.

After my patch, we how show this:

  (gdb) show param-none
  The current value of 'param-none' is "off".

Which at least is a real sentence, even if it's not very informative.

This patch does change the way that the Python API behaves slightly,
but only in the cases when the user has missed providing GDB with some
information.  In most cases I think the new behaviour is a lot better,
there's the one case (noted above) which is a bit iffy, but I think is
still OK.

I've updated the existing gdb.python/py-parameter.exp test to cover
the modified behaviour.

Finally, I've updated the documentation to (I hope) make it clearer
how the various bits of help text come together.

---
## [kraj/binutils-gdb](https://github.com/kraj/binutils-gdb)@[299953ca95...](https://github.com/kraj/binutils-gdb/commit/299953ca95cc5ac47e52236e2eeb44afc5369134)
#### Wednesday 2022-01-26 23:16:31 by Andrew Burgess

gdb/python: handle non utf-8 characters when source highlighting

This commit adds support for source files that contain non utf-8
characters when performing source styling using the Python pygments
package.  This does not change the behaviour of GDB when the GNU
Source Highlight library is used.

For the following problem description, assume that either GDB is built
without GNU Source Highlight support, of that this has been disabled
using 'maintenance set gnu-source-highlight enabled off'.

The initial problem reported was that a source file containing non
utf-8 characters would cause GDB to print a Python exception, and then
display the source without styling, e.g.:

  Python Exception <class 'UnicodeDecodeError'>: 'utf-8' codec can't decode byte 0xc0 in position 142: invalid start byte
  /* Source code here, without styling...  */

Further, as the user steps through different source files, each time
the problematic source file was evicted from the source cache, and
then later reloaded, the exception would be printed again.

Finally, this problem is only present when using Python 3, this issue
is not present for Python 2.

What makes this especially frustrating is that GDB can clearly print
the source file contents, they're right there...  If we disable
styling completely, or make use of the GNU Source Highlight library,
then everything is fine.  So why is there an error when we try to
apply styling using Python?

The problem is the use of PyString_FromString (which is an alias for
PyUnicode_FromString in Python 3), this function converts a C string
into a either a Unicode object (Py3) or a str object (Py2).  For
Python 2 there is no unicode encoding performed during this function
call, but for Python 3 the input is assumed to be a uft-8 encoding
string for the purpose of the conversion.  And here of course, is the
problem, if the source file contains non utf-8 characters, then it
should not be treated as utf-8, but that's what we do, and that's why
we get an error.

My first thought when looking at this was to spot when the
PyString_FromString call failed with a UnicodeDecodeError and silently
ignore the error.  This would mean that GDB would print the source
without styling, but would also avoid the annoying exception message.

However, I also make use of `pygmentize`, a command line wrapper
around the Python pygments module, which I use to apply syntax
highlighting in the output of `less`.  And this command line wrapper
is quite happy to syntax highlight my source file that contains non
utf-8 characters, so it feels like the problem should be solvable.

It turns out that inside the pygments module there is already support
for guessing the encoding of the incoming file content, if the
incoming content is not already a Unicode string.  This is what
happens for Python 2 where the incoming content is of `str` type.

We could try and make GDB smarter when it comes to converting C
strings into Python Unicode objects; this would probably require us to
just try a couple of different encoding schemes rather than just
giving up after utf-8.

However, I figure, why bother?  The pygments module already does this
for us, and the colorize API is not part of the documented external
API of GDB.  So, why not just change the colorize API, instead of the
content being a Unicode string (for Python 3), lets just make the
content be a bytes object.  The pygments module can then take
responsibility for guessing the encoding.

So, currently, the colorize API receives a unicode object, and returns
a unicode object.  I propose that the colorize API receive a bytes
object, and return a bytes object.

---
## [marekjm/viuavm](https://github.com/marekjm/viuavm)@[9d677c2efa...](https://github.com/marekjm/viuavm/commit/9d677c2efa71cc8942bb08b10173ac6920d586a6)
#### Wednesday 2022-01-26 23:19:47 by Marek Marecki

Release 0.11.1

The new, prototype distribution includes more or less functional tools
that allows somewhat normal workflow. There toolchain includes:

- assembler: for turning source code into executable ELFs
- disassembler: to make inspecting ELFs easier by converting them back
  into textual representation
- readelf: to easily get some high-level information about contents of
  ELFs produced by the assembler
- virtual machine kernel: for actually executing the bytecode contained
  in ELFs

There is no debugger (only a disassembler and an EBREAK instruction),
and no static analyser. The programmers are on their own and the VM went
back to living in the wild, wild west.

But I like the direction in which we the new prototype is going. I think
it will yield a better code then the VM I were developing for the
past... let me check my notes... 7? SEVEN FUCKING YEARS? Damn, how the
time flies. It was that long ago.

And still, no stable release. Nicely done, or rather NOT done. Good
going. Maybe I will have something usable when the VM hits a decade of
commit history. And that's a biiig maybe.

---
## [barefootcoder/common](https://github.com/barefootcoder/common)@[8c521954fc...](https://github.com/barefootcoder/common/commit/8c521954fc583811d2a2dc197791562a22f69e29)
#### Wednesday 2022-01-26 23:20:55 by Buddy Burden

finally fix the `win-stack-comms` bug(s)

stop trying to change desktops in `xrestore`
-	`win-stack-comms` can't help but do it, but doing it in `xrestore` is just fucking shit up
-	basically, since `xrestore`ing Thunderbird is happening in the background,
--		now it's trying to restore the original desktop twice
--		with predictably chaotic results
-	and, to add insult to injury, it's just not necessary
but the big bug that was making me have to run `win-stack-comms` twice in a row every single time
-	was that `is_visible` in `xrestore` would just die if the window wasn't visible yet
-	which ... no.  just no.
-	so, fixing that solved the majority of my problems
ancillary change:
-	getting rid of the desktop switching allowed me to expunge a loop
-	plus the `cur_desktop_num` function was no longer necessary
-	`win-stack-comms` needed to silence output from `xrestore`ing Thunderbird
--		because the output would often come after the main script had exited entirely

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[7d31da60a2...](https://github.com/mrakgr/The-Spiral-Language/commit/7d31da60a26fe44bebc0fbc39139fc0a099724be)
#### Wednesday 2022-01-26 23:41:34 by Marko Grdinić

"11:45am. I am on sick leave today. My brain literally hurts from lack of sleep. I went to bed earlier at 10:40pm, but it was a struggle to fall asleep, I must have been wide awake till around 6am.

It has been a while since I fell sick last. It must have been years. I def got this from my father. Let me take my temperature. After that comes breakfast. Maybe I'll watch some Houdini tutorials, but I won't obligate myself. This is a great day to just read the novels I got recently.

12:30pm. 38.5C. Yep, today is a a day to just let loose.

12:50pm. Let me go to bed. I am feeling the chills.

2:15pm. I can't stand lying in bed after all. It is just increasing my headache, and that medicine did make me feel better.

4:20pm. Let me go to bed. I am feeling the chills again.

11:15pm. I am up. I got some actually sleep between 6:30 and 10. It is just that after consuming medicine, my body temperature is going haywire and I am sweating like a pig despite removing all but a single blanket. If I try to force sleep I'll end up like yesterday. Since I did get some rest, I might as well finish vol 16. I really did not get my chill time today in the usual sense.

Common colds are the worst at the start, usually I get over them after a few days. Assuming I could get some rest tonight, maybe I could get some studying done tomorrow.

12:40pm. Fatigue is hitting me. Let me go to bed here now that I've finished dinner and Dendro vol 16. Hopefully I'll be able to get some proper sleep tonight. If I can recover a bit by tomorrow, I'll be able to resume my studies."

---
## [5484-Enderbots-FTC/Frieght-Frenzy](https://github.com/5484-Enderbots-FTC/Frieght-Frenzy)@[53a37ddcce...](https://github.com/5484-Enderbots-FTC/Frieght-Frenzy/commit/53a37ddcce01fe2c959661cea98075b9fd1973b6)
#### Wednesday 2022-01-26 23:47:56 by Tonny0414

i hate this shit

tears in my eyes,  chunkles in my thighs

---

