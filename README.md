## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-08-10](docs/good-messages/2023/2023-08-10.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,297,436 were push events containing 3,452,968 commit messages that amount to 254,352,210 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 62 messages:


## [mc776/freedoom](https://github.com/mc776/freedoom)@[a828330d25...](https://github.com/mc776/freedoom/commit/a828330d25e950933bc97ef5ba5630e2a2dca93a)
#### Thursday 2023-08-10 00:11:29 by mc776

levels: more minor fixes. (#1040)

* levels: fix e1m2 tutti frutti around exit door.

Also took the liberty of fixing a longtime pet peeve I had about the really bright grey-white of the exit room steps clashing with the rest of the room for no apparent reason. (It looks less bad with Korp's new greys but we're not adding those yet...)

* levels: fix floating candle on map22.

It's fine until you actually use the secret, at which point it snaps to the top of the lowering platform.

* levels: more minor fixes.

Mostly for objects "floating" with a tiny bit of their hitbox rounded to be overlapping a higher adjacent floor.

E1M8
Inside the pillars containing the painlords there are two that spawn gore (and a dead player) in lieu of painlords only on easy. These have now been edited so that in each pillar the gore appears whenever the painlord does not. (The player has also been changed to a gore actor.)

Map03
Floaties by the first door switch.

Map23
Central room with the barrels and combat slugs has several gore decorations that do not appear on hard, but do not block movement nor represent any living monsters that might appear there in hard. Flagged to appear in all skill levels (and also not be flagged ambush).

Map25
1-pixel vertical misalignment on line 44.

Map28
Floaty medikit(s?) near (-955,-435), moved away from the double teleport pad.
Fixed the textures on that door now that the SLOPPY textures have been updated
Moved stuff around the starting skull switch so you start with a screen full of skull again.

Map29
Floaty shellbox 444.

* levels: more minor fixes.

Mostly to address #1043.

Map09
- Moved the crates in front of the eastern teleport door to keep the player from potentially falling into the gap between the big crate and the main crate rack and softlocking. The small step-crates are now also properly aligned with the flat they use.

Map14
- The entire lower floor of the big octagon room has been lowered to -56 from -48. This restores access to the alcove in front of the minigun secret, and also better aligns with the textures of several surrounding walls.
- Merged the sectors of the yellow key cage teleporter pad so the lights would sync.

Map15
- A room will lower two teleporters when you step in and two worms will warp in through those teleporters in hard, one in medium, none in easy. It looks bugged where the worms don't appear and absolutely nothing shows up, so pickups are revealed instead when they don't.

Map18
- Added one more step crate to let the player directly access the necromancer soul sphere (and the health bonus tucked away in the corner) without retracing their route back to the upper ledge.

Map25
- Got rid of that starting elevator once and for all. The only purpose in forcing that starting gunshot was to make that first room marginally more awful to pistol-start. Moved the shotgun and shells to the "outside" platforms to make up for it.
- Widened the side windows facing the yellow key so the trilobites have room to move.
- Shrunk down the exit line to make it completely impossible to trigger it while the painlord/necromancer standing there is alive.
- Added more monster blockers to the RL warp-in ambush closet, as the worms would still sometimes warp in both on the same side. I've also made the destination sectors larger as that simplifies the underlying geometry a bit.
- Flagged everything in the deathmatch arena multi-only.
- Thing 445 (last monster before SSG in hard mode) is now a pain lord instead of an octaminator.

* levels: more minor fixes.

Map13
Exit teleport pad lines now block monsters.

Map18
End soulsphere secret is now tagged as secret.

Map19
The straferun armour trench setup could not possibly work without having the worms below block your movement sometimes. The trench is now fenced off and the platform accessible by bridge; the pinkies are now spectres outside of easy and hard gives you two more of them; they can only harm you by teleporting.

* levels: readjust map28 skull.

The vertical offset would no longer be needed after #1047; however the tiling is a bit off if we need to offset this horizontally due to the additional trim, so a new linedef was added.

* levels: map26 minor fixes.

The secret blue lift switch error message would indicate it's a "door" which despite being correct from an engine point of view doesn't reflect its actual function.

The red armour secret is now player-shoot only, and the wall breach effect is instant.

* levels: fix high jump platform texture alignment.

---
## [Peliex/tgstation](https://github.com/Peliex/tgstation)@[dc0e5caca7...](https://github.com/Peliex/tgstation/commit/dc0e5caca763769242fe9254d95049ac0468bf64)
#### Thursday 2023-08-10 00:31:50 by Sheits

Base Female sprite tweaks (#77407)

## About The Pull Request

ASS STUFF HAS BEEN REMOVED BUT I STILL HATE IT

This PR tones down the proportions of the female base sprites, as
currently they have about SIX extra pixels on the ass and a random pixel
missing from the neck, which breaks some hairstyles & makes the neck
look quite stupid.
It also adds a couple pixels to the male one because theirs was so
stupidly SMALL it looked like they had no tailbone (still does, kind
of).

Here is the current sprite 

![image](https://github.com/tgstation/tgstation/assets/81964183/1bf22dd7-2b06-4632-8617-b89b3b1c8d2c)
& new sprite (only neck pixel removed)

![image](https://github.com/tgstation/tgstation/assets/81964183/b1228e01-23e0-4508-86a6-bc8e73b0fcd0)

## Why It's Good For The Game

Fixes some hairs


![image](https://github.com/tgstation/tgstation/assets/81964183/3b293cf9-2661-4358-a327-2882acb93067)


## Changelog

:cl:
image: fixes weird inconsistency on the neck and butt of the female base
sprite
/:cl:

---
## [Peliex/tgstation](https://github.com/Peliex/tgstation)@[3dc75f84f2...](https://github.com/Peliex/tgstation/commit/3dc75f84f2eebc388c7f698284d77df4d8cf8fdf)
#### Thursday 2023-08-10 00:31:50 by YakumoChen

Chen And Garry's Ice Cream: Ice Cream DLC (LIZARD APPROVED!) (#77174)

## About The Pull Request

Authored with help and love from @Thalpy 

I scream for ice cream!!


![image](https://github.com/tgstation/tgstation/assets/10399117/db1e559b-7dab-499b-a076-8f12748ba2e8)

Introduces many new flavours of ice cream:
-Caramel
-Banana
-Lemon Sorbet
-Orange Creamsicle
-Peach (Limited Edition!)
-Cherry chip
-Korta Vanilla (made with lizard-friendly ingredients!)


![image](https://github.com/tgstation/tgstation/assets/10399117/99a87615-f55c-49be-8caf-2b1ac4c7f03f)

Korta Cones! Now too can Nanotrasen's sanitation staff enjoy the wonders
of ice cream!
You can also substitute custom ice cream flavours with korta milk!
Finally, the meaty ice cream lactose-intolerants asked for is in reach!

## Why It's Good For The Game

I always thought the ice cream vat could use more flavours. The custom
flavour besides, it isn't as intuitive to rename the cone and the added
variety is good. The lack of a banana flavour already was questionable.
All the ice cream flavours used a selection of five sprites, now it's
just one sprite and better supporting more additions.
Some of the flavours don't use milk! You can't do this with the custom
flavour, making it slightly more interesting.

## Changelog
:cl: YakumoChen, Thalpy
add: Chen And Garry's Ice Cream is proud to debut a wide selection of
cool new frozen treat flavours on a space station near you!
add: Chen And Garry's Ice Cream revolutionary Korta Cones allow our ice
cream vendors to profit off the lizard demographic like never before!
code: Ice cream flavours now are all greyscaled similarly to GAGs
/:cl:

---
## [rizalgowandy/oauth2](https://github.com/rizalgowandy/oauth2)@[a835fc4358...](https://github.com/rizalgowandy/oauth2/commit/a835fc4358f6852f50c4c5c33fddcd1adade5b0a)
#### Thursday 2023-08-10 00:49:38 by Brad Fitzpatrick

oauth2: move global auth style cache to be per-Config

In 80673b4a4 (https://go.dev/cl/157820) I added a never-shrinking
package-global cache to remember which auto-detected auth style (HTTP
headers vs POST) was supported by a certain OAuth2 server, keyed by
its URL.

Unfortunately, some multi-tenant SaaS OIDC servers behave poorly and
have one global OpenID configuration document for all of their
customers which says ("we support all auth styles! you pick!") but
then give each customer control of which style they specifically
accept. This is bogus behavior on their part, but the oauth2 package's
global caching per URL isn't helping. (It's also bad to have a
package-global cache that can never be GC'ed)

So, this change moves the cache to hang off the oauth *Configs
instead. Unfortunately, it does so with some backwards compatiblity
compromises (an atomic.Value hack), lest people are using old versions
of Go still or copying a Config by value, both of which this package
previously accidentally supported, even though they weren't tested.

This change also means that anybody that's repeatedly making ephemeral
oauth.Configs without an explicit auth style will be losing &
reinitializing their cache on any auth style failures + fallbacks to
the other style. I think that should be pretty rare. People seem to
make an oauth2.Config once earlier and stash it away somewhere (often
deep in a token fetcher or HTTP client/transport).

Change-Id: I91f107368ab3c3d77bc425eeef65372a589feb7b
Signed-off-by: Brad Fitzpatrick <bradfitz@golang.org>
Reviewed-on: https://go-review.googlesource.com/c/oauth2/+/515675
TryBot-Result: Gopher Robot <gobot@golang.org>
Reviewed-by: Roland Shoemaker <roland@golang.org>
Reviewed-by: Adrian Dewhurst <adrian@tailscale.com>
Reviewed-by: Michael Knyszek <mknyszek@google.com>

---
## [Oyu-De/Paradise](https://github.com/Oyu-De/Paradise)@[2d10818063...](https://github.com/Oyu-De/Paradise/commit/2d1081806334fc023de600338b836d55dd6fa5ee)
#### Thursday 2023-08-10 00:52:56 by ATP-Engineer

Fixes IV bag blood overlays being too damn bright for some mixtures (#21813)

* Removes old .dmi

* Fixes blood overlay coloring being too bright for IV bags

* Fine-tuning

* Makes the blood bag IV color overlays not as bright as they used to be

In hindsight it was probably easy to avoid

* FINAL TUNE UP

FUCK

* Fixes coloring for IV bags so they're not too bright

FINAL COMMIT

---
## [YesterdaysPromise/tgstation](https://github.com/YesterdaysPromise/tgstation)@[52c8da7ea4...](https://github.com/YesterdaysPromise/tgstation/commit/52c8da7ea49ef566c9a997a4b7cfc5d3d2a59178)
#### Thursday 2023-08-10 01:59:50 by Jacquerel

PAI Holochassis are now leashed to an area around their card (#76763)

## About The Pull Request

This change restricts PAI holograms to an area around their assigned PAI
card. If you leave this area, you are teleported back to the card's
location (but not automatically put back into the card).

https://www.youtube.com/watch?v=L2ThEVa4nx8

This setting can be configured from the PAI menu, it's set pretty short
in the video because otherwise it wouldn't teleport when I threw the
card and I like doing that.

![image](https://github.com/tgstation/tgstation/assets/7483112/faf0fa0b-e9d6-4990-8d8c-f30def2892f1)

To accomodate this I set up a component to deal with a reasonably common
problem I have had, "what if I want to track the movement of something
in a box in a bag in someone's inventory". Please tell me if the
solution I came up with is stupid and we already have a better one that
I forgot about.

Also now you can put pAIs inside bots again, by popular request.

## Why It's Good For The Game

Personal AIs are intended to be personal assistants to their owner.
rather than fully independent entities which can pick up their own card
and leave as soon as they spawn.
As "aimless wanderer" players can now possess station bots, pAIs can be
limited to an area around the bearer of their card.

Because the holoform now doesn't contain the card, this also means that
a PAI cannot run off and then be impossible to retrieve. You are always
in control of where it can go.

Also it's funny to throw the card and watch the chicken get teleported
to it.

## Changelog

:cl:
add: Personal AI holograms are now limited to an area around their PAI
card. The size of this are can be configured via the PAI card.
add: pAI cards can now be placed inside bots in order to grant them
control of the bot.
/:cl:

---
## [efzapa/Paradise](https://github.com/efzapa/Paradise)@[a3dc32cf34...](https://github.com/efzapa/Paradise/commit/a3dc32cf344dbd441e85f6cbb694b166dc1f5e4b)
#### Thursday 2023-08-10 02:39:25 by ATP-Engineer

Fixes issue where Turret Control sprites arent actually updated in previous PR (#21538)

* Removes actual turret file

FUCK

* Fixes turret controllers not actually being changed

GOD DAMNIT.

---
## [c0ntradicti0n/dialectics](https://github.com/c0ntradicti0n/dialectics)@[f9f4356a69...](https://github.com/c0ntradicti0n/dialectics/commit/f9f4356a692cfd94821612319be54b753134493b)
#### Thursday 2023-08-10 02:40:35 by c0ntradicti0n

Automated TOC Commit: 3/3/1/3/.Agnosticism.md 3/2/2/2/_Federal-Unitary.md 2/2/3/3/.Healthcare.md 3/2/2/1/_Authority-Sovereignty.md Categories.md" 1/3/3/1/_Heredity-Variation.md 3/1/1/2/_Free-Bound.md 2/2/3/1/_Success-Failure.md Space.md" 2/1/1/2/_Famine-Feast.md 2/3/1/3/.Duties.md 3/3/2/2/.Narrative.md Art.md" 1/2/3/1/_Metrical-Triangular,.md 3/1/2/1/_Dissonance-Consonance.md 2/2/1/3/.Reasoning.md Thinking.md" 3/1/1/3/.Semiotics.md Theories.md" 2/1/1/1/_Thirst-Hydration.md 2/1/3/3/.Distribution.md 2/1/1/1/.Dependence.md 1/3/3/3/.Adaptation.md 3/3/2/3/_Choreography-Improvisation.md 2/2/1/3/_Induction-Deduction.md 1/2/1/1/_Structured-Unstructured.md 3/1/2/2/.Harmony.md 3/1/1/2/.Morphology.md 3/1/1/3/_Signifier-Signified.md 2/2/3/1/.Competitions.md 2/3/1/2/.Laws.md 3/1/1/1/.Phonetics.md 2/1/1/1/.Eating.md Inquiry.md" Stories.md" 1/3/3/3/.Evolution.md 2/2/2/3/.Fallacies.md 3/3/1/2/_Spiritual-Material.md 2/3/1/2/.Rights.md 3/3/1/2/.Animism.md 2/2/2/3/_Logical-Emotional.md 2/1/1/1/.Drinking.md 3/1/2/1/.Melody.md 3/3/2/2/.Literature.md 3/3/2/3/.Dance.md 3/2/1/2/.Curriculum.md 2/2/2/1/_Righteous-Wicked.md 3/3/1/1/.Deism.md 2/2/2/1/.Morality.md 1/1/3/1/_Finite-Infinite.md 3/2/3/2/_Capitalism-Socialism.md 2/3/2/1/_Old-New.md 1/1/3/2/_Countable-Uncountable.md 1/3/2/2/_Covalent-Ionic.md 3/2/3/1/_Rights-Liberties.md 2/2/3/3/_Sickness-Wellness.md 1/3/1/3/_Observed-Unobserved.md Economy.md" Myths.md" 2/2/2/1/.Ethics.md 3/1/3/3/.Mediation.md 3/1/1/1/.Phonology.md Journey.md" 3/3/1/3/.Atheism.md 3/3/2/1/_Form-Content.md Dimensions.md" 2/2/2/3/.Logic.md Diagram.md" 1/1/3/3/_Homogeneity-Heterogeneity.md 2/2/3/2/.Performances.md 3/1/2/1/.Tune.md Philosophy.md" 3/1/2/2/_Stable-Unstable.md 1/2/3/2/_Past-Future.md 3/2/1/3/.Pedagogy.md Epics.md" 2/2/3/3/.Medicine.md Prophecies.md" 3/1/2/2/.Chords.md 3/3/1/2/.Polytheism.md 3/3/2/1/.Sculpture.md 3/3/3/1/_Beginning-End.md 2/3/2/1/.Customs.md 2/1/2/3/.Reproduction.md 2/3/2/2/_Resistance-Adoption.md 1/1/2/3/.Boundaries.md 3/3/2/2/_Plot-Character.md 3/3/3/3/_Decay-Renewal.md 3/1/2/3/.Beat.md 2/3/2/3/_Discovery-Creation.md Thinking.md" 1/3/2/1/_Elementary-Composite.md 1/3/2/3/_Organic-Inorganic.md 1/3/3/3/_Mutation-Selection.md Art.md" 2/2/3/1/.Sports.md 2/3/1/3/.Responsibilities.md 3/1/1/1/_Voiced-Unvoiced.md 2/1/1/3/.Shelter.md 2/3/2/3/.Achievements.md 3/1/2/3/_Syncopated-Regular.md 1/3/1/1/_Potential-Kinetic.md 2/1/2/2/.Gender.md 3/3/1/3/_Belief-Doubt.md 2/3/1/2/_Legal-Illegal.md 3/3/1/1/_Transcendent-Immanent.md 3/1/1/3/.Pragmatics.md 3/3/3/2/_Trial-Triumph.md Myths.md" 2/3/1/1/.Inventions.md 3/1/1/2/.Syntax.md 1/3/1/2/_Statics-Dynamics.md Chain.md" 1/1/2/3/_Finite-Infinite.md 3/3/1/1/.Monotheism.md Dimensions.md" 2/2/1/1/_Bias-Neutral.md 3/2/2/3/_Majority-Minority.md 2/3/2/2/.Revolutions.md 2/2/1/2/_Hypothesis-Theory.md 2/3/1/3/_Obligation-Choice.md Continuum.md" 3/1/2/3/.Rhythm.md

---
## [kast-spells/summon](https://github.com/kast-spells/summon)@[29a22286f3...](https://github.com/kast-spells/summon/commit/29a22286f346da4f518b4f7bca14f88945f06252)
#### Thursday 2023-08-10 02:51:13 by Namen Malkav

"So it seems sleep has a cousin named death and Chuck Norris is sleeps Uncle which makes Chuck Norris Death's dad! Oh man i feel sorry for death's boyfriend!"

---
## [AndrewDunne/FreeSpirit](https://github.com/AndrewDunne/FreeSpirit)@[a852738bcd...](https://github.com/AndrewDunne/FreeSpirit/commit/a852738bcdd2f888c8919f51908f367b0e5733ca)
#### Thursday 2023-08-10 03:17:02 by Chord Shore

Mandatory late night crisis

So I had the silly idea to make a quick change to the folder layout in the content browser before I went to bed. Just shift a few folders around, what could go wrong right? They're just folders after all...

Turns out Unreal automatically deletes empty subfolders when you move a parent folder.

Fuck. I had to recreate a ton of subfolders using the screenshot I posted to #progress. Only took 20 minutes, but I'm lucky I had that for reference or I would have lost a day. Should be ok now, but the "Sound/Audio_*" folder structure is LOCKED until I can populate each one with foley and other assets.

---
## [Xexxa/serenity](https://github.com/Xexxa/serenity)@[8edc2c2689...](https://github.com/Xexxa/serenity/commit/8edc2c2689e094382544d815864312bcdb2205a9)
#### Thursday 2023-08-10 03:40:10 by Xexxa

Base: Improve emoji

Remove unneccessary left/right padding

❣️ - U+2763 HEART EXCLAMATION
🚶 - U+1F6B6 PERSON WALKING
🚴 - U+1F6B4 PERSON BIKING
🌻 - U+1F33B SUNFLOWER
🪻 - U+1FABB HYACINTH
🍉 - U+1F349 WATERMELON
🍍 - U+1F34D PINEAPPLE
🫒 - U+1FAD2 OLIVE
🌽 - U+1F33D EAR OF CORN
🌯 - U+1F32F BURRITO
🍘 - U+1F358 RICE CRACKER
🧁 - U+1F9C1 CUPCAKE
🍫 - U+1F36B CHOCOLATE BAR
🍭 - U+1F36D LOLLIPOP
🍼 - U+1F37C BABY BOTTLE
🧋 - U+1F9CB BUBBLE TEA
🧃 - U+1F9C3 BEVERAGE BOX
🥢 - U+1F962 CHOPSTICKS
💈 - U+1F488 BARBER POLE
🌛 - U+1F31B FIRST QUARTER MOON FACE
🌜 - U+1F31C LAST QUARTER MOON FACE
🌡️ - U+1F321 THERMOMETER
🪐 - U+1FA90 RINGED PLANET
⚡ - U+26A1 HIGH VOLTAGE
💧 - U+1F4A7 DROPLET
🧨 - U+1F9E8 FIRECRACKER
🥇 - U+1F947 1ST PLACE MEDAL
🥈 - U+1F948 2ND PLACE MEDAL
🥉 - U+1F949 3RD PLACE MEDAL
🏓 - U+1F3D3 PING PONG
🪀 - U+1FA80 YO-YO
♟️ - U+265F CHESS PAWN
🧦 - U+1F9E6 SOCKS
💄 - U+1F484 LIPSTICK
📱 - U+1F4F1 MOBILE PHONE
🔌 - U+1F50C ELECTRIC PLUG
💡 - U+1F4A1 LIGHT BULB
📍 - U+1F4CD ROUND PUSHPIN
🔩 - U+1F529 NUT AND BOLT
🪝 - U+1FA9D HOOK
🧪 - U+1F9EA TEST TUBE
🔭 - U+1F52D TELESCOPE
🩸 - U+1FA78 DROP OF BLOOD
💊 - U+1F48A PILL
🩹 - U+1FA79 ADHESIVE BANDAGE
🧼 - U+1F9FC SOAP
🪥 - U+1FAA5 TOOTHBRUSH
♀️ - U+2640 FEMALE SIGN
♂️ - U+2642 MALE SIGN
➕ - U+2795 PLUS
➗ - U+2797 DIVIDE
❓ - U+2753 RED QUESTION MARK
❔ - U+2754 WHITE QUESTION MARK
❕ - U+2755 WHITE EXCLAMATION MARK
❗ - U+2757 RED EXCLAMATION MARK
◼️ - U+25FC BLACK MEDIUM SQUARE
◻️ - U+25FB WHITE MEDIUM SQUARE
◾ - U+25FE BLACK MEDIUM-SMALL SQUARE
◽ - U+25FD WHITE MEDIUM-SMALL SQUARE
▪️ - U+25AA BLACK SMALL SQUARE
▫️ - U+25AB WHITE SMALL SQUARE
🚩 - U+1F6A9 TRIANGULAR FLAG

---
## [domondi1/IlluminateSite](https://github.com/domondi1/IlluminateSite)@[401f4ab2a5...](https://github.com/domondi1/IlluminateSite/commit/401f4ab2a532de75c097dc0d3222984321365dd5)
#### Thursday 2023-08-10 03:53:30 by domondi1

Octob- her HTML

Octob-her Foundation: Empowering Needy Students in Kenya

Discover Octob-her, a non-profit initiative dedicated to illuminating the path of education for underprivileged children in Kenya. Our website showcases our mission to uplift young girls, providing scholarships that break the chains of early marriage and FGM, and offering school supplies that nurture dreams. Experience stories of resilience, meet Amina and Nia, whose lives have been transformed by our commitment. Join us in weaving a future where education empowers change and dreams flourish.

---
## [Bubberstation/Bubberstation](https://github.com/Bubberstation/Bubberstation)@[a1609c4536...](https://github.com/Bubberstation/Bubberstation/commit/a1609c4536fe05f95560bd1a1be4607b944ee5a5)
#### Thursday 2023-08-10 04:21:48 by SkyratBot

[MIRROR] [NO GBP] Fixes clown car + deer collision  [MDB IGNORE] (#22709)

* [NO GBP] Fixes clown car + deer collision  (#77076)

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

* [NO GBP] Fixes clown car + deer collision

---------

Co-authored-by: Rhials <28870487+Rhials@users.noreply.github.com>

---
## [yasaswini2005/Our-dream-menu](https://github.com/yasaswini2005/Our-dream-menu)@[a4c3a0b82f...](https://github.com/yasaswini2005/Our-dream-menu/commit/a4c3a0b82f4df801c824fa838bb0a134c6565b4a)
#### Thursday 2023-08-10 04:23:34 by GURIVI REDDY YASASWINI

Add files via upload

 our dream menu 
 home page
breakfast page
lunch page
dinner page
snacks page 
thank you page

---
## [Rebirth-of-the-Night/Rebirth-Of-The-Night](https://github.com/Rebirth-of-the-Night/Rebirth-Of-The-Night)@[dd95fcd885...](https://github.com/Rebirth-of-the-Night/Rebirth-Of-The-Night/commit/dd95fcd885f9f164cfe0fa282d6a23c70af0b182)
#### Thursday 2023-08-10 05:23:42 by Foreck1

I keep crashing... anyway

Custom blocks for Ozy to play with. I know they work, but I keep crashing so I can't properly implement them or take cool screenshots for my hecking Midnight no-context teaser 25 which is really making me lose my mind. I had a migraine, and after todays weird internal affairs, I was supposed to go to bed with a hot-water bottle at 22:00 after having watched cute animal videos on youtube because it's 8ºC here (46ºF), but it's now 1:20 and the headache went away before I could enjoy a warm bed and I already forgot the cute animals. Only dissatisfaction and lack of closure remains.

Anyways:
-Chandelier thing
-Bowl (should look cool on a table with turkey)
-Paper: 1,2, and 3 (add to the aforementioned table)

---
## [lessthnthree/tgstation](https://github.com/lessthnthree/tgstation)@[3af26df8ca...](https://github.com/lessthnthree/tgstation/commit/3af26df8cacc24ab7ccacdfbe61005a165472e0f)
#### Thursday 2023-08-10 07:59:04 by GoldenAlpharex

Fixes bloody soles making jumpsuits that cover your feet bloody when you're wearing shoes (#77077)

## About The Pull Request
Title says it all.

It basically made it so wearing something like a kilt would result in
the kilt getting all bloody as soon as you walked over blood, even when
you were wearing shoes, unless you wore something else that obscured
shoes.

I debated with myself a lot over the implementation for this, I was
thinking of adding some way to obscure feet in particular, but it's
honestly so niche that it could only have caused more issues elsewhere
if I tried to fix this issue that way.

---
## [luoxz-ai/MegaMocapVR](https://github.com/luoxz-ai/MegaMocapVR)@[db1481129a...](https://github.com/luoxz-ai/MegaMocapVR/commit/db1481129a211d646ef05bc71636a10d4b89ed52)
#### Thursday 2023-08-10 08:05:21 by Megasteakman

UE5.1.1 - Calibration Mode Overlay

Added a nice new UI overlay to let you know that you are in Calibration Mode after hearing some people get confused about what happens when you first start the system.  If you don't like it, disconnect it in the function for VRPlayerMode_CalibrationMode.

Did a lot of work on the UE5 Manny control rig.  It could be better.  It could be worse.  I find it really hard to tell sometimes, so I did leave the old one in MegaMocapVR\ControlRigs\WIP_ControlRigs\OLD_MMVR_UE5Manny_ControlRig

The UE5 Manny control rig now has a way to lock the arm goals to the chest control, so you can use it for animation/cleanup a bit easier.  This variable is exposed to cinematics, which is a sick feature I want to make more use out of.

I reduced the tick on the editor utility widget.

Revamped the teleprompter, creating a new Teleprompter Screen actor that gets spawned in if you use the new event on the player pawn 'Event_TeleprompterUpdate.

Did some small changes to the metahuman control rig, but... I don't remember what they were.  Again, who knows if its better.  I think I made an 'is valid' check on the iphone name so it wouldn't throw you errors if no iphone was added to the player pawn.

---
## [Techyte/Mythrail](https://github.com/Techyte/Mythrail)@[b25e817d91...](https://github.com/Techyte/Mythrail/commit/b25e817d9104ee72e81d6877d3da27bb9c966d37)
#### Thursday 2023-08-10 10:45:13 by Techyte

Fixed not being able to move

It was only when you joined the second time because unity's OnSceneLoaded system kinda sucks if you want to assign things during it, also it seems to sometimes be run twice. Anyway moral of the story for future me is DONT USER SceneManager.OnSceneLoaded!!!!!!!!!!

---
## [ericliu515515/MathNotic](https://github.com/ericliu515515/MathNotic)@[68f10b445d...](https://github.com/ericliu515515/MathNotic/commit/68f10b445d01d643efb1cf5ecc129213bef6f17d)
#### Thursday 2023-08-10 10:45:57 by eric liuuuuuuuu

The last property is more complicated than I thought, although today I can not wotk much because I spent necesseary time with my girlfriend in the morning and I did't wake up early since last night I stay up late for a date, and I have a haircut today, but today I do make some progress, and I will say is a lot of progress.

---
## [afirpo/tgstation](https://github.com/afirpo/tgstation)@[66b8748091...](https://github.com/afirpo/tgstation/commit/66b87480915434f1184ac257c9ed0f1f3fe87c58)
#### Thursday 2023-08-10 10:52:46 by carlarctg

Adds Summon Simians & Buffs/QoLs Mutate (#77196)

## About The Pull Request

Adds Summon Simians, a spell that summons four monkeys or lesser
gorillas, with the amount increasing per upgrade. The monkeys have
various fun gear depending on how lucky you get and how leveled the
spell is. If the spell is maximum level, it only summons normal
gorillas.

Added further support for nonhuman robed casting: Monkeys, cyborgs, and
drones can all now cast robed spells as long as they're wearing a
wizardly hat as well.

Made monkeys able to wield things again.

Wizard Mutate spell works on non-human races. It also gives you
Gigantism now (funny). If the Race can't support tinted bodyparts, your
whole sprite is temporarily turned green.

Made Laser eyes projectiles a subtype of actual lasers, which has
various properties such as on-hit effects and upping the damage to 30.

Improved some monkey AI code.

## Why It's Good For The Game

> Adds Summon Simians, a spell that summons four monkeys or lesser
gorillas, with the amount increasing per upgrade. The monkeys have
various fun gear depending on how lucky you get and how leveled the
spell is. If the spell is maximum level, it only summons normal
gorillas.

It's criminal we don't have a monky spell, and this is a really fun spin
on it. Total chaos, but total monky chaos. It's surprisingly strong,
but! it can very well backfire if you stay near the angry monkeys too
long and your protection fades away. Unless you become a monkey
yourself!!

> Wizard Mutate spell works on non-human races. 

This spell is great but it's hampered by the mutation's human
requirement, which is reasonable in normal gameplay. Wizards don't need
to care about that, and the human restriction hinders a lot of possible
gimmicks, so off it goes. Also, wizard hulk does't cause chunky fingers
for similar reasons

> Made Laser eyes projectiles a subtype of actual lasers, which has
various properties such as on-hit effects and upping the damage to 30.

Don't really caer about the damage so much, this is more so that it has
effects such as on-hit visuals. Can lower the damage if required, but
honestly anything that competes against troll mjolnir is good.

> Added further support for nonhuman robed casting: Monkeys, cyborgs,
and drones can all now cast robed spells as long as they're wearing a
wizardly hat as well.

SS13 is known for 'The Dev Team Thinks of Everything' and I believe this
is a sorely lacking part of this or something. It's funny.
I want to see a monkey wizard.

> Made monkeys able to wield things again.

I really don't know why this was a thing and it was breaking my axe and
spear wielding primal monkeys. Like, why?

## Changelog

:cl:
add: Adds Summon Simians, a spell that summons four monkeys or lesser
gorillas, with the amount increasing per upgrade. The monkeys have
various fun gear depending on how lucky you get and how leveled the
spell is. If the spell is maximum level, it only summons normal
gorillas.
balance: Wizard Mutate spell works on non-human races. It also gives you
Gigantism now (funny). If the Race can't support tinted bodyparts, your
whole sprite is temporarily turned green.
balance: Made Laser eyes projectiles a subtype of actual lasers, which
has various properties such as on-hit effects and upping the damage to
30.
add: Added further support for nonhuman robed casting: Monkeys, cyborgs,
and drones can all now cast robed spells as long as they're wearing a
wizardly hat as well.
balance: Made monkeys able to wield two-handed things again.
/:cl:

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [afirpo/tgstation](https://github.com/afirpo/tgstation)@[87f707dfa8...](https://github.com/afirpo/tgstation/commit/87f707dfa8dd901310f72585c6f701035bc653ee)
#### Thursday 2023-08-10 10:52:46 by DeerJesus

Adds the Storage Implanter to the spy kit. (#77452)

## About The Pull Request

Adds the storage implanter to the spy kit to make it decent.

## Why It's Good For The Game
This PR hopes to bring Spy at least a little more in-line with the rest
of the syndie-kit specials, so it doesn’t feel like a complete dud to
get.

Spy absolutely sucks as a syndie-kit and getting it is basically
throwing away 20 TC. Not all of them should be equally powerful but all
of them should be at least more satisfying to get. Spy is so bad that
it’s listed in the official wiki as ‘honestly not that good’. It’s also
_barely_ even above 25 telecrystals as the switchblade is a black market
uplink item, not a syndicate uplink item, and not even that good of an
item at that! And the chameleon kit inside isn’t even a full chameleon
kit! Pitiful. Compare it to stealth right below it which totals to _36_
telecrystals.

Adding a storage implant adds a relatively useful item to the kit that
still fits with the entire theme of ‘stealth and deception’, as you can
be searched without having anything on you. To be stealthy, and deceive
people. Like you should. Given the fact that searches are quite common.
It doesn’t make it TOO overpowered as the rest of the gear is still ‘not
that great’.


## Changelog

:cl:
balance: added the storage implanter to the syndie-kit tactical 'spy'
kit to make it decent.
/:cl:

Co-authored-by: oilysnake <63020759+oilysnake@users.noreply.github.com>

---
## [krzk/linux](https://github.com/krzk/linux)@[08c6b43df2...](https://github.com/krzk/linux/commit/08c6b43df24961c6aa80a1ffc7a8653a4905329d)
#### Thursday 2023-08-10 11:22:15 by David Hildenbrand

smaps: use vm_normal_page_pmd() instead of follow_trans_huge_pmd()

We shouldn't be using a GUP-internal helper if it can be avoided.

Similar to smaps_pte_entry() that uses vm_normal_page(), let's use
vm_normal_page_pmd() that similarly refuses to return the huge zeropage.

In contrast to follow_trans_huge_pmd(), vm_normal_page_pmd():

(1) Will always return the head page, not a tail page of a THP.

 If we'd ever call smaps_account with a tail page while setting "compound
 = true", we could be in trouble, because smaps_account() would look at
 the memmap of unrelated pages.

 If we're unlucky, that memmap does not exist at all. Before we removed
 PG_doublemap, we could have triggered something similar as in
 commit 24d7275ce279 ("fs/proc: task_mmu.c: don't read mapcount for
 migration entry").

 This can theoretically happen ever since commit ff9f47f6f00c ("mm: proc:
 smaps_rollup: do not stall write attempts on mmap_lock"):

  (a) We're in show_smaps_rollup() and processed a VMA
  (b) We release the mmap lock in show_smaps_rollup() because it is
      contended
  (c) We merged that VMA with another VMA
  (d) We collapsed a THP in that merged VMA at that position

 If the end address of the original VMA falls into the middle of a THP
 area, we would call smap_gather_stats() with a start address that falls
 into a PMD-mapped THP. It's probably very rare to trigger when not
 really forced.

(2) Will succeed on a is_pci_p2pdma_page(), like vm_normal_page()

 Treat such PMDs here just like smaps_pte_entry() would treat such PTEs.
 If such pages would be anonymous, we most certainly would want to
 account them.

(3) Will skip over pmd_devmap(), like vm_normal_page() for pte_devmap()

 As noted in vm_normal_page(), that is only for handling legacy ZONE_DEVICE
 pages. So just like smaps_pte_entry(), we'll now also ignore such PMD
 entries.

 Especially, follow_pmd_mask() never ends up calling
 follow_trans_huge_pmd() on pmd_devmap(). Instead it calls
 follow_devmap_pmd() -- which will fail if neither FOLL_GET nor FOLL_PIN
 is set.

 So skipping pmd_devmap() pages seems to be the right thing to do.

(4) Will properly handle VM_MIXEDMAP/VM_PFNMAP, like vm_normal_page()

 We won't be returning a memmap that should be ignored by core-mm, or
 worse, a memmap that does not even exist. Note that while
 walk_page_range() will skip VM_PFNMAP mappings, walk_page_vma() won't.

 Most probably this case doesn't currently really happen on the PMD level,
 otherwise we'd already be able to trigger kernel crashes when reading
 smaps / smaps_rollup.

So most probably only (1) is relevant in practice as of now, but could only
cause trouble in extreme corner cases.

Let's move follow_trans_huge_pmd() to mm/internal.h to discourage future
reuse in wrong context.

Link: https://lkml.kernel.org/r/20230803143208.383663-3-david@redhat.com
Fixes: ff9f47f6f00c ("mm: proc: smaps_rollup: do not stall write attempts on mmap_lock")
Signed-off-by: David Hildenbrand <david@redhat.com>
Acked-by: Mel Gorman <mgorman@techsingularity.net>
Cc: Hugh Dickins <hughd@google.com>
Cc: Jason Gunthorpe <jgg@ziepe.ca>
Cc: John Hubbard <jhubbard@nvidia.com>
Cc: Linus Torvalds <torvalds@linux-foundation.org>
Cc: liubo <liubo254@huawei.com>
Cc: Matthew Wilcox (Oracle) <willy@infradead.org>
Cc: Mel Gorman <mgorman@suse.de>
Cc: Paolo Bonzini <pbonzini@redhat.com>
Cc: Peter Xu <peterx@redhat.com>
Cc: Shuah Khan <shuah@kernel.org>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[385ab7a166...](https://github.com/tgstation/tgstation/commit/385ab7a1667250947d480725949bec924ce4ac8a)
#### Thursday 2023-08-10 11:36:34 by Pickle-Coding

Changeling armblade gets 35% armour penetration + better wounding. (#77416)

## About The Pull Request
Gives the changeling armblade an armour penetration of 35%. Sets their
bare_wound_bonus to 10 (from 20), and a wound_bonus of 10 (from -20).
## Why It's Good For The Game
The wound bonuses basically gave massive punishment if they attacked
anything but the skin. It honestly felt kinda lame. The better wounding
potential will help bring a bloodier and more exciting atmosphere when a
changeling whips out the blade.

The armour penetration will help reduce dragged out fights that get a
little silly, while keeping the wounding more consistent.
## Changelog
:cl:
balance: Changeling arm blade has an armour penetration of 35%.
balance: Changeling arm blade has a wound bonus of 10, from -20.
balance: Changeling has a bare wound bonus of 10, from 20.
/:cl:

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[38235dce1d...](https://github.com/tgstation/tgstation/commit/38235dce1d1644be32d1758dcc18734a17e61b1d)
#### Thursday 2023-08-10 11:39:26 by carlarctg

Drill module automatically disables if it's about to drill into gibtonite (#77385)

## About The Pull Request

Drill module automatically disables if it's about to drill into
gibtonite.

## Why It's Good For The Game

> Drill module automatically disables if it's about to drill into
gibtonite

There's not enough time to react, the mining scanner is surprisingly
slow sometimes and it means you drill straight into gibtonite, which
primes it the first drill and blows it up the second, which is a lot
more of a pain than it sounds because drilling is night-instant. These
explosions are usually enough to crit you, and if they don't, the stun
and area clear means any fauna can wander in and finish you off.

The auto-disable still makes it an annoyance to stumble upon gibtonite,
but it won't round end you for using modsuits.

## Changelog

:cl:
qol: Drill module automatically disables if it's about to drill into
gibtonite
/:cl:

---
## [payday-restoration/restoration-mod](https://github.com/payday-restoration/restoration-mod)@[617bf4c68a...](https://github.com/payday-restoration/restoration-mod/commit/617bf4c68ac88bf2d0059f6353ab916187cd695f)
#### Thursday 2023-08-10 12:10:45 by Hater-mater

Fuck you, Bail

Disable garage escape on Hox Revenge

---
## [Erol509/Skyrat-tg](https://github.com/Erol509/Skyrat-tg)@[4537b1e980...](https://github.com/Erol509/Skyrat-tg/commit/4537b1e980f226f2f6a18ef1c92d6ffc3e3b6ac4)
#### Thursday 2023-08-10 12:18:22 by Bloop

[MISSED MIRROR] New space ambient track (#76547) (#22449)

New space ambient track (#76547)

## About The Pull Request

Adds a new space ambient track made by me to the game, supposed to be a
bit scarier than the others that were recently added as I feel that
they're a bit too happy (not to diss I really like them), also cleaned
up a bit of ambience.dm as the medical portion of it didn't follow the
same rules as the other ones. also also this will only be used for
tgstation so license wise I think this is CC BY-SA 3.0 but I'm not sure
so correct me if I'm wrong, also this is my first PR so yeah. Here's a
link to listen to the track https://voca.ro/18WvrGORDDdR

## Why It's Good For The Game

Variety is the spice of life.

## Changelog

:cl:
sound: A new ambient track will now play in space
/:cl:

Co-authored-by: atlasle <132299254+atlasle@users.noreply.github.com>

---
## [norov/linux](https://github.com/norov/linux)@[4f0cb6db7c...](https://github.com/norov/linux/commit/4f0cb6db7c99d800fa525a4a9806f9710c8ddc21)
#### Thursday 2023-08-10 12:24:17 by Yury Norov

sched/topology: add for_each_numa_{,online}_cpu() macro

for_each_cpu() is widely used in the kernel, and it's beneficial to
create a NUMA-aware version of the macro to improve on node locality..

Recently added for_each_numa_hop_mask() works, but switching existing
codebase to using it is not an easy process.

New for_each_numa_cpu() is designed to be similar to the for_each_cpu().
It allows to convert existing code to NUMA-aware as simple as adding a
hop iterator variable and passing it inside new macro. for_each_numa_cpu()
takes care of the rest.

At the moment, we have 2 users of NUMA-aware enumerators. One is
Melanox's in-tree driver, and another is Intel's in-review driver:

https://lore.kernel.org/lkml/20230216145455.661709-1-pawel.chmielewski@intel.com/

Both real-life examples follow the same pattern:

	for_each_numa_hop_mask(cpus, prev, node) {
 		for_each_cpu_andnot(cpu, cpus, prev) {
 			if (cnt++ == max_num)
 				goto out;
 			do_something(cpu);
 		}
		prev = cpus;
 	}

With the new macro, it would look like this:

	for_each_numa_online_cpu(cpu, hop, node) {
		if (cnt++ == max_num)
			break;
		do_something(cpu);
 	}

Straight conversion of existing for_each_cpu() codebase to NUMA-aware
version with for_each_numa_hop_mask() is difficult because it doesn't
take a user-provided cpu mask, and eventually ends up with open-coded
double loop. With for_each_numa_cpu() it shouldn't be a brainteaser.
Consider the NUMA-ignorant example:

	cpumask_t cpus = get_mask();
	int cnt = 0, cpu;

	for_each_cpu(cpu, cpus) {
		if (cnt++ == max_num)
			break;
		do_something(cpu);
 	}

Converting it to NUMA-aware version would be as simple as:

	cpumask_t cpus = get_mask();
	int node = get_node();
	int cnt = 0, hop, cpu;

	rcu_read_lock();
	for_each_numa_cpu(cpu, hop, node, cpus) {
		if (cnt++ == max_num)
			break;
		do_something(cpu);
 	}
	rcu_read_unlock();

The latter looks more verbose and avoids from open-coding that annoying
double loop. Another advantage is that it works with a 'hop' parameter with
the clear meaning of NUMA distance, and doesn't make people not familiar
to enumerator internals bothering with current and previous masks machinery.

Signed-off-by: Yury Norov <yury.norov@gmail.com>

---
## [mamehaze/mame](https://github.com/mamehaze/mame)@[e97630981c...](https://github.com/mamehaze/mame/commit/e97630981c406ba446e2d7fb1bf8ecf8d3a6b93b)
#### Thursday 2023-08-10 12:25:27 by A-Noid33

Added software list for cracked Macintosh floppy images. (#11454)

New working software list items (mac_flop_orig.xml)
-------------------------------
Alter Ego (male version 1.0) (san inc crack) [4am, san inc, A-Noid]
Alter Ego (version 1.1 female) (san inc crack) [4am, san inc, A-Noid]
Alternate Reality: The City (version 3.0) (san inc crack) [4am, san inc, A-Noid]
Animation Toolkit I: The Players (version 1.0) (4am crack) [4am, A-Noid]
Balance of Power (version 1.03) (san inc crack) [4am, san inc, A-Noid]
Borrowed Time (san inc crack) [4am, san inc, A-Noid]
Championship Star League Baseball (san inc crack) [4am, san inc, A-Noid]
Cutthroats (release 23 / 840809-C) (4am crack) [4am, A-Noid]
CX Base 500 (French, version 1.1) (san inc crack) [4am, san inc, A-Noid]
Deadline (release 27 / 831005-C) (4am crack) [4am, A-Noid]
Defender of the Crown (san inc crack) [4am, san inc, A-Noid]
Deluxe Music Construction Set (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Déjà Vu (version 2.3) (4am crack) [4am, A-Noid]
Déjà Vu: A Nightmare Comes True!! (san inc crack) [4am, san inc, A-Noid]
Déjà Vu II: Lost in Las Vegas!! (san inc crack) [4am, san inc, A-Noid]
Dollars and Sense (version 1.3) (4am crack) [4am, A-Noid]
Downhill Racer (san inc crack) [4am, san inc, A-Noid]
Dragonworld (4am crack) [4am, A-Noid]
ExperLisp (version 1.0) (4am crack) [4am, A-Noid]
Forbidden Castle (san inc crack) [4am, san inc, A-Noid]
Fusillade (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Geometry (version 1.1) (4am crack) [4am, A-Noid]
Habadex (version 1.1) (4am crack) [4am, A-Noid]
Hacker II (san inc crack) [4am, san inc, A-Noid]
Harrier Strike Mission (san inc crack) [4am, san inc, A-Noid]
Indiana Jones and the Revenge of the Ancients (san inc crack) [4am, san inc, A-Noid]
Infidel (release 22 / 840522-C) (4am crack) [4am, A-Noid]
Jam Session (version 1.0) (4am crack) [4am, A-Noid]
Legends of the Lost Realm I: The Gathering of Heroes (version 2.0) (4am crack) [4am, A-Noid]
Lode Runner (version 1.0) (4am crack) [4am, A-Noid]
Mac Pro Football (version 1.0) (san inc crack) [4am, san inc, A-Noid]
MacBackup (version 2.6) (4am crack) [4am, A-Noid]
MacCheckers and Reversi (4am crack) [4am, A-Noid]
MacCopy (version 1.1) (4am crack) [4am, A-Noid]
MacGammon! (version 1.0) (4am crack) [4am, A-Noid]
MacGolf (version 2.0) (4am crack) [4am, A-Noid]
MacWars (san inc crack) [4am, san inc, A-Noid]
Master Tracks Pro (version 1.10) (san inc crack) [4am, san inc, A-Noid]
Master Tracks Pro (version 2.00h) (san inc crack) [4am, san inc, A-Noid]
Master Tracks Pro (version 3.4a) (san inc crack) [4am, san inc, A-Noid]
Master Tracks Pro (version 4.0) (san inc crack) [4am, san inc, A-Noid]
Math Blaster (version 1.0) (4am crack) [4am, A-Noid]
Maze Survival (san inc crack) [4am, san inc, A-Noid]
Microsoft Excel (version 1.00) (san inc crack) [4am, san inc, A-Noid]
Microsoft File (version 1.04) (san inc crack) [4am, san inc, A-Noid]
Mindshadow (san inc crack) [4am, san inc, A-Noid]
Moriarty's Revenge (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Moriarty's Revenge (version 1.03) (4am crack) [4am, A-Noid]
Mouse Stampede (version 1.00) (4am crack) [4am, A-Noid]
Murder by the Dozen (Thunder Mountain) (4am crack) [4am, A-Noid]
My Office (version 2.7) (4am crack) [4am, A-Noid]
One on One (san inc crack) [4am, san inc, A-Noid]
Orb Quest: Part I: The Search for Seven Wards (version 1.04) (san inc crack) [4am, san inc, A-Noid]
Patton Strikes Back (version 1.00) (san inc crack) [4am, san inc, A-Noid]
Patton vs. Rommel (version 1.05) (san inc crack) [4am, san inc, A-Noid]
Pensate (version 1.1) (4am crack) [4am, A-Noid]
PFS File and Report (version A.00) (4am crack) [4am, A-Noid]
Physics (version 1.0) (4am crack) [4am, A-Noid]
Physics (version 1.2) (4am crack) [4am, A-Noid]
Pinball Construction Set (version 2.5) (san inc crack) [4am, san inc, A-Noid]
Pipe Dream (version 1.2) (4am crack) [4am, A-Noid]
Professional Composer (version 2.3Mfx) (san inc crack) [4am, san inc, A-Noid]
Q-Sheet (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Rambo: First Blood Part II (san inc crack) [4am, san inc, A-Noid]
Reader Rabbit (version 2.0) (4am crack) [4am, A-Noid]
Rogue (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Seastalker (release 15 / 840522-C) (4am crack) [4am, A-Noid]
Seven Cities of Gold (san inc crack) [4am, san inc, A-Noid]
Shadowgate (san inc crack) [4am, san inc, A-Noid]
Shanghai (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Shufflepuck Cafe (version 1.0) (4am crack) [4am, A-Noid]
Sierra Championship Boxing (4am crack) [4am, A-Noid]
SimCity (version 1.1) (4am crack) [4am, A-Noid]
SimCity (version 1.2, black & white) (4am crack) [4am, A-Noid]
SimEarth (version 1.0) (4am crack) [4am, A-Noid]
Skyfox (san inc crack) [4am, san inc, A-Noid]
Smash Hit Racquetball (version 1.01) (san inc crack) [4am, san inc, A-Noid]
SmoothTalker (version 1.0) (4am crack) [4am, A-Noid]
Speed Reader II (version 1.1) (4am crack) [4am, A-Noid]
Speller Bee (version 1.1) (4am crack) [4am, A-Noid]
Star Trek: The Kobayashi Alternative (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Stratego (version 1.0) (4am crack) [4am, A-Noid]
Suspect (release 14 / 841005-C) (4am crack) [4am, A-Noid]
Tass Times in Tonetown (san inc crack) [4am, san inc, A-Noid]
Temple of Apshai Trilogy (version 1985-09-30) (san inc crack) [4am, san inc, A-Noid]
Temple of Apshai Trilogy (version 1985-10-08) (san inc crack) [4am, san inc, A-Noid]
The Chessmaster 2000 (version 1.02) (4am crack) [4am, A-Noid]
The Crimson Crown (san inc crack) [4am, san inc, A-Noid]
The Duel: Test Drive II (san inc crack) [4am, san inc, A-Noid]
The Hitchhiker's Guide to the Galaxy (release 47 / 840914-C) (4am crack) [4am, A-Noid]
The King of Chicago (san inc crack) [4am, san inc, A-Noid]
The Lüscher Profile (san inc crack) [4am, san inc, A-Noid]
The Mind Prober (version 1.0) (san inc crack) [4am, san inc, A-Noid]
The Mist (san inc crack) [4am, san inc, A-Noid]
The Quest (4am crack) [4am, A-Noid]
The Slide Show Magician (version 1.2) (4am crack) [4am, A-Noid]
The Surgeon (version 1.5) (san inc crack) [4am, san inc, A-Noid]
The Toy Shop (version 1.1) (san inc crack) [4am, san inc, A-Noid]
The Witness (release 22 / 840924-C) (4am crack) [4am, A-Noid]
ThinkTank 128 (version 1.000) (4am crack) [4am, A-Noid]
Uninvited (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Uninvited (version 2.1D1) (san inc crack) [4am, san inc, A-Noid]
Where in Europe is Carmen Sandiego? (version 1.0) (4am crack) [4am, A-Noid]
Winter Games (version 1985-10-24) (san inc crack) [4am, san inc, A-Noid]
Winter Games (version 1985-10-31) (san inc crack) [4am, san inc, A-Noid]
Wishbringer (release 68 / 850501-D) (4am crack) [4am, A-Noid]
Wizardry: Proving Grounds of the Mad Overlord (version 1.10) (san inc crack) [4am, san inc, A-Noid]
Zork II (release 48 / 840904-C) (4am crack) [4am, A-Noid]
Zork III (release 17 / 840727-C) (4am crack) [4am, A-Noid]

---
## [SPSquonK/useleSS](https://github.com/SPSquonK/useleSS)@[2e56d3cc08...](https://github.com/SPSquonK/useleSS/commit/2e56d3cc08860616093af4a9e8d21a28bf3719f3)
#### Thursday 2023-08-10 12:33:27 by SquonK

Remove ShadowMask

One day, a distinguished woman said something like

"You better start making sens you rotten code, or you're gonna
be sorry. Maybe I'll rip your lines out one by one, or maybe
I'll put you in the godamn bin.
How can something with such a big longetivity can contain
so much useless classes huh? Oh ShadowMask, I love you ShadowMask.
Come over and give the code a big sloppy kiss, ShadowMask."

---
## [Tangerineje/PsychonautStation](https://github.com/Tangerineje/PsychonautStation)@[755fa4db6d...](https://github.com/Tangerineje/PsychonautStation/commit/755fa4db6d5c811770188c340cd2ccb85469d505)
#### Thursday 2023-08-10 13:19:28 by san7890

Loads Away Missions for Unit Testing (#76245)

## About The Pull Request

Hey there,

A pretty bad bug (#76226) got through, but it was fixed pretty quickly
in #76241 (cf92862daf339e97c76b52c91f31d49ba5113bd4). I realized that if
we were testing all the away missions, that this could theoretically get
caught and not happen again. Regardless, unit testing gateway missions
has been on my to-do list for a while now, and I finally got it nailed
down.

Basically, we just have a really small "station" map with the bare bones
(_teeny_ bit of fluff, maploading is going to take 30 seconds tops
anyways let me have my kicks) with a JSON map datum flag that causes it
to load all away missions in the codebase (which are all in one folder).
Just in case some admins were planning on invoking the proc on
`SSmapping`, I also decided to gate a `tgui_alert()` behind it because
you never can be too sure of what people think is funny these days (it
really does lock up your game for a second or so at a time).

I also alphabetized the maps.txt config because that was annoying me.
## Why It's Good For The Game

Things that break on production could(?) be caught in unit testing? I
don't know if the linked issue I mentioned above would have been caught
in retrospect, but it's likely to catch more than a few upcoming bugs
(like the UO45 atmospherics thing at the very top) and ensure that these
gateway missions, which tend to be the most neglected part of mapping,
stay bug-free.

This is also helpful in case someone makes a new away mission and wants
to see if stuff's broken. Helps out maptainers a bit because very, very
technically broken mapping will throw up runtimes. Neato.
## Changelog
Nothing that players should be concerned about.

Let me know if there's a better way to approach this, but I really think
that having a super-duper light map with the bare basics to load up
gateway missions and then all nine-ish gateway missions can sequentially
load during init. I can't think of a better way to do it aside from some
really ugly `#ifdef` shit. Also also, it has the added benefit of being
a map that will always load your away mission without touching a single
shred of config (and it's not likely to break if you follow sane
practices such as making your own areas)

---
## [Tangerineje/PsychonautStation](https://github.com/Tangerineje/PsychonautStation)@[48cc57010d...](https://github.com/Tangerineje/PsychonautStation/commit/48cc57010d3ff01c55c53131b9399a4e71656d8d)
#### Thursday 2023-08-10 13:19:28 by Jacquerel

Various spider fixes (#76528)

## About The Pull Request

Fixes #76484
Then I noticed some weird stuff which slipped through the PR and poked
at that too.

- Spiderlings and Spiders once more have names ending in (###)
- Removed an unused property on Spiderlings.
- Rewrote the descriptions for a bunch of web-abilities and web-objects
to be clearer and have better capitalisation.
- Refactored the "Web Carcass" ability to not extend from "lay web" as
it didn't need to perform most of that behaviour.
- Also I renamed it and made the description give you a hint about why
you would want to instantly spawn a statue.
- The web effigy now despawns at the same rate as the ability cools down
so you're not dumping spider statues all over the place.
- I made spiderlings move at about the same speed as humans except if
they're on webs in which case they're still pretty fast.

To be honest I am not certain an instant statue spawning button is great
to begin with and I didn't even know it was added to the game but I am
not interested in messing much with the balance for now.

This made me look at spiderlings enough that I'm going to try and make a
new sprite for them that isn't awful.

## Why It's Good For The Game

Lets you differentiate individual spiders a little bit.
Makes usage of abilities clearer.

## Changelog

:cl:
balance: Guard spider web statues despawn as the ability comes back off
cooldown.
balance: Spiderlings now only move at light speed if they're on webs,
stay safe little guys.
fix: Spiders once again have random numbers after their names.
/:cl:

---
## [FaBrand/rules_rust](https://github.com/FaBrand/rules_rust)@[80f0eb488a...](https://github.com/FaBrand/rules_rust/commit/80f0eb488ab9cabc4920ac446478cbf2feedc3f3)
#### Thursday 2023-08-10 13:33:54 by scentini

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
## [vampirebat74/lobotomy-corp13](https://github.com/vampirebat74/lobotomy-corp13)@[31d09de099...](https://github.com/vampirebat74/lobotomy-corp13/commit/31d09de099fabc169e566f10e0a8f1ba7033cb9a)
#### Thursday 2023-08-10 13:36:05 by Mr.Heavenly

Adds Red Shoes

Mr. Heavenly's Abnormality Jam Entry #1

Records

uncommented weapon

Finishing touches

Design rework

adds ego gift and inhands

New sprites!

uncommented sfx

insanity fix

quieter sound loop

Fixes some shit

fix linters

requested changes

---
## [Sealed101/tgstation](https://github.com/Sealed101/tgstation)@[4e91d057d7...](https://github.com/Sealed101/tgstation/commit/4e91d057d7d627bd8c356a2251195eb579106707)
#### Thursday 2023-08-10 13:43:43 by MrMelbert

Adds a wizard Right and Wrong that lets the caster give one spell (or relic) to everyone on the station (#76974)

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

---
## [realforest2001/forest-cm13](https://github.com/realforest2001/forest-cm13)@[3e9d54628d...](https://github.com/realforest2001/forest-cm13/commit/3e9d54628d68fe91319ae87ad7ebd7aef9500811)
#### Thursday 2023-08-10 14:16:25 by Ben

Can no longer bypass Lesser Drone Limit (#4034)

# About the pull request

Users can no longer keep menu open and bypass lesser drone slots

# Explain why it's good for the game

Honestly kinda wish I didn't make this one, infinite lesser drones
sounds really funny.

# Changelog
:cl:
fix: You can no longer circumvent the lesser drone limit by keeping the
prompt open.
/:cl:

---
## [mohammadanasalam/ASSINGMENTS-PYTHON](https://github.com/mohammadanasalam/ASSINGMENTS-PYTHON)@[4b595c533f...](https://github.com/mohammadanasalam/ASSINGMENTS-PYTHON/commit/4b595c533fbb4aa41e7ff08d3bd1cab74e0ade23)
#### Thursday 2023-08-10 15:30:14 by mohammadanasalam

Questions

Q1. Create a function which will take a list as an argument and return the product of all the numbers
after creating a flat list.
Use the below-given list as an argument for your function.
list1 = [1,2,3,4, [44,55,66, True], False, (34,56,78,89,34), {1,2,3,3,2,1}, {1:34, "key2": [55, 67, 78, 89], 4: (45,
22, 61, 34)}, [56, 'data science'], 'Machine Learning']
Note: you must extract numeric keys and values of the dictionary also.
Q2. Write a python program for encrypting a message sent to you by your friend. The logic of encryption
should be such that, for a the output should be z. For b, the output should be y. For c, the output should
be x respectively. Also, the whitespace should be replaced with a dollar sign. Keep the punctuation
marks unchanged.
Input Sentence: I want to become a Data Scientist.
Encrypt the above input sentence using the program you just created.
Note: Convert the given input sentence into lowercase before encrypting. The final output should be
lowercase.

---
## [RipGrayson/TerraGov-Marine-Corps](https://github.com/RipGrayson/TerraGov-Marine-Corps)@[fb4899d20e...](https://github.com/RipGrayson/TerraGov-Marine-Corps/commit/fb4899d20e990a0a65b8cb5b0ad19b1ef9ab083e)
#### Thursday 2023-08-10 15:34:27 by KM-Catman

Slight redesign of Valhalla Vendors and Chemistry. Adds FC and Synth to Valhalla. (#13612)

* Valhalla Fixes

Start room is now all Hulls, adds a Friend, Materializes the Chaplain's chained demon, and adds more Xeno Huds.

* FC and Synth Added. Slight readjustment.

* Changed the vendor section as per Grayson's request

* Adds three new Warning Stripes.

Adds a FCDR, Synth, and Mech warning stripe. Adds them in front of the prep rooms

* Duct Taped Space

* Removed random bedsheet (Goddamn you hotkeys)

---
## [codecov/codecov-api](https://github.com/codecov/codecov-api)@[4bacedc50c...](https://github.com/codecov/codecov-api/commit/4bacedc50c4c3efebc6d2a23ec8ef3bd0fd416b2)
#### Thursday 2023-08-10 15:56:17 by Gguidini

fix: lru_cache issues + meta info missing

Context: https://github.com/codecov/engineering-team/issues/119

So the real issue with the meta info is fixed in codecov/shared#22.
spoiler: reusing the report details cached values and _changing_ them is not a good idea.

However in the process of debuging that @matt-codecov pointed out that we were not using lru_cache correctly.
Check this very well made video: https://www.youtube.com/watch?v=sVjtp6tGo0g

So the present changes upgrade shared so we fix the meta info stuff AND address the cache issue.
There are further complications with the caching situation, which explain why I decided to add the cached value in the
`obj` instead of `self`. The thing is that there's only 1 instance of `ArchiveField` shared among ALL instances of
the model class (for example, all `ReportDetail` instances). This kinda makes sense because we only create an instance
of `ArchiveField` in the declaration of the `ReportDetail` class.

Because of that if the cache is in the `self` of `ArchiveField` different instances of `ReportDetails` will have dirty cached value of other `ReportDetails` instances and we get wrong values. To fix that I envision 3 possibilities:
1. Putting the cached value in the `ReportDetails` instance directly (the `obj`), and checking for the presence of that value.
If it's there it's guaranteed that we put it there, and we can update it on writes, so that we can always use it. Because it is
for each `ReportDetails` instance we always get the correct value, and it's cleared when the instance is killed and garbage collected.

2. Storing an entire table of cached values in the `self` (`ArchiveField`) and using the appropriate cache value when possible. The problem here is that we need to manage the cache ourselves (which is not that hard, honestly) and probably set a max value. Then we will populate the cache and over time evict old values. The 2nd problem is that the values themselves might be too big to hold in memory (which can be fixed by setting a very small value in the cache size). There's a fine line there, but it's more work than option 1 anyway.

3. We move the getting and parsing of the value to outside `ArchiveField` (so it's a normal function) and use `lru_cache` in that function. Because the `rehydrate` function takes a reference to `obj` I don't think we should pass that, so the issue here is that we can't cache the rehydrated value, and would have to rehydrate every time (which currently is not expensive at all in any model)

This is an instance cache, so it shouldn't need to be cleaned for the duration of the instance's life
(because it is updates on the SET)

closes codecov/engineering-team#119

---
## [jsboige/semantic-kernel](https://github.com/jsboige/semantic-kernel)@[2733a5574f...](https://github.com/jsboige/semantic-kernel/commit/2733a5574f72980413e339f100dbe4272644888c)
#### Thursday 2023-08-10 16:12:09 by Mark Karle

Python: Import OpenAPI documents into the semantic kernel (#2297)

### Motivation and Context

<!-- Thank you for your contribution to the semantic-kernel repo!
Please help reviewers and future users, providing the following
information:
  1. Why is this change required?
  2. What problem does it solve?
  3. What scenario does it contribute to?
  4. If it fixes an open issue, please link to the issue here.
-->

This allows us to import OpenAPI documents, including ChatGPT plugins,
into the Semantic Kernel.

### Description

<!-- Describe your changes, the overall approach, the underlying design.
These notes will help understanding how your code works. Thanks! -->
- The interface reads the operationIds of the openapi spec into a skill:
```python
from semantic_kernel.connectors.openapi import register_openapi_skill
skill = register_openapi_skill(kernel=kernel, skill_name="test", openapi_document="url/or/path/to/openapi.yamlorjson")
skill['operationId'].invoke_async()
```
- Parse an OpenAPI document
- For each operation in the document, create a function that will
execute the operation
- Add all those operations to a skill in the kernel
- Modified `import_skill` to accept a dictionary of functions instead of
just class so that we can import dynamically created functions
- Created unit tests

TESTING:
I've been testing this with the following ChatGPT plugins:
- [Semantic Kernel Starter's Python Flask
plugin](https://github.com/microsoft/semantic-kernel-starters/tree/main/sk-python-flask)
- [ChatGPT's example retrieval
plugin](https://github.com/openai/chatgpt-retrieval-plugin/blob/main/docs/providers/azuresearch/setup.md)
- This one was annoying to setup. I didn't get the plugin functioning,
but I was able to send the right API requests
- Also, their openapi file was invalid. The "servers" attribute is
misindented
- [Google ChatGPT
plugin](https://github.com/Sogody/google-chatgpt-plugin)
- [Chat TODO plugin](https://github.com/lencx/chat-todo-plugin)
- This openapi file is also invalid. I checked with an online validator.
I had to remove"required" from the referenced request objects'
properties:
https://github.com/lencx/chat-todo-plugin/blob/main/openapi.yaml#L85

Then I used this python file to test the examples:

```python
import asyncio
import logging

import semantic_kernel as sk
from semantic_kernel import ContextVariables, Kernel
from semantic_kernel.connectors.ai.open_ai import AzureTextCompletion
from semantic_kernel.connectors.openapi.sk_openapi import register_openapi_skill

# Example usage
chatgpt_retrieval_plugin = {
    "openapi": # location of the plugin's openapi.yaml file,
    "payload": {
        "queries": [
            {
                "query": "string",
                "filter": {
                    "document_id": "string",
                    "source": "email",
                    "source_id": "string",
                    "author": "string",
                    "start_date": "string",
                    "end_date": "string",
                },
                "top_k": 3,
            }
        ]
    },
    "operation_id": "query_query_post",
}

sk_python_flask = {
    "openapi":  # location of the plugin's openapi.yaml file,
    "path_params": {"skill_name": "FunSkill", "function_name": "Joke"},
    "payload": {"input": "dinosaurs"},
    "operation_id": "executeFunction",
}
google_chatgpt_plugin = {
    "openapi":  # location of the plugin's openapi.yaml file,
    "query_params": {"q": "dinosaurs"},
    "operation_id": "searchGet",
}

todo_plugin_add = {
    "openapi":  # location of the plugin's openapi.yaml file,
    "path_params": {"username": "markkarle"},
    "payload": {"todo": "finish this"},
    "operation_id": "addTodo",
}

todo_plugin_get = {
    "openapi":  # location of the plugin's openapi.yaml file,
    "path_params": {"username": "markkarle"},
    "operation_id": "getTodos",
}

todo_plugin_delete = {
    "openapi":  # location of the plugin's openapi.yaml file,
    "path_params": {"username": "markkarle"},
    "payload": {"todo_idx": 0},
    "operation_id": "deleteTodo",
}


plugin = todo_plugin_get # set this to the plugin you want to try

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

kernel = Kernel(log=logger)
deployment, api_key, endpoint = sk.azure_openai_settings_from_dot_env()
kernel.add_text_completion_service(
    "dv", AzureTextCompletion(deployment, endpoint, api_key)
)

skill = register_openapi_skill(
    kernel=kernel, skill_name="test", openapi_document=plugin["openapi"]
)
context_variables = ContextVariables(variables=plugin)
result = asyncio.run(
    skill[plugin["operation_id"]].invoke_async(variables=context_variables)
)
print(result)
```

### Contribution Checklist

<!-- Before submitting this PR, please make sure: -->

- [ ] The code builds clean without any errors or warnings
- [ ] The PR follows the [SK Contribution
Guidelines](https://github.com/microsoft/semantic-kernel/blob/main/CONTRIBUTING.md)
and the [pre-submission formatting
script](https://github.com/microsoft/semantic-kernel/blob/main/CONTRIBUTING.md#development-scripts)
raises no violations
- [ ] All unit tests pass, and I have added new tests where possible
- [ ] I didn't break anyone :smile:

---------

Co-authored-by: Abby Harrison <abharris@microsoft.com>

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[87a7d7f43b...](https://github.com/git-for-windows/git/commit/87a7d7f43b06519833c42b08138ac2b8c6049799)
#### Thursday 2023-08-10 16:12:31 by Johannes Schindelin

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
## [sourcegraph/sourcegraph](https://github.com/sourcegraph/sourcegraph)@[340b0dea25...](https://github.com/sourcegraph/sourcegraph/commit/340b0dea25f073119d0506b8dd3c6228516cf9c4)
#### Thursday 2023-08-10 16:49:04 by David Veszelovszki

JetBrains: Fix dotcom logging issue (#54885)

We didn't convert an object to a string → our Go backend rejected it →
got no logs on Dotcom :bang-head:

Currently, I'm getting back a bunch of 429 – Too Many Requests responses
from Dotcom for some reason, but the problem should be solved.

I feel sorry about losing all those logs, it really sucks. We were too
much in a rush and didn't test this properly. Totally my mistake.

## Test plan

Tested it with the built-in-debugger and by copying the requests to our
GraphQL API console.

---
## [Amerecanno/CoffeStation](https://github.com/Amerecanno/CoffeStation)@[1895bd5c51...](https://github.com/Amerecanno/CoffeStation/commit/1895bd5c511012ac1978d52aea8f6810a90fcf08)
#### Thursday 2023-08-10 16:50:33 by CDB

Im so sick of bugs. (#4739)

* Mother fucker. Im so sick of bugs.

Cigarettes no longer(seem to) cause kidney damage to people with unclean living.

psion void armor has correct slowdown for shoes and doesn't use slowdown on other pieces of armor. Additionally, no longer allows ears to flop outside of it. It's a fucking space suit, why would they be out?

Opifex medbelt no longer selectable, sorry powergamers.

Removes change_appearance from baseline armor vest. Why? It is the parent to MANY MANY MANY fucking items and thus caused MANY MANY MANY items to have erronious change_appearance procs that only had two options for the base parent item. This is why we don't put fucking procs on BASE PARENT items that affect DOZENS of other items. Fixes a few others, WO plate has no unique sprite and now has a proper working change appearance. CO does have a unique sprite, it is gone.

Fixes #4732
Fixes #4734
fixes #4724

* Update psi_Larmor.dm

---
## [VipansinghDA/Maven_Family_Leave_Challenge](https://github.com/VipansinghDA/Maven_Family_Leave_Challenge)@[c5d6901181...](https://github.com/VipansinghDA/Maven_Family_Leave_Challenge/commit/c5d6901181e574affb9d4559b4732b2c0a8f49c7)
#### Thursday 2023-08-10 17:10:11 by Vipan Singh

Add files via upload

#About the Challenge:

At MavenCare, we understand that family matters. The Family Leave Empowerment Challenge encourages participants to prioritize family time while fostering their career growth. This challenge empowers you to take the time you need to bond with your loved ones, recharge, and return to work with renewed energy.

#Key Features:

- Holistic Well-being: Embrace the opportunity to care for yourself and your family. The challenge promotes mental, emotional, and physical well-being through meaningful family interactions and self-care activities.

- Work-Life Integration: Strive for a harmonious balance between your professional aspirations and your role as a family member. We encourage you to set boundaries, communicate your needs, and craft a supportive environment.

- Skill Enrichment: Use your family leave to explore new hobbies, enhance your skills, or embark on personal development projects. This challenge encourages growth on all fronts.

---
## [acornett21/ack-test-infra](https://github.com/acornett21/ack-test-infra)@[95e4857b28...](https://github.com/acornett21/ack-test-infra/commit/95e4857b28122c6c5f8a30260be3dcac94e0e466)
#### Thursday 2023-08-10 17:36:36 by Amine

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
## [Fray2/RU-CMSS13](https://github.com/Fray2/RU-CMSS13)@[f3fc60ed65...](https://github.com/Fray2/RU-CMSS13/commit/f3fc60ed655d27bb3f012d0e0d834c64990b173d)
#### Thursday 2023-08-10 17:50:13 by morrowwolf

Attachment nerfs and removals (#4122)

# About the pull request

This PR:

Removes the barrel charger from vendors

Removes all benefits other than wield delay mod from the angled grip

Adds wield delay to the extended barrel

# Explain why it's good for the game

Barrel charger is a straight damage increase and rather silly to work
around given how burst works bypassing real fire rate concerns. If you
know, you know. Horrible idea, I am amazed it's been around this long.

Angled grip had zero downside. Now it still has zero downside but isn't
also a ton of accuracy buffs on top of the god-tier lower wield delay.

Extended barrel had zero downside. Now it has a downside.

# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog

:cl: Morrow
balance: Removed the barrel charger from vendors
balance: Removed all benefits other than wield delay mod from the angled
grip
balance: Added wield delay to extended barrel
/:cl:

---
## [openai/evals](https://github.com/openai/evals)@[30e35436be...](https://github.com/openai/evals/commit/30e35436be663f416ce6d125f09f92a1faf70d12)
#### Thursday 2023-08-10 18:09:46 by Nazar

Hard russian computer science tasks  (#1323)

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

hard_russian_computer_science_tasks

### Eval description

Challenging computer science problems primarily sourced from Russian
academic and competitive programming contexts. The problems cover
various subfields of computer science, including data structures,
algorithms, computational mathematics, and more.

### What makes this a useful eval?

Russian computer science education and competitive programming are known
for their rigorous and complex problem sets. These problems can be used
to assess an GPT's ability to solve high-level, challenging problems.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [ + ] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [ + ] Contains failures where a human can do the task, but either
GPT-4 or GPT-3.5-Turbo could not.
- [ + ] Includes good signal around what is the right behavior. This
means either a correct answer for `Basic` evals or the `Fact`
Model-graded eval, or an exhaustive rubric for evaluating answers for
the `Criteria` Model-graded eval.
- [ + ] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should

- [ + ] Check that your data is in `evals/registry/data/{name}`
- [ + ] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [ + ] Ensure you have the right to use the data you submit via this
eval

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

- [ + ] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [ + ] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [ + ] I understand that opening a PR, even if it meets the
requirements above, does not guarantee the PR will be merged nor GPT-4
access be granted.

### Submit eval

- [ + ] I have filled out all required fields of this form
- [ + ] I have used **Git LFS** for the Eval JSON data
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `mypy`, `black`,
`isort`, and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "Алёна очень любит алгебру.
Каждый день, заходя на свой любимый алгебраический форум, она с
вероятностью $\\frac14$ находит там новую интересную задачу про группы,
а с вероятностью $\\frac{1}{10}$ интересную задачку про кольца. С
вероятностью $\\frac{13}{20}$ новых задач на форуме не окажется. Пусть
$X$ — это минимальное число дней, за которые у Алёны появится хотя бы
одна новая задача про группы и хотя бы одна про кольца. Найдите
распределение случайной величины $X$. В ответе должны участвовать только
компактные выражения (не содержащие знаков суммирования, многоточий и
пр.)."}], "ideal": "Нам нужно найти $ P[X = k] $. Для этого надо понять
на пальцах, в каком случае $ X = k $. Первый случай — когда в каждый из
предыдущих $ k - 1 $ дней либо не было задач, либо были только про
группы, а в $k$-ый попалась задача про кольца. Второй случай — когда в
каждый из предыдущих $ k - 1 $ дней либо не было задач, либо были только
про кольца, а в $k$-ый попалась задача про группы. На самом деле мы оба
раза учли не подходящий случай, когда все предыдущие $k-1$ дней задач не
было вообще. С поправкой на это ответ будет таким: $P[x=k]=\\left
(\\left (\\frac{13}{20}+\\frac{1}{4}\\right )^{k-1}-\\left
(\\frac{13}{20} \\right )^{k-1}\\right )\\cdot\\frac{1}{10}+\\left
(\\left (\\frac{13}{20}+\\frac{1}{10}\\right )^{k-1}-\\left
(\\frac{13}{20} \\right )^{k-1}\\right )\\cdot\\frac{1}{4}$"}
{"input": [{"role": "system", "content": "В множестве из $n$ человек
каждый может знать или не знать другого (если $A$ знает $B$, отсюда не
следует, что $B$ знает $A$). Все знакомства заданы булевой матрицей
$n×n$. В этом множестве может найтись или не найтись знаменитость —
человек, который никого не знает, но которого знают все. Предложите
алгоритм, который бы находил в множестве знаменитость или говорил, что
ее в этом множестве нет. Сложность по времени — $O(n)$, сложность по
памяти — $O(1)$."}], "ideal": "Для определенности положим
$K_{ij}=\\left\\{\\begin{matrix}1, \\text{если i-й знает j-ого;}
\\\\0\\text{,иначе.}\\end{matrix}\\right.$.\nЗаметим, что если
$K_{ij}=1$, то $i$-ый не может быть знаменитостью, а если $K_{ij}=0$, то
$j$-ый не может быть знаменитостью. Таким образом, за одну проверку
можно исключить одного человека из кандидатов в знаменитости.\nСначала
пусть $s=1$, а $l$ пробегает значения от $22$ до $n$. Если в какой-то
момент $K_{sl}=1$, то приравниваем $s=l$. Тогда значение $s$ после
последней проверки — номер единственного оставшегося кандидата. Чтобы
проверить, является ли этот кандидат знаменитостью, нужно провести еще
$n−1$ проверок, знают ли его остальные, и $n−1$ проверок, знает ли он
остальных. Всего будет проведено $3(n−1)$ проверок, следовательно,
сложность по времени — $O(n)$. Поскольку мы использовали только $2$
переменные, сложность по памяти — $O(1)$."}
{"input": [{"role": "system", "content": "В двумерном полукруге есть n
неизвестных нам точек. Разрешается задавать вопросы вида «каково
расстояние от точки X до ближайшей из этих точек?» Если расстояние
оказывается нулевым, точка считается угаданной. Докажите, что хотя бы
одну из этих точек можно угадать не более чем за $2n+1$ вопрос."}],
"ideal": "Возьмем на диаметре полукруга $n+1$ точку. Точки назовем
$A_1$, $A_2$, … $A_{n+1} и для каждой из них зададим наш вопрос. По
принципу Дирихле, для каких-то двух соседних точек ближайшая точка будет
одна и та же и полученное расстояние было бы до одной и той точки из
множества загаданных точек. Теперь мы рассматриваем точки $B+i$
пересечения окружностей с центрами в точках $A_i$ и $A_{i+1}, $i=1, … ,
n и радиусами равными ответам полученным на предыдущем шаге. По принципу
Дирихле, хотя бы одна из загаданных точек совпадает с одной из точек
$B_i$. Тогда за n вопросов для каждой точки $B_i$ мы получим хотя бы
один ответ 0. Итого нам потребовалось не более (n+1)+n=2n+1 вопросов."}
{"input": [{"role": "system", "content": "В равностороннем треугольнике
$ABC$ площади $1$ выбираем точку $M$. Найти математическое ожидание
площади $ABM$."}], "ideal": "Заметим, что
$M(S_{ABM}+S_{BCM}+S_{CAM})=1$. Тогда из линейности матожидания и
равенства матожиданий площадей треугольников $ABM$, $BCM$ и $CAM$
получим $M(S_{ABM})=\\frac{1}{3}$."}
{"input": [{"role": "system", "content": "Верно ли, что всякая нечетная
непрерывная функция, \nудовлетворяющая условию $f(2x) = 2f(x)$,
линейна."}], "ideal": "Контрпример: $f(x) = x \\cos(2\\pi
\\log_2(|x|))$.\nНеверно."}
{"input": [{"role": "system", "content": "Верно ли, что rank AB = rank
BA для любых квадратных матриц A и B?"}], "ideal": "Пусть
$A=\\begin{pmatrix} 0& 1 \\\\ 1& 0 \\\\ \\end{pmatrix}$, а
$B=\\begin{pmatrix} 1& 0 \\\\ 1& 0 \\\\ \\end{pmatrix}$. Тогда rank AB =
0, но rank BA = 1. Неверно."}
{"input": [{"role": "system", "content":
"Вычислите $\\int_{0}^{2π}(\\sin x)^8dx$."}], "ideal": "Заметим, что
$\\int_{0}^{2\\pi} (\\sin x)^n dx=-\\int_{0}^{2\\pi} (\\sin x)^{n-1}
d(\\cos x)=(n-1)\\int_{0}^{2\\pi} (\\cos x)^2(\\sin x)^{n-2}
dx$.\nИспользуя основное тригонометрическое тождество,
получаем:\n$\\int_{0}^{2\\pi} (\\sin x)^n
dx=\\frac{n-1}{n}\\int_{0}^{2\\pi} (\\sin x)^{n-2}dx$.\nТогда
$\\int_{0}^{2\\pi} (\\sin x)^8 dx=2\\pi
\\prod_{\\substack{k=2\\\\k+=2}}^{8}\\frac{k-1}{k}=\\frac{35\\pi}{64}$."}
{"input": [{"role": "system", "content": "Дан массив из $n$ чисел.
Предложите алгоритм, позволяющий за $O(n)$ операций определить, является
ли этот массив перестановкой чисел от $1$ до $n$. Дополнительной памяти
не более $O(1)$."}], "ideal": "Идея состоит в том, чтобы рассматривать
массив $A$ как подстановку. Пусть индекс $i$ пробегает значения от $0$
до $n−1$. Когда мы встречаем положительный элемент $A[i]$, переходим от
него к элементу $A[A[i]−1]$, от элемента $A[A[i]−1]$ к элементу
$A[A[A[i]−1]−1]$ и так далее, пока мы не не вернемся к $A[i]$, либо не
сможем совершить очередной шаг (в таком случае, массив перестановкой не
является). В процессе меняем знак всех пройденных элементов на
отрицательный. Поскольку на каждом элементе массива мы можем оказаться
максимум два раза, итоговая сложность — $O(n)$. Дополнительная память —
$O(1)$."}
{"input": [{"role": "system", "content": "Дан неориентированный непустой
граф $G$ без петель. Пронумеруем все его вершины. Матрица смежности
графа $G$ с конечным числом вершин $n$ (пронумерованных числами
от 11 до $n$) — это квадратная матрица $A$ размера $n$, в которой
значение элемента $a_{ij}$ равно числу ребер из $i$-й вершины графа
в $j$-ю вершину. Докажите, что матрица $A$ имеет отрицательное
собственное значение."}], "ideal": "Заметим, что $A$ — симметрическая
ненулевая матрица с неотрицательными элементами и нулями на диагонали.
Докажем, что у такой матрицы есть отрицательное собственное
значение.\nИзвестный факт, что симметрическая матрица диагонализуема в
вещественном базисе (все собственные значения вещественны). Допустим,
что все собственные значения $A$ неотрицательны. Рассмотрим квадратичную
форму $q$ с матрицей $A$ в базисе $\\{e1,…,en\\}$. Тогда эта
квадратичная форма неотрицательно определена, так как все собственные
значения неотрицательны. То есть $\\forall v:q(v)⩾0$. С другой стороны,
пусть $a_{ij}≠0$. Тогда $q(e_i−e_j)=a_{ii}−2a_{ij}+a_{jj}=−2a_{ij}<0$.
Это противоречит неотрицательной определенности $q$. Значит, исходное
предположение неверно, и у $A$ есть отрицательное собственное
значение."}
{"input": [{"role": "system", "content": "Дана матрица из нулей и
единиц, причем для каждой строки матрицы верно следующее: если в строке
есть единицы, то они все идут подряд (неразрывной группой из единиц).
Докажите, что определитель такой матрицы может быть равен только $\\pm1$
или $0$."}], "ideal": "Переставляя строки, мы можем добиться того, чтобы
позиции первых (слева) единиц не убывали сверху вниз. При этом
определитель либо не изменится, либо поменяет знак. Если у двух строк
позиции первых единиц совпадают, то вычтем ту, в которой меньше единиц
из той, в которой больше. Определитель при этом не меняется. Такими
операциями мы можем добиться того, что позиции первых единиц строго
возрастают сверху вниз. При этом либо матрица окажется вырожденной, либо
верхнетреугольной с единицами на диагонали. То есть, определитель станет
либо $0$, либо $1$. Так как определитель при наших операциях либо не
менялся, либо поменял знак, изначальный определитель был $\\pm1$ или
$0$."}
  ```
</details>

---
## [broscolotos/Traincraft-5](https://github.com/broscolotos/Traincraft-5)@[013605055d...](https://github.com/broscolotos/Traincraft-5/commit/013605055d1d02e8c70c8be8483811be24f4333c)
#### Thursday 2023-08-10 18:28:18 by broscolotos

omg he did

-Fixed dupe when breaking trains sometimes. Happened because an entity can die twice in a single tick??? dumb game
-Added page memory to the paint bucket GUI; when you open the UI it will default to the entities current skin instead of the default. Maybe add to config later
-Added "Random" button to paint bucket GUI. Will select and apply a random skin out of the available skins.

---
## [Ua-Gi-Oh/UA_EDO](https://github.com/Ua-Gi-Oh/UA_EDO)@[05e12c5938...](https://github.com/Ua-Gi-Oh/UA_EDO/commit/05e12c5938e3b7318a9a6ea5f39b7feb5f16a461)
#### Thursday 2023-08-10 19:03:42 by Ua-Gi-Oh

Перекладено карт

1 - Yoko, the Graceful Mayakashi
2 - Insect Armor with Laser Cannon
3 - Dicephoon
4 - Don Turtle
5 - Appliancer Dryer Drake
6 - Stealth Bird
7 - Coach Soldier Wolfbark
8 - Evilswarm Zahak
9 - Allvain the Essence of Vanity
10 - Dice Jar
11 - White Duston
12 - Latency
13 - Link Back
14 - Swordsman of Landstar
15 - Crystolic Potential
16 - Merlin
17 - Shreddder
18 - One Who Hunts Souls
19 - Gagaga Girl
20 - Endymion, the Mighty Master of Magic
21 - Skull Guardian
22 - Cyber Angel Idaten
23 - Elemental HERO Great Tornado
24 - The Legendary Fisherman
25 - Ally of Justice Searcher
26 - Cyber Valley
27 - Overload Fusion
28 - Knightmare Mermaid
29 - Double Snare
30 - Karakuri Cash Inn

---
## [tagup/streamlit](https://github.com/tagup/streamlit)@[c464422e1b...](https://github.com/tagup/streamlit/commit/c464422e1bbea66b3184769ea22599356d710f9a)
#### Thursday 2023-08-10 19:13:33 by Danny Wolf

Upgrade react-range to fix memory usage of sliders (#6764)

As mentioned in
https://blog.streamlit.io/six-tips-for-improving-your-streamlit-app-performance/
memory usage struggles in the browser if you have large ranges:

> Due to implementation details, high-cardinality sliders don't suffer
> from the serialization and network transfer delays mentioned earlier,
> but they will still lead to a poor user experience (who needs to
> specify house prices up to the dollar?) and high memory usage. In my
> testing, the example above increased RAM usage by gigabytes until the
> web browser eventually gave up (though this is something that should
> be solvable on our end. We'll look into it!)

This was caused by a bug in react-range, which I fixed last year.
https://github.com/tajo/react-range/pull/178

At the time, I had figured it would get picked up by a random yarn
upgrade and didn't worry too much about it.
But, apparently yarn doesn't really have an easy way of doing upgrades
of transitive dependencies (see https://github.com/yarnpkg/yarn/issues/4986)?
I took the suggestion of someone in that thread to delete the entry and
let yarn regenerate it.

Some technical details about the react-range fix from the original
commit message (the "application" is a streamlit app):

> We have an application that uses react-range under the hood, and we
> noticed that a range input was taking 2GB of RAM on our machines. I
> did some investigation and found that regardless of whether the marks
> functionality was being used, refs were being created for each
> possible value of the range.

> We have some fairly huge ranges (we're using the input to scrub a
> video with potential microsecond accuracy), and can imagine that
> other people are affected by the previous behavior. This change
> should allow us to continue using large input ranges without
> incurring a memory penalty.

---
## [EmanuelCN/kernel_xiaomi_sm8250](https://github.com/EmanuelCN/kernel_xiaomi_sm8250)@[70665e8fbe...](https://github.com/EmanuelCN/kernel_xiaomi_sm8250/commit/70665e8fbee178fa33c16d5e22f8252bf1ce7b82)
#### Thursday 2023-08-10 19:19:25 by Peter Zijlstra

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
Change-Id: I40e0e01946eadb1701a4d06758e434591e5a5c92

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[1c852d2863...](https://github.com/tgstation/tgstation/commit/1c852d2863622bb24acf7511d7a9bb06813619fc)
#### Thursday 2023-08-10 20:22:10 by EOBGames

Martian Food: A Taste of the Red Planet (#75988)

## About The Pull Request
Adds a selection of new foods and drinks based around Mars.
More information on Mars can be found here:
https://github.com/tgstation/common_core/blob/master/Interesting%20Planets/Human%20Space/The%20Sol%20System.md
To summarise for the general audience, Mars is a vital colony of the
Terran Federation, having been primarily settled (at least originally)
by Cybersun Industries to harvest its lucrative supplies of plasma, the
second largest in human space behind Lavaland. This has given Mars a
diverse culture evolving from the mostly East Asian colonists, and their
food reflects this.

Thanks to Melbert for their work on the soup portion of this PR.

The food:
Martian cuisine draws upon the culinary traditions of East Asia, and
adds in fusion cuisine from the later colonists. Expect classics such as
ramen, curry, noodles and donburi, as well as new takes on the formula
like the Croque-Martienne, Peanut Butter Ice Cream Mochi, and the
Kitzushi- chilli cheese and rice inside a fried tofu casing. Oh, and
lots of pineapple. The Martians love pineapple:

![image](https://github.com/tgstation/tgstation/assets/58124831/c9ae33a1-e03a-4f94-8ce0-8ad124e88e8d)
Also included are some foods for Ethereals, which may or may not be
hinting at something I've got planned...

The drinks:
Four new base drinks make their way to the game, bringing with them a
host of new cocktails: enjoy new ventures in bartending with Coconut
Rum, Shochu/Soju, Yuyake (our favourite legally-distinct melon liqueur),
and Mars' favourite alcoholic beverage, rice beer. Each is available in
the dispenser, as well as bottles in the booze-o-mat:

![image](https://github.com/tgstation/tgstation/assets/58124831/914a6e2a-7ef5-4791-ae31-d08fa9211083)

The recipes:
To make your (and the wiki editors) lives easier, please find below the
recipes for both foods and drinks:
Food: https://hackmd.io/@EOBGames/BkVFU0w9Y
Drinks: https://hackmd.io/@EOBGames/rJ1OhnsJ2
## Why It's Good For The Game
Another lot of variety for the chef and bartender, as well as continuing
the work started with lizard and moth food in getting Common Core into
the game in a tangible and fun way.
## Changelog
:cl: EOBGames, MrMelbert
add: Mars celebrates the 250th anniversary of the Martian Concession
this year, and this has brought Martian cuisine to new heights of
popularity. Find a new selection of Martian foods and drinks available
in your crafting menu today!
/:cl:

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [sorbet/sorbet](https://github.com/sorbet/sorbet)@[6a1084aa55...](https://github.com/sorbet/sorbet/commit/6a1084aa558fbf334ccb605e40f347c6fa7f5069)
#### Thursday 2023-08-10 21:10:50 by Jake Zimmerman

Factor some common code (#7202)

* Factor some common code

I was seeing some crashes that arise because we were desugaring `begin;
end` to `EmptyTree`.

That's super annoying when it happens, because EmptyTree is the only
node in Sorbet's AST that doesn't have a loc (it doesn't have a loc so
that we can manage to allocate only one of them and share it across all
trees).

Which honestly, is kind of dumb these days anyways? Because the
EmptyTree will get inlined into the pointer, so it's not like we're
actually allocating memory for the EmptyTree. We're just clinging to our
old habits.

Anyways, `Kwbegin` is `begin; end` while `Begin` is `( )` (because of
course `x = ()` is valid Ruby). Their implementations in desugar were
identical, except that `()` desugared to `Nil` instead of `EmptyTree`,
and thus got a loc. That's the behavior I want, so I factored out a
helper and used it in both places.

(Maybe in a future change change I'll make it so that EmptyTree is no
longer shared globally, but that's a problem for some other day.)

* Update exp files

* Remove this error

Sorbet infers the type as `NilClass` now.

---
## [TheNeoGamer42/Echo-SS13](https://github.com/TheNeoGamer42/Echo-SS13)@[ee4021c507...](https://github.com/TheNeoGamer42/Echo-SS13/commit/ee4021c50792c11bfd21085156edd32200c21cb8)
#### Thursday 2023-08-10 21:34:56 by Imaginos16

Destroying Sprite Cruft Part One: Cruft Sucks (#2220)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Title


![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/1cedcdb1-01b5-4f28-a759-65428c2dcd0a)

In total, the:

- IV Drip
- All-In-One Grinder
- Book Binder
- Book Scanner
- Water Cooler
- Tank Dispenser

Have all been successfully uncrufted. No more cruft. Just clean sprites
now :D

Oh and dressers have directionals now at the request of @Bjarl 

Credit goes to the original authors in the changelog.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
begone cruft I fucking hate cruft
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: PositiveEntropy, Maxymax13, Wallemations, Kryson,
Viro/Axietheaxolotl, MeyHaZah
imageadd: Books, IV drips, tank dispensers, all-in-one grinders, water
coolers, book binders and book scanners have been resprited!
imageadd: Dressers now have directionals!
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Fennec82/ChaosStation--Coyote-Bayou](https://github.com/Fennec82/ChaosStation--Coyote-Bayou)@[f26fec823d...](https://github.com/Fennec82/ChaosStation--Coyote-Bayou/commit/f26fec823d7d769507a58776ceb2ecf9622f3de4)
#### Thursday 2023-08-10 21:37:40 by Tk420634

Unleashing the void

If I want to play as the literal Void from Hallow Knight I fucking will, fuck you Poojawa.

---
## [haflettjm/odin-Signupform](https://github.com/haflettjm/odin-Signupform)@[2f4e5c0f29...](https://github.com/haflettjm/odin-Signupform/commit/2f4e5c0f29b2da23d6c7507e5b130757a595f441)
#### Thursday 2023-08-10 21:39:28 by Jacob Haflett

Styling boxes re-did whole design and updating and aligning divs I hate my life

---
## [Wallemations/heavenstation](https://github.com/Wallemations/heavenstation)@[6c34d93be7...](https://github.com/Wallemations/heavenstation/commit/6c34d93be715012943626d0f812e99f730a536ef)
#### Thursday 2023-08-10 22:01:47 by necromanceranne

Nukies Update 7: Hats (Also massive uplink standardization, weapon kits and ammo changes) (#77330)

## About The Pull Request

Massively overhauls and standardizes the nuclear operative uplink. 

### Weapon Kits

Essentially, all the main weapons of the uplink have been changed to
instead come as 'weapon kits', which are essentially cases containing a
weapon loadout to enable operatives to easily start operating on only
just one item purchase, without the fuss of worrying whether or not
operatives are getting spare ammo, or getting relevant equipment for
success. Consider this a pseudo-loadout, though without necessarily
restricting the purchasing of more weapon kits.

All kits come in three categories: Low Cost (8 TC), Medium Cost (14 TC)
and High Cost (18 TC). This is also matched by categorized ammo costs;
Basic Ammo (2 TC), Hollow Point and Armour Penetrating (4 TC),
Incendiary (3 TC) and Special (or anything that does not easily fit
these categories and does something real extra) (5 TC). Weapons that
lacked these ammos have gained these ammo types to fill the gaps.

<details>
There is may one exception to this in disruptor ammo, which is priced as
basic ammo if only because it isn't _quite_ good enough to justify
pricing at 5 tc and I can see an op wanting to use it as a basic ammo
type instead of normal .50 BMG against, say, a silicon/mech heavy
opposition. Since it cannot kill organics on its own, I'll consider this
mostly basic-adjacent
</details>
The kits have also been labelled based on potential difficulty. This
reflects possible difficulties in using the item, how conducive it is to
success for how much game knowledge needed to actually use it, and how
likely an op is to succeed using it. I don't expect ops to win using
nothing but a rocket launcher, but I think ops should get a fair shake
at trying, yeah?

The kits are as below:
#### **Low-Cost**
_Bulldog (Moderate):_ Shotgun and three magazines of standard ammo.
_Ansem (Easy/Spare):_ Pistol and three spare magazines of standard ammo.
#### **Medium Cost**
_C-20r (Easy):_ SMG and three spare magazines of standard ammo.
_Energy Sword and Shield (Very Hard):_ Energy sword and shield. (Also a
special hat)
_Revolver (Moderate):_ Revolver and three speedloaders of standard ammo.
_Rocket Launcher (Hard):_ Rocket launcher with three spare rockets.
#### **High Cost**
_L6 SAW (Moderate):_ LMG, and that's it. No spare ammo.
_M-90gl (Hard):_ Rifle, two spare magazines of standard ammo and a box
of rubber grenades.
_Sniper (Hard):_ Sniper rifle, two spare magazine of standard ammo, and
one magazine of disruptor ammo. Also suit and tie.
_CQC (Very Hard):_ Comes with a stealth implant and a bandana.
_Double-Energy Sword (Very Hard):_ Double-energy sword, syndicate soap,
antislip module, meth injector and a prisoner jumpsuit.
_**NEW** Grenadier's Kit (Hard):_ Grenadier's belt and grenade launcher
(the one that launchers chem grenades). (I replaced the shit acid
grenade with another flashbang in the belt)

Surplus SMG (Flukie difficulty) has been unchanged. It just now comes
with two rations.

Includes two new revolver ammo types: Phasic, which goes through walls
and armor, but has significantly less damage as a result (I've equalized
the revolver damage and the rifle version's damage to 30 for both). And
Heartseeker, which has homing bullets. Both are Special ammo, and are
priced at 5 TC a speedloader.

### Other Gear

The other items in the uplink have also been consolidated and
standardized in various ways.

#### Grenades

Most now cost 15 TC for three grenades of any given type (including the
full fungal tuberculous). This is pretty much identical to the previous
price, just more consistent overall and front-loaded in cost.

#### Reinforcements

All the various reinforcements now cost 35 TC and all refundable,
equalizing cost to the average across the reinforcements. This is
primarily because I feel like all these options should be weighed
equally, and not one of these options are necessarily worse or better
than the other in their current balance. They're largely inaccessible
for normal ops regardless, and typically come out when there is a
discount or war ops. I took the average value and went with it. Not much
more to say.

#### Mechs

They're just cheaper. These things still suck and they need help.
They've always needed help. A slightly less excessive value for the
mechs may help see people willing to spend the TC on them. I doubt it. I
seriously suggest not buying these still. I keep them in primarily
because they are big stompy mechs and are kind of iconic 'war ops' gear.

#### Bundles

Since I've implemented weapon kits, gun bundles are rather redundant. So
the bulldog weapon and ammo bundle, the c20-r weapon and ammo bundle and
technically the sniper bundle were removed. The sniper bundle is now the
weapon kit, obviously.

Nothing else here really. Except for one....

#### Implants

Not much changed here. I standardized the implant prices to 8 TC a pop.
This is in accordance with traitor implants, which ops also get. So
everything in this category bar a few exceptions (like macro/microbombs)
are around 8 TC. Makes sense to me, really.

Importantly, I made the Implant bundle 25 TC, and I unrandomized the
contents. Who in the right fucking mind would spend 40 TC just to get
five reviver implants is beyond me. But instead, you get one of each of
the cybernetic implants except thermal eyes (you can just buy thermals
and get the benefit of both vision types; x-ray and thermal vision, if
you want to use smokescreens a lot).

#### Base Keys

They're all now 15 TC, except the fridge which is 5 TC. It's weird
they're valued differently when they are taken mostly to do gimmicks
like xenobio and toxins in a hurry before hitting the station. So we've
standardized it.

## Hat Crate

**YES, GOOD SIR, YOU TOO CAN ORDER A HAT CRATE FROM THE SYNDICATE STORE
FOR ONLY 5 TC!**

**NO NEED FOR A KEY, JUST BUY IT AND PULL IT OPEN WITH YOUR STANDARD
ISSUE CROWBAR!**

**ENJOY YOUR NEW CRATE! ENJOY YOUR NEW HAT!**

**PUT IT ON USING THE FREE HAT STABILIZERS WE INCLUDED WITH THE HATS!**

~~**NO REFUNDS IF YOU GET BLOOD ON YOUR HAT!**~~

<details>
There is a 1% chance to instagib people with direct hits from a rocket.
This does the crit effect.
</details>

## Why It's Good For The Game

The uplink needed more spring cleaning and standardization.

With this, I've partially implemented my older idea for ammo consistency
and initial allowance for nukies. Ammo is kind of over-priced and often
where a good chunk of TC goes towards without really pushing nukies
towards meaningful success. And it is often what is tripping up new
players who didn't think to get any. Now, when they get a gun, they get
ammo in their case. On top of this, the weapon kit category is both at
the top of the uplink AND has a little label to say 'Recommend', so that
these new players will hopefully know they should be looking there
first.

In addition, it is the gateway towards a concept that is currently being
worked on. Nuclear operatives having some degree of predefined loadouts
for players to select if they aren't sure what they want, or don't know
what to get. Nukies is very confusing for many players. So giving them a
fighting chance with some premade setups can help ease them into the
role without needing too much player knowledge in how to apply the
items. This is only one step towards that, so that players can identify
what gear they need to help succeed based on their skill.

I wanted to implement a difficulty warning so that players can choose
gear loadouts that are actually conducive to their skill and knowledge.
I based it on how much players would need to know to engage in combat
with it, and how much fiddling is required to get something to work
properly (overly involved reloading is a consideration, for example, as
well as precise button presses). In addition, how much of a force
multiplier some weapons can be for their ease of use.

Most people recognize the c20-r as the most new player friendly weapon,
as an example. So it would be good to steer players towards taking that
gun because of how easy it is to use, understand and succeed with it.

And most importantly of all; Having standards within the uplink is
important. Most of the values in the uplink are just completely random.
Nobody has a good grasp of what is too much or too little. Even just a
hint of consistency, and people will stick to it (see implants for what
I mean). And there is still some work to be done even there. A good
start is weapons. Price for power can be meaningful when decided whether
we want some weapons to come out more often than others. Players do
enjoy making informed decisions and choices, and having affordability be
a draw to some otherwise less powerful weapons (looking at you, Bulldog)
can actually be a worthwhile and meaningful difference.

~~I thought it would tick off the gun nerds to change the calibers on
the guns.~~

~~I also thought adding hats would be funny given the release of TF2's
most recent update.~~

## Changelog
:cl:
balance: Standardizes some of the nuclear operative entries to have more
consistent pricing within their respective categories.
add: Adds some new categories so that players have an easier time
navigating the nuclear operative uplink.
balance: Many items have had prices reduced or adjusted to make them
more desirable or more consistent within their category.
add: Weapon kits have replaced almost all the individual weapons in the
uplink. You now buy these instead of the individual weapon. These often
come with spare ammo or relevant gear for success.
add: Most ammo types have been standardized in price.
refactor; Removes a lot of redundant item entry code and tidies up the
actual code part of the nuclear uplink so that it is much easier to find
things within it.
add: Added 40 new cosmetic items to the Syndicate Store. Buy them now
from the Hat Crate, only 5 TC!
code: Updated the nuclear operative uplink files.
/:cl:

---
## [Wallemations/heavenstation](https://github.com/Wallemations/heavenstation)@[95ec0e6545...](https://github.com/Wallemations/heavenstation/commit/95ec0e65458ece9c5c80952e75d5d32c4fbb794b)
#### Thursday 2023-08-10 22:01:47 by necromanceranne

Dissection experiments are handled by autopsy surgery. Removes redundant dissection surgery. You can repeat an autopsy on someone who has come back to life. (#77386)

## About The Pull Request

TRAIT_DISSECTED has had the surgical speed boost moved over to
TRAIT_SURGICALLY_ANALYZED.

TRAIT_DISSECTED now tracks if we can do an autopsy on the same body
again, and blocks further autopsies if it is on the mob. A mob that
comes back to life loses TRAIT_DISSECTED. This allows for mobs to be
autopsied once again.

Since it is completely redundant now (and was the whole time TBH),
dissections have been removed in favour of just having the experiment
track autopsies.

Fixes https://github.com/tgstation/tgstation/issues/76775

## Why It's Good For The Game

Today I showed up to a round where someone autopsied all the bodies in
the morgue, not realizing they were using the wrong surgery. Since I
couldn't _redo_ the surgery, this rendered all these bodies useless.
This was not out of maliciousness, they just didn't know better. There
are two autopsies in the surgery list, but only one is valid for the
experiment and doing the wrong one blocks _both surgeries_. Dissection
is completely useless outside of experiments. This same issue also
prevents additional autopsies on the same person, even if they had come
back to life and died again after you had done the initial autopsy.
Surely you would want to do more than one autopsy, right? That's two
separate deaths!

This resolves that by giving you a method of redoing any screwups on the
same corpse if necessary. It only matters if the experiment is available
anyway, so there isn't much reason to punish players unduly just because
they weren't aware science hadn't hit a button on their side (especially
since it isn't communicated to the coroner in any way to begin with). It
also removes a completely useless surgery and ties in the experiment to
what the coroner is already going to be doing. They can dissect their
corpses to their hearts content without worrying about retribution from
science for doing so.

In addition, someone repeatedly dying can continue to have autopsies
done on them over the course of the round. The surgery bonus only
applies once, so the only reason to do autopsies after the first is to
discover what might have killed someone. No reason this should block
further surgeries, just block surgeries when the person remains a
corpse.

## Changelog
:cl:
fix: You can do autopsies on people who were revived and died again
after they had already been dissected.
qol: Autopsies have become the surgery needed to complete the dissection
experiments. As a result, the dissection surgery has been removed as it
is now redundant.
qol: A coroner knows whether someone has been autopsied and recently
dissected (and thus hasn't been revived) by examining them.
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [LM95A1/Project-Epsilon-4](https://github.com/LM95A1/Project-Epsilon-4)@[a38e8eb04c...](https://github.com/LM95A1/Project-Epsilon-4/commit/a38e8eb04c3e040d254248a24bb0a765b9fbcb6c)
#### Thursday 2023-08-10 22:12:38 by LM95A1

Acquired a Tuesday

Added templates directory to house index.html
Updated spiderweb.py since the original was f**ked
Updated script.js for additional features
Updated style.css to add a bunch of different options, many of which may remain unused
Added pokeball.png in images directory; I was sick of the f**king paw logo

Been experimenting with the structure of the dashboard and the features of the Pokedex to better fit what we're trying to do. Making progress at a very slow rate, given the time constraints and outside obligations piling up. Bad timing, yeah? Gonna have to go full throttle with this tonight and tomorrow.

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[af5a815192...](https://github.com/treckstar/yolo-octo-hipster/commit/af5a815192f61a41703a4aa0552a5fefe3384ddf)
#### Thursday 2023-08-10 22:22:04 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [peff/git](https://github.com/peff/git)@[bd7e41ab4f...](https://github.com/peff/git/commit/bd7e41ab4f23ab57b4307b69b6f62efa489bc6aa)
#### Thursday 2023-08-10 22:37:21 by Jeff King

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
## [colinhacks/next.js](https://github.com/colinhacks/next.js)@[e06880ea4c...](https://github.com/colinhacks/next.js/commit/e06880ea4c061fc5c298b262d01f347edd8dce74)
#### Thursday 2023-08-10 23:40:02 by Josh Story

Implement new forking technique for vendored packages. (#51083)

## Vendoring

Updates all module resolvers (node, webpack, nft for entrypoints, and nft for next-server) to consider whether vendored packages are suitable for a given resolve request and resolves them in an import semantics preserving way.

### Problem

Prior to the proposed change, vendoring has been accomplished but aliasing module requests from one specifier to a different specifier. For instance if we are using the built-in react packages for a build/runtime we might replace `require('react')` with `require('next/dist/compiled/react')`.

However this aliasing introduces a subtle bug. The React package has an export map that considers the condition `react-server` and when you require/import `'react'` the conditions should be considered and the underlying implementation of react may differ from one environment to another. In particular if you are resolving with the `react-server` condition you will be resolving the `react.shared-subset.js` implementation of React. This aliasing however breaks these semantics because it turns a bare specifier resolution of `react` with path `'.'` into a resolution with bare specifier `next` with path `'/dist/compiled/react'`. Module resolvers consider export maps of the package being imported from but in the case of `next` there is no consideration for the condition `react-server` and this resolution ends up pulling in the `index.js` implementation inside the React package by doing a simple path resolution to that package folder.

To work around this bug there is a prevalence of encoding the "right" resolution into the import itself. We for instance directly alias `react` to `next/dist/compiled/react/react.shared-subset.js` in certain cases. Other times we directly specify the runtime variant for instance `react-server-dom-webpack/server.edge` rather than `react-server-dom-wegbpack/server`, bypassing the export map altogether by selecting the runtime specific variant. However some code is meant to run in more than one runtime, for instance anything that is part of the client bundle which executes on the server during SSR and in the browser. There are workaround like using `require` conditionally or `import(...)` dynamically but these all have consequences for bundling and treeshaking and they still require careful consideration of the environment you are running in and which variant needs to load.

The result is that there is a large amount of manual pinning of aliases and additional complexity in the code and an inability to trust the package to specify the right resolution potentially causing conflicts in future versions as packages are updated.

It should be noted that aliasing is not in and of itself problematic when we are trying to implement a sort of lightweight forking based on build or runtime conditions. We have good examples of this for instance with the `next/head` package which within App Router should export a noop function. The problem is when we are trying to vendor an entire package and have the package behave semantically the same as if you had installed it yourself via node_modules

### Solution

The fix is seemingly straight forward. We need to stop aliasing these module specifiers and instead customize the resolution process to resolve from a location that will contain the desired vendored packages. We can then start simplifying our imports to use top level package resources and generally and let import conditions control the process of providing the right variant in the right context.

It should be said that vendoring is conditional. Currently we only vendor react pacakges for App Router runtimes. The implementation needs to be able to conditionally determine where a package resolves based on whether we're in an App Router context vs a Page Router one.

Additionally the implementation needs to support alternate packages such as supporting the experimental channel for React when using features that require this version.

### Implementation

The first step is to put the vendored packages inside a node_modules folder. This is essential to the correct resolving of packages by most tools that implement module resolution. For packages that are meant to be vendored, meaning whole package substitution we move the from `next/(src|dist)/compiled/...` to `next/(src|dist)/vendored/node_modules`. The purpose of this move is to clarify that vendored packages operate with a different implementation. This initial PR moves the react dependencies for App Router and `client-only` and `server-only` packages into this folder. In the future we can decide which other precompiled dependencies are best implemented as vendored packages and move them over.

It should be noted that because of our use of `JestWorker` we can get warnings for duplicate package names so we modify the vendored pacakges for react adding either `-vendored` or `-experimental-vendored` depending on which release channel the package came from. While this will require us to alter the request string for a module specifier it will still be treating the react package as the bare specifier and thus use the export map as required.

#### module resolvers
The next thing we need to do is have all systems that do module resolution implement an custom module resolution step. There are five different resolvers that need to be considered

##### node runtime
Updated the require-hook to resolve from the vendored directory without rewriting the request string to alter which package is identified in the bare specifier. For react packages we only do this vendoring if the `process.env.__NEXT_PRIVATE_PREBUNDLED_REACT` envvar is set indicating the runtime is server App Router builds. If we need a single node runtime to be able to conditionally resolve to both vendored and non vendored versions we will need to combine this with aliasing and encode whether the request is for the vendored version in the request string. Our current architecture does not require this though so we will just rely on the envvar for now

##### webpack runtime
Removed all aliases configured for react packages. Rely on the node-runtime to properly alias external react dependencies. Add a resolver plugin `NextAppResolverPlugin` to preempt perform resolution from the context of the vendored directory when encountering a vendored eligible package.

##### turbopack runtime
updated the aliasing rules for react packages to resolve from the vendored directory when in an App Router context. This implementation is all essentially config b/c the capability of doing the resolve from any position (i.e. the vendored directory) already exists

##### nft entrypoints runtime
track chunks to trace for App Router separate from Pages Router. For the trace for App Router chunks use a custom resolve hook in nft which performs the resolution from the vendored directory when appropriate.

##### nft next-server runtime
The current implementation for next-server traces both node_modules and vendored version of packages so all versions are included. This is necessary because the next server can run in either context (App vs Page router) and may depend on any possible variants. We could in theory make two traces rather than a combined one but this will require additional downstream changes so for now it is the most conservative thing to do and is correct

Once we have the correct resolution semantics for all resolvers we can start to remove instances targeting our precompiled instances for instance making `import ... from "next/dist/compiled/react-server-dom-webpack/client"` and replacing with `import ... from "react-server-dom-webpack/client"`

We can also stop requiring runtime specific variants like `import ... from "react-server-dom-webpack/client.edge"` replacing it with the generic export `"react-server-dom-webpack/client"`

There are still two special case aliases related to react
1. In profiling mode (browser only) we rewrite `react-dom` to `react-dom/profiling` and `scheduler/tracing` to `scheduler/tracing-profiling`. This can be moved to using export maps and conditions once react publishses updates that implement this on the package side.
2. When resolving `react-dom` on the server we rewrite this to `react-dom/server-rendering-stub`. This is to avoid loading the entire react-dom client bundle on the server when most of it goes unused. In the next major react will update this top level export to only contain the parts that are usable in any runtime and this alias can be dropped entirely

There are two non-react packages currently be vendored that I have maintained but think we ought to discuss the validity of vendoring. The `client-only` and `server-only` packages are vendored so you can use them without having to remember to install them into your project. This is convenient but does perhaps become surprising if you don't realize what is happening. We should consider not doing this but we can make that decision in another discussion/PR.

#### Webpack Layers
One of the things our webpack config implements for App Router is layers which allow us to have separate instances of packages for the server components graph and the client (ssr) graph. The way we were managing layer selection was a but arbitrary so in addition to the other webpack changes the way you cause a file to always end up in a specific layer is to end it with `.serverlayer`, `.clientlayer` or `.sharedlayer`. These act as layer portals so something in the server layer can import `foo.clientlayer` and that module will in fact be bundled in the client layer.

#### Packaging Changes
Most package managers are fine with this resolution redirect however yarn berry (yarn 2+ with PnP) will not resolve packages that are not defined in a package.json as a dependency. This was not a problem with the prior strategy because it was never resolving these vendored packages it was always resolving the next package and then just pointing to a file within it that happened to be from react or a related package.

To get around this issue vendored packages are both committed in src and packed as a tgz file. Then in the next package.json we define these vendored packages as `optionalDependency` pointing to these tarballs. For yarn PnP these packed versions will get used and resolved rather than the locally commited src files. For other package managers the optional dependencies may or may not get installed but the resolution will still resolve to the checked in src files. This isn't a particularly satisfying implemenation and if pnpm were to be updated to have consistent behavior installing from tarballs we could actually move the vendoring entirely to dependencies and simplify our resolvers a fair bit. But this will require an upstream chagne in pnpm and would take time to propogate in the community since many use older versions

#### Upstream Changes

As part of this work I landed some other changes upstream that were necessary. One was to make our packing use `npm` to match our publishing step. This also allows us to pack `node_modules` folders which is normally not supported but is possible if you define the folder in the package.json's files property.

See: #52563

Additionally nft did not provide a way to use the internal resolver if you were going to use the resolve hook so that is now exposed

See: https://github.com/vercel/nft/pull/354

#### additional PR trivia
* When we prepare to make an isolated next install for integration tests we exclude node_modules by default so we have a special case to allow `/vendored/node_modules`

* The webpack module rules were refactored to be a little easier to reason about and while they do work as is it would be better for some of them to be wrapped in a `oneOf` rule however there is a bug in our css loader implementation that causes these oneOf rules to get deleted. We should fix this up in a followup to make the rules a little more robuts.


## Edits
* I removed `.sharedlayer` since this concept is leaky (not really related to the client/server boundary split) and it is getting refactored anyway soon into a precompiled runtime.

---
## [youngfeiler/SmartBetter-website](https://github.com/youngfeiler/SmartBetter-website)@[61aa943eea...](https://github.com/youngfeiler/SmartBetter-website/commit/61aa943eeaa1cdb36509b059bba43ffa55a42061)
#### Thursday 2023-08-10 23:50:57 by micahcb

ahhhhhh helppppp my brain its FUCK FUCK shit balls

---

