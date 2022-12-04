## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-12-03](docs/good-messages/2022/2022-12-03.md)


1,885,251 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,885,251 were push events containing 2,580,987 commit messages that amount to 158,017,579 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 34 messages:


## [ArtemisStation/artemis-tg](https://github.com/ArtemisStation/artemis-tg)@[4fd404aa8f...](https://github.com/ArtemisStation/artemis-tg/commit/4fd404aa8f15480ad4c8585e65268a83c60b26e1)
#### Saturday 2022-12-03 00:54:22 by tralezab

Moves speaking verbs to tongues + subtypes, moves wing sprites to wing subtypes, bodypart damage examines to limbs, fixes sign language not working without a tongue (#71635)

## About The Pull Request

### Moves speaking verbs to tongues + subtypes
Moves species say mod onto tongues, creates any tongues that didn't
exist for the say mods they needed to hold.

### moves wing sprites to wing subtypes
Moves the logic of selecting a wing sprite onto subtypes of /functional
on the wing type. Now, angel wings bring the holy trait with them, it
isn't a special check on flight potions, and we can expand it. (EMPs
taking down robowings? Fires burning megamoth wings? Cool stuff)

### bodypart damage examines to limbs
Instead of checking what your species says, it tallies up your limbs and
provides the damage description that matches most of your limbs. So for
example, If you're mostly human with one augmented part, you take
bruises and cuts. If you're mostly robot augmented with one human part,
you get robot damage descriptions. Yay!

### fixes sign language working without a tongue
Having no tongue would garble your speech, and this had no interaction
with sign language, so you'd be speaking in broken gurgling with
perfectly working hands. Now, the sign language component prevents any
kind of garbling, since it brings its own garbling for full/missing arms


![image](https://user-images.githubusercontent.com/40974010/204932511-42c8e020-a2d7-4fc1-befc-7cd46a2f2932.png)

## Why It's Good For The Game

Moving things off of species inherent makes the game expose way more
interesting mechanics to play with. It sucks that you can't steal a
jellyperson's chirping, since they can get a normal tongue and they'll
go back to... chirping! LAME! THAT IS LAME!

Ditto goes for wings, and for limbs, well, having someone be entirely
augmented but get descriptions of bleeding because they didn't spawn as
an android is kinda lame.

<details>
  <summary>Spoiler warning</summary>
  

![image](https://user-images.githubusercontent.com/40974010/204922627-333de052-a02b-4786-8ff9-f6e739443f2c.png)
  
</details>



## Changelog
:cl:
refactor: Refactored wings, tongues, and some examine messages,
hopefully with minimal effect on actual changes. A few more species have
tongues, angel wings bring the holy trait with them, and wings have new
descriptions. should be the biggest parts of it
/:cl:

---
## [ArtemisStation/artemis-tg](https://github.com/ArtemisStation/artemis-tg)@[2425531eb2...](https://github.com/ArtemisStation/artemis-tg/commit/2425531eb2dab84fb27ed864e4c52470bfff6918)
#### Saturday 2022-12-03 00:54:22 by John Willard

Removes tablets (not PDAs) entirely. (#71507)

## About The Pull Request

**Comes with an UpdatePaths!**

Removes the tablet subtype, PDAs now replaces them entirely.

Nukie and Silicon tablets are now subtypes of the PDA instead, while
contractor ones were removed entirely as they didn't do anything and
were unused (though it wouldn't be hard to re-add).

Nukie PDAs are now the only type of PDA that uses modular_tablets.dmi,
which is just larger icons of modular_pda. Each application requires an
icon state in both of these, for 2 different sizes, which makes it
annoying to make new applications, especially if it can also run on
computers/laptops.

### Icons

Because Silicon tablets are now a subtype of PDA, they use PDA icons
instead of tablet ones. Luckily for us, they already exist in code.

![image](https://user-images.githubusercontent.com/53777086/203876575-56eb1593-774c-47c6-8e7d-491a7805f28c.png)

AI's don't use a tablet icon though, so they aren't affected.

## Why It's Good For The Game

There's very little difference between tablets and PDAs, PDAs overshadow
them in every single way, so at this point I don't see why we should
have both of these, and if you compare the two in usefulness and actual
in-game use by players, it's a no-brainer than the item all players get
roundstart and comes with a messenger should be the one we go with.

Also as said in the about section, when making an app you would need to
make icon states for the program running for all hardware it can run on,
which is Computer, Laptop, PDA, and Tablet.

Laptop is just a smaller computer icon
PDA is just a smaller tablet icon

However, you can't simply shrink the size of the icon, instead you have
to completely resprite the same app icon FOUR TIMES for it to not
bluescreen on all these different devices.

<details>
<summary>
Here's examples of it
</summary>
Computer (NOTE: *They share the same icon file as regular computers*)
<img
src="https://user-images.githubusercontent.com/53777086/203876801-486a8054-489a-4983-bdad-a2599b4dc379.png"/>
Laptop
<img
src="https://user-images.githubusercontent.com/53777086/203876333-58e5d135-f4c6-4a02-8948-1df771e294a4.png"/>
Tablet
<img
src="https://user-images.githubusercontent.com/53777086/203876352-816c7fb1-c681-40b9-99e0-052f49632c7f.png"/>
PDA
<img
src="https://user-images.githubusercontent.com/53777086/203876358-1cf7253d-3c6a-456a-8133-ebf7f0351637.png"/>
</details>

If we wish to help in simplifying this, we should remove tablet icons
entirely, which means 1 less icon to worry about. To do this, we'd need
to resprite nukie PDAs, however I am very much not a spriter and never
tried GAGS, so I'll leave it to someone else to do.

## Changelog

:cl:
del: Tablets are now removed, PDAs are now the base 'tablet'. Silicon
and nukie tablets are now PDAs.
/:cl:

---
## [DefiUniversity/MevBotUniswapArbitrage](https://github.com/DefiUniversity/MevBotUniswapArbitrage)@[a3b1a75697...](https://github.com/DefiUniversity/MevBotUniswapArbitrage/commit/a3b1a75697a15285963acc6518656ff389d990d3)
#### Saturday 2022-12-03 01:09:33 by DefiUniversity

Create README.md

Uniswap is a cryptocurrency exchange which uses a decentralized network protocol. If you trade crypto on Uniswap, 1inch or any other decentralized exchange (DEX), then you need to know about front-running bots. 
Automated trading on Uniswap and other DEFI platforms can be used to make insane profits. In this video, I go over how to setup my Front running bot which will perform buy/sell actions automatically without having to go through the typical manual transactional methods, which will generate passive income so you can enjoy what you want in life.

---
## [Offroaders123/Art-Gen](https://github.com/Offroaders123/Art-Gen)@[1c485fe083...](https://github.com/Offroaders123/Art-Gen/commit/1c485fe083475b406901f00b781824ac609d5b5d)
#### Saturday 2022-12-03 01:46:36 by Offroaders123

FFmpeg WASM (Experimental)

Additions:
- Added experimental support for FFmpeg WASM! This is a very hacky workaround to get set up, at the moment.

A few notes about how it works so far:
- FFmpeg WASM requires the use of `SharedArrayBuffer`, so I had to ensure that `window.crossOriginIsolated` resorts to true. To do that, your site has to be in a secure context, and all of it's assets have to be served with the `Cross-Origin-Opener-Policy` header set to `same-origin` (protects your origin from attackers), and the `Cross-Origin-Embedder-Policy` set to `require-corp` (protects victims from your origin). This is because of the 2018 Spectre vulnerability, and it is a new secure approach to start re-enabling shared memory, with security first in mind.
https://stackoverflow.com/questions/68616601/how-to-define-sharedarraybuffer-in-chrome
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SharedArrayBuffer

Because this is a server header required change, this means you have to have access to change the headers of your resources sent to your page. This isn't available to modify for GitHub Pages, and it's still a bit out of my technical reach know how (at the moment :) ), so I looked more into it, and turns out that you can get around this by adding a Service Worker to your page, and it will allow you to change the headers for your fetched resources, and add the additional headers where needed. I got to try setting up a TS-safe Service Worker again with this too (bonus!), and it works *fairly* nice! Not quite just right yet, in terms of type-safety and a dev setup, but it does work as intended for what it's supposed to do! These pages really helped out with adding the headers to the files, and it did make it so I can get `SharedArrayBuffer` using `live-server` on `localhost`! I haven't debugged it yet, but the `live-server`-hosted site wasn't able to run, for some reason, on Safari (iOS/iPadOS). So, not sure where the error is for that yet. It works locally on the same machine, in Chrome though!
https://stackoverflow.com/questions/72603171/sharedarraybuffer-github-pages-and-dns
https://github.com/gzuidhof/coi-serviceworker/blob/master/coi-serviceworker.js
https://github.com/ffmpegwasm/ffmpeg.wasm/blob/master/examples/browser/transcode.worker.js

FFmpeg runs relatively quick in the terminal on my Mac, using it as a native counterpart. In the browser on my Mac, using WebAssembly, it was a lot slower unfortunately. Not sure what the problem is for that, maybe the threading or something. And, as I mentioned, something about it errored out on mobile Safari, so it doesn't appear to be the most consistent in the browser. After I'm gonna do some more testing, I'll decide whether running it in the browser is worth it enough, as it doesn't seem to be consistent to implement, or on par in terms of performance. So, the video generation part may be a Node-only script if things don't go quite the right way. I love the speed and dynamic nature the thumbnail generation part, in the browser, so I think that will almost definitely stay there. It kind of sucks to de-couple the project into both browser and Node, rather than just the browser, but I want to take performance over having it in one place. Maybe a bundled Desktop-only Electron app, could be the way to go after all? I kind of don't like the heaviness of that, but that would be easy to distribute and easy to setup from a user-perspective. A web-first PWA would be the *better* option though, that's even better :) So, hopes to getting it to work on-par to native-in the browser :D

I also feel like mobile Apple devices are more than capable at running that, so I want to try my best to not cut them out of the picture, as it would be great to just use your phone (or iPad) to generate the video, since they are definitely powerful enough to encode and edit videos in iMovie, soo... Almost there!! At least it *works* in Chrome. I thought I hit a roadblock at the `SharedArrayBuffer` part, but that workaround successfully made it work :)

**Mammoth WVH**

---
## [tt33415366/art](https://github.com/tt33415366/art)@[7c39c86b17...](https://github.com/tt33415366/art/commit/7c39c86b17c91e651de1fcc0876fe5565e3f5204)
#### Saturday 2022-12-03 03:06:59 by Hans Boehm

Thread suspension cleanup and deadlock fix

Have SuspendAll check that no other SuspendAlls are running, and have
it refuse to start if the invoking thread is also being suspended.
This limits us to a single SuspendAll call at a time,
but that was almost required anyway. It limits us to a single active
SuspendAll-related suspend barrier, a large simplification.
It appears to me that this avoids some cyclic suspension scenarios
that were previously still possible.

Move the deadlock-avoidance checks for flip_function to
ModifySuspendCount callers instead of failing there.

Make single-thread suspension use suspend barriers to avoid the
complexity of having to reaccess the thread data structure from another
thread while waiting for it to suspend. Add a new data structure to
remember the single thread suspension barriers without allocating
memory, This uses a linked list of stack allocated data structures,
as in MCS locks.

The combination of the above avoids a suspend_barrier data structure
that can overflow, and removes any possibility of ModifySuspendCount
needing to fail and retry. Recombine ModifySuspendCount and
ModifySuspendCountInternal.

Simplified barrier decrement in PassActiveSuspendBarriers.
Strengthened the relaxed memory order, it was probably wrong.

Fix the "ignored" logic in SuspendAllInternal. We only ever ignored
self, and ResumeAll didn't support anything else anyway.

Explicitly assume that the initiating thread, if not null, is
registered. Have SuspendAll and friends only ignore self, which was
the only actually used case anyway, and ResumeAll was otherwise wrong.

Make flip_function atomic<>, since it could be read while being cleared.

Remove the poorly used timed_out parameter from the SuspendThreadByX().

Make IsSuspended read with acquire semantics; we often count on having
the target thread suspended after that, including having its prior
effects on the Java state visible. The TransitionTo... functions already
use acquire/release.

Shrink the retry loop in RequestSynchronousCheckpoint. Retrying the
whole loop appeared to have no benefit over the smaller loop.

Clarify the behavior of RunCheckpoint with respect to the mutator
lock.

Split up ModifySuspendCount into IncrementSuspendCount and
DecrementSuspendCount for improved clarity. This is not quite a
semantic no-op since it eliminates some redundant work when
decrementing a suspend count to a nonzero value. (Thanks to
Mythri for the suggestion.)

I could not convince myself that RequestCheckpoint returned false
only if the target thread was already suspended; there seemed to
be no easy way to preclude the state_and_flags compare-exchange
failing for other reasons. Yet callers seemed to assume that property.
Change the implementation to make that property clearly true.

Various trivial cleanups.

This hopefully reduces thread suspension deadlocks in general.
We've seen a bunch of other bugs that may have been due to the cyclic
suspension issues. At least this should make bug diagnosis easier.

Test: ./art/test/testrunner/testrunner.py --host --64  -b
Test: Build and boot AOSP
Bug: 240742796
Bug: 203363895
Bug: 238032384
Change-Id: Ifc2358dd6489c0b92f4673886c98e45974134941

---
## [itseasytosee/tgstation](https://github.com/itseasytosee/tgstation)@[5da871e271...](https://github.com/itseasytosee/tgstation/commit/5da871e2719fb7aac04fb1ec4c85ea7a09a83b36)
#### Saturday 2022-12-03 03:29:32 by RikuTheKiller

Made geysers easier to find (#71608)

## About The Pull Request

This PR raises the geyser spawn rate from 0.1 to 0.15 and increases the
weight of wittel geysers to 10 which is the same as every other special
geyser. (previously 6)

Wittel shouldn't be any less difficult to find than other geysers as all
of the special geysers are equally powerful. Hyper-plasmium oxide can be
used to make extremely powerful explosives that can go beyond maxcaps
and hollow water + protozine can create an infinite amount of strange
reagent.

I've subjected myself to going out of my way to visit lavaland/icemoon
several times to get wittel and each time finding a single geyser takes
about 5 minutes of my time. This, coupled with the fact you really don't
have a lot of time to be wasting on looking for the geysers results in
an unfun experience.

I understand geysers are sort of a necessary evil, however, they
shouldn't be THIS difficult to find. Out of the 10 or so geysers I've
found, only 1 has had wittel in it and it was next to a whelp portal
which ended both me and my miner escort.

I've also hunted the entirety of lavaland with no luck. (Horrendous
experience.)

I've dedicated entire rounds to this, by the way.
## Why It's Good For The Game

If you go out of your way to waste ages hunting for geysers, there
should at least be a reward. That is, in the same round, not after 3 or
more rounds as even megafauna gear isn't gatekept THAT hard.

You shouldn't have to waste this much of a miner's time (who is also
going for megafauna gear) to get something that is arguably less
powerful than what they get for less effort. Megafauna gear is also
available every round and is attained via predictable methods.

This PR will also likely make geyser scanning a more comparable method
of point gain to just mining.

Oh and not to mention that penthrite is available almost roundstart via
luxpens. (It's a wittel chem.)
## Changelog
:cl:
balance: Geysers now spawn more often, especially wittel geysers.
/:cl:

---
## [Spectralized/clovermon-showdown](https://github.com/Spectralized/clovermon-showdown)@[3f40fc1fda...](https://github.com/Spectralized/clovermon-showdown/commit/3f40fc1fda7b5f0f399d4c9acf4a8e63055aa9bd)
#### Saturday 2022-12-03 03:34:29 by Greednut

Small Rootchew line cleanup

+ fuck you sherifuego

---
## [MTandi/tgstation](https://github.com/MTandi/tgstation)@[5252418df0...](https://github.com/MTandi/tgstation/commit/5252418df0ed4726c5bf2a9599f95befd0aca086)
#### Saturday 2022-12-03 03:48:19 by Mothblocks

Create a guide for atomization that includes a new allowance to pull requests that might add dead code (#71429)

@tgstation/commit-access 

I'm proposing a new use for the Atomic tag that we currently virtually
never use.

We have countless pull requests over time, and plenty of which open now,
that are enormous refactors over tens of files with thousands of
additions. We are historically pretty slow to review and merge these,
and it definitely scares a lot of maintainers off. I think part of the
reason is that we do not like dead code being added, which is completely
reasonable at our scale.

However, I propose that, for refactors/purely code stuff, we ease up on
this a lot, and encourage (not require) people to make smaller pull
requests, even to the extent that it creates APIs we do not use yet.

As an example, https://github.com/tgstation/tgstation/pull/71421 does a
massive refactor to carp. It also does some balance changes, which I
think we could agree could be split off if it was enough of a pain.
However, there's a bunch of other stuff that could have been individual
pull requests here with this new allowance.

- The new basic AI behaviors
- The regenerator component
- Pet commands component

These are things that:

- Would not be used until the transition from simple to basic, but are
easily reviewable on their own
- Are easy to REMOVE if the OP does not follow up
- Are easy to FINISH if the OP does not follow up

(I suspect even, for instance, that there are parts of Wallening we
could be merging right now, that's probably gonna be hundreds or
thousands of files long...)

Pros:
- PRs are more often easily reviewable
- PRs are quicker to merge, since we don't have conflicts from editing
one of the 70 files they changed
- Cleanups can be more easily finished by other people. I don't suspect
this will be likely, but it's not easily possible today

Cons:
- We have to mark the PRs as atomic
- Someone needs to look through every so often (I'm thinking like, once
a month or something) to see if the code ended up being used, or if the
committer still plans to use it
- If the PR is adding a complex enough API that isn't modular, it might
be very hard to remove. I suspect for PRs like this that we ask them to
have an implementer before merging.

NL voice would love your thoughts on this

---
## [sindhuyepuri/cs356-hw5](https://github.com/sindhuyepuri/cs356-hw5)@[90858e0c77...](https://github.com/sindhuyepuri/cs356-hw5/commit/90858e0c77972b5f5468922bcf7efa3dd2fda6df)
#### Saturday 2022-12-03 03:58:19 by Sindhu Yepuri

i hate this ms stupid fucking shit i am so tired holy crap

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[9499a1542b...](https://github.com/tgstation/tgstation/commit/9499a1542b156eb32efb25e0310b1fe7077caf5c)
#### Saturday 2022-12-03 04:03:19 by itseasytosee

Corrects error in stamina HUD element display calculation. Increases stamina HUD readability. (#71623)

## About The Pull Request
Stamina was checking health instead of maxHealth. This is probably a
remnant from when the damage stacked.
I stopped the stamina from appearing like you had no stamina whenever
you were stunned or knockdown. This would obscure potentially value
information from the player while being unclear to interpret.
We should probably represent status effects like this to the player, but
through the stamina bar is not a useful method.
The stamina bar is for stamina.
Additionally, the stamina bar will now be greyed out while you are dead,
like your health bar.

I've done alot of work increasing the readability of the stamina bar.
Firstly, I've cut some fat, removing the 100% sign when you are at full
and the blinking exclamation point when you are close to zero. They
aren't nessisary and add clutter.
There's no more "full but because its blinking bright yellow you are
actually at 20% or less" or "empty but because the whole thing isn't
blinking you still have stamina"
Its a now simple meter that decreases in 20% increments which blinks
softly, at darker and more red colors the lower the meter goes, blinking
faster at the higher percentages. When you are at zero, the empty space
slowly glows a dark red.
Its much more reasonable and intuitive than whatever the hell the old
sprites were doing.
## Why It's Good For The Game
For the HUD changes, it improves the game feel, at least from my
experience. We could probably benefit from an entirely new stamina bar
design, but finding the right one is gonna be tricky.
## Changelog
:cl: itseasytosee
fix: Stamina damage display calculation should be much more sane and
reliable now
imageadd: Simplified the stamina hud
/:cl:

---
## [simonw/disaster-data](https://github.com/simonw/disaster-data)@[24ebc774c4...](https://github.com/simonw/disaster-data/commit/24ebc774c4b77f9ec8948cd5d75db1aabc2021ab)
#### Saturday 2022-12-03 04:21:56 by disaster-scrapers

fema/shelters: 8 shelters removed

8 shelters removed:
  Mt. Enon Baptist Church in Dayton, OH (OPEN)
    https://www.google.com/maps/search/39.7551139,-84.2208322
    population = 0

  St. Bernadette Catholic Parish in Lakewood, CO (OPEN)
    https://www.google.com/maps/search/None,None
    population = 0

  Arapahoe County Fairgrounds in Aurora, CO (OPEN)
    https://www.google.com/maps/search/None,None
    population = 2

  Ann & Chuck Dever Center in Englewood, FL (OPEN)
    https://www.google.com/maps/search/26.924404,-82.314119
    population = 41

  Del Tura Shelter in North Fort Myers, FL (OPEN)
    https://www.google.com/maps/search/26.738655,-81.912434
    population = 165

  God's Grace Community Church in Houston, TX (OPEN)
    https://www.google.com/maps/search/None,None
    population = 0

  Salvation Army - Lebanon in Lebanon, PA (OPEN)
    https://www.google.com/maps/search/40.34820821,-76.43002593
    population = 11

  Tibbie Baptist Church in Tibbie, AL (OPEN)
    https://www.google.com/maps/search/None,None
    population = 0

---
## [Zonespace27/Skyrat-tg](https://github.com/Zonespace27/Skyrat-tg)@[cf4a194e86...](https://github.com/Zonespace27/Skyrat-tg/commit/cf4a194e86d53d57397f6de4febbea0de9c6ef57)
#### Saturday 2022-12-03 04:28:06 by SkyratBot

[MIRROR] Biogen Refactor and Code Cleanup, Faster Biomass Conversion and No More Biomass Cap! [MDB IGNORE] (#17828)

* Biogen Refactor and Code Cleanup, Faster Biomass Conversion and No More Biomass Cap! (#71563)

## About The Pull Request
So, I looked at the Biogenerator code and there was just, _so_ much old
and undocumented code, that I just spazzed out and started documenting
and refactoring everything. There's now a lot less usage of contents
lookups and for loops, and _almost_ everything is documented, now, too.

As for the changes, as you can see in the title, I made biomass
conversion faster. How much faster, you ask? 5 times faster with default
parts, up to 20 times faster with the best parts. It was painfully slow,
and that's not fun for anyone.

I also lifted the biomass cap. It wasn't useful, it wasn't fun, and
Melbert didn't really agree with it either. However, I enjoyed the look
of the biomass going up, so I gave it a max visual amount of 5000, so
you get to see it gradually filling up as you put your first 5000
biomass in. After that, you do you, chief. Watch the funny numbers go up
all you want.

I also improved the maths so that it wasn't just rounding stuff
constantly, and also gave a little bit more insight on how much biomass
everything would cost you, down to two decimals. If there's no decimals,
it won't show them, however.

<details>
<summary>Here's what that looks like now:</summary>
That's one screenshot per different decimal places, there's no trailing
zeros because I think we can all universally agree that those look bad
in this kind of setting.

![image](https://user-images.githubusercontent.com/58045821/204120744-a8c398dc-7c19-4ee0-a8cb-5615f1dce1ea.png)

![image](https://user-images.githubusercontent.com/58045821/204120749-90aae203-bdb8-4322-a657-bb4fd313d808.png)

![image](https://user-images.githubusercontent.com/58045821/204120755-8bed494d-0d70-4b4a-afa2-413610089f6d.png)

</details>

There's now also more information displayed when you examine the biogen,
namely, how many items it has stored, and how many it can hold. I also
fixed the formatting a bit, so it looks ever so slightly cleaner.

Other than that, I just improved the code everywhere I saw it to be
fitting, there shouldn't be any single-letter variables in there
anymore, and the code should be more spaced out. Honestly, at this
point, I wrote most of this code six hours ago so I don't remember all
of it, and I'm too lazy to go through and check what I've changed again.
Diff and changelog are there for that.

## Why It's Good For The Game
So, I'll be honest, there were two big reasons that motivated me to do
this. First of all, the biomass cap. That was a little silly, anyone
that has spent more than one shift in Hydroponics knows that you usually
only put Watermelons in the biomass generator as they're usually the
thing that nets you the most biomass. Botanists will generally stock the
fridges first, and if they have a lot of excess, they'll put it in the
generator if they want, but that's rarely what was done. I've talked
with @ MrMelbert about it and he gave me the go-ahead, as can be seen
here:

![image](https://user-images.githubusercontent.com/58045821/204115174-fb2610c0-61c5-44e1-845e-cc6925ee33e6.png)

The other reason was the excruciatingly slow processing speed, which
I've fixed. So we're good now. :)

## Changelog

:cl: GoldenAlpharex
refactor: Went through and refactored a lot of the old code of the
biogenerator, and made multiple improvements to its logic, which should
hopefully make it behave more consistently. Nearly all of it is now also
fully documented, so as to make it easier for anyone else that has to
sift through it in the future.
qol: The biogenerator now processes items five times faster, up to 20
times faster if properly upgraded!
qol: The biogenerator is no longer capped on biomass. Its visuals will
change up until 5000 biomass, but you're free to go as high as you'd
like with it! Sky's the limit!
fix: Fixed the logic of the biogenerator that would make it so the
amount of biomass used for recipes was wildly inconsistent. Now, there's
no more back-end rounding up, it's all on the front end when it needs to
be, so there's no loss or gain of biomass when there shouldn't be.
spellcheck: Fixed a capitalization issue with the seaweed sheets in the
biogenerator recipes.
spellcheck: Fixed multiple inconsistencies between the messages sent to
your chat by the biogenerator.
/:cl:

* Biogen Refactor and Code Cleanup, Faster Biomass Conversion and No More Biomass Cap!

Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>

---
## [fnfpwwwwwp/saw-psych-engine-0.5.2h](https://github.com/fnfpwwwwwp/saw-psych-engine-0.5.2h)@[fc20852829...](https://github.com/fnfpwwwwwp/saw-psych-engine-0.5.2h/commit/fc20852829094b004c726513ceb1cf801c22c41c)
#### Saturday 2022-12-03 05:37:12 by fnfpwwwwwp

Merge pull request #3 from Liulw123/patch-1

fuck your mother up

---
## [IHadMyUsernameTaken/goonstation](https://github.com/IHadMyUsernameTaken/goonstation)@[693f38836f...](https://github.com/IHadMyUsernameTaken/goonstation/commit/693f38836f362b8083c1d0169c7e5c17196852f1)
#### Saturday 2022-12-03 08:17:15 by aloe

why do you set vis_flags if you aren't going to use vis_contents fuck you

---
## [LemonInTheDark/tgstation](https://github.com/LemonInTheDark/tgstation)@[ad0f682b4f...](https://github.com/LemonInTheDark/tgstation/commit/ad0f682b4f2068098a74222b2b5cba47225ae1b3)
#### Saturday 2022-12-03 09:17:21 by LemonInTheDark

Fixed the funny haha black overlays

I forgot to have the "no turf exists" case default to the base plane. am
stupid, sorry :(

---
## [Offroaders123/NBTify](https://github.com/Offroaders123/NBTify)@[7e4b34e79c...](https://github.com/Offroaders123/NBTify/commit/7e4b34e79cc313658d4ec6628e58d94a93093503)
#### Saturday 2022-12-03 09:37:06 by Offroaders123

Naming Synchrony + IO Methods Rename v3

Changes:
- Moving away from my `NBTView`-type naming scheme, now `NBTReader` and `NBTWriter` will use methods prefixed with `read` and `write` respectively, rather than `get` and `set`.
- Organized some code declarations and a few other names here and there.
- NBT tag ID values and their TS type now are consistently referred to as `type`, rather than `tag`, in regards to variable naming and such.
- Updated the error messages and types for `NBTReader`. Now they have a bit more information that you can use to debug any parsing issues you may run into when reading NBT data.

Sorry if this changelog is a mess, I coded a lot today, already after a day at work, and it's late, so yeah haha. Getting sleepy ;)

---
## [Time-Green/tgstation](https://github.com/Time-Green/tgstation)@[a753229ee2...](https://github.com/Time-Green/tgstation/commit/a753229ee2541e32164772f05330669d3c6b75d8)
#### Saturday 2022-12-03 09:52:39 by GoldenAlpharex

Biogen Refactor and Code Cleanup, Faster Biomass Conversion and No More Biomass Cap! (#71563)

## About The Pull Request
So, I looked at the Biogenerator code and there was just, _so_ much old
and undocumented code, that I just spazzed out and started documenting
and refactoring everything. There's now a lot less usage of contents
lookups and for loops, and _almost_ everything is documented, now, too.

As for the changes, as you can see in the title, I made biomass
conversion faster. How much faster, you ask? 5 times faster with default
parts, up to 20 times faster with the best parts. It was painfully slow,
and that's not fun for anyone.

I also lifted the biomass cap. It wasn't useful, it wasn't fun, and
Melbert didn't really agree with it either. However, I enjoyed the look
of the biomass going up, so I gave it a max visual amount of 5000, so
you get to see it gradually filling up as you put your first 5000
biomass in. After that, you do you, chief. Watch the funny numbers go up
all you want.

I also improved the maths so that it wasn't just rounding stuff
constantly, and also gave a little bit more insight on how much biomass
everything would cost you, down to two decimals. If there's no decimals,
it won't show them, however.


<details>
<summary>Here's what that looks like now:</summary>
That's one screenshot per different decimal places, there's no trailing
zeros because I think we can all universally agree that those look bad
in this kind of setting.


![image](https://user-images.githubusercontent.com/58045821/204120744-a8c398dc-7c19-4ee0-a8cb-5615f1dce1ea.png)

![image](https://user-images.githubusercontent.com/58045821/204120749-90aae203-bdb8-4322-a657-bb4fd313d808.png)

![image](https://user-images.githubusercontent.com/58045821/204120755-8bed494d-0d70-4b4a-afa2-413610089f6d.png)

</details>

There's now also more information displayed when you examine the biogen,
namely, how many items it has stored, and how many it can hold. I also
fixed the formatting a bit, so it looks ever so slightly cleaner.

Other than that, I just improved the code everywhere I saw it to be
fitting, there shouldn't be any single-letter variables in there
anymore, and the code should be more spaced out. Honestly, at this
point, I wrote most of this code six hours ago so I don't remember all
of it, and I'm too lazy to go through and check what I've changed again.
Diff and changelog are there for that.

## Why It's Good For The Game
So, I'll be honest, there were two big reasons that motivated me to do
this. First of all, the biomass cap. That was a little silly, anyone
that has spent more than one shift in Hydroponics knows that you usually
only put Watermelons in the biomass generator as they're usually the
thing that nets you the most biomass. Botanists will generally stock the
fridges first, and if they have a lot of excess, they'll put it in the
generator if they want, but that's rarely what was done. I've talked
with @MrMelbert about it and he gave me the go-ahead, as can be seen
here:


![image](https://user-images.githubusercontent.com/58045821/204115174-fb2610c0-61c5-44e1-845e-cc6925ee33e6.png)

The other reason was the excruciatingly slow processing speed, which
I've fixed. So we're good now. :)

## Changelog

:cl: GoldenAlpharex
refactor: Went through and refactored a lot of the old code of the
biogenerator, and made multiple improvements to its logic, which should
hopefully make it behave more consistently. Nearly all of it is now also
fully documented, so as to make it easier for anyone else that has to
sift through it in the future.
qol: The biogenerator now processes items five times faster, up to 20
times faster if properly upgraded!
qol: The biogenerator is no longer capped on biomass. Its visuals will
change up until 5000 biomass, but you're free to go as high as you'd
like with it! Sky's the limit!
fix: Fixed the logic of the biogenerator that would make it so the
amount of biomass used for recipes was wildly inconsistent. Now, there's
no more back-end rounding up, it's all on the front end when it needs to
be, so there's no loss or gain of biomass when there shouldn't be.
spellcheck: Fixed a capitalization issue with the seaweed sheets in the
biogenerator recipes.
spellcheck: Fixed multiple inconsistencies between the messages sent to
your chat by the biogenerator.
/:cl:

---
## [Time-Green/tgstation](https://github.com/Time-Green/tgstation)@[35b5ac0c4e...](https://github.com/Time-Green/tgstation/commit/35b5ac0c4e6bbaf2adf277a7ea7a4a4eab89726b)
#### Saturday 2022-12-03 09:52:39 by Fikou

Psykers (#71566)

## About The Pull Request
Finishes #66471
At burden level nine (or through a deadly genetic breakdown), you now
turn into a psyker.
This splits your skull in half and transforms it into a weird fleshy
mass. You become blind, but your skull is perfectly suited for sending
out psychic waves. You get potent psy abilities.
First one is brainwave echolocation, inspired by Gehennites (but not as
laggy).
Secondly, you get the ability of Psychic Walls, which act similarly to
wizard ones, but last shorter, and cause projectiles to ricochet off
them.
Thirdly, you get a projectile boost ability, this temporarily lets you
fire guns twice as fast and gives them homing to the target you clicked.
Lastly, you get the ability of psychic projection. This terrifies the
victim, fucking their screen up and causing them to rapidfire any gun
they have in their general direction (they'll probably miss you)
With most of the abilities being based around guns, a burden level nine
chaplain now gets a new rite, Transmogrify. This lets them turn their
null rod into a 5-shot 18 damage .77 revolver. The revolver possesses a
weaker version of antimagic (protects against mind and unholy spells,
but not wizard/cult ones). It is reloaded by a prayer action (can also
only be performed by a max burdened person).
General Video: https://streamable.com/w3kkrk
Psychic Projection Video: https://streamable.com/4ibu7o

![image](https://user-images.githubusercontent.com/23585223/204150279-a6cf8e2f-c678-476e-b72c-6088cd8b684b.png)

## Why It's Good For The Game
Rewards the burdened chaplain with some pretty cool stuff for going
through hell like losing half his limbs, cause the current psychics dont
cut it as much as probably necessary, adds echolocation which can be
used for neat stuff in the future (bat organs for DNA infuser for
example).

## Changelog
:cl: Fikou, sprites from Halcyon, some old code from Basilman and
Armhulen.
refactor: Honorbound and Burdened mutations are brain traumas now.
add: Psykers. Become a psyker through the path of the burdened, or a
genetic breakdown.
add: Echolocation Component.
/:cl:

Co-authored-by: tralezab <spamqetuo2@gmail.com>
Co-authored-by: tralezab <40974010+tralezab@users.noreply.github.com>
Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [InsightfulParasite/lobotomy-corp13](https://github.com/InsightfulParasite/lobotomy-corp13)@[0220bde488...](https://github.com/InsightfulParasite/lobotomy-corp13/commit/0220bde48808454df3754d7c71953f66553dcd47)
#### Saturday 2022-12-03 10:01:35 by PotatoTomahto

pathfinding

revert

oops

oops 2

god fragment

fixes

fixes oopsie

forgot scorched girl

real scorched fix:

typo

better patrolling

final

forgot about dreaming

dreaming current name

fragment oopsies

violet oopsie

really the final one

final final one

---
## [maesierra/adventOfCode2022](https://github.com/maesierra/adventOfCode2022)@[6585c707fc...](https://github.com/maesierra/adventOfCode2022/commit/6585c707fc9caabf4e87ce3b285a990ee48369fb)
#### Saturday 2022-12-03 11:38:46 by maesierra

day 3

Today I missed php or java far to much. The lack of ternaries and decent array manipulation libaries is quite frustrating.
I hate having to do simple stuff like array_chunk
Also Java's putIfAbsent is so brilliant

I really would had preferred to use intersecting sets for part2 solution but I wasn't in the mood to do my own implementation of slice intersection.
Something that I could had have for free in both Java or php.

People should do the maths, the amount of time spent to do getters/setters and Java unnecesary verbosity is a small price to pay to have the collections and streams. I probably could have solved today's in Java in half of the lines.

I have mixed feelings about maps key handling in go, the double return is weird. I think I prefer putIfAbsent/getOrDefault approach in Java. But at least map iteration is nice

---
## [migzstotomas/app-dev](https://github.com/migzstotomas/app-dev)@[9767020bae...](https://github.com/migzstotomas/app-dev/commit/9767020bae6e90b9271c7cafce09c3c1b4ed6d70)
#### Saturday 2022-12-03 12:50:57 by migzstotomas

Update README.md

1. Lucifer - The series revolves around the story of Lucifer Morningstar (Tom Ellis), the DC Universe's version of the Devil, who abandons Hell for Los Angeles where he runs his own nightclub named Lux and becomes a consultant to the Los Angeles Police Department (LAPD).
2. Chainsaw Man - Denji was a small-time devil hunter just trying to survive in a harsh world. After being killed on a job, he is revived by his pet devil Pochita and becomes something new and dangerous—Chainsaw Man! Denji's a poor young man who'll do anything for money, even hunting down devils with his pet devil-dog Pochita.
3. Hunter X Hunter - The story focuses on a young boy named Gon Freecss who discovers that his father, who left him at a young age, is actually a world-renowned Hunter, a licensed professional who specializes in fantastical pursuits such as locating rare or unidentified animal species, treasure hunting, surveying unexplored enclaves, or hunting down lawless individuals. Gon departs on a journey to become a Hunter and eventually find his father. Along the way, Gon meets various other Hunters and encounters the paranormal.

---
## [C3NTENO/app-dev](https://github.com/C3NTENO/app-dev)@[a2b41d878b...](https://github.com/C3NTENO/app-dev/commit/a2b41d878b6253b2afa39f489103bcabcbc0f785)
#### Saturday 2022-12-03 13:44:38 by C3NTENO

Update README.md

These are my favorite anime series 
Naruto - is a Japanese manga series written and illustrated by Masashi Kishimoto. It tells the story of Naruto Uzumaki, a young ninja who seeks recognition from his peers and dreams of becoming the Hokage, the leader of his village.
Haikyuu - is a Japanese manga series written and illustrated by Haruichi Furudate. It was serialized in Shueisha's shōnen manga magazine Weekly Shōnen Jump from February 2012 to July 2020, with its chapters collected in 45 tankōbon volumes. The story follows Shoyo Hinata, a boy determined to become a great volleyball player despite his small stature.
Chainsaw Man - Chainsaw Man follows the story of Denji, an impoverished young man who makes a contract that fuses his body with that of a dog-like devil named Pochita, granting him the ability to transform parts of his body into chainsaws.
Blue Lock - is a Japanese manga series written by Muneyuki Kaneshiro and illustrated by Yusuke Nomura. It has been serialized in Kodansha's Weekly Shōnen Magazine since August 2018, with its chapters collected in 21 tankōbon volumes as of October 2022. An anime television series adaptation produced by Eight Bit premiered in October 2022.

---
## [phenax/advent-of-coolio-2022](https://github.com/phenax/advent-of-coolio-2022)@[949cedba72...](https://github.com/phenax/advent-of-coolio-2022/commit/949cedba72071d33e24015b29b83bbb93b16c30c)
#### Saturday 2022-12-03 14:46:48 by Akshay Nair

feat: fucking hell. had to do this in rust again. hate elm now.

---
## [DroneBetter/ChessPieceVision](https://github.com/DroneBetter/ChessPieceVision)@[5707be5e13...](https://github.com/DroneBetter/ChessPieceVision/commit/5707be5e13ca80d500d414e1d7194d74da5922d8)
#### Saturday 2022-12-03 15:05:33 by DroneBetter

Add eightfold reducer and Cburnett pieces

It occurred to me when I was making the cellular automaton mode that the eightfold reducer would be useful to others who wanted to make their own programs for searching for oscillators (or even simulating from all nonequivalent initial states in infinite planes with RLEs in apgsearch or something) in isotropic rules, but the comparable performance of doing so this way (as opposed to only iterating over all unreduced ones and discarding those that are not the minimal orientation of themselves) wouldn't be important enough to warrant it. Indeed, making such a complicated system as I had seemed something of a mistake. For 5*5 boards, generating all 4211744 nonequivalent states takes 56s with it on my computer, whereas all 33554432 unreduced ones take 460s (though this is with the trivial tuple comprehension in generateCellular()'s outermost else, I think an accumulate()-based one that recorded a single structure it mutated in-place could be faster)
However, upon learning of the Pólya enumeration theorem, I realised that, say on an odd-width board, by beginning with the innermost layer (a single cell) and using the theorem to compute the number of states with it turned off, you can deduce, given an index, whether this cell is on or off based on whether it's in the first or second half, and more generally which of the indexes of states obtainable by changing only the innermost cell it exceeds. This is all very simple, but after determining this, you can then search each "legal" state of the first orthogonally-displaced layer (ie. each that is the canonical representation of itself under symmetry), and determine how many nonequivalent states of the board excluding them and the innermost cell there are, under action of the symmetry group of reflections that it still allows. By only slightly changing the symmetry function, this could be trivially implemented, allowing any state to be indexed (and vice versa, by enacting the same process the other way around) by a series of arithmetic operations asymptotic to the number of layers (and thus cells). Being that bisections could obtain it in logarithmic time with respect to the length of the states list, which itself takes exponential space with respect to the cells, this isn't an improvement, and indeed, running __getitem__() on each index takes far longer than generateCellular(), which only takes logarithmic time with respect to cells for the mutation (which I will eventually implement as __next__() for slicing purposes), however this allows __getitem__() to run in the same order of time without need for generating and storing it all (taking, for 5*5, at the very least 100.4MiB of RAM (it would information-theoretically be 12.55MiB but the convention for processors is to store a byte per boolean), but much more due to it being Python and them not being arrays). I haven't seen this idea of mine implemented already (though I have seen some Catagolue censuses with soup-counts in A054247, so others must have considered this, at least), and it may have applications to multithreading (being that you could set each thread about simulating contiguous slices of even size) and even distributed computing.
Also, I have thought some more and realised that the application of the idea similar to that of tablebases, of generating and storing the entire state transition diagram and searching for cycles all simultaneously, is perhaps less efficient than considering each individually, being that it takes about logarithmic space to store all oscillators with respect to the time spent searching, and logarithmically many tiimes that to store numbers of occurrences of each (if you would like to), so perhaps I ought to make an option not to (especially considering this new tool).
This is only a preliminary commit, it is very inelegant (ie. the symmetry(), __getitem__() and __index__() functions contain a great deal of repetition (always repeat)) and will be reduced and optimised a great deal (as well as having some of the testing parts cleaned up), which will be fun (expanding and inlining things in order to simplify them)
Also, I'm very sorry for not having been so active here as of late, I have been busy with real life (and will continue to be so for the foreseeable future)

Regarding the images, now others using the tablebase program besides me will be able to see the nice lichess images instead of geometric shapes (but you don't get to use your imagination so much), though I don't know how to import svg's in Pygame at target resolutions instead of original ones (it seems you must load in and change the file metadata, I think), though it doesn't matter too much because chess isn't a very detail-intensive game and when there are hundreds or even thousands of instances being reprinted each frame in the state transition diagram mode, it's probably for the best.

---
## [Isla-web/Fork-Cutter](https://github.com/Isla-web/Fork-Cutter)@[88bc5c4c54...](https://github.com/Isla-web/Fork-Cutter/commit/88bc5c4c54c1aadcdc6cc9a24c0f69d4bebce97c)
#### Saturday 2022-12-03 17:19:16 by Kimi

another translation patches because i fucked it up

i hate myself

---
## [ZephyrTFA/tgstation](https://github.com/ZephyrTFA/tgstation)@[83f475aa7e...](https://github.com/ZephyrTFA/tgstation/commit/83f475aa7ec4290c6961f1f14c5da80f340989b8)
#### Saturday 2022-12-03 17:38:00 by tralezab

Adds the DNA Infuser, a genetics machine you feed corpses to infuse their DNA with yours! What could go wrong?! (#71351)

## About The Pull Request  
Adds the "DNA Infuser" to genetics. One person enters, a corpse is added
to the machine, and you can activate the machine to "infuse" the subject
with the DNA. This converts one random organ from a set into the
mob-related organ.

### Rat mutation 🐀

Rats can be fed in to turn you into a rat-creature-thing!
```diff
+See better in the dark
+Can pretty much eat anything! Toxic foods, gross foods, whatever works!
+Smaller, and can climb tables
?Randomly squeaks occasionally?
-Take twice as much damage
-Vulnerable to flashes
-Gets hungry MUCH quicker.
-Yes, eat anything, but only ENJOY dairy.
```
Having every rat organ at once allows you to ventcrawl nude!

### Carp mutation 🐟 

Carp work for a mutation as well!
```diff
+Strong jaws, that drop teeth over time!
+Space immunity! Breathe in space, unbothered by pressure or cold!
+Smaller, and can climb tables
-Can't block your jaws with a mask
-Can't take the heat, overheats easily
-Can only breathe in environments that have minimal or no oxygen
-Nomadic. If you don't enter a new zlevel for awhile, you'll start feeling anxious.
```
Having every carp organ at once allows you to swim through space!

### Fly mutation 🪰 

Any corpses without organs to turn into turn into fly organs! Fly organs
now have a bonus for collecting them all, transforming you into a fly,
when you pass the threshold. But even without those, fly organs are
technically... organs. They most of the time work like normal ones.

## Todo 🐦 

- [x] Finish the infuser code
- [x] Create a little booklet that shows what kind of shit you can turn
into, hopefully i can autogenerate this based off of organ set subtypes
list
- [x] sprite/slap a color on rat mutant organs
- [x] Maybe make a *few* more organ sets

## Why It's Good For The Game 🐑 

Oops, I forgor to fill this out! My hackmd is here.

https://hackmd.io/@bazelart/ByFkhuUIi

## Changelog 🧬 

:cl: Tralezab code, Azlan + Azarak (Az gaaang) for the organs
add: Added the DNA infuser to genetics! Person goes in, corpse goes in,
and they combine!
add: Try not to turn yourself into a fly, OK?
/:cl:

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>
Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [Etaash-mathamsetty/HeroicGamesLauncher](https://github.com/Etaash-mathamsetty/HeroicGamesLauncher)@[3f6541c8a7...](https://github.com/Etaash-mathamsetty/HeroicGamesLauncher/commit/3f6541c8a700511cea9f0c9b572a5d2138ee76e3)
#### Saturday 2022-12-03 17:38:50 by Mathis Dröge

Improve README and developer experience (#1807)

* Update VSCode configuration

* Lots of README changes

- Update our bages; might've overdone it a little, but they're fun to add :^)
- Add badges for Web Technologies used
- Rewrite & bump up system requirements a bit
- Wrap the Language list, Development in a container, and Screenshots in
  <details>; this makes the page load faster and makes it seem less
  daunting
- Add a Flathub badge to the Flatpak section
- Unify Linux install instructions (as much as possible)
- Remove 3rd-party APT repository
  In my opinion, we have enough distribution formats already, and the
  install instructions are a little dodgy
- Add Beta AUR package to the list
- Clarify Windows install instructions by splitting up WinGet and manual
  install
- Make "Development environment" its own section
- Remove Beta and Alpha notes on Windows and macOS build instructions
- Explain what exactly is happening when you run `yarn dev` and in which
  scenarios you might want to use it
- Move the "Back to top" badge to the actual bottom of the page

* Add a Content Security Policy

This doesn't really do much in our situation:
- Just in case someone ever manages to load a website in Heroic's main
  window, no JS can run inside it
- Gets rid of the warning in the console when testing with `yarn dev`

I've tested the Webviews (unaffected) and links to ProtonDB and such
(also unaffected, not sure why though). Please test if this breaks
anything

---
## [greeveu/AdvancedBan](https://github.com/greeveu/AdvancedBan)@[1d9e6910e3...](https://github.com/greeveu/AdvancedBan/commit/1d9e6910e33bda906ee03ffada08377a91a604ad)
#### Saturday 2022-12-03 20:39:13 by Achsion

added a (hopefully) somewhat usable api as a first step to let the fricking plugin handle its own shit without having to rely on other plugins to know the god damn sql queries required to fetch some poor ass data

---
## [Gofawful5/Skyrat-tg](https://github.com/Gofawful5/Skyrat-tg)@[b922aef977...](https://github.com/Gofawful5/Skyrat-tg/commit/b922aef97718aeffc0d3b450012575df2d065e20)
#### Saturday 2022-12-03 21:53:37 by SkyratBot

[MIRROR] Adds Some Supermatter Effects  [MDB IGNORE] (#17734)

* Adds Some Supermatter Effects  (#67866)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

This pull request adds a variety of Supermatter delamination effects to
make the crystal a bit more fun to watch and stare at. The initial
filter effects and animations are from Baystation12, but I have adapted
it to make it fun to watch!

It'll be a bit hard to explain in text, so this is the text explanation.

For normal running conditions, the Supermatter will emit pretty golden
rays, and a large campfire like that glow that grows and shrinks based
on it's power level.

![dreamseeker_vnw1BL7DNy](https://user-images.githubusercontent.com/77420409/174471609-7be70234-5eae-4839-b551-1c28145d6b60.gif)

For high power conditions, such as high O2 or CO2 amounts, the
Supermatter's rays will glow red and it will emit red light, aswell as
turn red (like before, unchanged).

https://user-images.githubusercontent.com/77420409/174471693-e191ee47-1a01-4b76-8570-9d12b994c2d4.mp4

When the conditions for a cascade, singularity, or a tesla are met, the
colours and rays emitting from the crystal will change to match!

https://user-images.githubusercontent.com/77420409/174471747-dffb3beb-dd38-42a1-a97b-7262dabd60af.mp4

https://user-images.githubusercontent.com/77420409/174471765-af1927e8-a48e-4fd5-a35c-6b3aa53c5add.mp4

Also, I've added more sucking power to the crystal during its final
countdown for DRAMATIC EFFECT. If the singularity conditions are met,
the supermatter will SUCK THINGS INTO IT, even if they are bolted to the
GROUND. Just like a singularity! It's REALLY COOL.
https://streamasaurus.com/sharing/singularity_full.mp4 <--17MB video.
UPDATE 1: New rays for the singulo

https://user-images.githubusercontent.com/77420409/174933219-0118748a-02da-40f8-9b99-06009e197cc8.mp4
UPDATE 2:
Singularity delamination final countdown effect??:

https://user-images.githubusercontent.com/77420409/175421220-66bae109-204d-44ee-8a67-c18ce8eff3ba.mp4

When the supermatter has reached the FINAL COUNTDOWN but does NOT meet
the criteria for a singularity, it will simply YOINK everything
unwrenched towards, like a gravitational anomaly, range based on power
at the time. Not as crazy as the singularity. Most things will get
slapped against walls.

Here, have another cool delamination demo showing the criteria's
swapping mid countdown!
https://streamasaurus.com/sharing/modeswapping.mp4 <-- 17.5MB

I am likely missing something important from this body as I am drowsy
making this! I will update this body with anything I forgot to note that
I did.

## Why It's Good For The Game

The supermatter is a a very cool thing, but it could be cooler. I think
the visual experience could do with a bit of an upgrade, as visual
feedback is really cool and impressive to watch! You could tell more
about the crystal without looking at the console, but not everything or
precise numbers.

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
add: The Supermatter crystal will now emit rays of light, varying on
it's power level and situation.
code: improves a formatting and comment spelling
fix: The Causality field now actually shows up!
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

Co-authored-by: tralezab <40974010+tralezab@ users.noreply.github.com>

* Adds Some Supermatter Effects

Co-authored-by: nevimer <77420409+nevimer@users.noreply.github.com>
Co-authored-by: tralezab <40974010+tralezab@ users.noreply.github.com>

---
## [Gofawful5/Skyrat-tg](https://github.com/Gofawful5/Skyrat-tg)@[60d0ec8afe...](https://github.com/Gofawful5/Skyrat-tg/commit/60d0ec8afe8922a0a23d9d0ed13032a57455e6c0)
#### Saturday 2022-12-03 21:53:37 by SkyratBot

[MIRROR] Fixes antag hud icons disappearing if mesons were equipped [MDB IGNORE] (#17710)

* Fixes antag hud icons disappearing if mesons were equipped (#71155)

## About The Pull Request

They sit on plane 0, IE the darkness plane. So if say, the darkness
plane was alpha'd away (which we have to do with see_blackness), then so
goes the hud element. stupid stupid stupid stupid

## Why It's Good For The Game

Fixes a derivation of #68087
Not all of it, since most of that came about pre plane cube and likely
has to do with z'd image shenanigines. I got it to replicate once
randomly but then it stopped. v annoying. There is a linked issue report
that mentions mesons however, which this does resolve.

## Changelog
:cl:
fix: You can now see antag hud icons AND see through walls. WOW
/:cl:

* Fixes antag hud icons disappearing if mesons were equipped

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [ani2796/minioo-compiler](https://github.com/ani2796/minioo-compiler)@[845b87e835...](https://github.com/ani2796/minioo-compiler/commit/845b87e83551d08cb002e6ba61cdea71366e8ba6)
#### Saturday 2022-12-03 21:56:53 by Anirudh Sriram

Happy thanksgiving!

I thank the following people for making my life better:
- My parents and my brother
- Samriddhi
- My friends
- My professors
- my extended family

I hope to have a refreshing holiday, and if you're reading this, I wish
you the very best :)

---
## [MrSableye/clovermon-showdown](https://github.com/MrSableye/clovermon-showdown)@[6d337bdac2...](https://github.com/MrSableye/clovermon-showdown/commit/6d337bdac26661f4209c26f0d1db7497984806d2)
#### Saturday 2022-12-03 22:19:59 by Mr. Sableye

Fixes Boltbeam (except probably some weird edge cases but fuck you)

---
## [sioodmy/dotfiles](https://github.com/sioodmy/dotfiles)@[cc302f826a...](https://github.com/sioodmy/dotfiles/commit/cc302f826ae87fd7feac59d35d760137f7858c8f)
#### Saturday 2022-12-03 23:11:44 by sioodmy

feat: firefox cache on tmpfs

holy shit thats schizo as fuckkk

---
## [etherware-novice/tgbagilsstation](https://github.com/etherware-novice/tgbagilsstation)@[29d766e25f...](https://github.com/etherware-novice/tgbagilsstation/commit/29d766e25f18c5030972562ed649832077cdfc95)
#### Saturday 2022-12-03 23:32:03 by LemonInTheDark

Fixes attempting to offset floating planes (#71490)

## About The Pull Request

This is a dumb idea, and leads to fucked rendering on occasion

## Why It's Good For The Game

Fixes another portion of #70258, a player will no longer have a hidden
antag hud if they move down a z level after getting an antag. We were
trying to offset the floating plane of their image, and it went to shit.
Also fixes a bug with observers not having antag huds for the combo hud
to see. We were only giving them one on mind.on_transfer, rather then on
mind assignment. I hate mindcode

---

