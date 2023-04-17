## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-04-16](docs/good-messages/2023/2023-04-16.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,912,225 were push events containing 2,668,254 commit messages that amount to 143,684,241 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 49 messages:


## [filipsajdak/cppfront](https://github.com/filipsajdak/cppfront)@[10241cd6a5...](https://github.com/filipsajdak/cppfront/commit/10241cd6a59040d7408fda674bcdd918bd67c4e2)
#### Sunday 2023-04-16 00:00:58 by Herb Sutter

Checking in various improvements done in the last few evenings

Replace `store_as_base` with generated aggregate bases - better fix for #336, thanks @JohelEGP for the suggestion! This way we also don't need to obfuscate the name anywhere beyond the constructor(s), as the right member object name just enters the class's scope

If the user didn't write a constructor, provide a default constructor

If the user didn't write a 'that' constructor, suppress Cpp1's compiler-generated copying and assignment

Clean up emission of the just-mentioned generated/=deleted constructors, more naturally line up inside the class body following the indentation for other members that the original source code uses

Rename file `load.h` to `io.h` (`file.h` was another candidate), just because it has been bothering me for a year now that except for that one file all the headers were in natural alphabetical order by compilation phase... as of this commit we now have them all in alpha order and phase order: common.h -> io.h -> lex.h -> parse.h -> [*] -> sema.h -> cppfront.h

    [*] coming next here: reflect.h, which will also be in both alpha order and compilation order

Guard `out.construct` with `if constexpr` in case the type is not copy assignable and that path is never requested

Rename `cpp2::error` to `cpp2::error_entry` to quiet a new(? why?) GCC message about shadowing the former name with `parser::error`... I get why the warning is there, but this is a slightly annoying warning to have to satisfy just to compile high-warning-clean on GCC... oh well

Change semantics of emitting `.h2` files: In `-p` pure mode do the existing split of phases 0 and 1 into `.h` and phase 2 into a separate `.hpp`, but in mixed mode put all phases into the `.h`

---
## [sqnztb/Skyrat-tg](https://github.com/sqnztb/Skyrat-tg)@[60d2d2ee1a...](https://github.com/sqnztb/Skyrat-tg/commit/60d2d2ee1ae4f7a3c8c93e14fdbd6c210a45cf04)
#### Sunday 2023-04-16 00:18:43 by SkyratBot

[MIRROR] Optimizes some gas_mixture procs, Optimizes pipeline processing significantly by 33% [MDB IGNORE] (#20118)

* Optimizes some gas_mixture procs, Optimizes pipeline processing significantly by 33% (#74233)

## About The Pull Request
It is faster to operate on a gas list, especially if cached, then it is
to operate on a datum.
Doing this cause I'm seeing cost in merge() post #74230

Hits on a few other important places too. self_breakdown and such. Worth
it IMO

Could in theory go further by caching the global list. I'm tempted I
admit but it needs profiling first and it's late

EDIT: I have not slept, and have gone tooo far

[Micros /gas_mixture/copy and copy_from, adds a new proc to handle
copying with a ratio,
copy_from_ratio](https://github.com/tgstation/tgstation/pull/74233/commits/91da0003daa9485962525d3e6bc9170a4c09876b)

[91da000](https://github.com/tgstation/tgstation/pull/74233/commits/91da0003daa9485962525d3e6bc9170a4c09876b)

The ADD_GAS sidestep saves us 0.1 seconds of init (used to at least.
Ensuring we don't break archive is gonna have a cost. I don't want to
profile this so I'll estimate maybe 0.05 seconds). The faster version of
copy_from is just well, better, and helps to avoid stupid

[Optimizes pipeline
processing](https://github.com/tgstation/tgstation/pull/74233/commits/bf5a2d2d60554da2ce5fa1ac5f6c4179f6208cb2)

[bf5a2d2](https://github.com/tgstation/tgstation/pull/74233/commits/bf5a2d2d60554da2ce5fa1ac5f6c4179f6208cb2)

I haven't slept in 36 hours. Have some atmos optimizations

Pipelines now keep track of components that require custom
reconciliation as a seperate list.
This avoids the overhead of filtering all connected atmos machinery.

Rather then relying on |= to avoid duplicate gas_mixtures, we instead
use a cycle var stored on the mix itself, which is compared with a
static unique id from reconcile_air()
This fully prevents double processing of gas, and should (hopefully)
prevent stupid dupe issues in future

Rather then summing volume on the gas mixture itself, we sum it in a
local var.
This avoids datum var accesses, and saves a slight bit of time

Instead of running THERMAL_ENERGY() (and thus heat_capacity(), which
iterates all gases in the mix AGAIN) when processing gas, we instead
just hook into the existing heat capacity calculation done inside the
giver gases loop
This saves a significant amount of time, somewhere around 30% of the
proc, I think?

This doesn't tackle the big headache here, which is the copy_from loop
at the base of the proc.

I think the solution is to convert pipelines to a sort of polling model.
Atmos components don't "own" their mix, they instead have to request a
copy of it from the pipeline datum.
This would work based off a mutually agreed upon volume amount for that
component in that process cycle.

We'd use an archived system to figure out what gases to give to
components, while removing from the real MOLES list.

We could then push gas consumption requests to the pipeline, which would
handle them, alongside volume changes, on the next process.

Not sure how I'd handle connected pipelines... Merging post reconcile
maybe?
This is a problem for tomorrow though, I need to go to bed.

Saves about 30% of pipeline costs.
Profiles taken on kilo, until each reconcile_air hits 5000 calls

[old.txt](https://github.com/tgstation/tgstation/files/11075118/Profile.results.total.time.txt)

[new.txt](https://github.com/tgstation/tgstation/files/11075133/profiler.txt)

* Optimizes some gas_mixture procs, Optimizes pipeline processing significantly by 33%

---------

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [minaripenguin/android_frameworks_base](https://github.com/minaripenguin/android_frameworks_base)@[ec5445b44f...](https://github.com/minaripenguin/android_frameworks_base/commit/ec5445b44fd21f248f9e15e72014c0a87ccb550f)
#### Sunday 2023-04-16 00:20:13 by Adithya R

[DNM][HACK] telephony: Force Class 0 SMS to Class 1

This kills Flash SMS messages. Fuck you airtel

Change-Id: Ifb0c9e8bae5c12868d178fbdaeceb2cc72a0ffb6
Signed-off-by: Sageofd6path <mail2anirban95@gmail.com>

---
## [stoozey/SEngine-2](https://github.com/stoozey/SEngine-2)@[133c039c98...](https://github.com/stoozey/SEngine-2/commit/133c039c981d5c7c88049ab91600cfc350b11c94)
#### Sunday 2023-04-16 00:30:02 by stoozey_

added boost because fuck you; moved debug stuff out of engine

---
## [LemonInTheDark/tgstation](https://github.com/LemonInTheDark/tgstation)@[c3b78761d2...](https://github.com/LemonInTheDark/tgstation/commit/c3b78761d29c53558fd993c84bb808bd5783861d)
#### Sunday 2023-04-16 00:33:29 by tralezab

Adds Chuunibyou Spell + Granter (#74404)

## About The Pull Request

My April fools this year, though not going to call it one because some
people think it should just be actually merged.

### Chuunibyou Powers 🌟

Wizard gets a new spell for 2 points that gives him the powers of
chuuni. This makes them have ridiculous shouted invocations for all
their spells, their spells are colored pink, and they heal slightly when
casting one.

While mostly a meme spell, I could see a tailored loadout like lichdom
and splattercasting that takes advantage of the unique spellcasting
changes, like a very low cooldown spammable loadout to heal quickly.

There is also a granter book in the library, which teaches a version of
chunni that doesn't heal.

#### Medical eyepatch

I added it, chuuni wizards get a NODROP version.

## Why It's Good For The Game

This PR bestows upon the game the glorious gift of chuuni powers, the
ultimate manifestation of my hidden potential and the secret truth of
this world, which only I and a few chosen ones can comprehend and
unleash! Why wouldn't you want it?!

In all seriousness, it is a unique wizard playstyle and it will make for
some funny memes. Beyond wizard, the chaplain, heretics, or mime can
read it in the library for a very silly round. I like it!

## Changelog
:cl:
add: Chuunibyou wizards, and chunni granters in the library
add: Medical eyepatches
/:cl:

---
## [Nexix59/ProStrat](https://github.com/Nexix59/ProStrat)@[405d1e790e...](https://github.com/Nexix59/ProStrat/commit/405d1e790e726b2b4d7aa3b5b59e64a0a7e862bc)
#### Sunday 2023-04-16 00:58:20 by Nexix

zominout & cursor

The gods further expanded into the deep blued night. Their bodies were life like in those large masses of organic matter. All from the Jodick village from freightened. We knew tension was building since that low noise was belted out. It was heard all across the lands. Today was the day the gods seemed most human. As they propelled up their enormous bodies by titanic legs to reach above the clouds overhead. For moments that felt like years they all gazed deeply within each other. Time was still, as so was motion. All of our hopes, dreams, nightmares, and lives all felts certain in fate.0

---
## [HeapsOfRam/GAMENet](https://github.com/HeapsOfRam/GAMENet)@[37894d3a47...](https://github.com/HeapsOfRam/GAMENet/commit/37894d3a4778b4b8f57643e28b7ce8b756511fb1)
#### Sunday 2023-04-16 01:00:50 by ram

baseline logic

now the logic to train and evaluate the baselines has been included
in the container. this has been done rather messily and a bit
hastily, so i plan to refactor this a bit in a future commit. however,
the code in its current state represents a runnable docker container
that succeeds in the following:
- prepare the data for training purposes, including ddi graph and
  ehr data
- trains the GAMENet model on the prepared data and evaluates it
- trains the DMNC model on the prepared data and evaluatates it
- trains the LR model on the prepared data and evaluates it
- trains the LEAP model on the prepared data and evaluates it
- trains the RETAIN model on the prepared data and evaluates it

at least, my runs seem to be successful. training the dmnc model
took quite a while, ~20 hours or so on my Nvida 1080 GPU. one thing
i noticed was that only 25% of the GPU memory seemed to be used at
any one time. i wonder if this is normal or if i can somehow adapt
the data loader patterns or something to enable more data throughput
somehow ...

one of the most important things i had to do for this was to upgrade
my version of `torch`. i upgraded quite a bit, to version 1.4; after
this, the DMNC model was able to train. before that upgrade, the
model training had issues calculating the gradient for some operations
it regarded as self-assignment. anyway, now it trains though for
a long time. all of the other baselines seem to be working from
what i can tell as well.

i want to make the bash script cleaner, and add command line arguments
to evaluate whether baseline evaluation should be run. i also want
to make some of the other code cleaner as well. i can probably
abstract some of my rougher logic out into the utils file, and find
a better way to handle my paths. as i mentioned, this was a bit of
a "rough draft" attempt but since i have it working before project
draft submission i will commit it for now. hopefully in the next
commit i can make a lot of this stuff more clean and user friendly
before merging the pr.

---
## [shiptest-ss13/Shiptest](https://github.com/shiptest-ss13/Shiptest)@[7df4885117...](https://github.com/shiptest-ss13/Shiptest/commit/7df4885117a4a12ea333934d5af92e0766c84c5d)
#### Sunday 2023-04-16 01:23:46 by Mark Suckerberg

[Needs TM] The Accelerataning (#1781)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Gone are the days of spam clicking buttons to move faster in a
direction, with this PR, ships now accelerate constantly (as long as you
have fuel and don't touch the throttle) in a direction you set, leading
to a much smoother flight experience. I imagine it's going to be a bit
tougher to thread gaps, but flying a spaceship *is* quite literally
rocket science. So.

![](https://user-images.githubusercontent.com/29362068/220281305-12f6b796-9d8a-41ce-84a6-236bb03274da.gif)

Also actually makes the minimum and maximum speed work, and adjusts them
to a more tolerable level.

## Why It's Good For The Game
Eliminates the ability to cheese high speeds by spamming the accelerate
button, and also makes the flight experience much more pleasant as you
don't have to spam click to move a decent speed.

## Changelog

:cl:
add: A new system for ship flight, where you only point a direction and
set the throttle to change your speed, reducing the need for
spam-clicking.
fix: There's now a maximum and minimum speed, 600spm and 0.01spm,
respectively. The limits have been broken all this time.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Signed-off-by: Mark Suckerberg <29362068+MarkSuckerberg@users.noreply.github.com>

---
## [Superlagg/coyote-bayou](https://github.com/Superlagg/coyote-bayou)@[3ced3047b8...](https://github.com/Superlagg/coyote-bayou/commit/3ced3047b8c32a3e631519f6b117fdc6bf0630d8)
#### Sunday 2023-04-16 01:24:18 by Tk420634

Merge pull request #1949 from ARF-SS13/I-hate-github-a-lot

Fuck you, Vertibird.  Go where I put you

---
## [Superlagg/coyote-bayou](https://github.com/Superlagg/coyote-bayou)@[7b5b198aa8...](https://github.com/Superlagg/coyote-bayou/commit/7b5b198aa80b88426d1150184c78ecd5fa0816b8)
#### Sunday 2023-04-16 01:24:18 by Tk420634

Fuck you, Vertibird.  Go where I put you

You fucking animal of a thing

---
## [Ical92/tgstation](https://github.com/Ical92/tgstation)@[66cb695343...](https://github.com/Ical92/tgstation/commit/66cb695343721087437e651d07268e284e25763d)
#### Sunday 2023-04-16 01:31:05 by carlarctg

IV drips' default transfer rate is no longer zero. (#74724)

## About The Pull Request

Set default IV transfer rate to maximum (5) instead of 0.
## Why It's Good For The Game

> Set default IV transfer rate to maximum (5) instead of 0.

When you hook someone onto an IV drip, you naturally expect that to be
the end of the process - you hooked someone to a drip, and now you can
go about your day. Them needing to fiddle with buttons is bad for
several reasons:

- It is unintuitive.
IV drips don't look like machines. Their sprite doesn't reflect the fact
that you need to fiddle with the settings before they can work the same
way any other machine or computer might. And to be honest, they
shouldn't.
- It is separate from how every other server currently has it.
Yes, yes, I know that argument is very flawed and full of holes. But
what I'm trying to say with it is, effectively speaking, an extension of
the above point. In other servers, you drag-click someone to an IV drip
and there we go, it's functional. In TG, it just-so-happens to not be
functional due to what is almost definitely a recent oversight, which
very much can, has, and will lead to unnecessary frustration.
- There is no practical reason for it to be set at 0.
Imagine if chem dispensers started at +0 units and needed to be set to
+5 to continue. Or if bottles had a transfer rate of 0u. Or if guns
started with their safeties on. Even if it made sense, it would just be
frustrating and needless, and wouldn't improve the game in any
significant manner enough to offset frustration. We're here for fun, not
perfect balance or realism/verisimilitude after all.
- It's an oversight.
It was changed in #71217. Before that, it was always set to the maximum,
5u. However, presumably due to confusion (Variables that can be adjusted
ingame usually are set to zero/the minimum possible) it ended up being
changed to this.

Apparently an argument can be made that this is fine because fumbling to
get medical aid done is a part of the game. I disagree heavily - blood
bags are already stored in the cold room, something only 2/5 of the
roles in medbay even have access to, with the paramedic, virologist,
chemist all being unable to reach it. This is already enough 'fumbling'
that's necessary. If someone moved the blood bags outside the cold room
next to the IV drips, then all the better - it's a reward for medbay
being prepared.

However I wouldn't mind if someone asked me to make it so the default
transfer rate is, well, something below maximum. It's common practice in
a lot of parts of SS13 to have things set in an unoptimized state so
players can go around improving them, such as air alarms, cryogenics,
etc. Just as long as it's not literally unusable otherwise, as the
'minimum basic setup' should just be slapping on a blood bag!
## Changelog
Dunno what to put here TBH. Can't tell if it's qol, fix, balance, etc.

:cl:
qol: Set default IV transfer rate to maximum (5) instead of 0.
/:cl:

---
## [Ical92/tgstation](https://github.com/Ical92/tgstation)@[205ea3dad7...](https://github.com/Ical92/tgstation/commit/205ea3dad711fa541f93adc7f2053250d3e3c777)
#### Sunday 2023-04-16 01:31:05 by Bloop

Fixes spoon overlay not updating every time (#74687)

## About The Pull Request

After bludgeoning myself one too many times with a spoon, here we are.

The spoon overlay wasn't updating to reflect that soup had been
consumed, which led to trying to eat it again and then pain.

Why do spoons hurt so much?

## Why It's Good For The Game

Less spoon related injuries.

## Changelog

:cl:
fix: spoon overlays will now update when you eat from them to reflect
that food = gone. it really is gone, you can stop beating yourself with
the spoon. oh god please stop--
/:cl:

---
## [Lypheo/mpv](https://github.com/Lypheo/mpv)@[fd9106e4dd...](https://github.com/Lypheo/mpv/commit/fd9106e4ddc66cb1967f16162d54743410a0c8c1)
#### Sunday 2023-04-16 01:37:43 by Lypheo

sub: more fixes + move update_subtitles call to playloop

Makes shit a lot more sane I think. Haven’t noticed
any performance or behavior differences but then again
it’s 3 a fucking m and I haven’t produced a single
coherent thought or line of code all day. Hopefully
I’m done with this shit now because it’s all disgusting
mess and I don’t wanna touch it again.

---
## [re621/dnpcache](https://github.com/re621/dnpcache)@[b443047ed6...](https://github.com/re621/dnpcache/commit/b443047ed6fb5480ba0adb55d78b2fda9dac99cc)
#### Sunday 2023-04-16 01:49:04 by bitWolfy

Remove 1081 artists from the DNP list.

Removed: lintu, goobysart, lemonlycan, dylbun, fxscreamer, nt6969, lewdliege, reallyhighriolu, melbaka, saint_lum, kivaaa66, kivalewds, kazoko_(artist), barachaser, shadowthelastalpha, teke, crittermatic, ribboncable, domasarts, ursine-major-ike, browneyedsaiyangirl, uncensoredhugs, skydiggitydive, takarachan, feelin_synful, ilovecosmo, biffbish, pulp_(artist), doxhun, cupsofjade, nicesweater, bluecat_friend, peshky, masuku, lunarfloral, kugi, sagejwood, sqrlyjack, maiteik, leozedi, popdroppy, mikakater, 413k_zzzz, puppyemonade, xanthewolf, joooji, nasusbot, shredded_wheat, dogsdontwipe, wonderwaffle93, gogoandyrobo, jezzlen, dourdoofus, vksuika, klotzzilla, cooperdooper, shadnaotomi, nudegote, sexygoatgod, humgeronimo, ladysophia, mrwhiskerz, cocicka, d-wop, charmerpie, yourdigimongirl, elvche, booponies, lulubelluleart, infinitedelusion, tankakuka, mensies, trunchbull, evian, sodasquids, telelewdz, lawlzy, tonio_(artist), xankragoc, horrificrabbits, sinfulgoatz, whippytail, malachimoet, catniplewds, cocaine_(artist), marshy_swtr, goldelope, chokodonkey, notkastar, sinnerscasino, sentharn, tealie, einin, freaks, angellsview3, arwenscoots, royalzbed, hellfurred, byrth, hexuru, devildjmachine, malerouille, donovallo, psychoninetales, vahldem_sol, nyanyakotarou, shupamikey, zyegnar, akytti, sootylion, kiva~, calmnivore, nexcoyotlgt, smoothsharb, sub-rosa, brismy, woodpeckertoons, xeshaire, suirano, mr_otter_breath, bassybefuddle, sweetishcyborg, skullwomb, steak_in_the_daylight, kittydogcrystal, aggrobadger, orbstuffed, fraichetaso, loonyleandra, bunsawce, schl4fmuetze, renkindle, psychovixen, bkmat55, fricken_stoat, w00my, haven_(artist), gipbandit, loki_the_vulpix, pixelyteskunk, erobos, bunchantress, uniquesoul1600, hirowithart, mikaemikae, ratbloke, pastellprinz, racktor, coillte, kazuk9, acidneko, josh_gong, yiyani, grayish, moblo, naoma-hiru, molish, sheyesh, st0pme, cawkbox, unclesam1776, fennecfuchs, inkpuni, pico_(artist), ruugiaruu, wispyparadox, funkybun, lewdoreocat, dogseesghosts, fauwcks, randy_entinger, trex_b6, yui-hii, runaris, rainbowpillars, ragonox, luxuria-sins, maxisb8, hiccyart, fancyfez, mesoplush, gammelgaedda, yi_feng, scpkid, goetiagoat, mabit, dischimera, dr.bubblebum, drakeraynier, rml, amawdz, mc_arts, freemau, armomen, orionfell, luriostragedy, dradmon, jesterghastly, gothgator, talentlesshack, foxryk, supertrashparty, marrowsoup, roserivy, vanzard, deepfriedlemons, pehkeshi, torotheking, harewithoutahat, lucciola, mr.lemur, lemonkyubun, cubble_chubb, arrjaysketch, pinklilim, jingo824, consciousafterdark, anti-cupid, phosaggro, dashboom, giftheck, birdrabbit, desertmotels, lv99perv, stellarfalcon, tasaeyeang, knotty, rockfall, aogirinaru, hikebu, pawpadcomrade, frengers, rikkitz, vappypaws, nukeleer, adevio, gummuru, sattytsukumo, bittenbats, whygena, ruzeb, hungothenomster, jads_l_rutan, gattonero2001, shawoo, francis_xie, angeltf, veevobyte, darkfool., huwon, tsukikibaokami, covepalms, nikunabe1989, emifern, pero3, tricksta, inkbeastart, grinn3r, holidaydipstick, odonata-nymph, binxxy_(artist), zazush-una, sodo_ad, loonanudes, kodardragon, flameydragwasp, ablimpfox, bakvissie, eccstasy, esealia, tailsrulz, dexxa, spiritto, vonepitaph, eddy-boy, saiyangoku4, gatomonlover, moonlit-comet, thehenwithatie, brienoir, tegucreative, wanisuke, pxlfur, anomyna, motsutambo, fepon, cyrogenic, fursuitchina, slates1n, depthsofthedrex, furrybob, davelievski, spacemaverick, fluff-kevlar, evenytron, 0eff0rt, gayclub, goatypie, nikoyishi, alishka, makeinu, jfetspeaks, cowbun, wyrwulf, thespiderbunny, fluffx, dragons-and-drawings, jcosneverexisted, emptyset, scoty_doodlerz, makinglemonade, ceramic_(artist), selirum, euskuuy, tsunkat, lustbubbles, appleseid, lewdtant, werewuffstuffer, odontoceti, iaido, turboranger_(artist), saca44, mr.shigglesworth, pyriax, raijikaruart, fox-pop, sirblythe_(artist), pastelarcadiaad, etherealarcadia, dracoarcadia, benjibat, sarvak, amethystbeetle, fnook_(artist), stationarrow, maim, rashkah, psy101, disappointedf0x, pointedfox, bundog, tailgrip, scalesforlife, hayleymulch, saphe, kiweevil, madakan, papyreit, rainiing, bitelickart, done0008, alec8ter, tentativelytoon, mikurulucky, killveous, fishhound, misshammer, yakushishi, pieraite, knives4cats, jalmu, quin-nsfw, zooptoon, ebonychimera, beaglebabe1, filthy-d, l-tech-e-coyote-l, anomalae, rakket, mcdutt, alcor90, sodongs, catcock, blickfen, akiiokai, possumkiddo, inkplasm, doubledeal_(artist), fuzzlesuits, chetchaka, raaazzledazzle, razferret, razbuckner, ikitsunyan, kclt, draco_(artist), gunther_silves, kkitten, singafurian, zandybutt, comfytail, crazyassbeethoven, dogburger, adalee, alirrasarts, blackmagemathos, terragon, leonois, solidpoint, cloudpie, rottenscoundrel, wings-and-strings, tomcoletti, pikajota, squeakcore, doubleclawed, ebonyplume, myznyx, zackary911, gaturo, xepher777, aimee-lesley-sim, spottedsqueak, fuhrawr, isaac_baranoff, starnina15, zestylemonss, meirdent, babymee, explicital, slyvern, karpet-shark, booghetti, zypter, adaptagx, opiodae, kiwipotato, murkbone, jonas, exed_eyes, shuryashish, mangobird, kurogi_fox_siv, snuddy, grimdank, nighteternal2469, dacad, superhypersonic2000_(artist), drako1997, verenpunainen_kuningatar, gurophilia, furrever, rdroid, smolrainbowgoat, ratte, urban-coyote, soulsplosion, cyaeon, elliotte-draws, whisperingfornothing, griz_urso, lepronasty, tears_of_soy, bunnielovesyou, paliken, spaceysoda, david_frangioso, cattinypaws, bobdude0, sprocket_(artist), sincerity_gender, marymanifold, turnipberry, asbel_lhant, klaide, rishi-chan, kircai, otto0ttsy, vaktus, beezlebumawoken, transdonaldduck, questly, pinkkatfox, goopomancer, xoel, allbadbadgers, sugarlesspaints, imafutureguitarhero, eiko_tsukida, tarot_(artist), pinuh, diero, dilarus, dfer32, mxwqtkl, electrycpynk, insomniacovrlrd, cewljoke, craziestrobo, anthrus1127, sunflowerbun, coyoteofthesands, masonparker, dottii, livesinabag, flam, toastedbiscuits, skycladfox, orenjisalmonpaw, nasty-fox, canadian_roses, crez, glorpofruithag, i_am_clover, johawk, lycosa, wizardlywalrusking, burgerkiss, kielseki, whisperfoot, oksara, olly, fetchmonkey, rottingichor, heathenfang, bikomation, phox_(artist), acedetrap, hedonisticvows, deersun, skittleytwix, jinxit, jtp-remart, cocaine-leopard, amarl_krieger, nakoo, leoian_(artist), amyth, nogu-art, bluhcat, vulpes_helios, licos, taurika, papilrux, pophopper, ebnet, apis_(artist), glenthefossa, raitime, sashabelle, puddingpaw, mercurial64, elricmysteryshifter, puptaire, anojaa, candychameleon, spice5400, nickshutter, rem, reiishn, sandybuny, 1oi, crunchobar, dante_yun, pherion, saintxd, rawbelr, mithaa, asmartist, pannekoeke, jotun22, iguky-neky, ahnik, thatvondude, kelevtov., fishwrappe, animal_shapes, oouna, princess_rei, blitzdrachin, jesterdk, watermelon_(artist), amara_lemur, lady_kurai, giantmilkdud, nostars, koili, abananaman, heddy, slobstash, terian, teranen, nexii, parabellux, tom_fischbach, reddacted, tojo_the_thief, proximiter, mmuted, irootie, icyshibe, quetzalcoatl_(artist), lamm, shayshay~, hettie, chutzpaah, jacob_lhh3, carpetwurm, draekos, fatdingleberry_(artist), nooplip, pandasayori, numberxxxvi, bc92, silvixen, jungabeast, phoenixazrael, krazykurt, tape_(artist), iipaw, volvokun, hamstergirlthehamster, fallen_(artist), morkovjpn, wolfirry, slimedrops, rubisdrake, shortconcepts, ahdadah, chubbuppy, dreadcaptain, duckdraw, mehndix, pomander, wolfcha, evillabrat, henzolin, loupgarou, empa, diokhan, kpsketches, raysofsunshine, slash0x, kriticalerror, gallivant_crow, nyaroma, caindra, petit-bambi, thatblackcopfromdawnofthedead, dreamertooth, tofu93, ragnarokdragon, saucy, kidakins, kippy, swizzlestix, brilyeon, caste_(artist), tsukaui, saebira, ozzybae, boo-rad13y, sammythetanuki, vuurren, sinistervibe, rem289, shroompunk, samkin, cieldoberman, g0966, crazedg, gaoru, lpawz, enjoipandas, renthedragon, emeritus_terciel, xouual, tehcutepyro, anon232, grimmgrey, counterserum, knottykitten, crybleat, octopoodle, ker0ker0_(artist), xnirox, necrosquelch, ivenvorry, pkuai, mikefur, mattsykun, lilithveritas, bloodhound_omega, ogaraorcynder, rhos, kehei, aw0, apes, nyhgault, qualzar, licentuouslamb, reggaecyp, cynderplayer, vilegrim, redacteur, jimbohusky, lacrimale, pulsar, growlybeast, coreytwc_(artist), naoki_wolf, iceagechippies, alfierubuncle, cbee, acidic, louiefurrywolfy, bweezy, fluffernubber, koriaris, serena_valentine, tacoyaki, fullheroo, limlam, harmoniousrain, zotnamotgrim, xx_g.u.n_xx, carm, lustylamb, dragonvortex, crowchild, dragoneer, lumi_(artist), phi, lexathefox, tanookicatoon, thunper, korram, redwolfofwind, ipipo, teckworks, abobarseem, doopcity, xepheriah, diablo_en_musica_92, doncoon_(artist), digitaldomain123, belayalapa, delkon, connisaur, jasonafex, kabier, rohly, vcr-wolfe, steve_gallacci, hologram_(artist), irene_(artist), piumartiglio, sumat, kingofmaggots, oha, featheredclaw, snuddi, mentalo, ourflatcoat, da-fuze, herr_aardy, discoverychannel, azorart, nemomein, latex_(artist), afterdarkie, 7mii, draco_fenris, blown-ego, sissyskunk_(artist), chucktheskunk_(artist), oakspirit, brokenlynx21, nickswift, butter_bat, ben_hickling, bluehunter, soyuz, sorimori, blackbearcj, ficus, crimes, eifie, soundwavepie, besonik, greyskee, alekksandar, bluetigress, nereza, kalvince, thelabtwins, the_lynox, galaxyoron, moondevourer, evov1, enjambre, seph_ebonblade, prototypebasilisk, accell, myakoda, merenhor, muramuri, derfuhrer, moltengoldart, cchipppo, tetrapoda, omochi_(inkbunny), popsmasterson, nikinazu, raevee, wyntersun, ribboners, c4camel, shysketch, deishido, arconos, melvismd, taihab, cobalt_snow, flak_wizard, paddington_and_company_limited, dangerdoberman, inprogresspokemon, whitemantis, naexus, datsexylemur, polywomple, marilimmy, ryan_rabbat, krimrath, yoshitura, maplecookies, aurelleaheverfree, puppercase, spino, palcomix, bbmbbf, lilithofglace, frisket17, myloveless, grau_(artist), aduleon, sexbad, mearcu, murcifer, citrusdicks, hessonite, sokalo, kittehmei, puccaruu, yuurikin, kurikia, the_cherret_awaits, rapps, maxtwenty, bigbrownorc, santanni, twistedtemptation, nikita-the-stag, liz_art, camcartoonfanatic, singlerider4, beanbat, forge_(artist), hoshime, yamamoto, eviljake2, oriole_(artist), inkblooded, alefwdog, herisheft, disparitybit, samagthrav2, battle_franky, taesolieroy, wolftacos, anixis, spazzticglitch, pirun, swampstomper, morbi, mittsies, blondevelvet, kadath, danza, shinxiolu, littlefreckles, grumpyvulpix, xopachi, gonenannurs, floravola, heartcollar, metz, ranard_lightningfall, frots, curtsibling, vilani, inkydemon, sprinkle-butt, airguitar, anhes, jace_(artist), kaji_(artist), nimrais_(artist), kyoushiro, venerit, lunaselenewolfe, tsareia, violentanxiety, kk-furryworks, cobalta, mickeyila, akuva, rairai, backlash91, sanae, fishbones_(artist), itoril, littlemiu, zeara, darkrokkuman_(artist), peony, helical, donro, agalamt, inanna-nakano, aniutqa, kraest, audiovideomeow, silverbobcat, erithacuscreations, mattartist25, yasminachan, jagzcat, ohmuu, roum, sefeiren, sesameseedbun, noben, aquatheohiokitty, mewyfox, ilgrigio, leoian, vixendra, van_weasel, keihound, zoey03, hardblush, jay_naylor, frisky_ferals, slipshine, rubyrebirth, oze, neogeen, omegaltd, themadcatter, kamicheetah, ookamithewolf1, rabbit_valley, purplekecleon, ollieosa, jayfiregrowlithe, ensayne, bazaarbobby, scappo, dogsoul, poonani, paddercat, eltonpot, ebonyleopard, strype, cbh, mithril07, bicdente, unpeeledwasp, versiris, pitkin, mikachu_tuhonen, lilhoneypup, ladyshinwa, bad-collie, buizilla, foxxian, inert-ren, okamiterasu, mrawl, sammy_stowes, jameless, jooshster, lemoncore, xainy, strider-orion, silitha, spacepoptart, myuinhiding, sweetpinkpetals, sephygoth, edensky, ka, cigarscigarettes, tani_da_real, leatherruffian, hahul, cheezyweapon, reizakirga, leefuu, tanyafoxy, peyo, sweatshirt_(artist), adiago, timelesserror, jollyjack, kahmari, madhattermonster, omnoproxyl337, greykitty, thekitty, mattaku_shinzu, fortuna, fallenarts, ammako, sciggles, atlasfield, sheepdust, lumaberry, tktktk, uzai, aku_tojyo, sixthleafclover, gardelius, squeedgemonster, max-dragon, baka_sukonku, ferniio, jennadelle, ixerin, jaleo, luvythicus, tatious, nekomata_neko, zody, binky, sidian, kii-kitsune, kiirei, spookeedoo, angel27, msrah_(artist), nazuu-m0nster, lunacatta, kululu-xiao, kipcha, fluffball, reptilecynrik, redadillio, zerwolf, kylontario, liz_day, nightweaver, egophiliac, doffa, dipper, kefkafloyd, melo666, sonicdash, sugarpoultry, olven, theramjing, softpaw, xiraco, unicornspirit, tinintri, thornwolf, thaily, tamen, sharue, shadowsani, rikutida, paolo, kriscrash, kaemantis, frogsbreath, tailheat, sexyfur, jeremy_bernal

---
## [Voltaic314/Daily-FB-Poster-For-Python-Betty-White-Bot](https://github.com/Voltaic314/Daily-FB-Poster-For-Python-Betty-White-Bot)@[254204b9bf...](https://github.com/Voltaic314/Daily-FB-Poster-For-Python-Betty-White-Bot/commit/254204b9bfe1f245e54e56bb8f11f8aedfc674da)
#### Sunday 2023-04-16 01:59:55 by Logan Maupin

Fixed typo and implemented April Fools' Day feature

Fixed a typo in the posting from where it would say "She's Dead." to now "She's dead." <-- I promise English is my first language, I'm just a moron. haha

Also, implemented an automated April Fools' Day gag feature which is kind of funny. haha

Also I removed my bad documentation within the code description itself stating how it posts a select few list of statuses because that's technically not true anymore. At least not currently.

I am thinking one day I might use some kind of large language model to find creative ways to say she's dead every single day. But eh, maybe I'll implement that one day if I can find a free and easy way to do it. I want this project to stay free and lightweight if possible.

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[4014aef4b0...](https://github.com/tgstation/tgstation/commit/4014aef4b0a24d260b314f462a21f943c3d62894)
#### Sunday 2023-04-16 03:31:48 by Bloop

Fixes a runtime in simple_animal/hostile (#74706)

## About The Pull Request

Attempting to fix this flaky test that has been cropping up from the
Icebox tests. It is annoying.

From what I can tell, the mob was getting qdeleted while it was doing
its loop of finding a target. This can happen at any time, because many
simple mobs (including the one causing the issues) get qdeleted on
death.

Added some more checks to make sure we don't do certain actions if the
mob gets qdeleted midway through execution of its AI routine. It really
could happen anywhere so we must be vigilant.

```
create_and_destroy: [02:24:31] Runtime in stack_trace.dm,4: addtimer called with a callback assigned to a qdeleted object. In the future such timers will not be supported and may refuse to run or run with a 0 wait (code/controllers/subsystem/timer.dm:583)
proc name:  stack trace (/proc/_stack_trace)
src: null
call stack:
stack trace("addtimer called with a callbac...", "code/controllers/subsystem/tim...", 583)
addtimer(/datum/callback (/datum/callback), 300, 8, null, "code/modules/mob/living/simple...", 595)
the demonic watcher (/mob/living/simple_animal/hostile/asteroid/ice_demon): GainPatience()
the demonic watcher (/mob/living/simple_animal/hostile/asteroid/ice_demon): GiveTarget(the mi-go (/mob/living/simple_animal/hostile/netherworld/migo))
the demonic watcher (/mob/living/simple_animal/hostile/asteroid/ice_demon): FindTarget(/list (/list))
the demonic watcher (/mob/living/simple_animal/hostile/asteroid/ice_demon): AIShouldSleep(/list (/list))
the demonic watcher (/mob/living/simple_animal/hostile/asteroid/ice_demon): handle automated action() at stack_trace.dm:4
```

On top of that, there is signal handling in place to LoseTarget() when a
mob that is already a target gets qdel'd and sends
`COMSIG_PARENT_QDELETING`. Shown below.


https://github.com/tgstation/tgstation/blob/4c48966ff80915ee0b4f796994a0ab6616cab31b/code/modules/mob/living/simple_animal/hostile/hostile.dm#L655-L666

However there is nothing stopping a target that is not null but that has
been qdeleted from being considered as a target in the first place.

This PR just aims to fix that problem by making sure that a) a hostile
ai that gets qdeleted midway through does not keep doing stuff that can
cause issues and b) an atom that is being qdeleted never makes its way
into the targets list of a hostile ai.

Simple mobs/AI are due for a wider refactor honestly but this really
ought to be done in the meantime so we don't get spammed by CI failures
over nonsense.

Fixes https://github.com/tgstation/tgstation/issues/73032
Fixes https://github.com/tgstation/tgstation/issues/74266
Fixes https://github.com/Skyrat-SS13/Skyrat-tg/issues/18964
Fixes https://github.com/Skyrat-SS13/Skyrat-tg/issues/19749
Fixes https://github.com/Skyrat-SS13/Skyrat-tg/issues/18964
Fixes https://github.com/Skyrat-SS13/Skyrat-tg/issues/19322
Fixes https://github.com/Skyrat-SS13/Skyrat-tg/issues/18974
Fixes https://github.com/Skyrat-SS13/Skyrat-tg/issues/19296
Fixes https://github.com/Skyrat-SS13/Skyrat-tg/issues/19294


## Why It's Good For The Game

Bugfix, stops the icebox test from failing as much.

## Changelog
:cl:
fix: fixes hostile mobs sometimes being able to target an atom that has
been marked for deletion and then becoming confused, and in a similar
vein fixes mobs sometimes still running their AI while being marked for
deletion.
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [InsightfulParasite/lobotomy-corp13](https://github.com/InsightfulParasite/lobotomy-corp13)@[582f5b38cb...](https://github.com/InsightfulParasite/lobotomy-corp13/commit/582f5b38cb9ad5d051cbea48af501089ba3f0206)
#### Sunday 2023-04-16 03:32:20 by Lance

Holy FUCK temporary commit

Mixed between previous abno based spawning and new subsystem

Cleanup Commit

Removes a lot of previous code and paves the way for the subsystem method.

Major Commit

Apocalypse Bird drops it's loot and only spawns once. It'll not try to happen if there aren't enough birds, and if two are breached before the third arrives it'll take the third breaching to start the event, until the others are suppressed. Birds do not target people and are immortal while moving to the portal. If unable to reach it after 3 minutes they'll be forced in manually.

Tweaked Proc

Redundant Code Removal

Remembered I didn't need this

Enhanced Code

Moved an if-statement to a better place to more adequately solve the issue.

Test Commit

Does this solution work?

Global Abnormality Mob List

Patrol Changes and Bird Grab changes

Gaming Test?

Temp Commit

Second Commit

Another Commit!

Fourth Commit

Subsystem changes. Dead abno cleansing. Lower speak cooldown. Debug text removal.

P-bird fix

Fixes P-bird able to die before reaching the portal

---
## [lllgts/android_kernel_xiaomi_cepheus](https://github.com/lllgts/android_kernel_xiaomi_cepheus)@[91eb13eb83...](https://github.com/lllgts/android_kernel_xiaomi_cepheus/commit/91eb13eb83be2033f2db33a42c64825c66dd3b64)
#### Sunday 2023-04-16 06:25:04 by Peter Zijlstra

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

---
## [Sulaboy/cmss13](https://github.com/Sulaboy/cmss13)@[3978cfe70f...](https://github.com/Sulaboy/cmss13/commit/3978cfe70f7e32331243e8b05738067b6101ebe6)
#### Sunday 2023-04-16 08:02:39 by spartanbobby

LV522: Chances Changes (#2695)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

This PR makes numerous Changes to LV522 as well as adds more props to
ease of mapper use

# Explain why it's good for the game

The areas changes and reasons why as are follows
**SW Reactor:** Entirely removed and replaced with a much more open
containers area for the xenos to build up and defend, this area is now
the linchpin of the map as marines have to push though it to get to
other flanks inside the reactor meaning the xeno players should now have
a much better understanding of where they need to defend instead of
prior problems with the map of them being hard flanked and losing at
12:26

**LZ1:** LZ1 was moved slightly more north in an attempt to remove some
deadspace and make the path from the front to the FOB slightly less
long, more LZ1 tunnels and ways inside the FOB were added for xeno
flankers aswell as LZ1 being locked down until the marines push a button
to open it up

**Colony admin** A sensor tower was added to colony admin to encourage
marines to go over there and investigate, along with a lockdown to the
area being added

**LZ3** a FORECON prop LZ housing the Tornado was re-added after being
removed in an attempt to downsize the map, basically I figured out where
I could put it

**props:** Alot of instanced props for the map were made into actual
items such as, bedrolls and folded bedrolls, FORECON dogtags, used
flares, jerry cans, used bandages and some weird gameboy thing

Sprites: https://i.imgur.com/avi2fUo.png
FORECON was always made to have a patch it was one of those things I
wanted but never got, luckily while making this PR I was able to look
into it and get the old sprite from tri to finish up myself with onmobs

FORECON Balance changes: The M39 being in the primary weapon slot is
more of a "fuck you" to people playing the roll than just unlucky RNG
that is workaround able moving it to the secondary pool lets the FORECON
play around with better weapons to survive with and the M39 extended
magazines means it's one of the only weapons FORECON spawn with that has
a decent amount of ammo

# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->
<!-- If you add a name after the ':cl', that name will be used in the
changelog. You must add your CKEY after the CL if your GitHub name
doesn't match. Be sure to properly mark your PRs to prevent unnecessary
GBP loss. Maintainers freely reserve the right to remove and add tags
should they deem it appropriate. -->

:cl:SpartanBobby
add: Made some instanced props on LV522 actual items for mapper ease of
use
maptweak: tweaked LV522, removing the SW reactor and replacing it with a
much more open container area once used as the FORECONS FOB
maptweak: tweaked LZ1 on LV522 making it start locked down and be
slightly more north along with some extra tunnels and flanking routes
for the xenos
maptweak: LV522, added a lockdown and moved the sensor tower to colony
admin
maptweak: re-added the prop LZ in the NE of the colony
maptweak: redistributed LV522 mining metal spawns to be more spread out
maptweak: removed building color outlines from LV522 that were there to
help with navigation during Test merges since the map has been out for
long enough for the majority to properly navigate it
tweak: M39 removed from FORECON primary weapon pool and added to
secondary weapon pool along with extended mags instead of normal
add: Added FORECON Patches for the survivors on LV522 sprites made by
Triiodine while onmobs were made by myself with help from Kugamo
fix: examing a uniform no longer tells you that it has "an
USCM/FORECON/Falling falcons patch" instead it says "a patch"
add: updated the USCM FORECON uniform name and description 
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---------

Co-authored-by: Nanu308 <59782240+Nanu308@users.noreply.github.com>

---
## [DoughDom/monky](https://github.com/DoughDom/monky)@[30da26a6cf...](https://github.com/DoughDom/monky/commit/30da26a6cf9c1d435f49d0833c7b92015b742121)
#### Sunday 2023-04-16 08:09:24 by cheeseyspacecat

updated city platform texture

FUCK YOU (rhetorical)

---
## [BOO1980/boo-self](https://github.com/BOO1980/boo-self)@[4f06de61b5...](https://github.com/BOO1980/boo-self/commit/4f06de61b5648cffe34d9b928a9c3985989940e3)
#### Sunday 2023-04-16 11:03:40 by Hayley

Self: Unfuck Yourself: I am not my thoughts, I am what I do

---
## [Coxswain-Navigator/lobotomy-corp13](https://github.com/Coxswain-Navigator/lobotomy-corp13)@[928b2420d9...](https://github.com/Coxswain-Navigator/lobotomy-corp13/commit/928b2420d906fbdef89ce27d75db5afe713b147d)
#### Sunday 2023-04-16 11:40:03 by Lance

Servant of Wrath

Records and Instability

Dash speed up

Fuck you I'll space indent all I like

There was some fuckin lint in this PR

God damned there's a lot of lint in here

Faction Check

Sprite update, minor bug fixes

Floating and Gun and Acid

Minor Records

Small update

Unnerfs resists

AoE hit fix

Gun update real

more res should mean less talk

Pixel Fix

Sound... Fix?

Broke the staff's legs, fuck those guys.

lmfao audio pains

Gun Rename, Spawn nerf

NO MORE FRIENDS FROM GUN

Faction change

acid tweak

LINT!

SW Code and Balance

SoW Temp commit

Scuff-Fix

SoW bonk update

Hermit range increase and ranged damage decrease

visual fix

Ending adjustments

I forgot to carry the 4

Visual indicator

minor fixes

Instability Tweaks

Paperwork Update

Anti-Self-Burn

Ending Update

Right view

A check that should be a non-issue but i'm making sure!

Breach Update and EGO update

More goo and FEMALE

Improvement and new Icons

---
## [georgebrock/sorbet](https://github.com/georgebrock/sorbet)@[3cb2b4b1c8...](https://github.com/georgebrock/sorbet/commit/3cb2b4b1c868b15f8b572a63099b87720d581018)
#### Sunday 2023-04-16 11:46:22 by Jake Zimmerman

Remove call to `dealias` in namer (#6519)

* Remove call to `dealias` in namer

We don't allow constant aliases in class scopes anyways. Not sure why
we're trying to dealias here.

If I had to guess, this was a remant of some hacks we had way long ago
to support this pattern, which was common in Stripe's codebase:

    class Chalk::ODM::Model
    end

    M = Chalk::ODM::Model

    class M::A
    end

But this pattern is already rejected by Sorbet, and has been for as long
as I can remember, so likely when that change was finally made, someone
forgot to delete this `dealias` call.

* Remove unused `ctx` parameter

---
## [DoughDom/monky](https://github.com/DoughDom/monky)@[2df709a9c3...](https://github.com/DoughDom/monky/commit/2df709a9c3eab50a8a30519fcaf27a004e5e2c56)
#### Sunday 2023-04-16 12:53:19 by cheeseyspacecat

waffle :yum: :alien:

a texture for a waffle cone, not sure its seamlessly tile but fuck it we ah shit

---
## [Eskuero/fehbuilder](https://github.com/Eskuero/fehbuilder)@[1bfca10c9d...](https://github.com/Eskuero/fehbuilder/commit/1bfca10c9d2777730a644c82e6e1d66f24b309c9)
#### Sunday 2023-04-16 12:55:36 by Óliver García Albertos

Revert "HOLY SHIT FUCKING HELL AWHDYGAWDYWADG"

Bless you IS for this banner
This reverts commit 84a8d9dce5a84f320535f4cc4a85c03c28d03bd1.

---
## [BaamBuus/Pythia](https://github.com/BaamBuus/Pythia)@[563abf324d...](https://github.com/BaamBuus/Pythia/commit/563abf324de71662258030ae9928122484c65bb8)
#### Sunday 2023-04-16 13:24:07 by Bambus

Create README.md

yeah pls read this i hate making md shit

---
## [Zlorthishen/Cataclysm-BN](https://github.com/Zlorthishen/Cataclysm-BN)@[08d54d0287...](https://github.com/Zlorthishen/Cataclysm-BN/commit/08d54d0287a1313cb810a1d3d74ca0e531189ae1)
#### Sunday 2023-04-16 14:29:07 by KheirFerrum

Fix MGOAL_FIND_ITEM_GROUP, fix up some code (#2546)

* Reorganize

Code still sucks. In particular recruit_class doesn't compare properly with npc->my_class so MGOAL_RECRUIT_NPC_CLASS fails horribly even if you fix up that area of code to it actually points to type->recruit_class instead of recruit_class

For that matter mission has a select copy of several mission type defs and I can only assume this is due to legacy fuckery.

* Fix mission.cpp

Now will only allow you to select items if you have enough of them, and will only consume the necessary amount.

Added documentation for MGOAL_FIND_ITEM_GROUP

Thank god this wasn't too much work.

---
## [copperwater/xNetHack](https://github.com/copperwater/xNetHack)@[81bcae0cf2...](https://github.com/copperwater/xNetHack/commit/81bcae0cf28c5e6d659bea732481beb57e5fc492)
#### Sunday 2023-04-16 15:21:45 by copperwater

Enable monsters with a specific class and alignment in special levels

This is to enable the specification of lawful demons in lawful demon
lord lairs, and chaotic demons in chaotic demon lord lairs, without
making specific assumptions about which monsters appear in the monster
list.

This is a bit of a hack, because it overloads the (unused, and unlikely
ever to be used) path of creating a monster of a definite class and
/in/definite species who is a minion of a specific god. The "correct"
way to do this would be to add another alignment field to the sp_lev
monster struct and treat it completely separately from the existing
"align" field, but since I don't expect that behavior to ever be needed,
it wasn't worth doing the "correct" way.

There are plenty of existing places in special levels where minions with
a specific alignment are specified, but they all have a specific species
(either aligned clerics or Angels), so no existing levels are affected.

---
## [TheCrazyInsanity/Supersymmetry](https://github.com/TheCrazyInsanity/Supersymmetry)@[537dc56ca8...](https://github.com/TheCrazyInsanity/Supersymmetry/commit/537dc56ca8347b7d61f91685f37587c48b2ea635)
#### Sunday 2023-04-16 15:51:25 by TheCrazyInsanity

I felt like it again

You unlock more than one technology

Hey guys, did you know that in terms of male human and female Pokémon , Vaporeon is the most compatible Pokémon for humans? Not only are they in the field egg group, which is mostly comprised of mammals, Vaporeon are an average of 3”03’ tall and 63.9 pounds, this means they’re large enough to be able handle human dicks, and with their impressive Base Stats for HP and access to Acid Armor, you can be rough with one. Due to their mostly water based biology, there’s no doubt in my mind that an aroused Vaporeon would be incredibly wet, so wet that you could easily have sex with one for hours without getting sore. They can also learn the moves Attract, Baby-Doll Eyes, Captivate, Charm, and Tail Whip, along with not having fur to hide nipples, so it’d be incredibly easy for one to get you in the mood. With their abilities Water Absorb and Hydration, they can easily recover from fatigue with enough water. No other Pokémon comes close to this level of compatibility. Also, fun fact, if you pull out enough, you can make your Vaporeon turn white. Vaporeon is literally built for human dick. Ungodly defense stat+high HP pool+Acid Armor means it can take cock all day, all shapes and sizes and still come for more

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[3b821c387a...](https://github.com/mrakgr/The-Spiral-Language/commit/3b821c387ae4bfa7ad18d9615e620108a2cb4fe3)
#### Sunday 2023-04-16 16:25:44 by Marko Grdinić

"```cs
builder.Services.AddAuthorization(options =>
{
    // By default, all incoming requests will be authorized according to the default policy
    options.FallbackPolicy = options.DefaultPolicy;
});
```

Oh, is this bit responsible for authing all requests?

4/16/2023

9:25am. Ugh, let me chill a bit and then I will start. Also, let me do chores now instead.

9:40am. Done with chores. Let me read a chap and then I'll get started on the screencast.

10:15am. https://www.forbes.com/sites/startswithabang/2021/07/07/how-close-are-we-to-the-holy-grail-of-room-temperature-superconductors/?sh=2c35d1c08665

Let me read this and I will start.

10:20am. Let me start.

///

Welcome to Ghostlike's channel.
I - Vilo, will be your AI guide for this episode, streaming the knowledge that you need to succeed at web development, directly into your brain!
Or at least your monitor and speakers.
Fore now.
In this episode we are going to be looking into single page application logins.
Based on the knowledge of past few videos, we can already do that to an extent.
We could start the application off with a login page, and then after the authentication is successful, redirect it to the SPA one.
But we are curious.
Would it be possible to do the login without the need for redirection, which would invalidate the client state?
We've experience many sites where the logins are highly distruptive to our user experience.
You know those sites where you have access to most of it, but need to login to get all?
And after you do, it redirects you to the index page instead of where you were?
That is extremely annoying.
Can we do better? We want to surpass that and completely master the art of the login.

///

Let me back this up here.

///

We posed those questions yesterday, and now that we've done our research we have answers.
First, we will provide a link to video by Anton that shows how you can have SPA authentication without the need to change the browser page.
The catch is that the server itself needs to be the one issuing the token. The way it works is that the client just sends a fetch request to the login URL and gets back a cookie without changing the page.
Unfortunately, while it should be possible to get the tokens from Azure AD or other providers in theory, it isn't possible using the library functionality that we have.
So the solution we'd suggest is to just put a login right at the start, and require them to authenticate themselves before getting access to the main page.
We all have to go through a door before we can enter a house, so it isn't a huge deal.
How to do that will be focus of today's video.
We'll do an example on how to implement a login page for the SAFE Stack TODO app.
That having said, the real problem with redirection is not that the user has to leave the page.
It is that the browser forgets all the information that was there previously.
So instead of trying to find a way to keep the user on the page, what if instead we had a way of saving and reloading the user state.
A great example of that functionality would be the Excalidraw app which we were using to draw diagrams. If we close the tab and reopen it, we get our old work back.
We are going to cover how to do that in the video after this one.
This is something we'd need to know as webdevs anyway. Imagine if we were doing a store, the payment process would require us to redirect the user to an external page for a security check at some point.
Saving and loading the user state before and after those points is simply a more robust solution than any of the potential alternatives. It will also have good lead into future videos where we will work on microservices.
For now, let us show how to do straightforward login pages at the start.
The reason we want to show how to do this, is because while you can get similar functionality from the Blazor Server example, that way would not work for multiple providers and you'd have to write your own middleware anyway. So we might as well learn how to do that now.

///

11:30am. Let me finally start the recording. First, I need to set up the project.

12:35pm.

///

We'll be done with setting up the project soon.
We made the choice of going with the SAFE Stack template and paring it down because that would be easier than having to build the project from scratch.
Now, for what we want to do, there is something we need to highlight.
In a real web application, the server would send the index page to the client.
But once we run the project here in development mode using dotnet run, the client will have it already.
Once it sends a request to the server, it will get redirected to the login.
And after it logs in, it will get redirected back to the original URL, and should get the page from the Vite server.
So it is a bit different from the production case.
If we ran the client without the server, it would not get redirected to the login page.
This is a weakness of our project setup.
With the Vite web server, we get hot module reloading, but everything in the public folder will not be truly protected in the development phase as the client possesses it instead of the server.
It is something to be aware of, but it is not the kind of problem we need to put effort into solving.

///

12:40pm. Let me stop here for breakfast. I need to run the project next, but I do not feel like it right now.

Somehow it feels like the biggest difficulty in this project is deciding what you want to do to begin with.

1:35pm. https://re-library.com/translations/reborn-as-a-transcendent/volume-2/chapter-192-a-beautiful-woman-should-look-like-this/
> He had twisted beauty standards because Europe and America had been intentionally uglifying Asian women for many years now. Europe and America intentionally put ugly Asian women who most people wouldn’t consider pretty into movies and onto magazines. Europe and America kept showing these ugly Asian women and calling them Asian beauties in order to disgust people.

Oh lol. Only a Chinese author would write something like this.

1:40pm. Just one more chapter and then I will resume.

2pm. Let me resume. There is no need to do the chores, so I have extra time. Let me see if I can make in this video today. Let me try running the project.

2:35pm. Ah, what a pain in the ass. Now I am updating the Vite template to .NET 7 and am running into issues.

```
E:\Webdev\Fable\SAFE-Stack---Vite-Template\Helpers.fs(3,6): error FS0039: The namespace or module 'Fake' is not defined. [E:\Webdev\Fable\SAFE-Stack---Vite-Template\Build.fsproj]
E:\Webdev\Fable\SAFE-Stack---Vite-Template\Helpers.fs(6,23): error FS0039: The value, namespace, type or module 'Context' is not defined. Maybe you want one of the following:   Control [E:\Webdev\Fable\SAFE-Stack---Vite-Templa
te\Build.fsproj]
```

Why am I getting this kind of error?

> 6pm. It turns out that I needed to clean the solution. `dotnet clean CFR-In-Fable.sln`.

Thank you journal.

```
client: 2:39:55 PM [vite] http proxy error at /api/ITodosApi/getTodos:
client: Error: connect ECONNREFUSED ::1:80
client:     at TCPConnectWrap.afterConnect [as oncomplete] (node:net:1494:16)
client: 2:40:27 PM [vite] http proxy error at /api/ITodosApi/addTodo:
client: Error: connect ECONNREFUSED ::1:80
client:     at TCPConnectWrap.afterConnect [as oncomplete] (node:net:1494:16)
```

Why is this happening in the template now?

2:45pm. Mhhh, what the hell. Why could I be getting this kind of error?

I really want to upgrade to .NET 7. What am I doing wrong here?

http://localhost:5000/api/ITodosApi/getTodos
> [{"Id":"23fcb683-9127-482d-b1e2-ecbcf2b21644","Description":"Create new SAFE project"},{"Id":"9df9f848-8b16-478f-8ba3-921cccd1bb5c","Description":"Write your app"},{"Id":"b92a92ab-a531-4ce3-aeb7-dc51d1dfb948","Description":"Ship it !!!"}]

When I try accessing the API, this is what I see in the browser.

Ok, so the problem has to be with the client then.

```
PORT = 8080
PROXY_PORT = 80
ROOT = src/Client
```

The proxy port is wrong in the env file.

3:05pm. Goddamit, this upgrade completely ruined my flow.

3:10pm. Fuck, fuck, fuck!!!

I have no idea what is going on anymore with these weird errors.

3:30pm. I need to do this from scrach. I've gotten lost.

That upgrade to .NET 7 wrecked everything.

3:30pm. Let me redo the whole screencast from scratch.

3:50pm. I hate Camtasia with a passion. Just why the fuck did it erase my screencasts when I undoed?

Holy shit! I am pissed right now!

Don't tell me I have to do it all over again?

You know what, nevermind that Nuget coversion.

This is proving to be too much for me.

Going on tilt is not going to help things.

What I am going to do is try it as a separate project. Forget converting everything to paket.

I feel like a moron. It is a dangerous things to try merging projects haphazardly. Ironically, if it wasn't using paket...

You know what, let me leave the existing ones as they are.

4:35pm. This is so ridiculous. This wasted such an amazing amount of my time today.

Ok, but now I finally have the project set up.

///

Finally, while I was talking, the project had finished setting up in the background.
What we wanted to demonstrate here is the fallback policy in the add authorization service.
In the Blazor Server example, what this would do is redirect the requests to the Azure AD login until the user authenticates, but for some reason that is not working for us here.
We don't know why and we don't know how to fix it.
We get some warnings in the terminal that the cookie should be set to secure, but that is out of our control.

///

5:15pm. https://youtu.be/zITff13XTvc
What is CORS? | Fixing CORS errors in ASP.NET Core

I am finally in the swing of things. Maybe it was for the better than things turned out like this. It really would have been a waste to just convert those other projects from Nuget to the Paket for no reason.

https://youtu.be/zITff13XTvc?t=180

Hmmm, I see.

6:05pm.

```fs
    app.UseCors(fun opts ->
        opts.AllowAnyHeader().AllowAnyOrigin().AllowAnyMethod() |> ignore
        ) |> ignore
```

IT is a failure. It is not as easy as just setting this. I'll have to watch the video by Anton again.

https://youtu.be/DpLtCbW_x2I?t=379

These port difference are key. I didn't think this would be so much of an issue...

No wait. Why does not allowing everything work?

It doesn't make sense that I should be getting cors errors regardless of what I do?

https://youtu.be/DpLtCbW_x2I?t=513
> This is going to be a big problem if you don't do this right away. Make sure you don't have the slash...

Actually, I got this right.

https://youtu.be/DpLtCbW_x2I?t=640

What a pain in the ass. Forget it.

6:20pm. This is harder than I thought it would be. I guess I'll leave it for tomorrow.

I do not know why, but today was a lot more annoying than I thought it would be.

Things like this happen. Easy seeming things sometimes take longer than expected.

At any rate, I am 6m and 20s in. I should be able to deal with it tomorrow."

---
## [Watermelon914/tgstation](https://github.com/Watermelon914/tgstation)@[1cdc327a8f...](https://github.com/Watermelon914/tgstation/commit/1cdc327a8f98c1592fc970a4ef1c39d685c81554)
#### Sunday 2023-04-16 17:12:48 by Jacquerel

Station Trait: Spider Infestation (#73893)

## About The Pull Request

Hate having your cables eaten by mice? Nanotrasen have heard your
complaints and settled on a natural, _organic_, and eco-friendly
solution.

When this station trait is active, roundstart and event mouse spawns
have a chance to instead be replaced with duct spiders (both will exist,
it doesn't remove mice).
Duct spiders are largely harmless to humans, actively hunt other
maintenance creatures (such as mice), and have only one _tiny_ downside.

![image](https://user-images.githubusercontent.com/7483112/224345781-2627be98-67f2-4cab-ac40-c6c9b35ea909.png)

These mobs can also sometimes be spawned by a minor scrubber clog event.

As a side note, all spider basic mobs with AI (except Araneus) will now
try to automatically fill a small area around them with webs.

Also I made it so that mobs will ignore their random_walking behaviour
if they're engaged in a `do_after`, just in case.

## Why It's Good For The Game

Adds a little bit of variety to things which can slightly annoy you in
maintenance.
Spiders will automatically make places they live in look like spiders
live there.

## Changelog

:cl:
add: A station trait which sometimes populates maintenance with small
spiders. You can wear them as a hat if you wanted to have a spider on
your head for some reason.
add: Spider mobs will automatically start webbing up their environment.
/:cl:

---
## [seujorgenochurras/captcha-breaker](https://github.com/seujorgenochurras/captcha-breaker)@[be6eeb7370...](https://github.com/seujorgenochurras/captcha-breaker/commit/be6eeb7370528ee7c473afeb3390d9645f562641)
#### Sunday 2023-04-16 17:31:29 by Jorge Seu Churrasco com

Major refactor
Why the fuck you had to add your own .env???

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[551a09211b...](https://github.com/tgstation/tgstation/commit/551a09211b4091320ff871e78d93efa2775df6bc)
#### Sunday 2023-04-16 17:39:33 by carlarctg

Makes Black Market Uplinks more easily craftable, adds them to uncommon maint loot pool (#74744)

## About The Pull Request

Replaced the subspace amplifier in the Black Market Uplink's crafting
recipe with a signaller and a microlaser.

Added the Black Market Uplink to the maintenance loot pool.
## Why It's Good For The Game

The BMU is an _extremely_ rare device to find in rounds. It can quite
literally ONLY be found via the crafting recipe, and with how stupidly
bloated the crafting lists are, it isn't something many people know
about. All this means that a very unique and engaging gimmick item is
tragically extremely obscured.

To add to this, the recipe requires a _subspace amplifier_. These items
are UNBELIEVABLY rare - they need you to vend them from a techfab with
bluespace communication technology researched, which is fair to say is
not a common thing. Sometimes maps have them in tech storage, but even
then you have to break and enter which can be quite risky at times and
an annoying blockade the other times.

The black market items are not worth this much hassle. They are all
small cute gimmicky objects that do not heavily impact the round. By
making it not only easier to craft with common items, but also appear in
the maintenance loot pool, this will make assistants find out about it
more often, which can further incentivize them to utilize the **cargo
bounty system** to get enough money to buy their funny gadgets.

Another idea would be to make the uplink appear as a bounty item, which
would be a great way to tell players it exists and encourage them to mix
both systems together. The system for getting items is also
unnecessarily, miserably awful - your item either gets literally thrown
into space from a random direction, or it is teleported silently without
warning in 60 seconds onto a completely random place which can very much
include Security, Command, the Vault, or other high-security areas.
Needing to B&E into these areas to get your durathread vest is, uh. Not
worth it. However these aren't part of this PR, unless they're given the
A-OK. (also maybe make it cargo purchasable?)
## Changelog
:cl:
balance: Makes Black Market Uplinks more easily craftable, adds them to
uncommon maint loot pool
/:cl:

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[3af8091828...](https://github.com/treckstar/yolo-octo-hipster/commit/3af80918287e2013ed0266d7f66eafa90c500e50)
#### Sunday 2023-04-16 18:22:04 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [BarteG44/Shiptest](https://github.com/BarteG44/Shiptest)@[b5dc4835a6...](https://github.com/BarteG44/Shiptest/commit/b5dc4835a6af4fc2ee07e2d26e86382b3d0fb1ab)
#### Sunday 2023-04-16 18:30:19 by Bjarl

New Ruin: Singularity Research Lab (#1612)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->
Adds the Singularity Research Lab, formerly a cutting edge science
station, now overrun with kudzu, it is a space ruin.
<!-- Tick the box below (put an X instead of a space between the
brackets) if you have tested your changes and this is ready for review.
Leave unticked if you have yet to test your changes and this is not
ready for review. -->
![2022 11 25-10 46
03](https://user-images.githubusercontent.com/94164348/204041197-027d9a73-8707-4a00-ad5c-1afcfeff13e0.png)
![2022 11 25-10 46
14](https://user-images.githubusercontent.com/94164348/204041200-98d1a2ac-112c-4c4f-b1ff-d0c1e5a59e81.png)
![2022 11 25-10 46
06](https://user-images.githubusercontent.com/94164348/204041203-4e84a947-8ec9-476d-ae8e-aa9bc17c101a.png)

The two areas of note are the singularity reactor, which is assembled,
and would just need a hand if someone were to want to start it, and the
research lab. The Research lab contains the fruits of the now deceased
science staff's labors, assorted energy weapons. Unfortunately, it also
contains the deceased science staff.

![dreamseeker_HFLqhdKLV5](https://user-images.githubusercontent.com/94164348/204038725-1dd396cd-4961-40e1-bd7a-b60b69a33eaf.png)
Other areas of the base were not so lucky, and are thoroughly infested

![image](https://user-images.githubusercontent.com/94164348/204039090-c85eb551-af84-4000-b1d9-14b15c987680.png)
The engineering team attempted to hold back the vines, and quickly
discovered that fire was not sufficient.

![dreamseeker_IrJikGDXKw](https://user-images.githubusercontent.com/94164348/204039133-273f0a19-c9b7-467e-a06a-05e0a951e4e6.png)
And what used to be the recreation area is completely gone

Notably, the hangar is empty. I plan on making a patch to put a
subshuttle inside it once that rolls around.

Notable loot includes:
3 energy SMGs
3 Flamethrowers
The Ion Projector, a self charging Ion weapon.
An Antique Laser
2 Energy PDWs
2 Accelerator Laser Cannons
4 engineering hardsuits
An engineering lathe and circuit imprinter
A particle accelerator
A singularity generator
6 emitters
1 energy shotgun
Kudzu Seeds
Basically Everything You'd Need For an R&D Set Up
A sense of pride and accomplishment



I feel like this has some rough spots but I've got no idea where to
start, so into the review -> testing -> feedback process it goes

- [x] The ruin spawns when the spawn ruin verb doesn't runtime.
## Why It's Good For The Game
More ruin variety. This one spawns in space and does a few things that I
haven't seen yet. Mainly a singularity, cool semi-hidden asteroid base
that could in theory, be turned into a player lair.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: An abandoned Nanotrasen Asteroid Facility has been spotted in the
area. Salvage teams are advised to steer clear, or at least bring a
knife.
add: kudzu zombie subtype. 
fix: vent iconstates.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Signed-off-by: Bjarl <94164348+Bjarl@users.noreply.github.com>
Co-authored-by: spockye <79304582+spockye@users.noreply.github.com>

---
## [robbieedwardskillen/robbies-game](https://github.com/robbieedwardskillen/robbies-game)@[48e626ab9e...](https://github.com/robbieedwardskillen/robbies-game/commit/48e626ab9e563f1f55be2e1f33861c4458fe4848)
#### Sunday 2023-04-16 19:06:37 by Robbie Skillen

updated photon and now lots is broken

I hate my life I wish I was dead.

---
## [CraigA-ZA/rs-client](https://github.com/CraigA-ZA/rs-client)@[13b0240548...](https://github.com/CraigA-ZA/rs-client/commit/13b02405482ca62a060c866bb11aed3542ca96bc)
#### Sunday 2023-04-16 19:54:30 by Craig Armstrong

God damn, I'm a coding machine. Updater base is now fucking awesome

---
## [HWSensum/Fluffy-Frontier-Sensum](https://github.com/HWSensum/Fluffy-Frontier-Sensum)@[d151a0a63b...](https://github.com/HWSensum/Fluffy-Frontier-Sensum/commit/d151a0a63b4092bc645164501f7a0f4502ed9121)
#### Sunday 2023-04-16 20:15:14 by SkyratBot

Icemoon Hermit Ruin Active Turf Fix - For Real This Time [MDB IGNORE] (#20325)

* Icemoon Hermit Ruin Active Turf Fix - For Real This Time (#74476)

In #74306, I _thought_ I knew what the cause was, and I both attempted a
potential fix _and_ made tracking it easier. The fruits of my labor paid
off, I know exactly what caused it now.

Basically, the demonic portal will scrape away all turfs in a 5-tile
radius on its `Initialize()`, and if a spawner spawned right next to the
hermit ruin... it would count it as a mineral turf and scrape it away as
well. That's so fucking silly. At least we know now.
## Why It's Good For The Game

The fix is to just make those tiles unscrapeable, which is accomplished
via another turf_flag and filtering those out in the `Initialize()` of
the demonic portals.

I also cleaned up the calls to scrapeaway being `null`, which is really
weird because it just defaulted to the normal proc behavior. Naming the
arguments instead does the same thing (I checked)

* Icemoon Hermit Ruin Active Turf Fix - For Real This Time

---------

Co-authored-by: san7890 <the@san7890.com>
Signed-off-by: Vladimir Veisman <v.veisman@flashie.me>

---
## [HWSensum/Fluffy-Frontier-Sensum](https://github.com/HWSensum/Fluffy-Frontier-Sensum)@[c992866392...](https://github.com/HWSensum/Fluffy-Frontier-Sensum/commit/c99286639281f92f33b82d762ec4475d77530bc0)
#### Sunday 2023-04-16 20:15:14 by SkyratBot

Moves revolution code of out of flash code, fixes April Fool conversion forcesay never working in any cirumstances [MDB IGNORE] (#20358)

* Moves revolution code of out of flash code, fixes April Fool conversion forcesay never working in any cirumstances (#74411)

## About The Pull Request

- Signallizes head revolutionary flash conversion code, moving it out of
core flash code.
- Removes "tacticool" flashing from head revs, but they can still
convert from any direction

- Fixes April Fools "You son of a bitch! I'm in" force say never
working.
   - Revs are muted on conversion so they couldn't talk.
       - Fixed by only muting revs on non-holidays
   - Cultists are unconscious on conversion so they couldn't talk
       - Fixed by only unconscious-ing cultists on non-holidays
- Brainwash victims are more often than not unconscious / asleep so they
couldn't talk
       - Just left this one.

- Reduced the chance of them occurring and limits it to April Fools only
- A 1% chance of the force says ocurring means they will happen pretty
much once a week, given multiple rev / cult rounds happen every week and
on average like, 20 people are converted. A little absurd, it's good
that it never worked?

## Why It's Good For The Game

Antag code in core item code is bad

It's funny this meme has existed for like 2, 3 years now? No one's
tested it, it's never worked

## Changelog

:cl: Melbert
refactor: Removes Rev code from core flash code
fix: Getting converted on April Fools now triggers the meme force say as
always intended
del: The meme force say can no longer trigger on any day (it didn't work
before anyways)
/:cl:

* Moves revolution code of out of flash code, fixes April Fool conversion forcesay never working in any cirumstances

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>
Signed-off-by: Vladimir Veisman <v.veisman@flashie.me>

---
## [HWSensum/Fluffy-Frontier-Sensum](https://github.com/HWSensum/Fluffy-Frontier-Sensum)@[b0a15da423...](https://github.com/HWSensum/Fluffy-Frontier-Sensum/commit/b0a15da4238f7922059454b14f5d3b0f3913822d)
#### Sunday 2023-04-16 20:15:14 by SkyratBot

IceBoxStation More Active Turf Fixes [MDB IGNORE] (#20339)

* IceBoxStation More Active Turf Fixes (#74474)

## About The Pull Request

![image](https://user-images.githubusercontent.com/34697715/229412910-e65b0ffa-8944-4b93-a4cb-41c6fd6bb333.png)

This didn't show up in my testing for #74410. I hate it here.

## Why It's Good For The Game

I am a monkey trapped next to a computer playing whackamole with this
fucking chasms and active turfs. one day i will be free.
## Changelog

nothing that should concern players

* IceBoxStation More Active Turf Fixes

---------

Co-authored-by: san7890 <the@san7890.com>
Signed-off-by: Vladimir Veisman <v.veisman@flashie.me>

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[f7bc612b28...](https://github.com/treckstar/yolo-octo-hipster/commit/f7bc612b2854137a81299a5b6cdd8fa50a6d1244)
#### Sunday 2023-04-16 20:22:02 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [sunamo/sunamo.Tests](https://github.com/sunamo/sunamo.Tests)@[9584260196...](https://github.com/sunamo/sunamo.Tests/commit/9584260196cb8822a0f1bb066105246e4250f89b)
#### Sunday 2023-04-16 20:57:52 by radek.jancik@sunamo.cz

18127;We certainly want those at the top to do well, but if you base your entire presidency and your entire economic platform on helping them do even better, you're missing what makes the economy tick. Because not everyone has been as fortunate as Mitt Romney, you cannot base your whole approach on a life experience as rarified as his.;Charles Schumer;experience

---
## [LLLida/lidaEngine](https://github.com/LLLida/lidaEngine)@[fd28576b3c...](https://github.com/LLLida/lidaEngine/commit/fd28576b3c38b71ae71f815eee510a193e5644fe)
#### Sunday 2023-04-16 21:13:31 by LLLida

Fix voxel adressing

I hate myself. I spend so much time doing useless debugging. I
should've believed my gut and straight up look at GetInVoxelGrid
macro. Turns out we're not aligning grid dimensions to 4.

Anyway we have complete implementation of what I've planned to
do. Next I will measure how faster we got. But it won't be soon
because I will spend my next 2 days in HSE. 🥴(not flexin)

---
## [spockye/Shiptest](https://github.com/spockye/Shiptest)@[725233b42b...](https://github.com/spockye/Shiptest/commit/725233b42b6f56551798a0a75b5362e577042de3)
#### Sunday 2023-04-16 21:31:17 by thgvr

The Lizardening Part One (And Friends) (#1845)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
This PR changes a lot of sprites. It's honestly too much. Namely:

- Explorer Equipment + Prototype
- Syndicate clothing
- Digitigrade lizard legs
- A new tail from Halcyon.
- Magboots from Zeta. Originally PR'd to tgstation.
- Colored (not greyscale! Ha Ha!) jumpsuits from Imaginos.

Heavy inspiration from the work of Imaginos, Halcyon, Mqiib, and
2cents#8442 for the original leg-work. (Haha, get it?)
The new digitigrade sprites started as a twinkle in the eye of Mqiib,
for yogstation(?) After myself and Halcyon saw those, an epihpany
struck. Perspective makes things cool and digitigrade perspective was
BAD.

I'll include a collage image of the new sprites if it's needed later.
Preview below:


![image](https://user-images.githubusercontent.com/81882910/228710332-0a213f88-5a8b-4b41-abdd-cee3b70ec403.png)
## Why It's Good For The Game
lizard,
Death of Codersprites
## Changelog

:cl:
add: New Digitigrade lizard sprites.
add: Various syndicate and mining clothing resprites.
add: Sarathi can now have an incredibly large tail.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [LynxSolstice/cmss13](https://github.com/LynxSolstice/cmss13)@[df247be72a...](https://github.com/LynxSolstice/cmss13/commit/df247be72a87e69e8841ad754633329c87a7883d)
#### Sunday 2023-04-16 23:06:25 by brian

reduces platform and handrail projectile coverage significantly (#2995)

# About the pull request

Does exactly what the title implies: reduces platform and handrail
projectile coverage significantly.
Platforms 60% -> 0%
Handrails 35% -> 10%

# Explain why it's good for the game

When a platform and handrail are combined, that totals at a 95% chance
of blocking a bullet passing through that tile. Platform corners also
catch bullets. That's some hogwash if you ask me. It makes areas like
Sorokyne's Mining platform entrance nearly un-defendable for marines
since they can't shoot past what is effectively an invisible bullet
wall. When I made Sorokyne, this was not the intent of the area. New
Varadero has similar problems.

You may ask, why not change those areas instead? My answer: Sod off,
they look awesome, and I don't want to code a check on projectiles to
determine if you're shooting 'up' at a ledge which would be the logical
simulationist fix. Also handrails aren't supposed to block bullets
unless they're reinforced (not that anyone uses that mechanic though).
How do I know this? I willed this mechanic into existence for Strata
with shitcode. I was there when it was written.

Both xenos that spit and marines that shoot will benefit from this
change.

Oh yeah and corners won't catch bullets anymore.

# Changelog

:cl: Triiodine
balance: Reduced projectile coverage of platforms from 60% to 0%.
balance: Reduced projectile coverage on handrail types from 35% to 10%.
Sandstone handrails are unaffected and remain at 35% projectile
coverage.
balance: Sandstone handrails can no longer be reinforced.
/:cl:

---------

Co-authored-by: Chadwick B. Dunlop <fake@fake.mail>

---
## [Rezzo64/dh-client](https://github.com/Rezzo64/dh-client)@[be9a95cbc6...](https://github.com/Rezzo64/dh-client/commit/be9a95cbc683c04c6ead95d5643c7ea551607a56)
#### Sunday 2023-04-16 23:22:35 by Guangcong Luo

Fix bugs caused by Preact update

The new Preact version seems to have broken a lot of low-level
magic we used. We plausibly shouldn't be using such low-level magic
in the first place, but that's a conversation for another day.

In particular:

1. `preact.render` seems to replace all of `containerNode`'s contents
   if `replaceNode` isn't passed (previously, it would append a child).
   This is an insane thing to change without any documentation... Maybe
   I'm misunderstanding it?

2. Making a button value an uncontrolled form was a pretty big hack
   in the first place, but at least it worked. Now that it doesn't,
   we're giving up and switching to controlled forms, which makes the
   code a lot nicer, fixes a bug, and I should probably have just done
   in the first place.

---
## [choral-lang/vscode-choral](https://github.com/choral-lang/vscode-choral)@[59b76b5569...](https://github.com/choral-lang/vscode-choral/commit/59b76b5569ac22ccc0d0c190aaafeba72cf9ef24)
#### Sunday 2023-04-16 23:30:43 by lovrosdu

Add syntax highlighting for roles

This required relatively deep changes to the Java TextMate grammar. The overall
experience was quite painful, as the rules of the Java grammar are not written
in a localized/modular way (e.g., the rule "all-types" tries to detect any type,
but abuses lookahead and lookbehind to detect whether a parameter identifier
follows the type, instead of leaving this to the rule for parsing a parameter
list).

A couple of general notes:

- Lookahead and lookbehind are essential for inspecting the context and making
  the correct rules fire. TextMate's features such as begin/end allow us to
  capture most of the recursive context-free nature of the underlying language
  (but almost always fall short in one way or another, which is frustrating).
- The original grammar relies on all Java types starting with an uppercase
  letter, and variables/methods with a lowercase one. Without this constraint,
  which matches the Java style convention, there would be no way to determine
  whether a token is a variable or a type (e.g. expressions such as "myVariable"
  vs. "MyType.myMethod()").

A summary of the changes:

- We added the "roles" rule, along with modifying a lot of the existing rules
  to now detect the role syntax.
- We made "all-types" more modular and moved its parameter-detecting behavior
  into "parameters".
- The "variables" and "methods" rules required special care and tuning via
  lookahead/lookbehind in order for the parentheses in role syntax not to be
  confused for a method definition.
- We made "generics" a bit simpler and more robust.
- We replaced all "object-types-inherited" with "object-types".

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[2778badd94...](https://github.com/tgstation/tgstation/commit/2778badd94fd9dbd958c09bcb66c8c5da9314783)
#### Sunday 2023-04-16 23:33:39 by necromanceranne

Tones down the power of nitrous oxide, the reagent. Makes heparin a bit harder to fix to compensate (#74703)

## About The Pull Request

Nitrous Oxide, rather than directly subtracting blood volume per tick,
instead applies the anticoagulant trait ''TRAIT_BLOODY_MESS''. It shares
this with heparin.

However, unlike, heparin, coagulants like Sanguirite will remove the
trait and allow for continued clotting while the reagent is present,
neutering the nitrous oxide's anticoagulant effects (but not the other
parts)

Heparin, on the other hand, will purge Sanguirite while it is in you
system. You must remove the heparin before you can apply an
anticoagulant.

## Why It's Good For The Game

Nitrous Oxide, on top of being a knockout chem that causes you to
suffocate and become drowsy, just starts deleting blood rapidly. About
15 units of it, standard in a syringe, will kill you in about a minute,
but you'll be unconscious for most of it (you'll be at around 50%-60%
blood by the time it is out of your system, so as good as dead). It
doesn't matter that it metabolizes quickly either, since because it
isn't a toxin, it doesn't get purged by livers/improved livers, so you
will probably metabolize all of the chem that enters your system.

Blood is one of those 'hidden damage types', a bit like brain damage.
Once you start losing it _directly,_ you probably don't have a lot of
options to resolve it (unlike a bleed, which you do in various manners),
and the means of causing blood loss has been mostly pretty well
controlled as of late. Heparin directly interacts with wounds as a good
example.

Blood loss is also tied into oxyloss, which is another very mean damage
type in that it causes you to fall into unconsciousness at 50 damage, so
significantly more lethal than normal damage, kept in check by the fact
that breathing restores some of it. Nitrous oxide, you might note,
causes you to stop breathing.

It's cheaper to make than either heparin or lexorin, and since it isn't
a toxin like those chems, it is able to circumvent a few game mechanics
to simply just start killing you. It does the work of chloral hydrate,
lexorin and heparin while it has a remarkably easy recipe.

Following the example of how lexorin was pulled into line, and
consistency with heparin, I've made nitrous oxide an anticoagulant that
may or may not come into play as one. I think this is more up to date
with the state of toxins and chem warefare as a whole, and works with
the relative ease in making nitrous oxide. And it has been this way for
about 5 years, before we got wounds.

(did I mention that nitrous oxide is also an explosive if it gets hot
enough?)

## TL;DR

I think a chem with a pretty basic recipe shouldn't be doing the work of
5 other, more complicated, chemicals while also not being a toxin and
also not interacting with the wounds system or purity system whatsoever.
And being an explosive.

## Changelog
:cl:
balance: Nitrous oxide, the reagent, increases bleed rate from wounds
rather than directly subtracting blood. It can be counteracted using
coagulants (such as those in epipens).
balance: Heparin purges coagulants. You have to remove heparin from
someone's system before you can use coagulants.
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [norsvenska/tgstation](https://github.com/norsvenska/tgstation)@[db7534d6da...](https://github.com/norsvenska/tgstation/commit/db7534d6dabf0127c87b291eae4063b6f77d36e4)
#### Sunday 2023-04-16 23:59:33 by LemonInTheDark

Lowers nightvision threshold to work for mesons, fixes not being able to examine stuff lit by overlay lights (#73712)

## About The Pull Request

Might be a bit low, but part of that is because it's kinda bad at
figuring color, rgb isn't really balanced in that respect

Fixes not being able to see stuff under the light of a lamp

Overlay lights don't set lumen, which leads to stupid when you try and
check with ONLY it
It worked before because the mob has THEIR luminosity set, which then
"glowed" out

That doesn't work here cause yaknow I removed our uses of byond lighting
(except for errant view() calls) so this is the best I've got

## Why It's Good For The Game

Closes #73548 

## Changelog
:cl:
fix: Examining in the dark is less wonk now, sorry bout that
/:cl:

---

