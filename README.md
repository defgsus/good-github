## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-03-25](docs/good-messages/2022/2022-03-25.md)


1,809,382 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,809,382 were push events containing 2,844,360 commit messages that amount to 200,488,648 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 35 messages:


## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[55336d1e53...](https://github.com/tgstation/tgstation/commit/55336d1e5308789be1616413c8d8f87e073f7302)
#### Friday 2022-03-25 00:02:35 by vincentiusvin

Atmos Control Console Refactor (and syndiebase atmos tidyup) (#65372)

Main Takeaways For Mappers:

Use monitored pathed atmos devices very carefully. Also dont put atmos_sensors willy nilly. They are used to hook to atmos control monitors.

We want to keep at most one device broadcasting for each of the atmos sensor, inlets, and outlets. Run the mapping verb Check Atmos Chamber Devices to be sure, though this might not catch everything.

Some of the warning are pretty harmless. For example if you have reconnected the "station atmos monitor" and you get no listener for distro/waste loop warning, it's safe to ignore.

I don't know what the maptainer policy is on making new subtypes for offstation content, but if you do please branch off the general ones instead of the specific gas ones. If you aren't making a new subtype, varedit the general ones too.

About The Pull Request:

Need Would prefer this to be merged before #65271 (In game atmos guide).
Not strictly necessary, just makes me sleep better knowing the handbook wont die alongside the rest of the UI.

Fixes #36668 (Atmos Monitoring Consoles don't update it's sensors to the new tank after reconnect())
Fixes #32122 (Mix console fucked after reconnecting it)

Also made the distro meter thing broadcast more info instead of just the pressure, because I'm sure nobody would care and it would make my life easier.

A small high-level overview in case this breaks again in the future:

A signal datum (not DCS) is sent by the atmospheric devices (injectors and vents) and will be received by the atmos computers. The data is then stored at the monitor object and then passed to the UI. This initial signal is sent by `broadcast_signal()`, called by `atmos_init()`.

New sensors/vents (if you can actually get them in game, still only adminspawn/wrenchables afaik) will also initiate the conversation if atmos_init() is called, so it works fine. This means you need to unwrench and re-wrench the devices if you adminspawn them though, ugh.

In case of a newly built computer, it needs to be the one that prompt the data to the devices, so we send a request signal. This is a bit inefficient since it doesnt work off of callbacks and assocs like DCS, but won't really matter since we're doing this rarely.

We only talk with the injectors and vents when necessary here, while sensors and meters keep beeping with every process_atmos() tick so they rarely break.


Why It's Good For The Game:

Messy code gone (debatable).


Refactored the atmos control console devices. The ones that hook to the big turf chambers.
Distro meter now broadcast the whole gasmix info instead of just pressure to the monitors.
Lavaland syndie's atmos chamber vents are now actually configurable. Moved a few things around to accomodate this.
Lavalannd syndie chambers hooked to distro and moved distro pipe to layer2
atmos monitors can detect reactions now.
Some minor code changes to how anomaly refinery and implosion compressor show the gas info. No changes expected, report if bug.
recoded checks for atmos chamber abnormalities in debug verbs.

---
## [Urumasi/flesh-station](https://github.com/Urumasi/flesh-station)@[dd747fcc5a...](https://github.com/Urumasi/flesh-station/commit/dd747fcc5a46df051a5fe0e42950c46c72269244)
#### Friday 2022-03-25 00:31:15 by MrMelbert

BIDDLE HERETICS: Heretic revamp! (Shadow Realm, UI Overhaul, Refactoring, and Murderhoboing Tweaks)  (#64658)

About The Pull Request

This PR seeks to revamp heretic in it's almost entirety.

Closes #58435
Closes #62114
Closes #63605

image
Gameplay changes:

    The heretic no longer starts with a Codex Cicatrix or a Living Heart.
        Heretics now draw transmutation runes by using any writing tool while having Mansus Grasp active.
            The Mansus Grasp can be used to remove heretic runes.
        Draining influences can be done with "right click".
            While draining, people who examine you may get a message hinting that you're interacting with an influence.
            Drained influences can also be dispersed with anomaly neutralizers!
        The Codex Cicatrix is now a researchable item that lets you gain additional knowledge from influences.
            The Codex can still draw and remove runes, and does it faster.
        The Living Heart is now the heretic's heart. Literally. It's the heart in their chest. Their heart takes on the appearance of a living heart, and they can pulse it on demand to track their targets. This makes an audible noise.
            If your heart is lost (you're disemboweled or whatever), you need to do a ritual to regain it!

    Casting any heretic spell (besides Grasp) requires a Focus.
        A Heretic Focus is a neck item they can transmute.
        Heretic robes also function as a focus when toggled up.
        Ascending also disables the need for a focus, because of course.

    Heretics now gain 1 knowledge point passively every 20 minutes.

    Sacrificing has been revamped entirely.
        A heretic now gains four sacrifice targets on spawn.
            One random crewmember
            One member of their department
            One member of security
            One member of command (a "high value" sacrifice)
        You can sacrifice people who are in in soft-crit, hard-crit, or dead.
        Sacrificing someone will cuff them (if they are not), HEAL them, revive them, and set them unconscious. After a short time. they will be sent to a shadow realm. This shadow realm is themed to your heretic type.
            The shadow realm is a 2 minute long survival challenge where the sacrificee is subject to a constant barrage of shadowy hands.
            If they survive, they are teleported back to a random turf with no memory of how they got there. They'll also slur a TON to get the point across.
            If they die, their corpse is teleported back to a random turf on the station.

    No more multi-hearting! Your targets are your own.
        BUT adds a knowledge that allows heretics to reroll their sacrifice targets with a ritual.

    Each path now has a "Rituals of Knowledge". These are randomly generated rituals that may be difficult to complete but awards knowledge points in return.

    Ascending now has some requirements.
        To learn the ascension ritual, you need to complete all of the objective you are assigned.
        The ascension ritual now each have a varied requirement, instead of "needing 3 bodies" only.

    Other minor gameplay changes:
        Lots of balance tweaking.
            Buffed some summons.
            Buffed the Lord of the Night very slightly.
            Nerfed the Madness Mask.
        Put a limit on the amount of blade transmutations possible at once. 3 for flesh, 2 for other paths.
        Logs of BUG fixing.
        Rust Grasp is now based on right click for surfaces instead of combat mode.
        General grammar and flavor tweaks a ll around.

Admin / code changes:

    Revamped the way heretics appear within the traitor panel.
        You can now easily see who they're targeting for sacrifice and what they have researched
        Also adds some helpful buttons to heretics, like giving them points!
    Refactored much, much of heretic code
        LIKE ALL OF HERETIC CODE WAS IN 4 FILES.
            Split up all the knowledge, spells, and items that belong to the heretic into their own files and folders.
        Not only that, but everything internally was still named "Eldritch Cultist" and similar.
            Almost every mention of "Eldritch Cultist" has been properly replaced by "Heretic".
    Much better reference handling all around.
    General code improvements over heretic stuff.
    Unit tests, because of course.

Todo

Sprites for the focus

    Look at adding 1-2 other objectives prior to ascension. Theft? Special rituals? ("Rust [x] tiles to be able to ascend")

Why It's Good For The Game
Okay but why?

Heretics are not in a good place at the moment, this much is clear. They've been completely disabled on MRP for this reason.

The reasoning is simple: A lot of murder.
There's nothing inherently wrong with an antagonist heavy with murder, but the Heretic really missed the mark.
Gib, gib, gib, then ascend so you can keep killing.

In the background, the Heretic was FULL of flavorful spells, rituals, and "lore" stolen from Cultist Simulator that was unfortunate enough to be shackled to the heretic's gameplay loop.

So, this revamp aims to amend that:

Dial back the heretic's focus on mass murder and put more focus on the heretic's interesting flavor.
Spooky maintenance rituals, knowledge seeking maniac.

    Sacrifice no longer outright kills / requires murder, meaning a heretic can progress without racking up a bodycount.
    Influence is gained passively over time, so they can spend influence on more interesting side paths.
    Side paths are required to progress to ascension, so they're encouraged to explore new things.

Ultimately, while there still may be a little way to go, this PR seeks to take a good leap in starting it.
Changelog

cl Melbert
add: Large scale heretic revamp!
expansion: The Codex Cicatrix is no longer a roundstart heretic item. Research is handled through their antag info UI. Rune drawing is done by using a writing tool with Mansus Grasp active in your offhand. The actual Codex is an unlockable ritual item now.
expansion: The Living Heart is no longer a roundstart heretic item - their actual heart now becomes their Living Heart, and it makes a sound when triggered. Losing your heart (being disemboweled) will require you to do a ritual to regain it.
expansion: The Hereic Antag UI has been overhauled, and now hosts much of their mechanics as well as providing some helpful tips for newer players.
expansion: Most heretic spells now require a focus to cast. All heretics can make a basic focus necklace, and some heretic equipment also functions as a focus. (Credit to Imaginos for the focus sprite!)
expansion: Heretics now passively gain +1 influence every 20 minutes.
expansion: Heretic sacrificing has been reworked. You can now sacrifice people who are in soft crit or weaker. Sacrificing someone heals them, cuffs them, and teleports them to the SHADOW REALM, where they must dodge a barrage of hands to survive. Survive long enough and you return without memory - die, and your body will be thrown back.
expansion: Heretics now have a few new rituals, including the Ritual of Knowledge, a randomly generated ritual that awards knowledge points.
expansion: Heretic ascension now has a few requirements - you must complete your objectives assigned to you prior to learning the final ritual, and all the final rituals have been changed a bit!
qol: Using the Heretic's Mansus Grasp on surfaces (EX: Rust Grasp) now works on right-click, instead of combat mode.
qol: Used heretic influences can now be removed with a Anomaly Neutralizers.
balance: Some heretic rituals are now limited in the amount they can make. You can only have up to 2 heretic blades crafted at once (3 if you are Path of Flesh).
balance: The Lord of the Night has been buffed to be a little scarier. Did you know the Lord of the Night can eat arms to regain body parts and heal?
balance: Buffed some heretic summons - mostly their health pools.
balance: Nerfed the heretic's Mask of Madness. It can no longer infinite stam-crit you.
balance: Nerfed the heretic's ash mark.
balance: Nerfed a bunch of on-hit-heretic-blade effects. Many effects only apply on mark detonation now: Void blade silence, flesh blade wounds, ash blade gasp cooldown refund.
fix: Fixed quite a few bugs and unintended behaviors with heretic code.
refactor: Refactored and improved much of Heretic code. Improved the file structure dramatically.
admin: The heretic's traitor panel has been beefed up a bit.
/cl

---
## [Emisse/space-station-14](https://github.com/Emisse/space-station-14)@[cc49ed56d7...](https://github.com/Emisse/space-station-14/commit/cc49ed56d7109fe4ce98afa616b9caf91d5c24b1)
#### Friday 2022-03-25 03:20:26 by Emisse

Merge branch 'space-wizards:master' into shitty-ass-branch-annoying

---
## [dvsdude2/doom](https://github.com/dvsdude2/doom)@[35fba9ba1e...](https://github.com/dvsdude2/doom/commit/35fba9ba1e7e8869593dc6da60b2e27f2b9d4867)
#### Friday 2022-03-25 04:09:15 by dvsdude2

the next installment of this is my config

@@ -100,8 +100,8 @@
changed this because its annoying in elfeed.
messes up the windows text in elfeed. changed to text mode instead
fixed the problem

@@ -689,7 +689,7 @@
this I just noticed, has been wrong since it inception.
the prefix is most all toggles so fixed this.

@@ -726,7 +726,7 @@
here i've decided to move some of these personal files out of .emacs.d
to .doom.d this way they are under vc and can be replaced if needed.
or kept updated. will move them as I come across them.

@@ -749,16 +749,36 @@
sorry you had to see this! It's a fuckin mess right now.
this is me trying to figure out why none of the bindings don't work
still right in the middle of mucking about.
would seem to me it has to do with the mode, in org mode doesn't seem
to recognize spray mode ...ergo no binding .....this is what i'm trying
to deduce. only a theory right now. will figget with it again.
brings me to this point.... I find just throwing what I want to try
right in the config and mess with it there. not sure what advantage
I get by doing the same in separate buffer and just evaluate it from
there. have tried it and ya ..... it worked. But once I had it I would
still have to transfer it over and do a whole save restart anyways.
probably just me and my old ways. (did this for everything else)

@@ -815,6 +835,10 @@
this was something I noticed this in some configs online.
mainly had the problem myself...telling emacs to play a file rather than
edit. this I thought there must be a default way to do this but no I
could not see one and seen this in configs though this must be it...
seem overkill for something most programs do by default..but what ev's
but before I did all of that I thought to look deeper first and it was
not looking like a default way ...it looked as if it's not maintained
and old. reports of bugs,somelinks were dead or moved. not many stars.
after all that decided to not bother and find a work around which I did.
just use mpv-play it would open it and you can controle with org-doc
so no need for this after all will delete soon. sloppy wasn't ready for
picture, kinda decided just to do it.

@@ -930,7 +954,45 @@
had to add these....figured I would didn't make sense why he'd put them
there if they were not needed.live and learn.

@@ -993,14 +1055,25 @@
this is I found in my searching, like I had said before I use to use
a fzf in the terminal to watch videos with out downloading so this
made sense. it is modified youtube dl. only thing is lbry links
don't work so thats ok that is odysee is for. it appears he just sends
mpv to open the url and mpv takes care of the rest. need a protocol
thou. still good. as of now I have many ways of dealing with video
or any other file or url in my elfeed. lots of options that a bonus.

@@ -1009,17 +1082,46 @@
this is what I said earlier. lots of option when dealing with my feeds.
here I add two more eww(emacs web wowser) and w3m. both are new to me.
but should be able to incorporate spay with one or both not sure.
still learning. but that is why spray is being worked on right now.
after getting all this ready and working it's then i notice sprays
keys don't work and I'm not sure why... so lots going on all over at
once. elfeeds turning into a huge beast, was only two lines before. Now?

@@ -1051,3 +1153,17 @@
this is the other part of the elfeed upgrade. the w3m which needed a
package. still trying this so not much can be said about it.
but the big deal is I got all three of these to work. well done.
plus learned some more just going through the process. and it worked!
that should do it for now

---
## [yammyshep/dockerbuildtest](https://github.com/yammyshep/dockerbuildtest)@[91d103e858...](https://github.com/yammyshep/dockerbuildtest/commit/91d103e85854180b0324366d69729918973139d7)
#### Friday 2022-03-25 05:36:06 by YammyShep

holy fucking shit i am loosing my fucking mind can you stop being such a massive steaming hot piece of shit, node.js?

---
## [stamp-protocol/core](https://github.com/stamp-protocol/core)@[e755b6a7c1...](https://github.com/stamp-protocol/core/commit/e755b6a7c109b354b518f6c2663bddfea9075ecc)
#### Friday 2022-03-25 05:58:49 by Andrew Danger Lyon

replacing sodox::sign::* with ed25519-dalek

not super happy about this, because the two are NOT compatible, either
in key generation from seed or even in valid signature results (sigs
from sodox are "invalid" in ed25519-dalek for some godforsaken reason).

basically, this means all existing identities are completely invalid and
need to be regenerated, which sucks because i have to rebuild the Zephy
ID in the stamp doc (lol).

also, had to update a shit ton of tests and fix some serialization junk.
also, implementing rand_chacha20 since i thought it would make the
derive-from-seed signing keys line up. nope. oh well, at least it's more
secure than the StdRnd or w/e the hell it's called.

---
## [AlexandrBasan/jekyll-theme-memoirs](https://github.com/AlexandrBasan/jekyll-theme-memoirs)@[fdfc55b88c...](https://github.com/AlexandrBasan/jekyll-theme-memoirs/commit/fdfc55b88c33a1d1bc10bb017a8127ac811580e7)
#### Friday 2022-03-25 06:06:56 by Alexandr Basan

Create 2022-03-24-russia-warship-go-fuck-yourself.md

---
## [tbg/cockroach](https://github.com/tbg/cockroach)@[255c1fb027...](https://github.com/tbg/cockroach/commit/255c1fb02708f99fef62b0af719af5e0984d9de3)
#### Friday 2022-03-25 07:49:41 by craig[bot]

Merge #71542 #73319 #74077 #76401 #76748

71542: backupccl: Support RESTORE SYSTEM USERS from a backup r=gh-casper a=gh-casper

Support a new variant of RESTORE that recreates system users that don't exist in current cluster from a backup that contains system.users and also grant roles for these users. Example invocation: RESTORE SYSTEM USERS FROM 'nodelocal://foo/1';

Similar with full cluster restore, we firstly restore a temp system database which contains system.users and system.role_members into the restoring cluster and insert users and roles into the current system table from the temp system table.

Fixes: #45358

Release note (sql change): A special flavor of RESTORE, RESTORE SYSTEM USERS FROM ..., is added to support restoring system users from a backup. When executed, the statement recreates those users which are in a backup of system.users but do not currently exist (ignoring those who do) and re-grant roles for users if the backup contains system.role_members.

73319: jobs: Execute scheduled jobs on a single node in the cluster. r=miretskiy a=miretskiy

Execute scheduled jobs daemon on a single node -- namely, the lease
holder for meta1 range lease holder.

Prior to this change, scheduling daemon was running on each node,
polling scheduled jobs table periodically with a `FOR UPDATE` clause.
Unfortunately, job planning phase (namely, the backup planning phase) could
take significant amount of time.  In such situation, the entirety
of the scheduled jobs table would be locked, resulting in inability
to introspect the state of schedules (or jobs) via `SHOW SCHEDULES` or similar
statements.

Furthermore, dropping `FOR UPDATE` clause by itself is not ideal because
that would lead to expensive backup planning being executed on almost every
node, with all but 1 node making progress.

The single node mode is disabled by default, but can be enabled
via a `jobs.scheduler.single_node_scheduler.enabled` setting.

Release Notes: scheduled jobs scheduler now runs on a single node by default
in order to reduce contention on scheduled jobs table.

74077: kvserver: lease transfer in JOINT configuration r=shralex a=shralex

Previously:
1. Removing a leaseholder was not allowed.
2. A VOTER_INCOMING node wasn't able to accept the lease.

Because of (1), users needed to transfer the lease before removing
the leaseholder. Because of (2), when relocating a range from the
leaseholder A to a new node B, there was no possibility to transfer
the lease to B before it was fully added as VOTER. Adding it as a
voter, however, could degrade fault tolerance. For example, if A
and B are in region R1, C in region R2 and D in R3, and we had
(A, C, D), and now adding B to the cluster to replace A results in
the intermediate configuration (A, B, C, D) the failure of R1 would
make the cluster unavailable since no quorum can be established.
Since B can't be added before A is removed, the system would
transfer the lease out to C, remove A and add B, and then transfer
the lease again to B. This resulted a temporary migration of leases
out of their preferred region, imbalance of lease count and degraded
performance.

The PR fixes this, by (1) allowing removing the leaseholder, and
transferring the lease right before we exit the JOINT config. And (2),
allowing a VOTER_INCOMING to accept the lease.

Release note (performance improvement): Fixes a limitation which meant 
that, upon adding a new node to the cluster, lease counts among existing
nodes could diverge until the new node was fully upreplicated.

Here are a few experiments that demonstrate the benefit of the feature.
1. 
> roachprod create local -n 4 // if not already created and staged
> roachprod put local cockroach
> roachprod start local:1-3 --racks=3 // add 3 servers in 3 different racks
> cockroach workload init kv --splits=10000
> roachprod start local:4 --racks=3 // add a 4th server in one of the racks

Without the change (master):
<img width="978" alt="Screen Shot 2022-02-09 at 8 35 35 AM" src="https://user-images.githubusercontent.com/6037719/153458966-609dbb7e-ca3d-4db6-9cfb-adc228f2bdf2.png">

With the change:
<img width="986" alt="Screen Shot 2022-02-08 at 8 46 41 PM" src="https://user-images.githubusercontent.com/6037719/153459366-2d4e2def-37cf-405b-b601-8be57419ae02.png">

We can see that without the patch the number of leases on server 0 (black line) goes all the way to 0 before it goes back up and that the number of leases in other racks goes up, both undesirable. With the patch both things are no longer happening.

2. Same as 1, but with a leaseholder preference of rack 0:

ALTER RANGE default CONFIGURE ZONE USING lease_preferences='[[+rack=0]]';

Without the change (master):
<img width="966" alt="Screen Shot 2022-02-09 at 10 45 27 PM" src="https://user-images.githubusercontent.com/6037719/153460753-bce048f0-f6da-4e21-afdc-317620c035b2.png">

With the change:
<img width="983" alt="leaseholder preferences - with change" src="https://user-images.githubusercontent.com/6037719/153460780-55795866-cf47-404d-b77a-45d9e011f972.png">

We can see that without the change the number of leaseholders in racks 1 and 2 together (not in preferred region) grows from 300 to 1000, then goes back to 40. With the fix it doesn’t grow at all.






76401: pgwire: add server.max_connections public cluster setting r=rafiss a=ecwall

This setting specifies a maximum number of connections that a server can have open at any given time.
<0 - Connections are unlimited (existing behavior)
=0 - Connections are disabled
>0 - Connections are limited
If a new non-superuser connection would exceed this limit, the same error message is
returned as postgres: "sorry, too many connections" with the 53300 error code
that corresponds to "too many connections".

Release note (ops change): An off-by-default server.max_connections cluster
setting has been added to limit the maximum number of connections to a server.

76748: sql: add missing specs to plan diagrams r=rharding6373 a=rharding6373

This change allows missing specs (e.g., RestoreDataSpec and
SplitAndScatterSpec) to be shown in plan diagrams. Before this change a
plan involving these types would result in an error generating the
diagrams. Also added a test to make sure future specs implement the
`diagramCellType` interface, which is required to generate diagrams.

Release note: None


Co-authored-by: Casper <casper@cockroachlabs.com>
Co-authored-by: Yevgeniy Miretskiy <yevgeniy@cockroachlabs.com>
Co-authored-by: shralex <shralex@gmail.com>
Co-authored-by: Evan Wall <wall@cockroachlabs.com>
Co-authored-by: rharding6373 <rharding6373@users.noreply.github.com>

---
## [JuliaLang/julia](https://github.com/JuliaLang/julia)@[b5ca35b08e...](https://github.com/JuliaLang/julia/commit/b5ca35b08e717a857974ea5ea9d2887a5ae0348b)
#### Friday 2022-03-25 08:20:30 by Mirek Kratochvil

avoid using `@sync_add` on remotecalls (#44671)

* avoid using `@sync_add` on remotecalls

It seems like @sync_add adds the Futures to a queue (Channel) for @sync, which
in turn calls wait() for all the futures synchronously. Not only that is
slightly detrimental for network operations (latencies add up), but in case of
Distributed the call to wait() may actually cause some compilation on remote
processes, which is also wait()ed for. In result, some operations took a great
amount of "serial" processing time if executed on many workers at once.

For me, this closes #44645.

The major change can be illustrated as follows: First add some workers:

```
using Distributed
addprocs(10)
```

and then trigger something that, for example, causes package imports on the
workers:

```
using SomeTinyPackage
```

In my case (importing UnicodePlots on 10 workers), this improves the loading
time over 10 workers from ~11s to ~5.5s.

This is a far bigger issue when worker count gets high. The time of the
processing on each worker is usually around 0.3s, so triggering this problem
even on a relatively small cluster (64 workers) causes a really annoying delay,
and running `@everywhere` for the first time on reasonable clusters (I tested
with 1024 workers, see #44645) usually takes more than 5 minutes. Which sucks.

Anyway, on 64 workers this reduces the "first import" time from ~30s to ~6s,
and on 1024 workers this seems to reduce the time from over 5 minutes (I didn't
bother to measure that precisely now, sorry) to ~11s.

Related issues:
- Probably fixes #39291.
- #42156 is a kinda complementary -- it removes the most painful source of
  slowness (the 0.3s precompilation on the workers), but the fact that the
  wait()ing is serial remains a problem if the network latencies are high.

May help with #38931

Co-authored-by: Valentin Churavy <vchuravy@users.noreply.github.com>
(cherry picked from commit 62e0729dbc5f9d5d93d14dcd49457f02a0c6d3a7)

---
## [KingmiguelAguilar/KingmiguelAguilar](https://github.com/KingmiguelAguilar/KingmiguelAguilar)@[0fe7c04d8a...](https://github.com/KingmiguelAguilar/KingmiguelAguilar/commit/0fe7c04d8af71dd9ff18e9a540f35d5348da9257)
#### Friday 2022-03-25 08:35:26 by KingmiguelAguilar

Create README.md

In females 
More about females 
With females 
With females.      / jk Im the chosen guys and i really need your smartness. Help on the days to come and if tbe government tries tell you and you work for me just don't do nothing corrupt or steal from me cause god is watching over me im here cause i got a copy right of what im trying to accomplish first Im building Real talk social media app buy i want mine live 3d background and letters to slide not the background the best is yet to come

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[bb933bf7f1...](https://github.com/treckstar/yolo-octo-hipster/commit/bb933bf7f1205d74cdff875fd9fdeb24d257261b)
#### Friday 2022-03-25 08:45:04 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [ondrejbudai/osbuild-composer](https://github.com/ondrejbudai/osbuild-composer)@[38bf61f8ec...](https://github.com/ondrejbudai/osbuild-composer/commit/38bf61f8ec862ad01c3f131360aa46ddb26fa79f)
#### Friday 2022-03-25 09:07:58 by Ondřej Budai

cloudapi: rename gpg_key field to gpgkey

Oh no, we made a mistake here: Both our json repositories and repo files in
/etc/yum.repos.d have the GPG key in a field named `gpgkey`. Unfortunately,
cloudapi uses a field named `gpg_key`. One consequence of this issue is that
our api.sh test is meant to pass GPG keys in the compose request but since
it's using a bad field name (`gpgkey`), the key is actually not used.

I've decided to fix this in cloudapi: The `gpg_key` field is now renamed to
`gpgkey`. This is a breaking change but no one is using this API anyway so
we think it's better to do this now than introducing weird backward
compatible hacks.

Signed-off-by: Ondřej Budai <ondrej@budai.cz>

---
## [josephlee222/terminal](https://github.com/josephlee222/terminal)@[855e1360c0...](https://github.com/josephlee222/terminal/commit/855e1360c0ff810decf862f1d90e15b5f49e7bbd)
#### Friday 2022-03-25 09:10:29 by Mike Griese

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

---
## [arjunrn/api](https://github.com/arjunrn/api)@[5b82635ef1...](https://github.com/arjunrn/api/commit/5b82635ef101e7c10b5fcbbcfb81315bb7a0da20)
#### Friday 2022-03-25 09:22:38 by W. Trevor King

config/v1/types_cluster_version: Add capabilties properties

Roughly as described in [enhancement].  After discussion with Ben and
David, we've made the following changes:

# spec

## capabilities

The [enhancement] didn't have an opinion on whether or not this should
be a pointer.  I've gone with pointer, because I'm fine allowing folks
to leave this unset.  The docs for this pointer property point out
that there's no distinction between nil (Go, or for JSON, null) and an
empty object (&ClusterVersionCapabilitiesSpec{} in Go, {} in JSON), so
we don't have to rehash all the ClusterVersionCapabilitiesSpec
children defaults here, where they'd likely go stale as folks update
defaults within ClusterVersionCapabilitiesSpec or add new child
properties.

### baselineCapabilitySet

David prefered this name to the [enhancement]'s inclusionDefault, and
Ben and I are fine with that name.

David also prefered None to Exclude and vCurrent to Include, with
additional values like v4.11 for "give me the 4.11 stuff, but not new
4.12 stuff, until I have time to look that over after I update to
4.12".  That seems overly complicated to me, and also like we coulld
add v4.11 later if folks felt None and vCurrent weren't convenient
enough, but David wanted v4.11 out of the gate.  We can always see how
it plays out in production, and we can stop adding new v4.y forms if
they aren't popular enough to be worth maintaining.  There's an enum
type to make it easy to validate, and hard to typo, these values.

There's also a map, so consumers like the cluster-version operator who
vendor the API repository can get the API-maintainer-intended
capability membership for each set, now that those semantics are more
complicated than all or nothing.

There were a few ways we could have taken the property default here:

a. Explicit +kubebuilder:default:=... .  No option for folks to sit on
   the fence, or to adjust existing clusters later without the admin's
   explicit buy-in.  But no ambiguity about what happens if the user
   has no opinion.

b. omitempty, and docs for "we'll pick a sane default if you don't
   care", that don't commit to a specific default.  Great for when we
   decide to change our default preference, because we don't need to
   hunt down buy-in from admins that have deferred to us.  Not great
   for folks who are mildly curious about our current choice, but who
   still trust us to evolve the default (I think this set is nearly
   empty).

c. omitempty, and docs for "the current default is A, but who knows
   tomorrow".  Effectively (b), but also gives folks some information
   that's not actionable which can go stale as soon as they close
   their eyes.

(a) makes sense if we are confident we will never want to change our
default, and that seems plausible in this case.  (b) makes sense when
we think we might change our default, and I'm fine with that in this
case too.  I don't really understand the use case for (c), but as
David points out, even if we do change the default, we don't expect to
change it often, so maybe my personal take is off and there are a
bunch of folks who are mildly curious about our current choice, but
who still trust us to evolve the default.  Anyhow, David's the
approver, so we're going with (c).

### additionalEnabledCapabilities

David prefered this name to the [enhancement]'s inclusionDefault, and
Ben and I are fine with that name.

In the [enhancement], Ben had intended to distribute the ability to
create new capabilities to all manifest-providing repositories, simply
by declaring the capability.openshift.io/name annotation.  David was
worried about validation, and also possibly about insufficiently
scoped names between separate teams, so this pull request declares a
central enum where API maintainers can review and approve new
capability names, and work them into the appropriate entries in the
set maps.  The installer and cluster-version operator will have to
bump their vendored API version after each addition to pick up the new
changes, but new capability additions shouldn't be too frequent to
make that particularly painful.

### exclude

The [enhancement] also provided a way to drop specific capabilities
from the selected set (inclusionDefault or baselineCapabilitySet).
Ben still feels like that will be popular, but David is skeptical, and
because we can always add a property in this space later without
breaking backwards compatibility, we're leaving it off for now.

# status

## capabilities

The [enhancement] didn't have an opinion on whether or not this should
be a pointer.  I've gone with non-pointer, because we will always
declare at least some capabilities (e.g. knownCapabilities), so users
will be able to discover additional capabilities which they might want
to enable in their cluster.

### enabledCapabilities

David prefered this name to the [enhancement]'s include, and Ben's ok
with that name.  I'm not wild about 'Capabilities' in:

  status:
    capabilities:
      enabledCapabilities: ...

but David was committed, citing the example of:

  FeatureGateSelection.FeatureSet

Although FeatureGateSelection is consumed with less context:

  type FeatureGateSpec struct {
	FeatureGateSelection `json:",inline"`
  }

I'd pushed back against the stuttering in [stutterPrecedent], but
without success, and :shrug:, doesn't matter all that much if folks
have to type a few redundant characters to use this property.

### knownCapabilities

The [enhancement] had floated 'exclude'.  There are a few capability
sets in play for the status listings:

* A is the set of all caps.
* I is the set of included caps.
* E is the set of excluded caps.
* Each cap must be either included or excluded, so I and E are disjoint, and the union of I and E is A.

So you can take any two of those three sets and construct the one
you're missing:

* A = I ∪ E
* E = A - I
* I = A - E

If we have to pick two to include in status, picking I and E gives us
all the data we need, and saves a few bytes by excluding the largest,
which is A.  But David preferred picking I (as enabledCapabilities)
and A (as knownCapabilities) [knownCapabilities], so that's what we're
doing in this commit.

### inclusionDefault

The [enhancement] also provided a way to echo the spec set in an
inclusionDefault status property.  I've left that out of the status
structure, because I'm using explicit, exhaustive list for
enabledCapabilities and knownCapabilities there.  The exhaustive lists
will provide a convenient set (via A - I set subtraction) of "things
you don't have right now, but which you could choose to install right
now", so admins don't have to guess about their options there.  With
the exhaustive lists, reflecting the default setting didn't seem to
add much useful information.  And we can always add that property to
the status structure later if we do decide it would be useful.

## conditions

I have not created a constant with the status.conditions[] type that
will be used to declare "we are installing a capability you have not
asked for, because we don't support uninstalling capabilities, and
that one was tainted in via your cluster's history".  We can come back
and declare that constant later if we want, although that's somewhat
complicated by the fact that we use ClusterOperatorStatusCondition,
and the new condition type would not be something that makes sense for
ClusterOperator.

[enhancement]: https://github.com/openshift/enhancements/blob/88cb7438f3ac0a8121e3cef87cb144097ece8cda/enhancements/installer/component-selection.md
[knownCapabilities]: https://github.com/openshift/api/pull/1106#discussion_r799819632
[validation]: https://book.kubebuilder.io/reference/generating-crd.html#validation
[statusPropertyNames]: https://github.com/openshift/api/pull/1106#discussion_r799819632
[stutterPrecedent]: https://github.com/openshift/api/pull/1106#discussion_r799879689

---
## [laminas/laminas-cache](https://github.com/laminas/laminas-cache)@[1a6e688271...](https://github.com/laminas/laminas-cache/commit/1a6e688271793a0e3cd7eb43aec063526c931047)
#### Friday 2022-03-25 09:26:31 by Michał Bundyra

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
## [John-sanpe/lightcore](https://github.com/John-sanpe/lightcore)@[be120e4738...](https://github.com/John-sanpe/lightcore/commit/be120e473866325e41321a9548276378a48a7aca)
#### Friday 2022-03-25 10:40:10 by John-sanpe

Maintain: Fixed some minor problems with the global kernel

[cmpxchg] Change from macro processing to function processing
    -- Some strange strong convert errors are avoided,
        in short, gcc fuck you.

[pgalloc] Replace the x86 pgalloc to asm-generic
    -- The size of most page tables is fixed 4K, so we
        have a more general solution.

---
## [cloudify-cosmo/cloudify-common](https://github.com/cloudify-cosmo/cloudify-common)@[86cadd1f6e...](https://github.com/cloudify-cosmo/cloudify-common/commit/86cadd1f6e67e3263b5e6c4d9ed5522146910480)
#### Friday 2022-03-25 10:55:26 by Lukasz Maksymczuk

RD-4502 Hide useless tracebacks (incl. DSLParsingExc) (#1025)

* Remove disused .deployments_contexts

It was, a long time ago, used in snap-res. But now it's not. I've had
a mental note to remove it for like a year now, but now I'm going
to change stuff about `.start_local_tasks_processing`, so let's
just remove this, then.

* local_tasks_processing: use a `with` rather than try/finally

* workflow handler: only returh the original traceback

This is a small hack allowing us to only show the user the traceback
of their workflow function, without the several frames added by the
framework itself.

* RD-4502 Skip tracebacks for DSLParsingException

This error is already human-readable and formatted. For showing it
to the user, we can skip the traceback.

The .hide_traceback this is perhaps a bit dirty, but it's going to
be very useful! Soon, we can also consider hiding the tracebacks
of other exception kinds, eg. WorkflowFailed itself.

* flake

* reraise the exception `from None`

...actually using this stupid syntax.
Makes the output much better. Hides the parts where the exception was
in the _WorkflowFuncError state.

* Compat for local workflows

Also the mock needs to be a magicmock because `__enter__`

* Whoops. Better return before .get()ing all these

It was the case before, too. In case of an error, we don't want to
.get() all the tasks.

Now, I do recognize it's a bit unwieldy, not throwing, but returning.
Although it makes the traceback nicer, so oh well.

---
## [KhalidReda01/The-Complete-React-Developer-Course-w-Hooks-and-Redux-](https://github.com/KhalidReda01/The-Complete-React-Developer-Course-w-Hooks-and-Redux-)@[ebd542afc5...](https://github.com/KhalidReda01/The-Complete-React-Developer-Course-w-Hooks-and-Redux-/commit/ebd542afc5da303b410876dca0ddecbcf820b504)
#### Friday 2022-03-25 12:13:40 by khalidreda

OMG it was typo at the filters I wrote it fiters without l OMG but you discovere that good not bad at all keep going this is part of learning make mistake and solve it I mean this is your own  mistakes and  you learn better by this way Fuck time the real benefit for me is just really understand the code that I write

---
## [avar/git](https://github.com/avar/git)@[193534b0f0...](https://github.com/avar/git/commit/193534b0f079b5595efbfdc3febaa87910fae6a5)
#### Friday 2022-03-25 12:17:28 by Ævar Arnfjörð Bjarmason

pack-objects: lazily set up "struct rev_info", don't leak

In the preceding [1] (pack-objects: move revs out of
get_object_list(), 2022-03-22) the "repo_init_revisions()" was moved
to cmd_pack_objects() so that it unconditionally took place for all
invocations of "git pack-objects".

We'd thus start leaking memory, which is easily reproduced in
e.g. git.git by feeding e83c5163316 (Initial revision of "git", the
information manager from hell, 2005-04-07) to "git pack-objects";

    $ echo e83c5163316f89bfbde7d9ab23ca2e25604af290 | ./git pack-objects initial
    [...]
	==19130==ERROR: LeakSanitizer: detected memory leaks

	Direct leak of 7120 byte(s) in 1 object(s) allocated from:
	    #0 0x455308 in __interceptor_malloc (/home/avar/g/git/git+0x455308)
	    #1 0x75b399 in do_xmalloc /home/avar/g/git/wrapper.c:41:8
	    #2 0x75b356 in xmalloc /home/avar/g/git/wrapper.c:62:9
	    #3 0x5d7609 in prep_parse_options /home/avar/g/git/diff.c:5647:2
	    #4 0x5d415a in repo_diff_setup /home/avar/g/git/diff.c:4621:2
	    #5 0x6dffbb in repo_init_revisions /home/avar/g/git/revision.c:1853:2
	    #6 0x4f599d in cmd_pack_objects /home/avar/g/git/builtin/pack-objects.c:3980:2
	    #7 0x4592ca in run_builtin /home/avar/g/git/git.c:465:11
	    #8 0x457d81 in handle_builtin /home/avar/g/git/git.c:718:3
	    #9 0x458ca5 in run_argv /home/avar/g/git/git.c:785:4
	    #10 0x457b40 in cmd_main /home/avar/g/git/git.c:916:19
	    #11 0x562259 in main /home/avar/g/git/common-main.c:56:11
	    #12 0x7fce792ac7ec in __libc_start_main csu/../csu/libc-start.c:332:16
	    #13 0x4300f9 in _start (/home/avar/g/git/git+0x4300f9)

	SUMMARY: LeakSanitizer: 7120 byte(s) leaked in 1 allocation(s).
	Aborted

Narrowly fixing that commit would have been easy, just add call
repo_init_revisions() right before get_object_list(), which is
effectively what was done before that commit.

But an unstated constraint when setting it up early is that it was
needed for the subsequent [2] (pack-objects: parse --filter directly
into revs.filter, 2022-03-22), i.e. we might have a --filter
command-line option, and need to either have the "struct rev_info"
setup when we encounter that option, or later.

Let's just change the control flow so that we'll instead set up the
"struct rev_info" only when we need it. Doing so leads to a bit more
verbosity, but it's a lot clearer what we're doing and why.

We could furthermore combine the two get_object_list() invocations
here by having repo_init_revisions() invoked on &pfd.revs, but I think
clearly separating the two makes the flow clearer. Likewise
redundantly but explicitly (i.e. redundant v.s. a "{ 0 }") "0" to
"have_revs" early in cmd_pack_objects().

This does add the future constraint to opt_parse_list_objects_filter()
that we'll need to adjust this wrapper code if it looks at any other
value of the "struct option" than the "value" member.

But that regression should be relatively easy to spot. I'm
intentionally not initializing the "struct wrap" with e.g. "{ 0 }" so
that various memory sanity checkers would spot that, we just
initialize the "value" in po_filter_cb(). By doing this e.g. we'll die
on e.g. this test if we were to use another member of "opt" in
opt_parse_list_objects_filter()>

    ./t5317-pack-objects-filter-objects.sh -vixd --valgrind-only=3

While we're at it add parentheses around the arguments to the OPT_*
macros in in list-objects-filter-options.h, as we need to change those
lines anyway. It doesn't matter in this case, but is good general
practice.

1. https://lore.kernel.org/git/619b757d98465dbc4995bdc11a5282fbfcbd3daa.1647970119.git.gitgitgadget@gmail.com
2. https://lore.kernel.org/git/97de926904988b89b5663bd4c59c011a1723a8f5.1647970119.git.gitgitgadget@gmail.com/

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>

---
## [lime360/bucket-webring](https://github.com/lime360/bucket-webring)@[81fa1234d9...](https://github.com/lime360/bucket-webring/commit/81fa1234d9f99531f8d98d699249e4c00c4e819f)
#### Friday 2022-03-25 12:19:35 by rowan tobias

swiftyshq format fix

i was having errors fsr so i thought removing punctuation etc would fix it. We'll See! (sorry if you got notifs for my other prs that i deleted i was struggling.)

---
## [axietheaxolotl/Skyrat-tg](https://github.com/axietheaxolotl/Skyrat-tg)@[5c1e69aa44...](https://github.com/axietheaxolotl/Skyrat-tg/commit/5c1e69aa448e6e28738b4643a54bb104ee032555)
#### Friday 2022-03-25 12:36:28 by SkyratBot

[MIRROR] Fixes borg wallmounting [MDB IGNORE] (#12046)

* fixes wallmounts (#65408)

closes #65393 (Engineering Cyborgs can't place APC or Air alarm frames on walls anymore)
fixes the code error in #64428 (afc1e44ee2922a316feb958249f7806568953bbe)

basically what occured is that he typed out the T(turf) attackby proc to input the screwdriver as an arg rather then the wallmount, remember, you want the WALLMOUNT to hit the wall to place it, not the screwdriver, that just creates runtimes and doesnt place anything

EDIT: actually re-reading it, what it was actually doing was using the screwdriver as the user arg, and trying to smash the user into the wall, thats actually kinda funny

borgo wallmounting is a good thing, good borgos need their treats

* Fixes borg wallmounting

Co-authored-by: 小月猫 <alina.r.starkova@gmail.com>

---
## [near/nearcore](https://github.com/near/nearcore)@[6d8d6c607f...](https://github.com/near/nearcore/commit/6d8d6c607f81e6b1ea93d66bc8320603d410284a)
#### Friday 2022-03-25 12:36:33 by Simonas Kazlauskas

Use non-blocking log writer

This will utilize a separate thread to write out the spans and events
without while letting the main computation to proceed with its business.
Additionally, we are buffering the output by lines, thus reducing the
frequency of syscalls that can occur when the subscriber is writing out
parts of the message.

This should mitigate concerns of enabling debug logging as its impact on
performance should now be minimal (putting an event structure onto a
MPSC queue.) There are still costs associated with logging everything
however. Most notably formatting and construction of the
`tracing_core::ValueSet`s still occur on the caller side, so if
constructing those is expensive, the logging might remain expensive.
An example of code sketchy like that (although silly) could be:

```
debug!(message = { std::time::sleep(Duration::from_secs(1)); "hello" })
```

or for a less silly example:

```
debug!("{}", my_vector.iter().map(|...| {
  do_expensive_stuff()
}).collect::<String>())
```

These should be considered a bug (alas one that `tracing` does not have
any tooling to detect, sadly.)

I opted adding a new crate dedicated to observability utilities. From my
experience using things like prometheus will eventually result in a
variety of utilities being written, so this crate eventually would
likely expand in scope...

---
## [ammarfaizi2/linux-block](https://github.com/ammarfaizi2/linux-block)@[c570449094...](https://github.com/ammarfaizi2/linux-block/commit/c570449094844527577c5c914140222cb1893e3f)
#### Friday 2022-03-25 13:52:52 by Jason A. Donenfeld

random: use linear min-entropy accumulation crediting

30e37ec516ae ("random: account for entropy loss due to overwrites")
assumed that adding new entropy to the LFSR pool probabilistically
cancelled out old entropy there, so entropy was credited asymptotically,
approximating Shannon entropy of independent sources (rather than a
stronger min-entropy notion) using 1/8th fractional bits and replacing
a constant 2-2/√𝑒 term (~0.786938) with 3/4 (0.75) to slightly
underestimate it. This wasn't superb, but it was perhaps better than
nothing, so that's what was done. Which entropy specifically was being
cancelled out and how much precisely each time is hard to tell, though
as I showed with the attack code in my previous commit, a motivated
adversary with sufficient information can actually cancel out
everything.

Since we're no longer using an LFSR for entropy accumulation, this
probabilistic cancellation is no longer relevant. Rather, we're now
using a computational hash function as the accumulator and we've
switched to working in the random oracle model, from which we can now
revisit the question of min-entropy accumulation, which is done in
detail in <https://eprint.iacr.org/2019/198>.

Consider a long input bit string that is built by concatenating various
smaller independent input bit strings. Each one of these inputs has a
designated min-entropy, which is what we're passing to
credit_entropy_bits(h). When we pass the concatenation of these to a
random oracle, it means that an adversary trying to receive back the
same reply as us would need to become certain about each part of the
concatenated bit string we passed in, which means becoming certain about
all of those h values. That means we can estimate the accumulation by
simply adding up the h values in calls to credit_entropy_bits(h);
there's no probabilistic cancellation at play like there was said to be
for the LFSR. Incidentally, this is also what other entropy accumulators
based on computational hash functions do as well.

So this commit replaces credit_entropy_bits(h) with essentially `total =
min(POOL_BITS, total + h)`, done with a cmpxchg loop as before.

What if we're wrong and the above is nonsense? It's not, but let's
assume we don't want the actual _behavior_ of the code to change much.
Currently that behavior is not extracting from the input pool until it
has 128 bits of entropy in it. With the old algorithm, we'd hit that
magic 128 number after roughly 256 calls to credit_entropy_bits(1). So,
we can retain more or less the old behavior by waiting to extract from
the input pool until it hits 256 bits of entropy using the new code. For
people concerned about this change, it means that there's not that much
practical behavioral change. And for folks actually trying to model
the behavior rigorously, it means that we have an even higher margin
against attacks.

Cc: Theodore Ts'o <tytso@mit.edu>
Cc: Dominik Brodowski <linux@dominikbrodowski.net>
Cc: Greg Kroah-Hartman <gregkh@linuxfoundation.org>
Reviewed-by: Eric Biggers <ebiggers@google.com>
Reviewed-by: Jean-Philippe Aumasson <jeanphilippe.aumasson@gmail.com>
Signed-off-by: Jason A. Donenfeld <Jason@zx2c4.com>

---
## [WordPress/gutenberg](https://github.com/WordPress/gutenberg)@[3ea2d42b0a...](https://github.com/WordPress/gutenberg/commit/3ea2d42b0a6a206663735a47f9796bd42eda2186)
#### Friday 2022-03-25 15:21:05 by Dennis Snell

Blocks: Remember raw source block for invalid blocks. (#38923)

Part of #38922

When the editor is unable to validate a block it should preserve the
broken content in the post and show an accurate representation of that
underlying markup in the absence of being able to interact with it.

Currently when showing a preview of an invalid block in the editor we
attempt to re-generate the save output for a block given the attributes
we originally parsed. This is a flawed approach, however, because by
the nature of being invalid we know that there is a problem with those
attributes as they are.

In this patch we're introducing the `__unstableBlockSource` attribute on 
a block which only exists for invalid blocks at the time of this patch. That 
`__unstableBlockSource` carries the original un-processed data for a block
node and can be used to reconstruct the original markup without using
garbage data and without inadvertently changing it through the series
of autofixes, deprecations, and the like that happen during normal block loading.

The noticable change is in `block-list/block` where we will be showing
that reconstruction rather than the re-generated block content. Previously
it was the case that the preview might represent a corrupted version of the
block or show the block as if emptied of all its content. Now, however,
the preview sould accurately reflect the HTML in the source post even
when it's invalid or unrecognized according to the editor.

Further work should take advantage of the `__unstableBlockSource`
property to provide a more consistent and trusting experience for
working with unrecognized content.

---
## [Sedna-Games/Zero-Possession-Prototype](https://github.com/Sedna-Games/Zero-Possession-Prototype)@[64478f1022...](https://github.com/Sedna-Games/Zero-Possession-Prototype/commit/64478f1022ce8b50c3a832cdc3888462e3697b9d)
#### Friday 2022-03-25 15:36:07 by Hamraj

[WIP] More Buildings

- yeah still a long ass way to go but im faster at the shit now

---
## [msm-code/karton](https://github.com/msm-code/karton)@[fab6b0b41d...](https://github.com/msm-code/karton/commit/fab6b0b41d7645626533d013dd8af277bb15df74)
#### Friday 2022-03-25 15:39:14 by msm-code

Apply suggestions from code review

Ok, this is clearly my fault. My Github notifications are poorly configured, and I miss them all the time (and my e-mail client doesn't show images). I've also didn't apply the suggestions, even though I thought I did - I probably didn't commit the changes after batching them. My bad again.

On the other hand, after this issue was reported, I've stayed up late for two nights in a row, to help fix this in a timely manner. I clearly cared about getting this done quickly. And I've honestly thought these improvements were incorporated into the main branch a long time ago.

Dear maintainers: In the future, if a PR is waiting for me for an extended period of time, please ping me. Especially since we know and talk to each other all the time. Or apply the requested changes yourself - you know you're free to use my code any way you like (like @psrok1 took my #144 and improved it in #146).

Apologises for the rant. I feel pretty bummed by how it turned out.

On a more technical side, please see the first two sentences of the PR description. Some of this code can be refactored (with the `make_pipeline` function @psrok1 introduced in #146). I think the debug logs should also be removed. And if you decide to merge this PR as it is, I advise some correctness testing (since the changes are in a deep internals of Karton).

Co-authored-by: Michał Praszmo <nazywam@gmail.com>

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[2b6aded689...](https://github.com/treckstar/yolo-octo-hipster/commit/2b6aded6894225587814458e91f0932846c05a6f)
#### Friday 2022-03-25 17:00:04 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [alphagov/di-onboarding-product-page](https://github.com/alphagov/di-onboarding-product-page)@[5fdb8ac65d...](https://github.com/alphagov/di-onboarding-product-page/commit/5fdb8ac65d7e9077635a2a571c91ffe1617509aa)
#### Friday 2022-03-25 18:01:57 by John Watts

Two SAM configurations - one with a lambda that calls a lambda and another that gets called by a lambda.

Confused? It is confusing.  The real meat and bones is with the Roles and Policies (Trust Policy and Permissions Policies - because they're two different things).

You could use sam to build and deploy these to new stacks but you'd have to dig out the various outputs and paste them into the templates.  You'll see one has some parameters that aren't used.  They hark back to a time when I niaively thought I could just write a template that would work.  Such happy times before the dark clouds of knowledge and experience beat me down into the click-ops and copy pattern.  Anyway, if you go into the integration account and invoke the CallingFunction lambda (with a test paylod of {"message": "whatever message you want"}) you'll see a response from the lambda in the development account.

There's more work to do figuring out the best way to pass things in.  I initially used ENV_VARS for the lambdas and I think that's still the best way.  Cross-Account exporting isn't a thing. It seems you can have a lambda that returns a list of exports in the account but you still need to do the bootstrapping of roles and stuff that these two stacks do.  It is a way we could avoid too much clickery in future.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[226d416800...](https://github.com/mrakgr/The-Spiral-Language/commit/226d416800e6caadc8642a47fa8d7a4681faeb4e)
#### Friday 2022-03-25 18:53:28 by Marko Grdinić

"11:20am. Let me chill a bit and then I will get started. Yesterday after I closed and had a bit of rest, I tried redoing that piece again when I realized I could have inset the bottom poart to start things off, but I ran into trouble with beveling.

It is surprising. Eveling is actually more difficult that is seems at first glance. It is the thing that gave me the most trouble yesterday because how unpredicatble it has been. But is only a single piece that was giving me trouble so it is no big deal. For that indent, maybe I should have put in a bunch of points and use proportional editing instead. That could have worked better than beveling.

11:35am. You know what, let me skip the morning session. Who is going to start things now. I'll read the new chapter of Otome Survival, have breakfast, do the chores and then start.

1:15pm. Let me do the chores here and I will start.

1:40pm. Let me start.

Ah, I want an easy life, but wanting that while still human is just stucking your head into the sand. The specter of mortality is always one step behind. The only way to live is to go forward before it reaches you.

Right now what I am experiencing is essentially the ordinary life. My way of advancement in ML is closed, so I can only fall towards the primordial arts. Before the age of computers, people were drawing and writing.

1:45pm. In order to move forward in ML, I know what I have to do - with my programming skill I have to pour enormous resources into infering the right algorithms. In the situation I am in, if I had a genie that could grant me the kinds of computational resources that I need, I could make progress in a more brutish manner.

Instead of doing art, would the right choice really be to get a job and make money the old fashioned way? Programming would certainly pay more than art.

But I just can't accept it.

I didn't become a programmer for the sake of serving other people no matter how much it pays.

Always I should be attacking. Back when I looked for a job I was reeling from the blow. My heart was not in it.

I would have considered a job in ML seriously, but then I got whipsawed from that one attempt.

2pm. I should dream. Art is something you cultivate. I should not restrict myself to what is possible to 2d artists. Mangakas get 5h a sleep at night because they are always drawing. Sleep is one thing I won't compromise on in my path to stardom.

if I am going to be an artist, I'd want to go far beyond that in terms of productivity. Using your pen and hand and doing all the art like that is a thing of the past.

It is one thing to have pride in your programming skills, but what is programming for?

I need to remind myself of that.

Programming is all about automation.

For poker, I wanted to automate poker playing.

Then as long as I desire to automate my writing and art, that should be enough.

A true programmer is one who aims for automation, not one who makes money gluing together libraries to do some cheap thing.

If I want to be a programmer and an artist, that is, if I want to stay true to my old path, I should be aiming to automate my art skills. Sure, I can't do it right now, but it is not like I can do that with poker either. Ironically, had I attempted to do poker in the old school style, by making symbolic rules and testing them, I might have had some success, but I know that it would not be the true path.

2:10pm. Since I am going to be getting down and dirty in programming either way, I should pick a spot of my liking before I start digging.

3d art is not a bad thing to get good at. It has lot of potential for automation with programming. Today's NNs can't really abstract it, but future techniques should be more effective.

With art and msusic under my belt, even if Heaven's Key turns out to be a flop, I'll have all the skills that I need to be a solo gamedev. After Heaven's Key I could do a shooter like Hell's Prototype. The game itself would be simpler in terms of story than Heaven's Key, but games have a draw VNs don't.

And even though it is foolish to expect to make much money from a VN, I think I have enough life experience to develop my own unique style that cannot be immitated by anyone else. I can see storytelling possibilities that none other can right now.

So why not tap into that?

Rocking the boat might be bad in personal life, but it is a good thing to do in impersonal life. No matter how many holes one pokes into it, nothing is going to break the social bubble. It is unbreakable. So why not keep poking holes further for my own benefit.

I am really disappointed with the reception of the original Simulacrun. I was hoping that people would be so shocked as to oppose me. That might have lead to something productive. Instead I was greeted with silence.

This was heartbreaking, to think I really live in a world filled with NPCs. People just follow a predetermined script, driven by their emotions and never desiring to go beyond their nature. Humans are still living in the jungle.

So I do not need to feel bad about spreading an ideology of evil as long as it makes me money. I know that pretty much nobody in this world has what it takes to enter the self improvement loop. The reception makes it clear.

2:25pm. The fact that it is evil should make it feel fresh and interesting.

People live with suppressed emotions, so putting thme into a context where they are free should feel uplifting.

It is only a matter of time before the current isekai wave starts to feel oppressive. Deep down, nobody want to die just to get reborn in another world with superpowers. Deep down, I think people would desire that technology is not meaningless. The allure of magic is that it belongs to the wizard and not to a million other people.

I will show them where they need to look.

2:30pm. Dman it. i do not have any choice, but to make use of the power of other humans to get through my current hurdle.

2:35pm. Maybe I was too much in a hurry.

But it is not like I could have done this from the start. I only realized the essence of self improvement back in 2013. This served as the muse in 2014. I had tried writing before that, but it was uninspired and I only got a few pages in before getting bored of it. Before 2013 the only I was capable of would have been making cliche stories.

It is true, I had it in mind to publish the early arcs of Simulacrum once I was done and to make some money that way...it is not like making money was the primary thing.

Back then, what I really wanted is to see if I could make a story that convince myself of the self improvement loop.

2:40pm. The reason why I did not publish the story is similar to why I am getting out of programming now. No money to pay the editor or artist for the cover. To get it I'd need to get a job. Back then I was really mad that the path I stepped on and wanted to support me made such demands of me.

At it is reasonable. If a path of progression turns into one of regression it is only natural to abandon it.

This can happen.

Think of even very good artists of today using just pen and paper. What are they going to go when art goes to the enxt level in the follow up wave of ML?

Power is something to pursue. And power is something to exploit. But that same power can become a fetter to one's current position.

In today's world, programming skill no matter how great is not enough to let you tower above others.

It should be used whenver possible, but it has limitations that the old methods of just using your own hands don't.

2:45pm. So I should not restrict myself and just use whatever is appropriate for the situation at hand.

2:50pm. Money does not matter. What is important is that I myself feel a sense of freedom, like I did when I was a kid before school crushed my spirit.

The feeling of being able to do anything if one puts in the effort.

2:55pm. I had an idea.

Since I've come this far, why not make the covers for the first 3 arcs of Simulacrum and publish them. The Torment arc...I super aptly named. It is more like a mental breakdown than an actual story. So I'll leave that one aside.

3pm. I really understand the reason why Isayama acted the way he did with the end of Shingeki no Kyojin. Even if one is awakened to the alure of an evil ideology, is not like that by itself is enough to get rid of old values and lingering affections. So even though the most sensible progression of the story is 100% genocide, you get an 80% where nobody is happy.

3:05pm. Deep down, I do think that spreading an ideology is a good way to make money, but there is the loser voice urging me to get a programming job. And there was the kid voice urging me to push forward with my own power.

The kid is just about dead after I threw in the towel on ML, but I need to get rid of the loser voice.

It wouldn't actually take much to satisfy it. Even 100$ a month would get it to quiet down. That particular thread's greatest fear is that I will get bogged down making no progress for years and just end up taking a programming job anyway.

3:10pm. Let me step away from the screen for a while. I can't crank out things like a machine.

3:15pm. Yestereday when I wroked on the desk in Blender I had a really good feeling. Things are smooth and the way I move in the program is quite effective. I have a decent amount of skill right now. After 6 months I am by no means a beginner anymore. That is how I feel.

It is at this point that I can take on projects and see them through to completion.

Houdini...I am not sure what I will do with it. Its procedural capabilities will probably be less necessary than one expects, but I'll continue leearning it. It won't be my main focus by any means anymore. If I need to drop it, I'll just drop it. I won't hesitate to do so in order to focus on just Blender and Clarisse.

I go through these cycles. I internalize a skill, feel the power of simplicity, but then notice where doing things by hand becomes lacking and seek out more power. That is the way to get better, but the disadvantage of that is that you end up spending time learning skills you do not need.

In the past months after learning Blender I could feel the surge in capability over what I could do using very simple things.

Simplicity is what you truly need.

6:20pm. I've had time to think about my goals.

With poker an important part of the whole drive was what I imagined would me making modifications and getting ever increasing performance. Instead, I flatlined very quickly on that. My ideas failed and I could not get anything better than vanilla.

6:25pm. If it worked, I'd have made money, but the overall goal was to make an external cortex.

Even if it worked I'd just have let the algorithm do everything. I'd completely ignore the interaction aspect needed to build a connection between me and the program.

You know that image you see in psych articles of dark spots on a canvas that your brain images as being a dog?

What I need is a system that can do that kind of inference.

Make a few strokes and have the memory system anticipate what the rest of the picture is going to be, and build it.

7:05pm. Back from lunch.

To resume, even today you have the style tranfser using NNs. That could be useful for me to 2d-ify 3d scenes into 2d. Having to go over a 3d scene stroke by stroke would otherwise be so tedious that I would not want to do it. It would take me hours for every scene, it is not worth doing it.

7:10pm. This belief of building an external brain can be real or sophistry depending on the approach. It depends on the path one takes. It is true that up to now my approach has been very programming focused, but the domain that will have most opportunity for cooperative development is doing art. Definitely.

Imagine if I was trying to automate my own programming using a RL agent. That would be an impossible approach. Writing a bunch of lines of code would not even be close to getting my intent across. A program is a fragment of reality, and half a program is nothing.

Images and unstructured text are the complete opposite. They are filled with meaning and intent.

Even if my poker plan succeeded I'd have realized this basic problem. The agents would have been developing, but in a way that is separate from me.

For the best results in this pursuit of Singularity, I should do things as cooperatively as possible.

And interestly, this kind of cooperation is not like the one between humans. Having a program complete your input is literally how having a different brain would work.

Trying to play games together would not have the same effect.

Doing art in this era will be directly playing with memory systems.

The echoes of the future reverbarate through the halls of time into the now.

7:25pm. The ideas I had were interesting, but the intent was wrong. The games were too obvious as a path. The fact that supervised learning is so dominant should have clued me in.

7:30pm. If I can get some resources I'll take up programming again. If not, I guess I'll be waiting for the rest of the field to come up with something good.

Ultimately, I can't win just by failing. My art path is simply going to have to give me something in return.

I am going to have to win by getting an audience and having it support me.

Wasn't that always in the cards? Subconsciously, that must be the reason why I am making these public commits, a trace of my journey.

7:35pm. First comes the art, then come the games.

Right now, I should forget about memory systems and for the next six months firmly focus on cementing down the fundamentals. I should master everything I need to know by working with my hands.

After I reach that level of expertise I should be able to start outputting Heaven's Key at a steady pace. It is at that point, once I've garnered some resources, that I will be able to think of automating the workflow using NNs. I'll get nice big GPU and train some GANs as an exercise. Maybe the activation function I was using for RL would work well for that. And there is the duality gap method for stability, though it would spike training times massively.

If I can get AI chips, that would be even better.

As a rule, I want to make the third run from strength to strength. I should already be a good artist at that point and seeking to leave the rest of the crowd firmly in the dust.

7:45pm. Let me close here. I needed to rant a bit.

Tomorrow I am going to focus on shading. If needed just for a few hours a day. I really need a break. I've pushing myself hard lately.

I needed to re-establish my goals. Imagining myself just being a prop artist hurts a lot. If I had to accept the limits of the current tooling, the way Blender and Clarisse are now, I might as well become a wageslave anyway. But if I have a dream it will give me the stregnth to persevere. The machines will give me the power to escape my current predicament.

Random jobs will certainly not have the benefit of cooperative development between myself and the memory system I will be cultivating. If anybody else has a stronger way, then they are free to try it. If the big companies think they can plow through the hardship using just money then they can try."

---
## [pelavarre/byobash](https://github.com/pelavarre/byobash)@[59d54a72ab...](https://github.com/pelavarre/byobash/commit/59d54a72ab05ea1eb5a82f93c181353a697ad3d8)
#### Friday 2022-03-25 18:56:53 by Pat LaVarre

byobash: 6/N - capture more magic spells friends don't let friends work without

derive the BrokenPipeSink Class straight from Object,
    no need to derive from 'contextlib.ContextDecorator'

bin/cv: capture use cases of the Os Copy-Paste Clipboard,
    found at Mac Terminal 'pbpaste' and 'pbcopy'

bin/ipython3.py: capture how to reconfigure to run like plain 'python3',
    except with tab-completion, and with a command-line editor
        that doesn't depend on Gnu 'import readline'

bin/jq.py: choose '|jq .' as the default meaning of '|jq'

bin/ls.py: choose 'ls -rt' as the default meaning of 'ls' within standard options
bin/ls.py: start dreaming of 'ls' always providing some visible result

bin/python3.py: start capturing uses case of 'import pdb'

bin/stty.py: start capturing the most common use cases found near my work and play

---
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[65329f4fac...](https://github.com/pytorch/pytorch/commit/65329f4fac8fb22318b7a3eb115e9da207d8d41a)
#### Friday 2022-03-25 20:05:52 by Edward Z. Yang

Disable meta device tests.

After discussion with Can Balioglu, we have concluded that
https://github.com/pytorch/pytorch/pull/53682 , while clever, is more
trouble than it is worth.  The main problem is that whenever someone
adds support for new meta tensors, they then get dozens of new test case
failures, because tests that were previously halted by lack of support
for an operator on meta tensors, now have gotten further and hit some
logic which expects to be able to, e.g., pull out a real value from a
tensor (which clearly doesn't work).  This is very annoying and time
consuming!  Most of these tests aren't written with meta device in
mind, and it's not a good use of time to try to make them more generic.

The plan on record is to switch meta testing to OpInfo, but that patch
will take some time to prepare for now I want to stem the bleeding.  I
don't think we're at high risk for regressions here because meta tensors
mostly share logic with their regular brethren.

Signed-off-by: Edward Z. Yang <ezyangfb.com>

Pull Request resolved: https://github.com/pytorch/pytorch/pull/74468

Approved by: https://github.com/mruberry

---
## [hikidy123github/hikidy123-arrasworld-client](https://github.com/hikidy123github/hikidy123-arrasworld-client)@[d16eea8d12...](https://github.com/hikidy123github/hikidy123-arrasworld-client/commit/d16eea8d1254d55855fb9368f9f417a2bc4a959a)
#### Friday 2022-03-25 21:48:52 by hikidy123github

for arras server

Bambi is the titular protagonist of Disney's 1942 animated feature film of the same name. A deer living in a forest, he is best friends with Thumper (a rabbit) and Flower (a skunk). However, he was closest to his mother, who was shot and killed by a hunter during his first winter. Raised into a buck by his father, he strongly falls in love with his childhood sweetheart and love interest, Faline, and they end up, later on, having twin fawns, a son and daughter named Geno and Gurri, respectively.
Bambi originated as the main character in Felix Salten's Bambi, a Life in the Woods. He has made cameos in several Disney cartoons. In the Disney films, his specie

---
## [oxen-io/session-pysogs](https://github.com/oxen-io/session-pysogs)@[31bfd14d80...](https://github.com/oxen-io/session-pysogs/commit/31bfd14d80ec723fde3c3589408a27fc878f247f)
#### Friday 2022-03-25 22:19:39 by Jason Rhinelander

Use SQLAlchemy for database backend

We're using it fairly minimally: essentially still writing manual
queries, but now using SQLAlchemy to handle placeholder binding which is
nicer, and portable.

The API now goes like this:

- `db.get_conn()` returns a connection from the connection pool;
  web.appdb, in particular, is a preloaded, app-context connection
  object that most code uses.

- `web.query()` does an SQLAlchemy 'text' query, which is almost like
  regular prepare+bind+execute, except that it always uses `:name` for
  placeholders and binds using `name=...` keyword arguments.  That is,
  instead of:

      db.execute("SELECT token FROM rooms WHERE id = ?", (123,))

  we now do:

      query("SELECT token FROM rooms WHERE id = :id", id=123)

  or equivalently:

      db.query(appdb, "SELECT token FROM rooms WHERE id = :id", id=123)

  (the latter version is more useful where an app context doesn't exist
  and you need to pass in some other conn, such as is now done in
  __main__).

- transactions are now controlled with a `with appdb.begin_nested():`
  context, replacing the custom nested tx handler I made for sqlite.

We *could* start using more advanced SQLAlchemy query composition, but
that seems like more of a pain rather than something useful.  (I *don't*
want to use SQLAlchemy ORM, because in my experience ORM just gets in
the way as soon as you want non-trivial database structure, which we
have here).

This will allow us to (easily) add postgresql support.  (Other database
are probably a no-go: SQLite has long looked up to postgresql for
features and syntax and so the two are very similar dialects).

---
## [flesh-cube/flesh-and-blood-cards](https://github.com/flesh-cube/flesh-and-blood-cards)@[c86bad2061...](https://github.com/flesh-cube/flesh-and-blood-cards/commit/c86bad2061957ce28f95dc5643bd817c82a49479)
#### Friday 2022-03-25 22:29:31 by Tyler Luce

- Fix various data issues with Over Loop, Hamstring Shot, Salvage Shot, Become the Arknight, Forked Lightning, Command and Conquer, Life for a Life, Enchanting Melody, Eirina’s Prayer, Arknight Shard, Massacre, Blessing of Serenity, Zephyr Needle, Heron’s Flight, Cintari Saber, Dauntless, Hit and Run, Absorption Dome, High Speed Impact, Combustible Courier, Kavdaen, Trader of Skins, Feign Death, Dread Triptych, Rattle Bones, Mauvrion Skies, Meat and Greet, Cindering Foresight, Gambler’s Gloves, Spears of Surreality, Dimenxxional Gateway, Seeping Shadows, Seeds of Agony, Tremor of iArathael, Oaken Old, Cold Wave, Rejuvenate, Chill to the Bone, Wild Ride, Bad Beats, Nerves of Steel, Twin Twisters, Blood on Her Hands, Oath of Steel, Slice and Dice, Outland Skirmish, Dissolution Sphere, T-Bone, Zoom In, Release the Tension, Revel in Runeblood, Veiled Intentions, and Life of the Party

---
## [iu7og/bongodb](https://github.com/iu7og/bongodb)@[ea8c3cbf6a...](https://github.com/iu7og/bongodb/commit/ea8c3cbf6a8c8f1f9e4d4242299ace4994933727)
#### Friday 2022-03-25 22:54:44 by trvehazzk3r

[GH-13] Ok, fuck your LLVM you know, really, fuck it and your fucking default configuration for fucking linter

---

