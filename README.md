## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-09-20](docs/good-messages/2022/2022-09-20.md)


2,249,461 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,249,461 were push events containing 3,342,654 commit messages that amount to 248,258,598 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 25 messages:


## [kernelci/linux](https://github.com/kernelci/linux)@[69337fce08...](https://github.com/kernelci/linux/commit/69337fce08d23d3435a14d8ffbf0fe51975abec3)
#### Tuesday 2022-09-20 00:04:21 by Johannes Weiner

mm: vmscan: fix extreme overreclaim and swap floods

During proactive reclaim, we sometimes observe severe overreclaim, with
several thousand times more pages reclaimed than requested.

This trace was obtained from shrink_lruvec() during such an instance:

    prio:0 anon_cost:1141521 file_cost:7767
    nr_reclaimed:4387406 nr_to_reclaim:1047 (or_factor:4190)
    nr=[7161123 345 578 1111]

While he reclaimer requested 4M, vmscan reclaimed close to 16G, most of it
by swapping.  These requests take over a minute, during which the write()
to memory.reclaim is unkillably stuck inside the kernel.

Digging into the source, this is caused by the proportional reclaim
bailout logic.  This code tries to resolve a fundamental conflict: to
reclaim roughly what was requested, while also aging all LRUs fairly and
in accordance to their size, swappiness, refault rates etc.  The way it
attempts fairness is that once the reclaim goal has been reached, it stops
scanning the LRUs with the smaller remaining scan targets, and adjusts the
remainder of the bigger LRUs according to how much of the smaller LRUs was
scanned.  It then finishes scanning that remainder regardless of the
reclaim goal.

This works fine if priority levels are low and the LRU lists are
comparable in size.  However, in this instance, the cgroup that is
targeted by proactive reclaim has almost no files left - they've already
been squeezed out by proactive reclaim earlier - and the remaining anon
pages are hot.  Anon rotations cause the priority level to drop to 0,
which results in reclaim targeting all of anon (a lot) and all of file
(almost nothing).  By the time reclaim decides to bail, it has scanned
most or all of the file target, and therefor must also scan most or all of
the enormous anon target.  This target is thousands of times larger than
the reclaim goal, thus causing the overreclaim.

The bailout code hasn't changed in years, why is this failing now?  The
most likely explanations are two other recent changes in anon reclaim:

1. Before the series starting with commit 5df741963d52 ("mm: fix LRU
   balancing effect of new transparent huge pages"), the VM was
   overall relatively reluctant to swap at all, even if swap was
   configured. This means the LRU balancing code didn't come into play
   as often as it does now, and mostly in high pressure situations
   where pronounced swap activity wouldn't be as surprising.

2. For historic reasons, shrink_lruvec() loops on the scan targets of
   all LRU lists except the active anon one, meaning it would bail if
   the only remaining pages to scan were active anon - even if there
   were a lot of them.

   Before the series starting with commit ccc5dc67340c ("mm/vmscan:
   make active/inactive ratio as 1:1 for anon lru"), most anon pages
   would live on the active LRU; the inactive one would contain only a
   handful of preselected reclaim candidates. After the series, anon
   gets aged similarly to file, and the inactive list is the default
   for new anon pages as well, making it often the much bigger list.

   As a result, the VM is now more likely to actually finish large
   anon targets than before.

Change the code such that only one SWAP_CLUSTER_MAX-sized nudge toward the
larger LRU lists is made before bailing out on a met reclaim goal.

This fixes the extreme overreclaim problem.

Fairness is more subtle and harder to evaluate.  No obvious misbehavior
was observed on the test workload, in any case.  Conceptually, fairness
should primarily be a cumulative effect from regular, lower priority
scans.  Once the VM is in trouble and needs to escalate scan targets to
make forward progress, fairness needs to take a backseat.  This is also
acknowledged by the myriad exceptions in get_scan_count().  This patch
makes fairness decrease gradually, as it keeps fairness work static over
increasing priority levels with growing scan targets.  This should make
more sense - although we may have to re-visit the exact values.

Link: https://lkml.kernel.org/r/20220802162811.39216-1-hannes@cmpxchg.org
Signed-off-by: Johannes Weiner <hannes@cmpxchg.org>
Reviewed-by: Rik van Riel <riel@surriel.com>
Acked-by: Mel Gorman <mgorman@techsingularity.net>
Cc: Hugh Dickins <hughd@google.com>
Cc: Joonsoo Kim <iamjoonsoo.kim@lge.com>
Cc: <stable@vger.kernel.org>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>

---
## [jwellan1/graspologic](https://github.com/jwellan1/graspologic)@[240b913560...](https://github.com/jwellan1/graspologic/commit/240b913560c6dc7437750fc6a519645453556b3c)
#### Tuesday 2022-09-20 00:26:50 by Dwayne Pryce

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
## [jwellan1/graspologic](https://github.com/jwellan1/graspologic)@[020e451ee6...](https://github.com/jwellan1/graspologic/commit/020e451ee61c83fbb3effc67a6a30781dddff900)
#### Tuesday 2022-09-20 00:26:50 by Dwayne Pryce

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
## [jjpark-kb/Skyrat-tg](https://github.com/jjpark-kb/Skyrat-tg)@[00d7e1f375...](https://github.com/jjpark-kb/Skyrat-tg/commit/00d7e1f375b7f6f55f71d77be8c7612a6a5d6030)
#### Tuesday 2022-09-20 01:11:51 by SkyratBot

[MIRROR] Rocking The Boat, er, Map Vote [MDB IGNORE] (#16083)

* Rocking The Boat, er, Map Vote (#69561)

* Rocking The Boat, er, Map Vote

Hey there,

A while ago, I spooke (typo intentional) to some other people. One frustration I heard was the fact that people would sometimes sneak through map votes during the very start of a shift, during a high-paced portion, or just as a meme. People in OOC would then flood the vote, putting in any given station. However, if a vote happens 10 minutes in- and the round goes for 70 minutes and not many of the original players are around, then it's not particularly fair to those who have to play next shift on a map they bemoan.

So, we can rock the vote! If a player isn't particularly chuffed with the hand they are given, they can poll the players to see if they want to change the map as well. If rocking the vote goes through, huzzah, you get the ability to vote for the map again. If it doesn't go through: tough luck. You can rock the vote one time per shift by default, and server operators can change the amount of times you can call to rock the map vote at their discretion. Calling to rock the vote either successfully or non-successfully counts as a "call", and when that limit is exceeded: no more calls.

Does this mean that we will only rotate between two maps because pissants will keep rocking the vote until they get what they like? Maybe? I still see people bemoan getting Tram or shit the bed over IceBox, but I think enough people get sick of bread-on-butter to take the server where it need to go. If operators don't really like seeing only two maps play, they can always adjust the config to ensure it doesn't happen.

* makes the grammar grammar

it would be "Rock the Vote vote" otherwise

* Rocking The Boat, er, Map Vote

Co-authored-by: san7890 <the@san7890.com>

---
## [facebook/hermes](https://github.com/facebook/hermes)@[2ee505c6db...](https://github.com/facebook/hermes/commit/2ee505c6db6f0452006e15719fd5c1f5d6aa6231)
#### Tuesday 2022-09-20 01:52:47 by Tzvetan Mikov

produce a single hermesvm library

Summary:
The separate library per component strategy is straight-forward to create
and simplifies unit testing and simple tools. However it is very
inconvenient for users of the whole, since the names and paths of all
internal libraries are just implementation details. An embedder of
Hermes should ideally just need to link against `libhermes.a`.

This is what this commit does - it produces three standalone libraries:
- `libhermescompiler.a`
- `libhermesvm.a`
- `libhermesvmlean.a`

The `hermes`, `hermesc`, and `hvm` tools, as well as the JSI API, just
link to the corresponding library.

## Implementation Details

This is a rather big change, touching all CMakeLists.txt files.

It attempts to preserve the previous capabilities in a natural way (the
ability to just link against a library defined in a directory) while
generating the new "combined" libraries, hopefully without too many
hacks. It doesn't complete succeed to avoid hacks, but it passes
tests.

First, support for HERMES_LINK_COMPONENTS is removed, since it is
unnecessary and confusing - just an extra implicit way to add
dependencies to a target, as if we didn't have enough already.

The big change that enables the "amalgamation" of smaller libraries into
a large combined one, without hacks, is using CMake's "OBJECT"
libraries.

A CMake "OBJECT" library is an abstract collection of objects with
metadata, which acts in many ways similar to a regular library: it can
be linked against, and it propagates metadata transitively (defines,
include directories, etc).

One critical way in which it differs from normal libraries is that it
doesn't transitively propagate "OBJECT" library dependencies. In other
words, if OBJECT library B depends on OBJECT library A, and we link
a binary against B, we will get link errors for A's symbols.

So, it is impossible to just replace normal libraries with object
libraries, we need to be aware of the distinction.

### add_hermes_library() changes

We have extended `add_hermes_library()` to support this new notion of
OBJECT libraries, by recognizing the STATIC, SHARED or OBJECT keyword,
defaulting to OBJECT. If STATIC or SHARED is used, it works as it did
previously. If no keyword, or OBJECT, is specified it creates the new
type of library.

The dependencies that can be supploed to `add_hermes_library()` are also
extended: "normal" libraries are specified as before with `LINK_LIBS`,
but object library dependencies are specified with `LINK_OBJLIBS`. Since
we have converted most libraries to OBJECT, `LINK_OBJLIBS` is now more
common.

Example:
```
add_hermes_library(foo OBJECT f1.c
        LINK_OBJLIBS dep1 dep2
        LINK_LIBS pthread)
target_compile_definitions(foo_obj PUBLIC FOO=1)
```

Here a new OBJECT library `foo_obj` containing `f1.c.o` is defined. It
depends on `dep1_obj` and `dep2_obj`, this transitively pulling their
metadata. It also depends on `pthread`, which is a normal library.

`foo_obj` also has a public definition `-DFOO=1`.

A regular STATIC library `foo` is also defined. It depends on
`foo_obj`, which means that it pulls in its object files (`foo_obj`'s
object files are copied to the `.a` file without recompiling) and also
pulls it its transitive metadata, including the dependency on `pthread`
and `-DFOO=1`.

So, `foo_obj` is a collection of object files that we can use to combine
into a combined library, while `foo` is a static library, which we may
continue use as before.

Very important: note that `target_compile_definitions()` refers to
`foo_obj` instead of `foo`. I hope it is clear why. That is rather
annoying, but unfortunately there doesn't seem to be another war.

Also note that when rebuilding `hermes`, none of the many small
libraries are built, since `hermes` only depends on `hermesvm`, which
only depends on `xxx_obj` libraries. So, the build is not slower than
before.

Reviewed By: neildhar, avp

Differential Revision: D39264257

fbshipit-source-id: a972ef97f2b1b71ec4a52756c135efdd99756269

---
## [necromanceranne/tgstation](https://github.com/necromanceranne/tgstation)@[ad01ab5ed0...](https://github.com/necromanceranne/tgstation/commit/ad01ab5ed0a5f80278076b1e0e6ac33fe73b0e32)
#### Tuesday 2022-09-20 02:21:31 by LemonInTheDark

Fixes asset caching (#69852)

The asset was being loaded, seeing that fully_generated is false, so it
attempts to rebuild. The rebuilding clears the existing file cache, and
fucks us.

Life is pain.

---
## [oxidecomputer/omicron](https://github.com/oxidecomputer/omicron)@[53c732aa97...](https://github.com/oxidecomputer/omicron/commit/53c732aa97f79e2ba494131660390de951227b40)
#### Tuesday 2022-09-20 02:40:28 by Andrew J. Stone

Bootstore message handler implementation (#1687)

This is the second PR of the `bootstore` implementation. It creates handler
methods for all existing messages and their corresponding DB requirements. RFD
238 section 5 will need to be updated to reflect this flow.

The way the flow currently is supposed to work is that there is a coordinator
(coming in a follow up PR) that sends the following messages to initialize the
trust quorum:
 * `Initialize`
 * `KeyShareCommit` (for epoch 0)

`Initialize` can be sent multiple times until the `KeyShareCommit` for epoch 0
locks in the configuration and Rack UUID. This allows the initial coordinator
(RSS) to die, and even have its local storage or entire sled die, and still
allow us to make progress via a new RSS. Importantly, once wired through the
system, the coordinator will negotiate (via sled-agent and nexus) to write the
`KeyShareCommit` to CockroachDB before sending it to all nodes. This ensures
that the rack initialization will complete and CockroachDB only has to be setup
once. There are some tricky failure modes here, but none of that is in this PR,
so we can move on. The important point here is that once a `KeyShareCommit` for
epoch 0 succeeds the rack is initialized.

After initialization, reconfiguration of the trust quorum can take
place. Reconfiguration messages must be issued with the same Rack UUID. A
reconfiguration consists of a `KeySharePrepare` for an `epoch > 0` followed by
a `KeyShareCommit` for the same epoch. After initialization a `KeySharePrepare`
can never be mutated. However, to allow for certain failures, such as
the failure of a node being prepared to ack (since we require unanimous
acknowledgement in 2PC), we allow for new `KeySharePrepare`s at higher
epochs to proceed. We keep track of these epochs in CockroachDB to maintain
linearizability. Once a node receives a prepare for a higher epoch, it will no
longer accept prepare or commit messages for any lower epoch. Once a successful
`KeyShareCommit` is handled, the sled is now operating at the new epoch.

`GetShare` requests are used to unlock trust quorum. They will rely on
sprockets at the network level for authentication, confidentiality, integrity,
and attestation. Some DeviceId membership validation will also be added to
`Node`in future commits as it currently exists in sled agent.

This is an incremental PR and there is still a lot to do here. Follow up
commits will:
 * Add more negative tests (possibly in this PR also)
 * Add code for a coordinator
 * Add a mechanism to store the encrypted (wrapped) root secret for each
   epoch and likely include it in each `KeySharePrepare`. This is the most
   straightforward way to transfer wrapped secrets. We can get more
   sophisticated in the future. Again, this needs to be written up in RFD 238,
   but I'm likely to just implement it within the next week and see how it works
   first.
 * Add some key derivation from the root secret such that we can use these keys
   to encrypt and decrypt storage
 * Add property based tests to simulate a full cluster along with failures and
   ensure rack unlock works according to the model and ensure that we can
   *always* unlock encrypted storage while tolerating our prescribed failure
   conditions within the model.

After that, the `bootstore` will basically be implemented at a non-network
level. We'll then likely want to port over the sprockets code from the
bootstrap agent to a higher level here, and use the `Node` and `Coordinator`
from that level, which will end up interacting with Nexus and CockroachDB
via the sled-agent. Multiple tasks will be utilizing the `Node` and its
underlying `Db` at this point and so we'll need some concurrency control.
I've given this a bit of thought and my current thinking is to have the `Node`
running in it's own thread and serialize all operation via a channel. Outside
of reconfiguration, all operations are reads, and we can simply cache the
current share in memory for rack unlock purposes (e.g. `GetShare`). During
reconfiguration, we'll mutate the DB as necessary, and refresh our cache. This
strategy avoids the need for mutexes and has the characteristic that the `Node`
and `Db` code we run in a single threaded manner in property based tests is
actually running the same way in production with just a single DB connection.
This strategy isn't set in stone, but in my mind it's the easiest to reason
about and also the easiest way to hook async to sync code.

---
## [s11071802/Rokovaki_s11071802](https://github.com/s11071802/Rokovaki_s11071802)@[a948c85323...](https://github.com/s11071802/Rokovaki_s11071802/commit/a948c85323e5d16474822a9b7715b1ba0d0a6a8e)
#### Tuesday 2022-09-20 04:08:36 by Asinate Rokovaki

Add files via upload

Milestone 2
1.	Document Review: You’re Doing it Wrong Cognitive Psychology and the Attorney’s Mental Plate
Summary
Splitting document review into several steps is a strategy Sidley Austin LLP gives to lawyers trying to address the issues caused by ineffective document review. Reviewers are frequently told to perform a thorough factual assessment of the documents in addition to the usual privilege review and production review.

Reference
Keeling, R. (2020). Document Review: You’re Doing It Wrong Cognitive Psychology and the Attorney’s Mental Plate. University of Arkansas at Little Rock Law Review, 42(2), 257–278.

2.	Law, Psychology, and Morality: The Role of Loss Aversion

The Psychology of Loss of Aversion 

Chapter 1: Loss Aversion

Summary
The study of loss aversion looks at how it affects more specific phenomena including constrained ethicality, the endowment effect, the status quo bias, and omission bias. The chapter also discusses research on how emotions and loss aversion interact. It draws attention to how prevalent reference reliance is in people's perceptions and assessments. It also emphasizes the influence loss aversion has had on other areas.
Reference
Zamir, E. (2014). Law, Psychology, and Morality:. The Role of Loss Aversion. https://doi.org/19 September, 2022
	
3.	Law, Psychology, Morality: Understanding Human Behaviour in Human Contexts
Chapter 2 

Summary
The law must consider how people perceive the options available to them and how these perceptions influence their decisions and conduct in order to effectively guide human behaviour. Due to people's tendency to favour the status quo, the essential actions to combat climate change are likely to face fierce opposition.	
	Reference
Zamir, E. (2014). Understanding Human Behaviour in Legal Contexts:. Law, Psychology, and Morality:. https://doi.org/19 September, 2022

4.	The Cognitive Psychology of Circumstantial Evidence
Summary
Jurors frequently overvalue direct evidence while undervaluing indirect evidence (such as DNA and fingerprints) (eyewitness identifications and confessions). This is true despite the fact that data on false convictions suggests the former is typically more dependable and probative than the latter.
Reference
Heller, K. J. (2006). The Cognitive Psychology of Circumstantial Evidence. Michigan Law Review, 105(2), 241–305. http://www.jstor.org/stable/40041577

5.	Towards a New Relationship Between trademark Law and Psychology 
Summary
Establishing the mental states of consumers is a topic that both trademark law and cognitive psychology address. Further investigation reveals significant issues, particularly those related to the registration process under trademark law. The objectives and philosophical tenets of these two disciplines are not easily reconciled. To make that happen, we must abandon the notion that psychological insights are only applicable to resolving legal conflicts. Testing trademark laws at a higher level of abstraction is a better strategy.
Reference
Burrel, R, Weatherall, K, Towards a New Relationship Between Trade Mark Law and Psychology. Current Legal Problems, Volume 71, Issue 1, 2018, Pages 87-118. https://doi.org/10.1093/clp/cuy001

---
## [Star12345678900/Star12345678900](https://github.com/Star12345678900/Star12345678900)@[0fbc292627...](https://github.com/Star12345678900/Star12345678900/commit/0fbc292627297286b63d9c5ad546b2caae53fabe)
#### Tuesday 2022-09-20 06:16:31 by Anjanee kumari

Update README.md

I am Anjanee kumari. Pursuing my Bachelors in Computer Science & Engineering. I want contributing to Open source program, project and am really enthusiastic about learing new technology. I learnt web development till now ,I also learnt c++ and now I learing java and DSA. Apart from outside the world of teach too. I love pushing myself to develop new skills.I love reading books on personal development and financial literacy.My favourites ones are Rich Dad Poor Dad by Robert Kiyosaki in the genre of financial literacy . I like to  play badminton and I love to  travel & I hoping after my clg I want to travel in diff diff country......

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[b3b85cae9b...](https://github.com/odoo-dev/odoo/commit/b3b85cae9b1951b82053d7c6b55e559cbc48307d)
#### Tuesday 2022-09-20 08:22:20 by Xavier Morel

[IMP] *: owlify password meter and convert change password to real wizard

The changes in `auth_password_policy` are largely the owlification of
the password meter widget:

- modernize the password policy module and convert it to an
  odoo-module (note: now exports a pseudo-abstract class which is
  really a policy, for the sake of somewhat sensibly typing
  `recommendations`)
- replace the implementation of the Meter and PasswordField widgets by
  owl versions

The changes to web and base stem from taking a look at converting the
ChangePassword wizard, and finding that it would be a pain in the ass
but also... unnecessary? It seems to have been done as a wizard
completely in javascript despite being backend-only for legacy
reasons: apparently one of the very old web clients (v5 or v6
probably) implemented it as a "native action" which was directly part
of the client's UI, and so it had to be implemented entirely in the
client.

Over time it was moved back into the regular UI (and moved around
quite a bit), hooked as a client action to maintain access to the
existing UI / dialog.

But since it's been an action opened via a button for years it can
just... be a normal wizard, with password fields, which
auth_password_policy can then set the widget of.

So did that:

- removed the old unnecessary JS, and its dedicated endpoint (which is
  *not* used by portal, portal has its own endpoint)
- used check_identity for the "old password check"
- split out `change_password` with an internal bit so we can have a
  safer (and logged) "set user password" without needing to provide
  the old password, which is now used for the bulk password change
  wizard as well
- added a small wizard which just takes a new password (and
  confirmation), for safety a given change password wizard is only
  accessible to their creator (also the wizard is restricted to
  employees though technically it would probably be fine for portal
  users as well)

Rather than extensive messy rewrite / monkeypatching (the original
wizard was 57 LOC, though also 22 LOC of template, the auth_policy
hooking / patching was 33, plus 8 lines of CSS),
`auth_password_policy` just sets the widget of the `new_password`
field in the new wizard, much as it did the bulk wizard.

Also improve the "hide meter if field is empty" feature by leveraging
`:placeholder-shown`. This requires setting a placeholder, and while
empty works fine in firefox, it doesn't work in chrome. So the
placeholder needs to be a single space. Still, seems better than
updating a fake attribute or manipulating a class for the sake of
trivial styling.

Notes on unlink + transient vacuum

Although the wizard object is only created when actually calling
`change_password`, and is deleted on success, it is possible for the
user to get an error and fail to continue (it should be unlikely
without overrides since the passwords are checked while creating /
saving but...).

While in that case the `new_password` in the database is not the
user's own, it could be their *future* password, or give evidence as
to their password-creation scheme, or some other signal useful to
attack that front of the user's life and behavior. As such, quickly
removing leftovers from the database (by setting a very low transient
lifetime) seems like a good idea.

This is compounded by the `check_identity` having a grace period of 10
minutes. 0.1 is 6 minutes, but because the cron runs every 10 the user
effectively has 6~10 minutes between the moment they create an
incorrect / incomplete version of the wizard and the moment where it
is destroyed if they just leave it.

closes odoo/odoo#99458

Signed-off-by: Xavier Morel (xmo) <xmo@odoo.com>

---
## [mathieufontaine/free-programming-books](https://github.com/mathieufontaine/free-programming-books)@[94eeda1bba...](https://github.com/mathieufontaine/free-programming-books/commit/94eeda1bbaca9e88505ea27d120b6056814622d8)
#### Tuesday 2022-09-20 09:19:00 by Mathieu FONTAINE

Update free-programming-cheatsheets.md - React

I suggested a React cheat sheet that I use very often. It is one of the most exhaustive and qualitative in my opinion.

---
## [lerndmina/Laddie-bot](https://github.com/lerndmina/Laddie-bot)@[72d7d63ba9...](https://github.com/lerndmina/Laddie-bot/commit/72d7d63ba938a1ec8d377f36a3a22ef429676c93)
#### Tuesday 2022-09-20 10:36:06 by Adam

Holy shit. This was the most annoying bug to solve

---
## [MLGCrisis/qb-vehiclekeys](https://github.com/MLGCrisis/qb-vehiclekeys)@[757fdd0859...](https://github.com/MLGCrisis/qb-vehiclekeys/commit/757fdd0859013e45f9d432fa894f0ecb03d8bbf5)
#### Tuesday 2022-09-20 11:15:48 by ItsANoBrainer

Proper Refactor

Refactored the entire resource because the key system was not working.

No longer does a server callback 10 or so times a second, on top of other bad practices.

Tested pretty much everything with my devs, but there might be some weird issues we havnt found. Please lookover as I've been going crazy with the small tedious issues I've come across doing this.

Throwing this up to get feedback, and for people to use who want it.

Features:

- Keys are saved server side, and sent to each client when they are added or removed, as well as on character selection. This allows characters to leave and come back in the same server uptime session and still have the same keys
- Keys are only pulled from the server once on character load
- Giving keys has 3 types, /givekeys with an id will attempt to give keys you have to an id, not including an id will try to give it to the closest person, and if you're in a vehicle it will give to everyone
- Can only give keys to vehicles you have keys to
- Server event to force acquire keys to a plate for a person (for lockpicking/stealing/spawning, etc.)
- Can Carjack an NPC with a gun, has different percentages to work based on weapon (config)
- Take keys from dead npc drivers
- Can lockpick a car to unlock the doors
- Can hotwire a car if you're in the driver seat of the vehicle you dont have keys to to get keys
- Keeps the engine of a vehicle off if you dont have keys to it (allows other resources to attempt to toggle car engine without needing to interface if you have keys or not)
- Vehicle blacklist system for vehicles you dont want to be lockable (always unlocked)
- Police Alerts from lockpicking/hotwiring/carjacking
- Export to check if you have keys to a vehicle
- Locking/unlocking with hotkey
- Locking/unlocking and giving keys uses a custom GetVehicleInDirection you are facing for realism/accuracy
- Fully compatible with old resource. Has an event handler for 'vehiclekeys:client:SetOwner' in which it gives keys for that plate
- Some other shit I probably forgot

TODO:
- Add LOCALE support
- Stop peds from wanting to get back into the vehicle they just got carjacked out of as they're fleeing

---
## [hjwp/2022.pyconuk.org](https://github.com/hjwp/2022.pyconuk.org)@[ab1643dfe4...](https://github.com/hjwp/2022.pyconuk.org/commit/ab1643dfe478cb99d7abf7107a02b2aec89caa9d)
#### Tuesday 2022-09-20 15:45:12 by Harry Percival

Add X-Clacks Overhead memorials http head/meta tags

Although it's kinda too late for this year, I figured I'd add this as a base for future year's copypasting

this html `<meta>` tag is the [recommended way](http://www.gnuterrypratchett.com/#HTML) to implement gnu-terry-pratchett if you don't have control over your webserver's headers.

looks like we're currently hosted by netlify so [there may be another way](https://docs.netlify.com/routing/headers/) -- but that would lock us into netlify a bit?  this felt more vendor-neutral.  not that bothered tho.  more keen on making the gesture one way or another.

---
## [SallyBsat/Tracking-Sally-s-work](https://github.com/SallyBsat/Tracking-Sally-s-work)@[6a877eaa77...](https://github.com/SallyBsat/Tracking-Sally-s-work/commit/6a877eaa778c83c194d87dd44bbd57339c5d77c8)
#### Tuesday 2022-09-20 16:39:42 by AndreaMariani-AM

Uh oh, uh oh, uh oh, oh no no
Uh oh, uh oh, uh oh, oh no no
Uh oh, uh oh, uh oh, oh no no
Uh oh, uh oh, uh oh, oh no noYou got me looking, so crazy my baby
I'm not myself lately I'm foolish, I don't do this
I've been playing myself, baby I don't care
Baby your love's got the best of me
Your love's got the best of me
Baby your love's got the best of me
Baby you're making a fool of me
You got me sprung and I don't care who sees
Cause baby you got me, you got me, oh you got me, you got meI look and stare so deep in your eyes
I touch on you more and more every time
When you leave I'm begging you not to go
Call your name two or three times in a row
Such a funny thing for me to try to explain
How I'm feeling and my pride is the one to blame
And I still don't understand
Just how your love could do what no one else can Got me looking so crazy right now
Your love's got me looking so crazy right now
Got me looking so crazy right now
Your touch got me looking so crazy right now (your love)Hoping you'll save me right now
Your kiss got me hoping you'll save me right now (your love)
Looking so crazy in love
Got me looking, got me looking so crazy in love
Got me looking so crazy right now
Your love's got me looking so crazy right now
Got me looking so crazy right now
Your touch got me looking so crazy right nowGot me hoping you'll save me right now
Your kiss got me hoping you'll save me right now (your love)
Looking so crazy in love
Got me looking, got me looking so crazy in loveUh oh, uh oh, uh oh, oh no no
Uh oh, uh oh, uh oh, oh no no
Uh oh, uh oh, uh oh, oh no no
Uh oh, uh oh, uh oh, oh no no

---
## [SorryPip/C299-mthree-assignments](https://github.com/SorryPip/C299-mthree-assignments)@[cadb1370d3...](https://github.com/SorryPip/C299-mthree-assignments/commit/cadb1370d30e1cbb5266debe9fdb29e55012f8ca)
#### Tuesday 2022-09-20 16:40:48 by SorryPip

I hate my life, but one down

i rushed it so there user inputs arents validated properly
so dont f around w the inputs pls

---
## [apollographql/apollo-server](https://github.com/apollographql/apollo-server)@[bdd3da0b51...](https://github.com/apollographql/apollo-server/commit/bdd3da0b519744fd5483f5d5b6e4b1fce0e41cf3)
#### Tuesday 2022-09-20 18:49:21 by Trevor Scheer

Strengthen messaging around lack of support for Playground (#6925)

Playground will be published for AS4 only as a means to facilitate
migration, but we will not promise any support for it after its initial
post-alpha/rc publish. Let's make this messaging extra clear for users.

Leaving it in the migration guide (as is its purpose) but removed it
from our API docs. I could be convinced to restore that portion but I
think I'd rather users have to jump through at least one hoop and look
at the types if they want to use it that badly.

Closes https://github.com/apollographql/apollo-server/issues/6109
<!--
First, 🌠 thank you 🌠 for taking the time to consider a contribution to
Apollo!

Here are some important details to follow:

* ⏰ Your time is important
To save your precious time, if the contribution you are making will take
more
than an hour, please make sure it has been discussed in an issue first.
          This is especially true for feature requests!
* 💡 Features
Feature requests can be created and discussed within a GitHub Issue. Be
sure to search for existing feature requests (and related issues!) prior
to
opening a new request. If an existing issue covers the need, please
upvote
that issue by using the 👍 emote, rather than opening a new issue.
* 🔌 Integrations
Apollo Server has many web-framework integrations including Express,
Koa,
Hapi and more. When adding a new feature, or fixing a bug, please take a
peak and see if other integrations are also affected. In most cases, the
fix can be applied to the other frameworks as well. Please note that,
since new web-frameworks have a high maintenance cost, pull-requests for
new web-frameworks should be discussed with a project maintainer first.
* 🕷 Bug fixes
These can be created and discussed in this repository. When fixing a
bug,
please _try_ to add a test which verifies the fix. If you cannot, you
should
still submit the PR but we may still ask you (and help you!) to create a
test.
* 📖 Contribution guidelines
Follow
https://github.com/apollographql/apollo-server/blob/main/CONTRIBUTING.md
when submitting a pull request. Make sure existing tests still pass, and
add
          tests for all new behavior.
* ✏️ Explain your pull request
Describe the big picture of your changes here to communicate to what
your
pull request is meant to accomplish. Provide 🔗 links 🔗 to associated
issues!

We hope you will find this to be a positive experience! Open source
contribution can be intimidating and we hope to alleviate that pain as
much as possible. Without following these guidelines, you may be missing
context that can help you succeed with your contribution, which is why
we encourage discussion first. Ultimately, there is no guarantee that we
will be able to merge your pull-request, but by following these
guidelines we can try to avoid disappointment.
-->

Co-authored-by: Rose M Koron <32436232+rkoron007@users.noreply.github.com>

---
## [IvanYashchuk/pytorch](https://github.com/IvanYashchuk/pytorch)@[afcc7c7f5c...](https://github.com/IvanYashchuk/pytorch/commit/afcc7c7f5c7cef740241ff0abdae8d4f2ad22a03)
#### Tuesday 2022-09-20 19:01:23 by Andrew Gu

[FSDP] Generalize prefetching; lower unshard/reshard to handle (#83665)

### Additional Constructor Changes
- `self.sharding_strategy`
    - If the world size is 1, I clamp the sharding strategy to `NO_SHARD`, regardless of the passed-in sharding strategy, since the behavior is fully equivalent. This absolves the need for `p._is_sharded or self.world_size == 1` checks in the core code. Once we fully shift the paradigm to using handles, this should result in a clear net positive. However, for now, we still have some places where we interface directly with the `FlatParameter`, in which case we have some temporary hacky code.
- `HandleConfig`
    - As a part of the new design abstraction, much logic is lowered to the `FlatParamHandle`. This requires the handle be aware of mixed precision, CPU offloading, sharding strategy, and the process group (for world size > 1). To be less error-prone, I re-defined the `dataclass`s and `enum`s for the handle. These can be removed and coalesced with the existing ones.
    - The drawback is that the `FlattenParamsWrapper` constructor now takes in the `HandleConfig` to forward it to the `FlatParamHandle` constructor. I tolerate this since we plan to retire the FPW. For now, the handle's process group attributes are set later when we call `handle.shard()`.
    - We will dive into this logic lowering later. For now, the idea is we need to pass some extra info to the handle, which must go through the FPW.
- `FullyShardedDataParallel._shard_parameters()` -> `FlatParamHandle.shard()`
- [Important] Generalizing attributes to remove the 1 `FullyShardedDataParallel` : 1 `FlatParameter` assumption
    - **Before:** `_fsdp_graph_order`, `_pre_backward_hook_full_params_prefetched`, `_forward_full_params_prefetched`, `reshard_after_forward` are with respect to 1 `FullyShardedDataParallel`
    - **After:** (1) We use `FlatParamHandle` in place of `FullyShardedDataParallel`. (2) The atomic unit for forward and pre-backward is a _group_ of handles involved in the same module's forward/pre-backward. This is represented as `Tuple[FlatParamHandle, ...]`. For now, this is **always a singleton tuple**, but this shift enables a module having multiple FSDP parameters (which we have use cases for).
- `_reset_lazy_init()` attributes
    - The prefetched flags are merged into `self._handles_prefetched`, which is directly defined in the constructor. `reshard_after_forward` is retired since it can be fully determined by other attributes (`_is_root` and `sharding_strategy`).

## FSDP Runtime: Unshard

The first step is to read the existing `_rebuild_full_params()`. A few notable observations:
- It returns `Tuple[Tensor, bool]`. The first element is the _padded unsharded flattened parameter_, and the second element is whether we can free it upon exiting `summon_full_params()`. This return value is **only used in `summon_full_params()`**.
- If parameter mixed precision is enabled and the `FlatParameter` is already unsharded, then the low precision shard (`_mp_shard`) is still re-allocated on GPU. (It is freed at the end of the method.)
- If CPU offloading is enabled and the `FlatParameter` is already unsharded, then there is a no-op `p.data = p.data.to(self.compute_device, non_blocking=True)`.
- Inside `summon_full_params()`, `mixed_precision_cast_ran` is always `False`. Therefore, the return value for the `not p._is_sharded and mixed_precision_cast_ran` branch is unused.
-`summon_full_params()` can only be called (before forward or after backward) or (between forward and backward). Given this, I cannot think of a case where we call `summon_full_params()`, the `FlatParameter` is already unsharded, but `reshard_after_forward` is `True`. The `FlatParameter` should be sharded (before forward or after backward), and the `FlatParameter` may only be unsharded (between forward and backward) if `reshard_after_forward` is `False`.
- If parameter mixed precision is enabled and the sharding strategy is a sharded one, then inside `summon_full_params()`, the `FlatParameter` is unsharded in full precision. This involves allocating a new padded unsharded flattened parameter on GPU in full precision since `_full_param_padded` is in the low precision.

Some comments:
- Ideally, we reduce the complexity of the core code path: i.e. unshard for forward and pre-backward. If the return value is only used for `summon_full_params()`, we should consider if we can compartmentalize that logic.
- The branching is complex, and some return values are never used, where this fact is not immediately obvious. We should see if we can reduce the branch complexity.

Disclaimer: The difference in attribute semantics between `NO_SHARD` and the sharded strategies makes it challenging to unify the cases. This PR does not attempt to address that since it requires more design thought. However, it does attempt to reduce the complexity for the sharded strategies.

### Unshard: Core Code Path
Let us trace through the new logical unshard.
1. `FullyShardedDataParallel._unshard(self, handles: List[FlatParamHandle], prepare_gradient: bool)`
    - This iterates over the handles and calls `handle.pre_unshard()`, `handle.unshard()`, and `handle.post_unshard(prepare_gradient)` in the all-gather stream.
2. `FlatParamHandle.needs_unshard(self)`
    - We take an aside to look at this key subroutine.
    - For `NO_SHARD`, this returns `False`.
    - For sharded strategies, this checks if the padded unsharded flattened parameter is allocated. The padded unsharded flattened parameter is the base tensor for the unpadded unsharded flattened parameter, which is a view into the padded one. Thus, the padded one's allocation fully determines if the `FlatParameter` is unsharded.
    - For sharded strategies, to accommodate the parameter mixed precision + `summon_full_params()` case, we introduce `_full_prec_full_param_padded`, which is the padded unsharded flattened parameter in full precision. The helper `_get_padded_unsharded_flat_param()` takes care of this casing and returns the padded unsharded flattened parameter. Instead of allocating a new tensor each time, we manually manage `_full_prec_full_param_padded`'s storage just like for `_full_param_padded`.
3. `FlatParamHandle.pre_unshard(self)`
    - For sharded strategies, the postcondition is that the handle's `FlatParameter` points to the tensor to all-gather. This should be on the communication device and in the desired precision. The allocation and usage of the low precision shard for parameter mixed precision and the CPU -> GPU copy for CPU offloading both classify naturally in the pre-unshard.
    - For sharded strategies, if the `FlatParameter` does not need to be unsharded, `pre_unshard()` is a no-op. This avoids unnecessarily allocating and freeing the low precision shard.
    - For `NO_SHARD`, we simply preserve the existing semantics.
4. `FlatParamHandle.unshard(self)`
    - If the handle was resharded without freeing the padded unsharded flattened parameter (e.g. `summon_full_params()` between forward and backward when `reshard_after_forward=False`), then the `FlatParameter` points to the sharded flattened parameter. We need to switch to using the unsharded parameter. This is a design choice. Alternatively, we may not switch to using the sharded flattened parameter in `reshard()` if we do not free the padded unsharded flattened parameter. However, the postcondition that the `FlatParameter` points to the sharded flattened parameter after `reshard()` is helpful logically, so I prefer this approach.
    - Otherwise, this allocates the padded unsharded flattened parameter, all-gathers, and switches to using the unpadded unsharded flattened parameter.
    - In the future, we may add an option to `unshard()` that additionally all-gathers the gradient.
5. `FlatParamHandle.post_unshard(self, prepare_gradient: bool)`
    - For sharded strategies, if using parameter mixed precision, this frees the low precision shard. More generally, this should free any sharded allocations made in `pre_unshard()` since the all-gather has been launched. If using CPU offloading, the GPU copy of the local shard goes out of scope after `unshard()` and is able to be garbage collected. **We should understand if there is any performance difference between manually freeing versus deferring to garbage collection since our usage is inconsistent.** For now, I preserve the existing semantics here.
    - `prepare_gradient` is meant to be set to `True` for the pre-backward unshard and `False` for the forward unshard. This runs the equivalent logic of `_prep_grads_for_backward()`.
    - This post-unshard logic (notably the gradient preparation) now runs in the all-gather stream, which is fine because we always have the current stream wait for the all-gather stream immediately after `FullyShardedDataParallel._unshard()`. IIUC, we do not need to call `_mp_shard.record_stream(current_stream)` (where `current_stream` is the default stream) because `_mp_shard` is allocated and freed in the same (all-gather) stream.
    - A postcondition is that the `FlatParameter` is on the compute device. It should also have the unpadded unsharded size (though I do not have a check for this at the moment).

### Unshard: `summon_full_params()`
Now that we see how the logical unshard has been reorganized for the core code path, let us dive into `summon_full_params()`.

The two constraints are:
1. If using parameter mixed precision, we should unshard in full precision.
2. We must determine if we should free the padded unsharded flattened parameter upon exiting.

The first constraint is addressed as described before in the core unshard code path, so it remains to explore the second constraint.

I propose a simple rule: **We free iff we actually unshard the `FlatParameter` in `summon_full_params()`** (i.e. it was not already unsharded). We perform a case analysis:

**Parameter mixed precision enabled:**
* `NO_SHARD`: `flat_param.data` points to `flat_param._local_shard`, which is the full precision unsharded flattened parameter. This is **not safe to free**.
* `FULL_SHARD` / `SHARD_GRAD_OP`: We force full precision and all-gather to `_full_prec_full_param_padded`. We do not support `nested summon_full_params()`, so `_full_prec_full_param_padded` must be unallocated. We unshard, and it is **safe to free**.

**Parameter mixed precision disabled:**
* `NO_SHARD`: This is the same as with mixed precision enabled. This is **not safe to free**.
* `FULL_SHARD` / `SHARD_GRAD_OP`: We all-gather to `_full_param_padded`. It may already be unsharded.
    * Already unsharded: The unshard is a no-op. This is **not safe to free**.
        * For `FULL_SHARD`, this can happen for the root FSDP instance after `forward()` but before backward.
        * For `SHARD_GRAD_OP`, this can happen for all FSDP instances after `forward()` but before backward.
    * Needs unshard: We unshard. This is **safe to free**.

Therefore, we see that it is not safe to free when using `NO_SHARD` and when using a sharded strategy but the `FlatParameter` is already unsharded. This is precisely the proposed rule.

There were two notable edge cases that the existing code did not address.
1. The existing code tests if the `FlatParameter` is already unsharded by checking the allocation status of `_full_param_padded`. When using parameter mixed precision, this is the incorrect tensor to check. If `_full_param_padded` is allocated (e.g. when `reshard_after_forward=False` and calling `summon_full_params()` between forward and backward), the already-unsharded check is a false positive, and `summon_full_params()` does not correctly force full precision. https://github.com/pytorch/pytorch/issues/83068
    - This PR's `needs_unshard()` check correctly routes to the appropriate padded unsharded flattened parameter depending on the calling context (i.e. if it needs to force full precision or not).
2. The existing code does not free the GPU copy of the padded unsharded flattened parameter when calling `summon_full_params(offload_to_cpu=True)`. It unshards the `FlatParameter`, moves the padded unsharded flattened parameter to CPU, and sets the `FlatParameter` data to be the appropriate unpadded view into the padded unsharded flattened parameter on CPU. However, `_full_param_padded` still points to the all-gathered padded unsharded flattened parameter on GPU, which is kept in memory. https://github.com/pytorch/pytorch/issues/83076
    - This PR frees the GPU copy and reallocates it upon exiting `summon_full_params()`. This is essential for avoiding peak GPU memory usage from increasing as we recurse through the module tree. There may be some cases where we can avoid reallocation altogether, but that can be addressed in a follow-up PR.
    - This PR offloads the *unpadded* unsharded flattened parameter to CPU directly instead of the *padded* one. As far as I can tell, there is no need to include the padding since unflattening the original parameters does not require the padding.
    - The relevant code is in the context manager `FlatParamHandle.to_cpu()`.

### Unshard: Mixed-Precision Stream

This PR removes the mixed precision stream usage. As is, I do not think there is any extra overlap being achieved by the stream usage.

The low precision shard is allocated and copied to in the mixed precision stream ([code](https://github.com/pytorch/pytorch/blob/1f99bdfcc4a3f97d28471a531d2b69def762f6ba/torch/distributed/fsdp/fully_sharded_data_parallel.py#L1401-L1412)), and the current stream (in this case the all-gather stream) waits for the mixed precision stream ([code](https://github.com/pytorch/pytorch/blob/1f99bdfcc4a3f97d28471a531d2b69def762f6ba/torch/distributed/fsdp/fully_sharded_data_parallel.py#L1414)). However, we immediately schedule an all-gather that communicates that exact low precision shard ([code](https://github.com/pytorch/pytorch/blob/1f99bdfcc4a3f97d28471a531d2b69def762f6ba/torch/distributed/fsdp/fully_sharded_data_parallel.py#L3338)) with no other meaningful computation between. If we remove the mixed precision stream, the low precision shard is allocated and copied to in the all-gather stream (including the non-blocking CPU -> GPU copy if using CPU offloading).

Under this PR's design, we may consider a "pre-unshard" stream for all logical pre-unshard data transfers if we want to overlap in the future. IIUC, the overlap opportunity exists if there are multiple `FlatParameter`s per module, and we only have the all-gather stream wait for the data transfer corresponding to the local shard it communicates, not the others.

If we agree on removing the mixed-precision stream for now, I will remember to delete it from `_init_streams()`.

## FSDP Runtime: Reshard

Like with unshard, the first step is the look at the existing `_free_full_params()` and `_use_param_local_shard()`. A few notable observations:
- For only `NO_SHARD`, `_free_full_params()` includes a call to `_free_mp_shard()`.
- For `summon_full_params()`, there is a separate `_free_full_params_and_use_local_shard()` that duplicates the main logic of `_free_full_params()` and calls `_use_param_local_shard()`.
- In `forward()`, if `reshard_after_forward=True`, we call `_free_full_params()` and then `_free_mp_shard()`. Hence, for `NO_SHARD`, the `_free_mp_shard()` is a no-op.
- In the post-backward hook, we typically call `_free_full_params()` and `_free_mp_shard()`. The `_free_mp_shard()` is a no-op for `NO_SHARD` and if `reshard_after_forward=True`.

Some comments:
- The code certainly works, but some of the no-ops are subtle. When possible, we should make it clear when calls are no-ops or not. It is good that the existing code documents that `_free_mp_shard()` is a no-op in the post-backward hook when `reshard_after_forward=True`. However, there are still some non-obvious no-ops (around `NO_SHARD`).
- We should see if we can avoid the duplicate `_free_full_params_and_use_local_shard()`.

Let us trace through the logical reshard:
1. `FullyShardedDataParallel._reshard(self, handles: List[FlatParamHandle], free_unsharded_flat_params: List[bool])`
    - The two args should have the same length since they are to be zipped.
    - The goal of having `free_unsharded_flat_params` is that the caller should be explicit about whether the (padded) unsharded flattened parameter should be freed. The low precision shard is always meant to be freed (as early as possible), so there is no corresponding `List[bool]`.
2. `FlatParamHandle.reshard(self, free_unsharded_flat_param: bool)`
    - This frees the (padded) unsharded flattened parameter if `free_unsharded_flat_param` and switches to using the sharded flattened parameter.
    - Echoing back to forcing full precision in `summon_full_params()`, `_free_unsharded_flat_param()` frees the correct tensor by using `_get_padded_unsharded_flat_parameter()`.
3. `FlatParamHandle.post_reshard(self)`
    - I am not fully content with the existence of this method, but this seems to be an unavoidable consequence of `NO_SHARD`. Perhaps, this may be useful in the future for other reasons though.
    - Right now, this method is only meaningful for `NO_SHARD` + parameter mixed precision + outside `summon_full_params()`. `_mp_shard` is not freed in the post-unshard since it is also the low precision _unsharded_ flattened parameter, so we must delay the free until the the post-reshard.

Below the `FlatParamHandle.reshard()` and `post_reshard()` layer, there should not be any no-ops.

One final comment I will mention is that I like the `pre_unshard()`, `unshard()`, `post_unshard()`, and `reshard()`, `post_reshard()` organization because it makes it clear what the boundaries are and their temporal relationship. Through that, we can set pre- and post-conditions. Furthermore, we can eventually convert logic to hooks that may be registered on the `FlatParamHandle` (for `pre_unshard()`, `post_unshard()`, and `post_reshard()`). This may improve the customizability of FSDP.

 ## FSDP Runtime: `forward()`

- This PR reorganizes `forward()` in preparation for non-recursive wrapping, which uses pre-forward and post-forward hooks that expect the signature `hook(module, input)`. For FSDP, the `module` and `input` arguments are not used.
- This PR creates a new method `_fsdp_root_pre_forward()` to handle the logic only the root FSDP should run.

## FSDP Prefetching

Finally, we dive into the prefetching changes. Some highlights:
1. This PR unifies the execution order validation and prefetching implementations.
    - Both involve the execution order and can be unified to share some boilerplate.
2. Execution order validation only runs when the distributed debug level is `INFO`.
    - We have yet to have one success case where we actually catch an unintended source of dynamism. The warning is also too verbose. Hence, we are gating it by the `INFO` level.
3. This PR moves prefetching to be with respect to groups of handles (as mentioned in the constructor comment).
    - This is essential for supporting prefetching with non-recursive wrapping.
4. This PR does not include "bubbles", i.e. modules with no handles, in the recorded execution order(s). This deviates from the existing implementation.
    - This makes prefetching possibly more aggressive (when there are such bubbles), but it should not have significant performance implications either way.
5. This PR changes backward prefetching to reset the post-forward order each iteration (as intended).
6. This PR changes forward prefetching to use the first iteration's pre-forward order instead of the first iteration's post-forward order. (We can discuss whether we want this in this PR or not. Otherwise, I can keep it as using the post-forward order to preserve the existing semantics.) This PR also removes the `all_gather_stream.wait_stream(current_stream)` before forward prefetching because it does not help with high GPU reserved memory. We can add that back if desired.

### Appendix
#### Reverse Post-Forward Order Is Not Always the Pre-Backward Order
The existing PT-D FSDP pre-backward prefetching uses the reverse post-forward order.
<details>
  <summary>Model Code</summary>

  ```
  class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.block1 = nn.Sequential(
            nn.Conv2d(3, 4, kernel_size=3),
            nn.BatchNorm2d(4),
            nn.ReLU(inplace=True),
        )
        self.block2 = nn.Sequential(
            nn.Conv2d(4, 4, kernel_size=3),
            nn.BatchNorm2d(4),
            nn.ReLU(inplace=False),
        )
        self.block3 = nn.Linear(12, 8)
        self.head = nn.Sequential(
            nn.AdaptiveAvgPool2d(output_size=(1, 1)),
            nn.Flatten(),
            nn.Linear(4, 10),
        )

    def forward(self, x):
        x = self.block1(x)
        x = self.block2(x)
        x = self.block3(x)
        return self.head(x)

  model = Model().cuda()
  fsdp_kwargs = {}
  model.block1[1] = FSDP(model.block1[1], **fsdp_kwargs)  # BN2d
  model.block2[1] = FSDP(model.block2[1], **fsdp_kwargs)  # BN2d
  model.block1 = FSDP(model.block1, **fsdp_kwargs)
  model.block2 = FSDP(model.block2, **fsdp_kwargs)
  model.block3 = FSDP(model.block3, **fsdp_kwargs)
  model = FSDP(model, **fsdp_kwargs)
  ```
</details>

<details>
  <summary>Execution Orders </summary>

  ```
  Pre-backward hook for ('head.2.weight', 'head.2.bias') 140339520587136 (model)
  Pre-backward hook for ('weight', 'bias') 140339461194656 (block3)
  Pre-backward hook for ('0.weight', '0.bias') 140339520589776 (block2)
  Pre-backward hook for ('weight', 'bias') 140339520587664 (block2 BN)
  Pre-backward hook for ('weight', 'bias') 140339520586656 (block1 BN)
  Pre-backward hook for ('0.weight', '0.bias') 140339520588768 (block1)

  Pre-forward order:
  ('head.2.weight', 'head.2.bias') 140339520587136 (model)
  ('0.weight', '0.bias') 140339520588768 (block1)
  ('weight', 'bias') 140339520586656 (block1 BN)
  ('0.weight', '0.bias') 140339520589776 (block2)
  ('weight', 'bias') 140339520587664 (block2 BN)
  ('weight', 'bias') 140339461194656 (block3)

  Reverse post-forward order:
  ('head.2.weight', 'head.2.bias') 140339520587136 (model)
  ('weight', 'bias') 140339461194656 (block3)
  ('0.weight', '0.bias') 140339520589776 (block2)
  ('weight', 'bias') 140339520587664 (block2 BN)
  ('0.weight', '0.bias') 140339520588768 (block1)
  ('weight', 'bias') 140339520586656 (block1 BN)
  ```
</details>

Differential Revision: [D39293429](https://our.internmc.facebook.com/intern/diff/D39293429)
Pull Request resolved: https://github.com/pytorch/pytorch/pull/83665
Approved by: https://github.com/zhaojuanmao

---
## [facebook/hhvm](https://github.com/facebook/hhvm)@[5d2299c8aa...](https://github.com/facebook/hhvm/commit/5d2299c8aab8378db96447b1f3918d4a9e5cf79d)
#### Tuesday 2022-09-20 19:40:40 by Hunter Goldstein

Relax type checks for using array like interfaces in native function signatures

Summary:
This diff updates the interpreter and JIT to interpret array like interfaces (`Traversable` et al) as being unchecked types for native functions.

I'd like to write the `dict` / `vec` / `keyset` functions in a way that preserves the input typing for the sake of typing the rest of systemlib. The current signatures are a a pain to work through (especially for `ext_collection-map.php`) and are scattering a ton of unnecessary FIXMEs / UNSAFE_CASTs

The options I've considered are:
* The current diff: hacking HHVM to understand the interfaces. This feels somewhat fragile, but I don't think it's any more fragile than the current state of the world, where a magic interface is implemented by value types.
* Hide these definitions from the typechecker using something like `__PHPStdLib` and present HHI definitions that are suitable: this is my main alternative if this solution isn't acceptable. It's spiritually correct in that these constructors are effectively pseudofunctions (they're compiled to bytecodes when used directly). I find this *about as hacky* as the current soln, it's just relying on hack-y-ness in the typechecker rather than in the runtime.
* Delete the relevant functions and rely solely on HHIs: this would be possible, and probably optimal, if I had signal that these functions aren't dynamically invoked (h/t periodic1236). Unfortunately, all systemlib symbols are implicitly dynamically callable.

Reviewed By: alexeyt, edwinsmith

Differential Revision: D37868168

fbshipit-source-id: c83a6bca23c710eb1caf88b991153ebe06788ed9

---
## [aospa-op5t/kernel_oneplus_msm8998](https://github.com/aospa-op5t/kernel_oneplus_msm8998)@[5e237c6f26...](https://github.com/aospa-op5t/kernel_oneplus_msm8998/commit/5e237c6f2609f14e269298644155c1f208be9107)
#### Tuesday 2022-09-20 20:01:08 by Christian Brauner

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

---
## [laminas/laminas-xmlrpc](https://github.com/laminas/laminas-xmlrpc)@[f2dd95c53f...](https://github.com/laminas/laminas-xmlrpc/commit/f2dd95c53f66d0e8c4972e3c7d240b27fe7fe20c)
#### Tuesday 2022-09-20 20:11:02 by Michał Bundyra

Message against the war, in Russian and English

🇷🇺 Русским гражданам

Мы, участники Laminas, родились и живем в разных странах. У многих из нас есть друзья, родственники и коллеги как в России, так и в Украине. Некоторые из нас родились в России. Некоторые из нас живут в России. У некоторых бабушки и дедушки сражались с фашистами во Второй мировой войне. Здесь никто не поддерживает фашизм.

У одного из нас есть украинская родственница, которая спаслась из дома вместе с сыном. Поезд задержался из-за бомбежки на дороге впереди. У нас есть друзья, которые прячутся в бомбоубежищах. Мы с тревогой ждем весточки от них после воздушных налетов, которые беспорядочно наносят удары и попадают по больницам, школам, детским садам и домам. Мы не берем это из каких-либо СМИ. Мы наблюдаем это напрямую.

Вы доверяете нам достаточно, чтоб использовать наши программы, и мы просим вас довериться нам вновь. Мы нуждаемся в помощи. Выходите и протестуйте против этой бесполезной войны. Остановите кровопролитие. Скажите "Нет войне!"

🇺🇸 To Citizens of Russia

We at Laminas come from all over the world. Many of us have friends, family and colleagues in both Russia and Ukraine. Some of us were born in Russia. Some of us currently live in Russia. Some have grandparents who fought Nazis in World War II. Nobody here supports fascism.

One team member has a Ukrainian relative who fled her home with her son. The train was delayed due to bombing on the road ahead. We have friends who are hiding in bomb shelters. We anxiously follow up on them after the air raids, which indiscriminately fire at hospitals, schools, kindergartens and houses. Were not taking this from any media. These are our actual experiences.

You trust us enough to use our software. We ask that you trust us to say the truth on this. We need your help. Go out and protest this unnecessary war. Stop the bloodshed. Say "stop the war!"

Signed-off-by: Michał Bundyra <contact@webimpress.com>

---
## [postgres/postgres](https://github.com/postgres/postgres)@[1c27d16e6e...](https://github.com/postgres/postgres/commit/1c27d16e6e5c1f463bbe1e9ece88dda811235165)
#### Tuesday 2022-09-20 22:03:47 by Tom Lane

Revise tree-walk APIs to improve spec compliance & silence warnings.

expression_tree_walker and allied functions have traditionally
declared their callback functions as, say, "bool (*walker) ()"
to allow for variation in the declared types of the callback
functions' context argument.  This is apparently going to be
forbidden by the next version of the C standard, and the latest
version of clang warns about that.  In any case it's always
been pretty poor for error-detection purposes, so fixing it is
a good thing to do.

What we want to do is change the callback argument declarations to
be like "bool (*walker) (Node *node, void *context)", which is
correct so far as expression_tree_walker and friends are concerned,
but not change the actual callback functions.  Strict compliance with
the C standard would require changing them to declare their arguments
as "void *context" and then cast to the appropriate context struct
type internally.  That'd be very invasive and it would also introduce
a bunch of opportunities for future bugs, since we'd no longer have
any check that the correct sort of context object is passed by outside
callers or internal recursion cases.  Therefore, we're just going
to ignore the standard's position that "void *" isn't necessarily
compatible with struct pointers.  No machine built in the last forty
or so years actually behaves that way, so it's not worth introducing
bug hazards for compatibility with long-dead hardware.

Therefore, to silence these compiler warnings, introduce a layer of
macro wrappers that cast the supplied function name to the official
argument type.  Thanks to our use of -Wcast-function-type, this will
still produce a warning if the supplied function is seriously
incompatible with the required signature, without going as far as
the official spec restriction does.

This method fixes the problem without any need for source code changes
outside nodeFuncs.h/.c.  However, it is an ABI break because the
physically called functions now have names ending in "_impl".  Hence
we can only fix it this way in HEAD.  In the back branches, we'll have
to settle for disabling -Wdeprecated-non-prototype.

Discussion: https://postgr.es/m/CA+hUKGKpHPDTv67Y+s6yiC8KH5OXeDg6a-twWo_xznKTcG0kSA@mail.gmail.com

---
## [TemperanceTempy/lobotomy-corp13](https://github.com/TemperanceTempy/lobotomy-corp13)@[f0e6476eb0...](https://github.com/TemperanceTempy/lobotomy-corp13/commit/f0e6476eb051d781f7e4d0be7976dff0ff72fda0)
#### Tuesday 2022-09-20 22:44:25 by Lance

The Great Workening

Attribute Levels Displayed

No thoughts were had, thoughts injected.

Attribute Levels go brrr

Requested Change Made

WHOOPS WRONG PARENTHESIS

I swear I know how Clamps work

Holy shit how did this not get found out earlier

---
## [jonbell-lot23/devtools](https://github.com/jonbell-lot23/devtools)@[9dc23c2b4d...](https://github.com/jonbell-lot23/devtools/commit/9dc23c2b4dc82ac980e5d4d73eac9ea96ef30813)
#### Tuesday 2022-09-20 23:35:34 by Josh Morrow

Refine focus region based on received points

I'm not sure how this particular feature never got in. I remember
thinking last time I was working on focus stuff that we should do it,
but I guess I never actually got around to doing it. The idea is
relatively simple:

Sometimes the user asks for a focus region in which our known timeline
is sparse. We do our best to get them an accurate window, but it's tough
because points are few and far between. But there is *good* news there,
which is that we can't display anything incorrectly, because we don't
know about anything in the sparse ranges (that's why they are sparse).

But, then the trouble starts. The user has chosen a window, and they
start doing things like settings breakpoints. We are filling in our
sparse timeline! But sometimes those points actually fall *between* the
displayed end of the focus region and real end of the window for which
we are currently making requests. When this happens, you get
funny-looking results, like analysis points hanging out in regions that
look unloaded. The solution is actually relatively simple. When we are
focused and we discover new points, we check to see if any of those
points could be used to make a more refined focus window. If so, we just
update our focus window. No additional interactions with the backend are
required, and if we have a really dense analysis, that's fine, because
it just means we will get even *more* accurate information about the
point <-> time relationship in that region.

---
## [JoyfulKoinu/CA](https://github.com/JoyfulKoinu/CA)@[bdf5772e97...](https://github.com/JoyfulKoinu/CA/commit/bdf5772e9785e9db453aa2f9b19cf1c324af2ab3)
#### Tuesday 2022-09-20 23:44:10 by JoyfulKoinu

Fixed Neko Night Vision being a BITCH

bitch boy fix yo shit

---

