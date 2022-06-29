## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-06-28](docs/good-messages/2022/2022-06-28.md)


1,743,315 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,743,315 were push events containing 2,613,612 commit messages that amount to 196,560,717 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 32 messages:


## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[707fbfac7e...](https://github.com/tgstation/tgstation/commit/707fbfac7e11837865d70587011aa8197b1d0c35)
#### Tuesday 2022-06-28 00:02:24 by san7890

[MDB Ignore] Shifts all (sane) varedited signs to directionals  (#68004)

* [MDB Ignore] Shifts all (sane) varedited signs to directionals

Hey there,

So we have these cool new sign directionals now, but we still have all of the old pixel-shifted pre-fabrications lying around. So, I added an UpdatePaths (as well as Updated the Paths) to be a bit better at using directionals, because directionals are pretty neato.

This should update every single var_edit that used the proper 32 pixelshift (some of them used 28, and I'm unable to account for that automatically with current tooling) into a proper subtype. Mappers tend to learn by looking at well established maps, so it's always important to ensure that the well-established maps use the most recent tooling (i.e.: bring them up to the surface) and avoid needless excess lines in maps.

* The Commit With All The Maps

OH GOD OH FUCK

* Renames the UpdatePaths

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[6cbe2c9e78...](https://github.com/treckstar/yolo-octo-hipster/commit/6cbe2c9e780176c57dbf1173335fee9c3da09021)
#### Tuesday 2022-06-28 00:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [StarStation13/StarStation13](https://github.com/StarStation13/StarStation13)@[8f0df7816b...](https://github.com/StarStation13/StarStation13/commit/8f0df7816bae3c5dedf599611cda3e6039024e14)
#### Tuesday 2022-06-28 00:34:14 by Kylerace

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
## [ChakatStormCloud/Tannhauser-Gate](https://github.com/ChakatStormCloud/Tannhauser-Gate)@[fb4f191c52...](https://github.com/ChakatStormCloud/Tannhauser-Gate/commit/fb4f191c52772cb5d718bbd399361b36cb8d7732)
#### Tuesday 2022-06-28 01:11:58 by Zonespace

[MDB IGNORE] Mirrors 67324 (#13928)

* [MDB Ignore] OH GOD OH FUCK OH SHIT OH LORD - SPACE AND RUINS IS BROKEN (#67324)

So, for the last few days on production, Space Ruin generation has refused to work. Why is this? It's because in #67107 (cfc233052885dd294b2e7e676caaf84a2a37592b), we repathed `/area/space`  to `/area/misc/space` (lol i should have paid attention to that) without updating everything in code to match. I couldn't seem to get `/area/misc/space` to properly work somehow (this could have also been something I was doing wrong), but I worked it back to just making everything vanilla `/area/space` and all of those unwanted behaviors should be squashed out. Let's get the game working again.

* fix

* fix2

Co-authored-by: san7890 <the@san7890.com>

---
## [mattwoodrow/WebKit](https://github.com/mattwoodrow/WebKit)@[3c797154a8...](https://github.com/mattwoodrow/WebKit/commit/3c797154a8045f544770a8081272a738567fc125)
#### Tuesday 2022-06-28 01:18:21 by Matt Woodrow

Don't allocate backing stores for non-animated compositing layers with zero opacity
https://bugs.webkit.org/show_bug.cgi?id=241935

Reviewed by NOBODY (OOPS!).

We currently allocate (and paint) a backing store for opacity:0 layers, so that we can
initiate animations faster. Unfortunately this uses a lot of memory, so we're going to
try skipping this, and allocating/painting on demand when an animation is started.

This adds a new test with various opacity:0 layers, with and without animations. It also
tests the case where we animate 0 to 0, which could in theory skip a backing store, but
doesn't yet (and is unlikely to be a problem in the wild).

* LayoutTests/compositing/backing/zero-opacity-expected.txt: Added.
* LayoutTests/compositing/backing/zero-opacity.html: Added.
* LayoutTests/compositing/backing/zero-opacity-invalidation-expected.txt: Added.
* LayoutTests/compositing/backing/zero-opacity-invalidation.html: Added.
* LayoutTests/compositing/geometry/bounds-ignores-hidden-dynamic-negzindex-expected.txt:
* LayoutTests/compositing/geometry/fixed-position-flipped-writing-mode-expected.txt:
* LayoutTests/compositing/visibility/layer-visible-content-expected.txt:
* Source/WebCore/rendering/RenderLayerBacking.cpp:
(WebCore::RenderLayerBacking::containsPaintedContent const):
* Source/WebCore/style/Styleable.cpp:
(WebCore::Styleable::mayHaveNonZeroOpacity const):
* Source/WebCore/style/Styleable.h:

---
## [san7890/bruhstation](https://github.com/san7890/bruhstation)@[ee7875d02f...](https://github.com/san7890/bruhstation/commit/ee7875d02f244300eb6a0591fc42a828b4701ace)
#### Tuesday 2022-06-28 01:21:46 by san7890

OH GOD DAMMIT FUCKING BITCH SHIT

I HATE CONSTANT EXPRESSIONS!!!! I HATE CONSTANT EXPRESSIONS!!!!

GHHHHIIIIIILLLLLLLLLLLKKKKKKKKKKKKKKKKKKEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRRR

---
## [AllTheMods/ATM-7](https://github.com/AllTheMods/ATM-7)@[8bff1fe476...](https://github.com/AllTheMods/ATM-7/commit/8bff1fe4769e3ecd98814c640bc44640ee6e9f1a)
#### Tuesday 2022-06-28 01:36:31 by 90

Add more starting books

Tome now also includes guides/READMEs from Blood Magic, Evilcraft, RFTools, Roots Classic, SecurityCraft, Silent Gear, Spice of Life: Carrot Edition, The One Probe and The Twilight Forest.

---
## [LesterJones/CodeWars](https://github.com/LesterJones/CodeWars)@[8231c25d02...](https://github.com/LesterJones/CodeWars/commit/8231c25d0251b2c82d1f7bc48a85034527685aac)
#### Tuesday 2022-06-28 02:17:41 by Lester Jones

Create TheMillionthFibonacci

ESCRIPTION:
The year is 1214. One night, Pope Innocent III awakens to find the the archangel Gabriel floating before him. Gabriel thunders to the pope:

Gather all of the learned men in Pisa, especially Leonardo Fibonacci. In order for the crusades in the holy lands to be successful, these men must calculate the millionth number in Fibonacci's recurrence. Fail to do this, and your armies will never reclaim the holy land. It is His will.

The angel then vanishes in an explosion of white light.

Pope Innocent III sits in his bed in awe. How much is a million? he thinks to himself. He never was very good at math.

He tries writing the number down, but because everyone in Europe is still using Roman numerals at this moment in history, he cannot represent this number. If he only knew about the invention of zero, it might make this sort of thing easier.

He decides to go back to bed. He consoles himself, The Lord would never challenge me thus; this must have been some deceit by the devil. A pretty horrendous nightmare, to be sure.

Pope Innocent III's armies would go on to conquer Constantinople (now Istanbul), but they would never reclaim the holy land as he desired.

In this kata you will have to calculate fib(n) where:

fib(0) := 0
fib(1) := 1
fin(n + 2) := fib(n + 1) + fib(n)
Write an algorithm that can handle n up to 2000000.

Your algorithm must output the exact integer answer, to full precision. Also, it must correctly handle negative numbers as input.

HINT I: Can you rearrange the equation fib(n + 2) = fib(n + 1) + fib(n) to find fib(n) if you already know fib(n + 1) and fib(n + 2)? Use this to reason what value fib has to have for negative values.

HINT II: See https://mitpress.mit.edu/sites/default/files/sicp/full-text/book/book-Z-H-11.html#%_sec_1.2.4

---
## [fuck-you-rory/sam-devteam.github.io](https://github.com/fuck-you-rory/sam-devteam.github.io)@[73cdc29705...](https://github.com/fuck-you-rory/sam-devteam.github.io/commit/73cdc297058c0eb630d432ea3166dc627935ca5f)
#### Tuesday 2022-06-28 02:51:24 by fuck-you-rory

Merge pull request #1 from fuck-you-rory/fuck-you-rory-patch-1

Create awesome.cs

---
## [TDKorn/my-magento](https://github.com/TDKorn/my-magento)@[678628cfca...](https://github.com/TDKorn/my-magento/commit/678628cfca9f78bfaf2fbd252e66b22c07fd2e65)
#### Tuesday 2022-06-28 03:58:35 by TDKorn

Update README I think this was a mistake

* Oh my god?? That took so long
* What
* What am I gonna do when I update literally anything
* It's kinda 🆒 though 😎

---
## [dillytin/crawl](https://github.com/dillytin/crawl)@[af92d4a5d6...](https://github.com/dillytin/crawl/commit/af92d4a5d6ba2f841e8bfdf8639f77a784fcaeae)
#### Tuesday 2022-06-28 04:12:05 by Nicholas Feinberg

Make Hell Knights evil again (catern)

Lost this when they lost Pain.

Slightly hacky.

---
## [Die4Ever/deus-ex-randomizer](https://github.com/Die4Ever/deus-ex-randomizer)@[a29391e06f...](https://github.com/Die4Ever/deus-ex-randomizer/commit/a29391e06f7381cb52afa2dda450c0a656b0e4d9)
#### Tuesday 2022-06-28 04:23:09 by theastropath@gmail.com

Added bingo events for killing the sick man in Battery Park who wants to
die, giving money to the junkie who lives under Maggie Chow, and for
getting the VersaLife maps from the guy in the Old China Hand

---
## [pederng/dwm](https://github.com/pederng/dwm)@[67d76bdc68...](https://github.com/pederng/dwm/commit/67d76bdc68102df976177de351f65329d8683064)
#### Tuesday 2022-06-28 04:50:51 by Chris Down

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
## [WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER](https://github.com/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER)@[85bea07c0f...](https://github.com/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/commit/85bea07c0f6acb8fe0e03fd4e6c593ee8f7c0b14)
#### Tuesday 2022-06-28 06:35:55 by WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER

xmas-sgo2107-domain-BLOOMBERG-COLUMBIA

#Subject: Fwd: Fwd:Fwd:Fwd:Fwd:Fwd:Fwd:Fwd:Fwd:» » » STATE FARM - B

/S/ BO DINCER

    ----- Forwarded Message -----
    From: "Bo Dincer" <b.dincer@columbia.edu>
    To: "Office of Public Affairs" <opa@ftc.gov>, "atlanta@sec.gov" <atlanta@sec.gov>, "boston@sec.gov" <boston@sec.gov>, "CommissionerPeirce@sec.gov" <CommissionerPeirce@sec.gov>, "CommissionerRoisman@sec.gov" <CommissionerRoisman@sec.gov>, "denver@sec.gov" <denver@sec.gov>, "dfw@sec.gov" <dfw@sec.gov>, "IMShareholderProposals@sec.gov" <IMShareholderProposals@sec.gov>, "miami@sec.gov" <miami@sec.gov>, "news@sec.gov" <news@sec.gov>, "webmaster@sec.gov" <webmaster@sec.gov>, "alex.kress@wilsonelser.com" <alex.kress@wilsonelser.com>, "Chair" <chair@sec.gov>, "craig.brinker@wilsonelser.com" <craig.brinker@wilsonelser.com>, "craig.hunter@wilsonelser.com" <craig.hunter@wilsonelser.com>, "curt.schlom@wilsonelser.com" <curt.schlom@wilsonelser.com>, "daniel.flores@wilsonelser.com" <daniel.flores@wilsonelser.com>, "fellows@abfm.org" <fellows@abfm.org>, "Marlyn Delva" <mmt22@columbia.edu>, "ricki.roer@wilsonelser.com" <ricki.roer@wilsonelser.com>, "roger.gottilla@wilsonelser.com" <roger.gottilla@wilsonelser.com>, "sean.wagner@wilsonelser.com" <sean.wagner@wilsonelser.com>, "thomas.manisero@wilsonelser.com" <thomas.manisero@wilsonelser.com>, "William McKenzie" <wmckenzi@nycourts.gov>, "william.behr@wilsonelser.com" <william.behr@wilsonelser.com>, "​ainfo@buildings.nyc.gov" <ainfo@buildings.nyc.gov>, "​Angela.Weis@cityofchicago.org" <Angela.Weis@cityofchicago.org>, "​bbrief@bloomberg.net" <bbrief@bloomberg.net>, "​blawre@bloomberg.net" <blawre@bloomberg.net>, "​bloombergsupport@bloomberg.net" <bloombergsupport@bloomberg.net>, "​DOB-ECBVioAppeals@buildings.nyc.gov" <DOB-ECBVioAppeals@buildings.nyc.gov>, "​DOBMarshal@buildings.nyc.gov" <DOBMarshal@buildings.nyc.gov>, "​Education@rebny.com" <Education@rebny.com>, "​fellows@abfn.org" <fellows@abfn.org>, "​iceglobalnetwork-info@ice.com" <iceglobalnetwork-info@ice.com>, "​ICEIndices@ice.com" <ICEIndices@ice.com>, "​licensing@dos.ny.gov" <licensing@dos.ny.gov>, "​mharvey13@bloomberg.net" <mharvey13@bloomberg.net>, "​msrbsupport@msrb.org" <msrbsupport@msrb.org>, "​newyork@SEC.GOV" <newyork@sec.gov>, "​nycdevelopmenthub@buildings.nyc.gov" <nycdevelopmenthub@buildings.nyc.gov>, "​Rule-comments@sec.gov" <Rule-comments@sec.gov>, "​TO-ICENGX@ice.com" <TO-ICENGX@ice.com>, "inspector.general@eeoc.gov" <inspector.general@eeoc.gov>, "DZUCKER@mskyline.com" <DZUCKER@mskyline.com>, "Laskowitz, Shari" <slaskowitz@ingramllp.com>, "lzucker@mskyline.com" <lzucker@mskyline.com>, "Bo Dincer" <BD2561@columbia.edu>, "colin.brooks@morgan.stanley.com" <colin.brooks@morgan.stanley.com>
    Sent: Sun, Dec 19, 2021 at 5:51 AM
    Subject: Fwd: Fwd:Fwd:Fwd:Fwd:Fwd:Fwd:Fwd:Fwd:» » » STATE FARM - B

            They still have not returned my tapes.
                    
            Also, the Judge in court seems to find nothing wrong with them filming my private and sexual activities INSIDE of my apartment...
                      
            OK?
                     
            Have a nice day.
               
                         
            » » » STATE FARM - BLOOMINGTON » » » Northern Trust Company. ACRIS 6MM

                From: BD DINCER (COLUMBIA UNIVERSITY) At: 12/18/21 18:37:40 UTC-5:00
                To: Susan Byrne (WESTWOOD MANAGEMENT ) , Julie Hoyer (STATE FARM MUTUAL AU ) , Greg Shull (STATE FARM MUTUAL AU ) , Jeffrey Attwood (STATE FARM MUTUAL AU ) , John Malito (STATE FARM MUTUAL AU ) , Steven Santiccioli (NORTHERN TRUST COMPA ) , Robert Stephan (STATE FARM MUTUAL AU ) , Lisa Rogers (STATE FARM MUTUAL AU ) , Elena Khoziaeva (BRIDGEWAY CAPITAL MA ) , Bill Trauner (STATE FARM MUTUAL AU ) , Heather Caldwell (STATE FARM MUTUAL AU ) , Theresa Baker (STATE FARM MUTUAL AU ) , Tammy Gipson (STATE FARM MUTUAL AU ) , Brent Reeder (NORTHERN TRUST COMPA ) , Michael Whipple (BRIDGEWAY CAPITAL MA ) , Michael Zaroogian (STATE FARM MUTUAL AU ) , Terence Lynch (GAINSCO SERVICE CORP ) , Rebekah Holt (STATE FARM MUTUAL AU ) , Katie Hubbard (STATE FARM MUTUAL AU ) , Leigh Ann Rogalski (STATE FARM MUTUAL AU ) , Chad Moser (STATE FARM MUTUAL AU ) , Tim Zelgert (STATE FARM MUTUAL AU ) , Ray Renken (STATE FARM MUTUAL AU ) , Kara Olson (STATE FARM MUTUAL AU ) , Jim Chan (BLACKROCK INSTITUTIO ) , Matt Harvey (STATE FARM MUTUAL AU ) , Steve Brucker (STATE FARM MUTUAL AU ) , John Socha (STATE FARM MUTUAL AU ) , Jennifer Hsui (BLACKROCK INSTITUTIO ) , Joe Young (STATE FARM MUTUAL AU ) , Wade Reinthaler (STATE FARM MUTUAL AU ) , Scott Reid (STATE FARM MUTUAL AU ) , Adam Hallman (STATE FARM MUTUAL AU ) , Tyler Smith (STATE FARM MUTUAL AU ) , Wei Hao (STATE FARM MUTUAL AU ) , Chris Minter (STATE FARM MUTUAL AU ) , Shelly Marsh (STATE FARM MUTUAL AU ) , Hollie Marsh (STATE FARM MUTUAL AU ) , Matthew Lockridge (WESTWOOD MANAGEMENT ) , Rich Rebholz (STATE FARM MUTUAL AU ) , Michael Mayberger (STATE FARM MUTUAL AU ) , Ashley Smock (STATE FARM MUTUAL AU ) , Brian Bengtson (STATE FARM MUTUAL AU ) , Cory Swartzlander (STATE FARM MUTUAL AU ) , Scott Lawson (WESTWOOD MANAGEMENT ) , Ayman Bari (STATE FARM MUTUAL AU ) , Adam Vales (STATE FARM MUTUAL AU ) , Robert Middleton (STATE FARM MUTUAL AU ) , Shane Jent (STATE FARM MUTUAL AU ) , Kevin Rock (STATE FARM MUTUAL AU ) , Mark Dunford (STATE FARM MUTUAL AU ) , Jean-Francois Ducrest (DUCREST, JEAN-FRANCO ) , Caroline Dirks (STATE FARM MUTUAL AU ) , Kyle Gilmore (STATE FARM MUTUAL AU ) , Diane Hsiung (GEODE CAPITAL MANAGE ) , Hunter Rose (STATE FARM MUTUAL AU ) , Cameron Kurak (STATE FARM MUTUAL AU ) , Mark Broughton (FIRST REPUBLIC BANK ) , Betsey Euliss (STATE FARM MUTUAL AU ) , Kim Bretz (STATE FARM MUTUAL AU ) , Jon Wilson (STATE FARM MUTUAL AU ) , Numan Ahmed (STATE FARM MUTUAL AU ) , Walter Ruane (STATE FARM MUTUAL AU ) , Shawna Barlow (STATE FARM MUTUAL AU ) , Philip Kroger (STATE FARM MUTUAL AU ) , Gabrielle Poole (STATE FARM MUTUAL AU ) , Ricardo Correa (STATE FARM MUTUAL AU ) , Felipe Castella (STATE FARM MUTUAL AU ) , Matt Krebsbach (STATE FARM MUTUAL AU ) , Gabriel Prado Correa (STATE FARM MUTUAL AU ) , Larnita Gates (STATE FARM MUTUAL AU ) , Ketrick Karsten (STATE FARM MUTUAL AU ) , Sophie Kim (STATE FARM MUTUAL AU ) , Vicki Trimpe (STATE FARM MUTUAL AU ) , Christin Higham (STATE FARM MUTUAL AU ) , BD DINCER (COLUMBIA UNIVERSITY ) , b.dincer@columbia.edu
                Cc: Kerri Saperstein (MORGAN STANLEY & CO. ) , COLIN.BROOKS@MORGAN.STANLEY.COM
                Subject: Fwd:Fwd:Fwd:Fwd:Fwd:» » » STATE FARM - BLOOMINGTON » » » Northern Trust Company. ACRIS 6MM

                    From: BD DINCER (COLUMBIA UNIVERSITY) At: 12/18/21 18:34:03 UTC-5:00
                    To: Kerri Saperstein (MORGAN STANLEY & CO. ) , colin.brooks@morgan.stanley.com
                    Cc: james.gorman@morganstanley.com
                    Subject: Fwd:Fwd:Fwd:Fwd:» » » STATE FARM - BLOOMINGTON » » » Northern Trust Company. ACRIS 6MM

                        From: BD DINCER (COLUMBIA UNIVERSITY) At: 12/18/21 18:27:47 UTC-5:00
                        To: james.gorman@morgan.stanley.com
                        Cc: Christina Constantine (FINRA ) , Ms Hy (MORGAN STANLEY INVES ) , Ms Hyld (MORGAN STANLEY ) , Peter Melley (FINRA ) , Susan Byrne (WESTWOOD MANAGEMENT ) , Julie Hoyer (STATE FARM MUTUAL AU ) , Greg Shull (STATE FARM MUTUAL AU ) , Jeffrey Attwood (STATE FARM MUTUAL AU ) , John Malito (STATE FARM MUTUAL AU ) , Steven Santiccioli (NORTHERN TRUST COMPA ) , Robert Stephan (STATE FARM MUTUAL AU ) , Lisa Rogers (STATE FARM MUTUAL AU ) , Elena Khoziaeva (BRIDGEWAY CAPITAL MA ) , Bill Trauner (STATE FARM MUTUAL AU ) , Heather Caldwell (STATE FARM MUTUAL AU ) , Theresa Baker (STATE FARM MUTUAL AU ) , Tammy Gipson (STATE FARM MUTUAL AU ) , Brent Reeder (NORTHERN TRUST COMPA ) , Michael Whipple (BRIDGEWAY CAPITAL MA ) , Michael Zaroogian (STATE FARM MUTUAL AU ) , Terence Lynch (GAINSCO SERVICE CORP ) , Rebekah Holt (STATE FARM MUTUAL AU ) , Katie Hubbard (STATE FARM MUTUAL AU ) , Leigh Ann Rogalski (STATE FARM MUTUAL AU ) , Chad Moser (STATE FARM MUTUAL AU ) , Tim Zelgert (STATE FARM MUTUAL AU ) , Ray Renken (STATE FARM MUTUAL AU ) , Kara Olson (STATE FARM MUTUAL AU ) , Jim Chan (BLACKROCK INSTITUTIO ) , Matt Harvey (STATE FARM MUTUAL AU ) , Steve Brucker (STATE FARM MUTUAL AU ) , John Socha (STATE FARM MUTUAL AU ) , Jennifer Hsui (BLACKROCK INSTITUTIO ) , Joe Young (STATE FARM MUTUAL AU ) , Wade Reinthaler (STATE FARM MUTUAL AU ) , Scott Reid (STATE FARM MUTUAL AU ) , Adam Hallman (STATE FARM MUTUAL AU ) , Tyler Smith (STATE FARM MUTUAL AU ) , Wei Hao (STATE FARM MUTUAL AU ) , Chris Minter (STATE FARM MUTUAL AU ) , Shelly Marsh (STATE FARM MUTUAL AU ) , Hollie Marsh (STATE FARM MUTUAL AU ) , Matthew Lockridge (WESTWOOD MANAGEMENT ) , Rich Rebholz (STATE FARM MUTUAL AU ) , Michael Mayberger (STATE FARM MUTUAL AU ) , Ashley Smock (STATE FARM MUTUAL AU ) , Brian Bengtson (STATE FARM MUTUAL AU ) , Cory Swartzlander (STATE FARM MUTUAL AU ) , Scott Lawson (WESTWOOD MANAGEMENT ) , Ayman Bari (STATE FARM MUTUAL AU ) , Adam Vales (STATE FARM MUTUAL AU ) , Robert Middleton (STATE FARM MUTUAL AU ) , Shane Jent (STATE FARM MUTUAL AU ) , Kevin Rock (STATE FARM MUTUAL AU ) , Mark Dunford (STATE FARM MUTUAL AU ) , Jean-Francois Ducrest (DUCREST, JEAN-FRANCO ) , Caroline Dirks (STATE FARM MUTUAL AU ) , Kyle Gilmore (STATE FARM MUTUAL AU ) , Diane Hsiung (GEODE CAPITAL MANAGE ) , Hunter Rose (STATE FARM MUTUAL AU ) , Cameron Kurak (STATE FARM MUTUAL AU ) , Mark Broughton (FIRST REPUBLIC BANK ) , Betsey Euliss (STATE FARM MUTUAL AU ) , Kim Bretz (STATE FARM MUTUAL AU ) , Jon Wilson (STATE FARM MUTUAL AU ) , Numan Ahmed (STATE FARM MUTUAL AU ) , Walter Ruane (STATE FARM MUTUAL AU ) , Shawna Barlow (STATE FARM MUTUAL AU ) , Philip Kroger (STATE FARM MUTUAL AU ) , Gabrielle Poole (STATE FARM MUTUAL AU ) , Ricardo Correa (STATE FARM MUTUAL AU ) , Felipe Castella (STATE FARM MUTUAL AU ) , Matt Krebsbach (STATE FARM MUTUAL AU ) , Gabriel Prado Correa (STATE FARM MUTUAL AU ) , Larnita Gates (STATE FARM MUTUAL AU ) , Ketrick Karsten (STATE FARM MUTUAL AU ) , Sophie Kim (STATE FARM MUTUAL AU ) , Vicki Trimpe (STATE FARM MUTUAL AU ) , Christin Higham (STATE FARM MUTUAL AU ) , BD DINCER (COLUMBIA UNIVERSITY ) , Donald Rizer (FINRA ) , Paul Aragon (FINRA ) , b.dincer@columbia.edu, chair@sec.gov
                        Subject: Fwd:Fwd:Fwd:» » » STATE FARM - BLOOMINGTON » » » Northern Trust Company. ACRIS 6MM

                            From: BD DINCER (COLUMBIA UNIVERSITY) At: 12/18/21 18:22:34 UTC-5:00
                            To: Kerri Saperstein (MORGAN STANLEY & CO. ) , james.gorman@morganstanley.com
                            Cc: bd2561@columbia.edu
                            Subject: Fwd:Fwd:» » » STATE FARM - BLOOMINGTON » » » Northern Trust Company. ACRIS 6MM

                                From: BD DINCER (COLUMBIA UNIVERSITY) At: 12/18/21 18:21:00 UTC-5:00
                                To: bo.dincer@yahoo.com
                                Subject: Fwd:» » » STATE FARM - BLOOMINGTON » » » Northern Trust Company. ACRIS 6MM



                                    From: BD DINCER (COLUMBIA UNIVERSITY) At: 12/18/21 18:20:35 UTC-5:00
                                    To: Michael Karp (FINRA ) , Brian Carr (FINRA ) , Trudy Clarke (FINRA ) , William Downey (FINRA ) , Jay Loftus (FINRA ) , Viviana Lui-Chan (FINRA ) , Marc Freeman (FINRA ) , newyork@sec.gov, chair@sec.gov
                                    Cc: Kerri Saperstein (MORGAN STANLEY & CO. ) , b.dincer@columbia.edu, bondstrt@protonmail.com
                                    Subject: » » » STATE FARM - BLOOMINGTON » » » Northern Trust Company. ACRIS 6MM

                                        From: BD DINCER (COLUMBIA UNIVERSITY) At: 12/18/21 18:15:44 UTC-5:00
                                        To:  Ms. Hayashi (NOMURA SECURITIES CO ) ,  Morgan32 Stanley (MORGAN STANLEY ADVTG ) ,  Morgan Stanley154 (MORGAN STANLEY ADVTG ) ,  Morgan Stanley15 (MORGAN STANLEY ADVTG ) ,  Ms Hy (MORGAN STANLEY INVES ) ,  Ms Hyld (MORGAN STANLEY ) 
                                        Cc:  Kerri Saperstein (MORGAN STANLEY & CO. ) ,  Cmo Citibank (CITIBANK NA ) ,  Samriddi Abney (FEDERAL HOME LOAN BA ) ,  Federated Mmktops (FEDERATED INVESTMENT ) ,  Jesse Aguilar (FEDERAL HOME LOAN BA ) ,  Shafat Alam (FEDERAL RESERVE BANK ) ,  Steven Santiccioli (NORTHERN TRUST COMPA ) ,  bd2561@columbia.edu,  colin.brooks@morgan.stanley.com
                                        Subject: Fwd:STATE FARM - BLOOMINGTON  » Northern Trust Company. ACRIS 6MM

                                            Hey SAPS... Merry Christmas!

                                            You think this guy will figure it out???
                                            - THE 6MM? Acris report and 6MM.


                                                              
                                                Brent Reeder

                                                Fund Manager  
                                                Northern Trust Company, The
                                                      +1-312-557-0153 (o)                  181 W Madison St
                                                         bdr11@bloomberg.net (w)             Chicago IL 60602-4510, US

                                                                             Focus       Large Cap Stocks, Growth Investing, United States, Equities, 
                                                                                            Mid Cap Stocks, Small Cap Stocks, Global, United Kingdom, | More »

                                                                             Funds Managed (43 Funds/51.6B Total Assets in USD) | More »

                                                 » » » » » »   590xxxx   



                                               » » » » » »   ???????



                                            Investment Information Analyst
                                            State Farm Mutual Automobile Ins Co
                                                   +1-309-735-2705 (o)                  1 State Farm Plz
                                                   +1-309-530-1865 (m)                  Investment Department E-8
                                                    krock5@bloomberg.net (w)            Bloomington IL 61701, US

                                            You think this guy will figure it out???
                                            - THE 6MM? 

                                                                            Phil Supple                1 Views Today
                                            Spokesperson   Career
                                            State Farm Life Insurance Co                                                                          Current
                                                 +1-800-782-8332 (o)                  1 State Farm Plaza                                       State Farm Life Insurance Co
                                                phil.supple.hid9@statefarm.com (w  Bloomington IL 61710, US    


                                    Subject: STATE FARM - BLOOMINGTON


                                        TY.


                                                            Kevin Rock

                                        Investment Information Analyst
                                        State Farm Mutual Automobile Ins Co
                                            +1-309-735-2705 (o)                  1 State Farm Plz
                                            +1-309-530-1865 (m)                  Investment Department E-8
                                           krock5@bloomberg.net (w)            Bloomington IL 61701, US


                                                                        Phil Supple           1 Views Today
                                        Spokesperson        Career
                                        State Farm Life Insurance Co                                                                          Current
                                               +1-800-782-8332 (o)                  1 State Farm Plaza                                       State Farm Life Insurance Co
                                                phil.supple.hid9@statefarm.com (w  Bloomington IL 61710, US                               Spokesperson



                                                                                   Nicole Tamilyn Bowyer

                                        Attorney
                                        State Farm Insurance
                                             +1-504-840-4900 (o)                  853 Fincastle Turnpike

                                                          +1-504-840-4941 (f)                   North Tazewell VA 24630
                                                        nicole.bowyer@statefarm.com (w)
                                                                              Focus       Legal

                                                         Rebecca Coyle          1 Views Today
                                                    Analyst:Public Policy       Career
                                                    State Farm Life Insurance Co                                                                          Current
                                                           +1-309-766-2311 (o)                  1900 M Street NW                                          State Farm Life Insurance Co
                                                          rebecca.coyle@statefarm.com (w)   Washington DC 20036, US                                Analyst:Public Policy
                                                                                                                                                                         2012-Present


                                                                                                      Steven Santiccioli

                                                    VP:Quantitative Management   
                                                    Northern Trust Company, The
                                                            +1-3124444419 (o)                     Addl Contact Info  »
                                                           312-444-5777 (o)                       181 W Madison St
                                                      steve@bloomberg.net (w)             Chicago IL 60602-4510, 
                                                         sjs5@ntrs.com (w)
                                                                                         I would work harder on my marriage if there was a retirement plan.
                                                                                       Focus       Large Cap Stocks, Growth Investing, Global, Equities, 
                                                                                                     Thematic Investing, United States, Developed Markets

                                                                                       Funds Managed (7 Funds/7.7B Total Assets in USD) | More »
                                                             Fund Name       Tot Ast YTD Ret 3M Px   Objective       Status
                                                    21)        Northern International Equity In        5.5B    7.8             Foreign Blend   ACTV
                                                    22)  Northern Global Sustainability In       1.3B    20.5            Thematic Sector ACTV
                                                    23)  Green Century Equity Fund       552.1M  25.2            Thematic Sector ACTV

                                                                                       Recent News | More »
                                                    41)                 Northern Funds: 497 2019/07/02          EDG     07/2019  

                                                               






    << HAPPY HOLIDAYS and Merry xmas >>

---
## [alphagov/govuk-prototype-kit](https://github.com/alphagov/govuk-prototype-kit)@[0d40cc2786...](https://github.com/alphagov/govuk-prototype-kit/commit/0d40cc2786a4778a583fa8d8abf99b700609fa72)
#### Tuesday 2022-06-28 08:26:31 by Laurence de Bruxelles

Change tests to generate a release archive only once

Use a lockfile to make sure that if the test helper `mkReleaseArchive()`
is called more than once, it won't create more than one
`create-release-archive` process. The behaviour we want is that it all
calls will block until the initial process has finished.

The way I figured to do that was that all calls try and acquire a
lockfile (atomically), if that lockfile is already held that means
another call is already creating the release archive. When the lockfile
is released, the process should have successfully created a release
archive, so no extra work is needed.

Unfortunately, in Node.js it seems there is no way to block waiting for
a lockfile to be released, so we have to rewrite the test utils and all
relevant tests to be asynchronous. To be fair they should have been
asynchronous in the first place, but it was still a very painful
process.

Note that I haven't rewritten the scripts in `cypress/scripts` to use
async functions; without the use of top-level await it was a bit more
effort than I was prepared to do, compounded with the fact that
there doesn't seem to be an easy way to await `child_process.spawn()`
(`util.promisify` doesn't work), and async `child_process.exec()` and
`child_process.execFile()` don't do `stdio: 'inherit'`. Maybe the only
way around it is to use the `execa` library (: Anyway I couldn't be
dealing with that, so now we have to deal with duplication in
`__tests__/util`. There are ...ways... to reduce the duplication
(proper-lockfile does this with its `lib/adapter` module) but they are a
bit magic, and plus it means writing our code using callbacks, which is
just... woof. No.

Anyway as you can tell this is has been a great learning opporunity :')
Just use async the first time and save myself the pain later!!

---
## [GeoB99/reactos](https://github.com/GeoB99/reactos)@[9326ab8fa2...](https://github.com/GeoB99/reactos/commit/9326ab8fa263ac959d46f0e267d7ca61e24688aa)
#### Tuesday 2022-06-28 08:51:40 by George Bișoc

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
## [Roblox-Thot/VapeV4ForRoblox](https://github.com/Roblox-Thot/VapeV4ForRoblox)@[729ed03fce...](https://github.com/Roblox-Thot/VapeV4ForRoblox/commit/729ed03fce6760633724da0f77c65885ef1c5b87)
#### Tuesday 2022-06-28 09:18:52 by Roblox Thot

make the dont use more cancer to look at because

I CAN FUCK YOU

---
## [resiki8182/Fedoraware](https://github.com/resiki8182/Fedoraware)@[5a23d95aca...](https://github.com/resiki8182/Fedoraware/commit/5a23d95aca96005b454a9a9b75ba2ac9ae603c83)
#### Tuesday 2022-06-28 11:46:34 by Johnathon Walnut

Merge pull request #380 from femboy-boop/patch-2

fuck you baan

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[aad0c2680a...](https://github.com/mrakgr/The-Spiral-Language/commit/aad0c2680a8921d41144b6b37c1f344785d67887)
#### Tuesday 2022-06-28 12:20:47 by Marko Grdinić

"10:40am. I could have gotten up even earlier and did the chores, but decided to get more sleep. Tomorrow if this happens again, I am going to get up and do the chores instead. It is time to start getting them done.

Let me chill here.

11am. Let me start here.

So yesterday I gave Genshin Impact a try. The game has beautiful style and world design, but is extremely casual. The only time I've been challenged is when I wandered into a high level zone as lvl 1 and fought against a lvl 19 enemy. The rest is just me being a tourist. I'll get tired of it soon enough.

I got far enough to unlock the gatcha mechanism. I had 2 pulls, on the first one I got some 4 star greatsword I can't use, and on the second pull I got Mona.

https://danbooru.donmai.us/posts/5439412

Going into the game I made up my mind to accept whatever it throws at me, not that I'd have money to spend on rolls anyway, but I do have my preferences, and out of all the characters, Mona is the one I'd most wanted. Interesting that this happened. The odds of rolling a 5 star is only 0.6%.

Incidentally, I really wish I could draw as well as the guy I linked to. Something like the above would be impossible in 3d. It feels that people better at me than art are literally everywhere in this world. I wouldn't have even bothered unless it was to dab on writers.

Sigh, I wish I had time. Well, let me finish my sculpting development. I am going to do an anime character from start to finish. Since it has been 7 months that I did that base mesh, I'll do the whole thing from the ground up to get rid of the rust.

Right now my biggest priority is face and hair. I need some targeted advice on this. The first vid I watched yesterday was too slow, and the last one was too fast. I'll find something good.

11:20am. Focus me. I do not much left to cultivate in 3d. I am close to the end of my apprentice journey. These couple of chara models will mark the end of my apprenticeship.

Last night I thought about what it is that I wanted to do, and I realized that I want to be a writer.

It is true that I also want to pursue omnipotence, but it is not like I have something I want to particularly want to do with that power.

The problem with being a writer is that it has extremely limited cultivation potential. The regular writer's path has you just putting words on paper, and that is it. There is no programming, no AI, no visuals, no music. No nothing.

11:25am. Whereas general art has more of that kind of suffering that I crave.

I am actually a lot scared about the recent development in AI myself. All indications point that it a very resource intensive thing. Rather than doing art, I'd be better accumulating money like I said I would in one of my PL sub posts. So can I really justify doing art, when I should be making money, like those chad chinaman cultivators?

I don't know. But one thing I am sure is that I do not want the pursuit of AI to be like this.

I do not want the ignition of the Singularity to depend on the size of one's bank account. Even though I have fear, I do not want that fear to dominate my actions. It might end up leading to my ultimate loss, a life drive by incompetence and a story of limitations never exceeded.

11:35am. So let me persevere. I am afraid that I might not even make 1k a month from Heaven's Key, but who knows. I'll see where that goes.

https://youtu.be/fQZ7TEdFdMU
Blender 2.9: Anime Girl Head Modeling In 30 Minutes WIP #1

Let me start with this.

https://youtu.be/fQZ7TEdFdMU?t=118

Hmmm, interesting.

https://youtu.be/fQZ7TEdFdMU?t=231

The easiest thing in the world here would be to give up, but I want to accept this curse of labor and continue persevering.

11:40am. The only way I could justify not doing the sculpting is if I draw it myself.

https://youtu.be/RLX78cVyE5Y
Blender 2.9: Anime Girl Head Modeling WIP #2

Let me go a bit further. I am not interested in the modeling stuff too much.

https://youtu.be/RLX78cVyE5Y?t=78

I hate the way they approach the modeling task here. This is a very unnatural way of doing it. With sculpting, you could at least have some artistry to it, but this is just tracing.

https://youtu.be/sdRLrzqOOkI?t=1968

Drawing individual vertices like this...

11:55am. https://www.youtube.com/results?search_query=blender+genshin

I'll watch some of these, but before that.

https://youtu.be/yKMbnrc7IWI
How I Model Anime Hair in Blender

I guess I'll be going with Shonzo again.

I really have no idea why he keeps playing those randoms SFX.

https://youtu.be/yKMbnrc7IWI?t=499

Lots of fiddling with curves. I see. That is how I will be doing it as well. He said something about doing it as pure mesh. I wonder how that works.

After I am done with the tutorials, which will be today, I will sculpt my own head and do a study on it. I will actually try drawing it and do some observation.

12:15pm. https://youtu.be/yKMbnrc7IWI?t=808

It is speed up quite a bit and still takes 50m. Come to think of it, how would Flycat do this?

At any rate, this is a really important prerequisite to clear.

Trying to draw based of high level mental features and off reference would lead to a huge difference in quality.

With anime faces, I am not actually sure what I am even drawing in the first place, even with the CSP model. Whereas with actual refs, the process is similar to tracing.

So doing this 3d part is to answer a very important question - just what should I be drawing.

Once I have a concrete vision, even if one is as bad as I am, the results should be a lot better compared to other /beg/s that skip important parts of the process. This is what you have to do if you don't have a visual library.

12:20pm. Yeah, I should definitely do the clothes as well this time around.

Inside of the mouth too. As well as riging. I should aim for full completion this time. Let me do a list.

* Sculpt base mesh with an anime head.
* Do the hair.
* Do the inside of the mouth.
* Do the clothes.
* Texture it.
* Retopo and rig it.
* Do the Genshin look for it.
* After all the above is done, do a drawing study from various angles.

The above list is basically all that I've yet to do in 3d apart from animation. After I conquer that I'll be very complete as a 3d illustrator and will be able to move on to music. Well, I'll have to do a few of such models before I am ready to move on to that.

12:25pm. A month should be enough for this.

https://youtu.be/yKMbnrc7IWI?t=1470

Hmmm, did he turn that into mesh around this point.

https://youtu.be/yKMbnrc7IWI?t=1554

Lots of messing around. But 3d is a lot closer to programming in that regard. If you make a program and there are bugs in it, you don't dump it overboard and do it all from scatch. Instead you modify it a bit to fix the error.

In contrast, the way 2d artists do it is just bizzare. They are much more likely to just dump it and start again.

12:45pm. https://youtu.be/yKMbnrc7IWI?t=1684

Let me pause here. It is time for breakfast.

1:20am. Let me resume. It really is quite difficult to follow this path.

I am going to put a stopgap measure. If I can't get to the point where I want by the end of the year, I am going to take a break for a month and then start applying to programming jobs. That sort of thing would be far easier, and the income I could put into ML.

There is no point in struggling too much over over this. Either way it will have been worth it to try art once in my life.

But until then, let me just persevere. Wanting to do things with his own power is a man's romance. A woman's romance is marrying somebody powerful.

1:25pm. Let me get back to the vidoe.

https://youtu.be/yKMbnrc7IWI?t=2064

Hmmm, what is he doing here?

1:35pm. https://youtu.be/yKMbnrc7IWI?t=2426

Real time, it probably took him 8x as long than 50m. Meanwhile, a good 2d illustrator could put this up in under an hour.

Yeah, 3d is a tough path to take. The fast part is if you use primitives for most of the scene like in my previous illustration.

1:40pm. Well, in the worst case, I can just get a GAN to generate some anime faces. Job done, easy peasy.

1:50pm. Ok, done.

https://www.youtube.com/results?search_query=blender+genshin

1:55pm. Yeah, I am troubled. I am troubled!

By DALLE no less. I can understand why /ic/ is freaking out so much.

And I have to ask myself at this point - does it really make sense to try to do art myself when a years down the road, I'll let NN do all the work anyway.

I've already decided that getting a job so I can buy hardware to do RL is not worth it. I am extremely peeved at RL.

But getting a job so I can buy hardware to do art? That's another thing entirely.

Why not take it easy?

2:05pm. In late 2021 after I threw in the towel on RL, I was crazy. I was 'AI chips, AI chips, where are my AI chips!? Won't somebody give me an AI chip!?'

2:10pm. Looking at the tutorial I can't help, but think do I want to spend all my fucking time pushing hair around and so on. It would really be great if I could do this and get paid for it, but that is not going to happen unless I start doing art comissions for cheap.

Getting a programming job here might be giving up, but it would not be the same kind of giving up as if I'd gotten a job in late 2021. It is how in 2015 I started programming, only in late 2016 I attained the desire to do my own language.

In the /ic/ thread I saw posts to the effect that if an AI did it it would not be my own voice and feeling, but who care about that. Letting an AI do it is more like being an director, a role which I'd rather much prefer than being an artist.

The really important part of my work is the writing, this cannot be replaced by anybody.

2:15pm. Ok, nevermind that for today. Let me just watch the Genshin look vid now. Tomorrow I will start doing early morning chores and start thinking about applying to Generally Intelligent or whatever ML companies are there. I'll dust off my resume, append the 3d software knowledge to it and pass it around."

---
## [jasoncmyers/mame2003-plus-custom](https://github.com/jasoncmyers/mame2003-plus-custom)@[fecf11dfbd...](https://github.com/jasoncmyers/mame2003-plus-custom/commit/fecf11dfbdf77f24dc20531d5bc489c5ec9fb80f)
#### Tuesday 2022-06-28 13:11:16 by Kyland K

Killer Instinct 1 and 2 Cheats Update! (#1325)

Note: Being that this the initial addition of massively updated KI1 and KI2 Cheats, please do not expect all Cheats to fully function as advertised! Some of the Cheats may be subject to change in future Updates!

Killer Instinct 1 and 2 Cheats Update!
Killer Instinct 1: Attack and Movement Speed Manipulation via Updated Cheats (cheat.dat)!

Selection of 12 different speeds and 21 different sizes, including Defaults.  You can choose to move as slow as molasses, or as fast as a Jedi!  Fight as a metaphorical watching paint dry sloth, or as frenetic as a one inch punch from Bruce Lee!  You can also be as small as a mouse or as large as a Kaiju!

Dozens of other Cheats added for both Killer Instinct 1 and 2, including Automated Ultra Combos and Humiliations and No Mercy Finishers!

Personal thanks to Mahoneyt944 and Abystus for their incredible efforts and insight in this little project I personally wanted to implement to help better lower spec platforms!

retroarch/system/mame2003-xtreme/cheat.dat

retroarch/system/mame2003-plus/cheat.dat

If using 2003 Plus, you must delete the .rzip, before the new cheat.dat will take effect!

R2 to open MAME Menu on 2003 Xtreme; L3 or Core Options to do the same for 2003 Plus.

Select Cheats, Apply, Resume Game, Rinse and Repeat, Enjoy the Performance/Speed Boost!

---
## [thelazier/dash](https://github.com/thelazier/dash)@[67ceda1b5a...](https://github.com/thelazier/dash/commit/67ceda1b5aa0c51f1fdce4fb71ccba1922e880f6)
#### Tuesday 2022-06-28 15:09:10 by fanquake

Merge #18295: scripts: add MACHO lazy bindings check to security-check.py

5ca90f8b598978437340bb8467f527b9edfb2bbf scripts: add MACHO lazy bindings check to security-check.py (fanquake)

Pull request description:

  This is a slightly belated follow up to #17686 and some discussion with Cory. It's not entirely clear if we should make this change due to the way the macOS dynamic loader appears to work. However I'm opening this for some discussion. Also related to #17768.

  #### Issue:
  [`LD64`](https://opensource.apple.com/source/ld64/) doesn't set the [MH_BINDATLOAD](https://opensource.apple.com/source/xnu/xnu-6153.11.26/EXTERNAL_HEADERS/mach-o/loader.h.auto.html) bit in the header of MACHO executables, when building with `-bind_at_load`. This is in contradiction to the [documentation](https://opensource.apple.com/source/ld64/ld64-450.3/doc/man/man1/ld.1.auto.html):
  ```bash
  -bind_at_load
       Sets a bit in the mach header of the resulting binary which tells dyld to
       bind all symbols when the binary is loaded, rather than lazily.
  ```

  The [`ld` in Apples cctools](https://opensource.apple.com/source/cctools/cctools-927.0.2/ld/layout.c.auto.html) does set the bit, however the [cctools-port](https://github.com/tpoechtrager/cctools-port/) that we use for release builds, bundles `LD64`.

  However; even if the linker hasn't set that bit, the dynamic loader ([`dyld`](https://opensource.apple.com/source/dyld/)) doesn't seem to ever check for it, and from what I understand, it looks at a different part of the header when determining whether to lazily load symbols.

  Note that our release binaries are currently working as expected, and no lazy loading occurs.

  #### Example:

  Using a small program, we can observe the behaviour of the dynamic loader.

  Conducted using:
  ```bash
  clang++ --version
  Apple clang version 11.0.0 (clang-1100.0.33.17)
  Target: x86_64-apple-darwin18.7.0

  ld -v
  @(#)PROGRAM:ld  PROJECT:ld64-530
  BUILD 18:57:17 Dec 13 2019
  LTO support using: LLVM version 11.0.0, (clang-1100.0.33.17) (static support for 23, runtime is 23)
  TAPI support using: Apple TAPI version 11.0.0 (tapi-1100.0.11)
  ```

  ```cpp
  #include <iostream>
  int main() {
  	std::cout << "Hello World!\n";
  	return 0;
  }
  ```

  Compile and check the MACHO header:
  ```bash
  clang++ test.cpp -o test
  otool -vh test
  ...
  Mach header
        magic cputype cpusubtype  caps    filetype ncmds sizeofcmds      flags
  MH_MAGIC_64  X86_64        ALL LIB64     EXECUTE    16       1424   NOUNDEFS DYLDLINK TWOLEVEL WEAK_DEFINES BINDS_TO_WEAK PIE

  # Run and dump dynamic loader bindings:
  DYLD_PRINT_BINDINGS=1 DYLD_PRINT_TO_FILE=no_bind.txt ./test
  Hello World!
  ```

  Recompile with `-bind_at_load`. Note still no `BINDATLOAD` flag:
  ```bash
  clang++ test.cpp -o test -Wl,-bind_at_load
  otool -vh test
  Mach header
        magic cputype cpusubtype  caps    filetype ncmds sizeofcmds      flags
  MH_MAGIC_64  X86_64        ALL LIB64     EXECUTE    16       1424   NOUNDEFS DYLDLINK TWOLEVEL WEAK_DEFINES BINDS_TO_WEAK PIE
  ...
  DYLD_PRINT_BINDINGS=1 DYLD_PRINT_TO_FILE=bind.txt ./test
  Hello World!
  ```

  If we diff the outputs, you can see that `dyld` doesn't perform any lazy bindings when the binary is compiled with `-bind_at_load`, even if the `BINDATLOAD` flag is not set:
  ```diff
  @@ -1,11 +1,27 @@
  +dyld: bind: test:0x103EDF030 = libc++.1.dylib:__ZNKSt3__16locale9use_facetERNS0_2idE, *0x103EDF030 = 0x7FFF70C9FA58
  +dyld: bind: test:0x103EDF038 = libc++.1.dylib:__ZNKSt3__18ios_base6getlocEv, *0x103EDF038 = 0x7FFF70CA12C2
  +dyld: bind: test:0x103EDF068 = libc++.1.dylib:__ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEE6sentryC1ERS3_, *0x103EDF068 = 0x7FFF70CA12B6
  +dyld: bind: test:0x103EDF070 = libc++.1.dylib:__ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEE6sentryD1Ev, *0x103EDF070 = 0x7FFF70CA1528
  +dyld: bind: test:0x103EDF080 = libc++.1.dylib:__ZNSt3__16localeD1Ev, *0x103EDF080 = 0x7FFF70C9FAE6
  <trim>
  -dyld: lazy bind: test:0x10D4AC0C8 = libsystem_platform.dylib:_strlen, *0x10D4AC0C8 = 0x7FFF73C5C6E0
  -dyld: lazy bind: test:0x10D4AC068 = libc++.1.dylib:__ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEE6sentryC1ERS3_, *0x10D4AC068 = 0x7FFF70CA12B6
  -dyld: lazy bind: test:0x10D4AC038 = libc++.1.dylib:__ZNKSt3__18ios_base6getlocEv, *0x10D4AC038 = 0x7FFF70CA12C2
  -dyld: lazy bind: test:0x10D4AC030 = libc++.1.dylib:__ZNKSt3__16locale9use_facetERNS0_2idE, *0x10D4AC030 = 0x7FFF70C9FA58
  -dyld: lazy bind: test:0x10D4AC080 = libc++.1.dylib:__ZNSt3__16localeD1Ev, *0x10D4AC080 = 0x7FFF70C9FAE6
  -dyld: lazy bind: test:0x10D4AC070 = libc++.1.dylib:__ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEE6sentryD1Ev, *0x10D4AC070 = 0x7FFF70CA1528
  ```

  Note: `dyld` also has a `DYLD_BIND_AT_LAUNCH=1` environment variable, that when set, will force any lazy bindings to be non-lazy:
  ```bash
  dyld: forced lazy bind: test:0x10BEC8068 = libc++.1.dylib:__ZNSt3__113basic_ostream
  ```

  #### Thoughts:
  After looking at the dyld source, I can't find any checks for `MH_BINDATLOAD`. You can see the flags it does check for, such as MH_PIE or MH_BIND_TO_WEAK [here](https://opensource.apple.com/source/dyld/dyld-732.8/src/ImageLoaderMachO.cpp.auto.html).

  It seems that the lazy binding of any symbols depends on whether or not [lazy_bind_size](https://opensource.apple.com/source/xnu/xnu-6153.11.26/EXTERNAL_HEADERS/mach-o/loader.h.auto.html) from the `LC_DYLD_INFO_ONLY` load command is > 0. Which was mentioned in [#17686](https://github.com/bitcoin/bitcoin/pull/17686#issue-350216254).

  #### Changes:
  This PR is one of [Corys commits](https://github.com/theuni/bitcoin/commit/7b6ba26178d2754568a1308d3d44e038e9ebf450), that I've rebased and modified to make build. I've also included an addition to the `security-check.py` script to check for the flag.

  However, given the above, I'm not entirely sure this patch is the correct approach. If the linker no-longer inserts it, and the dynamic loader doesn't look for it, there might be little benefit to setting it. Or, maybe this is an oversight from Apple and needs some upstream discussion. Looking for some thoughts / Concept ACK/NACK.

  One alternate approach we could take is to drop the patch and modify security-check.py to look for `lazy_bind_size` == 0 in the `LC_DYLD_INFO_ONLY` load command, using `otool -l`.

ACKs for top commit:
  theuni:
    ACK 5ca90f8b598978437340bb8467f527b9edfb2bbf

Tree-SHA512: 444022ea9d19ed74dd06dc2ab3857a9c23fbc2f6475364e8552d761b712d684b3a7114d144f20de42328d1a99403b48667ba96885121392affb2e05b834b6e1c

---
## [tumenicooks/tumenicooks](https://github.com/tumenicooks/tumenicooks)@[1e41625666...](https://github.com/tumenicooks/tumenicooks/commit/1e41625666b63cdf0e68dbfa70b2e997b90f026c)
#### Tuesday 2022-06-28 16:02:35 by tumenicooks

Create Day 4: rockpaperscissors

cuz fuck logic amirite, came up with a simpler solution than using >, <, etc etc operators. Was too lazy to change code towards lecture solution cuz I got everything running anyway, including the invalid number prompt.

Also skipped a day cuz literally dropped ded and slept the entire night yesterday

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[55d9ca16a8...](https://github.com/mrakgr/The-Spiral-Language/commit/55d9ca16a8ea57a51f0bdff8665305346e1fec76)
#### Tuesday 2022-06-28 16:03:06 by Marko Grdinić

"3:05pm. Done with the bath. What I've done just now is gotten Anatomy For Sculptors.

I think I am just losing my nerve here. Yeah, there is nothing wrong with getting a job. There is nothing wrong with not wanting to spend all my time drawing or sculpting the same thing over and over again. It is not wrong to be nervous about my prospects as a writer or being desirous of higher income and safety that programming would provide me.

But there is nothing wrong with wanting to learn art either. There is always time to learn something. I might not have time to do an untold number of models, but I do have time to do a few of them.

Like I said, I can spend a month doing this.

4:05pm. What is the problem then?

Anime.

I am being overwhelmed by it.

Stylized art seems easier at first glance, and for bad artists it in fact is. It is true that it is a shortcut in all sorts of ways, but what it isn't a shortcut is for learning.

It is always a mistake to try to grasp the feeling directly.

What I should be doing is a starting with realistic bodies and simplifying them down to anime.

CSP models aren't good for this. Just what will I do with those dull hollow eyed models.

Once I understand exactly what my charas should be in 3d, that is when I am ready to actually draw them. I'll do the anime face in 3d and come to understanding of what the various expressions should be in 3d for any kind of perspective.

4:10pm. It is not bad to obsess about realism at this stage. I can easily smooth the model and remove detail after I am done with that. That is the point of stylization.

This is the direction I picked for my env art. It is time to replicate the same thing my chara art.

In a way what I've done with Scatter 5 with the city scene is what I should have done back in January instead of going to Houdini. An expert can do in a day what would take a novice months. If I had to do the flower scene today, I could easily do it in Blender in just a few days in a far simpler fastion than in Houdini.

4:15pm. Forget about the shitty technique of that VR tuber guy. Trying to do it like him is absolutely the wrong way to go. I'd honestly respect him more if he started with an already finished model and lightly adjusted it. That would have been faster as well.

4:25pm. If I focus on learning proper anatomy first, that will give me an objective measure for how good or bad my model is. What do I know how good a random anime face is?

4:30pm. Methodically going through that book will also give me a reason to redo the base mesh. Last time I was just immitating Flycat, but going by the book is the proper process.

Forget anime, let me prend my goal is to make a bunch of realistic characters.

Come to think of it, there should be some face2anime GANs. It might be worth looking into them once I have the proper model.

4:35pm. One thing I want to do is to make a skeleton as well. This is a good opportunity to do so.

5:15pm. I've decided.

I do not want to pursue the Heaven's Key plan while seriously expecting it will give me money. The value of Heaven's Key is that it cured me of my obsession with poker and made me consider more broadly what could be possible with AI.

Post-Singularity I'll be making stories such as it all the time.

As a human, what is really important is AI itself.

But at the same time it pissed me off not being able to do an anime character. 2022 is my vacation. If I want to spend a few months just sculpting the human body then that is no problem.

As far as environments are concerned, I am feel quite proficient at them now.

Considering how much effort I put into this in 2022, it should be no wonder. But chara modeling has only a single month invested into it.

5:25pm. I can't be mogged by some dumb Youtuber performance art.

If I want money I should just go and get it, and if I want to do art, I should just do art.

5:55pm. 30/228. It's an interesting book. Despite it being mostly pictures, I am making slow progress through it.

I feel like closing here.

I really should reconsider my path. There really is a lot of difference between being able to make a decent picture in under a minute like an AI would taking several days minimum like I do.

I said I would rather make 1k as an artist vs 10k as a programmer, but I should reconsider how sane that really is. Especially considering it is questionable if I am going to get to 1k in the first place. Being humple about my desires does not mean I will fulfil them, so why not have big desires to begin with.

I was wrong to want to rock the online gambling dens, I'd be better off trying to crash the anime industry instead.

6pm. Being good at art is not complicated. Can you do a house, can you do a tree, can you do a car...

You go through the list until you can do everything efficiently. If you can do all that you imagine, then you are good at it.

I'll take aim at the human body again, but I won't bother with struggling against the pros or any of that nonsense. I know I have a 5/5 skill in which I am greatly talented. So there is no point in agitating over being good over something I have low aptitude for. I should just internalize the body, and then move on to the next thing whether that be programming, music or Heaven's Key."

---
## [couriersud/mame](https://github.com/couriersud/mame)@[ba63081d10...](https://github.com/couriersud/mame/commit/ba63081d109c904902958c6324b013cb10b42732)
#### Tuesday 2022-06-28 16:34:40 by 0kmg

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
## [ThetaStation/ThetaStation](https://github.com/ThetaStation/ThetaStation)@[949fbd0194...](https://github.com/ThetaStation/ThetaStation/commit/949fbd019404b32fded90f37e3f6a7548790e55e)
#### Tuesday 2022-06-28 18:13:00 by Emisse

Bagel Update 13.7 (#8690)

* fuck shit ass shit

* Add files via upload

---
## [Calyxman/Foundation-19](https://github.com/Calyxman/Foundation-19)@[04d704a78a...](https://github.com/Calyxman/Foundation-19/commit/04d704a78ac84cbd9fef3ae3c9c68e9232dfccf1)
#### Tuesday 2022-06-28 18:19:26 by Calyxman

Deletes corporations, gets rid of lion-spelling.

Fuck the old one. It was written by a toddler. And none of these old corporations were removed. Fuck you Lion

---
## [SHAMUH2020/initials.py](https://github.com/SHAMUH2020/initials.py)@[2c9a417361...](https://github.com/SHAMUH2020/initials.py/commit/2c9a4173614aa2508136ed70c5d893cfb1da9dd5)
#### Tuesday 2022-06-28 18:59:27 by Shanthamurthy Hanumantharayappa

Update README.md

Receipts for Lovely Loveseats
We’ve decided to pursue the dream of small-business ownership and open up a furniture store called Lovely Loveseats for Neat Suites on Fleet Street. With our newfound knowledge of Python programming, we’re going to build a system to help speed up the process of creating receipts for your customers.

In this project, we will be storing the names and prices of a furniture store’s catalog in variables. You will then process the total price and item list of customers, printing them to the output terminal.

Please note: Projects do not run tests against your code. This experience is more open to your interpretation and gives you the freedom to explore. Remember that all variables must be declared before they are referenced in your code.

---
## [linux-kdevops/kdevops](https://github.com/linux-kdevops/kdevops)@[f81a6593ff...](https://github.com/linux-kdevops/kdevops/commit/f81a6593ff2b46320185dcf36705ae82a3210956)
#### Tuesday 2022-06-28 19:09:10 by Luis Chamberlain

kdevops: generate nodes & Vagrantfile file with jinja2 templating

The file vagrant/kdevops_nodes.yaml is today generated using a set
of scripts which depend on what workflow / filesystem you want to
use. This is ugly and complex.

Likewise the top level vagrant/Vagrantfile is getting quite out of
hand with tons of bells and whistles added for each new technology
we want to add support for.

We can simplify things consirably by just using jinja2 templating,
so that the nodes file is generated based on input in a more
gramatically consistent manner similar to how we generate the
ansible hosts file. Later hope is to just share some of this
code between both.

The vagrant/Vagrantfile is complex because it supports both
virtualbox and libvirt, and it also supports a slew of technologies.
This will only grow more in the future. For example, we'll be
extending it soon with a slew of CXL options. To make things
easier to maintain and to allow this to be easier to grow and
read we now generate the vagrant/Vagrantfile by trimming it
with code which is not needed. This should make it easier for
users to read and understand the file while also extending it
with new features.

Later on we can make things even easier to read by just justing
include files. But take note: jinja2 processing has restrictions
on variables used, so you can't exactly be setting variables to
do complex math and expect them to be carried out on macros.
Hacks like using loop.index, etc are required [0]. If you
need anything complex, that should all be done as on the ansible
tasks variables, as ansible does allow you to do pretty complex
things with variables. Templating should be used for simple
processing. That's it.

We can still do better! For instance, now that we have the power
of stuffing variables within ansible, I don't think we need the
vagrant/kdevops_nodes.yaml file at all. We just have to add data
for simple loops to be processed. Then, in consideration of growth
for new technology, the approach to extend vagrant/kdevops_nodes.yaml
for new technology seems wrong, we should just have to process some
variables on ansible and then have the Vagrantfile have a macro to
process the new technolgy. For instanced, the fact that the code to
support ZNS in the vagrant/Vagrantfile is left in place whether or
not you support ZNS is just cumbersome. We should just define a new
variable for nvme drives and have a bool for zns drives. Then we
split the current nvme set into two arrays and have the template
generation work on two separate arrays using the shared macro. We
may then just want to create a separate PCI root bus for each, one
for regular nvme drives, and another for ZNS drives.

Adding CXL support should learn from these growing pains and lead
the way with cleaner processing.

And again the diff stat says it all:

 27 files changed, 476 insertions(+), 822 deletions(-)

Converting over to generate the required files for terraform using
jinja2 is next. And then we can have a path forward to grow in a very
nice way for both cloud and local virtualization.

[0] https://jinja.palletsprojects.com/en/3.1.x/templates/

Signed-off-by: Luis Chamberlain <mcgrof@kernel.org>

---
## [batrick/ceph](https://github.com/batrick/ceph)@[fecacd1fb3...](https://github.com/batrick/ceph/commit/fecacd1fb33e7d7656211139746eb4d85c5e2e63)
#### Tuesday 2022-06-28 20:50:51 by Patrick Donnelly

qa: use postmerge hooks for filtering stock kernel

Up to now, the k-stock kernel required an awkward matrix configuration
to ensure that we're only testing the rhel stock kernel. This is
basically done by overriding (evil) the yaml fragment specifying the
distribution.  So, you'd have a config like:

	fs/snaps/{begin clusters/1a3s-mds-1c-client conf/{client mds mon osd} distro/{ubuntu_latest} mount/kclient/{mount overrides/{distro/stock/{k-stock rhel_8} ms-die-on-skipped}} objectstore-ec/bluestore-bitmap overrides/{whitelist_health whitelist_wrongly_marked_down} tasks/workunit/snaps}

One would rightly believe it's running with ubuntu but, actually, the
rhel_8 fragment overrides this.

Instead of this, we're using the new postmerge teuthology hooks to
filter our configs containing k-stock when the rhel distribution is not
selected.

This is great (and a small change by itself) but doing so would bias the
selection of jobs towards k-testing/fuse which do not drop configs not
using rhel. To work around this, we add another two rhel (three total)
fragments to the custom `qa/cephfs/distro` to compensate. The extra two
rhel fragments drop if the k-stock config is not in use.  This also
uses the teuthology postmerge hooks.

Simultaneously, we're dropping the random selection of distributions as
it's no longer necessary with nested subsets (another newer teuthology
feature). Instead, modify fs:* sub-suites to divide jobs by 2 to
approximate.

Signed-off-by: Patrick Donnelly <pdonnell@redhat.com>

---
## [mhcwebdesign/opencart-php8](https://github.com/mhcwebdesign/opencart-php8)@[89c304ae61...](https://github.com/mhcwebdesign/opencart-php8/commit/89c304ae61fb683b2ca8ff7dcf5ceabfc4f5a0eb)
#### Tuesday 2022-06-28 20:57:45 by Anton

OC4 return created module_id

IMHO every single model function, creating a row in DB, must return this row id after executed.

I can check `$module_id = $this->db->getLastId();` in my code on clean opencart installation.
But what if this model function calls any `after` events which also insert rows into DB?

This is not a developer friendly software architecture when you need to create hacks, hooks, workarounds and other voodoo magic to get a single value for page redirect.

BUG:
By the way on creating, for example a banner module, on save you are not redirected to created module page. 
So every click on Save button just creates a duplicate of a module.

---
## [NadyaNayme/DalamudPlugins](https://github.com/NadyaNayme/DalamudPlugins)@[ee4b3f2550...](https://github.com/NadyaNayme/DalamudPlugins/commit/ee4b3f25503c231052483b1afe90db91e1720f53)
#### Tuesday 2022-06-28 22:00:18 by Nadya

Tidy Chat 1.2.0

**Changes**

- Adds new filter for blocking the "You can't join Novice Network because it is full" message that appears on every zone change when the game tries to autojoin the Novice Network. This setting is disabled by default and can be found under System->Hide messages shown by default
- The Whitelist has been reworked into a Custom Filters system with the ability to Allow **OR** Block messages based on Substring or RegEx matches.
- Versioning has been changed to a three number system `1.2.0` to prevent users from thinking it may still be beta-quality due to the leading `0` in the old versioning. Tidy Chat will remain `1.x.y` until a total rewrite. `x` will increment when entirely new features are added while `y` will increment whenever new filters are added, bugfixes are made, and/or localization changes are made.

**More on the Custom Filters changes**

- In order to use Regex matches the first and last character must be `/`. For example `some item` is a substring search while `/some item/` is a regex search.
- Filters can override one-another - so be as specific as possible to avoid potential conflicts.
- Last Name and Server Name fields have been hidden, but not removed, so that existing whitelist setups should continue working. However if you need to modify an item in your old whitelist you will need to recreate it. The fields were primarily cosmetic and to help the user enter data correctly - but it was confusing having them when they weren't technically required. To whitelist a friend simply whitelist their name as it appears in chat for you. You can include the server name as `Last@Server`. If you have initialized names it might look like `Firstname L.@ServerName` or even `F. L.@ServerName`
- Much of the help text wasn't updated for the new changes - so sorry for any confusion. It's mostly still accurate though.
- **Please still request for new filters to be added**. While these filters enable you to block/allow message as you please adding personal filters does not benefit other Tidy Chat users. If you think a specific filter would be beneficial for other players to have - please do make a Whitelist Request on Tidy Chat Github repo so that others may benefit without having to write their own filters. This system was made to empower users with have very niche or very complicated requests that I do not wish to implement - it was not created to replace the possible need for more filters.

**Localization**
- French translation has been completed due to the massive efforts of Khayle. Filters still have not reached 100% coverage for French but it's roughly 98% or so - only a few filters are still needed. 
- Tidy Chat is roughly 40% translated for German and is still seeking translators for German, Japanese, Italian, Norwegian, Russian, and Spanish. To help translate join the CrowdIn project! https://crwd.in/tidy-chat

---
## [ClearHeadToDo-Devs/ClearHeadToDo](https://github.com/ClearHeadToDo-Devs/ClearHeadToDo)@[6c90ab4eab...](https://github.com/ClearHeadToDo-Devs/ClearHeadToDo/commit/6c90ab4eab823d3ba10ca05cf2e9ee3ac7889641)
#### Tuesday 2022-06-28 23:46:08 by Darrion Burgess

moving for backup but I don't like this push, there is a problem with
the tests for clap now that I have upgraded so this is a great example
of why we test other dependencies but it makes me kinda annoyed at clap,
although, I suppose it could be argued this is a relatively easy thing
once I figure out what exactly is happening because it might be that I
just don't know how to use fucking iterators

---

