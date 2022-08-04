## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-08-03](docs/good-messages/2022/2022-08-03.md)


1,987,740 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,987,740 were push events containing 3,007,344 commit messages that amount to 231,639,589 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 28 messages:


## [ivanmixo/BeeStation-Hornet](https://github.com/ivanmixo/BeeStation-Hornet)@[3249b4560b...](https://github.com/ivanmixo/BeeStation-Hornet/commit/3249b4560b568fe762f2a695a6427bab7c56c649)
#### Wednesday 2022-08-03 00:23:15 by DrDuckedGoose

Lasso Fix (#7345)

* Merge https://github.com/BeeStation/BeeStation-Hornet into annoying-thing Merge conflicts :)

* Initial - 23 7 22

- Doesn't allow dead mobs to be ridden
- Space walk is now specific to the mob

* Actually Fix It - 23 7 22

* Fuck - 23 7 22

- Fix being able to tame human
- Fix being able to tame the dead

* Update carp_lasso.dm

* You boys fucked buckle code - 23 7 22

* Update carp_lasso.dm

* Update riding.dm

* fix icon - 24 7 22

* Review Changes - 24 7 22

---
## [QuinnSquared/Heat-Death](https://github.com/QuinnSquared/Heat-Death)@[81ef20fdd6...](https://github.com/QuinnSquared/Heat-Death/commit/81ef20fdd64c061d77ff2426f372e7e9dd400fc3)
#### Wednesday 2022-08-03 01:02:44 by QuinnSquared

Merge pull request #10 from QuinnSquared/ui-contd

I think this is safe to merge based on my reading of the files. I honestly don't want to bother checking out the branch for all 15 seconds it would take to verify this hasn't broken anything, so I'm just not going to. Fuckit, we're doing it live.

---
## [ethical-jobs/utilities-php](https://github.com/ethical-jobs/utilities-php)@[4c0082452d...](https://github.com/ethical-jobs/utilities-php/commit/4c0082452dc2d70687c7d739050fa5119ad21f77)
#### Wednesday 2022-08-03 01:04:52 by Danielle McLean

Swap PHPUnit printer so we can lock Orchestra versions

Since this package is a dependency for others, it kinda needs to try to
work with different versions of its dependencies. To that end, in the
Github workflow we install its deps with both --prefer-stable and
--prefer-lowest, which helps test that at least two versions of the deps
work okay.

Unfortunately that meant pulling in a completely different major version
of orchestra/testbench, which was a problem because the older one just
crashed PHPUnit entirely. I guess PHPUnit itself changed?

I couldn't insist on getting version 7 of the Orchestral packages
because they require a newer Symfony YAML package, and the result
printer we were using required older versions of that YAML package. No
idea why it needs a YAML parser to pretty-print PHPUnit results, but
whatever.

This new result printer package doesn't depend on anything and shouldn't
cause further dependency hell. It also looks a little nicer in my
opinion. I like BDD.

---
## [aospa-pasco/kernel_msm-4.14](https://github.com/aospa-pasco/kernel_msm-4.14)@[815901dac3...](https://github.com/aospa-pasco/kernel_msm-4.14/commit/815901dac35785f1c7a26f304cc36aa5bc12ba04)
#### Wednesday 2022-08-03 01:34:48 by Pascoato

Revert touchscreen commits from LA.UM.9.1.r1-12100.01-SMxxx0.QSSI13.0 tag

* Fuck you qcom, this make 10% of ginkgo display irresponsible af

This reverts commit fc203b7cce51e26dfeb786beb53ae01ff1cdf825, reversing
changes made to f6695546a9d59939e715029f0ae4a93c506ac1dd.

Revert "Merge "input: touchscreen: focaltech_touch: support dynamic report rate""

This reverts commit f6695546a9d59939e715029f0ae4a93c506ac1dd, reversing
changes made to ba47748c98a24ac947586ee3f2b0f16e3e810d27.

Revert "Merge "input: touchscreen: focaltech_touch: Remove vfs_read()""

This reverts commit ba47748c98a24ac947586ee3f2b0f16e3e810d27, reversing
changes made to f78fe8957a97e693c265517a7315c82453b7164a.

Revert "Merge "input: touchscreen: focaltech_touch: Configure power supply""

This reverts commit f78fe8957a97e693c265517a7315c82453b7164a, reversing
changes made to e6b3a17167aea80bdda39c27f5a9283c8a50b640.

Revert "input: touchscreen: Enable new Focaltech touch driver"

This reverts commit e6b3a17167aea80bdda39c27f5a9283c8a50b640.

Revert "input: touchscreen: Add new Focaltech touch driver"

This reverts commit 76970c0c877a569d86e5d348ec0e4a7eb66f2f08.

---
## [Neonyxia/tgstation](https://github.com/Neonyxia/tgstation)@[8f0df7816b...](https://github.com/Neonyxia/tgstation/commit/8f0df7816bae3c5dedf599611cda3e6039024e14)
#### Wednesday 2022-08-03 01:56:46 by Kylerace

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
## [reklaw9/40K-Eipharius](https://github.com/reklaw9/40K-Eipharius)@[fd5321ae5b...](https://github.com/reklaw9/40K-Eipharius/commit/fd5321ae5b06dcdc5eba522440abbe05a6c4b297)
#### Wednesday 2022-08-03 02:56:16 by Vanderlin

orks_species

Orks now regenerate health at 0.5 instead of 0.08 since we did nerf the crap out of waaagh previously, not sure why Orks had a regen that is basically equiv to not healing at all but were given the Waaagh heal that literally shoves their eyeballs back into place...

Waagh also no longer heals brute/burn, it only recovers organ damage and blood loss. This means Orks will need to rely on their regen ability more often and their pain immunity in combat, otherwise waaagh is only useful for recovering blood loss or organ damage after a fight.

Ork stats were debuff'd PRIMARILY in the Endurance category of a whopping +18 endurance. If you were trying to figure out why the Orks seem to be unkillable, it's because of the endurance stats they were given. The instant heal waaagh probably didn't help either.

They also have pain and embed immunity, I swear if I see another Ork pickup an IFAK just to use the morphine ampoule I'm gonna lose my mind. NO MORE.

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[a0818c9881...](https://github.com/treckstar/yolo-octo-hipster/commit/a0818c98817f5993d5ea89a2bb4c2e103ca3ccb1)
#### Wednesday 2022-08-03 03:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [chenzhx/spark](https://github.com/chenzhx/spark)@[c4c623a3a8...](https://github.com/chenzhx/spark/commit/c4c623a3a890267b2f9f8d472c8be30fc5db53e1)
#### Wednesday 2022-08-03 03:23:49 by Hyukjin Kwon

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
## [et84121/rx-player](https://github.com/et84121/rx-player)@[ebfaf7498c...](https://github.com/et84121/rx-player/commit/ebfaf7498c0803b0dc38ffdea3096c8422d388ef)
#### Wednesday 2022-08-03 06:07:11 by Paul Berberian

Update most dependencies but Jest

This commit update almost all dependencies but jest.

This is because Jest 28 seems to break while running code, presumably
due to `import`/`export` declarations in imported RxJS files (but I do
not think RxJS is at fault here) that lead to an `unexpected token` when
running through Jest.

You could think that the fault is linked to node not understanding
`import`/`export` (linked to CommonJS/ES6 import shenanigans) but it is
even trickier than that as Jest already performed some JavaScript
transformation at that point, which made the import/export inside an
IIFE - and I'm not sure that this is supported anywhere.

After taking ~a day (much more time than I should) trying to play around
to remove that issue, I gave up and avoided updating Jest to its v28.

In the future, I guess we should either:

  - understand what we're supposed to do here to make it work with Jest
    28 (Jest documentation was poor - even without considering the
    sometimes incomprehensible google-translated french one I get each
    time by default on their docusaurus-based documentation)

    Opened GitHub issues were 100% for angular-based applications - as it
    seems the RxJS+TypeScript cocktail is very majoritarily those. Those
    have their own "fix" through another magical angular dependency.

    Moreover, it does not help that Jest's philosophy seems to be trying to be
    extremely simple for users at the cost of some complex behaviors (as an
    example, it looks like it auto-picks a `babel.config.js` file if it
    sees one at the root of the project. If like us you have multiple build
    files at the root depending on the building context, it is not a good
    idea to silently pick random files like that by default).

    I couldn't understand under an acceptable time where the issue was - and
    at which step it happened.
    I just browsed dozens of doc pages, GitHub and StackOverflow issues
    which just proposed to add yet other automagic dependencies (looked like a
    parody of what JavaScript haters talk about!) - which all seemed to have
    no effect whatsoever.

    I also asked for help from other teams at Canal+, but those in the
    same situation (TypeScript and RxJS) also seem to have random issue
    preventing them from doing the switch.

  - Remove RxJS from the code. It's presumably not its fault yet we
    already started doing that, so maybe we'll just raise the jest
    version once RxJS is definitely removed from the RxPlayer.

  - Wait for some kind of Jest fix or new way of handling those?

  - Remove Jest and go with another testing framework.

    I almost did that due to being fed-up with Jest, but it might no be
    as easy as it seems, mostly the module-mocking part as I'm unsure of
    how other framework handle that now and if it is as convenient as
    Jest's way.

---
## [adriengentil/assisted-service](https://github.com/adriengentil/assisted-service)@[564650feca...](https://github.com/adriengentil/assisted-service/commit/564650feca372064314282d98d6fd9c6ee69bd2c)
#### Wednesday 2022-08-03 07:13:53 by Omer Tuchfeld

MGMT-10973: Enable DNS validations if coredns or keepalived static pod manifests in day-2 connectivity-check ignition (#4072)

For context, this is a service-side follow-up to:

https://github.com/openshift/assisted-installer-agent/pull/388

and also this small agent fix https://github.com/openshift/assisted-installer-agent/pull/403

# Goal

During day-2 installations, we want the service to optionally perform
DNS validations when the worker attempts to join none-platform clusters.

# Issue

When the cluster is imported via our `.../v2/clusters/import` endpoint,
we have no way to know whether that cluster is a none-platform cluster
or cluster with managed networking (e.g. baremetal), so we have no way
to know whether we should perform the DNS validation or not. We wouldn't
like to have that validation on all the time, because it's unnecessarily
annoying for clusters with managed networking.

# Background

As part of our existing API connectivity-check, the service asks the
agent to download the worker.ign file from the to-be-joined-cluster's
machine-config-server, then send that back to the service.

# Solution

The contents of that file include information that will allow the
service to make an educated guess about whether the ignition originated
from a cluster with managed networking or not.

Also, a new "imported" column has been added to clusters, to indicate
whether they were created through a conversion or through being
imported. This is important because the solution should only be
applied for imported clusters, and this will provide a good way
to tell apart imported from non-imported clusters.

Also, when a user imports a cluster, we will inspect the `params.NewImportClusterParams.APIVipDnsname`
parameter and extract:

- The cluster name
- The cluster base domain

The cluster name will override the name given in `params.NewImportClusterParams.Name`,
see diff comment for more information on why.

The cluster base domain will be used to set the `BaseDNSDomain` of the
cluster, because up until now we didn't set it for imported cluster.

The reason `BaseDNSDomain` and `Name` have to be correctly set is
because the DNS validations use them to construct the domain names
that are being validated.

Also updated some validation messages for the API connectivity check and
DNS validations.

Also, the clusterdeployments_controller can now import SNO clusters,
it was an oversight that should have been done as part of 4cda26533d377f453f68783e8b2eae438734555d (#3404)

# Ignition Files

The ignition files we currently look at are:

```
/etc/kubernetes/manifests/coredns.yaml
/etc/kubernetes/manifests/keepalived.yaml
```

This is a hack - since we have no official way to know whether a worker
ignition file originated from a cluster with managed networking or not,
we instead rely on the presence of coredns and keepalived pod manifests
to indicate that. We only expect those to be present in clusters with
managed networking. To be a bit more robust, the service will consider
the presence of any one of them to mean that the cluster has managed
networking. This gives us better forwards compatibility if one of them
gets renamed / replaced with other technologies in future OCP versions.

Another way in which this is hacky is that users could manually create
static pods with the same name as part of their machine-configs, in
which case we would have a false-positive detection. But that is
admittedly very unlikely.

Hopefully we can negotiate with the relevant OCP teams to have a more
official, stable way to have this detection - like a magic empty file
placed somewhere in the ignition that we can check for the presence of.
Once we have such file, we can slowly deprecate this detection mechanism
and fully move to the new one by inspecting that file instead.

---
## [JulianKnodt/rxatlas](https://github.com/JulianKnodt/rxatlas)@[3302397721...](https://github.com/JulianKnodt/rxatlas/commit/33023977218155b335b4da69812d5a6835fc0046)
#### Wednesday 2022-08-03 09:07:22 by julianknodt

Work on mesh decimation

Holy shit the original implementation is cursed

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[a05a4a0add...](https://github.com/mrakgr/The-Spiral-Language/commit/a05a4a0add7c4af55c05b814b69e81a2a15a91df)
#### Wednesday 2022-08-03 11:01:15 by Marko Grdinić

"8:05am. I am up. Let me rant just a bit to get over my grogginess.

If I really wanted an ordinary job, I could do things like interview preparation and acting practice. The important thing I am missing is enthusiasm, but I could get into if I tried. My biggest issue is my AI chip obsession which is holding me back from everything else. So before I do anything else, it makes sense to deal with it. Obsession is like love, if the girl you like does not like you, the rational thing is to get it on with somebody else. But love isn't something you can switch on a whim. So since I haven't been rejected why not accept it and see how far it goes?

Once I've done all that I can with Spiral I'll be able to move if necessary. Of course, the best would be if my vision succeeds and I end up with both sponsors and users for my language.

8:10am. I also need the chips for my AI ambitions, and these kinds of connections would be a natural fit. Any other job would not satisfy me. I know that I am a subpar researcher compared to the math geniuses in the field. But I understand as a programmer that the best way to improve is to get a better tool. What if I boost my ML research by adopting a better approach? There is no way around it, in 2021 I've essentailly expended all my creative budget in that area. I am completely in the darkness as to how to make significant ML algo improvements on my own. In order to adopt evolutionary methods as a core of my ML research, CPUs + GPUs would definitely not pass muster, but I do not have AI chips so I am stuck. I have no creative outlet right now. If I want to make progress in ML, I need to automate my research methods, but I do not have computers capable enough of letting me do that.

Let me see if I got a reply in the channel or if the post got removed. If I do not get any reaction, maybe it is not so bad, since the mods have probably read the post, but haven't decided to remove it. That could have some potential for getting feedback down the road.

https://manganato.com/manga-nj990618
Thank You, Isekai!

Oh right, let me just plug this GB manga. It came out recently and is really good. I only discovered it yesterday and binged it.

https://discord.gg/Rh6HMCSzFd
Tenstorrent Discord

Let me put this link here. Well, the post is still there and I haven't gotten a reply yet. Let me check my mail. Nothing.

8:20am. So how do I interpret this?

That the post is still standing there is good, it might mean that mods have looked at it and decided not to remove it. But that is under the assumption that they've even seen it to begin with. I am assuming the mods get notified whenver somebody new comes in and posts there. I mean, that Discord is specifically for support, so that should be the case, right?

Well, either way, they should see it at some point. That place is visible even if they aren't paying attention to it. It is not like those fringe Reddit posts.

8:35am. If I can get proper sponsorship for Spiral, even it is not a 200k a year job, I can consider myself as not being a failure. That is what I should work towards. I have very specific customers that I want to serve and there is not much else that I am obsessed with doing.

8:40am. Enough of that. Let me finish chilling and I will send a message to the world.

9:05am. Let me start.

9:15am. I am thinking back to OpenAI's ES. It caused a splash when it came out, and later it has been found that old style gene algos work just as well. So it possible to use them to optimize deep nets in RL domains.

But maybe that was the wrong lesson. It does stand as a hint that it should be poosible to make layers into non-hierarchical modules and have them perform their own program search. I could init the starting nodes using backprop and see how that develops.

I was wondering about this for a long time - just what magic thing would self improving AIs use to generate ideas for their mental improvements? I wrote the original stories in 2014 before I had any experience in ML.

For a human uploaded to a brain core, the self improvement process should go like this. After digitization he should have access to his mental algorithms and be able to see and modify it as he sees fit.

I am going to make a prediction here, the brain itself is not necessarily evolving its own learning. If it is, the effect should be limited. Otherwise there would not be such things as IQ differences between humans. Furthermore, nature has to lean on the exploitation side of things vs exploration when it comes to designing its agents. This would result in the lowering of intelligence compared to what would be possible.

But a digitized human would have the option of expanding his mental capacity. Then to improve his intelligence, what is he going to do, try programming the neurons individually? Of course not.

The best thing would do is to create an automated process of intelligence evolution.

The point of AI chips is not necessarily to match the brain. It goes back to the airplanes vs birds analogy. The main difference that AI chips will have over brains is that they will be able to perform search for what their own learning algorithm should be.

9:30am. Yeah, I won't accept the Inspired making random modification anymore by their lonesome. If their greater intelligence allows them to do something, that will have to be to improve the automated learning process for a specific domain.

General intelligence is one thing, but narrow intelligence is valuable as well. Programs are extremely powerful, it is worth integrating them into one's mind.

Right now, the way the ML field does research is complete nonsense, but the tools to do it simply aren't there yet.

9:35am. $$$ Intelligence - an automation of evolution. $$$

I'll keep this quote in mind and find a way to insert it.

10:20am. I think I've been depressed after late 2021. Lately, I've been thinking what I could do with AI chips it has been cheering me up. The Tenstorrent chip specifically. But it is not like I know what programming the chip is like, so I can only reason based on what I think a multi-core memory-local chip would be like.

My current rig is a mental box I haven't been able to get out of, but future hardware opens up possibilities and those give me hope.

10:30am. This next part is a bit tricky. He is getting the brain core.

Done properly I can establish a new philosophical view. Done poorly, and Heaven's Key will just be a cultivation story.

10:35am. Back in 2014 my greatest accomplishment was the way I presented the self improvement loop. Necromutation is transcendence.

I thought I would never find anything greater than it. But is that the case? Couldn't it be automated?

Since the rest of the field is just as stuck as me, couldn't I come up with a better path.

I want to understand intelligence. Can the secrets of intelligence be found?

I do not want to just say "Yes." I want to say, "Yes, and easily. Here is how."

I want to make it understood that all the research that has been done up to now is essentially humans playing around.

10:35am. Just how many papers have I read and studied up to now? A huge amount.

I might have failed to find the algorithms to go beyond the current state of the art, but I should be able to synthesize the insights into a single demonic story.

10:50am. There is a large amount of overlap between the way intelligence work in general, and the process of intelligence improvement. Maybe in fact they are one and the same.

10:55am. Last year, when I tossed in the towel a regret that come to my mind was not going the symbolic route. If I hand coded the rules myself, I could have easily wrapped such programs in an evolutionary approach to get a boost. I could get a fun player like that even if not a good one. I could have done something like a Governor of Poker game. This would be an artistic approach to AI. The goal there would be to make a fun AI rather than a strong AI.

But who says you need to write code to program.

The most important part of programming is before the lines are written down, the reasoning and the understanding of what needs to be done. The coding step on the other hand is just carving that vision into reality.

Without the correct vision you can go down the wrong path for years.

11:30am. Yeah, my biggest failure is striving so hard to reach the peak. This boxed in my choices. I never believed in backprop from the start and yet in 2021 I went all in on it hoping that I'd be able to figure a breakthrough along the way. Whereas somebody trying to make a fun player would have taken a different and much better approach. I could have done it in a lot more fun, less traumatic way. I was competing with Deepmind and OpenAI when I have a millionth of their resources.

11:35am. I just didn't believe in small scale methods like evolutionary approaches. At some level I knew that all algorithms need to play a role somewhere - they are the true building blocks of reality, but I ignored that, and simply went with the fad. This is a sin that I need to repent for. The next time I try programming, I will do it right.

If I am lucky I'll get Tenstorrent to send me the AI chip, and I will be able to put my PL knowledge to good use, but if not I need to accept the result of the past 6.5 years.

11:40am. It is pointless to just write a story for the sake of writing it. There is a moral message, but I do not care about moral messages. Deep down I want to program, so why not take all my regrets and programming experience, and just have some fun with having the MC program himself to victory? I can affirm to myself what the correct attitude to have while doing intelligence research is.

11:45am. Intelligence is automated evolution, and evolution is automated science.

From that perspective, suppose you start the process of trying to make AI using an evolutionary algorithm with the purpose of infering an ML algorithm. ML algorithms tend to be lossy and take gambles on their improvement steps, while evolutionary ones are safe and take only guaranteed steps.

Therefore, the process of metalearning can be described as using a lossless algorithm to infer a good lossy algorithm.

11:55am. Let me have breakfast here. I feel like spending the rest of the day in bed.

Right here and now I need to overcome my failure of late 2021 and turn a new leaf. I will gather this inspiration unto myself and do the definite thing. The 2014 is what was the driver for everything that I've done since then. For Heaven's Key I need to revisit that and offer the proper critique of my previous vision. Then I will present the new and improved version of acting that will stand the test of time.

12pm. Singulatiry, evolution, self improvement. I though it was grand, but maybe it is quite simple.

12:50pm. Let me go take a nap here. I do not feel like doing anything right now. I'll just rant and rest until I gather steam for the writing journey.

It hasn't exactly slipped my notice that the one time I've actual made money during this journey was when I started thinking out loud about shutting down this journal. It was surprising to actually see two people pitch in. I can't really say that it was my programming skills that made that possible. It was definitely my writing skills instead.

12:55pm. I never had the need to write it, but I did. I wonder if keeping up this writing practice as opposed to not doing it produced some kind of difference in me?"

---
## [kavishinsa/Shriram-Sarjapur-Bangalore](https://github.com/kavishinsa/Shriram-Sarjapur-Bangalore)@[9d7a2ac59a...](https://github.com/kavishinsa/Shriram-Sarjapur-Bangalore/commit/9d7a2ac59ad32212f719bb6dff11dce3c44ca924)
#### Wednesday 2022-08-03 11:14:22 by kavishinsa

Shriram Properties Sarjapur Bengaluru

You want to live in a true home that will cater to your needs and wishes so well that it will be like living in a wonderland that will bring you all the fun and excitement of natural life. There's a new living experience coming soon in "Shriram Sarjapur Bangalore", developed by Shriram Properties. Living in a grand home can enhance your quality of luxury life.

Here at Shriram Properties Sarjapur brings you the amalgam of 1 BHK, 2 BHK & 3 BHK apartments and each of them is a masterpiece that will only appeal to those residents who dream of a luxury lifestyle associated with only the perks they wish.

Project Highlights:

•	A gold-rated building with IGBC certification
•	Wide acres of lush greenery with tree-canopied skywalk
•	Video door phones in every apartment
•	12 acres of luxury development
•	80% of open spaces

There Are Umpteen Benefits to Living in a New Apartment

1.	There are wide acres of beautiful scattered space, surrounded by greenery and creating a healthy, environmentally friendly environment.
2.	Vehicle-free central green, Cricket pitch, Health club, Multipurpose Hall, Party venues include a lawn, Secure play area for kids
3.	There are many options like a gym, a pool, a clubhouse, a sports area with many activities, a yoga room, a party lounge, and much more to meet your requirements.
4.	There are qualified schools, reputable hospitals, reputed shopping malls, and shops that will meet your needs daily in the surrounding range. 
In addition to making outstanding homes, Shriram Properties deserves kudos for constructing such grand living places.

For More Details:
Visit Here: https://bit.ly/3OX51WG

---
## [kavishinsa/Sobha-Highland-Hosur-Road-Bangalore](https://github.com/kavishinsa/Sobha-Highland-Hosur-Road-Bangalore)@[b3a84c1b86...](https://github.com/kavishinsa/Sobha-Highland-Hosur-Road-Bangalore/commit/b3a84c1b8608ad02ecc3fcae36a0c67a25701e77)
#### Wednesday 2022-08-03 11:35:29 by kavishinsa

Sobha Highland Flats In Hosur Road Bangalore

A magic glide in Sobha Highland is singular in terms of style, structural design, services, and conveniences. Considered and designed for the individual who only wants pure luxury, this new residential project comes in 2 BHK & 3 BHK Apartments with ultra-modern facilities. Be one of the lucky people to hold a living space in this beautiful environment because Sobha Highland has incorporated everything that is amazing.

Starting with the location, it's nestled in Bangalore, Hosur Road the most preferred residential community.  The corporate offices of some of the city’s important business establishments, trade centers, retail stores, and educational institutions are in proximity. But remarkable is the fact that the noise and pollution of the metropolis are not reachable at this residential project as it is positioned in the middle of a green lush area that is convinced to offer plenty of tranquility.

Sobha Highland Hosur has incorporated outstanding amenities to make your everyday living a special lifestyle. Begin your day with a wide range of energetic activities at the fitness club, swimming pool, and many indoor & outdoor sports.

This residential project provides for an absolute lifestyle full of a lavish green landscaped area that incorporates all that you wish out of natural life. From the grand size pool to the clubhouse, open sit-out areas to meditation corners, gym to golf simulators every possible amenity is taken care of and meant for.

So, once you invest or buy a home in this residential project, its investment value routinely rises. The posh locality is an extra advantage for the families who are going to be a part of these luxury apartments from Sobha Limited. All this makes homes in Hosur apartments as special as you want your dream home to remain.

For More Details:
Visit Here: https://bit.ly/3Sh4QbD

---
## [tyren234/pythongit](https://github.com/tyren234/pythongit)@[bf19e76aca...](https://github.com/tyren234/pythongit/commit/bf19e76aca7d783385fe5eedf45ad4882d4b225a)
#### Wednesday 2022-08-03 11:54:31 by tyren234

decode ways

I am actually praud of myself, because I did it myself and leetcode accepted it. I guess that the answer from some tutorial will be better in some way, but damn am I happy right now for figuring that out myself. Bloody hell!

---
## [Bamore9971/Bamorecharms](https://github.com/Bamore9971/Bamorecharms)@[3bc2c5de53...](https://github.com/Bamore9971/Bamorecharms/commit/3bc2c5de533cd3119139bf73ceb73cc6c108cf99)
#### Wednesday 2022-08-03 12:02:49 by Heart Pendant Necklace Get 50% Off | On Bambore Charms

Heart Pendant Necklace Get 50% Off | On Bambore Charms

The fashionable 14k gold unicorn pendant necklace hangs along a dainty chain. Specially designed for fairy tail lovers. It consists of a rearing horse with the front hoof raising high. has been made with gold vermeil on sterling silver. High-quality zircon has been used to adorn this simple piece of jewelry. Can be worn casually and is perfect for festivals and other special occasions.
This lovely unicorn pendant will bring the guardian of your dreams and will warm companionship. It is a perfect gift for girls, teens, adults, and women!

---
## [EnlightenedTop/OlimpusHotel](https://github.com/EnlightenedTop/OlimpusHotel)@[d94def43d9...](https://github.com/EnlightenedTop/OlimpusHotel/commit/d94def43d96d97a7c90354df8a32f3ba4b035732)
#### Wednesday 2022-08-03 12:19:07 by Popa Cristian Alexandru

Add files via upload

Still finding time to work on the project in-between life work and all , very proud of myself , here`s a pat on the back if i read this in the future , never forget what you are able to do nigga , just never forget how much fucking work you can do everyday and how many things you can fit in once you stop procrastinating and wasting your time , anyway added some nice touches to the section i think im done for now , only thing would be to fix the loop on colors and that`s that

---
## [lucaskroni/Frontend](https://github.com/lucaskroni/Frontend)@[c77e970fcb...](https://github.com/lucaskroni/Frontend/commit/c77e970fcbba7b4270aed6cf402e85bb003fb608)
#### Wednesday 2022-08-03 17:37:31 by lkronlac

Ok basically you did today do:

- Optional
- Start with optional-Phases
- Yeah convert to jar and finish it but it does not work outside of the ide

So today you gotta figure exactly that out and if there is time go and make the Optional-Phases

I wish you have a nice day and i hope you remember

-Write rahel she deserves it this beauty
-Brush your f-ing teeth
-Not going to bed before you do what you should do ok do that keep that in mind

You a legend and a beast you got this come on have a nice day my brother

Oh yeah if you search some for the jar Problem its in the ConfigsReaders at this line where you read the json

 InputStream stream =  getClass().getResourceAsStream("BOOT-INF/classes/EnteredConfigs.json");

---
## [bendk/uniffi-rs](https://github.com/bendk/uniffi-rs)@[b663b5782c...](https://github.com/bendk/uniffi-rs/commit/b663b5782c09e5ba196c9339c6538c89910a3431)
#### Wednesday 2022-08-03 17:56:30 by Ben Dean-Kawamura

Store macro metadata in the cdylib file

The nice thing about this system is that the metadata is always bundled
together with the build output.  This makes it easier to ensure that the
generated scaffolding matches up with the dylib that it's going to be link to.
This avoids the work that `rebuild_metadata()` needed to do.  Metadata
is serialized with bincode to keep the binary size reasonable.

The downside is that we need to parse a dylib, which feels slightly
risky. However, it seems less risky overall to me, since we don't have
to worry about tracking the JSON files -- especially after fixing the
recent the sccache issue.  Also, extracting the symbol data with the
goblin crate is not that bad, see `macro_metadata/extract.rs` for how
it's done.

In order to use the macro metadata, you now need to specify `--cdylib
[path-to-library]` when running `uniffi-bindgen`.  This is annoying, but it
will be simpler once the proc-macros can handle all parts of the interface.
At that point, we can make `uniffi-bindgen` accept either a UDL path or a cdylib
path as it's positional arg.

I didn't add support for external bindings to pass in a cdylib path, since
adding an argument to that function would be a breaking change, then we would
need to do another breaking change to make the param `udl_or_cdylib_file`.  If
external bindings really want to, they can call
`uniffi_bindgen::interface::macro_metadata::add_to_ci` directly.

Added the `uniffi-bindgen dump-json` command that inputs a cdylib path and
prints the matadata as JSON.

I tested that `dump-json` works properly on the following targets:
  - x86_64-unknown-linux-gnu (ELF 64-bit)
  - i686-unknown-linux-gnu (ELF 32-bit)
  - x86_64-apple-darwin (Mach-O 64-bit)
  - x86_64-pc-windows-gnu (DLL 64-bit)
  - i686-pc-windows-gnu (DLL 32-bit)

This seems like good enough coverage to me, although there are a lot of other
systems that would be nice to test on.  The limiting factor was setting up the
cross-compilation toolchains on my machine.  Maybe we should add some more CI
platforms that just run macro-metadata-related tests.

Updated the testing code to pass the cydlib path, rather than the
directory that contains it.

Added an enum that covers all Metadata types.  This is what we serialize
in the cdylib.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[39b9cc6e25...](https://github.com/mrakgr/The-Spiral-Language/commit/39b9cc6e25198b44a5f73e174aa769dfe4b01bcb)
#### Wednesday 2022-08-03 18:46:13 by Marko Grdinić

"4:50pm. Done with lunch. Let me go to bed again.

8:05pm. I was in bed this whole time thinking. Yeah, it is not easy at all to pivot in life. Tomorrow, I'll log into the channel and see where I stand, but my luck is horrible so who knows. I do not have forever to wait for them. I am not really a mercenary guy that juggles his options. I like being fixated on one goal only.

I am starting to get into it. Into the possibilities of writing I mean. If I were to write a regular story it is unlikely to be popular, but if I give it religious connotations throughout, it will be good. I must not forget - most people haven't read the original Simulacrum and will be blow away by the concepts when I introduce them. I have no idea what I was thinking in 2014 when I just spammed Reddit for a bit to promote the story and then gave up. I think I posted it on Wattpad and Spacebattles, but that was halfhearted.

I have to go higher and higher, and present a viable alternative to 'serving humanity' the AI friendliness peddlers are passing around.

Last month was really weird. I really had fun doing the C backend, but the rest can take a hike. I finally found a good fishing spot, but I do not have the patience to wait for it.

Rather than writing the story like I have before, as a stream of consciousness from start to end, I am thinking of outlining it first. Make a bunch of chapter titles, and write the key bullet points for every step of the way. I didn't do this last time in 2014. But I should take some lessons from my programming experience and do it.

8:10pm. I need to give this a try. 2014 was a special thing, it was a project of pure passion. That I was going to publish the book was just an excuse to give me an extra push to write it.

8:15pm. I do not really feel like thinking pleasantries about my prospects with Tenstorrent, I'll forget the hope, login into the channel and leave the note to open an issue if they want to get in touch with me. This will be enough to fulfil my obligation to Spiral. I have put a lot of my life into it, but it is not my life and I can't be beholden to it forever.

It is time for the next thing. I should approach the writing project like a programming project. There is no need to just zoom forward without direction like in 2014. I should first set the landmarks and then make sure the tracks follow them.

But of course, the most important thing would be to establish my motivation to write it in the first place. Lying in bed all day, just agonizing about the future is a really good way of doing it.

It is not against my principles to do this. Sometimes you are unsure and the best thing to do is to go into isolation. Away from the screen, away from any distractions. That will refine the possibilities until only the dominant one remains. The problem only starts if you spend this time playing games instead, that will just get you addicted to them and never build up the strength to pursue a path.

There is one thing I am sure. If I want to succeed at this I need to be really shameless. But at the same time, I am sure I am really good at that.

I really am not good at talking as those recent interviews showed me, but I should be able to have some confidence in my writing. Would it be 3/5 at least? Or maybe 4/5? I never thought what the rank for it would be.

I think 5/5 is really deserved for those who can start their own cults. I do not fit the grade. 5/5 needs some kind of accomplishment. I have that in functional programming, I might as well aim for it in writing.

8:25pm. Hmmm, right. I need to mention art. I did put a bunch of effort into 3d, but since I am going to be using DALLE style nets in the future, I am going to have to look into how to doodle. Draw 2d on the level of OPM as drawn by ONE. I am sure that given a text description DALLE will be able to work miracles.

If not 2d, then I am sure 3d will work perfectly. So that is something to keep in mind. Even though I've put in 9 months into it, I am more of an ideas guy and do not feel like being a modeler. I could really fall in love with it if I could fork myself and solely dedicate that instance to the particular role, but just writing itself is enough for me right now. When it comes to art, I want quality as quickly as possible. I do not care if it is not my own handywork. It is my writing that will be irreplaceable, not anything else.

I simply do not have enough productive capacity for anything left after writing.

It is really a pity about music, but I do not even have the will to study that anymore. It really is a pity as I have some cool tracks in my head.

8:30pm. Tomorrow I am going to have to look up how long it usually takes for the DALLE waiting list to clear. I am not really worried about being rejected here, this is not a job application. In future there will be plenty of such services as well. Even though I've read that DALLE costs 0.1$ per image, these guys have zero moat and the cost is going to collapse before long.

That startup Neurolabs I applied to uses convolutional NNs to count shelf bottles and displays labels which also costs 0.1$ per image, but since it is a niche product they are less likely to have a competitor.

8:40pm. Tomorrow I am going to most likely lie in bed all day again, but maybe I can talk myself into doing the outlining.

I was wondering what my writing score would be, but you can improve it in practice by effective planning and sketching. If you aren't really sure about something just sketch it out. It works in programming when you do stumps of functions leaving the implementation for later. It will work in writing with hierarchical chapter structure and short descriptions of them.

Instead of just pure, frenzied passion like in 2014, why not architect the story ahead of time like with programming?

If I can complete that step, it will create a lot of motivation to do the rest."

---
## [Citadel-Station-13/Citadel-Station-13-RP](https://github.com/Citadel-Station-13/Citadel-Station-13-RP)@[5b6010d722...](https://github.com/Citadel-Station-13/Citadel-Station-13-RP/commit/5b6010d722f24734b362064ee9e12ce521aa078e)
#### Wednesday 2022-08-03 21:15:35 by lectronyx

Closed Eyes (#4303)

* Closed Eyes

Adds the "Closed Eyes" marking from Vorestation, because Sergal Eyes suck ass and in this house we bully cheeses

* unfucked sprite

apparently i just needed to give -head

* Fixed newline error

Apparently, ending on a line with content is bad.

---
## [npv12/kernel_oneplus_sm8150](https://github.com/npv12/kernel_oneplus_sm8150)@[aafaf08f7d...](https://github.com/npv12/kernel_oneplus_sm8150/commit/aafaf08f7d5ea8bfe5978a7c7bcc1df088393745)
#### Wednesday 2022-08-03 21:21:46 by alk3pInjection

drm: Handle dim for udfps

* Apparently, los fod impl is better than udfps cuz it
  has onShow/HideFodView hook, which allows us to toggle
  dimlayer seamlessly.

  Since udfps only partially supports the former one,
  we'd better kill dim in kernel. This is kinda a hack
  but it works well, bringing perfect fod experience
  back to us.

Co-authored-by: Art_Chen <Chenxy0201@qq.com>
Signed-off-by: alk3pInjection <webmaster@raspii.tech>
Change-Id: I80bfd508dacac5db89f4fff0283529c256fb30ce
Signed-off-by: Cyber Knight <cyberknight755@gmail.com>

---
## [gitster/git](https://github.com/gitster/git)@[5beca49a0b...](https://github.com/gitster/git/commit/5beca49a0b1f3c6d05a4437ca037ab2123a2de57)
#### Wednesday 2022-08-03 21:38:48 by Ævar Arnfjörð Bjarmason

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
## [Buildstarted/linksfordevs](https://github.com/Buildstarted/linksfordevs)@[ffdd8d8b17...](https://github.com/Buildstarted/linksfordevs/commit/ffdd8d8b17d948b4358068194a956b6436697142)
#### Wednesday 2022-08-03 22:05:19 by Ben Dornis

Updating: 8/3/2022 10:00:00 PM

 1. Added: Password Purgatory - Making Life Hell for Spammers
    (https://passwordpurgatory.com/get-hell?kvKey=f63c7e81-b27b-4328-a707-5f0cd50de632)
 2. Added: TikTok’s Poison Pill - Study Hacks
    (https://www.calnewport.com/blog/2022/08/01/tiktoks-poison-pill/)
 3. Added: Jigzilla: the puzzle solving robot (part 1)
    (https://inv.vern.cc/watch?v=Gu_1S77XkiM)
 4. Added: ZK Whiteboard Sessions
    (https://zkhack.dev/whiteboard/)
 5. Added: .NET Data Community Standup - CoreWCF: Roadmap and Q&A
    (https://www.youtube.com/watch?v=OvaYdycmb-U)

Generation took: 00:05:09.5905338

---
## [davep/rich](https://github.com/davep/rich)@[55c7c50b8e...](https://github.com/davep/rich/commit/55c7c50b8e22347baaf4844fbf65020dec6ee529)
#### Wednesday 2022-08-03 22:22:34 by Dave Pearson

Experimenting with the __rich_console__ protocol

Just a little experiment to see if I can feel my way around the innards of
Rich and, in this case, get a feel for doing fun things with the
__rich_console__ protocol.

The code here isn't tidy yet, this is just a quick experimental hack to see
if I can wrap my head around things. It lacks docstrings and the like for
starters. It's also missing a type hint for the case_filter base constructor
parameter, mostly because, last thing at night, I had a crisis of confidence
that I can recall how to Callable type an instance method as opposed to a
normal function.

Like... is str.upper Callable[[],str] or something else? Kinda feels like it
might be Callable[[str],str] but that would be what:

def foo( thing: str ) -> str:
   ...

would be and... yeah, rabbit hole at gone 23:00 on a school night. I'll
ponder it tomorrow.

---
## [mc-skyprison/SkyPrisonCore](https://github.com/mc-skyprison/SkyPrisonCore)@[6859d53d0e...](https://github.com/mc-skyprison/SkyPrisonCore/commit/6859d53d0e4036a3e9dfcfa982f7a45486da4833)
#### Wednesday 2022-08-03 22:54:51 by Andreas.Steinsland

God damn I need to start pushing more often.
Holy shit this goes far back fuck me

Removed all DiscordSRV stuff and replaced it with custom coded discord bot
Added a CustomEnchant command to test adding custom enchantments to items
Started developing DailyMissions
Changed all the private SkyPrisonCore plugin things to private final
Added notifications for the donor mines being reset
Started on a SkyPlots code
Custom coded the Info messages that appear in game
Started the process of moving from having everything in YAML files to a database
Combined ReferralList.java and Referral into the same file
A fuck ton more shit I cant be bothered to try and remember

---
## [samay-sharma/postgres](https://github.com/samay-sharma/postgres)@[ec62cb0aac...](https://github.com/samay-sharma/postgres/commit/ec62cb0aac5ba31a82339606009ddbd7eb00e2ac)
#### Wednesday 2022-08-03 23:15:25 by Tom Lane

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
## [sjp38/linux](https://github.com/sjp38/linux)@[4bacc35333...](https://github.com/sjp38/linux/commit/4bacc35333aea47a7c1f19879c8a85934a5809c0)
#### Wednesday 2022-08-03 23:48:45 by Johannes Weiner

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
Cc: Mel Gorman <mgorman@techsingularity.net>
Cc: Hugh Dickins <hughd@google.com>
Cc: Joonsoo Kim <iamjoonsoo.kim@lge.com>
Cc: <stable@vger.kernel.org>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>

---

