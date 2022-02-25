## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-02-24](docs/good-messages/2022/2022-02-24.md)


1,784,199 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,784,199 were push events containing 2,832,664 commit messages that amount to 206,386,220 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 31 messages:


## [rorydale/pointbreakradio](https://github.com/rorydale/pointbreakradio)@[b949ed7fa5...](https://github.com/rorydale/pointbreakradio/commit/b949ed7fa58f0bb8a75f5a72d6ef9cd82945e2dd)
#### Thursday 2022-02-24 00:14:29 by Rory Dale

2022-02-23

Wednesday, February 23rd, 2021 - the Summer of Love show! Today's show was inspired by a tweet shared with me this morning by my Dad containing lyrics to Procol Harum's A Whiter Shade of Pale, containing a rarely heard third verse. As this track was one of the anthems of the Summer of Love, I decided to base the show around it, working chronologically from January to August thinking about what it must have been like to have been buying albums in the run up to the Summer. I've tried to play deeper cuts from the albums as I like to imagine them ringing distant bells for people who owned them at the time, instead of playing through the more well known singles. With the passing of Gary Brooker on Saturday, A Whiter Shade of Pale deserves the extra attention and after a few hours of back and forth, my Dad shared a version of the song with a fourth rarely heard verse recorded live for its 30th anniversary in 1997.

---
## [odoo/odoo](https://github.com/odoo/odoo)@[4c9f12d55c...](https://github.com/odoo/odoo/commit/4c9f12d55c06d7e2734bbdbe05f524122ad75327)
#### Thursday 2022-02-24 00:16:57 by Julien Castiaux

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
## [DragonTrance/tgstation](https://github.com/DragonTrance/tgstation)@[906fb0682b...](https://github.com/DragonTrance/tgstation/commit/906fb0682bab6a0975b45036001c54f021f58ae7)
#### Thursday 2022-02-24 00:58:15 by necromanceranne

Ballistic to Energy: Autorifles for Thermal Pistols; Adds .38 Crate to Cargo (#64280)

About The Pull Request
The design doc behind this PR, which is only mildy been deviated from on some of the end particulars. Cobby-Approved! Maintainer Discussed!
https://hackmd.io/@6DbtsAKCTtW_9MByKFjZqg/r1xYKCNOt

Cargo Changes
Cargo has had all WT-550's removed and replaced with Thermal Pistols.
Cargo can now order Thermal Pistols, a kind of energy/ballistic hybrid weapon shooting chunks of altered nanites into people. We couldn't use them in people, so maybe we'll use them as bullets! Magma/Ice bullets, to be exact.
You can, after paying a whopping 4K on a goodie pack (you have to pay from your own personal account) buy a .38 revolver. This is mostly to help some poor detective who lost their revolve in what I'm sure will be an inevitable scramble for ballistics. If even the 4K pricetag isn't enough, at least it requires detective access to open the pack...I hope.
Some of the crates that contained autorifle related items have been changed/removed.

unknown (2)

securarevolver 4 0

Science Changes
Ballistic Weaponry node no longer exists, and has been replaced with Exotic Ammo as both the pre-requisite to other nodes, as well as being able to be researched as soon as the Weaponry node is unlocked and not Advanced Weaponry.

Thermal Pistols
-Fairly average bullet statistics; 10 AP but shooting into Energy armor. 20 damage (Brute for cryo, Burn for inferno). Decent wounding potential, but individually much lower ammo counts than lasers.
-Bought in twinned pairs in a two gun holster (just for normal sized energy guns). They're normal sized.
-Each gun has 8 shots (thereabouts). 16 between two.
-Cryo pistols do a knockdown and extra damage against extremely hot targets. Inferno pistols do an explosion cantered on the target against extremely cold targets.
-The guns are EMP-proof.

Why It's Good For The Game
The current gameplay loop of crew combatants is them relying on backup and retreating as necessary to reload their weapons during fights. The ability to repeatedly harry opponents in the field reloads is something that should be moved away from for crew equipment, as it emphasizes lone wolf tactics and one-man army problems, with boxes full of spare ammo usually allowing any single combatant to outlast multiple foes. In addition, ballistics often are not subject to the same (interesting) limitations of energy weapons, so they're typically a no-brainer choice. We shouldn't have such an easy choice be readily available like that.

The thermal pistols present a more challenging weapon to use as a solo combatant but become far more versatile and potent when paired with a decent buddy and basic level co-ordination. They're not a straightforward choice for every situation, but instead are a weapon employed given the right circumstances for them to shine.

In addition to the gameplay issues that ballistics pose, we're in a goddamn spacegame. Unless the ballistics are noticeably weird (they're not), we should expect that our more advanced research station has some pretty odd guns of the energy variety.

Changelog
🆑 Necromanceranne, quin
add: Adds the Inferno and Cryo Pistols. A hybrid energy/ballistic weapon, to cargo. It can be purchased in either a goodies pack or a normal crate order.
add: Thermal Pistols do more damage and a special based on temperature of the target hit.
add: Inferno pistols cause an explosion when they hit a severely cold target.
add: Cryo pistols cause a knockdown and extra damage if they hit a severely hot target.
add: There is a special nanite pistol, which is admin spawned. Don't tell anyone about the forbidden ballistic energy gun.
add: You can order a .38 revolver as a goodie pack. It is expensive.
del: Removes WT-550's from cargo and related content from the techweb/protolathes.
balance: Exotic Ammo is now much earlier in the tech web to take the place of Ballistic Weaponry.
/🆑

---
## [bit-bandit/wastebin](https://github.com/bit-bandit/wastebin)@[fae820a076...](https://github.com/bit-bandit/wastebin/commit/fae820a0761ce25fd2254ad59de2ee7cb5361e35)
#### Thursday 2022-02-24 01:11:16 by PK

Actually escape characters before submission this literally is an XSS vulerability why the fuck did I not fix this before we're dealing with user input for godssake how am I this fucking stupid

---
## [bknox83/Stockfish](https://github.com/bknox83/Stockfish)@[cb9c2594fc...](https://github.com/bknox83/Stockfish/commit/cb9c2594fcedc881ae8f8bfbfdf130cf89840e4c)
#### Thursday 2022-02-24 02:01:27 by Tomasz Sobczyk

Update architecture to "SFNNv4". Update network to nn-6877cd24400e.nnue.

Architecture:

The diagram of the "SFNNv4" architecture:
https://user-images.githubusercontent.com/8037982/153455685-cbe3a038-e158-4481-844d-9d5fccf5c33a.png

The most important architectural changes are the following:

* 1024x2 [activated] neurons are pairwise, elementwise multiplied (not quite pairwise due to implementation details, see diagram), which introduces a non-linearity that exhibits similar benefits to previously tested sigmoid activation (quantmoid4), while being slightly faster.
* The following layer has therefore 2x less inputs, which we compensate by having 2 more outputs. It is possible that reducing the number of outputs might be beneficial (as we had it as low as 8 before). The layer is now 1024->16.
* The 16 outputs are split into 15 and 1. The 1-wide output is added to the network output (after some necessary scaling due to quantization differences). The 15-wide is activated and follows the usual path through a set of linear layers. The additional 1-wide output is at least neutral, but has shown a slightly positive trend in training compared to networks without it (all 16 outputs through the usual path), and allows possibly an additional stage of lazy evaluation to be introduced in the future.

Additionally, the inference code was rewritten and no longer uses a recursive implementation. This was necessitated by the splitting of the 16-wide intermediate result into two, which was impossible to do with the old implementation with ugly hacks. This is hopefully overall for the better.

First session:

The first session was training a network from scratch (random initialization). The exact trainer used was slightly different (older) from the one used in the second session, but it should not have a measurable effect. The purpose of this session is to establish a strong network base for the second session. Small deviations in strength do not harm the learnability in the second session.

The training was done using the following command:

python3 train.py \
    /home/sopel/nnue/nnue-pytorch-training/data/nodes5000pv2_UHO.binpack \
    /home/sopel/nnue/nnue-pytorch-training/data/nodes5000pv2_UHO.binpack \
    --gpus "$3," \
    --threads 4 \
    --num-workers 4 \
    --batch-size 16384 \
    --progress_bar_refresh_rate 20 \
    --random-fen-skipping 3 \
    --features=HalfKAv2_hm^ \
    --lambda=1.0 \
    --gamma=0.992 \
    --lr=8.75e-4 \
    --max_epochs=400 \
    --default_root_dir ../nnue-pytorch-training/experiment_$1/run_$2

Every 20th net was saved and its playing strength measured against some baseline at 25k nodes per move with pure NNUE evaluation (modified binary). The exact setup is not important as long as it's consistent. The purpose is to sift good candidates from bad ones.

The dataset can be found https://drive.google.com/file/d/1UQdZN_LWQ265spwTBwDKo0t1WjSJKvWY/view

Second session:

The second training session was done starting from the best network (as determined by strength testing) from the first session. It is important that it's resumed from a .pt model and NOT a .ckpt model. The conversion can be performed directly using serialize.py

The LR schedule was modified to use gamma=0.995 instead of gamma=0.992 and LR=4.375e-4 instead of LR=8.75e-4 to flatten the LR curve and allow for longer training. The training was then running for 800 epochs instead of 400 (though it's possibly mostly noise after around epoch 600).

The training was done using the following command:

The training was done using the following command:

python3 train.py \
        /data/sopel/nnue/nnue-pytorch-training/data/T60T70wIsRightFarseerT60T74T75T76.binpack \
        /data/sopel/nnue/nnue-pytorch-training/data/T60T70wIsRightFarseerT60T74T75T76.binpack \
        --gpus "$3," \
        --threads 4 \
        --num-workers 4 \
        --batch-size 16384 \
        --progress_bar_refresh_rate 20 \
        --random-fen-skipping 3 \
        --features=HalfKAv2_hm^ \
        --lambda=1.0 \
        --gamma=0.995 \
        --lr=4.375e-4 \
        --max_epochs=800 \
        --resume-from-model /data/sopel/nnue/nnue-pytorch-training/data/exp295/nn-epoch399.pt \
        --default_root_dir ../nnue-pytorch-training/experiment_$1/run_$run_id

In particular note that we now use lambda=1.0 instead of lambda=0.8 (previous nets), because tests show that WDL-skipping introduced by vondele performs better with lambda=1.0. Nets were being saved every 20th epoch. In total 16 runs were made with these settings and the best nets chosen according to playing strength at 25k nodes per move with pure NNUE evaluation - these are the 4 nets that have been put on fishtest.

The dataset can be found either at ftp://ftp.chessdb.cn/pub/sopel/data_sf/T60T70wIsRightFarseerT60T74T75T76.binpack in its entirety (download might be painfully slow because hosted in China) or can be assembled in the following way:

Get the https://github.com/official-stockfish/Stockfish/blob/5640ad48ae5881223b868362c1cbeb042947f7b4/script/interleave_binpacks.py script.
Download T60T70wIsRightFarseer.binpack https://drive.google.com/file/d/1_sQoWBl31WAxNXma2v45004CIVltytP8/view
Download farseerT74.binpack http://trainingdata.farseer.org/T74-May13-End.7z
Download farseerT75.binpack http://trainingdata.farseer.org/T75-June3rd-End.7z
Download farseerT76.binpack http://trainingdata.farseer.org/T76-Nov10th-End.7z
Run python3 interleave_binpacks.py T60T70wIsRightFarseer.binpack farseerT74.binpack farseerT75.binpack farseerT76.binpack T60T70wIsRightFarseerT60T74T75T76.binpack

Tests:

STC: https://tests.stockfishchess.org/tests/view/6203fb85d71106ed12a407b7
LLR: 2.94 (-2.94,2.94) <0.00,2.50>
Total: 16952 W: 4775 L: 4521 D: 7656
Ptnml(0-2): 133, 1818, 4318, 2076, 131

LTC: https://tests.stockfishchess.org/tests/view/62041e68d71106ed12a40e85
LLR: 2.94 (-2.94,2.94) <0.50,3.00>
Total: 14944 W: 4138 L: 3907 D: 6899
Ptnml(0-2): 21, 1499, 4202, 1728, 22

closes https://github.com/official-stockfish/Stockfish/pull/3927

Bench: 4919707

---
## [squid-cache/squid](https://github.com/squid-cache/squid)@[2b6b1bcb86...](https://github.com/squid-cache/squid/commit/2b6b1bcb8650095c99a1916f5964305484af7ef0)
#### Thursday 2022-02-24 02:20:09 by Alex Rousskov

Bug 5055: FATAL FwdState::noteDestinationsEnd exception: opening (#877)

The bug was caused by commit 25b0ce4. Other known symptoms are:

    assertion failed: store.cc:1793: "isEmpty()"
    assertion failed: FwdState.cc:501: "serverConnection() == conn"
    assertion failed: FwdState.cc:1037: "!opening()"

This change has several overlapping parts. Unfortunately, merging
individual parts is both difficult and likely to cause crashes.

## Part 1: Bug 5055.

FwdState used to check serverConn to decide whether to open a connection
to forward the request. Since commit 25b0ce4, a nil serverConn pointer
no longer implies that a new connection should be opened: FwdState
helper jobs may already be working on preparing an existing open
connection (e.g., sending a CONNECT request or negotiating encryption).

Bad serverConn checks in both FwdState::noteDestination() and
FwdState::noteDestinationsEnd() methods led to extra connectStart()
calls creating two conflicting concurrent helper jobs.

To fix this, we replaced direct serverConn inspection with a
usingDestination() call which also checks whether we are waiting for a
helper job. Testing that fix exposed another set of bugs: The helper job
pointers or in-job connections were left stale/set after forwarding
failures. The changes described below addressed most of those problems.


## Part 2: Connection establishing helper jobs and their callbacks

A proper fix for Bug 5055 required answering a difficult question: When
should a dying job call its callbacks? We only found one answer which
required cooperation from the job creator and led to the following
rules:

* AsyncJob destructors must not call any callbacks.

* AsyncJob::swanSong() is responsible for async-calling any remaining
  (i.e. set, uncalled, and uncancelled) callbacks.

* AsyncJob::swanSong() is called (only) for started jobs.

* AsyncJob destructing sequence should validate that no callbacks remain
  uncalled for started jobs.

... where an AsyncJob x is considered "started" if AsyncJob::Start(x)
has returned without throwing.

A new JobWait class helps job creators follow these rules while keeping
track on in-progress helper jobs and killing no-longer-needed helpers.

Also fixed very similar bugs in tunnel.cc code.


## Part 3: ConnOpener fixes

1. Many ConnOpener users are written to keep a ConnectionPointer to the
   destination given to ConnOpener. This means that their connection
   magically opens when ConnOpener successfully connects, before
   ConnOpener has a chance to notify the user about the changes. Having
   multiple concurrent connection owners is always dangerous, and the
   user cannot even have a close handler registered for its now-open
   connection. When something happens to ConnOpener or its answer, the
   user job may be in trouble. Now, ConnOpener callers no longer pass
   Connection objects they own, cloning them as needed. That adjustment
   required adjustment 2:

2. Refactored ConnOpener users to stop assuming that the answer contains
   a pointer to their connection object. After adjustment 1 above, it
   does not. HappyConnOpener relied on that assumption quite a bit so we
   had to refactor to use two custom callback methods instead of one
   with a complicated if-statement distinguishing prime from spare
   attempts. This refactoring is an overall improvement because it
   simplifies the code. Other ConnOpener users just needed to remove a
   few no longer valid paranoid assertions/Musts.

3. ConnOpener users were forced to remember to close params.conn when
   processing negative answers. Some, naturally, forgot, triggering
   warnings about orphaned connections (e.g., Ident and TcpLogger).
   ConnOpener now closes its open connection before sending a negative
   answer.

4. ConnOpener would trigger orphan connection warnings if the job ended
   after opening the connection but without supplying the connection to
   the requestor (e.g., because the requestor has gone away). Now,
   ConnOpener explicitly closes its open connection if it has not been
   sent to the requestor.

Also fixed Comm::ConnOpener::cleanFd() debugging that was incorrectly
saying that the method closes the temporary descriptor.

Also fixed ConnOpener callback's syncWithComm(): The stale
CommConnectCbParams override was testing unused (i.e. always negative)
CommConnectCbParams::fd and was trying to cancel the callback that most
(possibly all) recipients rely on: ConnOpener users expect a negative
answer rather than no answer at all.

Also, after comparing the needs of two old/existing and a temporary
added ("clone everything") Connection cloning method callers, we decided
there is no need to maintain three different methods. All existing
callers should be fine with a single method because none of them suffers
from "extra" copying of members that others need. Right now, the new
cloneProfile() method copies everything except FD and a few
special-purpose members (with documented reasons for not copying).

Also added Comm::Connection::cloneDestinationDetails() debugging to
simplify tracking dependencies between half-baked Connection objects
carrying destination/flags/other metadata and open Connection objects
created by ConnOpener using that metadata (which are later delivered to
ConnOpener users and, in some cases, replace those half-baked
connections mentioned earlier. Long-term, we need to find a better way
to express these and other Connection states/stages than comments and
debugging messages.


## Part 4: Comm::Connection closure callbacks

We improved many closure callbacks to make sure (to the extent possible)
that Connection and other objects are in sync with Comm. There are lots
of small bugs, inconsistencies, and other problems in Connection closure
handlers. It is not clear whether any of those problems could result in
serious runtime errors or leaks. In theory, the rest of the code could
neutralize their negative side effects. However, even in that case, it
would only be a matter of time before the next bug bites us due to stale
Connection::fd and such. These changes themselves carry elevated risk,
but they get us closer to reliable code as far as Connection maintenance
is concerned. Without them, we will keep chasing deadly side effects of
poorly implemented closure callbacks.

Long-term, all these manual efforts to keep things in sync should become
unnecessary with the introduction of appropriate Connection ownership
APIs that automatically maintain the corresponding environments (TODO).


## Part 5: Other notable improvements in the adjusted code

Improved Security::PeerConnector::serverConn and
Http::Tunneler::connection management, especially when sending negative
answers. When sending a negative answer, we would set answer().conn to
an open connection, async-send that answer, and then hurry to close the
connection using our pointer to the shared Connection object. If
everything went according to the plan, the recipient would get a non-nil
but closed Connection object. Now, a negative answer simply means no
connection at all. Same for a tunneled answer.

Refactored ICAP connection-establishing code to to delay Connection
ownership until the ICAP connection is fully ready. This change
addresses primary Connection ownership concerns (as they apply to this
ICAP code) except orphaning of the temporary Connection object by helper
job start exceptions (now an explicit XXX). For example, the transaction
no longer shares a Connection object with ConnOpener and
IcapPeerConnector jobs.

Probably fixed a bug where PeerConnector::negotiate() assumed that
sslFinalized() does not return true after callBack(). It may (e.g., when
CertValidationHelper::Submit() throws). Same for
PeekingPeerConnector::checkForPeekAndSpliceMatched().
 
Fixed FwdState::advanceDestination() bug that did not save
ERR_GATEWAY_FAILURE details and "lost" the address of that failed
destination, making it unavailable to future retries (if any).

Polished PeerPoolMgr, Ident, and Gopher code to be able to fix similar
job callback and connection management issues.

Polished AsyncJob::Start() API. Start() used to return a job pointer,
but that was a bad idea:
    
* It implies that a failed Start() will return a nil pointer, and that
  the caller should check the result. Neither is true.

* It encourages callers to dereference the returned pointer to further
  adjust the job. That technically works (today) but violates the rules
  of communicating with an async job. The Start() method is the boundary
  after which the job is deemed asynchronous.
    
Also removed old "and wait for..." post-Start() comments because the
code itself became clear enough, and those comments were becoming
increasingly stale (because they duplicated the callback names above
them).

Fix Tunneler and PeerConnector handling of last-resort callback
requirements. Events like handleStopRequest() and callException() stop
the job but should not be reported as a BUG (e.g., it would be up to the
callException() to decide how to report the caught exception). There
might (or there will) be other, similar cases where the job is stopped
prematurely for some non-BUG reason beyond swanSong() knowledge. The
existence of non-bug cases does not mean there could be no bugs worth
reporting here, but until they can be identified more reliably than all
these benign/irrelevant cases, reporting no BUGs is a (much) lesser
evil.

TODO: Revise AsyncJob::doneAll(). Many of its overrides are written to
check for both positive (i.e. mission accomplished) and negative (i.e.
mission cancelled or cannot be accomplished) conditions, but the latter
is usually unnecessary, especially after we added handleStopRequest()
API to properly support external job cancellation events. Many doneAll()
overrides can probably be greatly simplified.

---
## [happynerdfreak17/Empower-and-Elevate](https://github.com/happynerdfreak17/Empower-and-Elevate)@[4c0e835e3e...](https://github.com/happynerdfreak17/Empower-and-Elevate/commit/4c0e835e3e3cb4e497604abaa992ef18784e56de)
#### Thursday 2022-02-24 03:11:24 by timothygao8710

trying to oragnize this fucking shit

so frustrating

---
## [Kazkin/sojourn-station](https://github.com/Kazkin/sojourn-station)@[9410031f12...](https://github.com/Kazkin/sojourn-station/commit/9410031f12ac9c565933ed7c29af071d31e4a807)
#### Thursday 2022-02-24 04:49:09 by Kazkin

Rise of the Most Unpopular PR of All Time 2: Revengeance Rising Revelations Reborn Featuring Dante from Devil May Cry and Knuckles

-All tier 2 medical kits now have special checks that verify both perk and bio checks to allow use. All medical kits, including gauze and ointment, requires you to have 0 or greater bio to use. (Dump stating bio now has a detriment).
-Advanced bruise/burn kits require soteria medical expertise perk or 75 bio to use.
-Hunting lodge blood tongues and powder pouches require master butcher or 10 bio.
-Church medical kits require the soteria medical expert perk or 15 bio (intentionally made easy to use since they are rare, costly to mass produce, and only come from the church). Uses the soteria perk since it is essentially an easier to use advanced kit.
-Blackshield medkits now come with regular gauze and ointment in place of advanced kits. This has a side benefit of reducing storage space by 50% as these medical items are smaller.
-Most random spawners now spawn standard regular kits instead of advanced kits.
-Regular medkits and first aid kits have their spawn chance reduced.
-Cargo techs still have a chance to spawn with advanced kits (sell them to doctors)
-Ifaks now contain gauze and ointment.
-Prospector factions no longer spawn advanced kits. Due to how probability works, they now have a 1 in 20 chance to get a combat medkit kit instead of an ifak. This change effects salvagers and foremans.
-Corpsman now spawn with regular first aid kits.
-Syringes now require 15 bio to do **anything** with them.
-Autoinjectors can now be refilled using a syringe. Autoinjectors do not have a bio check.
-Blackshield kits now contain only bandages and gauze.
-Surgery now has had its difficult risen by 90 and takes 120 ticks longer unless you have the soteria advanced surgical perk or surgical mastery perk. For reference, the base difficulty of surgery is 80, tool quality, precision bonuses, and bio skill change the odds. 120 ticks is roughly 12 seconds. This timer is modified by bio skill.

---
## [Joecontrair/Joecontrair.github.io](https://github.com/Joecontrair/Joecontrair.github.io)@[1feb8c9374...](https://github.com/Joecontrair/Joecontrair.github.io/commit/1feb8c9374be42493d6a3f1a89d14ecb01ab9af9)
#### Thursday 2022-02-24 05:15:16 by Joseph Daly

Comment

God Damn do I hate programming. This isn't even programming it's fucking website design or something l,ao

---
## [AzureMarker/rust-horizon](https://github.com/AzureMarker/rust-horizon)@[547f2ba06b...](https://github.com/AzureMarker/rust-horizon/commit/547f2ba06bc4aa93a375c54e1af3fd1216eeaf62)
#### Thursday 2022-02-24 05:20:12 by bors

Auto merge of #86988 - thomcc:chunky-splitz-says-no-checking, r=the8472

Carefully remove bounds checks from some chunk iterator functions

So, I was writing code that requires the equivalent of `rchunks(N).rev()` (which isn't the same as forward `chunks(N)` — in particular, if the buffer length is not a multiple of `N`, I must handle the "remainder" first).

I happened to look at the codegen output of the function (I was actually interested in whether or not a nested loop was being unrolled — it was), and noticed that in the outer `rchunks(n).rev()` loop, LLVM seemed to be unable to remove the bounds checks from the iteration: https://rust.godbolt.org/z/Tnz4MYY8f (this panic was from the split_at in `RChunks::next_back`).

After doing some experimentation, it seems all of the `next_back` in the non-exact chunk iterators have the issue: (`Chunks::next_back`, `RChunks::next_back`, `ChunksMut::next_back`, and `RChunksMut::next_back`)...

Even worse, the forward `rchunks` iterators sometimes have the issue as well (... but only sometimes). For example https://rust.godbolt.org/z/oGhbqv53r has bounds checks, but if I uncomment the loop body, it manages to remove the check (which is bizarre, since I'd expect the opposite...). I suspect it's highly dependent on the surrounding code, so I decided to remove the bounds checks from them anyway. Overall, this change includes:
- All `next_back` functions on the non-`Exact` iterators (e.g. `R?Chunks(Mut)?`).
- All `next` functions on the non-exact rchunks iterators (e.g. `RChunks(Mut)?`).

I wasn't able to catch any of the other chunk iterators failing to remove the bounds checks (I checked iterations over `r?chunks(_exact)?(_mut)?` with constant chunk sizes under `-O3`, `-Os`, and `-Oz`), which makes sense, since these were the cases where it was harder to prove the bounds check correct to remove...

In fact, it took quite a bit of thinking to convince myself that using unchecked_ here was valid — so I'm not really surprised that LLVM had trouble (although compilers are slightly better at this sort of reasoning than humans). A consequence of that is the fact that the `// SAFETY` comment for these are... kinda long...

---

I didn't do this for, or even think about it for, any of the other iteration methods; just `next` and `next_back` (where it mattered). If this PR is accepted, I'll file a follow up for someone (possibly me) to look at the others later (in particular, `nth`/`nth_back` looked like they had similar logic), but I wanted to do this now, as IMO `next`/`next_back` are the most important here, since they're what gets used by the iteration protocol.

---

Note: While I don't expect this to impact performance directly, the panic is a side effect, which would otherwise not exist in these loops. That is, this could prevent the compiler from being able to move/remove/otherwise rework a loop over these iterators (as an example, it could not delete the code for a loop whose body computes a value which doesn't get used).

Also, some like to be able to have confidence this code has no panicking branches in the optimized code, and "no bounds checks" is kinda part of the selling point of Rust's iterators anyway.

---
## [zclkkk/kernel_realme_sm8350](https://github.com/zclkkk/kernel_realme_sm8350)@[ca03c78403...](https://github.com/zclkkk/kernel_realme_sm8350/commit/ca03c784036a16cd7af577964cecc7fcbc009ea2)
#### Thursday 2022-02-24 07:16:18 by zclkkk

techpack/display: Kang from OnePlus OSS

* Our display module is broken...
* Fuck you realme

---
## [newstools/2022-metro](https://github.com/newstools/2022-metro)@[be17b3daaf...](https://github.com/newstools/2022-metro/commit/be17b3daaf4345f0694ce8749a4a731cec46e245)
#### Thursday 2022-02-24 08:41:31 by Billy Einkamerer

Created Text For URL [metro.co.uk/2022/02/24/my-boyfriend-wont-let-my-travel-dreams-come-true-what-should-i-do-16160840/]

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[3799bd7828...](https://github.com/mrakgr/The-Spiral-Language/commit/3799bd7828075fee8e4065efb30ee17cfa222e37)
#### Thursday 2022-02-24 09:48:43 by Marko Grdinić

"11:25am. I slept well, but decided to stay in bed for a while. I've had to time to think about what I want to do, and I'll think I'll watch the cloud tutorials by Rohan. I should play around with volumes for a bit.

11:45am. Let me have breakfast here. I want to start, but this is no time to be doing that.

12:20pm. Another chap and then it is chores time.

12:45pm. Let me do the chores here. I've done enough morning slacking. There simply aren't enough hours in the day to satisfy me.

3:05pm. I am back. Let me chill a bit first. I need to cool down.

3:40pm. I've cooled down. It if far later than usual, but let me finally start.

It is just so hard to find the time to do this even though I have the whole day to myself.

Forget the tutorial by Rohan. Let me check out some of the stuff on Youtube.

https://youtu.be/WTg_pVZoac0
Free Masterclass: Developing Complex Details Using Volumes in Houdini

Oh, this is 3.5 hours. This will teach me a lot about volumes.

https://youtu.be/WTg_pVZoac0?t=19

Looking at the TOC, he covers walls and bricks. This is not what I imagined volumes would be for. I'll definitely benefit a lot from this. These cliffs look amazing.

https://www.youtube.com/c/Rebelway/search?query=free%20masterclass

This channel has hours long courses. What a find. I wonder why the volume one does not show up in search? Ah, it does. It is the second one.

https://www.youtube.com/playlist?list=PLrwHqtPQxnbY7kjiqnTNhvvQFeX39rMPD

Here is the playlist of them. It would take me two weeks at least to go through all of these.

https://youtu.be/WTg_pVZoac0?t=251

He mentions that VDB is better than Houdini's native volume.

https://youtu.be/WTg_pVZoac0?t=327

Let me follow along. The video tutorials are much better than reading docs.

4:20pm. https://youtu.be/WTg_pVZoac0?t=546

This is so confusing. I am playing with volumes and am noticing that its rendering is completely different depending on the absolute size of the sphere. Setting the voxel size does not adjust for that.

https://youtu.be/WTg_pVZoac0?t=625

I do not get why the noise pattern looks so much better for him. When I try it, I get areas that are extremely light and dark.

Let me ask.

///

>>884062 (You)
Try hscript point() expression

///

Hmmm, this is for that attribute question. Let me save what I am currently doing and I will try it out. If I can use the @ptnum inside the expression it could work.

5:40pm. Let me stop here for lunch.

6:35pm. What the hell? How did it last this long. At any rate, no way I am going to stop here. I am going to keep going till 10pm.

7:25pm. https://youtu.be/WTg_pVZoac0?t=1914

The voronois fracture changed significantly.

8:10pm. AHhhhhhhhh. The Toogle visualization is that small icon after piece prefix.

8:35pm. Holy shit, I just can't figure out what the debug flag for VOPs does. Right now I want to look into the random node to see why it is not outputting the y axis and can't figure out how to do it.

8:40pm. Maybe it is just an support flag without any explicit effect.

///

>>884262 (You)
the ramp parameter node?
there's a weird quirk to it - you can't tweak it from inside the vop. go up a level and you'll see the interface exposed on the vop parameters. by default it's set to zero. don't ask me why.

///

I did not expect this. I'll have to keep this in mind for the future.

8:50pm. https://youtu.be/WTg_pVZoac0?t=2375

It has taken me a while to remember that moving the offset is not for the points, but for the noise itself. What he is doing here is spew, he should have just turned on 3d output.

Let make sure. I'll try outputting the thing as an attribute.

Bind Export VOP is what I need. And I see that the 3d outputs are in fact random. Great. This is much better than the solution in the video.

Hmmm, for storing the distance of each piece, I should be using a dictionary rather than attaching it to primitives. How do I do that.

https://www.sidefx.com/docs/houdini/vex/dicts.html
> The dict type will be considerably less efficient than expanding the dictionary as a variable per entry; so should only be used where the set of variables and types are varying.

I was wrong. I guess I should just attach the dist value to primitives.

9:20pm. I've played around quite a bit. I did managed to extrude every individual fractured piece.

https://youtu.be/WTg_pVZoac0?t=2552

Did this guy forget that each piece already had a name attribute?

But at least this is educational.

https://youtu.be/WTg_pVZoac0?t=2632

He is packing to get the centroid. Wasn't there an extract centroid. He also could have iterated over each individual piece and got the center of the bounding box. Also, I think I saw the extract centroid node while looking around.

Extract Centroid SOP, just as I suspected.

9:30pm. I could use that. But the Voronoi Fracture in fact does give the centroid information as its second output.

The approach this guy is taking can be unoptimized. This demonstrates the danger of just following courses blindly.

I am making slow progress, but this way of going through it is pretty immersive.

Now what is he doing what that rest attribute?

> Creates rest attributes on the geometry so procedural textures stay put on the surface as it deforms.

This is possible?

https://youtu.be/WTg_pVZoac0?t=2731

9:50pm. point("../centroids",detail("../foreach_begin2_metadata1/","iteration",0),"P",0)

It is a huge pain in the ass to access something in hexpressions

10:30pm. Voronoi fracture has an option to output the primitive piece in addition to the connectivity.

10:45pm. I am still at it, trying to figure out optimal ways to implement what he is saying. My own methods are actually better than what is show in the vid, but on the flipside it takes me forever to do it.

https://youtu.be/WTg_pVZoac0?t=2731

Let me watch this just for a bit and then I will stop.

10:50pm. Let me stop here. I actually went quite far with this today. I was actually considering stopping a lot earlier despite what I said.

I figured out a cool trick on how to import attributes as detail attributes in a loop so you don't have to use channels in Hexpressions. You just use the various import nodes and re-export them. This is annoying to do, but it a lot better than having to mess around with copy pasting channels and whatnot.

I am going to have to redo the rotation to match what he is doing. He is using the AA noise inside a VOP node while I am doing something else. Is AA noise the simplex noise?

...No, no it is not. I can only use AA noise in VOP nodes unfortunately.

11am. Tomorrow, I am going to put a dent in this. I've gotten sidetracked from my original goal, but learning about volumes is a worthy endeavor at this point. I really am curious how his did those super realistic cliff, wall and rock faces."

---
## [WangyuHello/mpv](https://github.com/WangyuHello/mpv)@[c1a961ad78...](https://github.com/WangyuHello/mpv/commit/c1a961ad78b6d1da339e622c723d753a80687824)
#### Thursday 2022-02-24 09:57:35 by wm4

draw_bmp: rewrite

draw_bmp.c is the software blender for subtitles and OSD. It's used by
encoding mode (burning subtitles), and some VOs, like vo_drm, vo_x11,
vo_xv, and possibly more.

This changes the algorithm from upsampling the video to 4:4:4 and then
blending to downsampling the OSD and then blending directly to video.
This has far-reaching consequences for its internals, and results in an
effective rewrite.

Since I wanted to avoid un-premultiplying, all blending is done with
premultiplied alpha. That's actually the sane thing to do. The old code
just didn't do it, because it's very weird in YUV fixed point.
Essentially, you'd have to compensate for the chroma centering constant
by subtracting src_alpha/255*128. This seemed so hairy (especially with
correct rounding and high bit depths involved) that I went for using
float.

I think it turned out mostly OK, although it's more complex and less
maintainable than before. reinit() is certainly a bit too long. While it
should be possible to optimize the RGB path more (for example by
blending directly instead of doing the stupid float conversion), this is
probably slower. vo_xv users probably lose in this, because it takes the
slowest path (due to subsampling requirements and using YUV).

Why this rewrite? Nobody knows. I simply forgot the reason. But you'll
have it anyway. Whether or not this would have required a full rewrite,
at least it supports target alpha now (you can for example hard sub
transparent PNGs, if you ever wanted to use mpv for this).

Remove the check in vf_sub. The new draw_bmp.c is not as reliant on
libswscale anymore (mostly uses repack.c now), and osd.c shows an
error message on missing support instead now.

Formats with chroma subsampling of 4 are not supported, because FFmpeg
doesn't provide pixfmt definitions for alpha variants. We could provide
those ourselves (relatively trivial), but why bother.

---
## [pedrothepanda64/udmxdm](https://github.com/pedrothepanda64/udmxdm)@[ec4c3e7445...](https://github.com/pedrothepanda64/udmxdm/commit/ec4c3e7445b2cb66bd8196e8a1cb1a2e6075d533)
#### Thursday 2022-02-24 10:16:19 by pedrothepanda64

fix broken shit from last commit

this wouldn't have been a problem if I could just upload a file that's a little larger than 100 mb that actually REDUCES the overall file size. fuck you.

---
## [thinker227/RelineLang](https://github.com/thinker227/RelineLang)@[4c3ca6e063...](https://github.com/thinker227/RelineLang/commit/4c3ca6e0635bd59fe9674b638aea47afdd3f10a1)
#### Thursday 2022-02-24 11:31:12 by thinker227

Initial extension support

This is largely the default yo template, but the syntax highlighting works alright for now.

I had to install Node for this. Fuck you Node.

---
## [W2Codam/Minishell](https://github.com/W2Codam/Minishell)@[b0a601f22a...](https://github.com/W2Codam/Minishell/commit/b0a601f22a369d99e19cdb3bab5203496c04468c)
#### Thursday 2022-02-24 11:43:11 by W2.Wizard

Rip out all those ugly ass shit things, its global time

---
## [DataDog/libddprof](https://github.com/DataDog/libddprof)@[db8443da36...](https://github.com/DataDog/libddprof/commit/db8443da36808aebcc8916770eb0f5f691ec3bf4)
#### Thursday 2022-02-24 11:50:48 by Ivo Anjo

RFC: Introduce `ddprof_ffi_Buffer_from_byte_slice` function to enable reporting of external data using libddprof_ffi

 # Context:

The `ProfileExporterV3` high-level API enables libddprof_ffi callers to report profiling data without needing to know anything about the backend API.

The current signature of `build` (used to prepare a request) is:

```rust
 #[export_name = "ddprof_ffi_ProfileExporterV3_build"]
pub unsafe extern "C" fn profile_exporter_build(
    exporter: Option<NonNull<ProfileExporterV3>>,
    start: Timespec,
    end: Timespec,
    files: Slice<File>,
    timeout_ms: u64,
) -> Option<Box<Request>>
```

in particular, the payload data to be reported (usually pprof and JSON data) is provided using a `File`, which is defined as:

```rust
 #[repr(C)]
pub struct File<'a> {
    name: ByteSlice<'a>,
    file: Option<NonNull<Buffer>>,
}
```

and further, a buffer is represented as

```rust
/// Buffer holds the raw parts of a Rust Vec; it should only be created from
/// Rust, never from C.
 #[repr(C)]
pub struct Buffer {
    ptr: *const u8,
    len: size_t,
    capacity: size_t,
}
```

It follows from the required usage of `Buffer` that libddprof_ffi callers can only provide `Buffers` that were created by libddprof_ffi.

The only way a libddprof_ffi caller can get a `Buffer` containing profiling data, is through usage of `ddprof_ffi_Profile_serialize` which returns a `EncodedProfile` which contains a `Buffer` with the encoded data.

Thus, this means that libddprof_ffi callers **cannot provide their own data** to be reported, e.g. to report a pprof that was encoded using different means (for instance, if the runtime provided it), or to report the `code_provenance.json` or `metrics.json` extra files.

 # Use case:

My use case is the integration of libddprof_ffi into the Ruby profiler:
1. I want to make this a staged introduction, so in the first version I will only be using libddprof_ffi to report data, not to encode it
2. Ruby is already reporting `code_provenance.json` and this should continue to be reported even after moving to libddprof_ffi

 # Alternatives considered:

I considered two main approaches to this problem:

1. Introduce a new `ddprof_ffi_Buffer_from_byte_slice` API. This API copies a `ByteSlice` (an array of bytes) into a `Buffer`, which we can then happily use.

    Advantage: simpler, as no other APIs need to change to support this

    Disadvantage: introduces an extra copy of the data (even if temporary)

2. a) Modify `profile_exporter_build` to receive a `ByteSlice` inside `File`, not a `Buffer`

    Advantage: resulting API simpler and more concise to use; avoids extra copy from (1.)

    Disadvantage: involves several breaking API changes

2. b) Leave existing `profile_exporter_build` API, but add an extra one to receive `ByteSlice`s

    Advantage: no breaking API changes; avoids extra copy from (1.)

    Disadvantage: adds complexity and possibly duplication

In this PR, I decided to go with (1.), as it seems to me the extra copy is not that roblematic.

 # Additional Notes:

This is my first time writing Rust code so please DO suspect that EVERYTHING IS OFF AND THAT THIS IS A TERRIBLE MISTAKE.
And then help me figure out how to improve it :)

This writeup may be a bit overkill for this small change, but this is 20% sharing with the rest of the team what I'm doing and 80% working through this myself and making sure I understand what's up :)

 # How to test the change:

This is a new API; my plan is to integration test it on the dd-trace-rb side: write a test that validates that the correct HTTP requests are done, with the correct payloads.

---
## [alphagov/govuk_publishing_components](https://github.com/alphagov/govuk_publishing_components)@[6e0eb5b830...](https://github.com/alphagov/govuk_publishing_components/commit/6e0eb5b830a4d8209ffb4ecb6049c6eba7b6acdd)
#### Thursday 2022-02-24 12:15:40 by Kevin Dew

Clobber assets before running jasmine tests

I'm adding this in because we use globbing to match what files to test.
I'm concerned that without this we're at risk of the same files being
included multiple times (say you have application-1234.js, then edit it
and end up with application-2345.js)

It's a bit of a pain to do a clobber first as it means you'll always
have to experience the cost of compiling assets each test run, however
this is preferable to tests liable to fail.

---
## [GeorgeD88/Minesweeper-Solver](https://github.com/GeorgeD88/Minesweeper-Solver)@[b9140d9d15...](https://github.com/GeorgeD88/Minesweeper-Solver/commit/b9140d9d15e882731a878f00427738ef533a55fd)
#### Thursday 2022-02-24 12:29:57 by George Doujaiji

Condense README intro to concise paragraph

At first I wrote a whole fucking life story about the timeline of the
project and shit, but then I started revising and condensing it and
ended up making a much better intro with well delivered info.

---
## [BlackCatMS/V1-OOP](https://github.com/BlackCatMS/V1-OOP)@[0e4154a5de...](https://github.com/BlackCatMS/V1-OOP/commit/0e4154a5dee4f649d8d41d1a6355a4cf4a29c775)
#### Thursday 2022-02-24 15:59:58 by Josie

Practicum 3A, 3B, 4A checked

hate this class jesus christ why does everything have to go through one retarded single convention if there are at least 400 other ways to do it normally i hate this class and i hate java so much holy fuck

---
## [kdave/btrfs-devel](https://github.com/kdave/btrfs-devel)@[ff72a0795d...](https://github.com/kdave/btrfs-devel/commit/ff72a0795db3815a2819aa43acffc24b7e8e387d)
#### Thursday 2022-02-24 16:12:38 by Josef Bacik

btrfs: do not WARN_ON() if we have PageError set

Whenever we do any extent buffer operations we call
assert_eb_page_uptodate() to complain loudly if we're operating on an
non-uptodate page.  Our overnight tests caught this warning earlier this
week

  WARNING: CPU: 1 PID: 553508 at fs/btrfs/extent_io.c:6849 assert_eb_page_uptodate+0x3f/0x50
  CPU: 1 PID: 553508 Comm: kworker/u4:13 Tainted: G        W         5.17.0-rc3+ #564
  Hardware name: QEMU Standard PC (Q35 + ICH9, 2009), BIOS 1.13.0-2.fc32 04/01/2014
  Workqueue: btrfs-cache btrfs_work_helper
  RIP: 0010:assert_eb_page_uptodate+0x3f/0x50
  RSP: 0018:ffffa961440a7c68 EFLAGS: 00010246
  RAX: 0017ffffc0002112 RBX: ffffe6e74453f9c0 RCX: 0000000000001000
  RDX: ffffe6e74467c887 RSI: ffffe6e74453f9c0 RDI: ffff8d4c5efc2fc0
  RBP: 0000000000000d56 R08: ffff8d4d4a224000 R09: 0000000000000000
  R10: 00015817fa9d1ef0 R11: 000000000000000c R12: 00000000000007b1
  R13: ffff8d4c5efc2fc0 R14: 0000000001500000 R15: 0000000001cb1000
  FS:  0000000000000000(0000) GS:ffff8d4dbbd00000(0000) knlGS:0000000000000000
  CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
  CR2: 00007ff31d3448d8 CR3: 0000000118be8004 CR4: 0000000000370ee0
  Call Trace:

   extent_buffer_test_bit+0x3f/0x70
   free_space_test_bit+0xa6/0xc0
   load_free_space_tree+0x1f6/0x470
   caching_thread+0x454/0x630
   ? rcu_read_lock_sched_held+0x12/0x60
   ? rcu_read_lock_sched_held+0x12/0x60
   ? rcu_read_lock_sched_held+0x12/0x60
   ? lock_release+0x1f0/0x2d0
   btrfs_work_helper+0xf2/0x3e0
   ? lock_release+0x1f0/0x2d0
   ? finish_task_switch.isra.0+0xf9/0x3a0
   process_one_work+0x26d/0x580
   ? process_one_work+0x580/0x580
   worker_thread+0x55/0x3b0
   ? process_one_work+0x580/0x580
   kthread+0xf0/0x120
   ? kthread_complete_and_exit+0x20/0x20
   ret_from_fork+0x1f/0x30

This was partially fixed by c2e39305299f01 ("btrfs: clear extent buffer
uptodate when we fail to write it"), however all that fix did was keep
us from finding extent buffers after a failed writeout.  It didn't keep
us from continuing to use a buffer that we already had found.

In this case we're searching the commit root to cache the block group,
so we can start committing the transaction and switch the commit root
and then start writing.  After the switch we can look up an extent
buffer that hasn't been written yet and start processing that block
group.  Then we fail to write that block out and clear Uptodate on the
page, and then we start spewing these errors.

Normally we're protected by the tree lock to a certain degree here.  If
we read a block we have that block read locked, and we block the writer
from locking the block before we submit it for the write.  However this
isn't necessarily fool proof because the read could happen before we do
the submit_bio and after we locked and unlocked the extent buffer.

Also in this particular case we have path->skip_locking set, so that
won't save us here.  We'll simply get a block that was valid when we
read it, but became invalid while we were using it.

What we really want is to catch the case where we've "read" a block but
it's not marked Uptodate.  On read we ClearPageError(), so if we're
!Uptodate and !Error we know we didn't do the right thing for reading
the page.

Fix this by checking !Uptodate && !Error, this way we will not complain
if our buffer gets invalidated while we're using it, and we'll maintain
the spirit of the check which is to make sure we have a fully in-cache
block while we're messing with it.

CC: stable@vger.kernel.org # 5.4+
Signed-off-by: Josef Bacik <josef@toxicpanda.com>
Signed-off-by: David Sterba <dsterba@suse.com>

---
## [greenhas/hugo-website](https://github.com/greenhas/hugo-website)@[5d1f3e9a4c...](https://github.com/greenhas/hugo-website/commit/5d1f3e9a4c5693c5a5ccb53a671e001bea4fc288)
#### Thursday 2022-02-24 17:01:21 by Spencer Greenhalgh

post Remembering the time that the only person at church who understood my dissertation research was the one who worked for the state of Michigan doing social media surveillance of social justice movements.

---
## [mawrick26/SM8250](https://github.com/mawrick26/SM8250)@[a4a24c0c6f...](https://github.com/mawrick26/SM8250/commit/a4a24c0c6f8f9cef395a658d1754cde2c4930da9)
#### Thursday 2022-02-24 17:21:00 by Peter Zijlstra

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
Signed-off-by: Adam W. Willis <return.of.octobot@gmail.com>

---
## [TT-Amiga/gcc](https://github.com/TT-Amiga/gcc)@[aeac414923...](https://github.com/TT-Amiga/gcc/commit/aeac414923aa1e87986c7fc6f9b921d89a9b86cf)
#### Thursday 2022-02-24 20:25:17 by Thomas Schwinge

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
## [JohnKnee3/zookeepr](https://github.com/JohnKnee3/zookeepr)@[f530421036...](https://github.com/JohnKnee3/zookeepr/commit/f530421036858cfd1a0af4154957a30125dacb4e)
#### Thursday 2022-02-24 21:04:15 by john.a.clark3

11.1.5

We first used a simple
app.get('/api/animals', (req, res) => {
  res.send('Hello!');
});
That sent Hello if our .get was talking to animals.json animals object.

Then we updated it
app.get('/api/animals', (req, res) => {
  res.json(animals);
});
To grab the entire animals array using .get instead of .send.

Then we used this

app.get('/api/animals', (req, res) => {
  let results = animals;
  console.log(req.query)
  res.json(results);
});
+
 http://localhost:3001/api/animals?name=Erica
To console log the name Erica.

Finally we updated the .get into it's final form
app.get('/api/animals', (req, res) => {
  let results = animals;
  if (req.query) {
    results = filterByQuery(req.query, results);
  }
  res.json(results);
});
to set it up to receive .querys that talk to the function filterbyQuery.

function filterByQuery(query, animalsArray) {
  let filteredResults = animalsArray;
  if (query.diet) {
    filteredResults = filteredResults.filter(animal => animal.diet === query.diet);
  }
  if (query.species) {
    filteredResults = filteredResults.filter(animal => animal.species === query.species);
  }
  if (query.name) {
    filteredResults = filteredResults.filter(animal => animal.name === query.name);
  }
  return filteredResults;
}
Which will look at what you type for example
http://localhost:3001/api/animals?name=Erica
grabs Erica's object
{
      "id": "2",
      "name": "Erica",
      "species": "gorilla",
      "diet": "omnivore",
      "personalityTraits": ["quirky", "rash"]
    },
and
http://localhost:3001/api/animals?species=gorilla
would grab
{
"id": "1",
"name": "Terry",
"species": "gorilla",
"diet": "omnivore",
"personalityTraits": [
"anxious",
"goofy"
]
},
{
"id": "2",
"name": "Erica",
"species": "gorilla",
"diet": "omnivore",
"personalityTraits": [
"quirky",
"rash"
]
}
We finally set up the personalityTraits query which is a bit more involved because it is an array.

function filterByQuery(query, animalsArray) {
  let personalityTraitsArray = [];
  // Note that we save the animalsArray as filteredResults here:
  let filteredResults = animalsArray;
  if (query.personalityTraits) {
    // Save personalityTraits as a dedicated array.
    // If personalityTraits is a string, place it into a new array and save.
    if (typeof query.personalityTraits === "string") {
      personalityTraitsArray = [query.personalityTraits];
    } else {
      personalityTraitsArray = query.personalityTraits;
    }
    // Loop through each trait in the personalityTraits array:
    personalityTraitsArray.forEach((trait) => {
      // Check the trait against each animal in the filteredResults array.
      // Remember, it is initially a copy of the animalsArray,
      // but here we're updating it for each trait in the .forEach() loop.
      // For each trait being targeted by the filter, the filteredResults
      // array will then contain only the entries that contain the trait,
      // so at the end we'll have an array of animals that have every one
      // of the traits when the .forEach() loop is finished.
      filteredResults = filteredResults.filter(
        (animal) => animal.personalityTraits.indexOf(trait) !== -1
      );
    });
  }
was added to the top and used the initial if statement to check if you one trait else you checked for multiple.  Then it assings it to the personality traits array let.  Then using for each it finds each query and grabs what is needed.

Very dense and may need to read again.

---
## [maltejur/next.js](https://github.com/maltejur/next.js)@[91146b23a2...](https://github.com/maltejur/next.js/commit/91146b23a21e33d54332a469f30afe6e6156cd65)
#### Thursday 2022-02-24 21:16:41 by Glenn Gijsberts

Make adjustment to cache config of with-apollo example (#32733)

## Description
This year we implemented the new Apollo config using this example. We recently moved to `getServerSideProps` as well, however, this was giving us some cache problems. The issue was that the cache was older than the actual data that was coming from the server side query. 

Because the `merge` of the cache in `apolloClient.js` is merging the existingCache in the initialState it will overwrite the "fresh" initialState with properties that already exists. This means that if you have something in your cache from previous client render, for example `user` with the value `null`, and you go to a new page and do a new query on the server which returns a value for the `user` field, it will still return `null` because of that `merge` function.

Since this was weird in our opinion, we've changed this in our own environment by always overwriting the existing cache with the new initialState, so that the initialState that is coming from a fresh server side query is overwriting. We thought it was a good idea to reflect this also in this example, because we couldn't think of a reason why the existing cache should overwrite fresh queries.

I've added a reproduction that shows what this is exactly about. I hope my description makes sense, let me know what you think!

## Reproduction of old scenario
Created a reproduction branch here: https://github.com/glenngijsberts/with-apollo-example. Using a different API than in the example, because of https://github.com/vercel/next.js/issues/32731.

1. checkout the example
2. yarn
3. yarn dev
4. visit http://localhost:3000/client-only
5. Hit "Update name". This will run a mutation that will update the cache automatically. Because I use a mocked API, the actual value on the API won't be updated, but this is actually the perfect scenario for the problem because in reality data can already change in the meantime when you're doing a new request.
6. Go to the SSR page
7. This will display two values: one is coming from the server side request (which is the latest data, because no cache is used in `getServerSideProps`) and the other is using the cache, which is outdated at that point, yet it's still returned because the old way of merging the cache was picking the existing cache over the initialState that was coming from the fresh server side query.

## Documentation / Examples

- [x] Make sure the linting passes by running `yarn lint`

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[160c526de4...](https://github.com/mrakgr/The-Spiral-Language/commit/160c526de492f5e571eda39145319fd108f5f7b9)
#### Thursday 2022-02-24 21:33:01 by Marko Grdinić

"10:45am. It seems I forgot to commit yesterday. So much for my years long perfect commit streak. Let me do it now and then I will resume the tutorial.

11:05am. Did a little reply on the Github issue page. Let me start the volume tutorial.

///

Which part of the 90s are you trying to emulate?? If you're talking about the early-mid 1990s there ware few things to keep in mind.

1.There was no Subdivision surfaces until around 1997-1998, so there was no way to smooth low poly models into smooth, high poly ones. Can you imagine moving thousands of verticies around by hand? Yeah... not happening.

During the early-mid 1990s there was only low poly modeling, extruding along splines, revolving/lathing splines, and NURBS for high-end work.

2.As far as texturing goes, there was not automatic UV unwrap like today , so people just used simple texture mapping options like planar, spherical, or cylindrical mapping. Or they relied on the fact that spline objects (lofts/extrudes, lathes/revolves, and NURBS) all had automatic texture coordinates. (e.g. if you were to take a spline and revolve it into a vase, cup, jar, etc. the texture coordinates would be automatic)

There was also the option of using 3D procedural textures (wood, marble, noise, cloud, granite, etc.). These didn't require texture coordinates at all.

3.For lighting and rendering, people tended to use shadow maps or very sharp, hard raytraced shadows. Soft raytraced shadows take a very long time to render. Also, gamma correction was almost never used.

4.Animation: High end 3D software had the option to use skeleton deformation, but low end work tended to consist of characters that were just made of seperate objects "parented" to one another.

To get an idea of what I mean:
http://www.youtube.com/watch?v=aJgV6LBUFgA&t=14m17s

http://www.youtube.com/watch?v=DaDZZze4w20&t=0m22s
-----------

There really isn't much difference between the very late 90s (like 1998-2000). Because all the things above I mentioned don't apply. They had all the "advanced" features that people take for granted today (subdivision surfaces, automatic uv unwrap, etc.)

///

No answers to any of my questions in the Houdini thread, but I thought this post was interesting enough to archive.

11:20am. Hmmm, this is tough. When I use the Transform matrix VOP, it works, but I get crazy deformations on a few points. Why is this happening? It did not happen with a regular transform.

11:25am. The problem is not with the transform, but with extrude. It does something crazy for whatever reason if I rotate the points first. I'll have to move it to before the rotation like yesterday.

It does not matter.

Also, I just noticed that extrude has local control attributes. Using those might have made more sense than one big distance. But still, how would per point or per primitive scales work? I'll leave that mistery for later.

11:35am. Oh, rather than that the Clean SOP does the trick. Cleaning up degenerate primitives resolves my problem. Now that I see the spot, I noticed that even when extrusion is done first there are weird shading artefacts at the affected spot.

11:50am. The VOPs are actually quite nice to use. You can do it all in Vex, but it is easier to shot yourself there. I hate having to figure out which argument is which. I can't remember the order of anything.

Focus me. Let me resume the tutorial now that I've put in the AA noise for rotation.

12:35pm. This is so annoying. I want to move into the tutorial, but I am getting issues with degenerate primitives and the clean node is not doing its thing.

Come to think of it, this should not be happening. The problem can't be because of volumes. Self intersections should...Hmmm...

https://forums.odforce.net/topic/48042-avoiding-self-intersection-when-displace-along-n/

I won't go into this now since it is 40m.

12:45pm. Let me undo, I need to make sure that spike is due to extrusion.

So far, this tutorial could have been better in preparing me against these footguns.

1pm. I figured out an improvement. Instead of promoting the piece attribute to something lower, I can just import it directly. I do get the primnum even in point VOPs.

1:05pm. This is ridiculuos. There are all sorts of problems that arise due to self intersections when adding noise like this. The tutorial guy is adept at not running into them for some reason, but it just confirms what I suspected - adding noise like this is not great. I'd be better off using the voronoi fractures as a mask on a height map. But I suppose this way of doing things would get me a slanted cliff. Still there might be better way of doing that using height maps.

Let me continue with the tutorial. I had to turn off the initial point VOP to get this to work.

1:10pm. Let me have breakfast here. I am overdue for it.

2:10pm. Done with food. Let me do the chores.

4:40pm. Done with chores. Let me chill for a bit.

5:15pm. Let me start. First off, let me play around with a cube. I want to see how remesh deals with intersecting meshes.

Hmmm, I see.

It seems that self intersections aren't actually a problem by themselves when either remeshing or converting to volume.

Still, I am not really happy with adding noise to points diretly. It might be better to just displace them in the normal direction.

Well, no matter, let me move on. Where was I?

5:55pm. Had to leave for lunch. Let me resume. I want to keep going for a while longer.

6:10pm. Houdini segfaulted on me.

6:25pm. I can't figure out how to make combine work on my own. Let me see how he does it.

6:30pm. Ohhh, the VDB booleans are density sensitive.

https://youtu.be/WTg_pVZoac0?t=3641

Let me try immitating this.

7:05pm. At this point I am wondering strongly what the various settings are.

7:20pm. This is too annoying. I'll figure out how to clip properly later. For now let me just lower the amount of voxels as it is taking forever to make any change.

Now, why am I not seeing the AA noise related resampling changes correctly.

7:30pm. I just noticed that AA noise allows me to pick the noise type between Perlin and Simplex.

So it is not a different kind of noise than the ones offered to me.

7:55pm. You know what, I hate working with noise like this.

8pm. https://youtu.be/WTg_pVZoac0?t=3752

Sigh, did he do all this just for the edges?

https://youtu.be/WTg_pVZoac0?t=3990

I am almost mad at this course now. I am not a fan of stacking noise on top of one another. Given how much of it he put on the volume level, messing with the mesh should have been wholly unecessary.

Based on how things are going I should have just gone with my own idea for getting those floating tiles. I am starting to doubt that I need volumes to implement my idea.

It would certainly be more efficient that messing with volumes. Well, let me plow on. I should at least watch this to completion.

https://youtu.be/WTg_pVZoac0?t=4071

Oh, it broke the inside as well.

https://youtu.be/WTg_pVZoac0?t=4286

Yeah, let me just watch this thing for now. I can always go back and try it by hand if I want to. I feel like I've gotten enough exp with volumes from playing around today and yesterday with this.

https://youtu.be/WTg_pVZoac0?t=4643

This guy is operating on another level than me. I can only see some nasty goop in this, but he seems to think he has something useful.

8:35pm. Let me read Kaiji. At this point I really feel like closing.

8:50pm. https://youtu.be/WTg_pVZoac0?t=5093

Let me pause this here. I want to go through VDB basics.

https://youtu.be/9VcIP7ByDGE
Boolean Denting (VDB Basics)

He said he would explain why the interior needs to be filled, but so far, no explanation has been forthcoming, so I'll go with this Entagma tutorial.

8:55pm. https://youtu.be/9VcIP7ByDGE?t=426

I bet SDF stands for surface density function. That other tutorial did not explain why he is using the fog instead of the surface proper.

But these voxels are a pain in the ass. I can't even imagine how annoying it would be to do the background for the scene using voxels instead of shader nodes in Blender.

https://youtu.be/9VcIP7ByDGE?t=785

He is giving me advice on how to export here. It seems if it is just for a single frame, even Alembic is fine. I do not know what that format is, but it bides well for exporting to USD.

https://youtu.be/GdvVco6O-Ok
Houdini VDB In 5 minutes

Let me watch this.

I am starting to understand some things. volumes can be used as remeshable surfaces. This is what they've been doing.

That rock surface tutorial really annoys me because most likely 95% of the processing and more has gone into vertices that weren't even the edges. What he had done is all about getting those nice cracks, but all the time I am spending waiting is on the flat and the inner parts. Hell, the cracks themselves are only half a dozen voxels tall. It is is a scam.

https://youtu.be/GdvVco6O-Ok?t=82

He says they will throw up the empty voxels. But does that apply if I check fill interior? Does that apply to the fog VDB which has density?

And for the surface VDB, what does distance from voxel mean?

Ah, I see. If I go into wireframe mode, I can see the exterior and interior bands.

https://youtu.be/GdvVco6O-Ok?t=181

You can clip it like this. Interesting.

9:35pm. That video was a bit informative, but I am still not sure how the various VDBs differ. Right, he created that attribute and it served as a custom VDB.

9:45pm. https://youtu.be/UKED3rpvYEw?t=458

SDF is the Signed Distance Field! I got it wrong.

I was absolutely sure the the S is going to be surface and extrapolated based on that.

https://youtu.be/UKED3rpvYEw?t=704

At first I thought it was spew to convert to VDB and back, but maybe that is how Blender's shitty remesher works. It would explain why seprate geometries get glued together.

10:10pm. https://youtu.be/WTg_pVZoac0?t=5212

Enough, let me stop here for the day.

Tomorrow, I think I will stop experimenting so much and just watch the rest of the video. After that I'll go with my own ideas.

10:15pm. https://www.openvdb.org/download/
> This Houdini hip file demonstrates many of the nodes in the toolkit and illustrates fundamental concepts such as OpenVDB tree structures, tiles and voxels, narrow-band level sets and fog volumes. More importantly, it presents recommended workflows for common tasks like particle surfacing, polygon conversion, fracturing, filtering, resampling, extrapolation, etc. The current hip file is tested with Houdini 18.5.351 and OpenVDB 8.1.

Found this in the forum. I'll download this file and go into it tomorrow.

Right now I do not really understand fog volumes and how its density works. In the docs I read something about powers of two for the inner parts, but I did not understand how that could work unless I fill the interior.

And filling the interior is really bad. Though it is not as expensive as I'd feared, but it is still 10x more expensive than vanilla.

10:20pm. Moreover I hate the noise sculpting method. Is that how Rohan did it? I'll have to check. When I saw him doing his thing the first time, I did not pay too close of an attention to what nodes he was using, but now I've trained my memory a bit and should be able to digest exactly what he is doing.

10:25pm. Damn, the file gives me pages of errors. But I might be able to get something out of it. It seems like a very well done example.

10:30pm. This is really thorough, there is a ton of stuff in the VDB examples file. I am sure to learn quite a bit from this. Let me leave it for tomorrow. It is time for rest."

---
## [Jayman2000/godot-docs-pr](https://github.com/Jayman2000/godot-docs-pr)@[b872229427...](https://github.com/Jayman2000/godot-docs-pr/commit/b872229427dddb9b749f46af597e85e25cf2955a)
#### Thursday 2022-02-24 22:46:54 by Rémi Verschelde

Remove controversial satirical piece 🔥

This piece was written back in 2014 before open sourcing Godot, and while its
intent is to be sarcastic, it leaves ample room for misinterpretation.

The intended meaning of this piece was, and always has been, the following:

Exploitative game mechanics suck. Games are a beautiful and artful medium
which can provide players with a wide range of experiences: entertainment,
enlightenment, joy, sadness... Games can be just for fun or they can bear
a message. They can connect people with each other or open the player's mind.

Make games worth your players' time and their money, and do your best to do so
while running a successful and respectful business. Hugs <3

---
## [laundmo/NorthstarLauncher](https://github.com/laundmo/NorthstarLauncher)@[ac13d8e3d1...](https://github.com/laundmo/NorthstarLauncher/commit/ac13d8e3d168d9b7a5b010e9b76b664bb6ad392c)
#### Thursday 2022-02-24 23:30:02 by Emma Miler

Added code for chathooks

This may not seem like much to a passing observer, but this commit took me 30 hours of blood, sweat, tears, IDA debugging, server crashes, and insanity.

---
## [i3roly/glibc_ddwrt](https://github.com/i3roly/glibc_ddwrt)@[0be4c905a6...](https://github.com/i3roly/glibc_ddwrt/commit/0be4c905a6c2ed34b76dddc808fc86df491df899)
#### Thursday 2022-02-24 23:36:12 by gagan sidhu

48427/4.14.268 revert dnsmasq+fix 3040+misc. "a friend without autotune is not a friend of mine" - randy marsh

- fixed the 3040 build. turns out the ramcode combo caused it to have a
  seizure
- on that note i noticed dnsmasq sucked balls on the 3040, and it seems
  the new version has issues. i have moved back to 2.86 as it was weird
  that 2.87test* was having issues staying up and assigning a lease.
- minor tweaks, really. nothing of note aside from the kernel update and
  whatever egc keeps fucking with. he should tell that assfuck to move
  back to 2.86. i bet assfuck kept it on 2.87 to ruin my builds because
  he knows they're better than his :P

really i was so annoyed with the 3040 build not working that i am not
interested in posting some diatribe about how marsh is being as big of
an assfuck as BS (hahaha) because someone wants to use this badly, so
i'll just cut to the PIZZASTE

TESTED AND WORKING

* Shelly's room, evening. Randy knocks on her door *

Randy
        Shelly, that's enough time on your phone.

Shelly
        Leave me alone, Dad! Stop nagging me all the time!

Randy
        You know we're all cutting down on phone time.

Shelly
        [sits up]

        Don't limit me! You don't even understand me!

Randy
        [sees a poster of himself as <'famous' "musician">,
        his secret identity]

        Yeah. I don't understand you at all. A lot you know.

        [walks away saddened]

        *   The Marsh garage    *

*  Randy is adding more stacks of cash to those already  *
*    hidden behind the poster. A door opens and Randy    *
*            quickly seals it up.                        *

* He gets to his workbench just as Stan closes the door. *

Stan
        Uh hey Dad. I need to talk to you.

Randy
        Oh really? A-About... about what?

Stan
        Dad, is it possible for someone to be one way on
        the outside but totally different on the inside?

        [Randy sighs deeply and stands up to walk]

        I mean, can someone identify as one sex but be
        something else but still have it be nothing about sex?

Randy
        Yes. Yes, Stan. I am <'famous' "musician">.

Stan
        ...What?

Randy
        It started off so simple. There's a guy at work. Hanson.
        He would use the bathroom and just blow the thing up, you know?
        Not only that, but he was in there all the time! I finally got
        fed up and pretended to be a woman.
        I called myself <'famous' "musician">. Have you ever been in a
        woman's bathroom, Stan? It's all clean and there's enough stalls
        for everyone. It was so freeing. I started singing while I was
        in there, and then I- started writing things down.

Stan
        Well you said you knew a guy at work who was
        <'famous' "musician">'s uncle.

Randy
        Yah, that's my cover.

Stan
        The chick that wrote the theme song to the new
        <shitty recession stimulus-funded book and movie series>, is you?

Randy
        Yeah.

        [turns around and faces Stan]

        The record company messed it all up. It was supposed to go:

            "<shitty recession stimulus-funded book and movie series>,
            yah yah yah, yah yah yah! <shitty recession stimulus-funded
            book and movie series>."

        But they just- do what they want with my songs.

Stan
        Wha-wait, <'famous' "musician"> sounds like a girl.

Randy
        Autotune. Wanna see how I do it?

        [moments later, a music program pops up.
        Twelve tracks are shown at lower left]

        I come up with all my best stuff in the bathroom at work.

        I use this program to import the recordings I make on my phone.

        [plays the highlighted track]

            "Yeah yeah, feeling good on a Wednesday. Sparklinnnnn'
            thoughts. Givin' me the hope to go ohhhn"

            [farts and poop noises]

            "Oh! Whoa. What I need now is a little bit of shelter."

Stan
        Dad, <'famous' "musician">'s music is actually really good.

Randy
        Thanks.

        But it gets even better when I add the drum loops.

        [replays the same track with drum loops added]

        Then with the computer I can actually quantize everything.

        [brings up the quantizer and chooses his settings]

        Backup instruments.

        [scale, beats, bass, tambourine, guitars, strings]

        And then finally I use the Autotune.

        ["Auto-Tuner v10." He chooses his settings there, and
        the song is transformed. The same track is now enhanced
        with <no name shitty "musician">'s voice and no trace of Randy]

            "Sparklin' thoughts, feelin' good on a Wednesday.
            Givine me the hope, givin' givin' me the hope to go ohhhn.
            What I need is a little bit of shelter."

        [this is all too much for Stan to take in, and he passes out.]

        [Randy notices]

        Stan?

---

