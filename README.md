## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-08-05](docs/good-messages/2022/2022-08-05.md)


1,885,190 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,885,190 were push events containing 2,834,410 commit messages that amount to 216,845,054 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 35 messages:


## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[5dc17bd865...](https://github.com/tgstation/tgstation/commit/5dc17bd86556c01cc0f81f54a6ce270169c00088)
#### Friday 2022-08-05 00:02:36 by san7890

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
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[f0cef47678...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/f0cef47678384716080d4cc2adfa8be85b9ddc69)
#### Friday 2022-08-05 00:03:06 by SkyratBot

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
## [CubicMC/cubic-server](https://github.com/CubicMC/cubic-server)@[7cf11fb758...](https://github.com/CubicMC/cubic-server/commit/7cf11fb75810a51cef2bf8fcbfaa29eef1e4ffec)
#### Friday 2022-08-05 00:24:25 by Alexandre Flion

Finish handshake status packet parsing

My god that was pain
And the code looks like shit

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[b4f19a7e0f...](https://github.com/tgstation/tgstation/commit/b4f19a7e0fc3802856ec4117eb71418287c51ac6)
#### Friday 2022-08-05 00:39:05 by John Willard

Greatly increases Pun Pun's abilities and strengths (using desk bells, cross stun immunity) (#68870)


About The Pull Request

Pun Pun has a new AI, with it they received the following:

    Instead of screeching/roaring/scratching/jumping/rolling, Pun Pun will instead sing/dance/bow/clear throat/sign.
    Pun Pun now rings desk bells instead of finding random shit to pick up, and doesn't intentionally seek out weapons.
    Pun Pun has a higher chance of giving people stuff in their hand, so the Bartender can give them a drink and let them go walking around.

Additionally:

    Pun Pun is now immune to being hardstunned by walking into them, giving them a little more bite for greytiders beating them up.
    Monkeys can now use desk bells.

Why It's Good For The Game

I like Pun Pun and when Monkey AIs were originally added, there was a note about giving them a unique AI. Since we're slowly turning the poor monkey into an actual Bartender assistant, I find it thematic that they would ring the bell and give out drinks in their hand, as if the Bartender taught them themselves.

For the hardstun immunity, I mostly did it because I find it annoying for a Bartender to have to carefully navigate around Pun Pun to not knock them over and make them drop an instrument (or anything else) in their hand, but it also works as a buff to people trying to kill them. Pun pun is a unique monkey so I don't believe they should be as easy to kill as any other.

Desk bell addition was necessary for Pun Pun to use it.
Changelog

cl
add: Pun Pun now gives stuff in their hand frequently and rings desk bells.
add: Pun Pun now has gentleman-like emotes, rather than screeching and roaring.
balance: Pun Pun no longer looks for weapons in their off time.
balance: Pun Pun is no longer vulnerable to stuns by being walked into.
qol: Monkeys can now use desk bells.
/cl

---
## [sjp38/linux](https://github.com/sjp38/linux)@[45c69de43a...](https://github.com/sjp38/linux/commit/45c69de43ac8d34764f2044b22ea7141d308cec2)
#### Friday 2022-08-05 01:18:35 by Johannes Weiner

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
## [lyq628/research_postgres](https://github.com/lyq628/research_postgres)@[c40ba5f318...](https://github.com/lyq628/research_postgres/commit/c40ba5f318f96a6a5a29729b987ead11c5dc65c1)
#### Friday 2022-08-05 01:34:57 by Tom Lane

Fix rowcount estimate for SubqueryScan that's under a Gather.

SubqueryScan was always getting labeled with a rowcount estimate
appropriate for non-parallel cases.  However, nodes that are
underneath a Gather should be treated as processing only one
worker's share of the rows, whether the particular node is explicitly
parallel-aware or not.  Most non-scan-level node types get this
right automatically because they base their rowcount estimate on
that of their input sub-Path(s).  But SubqueryScan didn't do that,
instead using the whole-relation rowcount estimate as if it were
a non-parallel-aware scan node.  If there is a parallel-aware node
below the SubqueryScan, this is wrong, and it results in inflating
the cost estimates for nodes above the SubqueryScan, which can cause
us to not choose a parallel plan, or choose a silly one --- as indeed
is visible in the one regression test whose results change with this
patch.  (Although that plan tree appears to contain no SubqueryScans,
there were some in it before setrefs.c deleted them.)

To fix, use path->subpath->rows not baserel->tuples as the number
of input tuples we'll process.  This requires estimating the quals'
selectivity afresh, which is slightly annoying; but it shouldn't
really add much cost thanks to the caching done in RestrictInfo.

This is pretty clearly a bug fix, but I'll refrain from back-patching
as people might not appreciate plan choices changing in stable branches.
The fact that it took us this long to identify the bug suggests that
it's not a major problem.

Per report from bucoo, though this is not his proposed patch.

Discussion: https://postgr.es/m/202204121457159307248@sohu.com

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[5fba1b8b1c...](https://github.com/treckstar/yolo-octo-hipster/commit/5fba1b8b1cae30cf48ffa2f2beabb2e68e6750c3)
#### Friday 2022-08-05 02:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [YellowHCH/thefuck](https://github.com/YellowHCH/thefuck)@[7f97818663...](https://github.com/YellowHCH/thefuck/commit/7f97818663de9351ac7e2c6314ed94184811d62a)
#### Friday 2022-08-05 02:22:17 by Romain Heller

#455: [README] Add uninstall instructions (#1171)

* ~[Doc] Add Uninstall instructions

As we need the package and to modify the shell config, users could have a pain in the ass when it comes to retire *The Fuck* from the system.

* Update README.md

* Update README.md

Co-authored-by: Pablo Aguiar <scorphus@gmail.com>

---
## [kleinerm/Psychtoolbox-3](https://github.com/kleinerm/Psychtoolbox-3)@[c4e7808150...](https://github.com/kleinerm/Psychtoolbox-3/commit/c4e7808150009caa232767696d32f91063b4f2e4)
#### Friday 2022-08-05 03:02:11 by kleinerm

Merge pull request #775 from kleinerm/master

Pull for 3.0.18.11 update

This is mostly a release with smaller quality of life improvements, some bug/compatibility fixes, and more work to take advantage of new Ubuntu 22.04-LTS features and improvements.

### General

- Various help text and documentation updates. Minor cleanups and improvements, maintenance work etc.

- PsychVRHMD: Prep work for future OpenXR driver, and some cleanups and minor fixes.

- PsychPortAudio: Add new AM modulator flag 256 "kPortAudioAMModulatorNeutralIsZero". By default, a stopped AM modulator device acts as if no AM modulator is attached. With this flag set, while attached to an audio output slave device, it will instead "gate" or "mute" sound output on its associated audio output device, iow. the AM gain value during stopped modulator is zero instead of one. This has proven useful to allow to output tone bursts that are windowed/gated/modulated by an envelope function. Sponsored by a paid support membership - Thanks.

- Eyelink: Fix potential false "buffer overflow" alert in 'EyelinkGetQueuedData', which can cause Octave/Matlab to abort() as a false alarm. Sponsored by SR-Research, paying members of our partnership program - Thanks.

### Linux

- XOrgConfCreator: Split up into a legacy version for systems with X-Server 1.20 and earlier, e.g., Ubuntu 20.04-LTS, and a modern version for systems with X-Server 21 and later, e.g., Ubuntu 22.04-LTS. The legacy version is now in maintenance mode, frozen in its behaviour for old systems. The X-Server 21 / Ubuntu 22.04-LTS version was cleaned up, extended and made more plug and play. It hides some rarely needed (for normal users) options behind a "expert mode" flag, simplifies the questions it asks to users, streamlines the whole setup experience, and exposes some new functionality only available on modern X-Server 21, e.g., AsyncFlipSecondaries support for clone/mirror display setups (subject + experimenter displays) which are not synchronized. Improvements to deep color setup, Prime renderoffload "Optimus" setup, VRR setup etc.

- Deal better with problems in AssertOpenGL, giving better troubleshooting advice -- now updated for Ubuntu 22.04-LTS

- Gamepad/GetGamepadIndices: Refinements for Linux/X11, help text updates. Make selection of the proper GamePad / Joystick device more simple and robust. This work supported by a Psychtoolbox paid support membership - Thanks.

### macOS

- PsychVulkan: Add a new workaround for another macOS Metal bug. Make visual presentation timing it a bit better, but still quite awful.

- Screen('AddFrameToMovie'): Change mapping of 'rect' to actual capture area. The old math didn't determine vertical start position of the capture rectangle by rect(kPsychTop), but based on rect(kPsychBottom), which could cause inconsistencies on movie frame capture area on macOS with Retina displays in Retina backwards compatibility mode. The new math fixes this, to deal with Retina displays better.

- Maybe restore backwards compatibility of Psychtoolbox 3.0.18 with macOS versions older than 10.15 Catalina, possibly back to 10.11 El Capitan with fixes to Screen and PsychPortAudio. This is untested, due to lack of any macOS test systems other than 10.15.7 Catalina final, but may work. Maintaining backwards compatibility is difficult without test systems and the constant breakage introduced by the iToys company in more recent SDK's and compiler toolchains. Officially we don't guarantee that current 3.0.18 runs on anything but Catalina.

---
## [crawl/qw](https://github.com/crawl/qw)@[1b253f7141...](https://github.com/crawl/qw/commit/1b253f7141c1c9159d1695c7a75228f18735f9f9)
#### Friday 2022-08-05 03:36:05 by gammafunk

feat: Improve zealot handling of GOD_LIST

Previously, `GOD_LIST` had to include the god of any zealot combo that
was being played to prevent qw from abandoning its starting god
immediately.  This was presumably to support abandoning Xom as a chaos
knight. But this behaviour makes configuring other zealots difficult,
since if their start god isn't in the god list, they'll abandon
immediately. If we add their starting god(s) to the god list, all other
combos will consider those zealot gods as viable options to join, which
may not be what a user wants.

This commit has all zealots set the c_persist.joined_initial_god
variable we use to track god worship. This way they won't abandon if
their god isn't in `GOD_LIST`. For chaos knights, we add a
`CK_ABANDON_XOM` variable, defaulting to true, to the rcfile. The
abandonment will proceed specifically for chaos knights who are
currently worshiping Xom when this variable is true.

---
## [david-rowley/postgres](https://github.com/david-rowley/postgres)@[ec62cb0aac...](https://github.com/david-rowley/postgres/commit/ec62cb0aac5ba31a82339606009ddbd7eb00e2ac)
#### Friday 2022-08-05 03:39:45 by Tom Lane

Revert applying column aliases to the output of whole-row Vars.

In commit bf7ca1587, I had the bright idea that we could make the
result of a whole-row Var (that is, foo.*) track any column aliases
that had been applied to the FROM entry the Var refers to.  However,
that's not terribly logically consistent, because now the output of
the Var is no longer of the named composite type that the Var claims
to emit.  bf7ca1587 tried to handle that by changing the output
tuple values to be labeled with a blessed RECORD type, but that's
really pretty disastrous: we can wind up storing such tuples onto
disk, whereupon they're not readable by other sessions.

The only practical fix I can see is to give up on what bf7ca1587
tried to do, and say that the column names of tuples produced by
a whole-row Var are always those of the underlying named composite
type, query aliases or no.  While this introduces some inconsistencies,
it removes others, so it's not that awful in the abstract.  What *is*
kind of awful is to make such a behavioral change in a back-patched
bug fix.  But corrupt data is worse, so back-patched it will be.

(A workaround available to anyone who's unhappy about this is to
introduce an extra level of sub-SELECT, so that the whole-row Var is
referring to the sub-SELECT's output and not to a named table type.
Then the Var is of type RECORD to begin with and there's no issue.)

Per report from Miles Delahunty.  The faulty commit dates to 9.5,
so back-patch to all supported branches.

Discussion: https://postgr.es/m/2950001.1638729947@sss.pgh.pa.us

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[ba6fceff4e...](https://github.com/mrakgr/The-Spiral-Language/commit/ba6fceff4e7862277805ff81d8166bcdee147cae)
#### Friday 2022-08-05 08:38:03 by Marko Grdinić

"8:20am. Nothing of note in the mail.

At first I was fearful, then I was anxious, then I was sad, and towards the end of yesterday I became perplexed. That is how I am now.

8:35am. I am reflecting on my past mistake. Before I became a programmer I was a trader and I came at it with the same strong-willed, intense if lazy approach. The end result was failure. I learned to trade, but not so much how to make money.

I think maybe if I was less willful about it the results would have been different. With programming writing the early arc of Simulacrum inspired me to pursue the Singularity, but in the end what was the point of that if I am only going to come to the conclussion that I need to use the machine to derive the result?

If I got those AI chips now, sure, I'd have an edge due to having Spiral, but given enough time I am sure that the Deepmind guys will be able to do it themselves.

So what was the point? Do I have a single path of advancement left to me?

Freelancing could be different if there were different ranks to it. Like in those adventure guilds, you could start at the bottom taking F ranks, and then work your way up to something that pays well. But from what I've seen of Freelance and Upwork, all the work is F rank and I do not know if there is any chance of advancement, so that makes it very unappealing as a path.

Jobs are weird. Suppose programmers were wizards, and you have beginner programmers which can only cast lvl 1 spells all the way to the experts which can cast lvl 3,4,5.

I was better than my cohort in high school, but it is not like I have anyone to compare myself. I might be a lot better than my past me, but maybe I am just a frog in a well thinking he is lvl 5 when he is really lvl 3. So suppose I start applying and get rejected saying: 'Oh no, based on the level of expertise demonstrated you are just a level 3 wizard, we want somebody who is at least level 5.'

I could accept it. It would give me a goal and something to strive for.

But this scenario where I am being tested on my attitude and personality, as well as only tested on the bare minimum of my skill sits ill at ease for me. This kind of atmosphere turns me off and is making me unsure whether I even want a job to begin with. Forget lying on my resume and bullshiting for a moment.

Fundamentally, the job of the recruiters should be to gauge my skill accurately and hire me based on that. If it is not, I should find a place where it is.

Imagine if the application was for a neurosurgeon. You probably wouldn't care whether the guy was charming and personable, but whether he would kill the patient or not.

The job I want should test the extremity of my skill.

8:55am. So when I stopped programming last year, I went into art and cultivated my 3d skills, but it is not really my talent.

What would have made sense back then would be to start writing immediately.

My problem is that it is hard to have a strong attitude when you go into writing. Back in 2014, I figured out an important part of reality and was filled with pride, but right now I do not feel like I've discovered anything more noteworthy. Sure based on 7 years on programming I could put some twists to get closer to the truth, but it is not fundametally as earthshaking.

It is simply impossible for me to emulate the attitude of the 2014 early arcs. I have nothing to warrant such a level of will and confidence.

9:10am. But maybe that is the wrong reason to write.

The last thing I read was the Legendary Mechanic. It was fun for a bit, but it is a story about a robot of a human who only wins and ever grows stronger. It does not have much value as a literary work.

Right now, I am thinking and I am coming to the conclussion that this humbled, perplexed attitude might be the ideal way to approach the story. It will give it a sense of balance and contrast that would not be there otherwise. Plus writing with a strong attitude is very draining.

What if I wrote the same way I am keeping this journal?

9:15am. For the upkeep of the journal I wasn't ever straining my willpower. I was just airing my thoughts all along.

9:20am. I can't really approach writing saying my goal is to get 1k subscribers or something like that. I have zero way of making that happen. It is not a game where I can improve by taking different choices and actions. It makes no sense to approach writing as if it were combat or sports. Writing is one place where it is obvious you are not competing based on technical proficiency. There aren't rules and they don't matter.

9:30am. Maybe I need to go back to the way I was during my school days. Coming to an understand of the self improvement loop burst forth a wave of desire in me to become a programmer, but back then I didn't know anything about it. I only had an idea that purpose of life is to attain omnipotence and was looking for a path to attain it that would be realistic. I must have spent over a decade nursing this deep seated belief and desire.

I do not hate that old me. I think that holding on to my belief back then was the only thing of worth to me.

9:35am. I am going to start writing, but first I want to digest this grief and perplexity. I'll reaffirm the strong desire in me, and while I am holding on to it, write on the side. I won't bother trying to put it into the work itself like back in 2014.

I cannot do without it.

A strong desire is like a light that illuminates your life.

9:50am. I need to change just a bit.

Let me do my morning reading instead of just standing here in thought and then I will go back to bed.

10:35am. Let me go to bed. I am going to leave catching up to OPM for later. I am going to try to internalize the new mindset and do some writing after that. Maybe I'll manage to find the strength tomorrow.

It is taking me a long time as writing is not a matter of determination. Doing Heaven's Key has to take place of writing this journal.

On the plus side, at least I haven't been sleeping poorly."

---
## [LanCreates/OpenGL-practice](https://github.com/LanCreates/OpenGL-practice)@[dfd3bfb05f...](https://github.com/LanCreates/OpenGL-practice/commit/dfd3bfb05fba343c92f61a74e74dc933d12e1c5c)
#### Friday 2022-08-05 09:39:19 by Valent F.A.R

Add another VAO and window resize callback

Here I was trying to understand more about VAO. To do that, I was testing some things to see how VAO behaves. It did answer some of my curiosity too. Anyway, this is something I made while messing around with it. Man, Finding the momentum to make it like this was kinda a pain haha.

---
## [samba-team/samba](https://github.com/samba-team/samba)@[f24ef117cf...](https://github.com/samba-team/samba/commit/f24ef117cfa195ef19b8130040555b75f42ae00b)
#### Friday 2022-08-05 10:26:46 by Jeremy Allison

s3: smbd: Change srvstr_get_path_internal() to always call check_path_syntaxXXX(), even on DFS pathnames.

The original design decision to just copy a DFS path and let
parse_dfs_path() take care of it was a horrible mistake.

Fix srvstr_get_path_internal() to always return a
/server/share/path (i.e. a path separated with '/', not '\').

This is a more complex change than I like to allow
DFS path procesing in srvstr_get_path_internal() but
needed as clients (including Samba smbclient) have a
rather "fuzzy" idea of what constitutes a valid DFS path.
If we detect the DFS path isn't valid here we have to
fall back to treating it as a local path.

I also need to modify the DFS parsing in
filename_convert_smb1_search_path() to cope with only '/'
separators.

This also means parse_dfs_path() needs changing to
cope.

The changes here are best reviewed by just applying
the fix and looking at the modified functions:

srvstr_get_path_internal()
parse_dfs_path()

For parse_dfs_path() it's mostly removing bad code
and makes parse_dfs_path() much easier to read.

These changes will enable me to remove some ugly mistakes made
adding ucf_flags to extract_snapshot_token(), as
we can now always assume canonicalized paths.

This is a little messy, but has to be done in
one chunk as the change to srvstr_get_path_internal()
depends on the change to parse_dfs_path().

Thanks to Volker for the insight that made this
cleanup possible.

Signed-off-by: Jeremy Allison <jra@samba.org>
Reviewed-by: Volker Lendecke <vl@samba.org>

---
## [Ku95/bevy](https://github.com/Ku95/bevy)@[4847f7e3ad...](https://github.com/Ku95/bevy/commit/4847f7e3adc835053a8907dd578c342b4bd395e2)
#### Friday 2022-08-05 10:44:39 by ira

Update codebase to use `IntoIterator` where possible. (#5269)

Remove unnecessary calls to `iter()`/`iter_mut()`.
Mainly updates the use of queries in our code, docs, and examples.

```rust
// From
for _ in list.iter() {
for _ in list.iter_mut() {

// To
for _ in &list {
for _ in &mut list {
```

We already enable the pedantic lint [clippy::explicit_iter_loop](https://rust-lang.github.io/rust-clippy/stable/) inside of Bevy. However, this only warns for a few known types from the standard library.

## Note for reviewers
As you can see the additions and deletions are exactly equal.
Maybe give it a quick skim to check I didn't sneak in a crypto miner, but you don't have to torture yourself by reading every line.
I already experienced enough pain making this PR :) 


Co-authored-by: devil-ira <justthecooldude@gmail.com>

---
## [google/crubit](https://github.com/google/crubit)@[7003909c14...](https://github.com/google/crubit/commit/7003909c1451352974397beda9119991a9507b02)
#### Friday 2022-08-05 11:05:52 by Devin Jeanpierre

Partial and hacky fix for ElaboratedType-related errors.

This really is my best short right now! I tried being cleverer with how each case handles desugaring, but, for example, one problem I think I am running into is that they generally expect to fully desugar all the way past all sugar nodes, but the nodes we're casting are themselves sugar nodes -- so they skip past both the ElaboratedType and the very node they were meant to match. (Where, before, as a special-case, they matched the node because it wasn't nested inside other sugar.)

(Or in other cases I just seriously don't understand why `getAs`/`getAsAdjusted` don't do what I expect, to be honest. Presumably something like "The Canonical type isn't what I expect"...)

This doesn't fix all tests; I do not currently understand why this happens:

```
thread 'test_incomplete_record_has_rs_name' panicked at 'input unexpectedly didn't match the pattern:
expected '"test_namespace_bindings::MyTemplate<test_namespace_bindings::Param>"'
but got '"test_namespace_bindings::MyTemplate<Param>"'
```

It could be that these are coincidental? There are other differences in the AST: https://godbolt.org/z/WsvKjzG6Y (e.g. `TemplateSpecializationType 'MyTemplate<Type>' sugar MyTemplate` vs `TemplateSpecializationType 'MyTemplate<ns::Type>' sugar MyTemplate`.) I'd need to dig more.

But for now, at least opting for fixing a subset of tests and getting help fixing the rest... My brain tired.

PiperOrigin-RevId: 465531292

---
## [thiagocardozo/terminal](https://github.com/thiagocardozo/terminal)@[77215d9d77...](https://github.com/thiagocardozo/terminal/commit/77215d9d77b99b48d1ee8302736178f2ec9f3a77)
#### Friday 2022-08-05 12:34:09 by Mike Griese

Fix `ShowWindow(GetConsoleWindow())` (#13118)

A bad merge, that actually revealed a horrible bug.

There was a secret conflict between the code in #12526 and #12515. 69b77ca was a bad merge that hid just how bad the issue was. Fixing the one line `nullptr`->`this` in `InteractivityFactory` resulted in a window that would flash uncontrollably, as it minimized and restored itself in a loop. Great. 

This can seemingly be fixed by making sure that the conpty window is initially created with the owner already set, rather than relying on a `SetParent` call in post. This does pose some complications for the #1256 future we're approaching. However, this is a blocking bug _now_, and we can figure out the tearout/`SetParent` thing in post. 

* fixes #13066.
* Tested with the script in that issue.
* Window doesn't flash uncontrollably.
* `gci | ogv` still works right
* I work here.
* Opening a new tab doesn't spontaneously cause the window to minimize
* Restoring from minimized doesn't yeet focus to an invisible window
* Opening a new tab doesn't yeet focus to an invisible window
* There _is_ a viable way to call `GetAncestor` s.t. it returns the Terminal's hwnd in Terminal, and the console's in Conhost


The `SW_SHOWNOACTIVATE` change is also quite load bearing. With just `SW_NORMAL`, the pseudo window (which is invisible!) gets activated whenever the terminal window is restored from minimized. That's BAD.


There's actually more to this as well. 


Calling `SetParent` on a window that is `WS_VISIBLE` will cause the OS to hide the window, make it a _child_ window, then call `SW_SHOW` on the window to re-show it. `SW_SHOW`, however, will cause the OS to also set that window as the _foreground_ window, which would result in the pty's hwnd stealing the foreground away from the owning terminal window. That's bad.

`SetWindowLongPtr` seems to do the job of changing who the window owner is, without all the other side effects of reparenting the window. 

Without `SetParent`, however, the pty HWND is no longer a descendant of the Terminal HWND, so that means `GA_ROOT` can no longer be used to find the owner's hwnd. For even more insanity, without `WS_POPUP`, none of the values of `GetAncestor` will actually get the terminal HWND. So, now we also need `WS_POPUP` on the pty hwnd. To get at the Terminal hwnd, you'll need

```c++
GetAncestor(GetConsoleWindow(), GA_ROOTOWNER)
```

---
## [thiagocardozo/terminal](https://github.com/thiagocardozo/terminal)@[9ccd6ecd74...](https://github.com/thiagocardozo/terminal/commit/9ccd6ecd744890b856f3d8a39ff0616c0e34d4fb)
#### Friday 2022-08-05 12:34:09 by Mike Griese

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
## [AirSkyBoat/AirSkyBoat](https://github.com/AirSkyBoat/AirSkyBoat)@[6ec1eb725a...](https://github.com/AirSkyBoat/AirSkyBoat/commit/6ec1eb725a01dd48b56436c37abffe85d2d8fcdd)
#### Friday 2022-08-05 15:33:27 by Abdiah

Operation Desert Swarm Implementation (#253)

* Operation Desert Storm

Evidence:
https://ffxiclopedia.fandom.com/wiki/Operation_Desert_Swarm

- Removed Adaman ingot from drop tables as sample rate contained 1/288
- Removed Mythril ingot with drop rate 0%
- Added battlefield mob type to the platoon scorpions
- Increased sword strap drop rate from 2.2% to 22% as seen in wiki

* ODS early work

* Operation Desert Swarm Full fix

Co-authored-by: OpheliaXI <heliashelium@gmail.com>

Changes:

Fixed crash that would occur when all scorpions were alive and wild rage was used
Fixed bug that caused scorpions to infinitely loop when using abilities
Corrected Wild Rage damage to scale as they die. Damage will start from ~350 and reach ~650. Extensive testing was done on this part
Fixed proper messaging from scorpions to display that they do not have enough energy to attack while on mimic cooldown - which is set to 7 seconds after the scorpions mimic one another
Scorpions will only be bound as msg IDs suggest scorpions only getting stuck and not stunned. Furthermore the crash that was earlier fixed was due to stun being applied to the scorpion

* sleep res build

Added sleep and lullaby build resistance as scorpions die
Evidence:
https://ffxiclopedia.fandom.com/wiki/Operation_Desert_Swarm#:~:text=They%20cannot%20be%20feasibly%20slept%20after%20the%203rd%20or%204th%20Sleep.%20Their%20Sleep%20resistance%20increases%20drastically%20when%20only%20few%20of%20them%20are%20left.%20Bind%20and%20Gravity%20are%20suggested.

* Death fix

Added iskiller to on mob death to prevent multiple looping for each member in the battlefield

---
## [nbdd0121/linux](https://github.com/nbdd0121/linux)@[4a557a5d1a...](https://github.com/nbdd0121/linux/commit/4a557a5d1a6145ea586dc9b17a9b4e5190c9c017)
#### Friday 2022-08-05 15:42:37 by Linus Torvalds

sparse: introduce conditional lock acquire function attribute

The kernel tends to try to avoid conditional locking semantics because
it makes it harder to think about and statically check locking rules,
but we do have a few fundamental locking primitives that take locks
conditionally - most obviously the 'trylock' functions.

That has always been a problem for 'sparse' checking for locking
imbalance, and we've had a special '__cond_lock()' macro that we've used
to let sparse know how the locking works:

    # define __cond_lock(x,c)        ((c) ? ({ __acquire(x); 1; }) : 0)

so that you can then use this to tell sparse that (for example) the
spinlock trylock macro ends up acquiring the lock when it succeeds, but
not when it fails:

    #define raw_spin_trylock(lock)  __cond_lock(lock, _raw_spin_trylock(lock))

and then sparse can follow along the locking rules when you have code like

        if (!spin_trylock(&dentry->d_lock))
                return LRU_SKIP;
	.. sparse sees that the lock is held here..
        spin_unlock(&dentry->d_lock);

and sparse ends up happy about the lock contexts.

However, this '__cond_lock()' use does result in very ugly header files,
and requires you to basically wrap the real function with that macro
that uses '__cond_lock'.  Which has made PeterZ NAK things that try to
fix sparse warnings over the years [1].

To solve this, there is now a very experimental patch to sparse that
basically does the exact same thing as '__cond_lock()' did, but using a
function attribute instead.  That seems to make PeterZ happy [2].

Note that this does not replace existing use of '__cond_lock()', but
only exposes the new proposed attribute and uses it for the previously
unannotated 'refcount_dec_and_lock()' family of functions.

For existing sparse installations, this will make no difference (a
negative output context was ignored), but if you have the experimental
sparse patch it will make sparse now understand code that uses those
functions, the same way '__cond_lock()' makes sparse understand the very
similar 'atomic_dec_and_lock()' uses that have the old '__cond_lock()'
annotations.

Note that in some cases this will silence existing context imbalance
warnings.  But in other cases it may end up exposing new sparse warnings
for code that sparse just didn't see the locking for at all before.

This is a trial, in other words.  I'd expect that if it ends up being
successful, and new sparse releases end up having this new attribute,
we'll migrate the old-style '__cond_lock()' users to use the new-style
'__cond_acquires' function attribute.

The actual experimental sparse patch was posted in [3].

Link: https://lore.kernel.org/all/20130930134434.GC12926@twins.programming.kicks-ass.net/ [1]
Link: https://lore.kernel.org/all/Yr60tWxN4P568x3W@worktop.programming.kicks-ass.net/ [2]
Link: https://lore.kernel.org/all/CAHk-=wjZfO9hGqJ2_hGQG3U_XzSh9_XaXze=HgPdvJbgrvASfA@mail.gmail.com/ [3]
Acked-by: Peter Zijlstra <peterz@infradead.org>
Cc: Alexander Aring <aahringo@redhat.com>
Cc: Luc Van Oostenryck <luc.vanoostenryck@gmail.com>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>

---
## [TheVanderlin/40K-Eipharius](https://github.com/TheVanderlin/40K-Eipharius)@[5993bf1051...](https://github.com/TheVanderlin/40K-Eipharius/commit/5993bf10514cda880474211ad1f57eb367c0ec0e)
#### Friday 2022-08-05 16:22:58 by Vanderlin

Power Sword Nerf

Holy fuck the original stats were the equiv of holding the power of a neutron star in your hand. It literally instantly kills an Astartes in one hit. Instant death. It also has 100 percent chance of decap every time even if you wear power armor.

I had to kill that shit fast.

---
## [wxifuwu/dbw](https://github.com/wxifuwu/dbw)@[3051a729c1...](https://github.com/wxifuwu/dbw/commit/3051a729c1fa600bd0dfdd31764333ae35cf7845)
#### Friday 2022-08-05 16:37:36 by Luna / wxifu

Fuck you Google for complaining about Link Content

---
## [ericberman/MyFlightbookWeb](https://github.com/ericberman/MyFlightbookWeb)@[ed9fc19185...](https://github.com/ericberman/MyFlightbookWeb/commit/ed9fc19185c30539878fbda2a892355ce545c9e6)
#### Friday 2022-08-05 16:50:17 by ericberman

Issue #967: stop using obsolete textboxwatermarkextender

 - Replace watermarks with placeholder attribute throughout
 - change crossfill and other code to use .value instead of $find(xxx).set_text/get_text
 - remove now obsolete EndorsementTextBox, EndorsementWatermark
 - fix night mode styling for menus
 - Added BIGREDBUTTONS option for authredir to make apple's fucking capricious and arbitrary app reviewers happy.  Pains in the ass.

---
## [luzpaz/gimp](https://github.com/luzpaz/gimp)@[7123b6c466...](https://github.com/luzpaz/gimp/commit/7123b6c466dcf38bb274734e9d7494c9c4fd8b8e)
#### Friday 2022-08-05 17:17:22 by Jehan

Issue #7685: g-ir-doc-tool produces broken XML.

To work around the issue, I just wrote a stupid sed script. Of course,
it means that if we encounter again the issue on some other docs, we'll
have to update it. In other words, it's neither robust nor a proper
long-term fix. Just a temporary hack.
See: https://gitlab.gnome.org/GNOME/gobject-introspection/-/issues/425

Also fixing this issue, I encountered another bug, this time in meson,
which changes backslashes in slashes on 'command' arguments, in a
completely uninvited manner! The only workaround to this is apparently
to call an external script, which is ridiculous for such a basic stuff.
But well… here is why I implement this with a script, instead of
directly calling sed in the meson 'command'.
See: https://github.com/mesonbuild/meson/issues/1564

---
## [Himemoria/android_kernel_xiaomi_mt6768](https://github.com/Himemoria/android_kernel_xiaomi_mt6768)@[793087b259...](https://github.com/Himemoria/android_kernel_xiaomi_mt6768/commit/793087b25947c66d8a499653ff5f07ccb24eb07a)
#### Friday 2022-08-05 18:08:46 by Peter Zijlstra

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
Signed-off-by: Egii <regidesoftian@gmail.com>

---
## [lefetmeofefet/rabota](https://github.com/lefetmeofefet/rabota)@[012fed3f0e...](https://github.com/lefetmeofefet/rabota/commit/012fed3f0ec820125a63ffd58b2d209b19ad637c)
#### Friday 2022-08-05 19:01:05 by Shlomo

YES!, working as a frikin thing!, opens game, goes to chest, goes to tp, goes to black marsh, fucks your mom, eats a burger with extra steez, commits suicide in hardcore mode, proceeds to delete all of your characters and confess to botting to the mods, become sentient, open a longbow kicksin that uses whirlwind, get hooked, die while fighting random minimbosses in act1 hell, get angry, start writing a bot to get unhooked, commit artifical intelligencide.+ p.s, it loops now

---
## [PCSX2/pcsx2](https://github.com/PCSX2/pcsx2)@[89f10e1605...](https://github.com/PCSX2/pcsx2/commit/89f10e160572063b4871bfb8d0c6ffff54f9543a)
#### Friday 2022-08-05 19:11:28 by RedDevilus

GameDB:  ':' to '-' + GS and other fixes

Windows doesn't like you to use ':' in folders this caused issues for when CK1 did savestates in folders and now it's also messing with unable to add covers in Qt so better to replace them and also to avoid other issues now and the future.
GS HW Fixes and other fixes for:
- Adventures of Cookie & Cream, The
- Brothers in Arms - Earned in Blood / Road to Hill 30
- Black
- Chaos Legion
- God Hand
- Knockout Kings 2001
- Kuon
- Outrun 2006 / 2 SP
- Project Eden
- Psi-Ops - The Mindgate
- Punisher, The
- Ratchet Deadlocked (USA) / Gladiator (Europe) / 3 Up Your Arsenal
- Silent Hills Origins / Shattered Memories / 3 / 4
- SoulCalibur II / III

Also made sure that the comments and their spacing were consistent.

---
## [petre-symfony/firebase-pinia-vite-vue3-aug-2022](https://github.com/petre-symfony/firebase-pinia-vite-vue3-aug-2022)@[38434255f0...](https://github.com/petre-symfony/firebase-pinia-vite-vue3-aug-2022/commit/38434255f0114be8b06256b4ec2c76b10823441c)
#### Friday 2022-08-05 20:21:15 by petrero

12.143(2) Routing - history api was introduced to solve issues of the hash system api.

  For more details acces the link https://developer.mozilla.org/en-US/docs/Web/API/History_API. We don't have to worry about the details of how the history api works because the router library will take care of it for us.
  There's another mode available called memory. This mode is when you want to keep the route changes track internally without modifying the url bar. It's not a common mode to use but is available if you ever needed. The history mode will suffice for now.
  Save your changes and view the browser. Everything will continue to work. Let's try changing the path to something else. The application will continue to render the component associated with the record. This behaviour is fine but there're a couple of things you should be aware of. First is that the page get's reloaded. If you were to view the network panel clear it out  and then change the path. This will result in a page refresh.
  This isn't an issue with vue or even javascript. This behaviour is how browser is supposed to behave. Anytime a change is made to the url in the address the browser will force a new request. Otherwise it will be hard to navigate around the web. Previously, when we used hashes, this wasn't the case. It's because browsers are smart enough to know the anything after a hash relates to the contents on the page and not some other location. If we want to navigate from page to page without reloading assets we'll need to add links.
  That's perfectly fine anyway. Users don't normally browsers site by constantly changing the url in the address bar. They navigate around by clicking on links.
  The very last thing i want to mention is how pages are delivered to the client. You use a client side library. It will not run until the application is delivered to the client. Therefore is always important to respond with an indexed .html file regardless of the url. Just because you make a request to the about page doesn't mean the vue router will automatically handle it. Servers always get first dives on stuff like this. After the indexed file is delivered our application can take over routing and display the correct content. We don't have to worry about doing that because we are using vite to create a server. Vite will always serve the indexed file. If you are using a different backend then you will need to configure this yourselves or even have a backend developer handle it.
  I provide this link https://router.vuejs.org/guide/essentials/history-mode.html#memory-mode to the history mode documentation page. As stated on the page simply changing the mode to a history won't automaticalyy make routing work. There are example configuration you can make to the backend to get this to work fully. It depends on what you using it as the server. I mentioning this now because you may want to test this on the production server. Things may not work as expected. Just remember to serve the indexed file so that you can handle the routing

---
## [Paxilmaniac/Skyrat-tg](https://github.com/Paxilmaniac/Skyrat-tg)@[b15331b4df...](https://github.com/Paxilmaniac/Skyrat-tg/commit/b15331b4df9bd525ba80b284beb3442f180c01be)
#### Friday 2022-08-05 20:43:00 by OrionTheFox

[MANUAL MIRROR] The GAGening: Clothesmate edition [MDB IGNORE] (#15100)

* The GAGening: Clothesmate edition

* ThisShouldWork

* hgnbhg

* would probably help to have the right .dmi

* fixed?

* Fuck you

Co-authored-by: Twaticus <46540570+Twaticus@users.noreply.github.com>

---
## [GarreauArthur/minesweeper-rust-wasm](https://github.com/GarreauArthur/minesweeper-rust-wasm)@[d3363ae5e8...](https://github.com/GarreauArthur/minesweeper-rust-wasm/commit/d3363ae5e838c2f57dc0c57424e36da54f1162bc)
#### Friday 2022-08-05 21:03:40 by cqncpdp

I just want to upload 1 file & a directory and its files, why is it so fucking hard, this shit actually sucks

---
## [uber-go/cadence-client](https://github.com/uber-go/cadence-client)@[f5e0fd25e4...](https://github.com/uber-go/cadence-client/commit/f5e0fd25e4347c85b28dac87f51b532700455d2c)
#### Friday 2022-08-05 21:26:58 by Steven L

Sharing one of my favorite "scopes" in intellij, and making it easier to add more (#1182)

Goland is nice, and the type-based navigation is wildly superior to gopls-driven
stuff in my experience, so I tend to lean hard on it when I'm able.

By default though, Goland searches *everything*.  All the time.
That's totally reasonable as a default, but we can do better:

- Tests are not usually all that interesting when trying to understand and navigate code.
  (perhaps they should be, but that's more a platonic ideal than a reality)
- Generated RPC code is almost never useful to dive into.  The exposed API surface is sufficient,
  if it compiles, it's correct.
- Non-Go files are just less interesting in a Go project.

So this scope excludes ^ all that.
To add more shared ones, just check the "share through vcs" box and commit it.

To use it, just select the scope from the dropdown when you search.  E.g. "find in files" ->
change from "in project" to "scope" -> change the dropdown.  This custom scope will now appear,
and it'll remember what you last used, so it's a nice default.

This also works in "call hierarchy", "go to implementations" (open it in a panel to configure it,
with the gear on the side.  it's awful UI but it works), etc quite a lot of places.

This same kinda-obtuse search-scope query language can be used to mark things as generated or test
related, which will also help other parts of the IDE mark things as more or less relevant for you.
It's worth exploring a bit, scopes and filters can be used to do a lot: https://www.jetbrains.com/help/idea/scope-language-syntax-reference.html

---
## [Qwertytoforty/Paradise](https://github.com/Qwertytoforty/Paradise)@[fd5580307e...](https://github.com/Qwertytoforty/Paradise/commit/fd5580307e1d3a2821ae8b2f26cb04cdcd139f87)
#### Friday 2022-08-05 22:14:21 by Contrabang

Adds a blue overlay to scrying orb users. Spirit realm and scrying orb users now have a special description instead of being catatonic (#18366)

* holy shit blue ghosts

* lets fix that

* you cant see it if its not in ya hand

* Their glowing red eyes are glazed over

* farie review

* farie review pt 2

---
## [paulallenbeck/four-in-a-row](https://github.com/paulallenbeck/four-in-a-row)@[548ad60582...](https://github.com/paulallenbeck/four-in-a-row/commit/548ad605825da246c4a3d159e4d741828592983a)
#### Friday 2022-08-05 22:41:25 by Kevin Tang

Fix publish.yml not created published branch (#17)

* try fix

* bruh fuck

* holy shit someone else did this already of course

* fix this shit fuck

---
## [git/git](https://github.com/git/git)@[5beca49a0b...](https://github.com/git/git/commit/5beca49a0b1f3c6d05a4437ca037ab2123a2de57)
#### Friday 2022-08-05 23:31:35 by Ævar Arnfjörð Bjarmason

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
## [Pickle-Coding/tgstation](https://github.com/Pickle-Coding/tgstation)@[6fe0683a7b...](https://github.com/Pickle-Coding/tgstation/commit/6fe0683a7bc788a497dbce8771768e427d0dffb1)
#### Friday 2022-08-05 23:56:47 by Jolly

[READY] [KC13] Showing "The Derelict" some love: General updates, aesthetic changes and misc (#67696)

With this PR I aim to make KC13 (TheDerelict.dmm), or Russian Station (whatever you guys call it) a tad bit more flavorful with its environment as well as somethings on the mapping side (like adding area icons!).
To preface, no, I'm not remapping anything here extensively. The general layout should be relatively the same (or should be in theory).

Halfway through naming the area icons I checked the wiki page and found out it was KC not KS, so, its KS13 internally.

Readability for turf icons are cool.
Also just making the ruin more eye appealing would be better.
General cleanup and changes will give new life to this rather.. loved? Hated? Loot pinata? Ruin.
The ruin also now starts completely depowered, like Old Station (its a Derelict, it makes no sense for it to still be powered after so long). As for some mild compensation, a few more batteries were sprinkled in to offset any issues. If there is any concern of "But they'll open the vault faster!", there were always 5 batteries that people used to make the vault SMES.
Lastly, giving it some "visual story telling" is cool, as mapping fluff goes.

I also added a subtle OOC hint that the SMES in the northern most solar room needs a terminal with the following:

SMES Jumpscare
As an aside, I aim to try and keep the feel of this ruin being "dated" while at the same time having some of our newer things. With that, certain things I'll opt out of using in favor of more "generic" structures to give KC13 that true "Its old but not really" feel and look.

---

