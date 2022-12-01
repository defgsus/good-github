## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-11-30](docs/good-messages/2022/2022-11-30.md)


2,332,958 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,332,958 were push events containing 3,500,054 commit messages that amount to 257,920,218 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 53 messages:


## [MTandi/tgstation](https://github.com/MTandi/tgstation)@[a753229ee2...](https://github.com/MTandi/tgstation/commit/a753229ee2541e32164772f05330669d3c6b75d8)
#### Wednesday 2022-11-30 00:04:40 by GoldenAlpharex

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
## [nelsonmilum/NetHack](https://github.com/nelsonmilum/NetHack)@[8a549b0a60...](https://github.com/nelsonmilum/NetHack/commit/8a549b0a602fdb13d13fa83bb2f6b1d1a1a257cf)
#### Wednesday 2022-11-30 00:05:23 by Michael Meyer

Shopkeepers hold a grudge against past thieves

When you steal from a shop, its shopkeeper will remember you as a thief
and charge you higher prices in the future (as well as be more curt and
less polite in interactions with you, though not outright hostile) even
if you pacify them, or die on the level and revisit it later as a bones
file.  This was an idea aosdict had, and I think it makes sense that a
shopkeeper doesn't forgive and forget, immediately returning to treating
you exactly like anyone else, just because you were terrorized into
paying her back.  Paying a shopkeeper off may cause her to stop actively
attacking you, but it feels like she'd have her eye on you as a known
thief going forward (and maybe would hang up a sign with your picture,
saying something like "DO NOT ACCEPT CHECKS FROM THIS HERO").

This surchage already existed, but since it was tied to active anger
(which typically causes a shopkeeper to quickly abandon their shop to
follow you) it was somewhat rare to see it in action.

I did not implement it here, but one possible further tweak might be to
clear the surcharge if the shopkeeper is pacified via taming magic
(which more-or-less magically brainwashes the target to feel positively
towards the hero) but not if you simply pay your debts.

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[cf4a194e86...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/cf4a194e86d53d57397f6de4febbea0de9c6ef57)
#### Wednesday 2022-11-30 00:38:43 by SkyratBot

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
## [red-creature/coSINE19](https://github.com/red-creature/coSINE19)@[54b475eb0b...](https://github.com/red-creature/coSINE19/commit/54b475eb0b3ff9913f6ec5de25243c899edcde7a)
#### Wednesday 2022-11-30 00:53:46 by Andromeda

removes annoying shit

sorry, i hate punpun and the portals

---
## [DeltaFire15/NSV13](https://github.com/DeltaFire15/NSV13)@[c31615bc74...](https://github.com/DeltaFire15/NSV13/commit/c31615bc74ce6ffba642cda2149cccf5dd74cf01)
#### Wednesday 2022-11-30 01:13:20 by DeltaFire

[insert maniacal laughing here]

Oh my god it's alive.
actual "fire slug go through map leave it, go to overmap" works now.
Particles, with variable lifetime and constant accel depending on amount of components. Soon: Acceleration depending on rail charge.
Prefab for testing.
Funny emag interaction.
Black Math Magic.

---
## [Jolly-66/JollyStation](https://github.com/Jolly-66/JollyStation)@[d27bbf8fe7...](https://github.com/Jolly-66/JollyStation/commit/d27bbf8fe7154af2184fd275814a9369167857b6)
#### Wednesday 2022-11-30 01:30:32 by Jolly

this is the most hacky way to do shit you have no fucking idea man (#3379)

---
## [tkellogg/dura](https://github.com/tkellogg/dura)@[4dc10296b1...](https://github.com/tkellogg/dura/commit/4dc10296b17dcae9ce273dc2cc6d517ef4617214)
#### Wednesday 2022-11-30 01:46:38 by Tim Kellogg

Optimization: Check file timestamps (#127)

The current version performs a `git commit` on every repository every 5
seconds. If nothing changed, it simply has no effect. This strategy is
eating up sometimes 10-20% of my CPU (on a poor dev machine), due to the
massive amount of hashing needed to commit so many repositories.

This change creates an optimization by tracking file changed timestamps
and comparing them against last commit timestamps. To do this, we have
to traverse all files in each repository, which `git commit` is doing
anyway. The big difference is that we only need to traverse to the inode
(directory) for the file timestamp entries, so it should be
significantly faster.

Considered design: It has been suggested to use the `notify` crate to be
notified of file changes. The trouble here was a global limit on file
descriptors that can be watched, so you can't watch all files. I
considered some machine learning appraches to guessing which files
should be watched, but abandoned the approach because every strategy I
could think of inolved a fallback to eactly what I'm doing here.

Considered design: Use SQLite to remember timestamps of every file. This
was needlessly complex because I only need to remember one timestamp -
the most recent one. And more important, the last dura commit already
stores it, so SQLite wasn't adding any value.

---
## [abmaschietto/parquetBaby](https://github.com/abmaschietto/parquetBaby)@[7540daf082...](https://github.com/abmaschietto/parquetBaby/commit/7540daf0823129b66a2377f2a35a1b7ca7faef4b)
#### Wednesday 2022-11-30 01:50:35 by abmaschietto

using fixed schema fuck you avro for not letting me use localdate and making me work so many extra hours

---
## [sinisterstuf/escort-mission](https://github.com/sinisterstuf/escort-mission)@[2b3fbed52f...](https://github.com/sinisterstuf/escort-mission/commit/2b3fbed52f5337b9867934a55deb20d99d9db463)
#### Wednesday 2022-11-30 02:12:21 by Siôn le Roux

Increase boss hitpoints back from 7 to 10

This is much more exciting because you don't have enough bullets and
need to reload in between.  The animation sequence for hitpoints goes
like:

- 3 hits for left arm
- 3 hits for right arm
- 2 hits for torso
- 1 hit for demon

Hmmm that adds up to 9, so something is not quite how I thought it was
anyway it seems to kinda work like this in the game.

---
## [KimberlyDetablan/app-dev](https://github.com/KimberlyDetablan/app-dev)@[29185f192f...](https://github.com/KimberlyDetablan/app-dev/commit/29185f192f85059d56ba58d7a84b5ac6abda827c)
#### Wednesday 2022-11-30 02:20:35 by KimberlyDetablan

Update README.md

Stranger Things is about a group of young friends who witness supernatural forces and secret government exploits. As they search for answers, the children unravel a series of extraordinary mysteries.
Jirisan is a South Korean television series a thrilling adventure. The drama is inspired by real-life stories as told by the rangers of JIrisan National Park.
Harry Potter series is a phenomenon because it introduced the world to an enormous and magical world that millions of people have dreamed of escaping into.
Descendants of the sun is a love story between Captain Yoo Shin Ji, Korean Special Forces, and Doctor Kang Mo Yeon, a surgeon at Haesung Hospital. Together they face danger in a war-torn country.
Vicenzo a Korean-Italian mafia lawyer gives a conglomerate a taste of its own medicine with a side of justice.
Alchemy of Souls a powerful sorceress in a blind woman's body encounters a man from a prestigious family, who wants her help to change his destiny.
All of us are dead, trapped students must escape their high school which has become ground zero for a zombie virus outbreak.
Fear Street is an American horror film series, with varying subgenres of horror, particularly the slasher and supernatural subgenres.

---
## [timothymtorres/tgstation](https://github.com/timothymtorres/tgstation)@[83f475aa7e...](https://github.com/timothymtorres/tgstation/commit/83f475aa7ec4290c6961f1f14c5da80f340989b8)
#### Wednesday 2022-11-30 02:23:25 by tralezab

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
## [SyncIt21/The-TG-Station-Fork](https://github.com/SyncIt21/The-TG-Station-Fork)@[35b5ac0c4e...](https://github.com/SyncIt21/The-TG-Station-Fork/commit/35b5ac0c4e6bbaf2adf277a7ea7a4a4eab89726b)
#### Wednesday 2022-11-30 03:20:01 by Fikou

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
## [Nightingale1997/Historical-Flavor-Expansion](https://github.com/Nightingale1997/Historical-Flavor-Expansion)@[8c580f51dc...](https://github.com/Nightingale1997/Historical-Flavor-Expansion/commit/8c580f51dc0a7fdfb18c10c37c5fcc3c2e301bd7)
#### Wednesday 2022-11-30 03:22:40 by thatswede

added heavenly kingdom flav

created "taiping moralism" unique ideo, its in flavoured Ideologies txt. created hong xiuquan DNA file and character file for heavenly kingdom with IG and traits. i have no clue how to create a a new intrest group tho so you'll have to do that. just contact me and ill tell u what i think it should have Ideology wise

---
## [tbry3467/AKL-cleaning-roster-updated](https://github.com/tbry3467/AKL-cleaning-roster-updated)@[4dab37ea4d...](https://github.com/tbry3467/AKL-cleaning-roster-updated/commit/4dab37ea4d52386668ca6dcb43131bfaeb908ab7)
#### Wednesday 2022-11-30 03:24:07 by tbry3467

Commented Thoughts on How to Improve This Old-ish Program

Been a while since I've looked at this project. It's quite a bit ugly and inneficient compared to what I remember it being. I would start from scratch if I felt the need to re-code this. Commented are my thoughts on what to do differently

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[5252418df0...](https://github.com/tgstation/tgstation/commit/5252418df0ed4726c5bf2a9599f95befd0aca086)
#### Wednesday 2022-11-30 03:50:33 by Mothblocks

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
## [chandanagindi/basics-of-java](https://github.com/chandanagindi/basics-of-java)@[2406f0367a...](https://github.com/chandanagindi/basics-of-java/commit/2406f0367a463f74030185ba432170f86ffc4bc4)
#### Wednesday 2022-11-30 04:09:26 by chandanagindi

Create team flesh

A young man named Diffny leaves home to travel to California, to join the Team Flash. Although Diffny is not able to join this elite team immediately, he befriends the three most formidable members of the age: Joe, Ramsey and vixon and gets involved in affairs of the state and court.At that time, the Villan was planning to dethrone the king and to take the kingdom and to remove the Team Flash of the guard. Since the Villan has spies mixed with the local public , Diffny decides to send a message of his whereabouts to the team Flash in unique way.He gave a note to a boy which has the following message. I am at the midpoint of the line joining the farmhouse next to the palace and the light house. The Team Flash were puzzled. Can you help them find out the location of Diffny?Given the coordinates of the 2 places (x1,y1) and (x2,y2), write a program to find the location of Diffny.

---
## [CarpeDelirium/NuyenImproved](https://github.com/CarpeDelirium/NuyenImproved)@[35c0410e31...](https://github.com/CarpeDelirium/NuyenImproved/commit/35c0410e31cc9773b492b4ec7384f903ae863a00)
#### Wednesday 2022-11-30 04:21:06 by CarpeDelirium

Junkyard Jaw is F

Illicit combat modifications performed by unlicensed and unregistered barrens docs are a blight on our society!

The SFC along with Knight Errant, and our corporate manufacturing partners are committed to protecting you through policy to keep these hyper violent and unstable criminals off the streets and through cutting edge product offerings. Defend yourself legally today with an implanted firearm from any one of our licensed distribution and installation partners.

Quality you can trust.

---
## [Cutiekittypet/Tannhauser-Gate](https://github.com/Cutiekittypet/Tannhauser-Gate)@[317aea0435...](https://github.com/Cutiekittypet/Tannhauser-Gate/commit/317aea043510ee0c3591ff3a06fdffd360fdfc29)
#### Wednesday 2022-11-30 04:48:49 by Jolly

[FUCK] [NO GBP] Yeah, fixes something in NuInterlink(?) (#17544)

fucking GODDAMNIT

---
## [radian-software/hypercast](https://github.com/radian-software/hypercast)@[e21ba94014...](https://github.com/radian-software/hypercast/commit/e21ba940148c8de88d604b83cb019a96299ffd3e)
#### Wednesday 2022-11-30 05:14:02 by Radon Rosborough

Make the dang thing work for Hulu

Hulu is a completely awful dumpster fire of sewage. I mean this in the
sense that if you imagine filling a dumpster with raw sewage and
adding enough gasoline that you can set it on fire, the sensory
experience will be much like trying to integrate with Hulu's
godawfully broken video player implementation that disregards every
possible notion of stability and compatibility to maximize the number
of ads they can force down people's throats.

And don't even get me started on Google's goddamn Manifest V3 making
it impossible to do any realistic userscripting, just so it's harder
for people to block ads. Fuck you, Google. What is it with advertising
companies and a complete disregard of anything resembling human
morality?

Following commits will hopefully be less angry now that the most awful
limitations imposed by uncaring-at-best, actively-malicious-at-worst
megacorporations have been more or less worked around.

---
## [Willardstation/tg-voidcrew](https://github.com/Willardstation/tg-voidcrew)@[bbb956d2a6...](https://github.com/Willardstation/tg-voidcrew/commit/bbb956d2a670656e546c35a09ec27295e5e06e94)
#### Wednesday 2022-11-30 05:44:17 by OrionTheFox

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
## [IftekharAnamArnob/life-story](https://github.com/IftekharAnamArnob/life-story)@[40e0da59ea...](https://github.com/IftekharAnamArnob/life-story/commit/40e0da59ea50bfcabe37f4d6307b92030489366f)
#### Wednesday 2022-11-30 05:49:51 by LoneWolf

My life story 

This commit holds my life cycle , my pain ,my misery .

---
## [20hr1a0460/practice](https://github.com/20hr1a0460/practice)@[b5ce3247e6...](https://github.com/20hr1a0460/practice/commit/b5ce3247e6168841c4116518fb17b81912405430)
#### Wednesday 2022-11-30 06:19:13 by 20hr1a0460

The Chronicles of Narnia

Four kids Peter,Susan,Edmond and Lucy travel through a wardrobe to the land of Narnia. Narnia is a fantasy world of magic with mythical beasts and talking animals.While exploring the land of narnia Lucy found Mr.Tumnus the two legged stag ,and she followed it, down a narrow path .She and Mr.Tumnus became friends and he offered a cup of coffee to Lucy in his small hut.It was time for Lucy to return to her family and so she bid good bye to Mr.Tumnus and while leaving Mr.Tumnus told that it is quite difficult to find the route back as it was already dark.He told her to see the trees while returning back and said that the first tree with two digits number will help her find the way and the way to go back to her home is the sum of digits of the tree and that numbered way will lead her to the tree next to the wardrobe where she can find the others.Lucy was already confused, so pls help her in finding the route to her home....

---
## [Pixel-2/android_frameworks_base](https://github.com/Pixel-2/android_frameworks_base)@[a5efdc7497...](https://github.com/Pixel-2/android_frameworks_base/commit/a5efdc7497374e5a5be0270ff23c93840c029ebf)
#### Wednesday 2022-11-30 06:56:58 by Kuba Wojciechowski

[SQUASHED] core: Blacklist pixel system feature from Google Photos

    We want to include the P21 experience flag to enable new features,
    however it seems like Google Photos uses it to decide whether to use the
    TPU tflite delegate. There doesn't seem to be any fallback so we need to
    make sure the feature is not exposed to the app so that a normal
    NNAPI/GPU delegate can be used instead.

    Test: Google Photos editor with PIXEL_2021_EXPERIENCE feature in product
    Signed-off-by: Kuba Wojciechowski <nullbytepl@gmail.com>
    Change-Id: I51a02f8347324c7a85f3136b802dce4cc4556ac5

commit 67eb31b3bb43d06fcc7f6fdb2f92eb486451cae6
Author: kondors1995 <normandija1945@gmail.com>
Date:   Thu Jun 9 17:39:25 2022 +0530

    Core: Extend Pixel experience Blacklist For Google Photos

    Turns out having these brakes Original quality backups.
    Since these indicate that the device is pixel 4 with in the turn brakes device spoofing as OG pixel

    Change-Id: I336facff7b55552f094997ade337656461a0ea1d

commit 508a99cde60b73dc3f1e843d569bca31def35988
Author: ReallySnow <reallysnow233@gmail.com>
Date:   Fri Dec 31 16:40:23 2021 +0800

    base: core: Blacklist Pixel 2017 and 2018 exclusive for Google Photos

    * In this way can use PixelPropsUtils to simulate the Pixel XL prop
      method to use the unlimited storage space of Google Photos
    * Thanks nullbytepl for the idea

    Change-Id: I92d472d319373d648365c8c63e301f1a915f8de9

commit aaf07f6ccc89c2747b97bc6dc2ee4cb7bd2c6727
Author: Akash Srivastava <akashniki@gmail.com>
Date:   Sat Aug 20 19:04:32 2022 +0700

    core: Pixel experience Blacklist For Google Photos for Android 13

    * See, in Android 13 pixel_experience_2022_midyear was added, which needs to be blacklisted aswell

    Change-Id: Id36d12afeda3cf6b39d01a0dbe7e3e9058659b8e

commit 9d6e5749a988c9051b1d47c11bb02daa7b1b36fd
Author: spezi77 <spezi7713@gmx.net>
Date:   Mon Jan 31 19:17:34 2022 +0100

    core: Rework the ph0t0s features blacklist

    * Moving the flags to an array feels more like a blacklist :P
    * Converted the flags into fully qualified package names, while at it

    Signed-off-by: spezi77 <spezi7713@gmx.net>
    Change-Id: I4b9e925fc0b8c01204564e18b9e9ee4c7d31c123

commit d7201c0cff326a6374e29aa79c6ce18828f96dc6
Author: Joey Huab <joey@evolution-x.org>
Date:   Tue Feb 15 17:32:11 2022 +0900

    core: Refactor Pixel features

    * Magic Eraser is wonky and hard to
      enable and all this mess isn't really worth
      the trouble so just stick to the older setup.

    * Default Pixel 5 spoof for Photos and only switch
      to Pixel XL when spoof is toggled.

    * We will try to bypass 2021 features and Raven
      props for non-Pixel 2021 devices as apps usage
      requires TPU.

    * Remove P21 experience system feature check

Change-Id: Iffae2ac87ce5428daaf6711414b86212814db7f2

---
## [vylryna/Terraria-Docs](https://github.com/vylryna/Terraria-Docs)@[37a4c85afb...](https://github.com/vylryna/Terraria-Docs/commit/37a4c85afb4508c96fe88129a0cbfa489f7aabfe)
#### Wednesday 2022-11-30 07:32:15 by xenona

HOLY SHIT that took a while sorry not everything is finished but I am for the day :P

---
## [Sonic121x/Skyrat-tg](https://github.com/Sonic121x/Skyrat-tg)@[932d25cdeb...](https://github.com/Sonic121x/Skyrat-tg/commit/932d25cdebb11b433f6faefa9f983a91e2011a67)
#### Wednesday 2022-11-30 07:54:04 by SkyratBot

[MIRROR] Mail sorting helper, and disposals fixes [MDB IGNORE] (#17683)

* Mail sorting helper, and disposals fixes (#70861)

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

* Mail sorting helper, and disposals fixes

* vr fixes

Co-authored-by: Profakos <profakos@gmail.com>
Co-authored-by: Jolly-66 <70232195+Jolly-66@users.noreply.github.com>

---
## [elfenbeinturm/Digital-Humanities1](https://github.com/elfenbeinturm/Digital-Humanities1)@[b513bec1c7...](https://github.com/elfenbeinturm/Digital-Humanities1/commit/b513bec1c77d6d43b2975edf379fd841c02504a1)
#### Wednesday 2022-11-30 08:17:34 by elfenbeinturm

add: list and worms

What the fuck did you just fucking say about me, you little bitch? I'll have you know I graduated top of my class in the Navy Seals, and I've been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I'm the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You're fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that's just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little "clever" comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn't, you didn't, and now you're paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You're fucking dead, kiddo.

---
## [ODRI-the-human/Vampire-Pooers](https://github.com/ODRI-the-human/Vampire-Pooers)@[d7c4ee75af...](https://github.com/ODRI-the-human/Vampire-Pooers/commit/d7c4ee75af94a2cff456635135cd20807def783e)
#### Wednesday 2022-11-30 08:19:03 by ODRI-the-human

the much anticipated POOPOO UPDATE!

Added the saw shot item. Reorganised a lot of the code in HPDamageDie so it's not as ugly, and collision/triggers work the same regarding dealing damage. All on-hit effects now have a method "RollOnHit", that rolls/applies its effect on hit - this was done so things like the sawshot can cause things like bleed procs despite, ya know, only hitting enemies one time. Shit like creep and orbitals now don't cause a specific cooldown thing in its victim's HPDamageDie, but rather tick every so often (the tick interval can be set from DealDamage, by default for bullets and the like it's 1)

---
## [lefevbre-organization/eShopOnContainers](https://github.com/lefevbre-organization/eShopOnContainers)@[2089ca104e...](https://github.com/lefevbre-organization/eShopOnContainers/commit/2089ca104e7923d47eac7ceea5cf82887122dd85)
#### Wednesday 2022-11-30 08:29:06 by jvalls-lef

{     "general_email": "Email",     "general_button_cancel": "Cancel",     "general_button_clean": "Clean up",     "general_button_save": "Save",     "general_button_update": "Update",     "general_button_download": "Download",     "general_button_new": "New",     "general_attachment": "Attach",     "general_close": "Close",     "general_button_refresh": "Refresh",     "general_button_ok": "Ok",     "general_delete": "Delete",     "general_button_yes": "Yes",     "general_button_no": "No",     "general_button_create": "Create",     "general_button_filter": "Filter",     "general_button_send": "Send",     "general_select_other": "Select another",     "general_adjust_size": "Adjust size",     "general_tags": "Name",     "general_title": "Title",     "general_states": "States",     "general_state": "State",     "general_share": "Publish on the portal:",     "general_shared": "Published document:",     "general_documentation": "Documentation",     "general_option_list": "List",     "general_invalid_file_type": "Invalid extension file.",     "general_adjust_size_image_title": "Adjust image sizes",     "general_size": "Size",     "general_error": "Error",     "general_date_modified": "Modification date",     "general_date_created": "Creation date",     "general_modified": "Modified",     "general_created": "Created",     "general_location": "Location",     "general_ascending": "Ascending",     "general_descending": "Descending",     "general_none": "Noe",     "general_permission": "Permision",     "general_error_notification": "The notification could not be delivered, please validate the email address",     "general_search": "Search",     "general_search_minimum": "Search (minimum 3 characters)",     "general_max_image_size": "Maximum size: 320x55",     "general_text_description": "Description",     "general_text_attach": "Attach document",     "general_text_attachs": "Attach documents",     "general_text_view": "Preview",     "general_text_clasification": "Classification",     "general_preview": "Preview",     "general_discard": "Discard",     "general_youtube": "Youtube",     "general_upload": "Upload",     "general_select_all": "Select all",     "general_order_by": "Sort",     "general_refresh": "Refresh",     "general_twitter": "Twitter",     "general_facebook": "Facebook",     "general_linkedin": "Linkedin",     "general_phone": "Phone",     "general_title_tab": "Tab title",     "general_business_name": "Business name",     "general_see_all": "See all",     "general_see": "View",     "general_all": "All",     "general_add": "Add",     "general_outbound_server": "Outbound Server",     "general_port": "Port",     "general_safe_connection": "Secure Connection",     "general_test_connection": "Test Connection",     "general_smtp_connection_success": "The connection configuration with the mail server is correct",     "general_smtp_connection_error": "Could not connect with the mail server. Verify that the connection data is correct.",     "general_close_preview": "Close preview",     "general_required_field": "This field is required.",     "general_settings": "Settings",     "general_logout": "Logout",     "general_name": "Name",     "general_last_name": "Last Name",     "general_sur_name1": "Last Name 1",     "general_sur_name2": "Last Name 2",     "general_description": "Description",     "general_client": "Client",     "general_client_of": "Client of",     "general_filter_date_from": "Date from",     "general_filter_date_to": "Date to",     "general_min_length_field": "The minimum length of this field is {param} characters.",     "general_max_length_field": "The maximum length of this field is {param} characters.",     "general_not_found": "Information vot found",     "general_default_value": "Default value",     "general_delete_error": "We are sorry, the deletion operation couldn't be completed.",     "general_error_message": "Sorry, the operation couldn't be completed.",     "general_success_message": "The operation has been successfully completed.",     "general_get_error_message": "We are sorry. The information could not be obtained.",     "general_search_placeholder": "Enter search",     "general_invalid_email": "Please enter a valid e-mail address.",     "general_invalid_number": "Please enter a valid number, for example (1.0, 2.0)",     "general_placeholder_input_file": "Upload or drag and drop the file",     "general_pagination_of": "of",     "general_pagination_pages": "pages",     "general_pagination_documents": "documents",     "general_translate": "Translate",     "general_language": "Language",     "general_translate_text": "Custom field name",     "general_attach_documents": "Attachments",     "general_save_change": "Save changes",     "general_spanish": "Spanish",     "general_english": "English",     "general_catalan": "Catalan",     "general_italian": "Italian",     "general_french": "French",     "general_basque": "Basque",     "general_customization": "Customization",     "general_request_info": "Request for information",     "general_no_have_contract_clint_link": "You have not purchased this product",     "general_no_show_message_again": "Do not display the message again",     "general_title_message": "Message",     "login_username": "User",     "login_password": "Password",     "login_required_user": "The user is required.",     "login_required_password": "The password is required.",     "login_forgot_password": "Forgot your password?",     "login_remember": "Remember",     "login_btn_session": "LOG IN",     "login_helper_need": "Need help?",     "login_contact_administrator": "Contact the task administrator",     "login_invalid_credentials": "Invalid credentials, please verify your user and password",     "login_information_data_personals": "Personal data processing information",     "login_information_data_personals_message": "The data controller is <strong>{{value}}</strong> and the purpose is to exchange information related to the service provided by the data controller with customers. The legitimacy of the treatment is based on the contractual relationship that unites the data controller with its clients. The processed data will not be subject to international transfers nor will they be shared with third parties unless there is again a legal obligation. Data protection rights can be exercised at the addresses provided in the Privacy Policy that are included at the bottom of this page, where you can also access more information on personal data protection.",     "login_social_reason": "Customer's company name",     "forgot_password_title": "I forgot my password",     "forgot_password_subtitle": "Enter your email address to receive instructions and set a new password",     "forgot_password_required_email": "Email address is required.",     "forgot_password_invalid_email": "Please, introduce a valid email address.",     "forgot_password_send_email": "Send email",     "forgot_password_success": "An email has been sent to {email}",     "forgot_password_error_reset_password": "It is not possible to reset the password for the data entered, please contact Customer Service",     "reset_password_title": "Reset password",     "set_password_title": "Set my password",     "reset_password_new_password": "New password",     "reset_password_confirm_new_password": "Confirm password",     "reset_password_invalid_lenght_password": "Password must be at least 8 characters",     "reset_password_invalid_match_password": "Password does not match",     "reset_password_save_password": "Save password",     "home_see_all": "SEE ALL",     "general_customizer_title": "General Customization",     "general_customizer_desc": "With the following customization options you can include your company's brand communication to all communications and external pages of the Customer Portal.",     "general_customizer_section_brand": "Branding and graphics",     "general_customizer_button_notification_preview": "Notification Preview",     "general_customizer_button_external_page_preview": "External Page Preview",     "general_customizer_label_logo": "Logo",     "general_customizer_label_color_logo": "Color Logo",     "general_customizer_label_white_logo": "White Logo",     "general_customizer_label_logo_footer": "Footer Logo",     "general_customizer_label_favicon": "Favicon",     "general_customizer_label_main_color": "Main Color",     "general_customizer_label_secondary_color": "Secondary Color",     "general_customizer_label_design_header_page": "Page Header Design",     "general_customizer_label_design_footer_page": "Page Footer Design",     "general_customizer_option_not_sync": "Do not synchronize",     "general_customizer_option_sync_auto": "Synchronize automatically",     "general_customizer_option_sync_manual": "Synchronize manually",     "general_customizer_label_sync_client": "Synchronize Client Link",     "general_customizer_option_bc_white_icon_main": "White background with icons in the main color",     "general_customizer_option_bc_white_icon_black": "White background with black icons",     "general_customizer_option_bc_main_icon_white": "Main color background with white icons",     "general_customizer_option_bc_main_icon_black": "Main color background with black icons",     "general_customizer_section_social_networks": "Social Networks and Information on Footer",     "general_customizer_show_logo_footer": "Show logo on footer",     "general_customizer_show_automatic_notify": "Show automatic communications",     "general_customizer_success_message": "The configuration has been saved successfully.",     "general_customizer_default_language_required": "You must select a default language",     "general_customizer_language_required": "You must check at least one language",     "general_customizer_logo_required": "Logo required",     "general_customizer_logo_footer_required": "Footer logo required",     "general_customizer_white_logo_required": "White logo required",     "general_customizer_favicon_requried": "Favicon required",     "general_customizer_main_color_required": "Main color required",     "general_customizer_secondary_color_required": "Secondary color required",     "general_customizer_notification_text": "If you want all general communications from the Customer Portal to be sent to an email account different from the product's, activate the custom configuration and complete the requested fields.",     "general_customizer_notification_image_required": "Notification Image required",     "general_customizer_outbound_server_required": "Outbound server required",     "general_customizer_port_required": "Port required",     "general_customizer_user_required": "User required",     "general_customizer_password_required": "Password required",     "general_customizer_default_language": "Default language",     "general_customizer_other_languages": "Other languages",     "general_customizer_active_notification": "Automatic communications",     "general_customizer_email": "Email",     "general_customizer_add_tooltip": "Add new email fields",     "general_customizer_delete_tooltip": "Remove fields from email",     "general_column_action": "Actions",     "panel_table_type": "Type",     "panel_table_name": "Name",     "panel_table_file": "File",     "panel_table_height": "Creation Date",     "panel_table_date": "Modification Date",     "panel_table_public": "Public",     "general_column_public": "Public",     "general_customizer_section_send_email_settings": "Custom email to send communications",     "general_customizer_section_custom_email_notification": "Custom email to receive communications",     "general_config_sync_client_link": "Configuring Contact with Client Link",     "general_config_what_is_client_link": "What is Client Link?",     "general_customizer_label_notification_img": "Image for Notification",     "general_customizer_activate_custom_email": "Activate custom email",     "general_customizer_preview_badge_message": "Centinela Compliance Penal",     "general_customizer_preview_implantation_message": "Implementation: Title",     "general_customizer_preview_notification_title": "Communication title",     "general_customizer_preivew_notification_body_text_1": "Dear ##Recipient Name##",     "general_customizer_preivew_notification_body_text_2": "Informative text to introduce the communication. highlights on bold the",     "general_customizer_preivew_notification_body_text_3": "##dynamic data##",     "general_customizer_preivew_notification_body_text_4": "that corresponds.",     "general_customizer_preview_direct_access": "Direct access",     "general_home": "Home",     "home_email_section_label": "Email",     "home_client_section_label": "Clients",     "home_client_section_tab_last_new_client": "Latest Clients Created ",     "home_document_section_tab_last_document_client": "Latest Documents Created",     "home_client_section_tab_last_movement": "Last Edits",     "home_search_all_site": "Search in all site",     "home_search_client": "Search Client",     "notification_title": "Notification",     "notifications_communication_title": "Communications",     "notification_communication_new": "New communication",     "notification_communication_create": "Create communication",     "notification_column_issue": "Subject",     "notification_column_start_date": "Date sent",     "notification_column_created_date": "Creation date",     "notification_column_end_date": "End date",     "notification_column_alert": "Alert",     "notification_title_add": "Add new communication",     "notification_alert_title_add": "Add new alert",     "notification_title_modify": "Modify communication",     "notification_title_alert_modify": "Modify Alert",     "notification_title_field": "Notification title",     "notification_receiver_field": "Receivers",     "notification_person_responsible_field": "Person in charge of communication",     "notification_date_title": "Notification date",     "notification_date_alert_title": "Alert date",     "notification_repeat_title": "Repeat",     "notification_subject": "Email subject",     "notification_create_alert": "Create Alert",     "notification_edit_alert": "Edit alert",     "notification_property": "Property",     "notification_detail": "Notification detail",     "notification_search": "Search communication",     "notification_comment": "Comment",     "notification_list_comment": "Comment",     "notification_drag": "Drag and drop your documents here",     "notification_explore_computer": "Explore your computer",     "notification_ask_delete_confirmation": "You are deleting a communication. Do you wish to continue?",     "notification_delete_confirmation": "The communication has been deleted correctly.",     "notification_detail_comment_confirmation": "You are going to delete this comment Do you want to continue?",     "notification_edit": "Edit communication",     "notification_delete": "Delete communication",     "notification_not_found": "Notifications not found",     "notification_name_communication": "Communication name",     "notification_preview_notification_body_text_1": "Dear Customer",     "notification_preview_notification_body_text_2": "We have sent you a new communication from our Portal. To access it, click on the following link:",     "notification_preview_notification_body_text_3": "Best regards.",     "clients_add_new_client": "Add new client",     "clients_edit_new_client": "Edit client",     "clients_name_column": "Name",     "clients_surname_column": "Last Name",     "clients_description_column": "Description",     "clients_number_id_column": "ID #",     "clients_email_column": "Email",     "clients_mobile_column": "Phone",     "clients_address_column": "Address",     "clients_city_column": "Province",     "clients_status_column": "Status",     "clients_edit_client": "Edit",     "clients_status_in_progress": "In progress",     "clients_status_completed": "Completed",     "clients_status_on_queue": "On queue",     "documents_new_folder": "New folder",     "documents_new_word": "New document",     "documents_new_new_excel": "New Excel sheet",     "documents_new_ppoint": "New PowerPoint presentation",     "documents_upload_document": "Attach document",     "documents_add_document_folder": "Add document to a folder",     "documents_add_document": "Add document",     "documents_classification": "Classified document",     "document_delete_selected": "Delete selected document",     "documents_paste": "Paste",     "documents_cut": "Cut",     "documents_copy": "Copy",     "documents_rename": "Rename",     "documents_delete": "Delete",     "documents_download": "Download",     "documents_deselect": "Deselect",     "documents_details": "Details",     "documents_open": "Open",     "documents_path": "Path",     "document_file_size_large": "File size is too large",     "document_detail_title": "Document properties",     "document_detail_field_name": "Document title",     "document_detail_field_version": "Version",     "document_detail_update": "Update document",     "document_permission_delete": "User {{value}} does not have permission to delete this file or folder",     "document_permission_rename": "User {{value}} does not have permission to rename this file or folder",     "document_permission_copy": "User {{value}} does not have permission to copy this file or folder",     "document_permission_move": "User {{value}} does not have permission to move this file or folder",     "document_permission_edit": "The user {{value}} does not have permission to edit this file",     "notify_detail_update": "Update communication",     "document_fail_upload": "File failed to upload",     "document_success_upload": "File uploaded successfully",     "document_contact_notifications": "Do you want to share the contacts of this client?",     "document_add_contacts": "Add contacts",     "document_contact_permissions": "Select the contacts that must have permission",     "documents_item_selection": "Item selection",     "documents_items_selection": "Items selection",     "documents_view_large_icons": "Large icons",     "documents_view_details": "View details",     "documents_header_folder": "Folder",     "documents_content_folder": "Enter your folder name",     "documents_content_rename": "Enter your new name",     "documents_header_rename_confirmation": "Name change confirmation",     "document_alert_download": "You have started downloading the files.",     "documents_content_rename_confirmation": "Sorry, the file extension can't be changed.",     "documents_header_delete": "Delete file",     "documents_content_delete": "Are you sure you want to delete this file?",     "documents_header_multiple_delete": "Delete multiple files",     "documents_content_multiple_delete": "Are you sure you want to delete these {0} files?",     "documents_header_folder_delete": "Delete folder",     "documents_content_folder_delete": "Are you sure you want to delete this folder?",     "documents_header_duplicate": "The file / folder exists",     "documents_content_duplicate": "{0} already exists. Do you want to rename and paste?",     "documents_header_upload": "Upload data",     "documents_validation_empty": "The file or folder name cannot be empty.",     "documents_validation_invalid": "The file or folder name {0} contains invalid characters. Please use a different name. Valid file or folder names cannot end with a period or space and cannot contain any of the following characters: \\ /: *? '<> |",     "documents_validation_folder_exists": "A file or folder with the name {0} already exists.",     "documents_validation_rename_exists": "Cannot rename {0} to {1}: destination already exists.",     "documents_folder_empty": "This folder is empty",     "documents_file_upload": "Drag files here to upload",     "documents_search_empty": "No results found",     "documents_search_key": "Try other keywords",     "documents_filter_key": "Try a different filter",     "documents_sub_folder_error": "The destination folder is the subfolder of the source folder.",     "documents_same_folder_error": "The destination folder is the same as the source folder.",     "documents_access_denied": "Access denied",     "documents_access_details": "You don't have permission to access this folder.",     "documents_header_retry": "The file already exists",     "documents_content_retry": "A file with this name already exists in this folder. What do you want to do?",     "documents_button_keep_both": "Keep both",     "documents_button_replace": "Replace",     "documents_button_skip": "Skip",     "documents_apply_all_label": "Do this for all current articles",     "documents_KB": "KB",     "documents_search_browser": "Select files on your computer",     "documents_success_upload_file": "The documents have been uploaded successfully",     "documents_access_message": "{0} is not accessible. You need authorization to take action {1}.",     "documents_network_error": "NetworkError: Failed to send to XMLHTTPRequest: Failed to load",     "documents_server_error": "ServerError: invalid response from",     "documents_not_found_client": "no information found for this customer",     "documents_document_public": "Remember that you can edit the details of the documents with right click.",     "documents_all_file": "All the files",     "document_publish_documents_portal": "Do you want to publish these documents on the portal?",     "document_publish_document_portal": "Do you want to publish this document on the portal?",     "documents_new_document_message_info": "Select a client, a folder and click again on the \"+New\" button",     "documents_unable_move_locked_folders": "Unable to move locked folders",     "documents_share_permission": "Share",     "Settings_custom_folder": "Custom folders",     "Settings_custom_fields": "Custom fields",     "Settings_calendar": "Calendar",     "Settings_document_status": "Document status",     "Settings_labels": "Classifications",     "custom_folder_client_list": "Client list",     "custom_folder_create_folder": "Create Folder",     "custom_folder_create_sub_folder": "Create Subfolder",     "custom_folder_root_folder": "Root folder",     "custom_folder_add_folder": "Add folder",     "custom_folder_add_subfolder": "Add subfolder",     "custom_folder_not_found": "Folder not found",     "custom_folder_new_folder": "New folder",     "custom_folder_edit_folder": "Edit folder",     "custom_folder_new_subfolder": "New subfolder",     "custom_folder_edit_subfolder": "Edit subfolder",     "custom_folder_delete_confirmation": "You are going to delete the folder or subfolder \"{folderName}\". Do you want to continue?.",     "custom_folder_delete_success": "Folder or subfolder \"{folderName}\" has been deleted successfully.",     "custom_folder_folder_create_success": "The folder has been created successfully",     "custom_folder_subfolder_create_success": "The subfolder has been created successfully",     "custom_folder_folder_name": "Folder name",     "custom_folder_subfolder_name": "Subfolder name",     "custom_folder_translation": "Translation",     "custom_folder_translate": "Translate custom folders",     "new_document_word_title": "New document",     "new_document_word_edit_title": "Edit document",     "new_document_excel_title": "New Excel document",     "new_document_ppoint_title": "New PowerPoint document",     "new_document_text_version": "Version",     "new_document_text_public": "Publish to client",     "new_document_title_public_documents": "Publish document",     "new_document_text_maximum_size": "Maximum size 50MB",     "new_document_text_maximum_size_download": "Download limit exceeded. Maximum size 200MB",     "new_document_text_maximum_size_upload": "The upload limit has been exceeded. Maximum size 50MB",     "custom_field_select_field": "Choose the type of fields that you need",     "custom_field_group_fields": "Group fields",     "custom_field_text_fields": "Text field",     "custom_field_textarea_field": "Text area",     "custom_field_number_fields": "Number",     "custom_field_currency_fields": "Currency",     "custom_field_simple_list_fields": "Simple selection list",     "custom_field_multiple_selection_list_fields": "Multiple selection list",     "custom_field_option_fields": "Option yes / no",     "custom_field_date_fields": "Date",     "custom_field_not_found_custom_fields": "No custom fields in Contacts of type Customer",     "custom_field_not_found_subtext_custom_fields": "Select and set up new form fields to record more information",     "custom_field_group_form_title_label": "Group title",     "custom_field_group_form_fields_label": "What fields are in the group?",     "custom_field_form_title_label": "Field Title",     "custom_field_choose_group": "Do you want to group this field?",     "custom_field_max_characters": "Maximum characters allowed",     "custom_field_one_hundred_allowed": "Maximum 100 characters",     "custom_field_three_hundred_allowed": "Max. 300 characters",     "custom_field_add_option": "Add option",     "custom_field_add_checkbox": "Add checkbox",     "custom_field_list_option": "List option",     "custom_feild_delete_field_confirmation": "You are going to delete the field \"{fieldName}\". Do you want to continue?.",     "custom_feild_delete_document_confirmation": "You are going to delete this document. Do you want to continue?",     "custom_feild_delete_document_success": "The document has been deleted successfully.",     "custom_feild_delete_field_success": "The field \"{fieldName}\" has been deleted successfully.",     "custom_feild_delete_comment_success": "The comment has been successfully deleted.",     "custom_feild_save_document_field_success": "Instructions have been sent successfully",     "custom_feild_send_document_success": "The changes have been sent successfully",     "custom_field_delete_error_message": "We are sorry, the deletion operation couldn't be completed.",     "custom_field_operation_error_message": "We are sorry, the current operation couldn't be completed.",     "custom_field_translate_title": "Translate custom fields",     "custom_field_translate_column_field": "Custom field name",     "custom_field_translate_column_translation": "Translation",     "custom_field_translate_title_field_group": "Group title",     "custom_field_translate_title_field": "Field title",     "state_title_new": "New document state",     "state_title_edit": "Edit document state",     "state_text_name": "State name",     "state_text_color": "Color",     "state_text_new_name": "New state name",     "state_text_new_color": "New Color",     "state_translate": "Translate document state",     "tag_text_new": "New Tag",     "tag_text_edit": "Edit Tag",     "tag_translate": "Translate tags",     "client_management_basic_data": "Basic Data",     "client_management_custom_data": "Custom Data",     "client_management_access": "Access",     "client_management_access_active": "Access activated",     "client_management_access_send": "Access sent",     "client_management_give_access": "Grant access",     "client_management_revoke_access": "Revoke access",     "client_management_resend_instruction_access": "Resend access instructions",     "client_management_instruction_sent_successfully": "Instructions have been sent successfully",     "client_management_yes_has_access": "With portal access",     "client_management_no_has_access": "No access",     "client_management_contact": "Contacts",     "client_management_contact_synchronize_data": "Do you want to synchronize the contact data with Client Link?",     "client_management_contact_error_synchronize": "Error when synchronizing Client Link",     "client_contact_email_exist": "The contact's email address already exists",     "client_management_contact_required": "You must add at least one contact",     "client_placeholder_upload_logo": "Upload or drag and drop the logo",     "client_management_field_name": "Company name",     "client_management_field_id": "Tax ID",     "client_management_field_contact_name": "Contact name",     "client_management_field_type_organization": "Type of organization",     "client_management_field_natural_person": "Individual",     "client_management_field_legal_person": "Legal entity",     "client_management_field_phone": "Phone",     "client_management_field_email": "Email",     "client_management_field_address": "Address",     "client_management_field_cp": "Postal Code",     "client_management_field_state": "City",     "client_management_field_city": "Province",     "client_management_created_success_msg": "Client has been successfully created!",     "client_management_updated_success_msg": "Client has been updated successfully!",     "client_management_error_msg": "Sorry, the operation could not be completed.",     "client_management_error_nif": "Tax ID is not valid, please enter a valid Tax ID.",     "client_management_duplicate_nif": "The client's Tax ID already exists",     "client_delete_confirmation": "You are going to delete the client \"{clientName}\". Do you want to continue?",     "client_delete_success": "The client \"{clientName}\" has been deleted successfully.",     "client_access_placeholder": "Through this section you can grant access to the Customer Portal. Your client will receive an email with a link that will allow them to create their access password. In the Portal your client will be able to consult the data you make public, files, invoices, proformas, provisions, etc.",     "client_check_access_placeholder": "The client already has access credentials to the portal",     "client_access_button_text": "Send access credentials",     "client_contact_add_new": "Add new contact",     "client_contact_update": "Update contact",     "client_contact_not_found": "Contacts not found",     "client_access_info_text": "Provide access for file sharing and communication from the portal",     "client_required_contact": "You must add at least one contact",     "document_not_found": "Documents not found",     "client_not_found": "Clients not found",     "client_contact_delete_confirmation": "You are going to delete the contact \"{contactName}\". Do you want to continue?.",     "client_contact_delete_success": "The contact \"{contactName}\" has been deleted successfully.",     "client_search_contact": "Search contact",     "results_search_all_title": "Results",     "results_search_all_close": "Close Results",     "results_search_clients_link": "Clients",     "results_search_contacts_link": "Contacts",     "results_search_documentation_link": "Documentation",     "results_search_notifications_link": "Notifications",     "results_search_filter_by": "Filter by",     "results_search_placeholder_clients": "Search on \"clients\"",     "results_search_placeholder_documentation": "Search on \"documentation\"",     "results_search_placeholder_notification": "Search on \"communication\"",     "results_search_placeholder_contacts": "Search in \"contacts\"",     "attach_form_selected_documents": "Selected Documents",     "attach_form_attach_document": "Attach document of \"{clientName}\"",     "attach_form_document_search": "Search document",     "tags_not_found": "Classifications not found",     "state_not_found": "State not found",     "tag_not_found": "Classification not found",     "cookies_accept_all": "Accept all cookies",     "cookies_config": "Cookie settings",     "cookies_body": "Basic and essential cookies are necessary to browse this website and receive the service offered through it, and therefore do not require consent. These cookies are intended solely to enable communication between the user's computer and the network and to provide a service that has been requested by the user.",     "calendar_calendars_sync": "Calendar synchronization",     "calendar_no_account": "There is no email account configured. Please add your account and refresh this screen at the end of the process.",     "calendar_config_account": "Set up account",     "calendar_refresh_screen": "Refresh screen if you have already set up the account",     "calendar_create_event": "Create event" }

AB#4693 Update English translations

---
## [DeepikaCS28/deepika](https://github.com/DeepikaCS28/deepika)@[c5263b157b...](https://github.com/DeepikaCS28/deepika/commit/c5263b157b0d1a25a1309bc7241c442e0cc109f1)
#### Wednesday 2022-11-30 09:05:01 by DeepikaCS28

Three Idiots

Ajay, Binoy and Chandru were very close friends at school. They were very good in Mathematics and they were the pet students of Emily Mam. Their gang was known as 3-idiots. Ajay, Binoy and Chandru live in the same locality. A new student Dinesh joins their class and he wanted to be friends with them. He asked Binoy about his house address. Binoy wanted to test Dinesh's mathematical skills. Binoy told Dinesh that his house is at the midpoint of the line joining Ajay's house and Chandru's house. Dinesh was puzzled. Can you help Dinesh out? Given the coordinates of the 2 end points of a line (x1,y1) and (x2,y2), write a program to find the midpoint of the line.

---
## [lessthnthree/Skyrat-tg](https://github.com/lessthnthree/Skyrat-tg)@[37b60d187d...](https://github.com/lessthnthree/Skyrat-tg/commit/37b60d187daa6b8c8f2c2623dbf49555774a90aa)
#### Wednesday 2022-11-30 11:16:09 by SkyratBot

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
## [Thunder12345/tgstation](https://github.com/Thunder12345/tgstation)@[03bc97ade5...](https://github.com/Thunder12345/tgstation/commit/03bc97ade5a76f156229b946e38816ced97a0e30)
#### Wednesday 2022-11-30 11:57:39 by necromanceranne

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
## [Thunder12345/tgstation](https://github.com/Thunder12345/tgstation)@[a811adac74...](https://github.com/Thunder12345/tgstation/commit/a811adac74513494a620fae631da95d2626b1be7)
#### Wednesday 2022-11-30 11:57:39 by Epic

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
## [Thunder12345/tgstation](https://github.com/Thunder12345/tgstation)@[c185dffda0...](https://github.com/Thunder12345/tgstation/commit/c185dffda0cc30d8187fa1ba37e5784b8d630ba4)
#### Wednesday 2022-11-30 11:57:39 by Jacquerel

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
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[e7c8fed8e3...](https://github.com/odoo-dev/odoo/commit/e7c8fed8e373d7005c16c88d3a7bad6f425d13e5)
#### Wednesday 2022-11-30 12:45:18 by qsm-odoo

[FIX] website, *: allow to re-edit company team snippet images

*: web_editor

Since [1], it was not possible to edit a company team snippet image
anymore as soon as the page was saved once. Indeed that commit added
o_not_editable/contenteditable="false" on the parent column to make sure
no text can be added in that column and contenteditable="true" on the
images so that they are still editable (even though HTML-specs-wise
adding contenteditable="true" on images probably does not mean much as
images are self-closing tags, our editor understand that as the ability
to edit the image anyway). That contenteditable="true" part is however
removed when leaving edit mode... and was not restored upon entering
edit mode again.

This fixes the problems with an ugly patch. We'll review what to do in
master.

Funny enough, that bug was actually gone in 15.0... by mistake. A recent
bug fix actually reintroduced that isolated bug at [2] (by reintroducing
the fact that images in a non-editable environment are not possible to
edit). The 3 opened tickets this commit mentions were actually reported
for 15.0 immediately after that, while the 14.0 being broken about this
since the beginning apparently did not bother anyone.

[1]: https://github.com/odoo/odoo/commit/656cac1bf21c7c5a56aa569008aac58436c747fb
[2]: https://github.com/odoo/odoo/commit/e113bae04a64a8bd341a80736086ab7c25079dd3

opw-3031217
opw-3032482
opw-3035289

closes odoo/odoo#104156

Signed-off-by: Romain Derie (rde) <rde@odoo.com>

---
## [Priya-Varshney08/Java-Questions](https://github.com/Priya-Varshney08/Java-Questions)@[6a29cd07f6...](https://github.com/Priya-Varshney08/Java-Questions/commit/6a29cd07f6a66e9260d2335d1d5a6cf19211149e)
#### Wednesday 2022-11-30 13:18:30 by Priya Varshney

Pair of Roses

Deepak has a limited amount of money that he can spend on his girlfriend. So he decides to buy two roses for her. Since roses are of varying sizes, their prices are different. Deepak wishes to completely spend that fixed amount of money on buying roses for her.
As he wishes to spend all the money, he should choose a pair of roses whose prices when summed up are equal to the money that he has.
Help Deepak choose such a pair of roses for his girlfriend.

NOTE: If there are multiple solutions print the solution that minimizes the difference between the prices i and j. After each test case, you must print a blank line.

Input Format
The first line indicates the number of test cases T.
Then, in the next line, the number of available roses, N is given.
The next line will have N integers, representing the price of each rose, a rose that costs less than 1000001.
Then there is another line with an integer M, representing how much money Deepak has.
There is a blank line after each test case.

Constraints
1≤ T ≤100
2 ≤ N ≤ 10000
Price[i]<1000001

Output Format
For each test case, you must print the message: ‘Deepak should buy roses whose prices are i and j.’, where i and j are the prices of the roses whose sum is equal do M and i ≤ j. You can consider that it is always possible to find a solution. If there are multiple solutions print the solution that minimizes the difference between the prices i and j.

Sample Input
2
2
40 40
80

5
10 2 6 8 4
10
Sample Output
Deepak should buy roses whose prices are 40 and 40.
Deepak should buy roses whose prices are 4 and 6.
Explanation
Find two such kinds of price of roses which has sum up to equal to Deepak's Money.

---
## [guardian/gateway](https://github.com/guardian/gateway)@[b962f668b3...](https://github.com/guardian/gateway/commit/b962f668b35ac72f8f0a0aaace8ee180da8b816e)
#### Wednesday 2022-11-30 13:56:14 by Mahesh Makani

feat(okta): show onboarding flow for new social users

In Okta it is currently not possible to differentiate between new social users, and existing social users. This means that is was not possible to show social users the
onboarding flow.

However there is a case where a new social user differentiates form existing social users. This is to do with the email validated status. A new social user will be in
the `GuardianUser-EmailValidated` but their `emailValidated` field in their user profile will be `false` or `undefined`. So we have a remediation step in our callback to
handle this discrepency, and set the `emailValidated` flag should the user be in the `GuardianUser-EmailValidated` group. This was introduced in this commit:
https://github.com/guardian/gateway/commit/9af078165aa5add60b9e11bfe6731ff25badca6e

This means that the only time this discrepency will occur is for new social users, meaning at this point we can differentiate them from existing social users. This
allows us to use this functionality and set a flag to show the onboarding flow `authState.confirmationPage = consentPages[0].path;`. At any other point in time the user
will have both the `GuardianUser-EmailValidated` group and the `emailValidated` flag set, so they would not see the onboarding flow again.

A number of other options were considered for this functionality, but would involve other changes to the Okta configuration.

1. Using Okta groups
The first option we tried was to use Okta groups to do this. The theory was for new social users we assign them to a specific Okta group that we create, we can then
check this group, and if a user is in this group show then the onboarding flow. We can then remove them from this group so they're not shown the onboarding flow again.

However although this does work and new social users do see the Onboarding flow. I noticed that all social users started seeing the onboarding flow, whether they were
new users, existing users, or had even seen the onboarding flow before. Turns out Okta will always add all social users to the new group if they are not currently in it.
So even when removing the group from the user,  the next time they sign in with social, they get added to the group again, and they get shown the onboarding flow again.
Which wasn't ideal.

2. Using the account `created` timestamp on the user object.
This option was to use the `created` field in the user profile to determine if we should show the onboarding flow or not. This would involve checking this field
everytime a user went to the oauth callback endpoint, and if it's within a certain time period, say 1 minute, then to show the onboarding flow in that scenario.

However the account `created` field isn't returned by default in either the access or id token. So we'd either have to make an additional API call for every time a user
goes to the oauth callback endpoint, or to add a custom claim to add this field to the id token.

Using the API option would require making additional API calls, which we're trying to avoid, due to a limited number of API calls we're able to make to Okta. While
adding this field to the id token would require changes to the Okta terraform configuration to add this in, and would add an additional payload to what's only
effectively used once.

Also we'd have to chose the time period to check to avoid users seeing the onboarding flow multiple times if we set it too long, e.g. if they sign in immeditely after
registering on another browser/device, or not seeing the onboarding flow at all if we set it too short.

Hence the reason I went with the approach that we did.

---
## [openSUSE/systemd](https://github.com/openSUSE/systemd)@[48f40fbc8e...](https://github.com/openSUSE/systemd/commit/48f40fbc8e38c1a89a8a648ab23d687e5db2aacf)
#### Wednesday 2022-11-30 13:56:30 by Lennart Poettering

pid1: set SYSTEMD_NSS_DYNAMIC_BYPASS=1 env var for dbus-daemon

There's currently a deadlock between PID 1 and dbus-daemon: in some
cases dbus-daemon will do NSS lookups (which are blocking) at the same
time PID 1 synchronously blocks on some call to dbus-daemon. Let's break
that by setting SYSTEMD_NSS_DYNAMIC_BYPASS=1 env var for dbus-daemon,
which will disable synchronously blocking varlink calls from nss-systemd
to PID 1.

In the long run we should fix this differently: remove all synchronous
calls to dbus-daemon from PID 1. This is not trivial however: so far we
had the rule that synchronous calls from PID 1 to the dbus broker are OK
as long as they only go to interfaces implemented by the broke itself
rather than services reachable through it. Given that the relationship
between PID 1 and dbus is kinda special anyway, this was considered
acceptable for the sake of simplicity, since we quite often need
metadata about bus peers from the broker, and the asynchronous logic
would substantially complicate even the simplest method handlers.

This mostly reworks the existing code that sets SYSTEMD_NSS_BYPASS_BUS=
(which is a similar hack to deal with deadlocks between nss-systemd and
dbus-daemon itself) to set SYSTEMD_NSS_DYNAMIC_BYPASS=1 instead. No code
was checking SYSTEMD_NSS_BYPASS_BUS= anymore anyway, and it used to
solve a similar problem, hence it's an obvious piece of code to rework
like this.

Issue originally tracked down by Lukas Märdian. This patch is inspired
and closely based on his patch:

       https://github.com/systemd/systemd/pull/22038

Fixes: #15316
Co-authored-by: Lukas Märdian <slyon@ubuntu.com>
(cherry picked from commit de90700f36f2126528f7ce92df0b5b5d5e277558)

[fbui: adjust context]
[fbui: fixes bsc#1203857]

---
## [emillon/dune](https://github.com/emillon/dune)@[5f2128bb59...](https://github.com/emillon/dune/commit/5f2128bb593c163d5f4a957780e0dd05101a9dfe)
#### Wednesday 2022-11-30 14:27:05 by Etienne Millon

Add shell completion

This provides a shell completion mechanism for dune. This relies on the
bash completion API, which can be used with zsh as well.

The architecture is:

- `dune complete script` outputs a script to be sourced in the user's
  shell. It is comprised of a `_dune` function and the `complete -F
  _dune dune` command to register it. The `_dune` function can be used
  in cram tests to write natural-looking tests for this feature.
- this script calls `dune complete command` with the partial
  command-line. This internal command parses it to determine what the
  word being completed refers to: a command name, an argument name, or
  an argument value. The first two ones are part of the metadata
  `cmdliner` knows about; the last one is provided through a completion
  function that can be passed in one the `Arg` functions.
- the interface between `bash` and `dune complete command` is simple:
  it passes the command line and a position to complete at (this is
  necessary to encode the difference between `dune bui<tab>` and `dune
  build <tab>` for example), and reads an array from the output of the
  command.

The things I'm happy with:

- it is small!
- coverage is pretty good: command names, arguments (positional and
  optional, including optional arguments with optional names), and the
  `--` construct are supported. So, this is likely to improve the user
  experience already.
- it is easy to test through cram or unit tests (I chose the former).

Now, for the ugly bits...

- this effectively is a partial reimplementation of cmdliner inside
  `complete.ml`. If the exact parsing rules are different, it means that
  we can complete to something with different or wrong semantics.
- the vendored copy of cmdliner is patched to expose so that it is
  possible to use the private APIs. these two points need to be resolved
  before we can think about how to upstream this.
- some bits of the cmdliner API need to be modified to provide
  completion automatically. For example for things like `enum` it's easy
  to provide a completion function automatically.
- it is difficult to define the right API for the completion functions.
  `unit -> string list` is a first approximation but with some
  limitations. For example, getting a list of buildable targets needs to
  run under `Fiber`, but we can't pollute the API with it. Interestingly
  enough, algebraic effects seem like they would be an interesting
  solution for this.
- at the moment, we're not relying on the shell's completion helpers to
  complete things like filenames. To support this we would either need
  to implement that in OCaml, or extend the bash/dune interface so that
  the completion function could call `compgen -f` based on the dune
  output.
- as a way to tie the two previous points: if we wanted to complete
  `dune build dir/file<tab>`, it would be a lot more efficient to pass
  the prefix to the build system and let it compute just the targets
  that match this, rather than compute everything and filter it
  afterwards. So that prefix would need to appear in the completion API.

Signed-off-by: Etienne Millon <me@emillon.org>

---
## [RazorManager89/tgstation](https://github.com/RazorManager89/tgstation)@[3582aa77bb...](https://github.com/RazorManager89/tgstation/commit/3582aa77bb68d43c1ebbff9e06226bf3089cb07a)
#### Wednesday 2022-11-30 14:40:03 by LemonInTheDark

Slightly optimizes reagent splashing (#70709)

* Slightly optimizes reagent splashing

Ok so like, before, splashing a reagent performed a rudimentary
floodfill based off atmos connectivity.

This was really slow, because it did it using orange(), and repeated
orange()s to cut out JUST the rim, because we
needed to ensure things were ordered.

I've changed this to use floodfill. I've also moved some code that was
in a second loop into the first one, and replaced a repeated in check
with a single use of &

This is still not optimal for large ranges, because we filter by connectivity first
and THEN view, but it's faster for smaller ones.

BTW I'm also capping the max spread range at 40x40 tiles. If you want
more then 1600 you can rot in hell.

This takes the (uncapped range) cost of deconstructing a highcap tank
from 40 seconds to 0.16.

I hate this codebase

* god damn it

Co-authored-by: san7890 <the@san7890.com>

* whoops that's redundant

Co-authored-by: san7890 <the@san7890.com>

---
## [scaish/Abaddon](https://github.com/scaish/Abaddon)@[6c42446811...](https://github.com/scaish/Abaddon/commit/6c424468115306d2e2a85cf13663c7507885382c)
#### Wednesday 2022-11-30 15:34:51 by Nukechickenu64

fuck you paradise this my shit now idc if its cobblerigged to

---
## [oreillymedia/jupyter-book-to-htmlbook](https://github.com/oreillymedia/jupyter-book-to-htmlbook)@[2ed42d928b...](https://github.com/oreillymedia/jupyter-book-to-htmlbook/commit/2ed42d928bf7430897a93253e8449c404bd7c266)
#### Wednesday 2022-11-30 15:57:23 by Danny Elfanbuam

Refactor to better isolate `number_codeblock`

This is in part a way to get ahead for a future PR in which we'll make
numbering code blocks optional (per author request), but mostly the
logic for numbering code blocks was too entangled with if checks in the
process_code function, which is probably still a little too complex
anyway.

tl;dr: made number_codeblock stand more on its own

Slightly longer explanation:
* A hard thing to remember, but BeautifulSoup operations work "in
  place", so there is no need to really "return" the elements inside
  functions, so instead of returning the pre_block, we just modify it in
  place and return information about the cell numbering, which means we
  can...
* Move the input/output checks into the number_codeblock function
* This required the adjustment of a bunch of tests accordingly
* During which time I discovered a bug in one of the tests! Fixed that.
  Previously we were asserting that there was input when we should have
  been asserting there was output.
* Also, instead of checking the entire "result" (i.e., "chapter") in the
  tests, moved more towards asserting against _only_ the block in
  question, which is both more accurate, durable, and frankly better
  practice. Shame it took me so long to get there.

---
## [anirban-oss/computer-science-memories](https://github.com/anirban-oss/computer-science-memories)@[11c1f29d6b...](https://github.com/anirban-oss/computer-science-memories/commit/11c1f29d6be02aa91ce3b2b14e73d454a93bfebf)
#### Wednesday 2022-11-30 17:50:38 by anirban

missed yesterday for some work that i dont remember which is a very bad thing, i promise to not make this kind of silly fucking mistake again as journaling takes no time to do

---
## [casualspacestation14enjoyer/500toHCZ](https://github.com/casualspacestation14enjoyer/500toHCZ)@[8cb2fe21de...](https://github.com/casualspacestation14enjoyer/500toHCZ/commit/8cb2fe21de9298b9106adf47f0101583f253edd1)
#### Wednesday 2022-11-30 18:16:27 by f19_enjoyer

fixes random shit (just please i want to die this PR is so FUCKING SHIT)

---
## [dotnet/runtime](https://github.com/dotnet/runtime)@[1412ee7643...](https://github.com/dotnet/runtime/commit/1412ee76430e8c2d4319e418ab46bfb1af5b839f)
#### Wednesday 2022-11-30 18:29:58 by Vitek Karas

Enable basic Kept validation in NativeAOT running linker tests (#78828)

This implements basic Type and Method Kept attribute validation.
It adds a `KeptBy` property on all `KeptAttribute` which uses the same `ProducedBy` enum to specify exceptions for each target product. (Eventually after the source merge we should rename `ProducedBy` enum to just `Tool` or `Platform`, but it's not important and I didn't want to do it here as it would be a giant diff).

The validation is done by going over all `ConstructedEETypeNode` and `IMethodBodyNode` nodes in the final graph and remembers that list. Then it compares that list to the expected kept members as per the attributes in tests. There are some tweaks:
* Filters out all compiler added types/members
* Doesn't track generic instantiations - only remember definition
* If a method body is kept, then it behaves as if the type is also kept even though there's no `ConstructedEETypeNode` - this is technically wrong (since NativeAOT can remove the type if for example only static methods are used from it), but it would require major changes to the linker tests (since in IL this is a necessity). If we ever need precise validation of this, we would probably add a new attribute to check just for this.

I also copied all of the "other assemblies" kept validation code from ResultChecker (were it lives in linker) to AssemblyChecker where it will need to be to actually work (and where it should probably be anyway). That code is not used yet.

Left lot of TODO/commented out code in the AssemblyChecker - lots of other validation to enable eventually.

Fixed/adapted all of the tests which were already ported to NativeAOT to pass with this new validation.
Removed a test for unresolved members, since it actually fails NativeAOT compilation, so it doesn't test anything really.

One tiny product change:
Display names now consistently include all parent types when writing out nested type names. ILLink already does this and NativeAOT was a bit inconsistent. Since the display names are used only in diagnostics, this brings the diagnostics experience closer between the two tools. The added benefit is that we can use display names to compare members between Cecil and Internal.TypeSystem more precisely.

Co-authored-by: Tlakaelel Axayakatl Ceja <tlakaelel.ceja@microsoft.com>

---
## [peff/git](https://github.com/peff/git)@[fa967eb355...](https://github.com/peff/git/commit/fa967eb355a7b25358386bbdda53ce7a56cf3c4f)
#### Wednesday 2022-11-30 20:38:24 by Jeff King

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
## [peff/git](https://github.com/peff/git)@[27f66a83f3...](https://github.com/peff/git/commit/27f66a83f39a8375cb243a0b643946cc83dab3df)
#### Wednesday 2022-11-30 20:38:54 by Jeff King

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
## [andrewbaptist/cockroach](https://github.com/andrewbaptist/cockroach)@[1d04cec7c5...](https://github.com/andrewbaptist/cockroach/commit/1d04cec7c5f887d309e09b7b5a267d5269d86b5a)
#### Wednesday 2022-11-30 20:41:00 by craig[bot]

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
## [fizek/awesome-console-services](https://github.com/fizek/awesome-console-services)@[4b8f298fb2...](https://github.com/fizek/awesome-console-services/commit/4b8f298fb2b94b3c492da39ca43fcd2775907eea)
#### Wednesday 2022-11-30 21:27:06 by techie2000

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
## [hsurya0527/zulip](https://github.com/hsurya0527/zulip)@[23a776c144...](https://github.com/hsurya0527/zulip/commit/23a776c1448da18b906529e5951e24d8d58a7e81)
#### Wednesday 2022-11-30 21:42:04 by Mateusz Mandera

maybe_send_to_registration: Don't reuse pre-existing PreregistraionUser.

There was the following bug here:
1. Send an email invite to a user.
2. Have the user sign up via social auth without going through that
   invite, meaning either going via a multiuse invite link or just
   straight-up Sign up if the org permissions allow.

That resulted in the PreregistrationUser that got generated in step (1)
having 2 Confirmations tied to it - because maybe_send_to_registration
grabbed the object and created a new confirmation link for it. That is a
corrupted state, Confirmation is supposed to be unique.

One could try to do fancy things with checking whether a
PreregistrationUser already have a Confirmation link, but to avoid races
between ConfirmationEmailWorker and maybe_send_to_registration, this
would require taking locks and so on - which gets needlessly
complicated. It's simpler to not have them compete for the same object.

The point of the PreregistrationUser re-use in
maybe_send_to_registration is that if an admin invites a user, setting
their initial streams and role, it'd be an annoying experience if the
user ends up signing up not via the invite and those initial streams
streams etc. don't get set up. But to handle this, we can just copy the
relevant values from the pre-existing prereg_user, rather than re-using
the object itself.

---
## [Frank-py/Japy](https://github.com/Frank-py/Japy)@[2f044b1f3e...](https://github.com/Frank-py/Japy/commit/2f044b1f3e3f2ecd73368a9de7c53d98a86c36ef)
#### Wednesday 2022-11-30 21:44:07 by Daniel

I am actually so fucking pissed bro this is so fucking annoying nothing ever works this is so fucking shit fuck this shit please help

---
## [xhsu/AmxModX-Module-CPP23-Example](https://github.com/xhsu/AmxModX-Module-CPP23-Example)@[d2aae71ce6...](https://github.com/xhsu/AmxModX-Module-CPP23-Example/commit/d2aae71ce6e7e55aa565107b90858357114a7109)
#### Wednesday 2022-11-30 22:01:56 by xhsu

Default: Enable UTF-8 Support

- Enforce compile execution char set to be UTF-9
- Revert C++20 nasty, ugly, stupid and toxic paper P0482R6 by command line. (a.k.a. enforcing C++23 paper P2513R4	 regardless what /std you choose)
- Fvck you Tom mother-forking Honermann for the pain you caused since C++20

---
## [wor3dl/wor3dl](https://github.com/wor3dl/wor3dl)@[5b9e79255e...](https://github.com/wor3dl/wor3dl/commit/5b9e79255efc4aa35be2e7f6d14dcbdcc4dfbc9c)
#### Wednesday 2022-11-30 22:47:16 by wor3dl

rudimentary verification of words added (fuck your dictionaries)

---
## [BradleyMasters2022-23/MastersProject](https://github.com/BradleyMasters2022-23/MastersProject)@[daee1b2a99...](https://github.com/BradleyMasters2022-23/MastersProject/commit/daee1b2a99b8f0521cf0c17ba7a39ff7164f0d92)
#### Wednesday 2022-11-30 23:26:32 by BenSchu438

Quick bug fixes

FUCK YOU AUDIO SPAM BUG AND FUCK YOU DIO

---

