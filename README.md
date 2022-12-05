## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-12-04](docs/good-messages/2022/2022-12-04.md)


1,879,622 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,879,622 were push events containing 2,572,992 commit messages that amount to 152,978,667 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 43 messages:


## [laurens1995s/Grasscutter-1](https://github.com/laurens1995s/Grasscutter-1)@[88bc5c4c54...](https://github.com/laurens1995s/Grasscutter-1/commit/88bc5c4c54c1aadcdc6cc9a24c0f69d4bebce97c)
#### Sunday 2022-12-04 00:49:50 by Kimi

another translation patches because i fucked it up

i hate myself

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[661eaa985e...](https://github.com/tgstation/tgstation/commit/661eaa985e32056cc25f32bd81d9106861a4f9f8)
#### Sunday 2022-12-04 01:08:46 by MrMelbert

Important heretic spell rebalancing (#71620)

## About The Pull Request

Nerfs
- Furious steel cooldown: 30s -> 60 seconds (when ascended: 10s -> 30s)
- Furious steel: Now affected by antimagic
- Cleave cooldown: 40s -> 45s
- Cleave range: 9 tiles -> 4 tiles
- Cleave wound: Now has natural clotting, changing the amount of blood
loss from inf -> ~40%
- Blood siphon range: 9 tiles -> 6 tiles
- Void Pull: Now affected by antimagic
- Void Phase: Now affected by antimagic

Buffs
- Void Blast cooldown: 60s -> 30s

Other
- Rust Formation now has a "distinct" icon
- Void Blast now has a "distinct" icon

## Why It's Good For The Game

A lot of these spells were extremely oppressive, and made it pretty much
a joke to get away with anything.
They were no-brainer choices, and as a result no one really pathed into
anything else but these.

- Furious Steel: 
- Now that blade heretics have "realignment" in their repertoire, which
offers them another counter for being hit by disablers or batons, this
spell doesn't need to have such an insanely high uptime. The spell
should be used for initiating and obtaining the lead in a combat,
instead of having nigh-invulnerability for most periods.
- Additionally, antimagic protection was kind of missing, which was
partially an oversight of it not being a `/magic` projectile.
 
- Cleave:
- Cleave was by far the most absurd ability available bar none. This
spell was guaranteed death in 30 seconds if the target had no way to
stop the bloodflow immediately. AND it could be casted from across the
screen. This brings cleave's range into midrange between you and the
target, giving a lot more opportunity to be aware for the victim.
- Critical bleed wounds had a negative clotting rate, meaning that prior
you would bleed to 0% from cleave if you didn't stop it. Not very fun,
so with the default clotting rate it now stops at 60% blood flow -
enough to be lethal if untreated, but doesn't completely tap you out
   - **Alternatives**: 
      - Keep the no clotting, make it a pure melee / touch spell. 
      - Reduce the cooldown, make it a projectile
- Change it to be like a cool scythe attack that comes out of the caster
and does a sweep

- Blood Siphon: 
- This was primarily done to slot in better with Cleave's range
decrease, encouraging more close range combat between the two. Getting
point clicked from across the screen isn't fun.

- Void Pull and Phase:
- Largely done for consistency. These are spells which cause damage, so
anti-magic should stop the damage from the spells.

- Void Blast
- I have no idea why I made the cooldown so high on this, 1 minute made
it almost worthless.

TLDR: Instakill click spells from across the screen bad, invulnerability
bad

## Changelog

:cl: Melbert
balance: Heretic: Furious Steel's cooldown has been doubled (30s ->
60s), and abides by antimagic
balance: Heretic: Cleave's cooldown has increased by 5s, range has been
decreased to 4 tiles, and wound applied now has natural clotting
balance: Heretic: Blood Siphon's range has been decreased to 6 tiles
balance: Heretic: Void Pull and Phase abide by antimagic
balance: Heretic: Halved Void Blast's cooldown to 30s
qol: Heretic: Void Blast and Rust Formation now have distinct icons 
/:cl:

---
## [treuks/AoC-2022](https://github.com/treuks/AoC-2022)@[550ae4f1d2...](https://github.com/treuks/AoC-2022/commit/550ae4f1d2a79b2151c95c0d3fbb0b07b57c7558)
#### Sunday 2022-12-04 02:03:39 by Niko

Day 3 finished!!!!

I fucking hate the c++ iterators.
But it was worth it for le funny chemicals

---
## [fhgwright/git](https://github.com/fhgwright/git)@[f1c903debd...](https://github.com/fhgwright/git/commit/f1c903debdcbf6aaf8fd3abf222fa941b42d5d31)
#### Sunday 2022-12-04 02:35:27 by Ævar Arnfjörð Bjarmason

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
## [jnsrsmrn/App-dev](https://github.com/jnsrsmrn/App-dev)@[66ddfe7ad6...](https://github.com/jnsrsmrn/App-dev/commit/66ddfe7ad6ef903d2375865296586c2506cf1dfa)
#### Sunday 2022-12-04 02:40:58 by jnsrsmrn

Update README.md

Maxpein is a spunky provincial girl raised by her grandmother and uncle, after her mother died in Japan when she was 11 years old. Maxpein is surprised when her wealthy father, whom she recently discovered, offers to help pay for her grandmother's hospitalization. Out of gratitude, she agrees to her father's request to live with him and his family in Manila. Maxpein is treated as an unwelcome outsider at Benison International School where she stands up against Deib, the basketball varsity captain. Deib gets their entire batchmates to prank and bully Maxpein, but the more they engage in their game of cat-and-dog one-upmanship, the more Deib realizes that his goal to crush Maxpein's spirit has turned into a love crush for the girl he never thought he would even like. However, the return of the ghosts from their past and their various family problems threaten to ruin Max and Deib's blossoming and fragile romance.

---
## [JudeEdisonDicen/app-dev](https://github.com/JudeEdisonDicen/app-dev)@[2bc5ca3f1c...](https://github.com/JudeEdisonDicen/app-dev/commit/2bc5ca3f1c8f339b2caa5649149e54253c59ac4d)
#### Sunday 2022-12-04 02:53:55 by Jude Edison Dicen

This series are worth to watch.

Wednesday is the latest live-action adaptation of The Addams Family franchise coming to Netflix on November 23, 2022. As the director, Tim Burton wanted to make sure that this new series would not be mistaken for a remake or a reboot, but a spinoff that focuses on an entirely new chapter of Wednesday’s life as she grows into adulthood. The main members of the Addams Family are all well-known and beloved, based on the original characters by Charles Addams. However, this version of Wednesday is much older than when we last saw her as portrayed by Christina Ricci. Now that Wednesday is of high school age, there are bound to be new faces in her life, both friends and foes. Watch the official trailer below if you haven’t seen it yet! 
The plot revolves around Nanno, an enigmatic girl who transfers to different private schools in Thailand and exposes the students and faculty's stories of lies, secrets, and hypocrisy. Nanno on occasion lies to provoke others. She is revealed to be an immortal entity, punishing wrongdoers for their crimes and misdeeds. In Season 2, Nanno meets her match in newfound rival Yuri, who has a different, more revenge focused ideology and wants to take over Nanno's duties.

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[fcdf5d850c...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/fcdf5d850c47ac8c9c17045bb5a021d8283d3c0c)
#### Sunday 2022-12-04 03:45:20 by SkyratBot

[MIRROR] Psykers [MDB IGNORE] (#17825)

* Psykers (#71566)

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

Co-authored-by: tralezab <spamqetuo2@ gmail.com>
Co-authored-by: tralezab <40974010+tralezab@ users.noreply.github.com>
Co-authored-by: MrMelbert <51863163+MrMelbert@ users.noreply.github.com>

* Psykers

* commented out stuff is now in

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>
Co-authored-by: tralezab <spamqetuo2@ gmail.com>
Co-authored-by: tralezab <40974010+tralezab@ users.noreply.github.com>
Co-authored-by: MrMelbert <51863163+MrMelbert@ users.noreply.github.com>
Co-authored-by: John Doe <gamingskeleton3@gmail.com>

---
## [Nerev4r/Skyrat-tg](https://github.com/Nerev4r/Skyrat-tg)@[24ae11ad6f...](https://github.com/Nerev4r/Skyrat-tg/commit/24ae11ad6f6af9c0b6dab12986b95943f0cdf1f8)
#### Sunday 2022-12-04 04:21:30 by SkyratBot

[MIRROR] Adds a reagent injector component and BCI manipulators to all circuit labs [MDB IGNORE] (#17617)

* Adds a reagent injector component and BCI manipulators to all circuit labs (#71236)

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

Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>

* Adds a reagent injector component and BCI manipulators to all circuit labs

Co-authored-by: RikuTheKiller <88713943+RikuTheKiller@users.noreply.github.com>
Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>
Co-authored-by: Paxilmaniac <paxilmaniac@gmail.com>

---
## [queercpu/script](https://github.com/queercpu/script)@[ff2fad4817...](https://github.com/queercpu/script/commit/ff2fad48171fda7bf74f7be6fa6eec077fa493c3)
#### Sunday 2022-12-04 04:25:52 by home.cpu

1billion the anatomy of broken dreams has progressed quite far... internally and externally... i did some writing this morning by hand thats not transcribed...ive mostly been brainstorming and crystallizing the ship...  there are some rules im still trying to be strict about, saying NO, to things like combat missions on the ship(excuse to squeeze in war scenes) i could possibly do those without showing a single person being shot, could be any variety of things, the goal for me is not to showcase world building immersive shit or like depth of a universe my goal is to always test the girls and get them interacting and talking, its a character drama I think at heart or its going to be...

---
## [LemonInTheDark/tgstation](https://github.com/LemonInTheDark/tgstation)@[a753229ee2...](https://github.com/LemonInTheDark/tgstation/commit/a753229ee2541e32164772f05330669d3c6b75d8)
#### Sunday 2022-12-04 05:13:51 by GoldenAlpharex

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
## [aswild/meta-wild-common](https://github.com/aswild/meta-wild-common)@[c42b150064...](https://github.com/aswild/meta-wild-common/commit/c42b150064ff76698634086035213e4d9c6b6440)
#### Sunday 2022-12-04 05:16:05 by Allen Wild

langdale: update rust recipes

oe-core now basically includes meta-rust, and meta-rust-bin broke, so
update things to work with the new system. It's like 30+ more minutes of
build time to bootstrap LLVM and rustc, but at least it's cached and
it's nicer to be official. Maybe maybe-rust-bin will get fixed and I can
add it back in.

However, I need some workarounds for the built-in Rust support, mainly
that it's expected that we make recipes for every single dependency
(using cargo-bitbake probably) and then crates.io is ignored. That's
cool and all for reproducibility, but a massive maintenance headache
that I want no part of.

Wrap the common Rust changes I want in cargo-wild.bbclass and use that
form my recipes.

---
## [zedongh/cadence-client](https://github.com/zedongh/cadence-client)@[f5e0fd25e4...](https://github.com/zedongh/cadence-client/commit/f5e0fd25e4347c85b28dac87f51b532700455d2c)
#### Sunday 2022-12-04 05:37:50 by Steven L

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
## [TELIT-Hackathon/kosice2-crying_in_the_library](https://github.com/TELIT-Hackathon/kosice2-crying_in_the_library)@[9cea5b511f...](https://github.com/TELIT-Hackathon/kosice2-crying_in_the_library/commit/9cea5b511ff2e1707e5b5791cb43535cca8d2d77)
#### Sunday 2022-12-04 05:43:54 by kedar389

fixed everything , hate my life, thank u for reading

---
## [LongSleeves/sojourn-station](https://github.com/LongSleeves/sojourn-station)@[2290e12bed...](https://github.com/LongSleeves/sojourn-station/commit/2290e12bedf65b90c6cf5bf4a8d43fdb43335512)
#### Sunday 2022-12-04 06:04:08 by WilsonWeave

More beacon fiddling, part TWO!! WOW! !EGHGHG!!!  (#4128)

* Sheet Snatchers Offers!! Wow!!

Makes Lancer station offer 300 credits for up to 4 sheet snatchers at a time, considering Solnishko buys many more knives at a time, for 150 each, this seems more than fair considering the effort  and materials involved. Also ain't no one cooking food for trade offers chief.

Also makes Boris station offer 400 credits for up to 2  guild made advanced sheet snatchers at a time.  Having literally only one, extremely niche and rare to obtain offer as the only offer for a station is a really bad idea. Might not make the most sense for this station, but I'll consider replacing it with something more fitting. Eventually. But it works for now.

* More beacon fiddling, part TWO!! WOW! !EGHGHG!!!

Makes the religion stations buy meat, not as much per slab as Dionis does (given it's a tier one, roundstart station), but they can buy more at a time based on RNG.

Gives meat and all of it's sub-types a base price of 20 credits (hopefully)

Ghost-kitchen, AKA the VERY under utilized chef station now buys dinner trays. Slightly cheaper than knives. But I may change this to be more profitable than knives, albeit very restricted in number sold at a time, given it's one steel PLUS a tool-step. (Though honestly, I think I'm gonna tone back kitchen knife sales to 100, at LEAST, here soon.)

BUG FIX!!! Casino station no longer has an unlisted secret inventory, it now correctly displays, and gives a name to the extra tab. TODO! Make rigsuits more expensive overall, because you're paying a premium for a usually inferior rigsuit. (And voidsuits suits on that note). Oh and make it so the gems are properly sold for a million credits instead of twenty or two hundred million credits.

Casino station now buys cardboard boxes. For the meantime, it's plain cardboard boxes, while it's supposed to be a rebate, the boxes used for the Casino sales are a special subtype that include a LOT of non-box special objects. It works as an alternate favor method for now.

Brings a few more kitchen dishes up to closer par with roach-meat burgers. Vermouth pays FIVE HUNDRED credits for certain types of roach burgers roundstart. Bacon is a somewhat limited resource, and a pain to cook, so it should a LEAST be closer to roach meat. Effected stations are the trash refining station and the bluespace station.

---
## [OdatNurd/devember-2022](https://github.com/OdatNurd/devember-2022)@[95e330b3e5...](https://github.com/OdatNurd/devember-2022/commit/95e330b3e588eff0076d4a63ec879e6fe836f405)
#### Sunday 2022-12-04 07:57:59 by Terence Martin

Remove the minor curse that is NW.js

After some testing, we can only get our desired tray icon if we use an
older version of NW because tray icons in Linux haven't worked for 2
years at this point (at least on Slack/XFCE).

In addition, older versions don't have the same niceties for launching
node scripts, which is a bit of a bummer.

The largest letdown is that NW appears flakey as hell on Linux (again,
at least on my box) and routinely fails to display a window even though
it's actually running, which is the sad maker.

---
## [erjaschristine/app-dev](https://github.com/erjaschristine/app-dev)@[bb904638ea...](https://github.com/erjaschristine/app-dev/commit/bb904638ea4b582cdf5ce8bd3a86414e4214b5f5)
#### Sunday 2022-12-04 09:13:37 by erjaschristine

Update README.md

Follows Wednesday Addams' years as a student, when she attempts to master her emerging psychic ability, thwart and solve the mystery that embroiled her parents. Wednesday Addams misadventures as a student at Nevermore Academy: a very unique boarding school snuggled in deepest New England. Wednesday’s attempts to master her emerging psychic ability, thwart a monstrous killing spree that has terrorized the local town, and solve the supernatural mystery that embroiled her parents 25 years ago — all while navigating her new and very tangled relationships at Nevermore. After getting kicked out of eight schools in Five years, Willa aka Wednesday Adams is beginning a new chapter of her life at the academy, the two century old boarding school attended by her parents. However, Willa wants nothing to do with their alma mater and she’s already planning her escape. But this academy is like no other school she’s ever attended. It’s a school of outcasts with four main cliques, the Fangs (vampires) the Furs (werewolves), the Scales (sirens) and the Stoners. It is also a piece of the mystery that holds dark secrets about her family’s past.

---
## [Shaneee27/SamanApp-Dev](https://github.com/Shaneee27/SamanApp-Dev)@[c4ca0b222d...](https://github.com/Shaneee27/SamanApp-Dev/commit/c4ca0b222d235332ab13ca1c635685fa89016b8f)
#### Sunday 2022-12-04 09:24:26 by Shaneee27

Update README.md

Wednesday - What is the meaning of Wednesday Addams?
When the characters were adapted to the 1964 television series, Charles Addams gave her the name "Wednesday", based on the nursery rhyme line, "Wednesday's child is full of woe". The idea for the name was supplied by the actress and poet Joan Blake, an acquaintance of Addams.
Stranger Things - When a young boy vanishes, a small town uncovers a mystery involving secret experiments, terrifying supernatural forces and one strange little girl. Watch all you want. This nostalgic nod to '80s sci-fi and horror classics has earned dozens of Emmy nominations, including three for Outstanding Drama.
Enola Holmes - In the film, Enola travels to London to find her missing mother but ends up on a thrilling adventure, pairing up with a runaway lord as they attempt to solve a mystery that threatens the entire country. In addition to Brown, the film also stars Sam Claflin, Henry Cavill, and Helena Bonham Carter.
Elite - When three working-class teens enroll in an exclusive private school in Spain, the clash between them and the wealthy students leads to murder.

---
## [SyncIt21/The-TG-Station-Fork](https://github.com/SyncIt21/The-TG-Station-Fork)@[4fd404aa8f...](https://github.com/SyncIt21/The-TG-Station-Fork/commit/4fd404aa8f15480ad4c8585e65268a83c60b26e1)
#### Sunday 2022-12-04 10:02:48 by tralezab

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
## [SyncIt21/The-TG-Station-Fork](https://github.com/SyncIt21/The-TG-Station-Fork)@[9499a1542b...](https://github.com/SyncIt21/The-TG-Station-Fork/commit/9499a1542b156eb32efb25e0310b1fe7077caf5c)
#### Sunday 2022-12-04 10:02:48 by itseasytosee

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
## [SKS200/MDOLC-Multi-Dialect-Odia-Song-Lyric-Corpus-](https://github.com/SKS200/MDOLC-Multi-Dialect-Odia-Song-Lyric-Corpus-)@[40e121dcc3...](https://github.com/SKS200/MDOLC-Multi-Dialect-Odia-Song-Lyric-Corpus-/commit/40e121dcc320d188eda15e0d4d02149aa7914385)
#### Sunday 2022-12-04 10:04:02 by Shashikanta Sahoo

dev.txt

mor ne gute chhata mate magla chhata	spv
e malki dela malki danga	spv
gahata pari kale nemi pauna re muin pare dangabala	spv
jhia pakaa hulahuli re pua marare siti	ori
tu khushi re rahibu	ori
tui liza tor boyfriend kenta achhe kenta kenta	spv
lade gelhe manau thili tui thile mor nu tohfa	spv
hele kehi nai jani pyar ra asliyat	spv
gela hau thitin sapan dekhu thitin	spv
aalo chagali raago toh naali	ori
tate nei jibi rangei lunda lo	ori
hai topain khelana prema	ori
hae re soni nakhara tora laguchi pura jabar	ori
e e e e rasia	spv
dek tor eta gura muhuta phika padigala	spv
mor nu ghanti heu chu	spv
lagei delu kain mahani	spv
life mara thanduchu la	ori
kabira shayari tu lo insha-allah	ori
rasabati rasmalei chali jaisu anta halei	spv
hae tui phoon mate nai karu chu re	spv
karichhu mate diwaana	spv
mast disu chu	spv
to sathe lekha mora kete kahani	ori
tui gunehgar lo	spv
jamaru to katha hauni hajama	ori
are mann janu che manar katha rani lo	spv
sabu tv channel re hot khabara	ori
sahe sahe re sahe sahe re	ori
prema mora heijiba	ori
lage dekhuchi mun gote film	ori
katha mor sunuchhe nai	spv
habare mast cool	ori
prema aakashe hasuthila megha	ori
namkin to nakhara	ori
deija lo tor pata thikana	spv
tui aau mor jarurat	spv
nai dharan sate kehi	spv
luha dei chaligalu aakhire mora.	ori
aamar katha hetei kari	spv
chikina chora lagu chu piyara	spv
kete bam daauchhu heart re	ori
kahaku aau dekhena	ori
tor man ke churei kari	spv
suna re sahi nian paren	spv
hai tor bindiya churei nela mor nindiya	spv
mehndi laga hate tor neija	spv
dine nain dekhele nure diwana	spv
gotie faguna lage suna suna	ori
payejhal cham cham lagsi mahani atha	spv
i duniyar sabu lo	spv
mor jiban dia pyar ke galu bhuli	spv
lagila amiti sata nuha ea	ori
sweety aalo sweety	ori
amo gaan pari gann nahi	ori
nai paayein boli jani	spv
chuchupi aasilu mo shehjada	ori
madhura madhura to payi	ori
khasara mashara hauchi la	ori
hai re tumer maya jaale	spv
haa bhari tatala ha she niswasha chuare	ori
jaani gali tor chalana	spv
jahna anibu	ori
chiri delu phadi delu go mor love letara	spv
mun aaji kanduchhi jemiti	ori
chal aame aauthare dream tike dekhiba	ori
tahake ku tadpeu kesu	spv
impress hei kari	spv
mor dil bhitire jebbhe	spv
aakhire jebethu misscall delu	ori
dhum machale zero night	ori
tumo jibana tumo niswasa tumo arambha tumoro sesa	ori
chaligalu mate bhandei	ori
thare thare sapanare hauhili dekhare	ori
hele sabkar nu badhi kari mui	spv
kichi jani nahun	ori
kemiti chhuinbi re dhana tora range	ori
nain pade kahar najara hai	spv
tate dekhi aame helu pagala	spv
nai jibu bele mor dil ra heba bura hal	spv
bhija sakalara tu mo prema	spv
e jahn tike sunija	spv
bhet padma bali	spv
guri tor lachki chali kanli anta	spv
bhijiba ku haere	ori
tor paribar nu chadei anmi lo	spv
jan chorei nela o priya	ori
tahake besi bhal paisan	spv
ex-lover kainje bhabu chu	spv
tension vension tor laagi re suna	spv
tamer thane tumer nani	spv
han prema re prema re	ori
taro kamoli kamoli akhi	ori
tor i prem kahanir	spv
part two thi sorry kahi sapideli dil	spv
kuchbhi karega	ori
oraja mor jhumka	spv
duru dekhele re dhana	spv
lancha dei bayasara rakhi debi bata	ori
o janu mor dil thi	spv
kete karu nakhara	spv
tate fursat thi patami	spv
a mor pardesi babu i love you	spv
thumuru thumuru padare	ori
mate gf banei dela e jigar wala	spv
hae re chamki jau chhe	spv
pyar bali  figure tora  de chulubuli	ori
jhim jhim pani barsu thila	spv
nadi amar mahanadir jhare hira moti	spv
rahichhu tu rahithibu mo aakhire	ori
mate toh miligola sundari radha	ori
oda heigali premare toori	ori
hai chhati mor dulkila	spv
pagala premika sun	ori
re mor love letara	spv
maa luti nei thitha baula	spv
raba raba	ori
hnn tu mora champa kali,	ori
ethi sethi pada thau thau phula hau aba kanta hau	ori
rusi gale tui manabu	spv
e e e e rasia	spv
kane pindhichhu lo gathian jhalaka	spv
mahula jabani pahela china	spv
tui ta mor manar maina pakhe thile kainta  una	spv
o beby dil ra tajmahal thi	spv
chhati mor dulkila	spv
mate padheilu baby prema malika	ori
katha mor sunuchhe nai	spv
mu anamana firingi bauda	ori
rupar badale suna gahana	spv
are juri jhuri bhali maru thisi ga	spv
mate love karabar mauka delo dhana	spv
ja lo michei mana deli bujhei	ori
bayasa ma dauchu shari	ori
benir majhi khuchichha khirpini ho sanga gelhei rani	spv
bhuli jibi sabu kichi paigale puni kebe	ori
rajanigandha re tora,	ori
pyaar ra na thi tui gute kalank aau lo	spv
mui kana karmi tui bata lo	spv
kana bhul kali ete helu raag lepi delu dihen mor kalankar daagtui gunehgar re	spv
kemiti karibu re mate impress	ori
faguna ra hatare	ori
khojuchi lakhe srabana	ori
suni pakale nachi pakabu re	spv
hele tu baby kagaja bhabi fil ku dau chiri	ori
jangli ae mana mora jangli	ori
sidha sadha thisi e suna pila	spv
nan nana nana naine naine	spv
ho  mana thila aadha aadha	ori
patar khali lekhe udi bulu chhu	spv
jen bat ke jaisu tui se batke atki thisi mui	spv
tar aakhi buji dele mor rati suru hue re	spv
pachare na tate kete mana mo chahe	ori
maan heuche chanchania	spv
to sat chali pura latest fashion	ori
sampark ki pain kati delu	ori
dina sara bhabi rahi parena	ori
alpa thiba aa pheria tike pheriadairty..	ori
dine na dine tu paibu	ori
mote tk sikhei dei thitu	spv
tote paigala pare	ori
hae jebeki badhe ha eratira bayasha	ori
tumer badkha nani mor purna lover	spv
sedina thoo janili eka	ori
kariba swite papa	ori
to prema branabodha	ori
to ashique re dil bichara hajila	ori
sebe sebe lage bhari nijara	ori
jamaru tale padib nahin gotea boli mada	ori
bhala khali bhala	ori
aaji mu janili siye tu,siye tu siye tu	ori
love temperature a mor man mayuri han han tor lagi hei che matelo love fever	spv
kain tu motharu motharu nelu alvida	ori
rim jhim pani barsu thila re	spv
maa se mo maa, ho maa se mo maa	ori
pakhaku gale signal die prema ratha ta	ori
patli kamar halu tike jhar jhar jharu romance	ori
maruthiba siti	ori
e sajani lo	spv
kala premara majburian	ori
dil thila re banjara tui delu re sahara	spv
luki luki lo tate	spv
kahide dill ra katha nai kar mate aatha	spv
rati sara	ori
e duniyar aagade re mui kahuchhen khulam khulla	spv
chal hat chal hat	spv
call karuchhe mate mor pagili	spv
bhijei prema jale bhijei	ori
to rupa ku sajeila sagara ragini gayi	ori
mor darling dekhe lajelaje heuchhe	spv
i love u kahi de j sunmi ghae mui	spv
dil thi chidiya	spv
tui mor jiban sathi premi kale tui ete	spv
hele aamer lagi achhe ma ha puru	spv
tu nahu sobuta adha	ori
a hansi hansi mulki hansi	spv
a mor pardesi babu	spv
muhan muhin hele	ori
mor na tanka paisa kichi nai na	spv
tora hrudaya nahin	spv
kahaku aau chinhe na	ori
hey ae	spv
chataru mailu aakhi thara	ori
e luka chura prem khand madhura go machara tale	spv
he mor chhin udeai nelu re	spv
tor chahani mahani misa	spv
je kana hela re pila kana hela	spv
aaa mo pakha ku aaa thare dekha dei ja	ori
a chati sahiba nahi.	ori
he alga kahake dil debu	spv
mor ne gute chhata mate magla chhata	spv
chakhi chakhi tor kuanri chakhi lo	spv
to upare padiba lo mo niswas	ori
mate tor jarurat thila jebhe tui mate chadi thilu	spv
sabit kari delu nijke beimaan	spv
dhulki jibare dul dul dul	spv
a maain nai karba mate gali go go maain	spv
men rat se lekar shubha tak	ori
chumbak lekhe mate tani nelu	spv
to gala ra kalajai mahama hrudaya re	ori
hn tu kali kandibu semiti	ori
joubana chali jae	ori
to sathe chalichhi mora	ori
o my janam o my janam	ori
patar khali lekhe udi bulu chhu	spv
kahibu jadi uthei nebi rata rati to medha	ori
duru dekhele re dhana	spv
bhaav pirati sardha sathi	spv
baja bajei rani sajei	spv
dil ki ghadi re	ori
ore sawariya tu smruti ra gaan	ori
lage emiti haji kouthi	ori
jeibaku mote tike de ijajat	ori
kusna bali re kusna bali	spv
bhijei demi gura badan churei nemi man kain	spv
love pain shreedevi ta	ori
jhari re jhara buli aaeba aamar para	spv
pagala mujhe jani jani	ori
paudar ra kamal	spv
mori bato sra tumo smruti re	ori
jete bad sundri hele bi nai dekhu thili	spv
mast disu chu	spv
aaibu ki nia khabar pathei de lo	spv
thare thare harabat	ori
hasi hasi dekho udijaaye	ori
pura dana dan	spv
akhire akhire kahilu kichire bhujhi gali sabu mu	ori
feshion besi nain karbu	spv
aare aare aare mo rasia pila	spv
raati rati jaie biti	ori
chiri delu phadi delu	spv
sweet feel sweet thril daba jhumei	ori
khoji nua rasta	ori
jebe tate bhabe tu kichhi kahila pari mate subhe	ori
tor hasi tiker lagi	spv
e aa aa aa	spv
mor dil nei kusna dei tha	spv
nijathu haje kain mu aaji	ori
he sabu pila mankar	spv
to bina jete dina	ori
ho akhir sapan hesi tana bana	spv
tor bina mor dill aadha	spv
ee pila ee pila ee pila ma mote ta	spv
karei upare chatu	spv
a sunar makut pindhuthili go maain	spv
na re  na re na re hey	spv
tor ee thara nara	spv
nai kar rishmi	spv
khuda kasam harigali premare tora	ori
tuma pare premo mate debeni kehi sukha jete jaani goli tumaku paaie	ori
nua handsome te jiba tate mili	spv
tui lo geet ter lyrics hele	spv
aalo chuile tate current mare	spv
deu thisi kete gali	spv
ete kain to pain	ori
tor sabu katha ke mui mehesus karli	spv
sathi prema ki hela	ori
aalo mo baby cute tora photo	ori
tate bhabu bhabu tarali jae mu	ori
luki luki mate dekhu thisa tume	spv
gadami re pana patare	spv
dekhei delu mote tor tor aukaat	spv
rati sara sapana re kali tate intezar	spv
mori katha re mori gitare	ori
tu laguchu bhari sundari	ori
ae nai naire nai nai jai re mui	spv
hey baja baju thiba lo mauj masti heba	spv
rim jhim pani barsu thila	spv
tu mora har wafa	ori
dinare mate dekhei delu	ori
aa nachiba yaar	ori
tadpi maruchen mui	spv
mahanadir ujal pani dise jhalamala re dise jhalamala	spv
ho kete pila propose kale	spv
haye re mote chiri delare	ori
chinhi nahi kahu	ori
e nain delu khabara	spv
mate nazar nai pakaba	spv
hai re mo anar kali	ori
tor lagi mui sabu chhadili	spv
se meghare priya ku	ori
suna rangi mora suneli	spv
pichili jiba	spv
se badhei mora sosa	ori
nali nali sindura pindi galu palei	spv
tate sina dil ta khuli muin entry deli	spv
tate paibaku dine o priya re thila mora arman	spv
oye oyee oyee	ori
muskan pyari	ori
chahani re marideluni adhha	ori
tate na dekhile dina sare nahin	ori
sete besi kain khoju thaye	ori
ita tor thane mui challenge lagali	spv
ho bhal tate paebar saja aau kete paemi	spv
mor priyar dihe pahela chhita lagei de	spv
sunitha sunitha	spv
tate nei sathire nei	ori
dekhichhu` ta prema mora	ori
to pain awara mana sarfira	ori
ta hato bandhi deli apana panate muthaie tiki phula	ori
swartha sari gale kie ba kahara madhu	ori
tu kahile chando ku ani	ori
mitha mitha megha chhita	ori
tumo saru otho dhaare krushna chuda phute	ori
hebi mun colorful cover	ori
tui aau mor lovely gudia	spv
tor katha bhali aanuchhe mate go piratir jara	spv
laguchi jemiti deuchhu mate daki	ori
i miss you re	spv
jibana ta bina bhabi huena	ori
alga hei tui dekhei delu mote tor aukaat	spv
dhulki jibare dul dul dul	spv
hei paren mui malmalia	spv
tui mor sona mui tor kantabanjia babu	spv
tu eka lagu nijara ye duniya parayee	ori
puni thare hei jaa mu	ori
chali mo hata dhari sathi tiye hoyi	ori
aagore kando pachare haso.	ori
tui eka sundri	spv
da re aa re lahari jete	ori
ishara tui kari dele dunia thi jhan kain	spv
bhugli bhugli love kale badhia ae go	spv
hai re doli thi tate baseikari	spv
ishara sarmili tor ishara sharmili a mor suna sunku suna re	spv
fectri chhutire bell bajigale lage aaha	ori
life ra jhola nigidi gala ni	ori
aau kahake dill dele chhati jail jau	spv
chhati phata katha ke ta suni sate marijimi	spv
tame tame makhi chha	spv
first time kain feel hela	ori
aakhi dekhuthila kete swapna	ori
phul bagir jatne rakhi thili mahara hei dihen bhedi galu	spv
pas ke mate daku chhe	spv
khara ra kanla prutha upare nijaku lekhi nijaku lekhi	ori
otha tora madusala	ori
mote bhal pau chhe	spv
are handia bali mor kusuna balii	spv
dill more dei deli	spv
bada badmash tui lo	spv
nazarare chhuin jebe jaauchu chali	ori
khoje mun khoje mun	ori
pal pal mo palakare	ori
e jahn tike rahija	spv
hata to najara habani asara shunani to kahanee	spv
aakasho mate udijibaku hato tharilani	ori
bayasa ha ha bayasa kebe luchhi rahena,	ori
chalu chalu batare	ori
jebhe tiktok thi video tume chadla	spv
taa masta figara nela	ori
lagu kain mo painki ete jarori	ori
he bela ru ru	spv
pauni mun furushat	ori
ghare rahi nia hela ki	spv
tu mo ghruna dekhibu	ori
kea dela tate saragara sukha	ori
mun tamaku bhala paye,bhala paye,bhala paye	ori
kabat kune luki kandu thilu	spv
but ithhi b tui laguchhu pyaara	spv
o mor dil ke bekabu aji kari galu tui	spv
ha kahi dele tu	ori
tati jae sara rati	ori
kaen dusaguna karichhu lo kehinahi than dhari	spv
chalu thilu tike tike jhuntu thilu tike tike	ori
bata ghata tu mora premara jhanda	ori
a kansi ainla	spv
gotie karana lage suna suna	ori
budi basate nuaa dhangara	spv
mu bhala pauchhi	ori
nei tu mate manei	ori
chala bate phul bichhami	spv
gura gale rasi gute otha kari lali	spv
mor dil nei kusna dei tha	spv
mo duniata nua nua lage niara	ori
chahun jebe pheri pheri	ori
enta katha kahebu jadi pila re	spv
paudar ra kamal	spv
mu bhiji jaichi, bhiji jaichi	ori
ude aaji ude ta dehara mitha basna chariaade	ori
hai re kalu kaen mantara	spv
tor looki tor taki jadu karuchhe	spv
sunjara sunjara	ori
chali jau hasi dei	ori
khuji nuri	spv
aagaru ru laguthilo nihati boka	ori
baby tike eade ana au tu late karana	ori
pagala mun pura helinire kete dina ru mun khoji khoji	spv
chiri delu phadi delu	spv
sara rati basi basi vabe ta katha basi	ori
kahithile bahu karibe tate	ori
emiti tu chahni delu chahnanire mani nelu	ori
chatire galu rahitu jebe dhire dhire	ori
tor nua hero kain dela tate chadi	spv
gudar gudar pahen thi mor go	spv
anamika naika mu tu jajabar	ori
to premare padigali o priya	ori
kemiti tu rahu	ori
oh hello dirty fellow	ori
man ke chinhi tha man ke bujhei tha	spv
ame samalpuriaaaa	spv
ae tor sundri muhe scarp lagei	spv
ei mana thila, laja kula	ori
katha jebe delu deha mora chhuin	ori
hai tor bindiya churei nela mor nindiya	spv
to paain to pain	ori
he bujhi sabu ishara kain karuchu ete nakhara	ori
kanaa ta thare lo badi hajasi	spv
dekhu thibe tor sapan hele tor dream ra king muin	spv
dhuan dhuan to parchhaian	ori
to deha ra parchhai mo deha nakhara re	ori
bhal paesu bele mate ete rage nai kaha	spv
bujhibu tu jaudina pasteibu khali	ori
kashiq banei delu mate dhire dhire sathi	spv
aaina re kachha badale nahi re	ori
mo saponora tu rajohanshi	ori
mui bhi jiban thi kebhe hari nia	spv
jadugara kuhuka karidelu	ori
bajale thoda shor	ori
mui dewana i luv u re sajani	spv
mor dil ra dhadkan suni paka thare slowly dhire dhire	spv
tor kule suikari	spv
tu banijaa mo pain dilhi ka pani	ori
ghini thili mui jatra thane	spv
24 ghante khap khaana payi rakhdae	spv
aakhi ne kala kajala go maain	spv
tu mora majunu mu hebi to laila	spv
market khaila	spv
dil thila re banjara tui delu re sahara	spv
sawan barsha pani tike bhijei de	spv
rupa rangi tora balia jhuri lo	spv
kia lo tate michi michhi nela kolei	spv
mun tate kichhi kahini	ori
ja ja ja	spv
hele tor kaatil naina mate murder kari desi re	spv
ete kain to pain	ori
to bina gote muhurta jien mun parena	ori
dise sundara go dise sundara	spv
sara rati jeein baku	ori
to aasaraa	ori
kenu aelu aelu aelu aelu tui	spv
tumke saju chhe beuty palara go	spv
tor deewana akule dakuche lo	spv
hau disco aba break body heu tike shake	ori
nai dharan sate kehi	spv
lala la	spv
kahniki ete tu pauchu re bhala	ori
mor ladli mor pagali mor gelehi raani	spv
mane baaje harmaniya	ori
sajani re re a sajani re a sajani re sajani sajani sajani sajani	spv
area ta sara dhuli udiba	ori
dise sundara go dise sundara	spv
mu para tora cute munda	ori
chhatire hooka pakei delu	ori
tu mora mane rahilu	ori
tu mo love story	ori
ta akhire tike	ori
tui mor laagi madam sir bani galu re jebhe join kali tor prem pathsala	spv
mo chhatire dheu khele to prema ra juara	ori
love hba aamara five star rated	ori
panchami dine lo aame	spv
are bahana mara tor jana ta gala na	spv
tor maa bua ke chakma dei	spv
mo akhi nidaku	ori
bhaabanaara bandha baada jaae uchhuli	ori
hey shona hey shona, nida chore kalu tu	ori
jigar bala himat wala tor pyar thi mental hela	spv
mast disu chu	spv
jete nachile bhi nain hare muin	spv
smbalpuria	spv
padi gala bodhe sie na ken pakhe najara	spv
tu para mora cute munda	ori
ee ta prem parikhya kari de faisala	spv
kariba colourful	ori
to pakhare atakichhi samaya	ori
bhijei delu aare prema re	ori
gan gan nu sabu jete sahara	spv
mun dekhi dekhiki dekhi dekhiki	ori
tori payin lagu hela water cokkie rule	ori
muskan pyari	ori
katha nahin	ori
ita janitha nani	spv
prathama thara koli premo sauda	ori
thare thare jibanare	ori
aye priya tui daga diya alga hei	spv
e prema papa	ori
nai pade mui	spv
jani jani deigalu chatire kaha	spv
tate jiban dei chahun chhen suna	spv
mo matha ra naseeb tu	ori
tu mo ghruna dekhibu	ori
maja laage sei isarare	ori
impress heikari mui tor heikari	spv
mu aau nahni mora	ori
mor gudia rani	spv
he karei upare chatu	spv
katha jama sarunahin katha hele	ori
mor hei kari pase thile bhal ae go	spv
pahela dekhane mor dil luti nelu	spv
jalidelu jibana mora	ori
indradhanu ranga ani ta batare buni debi	ori
nai boile mui dhangara	spv
mor lover mast aaye re	spv
palithin jari go nai na sundiri	spv
mere mere jine ki wajah sirf tum ho	spv
he baby to cute face	ori
mu deyichi maana debi zibana magile mote tu	ori
amar sambalpuri ra tale	spv
dala dala bhal paile badhia ae go	spv
premara eki ranga lagila	ori
hai jhuma jhuma nua nisa re	ori
laje laje heu thila dil thi mor basi thila	spv
aji mora otha sara hasa kuanara	ori
baju thile dasara badya dhula ta	spv
sahi nai pare sajani	spv
choto bele aamo ghare ghele ghele	ori
udi udi kete suraj aankhir aage budi gala na	spv
pheribar bato bhulici haye	ori
janinathili prema ta tora thila ete michha	ori
ta die mari	ori
kemiti sahiba deha	ori
smile tara luni luni	ori
sabu janame mana khoje to prema chhuaa	ori
are dule rapper stage upre marsi jebe rappe	spv
o my sona only for you	spv
bewafa mor priya bewafa	spv
aaji bujhili mo prema pain	ori
jiethiba jae tate rakhibi mun saiti	ori
o suna rangi to chehera sunapatia	ori
katha fix hau thare	ori
mui tor aage pache thile	spv
chik chik chik tor bhujni gala	spv
najara re najara	ori
hetir lagi ta pher ghae thare mui	spv
tate dekhi aame helu pagala	spv
ee dil ta tadpi tadpi dhadku thisi	spv
tor chehera nirali	spv
mana nei tu khelidelu looo	ori
lage to chhuaa munjhe kiya huaa	ori
mana  mora chori hele hau pakhe akhe kiye thile tau	ori
tor pyar jenta mahu mitha hei ja tui bhamar atha	spv
kandhei kandhei kondhei lo,	ori
chahinle mun parunahin luchei	ori
tate bhabi lo nida laguni ratire	spv
tu nua sayari na nua kabita	ori
ekeda ekeda aara aara aara	ori
dress aau sadhi	ori
eyi akhi akhi re kahi bulu tu mote bhala pau	ori
toteto dekhile	ori
tu sarmili sayoni mo manara manini	ori
duniar agade e suna pila khel kari desi re	spv
kahi kari prem kahani	spv
juade mu jae aaji ta prema jaere chhuin	ori
ek gote ekela ghare	ori
nai gala jhumura	spv
tate rani kari rakhibi	ori
ore sawariya tu premara naann	ori
laguchhi aji tu thilu	ori
chitki jibu re dhangara pila	spv
e e e man rasia	spv
sie bahanaare deli jebe chuin	ori
ete bhala paigalu tu han tu hi tu	ori
tate diwana banauchhe	spv
duniare eka eka thili eka	ori
rahi nai delu ekela	spv
a pakhu mor chalijaisi	spv
arey hotare hota najaro hota	ori
sabu dina aathi maru chi	ori
bhari gulu guli jete sabui cuty billi	ori
baras jakar hasi khusi milan heba aaech bhai	spv
balia jhuri ke helana kala	spv
ai mo jibono thila nichatia choti ghro	ori
sabu raati jhareibi purnomi indu	ori
chhana chhana jaubana chahata chika	spv
tu mora jibanara nua thikana	ori
tike chahare dei chadhei lekhe jaisi udi udi	spv
mun tate bhala lagili	ori
to premare pai gala pare	ori
nija ku hajei paichhi tate mun	ori
aaji bhi mui takichhein re	spv
galu mate mate mate mate	spv
to premare maruchi mu aji	ori
udigala udajahaja	spv
han	spv
mora ei ki anubhutire	ori
tate bhabi neichhen mor dunian	spv
man ke mor manei kari	spv
mui hela na aatha ee pila ee pila	spv
first time gote jhia tu karilu pagala	ori
haye to hasa to hasa haye re mote chori kalare	ori
gadei gadei mali mo bopalo	ori
khoya khoya to madhosiyan	ori
abujha e mana mora hela re chagala	ori
sacha bandhan kana tui nain jani kehi nai chadan kaha ke jenta rupe thile v chinhi hei jaisi mahake	spv
tui au mor sona babu mui tor princess	spv
bata jama saru nahin kete bele	ori
pata thikana delo nani	spv
dekhu dekhu fida mun heli	ori
mu sammohini mu mu sammohini mu	ori
tor baat mui jugichhein dhana	spv
me tera hero tu heroine	ori
jani thili manata mo bhari niriha	spv
to premare pagala mu aji	ori
tor katha bhabu chen sapan mui dekhu chen	spv
a suru nani suri sali eeee	spv
baja baja	spv
jebethu asilu pakhare basilu mana kini nelu tu	ori
aakhi jhuruthisi tor chehera jhalamala lo	spv
nei nei kahebu bele fasei demi tate na	spv
rasabati dhana tui rasa mahul	spv
mitha mitha to chuanre laje marigali	ori
mora future darling	ori
to pain ei chati bhitare	ori
gudulu gudulu gumma	ori
deewana bani gali	spv
jaani paile nani tumer	spv
nai base kebhe kagaj phule ta	spv
luchile ei prema se kn luchi pare	ori
kete dina kaha emiti chaliba	ori
baulo phula buda chuinbo baula helani	ori
dina sara bhabi rahi parena	ori
di aakhire dui dharo	ori
bhijili to prema re	ori
kanje tui dure achu paske tui nai aasu chu	spv
rakhlunga dil mai chupa ke	spv
mayabati malika rani	spv
jhumuka moro kanoku chumi jhumei galani	ori
tor pyar mor dil thi	spv
aau kia	spv
badalo mate taani nebaku haato bulinali	ori
are handia bali mor kusuna bali	spv
makeup budget badhi gala	ori
dui nambar mal	spv
to bina mu rahi parena	ori
sei akhiru to baari heijaae	ori
tor lekhe sundara ga tor lekhe sundara	spv
chhidigala chhidi gala	ori
diwani bani gali gali gali	spv
mori premara aarambha khali tu..tu hi sesa	ori
baji gale re	spv
soilu aau ka sathi re	ori
hai re	spv
bewafi ta kana tor nu duniya sikhba lo	spv
first time gote jhia tu lagilu nijara	ori
tui gunehgar lo	spv
ea mano ku kolu kina bika	ori
mo jibana jalidei chhalana niaan re	ori
raji hele duniya agare hit heba ama story	ori
magile tora dil ra chabi	ori
jane ta beautiful bebo	ori
pata thikana delo nani	spv
tor prame mui andha lo	spv
hai tor kainli aata	spv
to bina gote muhurta jien mun parena	ori
amo kain ku thore jia dekhichi	ori
jai jai sambalpuri aaye jagat jita	spv
bhab biswas milan bhara	spv
mane mane tote bhala pae kete,	ori
e e e e rasia	spv
sabu kichhi aape mun bhuli jae	ori
amo kain ku nebo chorei	ori
miss kale missed call chali jauchi	ori
a mor dil thi tor naa ache re	spv
mor darling mor darling mor darling	spv
aajanate nei galu mo mana chorei	ori
darke lo darei kari	spv
hele duniar aagade hansbar sikhei desi	spv
heigala impress	ori
bhul bujhibuni mate pilatidinaru tate	ori
bindas e life tike colour bhariba	ori
paan supari khai re guri malkila	spv
lal mandara hai	spv
kenta katu che raet	spv
muin tor rasia bara	spv
gala jana padi	spv
hai tor nili nili akhi ke suna	spv
bhal paesu bele mate ete rage nai kaha	spv
to pain dil teli phone	ori
tor sweet hansi thi	spv
basanta aji barasa bele phulare khele doli	ori
cham cham	spv
chunmuk chunmuk payal	ori
dhire dhire mitha mitha daraja delu	ori
tu haan ki na kar, tori marzi	ori
dhol nishan tasha sange sambalpuri cap	spv
tate gf banei dela	spv
dada aaila side de	spv
hansi hansi sesh ke mui rasi jaai chen	spv
second time jebe muin tote dekhli	spv
achhen ta besi sundara	spv
tor familly mate banalu	spv
tate dekhiba payin	ori
chhati taku hurt kare hae tanka matka chali	ori
dehita sara dehita sara jhaale bhijigala	spv
mate bhala pai kain bhuligalu	ori
surya chandra tara badale nahi re	ori
nai nachi kahin jibu	spv
hai re samiyan dekhi chhina chaka	spv
udi udi kete suraj aankhir aage budi gala na	spv
tu mo ghruna dekhibu	ori
heu chhu go kete chakhi	spv
aa suna gharu bahria re	spv
tu jieba karana tu khusi re melana	ori
mote mari dela to ishara	ori
nili nili akhi kanlia chakhi tui ta hur huria dhuka hai re tui ta hur huria dhuka	spv
rupeli otha dhare to naa sabada re	ori
dil ke kala mor chori chori	spv
janeman kahan jayenge	spv
jadiba kali asiba e jhada	ori
sara jibana ku mana nela	ori
hatare to hata de	ori
right angle re rowdy	spv
tor paglami dekhi	spv
udi udi udi han jae mo kani	spv
to surma laga aakhi bada nasila	ori
khali kor sanam tui nia na	spv
tate nei mor jiban tate dekhi mor sapan	spv
mun khali to pain	ori
hato deli haate	ori
malka malka halka halka  e manata bhala  lage kahein baby	ori
kauthu aasichu	spv
ek dewaana tha	ori
akhitara nai	ori
tu sasughara galu kemiti lo	ori
sor paichen bolli	spv
tate khali dekhibaku akhi mage manjuri	ori
bhalapauthibi tate saata janma	ori
kain dinare dekhuchu suna sapana	ori
dill thi hesi halchal	spv
aji goli delu tu	ori
dhire dhire tu asilu	ori
oye oye o my raja jee	spv
heu thibu kala bala	spv
chagali fula pari mo deha basuthae	ori
close tk huantu ki karantu ki daya	ori
jebhe tiktok thi tiktok thi tiktok thi	spv
sat dau che tor nua saheli	spv
bayasa mahake bichhi chhe	spv
emiti semiti toka nuha ea	ori
mo dil deewana hei gala	ori
muhun sundar man nida pathar jani nain parli mui lo	spv
bale kari dhari thibu re nani	spv
mor dil nei kusna dei tha	spv
dhana to hritik style	ori
srabana re srabana	ori
ea mui bhale bunili chana	spv
bholi bhali dilwali lekhen laguchhu	spv
sabu jail demi,nije jail jimi,pagal hei jimi	spv
mate nei ja tu rangei lunda re	ori
romio raajare tu ta nirala	ori
bachhi anichi mu bachhi	ori
sate ki mu ghuri bule premara e swargare	ori
mor maa kahesi tike mui chagala	spv
bhul thile sorry	ori
tui bhi kari suna same to same	spv
jete to tharu mu dure jaye	ori
ho udi bulsi e man bhamara	spv
utki utki nachu thimi	spv
manguli rasta re jebe	ori
tate breakup karuchhe re dhana	spv
dhire dhire asi ajanate mora	ori
tor sange thimi sabu dina	spv
abujhata kichhi nahin	ori
tor sange jina sange mar na	spv
mana jhure mun janena	ori
aa nachma hai go rasia	spv
he kale kale sutre satre collage jaau thili	spv
hasi hasi mate kahide	ori
aare aare aare mo sunduri lela	spv
to prema ra chita mo mana sara	ori
chik chik chik tor bhujni gala	spv
jebethu ta sathe love heichi	ori
nida re tu tha mo sapane tu tha	ori
creazy karsi tar aankhi anokha number one beauty se mor sambalpuri quine	spv
prema ku kalu sauda	ori
love tijori tala khuli	spv
milky galare tora kiss gote dianti	ori
pachharu marilu tu chhuri	ori
endradhanu lekhe	spv
dekhu dekhu hela hangover	ori
mahu re odha odhani te pari	ori
love fever mate hei jaichhe	spv
badal tale tui kete lukuchhu hai	spv
harjit re matlab nahin life jienba full	ori
sadake gala matara	spv
tu mo ghruna dekhibu	ori

---
## [LemonInTheDark/Sandstorm-Station-13](https://github.com/LemonInTheDark/Sandstorm-Station-13)@[279542c739...](https://github.com/LemonInTheDark/Sandstorm-Station-13/commit/279542c739961b9b378c1e077b866b0091dffb0a)
#### Sunday 2022-12-04 10:59:11 by LemonInTheDark

Caches GetJobName. Fuck you

This code made me deeply upset, WHY IS IT RECURSIVE WHY WHY WHY WHY WHY WHY WHY WHY WHY WHY WHY

---
## [AvdanDOE/doebox](https://github.com/AvdanDOE/doebox)@[5c596508e1...](https://github.com/AvdanDOE/doebox/commit/5c596508e12f3b3616df22f5dfdafbb8504d334b)
#### Sunday 2022-12-04 11:00:10 by kerichdev

i fucking hate eww and how it handles images holy shit

---
## [maranxlee/PureInJava](https://github.com/maranxlee/PureInJava)@[a62dbe6153...](https://github.com/maranxlee/PureInJava/commit/a62dbe61539b53b564e11a8f06eee5c24081c594)
#### Sunday 2022-12-04 11:12:35 by Alvin Maranx, II ツ

Commit-a-thon (Chapter 2) (P1)

- VSCODE changed my bin folder - so the .pseudos are now in the lib folder
- Now commits from both my Surface Pro X and Desktop!
- Finally finished Q25 (using translation from my computer science book)
- Converted whole project to Gradle (kinda)
- Contradiction time " So yeah, when I feel like exploring the hundreds of Ideas I have left I will do somethin, somethin' Maybe tomorrow."
- Be tuned in for the next commit happenin' soon!
- 𝕞𝕒𝕣𝕒𝕟𝕩𝕝𝕖𝕖 | 𝕻𝖚𝖗𝖊𝕴𝖓𝕵𝖆𝖛𝖆 | ℭ𝔬𝔪𝔪𝔦𝔱-𝔞-𝔱𝔥𝔬𝔫 (Chapter 2)

---
## [Oferio/App-Dev](https://github.com/Oferio/App-Dev)@[97d582bf99...](https://github.com/Oferio/App-Dev/commit/97d582bf99a5a507342efefbfaf03d39bcb32808)
#### Sunday 2022-12-04 12:24:05 by Oferio

Update README.md

Fun facts why I love watching anime:
Anime is filled with storylines that will draw you in and keep you guessing. There are some scenes that will disturb you as much as any horror movie you have ever seen and there are other scenes that will make you weep for hours. Even though you aren't watching real people, you will experience real emotions.

---
## [JoeBidenWhatAreYouHiding/kx](https://github.com/JoeBidenWhatAreYouHiding/kx)@[c3e15f0d7a...](https://github.com/JoeBidenWhatAreYouHiding/kx/commit/c3e15f0d7a371119fdc4158d2fa0b217c0240b61)
#### Sunday 2022-12-04 12:50:25 by Nickay

holy fucking shit how can you fuck something so much up

---
## [AshleySuh1/ANT_COLONY](https://github.com/AshleySuh1/ANT_COLONY)@[1dfab7a27a...](https://github.com/AshleySuh1/ANT_COLONY/commit/1dfab7a27aa9c333b12c7c901c1caf9137cb0dc6)
#### Sunday 2022-12-04 12:53:03 by AshleySuh1

Update Ant_Simulation.m

EDITS
lines 11-24: I think this is a little bit neater? You can just input name of file you need. Also lets the TA input other maps we might not have.

lines 29&30: I think there should be more random angles to explore with sigma2 bc thats the ants without pheromones in their area. They need to explore more to find pheromones.

line 39: One of the requirements was to make the ant starting angle go around the entire colony in a circle, not the same angle. I'm not sure how to put the structures into an array better than this ;-;

Lines 48 and below: Ants with food follow blue, ants without food follow red. The current code makes it so the ants follow any and all pheromones. I tried to fix this by making two sets of array for each type of pheromone....

Line 66: So ant without food only looks at pheromone1 array which should only contain red pheromones, and vice versa

Line 77 & 85: Just corresponding to the T/F changes i made in CheckColonyProximity and CheckFoodProximity

Lines 97-110: Since there's two different sets, we don't need to check type anymore. I think at this point the second column for the pheromones and concentrations can be deleted? idk

Line 130: I just kinda repeat the while loop to go through red and blue separately
Line 190: Also just repeat the plotting thing to do red and blue separately

REQUIREMENTS
part of the requirement: There is supposed to be a high amount of blue pheromones at the colony and a high amount of red pheromones on each food. I attempted to add this in the pheromones and concentration arrays in the beginning indices, but it did not work for me ;;;;;; also, blue pheromone at colony is permanent but red pheromones at food should completely (w/out decay) disappear when the ant takes it right? ;;; can u maybe try to figure this out, I am not sure where to head from here. 

EFFICIENCY
-There was a "drawnow" command that can just change updates, so we don't have to use the clf function to remake the whole graph each frame. My brain kinda hurts rn and I'd like to figure out the pheromones on the colony and foods b4 attempting to clean anything tho...
-I think efficiency also increases when you make arrays with a set length than just []? For the arrays of pheromone and concentrations, we can predict max size. For pheromone1 it's going to be (1/deltaB) + 1 if rem(1,deltaB)>0. To be honest, I don't this will help much though.
-I'll look into this more later

---
## [NextWork123/platform_frameworks_base](https://github.com/NextWork123/platform_frameworks_base)@[48c0702200...](https://github.com/NextWork123/platform_frameworks_base/commit/48c07022004c4c93fb58c0e1357b6266269abe36)
#### Sunday 2022-12-04 13:33:32 by Joey Huab

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

---
## [MTandi/tgstation](https://github.com/MTandi/tgstation)@[3c187487b1...](https://github.com/MTandi/tgstation/commit/3c187487b1884040608ba23b0a89aa8b0176c2aa)
#### Sunday 2022-12-04 13:47:44 by MrMelbert

Renews a bunch of old roundend new reports that got lost. Plus, some roundend report QoL for cult and revs. (#71284)

## About The Pull Request

A few roundend reports got lost from moving to dynamic and other prs.
This PRs re-allows them to occur. Namely: "Wizard Killed" (lost in
dynamic), "Blob nuked" (lost in dynamic), "Cult escaped" (lost in cult
rework), and "Nuke Ops Victory" (station destroyed via nuke) (lost from,
what I can see, an oversight / accidental swap of report values).

Additionally, small roundend report QOL for cult: Removes antag datums
from spirit realm ghosts after being dusted, so they do not show up on
the report. And in reverse, heads of staff who were dusted / destroyed
in revolution rounds are now also shown in roundend reports.

## Why It's Good For The Game

Some of these reports are dead, which is is a shame because I think
they're cool and fun.

## Changelog

:cl: Melbert
qol: Successfully fending off a blob now has a cross station news report
again. More pressing reports will take priority over it, though.
qol: Successfully killing a wizard (and all of their apprentices) now
has a cross station news report again.
qol: If more than half of a cultist team manages to escape on the
shuttle (rather than summoning Nar'sie), they will send a unique cross
station news report. This is still a loss, by the way. Summon Nar'sie!
qol: Nuclear Operatives successfully nuking the station now has its
unique cross station news report again, and no longer uses the generic
"The station was nuked" report.
qol: Nuking the station to stop a blob infection now has a unique cross
station news report again. Good luck convincing admins to allow this.
qol: Cult ghosts from "Spirit Realm" no longer persist on the cult's
team after being desummoned, meaning they will not show up on roundend
report.
qol: Heads of staff will now always show up on revolution roundend
report - even if their body was fully destroyed.
/:cl:

---
## [MTandi/tgstation](https://github.com/MTandi/tgstation)@[03bc97ade5...](https://github.com/MTandi/tgstation/commit/03bc97ade5a76f156229b946e38816ced97a0e30)
#### Sunday 2022-12-04 14:11:06 by necromanceranne

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
## [Shimyytrov/Turret-Expansion](https://github.com/Shimyytrov/Turret-Expansion)@[9664fae315...](https://github.com/Shimyytrov/Turret-Expansion/commit/9664fae3158c7574f67e1366994a815cf9993ee9)
#### Sunday 2022-12-04 14:11:35 by YamiyoshinLevi

RICKROLL

Never gonna give you up,
Never gonna FUCK YOU DOWN

---
## [mhei/libmodbus](https://github.com/mhei/libmodbus)@[6f915d4215...](https://github.com/mhei/libmodbus/commit/6f915d4215c06be3c719761423d9b5e8aa3cb820)
#### Sunday 2022-12-04 14:18:13 by Stéphane Raimbault

Fix my so stupid fix for VD-1301 vulnerability

I can't believe I committed that copy/paste mistake.
Sorry Maor Vermucht and Or Peles, excepted naming your original
patch was OK.

Thank you Karl Palsson for your review.

---
## [SomeRandomOwl/Skyrat-tg](https://github.com/SomeRandomOwl/Skyrat-tg)@[460ab7adf5...](https://github.com/SomeRandomOwl/Skyrat-tg/commit/460ab7adf560856148d46233e3cde565d05354a4)
#### Sunday 2022-12-04 17:33:11 by SkyratBot

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
## [Dabger1/tgstation](https://github.com/Dabger1/tgstation)@[25d4afc869...](https://github.com/Dabger1/tgstation/commit/25d4afc869585373571da5ba4a77fb967ffdedfe)
#### Sunday 2022-12-04 17:47:33 by Iamgoofball

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
## [newstools/2022-sowetan-live](https://github.com/newstools/2022-sowetan-live)@[5fb2d33142...](https://github.com/newstools/2022-sowetan-live/commit/5fb2d3314268dc199dcbc3e9086bc8a6f1205fac)
#### Sunday 2022-12-04 17:48:17 by Billy Einkamerer

Created Text For URL [www.sowetanlive.co.za/news/south-africa/2022-12-04-kzn-traffic-cop-takes-his-life-after-shooting-girlfriend/]

---
## [TestyWritesCode3/custom_ffmpeg_compressor](https://github.com/TestyWritesCode3/custom_ffmpeg_compressor)@[8520509d82...](https://github.com/TestyWritesCode3/custom_ffmpeg_compressor/commit/8520509d8269073e3b4a8f5d37387be83223a36c)
#### Sunday 2022-12-04 19:45:36 by TetyLike3

Refactored the entire fucking thing holy shit
LogFile class added, makes logging easier ofc what did you want

---
## [Erol509/Skyrat-tg](https://github.com/Erol509/Skyrat-tg)@[bbaefcefeb...](https://github.com/Erol509/Skyrat-tg/commit/bbaefcefebf4200cf30456cfdb3cbfdb30af6c49)
#### Sunday 2022-12-04 20:35:16 by SkyratBot

[MIRROR] UpdatePaths Readme - Reforged [MDB IGNORE] (#17204)

* UpdatePaths Readme - Reforged (#70806)

* UpdatePaths Readme - Reforged

I'm a bit tired after typing for the last hour so apologies if some of this stuff is unreadable. Basically, I just took time to add a small blurb about UpdatePaths in MAPS_AND_AWAY_MISSIONS.md, as well as write out examples on how you can properly use every single function UpdatePaths might have. I'm probably missing something? I think I got everything though. Let me know if I should be consistent somehow, but I did deliberately choose different test-cases per example because it's nearly impossible to come up one "generic" fit-all situation that illustrates every possible use of UpdatePaths (to my small mind).

Anyways, hope this helps.

* i fucked up with the TGM format

augh

* UpdatePaths Readme - Reforged

Co-authored-by: san7890 <the@san7890.com>

---
## [sunamo/sunamo](https://github.com/sunamo/sunamo)@[1bb93a0b8d...](https://github.com/sunamo/sunamo/commit/1bb93a0b8d29231583553c476c907e18ae6f18b1)
#### Sunday 2022-12-04 21:05:34 by sunamo

I am a perfectionist but I know how to live life. When I'm working, it's 100%. When I'm with my friends, I put everything away and enjoy life. When I come home to my kids, it's pure joy and everything's worth it. Every time, I really focus 100 percent on one thing. I've learned how to juggle my life and I feel like now I have the perfect balance. - Monique Lhuillier

---
## [Offroaders123/NBTify](https://github.com/Offroaders123/NBTify)@[932cb49178...](https://github.com/Offroaders123/NBTify/commit/932cb49178518b4ea999ebff1a00c778fd87d405)
#### Sunday 2022-12-04 21:06:59 by Offroaders123

Smart Buffers!

Expanding off of yesterday's find and solution, this update make the library's buffer handling a bit smarter. Now that I know how `TypedArray`s interact with `ArrayBuffer`s a bit better, I made it so original `ArrayBuffer` input data can be used as much as possible. I didn't know how to work with the `byteOffset` and `byteLength` properties completely yet, and now I know how to work with them, so I'm using that to make new `TypedArray`s that reference the same underlying `ArrayBuffer` data directly, rather than duplicating certain sections of it just for reading purposes. I haven't visibly noticed any performance changes yet, but this will definitely help with more hefty files eventually, once I get to working with those. It sounds much more performant to read the data at a specific offset, rather than duplicating the same data just to have a certain section of it.

This brings back the internal `#data` property to the IO classes, as it makes the data access and calculations much easier. The `Uint8Array` itself now manages where you read the underlying data from, rather than the library manually applying that to the `DataView` and `.slice()` calls.

These changes are mostly to do with the reading side of the library, as the writing side won't have any custom `byteOffset` or `byteLength` properties set, because the library can manage the length of the buffer as it needs to, with `#accommodate()`.

After a little bit of Googling, and reading, this article covers how this works *very* nicely, and it helped confirm what I thought I now understand. Yay!
http://shockry.blogspot.com/2017/04/javascript-typed-arrays-slice-vs.html

Turns out I was using `.slice()` wrong too, at least in terms of performantly reading the data. `.subarray()` does the same things as before, but now even better because it uses the exact same data, rather than making a copy of the base `ArrayBuffer` between the indices!

Not in this update, but I'm going to look into it next, I want to redo/verify how the `#accommodate()` function works, just to see if I can make it more performant or straightforward too. I found this post which covers that other implemenetations tend to double the length of the buffer when it needs to expand, and that writing to the buffer performs "in O(1) amortized time". I'm no expert on O-notation yet, but I think that's the good one you want to have, hehe. I'm definitely curious what the different trade-offs are in terms of how often to expand the buffer (make a new one at x length), vs making the buffer larger to prevent having to expand it as often. It seems like from the description here (and thingking like O-notation) that having to reallocate less often is a nice sweet spot, even though it is more space. Definitely gonna look into that! :D
https://stackoverflow.com/questions/45898229/recommended-way-to-grow-a-buffer/46138231#46138231

Oh yeah, this is a semi revert/rework of the changes made in "IO Class State Properties". That's when I removed the internal `#data` properties in favor of just using the raw `ArrayBuffer` from the view instead. Now I have a `TypedArray` to access the data from the correct offsets, as expected!

I'm glad that the Bedrock Level file kinda broke this, because I've wanted to understand how this ArrayView setup has worked, since essentially the beginning of this whole project. I think I've understood the idea of what it was doing, the view vs the raw data itself, it was just the implementation of managing that kind of setup that was tricky for me. Now that I have a working version that manages it, it's super neat! `TypedArray`s are cool :)

---
## [sunamo/sunamo](https://github.com/sunamo/sunamo)@[d8f1381eb4...](https://github.com/sunamo/sunamo/commit/d8f1381eb4357138df2b512c214c8846445ff42e)
#### Sunday 2022-12-04 21:10:30 by sunamo

18156;My experience, with both my parents, is that grief has a lot of down, sad things, but I was also really emotionally raw, in the first year after each of them passed. Flowers smelled more intensely, my relationships were hotter, and I was more willing to risk. I was going for it a lot more. I was 'unsober' and I wasn't playing by my rules.;Mike Mills;experience

---
## [Zergspower/Skyrat-tg](https://github.com/Zergspower/Skyrat-tg)@[cf4a194e86...](https://github.com/Zergspower/Skyrat-tg/commit/cf4a194e86d53d57397f6de4febbea0de9c6ef57)
#### Sunday 2022-12-04 21:44:11 by SkyratBot

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
## [brianwang30/Grinder__bwang30_jli31_dbi30_byang30](https://github.com/brianwang30/Grinder__bwang30_jli31_dbi30_byang30)@[de71714255...](https://github.com/brianwang30/Grinder__bwang30_jli31_dbi30_byang30/commit/de71714255ebccc22f4897d6a07a4417cc9564bf)
#### Sunday 2022-12-04 22:16:07 by brianwang30

a few years ago when the judge slammed his gavel and said "You have committed arsonry", I had no idea what he waws talking about. Whenever i see the wwords "commit" nowadays I think about how I commited to this life, not one of burning down houses, but one of trying to help others clean up after their messes. And setting fire to thta one guy's stuff, he was annoying.

---
## [abhiram540/365-Days-Of-Python-Challenge](https://github.com/abhiram540/365-Days-Of-Python-Challenge)@[11eae6f525...](https://github.com/abhiram540/365-Days-Of-Python-Challenge/commit/11eae6f5256d314e51e85643cfc21b4498a8cba9)
#### Sunday 2022-12-04 22:40:09 by Abhiram Muktineni

Day 5: using the while loop

A junior magician has picked a secret number. He has hidden it in a variable named secret_number. He wants everyone who run his program to play the Guess the secret number game, and guess what number he has picked for them. Those who don't guess the number will be stuck in an endless loop forever! Unfortunately, he does not know how to complete the code.

Your task is to help the magician complete the code in the editor in such a way so that the code:

- will ask the user to enter an integer number;
- will use a while loop;
- will check whether the number entered by the user is the same as the number picked by the magician. If the number chosen by the user is different than the magician's secret number, the user should see the message "Ha ha! You're stuck in my loop!" and be prompted to enter a number again. If the number entered by the user matches the number picked by the magician, the number should be printed to the screen, and the magician should say the following words: "Well done, muggle! You are free now."

---
## [newstools/2022-daily-dispatch](https://github.com/newstools/2022-daily-dispatch)@[0851ed925d...](https://github.com/newstools/2022-daily-dispatch/commit/0851ed925d2b9902b99d301034d932e019cd2492)
#### Sunday 2022-12-04 23:40:52 by Billy Einkamerer

Created Text For URL [www.dispatchlive.co.za/news/2022-12-04-kzn-traffic-cop-takes-his-life-after-shooting-girlfriend/]

---

