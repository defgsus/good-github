## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-06-25](docs/good-messages/2022/2022-06-25.md)


1,482,339 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,482,339 were push events containing 2,006,340 commit messages that amount to 115,236,856 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 36 messages:


## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[8f0df7816b...](https://github.com/tgstation/tgstation/commit/8f0df7816bae3c5dedf599611cda3e6039024e14)
#### Saturday 2022-06-25 00:02:38 by Kylerace

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
## [hexagon-geo-surv/linux-stable-rt](https://github.com/hexagon-geo-surv/linux-stable-rt)@[226b3c797c...](https://github.com/hexagon-geo-surv/linux-stable-rt/commit/226b3c797c6246e14c713d048cdb3490a1f67701)
#### Saturday 2022-06-25 00:27:54 by Vasily Averin

mm, oom: pagefault_out_of_memory: don't force global OOM for dying tasks

commit 0b28179a6138a5edd9d82ad2687c05b3773c387b upstream.

Patch series "memcg: prohibit unconditional exceeding the limit of dying tasks", v3.

Memory cgroup charging allows killed or exiting tasks to exceed the hard
limit.  It can be misused and allowed to trigger global OOM from inside
a memcg-limited container.  On the other hand if memcg fails allocation,
called from inside #PF handler it triggers global OOM from inside
pagefault_out_of_memory().

To prevent these problems this patchset:
 (a) removes execution of out_of_memory() from
     pagefault_out_of_memory(), becasue nobody can explain why it is
     necessary.
 (b) allow memcg to fail allocation of dying/killed tasks.

This patch (of 3):

Any allocation failure during the #PF path will return with VM_FAULT_OOM
which in turn results in pagefault_out_of_memory which in turn executes
out_out_memory() and can kill a random task.

An allocation might fail when the current task is the oom victim and
there are no memory reserves left.  The OOM killer is already handled at
the page allocator level for the global OOM and at the charging level
for the memcg one.  Both have much more information about the scope of
allocation/charge request.  This means that either the OOM killer has
been invoked properly and didn't lead to the allocation success or it
has been skipped because it couldn't have been invoked.  In both cases
triggering it from here is pointless and even harmful.

It makes much more sense to let the killed task die rather than to wake
up an eternally hungry oom-killer and send him to choose a fatter victim
for breakfast.

Link: https://lkml.kernel.org/r/0828a149-786e-7c06-b70a-52d086818ea3@virtuozzo.com
Signed-off-by: Vasily Averin <vvs@virtuozzo.com>
Suggested-by: Michal Hocko <mhocko@suse.com>
Acked-by: Michal Hocko <mhocko@suse.com>
Cc: Johannes Weiner <hannes@cmpxchg.org>
Cc: Mel Gorman <mgorman@techsingularity.net>
Cc: Roman Gushchin <guro@fb.com>
Cc: Shakeel Butt <shakeelb@google.com>
Cc: Tetsuo Handa <penguin-kernel@i-love.sakura.ne.jp>
Cc: Uladzislau Rezki <urezki@gmail.com>
Cc: Vladimir Davydov <vdavydov.dev@gmail.com>
Cc: Vlastimil Babka <vbabka@suse.cz>
Cc: <stable@vger.kernel.org>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

---
## [zeeb92/tgstation](https://github.com/zeeb92/tgstation)@[9428d97a4f...](https://github.com/zeeb92/tgstation/commit/9428d97a4fadf8a486b0c6fbe2ee345a2780e687)
#### Saturday 2022-06-25 00:38:07 by Imaginos16

[MDB IGNORE] The Tilening V2 - Damaged Tile Overlays Edition (#67761)


About The Pull Request

Hello once more! As we near summer, I continued to reminisce on several PRs done throughout last year! One of them was the controversial, but rather positive Tilening V1, as done by me and Twaticus a while back (#58932), and felt I could've done a better job with how it was presented.

And thus, thanks to @Fikou encouraging me with a very interesting find of a previous tile resprite attempt, I've successfully done it!

Ladies and Gentlemen, I present to you all, Tilening Version Two!
image

Now this isn't your run of the mill tile resprite. While I did improve the appearance of several tiles I haven't touched last time (including the showroom/freezer tiles now), I decided to do something special that most mappers shall appreciate!

Don't you hate it when of all damaged states, there's only ones for grey tiles when we have white, black, terracotta and a bunch of other materials? Don't you wish they were overlays instead?

Well golly gee do I have good news for you!
image
image

After painstakingly spending at least several hours trying to learn enough code to pull it off, I have successfully made it so most tiles display transparent versions of damage overlays over them! This means mappers can express their creativity that much better! And thanks to how the code is written, its super easy to snowflake certain tile types to make them use unique damaged states (looking at you wooden tiles), so fret not in that aspect.

Credits to:
@WJohn For actually making those damaged overlays! Wouldn't've done the PR if it wasn't for you.
@dragomagol, @RigglePrime and @LemonInTheDark for helping me out in a VC at 10 PM to 12 AM troubleshooting the code to make this improvement work!
Why It's Good For The Game

The shading is done better as compared to last time, making them feel more cubical and less like a pancake when seen from above! This PR also makes it so that we never ever have to touch damaged tiles ever again potentially, saving up some RSC regarding icons.

However, due to how damaged tiles are currently mapped in, rather than overlayed as I envision in the future, it'll require a PR by San to be merged later that should make it safe to remove these icons.
Changelog

cl PositiveEntropy, WJohnston, Dragomagol, LemonInTheDark, Riggle
imageadd: Resprites most variety of tiles into a better shaded version!
code: Damaged floors are now damaged overlays, meaning that most tiles should properly display a damaged state!
/cl

---
## [AirSkyBoat/AirSkyBoat](https://github.com/AirSkyBoat/AirSkyBoat)@[ccf500070d...](https://github.com/AirSkyBoat/AirSkyBoat/commit/ccf500070d4448d1e2acbdb711190d5b4e21c4e6)
#### Saturday 2022-06-25 00:46:03 by neuromancerxi

Add scripts and adjust plumbing for many temp items (#670)

* Add scripts and adjust plumbing for many temp items

Adds Scripts for items.
Adds Effect scripts for X_BOOST_II
Updates Effect scripts for the following:

ACCURACY_BOOST
ATTACK_BOOST
INTENSION
MAGIC_SHIELD
MULTI_STRIKES
MULTI_SHOTS
PAX
PHYSICAL_SHIELD
POTENCY
RAMPART

Adjusts item_usable use times to 1s.

Notes on effects:

Ascetics Tonic/Gambir - +25/+50 MATT/MACC
A big Thank You to Nyu for confirming the Intension effect for MACC.
https://www.bg-wiki.com/bg/Ascetic's_Tonic
https://www.bg-wiki.com/bg/Ascetic's_Gambir

Bravers Drink - +15 to All Stats
https://www.bg-wiki.com/bg/Braver's%20Drink
Reference to Icons/Effects - https://youtu.be/JYT5a_pTA3o?t=20

Champions Tonic - +15 Haste / +3 Crit rate
Champions Drink/Gambir - +18 Haste / +5% Crit rate
Expected Haste effect to be Magic pool based on BG comment (18 and 15)
Critical Hit rate, no data available from community sources, conservative value of 5 (Drink/Gambir) 3 (Tonic)
Both BG and 'clopedia sources confirm Critical Hit Rate (as does the effect description), however, only BG has a reference to Haste value.
https://www.bg-wiki.com/bg/Champion's_Tonic

Gnostics Drink - Enmity -10
No community resources confirm this value, using SCH Animus Minuo as an reference.
https://www.bg-wiki.com/bg/Gnostic's%20Drink
https://www.bg-wiki.com/bg/Animus_Minuo

Monarchs Drink - Regain +3 (30/1000 per tick) for 3 minutes.
https://www.bg-wiki.com/bg/Monarch's_Drink

Stalwart's Tonic/Gambir - ACC/RACC 50/100 ATTP/RATTP 25/50
A big Thank You to Nyu for confirming the effects apply ACC/RACC and ATTP/RATTP across two effects.
https://www.bg-wiki.com/bg/Stalwart's_Tonic
https://www.bg-wiki.com/bg/Stalwart's_Gambir

Berserker's Tonic/Drink - DA 50/100
Thanks to Nyu for confirming the MULTI_STRIKES effect and 1m duration.
https://ffxiclopedia.fandom.com/wiki/Berserker%27s_Drink
No full data on DA rate, minus 'clopedia which has verification tags. Working on the expectation that this follows a good portion of the other items and follows the half potency values for the lesser item.

Swiftshot Tonic/Drink - Double Shot 50/100
https://www.ffxiah.com/forum/topic/28603/fools-tonic-broken#1749569

Dusty Scroll of Reraise - Reraise III, 10m duration.
https://www.bg-wiki.com/bg/Dusty_Reraise

Spiritual Incense/Fools Drink/Tonic/Powder: See effects/magic_shield
Carnal Incense/Fanatics Drink/Tonic/Powder: See effects/physical_shield

* Removed copypasta subp and trailing whitespace.

* Item script clean-up and move effect functions to item_utils.

* Resolve Conflicts

Convert namespace in scripts from item_utils to xi.item_utils
PHYS_ABSORB to Percent from 10000 Scale

---
## [jupyterkat/Pariah-Station](https://github.com/jupyterkat/Pariah-Station)@[fb13b0e4ff...](https://github.com/jupyterkat/Pariah-Station/commit/fb13b0e4ff4a8957f2837adf7ba06ae2eb388bf8)
#### Saturday 2022-06-25 01:18:00 by PariahBot

[MIRROR] Vim mecha changes (#541)

* Vim mecha changes (#66153)

This PR changes the following:

    fixes a bug with Vim overlays, making it always appear as if there was a pilot inside, even after leaving it
    adds a balloon alert when a mob fails to enter the mech due to its size
    adds a crafting recipe for Vim in the "robots" category
    allows using Vim as a circuit shell
    allows small mobs to use the mech as well

My reasoning behind the changes:

    fixing the overlay bug - bugfixes good, bugs bad
    balloon alert - it should help reduce confusion among players who can't figure why on earth they cannot enter the mech
    crafting recipe - I think a crafting recipe will make it a lot more accessible to players, especially because there is no way to learn about its existence in-game
    circuit shell - non-standard circuit shells can be pretty fun and people seemed to enjoy the ability to use circuits inside their piano synths or cameras, so I figured we could expand on this, while giving players more ways to interact with sentient pets
    maximum mob size increase - Vim has never really been built too often, most likely because even if people got their hands on a sentient pet, it wouldn't probably fit in the tiny mecha anyway. Currently pretty much only butterflies, rats and cockroaches can use Vim and they pretty much never become sentient.

* Vim mecha changes

Co-authored-by: B4CKU <50628162+B4CKU@users.noreply.github.com>
Co-authored-by: Debian <debian@packer-output-01d6f1be-59bf-4994-80ec-c61b12fe30e1>

---
## [treacherousfiend/LightmapUtil](https://github.com/treacherousfiend/LightmapUtil)@[11dc418b8b...](https://github.com/treacherousfiend/LightmapUtil/commit/11dc418b8b74a0f0d131a13be05bc9199520c88b)
#### Saturday 2022-06-25 01:38:18 by treacherousfiend

change license (again)

haha unlicense is public domain but not really so i'm using cc0 now.

i fucking hate all of this copyright bullshit just let people use my code

---
## [TheBoondock/tgstation](https://github.com/TheBoondock/tgstation)@[763a10d1cc...](https://github.com/TheBoondock/tgstation/commit/763a10d1cc44c91720101d422d8709ad1aa0644d)
#### Saturday 2022-06-25 01:52:20 by distributivgesetz

Resonance cascade polishening, bugfixes and better logging (#67488)

This PR rewrites almost all messages related to cascade events. Some messages felt kinda clunky to read or could have been written better. Overall, the new messages add to the experience as a cascade being a terrifying event in a way that I felt the old ones missed, and they make the event feel overall a lot sharper.

While looking at the resonance cascade code, I noticed that there a lot of stuff about cascades in the air which was not touched on. So, as I do, this PR evolved into a polish and roundup PR for cascades. There was a lot of stuff still hanging out relating to the event, and although the big backend of it sits, there was still a bit left to be completed. Therefore this PR deserves more the title of the "Resonance cascade POLISHENING" instead of the "REFLAVAHRING". But yeah, you ever go on a massive tangent before?

---
## [newstools/2022-los-angeles-times](https://github.com/newstools/2022-los-angeles-times)@[b8818dc722...](https://github.com/newstools/2022-los-angeles-times/commit/b8818dc72247b83246ce1773bd0c57c76307bce6)
#### Saturday 2022-06-25 02:35:00 by Billy Einkamerer

Created Text For URL [www.latimes.com/entertainment-arts/music/story/2022-06-24/dove-cameron-boyfriend-breakfast-disney-queer]

---
## [Kostucha616/bild](https://github.com/Kostucha616/bild)@[949fbd0194...](https://github.com/Kostucha616/bild/commit/949fbd019404b32fded90f37e3f6a7548790e55e)
#### Saturday 2022-06-25 02:42:20 by Emisse

Bagel Update 13.7 (#8690)

* fuck shit ass shit

* Add files via upload

---
## [RoadrunnerWMC/Reggie-Updated](https://github.com/RoadrunnerWMC/Reggie-Updated)@[ba84351fc9...](https://github.com/RoadrunnerWMC/Reggie-Updated/commit/ba84351fc9d69546a4bc5454be1a8915cb02f0b8)
#### Saturday 2022-06-25 02:58:32 by RoadrunnerWMC

Allow putting tilesets in ../Tilesets

I hate adding NewerSMBW-specific hacks to Reggie, but given that this is a widespread annoyance and I'm not planning on ever implementing a more proper solution (i.e. loading Riivo patches instead of raw Stage folders)... this is a good enough compromise

---
## [chazizgrkb/heelercrap-node](https://github.com/chazizgrkb/heelercrap-node)@[9dbdb8dccd...](https://github.com/chazizgrkb/heelercrap-node/commit/9dbdb8dccd5b94f51f0315729114ea3eebfb828d)
#### Saturday 2022-06-25 03:52:16 by Chaz "Gamerappa" Péloquin

bring some of the shit back

also just make every auth attempt valid because fuck you

---
## [bambitheone82112/Haxe-File](https://github.com/bambitheone82112/Haxe-File)@[1e8d0fd79b...](https://github.com/bambitheone82112/Haxe-File/commit/1e8d0fd79b3a6504932fe285a09ec285d9e73f08)
#### Saturday 2022-06-25 04:00:27 by imliterallydanishlol

gggggrrrrr i hate that bitch making this stupid fucking dumb idiot i deleted >:((((((

fuck yopu bitches

---
## [shermanCRL/cockroach](https://github.com/shermanCRL/cockroach)@[0a3447944a...](https://github.com/shermanCRL/cockroach/commit/0a3447944ae259b725ebff7d84cecd1b6a1de19c)
#### Saturday 2022-06-25 04:07:00 by craig[bot]

Merge #80894 #81200 #81330 #81406

80894: build,gcp: enable nightly config to run GCP unit tests r=adityamaru a=adityamaru

Previously, the `pkg/cloud/gcp` tests package was skipped on CI
because most of the tests require credentials, and we risked exfiltration
of these secrets when running on public teamcity agents.

With the ability to run tests on agents that are not part of the public
pool we now have a `Cloud Unit Test` config that runs these tests nightly.
This change adds the script invoked by the config and cleans up the unit
tests to be more uniform in their authentication and environment variable
checks.

Informs: https://github.com/cockroachdb/cockroach/issues/80877

Release note: None

81200: ui: Improve time picker keyboard input r=jocrl a=jocrl

Fixes #80655, mostly.

Previously, users had to type `1:03 PM (UTC)` in order to enter text into the time picker.

This commit modifies the time picker so that users would instead type either
- `1:03`, or
- `01:03`

to enter text into the time picker. Copying and re-pasting the text from a time picker still works.

Alternate approaches not pursued (these are not needed with the removal of AM/PM).

1) Make our own time picker component, and style it to look like antd's. There's
a general issue of antd's components not being keyboard friendly:
https://github.com/ant-design/ant-design/issues/5685

2) Upgrade to `antd` version 4, and use an undocumented prop type. `antd`'s time
picker uses the time picker from the `rc-picker` library under the hood. In
`rc-picker`, the `format` prop is of type `String | String[]`, where if it's an
array the first value will be used for display and the remaining ones will be
used for parsing, as documented [here](https://react-component.github.io/picker). In theory, `antd` passes `format`
(and also any remaining, additional props in addition to the specified ones) to
the `rc-picker` component. So even though the `antd` `TimePicker` component
`format` prop is not documented to take in a string array, one might think that
passing in a string array anyway would work. In practice, passing in a string
array works in `antd` version `4.20.4`, as tested in the [antd sandbox](https://ant.design/docs/react/getting-started) 
(render `<TimePicker format={
["h:mm A", "h:mma"]}/>`). However, this does not work in our codebase
(which installs `antd` `v3.25.2`), or in the `antd` version `3.x` [sandbox](https://3x.ant.design/docs/react/getting-started). The errors that appear in
these two situations are different, and in a way demonstrate the potential for
breakage from using an undocumented feature in future upgrades from a version
that we've to work. If we do this, we should add a test.

3) Dead end: The `antd` `TimePicker` component takes an `onChange` prop with a
second `timeString` paramater. However, `onChange` only fires if the input is
of the correct, parsable format. The specific code that ignores text input that
is not of a parsable format is in `rc-picker`, [here](https://github.com/react-component/picker/blob/5306c8938aded49c5d6f6b6d4761ddab25e3cce9/src/Picker.tsx#L237).
This prevents us from being the one to do the fuzzy matching and passing the
value back to the component.

Release note (ui): The time picker component has been improved such that users
can use keyboard input to select a time without having to type `" (UTC)"`

81330: authors: add annrpom to authors r=annrpom a=annrpom

Release note: None

81406: geomfn: check NaN coordinates for ST_MinimumBoundingCircle r=rafiss a=otan

Resolves #81277

Release note (bug fix): Fix a bug where ST_MinimumBoundingCircle with
NaN coordinates could panic.

Co-authored-by: Aditya Maru <adityamaru@gmail.com>
Co-authored-by: Josephine Lee <josephine@cockroachlabs.com>
Co-authored-by: Annie Pompa <annie.pompa@cockroachlabs.com>
Co-authored-by: Oliver Tan <otan@cockroachlabs.com>

---
## [mamh-mixed/microsoft-terminal](https://github.com/mamh-mixed/microsoft-terminal)@[8962f88f90...](https://github.com/mamh-mixed/microsoft-terminal/commit/8962f88f907d86fd8684b66f7f3e32a2709e3237)
#### Saturday 2022-06-25 04:10:25 by Dustin L. Howett

Disable the VT color quirk for pwsh and modern inbox powershell (#13352)

In #6810, we introduced a "quirk" for all known versions of PowerShell
that suppressed their requests for black background/gray foreground.
This was done to avoid an [issue in PSReadline] where it would paint
black bars all over the screen if the default background color wasn't
the same as the ANSI black color.

Years have passed since that quirk was introduced. The underlying bug
was fixed, and the fix was released broadly long ago. It's time for us
to remove the quirk... almost.

Terminal still runs on versions of Windows that ship a broken version of
PSReadline. We must maintain the quirk there -- the user can't do
anything about it, and we would make their experience worse if we
removed the quirk entirely.

PowerShell 7.0 also ships a broken version of PSReadline. It is still in
support for another 6 months, but updates have been available for some
time. We can encourage users to update.

Therefore, we only need the quirk for Windows PowerShell, and then only
for specific versions of Windows.

_Inside Windows_, we don't even need that: we're guaranteed to be built
alongside a fixed version of PowerShell!

Closes #6807

[issue in PSReadline]: https://github.com/PowerShell/PSReadLine/issues/830#issuecomment-650508857

---
## [mamh-mixed/microsoft-terminal](https://github.com/mamh-mixed/microsoft-terminal)@[9ccd6ecd74...](https://github.com/mamh-mixed/microsoft-terminal/commit/9ccd6ecd744890b856f3d8a39ff0616c0e34d4fb)
#### Saturday 2022-06-25 04:10:29 by Mike Griese

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
## [mamh-mixed/microsoft-terminal](https://github.com/mamh-mixed/microsoft-terminal)@[442432ea15...](https://github.com/mamh-mixed/microsoft-terminal/commit/442432ea15241a3e9ee3d70c5c24e5565655e55b)
#### Saturday 2022-06-25 04:10:56 by Mike Griese

Fixes the wapproj fast-up-to-date check (#11806)

I'm working on making the FastUpToDate check in Vs work for the Terminal project. This is one of a few PRs in this area.

FastUpToDate lets vs check quickly determine that it doesn't need to do anything for a given project. 

However, a few of our projects don't produce all the right artifacts, or check too many things, and this eventually causes the `wapproj` to rebuild, EVERY TIME YOU F5 in VS. 

This third PR deals with the Actual fast up to date check for the CascadiaPackage.wapproj. When #11804, #11805 and this PR are all merged, you should be able to just F5 the Terminal in VS, and then change NOTHING, and F5 it again, without doing a build at all. 




The wapproj `GetResolvedWinMD` target tries to get a winmd from every cppwinrt
executable we put in the package. But we DON'T produce a winmd. This makes the
FastUpToDate check fail every time, and leads to the whole wapproj build
running even if you're just f5'ing the package. EVEN AFTER A SUCCESSFUL BUILD.

Setting GenerateWindowsMetadata=false is enough to tell the build system that
we don't produce one, and get it off our backs.

### teams chat where we figured this out

[3:38 PM] Dustin Howett
however, that's not the only thing that "GetTargetPath" checks.

[3:38 PM] Dustin Howett
oh yeah more info: wapproj calls GetTargetPath on all projects it references

[3:38 PM] Dustin Howett
when it calls GTP on WindowsTerminal.vcxproj it is getting back a winmd (!)


[3:39 PM] Dustin Howett
here's the magic

[3:39 PM] Dustin Howett
![image](https://user-images.githubusercontent.com/18356694/142945542-74734836-20d8-4f50-bf3a-be4e1170ae13.png)


[3:39 PM] Dustin Howett
it checks if any Link items specify GenerateWindowsMetadata

![image](https://user-images.githubusercontent.com/18356694/142945593-fd232243-0175-4653-8c34-cdc364a16031.png)

---
## [Zonespace27/Skyrat-tg](https://github.com/Zonespace27/Skyrat-tg)@[a3c0819e80...](https://github.com/Zonespace27/Skyrat-tg/commit/a3c0819e8091ab99a5ab8f53b59c4687e5b2f2cf)
#### Saturday 2022-06-25 05:12:43 by SkyratBot

[MIRROR] Removes (in) smoke and foam reactions [MDB IGNORE] (#13963)

* Removes (in) smoke and foam reactions (#67270)

* Removes smoke and foam reactions

Turns out when you let reagents react in foam/smoke, people put bombs in
them.

This behavior was initially added to just smoke, accidentially in
(56f7ac0c0a29e8f898c4aab35947d027952b43f7) accidentialy (thalpy tried to
make both foam and smoke instant react, but instead made smoke's temporary
holder reagent instant instead. hhhhhhh)

Assuming this was intentional it was then extended to foam in
(1879e2d338c9bf5f191cef6c39944b26a41e6092)

Basically, we're idiots. Anyway lets just walk this all back to instant
reaction on smoke/foam formation. Hate you people

* Removes another source of gunpowder smoke

Temporal told me about this. Gunpowder uses an ex_act signal as a
starter, and that also counts for smoke objects.

Really don't want instant detonation smoke bombs, so let's just... not
shall we?

* Removes (in) smoke and foam reactions

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [darshan-/PurpOS](https://github.com/darshan-/PurpOS)@[0b502ccc58...](https://github.com/darshan-/PurpOS/commit/0b502ccc584a776087276cb4b84955cc25940be9)
#### Saturday 2022-06-25 06:19:39 by Darshan-Josiah Barber

If I put the value in r8 first, then move from r8 to rax letter, I'm good... which is super weird.  And confusing.  I definitely don't understand it.  It definitely seems wrong.  Setting rsp shouldn't change how the address is...  Hmmmmmmmm.  Hmm.  Is GCC storing it on the stack still, because that's how I passed it in?  Hmm, well, this was starting to make a lot of sense, until... Oh, maybe it still does!  Making a new variable still has the same issue... but it's not a heap-allocated variable.  It's literally on the stack, and I literally can't access it anymore once I change rsp.  Okay, thank God, this finally makes sense.  And goes from frustrating and annoying to kinda cool to have had to wrestle with.  Okay, still committing, before I figure out how I actually want to do things, now that I understand what's going on.  What a relief!  Phew!

---
## [SweetBlueSylveon/Shiptest](https://github.com/SweetBlueSylveon/Shiptest)@[9b53b27b3c...](https://github.com/SweetBlueSylveon/Shiptest/commit/9b53b27b3c0e91a3e49f66d07dfc9b40d6e82350)
#### Saturday 2022-06-25 08:28:41 by SweetBlueSylveon

Adds a bunch of shit

-Fuck you
-They're the power rangers
-Science ship???
-Ignore the honksquad suit it isn't real

---
## [pkviet/cef](https://github.com/pkviet/cef)@[aac40ab280...](https://github.com/pkviet/cef/commit/aac40ab280db23e96a6ca778ad5d43582c5cc36a)
#### Saturday 2022-06-25 09:35:28 by Jim

Legendary 4638 shared texture perf improvement

This fixes remaining performance and frame pacing issues when using CEF
95 with texture sharing on Windows. I hacked Chromium internally to
treat shared textures similarly to how the 3770 method worked.

Let me document my little adventure.

First, we were getting system freezes, and from analysis of the
bluescreen dumps, they were always during synchronization, so I had a
hunch: "are keyed mutexes doing this?" The system freeze issue left me
hopeless. I already had a disdain for the stupid keyed mutexes, and due
to my immense hatred of them, I was angry and I just wanted to try
removing them, because 1.) What if they were the cause? (They were), and
2.) I hated them anyway. It was an irrational vendetta, and I was on a
war path to remove them just in the *slightest* chance that those god
forsaken keyed mutexes were the cause.

So I got angry and decided to remove them from almost everything in
Chromium just to see if it would fix the system freeze issue. I removed
their usage from almost everything in Chromium related to GLImageDXGI.

Let me go on a rant about keyed mutexes. I hate keyed mutexes. I *want*
synchronization between devices, but what I *don't* want is to be forced
to swap stupid "keys" between the two devices; especially if you're in a
situation where you cannot pass the next key value to the next device so
the next device knows what key to use, because then, the original device
can no longer lock the object anymore, and the object is completely
forfeit. Then you get suck in a situation where you're forced to wait
infinitely if you have no way of telling the other device to use the
correct key. I wish I could suggest a better design, but all I know is
that I hate it, it's an insufferable design as it is right now, and I
don't think there's a single human being on the planet who will ever
convince me otherwise. Absolutely insufferable design. I've always hated
them and always will.

Anyway, sorry about that. Like I was saying, I removed keyed mutex usage
from texture sharing inside chromium. But the problem is that with the
4638 version of shared textures, it was about 5 textures which were used
round-robin. Because we were forced to remove keyed mutexes (which were
crashing the entire system), we could no longer synchronize between
client and Chromium, thus frame pacing issues were introduced. Even
flushing wasn't helping. They weren't noticeable, and we were *almost*
just going to use it as it, but I decided I wasn't finished with my war
path.

I had fixed the system freeze issue by removing keyed mutexes, but now
there was this frame pacing issue. So, I was upset, and I tried many
different techniques to try to synchronize. Flushing, more textures,
less textures, trying to adjust timing; I thought it was hopeless, until
I started looking at the 3770 version and started looking around
4638 code for ways I could do the same thing. I had already removed
keyed mutex objects from GLImageDXGI objects, but then I realized: what
if I just add the same staging/CopyResource method 3770 did, and then
just use one shared texture? 3770 worked amazingly well, so why not try
it? Through much toil and experimentation, I got it working.

However, there was still one annoying caveat. Because of the fact that
Chromium now only deals with NT-style HANDLE objects for shared
textures, it would duplicate handles every time it was passed. There was
no way of detecting whether we were already using the same shared
texture (and CompareObjectHandles in KernelBase didn't work), so we had
to recreate the stupid texture object every time. So I introduced a new
OnAcceleratedPaint2 function specifically to specify whether the texture
has been changed -- that way we don't need to have to continually keep
recreating the god-forsaken texture object.

All these things combined has won us a huge victory, not only did we
solve the system freeze issue, but we also reduced the amount of
resources being used from the original version by removing the round
robin, eliminated frame pacing issues, and improved the perf back to
3770 levels. In fact, I'm pretty sure that perf levels are even better
than they were even with the keyed mutex version (if they weren't
causing stupid system freezes), because the keyed mutex version forced
INFINITE lock durations due to the inability to relay keys.

After 27.2 had this issue, I had to delay the release, and I spent a
week toiling over this. To get the system freeze issue fixed, and then
to get perf levels back to 3770 levels. And I did it by sifting through
millions of lines of Chromium code.

Needless to say I feel really damn good right now. This was a legendary
fix. I'm sorry, I need a little bit of ego just for once. I feel like
I've earned it.

---
## [GeoB99/reactos](https://github.com/GeoB99/reactos)@[989e66173c...](https://github.com/GeoB99/reactos/commit/989e66173c460e1cfcf8d58c937672d2e8c4c9b5)
#### Saturday 2022-06-25 10:12:37 by George Bișoc

[NTOS:SE] Properly handle dynamic counters in token

On current master, ReactOS faces these problems:

- ObCreateObject charges both paged and non paged pool a size of TOKEN structure, not the actual dynamic contents of WHAT IS inside a token. For paged pool charge the size is that of the dynamic area (primary group + default DACL if any). This is basically what DynamicCharged is for.
For the non paged pool charge, the actual charge is that of TOKEN structure upon creation. On duplication and filtering however, the paged pool charge size is that of the inherited dynamic charged space from an existing token whereas the non paged pool size is that of the calculated token body
length for the new duplicated/filtered token. On current master, we're literally cheating the kernel by charging the wrong amount of quota not taking into account the dynamic contents which they come from UM.

- Both DynamicCharged and DynamicAvailable are not fully handled (DynamicAvailable is pretty much poorly handled with some cases still to be taking into account). DynamicCharged is barely handled, like at all.

- As a result of these two points above, NtSetInformationToken doesn't check when the caller wants to set up a new default token DACL or primary group if the newly DACL or the said group exceeds the dynamic charged boundary. So what happens is that I'm going to act like a smug bastard fat politician and whack
the primary group and DACL of an token however I want to, because why in the hell not? In reality no, the kernel has to punish whoever attempts to do that, although we currently don't.

- The dynamic area (aka DynamicPart) only picks up the default DACL but not the primary group as well. Generally the dynamic part is composed of primary group and default DACL, if provided.

In addition to that, we aren't returning the dynamic charged and available area in token statistics. SepComputeAvailableDynamicSpace helper is here to accommodate that. Apparently Windows is calculating the dynamic available area rather than just querying the DynamicAvailable field directly from the token.
My theory regarding this is like the following: on Windows both TokenDefaultDacl and TokenPrimaryGroup classes are barely used by the system components during startup (LSASS provides both a DACL and primary group when calling NtCreateToken anyway). In fact DynamicAvailable is 0 during token creation, duplication and filtering when inspecting a token with WinDBG. So
if an application wants to query token statistics that application will face a dynamic available space of 0.

---
## [BakKeener/Paradise](https://github.com/BakKeener/Paradise)@[6082c95eb3...](https://github.com/BakKeener/Paradise/commit/6082c95eb300a9f05b5422060db79f55fe91b9b3)
#### Saturday 2022-06-25 11:49:21 by LightFire53

Relocates The Entertainment Offices and Custodial Closet on DeltaStation (#17480)

* Location, Location, Location!

* Lights and Pipes

I am so sorry for how hacky that disposal piping is

* TFW Disposals

* Oh god, what if there is a fire?!

* And a light switch...

Maybe the final commit? Taking bets on if I managed to forget something else

* If you bet on the requests console

You would be right.

* Bigger, Better, Janitor

* Bloody requests console...

---
## [newstools/2022-the-irish-times](https://github.com/newstools/2022-the-irish-times)@[2494b00891...](https://github.com/newstools/2022-the-irish-times/commit/2494b0089170e428e20712330d3b1b7314562853)
#### Saturday 2022-06-25 12:25:47 by Billy Einkamerer

Created Text For URL [www.irishtimes.com/opinion/2022/06/25/fintan-otoole-the-great-social-revolution-of-the-last-30-years-may-have-made-life-better-for-most-people-but-not-less-fretful/]

---
## [christinahansen/marvyaql](https://github.com/christinahansen/marvyaql)@[d679c4f82b...](https://github.com/christinahansen/marvyaql/commit/d679c4f82bea89245f8f2c67104b3e1154e7e4f8)
#### Saturday 2022-06-25 14:14:31 by christinahansen

https://doxbin.net/upload/MarvelousAQL  T h e  F a l l  o f  N a t h a n  A n d e r s o n __________________________________________________   Vid proof: https://www.youtube.com/watch?v=i2N7FXBenck Dox reason: Marvy gets caught grooming a child, resorts to "kill yourself" and "fuck you" as his only comebacks  =x=x=x= His info  Full Name: Nathan "Nate" Riley Anderson Relatives: Travis Anderson : https://open.spotify.com/user/1286111676 Location: Minnesota, United States  Fetishes: Inflation fetish, fat chick fetish, BBW, fart fetish.  Steam: https://steamcommunity.com/profiles/76561198307666783 Discord: MommaMarvyAQL2020#2533 | 242042408907440129 Facebook: https://www.facebook.com/syfimaster2020 BattleNET: Mommarvyaql#1591 Reddit: https://www.reddit.com/user/animefan2020 Github: https://github.com/nathanbb2020 Spotify: https://open.spotify.com/user/outlawnathan Twitter: https://twitter.com/MommaMarvy | 3141844258 Youtube: https://www.youtube.com/channel/UC-osWzEM3t9tf96cPDTnhww/about Twitch: https://www.twitch.tv/nekookaasanmarvy Xbox Live: syfimaster2020  =x=x=x= PC Information/Metasploit info:  ISP:                        Broadcom Device name:                BiosStar-I7-Nate Processor                   Intel(R) Core(TM) i7-2600K CPU @ 3.40GHz   3.40 GHz RAM                         16.0 GB Device ID                   B6410442-D855-4F6E-ADFB-68C00D12CA69 Product ID                  00326-10000-00000-AA648 System type                 64-bit operating system, x64-based processor Pen and touch               No pen or touch input is available for this display Display                     MSI NVIDIA 750 GTX   =x=x=x= Alternate Aliases and names:   Nathan Anderson nathanbb2020 animefan2020 outlawnathan nateanderson1105 nekookaasanmarvy MommaMarvy Nathan Anderson

https://doxbin.net/upload/MarvelousAQL

T h e  F a l l  o f  N a t h a n  A n d e r s o n
__________________________________________________


Vid proof: https://www.youtube.com/watch?v=i2N7FXBenck
Dox reason: Marvy gets caught grooming a child, resorts to "kill yourself" and "fuck you" as his only comebacks

=x=x=x= His info

Full Name: Nathan "Nate" Riley Anderson
Relatives: Travis Anderson : https://open.spotify.com/user/1286111676
Location: Minnesota, United States

Fetishes: Inflation fetish, fat chick fetish, BBW, fart fetish.

Steam: https://steamcommunity.com/profiles/76561198307666783
Discord: MommaMarvyAQL2020#2533 | 242042408907440129
Facebook: https://www.facebook.com/syfimaster2020
BattleNET: Mommarvyaql#1591
Reddit: https://www.reddit.com/user/animefan2020
Github: https://github.com/nathanbb2020
Spotify: https://open.spotify.com/user/outlawnathan
Twitter: https://twitter.com/MommaMarvy | 3141844258
Youtube: https://www.youtube.com/channel/UC-osWzEM3t9tf96cPDTnhww/about
Twitch: https://www.twitch.tv/nekookaasanmarvy
Xbox Live: syfimaster2020

=x=x=x= PC Information/Metasploit info:

ISP:                        Broadcom
Device name:                BiosStar-I7-Nate
Processor                   Intel(R) Core(TM) i7-2600K CPU @ 3.40GHz   3.40 GHz
RAM                         16.0 GB
Device ID                   B6410442-D855-4F6E-ADFB-68C00D12CA69
Product ID                  00326-10000-00000-AA648
System type                 64-bit operating system, x64-based processor
Pen and touch               No pen or touch input is available for this display
Display                     MSI NVIDIA 750 GTX


=x=x=x= Alternate Aliases and names: 

Nathan Anderson
nathanbb2020
animefan2020
outlawnathan
nateanderson1105
nekookaasanmarvy
MommaMarvy
Nathan Anderson

---
## [Pixel-Pro-Inc/RodizioExpressDesktopApp](https://github.com/Pixel-Pro-Inc/RodizioExpressDesktopApp)@[d6871c0309...](https://github.com/Pixel-Pro-Inc/RodizioExpressDesktopApp/commit/d6871c03096baa370cb5bf27a7f72834d558c458)
#### Saturday 2022-06-25 14:20:17 by Abel3047

DO NOT PULL FROM HERE

-There was too much, way too much to finish in one sitting.
FirebaseDatacontext was actually hell. I thought it was bad in
QRCashless but it was nothing compared. But let me try breaking down
progress

-The Menu aggregate was introduced. This was also done in QR. We also
introduced an exception and other works that were found in QR or were
created as a consequence of the copy. Please not that the kernel will
have to remove most of these copies.
-I plan on having OfflineDataHelpers become the service in charge of all
things offline.
-Two xaml files were edited to have the MenuService included in them.

Now for the pain
-So in FirebaseDataContext. Alot of stuff that should have been in a
different thing from firebase was there, but at the same time was
heavily coupled with the things inside firebase. So it was difficult
untieing the mess. It still is. Not only was it coupled with
firebase functionality but also OfflineContext. So As it stands there
are alot that aren't connected and are still loose within both
firebase and dataService.
-we also have a problem where DataService required firebaseDataContext
directly. I am hoping I can make a DatabaseService that will encapsulate
these new methods and simply get its data from FirebaseServices as an
inherited property. But that's a problem for future Abel.

---
## [dunkanos/Angel-Arena-Reborn](https://github.com/dunkanos/Angel-Arena-Reborn)@[90573812a2...](https://github.com/dunkanos/Angel-Arena-Reborn/commit/90573812a2d3342b57555316986f78b6dce37f67)
#### Saturday 2022-06-25 14:21:09 by Dunkan

Patch 25.06.2022

Hero changes:

Abaddon
	- 1 skill self damage	changed from 30/35/40/45/50/55/60 to 50
	- 2 skill cast point  changed from 0.452 to 0.3
	- 2 skill duration  changed from  13 to 15
	- 3 skill movement speed changed from 25 to 15/17/19/21/23/25/25"

Abyssal Underlord
	- 2 skill root duration 	1.0/1.2/1.4/1.5/1.6/1.7/2.1" to 1.0/1.2/1.3/1.4/1.5/1.6/1.7

Alkchmist
	- shard skill Berserk Potion bonus ms 0 to 30

Ancient Аpparation
	- 2 skill shard damage changed from 40 to 150
	- 2 skill shard attack speed slow changed from 20 to 50

Dragon Knight
	- Fireball damage changed from 75 to 150

Furion
	- 1 skill Cooldown changed from 14/13/12/11/10/9/8 to 15
	- 3 skill treant health changed from 550/650/750/850/950/1050/1150 to 550/600/650/700/750/850/1100
	- 3 skill treant damage changed from 45/55/65/75/85/95/105 to 25/30/45/55/60/65/105
	- 4 skill Cooldown changed from 50 to 65

Huskar
	- 4 skill health damage changed from 45 to 20/22/25/27/33/36/45

Chaos Knight
 	- 3 skill crit chance changed from 30 to 25
 	- 3 skill crit max changed from 190/220/250/280/310/350/400 to 170/190/220/250/290/320/350
 	- 3 skill lifesteal changed from 30/35/40/45/50/55/60 to 25/30/35/40/45/50/55

Crystal Maiden's

 	- 3 skill mana per cast 10/15/20/25/30/35/40

Centaur
 	- 1 skill stun duration changed from 2.0 to 2.0/2.1/2.2/2.3/2.4/2.5/2.6

Dawnbreaker
 	- 4 skill damage of pulsation changed from 30/50/70/80/90/100/110 to 50/75/100/125/150/175/200
 	- 4 skill heal of pulsation changed from 50/70/90/110/130/150/170 to 50/75/100/125/150/175/200
 	- 4 skill damage changed from 130/160/190/220/250/280/310 to 200/300/400/500/600/700/800

Medusa
	- Cold Blooded Cooldown changed from 6 to 10

Marci
	- 4 skill Cooldown changed from 110/100/90/80/70/60/50 to 80/75/70/65/60/55/50
	- 4 skill between flurries changed from 1.75 to 1.55/1.50/1.45/1.40/1.35/1.30/1.25
	- 4 skill attack Stacks changed from 3/4/5/6/7/8/9 to 4/5/6/7/8/9/10
	- talent 25lvl silence duration changed from 1.5sec to 0.5sec

Primal Beast
	- Added to Angel Arena

Techies
	- Added techies skill frm dota

Undying
	- 4 skill Cooldown changed from 40 to 60
	- Shard Cooldown ultimate changed from 35 to 20

Item changes:

Tome of heroes
	- stack start game 5
	- delay before the start of the game 600sec
	- Max stack 40
	- Cooldown stack 20sec
	- Cost changed from 1250 to 1500

Ethereal Blade
	- Craft changed from Ghost scepter + Recipe to Mystic staff + Ghost scepter + Recipe

Gem
	- cast range changed from 300 to 500
	- active skill radius changed from 300 to 500
	- duration active skill changed from 4 to 8
	- Cooldown active skill changed from 12 to 30

Bosses:

Keymaster
	- now Ignores terrain
	- ms changed from 365 to 400

Creeps:

Satyr hand
	- 3 skill magic amplify changed from 50 to 20

Fixes:
Storm Spirit 1 skill damage fixed
Earth Spirit ultimate fixed
Elder Titan ultimate fixed
Abyssal Underlord ultimate fixed
Omniknight 3 skill and ultimate fixed
Pudge 3 skill fixed
Templar Assassin 3 skill fixed
Shadow Fiend aghanim fixed
Hoodwink shard skill fixed
Morphlimg 1 skill fixed
Swift blink range fixed
Overwhelming blink range fixed
Arcane blink range fixed

---
## [electricdreamers/electricdreams.online](https://github.com/electricdreamers/electricdreams.online)@[c2715fd3c6...](https://github.com/electricdreamers/electricdreams.online/commit/c2715fd3c649d8d3d16224f3aba073611525fe2a)
#### Saturday 2022-06-25 15:25:35 by JamesBardolf

Remove sprites fucking stupid ass music 

Fucking commit spammer

---
## [Aman23Gupta/Rocket.Chat](https://github.com/Aman23Gupta/Rocket.Chat)@[5a37518e42...](https://github.com/Aman23Gupta/Rocket.Chat/commit/5a37518e42dec114e0ed1a71b5d103b4a62e9b58)
#### Saturday 2022-06-25 15:49:29 by Ben Wiederhake

[FIX] Client-generated sort parameters in channel directory  (#25768)

## Proposed changes (including videos or screenshots)
- In the web-client, sorting the channel directory by "Last Message" raises the error "Invalid sort parameter provided".

I don't think a screenshot is necessary, but if you'd like one anyway, here it is:

![Bildschirmfoto_2022-06-06_12-54-34](https://user-images.githubusercontent.com/2690845/172147996-e9942daf-6819-4eee-afa4-b1c6bce7a650.png)


## Issue(s)
Closes #25695

## Steps to test or reproduce

- Open the web client, i.e. navigate your browser to `https://rocketchat.$DOMAIN/home`
- Click the "Directory" button in the top left, (or just navigate directly to `https://rocketchat.$DOMAIN/directory/channels`)
- In the table header, click on "Last message" once
- In the table header, click on "Last message" again

Expected behavior: Clicking "Last message" turns on and then toggles sorting by the date of the last message, either first ascending and then descending, or the other way around.

Actual behavior: The first click sorts the messages in ascending order (good!), the second click shows a red warning box "FIXME", the table content disappears, and is replaced by throbbing grey placeholders.

### "Good" request (ascending order):

`https://rocketchat.domain.org/api/v1/directory?query=%7B%22type%22%3A%22channels%22%2C%22text%22%3A%22%22%2C%22workspace%22%3A%22local%22%7D&sort=%7B%22lastMessage%22%3A1%7D&count=25`

More easily readable GET parameters:

```
query | {"type":"channels","text":"","workspace":"local"}
sort | {"lastMessage":1}
count | 25
```

Response:
```
{"result":[{"_id":"AAAAAAAAAAAAAAAAA","name":"foobar","fname":"foobar","t":"c","usersCount":10,"ts":"2019-01-01T00:00:00.000Z","default":false,"lastMessage":{"_id":"AAAAAAAAAAAAAAAAA","rid":"AAAAAAAAAAAAAAAAA","msg":"Hello, World!","ts":"2019-01-01T00:00:00.000Z","u":{"_id":"AAAAAAAAAAAAAAAAA","username":"normaluser","name":"normaluser"},"unread":true,"_updatedAt":"2019-01-01T00:00:00.000Z","urls":[],"mentions":[],"channels":[]},"description":"Obviously, this JSON response is heavily censored."}],"count":25,"offset":0,"total":52,"success":true}
```

(Obviously, this JSON response is heavily censored, but you get the gist: It was successful.)

### "Bad" request (descending order):

`https://rocketchat.domain.org/api/v1/directory?query=%7B%22type%22%3A%22channels%22%2C%22text%22%3A%22%22%2C%22workspace%22%3A%22local%22%7D&sort=%7B%22lastMessage%22%3A0%7D&count=25`

More easily readable GET parameters:

```
query | {"type":"channels","text":"","workspace":"local"}
sort | {"lastMessage":0}
count | 25
```

Response:
```
{"success":false,"error":"Invalid sort parameter provided: \"{\"lastMessage\":0}\" [error-invalid-sort]","errorType":"error-invalid-sort","details":{"helperMethod":"parseJsonQuery"}}
```

## Further comments

Version on the server where I noticed this: `https://rocketchat.$DOMAIN/api/info` returns `{"version":"4.8","success":true}`. According to the "Releases" page, this version appeared 5 days ago, so I believe this is up to date.

### The journey to here

For some reason, the descending order uses the wrong magic number "0", and the server can't interpret that. However, this *used* to work, so I'm not very sure about this.

The error message appears in the source code of the entire organization exactly once: https://github.com/RocketChat/Rocket.Chat/blob/31ae30f30ad71d9e5a1b0cad494b3471a7dd8807/apps/meteor/app/api/server/helpers/parseJsonQuery.ts#L42
So I'll guess that this is the line of code that generated this particular message.

A few lines above we see that the server only knows 1 and -1 as magic numbers for the sorting:
https://github.com/RocketChat/Rocket.Chat/blob/31ae30f30ad71d9e5a1b0cad494b3471a7dd8807/apps/meteor/app/api/server/helpers/parseJsonQuery.ts#L35
This matches the observed bug: The browser sends 1 (which works) and 0 (which doesn't work).

Generally, it seems that the web client actually uses the strings "asc" and "desc" internally, which are hard to mix up. So I assume that it's the conversion of that is broken somehow.

Exactly this seems to be the case here:
https://github.com/RocketChat/Rocket.Chat/blob/31ae30f30ad71d9e5a1b0cad494b3471a7dd8807/apps/meteor/client/views/directory/hooks.js#L11

The code around it produces exactly the kind of query seen in the network log, and can also produce the buggy parameter `sort: 0`. This either fixes bug #25695, or a different bug of the same kind.

I am not sure how to add tests for this, can someone do this for me or show me where to start? I'm actually just an end-user and "accidentally" found the fix for the bug while writing the bug report ^^'

EDIT: Rebased for convenience, and to re-check CI.

---
## [newstools/2022-startribune](https://github.com/newstools/2022-startribune)@[e9e686f459...](https://github.com/newstools/2022-startribune/commit/e9e686f45993c307d1302bca9567131dc809103b)
#### Saturday 2022-06-25 16:13:08 by Billy Einkamerer

Created Text For URL [www.startribune.com/restaurants-where-to-eat-in-downtown-minneapolis-st-paul-for-breakfast-lunch-dinner-happy-hour/600184912/]

---
## [amameuser/mame](https://github.com/amameuser/mame)@[ba63081d10...](https://github.com/amameuser/mame/commit/ba63081d109c904902958c6324b013cb10b42732)
#### Saturday 2022-06-25 17:23:39 by 0kmg

gameboy.xml: Added 21 more prototypes. (#9962)

* gameboy.xml: Added 21 more prototypes.

New working software list additions
-----------------------------------
Astérix (earlier prototype) [VGHF, Hidden Palace]
Astérix (early prototype) [VGHF, Hidden Palace]
Asteroids (prototype) [VGHF, Hidden Palace]
Barbie - Game Girl (prototype) [VGHF, Hidden Palace]
Battle Ships (Spain, prototype) [VGHF, Hidden Palace]
Blaster Master Boy (USA, prototype) [VGHF, Hidden Palace]
Bomb Jack (earlier prototype) [VGHF, Hidden Palace]
Bomb Jack (later prototype) [VGHF, Hidden Palace]
Bonk's Adventure (USA, prototype) [VGHF, Hidden Palace]
Bubble Ghost (prototype) [VGHF, Hidden Palace]
Catrap (prototype) [Forest of Illusion, Swanhubstream]
Cosmo Tank (USA, prototype) [VGHF, Hidden Palace]
Dropzone (prototype, alt) [VGHF, Hidden Palace]
Gauntlet II (prototype) [Forest of Illusion, Rezrospect]
Ghostbusters II (prototype) [VGHF, Hidden Palace]
Kung-Fu Master (prototype) [Forest of Illusion, FNeogeo]
Mysterium (prototype) [Forest of Illusion, Rezrospect]
Obélix (Europe, French / German, prototype) [Forest of Illusion]
Prince of Persia (prototype) [Forest of Illusion, FNeogeo]
The Blues Brothers (prototype) [Forest of Illusion, FNeogeo]
Triumph (prototype) [Gaming Alexandria]

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[c93b9c051e...](https://github.com/mrakgr/The-Spiral-Language/commit/c93b9c051e9f11fdb4af2231de99d4e24b6a7ecf)
#### Saturday 2022-06-25 18:22:56 by Marko Grdinić

"11am. Let me chill just a bit and then I will start.

11:30am. Let me start. I have an idea for how to make the scene more impactful. I am going to bevel some of the houses and turn the roughness to 0. That will get me gleam off the edges. Let me give it a try.

11:45am. I beveled the original assets, but I am confused now. I know that I selected to hide the unexported ones, but how do I unhide...ahhh, the system list.

12:20pm. This is hard. I can't get it to stick. I am going to have to throw the style transfer at it en masse and see if something good comes out. I put a bunch of lights all of the scene, and if I could get a style transfer effect where that ends up looking gleaming bright similar to how it was in the VN cover image that would be great.

12:30pm. Done rendering. I'll have to put it through style transfer now.

12:35pm. While this is going on, let me go get breakfast. Ideal time for it. Later in the day I might need to step out of the house for a bit.

1:55pm. Done with breakfast. Let me just finish the chapter of LM and I will check out the style transfer results.

2:05pm. Ok me, stop reading novels and start doing art.

2:10pm. This time, only the dawn over death has caught my eye. It is not exactly what I want, but maybe a soft solemn lighting could do fine.

2:35pm. https://www.youtube.com/watch?v=c0jZ7sPyouE
Jade Moon Upon a Sea of Clouds - Disc 2: Shimmering Sea of Clouds and Moonlight｜Genshin Impact

Maybe I'll give Genshin Impact a try at some point. It is weird how for the past couple of years I've been picking games based on their OST. As a kid I never cared about the OST at all.

3:25pm. I am not happy with any of this. Let me try making the buildings emmisive yellow.

3:30pm. I had a happy accident just now.

3:45pm. But it is a lot different how I imagined it originally. I am not sure I want the city to be dark up top. Rather I'd like it to be bright.

4:10pm. Damn it, I have the same problem as before with adding instance collections to the scene. I am going to make a bug report.

4:40pm. Had to take a short break. What I want to do next is figure out how to do variable shading.

https://youtu.be/X4m344gWTZw
Blender 2.8 Eevee tutorial - How to make night city easy

Ah, let me watch this.

https://youtu.be/i0FQZ_euU_A
How to Create a Material ID in Blender 2.9 - Guide to Beginners

5:05pm. https://docs.blender.org/manual/en/latest/render/shader_nodes/input/object_info.html

The weather is so hot that I've resorted to pouring water on my head. At any rate, I have an appointment with a hairdressed in two days, Monday 5pm.

The mane I have now is too much for this kind of weather.

At any rate, this node had color. I'll be able to use that to randomize the instance.

> Object color, same as Color in the Properties ‣ Object Properties ‣ Viewport Display.

Whops, not what I thought.

> Random number unique to a single object instance.

This is what I want.

5:15pm. Actually no, I want face IDs here. Let me watch that video.

https://youtu.be/i0FQZ_euU_A?t=478

I get the concept of baking, but how did he select the output texture for the bake?

https://www.youtube.com/results?search_query=blender+shading+random+face

Let me watch some of these.

https://youtu.be/kBrOzCxOWhM
Blender quick tip - Randomize material per polygon

https://youtu.be/kBrOzCxOWhM?t=160

Hmmm, ok, this is something. I would not have thought of doing it like this.

6:25pm. https://youtu.be/bkXtDf-MT2o
Blender Quick Tip: Assign Random Colors To Polygons

Let me just check if this uses the same technique.

6:30pm. Nope, it is some hacky thing. Nevermind that. What I need to do now is put in a background.

https://www.flickr.com/photos/145781270@N02/31856549553/in/photolist-Qx49jn-KqRYJc-etGRze-S57QvG-XwrkTt-WBfsof-d2M3fL-UrxGzR-aaXEWa-dd1LkW-EFL6E7-UdzuP3-R6DZyK-Wt4h9C-Sj8Q97-R4ghXd-razxNe-VgFpka-U4nyVg-nNBTeA-Ryztmr-TqXjYz-kpnCe6-WNjws4-YbdQ32-SNjWWN-qs9QGn-pTKuh8-z9r6zL-aoEw18-TT2N4a-qawECy-nvtZdr-SHrtqk-USavZY-RSyS83-27rSxBL-RTEeRJ-XjK6gS-XF7yzD-q6UTjs-XR9BbC-X6cbXj-XEq1vZ-XJKeYU-SRHzAN-CvCEL1-Vr9oM3-BBoFo8-Yz46GV

This one is nice.

7:15pm. Done with lunch. While I saw busy with that I let it render. Let me do a round of style transfer.

7:25pm. Let me stop the ST for a bit. I want to try something.

7:30pm. No it's fine. I did well. I thought of making the playform more intense than the buildings, but that sort of thing does not really work well. The buildings should be intense.

7:45pm. Instead of doing the ST on the CPU, I really should just try the GPU. I think there should be enough RAM for it. I just fell into using the CPU out of habit, but even for a single image at this resolution it does take a couple of seconds.

...Nope, it does not seem the GPU has enough mem for 2k images.

The CPU will have to do.

8pm. I am done for the day. I could go with adding more detail, but that would be fruitless. The way the composition is now is good enough. I'll post it on Twitter tomorrow.

8:05pm. I think I did get it right this time. This taught me a bit about composition. Right now I like a lot of the style transfered results whereas previously I only liked 'curviness'. I think I am going to kick most of the drawing from personal list. They aren't good compared to the paintings.

8:10pm. Maybe I'll go with the great wave again, since I went with it for the cover.

8:15pm. I am really enjoying watching the style transfered images. They aren't at all trivial modification of the original, even though they share a lot of the same structure. I feel that they do have a lot of artistic value while my original does not.

...No, for most of these style tranfered images you wouldn't be able to tell are 3d, while my original is obviously so.

8:20pm. Without style transfer I would in fact probably have to bring in fancier models and do more elaborate texturing, but with ST this is good enough.

Let me close here. It is time to rest. Tomorrow I'll post this on Twitter and move on to character modeling."

---
## [macdice/postgres](https://github.com/macdice/postgres)@[c40ba5f318...](https://github.com/macdice/postgres/commit/c40ba5f318f96a6a5a29729b987ead11c5dc65c1)
#### Saturday 2022-06-25 20:12:23 by Tom Lane

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
## [62832/ATM-7](https://github.com/62832/ATM-7)@[8bff1fe476...](https://github.com/62832/ATM-7/commit/8bff1fe4769e3ecd98814c640bc44640ee6e9f1a)
#### Saturday 2022-06-25 20:53:40 by 90

Add more starting books

Tome now also includes guides/READMEs from Blood Magic, Evilcraft, RFTools, Roots Classic, SecurityCraft, Silent Gear, Spice of Life: Carrot Edition, The One Probe and The Twilight Forest.

---
## [darshan-/dot](https://github.com/darshan-/dot)@[0262fd32ec...](https://github.com/darshan-/dot/commit/0262fd32ecb0d2183572b45132da933d1e324403)
#### Saturday 2022-06-25 22:12:46 by Darshan-Josiah Barber

Electric indent has been driving me crazy, so I finally am trying a basic setup to do what I want: enter leaves current line alone, adds a new line, and indents that new line.  Close curly bracket adds a close curly bracket and indents the line.  Ideally I want to check if the line is only whitespace and close curly bracket, but this is a good start.  Notably, commenting *doesn't* fuck up my indentation, and enter doesn't fuck up my current line.  There may be more things I want, but I think this will be a much calmer existence for me for now.

---
## [peff/git](https://github.com/peff/git)@[abf92281d9...](https://github.com/peff/git/commit/abf92281d997043b5a36492cebac297cb74188a4)
#### Saturday 2022-06-25 22:55:35 by Jeff King

commit: give a hint when a commit message has been abandoned

If we launch an editor for the user to create a commit
message, they may put significant work into doing so.
Typically we try to check common mistakes that could cause
the commit to fail early, so that we die before the user
goes to the trouble.

We may still experience some errors afterwards, though; in
this case, the user is given no hint that their commit
message has been saved. Let's tell them where it is.

Signed-off-by: Jeff King <peff@peff.net>

---
## [peff/git](https://github.com/peff/git)@[bb6f3575d3...](https://github.com/peff/git/commit/bb6f3575d380e43a4da2a2f455b784654e2b685f)
#### Saturday 2022-06-25 22:55:41 by Jeff King

ahead-behind: do not die when we see no INTERESTING pending object

We currently die if we are fed an ahead/behind with zero
objects (`foo..foo` in the most basic case, but in practice
something like `foo@{upstream}..foo`, when `foo` has just
been merged).  The problem is that we let
`handle_revision_arg` parse it, and then pick the pieces out
of the pending object list. So "^foo" looks no different to
us there than "foo".

This patch hacks around it by picking up the UNINTERESTING
object in that case. However, this isn't great because:

  1. Now we won't notice some types of bogus input.

  2. We end up reporting the name of the UNINTERESTING object.

We probably should pick apart the ".." ourselves, or even
just change it to ":" or whitespace.

Signed-off-by: Jeff King <peff@peff.net>

---

