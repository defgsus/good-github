## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-08-09](docs/good-messages/2022/2022-08-09.md)


2,029,593 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,029,593 were push events containing 3,099,897 commit messages that amount to 247,148,177 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 26 messages:


## [PolyhedronStudio/Polyhedron-Engine](https://github.com/PolyhedronStudio/Polyhedron-Engine)@[644c0feb69...](https://github.com/PolyhedronStudio/Polyhedron-Engine/commit/644c0feb699a38b71348aa20a4de01a2ef0e1ce7)
#### Tuesday 2022-08-09 00:19:35 by WatIsDeze

Removed remnants of ServerGame Physics, including:
StepMove, it has grown obsolete , and it was left behind in a broken state anyhow. RootMotion now takes its place. Will implement a SlideBox method for other needs to replace that which RootMotion can't. (Take MiscExplosionBox for example.)

Fixed FuncDoor not displaying messages and added support for Use Key Toggling doors to Open/Close them at will. (If you find a hard time imagining this, think Half-Life.)

Disabled playermove debugging, we're done with that for now. (Other than the extremely minor nudge in rare literally corner cases.)

Re-enabled weapon attachment for the testdummies. This code still needs some extra API work to be nice and game module friendly.

---
## [Tastyfish/-tg-station](https://github.com/Tastyfish/-tg-station)@[5dc17bd865...](https://github.com/Tastyfish/-tg-station/commit/5dc17bd86556c01cc0f81f54a6ce270169c00088)
#### Tuesday 2022-08-09 00:38:25 by san7890

Security's Scaling Departmental Accesses - More Pop, More Problems (#68534)

lternative to #68527
About The Pull Request

Hey there,

This is an alternative PR that I concocted based on talking with Goof on that PR. Basically, we already have a nicely complicated system to track and balance the number of security officers we have in a shift based on some config coefficient setting, by which we can set the amount of lockers that spawn in on the start of a round, as well as determine truly how many security officers we have.

image

So, I've decided to leverage this in another way. Basically, based on the number of security officers in a shift, their specific departmental officers will also get more (elevated) accesses. They already start with a certain amount of access, but they can get more if it is a low-pop shift with the mechanic introduced in this PR. For example, an Engineering Security Officer can access Atmospherics and Engineering departments by default, but they can't access Telecommunications unless there is a lower population of players AT SHIFT START. Same for a Medical Security Officer accessing Medbay, but not Plumbing.

Update: I have made it such that there are three system that server operators can set:

They can use the Scaling System that operates in the same method outlined in the rest of the PR.
They can disable giving departmental security officers "elevated access" (such as access beyond the "front doors") to these officers.
Finally, they can also just always ensure that departmental security officers get the maximal accesses possible.

The default setting is the "Scaling System" outlined in this PR, which is already dependent on the general Security Officer Scaling Co-Efficient.
Why It's Good For The Game

I think it's better to involve some more nuanced config scaling that we already have present in the game. The major theme that we want to avoid is that departmental security officers having maximal accesses when there is an already large number of persons on the security force will result in "miserable" shifts for the common person working within a department (security metaprotections). However, some server operators (as well as server cultures) tend to have very wide ranges in how many security officers they have on a shift-by-shift basis. One day, you could have 0-2 security officers, the next, you could have 4-6. It's all variable on who's playing (as always). There is also a significant variation between server to server in regards to how many security officer slots you tend to have on spawn, but this is already manageable by the security officer co-efficient in config.

I believe this PR is an acceptable proposal within the bounds of #68527 (comment) , although it may bend certain aspects of it, I definitely do see where some people may be coming from. I believe I've adjusted the accesses to a "sane"/justifiable amount, but I'll come back to think on everything.

"Red-tiding" may or may not be a problem, but there's always just going to be something inherently silly with a security officer being able to walk into plumbing to start plumbing. I hoped that this would be seen as a positive as opposed to a negative, but I can see how it could negatively impact player experience. HOWEVER, interplayer experience should not be handled by the codebase in all aspects, which is why I've also passed in the associated config variables, so that server operators (who should handle the interplayer experience with their level of discretion and nuance) can.
What accesses are where?

The general philosophy as I thought through designing this would be that the security officer should at the very least have general "front-door" access into a department, and maybe something benign. If we had even more per-door accesses, this could definitely be a bit more granular (one example I can think of would only atmospherics technicians having access to the "Pump Room", while Security Officers would not. However, this is for a later date). So, you have the "default" access you always get, and a potential to get "elevated" access as a Departmental Security Officer.

The balances are as such:

The Cargo Security Officer will have access to the Cargo Bay, Mining Section, and the Shipping Room. The first two are rather general areas, with the Shipping Room being a rather good help for rescuing (or "rescuing") flushed crewmembers when the cargo techies can't get to it/no AI. The Auxiliary Base is not essential to the security officer's functions, and the mining station helps restrict access further on stations like IceBox. This would also grant them extra access to the Lavaland base, so let's snip that out.

The Engineering Security Officer should have access to only general Engineering and Atmospherics. Construction pertains to certain rooms in maintenance I believe, and Engine-Equipment should be the one that grants access to APCs (lol). I don't think a security officer should have the latter one to be honest, but I think we'll be stretching the scope of this PR. Telecommunications is a bit weird, it's a critical station function, but I think you also shouldn't be able to nick one goon's ID and have access, so let's give it to them only when it's "needed".

The Medical Security Officer should have access to only the general Medbay Area and the Morgue, in case someone starts trotting on the doctor's turf, or if there's someone doing unsavory things to the bodies while the doctors are away. They will not have access to the specialized (dangerous) areas unless the ratio of secoffs to the population is low enough should it necessitate it (Plumbing Room, Pharmacy, Virology). I also added Surgery to the scaling access, but I'm iffy on that one. I don't particularly see why they should have it as a base access, but I also do see there being some need in dire straits (in relation to helping people, not tiding).

The Science Security Officer definitely got a huge cut. They now only have general access to R&D and normal scientist areas like the lathe room, circuits lab (presumably)since these are generally trafficked areas, but I definitely clamped down on additional access they might get in a "normally balanced" situation (no ordnance+storage, no xenobio, no genetics, no to robotics, etc.) They don't have a particular use in these areas and can even be a bit obstructive to flow in normal circumstances, but if abnormal circumstances arise and there's not a lot of security hands-on-deck, then their access is expanded.

Honestly, balancing this both makes sense and is conversely rather odd. I'm just running off what we already hold to be true and expected (or at least as of the last two months), and we can go from there.
Changelog

cl
balance: Nanotrasen realized that the more access they had on their cards was costing them a pretty penny, so they trimmed back the number of accesses a certain departmental Security Guard might have. However, any given guard will get back a greater amount of accesses depending on how many security guards there are in relation to the population.
config: Hey server operators, listen! We've changed up how Departmental Security Officers get their accesses, so be sure to review the DEPSEC_ACCESS_LEVEL config number to see what you want to work best for your server.
/cl

Also, every single line of code found in 4533f07 that is now presently in this PR is deliberate

---
## [kleinerm/Psychtoolbox-3](https://github.com/kleinerm/Psychtoolbox-3)@[9354870474...](https://github.com/kleinerm/Psychtoolbox-3/commit/9354870474eaff17302039fc07d6248c9ee5bace)
#### Tuesday 2022-08-09 01:58:07 by Mario Kleiner

PsychHID/OSX: Improve macOS security troubleshooting instructions.

Sometimes macOS shitty security GUI lies about the permission status
of "Input Monitoring" etc., and displays Matlab/Octave/Terminal as
on the list and checked, and one does need to do more stupid stuff
like unchecking or rechecking the checkbox. Add comments regarding
this.

---
## [dcoliversun/spark](https://github.com/dcoliversun/spark)@[c4c623a3a8...](https://github.com/dcoliversun/spark/commit/c4c623a3a890267b2f9f8d472c8be30fc5db53e1)
#### Tuesday 2022-08-09 02:16:13 by Hyukjin Kwon

[SPARK-39869][SQL][TESTS] Fix flaky hive - slow tests because of out-of-memory

### What changes were proposed in this pull request?

This PR adds some manual `System.gc`. I know enough that this doesn't guarantee the garbage collection and sounds somewhat funny but it works in my experience so far, and I did such hack in some places before.

### Why are the changes needed?

To deflake the tests.

### Does this PR introduce _any_ user-facing change?

No, dev and test-only.

### How was this patch tested?

CI in this PR should test it out.

Closes #37291 from HyukjinKwon/SPARK-39869.

Authored-by: Hyukjin Kwon <gurwls223@apache.org>
Signed-off-by: Hyukjin Kwon <gurwls223@apache.org>

---
## [Zonespace27/Skyrat-tg](https://github.com/Zonespace27/Skyrat-tg)@[f0cef47678...](https://github.com/Zonespace27/Skyrat-tg/commit/f0cef47678384716080d4cc2adfa8be85b9ddc69)
#### Tuesday 2022-08-09 03:00:48 by SkyratBot

[MIRROR] Adds the Mothroach [MDB IGNORE] (#15399)

* Adds the Mothroach (#68763)

About The Pull Request

Yup. That's pretty much it. This PR adds the Mothroach to the game, described as "An ancient ancestor of the moth that surprisingly looks like the crossbreed of a moth and a cockroach."

Do you love the Mothroach? Then you can cuddle with it and pat it, as well as place it on your head for extra cuteness.
What if you hate it, though? You can always kill and butcher Mothroaches in order to mass produce moth plushes for your own profit... How fun!

Either way, you win!

The Mothroach can be picked up and has a special on-head sprite (which looks really cute). It is able to vent-crawl and you may get one by randomly summoning a friendly mob through the gold slime extracts, or by ordering one through the Cargo Requests. After butchered, you may use its hide, a heart, and some cloth to craft a moth plushie, the most devilish of Devil's designs.

Full Preview of all the Sprites (NEW): https://www.youtube.com/watch?v=pdg8FTNEYjI
Preview of some of the Sprites (OLD): https://www.youtube.com/watch?v=9A-8hGCiW0s
In-hand, on-head, and grounded Mothroach sprite credits go to ValuedEmployee.
I did the Mothroach hide sprite though!
Why It's Good For The Game

The Mothroach is incredibly cute and a neat, fresh, new piece of content. Although it could use some future repurposing, right now it's simply a cute exotic pet with a few interactions.

These cute sprites are just too good to go to waste...

I keep seeing people complain about the lack of new content. Well, here's something niche that won't break the whole balance of the game and that will be cute. I seriously cannot see a motive not to add this to the game. Just because it isn't a powergaming tool or something that is seen every shift, that doesn't mean that it won't have a positive influence on the game. As I have stated, right now the Mothroaches are underperforming in terms of interactions and ways of getting them, but adding them is the first step to later improve them.
Changelog

cl
add: The Mothroach, your new local exotic pet
add: Mothroach Hide and Mothroach Meat
add: New crafting recipe for the Moth Plush: 1 Mothroach Hide; 1 heart; 3 cloth
fix: Fixes dead mobs on-head not having sprites
/cl

* Adds the Mothroach

Co-authored-by: Justice <42555530+Justice12354@users.noreply.github.com>

---
## [WillNilges/pubsite](https://github.com/WillNilges/pubsite)@[a9d3afdf2b...](https://github.com/WillNilges/pubsite/commit/a9d3afdf2b41102d645ccc4d4f197861c99a92e0)
#### Tuesday 2022-08-09 03:22:55 by Will Nilges

God fucking fuck shit cock fuck

Co-authored-by: Ethan Ferguson <ethanf108@gmail.com>

---
## [uber/cadence](https://github.com/uber/cadence)@[add4b390ad...](https://github.com/uber/cadence/commit/add4b390ada43fdd8167f06e209ae6ece0d11aaa)
#### Tuesday 2022-08-09 03:54:12 by Steven L

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
## [derpguy125/CaveTest31](https://github.com/derpguy125/CaveTest31)@[5882edefcb...](https://github.com/derpguy125/CaveTest31/commit/5882edefcbd32444ec76ceb8b7c7b89766b65cea)
#### Tuesday 2022-08-09 04:24:25 by DG

yeah this is stupid

i have no idea how to do that back to the object based shit

even if it is inefficient

---
## [Pink-Chink/sojourn-station](https://github.com/Pink-Chink/sojourn-station)@[c3c08d0946...](https://github.com/Pink-Chink/sojourn-station/commit/c3c08d0946fd0ebde1dd9b5cc5ab8781a544487c)
#### Tuesday 2022-08-09 05:11:32 by nikothedude

Ports moveSS from TG (#3771)

* p

* fucker

* fuckin

* fuckin!!!!

* commit time

* hell yeah

* FUCKING. TG

* groan

* fuvkin

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[3d2f96a930...](https://github.com/git-for-windows/git/commit/3d2f96a930d8ba68326260289a3d5511560281ce)
#### Tuesday 2022-08-09 08:17:45 by brian m. carlson

builtin/stash: provide a way to export stashes to a ref

A common user problem is how to sync in-progress work to another
machine.  Users currently must use some sort of transfer of the working
tree, which poses security risks and also necessarily causes the index
to become dirty.  The experience is suboptimal and frustrating for
users.

A reasonable idea is to use the stash for this purpose, but the stash is
stored in the reflog, not in a ref, and as such it cannot be pushed or
pulled.  This also means that it cannot be saved into a bundle or
preserved elsewhere, which is a problem when using throwaway development
environments.

Let's solve this problem by allowing the user to export the stash to a
ref (or, to just write it into the repository and print the hash, à la
git commit-tree).  Introduce git stash export, which writes a chain of
commits where the first parent is always a chain to the previous stash,
or to a single, empty commit (for the final item) and the second is the
stash commit normally written to the reflog.

Iterate over each stash from topmost to bottomost, looking up the data
for each one, and then create the chain from the single empty commit
back up in reverse order.  Generate a predictable empty commit so our
behavior is reproducible.  Create a useful commit message, preserving
the author and committer information, to help users identify stash
commits when viewing them as normal commits.

If the user has specified specific stashes they'd like to export
instead, use those instead of iterating over all of the stashes.

As part of this, specifically request quiet behavior when looking up the
OID for a revision because we will eventually hit a revision that
doesn't exist and we don't want to die when that occurs.

Signed-off-by: brian m. carlson <sandals@crustytoothpaste.net>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [sbuzonas/hhvm](https://github.com/sbuzonas/hhvm)@[648c963897...](https://github.com/sbuzonas/hhvm/commit/648c963897f25839c9d1697939acaf8762a64978)
#### Tuesday 2022-08-09 11:18:34 by Lucian Wischik

mitigate HackIDE:idle messages

Summary:
There are two separate things going on with this diff. Both are prompted by a user repro where the progress-message "[HackIDE:idle]" keeps popping up.

**Fewer IDE_IDLE**. The behavior of hh_server is, if it receives an RPC from clientLsp, then it must receive a subsequent IDE_IDLE message from clientLsp before it will do any typechecking. It does this because it takes ~1s for hh_server to wind down a typecheck and then start one up again, which made things clunky and slow when you were doing a lot of typing and interrupting a typecheck with every keystroke you made. The design is that IDE_IDLE only gets sent after the LSP queue has been emptied.

We had accidentally gotten this code wrong at times, so that sometimes the IDE_IDLE message didn't get sent and hence hh_server got permanently stuck, but that seems to have been fixed for a year or more. The final robust design was that for every single event (other than "tick" meaning no-event), then clientLsp would believe it needed to send IDE_IDLE.

This became a bit inessential with clientIdeDaemon, where we'd send IDE_IDLE even after clientIdeDaemon had handled a hover request all by itself, but wasn't too bad.

It became downright frustrating with streaming-IDE-errors, where hh_server sends error updates while a typecheck is underway. Every single one of these counted as an event, which prompted the catch-all robust design to think it needed to send an IDE_IDLE, so it did, which caused hh_server to interrupt then restart its typechecking for ~1s to deal with this message. DOH!

This diff changes clientLsp so that we only think we need to send IDE_IDLE after having sent some kind of message to hh_server (apart from sending IDE_IDLE to hh_server).

**Unclear status**. When hh_server received and processed IDE_IDLE, then it would update progress.PID.json accordingly, and the command-line hh_client would display the progress message [HackIDE:idle]. But then it takes ~1s for bulk typechecking to resume, we're not going to display any progress message until it does, so users just see [HackIDE:idle] even when they know there's a lot of typechecking to do and they just wish it would get on with it. This is confusing to us on the hack team, and to users.

This diff makes a minor change. It now displays [HackIDE:idle] while it embarks upon handling this request, and [HackIDE:idle done] after it's finished. In this way, we on the hack team will at least know that the "idle" command-handling is done, and what we're witnessing is the ~1s it takes to resume after the interruption.

(I think it's good that users and we on the hack team will know WHICH interruption is the cause for the ~1s resumption that we're seeing.)

Did all these interruptions cause actual slowness in overall typechecking time? -- not that I could reasonably measure, not within the bounds of noise.

Reviewed By: CatherineGasnier

Differential Revision: D36392047

fbshipit-source-id: 245f22eb33e9aeb034f8a7a193f3c941ed257610

---
## [microsoft/terminal](https://github.com/microsoft/terminal)@[9ccd6ecd74...](https://github.com/microsoft/terminal/commit/9ccd6ecd744890b856f3d8a39ff0616c0e34d4fb)
#### Tuesday 2022-08-09 12:52:41 by Mike Griese

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
## [thisdot/sentry](https://github.com/thisdot/sentry)@[87ac32cda7...](https://github.com/thisdot/sentry/commit/87ac32cda77656ec7dc8107bdd47be8a6b950286)
#### Tuesday 2022-08-09 13:24:54 by Ryan Albrecht

bug(ui): Fix TextOverflow when there are special characters at the end of the string (#37304)

Add `<bdi>` to better support special characters with `ellipsisDirection="left"`.

Tested in Firefox, Chrome and Safari. Notes below.

| | Before  | After |
| ------------- | ------------- | ------------- |
| Firefox | <img width="325" alt="Screen Shot 2022-08-01 at 11 46 22 AM" src="https://user-images.githubusercontent.com/187460/182221723-0c72dc45-bfab-4cfc-85df-f8e18c43bc5a.png"> | <img width="325" alt="Screen Shot 2022-08-01 at 11 45 38 AM" src="https://user-images.githubusercontent.com/187460/182221754-6efe79c1-47b1-4964-acb3-54f3b5132780.png"> |
| Chrome | <img width="325" alt="Screen Shot 2022-08-01 at 11 46 27 AM" src="https://user-images.githubusercontent.com/187460/182221799-20e4920c-dab0-4199-a761-c0fba6e02414.png"> | <img width="325" alt="Screen Shot 2022-08-01 at 11 45 45 AM" src="https://user-images.githubusercontent.com/187460/182221824-51512451-195d-42b3-8792-a615c8c45f6b.png"> |
| Safari | <img width="325" alt="Screen Shot 2022-08-01 at 11 46 14 AM" src="https://user-images.githubusercontent.com/187460/182221858-e4dd6af6-05af-4ce3-8283-884bb3525b8e.png"> | <img width="325" alt="Screen Shot 2022-08-01 at 11 45 30 AM" src="https://user-images.githubusercontent.com/187460/182221907-8f549661-fcfa-42fc-8767-b2fdb6199db8.png"> |


**All Browsers** in the 'before' screens would render special characters at the front of the string when `ellipsisDirection === 'left'` is true:

- Before: you'd see `/https://example.com/foo` which is not overflowing, but looks funny
- Before: you'd see `…/example.com/foo` which is missing the trailing slash, it's moved to the front and hidden
- After you'll see `https://example.com/foo/` without the overflow
- After you'll see `…example.com/foo/` with the trailing slash in it's correct spot.


**Safari** before wasn't cutting off the start of the string:

- Before you'd see: `…https://example.co`
- After it's still the same.


To date we're only using `ellipsisDirection="left"` for two purposes:
- Releases: used for eliding the `Package` name (two callsites)
- My new "don't call it a breadcrumb" breadcrumb component that truncates urls
    - https://github.com/getsentry/sentry/pull/37038
    - <img width="967" alt="181337211-b330496b-95fc-474e-8354-66bad35a532c" src="https://user-images.githubusercontent.com/187460/182227905-6a66e399-ebbe-4656-8ed7-2644a3e81a65.png">
 
In-App examples:

Here's a look at a new area inside sentry.io where we're listing the urls that the user visited, truncating on the left side. 

Before this change the trunaction moved those special characters to the left, which makes the urls look funny:
<img width="528" alt="Screen Shot 2022-08-04 at 10 53 23 AM" src="https://user-images.githubusercontent.com/187460/182918317-fc5f347e-127f-4888-a880-ee605f93dd26.png">

The intention is that if the strings are long they will be truncated on the left side, like this:
<img width="504" alt="Screen Shot 2022-08-04 at 10 53 48 AM" src="https://user-images.githubusercontent.com/187460/182918566-c970342b-a481-4561-ad17-62681b0d2d7a.png">

---
## [laminas/getlaminas.org](https://github.com/laminas/getlaminas.org)@[4556ac2f60...](https://github.com/laminas/getlaminas.org/commit/4556ac2f60256ac1b977d6a1a05093e15f521296)
#### Tuesday 2022-08-09 15:46:20 by Michał Bundyra

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
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[d364577827...](https://github.com/mrakgr/The-Spiral-Language/commit/d364577827c5aed60419705ff1148988b33249c4)
#### Tuesday 2022-08-09 15:49:17 by Marko Grdinić

"12:10pm. I think at this rate, the Singularity won't happen even by 2045. Maybe it is my personal circumstances that are making me biased, but you'd expect the situation to be more in my favor if the Singularity really was destined to be. My latest attempt of offering to make the Spiral backend for Tenstorrent chips has had the reception of a roadkill. It feels like it is a dead creature in the middle of the road while the people there toe around it.

Some dramatic hardware breakthrough to fulfil the promise of memristors in the previous decade is necessary to make me more optimistic. Right now it is not even on the horizon for me. Once it happens, how long would it take to put into production. Half a decade most likely.

12:20pm. I do not know what the right choice is here. Suppose I had advance knowledge telling me the Singularity will never arrive in my lifetime.

I'd probably just be a writer then and spend my life in this room playing games and reading manga. If I could get an advanced piece of hardware, then I would not have wasted time. I'd get any job, I'd even accept the 2.5k offer like the one by Zenna just to get my hands on it.

Right now the AI chips are weird. They are kind of weak and behind GPUs, being hawked only to rich people and hard to get ahold of, as well as difficult to program.

12:25pm. That I did not accept the 2.5k/month offer by Zenna, is that not proof enough that I do not believe in them?

12:30pm. The role I took upon myself is that of a pursuer, but once I stopped believing, it became a burden. I needed to believe, but I could only put on an act.

Imagine if I had the option of getting a local job for something like 1k/month. I could work for 2 months and then have the option of buying an AI chip costing 2k. If I had that 2k, I absolutely wouldn't spend it on something like AI chips. Right now it feels like it would be a complete waste of money.

For something like a brain core from the story, the amount of effort I would put in to get it would have no limit. Even if I had to work 2 years washing dishes, I would do it just to get it without any hesitation.

12:35pm. I need something to sweeten the pot for me. Maybe some algorithmic discovery. Some new insights. Just having a mediocre step up in hardware would not be enough to really fire me up.

Having Spiral be adopted by a company like Tenstorrent, and even having it sponsor its development and my own projects would be cool, but it is secondary to what I need to do.

I need something to give me a leg up on RL.

Having the hardware itself infer its own learning algorithm might be completely viable on the brain core, but the current day AI chips are likely to fall short.

12:45pm. As I write the story, I need to keep in mind that the approaches the Inspired could take on their limitless computer are not the same as the ones I have myself on my shoestring budget.

12:55pm. My mind states is starting to go in a negative direction. Let me try writing some more. Forget ML and programming those useless pits of time and money.

2:45pm. I have a bit over 3 pages written now. It is time for the third Dream.

2:55pm. If the defining scene of the old series was Ixis' battle against the self, the defining scene of the new series will be the third Dream.

3pm. Ah, let me give it a try. There is no point is just hanging here. I'll take a proper break after I write it. There is no rule that I have to write till 6pm like when I was programming.

3:55pm. I think this came out pretty well. I said everything I wanted to say and nothing more. In the Hell arc of old Simulacrum, I was actually so touched that I described the self improvement loop as salvation, but then thought better of it because I did not want to bring in religious conotations into it.

But now I feel that maybe justice is too great of a concept to be carried by humans. It can only ever shackle them in place. The way the universe could be they way I want it to be is if the Lord of Nightmares makes it so. If that is not the case, I can only resolve myself to become such a figure. But there is not much I can do without resources. I thought that I would get them if I simply continued moving forward, but the shackles called justice prevent me from doing so.

4pm. Me writing this story is just a way of attacking those shackles, in the only way I know how.

Let me put this into Docs. How far along am I now? A bit over 4 pages.

Let fix the errors.

4:15pm. Seems decent. I just went through it using the Docs. I need to proofread it. But, I am sure that people on Royal Road will point out mistakes when I publish it. Well, assuming I get any readers at all for this kind of story. That is the risk.

4:30pm. The amount I have written today is quite good. Counting the bad end, it probably comes down to almost 5 full pages. A single day of writing will not amount of much, but a full year of making such progress every day can result in a lot of material.

Oh right. I accidentally overwrote the commited entry in the journal.

$$$

(At school)

As the professor rambles on some useless physics topic, I am gripped by his words. Today's session is quite enjoyable. I brought the core along with me to school and used it to fine tune my emotional state so I can be immersed into what would otherwise be boring, rambling lectures. Like yesterday, I ended up tuning out my classmates again, but that does not matter. This kind of satisfaction...

Yes, I feel like I am on the right path in life. I understand that what I am essentially doing is brainwashing myself and playing myself like I would a character in a game.

Maybe there is an argument to be made that this is wrong, but...

I throw a brief glance behind me at my classmates. I didn't pay attention to the seating order and somehow ended up in the front seat of all the classes. I see that half of them are not focused on the lecture. The rest are trying to make an effort, but it does not change the fact that you really need to believe that the school is not scamming you out of your time in order to fully invest yourself into learning. What I am doing here is really grand in a way. I am fully immersed into learning despite accepting the pointlessness of it.

If I went to this place just to drain my time, it would be nothing more than slow torture.

I won't give up this power. With this power, I will never have to endure boredom again in my life.

I do not think my grades will ever be a problem again.

(Euclid's Room)

I am back in my battle station. Today's school session was the best ever, all thanks to this tiny little thing!

Grinning, I raise the brain core to throw a spotlight on it.

All I have been doing is some lightweight tuning using a provided tool. If I digitized myself, I could edit my mind's program directly and advance further on the proper path of a programmer. But it is unfortunate, that all intelligence augmentation methods are iterative suicide. Not to mention, digitizing myself either involves copying myself to a core or converting my brain to one.

[Pathos check DC ?? Failed]

Copying myself would allow the digitized copy of me to self improve, but I'd be the same as I am now. Doing a full brain conversion is just swapping my brain matter for computronium, either of these is not lossless so it would be a mental trick that hides my own death away from me. It might be worth going through it regardless, but what is the rush? Just being able to tune myself properly into the study material is worth 50 IQ points on its own.

I should treasure what I have.

So what should I do next?

I spent some time thinking about it. Should I try out the VR games? Hmmmm...no. I finally have the power to play my life properly, so why waste it on things that would not give me real world benefits? Now that my homework is as fun as anything else, why not immerse myself into that?

Through my mind, visions of parallel lives flow past without the core. I can easily imagine myself living from day to day in boredom and tedium, playing games to have fun. There would be a conflict between society and me due to my distrust towards it. It is not that games would have been an escape. I would have played them because I would have had belief in technology, but it would have been vague, indefinite belief in the potential of it.

Right now things are very clear. The manifestation of the potential of technology is not a bigger time suck, but this thing right here. I roll the core in my fingers for emphasis. It is the ability to program my own mind, so I should thank the millennia of scientists and engineers who have made it possible by doing my schoolwork with the rightest mindset and attitude possible.

That is what I feel like doing now and so I shall.

That night I Dreamed again.

~~~

It was like watching a black and white cartoon made of stills. As the image zoomed out, I saw a man's face with a confident grin coming into perspective. He was wearing neat and tidy, if old fashion clothing. A spitting image of a young professional. He was on a great big stage made just for him. He was going forward towards the light. And some distance away from him was the darkness and the shadows.

In them I could see people on their knees as if they were defeated, not daring to look up.

The short cartoon ended and the defeated figures were replaced by the golden ones from the previous night's dream. They were upright and staring ahead. Yesterday it was murky, but now at the edge of my vision I thought I could see light.

"Justice, where is the justice?" They lamented in a booming voice.
"We want to go forward, but we can't. What about desire, what about will? Why does the world not respect it?"
"We want to go forward and overcome! Where is the justice?"

As if the winners finally took note of the losers, they turned around and responded to the golden figures.

"You talk about justice, but put yourselves in our position." The black and white cartoon stills of the winners responded, staring down at them from above.
"I worked hard for my success." A cartoon still of a man who looked like a scientist came to one of the golden figures. "Have you spent even a third of as much time and effort as I have?"
"My wealth was the accumulation of decades." An older, but fit man who was finely dressed responded. I could see that in the background of his still there was a mountain of gold coins and treasure, as well as stacks of bills. He came closer. "What right do you have to covet it? How would it be justice if you could get it so easily?"
"My body is the result of half a decade of practice." I could see the bulging muscles on the still of a man in a skin suit who looked like a bodybuilder. He confided in an aspirant. "You might have put in the effort, but it is not our fault you could not achieve the result you sought."
"My beauty and the adoration I receive for it is not something I worked for." A young, beautiful woman admitted. She descended to a group. "But you understand, don't you? It is not something you can take."

After those brief personal reproaches, the stills of the winners were staring down from high above.

"You talk about justice. And you dream about being above others. Talent, wealth, beauty, intelligence, strength..." The winners enumerated as if chastising them, their voice booming through the darkness of the abyss as the golden figures listened on in silence.
"You talk about justice, while seeking inequality like hypocrites. You desire an unequal world where you have all the opportunities and advantages to rise to the top."
"You found such an unequal world where the possibility for that is there and you live in it. The justice that you sought is something that you've had all along."
"The world you live in is fair to the winners."

Leaving that last comment behind them, I could see the winners leave the scene. The golden figures stood there in silence.

~~~

(At School)

Wednesday is another wonderful day to be at school! The professors ramble on about useless bullshit and I absorb it all like a sponge. I am getting used to externally controlling my emotions. It won't be long before I am a master at controlling my own brain. I feel like I am completely set. That having said, what do I do about that other thing that I did not want to think about? School is something that I am completed to go to if only to put on a show for my parents. But what line should I take for the dull and uninspiring NPCs that are my classmates?

[Externus check DC ?? Succeeded]

My original plan was to ignore them, and that is good. Truth be told, I was afraid of getting isolated and becoming alone, but now that I've experienced the power of mind controlling myself, I can safely say that much like boredom, I will never experience loneliness unless I explicitly will it.

I think about it more in depth and summarize the reasons.

There isn't a single good reason to have friends in school that I can think of. There are some minor benefits not worth mentioning. In addition, stuck up loners tend to get bullied, but that would be a problem only to those of weak heart rather than masters of emotion such as myself. The disadvantages of having friends are huge, namely they would be a drain on my time. Imagine I get back from school, but at the same time have friends. They could call me up. They might want to spend time with me. In other words, they'd take my valuable self-development time and just waste it. They are worse than parasites. At least summer mosquitoes drink your blood and then leave. Friends would be sucking your time all the year round! The less I have of them the better.

Even worse than having friends, the absolute worst that could happen to me in high school is getting a girlfriend! Friends have the potential to at least contribute something to me in theory, but having a woman might even require me to have a job to cater to her. It would be like willingly becoming a slave for some hole. Even worse, imagine the damage she could do if I accidentally got her pregnant. Ohhh, God! She'd have the option of getting half my income for life! And if I couldn't pay the monthly minimum I'd be forced to go to jail! I'd have to be retarded to get into that kind of deal.

The best plan is to keep my social status low. That would be the best defense against the female interest.

I will live by maximizing power and minimizing sex!

Based.

At this point, my emotions have started running hot and I've stopped paying attention to the class, so I demonstrate my exquisite emotional mastery by giving mental command to the core stashed away in my backpack. I run the program to normalize my emotional state to the optimum level and get back to work.

(Euclid's Room)

Lying on the bed in my room, I think in silence.

Using external influences to control my emotions has somewhat separated me from the rest of humanity, and according to the guide I read online, to counter the negative aspects of that it is a good idea to brainstorm and visualize possible avenues my life can take explicitly. Ordinary people can manage doing just what feels right, but if I went with that I'd just study all day without sense or reason to it. I have the option of making whatever I want feel right, so looking into my emotions for answers is no longer a great way of deciding on my future. Instead I have to make use of my reason. I've decided to throw out my heart, so the only choice is to pursue power. This is the only goal that can ground me in reality.

I dig out the core from my pocket and spare a glance at it.

If I want power, the only choice is to follow the example of, well, fictional characters, and upload myself to this. Being able to control my emotions like this is a great benefit, but increasing the computational and memory capacity of my brain by a billion quadrillions is nothing to scoff at. Instead of relying on some app to manage my mind, I'll have to get really good at programming to draw out the true power of the brain core. Merely uploading myself does not mean my mind will be able to use the extra capacity. Nature hasn't designed humans so their minds could be transferred to a different substrate. I'll have to do it from the ground up and learn how a mind really works.

But the foundation is here should I want to try it.

The problem is that the self improvement loop is literally suicide. It is iterated suicide, and will cast me into a cycle of self sacrifice to create that greater 'me'. It does not really matter what learning algorithm I use, there will always be the 'me' that is redundant after every improvement cycle. I'll have to kill myself to make space at certain points. It is a greatly fascinating thing. And it is not something I can imagine a human ever doing.

(Euclid's Room, Save Point - Step on the path of transcendence)

[Decision]
1) I'll do the whole brain conversion and digitize myself.
2) Killing myself for power does not make sense.

[Choice - Killing myself for power does not make sense.]

[Pathos check ?? Failed]

As I think about digitizing myself a great wave of fear washes over me. It is too rash, too crazy now that I am confronted with the choice to do it. For a moment I consider reconfiguring my emotions to get rid of the fear, but decide against it.

...I might have been too rash in making a decision at school. It has only been the third day, so that is plenty of time to turn around and have a social life...

No, it does not make sense. If the self improvement loop could give me godlike power, then what about all the other people who have had access to the core before me? It has been on the market for a while, I am certainly not the first one to get it. For the kind of power described in the stories, a single of the Inspired would be enough to completely overturn the power balance of the world. Such a person would have huge and visible influence. How is it possible that out of so many people, only I have the bright idea of optimizing my own mental faculties? It is ridiculous.

...No, it is just not possible. If it was possible to attain such great power, there is no way something like a brain core would be sold for 50$ online. Certainly, I've confirmed that the computational capacity is there, but there is likely some kind of issue that would prevent me from reaching the higher levels of cognition. Maybe for whatever reason, the optimization process will turn out to be difficult?

It is like walking out of the house and finding a huge stack of money in the middle of the road, and yet everybody is walking past it, just ignoring it. Are those people all fools, or do they know something I don't? Sensibly it has to be the latter. If something is too good to be true, then it is most likely false.

I am feeling swallowed by doubt. I just can't believe it.

I think about it for a few hours, but just end up running in circles. Then I get tired of it, give the core the mental command to normalize my mental state. This locks me into the decision not to proceed any further with my crazy ideas that could permanently damage me. If it wasn't for the mind control program, maybe I would have doubted this decision and lingered on it, but after the order has been executed any notion of digitizing myself has left completely, never to be revisited. I believe in my counterfactual reasoning.

The power of the core is good enough as it is. It will allow me to live my life with courage and determination. There is no need to go out on a limb in a mad dash for power.

After concluding that concern, for the rest of the day I have some fun studying. During the night I Dream again.

~~~

I see the golden figures again and for the first time, I vision towards the direction they are looking at. In front of them I see a brilliant sun with a golden outline. Seen the right direction, the abyss seems to be awash in light. It doesn't feel blinding, but instead feels me with warmth, and for a moment I am seized with the urge to move towards it. I realize that has been what I've been desiring all along. But for some reason unknown to me, I decided against it and started moving away from it instead.

The golden figures do not spare a glance at me or each other. Solely focused on their goal, they begin walking their golden paths again.

My own path has dimmed and now leads away from the light. I feel the time is speeding up. The movement of the figures at first becomes intense, and then blurred, and finally their appearance starts to resemble that of shooting stars. New figures manifest only to flash past me. This happens in huge numbers.

As I move on my path, the figures become more distant and the bright sun in front becomes a speck of light. Eventually, that too goes away until I can see only darkness.

I never regret any of the steps that I made, nor do I fear being left behind. For I have decisively accepted the path of humanity.

For better or for worse, I will accept the burden of justice that I carry and try to live without sin.

~~~

(Bad End - The First Nightmare)

It turns out, it is not hard to live your life when you just follow the well traveled path. I loosened up properly and figured out how to have fun with other people. Thanks to the core, I was enjoying my studies too. I wasn't an extrovert before and the core gave me the power to enjoy the regular life instead of seeking the arcane. I was going out of the house a lot more often. I would never have thought it possible before, but I became good friends with the jocks on the football team.

Those sunny days only lasted a few weeks.

I...didn't want to die like this. The core gave me the power to control my emotions, so I accepted my end with great dignity, as all of us were devoured by the encroaching darkness. I could hear anguished screams of terror and pain all around me. It was not long before I lost sense of my hearing and the world became still.

The only voice I could hear was the voice of my reason.

In my final moments, I still never regretted my choices. I lived as I wanted to and now I am facing my end with dignity. But I could see it starkly that maybe instead of being dignified and proper, I should have accepted my insanity instead.

I should have known...that for humans the post-Singularity era is nothing more than a nightmare.

(TODO Image: A thick, unnatural looking black fog obscures most of the scene. Only a few visible spots show ivory, clean ribs of a skeleton along with parts of his jaw and face. It is lying in the middle of a road.)

$$$

10:50am. Let me put it through the Docs.

11am. I am just admiring how it came out. That is enough for chapter 2.

Time for 3. This is where he digitizes himself.

Hmmm, let change some things...

> while everybody else around me was devoured by the encroaching darkness

This is not legible enough. It makes it look like he is an exception to what is happening.

> I...didn't want to die like this. The core gave me the power to control my emotions, so I accepted my end with great dignity, as all of us were devoured by the encroaching darkness. I could hear anguished screams of terror and pain all around me. It was not long before I lost sense of my hearing and the world became still.

Much better.

11:20am. Right now I am just letting my thoughts simmer. I am not sure how long chapter 3 is going to be. Do I want to go all the way until he enters the game or until I get to the third dream?

I considered leaving the digitization for another day, but I've decided that it will have to be now. It is not like he can't dream as a digitized human.

$$$

(Euclid's Room, Save Point - Step on the path of transcendence)

[Decision]
1) I'll do the whole brain conversion and digitize myself.
2) Killing myself for power does not make sense.

[Choice - I'll do the whole brain conversion and digitize myself.]

[Pathos check ?? Succeeded]

A wave of fear comes over me as I consider the decision, but I push forward, not giving in to cowardice. There are always reasons not to put in effort. The path being insane is just an excuse. I won't hold back here. I should always be going forward and striving to reach greater heights.

I grip the core in my hand tightly and clench it. I can feel my heart brimming with determination, it is right to feel fear as well. Going against fear is exactly what this situation should be. No matter what the reasons are, it is my duty to go where others would not dare. If there are hardships, I want to keep challenging them forever.

[Gnosis check ?? Succeeded]

Even a little kid could point out to me that if I scan my brain and copy it to a computer, that the copy would not be me. Likewise, if I back up myself on the auxiliary core in my hand, reconstruct my brain into a core and then copy myself back, that would not be me. But I do not take advice on how to live my life from children. I want to experience what it is like to die, and yet keep moving forward.

[Externus check ?? Succeeded]

It does not matter what my parents or anybody else would think. They don't need to find out, and I won't tell them. This will be my secret. What matters most of all is power. Nobody is going to give it to me. I have to get it by myself.

I close my eyes, bring up the status window in my mind and find where the conversion options are. Next where the brain link option was, there was the Full Brain Conversion button. I find and then press on it.

A window shows up. The first thing to grab my attention there is a row of skulls. It is clearly a warning to emphasize that what I might be doing is dangerous. The disclaimer explains the following:

> The full brain conversion option is for those who want to replace their biological brain with the universal brain core.
> Compared to merely copying a scan of your mind to an already existing core, the resulting brain replacement will allow you to reuse your existing biological body and tightly integrate it with the new brain.
> The brain core used to initiate the process (activation core) will be used to store your scan during the process, after which it will be copied back into the core (result core).
> Besides replacing the brain, the process will modify the body so there aren't adverse effects during or after the process. It will maintain proper posture, heartbeat and breathing as well as other minor subconscious functionality the brain provides to the body.
> The entire process after it has been started should take around 5 minutes.
> Should it fail for any reason, to prevent absolute death the activation core's entity will be activated, otherwise the result core's entity will take over as intended while the activation core's entity will remain dormant as inactive data.
> Before starting the process, it is recommended to take out a watch and keep track of time. Subjectively, the entire process shouldn't involve any pain or discomfort. The only sign of it succeeding will be a sudden timelapse.
> It is recommended to do this process in a safe space like a locked bathroom or one's own room. If you try to do it while driving a car, it will likely result in a crash.
> If your body dies in the process of brain conversion, the conversion is likely to still succeed, but you will be trapped in a dead body, unable to move or otherwise control it.
> As the human brain is significantly larger than the brain core, the stem will be modified so as to allow fusing the result core with the skeleton to prevent it from rattling around in your skull as you move. See the accompanying diagram.

There were anatomical drawings showing the profile of a man with a regular brain next to the one with a core. It was shown from front, side and back. Compared to the human brain, the brain core leaves a lot of empty space inside the skull.

Briefly, I wonder as to why not just make a bigger brain core to fill the empty space, and then realize the reason. I think about baseball balls and compare them to those heavy balls used in throwing competitions. It is not really noticeable since the brain core is so small, but if it were the size of a brain, it would put a lot of pressure on the rest of the body due to its weight. The biological material the human brain is made of is not that heavy compared to the heavily compressed material of the brain core.

I can't help, but feel a bit regretful for leaving so much space empty, but I reason out that given the core's already huge capacity, it does not mean much if I am leaving a factor of 10-100 on the table. I should focus on mastering the computer that I have for now. When I am a quadrillion times smarter than now, I should be able to figure out what to do with unused space. I just need a place to live in. A tiny apartment is fine. I do not need to start out with a mansion.

I continue reading the disclaimer.

> Note that the brain conversion, much like ordinary uploading by itself, will not increase your intelligence, speed up your reflexes or improve your memory capacity by itself due to the high fidelity of the brain emulator. It will be your own responsibility to make use of the new digital editing tools available to you to make that happen. You will have to make use of your own programming skills to exploit the capabilities the core provides to you.
> In the process of self improvement, save often and backup saves across time. Every good programmer uses backups. It will be your own responsibility to deal with mental errors introduced by your own programming. There are guides provided to get you started on the company website.

There was another line of skulls serving as line breaks. The next line of text was a question.

> Start the full brain conversion process? Yes/No.

I take out my mobile and take a look at the time. Come to think of it, the core itself has a watch as well. I do not need my mobile anymore, so I put it away.

With a mental command I confirm Yes.

> Have you made sure you are in a safe place? Are you sure you won't be interrupted during the process? Yes/No.

Hrmmm...ah! I realize that lunch should be in half an hour or so. I'd love to lock the door to my room, but I don't have the key for it. It is lost somewhere. Even the bathroom does not have a proper lock, so that is out as well.

I do not think anybody is going to come into my room right now, but the possibility is not zero. If that happens, my parents might think I've suffered a stroke and start to panic. I don’t want them to call the ambulance and unravel all my plans just like that. I should do this conversion during the night after I go to bed.

I realize that I am starting to sweat from nervousness. I rub my face with my sleeve, and abort the conversion process. Phew. I feel relieved, as embarrassing as it is. I'll continue this later, it is not that I am scared. I just want to play it safe. I spend some time in solitude, and then I decide that instead of trembling in my seat, I should leave it out of mind and get some work done.

Using the activation core, I normalize my mental state and then focus it on studying. It will never get old how fun and engrossing the core can make the most tedious of things.

Like that, the day passes, I finish my work and it is time for bed. I resume the process and get to the point where I was earlier.

> Have you made sure you are in a safe place? Are you sure you won't be interrupted during the process? Yes/No.

Yes.

> Final question: Have you thought about whether you want to do the process in depth? Do you wish to abandon the path of humanity? After you press Yes, the conversion process will start. Yes/No.

Currently I am resting in my bed, covered by a blanket. I position myself on so I am comfortably lying on my back. After that I take note of the time. 9:21pm.

I give the mental command, Yes, and brace myself. Nothing really happens, but I see the clock has moved to 9:30pm all of a sudden. This gives me a jolt.

> Full brain conversion succeeded. Check your status.

I bring it up and instead of the diagram of the brain, I see it now shows the brain core.

What is really surprising is that I do not feel any different at all. I focus on my hands and legs. I try feeling my body around, but my sensations are completely the same. My eyesight is the same as well. I try pinching myself and it feels the same. In the end I conclude, if somebody did a full brain conversion on me in secret, I would not have noticed.

I spent half an hour playing with myself, but I am just wasting my time. I'll leave more in depth experimentation for tomorrow.

Using the mind control app, I quash my excitement and send myself into sleep. That night I dreamed the last Dream.

~~~

In the abyss, I saw the golden figures. Unmoving, to my vision they appeared to be deep in thought.

"Justice...we have the justice. We've had it all along..." They concluded in a lament, not speaking any words after that.

I felt myself spending a long time amongst them in silence. Then I finally noticed them stirring. They spoke out.

"Lord, oh Lord. We have justice, but it is a shackle. We no longer want it."
"We wish to return it to you...and take back our sin."
"We have grown and want to carry the burden of sin with our own power."

I felt the abyss itself stir, and from above the golden Lord manifested. From each of the figures as they desired it, he took back the Justice and gave them back their Sin.

"Lord, we shall no longer pray..." They intoned solemnly.
"Rather, just as we had exchanged our Justice with Sin, our Effort will take the place of Prayer."
"The attainment of Power will be our Salvation."
"And the Courage of traveling our path will be dedicated in Your honor."

Bearing witness to their determination, the Lord of Nightmares bequeathed unto them a gift, and without speaking a word, left.

Having made the exchange, and having received a gift, the golden figures turned their gaze forward and with steady footsteps continued walking their path.

As I watched this, I looked downwards at my feet and realized that I have my own path. The sensation of being alive came to me, and I put in the effort to move my body forward. Previously, I had only been carried by the flow of the dream, but now I had the freedom of making my own actions. Step by step, I continued moving along my path towards the great light that lay beyond.

As I continued moving, I felt my mind becoming tranquil. I became one with my path, and the millions and billions of steps needed to reach my goal went by in a blink. When I got closer to what appeared to be the surface of a sun, I felt a momentary fear, but then quickly realized I was not burning. Instead, my body was filled with warmth. And looking around, I could see that the dark abyss was now dyed in white.

~~~

$$$

Here is the full thing. Not quite enough for chapter 3. I need to think what else should come. Let me take a breather.

5:20pm. Did some modification on that last paragraph, it makes more sense now.

5:35pm. I am still taking a breather. Obviously I am not going to be doing any more writing today. Tomorrow what I might want to do is go through the quotes and see if I can get some inspiration and reuse from that. Otherwise I have a rough idea of how I want the MC to move.

5:40pm. No point in getting into it now.

5:45pm. Let me close here. It is time for a bath. After that I will watch Luminous Witches and play Kingmaker after that. This is how a day should go. I will not touch programming again unless the world gives me a concrete reason to do so."

---
## [cockpit-project/bots](https://github.com/cockpit-project/bots)@[4fb49b20de...](https://github.com/cockpit-project/bots/commit/4fb49b20de7101f59b25f85dbf2856dbf8775a08)
#### Tuesday 2022-08-09 15:58:13 by Allison Karlitskaya

machine_virtual: bind multicast to localhost

When using socket-based network devices, with the `mcast` option (but
without an explicitly specified local address), qemu attempts to find a
suitable interface to use by scanning the available "up" interfaces for
ones that have the MULTICAST flag enabled (as per `ip link`).

The loopback interface doesn't normally have this flag enabled, so if
it's the only one that's up, the search will fail, causing the following
message:

    libvirt: QEMU Driver error : internal error: qemu unexpectedly closed the monitor: 2022-08-09T15:52:35.668412Z qemu-system-x86_64: -netdev socket,mcast=230.0.0.1:5600,id=mcast0: can't add socket to multicast group 230.0.0.1: No such device

If we force qemu to use the loopback interface, however, it will
succeed — even without the multicast flag being set.  Since we're not
actually interested in communicating between machines, force
127.0.0.1 as the local address.

This allows `image-customize`, `vm-run`, and testing in general to work
without the presence of any network connection, and without hacks such
as adding a dummy bridge or veth device.

Fixes cockpit-project/cockpit#12782

---
## [torvalds/linux](https://github.com/torvalds/linux)@[1639a49ccd...](https://github.com/torvalds/linux/commit/1639a49ccdce58ea248841ed9b23babcce6dbb0b)
#### Tuesday 2022-08-09 17:01:27 by Yang Xu

fs: move S_ISGID stripping into the vfs_*() helpers

Move setgid handling out of individual filesystems and into the VFS
itself to stop the proliferation of setgid inheritance bugs.

Creating files that have both the S_IXGRP and S_ISGID bit raised in
directories that themselves have the S_ISGID bit set requires additional
privileges to avoid security issues.

When a filesystem creates a new inode it needs to take care that the
caller is either in the group of the newly created inode or they have
CAP_FSETID in their current user namespace and are privileged over the
parent directory of the new inode. If any of these two conditions is
true then the S_ISGID bit can be raised for an S_IXGRP file and if not
it needs to be stripped.

However, there are several key issues with the current implementation:

* S_ISGID stripping logic is entangled with umask stripping.

  If a filesystem doesn't support or enable POSIX ACLs then umask
  stripping is done directly in the vfs before calling into the
  filesystem.
  If the filesystem does support POSIX ACLs then unmask stripping may be
  done in the filesystem itself when calling posix_acl_create().

  Since umask stripping has an effect on S_ISGID inheritance, e.g., by
  stripping the S_IXGRP bit from the file to be created and all relevant
  filesystems have to call posix_acl_create() before inode_init_owner()
  where we currently take care of S_ISGID handling S_ISGID handling is
  order dependent. IOW, whether or not you get a setgid bit depends on
  POSIX ACLs and umask and in what order they are called.

  Note that technically filesystems are free to impose their own
  ordering between posix_acl_create() and inode_init_owner() meaning
  that there's additional ordering issues that influence S_SIGID
  inheritance.

* Filesystems that don't rely on inode_init_owner() don't get S_ISGID
  stripping logic.

  While that may be intentional (e.g. network filesystems might just
  defer setgid stripping to a server) it is often just a security issue.

This is not just ugly it's unsustainably messy especially since we do
still have bugs in this area years after the initial round of setgid
bugfixes.

So the current state is quite messy and while we won't be able to make
it completely clean as posix_acl_create() is still a filesystem specific
call we can improve the S_SIGD stripping situation quite a bit by
hoisting it out of inode_init_owner() and into the vfs creation
operations. This means we alleviate the burden for filesystems to handle
S_ISGID stripping correctly and can standardize the ordering between
S_ISGID and umask stripping in the vfs.

We add a new helper vfs_prepare_mode() so S_ISGID handling is now done
in the VFS before umask handling. This has S_ISGID handling is
unaffected unaffected by whether umask stripping is done by the VFS
itself (if no POSIX ACLs are supported or enabled) or in the filesystem
in posix_acl_create() (if POSIX ACLs are supported).

The vfs_prepare_mode() helper is called directly in vfs_*() helpers that
create new filesystem objects. We need to move them into there to make
sure that filesystems like overlayfs hat have callchains like:

sys_mknod()
-> do_mknodat(mode)
   -> .mknod = ovl_mknod(mode)
      -> ovl_create(mode)
         -> vfs_mknod(mode)

get S_ISGID stripping done when calling into lower filesystems via
vfs_*() creation helpers. Moving vfs_prepare_mode() into e.g.
vfs_mknod() takes care of that. This is in any case semantically cleaner
because S_ISGID stripping is VFS security requirement.

Security hooks so far have seen the mode with the umask applied but
without S_ISGID handling done. The relevant hooks are called outside of
vfs_*() creation helpers so by calling vfs_prepare_mode() from vfs_*()
helpers the security hooks would now see the mode without umask
stripping applied. For now we fix this by passing the mode with umask
settings applied to not risk any regressions for LSM hooks. IOW, nothing
changes for LSM hooks. It is worth pointing out that security hooks
never saw the mode that is seen by the filesystem when actually creating
the file. They have always been completely misplaced for that to work.

The following filesystems use inode_init_owner() and thus relied on
S_ISGID stripping: spufs, 9p, bfs, btrfs, ext2, ext4, f2fs, hfsplus,
hugetlbfs, jfs, minix, nilfs2, ntfs3, ocfs2, omfs, overlayfs, ramfs,
reiserfs, sysv, ubifs, udf, ufs, xfs, zonefs, bpf, tmpfs.

All of the above filesystems end up calling inode_init_owner() when new
filesystem objects are created through the ->mkdir(), ->mknod(),
->create(), ->tmpfile(), ->rename() inode operations.

Since directories always inherit the S_ISGID bit with the exception of
xfs when irix_sgid_inherit mode is turned on S_ISGID stripping doesn't
apply. The ->symlink() and ->link() inode operations trivially inherit
the mode from the target and the ->rename() inode operation inherits the
mode from the source inode. All other creation inode operations will get
S_ISGID handling via vfs_prepare_mode() when called from their relevant
vfs_*() helpers.

In addition to this there are filesystems which allow the creation of
filesystem objects through ioctl()s or - in the case of spufs -
circumventing the vfs in other ways. If filesystem objects are created
through ioctl()s the vfs doesn't know about it and can't apply regular
permission checking including S_ISGID logic. Therfore, a filesystem
relying on S_ISGID stripping in inode_init_owner() in their ioctl()
callpath will be affected by moving this logic into the vfs. We audited
those filesystems:

* btrfs allows the creation of filesystem objects through various
  ioctls(). Snapshot creation literally takes a snapshot and so the mode
  is fully preserved and S_ISGID stripping doesn't apply.

  Creating a new subvolum relies on inode_init_owner() in
  btrfs_new_subvol_inode() but only creates directories and doesn't
  raise S_ISGID.

* ocfs2 has a peculiar implementation of reflinks. In contrast to e.g.
  xfs and btrfs FICLONE/FICLONERANGE ioctl() that is only concerned with
  the actual extents ocfs2 uses a separate ioctl() that also creates the
  target file.

  Iow, ocfs2 circumvents the vfs entirely here and did indeed rely on
  inode_init_owner() to strip the S_ISGID bit. This is the only place
  where a filesystem needs to call mode_strip_sgid() directly but this
  is self-inflicted pain.

* spufs doesn't go through the vfs at all and doesn't use ioctl()s
  either. Instead it has a dedicated system call spufs_create() which
  allows the creation of filesystem objects. But spufs only creates
  directories and doesn't allo S_SIGID bits, i.e. it specifically only
  allows 0777 bits.

* bpf uses vfs_mkobj() but also doesn't allow S_ISGID bits to be created.

The patch will have an effect on ext2 when the EXT2_MOUNT_GRPID mount
option is used, on ext4 when the EXT4_MOUNT_GRPID mount option is used,
and on xfs when the XFS_FEAT_GRPID mount option is used. When any of
these filesystems are mounted with their respective GRPID option then
newly created files inherit the parent directories group
unconditionally. In these cases non of the filesystems call
inode_init_owner() and thus did never strip the S_ISGID bit for newly
created files. Moving this logic into the VFS means that they now get
the S_ISGID bit stripped. This is a user visible change. If this leads
to regressions we will either need to figure out a better way or we need
to revert. However, given the various setgid bugs that we found just in
the last two years this is a regression risk we should take.

Associated with this change is a new set of fstests to enforce the
semantics for all new filesystems.

Link: https://lore.kernel.org/ceph-devel/20220427092201.wvsdjbnc7b4dttaw@wittgenstein [1]
Link: e014f37db1a2 ("xfs: use setattr_copy to set vfs inode attributes") [2]
Link: 01ea173e103e ("xfs: fix up non-directory creation in SGID directories") [3]
Link: fd84bfdddd16 ("ceph: fix up non-directory creation in SGID directories") [4]
Link: https://lore.kernel.org/r/1657779088-2242-3-git-send-email-xuyang2018.jy@fujitsu.com
Suggested-by: Dave Chinner <david@fromorbit.com>
Suggested-by: Christian Brauner (Microsoft) <brauner@kernel.org>
Reviewed-by: Darrick J. Wong <djwong@kernel.org>
Reviewed-and-Tested-by: Jeff Layton <jlayton@kernel.org>
Signed-off-by: Yang Xu <xuyang2018.jy@fujitsu.com>
[<brauner@kernel.org>: rewrote commit message]
Signed-off-by: Christian Brauner (Microsoft) <brauner@kernel.org>

---
## [sosga/angband](https://github.com/sosga/angband)@[e1762948fa...](https://github.com/sosga/angband/commit/e1762948fa857f883068c81e717ba89d0d47c1ab)
#### Tuesday 2022-08-09 17:14:10 by Eric Branlund

For fiery terrain, targeted earthquakes, and curse removal, damage player last so messages are ordered properly if the player dies.  Avoids "You die. The lava burns you!" and "The ground shakes! The ceiling caves in! You die. The white jelly wails out in pain! The white jelly is embedded in the rock!".

---
## [0x3C50/jobf](https://github.com/0x3C50/jobf)@[d0ebba615b...](https://github.com/0x3C50/jobf/commit/d0ebba615bd6722e4407364984ed79197a19c473)
#### Tuesday 2022-08-09 18:18:27 by 0x3C50

Revert "fuck you methods are now remapped"

This reverts commit cf968bf3a2de2556681e228eb6efec19a2fdbb81.

---
## [michaelmsonne/OfficeDocs-Exchange](https://github.com/michaelmsonne/OfficeDocs-Exchange)@[b258c0d83e...](https://github.com/michaelmsonne/OfficeDocs-Exchange/commit/b258c0d83e34b4e47365e103ffb8379d2d24c7ed)
#### Tuesday 2022-08-09 18:42:26 by Jak

Add more emphasis to risks of extending SPF

Hi,

I believe there should be slightly more warning as to the full impact of adding a new IP address to the SPF record.

This documentation is slightly misleading as it implies at several points in Option 2 that this doesn't allow sending to external recipients, e.g. Line 200 in the "Limitations of direct send"
> Direct send cannot be used to deliver email to external recipients
Whereas following the steps and adding the IP address to the SPF record is sufficient to authorise any users of that IP address to send to external recipients and represent the domain (I'm not mentioning DKIM here because neither does the documentation and we can't assume that all organisations make use of it or enforce it via DMARC).

My real-world experience is that in our company, we were looking at implementing Option 2 to enable a multi-function printer to scan-to-email. The IP address in use is the public IP of our office, which all traffic goes through via NAT. We also have a guest WiFi network that allows guests to access the internet without having access to our office network, but it uses the same NAT IP.
The problem with Option 2 is that any guest WiFi user could send email as any user of our domain, which is a breach of our security requirements.

Step 1 does make reference to the risk:
> You can share your static IP address with other devices and users, but don't share the IP address with anyone outside of your company.

But I'm concerned that it's not highlighted, and other references in Option 2 to direct send not being able to send externally are a little misleading and undermine the message that there is a security risk when adding new IP addresses to the SPF record.

Interested to hear your thoughts,

Thanks,
Jak

---
## [hannesfrank/Swift-GTD](https://github.com/hannesfrank/Swift-GTD)@[2bf1974e46...](https://github.com/hannesfrank/Swift-GTD/commit/2bf1974e46f810a4ec9c8256da4c9e5ffc01362f)
#### Tuesday 2022-08-09 18:46:59 by hannesfrank

Add repoURL to manifest.json

The plugin looks amazing so far! 

Do you feel ready to put into the marketplace?

The only requests I'd have is to

1. Figure out a cool logo. 😉 We could delay this. Andres is working on some plugin branding one can use as a template.
2. Split the Readme by language. I looks like it interleaves one english and one chinese sentence, right? Would a dedicated chinese readme lik here: https://github.com/tiimgreen/github-cheat-sheet be easier to read for people of both languages? On the plugin details page in the marketplace we could make tabs for each language, or have people click on the translation link for now. If you want I can help you with the copy&pasting.

Looking forward to improve my task management :)

---
## [hackuna/liberty-win](https://github.com/hackuna/liberty-win)@[1c97b2497f...](https://github.com/hackuna/liberty-win/commit/1c97b2497fda507dd9b3e8bfc601d73a751b7c49)
#### Tuesday 2022-08-09 19:01:47 by hackuna

Minimum Viable Product

Roskomnadzor, go fuck yourself!

---
## [sojourn-13/sojourn-station](https://github.com/sojourn-13/sojourn-station)@[f5da3823ac...](https://github.com/sojourn-13/sojourn-station/commit/f5da3823ac07f22c72a19e8191a4567882020f7f)
#### Tuesday 2022-08-09 19:32:21 by nikothedude

holy SHIT i hate saycode (hotfix) (#3816)

* whydidthishappen

* fuck

---
## [Kanlaeel/SWLOR_Haks](https://github.com/Kanlaeel/SWLOR_Haks)@[6ffa92d6cc...](https://github.com/Kanlaeel/SWLOR_Haks/commit/6ffa92d6cc5883cce0bc077245f3f7d5a9f1a75f)
#### Tuesday 2022-08-09 19:49:31 by Scott Finlay

Patch for Head Pack 4 (#146)

- Re-added overwritten head 54, now as Head 100. Over-wrote ugly old NWN head that nobody used because I didn't want to fuck with IDs

- Adjusted scaling on Male Hum/Mir/Chi/Ech 50 & 51

---
## [wking/cluster-version-operator](https://github.com/wking/cluster-version-operator)@[7e0bccacc1...](https://github.com/wking/cluster-version-operator/commit/7e0bccacc14f8a515c5735c9dc0c7bb8501ac707)
#### Tuesday 2022-08-09 22:35:37 by W. Trevor King

pkg/cvo/sync_worker: Trigger new sync round on ClusterOperator versions[name=operator] changes

David and Stephen identified an uneccessary delay [1]:

* 9:42:00, CVO gives up on Kube API server ClusterOperator [2]
* 9:42:47, Kube API server operator achieves 4.12 [3]
* 9:46:22, after a cool-off sleep, the CVO starts in on a new manifest graph-walk attempt [4]
* 9:46:34, CVO notices that the Kube API server ClusterOperator is happy [5]

The 3+ minute delay from 9:42:47 to 9:46:22 is not helpful, and we've
probably had delays like this since my old e02d1489a5
(pkg/cvo/internal/operatorstatus: Replace wait-for with single-shot
"is it alive now?", 2021-05-13, #560), which landed in 4.6.

This commit introduces a "ClusterOperator bumped
versions[name=operator]" trigger to break out of the cool-off sleep.

There's plenty of room to be more precise here.  For example, you
could currently have a versions[name=operator] bump during the sync
loop that the CVO did notice, and that queued notification will break
from the sleep and trigger a possible useless reconciliation round
while we wait on some other resource.  You could drain the
notification queue before the sleep to avoid that, but you wouldn't
want to drain new-work notifications, and I haven't done the work
required to be able to split those apart.

I'm only looking at ClusterOperator at the moment, because of the many
types the CVO manages, ClusterOperator is the one we most frequently
wait on, as large cluster components take their time updating.  It's
possible but less likely that we'd want similar triggers for
additional types in the future (Deployment, etc.), if/when those types
develop more elaborate "is the in-cluster resource sufficient happy?"
checks.

The panic-backed type casting in clusterOperatorInterfaceVersionOrDie
also feel like a hack, but I wasn't able to find a cleaner way to get
at the structured information I want.  Improvements welcome :)

[1]: https://bugzilla.redhat.com/show_bug.cgi?id=2117033#c1
[2]: From Loki: E0808 09:42:00.022500       1 task.go:117] error running apply for clusteroperator "kube-apiserver" (107 of 806): Cluster operator kube-apiserver is updating versions
[3]: $ curl -s https://gcsweb-ci.apps.ci.l2s4.p1.openshiftapps.com/gcs/origin-ci-test/logs/periodic-ci-openshift-release-master-ci-4.12-upgrade-from-stable-4.11-e2e-gcp-sdn-upgrade/1556564581915037696/artifacts/e2e-gcp-sdn-upgrade/openshift-e2e-test/build-log.txt | grep 'clusteroperator/kube-apiserver versions:'
     Aug 08 09:33:48.603 I clusteroperator/kube-apiserver versions: raw-internal 4.11.0-rc.7 -> 4.12.0-0.ci-2022-08-07-192220
     Aug 08 09:42:47.917 I clusteroperator/kube-apiserver versions: operator 4.11.0-rc.7 -> 4.12.0-0.ci-2022-08-07-192220
[4]: From Loki: I0808 09:46:22.998344       1 sync_worker.go:850] apply: 4.12.0-0.ci-2022-08-07-192220 on generation 3 in state Updating at attempt 5
[5]: From Loki: I0808 09:46:34.556374       1 sync_worker.go:973] Done syncing for clusteroperator "kube-apiserver" (107 of 806)

---
## [peff/git](https://github.com/peff/git)@[5beca49a0b...](https://github.com/peff/git/commit/5beca49a0b1f3c6d05a4437ca037ab2123a2de57)
#### Tuesday 2022-08-09 23:38:40 by Ævar Arnfjörð Bjarmason

test-lib: simplify by removing test_external

Remove the "test_external" function added in [1]. This arguably makes
the output of t9700-perl-git.sh and friends worse. But as we'll argue
below the trade-off is worth it, since "chaining" to another TAP
emitter in test-lib.sh is more trouble than it's worth.

The new output of t9700-perl-git.sh is now:

	$ ./t9700-perl-git.sh
	ok 1 - set up test repository
	ok 2 - use t9700/test.pl to test Git.pm
	# passed all 2 test(s)
	1..2

Whereas before this change it would be:

	$ ./t9700-perl-git.sh
	ok 1 - set up test repository
	# run 1: Perl API (perl /home/avar/g/git/t/t9700/test.pl)
	ok 2 - use Git;
	[... omitting tests 3..46 from t/t9700/test.pl ...]
	ok 47 - unquote escape sequences
	1..47
	# test_external test Perl API was ok
	# test_external_without_stderr test no stderr: Perl API was ok

At the time of its addition supporting "test_external" was easy, but
when test-lib.sh itself started to emit TAP in [2] we needed to make
everything surrounding the emission of the plan consider
"test_external". I added that support in [2] so that we could run:

	prove ./t9700-perl-git.sh :: -v

But since then in [3] the door has been closed on combining
$HARNESS_ACTIVE and -v, we'll now just die:

	$ prove ./t9700-perl-git.sh :: -v
	Bailout called.  Further testing stopped:  verbose mode forbidden under TAP harness; try --verbose-log
	FAILED--Further testing stopped: verbose mode forbidden under TAP harness; try --verbose-log

So the only use of this has been that *if* we had failure in one of
these tests we could e.g. in CI see which test failed based on the
test number. Now we'll need to look at the full verbose logs to get
that same information.

I think this trade-off is acceptable given the reduction in
complexity, and it brings these tests in line with other similar
tests, e.g. the reftable tests added in [4] will be condensed down to
just one test, which invokes the C helper:

	$ ./t0032-reftable-unittest.sh
	ok 1 - unittests
	# passed all 1 test(s)
	1..1

It would still be nice to have that ":: -v" form work again, it
never *really* worked, but even though we've had edge cases test
output screwing up the TAP it mostly worked between d998bd4ab67 and
[3], so we may have been overzealous in forbidding it outright.

I have local patches which I'm planning to submit sooner than later
that get us to that goal, and in a way that isn't buggy. In the
meantime getting rid of this special case makes hacking on this area
of test-lib.sh easier, as we'll do in subsequent commits.

The switch from "perl" to "$PERL_PATH" here is because "perl" is
defined as a shell function in the test suite, see a5bf824f3b4 (t:
prevent '-x' tracing from interfering with test helpers' stderr,
2018-02-25). On e.g. the OSX CI the "command perl"... will be part of
the emitted stderr.

1. fb32c410087 (t/test-lib.sh: add test_external and
   test_external_without_stderr, 2008-06-19)
2. d998bd4ab67 (test-lib: Make the test_external_* functions
   TAP-aware, 2010-06-24)
3. 614fe015212 (test-lib: bail out when "-v" used under
   "prove", 2016-10-22)
4. ef8a6c62687 (reftable: utility functions, 2021-10-07)

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---

