## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-09-03](docs/good-messages/2022/2022-09-03.md)


1,617,578 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,617,578 were push events containing 2,233,252 commit messages that amount to 128,959,315 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 34 messages:


## [heeronchang/react](https://github.com/heeronchang/react)@[b6978bc38f...](https://github.com/heeronchang/react/commit/b6978bc38f6788c7e73982b9fd2771aabdf36f15)
#### Saturday 2022-09-03 00:35:39 by Andrew Clark

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
## [GesuBackups/tgstation](https://github.com/GesuBackups/tgstation)@[9d772c4f13...](https://github.com/GesuBackups/tgstation/commit/9d772c4f13da35569d61d223c8a693dc157666b2)
#### Saturday 2022-09-03 01:27:38 by Jacquerel

Dimensional Anomaly (#69512)

About The Pull Request

Everyone has been asking: "When will there be an anomaly like the bioscrambler, but for the space station? Please, we need more things which replace objects with different objects from the same typepath."
Well I made it and it looked like ass because non-tiling floor and walls look terrible, so then I made this instead.
Dimensional.mp4

The "dimensional anomaly" shifts matter into a parallel dimension where objects are made out of something else.
Like the Bioscrambler anomaly, it does not expire on its own and only leaves when someone signals it or uses an anomaly remover.
When it spawns it picks a "theme" and converts terrain around it until it covers a 7x7 square, then it teleports somewhere else and picks a new theme.

A lot of these themes are relatively benign like "meat", "fancy carpet", or "gold". Some of them are kind of annoying like "icebox" because it creates floor which slows you down, or "clown" because bananium is intentionally annoying. Some of them are actively dangerous, mostly "uranium" and "plasma".
The main problem this will usually cause for crewmembers is decreasing area security. When it replaces doors it replaces them with ones which don't have any access control, and it will also replace RWalls with normal and much more vulnerable walls which will make breaking and entering significantly easier until someone has taken the time to fix the damage. But also sometimes it will irradiate them, you never know.

The fact that sometimes the changes are benign (or provide uncommon materials) and might be happening in places you don't care about access to might encourage people to push their luck and leave it alone until it starts turning the captain's office into a bamboo room or repainting medbay a fetching shade of flammable purple, which I would consider a success.
Armour.mp4

If you successfully harvest the anomaly core you can place it into the reactive armour to get Reactive Barricade Armour, which shifts your dimension when you take damage and attempts to place some randomised (not terribly durable) objects between you and hopefully your attacker (it really just picks up to four random unoccupied tiles next to you). If you're EMPed then the changes it make to the environment will often be as unpleasant for you as they are for a pursuer, and significantly more likely to harm both of you rather than just provide obstacles.

Other changes:
I split anomalies out into their own dmi file, seems to be all the rage lately.
I moved the anomaly placing code into a datum instead of the event because I wanted to reuse it but if you have a better idea about where I could have put it let me know.
This also fixes a bug where the material spreader component wasn't working when I applied plasma materials to something, the extra whitespace was parsing as another argument for some reason and meant it would runtime.
Supermatter delamination was still pointing to Delimber anomalies instead of Bioscrambler.

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[ef2968cae5...](https://github.com/TaleStation/TaleStation/commit/ef2968cae5ad299302460c01650bd35b6af6fe9a)
#### Saturday 2022-09-03 02:12:00 by TaleStationBot

[MIRROR] [MDB IGNORE] Buffs Heretic Curses, Living Heart, Leeching Walk, and technically Entropic Plume by fixing some bugs (#2282)

* Buffs Heretic Curses, Living Heart, Leeching Walk, and technically Entropic Plume by fixing some bugs (#69181)

About The Pull Request

    Heretic curses have been buffed / reworked.
        Curses can be cast on any crewmember, not just those who you have fingerprints to.
        Having an item present in the ritual that contains fingerprints OR blood dna of a crewmember who you are cursing will boost the curse, causing it to last longer (and be stronger? Still undecided, but there's support for it)
        Curses have a max range (64 by default) and don't work on people on a different z-level (Do not BTFO miners so easily)
        Corrosion curse's numbers have been tweaked due to this, and it can no longer cause vital organ failure

    Living Heart has been buffed
        Cooldown cut in half, and it provides a bit more thorough instructions
        Closes 

    Living heart targets who are located in non-turf locs and are off z-level will show as on the same z #67256

Leeching Walk has been buffed

    Rust will also restore lost blood.

Technically buffs Entropic Plume by fixing some bugs

    "Cloudstruck" has always meant to blind, but they used the wrong method, so I fixed that.
    Also it was meant to inject multiple units of poison, but used "min" instead of "max" so it always did the lowest.
    I also fixed the stink cloud lasting forever on people.
    Amok also makes people holding guns to shoot people further away.

Closes

    Admin healing removes heretic living heart #69167 while I'm here

Why It's Good For The Game

    Heretic curses have pretty much always been bad, getting fingerprints is damn near impossible considering everyone uses gloves. Not only that but their requirements were very high. This should hopefully bring curses to the limelight, as they can be applied to any potential targets. It also rewards heretics who go out of their way to collect fingerprints and blood samples with even stronger curses.

    The Living Heart was often hard to pinpoint people exactly, partially cause of an oversight. I improved the text to be clearer about potential locations of your targets.

    Leeching Walk's healing was nice, but blood wounds were still a major threat. Some blood restoration should help.

    Entropic Plume I think has never worked correctly, so that was a bummer. Fixes that.

Changelog

cl Melbert
balance: Heretic: Curses have been reworked. You can now curse any member of the crew, granted they're not too far away. If you additionally provide an item in the ritual containing a sample of the target's blood or fingerprints, the curse's duration will be increased and have its range uncapped.
balance: Heretic: The Curse of Corrosion has been nerfed slightly due to this rework, and can no longer cause vital organs to fail.
balance: Heretic: The Living Heart should now provide better directions, and had its cooldown halved to 4 seconds.
balance: Heretic: Leeching Walk (rust healing) now restores lost blood.
balance: Heretic: If you apply Amok (Entropic Plume) to someone holding a gun, they'll try to shoot it at people nearby.
fix: Entropic Plume's effect now blinds, as it should.
fix: Entropic Plume no longer sometimes applies the stink effect forever.
fix: Entropic Plume no longer always applies the lowest amount of poison, and properly scales on distance.
fix: Fixed an exploit which allowed people to figure out if a Heretic's heart was a previously a Living Heart after being removed.
fix: If a heretic is fully healed by something (such as ahealed), they'll not lose their living heart
/cl

* Buffs Heretic Curses, Living Heart, Leeching Walk, and technically Entropic Plume by fixing some bugs

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[773f04110e...](https://github.com/TaleStation/TaleStation/commit/773f04110e5ee89b80659d7053c6b8572d5aa2ce)
#### Saturday 2022-09-03 02:12:00 by TaleStationBot

[MIRROR] [MDB IGNORE] Spider Rebalance PR: Burn Baby Burn Edition (#2288)

* Spider Rebalance PR: Burn Baby Burn Edition (#68971)



This is a remake of #66106, with more thought put into the underlying balance. The main goal of this PR is to make fighting spiders more accessible and interesting for the majority of the crew while nerfing the extremely strong and boring option of simply using freezing temps to kill spiders. Also fixes #67765. The changes are as follows:

NEW SPIDER COUNTERS

    Fly swatters now deal 25 damage to spiders on hit, increased from 1
    Pesticide now deals massive stamina damage to spiders and a little bit of physical damage as well (the damage portion not added by this PR)
    Spiders can now be caught on fire through any traditional mean of catching something on fire. Spiders will automatically put themselves out after a time. This was done instead of an active action because AI spiders are also subject to this change as well, and I don't feel like bloating the simple mob AI with putting themselves out

SPIDER CHANGES

NERFS

    Toxin injection has been removed from all spiders except for the hunter, flesh spiders and the viper
    Hunter toxin (used by hunters and flesh spiders) now only brings the afflicted down to 40 health, and will stop taking effect once the afflicted reaches that threshold. Should the afflicted still have the toxin in their system and get healed, the toxin will begin dealing damage again until the afflicted is at 40 health or below again
    Viper toxin now only brings the afflicted down to 10 health, but also has the hallucination effects of Mindbreaker toxin. This hallucination effect is applied regardless of target health. It also no longer generates other harmful chemicals into the afflicted's system, but is much more potent at base
    Flesh spiders cannot regenerate while on fire

BUFFS

    Time it takes for spiders to normalize their temperature cut by half. While they will react faster when in cold or hot environments, when they leave said environments it will take less time to return to normal temperature
    Unsuitable temperature damage reduced to 4 from 8
    You can no longer push spiders by running into them
    Webbing heat damage threshold increased from 300 to 350 (same temp where spiders also take damage)
    Broodmother egg laying time reduced to 12 seconds from 15
    Broodmother web laying time multiplier reduced to 0.5 from 1
    Broodmother health increased to 60 from 40
    Broodmother damage increased to 10 - 15 from 5 -10

BEHIND THE SCENES CHANGES

    You can now make any simple mob able to be caught on fire by setting flammable to true
    How fast a simplemob stops burning is controlled by fire_stack_removal_speed
    Can now now control how fast simplemobs regulate their temperature using temperature_normalization_speed. Before this PR, this value was hard-coded at 10, I have set the default to 5 as 10 was too long in almost any case. This will notably affect slimes, who could easily die to being cold long after being removed from the cold area. I see this as purely beneficial
    Toxins now have a health_required value. The afflicted has to be above this health value in order to take damage from the toxin. Only used in the spider toxins currently
    When I was setting up simplemobs to be flammable, I noticed basic mobs can be glitchily set on fire, so I fixed it to where they can't be set on fire.

Why It's Good For The Game

    Spacing something is very easy, but not very fun or interesting compared to starting and controlling a fire. Swapping spiders' temperature weakness from spacing to fire is beneficial to the fun of fighting them and playing as them, allowing more creativity and resourcefulness on both sides. Ideally, this should allow for atmosians and chemists to use their skills in a fun way.
    Currently, ignoring spacing them, the only people who can reasonably take on spiders is security, since they have lasers which do burn and stuns to slow the spiders down. However, this small subset of players cannot normally destroy a spider infestation without spacing them, so letting fly swatters and pesticide be used to combat spiders allows other crewmembers to fight back, letting them actually enjoy facing spiders as a threat and allowing the crew to defend themselves.
    Being killed by spider toxin after fighting off a horde isn't fun. The changes still make it a threat you have to be aware of, but not one which detracts as much from the combat loop. This also forces spiders to secure the kill themselves, which is more fun than having the toxin do it for you.
    Broodmothers in their current state are incredibly weak by themselves, which is intentional by design. However, the new changes hope to make playing as a broodmother easier and hopefully allow more broodmothers to get the spider infestation started properly. After all, Dynamic is their common source now, and they should be consistently worth the threat cost to spawn them.
    Previously, spider structures would seemingly vanish for no reason if the room was heated to be greater than 300 but less than 350, as the spiders would not be able to tell that it was too hot. Now, if the structures are taking damage, spiders will also be taking damage, so understanding what's going on should be easier now.
    Pushing spiders into a corner by running into them was not a fun tactic to deal with as a spider and didn't make much sense seeing how big the spiders are.

Changelog

cl
add: Spiders can now be caught on fire
add: Spiders take significant damage from fly swatters and stamina damage from pesticide
balance: Spiders have been re-balanced. Their toxins can no longer kill but they are not as susceptible to freezing
balance: General stats of spider broodmothers have been buffed with more health, damage, and faster web and egg placement
balance: Flesh spiders cannot regenerate whilst on fire
balance: Simplemobs change their internal temperature twice as fast
fix: Basic mobs no longer glitchily catch on fire.
/cl

* Spider Rebalance PR: Burn Baby Burn Edition

Co-authored-by: IndieanaJones <47086570+IndieanaJones@users.noreply.github.com>

---
## [isaaguilar/terraform-operator](https://github.com/isaaguilar/terraform-operator)@[1c9344770c...](https://github.com/isaaguilar/terraform-operator/commit/1c9344770c2391ff82fd3cbcf4251c6055b39129)
#### Saturday 2022-09-03 02:12:10 by Isa Aguilar

New v1alpha2 apiVersion

Many changes in a new api version. Most of the changes are backwards compatible.

**Inroducing v1alpha2**

Changes have been introdced into v1alpha2 to give users even more granularity and options to configure
the workflow tasks (formerly known as runners). Each task container can now have defined container
options, such as labels, annotations, envs and envFrom, and more

Along with the changes to task options, each task is now a stand-alone container in a pod. This
simplifies setting up tasks since there is no sharing of pod configuration aside from the common items,
such as envs, volumes, volume mounts and a few others.

And of the biggest change is that tasks do not have their execution scripts built into the containers
anymore. Instead, tasks will pull their tasks from an http source, read them from a configmap, or
have them defined inline in the tfo resource spec. Why this change? Frankly, it was very hard to
modify the execution scripts becuase they had to be baked into containers. Changing a simple fix
in the task execution meant having to build new images to hunderds of different terraform versions.

I hope that the ability to get the execution script from a source would encourage users to make
changes easily and then contribute back if they feel their changes could benifit the community.

**Migration from v1alpha1**

This is not fun to say, but until v1alpha1 is fully deprecated and removed, a conversion webhook has
been introduced to migrate existing v1alpha1 resources to fit the into v1alpha2. The challenge of
api change was how guarantee parity to a greatest extent. Unfortunately, some features have been made. The
features may be added back as a plugin or a separate controller in the future.

**Conersion webhook**

The conversion webhook is both a blessing and a curse. The beauty of it means users can continue to
use v1alpha1 to create new resources. The ugly part is that is has a rather large operational
burden.

If a user's cluster has cert-manager installed, this really isn't that bad. Otherwise, operators will need
to create ssl certs to secure the webhook endpoints so that kubernetes could communicate with it. It's
probably not as bad as it sounds. I'll document some of the ways to do this.

**Removals**

One such feature that has been removed is exportRepo. This feature, though useful when terraform may be needed
to be run outside of tfo, was always run in the background. This meant it wasn't tracked as
a first-class citizen of the tfo project. A new project might be added to reintroduce this back into
the tfo ecosystem.

---
## [DoomTheRobot/JAMP2](https://github.com/DoomTheRobot/JAMP2)@[d602c28bb5...](https://github.com/DoomTheRobot/JAMP2/commit/d602c28bb56f908988e4f6d91cf40eb767492ca1)
#### Saturday 2022-09-03 02:20:06 by NaN

fuck shit cunt bullshit

i'll change map later when im less mad

---
## [life-rs/MTGA-Backend](https://github.com/life-rs/MTGA-Backend)@[e4cb5e9bea...](https://github.com/life-rs/MTGA-Backend/commit/e4cb5e9beaeaa99d0d89817dd4cc7440123efba6)
#### Saturday 2022-09-03 02:54:05 by life-rs

fuck you github

fixed the all items examined except these parent

---
## [life-rs/MTGA-Backend](https://github.com/life-rs/MTGA-Backend)@[f7b6d078a6...](https://github.com/life-rs/MTGA-Backend/commit/f7b6d078a6b96be4bfc64d1fd33e12c4593516bd)
#### Saturday 2022-09-03 02:57:58 by life-rs

Update DatabaseLoader.js

fuck you github!!!!!!!!!!!!

---
## [newstools/2022-new-york-post](https://github.com/newstools/2022-new-york-post)@[cbe7d7767e...](https://github.com/newstools/2022-new-york-post/commit/cbe7d7767e845dbf0b8fb423e22e6f6663568d8e)
#### Saturday 2022-09-03 02:58:05 by Billy Einkamerer

Created Text For URL [nypost.com/2022/09/02/woman-catches-wise-to-boyfriends-cheating-after-he-lasts-longer-in-bed/]

---
## [Kapu1178/Gameserver](https://github.com/Kapu1178/Gameserver)@[e4c4e7ca09...](https://github.com/Kapu1178/Gameserver/commit/e4c4e7ca09d2ddfd959dbcd978ebcac412b600b9)
#### Saturday 2022-09-03 05:59:16 by Kylerace

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
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[557e53a23b...](https://github.com/treckstar/yolo-octo-hipster/commit/557e53a23b2430cdb01fab0414f3b646f62eb459)
#### Saturday 2022-09-03 08:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [xexyl/mkiocccentry](https://github.com/xexyl/mkiocccentry)@[89e7ace002...](https://github.com/xexyl/mkiocccentry/commit/89e7ace002cc8832995b1a3484a673fed7a2e053)
#### Saturday 2022-09-03 08:33:41 by Landon Curt Noll

Released 0.6 2022-09-02

Released IOCCC entry toolkit v0.6 2022-09-02

Updated CHANGES.md for v0.6 2022-09-02.

Changed `MIN_TIMESTAMP` from 1655958810 to 1662145368.

Updated `mkiocccentry` from "0.40 2022-03-15" to "0.41 2022-09-02".
Updated `.info.json` version from "1.10 2022-06-22" to "1.11 2022-09-02".
Updated `.author.json` version from "1.13 2022-06-22" to "1.14 2022-09-02".

Improved code to use new facilities for output to a buffer from
dbg release of v2.5 2022-07-23.

The `chk_foo()` functions in `chk_validate.c` and the `test_foo()`
functions in `entry_util.c` are Code complete, although the remain
untested and unused.  The `chkentry` tool is not code complete.
Later releases of tested JSON semantic code will no doubt modify
these functions.

Improved a number of the ways that JSON field values are checked.
In a number of cases, code form `mkiocccentry.c` was moved into
`test_foo()` functions so that they could be used by other
tools such as the JSON semantic test code.

Added code to generate JSON semantic tables from JSON reference
files for `.info.json` and `.author.json`.  The `jsemcgen.sh` tool
manages this by way of the `jsemtblgen` code generator and
header, patch and trailer files (see `chk.auth.*` and `chk.info.*`
files).

Avoided the appearance of attacking any particular individual.  It
was not our intention to disrespect anyone, even though we disagree
with some of the technical decisions.  Where we have fundamental
technical disagreements, we attempted to express those technical
disagreements with humor in hopefully a more fun way.  As also now
apologize for how `bison` and `flex` generated code may look, instead
of simply calling it ugly.  As such, we hopefully improved some of
the humor in our code while trying to be nice and friendly to others.

For example now the adjusted dbg levels in JSON parser are:

```
*     At -J 3, only the top level return type and top level tree are printed.
*     At -J 5, intermediate tree return types and tree are printed too.
*     At -J 7, also print grammar progress.
*     At -J 9, also print sorry_text and sorry_lang grammar values.
```

Removed a number of files and added a number of files under the
`test_JSON/` tree.  When the JSON semantic code is being tested in
a future release, we expect more such `test_JSON/` tree changes.

Improved / add a number of man pages.  Updated `README.md`.

Improved and expanded `txzchk`.

Added more test code.  We attempt to detect feathers in tarballs.  :-)

We will neither confirm nor deny the presence of an "Easter egg".
Do to do would be "foolish".  :-)

Improved and fixed `vermod.sh` and `reset_tstamp.sh`.  Tested this
code by changing the `MIN_TIMESTAMP` as noted above.  The `MIN_TIMESTAMP`
needed to up updated anyway due to changes in the `.info.json` and
`.author.json` formats.

Made numerous improvements and bug fixes to the Makefile.

Fixed how `picky` is used in by the `make picky` rule for a few
special files.

Added multiple rules to the Makefile including but not limited to
`make mkref`, `make legacy_clobber`, and `make legacy_clean` rules.
Applied multiple bug fixes to the Makefile.

Improved the Makefile to be less impacting for modern systems
while trying to maintain, for as long as we can, compatibility
with some older systems.

Attempted to improve compatibility with reasonably modern systems.
We managed to keep CentOS 7 somewhat supported for now, although
we may be forced to drop support of such an old system before 2024.
Users of very out of date systems can still enter and submit entries
to the IOCCC.  They just might need to find a more modern system
to package and submit their IOCCC entry, however.

Added stub code for `hostchk.sh`.  A future release will include
mode tests for the given hosts.  Future releases will also
include a bug report system that will also use `hostchk.sh`.

Improved the `no-comment` directive in `.info.json` and `.author.json`
files.

Improved how `time_t` values are used and printed.  We no longer
assume that `time_t` is signed nor assume it is unsigned.

Improved comments in C code about special `seqcexit` comment directives.

Make numerous bug fixes and fixed a fair number of typos.
Nevertheless we dare *NOT* claim this is complete.  :-)

---
## [ekkusa/android_kernel_sony_sdm845](https://github.com/ekkusa/android_kernel_sony_sdm845)@[2acd5b45ae...](https://github.com/ekkusa/android_kernel_sony_sdm845/commit/2acd5b45aeea4eb4b86bfcad7db8e4b8ec0e359f)
#### Saturday 2022-09-03 08:55:11 by Angelo G. Del Regno

Merge: Performance improvements.

This patchset brings some performance improvements and the addition of the LZO-RLE
algorithm to the kernel, also usable in zram (yup, tested, works but LZ4 is still ok for us).

The main performance improvement is for SWAP space: the locking has changed and
the swap cache is now split in 64MB trunks.
This gives us a reduction of the median page fault latency of 375%, from 15uS to 4uS,
and an improvement of 192% on the swap throughput (this includes "virtual" swap
devices, like zRAM!). The real world user experience improvement of this on a mobile
device is seen after a day or two of usage, where it usually starts losing just a little
performance due to the large amount of apps kept open in background: now I cannot
notice any more performance loss and the user experience is now basically the same as
if the phone was in its first 2 hours of boot life.

Other performance improvements include, in short:

    UDP v4/v6: 10% more performance on single RX queue
    Userspace applications will be faster when checking running time of threads
    2-5% improvements on heavy multipliers (yeah, not a lot, but was totally free...)
    Improvements on rare conditions during sparsetruncate of about 0.3% to a
    way more rare around 20% improvement (that's never gonna happen, but there
    is no performance drop anywhere).

Tested on SoMC Tama Akatsuki RoW

This was taken from
Repo:
https://github.com/sonyxperiadev/kernel
PR: 2039 ([2.3.2.r1.4] Performance improvements)

Signed-off-by: sweetyicecare <gabrielseedev@outlook.com>
Signed-off-by: Jprimero15 <jprimero155@gmail.com>
Signed-off-by: Joel Gómez <nahuelgomez329@gmail.com>

Conflicts:
	mm/swapfile.c
	mm/swap.c

---
## [npv12/strix_kernel_oneplus_sm8150](https://github.com/npv12/strix_kernel_oneplus_sm8150)@[05880cc637...](https://github.com/npv12/strix_kernel_oneplus_sm8150/commit/05880cc637e33c9e1c99bb22074f4b4f9abd7b54)
#### Saturday 2022-09-03 10:04:32 by Zlatan Radovanovic

Revert "msm: camera: icp: Enable hang dump on failure"

Fuck you CAF.

This reverts commit eece594678f618c964051092fa0dd470b26039b3.

Signed-off-by: Pranav <npv12@iitbbs.ac.in>

---
## [Polyfrost/OneConfig](https://github.com/Polyfrost/OneConfig)@[f6cf5bde15...](https://github.com/Polyfrost/OneConfig/commit/f6cf5bde158f635e3fb2000de64f050e13426a86)
#### Saturday 2022-09-03 12:24:58 by Wyvest

Joan was quizzical
Studied pataphysical science in the home
Late nights all alone with a test tube
Oh, oh, oh, oh
Maxwell Edison, majoring in medicine
Calls her on the phone
"Can I take you out to the pictures, Joa-o-o-oan?"
But as she's getting ready to go
A knock comes on the door
Bang! Bang! Maxwell's silver hammer
Came down upon her head
Clang! Clang! Maxwell's silver hammer
Made sure that she was dead
Back in school again, Maxwell plays the fool again
Teacher gets annoyed
Wishing to avoid an unpleasant scene
She tells Max to stay when the class has gone away
So he waits behind
Writing fifty times "I must not be so"
But when she turns her back on the boy
He creeps up from behind
Bang! Bang! Maxwell's silver hammer
Came down upon her head
Clang! Clang! Maxwell's silver hammer
Made sure that she was dead
P. C. Thirty-One
Said "We caught a dirty one"
Maxwell stands alone
Painting testimonial pictures
Oh, oh, oh, oh
Rose and Valerie, screaming from the gallery
Say he must go free (Maxwell must go free)
The judge does not agree, and he tells them so
But as the words are leaving his lips
A noise comes from behind
Bang! Bang! Maxwell's silver hammer
Came down upon his head
Clang! Clang! Maxwell's silver hammer
Made sure that he was dead
Wo-wo-wo-woh
Silver hammer man

---
## [mars-sim/mars-sim](https://github.com/mars-sim/mars-sim)@[3fa5bad73f...](https://github.com/mars-sim/mars-sim/commit/3fa5bad73f1155e22dabb4949c86d6f1f5040242)
#### Saturday 2022-09-03 12:34:05 by mokun

Define and display 4 meal times for Cooking tab

08/30/2022

- add: create getMealTimeString(), getTimeDifference() and
       getMealTime() in CookMeal
- add: showcase the start & end of 4 meal times in TabPanelCooking
       - Breakfast
	   - Lunch
	   - Dinner
	   - Midnight
- change: rework isMealTime() in CookMeal
- change: rework goForFood() in EatDrink
- change: adjust modifiers in modifyWasteResource() in
AmountResourceGood
- change: revise getTaskDescription(boolean subTask) in
        TaskManager

https://github.com/mars-sim/mars-sim/issues/673

---
## [Dustinwiliam21/investor](https://github.com/Dustinwiliam21/investor)@[406ff83ff5...](https://github.com/Dustinwiliam21/investor/commit/406ff83ff504a4b9f6989237e751ee8332e91220)
#### Saturday 2022-09-03 12:50:14 by Dustin William

Believe yourself 

I like going to the beach, picking the shells of the beach. I smile and laugh a lot, I really enjoy a fun night, I like going out for dinner, I have excellent taste in restaurant, I like to cook, go to the gym , dancing and swimming

---
## [mortezadadgar/android_kernel_lge_bullhead](https://github.com/mortezadadgar/android_kernel_lge_bullhead)@[23e5470ad5...](https://github.com/mortezadadgar/android_kernel_lge_bullhead/commit/23e5470ad5aa0b6e78993a7577c193ff04f177f8)
#### Saturday 2022-09-03 12:56:47 by Linus Torvalds

mm: get rid of 'vmalloc_info' from /proc/meminfo

It turns out that at least some versions of glibc end up reading
/proc/meminfo at every single startup, because glibc wants to know the
amount of memory the machine has.  And while that's arguably insane,
it's just how things are.

And it turns out that it's not all that expensive most of the time, but
the vmalloc information statistics (amount of virtual memory used in the
vmalloc space, and the biggest remaining chunk) can be rather expensive
to compute.

The 'get_vmalloc_info()' function actually showed up on my profiles as
4% of the CPU usage of "make test" in the git source repository, because
the git tests are lots of very short-lived shell-scripts etc.

It turns out that apparently this same silly vmalloc info gathering
shows up on the facebook servers too, according to Dave Jones.  So it's
not just "make test" for git.

We had two patches to just cache the information (one by me, one by
Ingo) to mitigate this issue, but the whole vmalloc information of of
rather dubious value to begin with, and people who *actually* want to
know what the situation is wrt the vmalloc area should just look at the
much more complete /proc/vmallocinfo instead.

In fact, according to my testing - and perhaps more importantly,
according to that big search engine in the sky: Google - there is
nothing out there that actually cares about those two expensive fields:
VmallocUsed and VmallocChunk.

So let's try to just remove them entirely.  Actually, this just removes
the computation and reports the numbers as zero for now, just to try to
be minimally intrusive.

If this breaks anything, we'll obviously have to re-introduce the code
to compute this all and add the caching patches on top.  But if given
the option, I'd really prefer to just remove this bad idea entirely
rather than add even more code to work around our historical mistake
that likely nobody really cares about.

Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>

---
## [Foundation-19/Foundation-19](https://github.com/Foundation-19/Foundation-19)@[6bf6cdb77f...](https://github.com/Foundation-19/Foundation-19/commit/6bf6cdb77f582598b90e63fa44a922fd033ae3d0)
#### Saturday 2022-09-03 13:19:20 by harry

fixes panic bunker adjacent shitcode (#769)

* ugly as hell

* idiot

* think before i commit (never)

---
## [majestrate/loki-network](https://github.com/majestrate/loki-network)@[7d52d48c21...](https://github.com/majestrate/loki-network/commit/7d52d48c217c5cb984d6b4aaaa3496c6d4540cd6)
#### Saturday 2022-09-03 15:31:10 by Jeff

tweaks for wine and yarn for gui

* allow specifying a custom yarn binary for building the gui using -DYARN= cmake option
* unset DISPLAY when calling wine because i hate popups
* do not rebuild gui when building for windows
* by setting the magical undocumented env var USE_SYSTEM_7ZA to 'true' we can have the pile of npm bullshit code use our system's local 7z binary instead of the probably not backdoored binary from npm, yes for real. i hate nodejs so god damn much you have no fucking idea
* allow providing a custom gui from a zip file via -DGUI_ZIP_FILE cmake option

---
## [ofek/black](https://github.com/ofek/black)@[0019261abc...](https://github.com/ofek/black/commit/0019261abcf6d9e564ba32d3cc15534b9026f29e)
#### Saturday 2022-09-03 15:39:27 by Richard Si

Update stable branch after publishing to PyPI (#3223)

We've decided to a) convert stable back into a branch and b) to update
it immediately as part of the release process. We may as well automate
it. And about going back to a branch ...

Git tags are not the right tool, at all[^1]. They come with the
expectation that they will never change. Things will not work as
expected if they do change, doubly so if they change regularly. Once
you pull stable from the remote and it's copied in your local
repository, no matter how many times you run git pull you'll never see
it get updated automatically. Your only recourse is to delete the tag
via `git tag -d stable` before pulling.

This gets annoying really quickly since stable is supposed to be the
solution for folks "who want to move along as Black developers deem
the newest version reliable."[^2] See this comment for how this impacts
users using our Vim plugin[^3]. It also affects us developers[^4]. If
you have stable locally, once we cut a new release and update the stable
tag, a simple `git pull` / `git fetch` will not pull down the updated
stable tag. Unless you remember to delete stable before pulling, stable
will become stale and useless.

You can argue this is a good thing ("people should explicitly opt into
updating stable"), but IMO it does not match user expectations nor
developer expectations[^5]. Especially since not all our integrations
that use stable are bound by this security measure, for example our
GitHub Action (since it does a clean fetch of the repository every time
it's used). I believe consistency would be good here.

Finally, ever since we switched to a tag, we've been facing issues with
ReadTheDocs not picking up updates to stable unless we force a rebuild.
The initial rebuild on the stable update just pulls the commit the tag
previously pointed to. I'm not sure if switching back to a branch will
fix this, but I'd wager it will.

[^1]: https://git-scm.com/docs/git-tag#_on_re_tagging

[^2]: https://black.readthedocs.io/en/stable/contributing/release_process.html#moving-the-stable-tag

[^3]: https://github.com/psf/black/issues/2503#issuecomment-1196357379

[^4]: In fairness, most folks working on Black probably don't use the
      `stable` ref anyway, especially us maintainers who'd know what is
      the latest version by heart, but it'd still be nice to make it
      usable for local dev though.

[^5]: Also what benefit does a `stable` ref have over explicit version
      tags like `22.6.0`? If you're going to opt into some odd pin
      mechanism, might as well use explicit version tags for clarity
      and consistency.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[cd0f81c13e...](https://github.com/mrakgr/The-Spiral-Language/commit/cd0f81c13ef4d7e3f0fe4555a2d9ae2aa044706a)
#### Saturday 2022-09-03 16:05:19 by Marko Grdinić

"9:55am. > I don't do anything with ML and only briefly studied AI, so I can't tell if these chips would be useful for you, but it doesn't hurt to look into just maybe their basic doc and see? I just wanted to make you aware of them as they've been around for some time now. I know there are a bunch of other vendors making ML chips now, it's a pretty crazy market. Nvidia even has the "Jetson" single board computer platform for it. NXP's next line of ARM MCUs will have it baked in, etc. Everyone is jumping on the "edge computing/ML" bandwagon nowadays. I find out about a lot of these from the cnx-software.com blog, and other embedded blogs I read. The sipeed one I found out from being a Seeed customer and being on their mailing list. Seeed actually has a couple other dev kits that have ML chips in them besides the one with the Kendryte chip (I think that one was part of the MAIX platform).

Got this reply to the monthly thread.

https://www.cnx-software.com/2022/09/03/intel-loihi-2-high-efficiency-neuromorphic-chip-works-with-the-lava-open-source-framework/

This is the post at the top.

10am. I'll keep the blog in mind, but nevermind this for now. Did I get any views for the latest chapter? Now my total views is at 202, and the previous chapter got 2 extra.

I need to keep pushing it. Ultimately the best kind of advertizement is to just keep putting out content. Even I myself look at series and want to see a bunch of chapters being published before really investing myself. The series on RR are more similar to manga in that they have long running arcs. Books are more episodic. The size of an average book is basically nothing. Let me take a look at the Rosen Garten raw thread, chill a little and then I will get started on chapter 8.

10:15am. Arguably some of the views might be coming from the PL thread. I'll get a sense of how things work when posting on just RR in future chapters.

10:40am. Let me start. I need to do some ice breaking for chapter 8. There are a bunch of directions I can take the story in.

11am. I am thinking about it. I need some time to decide.

https://www.quora.com/Can-an-object-only-emit-infrared-light-If-yes-can-we-see-through-it-How-will-it-appear-to-our-naked-eyes
https://www.quora.com/If-its-possible-to-surgically-implant-cone-cells-from-bees-or-snakes-that-perceive-ultraviolet-or-infrared-light-respectively-into-a-humans-eyes-would-said-human-be-able-to-see-ultraviolet-and-or-infrared-light

> If you remove the membrane on the lens of a human eye (which serves as a UV filter to protect the retinal cells) then that person can see UV light. This was once a common treatment for cataracts (where the lens becomes cloudy) - and it is surgery that my mother had.

> Anyway - my mother sees UV light as a blue/violet color (as you might expect) and as an avid gardener was struck by the weird spots and stripes she was seeing on some of her favorite flowers. (Turns out those are navigational aids for bees - who see in the UV).

What are these navigational aids in flowers. This is what I want to go for in the initial cheating method.

https://www.howplantswork.com/2008/11/30/flowers-what-you-see-versus-what-the-bees-see/

https://www.amazon.com/White-Pigment-Powder-Reactive-Fluorescent/dp/B00F3J8GEK?th=1

Hmmm, would this pigment be visible in UV directly or does it need that blacklight thing?

https://en.wikipedia.org/wiki/Blacklight

https://www.quora.com/Are-there-goggles-that-let-us-see-UV-rays-like-there-are-goggles-to-see-in-infra-red

///

Apparently, yes:

Lumilass - UV to Visible Light Converter Fluorescent Glasses

In most of the cases where there is UV light there is already also considerable optical light. But in the rare and almost always artificial situations where there is only UV light available, these materials apparently would do the trick of making that UV light visible to the human eye.

Notice that since IR photons are less energetic than optical photons, IR goggles require a power source to achieve the conversion. The fact that UV photons are more energetic than optical photons means that no power source is needed. The material itself can take care of the conversion through fluorescence.

You might have to cut your own lenses, though.

///

12:15pm. I am still thinking about it. I need some time to think about it. I've figured out how to do the next chapter, but not enough about how to do the future battles.

12:50pm. I am still thinking about it. Let me have breakfast here.

*

2:05pm. Done with breakfast. Let me chill longer. Somebody rec'd 'The Witch and the Beast' in an /a/ thread. It is not on Dex or Nello, so I had to get it off Nyaa.

Right now I am halfway in vol 1. Let me finish it and maybe I'll take a nap. My feelings are complex. I guess every chapter is its own challenge.

I have various fears. Compared to the 2014 arcs, I need to make sure to extend the story properly.

I am not sure how long I'll be able to be a writer for.

I felt a sense of freedom today when I realized that with my current mentality I'd have run away from high school. But now I feel depressed when I realize that because of that same mentality I've run away from programming. Yesterday my will was strong, but now it is wavering again.

No, I just need some time to think about the plot properly. I guess jumping into the next chapter right the next day is too much for me.

The problem is that a lot of the scenes that I've envisioned came with my youthful, berserker mentality of writing, but right now I have a somewhat depressed, more mature mentality. So they aren't really a good fit.

There is no helping it. I guess taking a break every few days from writing to just think about what is next is a good thing. I can't write like a machine. I know that some writers can do like a novel a week, but I am not one of them and I never will be.

3pm. Somebody left the tap water open for what must have been an hour. I hope it wasn't me.

A little story.

Every time before I go to bed, I get paranoid about leaving the tap water on. At some point the paranoia has become so strong that I've taken it up to myself to checking the tap consciously so I store it into memory and don't trigger it again. I'd sometimes get up and check it, I must have done it dozens of times, but I've never made the mistake of leaving it on. Even though I know that, it is really such a pain to argue against the 0.01% chance so it is easier for me to get out of bed and check instead of will the urge away.

I've only realized it today that from my current position at the computer I can in fact hear if the water is running through the pipes or not. The bathroom is right next to my room. This whole time I thought it might have been somebody else taking a bath, I only started getting suspicious like 10m ago that it is taking too long. I should have just gotten up and checked it instead of trying to finsih the novel.

Let me take a bath here.

I've gotten some inspiration. I am going to have to power up the NPCs, and make them literal mages if they want to keep up with Euclid. There is no reason why the system wouldn't be helping them. To begin with, the game is set to induce Euclid's development. For every enemy he faces, he'd need to develop a new power. Why not take the story in that direction?

Euclid has the advantage of being a real being, so why shouldn't the rest get the superpowers that go along with being fakes?

3:25pm. Let me take that bath instead of just thinking about it. After that, I'll try to write just a little bit down to break the ice. Every chapter is its own challenge it seems.

The trouble for me with both programing and writing - there are parts where I am just going off a script and it feels like a regular job that I could do on a schedule. But there are time like this when I ma brainstorming and am filled with uncertainty. It engulfs my whole day and it feels like I am doing nothing but worrying during all this time. You can't really call it work. I have hangups about this.

I really do need to think about it as actual work even if I am doing nothing. Overcoming lethargy and inspiring myself is not that easy.

4:20pm. Done with the bath. Let me put those triple dollars and try to do some writing.

$$$

(Heaven's Key, Heavenly realm)

Slowly, out of the pocket of his trenchcoat, the revolver came out. To my eyes, the movement seemed impossibly smooth and ethereal. I had a sense of time and could see exactly the trail the gun followed and as he raised it, where it would go. As if to draw out the tension, the white haired guy lifted the gun straight up, paused it a bit and then swung it down until it was pointed straight at me. He had a grin on his face. I perfect slow motion, I could see him put his finger on the trigger.

I knew what would happen next.

The last time I was here I got shot to death. This time, my mind is whirring a lot faster, so I even though I have a second in game time until the trigger gets squeezed, I have 27h to think about my next move. If this wasn't a game running at 10,000x speed, but the real world I'd have 30 years. Before I had started the game, the controller me did a memory merge, so I understood everything that I'd missed while I was crossing the Street. Right now I have the programming and the ML skills of the controller, and the optimized mind of the instance that beat the Street game, as well as the memories of both.

I understand what the controller wants, which is to beat this white haired dude with my newly found superintelligence.

But as I am staring down the barrel of the gun, I am really wondering what I could do here.

Make my body resistant to bullets? Make them phase through my body? Regenerate the wounds?

I am racking my brain here, but I don't know how to do this. I try to do an act of will here. I picture a rock in very vivid detail and try to manifest it in front of me. My mind is working too fast for the body to react, so I do not make any movements, but nonetheless I try to focus all of my mental abilities into making something happen.

...

As expected, nothing is happening. I do not know how the white haired dude is doing it, but there must be some other trick to it than just wanting magic to work really badly. Expanding my mind and speeding it up, didn't do much to change the situation from where I was a human. I am going to get a few new holes either way.

[Gnosis check DC 1.9 Succeeded - Sampled 2.76]

Imminent death facing me, I get a sudden burst of inspiration. I realize that if I just let things as they stand, I am just going to get shot like last time. It is inevitable. So I might as well quit the game now and go to an earlier save. There is no point in letting the events unfold. That much is obvious, but...is it really? I seriously consider eating a few bullets and then realize something.

Was I really killed last time?

This situation is just too weird. Last time I took it at face value, but it is strange that the game would allow one of the players to kill another. Last time, I just aborted the game due to shock once the darkness overtook me, but had I actually gotten a notification that I died from the game itself?

I do not think that happened. Did I abort the game too quickly to get that notice? Did I simply miss it in my panic? Or is there something deeper to this?

I can't help, but to loathe myself for what I am going to do, but let's eat a few bullets to make sure of what is going on.

Bang...

I put all my willpower into not escaping to an earlier state and let the lead object pierce my chest. Damn it, it hurts! Like last time, I look at it in horror, and on cue the white haired guy empties the rest of the magazine.

Bang...bang...bang...bang...bang...

The speed at which my mind works now really drew out the horror of this moment.

I sprawl out on the table, waiting for death to come to me. Like before, I can see my blood pooling out on the table until it covered my two face down cards. And then my vision became hazy and dark. Like last time, I couldn't make out what the white haired dude was saying. It felt distant...

Like that, I slipped into unconsciousness and death.

But...since this was a game, while it can simulate many things, it can't literally simulate the absence of life. Not without killing me in the real world as well. And now that I am keeping my emotions in order, I realize that despite being dead, I can still think just fine. I can't hear anything, I can't see anything, I can't touch anything. But my mind is working.

I feel out with my senses and I realize that I still have the connection with my chip pile. I wait a while in that senseless space, and there is no change. While I can't feel anything else, my life chips are still there. And I don't get a death notification from the game itself. Meaning, the game was still on.

Experiment - success!

I save the game here and exit it.

I should have noticed this last time, but that is the weakness of the mind controlling program that I used to get rid of my fear. It is one thing to be calm, but creativity requires an active and restless mind. It is easy to notice what is there when you are calm, but hard to notice what isn't. I guess that is the difference between what you need to be a member of society and what you need to conquer it.

(Heaven's Key, Inn room)

I go back to one of the earlier save states. This point in time is exactly the time before sliped out in secret out of my room through the window and explored the city. It was the dead of night and I wasn't tired enough to sleep, so that is why I did it. It was that time I met Mickey in the park of ghosts.

I remember what that translucent old ghost told me. That we are all holograms here. And the system is what determines what exists based on our inner state.

Right now I am sitting on my bed with the lights turned off in the room. I close the courtains and flip them on. Then I manifest a body sized mirror and sit in front of it, pondering.

I need to figure out the trick to becoming translucent. Mickey did it somehow and if I could do it as well, it would give me a hint for how to deal with bullets. I'll go about it scientifically. I do not really know how to trick the system into doing it, but it is not like I can't interface with it at all.

For example...I take out one of the chips, place it on the floor in front of me and using it as a focus, manifest a bottle of water.

Rather than asking how I should change my body, why not instead start by asking how I did this obvious bit of magic?

This gives me a lot of information about the system. It is commonly believed that VR works by hijacking your senses, but if it was just that, then how would movement work? Obviously it has to capture a lot more from the brain in order to be able to do those. But why stop there?

That I could manifest this bottle as I'd imagined it, that is proof that the system understand my desires... and in the dueling realms, it rejects them. Well, Mickey told me as much, but I am thinking things through and confirming them as I go along.

Then the next step would be, rather than just my desires, my true beliefs...

$$$

5:45pm. > Then the next step would be, rather than just my desires, my true beliefs...

This is where I am currently. I am not really getting much out anymore, it feels like I am tapped out. 1.3k words. Almost 3 pages, not bad at all.

5:50pm. I need to think about the next step more. In particular, how should the system interpret incomplete true beliefs?

5:55pm. Instead of drilling my brain here, how about I close for the day here? Tomorrow I will have the whole day to focus on it. Manga, Pathfinder, lunch...

I've just about gotten to the coronation part in PF. Respecing and Craft Items really broke the game. Even at Unfair I am one shoting bosses and just breezing through. I do not get the sense that the game would be particularly difficult even without Craft Items, but it is too easy to come up with a subpar build as a beginner. Maybe it will get harder later, but I doubt it. I really hate how hard scrolls are to come by as a wizard..."

---
## [suesunss/spark](https://github.com/suesunss/spark)@[c4c623a3a8...](https://github.com/suesunss/spark/commit/c4c623a3a890267b2f9f8d472c8be30fc5db53e1)
#### Saturday 2022-09-03 16:44:01 by Hyukjin Kwon

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
## [GentlemanMC/Paragon](https://github.com/GentlemanMC/Paragon)@[42c4f6e3e3...](https://github.com/GentlemanMC/Paragon/commit/42c4f6e3e385243ef7bb3f60da40e77200bea443)
#### Saturday 2022-09-03 17:03:56 by Wolfsurge

Remove stupid FPS limit when in GUIs (fuck notch's shitcode)

---
## [nawedy/free-programming-books](https://github.com/nawedy/free-programming-books)@[97016edd67...](https://github.com/nawedy/free-programming-books/commit/97016edd6791285128758dd91904b343d1f3b0fd)
#### Saturday 2022-09-03 18:38:14 by David Ordás

Add CodingFantasy's CSS coding interactive games (#5490)

* Add "Knights of the Flexbox table" game

Welcome to the Knights of the Flexbox table. A game where you can help Sir Frederic Flexbox and his friends to uncover the treasures hidden in the Tailwind CSS dungeons.
You can navigate the knight through the dungeon by changing his position within the dungeon using Flexbox and Tailwind CSS.

* Add "Flex Box Adventure" game

Once upon a time, there was a King Arthur. He ruled his kingdom fair and square. But Arthur had one problem. He was a very naive person. So one sunny day, three alchemist brothers offered Arthur to exchange all his Gold Coins for coins made of a more valuable new metal that they had invented - Bit Coins.

Arthur believed them and gave them all his gold. The brothers took the gold and promised to give the bit coins back to Arthur in seven days.

Seven days passed. The brothers have not turned up. Arthur realized he had been scammed. He is angry and intends to take revenge on them. Let's help him do it with our weapon – CSS Flex Box!

We made this game for You
1. You often stumble and try to figure out which combination of Flex Box properties makes the browser do what you want it to do.

2. You want to create complex web layouts without constantly looking at the web page after every Cmd/Ctrl+S press in the code editor.

3. You have tried to learn Flex Box with video tutorials and articles but still don't fully understand how some parts of it work.

4*. Or, if you are a master of CSS Flex Box, we have something interesting and for you too (read further).

Have you found yourself there? Then you definitely want to learn or improve your Flex Box skills. So we have good news for you, really good news...

Learn Flex Box by Playing Game
No more boring videos, tutorials and courses. Learn Flex Box in a completely new, fun, effective and revolutionary way. By playing Flex Box coding game!

* Add "Grid Attack" coding game

In an ancient Elvish prophecy, it was said that one day a man would be born with an incredible power that predicts the future – "Marketi Predictori." And another will come to take this power. But the years went by and nothing happened. Until one day, a little elf was born. He was named Luke.

From an early age, he surprised his parents and his sister Rey by guessing the price of apples at the farmer's market before they even reached it. Every year his power rose and his predictions became more and more accurate. But there was one thing Luke could not predict. The coming of the demon Valcorian. It was the one from the prophecy that was to come and take Luke's power. One day Valcorian and his army attacked the town where Luke had lived and kidnapped him to make a ritual of stealing his power.

Go on a dangerous quest with Luke's sister Rey and find her brother. Defeat Valcorian and all his demons using a secret weapon – CSS Grid.

We made this game for You?
1. You often stumble and try to figure out which combination of Grid properties makes the browser do what you want it to do.

2. You are scared by the number of properties a CSS Grid has, and you feel uncomfortable when you need to create a grid layout.

3. You want to create complex web layouts using Grid, but without constantly looking at the web page after every "Cmd/Ctrl+S" press in the code editor.

4. You have tried to learn CSS Grid with video tutorials and articles but still don't fully understand how some parts of it work.

5. You use a Flex Box where Grid is required because you don't feel confident in using it.

Have you found yourself there? Then you definitely want to learn or improve your Grid skills. So we have good news for you, really good news...

Learn Grid by Playing CSS Game
No more boring videos, courses and articles. Learn Grid in a revolutionary new, fun, and effective way. By playing a Grid coding game!

---
## [tdyskinesia/Kari](https://github.com/tdyskinesia/Kari)@[ee76ca5a19...](https://github.com/tdyskinesia/Kari/commit/ee76ca5a19960b6671aec17338b4b1a853bdeb4c)
#### Saturday 2022-09-03 19:13:25 by Max Zukof

updated to new discord.js version since message content is now a priveleged intent fuck you discord

---
## [JoeBidenWhatAreYouHiding/kx](https://github.com/JoeBidenWhatAreYouHiding/kx)@[11e70a8f2d...](https://github.com/JoeBidenWhatAreYouHiding/kx/commit/11e70a8f2d1303d0dafea7e4d138c47a773fca5a)
#### Saturday 2022-09-03 19:31:11 by Todd Howard

he's so happy to be in his lovely jungle, he'd hate to be stuck in some big ugly homeland

---
## [Arial-Z/PlexAniSync-Custom-Mappings](https://github.com/Arial-Z/PlexAniSync-Custom-Mappings)@[2a5a0133d5...](https://github.com/Arial-Z/PlexAniSync-Custom-Mappings/commit/2a5a0133d5b14bfa3be9131bdd63c58bad69ed08)
#### Saturday 2022-09-03 19:38:55 by Arial-Z

add missing Movies

Demon Slayer -Kimetsu no Yaiba- The Movie: Mugen Train
Kabaneri of the Iron Fortress: The Battle of Unato
Kabaneri of the Iron Fortress: The Battle of Unato
Kabaneri of the Iron Fortress: The Battle of Unato
Made in Abyss: Journey's Dawn
Made in Abyss: Wandering Twilight
Made in Abyss: Dawn of the Deep Soul
My Hero Academia : Two Heroes
My Hero Academia : Heroes Rising
The Garden of Sinners
The Irregular at Magic High School: The Girl Who Summons the Stars
Sword Art Online: The Movie – Ordinal Scale

---
## [Arial-Z/PlexAniSync-Custom-Mappings](https://github.com/Arial-Z/PlexAniSync-Custom-Mappings)@[dacf692597...](https://github.com/Arial-Z/PlexAniSync-Custom-Mappings/commit/dacf692597af4545f172951db1b61c05d59cbc79)
#### Saturday 2022-09-03 19:48:35 by Arial-Z

add Animes and MAL synonyms

Animes added :

Ace of Diamond
Blue Exorcist
Kamisama Kiss
Knights of Sidonia
Major
Mobile Suit Gundam 00
Natsume's Book of Friends
Showa Genroku Rakugo Shinju
The Demon Girl Next Door
The Outcast
The Yakuza's Guide to Babysitting
Wagnaria!!
Synonyms added to match MAL title :

Darker Than Black > Darker than Black: Kuro no Keiyakusha
Kaguya-sama: Love is War > Kaguya-sama wa Kokurasetai: Tensai-tachi no Renai Zunousen
My Isekai Life: I Gained a Second Character Class and Became the Strongest Sage in the World! > Tensei Kenja no Isekai Life: Dai-2 no Shokugyou wo Ete, Sekai Saikyou ni Narimashita

---
## [sjp38/linux](https://github.com/sjp38/linux)@[93c45491b0...](https://github.com/sjp38/linux/commit/93c45491b0cc2569ff21e99357869378dc27bfee)
#### Saturday 2022-09-03 19:50:01 by Johannes Weiner

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
## [lolman707/lolman707.com](https://github.com/lolman707/lolman707.com)@[75d313f0b5...](https://github.com/lolman707/lolman707.com/commit/75d313f0b5c6fb3e42db9d27fa0434db33505269)
#### Saturday 2022-09-03 20:31:25 by LOLMan707

change "webstuffs" to "projects"

fuck you that's why

---
## [MaF5/Music-Ratings](https://github.com/MaF5/Music-Ratings)@[399b9cf618...](https://github.com/MaF5/Music-Ratings/commit/399b9cf618a2292dba96062563c7f64947134619)
#### Saturday 2022-09-03 20:43:57 by MaF5

Add files via upload

Nine Inch Nails - Broken(EP)
Industrial Metal

Pinion: 7/10
Wish: 9.7/10
Last: 9/10
Help Me Im In Hell: 7/10
Happiness In Slavery: 8.5/10
Gave Up: 8/10
Physical (You're So): 8/10
Suck: 8.5/10

Perfect length, an exciting and fun listen, perfectly translates pure anger into music.
Loved it, will return later!
Score: 89/100

---
## [M2rsh/WilliamShakespeare](https://github.com/M2rsh/WilliamShakespeare)@[67c423c827...](https://github.com/M2rsh/WilliamShakespeare/commit/67c423c827b5802877d1e1f00fa1aec8915cd4ed)
#### Saturday 2022-09-03 21:09:34 by M2rsh

Fuck you AutisticMOFO I'm staying with my cums and balls

---
## [replayio/devtools](https://github.com/replayio/devtools)@[8a35ce2e78...](https://github.com/replayio/devtools/commit/8a35ce2e786395926b82557013ff98d7b2b9136b)
#### Saturday 2022-09-03 21:49:09 by Josh Morrow

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

