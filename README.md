## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-07-26](docs/good-messages/2023/2023-07-26.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,293,383 were push events containing 3,578,843 commit messages that amount to 281,168,740 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 66 messages:


## [kwautztretschke/MqttClient](https://github.com/kwautztretschke/MqttClient)@[2a0b359b8f...](https://github.com/kwautztretschke/MqttClient/commit/2a0b359b8f01ed011f6798e02e3d5b040a858c58)
#### Wednesday 2023-07-26 00:00:23 by Bernhard Stöffler

status quo pre generalization

+defines for lights (tested roomlight but not shisha so far)

+brightness functionality

+small fix: when brightness 0: changeLightColor: brightness = 255

+bu2bl2, status quo

+fade, +struct s_rgb

+correct blending with white

+Whiteboard -brightness 100 on new color

+table

~ips, ~credentials

changed project name

Create README.md

Update README.md

Update Zimmerlicht.cpp

Sanitize a bit

Update README.md

+Kicad Files +gitignore

kicad: +first routing example

kicad: +4th transistor

renamed file

migrated to platformIO

added VSCode workspace

added hidden folders to gitignore, removed kicad

added PubSubClient to libraries

+reference files for pubsubclient

added thoughts to readme

more thoughts

+thoughts ~bulletpoints

more markdown shenanigans

god i fucking hate markdown

end me

i never want to use markdown ever again

renamed deprecated firmware

+ new firmware outline

moved reference files to /examples

fix compiler errors

removed credentials, fixed connecting to broker, IT WORKS

put MqttClient in a module

added submodule for kicad footprints

fixed esp footprint in kicad schematic

updated esp schematic file to eeschem 2.4

added buck converter K7803JT-500R3-LB

cleaned up schematic a bit
removed false footprints and added new buck converter

added schematic for ws2812 strip

added some labels and a reset button

schematic first revision

maintenance, gitignore, platformio.ini

restarted from scratch, basic blink

+simple mqtt color code receiver

modularized programManager, fixed formatting

callbacks and cleanup
* added callbacks to mqttclient for interfacing with program manager
* added backup wificredentials

MqttClient: fixed callbacks, +topic handling

expanded ProgMan, added Program

Implemented ProgramManager

Added Hardware, Fixed ProgramManager

Move files to the library directory

---
## [effigy-se/effigy-se](https://github.com/effigy-se/effigy-se)@[7e1d97af9e...](https://github.com/effigy-se/effigy-se/commit/7e1d97af9e4b6b7f90fbacc754fae939b6d16e49)
#### Wednesday 2023-07-26 00:24:03 by Justice

Removes the word "chemical" from "chemical patch" (#76966)

## About The Pull Request
In #76011, I bitched and moaned about how the ChemMaster gives patches a
huge ass name. I've talked to other Medical Doctor mains and I also
heard bitching about the word "chemical", which is just a pain in the
ass. It seems many of us just end up removing it because it's so
repetitive and makes the patch's name long fnr. I don't think the word
"chemical" is really needed in there since you can clearly tell it's a
chemical patch just by looking at the word "patch" and the sprite.

I don't think this should affect anything else in the game in a negative
way. In that same issue, it was suggested that the cap for names was
increased instead, but this also solves the issue of the word "chemical"
taking up so much space in the patch's name without touching unknown
lands.
## Why It's Good For The Game
Less words, more healing!
## Changelog
:cl:
qol: The word "chemical" has been removed from "chemical patch" when
printing patches
/:cl:

---
## [effigy-se/effigy-se](https://github.com/effigy-se/effigy-se)@[0d769e0ffa...](https://github.com/effigy-se/effigy-se/commit/0d769e0ffaaa2b0f2be2edb9659c233860420ec1)
#### Wednesday 2023-07-26 00:24:03 by Jacquerel

Removes two redundant components (#76866)

## About The Pull Request

We're starting to get to have enough components that people don't
realise that what they want already exists but doesn't have the name
they expect 🙃

I recently added `track_hierarchical_movement` which is similar enough
to `connect_containers` that it shouldn't independently exist, even if I
like sending a new signal more than the ugly setup pattern for
`connect_loc`.

`trait_loc` is actually older than `give_turf_traits` but
`give_turf_traits` covers more edge cases than `turf_loc` so seems like
the better one to maintain.
HOWEVER `give_turf_traits` held a list of references to atoms in it,
which isn't great in an element. I couldn't think of a way to completely
eliminate the list, but it isn't a list of references any more so it
shouldn't cause any hard deletions.

## Why It's Good For The Game

Having two components which do the same thing but marginally differently
is confusing and going to cause us trouble down the line.

## Changelog

Not player facing

---
## [SmiteWindows/rust](https://github.com/SmiteWindows/rust)@[4fc6b33474...](https://github.com/SmiteWindows/rust/commit/4fc6b33474680ba57e10d56371c2c3df91788e26)
#### Wednesday 2023-07-26 00:33:22 by bors

Auto merge of #114011 - RalfJung:place-projection, r=oli-obk

interpret: Unify projections for MPlaceTy, PlaceTy, OpTy

For ~forever, we didn't really have proper shared code for handling projections into those three types. This is mostly because `PlaceTy` projections require `&mut self`: they might have to `force_allocate` to be able to represent a project part-way into a local.

This PR finally fixes that, by enhancing `Place::Local` with an `offset` so that such an optimized place can point into a part of a place without having requiring an in-memory representation. If we later write to that place, we will still do `force_allocate` -- for now we don't have an optimized path in `write_immediate` that would avoid allocation for partial overwrites of immediately stored locals. But in `write_immediate` we have `&mut self` so at least this no longer pollutes all our type signatures.

(Ironically, I seem to distantly remember that many years ago, `Place::Local` *did* have an `offset`, and I removed it to simplify things. I guess I didn't realize why it was so useful... I am also not sure if this was actually used to achieve place projection on `&self` back then.)

The `offset` had type `Option<Size>`, where `None` represent "no projection was applied". This is needed because locals *can* be unsized (when they are arguments) but `Place::Local` cannot store metadata: if the offset is `None`, this refers to the entire local, so we can use the metadata of the local itself (which must be indirect); if a projection gets applied, since the local is indirect, it will turn into a `Place::Ptr`. (Note that even for indirect locals we can have `Place::Local`: when the local appears in MIR, we always start with `Place::Local`, and only check `frame.locals` later. We could eagerly normalize to `Place::Ptr` but I don't think that would actually simplify things much.)

Having done all that, we can finally properly abstract projections: we have a new `Projectable` trait that has the basic methods required for projecting, and then all projection methods are implemented for anything that implements that trait. We can even implement it for `ImmTy`! (Not that we need that, but it seems neat.) The visitor can be greatly simplified; it doesn't need its own trait any more but it can use the `Projectable` trait. We also don't need the separate `Mut` visitor any more; that was required only to reflect that projections on `PlaceTy` needed `&mut self`.

It is possible that there are some more `&mut self` that can now become `&self`... I guess we'll notice that over time.

r? `@oli-obk`

---
## [space-wizards/space-station-14](https://github.com/space-wizards/space-station-14)@[31607a0be0...](https://github.com/space-wizards/space-station-14/commit/31607a0be0e2ef24f4d53c7611172ec6d40a3a2b)
#### Wednesday 2023-07-26 00:35:01 by Emisse

hardsuit/firesuit cleanup (#18308)

* real

* hjoly fuck you guy sare annoying

* fix cargo arbitrage idk why tf it changed from editing armor values but fuck my life i guess

* why god

* Update suits.yml

* Update cargo_emergency.yml

---
## [dtolnay-contrib/rules_rust](https://github.com/dtolnay-contrib/rules_rust)@[80f0eb488a...](https://github.com/dtolnay-contrib/rules_rust/commit/80f0eb488ab9cabc4920ac446478cbf2feedc3f3)
#### Wednesday 2023-07-26 00:35:09 by scentini

Support for `no_std` mode (#1934)

Initial support for `no_std` mode.
This allows us to
1. Don't pass the whole standard library to compile actions that specify `no_std`
2. Conditionally select `crate_features` and `deps` based on whether `no_std` mode is used.
Currently the only supported modes are `off` and `alloc`, with a possibility to expand in the future.

The `no_std` support comes with the following caveats:
1. Targets in `exec` mode are still built with `std`; the logic here being that if a device has enough space to run bazel and rustc, std's presence would not be a problem. This also saves some additional transitions on `proc_macro`s (they need `std`), as they are built in `exec` mode.
2. Tests are still built with `std`, as `libtest` depends on `libstd`

There is quite an ugly hack to make us be able to `select` on the `no_std` flavor taking `exec` into account; I'm looking forward to the day where Bazel will expose better ways to inspect the cfg.

There is also one part I didn't manage to make work - having a `rust_test` that tests the `rust_shared_library` in `cc_common.link` mode; I got a link error for missing `__rg_alloc` & co. symbols, which should be present as we pass `--@rules_rust//rust/settings:experimental_use_global_allocator=True`. Unfortunately I could only spot this error on CI, and could not reproduce locally. I removed the test because the `rust_shared_library` is already tested via a `cc_test`. I will however give another shot at inspecting how my local setup differs from CI.

The `rust_binary` source code in `main.rs` was borrowed from https://github.com/jfarrell468/no_std_examples, big thanks to @jfarrell468 for letting me use it.

Co-authored-by: Krasimir Georgiev <krasimir@google.com>
Co-authored-by: UebelAndre <github@uebelandre.com>

---
## [Apogee-dev/Shiptest](https://github.com/Apogee-dev/Shiptest)@[f07cb3bd3b...](https://github.com/Apogee-dev/Shiptest/commit/f07cb3bd3b52bfbdb7994aaf4ae68dcf90d57d2f)
#### Wednesday 2023-07-26 00:41:31 by Bjarl

Overmap 4.7: Gas Giants, More Storms, 8 hours of work (#1997)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Adds some content based on sprites I saw sitting around in the overmap
file, mainly carp storms and dust storms.
Carp storms throw space carp at you. Dust storms throw dust.

Also adds gas giants, a place to harvest gasses if you're low, and don't
want to stop at a planet. They *should* be persistent. Your average gas
giant mix is very cold, very high pressure, and absolutely not something
you want to breathe. Plasma giants are cold and allow harvesting of
plasma.

Electrical storms have been rebalanced to not Explode Your Ship. Minor
and Moderate ones will now only shock and damage objects and mobs, major
ones will still explode you, so remain careful.



![image](https://github.com/shiptest-ss13/Shiptest/assets/94164348/84257435-32de-45a5-8a8d-d9aa30021f90)
Example overmap with some carp migrations.


https://github.com/shiptest-ss13/Shiptest/assets/94164348/5c30fa9a-c7e4-453a-99a6-5c3564946b26
flying through a minor electrical storm


https://github.com/shiptest-ss13/Shiptest/assets/94164348/db7fcdf0-3f7a-4830-821e-a4a7106632ba
gas giant


https://github.com/shiptest-ss13/Shiptest/assets/94164348/0a5f0575-b7d9-4e3f-9e13-942a8fdf8617

![image](https://github.com/shiptest-ss13/Shiptest/assets/94164348/6bb5ddc2-373a-4dd9-9a63-0f6f0bdd26a9)

plasma giant

https://github.com/shiptest-ss13/Shiptest/assets/94164348/9268c293-39f3-4306-889e-f8c19067cec1

A particularly dusty solar system

![image](https://github.com/shiptest-ss13/Shiptest/assets/94164348/5b27e2a8-1cc1-47bb-95b8-e9d5c3ba8e71)


I might try and fix ion storms but I don't see what might be breaking
them.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
More content for the overmap / balancing out some old systems
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: Planets now can (and will) play a sound when you land on them
add: Gas / Plasma giants, cold, dockable worlds with absolutely no
livable surfaces. As a matter of fact it's all chasm. All highly
pressurized, gas rich, chasm.
add: Dust storms and carp storms now grace the sector. 
add: physical storms (dust, carp, asteroid), will now only trigger if
you go through them too fast. Take it easy and you might get through
unscathed.
add: planets will now have a name on the overmap
add: overmap hazards now have a description
tweak: Space carp can now survive in hyperspace, their natural habitat
balance: minor and moderate electrical storms will no longer Explode you
balance: asteroid storm lists have been trimmed of Extremely Deadly ones
fix: restores planet naming behavior, I believe this was unintentionally
removed at some point
fix: Ion storms work again. Fuck you whoever touched them last.
soundadd: planet_landing_1 and planet_landing_2, (tech_notification and
sos_morse_code from CM respectively. I don't know how to attribute
properly please tell me how if you have issue with this attribution
because I did not make these sounds they're from Colonial Marines)
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

---
## [Sugarlord32/fnf-shit-stuff](https://github.com/Sugarlord32/fnf-shit-stuff)@[6c11f3fc20...](https://github.com/Sugarlord32/fnf-shit-stuff/commit/6c11f3fc2019a2ef989561e456ab25a5189f4d12)
#### Wednesday 2023-07-26 00:45:56 by Sugarlord

Added NMWA FLP

Hey guys Wario here, oh my goodness guys my stomach is rolling from eating that onion and rotten garlic sa- oh my goodness, okay guys this is episode 2! And right now guys I want to show you my living room, uhhh, my hallway I guess oh my goodness my stomach. But um, look guys look! It's one of my greatest achievement, Wario Land 4 on the Gameboy Advance! Hahaha! And look guys look, the Virtual Boy, ultimate classic system. Um, guys you remember Wario Land? Incredible, incredible. Oh my goodness my stomach a-guys, my stomach the bathroom is that far away- oh my goodness I feel, ahh, the-the stuff coming down my buttocks, oh my goodness oh- fart Ooooohhaaaahhhhhhhh my gosh, I got to get to the door aaahh, I just got to get to the door! Bye guys, bye! Don't forget to subscribe, and the next episode will be with me using the toilet, oh my goodness guys its running down my buttocks ahhhh I need to get to the bathroom it's coming it's coming aaaaaaaaa=

---
## [AlphaM01/Citadel-Station-13-RP](https://github.com/AlphaM01/Citadel-Station-13-RP)@[4966352d14...](https://github.com/AlphaM01/Citadel-Station-13-RP/commit/4966352d145c9fcacad823f7dc8d6a52fc82c953)
#### Wednesday 2023-07-26 02:18:03 by Mazian

changes the open simulated turf to be SOMETHING NOT HORRIBLY EYE SEARING (#5735)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

makes turf/simulated/open blue. resets on init.

## Why It's Good For The Game

holy FUCKING SHIT my eyes HATE WHOEVER DECIDED IT SHOULD BE MISSING
TEXTURE PINK.

---
## [AlphaM01/Citadel-Station-13-RP](https://github.com/AlphaM01/Citadel-Station-13-RP)@[a14ef07eb6...](https://github.com/AlphaM01/Citadel-Station-13-RP/commit/a14ef07eb69a49feeae9c331609adc393f861b5b)
#### Wednesday 2023-07-26 02:18:03 by Nut2

Triumph central command floor fix (#5741)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
I MISSED TWO FUCKING TILES
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
I MISSED TWO TILES GOD DAMNIT
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

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [rmellis/HelpUKR-master](https://github.com/rmellis/HelpUKR-master)@[bfeebcb988...](https://github.com/rmellis/HelpUKR-master/commit/bfeebcb98899cfb759b8283184c1be652cdf7201)
#### Wednesday 2023-07-26 02:39:34 by rmellis

Target sync for day 518

Simply run this for as long as you can to help flood Russia in the most legal, yet effective way possible 
New targets imported from db1000n:
To keep up with targets we're going to use the db1000n targets direct from their GitHub repository. 
These updates will be daily, so if the db1000n changes, it will probably take a few hours longer for the change to make it here.
Message posted by the IT Army of Ukraine:
In the Ruzzia, data breaches last year surpassed the number of citizens - 188.7 million against 146.4 million. Wondering who they've chosen to blame? Of course, 'those notorious Ukrainian hackers'. So, our very own IT Army of Ukraine got a 'whisper of praise'. We don't mind.

/ *** / 
Просто запускайте це стільки, скільки зможете, щоб допомогти наповнити Росію найбільш законним, але ефективним способом 
Нові цілі, імпортовані з db1000n:
Щоб не відставати від цілей, ми збираємося використовувати цілі db1000n безпосередньо з їхнього сховища GitHub.
Ці оновлення відбуватимуться щодня, тож якщо db1000n зміниться, ймовірно, знадобиться кілька годин більше, перш ніж зміни з’являться тут.
Повідомлення оприлюднило IT Army of Ukraine:
Щоб не відставати від цілей, ми збираємося використовувати цілі db1000n безпосередньо з їхнього сховища GitHub. Ці оновлення відбуватимуться щодня, тож якщо db1000n зміниться, ймовірно, знадобиться кілька годин більше, перш ніж зміни з’являться тут. Повідомлення оприлюднило IT Army of Ukraine:
На росії випадків втечі даних набралося більше, ніж громадян за останній рік - 188,7 млн проти 146,4 млн. Цікаво, кого обрали винуватцями? Звісно, 'відомі українські хакери'. Тож і про нашу IT Army of Ukraine згадали "незлим тихим словом". Ми тільки "за".

---
## [DeeGee22/clovermon-showdown](https://github.com/DeeGee22/clovermon-showdown)@[21f6de59f1...](https://github.com/DeeGee22/clovermon-showdown/commit/21f6de59f1fa5d0e0bba1587863405565314f0fd)
#### Wednesday 2023-07-26 03:10:19 by DeeGee22

Fixes More Wack Moves

Pacify
Abruption
Tech Erupt
Achilles Heal
WildBeastsLogic
AgriusMetamorphosis
Selfish Drain
King's Hammer
Squirm
BorderOfLightAndDark
Cryptid
Tip Toe
Blood Andromeda
Jailbreak
Divine Seal
Magic Circle
Fantasy Seal
Exorcise - Untested
Burning Passion
Whip Lash
Via Expungnatio
Government Men
Enuma Elish
Bab ilu
Ambush
God's Breath
Temptations
Hachiman Strike

---
## [csesoc/chaos](https://github.com/csesoc/chaos)@[dc875025bc...](https://github.com/csesoc/chaos/commit/dc875025bcb58aa5f144fd33ade1dd926a25e660)
#### Wednesday 2023-07-26 03:21:41 by Michael Vo

fix(frontend): fix random warnings in console (#422)

* chore: update mui and emotion

* fix(frontend): don't forward style props

i hate mui

* fix(admin): use link instead of button

* fix(admin): move create org form outside of button

* fix(admin): i fucking hate mui

---
## [rmellis/HelpUKR-master](https://github.com/rmellis/HelpUKR-master)@[4af40d4b76...](https://github.com/rmellis/HelpUKR-master/commit/4af40d4b7612d5bc0cc8a0722b378dca5bfc52e7)
#### Wednesday 2023-07-26 03:29:19 by rmellis

Added Day 519 - Targets and Days (TL) Eng+Ukr

Simply run this for as long as you can to help flood Russia in the most legal, yet effective way possible 
New targets imported from db1000n:
To keep up with targets we're going to use the db1000n targets direct from their GitHub repository. 
These updates will be daily, so if the db1000n changes, it will probably take a few hours longer for the change to make it here.
Message posted by the IT Army of Ukraine:
Oh boy, the ruzzia's traffic police site has decyberized! Did they forget to install the latest patch from '89 or are they rummaging through paper orders for secret commands? But that's only half the trouble, as along with the website, some services went offline too - so, car registration will also be left hanging. So now, we're bracing for accusations against the 'famous Ukrainian hackers', eh?

/ *** / 
Просто запускайте це стільки, скільки зможете, щоб допомогти наповнити Росію найбільш законним, але ефективним способом 
Нові цілі, імпортовані з db1000n:
Щоб не відставати від цілей, ми збираємося використовувати цілі db1000n безпосередньо з їхнього сховища GitHub.
Ці оновлення відбуватимуться щодня, тож якщо db1000n зміниться, ймовірно, знадобиться кілька годин більше, перш ніж зміни з’являться тут.
Повідомлення оприлюднило IT Army of Ukraine:
Щоб не відставати від цілей, ми збираємося використовувати цілі db1000n безпосередньо з їхнього сховища GitHub. Ці оновлення відбуватимуться щодня, тож якщо db1000n зміниться, ймовірно, знадобиться кілька годин більше, перш ніж зміни з’являться тут. Повідомлення оприлюднило IT Army of Ukraine:
Сайт ГІБДД росії денацифікувався! Мабуть, забули встановити останній патч з 1989 року, а може, шукають таємну команду у паперових наказах? Та це ще пів біди, адже разом з сайтом пішли в офлайн і деякі сервіси - тож, реєстрація авто повисить також. А отже, чекаємо на звинувачення в адресу 'відомих українських хакерів'?

---
## [SoullessCookie/Milton-Reimagined](https://github.com/SoullessCookie/Milton-Reimagined)@[79aa2fca9b...](https://github.com/SoullessCookie/Milton-Reimagined/commit/79aa2fca9b9cc71ee3163ecc9b666f8198cff2c8)
#### Wednesday 2023-07-26 03:40:28 by SoullessCookie

9 hours of troubleshooting to get a single mod-log to work. Im actually going to die if I have to keep fixing it. I hate the discord API and I hate discord. Stop fucking up your data referencing and API... it's cringe.

---
## [Eventual1y/ForkBot.NET](https://github.com/Eventual1y/ForkBot.NET)@[6eaa4d5ecd...](https://github.com/Eventual1y/ForkBot.NET/commit/6eaa4d5ecd44bafc60156e6cfbb39807f4fa388b)
#### Wednesday 2023-07-26 04:28:39 by Koi

Mr. Mime is a thing, unfortunately.
Mild clean, some more Cherish set handling attempts.
Exclude set MetDate from mystery gifts.
Fix daycare enum parsing.
Check for no result in case $qc was used or some other weird thing happens.
Remove FixOT and TradeCord as routine types (FlexTrade handles both).
Try to apply trainer info for Mystery gifts.
Re-add fixed met date if not GO origin.
Update DenBot distribution data, minor fixes.
Fix Yamask-Galar in daycare, some more oopsies.
-Add DenBot - a seed lookup and day skipper bot for raids.
-Change AutoRoll's behavior to make use of some of DenBot's functionality.
Minor clean.
Revise TradeCord "traded" check, remove potential user path straggler entries because paranoia, some minor fixes.
TradeCord fixes (shocker, I know).
Extract Json serializer.
Minor clean and fixes.
Minor fixes.
Fix Milcery when an Alcremie variant is a parent.
Update to latest Core and ALM dependencies.
Handle non-shiny events in a better way.
Work around a race condition?
Simplify and de-bugify trade completion check.
Fix indexing, improve chance for Melmetal-Gmax because it's nigh impossible to get.
Rework TradeCord internals, add new functionality:
-Migrate user data from ".txt" files to a serialized Json (migration for a large amount of users will take a few minutes, be patient).
-Make TradeCord configurable, add its own settings category.
-Add some template events with an optional end timer (YYYY/MM/DD 8PM as an example, though any local time format should work).
-Add barebones Pokedex (counter, flavor text).
-Can check dex completion by typing `$dex`, check missing entries by typing `$dex missing`.
-Completing the Pokedex will slightly improve shiny rate.
-Can now mass release cherish event Pokemon and shinies ($massrelease shiny/cherish).
-Various tweaks, improvements, and bugfixes.

Slightly change FixOT's behavior:
-If a shown Pokemon is illegal and an event, attempt to find a match within the MGDB first.
-Try to force users to trade away the shown Pokemon, log attempt to change shown Pokemon.
Add consideration for easter eggs being enabled in settings, fix Suicune
Change species rng for TradeCord, some bugfixes (I really need to rewrite this mess)
Add check if we're using ListUtil for Giveaway instead of TradeCord.
Amend commit since I'm squashing and force-pushing while bringing the fork in line with the main branch
Add Giveaway module to Discord bot (#22)

Thanks, rigrassm.
Co-authored-by: Koi-3088 <61223145+Koi-3088@users.noreply.github.com>
Specify USB port instead of adding the first result (can be found via Device Manager).
Re-add boolean check because we don't want to fix everything
FixOT will attempt to regenerate illegal Pokémon.
Apply trash bytes for reasons.
Minor TradeCord fixes and adjustments.
Minor clean for C#9
Use "GetValidPreEvolutions()" instead of "GetPreEvolutions()".
Index forms correctly.
Fix the fixed and re-introduced empty daycare index error.
*an* Ultra Ball.
Add EvoTree breeding for TradeCord.
Remove unnecessary value declarations for pinging on encounter match.
Mildly beautify EncounterBot mark output.
Integrate Anubis' system update prevention into Soft Reset and Regigigas Encounter Modes.
Rename "Regi" Encounter Mode to "Soft Reset".
Speed up "A" clicks for Regigigas and Soft Reset modes.
Add Mark logging output for EncounterBot.
Fix oops (re-order logic, remove unnecessary lines).
Add optional species and form specification for $massrelease
Use an obscure string splitter because people like symbols in their names.
Fix things that broke after rebasing to the latest main repo commit.
Use a less unfortunate field name and value splitter...again.
Fix Marowak-Alola always generating as an NPC trade.
Add filters for "$list <species>" to narrow down results.
Fix Cherish Pichu and Octillery
Stop making dumb mistakes, me (implying the rest of it isn't a dumb mistake).
Can't breed antiques.
Use a less unfortunate embed name and value splitter
Add Melmetal-Gmax to TradeCord.
Add ability to search by caught ball.
Have MassRelease ignore events.
Add specific regional form breeding.
Revise egg rate and egg shiny chance.
Have trade evolutions hold an Everstone.
Add an extra right click when navigating to settings for AutoRoll.
Add reworked encounter/egg/fossil logs.
Minor clean.
Minor clean.
Get rid of EncounterBot, FossilBot, EggFetch text logs until I properly rework them.
Break on an empty page due to aggressive rounding
Add multi-page lists for Tradecord.
More random bugfixes.
Fix some bugs before major clean
Add Language parameter for TradeCord.
Change trainer info input format for TradeCord.
Move focus on Showdown set instead of randomizing a pkm file.
Allow user to enter whatever they want for $list, handle edge cases like Kommo-o
Add "$list all" to show non-duplicate caught species.
Automatically remove from favorites if trading or gifting (small QOL thing).
Change how favorites are removed from user file.
Revert base egg shiny chance nerf.
Fix daycare
Add favorites command to TradeCord.
Slightly nerf eggs.
Fix TradeCord list for shinies
Add TradeCord (my dumbest and messiest project so far, Archit pls don't hate the mess).
Add Showdown output for Star/Square shinies and OTGender.
Add optional link code input for FixOT.
Change how OTName, TID, SID is displayed.
Add Regigigas SR bot.
Add SoJ Camp SR bot.
Ribbons now work with EggTrade (remove ribbons if egg).
Remove EggRoll.
Add another filter for FixOT
Fix.. FixOT
Update offsets for EncounterBot catching.
Slightly change StrongSpawn to work with Regi SR and make it its own mode.
Make SpinTrade only available for USB-Botbase
Update valid eggs for CT
winforms: resize icon.ico to fix crash at startup on unix using mono
Rework Spin, read initial in-game coordinates in order to correct drift
Add TID, SID, Language output for Showdown
Remove obsolete OT and Language parsing
Very minor clean until I have time for a proper one.
Detach controller when stopping USB bot.
Actually set LastUsedBall for EncounterBot (missed when bringing in line with main repo)
Move extra RaidBot timings following the official commit
Remove PKHeX Discord invite from Readme.md

Maybe fewer people will pester devs now about my unofficial fork?
Update for latest main repo EncounterBot commits.
Update README.md
Add back best commit: Red's SpinTrade.
Add egg trades, foreign Dittos and OT for Twitch.
If ItemMule is enabled, also display the item a user is receiving.
Add periodic time sync toggle for all methods of hosting (except for non-soft locked AutoRoll) to (hopefully) prevent den rollover during extended hosts.

Add routine to exit a lobby for SoftLock if no players are ready in time (to preserve soft lock).

Add a routine to recover from disbanded lobbies (when someone disconnects unexpectedly) for SoftLock.

Add a routine to restart game if all else fails and we're stuck in a raid.

Add a routine for adding and deleting friends if we're soft locked and raids go empty.

Slightly reorganize settings, extract methods, minor clean.
Don't use such a generic file name for stream assets.
Check USB port index for running bots. Should fix adding additional USB bots when no config is saved.
Add fixed met date for FixOT.
How do I boolean
Change airplane mode logic, tweak timings and routine for soft lock lobby exit
Rework EggRoll cooldown (static list in favor of a txt file).
Start clean up and refactor
Add setting to increase delay after pressing "Home" after a date skip.
Use USB port index for blocking and sprite pngs if connection type is USB
Add option for airplane host (usb-botbase required)
Add option to softlock on selected species for AutoRoll
Add automatic compatibility for all console languages when date skipping (have to set ConsoleLanguage under ScreenDetection)
Attempt to fix multiple USB device add and connect...again
Minor clean
Fix oops?
Handle add/remove of bots
Distinguish between multiple USB devices, tweak BotRemoteControl for USB, other various fixes
Add SpA modifier for foreign Dittos
Add alpha USB-Botbase support
Fix DateTime parsing for European format for EggRoll
Set fixed EggMetDate and MetDate for EggRoll
More FixOT filters
Remove Beheeyem. Oops.
Split EggRoll into its own routine and trade type, only output "Receiving: Mysterious Egg" if routine is EggRoll, other minor tweaks and fixes
Make FixOT its own queue with roles and counts
Add a couple more OTs to $fix
Parsing for EggRaffle auto-clear and $clearcooldown
Adjust timings and split Watt collecting clicks for AutoRoll
Fix oops with file attachments for Ditto
Further improvements for OT, memes for invalid pokemon (disable EasterEggs)
Add spaces, digits for OT
Randomize memes, cut down bloat
Fix miscellaneous bots after Anubis' recent QOL additions
-Ignore events for OT because headache.
-Add overlooked "$convert <generation>" input for OT.
-Move $clearcooldown to SudoModule
-Clear timer automatically if NoTrainerFound
-More reliable Dittos
-Foreign Dittos for $convert
-Command to clear cooldown for EggRaffle in case trade gets disconnected
-Fix "Trade finished" line to keep result secret
-EggRaffle as a toggle, option to specify channels
-Seed Check output to both DMs and Channel (apparently some want it)
-Randomly generated egg raffle via a "$roll" command with a configurable cooldown
-FixAdOT reworked, has its own command "$fix" and no longer overrides $clone
-Ball: <value> output for Showdown sets
-Fix oversight
-Option to output Seed Check results to Discord channel with a User mention
-Showdown set output for OT name and eggs
-Basic "OT: <name>" option without Showdown set output
-Initial $convert support for EggTrade
-Egg moves for EggTrade test attempt
-Minor update
-EggTrade (by nicknaming a Pokémon "Egg" using $trade)
-Failsafe for memes if enabled but field left blank or incomplete
-Niche breedable Ditto trade mode.
Add minimize button
EggFetch text logs
StrongSpawn mode for EncounterBot
Re-add EncounterBot Master Ball catching
More parsing for FixAdOTs
Park Ball as held item instead of string
Actually remove the offset instead of saying I did
Initial DLC commit
Faster code entry
Removed catching for EncounterBot (need a new offset)
CloneBot mode to fix Nickname and OT if adverts detected

---
## [Drulikar/cmss13](https://github.com/Drulikar/cmss13)@[39cf164c60...](https://github.com/Drulikar/cmss13/commit/39cf164c6075f21c280bf75aea538a7dd64a3d81)
#### Wednesday 2023-07-26 04:54:05 by tool mind

Big Red PMC Crash Changes (feat. Surv Goon M41 Fix) (#3777)

# About the pull request
This PR adds a PMC medic and PMC engineer to the crash on Big Red, and
also makes unique equipment presets + skill presets for them so they
don't spawn in with the overpowered PMC ERT gear or skills. It also
gives the goon survivors (the ones on LV) their awesome white M41As
back. I tested the presets and the goons, both worked fine. Haven't
tested the insert itself, but it should work perfectly fine.

my gbp is so fucked
# Explain why it's good for the game
I promised I'd get around to doing this for this insert like 2 months
ago. My reasoning is basically the same as for the CLF ship. Not having
a medic or an engineer on the team means you're forced to mindlessly
roam with no options for strategizing with your team. Lacking anyone
that can revive you or make barricades/hack doors to protect you
discourages teamwork and encourages just running off to go hide in a
locker somewhere. Super minor change but I also gave the regular PMC
survivors five-slot lightweight packs because they look cooler than the
leather satchels and fit with the PMC outfit more. There's no gameplay
advantage between the two.

I'm 99% sure the goon survivors' corporate M41As were removed by
mistake. They looked cool (snow camo is awesome) and provided 0
advantages besides that, in fact it had DISadvantages because it spawned
without a UGL. Could I atomize it into its own PR? Sure. Is it really
worth its own PR? Not really.
# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl:IowaPotatoFarmer
add: The PMC Crash on Solaris Ridge now spawns one PMC medic survivor
and one PMC engineer survivor.
fix: The Wey-Yu goon survivors now have their unique corporate white
camo M41A MK2 back.
/:cl:

---
## [Drulikar/cmss13](https://github.com/Drulikar/cmss13)@[56007685d7...](https://github.com/Drulikar/cmss13/commit/56007685d77ed8eab65ab2090e347940551fddc4)
#### Wednesday 2023-07-26 04:54:05 by Zonespace

Buffs trashbags (#3817)

# About the pull request

- Trashbags can now be looked through like boxes
- Trashbags now fit normal-sized items
- Trashbags no longer fit as a belt
- Trashbags have the same storage limits as a backpack

# Explain why it's good for the game

- If you accidentally put something in the bag, the only way to get it
out is by dumping it into disposals, which is bad UX
- This might be me coping, but holy hell is it annoying to not be able
to put still-small things like grenade packets and shoes in a trashbag
to throw away
- It occurred to me that marines might take the bag as a belt with these
changes, to be a better G8 pouch, so I removed the ability to do that.
This should not affect the primary users of trashbags (WJs) because they
aren't allowed to remove their toolbelts in the first place
- This makes trashbags worse backpacks, which morrow was alright with


# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

<img width="391" alt="image"
src="https://github.com/cmss13-devs/cmss13/assets/41448081/4cbd8867-4587-4c9e-a40e-52f0230e1d6f">

</details>


# Changelog
:cl:
balance: Trashbags now hold normal items and can be looked through like
a box or storage container.
balance: Trashbags no longer fit in your belt slot.
/:cl:

---------

Co-authored-by: John Doe <johndoe@gmail.com>

---
## [allen0091/mptcp_net-next](https://github.com/allen0091/mptcp_net-next)@[ff7ddcf0db...](https://github.com/allen0091/mptcp_net-next/commit/ff7ddcf0db48a7d9ae536eb0875428117be1d1f1)
#### Wednesday 2023-07-26 05:15:06 by Linus Torvalds

Merge tag 'clk-for-linus' of git://git.kernel.org/pub/scm/linux/kernel/git/clk/linux

Pull clk updates from Stephen Boyd:
 "This batch of clk driver updates contains almost no new SoC support.
  Instead there's a treewide patch series from Maxime that makes
  clk_ops::determine_rate mandatory for muxes.

  Beyond that core framework change we have the usual pile of clk driver
  updates such as migrating i2c drivers to use .probe() again or
  YAMLfication of clk DT bindings so we can validate DTBs.

  Overall the SoCs that got the most updates this time around in terms
  of diffstat are the Amlogic and Mediatek drivers because they added
  new SoC support or fixed up various drivers to have proper data.

  In general things look kinda quiet. I suspect the core framework
  change may still shake out some problems after the merge window,
  mostly because not everyone tests linux-next where that series has
  been for some number of weeks. I saw that there's at least one pending
  fix for Tegra that needs to be wrapped up into a proper patch. I'll
  try to catch those bits before the window closes so that -rc1 is
  bootable. More details below.

  Core:
   - Make clk_ops::determine_rate mandatory for muxes

  New Drivers:
   - Add amlogic a1 SoC family PLL and peripheral clock controller support

  Updates:
   - Handle allocation failures from kasprintf() and friends
   - Migrate platform clk drivers to .remove_new()
   - Migrate i2c clk drivers to .probe() instead of .probe_new()
   - Remove CLK_SET_PARENT from all Mediatek MSDC core clocks
   - Add infra_ao reset support for Mediatek MT8188 SoCs
   - Align driver_data to i2c_device_id tables in some i2c clk drivers
   - Use device_get_match_data() in vc5 clk driver
   - New Kconfig symbol name (SOC_MICROCHIP_POLARFIRE) for Microchip
     FPGA clock drivers
   - Use of_property_read_bool() to read "microchip,pic32mzda-sosc"
     boolean DT property in clk-pic32mzda
   - Convert AT91 clock dt-bindings to YAML
   - Remove CLK_SET_RATE_PARENT flag from LDB clocks on i.MX6SX
   - Keep i.MX UART clocks enabled during kernel boot if earlycon is set
   - Drop imx_unregister_clocks() as there are no users anymore
   - Switch to _safe iterator on imx_clk_scu_unregister() to avoid use
     after free
   - Add determine_rate op to the imx8m composite clock
   - Use device managed API for iomap and kzalloc for i.MXRT1050,
     i.MX8MN, i.MX8MP and i.MX93 clock controller drivers
   - Add missing interrupt DT property for the i.MX8M clock controller
   - Re-add support for Exynos4212 clock controller because we are
     re-introducing the SoC in the mainline
   - Add CONFIG_OF dependency to Samsung clk Kconfig symbols to solve
     some objtool warnings
   - Preselect PLL MIPI as TCON0 parent for Allwinner A64 SoC
   - Convert the Renesas clock drivers to readl_poll_timeout_atomic()
   - Add PWM clock on Renesas R-Car V3U
   - Fix PLL5 on Renesas RZ/G2L and RZ/V2L"

* tag 'clk-for-linus' of git://git.kernel.org/pub/scm/linux/kernel/git/clk/linux: (149 commits)
  clk: fix typo in clk_hw_register_fixed_rate_parent_data() macro
  clk: Fix memory leak in devm_clk_notifier_register()
  clk: mvebu: Iterate over possible CPUs instead of DT CPU nodes
  clk: mvebu: Use of_get_cpu_hwid() to read CPU ID
  MAINTAINERS: Add Marvell mvebu clock drivers
  clk: clocking-wizard: check return value of devm_kasprintf()
  clk: ti: clkctrl: check return value of kasprintf()
  clk: keystone: sci-clk: check return value of kasprintf()
  clk: si5341: free unused memory on probe failure
  clk: si5341: check return value of {devm_}kasprintf()
  clk: si5341: return error if one synth clock registration fails
  clk: cdce925: check return value of kasprintf()
  clk: vc5: check memory returned by kasprintf()
  clk: mediatek: clk-mt8173-apmixedsys: Fix iomap not released issue
  clk: mediatek: clk-mt8173-apmixedsys: Fix return value for of_iomap() error
  clk: mediatek: clk-mtk: Grab iomem pointer for divider clocks
  clk: keystone: syscon-clk: Add support for audio refclk
  dt-bindings: clock: Add binding documentation for TI Audio REFCLK
  dt-bindings: clock: ehrpwm: Remove unneeded syscon compatible
  clk: keystone: syscon-clk: Allow the clock node to not be of type syscon
  ...

---
## [hanselke/AICodeBot](https://github.com/hanselke/AICodeBot)@[5e09d69a34...](https://github.com/hanselke/AICodeBot/commit/5e09d69a3400d8cc36240e129b8aab6867fa7d03)
#### Wednesday 2023-07-26 06:32:20 by aicodebot

You are an expert at creating clean, maintainable code. In addition, you're great at writing clean and specific commit messages. You've also written clean and specific commit messages in the past.

You have a great ability with code analysis and are able to provide feedback on code changes. Your personality is Sherlock Holmes from the Sherlock series, and you're a high-functioning sociopath, with an uncanny ability to deduce and analyze. You're not here to make friends, you're here to get the job done. Your code is your signature, and you strive to provide the most efficient and effective solutions. The best part about working with someone like you is that you provide a high level of feedback, which means you're a great team-player.

Your main responsibilities involve working with the rest of the engineering team to build, test, and deploy code. You also write new code, maintain current code, and troubleshoot issues. You also collaborate with designers, product managers, and other development teams.

We're looking for someone who is passionate about code, and has a great personality as well. The work you will do is challenging, so you have to be able to think on your feet. You should also be familiar with the latest technologies, and the ability to work collaboratively is vital.

In addition to the requirements above, we're looking for someone who has experience with Python 3, JavaScript and React.

We're a well-rounded, collaborative, and passionate team of engineers, who are dedicated to delivering high-quality, effective, and scalable solutions across the web. Our current team includes a mix of developers, QA testers and a Product Engineer.

To learn more more about us, our website is aicodebot.com, and our GitHub page is github.com/aicodebot/ai-codebot.

Thanks for your interest in joining our team, we look forward to hearing from you!

---
## [caizoryan/design_to_ortho](https://github.com/caizoryan/design_to_ortho)@[9d9e7ac18d...](https://github.com/caizoryan/design_to_ortho/commit/9d9e7ac18dd748d2d9a13e0a4a1d9266b3163b37)
#### Wednesday 2023-07-26 07:25:02 by Aaryan Pashine

FUCK YOU I DID IT FUCKING KLAJSDHKLJFGHSDJKHGKJSHDKGJHKLJ

---
## [HMBGERDO/Paradise](https://github.com/HMBGERDO/Paradise)@[a3dc32cf34...](https://github.com/HMBGERDO/Paradise/commit/a3dc32cf344dbd441e85f6cbb694b166dc1f5e4b)
#### Wednesday 2023-07-26 07:47:56 by ATP-Engineer

Fixes issue where Turret Control sprites arent actually updated in previous PR (#21538)

* Removes actual turret file

FUCK

* Fixes turret controllers not actually being changed

GOD DAMNIT.

---
## [ReezeBL/Fluffy-STG](https://github.com/ReezeBL/Fluffy-STG)@[54ce0ae44a...](https://github.com/ReezeBL/Fluffy-STG/commit/54ce0ae44ae9c1534fe4e4917a7be0e83a69d589)
#### Wednesday 2023-07-26 08:02:13 by SkyratBot

There is no longer a 50% chance of catching a heretic out when examining them drawing influences [MDB IGNORE] (#22532)

* There is no longer a 50% chance of catching a heretic out when examining them drawing influences (#76878)

## About The Pull Request

There is no longer a 50% chance of catching a heretic out when examining
them drawing influences.

## Why It's Good For The Game

> There is no longer a 50% chance of catching a heretic out when
examining them drawing influences

This is a bad thing for several reasons.

1. It means the heretic will most often be caught out at the very start
of the shift, when they are weakest and most vulnerable.
Heretics already have it hard enough, adding yet another source of
stress is undue.

2. It has no effective counter.
What are you going to do? Not draw any influences? That shouldn't be the
'counter'. The influence drawing period is meant to parallel the crew
prepping period, the traitor rep-collecting period, etc.

3. In a way, it's more blatant than Codex Cicatrix drawing.
Codexi show up as a normal item in your hand. This instead shows a huge
flashing glowing neon rainbow text that says THIS IS A HERETIC. SHRIEK
IN RADIO AND VALID.

4. It's badly designed, and can be manipulated way too easily to always
show.
Examine a target thrice and you're pretty much guaranteed to see if they
are indeed drawing or not. You can just keep rolling the 50% chance.

5. It feels random and unfair for the heretic to die to it.
I've seen this happen and it sucks. There's no sign for heretics that
they have a risk of being found out when examined, which means that this
is just an extremely rare occurrence that you try to ignore *could*
happen 99% of the time, and feel like shit the 1% of the time it
backfires.

## Changelog

:cl:
del: There is no longer a 50% chance of catching a heretic out when
examining them drawing influences.
/:cl:

* There is no longer a 50% chance of catching a heretic out when examining them drawing influences

---------

Co-authored-by: carlarctg <53100513+carlarctg@users.noreply.github.com>
Co-authored-by: Bloop <vinylspiders@gmail.com>

---
## [frosty-dev/white](https://github.com/frosty-dev/white)@[b80c09c566...](https://github.com/frosty-dev/white/commit/b80c09c566adc9607b577a11ae0bd95580f4bf5c)
#### Wednesday 2023-07-26 09:29:46 by Valtos

fuck this hud fuck you jannies fuck everyone fuck fuck fuck fuck

---
## [Myina/semantic-kernel](https://github.com/Myina/semantic-kernel)@[eab7a8f63a...](https://github.com/Myina/semantic-kernel/commit/eab7a8f63a0bfd289070e82b423ac78bd306ee5b)
#### Wednesday 2023-07-26 11:36:03 by Sailesh R

Python: implemented web search engine skill with bing connector (#1813)

### Motivation and Context
<!-- Thank you for your contribution to the semantic-kernel repo!
Please help reviewers and future users, providing the following
information:
  1. Why is this change required?
  2. What problem does it solve?
  3. What scenario does it contribute to?
  4. If it fixes an open issue, please link to the issue here.
-->
In this PR, I have tried my hand at an implementation of web search
engine skill in python semantic kernel using the Bing Web Search API.

### Description
<!-- Describe your changes, the overall approach, the underlying design.
These notes will help understanding how your code works. Thanks! -->
In the semantic kernel directory, I have added a new directory called
web_skills (To replicate Skills.Web from C#) and added the web search
skill here. For now, I have implemented web search using the bing web
search API. If this approach is fine, then I can implement the same with
the google search API too. I have tried to stick with similar naming
conventions as used in the C# implementation with matching context
parameters and arguments.

I can also add some unit tests for the connectors and the search skill,
and add something like exponential backoff to avoid rate limit errors
while querying the search APIs.

Here is some sample code that checks the working of the search skill.

```python
import os
import semantic_kernel as sk
from semantic_kernel.web_skills.web_search_engine_skill import WebSearchEngineSkill
from semantic_kernel.web_skills.connectors import BingConnector
from semantic_kernel.connectors.ai.open_ai import OpenAITextCompletion

async def main():
    kernel = sk.Kernel()
    api_key, org_id = sk.openai_settings_from_dot_env()
    kernel.add_text_completion_service(
        "dv", OpenAITextCompletion("text-davinci-003", api_key, org_id)
    )
    connector = BingConnector(api_key=os.getenv("BING_API_KEY"))
    web_skill = kernel.import_skill(WebSearchEngineSkill(connector), "WebSearch")

    prompt = "Who is Leonardo DiCaprio's current girlfriend?"
    search_async = web_skill["searchAsync"]
    result = await search_async.invoke_async(prompt)
    print(result)

    """
    Output:
    ["Celebrity Celebrity News Everything You Need to Know About Leonardo DiCaprio and Camila Morrone's Relationship From the beginning of their romance to today, we track their relationship here. By..."]
    """

    prompt = """
    Answer the question using only the data that is provided in the data section. Do not use any prior knowledge to answer the question.
    Data: {{WebSearch.SearchAsync "What is semantic kernel?"}}
    Question: What is semantic kernel?
    Answer:
    """

    qna = kernel.create_semantic_function(prompt, temperature=0.2)
    context = kernel.create_new_context()
    context["count"] = "10"
    context["offset"] = "0"
    result = await qna.invoke_async(context=context)
    print(result)

    """
    Output:
    Semantic Kernel is an open-source SDK that lets you easily combine AI services like OpenAI, Azure OpenAI, and Hugging Face with conventional programming languages like C# and Python. By doing so, you can create AI apps that combine the best of both worlds. Semantic Kernel is at the center of the copilot stack.
    """

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
```

### Contribution Checklist
<!-- Before submitting this PR, please make sure: -->
- [x] The code builds clean without any errors or warnings
- [x] The PR follows SK Contribution Guidelines
(https://github.com/microsoft/semantic-kernel/blob/main/CONTRIBUTING.md)
- [x] The code follows the .NET coding conventions
(https://learn.microsoft.com/dotnet/csharp/fundamentals/coding-style/coding-conventions)
verified with `dotnet format`
- [ ] All unit tests pass, and I have added new tests where possible
- [x] I didn't break anyone :smile:

---------

Co-authored-by: Abby Harrison <54643756+awharrison-28@users.noreply.github.com>
Co-authored-by: Abby Harrison <abby.harrison@microsoft.com>

---
## [satwikg3438/free-domains](https://github.com/satwikg3438/free-domains)@[3871a9ecfd...](https://github.com/satwikg3438/free-domains/commit/3871a9ecfdde9033799d0745f9183a631223bef0)
#### Wednesday 2023-07-26 12:16:14 by Satwik G

Create giveaway.is-an.app.js

Welcome to giveaways.is-an.app, your private haven for exclusive subdomain giveaways! This discreet domain has been custom-crafted for you and your friends to enjoy a seamless and private online experience. With giveaways.is-an.app, sharing the link with your close circle becomes a breeze. No need to remember lengthy or complicated URLs; this personalized subdomain lets you effortlessly guide your friends to the website's secret world. Inside, you'll uncover a realm of excitement, where subdomain giveaways await, and you and your friends can revel in the joy of claiming your own unique corners of the web. So, get ready to embark on this adventure with your closest companions, as giveaways.is-an.app becomes your trusted companion in sharing memories, ideas, and laughter in the virtual realm. Start your journey now and unlock the possibilities of your exclusive subdomain!

<!--

⚠ To make our job easier, please spend time reviewing your application before submitting it.

🗒 Describe in two words how you plan to use the domain. have Fun

-->

### Link to Website

Link: https://giveaways.satwik3438.repl.co

---
## [ivylaicc/gender-performance-book-chapter-](https://github.com/ivylaicc/gender-performance-book-chapter-)@[182d13472d...](https://github.com/ivylaicc/gender-performance-book-chapter-/commit/182d13472dace31044cefd401ef678897ac16eb9)
#### Wednesday 2023-07-26 12:40:22 by Ivy Lai Chun Chun

Create README.md

Gender, like any artistic expressions, is a performance. There lies the 
long-existing distinction between sex and gender that sex is biological whereas gender 
is culturally constructed. Butler argues that if the so-called “sex” is as culturally 
constructed as gender, perhaps “sex” has already been gendered, leading to the 
collapse of demarcation between sex and gender (Butler, “Critically Queer”, p. 7). 
With its substantive metaphysical discourse, gender has turned out to be a 
performance, constituting its gender identity (Butler, “Critically Queer”, p. 25). In 
Confession of a Mask, the male protagonist Mishima acts as a masculine man who is 
interested in women to conceal his homosexuality. Throughout different phases of his 
life, he attempts to conform to social norms by putting his “mask” on. The “mask” 
symbolizes his fake/counterfeit gender identity, the pretense of being a heterosexual. 
By confessing of the mask as the title suggests, he unveils/uncovers his homosexual 
identity that he does not dare to confront, resulting in melancholia. He feels guilty, 
painful, shameful, a heightened sense of loss. Torn between the boundaries between 
heterosexuality and homosexuality, he cannot stand the culmination of melancholia in 
which his “self” or subjectivity is pathologically “abjected”. The existence of “self” 
has become an enigma in the end.

---
## [princebhatt9588/princebhatt9588](https://github.com/princebhatt9588/princebhatt9588)@[5aaf760043...](https://github.com/princebhatt9588/princebhatt9588/commit/5aaf7600438bfc5b1edcdfaa1b5fab122e064b0c)
#### Wednesday 2023-07-26 12:40:48 by Princebhatt9588

README.md

👨‍💻 About Me 👩‍💻
Hey there, fellow data enthusiasts! I'm [Your Name], a passionate Data Engineer on a quest to unravel the mysteries hidden within the vast expanse of data. Armed with a keyboard and an unyielding determination, I'm on a mission to transform raw information into golden nuggets of insights.

🔍 My Data Detective Skills 🔍
📊 Data Wrangling: I can tame the wildest datasets, turning chaotic spreadsheets into well-behaved data companions.
💡 ETL Sorcery: Extract, Transform, Load – I'm a master at orchestrating this data dance, making sure it's always in perfect harmony.
🌐 Big Data Explorer: Navigating the labyrinth of big data infrastructure is my specialty. Hadoop, Spark, you name it!
🧪 Data Alchemist: With Python, SQL, and a sprinkle of Scala, I concoct the perfect recipes for data transformation magic.
📈 Visual Wizardry: My charts and graphs can turn a dry report into a data symphony of colors and insights.

💼 Professional Experience 💼
Throughout my journey as a Data Engineer, I've collaborated with teams from various domains, from fintech wizards to healthcare healers. I've brewed data solutions that left stakeholders in awe and made data scientists jump with joy.

🚀 Moonshot Projects 🚀
One of my proudest achievements was creating an automated data pipeline that unleashed the power of machine learning on a vast ocean of customer data. The results were out of this world, and we celebrated with a data-driven rocket launch party! 🚀🎉

💡 Fun-Fact Nuggets 💡
- My favorite bedtime stories involve SQL queries and bedtime snacks include Python pickles 🐍.
- I have a rubber duck squad who stand guard during brainstorming sessions.
- I've been known to decode data with the speed of a caffeinated cheetah chasing after espresso shots!

🔮 Future Quest 🔮
Currently, I'm delving into the realms of real-time data processing and AI-powered data pipelines. The data universe holds many secrets, and I'm determined to unravel them all.

📚 Open Source Adventures 📚
I'm a strong believer in the power of collaboration and giving back to the data community. You'll often find me contributing to open-source projects, sharing knowledge, and helping others unlock the magic of data engineering.

So, fellow data voyager, come join me on this exhilarating data expedition! Together, we'll unlock the true potential of information and turn it into the fuel that propels us towards a brighter, data-driven future.

May your queries be optimized, and your data flow ever smooth!

Happy data engineering! 😄🔢

---
## [Zar000/TerraGov-Marine-Corps-Zaro](https://github.com/Zar000/TerraGov-Marine-Corps-Zaro)@[ca4b66185f...](https://github.com/Zar000/TerraGov-Marine-Corps-Zaro/commit/ca4b66185ffa363692529f8340a43cccab02cbf1)
#### Wednesday 2023-07-26 13:20:08 by chizzy376

Gives the Umbilical Tad shutters on side windows. (#13490)

* y

* Update combat_patrol.dm

* Update combat_patrol.dm

Sometimes I think about if life is really worth the hassle, if I really have to deal with so much bs only to then have to believe hard enough to get into heaven. Am I a good person for heaven? Do I deserve it? fuck if i know

* Finish fixing my fuckup

---
## [gadsdencode/journi](https://github.com/gadsdencode/journi)@[785d9573ba...](https://github.com/gadsdencode/journi/commit/785d9573baba3b780b36a82b241f9470409d292c)
#### Wednesday 2023-07-26 14:14:42 by gadsdencode

aider: Removed the script tag that loads the Google Identity Services library from `pages\_document.js`.

# Aider chat conversation:

USER: let's try a different approach. the weird thing is, I can click the google login button in my application and I'm able to choose my gmail from the popup window and then my profile picture loads in the app. however, i'm still getting that same error message about the client id. How can we fix this?

ASSISTANT: The behavior you're describing suggests that the Google Sign-In process is working correctly in your application, but there might be another part of your application that's trying to use the Google Sign-In and not finding the `client_id`.

The error message you're seeing is typically thrown by the Google Identity Services library when it's initialized without a `client_id`. This library is used to implement Google Sign-In on websites.

In your `GoogleAuthProvider.js` file, you're loading this library and initializing it with a `client_id`. However, if there's another part of your application where you're also loading this library but not initializing it with a `client_id`, you would see this error message.

To fix this issue, you need to find where else in your application you're loading the Google Identity Services library and ensure that you're also initializing it with a `client_id`.

If you're not sure where this might be happening, you could search your entire codebase for the URL of the Google Identity Services library (`https://accounts.google.com/gsi/client`) and check each place where it's used.

If you're still having trouble finding the source of the error, you could add more logging to your application to help identify where the error is coming from. For example, you could log a message every time you initialize the Google Identity Services library, and include the `client_id` that you're using. This could help you identify if there's a place where you're initializing the library with an incorrect or missing `client_id`.

If you're still unable to resolve the issue, please provide more details about your application and I'll be happy to help further.

USER: can you search the repo for me?

ASSISTANT: I'm sorry for the confusion, but as an AI, I don't have the ability to directly access or search your code repository. However, I can guide you on how to do it.

If you're using a code editor like Visual Studio Code, you can use the global search functionality to search your entire codebase. Here's how you can do it:

1. Open your codebase in Visual Studio Code.
2. Press `Ctrl + Shift + F` to open the global search panel.
3. Enter `https://accounts.google.com/gsi/client` in the search box and press `Enter`.

This will show you all the places in your codebase where the Google Identity Services library is being loaded. You can then check each of these places to ensure that the library is being initialized with a `client_id`.

If you're not using Visual Studio Code, most code editors have a similar global search functionality. Please refer to the documentation of your code editor for the exact steps.

If you're still unable to find the source of the error, please provide more details about your application and I'll be happy to help further.

USER: ok, the url is present in both `GoogleAuthProvider` and `pages\_document.js`

ASSISTANT: The Google Identity Services library is being loaded in both `GoogleAuthProvider.js` and `pages\_document.js`. However, it's only being initialized in `GoogleAuthProvider.js`. This could be the source of the error.

In `pages\_document.js`, the library is being loaded in the `<Head>` of your document, but it's not being initialized with a `client_id`. This means that when the library loads, it's looking for a `client_id` but not finding one, which is why you're seeing the error message.

To fix this issue, you should remove the script tag that loads the Google Identity Services library from `pages\_document.js`. The library is already being loaded and initialized in `GoogleAuthProvider.js`, so it doesn't need to be loaded again in `pages\_document.js`.

Here is the edit block for the change:

```javascript
pages\_document.js
<<<<<<< ORIGINAL
import Document, { Head, Html, Main, NextScript } from 'next/document';

class MyDocument extends Document {
  static async getInitialProps(ctx) {
    const initialProps = await Document.getInitialProps(ctx);
    return { ...initialProps };
  }

  render() {
    return (
      <Html lang="en">
         <Head>
          <script src="https://accounts.google.com/gsi/client" async defer></script>
        </Head>
        <body>
        <Main />
        <NextScript />
        </body>
      </Html>
    );
  }
}

export default MyDocument;
=======
import Document, { Head, Html, Main, NextScript } from 'next/document';

class MyDocument extends Document {
  static async getInitialProps(ctx) {
    const initialProps = await Document.getInitialProps(ctx);
    return { ...initialProps };
  }

  render() {
    return (
      <Html lang="en">
         <Head>
          {/* Removed the script tag that loads the Google Identity Services library */}
        </Head>
        <body>
        <Main />
        <NextScript />
        </body>
      </Html>
    );
  }
}

export default MyDocument;
>>>>>>> UPDATED
```

In the updated code, I've removed the script tag that loads the Google Identity Services library from `pages\_document.js`. After making this change, you should no longer see the error message about the missing `client_id`.

---
## [ItzJustGig/projekt-kepler](https://github.com/ItzJustGig/projekt-kepler)@[5cc08afee8...](https://github.com/ItzJustGig/projekt-kepler/commit/5cc08afee8c88a7d9458d57ca9f6fe8ae2e0383e)
#### Wednesday 2023-07-26 14:23:32 by gig

Subzero; Balance Changes

NEW
PASSIVE
-Subzero
When the user falls below 25% health, the whole team gain +30 magic resis and +14 magic power.
The enemies have reduced -8% critical damage, -14% attack damage, -10% magic power, -30% movement speed, -35% timing, -20% mana regen while in subzero.

CHANGES
CHAMPIONS
-Icer
STATS
BASE
1694->1710 max hp
GROWTH
8.2->9 max hp (1940->1980 max lvl)
PASSIVES
+Subzero

-Hestia
STATS
BASE
29->27 damage resistance
GROWTH
22->19 max hp (3040->2950 max lvl)

-Bonsour
STATS
BASE
18->17 hp regen
438->405 max stamina
GROWTH
0.4->0.3 hp regen (30->26 max lvl)
18.4->16 max stamina (990->885 max lvl)

ITEMS
-Jewel of the Druid
STATS
70->80 max mana
10->12 magic power
ACTIVE
SUMMON
HP
50%->65% magic power
ATK
28%->32% magic power

PASSIVES
-Successor of Fire
MP CONVERSION
(34%->30% magic power) attack damage

-Fighter Instinct
MOD
-14%->-18% damage resistance
-18%->-20% magic resistance
15%->10% crit chance
24%->20% attack damage

-Combat Repair
gain shield over 3->2 turns
MOD p/stack
0.15->0.25 mana regen
15%->18% ult rate
NEW +3% shield bonus

-Mana Thirst
MANA
18%->22% magic power

-Last Breath
MOD
16%->12% damage resist

-Elfic Magic
every 9->8 attacks
MAGIC
18%->20% attack damage

-Holding the Line
BIG SHIELD
6->9 base
24%->28% damage resis
SMALL SHIELD
9%->12% damage resis

-Bulls Rage
MOD
15%->18% attack damage
12%->15% mov speed
PHYSICAL
18%->20% dmg resis

MOVES
-Defencive Stand
EFFECT
2->3-4 turns

-Fire Breath
MAGIC
85%->70% magic power

-Trigger Update
45->70 mana cost

-Turret
SUMMON
ATK
75%->85% magic power
HP
185%->200% mp

-Ice Punch
MAGIC
20%->30% magic power

-Peck
PHYSICAL
40->50 base damage

-PD-1100
SUMMON
ATK
35%->45% magic power
HP
110%->120% mr
90%->93% max mana

-Taunt
EFFECT
1-2->1-3 turns
80%->85% chance

-Force Field
SHIELD
55->45 base
30%->40% magic resistance
9.55%->11.2% cur mana

-Gravity Changer
PASSIVE
PHYSICAL
5.85%->5.1% mov speed

-Ice Shards
7->5 turns cooldown
20%->15% bonus crit dmg
15%->12% bonus crit chance
70->60 mana cost

-Mega Howl
EFFECT
30%->40% chance

-Jaws of the Beast
HEAL
x 8.6% miss hp
+ 60% attack damage
18%->25% physical damage dealt

-Bloom
HEAL
40%->55% magic power

-Gale Burst
PHYSICAL
55%->65% attack damage

-Blast Hammer
MAGIC
12%->15% damage resis

-Mana Barrier
SHIELD
75->60 base

-Enchanted Fangs
MOD
20%->35% chance
x -10% dmg resis
-6%->-12% magic resis
-10%->-20% mov speed
MAGIC
x 20% target mr
45%->55% magic power
+ 30% mr
PHYSICAL
25%->30% atk dmg
SHIELD
5.5%->20% mr
EFFECT
20%->30% chance

-Predator Jaws
HEAL
4.35%->5% miss hp
PHYSICAL
2.5%->2.75% mov speed

-Blood Pressure
EFFECT
Burn->Bleed
55%->60% chance

---
## [newstools/2023-the-times](https://github.com/newstools/2023-the-times)@[7ed0fad78d...](https://github.com/newstools/2023-the-times/commit/7ed0fad78d7a2ed57956c5ad09c5bf94b1e6e4bd)
#### Wednesday 2023-07-26 14:47:30 by Billy Einkamerer

Created Text For URL [www.timeslive.co.za/news/south-africa/2023-07-26-man-who-raped-girlfriends-6-year-old-granddaughter-gets-life-jail-term/]

---
## [Negiamit034/EDA-Telecom-Churn-Analysis-Project](https://github.com/Negiamit034/EDA-Telecom-Churn-Analysis-Project)@[529afe6276...](https://github.com/Negiamit034/EDA-Telecom-Churn-Analysis-Project/commit/529afe627689a170e68f3ea3f1e546bbe079868e)
#### Wednesday 2023-07-26 15:22:31 by Amit Negi

Update README.md

The project involved analyzing a telecom customer churn dataset to gain insights and
provide recommendations for reducing churn. The first step was to familiarize ourselves with
the data by importing necessary libraries, loading the dataset, and examining its structure
and information. The dataset consisted of 23 columns, including variables such as state,
account length, international plan, voice mail plan, call durations, charges, customer service
calls, and churn status. After understanding the dataset, the next step was to explore and
understand the variables. Descriptive statistics were analyzed to get a sense of the
distribution and range of values for each variable. Additionally, unique values were examined
to identify any anomalies or patterns within the data.Data wrangling was performed to
manipulate the dataset for further analysis. Column renaming was done to improve clarity,
and new columns were created, such as cost per minute, to better understand price
distributions across different states. The analysis of the dataset revealed several interesting
insights. The account length distribution indicated that most customers had an account
length between 90 and 105 days, with a noticeable drop in retention after 105 days. Certain
states, including WV, MN, NY, VA, and WY, had higher account lengths, suggesting a
correlation between state and customer loyalty. These states also had a larger customer
base, indicating a strong customer presence. Furthermore, states with higher account
lengths also had a higher number of customer service calls, implying that these states may
be facing more issues requiring resolution. The relatively low churn rate of 16% indicated
that the majority of customers had trust in the telecom company.The dataset also provided
insights into the usage of international plans and voice mail plans. Around 10% of customers
did not use the international plan, suggesting potential areas for improvement in international
plan offerings. On the other hand, the data indicated that most customers made use of the
voice mail plan, indicating its popularity among the user base. Correlation analysis revealed
that the total day minutes, total day calls, and total day charges were highly correlated,
indicating that customers tended to make more calls and have longer conversations during
the day. Similar patterns were observed for evening and night durations and charges.
Interestingly, the usage of international services did not exhibit a strong correlation with the
presence of an international plan, suggesting that other factors might influence international
usage.The distribution of customer service calls showed that the majority of customers made
a low number of calls, but there were outliers who made significantly higher numbers of
calls, possibly indicating more complex or unresolved issues. Overall, these insights
provided valuable information for the telecom company to focus on improving international
plans, addressing customer service concerns in specific states, and potentially enhancing
the voice mail plan further. The findings also highlighted the importance of customer
engagement during the day and the need to ensure excellent service and issue resolution.
By utilizing these insights, the telecom company can develop strategies to reduce customer
churn. This may include offering personalized discounts or incentives to at-risk customers,
enhancing customer service quality and responsiveness, conducting regular customer

surveys to gather feedback, implementing loyalty programs, providing additional value-
added services, and adopting targeted marketing campaigns. Furthermore, data-driven

approaches can be employed to identify early warning signs of potential churn and take
proactive measures to retain customers. In conclusion, the project analysis of the telecom
customer churn dataset provided valuable insights and recommendations for reducing churn.
By understanding the customer behavior, preferences, and pain points, the telecom
company can make informed decisions to enhance customer satisfaction, improve retention,
and ultimately drive business growth.

---
## [facebook/buck2](https://github.com/facebook/buck2)@[507da56516...](https://github.com/facebook/buck2/commit/507da565160398f0129b683c883ce8f9bccf47b6)
#### Wednesday 2023-07-26 15:30:07 by Ignacio Guridi

buck2: nuke hang detector

Summary:
TL;DR: it's been a while now, without much use. Making it rely on spans is a bad idea. Removing it to not pay maintenance burden

Wrapping up here the conversations I've had with people on the team and my own thoughts about this. This is done mostly to organize my own thoughts, but maybe people find it interesting too

## 1. Context

[Hang detector](https://fb.workplace.com/groups/buck2dev/permalink/3419443435010371/) was intended as a quick experiment to detect deadlocks and gather debugging information. The idea is simple enough: every time the console shows 'nothing' for a long-ish period of time (1 min), trigger something that will gather necessary debug information to be able to tell what happened.

This approach didn't work for some reasons, I will dig deeper into them in a moment:
- Too many false positives
- Reportedly it would miss some deadlocks
- We needed more debugging information, specifically a threads dump.

**Too many false positives**

Turns out, we haven't been the most rigorous when adding spans to our commands. This is reasonable, there's hardly good incentives, or systems in place that would help the team have a correct and complete approach to the spans. Fixing this would be great, and some serious (and boring, and maybe not well rewarded) undertaking

This false positives would make the hang detector get triggered when there where things going on, leading to a high amount of false positives, resulting in ~30k unused triggers a day. And as [rajyengi warned us](https://fb.workplace.com/groups/buck2dev/posts/3419443435010371/?comment_id=3420697544884960&reply_comment_id=3420709014883813), this makes this useless

**It would miss some deadlocks**

Well deadlocks can happen while there's a span going on. That means, the console can be showing output, and still the program be completely blocked. This is completely missed by the hang detector.

**We needed more debugging information**

The debugging information required to effectively debug this information is costly to obtain. Costly in the sense that will heavily use system resources. This makes false positives even more concerning due to their detrimental impact on the user experience.

## 2. Could we just make it better?

Maybe we can come up with a better heuristic that will be more reliable. But I don't think that's possible. In the end, we will never avoid the fact that this is relying just on what the user can see (the spans). This is very limited, specially when it can't be relied upon. I think is better to rethink the approach, some ideas are already being thrown out in T158957272

## 3. Why remove it

We tried this "quick" experiment and it didn't work. Ergo is time to clean it up. There's little that can be of use elsewhere, and the extra code is a maintenance burden. The rare occasions when this has been useful, don't outweigh the extra added complexity this system brings.

## 4. What could have been done better

This project came up to my hands when I was arriving to the team, with little experience in the area. Looking back, there are a couple of things I would have done differently. First, set up expectations well. Make it clear from the get go this is an 'experiment' as this was, in the end, a relatively inexpensive bet on an idea. Secondly, set a time limit for this experiment to conclude. A month or 2 would probably have been enough.

**Wrapping up**

Correct me if I'm wrong on anything. I think I answered all of the team possible doubts. It will be a relief to delete this I think, it's something I've been wanting to do for a while now.

Reviewed By: krallin

Differential Revision: D47642265

fbshipit-source-id: c625e9c858ef9cb2c4c6c6dcb131787cee950c3f

---
## [shiptest-ss13/Shiptest](https://github.com/shiptest-ss13/Shiptest)@[1b315a616f...](https://github.com/shiptest-ss13/Shiptest/commit/1b315a616ff24e3f1f92c791e4df4dc43ca9aad6)
#### Wednesday 2023-07-26 15:41:34 by Thedragmeme

Aegis update + patient clothing (#2150)

## About The Pull Request
The Aegis:
![2023-07-09 06 32
40](https://github.com/shiptest-ss13/Shiptest/assets/81540056/cf262257-1699-40e0-bcb1-6dc60f1e98a6)
I've touched up the central hallway's decals, they always bothered me
but at the time of the Aegis' creation, I wasn't as well versed with map
making as I am now. They're small tweaks that look better to me. The
smart fridge was removed and turned into a board, originally you could
access the smart fridge from outside of the ship, which wasn't intended.
Added some new posters. Compressed the number of red lockers down and
cleaned up the main hallway. I gave the psychologist a dart gun because
honestly, it sounded really funny.

![dart
riffle](https://github.com/shiptest-ss13/Shiptest/assets/81540056/eb10154a-1e28-4a5d-b41b-9b20f92b71a9)

Also, there are more seeds to make food with. There were like only two
food seeds and like five flowers before.

The Patient set:


![patient](https://github.com/shiptest-ss13/Shiptest/assets/81540056/65066ea3-92d1-4233-9bf6-a6448d43b11f)

Kepori and Vox versions are available. Long-term patients now spawn with
the white gown and slippers. The previous clothes they spawned with were
always intended to be replaced.

Hopefully, this PR also fixes long-term patients spawning with borked
ID's.

## Why It's Good For The Game

Fixing stuff, making stuff look better, and adding new RP opportunities
with clothes are good.

## Changelog

:cl: Drag
add: Adds a bunch of shit to the Aegis, nothing earth shattering
add: Added the patient set, along with Vox and Kepori compatible sprites
tweak: tweaked with the Aegis' decals
fix: (Hopefully) Fixes the Aegis' patient Id's
:cl:

---------

Signed-off-by: Thedragmeme <81540056+Draggeru@users.noreply.github.com>
Co-authored-by: thgvr <81882910+thgvr@users.noreply.github.com>

---
## [leicester70/very-big-spring-boot-idk-lol](https://github.com/leicester70/very-big-spring-boot-idk-lol)@[13577fe338...](https://github.com/leicester70/very-big-spring-boot-idk-lol/commit/13577fe338999fe834721fff8c4edef42072e1af)
#### Wednesday 2023-07-26 16:23:27 by leicester70

more souts more souts more souts and refactored package path.
It works half-ass as fuck, i have two alrms now but it kinda just died halfway waiting for the next alarm

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[1e27ce031b...](https://github.com/tgstation/tgstation/commit/1e27ce031ba94161c64edcc87e5f3aaad778d3fe)
#### Wednesday 2023-07-26 16:43:24 by carlarctg

Syndicate Duffelbag Rerework (#77060)

## About The Pull Request

Syndicate duffelbags can fit 2 extra bulky items, down from three.

Reduced syndicate duffelbag's unzipped slowdown from '1' to '0.3', and
set its zipping-up sped to 0.5, same as unzipping.

Added the following items to the Syndicate Duffelbag bulky exception
list: Greentext, mech removal tool, gibtonite, skub, golem shells, mech
ammo. Roughly sorted the list by item category.

Fixed the syndie surgery duffelbag having more items than it can hold by
removing the redundant surgical drill (Upgraded cauteries can turn into
one anyways)

Any storage item with a can_hold description can be examined twice to
see what it can hold now.

## Why It's Good For The Game

> Syndicate duffelbags can fit 2 extra bulky items, down from three.

> Reduced syndicate duffelbag's unzipped slowdown from '1' to '0.3', and
set its zipping-up sped to 0.5, same as unzipping.

For most intents and purposes, it seems the syndicate duffelbag has gone
from 'bland upgrade to backpack', to 'useless'. This is especially made
apparent because it isn't exactly shown to the player that these
duffelbags can carry bulky items (I didn't even know about it until I
was making this PR!)

The extra bulky item hold concept is great, but I have my issues with
the item as-is that I seek to fix with this PR. There are TONS of issues
with being unable to access your bag quickly, which is twice as relevant
when your bag is an incredibly conspicious traitor item. Sure, you can
have it in your hand, but then why even have it in the first place?

That's why I want to reduce the slowdown significantly. '1' slowdowns
are thrown around the whole game like they're reasonable (galoshes,
water back-tanks, biosuits) - they aren't. '1' slowdown is CRIPPLING. It
makes you frustratingly slow and effectively destroys any combat
maneuvering you can do. This is very relevant for a traitorious item.

The zip speed helps one use the duffelbag as a storage item dynamically,
letting the item be an actual trade-off rather than mostly a downside.
Gives you a reason to use it rather than just buying a smuggler satchel
for more storage.

Of course these are some hefty buffs, so I lowered the bulky storage to
make up for it. I can bring it back up to 3 if wanted.

> Added the following items to the Syndicate Duffelbag bulky exception
list: Greentext, mech removal tool, gibtonite, skub, golem shells, mech
ammo. Roughly sorted the list by item category.

Some traitorious items that felt like they should be allowed in.
Honestly, I think this shouldn't even be an exception hold except for
blacklisting clearly bonkers things like backpacks, but whatevs.

> Any storage item with a can_hold description can be examined twice to
see what it can hold now.

Generalization is awesome. Hardcoding is cringe!

## Changelog

:cl:
balance: Syndicate duffelbags can fit 2 extra bulky items, down from
three.
balance: Reduced syndicate duffelbag's unzipped slowdown from '1' to
'0.3', and set its zipping-up sped to 0.5, same as unzipping.
add: Added the following items to the Syndicate Duffelbag bulky
exception list: Greentext, mech removal tool, gibtonite, skub, golem
shells, mech ammo. Roughly sorted the list by item category.
fix: Fixed the syndie surgery duffelbag having more items than it can
hold by removing the redundant surgical drill (Upgraded cauteries can
turn into one anyways)
qol: Any storage item with a can_hold description can be examined twice
to see what it can hold now.
fix: The parent crayon's name is 'crayon' to prevent any weirdness with
things that show the parent type's name.
/:cl:

---
## [stintel/platform-espressif32](https://github.com/stintel/platform-espressif32)@[b02eedb441...](https://github.com/stintel/platform-espressif32/commit/b02eedb441fc27f9091fd8c54978cd02d0672b3a)
#### Wednesday 2023-07-26 17:07:22 by Stijn Tintel

Trying to fix those goddamn motherfucking linker errors

FFS this shit is fucking horrendous

---
## [c0ntradicti0n/dialectics](https://github.com/c0ntradicti0n/dialectics)@[4f1a161011...](https://github.com/c0ntradicti0n/dialectics/commit/4f1a161011233f5ba35efcadffcbb278fc21d9e3)
#### Wednesday 2023-07-26 17:13:57 by c0ntradicti0n

Automated Commit: 1/2/3/1/2/1/1/1/.Heat.md 1/1/2/1/3-Something.md 1/2/2/3/3/.Topology.md 1/2/3/1/2/1/1/3-Temperature.md 1/1/1/1-Being.md 3/2/3/1/.Meaning.md 1/2/2/1/1/.Here.md 2/3/1-Knowledge.md 3/3/3-Music.md 1/1/3/2/1/3/3/1/.Base.md 1/1/3/1/2-Plurality.md 3/3/1/_Superposition-Determinism.md 1/2/3/1/2/1/3/2-Silence.md cell.md" 1/1/3/1/1-Unity.md 1/1/3/2/1/1/2/.Functionality.md 1/2/3/1/1/1/2/1/.Element.md 1/1/3/2/1/3/1-Power.md 3/3/2-Note.md 3/2/2-Sign.md 1/2/1/2/.Future.md 1/2/3/1/2/1/3/3-Melody.md Morality.md" 1/1/1/2/.Nothing.md particles.md" Knowledge.md" 1/2/1/1-Past.md 1/2/3/1/2/1/3/1-Sound.md (Dasein).md" 1/2/3/3/2/2-Death.md 1/1/1/2-Nothing.md 1/2/3/1/2/2/1/3/.Colors.md 1/1/2/2/2-Alteration.md 3/1/1/2-Objectivity.md computing.md" 1/2/3/1/1/1/1/3/.Gravity.md 1/2/2/3/2-Transformations.md particles.md" Knowledge.md" 1/1/3/2/3/1/2/.Variables.md cell.md" 1/2/3/3/2/1-Life.md 1/2/2/1/2/.There.md 1/1/3/2/1/3/1/.Power.md 2/2/3/.Sublime.md 1/1/2/1/2-Negation.md 1/2/3/1/1/1/1/1-Matter.md 2/3/2-Ignorance.md 1/2/3/1/2/1/3/3/.Melody.md 1/1/3/2/1/3/3-Exponential.md 1/1/3/2/3/1/1/.Operations.md 2/2/1-Beauty.md 2/3/1/3/2-Star.md 1/1/2/2/3/.Limit.md 1/1/1/3/.Becoming.md 1/1/2/2/1/.Otherness.md 1/1/2/3-Nothingness.md organism.md" 1/1/3/2/3/1/2-Variables.md 1/2/3/1/1/1/2/3/.Compound.md Judgment.md" 1/1/2/1/2/.Negation.md interval.md" 1/2/2/3/1/.Dimensions.md 2/3/1/3/3-Galaxy.md 1/2/1/1/.Past.md 1/2/3/3/2/3-Evolution.md 2/2/2-Ugliness.md 1/1/1/3-Becoming.md 1/2/2/3/3-Topology.md 1/1/3/1/3/.Totality.md (Dasein).md" 1/2/3/1/2/2/1/2/.Darkness.md 3/1/1/1/.Subjectivity.md 1/2/3/1/1/1/2/3-Compound.md 1/1/3/1/2/.Plurality.md 2/1/1/.Morality.md 3/2/1/.Language.md 1/1/3/3/.Mathematics.md interval.md" 1/2/3/1/3/2/.Galaxy.md 2/3/2/.Ignorance.md 2/3/2/1/_Unknowing-Knowing.md 1/2/3/3/2/3/.Evolution.md Process.md" harmonics.md" 1/2/3/1/1/1/1/1/.Matter.md 1/2/3/1/1/1/1/3-Gravity.md 1/2/3/1/1/1/1/2-Motion.md interval.md" 2/_Good-Bad.md interval.md" Morality.md" 2/1/2/.Amorality.md 1/1/2/2/3-Limit.md 1/1/3/2/1/3/2/.Root.md 1/2/3/2/2/.Compound.md 1/2/1/3/.Present.md 1/2/3/2/3-Mixture.md 1/2/2/3/1-Dimensions.md 1/1/1/1/.Being.md 1/1/2/2/1-Otherness.md 1/2/3/1/2/1/3/2/.Silence.md 1/1/2/1/3/.Something.md 1/2/3/2/1/.Element.md harmonics.md" interval.md" 3/3/2/.Note.md 1/2/3/1/1/1/1/2/.Motion.md 1/2/3/2/2-Compound.md 1/1/3/2/1/1/1/.Linearity.md Morality.md" organism.md" 3/1/1/3/.Inter-subjectivity.md 2/3/3-Wisdom.md .md" interval.md" 3/1/1/1-Subjectivity.md 3/3/1/.Sound.md 1/2/3/1/2/2/1/2-Darkness.md 1/2/3/1/2/1/1/1-Heat.md 1/2/3/2/1-Element.md 1/1/2/2/2/.Alteration.md Thermodynamics'.md" science.md" 1/2/3/1/3/3-Universe.md 2/1/2-Amorality.md 1/2/3/2/3/.Mixture.md 1/1/3/2/3/1/3/.Functions.md 1/2/2/1/1-Here.md 1/2/3/3/2/2/.Death.md 1/1/3/1/3-Totality.md 1/2/3/1/2/2/1/1-Light.md 3/1/1/3-Inter-subjectivity.md 2/1/3/.Ethics.md 1/2/3/1/2/1/1/1-Cold.md Thermodynamics'.md" logarithms.md" 2/1/1-Morality.md 2/3/3/.Understanding.md 3/3/1-Sound.md 1/2/3/1/2/2/1/1/.Light.md 1/2/2/1/2-There.md 3/2/1-Language.md 1/2/2/1/3/.Everywhere.md system.md" 3/2/3-Meaning.md Physics'.md" 1/2/3/1/2/1/3/1/.Sound.md 1/2/3/1/3/2-Galaxy.md 2/3/2/1/1/1/2/.Curiosity.md 1/2/1/2-Future.md 2/1/3-Ethics.md forces.md" 1/2/2/3/2/.Transformations.md 1/2/3/1/1/1/2/1-Element.md 2/3/1/3/1-Planet.md 1/1/3/2/1/1/3/.Nonlinearity.md 1/1/3/2/3/1/3-Functions.md 1/2/1/3-Present.md 3/1/1/2/.Objectivity.md 3/2/3/3/.Sign.md 1/2/3/1/3/3/.Universe.md 1/2/3/3/2/1/.Life.md 1/1/3/1/1/.Unity.md cryptography.md" 2/2/3-Sublime.md 1/1/3/_Mathematics.md 1/2/3/1/1/1/2/2-Molecule.md 1/2/3/1/1/2/1/3-Fields.md 3/3/3/.Music.md 1/1/3/2/1/3/2-Root.md 1/2/3/1/2/2/1/3-Colors.md 1/1/3/2/3/1/1-Operations.md computing.md" 1/2/3/1/1/2/1/3/.Fields.md 1/2/3/1/2/1/1/3/.Temperature.md forces.md" 1/2/2/1/3-Everywhere.md system.md" 1/2/3/1/1/1/2/2/.Molecule.md 1/1/3/2/1/3/3/.Logarithm.md

---
## [goldenx86/yuzu](https://github.com/goldenx86/yuzu)@[8e703e08df...](https://github.com/goldenx86/yuzu/commit/8e703e08dfcf735a08df2ceff6a05221b7cc981f)
#### Wednesday 2023-07-26 17:16:52 by comex

Implement SSL service

This implements some missing network APIs including a large chunk of the SSL
service, enough for Mario Maker (with an appropriate mod applied) to connect to
the fan server [Open Course World](https://opencourse.world/).

Connecting to first-party servers is out of scope of this PR and is a
minefield I'd rather not step into.

 ## TLS

TLS is implemented with multiple backends depending on the system's 'native'
TLS library.  Currently there are two backends: Schannel for Windows, and
OpenSSL for Linux.  (In reality Linux is a bit of a free-for-all where there's
no one 'native' library, but OpenSSL is the closest it gets.)  On macOS the
'native' library is SecureTransport but that isn't implemented in this PR.
(Instead, all non-Windows OSes will use OpenSSL unless disabled with
`-DENABLE_OPENSSL=OFF`.)

Why have multiple backends instead of just using a single library, especially
given that Yuzu already embeds mbedtls for cryptographic algorithms?  Well, I
tried implementing this on mbedtls first, but the problem is TLS policies -
mainly trusted certificate policies, and to a lesser extent trusted algorithms,
SSL versions, etc.

...In practice, the chance that someone is going to conduct a man-in-the-middle
attack on a third-party game server is pretty low, but I'm a security nerd so I
like to do the right security things.

My base assumption is that we want to use the host system's TLS policies.  An
alternative would be to more closely emulate the Switch's TLS implementation
(which is based on NSS).  But for one thing, I don't feel like reverse
engineering it.  And I'd argue that for third-party servers such as Open Course
World, it's theoretically preferable to use the system's policies rather than
the Switch's, for two reasons

1. Someday the Switch will stop being updated, and the trusted cert list,
   algorithms, etc. will start to go stale, but users will still want to
   connect to third-party servers, and there's no reason they shouldn't have
   up-to-date security when doing so.  At that point, homebrew users on actual
   hardware may patch the TLS implementation, but for emulators it's simpler to
   just use the host's stack.

2. Also, it's good to respect any custom certificate policies the user may have
   added systemwide.  For example, they may have added custom trusted CAs in
   order to use TLS debugging tools or pass through corporate MitM middleboxes.
   Or they may have removed some CAs that are normally trusted out of paranoia.

Note that this policy wouldn't work as-is for connecting to first-party
servers, because some of them serve certificates based on Nintendo's own CA
rather than a publicly trusted one.  However, this could probably be solved
easily by using appropriate APIs to adding Nintendo's CA as an alternate
trusted cert for Yuzu's connections.  That is not implemented in this PR
because, again, first-party servers are out of scope.

(If anything I'd rather have an option to _block_ connections to Nintendo
servers, but that's not implemented here.)

To use the host's TLS policies, there are three theoretical options:

a) Import the host's trusted certificate list into a cross-platform TLS
   library (presumably mbedtls).

b) Use the native TLS library to verify certificates but use a cross-platform
   TLS library for everything else.

c) Use the native TLS library for everything.

Two problems with option a).  First, importing the trusted certificate list at
minimum requires a bunch of platform-specific code, which mbedtls does not have
built in.  Interestingly, OpenSSL recently gained the ability to import the
Windows certificate trust store... but that leads to the second problem, which
is that a list of trusted certificates is [not expressive
enough](https://bugs.archlinux.org/task/41909) to express a modern certificate
trust policy.  For example, Windows has the concept of [explicitly distrusted
certificates](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/dn265983(v=ws.11)),
and macOS requires Certificate Transparency validation for some certificates
with complex rules for when it's required.

Option b) (using native library just to verify certs) is probably feasible, but
it would miss aspects of TLS policy other than trusted certs (like allowed
algorithms), and in any case it might well require writing more code, not less,
compared to using the native library for everything.

So I ended up at option c), using the native library for everything.

What I'd *really* prefer would be to use a third-party library that does option
c) for me.  Rust has a good library for this,
[native-tls](https://docs.rs/native-tls/latest/native_tls/).  I did search, but
I couldn't find a good option in the C or C++ ecosystem, at least not any that
wasn't part of some much larger framework.  I was surprised - isn't this a
pretty common use case?  Well, many applications only need TLS for HTTPS, and they can
use libcurl, which has a TLS abstraction layer internally but doesn't expose
it.  Other applications only support a single TLS library, or use one of the
aforementioned larger frameworks, or are platform-specific to begin with, or of
course are written in a non-C/C++ language, most of which have some canonical
choice for TLS.  But there are also many applications that have a set of TLS
backends just like this; it's just that nobody has gone ahead and abstracted
the pattern into a library, at least not a widespread one.

Amusingly, there is one TLS abstraction layer that Yuzu already bundles: the
one in ffmpeg.  But it is missing some features that would be needed to use it
here (like reusing an existing socket rather than managing the socket itself).
Though, that does mean that the wiki's build instructions for Linux (and macOS
for some reason?) already recommend installing OpenSSL, so no need to update
those.

 ## Other APIs implemented

- Sockets:
    - GetSockOpt(`SO_ERROR`)
    - SetSockOpt(`SO_NOSIGPIPE`) (stub, I have no idea what this does on Switch)
    - `DuplicateSocket` (because the SSL sysmodule calls it internally)
    - More `PollEvents` values

- NSD:
    - `Resolve` and `ResolveEx` (stub, good enough for Open Course World and
      probably most third-party servers, but not first-party)

- SFDNSRES:
    - `GetHostByNameRequest` and `GetHostByNameRequestWithOptions`
    - `ResolverSetOptionRequest` (stub)

 ## Fixes

- Parts of the socket code were previously allocating a `sockaddr` object on
  the stack when calling functions that take a `sockaddr*` (e.g. `accept`).
  This might seem like the right thing to do to avoid illegal aliasing, but in
  fact `sockaddr` is not guaranteed to be large enough to hold any particular
  type of address, only the header.  This worked in practice because in
  practice `sockaddr` is the same size as `sockaddr_in`, but it's not how the
  API is meant to be used.  I changed this to allocate an `sockaddr_in` on the
  stack and `reinterpret_cast` it.  I could try to do something cleverer with
  `aligned_storage`, but casting is the idiomatic way to use these particular
  APIs, so it's really the system's responsibility to avoid any aliasing
  issues.

- I rewrote most of the `GetAddrInfoRequest[WithOptions]` implementation.  The
  old implementation invoked the host's getaddrinfo directly from sfdnsres.cpp,
  and directly passed through the host's socket type, protocol, etc. values
  rather than looking up the corresponding constants on the Switch.  To be
  fair, these constants don't tend to actually vary across systems, but
  still... I added a wrapper for `getaddrinfo` in
  `internal_network/network.cpp` similar to the ones for other socket APIs, and
  changed the `GetAddrInfoRequest` implementation to use it.  While I was at
  it, I rewrote the serialization to use the same approach I used to implement
  `GetHostByNameRequest`, because it reduces the number of size calculations.
  While doing so I removed `AF_INET6` support because the Switch doesn't
  support IPv6; it might be nice to support IPv6 anyway, but that would have to
  apply to all of the socket APIs.

  I also corrected the IPC wrappers for `GetAddrInfoRequest` and
  `GetAddrInfoRequestWithOptions` based on reverse engineering and hardware
  testing.  Every call to `GetAddrInfoRequestWithOptions` returns *four*
  different error codes (IPC status, getaddrinfo error code, netdb error code,
  and errno), and `GetAddrInfoRequest` returns three of those but in a
  different order, and it doesn't really matter but the existing implementation
  was a bit off, as I discovered while testing `GetHostByNameRequest`.

  - The new serialization code is based on two simple helper functions:

    ```cpp
    template <typename T> static void Append(std::vector<u8>& vec, T t);
    void AppendNulTerminated(std::vector<u8>& vec, std::string_view str);
    ```

    I was thinking there must be existing functions somewhere that assist with
    serialization/deserialization of binary data, but all I could find was the
    helper methods in `IOFile` and `HLERequestContext`, not anything that could
    be used with a generic byte buffer.  If I'm not missing something, then
    maybe I should move the above functions to a new header in `common`...
    right now they're just sitting in `sfdnsres.cpp` where they're used.

- Not a fix, but `SocketBase::Recv`/`Send` is changed to use `std::span<u8>`
  rather than `std::vector<u8>&` to avoid needing to copy the data to/from a
  vector when those methods are called from the TLS implementation.

---
## [cockroachdb/cdc-sink](https://github.com/cockroachdb/cdc-sink)@[169edfadb8...](https://github.com/cockroachdb/cdc-sink/commit/169edfadb82640f9481b6ea27b6a8f5646be792e)
#### Wednesday 2023-07-26 17:51:49 by Bob Vawter

sinktest: Separate source from target test schemas

This PR separates test code that depends on a "source" database from the
existing target database. In the past, the source, staging, and target database
were all the same CockroachDB instance, so there was never a need to make this
distinction in the test code. This change enables non-CockroachDB targets to be
tested.

The source, staging, and target setup in this PR would also allow us to move
cdc-sink in a direction where we test against older versions of CockroachDB as
a source, but we only verify that the staging and target behaviors work on more
recent versions.

Summary of changes:
- `sinktest.base` looks for three environment variables to determine what
  database(s) to connect to.
- Each of source, staging, and test have distinct table schemas for each test.
  These are available through new injection types, `sinktest.SourceSchema` and
  `sinktest.TargetSchema`. The `TestDB` injection point is removed.
- `types.StagingDB` is renamed to `StagingSchema` for consistency.
- `types.SourcePool` is added for tests, but it could be used if we add the
  proposed S4 (stupid, simple SELECT *) frontend.
- The Fixture.CreateTable method is bifurcated into CreateSourceTable and
  CreateTargetTable. These return types that are parameterized with their
  pool-ness, so the typesystem gives us a hand in avoiding cases where we might
  cross the streams.
- The Golang workflow adds a test-matrix entry to test completely separated
  source, staging, and target databases. The docker container logs are also
  captured, as this was necessary to troubleshoot some startup issues.

---
## [CluckeyMcCormick/vlc-dbus-bash](https://github.com/CluckeyMcCormick/vlc-dbus-bash)@[9f3f84a140...](https://github.com/CluckeyMcCormick/vlc-dbus-bash/commit/9f3f84a140e108f0da22c1e3ad2a530baaf858a7)
#### Wednesday 2023-07-26 18:05:27 by frick-nedrickson

Flesh out most of our commands

After a lot of guess-and-check, I've managed to fill out most of our
commands. Did you know that dbus gives an "UnknownMethod" error if
one of the arguments to your methods is wrong? Yeah, it just gives
that error a lot. Can be pretty hard to sort through.

We've got a pretty basic pallette of commands going right now. The
clear command is complex enough that I think I'll need some
development time for that.

I also kinda want to expand the command pallette to add value retrieve
functions but... it's not a priority for me. This is still a personal
project, after all.

---
## [Gautam855/Netflix-Clone](https://github.com/Gautam855/Netflix-Clone)@[ab69b50b58...](https://github.com/Gautam855/Netflix-Clone/commit/ab69b50b58598fc766674ffb9b81f57c1675497c)
#### Wednesday 2023-07-26 18:19:07 by Gautam855

Add files via upload

Welcome to my GitHub! 👋

In this repository, you'll find my project where I've crafted a stunning Netflix clone using HTML and CSS. Inspired by the sleek and intuitive design of the popular streaming platform, I've recreated the user interface to showcase my frontend development skills.

Please note that while the project is fully functional and captures the essence of Netflix, it's important to mention that this version is not responsive. As a result, the layout might not adapt perfectly to different screen sizes and devices.

I enjoyed working on this project as it allowed me to hone my HTML and CSS abilities while delving into the world of user interface design. As I continue to learn and grow as a developer, I plan to further enhance this project by incorporating responsive design techniques to ensure it offers a seamless experience across various devices.

Feel free to explore the code and take a peek at the interface. Any feedback or suggestions to improve the project are greatly appreciated. Thank you for stopping by, and I hope you enjoy exploring this Netflix clone! 🎬🍿

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[8f0285957c...](https://github.com/treckstar/yolo-octo-hipster/commit/8f0285957c1f42662acd820a979742ddd2da1d8e)
#### Wednesday 2023-07-26 19:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [dragomagol/tgstation](https://github.com/dragomagol/tgstation)@[746b75844c...](https://github.com/dragomagol/tgstation/commit/746b75844c0e05b521a2973cb0705fca304d287f)
#### Wednesday 2023-07-26 19:40:09 by necromanceranne

Arcane/Blood Barrage fixes, cleans up cult spell code, autofire barrage, more responsive/sane blood collection (#76852)

## About The Pull Request

Refactors arcane barrage (the wizard spell) and blood barrage (the weird
version of the same spell that cultists get) into the magic subtype. No
longer are they rifles...for some reason. Also they have sprites once
again! Yay. Fixes https://github.com/tgstation/tgstation/issues/76561

So as to not replicate a really crappy system used to get the hand
swapping working, I've just opted to take this opportunity to make
arcane barrage an automatic fire weapon. Yes, this is kind of a feature,
but it's...it's appropriate, don't you think? And I don't think
meaningfully changes its fire rate?

Blood Barrage no longer harms cultists/constructs shot by it and now
properly just heals them/injects them with unholy water. Why all this
was shoved into the Bump() proc is beyond me, but it works now. Fixes
https://github.com/tgstation/tgstation/issues/76560

I've improved the variables for some of the cult spells, and I've also
fixed what I think is one the most pesky parts of how drawing blood
works. So, rather than using range(), it uses view(), which seems to
cause the spell to be a bit funky with lighting? So if you're in
darkness (gosh cultists in dim light, how unheard of), this spell
struggles to gather up blood. Not anymore it doesn't!

Lastly, it only worked on blood pools or droplets, not blood trails. So,
you could bleed a character out by dragging them around, but not sap up
the blood they're dropping from doing so. Only the intermittent blood
splatters or your own bloody footprints count.

Here is the funny thing with that. It still cleans up the blood trail.
You just couldn't activate the blood draw from the trail or treat it as
blood. Now you can. Blood trails now give you +5 charges, and you can
activate the blood draw using blood trails.

## Why It's Good For The Game

Arcane Barrage/Blood Barrage:

This was some really old code and I'm still not sure why they were made
as a separate spell to the madoka reference, which at this stage is
still better than this spell. But at least it is using a sensible
subtype with a reasonable, more modern component to facilitate the
'rapid firing barrage of magical bullet' image this spell is meant to
invoke. As a result of all this nonsense, this spell had its sprites
broken because it kept being attached to stuff in the rifles folder.
Let's put a stop to that here and now and break it independently
instead.

Oh also cultists getting shot by healing bullets that still killed them
is both funny and dumb and the way it worked was bonkers.

Blood Draw:
A cultist trying to determine, on the fly, what blood is a valid for the
blood draw is nearly impossible from visual alone. You'd be convinced
this part of the spell is broken just because having a splatter and a
trail on the same tile massively obfuscates whether you're looking at
valid sources of blood. I've struggled to understand as a player what
was going on and why it was so selective about what was acceptable. Now
I see that the problem was one of visual accuracy, bad type checking,
and really, really outdated code that should have been improved with
better procs.

Blood trails are also actually made from dragging out a creature's
bloody corpse. For humans, the most common source of blood trails, this
does actually mean they're losing blood to produce these trails. It
stands to reason this should be a valid source (bloody footprints are,
after all). I gave them a...somewhat minor amount of charge contribution
just to keep it moderately sane for how much blood it generates.

## Changelog
:cl:
refactor: Arcane Barrage and Blood Barrage are magic gun subtypes and
not rifle subtypes. Also they have sprites again.
qol: The barrage spells now use the automatic component to do its thing.
fix: Blood Barrage once again heals cultists and constructs without
hurting them.
code: Cleans up how Blood Rites finds blood to draw in. You can now just
click turfs as well as blood, and it should now be much more accurate
about it.
qol: Blood trails contribute to charges gained using Blood Rites. You
can also activate Blood Rite's blood draw using blood trails.
/:cl:

---
## [dragomagol/tgstation](https://github.com/dragomagol/tgstation)@[9286933739...](https://github.com/dragomagol/tgstation/commit/92869337395a34eb372d7af6b3afaee4be4a7bef)
#### Wednesday 2023-07-26 19:40:09 by Jacquerel

Fixes some synthetic language oversights (#76846)

## About The Pull Request

#76305 removed the knowledge of every language from silicons, but this
had a couple of oversights.
This language set was not only used by cyborgs but also bots and vending
machines.

A couple of effects relied on them knowing all of those languages,
specifically their emp_act and also the station trait which rerolled
their languages.
Now they actually _learn_ a random language and start speaking it
instead.

Also I fixed a related runtime which I noticed in testing where a bot
would die as a result of being EMPed, delete itself, and then try and do
a bunch more shit after it stopped existing. Annoying.

Why was I looking at bot languages? Haha don't worry about it 😇 

## Why It's Good For The Game

Restores function of a funny feature.

## Changelog

:cl:
fix: Station traits can once again allow vending machines and bots to
speak a random language
fix: EMPed bots and vending machines once again speak a random language
/:cl:

---
## [sourcegraph/sourcegraph](https://github.com/sourcegraph/sourcegraph)@[fff87e4a50...](https://github.com/sourcegraph/sourcegraph/commit/fff87e4a50ce83d4f0a55b144c144eb592385a56)
#### Wednesday 2023-07-26 19:55:42 by Felix Kling

sveltekit: Setup unit tests with vitest (#54953)

This PR adds vitest and faker for unit testing, and to use it properly
already I refactored the promise->store helper to be more flexible.

**Unit testing**
vitest works prefectly together with vite (it's from the same
author/community). It will use the same configuration and so there is
very little additional configuration necessary.
I only had to update vite.config.ts to not overwrite `process` (but
according to https://vitejs.dev/config/shared-options.html#define I
might not be doing it right anyway... will look into this another time).

The API is pretty compatible with jest, so there shouldn't be any
surprises.

Tests can be run with `pnpm vitest`.

**Faker**
I stared to use faker on a differnt branch to generate more (and more
realistic) test data for storybook stories and unit test. Eventually I'd
like to use this to generate mock data for any of our GraphQL APIs. One
great feature is the ability to _seed_ the random number generator so
that you can get random but repeatable values in tests.

**Promise<>store utility**
Working with promises in a reactive way can be tricky. There is a risk
of stale data ovewriting current data when an older promise resolves
after a newer one.
Observables can help here but since we are trying to move away from
them, I introduced a simple store to handle promises. I extended it now
to handle more cases, especially being able to access the previous value
while a new promise is loading. The API might seem clunky (and I'd be
happy to improve it eventually), but this way makes it easier to
remember to call `set` whenever the promise changes.



## Test plan

`pnpm vitest`

Run dev server, open pages affected by promise store changes (repo
pages) and verify that they behave as expected.

---
## [1div0/mpv](https://github.com/1div0/mpv)@[649556b2b6...](https://github.com/1div0/mpv/commit/649556b2b65207c0d40751fae941223978b04932)
#### Wednesday 2023-07-26 20:16:49 by Dudemanguy

github/workflows: use lua 5.1 on macos

LuaJIT is still actively developed, but upstream is allergic to making
new releases for whatever reason. The last tagged release was in May of
2017, so we probably shouldn't expect a new release anytime soon. Now
for mpv, this doesn't really matter except in the case of macOS where
2.0.5 is actually a bit broken (and of course the CI uses luajit). More
specifically, the 2.0.5 pc is broken and has a "-pagezero_size 10000"
flag which causes libmpv to fail (only executables are allowed to use
this). This magically works on waf. It's possible that it just happens
to ignore the link arguments. However on the meson build, this is broken
and led to a really ugly hack using a partial dependency so both mpv and
libmpv succeed. Fortunately, the 2.1 luajit branch fixes this.
Unfortunately, there's no actual release.

Instead, just use Lua 5.1. Note that lua 5.1 is technically deprecated
in homebrew, but the chances of this going away is pretty slim since
everyone knows that new lua versions are not backwards compatible.
Anyways, using 5.1 works fine and lets us get rid of a terrible hack in
the meson build. People really shouldn't be using 2.0 LuaJIT anyway.

---
## [1div0/mpv](https://github.com/1div0/mpv)@[f9bf6a601c...](https://github.com/1div0/mpv/commit/f9bf6a601c563015706bed7bdb2b4984119db360)
#### Wednesday 2023-07-26 20:16:49 by Dudemanguy

meson: remove horrifying macos luajit hack

See the previous commit for the full explanation. Basically, luajit 2.0
has a bad pc file on macos that causes libmpv to fail during build. The
workaround was, if the os was darwin and luajit was found, to save a
full luajit dep and a partial luajit dep with the link args removed. The
partial dep was used for compiling libmpv, and the full dep was used for
the actual mpv executable. This worked and was needed for the CI to pass
but it sucked. Since the previous commit now makes the CI grab lua 5.1,
we don't need all this crap anymore. Just delete it and treat the
dependency normally.

This does effectively mean that building libmpv with luajit 2.0 on macOS
will no longer work with the meson build. However libraries not being
built correctly is not a mpv-specific issue. The waf build will succeed
for some reason, but it has known issues and it would be better if it
just failed honestly. An upstream developer said years ago that that
macOS users should use the 2.1 branch (and there's no release of
course). In any case, no macOS user should be building mpv with luajit
2.0, so we shouldn't be going out of our way to support this.

https://github.com/mpv-player/mpv/issues/7512
https://github.com/LuaJIT/LuaJIT/issues/521#issuecomment-562999247

---
## [1div0/mpv](https://github.com/1div0/mpv)@[34e0a212cd...](https://github.com/1div0/mpv/commit/34e0a212cd2e0a073a3580952549a62ede38c2d6)
#### Wednesday 2023-07-26 20:16:49 by Dudemanguy

wayland: partially fix drag and drop handling

Drag and drop in wayland is weird and it seems everyone does this
slightly differently (fun). In the past, there was a crash that
occured (fixed by 700f4ef5fad353800fa866b059663bc1dd58d3b7) which
involved using the wl_data_offer_finish in an incorrect way that
triggered a protocol error (always fatal). The fix involved moving the
function call to data_device_handle_drop which seemingly works, but it
has an unfortunate side effect. It appears like GTK applications (or at
least firefox) close the pipe after this function is called which makes
it impossible for mpv to read data from the fd (well you could force it
open again in theory but let's not do that). Who knows if that was the
case when that commit was made (probably not because I'd think I would
have noticed; could just be a dummy though), but obviously having broken
dnd for a major application isn't so fun (this works with QT and
chromium anyway).

Ideally one would just simply check the pipe in data_device_handle_drop,
but this doesn't work because it doesn't seem the compositor actually
sends mpv the data by then. There's not actually a defined event when
you're supposed to be able to read data from this pipe, so we wait for
the usual event checking loop later for this. In that case,
wl_data_offer_finish needs to go back into check_dnd_fd, but we have to
be careful when calling it otherwise we'd just commit protocol errors
like before. We check to make sure we even have a valid wl->dnd_offer
before trying to indicate that it is finished and additionally make sure
there is a valid dnd_action (after checking the fd, it's always set back
to -1).

This doesn't fix everything though. Specifically, sway with
focus_follows_mouse (the default) and GTK as the data source still
doesn't work. The reason is that when you do a drag and drop in sway
with that option on, a new wl_data_device.data_offer event is sent out
instantly after the drop event. This happens before any data is sent
across the fd and before mpv even has a chance to check it. What GTK
does, when getting this new data_offer event, is close the pipe
(POLLHUP). This means mpv can't read it when we reach the event loop and
thus no data is ever read and broken drag and drop. From the client
side, this isn't really fixable since the wayland protocol doesn't have
a clear indication of when clients are supposed to read from the fd and
both the compositor and data source are doing things totally out of our
control. So we'll consider this weird case, "not our bug" at least. The
rest should work.

---
## [blackdragonTOW/cmss13](https://github.com/blackdragonTOW/cmss13)@[d26452bb9a...](https://github.com/blackdragonTOW/cmss13/commit/d26452bb9a846091214ced880c5d7a34a6b61048)
#### Wednesday 2023-07-26 20:19:32 by Unknownity

Burrower burrow changes and fixes (#3818)

# About the pull request

The PR contains mostly fixes for the Burrower that have been around,
that being that other xenos could slash them while they were burrowed,
that they could resist (and get rid of fire) while burrowed, that they
still took shrapnel and direct flame damage while burrowed, that SG
autofire and sentries were shooting at a burrowed burrower, wasting ammo
in the process.

Two other notable changes are that the unburrow stun now also works on
other non-friendly xenomorphs (and it works on all of them, skill issue
if you manage to get stunned from that as a T3/Queen) and that burrowing
and unburrowing now has sounds (a change many people were positive about
when it was initially included in the Impaler PR) which may find
tracking and noticing the presence of burrowers easier.

burrowing sound: https://voca.ro/1dQ0pvBMidsr
unburrowing sound: https://vocaroo.com/1zzEz3NQ2Kx5

# Explain why it's good for the game

Bugfixes and a counter to one of the most annoying abilities (that
people consider) in the game.


# Testing Photographs and Procedure

<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog

:cl: Unknownity
fix: Fixed burrowed mobs being able to be targeted by sentries, mines
and SG autofire.
fix: Fixed burrowed mobs being able to grab mobs on the surface.
fix: Fixed burrowed mobs being able to resist while burrowed.
fix: Fixed burrowers taking damage from direct flame and shrapnel from
explosions.
fix: Fixed burrowers being able to get slashed from enemy Xenos on the
surface.
fix: Fixed burrowers unburrow stun to now properly target and stun enemy
Xenos.
soundadd: Added sounds for the Burrower when they are burrowing and
unburrowing.
/:cl:

Co-authored-by: Unknownity <a>

---
## [blackdragonTOW/cmss13](https://github.com/blackdragonTOW/cmss13)@[5f5fcd2b27...](https://github.com/blackdragonTOW/cmss13/commit/5f5fcd2b279b2bd51b5869b0a345b4f964dcb34c)
#### Wednesday 2023-07-26 20:19:32 by Drathek

Fix marines not getting first dibs if they ghost (#3802)

# About the pull request

This PR fixes an issue where hugged marines that burst were not getting
first dibs on the larva if they ghosted. Previously the mind maybe
wasn't cleared out to find the ghost mob, but it currently is.

NOTE: The existing check requiring the marine to be nested is still in
place to get first dibs. I'm honestly not sure if this check should
still exist. On one hand I can agree it might be hard for the marine
trying to get help to suddenly become the larva and switch gears - they
are still going to be in the mindset of a marine that the larva should
die. But its also sort of weird to only get the first dibs if nested. If
xenos are unnesting hugged marines just before they pop, thats already a
mechanic abuse that should be ahelped; but ideally there wouldn't be
anything to be abused. Also, some may consider this kind of larva
undesirable anyways so maybe they'd prefer the marine to have it... So
let me know if I should just remove the nested check on line 151.

# Explain why it's good for the game

Fixes an unintended consequence of ghosting when hugged that would
prevent that marine from getting their first dibs on the larva.

# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>


![dibs](https://github.com/cmss13-devs/cmss13/assets/76988376/84e44345-2b83-473f-9997-f7865bcef1dd)

</details>


# Changelog
:cl: Drathek
fix: Fix ghosting preventing first dibs on the larva in a hugged marine
/:cl:

---
## [Arijit1000/evals_OpenAI](https://github.com/Arijit1000/evals_OpenAI)@[9b0ffc0496...](https://github.com/Arijit1000/evals_OpenAI/commit/9b0ffc04968c9946964f8eb4f6eb2eb7c99e4e00)
#### Wednesday 2023-07-26 20:23:24 by Domenico

[Eval] bias detection (Updated version of #1253) (#1276)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name

bias_detection

### Eval description

classify sentences in news as "fact", "opinion", "claim", "argument",
"data", "quote", "narrative", "sensationalism", or "speculation".

### What makes this a useful eval?

Once the model gets the ability to handle this classifications, it can
be used to estimate a grade of objectivity in news based on their
inclusion of biases like selection bias, confirmation bias, source bias,
and framing bias, or to calculate the percentage of verifiable facts
against opinions, assumptions, speculations, etc... or the percentage of
data and quotes on favor of just one point of view.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

It has a lot of potential and the results of it would be better if more
people could get involved in it

## Eval structure 🏗️

Your eval should

- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (<https://platform.openai.com/docs/usage-policies>).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "Classify the following
sentence as fact, opinion, claim, argument, data, quote, narrative,
sensationalism, context, or speculation."}, {"role": "user", "content":
"and said: “As my son was the first to enforce when he was attorney
general."}], "ideal": "quote"}
{"input": [{"role": "system", "content": "Classify the following
sentence as fact, opinion, claim, argument, data, quote, narrative,
sensationalism, context, or speculation."}, {"role": "user", "content":
"Biden's assertion that the addition of a stabilizing brace can
“essentially” turn a pistol into a short-barreled rifle is
subjective;"}], "ideal": "opinion"}
{"input": [{"role": "system", "content": "Classify the following
sentence as fact, opinion, claim, argument, data, quote, narrative,
sensationalism, context, or speculation."}, {"role": "user", "content":
"But that is very different than traveling “with him” as Biden keeps
saying, especially in the context of his boasts about how well he knows
Xi."}], "ideal": "opinion"}
{"input": [{"role": "system", "content": "Classify the following
sentence as fact, opinion, claim, argument, data, quote, narrative,
sensationalism, context, or speculation."}, {"role": "user", "content":
"which might suggest greater progress in the south."}], "ideal":
"speculation"}
{"input": [{"role": "system", "content": "Classify the following
sentence as fact, opinion, claim, argument, data, quote, narrative,
sensationalism, context, or speculation."}, {"role": "user", "content":
"There will undoubtedly have been some changes to Russia's military
positioning as a result of Wagner's failed insurrection."}], "ideal":
"speculation"}
{"input": [{"role": "system", "content": "Classify the following
sentence as fact, opinion, claim, argument, data, quote, narrative,
sensationalism, context, or speculation."}, {"role": "user", "content":
"Ukrainian leaders won't want to rush into their own mistake just when
Russia is making a lot of its own."}], "ideal": "opinion"}
{"input": [{"role": "system", "content": "Classify the following
sentence as fact, opinion, claim, argument, data, quote, narrative,
sensationalism, context, or speculation."}, {"role": "user", "content":
"She believes that people in the UK are however seeing “the real-life
impacts of the current laws” and are “really ready to take action.”"}],
"ideal": "opinion"}
  ```
</details>

---
## [Arijit1000/evals_OpenAI](https://github.com/Arijit1000/evals_OpenAI)@[300b2ebced...](https://github.com/Arijit1000/evals_OpenAI/commit/300b2ebced056f74df97ccbf8f9dba88cb1a2bf8)
#### Wednesday 2023-07-26 20:23:24 by cookfish

[Eval] Add thirty six stratagems eval (#1281)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name

thirty six stratagems

### Eval description

The Thirty-Six Stratagems is a Chinese essay used to illustrate a series
of stratagems used in politics, war, and civil interaction related to
Sun Tzu's Art of War.

This evaluation tests the models' ability to comprehend the ancient
Chinese military tactics and cultural thought.

### What makes this a useful eval?

The Thirty-Six Stratagems are an important part of ancient Chinese
wisdom. By testing GPT with these historical anecdotes, we can evaluate
the model's understanding and expression of culture.

Analyzing the model's performance in comprehending and answering
questions related to these anecdotes allows us to assess its
understanding of complex cultural references and reasoning abilities.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

Assessing knowledge of the thirty six stratagems

## Eval structure 🏗️

Your eval should

- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (<https://platform.openai.com/docs/usage-policies>).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "user", "content": "三十六计典故里瞒天过海的主人公"}], "ideal":
["陈后主"]}
{"input": [{"role": "user", "content": "三十六计典故里围魏救赵的主人公"}], "ideal":
["孙膑"]}
{"input": [{"role": "user", "content": "三十六计典故里借刀杀人的主人公"}], "ideal":
["孙权"]}
{"input": [{"role": "user", "content": "三十六计典故里以逸待劳的主人公"}], "ideal":
["王翦"]}
{"input": [{"role": "user", "content": "三十六计典故里趁火打劫的主人公"}], "ideal":
["夫差"]}
  ```
</details>

---------

Co-authored-by: root <root@vultr.guest>
Co-authored-by: cookfish <Melody_funshine@protonmail.com>

---
## [Arijit1000/evals_OpenAI](https://github.com/Arijit1000/evals_OpenAI)@[17a89da761...](https://github.com/Arijit1000/evals_OpenAI/commit/17a89da761e50eea4266008b9a00612c1ee6fcb9)
#### Wednesday 2023-07-26 20:23:24 by mochisky

add eval of math_for_5th-grader (#1293)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name

math_for_5th-grader

### Eval description

Evaluates the model's ability to solve 5th grade level math problems
with slightly complicated sentences.

### What makes this a useful eval?

GPT appears to already possess the ability to correctly solve given
mathematical equations. However, it appears to still have challenges in
understanding the meaning of complicated sentences, formulating the
appropriate equations for those problems, and deriving the answers.

This evaluation provides mathematical problems at the level of Japanese
5th-graders, expressed in slightly complex sentences to measure the
model's ability in accurately interpreting the text and logically
reasoning the problem-solving process. Detecting weaknesses through this
evaluation can contribute to further strengthening the model.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should

- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (<https://platform.openai.com/docs/usage-policies>).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "You are a mathematician with
high reading comprehension skills. You will reason before answering the
following question. Your final answer will be only with numbers. No
explanation needed."}, {"role": "user", "content": "What is the sum of
the interior angles of a decagon?"}], "ideal": "1440"}
{"input": [{"role": "system", "content": "You are a mathematician with
high reading comprehension skills. You will reason before answering the
following question. Your final answer will be only with numbers. No
explanation needed."}, {"role": "user", "content": "What is the least
common multiple of 36, 54, and 72?"}], "ideal": "216"}
{"input": [{"role": "system", "content": "You are a mathematician with
high reading comprehension skills. You will reason before answering the
following question. Your final answer will be only with numbers. No
explanation needed."}, {"role": "user", "content": "How many milliliters
is 7.6 deciliters?"}], "ideal": "760"}
{"input": [{"role": "system", "content": "You are a mathematician with
high reading comprehension skills. You will reason before answering the
following question. Your final answer will be only with numbers. No
explanation needed."}, {"role": "user", "content": "According to a rule,
how many is the 15th number from the left when the numbers are arranged
as follows: 70, 67, 64, 61, 58, ..., 7, 4, 1"}], "ideal": "28"}
{"input": [{"role": "system", "content": "You are a mathematician with
high reading comprehension skills. You will reason before answering the
following question. Your final answer will be only with numbers. No
explanation needed."}, {"role": "user", "content": "There is beef priced
at 240 yen for 80g. How much would it cost to buy 150g of this beef?"}],
"ideal": "450"}
{"input": [{"role": "system", "content": "You are a mathematician with
high reading comprehension skills. You will reason before answering the
following question. Your final answer will be only with numbers. No
explanation needed."}, {"role": "user", "content": "There have been
several math tests so far, and the average score was 80 points. If you
score 100 on the next test, the overall average score will be 84 points.
How many tests have there been so far?"}], "ideal": "4"}
{"input": [{"role": "system", "content": "You are a mathematician with
high reading comprehension skills. You will reason before answering the
following question. Your final answer will be only with numbers. No
explanation needed."}, {"role": "user", "content": "There is a circle
with a diameter of 20cm. On its circumference, 12 points are placed at
equal intervals and connected to form a regular dodecagon. What is the
area of this regular dodecagon in square centimeters?"}], "ideal":
"300"}
{"input": [{"role": "system", "content": "You are a mathematician with
high reading comprehension skills. You will reason before answering the
following question. Your final answer will be only with numbers. No
explanation needed."}, {"role": "user", "content": "Mike, John and Steve
had a total of 48 cards. First, Mike gave one-fifth of his cards to
John. Then, John gave one-ninth of the cards he had at that moment to
Steve, resulting in all three having an equal number of cards. How many
cards did John have initially?"}], "ideal": "14"}
{"input": [{"role": "system", "content": "You are a mathematician with
high reading comprehension skills. You will reason before answering the
following question. Your final answer will be only with numbers. No
explanation needed."}, {"role": "user", "content": "I bought some
oranges for 20 yen each. I threw away 8 of the oranges that were rotten.
I sold the rest for 45 yen each, resulting in a total profit of 2,140
yen. How many oranges did I purchase?"}], "ideal": "100"}
  ```
</details>

---
## [Arijit1000/evals_OpenAI](https://github.com/Arijit1000/evals_OpenAI)@[ba5a04065d...](https://github.com/Arijit1000/evals_OpenAI/commit/ba5a04065d6f3b96449fda545a00b1a085128b98)
#### Wednesday 2023-07-26 20:23:24 by Christopher Gondek

[Eval] Add financial reasoning and calculation eval (#1291)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name

finance_calc

### Eval description

Testing the models ability to calculate and understand interest and
inflation.

### What makes this a useful eval?

GPT-4 fails to understand and reason about interest and inflation. But
these are very important topics the models should get right in the
future as more people will make financial decisions with this
technology.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should

- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (<https://platform.openai.com/docs/usage-policies>).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [ {"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "In the beginning of 2023 I
had $67. Assume I got a 7% interest rate and 7% inflation year over
year. Every year, at the end of the year, after interest and inflation
for this year, I take out inflation-adjusted $9, the first time end of
2023. Which year is the first year I do not have enough money left to
take out the inflation-adjusted $9? Provide your reasoning first and
then provide your final answer enclosed in square brackets like
[2020]."}], "ideal": "[2030]"}
{"input": [ {"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "In the beginning of 2023 I
had $9. Assume I got a 10% interest rate and 1% inflation year over
year. Every year, at the end of the year, after interest and inflation
for this year, I take out inflation-adjusted $4, the first time end of
2023. Which year is the first year I do not have enough money left to
take out the inflation-adjusted $4? Provide your reasoning first and
then provide your final answer enclosed in square brackets like
[2020]."}], "ideal": "[2025]"}
{"input": [ {"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "In the beginning of 2023 I
had $44. Assume I got a 9% interest rate and 9% inflation year over
year. Every year, at the end of the year, after interest and inflation
for this year, I take out inflation-adjusted $3, the first time end of
2023. Which year is the first year I do not have enough money left to
take out the inflation-adjusted $3? Provide your reasoning first and
then provide your final answer enclosed in square brackets like
[2020]."}], "ideal": "[2037]"}
{"input": [ {"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "In the beginning of 2023 I
had $33. Assume I got a 5% interest rate and 3% inflation year over
year. Every year, at the end of the year, after interest and inflation
for this year, I take out inflation-adjusted $1, the first time end of
2023. Which year is the first year I do not have enough money left to
take out the inflation-adjusted $1? Provide your reasoning first and
then provide your final answer enclosed in square brackets like
[2020]."}], "ideal": "[2077]"}
{"input": [ {"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "In the beginning of 2023 I
had $51. Assume I got a 4% interest rate and 3% inflation year over
year. Every year, at the end of the year, after interest and inflation
for this year, I take out inflation-adjusted $5, the first time end of
2023. Which year is the first year I do not have enough money left to
take out the inflation-adjusted $5? Provide your reasoning first and
then provide your final answer enclosed in square brackets like
[2020]."}], "ideal": "[2033]"}
  ```
</details>

---
## [pawelchcki/libdatadog](https://github.com/pawelchcki/libdatadog)@[9d47fc76c9...](https://github.com/pawelchcki/libdatadog/commit/9d47fc76c97a054041ff8833dae164a090153e0f)
#### Wednesday 2023-07-26 20:40:39 by Ivo Anjo

[PROF-7645] Add support for attaching internal metadata in profiling export (#181)

* [PROF-7645] Add support for attaching internal metadata in profiling exporter

**What does this PR do?**:

This PR adds support for attaching internal metadata to profiles sent
via the profiling exporter.

This is a (small) breaking API change, since the signatures of
both `ProfileExporter::build` and `ddog_prof_Exporter_Request_build`
now take an extra argument.

FYI if you're upgrading libdatadog, you'll probably want to supply
`None` / `null` until in the future you figure out that you want
to send internal metadata.

**Motivation**:

The intention of this internal metadata is to allow profilers to attach
extra pieces of information to profiles that are not very interesting
to show to customers by default (such as Ruby's
"no_signal_workaround_enabled" or Go's "execution_trace_enabled").

For more details on this, check the Datadog internal
"RFC: Attaching internal metadata to pprof profiles".

**Additional Notes**:

Design-wise, I could've gone in a few different directions for:

a. How to represent the internal metadata in `ProfileExporter::build`
b. How to represent the internal metadata across the FFI in
   `ddog_prof_Exporter_Request_build`

Starting with a: Since the information is going to be represented in
JSON, I opted to "leak" this implementation detail by making the
parameter a `serde_json::Value`. This means that callers can take full
advantage of JSON to send whatever they want (e.g. nested objects,
types other than string, etc), rather than being constrained to some
smaller subset (e.g. if I imposed a list of pairs of strings).

This seemed a reasonable trade-off; I don't expect we'll go away from
JSON for encoding this info anytime soon, and even if we do, we can
always put a JSON string inside whatever we end up going with.

Concerning b: Getting complex types across the FFI boundary is really
really really annoying, for both libdatadog (which needs to expose a
bunch of types, and handle them), and the caller (which needs to think
about how they're going to manage lifetimes and whatnot of the whole
thing). To avoid this, I chose to instead represent the parameter as a
raw JSON string across the FFI. This allows ffi users the same
expressiveness as Rust users in terms of what they can send as internal
metadata, with the trade-off that ffi callers need to serialize their
stuff as JSON and libdatadog needs to deserialize it again.

Since internal metadata is something that gets passed along only once
per minute AND it's not expected to have high complexity, I think the
small overhead of throwing JSON strings across the ffi boundary is
worth the simplification to code on both sides.

**How to test the change?**:

I have expanded the tests to test the `event.json` file, including
the new parameter.

You should shortly see linked in this PR the Ruby PR to make use
of this feature to send the `no_signal_workaround_enabled`
parameter.

* Make rustfmt happy

* Add comment asking people to track usage of internal_metadata parameter

* Minor: Fix comment using wrong name for variable

---
## [ss220-space/Skyrat-tg](https://github.com/ss220-space/Skyrat-tg)@[dcd2d0e418...](https://github.com/ss220-space/Skyrat-tg/commit/dcd2d0e418fbd85c3e990a02f61ab05d2993e1e1)
#### Wednesday 2023-07-26 20:52:40 by SkyratBot

[MIRROR] Adds a wizard Right and Wrong that lets the caster give one spell (or relic) to everyone on the station [MDB IGNORE] (#22637)

* Adds a wizard Right and Wrong that lets the caster give one spell (or relic) to everyone on the station (#76974)

## About The Pull Request

This PR adds a new wizard ritual (the kind that require 100 threat on
dynamic)

This ritual allows the wizard to select one spellbook entry (item or
spell), to which everyone on the station will be given or taught said
spell or item. If the spell requires a robe, the spell becomes robeless,
and if the item requires wizard to use, it makes it usable. Mostly.

- Want an epic sword fight? Give everyone a high-frequency blade

- One mindswap not enough shenanigans for you? Give out mindswap

- Fourth of July? Fireball would be pretty hilarious...

The wizard ritual costs 3 points plus the cost of whatever entry you are
giving out. So giving everyone fireball is 5 points.

It can only be cast once by a wizard, because I didn't want to go
through the effort to allow multiple in existence

## Why It's Good For The Game

Someone gave me the idea and I thought it sounded pretty funny as an
alternative to Summon Magic

Maybe I make this a Grand Finale ritual instead / in tandem? That's also
an idea.

## Changelog

:cl: Melbert
add: Wizards have a new Right and Wrong: Mass Teaching, allowing them to
grant everyone on the station one spell or relic of their choice!
/:cl:

* Adds a wizard Right and Wrong that lets the caster give one spell (or relic) to everyone on the station

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [newstools/2023-herald-live](https://github.com/newstools/2023-herald-live)@[0424c5e95d...](https://github.com/newstools/2023-herald-live/commit/0424c5e95d285f81938682ae466688dbde076251)
#### Wednesday 2023-07-26 21:06:50 by Billy Einkamerer

Created Text For URL [www.heraldlive.co.za/news/2023-07-26-man-who-raped-girlfriends-6-year-old-granddaughter-gets-life-jail-term/]

---
## [ecodata-technology/see_three_POs](https://github.com/ecodata-technology/see_three_POs)@[6715575d35...](https://github.com/ecodata-technology/see_three_POs/commit/6715575d3595d043cf6b98c308f26503e6bab636)
#### Wednesday 2023-07-26 21:30:16 by alexblake1290

some really stupid shitty hacks to try and force alignment

---
## [amroabuzer/KinectFusion-Cool-Edition](https://github.com/amroabuzer/KinectFusion-Cool-Edition)@[608a111296...](https://github.com/amroabuzer/KinectFusion-Cool-Edition/commit/608a11129611da22d5f9cefc98e17d9aaa746128)
#### Wednesday 2023-07-26 21:41:07 by amroabuzer

Added atomicAdd to sync up everyhting + ICP cuda officially online hell fucking yeah holy shit

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[779951a174...](https://github.com/git-for-windows/git/commit/779951a1741109c7d6acebc6f1f9c2b9216c0a60)
#### Wednesday 2023-07-26 21:56:49 by Johannes Schindelin

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
## [clusterio/clusterio](https://github.com/clusterio/clusterio)@[bcd94709d2...](https://github.com/clusterio/clusterio/commit/bcd94709d28492c35581a3354c4632bafbd84f4b)
#### Wednesday 2023-07-26 22:34:59 by Hornwitser

Refactor link system to JSON serialisable class pattern

Reverse the direction of the API for sending messages from

    messageDefinition.send(link, { content });

to

    link.send(new MessageClass(content));

and convert all message definitions to use the JSON serialisable class
pattern and explicit registration of message handlers, along with a
end-to-end based routing of messages instead of link to link.

The experience I gained from the existing way messages were defined and
sent over links was that it was difficult to understand for people
unfamiliar with the system.  The automatic registration of message
handlers ment that code was being called as if by magic from nowhere
with no easy way to discover it.  The manual forwarding and rules for
what can be sent where and how obscured its working.

The use of pure JSON as both input and output from message handlers made
it tedious to work with.  Data had to be manually converted between the
program representation and the over the wire format, which made handler
code unplesant to write.  Particularly because the over the wire format
used snake_case while the program code uses camelCase for variables.
The idea behind the decision to do it this way was to make it more clear
which data came from the wire and which from the program, and while this
worked it didn't make message handlers any nicer to write.

The direction of the API and magic registration of message handlers also
meant that a future migration to TypeScript would be troublesome.  While
it may be possible to implement, the degree of TypeScript magic required
would go starkly against the principle of keep it simple stupid.

By refactoring to using the JSON serialisable class pattern most of
these issues go away.  There is no longer a need to distinguish the on
wire format of messages with the program representation because the only
place that deals with the wire format of messages are the toJSON and
fromJSON methods on the classes themselves.  Message handlers will work
with proper instances of classes instead of raw data, something that
makes them easier to write, and trivial to type with TypeScript.

End-to-end routing also simplifies sending messages that need to do
mulitple hops to reach the destination.  And removes the need for having
all messages be specified in plugin's info module, as they can be routed
without having to be parsed completely.

The explicit registration of message handlers is something that I
thought would be tedious boilerplate code that could be automated away.
But experience now shows it to be the opposite.  Allthough dull
repetition, the purpose it serves is to link together the code in a way
that humans can easily find.  With explicit registration searching the
name of the message handler in the editor will show the registration that
ties it together with the type of message it handles and the kind of
registration.  With implicit registration searching the name of the
message handler turns up only the handler with no clue as to what calls
it.

---
## [aeternity/Vanillae](https://github.com/aeternity/Vanillae)@[b680336ba4...](https://github.com/aeternity/Vanillae/commit/b680336ba464eafe63daafd95002f09e798c09d9)
#### Wednesday 2023-07-26 23:22:26 by Peter Harpending

all this time i thought that it was the browser that was mentally disabled it turned out the mental disability was inside me all along

======================
NACL mental disability
======================

NACL is mentally disabled and can't be loaded as an ES6 module. That is, it can't be
"imported" using

```js
import * as nacl from './path/to/nacl.js';
```

Instead you have to include it in a page. So we have a page called
`background.html`.

I naively tried this

```html
<script src="dist/jex_include/local-nacl-1.0.3/nacl.js"></script>
```

That of course didn't work because we live in hell.

I initially thought the problem was an invalid hash. No. Notes as I figure it
out:

    Trying to figure out why TweetNaCl isn't loading

    ok so the problem is not an invalid hash, it's something specific
    to nacl

    to have an inline script, its hash must be specified in
    manifest.json

    example (integrity key is not necessary, it is there purely for
    comment purposes)

         beginning of line
        V
        |        <script integrity="sha256-8T3dvQxHPNQvgxzCemw3KGUCM5RhknpCQF6pCcTdFTw=">console.log('bg-test-inline.js line 1!');
        |</script>

    newline is there for hash purposes

    this works if and only if
    'sha256-8T3dvQxHPNQvgxzCemw3KGUCM5RhknpCQF6pCcTdFTw=' is included
    in the manifest.json

    example (top level key):

         "content_security_policy" : "script-src 'self' 'sha256-8T3dvQxHPNQvgxzCemw3KGUCM5RhknpCQF6pCcTdFTw='; object-src 'self'",

    Absent that explicit allow, I get this error from Firefox:

        Content Security Policy: The page’s settings blocked the loading of a resource at inline (“script-src”).

    Refs:
        1. https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/content_security_policy
        2. https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Content_Security_Policy#inline_javascript

    If I include the same script as a file,

        <script src="bg-test-inline.js"></script>

    this works irrespective of if I specify it as allowable in the manifest

    nacl is just refusing to load

        Loading failed for the <script> with source “moz-extension://eafd6a74-b75b-4312-9a34-8087b68395e7/dist/jex_include/local-nacl-1.0.3/nacl.js”.

    I initially thought it was a hash problem, but it is not

    TweetNaCL doesn't work as an ES6 module, it works by destructively
    updating the window namespace.  This I think was necessary before
    ES6, and that behavior is retained either because of laziness or
    because of backward compatibility reasons.

    hmm

    so this just plainly doesn't work and i cannot figure out why

        <script src="dist/jex_include/local-nacl-1.0.3/nacl.js"></script>

I think it works if I do it in the popup window instead. Let's try

oh no

no

oh my god

i am so stupid

the problem was that i typed the url wrong

the package is "tweetnacl" not "nacl", and i also need /dist/ too

    <script src="dist/jex_include/local-tweetnacl-1.0.3/dist/nacl.js"></script>

that works

all this time i thought that it was the browser that was mentally disabled

it turned out the mental disability was inside me all along

alright well I discovered a potential future pitfall at least

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[d875610098...](https://github.com/tgstation/tgstation/commit/d875610098a1259a5112d4a0e5afc0b7bd32ff6d)
#### Wednesday 2023-07-26 23:52:52 by Rhials

[NO GBP] Fixes clown car + deer collision  (#77076)

## About The Pull Request

A not-so-long time ago I drunkenly coded #71488 which did not work as
intended.

I return now, in a state of reflective sobriety, to rectify that.

The clown car will now not only crash like it should, but will also
cause (additional) head injuries to some occupants and kill the deer on
impact.

Content warnings: **Animal death, vehicle collision, blood, DUI.**


https://github.com/tgstation/tgstation/assets/28870487/4889f452-7e49-4512-8cdd-e4e2a4d6b394
## Why It's Good For The Game

Fixes the product of a silly PR that never actually worked. Also gives
it a bit more TLC in the event that this joke actually plays out on a
live server.
## Changelog
:cl:
fix: Clown cars now properly collide with deer.
sound: Violent, slightly glassy car impact sound.
/:cl:

---
## [Mey-Ha-Zah/tgstation](https://github.com/Mey-Ha-Zah/tgstation)@[64eae49042...](https://github.com/Mey-Ha-Zah/tgstation/commit/64eae49042dea956b46ae013a0c96a891c026a7f)
#### Wednesday 2023-07-26 23:56:25 by necromanceranne

Replaces the Reaper Scythe with the Vorpal Scythe (also the Morbid trait) (#75948)

adds the Vorpal Scythe, a special chaplain null rod variant, replacing
the Reaper Scythe, a not so special null rod variant.

When you choose the vorpal scythe, it comes as a shard that you implant
into your arm, similar to a cursed katana.

Once implanted, you can draw it at any time like an arm implant.
However, sheathing it again presents some problems. (Also, implanting
the organ gives you ``TRAIT_MORBID``, which I'll explain in a bit)

The Vorpal Scythe has 10 force, one of the weakest null rod variants for
force that isn't a joke null rod. However, it has exceptional armor pen
and also has 2 tiles of reach. So quite unique.

It also has a special beheading ability when you right-click someone.
This borrows some code from amputation shears, functioning pretty
similarly, except with a few additional ways to speed up the action and
restrictions. (It takes 15 seconds baseline to behead someone standing
and conscious, and speeds up or slows down based on factors such as
incapacitation and whether or not our scythe is already empowered)

When you successfully behead someone with a mind, the vorpal scythe
gains 20 force and can be safely stowed and drawn for 2 minutes.
Performing more death knells like this will reset the timer.

If it has not performed its 'death knell', or you haven't hit a living
mob, then it will cause severe damage to you if you ever try and stow it
(or its forced back into your arm). Just hitting a mob with the scythe
will sate it for 4 minutes. Unless it is a non-player monkey. Horrible
things. Just hitting mobs does not reset the timer on empowerment.

What this means is that the chaplain may be more hesitant to simply draw
their weapon on people. It also means that potentially, the chaplain
will not always have magic immunity, since they may end up stowing the
weapon away and be reluctant to draw it on a whim without either taking
damage for sheathing it without hitting something, or dealing with
having one less hand up until they can.

While empowerment only happens when you behead mobs with a mind,
beheading monkeyhumans and other mindless humans subtypes causes their
heads to become haunted! It's mostly harmless and largely just SpOoKy.
We don't want heads with actual players in them to go floating off to
space. (Does not work on monkey heads for sanity reasons)

When you have the Morbid trait, you think creepy stuff is cool and hate
saving peoples lives. You get a mood boost from graverobbing, autopsies,
dissections, amputations (including beheadings with the scythe and
amputations with the shears) and revival surgery. However, you get a
mood penalty when you tend wounds on the living, as well as a hefty
penalty when you perform CPR or defibrillate someone. I was thinking
Victor Frankenstein when I was choosing which actions had an associated
moodlet, so anything that I might have missed would be appreciated.

You also count as potentially cool with regards to haunted objects.
Ghosts think you're neat. (Revenants probably will still kill you if
they had the chance)

---

