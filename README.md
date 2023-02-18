## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-02-17](docs/good-messages/2023/2023-02-17.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,259,890 were push events containing 3,415,638 commit messages that amount to 261,721,899 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 58 messages:


## [Boopideedoo/tgstation](https://github.com/Boopideedoo/tgstation)@[374c8340c8...](https://github.com/Boopideedoo/tgstation/commit/374c8340c8c99586a4b4b8e978947c0b0f83a9d7)
#### Friday 2023-02-17 00:02:21 by Jacquerel

Console Hack / Unfavourable Events won't run ghost roles which don't have time to do anything (#73343)

## About The Pull Request

Fixes #69201
The dynamic subsystem will never roll a new antagonist once the shuttle
is past the point of no return, but this check is bypassed by Console
Hacks and Unfavourable Event rolls (which are chiefly triggered from
console hacks, but also from when the Revolution wins).

I have made these procs more discerning.
Unfavourable Events will now never pick any heavy dynamic midround if
the shuttle is past the point of no return.
Console Hacking will now never spawn sleeper agents if the shuttle is
past the point of no return, and won't spawn Fugitives or Pirates if the
shuttle is called at all even if it can still be recalled

It's my feeling that given the need to get organised and move a ship to
the station there isn't really time for either of those events to
actually start properly rolling, but if you feel like that information
might be metagamed in some way by messing around with the shuttle (not
sure why or to what end, but it's technically manipulatable if you know
how the code works?) I can just give these the same restriction as
Traitor even if it means the bounty hunters risk showing up after the
shuttle has already left.

## Why It's Good For The Game

To some extent it's your own fault for clicking the popup while knowing
full well how much round time is left until the game ends, but it's
still disappointing to see a Blob or Pirates or Wizard alert appear at a
time when they can't possibly do anything interesting.
This is more true for the Pirate and Fugitive events because they
involve teamwork, placing a space ship, travel between the ship and the
station, and in the case of Fugitives its own internal five minute timer
before the other team actually arrives.

## Changelog

:cl:
fix: Hacking the Comms Console or winning a Revolution can no longer
spawn antagonists if there's not enough time left in the round for them
to antagonise anyone.
/:cl:

---
## [Boopideedoo/tgstation](https://github.com/Boopideedoo/tgstation)@[645054b489...](https://github.com/Boopideedoo/tgstation/commit/645054b489212a34d80e6e1a7fa1320e35d9bfc7)
#### Friday 2023-02-17 00:02:21 by MrMelbert

Fixes encoding on syndicate declaration of war, Fixes a way to send unencoded text to newscasters (#73366)

## About The Pull Request

Ugly


![image](https://user-images.githubusercontent.com/51863163/218280311-f282bd75-2f6e-4290-b3f4-d9d856ff36d3.png)

Nice


![image](https://user-images.githubusercontent.com/51863163/218280315-233da635-f777-4006-8778-c673b83e887e.png)

War dec: 

- TGUI inputs for syndicate declaration of war no longer double-encode
sending customized messages into the announcement
- The alert box for the war declaration no longer has multiple errors
(an extra bracket, negative seconds)
- Reduces some copy and paste in the war declaration device
- Adds a debug item that's a war declaration device but it only does the
sound and message. Please don't fake war decs admins it's a horrible
idea

Additionally

- Documented `priority_announcement`
- Ensures all uses of text and title in the priority announcement
message are encoded (Some were not!)

## Why It's Good For The Game

Encoding looks bad, unencoded text is also bad

## Changelog

:cl: Melbert
fix: Syndicate declarations of war no longer murder apostrophes and
their friends
fix: The alert box for the declaration of war no longer looks funky, and
counts forwards in time rather than backwards
fix: Fixed being able to send unencoded HTML to newscasters
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[32c31b8fc0...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/32c31b8fc08aaec64dfc0583e02ed55b193ffa19)
#### Friday 2023-02-17 00:08:31 by SkyratBot

[MIRROR] Lighting source refactor (Tiny) [MDB IGNORE] (#19370)

* Lighting source refactor (Tiny) (#73284)

## About The Pull Request

I'm doing two things here. Let's get the boring bit out of the way.

Lighting source updates do three distinct things, and those things were
all in one proc.
I've split that one proc into three, with the first two feeding into the
third.

Second, more interesting thing.

An annoying aspect of our lighting system is the math we use for
calculating luminosity is hardcoded.
This means that we can't have subtypes that are angled, or that have
squared falloff, etc. All has to look the same.
This sucks, and it shows.

It has to be, goes the thinking, because we need very fast lookups that
OOP cannot provide.
We can't bog down the main equation with fluff, because the main
equation needs to be really speedy.

The thing about this equation is the only variants on a turf to turf
basis is exactly how far turfs are from the center.
So what if, instead of doing the math in our corner worker loop, we
build lookup tables to match our current source's state.
The tables, like a heatmap, could encode the lighting of any point along
the line.

This is actually faster then doing the math each time, because the list
generation can be cached.
It also means we've pulled the part we want to override out of hotcode.
It's cheap to override now, and a complex subtype, with angles and such
would have no impact on the typical usage.

So the code's faster, easier to read, and more extensible.
And we can do stuff like squared falloff for some lights in future
without breaking others.

Winning!

## Why It's Good For The Game

Winning

* Lighting source refactor (Tiny)

---------

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [hexagon-geo-surv/qtbase](https://github.com/hexagon-geo-surv/qtbase)@[cc4a392450...](https://github.com/hexagon-geo-surv/qtbase/commit/cc4a3924500ccb75b18a1ecec1037ff5aeb16820)
#### Friday 2023-02-17 00:23:29 by Marc Mutz

QVarLengthArray: fix UBs in emplace()/insert() ([basic.life], broken class invariant)

There are two problems in emplace_impl() (the same code exists as
rvalue insert() since 5.10):

First, the old code updated size() at the end of the function.

However, if, after constructing the new end element, one of the
subsequent move-assignments fail (throws), then the class invariant
that size() be the number of alive elements in the container is
broken, with the immediate consequence that the QVLA dtor would not
destroy this element, but surely other unpleasantness (UB) that the
C++ lifetime rules decide to throw our way.

Similarly, in the trivially-relocatable case, the memmove() starts the
life-time of the new end object, so if the following placement new
fails, we're in the same situation.

The latter case is worse, though, since here we leave *b in some weird
zombie state: the memmove() effectively ended its lifetime in the
sense that one mustn't call the destructor on the source object after
trivial relocation, but C++ doesn't agree and QVLA's dtor will happily
call b->~T() as part of its cleanup.

The other ugly thing is that we're using placement new into an object
that C++ says is still alive. QString is trivially relocatable, but
not trivially copyable, so we can't end a QString's lifetime by
placement-new'ing a new QString instance into it without first having
ended the old object's lifetime.

The fix for both of these is, fortunately, the same: It's a rotate!™

By using emplace_back() + std::rotate(), we always place the new
object in a spot that didn't contain an alive object (in the C++
sense) before, we always update the size() right after doing so,
maintaining that invariant, and we then rotate() it into place, which
doesn't leave zombie objects around.

std::rotate() is such a fundamental algorithm that we should trust the
STL implementors to have optimized it well:
https://stackoverflow.com/questions/21160875/why-is-stdrotate-so-fast

We know we can do better only for trivially-relocatable, but
non-trivially-copyable types (ex: QString), so in order to not lose
the memmove() optimization, we now fall back to std::rotate on raw
memory for that case.

Amends dd58ddd5d97f0663d5fafb7e81bff4fc7db13ba7.

Change-Id: Iacce4488ca649502861e0ed4e084c9fad38cab47
Reviewed-by: Thiago Macieira <thiago.macieira@intel.com>
Reviewed-by: Fabian Kosmale <fabian.kosmale@qt.io>
(cherry picked from commit e24df8bc726d12e80f3f1d14834f9305586fcc98)
Reviewed-by: Mårten Nordheim <marten.nordheim@qt.io>

---
## [Dosendusche/foundryvtt-starfinder](https://github.com/Dosendusche/foundryvtt-starfinder)@[a1eed2f86e...](https://github.com/Dosendusche/foundryvtt-starfinder/commit/a1eed2f86e2353efe21df366d5ae9a43f9d4e8e1)
#### Friday 2023-02-17 00:32:02 by Dosendusche

removed unnecessary async populate.

Caused bugs while calculating save dc for spells.
Absolute wild code that calls an async function without awaiting it and still relying on it's result which magically fucking works. No I don't know why and we better not touch it again because it's a calculation done on actor update.

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[26688597e3...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/26688597e317b30cdad644954c2f4654afec2b97)
#### Friday 2023-02-17 00:41:44 by Rimi Nosha

[MODULAR] [MDB IGNORE] Dim Lighting Some More, Removes Egregious Lighting Varedits in Interlink, Dynamically Calculate Night Shift Light Brightness and Color (#19039)

* Boom.

* Oop

* Fuck off single letter vars

* Fingers crossed.

* IT WORKS

* Adjust funny numbers

* Update a comment

---
## [Bluewry/spookening-pack](https://github.com/Bluewry/spookening-pack)@[303edcc18d...](https://github.com/Bluewry/spookening-pack/commit/303edcc18d1781a16f8d1accb6f5966367ab2d6c)
#### Friday 2023-02-17 01:07:38 by Alex

Small updates and additions

- Gold/Iron Nuggies
- Fucking Awful Pun -> Not Funny
- Updated Ice Bucket time
- Derpstone
- Enchant Level V -> Pog
- Flask of Crimson Tears
- Potion of Scarlet Rot

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[c58cbb4dfb...](https://github.com/tgstation/tgstation/commit/c58cbb4dfb42e0d9d6198c3ad581dc5a4d2f8f48)
#### Friday 2023-02-17 01:14:26 by John Willard

Reworked PDA menu & NtOS themes (#73070)

## About The Pull Request

This is a port/rework of
https://github.com/yogstation13/Yogstation/pull/15735 - I changed a lot
of how it acted (some themes are locked behind maintenance apps).

The original author allowed this port to happen, and I really liked how
it looked there so I'd like to add it here.

### Applications

Removes the hardware configurator application, as all it did was show
you your space and battery now that all hardware was removed. These are
things your PC does by default, so it was just a waste of space.
Adds a Theme manager application instead, which allows you to change
your PDA's theme at will.
Adds a new Maintenance application that will give a new theme, however
it will also increase the size of the theme manager app itself as it's
bloatware.

### Menu

There's now a bar at the top of the menu showing 'special' tablet apps
which, for one reason or another, should stand out from the rest of the
apps. Currently this is PDA messenger and the Theme manager

Flashlight and Flashlight color is now only an icon, and is shown on the
same line as Updating you ID


https://cdn.discordapp.com/attachments/961874788706574386/1069621173693972551/2023-01-30_09-10-52.mov


![image](https://user-images.githubusercontent.com/53777086/215501361-5ea3086e-2ff5-4ab1-bde4-8a3d14014fce.png)

### Themes

Adds a lot of themes to choose from, although SOME are hidden behind
Maintenance applications, which will give you a random theme. These are
bloatware however, so they come with some extra cost to the app's
required space storage.

Themes are now supported on ALL APPLICATIONS! If you have a computer
theme, you will have that theme in EVERY app you enter, rather than just
a select few.
ALSO also, emagging the tablet will automatically set & unlock the
Syndicate theme, which makes your PDA obvious but you can disguise it if
you wish through just re-painting it to something else.


https://cdn.discordapp.com/attachments/828923843829432340/1069565383155122266/2023-01-30_05-29-53.mov

### Preferences

This also adds a pref for theme, reworking the ringtone code to work
with it as well. I also removed 2 entirely unused PDA prefs just 'cause.

Screenshot not up-to-date, they now have proper names.

![image](https://user-images.githubusercontent.com/53777086/215463669-0fe9951a-71f8-4b71-a97d-b79b5a2f945a.png)

### Other stuff

Made defines for device_themes
Added support for special app-side checks to download files
Fixed programs downloading themselves TWICE because defines all had the
same definition
Removes the Chemistry computer disk as it was empty due to chemistry
app's removal
Removes the 'run_emag' proc, since apps can directly refer to the
computer to check for emag status instead.
Moved over and added better documentation on data computer files, and
moved the ordnance ones to the same file as the others.

## Why It's Good For The Game

It makes PDAs a lot more customizable while adding more features to
maintenance applications. I think the themes look cool and it fits with
PDAs being "personal" anyways.

I also explained most of my other arguments in the about section, such
as the hardware configuration application.

## Changelog

:cl: Chubbygummibear & JohnFulpWillard
add: A ton of new NtOS themes, which are accessible by the new Themify
application that comes with all PCs.
add: Emagging a PC now defaults it to the Syndicate option (and adds it
to go back to it if you wish)
add: There's a new maintenance app that gives you rarer themes
qol: The NtOS Main menu was moved around, added "header" applications
that are shown where the Flashlight is, such as your Theme manager and
PDA messenger.
code: Made defines for device_themes
code: Added support for special app-side checks to download files
code: Removes the 'run_emag' proc, since apps can directly refer to the
computer to check for emag status instead.
fix: Programs no longer download twice.
del: Removes the Chemistry computer disk as it was empty due to
chemistry app's removal
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [samuel40791765/aws-lc](https://github.com/samuel40791765/aws-lc)@[4263903bd1...](https://github.com/samuel40791765/aws-lc/commit/4263903bd1d15d56c47cbd6440bea657df2c142e)
#### Friday 2023-02-17 01:50:03 by David Benjamin

Maintain a frame pointer in aesni-gcm-x86_64.pl and add SEH unwind codes

Some profiling systems cannot unwind with CFI and benefit from having a
frame pointer. Since this code doesn't have enough register pressure to
actually need to use rbp as a general register, this change tweaks
things so that a frame pointer is preserved.

As this would invalidate the SEH handler, just replace it with proper
unwind codes, which are more profiler-friendly and supportable by our
unwind tests. Some notes on this:

- We don't currently support the automatic calling convention conversion
  with unwind codes, but this file already puts all arguments in
  registers, so I just renamed the arguments and put the last two
  arguments in RDI and RSI. Those I stashed into the parameter stack
  area because it's free storage.

- It is tedious to write the same directives in both CFI and SEH. We
  really could do with an abstraction. Although since most of our
  functions need a Windows variation anyway.

- I restored the original file's use of PUSH to save the registers.
  This matches what Clang likes to output anyway, and push is probably
  smaller than the corresponding move with offset. (And it reduces how
  much thinking about offsets I need to do.)

- Although it's an extra instruction, I restored the original file's
  separate fixed stack allocation and alloca for the sake of clarity.

- The epilog is constrained by Windows being extremely picky about
  epilogs. (Windows doesn't annotate epilogs and instead simulates
  forward.) I think other options are possible, but using LEA with an
  offset to realign the stack for the POPs both matches the examples in
  Windows and what Clang seems to like to output. The original file used
  MOV with offset, but it seems to be related to the funny SEH handler.

- The offsets in SEH directives may be surprising to someone used to CFI
  directives or a SysV RBP frame pointer. All three use slightly
  different baselines:

  CFI's canonical frame address (CFA) is RSP just before a CALL (so
  before the saved RIP in stack order). It is 16-byte aligned by ABI.

  A SysV RBP frame pointer is 16 bytes after that, after a saved RIP and
  saved RBP. It is also 16-byte aligned.

  Windows' baseline is the top of the fixed stack allocation, so
  potentially some bytes after that (all pushreg and allocstack
  directives). This too is required to be 16-byte aligned.

  Windows, however, doesn't require the frame register actually contain
  the fixed stack allocation. You can specify an offset from the value
  in the register to the actual top. But all the offsets in savereg,
  etc., directives use this baseline.

Performance difference is within measurement noise.

This does not create a stack frame for internal functions so
frame-pointer unwinding may miss a function or two, but the broad
attribution will be correct.

Change originally by Clemens Fruhwirth. Then reworked from Adam
Langley's https://boringssl-review.googlesource.com/c/boringssl/+/55945
by me to work on Windows and fix up some issues with the RBP setup.

Bug: b/33072965, 259
Change-Id: I52302635a8ad3d9272404feac125e2a4a4a5d14c
Reviewed-on: https://boringssl-review.googlesource.com/c/boringssl/+/56128
Reviewed-by: Adam Langley <agl@google.com>
Commit-Queue: David Benjamin <davidben@google.com>
(cherry picked from commit 0d5b6086143d19f86cc5d01b8944a1c13f99be24)

---
## [yogstation13/Yogstation](https://github.com/yogstation13/Yogstation)@[818973e1e9...](https://github.com/yogstation13/Yogstation/commit/818973e1e91edd0d62357f0ca4361916fb1d3f69)
#### Friday 2023-02-17 03:40:04 by wejengin2

fixes some issues in infiltrator base (#17861)

* huh

* man

* adds griddle

* that's really funny but fuck you

---------

Co-authored-by: Byemoh <baiomurang@gmail.com>

---
## [VitalyAnkh/wasmtime](https://github.com/VitalyAnkh/wasmtime)@[1efee4abdf...](https://github.com/VitalyAnkh/wasmtime/commit/1efee4abdfdb48b694828f0dc2ead394ba42a234)
#### Friday 2023-02-17 03:48:00 by Alex Crichton

Update CI to use GitHub's Merge Queue (#5766)

GitHub recently made its merge queue feature available for use in public
repositories owned by organizations meaning that the Wasmtime repository
is a candidate for using this. GitHub's Merge Queue feature is a system
that's similar to Rust's bors integration where PRs are tested before
merging and only passing PRs are merged. This implements the "not rocket
science" rule where the `main` branch of Wasmtime, for example, is
always tested and passes CI. This is in contrast to our current
implementation of CI where PRs are merged when they pass their own CI,
but the code that was tested is not guaranteed to be the state of `main`
when the PR is merged, meaning that we're at risk now of a failing
`main` branch despite all merged PRs being green. While this has
happened with Wasmtime this is not a common occurrence, however.

The main motivation, instead, to use GitHub's Merge Queue feature is
that it will enable Wasmtime to greatly reduce the amount of CI running
on PRs themselves. Currently the full test suite runs on every push to
every PR, meaning that our workers on GitHub Actions are frequently
clogged throughout weekdays and PRs can take quite some time to come
back with a successful run. Through the use of a Merge Queue, however,
we're able to configure only a small handful of checks to run on PRs
while deferring the main body of checks to happening on the
merge-via-the-queue itself. This is hoped to free up capacity on CI and
overall improve CI times for Wasmtime and Cranelift developers.

The implementation of all of this required quite a lot of plumbing and
retooling of our CI. I've been testing this in an [external
repository][testrepo] and I think everything is working now. A list of
changes made in this PR are:

* The `build.yml` workflow is merged back into the `main.yml` workflow
  as the original reason to split it out is not longer applicable (it'll
  run on all merges). This was also done to fit in the dependency graph
  of jobs of one workflow.

* Publication of the `gh-pages` branch, the `dev` tag artifacts, and
  release artifacts have been moved to a separate
  `publish-artifacts.yml` workflow. This workflow runs on all pushes to
  `main` and all tags. This workflow no longer actually preforms any
  builds, however, and relies on a merge queue or similar being used for
  branches/tags where artifacts are downloaded from the workflow run to
  be uploaded. For pushes to `main` this works because a merge queue is
  run meaning that by the time the push happens all artifacts are ready.
  For release branches this is handled by..

* The `push-tag.yml` workflow is subsumed by the `main.yml` workflow. CI
  for a tag being pushed will upload artifacts to a release in GitHub,
  meaning that all builds must finish first for the commit. The
  `main.yml` workflow at the end now scans commits for the preexisting
  magical marker and pushes a tag if necessary.

* CI is currently a flat list of "run all these jobs" and this is now
  rearchitected to a "fan out" approach where some jobs run to determine
  the next jobs to run which then get "joined" into a finish step. The
  purpose for this is somewhat nuanced and this has implications for CI
  runtime as well. The Merge Queue feature requires branches to be
  protected with "these checks must pass" and then the same checks are
  gates both to enter the merge queue as well as pass the merge queue.
  The saving grace, however, is that a "skipped" check counts as
  passing, meaning checks can be skipped on PRs but run to completion on
  the merge queue. A problem with this though is the build matrix used
  for tests where PRs want to only run one element of the build matrix
  ideally but there's no means on GitHub Actions right now for the
  skipped entries to show up as skipped easily (or not that I know of).
  This means that the "join" step serves the purpose of being the single
  gate for both PR and merge queue CI and there's just more inputs to it
  for merge queue CI. The major consequence of this decision is that
  GitHub's actions scheduling doesn't work out well here. Jobs are
  scheduled in a FIFO order meaning that the job for "ok complete the CI
  run" is queued up after everything else has completed, possibly
  after lots of other CI requests in the middle for other PRs. The hope
  here is that by using a merge queue we can keep CI relatively under
  control and this won't affect merge times too much.

* All jobs in the `main.yml` workflow will not automatically cancel the
  entire run if they fail. Previously this fail-fast behavior was only
  part of the matrix runs (and just for that matrix), but this is
  required to make the merge queue expedient. The gate of the merge
  queue is the final "join" step which is only executed once all
  dependencies have finished. This means, for example, that if rustfmt
  fails quickly then the tests which take longer might run for quite
  awhile before the join step reports failure, meaning that the PR sits
  in the queue for longer than needed being tested when we know it's
  already going to fail. By having all jobs cancel the run this means
  that failures immediately bail out and mark the whole job as
  cancelled.

* A new "determine" CI job was added to determine what CI actually needs
  to run. This is a "choke point" which is scheduled at the start of CI
  that quickly figures out what else needs to be run. This notably
  indicates whether large swaths of ci (the `run-full` flag) like the
  build matrix are executed. Additionally this dynamically calculates a
  matrix of tests to run based on a new `./ci/build-test-matrix.js`
  script. Various inputs are considered for this such as:

  1. All pushes, meaning merge queue branches or release-branch merges,
     will run full CI.
  2. PRs to release branches will run full CI.
  3. PRs to `main`, the most common, determine what to run based on
     what's modified and what's in the commit message.

  Some examples for (3) above are if modifications are made to
  `cranelift/codegen/src/isa/*` then that corresponding builder is
  executed on CI. If the `crates/c-api` directory is modified then the
  CMake-based tests are run on PRs but are otherwise skipped.
  Annotations in commit messages such as `prtest:*` can be used to
  explicitly request testing.

Before this PR merges to `main` would perform two full runs of CI: one
on the PR itself and one on the merge to `main`. Note that the one as a
merge to `main` was quite frequently cancelled due to a merge happening
later. Additionally before this PR there was always the risk of a bad
merge where what was merged ended up creating a `main` that failed CI to
to a non-code-related merge conflict.

After this PR merges to `main` will perform one full run of CI, the one
as part of the merge queue. PRs themselves will perform one test job
most of the time otherwise. The `main` branch is additionally always
guaranteed to pass tests via the merge queue feature.

For release branches, before this PR merges would perform two full
builds - one for the PR and one for the merge. A third build was then
required for the release tag itself. This is now cut down to two full
builds, one for the PR and one for the merge. The reason for this is
that the merge queue feature currently can't be used for our
wildcard-based `release-*` branch protections. It is now possible,
however, to turn on required CI checks for the `release-*` branch PRs so
we can at least have a "hit the button and forget" strategy for merging
PRs now.

Note that this change to CI is not without its risks. The Merge Queue
feature is still in beta and is quite new for GitHub. One bug that
Trevor and I uncovered is that if a PR is being tested in the merge
queue and a contributor pushes to their PR then the PR isn't removed
from the merge queue but is instead merged when CI is successful, losing
the changes that the contributor pushed (what's merged is what was
tested). We suspect that GitHub will fix this, however.

Additionally though there's the risk that this may increase merge time
for PRs to Wasmtime in practice. The Merge Queue feature has the ability
to "batch" PRs together for a merge but this is only done if concurrent
builds are allowed. This means that if 5 PRs are batched together then 5
separate merges would be created for the stack of 5 PRs. If the CI for
all 5 merged together passes then everything is merged, otherwise a PR
is kicked out. We can't easily do this, however, since a major purpose
for the merge queue for us would be to cut down on usage of CI builders
meaning the max concurrency would be set to 1 meaning that only one PR
at a time will be merged. This means PRs may sit in the queue for awhile
since previously many `main`-based builds are cancelled due to
subsequent merges of other PRs, but now they must all run to 100%
completion.

[testrepo]: https://github.com/bytecodealliance/wasmtime-merge-queue-testing

---
## [Tichij/issrc](https://github.com/Tichij/issrc)@[118c151654...](https://github.com/Tichij/issrc/commit/118c15165401bb2acb62358f963777c44fb9c582)
#### Friday 2023-02-17 04:43:39 by Johannes Schindelin

Prevent `comctrl32.dll` from being inadvertently side-loaded

When running an installer from the Downloads folder, we do not trust any
file in that folder apart from the installer itself.

However, the way we need to mention `comctl32.dll` in the manifest
(because we want to use version 6, which cannot be simply loaded like
all the other `.dll` files because we would then end up with version 5)
unfortunately lets Windows look for a DLL side-load payload next to the
executable.

Now, it is relatively hard for a hacker to social-engineer their way to
a `<installer>.exe.Local` folder that contains the exact right subfolder
that then contains a usable (but maliciously-crafted) `comctl32.dll`.

However, we should prevent this if possible.

And it _is_ possible because we're copying the installer into a
temporary directory before spawning it there _anyway_, and before that
we do not need any visual styles, therefore we're plenty fine with using
`comctl32.dll` version 5 until that point.

So let's do this: modify the manifest of the installer (but not of its
compressed payload) so that it prevents DLL side-loading of
`comctl32.dll`.

Signed-off-by: Johannes Schindelin <johannes.schindelin@gmx.de>

---
## [Rustybuckets6601/tgstation](https://github.com/Rustybuckets6601/tgstation)@[728a0f1b91...](https://github.com/Rustybuckets6601/tgstation/commit/728a0f1b9147197bb81f22d946f67e9d08719d5a)
#### Friday 2023-02-17 04:51:04 by Jacquerel

Grand Ritual: Alternate Wizard objective (Wizard Events II) (#72918)

Adds an alternate greentext objective for Wizards known as the "Grand
Ritual". This was initially the gimmick of a different wizard-related
antagonist downstream. I didn't get permission to port it, so I'm
attaching it to regular Wizards instead.

Wizards will spawn in with a new Grand Ritual button next to their
antagonist info button. Pressing it will pinpoint them towards their
next Ritual Location (a randomly chosen region of the space station).
Once within that location, pressing it will summon a magic circle and
obliterate any dense objects which are in the way. This also puts the
ability on a two minute cooldown.
Clicking on the magic circle with an empty hand will begin a three-stage
invocation to gather magical power. You can interrupt this invocation at
any time and will resume from the last stage you completed (if you
finished two stages you only need to do one more).
Once you complete a ritual, a random event will be triggered based on
how many rituals you have performed so far. These tend to be ones which
annoy the crew in some manner, and Wizard Events are included in the
list. Additionally, something weird will usually happen to the room you
are in.
Then you are assigned a new location and can toddle off to do it again.

Once you have done this three times, you will be picked up by the
station's sensors every time you start a subsequent ritual and should
expect annoyed company to come investigate.
Once you have done this six times, you can finally spend all of that
accumulated power on the seventh Grand Finale ritual. Completing this
grants you victory at the end of the round and will have a larger,
flashier effect which you can pick from a list of options, think of it
like a wizard equivalent of a Traitor Final Objective or Heretic
Ascension.
After that you can still keep doing rituals if you want to pester the
crew further by summoning more random events, you've already "won" at
this point so now it's your job to make them want to go home.

I think it'd be more fun to just find out what the Finale ritual can do
by seeing it happen but maintainers will probably want a list of its
precise capabilities, so here it is:

Currently completing a ritual also has a chance to create Heretic
Reality Tears (of both varieties, available for Heretics to eat and
visible to crew) as a kind of cross-antagonist interaction which seemed
to make sense to me but if this seems thematically or mechanically
inappropriate it's easy to strip out.

---
## [SwordOfSouls/Iris](https://github.com/SwordOfSouls/Iris)@[dea3ec80ac...](https://github.com/SwordOfSouls/Iris/commit/dea3ec80ac2802bc4197d44ce03aafef64e9077d)
#### Friday 2023-02-17 05:25:37 by CocoTheOwner

Fix image mapping math

Fixes snippet code, prevents an NPE, fixes centered for coordinateScale scaled image noises, fixes tiling on negative numbers (-1 % 2 = -1, a free fuck you from java)

---
## [Kassicus/tower-def](https://github.com/Kassicus/tower-def)@[e29be7695b...](https://github.com/Kassicus/tower-def/commit/e29be7695b67cc1d04c278a6313d1e7606bdf32a)
#### Friday 2023-02-17 06:02:08 by Kason

Made the enemy and started waypoint finding

This shit fucking sucks, its overshooting its position and it doesnt
make a ton of sense... I think the issue is simply that the speed is too
fast?

---
## [Psychtoolbox-3/Psychtoolbox-3](https://github.com/Psychtoolbox-3/Psychtoolbox-3)@[b85250b062...](https://github.com/Psychtoolbox-3/Psychtoolbox-3/commit/b85250b062a7930681cdf7050f3e40457ff962b1)
#### Friday 2023-02-17 06:20:13 by Mario Kleiner

PsychHID/OSX: Avoid calling PsychHIDWarnAccessDenied frequently.

The latest fix for the latest security bullshit, introduced sometime after macOS
10.15 Catalina. This was found when testing Octave on macOS 12.5 Monterey.

Apparently the call to IOHIDCheckAccess() by PsychHIDWarnAccessDenied()
is now extremely costly on macOS 12 (possibly also macOS 11 - untested) iff
the host application was launched from Terminal.app instead of standalone via
clicking a launch icon. This showed on Octave 6.4 after upgrade to macOS 12.5,
as octave is always launched from Terminal, regardless if in console mode or
GUI mode. Matlab appeared unaffected, as it is usually launched by clicking the
Matlab icon, but if one launches Matlab from a terminal, the same happens.

Why IOHIDCheckAccess() was suddenly turned into such an expensive operation
by the iDiots, i don't know, but our workaround is to no longer call it at each
invocation of KbCheck or KbQueueCreate, but only at PsychHID startup, and
hope this does not have other new bad effects.

Note access time exploded from way less than 1 msec to over 15 msecs! Great
work Apple!

Now we are back to identical performance on Matlab and Octave in both GUI
and commandline mode. Performance is bad compared to Linux or Windows,
but manageable at about 2.4 msecs on macOS 12.5 Monterey on a MBP 2017.
However, if run on a MacBook with touchbar, two PsychHID('KbCheck') calls
are needed for each KbCheck() call, because the touchbar is a separate HID
device, serving the important ESCape key and also function keys, so owners
of a shitty touchbar machine will have to live with execution times of KbCheck
on the order of 5 msecs on not that old hardware like the MBP 2017! This makes
animation loops with KbChecks difficult to run beyond 60-100 fps. Such is the
life of Apple customers...

When we are here, improve troubleshooting instructions for security bullshit
on macOS, and fix two compiler warnings new on macOS 12.

---
## [kleinerm/Psychtoolbox-3](https://github.com/kleinerm/Psychtoolbox-3)@[1d87e20d5d...](https://github.com/kleinerm/Psychtoolbox-3/commit/1d87e20d5deba531f6ae8ce6d4b5c98486884d4f)
#### Friday 2023-02-17 06:58:14 by kleinerm

Merge pull request #796 from kleinerm/master

Pull request for Psychtoolbox 3.0.19

### Compatibility:

- Effective now, Psychtoolbox 3.0.18 is end of life and unsupported.

- GStreamer 1.20.5 or later required on MS-Windows, GStreamer 1.22.0 recommended on
  Windows and macOS.

- Octave 6 support cancelled, except for Linux. Octave 7.3 required on macOS and
  Windows.

- New baseline Matlab is R2022b.

- Recommended operating systems: Ubuntu 22.04-LTS Linux, MS-Windows 10, macOS 12.6.

- Ubuntu 20.04-LTS is considered in maintenance mode now. I will likely terminate its
  support in the foreseeable future. Lack of funding by our users makes it impossible
  to provide the levels of long term support as in the past, even for the best suited
  operating system for neuroscience :(.
  
- RaspberryPi OS 10 support is terminated. OS 11 32-Bit required.

- Support for all Windows versions older than recent Windows-10 will soon be completely
  removed. Stick to older Psychtoolbox versions if you want to continue older versions
  for some insane reason. All Windows versions older than Windows 10 are now dead, even
  for Microsoft customers which paid for expensive extended security support.
  It is dead, Jim!

- The macOS 10 (aka Mac OSX) and macOS 11 operating systems should continue to work
  but are officially unsupported and unsupportable. macOS 13 or Apple Silicon is not
  officially supported by this release.

### Highlights:

- OpenXR cross-platform, cross-vendor, cross-device support for VR/AR/MR/XR applications.
  A new modern foundation for these kind of things, highly extensible, future proof, and
  supports a much wider range of devices.

- Improved display mirroring support, including scaling and experimenter overlays for
  having setups with a stimulus monitor for the subject and a "experimenter console" /
  "experimenter control monitor" for the experimenter. PTB is still the only software
  that allows such setups without expensive special hardware and/or screwing up visual
  stimulation timing and timestamping. There are still corner cases where this is difficult,
  but we are better than ever now, increasing our lead over other toolkits further.

- Improved low-level USB support, especially useful for the PsyCalibrator toolbox for
  display calibration under Octave and Matlab.

- ASIO support for Matlab users on Windows sort-of back through the backdoor, without
  us actually having to add it back or dealing with the legal and licensing nightmares.

- Shitloads of new workarounds for shittons of new bugs brought to you by the iPhone
  company in their latest iToys operating systems.

### All:

- The main new feature, after over 700 hours of development, spread over 12 months,
  is our new OpenXR driver for virtual reality, augmented reality and mixed reality
  applications, known as eXtended Reality. The new PsychOpenXR driver should work on
  all VR/AR/MR/XR devices from all vendors on all operating systems which have an
  OpenXR 1 specification compliant runtime installed on your machine. So far the theory.
  In practice, this means GNU/Linux X11 and MS-Windows 10 and later, and so far it has
  only be tested with an Oculus Rift CV-1 VR HMD and Oculus touch controllers, remote
  and XBox 360 controller. Code for using other form-factors than VR HMD's is not yet
  implemented, but this driver should provide the foundation for relatively extension
  into this new realms if wanted. The whole topic deserves its own dedicated and detailed
  posts, so stay tuned. Some more overview info and setup instructions are to be found via
  'help OpenXR', the new drivers specific api in 'help PsychOpenXR', the general api
  improvements and help - sufficient for most use cases - in 'help PsychVRHMD', as before.
  Development of this driver was sponsored by a consumer VR company which wants to stay
  anonymous and not specifically credited here, so thank you for contributing most of the
  funding. As funding was insufficient to complete this very complex project, Mathworks
  (https://www.mathworks.com/solutions/neuroscience.html) sponsored another quarter of the
  remaining costs, thanks! Of course that means some other highly interesting project had
  to be delayed indefinitely, as the amount of funding we get from Mathworks is fixed, just
  the distribution of the fixed some to work items is flexible. In total, funding was totally
  insufficient for making any urgently needed profit or even breaking even nonetheless, so we
  end this one year project with a serious net loss of over 3000 Euros at this point, without
  the project being finished to my quality and performance standards, barely reaching what I
  would consider the minimum viable product from my perspective, but almost certainly still
  much better than anything competing out there for vision science applications. I expect
  more financial losses related to this area of functionality unless new contract work or
  funding come in, related to OpenXR aka VR/AR/MR/XR applications.

  The new driver should be reasonably backwareds compatible, essentially a drop-in replacement,
  so code written to our recommendations should work unchanged, just on a much wider variety
  of VR hardware than before.

  Effective immediately this means that all our old drivers are now considered to be in
  minimal maintenance mode - critical bug fixes only, no further enhancements. They are
  scheduled for removal as soon as the OpenXR driver has proven its maturity to some degree.

- Tons of minor bug fixes and improvements.

- PsychPortAudio: Improve diagnostics and help texts for channel mapping, and a new demo for
  multi-channel audio output, named BasicSoundChannelHoppingDemo.m which motivated those
  improvements, demonstrating dynamic switching between channels of a multi-channel sound card,
  e.g., hopping between the channels of a 24 channel sound card.

- SetStereoSideBySideParameters(): Add option to specify offsets in pixels, and add basic
  RemapMouse() support to deal better with changed stereo display geometry. Various other
  compatibility fixes to SetStereoSideBySideParameters() and RemapMouse() in combination with
  stereo display modes in combination with imaging pipeline geometric transformations like
  FlipHorizontal or FlipVertical. Also for 90 degree step rotation with the PanelFitter.

- Screen: Fix PsychImaging task 'MirrorDisplayTo2ndOutputHead' for most use cases.
  Turns out that this display mirroring task for macOS and MS-Windows only worked for
  trivial configurations without use of the panelfitter, MSAA, image processing or other
  complexities. It also works now when combined with the Vulkan special purpose display
  backend as primary stimulus display and the regular OpenGL method for the "experimenter
  feedback" / "control console" mirror display.

- Add overlay support to the display mirroring tasks 'MirrorDisplayTo2ndOutputHead' and
  'MirrorDisplayToSingleSplitWindow'. The new optional useOverlay parameter for these
  PsychImaging tasks generates a (normally transparent) overlay window, a "head up display"
  on top of the mirror window that shows a mirror image of the stimulus presented to the
  subject on the main stimulation display. overlaywin = PsychImaging('GetMirrorOverlayWindow', win);
  allows to get a window handle overlaywin to this overlay and then use Screen drawing commands
  to draw info only meant to be seen by the experimenter, not the subject, into the overlay.
  A common use case seems to be gaze position or gaze traces of a subject in eyetracking tasks,
  or other live feedback about task progression and subject performance. This is generally
  more flexible than hardware solutions, e.g., as provided by VPixx stimulators or similar
  equipment or some display splitters.

- PsychImaging: Allow size spec of mirror image for mirroring task 'MirrorDisplayToSingleSplitWindow'.
  Dealing with setups where the mirror/console/experimenter monitor has a lower/different resolution
  than the stimulus monitor needs same special rescaling of the mirror image. Implement rescaling +
  some minor optimizations. A future extension may allow to automate handling of such less standard
  display setups, but for now the user has to specify mirror monitor display resolution manually via
  a new optional parameter.

- PsychHID: Add support for synchronous USB bulk and interrupt transfers, and manual of automatic
  claiming of USB interfaces. The new subfunctions 'USBBulkTransfer' and 'USBInterruptTransfer'
  implement synchronous bulk and interrupt transfers. This now allows writing M-File drivers
  for more research equipment. The main motivation was to enable the free and open-source
  PsyCalibrator toolbox for Octave and Matlab to implement support for many more Photometers
  and other light measurement devices in a more efficient manner, starting with the cheap
  SpyderX device. Cfe. https://github.com/yangzhangpsy/PsyCalibrator

- PsychHID: Add PsychHID('USBClaimInterface', usbHandle, interfaceId) for manual claiming of
  device interfaces. This function allows to explicitely claim a USB interface to enable it
  for I/O from/to an USB interface endpoint. Bulk- or interrupt transfers don't work if the
  interface who owns the endpoint has not been claimed. If a call to this function is omitted
  before doing bulk or interrupt transfers, then PsychHID will automatically claim interface 0.
  Claimed interfaces are auto-released when closing an USB device. Kernel drivers potentially
  attached to - and blocking - an interface will be automatically detached, and then reattached
  at device close. In other words: Use of the most commonly used interface 0 does not need any
  extra user code. Use of other interfaces will require this call in time.

  On macOS: Note that if a macOS kernel driver (kext) has already claimed exclusive access to the
  device, then this will only work by detaching the kernel driver, which requires you to run Octave
  or Matlab as root. Only tested by myself with octave via "sudo octave" so far. For the hoops you
  have to jump through on macOS to get this working without sudo, read this FAQ:

  https://github.com/libusb/libusb/wiki/FAQ#how-can-i-run-libusb-applications-under-mac-os-x-if-there-is-already-a-kernel-extension-installed-for-the-device-and-claim-exclusive-access

  Executive summary: Give up, or be prepared to suffer greatly!

- Various help text and documentation updates.

- Terminate support for Python 2.x, it is officially end-of-life since beginning 2020. Only
  Python 3.6 and later are supported by our Python "Mex files" going forward. This makes the
  files also forward compatible with more Python versions by opt-in use of the Py limited api.
  Contributed mostly by Alex Forrence, with some tweaks by Mario Kleiner. Various other minor
  enhancements to PsychPython.
  
### Linux:

- Add support for 64-Bit Octave 7.x, implemented via the shared mex files for Octave 4.4 - Octave 7.3.
  This enables use with Octave on Ubuntu 22.10.

- Screen: Add gpu detection support for NVidia 170 "Ampere" gpu family and "Ada Lovelace" gpu
  family. Avoids some confusing warning and may improve Flip performance by a few dozen microseconds
  in some cases. Use of NVidia graphics cards is still discouraged due to the need of proprietary
  graphics drivers for all modern models, which limit useful functionality compared to gpus with
  open-source drivers, and make general use more tedious and troublesome.

- Drawtext plugin: Add workaround for Mesa bug with small non-anti-aliased text of 8 pixels and
  less. Rarely needed, but somebody in the VR research community needed it, so there.

- Compatibility fixes for the RaspberryPi on RaspberryPi OS 11 aka Debian 11 stable. Especially
  for old RPi 1,2,3 with VideoCore-4 gpu, XOrgConfCreator now generates a special xorg.conf
  file to enable fixes for these gpu's which were not neccessary on older RaspberryPi OS versions.
  Other misc compatibility improvements.
  
  Our build system for ARM / RaspberryPi is no 32-Bit RaspberryPi OS 11, with 32-Bit Octave 6.2,
  32-Bit ARM RaspberryPi 400. 64-Bit operating systems are not supported, and support for the
  legacy RaspberryPi OS 10 is now terminated.

- gamemode.ini: Comment out the amd_performance_level=high gpu perf option.
  Setting amd_performance_level=high for high performance level was found
  to cause stability issues at least on AMD Ryzen-5 2400G "RavenRidge" under
  Ubuntu 20.04.5-LTS with Linux 5.15 under prolonged load, likely a cooling problem.
  It may be safe to enable it for other AMD gpu's, especially well-cooled
  or discrete ones, but better safe than sorry by default, as i don't like
  my main devel machine crashing regularly and other users may also have machines
  with shaky cooling.


### Windows:

- 64-Bit Intel MSVC GStreamer version 1.20.5 is now required as minimum supported version
  for both Octave and Matlab. High quality text rendering will fail with any earlier version!
  From now on we always use the fontconfig-1.dll bundled with GStreamer 1.20.5 and later for
  font matching, which should simplify debugging of future issues on MS-Windows. This version
  also enables the ability to use User installed 3rd party fonts without extra configuration
  work by the user, obsoleting various hacks. GStreamer 1.22.0 was also lightly tested without
  obvious problems, so upgrading to 1.22.0 is recommended for new features, wider support for
  audio/video formats, improved performance and various bug fixes in the multi-media area.

- 64-Bit GNU/Octave 7.3 required for running Psychtoolbox 3.0.19 on Octave.

- Psychtoolbox was built and lightly tested against Matlab R2022b.

- PsychPortAudio: Allow use of a wider range of 3rd party portaudio_x64.dll plugins for the
  underlying PortAudio engine implementation. The most interesting use case of this is for
  users of Matlab, as recent versions of Matlab ship with a Mathworks provided Portaudio
  implementation that has builtin ASIO support, where all the legal licensing and trademark
  issues are taken care of by Mathworks. If one copies the DLL shipping with Matlab into the
  PsychtoolboxRoot() folder, renamed to the filename portaudio_x64.dll instead of the filename
  that Matlab uses (libportaudio.dll), then this will expose basic ASIO support, even when used
  with GNU/Octave. Please note that Mathworks is legally responsible for this ASIO support, whereas
  we do not include any support for ASIO into Psychtoolbox, we merely expose whatever a 3rd party
  portaudio DLL supports, which happens to be also ASIO in case of the Matlab provided dll, so we
  are legally in the clear, while some of our users may be more happy with their sound setup even
  if they refuse to switch to Linux. Obviously these 3rd party driver plugins are completely
  unsupported by us in case of trouble, and likely also by Mathworks, as this is not their intended
  use case, just a side-effect of some functionality that is probably meant for the audio toolbox.

- Update bundled libusb-1 for MS-Windows to most recent version 1.0.26 with many bug fixes and
  improvements over the last 11 years.

### macOS:

- 64-Bit GNU/Octave 7.3 required for running Psychtoolbox 3.0.19 on Octave. Other Octave versions
  from the Octave 6.3+ and 7.x series may work as well, but no guarantees.

- Psychtoolbox was built and lightly tested against Matlab R2022b.

- Switch only supported and lightly tested macOS version from 10.15 Catalina to 12 Monterey.
  No more development or testing on 10.15.7 Catalina, now that it has been wiped from my drive.
  We keep macosx-version-min at 10.11 for the time being, so PTB may still work back to 10.11,
  but no guarantees, and I don't care if it breaks on older systems than macOS 12.6 Monterey.
  macOS 13 Ventura is completely untested and not officially supported yet. Apple Silicon Macs
  continue to be unsupported and untested, with known completely broken visual stimulation timing
  and possible other issues. All mex files are for 64-Bit Intel processor architecture variants of
  Matlab and GNU/Octave only.

- PsychOculusVR: Remove for macOS. No VR virtual reality support on macOS anymore as of PTB 3.0.19.
  It only supported the long time out-of-sale since many years Oculus Rift DK1 and Rift DK2, with an
  Oculus v0.5 runtime for macOS that is not available for download from Oculus or anywhere else
  anymore since years, and only for macOS versions which supported 32-Bit Intel architecture executables,
  iow. doesn't work on macOS 10.15 Catalina and later anymore thanks to Apple breaking backwards
  compatibility with 32-Bit applications.

- Fix performance of PsychHID further for the latest Apple security bullshit, introduced sometime
  after macOS 10.15 Catalina. This was found when testing Octave on macOS 12.5 Monterey, a massive
  performance degradation for KbCheck and related functions if Matlab or Octave are launched from
  a terminal (iow. always for Octave!). Apple screwed up their api's further to increase processing
  time of some time sensitive operation from 1 msec to over 15 msec! Now we are back to about 2.4
  msecs on macOS 12, which is much worse than MS-Windows with less than 1 msecs or Linux with less
  than 0.1 msecs. So now it is merely Apple bad, as most Apple stuff.
  
- Screen: Unbreak our Vulkan display backend via MoltenVK Vulkan-on-Metal again for macOS 12, after
  Apple broke it somewhere after macOS 11. After close to 80 hours of diagnostic work, distributed
  over more than 4.5 months on and off, going down every conceivable route of diagnostics and low-level
  debugging, i could not find anything wrong with my code or MoltenVK. Turns out, it is yet another
  "dumb beyond imagination" bug in the iPhone companies latest macOS 12, nothing we did wrong. The
  root cause is unclear, but now we include a dumb hack which makes it work again, against any rhyme
  or reason. Of course, I don't know if Apple has broken it or will break it again in macOS 13 Ventura
  or later abominations. So basic HDR on macOS is back in the game...
  
- PsychHID: Switch low-level USB support to use of shared libusb-1 backend instead of Apples macOS
  proprietary backend, which became a maintenance nightmare. This now allows all operating systems
  to progress in the same way with shared high-quality code. It does mean however, that if one wants
  to use low-level USB device access, e.g., USB control-/bulk-/interrupt-transfers, one needs to
  install libusb-1.dylib with a minimum version of 1.0.22 from a suitable source, or these functions
  will refuse to work. The most simple way to get this library is via HomeBrew: brew install libusb
  
  The only affected Psychtoolbox function without libusb dylib is the ColorCal2() functions for using
  CRS ColorCal-II devices.

Enjoy!

---
## [rhit-johnsoz2/The-Undecideds](https://github.com/rhit-johnsoz2/The-Undecideds)@[c334746365...](https://github.com/rhit-johnsoz2/The-Undecideds/commit/c33474636568e77dbc3707cd5798c89d38a3cce8)
#### Friday 2023-02-17 07:51:44 by rhit-johnsoz2

Merge pull request #34 from rhit-johnsoz2/newDoc

FUCK YOU Liz :)

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[31d713d4eb...](https://github.com/git-for-windows/git/commit/31d713d4eb41db2428c4bbc334518e7442ee1276)
#### Friday 2023-02-17 08:12:23 by Johannes Schindelin

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

---
## [SyncIt21/The-TG-Station-Fork](https://github.com/SyncIt21/The-TG-Station-Fork)@[74144f2bc9...](https://github.com/SyncIt21/The-TG-Station-Fork/commit/74144f2bc9e69c9829339a1bd7ffa962e37c0cd0)
#### Friday 2023-02-17 08:44:44 by LemonInTheDark

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
## [vietduc1989/odoo](https://github.com/vietduc1989/odoo)@[639cfc76ba...](https://github.com/vietduc1989/odoo/commit/639cfc76ba259eea8f38284192017024809173b3)
#### Friday 2023-02-17 09:03:37 by Romain Derie

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

closes odoo/odoo#109812

Signed-off-by: Quentin Smetz (qsm) <qsm@odoo.com>

---
## [bhavik-goplani/Devweek-Hack](https://github.com/bhavik-goplani/Devweek-Hack)@[248910c737...](https://github.com/bhavik-goplani/Devweek-Hack/commit/248910c737c42eb7a5d5857004c0fa19834eee28)
#### Friday 2023-02-17 09:51:23 by Emma Nasseri

actually did global css igitignore fuck you hudson

---
## [ammarfaizi2/linux-block](https://github.com/ammarfaizi2/linux-block)@[4e9c84f06e...](https://github.com/ammarfaizi2/linux-block/commit/4e9c84f06efee83d89f6a36294a4a272e80deefb)
#### Friday 2023-02-17 11:11:22 by Greg Kroah-Hartman

ANDROID: struct io_uring ABI preservation hack for 5.10.162 changes

In the 5.10.162 release, the io_uring code was synced with the version
that is in the 5.15.y kernel tree in order to resolve a huge number of
potential, and known, problems with the codebase.  This makes for a more
secure and easier-to-update-and-maintain 5.10.y kernel tree, so this is
a great thing, however this caused some issues when it comes to the
Android KABI preservation and checking tools.

A number of the io_uring structures get used in other core kernel
structures, only as "opaque" pointers, so there is not any real ABI
breakage.  But, due to the visibility of the structures going away, the
CRC values of many scheduler variables and functions were changed.

In order to preserve the CRC values, to prevent all device kernels to be
forced to rebuild for no reason whatsoever from a functional point of
view, we need to keep around the "old" io_uring structures for the CRC
calculation only.  This is done by the following definitions of struct
io_identity and struct io_uring_task which will only be visible when the
CRC calculation build happens, not in any functional kernel build.

Yes, this all is a horrible hack, and these really are not the true
structures that any code uses, but so life is in the world of stable
apis.

Bug: 161946584
Bug: 268174392
Fixes: dc567ece9884 ("UPSTREAM: io_uring: import 5.15-stable io_uring")
Signed-off-by: Greg Kroah-Hartman <gregkh@google.com>
Change-Id: I2294f220ae78fe9aa32ee25b81829ae765e9deb2

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[873ab411b7...](https://github.com/mrakgr/The-Spiral-Language/commit/873ab411b796a69b0aae223600ef862961391fe7)
#### Friday 2023-02-17 11:40:58 by Marko Grdinić

"https://re-library.com/translations/heros-daughter/volume-13/chapter-621-the-heros-new-beginning/

///

“Heere, I made a sex change potion!”
“Fina?!”

///

Kek. Based.

2/11/2023

9:30am. I am up. Any mail? Nothing.

https://angel.co/jobs/applications

So far, all the jobs I have applied 3 weeks ago on AngelList have been rejected.

Sigh, let's just go forward. It is impossible to live honestly in this world it seems. But I knew that. I guess, the way I set up my resume, I must have been hoping for an entry level position. But those are very rare. So what I will do is really learn web development, and then put whatever it takes to get me that job once I am ready.

I'll learn the popular libraries in the .NET stack. And I will become a master concurrent programmer.

9:35am. I wonder if the Valora thread is dead as well? It would be great if it was not, but luck is not on my side.

It is pretty sad. Everything is trying to discourage me. I cannot do what I want. I have to experience this profound loneliness.

Before the AI apocalyspe inevitably starts, I'll at least make it so that I clear a single assignment and get paid. I should be competent enough for at least that.

Now, let me make a video on how to use the Elmish.Debugger.

https://mangakakalot.com/manga/bloomed_in_action

I'll leave this for later.

10am. Huh, this is confusing. I managed to use it yesterday. Where the hell is the time travel thing?

https://pixabay.com/music/beats-abstract-style-121455/

https://youtu.be/82oL1yuh96c
Getting Weird Websocket Error Messages In The Browser Console? Learn How To Use The Elmish Debugger

Here it is.

Now I need the Vite video.

But I do not know how to cover everything that I want yet, so let play a little. I need to see...

12:10pm. My god, why does it take so long to copy a folder with a lot of files in Total Commander. Maybe I should try a newer version of it?

```
PS E:\Webdev\Fable\test\safe-template-full-tutorial> npm run start

> start
> vite

▲ [WARNING] "import.meta" is not available with the "cjs" output format and will be empty [empty-import-meta]

    vite.config.js:4:12:
      4 │ console.log(import.meta.env.test);
        ╵             ~~~~~~~~~~~

  You need to set the output format to "esm" for "import.meta" to work correctly.
```

I just want to see if the env variables get set correctly.

```
file:///E:/Webdev/Fable/test/safe-template-full-tutorial/node_modules/vite/dist/node/cli.js:443
          throw new CACError(`Unknown option \`${name.length > 1 ? `--${name}` : `-${name}`}\``);
                ^

CACError: Unknown option `--env`
    at Command.checkUnknownOptions (file:///E:/Webdev/Fable/test/safe-template-full-tutorial/node_modules/vite/dist/node/cli.js:443:17)
    at CAC.runMatchedCommand (file:///E:/Webdev/Fable/test/safe-template-full-tutorial/node_modules/vite/dist/node/cli.js:641:13)
    at CAC.parse (file:///E:/Webdev/Fable/test/safe-template-full-tutorial/node_modules/vite/dist/node/cli.js:580:12)
    at file:///E:/Webdev/Fable/test/safe-template-full-tutorial/node_modules/vite/dist/node/cli.js:894:5
    at ModuleJob.run (node:internal/modules/esm/module_job:198:25)
    at async Promise.all (index 0)
    at async ESMLoader.import (node:internal/modules/esm/loader:385:24)
```

Hmmm...

https://vitejs.dev/guide/env-and-mode.html#modes

Maybe I could just change the mode?

Hmmm, instead of passing them from the command line, why don't I make the env files?

https://vitejs.dev/guide/env-and-mode.html#env-files

For some reason it is not really working.

https://stackoverflow.com/questions/67378099/import-meta-env-undefined-on-production-build-vitejs
> I just realized what the ViteJS documentation says and I'll leave it in case someone also suffers from this.

Ahhh, let me give this a try.

...I still get undefined!

> You don't have to use VITE_. You can use any prefix you like as long as you define it in the envPrefix option on the vite config.

https://www.youtube.com/results?search_query=vite

This is why Youtube vids are useful. Let me watch some of them.

12:35pm. I'll watch them after breakfast."

---
## [Vizavi/light-perfomance-testing-tool](https://github.com/Vizavi/light-perfomance-testing-tool)@[39fe1dc768...](https://github.com/Vizavi/light-perfomance-testing-tool/commit/39fe1dc76845b33715c905466341ac8f0cad6a1a)
#### Friday 2023-02-17 13:01:03 by Vizavi

Windows is suck for this dev project

fuck thi shit on win maching

---
## [RyuujiX/android_kernel_asus_sdm660](https://github.com/RyuujiX/android_kernel_asus_sdm660)@[8d3628e780...](https://github.com/RyuujiX/android_kernel_asus_sdm660/commit/8d3628e78074c936019a953a79f53082d4b72a4e)
#### Friday 2023-02-17 13:01:18 by Christian Brauner

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
Signed-off-by: RyuujiX <saputradenny712@gmail.com>

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[c68a159884...](https://github.com/odoo-dev/odoo/commit/c68a15988432b201ae3786eb54bac3110c4242f4)
#### Friday 2023-02-17 13:07:44 by Arnold Moyaux

[FIX] stock,purchase,mrp: accumulative security days

Usecase to reproduce:
- Set the warehouse as 3 steps receipt
- Put a security delay of 3 days for purchase
- Set a product with a vendor and 1 days as LT
- Replenish with the orderpoint

You expect to have a schedule date for tomorrow that contains all the
product needed in the incoming 4 days.

Currenly the internal transfer from QC -> Stock is for tomorrow (ok).
The transfer from Inpur -> QC is plan for 2 days in the past. (not ok)
The PO date is plan for 5 days in the past. (not ok)

It happens because the system check at each `stock.rule` application if
purchase is part of the route. If it's then it applies the security lead
time. It's a mistake because we should apply it only the first time.

To fix it we directly set it when the orderpoint run and not during
`stock.move` creation.
However for MTO it's not that easy. We don't want to deliver too
early the customer. So we keep applying the delay during the
`stock.move` creation but only when it goes under the warehouse stock
location.

X-original-commit: 97f52bd40d97109a7983549d252476959ddceada
Part-of: odoo/odoo#112325

---
## [Quacks-and-Kepteyn/Skyrat-tg](https://github.com/Quacks-and-Kepteyn/Skyrat-tg)@[5f9f60713b...](https://github.com/Quacks-and-Kepteyn/Skyrat-tg/commit/5f9f60713b7f79f548eb9d02baeec793c1e50243)
#### Friday 2023-02-17 14:42:00 by SkyratBot

[MIRROR] Starlight Polish (Space is blue!) [MDB IGNORE] (#19059)

* Starlight Polish (Space is blue!) (#72886)

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

* update modular

* Update _decal.dm

* Update _decal.dm

---------

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>
Co-authored-by: Zephyr <12817816+ZephyrTFA@users.noreply.github.com>
Co-authored-by: Tom <8881105+tf-4@users.noreply.github.com>
Co-authored-by: lessthanthree <83487515+lessthnthree@users.noreply.github.com>

---
## [NetBSD/pkgsrc](https://github.com/NetBSD/pkgsrc)@[e508349572...](https://github.com/NetBSD/pkgsrc/commit/e508349572730dfe0ce1bdde42a908e8bcfb1e55)
#### Friday 2023-02-17 14:55:13 by nikita

gotosocial: update to version 0.7.0

ChangeLog (taken from https://github.com/superseriousbusiness/gotosocial/releases/tag/v0.7.0)

v0.7.0 Stormy Sloth

Hello everyone! After much testing and prodding and poking, we're ready to release v0.7.0 Stormy Sloth into the world!

This is the umpteenth alpha release of GoToSocial (we stopped counting), and it brings a massive amount of new stuff, fixes, and tweaks.

Thank you for your continued support, and enjoy the release!
Release Highlights

    Basic video support (mp4 only). You can finally upload videos, and view videos from remote instances too. Not all mp4 files work, currently -- this is something we'll investigate for next release most likely.
    Support for federating reports in and out of GoToSocial, and viewing reports via the admin settings panel (this feature was sponsored by NLnet).
    Support for webp attachments, avatars, and headers.
    Users can now create, remove, and view status bookmarks!
    Domain blocks now apply on a wildcard basis, so you can block a second level domain (like example.org) and it will apply to subdomains too (like poop.example.org etc).
    HTTP request throttling -- only a certain number of http requests are served at a time now. This should vastly improve responsiveness under load on small instances.
    Much better logic for pruning old avatars + headers, leading to gb of disk space savings.
    So many bug fixes and performance improvements.

Migration notes
Upgrading

To upgrade to 0.7.0 from a previous release:
Binary/tar

    Stop GoToSocial
    Untar the new release, including the web assets and html templates.
    Edit your config.yaml file as necessary (see below).
    Start GoToSocial

Docker

    Stop GoToSocial.
    Pull the new docker container (superseriousbusiness/gotosocial:0.7.0 or superseriousbusiness/gotosocial:latest)
    Start GoToSocial.

config.yaml

The configuration file has changed since the previous release. We recommend copying the new file from example/config.yaml and pasting values into it from your previous config.yaml. You can see a diff of the config file here: v0.6.0...v0.7.0#diff-c071e03510b2c57e193a44503fd9528a785f0f411497cc75841a9f8d0b1ac622
Database migrations

This release contains several database migrations which will run the first time you start up this new version. Be sure not to interrupt this migration process. It will take anywhere between a couple seconds and a couple minutes. Please be patient.
Sqlite format changes

0.7.0 now uses SQLite's WAL journal mode by default. This means there will be some new SQLite related files in your GoToSocial directory:

    sqlite.db-shm
    sqlite.db-wal

When you do SQLite backups, you should back these files up too (you do have backups, right?).

If you use Postgres rather than SQLite, you can ignore this.
Updating from 0.7.0-rc2

0.7.0-rc2 was slightly broken. If you're getting lots of 'not found' errors for avatars and headers, after running 0.7.0-rc2, see here for steps to fix it: #1505

If you skipped over rc2, ignore this :)
Detailed Changelog
Features

    83b522a [feature/Frogend] basic report admin interface (#1424)
    a59dc85 [feature/frogend] (Mastodon) domain block CSV import (#1390)
    382512a [feature] Implement /api/v2/instance endpoint (#1409)
    3283900 [feature] Federate reports to remote instance as Flag (if desired) (#1386)
    08f8fea [feature/frontend] filterable local emoji list (#1385)
    17eecfb [feature] Public list of suspended domains (#1362)
    993aae5 [feature] Accept incoming federated Flag activity (#1382)
    faeb7de [feature] Implement reports admin API so admins can view + close reports (#1378)
    e974724 [feature] Implement /api/v1/reports endpoints on client API (#1330)
    73be244 [feature] Add RSS autodiscovery on profiles that enable RSS (#1373)
    acc333c [feature] Inherit resource limits from cgroups (#1336)
    627b8ee [feature] Tune sqlite pragmas (#1349)
    3512325 [feature] Add local user and post count to nodeinfo responses (#1325)
    d648793 [feature] Implement Report database model and utility functions (#1310)
    90a14ab [feature] HTTP request throttling middleware (#1297)
    1659f75 [feature] For video attachments, store + return fps, bitrate, duration (#1282)
    2bbc64b [feature] Enable basic video support (mp4 only) (#1274)
    d10388c [feature] support Sec-Websocket-Protocol in streaming API (#1254)
    69dd5fe [feature] domain block wildcarding (#1178)
    58c87bd [feature] allow uncaching of other media types (#1234)
    4b8d7bd [feature/frogend] Emoji copy "Steal this look" (#1222)
    cb2b2fd [feature] support configuring database caches (#1246)
    5e060d0 [feature] Start implementing refetch of lost media files via /api/v1/admin/media_refetch (#1221)
    477ae50 [feature] Allow users to create + delete bookbarks, and view bookmarked statuses (#1168)
    199b685 [feature] overhaul the oidc system (#961)
    1a3f26f [feature] media: add webp support (#1155)

Bugfixes

    b599309 [bugfix] Set 'discoverable' properly on API accounts (#1511)
    6ee0dc8 [bugfix] Set cache-control max-age dynamically for s3 (#1510)
    40b584c [bugfix] Fix 410 Gone race on account deletes (#1507)
    b8e1ab3 [bugfix] use woff(2) fonts for Noto Sans (#1509)
    6c6f042 [bugfix] Return empty result rather than 500 error when searching for blocked domains (#1498)
    561ad71 [bugfix] Fix up error getting account avatar/header errors, other small fixes (#1496)
    c223c75 [bugfix] Set appropriate cache-control when using presigned s3 links (#1480)
    e5e257c [bugfix] Fix error on searching for account w/accountDomain by host (#1465)
    52fbb3e [bugfix] fix 'steal this look' form, uncheck entries after processing (#1454)
    4e4da19 [bugfix] Use SignatureCheck middleware for web profile endpoints too (#1451)
    ad6ab03 [bugfix] don't trash emoji in profile fields on edit (#1440)
    ac2bdbb [bugfix] fix file range length calculation being off by 1 (#1448)
    6a6647d [bugfix] Ignore missing files when cleaning up media (#1435)
    75e1b9c [bugfix] fix old password hash staying in cache (#1432)
    80c26d6 [bugfix] Allow instance thumbnail description to be set separately from image (#1417)
    04ac3f8 [bugfix] Fix password change keys (#1416)
    abe9447 [bugfix] fix cache startup (#1414)
    271da01 [bugfix] Read Bookwyrm Articles more thoroughly (#1410)
    d4cddf4 [bugfix] Parse video metadata more accurately; allow Range in fileserver (#1342)
    132c738 [bugfix] Mount bookmarks endpoint correctly (#1338)
    1bda6a2 [bugfix] return early in websocket upgrade handler (#1315)
    2bf9bfa [bugfix] fix panic during status delete loop by breaking out early on len(statuses) == 0 (#1317)
    de74cc6 [bugfix/frogend] replace ch units to prevent layout shift on page load (#1301)
    eabb906 [bugfix] fix media create error not being checked (#1283)
    6ebdc30 [bugfix] Close reader gracefully when streaming recache of remote media to fileserver api caller (#1281)
    2b0342b [bugfix] use match-sorter for filtering domain blocks (#1270)
    1d24c1c [bugfix] Use null for empty api status language (#1268)
    8703933 [bugfix] fix unordered favorites (#1245)
    04636a3 [bugfix] attach bookmarks module to api (#1238)
    199672e [bugfix] fix unordered favorites (#1236)

Performance

    acc9592 [performance] processing media and scheduled jobs improvements (#1482)
    40bc03e [chore/performance] Update media prune logic, add extra CLI command (#1474)
    70739d3 [performance] remove throttling timers (#1466)
    95715f9 [performance] Don't fetch avatar + header if uri hasn't changed (#1463)
    02767bf [performance] remove local copying of file for satisfying range headers (#1421)
    5318054 [performance] media processing improvements (#1288)

Chores

    4cba90c [chore] Split the bug template in two (#1500)
    700ed77 [chore] Webkit frontend fixes (#1492)
    041c8e6 [chore] Do cache-control in a less silly way to avoid writing header twice (#1481)
    efbc5da [chore]: Bump github.com/minio/minio-go/v7 from 7.0.47 to 7.0.48 (#1486)
    33b77b3 [chore]: Bump golang.org/x/image from 0.3.0 to 0.4.0 (#1485)
    7231752 [chore]: Bump modernc.org/sqlite from 1.20.3 to 1.20.4 (#1484)
    6ac1dda [chore] small changes missed in previous dereferencer.GetAccount() PRs (#1467)
    65b1941 [chore] Fix report username wrapping (#1464)
    27e95fd [chore/bugfix] Serve + throttle publickey separately from rest of ActivityPub API (#1461)
    0ed50c1 [chore/frogend] domain blocklist layout on smaller screens (#1436)
    b63b1b6 [chore] Update bug report template (#1437)
    47daddc [chore/frogend] Restructure form data default values / update from Query data (#1422)
    0a98743 [chore]: Bump codeberg.org/gruf/go-runners from 1.4.0 to 1.5.1 (#1428)
    1df25a3 [chore]: Bump github.com/yuin/goldmark from 1.5.3 to 1.5.4 (#1427)
    dae14cc [chore]: Bump github.com/ulule/limiter/v3 from 3.10.0 to 3.11.0 (#1429)
    7f32457 [chore] stub /api/v1/featured_tags endpoint (#1420)
    33aee1b [chore] reformat GetAccount() functionality, support updating accounts based on last_fetch (#1411)
    49beb17 [chore] Text formatting overhaul (#1406)
    4ee4cd2 [chore/performance] use only 1 sqlite db connection regardless of multiplier (#1408)
    b80be48 [chore] Use 'immediate' lock for sqlite transactions (#1404)
    eccb380 [chore] Silence maxprocs logging (#1402)
    356e238 [chore]: Bump github.com/go-playground/validator/v10 (#1400)
    7bcdf35 [chore]: Bump github.com/microcosm-cc/bluemonday from 1.0.21 to 1.0.22 (#1399)
    782169d [chore] set max open / idle conns + conn max lifetime for both postgres and sqlite (#1369)
    27d4e36 [chore] Settings refactor fix4 (#1383)
    36f62d6 [chore] remove funky duplicate attachment in testrig (#1379)
    605dfca [chore] bump go version to 1.19.5 (#1377)
    98a09b5 [chore]: Bump github.com/spf13/viper from 1.14.0 to 1.15.0 (#1375)
    3e4dc6b [chore]: Bump github.com/abema/go-mp4 from 0.9.0 to 0.10.0 (#1374)
    13ec15d [chore] extending maximumPasswordLength to 256 (#1372)
    0ceacd7 [chore] bump db dependencies (#1366)
    b375d3b [chore] Add name to instance field for autosuggestion (#1359)
    747683b [chore] Settings refactor fix 2 (#1357)
    13e3aaa [chore] Fix new emoji preview title/alt text (#1354)
    9b139b6 [chore/frogend] Settings refactor (#1318)
    974ec80 [chore] Change default sqlite busy timeout to 5m (#1352)
    a6c6bdb [chore]: Bump codeberg.org/gruf/go-errors/v2 from 2.0.2 to 2.1.1 (#1346)
    fe3e9ed [chore]: Bump github.com/minio/minio-go/v7 from 7.0.44 to 7.0.47 (#1348)
    2a46980 [chore]: Bump golang.org/x/oauth2 from 0.3.0 to 0.4.0 (#1347)
    eafd73c [chore] Remove omitempty on account source; refactor tests to use prettyprint json (#1337)
    36aa685 [chore] Bump json5 from 1.0.1 to 1.0.2 in /web/source (#1308)
    ac562fa [chore]: Bump github.com/coreos/go-oidc/v3 from 3.4.0 to 3.5.0 (#1322)
    0ca6a9d [chore]: Bump golang.org/x/image from 0.2.0 to 0.3.0 (#1320)
    86ae0b1 [chore]: Bump golang.org/x/text from 0.5.0 to 0.6.0 (#1321)
    345b765 [chore]: Bump golang.org/x/net from 0.4.0 to 0.5.0 (#1319)
    6791920 [chore/frogend] update status blockquote css (#1302)
    adbc877 [chore] pull in latest go-cache, go-runners versions (#1306)
    0dbe6c5 [chore] Update/add license headers for 2023 (#1304)
    ff46dd4 [chore] Fix emoji notnull constraint on initial gtsmodel (#1303)
    71dfea7 [chore] shuffle middleware to split rate limitting into client/s2s/fileserver, share gzip middleware globally (#1290)
    941893a [chore] The Big Middleware and API Refactor (tm) (#1250)
    560ff12 [chore]: Bump github.com/abema/go-mp4 from 0.8.0 to 0.9.0 (#1287)
    b966d3b [chore]: Bump github.com/gin-gonic/gin from 1.8.1 to 1.8.2 (#1286)
    abd594b [chore]: Bump codeberg.org/gruf/go-bytesize from 1.0.0 to 1.0.2 (#1285)
    0871f5d [chore] note broken go v1.19.4 in contributing.md (#1278)
    0f38e7c [chore] fix some little config whoopsies (#1272)
    da751c0 update go-cache to v3.2.0 with support for ignoring errors (#1273)
    eb08529 [chore/bugfix] Switch markdown from blackfriday to goldmark (#1267)
    0f8d938 [chore] Add svg version of sloth logo as logo.svg (#1265)
    a7e71d7 [chore]: Bump golang.org/x/image from 0.1.0 to 0.2.0 (#1252)
    24b4f9b [chore] make single pull request template (#1239)
    e58d2d8 [chore] move caches to a separate State{} structure (#1078)
    dd1a4cd [chore] Remove deprecated linters (#1228)

Documentation

    674646b [docs] Update config.yaml (#1499)
    f3eb28a [docs] Suggest confirming host option in config (#1502)
    fd62847 [docs] Fix nginx fileserver caching example (#1506)
    76d1b48 [docs] move federating with gotosocial documentation into single file (#1494)
    eeca198 [docs] Update user/admin settings docs (#1491)
    dc766f9 [docs] Add an example on how to setup redirect with Traefik (#1395)
    43cbe3b [docs] Simplify Apache httpd proxy documentation (#1396)
    c59ec6f [docs] Add Flag documentation to federation docs (#1393)
    1fa574f [docs] Tidy up federation docs into 'federating with gotosocial' section (#1392)
    8d18888 [chore/docs] add instance-expose-suspended-web to instance docs (#1391)
    6b15b83 [docs] Remove videos from the list of missing features in the FAQ. (#1344)
    98edd75 [docs] Rewrite sponsorship + funding section, add NLnet (#1305)
    9859a43 [docs] Add s3 ssl variable to storage docs (#1294)
    2a1205a [docs] AWS S3 config details added (#1300)
    0b8eafe [docs] Fix documentation edit link (#1298)
    9ecb1c8 [docs] Add troubleshooting section for Apache (#1291)
    bae7398 [docs] Update Apache docs to use 127.0.0.1 instead of localhost (#1266)
    418bfbf [docs] Update nginx docs to use 127.0.0.1 instead of localhost (#1264)
    ce615b5 [docs] Serve static assets with nginx (#1251)
    d2a09c1 [docs] Caching webfinger with nginx (#1242)
    610c270 [docs] Update CONTRIBUTING.md, add pull request templates (#1216)
    aea16bb [docs] Update README.md (#1126)
    923d333 [docs] encourage using loopback bind address (#1166)

---
## [RevenueCat/purchases-android](https://github.com/RevenueCat/purchases-android)@[dfd2a22eac...](https://github.com/RevenueCat/purchases-android/commit/dfd2a22eac045e295c4572e7aeab356f61aea5be)
#### Friday 2023-02-17 14:56:10 by Josh Holtz

[CF-1121] Update Magic Weather for BC5 / SDK V6 (#768)

<!-- Thank you for contributing to Purchases! Before pressing the
"Create Pull Request" button, please provide the following: -->

### Checklist
- [x] If applicable, unit tests
- [x] If applicable, create follow-up issues for `purchases-ios` and
hybrids

### Motivation

[CF-1121](https://revenuecats.atlassian.net/browse/CF-1121)

### Description

- Migrated from SDK `5.0.0` to `6.0.0-alpha.2`
- Changes to `PaywallAdapter` to make paywall show more useful
information to user
  - Duration (gross code)
  - Multiple offers (and "best offer" first)
  - Pricing phases (gross looking now but will improve later)
- Works for both subscriptions and one-time purchases

#### Step 1

The initial migration (with only necessary code changes to compile) made
for a very confusing paywall 👇

- The subscriptions relied on the product title (which is the same for
each base plan)
- Did not include the duration so user had no idea what they were buying
- This is because these were previously in the individual subscription
titles for BC4
- It did use the default/best offer which was nice but didn't explain
any offer info

<img width="473" alt="Screen Shot 2023-01-30 at 8 23 51 AM (1)"
src="https://user-images.githubusercontent.com/401294/216314716-eb584d1c-d943-4dd1-9c03-2dd6436bb3e4.png">

#### Step 2

Big rework to programmatically show as much info as we could (even
though it is kind of ugly UI right now) 👇

- Shows all the options for each subscription with "best offer" on top
- This might be overkill because why not just choose the best offer but
wanted to show this as example 🤷‍♂️
- Shows the pricing phases that come with each option
- Needed very different logic for subscriptions vs one-time purchases
- This is because one-time purchases contain all the data in the
`StoreProduct`
- Where subscriptions contain all needed data in `SubscriptionOption`
and `PricingPhase`s


https://user-images.githubusercontent.com/401294/216314819-54f24dfa-48c4-4bd9-9d75-b89754015f92.mov




[CF-1121]:
https://revenuecats.atlassian.net/browse/CF-1121?atlOrigin=eyJpIjoiNWRkNTljNzYxNjVmNDY3MDlhMDU5Y2ZhYzA5YTRkZjUiLCJwIjoiZ2l0aHViLWNvbS1KU1cifQ

---
## [Bjarl/Shiptest](https://github.com/Bjarl/Shiptest)@[84a2a8f394...](https://github.com/Bjarl/Shiptest/commit/84a2a8f394a0296ecc527f23c0da470b30280c0c)
#### Friday 2023-02-17 15:04:22 by Bjarl

Die Of Fate Change (#1760)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
replaces the die of fate's d20 effect (spawn you as wizard) with spawn
wizard clothes and magic mirror under you.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
I'm sick of wizards spawning without admin intervention
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
balance: You can't be turned into a wizard by the die of fate, instead
getting a magic mirror and wizard clothes.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [HoleDroid/android_kernel_asus_sdm660](https://github.com/HoleDroid/android_kernel_asus_sdm660)@[8daec42b1d...](https://github.com/HoleDroid/android_kernel_asus_sdm660/commit/8daec42b1d2a2c13638653780e797a571bca8c47)
#### Friday 2023-02-17 15:16:47 by Dave Chiluk

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
Change-Id: If57838f807fc086da8cd6c3cac964b1be9a9889b
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

---
## [iamnotacake/themis](https://github.com/iamnotacake/themis)@[eac726f812...](https://github.com/iamnotacake/themis/commit/eac726f8121a68caa53bf7147bca81f29679ddba)
#### Friday 2023-02-17 15:19:19 by Oleksii Lozovskyi

CI: Remove Carthage distractions (#990)

Carthage has this retarded tendency to build every Xcode project it
sees when building dependencies. So when we do "carthage bootstrap"
during example builds, it downloads dependencies (Themis repo),
then proceeds to build the dependencies -- but instead of building
only Themis.xcodeproj in the root, Carthage decides that after that
it gotta build every other Xcode project there as well, why not.
Eventually it times out and dies.

This very frustrating, but Carthage people think this is fine,
multilanguage monorepos do not exist, and you should not put example
Xcode projects along with the source code. One repo = One library.

Anyway. This seems to help to avoid timeouts and prevent Carthage
from going on adventure. Sadly, builds still take fucking forever
while Carthage fetches the repo, then fetches OpenSSL binaries,
then do it again, then build Themis, then build example, then
repeat that 5 more times for other examples. But at least they
should not hang for 10 minutes and then die 🤞

Similar hack is applied in Bitrise builds, IIRC.

---
## [jhanu656/Fundamentals](https://github.com/jhanu656/Fundamentals)@[9662b3f0e9...](https://github.com/jhanu656/Fundamentals/commit/9662b3f0e9430facd1b3d73c882c9a59f30629b5)
#### Friday 2023-02-17 15:21:24 by Jhansi

Basics

Four kids Peter,Susan,Edmond and Lucy travel through a wardrobe to the land of Narnia. Narnia is a fantasy world of magic with mythical beasts and talking animals.While exploring the land of narnia Lucy found Mr.Tumnus the two legged stag ,and she followed it, down a narrow path .She and Mr.Tumnus became friends and he offered a cup of coffee to Lucy in his small hut.It was time for Lucy to return to her family and so she bid good bye to Mr.Tumnus and while leaving Mr.Tumnus told that it is quite difficult to find the route back as it was already dark.He told her to see the trees while returning back and said that the first tree with two digits number will help her find the way and the way to go back to her home is the sum of digits of the tree and that numbered way will lead her to the tree next to the wardrobe where she can find the others.Lucy was already confused, so pls help her in finding the route to her home.... 

Input Format:
Input consists of an integer corresponding to the 2-digit number.
Output Format:
Output consists of an integer corresponding to the sum of its digits.

Sample Input
23

Sample Output
5

---
## [spockye/Shiptest](https://github.com/spockye/Shiptest)@[0d19f3c85d...](https://github.com/spockye/Shiptest/commit/0d19f3c85d39f58ee663935eb75b72fd502752af)
#### Friday 2023-02-17 15:35:03 by Bjarl

Patches the Bombed Starport To Be Less Bad (#1754)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

![image](https://user-images.githubusercontent.com/94164348/217633782-c0dca540-0915-4acf-99f7-1031ea47f5ec.png)

![dreamseeker_vlOQGOERgI](https://user-images.githubusercontent.com/94164348/217633806-269717de-78fb-4fc2-8ab6-a7ee7a1c3b6e.png)

![dreamseeker_pP6WKD1PQT](https://user-images.githubusercontent.com/94164348/217633810-87471403-d8ad-4e46-bd3f-7a49c5eaad5d.png)
Puts some funny signs I painted over around, fixes the lighting, and
does a small pipe fix
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
I watched like 4 people walk into this ruin completely unaware that it
was horrifically radioactive and that was just kinda not fun.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
fix: Bombed Starport lighting now works properly
imageadd: fokrads sign
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
Co-authored-by: Zephyr <12817816+ZephyrTFA@users.noreply.github.com>

---
## [shiptest-ss13/Shiptest](https://github.com/shiptest-ss13/Shiptest)@[b03e7eb81c...](https://github.com/shiptest-ss13/Shiptest/commit/b03e7eb81c0676e69aeb7c2ee962b243e7aa5988)
#### Friday 2023-02-17 15:52:54 by spockye

beach ruin, The Treasure Cove! (#1701)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
This PR adds a new Beach ruin, Treasure Cove. 

![2023 01 17-11 26
30](https://user-images.githubusercontent.com/79304582/212874736-b17917a5-876e-4a7a-a073-1581cc394b8e.png)

![2023 01 17-11 26
58](https://user-images.githubusercontent.com/79304582/212874824-9a161419-b751-41d2-a82d-e50f06981025.png)


![image](https://user-images.githubusercontent.com/79304582/212879021-bcdc2238-b50b-48c2-9cd0-d17cccbd50dc.png)

Loot: 
cm-16 rifle (main loot)
energy gun
pirate sabre
frontiersmen hardsuit
misc combat supplies
secret documents
2x abandoned crates
research note / tesla researcher
basic engineering supplies (smes/tools/autolathe/battery charger)
two boats
silver crate / hidden gold crate
misc junk
______
Threat: 
1x spacesuit ranged pirate
2x sword pirates
1x ranged pirate
punji sticks
_____

Lore tidbit:
This "humble abode" is the home of our 5- now 4 Pirate friends! After a
mildly successful raid on a CMM VIP transport, they managed to take a
Cargo tech (the VIP), and a CMM guard as hostage. sadly it didn't all go
as planned, and the CMM officer managed to free himself and killed one
of the pirates. This is where you now find the cave, with both hostages
executed, their brother buried, and the pirates grieving his unfortunate
passing.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

<!-- Tick the box below (put an X instead of a space between the
brackets) if you have tested your changes and this is ready for review.
Leave unticked if you have yet to test your changes and this is not
ready for review. -->

- [x] I affirm that I have tested all of my proposed changes and that
any issues found during tested have been addressed.

## Why It's Good For The Game
more ruins = good.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: Adds a new beach ruin, the beach_treasure_cove
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Signed-off-by: Bjarl <94164348+Bjarl@users.noreply.github.com>
Co-authored-by: Bjarl <94164348+Bjarl@users.noreply.github.com>

---
## [Chezloc/World-War-Bruh-PMFU](https://github.com/Chezloc/World-War-Bruh-PMFU)@[0e8c7a42c6...](https://github.com/Chezloc/World-War-Bruh-PMFU/commit/0e8c7a42c65d02442b0cdda53472bf537bb44c68)
#### Friday 2023-02-17 16:43:11 by Caitlin

BBA v1.3.14 (Part 2)

- Added a number of new tank models for Brazil, mexico, and mongolia
- Cruisers can no longer use secondaries in the non dedicated Secondaries slot
- Small Gun hit profile 55 -> 60
- Ship Light Medium Battery 1/2/3/4 damage changed from 6/10/14/18 to 4/8/12/16
- Cruiser Engine 1/2/3/4 Speed multiplier changed from .20/.3/.35/.40 to .20/.25/.30/.35
- Light Cruiser Gun speed penalty debuff for guns 2/3/4 changed from -.04/-.05/-.06 to -.05/-.06/-.07
- Starting Mongolian Convoys increased from 50 to 100
- Mongolian Rubber Refinery focus fixed
- New Text added to Research Tab backgrounds thanks to Chezloc
- The localization has been refactored, so submods may have some broken localization
- Fixed a number of console errors

Japan:
- The spirit for the Pacific war that debuffs the allies has been shifted from getting a malice to atttack and defense against EU Axis, to an attack malice against EU axis, and the EU axis getting an attack bonus. This is because of funny paradox math making using defense_bonus_against doesn't really work right
- Japan has been given 3 new paths post China War, and they must do one of them
- Short War lets you go to war in July of 1940, but with some minor debuffs that mean you will need to be aggressive and conquering to take advantage
- Medium War lets you go to war in January of 1941 and is expected to be the default. Japan gets some buffs to help them build up for longer, including industry, military, and intel
- Long war lets you go to war in July of 1941, where Japan gets large industry buffs, military buffs, intel buffs, and some bonus destruction and collaboration

---
## [GisleGaren/NetworkPythonProgramming](https://github.com/GisleGaren/NetworkPythonProgramming)@[e07035f658...](https://github.com/GisleGaren/NetworkPythonProgramming/commit/e07035f658bde97c21eac19753911d32b4edb25d)
#### Friday 2023-02-17 16:43:20 by GisleGaren

Eline has tested the code because I can't run it on windows because of some bullshit reason. My virtualbox keeps crashing and I need to continuously restart the fucking thing. Fuck this lab-2 assignment I want to die

---
## [clayne/wrye-bash](https://github.com/clayne/wrye-bash)@[d1290a53e9...](https://github.com/clayne/wrye-bash/commit/d1290a53e9dc7ad557bd91378a32256a6455b094)
#### Friday 2023-02-17 17:46:53 by Infernio

Merge branch 'inf-190-bye-listboxes-pt1' into dev

And important merge that begins tackling one of WB's uglies GUI warts:
balt.ListBoxes. Not only is the code a mess (just look at
ListBoxes.__init__ for a taste), but the class can also do three
separate styles of behavior (several ListBox instances, several
CheckListBox instances or a TreeCtrl) and to top it all off, the
TreeCtrl version changes the input format of one of the parameters to
suddently be a dict instead of a list.

Additionally, from an end-user perspective, ListBoxes are just plain
ugly and nigh-on unusable. They're never sized right, they usually don't
wrap right when you resize them, and even if you do put in the effort
and get one resized to look nice, it doesn't even remember that and will
just start with a weird, probably-too-big automatic size anyways.

All around, not a good time. This branch first solves the wrapping
problem once and for all by introducing gui.WrappingLabel, which
automatically word-wraps when the GUI is resized. You still have to do
some work to initially wrap it properly when the GUI is created (see
settings_dialog.py for a particularly painful case), but it's actually
possible to get a responsive label in the GUI with this.

Next up, the branch replaces the ListBoxes popup used when an item is
deleted with a custom popup. This popup also enables us to drop some
internal complications and unify the deletion logic for all the tabs. We
even get a nice way to decide visually if you want to recycle or
permanently delete items.

Next were the Sync From Data, Clean Data and Monitor External
Installation popups. I created a new class, AMultiListEditor, that
fulfills the same purpose as the CheckListBox flavor of ListBoxes, but
with much better UX. For example, you can search with this one. There
are buttons for mass selecting and unselecting (rather than it being an
obscure right-click command). Wrapping works. And best of all, it
remembers when you resize it!

Finally, a small interlude commit enables an ancient option that has
sat, commented out, in WB's codebase since at least the 271 days. On the
Installers tab, you can now sort simple packages before complex ones. I
also renamed the relevant Sort By options for more consistency and
clarity (the rest of this work is on nightly).

Merging this now because nightly is already really big and I don't want
to resolve more conflicts. I tested it pretty thoroughly and everything
works great.

Under #190

---
## [clayne/wrye-bash](https://github.com/clayne/wrye-bash)@[55c39d4573...](https://github.com/clayne/wrye-bash/commit/55c39d45734a59dc3fb734adbbe36f7995648af2)
#### Friday 2023-02-17 17:46:53 by Infernio

Fix the whole 'auto-wrapping text' mess

I've finally figured it out. Took literally hours of fiddling around
with AutoWrapStaticText to work around a really weird bug, then more
hours to figure out how to get the settings dialog to wrap nicely when
it's opened, but it's done. It's wonderful. I never want to touch it
again.

Utumno:
We must link to the commit here - just a fixup (kept separate in case
there is a shorter url - certainly needs to wrap better :P)

I am really curious to learn what the 'really weird bug" was - I
remember wrapping being a pain so I'd like to know what made the
difference finally - is it just the `dc = wx.ClientDC(self)` (?)

You mean wx.AutoWrapStaticText and it _is_ wonderful

Edit: added a wx (Pep8) suffix to wx functions/overrides - makes it
much easier to figure out on first read (plus if we ever want to swap
gui libs this would be done by a metaclass reading off the correctly
suffixed method)

---
## [toolmind/cmss13](https://github.com/toolmind/cmss13)@[7731fa738f...](https://github.com/toolmind/cmss13/commit/7731fa738f01b0c83dce6183a3e58387984926bf)
#### Friday 2023-02-17 17:51:19 by naut

A small assortment of more fortunes (#2643)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

> _"When you look through rose-colored glasses, all the red flags just
look like flags."_

Adding to the fortune cookie poll once again with some nice
inspirational quotes and bits to help someone's mood. Contains an
assortment of movie/TV quotes, inspirational words, and quotes from real
people. Yes, real people.

Also alphabetizes the fortunes.txt file to make everything more tidy.
Unfortunately this also demolishes the diff file, so the new fortunes
are provided below instead.

# Explain why it's good for the game

A little more motivation never hurt anyone, eh?
Change comes from embracing the future, not fighting your past.

# New Fortunes

<details>
<summary>Click to expand</summary>

```
A broken vase is more interesting than a perfect one.
A bruise is a lesson, and each lesson makes us better.
After all, tomorrow is another day.
All we have to decide is what to do with the time that is given to us.
Be the reason someone thinks life is worth living.
Be the reason someone wants to wake up in the morning.
Change comes from embracing the future, not fighting your past.
Do the thing that scares you the most.
Don't let anyone ever make you feel like you don't deserve what you want.
Embrace a new narrative.
Enter unknown territory.
Every day, in every way, you are getting better and better.
Every new beginning comes from some other beginning's end.
Everything always goes wrong. You just have to deal with it.
Everything you do is your life's work.
Evolve as a human.
Expect great things of yourself before you do them.
Follow your heart and see what turns up.
Fortune and glory.
Generosity is its own form of power.
Get busy living or get busy dying.
Get lost in the right direction.
Get out of your comfort zone. It's not even that comfortable.
Good instincts are worthless if you don't follow them.
Good news: the light at the end of the tunnel is not a train.
Great men are not born great, they grow great.
Happiness is not something ready made. It comes from your own actions.
I never dreamed about success. I worked for it.
If we wait until we're ready, we'll be waiting for the rest of our lives.
Imperfections are beautiful.
It's not our abilities that show what we truly are. It's our choices.
It's what you do right now that makes a difference.
Live in the constant unexpected.
Look how far you've come.
Love doesn't have to be a person. It can be a passion.
Love yourself, conquer your fears!
Loving yourself isn't vanity; it's sanity.
Make someone laugh today.
Make someone smile today.
Mind over matter.
Never be cruel, never be cowardly. And never ever eat pears.
Never forget who you are. The rest of the world will not. Wear it like armor and it can never be used to hurt you.
Never let anyone tell you what you can't do.
No man is good enough to govern another man without that other’s consent.
Normal is nothing more than a cycle on a washing machine.
Nothing can dim the light that shines from within.
Oh yes, the past can hurt. But you can either run from it, or learn from it.
One day you’ll look back at right now and say, 'If I got through that, I can get through anything.' And that will truly be a gift.
Recognize yourself in others.
Some people can't believe in themselves until someone else believes in them first.
Surviving is the least we can do.
The present is just one chapter of your own novel.
The weirdest people happen to be the most successful.
Turn wounds into wisdom.
We all make choices, but in the end, choices make us.
What people call you weird for is in fact your greatest strength.
While there's life, there's hope.
Why are you trying so hard to fit in when you were born to stand out?
Worrying means you suffer twice.
You are your best thing.
You attract what you are ready for.
You can discover a whole new world by just adjusting how you see everything.
You cannot live your life to please others. The choice must be yours.
You don’t lead by pointing and telling people some place to go. You lead by going to that place and making a case.
You make your own luck.
You'll never meet someone who isn't important.
You're never alone in your struggles.
```

</details>

Some of my favorites:

> Why are you trying so hard to fit in when you were born to stand out?
> Never let anyone tell you what you can't do.
> You don’t lead by pointing and telling people some place to go. You
lead by going to that place and making a case.
> Good instincts are worthless if you don't follow them.

# Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->
<!-- If you add a name after the ':cl', that name will be used in the
changelog. You must add your CKEY after the CL if your GitHub name
doesn't match. Be sure to properly mark your PRs to prevent unnecessary
GBP loss. Maintainers freely reserve the right to remove and add tags
should they deem it appropriate. -->

:cl:
add: Added several new fortunes to fortune cookies.
code: Alphabetized the fortunes.txt file for fortune cookie blurbs.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [toolmind/cmss13](https://github.com/toolmind/cmss13)@[4c373316ad...](https://github.com/toolmind/cmss13/commit/4c373316ad1e9a68e5cd7ae0e216bddcd52ee3aa)
#### Friday 2023-02-17 17:51:19 by NewyearnewmeUwu

Alerts admins whenever humans try to gib another human. (#2560)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request
Successor to #2237 that properly addresses the issues brought up by
myself and others. This sends a admin alert similar to when a pred
activates their SD that allows admins to jump to the (strictly human)
player gibbing another human/human corpse and sleep them/amessage them.
This also creates logs when someone _attempts_ to stuff someone into a
gibber. I also fixed up some of the single letter variables in the
gibber code.
<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

Insanity RP is bad, and this solution allows admins to respond in
realtime. It takes 30 seconds to gib another human as a human, without
any skill modifiers helping. It also doesn't flag the player if they're
a pred, as they're _supposed_ to be doing funny human meat stuff.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->


# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->
<!-- If you add a name after the ':cl', that name will be used in the
changelog. You must add your CKEY after the CL if your GitHub name
doesn't match. Be sure to properly mark your PRs to prevent unnecessary
GBP loss. Maintainers freely reserve the right to remove and add tags
should they deem it appropriate. -->

:cl:
code: gibbing another human takes an unmodifiable 30 seconds
admin: admins are alerted when a human tries to gib another human
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [sourcegraph/sourcegraph](https://github.com/sourcegraph/sourcegraph)@[dd1e512434...](https://github.com/sourcegraph/sourcegraph/commit/dd1e512434655210cb62b231dadf76efecc53a50)
#### Friday 2023-02-17 18:00:44 by coury-clark

release-tool: refactor release config (#47711)

Closes [#47557](https://github.com/sourcegraph/sourcegraph/issues/47557)

This is a somewhat gruesome PR to read, so sorry for that. I wanted to
keep this change atomic so it's easy to revert if we need.

So, I set out to automate the dates in the release config and realized
that fundamentally the architecture of the release tool was coupled to
this config in a way that was making life more difficult than it needed
to be.

This PR refactors the release config in the release tool. It uses an
entirely new schema, and for the most part automates every interaction
anyone will have with the config. The new schema is designed to do a few
things:
1. Deprecate the annoying cached version by specifying two sections of
the release config, both a definition and an active releases field.
Anything in the active releases is considered in progress.
2. Sets up some architecture to support multi-release functionality from
the release tool. There are guard rails right now since this isn't fully
supported.

Also,
* Automatically detect and suggest versions
* Automatically generate release dates from a specified date or current
time
* QOL changes to flow to the appropriate commands if the release config
is in the wrong state. For example it will prompt for input if the
config is empty for a given version for commands that require a valid
state
* Guardrails around every interaction I could find that causes problems
* New commands to interact with the release config (activate-release,
deactivate-release, util:previous-version)

## Usage

To set a release as active, either use the activate command directly
```
pnpm run release release:activate-release
```
or transitively through another dependent command.

All release commands that interact with the _current_ release will read
from the active release in the release config.
All release commands that interact with _future_ releases will read and
write to the release definitions in the release config.

To deactivate the release:
```
pnpm run release release:deactivate-release
```

Most of these steps are not explicitly mandatory, and are coupled into
other relevant commands (for example closing the release will deactivate
the release also).

To add new scheduled release definitions:
```
pnpm run release release:prepare
```

To remove scheduled releases:
```
pnpm run release release:remove
```

To determine previous versions:
```
pnpm run release util:previous-version 4.2.1
Getting previous version from: 4.2.1...
4.2.0
```

or

```
pnpm run release util:previous-version
Getting previous version...
4.4.2
```


## Test plan

I did a lot of manual testing since so many commands were impacted. Some
example output is below, and here is an example of a fake issue that was
generated from the release tool:
https://github.com/sourcegraph/sourcegraph/issues/47760

Example of how the input will flow if the config is not in the correct
state, including version suggestions:
```
> @sourcegraph/dev-release@0.0.1 release /Users/coury@sourcegraph.com/Documents/code/sourcegraph/dev/release
> ts-node --transpile-only ./src/main.ts "release:status"

No active releases are defined! Attempting to activate...
Next minor release: 4.5.0
Next patch release: 4.4.3
Enter the version to activate: 
```

```
> @sourcegraph/dev-release@0.0.1 release /Users/coury@sourcegraph.com/Documents/code/sourcegraph/dev/release
> ts-node --transpile-only ./src/main.ts "release:status"

No active releases are defined! Attempting to activate...
Next minor release: 4.5.0
Next patch release: 4.4.3
Enter the version to activate: 4.4.3
Attempting to detect previous version...
Detected previous version: 4.4.2
Release definition not found for: 4.4.3, enter release information.

Enter the release date (YYYY-MM-DD). Enter blank to use current date: 
Using current time: 2023-02-16T11:01:34.710-08:00
Enter the github username of the release captain: coury-clark
Enter the slack username of the release captain: coury
Version created:
{
  "codeFreezeDate": "2023-02-09T10:01:34.710-08:00",
  "securityApprovalDate": "2023-02-09T10:01:34.710-08:00",
  "releaseDate": "2023-02-16T10:01:34.710-08:00",
  "current": "4.4.3",
  "captainGitHubUsername": "coury-clark",
  "captainSlackUsername": "coury"
}
Release: 4.4.3 activated!
```


<!-- All pull requests REQUIRE a test plan:
https://docs.sourcegraph.com/dev/background-information/testing_principles
-->

## App preview:

-
[Web](https://sg-web-cclark-refactor-release-config.onrender.com/search)

Check out the [client app preview
documentation](https://docs.sourcegraph.com/dev/how-to/client_pr_previews)
to learn more.

---
## [isinyaaa/dotfiles](https://github.com/isinyaaa/dotfiles)@[fabe23997d...](https://github.com/isinyaaa/dotfiles/commit/fabe23997d967f8e27edc34df7a636ccc0e6eff7)
#### Friday 2023-02-17 18:23:34 by Isabella Basso

fuck treesitter

This is a shitty software project. I just want my standard colors to be
applied where they should, and the complexity of this thing + SEEMINGLY
RANDOM AND BIZARRE coloring are just not worth the trouble.

After spending some hours **debugging diff highlighting** I think I've
had enough of this insanity.

Signed-off-by: Isabella Basso <isabbasso@riseup.net>

---
## [PalJohnson/cmss13](https://github.com/PalJohnson/cmss13)@[c7a33d5ff9...](https://github.com/PalJohnson/cmss13/commit/c7a33d5ff9f4f7563145e82dd6cd0cd00f6b53c5)
#### Friday 2023-02-17 19:02:48 by riot

PMC and Whiteout stuff (#1966)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

As a preword, I came up with every change in this PR and coded them in
the span of 10 hours, so some things may be iffy.

PMCs and Whiteout may be good, but they're a bit outdated, this
modernizes multiple loadout aspects, enables antag vendors for
admin-spawn, and does some balance changes to certain
portions(specifically chem ERT).

Individual changes, numbered, will go over each in why its good, may
have forgotten one or two things.

1. Buffs whiteout flamer with blue flame damage, belt-linked magharn,
and pyro underbarrel extinguisher
2. Adds a synthetic repair kit(medkit), with synth repair tools, gives
it to whiteout.
3. Adds breaching charges and swaps crowbars to tactical in whiteout
loadouts
4. Gives whiteout PMC sniper goggles(thermals)
5. Gives whiteout medic the required gear to actually repair a downed
member of the team, and just a lot of synth heals.
6. Gives whiteout leader a pyro extinguisher.
7. Gives whiteout weapons default attachments.
8. Adds an 'advanced' mini-flamer with the same stats as UPP integrated
UBF, gives it to NSG23 and random m41/2 attachie.
9. Gives detainer PMCs a version of the corporate m41A MK2(goon gun),
with attachies and adv flamer to replace flamethrower.
10. Swaps chem PMC TL P90(name is too long) with an M41/2
11. Gives normal PMC ERT roles a webbing vest with meds and
miniextinguisher
12. Gives PMC Surgeon the essentials required to act as a medic, swaps
NSG with M39/2, gives them a normal but unique look.
13. Whiteout and PMC SG powerpacks have 30k power by default, instead of
10k.
14. Gives PMC guns more options for random attachments, and gives m41/2
its intended collapsible stock
15. Gives PMC engi m39/2 instead of P90
16. Removes flamer from potential PMC loadouts.
17. Gives PMCs better CQC skill.
18. Gives PMC TLs autoinjector pouches(which gives chem TL a second
pouch in the first place)
19. Detainer PMCs now have tac-sechuds, PMC TLs have sensorhuds.
20. **Enables antag vendor for PMC roles.** (Look at file changes for
the specific things, too long for pr desc)

# Explain why it's good for the game

Modernization and some needed loadout/balance changes(IMO).
Per number:

1. Whiteout flamer did worse damage than napalm, and was incredibly easy
to lose.
2. More heals for each member of the whiteout team, allows more
self-sufficiency.
3. Breach charges for tacticool breaches, crowbar doubles as a melee
weapon in case the player doesn't know about synth punch
4. Whiteout didn't have proper NVG, thermals allows them to do
tacticooler breaches by lining up people wth breach charge.
5. Whiteout medic didn't have a lot of heals at all, and didn't have a
defib, so they weren't much of a medic.
6. To extinguish the flames and lead charges, works like pyro
underbarrel extinguisher, but handheld.
7. Default tacticool attachment, already made whiteout subtypes for
HEAP, why not give them good attachies with them too.
8. Mini-flamer sucks, gives a better version for NSG and m41/2, same
stats as the already existing UPP integrated UBF.
9. Detainers had flamers which sucked, gives them corpo m41s which
aren't as good as /2s, but have adv UBF for flames.
10. P90 sucks, having default m41/2 fits with other leader type, also
gives them a better gun than their underlings.
11. Medkit but in a webbing, its my personal combat webbing load when I
play so its good.
12. PMC Surgeon was horrifically undergeared, they didn't even have a
medhud, gives them basic gear similar to PMC med but with a beret to
tell them apart.
13. ERTs don't have spare batteries to get usually, more staying power
in fights.
14. More options for attachies to further make PMC weapons better, also
gives m41/2 the m41 collapsible stock because it needed it.
15. P90 sucks, support roles getting the m39/2 is cool.
16. Flamer sucks to get as PMC, and adv. UBF as a potential m41/2
attachie makes a full-sized flamer useless too.
17. PMCs could fireman carry, and multi-strip, but did it horrifically
slow, gives them MP level CQC(master for spec, expert for TL)
18. TL getting extra meds is neat, also chem TL had an empty pocket slot
and no meds, thats bad.
19. Sechud-thing for PMC detainers is useful(stops flashbang trolling
for one), giving PMC TL a sensorhud to watch their team's status is also
good.
20. Makes doing event bases for PMCs much easier, too long to post the
specific changes here but look at files for them.


# Testing Photographs and Procedure

I forgot to take screenshots but it all works. 👍 
I spawned myself as every changed role and tested every individual
change extensively.

# Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->
<!-- If you add a name after the ':cl', that name will be used in the
changelog. You must add your CKEY after the CL if your GitHub name
doesn't match. Be sure to properly mark your PRs to prevent unnecessary
GBP loss. Maintainers freely reserve the right to remove and add tags
should they deem it appropriate. -->

:cl:
add: PMCs are now able to use antag vendors.
balance: Multiple loadout and skill changes to PMCs and Whiteout
balance: Buffs whiteout flame damage to blue flame damage.
fix: PMC Investigator Lead now appropriately spawns with a medical pouch
in their pocket, instead of nothing.
fix: Maximum skill preset now appropriately also has BE and intel skill,
at maximum of course.
fix: PMC Smartgunner now appropriately a VP78 to go along with their
VP78 magazines
fix: Whiteout now appropriately have night vision.
fix: M41A/2 now appropriately comes equipped with a collapsible stock.
spellcheck: PMC smartgun drum now has a seperate description and name
from base SG to match its different appearance.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [bluk/diesel](https://github.com/bluk/diesel)@[448df6b615...](https://github.com/bluk/diesel/commit/448df6b61566dbd419554fc82abd018357848846)
#### Friday 2023-02-17 19:08:07 by Georg Semmler

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
## [Fussmatte/VVVVVV](https://github.com/Fussmatte/VVVVVV)@[86d90a1296...](https://github.com/Fussmatte/VVVVVV/commit/86d90a1296739adef30b224f41e3a6ab55069a48)
#### Friday 2023-02-17 20:11:06 by Misa

Add color support to Windows console output, properly

This adds color support to the output of the console on Windows. Now if
you're using Windows 10 build 1511 or later (I think it's build 1511
anyway; they added more VT sequence support in later versions), you will
see colors by default. This isn't due to Windows helping in any way;
this commit has to specifically enable it with SetConsoleMode() because
by default, Windows won't enable color support unless we enable it. (Or
if it's enabled in the registry, but having to go through the registry
to enable basic shit like that is completely fucking stupid.)

I tested this in my Windows 10 virtual machine and it's completely
working.

---
## [sh3rp/azerothcore-wotlk](https://github.com/sh3rp/azerothcore-wotlk)@[ef949f9ff0...](https://github.com/sh3rp/azerothcore-wotlk/commit/ef949f9ff0a89e837c67258d7e199da1706bc438)
#### Friday 2023-02-17 20:59:05 by ICXCNIKA

fix(DB/Locale): deDE fix request items texts #02 (#14615)

Process of translation: only original sources of deDE texts by
researching multiple sources, reverse translation by searching for
related quest items/NPCs and using these names to reconstruct a proper
translation.

This fixes the terms

Coldtooth-Mine (Eisbeißermine), Doomhammer (Schicksalshammer), Fizzle
(Zischel), Fizzledowser (Rutenwünschels), Fizzlebub (Zischelbub),
Burning Blade (Brennende Klinge), Ashenvale (Eschental),
Bloodscalp/s/stamm (Blutskalpe, Blutskalpstamm),
Darkspeartrolle/Darkspears/Darkspearstamm (Dunkelspeere,
Dunkelspeertrolle, -stamm), Moonglade (Mondlichtung), Starblaze
(Sternenschauer), Shadowglen (Laubschattental), Darrowshire (Darroheim),
Booty Bay (Beutebucht), Ratchet (Ratschet), Dizzywig (Flunkerblick),
Hearthglen (Herdweiler), Chillwindspitze (Zugwindspitze), Stormrage
(Sturmgrimm), Stormpike (Sturmlanze/n), Ironforge (Eisenschmiede),
Thunderhorn (Donnerhörner), Steamboil (Kesseldampf), Twilight-Hammer,
-klan (Schattenhammer/Schattenhammerklan), Fathom-Kern (Tiefenkern),
Blackfathom Deeps (Tiefschwarze Grotte), Blackrock-* (Schwarzfels-*),
Hawkwind (Falkenwind), Feathermoon (Mondfeder), Moonrage (Mondzorn),
Firemane (Feuermähne), Searingblade (Sengende Klinge), Ragefireabgrund
(Flammenschlund), Ironbands Areal (Eisenbands Lager), Zandalar
(Zandalari), Southshore (Süderstade)

for quest progress/request text entries for the deDE localisation with
proper casus/declension (these are not proper translated names of
locations/NPCs that have been left over by Blizzard since their language
localisations in TBC in 2006 and onward).

Added missing progress/request text entries for 308, 311, 417, 1644,
1787, 5059, 5060, 5721, 6004, 6023, 6025, 6187, 8042, 8043, 8044, 8046,
8047, 8048, 8050-8079, 8102, 8107, 8108, 8111, 8112, 8113, 8117, 8118,
8142, 8143, 8147, 8183-8195, 8238, 8239, 8240, 8243, 8246, 8860, 9594,
9692, 9707, 10414, 10415, 10919, 11451. (A lot of them are
Zandalari/Zul'Gurub related quests.)

Replaced post-Cataclysm progress/request text entries for 933, 935,
6387, 7383.

Fixed a wrong $R with plain text at progress/request text for 9147.

Added missing female gender equivalent to 6391.

(There are probably more changes in the file that aren't further
explained here as it was hard to keep track of everything. If you think
I made a mistake or have questions please contact me directly.)

<!-- First of all, THANK YOU for your contribution. -->

## Changes Proposed:
-  Fixing a lot in the quest_request_items_locale table.

## Issues Addressed:
<!-- If your fix has a relating issue, link it below -->
- Fixing some of the tasks in
https://github.com/azerothcore/azerothcore-wotlk/issues/14244
Referring to my other two bug reports from CC Github:
- https://github.com/chromiecraft/chromiecraft/issues/4697
- https://github.com/chromiecraft/chromiecraft/issues/4745

## SOURCE:
<!-- If you can, include a source that can strengthen your claim -->
- Read the text on top.

## Tests Performed:
<!-- Does it build without errors? Did you test in-game? What did you
test? On which OS did you test? Describe any other tests performed -->
- Not tested.


## How to Test the Changes:
<!-- Describe in a detailed step-by-step order how to test the changes
-->
All of the changes are to reward texts of quests, can be tested by
completing quests or simply reviewing the changed file.

## Known Issues and TODO List:
<!-- Is there anything else left to do after this PR? -->

- [ ]
- [ ]

<!-- If you intend to contribute repeatedly to our project, it is a good
idea to join our discord channel. We set ranks for our contributors and
give them access to special resources or knowledge:
https://discord.com/invite/DasJqPba)
Do not remove the instructions below about testing, they will help users
to test your PR -->
## How to Test AzerothCore PRs
 
When a PR is ready to be tested, it will be marked as **[WAITING TO BE
TESTED]**.

You can help by testing PRs and writing your feedback here on the PR's
page on GitHub. Follow the instructions here:

http://www.azerothcore.org/wiki/How-to-test-a-PR

**REMEMBER**: when testing a PR that changes something **generic** (i.e.
a part of code that handles more than one specific thing), the tester
should not only check that the PR does its job (e.g. fixing spell XXX)
but **especially** check that the PR does not cause any regression (i.e.
introducing new bugs).

**For example**: if a PR fixes spell X by changing a part of code that
handles spells X, Y, and Z, we should not only test X, but **we should
test Y and Z as well**.

---
## [Maetrim/DDOBuilder](https://github.com/Maetrim/DDOBuilder)@[8d6c5e13eb...](https://github.com/Maetrim/DDOBuilder/commit/8d6c5e13eb649225f1661c64cfdf7915175ef6bc)
#### Friday 2023-02-17 21:02:31 by Maetrim

Build 1.0.0.181

Fix: New past life "Past Life: Acolyte of the Skin" updated with correct text and effects from Lamannia
Fix: Feat "Legendary Toughness" now has its requirement of Con 21 (Reported by MuazAlhaidar)
Fix: Fury of the Wild: Furious Force is now correct at +1 Strength while raging (Reported by Huntxrd)
Fix: Filigree's in set "Zarigan's Arcane Enlightment" now shows the correct set bonus values (Reported by christhemisss)
Fix: Filigree's in set "Elemental Avatar" now shows the correct set bonus values (Reported by pevergreen)
Fix: Feat "Improved Damage Reduction" can now also be taken by Bladeforged characters (Reported by Nectmar)
Fix: "Legendary Dreadnought: Sundering Swings" no longer erroneously requires "Dire Attack" (Reported by christhemisss)
New: Shadowdancer: Epic Strike Melee/Ranged attacks now have DC entries for them (Requested by christhemisss)
New: "Eldritch Knight: Arcane Siphon" now has a user controlled stance to allow the spell power effect to be enabled/disabled (Requested by christhemisss)
Fix: PDK "Ambidexterity" in the racial tree now correctly costs 1AP - wiki also updated (Reported by Sardabot)
Fix: "Exalted Angel: Angelic Form" is no longer erroneously classed as a "Major Form" (Reported by KYRREHK)
Fix: A variety of spelling mistakes was fixed.
Fix: An effect stacking issue where the same item is equipped in multiple slots (ring1/2 and Weapon1/2) was fixed (Reported by Huntxrd)
Fix: Item "Legendary Firesplitter" now correctly has its set bonus (Reported by Nectmar)
Fix: Enhancement "Elf: Nothing is Hidden" now has the correct AP cost (Reported by gorocz)
Fix: The "Discipline" feat and the relevant GmOF enhancements will now correctly grant the additional +5 MRR/PRR (Reported by Huntxrd)
Fix: "Reaper's Potency" in Dire Thaumaturge now has the corerct values (Reported by KYRREHK)
Fix: The Tiefling "Incineration I/II" enhancements now have the correct text and effects (Reported by KYRREHK);
New: Filigree Set "Snowpeak's Gifts" added
Fix: Item "Dinosaur Bone Runearm" now has its set bonus (Reported by Talnar)
Fix: Items "Epic/Legendary Skull of the Sea" now have their set bonuses (Reported by Talnar)
Fix: Shuriken Expertise will now add your Dexterity to your Doubleshot when using a Shuriken (Reported by Huntxrd)
Fix: Vistani: Knife Master (Core6) enhancement text and effects updated (Reported by deochii)
Fix: Elf/Ranger Arcane Archer T5 - Elemental Arrows now correctly grants its +2 Imbue dice (Reported by Nectmar)

U58 Lamannia 2 Changes:
---Dark Hunter now gain Medium Armor Proficiency at level 1
---Dark Hunter loses the Evasion feat at level 9
---Dark Hunter enhancement tree updated to match the Lamannia notes
---Acolyte of the Skin enhancement tree now has text, but no effects
---The Blight Caster enhancement tree now has effects
---The Dark Hunter enhancement tree now has effects

---
## [gyrovorbis/libgimbal](https://github.com/gyrovorbis/libgimbal)@[935ec3d4ee...](https://github.com/gyrovorbis/libgimbal/commit/935ec3d4ee2b9a94b2689d6ce86bf1720e7bce91)
#### Friday 2023-02-17 21:05:09 by Falco Girgis

HOLY SHIT, please GOD work, newfangled iOS CI YAML.

---
## [ikalnytskyi/vm.kalnytskyi.com](https://github.com/ikalnytskyi/vm.kalnytskyi.com)@[96aaf189c1...](https://github.com/ikalnytskyi/vm.kalnytskyi.com/commit/96aaf189c1745b22ef7641811d5137e4bc5efd5e)
#### Friday 2023-02-17 21:10:42 by Ihor Kalnytskyi

Run Vaultwarden natively

Containers are pain in the ass if all you're looking for is to self host
a bunch of tiny services. The reality, however, bites since there lots
of software without proper packages for Linux distributions.

This patch moves Vaultwarden from running in Podman to be run natively
via old plain systemd unit. For that to happen we first need to unpack
Vaultwarden from the docker image to disk, and then run it in isolated
environment.

Part of the reason why I want this is to play a bit with systemd
sandboxing functionality to understand better its pros and cons.

---
## [sv1/chirp](https://github.com/sv1/chirp)@[12301814e2...](https://github.com/sv1/chirp/commit/12301814e238458766f1f7bf06476b39a4e3ab93)
#### Friday 2023-02-17 21:27:57 by Dan Smith

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
## [JohnFrancisMcFall/android_kernel_msm-4.14](https://github.com/JohnFrancisMcFall/android_kernel_msm-4.14)@[89f1ef46f7...](https://github.com/JohnFrancisMcFall/android_kernel_msm-4.14/commit/89f1ef46f7c93ff42f5a72a0cf22acc3fafc5e7c)
#### Friday 2023-02-17 21:46:16 by Wang Han

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
## [ty-hal/SWE-Project](https://github.com/ty-hal/SWE-Project)@[a434d8af15...](https://github.com/ty-hal/SWE-Project/commit/a434d8af1588397eff224184fd6ac3c129926f06)
#### Friday 2023-02-17 22:13:18 by steven miller

Merge branch 'main' of https://github.com/ty-hal/SWE-Project
fuck you thats why

---
## [ivanjermakov/dwm](https://github.com/ivanjermakov/dwm)@[67d76bdc68...](https://github.com/ivanjermakov/dwm/commit/67d76bdc68102df976177de351f65329d8683064)
#### Friday 2023-02-17 22:23:40 by Chris Down

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
## [YakumoChen/Skyrat-tg](https://github.com/YakumoChen/Skyrat-tg)@[de0a48b02e...](https://github.com/YakumoChen/Skyrat-tg/commit/de0a48b02e65875833c6416fda28729677bc6245)
#### Friday 2023-02-17 22:25:52 by SkyratBot

[MIRROR] Unironically removes the atmos and black beret [MDB IGNORE] (#18747)

* Unironically removes the atmos and black beret (#72722)

## About The Pull Request

Removes atmos berets

## Why It's Good For The Game
Berets shouldn't be thrown into every job, it's milsim circlejerking
dressup shit that creeps out of our milsim containment jobs (security)
and into other innocent jobs. There is absolutely no reason for this job
to have a beret just straight up. Can we add unique hats to the game,
not the same one recolored every way to Sunday? That's my problem. We
don't have unique clothes, we have a billion types of beret when the
BASE BERET TYPE has `IS_PLAYER_COLORABLE_1` so ANYONE can color it. So
again, why do we have the atmos beret? To clog the wardrobe, a vending
machine added specifically because we couldn't stop clogging the
original locker atmos techs spawned in?

The black beret has the same problem: recolored item when you can get
the item of any color

## Changelog
:cl:
del: Atmospherics beret and black beret
/:cl:

* Unironically removes the atmos and black beret

* update modular

Co-authored-by: tralezab <40974010+tralezab@users.noreply.github.com>
Co-authored-by: Tom <8881105+tf-4@users.noreply.github.com>

---
## [Citadel-Station-13/Citadel-Station-13-RP](https://github.com/Citadel-Station-13/Citadel-Station-13-RP)@[81c1229373...](https://github.com/Citadel-Station-13/Citadel-Station-13-RP/commit/81c1229373208790c3375a138579aaf76a0006d0)
#### Friday 2023-02-17 23:36:58 by Captain277

Adds Just Like, a Ton of Clothes (#5048)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

1. **Adds a wide array of clothes, listed below.**

## Why It's Good For The Game

1. _My good friend Tech provided me with some sprite sheets when I was
working on Ashlanders, requesting a hobo coat. Going through the sheets
I found several different items I thought it would be fun to add to our
expanding list of customization and fashion options. The list is huge so
I'm just gonna itemize it here. As for attributions, as I understand it
most of this is from a D&D server, and some from a 40k server._
2. _Two of the outfits, the Belial and Lilin items, are sprites crafted
by our very own Doopy, as part of their Lindenoak line!_

## Outfits & Where to Get them

**Costume Vendor**
1. _Banana Costume_
3. _Hashashin Costume_
4. _Bard Hat_
5. _Aquiline Enforcer Uniform_
6. _Scavenging Sniper Set_
7. _Spiral Hero Outfit_
8. _Body Tape Wrapping_
9. _Redcoat Uniform_
10. _Despotic General Uniform_
11. _Post-Revolution American Uniform_
12. _Prussian Uniform_

**Suit Vendor**
1. _Ragged Coat_
2. _Spiral Hero Cloak_
3. _Nerdy Shirt_

**Jumpsuit Vendor**
1. _Toga_
2. _Countess Dress_
3. _Baroness Dress_
4. _Revealing Cocktail Dress_
5. _Belial Striped Shirt and Shorts_
6. _Lilin Sash Dress_

**Shoes Vendor**
1. _Utilitarian Shoes_

**Loadout**
1. _Ragged Coat_
7. _Spiral Hero Cloak_
8. _Nerdy Shirt_
9. _Bard Hat_
10. _Utilitarian Shoes_
11. _Toga_
13. _Countess Dress_
14. _Baroness Dress_
15. _Scavenging Sniper Set_
16. _Spiral Hero Outfit_
17. _Body Tape Wrapping_
18. _Revealing Cocktail Dress_
19. _Belial Striped Shirt and Shorts_
20. _Lilin Sash Dress_

**Medieval Armor Supply Crate**
1. _Crimson Knight Armor_
2. _Forest Knight Armor_
3. _Hauberk_
4. _Elite Paladin Armor, Helmet, and Boots_
5. _Alternate Knight Helmet_

**Cryosuit Supply Crates (Under Voidsuit Menu)**
1. _Cryosuit, Variants: Security, Engineering, Atmos, Mining_

**Crafting Menu**
1. _Duraskull Helmet_

**Ashlander Specific Crafting Menu**
1. _Ashen Vestment_
2. _Ashen Tabard_

**Ashlander Spawn**
1. _Priests now spawn with the Ashen Vestment._

**Admin Spawn**
1. _Actual armored versions of all new Knight sets._
5. _Utilitarian Military Helmet, Armor, and Boots._

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
add: Adds a wide array of new clothing items. Itemized in PR. #5408
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [NewyearnewmeUwu/cmss13](https://github.com/NewyearnewmeUwu/cmss13)@[b53c9f0531...](https://github.com/NewyearnewmeUwu/cmss13/commit/b53c9f0531897023fe365961c16863d8f41983d9)
#### Friday 2023-02-17 23:42:31 by carlarctg

Turns all instances of 'colour' into 'color' (#2609)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

Turns all instances of 'colour' into 'color'.

Changed a shittily-named crayon variable's name.

# Explain why it's good for the game

We use burgerclapper english and we should standardize this

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->


# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->
<!-- If you add a name after the ':cl', that name will be used in the
changelog. You must add your CKEY after the CL if your GitHub name
doesn't match. Be sure to properly mark your PRs to prevent unnecessary
GBP loss. Maintainers freely reserve the right to remove and add tags
should they deem it appropriate. -->

:cl:
spellcheck: Removed all instances of 'colour' and replaced them with
'color'
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---

