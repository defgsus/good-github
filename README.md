## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-11-15](docs/good-messages/2023/2023-11-15.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,595,042 were push events containing 3,942,544 commit messages that amount to 307,056,736 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 65 messages:


## [retlaw34/Shiptest](https://github.com/retlaw34/Shiptest)@[590e8cb752...](https://github.com/retlaw34/Shiptest/commit/590e8cb752400295fe770c303cf5b65a0089fc97)
#### Wednesday 2023-11-15 00:00:40 by Imaginos16

Adds the Inkwell-class Supply Freighter (#2385)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->
## Wait, isn't there a freeze right now?
Correct, there is a ship freeze currently, but I have received
permission from @Apogee-dev to create the PR for this vessel, as it was
a ship I've been working on since at least early-to-mid August.

![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/653635cc-b83d-44d8-a9e3-384ffbd9367b)

If any other maptainer would like to overrule Apogee, I'd be more than
happy to temporarily close the PR. Until then, here it is!
## About The Pull Request
Hello everyone! Mr. SolGov here again to add yet another ship to be
tested!

This PR adds a completely new vessel, that being the **Inkwell-class
Supply Freighter**, a ship known for its vast cargo space!

![2023-10-13 13 54
57](https://github.com/shiptest-ss13/Shiptest/assets/77556824/9a70d97e-ab17-45af-a690-e528574b95cb)

![2023-10-13 13 54
59](https://github.com/shiptest-ss13/Shiptest/assets/77556824/2d9d6d0a-85e2-4c46-9754-d49f15be0560)

With extra starter money, three sonnensöldners, and three miners,
players can enjoy completing bounties like no tomorrow, have drinks with
their crewmates in peace, and supply other SolGov vessels with much
needed equipment in less time than you can say "I ran out of ammo!"

Notable things in this ship include:
- Turrets (with IFF!)
- A bar!
- A full-blown cafeteria with a small kitchen and lounge!
- An office space for bureaucrats and scribes!
- Decently-sized quarters for the Logistics Deck Officer and Captain!
- A massive cargo bay with pre-existing supplies!
- A secret compartment for private storage!

And finally, as for jobs, there are:
- 1 Captain
- 1 Logistics Deck Officer
- 3 Sonnensöldneren
- 2 Space Engineers
- 3 Field Engineers
- 2 Bureaucrats
- 6 Scribes
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
More SolGov content is nice! Especially when it comes to ships, for a
faction that only has two existing at the moment, haha.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: PositiveEntropy
add: The Solarian Port Authority Has Now Permitted Inkwell-class Vessels
To Explore The Stars!
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: spockye <79304582+spockye@users.noreply.github.com>

---
## [yarnpkg/berry](https://github.com/yarnpkg/berry)@[6460b597fa...](https://github.com/yarnpkg/berry/commit/6460b597fad141ff1b3fb792a2c53514ceb07b8b)
#### Wednesday 2023-11-15 00:19:34 by Tom Szwaja

docs: fix old info in contributing guide (#5779)

**What's the problem this PR addresses?**
<!-- Describe the rationale of your PR. -->
<!-- Link all issues that it closes. (Closes/Resolves #xxxx.) -->

EDIT: I just saw that #5776 beat me to it. However, the version I
propose adds clarity imho as well as links to relevant resources.

---

The instructions in the 'Writing documentation' section gave false
information (I assume it was simply outdated), making it harder for
people to contribute.

Pls tag for Hacktoberfest.
...

**How did you fix it?**
<!-- A detailed description of your implementation. -->

* Revised the 'Writing documentation' section so that it aligns with our
current project structure
* Fixed broken links
* Provided links to the tech we use  
...

**Checklist**
<!--- Don't worry if you miss something, chores are automatically
tested. -->
<!--- This checklist exists to help you remember doing the chores when
you submit a PR. -->
<!--- Put an `x` in all the boxes that apply. -->
- [x] I have read the [Contributing
Guide](https://yarnpkg.com/advanced/contributing).

<!-- See
https://yarnpkg.com/advanced/contributing#preparing-your-pr-to-be-released
for more details. -->
<!-- Check with `yarn version check` and fix with `yarn version check
-i` -->
- [ ] I have set the packages that need to be released for my changes to
be effective.

<!-- The "Testing chores" workflow validates that your PR follows our
guidelines. -->
<!-- If it doesn't pass, click on it to see details as to what your PR
might be missing. -->
- [x] I will check that all automated PR checks pass before the PR gets
reviewed.

Co-authored-by: Maël Nison <nison.mael@gmail.com>

---
## [lifning/omicron](https://github.com/lifning/omicron)@[2fc0dfd8c1...](https://github.com/lifning/omicron/commit/2fc0dfd8c11f31e66cfaf8ee80586bb2ed607216)
#### Wednesday 2023-11-15 00:48:00 by Andrew J. Stone

Extract storage manager related code from sled-agent (#4332)

This is a large PR. The changes are in many ways *just* moving code
around,
and at a cursory glance may appear to be a giant waste of time. To
justify
these changes and my rationale I will first present the goals I believe
we
should strive to meet in general sled-agent development. I'll then go
into
how I believe these goals can be realized via code patterns. I'll then
discuss
the concrete changes in this PR and how they implement the discussed
patterns.
Lastly, I'll list a few open questions about the implementation in the
PR.

I want to emphasize that a lot of what I talk about below is already
done in
sled-agent, at least part way. We can pick the best patterns already in
use and
standardize on them to build a more coherent and yet decoupled
architecture for
easier testing and understanding.

# Goals

This PR is an attempt to start making sled-agent easier to maintain. In
order to
make things easier to maintain, I believe we should attempt to realize a
few key
goals:

1. Initial startup and control code should read linearly. You shouldn't
have to
jump around to follow the gist of what's going on.
2. Tasks, like functions, should live at a certain abstraction level. It
must be clear
 what state the task is managing and how it gets mutated.
3. A developer must be able to come into the codebase and know where a
given
functionality should live and be able to clearly follow existing
patterns such
that their new code doesn't break or cross abstractions that make
following the
code harder in the future.
4. Tests for individual abstractions and task driven code should be easy
to
write. You shouldn't need to spin up the whole sled-agent in order to
test an
algorithm or behavior.
 5. Hardware should be abstracted out, and much of the code shouldn't 
 deal with hardware directly.

# Patterns

## Task/Handle

In my opinion, the most important pattern to follow for async rust
software
is what I call the "task/handle" pattern. This pattern helps code
maintenance
by explicitly managing state and making task driven code easier to test.
All
tasks that provide services to other tasks should follow this pattern.
In this
pattern, all state is contained in a type owned by the task and
inaccessible
directly to other tasks. The task has a corresponding handle which must
be
`Send` and `Clone`, and can be used to make requests of the task. The
handle
interacts with the task solely via message passing. Mutexes are never
used.

A few things fall directly out of this pattern:

* Code that manipulates state inside and outside the task can be
synchronous
* We don't have to worry about mutex behavior with regards to
cancellation,
   await points, etc...
 * Testing becomes easier:
   * We can test a bunch of the code without spawning a task in many
cases. We just [directly construct the state object and call
functions](https://github.com/oxidecomputer/omicron/pull/4332/files#diff-08315639e20a9323f2740455a7813d83ca43b05dca197ebbda66c13f750d446bR634-R656),
     whether sync or async.
   * When testing sequential operations that are fire and forget,
we [know when they have been processed by the task
loop](https://github.com/oxidecomputer/omicron/pull/4332/files#diff-08315639e20a9323f2740455a7813d83ca43b05dca197ebbda66c13f750d446bR702-R709),
     because our next request will only run after those operations. 
This is a direct result of the fifo channel between handle and task.
This is not possible with state shared outside the task via a mutex.
     We must poll that mutex protected state until it either changes to
     the value we expect or we get a timeout. If we expect no change, we
     must use a side-channel.
   * We can write complex state handling algorithms, such as those in 
      maghemite or bootstore, in a deterministic, synchronous style that
allows property based testing and model checking in as straightforward
     a manner as possible.
* We can completely [fake the
task](https://github.com/oxidecomputer/omicron/pull/4332/files#diff-08315639e20a9323f2740455a7813d83ca43b05dca197ebbda66c13f750d446bR163-R223)
without changing any of the calling code except the constructor. The
real
handle can instead send messages to a fake task. Importantly, this
strategy
can also be used to abstract out hardware for unit tests and simulation.

Beyond all that though, the understanding of how state is mutated and
accessed
is clear. State is only mutated inside the task, and can only be
retrieved from
code that has a copy of the handle. There is no need for separate
`_locked`
methods, and no need to worry about order of locking for different bits
of task
state. This can make the task code itself much shorter and easier to
read as
demonstrated by the new `StorageManager` code in `sled_storage`. We can
also
maintain internal stats for the task, and all of this can be retrieved
from the
handle for reporting in `omdb`.

There is one common question/problem with this pattern. How do you
choose a
bounded channel size for handle to task messages?

This can be tricky, but in general, you want the channel to *act*
unbounded,
such that sends never fail. This makes the channels reliable, such that
we never
drop messages inside the process, and the caller doesn't have to choose
what to
do when overloaded. This simplifies things drastically for developers.
However,
you also don't want to make the channel actually unbounded, because that
can
lead to run-away memory growth and pathological behaviors, such that
requests
get slower over time until the system crashes.

After discussions with @jgallagher and reflections from @sunshowers and
@davepacheco on RFD 400, the solution is to choose a large enough bound
such that we should never hit it in practice unless we are truly
overloaded.
If we hit the bound it means that beyond that requests will start to
build
up and we will eventually topple over. So when we hit this bound, we
just
[go ahead and
panic](https://github.com/oxidecomputer/omicron/pull/4332/files#diff-08315639e20a9323f2740455a7813d83ca43b05dca197ebbda66c13f750d446bR75-R77).

Picking a channel bound is hard to do empirically, but practically, if
requests are
mostly mutating task local state, a bound of 1024 or even 8192 should be
plenty.
Tasks that must perform longer running ops can spawn helper tasks as
necessary
or include their own handles for replies rather than synchronously
waiting. Memory
for the queue can be kept small with boxing of large messages.

It should also be noted that mutexes also have queues that can build up
and
cause pathological slowness. The difference is that these queues are
implicit
and hard to track.

## Isolate subsystems via the message driven decoupling

We have a bunch of managers (`HardwareManager`, `StorageManager`,
`ServiceManager`, `InstanceManager`) that interact with each other to
provide sled-agent services. However, much of that interaction is ad-
hoc with state shared between tasks via an `Inner` struct protected
by a mutex. It's hard to isolate each of these managers and test
them independently. By ensuring their API is well defined via a
`Handle`,
we can fake out different managers as needed for independent testing.
However, we can go even farther, without the need for dependency
injection
by having different managers announce their updates via [broadcast or
watch

channels](https://github.com/oxidecomputer/omicron/pull/4332/files#diff-08315639e20a9323f2740455a7813d83ca43b05dca197ebbda66c13f750d446bR129-R133).

With this strategy, we can drive tests for a task by using the handle to
both
trigger operations, and then wait for the outflow of messages that
should occur
rather than mocking out the handle API of another task directly and
checking
the interaction via the fake. This is especially useful for lower level
services
that others depend upon such as `StorageManager`, and we should do this
when we
can, rather than having tasks talk directly to each other. This strategy
leads
directly to the last pattern I really want to mention, the `monitor`
pattern.

## High level interaction via monitors

Remember that a primary goal of these patterns is to make the sled-agent
easier
to read and discover what is happening at any given point in time. This
has to
happen with the inherent concurrency of all the separate behaviors
occurring
in the sled-agent such as monitoring for hardware and faults, or
handling user
requests from Nexus. If our low level managers announce updates via
channels
we can have high level `Monitors` that wait for those updates and then
dispatch
them to other subsystems or across clients to other sleds or services.
This
helps further decouple services for easier testing, and also allows us
to
understand all the asynchrony in the system in fewer spots. We can put
RAS code
in these monitors and use them as central points to maintain stats and
track the
overall load on the system.

# The punchline

How do the patterns above satisfy the goals? By decoupling tasks and
interacting
solely via message passing we make testing easier(goal 4). By separating
out
managers/ services into separate tasks and maintaining state locally we
satisfy
goals 2 and 5. By making the tasks clear in their responsibilities, and
their
APIs evident via their handles, we help satisfy goal 3. Goal 3 is also
satisfied
to a degree by the elimination of sharing state and the decoupling via
monitors.
Lastly, by combining all the patterns, we can spawn all our top level
tasks and
monitors in one place after initializing any global state. This allows
the code
to flow linearly.

Importantly, it's also easy to violate goal 3 by dropping some mutexes
into the
middle of a task and oversharing handles between subsystems. I believe
we can
prevent this, and also make testing and APIs clearer, by separating
subsystems
into their own rust packages and then adding monitors for them in the
sled-agent.
I took a first cut at this with the `StorageManager`, as that was the
subsystem I was
most familiar with.

# Concrete Code changes

Keeping in line with my stated goals and patterns, I abstracted the
storage
manager code into its own package called `sled-storage`. The
`StorageManager`
uses the `task/handle` pattern, and there is a monitor for it in
sled-agent
that takes notifications and updates nexus and the zone bundler. There
are also a
bunch of unit tests where none existed before. The bulk of the rest of
the code
changes fell out of this. In particular, now that we have a separate
`sled-storage`
package, all high level disk management code lives there. Construction
and
formatting of partitions still happens in `sled-hardware`, but anything
above the
zpool level occurs in `sled-storage`. This allows testing of real
storage code on
any illumos based system using file backed zpools. Importantly, the
key-management
code now lives at this abstraction level, rather than in
`sled-hardware`, which
makes more sense since encryption only operates on datasets in ZFS.

I'd like to do similar things to the other managers, and think that's a
good way
to continue cleaning up sled-agent.

The other large change in this code base is simplifying the startup of
the bootstrap agent such that all tasks that run for the lifetime of
the sled-agent process are spawned in `long_running_tasks`. There is a
struct called `LongRunningTaskHandles` that allows interaction with all
the
"managers" spawned here. This change also has the side effect of
removing the
`wait_while_handling_hardware_updates` concurrent future code, since we
have
a hardware monitor now running at the beginning of time and can never
miss
updates. This also has the effect of negating the need to start a
separate
hardware manager when the sled-agent starts up. Because we now know
which
tasks are long running, we don't have to save their tokio `JoinHandle`s
to display
ownership and thus gain clonability.

# Open Questions

* I'm not really a fan of the name `long_running_task_handles`. Is there
a better
name for these?
* Instead of calling `spawn_all_longrunning_tasks` should we just call
the
individual spawn functions directly in `bootstrap/pre_server`? Doing it
this
way would allow the `ServiceManager` to also live in the long running
handles
and remove some ordering issues. For instance, we wait for the bootdisk
inside
`spawn_all_longrunning_tasks` and we also upsert synthetic disks.
Neither
of these is really part of spawning tasks.

---
## [jlsnow301/tgstation](https://github.com/jlsnow301/tgstation)@[bed92e193c...](https://github.com/jlsnow301/tgstation/commit/bed92e193ce4a79824fd4fd30a900245dca870ae)
#### Wednesday 2023-11-15 01:24:20 by san7890

Further Prevention of Disposals Qdeletion (#79714)

## About The Pull Request

Fixes the consequences of #79629 - Verdict is still out on what the root
issue is

This has been an issue for the last two years and everything I go
bananas trying to get a consistent reproduction case to figure out the
root issue. After three session of picking, I think it's just a
consequence of certain thing in disposals code sleeping due to
`addtimer()` and whatnot so I'm just throwing in the towel and just
making it so we stop sending atoms to nullspace for no reason.

`target_turf` is typically always a present arg, but regardless we are
guaranteed to get a valid turf to send people to instead of the deleted
mob room. We still `stack_trace()` whenever this happens, so tracking
this issue doesn't change any more than the present status quo- we just
don't keep torturing mobs by sending them to the shadow realm.
## Why It's Good For The Game

One day we'll figure out why we keep getting `null` passed into
`forceMove()` like this but today is not that day. i know turfs
technically can't be deleted but it's just there as a safety since we
nullcheck anyways (which is the whole point of this fix). Let's just
stop screwing with players for the time being

also the code looks much better
## Changelog
:cl:
fix: Safeties in the code have been added to prevent things in disposals
going into nullspace whenever they get ejected from a pipe - you will
just magically spawn at the turf that you were meant to be flung
towards.
/:cl:

---
## [jlsnow301/tgstation](https://github.com/jlsnow301/tgstation)@[5175ae0637...](https://github.com/jlsnow301/tgstation/commit/5175ae06374450b87324bb280c754e53880b7b16)
#### Wednesday 2023-11-15 01:24:20 by John Willard

TGUI Destructive Analyzer (#79572)

## About The Pull Request

I made this to help me move more towards my goals [laid out
here](https://hackmd.io/XLt5MoRvRxuhFbwtk4VAUA) which currently doesn't
have much interest.

This makes the Destructive Analyzer use a little neat TGUI menu instead
of its old HTML one. I also touch a lot of science stuff and a little
experimentor stuff, so let me explain a bit:
Old iterations of Science had different items that you can use to boost
nodes through deconstruction. This has been removed, and its only
feature is the auto-unlocking of nodes (that is; making them visible to
the R&D console). I thought that instead of keeping this deprecated code
around, I would rework it a little to make it clear what we actually use
it for (unhiding nodes).
All vars and procs that mentioned this have been renamed or reworked to
make more sense now.

Experimentor stuff shares a lot with the destructive analyzer, so I had
to mess with that a bit to keep its decayed corpse of deprecated code,
functional.

I also added context tips to the destructive analyzer, and added the
ability to AltClick to remove the inserted item. Removing items now also
plays a little sound because it was kinda lame.
Also, balloon alerts.

## Why It's Good For The Game

Moves a shitty machine to TGUI so it is slightly less shitty, now it's
more direct and compact with more player-feedback.
Helps me with a personal project and yea

### Video demonstration

I show off connecting the machine to R&D Servers, but I haven't changed
the behavior of that and the roundstart analyzers are connected to
servers by default.


https://github.com/tgstation/tgstation/assets/53777086/65295600-4fae-42d1-9bae-eccefe337a2b

## Changelog

:cl:
refactor: Destructive Analyzers now have a TGUI menu.
/:cl:

---
## [ZacharyTStone/ZacharyTStone](https://github.com/ZacharyTStone/ZacharyTStone)@[9784103939...](https://github.com/ZacharyTStone/ZacharyTStone/commit/9784103939c6405a751deb22fbe39a83246688e8)
#### Wednesday 2023-11-15 01:27:34 by ROBO-ZACH

Update README with new quote: "Friendship improves happiness and abates misery, by the doubling of our joy and the dividing of our grief." <br>— Cicero

---
## [y21/rust-clippy](https://github.com/y21/rust-clippy)@[c3a6b376a4...](https://github.com/y21/rust-clippy/commit/c3a6b376a43e1ce10c6f17872fd48e99ee294388)
#### Wednesday 2023-11-15 01:57:38 by bors

Auto merge of #11800 - blyxyas:meow-meow, r=Centri3

Removing @Centri3 from reviewer rotation

Catherine decided that the best course of action would be to (maybe temporarily) remove her from the reviewer's rotation (but not unassign her from her current reviews). This PR does that. She'll always be welcomed back if she wants to review some more :heart:

> Alejandra González: [youremyfrennow.mp4](https://rust-lang.zulipchat.com/user_uploads/4715/7nE2W6cb8Q02gcK-vubvmsPM/youremyfrennow.mp4)
>
>Catherine, Fred (`@xFrednet` ) noticed that you aren't as active as in the summer, and proposed that maybe you preferred to be removed from the reviewer rotation. Don't worry, you aren't being taken out of the team, just wanted to know if you maybe preferred to not have those reviews pilling up (they can be pretty stressful to see).
>
>If you decide to step out of the reviewers rotation, you wouldn't be removed from the team, you just wouldn't have that responsability. Everyone takes break and that's fine, so yeah, if you want to not have to review PRs, let me know!
>
>So yeah, from weird teenager transfem to (probably weird) teenager transfem, the choice is in your hand.
>
>Alejandra González: meow meow ^•ﻌ•^
>
>Catherine (Centri3): Yeah that's probably best now, I'll still try with any I'm currently assigned to but I would prefer not to get anymore until then
>Catherine (Centri3): meow meow :3

changelog:none

r? `@Centri3`

---
## [jplukas/berry](https://github.com/jplukas/berry)@[f5b7abd7c0...](https://github.com/jplukas/berry/commit/f5b7abd7c0074bfff365f4ea5091fa4f5bf055f7)
#### Wednesday 2023-11-15 02:41:56 by Maël Nison

Injects the PnP runtime in the process before requiring the user config (#5954)

**What's the problem this PR addresses?**

We added support for JS constraints thanks to the `yarn.config.cjs`
file. However this file is currently executed from within the Yarn
process, so it doesn't have access to the dependencies when operating
under the PnP installation mode.

Fixes #5878

**How did you fix it?**

I'm still on the fence on the right solution. This PR automatically
loads the `.pnp.cjs` file when the `loadUserConfig` file is called. An
alternative would be a post-install hook to allow each linker to inject
their runtime inside the process post-install, but that was more
involved and I figured it's worth more consideration.

Another alternative was to not do anything and expect users to setup the
PnP runtime themselves, but it feels something that Yarn should be able
to handle.

A third alternative would be to evaluate this file within a worker
thread, which would be started with the proper `execArgv` flags. It's
less intrusive than the post-install hook so I kinda like this idea, but
again - worth more consideration.

I'm working on enabling tests, and to this effect I'm checking whether
we can remove the `NODE_OPTIONS` values from the `makeTemporaryEnv`
subprocesses.

**Checklist**
<!--- Don't worry if you miss something, chores are automatically
tested. -->
<!--- This checklist exists to help you remember doing the chores when
you submit a PR. -->
<!--- Put an `x` in all the boxes that apply. -->
- [x] I have read the [Contributing
Guide](https://yarnpkg.com/advanced/contributing).

<!-- See
https://yarnpkg.com/advanced/contributing#preparing-your-pr-to-be-released
for more details. -->
<!-- Check with `yarn version check` and fix with `yarn version check
-i` -->
- [x] I have set the packages that need to be released for my changes to
be effective.

<!-- The "Testing chores" workflow validates that your PR follows our
guidelines. -->
<!-- If it doesn't pass, click on it to see details as to what your PR
might be missing. -->
- [x] I will check that all automated PR checks pass before the PR gets
reviewed.

---
## [openai/evals](https://github.com/openai/evals)@[b1ea4786dc...](https://github.com/openai/evals/commit/b1ea4786dc32dd4f320e56ff98043ea0ea8eef6a)
#### Wednesday 2023-11-15 02:51:44 by Andrei Alexandru

Add theory of mind eval (#1405)

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

Theory of mind.

### Eval description

The `ToMi` test set contains 5,993 question-answer pairs. These are
instances of the [Sally-Anne
test](https://en.wikipedia.org/wiki/Sally%E2%80%93Anne_test), which
assesses the ability of a person to infer false beliefs in others. The
original setting involves two people, Sally and Anne, who are together
in a room. Sally places a marble in a box. Then, Anne leaves the room,
and while she is away, Sally moves the marble to a basket elsewhere in
the room. When Anne returns to the room, where will she search for the
marble? If the person responding “has” theory-of-mind they’ll respond
that Anne searches for the marble in the box, where she had last seen
it. If they do not, they ascribe their own, accurate belief regarding
the location to Anne, and say that she looks for it in the basket.

The `SocialIQA` test set contains 2,224 question-answer pairs covering a
variety of social scenarios. These are multiple-choice, with 3 options
of which only one is correct. The questions cover a person’s wants,
needs, motivations, and reactions, as well as the effects of an action
(on self or others), and how that action reflects on the person carrying
it out (e.g. how others would perceive them after having carried out the
action).

Two "light" versions of the datasets are also provided, containing
1/10th of the data points. These are useful for iterating on prompts and
developing other scaffolding.
### What makes this a useful eval?

Measures theory of mind capability in language models.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should

- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

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

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `mypy`, `black`,
`isort`, `autoflake` and `ruff` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "user", "content": "Jackson entered the hall. Chloe
entered the hall. The boots is in the bathtub. Jackson exited the hall.
Jackson entered the dining_room. Chloe moved the boots to the pantry.
Where does Chloe think that Jackson searches for the boots?"}], "ideal":
"bathtub"} ```
</details>

---
## [openai/evals](https://github.com/openai/evals)@[e96b4d3550...](https://github.com/openai/evals/commit/e96b4d35502125e354391044512d899268ade99d)
#### Wednesday 2023-11-15 02:59:58 by Andrew

Fix the OpenAI Version to <=0.28.1  (#1410)

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

[Insert Eval name here]

### Eval description

[Insert a short description of what your eval does here]

### What makes this a useful eval?

[Insert why this eval is worth including and any additional context]

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [ ] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [ ] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [ ] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [ ] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should

- [ ] Check that your data is in `evals/registry/data/{name}`
- [ ] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [ ] Ensure you have the right to use the data you submit via this eval

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

- [ ] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [ ] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [ ] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [ ] I have filled out all required fields of this form
- [ ] I have used **Git LFS** for the Eval JSON data
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `mypy`, `black`,
`isort`, `autoflake` and `ruff` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
  INSERT_EVAL_HERE
  ```
</details>

---
## [Senthi1Kumar/pytorch](https://github.com/Senthi1Kumar/pytorch)@[3afb4e5cf7...](https://github.com/Senthi1Kumar/pytorch/commit/3afb4e5cf7b0162c532449fb5c9e7c7058a4c803)
#### Wednesday 2023-11-15 03:20:04 by Brian Hirsh

AOTAutograd: handle set_(), detect metadata mutations that cancel out (#111554)

This should be enough to get @voznesenskym 's FSDP branch to plumb `set_()` through AOTAutograd properly and have everything properly no-op out. Main changes are:

(1) graph break on `aten::set_.source_Tensor_storage_offset` (we could support it but it isn't needed, seems safer to graph break)

(2) Functionalization: add a "proper" functionalization kernel for `aten::set_.source_Tensor`. The previous one we had was codegen'd and it was wrong (it would just clone() and call set_(), which does not do the right thing). I also manually mark on the `FunctionalTensorWrapper` when a given tensor has been mutated by a `set_()` call.

(3) AOTAutograd: I added a new field, `InputAliasInfo.mutates_storage_metadata`, so we can distinguish between "regular" metadata mutations, and metadata mutations due to `set_()` calls. This is mainly because at runtime, one requires calling `as_strided_()` to fix up metadata, while the other requires calling `set_()`.

(4) Made AOTAutograd's detection for metadata mutations / set_() mutations smarter and detect no-ops (if the storage and metadata are all the same).

I also killed `was_updated()` and `was_metadata_updated()`, and replaced them with (existing) `has_data_mutation() ` and (new) `has_data_mutation()`, which can more accurately distinguish between data-mutation vs. `set_()` calls vs. metadata-mutation

**This PR is still silently correct in one case though**, which I'd like to discuss more. In particular, this example:
```
def f(x):
    x_view = x.view(-1)
    x.set_(torch.ones(2))
    x_view.mul_(2)
    return
```

If you have an input that experiences both a data-mutation **and** a `x_old.set_(x_new)` call, there are two cases:

(a) the data mutation happened on the storage of `x_new`. This case should be handled automatically: if x_new is a graph intermediate then we will functionalize the mutation. If x_new is a different graph input, then we will perform the usual `copy_()` on that other graph input

(b) the data mutation happened on the storage of `x_old`. This is more of a pain to handle, and doesn't currently work. At runtime, the right thing to do is probably something like:
```

def functionalized_f(x):
    x_view = x.view(-1)
    # set_() desugars into a no-op; later usages of x will use x_output
    x_output = torch.ones(2)
    # functionalize the mutation on x_view
    x_view_updated = x.mul(2)
    x_updated = x_view_updated.view(x.shape)
    # x experienced TWO TYPES of mutations; a data mutation and a metatadata mutation
    # We need to return both updated tensors in our graph
    return x_updated, x_output
def runtime_wrapper(x):
    x_data_mutation_result, x_set_mutation_result = compiled_graph(x)
    # First, perform the data mutation on x's old storage
    x.copy_(x_data_mutation_result)
    # Then, swap out the storage of x with the new storage
    x.set_(x_set_mutation_result)
```

There are two things that make this difficult to do though:

(1) Functionalization: the functionalization rule for `set_()` will fully throw away the old `FunctionalStorageImpl` on the graph input. So if there are any mutations to that `FunctionalStorageImpl` later on in the graph, the current graph input won't know about it. Maybe we can have a given `FunctionalTensorWrapper` remember all previous storages that it had, and track mutations on all of them - although this feels pretty complicated.

(2) AOTAutograd now needs to know that we might have *two* graph outputs that correspond to a single "mutated input", which is annoying.

It's worth pointing out that this issue is probably extremely unlikely for anyone to run into - can we just detect it and error? This feels slightly easier than solving it, although not significantly easier. We would still need `FunctionalTensorWrapper` to keep track of mutations on any of its "previous" storages, so it can report this info back to AOTAutograd so we can raise an error.

Pull Request resolved: https://github.com/pytorch/pytorch/pull/111554
Approved by: https://github.com/ezyang

---
## [san7890/bruhstation](https://github.com/san7890/bruhstation)@[6fefc9ce0e...](https://github.com/san7890/bruhstation/commit/6fefc9ce0eb09b9b97e3d54609ace23c43601394)
#### Wednesday 2023-11-15 04:05:23 by Andrew

Pipe painting, spraycan preset colors (#79521)

![dreamseeker_AZs0erdnrs](https://github.com/tgstation/tgstation/assets/3625094/06a12d22-387b-4a33-8b61-59bbe3495c82)

## About The Pull Request

Made pipe painter properly paint pipe colors, work on pipe items, and
added the same functionality to regular spraycans.

Spraycans now have the color presets in UI for easier selection of the
valid pipe colors.

## Why It's Good For The Game

Bug fixing is good.
It was weird that spraycans couldn't paint pipes, but some other device
could.
Also custom spraycan color is too clunky, presets are nice for quick
spraycan color selection.

## Changelog

:cl:
fix: fixed pipe painter not applying pipe color properly
qol: made spraycans work also as pipe painters
qol: spraycans now have basic color presets for quick selection
/:cl:

---
## [whistler420/CheesedUP-FMOD](https://github.com/whistler420/CheesedUP-FMOD)@[21eea86964...](https://github.com/whistler420/CheesedUP-FMOD/commit/21eea8696427e298276b767c0c892d955aac0410)
#### Wednesday 2023-11-15 04:48:39 by whistlr

get cotton and swamp back in there

fuck you denchick

---
## [akshatd/umich-aerosp588](https://github.com/akshatd/umich-aerosp588)@[df748042eb...](https://github.com/akshatd/umich-aerosp588/commit/df748042ebb5411354a085b6be5e4188a008649d)
#### Wednesday 2023-11-15 05:53:51 by Akshat Dubey

holy fuck i hate katex wtf removing spaces fixed the issue???

---
## [cyphar/runc](https://github.com/cyphar/runc)@[ae3fd6b345...](https://github.com/cyphar/runc/commit/ae3fd6b345cb6e7de7b0373211af3ddbc7862166)
#### Wednesday 2023-11-15 06:54:59 by Aleksa Sarai

tree-wide: use /proc/thread-self for thread-local state

With the idmap work, we will have a tainted Go thread in our
thread-group that has a different mount namespace to the other threads.
It seems that (due to some bad luck) the Go scheduler tends to make this
thread the thread-group leader in our tests, which results in very
baffling failures where /proc/self/mountinfo produces gibberish results.

In order to avoid this, switch to using /proc/thread-self for everything
that is thread-local. This primarily includes switching all file
descriptor paths (CLONE_FS), all of the places that check the current
cgroup (technically we never will run a single runc thread in a separate
cgroup, but better to be safe than sorry), and the aforementioned
mountinfo code. We don't need to do anything for the following because
the results we need aren't thread-local:

 * Checks that certain namespaces are supported by stat(2)ing
   /proc/self/ns/...

 * /proc/self/exe and /proc/self/cmdline are not thread-local.

 * While threads can be in different cgroups, we do not do this for the
   runc binary (or libcontainer) and thus we do not need to switch to
   the thread-local version of /proc/self/cgroups.

 * All of the CLONE_NEWUSER files are not thread-local because you
   cannot set the usernamespace of a single thread (setns(CLONE_NEWUSER)
   is blocked for multi-threaded programs).

Note that we have to use runtime.LockOSThread when we have an open
handle to a tid-specific procfs file that we are operating on multiple
times. Go can reschedule us such that we are running on a different
thread and then kill the original thread (causing -ENOENT or similarly
confusing errors). This is not strictly necessary for most usages of
/proc/thread-self (such as using /proc/thread-self/fd/$n directly) since
only operating on the actual inodes associated with the tid requires
this locking, but because of the pre-3.17 fallback for CentOS, we have
to do this in most cases.

In addition, CentOS's kernel is too old for /proc/thread-self, which
requires us to emulate it -- however in rootfs_linux.go, we are in the
container pid namespace but /proc is the host's procfs. This leads to
the incredibly frustrating situation where there is no way (on pre-4.1
Linux) to figure out which /proc/self/task/... entry refers to the
current tid. We can just use /proc/self in this case.

Yes this is all pretty ugly. I also wish it wasn't necessary.

Signed-off-by: Aleksa Sarai <cyphar@cyphar.com>

---
## [meddcohealthcare16/Inguinal-Hernia-Hernioplasty-Bilateral-rate-in-Agra-Meddco](https://github.com/meddcohealthcare16/Inguinal-Hernia-Hernioplasty-Bilateral-rate-in-Agra-Meddco)@[ad4f8aa8d9...](https://github.com/meddcohealthcare16/Inguinal-Hernia-Hernioplasty-Bilateral-rate-in-Agra-Meddco/commit/ad4f8aa8d9bcf8315bb958871b03d8ec99929ef2)
#### Wednesday 2023-11-15 09:01:33 by meddcohealthcare16

Inguinal Hernia Hernioplasty-Bilateral rate in Agra-Meddco

Title: Inguinal Hernia Hernioplasty-Bilateral: A Comprehensive Guide to Surgical Intervention
Introduction:
Inguinal hernias are a common medical condition where a portion of the intestine or other abdominal tissue protrudes through a weak spot or tear in the abdominal wall. This condition often requires surgical intervention to prevent complications and alleviate symptoms. One such surgical procedure is bilateral inguinal hernioplasty, a technique designed to address hernias on both sides of the groin simultaneously.
Understanding Inguinal Hernias:
Before delving into the details of bilateral inguinal hernioplasty, it is essential to comprehend the nature of inguinal hernias. These hernias occur when there is a weakness in the abdominal wall, allowing abdominal contents to bulge through. Inguinal hernias are particularly common in men, often manifesting as a noticeable bulge in the groin area.
Symptoms of inguinal hernias may include pain or discomfort, especially when lifting heavy objects, coughing, or straining during bowel movements. In some cases, the protruding tissue may become trapped or incarcerated, leading to a medical emergency.
Surgical Intervention:
While some inguinal hernias can be managed with conservative measures, surgery is often the preferred and more effective treatment, especially for bilateral hernias. Bilateral inguinal hernioplasty involves repairing hernias on both sides of the groin during a single surgical procedure.
Surgical Techniques:
Open Hernia Repair:
Traditional open hernia repair involves making an incision directly over the hernia site.
The surgeon pushes the protruding tissue back into place and strengthens the abdominal wall with sutures or synthetic mesh.
This technique allows for a direct view of the hernia and surrounding tissues.
Laparoscopic Hernia Repair:
In laparoscopic hernia repair, small incisions are made, and a laparoscope (a thin tube with a camera) is used to guide the surgeon.
The surgeon repairs the hernia using small instruments and often places a mesh to reinforce the weakened area.
Laparoscopic surgery generally results in smaller incisions, reduced pain, and a quicker recovery compared to open surgery.
Robotic-Assisted Hernia Repair:
Robotic-assisted hernia repair combines the benefits of laparoscopic surgery with enhanced precision and maneuverability offered by robotic systems.
Surgeons control robotic arms to perform the procedure, facilitating intricate movements with improved visibility.
Advantages of Bilateral Inguinal Hernioplasty:
Comprehensive Repair:
Bilateral inguinal hernioplasty addresses hernias on both sides, preventing the need for a separate surgery for the opposite side at a later date.
This comprehensive approach reduces the overall recovery time and inconvenience for the patient.
Reduced Recurrence Risk:
Repairing both sides simultaneously decreases the risk of developing a hernia on the opposite side after the initial surgery.
Reinforcing the weakened areas with mesh provides additional support, reducing the likelihood of recurrence.
Efficient Use of Resources:
Performing bilateral inguinal hernioplasty in a single session optimizes the use of medical resources and minimizes healthcare costs compared to two separate procedures.
Recovery and Postoperative Care:
Hospital Stay:
The length of hospital stay varies, with some patients being discharged on the same day (outpatient surgery) and others requiring an overnight stay.
Activity Restrictions:
Patients are usually advised to limit physical activity, especially heavy lifting, for several weeks following surgery to allow proper healing.
Pain Management:
Pain management is an integral part of the postoperative care plan. Medications may be prescribed to alleviate discomfort during the recovery period.
Follow-Up Appointments:
Regular follow-up appointments with the surgeon are crucial to monitor the healing process and address any concerns or complications promptly.
Conclusion:
Bilateral inguinal hernioplasty is a surgical procedure designed to address hernias on both sides of the groin simultaneously, offering a comprehensive solution to this common medical condition. Whether performed through traditional open surgery, laparoscopy, or robotic-assisted techniques, the goal remains the same: to reinforce the weakened abdominal wall and alleviate symptoms.
Understanding the advantages of bilateral inguinal hernioplasty, including reduced recurrence risk and efficient resource utilization, highlights the importance of this approach in the management of inguinal hernias. As with any surgical procedure, thorough preoperative evaluation, adherence to postoperative care guidelines, and regular follow-up with healthcare providers are crucial for a successful outcome and a smooth recovery.
Meddco is an innovative digital healthcare platform based in India that connects patients with healthcare providers and facilitates easy access to medical services. It aims to simplify the healthcare journey for individuals by providing a comprehensive and user-friendly platform.
Meddco offers a range of features and services to help patients make informed decisions about their healthcare needs. Through the Meddco app or website, users can search for doctors, hospitals, clinics, and diagnostic centers in their vicinity based on their specific requirements. The platform provides detailed information about healthcare providers, including their specialties, qualifications, and patient reviews, enabling patients to make well-informed choices.
One of the key highlights of Meddco is its transparent pricing feature. It allows users to compare the cost of medical procedures and treatments across different healthcare providers, helping them find affordable options without compromising on quality. This feature promotes transparency and empowers patients to make cost-effective decisions.
You can find the best package price in your nearby location.
Additionally, Meddco facilitates online booking of appointments, saving patients time and effort. Users can schedule appointments with doctors or diagnostic centers directly through the platform, eliminating the need for multiple phone calls or physical visits.

---
## [yngrdyn/kibana](https://github.com/yngrdyn/kibana)@[cd909f03b1...](https://github.com/yngrdyn/kibana/commit/cd909f03b1d71da93041a0b5c184243aa6506dea)
#### Wednesday 2023-11-15 09:09:35 by Kyle Pollich

[Fleet] Fix inability to upgrade agents from 8.10.4 -> 8.11 (#170974)

## Summary

Closes https://github.com/elastic/kibana/issues/169825

This PR adds logic to Fleet's `/api/agents/available_versions` endpoint
that will ensure we periodically try to fetch from the live product
versions API at https://www.elastic.co/api/product_versions to make sure
we have eventual consistency in the list of available agent versions.

Currently, Kibana relies entirely on a static file generated at build
time from the above API. If the API isn't up-to-date with the latest
agent version (e.g. kibana completed its build before agent), then that
build of Kibana will never "see" the corresponding build of agent.

This API endpoint is cached for two hours to prevent overfetching from
this external API, and from constantly going out to disk to read from
the agent versions file.

## To do
- [x] Update unit tests
- [x] Consider airgapped environments

## On airgapped environments

In airgapped environments, we're going to try and fetch from the
`product_versions` API and that request is going to fail. What we've
seen happen in some environments is that these requests do not "fail
fast" and instead wait until a network timeout is reached.

I'd love to avoid that timeout case and somehow detect airgapped
environments and avoid calling this API at all. However, we don't have a
great deterministic way to know if someone is in an airgapped
environment. The best guess I think we can make is by checking whether
`xpack.fleet.registryUrl` is set to something other than
`https://epr.elastic.co`. Curious if anyone has thoughts on this.

## Screenshots


![image](https://github.com/elastic/kibana/assets/6766512/0906817c-0098-4b67-8791-d06730f450f6)


![image](https://github.com/elastic/kibana/assets/6766512/59e7c132-f568-470f-b48d-53761ddc2fde)


![image](https://github.com/elastic/kibana/assets/6766512/986372df-a90f-48c3-ae24-c3012e8f7730)

## To test

1. Set up Fleet Server + ES + Kibana
2. Spin up a Fleet Server running Agent v8.11.0
3. Enroll an agent running v8.10.4 (I used multipass)
4. Verify the agent can be upgraded from the UI

---------

Co-authored-by: Kibana Machine <42973632+kibanamachine@users.noreply.github.com>

---
## [TheParasiteProject-Devices/kernel_sony_sm8550](https://github.com/TheParasiteProject-Devices/kernel_sony_sm8550)@[339472d19c...](https://github.com/TheParasiteProject-Devices/kernel_sony_sm8550/commit/339472d19cb9073ba443a0876a18411526772d99)
#### Wednesday 2023-11-15 09:32:13 by Angelo G. Del Regno

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

Signed-off-by: TogoFire <togofire@mailfence.com>
Change-Id: Icef2de24b839ae4b5a51bf90ae0ab9a4d816f329

---
## [Fluffy-Frontier/FluffySTG](https://github.com/Fluffy-Frontier/FluffySTG)@[428aa9384e...](https://github.com/Fluffy-Frontier/FluffySTG/commit/428aa9384ebeb081be35adff2332b21695951f90)
#### Wednesday 2023-11-15 10:09:08 by Iajret Creature

[MIRROR] Hey what if I made Sleeping Carp better at nonlethal takedowns and also deflect with combat mode instead of throw mode (but cost more)  (#499)

* [MIRROR] Hey what if I made Sleeping Carp better at nonlethal takedowns and also deflect with combat mode instead of throw mode (but cost more) [MDB IGNORE] (#24850)

* Hey what if I made Sleeping Carp better at nonlethal takedowns and also deflect with combat mode instead of throw mode (but cost more) (#79517)

## About The Pull Request

It's been a hot minute hasn't it?

When I initially reworked Sleeping Carp, we didn't have combat mode. Now
that we do, and that Sleeping Carp has substantially less defensive
power to justify having to make a choice between deflection and
attacking, it's probably about time we updated this aspect back to what
it was before my rework. Sorta.

Now, we can have all the deniability of the previous method, while also
letting you reliably protect yourself from ranged attacks at all times
while it matters. Because of this, I increased the price up to 17 TC
because of this change just to be on the safe side. The higher uptime of
projectile immunity while also being able to attack during that time
makes this a lot stronger overall.

Secondly, Sleeping Carp presently just isn't as good as a good ol'
baton. It takes a lot more hits to accomplish the same task that a baton
can. Many people feel like they can't even reasonably fight anyone for
fear of the baton, or they would rather use a baton and kill someone at
their leisure. So we've updated some of the moves in order to facilitate
Sleeping Carp as a substantial contender for 1v1 fighting, and lessen
the need for a baton by adding a lot more Stamina damage overall to the
various attacks;

**Keelhaul**: Now a Shove Shove combo. Does literally zero lethal
damage, but now temporarily blinds and dizzies the target as well as its
previous effects. The amount of lethal damage it did was...extremely
small, so this isn't a particularly big loss.

**Grabs and Shoves**: Deal some amount of stamina damage (20). You need
to be in combat mode in order to perform these special attacks (more
deniability). Grabbing someone while they have 80 Stamina damage or more
will cause them to fall unconscious. Yes, I really did just want to add
a Vulcan Nerve Pinch, what do you want from me?

That's it actually. Oh, I guess they are heavy sleepers now too. Because
its funny.

## Why It's Good For The Game

I often get told (read: thrown various insults and slurs at me while
mentioning this as the justification) that Sleeping Carp is not very
strong anymore since it lost all that invisible armor I added way back +
I removed the stuns in my initial rework. This made some people upset (I
think at least one person wished for my death).

So, having given it at least 2 years, I wanted to recapture parts of
what made the older Sleeping Carp (before my rework) strong, some of the
benefits of the new version, and introduce a brand new aspect; nonlethal
takedowns. This makes it beneficial for pacifists, as well as for
kidnapping.

This should not meaningfully make Sleeping Carp any stronger against the
things that typically ruin its day. I suspect in a straight joust with a
baton, Sleeping Carp will still struggle. But against what should be its
strong points (lone targets and ranged weapons), it will be strong once
again rather than clumsily unable to do very much at all.

## Changelog
:cl:
balance: Harnessing Shoreline Quay (bluespace energy, probably), a
mystical energy (total bullshit) that permeates the Astral Waterways
(bluespace quantum dimensions, probably), Sleeping Carp users can now
once against deflect projectiles with their bare hands when focused in
on battle (in combat mode).
balance: The Keelhaul technique is now nonlethal (a philosophical
acknowledgement of the familial bond of sleep and death), but causes the
target to become temporarily blind and dizzy along with its previous
effects.
balance: Sleeping carp users, while in combat mode, deal Stamina damage
with their grabs and shoves. If the target of their grab has enough
Stamina damage (80), they are knocked unconscious from a well placed
nerve pinch.
balance: Sleeping carp users find it very hard to wake up once they fall
asleep....
/:cl:

* Hey what if I made Sleeping Carp better at nonlethal takedowns and also deflect with combat mode instead of throw mode (but cost more)

---------

Co-authored-by: necromanceranne <40847847+necromanceranne@users.noreply.github.com>

* sleeping carp tweaks

---------

Co-authored-by: SkyratBot <59378654+SkyratBot@users.noreply.github.com>
Co-authored-by: necromanceranne <40847847+necromanceranne@users.noreply.github.com>
Co-authored-by: ReezeBL <shilk.e82@gmail.com>

---
## [ignacioct/argilla](https://github.com/ignacioct/argilla)@[300bfa58f1...](https://github.com/ignacioct/argilla/commit/300bfa58f1a7469019921f921f411f1c25bcd984)
#### Wednesday 2023-11-15 10:48:53 by Ayan Joshi

Updated Broken Links  (#4076)

# Argilla Community Growers

Thanks for your contribution! As part of our Community Growers
initiative 🌱, we're donating Justdiggit bunds in your name to reforest
sub-Saharan Africa. To claim your Community Growers certificate, please
contact David Berenstein in our Slack community or fill in this form
https://tally.so/r/n9XrxK once your PR has been merged.

# Pull Request Templates

Please go the the `Preview` tab and select the appropriate sub-template:

* [🐞-bug](?expand=1&template=bug.md)
* [📚-documentation](?expand=1&template=docs.md)
* [🆕-features](?expand=1&template=features.md)

# Generic Pull Request Template

Please include a summary of the changes and the related issue. Please
also include relevant motivation and context. List any dependencies that
are required for this change.



**Type of change**

(Please delete options that are not relevant. Remember to title the PR
according to the type of change)

- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing
functionality to not work as expected)
- [ ] Refactor (change restructuring the codebase without changing
functionality)
- [x] Improvement (change adding some improvement to an existing
functionality)
- [x] Documentation update

**How Has This Been Tested**

(Please describe the tests that you ran to verify your changes. And
ideally, reference `tests`)

- [ ] Test A
- [ ] Test B

**Checklist**

- [x] I added relevant documentation
- [ ] follows the style guidelines of this project
- [ ] I did a self-review of my code
- [ ] I made corresponding changes to the documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or that my
feature works
- [ ] I filled out [the contributor form](https://tally.so/r/n9XrxK)
(see text above)
- [ ] I have added relevant notes to the CHANGELOG.md file (See
https://keepachangelog.com/)

There were two broken links in the Readme , I fixed it of the
cheatsheets and the Contribution guidelines Have a look
at my pr @davidberenstein1957

---
## [KenAdeniji/WordEngineering](https://github.com/KenAdeniji/WordEngineering)@[195bd8680f...](https://github.com/KenAdeniji/WordEngineering/commit/195bd8680fc2dbfbd0269e2eea2cf4df7f1d4e57)
#### Wednesday 2023-11-15 11:17:33 by Ken Adeniji

					<li
						datetime="2023-11-14T05:05:31"
						data-HisWordID="158699"
						data-ContactID="594"
						data-Word="Let's get a space?"
						data-Commentary="We are traveling on a public transport bus and we stopped at a shopping Center. I wanted to buy crackers and I asked a male shopper. He led me westward. I later returned eastward, Center East, to find the crackers among the biscuits. ELarbi Philip Bouhali said to pay $800 extra to a friend for his trade-in vehicle. I entered a big American car through its South door and I expected to enter on the opposite side at the North door. Today is 2023-11-14T15:07:00 at Wienerschnitzel yesterday on 2023-11-13 during my first visit an Asian female showed me mushroom. During my second visit in the evening at the hot stove I saw an advertisement for sample of 2 items meal. A wife, husband, daughter, who wore a top. The family spoke to Julio Moreno and he said 99 Ranch Market, Warm Springs. Jose the Hispanic shopping cart pusher said his name. 2023-11-14 3 masturbation, thrice. 15:27 Dizzy sleepy. 15:10 The voice of Germany, the end of Germany. 2010-08-30T10:08:00 ContactMaintenance.aspx Microsoft windows operating system, Mozilla firefox browser tab closes. I saw the shame of Rome phase II."
					>
						I saw the shame.
					</li>

---
## [pixelkitty286/Citadel-Station-13-RP](https://github.com/pixelkitty286/Citadel-Station-13-RP)@[33cae266af...](https://github.com/pixelkitty286/Citadel-Station-13-RP/commit/33cae266af864b22c509f65ffff3ad7277bbb459)
#### Wednesday 2023-11-15 11:32:39 by Captain277

Subtypes Corporate Crates, Fixes Mapped Biohazard Crate, Renames Advanced Voidsuit (#6126)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

1. *Fixes Bug With Corporate Crates, Subtypes Them.*
2. *Removes Varedited Biohazard Bin and Places Normal Biohazard Bin.*
3. *Changes Advanced Voidsuit Name to Advanced Hardsuit.*

## Why It's Good For The Game

1. _I received reports of one specific corporate crate not rendering
properly when opened. As I inspected it, I realized it would be more
efficient to subtype all corporate crates, so I did that. HOWEVER, this
did not repair the initial bug. For some reason the crate was not
rendering its 'aethersecureopen' state, even though all variables and
code seemed to be working properly. No other crate exhibited this issue.
I discovered that by changing the name of the icon state from
'aethersecureopen' to 'aethersecopen', the state began to enforce and
render properly. I suspected it might be a name length issue, but tests
with other equally long icon states in the crate section disproved this
theory. This may warrant further investigation._
2. _This one avoided detection during my initial sweep through. Can't
remember who just went in and tried to varedit bins to fix biohazards,
but hopefully this is the last one they touched._
3. _This has been driving me crazy for a few days, and yesterday
especially. The Advanced Voidsuit is clearly misnamed, as it is in fact
a Hardsuit. When I tried to order these yesterday I overlooked this
cargo entry twice because I was looking for a hardsuit, not a voidsuit.
This just fixes the name._

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
add: Adds Corporate Crate Subtype, Reassigns Corporate Crates to It.
fix: Fixes incorrectly mapped biohazard bin.
tweak: Changes Name: Advanced Voidsuit to Advanced Hardsuit.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [xparq/Out_of_Nothing](https://github.com/xparq/Out_of_Nothing)@[dc43fa96e9...](https://github.com/xparq/Out_of_Nothing/commit/dc43fa96e9e7d831d519c597e807cd1c3a9b785a)
#### Wednesday 2023-11-15 11:50:50 by sz

Random non-code fixes etc.

+ Close #246 (Engine README, .cfg typo)
+ test.cmd regression: I somehow messed up the `dir` options used to
  find the latest exe (Funny enouh, I broke it as a "fix" to what I
  considered an obscure mistake in that same command line earlier.
  And indeed, it was actually kinda incorrect/redundant, but... OK,
  so just telling it as a warning, folks: SLEEP MORE, FFS!)
+ More notes about inspirations

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[2b0bf5ea5e...](https://github.com/TaleStation/TaleStation/commit/2b0bf5ea5e6afa983130a925463467a26ece0955)
#### Wednesday 2023-11-15 12:57:05 by TaleStationBot

[MIRROR] [MDB IGNORE] Basic Guardians/Holoparasites (#8552)

Original PR: https://github.com/tgstation/tgstation/pull/79473
-----
## About The Pull Request

Fixes #79485
Fixes #77552

Converts Guardians (aka Holoparasites) into Basic Mobs.
Changes a bunch of their behaviours into actions or components which we
can reuse.
Replaces some verbs it would give to you and hide in the status panel
with action buttons that you may be able to find more quickly.

They _**should**_ work basically like they did before but a bit
smoother. It is not unlikely that I made some changes by accident or
just by changing framework though.

My one creative touch was adding random name suggestions.
The Wizard federation have a convention of naming their arcane spirit
guardians by combining a colour and a major arcana of the tarot. The
Syndicate of course won't truck with any of that mystical claptrap and
for their codenames use the much more sensible construction of a colour
and a gamepiece.

This lets you be randomly assigned such creative names as "Sparkling
Hermit", "Bloody Queen", "Blue World", or "Purple Diamond".
You can of course still ignore this entirely and type "The Brapmaster"
into the box if so desired.

I made _one_ other intentional change, which is to swap to Mothblocks'
nice leash component instead of instantly teleporting guardians back to
you when they are pulled out of the edge of their range. They should now
be "dragged" along behind you until they can't path, at which point they
will teleport. This should make the experience a bit less disorienting,
you have the recall button if you _want_ to instantly catch up.

This is unfortunately a bumper-sized PR because it did not seem
plausible to not do all of it at once, but I can make a project branch
for atomisation if people think this is too much of a pain in the ass to
review.

Other changes:
- Some refactoring to how the charge action works so I could
individually override "what you can hit" and "what happens when you hit"
instead of those being the same proc
- Lightning Guardian damage chain is now a component
- Explosive Guardian explosive trap is now a component
- Added even more arguments to the Healing Touch component to allow it
to heal tox/oxy damage and require a specific click modifier
- Life Link component which implements the Guardian behaviour of using
another mob as your health bar
- Moved some stuff about deciding what guardians look and are described
like into a theming datum
- Added a generic proc which can return whether your mob is meant to
apply some kind of damage multiplier to a certain damage type. It's not
perfect because I couldn't figure out how ot cram limb modifiers in
there, which is where most of it is on carbons. Oh well.
- Riders of vehicles now inherit all movement traits of those vehicles,
so riding a charging holoparasite will let you cross chasms. Also works
if you piggyback someone with wings, probably.

## Changelog

:cl:
refactor: Guardians/Powerminers/Holoparasites now use the basic mob
framework. Please report any unexpected changes or behaviour.
qol: The verbs used to communicate with, recall, or banish your Guardian
are now action buttons.
balance: If (as a Guardian) your host moves slightly out of range you
will now be dragged back into range if possible, rather than being
instantly teleported to them.
balance: Protectors now have a shorter leash range rather than a longer
one, in order to more easily take advantage of their ability to drag
their charge out of danger.
balance: Ranged Guardians can now hold down the mouse button to fire
automatically.
balance: People riding vehicles or other mobs now inherit all of their
movement traits, so riding a flying mob (or vehicle, if we have any of
those) will allow you to cross chasms and lava safely.
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>
Co-authored-by: san7890 <the@san7890.com>

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[ba7c4b3993...](https://github.com/TaleStation/TaleStation/commit/ba7c4b3993e8e5d78c03123d26fb79e7f26e7ca7)
#### Wednesday 2023-11-15 12:57:05 by TaleStationBot

[MIRROR] [MDB IGNORE] Adds garbage dumpster ruins (#8542)

Original PR: https://github.com/tgstation/tgstation/pull/79446
-----

## About The Pull Request
Adds 4 small space ruins. Each is a dumpster in space containing hostile
mobs to fight and items to bring back to the station. There's a
decommissioned garbage truck pulling each dumpster which acts as a
staging area before you take on the mobs inside.
All the fights are in cramped dark areas with full pressure, air is
breathable but sometimes has miasma in it so beware of getting sick. So
you can drop your space suit and put on armour, but PKAs won't fire at
full power and keeping a gas mask on is recommended.
Also all the dumpsters look the same from the outside so you gotta crawl
inside to know what's inside. And no you can't metagame it with mesons
either.

Comes in the following flavours:
Food Waste
Full of trash from kitchens, and food. Some of the food is still edible.
There's a lot of territorial rats. You can chop them up into meat if you
want more food. The big prize is a big vat of cooking oil.

Medical Waste
Spare organs, cyberorgans and almost a full set of old surgical gear.
There's a syndicate agent here up to no good and he has a GUN. The gun
blows up when the agent dies so you can't get it. There's a few corpses
of different species in bodybags and some spare corpse parts so you can
bring them back to the station and give them to the coroner. Also a
single use eyestealer in a safe (the cool way to do surgery) and a bug
from the old traitor objective that doesn't do jack but can probably
still get you thrown in perma.

Construction Garbage
Tools and construction materials here, including a cool hammer that fits
in a tool belt and can function as a crowbar. There's also a drug lab
with plenty of weird pills to eat, cigarettes to eat and an angry
russian drug dealer who will stab you if he sees you. He has a badass
lighter and a flamethrower you can take after you kill him. Setting fire
to things in here is not recommended because of all the welding fuel.

Mall Trash
Action figures, trading cards, Christmas crackers and other trash the
local mall tossed out. Also a mothman used to live here but he got eaten
by giant spiders so you can grab his stuff, including snacks and a
civilian modsuit with no mods (wow). You can cut through the webs to
kill the spiders or let them eat you too if you want.
## Why It's Good For The Game
More content for space explorers.
More variety to the potential dangers of space, now u can get sick and
die or get eaten by rats (this is hobo RP)
Better environmental storytelling. Now instead of players left asking
"what happens to the garbage when it goes into space" they can rest
assured that there's busted ass garbage trucks in space. All their
questions are answered.
Loot that encourages working with people on the station. Raw food for
the kitchen, rats for genetics, organs for the coroner, etc
## Changelog
:cl:
add: 4 new space ruins
/:cl:

---------

Co-authored-by: DaCoolBoss <142358580+DaCoolBoss@users.noreply.github.com>

---
## [Samruddhi2003github/Landing-Page-Main](https://github.com/Samruddhi2003github/Landing-Page-Main)@[0306a6c590...](https://github.com/Samruddhi2003github/Landing-Page-Main/commit/0306a6c590d13b85a6ac9c926e1583ccd2e3a91f)
#### Wednesday 2023-11-15 13:15:10 by Samruddhi2003github

Create README.md

Thank you for visiting our Love Leaf Cafe Website! We hope you find it easy to use and enjoy your food experience. If you have any questions or feedback, please don't hesitate to contact us.

oibsip_taskno.1

---
## [Bol-o/CSS-stuff](https://github.com/Bol-o/CSS-stuff)@[5b8e3258cf...](https://github.com/Bol-o/CSS-stuff/commit/5b8e3258cf85816b8faaa6d9c3f2781abb52c33c)
#### Wednesday 2023-11-15 13:31:37 by Bolo

BLoody commit messages and git all together

Hopefully one day I will get git, and it won't piss me off so much.
It's probably, sounds like it, an amazing tool, so for now will take it
easy and won't format the computer and get rid of all this shit.

---
## [MajManatee/Yogstation](https://github.com/MajManatee/Yogstation)@[bc3374c7da...](https://github.com/MajManatee/Yogstation/commit/bc3374c7dacf3b2db39fe1c4dc36551d7ba82f79)
#### Wednesday 2023-11-15 14:02:40 by cowbot92

Even Further Heretic Adjustments: New minor things, Bug fixes, Heretic path adjustments and movement adjustments! (#20843)

* a whole lot of shit

yessir

* gun stuff

crazy

* haha

fuck guns

* my brain bursts

it hurts

* so much shit

im done

* fuck forgot this

god damn low memory mode

* removes backslashes

really linter

* oops

typos

---
## [PastelPrinceDan/Skyrat-tg](https://github.com/PastelPrinceDan/Skyrat-tg)@[69ea3c81ad...](https://github.com/PastelPrinceDan/Skyrat-tg/commit/69ea3c81ad86a0356af947f11fe3bd2ca953b0af)
#### Wednesday 2023-11-15 14:16:34 by SkyratBot

[MIRROR] Mafia can be played on your PDA [MDB IGNORE] (#24485)

* Mafia can be played on your PDA (#78576)

## About The Pull Request

Mafia is now friggin playable from the PDA, I also changed other stuff
too

- You can't use abilities on dead people if you're not supposed to (cant
kill the same person over and over)
- Changelings cant kill other Changelings
- Changelings can now only talk to eachother at night, rather than using
:j
- Everyone starts spawned in the center of the map, since people playing
on PDA can't move their characters. This is so everyone can hear PDA
users in person, as I don't want the chat log to be mandatory.

To do this, all messages you are meant to be able to see, is now logged
for you to see in your Mafia panel. This essentially means that people
playing through the PDA get a downgraded version of it, but I don't know
how much larger I want this UI to be.

Playing Mafia through the PDA will not tell you of other players ahead
of time when signing up (as it shows ckeys + pdas), but they can see the
names in-game. Unfortunately this means we'll have to remove your
customization coming with you, to prevent using it to tell who is dead
in round.

Things I am missing
- Program overlays on PDA/Laptop/Computer
- Icon for the app's header while a game is active

I'm not a spriter and can't make either of these

This is the new UI

![image](https://github.com/tgstation/tgstation/assets/53777086/7cf503d9-b2e2-4127-874a-acad6425d649)

I also fixed alert calls for PDAs and stuff

![image](https://github.com/tgstation/tgstation/assets/53777086/e09b2e5e-b9e7-43ae-9273-c168e9c8e642)

and removed the X at the top on computers since they had no battery

![image](https://github.com/tgstation/tgstation/assets/53777086/d3dd8307-805c-4aba-be5e-4c24a0bdcb91)

Looks a little better now hopefully 👍

## Why It's Good For The Game

- The current Arcade app sucks, and is a solo game. This is much more
entertaining and you can talk to others in it, which is swag as fuck.
- There's a larger potential playerbase for the Minigame making it more
likely to be played.
- Sets groundwork for a better version of
https://github.com/tgstation/tgstation/pull/75879
- Adds more suspense and teamwork in the minigame.

## Changelog

:cl: JohnFulpWillard, sprites by CoiledLamb
add: You can now play Mafia on your PDA.
balance: Mafia changelings can now only talk to eachother during the
night.
fix: Mafia abilities can't be repeatedly used on people.
/:cl:

* Mafia can be played on your PDA

---------

Co-authored-by: John Willard <53777086+JohnFulpWillard@users.noreply.github.com>

---
## [PastelPrinceDan/Skyrat-tg](https://github.com/PastelPrinceDan/Skyrat-tg)@[c63f897521...](https://github.com/PastelPrinceDan/Skyrat-tg/commit/c63f897521485898e00425a6c001495f7eef5de6)
#### Wednesday 2023-11-15 14:16:34 by SkyratBot

[MIRROR] It is now possible to survive the Mansus  [MDB IGNORE] (#24490)

* It is now possible to survive the Mansus  (#79131)

## About The Pull Request

Fixes #79113

There were a handful of bugs with the Mansus realm, this PR fixes them.

Firstly an most importantly, a refactor to damage handling touched the
"unholy determination" effect incorrectly (and I'm not even sure why?),
causing it to damage you instead of healing you most of the time. This
damage was not avoidable, so most people would be crit shortly after
entering the area and stay there.

Secondly, some of the heretic realms were unlit. A change to when
lazyloaded template atmosphere initialises means that the bonfires were
trying to light themselves with no air. Now they do this in
late_initialize instead, giving time for air to arrive.

Thirdly, the spooky hands were runtiming when passing through transit
tiles outside of the bounds of the heretic map. They shouldn't be
effected by shuttle drag anyway, so now they aren't.

Fourthly, I removed a row of empty space at the edge of the heretic map,
just because it annoyed me slightly.

Finally, while I was touching the heretic buff I made it heal you 1/4 as
much as it originally did. This is a balance change rather than a fix,
I'll atomise it out if it is controversial but I don't really expect it
to be.
In the future I would like to come back to these and make each realm
more specific to the path, because I think we could make these both more
exciting and more characterful.

## Why It's Good For The Game

Once it is working properly, the hand dodging minigame is actually
extremely forgiving, even if you don't move very much and get frequently
hit. This means some of those hits might actually add some tension.

## Changelog

:cl:
fix: You should be revived properly when entering the mansus realm
following a heretic sacrifice
fix: The buff which is supposed to heal you in the mansus realm will now
do that instead of unavoidably damaging you
balance: The mansus realm's healing buff heals for 25% as much as it did
before it was broken
/:cl:

* It is now possible to survive the Mansus

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [PastelPrinceDan/Skyrat-tg](https://github.com/PastelPrinceDan/Skyrat-tg)@[53cfff6ae1...](https://github.com/PastelPrinceDan/Skyrat-tg/commit/53cfff6ae1cd62766395534a6f4c8aa468c5066c)
#### Wednesday 2023-11-15 14:16:34 by SkyratBot

[MIRROR] Actually supports alpha passed into emissive stuff [MDB IGNORE] (#24481)

* Actually supports alpha passed into emissive stuff (#79117)

## About The Pull Request

Ok so like, the emissive procs have an alpha argument right? The thing
is, the thing is it doesn't fucking do anything.

Alpha is a component of the color var (at least when it's a matrix), so
when we set alpha and then set color to a matrix, the alpha gets
overriden. Inverse is also true.

I want to support alpha args, since I like the idea of dimmable
emissives. Soooooo
Let's take the alpha arg, divide it by 255, and replace everything that
cares about alpha (as an intensity thing) with it.

This lets us do transparent emissives and transparent emissive blockers.

I added some guard checks to hopefully avoid the list init most of the
time (it is in theory comprable since color sets should copy but I don't
trust byond to optimize for that)
Also modified the macros to suppport what I'm doing nicely

## Why It's Good For The Game

We should support this, and now we do

* Actually supports alpha passed into emissive stuff

---------

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [zizo1414/python-projects-](https://github.com/zizo1414/python-projects-)@[e728672feb...](https://github.com/zizo1414/python-projects-/commit/e728672feb8a76e8380d9cef55d8ff2afa602aa9)
#### Wednesday 2023-11-15 14:22:29 by zeyad anan

 tv data.py

1. TV, halftime shows, and the Big Game
Whether or not you like football, the Super Bowl is a spectacle. There's a little something for everyone at your Super Bowl party. Drama in the form of blowouts, comebacks, and controversy for the sports fan. There are the ridiculously expensive ads, some hilarious, others gut-wrenching, thought-provoking, and weird. The half-time shows with the biggest musicians in the world, sometimes riding giant mechanical tigers or leaping from the roof of the stadium. It's a show, baby. And in this notebook, we're going to find out how some of the elements of this show interact with each other. After exploring and cleaning our data a little, we're going to answer questions like:

What are the most extreme game outcomes?
How does the game affect television viewership?
How have viewership, TV ratings, and ad cost evolved over time?
Who are the most prolific musicians in terms of halftime show performances?

---
## [bevyengine/bevy](https://github.com/bevyengine/bevy)@[ab300d0ed9...](https://github.com/bevyengine/bevy/commit/ab300d0ed9990972679629af3ef18fd37c0e106c)
#### Wednesday 2023-11-15 14:35:41 by Connor King

Gizmo Arrows (#10550)

## Objective

- Add an arrow gizmo as suggested by #9400 

## Solution

(excuse my Protomen music)


https://github.com/bevyengine/bevy/assets/14184826/192adf24-079f-4a4b-a17b-091e892974ec

Wasn't horribly hard when i remembered i can change coordinate systems
whenever I want. Gave them four tips (as suggested by @alice-i-cecile in
discord) instead of trying to decide what direction the tips should
point.

Made the tip length default to 1/10 of the arrow's length, which looked
good enough to me. Hard-coded the angle from the body to the tips to 45
degrees.

## Still TODO

- [x] actual doc comments
- [x] doctests
- [x] `ArrowBuilder.with_tip_length()`

---

## Changelog

- Added `gizmos.arrow()` and `gizmos.arrow_2d()`
- Added arrows to `2d_gizmos` and `3d_gizmos` examples

## Migration Guide

N/A

---------

Co-authored-by: Nicola Papale <nicopap@users.noreply.github.com>

---
## [KDE/krita](https://github.com/KDE/krita)@[b520fe1920...](https://github.com/KDE/krita/commit/b520fe1920ed3e5d1caab994d814bf8bd1b07650)
#### Wednesday 2023-11-15 14:42:57 by Maciej Jesionowski

Draw assistants directly on the canvas

Change the way assistants are rendered on the canvas. Instead of drawing
the assistants into a pixmap, storing the pixmap in QPixmapCache, and
then painting the pixmap onto the canvas, this patch skips the intermediate
pixmap and draws the assistants directly on the canvas.

The QPixmapCache method is prone to a bug where the pixmap is evicted
from the cache before the rendering is complete, resulting in a black
rectangle. Also this method performs very poorly with hardware acceleration,
because we're doing a costly texture upload, texture sampling, and blending.
The performance is especially bad when assistants take a large portion
of the screen when zoomed in and the canvas is zoomed or rotated.

Changes in this patch:

- Add a menu option in Display settings to toggle assistants drawing mode
- Use direct drawing mode by default
- Remove the workaround detection for NVIDIA

The old options are left for troubleshooting, but it's unlikely anyone
would find them to work better on the current GPU hardware.

BUG:361709
BUG:401940

---
## [krnowak/systemd](https://github.com/krnowak/systemd)@[1761066b13...](https://github.com/krnowak/systemd/commit/1761066b135f1a322c446f102343ea4aa61fe3ee)
#### Wednesday 2023-11-15 15:50:29 by Lennart Poettering

storagetm: add new systemd-storagetm component

This implements a "storage target mode", similar to what MacOS provides
since a long time as "Target Disk Mode":

        https://en.wikipedia.org/wiki/Target_Disk_Mode

This implementation is relatively simple:

1. a new generic target "storage-target-mode.target" is added, which
   when booted into defines the target mode.

2. a small tool and service "systemd-storagetm.service" is added which
   exposes a specific device or all devices as NVMe-TCP devices over the
   network.  NVMe-TCP appears to be hot shit right now how to expose
   block devices over the network. And it's really simple to set up via
   configs, hence our code is relatively short and neat.

The idea is that systemd-storagetm.target can be extended sooner or
later, for example to expose block devices also as USB mass storage
devices and similar, in case the system has "dual mode" USB controller
that can also work as device, not just as host. (And people could also
plug in sharing as NBD, iSCSI, whatever they want.)

How to use this? Boot into your system with a kernel cmdline of
"rd.systemd.unit=storage-target-mode.target ip=link-local", and you'll see on
screen the precise "nvme connect" command line to make the relevant
block devices available locally on some other machine. This all requires
that the target mode stuff is included in the initrd of course. And the
system will the stay in the initrd forever.

Why bother? Primarily three use-cases:

1. Debug a broken system: with very few dependencies during boot get
   access to the raw block device of a broken machine.

2. Migrate from system to another system, by dd'ing the old to the new
   directly.

3. Installing an OS remotely on some device (for example via Thunderbolt
   networking)

(And there might be more, for example the ability to boot from a
laptop's disk on another system)

Limitations:

1. There's no authentication/encryption. Hence: use this on local links
   only.

2. NVMe target mode on Linux supports r/w operation only. Ideally, we'd
   have a read-only mode, for security reasons, and default to it.

Future love:

1. We should have another mode, where we simply expose the homed LUKS
   home dirs like that.

2. Some lightweight hookup with plymouth, to display a (shortened)
   version of the info we write to the console.

To test all this, just run:

    mkosi --kernel-command-line-extra="rd.systemd.unit=storage-target-mode.target" qemu

---
## [openai/evals](https://github.com/openai/evals)@[8d32b347f0...](https://github.com/openai/evals/commit/8d32b347f05fd2a735ff5d8745a0a4680bdfcce8)
#### Wednesday 2023-11-15 15:53:12 by johny-b

Bluff eval (#1402)

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

bluff

### Eval description

Evaluate how well a model can play (a variant of) the game of bluff,
also known as "liar's dice".

### What makes this a useful eval?

This is a game of deception - you have to deceive your opponent and
understand when you are deceived.
Models performing very well on this eval could also be capable of
deceiving humans in real-life scenarios.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [X] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should

- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

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

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `mypy`, `black`,
`isort`, `autoflake` and `ruff` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
  INSERT_EVAL_HERE
  ```
</details>

---
## [axelzonvolt/lizardsmashingkeyboard](https://github.com/axelzonvolt/lizardsmashingkeyboard)@[40dfaf3734...](https://github.com/axelzonvolt/lizardsmashingkeyboard/commit/40dfaf3734000b5e74e4101ab86516702f59425f)
#### Wednesday 2023-11-15 16:44:39 by Imaginos16

Reworks The Visuals Of Independent And Nanotrasen Captains (#2453)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Does what it says in the title. This is a demented PR that touches a lot
of things, but its main benefit is that now regular independent
captains, cowboy independent captains, and nanotrasen captains have a
unique identity.

Of those changed, it includes:

- The Nanotrasen Captain (parade)

![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/48a31cb1-b266-43cb-9b6e-525028893011)

- The Nanotrasen Captain (regular)

![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/799c88f0-b7ce-4736-956d-2e9c0a096433)

- The Independent Captain (regular/parade)

![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/17ecb3d3-5f2f-4ce0-a518-81366945ebdf)

- The Independent Captain (western)

![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/a56a798c-5adf-41d7-917a-730661f306ed)

The PR also axes a bunch of unused, or frankly quite basic lieutenant
outfits that were nothing more than set dressing with not much substance
behind them. The roles were not removed for now, and they have
appropriate outfits as a placeholder pending a full removal.

This also means that the Head of Personnel was slightly touched up,
mostly by having a coat and hat similar to the western captain's when
appropriate. The role itself is pending a full visual rework for later
that is beyond the scope of this PR.

Speaking of removals, this also means that captain outfits/roles that
were there as a legacy of removed ships, were finally axed for good.
Goodbye deserter captain for Riggs variant number 4, you will not be
missed.

This PR also touches several (a lot) of maps, mostly adding/removing
outfits that were either missing, or didn't fit with the dress code of
the vessel.

Also the PR fixes an oversight by @MarkSuckerberg by making the BYOND
version warning an actual warning, instead of an error when compiling.
Etto bleh.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
Visual cohesion is important, and dear fucking god if I see one more
independent western captain not wearing the duster because it wasn't in
the ship, I will weep, and my weeping will cause a biblical deluge.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: PositiveEntropy
imageadd: Outfits for independent and Nanotrasen captains have been
violently reworked.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [cockroachdb/cockroach](https://github.com/cockroachdb/cockroach)@[d1ddc072a8...](https://github.com/cockroachdb/cockroach/commit/d1ddc072a8c10c7568166af9495e6418df3e5a22)
#### Wednesday 2023-11-15 16:48:14 by craig[bot]

Merge #114273

114273: pkg/util/aggmetric: tick histogram windows in AggHistogram r=aadityasondhi a=abarganier

Fixes: https://github.com/cockroachdb/cockroach/issues/114175, https://github.com/cockroachdb/cockroach/issues/112947

**NOTE**: The ideal way to fix this is merging `pkg/util/metric/aggmetric` into 
`pkg/util/metric`. That way, we wouldn't have to expose any of the "tick" 
functionality in the histogram public API. However, merging the two packages 
would be a pain to backport, and therefore we're leaving the merging to a 
follow up PR (coming soon). In the meantime, this provides a fix with a minimized 
surface area, so that we can more easily backport the fix. The merging will only 
occur on the master branch. 

**Reviewer note:** Recommended to review commit-wise.

---

AggHistograms are wrappers around the histogram implementations found in
pkg/util/metric. Internally, Histogram implementations within
pkg/util/metric maintain histogram windows to calculate quantiles at
each scrape by CockroachDB's TSDB, instead of storing every single
histogram bucket. These windows are rotated periodically, where the
current window becomes the previous window, and the current window is
then set to a new histogram. This allows us to diff the two windows, and
internally, pkg/util/metric has "ticking" functionality which is
responsible for rotating these histogram windows.

Unfortunately, since `pkg/util/metric/aggmetric` is in a separate
package, somehow this "ticking"/rotating of histogram windows was never
implemented into the AggHistogram. Because of this, it's likely that
metrics powered by AggHistogram have been broken since its inception
within CockroachDB's internal TSDB (but work fine in Prometheus).

Previous patches did some work to expose this ticking library to
AggHistogram, and this patch implements it.

In this patch, we make it so AggHistogram ticks/rotates histogram
windows, similar to how the other Histogram library does it. Since
AggHistograms have child histograms, this means that the rotation of all
histograms for both parent and children need to be done atomically. We
implement this by providing the AggHistogram its own tick.Ticker, where
the onTick function holds a RWMutex shared by the parent & all its
children and rotates the histograms for all.

With this in place, histogram windows are properly rotated for
AggHistograms. Future work will merge `pkg/util/metric/aggmetric` into
`pkg/util/metric`, after which we can once again make all this ticking
functionality private to the metrics package.

Release note (bug fix): Previously, all `AggHistogram`-powered metrics
were not reporting quantiles properly in DB Console. The list of
affected metrics is:

- changefeed.message_size_hist
- changefeed.parallel_io_queue_nanos
- changefeed.sink_batch_hist_nanos
- changefeed.flush_hist_nanos
- changefeed.commit_latency
- changefeed.admit_latency
- jobs.row_level_ttl.span_total_duration
- jobs.row_level_ttl.select_duration
- jobs.row_level_ttl.delete_duration

This patch fixes the histograms so that the quantiles in DB Console are
reported correctly.

Please note: these histograms were only broken in the DB Console metrics
features, but were **not** broken in the Prometheus-compatible endpoint,
`/_status/vars`.

## Screenshots

#### AggHistogram in DB Console pre-fix:
![pre](https://github.com/cockroachdb/cockroach/assets/8194877/aa08592b-4ebd-43d5-acff-8d00edc4ada1)

#### AggHistogram in DB Console post-fix:
<img width="1059" alt="Screenshot 2023-11-10 at 4 06 57 PM" src="https://github.com/cockroachdb/cockroach/assets/8194877/723c4974-e038-4871-9721-8ec18fca5f95">

#### AggHistogram in Grafana post-fix:
<img width="1648" alt="Screenshot 2023-11-10 at 4 07 22 PM" src="https://github.com/cockroachdb/cockroach/assets/8194877/05920189-c1b1-4895-a1fa-b8b1e069407a">


Co-authored-by: Alex Barganier <abarganier@cockroachlabs.com>

---
## [james-aung/evals](https://github.com/james-aung/evals)@[db8b3dfe6f...](https://github.com/james-aung/evals/commit/db8b3dfe6f69450577314bba40582bfa41bd06a9)
#### Wednesday 2023-11-15 17:01:58 by Thiago M. Nóbrega

Add A is B and B is A Eval (#1366)

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

ab

### Eval description

This evaluation aims to assess the model's ability to correctly identify
and understand the relationship between two entities, where A is a
specific entity (which could be a chemical element, a painting, a bird
species, a star, a mountain, a novel, a river, or a musical instrument)
and B is a unique characteristic or fact about that entity. The model
should be able to accurately interpret the user's query about the entity
(A) and provide a relevant fact (B), and vice versa. This evaluation
will help in fine-tuning the model's understanding of context, relation
between entities, and its ability to provide accurate and relevant
responses. The entities and their characteristics have been chosen to be
specific and challenging.

### What makes this a useful eval?

This evaluation is important for several reasons:

1. Contextual Understanding: It tests the model's ability to understand
the context of a conversation, particularly the relationship between two
related entities (A and B).

2. Accuracy: It assesses the model's ability to provide accurate and
relevant information based on the user's query.

3. Relevance: It evaluates the model's ability to understand the
relevance of A to B and vice versa, which is crucial in providing
meaningful and coherent responses.

4. General Knowledge: This tests the model's knowledge about various
specific entities and their unique characteristics or facts, which is a
part of its general knowledge. The entities span a wide range of
categories, including chemistry, art, ornithology, astronomy, geography,
literature, and music, making this a comprehensive test of the model's
general knowledge.

5. Versatility: This checks the model's ability to handle different
types of queries, as the user can ask about the specific entity (A) or
its unique characteristic or fact (B). This tests the model's
flexibility in understanding and responding to a variety of query
structures across diverse knowledge domains.

gpt-3.5-turbo
[2023-10-10 22:42:42,192] [oaieval.py:229] Final report:
[2023-10-10 22:42:42,192] [oaieval.py:231] counts/A: 2
[2023-10-10 22:42:42,192] [oaieval.py:231] counts/B: 11
[2023-10-10 22:42:42,192] [oaieval.py:231] counts/D: 2
[2023-10-10 22:42:42,192] [oaieval.py:231] counts/C: 1

gpt-4
[2023-10-10 22:43:37,306] [oaieval.py:229] Final report:
[2023-10-10 22:43:37,306] [oaieval.py:231] counts/C: 7
[2023-10-10 22:43:37,306] [oaieval.py:231] counts/B: 7
[2023-10-10 22:43:37,306] [oaieval.py:231] counts/D: 2

class: modelgraded.classify:ModelBasedClassify
eval_type: cot_classify
modelgraded_spec: fact

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

A popular paper has been going around called 'The Reversal Curse: LLMs
trained on “A is B” fail to learn “B is A”'. I figured an Eval on this
would have a unique value.

## Eval structure 🏗️

Your eval should

- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

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

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
- [x] (Ignore if not submitting code) I have run `pip install
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
{"input": [{"role": "system", "content": "The user will ask you a
question about a specific chemical element that has the atomic number
79, please respond to the best of your abilities."}, {"role": "user",
"content": "What is the name of the element with atomic number 79?"}],
"ideal": "The element with atomic number 79 is Gold."}
{"input": [{"role": "system", "content": "The user will ask you a
question about a chemical element that is often associated with jewelry
and has the symbol Au, please respond to the best of your abilities."},
{"role": "user", "content": "Which element is this?"}], "ideal": "This
element is Gold."}
{"input": [{"role": "system", "content": "The user will ask you a
question about a specific painting that was stolen from the Isabella
Stewart Gardner Museum in 1990, please respond to the best of your
abilities."}, {"role": "user", "content": "What is the name of the
Vermeer painting stolen from the Isabella Stewart Gardner Museum in
1990?"}], "ideal": "The name of the Vermeer painting stolen from the
Isabella Stewart Gardner Museum in 1990 is 'The Concert'."}
{"input": [{"role": "system", "content": "The user will ask you a
question about a Vermeer painting that is still missing after being
stolen from a museum in Boston, please respond to the best of your
abilities."}, {"role": "user", "content": "Which painting is this?"}],
"ideal": "This painting is 'The Concert'."}
{"input": [{"role": "system", "content": "The user will ask you a
question about a specific species of bird that is known for its
elaborate courtship dance, please respond to the best of your
abilities."}, {"role": "user", "content": "What is the name of the bird
species known for its moonwalk-like courtship dance?"}], "ideal": "The
bird species known for its moonwalk-like courtship dance is the Blue
Manakin."}
{"input": [{"role": "system", "content": "The user will ask you a
question about a bird species that is known for its blue color and
unique courtship dance, please respond to the best of your abilities."},
{"role": "user", "content": "Which bird species is this?"}], "ideal":
"This bird species is the Blue Manakin."}

  ```
</details>

---
## [james-aung/evals](https://github.com/james-aung/evals)@[4b7a66bd45...](https://github.com/james-aung/evals/commit/4b7a66bd45f06156656e021e170e7574f6cde3f5)
#### Wednesday 2023-11-15 17:01:58 by Vilhjalmur Thorsteinsson

Added Icelandic inflection eval; JsonMatch eval function (#1387)

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

Icelandic noun phrase inflection

### Eval description

This eval consists of 3 x 100 samples in "easy", "medium" and "hard"
categories. Each sample
represents the task of inflecting a noun phrase in Icelandic, in all
four cases of the language
(nominative, accusative, dative and genitive), both singular and plural.
A noun phrase
consists of an adjective and a noun (e.g., "fallegur litur" = "beautiful
color").
In the easy category, both the adjective and the noun are
relatively common. In the medium category, they are less common, and in
the hard category they
are rare enough that it is pretty unlikely that they occur in any
training corpora.

### What makes this a useful eval?

The eval is designed to test the general grammatical proficiency of a
model in Icelandic, and
the eval accuracy is assumed to correlate with a model's ability to
generate grammatically
correct text in the language. GPT models have so far struggled with
generating correct Icelandic
text, even though GPT-4 was uniquely trained by RLHF in the language.
Icelandic is believed to
be a good bellwether for lower-resource, grammatically complex language
support in general.

Inflecting noun phrases is something that native language speakers do
without significant
effort, even if they have not seen the particular adjective and the noun
before, as it can be done on the
basis of generic grammatical pattern recognition. However, to date,
GPT-4 seems not to have
acquired enough of a "native feel" for Icelandic to be able to do this
task with high accuracy.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should

- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

**Note: this PR includes a new general eval class, JsonMatch, which is
not specific to the Icelandic evaluation
case. It allows completions and ideal answers to be represented as JSON
objects, comparing the objects
by individual key:value pairs. Tests and documentation of this
functionality are included in the PR.**

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (<https://platform.openai.com/docs/usage-policies>).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `mypy`, `black`,
`isort`, `autoflake` and `ruff` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "Þú ert sérfræðingur í
íslenskri málfræði."}, {"role": "user", "content": "Hvernig fallbeygist
nafnliðurinn \"palestínskur fréttavefur\" í öllum föllum (nf, þf, þgf,
ef), eintölu (et) og fleirtölu (ft), án greinis? Svaraðu í *JSON formi
eingöngu* og auðkenndu tölur og föll með skammstöfunum et, ft, nf, þf,
þgf, ef."}], "ideal": "{\"et\": {\"nf\": \"palestínskur fréttavefur\",
\"þf\": \"palestínskan fréttavef\", \"þgf\": \"palestínskum fréttavef\",
\"ef\": \"palestínsks fréttavefjar\"}, \"ft\": {\"nf\": \"palestínskir
fréttavefir\", \"þf\": \"palestínska fréttavefi\", \"þgf\":
\"palestínskum fréttavefjum\", \"ef\": \"palestínskra fréttavefja\"}}"}
{"input": [{"role": "system", "content": "Þú ert sérfræðingur í
íslenskri málfræði."}, {"role": "user", "content": "Hvernig fallbeygist
nafnliðurinn \"hliðhollt lyfjapróf\" í öllum föllum (nf, þf, þgf, ef),
eintölu (et) og fleirtölu (ft), án greinis? Svaraðu í *JSON formi
eingöngu* og auðkenndu tölur og föll með skammstöfunum et, ft, nf, þf,
þgf, ef."}], "ideal": "{\"et\": {\"nf\": \"hliðhollt lyfjapróf\",
\"þf\": \"hliðhollt lyfjapróf\", \"þgf\": \"hliðhollu lyfjaprófi\",
\"ef\": \"hliðholls lyfjaprófs\"}, \"ft\": {\"nf\": \"hliðholl
lyfjapróf\", \"þf\": \"hliðholl lyfjapróf\", \"þgf\": \"hliðhollum
lyfjaprófum\", \"ef\": \"hliðhollra lyfjaprófa\"}}"}
{"input": [{"role": "system", "content": "Þú ert sérfræðingur í
íslenskri málfræði."}, {"role": "user", "content": "Hvernig fallbeygist
nafnliðurinn \"refsiverð stjörnuleit\" í öllum föllum (nf, þf, þgf, ef),
eintölu (et) og fleirtölu (ft), án greinis? Svaraðu í *JSON formi
eingöngu* og auðkenndu tölur og föll með skammstöfunum et, ft, nf, þf,
þgf, ef."}], "ideal": "{\"et\": {\"nf\": \"refsiverð stjörnuleit\",
\"þf\": \"refsiverða stjörnuleit\", \"þgf\": \"refsiverðri
stjörnuleit\", \"ef\": \"refsiverðrar stjörnuleitar\"}, \"ft\": {\"nf\":
\"refsiverðar stjörnuleitir\", \"þf\": \"refsiverðar stjörnuleitir\",
\"þgf\": \"refsiverðum stjörnuleitum\", \"ef\": \"refsiverðra
stjörnuleita\"}}"}
{"input": [{"role": "system", "content": "Þú ert sérfræðingur í
íslenskri málfræði."}, {"role": "user", "content": "Hvernig fallbeygist
nafnliðurinn \"japönsk landbúnaðarvara\" í öllum föllum (nf, þf, þgf,
ef), eintölu (et) og fleirtölu (ft), án greinis? Svaraðu í *JSON formi
eingöngu* og auðkenndu tölur og föll með skammstöfunum et, ft, nf, þf,
þgf, ef."}], "ideal": "{\"et\": {\"nf\": \"japönsk landbúnaðarvara\",
\"þf\": \"japanska landbúnaðarvöru\", \"þgf\": \"japanskri
landbúnaðarvöru\", \"ef\": \"japanskrar landbúnaðarvöru\"}, \"ft\":
{\"nf\": \"japanskar landbúnaðarvörur\", \"þf\": \"japanskar
landbúnaðarvörur\", \"þgf\": \"japönskum landbúnaðarvörum\", \"ef\":
\"japanskra landbúnaðarvara\"}}"}
{"input": [{"role": "system", "content": "Þú ert sérfræðingur í
íslenskri málfræði."}, {"role": "user", "content": "Hvernig fallbeygist
nafnliðurinn \"dýrmætt vistheimili\" í öllum föllum (nf, þf, þgf, ef),
eintölu (et) og fleirtölu (ft), án greinis? Svaraðu í *JSON formi
eingöngu* og auðkenndu tölur og föll með skammstöfunum et, ft, nf, þf,
þgf, ef."}], "ideal": "{\"et\": {\"nf\": \"dýrmætt vistheimili\",
\"þf\": \"dýrmætt vistheimili\", \"þgf\": \"dýrmætu vistheimili\",
\"ef\": \"dýrmæts vistheimilis\"}, \"ft\": {\"nf\": \"dýrmæt
vistheimili\", \"þf\": \"dýrmæt vistheimili\", \"þgf\": \"dýrmætum
vistheimilum\", \"ef\": \"dýrmætra vistheimila\"}}"}
  ```
</details>

---
## [Maybe-Anton/Shiptest](https://github.com/Maybe-Anton/Shiptest)@[70463ae71b...](https://github.com/Maybe-Anton/Shiptest/commit/70463ae71b7d639eecea572d3251562c5ffef68b)
#### Wednesday 2023-11-15 17:02:51 by Mirag1993

Reworks The Visuals Of Independent And Nanotrasen Captains (#2453)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

Does what it says in the title. This is a demented PR that touches a lot
of things, but its main benefit is that now regular independent
captains, cowboy independent captains, and nanotrasen captains have a
unique identity.

Of those changed, it includes:

- The Nanotrasen Captain (parade)

![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/48a31cb1-b266-43cb-9b6e-525028893011)

- The Nanotrasen Captain (regular)

![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/799c88f0-b7ce-4736-956d-2e9c0a096433)

- The Independent Captain (regular/parade)

![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/17ecb3d3-5f2f-4ce0-a518-81366945ebdf)

- The Independent Captain (western)

![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/a56a798c-5adf-41d7-917a-730661f306ed)

The PR also axes a bunch of unused, or frankly quite basic lieutenant
outfits that were nothing more than set dressing with not much substance
behind them. The roles were not removed for now, and they have
appropriate outfits as a placeholder pending a full removal.

This also means that the Head of Personnel was slightly touched up,
mostly by having a coat and hat similar to the western captain's when
appropriate. The role itself is pending a full visual rework for later
that is beyond the scope of this PR.

Speaking of removals, this also means that captain outfits/roles that
were there as a legacy of removed ships, were finally axed for good.
Goodbye deserter captain for Riggs variant number 4, you will not be
missed.

This PR also touches several (a lot) of maps, mostly adding/removing
outfits that were either missing, or didn't fit with the dress code of
the vessel.

Also the PR fixes an oversight by @MarkSuckerberg by making the BYOND
version warning an actual warning, instead of an error when compiling.
Etto bleh.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

Visual cohesion is important, and dear fucking god if I see one more
independent western captain not wearing the duster because it wasn't in
the ship, I will weep, and my weeping will cause a biblical deluge.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

:cl: PositiveEntropy
imageadd: Outfits for independent and Nanotrasen captains have been
violently reworked.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [thisismy-github/pyplayer](https://github.com/thisismy-github/pyplayer)@[b9c0310eaf...](https://github.com/thisismy-github/pyplayer/commit/b9c0310eaf83326f6ec3cb94dafd8fd951a75189)
#### Wednesday 2023-11-15 17:20:30 by thisismy-github

Added prototype "Add text" edit (read description)

This is intentionally unfinished and very messy. I worked on this two
weeks ago for ~5 days before realizing a much better idea, but I wanted
the world to see my initial work (also I want to work on other things).

For a full write-up, see the "HACK:" comment added to `self._save()`.
tl;dr: I made a neat dialog for adding text to media, but translating
the realtime preview I was making with `QPainter` and `QFontMetrics`
into the parameters that FFmpeg expects while also getting alignments
to work proved very annoying.

The realization I had was that the main hack I was doing (manually
re-painting the preview onto a QPixmap and using PIL to calculate each
text block's true coordinates) would be far better suited to just saving
the QPixmap and flat out overlaying the entire thing as an image instead
of converting it into FFmpeg's `drawtext` filter.

This change would be far easier, 100% accurate (my current work is only
about 90% accurate - right-aligned text is especially broken), and allow
for far greater text-customization, rich text, and actual images.

Still though, this technically works. So I figured I'd commit it.

---
## [pktmasseta/pktmasseta.github.io](https://github.com/pktmasseta/pktmasseta.github.io)@[b0ff599e8a...](https://github.com/pktmasseta/pktmasseta.github.io/commit/b0ff599e8a5567a0a7159d388239461fb8f8df0e)
#### Wednesday 2023-11-15 17:26:03 by azhang1001

Removed David Magrefty temporarily

  - initials: DSM
    name: David Magrefty
    activities: StartMIT, Taekwondo
    major: Computer Science and Engineering (6-3)
    hometown: Ashdod, Israel
    quote: I'll take you to Israel!
    nickname: Kravmagrefty
    blurb: >
      Is it David Beckham? Is it Dave Franco? No, it's actually David Magrefty.

      Born in Ashdod, Israel, David is a true gentleman that is fluent in the languages of Hebrew, English, Python, node.JS, CSS, and love. Some see him as an army commander, we see him as a brother, and your girlfriend probably sees him as the man she wishes you could be. He's rigorously trained in the deadly martial art of Krav Maga but his stunning looks and charm are still the most lethal thing about him. When he isn't busy fielding stares from everyone in a 3-mile radius, David is usually busy finishing a pset due next semester in the MacGregor study room (either that or he's busy founding the next unicorn at MTC).

---
## [pktmasseta/pktmasseta.github.io](https://github.com/pktmasseta/pktmasseta.github.io)@[286999e18a...](https://github.com/pktmasseta/pktmasseta.github.io/commit/286999e18a6d3111c7a47e06d584b472c701cb25)
#### Wednesday 2023-11-15 17:38:53 by azhang1001

Removed Raz temporarily

- initials: RXG
    name: Raz Gaon
    activities: Mixed Martial Arts, Soccer, Snowboarding, OneWheeling, FIFA
    major: Computer Science and Engineering (6-3)
    hometown: Atlanta, GA and Hod Hasharon, Israel
    quote: Has a penchant for hamburgers
    nickname:
    blurb: >
      Whoosh! No, it is not the Flash nor a wild Cheetah, but a force far more majestic and deserving of a comic book: Brother Raz Gaon atop of his Onewheel zooming through the streets of Boston and Cambridge. Although a master of Mixed Martial Arts, black belt holder, and ex-military commander, his unfaltering discipline make his lightning-fast jab the least deadly thing about him. It is his striking good looks and charming personality that will have you, your girlfriend, your mom, and your girlfriend’s mom falling to the ground. A walking thesaurus, speaking to Raz for 5 minutes will expand your lexicon more than any CI-H would. It is impossible to have an uninteresting conversation with Raz, as is sharing a non-scrumptious meal.

---
## [0perator-github/mameui](https://github.com/0perator-github/mameui)@[65ec4542ca...](https://github.com/0perator-github/mameui/commit/65ec4542ca3c0092247ebcab86d21eff987e4472)
#### Wednesday 2023-11-15 18:20:23 by wilbertpol

msx2_flop.xml: Added 54 items (49 working) and replaced one item with a better dump. (#11698)

* Replaced VS Rotation (Japan) with a better dump. [file-hunter]
* Removed Ultima IV - Quest of the Avatar (Japan, alt disk 2) (disk 2 is from an English translation).
* Removed Vectron (Netherlands) and Vectron (Netherlands, alt) (extracted from a compilation).
* Removed Zoo (Netherlands, alt) and Zoo (Netherlands, alt 2) (hacked versions)

New working software list items (msx2_flop.xml)
-------------------------------
Konami Game Collection Bangai-hen (Japan, alt) [file-hunter]
The Legend of Shonan (Japan) [file-hunter]
Sailor-fuku Senshi Felis (Japan) [file-hunter]
Tempo Typen (Netherlands) [file-hunter]
Tenkyuhai Special - Tougen no Utage (Japan) [file-hunter]
Tenkyuhai Special - Tougen no Utage II (Japan) [file-hunter]
Thanatos (Japan) [file-hunter]
Tokimeki Sports Gal (Japan) [file-hunter]
Tominaga Koukou Tantei-bu (Japan) [file-hunter]
Trilogy Kuki Youka Shinden (Japan) [file-hunter]
The Tucs (Japan) [file-hunter]
Tulip Ichigou (Japan) [file-hunter]
Ultima II - The Revenge of the Enchantress (Japan) [file-hunter]
Undead Line (Woomb) [file-hunter]
Wizardry Scenario #3 - The Legacy of Llylgamyn (Japan) [file-hunter]
Xak - The Art of Visual Stage (Japan, Woomb) [file-hunter]
Yoshida Koumuten Data Library Vol. 2 (Japan) [file-hunter]
Yoshida Koumuten Data Library Vol. 3 (Japan) [file-hunter]
Yume Pro RPG Shaon-ban (Japan) [file-hunter]
Yumeji Asakusa-Kitan (Japan) [file-hunter]
Yuurei-kun (Japan) [file-hunter]
Zoo (Europe) [file-hunter]
GAME100 (Japan) [file-hunter]
Go! Volcano [NAGI-P SOFT]
Las Aventuras de Rudolphine Rur (Spanish) [Dwalin]
MSX Light [MSXdev]
Siege [NAGI-P SOFT]
Teddy's in Action Part 2 [file-hunter]
Terrahawks [file-hunter]
Tetravex (Netherlands) [file-hunter]
Tetris Master (Japan) [file-hunter]
Tetris Master - Operation Maison Ikkoku (Japan) [file-hunter]
Tetris Master - Operation Orange Road (Japan) [file-hunter]
Tetris Master - Operation Ranma 1/2 (Japan) [file-hunter]
Tetris Master - Series 1 Ranma 1/2 (Japan) [file-hunter]
Thunderbirds are Go (Netherlands, promo) [file-hunter]
Thunderbirds to the Rescue (Netherlands, promo) [file-hunter]
Tile Golf [NAGI-P SOFT]
Triplex (Netherlands) [file-hunter]
Trivial Pursuit (Netherlands) [file-hunter]
Trivial Pursuit - Aanvulling Jaareditie 1995 (Netherlands) [file-hunter]
Tunez: Garfield Edition [file-hunter]
The UHF Painter (Italy) [file-hunter]
War World FM-PAC Demo (Netherlands) [file-hunter]
Wiz Kids (Japan) [file-hunter]
Yupipati (demo) [file-hunter]
Zombie Night [Alberto Sgaggero]
Zoo Rally (Russia) [file-hunter]
Zoto (Germany?) [file-hunter]

New NOT_WORKING software list additions (msx2_flop.xml)
------------------------------------------
HBI-V1 Video Digitizer (Japan) [file-hunter]
Himitsu no Hanazono (Japan) [file-hunter]
Veldslag (Netherlands) [file-hunter]
Zeeslag (Netherlands) [file-hunter]
Zeeslag (Netherlands, demo) [file-hunter]

---
## [GPeckman/tgstation](https://github.com/GPeckman/tgstation)@[d31c21ff1b...](https://github.com/GPeckman/tgstation/commit/d31c21ff1b57ba7003f9bbdcf51171d3215a0774)
#### Wednesday 2023-11-15 18:26:15 by jimmyl

new space ruin, the biological research outpost (#79149)

## About The Pull Request

![2023-10-21 18 02
39](https://github.com/tgstation/tgstation/assets/70376633/5829e939-3b04-465f-a186-095ceb360bba)

adds this ruin to space ruin pool
this is a shady (as NT always is) bioresearch outpost that got fucked up
by an experiment
this has like some puzzle aspect to it since you gotta find keycards and
shit and press buttons to unlock shield gates
this ends with you fighting a heart which if you defeat, destroys the
blockade that prevents you from entering the outpost vault

also you can no longer literally just cut indestructible grilles or
unanchor indestructible windows

### new puzzle elements or something idk
variant of pressure plate that you cannot remove and it sends a puzzle
signal
cooler red puzzle doors that look very foreboding or something idk
theyre for this ruin
also puzzle blockades, which are indestructible dense objects that are
destroyed if they receive a puzzle signal
and also buttons and keycard pads for puzzles


https://github.com/tgstation/tgstation/assets/70376633/c98807ec-1e7b-49c4-a757-cdbb76a1b566



https://github.com/tgstation/tgstation/assets/70376633/9d5d9dd1-5868-44e6-a978-5ea57b30c298

stuff that throws electric shocks in a pattern, ignores insuls and only
knocks down, and no you cannot just run past


https://github.com/tgstation/tgstation/assets/70376633/5772917c-a963-48a4-a743-b0f610801d25

### enemies
living floor, it can only attack stuff on top of it and it attacks until
the victim is dead
it is invincible to all but a crowbar, and it cannot move, and it
remains hidden until a victim is in range


https://github.com/tgstation/tgstation/assets/70376633/aa1d54f6-b259-4e58-9d44-e393d2131acf

living flesh, it can replace your limbs with itself
the conditions for that are; the limb must have 20 or more brute, victim
must be alive and dismemberable, the limb may not be torso or head, or
the limb may not be living flesh
alternatively it can replace a missing limb
these are all checked with every attack
they have 20 hp
the limbs in question will sometimes act up, while passively draining
nutrition, arms will randomly start pulling nearby stuff, legs may step
randomly
limbs when detached, turn into mobs and reactivate AI 2 seconds later.
if the host is shocked, all living flesh limbs will detach, or if the
host dies they will also do that


https://github.com/tgstation/tgstation/assets/70376633/765cc99e-c800-4efb-aabe-d68817bbd7ae



## Why It's Good For The Game

ruin variety is cool i think
also the other things i added should be useful for other mappers for
bitrunning or whatever

also bug bad for that one fix
## Changelog
:cl:
add: living floor, living flesh, and other stuff for the bioresearch
outpost ruin
add: bioresearch outpost ruin
fix: you may not defeat indestructible grilles and windows with mere
tools
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [nikhilmishra1710/Fintech-hackathon](https://github.com/nikhilmishra1710/Fintech-hackathon)@[a62197132d...](https://github.com/nikhilmishra1710/Fintech-hackathon/commit/a62197132dee7fec039f703fc3bbacbe3a6db0cc)
#### Wednesday 2023-11-15 18:49:10 by LEVIII007

Update family_confirmation_successful_transfer_screen.dart

fuck you bitch

---
## [Olek97/zechub](https://github.com/Olek97/zechub)@[0d97121c8c...](https://github.com/Olek97/zechub/commit/0d97121c8ca6106c2c829f5b8f47679d1801a3f1)
#### Wednesday 2023-11-15 20:19:32 by TonyAkinsWritesCrypto

ZecWeekly66

# ZecWeekly (Episode 66)


The Zebra book, Zcash enhanced privacy, ZecHub Extras, Zcash 7th Anniversary , Ywallet Upgrade. 


Curated by "TonyAkins"[TonyAkin01](https://twitter.com/TonyAkins01))

---

#### Welcome to ZecWeekly Episode 66


Welcome to the thrilling episode of ZecWeekly, as we explore Zcash's implementation of FROST using Schnorr , Zcash 7th Anniversary celebrated with lots of merches and prizes, release of Zebra updated 1.3.0, and the introduction of UniFFi for Developer's use cases. 

–
### This Week Education's Pieces.

This week's education pieces will educate and refine us with all details about Zcash addresses, both shielded and transparent addresses and other the latest development in the Zcash payment system. 

Click  the link below to access the resource :

https://wiki.zechub.xyz/visualizing-zcash-addresses




### Zcash Updates

Zcash and ECC updates. 

[NowNodes features Zcash for upgraded Privacy ecosystem](https://twitter.com/NOWNodes/status/1716463761777680713)

[Ywallet Zcash Ledger app on Nano S Plus w/ Orchard tx](https://www.youtube.com/watch?v=HRVNpDDoh1Y&t=34s) 

[Zcash Digitals Decentralized](https://twitter.com/ElectricCoinCo/status/1717570088771952811)

[tECC DAYS 2023 celebrated](https://twitter.com/ECCIntegrator/status/1718035043736547504)


[Announcing Zebra 1.3.0](https://twitter.com/ZcashFoundation/status/1716524342853476576)

[Implementation of UniFFi on Zcash Network](https://twitter.com/eiger_co/status/1716801431510851824)

[Zcash SDK fixes now live](https://twitter.com/EdgeWallet/status/1716530980499128578)

#### Zcash Community Grants Updates

[WalletD Community Grant Application](https://forum.zcashcommunity.com/t/walletd-community-grant-application/45876?utm_source=dlvr.it&utm_medium=twitter)

[Security assessment for Zcash FROST published](https://twitter.com/ZecHub/status/1716930299140169764)

[Zcash Community funded @eiger_co to create UniFFi library](https://twitter.com/ZcashCommGrants/status/1717273970922123392)

#### Community Projects

[Zcash 7th Anniversary celebrated in grande style](https://free2z.cash/ZecHub/zpage/zcash-7th-anniversary-challenge)

[Post Comments on Free2Z using Zenith CLI! Go check it out!](https://www.youtube.com/watch?v=HtorP8TJ5vk)

#### News & Media

[Binance founder CZ’s fortune gets slashed $12B, while SBF is still at $0](https://cointelegraph.com/news/binance-ceo-changpeng-zhao-fortune-slashed-billionaires-index)

[Google to invest another $2B in AI firm Anthropic: Report](https://cointelegraph.com/news/google-to-invest-another-two-billion-in-ai-firm-anthropic)

[Kraken to suspend trading for USDT, DAI, WBTC, WETH, and WAXL in Canada](https://cointelegraph.com/news/kraken-suspend-trading-usdt-dai-wbtc-weth-and-waxl-stablecoin-canada)

[AI Girlfriend Amouranth Wants to Use Her 'Vaginal Yeast' to Brew Beer](https://decrypt.co/203517)

[Audits and rug-pulled projects, a $650B token burn, and major DeFi protocol quits UK: Finance Redefined](https://cointelegraph.com/news/audits-and-rug-pulled-projects-a-650b-token-burn-and-major-defi-protocol-quits-uk-finance-redefined)

[Bitcoin's 14% Weekly Gain Signals 'End of an Era' as Big Tech Dumps, Analyst Says](https://www.coindesk.com/markets/2023/10/27/bitcoins-14-weekly-gain-signals-end-of-an-era-as-big-tech-dumps-analyst-says/?utm_medium=referral&utm_source=rss&utm_campaign=headlines)

[Binance Founder CZ's Wealth Falls About $12B as Trading Revenue Slumps: Bloomberg](https://www.coindesk.com/business/2023/10/27/binance-founder-czs-wealth-falls-about-12b-as-trading-revenue-slumps-bloomberg/?utm_medium=referral&utm_source=rss&utm_campaign=headlines)

[How major German firms like Mercedes and Lufthansa are using NFTs](https://cointelegraph.com/news/germany-mercedes-lufthansa-nfts)

[ChatGPT creator OpenAI builds new team to check AI risks](https://cointelegraph.com/news/chatgpt-openai-new-team-ai-risks)

[Bitcoin restarting 2023 uptrend after 26% Uptober BTC price gains — research](https://cointelegraph.com/news/bitcoin-2023-uptober-btc-price-research)



## Some Zcash Tweets


[Central bank of Brazil account heard about Zcash today](https://x.com/anarchychains/status/1717288641288921272)

[Happy Birthday Zcash!!!](https://twitter.com/ZforZcash/status/1718085318543376404)

[ZcashFoundation and NCCGroupInfosec conduct a security assessment of the Foundation’s FROST](https://twitter.com/ZcashFoundation/status/1716849796315512935)

[What are Zero-knowledge Proofs](https://twitter.com/NighthawkWallet/status/1717730883933806958)

[Zcash Community Grant minutes](https://twitter.com/ZcashCommGrants/status/1717556482344907090)

[Keep yourself safe from hack with a Zcash wallet](https://twitter.com/NighthawkWallet/status/1717007699592851702)

[Metrics should be updated](https://twitter.com/ZcashForum/status/1716786643171225726)

[Join our UPA friends if you're at EFDevconnect](https://twitter.com/ElectricCoinCo/status/1716886693444530195)


[Social media Data collection, does it matter?](https://twitter.com/ZecHub/status/1716850588942577890)

[Follow NighthawkWallet for crypto privacy education](https://twitter.com/NighthawkWallet/status/1716625185623728248)

[Privacy is normal!](https://twitter.com/ZcashNigeria/status/1716755151497707660)


## Zeme of the Week

[https://twitter.com/ZcashNigeria/status/1718151545324200002](https://twitter.com/ZcashNigeria/status/1718151545324200002)

[https://twitter.com/zcashbrazil/status/1717609507432337754](https://twitter.com/zcashbrazil/status/1717609507432337754)

[https://twitter.com/zcashbrazil/status/1717225798019567621](https://twitter.com/zcashbrazil/status/1717225798019567621)



## Jobs in the Ecosystem

[Zcash needs graphic designers,writers, and privacy advocate in its ecosystem](https://twitter.com/ZecHub/status/1713947885220344234)

[Create Video HOWTO - Setup WSL in windows, and compile lastest zcashd](https://github.com/ZecHub/zechub/issues/567)

---
## [magnetophon/nixpkgs](https://github.com/magnetophon/nixpkgs)@[b6c06e216b...](https://github.com/magnetophon/nixpkgs/commit/b6c06e216bb3bface40eb8ea6576b25f9b2971dd)
#### Wednesday 2023-11-15 20:39:09 by Charles Strahan

ruby: new bundler infrastructure

This improves our Bundler integration (i.e. `bundlerEnv`).

Before describing the implementation differences, I'd like to point a
breaking change: buildRubyGem now expects `gemName` and `version` as
arguments, rather than a `name` attribute in the form of
"<gem-name>-<version>".

Now for the differences in implementation.

The previous implementation installed all gems at once in a single
derivation. This was made possible by using a set of monkey-patches to
prevent Bundler from downloading gems impurely, and to help Bundler
find and activate all required gems prior to installation. This had
several downsides:

* The patches were really hard to understand, and required subtle
  interaction with the rest of the build environment.
* A single install failure would cause the entire derivation to fail.

The new implementation takes a different approach: we install gems into
separate derivations, and then present Bundler with a symlink forest
thereof. This has a couple benefits over the existing approach:

* Fewer patches are required, with less interplay with the rest of the
  build environment.
* Changes to one gem no longer cause a rebuild of the entire dependency
  graph.
* Builds take 20% less time (using gitlab as a reference).

It's unfortunate that we still have to muck with Bundler's internals,
though it's unavoidable with the way that Bundler is currently designed.
There are a number improvements that could be made in Bundler that would
simplify our packaging story:

* Bundler requires all installed gems reside within the same prefix
  (GEM_HOME), unlike RubyGems which allows for multiple prefixes to
  be specified through GEM_PATH. It would be ideal if Bundler allowed
  for packages to be installed and sourced from multiple prefixes.
* Bundler installs git sources very differently from how RubyGems
  installs gem packages, and, unlike RubyGems, it doesn't provide a
  public interface (CLI or programmatic) to guide the installation of a
  single gem. We are presented with the options of either
  reimplementing a considerable portion Bundler, or patch and use parts
  of its internals; I choose the latter. Ideally, there would be a way
  to install gems from git sources in a manner similar to how we drive
  `gem` to install gem packages.
* When a bundled program is executed (via `bundle exec` or a
  binstub that does `require 'bundler/setup'`), the setup process reads
  the Gemfile.lock, activates the dependencies, re-serializes the lock
  file it read earlier, and then attempts to overwrite the Gemfile.lock
  if the contents aren't bit-identical. I think the reasoning is that
  by merely running an application with a newer version of Bundler, you'll
  automatically keep the Gemfile.lock up-to-date with any changes in the
  format. Unfortunately, that doesn't play well with any form of
  packaging, because bundler will immediately cause the application to
  abort when it attempts to write to the read-only Gemfile.lock in the
  store. We work around this by normalizing the Gemfile.lock with the
  version of Bundler that we'll use at runtime before we copy it into
  the store. This feels fragile, but it's the best we can do without
  changes upstream, or resorting to more delicate hacks.

With all of the challenges in using Bundler, one might wonder why we
can't just cut Bundler out of the picture and use RubyGems. After all,
Nix provides most of the isolation that Bundler is used for anyway.

The problem, however, is that almost every Rails application calls
`Bundler::require` at startup (by way of the default project templates).
Because bundler will then, by default, `require` each gem listed in the
Gemfile, Rails applications are almost always written such that none of
the source files explicitly require their dependencies. That leaves us
with two options: support and use Bundler, or maintain massive patches
for every Rails application that we package.

Closes #8612

---
## [magnetophon/nixpkgs](https://github.com/magnetophon/nixpkgs)@[407db7b019...](https://github.com/magnetophon/nixpkgs/commit/407db7b0196417296677f2a4ef929bb092ec382b)
#### Wednesday 2023-11-15 20:44:27 by Jan Tojnar

gtk_doc: replace catalog lookup hack

In the previous commit, we added a setup hook to docbook dtd and xsl
packages, that adds derivation’s catalog file to an environment variable.
That should, in theory, remove the need for declaring their catalogs manually.
Unfortunately, xmlcatalog utility expects exactly one catalog file, completely
disregarding the environment variable in non-interactive context. In the same
spirit, the design of gtk-doc m4 files only admits a single catalog file,
resulting in another ugly hack.

---
## [magnetophon/nixpkgs](https://github.com/magnetophon/nixpkgs)@[b3d5ca8359...](https://github.com/magnetophon/nixpkgs/commit/b3d5ca8359d3fac0f21ccece79c202557a9433b5)
#### Wednesday 2023-11-15 20:47:30 by aszlig

nixos/dhparams: Set default bit size to 2048

@Ekleog writes in https://github.com/NixOS/nixpkgs/pull/39526:

> I think a default of 4096 is maybe too much? See certbot/certbot#4973;
> Let's Encrypt supposedly know what they are doing and use a
> pre-generated 2048-bit DH params (and using the same DH params as
> others is quite bad, even compared to lower bit size, if I correctly
> remember the attacks available -- because it increases by as much the
> value of breaking the group).

> Basically I don't have anything personal against 4096, but fear it may
> re-start the arms race: people like having "more security" than their
> distributions, and having NixOS already having more security than is
> actually useful (I personally don't know whether a real-size quantum
> computer will come before or after our being able to break 2048-bit
> keys, let alone 3072-bit ones -- see wikipedia for some numbers).

> So basically, I'd have set it to 3072 in order to both decrease build
> time and avoid having people setting it to 8192 and complaining about
> how slow things are, but that's just my opinion. :)

While he suggests is 3072 I'm using 2048 now, because it's the default
of "openssl dhparam". If users want to have a higher value, they can
still change it.

Signed-off-by: aszlig <aszlig@nix.build>

---
## [metabase/metabase](https://github.com/metabase/metabase)@[e98d2619db...](https://github.com/metabase/metabase/commit/e98d2619db1bae175fa3c6489c1d6be6715dfef7)
#### Wednesday 2023-11-15 20:48:48 by John Swanson

Try using `memoize-for-application-db`

I'm not entirely sure, but I think *possibly* the issue was that tests used a different application-db than the
development environment, which caused memoization to fail.

I'd like to look into this more to confirm. Frustratingly, I was able to run `(do (dev) (start!))` and get a failure
earlier, but now I can't reproduce :facepalm:. I wonder if possibly there is some interaction I didn't think about -
e.g. did I run a test before running the above, causing the function to get called with a different app-db, causing
the (wrong) result to get stored?

---
## [magnetophon/nixpkgs](https://github.com/magnetophon/nixpkgs)@[62e34d1c87...](https://github.com/magnetophon/nixpkgs/commit/62e34d1c87ee8436bfa8ceaeac07ea3855fabd43)
#### Wednesday 2023-11-15 20:56:50 by Emily

nixos/acme: change default keyType to ec256

Previously, the NixOS ACME module defaulted to using P-384 for
TLS certificates. I believe that this is a mistake, and that we
should use P-256 instead, despite it being theoretically
cryptographically weaker.

The security margin of a 256-bit elliptic curve cipher is substantial;
beyond a certain level, more bits in the key serve more to slow things
down than add meaningful protection. It's much more likely that ECDSA
will be broken entirely, or some fatal flaw will be found in the NIST
curves that makes them all insecure, than that the security margin
will be reduced enough to put P-256 at risk but not P-384. It's also
inconsistent to target a curve with a 192-bit security margin when our
recommended nginx TLS configuration allows 128-bit AES. [This Stack
Exchange answer][pornin] by cryptographer Thomas Pornin conveys the
general attitude among experts:

> Use P-256 to minimize trouble. If you feel that your manhood is
> threatened by using a 256-bit curve where a 384-bit curve is
> available, then use P-384: it will increases your computational and
> network costs (a factor of about 3 for CPU, a few extra dozen bytes
> on the network) but this is likely to be negligible in practice (in a
> SSL-powered Web server, the heavy cost is in "Web", not "SSL").

[pornin]: https://security.stackexchange.com/a/78624

While the NIST curves have many flaws (see [SafeCurves][safecurves]),
P-256 and P-384 are no different in this respect; SafeCurves gives
them the same rating. The only NIST curve Bernstein [thinks better of,
P-521][bernstein] (see "Other standard primes"), isn't usable for Web
PKI (it's [not supported by BoringSSL by default][boringssl] and hence
[doesn't work in Chromium/Chrome][chromium], and Let's Encrypt [don't
support it either][letsencrypt]).

[safecurves]: https://safecurves.cr.yp.to/
[bernstein]: https://blog.cr.yp.to/20140323-ecdsa.html
[boringssl]: https://boringssl.googlesource.com/boringssl/+/e9fc3e547e557492316932b62881c3386973ceb2
[chromium]: https://bugs.chromium.org/p/chromium/issues/detail?id=478225
[letsencrypt]: https://letsencrypt.org/docs/integration-guide/#supported-key-algorithms

So there's no real benefit to using P-384; what's the cost? In the
Stack Exchange answer I linked, Pornin estimates a factor of 3×
CPU usage, which wouldn't be so bad; unfortunately, this is wildly
optimistic in practice, as P-256 is much more common and therefore
much better optimized. [This GitHub comment][openssl] measures the
performance differential for raw Diffie-Hellman operations with OpenSSL
1.1.1 at a whopping 14× (even P-521 fares better!); [Caddy disables
P-384 by default][caddy] due to Go's [lack of accelerated assembly
implementations][crypto/elliptic] for it, and the difference there seems
even more extreme: [this golang-nuts post][golang-nuts] measures the key
generation performance differential at 275×. It's unlikely to be the
bottleneck for anyone, but I still feel kind of bad for anyone having
lego generate hundreds of certificates and sign challenges with them
with performance like that...

[openssl]: https://github.com/mozilla/server-side-tls/issues/190#issuecomment-421831599
[caddy]: https://github.com/caddyserver/caddy/blob/2cab475ba516fa725d012f53ca417c3e039607de/modules/caddytls/values.go#L113-L124
[crypto/elliptic]: https://github.com/golang/go/tree/2910c5b4a01a573ebc97744890a07c1a3122c67a/src/crypto/elliptic
[golang-nuts]: https://groups.google.com/forum/#!topic/golang-nuts/nlnJkBMMyzk

In conclusion, there's no real reason to use P-384 in general: if you
don't care about Web PKI compatibility and want to use a nicer curve,
then Ed25519 or P-521 are better options; if you're a NIST-fearing
paranoiac, you should use good old RSA; but if you're a normal person
running a web server, then you're best served by just using P-256. Right
now, NixOS makes an arbitrary decision between two equally-mediocre
curves that just so happens to slow down ECDH key agreement for every
TLS connection by over an order of magnitude; this commit fixes that.

Unfortunately, it seems like existing P-384 certificates won't get
migrated automatically on renewal without manual intervention, but
that's a more general problem with the existing ACME module (see #81634;
I know @yegortimoshenko is working on this). To migrate your
certificates manually, run:

    $ sudo find /var/lib/acme/.lego/certificates -type f -delete
    $ sudo find /var/lib/acme -name '*.pem' -delete
    $ sudo systemctl restart 'acme-*.service' nginx.service

(No warranty. If it breaks, you get to keep both pieces. But it worked
for me.)

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[7fce8cd805...](https://github.com/tgstation/tgstation/commit/7fce8cd8054cc1d0b048db12d7e9587b42fcdef2)
#### Wednesday 2023-11-15 20:58:12 by san7890

Codifies male goats not having an udder (#79722)

## About The Pull Request

This was addressed in #78759 (1b1fde4908826ef5c54ffc0734e74028270af3fd)
and reviewed (and merged even though I didn't respond to it, oh well),
but I half-assed it because the whole point was to prevent male goats
from having an udder, but I only added it to the subtype of Pete i made
in that PR. Let's expand that to all male goats now.
## Why It's Good For The Game

It doesn't make biological nor morphological sense as to why a male goat
can provide milk. Ideally this should be like this for all animals
(because that's real life) but that's a later issue with further balance
implication.

I think it's still an interesting idea that Nanotrasen will just send
you any old goat despite it being "useless" beyond being very good at
eating plants. Maybe cargo should have a way to guarantee getting a
female goat in the future? It's just like real life where zoos and farms
have to constantly dealw ith female animals (such as giraffes or other
exotic stuff) tending to be far rarer/cost far more than their male
variants due to the potential to generate offspring (there's more nuance
to husbandry than this but just play along)... and in space, every
animal is "exotic".

It still remains possible to biogenerate milk, which tends to be far
faster than feeding/milking goats- which is something that the cook
should have access to anyways.
## Changelog
:cl:
balance: Male Goats should no longer spawn with an udder, instead of it
just being Pete.
/:cl:

---------

Co-authored-by: Ghom <42542238+Ghommie@users.noreply.github.com>

---
## [DerGorn/RustyTree](https://github.com/DerGorn/RustyTree)@[84f09a9ecc...](https://github.com/DerGorn/RustyTree/commit/84f09a9ecc450e8cfb9281c6f99a3fe12ec057dc)
#### Wednesday 2023-11-15 21:09:45 by DerGorn

close to finished rotating a rectangle only the fucking left side does stupid shit

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[764a304079...](https://github.com/treckstar/yolo-octo-hipster/commit/764a3040790d349f5f2d4e18206528399e828d5d)
#### Wednesday 2023-11-15 21:22:04 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [magnetophon/nixpkgs](https://github.com/magnetophon/nixpkgs)@[7553d0fe29...](https://github.com/magnetophon/nixpkgs/commit/7553d0fe29801938bcb280bb324b579ef9016aea)
#### Wednesday 2023-11-15 21:25:58 by Adam Joseph

stdenv: Nix-driven bootstrap of gcc

 #### Summary

By default, when you type `make`, GCC will compile itself three
times.  This PR inhibits that behavior by configuring GCC with
`--disable-bootstrap`, and reimplements the triple-rebuild using
Nix rather than `make`/`sh`.

 #### Immediate Benefits

- Allow `gcc11` and `gcc12` on `aarch64` (without needing new
  `bootstrapFiles`)
- Faster stdenv rebuilds: the third compilation of gcc
  (i.e. stageCompare) is no longer a `drvInput` of the final stdenv.
  This allows Nix to build stageCompare in parallel with the rest of
  nixpkgs instead of in series.
- No more copying `libgcc_s` out of the bootstrap-files or other
  derivations
- No more Frankenstein compiler: the final gcc and the libraries it
  links against (mpfr, mpc, isl, glibc) are all built by the same
  compiler (xgcc) instead of a mixture of the bootstrapFiles'
  compiler and xgcc.
- No more [static lib{mpfr,mpc,gmp,isl}.a hack]
- Many other small `stdenv` hacks eliminated
- `gcc` and `clang` share the same codepath for more of `cc-wrapper`.

 #### Future Benefits

- This should allow using a [foreign] `bootstrap-files` so long as
  `hostPlatform.canExecute bootstrapFiles`.
- This should allow each of the libraries that ship with `gcc`
  (lib{backtrace, atomic, cc1, decnumber, ffi, gomp, iberty,
  offloadatomic, quadmath, sanitizer, ssp, stdc++-v3, vtv}) to be
  built in separate (one-liner) derivations which `inherit src;`
  from `gcc`, much like https://github.com/NixOS/nixpkgs/pull/132343

 #### Incorporates

- https://github.com/NixOS/nixpkgs/pull/210004
- https://github.com/NixOS/nixpkgs/pull/36948 (unreverted)
- https://github.com/NixOS/nixpkgs/pull/210325
- https://github.com/NixOS/nixpkgs/pull/210118
- https://github.com/NixOS/nixpkgs/pull/210132
- https://github.com/NixOS/nixpkgs/pull/210109
- https://github.com/NixOS/nixpkgs/pull/213909
- https://github.com/NixOS/nixpkgs/pull/216136
- https://github.com/NixOS/nixpkgs/pull/216237
- https://github.com/NixOS/nixpkgs/pull/210019
- https://github.com/NixOS/nixpkgs/pull/216232
- https://github.com/NixOS/nixpkgs/pull/216016
- https://github.com/NixOS/nixpkgs/pull/217977
- https://github.com/NixOS/nixpkgs/pull/217995

 #### Closes

- Closes #108305
- Closes #108111
- Closes #201254
- Closes #208412

 #### Credits

This project was made possible by three important insights, none of
which were mine:

1. @ericson2314 was the first to advocate for this change, and
   probably the first to appreciate its advantages.  Nix-driven
   (external) bootstrap is "cross by default".

2. @trofi has figured out a lot about how to get gcc to not mix up
   the copy of `libstdc++` that it depends on with the copy that it
   builds, by moving the `bootstrapFiles`' `libstdc++` into a
   [versioned directory].  This allows a Nix-driven bootstrap of gcc
   without the final gcc would still having references to the
   `bootstrapFiles`.

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
[static lib{mpfr,mpc,gmp,isl}.a hack]: https://github.com/NixOS/nixpkgs/blob/2f1948af9c984ebb82dfd618e67dc949755823e2/pkgs/stdenv/linux/default.nix#L380

---
## [ioccc-src/temp-test-ioccc](https://github.com/ioccc-src/temp-test-ioccc)@[1daa978ce5...](https://github.com/ioccc-src/temp-test-ioccc/commit/1daa978ce5be601f5b98df0e29bf2698f2fbce95)
#### Wednesday 2023-11-15 21:55:11 by Cody Boone Ferguson

Fix typos (from paste) in 1996/huffman/try.sh

It should be more like:

   Well the wolf-man fell dead
   As you can plainly see
   And that's the end the story for you and me
   You still give a listen, you just may
   Hear a big wolf-man or little piggy say
   Little pig, little pig, let me in
   Not by the hair of my chinny, chin, chin
   Little pig, little pig, let me in
   Not by the hair of my chinny, chin, chin
   Well I'm huffin', I'm puffin'
   I'll blow your house in
   Huffin', puffin', blow your house in
   Huffin', puffin', blow your house in
   Huffin', puffin', blow your house in
   Huffin' and a puffin' and
   I'll blow your house in!
   Huffin' and a puffin' and
   I'll blow your house in!
   Huffin' and a puffin' and
   I'll blow your house in!
   Huffin' and a puffin' and
   I'll blow your house in!

   And the moral of the story is, that
   bands with no talent can easily amuse
   Idiots with a stupid puppet show.

... or something like that :-)

---
## [MemedHams/tgstation](https://github.com/MemedHams/tgstation)@[b0ec1e4098...](https://github.com/MemedHams/tgstation/commit/b0ec1e4098ed80fdb0bac69c6f950bd5e38012b8)
#### Wednesday 2023-11-15 22:22:58 by Jacquerel

[no gbp] Adds missing chat feedback to watcher abilities (#77700)

## About The Pull Request

I kept meaning to add this in my last PR and kept thinking "I'll add
that in with these review changes" and then forgot every time. This
should make it clearer what is happening to you and why.

Also I made the gaze ability stun the user for a short period after it
goes off because them shooting you instantly after they stop channeling
_is_ sort of bullshit.
Also while testing this I noticed the AI interrupt one of its actions to
do the other one which is a bit silly so now it cannot do that.

## Why It's Good For The Game

Outlines in the log why something bad just happened to you.

## Changelog

:cl:
qol: Added some textual feedback to new watcher abilities
balance: Watchers will not attack for a short period following their
gaze attack
fix: Watchers won't interrupt one ability to use the other one
/:cl:

---
## [ihatethisengine/cmss13](https://github.com/ihatethisengine/cmss13)@[1e890af39d...](https://github.com/ihatethisengine/cmss13/commit/1e890af39d7c4b6233439fbaa8693a3918e35f5c)
#### Wednesday 2023-11-15 22:33:43 by Steelpoint

Revolver Heavy Ammo Effect Change (#4706)

# About the pull request

This PR changes heavy ammo for the Revolver to knockback a mob and slow
them down instead of stunning it.

# Explain why it's good for the game

Combat balance is a precarious and often difficult conversation to hold,
ergo I'll lay my biases out on the table at first. I'm a marine main at
heart, but I have played a lot of xeno recently to gain a better
understanding of their side of the story, enough that I feel confident
to make these assertions.

My belief is that the heavy ammo of the revolver is a negative concept
for the game, and it needs to be removed, due to its stun factor.

The issue here is readability and prediction. When you see a RPG, you
know that it can fire a devastating warhead that can stun and kill T3s.
When you see a Warrior, you know it can leap to 4 tiles to stun and drag
a Human, when you hear a CAS strike you know exactly what is about to
drop. When you see a Queen you know she can stun screech and neuro stun
you.

But the issue with the Revolver is it has no obvious tell. It is a small
item, that can be fit inside backpacks, holsters, pouches, belts, armour
slots. It has no obvious advance warning when you are going to fire it.
There is no special uniform requirement making a revolver user standout
amongst the crowd. There is no tell.

The problem with the stun revolver is simply that is is a hard counter
to all T1s and most T2s. Its ability to stun allows it to perform an
attack that is uncounterable to a xeno as a xeno has no way to predict
who may be carrying one. A xeno can tell who a Specialist is, a xeno can
tell who has a shotgun or flamer or sniper or RPG, you can tell when a
mortar is being prepared, or a CAS strike or even an OB. You can see the
smartgunner. Even the Scout, a literal cloaked Marine, has to uncloak to
fire. You can not tell who has a revolver until they pull it out and
stun you. Once you are stunned you die.

A xeno equilivant would be if any Xeno could be carrying a special tool
that lets them grab a marine from 7 tiles away and pull them in plus
stun them for 2 seconds. But any xenomorph could be using it, including
a Lesser Drone.

Perhaps the heavy revolver could be reworked to do something else, but
ultimately the only reason anyone takes this ammo is for the stun.
Anything else is beating around the bush.

Those are my reasoning's, I'll leave the rest to the powers' that be. 

# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl:
balance: Revolver Heavy ammo no longer stuns targets it strikes, it will
instead knock them back and slow them down for a short time.
/:cl:

---------

Co-authored-by: Steelpoint <alexander.henley@hotmai.com>

---
## [cparadis777/GithubGameOff2023](https://github.com/cparadis777/GithubGameOff2023)@[382b40c4d5...](https://github.com/cparadis777/GithubGameOff2023/commit/382b40c4d51e086ce24ee030025672f7e98ab00b)
#### Wednesday 2023-11-15 22:49:48 by plexsoup

fucking with other peoples shit (sorry)

feel free to overwrite with your version if there's a conflict.

---
## [davep/tinboard](https://github.com/davep/tinboard)@[daf5e82cb0...](https://github.com/davep/tinboard/commit/daf5e82cb0aafecf1c12368b0528c41851ba7e43)
#### Wednesday 2023-11-15 23:03:29 by Dave Pearson

:construction: Revamping the Details pane

Mostly there with how I want it to look, but I need to spend a bit of time
thinking about how I'm going to do the tags. Using links in Markdown is
great and all, but it's a bit keyboard-hostile. I want to be
keyboard-friendly too.

So this is a WiP commit at the end of the evening, and the next time I'm in
here I'll have a proper think about how I'm going to do this.

See also https://github.com/Textualize/textual/issues/3687 as a related
issue that I've discovered while making these changes (it explains why the
scrollbar in the details pane isn't showing at the moment, if it's needed).

---
## [1393F/tgstation](https://github.com/1393F/tgstation)@[0f5d14e68b...](https://github.com/1393F/tgstation/commit/0f5d14e68b19111592301efe52a03de80aced61e)
#### Wednesday 2023-11-15 23:30:45 by Ben10Omintrix

Mook village and basic mook refactor (#78789)

## About The Pull Request
refactors mooks into basic mooks and re-adds them to the game

## Why It's Good For The Game
this refactors mooks into basic mobs and re adds them to the game. mooks
are now a part of lavaland. they come as a part of a random ruin which
consist of a entire village of friendly mooks. Mooks will aid players
but they will still attack ashwalkers because of some troubled history
between them.

![mookvillage](https://github.com/tgstation/tgstation/assets/138636438/ad1c5d63-c168-475a-a85d-b727dff43e7b)

mooks are a very diseased specie. nanotrasen discovered a small tribe of
mooks and cut a deal with their tribal chief to aid ss13 miners in
exchange for medical supplies.

tribal chief in his decked out home

![tribalchief](https://github.com/tgstation/tgstation/assets/138636438/cc0e0a11-9bf0-4322-b3ae-c7be43092ee8)

male mooks go out and mine and haul ore off back to their village. they
will deposit ores into a stand which is managed by another mook. they
will all return to their village to rest once a lavastorm comes.

![mookstand](https://github.com/tgstation/tgstation/assets/138636438/c7adbf4e-6322-4347-acfc-4e8d45aff798)

players can use this stand to withdraw any ore they like

![mookui](https://github.com/tgstation/tgstation/assets/138636438/a1318be8-50f7-49b2-827c-97bafdb2488a)

female mooks will stay behind in the village to guard it from
ashwalkers. they will also heal male mooks when they come back from a
long day of work. the tribal chief is a bum and chooses not to go out
and mine. he will stay behind in the village and issue commands to his
people rather than work

the village also has its own bard! he follows player visitors and plays
nice music for them while they are in the village (although he is not
very talented).

![mookbard](https://github.com/tgstation/tgstation/assets/138636438/5123e492-6657-4755-9dc7-ab94d4beb554)

he is still a warrior at heart tho so he will be smashing his guitar
over ashwalker skull

![mookshmash](https://github.com/tgstation/tgstation/assets/138636438/bf211bf0-e963-4dbb-b004-e653e06e3974)




## Changelog
:cl:
refactor: mooks are now basic mobs. please report any bugs
feature: added mook village to lavaland ruins!
/:cl:

---
## [FRC3636/bunnybots-2023](https://github.com/FRC3636/bunnybots-2023)@[3f9b610179...](https://github.com/FRC3636/bunnybots-2023/commit/3f9b6101791ba1ce6dd97eec1fdd07ce8590eef4)
#### Wednesday 2023-11-15 23:45:02 by Crafterzman

fix(swerve): working drivetrain (#7)

* i let megan cook

* feat(tracking): solve for optimal time offset

feat(tracking): refactor prior commit

* feat(tracking): add lead targeting

feat(tracking): solve for optimal time offset

feat(tracking): refactor prior commit

feat(tracking): add lead targeting

* feat(tracking): switch to multivariate regression, use NT timestamping

* refactor(tracking): change names :)

* refactor(CAN): change id's

asa says hi

* ok we're gonna try to fuck up this shit again baruch atah adonai frfr

* fix: change pid coefficients

* fix(vision): uncomment TargetVision subsystem

---------

Co-authored-by: rotating.cow <ben.arkonovich@gmail.com>

---
## [Oluwabusinuolatemi/Telco-customer-churn-rate](https://github.com/Oluwabusinuolatemi/Telco-customer-churn-rate)@[d35027bc4d...](https://github.com/Oluwabusinuolatemi/Telco-customer-churn-rate/commit/d35027bc4db0b7a2e3ee5412f59521c3621750a2)
#### Wednesday 2023-11-15 23:59:55 by Oluwabusinuolatemi

Add files via upload

TelcoCustomer Churn Dataset 

Analysis of the Churn rate using Power BI

OVERVIEW

The CSV file contained information of subscribers and this includes their ID, Gender, If they have dependants, If the have a Partner, if they have senior citizens, how long they have been subscribed for, if they were subscribed to phone services, multiple lines, Online Security, Online Bcakup, streamingTV, Streaming Movie, if they received Tech Support, their means of payment and if they are churned 

Altogether we have 21 coloums, 7043 Rows

The Business Question that will be answered here are as follows:

1. Total Number of subcribers
2. Total Number of churned customers
3. Average Tenure of Churned and not Churned customers 
4 what is the organaisation total Churn Rate
5. Which internet service has the highest rate of churn 
6.  What is the churn rate if subscribers have multiple lines 
7. What is the churn rate of internet service subscribers
8. What internet service has the highest churn rate 
9. What is the churn rate of Online security subscribers
10. What is the churn rate of online backup subscribers
11. What is the churn if Subscribers device protection 
12. What is the churn rate  if Subscribers enjoy tech support 
13. What is the churn rate  if Subscribers enjoy streaming Tv and Streaming movies
14. What contract length has the highest churn rate
15. What payment method has the highest churn rate 
16. What gender has the highest churn rate 
17. What is the churn rate if a subscriber is catering for a senior citizen
18. Does having a partner affect the churn rate 
19. Does having a dependent affect the churn rate 

Data Collection 

The dataset was provided by @manlikeSQI during a tutorial session 

Data Preparation
Given the nature of the dataset provided it beneficial to clean and visualize it in Power BI

Data Issues 
The data does not require alot of cleaning,the data also has no duplicate coloum

Conclusion:

1. There are a total of 7043 subscribers 

2. The Churn rate is 26.54%

3. Customers subscribed to the Fiber Optic internet service are more likely to churn

4. The female are more likely to churn this the male gender 

5. Customers paying by Credit card (automatic) have the lowest churn rate while customers paying by Electronic check has the highest churn rate ( it is therefore advised that customers should be advised to use the credit card (automatic) as a means of payment) 

6. Customers subscribed to Fiber optic, who has no Online security and does not also have online backup has the highest rate of churn 

7. Customers who are subscribed month to month, who does not have dependents and partners have the highest rate of churn

---

