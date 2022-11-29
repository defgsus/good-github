## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-11-28](docs/good-messages/2022/2022-11-28.md)


2,207,500 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,207,500 were push events containing 3,309,142 commit messages that amount to 256,037,129 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 43 messages:


## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[37b60d187d...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/37b60d187daa6b8c8f2c2623dbf49555774a90aa)
#### Monday 2022-11-28 00:10:24 by SkyratBot

[MIRROR] Fixes attempting to offset floating planes [MDB IGNORE] (#17745)

* Fixes attempting to offset floating planes (#71490)

## About The Pull Request

This is a dumb idea, and leads to fucked rendering on occasion

## Why It's Good For The Game

Fixes another portion of #70258, a player will no longer have a hidden
antag hud if they move down a z level after getting an antag. We were
trying to offset the floating plane of their image, and it went to shit.
Also fixes a bug with observers not having antag huds for the combo hud
to see. We were only giving them one on mind.on_transfer, rather then on
mind assignment. I hate mindcode

* Fixes attempting to offset floating planes

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [GabrielHenaut/philosophers](https://github.com/GabrielHenaut/philosophers)@[169a7cc31d...](https://github.com/GabrielHenaut/philosophers/commit/169a7cc31d8c5b47c395c87bc0cb629b724e5c75)
#### Monday 2022-11-28 00:14:23 by Gabriel Henaut

added the pthread flag so it compiles on the workspace... i hate my life

---
## [readpo/postgres](https://github.com/readpo/postgres)@[1d072bd203...](https://github.com/readpo/postgres/commit/1d072bd2030af0f2eaa522449028ff160f71ebf8)
#### Monday 2022-11-28 01:22:45 by Tom Lane

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
## [Zergspower/Skyrat-tg](https://github.com/Zergspower/Skyrat-tg)@[0b9264ce5f...](https://github.com/Zergspower/Skyrat-tg/commit/0b9264ce5f14565e42d5e3dc67660a95f5d48f65)
#### Monday 2022-11-28 02:56:14 by SkyratBot

[MIRROR] Fixes mineral turfs having weird lighting [MDB IGNORE] (#17618)

* Fixes mineral turfs having weird lighting (#71219)

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

* Fixes mineral turfs having weird lighting

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [ravitri/cluster-version-operator](https://github.com/ravitri/cluster-version-operator)@[9222fa9a66...](https://github.com/ravitri/cluster-version-operator/commit/9222fa9a6616b58a8056c780b9a6252e82a26e37)
#### Monday 2022-11-28 02:57:43 by W. Trevor King

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
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[c185dffda0...](https://github.com/tgstation/tgstation/commit/c185dffda0cc30d8187fa1ba37e5784b8d630ba4)
#### Monday 2022-11-28 04:14:08 by Jacquerel

Basic Mob Carp Bonus Part: Wall smashing (#71524)

## About The Pull Request

Atomisation of #71421 
This moves the attack function of "environment smash" flags which allow
simple mobs to attack walls into an element, so that we can put it on
other things later.
For some reason while working on carp I convinced myself that they had
"environment_smash" flags, which they do not, so this actually is not
relevant to carp in any way.

While implementing this I learned that the way wall smashing works is
stupid, because walls don't have health and so resultingly if a mob can
attack walls it deletes them in a single click. If we ever decide to
change this then it should be easier in an element than in three
different `attack_animal` reactions.
This is especially silly with the "wumborian fugu" item which allows any
mob it is used on to instantly delete reinforced walls, and also to
destroy tables if they click them like seven or eight times (because it
does not increase their object damage in any way).

## Why It's Good For The Game

Eventually someone will port a basic mob which does use this behaviour
(most of the mining ones for instance) and then this will be useful.
If we ever rebalance wall smashing to not instantly delete walls then
this will also be useful.
Admins can apply this to a mob to allow it to delete walls if they
wanted to do that for some reason, they probably shouldn't to be honest
at least until after we've done point two unless they trust the player
not to just use it to deconstruct the space station.

## Changelog
:cl:
refactor: Moves wall smashing out of simple mob code and into an element
we can reuse for basic mobs later
/:cl:

---
## [mexisme/nixos-hardware](https://github.com/mexisme/nixos-hardware)@[540c80a85a...](https://github.com/mexisme/nixos-hardware/commit/540c80a85a0fe032e928726a9033e1515207fbdc)
#### Monday 2022-11-28 04:39:10 by mexisme

Initial port from github.com/linux-surface/linux-surface, vendorising the patches and firmware binaries.

Add MS Surface Kernel patches from github.com/linux-surface/linux-surface

Add MS Surface Firmware from github.com/linux-surface/linux-surface

Add MS Surface Hardware config from github.com/linux-surface/linux-surface

Tie-together the Microsoft Surface .nix files

Set to use explicit version of Linux (5.4.7)

- Add the config for Linux 5.4.7

Add kernel 5.4.11

Add kernel 5.4.13

Remove unsupported patches

Revert to kernel 5.4.7 for now

- Problems initialising touchscreen & pen

Add kernel 5.4.15 and 5.4.16

Build kernel 5.4.16, instead

Add kernel 5.4.22

Update the patches for kernel 5.4

Placeholder for Linux kernel 5.5

Copy the IPTS kernel patch from the 5.5 dir to the 5.4 dir.

Conversation on https://gitter.im/linux-surface/community suggested this would
reenable IPTS on 5.4:

-----
@matrixbot Feb 29 15:33
hpfr Blaž Hrastnik (Gitter): thanks for the mention. mexisme (Gitter) finally, someone who actually knows Nix and isn't just a config nerd writing proper NixOS Surface configs! I am stuck on 4.19 at the moment because IPTS is now a proper reverse-engineered kernel driver (https://github.com/linux-surface/intel-precise-touch) instead of just a blob package, and I haven't had time to look at how to package that for Nix. If you're on 5.5, are you just not using IPTS? Would love to help out on packaging that for NixOS
hpfr also, development conversations seem to happen more at #linux-surface on freenode, which you can connect to with matrix via https://matrix.to/#/!OXIGGPCpnzaNVeGtCA:matrix.org if you don't like IRC clients

@matrixbot Feb 29 15:39
hpfr Also, I'm not using jakeday's patches, I'm using the more recent ones from the linux-surface/linux-surface repo, but yeah, for 4.19, so they're a bit different from the 5.x patchsets. afaik 4.19 is still supported because it's the last LTS release that supports the "official" IPTS blob before Linux made changes that required reverse engineering a driver that didn't use GuC submission (I'm just quoting here, I have no idea what that is haha)

@matrixbot Feb 29 19:27
Blaž > now a proper reverse-engineered kernel driver
Should be similar to before, we just offer it as a patch
Blaž https://github.com/linux-surface/linux-surface/blob/master/patches/5.5/0007-ipts.patch
Blaž Anyway I'm keeping an eye out on your NixOS builds since I'm thinking about giving it a try

@matrixbot Feb 29 19:32
Blaž Currently running Arch but using nix as a way to manage development environments for various projects

@matrixbot Mar 01 10:41
hpfr Blaž: well shoot is that patch all that’s necessary for building in-tree? It does all the things the linux-surface/intel-precise-touch repo does?

Dorian Stoll @StollD Mar 01 12:56
Yes
Just adds all the files from the repo to drivers/input/touchscreen and adds the necessary glue to drivers/input/touchscreen/{Makefile, Kconfig}

@matrixbot Mar 02 09:13
hpfr Dorian Stoll (Gitter): oof. Could’ve been on 5.4+ all this time!

Move kernnel *.nix packages under their respective kernel dirs

Use lib.mkDefault

Update to kernel 5.4.24

Update to kernel 5.5.8

Typo

Drivers are modules by default

Revert to 5.4.24 until can fix the config failures

---
## [Mothblocks/tgstation](https://github.com/Mothblocks/tgstation)@[7d04edb6e2...](https://github.com/Mothblocks/tgstation/commit/7d04edb6e2927330906a7af89664b7a5ab3aa48c)
#### Monday 2022-11-28 06:04:07 by Profakos

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
## [cheungglenda/comp1170-project2](https://github.com/cheungglenda/comp1170-project2)@[843b2ba00b...](https://github.com/cheungglenda/comp1170-project2/commit/843b2ba00b67e63cabfc8d5d70a0c94e14436a75)
#### Monday 2022-11-28 06:04:24 by justinweiyungwu

Merge pull request #14 from cheungglenda/justin

holy fucking shit

---
## [nytmyr/Server](https://github.com/nytmyr/Server)@[c8f146943c...](https://github.com/nytmyr/Server/commit/c8f146943c0392c476f67c64350d329f4b477858)
#### Monday 2022-11-28 06:06:23 by toxin06

[Bots] AI Revamp, add all holds, delays, thresholds, min thresholds, character heal settings. Bard fixes.

All group features for combat range and behind mob now work in raids

Every spell type can have a delay, minimum and maximum threshold to cast.

The delay is how quickly a bot can cast that type of spell, the timer starts from the beginning of the cast. If you set this to 10 seconds, as soon as a spell starts casting, another will start in 10 seconds provided it isn't on cooldown or has stacking/immune blocks.

The minimum threshold is the percent of health when a bot will stop casting a spell.
-Escapes, Hate Reductions, Lifetaps and Shaman In-Combat Buffs (Canni) will rely upon the bot's OWN health. (When do you want said bot to start trying to drop aggro, when they reach 80% until 20%? Do they lifetap starting at 60% and never stop till they die? (0%).

Threshold or maximum threshold is the percent of health when the bot will begin casting that type of spell.

Casters will now output what type of spell and what spell they are casting for all spell types except buffs.

Casters will now output all those messages to the entire group or raid, filterable by Pet Response.

Casters now dispel, escape, lifetap, snare and root automatically.

SKs will now cast their bonus hate spells as the spell type in-combat buffs rather than nuke so it can be held if needed.

Shamans will still Cannibalize using in-combat buffs, however you can set the minimum threshold to control when they stop Cannibalizing and the Maximum threshold will be based off their mana to start Cannibalizing.
--Shamans will never start to cannibalize if their mana is above 90% or their health is below 50% regardless of the minimum/maximum setting.

SKs, Paladins and Clerics will not cast their in-combat buffs if they have hit their stop melee level.

SKs, Rangers, Wizards, Enchanters and Bards will now cast hate reduction spells.

Necros/SKs will cast their Darkness line as the Snare spell type.
--Necros will not cast Insidious Retrogression.

Bards will now start casting their songs before they fade instead of waiting for them to fade so there is no gap in buffs.
-------
Casters no longer try to cast DoTs, nukes, roots or snares if it may result in aggro. Once enough aggro is built up by the tank to where they don't think they'll pull aggro, they will begin casting.
--SKs & Pallies will always cast these regardless of aggro, use holds or thresholds if you want them to stop.

Resist checks for spells will now take into affect level differences as well. (Higher level mobs are more likely to resist a spell than a lower level mob with the same resist stats)

If a target mob is Undead, Summoned or Plant, the appropriate classes will cast the appropriate nukes if available.
-Necromancers will nuke plants with Defoliation if they are of level.

Bots will verify spell immunity before casting all spell types.

Roots are held by default.

Bots will now honor Blocked Buffs. You can use this to get bots to cast other buffs. If you only want Virtue for example you would block Faith, Kazad's Mark and Ward of Gallantry.
--Look at bot spells lists on Allaclone to see what spells they can cast to control this.

Bots will now cast buffs that contain Illusions if you don't block them (Boon line for example.)

You can now set your player characters/clients to specific heal thresholds and delays that bots will respect.
-------
Pets will be healed using the default delay settings and can be toggled on/off with ^holdpetheals
-You can control when they start healing pets by stances, stances will only be used for this now as everything else is customizable
-The exception to this is that Warriors, Paladins and Shadowknights will enter a taunting state by default if set to Aggressive. This can still be toggled off by ^taunt as usual.

The thresholds for stances are as follows:
-Reactive will do all the regular default heals starting with HoTs @ 85%, CHs @ 70%,  Regular Heals @ 55% and Fast Heals @ 35%
-Efficient will start with CHs @ 70%, Regular Heals @ 55%, Fast Heals @ 35%
-Balanced (default) will start with Regular Heals @ 55% and Fast @ 35%.
-Burn will only cast Fast Heals/Regular Heals starting at 35%.
-BurnAE will only Fast Heals/Regular Heals starting @ 25%.
-Aggressive will ignore all and not heal at all, you don't want a tank stopping to heal.

-If a bot cannot cast a Fast Heal, CH or HoT, they will try the next best spell in order of: Fast Heal->Regular Heal->Complete Heal->Heal Over Time.
-Any Heal that casts in 2 seconds or less is considered a Fast Heal

---
## [UWINGS-KUNYI/ti-kernel](https://github.com/UWINGS-KUNYI/ti-kernel)@[adee8f3082...](https://github.com/UWINGS-KUNYI/ti-kernel/commit/adee8f3082b01e5dab620d651e3ec75f57c0c855)
#### Monday 2022-11-28 06:16:45 by Peter Zijlstra

x86/nospec: Unwreck the RSB stuffing

commit 4e3aa9238277597c6c7624f302d81a7b568b6f2d upstream.

Commit 2b1299322016 ("x86/speculation: Add RSB VM Exit protections")
made a right mess of the RSB stuffing, rewrite the whole thing to not
suck.

Thanks to Andrew for the enlightening comment about Post-Barrier RSB
things so we can make this code less magical.

Cc: stable@vger.kernel.org
Signed-off-by: Peter Zijlstra (Intel) <peterz@infradead.org>
Link: https://lkml.kernel.org/r/YvuNdDWoUZSBjYcm@worktop.programming.kicks-ass.net
[bwh: Backported to 5.10: adjust context]
Signed-off-by: Ben Hutchings <benh@debian.org>
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[a811adac74...](https://github.com/tgstation/tgstation/commit/a811adac74513494a620fae631da95d2626b1be7)
#### Monday 2022-11-28 06:28:14 by Epic

Changes Admin Prison to be Anti-Telekinesis: Walls off equipment rooms, replaces computers, and makes the tables tidy (#71433)

First PR, may require some changes or something because I don't know how
to do anything bleh
## About The Pull Request

We already had issues with crewmembers with telekinesis making changes
to the security records (purging them and what not). And, nothing has
been done about it, not yet, anyway. Not only record computers are a
problem as well.


![image](https://user-images.githubusercontent.com/106710384/203241399-8314bcba-d2d0-44af-9360-30ff58dbc39e.png)
Previously, prisoners can access the sec vendor with telepathy, and,
since the vendor is free, spam the vendor and be an annoyance. Sure, I
believe that it is not as big of a problem as purging the security
records, but I feel like it's against what the prison is supposed to
stand for; It's supposed to stop them and get them to listen to ahelps
thrown at them.

I've decided to make a bit of changes to the prison to make it so that
people with telekinesis won't fuck up things as much. This replaces real
computers with nonfunctional ones, adding walls to equipment areas to
make sure prisoners don't spam the vendor, and deletes guns/weapons from
the tables so they won't grab them.

## Why It's Good For The Game


![image](https://user-images.githubusercontent.com/106710384/203241465-833f79da-58a3-4feb-87b0-091fbb846e93.png)
This PR is more tailored to admins dealing with no-good-doers, and goes
for the vibe of "HEY, SOMEONE IS PMING YOU, REPLY TO THEM INSTEAD!" Of
course, this leads to prisoners not interacting with the current round,
and, less chance of them going insane and breaking all the windows with
a telekinesis auto-rifle.

Plus, this can always be reverted in-case someone comes up with coding
stuff in instead. I'm all through with that and willing to work with
whoever to solve the issue.

Also, of course, Closes #60967

## Changelog

:cl:
admin: Nanotrashen made some top-of-the-line changes to their
top-of-the-line prison by walling off their equipment area and removing
some spare guns they somehow left on the tables. We also stole the
security computers, so people with telekinesis can't access them.
/:cl:

---
## [NOUIY/git](https://github.com/NOUIY/git)@[f1c903debd...](https://github.com/NOUIY/git/commit/f1c903debdcbf6aaf8fd3abf222fa941b42d5d31)
#### Monday 2022-11-28 06:28:41 by Ævar Arnfjörð Bjarmason

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
## [mattdway/CreateWithVR](https://github.com/mattdway/CreateWithVR)@[188557a3c2...](https://github.com/mattdway/CreateWithVR/commit/188557a3c203a604725429005b76bd13c158c018)
#### Monday 2022-11-28 06:49:02 by mattdway

11-03-22 Commit

11-3-22		v2.2.3
11-03-22 Commit
Fixed a bug that one of my students found play testing on 11-03-22.  Under the correct circumstances when using teleport anywhere he was able to teleport himself outside the bounds of the room by placing the cursor between the room and the watering can.  I adjusted the teleportation anywhere plane so that there is now a  buffer on all four sides of floor and the outside walls in which teleportation is no longer possible.

I tested and I was not able to get out of bounds in the way found previous.

Papers can still clip through the floor and this does not appear to be due to this teleportation area layer.
 main
@mattdway
mattdway committed 15 hours ago

11-22-22	v2.3.1
11-22-22 Commit
No individual commits for 11/17/22 or 11/20/22 so all commits for these two dates plus on 11/22/22 are being made in the 11-22-22 Commit.

On 11/17/22 By creating no teleport plane that I made the same size as the furniture and plant by the window and by setting it slightly above the teleport anywhere plane by about .01 I was able to create a blocked area where teleportation can’t happen. This is neater and easier than trying to shrink the teleport anywhere plane as there are still areas by the window I want people to be able to get to.

I also duplicated this no teleport plane and positioned it under the desk and table with the food. Essentially any opportunity to teleport under/into an object and/or an object near s collider wall I want to eliminate as a teleport anywhere area.

Thus no teleporting outside the room (hopefully).

On 11/17/22 I also organized my hands, hands controllers and hand rays into child objects of parent objects for neatness and organization sake. It is now much easier to find the physics hand game objects, the non-physics hand game objects, the hand controller game objects and the hand ray game objects in the Hierarchy, especially since these objects are no longer exclusively childed.

On 11/20/22 I was able to rotate the ghost hands in scene so that these are facing the same way as my physical hands in the beginning. This means the ghost hands now have the same rotation as my physical hands without having to set it in C# code.

On 11/20/22 The colliders are still an issue. The swirling ghost hands at the beginning are still an issue. The hands not being hidden when picking something up is still an issue. I'm still troubleshooting to try and figure out why these bugs exist so that i have a better idea of how to patch these.

One more bug I have added to my list... whenever I use any reset button (or a reset from the reset menu) my physics hands are not present. So I also need to look at the code for that reset and see why the scene resets without those hand game objects present.

On 11/20/22 I solved the swirling hand issue by setting the controller parent object for both NP hands to be the exact same transform as my physics hand controllers. It's the controller difference and not the hand difference, I think, that was triggering the ghost hand code. I've tested twice and the physics hands are the active hands immediately and the non physics hands still show up when I press down on the couch arm. So both are activated and the NP hands only show up with that 0.05m

On 11/22/22 Turning off the Interactables/Right Hand Physics and the Interactables/Left Hand Physics in the Physics Matrix of the Project Settings stopped the weird collisions from happening while holding items but because the interactables also have both Rigidbodies and colliders (as they already had to have this for the XR Grab Interactable to work), this means my hands still knock around objects that I pick up. This also allows the hide hands method to work correctly, so my hands once again disappear.

By changing the interactable's Rigidbody's Collision Detection from Continuous Dynamic to Continuous Speculative I was also able to prevent interactable objects from clipping through the walls.  These items are now stopped when hitting walls.  You also now can't clip through the walls while holding items.

I was able to use a Hierarchy search for Rigidbody then I was able to Ctrl + select all my interactable items and then I set the Rigidbody Collision Detection to Continuous Speculative on all those objects at once.

Fixed the interactable items not colliding with the walls and door issue.  The XR Grab Interactable's Movement Type wasn't set to Velocity Tracking in all cases, thus in some cases where this was set to Kinematic, collisions were being ignored.  Fixed now and all the interactable items now seem to be stuck within the confines of the room without exiting out.  Also, I haven't yet found any item that I am holding that allows my hands to clip through the walls, despite the code that disables the colliders when holding an item.  So this seems to work well with physics hands.

I still need to fix the reset bug that reverts the objects in play mode back to non-interactable hands with no physical hands present.  This may be because code is reloading the main scene and not the secondary scene I saved as for building and testing purposes.  That scene will eventually be saved back over to the main scene once I've done a few more play tests and this may fix that issue.

---
## [MushiTea/21438_ChaoticCurrent_REPO](https://github.com/MushiTea/21438_ChaoticCurrent_REPO)@[502402ae79...](https://github.com/MushiTea/21438_ChaoticCurrent_REPO/commit/502402ae7968a18481b99f2af62261075c47f828)
#### Monday 2022-11-28 07:06:36 by Boredom

Srinirek push (#19)

* 11/26/22

* Omg girl do you watch forged in fire? Cuz I want you to pick usable steel from this pile of scrap metal to use as the base for your blades. They must meet the following parameters, a length between 8-10 inches, a full tang with a length of 3-4 inches, and width from spine to cutting edge of at least 1 1/2 inch but no longer than 2 1/2 inches. In the next round, you will be attaching handles to your blades to turn them into fully functional weapons. And for the third round we will put it through a series of tests, such as, dummy stab for sharpness, chain chop for durability, and a sheet metal stab for edge retention. And the two winners of the third round will be sent to their home forges to recreate an iconic weapons from history. The winner of the final round will go home with the title of forged in fire champion and a check for $10,000. Your time starts, now!

Essentially what we did was fix claw,slide, and arm positions and I added manual arm just because - Srinirek

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[6483cb7db1...](https://github.com/treckstar/yolo-octo-hipster/commit/6483cb7db1ebe9874fa79fb4a6ce439e6a44aa1f)
#### Monday 2022-11-28 07:22:01 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [Wolfsrudel/awesome-console-services](https://github.com/Wolfsrudel/awesome-console-services)@[4b8f298fb2...](https://github.com/Wolfsrudel/awesome-console-services/commit/4b8f298fb2b94b3c492da39ca43fcd2775907eea)
#### Monday 2022-11-28 07:37:47 by techie2000

ascii.town is no longer interactive

Attempting to access it now results in 
```
================================================================================

Nazis, fuck off!

Sorry to everyone else who enjoyed this space.  It was only a matter
of time, and it lasted a lot longer than I ever expected.  It breaks
my heart to log in and see hate on the canvas.  Obscurity is no
longer enough to keep this space as pleasant as it once was.  I'll
clean up what I can and keep https://ascii.town/explore.html running
so that what was created here can continue to be enjoyed.  Thank
you all for your contributions over the years.  You made something
beautiful.

Black lives matter.  Trans rights are human rights.  Much love to
all the gay weirdos out there.

~june

torus@ascii.town  2017-2022

================================================================================
```

---
## [Empire-Strikes-Back/Doc](https://github.com/Empire-Strikes-Back/Doc)@[d44ab51886...](https://github.com/Empire-Strikes-Back/Doc/commit/d44ab518862178ae79c9a0b028fa9dd113e026b0)
#### Monday 2022-11-28 09:43:51 by Doc

give me the damn page!

unlike TheViper we cannot divide ourselves between AoE2 and 4 - wine and beer

like Kip Andersen - different docuemntarie, same style - and garden - different programs but same network - wine

I listen to Jesus - I know about kingdom divided within itself, Pharisee yeast, blood and body, where and faith

let wine be wine - not beer
like Harry Tusker - ready to  jump on a horse between roofs into a pool

:Kristen-Jaimie-Lee-Wiig pooped my pants and proud of it!

---
## [apollographql/router](https://github.com/apollographql/router)@[cfb421a564...](https://github.com/apollographql/router/commit/cfb421a5646de4ae5d5634415c86336d70c6fb90)
#### Monday 2022-11-28 09:56:33 by Bryn Cooke

Fixes #2123 (#2162)

Issue was introduced with #2116 but no release had this in.

Move operations would insert data in the config due to the delete magic
value always getting added. Now we check before adding such values.

We may need to move to fluvio-jolt longer term.

<!--
First, 🌠 thank you 🌠 for considering a contribution to Apollo!

Some of this information is also included in the /CONTRIBUTING.md file
at the
root of this repository.  We suggest you read it!

  https://github.com/apollographql/router/blob/HEAD/CONTRIBUTING.md

Here are some important details to keep in mind:

* ⏰ Your time is important
To save your precious time, if the contribution you are making will
take more than an hour, please make sure it has been discussed in an
        issue first. This is especially true for feature requests!

* 💡 Features
Feature requests can be created and discussed within a GitHub Issue.
Be sure to search for existing feature requests (and related issues!)
prior to opening a new request. If an existing issue covers the need,
please upvote that issue by using the 👍 emote, rather than opening a
        new issue.

* 🕷 Bug fixes
These can be created and discussed in this repository. When fixing a
bug,
please _try_ to add a test which verifies the fix. If you cannot, you
should
still submit the PR but we may still ask you (and help you!) to create a
test.

* 📖 Contribution guidelines
Follow https://github.com/apollographql/router/blob/HEAD/CONTRIBUTING.md
when submitting a pull request. Make sure existing tests still pass, and
add
        tests for all new behavior.

* ✏️ Explain your pull request
Describe the big picture of your changes here to communicate to what
        your pull request is meant to accomplish. Provide 🔗 links 🔗 to
associated issues! Documentation in the docs/ directory should be
updated
        as necessary.  Finally, a /CHANGELOG.md entry should be added.

We hope you will find this to be a positive experience! Contribution can
be
intimidating and we hope to alleviate that pain as much as possible.
Without
following these guidelines, you may be missing context that can help you
succeed
with your contribution, which is why we encourage discussion first.
Ultimately,
there is no guarantee that we will be able to merge your pull-request,
but by
following these guidelines we can try to avoid disappointment.

-->

Co-authored-by: bryn <bryn@apollographql.com>

---
## [emorozov/dwm](https://github.com/emorozov/dwm)@[67d76bdc68...](https://github.com/emorozov/dwm/commit/67d76bdc68102df976177de351f65329d8683064)
#### Monday 2022-11-28 10:13:05 by Chris Down

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
## [Salex08/tgstation](https://github.com/Salex08/tgstation)@[fccd833526...](https://github.com/Salex08/tgstation/commit/fccd833526364b131ce440b4ab0e65022103927c)
#### Monday 2022-11-28 10:47:26 by GoldenAlpharex

Fishing Odds Code Improvements and Rescue Hooks (#71415)

## About The Pull Request
I wanted to try and implement an easier way for people to fish out
corpses from chasms, as I heard many tales of people trying to fish
others out of chasms and it taking over one IRL hour, with some cases
where it would take over two hours. Obviously, that's not really
interesting gameplay, and it doesn't really give people an incentive to
fish, it just turns it into an annoyance that people won't want to do
for fun. Now, we don't want that, do we?

As such, I've created the rescue hook, a special fishing hook that can
only be used in chasms (as that's currently the only place you can find
people into), which will only be able to fish out duds, skeleton
corpses, any mob that's fallen into a chasm and hasn't been rescued yet,
or rarely, a hostile monster lurking below. It has, at the time of
writing this, a weight of 5 (50 without bait, lower with bait) for duds
and a weight of 30 for chasm detritus, which themselves have a 50%
chance to be a random skeleton corpse, or a lobstrosity, and the
remaining 50% chance of fishing out a mob that's fallen into a chasm.
I'm open to tweaking these values if we think it's too easy or too hard,
but it's still a rather expensive item, so I'd consider it quite fine
the way it is myself, as it's still not risk-free.

It's currently only obtainable through buying it from cargo in the
goodies section, at a default price of 600 credits (making it
SIGNIFICANTLY more expensive than the rest of the fishing content, and
making it something that assistants will have to put some elbow grease
into if they want to be able to afford it).

As it stands currently, it can't be used to recover the fallen's
belongings that weren't on their person (i.e., their crusher if they
were holding it in hands), ~*but* I'm down to make that easier to fish
out using, for instance, the magnet hook, while also making it
incompatible with fishing out bodies, which would make it a nice way to
recover those lost items without spending over an hour fishing for them,
if that's something that maintainers would want.~ Maintainers did want
it, and as such...

The Magnetic hook is now the go-to hook to retrieve objects from chasms!
Not only does it inherently do a much better job at fishing out
non-fishes, it also has a lesser chance of retrieving random junk from
chasms, and an even lower chance of fishing out lobstrosities!

I also improved the code for the fishing weights calculation so that the
hooks and the rods can have an effect on the odds of certain types of
rewards more easily, with the option of offloading a more of what's
currently being calculated on `fishing_challenge` over on the rods or
even the hooks themselves.

I finished by fixing a handful of capitalization and punctuation issues
in various fishing items, as that bugged me when I was testing my
changes.

## Why It's Good For The Game
Corpses being recoverable from chasms was a great idea, however making
it so people would have to sink a major portion of their shift for a
chance at recovering a corpse doesn't create a particularly interesting
gameplay loop. However, being able to spend your hard-earned funds in
order to streamline that process without really being able to use that
to cheese other mechanics sounds like a great deal to me.

## Changelog

:cl: GoldenAlpharex
add: Added a Rescue Hook, that will allow the fishing rod it's attached
onto to become a lot more proficient at recovering corpses from chasms,
at the expense of making it unusable for more traditional fishing. It
isn't entirely lobstrosity-proof, however...
balance: The magnetic hook can no longer fish out corpses from chasms,
but will fish out items much more efficiently than any other hooks,
while also being much less attractive to lobstrosities. Some still fall
for it regardless, however.
spellcheck: Fixed the capitalization and punctuation in the description
of multiple fishing accessories.
code: Improved the code for fishing weights, to allow for different
hooks to have some more noticeable results on the weights without having
to add to an already massive proc.
/:cl:

---
## [Salex08/tgstation](https://github.com/Salex08/tgstation)@[0747099063...](https://github.com/Salex08/tgstation/commit/074709906301e3e396179c861ca0af068c3f36ec)
#### Monday 2022-11-28 10:47:36 by RikuTheKiller

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
## [Salex08/tgstation](https://github.com/Salex08/tgstation)@[bf582cb833...](https://github.com/Salex08/tgstation/commit/bf582cb833d89b7121b4fefa37e8da1773783245)
#### Monday 2022-11-28 10:47:36 by Profakos

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
## [Salex08/tgstation](https://github.com/Salex08/tgstation)@[bbb956d2a6...](https://github.com/Salex08/tgstation/commit/bbb956d2a670656e546c35a09ec27295e5e06e94)
#### Monday 2022-11-28 10:47:36 by OrionTheFox

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
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[9b70bfcb2e...](https://github.com/treckstar/yolo-octo-hipster/commit/9b70bfcb2e00c6cda403ac521a16ae94e89ef174)
#### Monday 2022-11-28 11:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [mindplay-dk/sql](https://github.com/mindplay-dk/sql)@[ebd772dd1d...](https://github.com/mindplay-dk/sql/commit/ebd772dd1d8b4f1f5c08ab32da768b7ee0cb0660)
#### Monday 2022-11-28 11:41:34 by Rasmus Schultz

add support for yield $index => $value in mappers

this feature was missing and has been implemented as described in the README.

this is actually a bugfix, but it's also potentially a breaking change for some poorly implemented mappers - specifically, if your mapper inadvertedly discards the indices of the given array (effectively renumbering the values) this bug would previously help this case by simply renumbering the entire result.

for example, the following mapper function is lossy and discards indices:

function my_mapper(array $rows)
{
  foreach ($rows as $row) {
    yield $row;
  }
}

If you were using batches of, say, 20 records, this mapper would return an array with indices 0..19 for the first batch, and indices 0..19 again for the second batch, and so on. This coud likely cause nasty bugs in a loop that actually uses these keys for something, since the keys of each batch would collide with the keys of the previous batch.

The faulty batch processing behavior would simply renumber these as 0..19, 20..39 and so on, since it was effectively discarding your bad indices and renumbering everything.

With the introduction of this change, Result::createIterator() will assign a running $record_index, which ensures unique indices across batches - these indices will propagate to mappers, but if any mapper discards the indices, well, you get key collissions... meaning, anywhere we use iterator_to_array() or Result::all() etc. you can expect colliding entries to (silently!) disappear.

The good news is, if you're using Result::all() you're probably not using batches - since you're intentionally loading the entire result into a single array. If you did specify a page size, however, and one of your mappers discards indices, then yeah, you'll have problems.

This would seem to be a limitation of the array type in the PHP language, unfortunately. There's no difference between "array being used as a map" and "array proper" in PHP, hence no way to type-hint or even for our code to type-check at run-time.

Well, we could collect all the keys, test for collisions, and throw exceptions - but this would mean memory overhead for all keys in memory, which is potentially a problem for scripts working with very large batches.

We might be able to test for key collisions in Result::all() since here we expect everything to fit in memory anyhow - so adding an exception here might be a meaningful addition?

---
## [RayaanJIrani/GUIHW4](https://github.com/RayaanJIrani/GUIHW4)@[13db2db18f...](https://github.com/RayaanJIrani/GUIHW4/commit/13db2db18f53ab8e788c98316a84e7941bc5d2a1)
#### Monday 2022-11-28 12:38:40 by RayaanJIrani

I got the fucking images working... Good fucking night bitches

---
## [raekuul/mm6-skill-emphasis-mod](https://github.com/raekuul/mm6-skill-emphasis-mod)@[e3c946bab8...](https://github.com/raekuul/mm6-skill-emphasis-mod/commit/e3c946bab89e1661b1fe14fc7282d086e8b64dbc)
#### Monday 2022-11-28 12:41:13 by Malekitsu

Fixed exp

11. Rescue a Damsel in Distress 5K
12. Find Lord Kilburn's Shield 10K (running past thoose wolves is hard, and you will die for sure)
14. Drink from the Fountain of Magic 5K
15. Storm the Silver Helm Outpost 5k
18. Get Knight's Nomination 5K
24. Slay Longfang Witherhide. 30K (with fixed dragon there is no need to change that, 15k if unfixed)
27. Repair the temple 5k
28. Capture the Prince of Thieves. 15k ( I think you need to complete dragoons and shadow guild first, also going up there from the sewers isn't non combat)
29 Fix the prices of all stables. 5K (super annoying)
30 Visit the Altar of the Sun 5K
32. Visit the Altar of the Moon 30K
34 End winter 15K ( I think you need fly spell to get there)
36 Reset all of the Dragon Towers 15K (you need to clear icewind keep first, so at that point in the game 5k will be just too low)

---
## [yangjiaxin1995/react](https://github.com/yangjiaxin1995/react)@[b6978bc38f...](https://github.com/yangjiaxin1995/react/commit/b6978bc38f6788c7e73982b9fd2771aabdf36f15)
#### Monday 2022-11-28 12:48:58 by Andrew Clark

experimental_use(promise) (#25084)

* Internal `act`: Unwrapping resolved promises

This update our internal implementation of `act` to support React's new
behavior for unwrapping promises. Like we did with Scheduler, when 
something suspends, it will yield to the main thread so the microtasks
can run, then continue in a new task.

I need to implement the same behavior in the public version of `act`,
but there are some additional considerations so I'll do that in a
separate commit.

* Move throwException to after work loop resumes

throwException is the function that finds the nearest boundary and
schedules it for a second render pass. We should only call it right 
before we unwind the stack — not if we receive an immediate ping and
render the fiber again.

This was an oversight in 8ef3a7c that I didn't notice because it happens
to mostly work, anyway. What made me notice the mistake is that
throwException also marks the entire render phase as suspended
(RootDidSuspend or RootDidSuspendWithDelay), which is only supposed to
be happen if we show a fallback. One consequence was that, in the 
RootDidSuspendWithDelay case, the entire commit phase was blocked,
because that's the exit status we use to block a bad fallback
from appearing.

* Use expando to check whether promise has resolved

Add a `status` expando to a thrown thenable to track when its value has
resolved.

In a later step, we'll also use `value` and `reason` expandos to track
the resolved value.

This is not part of the official JavaScript spec — think of
it as an extension of the Promise API, or a custom interface that is a
superset of Thenable. However, it's inspired by the terminology used
by `Promise.allSettled`.

The intent is that this will be a public API — Suspense implementations
can set these expandos to allow React to unwrap the value synchronously
without waiting a microtask.

* Scaffolding for `experimental_use` hook

Sets up a new experimental hook behind a feature flag, but does not
implement it yet.

* use(promise)

Adds experimental support to Fiber for unwrapping the value of a promise
inside a component. It is not yet implemented for Server Components, 
but that is planned.

If promise has already resolved, the value can be unwrapped
"immediately" without showing a fallback. The trick we use to implement
this is to yield to the main thread (literally suspending the work
loop), wait for the microtask queue to drain, then check if the promise
resolved in the meantime. If so, we can resume the last attempted fiber
without unwinding the stack. This functionality was implemented in 
previous commits.

Another feature is that the promises do not need to be cached between
attempts. Because we assume idempotent execution of components, React
will track the promises that were used during the previous attempt and
reuse the result. You shouldn't rely on this property, but during
initial render it mostly just works. Updates are trickier, though,
because if you used an uncached promise, we have no way of knowing 
whether the underlying data has changed, so we have to unwrap the
promise every time. It will still work, but it's inefficient and can
lead to unnecessary fallbacks if it happens during a discrete update.

When we implement this for Server Components, this will be less of an
issue because there are no updates in that environment. However, it's
still better for performance to cache data requests, so the same
principles largely apply.

The intention is that this will eventually be the only supported way to
suspend on arbitrary promises. Throwing a promise directly will
be deprecated.

---
## [wincent/wincent](https://github.com/wincent/wincent)@[e93badb049...](https://github.com/wincent/wincent/commit/e93badb049442bd9f93e5d57a3534e9392904d49)
#### Monday 2022-11-28 13:01:41 by Greg Hurrell

chore: note what we _would_ do if we wanted to install Homebrew Ruby

So I had little play with this to see if it is worth it, and sadly, I
don't think it is.

The rationale: Sorbet requires at least Ruby 2.7.0, and macOS Ventura
(2022) ships with Ruby 2.6 (2018). Ruby 2.6 is old/unsupported, so
"overwriting" it seams reasonable.

The reality: my system has a fragile dependency on Ruby. Neovim depends
on Ruby, and I get Neovim from Homebrew. I need Ruby support in Neovim
for Command-T (well, not really, as I am using the Lua version now, but
I'd still like it to work). It is not clear to me whether installing
Neovim before/after installing Ruby will produce a working set-up, or
whether I can have them be somewhat independent.

So, I tried out the code in this commit, adding the new Ruby to the
start of the path. Neovim `:checkhealth` notes that the Command-T C
extension doesn't work. If I try to use it, I see this:

    command-t.vim could not load the C extension.
    Please see INSTALLATION and TROUBLE-SHOOTING in the help.
    Vim Ruby version: 2.6.10-p210
    Expected version: 2.6.8-p205
    For more information type:    :help command-t-ruby

which is actually super puzzling. I think this means that the extension
didn't load, and the version numbers are misleading about why. The
current OS (Ventura) is running 2.6.10, and that's why that shows up
even though it isn't first in the `$PATH` (when Neovim was built, maybe
it linked against a specific version, or maybe it didn't). When
Command-T was built, pre-Ventura, 2.6.8 was probably the current
version, so that's what's showing up in the message. In reality, Neovim
must be using not 2.6.10 but the 3.1.0 version coming from Homebrew,
which is why the extension isn't loading.

I could fix all this by rebuilding, but it doesn't feel particularly
robust. So, I put my `$PATH` back the way it was before, did a rebuild,
and everything works again.

The other problem. Even with the new version of Ruby, I can't run `srb`
in the main repo I work in because it dies looking for a million
uninstalled Gems. I don't want to (and perhaps can't) install those, and
much less on an ARM Mac. So, if `srb` won't run, Neovim can't use it to
provide LSP services.

Finally, the bootstrap process is annoyingly interdependent. For
example, I install Neovim and Ruby with Brew in the "homebrew" aspect.
Later, in the "ruby" aspect, I install gems, but for those to work, the
`$PATH` has to already be up-to-date. But the `$PATH` won't be
up-to-date because it was set up in the "dotfiles" aspect earlier on in
the process, but from an older shell, which means that the `$PATH` won't
become active until next time I open a terminal. I could fix this by
updating the path in the running install process, but that feels rather
bothersome.

Overall, I deem this too much effort and the juice is not worth the
squeeze.

---
## [vicirdek/PsychonautStation](https://github.com/vicirdek/PsychonautStation)@[03bc97ade5...](https://github.com/vicirdek/PsychonautStation/commit/03bc97ade5a76f156229b946e38816ced97a0e30)
#### Monday 2022-11-28 13:43:18 by necromanceranne

Nukies Update 6: Interdyne is here for you! Medical Supplies and Atropine! (#71067)

## About The Pull Request

Quite a few changes overall to the nuclear operatives tactical medkit.
The kit is more of a full suite of equipment for performing field
medical duties as a nukie.

- I've split the medkits between two kinds. Basic and premium. Medical
bundle has the premium kit.
- Basic contains additional amounts of basic c2 chem patches, some spare
atropine autoinjectors, sutures and regen mesh, and some basic medical
equipment for tending wounds. 4 TC (as it was before). That's it.
- The premium kit is a far more useful full suite of advanced medical
equipment, MODsuit modules, medical supplies and cybernetic implants,
including the combat hypospray and the combat defib. 15 TC.

**In the premium kit, there is:**
- It has a box of beakers with powerful healing chems. Omnizine,
salicylic acid, oxandrolone, pentetic acid, atropine, salbutamol and
rezadone.
- The combat injector is empty, so you can load it as necessary.
- There are advanced sutures and regenerative mesh packs. They don't
work through spacesuits, but are invaluable for wound repair. Especially
burns.
- There is a surgery arm toolset so you can do field operations without
lugging tools.
- There is a surgery processor module that comes preloaded with advanced
surgeries, a threadripper module, and the combat defib module. The
module works entirely like a combat defib, but you don't need to lose
your belt slot to use it.
- The surgeries are revival, the upgrade surgeries (like vein
threading), brainwashing (did you know they didn't get access to
brainwashing, I think this is a shame) and the better tend wounds
option.
- The nightvision medical hud doubles as a pair of science goggles.

**Atropine changes:**
- Atropine now stops bomb implants from autoexploding. This does **NOT**
stop you from manually detonating the bomb. (This is possible even when
you're dead and haven't left your body)
- As a result, nukies get atropine medipens so that they can potentially
stop themselves detonating prematurely, or stop their allies detonating
prematurely. They have a little pamphlet to help explain how their
microbomb works.

## Why It's Good For The Game

Straight up: The medkit is ass.

The meds in the injector sucks, just getting c2 meds in patches is kind
of insulting for something granted to you from an uplink item (and also
you get those for free with your ~~xbox~~ infiltrator medical room so
lol), and operatives just got the kit for one reason and one reason
only. That combat defib as a _weapon_.

Fuck that. So the kits now much better as a way to both support yourself
AND your team through providing a range of improvements you can provide
the squad, while also not undermining the reason why people may have
wanted the kit (that defib). I would really like to see more nukies
attempt to support one another in combat, and a medic operative is a
role that needs love to make that a reality.

**Edit here**: I reintroduced a low end kit with more c2 medical
supplies _if you want them_. I can see how someone might pinch all of
the medical supplies like a cunt, so maybe we should have a failsafe for
that.

A huge culprit of the lack of value of support meds was usually that
ops...explode when they die. If a medic can pop atropine into an op
before they die, they might be able to save them, or an op could pop
themselves with atropine prematurely to maybe stave off death.

## Changelog
:cl:
balance: Splits the nuclear operative combat medical kit into two
versions: basic and premium.
balance: Basic contains additional amounts of basic c2 chem patches,
some spare atropine autoinjectors, sutures and regen mesh, and some
basic medical equipment for tending wounds. 4 TC (as it was before).
balance: The premium kit is a far more useful full suite of advanced
medical equipment, MODsuit modules, medical supplies and cybernetic
implants, including the combat hypospray and the combat defib. 15 TC.
balance: Atropine stops bomb implants from automatically detonating on
death. You can still manually activate your bomb implant (even when you
are dead).
balance: Operatives start with an atropine pen to stop themselves and
their allies from detonating so they can hopefully be saved by a medical
operative.
add: There is a pamphlet to explain this in the nuclear operative's
survival box.
add: I'm not telling you to read the pamphlet, but you should probably
read the pamphlet.
/:cl:

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [zxaber/tgstation](https://github.com/zxaber/tgstation)@[25d4afc869...](https://github.com/zxaber/tgstation/commit/25d4afc869585373571da5ba4a77fb967ffdedfe)
#### Monday 2022-11-28 14:32:42 by Iamgoofball

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
## [knz/cockroach](https://github.com/knz/cockroach)@[1d04cec7c5...](https://github.com/knz/cockroach/commit/1d04cec7c5f887d309e09b7b5a267d5269d86b5a)
#### Monday 2022-11-28 15:07:01 by craig[bot]

Merge #91394 #91627

91394: changefeedccl: roachtest refactor and initial-scan-only r=samiskin a=samiskin

Epic: https://cockroachlabs.atlassian.net/browse/CRDB-19057

Changefeed roachtests were setup focused on running a workload for a specific duration and then quitting, making it difficult to run an `initial_scan_only` test that terminated upon Job success.

We as a team have also noticed a greater need to test and observe changefeeds running in production against real sinks to catch issues we are unable to mock or observe from simple unit tests.  This is currently a notable hassle as one has to set up each individual sink and run them, ensure the changefeed is pointing to the right URI, and then be able to monitor the metrics of this long running process.  

This change refactors the cdcBasicTest into distinct pieces that are then put together in a test.  This allows for easier experimentation with live tests, allowing us to spin up a cluster and a workload, run one or more changefeeds on it, set up a poller to print out job details,have an accessible grafana URL to view metrics, and wait for some completion condition.

Changing the specialized `runCDCKafkaAuth`, `runCDCBank`, and `runCDCSchemaRegistry` functions were left out of scope for this first big change.

The main APIs involved in basic roachtests are now:
- `newCDCTester`: This creates a tester struct to run the rest of the APIs and initializes the database
- `tester.runTPCCWorkload(tpccArgs)`: Starts a TPCC workload from the last node in the cluster
- `tester.runLedgerWorkload(ledgerArgs)`: Starts a Ledger workload from the last node in the cluster
- `tester.runFeedLatencyVerifier(changefeedJob, latencyTargets)`: starts a routine that monitors the changefeed latency until the tester is `Close`'d
- `tester.waitForWorkload`: waits for a workload started by `setupAndRunWorkload` to complete its duration
- `tester.startCRDBChaos`: This starts a Chaos routine that periodically shuts nodes down and brings them back up
- `tester.newChangefeed(feedArgs)`: starts a new changefeed on the cluster and returns `changefeedJob` object
- `changefeedJob.waitForCompletion`: waits for a changefeed to complete (either success or failure)
- `tester.startGrafana`: Sets up a grafana instance on the last node of the cluster and prints out a link to a grafana, this automatically runs unless `--skip-init` is provided.  If `--debug` is not used, `StopGrafana` will be called on test teardown to publish prometheus metrics to the artifacts directory.

An API that is going to be more useful for experimentation are:
- `changefeedJob.runFeedPoller(ctx, stopper, onInfo)`: runs a given callback every second with the changefeed info

Roachtests can be ran locally with the `--local` flag or on an existing cluster without destroying it afterwards with `--cluster="my-cluster" --debug`

Ex: After adding a new test (lets say `"cdc/my-test"`) to the `registerCDC` function you can keep running 
```bash
./dev build cockroach --cross # if changes made to crdb
./dev build roachtest         # if changes made to the test

./bin/roachtest run cdc/my-test --cluster="my-cluster" --debug
```
as you try out different changes or options.  If you want to try a set of steps against different versions of the app you could download those binaries and use the `--cockroach="path-to-binary"` flag to test against those instead.

If you want to set up a large TPCC database on a cluster and reuse it for tests this can be done with roachtests's `--wipe` and `--skip-init` flags.

Release note: None

91627: upgrade: introduce "permanent" upgrades r=andreimatei a=andreimatei

This patch introduces "permanent" upgrades - a type of upgrade that is
tied to a particular cluster version (just like the existing upgrades)
but that runs regardless of the version at which the cluster was
bootstrapped (in contrast with the existing upgrades that are not run
when they're associated with a cluster version <= the bootstrap
version). These upgrades are called "permanent" because they cannot be
deleted from the codebase at a later point, in contrast with the others
that are deleted once the version they're tied drops below
BinaryMinSupportedVersion).

Existing upgrades are explicitly or implicitly baked into the bootstrap
image of the binary that introduced them. For example, an upgrade that
creates a system table is only run when upgrading an existing,
older-version, cluster to the new version; it does not run for a cluster
bootstrapped by the binary that introduced the upgrade because the
respective system tables are also included in the bootstrap metadata.
For some upcoming upgrades, though, including them in the bootstrap
image is difficult. For example, creating a job record at bootstrap
time is proving to be difficult (the system.jobs table has indexes, so
you want to insert into it through SQL because figuring out the kv's for
a row is tedious, etc). This is where these new permanent upgrades come
in.

These permanent upgrades replace the `startupmigrations` that don't have
the `includedInBootstrap` field set. All such startupmigrations have
been copied over as upgrades. None of the current `startupmigrations`
have `includedInBootstrap` set (except one but that's dummy one since
the actual migration code has been deleted), so the startupmigrations
package is now deleted. That's a good thing - we had one too many
migrations frameworks.

These permanent upgrades, though, do not have exactly the same semantics
as the startupmigrations they replace. To the extent that there is a
difference, the new semantics are considered more desirable:
- startupmigrations run when a node that has the code for a particular
  migration startups up for the first time. In other words, the
  startupmigrations were not associated with a cluster version; they were
  associated with a binary version. Migrations can run while old-version
  nodes are still around.  This means that one cannot add a
  migration that is a problem for old nodes - e.g. a migration creating a
  job of a type that the old version wouldn't recognize.
- upgrades are tied to a cluster version - they only run when the
  cluster's active version moves past the upgrade's version. This stays
  the case for the new permanent migrations too, so a v2 node will not
  immediately run the permant migrations introduced since v1 when it joins
  a v1 cluster. Instead, the migrations will run when the cluster version
  is bumped. As such, the migrations can be backwards incompatible.

startupmigrations do arguably have a property that can be desirable:
when there are no backwards compatibility issues, the v2 node can rely
on the effects of the startupmigrations it knows about regardless of the
cluster version. In contrast, with upgrades, not only is a node unable
to simply assume that a particular upgrade has run during startup, but,
more than that, a node is not even able to look at a version gate during
the startup sequence in order to determine whether a particular upgrade
has run or not (because, in clusters that are bootstrapped at v2, the
active cluster version starts as v2 even before the upgrades run). This
is a fact of life for existing upgrades, and now becomes a fact of life
for permanent upgrades too. However, by the time user SQL traffic is
admitted on a node, the node can rely on version gates to correspond to
migrations that have run.

After thinking about it, this possible advantage of startupmigrations
doesn't seem too useful and so it's not reason enough to keep the
startupmigrations machinery around.

Since the relevant startupmigrations have been moved over to upgrades,
and the two libraries use different methods for not running the same
migration twice, a 23.1 node that comes up in a 22.2 cluster will re-run
the several permanent upgrades in question, even though they had already
run as startupmigrations. This is OK since both startupmigrations and
upgrades are idempotent. None of the current permanent upgrades are too
expensive.

Closes https://github.com/cockroachdb/cockroach/issues/73813

Release note: None
Epic: None

Co-authored-by: Shiranka Miskin <shiranka@cockroachlabs.com>
Co-authored-by: Andrei Matei <andrei@cockroachlabs.com>

---
## [apollographql/apollo-server](https://github.com/apollographql/apollo-server)@[3fd7b5f261...](https://github.com/apollographql/apollo-server/commit/3fd7b5f26144a02e711037b7058a8471e9648bc8)
#### Monday 2022-11-28 17:18:29 by Trevor Scheer

Update `@apollo/utils.keyvaluecache` dependency (#7187)

Previous releases of the `@apollo/utils.keyvaluecache` package
improperly specified the version range for its `lru-cache` dependency.

Fresh installs of our packages should receive the patch update since
it's careted, so this issue can be worked around by forcing the update
if you're using a lockfile. We should update it anyway since `2.0.0` is
invalid.

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

---
## [airplanedev/lib](https://github.com/airplanedev/lib)@[a5978d8afe...](https://github.com/airplanedev/lib/commit/a5978d8afeee4652692dd3f3c2d2f39e369d64db)
#### Monday 2022-11-28 17:18:55 by Lee Weisberger

Send env vars when creating deployment (#411)

## Description
In bundle discovery, send env vars along with the bundles. Env vars are calculated from `airplane.yaml` and the task definition.

The original plan here was to calculate these in the bundler. However env vars contain secret values that must be resolved. I don't think we should do this in the bundler because we'd have to expose an endpoint to resolve secret values and the bundler doesn't have any sort of advanced authn. Let me know if you have any other thoughts here, or else we'll just send these with the bundle.

## Test plan
I wrote a unit tests

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[0ca2c0b527...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/0ca2c0b527a564de32818057b7fc09eb07875f51)
#### Monday 2022-11-28 17:22:21 by SkyratBot

[MIRROR] Gives bread and cake slice_types and adds screentip verbs to proccessed foods [MDB IGNORE] (#17721)

* Gives bread and cake slice_types and adds screentip verbs to proccessed foods (#71449)

## About The Pull Request

A side effect of my pizza PR #71202 I added contextual screentips as
part of processable.dm. In doing this, I noticed that with a few
exceptions, almost every single bread and cake type copies the proc
exactly the same for every single child of cake or bread, so I put the
proc on the parent of bread and cake and gave them slice_types, making
them more similar to pizza.dm

For everything else I've changed the default that I put in
processable.dm into "slice" or "cut" for things that use the knife and
"flatten" for things that use the rolling pin.

Finally, you can slice bread with saws now, because I think its silly
that only pizza gets this luxury.

## Why It's Good For The Game

Because it wasnt the focus of #71202 I didn't mess with screentips
outside of the pizza file a lot, but now that it's merged I figure I
should go and do that.
As Bread and Cake's processables are almost fully standardized it seems
silly for them to call on the proc 12 times in the same document so I
did this, which also allows for more versatility in editing how they
work as well allow people to, if they want to, add more tool behaviours
in the future without adding in 12 lines of code. Also means that people
who want to add new cake or bread have one less thing to do.

## Changelog

:cl:
add: you can saw bread with a saw into bread slices
qol: added screentip verbs to a bunch of food files
code: bread and cake now have slice types and all only have one call on
the processable.dm proc
/:cl:

* Gives bread and cake slice_types and adds screentip verbs to proccessed foods

* sco'ish

* fuck me ig

Co-authored-by: Sol N <116288367+flowercuco@users.noreply.github.com>
Co-authored-by: John Doe <gamingskeleton3@gmail.com>

---
## [Ryzen5950XT/android_device_samsung_a52q](https://github.com/Ryzen5950XT/android_device_samsung_a52q)@[02cff7580d...](https://github.com/Ryzen5950XT/android_device_samsung_a52q/commit/02cff7580d103b929667998d291c9b5f55b2527b)
#### Monday 2022-11-28 17:52:46 by Ruchit Marathe

a52q: Switch to prebuilt kernel

honestly cant be asked to fucking fix this shit only for evox so yeah.

---
## [algoz098/zigbee2mqtt.io](https://github.com/algoz098/zigbee2mqtt.io)@[f687c12435...](https://github.com/algoz098/zigbee2mqtt.io/commit/f687c12435c958716d98c37fcce3fccfd75883da)
#### Monday 2022-11-28 18:17:00 by Artur Sena

Update README.md

Hey guys, so, i want to share a problem i had for a couple of months, and manage to solve.

It prob has happens to other ppl, and prob, at least a couple of those, still have, or never manage to solve.

If the wrong place, sorry, but i think this should be in the FAQ, even it's not the most common problem.

So, i have a setup with a good router stick, home assistant, and zigbee2mqtt addon.

The problem: some devices was not updating it's status, or desyncing from the network, also, was unable to add new devices. Map, was not being generate prob and timeout was happening without a clue or reason.

I started asking for help, changing the router stick, and without luck, it just ignored because it was kinda working almost all the times.

One day i decide to modify a door sensor, and for such, i needed it to connect to the network to test, it was unable to do so.

I started zigbee2mqtt in a new computer, though docker, and it worked FLAWLESS, after a while, i try to move all the devices to such new device.

Everything working perfect. Doubled the size of the network, no problem.
Add more automations, no problem.

The reason of such strange behaiviour was my raspberry pi model 3+, because it just have 1gb memory or maybe the processor, but, the problem was the limitations of the platform.

The reason for using such a limited board, is, the model 4 is expensive where i live, and i never had such problems. It started without warning.

So, i would like to add such information to the FAQ of Zigbee2mqtt, for more people now that you need a little room of memory and processor to avoid timeouts.

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[460ab7adf5...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/460ab7adf560856148d46233e3cde565d05354a4)
#### Monday 2022-11-28 19:20:19 by SkyratBot

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
## [mkolodezny/cadence-client](https://github.com/mkolodezny/cadence-client)@[f5e0fd25e4...](https://github.com/mkolodezny/cadence-client/commit/f5e0fd25e4347c85b28dac87f51b532700455d2c)
#### Monday 2022-11-28 21:38:09 by Steven L

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
## [tralezab/tgstation](https://github.com/tralezab/tgstation)@[b77cf7c120...](https://github.com/tralezab/tgstation/commit/b77cf7c1205d466b8cb242cd3302891e82b44da2)
#### Monday 2022-11-28 23:14:32 by Iamgoofball

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
## [TheTimeSweeper/the](https://github.com/TheTimeSweeper/the)@[2fc37f5c37...](https://github.com/TheTimeSweeper/the/commit/2fc37f5c37d7d2cda73ce828796c7a126dbfa6d5)
#### Monday 2022-11-28 23:35:40 by TheTimeSweeper

whole hell of a lot of balance tweaking god damn it
saving before I fuck something up again

---
## [Jolly-66/JollyStation](https://github.com/Jolly-66/JollyStation)@[d27bbf8fe7...](https://github.com/Jolly-66/JollyStation/commit/d27bbf8fe7154af2184fd275814a9369167857b6)
#### Monday 2022-11-28 23:57:33 by Jolly

this is the most hacky way to do shit you have no fucking idea man (#3379)

---

