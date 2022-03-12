## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-03-11](docs/good-messages/2022/2022-03-11.md)


1,721,770 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,721,770 were push events containing 2,761,182 commit messages that amount to 193,644,393 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 28 messages:


## [rorydale/pointbreakradio](https://github.com/rorydale/pointbreakradio)@[71459277ab...](https://github.com/rorydale/pointbreakradio/commit/71459277aba48fcf0de050b7fd168418417d3ded)
#### Friday 2022-03-11 00:10:44 by Rory Dale

2022-03-10

Thursday, March 10th, 2022 - the new music show! More new music released in the last few hours, days, and weeks. Selections of rock, indie, folk, Americana, indie, progressive rock, and blues. I'm finding greater and greater enjoyment from seeking out and listening to new music again, and as the show nears its second birthday it's now once more become a part of life. Whether it's new material from familiar bands, or new bands and unfamiliar music it's all out there to be found. I hope you enjoy some of what caught my ear today!

---
## [Tastyfish/-tg-station](https://github.com/Tastyfish/-tg-station)@[eeb5465931...](https://github.com/Tastyfish/-tg-station/commit/eeb546593148ce940e9adac2c663c453d6557247)
#### Friday 2022-03-11 00:28:16 by vincentiusvin

Ordnance Content Update: Scientific Papers (#62284)

How do I play/test/operate this?

Download NT Frontier on any modular computers. It should debrief you on what experiments are available and how to publish.
If you want to do a bomb experiment, make sure it's captured by the doppler array (as usual) and then print the experiments into a disk and publish it.
If you want to do a gas experiment, make the gas and either pump it into a tank and 1) overpressurize it with a "clear" gas like N2 or 2) overpressurize tanks with the gas itself. Make sure you do the overpressurizing in the compressor machine. When tanks are destroyed/ejected leaked gas will get recorded. Print it into a disk and publish it.
For publication, the file needs to be directly present inside the computer's HDD. This means you need to copy it first with the file manager.
Fill the data (if desired, it will autofill with boiler plate if you dont) and send away!
Doing experiments unlock nodes, while doing them well unlocks boosts (which are discounts but slightly more restrictive) which are purchaseable with NT Frontier.
If you are testing this and have access to admin tools, there are various premade bombs under obj/effect/spawner/newbomb

A doc I wrote detailing the why and what part of this PR.
https://hackmd.io/JOakSYVMSh2zU2YL5ju_-Q

---

# Intro

## The Problem(s)

Ordnance, (previously toxins) seems to lack a lot of content and things to do. The gameplay loop consists of making a bomb and then sending it off for credits or using it to refine cores. Ordnance at it's inception originally relies on players experimenting and finding the perfect mix over multiple rounds, but once the recipe for a "do-everything" mix got out, the original charm of individual discoveries becomes meaningless.

Another issue with ordnance is the odd difficulty curve. As a new player, ordnance is almost impossible to decipher, but once you watch a tutorial or read a wiki and can mail a 50k into space, there pretty much isn't anything else to do. Most players will be satisfied at this point without the gameplay loop encouraging them to understand or play more. The only thing you can do afterwards is to sink your teeth in and understand why that particular mix explodes the way it does. This again has a significant difficulty curve, but if you do that, the department doesn't acknowledge or reward that in any way. There are pretty much two huge spikes, with the latter one not really existing inside the department.

TLDR:
* The content being same-y over rounds.
* Odd difficulty curve: 
    1. A new player is oblivious to everything. 
    2. Those in the middle can repeat the final goal consistently without needing to understanding why
    3. There is nothing to justify spending more time in the department after reaching the midgame.

## Abstract

Scientific Papers aim to add a framework to run multiple experiments in ordnance. Adding more experiments scattered across various atmospheric aspects might allow players of various knowledge levels to still have something engaging to do. A new player should have an easier challange than to mail a 50K. While those that already can make bombs should have an easier time understanding why their bombs explode the way it does. Once they fully understand why, they can set their sights on taking advantage of another reaction to set their bomb off or hone one particular reaction down.

## Goals

* Have some intro-level challanges for new players.
* Have some semblance of late-game challanges for more experienced players.
* Explain the mechanics better for those in the middle of the road.
* Incentivize trying new things out in the department.
* Better integrate Ordnance with Experisci

## Boundaries / Dont's

* Do not incentivize people to learn ordnance by using PvP loots.
* Do not shake or change the reaction system by a huge amount.
* Disincentivize having a single god-mix that does everything.
****

# Main design pillars

## A. Framework surrounding the experiments

### A.1. New experiments

Add new experiments to the ExperiSci module. These will come in two flavours: New explosions to do, and various gas synthesis experiments. Both of these are actually supported by the map layout of ordnance right now, but there is no reason to do anything outside of making a 50k as fast as possible.

### A.2. Rewards for experiments: Cash and Techweb Boosts.

Scientific papers will add a separate experiment handling system. A single experiment will be graded into various tiers, each tier corresponding to the explosion size or amount of gas made.  Doing any tier of a specific experiment will unlock the discount for that specific reactions. A single explosion **WILL NOT** do multiple experiments (or even tiers) at once.

On publication, a partner can be selected. A single partner only has a specific criteria of experiments they want. The experiments will then be graded on "how good they are done", with the criteria being more punishing as tier increases. Publication will then reward scientific cooperation with the partnered partner. Players can spend this cooperation on techweb boosts. Techweb boosts are meant to be subservient to discount from experiments and will not shave a node's price to be lower than 500 points.

**Experiments will only unlock nodes, discounts are handled through this boost system.**
This is more for maintainability than anything.

### A.3. On Tedium

*This is a note on implementation more than anything, but I think this helps explains why several things are done.*

Due to the nature of atmospheric reactions in the game (they're all linear), tedium is a very important thing to consider. An experiment should have a sweet spot to aim for, but there should not be a point where further mastery is stopped dead on it's track with a reward cap.

Scientific Papers attempts to discourage this behaviour by having the "maximum score" scale off to infinity but with the rewards being smaller and smaller. The sweet spot is always there to aim for and should be well communicated with players, but on their last submission of an experiment topic players should be encouraged to do their best. There should always be a reward for pushing the system to it's limit as long as it doesn't completely nullify the other subdepartments. This is the reason why there is a hard limit on the number of publications and why the score calculation is a bit more complex than it needed to be.

## B. Gas Synthesis (Early-Mid Game)

Scientific papers will add one new machine that requests a tank to release x amounts of y gas. This will be accomplished by adding a tank pumping machine which will either burst or explode a tank, releasing the gas inside. The gas currently requested are BZ, Nitryl, Halon and Nob.

The overarching goal of this compressor machine is to present a gas synthesis challange for the players and to get them more accustomed to how a tank explodes. The gas synthesis part can always be changed in order to reflect the current state of atmospheric reactions.

## C. Explosion Changes (Mid-Late Game)

### C.1 Cause and effect.

The main theme of the explosion changes is establishing cause and effect of explosions. Reactions that happens inside a tank that's going to explode will be recorded and forwarded to a doppler array. Some experiments will require only a single cause to be present (think of it as isolating a variable). This is currently implemented for nobliumformation and pressure based bombs. Having other reactions occuring besides noblium formation will fail the first one, while having any reactions at all will fail the second one. 

Adding more explosions here will be a slight challange because as of now the game has only two reactions that can reliably make an explosion.

### C.2 Tools upgrade.

Doppler array has now been retrofitted to state the probable cause of an explosion, be it reactions or just overpressurization on gas merging. These should help intermediate players figure out what is causing an explosion.

Added a new functionality to the implosion compressor:
Basically performs the gas merging and reaction that TTV does in a machine and reports the results back as if someone uses an analyzer on them. Here to give players feedback so they can try and understand what is actually going on in a bomb.

## D. Player Interaction

There should be more room for more than 1 player to play ordnance simultaneously. Previously players are also able to split tasks, but this rarely happens because tritium synthesis needs only the gas chamber to be reconfigured. Now, different players can pick different experiments and work on them. Players can also do joint tasks on one single experiment. Gases like noblium will need tritium production and also a cooling module online.

Ordnance can also coordinate with their parent department on what they really need, be it money or research bonuses.

# Potential Changes

The best-case changes that can be implemented if the current roster of content isn't enough is more reactions that can be used in bombs. Eliminating bombs entirely goes against the spirit of the subdepartment, while adding new ones will need a lot of care and consideration.

Another possible change is to implement a "gas payload" bomb. Bombs that has a set number of unreacting gas inside that will increase the heat capacity, reduce the payload, and neccesitates more bespoke mixes.

Adding more gas synthesis experiments is discouraged. The main focus of ordnance should be bombs, with gas synthesis being a side project for ordnance. These are present to ease the introduction to bombs and provide some side content. 
There should be a somewhat well-justified goal in adding new synthesis experiments: e.g. BZ is there as a "tutorial" gas, Nitryl to introduce players to cooling/heating mixes, Halon to a more efficient tritium production, and Nob as a nudge to nobformation bombs and mastery over other aspects.

# Conclusion / Summary

Add more experiments to ordnance that players can take, accomplish this by:
1. Making the players perform gas synthesis or make bombs.
2. Have them collect the data, see if it fits the criteria. Explain why if it fits and why if it doesn't.
3. Have the player publish a paper.

Reward them based on how well did they do, give players agency both on the experiment phase and also publication phase.


---
TLDR: Added new experiment to toxins, added the framework for those experiments existing. Experiments comes in gas synthesis and also bombs but with more parameters. Experiments needs to be published through papers, various choices to be made there.

Implementation notes:

Because of how paper works, ordnance experiments are handled outside of experiment_handler components. My reasoning for this is twofold:

The experiments will be completed manually on publication and if the experiment isn't unlocked yet it will still be completed.
Experiment handler datums have several procs which require an atom-level parent, and I figured this is the most sensible and cleanest way to implement this without changing the experiment handler datum too much.

Small change to /obj/machinery/proc/power_change() signal ordering to adjust the state first and then send the signal. Didn't found any other usage of this signal except mine but barge down my door if it broke something.

Rewrote the ttv merge_gases() code to be slightly more readable.
A small code improvement for thermomachine to use tofixed (my fault).

Ordnance have been updated to enable the publication of papers
Several new explosive and gas synthesis experiments have been added to ordnance
Anomaly compressor has been TGUIzed and now supports simulating the reaction of the gases inside the ttv.
New tank compressor machine for toxins. You can overpressurize tanks with exotic gases and complete experiments.
Several techweb nodes are locked and require toxin experiments to complete.
Toxins can purchase boosts for various techweb nodes.
You no longer need to anchor doppler arrays for it to work.
Doppler array and implosion compressor now supports deconstruction, implosion compressor construction added.
Doppler now emits a red light to denote it's direction and it being on. Doppler not malf.
Implosion compressor renamed to anomaly refinery.
Created a new program tab "Science" for the downloader app. Removed Robotics.
Reworked the code for bombspawner (used in the cuban pete arcade game)

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[745426eff2...](https://github.com/tgstation/tgstation/commit/745426eff227ff556105147a4802540617decd7b)
#### Friday 2022-03-11 00:45:56 by LemonInTheDark

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
## [yuwata/systemd-stable](https://github.com/yuwata/systemd-stable)@[0863a55ae9...](https://github.com/yuwata/systemd-stable/commit/0863a55ae95fe6bf7312b7a864d07a9e3fbee563)
#### Friday 2022-03-11 00:48:13 by Lennart Poettering

pid1: set SYSTEMD_NSS_DYNAMIC_BYPASS=1 env var for dbus-daemon

There's currently a deadlock between PID 1 and dbus-daemon: in some
cases dbus-daemon will do NSS lookups (which are blocking) at the same
time PID 1 synchronously blocks on some call to dbus-daemon. Let's break
that by setting SYSTEMD_NSS_DYNAMIC_BYPASS=1 env var for dbus-daemon,
which will disable synchronously blocking varlink calls from nss-systemd
to PID 1.

In the long run we should fix this differently: remove all synchronous
calls to dbus-daemon from PID 1. This is not trivial however: so far we
had the rule that synchronous calls from PID 1 to the dbus broker are OK
as long as they only go to interfaces implemented by the broke itself
rather than services reachable through it. Given that the relationship
between PID 1 and dbus is kinda special anyway, this was considered
acceptable for the sake of simplicity, since we quite often need
metadata about bus peers from the broker, and the asynchronous logic
would substantially complicate even the simplest method handlers.

This mostly reworks the existing code that sets SYSTEMD_NSS_BYPASS_BUS=
(which is a similar hack to deal with deadlocks between nss-systemd and
dbus-daemon itself) to set SYSTEMD_NSS_DYNAMIC_BYPASS=1 instead. No code
was checking SYSTEMD_NSS_BYPASS_BUS= anymore anyway, and it used to
solve a similar problem, hence it's an obvious piece of code to rework
like this.

Issue originally tracked down by Lukas Märdian. This patch is inspired
and closely based on his patch:

       https://github.com/systemd/systemd/pull/22038

Fixes: #15316
Co-authored-by: Lukas Märdian <slyon@ubuntu.com>
(cherry picked from commit de90700f36f2126528f7ce92df0b5b5d5e277558)
(cherry picked from commit 367041af816d48d4852140f98fd0ba78ed83f9e4)

---
## [andrassy/elasticsearch](https://github.com/andrassy/elasticsearch)@[37ea6a8255...](https://github.com/andrassy/elasticsearch/commit/37ea6a8255623d41be7df11440610ffa958ce50e)
#### Friday 2022-03-11 00:57:17 by Nik Everett

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
## [Gandalf2k15/tgstation](https://github.com/Gandalf2k15/tgstation)@[3bd5a2d8df...](https://github.com/Gandalf2k15/tgstation/commit/3bd5a2d8df49213708540f1c0ffe0873b5d2e233)
#### Friday 2022-03-11 01:22:44 by Wallem

Makes Ants glow, puts a minimum on ant screaming and shoe permeability, and other ant-related things. (#64786)

I found out how emissives work and my first thought was "damn ants should glow that would look sick"
So now they do.

Also, having less than 5u ants in your body will make you not scream, so 0.0001u ants will no longer have that tiny chance of making someone scream for their life.

If an ant pile has a max damage value less than 1, then they won't be able to bite through your shoes. This is the same threshold as the second tier ant icon.

Makes the giant ant a hostile mob with the neutral faction, meaning they will attack anything not in the neutral faction.

---
## [NBtheMC/The-Adventurers-Guild](https://github.com/NBtheMC/The-Adventurers-Guild)@[5c73ebe393...](https://github.com/NBtheMC/The-Adventurers-Guild/commit/5c73ebe3931add9eb1cb88f560425dba12112f72)
#### Friday 2022-03-11 02:29:00 by Eric Long

OMG so many fucking storylets

they're fucking done. And they're mostly setup. Yeah. sure.

---
## [ozzono/scripts](https://github.com/ozzono/scripts)@[91deea4944...](https://github.com/ozzono/scripts/commit/91deea49442df4c1def13834105ab39021799e5a)
#### Friday 2022-03-11 03:39:11 by Hugo Virgílio

Fortune Commit: My own dear love, he is strong and bold
	And he cares not what comes after.
His words ring sweet as a chime of gold,
	And his eyes are lit with laughter.
He is jubilant as a flag unfurled --
	Oh, a girl, she'd not forget him.
My own dear love, he is all my world --
	And I wish I'd never met him.
		-- Dorothy Parker, part 1

---
## [Perl/perl5](https://github.com/Perl/perl5)@[21a660d604...](https://github.com/Perl/perl5/commit/21a660d60415c5fba54f60fa7bd58e24c710b117)
#### Friday 2022-03-11 04:51:09 by Yves Orton

Create Porting/MANIFEST.dev as a complement to MANIFEST and related infra

This file is intended to list all the files in the repo which are not
listed in the main MANIFEST file, and which are used only for
development purposes, especially those files which are only useful when
working in a git checkout of the main perl git repository.

The files it contains will NOT be added to the production tarball
release. The file has the exact same format as the main MANIFEST:
"file\t+description" or "file".

Q. Why didn't I call this Porting/MANIFEST as mentioned in the
   discussion thread that lead to this patch?

A. The main reason was that Porting/README.pod includes a list of files
   in Porting with descriptions and explanations for what the files do
   or how they are used. In several places the file refers to
   "MANIFEST", which lead to ambiguity that would have had to be
   resolved by changing all the entries to refer to "Porting/whatever"
   instead. It was much simpler to give the new file an extension, and I
   thought that '.dev' suggests it is for "development" purposes.

Q. Why isn't this using MANIFEST.skip style functionality?

A1. Various parts of our build and test process expect to read the
    MANIFEST file and then do things based on the entries contained
    within. Eg, run tests, or extract data, or compare the file list to
    content in another file. Those parts of our build process would
    break if we used a skip style list of regexen. So it would be more
    work to teach them to deal with such a file, assuming it was
    actually doable - given the additional work I have not considered it
    deeply. On the other hand teaching that logic to simply read two
    files was and is easy.

A2. I think each file we have in the repo should have a description.
    This patch currently doesn't provide a description for each, but it
    does for many, especially those migrated from MANIFEST.

A3. I think that MANIFEST.skip style files of exclusion regexens and
    globs are error prone and easy to mess up, for instance by excluding
    far more than you had intended to. They can also be annoying to get
    right, obviously not impossible, but sometimes annoying. Explicitly
    listing everything is easy in every way, especially to mechanize.

A4. I would like to be able to move verbatim entries from our existing
    MANIFEST into the new Porting/MANIFEST.dev, description and all.
    MANIFEST.skip style files do not support descriptions except as
    comments as far as I recall. That would have meant munging the data
    from MANIFEST during the move process which would be annoying.

A5. I would like to be able to reuse our sorting logic to keep the files
    nicely sorted in a way where the file is somewhat readable. A list
    of skip files would be less amenable to doing so.

Q. There is a lot of duplicated logic related to testing manifests,
   should we refactor it out into a module or some resuable tool set?

A. YES! We already have Porting/manifest_lib.pm, but it currently does
   not declare a package, and it only contains one function. Instead of
   adding yet more code that depends on requiring a file and having it
   inject subs into package main I decided that doing the refactoring
   could wait for a separate commit or PR. But I definitely think we
   should refactor as much of this logic as possible.

Q. Some of the test files were fairly significantly changed, are you
   sure you didn't break or drop any of the tests?

A. I am reasonably confident I did not. Secondary review appreciated.
   Some of the touched files are quite old and obviously "quick hack"
   scripts. By rewriting them quite a bit I was able to simplify and
   perform some of the tests in different ways or parts of the script.
   As far as I know I didn't drop any.

Q. Why didn't you use newer features in the rewrite?

A. I am a bit conservative in my taste, and I like build tools to be
   able to run on older perls, and for things like this I prefer to
   stick with what I know well. Patches welcome.

Q. Why didn't you move more of the stuff we shouldn't bundle with
   our releases?

A. I figured someone like Nicolas R. (who helped motivate this patch)
   would feel left out if I didn't leave him anything to do. :-)

---
## [dandelion64-Repos/android_kernel_xiaomi_dandelion](https://github.com/dandelion64-Repos/android_kernel_xiaomi_dandelion)@[cf9f829523...](https://github.com/dandelion64-Repos/android_kernel_xiaomi_dandelion/commit/cf9f829523c09272ddddad7decc0e4f15b4976bb)
#### Friday 2022-03-11 04:53:09 by Christian Brauner

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
        kernel/signal.c - struct kernel_siginfo does not exist in 4.9
        kernel/sys_ni.c - cond_syscall is used instead of COND_SYSCALL
        arch/x86/entry/syscalls/syscall_32.tbl
        arch/x86/entry/syscalls/syscall_64.tbl

(1. manual merges because of 4.9 differences
 2. change prepare_kill_siginfo() to use struct siginfo instead of
kernel_siginfo
 3. exclude kill() changes to avoid struct kernel_siginfo usage
 4. exclude copy_siginfo_from_user_any() to avoid struct kernel_siginfo usage
 5. use copy_from_user() instead of copy_siginfo_from_user() in copy_siginfo_from_user_any()
 6. replaced COND_SYSCALL with cond_syscall
 7. Removed __ia32_sys_pidfd_send_signal in arch/x86/entry/syscalls/syscall_32.tbl.
 8. Replaced __x64_sys_pidfd_send_signal with sys_pidfd_send_signal in arch/x86/entry/syscalls/syscall_64.tbl.)

Bug: 135608568
Test: test program using syscall(__NR_pidfd_send_signal,..) to send SIGKILL
Change-Id: I00f1c618b2e9dbafae4d4113ad4d8a1a44b6957c
Signed-off-by: Suren Baghdasaryan <surenb@google.com>

---
## [DoveOfPiece/ashtom](https://github.com/DoveOfPiece/ashtom)@[3a07467bc7...](https://github.com/DoveOfPiece/ashtom/commit/3a07467bc7c7703788239b9422f9fd6a92950016)
#### Friday 2022-03-11 07:07:29 by DoveOfPiece

Create Stop war22 in Ukraine…!

While Ukraine is under missile attacks GitHub could be used by Russians to develop apps and platforms aiming to destabilize Ukrainian web resources.  
Please, prevent these actions and don't stay on the same side with invaders! All information about war can be found at:  https://war.ukraine.ua/   
We urge you to close GitHub for Russia and its developers! We value your support and we are in need for your actions!

It is not a shame, it is a disgust. The balance of peace in the world is ruined. Nobody knows the end of this cruelty. But humans. Real humans will not wash their hands in blood, will you? If Yes, this will be also blood of your kids, friends, parents. In future. 

Long live Ukraine.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[6a72ef0aae...](https://github.com/mrakgr/The-Spiral-Language/commit/6a72ef0aae705b3256699c7bac0a95ce25a880ed)
#### Friday 2022-03-11 08:10:28 by Marko Grdinić

"2:35pm. https://nautil.us/deep-learning-is-hitting-a-wall-14467/

If symbol manipulation is to be merged with NNs, as Marcus recommends, then better hardware is needed. GPUs aren't a good fit for that approach. AI chips could do it.

I wanted to make that comment. Let me finish reading this and I will start.

2:40pm. Let me start.

It is time to go into the action. Let me take care of that leaf.

2:45pm. Oh wow, the attribute paint even considers stroke. It is very nice!

2:55pm. Hmmm, instead of putting the material outside, wouldn't it be possible to put it inside as a detail attribute? That would be ideal.

3:05pm. Ah, I've just realized that the material assignment must always be a primitive. So no detail. But it does seem like it would work on individual faces.

Oh that does work. Interesting. This has potential.

3:10pm. https://www.sidefx.com/docs/houdini/nodes/sop/pack.html

I really want detail attributes to go from and to the packed primitive.

3:25pm. Forget trying to preserve the old architecture. For things like subdividing the petals and the leaves doing that before packing them will work fine. I can have two nulls as two different resolution outputs. Let me do the branches just a tad.

3:40pm. Why are point attributes being interpolated in such a strange manner?

4:05pm. Ok, at least the subdiv interpolation looks great.

The way they are interpolated in the viewport and in V-Ray is different, but it is not a problem ultimately.

4:15pm. I am thinking way too hard about this as usual. Let me just move on.

Wow, I hate that I can't just unpack, subdiv and repack like before. Let me ask about this. It is an real eyesore.

You know what, when unpacking I'll just transfer them to primitives and back. That is the easiest way. Just why am I racking my brain over this?

5pm. Interesting...actually let me test this with instancing before I just to conclussions.

Yeah, great. It does not work on faces, but when nesting packed primitives, it is fine if the outer primitives do not have material paths. It will just get them from the individual ones. Also I just realized why transfering the detail attributes is not done. It would lead to havoc in situations such as these where I could be packing an unpacking many different things.

5:45pm. It crashed. Damn, I should have been saving more often. I got a sense I am not doing it enough. I tried to do a quick save before the app closed in the middle of a crash and it corrupted the file. Thankfully Houd often makes backups.

5:50pm. I am a fool. Houdini is not like Blender. I should have known that trying to change structure of the nodes while it is rendering will lead to it crashing. I should have stopped and resumed the rendering. And saved before doing that.

The 'operations' nodes could not be designed any more annoying. It is hard to believe this is version 5. The plugin has been on the market for this long and they still haven't fixed this broken design. Once I have the money I am tempted to switch to Redshift just for this.

6:30pm. It looks like a funky leaf. Let me make a separate mask which is inverted for the bottom side.

8:10pm. How is it this late? I barely did anything despite going at it for the entire day.

8:35pm. Fuck V-Ray! It seems the floating point operation power node does not work. For fuck's sake!

8:45pm. I actually don't need the power op that much. The same role can be taken up by remap. I put in some sparse noise and took the min with respect to the original hues. It works well.

Once again, I've spent an entire day what should realistically take me 10m to do. But I did learn a bit.

It is actually pretty difficult to work like this. It really makes a huge difference whether I have real time feedback or 10s feedback. It makes a difference how easy the nodes are too use. It might have been better to use textures after all.

8:55pm. I've turned on the frame buffer a while ago, but I do not see any option how to save the existing image. I'll have to figure that out. For some reason the falloff texture is not really working as expected.

9:05pm. I did something pretty good now. It turns out you can just pass in a color to self illumination. now instead of white sphere, I have a yelow gradient at the borders. I made use of the falloff texture like this.

Ah yes, I might have painted the petal, but I lost that work due to the crash.

9:10pm. Note to self, use the attribute remap to put the mask in the [0,1] range. It would have made things a easier in the shader part.

9:15pm. Maybe I should have used Distance Along Geometry even for the leaf.

Right, I could have used groups to factor out the inner parts. That would have worked well. But it is not like that I did was hard. Still, I should keep it in mind. I'll probably be doing mask painting a lot in the future. I am kwetching about how textures would have been better, but I should see my current approach to its conclussion.

9:40pm. https://docs.chaos.com/display/CWVRAYMAX/GPU+Dispersion

What is dispersion?

9:45pm. No, I won't use this for the petals.

9:55pm. Let me work on the stalk.

10:10pm. Damn it, the power really does not work. I will literally have to use the remap for everything.

10:20pm. Let me work on the roughness settings for the stalk.

To start with just how did this work in Blender? V-Ray has a reflective color which I find confusing.

11:35pm. Let me just put some noise on the stalk and I will call it a day. The fatigue is really catching up to me.

11:35pm. The UV noise options really don't do a thing for some reason.

11:45pm. Random crash. Thankfully I've been saving regularly.

11:50pm. It crashed again just as I turned the bypass of on a remap node. The people working on V-Ray really aren't into concurrency or reactive programming. Or memory management.

12:10am. I am done with the flower. If I was actually good at this, I could have done it in half an hour or less. But I did get some insights today. While picking colors, I realized that the contrast between 0.01
and 0.03 blues is just as visible as between 0.1 and 0.3, and between 0.3 and 0.9. Light intensity is on a log scale up to a certain range. I think now that I understand this, my color picking should improve.

3/11/2022

9:05am. I am up. Did I forget to commit yesterday again? Yes I did. At any rate, I slept quite well. I do not know how well suited for art I am, but I am certainly motivated to do it. I am going to get started right away.

Today I want to find out two things:

* Why the UV noise in V-Ray does not work.

I thought that I was doing something wrong, but given the extreme betaness of its Houdini intergration, for all I know it might be broken.

* Try out Redshift.

Redshift does not have a crack, but I had the idea of simply rolling forward the trials using fake emails. I am going to try that. Let me state this: if it was not for V-Ray's buginess I would not even be considering it right now. I meant to get a V-Ray subscription when the the time was ripe, but now I am not sure I want it. Let me get on with it. Today I am going to stop for a while after lunch. Yesterday the session was so long that I missed the timming to take a bath."

---
## [vincentiusvin/tgstation](https://github.com/vincentiusvin/tgstation)@[0a9c61040b...](https://github.com/vincentiusvin/tgstation/commit/0a9c61040b9b32be6fd3628987dfa2c02536a4ca)
#### Friday 2022-03-11 11:00:04 by vincentiusvin

all offstation except snowdin
holy shit snowdin sucks

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[4ef2057b10...](https://github.com/mrakgr/The-Spiral-Language/commit/4ef2057b10563817c2bfeffc259cc590275cd4cb)
#### Friday 2022-03-11 11:41:48 by Marko Grdinić

"9:15am. Let me get the latest Redshift. I've made a temp email, created a new account using it and I see that this resets my trial. While that is going on, I'll try getting to the bottom of why UV noise is being messed up for me.

9:25am. Installed Redshift.

https://youtu.be/6FalgHWkhKE
V-Ray | How to RANDOMIZE your models | UVWRandomizer, Triplanar, Stochastic Tiling, MultiSubTex

Let me put this into action. I'll make a grid, put a checkerboard pattern and then try out UVRandomizer. I need to figure out why UV randomization is not working for me.

Booting up Houdini compared to Blender is night and day in how long it takes. This makes crashes that much more time consuming.

9:50am. Ok, it does work.

10am. It does work as long as you crank up the amount and lower the size. Only for the first input in the sequence though. Stochastic tiling works as well.

This restores my faith in V-Ray a bit. Let me think. What should I do next?

10:15am. Nope, making an alt Maxon account does not work for extending the Redshift trial. The license itself is keyed directly to my machine.

10:35am. I've given up on RS. Since I can't pirate it, there is no point in even considering it as an option. Instead what I've been doing is messing with UV noise. I've been trying to figure out how to apply it.

The results are somewhat bizarre. There is no problem in UV noising a texture color further using the Distortion node, but it only works with actual UVs and not the object. Also the scale for object seems to work different for 2d UVs and Object UVs.

10:40pm. Ah, yes, I forgot about making the frame buffer work. Let me just take a short break here.

* Distort.
* Frame Buffer.

11am. Let me resume.

11:05am. I've just realized something - the inbuilt UV noise is not zero centered. That could be an issue.

Also, I've figured out that it is possible to use Distort on existing textures. The UV spaces have to be the same for some reason.

11:20am. What are these distortion maps and why are there two different kinds of inputs?

11:25am. I've figured it out. The two map types just multiply each other. But if I wanted to add UV noise, instead of doing that, making use of these distortion maps is a much better choice!

Oh, color inversion literally just flips it from 0 to 1. I see.

11:35am. Ok, that settles the distortion.

Hmmmm, the invert node just does `1 - color`. This could actually be pretty useful for me.

It seems that color vectors can go above 1. What alpha. A lot of these places have alpha settings, but I have no idea what they supposed to be doing.

Ah, you can in fact separate out color channels using the Color Channel node. There is intensity and alpha there.

Oh, I was wrong. I thought that color was a 3-valued struct, but it is in fact a 4 valued struct in V-Ray. The alpha channel is in fact there, I just tried plugging it into the diffuse and it works.

I got foolded by Cd being a 3 value float.

Let me do a thing. I want to see if it can see the alpha in imported user attributes.

11:50am. Nope, it expects the user color to be 3 dimensional. I guess if I wanted to add alpha, I'd have to import it as a separate attribute.

12pm. Enough playing around. Let me watch those videos at the start. Actually, before that how do I make the frame buffer work?

https://www.youtube.com/results?search_query=vray+houdini+frame+buffer

Let me see if this gives me some hints. I can't see any save buttons. So what do I do?

12:10pm. Forget the video, I figured it out. In order to enable saving to history, I had to set the folder path first. Now it saves everything without issue. Nice.

Let me try something. Does plugging a color into a value input turn it into intensity or does it just do something stupid like grab the red channel?

12:15pm. Found a reactive bug in the frame buffer turning off A or B does not bring back the original layer unless I reload it manually. What a ripoff.

Right now I am experimenting with intensity and I see...actually I should be able to see the exact pixel vals in the frame buffer. Why am I eyeballing it?

For some reason it did not average them out, instead it is 0.321 for every channel. I am surprised it treats every channel as having the same intensity. wHat about luminosity?

12:25pm. Luminosity weights different channels differently rather than uniformly. It has two outputs that each do the same thing for some reason.

That having said, I was wrong that the values are 0.321. It is averaging them, it is just that after the rendering is done it seems less bright due to the lighting. This is a more likely explanation. Even with the luminance calc I get the same issue. So it is not that the values are off, it is just how the render comes out due to the light falloff.

Good.

What about the alpha? It get thrown away.

Ok.

12:40pm. https://www.youtube.com/watch?v=6FalgHWkhKE
V-Ray | How to RANDOMIZE your models | UVWRandomizer, Triplanar, Stochastic Tiling, MultiSubTex

https://www.youtube.com/watch?v=BbEQLYAm-YA
BerconTile and Multitexture

Let me stop here for the morning. I'll watch these after the break.

I really needed to take some time do research on how V-Ray works. Now my capability is up again."

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[f04b90b6e8...](https://github.com/odoo-dev/odoo/commit/f04b90b6e856bd8c1679cc728255f53fc788f8fd)
#### Friday 2022-03-11 11:42:59 by Julien Castiaux

[REF] core: HTTPocalypse (12) web ir.http & login

This commit is the 12th commit of a comprehensive refactor of our HTTP
framework. See odoo/odoo#78857 for complete historic, discussions and
rationnals.

The web module is twofold, on one side there are many controllers: /,
/web, /web/login, /web/database/selector, /web/dataset/call_kw, etc, on
the other side there is `session_info`: the method responsible to create
the web client's environ.

This module is kinda an exception as it is (with base) a server wide
module. In the case of the HTTP framework, it means that the controllers
of web are always accessible, i.e. going to / or /web/login will never
return a 404 Not Found even if the user is not connected to a database.

This is both a blessing and a curse. It is a blessing because the
controllers are always accessible it means that a new users can freely
access those routes. It is a curse because *any* user can access them,
even user who don't have a session yet thus who are not connected to a
database yet. From a developer standpoint, we have to put extra care to
correct serve users with and without a database. An example is the
/web/login route, the login/password pair is stored in a database,
without database it is impossible to validate a user login but users can
still access this route without db.

To solve this problem, there is the `ensure_db` function. This function
attempts to find a database using various sources (?db= query-string,
session db, mono db) and to save it on the user session. In case no db
is found, the user is redirected to the database selector. In a way,
this function grants a database to the user in a seamingly experience.
In a way, this function brings a welcome differentiation between
`auth='none'` with a database and `auth='none'` without a database. Such
differentiation only matters for the server wide modules as "regular"
module controllers are only accessible via the ir.http routing map, i.e.
it is not possible to declare a nodb controller outside of server wide
modules.

An important changement is the `session.authenticate` method, before it
was possible to call the method when the cursor was not yet initialized,
authenticate would open a cursor against the given database, setup a
registry and an environment and ultimately save everything on the
current request. Because the cursor is now greedily created, it is no
more possible to update the request environment when authenticating on
another database.

PR: odoo#78857
Task: 2571224

---
## [AliTaherkhany/Js-projects](https://github.com/AliTaherkhany/Js-projects)@[e926d1b137...](https://github.com/AliTaherkhany/Js-projects/commit/e926d1b137a2085a503ca3fa30bc9a038e7a4e04)
#### Friday 2022-03-11 13:31:37 by AliTaherkhany

I forgot to change the setup styling with my own !

OMG I think I fell in love with this project :laughing:

---
## [shiiion/gif_processor](https://github.com/shiiion/gif_processor)@[b0322bd621...](https://github.com/shiiion/gif_processor/commit/b0322bd62131ab661e1deb73b2016e2a36859f3c)
#### Friday 2022-03-11 13:36:10 by shiiion

fuck you more changes bad gif89 documentation deferred clear code? thanks for the info

---
## [xyberpastoril/xyberpastoril](https://github.com/xyberpastoril/xyberpastoril)@[65c1fde696...](https://github.com/xyberpastoril/xyberpastoril/commit/65c1fde696e96c56735b310acf8547f1c2a7bd3e)
#### Friday 2022-03-11 14:17:27 by Graeme Xyber Pastoril

Removed `Facebook` Social Link

I decided to make my Facebook limited to my family, close friends, work colleagues, college acquaintances, instructors, and professors. If you're someone currently outside this friend circle and wishes to contact me, please do so through my email.

---
## [ksant0s/android_kernel_samsung_universal8895](https://github.com/ksant0s/android_kernel_samsung_universal8895)@[bd0b9b2514...](https://github.com/ksant0s/android_kernel_samsung_universal8895/commit/bd0b9b25148501e940246eca4ca1e5e5f74b3626)
#### Friday 2022-03-11 14:56:23 by Masahiro Yamada

modpost: file2alias: go back to simple devtable lookup

commit ec91e78d378cc5d4b43805a1227d8e04e5dfa17d upstream.

Commit e49ce14150c6 ("modpost: use linker section to generate table.")
was not so cool as we had expected first; it ended up with ugly section
hacks when commit dd2a3acaecd7 ("mod/file2alias: make modpost compile
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

---
## [YOPED/CyberCodeOnline](https://github.com/YOPED/CyberCodeOnline)@[6d5cb134f2...](https://github.com/YOPED/CyberCodeOnline/commit/6d5cb134f217d2cfa2a14edfd3a81d4748a74fdc)
#### Friday 2022-03-11 15:36:43 by S0M3_DUD3

Updated german commen used curse words

Translations
		"Arschfresse" - Analface
		"Arschlecker" - Anallicker
		"Arschficker" - Analfucker
		"Pimmel" - other word for dick
		"Schwanzlutscher" - dicksucker
		"Kanacke" - curse word for imigrants
		"Fettsack" - "Fat guy"
		"Schlampe" - "Bitch"
		"Mutterficker" - "Motherfucker"
		"Assi" - curse word for jobless
		"Aushilfsnazi" - nazi thing

---
## [newstools/2022-cbs-news](https://github.com/newstools/2022-cbs-news)@[7f1b87b2a2...](https://github.com/newstools/2022-cbs-news/commit/7f1b87b2a2cce5c7ce8146586dce96573153dd2e)
#### Friday 2022-03-11 17:12:26 by Billy Einkamerer

Created Text For URL [www.cbsnews.com/news/will-smith-on-forgiving-his-father-thoughts-of-suicide-and-king-richard/]

---
## [SpaceDragon00/fulpstation](https://github.com/SpaceDragon00/fulpstation)@[c797bf79ea...](https://github.com/SpaceDragon00/fulpstation/commit/c797bf79ea71c9fd26f598306753a9abc55427d8)
#### Friday 2022-03-11 18:12:59 by Pepsilawn

Fixes broken ass area on Helios tation (#440)

* Fixes Helios

* fuck you turbine

* MACHINERY/wish_granter

---
## [Spu7Nix/SPWN-language](https://github.com/Spu7Nix/SPWN-language)@[9a8fd13a0d...](https://github.com/Spu7Nix/SPWN-language/commit/9a8fd13a0d49eec2a1a776ec8a4fdbf12e7790a8)
#### Friday 2022-03-11 19:11:36 by SpeckyYT

Fixed multiplying macros allocating 18 exabytes on negative numbers (#229)

* fixed mult allocating 18 exabytes on neg numbers

* fuck you baltimore

---
## [G3-Studio/Grief-Day](https://github.com/G3-Studio/Grief-Day)@[bfe839ebec...](https://github.com/G3-Studio/Grief-Day/commit/bfe839ebecca217d4b0f045b44526cad2073eaaa)
#### Friday 2022-03-11 21:39:00 by Vincent Gonnet

I commited a horrible and unbelievable sin, sorry Teddy, shall you forgive me master

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[a05aa36834...](https://github.com/mrakgr/The-Spiral-Language/commit/a05aa368347528940dba3c086bbb81708e8c050e)
#### Friday 2022-03-11 22:20:25 by Marko Grdinić

"2:10pm. https://www.otherlife.co/power/
> The defining characteristic of individuals who rise to power through the bottom-up path is that they publish high volumes of work with high variance in quality.

I should follow this guy more often.  He is right. If I want ot get noticed I am going to have to get into the swing of getting things out. I've been actually good at this while writing Simulacrum, but right now what I am really consistent is in learning.

There is no need to rush things. At some point my productive capability will move from learning to actually producing. I am already doing the best I can.

At any rate, I am done with breakfast and chores.

Let me watch those two video. But what I really want to do now is take a bath. The fact that my sessions have started lasting an unearthly amount has messed up my schedule. Well, let me push it for later.

Rather than dive into the shading work, I'll think about what I want to do. I feel that I have to slow down for a bit.

https://youtu.be/BbEQLYAm-YA?t=92

Hmmm, V-Ray was originally designed for applications like 3ds Max.

https://youtu.be/BbEQLYAm-YA?t=317

This video is informative, but I am confused as to what these map channels are.

https://www.youtube.com/results?search_query=v-ray+map+channel

Let me study up these map channels.

https://youtu.be/TzCjfhNettQ?t=77
Multiple Map Channels

She is saying that ever texture has a channel. Actually, this is a good thing to think about - how would you import multiple UVs.

Yeah, there is the UV Name node. It allows you to import UVs by name. This could be a choice. But what about those UV indexes? What do they represent in Houdini. I am confused about that.

2:45pm. https://www.youtube.com/watch?v=6FalgHWkhKE
V-Ray | How to RANDOMIZE your models | UVWRandomizer, Triplanar, Stochastic Tiling, MultiSubTex

Let me watch this. Maybe this will tell me what I need to know. I find it hard to follow 3ds Max tutorials.

...Ah, this is a 3ds tutorial as well. Well let me watch it for a bit.

https://youtu.be/6jLJOLjTYhM
How to Use UV Mapping Channels in 3D Studio Max for Basic Material Masking

Actually, let me watch this first.

https://youtu.be/5EUmg7KyEPk
Houdini Tutorial - Multiple UV Sets

This is a 2.5m tutorial. Let me watch it.

https://www.sidefx.com/forum/topic/54516/

Ok, this is enough info for me to just assume that 3ds Max's map channel equivalents are just names in Houdini. The real mystery is what that UV Channel Index is supposed to be doing in Houdini. But if I need multiple UVs then yes, I should just import by name. I still do not undertand why I would need this for tiling, but I guess I'll figure that out at some point.

3:10pm. Let me stop here for an hour.

I'll work on the stalk after I've taken care of hygiene. There is no point in pushing workaholic behavior. It was yesterday that I overdid it.

After I get back I will resume work by rendering a close up of the bulb and post it. I've meant to do that yesterday, but I was too tired. Actually, rather than posting the rendering of a single bulb, how about I finish the scene properly? It should be really easy as I only need the shader for the big stalk, and the frame. It might be worth it to remodel the frame so it looks more like constructions beams.

I'll do both. Let me establish my goal and I will go for it. Now that I know how to apply UV noise through the distort node I've gained a decent amount of capbility. I also have some ideas for how to use the mix node. I just need to keep going and I'll get where I want to be.

4:20pm. Ahhhh, much better.

Let me just play around with the distortion. Was I passing colored or RGB noise into it?

4:25pm. Actually, it seems that Bercon noise is in fact grayscale. Yeah, I somehow forgot this.

4:30pm. Ok, I got it. Let me take another break here.

After that I'll render the bulb part, and do the upwards shot of the vines that I've been trying to put together for what seems to be months now.

5:05pm. Let me start for real. I just realized that in the user guide it says that distortion maps are not supported on the GPU. Lame. One thing I'd really like to know is how they work. Google is being useless lately.

Let me try it again. Trying to render on the GPU crashed.

https://docs.chaos.com/display/VMAX/V-Ray+GPU+Supported+Features

There is a huge list of differences between the CPU and the GPU version. They might as well be completely different renderers.

https://docs.chaos.com/display/VMAX/V-Ray+GPU+Render+Settings
> V-Ray GPU is a separate render engine, introduced by Chaos, that utilizes GPU hardware acceleration. You can additionally use it with your CPU or combine CPU and GPU devices for hybrid rendering. Choosing the V-Ray GPU engine changes the available settings.

5:20pm. It crashes in the worst way possible when I try to use the distortion map with the GPU. It goes into an infinite loop. This was the second time I had to use the task manager to exit. When I get the money, I will seriously just switch to Redshift just to spite them for making me deal with all these bugs.

5:30pm. Just a minute or two more. I want to let it render for a bit.

5:40pm. Posted it and asked about stability of RS and Octane. Maybe the leaves could use some extra work. I should definitely try texture painting them for the added flexibility.

For now let me just move.

5:50pm. Let me add just a bit of flair to the frame.

For all its faults, Houdini's procedural workflow is a huge advantage in that like a programmer I can go back and edit things. I will add some highlight to the frame edges.

6:05pm. My first time exploring the group by angle so I am exploring a bit.

There is even something in there called toon shader attributes.

https://www.sidefx.com/docs/houdini/nodes/sop/toonshaderattribs.html
> This node let’s you set toon shader parameters for a group of primitives. Use this to color cartoon objects without using textures.

6:25pm. What I did was select the edges and turned them into curves. Now either that will work and I will make use of it, or I'll have to either resample or scatter points and use that as the distance basis.

Alternatively I could have done a remesh and then taken the curvature of that. Then beveled it. That would have kept the attributes around. Well, either way should work. Let me continue forward.

6:35pm. It is not working, but it is just like V-Ray to not tell me what is wrong.

Let me try an easier setup so I can infer how the thing works.

6:35pm. No it seems to absolutely want the object being looked at to be at the outer level. I can't just sensibly put it inside. A dumb restriction.

Instead of resampling, what if I kept the edges, but thickened them a tad.

7pm. I just used polywire instead, but the solution turned out perfect. Wonderful.

7:05pm. I figured it out. What just for the sake of the argument I used a toon shader instead. How would that look?

Oh, wow, this is my first time looking at it, and there is a ton of stuff in it!

https://docs.chaos.com/display/VMAX/V-Ray+GPU+Supported+Features

It is not supported on the GPU. It does not matter right now. I'll dedicate time to explore it. I haven't exactly decided how much realism to shoot for in my own style.

8:05pm. That is right, I turned off the small branches. Let me take a look at how it comes out.

8:25pm. Interesting. When the geometry gets really heavy, Houdini will auto convert it into boxes. Now, I love Houdini. I love that it did this instead of aborting to desktop.

8:30pm. My irritation at V-Ray just spiked. Why the hell did you stop rendering the vines!?

Because you are ignoring the output, and instead showing just the active node. Moron.

8:40pm. I've started the render. I can really feel my rig dedicating all of its resources to the task. Right now it takes me several seconds to get feedback in VS Code on what I am typing.

8:45pm. I'll let it run for 15m total. The estimate of how long it will take just keeps going up. A lot of object is one reason, sure, but even though I imagined those buld orbs to be emissive objects, this is not the brightest idea from a computational standpoint.

9:05pm. It still looks somewhat noisy even after 25m of rendering. I had a little break. Let me try changing the orbs into diffuse surfaces.

9:15pm. I'll also do a little thing to make their borders more like penumbras.

9:55pm. That feel when you want to add distortion, but remember that the GPU does not support it. I think the same goes for UV noise.

10:10pm. Finally got it. Working with color intensities is a bit like working with booleans. V-Ray feels like it is trying to get in my way the whole time, but I cracked it.

10:20pm. Let me try the shot again. I think this will be the last bit of messing around I do with it. The corona around the orbs really came out well. But I am mostly curious about how fast the scene will render. Having 5k lights less should have some effect.

10:20pm. Damn, I wish I save the closeup of the corona.

10:30pm. I find this confusing. When I press render is it actually doing on the CPU?

No, that can't be the case. I did in fact check which device it was using. How about I try using the bucket renderer instead?

Also I do not like how the orbs look dimmer. Given that the image quality nor the length it would take to render seems to have improved, I'll go back to it. I really need to try the bucket renderer. That should give me better insight in just how fast the render is progressing.

10:35pm. I like this one. After it does the bucket it ends up being super smooth! It is less taxing on the CPU as well. For rendering jobs it seems I really will benefit from a rig upgrade.

10:50pm. This really reminds me of the time I used to train agents. Right now I am watching the renderer go over the image in buckets. I am guessing the 4 buckets represent the 4 cores on my CPU.

10:55pm. It is done after 15:55m of rendering. It seems the estimate is the total time rather than the remaining. I think I should have lowered the noise threshold.

Let me post it in the Houdini thread. Maybe this would be fitting for the Twitter as well. I'll think about that.

///

>>886526
I think this came out well, though the beams are still a bit noisy. This is only half-finished. I need to add the girl and make it underwater to complete it. Plus there is the bigger overall scene that I need to deal with, but it should not be hard.

There are about 300 branches with flowers on them and 5000 flowers in the scene. Not all of them were captured in this particular shot. Not something I've want to attempt painting by hand. Houdini attracted me due to its ability to scatter points and instantiate the objects. Blender has started to get the capability to do this with its geometry nodes, but it nowhere near Houdini's level.

Despite my misgivings, I like V-Ray when it works, and the bucket renderer did a good job. The progressive renderer ended up struggling.

///

I was going to post this, but then I compared the progressive renderer image and it way less noisy I need to try lowering the noise threshold and let it churn away at it again. This image would make a good wallpaper if I could improve its quality.

11:15pm. Ok, I'll crank up the max subdivs to 48 and decrease the noise threshold from 0.01 to 0.0025. That should get me a decent image after an hour of rendering. Right now my fatigue is really hitting me. I was determined to get something done and I certainly do not have the energy to get anything else done.

11:20pm. Well, let me set it to render. It will lock up my PC after I do that so let me commit here."

---
## [Golder06/Goldbot](https://github.com/Golder06/Goldbot)@[6616a9491c...](https://github.com/Golder06/Goldbot/commit/6616a9491c5911149bc00607e94fc510b555005c)
#### Friday 2022-03-11 23:09:39 by Golder06

Added `colour` alias to `g!color`

(Fuck you Polar :p)

---
## [rorydale/pointbreakradio](https://github.com/rorydale/pointbreakradio)@[a87d3860a6...](https://github.com/rorydale/pointbreakradio/commit/a87d3860a6026618b412d4fb831217da145694d4)
#### Friday 2022-03-11 23:15:10 by Rory Dale

2022-03-11

Friday, March 11th, 2022 - the rockabilly revival show! Rockabilly, psychobilly, gothabilly (who's Billy?), swing revival, cowpunk... so many amusing and opaque genres, but the music is amazing. Today's show is a listen through somewhat chronologically to the rockabilly revival that began in the late 70s and continues through today, inspired by my friend Joe Fick releasing his Slap Bass tutorial on Discover Double Bass. If you're in the mood to swing, this might be your thing!

---
## [HumabHatterZed/WhistleWindLobotomyMod](https://github.com/HumabHatterZed/WhistleWindLobotomyMod)@[b893df6147...](https://github.com/HumabHatterZed/WhistleWindLobotomyMod/commit/b893df6147969c17f59d683eb607f83a7af73770)
#### Friday 2022-03-11 23:17:45 by HumabHatterZed

Tweaked Nothing Theres stats, reduced Nameless Fetus Awake's Health 6 --> 1, added Nothing There True sprite and emission, added Magical Girl S and Knight of Despair sprites and emissions

---

