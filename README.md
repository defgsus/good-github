## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-07-22](docs/good-messages/2022/2022-07-22.md)


1,837,184 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,837,184 were push events containing 2,794,263 commit messages that amount to 203,254,383 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 34 messages:


## [andlabs/libui](https://github.com/andlabs/libui)@[8b3e2665ed...](https://github.com/andlabs/libui/commit/8b3e2665ed1af3e7a2f70104551e90a6bffe095e)
#### Friday 2022-07-22 00:43:25 by Pietro Gagliardi

Good night, friend.

I meant to do this a year ago, but didn't, because the pandemic rotted my brain. I'm sorry.

This project is probably not big enough for something like this, but not doing this would be irresponsible, given the circumstances.

---
## [Hekzder/mojave-sun-13](https://github.com/Hekzder/mojave-sun-13)@[a7a0e33192...](https://github.com/Hekzder/mojave-sun-13/commit/a7a0e33192ad3fcac5ad64d441f24af6ec852054)
#### Friday 2022-07-22 01:23:08 by Hekzder

Mob overhaul for DT (#2117)

* Basic mobs

Title

* Start of simple robots

Title

* THE GREAT MOB SOUNDENING

TITLE

* Handies + ranged attack buffs

FASTER!!

* Protectrons, robobrains

* Death sounds and fixes some dumb shit

Title

* NEW ROACHES OMG!!!

WOW!

* Robo sounds

Title

* Mob projectile tweaks

I THINK WE'RE GOOD

* bitty

---
## [notfrying1pans/StarbloomSS13](https://github.com/notfrying1pans/StarbloomSS13)@[635f518d04...](https://github.com/notfrying1pans/StarbloomSS13/commit/635f518d04a30c4c9f977c0570d480f8d44e56d1)
#### Friday 2022-07-22 01:55:52 by notfrying1pans

web edit fuck yoooou

i swear to fucking god if this resets line endings or some shit im gonna scream

---
## [jsoref/terminal](https://github.com/jsoref/terminal)@[9ccd6ecd74...](https://github.com/jsoref/terminal/commit/9ccd6ecd744890b856f3d8a39ff0616c0e34d4fb)
#### Friday 2022-07-22 02:38:56 by Mike Griese

Manually copy trailing attributes on a resize (#12637)

## THE WHITE WHALE

This is a fairly naive fix for this bug. It's not terribly performant,
but neither is resize in the first place.

When the buffer gets resized, typically we only copy the text up to the
`MeasureRight` point, the last printable char in the row. Then we'd just
use the last char's attributes to fill the remainder of the row.

Instead, this PR changes how reflow behaves when it gets to the end of
the row. After we finish copying text, then manually walk through the
attributes at the end of the row, and copy them over. This ensures that
cells that just have a colored space in them get copied into the new
buffer as well, and we don't just blat the last character's attributes
into the rest of the row. We'll do a similar thing once we get to the
last printable char in the buffer, copying the remaining attributes.

This could DEFINITELY be more performant. I think this current
implementation walks the attrs _on every cell_, then appends the new
attrs to the new ATTR_ROW. That could be optimized by just using the
actual iterator. The copy after the last printable char bit is also
especially bad in this regard. That could likely be a blind copy - I
just wanted to get this into the world.

Finally, we now copy the final attributes to the correct buffer: the new
one.  We used to copy them to the _old_ buffer, which we were about to
destroy.

## Validation

I'll add more gifs in the morning, not enough time to finish spinning a
release Terminal build with this tonight.

Closes #32 🎉🎉🎉🎉🎉🎉🎉🎉🎉
Closes #12567

(cherry picked from commit 855e1360c0ff810decf862f1d90e15b5f49e7bbd)

---
## [jameslamb/hamilton](https://github.com/jameslamb/hamilton)@[834edac907...](https://github.com/jameslamb/hamilton/commit/834edac90764bb34a6c997a0b88575ade8bfa88e)
#### Friday 2022-07-22 02:47:17 by skrawczyk

Adds parameterized_inputs decorator

This is a squashed commit of all the commits to create the parameterized_inputs
decorator. See the commits below that are in reverse chronological order.

Basically, this replaces `parameterized_input`, and provides a more succinct
API by using the function doc as a template, removing the need for a tuple.

We believe this is a simpler API to read/maintain — the kwargs assumption will
make it harder to extend the API, but we don’t think we need to.

——— Consolidated commits below ——

Adds format doc function to parameterized_inputs

To consolidate formatting in a single place. Want to keep
the code DRY. (+7 squashed commits)
Squashed commits:
[338c02a] Touches up documentation typos

And adds reraising original exception for formatting errors.
[f2725ec] Adds validate test for parameterized_inputs for the doc string

Doc string templates errors should be checked during validate.
That way we can throw a better error.
[4689177] Changes parameterized_inputs to use kwargs

1. So that we don't scope creep this API. Key words arguments are
assumed to be outputs. This removes a level of nesting on the API.
2. We're inline with other decorators in having the kwargs behavior, e.g. config.when.
[df571f3] Changes parameterized_inputs to take dict and format doc string

With the prior design, the issue was documentation. But after noodling on it
and prodding from Eljiah, I realized that the documentation string should just
be a template. Since you're going to be using the same function, the doc string
should be fairly generic, with only the parameters being passed changing the
meaning -- which with templatization, allows for that to come through.

Note - stylistically I think we prefer:

```python
@parametrized_inputs(
    parameterization={
        'output_123': dict(input_value_tbd1='input_1',
                           input_value_tbd2='input_2',
                           input_value_tbd3='input_3')
    }
)
```
because syntax highlighting will make it clearer what is being replaced in the
function with what input value.

to

```python
@parametrized_inputs(
    parameterization={
        'output_123': {
                 'input_value_tbd1'='input_1',
                 'input_value_tbd2='input_2',
                 'input_value_tbd3'='input_3'
        }
    }
)
```
or

```python
@parametrized_inputs(
    parameterization=dict(
        output_123={
                 'input_value_tbd1'='input_1',
                 'input_value_tbd2='input_2',
                 'input_value_tbd3'='input_3'
        }
    )
)
```
I think the last two ones are less clear/readable.

Otherwise I did have the thought of using actual functions in the mapping. It would
then be clearer to trace what is going on with an IDE.
However that brings up the possibility of people importing functions and running
into import messes... So punting on that for now. We can always add that in later
if we think that's required.
[0e21e9d] Changes parameterized_input to parameterized_inputs in decorator docs

Since parameterized_input is deprecated, we should just remove it from the
docs and instead just push parameterized_inputs.
[4379a38] Adds ParameterMapping named tuple object to adjust parameterized_inputs

People creating a dictionary of tuple to tuples is probably unwieldy. This is a power
use case, and thus it should afford a little more friction to use, and the net result of that
is that the code should become more readable.

We should preference keyword arguments everywhere here -- as that will make the code
much more readable than without it. E.g. :
```python
@parametrized_inputs(
    parameters=['input_value_tbd1', 'input_value_tbd2', 'input_value_tbd3'],
    parameter_mappings=[
        ParameterMapping(
            inputs=['input_1', 'input_2', 'input_3'],
            output_name='output_123',
            output_docs='function_with_multiple_inputs called using input_1'),
    ]
)
def func(...)

@parametrized_inputs(
    ['input_value_tbd1', 'input_value_tbd2', 'input_value_tbd3'],
    [ParameterMapping(['input_1', 'input_2', 'input_3'], 'output_123', 'function_with_multiple_inputs called using input_1')]
)
```

Adjusts tests and documentation accordingly.
[c1d5fa8] Adds parameterized_inputs

This change adds `paramterized_inputs` decorator, which
is almost a carbon copy of `paramterized_input` but that it allows
any number of parameters to be mapped.

Why is it a separate class? Well for backwards compatibility
we don't want to break parameterized_input. Should we try to
consolidate them? I think so -- so we should then mark `parameterized_input`
as deprecated and will be removed in a 2.0 release?

I should then probably update all documentation to reflect `parameterized_inputs`
and thus the documentation on `paramterized_input` to either be hidden or
non-existant? Hmm.

---
## [emersonford/clap](https://github.com/emersonford/clap)@[d43f1dbf6f...](https://github.com/emersonford/clap/commit/d43f1dbf6f1f7865dccfece0e1605a12efb76670)
#### Friday 2022-07-22 03:17:08 by Ed Page

docs: Move everything to docs.rs

A couple of things happened when preparing to release 3.0
- We needed derive documentation
  - I had liked how serde handled theres
  - I had bad experiences finding things in structopt's documentation
- The examples were broken and we needed tests
- The examples seemed to follow a pattern of having tutorial content and
  cookbook content
- We had been getting bug reports from people looking at master and
  thinking they were looking at what is currently released
- We had gotten feedback to keep down the number of places that
  documentation was located

From this, we went with a mix of docs.rs and github
- We kept the number of content locations at 2 rather than 3 by not
  having an external site like serde
- We rewrote the examples into explicit tutorials and cookbooks to align
  with the 4 styles of documentation
- We could test our examples by running `console` code blocks with
  trycmd
- Documentation was versioned and the README pointed to the last release

This had downsides
- The tutorials didn't have the code inlined
- Users still had a hard time finding and navigating between the
  different forms of documentation
- In practice, we were less likely to cross-link between the different
  types of documentation

Moving to docs.rs would offer a lot of benefits, even if it is only
designed for Rust-reference documentation and isn't good for Rust derive
reference documentation, tutorials, cookbooks, etc.  The big problem was
keeping the examples tested to keep maintenance costs down.  Maybe its
just me but its easy to overlook
- You can pull documentation from a file using `#[doc = "path"]`
- Repeated doc attributes get concatenated rather than first or last
  writer winning

Remember these when specifically thinking about Rust documentation made
me realize that we could get everything into docs.rs.

When doing this
- Tutorial code got brought in as was one of the aims
- We needed to split the lib documentation and the README to have all of
  the linking work.  This allowed us to specialize them according to
  their rule (user vs contributor)
- We needed to avoid users getting caught up in making a decision
  between Derive and Builder APIs so we put the focus on the derive API
  with links to the FAQ to help users decide when to use one or the
  other.
- Improved cross-referencing between different parts of the
  documentation
- Limited inline comments were added to example code
  - Introductory example code intentionally does not have teaching
    comments in it as its meant to give a flavor or sense of things and
    not meant to teach on its own.

This is a first attempt.  There will be a lot of room for further
improvement.  Current know downsides:
- Content source is more split up for the tutorials

This hopefully addresses #3189

---
## [guest3444307/OneshotGB](https://github.com/guest3444307/OneshotGB)@[4f15741228...](https://github.com/guest3444307/OneshotGB/commit/4f15741228cd904d62a4c4798bc106a365fc8b7b)
#### Friday 2022-07-22 03:54:04 by Max Nexus

7/21/22 part 2 coloring update

7/21/22 part 2: b5 and b6 completed, Honestly i hope to try and get a bit of a team going for this if i were to continue. My pace is slow as this is a large project and im not motivated to work on it at all times. Like seriously. I would've released this much earlier if i didn't try implementing color, but i was suggested it by my brother when i showed him this and i thought it wouldn't be too hard, well i guess it would be easy if i was lazy and didn't try to make the look the best they possibly could but still. I have zero experience running a team for a modding project but that doesn't mean i'll do a terrible job. I just have to setup a goal and coordinate with others, not have high standards and also not expect a fast pace from them either since i'm pretty slow on this thing myself. Sorry for turning this into a blog but i feel like it's good to document my thoughts like this on the project. Maybe it'll be nice to look back later and read these.

---
## [kokizzu/cadence](https://github.com/kokizzu/cadence)@[add4b390ad...](https://github.com/kokizzu/cadence/commit/add4b390ada43fdd8167f06e209ae6ece0d11aaa)
#### Friday 2022-07-22 04:43:40 by Steven L

Standardizing cancellation behavior: a canceled workflow never starts a new run (#4898)

# Summary for busy people

Workflow cancellation was kinda weird and confusing, and left some awful, unrecoverable, and un-*preventable* edge cases (particularly with child workflows).  It also left users with no way to reliably stop work, aside from termination.  Termination is inherently "unclean" and risky, so it should not be required to achieve something outside exceptional circumstances where recovery is not possible.

This commit changes that: cancellation is now "sticky", and a canceled workflow does not ever trigger a new run after it completes, regardless of how it completes, so it can be used as a reliable "stop processing after cleanup" tool.  The final state of a canceled workflow's run is now *always* a successful completion with a value, canceled, or timed out. (termination remains always "terminated")  
A canceled workflow can still start and abandon child workflows, so all current behavior with retries / continue as new / etc can be replicated with child workflows if desired.

A fair bit of (not very complex) additional work here and in nearly all other repos is required to truly complete this, but it is *functional* and non-optional with this commit alone.  
In particular, adding a dynamic config to (temporarily!) restore old behavior should be fairly easy if it proves to be needed.

# More details and motivation

Part 1 of [many, tbd, in multiple repos] involved in changing workflow cancellation to reliably end workflows.
Tests will be coming soon, for now I'm using a fairly simple set of workflows and checking the resulting histories exhaustively by hand.

The primary motivation for these changes is to address some impossible-to-recover-from scenarios when canceling child workflows.  After further exploration and discussion we've realized that, without these changes, there is *no reliable way* to stop a sequence of workflows without relying on termination, which we consistently treat as a fallback / impure-but-necessary ultimate hammer.

Workflows should not *need* to rely on termination to achieve a desired behavior.  With these changes, cancellation becomes capable of *guaranteeing* that workflows end within some finite time, which is a unique ability and makes it much more consistent and reliable.  
Turning this into a "complete" change will require quite a few tests, documentation changes, client-side changes (to allow recording more info, and likely changing test suites), and some smallish database and maybe RPC changes (to hold/return more data in cancellation errors).

We are also not currently planning on making this configurable.  It's seen as a correction of an under-specified and somewhat flawed chunk of behavior, more than "a change".  
Existing workflows will not experience replay errors, but it is still a substantial *semantic* change, though from what we have seen cancellation is relatively rarely used (partly due to its complex behavior).  If issues are encountered / if users end up needing it, it should be fairly easy to add a per-domain/tasklist/workflow type configuration value, but it will be opt-*out*, not opt-*in*.

# What was happening

Previously, workflow behavior on cancellation was pretty frequently surprising to our users, arguably inconsistent, and not very well documented:

| **PREVIOUS**  | **simple**               | **retry**                                 | **cron**                                | **retry+cron**                                    |
|--------------:|--------------------------|-------------------------------------------|-----------------------------------------|---------------------------------------------------|
| **success**   | success                  | success                                   | success<br>continue cron<br>cron        | success<br>continue cron<br>cron<br>retry         |
| **cancel**    | canceled                 | canceled                                  | canceled                                | canceled                                          |
| **retryable** | (n/a, fatal)             | continue retry<br>retry<br>recorded error | (n/a, fatal)                            | continue retry<br>cron<br>retry<br>recorded error |
| **fatal**     | failed<br>recorded error | failed<br>recorded error                  | continue cron<br>cron<br>recorded error | continue cron<br>cron<br>retry<br>recorded error  |
| **continue**  | continue immediately     | continue immediately<br>retry             | continue immediately                    | continue immediately<br>retry                     |
| **timeout**   | timeout                  | continue retry<br>retry<br>recorded error | continue cron<br>cron<br>recorded error | continue retry<br>cron<br>retry<br>recorded error |

A legend is:
- success / etc shows the final state of the canceled run (success = completed with a value that can be retrieved)
- "continue X" covers what source is used to compute the next run's starting delay (cron, retry, or no delay)
- "cron" / "retry" shows whether or not cron/retry configuration is carried over to the new run
  - note that cron is lost by default with continue-as-new
- and "recorded error" is whether or not the returned error is saved in its entirety (type + reason + details)

This largely summarizes as "cancellation works when you end with the canceled-context error", say from `ctx.Err()`, otherwise it behaves like normal (or nearly) and many scenarios will start a new run.
That's somewhat reasonable, but it's fairly "fragile" (it depends on what you return, and there are *many* ways for code to return some other error), and most importantly it means *there is no reliable way to stop a workflow* except to terminate it.

That has severe consequences in at least two scenarios:
1. When termination is *unsafe*
2. When a parent workflow cancels a child by canceling its context

For 1, for manual cancellations it's potentially reasonable to just terminate a run that begins after a successful cancel... but in principle if you're using cancellation it implies that termination is *not* desired, and potentially not safe to do.  Canceling may result in a brand new run that immediately starts new behavior, leaving you with no safe window to terminate and not leave bad state lingering.  
So users wanting a safe way to stop a sequence of workflows have no reliable way to do so.

For 2, it puts parent+child workflows in an extremely awkward, and essentially unrecoverable scenario.  Cancellation is a *one time event*, and as far as the parent is concerned, if the child/its context is canceled, the child is canceled...  
...but if the child then starts a new run for *any* reason (retry, cron, reset, etc), that new run is no longer canceled.  The parent has no way to know this has happened, and has no way to *re*-cancel the new child, so it can easily lead to the collection of workflows getting into an impossible state that it never recovers from.

Both cases are able to lead to unreliable behavior which can only use termination to stop, and for which no "safe" option exists.

After reviewing some customer issues and desires and thinking about things, we've settled on "cancel should guarantee that things stop".  Not necessarily in a timely manner, but that's fine.  And if a workflow wants to run behavior longer or larger than its current run can achieve, it has a workaround: start a new (likely child) workflow to do the cleanup.

# What happens now

So that's what this PR does, in a minimal / to-be-polished way so we can start running it for our stuck users while we flesh out tests and change other behaviors.

Currently that means our cancellation behavior is now:

| **CURRENT**    | **simple**                                | **retry**                                 | **cron**                                  | **retry+cron**                            |
|--------------:|-------------------------------------------|-------------------------------------------|-------------------------------------------|-------------------------------------------|
| **success**   | success                                   | success                                   | success                                   | success                                   |
| **cancel**    | canceled                                  | canceled                                  | canceled                                  | canceled                                  |
| **retryable** | (n/a, fatal)                              | canceled<br>recorded error (details only) | (n/a, fatal)                              | canceled<br>recorded error (details only) |
| **fatal**     | canceled<br>recorded error (details only) | canceled<br>recorded error (details only) | canceled<br>recorded error (details only) | canceled<br>recorded error (details only) |
| **continue**  | canceled<br>(no details)                  | canceled<br>(no details)                  | canceled<br>(no details)                  | canceled<br>(no details)                  |
| **timeout**   | timeout                                   | timeout                                   | timeout                                   | timeout                                   |

And the new "details" entries cover whether or not an error's "details" (the custom encoded data, not reason or type) are saved.  Unfortunately the current cancellation event (and clients' API) does not allow recording all data, or any in some cases, so the original reason/message and error type are lost and are replaced with a canceled error.

Now, cancellation *always* ends workflows with the current run.  Returning a value will return that value, including in cron scenarios, timeouts are still timeouts (and they imply a possibly un-clean termination), and _all_ errors or attempts to continue-as-new will instead result in a canceled state.

# Future changes to make to finish this effort

With further changes to the clients and RPC/storage models, canceled errors will store more details about what was returned.  E.g. continue-as-new does not record what was *attempted* to be started, and other error types lose their "reason" (i.e. the message) and type but not details.  Pretty clearly this is sub-par, and we should be capable of reporting the actual return in full so it can be retrieved if needed.  This is also why returning a value now always ends in a completed state, so successful completions do not lose those values.

Prior to merging into master / a release, we may end up making this configurable (likely with a default of opt-out), to address both the sub-par information recording and the semantically-breaking behavior change.  Docs changes are also due, as well as some integration tests, client library changes (e.g. to make sure the test suite reflects the new behavior), etc.

Another gap to plug is that resetting a workflow does not "forward" the canceled state to the new run.  We should probably be treating cancellation like we do signals: cancel the new run if the current run is canceled.  This will ensure that you can reset a child and retain the parent's cancellation, so it'll very likely become the default behavior, but we'll allow overriding it.  Resets are manual actions, they can break the rules if desired.  And they can just manually cancel later if they decide they do want it.

And last and perhaps least: it's quite strange that continue-as-new does not retain cron config.  At least from the Go client.  I suspect it's just not adding to / pulling from the context correctly.

---
## [ShelbyHell/android_kernel_xiaomi_juice-R](https://github.com/ShelbyHell/android_kernel_xiaomi_juice-R)@[e0fed275fe...](https://github.com/ShelbyHell/android_kernel_xiaomi_juice-R/commit/e0fed275fe3b7badd521cdfc01ad639b54e7b39f)
#### Friday 2022-07-22 05:54:35 by Joonsoo Kim

mm/page_alloc: use ac->high_zoneidx for classzone_idx

Patch series "integrate classzone_idx and high_zoneidx", v5.

This patchset is followup of the problem reported and discussed two years
ago [1, 2].  The problem this patchset solves is related to the
classzone_idx on the NUMA system.  It causes a problem when the lowmem
reserve protection exists for some zones on a node that do not exist on
other nodes.

This problem was reported two years ago, and, at that time, the solution
got general agreements [2].  But it was not upstreamed.

[1]: http://lkml.kernel.org/r/20180102063528.GG30397@yexl-desktop
[2]: http://lkml.kernel.org/r/1525408246-14768-1-git-send-email-iamjoonsoo.kim@lge.com

This patch (of 2):

Currently, we use classzone_idx to calculate lowmem reserve proetection
for an allocation request.  This classzone_idx causes a problem on NUMA
systems when the lowmem reserve protection exists for some zones on a node
that do not exist on other nodes.

Before further explanation, I should first clarify how to compute the
classzone_idx and the high_zoneidx.

- ac->high_zoneidx is computed via the arcane gfp_zone(gfp_mask) and
  represents the index of the highest zone the allocation can use

- classzone_idx was supposed to be the index of the highest zone on the
  local node that the allocation can use, that is actually available in
  the system

Think about following example.  Node 0 has 4 populated zone,
DMA/DMA32/NORMAL/MOVABLE.  Node 1 has 1 populated zone, NORMAL.  Some
zones, such as MOVABLE, doesn't exist on node 1 and this makes following
difference.

Assume that there is an allocation request whose gfp_zone(gfp_mask) is the
zone, MOVABLE.  Then, it's high_zoneidx is 3.  If this allocation is
initiated on node 0, it's classzone_idx is 3 since actually
available/usable zone on local (node 0) is MOVABLE.  If this allocation is
initiated on node 1, it's classzone_idx is 2 since actually
available/usable zone on local (node 1) is NORMAL.

You can see that classzone_idx of the allocation request are different
according to their starting node, even if their high_zoneidx is the same.

Think more about these two allocation requests.  If they are processed on
local, there is no problem.  However, if allocation is initiated on node 1
are processed on remote, in this example, at the NORMAL zone on node 0,
due to memory shortage, problem occurs.  Their different classzone_idx
leads to different lowmem reserve and then different min watermark.  See
the following example.

root@ubuntu:/sys/devices/system/memory# cat /proc/zoneinfo
Node 0, zone      DMA
  per-node stats
...
  pages free     3965
        min      5
        low      8
        high     11
        spanned  4095
        present  3998
        managed  3977
        protection: (0, 2961, 4928, 5440)
...
Node 0, zone    DMA32
  pages free     757955
        min      1129
        low      1887
        high     2645
        spanned  1044480
        present  782303
        managed  758116
        protection: (0, 0, 1967, 2479)
...
Node 0, zone   Normal
  pages free     459806
        min      750
        low      1253
        high     1756
        spanned  524288
        present  524288
        managed  503620
        protection: (0, 0, 0, 4096)
...
Node 0, zone  Movable
  pages free     130759
        min      195
        low      326
        high     457
        spanned  1966079
        present  131072
        managed  131072
        protection: (0, 0, 0, 0)
...
Node 1, zone      DMA
  pages free     0
        min      0
        low      0
        high     0
        spanned  0
        present  0
        managed  0
        protection: (0, 0, 1006, 1006)
Node 1, zone    DMA32
  pages free     0
        min      0
        low      0
        high     0
        spanned  0
        present  0
        managed  0
        protection: (0, 0, 1006, 1006)
Node 1, zone   Normal
  per-node stats
...
  pages free     233277
        min      383
        low      640
        high     897
        spanned  262144
        present  262144
        managed  257744
        protection: (0, 0, 0, 0)
...
Node 1, zone  Movable
  pages free     0
        min      0
        low      0
        high     0
        spanned  262144
        present  0
        managed  0
        protection: (0, 0, 0, 0)

- static min watermark for the NORMAL zone on node 0 is 750.

- lowmem reserve for the request with classzone idx 3 at the NORMAL on
  node 0 is 4096.

- lowmem reserve for the request with classzone idx 2 at the NORMAL on
  node 0 is 0.

So, overall min watermark is:
allocation initiated on node 0 (classzone_idx 3): 750 + 4096 = 4846
allocation initiated on node 1 (classzone_idx 2): 750 + 0 = 750

Allocation initiated on node 1 will have some precedence than allocation
initiated on node 0 because min watermark of the former allocation is
lower than the other.  So, allocation initiated on node 1 could succeed on
node 0 when allocation initiated on node 0 could not, and, this could
cause too many numa_miss allocation.  Then, performance could be
downgraded.

Recently, there was a regression report about this problem on CMA patches
since CMA memory are placed in ZONE_MOVABLE by those patches.  I checked
that problem is disappeared with this fix that uses high_zoneidx for
classzone_idx.

http://lkml.kernel.org/r/20180102063528.GG30397@yexl-desktop

Using high_zoneidx for classzone_idx is more consistent way than previous
approach because system's memory layout doesn't affect anything to it.
With this patch, both classzone_idx on above example will be 3 so will
have the same min watermark.

allocation initiated on node 0: 750 + 4096 = 4846
allocation initiated on node 1: 750 + 4096 = 4846

One could wonder if there is a side effect that allocation initiated on
node 1 will use higher bar when allocation is handled on local since
classzone_idx could be higher than before.  It will not happen because the
zone without managed page doesn't contributes lowmem_reserve at all.

Reported-by: Ye Xiaolong <xiaolong.ye@intel.com>
Signed-off-by: Joonsoo Kim <iamjoonsoo.kim@lge.com>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Tested-by: Ye Xiaolong <xiaolong.ye@intel.com>
Reviewed-by: Baoquan He <bhe@redhat.com>
Acked-by: Vlastimil Babka <vbabka@suse.cz>
Acked-by: David Rientjes <rientjes@google.com>
Cc: Johannes Weiner <hannes@cmpxchg.org>
Cc: Michal Hocko <mhocko@kernel.org>
Cc: Minchan Kim <minchan@kernel.org>
Cc: Mel Gorman <mgorman@techsingularity.net>
Link: http://lkml.kernel.org/r/1587095923-7515-1-git-send-email-iamjoonsoo.kim@lge.com
Link: http://lkml.kernel.org/r/1587095923-7515-2-git-send-email-iamjoonsoo.kim@lge.com
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: celtare21 <celtare21@gmail.com>

---
## [abitmore/ml-cpp](https://github.com/abitmore/ml-cpp)@[4bc55b3d04...](https://github.com/abitmore/ml-cpp/commit/4bc55b3d04ebf5f2341ad75106e67ec3a7a3d3d9)
#### Friday 2022-07-22 06:54:49 by Tom Veasey

[ML] Logging enhancements plus compilation speed ups  (#2363)

Currently, logging requires one to manage wrapping up calls to many types in core::CContainerPrinter::print.
It would be nice if the logging experience was more streamlined. Another side effect is we ended up including
core/CContainerPrinter.h very widely, in many cases for LOG_TRACE statements which are compiled away
anyway. It would be nice to avoid this.

This PR introduces a pseudo stream manipulator CScopePrintContainers. This is dropped into our logging
macros so that all log lines simply get containers printed automatically. This approach first detects (at compile
time) whether types can be written directly to a std::ostream and uses this approach in preference. I also fixed
some obvious silly inefficiencies in CContainerPrinter. One might ask why not just specialise operator<< for
std::ostream and containers in the std namespace? I did in fact try this, but it turns out other libraries tend
to do this and you can easily get ODR violations. I hit this exact problem because libtorch does this and I
couldn't then compile pytorch_inference.

Separately, our compile times given the total LOC are rather long. One culprit is logging. Just including
CLogger.h adds around 70k lines to the output of the preprocessor and, for my setup, 0.4s for this step
alone to the compile time of file. Therefore, I've also started addressing some of the bottlenecks. I've migrated
LOG_TRACE to really discard the code altogether. This means we can have a special CLoggerTrace.h which
only optionally includes CLogger.h if we're not compiling with EXCLUDE_TRACE_LOGGING. (I think the
improved build times warrant only finding out later if we break a log line and anyway many things now just
print automatically, so this should be harder to do.) I also add CMemoryFwd.h to avoid including CMemory.h
too widely. This includes a lot of STL headers. Finally, I migrated CLoggerThrottler to a pimpl and moved
some obvious other details out of headers. The upshot for for my dev setup is 15% speed up to build everything.

---
## [WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/FEDERAL-USE-AND-DISTRIBUTION-ONLY](https://github.com/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/FEDERAL-USE-AND-DISTRIBUTION-ONLY)@[b977737635...](https://github.com/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/FEDERAL-USE-AND-DISTRIBUTION-ONLY/commit/b977737635ef99b6bbfa8faba9f72c57a4d3a76a)
#### Friday 2022-07-22 07:19:06 by WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER

$$$$$$$$$$$$$$$$$$$$$ AIRPLANE CABARET[40-17G]

$$$$$$$$$$$$$$$$$$$$$ AIRPLANE CABARET[40-17G]
AIRPLANE CABARET[40-17G]
    JULY 10 2022
   
    0149 AM EST, OUTBOUND.
    [ TEL. 917-378-3467 to 1-855-5324 on JULY 10 2022 CONVERSATION ]
    [ TIME 329 SECONDS ]



https://saaze2311prdsra.blob.core.windows.net/clean/84a87a115a09ed1182e5000d3a98e815/917-378-3467%20to%201-855-5324%20on%20JULY%2010%202022%20conv%20time%20329%20seconds.png

   
0212 EST,  OUTBOUND
INTER-AGENCY REGISTRATION
     
AS FOR MY DEPARTMENT MEMBERS,
WERE ADDRESSED AS FOLLOWS:
    JOB TITLE:      FELON.   
    ADDRESS:        JUST ENOUGH SPACE FOR CERTAIN NYSCEF LINKS, AND OTHER THINGS,
                    LIKE MY LINKED PROFILE, WHICH IS ALSO NOT AN XPS DOCUMENT THAT I CREATED.

     
I REGISTERED MYSELF WITH ONE OF THESE AGENCIES..., BUT AS STATED PRIOR
   
 CALL THE NUMBER ABOVE AND USE CODE #50074 90849565 NYSCEF 153974 2020 DOCKETS 309-315
    THAT IS TO GET THE CONVERSATION STARTED WITH THEM DIRECTLY.
   
    - IF YOU ARE UNSURE WHICH SELECTION IS BEST SUITED FOR YOURSELF, PLESE MAKE CERTAIN YOU LISTEN TO ALL AVAILABLE CHOICES, AND OPTIONS BEFORE YOU MAKE THE WRONG CHOICE, IT'S NOT WORTH IT.
    - I CAN TELL YOU THE 1ST OPTION HAS NOT CHANGED, AND ONLY SINCE THE 10TH OF JULY.

        https://saaze2311prdsra.blob.core.windows.net/clean/84a87a115a09ed1182e5000d3a98e815/917-378-3467%20to%201-855-5324%20on%20JULY%2010%202022%20conv%20time%20329%20seconds.png



TO RESTATE, I WAS APPROVED AS FOLLOWS AND USING THE FOLLOWING INFORMATION, AND I AM NOT IN PRISON, JAIL, AND HAVE NOT BEEN ARRESTED.
- SO PLEASE ACT RESPECTFULLY IF YOU DO DECIDE TO CALL, THEY WILL TREAT YOU FAIRLY AND VERY DECENTLY AFTER EVADING THE LAW FOR TWO YEARS...

selective service number
https://saaze2311prdsra.blob.core.windows.net/clean/8d7da71b4d09ed1182e5000d3a98e336/RegAck-8408404633.pdf

CV profile (endurance 50074 90849565)
https://saaze2311prdsra.blob.core.windows.net/clean/8611ef054d09ed1182e5000d3a98ee53/BarisDincerResume(Combine).pdf

RESUME and CV
https://saaze2311prdsra.blob.core.windows.net/clean/80c50da24c09ed1182e5000d3a98e336/BD_GS_RESUME2022.pdf


OR JUST MY SSN. I DON'T RECALL - JUST CALL THEM AND ASK, IF YOU HAVE ANY QUESTIONS.

***** THE HOUDINI AIRCRAFT CABARET

***** AKA "1212 58-58" (check that in the receipts,= ---- $58.58 - ]

all need to be refunded for REASONABLE CAUSE and CARRIED INTEREST ON RESERVE from EARLIER.
    > THANK YOU FOR THE OFFER MR. OFFICER (UN-NAMED)
    > WHEN I AM INSTRUCTED TO, I KNOW WHICH BUILDING I NEED TO PROCEED TO.
    > SO PEACEFULLY, GO ABOUT YOUR AFFAIRS AND I WILL ACT ACCORDINGLY
    > CLEARLY THIS IS NOT MY FIRST RODEO, IF ANYONE IS ON THIS THREAD WHO SHOULDN'T BE - I WOULD NOT EXPECT YOU TO NOTIFY ME -

AFTER ALL, I CAN'T DO EVERYTHING.
+ ITS JUST THE INTERNET...


(https://saaze2311prdsra.blob.core.windows.net/clean/09acb0e95109ed1182e5000d3a98e0dc/LOAN-50074-6%20PROPERTIES%20WITH%20NO%20CERTIFICATES%20OF%20OCCUPANCY%20TO-%20%20LEGALLY%20COLLECT%20RENT.jpg)

USC TITLE 18.225 VIOLATED IN NYSCEF MATTER 153974/2020
111 - 119 SULLIVAN STREET.
    TAX BLOCK 503, LOT 8
    TAX BLOCK 503, LOT 9
    TAX BLOCK 503, LOT 10
    TAX BLOCK 503, LOT 11
    TAX BLOCK 503, LOT 12


2020.08.08 -- TAX evasion -- 6MM - USC 18.225 KNOWN - UNLAWFUL conduct 18.4 - 18.3 - 18.2
>> OGIS -- is all ARCHIVED.AND THIS OBSTRUCTED THE STATEMENTS BY CIK FILER 93715 AND ALSO CIK FILER 1516523 BY PRICE WATERHOUSE COOPERS (A PUBLICLY TRADED AUDIT FIRM)

TCR5 INDEX HAS ALL OF THE INFORMATION WHICH THE OTHER AGENCIES NEED TO ASSESS, AND HAD I COMMITTED ANY ACT OTHER THAN TO BE APPROVED AFTER CONTACTING THE MAGIC MUFFIN AGENCY AND HAVING A 5 MINUTE DISCUSSION WITH THE GENTLEMAN, ,ALSO USED THE SAME CODES I USED IN 2012, AND AGAIN IN THE THREE MESSAGE AFTER I MADE SURE THAT THE LEWISOHN HALL WAS LOCKED DOWN, AND EVEN TAPED THE DOOR SO THE OTHER STUDENTS KNOW, JUST BECAUSE IT IS AN IVY LEAGUE SCHOOL - DOESN'T MEAN THEY HAVE "SPECIAL PRIVILEGES TO VIOLATE MY PRIVACY AND CIVIL RIGHTS FOR TWO YEARS, AND VIOLATE BANK AND SECURITIES LAWS WITHOUT REPRESCUSSION" .

>> I WILLFULLY AGAIN, CONSENTED TO PARTICIPATE

https://saaze2311prdsra.blob.core.windows.net/clean/a2beb57c5209ed1182e5000d3a98ec7c/2020.08.08%20--%20TAX%20evasion%20--%206MM%20-%20USC%2018.225%20KNOWN%20-%20UNLAWFUL%20conduct%2018.4%20-%2018.3%20-%2018.2-OGIS.pdf

WITH 30-YEAR TERMS AND OTHER SEVERE CONSEQUENCES
-- EVEN THEIR COUNSELORS HAVE AVOIDED TO THE RISKS AND TAX RISKS
    - AS IMPLIED -
    -    HELD BY THE WHOLE LIFE POLICY HOLDERS AND INVESTORS OF STATE FARM

https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=19MVPFXy0G0QvnmRLGpYIQ==

*** see also: voicemail from PAUL REGAN, counselor in NYSCEF MATTER 153974/2020
*** TO FOLLOW ME TO THE END OF THE WORLD, OR MY FATHER...
*** IS UNETHICAL HOWEVER AS IMPLIED TO INTIMIDATE OR CONSPIRE TO OR REPLACE A SUBJECT WITH ANOTHER
*** IS UNLAFUL, AND WAS RECORDED ANDP ROVIDED TO ME BY MY FATHER
*** WHICH IS THE ONLY REASON WHY I HAVE A COPY OF THAT VOICEMAIL.


[2/16/2022 11:57 PM]

https://github.com/BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER/files/8608620/000000000000000000000000000000000000000000000.pdf

*** SOMEONE ALSO HAD A PROBLEM WITH THE EMAIL ADDRESS --- AND HAD IT DELETED.

 --------
 --------

JUST LIKE THE ONE THEY DELETED ON DECEMBER 19TH, 2021
 --------
 --------

Lewisohn Hall
Address: Columbia University, USA
2970 Broadway, New York, NY 10027

USC Title 18. § 3 - Accessory after the fact
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=cve65PXNBCtdxjJFkfwUnw==

FELONY- MAY BE A LIFE SENTENCE OR WORSE.
USC TITLE 18 VIOLATIONS 18.225
LOAN FOR $6 MILLION DOLLARS WAS OBTAINED USING MISLEADING AND

https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=au8qh7Dn66hrVmJ9DX_PLUS_bdg==


NOTARIZED ON MAY 13TH, 2020
AS FILED: NEW YORK COUNTY CLERK 08/09/2020 02:24 AM INDEX NO. 153974/2020

https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=au8qh7Dn66hrVmJ9DX_PLUS_bdg==

---
## [neebe000/android_kernel_xiaomi_mt6785](https://github.com/neebe000/android_kernel_xiaomi_mt6785)@[0889a65fda...](https://github.com/neebe000/android_kernel_xiaomi_mt6785/commit/0889a65fda526d077573f25a226ac003fe36fb81)
#### Friday 2022-07-22 08:14:41 by Peter Zijlstra

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
Signed-off-by: neebe000 <neebexd@gmail.com>

---
## [lorc/xen](https://github.com/lorc/xen)@[be4eed38f9...](https://github.com/lorc/xen/commit/be4eed38f9a53e8194344ec96673aebec3bb3650)
#### Friday 2022-07-22 08:17:59 by Oleksandr Andrushchenko

xen/pci: arm: add stub for is_memory_hole

Add a stub for is_memory_hole which is required for PCI passthrough
on Arm.

Signed-off-by: Oleksandr Andrushchenko <oleksandr_andrushchenko@epam.com>
---
OT: It looks like the discussion got stuck. As I understand this
patch is not immediately needed in the context of current series
as PCI passthrough is not enabled on Arm at the moment. So the patch
could be added later on, but it is needed to allow PCI passthrough
to be built on Arm for those who want to test it.

Copy here some context provided by Julien:

Here a summary of the discussion (+ some my follow-up thoughts):

is_memory_hole() was recently introduced on x86 (see commit 75cc460a1b8c
"xen/pci: detect when BARs are not suitably positioned") to check
whether the BAR are positioned outside of a valid memory range. This was
introduced to work-around quirky firmware.

In theory, this could also happen on Arm. In practice, this may not
happen but it sounds better to sanity check that the BAR contains
"valid" I/O range.

On x86, this is implemented by checking the region is not described is
in the e820. IIUC, on Arm, the BARs have to be positioned in pre-defined
ranges. So I think it would be possible to implement is_memory_hole() by
going through the list of hostbridges and check the ranges.

But first, I'd like to confirm my understanding with Rahul, and others.

If we were going to go this route, I would also rename the function to
be better match what it is doing (i.e. it checks the BAR is correctly
placed). As a potentially optimization/hardening for Arm, we could pass
the hostbridge so we don't have to walk all of them.
---

---
## [ammarfaizi2/linux-block](https://github.com/ammarfaizi2/linux-block)@[0c80f9e165...](https://github.com/ammarfaizi2/linux-block/commit/0c80f9e165f8f9cca743d7b6cbdb54362da297e0)
#### Friday 2022-07-22 08:21:10 by Sudeep Holla

ACPI: PPTT: Leave the table mapped for the runtime usage

Currently, everytime an information needs to be fetched from the PPTT,
the table is mapped via acpi_get_table() and unmapped after the use via
acpi_put_table() which is fine. However we do this at runtime especially
when the CPU is hotplugged out and plugged in back since we re-populate
the cache topology and other information.

However, with the support to fetch LLC information from the PPTT in the
cpuhotplug path which is executed in the atomic context, it is preferred
to avoid mapping and unmapping of the PPTT for every single use as the
acpi_get_table() might sleep waiting for a mutex.

In order to avoid the same, the table is needs to just mapped once on
the boot CPU and is never unmapped allowing it to be used at runtime
with out the hassle of mapping and unmapping the table.

Reported-by: Guenter Roeck <linux@roeck-us.net>
Cc: Rafael J. Wysocki <rafael@kernel.org>
Signed-off-by: Sudeep Holla <sudeep.holla@arm.com>

--

Hi Rafael,

Sorry to bother you again on this PPTT changes. Guenter reported an issue
with lockdep enabled in -next that include my cacheinfo/arch_topology changes
to utilise LLC from PPTT in the CPU hotplug path.

Please ack the change once you are happy so that I can get it merged with
other fixes via Greg's tree.

Regards,
Sudeep

Acked-by: Rafael J. Wysocki <rafael.j.wysocki@intel.com>
Link: https://lore.kernel.org/r/20220720-arch_topo_fixes-v3-2-43d696288e84@arm.com
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[590ecdcb1c...](https://github.com/mrakgr/The-Spiral-Language/commit/590ecdcb1c5cb1311ec32b242add386bca34818b)
#### Friday 2022-07-22 10:39:36 by Marko Grdinić

"9am. I am up. I am getting bored of BG2. Ever since I crossed 3m exp and got summon dark planetar the game has become dull. But that is good since I will channel some of the extra energy into programming. Any mail?

Kalepa is really spamming my inbox, what the hell? Anyway, I just have the usual recruiter spam urging me to grab a slot. Nevermind that.

You know what...maybe I should grab a bunch of slots. Right now I am bored out of my mind waiting for the cards to get here. In the worst case, I'd just fail the interviews and have to apply at a later date.

Making them wait a week is one thing, but several weeks?

I can always just make them wait before I take the offer itself while I get my shit in order. Not exactly what I planned, but it is fine. I certainly do not need to finish the AWS Cloud project before I do interviewing, just before I start the job.

9:25am. Had a power outage 15m ago.

What I wanted to say, let me do my morning chililng, a little bit of Blazor and then I'll grab the slots. I'll spread them out over next week.

9:30am. I think I've lasted long enough. I am just too bored without anything significant going on. I definitely do not have the will to do solo projects like in the past years. I want to start grinding money. I need a proper goal. With money I can computers with which to do ML research. I can upgrade my own rig as well. I can work towards getting my own DALLE, once I have that Heaven's Key can start for real. Right now, I can't do anything.

9:40am. Let me continue for a while longer and then I will...actually forget Blazor. Let me grab the slots first. After that I will start the course.

10am. Slots, slots...

Ok, let me write them down one by one.

https://time.is/GMT+2

I am really confused. Why does my own clock have the exact time for GMT+2 when I set it to UTC+1. Those two should be the same.

10:10am. Nevermind that. If I google 'current time in Berlin' it shows the same thing as in Zagreb. I won't worry about it.

Kalepa: 10am - 7pm, Monday, July 25th (avail)

I thought I could just pick from free slots, but it seems this is a two stage process. Let me move on to the next. I'll pick this one on Tuesday and so on.

Neurolabs: 11:15 am – 12:00 pm, Tuesday, July 26, 2022 (booked)

That is two down. Let me move on to the next.

Alan: 5:15 PM - 6:00 PM (CEST), Tuesday Jul 26, 2022 (booked)

AssemblyAI: 20:30 - 20:45, Wednesday, July 27, 2022 (booked)

Generally Intelligent: 21:30 - 22:00, Thursday, July 28, 2022 (booked)

10:30am. The rest of them had dates given out. Kalepa is the first one that just let me pick availability. Let me organize them:

///

Kalepa: 10:30am-10:50am CEST, Monday, Jul 25, 2022
Neurolabs: 11:15 am – 12:00 pm, Tuesday, July 26, 2022
Alan: 5:15 PM - 6:00 PM (CEST), Tuesday Jul 26, 2022
AssemblyAI: 20:30 - 20:45, Wednesday, July 27, 2022
Generally Intelligent: 21:30 - 22:00, Thursday, July 28, 2022

///

The Generally Intelligent one is really late. There were slots in other days, but they were literally at midnight times. Well, 9:30pm is still fine.

This is good enough. Next week regardless of when the card arrive I'll have something to look forward to.

Now, that I've had a bit face to face experience, in this intro interview, I know that all I have to do is shut up, nod along and just let the other guy talk. Oh right. The AssemlyAI guys when asking me for extra info specifically asked for AWS experience. There was a bunch of database stuff too, so if I want to be a pro pogrammer, I should get familiar with those.

On Tuesday, I have two interviews. It couldn't be helped.

10:40am. This was handled well, I really couldn't just the initial stage hang for much longer. Nobody is going to wait for me to get ready. It should not be too hard to get a pass during this initial stage.

Now, let me archive those emails.

Oh got a reply from Kalepa. Let me replace that time with the exact one. At 10:30am on Monday. Hopefully I won't end up sleeping till 11.

10:50am. Hadn't gotten a link from Alan. I guess I'll just email the guy to send me an invite when the time comes...I checked the link and it says they'll get back to me.

Ok, good.

That takes care of that. Now I am free of this chores and can look towards something interesting happening in the near term.

11:20am. Had to take a break.

https://www.strongtowns.org/journal/2022/7/5/heres-why-we-respond-in-force-to-one-amtrak-crash-while-ignoring-thousands-of-daily-car-crashes
> I am going to give you the number, but first I want to go back to the combat deaths. There were 3,481 combat deaths in Operation Iraqi Freedom. Since 9/11, there have been over 30,000 military suicides.

30k suicides? Damn! The US military will off itself before its enemies get a chance.

Let me finish reading this and I will start.

11:35am. Had to do some chores. Let me finally start.

Blazor!

I am bored to death of it

https://youtu.be/QKr1HPq6YlI
Learn Blazor (.NET 6) - CRUD Operations, EF Core and Blazor Fundamentals

Let me try implementing some of that shit.

https://youtu.be/QKr1HPq6YlI?t=6305

Let me backtrack and I will do the bind prop.

https://youtu.be/QKr1HPq6YlI?t=4293

Thankfully it has a TOC in the description.

https://youtu.be/QKr1HPq6YlI?t=4353

Let me freeze it here. I'll use this as a reference.

First let me add a new item to the navbar.

11:50am. Focus me. Had to to some extras again.

12:15pm.

```razor
@page "/bindprop"

<PageTitle>Bind Properties</PageTitle>

@using TangyWeb_Server.Data

<h4>Product</h4>

<table class="table">
    <tbody>
            <tr>Name:   @prod.Name</tr>
            <tr>Active: @prod.IsActive</tr>
            <tr>Price:  @prod.Price</tr>
            <tr>This product is: @isActive(prod)</tr>
    </tbody>
</table>

Active: <input type="checkbox" checked=@prod.IsActive /> <br />
Price: <input value=@prod.Price/> <br />

@code {
    string isActive(ProductProp prod) => prod.IsActive ? "Active" : "InActive";

    ProductProp prod = new ProductProp
        {
            Name = "qwe",
            IsActive = true,
            Price = 10.54M
        };
}
```

Now that I am actually doing something, it is a lot more fun. I somehow got the controls without looking at any docs or the video. Now how do I get the bindings to work?

I can't remember, I'll have to look at the video. Just for a little bit.

https://youtu.be/QKr1HPq6YlI?t=4288

Oh I see.

12:25pm. Now I am trying to bind the product to the checkbox.

```razor
Active: <input name="checkb" type="checkbox" checked=@prod.IsActive onchange="" /> <br />
```

I am not sure what to do here. I vaguely remember him using the name, but...

I have no idea. I do not know how to pass in the control into onchange. I do not know how to use the bind-value to control the checked property.

...Let me jsut watch the video.

https://youtu.be/QKr1HPq6YlI?t=4483

Hmmm, I see.

12:35pm. https://youtu.be/QKr1HPq6YlI?t=4515

There is no need to do this. Just passing in a boolean directly works fine.

12:35pm. https://youtu.be/QKr1HPq6YlI?t=4589

Let me watch from here and then I'll do the assignment. There are 9 assignments in total, and my goal should be to go through them. After I do that, I can consider myself as having some Blazor skills.

Let me stop here for breakfast first."

---
## [Akbor002/Akbor002](https://github.com/Akbor002/Akbor002)@[7201cf7ddf...](https://github.com/Akbor002/Akbor002/commit/7201cf7ddfb37077f23f4f3bd9623ed64ad364ea)
#### Friday 2022-07-22 10:52:40 by Akbor002

.__f.CPP

// FuckYou

#include <iostream>

int main() {
    std::cout << "Fuck You";
    return 0;
}

---
## [Blizarre/dwm](https://github.com/Blizarre/dwm)@[67d76bdc68...](https://github.com/Blizarre/dwm/commit/67d76bdc68102df976177de351f65329d8683064)
#### Friday 2022-07-22 10:53:48 by Chris Down

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
## [Withicality/GDBrowser](https://github.com/Withicality/GDBrowser)@[9e8d435627...](https://github.com/Withicality/GDBrowser/commit/9e8d43562709c5dbc940aefa49949ad467ca8511)
#### Friday 2022-07-22 11:08:33 by GDColon

UNLEASH THE OBJECT FOLDER MOTHERFUCKERS

oops i dropped all these OBJECTS that aren't assembled correctly but who gives a shit i don't this is just for my google sheets thing

---
## [Fabizocker456/test](https://github.com/Fabizocker456/test)@[280152eac0...](https://github.com/Fabizocker456/test/commit/280152eac067db1fd288dcd000767cf30b94fe4e)
#### Friday 2022-07-22 11:27:23 by Fabizocker456

idk

Speaking of love, one problem that recurs more and more frequently these
days, in books and plays and movies, is the inability of people to communicate
with the people they love; Husbands and wives who can't communicate, children
who can't communicate with their parents, and so on.  And the characters in
these books and plays and so on (and in real life, I might add) spend hours
bemoaning the fact that they can't communicate.  I feel that if a person can't
communicate, the very _____least he can do is to shut up!
		-- Tom Lehrer, "That Was the Year that Was"

---
## [gradle/gradle](https://github.com/gradle/gradle)@[b95c1c2447...](https://github.com/gradle/gradle/commit/b95c1c2447d4d05e3a21018d9d0011a77d6049f9)
#### Friday 2022-07-22 12:24:42 by bot-gradle

Merge pull request #20658 Provide better experience when asserting the presence of multiple output lines in integration tests

This PR is the result of pain points encountered when writing assertions for: https://github.com/gradle/gradle/pull/19561.  Early investigations are here: https://github.com/gradle/gradle/issues/19608.

These changes cause the exception output to print _only_ twice, and make the results of a failed test assertion much easier to interpret by suppressing Groovy's power assertions, which tend to be extremely difficult to interpret when searching for large blocks of text inside of nested structures composed of large blocks of text.

It also adds new formatting options for asserting comparisons on multiline blocks which can produce clearer output.

To see an example, in `OutgoingVariantsReportTaskIntegrationTest` change line 1074 to 'Elements of runtime for the main variant' and compare the [current results in master](https://gist.github.com/tresat/1d49e1c41cfcd265228009dfeea8a0f5), to [the results in this branch](https://gist.github.com/tresat/477d9ce1ba46d6c2edbe5abcafedfd7c) after changing the `assertOutputContains` call to the new `assertOutputContainsLines` method:
- The meaningful output is only duplicated once
- The expected lines don't clutter the output when they match
- The mismatched line(s), and their line number location(s) in the actual output is highly visible - in the the case the actual output being searched is many lines, this supports copying that output into a text editor and quickly jumping to the problem area
- The differences in mismatches lines are highlighted with the JUnit comparison failure logic - within only the mismatched lines, NOT the entire output - this makes it MUCH easier to see where the problem lies
- If there are multiple potential locations in a long output block that almost match (the same number of expected lines mismatch), then **all** the potential matches will be printed in this fashion
- If an exact match exists, this should run quickly, to not slow down testing.  Upon failing to match, the performance of building this list of matches upon failure relies on some nested loops, which in practice shouldn't matter too much, unless the arguments are really tailored to make that happen, which I don't think is very likely in real-world usage.

This is accomplished by throwing exceptions which subclass `SpockException`, the root exception type thrown by the new `ExhaustiveLinesSearcher` class which powers the new search.  The new classes likely need some additional Javadoc and maybe some further cleanup, but I didn't want to do too much bikeshedding before demo-ing the approach I want to take and getting some feedback.

This change also:
- Overrides `toString()` on intermediate types (`GroupedOutputFixture` and `GroupedTaskFixture`) to simplify output when these new methods are **not** used.
- !Add a `noPowerAssert` method to `AbstractIntegrationSpec` [for use in suppressing power assertion output in an ad-hoc manner](https://gist.github.com/tresat/716208856bbe01ed827c2aec5a847266).~ Removed, people can manually implement this method in a test if desired.
- Adjusts existing test machinery in `OutputScrapingTestResult` to avoid duplicating gradle output upon failure more than once.
- ~Adds a dep on Google Truth to allow for optional git-like difference output.  This is **not** the default, because I think in the common case it is less readable, and it will only find a single place where the potential match might be, and it won't highlight the differences within the mismatched lines as well.~

### Questions
- ~I needed to ignore keys in `verification-metadata.xml` to add the Google Truth dependency and get the build to work.  This doesn't seem right, can someone who understands this better explain what I need to do here.  Alternately, Sterling suggested just copying the entire `DiffUtils` class (which surprisingly doeesn't import anything else from the Truth project), so this is also an option.~ Class duplicated
- ~To what extent should I replace existing test code using `result.groupedOutput.task(":myTask").assertOutputContains` to search for big blocks of text (for example, in `OutgoingVariantsReportTaskIntegrationTest`) with this new method?  The expectation is that anything passing using the old method should also pass with the new method, and test run time should not be meaningfully affected.~ We don't want to change any existing expectations, or allow commits with "formatting options" for output assertions.
- ~Is it okay to deprecate `assertOutputContains` without replacing it?~ Won't do.

### Additional Work
- A likely common failure case is the additional or subtraction of a single missing line of text.  The alternate git unifiedDiff algorithm can provide output that is potentially more clear in this case.  I might experiment with changing `PotentialMatch`'s output to check for this special case and display it differently, to spare the reader from having to mentally compute this.

Co-authored-by: Sterling Greene <sterling@gradle.com>

---
## [Saber1990Sabre1990/--](https://github.com/Saber1990Sabre1990/--)@[d7d3ea7680...](https://github.com/Saber1990Sabre1990/--/commit/d7d3ea7680635e2b217e192e40e93ac81dc2d561)
#### Friday 2022-07-22 13:35:50 by Saber1990Sabre1990

Romantic-talk-9ba91.web.app

Romantic love thoughts for lovers and love letters written on it love phrases, poems and judgment about life

 This application includes the most wonderful images of love, love, romance and love letters written on it with love phrases and sad poems, as well as you can share them with your lover or sweetheart or put them as pictures, this application has a large collection of romantic love thoughts and sad expressive thoughts for the lover or beloved and  As well as pictures of romantic poetry and pictures of sad reproach and romantic love letters, you will also find (yen) pictures of love with romantic words and others written on it words and phrases about love and separation
 This application enables you to save images in your phone.
 Sad, painful words and phrases in pictures that will make you stronger than before, share them with friends to benefit others and strengthen their personality in love and separation.
 The most beautiful sad phrases Sadness is one of the strong feelings that control a person, and he needs to reveal it when you control him.  What trembles in his chest, trying to get rid of his pain. Sad love words We remind you of some simple words and thoughts printed in the nature of sadness and pain in the hearts of lovers.
 Pictures and through carrying a lot of things that can deliver messages to your lover that you are unable to deliver, in pictures is the easiest way to express and communicate with others.  It is the highest degree of love, love and passion, short romantic words. Nice and beautiful words when it comes from a person who is dear to us and close to us as much as the lover. It has another taste and color, and here you will find short romantic words.  ;  The person who loves you reprimands you from the intensity of his love, and his fear of losing you, as many loved ones admonish each other for various reasons such as desertion, or not asking about him.
 Beautiful words of love for the lover, feelings are the only thing that no one can control, and when feelings of love attack you, you cannot deter or control them, and then you do all the things that make you happy, and make your partner happy, to be at the top of happiness, and this is of course  When the feelings are real and sincere, and one of the ways to declare love, and begin to reveal it, is the distinctive words and phrases that we will mention some of them together.  Never because it is like a cold response that gets tired and sick, and here in this application you will find words of love and tenderness.  Life is a long road full of barriers and in it we learn beautiful lessons and lessons, and in our application, I have collected beautiful and expressive words for you about life. Longing for a lover is one of the difficult things for people and how beautiful life is when they meet.  Anyone and because social networking sites have become part of the daily routine of every person, it has become common to express feelings and feelings on the arenas of these virtual sites by publishing a sad picture bearing words expressing sadness, separation and separation.
 Words about longing for the beloved, no matter how many days and years separate us, and no matter how estrangement and distance is our path, but this will not prevent or reduce the extent of my longing and nostalgia for you.  ..
 It is the most beautiful human feelings and the sweetest relations that bind people and connect them, as it is the motivation for life in the first place.  A wonderful and renewed application on a daily basis to enjoy the best and newest romantic images, which are shareable on all social networking sites, and you can save them in the memory of the devices with ease through the professionalism of the application and the simplicity of its use. I love you forever, the most beautiful thoughts about love. Love is an easy word for some people, but it contains  A great meaning that no one can imagine, love is not only written words, but it is an act and a feeling from the depths of the heart. Here are some of the most beautiful thoughts of love emanating from the heart, which were written to suit the emotional situation of lovers.

---
## [Crakenar/WeightApp](https://github.com/Crakenar/WeightApp)@[84a42c861d...](https://github.com/Crakenar/WeightApp/commit/84a42c861da217ff4924e48ac7151ba92657ba81)
#### Friday 2022-07-22 14:46:04 by Teo Berguerre

fuck you tailwind installation my ass not working FUCK YOU

---
## [DarkMoonPlayz1/lua-script-testing](https://github.com/DarkMoonPlayz1/lua-script-testing)@[8f531063c5...](https://github.com/DarkMoonPlayz1/lua-script-testing/commit/8f531063c561f427c99cd90252c1802a708c8b03)
#### Friday 2022-07-22 15:21:28 by DarkMoon

Updated README.md

I'm bad at explaining shit like how to install shit on your god damn potato pc

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[b6f723bbfa...](https://github.com/mrakgr/The-Spiral-Language/commit/b6f723bbfae1abc5fbe6fadbb834959827d0065d)
#### Friday 2022-07-22 16:49:08 by Marko Grdinić

"12:55pm. Oh, Otome Survival got updated.

1:20pm. https://re-library.com/translations/hero-king/volume-6/chapter-245-15-year-old-inglis-the-dragon-god-and-the-elder-king-18/

Let me just read this and I will resume.

1:45pm. Time to resume. Let me pour some water over myself and I will get started. It is 35C outside, and probably just as much in my room if not more. This heat wave is quite something. I've been meaning to buy AC for 1.5 decade at this point. Maybe next year will be the charm.

2pm. Let me resume for real. Time to watch that part.

https://youtu.be/QKr1HPq6YlI?t=4933

Now that I think about it, this is pretty complicated. He...actually does the selection need to be by string?

https://youtu.be/QKr1HPq6YlI?t=4956

Let me freeze it here. I'll try immitating using it as reference without necessarily writing every step by hand. This is the fun part of following a course like this.

```
Product Properties: <select @bind=selectedProp>
    @foreach (DemoProductProp prop in prod.ProductProperties)
    {
        <option value=@prop>@prop.Key</option>
    }
</select>
```

It really does need to be a string. I am getting an exception.

2:30pm. https://stackoverflow.com/questions/3518002/how-can-i-set-the-default-value-for-an-html-select-element

```html
<option value="" selected disabled hidden>Select the property.</option>
```

This is a good way of doing it.

2:40pm. Focus me. I've implemented the thing, good for me. Let me resume the course.

2:50pm. Had to cool myself down again. After a heat wave like this, once the cold weather rolls in, it will be the most pleasant thing in the world.

3:30pm. This has gotten me thinking. Let me check something out in Spiral. I want to see whether void arrays can be put into layouts properly.

```
Error trace on line: 1, column: 10 in module: c:\Users\Marko\Source\Repos\The Spiral Language\Spiral Compilation Tests\compilation_tests\tutorial1\main.spi.
inl main () =
         ^
Error trace on line: 2, column: 5 in module: c:\Users\Marko\Source\Repos\The Spiral Language\Spiral Compilation Tests\compilation_tests\tutorial1\main.spi.
    inl x : heap (a i32 ()) = heap (create 1)
    ^
Error trace on line: 2, column: 31 in module: c:\Users\Marko\Source\Repos\The Spiral Language\Spiral Compilation Tests\compilation_tests\tutorial1\main.spi.
    inl x : heap (a i32 ()) = heap (create 1)
                              ^
Compiler error: Type not supported in the codegen.
Got: YB
```

Hmmm, it seems not correctly.

3:40pm. I can't figure out the flow. I need a stack trace here. Just what is calling tyv on this?

```c
static inline void HeapRefcBody0(Heap0 * x, REFC_FLAG q){
    int32_t z0 = x->v0;
    ArrayRefc0(z0, q);
}
```

This is not right, I think. Instead of an int, that should be an array.

```fs
let refcs = x.free_vars |> refc_change' (fun (i,t) -> refc_vars.Add($"{tyv t} z{i} = x->v{i};"); $"z{i}") "q"
```

Ah, this is where it is getting the t.

```fs
| YArray t -> Some $"ArrayRefc{(carray t).tag}({f (i,t)}, {c});"
```

I am passing in the wrong thing by accident here.

Ok, good.

3:50pm. Let me push this out.

3:55pm. OVSX is giving me trouble. I keep getting a 502 error.

...I tried it a few times and I keep getting the same error. It does not matter. Maybe I'll try it in a few days.

4pm. Let me get back on track. What was I supposed to be doing?

4:10pm. https://youtu.be/QKr1HPq6YlI?t=5473

What he wants me to work on now is that table.

Let me do that assignment.

4:30pm. I did it, but I can't figure out how to align it. Nevermind that for now. Also I can't figure out how to do the stripe. Styling is my weakness at the moment. Let me just watch the vid for that.

4:40pm. https://stackoverflow.com/questions/58221915/difference-between-bind-and-bind-value
> @bind is an override of @bind-value with the event set to "onchange".

Whops, I didn't realize this. If I had I would've been using it directly instead of having to set `onchange` every time. I thought `bind` was something else.

4:45pm. https://youtu.be/QKr1HPq6YlI?t=5935

Focus me. Let me do this assignment.

5pm.

```
@*<div>
    @foreach (var prod in prods)
    {
    <div>
        <h3>Product - @prod.Id</h3>
        Name - @prod.Name
        Show Properties : <input name="chk" type="checkbox">
        @*@if (true)
        {
            <div>
            Flavor - @prod.ProductProperties.Key
            </div>
        }*@

    </div>
    }
</div>*@
```

What the hell is going on. Somehow I broke everything.

Ah, crap. I named the damn page the same as the model.

5:45pm. Some watermelon got sent my way so I took a break. Let me finish the assignment. No way will I finish the course by the time the cards arrive at this rate, but that is fine.

5:55pm.

```
@page "/demoproduct"

<PageTitle>Demo Product</PageTitle>

<h2 class="text-primary">Demo Product</h2>

<table class="table border">
    <tbody>
        <tr>
            @foreach (var prod in prods)
            {
                <td class="">
                    <div>
                        <h3>Product - @prod.Id</h3>
                        Name - @prod.Name <br />
                        Show Properties : <input type="checkbox" @bind=prod.IsActive >
                        @if (prod.IsActive)
                        {
                            @foreach (var prop in prod.ProductProperties)
                            {
                                <div> @prop.Key - @prop.Value </div>
                            }
                        }
                    </div>
                <tr>
                    <button>Create</button>
                    <button>Delete</button>
                </tr>
                </td>
            }
        </tr>
    </tbody>
</table>

@code {
    DemoProduct [] prods = DemoProduct.Examples;
}
```

This took me way too long. I wasn't sure whether I should associate the is active to the stuff in the data itself, but then I realized it would be stupid not to. I don't know how to make use of HTML control names anyway. Again, I do not know how to deal with with the styling. If I take up webdev for real, I'd have to get familiar with this. I am not in a hurry. Webdev is all about the UIs. Fiddling around with this is not that bad. The work certainly would not be stressful.

https://youtu.be/QKr1HPq6YlI?t=5941

Let me check out how he does it.

6:05pm. https://youtu.be/QKr1HPq6YlI?t=6105

6:30pm. https://youtu.be/QKr1HPq6YlI?t=6296

I am really confused how he managed to get the buttons to fall into one row.

Forget it, I got it to work in a different way. It does not matter.

6:40pm. https://youtu.be/QKr1HPq6YlI?t=6452

Let me stop here for the day. I do not feel like watching it anymore.

6:45pm. I am so tired. This is not the fastest way to get through the course, but is definitely the most immersive. I am really learning Blazor right now, as well as HTML and CSS on the side. I wasn't that bored today.

I am happy with how today went. You can't ask for much more than this. I am kind of into Blazor now and do not really care about some of the design quibs that bothered me before. That is good too."

---
## [TheArctesian/obsidian](https://github.com/TheArctesian/obsidian)@[b30ea94d47...](https://github.com/TheArctesian/obsidian/commit/b30ea94d477e5e3e1bb5569809fb5b9142ec700e)
#### Friday 2022-07-22 17:48:58 by The Arctesian

Rm `$` from install.md

Lets do this the proper way shall we. The $ in front is kinda annoying, makes you have to ctrl a then ctrl d which is not fun and for nubes having to arrow all the way back is a pain

---
## [FormidableLabs/victory](https://github.com/FormidableLabs/victory)@[1aaa85fedc...](https://github.com/FormidableLabs/victory/commit/1aaa85fedc133f0f1d0c4e402fda23087a1232d6)
#### Friday 2022-07-22 19:21:37 by Ryan Roemer

Infra: Switch monorepo tooling to wireit and pnpm (#2345)

This PR is a big infrastructure overhaul to switch us from lerna + yarn to wireit + pnpm.

## Why?

Our existing setup of yarn + lerna has the following undesirable things:

1. Installs are slow on yarn
2. Yarn1 isn't updated anymore and simple package dependency updates don't work out of the box. It's a huge pain to update anything.
3. Lerna is getting old, and while the NX team has agreed to support it now, our build is (1) slow, (2) not cached at all, and (3) opaque as to what you need to run task-wise to support other tasks.

So, let's welcome PNPM + Wireit!

1. PNPM is a fast installer and well supported for normal things like package upgrades.
2. Wireit allows fine-grained subtask caching and dependency specifications to allow us to: (1) specify dependencies so when you run `pnpm run jest` all the other things that need to happen magically happen, (2) caches sub-tasks so things that don't have changed file inputs don't re-run, and (3) has full GH actions CI support!

To get a sense of how much faster our build has become take a look at the CI times for this branch in https://github.com/FormidableLabs/victory/actions?query=branch%3Ainfra%2Fpnpm-wireit++ -- when no input files change our CI times are about 1 minute. When some things change, a couple minutes. When all things (or our base scripts) change, we take the full hit of a comparable existing Victory CI time of like 15-16 mins.

For the average Victory developer, if you're working in just one package, you can just run the project-level `pnpm run check` and have like a full build and everything work reasonably fast without needing to know more or run subtasks!

## Check it out

```sh
$ npm install -g pnpm
$ pnpm install
# This will be slow!
$ pnpm run check

# ... but the second time will be super fast! And as you change things subsequent runs should be very fast!
$ pnpm run check
```

## Implementation notes

- High level:
    - **Dependency graph architecture**: All of our tasks now use wireit to identify and run/cache dependencies. So, if you want to run jest, you just run `pnpm run jest` and don't need to worry about "what else needs to be built?" before that.
    - **Parallelization**: To best use wireit, we've refactored our tasks to be more package-specific where possible. E.g., we run lint in incremental mode per-package meaning that both Wireit (at package level) and eslint (at file level within package) re-execute on the narrowest unit of "changed files" possible.

- Demos: The demos originally had imports from `victory*/src/index` (source) which wasn't efficient or consistent because the transitive deps on other victory packages was on built files. I refactored these to be normal `victory(-<NAME>)` imports using built files.

- `src`:
    - Since we did a "fresh" install with pnpm, there were some updates in lint packages that meant source or tests needed small tweaks to continue passing/building.
    - Refactor self-references within a package to not use package name.
    - Fixed missing package dependencies uncovered as pnpm-based installs will fail on missing dependencies that are flattened and "accidentally work" in yarn/npm.

- Configs:
    - Webpack `resolve.alias`: Since we no longer hoist victory packages to root, we now add aliases for our webpack configs and storybook (which uses webpack) programatically.
    - Babel, Jest configs: Normalized the naming and location of these across normal and native ones.

- Incremental caching:
    - eslint

---
## [yogstation13/Yogstation](https://github.com/yogstation13/Yogstation)@[b26f9f03e0...](https://github.com/yogstation13/Yogstation/commit/b26f9f03e00ded330c6bc2e0efa54aec0f8500cb)
#### Friday 2022-07-22 19:26:49 by Vaelophis Nyx

Makes donkpocket boxes on Box station into random spawners (#14822)

* Makes donk pockets station wide into random spawners

also adds a pile of donkpocket boxes to sec's back room and gives them a microwave

* reduced quanitity of donkpockets in sec by 4 boxes

* adds randodonks to the box mining base

* another commit I fundamentally disagree with

* reduces # of donk boxes in all kitchen variants

kill me

* microwave & gun/bomb swap

* fuck you byond map code

* fixes it. again.

---
## [BelialClover/Rowe-Patcher](https://github.com/BelialClover/Rowe-Patcher)@[4c49615e63...](https://github.com/BelialClover/Rowe-Patcher/commit/4c49615e633ad9433010b92bb855f75554b147f9)
#### Friday 2022-07-22 19:35:26 by BelialClover

Update 1.7.2

Changelog 1.7.2
-Added a way to change the time between day and night, this will work like in Sun and Moon where it changes between those two but does not affect the daily events, you can access to this
 by sleeping in the bed in the Weather Institute or sleeping in your own bed(or your rival bed)
-Rockruff evolves into Lycanrock Dusk at 6 am with this
-Added an Emulation Check before the game starts to see if you are using a compatible emulator, if you don't see the message it means it is a supported emulator and you can continue
 playing without any problem, however the message will also show for MyBoy! users but you can dismiss the message(thanks to ProjectRevoTPP and Pikalax for this feature)
-Changed how the personality based colors works so they won't change when you make any change to your pokemon
-Fixed Indeede breeding not working as intended
-Fixed female Indeede not being available in the wild or with the dexnav
-Fixed female Meowstic not being available in the wild or with the dexnav
-Fixed Telepathy not working
-Fixed Galarian Darmanitan laying normal darumaka eggs
-Fixed Day evolutions not working at 5pm in Pokemon that don't evolve at Dusk
-Gave Galarian Darmanitan some fire type moves
-Odd keystone now boost Spiritomb's Special Defense when held
-Odd keystone can now be held by wild Spiritombs (5% Chance)
-Fixed Dustox not learning Omnious Wind
-Lowered Scraggy Evolution Level
-Fixed Mankey not counting torward a certain Achievement
-Some minor Changes

---
## [RealMCoded/the-most-epic-clicker-game-ever](https://github.com/RealMCoded/the-most-epic-clicker-game-ever)@[0a475a8e59...](https://github.com/RealMCoded/the-most-epic-clicker-game-ever/commit/0a475a8e5951b5bf4775a787b606eece48a8b583)
#### Friday 2022-07-22 20:26:03 by stuartt_mcoded

Merge pull request #14 from RealMCoded/master

10 commits behind fuck you

---
## [AdvancedProgrammingSUT2022/project-group-07](https://github.com/AdvancedProgrammingSUT2022/project-group-07)@[7234cf20b6...](https://github.com/AdvancedProgrammingSUT2022/project-group-07/commit/7234cf20b67edf73d8672994cc09210b8be96c60)
#### Friday 2022-07-22 20:48:40 by Mahan Bayhaghi

Trade and diplomacy !

* diplomacy and trade basic logic added (basic!)

haghighatan holy jesus christ
this is a lot of logic

* diplomacy is in good shape

honestly i don't care if it is not like the pdf
i just think it is good :)

* i forgot to add files :)

* logic of trade added

* i forgot to add trading asset (again)

* diplomacy panel is done (not that stylish yet)

---
## [zardoy/vscode-better-snippets](https://github.com/zardoy/vscode-better-snippets)@[61b7ffdb5c...](https://github.com/zardoy/vscode-better-snippets/commit/61b7ffdb5c2fce855817754ed288fe6218de13d2)
#### Friday 2022-07-22 21:00:32 by Vitaly

feat: Trigger Characters! (#16)

presenting you absolutely new feature! Now you can target some snippets to only show after typing specific character!
It wasn't possible before to split snippets into groups, but now you can do this with new `when.triggerCharacters` optional array.
### The Problem
Even if you have quick suggestions enabled, it doesn't mean it would show snippets after typing every character (even space).
What if we wanted to quickly specify true/false after property name or expand it as a method?

```ts
const config = {
  enableFeature
  customMethod
}
```

Here, we have two properties, we want to quickly specify `true` on first and epxand method on second.
Firstly, let's assume that we don't want complicated checks and hacks. No typing snippets.

We could add a snippet to expand it to `true`/method after a single word on the line so we could type space and... the snippet won't appear, yes, because you firstly need to trigger completions and only then you can select it, this can be super annoying

```ts
enableFeature t -> true
```

## The Solution

```json
{
            "name": "t",
            "body": ": true,",
            "when": {
                "lineHasRegex": "^\\s*\\w+ $",
                "triggerCharacters": [
                    " "
                ]
            },
            "replaceTriggerCharacter": true
        },
        // to expand it as method
                {
            "name": "fun",
            "body": "($1) {\n\t$0\n},",
            "when": {
                "lineHasRegex": "^\\s*\\w+ $",
                "triggerCharacters": [
                    " "
                ]
            },
            "replaceTriggerCharacter": true
        },
```

Also, as you can see, we also now have optional `replaceTriggerCharacter` setting, because we want to remove the trigger character (space in our case):

```ts
enableFeature t
enableFeature: true,
```

> You can use `-` or even `:` as a trigger character here

Also, as you can see now, they doesn't suffer with global snippets/completions. And, you also can't get them if you retrigger completions (you need to type space again), so this is ideal for *in-flow* snippets.

In theory it can be also used, as postfix:

```json
        {
            "name": "tChar",
            "body": "translate(0, $0)",
            "when": {
                "lineRegex": "\\wPos.$",
                "triggerCharacters": [
                    "."
                ]
            }
        }
```

// But please, don't, it'll turn into annoyance that you need write dot again. Make sure you specify additional regex.

To also register snippet as regular snippet (so it will also appear after retriggering completions), add empty string to the array of trigger characters:

`triggerCharacters: ['.', '']`

Note, that TS is currently working on providing solutions for usecases from the beginning, but examples above still would be useful for JS.

---
## [angband/angband](https://github.com/angband/angband)@[e1762948fa...](https://github.com/angband/angband/commit/e1762948fa857f883068c81e717ba89d0d47c1ab)
#### Friday 2022-07-22 22:07:56 by Eric Branlund

For fiery terrain, targeted earthquakes, and curse removal, damage player last so messages are ordered properly if the player dies.  Avoids "You die. The lava burns you!" and "The ground shakes! The ceiling caves in! You die. The white jelly wails out in pain! The white jelly is embedded in the rock!".

---
## [ninjutsudev/hestiacp](https://github.com/ninjutsudev/hestiacp)@[365dab5670...](https://github.com/ninjutsudev/hestiacp/commit/365dab5670f6d1a862858be01638072eeb2ec1db)
#### Friday 2022-07-22 22:31:55 by divinity76

Use secure RNG to generate passwords (#2726)

* use secure rng to generate passwords

quoting MDN:
>Math.random() does not provide cryptographically secure random numbers. Do not use them for anything related to security. Use the Web Crypto API instead

My rng is kinda shitty, i know there is some fast way to cut down higher digits to get a digit in range without introducing bias, but i also know that other people have introduced bias by trying to do that on an initially secure rng and getting it wrong (iirc it's discussed here? https://www.youtube.com/watch?v=LDPMpc-ENqY - been years since i saw the talk, but i know Lavavej discussed it in one of his presentations, i think it was that one)  , but anyway this is fast enough, and secure.

* shorter name

* randomString2 / centralize js string generation

* missed 2

---
## [gfxfundamentals/lesson-builder](https://github.com/gfxfundamentals/lesson-builder)@[2bbb52c3ce...](https://github.com/gfxfundamentals/lesson-builder/commit/2bbb52c3ce124e3ced2bf07dca09ef60b87be23e)
#### Friday 2022-07-22 23:21:46 by Gregg Tavares

Switch from a very old version of marked to markdown-it

I'm not really sure I why I made this change. The old version
worked fine. npm complained their were vulnerabilities in the
old marked but those were irrelevent as this is a static site
builder.

One reason was I'd like to use
[footnotes](https://github.blog/changelog/2021-09-30-footnotes-now-supported-in-markdown-fields/)
and that requires using a newer markdown parser.

Anyway, it seemed like a good idea but took a ton of time.
The biggest issue is since marked shipped 9 years ago
markdown got standardized and IMO made a frustrating choice.
The choice they made is that embedded html ends at the first
blank line. In other words if you have markdown like this

```md

Some paragraph of text.

<div style="background: red">
  <p>
   This is some callout text

   and more text
  </p>
  <p>And some more here</p>
</div>

More normal markdown text.
```

It will see that as 2 chuncks of HTML, not one. In other words it will
generate this HTML

```html
<h1>Title of article</h1>
<p>Some paragraph of text.</p>
<div style="background: red">
  <p>
   This is some callout text
<p>and more text</p>
  </p>
  <p>And some more here</p>
</div>
<p>More normal markdown text.</p>
```

I think I get it. The problem with requiring a markdown parser
to handle the case above is it actually has to be able to parse
HTML to find the closing tag where as what they wanted was to be
able to parse with very simple regular expression rules.

That's fine but for me I just wanted to be able to embed
random HTML in the middle of a document for diagrams or
svg or whatever and not have to remember, ohhhhhhhhh, it's
blank line sensitive.

Further, this builder is already running on files that have
these blank lines.

The old version of marked handled this so how. The new version I'm not
sure but given everyone is moving to [the standard](https://commonmark.org)
most implemenations no longer handle this case.

Anyway, at the moment I have a solution that seems to be working
and unfortunately it does require a full HTML parser. At a glance
it seems to be working on existing content.

I don't know. Maybe I should switch to standard and fix existing
content. Or maybe I should keep existing content old an old version
of the builder.

In anycase, at the moment, this seems to be working.

---

