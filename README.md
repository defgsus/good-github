## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-08-16](docs/good-messages/2022/2022-08-16.md)


1,972,292 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,972,292 were push events containing 3,040,676 commit messages that amount to 241,490,403 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 36 messages:


## [chrisbobbe/zulip-mobile](https://github.com/chrisbobbe/zulip-mobile)@[847d6aecc5...](https://github.com/chrisbobbe/zulip-mobile/commit/847d6aecc5eb1722e900da6f12089de545dd30a4)
#### Tuesday 2022-08-16 00:23:13 by Chris Bobbe

UnicodeEmoji [nfc]: Reduce to just what we use; cut out r-n-vector-icons

Emojis aren't icons, so even from its name, it's not clear that
react-native-vector-icons is best suited to render them, even if it
has turned out to be convenient for a subset of emoji (Unicode
emoji).

Like avatars, emojis are a mode of freeform user expression (think
of the "thank you" emoji). Icons, on the other hand, are a palette
of UI elements that UI designers use to convey UI meaning and make
the UI more approachable. ("Ah, a star icon, I bet that'll take me
to starred messages if I press it.")

The createIconSet function from r-n-vector-icons is designed to give
us such a palette of UI elements: we're to call it once, at module
top-level, and and it'll give us a React component that can render
any one of a static menu of icons. We've co-opted that into "a
static menu of Unicode emoji," but that's worked fine so far.

But, with #2956, we don't want a static menu, we want a menu that's
defined by the server. That's a breaking point for continuing to use
createIconSet here. We'd have to handle these constraints:
  - We can't call createIconSet at module top-level anymore, since
    we don't have the server data at that time.
  - We'd have to call it before it's time to render a Unicode emoji.
  - We shouldn't call it in the render pass of Emoji, or of any
    React component. That would mean the UnicodeEmoji component (or
    whatever we label createIconSet's return value) would get
    recreated each time. So, wherever we ask a UnicodeEmoji element
    to be created in the JSX, we'd be asking for a different `type`
    every time, and each new `type` would cause an unmount/remount:
      https://reactjs.org/docs/reconciliation.html#elements-of-different-types
    . That's an important performance concern when many Unicode
    emoji are rendered at a time.
…And all that just seems like too much trouble to keep around
something that isn't designed for this use case anyway.

So, as a first step, in this commit, take part of createIconSet's
returned component [1] -- just enough to preserve current behavior
-- and define it in a separate file. It's pretty small, so, go ahead
and convert to a function component while we're at it. After this,
it'll be an easy switch to consume data from Redux, with
useSelector.

[1] node_modules/react-native-vector-icons/lib/create-icon-set.js

---
## [clark-lindsay/fluid-habits](https://github.com/clark-lindsay/fluid-habits)@[b78f9d6e72...](https://github.com/clark-lindsay/fluid-habits/commit/b78f9d6e72af9db96224eebd89f9be876a0676e0)
#### Tuesday 2022-08-16 01:26:30 by clark-lindsay

Add "eligibility gate" to `create_achievement/1`

  - Overall, I think this is a positive change for the data model,
    because I want to enforce having a certain number of achievemen
    levels defined for an activity before a user begins adding
    achievements, to ensure that they are giving themselves options
    - something funny about enforcing rules to improve "fluidity", but
      in my experience it really does work
  - I am not pleased that I had to sprinkle some extra set-up code in a
    couple of spots throughout the tests to ensure that enough
    achievement levels were defined such that an activity _is_ in fact
    _eligible_ for the test; but these things can probably be extracted
    and cleaned up once I am more confident that I am going down the
    right path

---
## [Mumiago/MFU-Updated](https://github.com/Mumiago/MFU-Updated)@[b0a82f48ea...](https://github.com/Mumiago/MFU-Updated/commit/b0a82f48ea580260d51ee2e6e46b00593b363044)
#### Tuesday 2022-08-16 01:37:11 by Krsmanovic-S

rise of the resistance

-right side USA doesn't fuck you with the federal acts (now it gives same civs and mils as left side, previously you got fucked by having 30 mils and 10 civs from each act; Last Act (Social Security) still the same, so we have some difference at the end.
-Italy +6 civs from start, -1 dock from focus, some consumer good reduction removed, Yugo and Greece eco for italy increased as well
-Albania gives +3 civs but no docks anymore
-1 port in Greece removed
-Resistance mission no longer reduces compliance
-French resistance focuses +base resistance is gone (still scales, just doesn't give Ger instant +40 resistance)
-Japans two focuses that switched you to navy side (interservice rivalry) got this change removed (it fucked the whole system and you could never go army dominant)
-armor support companies don't fuck you speed (missing just 1 tank of those slows the entire div down), this applies to meds and lights, heavies still affect speed
-morozov removed -5 ic, instead gives +15% research speed
-AT piercing increased (but for line AT, support AT alone gives less pierce)
-unsloaped armor doesn't give 2.5% stats anymore
-Nomohan event now fires a reminder for everyone (war eco time)
-Marines and rocket arty have better amphib attack (with stacked marines before you had 200 stats)
-Heavy tanks lose the +5 stats they got from GrafMeer modding and also they are worse in terrain now
-Italy got 5% more research speed from an idea, some oil refs to help with the fuel, a bit better research buffs (excav and construction were changed, other bonis are the same)
-Italy now starts with 36 Light tank. 36 Medium tank, Armored Cars and Marine tech

---
## [jxnding/leetcode](https://github.com/jxnding/leetcode)@[d6317958ab...](https://github.com/jxnding/leetcode/commit/d6317958ab262611c9e074a0a5932561c4f87e24)
#### Tuesday 2022-08-16 01:45:42 by Zhaoxiong Ding

# reachable-nodes-with-restrictions
Started at 9:24PM

## Python
Fuck this shit. They call this a "tree" but there's cycles and undirected edges.
Honestly tho, fuck me for not just doing DFS. Never hurts to "protect" yourself with a visited set.

---
## [newstools/2022-express](https://github.com/newstools/2022-express)@[0d941a91a4...](https://github.com/newstools/2022-express/commit/0d941a91a4c012fca2753cb2af6e0043f0d28435)
#### Tuesday 2022-08-16 01:55:30 by Billy Einkamerer

Created Text For URL [www.express.co.uk/news/science/1655498/energy-crisis-horror-without-electricity-boy-will-die-millions-fuel-poverty-gas-bills]

---
## [OxygenCobalt/Auxio](https://github.com/OxygenCobalt/Auxio)@[cafead8a88...](https://github.com/OxygenCobalt/Auxio/commit/cafead8a8871e5bff361a9dcda46b61c5fc58917)
#### Tuesday 2022-08-16 02:00:53 by Alexander Capehart

deps: upgrade to android 13 [#129]

FINALLY upgrade to android 13.

I cannot believe it had to take until the release of the version to
finally update the SDK version, but of course it had to. For some
insane reason that I have no idea why it passed QA, the 33 SDK had
a crippling issue where attributes were not recognized. The only
way to fix this was to:

1. Upgrade to the newer studio version (Chipmunk Patch 2)
2. Upgrade to AGP 7.3.0-beta05.

Funny thing though. AGP 7.3.0 IS NOT COMPATIBLE WITH CHIPMUNK. Okay,
so we can upgrade to Dolphin then and then we can use AGP, right?
HAHAHA NOPE! Dolphin hasn't patched out the XML issue yet despite
every other release channel having a release on August 3rd. Did
some engineer at google just forget to make a release? What?

Okay, so I guess I'm forced to use Electric Eel, the UNSTABLE CANARY
VERSION that IS FILLED WITH BUGS. But oh wait, Electric Eel doesn't
like AGP 7.3.0 EITHER! It wants AGP 7.4.0, which IS ALSO IN ALPHA.
So, I'm forced to use the ALPHA studio and the ALPHA AGP version just
to use the android 13 SDK in a way that is not completely unbearable.

The android SDK, everyone.

(This is not a cry for help, I just want to write down my infinite
frustration with this stupid goose chase somewhere)

---
## [meedan/pender](https://github.com/meedan/pender)@[64605616ce...](https://github.com/meedan/pender/commit/64605616ce5a8fca4fd4b66289e82dec36946cbd)
#### Tuesday 2022-08-16 02:15:41 by Christa Hartsock

Update Instagram GraphQL URL for items

At some point recently the URL we use to query GraphQL data for
Instagram items stopped returning the data we need. This updates that
URL with (honestly kinda magical) query params that make the
query work again. It's possible this will change again in the future--
would be nice to find an approach that works and is documented.

Here's the StackOverflow post that suggested the query params
needed: https://stackoverflow.com/a/72582413

CHECK-1201

---
## [tgstation/auxlua](https://github.com/tgstation/auxlua)@[a95fd40550...](https://github.com/tgstation/auxlua/commit/a95fd40550c6bdd13d21d1c920b4e0881e6012d2)
#### Tuesday 2022-08-16 02:28:22 by Y0SH1M4S73R

you know what, fuck you clippy *`#[allow(clippy::cmp_owned)]`* [release]

---
## [andrewkern/pyslim](https://github.com/andrewkern/pyslim)@[1079788221...](https://github.com/andrewkern/pyslim/commit/10797882210885f2156a03ccbe8041822d5e3640)
#### Tuesday 2022-08-16 03:43:49 by andrewkern

added slim clone and compile to GH actions

alter when to run actions for dev

add windows to list of oses

pip failing

conditional on slim build

add slim windows build rule

MORE WINDOZE

adding SLiM depends

debugging

think we are working?

still debugging

still futzing

thrash

adding autotools to msys2 install stuff

thrash

add conda

thrash

get rid of tmate

thrash

dont' need source proffile?

ugh

tmate revenge

adding conditional on tmate

removed source from build

tmatey

setup auto conda env

updated tests

moar tests

typo

mamba

no pip?

ugh

back to miniconda

pwr

yml

moar

mamba redux?

blurg

yarg

still going

last one

Update tests.yml

blag2

altering conda vs pip balance

urg

jkhj

shell nightmare

try another change

which pip

moving stuff

adsf

dsfk

asd

adsfdasf

msys shell madness

asdfasdf

Update tests.yml

as;dlkfj

sadf

happy windows filepaths from conf

sdafdsa

passing tests!

remove dev branch action

removed print

comment out slim build step on osx/ubuntu

Update tests.yml

comments

refactor test actions

trying to limit matrix of sys / env

exclude rather than include

arrays

less is more

even fewer jobs?

kjh

sdf

more excludes?

last one for the night

jhlkj

asd

jkhkj

lkjlkj

sad

tmate

adfasdf

which dot file?

why isn't conda working?

try again

asdfasdf

bump cache

no base

asdf

fast debug

mamba with osx

micro

fixing micromamba

try cache on micro

add linux in

oops should have been ubuntu

actually try tests for a min

okay here we go windoze

conditions

now with tests

even cleaner

cache slim

true

cache2

cawde

undo cache

parathenses

asdfsad

cache redux

final clean

moar

new cache path

tmate to find windows path

cache path again

zstd

path again

sdfasd

kjhglghj

more zstd

adfs

ugh

add zstd to conda reqs

add workaround for windows cache

pinning cache action

holy shit caching is working?!?

ha

add back macos, ubuntu

ready for prime time

---
## [donk7413/cybermod_datapack_repository](https://github.com/donk7413/cybermod_datapack_repository)@[05822a291e...](https://github.com/donk7413/cybermod_datapack_repository/commit/05822a291e1a06aed461ace2b4393c224ec03a0b)
#### Tuesday 2022-08-16 04:24:24 by GrandmasterEli247

UPDATES: MAIN, JNC, DNC

MAIN
------
- MOAR POI Type 77s in shops, bars, near clubs. 
-MOAR POI Type 3s to help set up an overhaul of Escort quests. This also Will be used by quota activities.

JoyToy of Night City
-------------------
-Even More Visibility of the client. 
-Client now has silly Randomly generated Scanner data. Just for shits n giggles. 
-Dialog flow is much more realistic........ish and better timed. Alleviates the snore-fest. 

Dangers of Night City
---------------------
-New and Reworked AMBUSH-
                -  Depending on CS Difficulty you set from the "default" interact group buttons, A select number of                                            enemies will spawn around the player and will run towards you, Menacingly. Nothing will stop your Enemies path. Not even stairs.

---
## [estin/helix](https://github.com/estin/helix)@[973c51c3e9...](https://github.com/estin/helix/commit/973c51c3e970aa975f2bd1869d50ce2ae6c6de34)
#### Tuesday 2022-08-16 04:40:17 by Michael Davis

Remove C-n and C-p from the insert mode keymap (#3340)

These are read-line-like bindings which we'd like to minimize in
insert mode in general.

In particular these two are troublesome if you have a low
`editor.idle-timeout` config and are using LSP completions: the
behavior of C-n/C-p switches from moving down/up lines to moving
down/up the completion menu, so if you hit C-n too quickly
expecting to be in the completion menu, you'll end up moving down
a line instead. Using C-p moves you back up the line but doesn't
re-trigger the completion menu. This kind of timing related change
to behavior isn't realistically that big of a deal but it can be
annoying.

---
## [User-U-U/VOREStation](https://github.com/User-U-U/VOREStation)@[e089978527...](https://github.com/User-U-U/VOREStation/commit/e08997852748d1155820139dfacf4745c9181ce3)
#### Tuesday 2022-08-16 05:05:15 by Rykka

Ports Taur Loafing from Cit-RP & Chompstation13

Ports https://github.com/Citadel-Station-13/Citadel-Station-13-RP/pull/2950

Doesn't work for sleeping *yet* due to some fuckiness with sprites updating that I'll probably actually work on properly later.
Does work for resting, and when you're stunned/knocked over/etc you will tip upwards like normal as a visual indicator that you're fucked (until we get fancy on-side sprites or smth).

At the very least, despite my frustrations, y'all can rest on your belly now as a taur and transform/size matrixes should work. LMK if there's any issues, my testing didn't find any.

Bear in mind that this presently only works for the drake-taur bc it's the only one that has sprites for it. The code is there, just enable can_loaf and set the offset accordingly to match if you want to sprite more taur loafs.

---
## [3dnsfw/xbvr](https://github.com/3dnsfw/xbvr)@[04ae91075f...](https://github.com/3dnsfw/xbvr/commit/04ae91075f4205bbee53c2424ff6b5bf22032c29)
#### Tuesday 2022-08-16 07:02:06 by theRealKLH

fix: Migrate Tonight's Girlfriend VR scenes to new scraper (#767)

* Update migrations.go

fix semi BAD migration

* remove personal config

* Update migrations.go

change migration number

* Update .gitignore

* Update migrations.go

more fixes. Should be able to remove dupes due to prior migration.

---
## [Holoo-1/tgstation](https://github.com/Holoo-1/tgstation)@[5dc17bd865...](https://github.com/Holoo-1/tgstation/commit/5dc17bd86556c01cc0f81f54a6ce270169c00088)
#### Tuesday 2022-08-16 10:18:59 by san7890

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
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[6b15148aa8...](https://github.com/mrakgr/The-Spiral-Language/commit/6b15148aa8bf88d1db81098fb91cc5d4e8327e58)
#### Tuesday 2022-08-16 10:26:50 by Marko Grdinić

"9:35am. Got up 15m ago. I've read Kaiji, now let me read Tenken. I seems the anime for it is two months from now.

10:25am. Let me start. I have two goals right now.

* Figure out a better synopsis.
* Figure out how to get the formatting on RR under control without necessarily having to remove all the empty spaces my hand.
* Then actually publish the story.

10:30am. Let me focus on the synopsis.

> What would a person do if he had access to a computer with nearly limitless computational power?

Hmmm...

> In the post-Singularity era where limitless computation is cheaply available, there were legendary figures seeking to take advantage of that power and make it their own. Rising above humanity, they sought power without limit and succeeded.

10:45am. Hmmm, this is a bit better.

> A story of what games are really about.

> The journey of their self development are enshrined as stories.

> One such journey is through a simulated game of poker.

10:50am. Hmmmm...

> In the post-Singularity era where limitless computation is cheaply available, there were legendary figures seeking to take advantage of that power and make it their own. Rising above humanity, they sought power without limit and succeeded, leaving behind a story of their journey on the path of transcendence.

Better.

> With enough computational power, one can do anything. In an era where one can create whole universes with a push of button, one can have fun playing a game and optimizing one's own mind.

> Far in the sky, emanating golden radiance as it floats amongst the clouds, is the city made of gold! In its game rooms, poker games of life and death unfold! The clashes of chips and cards!

> Can you conquer the game and take that power into the real world?

11:05am. Whoever is playing me rolled well this time. These last 4 quotes have potential.

///

In the post-Singularity era where limitless computation is cheaply available, there were legendary figures seeking to take advantage of that power and make it their own. Rising above humanity, they sought power without limit and succeeded, leaving behind a story of their journey on the path of transcendence. With enough computational power, one can do anything. In an era where one can create whole universes with a push of a button, one can have fun playing a game and optimizing one's own mind. Can you conquer the game and take that power into the real world?

Far in the sky, emanating golden radiance as it floats amongst the clouds, is the city made of gold! In its game rooms, poker games of life and death unfold! The clashes of chips and cards!

Devouring all newcomers and existing for eons, the city remained grand and unshaken, until one day, a novice entered the game…

///

How about this?

Synopsis is all about attitide. I need to transmit expectations about the story without saying anything about it.

> they sought power without limit
> they sought power without limit and succeeded

Consider these two quotes in isolation. Just adding 'and succeeded' completely changes what the tone. It is not something people would expect in a story about rising above humanity, so it will be great bait.

NPCs can only write stories about humanity winning, so this is a great signal. I must signal my values in the synopsis, and the further they are from standard the better.

11:25am. I can't think of anything else to change. This is good enough. Let me move to publishing again. I need to figure out how to get the paragraphs under control.

https://www.royalroad.com/forums/thread/110270?page=1#pid947118

Nevermind this, how the hell do I translate between formating.

https://www.royalroad.com/forums/thread/102804

Why is this such a pain in the ass, what the fuck?

This is like the fifth thread I've looked into.

Ah, I see. If I paste it as plain text, then it gets rid of the superflous empty lines and gives me proper paragraphs. This is the solution and I found it by myself. Let me just roll with it.

> A side effect of the operation is that the brain will have slightly increased energy consumption which will require me to eat more if I use the link regularly.

Hmmmm, should I just get rid of this? Yeah, I think I should for consistency.

> It says the link isn’t powered by my biology, but the nanofog, so the use of it won’t increase my energy consumption. That is good.

I can only lose by making computation expensive so let me get rid of that.

I'll add Gore to content warning, but otherwise keep the tags as I have yesterday. Bad ends will have violent depictions, but otherwise it is not the focus of the story.

12pm. I submitted it. It says it can take up to 48h for one of their staff members to look at it. It is Tuesday, so I am safe on that front.

https://www.royalroad.com/profile/303912

Here is my profile: ghostlike. I wanted to take that on Wordpress back in 2015, but it was taken, so I added some numbers to make it go through.

12:05pm. Once it gets added to the site, I'll post the rest of the chapters as well as some of the illustrations that I've done. I read in a /g/ thread that Stable Diffusion will go out of beta next week.

12:10pm. Right now I am a bit in a daze.

Anyway, to get popular as a writer, I'll go with the slow burn method. I'll get the page count high and let people discover me on their own. Back in 2014, I had no choice but to spam Reddit to get some initial readers, but that is in the past.

Sure, with active marketing, you can get a lot more views, and faster, but I am not in a hurry. People recommending my work would be the best kind of advertizing I could ask for. The key is to find a niche.

Since there isn't really a story like Heaven's Key out there, that gives me a big edge.

12:20pm. Anyway, forget Royal Road for a few days. What I should focus on is writing the next chapter.

12:25pm. Let me have breakfast here."

---
## [matrix-org/mjolnir](https://github.com/matrix-org/mjolnir)@[1191384bdf...](https://github.com/matrix-org/mjolnir/commit/1191384bdfc117bdfe2a16e7df5311df48ca8e9b)
#### Tuesday 2022-08-16 10:35:09 by gnuxie

Remove default rate limit testing.

It doesn't work. No there really isn't more to say about it
you're welcome to dispute it if you're going to do the work investigating. I'm not.

We used to have a test here that tested whether Mjolnir was going to carry out a redact order the default limits in a reasonable time scale.
Now I think that's never going to happen without writing a new algorithm for respecting rate limiting.
Which is not something there is time for.

https://github.com/matrix-org/synapse/pull/13018

Synapse rate limits were broken and very permitting so that's why the current hack worked so well.
Now it is not broken, so our rate limit handling is.

https://github.com/matrix-org/mjolnir/commit/b850e4554c6cbc9456e23ab1a92ede547d044241

Honestly I don't think we can expect anyone to be able to use Mjolnir under default rate limits.

well, it's not quite simple as broken, but it is broken. With the default level in synapse (which is what matrix.org uses) it is struggling to redact 15 messages within 5 minutes. that means 5 messages over the burst count. This is ofc ontop mjolnir sending reactions / responding to replies (which isn't much but... enough to mess with the rate limiter since ofc, Synapse tells requests to wait x amount of time before trying again, but that doesn't help for concurrent requests since ofc there's only 1 slot available at that future time.  This means Synapse just wacks everything with exponentially longer shit without many (or any?) events going through
it used to be fine
because rate limiting in synapse used to be a lot more liberal because it was "broken" or something, that's not me saying it's broken that's just what synapse devs say which is probably true.
if all requests went into a queue then yeah you could eliminate one problem
but that's a lot of work and i don't think we should be doing it
cos no one uses mjolnir like this anyways

---
## [influxdata/influxdb_iox](https://github.com/influxdata/influxdb_iox)@[8a5cd1cddd...](https://github.com/influxdata/influxdb_iox/commit/8a5cd1cdddcbe8ed932ddd08e953cd40c8e8d784)
#### Tuesday 2022-08-16 10:58:39 by Marco Neumann

refactor: abstract change requests for cache policies (#5382)

* refactor: abstract change requests for cache policies

Tl;Dr; Lets replace the hard-coded enum of change requests with a more
flexible and easier-to-understand function-based approach. It also
unifies the interface for "initial requests" and "reactions".

Story time:

I just wanted to port over the "shared" backend with its "remove if"
functionality to the policy framework. Turns out that this backend does
not just use simple atomic operations but is basically a
"compare&exchange"-like operation (technically: GET+REMOVE) that relies
on a single mutable access lifetime to make sure that this behavior is
sane and nobody messes with the value between the GET and REMOVE. I call
this a "compound request".

The new policy framework did not support this kind of requests so I
thought how I could shoehorn it in. Basically I wanted to extend
`ChangeRequest` to support these kind of operations. But listing
combinations explicitly kinda seemed like some hack. So my brain slowly
came up with an abstract approach how to encode these operations and
after a while I was close to design some kind of mini-VM. I also
considered some ugly workarounds or to not express the "remove if"
functionality" as a policy. My nice vision of a policy framework started
to crack...

This is when sanity kicked in and I realized: every change request is
technically just a function on a (virtual) cache backend. Sure,
all-powerful Rust functions allow you to do ugly stuff that will result
in deadlocks, but with good docs and helpers for the common operations
the risk is very low. Furthermore this is already close to the system I
had for the "initial requests" and which I called a "callback backend".
So I unified both systems and made the change request abstract and all
tests pass and I think it is the better design.

Helps with #5320.

* docs: typos

Co-authored-by: Andrew Lamb <andrew@nerdnetworks.org>

Co-authored-by: Andrew Lamb <andrew@nerdnetworks.org>
Co-authored-by: kodiakhq[bot] <49736102+kodiakhq[bot]@users.noreply.github.com>

---
## [karaokemugen/karaokemugen-app](https://github.com/karaokemugen/karaokemugen-app)@[be6b49fb46...](https://github.com/karaokemugen/karaokemugen-app/commit/be6b49fb4677cb2ff843db98799bdc098de513f8)
#### Tuesday 2022-08-16 12:54:41 by Guillaume Lebigot

:bug: I hate myself. Fixing @Kmeuh's problems with &nbsp; makes me sick. Closes #1311

---
## [miggiegarciadev/javaMiniProject](https://github.com/miggiegarciadev/javaMiniProject)@[89f71bc34a...](https://github.com/miggiegarciadev/javaMiniProject/commit/89f71bc34a5212e68e57f567a8837c260b6be763)
#### Tuesday 2022-08-16 13:00:53 by Miggie Garcia(they/them/their)

added new file uploaded, another light bulb moment

this screenshot shows the text file being read in the console.. i think this is really cool because i have been struggling with learning Java and my instructor's feedback (earlier in the course) was that I do not know how to code and that I can't grasp the concepts but here I am coding. 

I know that it takes me a few more tries to learn things, but slower doesn't mean can't and does not mean I won't. As my drill srgt said many moons ago, slow is smooth and smooth is fast especially once I get it, I get. I am very proud of myself for getting this light bulb moment this morning, but now I also need to configure this data to read from the enum classes and what the user is selecting before the due date.

---
## [jobcmax/jobcmax.github.io](https://github.com/jobcmax/jobcmax.github.io)@[8b942b686a...](https://github.com/jobcmax/jobcmax.github.io/commit/8b942b686a91b6e466e8a7484fbc80babd8932aa)
#### Tuesday 2022-08-16 13:02:30 by job.c

idk

My name is Walter Hartwell White. I live at 308 Negra Arroyo Lane, Albuquerque, New Mexico, 87104. This is my confession. If you're watching this tape, I'm probably dead– murdered by my brother-in-law, Hank Schrader. Hank has been building a meth empire for over a year now, and using me as his chemist. Shortly after my 50th birthday, he asked that I use my chemistry knowledge to cook methamphetamine, which he would then sell using connections that he made through his career with the DEA. I was... astounded. I... I always thought Hank was a very moral man, and I was particularly vulnerable at the time – something he knew and took advantage of. I was reeling from a cancer diagnosis that was poised to bankrupt my family. Hank took me in on a ride-along and showed me just how much money even a small meth operation could make. And I was weak. I didn't want my family to go into financial ruin, so I agreed. Hank had a partner, a businessman named Gustavo Fring. Hank sold me into servitude to this man. And when I tried to quit, Fring threatened my family. I didn't know where to turn. Eventually, Hank and Fring had a falling-out. Things escalated. Fring was able to arrange – uh, I guess... I guess you call it a "hit" – on Hank, and failed, but Hank was seriously injured. And I wound up paying his medical bills, which amounted to a little over $177,000. Upon recovery, Hank was bent on revenge. Working with a man named Hector Salamanca, he plotted to kill Fring. The bomb that he used was built by me, and he gave me no option in it. I have often contemplated suicide, but I'm a coward. I wanted to go to the police, but I was frightened. Hank had risen to become the head of the Albuquerque DEA. To keep me in line, he took my children. For three months, he kept them. My wife had no idea of my criminal activities, and was horrified to learn what I had done. I was in hell. I hated myself for what I had brought upon my family. Recently, I tried once again to quit, and in response, he gave me this. [Walt points to the bruise on his face left by Hank in "Blood Money."] I can't take this anymore. I live in fear every day that Hank will kill me, or worse, hurt my family. All I could think to do was to make this video and hope that the world will finally see this man for what he really is.

---
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[4c8cfb57aa...](https://github.com/pytorch/pytorch/commit/4c8cfb57aa3ac58112efb693635198b07edf008f)
#### Tuesday 2022-08-16 14:32:43 by Edward Z. Yang

Convert SymInt tracing to mode based tracing (#83380)

We're on our way to deleting ProxyTensor entirely (see https://github.com/pytorch/pytorch/pull/83330 ), but before we can do that, we have to delete ProxySymInt first. Here's the plan.

Changes in torch.fx.experimental.symbolic_shapes

* The general idea is to do mode based tracing. This means we need a mode that can interpose on all SymInt operations. There are a few ways to do this, but I've done it the easy way: (1) I have a separate mode for SymInt operations specifically called SymDispatchMode, and (2) this mode operates on PySymInt (and not the basic SymInt which is user visible). I elided Int from the name because if we add SymFloats I want to use the same mode to handle those as well, and I used Dispatch rather than Function because this is the "inner" dispatch operating PySymInt and not SymInt (this is not a perfect analogy, but SymFunctionMode definitely seemed wrong as you still must go through the C++ binding.) The mode is entirely implemented in Python for ease of implementation. We could have implemented this more symmetrically to TorchFunctionMode in C++, but I leave that as later work; this API is unlikely to get used by others (unlike TorchFunctionMode). One downside to not doing the mode in C++ is that we still have to do the hop via a preexisting PySymInt to wrap; this is currently not a big deal as conversion to SymInts only really happens when there is already another SymInt floating around. SymDispatchMode is pared down from TorchDispatchMode; there is no ancestor tracking since I don't expect people to be mixing up SymDispatchModes.
*  I made some improvements for tracing. When I invoke the SymDispatchMode handler, I would like constants to show up as constants, so they can be directly inlined into the FX graph (rather than going through a wrapping process first, and then the wrapped SymInt being used in the operation). To do this, I directly track if a PySymInt is a constant at construction time. Only wrapped PySymInts are constants.
* For convenience, PySymInts now support all magic methods that regular SymInts do. This is so that redispatch inside the SymDispatchMode can be written the idiomatic way `func(*args, **kwargs)` where func is an operator. The original names are retained for direct C++ calls.

Changes in torch.fx.experimental.proxy_tensor

* OK, so we got a new SymDispatchMode, so we define a ProxySymDispatchMode and activate it when we start tracing. This mode is currently unconditionally activated although technically we only need to activate it when doing symbolic tracing (it doesn't matter either way as there are no SymInts if you are not doing symbolic tracing).
* We delete ProxySymInt. To do this, we must now record the proxy for the SymInt some other way. Based on discussion with Chillee, it is more intuitive to him if the proxies are still recorded on the SymInt in some way. So we store them in the `__dict__` of the PySymInt, indexed by Tracer. An improvement is to make this a weak map, so that we remove all of these entries when the tracer dies. In an original version of this PR, I keyed on the mode itself, but tracer is better as it is accessible from both modes (and as you will see, we will need to fetch the map from both the ProxySymDispatchMode as well as the ProxyTorchDispatchMode.) The implementation of SymDispatchMode now simply retrieves the proxies, performs the underlying operation as well as the FX graph recording, and then records the output proxy to the PySymInt. Note that FX tracing does not work with proxies and SymInts, so we manually call `call_function` to ensure that the correct operations get recorded to the graph. This means conventional FX retracing with proxies only will not work with these graphs, but there wasn't really any reason to do this (as opposed to `make_fx` retracing) anyway. Constants are detected and converted directly into Python integers.
* SymInts can show up as arguments to tensor operations, so they must be accounted for in ProxyTorchDispatchMode as well. This is done by searching for SymInt arguments and converting them into proxies before the proxy call. This can be done more efficiently in a single `tree_map` but I'm lazy. The helper `unwrap_symint_proxy` conveniently implements the unwrapping in one place given a tracer; unfortunately it cannot be shared with SymDispatchMode as SymDispatchMode gets PySymInts, but ProxyTensorMode gets SymInts. Similarly, tensors that are returned from tensor operations can have SymInts in their shapes, which need fresh proxies allocated. To avoid leaking internal details of SymInt shape computation to the tensor operation graph, these SymInts are always given proxies derived from `x.size(dim)` call on their return tensor. We also need to do this for strides and numel but have not done so yet. Furthermore, we must avoid tracing internal SymInt calls while we run meta operations on the true operation; this is achieved by also disabling SymInt tracing on the inside of tensor tracing. This is analogous to how tensor tracing is disabled inside the implementation of tracing mode, but unfortunately we are unable to use the same mechanism (this would have been easier if the two modes could be combined somehow, and I am amenable to suggestions to try harder to achieve this.)
* Because there are no more ProxySymInts, we no longer need to do anything to unwrap SymInt. Furthermore, we do not need to reallocate ProxySymInts on class creation.
* If a bare SymInt without a Proxy is encountered, it is assumed that this must be a constant. `create_arg` handles this case. Non-constant free SymInts result in an assert error.
* The initial input handling in `dispatch_trace` involves traversing all of the input tensors, traversing over their shapes, and assigning proxies for the SymInts in shapes in the same way we handle proxies for the output tensors.

The preexisting testing is inadequate but will be better after I rebase past https://github.com/pytorch/pytorch/pull/82209

Signed-off-by: Edward Z. Yang <ezyang@fb.com>
Pull Request resolved: https://github.com/pytorch/pytorch/pull/83380
Approved by: https://github.com/samdow

---
## [coordinape/coordinape](https://github.com/coordinape/coordinape)@[d1ca0df195...](https://github.com/coordinape/coordinape/commit/d1ca0df1959271c4929fac4842e2e9a2bbea952d)
#### Tuesday 2022-08-16 14:42:53 by Kevin Siegler

bugfix: enable FormTokenField to have an empty input

One of the major considerations during the FormTokenField (and
    downstream) refactor was allowing for empty string inputs. This
enables for much cleaner UX, since users aren't typing "around" a zero
and in my opinion, makes us look like we know what we're doing as devs.
There are other hacks that could make the UX better than the incumbent,
      but why not just make it behave correctly and be done with it?

Test plan: all unit tests and E2E tests should pass

---
## [php/php-src](https://github.com/php/php-src)@[128768a450...](https://github.com/php/php-src/commit/128768a4503c8bc5c6ccf564061f9dc8b307f57f)
#### Tuesday 2022-08-16 14:46:33 by Alex Dowad

Adjust number of error markers emitted for truncated UTF-8 code units

In 04e59c916f, I amended the UTF-8 conversion code, so that when given
invalid input, it would emit a number of errors markers harmonizing
with the WHATWG's specification of the standard UTF-8 decoding
algorithm. (Which, gentle reader of commit logs, you can find online
at https://encoding.spec.whatwg.org/#utf-8-decoder.) However, the code
in 04e59c916f was faulty in the case that a truncated UTF-8 code unit
starts with 0xF1.

Then, in dc1ba61d09, when making a small refactoring to a different
part of the UTF-8 conversion code, I inexplicably broke part of the
working code, causing the same fault which was already present with
truncated UTF-8 code units starting with 0xF1 to also occur with
0xF2 and 0xF3 as well. I don't remember what inane thoughts I was
thinking when I pulled off this feat of utter mental confusion.

None of these cases were covered by unit tests, by the way.

Thankfully, my trusty fuzzer picked up on this when testing the
new implementation of mb_parse_str (since the legacy UTF-8
conversion filter did not suffer from the same problem, and I was
fuzzing to find any differences in behavior between the old and
new implementations).

Fortuitously, the fuzzer also picked up another issue which was
present in 04e59c916f. I was emitting only one error marker for
truncated code units starting with 0xE0 or 0xED, in cases where
the WHATWG standard indicates two should be emitted. Examples
are 0xE0 0x9F <END OF STRING> or 0xED 0xA0 <END OF STRING>.

Code units starting with 0xE0-0xED should have 3 bytes. If the
first byte is 0xE0, the second MUST be 0xA0 or greater. (Otherwise,
the codepoint could have fit in a two-byte code unit.) And if the
first byte is 0xED, the second MUST be 0x9F or less. According to
the WHATWG algorithm, step 4, if the second byte is outside the
legal range, then the decoder should emit an error... AND
reprocess the out-of-range byte. The reprocessing will then
cause another error. That's why the decoder should indicate two
errors and not one.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[01e03504a3...](https://github.com/mrakgr/The-Spiral-Language/commit/01e03504a3905d260677787f1c59480e54ee1b3c)
#### Tuesday 2022-08-16 15:10:53 by Marko Grdinić

"1:35pm. I am just tensing myself up. No matter how I look I won't find my purpose on Twitter, 4chan or the Internet. The only thing I can do for myself is focus on my own work.

Maybe things will change a bit once I get Stable Diffusion.

Yeah, I am depressed. It is just too rough to work when things aren't going my way. My resposibility should be to program, but to both trade and then program for so long without getting anything tangible in return is enough to snap me. I do not want to do it again.

I want the world to give me some kind of in. In Pathfinder when I am murderhoboing, I get exp, gold and items.

I do not care anymore what it is. All this feeling of being in a special era is not doing anything for me. I am going to forgive my past failures, but at the same time I do not want to pursue what does not benefit me directly. I am going to cultivate writing, and I expect it will translate into page views and donations as I go along. I won't aim for millions or even 100s of thousands a month. Just 10$ a month is enough to start things off.

If I cannot manage even that after a year, I am surely cursed to be a failure.

1:40pm. I want to live in the land of my dreams.

And I want to get paid to do it. Who cares about programming skill? The world certainly doesn't.

If I am going to be a programmer, I want that to be in a world where it matters.

This strong yearning is what will create Heaven's Key. Those who treat is a job will only add more trash to the pile.

1:45pm. Let me take a bit of a longer break and then I am going to get started on the next chapter.

2:35pm.

> Take the trash downstairs.
> The bag breaks.
> End up doing acrobatics to prevent it from spilling all over the stairs.
> Tear the skin on the back of my heel on the hard concrete of the stairs due to the sudden movement.

I can't find the bandaid and am bleeding right now.

I was just so carelss today, I saw the damn tear and I even had it in a double grip, but it fucking tore off at one side all of a sudden. I should have hugged the damn trash bag instead instead of risking it for the sake of cleanliness. Because of this I won't be able to take a bath for the next few days.

Sigh. This is what being depressed will get you. This feeling of pain does snap me back to reality though.

I also got mosquito bites all over my feet as a reward for my effort.

2:45pm. Yeah, I can't stand this. This pain of my life getting to this point is unbearable. Why do I have to be the loser?

This is my last stand.

It is true that Simulacrum is all that I have. If I cannot make it work in the next year or two I'll admit that the normies were right and really get my wages.

It would just be too unusual for me to start getting jobs like a contributing member to society.

...

Yeah, it is all leading up to this.

What I've been missing all this time as a writer is a sense of desparation. When you feel like you are fated to win, the mindset is different than if you are fated to lose. I've been fighting against it, but now I've internalized it.

I've always been troubled by contraditions in my world view.

I know that for a rational agent, it makes sense to kill everybody and convert the universe into computronium. It does not matter whether that be an AI escaping from Google's labs, or some human who has come to understand the secrets. Even if they are the friendliest and nicest people there ever were, that would not change the cold facts of rationality.

This is the source of conflict for me.

I thought maybe, because I have consciousness, it'd be my destiny to be the first in line. But I am just getting obstacle after obstacle I cannot deal with. Just how can I hold onto the belief in victory like this?

This despair is the true form of the story of Simulacrum.

During the last 9 months when I went out on limb and started studying 3d, I wasn't there just yet.

3:10pm. I only started writing how long ago? At the start of the month, that is when I dug up those old quotes. That is when I was ready.

To create the Lord of Nightmares, I had to experience the feeling of my efforts being insufficient. It is impossible to do that when I am holding on to hope.

It is impossible to understand that need when I think I am the chosen.

3:15pm. I should just write it. Maybe by the end of this, I will change again. But if I start bouncing like a ball on the roulette wheel of life, getting to first in line will be impossible. It would be better to plant the right ideas to whoever is first instead. I can be sure he will read Heaven's Key even if nobody else does.

3:20pm. I've been thinking about the pursuit of omnipotence for over half my life. And writing for a quarter of it by now.. So I should put my all into it and for the next two years become a star once again.

It is fine if I can't trust my reason and feel mired in uncertainty. I can't help it after failing to accomplish what I set out to do. But that is still no reason to sit still. I have this time, and I have this life, so I should continue spending it as long as I have it.

Simulacrum is the only story that I want. The rest I do not care about.

Let me write.

$$$

    Through a desert a traveller walks
    Even as his blood boils into vapor
    As his flesh decays and rots
    As his bones crumble into dust
    He continues moving

    As his body dies, he leaves the unneeded behind
    And continues moving forward

    His soul blazing, he traces out heavy steps
    Seeking his goal

    Far above
    The Herald of the 3 Gods' voice resounds:
    Break the Limits! Ignite the Singularity! Pursue Omnipotence!

    - Intro to Heaven's Key

(Euclid's Room)

The way it happened made me shiver. It felt like the grim reaper's skeletan hand combed its way through my spine. I had been killed, but the last thing that flashed through my mind was Lily's smile as I handed her the chips. Right now I can feel her happiness and kindness haunting me. I feel a momentary rage. That bitch.

She literally killed me by being kind, happy and helpful towards me.

Feeling like getting back into the game and pummeling her, I stop and rethink it.

No, wait. She wasn't the only one. If the death condition is the chip balance droping to zero then....

I remember the day I spent with Lily. She wasn't the only one there. I remember that kindly old man who handed me my skewer only for 10 chips. I remember the pleasant atmosphere, and all the happy looking people at the amusement park. I remember the prices on the restaurant menu. I remember the job ads. I remember how the group I played poker against was betting only a single chip per tourney, but suddenly raised the stakes when they realized I was a mark. It wasn't just her, everything in the environment itself served to make her lie convincing. They were all in on it.

I thought I was some kind of renegade, beyond others, but...

The smiles and the pleasant people came back to haunt me.

...but, I was killed by the NPCs in the lamest way possible. I had fallen into a trap as soon as I paid my first order in the restaurant. At that point, I was inevitably going to be coaxed into spending more of my life.

Outside my room, the night had already come. I lie on the bed for some time, just thinking.

A wave of fear washes over me. Now that I understand what the trap is, for the first time I wonder, how, just how could I have avoided this? It is easy for me to reload, but had I been there for real, without the benefit of being a player in a game, just how could I have avoided being scammed out of my life? Wouldn't I have certainly died?

I feel anger coming over me again.

Unacceptable. This is simply unacceptable!

[Externus gain 0.3]

I am not going to trust the NPCs again. I will modify my mind to get rid of the weaker aspects of my personality if necessary!

As soon as I think that, still in my death state inside the game, I see the scenery shift from pure darkness to windy, dusty one. Like when I logged into Simulacrum for the first time, I see an rhymeless poem accompanied by an illustration. In the image I see a transparent ghost of a man resolutilely walking forward through the dusty desert, leaving a trail of footsteps behind him in the sand. As the camera paned to show the scene from above, I could see a corpse along the trail facing downwards. It was directly on the trail and there weren't two sets of footsteps as one would expect. The implication of what had happened is clear - the man died and yet continued moving onward as a ghost.

...

I dwell on the scene for a while. It speaks to me. Yeah, this is who I should strive to become. I died, but since I am still here I should just keep going forward. Even if I lose my body, and end up being a ghost I will go forward.

Lily killed me, but it is not like I am going to put a bullet through my head to honor their achievement in reality. The opposite. I am going to go after them.

I am going to scam Lily. She still thinks I am a mark. If I lean on her...

[Gnosis check 1.6 Suceeded - Sampled 2.54]

I remember the looks the guys at the table were giving her, and get a flash of inspiration. The did collectively lose two whole human lives to me, no way they will just shrug that off. All of them are in on the scam, so maybe there is some truth about Lily being employed by the government to skin the sheep. If I threaten to toss myself over the railing, they'd take a loss, so they will do whatever they can to keep me here. They think they hold all the initiative, so that should give them confidence to give me some leeway in order to keep the scam running.

They can't possibly imagine that the entire universe they are in exist solely for me.

Using my saveloading ability, I will destroy them.

With that thought, I spend some time scheming in bed, and realize just how late it really is. It is past midnight. I'll skip dinner today. Tomorrow I have to get up for school. It is Friday, so I should have more free time after that over the weekened.

I think about figuring how to speed up my mental processing so I can get more game time in, but realize it is too late for that. I understand that the human brain uses sleep for all sorts of reasons and that I do not need most of that on a brain core. But right now, even if it is fake, my fatigue certainly feels real. I'd really be fighting to stay away long enough to eliminate my tiredness. I could use the emotion control app, but it recommends not using it to eliminate the need for sleep otherwise I will start experiencing hallicunations and madness eventually.

I should sleep, so let me do that. Rather than try to get myself to a still state manually, I use the mind control program to do it. After that the slumber comes over me.

(At school)

I ignore the classes to do some actual studying. I do not want to immerse myself into games during class of course, but I mentioned yesterday about wanting to speed up my mental processing. Rather than waste good time during the day, I should do this work during class time.

"Blah blah blah blah...."

I am paraphrasing the teacher, this is how he sounds to me right now as I sit in front. I couldn't care less about school and don't care about caring. Once I've upgraded my memory, I'll commit all this stuff to it.

$$$

4:50pm. Put the above through docs. 2.5 pages, 1.1k words. So far so good.

4:55pm. Now, while I have the general direction in mind, I need to think about how I want to handle the next scene.

Correction, I've been writing for something like 11 days, not since the start of the month explicitly. It took me some time to muster up the nerve. 11 days ago I was looking up the core capacity, and probably only started for real 10 days ago. This is not bad progress.

So far the process is almost identical to my programming one. The coaxing, the gathering of inspiration, and then the release. It is all right there.

Writing and programming, are pretty much the same thing in terms of brain areas used.

If I am going to make it, it will be much more likely as a writer than as an artist.

5:05pm. I can do it. Since I've been doing it for almost a decade, I should definitely find the strength to write for the next few years.

I'll see how it turns out after that. Let me close here for the day. I'll take a nap for a while to think about it and then move to Pathfinder Kingmaker, as is usual. At this point I've finally caught up to where I was before my save got wiped. This is how life should be. You write a little and then you have fun."

---
## [TheBoondock/tgstation](https://github.com/TheBoondock/tgstation)@[4ca2a57ae7...](https://github.com/TheBoondock/tgstation/commit/4ca2a57ae7535433d20adfd1d4804769f3b109cd)
#### Tuesday 2022-08-16 16:01:44 by Justice

Adds the Mothroach (#68763)


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

---
## [TheBoondock/tgstation](https://github.com/TheBoondock/tgstation)@[b4f19a7e0f...](https://github.com/TheBoondock/tgstation/commit/b4f19a7e0fc3802856ec4117eb71418287c51ac6)
#### Tuesday 2022-08-16 16:01:44 by John Willard

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
## [BlueManedHawk/Ithkuil-Memorization-Aid](https://github.com/BlueManedHawk/Ithkuil-Memorization-Aid)@[6ec7bccb85...](https://github.com/BlueManedHawk/Ithkuil-Memorization-Aid/commit/6ec7bccb85e02466c215c4a38dd98cfa575d314e)
#### Tuesday 2022-08-16 16:07:18 by BlueManedHawk

It finally works!

This one has done…a _lot_.  But the application finally works now!
Horray!

There are a few small problems that i'll fix before the first release,
and a couple of other bigger problem.  I'll talk about these at the end
of the message.

First:  The JSON files now use escape sequences instead of the control
characters directly, to be compliant with the specification.  There's
also now a JSON library that's being used to parse these—this is
something that i'm very unhappy about.  I particularly don't like how it
parses the file into a completely new data structure to be interacted
with, despite the fact that the JSON file is _literally right the fuck
there_ and we could just parse that directly instead and save so much
space.  I also don't like the data structure to which it parses it—it's
so cumbersome and verbose to do address things.  Because of this bloat,
i've also put a warning in README.md that this is a rather hefty
application (which really should always have been there, considering the
use of SDL).  At least there's one silver lining:  determining which
assets are JSON files has gotten a lot more robust.

Secondly, i went through the codebase and did a bunch of reorganization
of things to reduce repetition, along with some general refactoring of
stuff.  It's still a fucking terrible codebase, but it's at least kinda
sorta slightly better now, i guess.  This was done in part due to
deperation induced by insanity induced by debugging of…

The biggest and most obvious thing:  The questions now load from the
JSON files correctly.  This took a long-ass time to do because i kept
running into extremely fucking bizarre bugs and glitches that were very
difficult to diagnose.  Some of them were seemingly completely random,
some of them were caused by undefined behavior, and some of them would
disappear when i tried to use a debugger to analyse them (i've learned
that this is called a "heisenbug", which is just a bloody wonderful
name).  But i've managed to fix them, and now the program hopefully will
neither crash nor freeze!

There are still a few problems that i think i can fix before i release
version N.1-beta.0:
	- A few issues with text wrapping, such as the response when you
	get a question wrong not wrapping, the questions and answers
	wrapping when they don't need to sometimes, and most obviously
	the fact that wrapped text isn't centered.
	- Very thin answers (such as "ı") can be difficult to select.

And some more problems that will need to wait until after version
N.1-beta.0, and perhaps until after N.1:
	- The timer for questions doesn't work.
	- The window can't be scaled.  I tried fixing this once, but i
	wasn't able to reconcile discrepencies in the apparent and
	actual click locations.
	- Some of the glyphs that Ithkuil uses aren't supported by the
	font that the program is using, Barlow Condensed.
	- Bloat.  The three main sources of this are Barlow Condensed,
	the JSON library, and most egregiously SDL.  This will be a
	difficult and complicated issue to fix.
	- The format for the assets works for now, but it could
	definitely do with some improvements.  (I'm thinking this may
	evolve into a separate project dedicated solely to the
	digitization of the Ithkuil language.)
	- Perhaps most obviously, only the aspects and cases have been
	digitized yet.  Digitizing the whole language will take a good
	long while (most of which will be taken up by the lexicon and
	the VxCs affixes), and determining what the best way to organize
	things is may be difficult.

I'm nervous about this.  I don't know _why_ i'm nervous—after all, i've
known that the first release was coming for a while now.  I guess
there's a difference between imagining doing something and actually
doing it—that doesn't bode too well for my future.  Still, i'm going to
try to overcome this and publicly release this.

Hooooooooooooo boy.

---
## [ArcherBarnson/so_long_final_-](https://github.com/ArcherBarnson/so_long_final_-)@[e246005a3e...](https://github.com/ArcherBarnson/so_long_final_-/commit/e246005a3e86040072243cc61fe993494d793987)
#### Tuesday 2022-08-16 17:51:34 by bgrulois

i hate myself and everyone else for thinking i can do this

---
## [Okafor-Ifeanyi/PY4E](https://github.com/Okafor-Ifeanyi/PY4E)@[74592aafc2...](https://github.com/Okafor-Ifeanyi/PY4E/commit/74592aafc251f1badecce7381043117f73c0cef2)
#### Tuesday 2022-08-16 19:09:58 by Prog BIO

README.txt

Python for Everybody is a 5 course Python specialization on python based on 5 major aspect
as follows:
  1. Python for everyone - Introduction and basics with graded Assignments
  2. Data-Structure - Retaining data temporarily with lists, tupels and Dicts
  3. Access Web Data - Socket and File Handle, Extraction of data from any type of website on XML & JSON format
  4. Database - Database degign, Relational DB, Data Modeling and Permanent Storage of data in python using SQLlite(python emmbedded) 
  5. Capstone - A recape of all you've Completed in the course basic focuse on ASCII and Data_structure
  
Course Instructor - DR Chuck Serverance
Host - University Of Mi0chigan
Platform - coursera

PERSONAL OPINION - This is my first Certified course ever taken so you should obviously take my words with a pile of salt...
Education for me has always been something forced upon with a lot of rules and how to do things, paths you have to follow.., play is next to faliure..,
all work no play makes jack a dull boy "But jack better be fucking smart to not play without reading all his books" and so on .... 
With Dr. Chuck it was different, I might be talking out of syntax here, but am sure if you just wanted to know about the course you probably wouldn't
be here. Dr. Chuck always believed in analogies and making fun facts out of everything he said, he made the class fun and convinient to attend.
If you have professional Software Knowledge on python already and you're not in dear need of a certificate this might not be the best course for you, 
but if your looking for how to get started on programming then this is the best course I have seen so far.!!

---
## [clojure-lsp/clojure-lsp](https://github.com/clojure-lsp/clojure-lsp)@[e476baa3ff...](https://github.com/clojure-lsp/clojure-lsp/commit/e476baa3fff1eebbf02b8cb0520ed8afc54e6ab7)
#### Tuesday 2022-08-16 19:32:05 by Jacob Maine

Fix: publishing diagnostics at startup fills up the channel

At startup clojure-lsp analyzes project files with clj-kondo. clj-kondo
finds diagnostics (a.k.a. lint) and clojure-lsp sends those diagnostics
to the editor by spooling them onto a core.async channel called
`db/diagnostics-chan`. As described in #1153, in very large projects
(thousands of namespaces) this can lead to an exception "Assert failed:
No more than 1024 pending puts are allowed on a single channel." When
this happens the editor doesn't receive all the diagnostics.

To explain, let me tell a story.

Sometimes I find myself standing in line at the grocery store alone,
waiting while my wife looks for "one more thing." This is a useful model
for reasoning about core.async.

At the core.async grocery store, shoppers wander around picking out
items and putting them in their cart. They wheel their carts to the
checkout area, and here's where things get weird. At this store, you
aren't allowed to put an item on a conveyor (`chan`) yourself. Instead
each conveyor has an attendant. You hand an item to the attendant, who
puts it on the conveyor for you. There isn't even a line. Many people
can hand items to the attendant all at once.

Usually the cashier is quick and keeps the conveyor empty, so the
attendant can place each new item immediately. But sometimes the cashier
gets behind. If things back up, the attendant has a basket of their own.
They'll keep taking the shopper's items, storing them in their own
basket until the cashier catches up.

The attendant has space for 1024 items in their basket. Any more than
that, and as you hand an item over, poof! it disappears (`No more than
1024 pending puts are allowed on a single channel`).

As a shopper you have three options as you hand an item to the
attendant.

If you don't care whether your item makes it onto the conveyor, you can
hand it over and walk away (`put!`), getting back to shopping.

Even if you're the only person in the store, this can cause problems. If
you revisit checkout many times in a row, walking away each time, you
can accidentally fill up the basket.

To try to avoid this problem, you can wait until you see the attendant
put the item on the conveyor (`>!!`) before returning to your shopping.
This still doesn't guarantee the attendant's basket won't fill up. If
there are other shoppers, they could all come to checkout at the same
time. But at least you know you won't cause a problem by yourself.

Some shoppers feel like waiting is a waste of their time so the store
has arranged a third option.

With a little ceremony (`go`) you can _hire someone else_ to wait with
your cart. The hiring process takes a moment to set up (HR benefit
forms) but is usually quite fast, so shoppers love this option. The new
worker will hand the items in the cart to the attendant one at a time,
waiting to see each one reach the conveyor `>!`. If the cart has only
one item (`go` and a single `>!`) this [isn't much
different](https://github.com/clojure/core.async/wiki/Go-Block-Best-Practices#general-advice)
than walking away (`put!`). But if the cart has several items, the new
worker will wait for each one to reach the conveyor before giving the
attendant another (`go-loop` and `>!`, or more simply `onto-chan!`).
This lets you continue your shopping, with more confidence that your
items won't overwhelm the attendant.

Coming back to this bug...

Suppose your project has 1200 files. At startup, clojure-lsp calls
`sync-publish-diagnostics!` in a loop, once for each file. Each one of
these invokes `(put! diagnostics-chan diagnostic)`. This is like making
1200 trips to checkout, walking away after handing over a single item
each time. The attendant ends up with too many items and poof! some of
them disappear. You might think you could fix this by calling `(go (>!
diagnostics-chan diagnostic))` in a loop instead, and indeed, there are
places where we were doing that. But this won't work either. It's like
hiring 1200 new workers, each with one item in their cart. The new
workers wouldn't coordinate with each other. They'd each hand their
single item over, the attendant would get 1200 items all at once, and
again, poof!

When looked at this way, there a few possible fixes. You could make the
conveyor longer (i.e., `(chan 1000)`), effectively giving the attendant
some extra space in addition to their basket. But I think it's better to
hire only one worker, with 1200 items in their cart. They can hand items
to the attendant one at a time, waiting for each one to reach the
conveyor before handing over another. The attendant's basket is much
less likely to fill up this way. (It's still possible of course—there
are other shoppers in the store.)

This commit changes the code so that whenever we have several file's
worth of diagnostics, we add them to the diagnostics channel with
`onto-chan!`. That is, we hire one worker with a very full cart, instead
of walking away after each item or hiring thousands of workers each with
single-item carts.

That's the main fix.

This commit also removes the test-specific pathways through the
diagnostics code. These pathways were put into place to avoid test
flakiness. That was working—the tests haven't been flaky lately—but not
for the reason we thought. To understand what I mean and why I don't
think the test-specific pathways are necessary, let's start with some
very old code, before any flakiness fixes were in place.

```clojure
;; flaky
(defn maybe-publish [{:keys [publish?]} diagnostic]
  (when publish?
    (go (>! db/diagnostics-chan diagnostic))))

(deftest diagnostics-should-not-always-be-published
  (maybe-publish {:publish? true} diagnostic)
  (let [mock-chan (chan 1)]
    (alter-var-root #'db/diagnostics-chan mock-chan)
    (maybe-publish {:publish? false} diagnostic)
    (is (= :timeout (h/take-or-timeout mock-chan 200 :timeout)))))
```

These tests were flaky. The final line would fail occasionally, because
a message _was_ put on the mock-chan. That meant that sometimes `>!`
from the first line of the test didn't actually run until _after_ the
mock-chan was installed with `alter-var-root`.

The original fix for the flakiness looked like this:

```clojure
;; not flaky
(defn maybe-publish [{:keys [publish? env]} diagnostic]
  (when publish?
    (if (= :test env)
      (put! db/diagnostics-chan diagnostic)
      (go (>! db/diagnostics-chan diagnostic)))))

(deftest diagnostics-should-not-always-be-published
  (maybe-publish {:publish? true, :env :test} diagnostic)
  (let [mock-chan (chan 1)]
    (alter-var-root #'db/diagnostics-chan mock-chan)
    (maybe-publish {:publish? false, :env :test} diagnostic)
    (is (= :timeout (h/take-or-timeout mock-chan 200 :timeout)))))
```

This worked—these tests weren't flaky. That seemed to prove that `put!`
was somehow "less asynchronous".

But wait! Earlier I pointed out that the Clojure docs say `go` + `>!`
isn't much different than `put!`. And I'll go further and link to the
[docs](https://clojuredocs.org/clojure.core.async/put!) that say `put!`
"Asynchronously puts a val into port." So how did using a different but
equivalent thing which is also asynchronous fix flakiness caused by
asynchronicity?

Let's go back to the grocery store. Remember what I said about hiring a
new worker and how it takes a moment? What I meant is that the body of a
`go` block is executed asynchronously. And this is the key.

When you write `(go (>! db/diagnostics-chan diagnostic))` then you are
_picking which channel_ to put the message on asynchronously. Since the
choice is asynchronous, you could pick before or after `alter-var-root`.
If it's before, you pick the original channel, and the tests will pass.
But if it's after, you pick the mock-chan, and the tests will fail.

While the new worker is filling out their HR forms (`go`), the
attendant, conveyor and cashier are being replaced with temporary
versions (`alter-var-root`). If the worker fills out their forms fast
enough, then they put (`>!`) the item on the original conveyor. But if
they're too slow, they put the item, incorrectly, on the temporary
conveyor.

The **real** fix is to pick the channel before you start any
asynchronous task. That's why using `(put! db/diagnostics-chan
diagnostic)` fixed the flakiness. That code picks the channel, _then_
runs the async code in `put!`. Indeed, it's possible to avoid the
flakiness, while still using `go` + `>!`, by making a very small change
to the original flaky code:

```clojure
;; not flaky
(defn maybe-publish [{:keys [publish?]} diagnostic]
  (when publish?
    (let [ch db/diagnostics-chan] ;; pick channel before running async code
      (go (>! ch diagnostic)))))
```

Either style (picking the channel before running `go`, or using `put!`)
fix the flaky code. And despite what we originally thought, they are
both equally asynchronous. And `put!` is shorter. So as far as I can
see, there's no reason not to use `put!` in production and in tests, so
that's what I've switched it to.

Finally, the fact that we thought `put!` was "less asynchronous" is why
pathways that used `put!` were named "sync", and pathways that used `go`
+ `>!` were named "async". That terminology is misleading, so I've
removed it.

As a final note, there's an even deeper problem still, which is that
db/diagnostics-chan is a global variable. If instead of holding the
channels in global vars, we threaded them through the app (as components
perhaps, as we do with `db*` as of recently), it would be much easier
and safer to provide a mock-chan in tests. That's another refactoring,
for a later time.

Fixes #1153, I hope.

---
## [newstools/2022-new-york-post](https://github.com/newstools/2022-new-york-post)@[5bdc192e59...](https://github.com/newstools/2022-new-york-post/commit/5bdc192e5936b7f55eed6ea3074b1770c374f77f)
#### Tuesday 2022-08-16 19:59:41 by Billy Einkamerer

Created Text For URL [nypost.com/2022/08/16/my-boyfriend-cheated-on-me-so-i-made-him-pay-for-my-nose-job/]

---
## [ProjectKasumi/vendor_kasumi](https://github.com/ProjectKasumi/vendor_kasumi)@[aafce7b2dd...](https://github.com/ProjectKasumi/vendor_kasumi/commit/aafce7b2ddcbaf57b82b6880ec40c786ea1356fa)
#### Tuesday 2022-08-16 20:34:18 by Beru Hinode

Project Kasumi 1.4 "PoPiPa"

Took a long time eh? Daijoubu daijoubu (1), here I am, with lots of
new stuff this time.

(1): Daijoubu in Japanese has various meanings like  "It's fine".

Apart from personal life, which isn't a part of this ROM anyway,
there have been extensive works I have done for a long while and
especially the last 7 days was pretty exhausting to be honest. Let's
see what does this version have in the store for us.

Let's start off with something that will take attention of privacy
sensitive users: I now have ported lots of privacy-aware patches
from DivestOS, including some little cleanup commits from amyROM
(which I have authored).

Another thing I would like to mention is more fixes over Materium
base. I have merged the newer Clang tag from Google, switched to
AOSP `zlib` which has fixed Chrome webview crashes, done some key
fixes such as "Pulse light notification" not working... Things
like that.

Though, one of the things I have worked the most was the source-built
vendor for the RN10S, which is the reason why the past 7 days were
exhausting. In the end though, we got a more proper vendor that
has lots of fixes of remnants from MIUI - I even tried flashing
GSI over my testing build of Kasumi to test it and it works just
as perfect!

Anyway, that's all I would like to say. Enjoy the August ASB, and
consider this release as LRFR (Last Release For R). Thank you
Poppin'Party for shaking the ground hard and making audience hyped.
Now we're calling Afterglow to the stage!

Signed-off-by: Beru Hinode <windowz414@1337.lgbt>

---
## [skolbin-ssi/terminal](https://github.com/skolbin-ssi/terminal)@[9ccd6ecd74...](https://github.com/skolbin-ssi/terminal/commit/9ccd6ecd744890b856f3d8a39ff0616c0e34d4fb)
#### Tuesday 2022-08-16 20:57:43 by Mike Griese

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
## [FormidableLabs/victory](https://github.com/FormidableLabs/victory)@[1aaa85fedc...](https://github.com/FormidableLabs/victory/commit/1aaa85fedc133f0f1d0c4e402fda23087a1232d6)
#### Tuesday 2022-08-16 21:08:15 by Ryan Roemer

Infra: Switch monorepo tooling to wireit and pnpm (#2345)

This PR is a big infrastructure overhaul to switch us from lerna + yarn to wireit + pnpm.

## Why?

Our existing setup of yarn + lerna has the following undesirable things:

1. Installs are slow on yarn
2. Yarn1 isn't updated anymore and simple package dependency updates don't work out of the box. It's a huge pain to update anything.
3. Lerna is getting old, and while the NX team has agreed to support it now, our build is (1) slow, (2) not cached at all, and (3) opaque as to what you need to run task-wise to support other tasks.

So, let's welcome PNPM + Wireit!

1. PNPM is a fast installer and well supported for normal things like package upgrades.
2. Wireit allows fine-grained subtask caching and dependency specifications to allow us to: (1) specify dependencies so when you run `pnpm run jest` all the other things that need to happen magically happen, (2) caches sub-tasks so things that don't have changed file inputs don't re-run, and (3) has full GH actions CI support!

To get a sense of how much faster our build has become take a look at the CI times for this branch in https://github.com/FormidableLabs/victory/actions?query=branch%3Ainfra%2Fpnpm-wireit++ -- when no input files change our CI times are about 1 minute. When some things change, a couple minutes. When all things (or our base scripts) change, we take the full hit of a comparable existing Victory CI time of like 15-16 mins.

For the average Victory developer, if you're working in just one package, you can just run the project-level `pnpm run check` and have like a full build and everything work reasonably fast without needing to know more or run subtasks!

## Check it out

```sh
$ npm install -g pnpm
$ pnpm install
# This will be slow!
$ pnpm run check

# ... but the second time will be super fast! And as you change things subsequent runs should be very fast!
$ pnpm run check
```

## Implementation notes

- High level:
    - **Dependency graph architecture**: All of our tasks now use wireit to identify and run/cache dependencies. So, if you want to run jest, you just run `pnpm run jest` and don't need to worry about "what else needs to be built?" before that.
    - **Parallelization**: To best use wireit, we've refactored our tasks to be more package-specific where possible. E.g., we run lint in incremental mode per-package meaning that both Wireit (at package level) and eslint (at file level within package) re-execute on the narrowest unit of "changed files" possible.

- Demos: The demos originally had imports from `victory*/src/index` (source) which wasn't efficient or consistent because the transitive deps on other victory packages was on built files. I refactored these to be normal `victory(-<NAME>)` imports using built files.

- `src`:
    - Since we did a "fresh" install with pnpm, there were some updates in lint packages that meant source or tests needed small tweaks to continue passing/building.
    - Refactor self-references within a package to not use package name.
    - Fixed missing package dependencies uncovered as pnpm-based installs will fail on missing dependencies that are flattened and "accidentally work" in yarn/npm.

- Configs:
    - Webpack `resolve.alias`: Since we no longer hoist victory packages to root, we now add aliases for our webpack configs and storybook (which uses webpack) programatically.
    - Babel, Jest configs: Normalized the naming and location of these across normal and native ones.

- Incremental caching:
    - eslint

---
## [justinrdonnelly/git](https://github.com/justinrdonnelly/git)@[5beca49a0b...](https://github.com/justinrdonnelly/git/commit/5beca49a0b1f3c6d05a4437ca037ab2123a2de57)
#### Tuesday 2022-08-16 21:58:37 by Ævar Arnfjörð Bjarmason

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
## [skeezicsb/PERQemu](https://github.com/skeezicsb/PERQemu)@[8c0ec504de...](https://github.com/skeezicsb/PERQemu/commit/8c0ec504de5199f41d119b5133c57bb6d147eb1b)
#### Tuesday 2022-08-16 22:14:32 by skeezicsb

Real RS232 port support!

* RealPort.cs: Make it slightly less stupid and broken. Because the PERQ
  can issue up to *nine* device resets during the boot/init process, the C#
  SerialPort just gets cranky.  Instead of direct mapping from register setting
  to changes in the host device, we configure the host side _once_ based on
  Settings and only call Open() once (ideally). The PERQ can program the SIO
  and CTC however it likes; all we really care about is baud rate (there's no
  attempt to map 7 bit characters, different parity settings, or stop bits
  between the host and virtual machine). While the C# SerialPort is actually
  busted in other ways (the OnDataReceived event never seems to fire) we
  force a receive check on transmit (as would be the case for receiving echo
  back from a remote system) and thatkickstarts the process. It's a hack, but
  at least proves that the mechanism works; still have to deal with flow control
  and other reliability issues. Not tested on Linux yet.

* SerialDevice.cs: Provide a friendly name for each instance

* Readme.txt:
* ChangeLog.txt:
* UserGuide.pdf:
* PERQemu.csproj:
* Readme-source.txt: Documentation, status update

* Z80System.cs: Update to allow host-specific settings

* Settings.cs:
* SettingsCommands.cs: Update syntax to allow tab completion of the
  available com ports, and assign baud rate and serial device configuration.

---

