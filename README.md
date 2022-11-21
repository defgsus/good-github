## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-11-20](docs/good-messages/2022/2022-11-20.md)


1,931,011 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,931,011 were push events containing 2,533,796 commit messages that amount to 144,552,108 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 33 messages:


## [saurabhmshr/exercism-rust](https://github.com/saurabhmshr/exercism-rust)@[7a49959ea4...](https://github.com/saurabhmshr/exercism-rust/commit/7a49959ea4aa3dbe3f5dd23a1de909196d62ea13)
#### Sunday 2022-11-20 00:04:35 by Remo Senekowitsch

xorcism: remove rstest dependency (#1590)

rstest uses proc macros, which make the tests timeout due to long
compile times. Replace rstest with a custom declarative macro.

Brings test time from 7.5 seconds to 0.8 seconds on my machine.

Drawbacks:
* more indentation
* module structure of tests is flipped around

both of those seem minor to me. 

Although declarative macros can be hard to read for those unfamiliar, 
that was already somewhat the case with rstest's magic in my opinion. So
I personally don't think it's worse in terms of the students being able to
understand the tests.

The only other alternative I see is to disable the online tests 
altogether and leave a note about that in the exercise description. That
probably wouldn't be that bad, since people solving this hard exercise
most likely have a solid local setup. But it would still be cool to run
the tests online as well.

https://github.com/exercism/rust/issues/1513

---
## [donkeyrat/HiddenUnits](https://github.com/donkeyrat/HiddenUnits)@[5573cc01b1...](https://github.com/donkeyrat/HiddenUnits/commit/5573cc01b19da4e0ad4829324a392418c224c551)
#### Sunday 2022-11-20 00:26:09 by donkeyrat

billy fixes #100

i fucking hate billy piece of shit

---
## [RigglePrime/tgstation](https://github.com/RigglePrime/tgstation)@[de662db397...](https://github.com/RigglePrime/tgstation/commit/de662db39763674f850977dabc8bbe66388d2c9b)
#### Sunday 2022-11-20 00:35:56 by Sol N

Excercise Equipment is now craftable (#71190)

## About The Pull Request

Imagine if you will a humble chaplain who wants nothing more than for
all of the spiritual folk on the station to get as massive gains as they
can, after finding that they can not just make more exercise equipment
and that the station does not have any in public places, they go annoy
security enough to get into permabrig only to find out that they cant
even unwrench the equipment and move it to the church!!!

NOT ANYMORE!!!


![jS2aBMBa0B](https://user-images.githubusercontent.com/116288367/200889423-f1b6365c-24c4-4f45-8ca4-c96c9085cf27.png)
crafting recipies


![dreamseeker_O4BgBRsFa8](https://user-images.githubusercontent.com/116288367/200889002-8dd7c927-0745-46a9-a4bc-578c7279042a.gif)
demonstrating unwrenching and wrenching equipment


![dreamseeker_hCFQJZdzoS](https://user-images.githubusercontent.com/116288367/200889019-5f4c8399-d539-4d84-8a3f-7735c3ba1f68.gif)
crafting a punching bag and punching it

Now you can craft as much exercise equipment as you want! May everyone
on the station get as strong as possible and not just prisoners.

Also I changed the message that plays when you try to use exercise
equipment someone else is using into a balloon alert.

![dreamseeker_PwNesmcR1f](https://user-images.githubusercontent.com/116288367/200890964-4f9fa3ee-ce07-4e6e-815c-a3f4593d06b1.png)

## Why It's Good For The Game

Access to exercise equipment on some maps is limited to static positions
and is currently mostly only for prisoners as every map does not have
public exercise equipment. Expanding the access means that you can have
a Drill Sargent Head of Security or Captain who commands people use
these or allows a psychologist to prescribe healthy exercise habits to
their patients.

I think having the potential for exercise equipment on every map is more
fun and also if prisoners get their hands on tools they should be
allowed to mess with these to annoy security or aid in their escape.

## Changelog
:cl:
add: the punching bag, bench press, and chest press are all able to be
crafted and unanchored.
add: crafting recipes for the above
qol: changed a chat message into a balloon alert
qol: adds screentips to equipment (thanks for suggesting i do this
mothblocks!)
/:cl:

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[b77cf7c120...](https://github.com/tgstation/tgstation/commit/b77cf7c1205d466b8cb242cd3302891e82b44da2)
#### Sunday 2022-11-20 00:58:42 by Iamgoofball

Hotkey-based inventory management now applies the click cooldown to prevent it from being abusable in combat scenarios. (#71325)


About The Pull Request

Hotkey-based inventory management now applies the click cooldown to prevent it from being abusable in combat scenarios.
Why It's Good For The Game

Players have been deploying unbelievable levels of abuse with these hotkeys having completely uncapped speeds.
I watched one cheater do automated inventory management using storage items and weirdly named empty pills to use as inventory delimiters.
Resolves people being able to have a baton hidden in their backpack and then activate and baton someone with it in 0.1 seconds without moving their mouse cursor off of their target.

Players should not be able to interact with their inventory faster than someone moving a mouse and clicking the left mouse button. This cripples the game balance and puts anyone with a worse internet connection, slower reaction speeds, or laggier computer at a distinct disadvantage against people who can macro their inventory management.

I can set up autohotkey so that I can withdraw a stun baton from my backpack, turn it on, and then click someone by just holding down a key and pressing M1 over someone. This shit needs to stop.

If a do_after() on hotkey management is too harsh, we can apply a combat click cooldown every time you use the hotkeys instead to discourage combat macro abuse.
Swapped it over to a click cooldown.
Changelog

cl
balance: Hotkey-based inventory management now applies the click cooldown to prevent it from being abusable in combat scenarios.
/cl

---
## [nurupo/chrome-mouse-wheel-tab-scroller](https://github.com/nurupo/chrome-mouse-wheel-tab-scroller)@[a63bf16d62...](https://github.com/nurupo/chrome-mouse-wheel-tab-scroller/commit/a63bf16d62622d69831d90d5ca7e8dde7886da97)
#### Sunday 2022-11-20 02:27:35 by Maxim Biro

Fix browser contents from occasionally scrolling

This finally fixes the long lasting issue for good.

We used to use Send() before, but after some changes and AutoIt update,
Send() was resulting in the Ctrl key being stuck in the pressed down
state. To work around this, we switched to using ControlSend(). However,
it turned out to have its own can of worms -- tab preview pop-ups were
eating up the keys we were trying to send, and the Ctrl key sometimes
was not being sent, with just PgUp/PgDn being sent, resulting in the web
page being scrolled instead of the tab being switched, which is
extremely annoying. While we worked around the tab preview pop-ups
eating keys, the page scrolling issue persisted. What made it especially
hard to troubleshoot is the inability to reproduce it -- it wasn't
obvious what exactly was causing it, it just happened occasionally. Only
recently I have managed to more or less reliably reproduce the page
scrolling issue: turns out it happens when you scroll just before or at
the time the tab preview pop-up gets created. The timing is very tight,
which is why when I have previously tested if the scrolling was caused
by the preview pop-ups I wasn't able to reproduce it. ControlSend()
attaches to the input thread of the application, so my guess is that
when a new control/window gets created while ControlSend() doing the
attachment, it somehow throws ControlSend() off, resulting in only
PgUp/PgDn being sent to the target control, so it's not something I can
fix without modifying AutoIt, which I can't do with it not being open
source. Recalling that none of this was the issue with the original
Send() code we had, I have switched to using that, and turns out you can
easily fix the issue of Ctrl being stuck by just pressing Ctrl once with
ControlSend() to unstuck it. So much time spent working around and
debugging ControlSend() issues when it was a lot easier to workaround
the Send() issue.

---
## [Zergspower/Skyrat-tg](https://github.com/Zergspower/Skyrat-tg)@[317aea0435...](https://github.com/Zergspower/Skyrat-tg/commit/317aea043510ee0c3591ff3a06fdffd360fdfc29)
#### Sunday 2022-11-20 02:42:37 by Jolly

[FUCK] [NO GBP] Yeah, fixes something in NuInterlink(?) (#17544)

fucking GODDAMNIT

---
## [Minecraft-Eternal/MC-Eternal-1.12](https://github.com/Minecraft-Eternal/MC-Eternal-1.12)@[cb2dfe3d66...](https://github.com/Minecraft-Eternal/MC-Eternal-1.12/commit/cb2dfe3d66d14db538eceac3fa111352faeb1acd)
#### Sunday 2022-11-20 03:03:57 by anabsolutesloth

make pure blood (vampirism) craftable with magic mods

baron spawnrates suck and fixing it will be annoying and maybe even not reasonable

---
## [Benbebop/Benbebot](https://github.com/Benbebop/Benbebot)@[9e88a10159...](https://github.com/Benbebop/Benbebot/commit/9e88a10159deae234975a9872525e711c2c9810e)
#### Sunday 2022-11-20 05:00:49 by Benbebop

source dedicated server fucking works omg

ive been fucking working on this for months im going insane its working

---
## [feeby2494/corolla_buddy_backend](https://github.com/feeby2494/corolla_buddy_backend)@[511644232b...](https://github.com/feeby2494/corolla_buddy_backend/commit/511644232b99972acaea4c2f891cda5aca8980e3)
#### Sunday 2022-11-20 05:06:37 by Jamie Lynn

Pushed out to a new brach called master on accident. Now rebasing master to main.

Git is fucking stupid as hell.

Started on repair_service app. Not included in "INSTALLED_APPS" yet.

---
## [Queerscriptors/queerscriptors.org](https://github.com/Queerscriptors/queerscriptors.org)@[5a8815c73e...](https://github.com/Queerscriptors/queerscriptors.org/commit/5a8815c73ee50c68b52d6ad78638df2d21df7ec1)
#### Sunday 2022-11-20 05:30:26 by HackerNCoder

Add a lot of games to the list

Coming Out Simulator
Missed Messages
A New Life
One Night, Hot Springs
Talking to my Dad
There's this girl
Us Lovely Corpses

---
## [lizardqueenlexi/orbstation](https://github.com/lizardqueenlexi/orbstation)@[84a85c827d...](https://github.com/lizardqueenlexi/orbstation/commit/84a85c827d71b3326b482444a204711de38cf518)
#### Sunday 2022-11-20 07:13:41 by lizardqueenlexi

Removed TRAIT_PLASMABURNT, fixed plasma river limb transformation. (#71157)

## About The Pull Request

Resolves #67282.

As originally designed, plasma rivers (namely, those on Icebox, though
the turf was originally made for the Snowdin away mission) are meant to
literally strip the flesh from your bones, leaving you with plasmaman
limbs. I'm not certain when this broke entirely, although it seems to
have never been updated to work alongside Kapulimbs.

Transformation of limbs into plasmaman limbs used to be accomplished by
adding the "PLASMABURNT" trait to limbs. However, this trait in the
current code is entirely meaningless, only checked in the proc that
makes plasmamen catch fire. Essentially, the only "interaction" is
having your flesh melted off by a plasma river, donating that specific
limb to a plasmaman, and pranking them with the fact that that specific
limb will still make them burst into flames.

Exciting.

I've removed the trait entirely, as it does functionally nothing, and
restored the ability of plasma rivers to turn your limbs - and
eventually, you - into plasmaman equivalents.

To be honest, I'm not _entirely_ satisfied with the plasmaman
transformation process - it doesn't especially suit the lore of
plasmamen, and if you transform into one in the plasma rivers you'll
probably immediately die from Icemoon's atmosphere anyway. However, this
is something I'd prefer to revisit in a later PR.
## Why It's Good For The Game

There's little reason _not_ to remove a trait that does nothing.

As for plasmafication, it's a fun interaction that was already _meant_
to be there. The message about your flesh melting off has always
printed, even while it's doing exactly nothing to you. It's cool to fall
into the deadly plasma river and come away from it permanently scarred
with a weird skeleton limb. Turning into a plasmaman entirely is
unlikely to happen and will probably just kill you, but it's a fun and
weird way to be dead.
## Changelog
:cl:
del: Removed the useless "plasmaburnt" trait.
fix: Restored a broken interaction with plasma rivers that slowly
transforms you into a plasmaman.
/:cl:

---
## [JohnFulpWillard/JollyStation](https://github.com/JohnFulpWillard/JollyStation)@[0cd78be6a1...](https://github.com/JohnFulpWillard/JollyStation/commit/0cd78be6a19a9a3d6907cdf84759c59717dd8cb4)
#### Sunday 2022-11-20 07:31:26 by TaleStationBot

[MIRROR] [MDB IGNORE] Heretics cannot be converted, and are immune to cult stun hands. Instead, the cult is rewarded for sacrificing them with the bloody bastard sword, an oversized SPIN2WIN funblade. + Soul Stealing Fantasy Affix (#2617)

* Heretics cannot be converted, and are immune to cult stun hands. Instead, the cult is rewarded for sacrificing them with the bloody bastard sword, an oversized SPIN2WIN funblade. + Soul Stealing Fantasy Affix (#69725)

About The Pull Request

Heretics can no longer be converted to a cult, as they follow their own Forgotten Gods.
Instead, Nar'Sie will reward the cult for managing to sacrifice one, with the bastard sword.
The bloody bastard sword has been cleaned up codewise and all that. Because it is a free reward instead of a (removed) progression mechanic of cult, it swings just a bit slower during the spin and doesn't have a jaunt. It's still a !fun! swinging sword of hilarity and death.
BLOODY BASTARD https://www.youtube.com/watch?v=ukznXQ3MgN0
Fantasy weapons can now roll "soul-stealing" weapons. They, on killing something, capture its soul inside the item.

    Add fail conditions that instantly end a spin2win, ala how 

    Mimes can now hold a baguette like a sword by right clicking it #69592 works

Why It's Good For The Game

Bloody bastard sword was fun, it made no sense that heretics were valid converts when they're already worshipping a DIFFERENT evil god granting them powers. Should be in a good spot as a nice little antag to antag special interaction. I fucking love antag to antag special interactions, we should have more of 'em

Fantasy affixes are always a neat thing to throw a new component into
Changelog

cl
add: Heretics can no longer be converted to cult. But sacrificing them is very valuable to Nar'Sie, and she will grant special weapons if you manage to do so.
add: Fantasy affixes can also include soul-stealing items!
/cl

* Heretics cannot be converted, and are immune to cult stun hands. Instead, the cult is rewarded for sacrificing them with the bloody bastard sword, an oversized SPIN2WIN funblade. + Soul Stealing Fantasy Affix

Co-authored-by: tralezab <40974010+tralezab@users.noreply.github.com>

---
## [Sunrin-Social-Network/SSN-server](https://github.com/Sunrin-Social-Network/SSN-server)@[bb494c3a72...](https://github.com/Sunrin-Social-Network/SSN-server/commit/bb494c3a72f7a7306faca972be4035c86aba1ec2)
#### Sunday 2022-11-20 09:31:17 by Hyunjun Yang

Merge pull request #13 from Sunrin-Social-Network/main

I HATE FUCKING SPRING

---
## [Sunrin-Social-Network/SSN-server](https://github.com/Sunrin-Social-Network/SSN-server)@[c18463c05f...](https://github.com/Sunrin-Social-Network/SSN-server/commit/c18463c05f33f05b35ed34629df57feb881ea71c)
#### Sunday 2022-11-20 09:31:17 by Hyunjun Yang

Merge pull request #14 from Sunrin-Social-Network/main

I HATE FUCKING SPRING

---
## [Sunrin-Social-Network/SSN-server](https://github.com/Sunrin-Social-Network/SSN-server)@[ef303cf507...](https://github.com/Sunrin-Social-Network/SSN-server/commit/ef303cf5077b2903a8a053527ab8785acf7f7473)
#### Sunday 2022-11-20 09:31:17 by Hyunjun Yang

Merge pull request #15 from Sunrin-Social-Network/main

I HATE FUCKING SPRING

---
## [Sunrin-Social-Network/SSN-server](https://github.com/Sunrin-Social-Network/SSN-server)@[4bb0500f27...](https://github.com/Sunrin-Social-Network/SSN-server/commit/4bb0500f275b5be8539d54bfa89eca09c2469472)
#### Sunday 2022-11-20 09:31:17 by Hyunjun Yang

Merge pull request #16 from Sunrin-Social-Network/main

I HATE FUCKING SPRING

---
## [Sunrin-Social-Network/SSN-server](https://github.com/Sunrin-Social-Network/SSN-server)@[06678b3a89...](https://github.com/Sunrin-Social-Network/SSN-server/commit/06678b3a89cc8487d40b19f5d81aaabe3cca90f2)
#### Sunday 2022-11-20 09:31:17 by Hyunjun Yang

Merge pull request #17 from Sunrin-Social-Network/main

I HATE FUCKING SPRING

---
## [Sunrin-Social-Network/SSN-server](https://github.com/Sunrin-Social-Network/SSN-server)@[9dadbdb9f6...](https://github.com/Sunrin-Social-Network/SSN-server/commit/9dadbdb9f6f870daf62bcbd1683f895f6656f4ee)
#### Sunday 2022-11-20 09:31:17 by Hyunjun Yang

Merge pull request #18 from Sunrin-Social-Network/main

I HATE FUCKING SPRING

---
## [JeserTheFox/cmss13](https://github.com/JeserTheFox/cmss13)@[7cb69c2a8b...](https://github.com/JeserTheFox/cmss13/commit/7cb69c2a8b6f8895d5475b709183a3f30d05fbeb)
#### Sunday 2022-11-20 10:34:46 by Joelampost

Creates a new tile for the predator ship (#1400)

* erm

* yer

* fuck you shaddeh

---
## [xljtswf/guava](https://github.com/xljtswf/guava)@[8a676ade61...](https://github.com/xljtswf/guava/commit/8a676ade617c6be992165cd0658779a14acef2f2)
#### Sunday 2022-11-20 12:07:11 by cpovirk

Make the build work under more JDK versions.

(Guava is already _usable_ under plenty of verions. This change affects only people who build it themselves.)

And run CI under JDK17. Maybe this will make CI painfully slow, but we'll see what happens. If we want to drop something, we should consider whether to revert 17 or to drop 11 instead (so as to maintain coverage at the endpoints of \[8, 17\]).

## Notes on some of the versions

### JDK9

I expected Error Prone to work, but I saw `invalid flag: -Xep:NullArgumentForNonNullParameter:OFF`, even though that flag is [already](https://github.com/google/guava/blob/166d8c0d8733d40914fb24f368cb587a92bddfe0/pom.xml#L515) part of [the same `<arg>`](https://github.com/google/error-prone/issues/1086#issuecomment-411544589), which works fine for other JDK versions. So I disabled Error Prone for that version.

Then I had a Javadoc problem with the `--no-module-directories` configuration from cl/413934851 (the fix for https://github.com/google/guava/issues/5457). After reading [JDK-8215582](https://bugs.openjdk.org/browse/JDK-8215582) more carefully, I get the impression that that flag might not have been added until 11: "addressed in JDK 11, along with an option to revert to the old layout in case of need." So I disabled it for 9-10.

Then I ran into a problem similar to https://github.com/bazelbuild/bazel/issues/6173 / [JDK-8184940](https://bugs.openjdk.java.net/browse/JDK-8184940). I'm not sure exactly what tool produced a file with a month of 0, but it happened only when building `guava-tests`. At that point, I gave up, though I left the 2 above workarounds in place.

### JDK10

This fails with some kind of problem finding a Guice dependency inside Maven. I didn't investigate.

### JDK15 and JDK16

These fail with [the `TreeMap` bug](https://bugs.openjdk.org/browse/JDK-8259622) that [our collection testers had detected](https://github.com/google/guava/issues/5801#issue-1068748849) but we never got around to reporting. Thankfully, it got reported and [fixed](https://github.com/openjdk/jdk/commit/2c8e337dff4c84fb435cafac8b571f94e161f074) for JDK17. We could consider suppressing the tests under that version.

### JDK18, JDK19, and JDK20-early-access

These fail with [`SecurityManager` trouble](https://github.com/google/guava/issues/5801#issuecomment-1293817701).

## Notes on the other actual changes

### `maven-javadoc-plugin`

I set up `maven-javadoc-plugin` to use `-source ${java.specification.version}`. Otherwise, it would [take the version from `maven-compiler-plugin`](https://github.com/google/guava/issues/5801#issuecomment-1314291284). That's typically fine: Guava's source code targets Java 8, so `-source 8` "ought" to work. But it doesn't actually work because we also pass Javadoc the _JDK_ sources (so that `{@inheritDoc}` works better), which naturally can target whichever version of the JDK we're building with.

### Error Prone

While Error Prone is mostly usable [on JDK11+](https://errorprone.info/docs/installation), some of its checks have [problems under some versions](https://github.com/google/error-prone/issues/3540), at least when they're reporting warnings.

This stems from its use of part of the Checker Framework, which [doesn't support JDKs in the gap between 11 and 17](https://github.com/typetools/checker-framework/blob/c2d16b3409000ac2e2ca95b8b81ae11e42195308/framework/src/main/java/org/checkerframework/framework/source/SourceChecker.java#L553-L554). And specifically,  it looks like the Checker Framework is [trying to look up `BindingPatternTree` under any JDK12+](https://github.com/typetools/checker-framework/blob/c2d16b3409000ac2e2ca95b8b81ae11e42195308/javacutil/src/main/java/org/checkerframework/javacutil/TreeUtils.java#L131-L144). But `BindingPatternTree` (besides not being present at all [until JDK14](https://github.com/openjdk/jdk/commit/229e0d16313b10932b9ce7506d84096696983699#diff-3db4b0ce4411c851bcf75d92ef4dadc7351debcf0f9b2c2623dc513923b45867R41)) didn't declare that method [until JDK16](https://github.com/openjdk/jdk/commit/18bc95ba51b6864150c28985e65b6f784ea8ee2c#diff-3db4b0ce4411c851bcf75d92ef4dadc7351debcf0f9b2c2623dc513923b45867R39).

Anyway, the problem we saw was [a `NoSuchMethodException` during the `AbstractReferenceEquality` call to `NullnessAnalysis.getNullness`](https://oss-fuzz-build-logs.storage.googleapis.com/log-a9d04aa2-8b5a-47ca-8066-7e6b38548064.txt), which uses Checker Framework dataflow.

To address that, I disabled Error Prone for the versions under which I'd expect the `BindingPatternTree` code to be a problem.

(I also disabled it for JDK10: As noted above, Error Prone [supports JDK11+](https://errorprone.info/docs/installation). And as noted further above, Maven doesn't get far enough with JDK10 to even start running Error Prone.)

Fixes https://github.com/google/guava/issues/5801

RELNOTES=n/a
PiperOrigin-RevId: 488902996

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[bf23f3662c...](https://github.com/treckstar/yolo-octo-hipster/commit/bf23f3662c411dc8ad500efd6bf57a4dadb48a54)
#### Sunday 2022-11-20 12:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [GeoB99/reactos](https://github.com/GeoB99/reactos)@[1f4cd525ca...](https://github.com/GeoB99/reactos/commit/1f4cd525cac8663d61d5958c65e811278d6cdaaf)
#### Sunday 2022-11-20 17:00:21 by George Bișoc

[SDK][CMLIB] Implement log transaction writes & Resuscitation

=== DOCUMENTATION REMARKS ===

This implements (also enables some parts of code been decayed for years) the transacted writing of the registry. Transacted writing (or writing into registry in a transactional way) is an operation that ensures the successfulness can be achieved by monitoring two main points.
In CMLIB, such points are what we internally call them the primary and secondary sequences. A sequence is a numeric field that is incremented each time a writing operation (namely done with the FileWrite function and such) has successfully completed.

The primary sequence is incremented to suggest that the initial work of syncing the registry is in progress. During this phase, the base block header is written into the primary hive file and registry data is being written to said file in form of blocks. Afterwards the seconady sequence
is increment to report completion of the transactional writing of the registry. This operation occurs in HvpWriteHive function (invoked by HvSyncHive for syncing). If the transactional writing fails or if the lazy flushing of the registry fails, LOG files come into play.

Like HvpWriteHive, LOGs are updated by the HvpWriteLog which writes dirty data (base block header included) to the LOG themselves. These files serve for recovery and emergency purposes in case the primary machine hive has been damaged due to previous forced interruption of writing stuff into
the registry hive. With specific recovery algorithms, the data that's been gathered from a LOG will be applied to the primary hive, salvaging it. But if a LOG file is corrupt as well, then the system will perform resuscitation techniques by reconstructing the base block header to reasonable values,
reset the registry signature and whatnot.

This work is an inspiration from PR #3932 by mrmks04 (aka Max Korostil). I have continued his work by doing some more tweaks and whatnot. In addition to that, the whole transaction writing code is documented.

=== IMPORTANT NOTES ===

HvpWriteLog -- Currently this function lacks the ability to grow the log file size since we pretty much lack the necessary code that deals with hive shrinking and log shrinking/growing as well. This part is not super critical for us so this shall be left as a TODO for future.

HvLoadHive -- Currently there's a hack that prevents us from refactoring this function in a proper way. That is, we should not be reading the whole and prepare the hive storage using HvpInitializeMemoryHive which is strictly used for HINIT_MEMORY but rather we must read the hive file block by block
and deconstruct the read buffer from the file so that we can get the bins that we read from the file. With the hive bins we got the hive storage will be prepared based on such bins. If one of the bins is corrupt, self healing is applied in such scenario.

For this matter, if in any case the hive we'll be reading is corrupt we could potentially read corrupt data and lead the system into failure. So we have to perform header and data recovery as well before reading the whole hive.

---
## [mc-oofert/tgstation](https://github.com/mc-oofert/tgstation)@[3c187487b1...](https://github.com/mc-oofert/tgstation/commit/3c187487b1884040608ba23b0a89aa8b0176c2aa)
#### Sunday 2022-11-20 17:09:21 by MrMelbert

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
## [LunarWatcher/Spaceport](https://github.com/LunarWatcher/Spaceport)@[e72f503eac...](https://github.com/LunarWatcher/Spaceport/commit/e72f503eacf094969a4a1dd75d45c84755c128a3)
#### Sunday 2022-11-20 17:41:13 by Olivia

Huge amounts of styling

God fucking damn I hate CSS

---
## [Lazar-Ilic/Lazar](https://github.com/Lazar-Ilic/Lazar)@[aba38b8b9c...](https://github.com/Lazar-Ilic/Lazar/commit/aba38b8b9cbd887372048d029f4c2745ed59ac14)
#### Sunday 2022-11-20 17:44:50 by Lazar-Ilic

Delete High Resolution Music 04 Flexing Getting High On Humans Dazzling Girls With Gold White Blood Little Tigers We're Magnificent Artists.png

---
## [SilverBestRival/silver](https://github.com/SilverBestRival/silver)@[1cca85f46d...](https://github.com/SilverBestRival/silver/commit/1cca85f46d8c36de32443a6bd4cc427f3ae06d58)
#### Sunday 2022-11-20 17:47:06 by !!Silver

Update README.md

Some information 'bout me 😋

  -----------------------------------------------------------------------------------------------------------------------------------------------------

--! My name is Silver n i go by He/They

-----------------------------------------------------------------------------------------------------------------------------------------------------
What my statuses mean

Busy :                            Probably offtab but still online
Away : i probably         fell asleep on ya sorry (or im just afk)
Looking for chat :        feelin unusually social 
looking for rp      :        exactly what it says ????

-----------------------------------------------------------------------------------------------------------------------------------------------------

DNI list
danganronpa or genshin player (if ur a friend ur fine)
basic dni criteria (racist, homophobic, etc)
people who call everything i talk or like mid for no reason (i hate yall with a burning passion let me like what i like just cause i like serena doesnt mean u gotta call her mid 😔 )
people who sexualize pokemon,,, get out.
people who make fatherless jokes /j
fnf motherfuckers i dont like yall sorry when i see you its on sight /j (just dont come up to me saying "so cold..." if ur a lost silver tf u want me to do respectfully

-----------------------------------------------------------------------------------------------------------------------------------------------------

INT PLEASE
Pokemon fan/enjoyer (ESPECIALLY IF YOU LIKE HOP SILVER CLEMONT I LOVE THEM AHBJFSDBHFJIKS
ARTISTS I LOVE YALL 
just anyone whos decent tbh

-----------------------------------------------------------------------------------------------------------------------------------------------------

im kind of introverted so dont mind it if im quiet i have a hard time finding anything to say during conversation 💀

---
## [Space-Boy-Industries/game-off-2022](https://github.com/Space-Boy-Industries/game-off-2022)@[c08307a189...](https://github.com/Space-Boy-Industries/game-off-2022/commit/c08307a189a0e9e47d237ef8d3e3ada69b00855b)
#### Sunday 2022-11-20 18:15:31 by Eric Sexton

Merge pull request #9 from Space-Boy-Industries/feature/3-striles-you-die

3 life you out

---
## [k21971/notdNetHack](https://github.com/k21971/notdNetHack)@[f260cde5a4...](https://github.com/k21971/notdNetHack/commit/f260cde5a426d936bca18ebbc6a22ee051cbd96d)
#### Sunday 2022-11-20 18:37:54 by chris

Monster healing fixes

Make one mhp > mhpmax check at end
-Fixes overhealing bug

Re-order mspec cooldown and digestion to start instead of end
-Fixes a bug where Lomya wouldn't get counted in degeneration cases.
-Reduces redundancy in special cases
-Does mean that if a monster dies from degeneration its cooldowns will still have ticked. This seems fine to me.

Switch some cases of == 0 to <= 0
-I don't think this could cause a bug, but better safe than sorry.

Re-order cases so that it goes magic healing->damaging effects->degeneration->natural effects.
-Degeneration was blocking Lolth's clouds and Cthulhu's mind blasts.
-Degeneration is defined as blocking natural healing
--Only one Degen case will take effect, due to early returns. Perhaps this should be considered a bug?

---
## [mcmityler/StorytellingGame](https://github.com/mcmityler/StorytellingGame)@[9fde8a8d2b...](https://github.com/mcmityler/StorytellingGame/commit/9fde8a8d2ba90a70de685384fb588851eea4232f)
#### Sunday 2022-11-20 19:21:35 by mcmityler

V0.1.3

Final Update Changelog:
- Added new fonts to make sure they are all 100% free to use
- Added new words to dictionary: Sun, Cup, Hat, Map, Can, Leg, Bed, Rain, Star, Road, Camel, Penguin, Cloud, Happy, Sad, Ball, Slide, Mood, Bird, Lips
	Kitchen, Nose, Water, Barn, House, Saturn, Rainbow, Alligator, Dolphin, Present, Rabbit, Glasses, Morning, Night, Sleep, Peanut
- Added how to play to the help screen chalkboard
- Removed Text displaying if there was sound or not and replaced it with a sound telling what sound isnt there.
- Added background to game screen with a fade.
- Added a tutorial that shows up first time playing the game
- Updated shop to make cheat button easier to see and makes to so it also unlocks the last two cursors.
- Added sound for Camel, Penguin, rain, no sound sound, Road, Rabbit, Alligator, Dolphin, Bed, Sad, Cake, Bird, Lips, Stars, Nose, Sleep, Water, Kitchen, Barn, Ball, Peanut
- Enabled BG music

---
## [chrmhoffmann/android_kernel_google_wahoo](https://github.com/chrmhoffmann/android_kernel_google_wahoo)@[a6dfa182c4...](https://github.com/chrmhoffmann/android_kernel_google_wahoo/commit/a6dfa182c46574024870f8275d54ec546f6b0d6e)
#### Sunday 2022-11-20 20:34:24 by Christian Brauner

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
## [Wozberry12/DesigningCritMoves](https://github.com/Wozberry12/DesigningCritMoves)@[f4727bfd46...](https://github.com/Wozberry12/DesigningCritMoves/commit/f4727bfd4666af0d93b945808ef1d3cc34d0409c)
#### Sunday 2022-11-20 22:07:37 by Benjamin Kamide

Forgive me for just pushing straight to master im sick of this branch shit on jah

---
## [coreynguyen/RE4_Utility](https://github.com/coreynguyen/RE4_Utility)@[f4efec86d6...](https://github.com/coreynguyen/RE4_Utility/commit/f4efec86d68e5193b222ca1c33e21a51f419908d)
#### Sunday 2022-11-20 23:11:29 by Corey

New FBX Class and UI Started

I scarped my old FBX Class and prototyped a new one in maxscript which I have now ported into c++. However, I wasn't able to adapt the node graph for the deflation decompression. So zlib is used instead and I also use a c++ wrapper called zlibComplete to make it easier for me to implement support into my FBX class.
I also tried to add LFS decompression support based on Emoose's re4lfs tool.. but for some reason I can't even port his code into my own. So I'll likely just end up wrapping around his EXE at some point. but for now, LFS decompression is not supported within my tool.

Early work on the User Interface started, the layout is copied directly from another tool called OLK Explorer by cipher. I liked the compact and minimalist nature of the layout so I've tried to mimic that using FLTK. I'll modify and change the UI as things evolve and move forward. Right now, I just want to show the sub-blocks in the UDAS in a tree view so the user can right click and exchange them. There will also be an info pane just to print basic file data like block addresses and sizes.

That all being said there have been quite a bit more dependencies added now. So, I've created a folder containing them all including a clone of their repository, license, and site URL.

I compiled under minGW /GCC so all the libraries in the lib folder are *.a files, you'll need to recompile the sources in the dependencies folder if you want to use MSVC or something else..

Some other notes:
Recently nvidia released their new GPU, the RTX 4090 along with a toolkit for modding DX9 games called RTX Remix which is coming soon.
https://www.nvidia.com/en-us/geforce/rtx-remix/
This is a MAJOR game changer, as it removes the need for reverse engineering games and making tools to edit their files.

Since RE4 is a DX9 game RTX Remix will work on it, so it really brings into question if I should continue work on my tool. Factoring in the new release of RE4 Remake is only a few months out also means that interest in the classic will be dead soon.
Based on all recent events I believe that my focus will shift and I may move onto doing other things. However, the RE4 Utility represents all the combine knowledge I’ve learned over the years self teaching myself programing and reverse engineering. For now the project acts as a repository of the file formats and reversed ands that’s the least I wanted to provide to the community and I’m so proud of that.

Also by the way I want to credit Emoose and nipkownix whom provide symbol names that I was able to apply to some of re4 structs. This helped make sense of the variables we previously had no clue about. In addition, boubouv12 whom shared the resident evil 4 iso’s for the trial, debug, and dev versions of the gamecube game over on moddb.com
The debug menu in RE4 GC was essential in figuring out most of the file formats and creating accurate file structures for the game.
-Corey

---
## [50471736/gh1](https://github.com/50471736/gh1)@[68a715995c...](https://github.com/50471736/gh1/commit/68a715995c9102d74354d4a855d182fab91d19a5)
#### Sunday 2022-11-20 23:42:39 by Retsam Teppup

Merge pull request #1 from 50471736/branch1

Update README.md (new fuck you)

---

