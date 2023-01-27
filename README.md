## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-01-26](docs/good-messages/2023/2023-01-26.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,093,853 were push events containing 3,133,088 commit messages that amount to 249,005,685 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 38 messages:


## [agraef/purr-data](https://github.com/agraef/purr-data)@[d8d940243e...](https://github.com/agraef/purr-data/commit/d8d940243ecb3470d94b21c5805c212670b2da63)
#### Thursday 2023-01-26 00:05:07 by Albert Gräf

Windows packaging: GH-friendly OutputBaseFilename.

This makes my life less miserable when doing releases on the GH mirror,
because I don't have to manually edit the installer filenames before
uploading any more.

GitHub doesn't like blanks in upload file names, using dashes instead
makes uploading much easier and eliminates the need to zip the installer
before uploading. We also include a proper cpu architecture designation
(x86 or x86_64) in the output file name in lieu of the '(64 bit)' suffix
which causes trouble in GH uploads as well, because of the parentheses.

Note that this shouldn't affect the Gitlab CI since it looks for a
'Purr*.exe' build artifact, which will still match the package name.

---
## [apify/crawlee](https://github.com/apify/crawlee)@[a95e6676b2...](https://github.com/apify/crawlee/commit/a95e6676b2e3574c8db3083c661dc09a5405751e)
#### Thursday 2023-01-26 00:21:12 by Martin Adámek

chore: switch to yarn v3 (#1752)

NPM got somehow [broken more than
usual](https://github.com/apify/crawlee/actions/runs/3997285915/jobs/6873858419)
and its no longer possible to install the dependencies in CI. We were
struggling with NPM for quite some time (especially after we moved to
turborepo). I’ve been advocating for yarn since my first days here, been
using it for last ~5 years on a daily basis and it never did anything
wrong to me, so I hope this will be the right step and a smooth
transition for all the collaborators.

What to expect? Since we require node 16, we can leverage `corepack`, a
new tool shipped with newer node versions (btw developed by yarn
maintainers). This means you just need to run `corepack enable` and yarn
should be available in your workspace. In case of some problems, you can
try running `corepack prepare yarn@stable --activate`, but it shouldn’t
be needed. Note that we use `corepack` instead of commiting yarn binary
to the git repo - that is the reason why `.yarn` folder is gitignored.

Initially we will start with a conservative setup, using a node linker,
so there will be the good `node_modules` folder we are all used to. I’d
like to experiment with the advanced features as well, mainly in the
project templates, as it could greatly improve the build times (we could
even skip the install step completely).

With that said, we will be still using NPM inside our E2E tests, to be
sure the project can be safely installed with NPM. This change should
affect only the collaborators, not our users. Ideally we should test
other package managers via CI too, so we are sure `pnpm` works as well,
or maybe even `bun`.

Few API differences and quality of life improvements yarn brings:
* `npm install` -> `yarn`
* `npm install xxx` -> `yarn add xxx`
* `npm run ...` -> `yarn …`
* `npx …` -> `yarn …`
* no need to deal with the `--` issue from `npm run` (propagating CLI
params to the script)
* powerful caching and _sane_ lockfile format

---
## [heyitsbench/azerothcore-wotlk](https://github.com/heyitsbench/azerothcore-wotlk)@[ef949f9ff0...](https://github.com/heyitsbench/azerothcore-wotlk/commit/ef949f9ff0a89e837c67258d7e199da1706bc438)
#### Thursday 2023-01-26 00:37:41 by ICXCNIKA

fix(DB/Locale): deDE fix request items texts #02 (#14615)

Process of translation: only original sources of deDE texts by
researching multiple sources, reverse translation by searching for
related quest items/NPCs and using these names to reconstruct a proper
translation.

This fixes the terms

Coldtooth-Mine (Eisbeißermine), Doomhammer (Schicksalshammer), Fizzle
(Zischel), Fizzledowser (Rutenwünschels), Fizzlebub (Zischelbub),
Burning Blade (Brennende Klinge), Ashenvale (Eschental),
Bloodscalp/s/stamm (Blutskalpe, Blutskalpstamm),
Darkspeartrolle/Darkspears/Darkspearstamm (Dunkelspeere,
Dunkelspeertrolle, -stamm), Moonglade (Mondlichtung), Starblaze
(Sternenschauer), Shadowglen (Laubschattental), Darrowshire (Darroheim),
Booty Bay (Beutebucht), Ratchet (Ratschet), Dizzywig (Flunkerblick),
Hearthglen (Herdweiler), Chillwindspitze (Zugwindspitze), Stormrage
(Sturmgrimm), Stormpike (Sturmlanze/n), Ironforge (Eisenschmiede),
Thunderhorn (Donnerhörner), Steamboil (Kesseldampf), Twilight-Hammer,
-klan (Schattenhammer/Schattenhammerklan), Fathom-Kern (Tiefenkern),
Blackfathom Deeps (Tiefschwarze Grotte), Blackrock-* (Schwarzfels-*),
Hawkwind (Falkenwind), Feathermoon (Mondfeder), Moonrage (Mondzorn),
Firemane (Feuermähne), Searingblade (Sengende Klinge), Ragefireabgrund
(Flammenschlund), Ironbands Areal (Eisenbands Lager), Zandalar
(Zandalari), Southshore (Süderstade)

for quest progress/request text entries for the deDE localisation with
proper casus/declension (these are not proper translated names of
locations/NPCs that have been left over by Blizzard since their language
localisations in TBC in 2006 and onward).

Added missing progress/request text entries for 308, 311, 417, 1644,
1787, 5059, 5060, 5721, 6004, 6023, 6025, 6187, 8042, 8043, 8044, 8046,
8047, 8048, 8050-8079, 8102, 8107, 8108, 8111, 8112, 8113, 8117, 8118,
8142, 8143, 8147, 8183-8195, 8238, 8239, 8240, 8243, 8246, 8860, 9594,
9692, 9707, 10414, 10415, 10919, 11451. (A lot of them are
Zandalari/Zul'Gurub related quests.)

Replaced post-Cataclysm progress/request text entries for 933, 935,
6387, 7383.

Fixed a wrong $R with plain text at progress/request text for 9147.

Added missing female gender equivalent to 6391.

(There are probably more changes in the file that aren't further
explained here as it was hard to keep track of everything. If you think
I made a mistake or have questions please contact me directly.)

<!-- First of all, THANK YOU for your contribution. -->

## Changes Proposed:
-  Fixing a lot in the quest_request_items_locale table.

## Issues Addressed:
<!-- If your fix has a relating issue, link it below -->
- Fixing some of the tasks in
https://github.com/azerothcore/azerothcore-wotlk/issues/14244
Referring to my other two bug reports from CC Github:
- https://github.com/chromiecraft/chromiecraft/issues/4697
- https://github.com/chromiecraft/chromiecraft/issues/4745

## SOURCE:
<!-- If you can, include a source that can strengthen your claim -->
- Read the text on top.

## Tests Performed:
<!-- Does it build without errors? Did you test in-game? What did you
test? On which OS did you test? Describe any other tests performed -->
- Not tested.


## How to Test the Changes:
<!-- Describe in a detailed step-by-step order how to test the changes
-->
All of the changes are to reward texts of quests, can be tested by
completing quests or simply reviewing the changed file.

## Known Issues and TODO List:
<!-- Is there anything else left to do after this PR? -->

- [ ]
- [ ]

<!-- If you intend to contribute repeatedly to our project, it is a good
idea to join our discord channel. We set ranks for our contributors and
give them access to special resources or knowledge:
https://discord.com/invite/DasJqPba)
Do not remove the instructions below about testing, they will help users
to test your PR -->
## How to Test AzerothCore PRs
 
When a PR is ready to be tested, it will be marked as **[WAITING TO BE
TESTED]**.

You can help by testing PRs and writing your feedback here on the PR's
page on GitHub. Follow the instructions here:

http://www.azerothcore.org/wiki/How-to-test-a-PR

**REMEMBER**: when testing a PR that changes something **generic** (i.e.
a part of code that handles more than one specific thing), the tester
should not only check that the PR does its job (e.g. fixing spell XXX)
but **especially** check that the PR does not cause any regression (i.e.
introducing new bugs).

**For example**: if a PR fixes spell X by changing a part of code that
handles spells X, Y, and Z, we should not only test X, but **we should
test Y and Z as well**.

---
## [lessthnthree/tgstation](https://github.com/lessthnthree/tgstation)@[5e80257423...](https://github.com/lessthnthree/tgstation/commit/5e802574231c9c6fe835c40b55f2c8aa9f1c68b4)
#### Thursday 2023-01-26 01:05:44 by Jeremiah

Refactors crew records (#72725)

## About The Pull Request
I have attempted or otherwise started this project at least 4 times. I
am sick of it being on my calendar. The code needs it. I need it.

- This makes crew records a proper datum rather than assigning
properties record.fields.
- General, medical, and security records are merged.
- Did some slight refactoring here and there for things that looked
obvious.
- Wanted states are now defined (and you can suspect someone through
sechud)
- pAI (unrelated but annoying) had some poorly named exported types that
i made more specific
- Job icons are moved back to the JS side (I wanted to get icons for
initial rank without passing trim)

<details>
<summary>previews</summary>

Editable fields & security console

![CM6d74brnC](https://user-images.githubusercontent.com/42397676/213950290-af6cfd76-eb8b-48e9-b792-925949311d9a.gif)

Medical records

![bFJErsvOaN](https://user-images.githubusercontent.com/42397676/214132534-59af1f8c-9920-4b51-8b27-297103649962.gif)

Look and feel of the more current version

![cxGruQsJpP](https://user-images.githubusercontent.com/42397676/214132611-0134eef0-e74c-4fad-9cde-328ff7c06165.gif)

</details>

## Why It's Good For The Game
TGUI'd some of the worst UIs in the game.
Creating new records is made much simpler. 
Manifest_inject is made readable.
Probably bug fixes

## Changelog

:cl:
refactor: Crew records have been refactored.
refactor: Medical records -> TGUI
refactor: Security records -> TGUI
refactor: Warrants console -> TGUI
qol: Players are now alerted when their fines are paid off.
qol: Cleaned up sec hud examination text.
qol: Adding and deleting crimes is easier.
qol: Writing crimes in the console sets players to arrest.
qol: You can now mark someone as a suspect through sec hud.
/:cl:

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [VladinXXV/tgstation](https://github.com/VladinXXV/tgstation)@[5250b1fcc6...](https://github.com/VladinXXV/tgstation/commit/5250b1fcc6aca1aa6d6b0f9ec81ce6ad5fe2fa03)
#### Thursday 2023-01-26 01:46:40 by san7890

Captain's Spare ID Safe Can Only Hold ID Cards (#72584)

## About The Pull Request

I've personally seen this strategy play out the exact same way on more
than one occasion in an higher frequency lately (I've never played as
either side, just witnessed it)- and it always just seems to be an abuse
of a skewed in-game mechanic. So, this PR makes it so that you can only
put IDs into the spare ID safe. Nothing else.
## Why It's Good For The Game

I think this balance change is needed because it really sort of ruins
what I like about nuclear operatives, having to run around and stay
fluid for whatever the nuclear operatives could have, not "HAHA WE WILL
PUT IT IN OUR (NEARLY) IMPENETRABLE SAFE THAT THEY WILL NEED TO USE A C4
DIRECTLY ON AND JUST END UP PLAYING BLOONS TOWER DEFENSE SIX AS WE AWAIT
THOSE RED FUCKS TO ARRIVE". I miss when it would be fun to inject it
into a monkey who could crawl around vents, put it in a disposals loop
around the station to keep the nukies on a wild goose chase, or just
holding your ground in the brig and retreating if they batter you down.
It's just a very OP location in a very OP place with lots of warranted
OP armor for it's intended use case, which is not really being followed
by putting the all-important disk in the safe.

It's just very strong overall due to how protected-from-damage the spare
ID safe is, and I don't really like the fact that this is emerging as a
new "meta gameplay" (even used when there aren't any nuclear
operatives), it just sullies the different variety of ways you can
defend yourself against nuclear operatives when there appears to be
**the clear choice**. I don't like that concept where you can have a
strategy so good that you _shouldn't_ do it.

Also, it's an _ID Safe_. Not a disk safe.
## Changelog
:cl:
balance: Due to materials costing a lot more than ever, Nanotrasen's
Spare ID Safe Supplier have cut down on the space inside of the ID Safe,
meaning you can only cram in things as thin as an ID Card.
/:cl:

---
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[f1fdedd392...](https://github.com/pytorch/pytorch/commit/f1fdedd39287e78f1a35e31dc1e98db2c3983090)
#### Thursday 2023-01-26 02:30:29 by Brian Hirsh

Update base for Update on "add torch.autograd._set_view_replay_enabled, use in aot autograd"

tldr; this should fix some minor perf regressions that were caused by adding more as_strided() calls in aot autograd.

This PR adds a new context manager, `torch.autograd._set_view_replay_enabled()`.

Context: AOT Autograd has special handling for "outputs that alias graph intermediates". E.g. given this function:

```
def f(x):
    y = torch.mul(x, 2)
    out = y.view(-1)
    return out
```

AOT Autograd will do the following:

```
def fn_to_compile(x):
    y = torch.mul(x, 2)
    out = y.view(-1)
    # return the graph intermediate
    return y, out

compiled_fn = compile(fn_to_compile)

def wrapper(x):
    y, out = compiled_fn(x)
    # regenerate the alias of the graph intermediate
    return out._view_func(y)
```

What's annoying is that `out._view_func()` will result in a `.as_strided` call, because `out` is an ordinary runtime tensor. This (likely?) caused a perf regression, because when running the backward, out `as_strided_backward()` is slower than our `view_backward()`.

In this PR, I added some TLS for instructing autograd to do view replay instead of as_strided, even when given a normal tensor. I'm definitely interested in thoughts from autograd folks (cc albanD soulitzer). A few points that I want to bring up:

(1) One reason that this API seems generally useful to me is because of the case where you `torch.compile()` a function, and you pass in two inputs that alias each other, and mutate one of the inputs. Autograd is forced to add a bunch of as_strided() calls into the graph when this happens, but this would give users an escape hatch for better compiled perf in this situation

(2) To be fair, AOT Autograd probably won't need this TLS in the long term. There's a better (more complicated) solution, where AOT Autograd manually precomputes the view chain off of graph intermediates during tracing, and re-applies them at runtime. This is kind of complicated though and feels lower priority to implement immediately.

(3) Given all of that I made the API private, but lmk what you all think.

This is a followup of https://github.com/pytorch/pytorch/pull/92255.




[ghstack-poisoned]

---
## [SyncIt21/The-TG-Station-Fork](https://github.com/SyncIt21/The-TG-Station-Fork)@[10a344bde0...](https://github.com/SyncIt21/The-TG-Station-Fork/commit/10a344bde0d48fb250dcb7a9eb4a1e98b9bb6df5)
#### Thursday 2023-01-26 04:35:53 by Time-Green

External Organ Rework: new bodypart_overlay system (#72734)

Bodypart overlays are now drawn by the new /datum/bodypart_overlay
datum.

External organs no longer draw anything and instead add a special
/datum/bodypart_overlay/mutant to the bodypart, which draws everything

Makes it way easier to add custom overlays to limbs, since the whole
system is now modularized and external organs are just one
implementation of it

I haven't moved anything but external organs to this new system, I'll
move eyes, bodymarkings, hair, lipstick etc to this later

New pipeline is as follows:
- External organ added to limb
- External organ adds /datum/bodypart_overlay/mutant to limb to
bodypart_overlays
- Limb updates its icon, looks for all /datum/bodypart_overlay in
bodypart_overlays
- Very cool new overlay on your limb!

closes #71820

:cl:
refactor: External organs have been near-completely refactored. 
admin: Admin-spawned external organs will load with a random icon and
color
fix: fixes angel wings not working for non-humans (it was so fucking
broken)
fix: fixes external organs being invisible if they werent initialized
with a human
/:cl:

### Why this is good for the game
External organs are cool but are pretty limited in some ways. Making
stuff like synthetic organs is kinda fucked. I tried and it was dogshit.
Now you can just give an icon state and icon and you're good (using
/datum/bodypart_accessory/simple)

Stuff like eyes, cat ears and hair seem like good choices for extorgans,
but don't quite work for it because their icons work a lot differently.
This solves for it completely since any organ (or object or whatever)
can add it's own icon to a bodypart.

Want to add an iron plate to someones head? Go ahead. Want a heart to
stick out of someones chest? No problem.

Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

---
## [SyncIt21/The-TG-Station-Fork](https://github.com/SyncIt21/The-TG-Station-Fork)@[36090c1b20...](https://github.com/SyncIt21/The-TG-Station-Fork/commit/36090c1b206dee8b643e83607e333c29906b6bc8)
#### Thursday 2023-01-26 04:35:53 by san7890

Refactors Suicide Verb + Basic Mobs (actually all (most) living mobs) Can Now Suicide (#72919)

## About The Pull Request

On the tin. There was a lot of needless copy-paste and a lot of
single-letter vars and weird indentation and... well just all of it was
at least eight years old. So, I decided to "abstract" as much as I could
of it out instead of piling onto the big copypaste clusterfuck for
implementing basic mob suicide.
## Why It's Good For The Game

Fixes #72903

Having more procs that can be easily repeatably called to the same
results is much better than having to transplant the same exact three
lines everywhere. It's also a good first step to further in-depth
behavior by allowing sub-type overrides of certain procs (which is quite
nice). Just feels more extensible overall for the next guy who wants to
add funny suicide behavior whenever they might come around.

There's probably a few better ways to do what I did, but I wrote code
comments explaining why I did what I did. I think there's a few ways to
make it more agnostic, but I think that'll be another can of worms that
will bloat out an already quite large PR. Let's just get the framework
set.

(this refactor should also make it quite easy to unit test suicide
actions :eyes:)
## Changelog
:cl:
fix: All Mobs (including Basic mobs) are now able to suicide. (warning:
some exclusions remain)
/:cl:

---
## [re621/dnpcache](https://github.com/re621/dnpcache)@[77b062da72...](https://github.com/re621/dnpcache/commit/77b062da72fdb6182aafe0c4166a733969ebad1e)
#### Thursday 2023-01-26 05:27:41 by bitWolfy

Remove 1018 artists from the DNP list.

Removed: booponies, lulubelluleart, infinitedelusion, tankakuka, mensies, trunchbull, evian, sodasquids, telelewdz, lawlzy, tonio_(artist), xankragoc, horrificrabbits, sinfulgoatz, whippytail, malachimoet, catniplewds, cocaine_(artist), marshy_swtr, goldelope, chokodonkey, notkastar, sinnerscasino, sentharn, tealie, einin, freaks, angellsview3, arwenscoots, royalzbed, hellfurred, byrth, hexuru, devildjmachine, malerouille, donovallo, psychoninetales, vahldem_sol, nyanyakotarou, shupamikey, zyegnar, akytti, sootylion, kiva~, peshky, calmnivore, nexcoyotlgt, smoothsharb, sub-rosa, brismy, woodpeckertoons, xeshaire, suirano, mr_otter_breath, bassybefuddle, sweetishcyborg, skullwomb, steak_in_the_daylight, kittydogcrystal, aggrobadger, orbstuffed, fraichetaso, loonyleandra, bunsawce, schl4fmuetze, renkindle, psychovixen, bkmat55, fricken_stoat, w00my, haven_(artist), gipbandit, loki_the_vulpix, pixelyteskunk, erobos, bunchantress, uniquesoul1600, hirowithart, mikaemikae, ratbloke, pastellprinz, racktor, coillte, kazuk9, acidneko, josh_gong, yiyani, grayish, moblo, naoma-hiru, molish, sheyesh, st0pme, cawkbox, unclesam1776, fennecfuchs, inkpuni, pico_(artist), ruugiaruu, wispyparadox, funkybun, lewdoreocat, dogseesghosts, fauwcks, randy_entinger, trex_b6, yui-hii, runaris, rainbowpillars, ragonox, luxuria-sins, maxisb8, hiccyart, fancyfez, mesoplush, gammelgaedda, yi_feng, scpkid, goetiagoat, mabit, dischimera, dr.bubblebum, drakeraynier, rml, amawdz, mc_arts, freemau, armomen, orionfell, luriostragedy, dradmon, jesterghastly, gothgator, talentlesshack, foxryk, supertrashparty, marrowsoup, roserivy, vanzard, deepfriedlemons, pehkeshi, torotheking, harewithoutahat, lucciola, mr.lemur, lemonkyubun, cubble_chubb, arrjaysketch, pinklilim, jingo824, consciousafterdark, anti-cupid, phosaggro, dashboom, giftheck, birdrabbit, desertmotels, lv99perv, stellarfalcon, tasaeyeang, 100101, knotty, rockfall, aogirinaru, hikebu, pawpadcomrade, frengers, rikkitz, vappypaws, nukeleer, adevio, gummuru, sattytsukumo, bittenbats, whygena, ruzeb, hungothenomster, jads_l_rutan, gattonero2001, shawoo, francis_xie, angeltf, veevobyte, darkfool., huwon, tsukikibaokami, covepalms, nikunabe1989, emifern, pero3, tricksta, inkbeastart, grinn3r, holidaydipstick, odonata-nymph, binxxy_(artist), zazush-una, sodo_ad, loonanudes, kodardragon, flameydragwasp, ablimpfox, bakvissie, eccstasy, esealia, tailsrulz, dexxa, spiritto, vonepitaph, eddy-boy, saiyangoku4, gatomonlover, moonlit-comet, thehenwithatie, brienoir, tegucreative, wanisuke, pxlfur, anomyna, motsutambo, fepon, cyrogenic, fursuitchina, slates1n, depthsofthedrex, furrybob, davelievski, spacemaverick, fluff-kevlar, evenytron, 0eff0rt, gayclub, goatypie, nikoyishi, alishka, makeinu, jfetspeaks, cowbun, wyrwulf, thespiderbunny, fluffx, dragons-and-drawings, jcosneverexisted, emptyset, scoty_doodlerz, makinglemonade, ceramic_(artist), selirum, euskuuy, tsunkat, lustbubbles, appleseid, lewdtant, werewuffstuffer, odontoceti, iaido, turboranger_(artist), saca44, mr.shigglesworth, pyriax, raijikaruart, fox-pop, sirblythe_(artist), pastelarcadiaad, etherealarcadia, dracoarcadia, benjibat, sarvak, amethystbeetle, fnook_(artist), stationarrow, maim, rashkah, psy101, disappointedf0x, pointedfox, bundog, tailgrip, scalesforlife, hayleymulch, saphe, kiweevil, madakan, papyreit, rainiing, bitelickart, done0008, alec8ter, tentativelytoon, mikurulucky, killveous, fishhound, misshammer, yakushishi, pieraite, knives4cats, jalmu, quin-nsfw, zooptoon, ebonychimera, beaglebabe1, filthy-d, l-tech-e-coyote-l, anomalae, rakket, mcdutt, alcor90, sodongs, catcock, blickfen, akiiokai, possumkiddo, inkplasm, doubledeal_(artist), fuzzlesuits, chetchaka, raaazzledazzle, razferret, razbuckner, ikitsunyan, kclt, draco_(artist), gunther_silves, kkitten, singafurian, zandybutt, comfytail, crazyassbeethoven, dogburger, adalee, alirrasarts, blackmagemathos, terragon, leonois, solidpoint, cloudpie, rottenscoundrel, wings-and-strings, tomcoletti, pikajota, squeakcore, doubleclawed, ebonyplume, myznyx, zackary911, gaturo, xepher777, aimee-lesley-sim, spottedsqueak, fuhrawr, isaac_baranoff, starnina15, zestylemonss, meirdent, babymee, explicital, slyvern, karpet-shark, booghetti, zypter, adaptagx, opiodae, kiwipotato, murkbone, jonas, exed_eyes, shuryashish, mangobird, kurogi_fox_siv, snuddy, grimdank, nighteternal2469, dacad, superhypersonic2000_(artist), drako1997, verenpunainen_kuningatar, gurophilia, furrever, rdroid, smolrainbowgoat, ratte, urban-coyote, soulsplosion, cyaeon, elliotte-draws, whisperingfornothing, griz_urso, lepronasty, tears_of_soy, tren, bunnielovesyou, paliken, spaceysoda, david_frangioso, cattinypaws, bobdude0, sprocket_(artist), sincerity_gender, marymanifold, turnipberry, asbel_lhant, klaide, rishi-chan, kircai, otto0ttsy, vaktus, beezlebumawoken, transdonaldduck, questly, pinkkatfox, goopomancer, xoel, allbadbadgers, sugarlesspaints, imafutureguitarhero, eiko_tsukida, tarot_(artist), pinuh, diero, dilarus, dfer32, mxwqtkl, electrycpynk, insomniacovrlrd, cewljoke, craziestrobo, anthrus1127, sunflowerbun, coyoteofthesands, masonparker, dottii, livesinabag, flam, toastedbiscuits, skycladfox, orenjisalmonpaw, nasty-fox, canadian_roses, crez, glorpofruithag, i_am_clover, johawk, lycosa, wizardlywalrusking, burgerkiss, kielseki, whisperfoot, oksara, olly, fetchmonkey, rottingichor, heathenfang, bikomation, phox_(artist), acedetrap, hedonisticvows, deersun, skittleytwix, jinxit, jtp-remart, cocaine-leopard, amarl_krieger, nakoo, leoian_(artist), amyth, nogu-art, bluhcat, vulpes_helios, licos, taurika, papilrux, pophopper, ebnet, apis_(artist), glenthefossa, raitime, sashabelle, puddingpaw, mercurial64, elricmysteryshifter, puptaire, anojaa, candychameleon, spice5400, nickshutter, rem, reiishn, sandybuny, 1oi, crunchobar, dante_yun, pherion, saintxd, rawbelr, mithaa, asmartist, pannekoeke, jotun22, iguky-neky, ahnik, thatvondude, kelevtov., fishwrappe, animal_shapes, oouna, princess_rei, blitzdrachin, jesterdk, watermelon_(artist), amara_lemur, lady_kurai, giantmilkdud, nostars, koili, abananaman, heddy, slobstash, terian, teranen, nexii, parabellux, tom_fischbach, reddacted, tojo_the_thief, proximiter, mmuted, irootie, icyshibe, quetzalcoatl_(artist), lamm, shayshay~, hettie, chutzpaah, jacob_lhh3, carpetwurm, draekos, fatdingleberry_(artist), nooplip, pandasayori, numberxxxvi, bc92, silvixen, jungabeast, phoenixazrael, krazykurt, tape_(artist), iipaw, volvokun, hamstergirlthehamster, fallen_(artist), morkovjpn, wolfirry, slimedrops, rubisdrake, shortconcepts, ahdadah, chubbuppy, dreadcaptain, duckdraw, mehndix, pomander, wolfcha, evillabrat, henzolin, loupgarou, empa, diokhan, kpsketches, raysofsunshine, slash0x, kriticalerror, gallivant_crow, nyaroma, caindra, petit-bambi, thatblackcopfromdawnofthedead, dreamertooth, tofu93, ragnarokdragon, saucy, kidakins, kippy, swizzlestix, brilyeon, caste_(artist), tsukaui, saebira, ozzybae, boo-rad13y, sammythetanuki, vuurren, sinistervibe, rem289, shroompunk, samkin, cieldoberman, g0966, crazedg, gaoru, lpawz, enjoipandas, renthedragon, emeritus_terciel, xouual, tehcutepyro, anon232, grimmgrey, counterserum, knottykitten, crybleat, octopoodle, ker0ker0_(artist), xnirox, necrosquelch, ivenvorry, pkuai, mikefur, mattsykun, lilithveritas, bloodhound_omega, ogaraorcynder, rhos, kehei, aw0, apes, nyhgault, qualzar, licentuouslamb, reggaecyp, cynderplayer, vilegrim, redacteur, jimbohusky, lacrimale, pulsar, growlybeast, coreytwc_(artist), naoki_wolf, iceagechippies, alfierubuncle, cbee, acidic, louiefurrywolfy, bweezy, fluffernubber, koriaris, serena_valentine, tacoyaki, fullheroo, limlam, harmoniousrain, zotnamotgrim, xx_g.u.n_xx, carm, lustylamb, dragonvortex, crowchild, dragoneer, lumi_(artist), phi, lexathefox, tanookicatoon, thunper, korram, redwolfofwind, ipipo, teckworks, abobarseem, doopcity, xepheriah, diablo_en_musica_92, doncoon_(artist), digitaldomain123, belayalapa, delkon, connisaur, jasonafex, kabier, rohly, vcr-wolfe, steve_gallacci, hologram_(artist), irene_(artist), piumartiglio, sumat, kingofmaggots, oha, featheredclaw, snuddi, mentalo, ourflatcoat, da-fuze, herr_aardy, discoverychannel, azorart, nemomein, latex_(artist), afterdarkie, 7mii, draco_fenris, blown-ego, sissyskunk_(artist), chucktheskunk_(artist), oakspirit, brokenlynx21, nickswift, butter_bat, ben_hickling, bluehunter, soyuz, sorimori, blackbearcj, ficus, crimes, eifie, soundwavepie, besonik, greyskee, alekksandar, bluetigress, nereza, kalvince, thelabtwins, the_lynox, galaxyoron, moondevourer, evov1, enjambre, seph_ebonblade, prototypebasilisk, accell, myakoda, merenhor, muramuri, derfuhrer, moltengoldart, cchipppo, tetrapoda, omochi_(inkbunny), popsmasterson, nikinazu, raevee, wyntersun, ribboners, c4camel, shysketch, deishido, arconos, melvismd, taihab, cobalt_snow, flak_wizard, paddington_and_company_limited, dangerdoberman, inprogresspokemon, whitemantis, naexus, datsexylemur, polywomple, marilimmy, ryan_rabbat, krimrath, yoshitura, maplecookies, aurelleaheverfree, puppercase, spino, palcomix, bbmbbf, lilithofglace, frisket17, myloveless, grau_(artist), aduleon, sexbad, mearcu, murcifer, citrusdicks, jdlaclede, hessonite, sokalo, kittehmei, puccaruu, yuurikin, kurikia, the_cherret_awaits, rapps, maxtwenty, bigbrownorc, santanni, twistedtemptation, nikita-the-stag, liz_art, camcartoonfanatic, singlerider4, beanbat, forge_(artist), hoshime, yamamoto, eviljake2, oriole_(artist), inkblooded, alefwdog, herisheft, disparitybit, samagthrav2, battle_franky, taesolieroy, wolftacos, anixis, spazzticglitch, pirun, swampstomper, morbi, mittsies, blondevelvet, kadath, danza, shinxiolu, littlefreckles, grumpyvulpix, xopachi, gonenannurs, floravola, heartcollar, metz, ranard_lightningfall, frots, curtsibling, vilani, inkydemon, sprinkle-butt, airguitar, anhes, jace_(artist), kaji_(artist), nimrais_(artist), kyoushiro, venerit, lunaselenewolfe, tsareia, violentanxiety, kk-furryworks, cobalta, mickeyila, akuva, rairai, backlash91, sanae, fishbones_(artist), itoril, littlemiu, zeara, darkrokkuman_(artist), peony, helical, donro, agalamt, inanna-nakano, aniutqa, kraest, audiovideomeow, silverbobcat, erithacuscreations, mattartist25, yasminachan, jagzcat, ohmuu, roum, sefeiren, sesameseedbun, noben, aquatheohiokitty, mewyfox, ilgrigio, leoian, vixendra, van_weasel, keihound, zoey03, hardblush, jay_naylor, frisky_ferals, slipshine, rubyrebirth, oze, neogeen, omegaltd, themadcatter, kamicheetah, ookamithewolf1, rabbit_valley, purplekecleon, ollieosa, jayfiregrowlithe, ensayne, bazaarbobby, scappo, dogsoul, poonani, paddercat, eltonpot, ebonyleopard, strype, cbh, mithril07, bicdente, unpeeledwasp, versiris, pitkin, mikachu_tuhonen, lilhoneypup, ladyshinwa, bad-collie, buizilla, foxxian, inert-ren, okamiterasu, mrawl, sammy_stowes, jameless, jooshster, lemoncore, xainy, strider-orion, silitha, spacepoptart, myuinhiding, sweetpinkpetals, sephygoth, edensky, ka, cigarscigarettes, tani_da_real, leatherruffian, hahul, cheezyweapon, reizakirga, leefuu, tanyafoxy, peyo, sweatshirt_(artist), adiago, timelesserror, jollyjack, kahmari, madhattermonster, omnoproxyl337, greykitty, thekitty, mattaku_shinzu, fortuna, fallenarts, ammako, sciggles, atlasfield, sheepdust, lumaberry, tktktk, uzai, aku_tojyo, sixthleafclover, gardelius, squeedgemonster, max-dragon, baka_sukonku, ferniio, jennadelle, ixerin, jaleo, luvythicus, tatious, nekomata_neko, zody, binky, sidian, kii-kitsune, kiirei, spookeedoo, angel27, msrah_(artist), nazuu-m0nster, lunacatta, kululu-xiao, kipcha, fluffball, reptilecynrik, redadillio, zerwolf, kylontario, liz_day, nightweaver, egophiliac, doffa, dipper, kefkafloyd, melo666, sonicdash, sugarpoultry, olven, theramjing, softpaw, xiraco, unicornspirit, tinintri, thornwolf, thaily, tamen, sharue, shadowsani, rikutida, paolo, kriscrash, kaemantis, frogsbreath, tailheat, sexyfur, jeremy_bernal

---
## [Omgise/Et-Futurum-Requiem](https://github.com/Omgise/Et-Futurum-Requiem)@[dc506a9fe1...](https://github.com/Omgise/Et-Futurum-Requiem/commit/dc506a9fe1c1448eaec73af46604a68fc52af553)
#### Thursday 2023-01-26 06:13:14 by Roadhog360

Thanks Eclipse for not saving this

Seriously getting sick of Eclipse's "save undo" horse shit
Might switch to IntelliJ because I keep saving in Eclipse only to go back to see it DIDN"T save and I have to save the same fucking changes again for them to apply and make these stupid micro-commits to push stuff that should have already been fucking pushed

---
## [GhanSaridnirun/Green-Peafowl-Population_Project__GS](https://github.com/GhanSaridnirun/Green-Peafowl-Population_Project__GS)@[7f3c5e8032...](https://github.com/GhanSaridnirun/Green-Peafowl-Population_Project__GS/commit/7f3c5e8032a088212ca1e469af2ba933e6f78592)
#### Thursday 2023-01-26 06:25:08 by Ghan Saridnirun

Update numerical matrix

- Add number assuagements
- Change some vector assignments for code running.
- The New code place below the assignment task
- I experience the problem when I tried to run difference model from differed parameter setting I got all values that I should excepted sensitivity and elasticity that appeared as NA.
- I have disable the code that assigned the Chick produce from F1Y due to 
I remember that the 2 year females F2Y and 3 year up females F3y  could provided the offspring while F1Y still immature to do that, I just noticed that I must forgot this point when we are constructing the matrix.

---
## [ariffjenong/kernel_xiaomi_lavender](https://github.com/ariffjenong/kernel_xiaomi_lavender)@[5d0debe61a...](https://github.com/ariffjenong/kernel_xiaomi_lavender/commit/5d0debe61abdbdcbf2b5f45fa1dfb583948c282c)
#### Thursday 2023-01-26 09:07:46 by Christian Brauner

BACKPORT: signal: add pidfd_send_signal() syscall

The kill() syscall operates on process identifiers (pid). After a process
has exited its pid can be reused by another process. If a caller sends a
signal to a reused pid it will end up signaling the wrong process. This
issue has often surfaced and there has been a push to address this problem [1].

This patch uses file descriptors (fd) from proc/<pid> as stable handles on
struct pid. Even if a pid is recycled the handle will not change. The fd
can be used to send signals to the process it refers to.
Thus, the new syscall pidfd_send_signal() is introduced to solve this
problem. Instead of pids it operates on process fds (pidfd).

/* prototype and argument /*
long pidfd_send_signal(int pidfd, int sig, siginfo_t *info, unsigned int flags);

/* syscall number 424 */
The syscall number was chosen to be 424 to align with Arnd's rework in his
y2038 to minimize merge conflicts (cf. [25]).

In addition to the pidfd and signal argument it takes an additional
siginfo_t and flags argument. If the siginfo_t argument is NULL then
pidfd_send_signal() is equivalent to kill(<positive-pid>, <signal>). If it
is not NULL pidfd_send_signal() is equivalent to rt_sigqueueinfo().
The flags argument is added to allow for future extensions of this syscall.
It currently needs to be passed as 0. Failing to do so will cause EINVAL.

/* pidfd_send_signal() replaces multiple pid-based syscalls */
The pidfd_send_signal() syscall currently takes on the job of
rt_sigqueueinfo(2) and parts of the functionality of kill(2), Namely, when a
positive pid is passed to kill(2). It will however be possible to also
replace tgkill(2) and rt_tgsigqueueinfo(2) if this syscall is extended.

/* sending signals to threads (tid) and process groups (pgid) */
Specifically, the pidfd_send_signal() syscall does currently not operate on
process groups or threads. This is left for future extensions.
In order to extend the syscall to allow sending signal to threads and
process groups appropriately named flags (e.g. PIDFD_TYPE_PGID, and
PIDFD_TYPE_TID) should be added. This implies that the flags argument will
determine what is signaled and not the file descriptor itself. Put in other
words, grouping in this api is a property of the flags argument not a
property of the file descriptor (cf. [13]). Clarification for this has been
requested by Eric (cf. [19]).
When appropriate extensions through the flags argument are added then
pidfd_send_signal() can additionally replace the part of kill(2) which
operates on process groups as well as the tgkill(2) and
rt_tgsigqueueinfo(2) syscalls.
How such an extension could be implemented has been very roughly sketched
in [14], [15], and [16]. However, this should not be taken as a commitment
to a particular implementation. There might be better ways to do it.
Right now this is intentionally left out to keep this patchset as simple as
possible (cf. [4]).

/* naming */
The syscall had various names throughout iterations of this patchset:
- procfd_signal()
- procfd_send_signal()
- taskfd_send_signal()
In the last round of reviews it was pointed out that given that if the
flags argument decides the scope of the signal instead of different types
of fds it might make sense to either settle for "procfd_" or "pidfd_" as
prefix. The community was willing to accept either (cf. [17] and [18]).
Given that one developer expressed strong preference for the "pidfd_"
prefix (cf. [13]) and with other developers less opinionated about the name
we should settle for "pidfd_" to avoid further bikeshedding.

The  "_send_signal" suffix was chosen to reflect the fact that the syscall
takes on the job of multiple syscalls. It is therefore intentional that the
name is not reminiscent of neither kill(2) nor rt_sigqueueinfo(2). Not the
fomer because it might imply that pidfd_send_signal() is a replacement for
kill(2), and not the latter because it is a hassle to remember the correct
spelling - especially for non-native speakers - and because it is not
descriptive enough of what the syscall actually does. The name
"pidfd_send_signal" makes it very clear that its job is to send signals.

/* zombies */
Zombies can be signaled just as any other process. No special error will be
reported since a zombie state is an unreliable state (cf. [3]). However,
this can be added as an extension through the @flags argument if the need
ever arises.

/* cross-namespace signals */
The patch currently enforces that the signaler and signalee either are in
the same pid namespace or that the signaler's pid namespace is an ancestor
of the signalee's pid namespace. This is done for the sake of simplicity
and because it is unclear to what values certain members of struct
siginfo_t would need to be set to (cf. [5], [6]).

/* compat syscalls */
It became clear that we would like to avoid adding compat syscalls
(cf. [7]).  The compat syscall handling is now done in kernel/signal.c
itself by adding __copy_siginfo_from_user_generic() which lets us avoid
compat syscalls (cf. [8]). It should be noted that the addition of
__copy_siginfo_from_user_any() is caused by a bug in the original
implementation of rt_sigqueueinfo(2) (cf. 12).
With upcoming rework for syscall handling things might improve
significantly (cf. [11]) and __copy_siginfo_from_user_any() will not gain
any additional callers.

/* testing */
This patch was tested on x64 and x86.

/* userspace usage */
An asciinema recording for the basic functionality can be found under [9].
With this patch a process can be killed via:

 #define _GNU_SOURCE
 #include <errno.h>
 #include <fcntl.h>
 #include <signal.h>
 #include <stdio.h>
 #include <stdlib.h>
 #include <string.h>
 #include <sys/stat.h>
 #include <sys/syscall.h>
 #include <sys/types.h>
 #include <unistd.h>

 static inline int do_pidfd_send_signal(int pidfd, int sig, siginfo_t *info,
                                         unsigned int flags)
 {
 #ifdef __NR_pidfd_send_signal
         return syscall(__NR_pidfd_send_signal, pidfd, sig, info, flags);
 #else
         return -ENOSYS;
 #endif
 }

 int main(int argc, char *argv[])
 {
         int fd, ret, saved_errno, sig;

         if (argc < 3)
                 exit(EXIT_FAILURE);

         fd = open(argv[1], O_DIRECTORY | O_CLOEXEC);
         if (fd < 0) {
                 printf("%s - Failed to open \"%s\"\n", strerror(errno), argv[1]);
                 exit(EXIT_FAILURE);
         }

         sig = atoi(argv[2]);

         printf("Sending signal %d to process %s\n", sig, argv[1]);
         ret = do_pidfd_send_signal(fd, sig, NULL, 0);

         saved_errno = errno;
         close(fd);
         errno = saved_errno;

         if (ret < 0) {
                 printf("%s - Failed to send signal %d to process %s\n",
                        strerror(errno), sig, argv[1]);
                 exit(EXIT_FAILURE);
         }

         exit(EXIT_SUCCESS);
 }

/* Q&A
 * Given that it seems the same questions get asked again by people who are
 * late to the party it makes sense to add a Q&A section to the commit
 * message so it's hopefully easier to avoid duplicate threads.
 *
 * For the sake of progress please consider these arguments settled unless
 * there is a new point that desperately needs to be addressed. Please make
 * sure to check the links to the threads in this commit message whether
 * this has not already been covered.
 */
Q-01: (Florian Weimer [20], Andrew Morton [21])
      What happens when the target process has exited?
A-01: Sending the signal will fail with ESRCH (cf. [22]).

Q-02:  (Andrew Morton [21])
       Is the task_struct pinned by the fd?
A-02:  No. A reference to struct pid is kept. struct pid - as far as I
       understand - was created exactly for the reason to not require to
       pin struct task_struct (cf. [22]).

Q-03: (Andrew Morton [21])
      Does the entire procfs directory remain visible? Just one entry
      within it?
A-03: The same thing that happens right now when you hold a file descriptor
      to /proc/<pid> open (cf. [22]).

Q-04: (Andrew Morton [21])
      Does the pid remain reserved?
A-04: No. This patchset guarantees a stable handle not that pids are not
      recycled (cf. [22]).

Q-05: (Andrew Morton [21])
      Do attempts to signal that fd return errors?
A-05: See {Q,A}-01.

Q-06: (Andrew Morton [22])
      Is there a cleaner way of obtaining the fd? Another syscall perhaps.
A-06: Userspace can already trivially retrieve file descriptors from procfs
      so this is something that we will need to support anyway. Hence,
      there's no immediate need to add another syscalls just to make
      pidfd_send_signal() not dependent on the presence of procfs. However,
      adding a syscalls to get such file descriptors is planned for a
      future patchset (cf. [22]).

Q-07: (Andrew Morton [21] and others)
      This fd-for-a-process sounds like a handy thing and people may well
      think up other uses for it in the future, probably unrelated to
      signals. Are the code and the interface designed to permit such
      future applications?
A-07: Yes (cf. [22]).

Q-08: (Andrew Morton [21] and others)
      Now I think about it, why a new syscall? This thing is looking
      rather like an ioctl?
A-08: This has been extensively discussed. It was agreed that a syscall is
      preferred for a variety or reasons. Here are just a few taken from
      prior threads. Syscalls are safer than ioctl()s especially when
      signaling to fds. Processes are a core kernel concept so a syscall
      seems more appropriate. The layout of the syscall with its four
      arguments would require the addition of a custom struct for the
      ioctl() thereby causing at least the same amount or even more
      complexity for userspace than a simple syscall. The new syscall will
      replace multiple other pid-based syscalls (see description above).
      The file-descriptors-for-processes concept introduced with this
      syscall will be extended with other syscalls in the future. See also
      [22], [23] and various other threads already linked in here.

Q-09: (Florian Weimer [24])
      What happens if you use the new interface with an O_PATH descriptor?
A-09:
      pidfds opened as O_PATH fds cannot be used to send signals to a
      process (cf. [2]). Signaling processes through pidfds is the
      equivalent of writing to a file. Thus, this is not an operation that
      operates "purely at the file descriptor level" as required by the
      open(2) manpage. See also [4].

/* References */
[1]:  https://lore.kernel.org/lkml/20181029221037.87724-1-dancol@google.com/
[2]:  https://lore.kernel.org/lkml/874lbtjvtd.fsf@oldenburg2.str.redhat.com/
[3]:  https://lore.kernel.org/lkml/20181204132604.aspfupwjgjx6fhva@brauner.io/
[4]:  https://lore.kernel.org/lkml/20181203180224.fkvw4kajtbvru2ku@brauner.io/
[5]:  https://lore.kernel.org/lkml/20181121213946.GA10795@mail.hallyn.com/
[6]:  https://lore.kernel.org/lkml/20181120103111.etlqp7zop34v6nv4@brauner.io/
[7]:  https://lore.kernel.org/lkml/36323361-90BD-41AF-AB5B-EE0D7BA02C21@amacapital.net/
[8]:  https://lore.kernel.org/lkml/87tvjxp8pc.fsf@xmission.com/
[9]:  https://asciinema.org/a/IQjuCHew6bnq1cr78yuMv16cy
[11]: https://lore.kernel.org/lkml/F53D6D38-3521-4C20-9034-5AF447DF62FF@amacapital.net/
[12]: https://lore.kernel.org/lkml/87zhtjn8ck.fsf@xmission.com/
[13]: https://lore.kernel.org/lkml/871s6u9z6u.fsf@xmission.com/
[14]: https://lore.kernel.org/lkml/20181206231742.xxi4ghn24z4h2qki@brauner.io/
[15]: https://lore.kernel.org/lkml/20181207003124.GA11160@mail.hallyn.com/
[16]: https://lore.kernel.org/lkml/20181207015423.4miorx43l3qhppfz@brauner.io/
[17]: https://lore.kernel.org/lkml/CAGXu5jL8PciZAXvOvCeCU3wKUEB_dU-O3q0tDw4uB_ojMvDEew@mail.gmail.com/
[18]: https://lore.kernel.org/lkml/20181206222746.GB9224@mail.hallyn.com/
[19]: https://lore.kernel.org/lkml/20181208054059.19813-1-christian@brauner.io/
[20]: https://lore.kernel.org/lkml/8736rebl9s.fsf@oldenburg.str.redhat.com/
[21]: https://lore.kernel.org/lkml/20181228152012.dbf0508c2508138efc5f2bbe@linux-foundation.org/
[22]: https://lore.kernel.org/lkml/20181228233725.722tdfgijxcssg76@brauner.io/
[23]: https://lwn.net/Articles/773459/
[24]: https://lore.kernel.org/lkml/8736rebl9s.fsf@oldenburg.str.redhat.com/
[25]: https://lore.kernel.org/lkml/CAK8P3a0ej9NcJM8wXNPbcGUyOUZYX+VLoDFdbenW3s3114oQZw@mail.gmail.com/

Cc: "Eric W. Biederman" <ebiederm@xmission.com>
Cc: Jann Horn <jannh@google.com>
Cc: Andy Lutomirsky <luto@kernel.org>
Cc: Andrew Morton <akpm@linux-foundation.org>
Cc: Oleg Nesterov <oleg@redhat.com>
Cc: Al Viro <viro@zeniv.linux.org.uk>
Cc: Florian Weimer <fweimer@redhat.com>
Signed-off-by: Christian Brauner <christian@brauner.io>
Reviewed-by: Tycho Andersen <tycho@tycho.ws>
Reviewed-by: Kees Cook <keescook@chromium.org>
Reviewed-by: David Howells <dhowells@redhat.com>
Acked-by: Arnd Bergmann <arnd@arndb.de>
Acked-by: Thomas Gleixner <tglx@linutronix.de>
Acked-by: Serge Hallyn <serge@hallyn.com>
Acked-by: Aleksa Sarai <cyphar@cyphar.com>

(cherry picked from commit 3eb39f47934f9d5a3027fe00d906a45fe3a15fad)

Conflicts:
        arch/x86/entry/syscalls/syscall_32.tbl - trivial manual merge
        arch/x86/entry/syscalls/syscall_64.tbl - trivial manual merge
        include/linux/proc_fs.h - trivial manual merge
        include/linux/syscalls.h - trivial manual merge
        include/uapi/asm-generic/unistd.h - trivial manual merge
        kernel/signal.c - struct kernel_siginfo does not exist in 4.14
        kernel/sys_ni.c - cond_syscall is used instead of COND_SYSCALL
        arch/x86/entry/syscalls/syscall_32.tbl
        arch/x86/entry/syscalls/syscall_64.tbl

(1. manual merges because of 4.14 differences
 2. change prepare_kill_siginfo() to use struct siginfo instead of
kernel_siginfo
 3. use copy_from_user() instead of copy_siginfo_from_user() in copy_siginfo_from_user_any()
 4. replaced COND_SYSCALL with cond_syscall
 5. Removed __ia32_sys_pidfd_send_signal in arch/x86/entry/syscalls/syscall_32.tbl.
 6. Replaced __x64_sys_pidfd_send_signal with sys_pidfd_send_signal in arch/x86/entry/syscalls/syscall_64.tbl.)

Bug: 135608568
Test: test program using syscall(__NR_pidfd_send_signal,..) to send SIGKILL
Change-Id: I34da11c63ac8cafb0353d9af24c820cef519ec27
Signed-off-by: Suren Baghdasaryan <surenb@google.com>
Signed-off-by: electimon <electimon@gmail.com>

---
## [ProjectBlaze/frameworks_base](https://github.com/ProjectBlaze/frameworks_base)@[973e5fc628...](https://github.com/ProjectBlaze/frameworks_base/commit/973e5fc628f3939e02181444090a7579c4a58044)
#### Thursday 2023-01-26 10:03:31 by Kuba Wojciechowski

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
## [OrionTheFox/Skyrat-tg](https://github.com/OrionTheFox/Skyrat-tg)@[1737ab8598...](https://github.com/OrionTheFox/Skyrat-tg/commit/1737ab8598dc94f6c5d8a9f11d8b8bc5a75055d6)
#### Thursday 2023-01-26 10:34:54 by SkyratBot

[MIRROR] Fixes parallax on >2 level maps going fucky with optimized multiz [MDB IGNORE] (#18298)

* Fixes parallax on >2 level maps going fucky with optimized multiz (#72169)

## About The Pull Request

We no longer always render parallax.
This was causing issues because we can't isolate the white of space from
the vaugely white of everything else.

So instead, if your parallax plane is out of view, we'll not only
disable it, but we'll disable the strand we send from the main plane TO
it.

Instead only blending against the bottom stack.

This does mean there's a possibility for fullwhite on z transition
borders (potentially fixable), or when hijacking the plane (also
fixable, but significantly more annoying).

This is enough to make large maps functional though, so I'm happy with
it

## Why It's Good For The Game

Allows for #71731 and other maps like it. Makes my code actually work

## Changelog
:cl:
fix: Using optimized multiz on > 2 z layer maps will no longer cause
fucko bungo
/:cl:

* Fixes parallax on >2 level maps going fucky with optimized multiz

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [alfael/alfkern_msm8953_tissot](https://github.com/alfael/alfkern_msm8953_tissot)@[6cbdaf108b...](https://github.com/alfael/alfkern_msm8953_tissot/commit/6cbdaf108b58528703cf4d0b708c5e1a57b10f36)
#### Thursday 2023-01-26 10:40:05 by George Spelvin

lib/sort: make swap functions more generic

Patch series "lib/sort & lib/list_sort: faster and smaller", v2.

Because CONFIG_RETPOLINE has made indirect calls much more expensive, I
thought I'd try to reduce the number made by the library sort functions.

The first three patches apply to lib/sort.c.

Patch #1 is a simple optimization.  The built-in swap has special cases
for aligned 4- and 8-byte objects.  But those are almost never used;
most calls to sort() work on larger structures, which fall back to the
byte-at-a-time loop.  This generalizes them to aligned *multiples* of 4
and 8 bytes.  (If nothing else, it saves an awful lot of energy by not
thrashing the store buffers as much.)

Patch #2 grabs a juicy piece of low-hanging fruit.  I agree that nice
simple solid heapsort is preferable to more complex algorithms (sorry,
Andrey), but it's possible to implement heapsort with far fewer
comparisons (50% asymptotically, 25-40% reduction for realistic sizes)
than the way it's been done up to now.  And with some care, the code
ends up smaller, as well.  This is the "big win" patch.

Patch #3 adds the same sort of indirect call bypass that has been added
to the net code of late.  The great majority of the callers use the
builtin swap functions, so replace the indirect call to sort_func with a
(highly preditable) series of if() statements.  Rather surprisingly,
this decreased code size, as the swap functions were inlined and their
prologue & epilogue code eliminated.

lib/list_sort.c is a bit trickier, as merge sort is already close to
optimal, and we don't want to introduce triumphs of theory over
practicality like the Ford-Johnson merge-insertion sort.

Patch #4, without changing the algorithm, chops 32% off the code size
and removes the part[MAX_LIST_LENGTH+1] pointer array (and the
corresponding upper limit on efficiently sortable input size).

Patch #5 improves the algorithm.  The previous code is already optimal
for power-of-two (or slightly smaller) size inputs, but when the input
size is just over a power of 2, there's a very unbalanced final merge.

There are, in the literature, several algorithms which solve this, but
they all depend on the "breadth-first" merge order which was replaced by
commit 835cc0c8477f with a more cache-friendly "depth-first" order.
Some hard thinking came up with a depth-first algorithm which defers
merges as little as possible while avoiding bad merges.  This saves
0.2*n compares, averaged over all sizes.

The code size increase is minimal (64 bytes on x86-64, reducing the net
savings to 26%), but the comments expanded significantly to document the
clever algorithm.

TESTING NOTES: I have some ugly user-space benchmarking code which I
used for testing before moving this code into the kernel.  Shout if you
want a copy.

I'm running this code right now, with CONFIG_TEST_SORT and
CONFIG_TEST_LIST_SORT, but I confess I haven't rebooted since the last
round of minor edits to quell checkpatch.  I figure there will be at
least one round of comments and final testing.

This patch (of 5):

Rather than having special-case swap functions for 4- and 8-byte
objects, special-case aligned multiples of 4 or 8 bytes.  This speeds up
most users of sort() by avoiding fallback to the byte copy loop.

Despite what ca96ab859ab4 ("lib/sort: Add 64 bit swap function") claims,
very few users of sort() sort pointers (or pointer-sized objects); most
sort structures containing at least two words.  (E.g.
drivers/acpi/fan.c:acpi_fan_get_fps() sorts an array of 40-byte struct
acpi_fan_fps.)

The functions also got renamed to reflect the fact that they support
multiple words.  In the great tradition of bikeshedding, the names were
by far the most contentious issue during review of this patch series.

x86-64 code size 872 -> 886 bytes (+14)

With feedback from Andy Shevchenko, Rasmus Villemoes and Geert
Uytterhoeven.

Link: http://lkml.kernel.org/r/f24f932df3a7fa1973c1084154f1cea596bcf341.1552704200.git.lkml@sdf.org
Signed-off-by: George Spelvin <lkml@sdf.org>
Acked-by: Andrey Abramov <st5pub@yandex.ru>
Acked-by: Rasmus Villemoes <linux@rasmusvillemoes.dk>
Reviewed-by: Andy Shevchenko <andriy.shevchenko@linux.intel.com>
Cc: Rasmus Villemoes <linux@rasmusvillemoes.dk>
Cc: Geert Uytterhoeven <geert@linux-m68k.org>
Cc: Daniel Wagner <daniel.wagner@siemens.com>
Cc: Don Mullis <don.mullis@gmail.com>
Cc: Dave Chinner <dchinner@redhat.com>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>

---
## [amjoseph-nixpkgs/nixpkgs](https://github.com/amjoseph-nixpkgs/nixpkgs)@[c36d256cec...](https://github.com/amjoseph-nixpkgs/nixpkgs/commit/c36d256cec33bc1246d32390a64416cca330230d)
#### Thursday 2023-01-26 10:59:41 by Adam Joseph

stdenv: external gcc bootstrap

#### Immediate Benefits

- Allow `gcc11` on `aarch64`
- No more copying `libgcc_s` out of the bootstrap-files or other
  derivations
- No more [static `lib{mpfr,mpc,gmp,isl}.a`
  hack](https://github.com/NixOS/nixpkgs/blob/2f1948af9c984ebb82dfd618e67dc949755823e2/pkgs/stdenv/linux/default.nix#L380)
- *Zero* additional `gcc` builds (stage1+stage2+stageCompare)
  - The `gcc` derivation builds `gcc` once instead of three times.
  - The libraries that are linked into the final `pkgs.gcc` (`mpfr`,
    `mpc`, `gmp`, `isl`, `glibc`) are built by
    `stdenv.__bootPkgs.gcc` rather than by the `bootstrapFiles`.  No
    more Frankenstein compiler!
  - stageCompare runs **concurrently** with (not in series with)
    with `stdenv`'s dependees.
- Many other `stdenv` hacks eliminated.
  - `gcc` and `clang` share the same codepath for more of
    `cc-wrapper`.
  - Makes the cross and native codepaths much more similar --
    another step towards "cross by default".

Note that *all* the changes in this PR are controlled by flags; no
old codepaths need to be removed until/if we're completely certain
that this is the right way to go.

#### Future Benefits

- This should allow using a [foreign] `bootstrap-files` so long as
  `hostPlatform.canExecute bootstrapFiles`.
- There will be an "avalanche of simplification" when we set
  `enableGccExternalBootstrap=true` and run dead code elimination.
  It's really quite a huge amount of code that goes away.
  Native-gcc has its own special codepath in so many places, while
  cross-gcc and clang work the same way (and are much simpler).
- This should allow each of the libraries that ship with `gcc`
  (`lib{backtrace,atomic,cc1,decnumber,ffi,gomp,iberty,offloadatomic,quadmath,sanitizer,ssp,stdc++-v3,vtv}`)
  to be built in separate (one-liner) derivations which `inherit
  src;` from `gcc`.
  - Building `libstdc++-v3` in a separate derivation will eliminate
    a lot of accidental-reference-to-the-`bootstrapFiles` landmines.

#### Incorporates

- https://github.com/NixOS/nixpkgs/pull/209054
- https://github.com/NixOS/nixpkgs/pull/210004
- https://github.com/NixOS/nixpkgs/pull/36948 (unreverted)
- https://github.com/NixOS/nixpkgs/pull/210325
- https://github.com/NixOS/nixpkgs/pull/210118
- https://github.com/NixOS/nixpkgs/pull/210132
- https://github.com/NixOS/nixpkgs/pull/210109

#### Closes

- Closes https://github.com/NixOS/nixpkgs/issues/208412
- Closes https://github.com/NixOS/nixpkgs/issues/108111
- Closes https://github.com/NixOS/nixpkgs/issues/108305
- Closes https://github.com/NixOS/nixpkgs/issues/201254

#### Build history

- First successful builds (stage1/stage2):
  - powerpc64le-linux at 9c7e9ef256714455914180c0bcb434e014e5b75a
  - x86_64-linux at 9c7e9ef256714455914180c0bcb434e014e5b75a
  - aarch64-linux at 4d5bc7dabfbe1f8758559390e373b91dda9d401e

- First successful comparisons (stageCompare):
  - at 81949cffa3272f8f9bdc8cfda8effb34be517d2f
  - [aarch64-linux][aarch64-compare-ofborg]
  - [x86\_64-linux][amd64-compare-ofborg]

#### Credits

This project was made possible by three important insights, none of
which were mine:

1. @ericson2314 was the first to advocate for this change, and
   probably the first to appreciate its advantages.  External
   bootstrap is "cross by default".

2. @trofi has figured out a lot about how to get gcc to not mix up
   the copy of `libstdc++` that it depends on with the copy that it
   builds.  Now that gcc is written in C++, it depends on
   `libstdc++`, builds a copy of `libstdc++`, and builds auxiliary
   products (like `libplugin`) which depend on `libstdc++`.  @trofi
   developed two important techniques for keeping this straight: the
   use of a [nonexistent sysroot] and moving the `bootstrapFiles`'
   `libstdc++` into a [versioned directory].  Without these two
   discoveries, external bootstrap would be impossible, because the
   final gcc would still have references to the `bootstrapFiles`.

3. Using the undocumented variable [`user-defined-trusted-dirs`]
   when building glibc.  When glibc `dlopen()`s `libgcc_s.so`, it
   uses a completely different and totally special set of rules for
   finding `libgcc_s.so`.  This trick is the only way we can put
   `libgcc_s.so` in its own separate outpath without creating
   circular dependencies or dependencies on the bootstrapFiles.  I
   would never have guessed to use this (or that it existed!) if it
   were not for a [comment in guix] which @Mic92 [mentioned].

My own role in this PR was basically: being available to go on a
coding binge at an opportune moment, so we wouldn't waste a
[crisis].

[aarch64-compare-ofborg]: https://github.com/NixOS/nixpkgs/pull/209870/checks?check_run_id=10662822938
[amd64-compare-ofborg]: https://github.com/NixOS/nixpkgs/pull/209870/checks?check_run_id=10662825857
[nonexistent sysroot]: https://github.com/NixOS/nixpkgs/pull/210004
[versioned directory]: https://github.com/NixOS/nixpkgs/pull/209054
[`user-defined-trusted-dirs`]: https://sourceware.org/legacy-ml/libc-help/2013-11/msg00026.html
[comment in guix]: https://github.com/guix-mirror/guix/blob/5e4ec8218142eee8e6e148e787381a5ef891c5b1/gnu/packages/gcc.scm#L253
[mentioned]: https://github.com/NixOS/nixpkgs/pull/210112#issuecomment-1379608483
[crisis]: https://github.com/NixOS/nixpkgs/issues/108305
[foreign]: https://github.com/NixOS/nixpkgs/pull/170857#issuecomment-1170558348

---
## [mahmood-eid/DB-task](https://github.com/mahmood-eid/DB-task)@[58ebc6c008...](https://github.com/mahmood-eid/DB-task/commit/58ebc6c00830c48e53d2fd7043d33bce60f9e67e)
#### Thursday 2023-01-26 12:58:15 by Mahm0ud-Eid

Oh! this idiot is causing me a lot of troubles! :( sorry there will be some more changes

---
## [getong/rust](https://github.com/getong/rust)@[336608aa92...](https://github.com/getong/rust/commit/336608aa924e1dfe38810997f81368a2d5df1213)
#### Thursday 2023-01-26 13:15:55 by bors

Auto merge of #13810 - tfpk:tfpk/macro-inline, r=Veykril

Add action to expand a declarative macro once, inline. Fixes #13598

This commit adds a new r-a method, `expandMacroInline`, which expands the macro that's currently selected. See  #13598 for the most applicable issue; though I suspect it'll resolve part of #5949 and make #11888 significantly easier).

The macro works like this:

![rust-analyser-feature](https://user-images.githubusercontent.com/10906982/208813167-3123e379-8fd5-4206-a4f4-5af1129565f9.gif)

I have 2 questions before this PR can be merged:

1. **Should we rustfmt the output?** The advantage of doing this is neater code. The disadvantages are we'd have to format the whole expr/stmt/block (since there's no point just formatting one part, especially over multiple lines), and maybe it moves the code around more in weird ways. My suggestion here is to start off by not doing any formatting; and if it appears useful we can decide to do formatting in a later release.
2.   **Is it worth solving the `$crate` hygiene issue now?** -- I think this PR is usable as of right now for some use-cases; but it is annoying that many common macros (i.e. `println!()`, `format!()`) can't be expanded further unless the user guesses the correct `$crate` value. The trouble with solving that issue is that I think it's complicated and imperfect. If we do solve it; we'd also need to either change the existing `expandMacro`/`expandMacroInline` commands; provide some option to allow/disallow `$crate` expanding; or come to some other compromise.

---
## [earthhologenome/EHI_bioinformatics](https://github.com/earthhologenome/EHI_bioinformatics)@[f4dd19c2aa...](https://github.com/earthhologenome/EHI_bioinformatics/commit/f4dd19c2aabd033b1153a074d9aa464508776b97)
#### Thursday 2023-01-26 14:23:44 by EisenRa

Never writing code like this in BASH again. Holy shit you have to love EOF character differences between MAC and linux..

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[1448584151...](https://github.com/mrakgr/The-Spiral-Language/commit/1448584151e35dda81d0eab2e62e0de62e44ab04)
#### Thursday 2023-01-26 14:24:59 by Marko Grdinić

"https://news.ycombinator.com/item?id=34519268
What we look for in a resume

///

One very small tip - don't overdo it in selling your accomplishments. I see surprisingly many resumes with the words "vast experience", and they're usually obvious bullshit.
reply

///

///

OTOH I've got a close-ish relative who's had a very successful career in HR in multiple large orgs and now does some résumé consulting on the side, and she always re-writes things way beyond what I'm comfortable actually claiming and insists that's for-sure the right thing to do when applying to most bigcos—just part of playing the game, and if you don't play, you can't win.

You'll tell her you did X and she'll be like "well it sounds to me like that was Y, so write that down" and you're like "well... kind of? But not really" and she's like "yes, it's Y, you're cutting yourself off at the kneecaps if you don't put Y". Where Y is usually something to do with leading or managing or "architecting" something, and it's maybe technically true but I'd never have characterized it that way and would be struggle to talk about it as if it were that.

///

This whole thread is like this. One person says one thing, and the other replies with the opposite.

I'll upvote this thread. It is really informative. It seems there is no hard and fast rules when it comes to resumes. My hunch is that with startups, people reading the resumes will go up compared to corpos. If I am replying to large places, with my resume the way it is now, it would just be tossed into the trash, but at startups I have a chance.

8:15pm. https://huyenchip.com/2023/01/24/what-we-look-for-in-a-candidate.html

It might be worth applying here at some point. Well, here and StabilityAI. Though the later must be absolutely swamped. No, it requires -8 UTC.

https://stability.ai/careers

Let me give it a shot. I'll just toss the dice and be honest as to why I'd work there.

8:35pm. Let me read Death Sword Girl, watch an ep of Tenten and I'll go to bed. Usually I go to bed later, but I'll start going earlier. Tomorrow, I will do something super simple. Just do the recording from start to finish, edit out the error, do the voice overs. Actually, I don't know how to include voice overs just yet in ActivePresenter, that is something I will have to figure out.

Forget the script for my first try. Just turn on the screen recording and blab. Get over the initial hump. Just let it all go out. Then refine it. That is the way I should do this.

1/26/2023

8:30am. I am up. I must have woken up a few hours ago and thought about it deeply. Someone messaged me on LinkedIn, but now that I've loged into linked in, I see I have a two month old offer for a PL job from a recruiter. Assuming the position is still open this might be up my alley. Let me also check my emails. Nothing meaningful. A reject from some EU backend position I applied to.

> I'm contacting you as I'm currently looking for a Machine Learning Compiler Engineer to join our client: a compute protocol for the world's deep learning models.

The two month old LinkedIn message starts like this. Let me reply to this.

https://www.linkedin.com/in/marko-grdinic-6063b321a/

Damn it, where the hell is the add media thing so I can plug my resume?

Nevermind it for now, let me take a bath.

9:40am. Done with the bath.

9:45am. Er, how do I put a piece of media there? I could find a link to it last time, but...

https://www.linkedin.com/pulse/how-add-media-your-linkedin-profile-lisa-marie-dias?trk=pulse-article

I figured it out. If you go under Add Position or Add Education, it allows you to Add Media. The thing in the article got moved.

I have that out of the way.

Now, I've been thinking about this during the night, but let me do some tweaking of my Twitter profile.

9:55am. I'll want to post the Heaven's Key albums there, along with some standout images.

Looking at my dashboard for Heaven's Key.

Total view 8,867. Avg views 161. Pages 589. 162.2k words published. Total comments at 8. Followers at 36. Favorites at 10. Ratings at 8 (avg 3.75). Reviews 0.

Even though I've spent months of my life on this, it isn't unfair to say that literally only a single person cares about it.

I thought I might get some comments wishing me good luck or something like that, but I am getting crickets.

Continuing to write Heaven's Key would not be good. It is the opposite. It is literally a threat to my survival. Had I been getting followers at a faster rate as well as Patreon subscribers, things would be different.

Maybe at some point in the future I will resume it. Maybe I'll write it a little to the side. But right now, it does not matter.

https://boards.eu.greenhouse.io/letsgetchecked/

Remote pacific time. Not good. This is the company of the guy who DM'd me on Reddit.

10am. Z said he would think about it 1.5 weeks, but since I haven't gotten a reply from him for this long, I guess I can forget about it. He is ghosting me. Though in the past he has taken a whole week to get back. I'd hoped he had gotten over this kind of tardiness, but I guess not.

I'll leave this completely out of mind. I won't mention his name ever again in this journal.

I gave this academic research engineering position a try and it did not work out. I need to move on to other opportunities.

Now...as I was saying earlier, let me beautify my Twitter profile. People will be checking out my Twitter page, so I want some better images in order to impress them.

10:20am. https://imgur.com/a/lBcfSqx

I put so much effort into this. Just how can one succeed in life?

10:25am. Oh it seems you can Ctrl+V images right into a Twitter post. That is cool.

10:45am. Let me upload ch 14 and ch 15 to Imgur. I'll really miss this.

11am. Damn it. 1 of 200 images is missing in the album, and I do not know which one it is.

...Why were they uploaded in such a weird order?

11:05am. I am going to find which image is missing by checking them 10 each. I'll find where it skips that way.

Damn it, how do I rearange the image in the album from the Images tab?

11:15am. Damn it. I do not know why this is happening, but it was not at all uploaded in the order I'd want it to be. It does not matter too much. But if I ever end up posting this on RR, I'll have to redo it.

Let me try it again.

11:20am. Uah, how much time is this going to waste me?

I guess I should have expected it.

11:25am. My slow internet connection is really killing me here. Well, uploading 400mb is not that easy.

11:30am. Let me try it again. 50 by 50.

If I move out of the page before the upload is done that can wreck things.

11:35am. I need to do this patiently. Let's do it correctly this time. I'll have to make sure I post the right twitter post this time as well.

11:45am. Finally uploaded it. Let me do the other 2 albums and then I'll post the Twitters.

11:50am. I should have done it 50 by 50 instead of all 70 at once. The upload got stuck on 70.

11:55am. It gave me a failure, but it seems the batch of 35 went through fine.

12:10pm. I missed an image somewhere and it broke things.

12:20pm. Finally uploaded it all to Imgur. Now let me upload the images to Twitter.

Wait, wait, wait. Have I been doing something really stupid? No. I was worried for a moment, it would be posting small sized images in Twitter, but these are fine.

12:30pm. Finally posted ch 14 on Twitter. Let me do ch 15.

1:15pm. https://www.linkedin.com/in/ghnogueira/

This guy actually was nice enough to refer me to the company. That PT is not pacific time, it probably part time. And the position is in Portugal. I've made a great mistake.

He sent me a referal link to LetsGetChecked, which is a remote F# position.

Let me have breakfast here. While I could study SQL, I really am going to start making Youtube videos instead. It is better to get some experience doing this than SQL. It will help me get over my nervousness.

2:30pm. Done with breakfast. Let me just reply to this communication. I've finished posting all the albums to Twitter. I meant to give a sneak peak into ch 17, but there are enough images there now.

https://twitter.com/Ghostlike

Here is the robotics guy.

///

That's a very good goal! Please let know if there's anything I could do to help you.

But let me tell that you are very capable! That's apparent from what you're working on, your ideas / understanding of quite complex topics, and the things you're trying to do. May I ask what resources are you referring to?

And please let me know once you discover better algorithms for AI robotics :D

///

I'll take the further correspondence private if this leads to a job opportunity.

///

> But let me tell that you are very capable! That's apparent from what you're working on, your ideas / understanding of quite complex topics, and the things you're trying to do. May I ask what resources are you referring to?
I have personal programming skills, but that is it. I do not have money or connections to start a company. Or social skills to lead it. My goal from the start was to do it with my personal power, and as long as I could get some better hardware to play with, I'd be happy. I want power over machines rather than people.

> That's a very good goal! Please let know if there's anything I could do to help you.
In the past few days, I've started looking for work. You can see my resume pinned on my Twitter along with some art I did for my web novel. If the startup you've mentioned could use somebody with my skills and doesn't mind that so far I've been a hobbyist, I'd like to apply there. Would you mind referring me to your company?

> And please let me know once you discover better algorithms for AI robotics :D
I wonder...I admit I am tempted to keep it a secret in order to just profit from it myself! Maybe if we end up working in the same company I would not mind sharing...

///

I can't forget to include the link.

...Emailed.

2:50pm. Let me post my Twitter in the SD sub.

https://www.reddit.com/r/StableDiffusion/comments/10lsh81/simulacrum_heavens_key_chapter_116_image_albums/

Here it is. No doubt, it will just get ignored.

3:05pm. Now what comes next?

This took so much of my energy today.

3:15pm. I really should record some screencasts instead of delaying this. I feel like calling it a day here, despite having not even started.

But I did needed to do this. Good art on my Twitter will help make a positive impression.

3:20pm. Let me try a screencast. I need to start getting used to talking to a camera. Let me commit here."

---
## [SHEHAN22000/Group-Project---Creating-Website](https://github.com/SHEHAN22000/Group-Project---Creating-Website)@[5c950cf7a0...](https://github.com/SHEHAN22000/Group-Project---Creating-Website/commit/5c950cf7a06a52f9d407a9a167d3bf8f497ca9e8)
#### Thursday 2023-01-26 14:43:52 by SHEHAN22000

Several important changes

1 - Logo and the Home btn file size reduced. You find the both PNG versions on GitHub.

2. All the pictures that I used for the home page are added to the GitHub as Hussain requested.

3. New updated HTML and CSS files added to the drive. After you complete your  Menu pages, Please add the link to the Breakfast, Lunch and Dinner buttons. I think you'll have use http://shell.hamk.fi/ and publish the page first. Get the link and add it to my code.

If you need any help with making images transparent(PNG), please contact me. If you have any questions, feel free to call/msg me on Whatsapp or leave a msg on teams.

---
## [saridormi/commits_dataset](https://github.com/saridormi/commits_dataset)@[1968d32693...](https://github.com/saridormi/commits_dataset/commit/1968d32693f7db17e0824f9da6004a6c291bf4ac)
#### Thursday 2023-01-26 15:14:44 by Alexandra Eliseeva

Prepare for next iteration

* Tweak data collection: we're collecting all commits now, not specific hashes
* Fix data logic in base class (it was actually wrong for collection, I guess I didn't run it for too long)
* Make RepoProcessor unrelated to BaseProcessor now (because it was kinda ugly)
* Update pydriller configuration: use -w option, support correct processing of date-related arguments (I want to use `since`)
* Support poetry, update requirements
* Update README

---
## [dependabot/dependabot-core](https://github.com/dependabot/dependabot-core)@[94c43d3dc7...](https://github.com/dependabot/dependabot-core/commit/94c43d3dc754997bf3415a7f3f4a5743c966a6c2)
#### Thursday 2023-01-26 15:37:21 by David Rodríguez

Make spec actually represent the real functionality

This is a weird one. Up until now, running the spec being changed here
in isolation fails:

```
$ bundle exec rspec spec/dependabot/bundler/update_checker_spec.rb:1183 --order defined --format documentation
Run options: include {:locations=>{"./spec/dependabot/bundler/update_checker_spec.rb"=>[1183]}}

Dependabot::Bundler::UpdateChecker
  #latest_resolvable_version
    given a gem with a git source
      that is not the gem we're checking
        that is private
          bundler v2
            updates the dependency (FAILED - 1)

Failures:

  1) Dependabot::Bundler::UpdateChecker#latest_resolvable_version given a gem with a git source that is not the gem we're checking that is private bundler v2 updates the dependency
     Failure/Error: raise Dependabot::GitDependenciesNotReachable, bad_uris.uniq

     Dependabot::GitDependenciesNotReachable:
       The following git URLs could not be retrieved: git@github.com:no-exist-sorry/prius
    # ...
    # ... stuff ...
    # ...

Finished in 3.35 seconds (files took 1.23 seconds to load)
1 example, 1 failure

Failed examples:

rspec ./spec/dependabot/bundler/update_checker_spec.rb:1183 # Dependabot::Bundler::UpdateChecker#latest_resolvable_version given a gem with a git source that is not the gem we're checking that is private bundler v2 updates the dependency
```

However, if I run the previous spec right before, it passes:

```
$ bundle exec rspec spec/dependabot/bundler/update_checker_spec.rb:1153:1183 --order defined --format documentation
Run options: include {:locations=>{"./spec/dependabot/bundler/update_checker_spec.rb"=>[1153, 1183]}}

Dependabot::Bundler::UpdateChecker
  #latest_resolvable_version
    given a gem with a git source
      that is not the gem we're checking
        is expected to eq #<Gem::Version "3.4.1">
        that is private
          bundler v2
            updates the dependency

Finished in 18.04 seconds (files took 1.48 seconds to load)
2 examples, 0 failures
```

The failing test is testing that if a git dependency is unreachable
(private) but we are updating a different dependency, it works.

However, in reality, it doesn't really work.

The fact that it's passing is just luck. The previous spec is
downloading a reachable gem at the exact same revision and putting it
into a cache that's shared among all specs.

Then the second spec will find the gem in the cache and just work
because it doesn't need to hit the network. This is not what happens in
real life, so the spec should not be passing.

This commit changes the locked reference of the fixture project used by
this spec to be a different one not shared by other specs, so that the
spec is forced to hit the network to pick the revision and fails,
representing the realworld behavior.

A better fix would be to remove this kind of side effects from the test
suite but I'll do that as a follow up.

---
## [zombieFox/kibana](https://github.com/zombieFox/kibana)@[afb09ccf8a...](https://github.com/zombieFox/kibana/commit/afb09ccf8a61d610e8e3d8beb2c80f413f1b33c5)
#### Thursday 2023-01-26 15:43:15 by Spencer

Transpile packages on demand, validate all TS projects (#146212)

## Dearest Reviewers 👋 

I've been working on this branch with @mistic and @tylersmalley and
we're really confident in these changes. Additionally, this changes code
in nearly every package in the repo so we don't plan to wait for reviews
to get in before merging this. If you'd like to have a concern
addressed, please feel free to leave a review, but assuming that nobody
raises a blocker in the next 24 hours we plan to merge this EOD pacific
tomorrow, 12/22.

We'll be paying close attention to any issues this causes after merging
and work on getting those fixed ASAP. 🚀

---

The operations team is not confident that we'll have the time to achieve
what we originally set out to accomplish by moving to Bazel with the
time and resources we have available. We have also bought ourselves some
headroom with improvements to babel-register, optimizer caching, and
typescript project structure.

In order to make sure we deliver packages as quickly as possible (many
teams really want them), with a usable and familiar developer
experience, this PR removes Bazel for building packages in favor of
using the same JIT transpilation we use for plugins.

Additionally, packages now use `kbn_references` (again, just copying the
dx from plugins to packages).

Because of the complex relationships between packages/plugins and in
order to prepare ourselves for automatic dependency detection tools we
plan to use in the future, this PR also introduces a "TS Project Linter"
which will validate that every tsconfig.json file meets a few
requirements:

1. the chain of base config files extended by each config includes
`tsconfig.base.json` and not `tsconfig.json`
1. the `include` config is used, and not `files`
2. the `exclude` config includes `target/**/*`
3. the `outDir` compiler option is specified as `target/types`
1. none of these compiler options are specified: `declaration`,
`declarationMap`, `emitDeclarationOnly`, `skipLibCheck`, `target`,
`paths`

4. all references to other packages/plugins use their pkg id, ie:
	
	```js
    // valid
    {
      "kbn_references": ["@kbn/core"]
    }
    // not valid
    {
      "kbn_references": [{ "path": "../../../src/core/tsconfig.json" }]
    }
    ```

5. only packages/plugins which are imported somewhere in the ts code are
listed in `kbn_references`

This linter is not only validating all of the tsconfig.json files, but
it also will fix these config files to deal with just about any
violation that can be produced. Just run `node scripts/ts_project_linter
--fix` locally to apply these fixes, or let CI take care of
automatically fixing things and pushing the changes to your PR.

> **Example:** [`64e93e5`
(#146212)](https://github.com/elastic/kibana/pull/146212/commits/64e93e580679dd55f4fdf19bd01402bc478a1a75)
When I merged main into my PR it included a change which removed the
`@kbn/core-injected-metadata-browser` package. After resolving the
conflicts I missed a few tsconfig files which included references to the
now removed package. The TS Project Linter identified that these
references were removed from the code and pushed a change to the PR to
remove them from the tsconfig.json files.

## No bazel? Does that mean no packages??
Nope! We're still doing packages but we're pretty sure now that we won't
be using Bazel to accomplish the 'distributed caching' and 'change-based
tasks' portions of the packages project.

This PR actually makes packages much easier to work with and will be
followed up with the bundling benefits described by the original
packages RFC. Then we'll work on documentation and advocacy for using
packages for any and all new code.

We're pretty confident that implementing distributed caching and
change-based tasks will be necessary in the future, but because of
recent improvements in the repo we think we can live without them for
**at least** a year.

## Wait, there are still BUILD.bazel files in the repo
Yes, there are still three webpack bundles which are built by Bazel: the
`@kbn/ui-shared-deps-npm` DLL, `@kbn/ui-shared-deps-src` externals, and
the `@kbn/monaco` workers. These three webpack bundles are still created
during bootstrap and remotely cached using bazel. The next phase of this
project is to figure out how to get the package bundling features
described in the RFC with the current optimizer, and we expect these
bundles to go away then. Until then any package that is used in those
three bundles still needs to have a BUILD.bazel file so that they can be
referenced by the remaining webpack builds.

Co-authored-by: kibanamachine <42973632+kibanamachine@users.noreply.github.com>

---
## [QuacksQ/Skyrat-tg](https://github.com/QuacksQ/Skyrat-tg)@[a57b142c1a...](https://github.com/QuacksQ/Skyrat-tg/commit/a57b142c1a4949ded1dcde1157ccf789fb21aabd)
#### Thursday 2023-01-26 15:52:26 by SkyratBot

[MIRROR] Basic mobs don't become dense upon death [MDB IGNORE] (#18679)

* Basic mobs don't become dense upon death (#72554)

## About The Pull Request

In #72260 what was previously a var became a flag, which was a sensible
change, however this inverted the default behaviour.
In virtually all cases we want dead mobs to _stop_ being dense, this
added a requirement for the flag to be present for that to happen and
then didn't add the flag to any mobs.

Rather than add this to every mob I inverted the function of the flag.
My reasoning here is that _simple_ mobs seemingly never required this
behaviour, basic mobs are probably going to need it rarely if ever, and
including it in `basic_mob_flags` by default seems messy and easy to
leave off when setting other flags (plus #72524 implies to me we want to
avoid adding more default values).

Setting this manually on each mob seems kind of silly as a requirement
going forward and I can't think of a way we'd unit test for people
forgetting.

For the same reason I did the same thing with the
`STOP_ACTING_WHILE_DEAD` flag I added to the AI controller in a recent
PR, the flag should denote unusual behaviour not the default.

## Why It's Good For The Game

It looks really odd when you're constantly shuffling places with dead
mobs, they're not supposed to do that.
It's tedious to add `STOP_ACTING_WHILE_DEAD` to every AI controller when
that should be an obvious default assumption.

## Changelog

:cl:
fix: Dead basic mobs are no longer "dense" objects and can be stepped
on.
/:cl:

* Basic mobs don't become dense upon death

* Removes a flag we didn't need anymore.

* Forgot to remove this one

Co-authored-by: Jacquerel <hnevard@gmail.com>
Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>
Co-authored-by: GoldenAlpharex <jerego1234@hotmail.com>

---
## [SOF3/PocketMine-MP](https://github.com/SOF3/PocketMine-MP)@[d9c70cb176...](https://github.com/SOF3/PocketMine-MP/commit/d9c70cb176c25bd67f7cab384428d6a9165f4539)
#### Thursday 2023-01-26 16:20:24 by Dylan K. Taylor

start.cmd: prevent idiotic behaviour when paths contain characters such as brackets
god I hate this shit so much

---
## [trunk-io/plugins](https://github.com/trunk-io/plugins)@[1a0b7ffe7f...](https://github.com/trunk-io/plugins/commit/1a0b7ffe7f5a1b34b5af6f6cf368041ae349ed94)
#### Thursday 2023-01-26 16:38:33 by Tyler Jang

Improve TaskFailure debug experience (#96)

The failure `detailPath` was formerly omitted, but passing in asymmetric
wrappers to `toMatchSpecificSnapshot` provides an alternative that
prints much more detailed failure information.

### Background
Improves CI and local experience of debugging when failures occur. This
has been a long time coming. Previous [failure
runs](https://github.com/trunk-io/plugins/actions/runs/3977200383/jobs/6818150578)
were painfully difficult to debug, particularly if they couldn't be
reproduced locally, and would often involve `cd`-ing into autodeleted
directories. Now, failure detail information is printed directly through
the use of asymmetric property matchers (see screenshot below).

![Screenshot 2023-01-21 at 11 39 16
PM](https://user-images.githubusercontent.com/42743566/213905613-a7f8e441-9017-4d81-b4eb-5a874c52d37d.png)

### Alternatives (that I considered and attempted)
1. Using custom serializers.
[jest-specific-snapshot](https://github.com/igor-dv/jest-specific-snapshot)
supports this, and there are decent
[documentation](https://jestjs.io/docs/expect#expectaddsnapshotserializerserializer)
and
[guides](https://medium.com/@luisvieira_gmr/jest-snapshot-serializers-6a96f5c362a1)
about how to approach this. However, whatever serialized output is
created is written to the snapshot file itself. This means that we would
have to save all of the detailPath contents (which presents numerous
problems, including nondeterministic paths), or none at all.
2. Ditching snapshots completely and using a stricter JSON approach.
This would be closer to the original approach, but it flies in the face
of recent work, including numerous QoL improvements, so I did not
thoroughly consider this option.
3. Using a custom asymmetric property matcher. There is also decent
documentation on [property
matchers](https://jestjs.io/docs/snapshot-testing#property-matchers) and
[guides](https://redd.one/blog/practical-guide-to-custom-jest-matchers).
There are a couple key problems, however. It is difficult or impossible
to write the actual contents of errors to snapshot files--they are
instead replaced with matcher names (see screenshot below). They are
also somewhat inflexible, particularly when used with
`jest-specific-snapshot`.
4. Wrapping expect in a try and rethrow. This
[suggestion](https://stackoverflow.com/a/55097584) was made, and it
would be a bit more general for the purposes of providing debug
information, but it would require significant custom code in order to
determine what the desired message to print would be. TaskFailures are
the primary focus here.
5. Using built-in asymmetric property matchers. The final approach that
I took is similar to option 3, but adds a bit more custom hacky code in
order to ensure that as much useful information is written to the
snapshot as possible. I use property matchers mapped to each individual
taskFailure, and I apply them conditionally based on the test state and
whether or not I have computed that failure to be present in the
snapshot (see comments in `tests/utils/index.ts`). The only operational
downside is that replacing existing snapshots with failure content
becomes a bit more difficult, but not significantly.

### Follow-up Work
- I may consider also including debug information such as the
trunkVersion and the linterVersion. If necessary, these wrappers can
also be expanded to include other useful information through additional
asymmetric matchers (custom or built-in).
- I may also integrate
[retries](https://www.npmjs.com/package/jest-retries) if flaky failures
are determined to be due to network issues after this PR brings out new
insights.

Alternative 3
![Screenshot 2023-01-21 at 11 45 52
PM](https://user-images.githubusercontent.com/42743566/213905770-d8737589-cb6b-4700-89de-7d112574b5c1.png)

Co-authored-by: Chris Clearwater <chris@trunk.io>

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[c7a40a8e69...](https://github.com/mrakgr/The-Spiral-Language/commit/c7a40a8e697ad2cb3d46f3f56b7e8bbf9f6837d0)
#### Thursday 2023-01-26 17:35:40 by Marko Grdinić

"3:45pm. This is really difficult. The Internet personalities make it look easy. Let me forget the webcam for a bit. It kind of dangles awkwardly on my monitor and it is hard to set it up properly. Once I get a job I'll definitely get a better one.

I really should just write a script. It is surprisngly difficult to do this in the spur of the moment. But let me just keep trying.

3:50pm. Right now I am out of it, but I should get into it over the next few days.

4pm. I've barely spoken for a few minutes and already I am feeling tired. Let me replay it so I can get a sense of how I sound, but it should be horrible. I am always struggling for words.

4:05pm. Ok, what is really surprising here is that the screencast ended up being 3 minutes. How is it possibly so long?

Hmm, the file once saved comes down to 87mb. No doubt the compressed version would be smaller.

4:10pm. Uah, I am feeling so lethargic about this.

...My rules for programming when I feel like this are to just sit in place and think. Like when I can't program, the best thing to do is to just turn off the screen, and go away from the computer. Take a nap.

I am going to pass on advertizing my Paperspace GPU fetcher script for now. The way to use SD on Paperspace should be its own series, and right now I can't convince anything of anybody.

How about I just do a Spiral tutorial. I already have the script in the form of the manual. Ad libing, doing it off the cuf, forget about that. Simplify. Let me do a poor Spiral tutorial from start to finish. Then I will repeat and refine. And edit.

4:30pm. I recorded 8 minutes of tutorial video just now. This is okay. Let me just go at it like this. I know I am horrible, but as I keep doing this I'll ease up.

What I want to do now is make a recording of me installing the Ionide extension.

4:45pm. Ah, I see. When I make subsequent screen captures it adds them to the tab to the left. This screencast where I installed the Ionide extension ended up being seamless.

4:50pm. I am kind of getting into it. This is important. Maybe that showing the people a professionaly done product, I should just play around instead. Take it easy and such.

5:50pm. After that second recording I went to take a nap and I thought about it.

I have some conclussions.

1) My voice itself is not bad. I have a weird accent, but nonetheless I am quite understandable.

2) I realized what my problem was. The times I feel insecure is when I fall into the situation of just explaining somethnig.

Should I be explaining this? Should I be explaining that? It is like my goals are in conflict and I start being pressured. When I started focusing on doing, how to compile a program for example, the time started going quickly for me and I started going into the zone.

I think I can make this work. Maybe not professionally, but...

6:15pm. Done with lunch.

What I wanted to say basically, is that usually think about many things at once, and that is not good when I am trying to talk. When I open my mouth I should have a clear goal in mind.

For example, either explaining Stable Diffusion or demonstrating Paperspace, but not both.

6:20pm. I've always had trouble with this in school. Forget about reciting a script. Just make a goal and follow it. Focus on the single goal as much as possible. That is what is going to get me good at making screencasts. I feel like I might be able to grasp it tomorrow, but right now I do not feel like it.

I am not going to write HK today, I feel like unwinding. Hell, at this point I must have been awake over 12h.

6:35pm. That thread I posted on the SD sub got burried. It is really the hardest thing in the world to be successful. HK is really breaking my heart.

Power. I wish I had power...

Maybe I will try writing just a little..."

---
## [FIJTeam/eternitystation](https://github.com/FIJTeam/eternitystation)@[66b7310039...](https://github.com/FIJTeam/eternitystation/commit/66b7310039297843b01c5b14a9b59180909ab52c)
#### Thursday 2023-01-26 17:50:29 by Rhials

STAY IN THE LIGHT: Adds terrify Nightmare spell, terrified status effect, and a reason to mind the shadows (#72282)

Adds the Terrify spell, and its associated status effect, Terrified.
This new spell is given to antagonist nightmares, as a part of their
brain. The spell only works in those surrounded by darkness, and will
apply the Terrified status effect if successful. Upon being Terrified,
victims will passively gain **Terror Buildup** if they remain in the
dark. As buildup increases, so do the negative effects, including tunnel
vision, panic attacks, dizziness, and more.

There are two primary methods for mitigating terror buildup. The first
is moving into the light, which will reverse the passive terror buildup
and eventually make it go away. The other method is by getting a hug
from a friendly hand, which will reduce buildup significantly.

Getting a hug from an UNfriendly hand (a nightmare, for instance) will
cause the victim to freak out and be briefly knocked down. This can be
spammed on targets who are caught alone in the dark, keeping them in an
unfavorable position (sideways) and adding to the victim's terror
buildup considerably. Escape into the light as soon as possible, or
you'll be pushed to MAXIMUM TERROR BUILDUP.

To what end? Heart failure. Past the soft terror cap (which limits how
much passively generated terror you can make) exists the hard terror
cap. Bypassing that threshold will cause a stress induced heart attack
and knock you unconscious (embarrassing!)

---
## [RedbackThomson/ack-test-infra](https://github.com/RedbackThomson/ack-test-infra)@[95e4857b28...](https://github.com/RedbackThomson/ack-test-infra/commit/95e4857b28122c6c5f8a30260be3dcac94e0e466)
#### Thursday 2023-01-26 18:31:40 by Amine

Move Go binaries to `/usr/bin` (#287)

Issue https://github.com/aws-controllers-k8s/community/issues/1640

TL;DR: Prow was mounting `test-infra` code volume into `$GOPATH`
causing the deletion of `kind` and `controller-gen` binaries that are
installed in `$GOPATH/bin`


Yesterday, i embarked on a wild 7 hour journey to fix a bug that had
been causing prow jobs to fail with the error message "Kind not found".
The bug was introduced after a recent update that bumped the Go compiler
to `1.19`. I found the investigation to this bug to be both interesting
and frustrating, so i wanted to share some key takeways with the
community:

[The patch](https://github.com/aws-controllers-k8s/test-infra/commit/14dda81ce8ea430b51c9ce738483bea3744a5450) that introduced Go `1.19` also modified a `go get` command
into a `go install` command (because of this deprecation notice:
https://go.dev/doc/go-get-install-deprecation), which technically should
not have caused any issues. I tried restarting the e2e jobs in various
repositories to figure out whether the error was only related to one
controller or code-generator only, but all the repositories that execute
e2e tests were affected.

First, i started suspecting that thee `go install` command was not
working properly or had not been used correctly. I experiemented with it
locally, using various combinations of `GOPATH` and `GOBIN`, however, i
learned that the Go compiler is sophisticated enough to always put
downloaded binaries under `GOBIN` or `GOPATH/bin`. I then wondered if
the `PATH` variable didn't include the `GOBIN` path, which is supposed
to contain the `kind` and `controller-gen` binaries. I spent some time
reading the Dockerfiles and testing scripts, but they all set `GOPATH`
and always included a `GOBIN` in the `PATH` variable.

I also suspected that the issue may be related to the containers, but
experimentations with "Go containers" and environement variables
manipulation did not yield any results. I also tried building minimal
DOckerfiles to try to reproduce the issue, but that also did not give
any clues.

At this point, I suspected the container image it self. I build an image
locally and ran a shell inside it, but everythin g looked fine. THe
`kind` and `controller-gen` binaries were present and the `PATH` and
`GOPATH` variables were properly set. I then suspect that we may have a
corrupted published image in ECR, but pulling the image and running the
same commands revealed that the image was fine.

I then took a break from experimenting with Go/Docker/Envvars and tried
to spin some prowjobs with `v0.0.10` and `v0.0.9` (the last two versions
that were still using Go 1.17) of the integration tests image. This
confirmed that the issue was only with `v0.0.11`.

So, I decided to investigate further and logged in the Prow production
cluster. My first attempt was to restart a job and try to "exec bash" in
it, but the jobs failed to quickly for that to be possible. I then ran
a custom prow job (with `v0.0.11` integration image tag) but with a
`sleep 10000` command. When looking inside, there were no `kind` or
`controller-gen` binaries, i searched the entire file system, they were
nowhere to be found, grep, find, name it all.. nada. I then execute a
`go install sigs.k8s.io/kind@v0.17.0"`, and bam, it worked, the binary
was here again. The same thing happened with controller-gen. So for now
we know that we ship images with all the necessary binaries and when a
prow job starts, they disapear...

To isolate the problem further, i created a `ProwJob` resource and
copied the `Pod` (spawned by Prow) spec and metadata into a different
file. Running the same commands used previously proved that indeed
something is wrong with the pod spec, causing the binaries to disapear.
And when a file disppears it reminds me of my college years, where i
epically failed to use symbolic links, which is a bit similar (at least
from a UX point) to volume mounts in the Docker world.

So, i decided to check the volume mounts, and to my not-surprise, I
found this:

```yaml
    - mountPath: /home/prow/go
      name: code
```

Yes... Prow is mounting the test-infra source code into `GOPATH`
(`/home/prow/go` in prow jobs) ! Which is the parent directory of
`GOBIN` where we install the binaries. And it all makes sense now.
Mounting code into this directory overrides the existing volume and
deletes everything existing in `GOPATH` including the binaries we
installed before.

The Dockerfile was missing the `mv` commands that puts `kind` and
`controller-gen` in `/usr/bin`. To fix this issue, I added the missing
`mv` command to the docker file and published and new `integration`
image `v0.0.12`.

---

Anyways, investigating the source of the volume mount led me to the Prow
presets configurations. Presets are a set of configurations (volume
mounts, environement variables, etc...) that are used for jobs with
specific labels in their metadata. I tried to play with this in our Prow
cluster, but quickly stoped when it was a bit risky and could break
other components too. While digging into `test-infra` pod-util package i
learned that the code volume is not coming from our defined presets and
is a default preset coming from Prow it self - the `/home/prow/go` value
is harded-coded in `prow/pod-utils/decorate/podspec.go#L54`. I'm not
sure whether we can override this value.

Anyways, for now, i'm just gonna implement a quick fix that moves the
binaries to `/usr/bin` instead of leaving them inside `GOBIN`. Ideally
we should either choose a new directory go `GOPATH` that is different
from `$HOME/go` or find a solution that will let the code and our
binaries coexist in the same place. Either of them requires a lot of
changes and can agressively break some our prow components/scripts.

@jljaco is currently workng on creating a staging cluster, which will
provide us a safe environementto test and experiment with new
configurations. This will allow us to try out new changes without having
to woryy about potentially impacting the production environement.

Signed-off-by: Amine Hilaly <hilalyamine@gmail.com>

By submitting this pull request, I confirm that my contribution is made under the terms of the Apache 2.0 license.

---
## [oaisd-ctc/Underloading](https://github.com/oaisd-ctc/Underloading)@[8dbbaeaef2...](https://github.com/oaisd-ctc/Underloading/commit/8dbbaeaef2c44ee3190a7d759b1d0bf99c2dc328)
#### Thursday 2023-01-26 19:20:50 by Lukas Batema

"Alright guys, [cough] I'm doing 'Take On Me' now, alright. I, I really, I really like this song, it sounds good."

Minin' away
I don't know what to mine
I'll mine this anyway
In this Minecraft day
So beautiful, mine further down
What's that I found?
Mine diamonds (Take on me)
Mine diamonds (Take on me)
I'll mine them
So far I've got two!
So easy to mine
With my Minecraft pickaxe and shovels
Hopefully they stay
In my Minecraft chests
So I'm gonna make
A lock on it
Mine diamonds (Take on me)
Mine diamonds (Take on me)
I'll mine them
So far I've got two!
"Ah! [cough, cough, cough, cough, sniff, cough]
I'm alright, I'm ready"
All these diamonds
Sittin' carefully lay
I'm getting worried ("Shut the fucking door!")
If they might get stolen
From my ender chest
Wait, who is that?
Holy sheep, it's Notch!
Mine diamonds (Take on me)
Mine diamonds (Take on me)
Now they're safe
Woahhhhhhhhhhhhhhhhh!
Now...
Now that they're safe
Woahhhhhhhhhhhhhhhhh!
Mine diamonds, [heavy breathing] (Take on me)
Mine diamonds (Take on me)
"Uh, Thanks, thanks for listening guys and thanks for recommending this song"

---
## [dylanfeehan/dategen](https://github.com/dylanfeehan/dategen)@[14b6350dda...](https://github.com/dylanfeehan/dategen/commit/14b6350ddae60f5acecf0f4596d1a1d14bfcf77b)
#### Thursday 2023-01-26 20:32:48 by dylanfeehan

pain in the fucking ass carousel. stretch goal will be to make dynamic...

---
## [CDCgov/prime-reportstream](https://github.com/CDCgov/prime-reportstream)@[8b92a1e515...](https://github.com/CDCgov/prime-reportstream/commit/8b92a1e515d1f0e0c68d9471fcb1163432dae487)
#### Thursday 2023-01-26 22:06:07 by Stephen Kao

Experience-7891: Disable organization-specific fetches as admin (#7928)

This changeset disables a few Organization-specific requests to mitigate the number of 404s we're getting as admins try to fetch Organization resources:
- Organization settings
- Deliveries
- Submissions

There's not a one-size-fits-all solution here given the different fetch mechanisms we already have and how the data is rendered, so I tried to add minimal changes to prevent disrupting anything down the line.  I think going forward, we can make a generic `useOrganizationQuery` hook that'll automatically be disabled if the user is logged in as an admin without impersonating an Organization.  There are a lot of layers with our fetching that in my opinion should be untangled, but that's out of the scope of this pull request.

---
## [majcosta/source](https://github.com/majcosta/source)@[57d2674f37...](https://github.com/majcosta/source/commit/57d2674f3779ea7881fd678c292a056278cd4569)
#### Thursday 2023-01-26 22:08:37 by majcosta

Use a modifiable user-preset sample for VS 2022/2019 (#97)

* Use a modifiable user-preset sample for VS 2022/2019

Customizing a repo-tracked preset file doesn't work:

Type in your gamedir for debugging, or toggle verbose mode for the build, or configure Chinese
UB MapEditor: you now have an unstaged `CMakePresets.json` change in your working directory.
very annoying.

Also, Visual Studio 2022's preset support has a bug: if you have a `CMakePresets.json` file,
no matter in which file (user or repo) the preset you have selected is defined, if you click
"Manage Configurations..." it will always open `CMakePresets.json` for editing, setting the
user up for failure and editing the commited-to-repository file.

Having just the `CMakeUserPresets.json` file also sidesteps another poor Visual Studio 2022
decision: hiding in Folder View files that are .gitignore'd (like `CMakeUserPresets.json`).

In the absence of a `CMakePresets.json` file, selecting "Manage Configurations..." will open
the right file for editing.

The workflow is then:

Copy `CMakeUserPresets.json.sample` into `CMakeUserPresets.json` _once_, then customize
that to your heart's content without git bothering you and accidentally adding an
unwanted change to a patch. Or make your own.

* Added auto-copy of profile template.

* declutter things a bit

move function out of root cmakelists.txt file
move user preset template to a presets directory

this is horrible and I hate it

Co-authored-by: CptMoore <39010654+CptMoore@users.noreply.github.com>

---
## [andyyang890/cockroach](https://github.com/andyyang890/cockroach)@[506035b80e...](https://github.com/andyyang890/cockroach/commit/506035b80e6ac83f1042aba6a42c0f526df5ba5b)
#### Thursday 2023-01-26 22:14:09 by craig[bot]

Merge #93270 #94102 #94147

93270: sql, server: implement and write to new recent statements cache r=amyyq2 a=amyyq2

This change implements and tests a new RecentStatementsCache that is used to store the recent statements that were executed. The cache has two new cluster settings that tune the capacity and time that a statement lives in the cache.

This change also implements writing ActiveQueries to the cache. The RecentStatementsCache is added to the ExecutorConfig, and the Server writes to this cache whenever a non-internal statement finishes. This change also removes queryMeta.phase, and replaces it with ActiveQuery.Phase. The phases Canceled, Timed Out, Completed, and Failed are also as possible values to ActiveQuery.Phase.

Part Of #86955
Fixes #91556

Release note: None

94102: build: add tooling to mirror NPM dependencies to GCS r=sjbarag a=sjbarag

Note that this doesn't actually _apply_ these changes yet! That'll happen in a separate PR so we can have a better discussion about the mechanics involved here (and also to make backporting significantly simpler)

-----

CockroachDB's NPM dependencies are currently provided by the git
submodule in pkg/ui/yarn-vendored [1] and are installed during the
Bazel build with the '--offline' flag [2] to avoid relying on public
NPM registries. Bazel's rules_nodejs unfortunately doesn't work well
with dependencies that are vendored on-disk in the Bazel workspace via
yarn-offline-mirror, which led to some unfortunate hacks [3,4] being
introduced during the initial Bazel setup.

In the time since those hacks were added, two significant events
occured:

1. Bazel's rules_nodejs was deprecated in favor of rules_js [5], which
   manually implements the pnpm resolver algorithm and doesn't support
   yarn's yarn-offline-mirror configuration value.
2. Bazel 6 was released [6], which removed the 'managed_directories'
   attribute to the top-level workspace() rule that makes yarn_install
   work in CockroachDB at all.

The use of yarn-vendored therefore blocks both migration away from
rules_nodejs and an upgrade to Bazel 6.

Instead of relying on a git submodule and --offline installation,
it's possible to use the pattern already used by CockroachDB's go
dependencies: copy them from public locations to a storage bucket
managed by Cockroach Labs, then ensure the bucket is used for future
downloads. Doing so allows the yarn_vendored submodule and --offline
installation to be removed in favor of _online_ builds from a location
Cockroach Labs controls, thus unblocking both a migration away from
rules_nodejs and an upgrade to Bazel 6.

Add a //pkg/cmd/mirror/npm tree (and supporting ./dev tooling) that
downloads NPM dependencies from public registries, uploads them to a
public-readable bucket, and rewrites yarn.lock files to use that bucket,
along with a test to ensure those mirrored dependencies continue to be
used in the future.

[1] https://github.com/cockroachdb/yarn-vendored
[2] https://classic.yarnpkg.com/en/docs/cli/install#toc-yarn-install-offline
[3] ./build/bazelutil/seed_yarn_cache.bzl
[4] ./build/bazelutil/seed_yarn_cache.sh
[5] https://blog.aspect.dev/rulesjs-launch
[6] https://github.com/bazelbuild/bazel/releases/tag/6.0.0

Part of: https://github.com/cockroachdb/cockroach/issues/85038
Release note: None

94147: release: pass GCS credentials to publish-provisional-artifacts r=rickystewart a=rail

Previously, publish-provisional-artifacts requires `GOOGLE_APPLICATION_CREDENTIALS` environment variable when `--gcs-bucket` is passed. This was not the case for the case where we upload the latest binaries (`--bless`).

This PR adds required steps to set up and pass the credentials.

Epic: none
Release note: None

Co-authored-by: amyyq2 <amy.qian@cockroachlabs.com>
Co-authored-by: Sean Barag <barag@cockroachlabs.com>
Co-authored-by: Rail Aliiev <rail@iqchoice.com>

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[040f6c37bf...](https://github.com/git-for-windows/git/commit/040f6c37bfcc30c5f4c6001ef675908dc17adcf8)
#### Thursday 2023-01-26 22:53:21 by Johannes Schindelin

windows: ignore empty `PATH` elements

When looking up an executable via the `_which` function, Git GUI
imitates the `execlp()` strategy where the environment variable `PATH`
is interpreted as a list of paths in which to search.

For historical reasons, stemming from the olden times when it was
uncommon to download a lot of files from the internet into the current
directory, empty elements in this list are treated as if the current
directory had been specified.

Nowadays, of course, this treatment is highly dangerous as the current
directory often contains files that have just been downloaded and not
yet been inspected by the user. Unix/Linux users are essentially
expected to be very, very careful to simply not add empty `PATH`
elements, i.e. not to make use of that feature.

On Windows, however, it is quite common for `PATH` to contain empty
elements by mistake, e.g. as an unintended left-over entry when an
application was installed from the Windows Store and then uninstalled
manually.

While it would probably make most sense to safe-guard not only Windows
users, it seems to be common practice to ignore these empty `PATH`
elements _only_ on Windows, but not on other platforms.

Sadly, this practice is followed inconsistently between different
software projects, where projects with few, if any, Windows-based
contributors tend to be less consistent or even "blissful" about it.
Here is a non-exhaustive list:

Cygwin:

	It specifically "eats" empty paths when converting path lists to
	POSIX: https://github.com/cygwin/cygwin/commit/753702223c7d

	I.e. it follows the common practice.

PowerShell:

	It specifically ignores empty paths when searching the `PATH`.
	The reason for this is apparently so self-evident that it is not
	even mentioned here:
	https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_environment_variables#path-information

	I.e. it follows the common practice.

CMD:

	Oh my, CMD. Let's just forget about it, nobody in their right
	(security) mind takes CMD as inspiration. It is so unsafe by
	default that we even planned on dropping `Git CMD` from Git for
	Windows altogether, and only walked back on that plan when we
	found a super ugly hack, just to keep Git's users secure by
	default:

		https://github.com/git-for-windows/MINGW-packages/commit/82172388bb51

	So CMD chooses to hide behind the battle cry "Works as
	Designed!" that all too often leaves users vulnerable. CMD is
	probably the most prominent project whose lead you want to avoid
	following in matters of security.

Win32 API (`CreateProcess()`)

	Just like CMD, `CreateProcess()` adheres to the original design
	of the path lookup in the name of backward compatibility (see
	https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessw
	for details):

		If the file name does not contain a directory path, the
		system searches for the executable file in the following
		sequence:

		    1. The directory from which the application loaded.

		    2. The current directory for the parent process.

		    [...]

	I.e. the Win32 API itself chooses backwards compatibility over
	users' safety.

Git LFS:

	There have been not one, not two, but three security advisories
	about Git LFS executing executables from the current directory by
	mistake. As part of one of them, a change was introduced to stop
	treating empty `PATH` elements as equivalent to `.`:
	https://github.com/git-lfs/git-lfs/commit/7cd7bb0a1f0d

	I.e. it follows the common practice.

Go:

	Go does not follow the common practice, and you can think about
	that what you want:
	https://github.com/golang/go/blob/go1.19.3/src/os/exec/lp_windows.go#L114-L135
	https://github.com/golang/go/blob/go1.19.3/src/path/filepath/path_windows.go#L108-L137

Git Credential Manager:

	It tries to imitate Git LFS, but unfortunately misses the empty
	`PATH` element handling. As of time of writing, this is in the
	process of being fixed:
	https://github.com/GitCredentialManager/git-credential-manager/pull/968

So now that we have established that it is a common practice to ignore
empty `PATH` elements on Windows, let's assess this commit's change
using Schneier's Five-Step Process
(https://www.schneier.com/crypto-gram/archives/2002/0415.html#1):

Step 1: What problem does it solve?

	It prevents an entire class of Remote Code Execution exploits via
	Git GUI's `Clone` functionality.

Step 2: How well does it solve that problem?

	Very well. It prevents the attack vector of luring an unsuspecting
	victim into cloning an executable into the worktree root directory
	that Git GUI immediately executes.

Step 3: What other security problems does it cause?

	Maybe non-security problems: If a project (ab-)uses the unsafe
	`PATH` lookup. That would not only be unsafe, though, but
	fragile in the first place because it would break when running
	in a subdirectory. Therefore I would consider this a scenario
	not worth keeping working.

Step 4: What are the costs of this measure?

	Almost nil, except for the time writing up this commit message
	;-)

Step 5: Given the answers to steps two through four, is the security
	measure worth the costs?

	Yes. Keeping Git's users Secure By Default is worth it. It's a
	tiny price to pay compared to the damages even a single
	successful exploit can cost.

So let's follow that common practice in Git GUI, too.

Signed-off-by: Johannes Schindelin <johannes.schindelin@gmx.de>

---
## [XebetaDefasado/TestRepository](https://github.com/XebetaDefasado/TestRepository)@[af02a5eff0...](https://github.com/XebetaDefasado/TestRepository/commit/af02a5eff01bd1cce1b8387a9431c264624048a0)
#### Thursday 2023-01-26 22:58:21 by XebezeraDefasado

What the fucking hell is this shit called whitespace

---
## [aecyia/February](https://github.com/aecyia/February)@[17c3ad913f...](https://github.com/aecyia/February/commit/17c3ad913f378bd90cadeb45c8bdfab8da359246)
#### Thursday 2023-01-26 23:07:01 by aecyia

MEMORY -- Read # Different Books Fix

+ ORIGINAL -- {2.SimName} has been spending a lot of time at the bookstore and has read {0.Number} unique books. {MA.He}{FA.She} will remember the laughs, tears, and the giant papercuts!
+ CHANGED -- {2.SimName} has been spending a lot of time with books and has read {0.Number} unique ones. {MA.He}{FA.She} will remember the laughs, tears, and the giant papercuts!
+ REASON -- My toddler Sim read toddler books and got the memory without visiting the bookstore. Changed to be more universal with different situations.

---

