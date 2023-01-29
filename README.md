## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-01-28](docs/good-messages/2023/2023-01-28.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,804,757 were push events containing 2,588,555 commit messages that amount to 157,880,918 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 27 messages:


## [Nerev4r/Skyrat-tg](https://github.com/Nerev4r/Skyrat-tg)@[406b6870bd...](https://github.com/Nerev4r/Skyrat-tg/commit/406b6870bd28dd78e65e59787d8c54c776078019)
#### Saturday 2023-01-28 00:10:59 by SkyratBot

[MIRROR] adds atmospheric gloves, small resprite of firefighter gear, repaths stupid glove paths [MDB IGNORE] (#18785)

* adds atmospheric gloves, small resprite of firefighter gear, repaths stupid glove paths (#72736)

repaths a lot of gloves off /color because they were incredibly stupid
firefighter gear has gotten an update (it doesnt cover hands anymore
though, you need something else)
firefighter helmets no longer hide your mask or glasses

![image](https://user-images.githubusercontent.com/23585223/212542599-c004d0e4-c141-40b4-a1bb-c838f9893c4b.png)
fixed engine goggles starting with darkness vision
to the atmos lockers adds atmospheric gloves, a pair of thick (chunky
fingers) gloves that are fireproof and fire protective, slightly shock
resistant and let you fireman carry people faster.
atmospheric firefighter helmets now are a subtype of welding hardhats,
you can enable a welding visor.
welding hardhats change mode with right click instead of altclick

im not a good spriter but i think this resprite makes them fit nicer
with other engi equipment
lets me firefighter rp

:cl:
add: Atmospheric Gloves, thick gloves that are fully fireproof and fire
protective and let you fireman carry people faster.
fix: fixes engine goggles starting with darkness vision
qol: firefighter helmets can now enable a welding visor
qol: welding hardhats change mode with right click instead of altclick
balance: firesuits no longer protect your hands
/:cl:

* Makes shit compile

* Updates the digi and snouted stuff to match the new sprites (thanks Halcyon!)

* Fixes a whole ton more issues that popped up

---------

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>
Co-authored-by: GoldenAlpharex <jerego1234@hotmail.com>

---
## [cd-public/eths23](https://github.com/cd-public/eths23)@[9b461456e9...](https://github.com/cd-public/eths23/commit/9b461456e9f8168c833c0c36040638103a246b4e)
#### Saturday 2023-01-28 00:56:15 by Mitchell Everetts

Addition of my url to the page

I thought I had done this twice already, but I was clearly having some kind of fever dream because not only was it not there, I checked my own fork and it wasn't updated, which has led me to the conclusion that I, in an out of body homework induced experienced, edited my repository in the spirit realm and thus the changes were not reflected in the material realm. 

Signed-off-by: Mitchell Everetts <77137408+Metvertz@users.noreply.github.com>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[ae08395328...](https://github.com/tgstation/tgstation/commit/ae08395328672ee40c5abb7f2bd1452bb932d6d4)
#### Saturday 2023-01-28 01:23:22 by san7890

Syndicate Bomb Core Payloads Can Only Be Triggered via the Bomb (#72986)

## About The Pull Request

Basically, you can't extract the bomb core, slap a 10-second c4 on it/on
the shell/and run off having triggered an incredibly powerful explosion.
This is accomplished by having the syndicate bomb override ex_act (it
will be deleted if the explosion goes off), as well as the payload
itself being subtyped into something resistant to bombs and burning.

In-universe, this is described as the shell being quite resistant to
forms of external explosive force- but if any explosive force comes from
within the bomb's shell: kabloom. The bombcore itself has been
redesigned (in a rare moment of non-ineptude) by Donk Co., who has
redesigned the bomb core payload from the ground up- meaning that it can
only be detonated electronically by an impulse from the bomb machinery.
Cutting the wrong wire and attempting to get rid of the bomb by hitting
it with an axe or something will still cause it to blow up, but you know
how those things can be.
## Why It's Good For The Game

I feel like the point of the syndicate bomb is to be a threat for the
crew to match up against. I want a clown in bomb squad gear to head out
to the site and sweat trying to figure out which wire it is, until....
KA-BLHONK: red mist. Or, I want some "helpful" assistant to interrupt
someone's session by going "I KNOW WHAT WIRE IT IS", and having those
odds of either blowing everyone around them up or actually saving the
day.

Being able to detonate something that was balanced and designed to have
_at least_ one minute and a half in **10 SECONDS** is just so injurious
to the game. You can buy a shitload of these bombs, extract the cores,
slap c4 on it and go around the station doling out some serious
explosions. You can run into medbay, wrench it down, slap a c4 on it AND
NO ONE CAN DO ANYTHING ABOUT IT! They can't cut wires, they can't figure
it out to save the day, all they can do is run. Running from danger is
fine and acceptable, but it's just completely stacked against the crew
in a way that I feel needs to be rectified somehow.

I like the idea of purposefully fucking with the wires on the spot so
you sacrificially kill everyone, that feels quite fair to me. I just
simply don't like the fact that you can waltz around the station
punching huge gaps in the hull (remember, putting c4 on the bomb core
itself would cause it to go kabloom) with nearly nothing as far as risk.
It's way too rewarding for something very easy to accomplish (there's a
reason why it's 90 seconds- it's not meant to be easy to accomplish).

This doesn't affect base bombcore behavior, just the explodey ones that
come standard in syndicate bombs.
## Changelog
:cl:
balance: After an unfortunate event occuring when some nuclear
operatives took the ship to a Fireworks Store, the Syndicate have
re-engineered their bomb cores to only explode when electronically
triggered by the bomb shell itself. The payload inside a standard
syndicate bomb can not be exploded with another explosion, you must keep
it in the bomb machinery for it to actually do some explodey stuff.
/:cl:

---
## [MicroWorldwide/SS13-TG-station](https://github.com/MicroWorldwide/SS13-TG-station)@[9e69e5d6ac...](https://github.com/MicroWorldwide/SS13-TG-station/commit/9e69e5d6acae10bf0941155c418ea3b9194668e5)
#### Saturday 2023-01-28 01:35:25 by LemonInTheDark

Minor plane cube cleanup (#72038)

## About The Pull Request

[Fixes area lighting not working on turf change in multiz
cases](https://github.com/tgstation/tgstation/commit/7b92deffbca92a834cb0a361fd685de51a12ea53)

If you modify a area lit turf when using multiz, it'd end up using the
wrong plane for its light, because of stupid shit on my part.
Stupid shit resolved

[Fixes some uses of plane masters that only specified one rather then
all](https://github.com/tgstation/tgstation/commit/a59ec96d29710b967bf8b3ffe8210b230cb194b3)

We almost never only want to show SOME hidden planes. 
Should really make a helper for this someday

---
## [DannyBoy3642/tgstation](https://github.com/DannyBoy3642/tgstation)@[10a344bde0...](https://github.com/DannyBoy3642/tgstation/commit/10a344bde0d48fb250dcb7a9eb4a1e98b9bb6df5)
#### Saturday 2023-01-28 02:31:52 by Time-Green

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
## [Floofies/tgstation](https://github.com/Floofies/tgstation)@[36090c1b20...](https://github.com/Floofies/tgstation/commit/36090c1b206dee8b643e83607e333c29906b6bc8)
#### Saturday 2023-01-28 02:39:58 by san7890

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
## [Floofies/tgstation](https://github.com/Floofies/tgstation)@[5e80257423...](https://github.com/Floofies/tgstation/commit/5e802574231c9c6fe835c40b55f2c8aa9f1c68b4)
#### Saturday 2023-01-28 02:39:58 by Jeremiah

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
## [michaeldelago/azerothcore-wotlk](https://github.com/michaeldelago/azerothcore-wotlk)@[ef949f9ff0...](https://github.com/michaeldelago/azerothcore-wotlk/commit/ef949f9ff0a89e837c67258d7e199da1706bc438)
#### Saturday 2023-01-28 03:28:41 by ICXCNIKA

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
## [Miiyo/android_kernel_sony_sdm845](https://github.com/Miiyo/android_kernel_sony_sdm845)@[2380e494d2...](https://github.com/Miiyo/android_kernel_sony_sdm845/commit/2380e494d2527d69c09b61c654d5b327dd9a30c7)
#### Saturday 2023-01-28 06:47:25 by tanish2k09

Introducing KLapse - A kernel level livedisplay module v4.0:

Author: @tanish2k09 (email: tanish2k09.dev@gmail.com)

What is it?
Kernel-based Lapse ("K-Lapse") is a linear RGB scaling module that 'shifts' RGB based on time (of the day/selected by user), or (since v2.0) brightness. This concept is inspired from
LineageOS (formerly known as 'CyanogenMod') ROM's feature "livedisplay" which also changes the display settings (RGB, hue, temperature, etc) based on time.

Why did you decide to make this? (Tell me a story).
I (personally) am a big fan of the livedisplay feature found on LineageOS ROM. I used it every single day, since Android Lollipop. Starting from Android Nougat, a native night mode
solution was added to AOSP and it felt like livedisplay was still way superior, thanks to its various options (you could say it spoiled me, sure). I also maintained a kernel (Venom
kernel) for the device I was using at that time. It was all good until the OEM dropped support for the device at Android M, and XDA being XDA, was already working on N ROMs. The issue
was, these ROMs weren't LineageOS or based on it, so livedisplay was... gone. I decided I'll try to bring that feature to every other ROM. How would I do that? Of course! The kernel! It
worked on every single ROM, it was the key! I started to work on it ASAP and here it is, up on GitHub, licensed under GPL (check klapse.c), open to everyone :)

How does it work?
Think of it like a fancy night mode, but not really. Klapse is dependent on an RGB interface (like Gamma on MTK and KCAL on SD chipsets). It fetches time from the kernel, converts it to
local time, and selects and RGB set based on the time. The result is really smooth shifting of RGB over time.

How does it really work (dev)?
Klapse mode 1 (time-based scaling) uses a method void klapse_pulse(void) that should ideally be called every minute. This can be done by injecting a pulse call inside another method that
is called repeatedly naturally, like cpufreq or atomic or frame commits. It can be anything, whatever you like, even a kthread, as long as it is called repeatedly naturally. To execute
every 60 seconds, use jiffies or ktime, or any similar method. The pulse function fetches the current time and makes calculations based on the current hour and the values of the tunables
listed down below.

Klapse mode 2 (brightness-based scaling) uses a method void set_rgb_slider(<type> bl_lvl) where is the data type of the brightness level used in your kernel source. (OnePlus 6 uses u32
data type for bl_lvl) set_rgb_slider needs to be called/injected inside a function that sets brightness for your device. (OnePlus 6 uses dsi_panel.c for that, check out the diff for that
file in /op6)

What all stuff can it do?

1, Emulate night mode with the proper RGB settings
2, Smoothly scale from one set of RGB to another set of RGB in integral intervals over time.
3, Reduce perceived brightness using brightness_factor by reducing the amount of color on screen. Allows lower apparent brightness than system permits.
4, Scale RGB based on brightness of display (low brightness usually implies a dark environment, where yellowness is probably useful).
5, Automate the perceived brightness independent of whether klapse is enabled, using its own set of start and stop hours.
6, Be more efficient,faster by residing inside the kernel instead of having to use the HWC HAL like android's night mode.
7, (On older devices) Reduce stuttering or frame lags caused by native night mode.
8, An easier solution against overlay-based apps that run as service in userspace/Android and sometimes block apps asking for permissions.
9, Give you a Livedisplay alternative if it doesn't work in your ROM.
10, Impress your crush so you can get a date (Hey, don't forget to credit me if it works).

Alright, so this is a replacement for night mode?
NO! Not at all. One can say this is merely an alternative for LineageOS' Livedisplay, but inside a kernel. Night mode is a sub-function of both Livedisplay and KLapse. Most comparisons
here were made with night mode because that's what an average user uses, and will relate to the most. There is absolutely no reason for your Android kernel to not have KLapse. Go ahead
and add it or ask your kernel maintainer to. It's super-easy!

What can it NOT do (yet)?

1, Calculate scaling to the level of minutes, like "Start from 5:37pm till 7:19am". --TODO
2, Make coffee for you.
3, Fly you to the moon. Without a heavy suit.
4, Get you a monthly subscription of free food, cereal included.

All these following tunables are found in their respective files in /sys/klapse/

1. enable_klapse : A switch to enable or disable klapse. Values : 0 = off, 1 = on (since v2.0, 2 = brightness-dependent mode)
2. klapse_start_hour : The hour at which klapse should start scaling the RGB values from daytime to target (see next points). Values : 0-23
3. klapse_stop_hour : The hour by which klapse should scale back the RGB values from target to daytime (see next points). Values : 0-23
4. daytime_rgb : The RGB set that must be used for all the time outside of start and stop hour range.
5. target_rgb : The RGB set that must be scaled towards for all the time inside of start and stop hour range.
6. klapse_scaling_rate : Controls how soon the RGB reaches from daytime to target inside of start and stop hour range. Once target is reached, it remains constant till 30 minutes before
   stop hour, where target RGB scales back to daytime RGB.
7. brightness_factor : From the name itself, this value has the ability to bend perception and make your display appear as if it is at a lesser brightness level than it actually is at.
   It works by reducing the RGB values by the same factor. Values : 2-10, (10 means accurate brightness, 5 means 50% of current brightness, you get it)
8. brightness_factor_auto : A switch that allows you to automatically set the brightness factor in a set time range. Value : 0 = off, 1 = on
9. brightness_factor_auto_start_hour : The hour at which brightness_factor should be applied. Works only if #8 is 1. Values : 0-23
10. brightness_factor_auto_stop_hour : The hour at which brightness_factor should be reverted to 10. Works only if #8 is 1. Values : 0-23
11. backlight_range : The brightness range within which klapse should scale from daytime to target_rgb. Works only if #1 is 2. Values : MIN_BRIGHTNESS-MAX_BRIGHTNESS

Signed-off-by: Eliminater74 <eliminater74@gmail.com>
Signed-off-by: energyspear17 <energyspear17@gmail.com>
Signed-off-by: Michael <loukerismichalis@gmail.com>
Signed-off-by: PainKiller3 <ninadpatil100@gmail.com>

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[e9e5342217...](https://github.com/git-for-windows/git/commit/e9e53422177b0f27404f916f091f81eba46dc904)
#### Saturday 2023-01-28 07:20:18 by Johannes Schindelin

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
## [Danda420/kernel_xiaomi_sm8250](https://github.com/Danda420/kernel_xiaomi_sm8250)@[ff4e49374b...](https://github.com/Danda420/kernel_xiaomi_sm8250/commit/ff4e49374b034ae4f5630740def930a19265eb5f)
#### Saturday 2023-01-28 08:10:01 by Wang Han

power: Introduce OnePlus 3 fingerprintd thaw hack

Taken from Oneplus 3, this hack will make fingerprintd recover from suspend quickly.

Small fixes for newer kernels since we're coming from 3.10.108..

Change-Id: I0166e82d51a07439d15b41dbc03d7e751bfa783b
Co-authored-by: Cyber Knight <cyberknight755@gmail.com>
[cyberknight777: forwardport and adapt to 4.14]
Signed-off-by: Shreyansh Lodha <slodha96@gmail.com>
Signed-off-by: Pierre2324 <pdbbasketball@gmail.com>
Signed-off-by: PainKiller3 <ninadpatil100@gmail.com>
Signed-off-by: Dhruv <dhruvgera61@gmail.com>
Signed-off-by: Cyber Knight <cyberknight755@gmail.com>

---
## [YBIFoundation/Dataset](https://github.com/YBIFoundation/Dataset)@[3d16e349a8...](https://github.com/YBIFoundation/Dataset/commit/3d16e349a835f0ba6e0969bff50e72906037fff2)
#### Saturday 2023-01-28 08:35:02 by Dr. Alok Yadav

Add files via upload

https://www.kaggle.com/datasets/miroslavsabo/young-people-survey?select=columns.csv

Introduction
In 2013, students of the Statistics class at FSEV UK were asked to invite their friends to
participate in this survey.

The data file (responses.csv) consists of 1010 rows and 150 columns (139
integer and 11 categorical).
For convenience, the original variable names were shortened in the
data file. See the columns.csv file if you want to match the data with the original names.
The data contain missing values.
The survey was presented to participants in both electronic and written form.
The original questionnaire was in Slovak language and was later translated
into English.
All participants were of Slovakian nationality, aged between 15-30.
The variables can be split into the following groups:

Music preferences (19 items)
Movie preferences (12 items)
Hobbies & interests (32 items)
Phobias (10 items)
Health habits (3 items)
Personality traits, views on life, & opinions (57 items)
Spending habits (7 items)
Demographics (10 items)
Research questions
Many different techniques can be used to answer many questions, e.g.

Clustering: Given the music preferences, do people make up
any clusters of similar behavior?
Hypothesis testing: Do women fear certain phenomena
significantly more than men? Do the left handed people have different
interests than right handed?
Predictive modeling: Can we predict spending habits of a person
from his/her interests and movie or music preferences?
Dimension reduction: Can we describe a large number of human
interests by a smaller number of latent concepts?
Correlation analysis: Are there any connections between music and
movie preferences?
Visualization: How to effectively visualize a lot of variables
in order to gain some meaningful insights from the data?
(Multivariate) Outlier detection: Small number of participants often cheats and randomly answers the questions. Can you identify them? Hint: Local outlier factor may help.
Missing values analysis: Are there any patterns in missing responses? What is the optimal way of imputing the values in surveys?
Recommendations: If some of user's interests are known, can we predict the other? Or, if we know what a person listen, can we predict which kind of movies he/she might like?
Past research
(in slovak) Sleziak, P. - Sabo, M.: Gender differences in the prevalence of specific phobias. Forum Statisticum Slovacum. 2014, Vol. 10, No. 6. [Differences (gender + whether people lived in village/town) in the prevalence of phobias.]

Sabo, Miroslav. Multivariate Statistical Methods with Applications. Diss. Slovak University of Technology in Bratislava, 2014. [Clustering of variables (music preferences, movie preferences, phobias) + Clustering of people w.r.t. their interests.]

Questionnaire
MUSIC PREFERENCES
I enjoy listening to music.: Strongly disagree 1-2-3-4-5 Strongly agree (integer)
I prefer.: Slow paced music 1-2-3-4-5 Fast paced music (integer)
Dance, Disco, Funk: Don't enjoy at all 1-2-3-4-5 Enjoy very much (integer)
Folk music: Don't enjoy at all 1-2-3-4-5 Enjoy very much (integer)
Country: Don't enjoy at all 1-2-3-4-5 Enjoy very much (integer)
Classical: Don't enjoy at all 1-2-3-4-5 Enjoy very much (integer)
Musicals: Don't enjoy at all 1-2-3-4-5 Enjoy very much (integer)
Pop: Don't enjoy at all 1-2-3-4-5 Enjoy very much (integer)
Rock: Don't enjoy at all 1-2-3-4-5 Enjoy very much (integer)
Metal, Hard rock: Don't enjoy at all 1-2-3-4-5 Enjoy very much (integer)
Punk: Don't enjoy at all 1-2-3-4-5 Enjoy very much (integer)
Hip hop, Rap: Don't enjoy at all 1-2-3-4-5 Enjoy very much (integer)
Reggae, Ska: Don't enjoy at all 1-2-3-4-5 Enjoy very much (integer)
Swing, Jazz: Don't enjoy at all 1-2-3-4-5 Enjoy very much (integer)
Rock n Roll: Don't enjoy at all 1-2-3-4-5 Enjoy very much (integer)
Alternative music: Don't enjoy at all 1-2-3-4-5 Enjoy very much (integer)
Latin: Don't enjoy at all 1-2-3-4-5 Enjoy very much (integer)
Techno, Trance: Don't enjoy at all 1-2-3-4-5 Enjoy very much (integer)
Opera: Don't enjoy at all 1-2-3-4-5 Enjoy very much (integer)
MOVIE PREFERENCES
I really enjoy watching movies.: Strongly disagree 1-2-3-4-5 Strongly agree (integer)
Horror movies: Don't enjoy at all 1-2-3-4-5 Enjoy very much (integer)
Thriller movies: Don't enjoy at all 1-2-3-4-5 Enjoy very much (integer)
Comedies: Don't enjoy at all 1-2-3-4-5 Enjoy very much (integer)
Romantic movies: Don't enjoy at all 1-2-3-4-5 Enjoy very much (integer)
Sci-fi movies: Don't enjoy at all 1-2-3-4-5 Enjoy very much (integer)
War movies: Don't enjoy at all 1-2-3-4-5 Enjoy very much (integer)
Tales: Don't enjoy at all 1-2-3-4-5 Enjoy very much (integer)
Cartoons: Don't enjoy at all 1-2-3-4-5 Enjoy very much (integer)
Documentaries: Don't enjoy at all 1-2-3-4-5 Enjoy very much (integer)
Western movies: Don't enjoy at all 1-2-3-4-5 Enjoy very much (integer)
Action movies: Don't enjoy at all 1-2-3-4-5 Enjoy very much (integer)
HOBBIES & INTERESTS
History: Not interested 1-2-3-4-5 Very interested (integer)
Psychology: Not interested 1-2-3-4-5 Very interested (integer)
Politics: Not interested 1-2-3-4-5 Very interested (integer)
Mathematics: Not interested 1-2-3-4-5 Very interested (integer)
Physics: Not interested 1-2-3-4-5 Very interested (integer)
Internet: Not interested 1-2-3-4-5 Very interested (integer)
PC Software, Hardware: Not interested 1-2-3-4-5 Very interested (integer)
Economy, Management: Not interested 1-2-3-4-5 Very interested (integer)
Biology: Not interested 1-2-3-4-5 Very interested (integer)
Chemistry: Not interested 1-2-3-4-5 Very interested (integer)
Poetry reading: Not interested 1-2-3-4-5 Very interested (integer)
Geography: Not interested 1-2-3-4-5 Very interested (integer)
Foreign languages: Not interested 1-2-3-4-5 Very interested (integer)
Medicine: Not interested 1-2-3-4-5 Very interested (integer)
Law: Not interested 1-2-3-4-5 Very interested (integer)
Cars: Not interested 1-2-3-4-5 Very interested (integer)
Art: Not interested 1-2-3-4-5 Very interested (integer)
Religion: Not interested 1-2-3-4-5 Very interested (integer)
Outdoor activities: Not interested 1-2-3-4-5 Very interested (integer)
Dancing: Not interested 1-2-3-4-5 Very interested (integer)
Playing musical instruments: Not interested 1-2-3-4-5 Very interested (integer)
Poetry writing: Not interested 1-2-3-4-5 Very interested (integer)
Sport and leisure activities: Not interested 1-2-3-4-5 Very interested (integer)
Sport at competitive level: Not interested 1-2-3-4-5 Very interested (integer)
Gardening: Not interested 1-2-3-4-5 Very interested (integer)
Celebrity lifestyle: Not interested 1-2-3-4-5 Very interested (integer)
Shopping: Not interested 1-2-3-4-5 Very interested (integer)
Science and technology: Not interested 1-2-3-4-5 Very interested (integer)
Theatre: Not interested 1-2-3-4-5 Very interested (integer)
Socializing: Not interested 1-2-3-4-5 Very interested (integer)
Adrenaline sports: Not interested 1-2-3-4-5 Very interested (integer)
Pets: Not interested 1-2-3-4-5 Very interested (integer)
PHOBIAS
Flying: Not afraid at all 1-2-3-4-5 Very afraid of (integer)
Thunder, lightning: Not afraid at all 1-2-3-4-5 Very afraid of (integer)
Darkness: Not afraid at all 1-2-3-4-5 Very afraid of (integer)
Heights: Not afraid at all 1-2-3-4-5 Very afraid of (integer)
Spiders: Not afraid at all 1-2-3-4-5 Very afraid of (integer)
Snakes: Not afraid at all 1-2-3-4-5 Very afraid of (integer)
Rats, mice: Not afraid at all 1-2-3-4-5 Very afraid of (integer)
Ageing: Not afraid at all 1-2-3-4-5 Very afraid of (integer)
Dangerous dogs: Not afraid at all 1-2-3-4-5 Very afraid of (integer)
Public speaking: Not afraid at all 1-2-3-4-5 Very afraid of (integer)
HEALTH HABITS
Smoking habits: Never smoked - Tried smoking - Former smoker - Current smoker (categorical)
Drinking: Never - Social drinker - Drink a lot (categorical)
I live a very healthy lifestyle.: Strongly disagree 1-2-3-4-5 Strongly agree (integer)
PERSONALITY TRAITS, VIEWS ON LIFE & OPINIONS
I take notice of what goes on around me.: Strongly disagree 1-2-3-4-5 Strongly agree (integer)
I try to do tasks as soon as possible and not leave them until last minute.: Strongly disagree 1-2-3-4-5 Strongly agree (integer)
I always make a list so I don't forget anything.: Strongly disagree 1-2-3-4-5 Strongly agree (integer)
I often study or work even in my spare time.: Strongly disagree 1-2-3-4-5 Strongly agree (integer)
I look at things from all different angles before I go ahead.: Strongly disagree 1-2-3-4-5 Strongly agree (integer)
I believe that bad people will suffer one day and good people will be rewarded.: Strongly disagree 1-2-3-4-5 Strongly agree (integer)
I am reliable at work and always complete all tasks given to me.: Strongly disagree 1-2-3-4-5 Strongly agree (integer)
I always keep my promises.: Strongly disagree 1-2-3-4-5 Strongly agree (integer)
I can fall for someone very quickly and then completely lose interest.: Strongly disagree 1-2-3-4-5 Strongly agree (integer)
I would rather have lots of friends than lots of money.: Strongly disagree 1-2-3-4-5 Strongly agree (integer)
I always try to be the funniest one.: Strongly disagree 1-2-3-4-5 Strongly agree (integer)
I can be two faced sometimes.: Strongly disagree 1-2-3-4-5 Strongly agree (integer)
I damaged things in the past when angry.: Strongly disagree 1-2-3-4-5 Strongly agree (integer)
I take my time to make decisions.: Strongly disagree 1-2-3-4-5 Strongly agree (integer)
I always try to vote in elections.: Strongly disagree 1-2-3-4-5 Strongly agree (integer)
I often think about and regret the decisions I make.: Strongly disagree 1-2-3-4-5 Strongly agree (integer)
I can tell if people listen to me or not when I talk to them.: Strongly disagree 1-2-3-4-5 Strongly agree (integer)
I am a hypochondriac.: Strongly disagree 1-2-3-4-5 Strongly agree (integer)
I am emphatetic person.: Strongly disagree 1-2-3-4-5 Strongly agree (integer)
I eat because I have to. I don't enjoy food and eat as fast as I can.: Strongly disagree 1-2-3-4-5 Strongly agree (integer)
I try to give as much as I can to other people at Christmas.: Strongly disagree 1-2-3-4-5 Strongly agree (integer)
I don't like seeing animals suffering.: Strongly disagree 1-2-3-4-5 Strongly agree (integer)
I look after things I have borrowed from others.: Strongly disagree 1-2-3-4-5 Strongly agree (integer)
I feel lonely in life.: Strongly disagree 1-2-3-4-5 Strongly agree (integer)
I used to cheat at school.: Strongly disagree 1-2-3-4-5 Strongly agree (integer)
I worry about my health.: Strongly disagree 1-2-3-4-5 Strongly agree (integer)
I wish I could change the past because of the things I have done.: Strongly disagree 1-2-3-4-5 Strongly agree (integer)
I believe in God.: Strongly disagree 1-2-3-4-5 Strongly agree (integer)
I always have good dreams.: Strongly disagree 1-2-3-4-5 Strongly agree (integer)
I always give to charity.: Strongly disagree 1-2-3-4-5 Strongly agree (integer)
I have lots of friends.: Strongly disagree 1-2-3-4-5 Strongly agree (integer)
Timekeeping.: I am often early. - I am always on time. - I am often running late. (categorical)
Do you lie to others?: Never. - Only to avoid hurting someone. - Sometimes. - Everytime it suits me. (categorical)
I am very patient.: Strongly disagree 1-2-3-4-5 Strongly agree (integer)
I can quickly adapt to a new environment.: Strongly disagree 1-2-3-4-5 Strongly agree (integer)
My moods change quickly.: Strongly disagree 1-2-3-4-5 Strongly agree (integer)
I am well mannered and I look after my appearance.: Strongly disagree 1-2-3-4-5 Strongly agree (integer)
I enjoy meeting new people.: Strongly disagree 1-2-3-4-5 Strongly agree (integer)
I always let other people know about my achievements.: Strongly disagree 1-2-3-4-5 Strongly agree (integer)
I think carefully before answering any important letters.: Strongly disagree 1-2-3-4-5 Strongly agree (integer)
I enjoy childrens' company.: Strongly disagree 1-2-3-4-5 Strongly agree (integer)
I am not afraid to give my opinion if I feel strongly about something.: Strongly disagree 1-2-3-4-5 Strongly agree (integer)
I can get angry very easily.: Strongly disagree 1-2-3-4-5 Strongly agree (integer)
I always make sure I connect with the right people.: Strongly disagree 1-2-3-4-5 Strongly agree (integer)
I have to be well prepared before public speaking.: Strongly disagree 1-2-3-4-5 Strongly agree (integer)
I will find a fault in myself if people don't like me.: Strongly disagree 1-2-3-4-5 Strongly agree (integer)
I cry when I feel down or things don't go the right way.: Strongly disagree 1-2-3-4-5 Strongly agree (integer)
I am 100% happy with my life.: Strongly disagree 1-2-3-4-5 Strongly agree (integer)
I am always full of life and energy.: Strongly disagree 1-2-3-4-5 Strongly agree (integer)
I prefer big dangerous dogs to smaller, calmer dogs.: Strongly disagree 1-2-3-4-5 Strongly agree (integer)
I believe all my personality traits are positive.: Strongly disagree 1-2-3-4-5 Strongly agree (integer)
If I find something the doesn't belong to me I will hand it in.: Strongly disagree 1-2-3-4-5 Strongly agree (integer)
I find it very difficult to get up in the morning.: Strongly disagree 1-2-3-4-5 Strongly agree (integer)
I have many different hobbies and interests.: Strongly disagree 1-2-3-4-5 Strongly agree (integer)
I always listen to my parents' advice.: Strongly disagree 1-2-3-4-5 Strongly agree (integer)
I enjoy taking part in surveys.: Strongly disagree 1-2-3-4-5 Strongly agree (integer)
How much time do you spend online?: No time at all - Less than an hour a day - Few hours a day - Most of the day (categorical)
SPENDING HABITS
I save all the money I can.: Strongly disagree 1-2-3-4-5 Strongly agree (integer)
I enjoy going to large shopping centres.: Strongly disagree 1-2-3-4-5 Strongly agree (integer)
I prefer branded clothing to non branded.: Strongly disagree 1-2-3-4-5 Strongly agree (integer)
I spend a lot of money on partying and socializing.: Strongly disagree 1-2-3-4-5 Strongly agree (integer)
I spend a lot of money on my appearance.: Strongly disagree 1-2-3-4-5 Strongly agree (integer)
I spend a lot of money on gadgets.: Strongly disagree 1-2-3-4-5 Strongly agree (integer)
I will hapilly pay more money for good, quality or healthy food.: Strongly disagree 1-2-3-4-5 Strongly agree (integer)
DEMOGRAPHICS
Age: (integer)
Height: (integer)
Weight: (integer)
How many siblings do you have?: (integer)
Gender: Female - Male (categorical)
I am: Left handed - Right handed (categorical)
Highest education achieved: Currently a Primary school pupil - Primary school - Secondary school - College/Bachelor degree (categorical)
I am the only child: No - Yes (categorical)
I spent most of my childhood in a: City - village (categorical)
I lived most of my childhood in a: house/bungalow - block of flats (categorical)

---
## [ginbot86/DingoCharge-Shizuku](https://github.com/ginbot86/DingoCharge-Shizuku)@[b3c7d0f242...](https://github.com/ginbot86/DingoCharge-Shizuku/commit/b3c7d0f242505452312dc2bcf6eff58ab17d485c)
#### Saturday 2023-01-28 09:42:28 by Jason Gin

Created update 1.5.0

Changed the low-current deadband threshold to activate if charge current is less than the threshold instead of less than/equal to (2023-01-01).
Updated copyright string in About screen to read "(C) 2021-2023".
Changed the default cell count to 2S for improved user experience; most PPS adapters go to 11V so a compatibility fail out of the box kinda sucks... (2023-01-06).
Changed how aggressive GC is enabled/disabled; set aggressiveGcThreshold to 0 instead of isAggressiveGcEnabled to false (not that you should do this anyway...) (2023-01-08).
Fixed issue where configuration menu libraries remain resident in memory even when no longer needed (2023-01-21).
Added LM135/LM235/LM335 support as external temperature sensors (2023-01-21).
Split off charge control function into a separate file which unloads upon termination to conserve memory (2023-01-27).
Renamed "DC4S-CompileMenu" to "DC4S-CompileLibs" to reflect that non-menu libraries are also compiled here (2023-01-27).
Changed how USB-C CC attachment errors are handled; user can retry the detection instead of needing to restart the charge setup procedure (2023-01-28).

---
## [NopemanMcHalt/coyote-bayou](https://github.com/NopemanMcHalt/coyote-bayou)@[9821251d81...](https://github.com/NopemanMcHalt/coyote-bayou/commit/9821251d8178f6ed89c4cadfec051d38beae4658)
#### Saturday 2023-01-28 09:47:07 by Superlagg

Merge pull request #1481 from ARF-SS13/Fuck-you-github

Map adjustments!

---
## [NopemanMcHalt/coyote-bayou](https://github.com/NopemanMcHalt/coyote-bayou)@[b7164095fd...](https://github.com/NopemanMcHalt/coyote-bayou/commit/b7164095fd1ad42d581cdce1b1861d180ec50323)
#### Saturday 2023-01-28 09:47:07 by Superlagg

Merge pull request #1482 from ARF-SS13/Fuck-you-github

Stinky nash gate buttons fixed

---
## [NopemanMcHalt/coyote-bayou](https://github.com/NopemanMcHalt/coyote-bayou)@[70042337db...](https://github.com/NopemanMcHalt/coyote-bayou/commit/70042337dbefb532ee9e1eb640edb00e9280c932)
#### Saturday 2023-01-28 09:47:07 by A Psycho

Merge pull request #1483 from ARF-SS13/Fuck-you-github

Small mapfixes

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[15992fa396...](https://github.com/mrakgr/The-Spiral-Language/commit/15992fa3968d45a96f6df02c78e40db2d8f3cf36)
#### Saturday 2023-01-28 12:05:34 by Marko Grdinić

"9:45am. Let me reply to that email and then I will start making screencasts.

I've been thinking what I want to do. Rather than random shit in Spiral, why don't I instead make a ML library with Cuda capabilities and do the poker agent on Paperspace. This should be my plan if nobody wants to hire me. I have an idea for an algorithm, so why don't I run with it? It will give me something to work on. It could be fun, streaming myself programming. I am just about good enough to do that now. It should raise my talking skills.

Who knows how the job hunt will go. I can never take anything for granted. Some people can take over a year and thousands applications before they get an offer. That would be a lot of time to spend out of the market. And my social skills are particularly low so I am a prime specimen for whom it might happen to.

Oh, right. In 3 days I should do a PL sub review. Maybe somebody would want me to give them a hand on their own PL.

10am. Focus me. Reply to that email, and then move on to the screencasts.

///

> Is this a hard requirement?

Yes. It would be too much for a shut-in loner like myself to move countries all of a sudden. I want to stay where I am with my parents.

> Thank you for sharing - you've worked on really cool projects! One thing I'm curious about: what was most challenging about creating Spiral?

Hmmm...it was pretty hard. Was it inventing novel features? Yes, reinventing partial evaluation on my own was quite hard. Working on a compiler with no prior experience in the field was hard. Working on a project far larger than what I've been used to previously was hard.

But I think what is hard is always the same thing, keeping the motivation up. It is like being in a war, and maintaining morale is a crucial aspect so the front line doesn't crumble. An army doesn't rout when it is near annihilation, but far before that, meaning that if you have two equally matched armies, the one that can persevere the longest will be the winner.

During the past decade, I've had to work for almost the entirety of it without any monetary compensation or encouragement from other people. My belief in my own vision is what has kept me going. I did have some intrinsic rewards though. As tough the work on Spiral has been, constantly refining and improving the language as well as my own programming skills has been satisfying. But it is not like I've been unbroken all this while. I actually gave up twice already. Once near the end of 2018 where I spent the entirety of 2019 doing random things like studying formal proofs in vain hope it would make me better at ML. And in late 2021. Since then I've been doing art, and I've only now recovered enough to do programming.

> Do UPMEM's devices fall under this umbrella? And have you considered reaching out to them to see if you could work on this for them (either full-time or contract based)? Suppose they'd be interested in having someone developing software to make their hardware easier to use.

Nothing went right for me with this company. I think I chased the lead compiler dev who initially pointed me to their simulator with my haughty attitude. And last week, I did get a reply from somebody higher up. In it he was asking me for a presentation. I sent him a little article summarizing Spiral's features and my plans for UPMEM, which are essentially nothing unless they sponsor or hire me. But my hunch is that they really want me to sell them face to face, which leaves me at a loss.

This experience is why I am going to become a Youtuber - in order to improve my talking and presentation skills. As I finish this email to you I am going to start a playlist on how to use Stable Diffusion on Paperspace. And then I am going to do a series on making an ML library and reinforcement learning in Spiral. I have an idea for a novel algorithm, and I might as well do it live this time.

> Have you thought about creating a "world" to make these experiments in that you could still run on your laptop while you wait for the new hardware to be developed and made available to individuals (I'm assuming your genetic program will output different learning algos that are then tested on "worlds" - real or simulated; a game can be a "world")? Or would that just be equivalent to using very simple games which aren't appropriate for what you're trying to accomplish?

That 'world' you are talking about was supposed to be the GVGAI port. You can see a link to it on my resume. Incidentally, if you look at the original Java library, it has many algorithms already implemented to solve such games, variants of MCTS and such. This might be of some interest to you given what you want to do. The GVGAI is a DSL for making simple games like the Atari ones, specifically made for AI agents to play in. But I want to focus on poker for the simple reason that it has very little wasted action. I see it as an ideal testbed, and even more, a superhuman poker agent could make me rich. Whereas in environments like the GVGAI ones and Atari, most of the processing time would be taken up working on irrelevant frames.

Arguably, mastering these 'irrelevant' frames is really important for real world tasks, but because it is so computationally expensive I do not want to try it before I've made headway on poker. As for why it was so hard…

> You told me that some RL experiments you tried to do on poker proved challenging to do given the limitations of the hardware you're using. What is it about poker that made it hard?

Partly my incompetence, but that I could only get my hardware to process 10,000s of hands per second instead of millions is a big part of why I failed. What kind of mistakes did I make?

Well, I knew that existing algorithms would not do it for me, so I've tried coming up with new ones. But I've approached the problem the same way I would have anything else. Whereas my approach would work for ordinary programming problems it would not have worked for ML. I also tried making novel NN architectures. I did come up with a transformer architecture that is as stable as feedforward nets on RL. The library transformers were absolutely horrible, but that doesn't mean much as it was still crap. Transformers, while they are very popular, have O(n^2) scaling, which means they don't scale at all. This really burdened me.

Static datasets are a lot easier to deal with transformers, but in poker the sequences have variable length. Because I was also doing batching for the sake of GPU utilization, I was getting out of memory errors, and I could not scale the architectures deeply. On the other hand, the algorithms I came up with that worked on toy games like Leduc poker completely broke down when I tried them on Holdem. I had some beautiful ideas, but when I stopped in late 2021 I was just doing regular AC training which I knew couldn't possibly work.

It is ridiculous. You can't do RL like this. If you want to do it seriously, you need a piece of hardware that has good enough bandwidth to handle batch sizes of 1 without performance issues. Having to do batching makes creating the game much harder too.

I know that for some people the job search can last over a year, so if that happens to me, I'll have a chance to do it better this time. I'll do it in the most straightforward way possible. I'll use tabular CFR which I know works well, and train the network using either evolution or a clustering approach I just thought up like during the night. When I get better hardware, I'll be able to make a genetic programming system to automate the architecture search and such.

> Was more thinking in terms of telling me you found it and charging me to use it or something - you could profit that way too :D

I am just kidding. Though I'd try to sell it to Google for millions of dollars, if I was in that situation, I'd release it. The reason for that is that I am pursuing the tech Singularity regardless of the cost. Any algorithm I'd get from a GP system would be a mess, and I'd need the help of others to generalize and explain how it works. Though I do not think I'll ever be in this situation.

The problem with the GP plan is that it is very resource intensive. Rather than me doing that kind of research, it is large companies who should be putting in large amounts of capital in order to break through the backprop bottleneck. I could implement the system, but with my computational resources I doubt the approach would get me particularly far.

So far I've been talking way too much about my own matters, so let me ask you some questions.

You've mentioned robotics a couple of times now. What kinds of algorithms are you guys using?

When I think of robotics, the first thing that comes to mind is PIMCO. Though that thing uses Gaussian Processes and has O(n^3) scaling. There are also linear approaches that use Newtonian optimization, I forgot what they were called. At the other end you have evolutionary approaches that are a lot less sample efficient, but you could make them work if you have good enough simulators. What kinds of robots are you guys making? If it is industrial robots, there you can constrain the environment and even hand craft the rules. If it is not, then you have a hard problem. Right now, even the hardware to make use of them in natural settings does not exist.

In the future, I think there will be memristor breakthroughs, and we'll have PIM chips with terabytes of non-volatile memory that would be suitable as primitive robot brains, though who knows how long that will take.

///

11am. Agh, I guess I'll paste it here. I ended up writing far more than intended.

11:30am. Had to take a break. Let me resume. Now it is finally time to screencast!

///

Since the early beginnings when generative neural nets were capable of making only tiny 64 by 64 pixel images, the world of generative art has come a long way. Generative AI models like Stable Diffusion allow you to make absolute masterpieces and stunning paintings and illustrations in under a minute! To use them however, you need a pretty beffy, and expensive GPU. For those of you who do not have the money or are not willing to spend what is needed to buy them just to use Stable Diffusion, but still want to use it to make high resolution images, then this video series is for you!

I will show you from start to finish how to get access to free Paperspace GPUs with memory capacities ranging from 8Gb to 80Gb at monthly subcription rates costing only 0,8 and 32$/month. I will also show you how to set everything up, in a series easy to follow steps! I will also give you a script to make getting the free tiers on Paperspace easier! So stay tuned!

///

11:35am. Right now I am feeling pretty jittery. I just need to do it.

11:40am. Yesterday while playing around with Camtasia I really got a feeling for how to edit video. So let me do it!

11:45am. I wish this program was faster to start up, but whatever. Let me start editing. I've found it is better if I take some time to pause the recital. Now I just need to cut on the empty periods and the retakes and I will be good to go. Brrr, I am so nervous!

It is really much easier if I do not need to get it all done perfectly the first try. Let me listen to it and then I will start cutting.

11:55am. Did some editing. The file is 1:06m long. Perfect. Now I just need some images.

https://lexica.art/

Let me do a screencast at his resolution of me just scrolling through this site.

12:05pm. Oh shit, that 2 minute recording is like 2Gb.

Well, it is fine. Let me export it.

https://youtu.be/jPGNJ9rKs5I
How to Remove Unused Footage or Media in Camtasia

I need to figure this out. That old recoding is taking up 2gb on my hard drive and I need to get rid of it.

I've decided to just ask the guy.

https://youtu.be/biVcFsVVa2M
How to Quickly Remove or Close ALL Gaps Between Video Clips In Camtasia

Let me watch this. Will it just be the magnet button.

https://youtu.be/biVcFsVVa2M?t=98

Yeah, it is.

12:30pm. Ah, whatever. Anyway, I have the mp4 file. I feel the video is too fast. It might be better if it cuts every second or so. But nevermind.

At 45mb, I can proceed to upload it to Youtube.

1pm.

https://www.youtube.com/watch?v=ClcTM97asqc&list=PL04PGV4cTuIVGO5ImYTk9wPVmbgdYbe7J
Intro

Here it is. My first Youtube video. Not bad. I am getting ahead in the world. I'll put Heaven's Key on the backburner in order to focus on this. Right now I'll just focus on making content, and later I'll make it pro looking. Like thumbnails, taking heads, end cards and so on.

Let me stop here for chores and breakfast. I'll do the next part of the series after that."

---
## [nushell/nushell](https://github.com/nushell/nushell)@[3d65fd7cc4...](https://github.com/nushell/nushell/commit/3d65fd7cc4f6e0db0c1c31b895feabf2be66cb0a)
#### Saturday 2023-01-28 13:50:16 by Doru

Expose filtering by file type in glob (#7834)

# Description

Add flags for filtering the output of `glob` by file type. I find myself
occasionally wanting to do this, and getting a file's
[file_type](https://docs.rs/wax/latest/wax/struct.WalkEntry.html#method.file_type)
is presumably fast to do as it doesn't have to go through the fallible
metadata method.

The design of the signature does concern me; it's not as readable as a
filter or "include" type list would be. They have to be filtered one by
one, which can be annoying if you only want files `-D -S`, or only want
folders `-F -S`, or only want symlinks `--butwhy?`. I considered
SyntaxShape::Keyword for this but I'll just defer to comments on this PR
if they pop up.

I'd also like to bring up performance since including these flags
technically incurs a `.filter` penalty on all glob calls, which could be
optimized out if we added a branch for the no-filters case. But in
reality I'd expect the file system to be the bottleneck and the flags to
be pretty branch predictor friendly, so eh

# User-Facing Changes
Three new flags when using `glob` and a slightly more cluttered help
page. No breaking changes, I hope.

# Tests + Formatting

Don't forget to add tests that cover your changes.

Make sure you've run and fixed any issues with these commands:

- `cargo fmt --all -- --check` to check standard code formatting (`cargo
fmt --all` applies these changes)
- `cargo clippy --workspace -- -D warnings -D clippy::unwrap_used -A
clippy::needless_collect` to check that you're using the standard code
style
- `cargo test --workspace` to check that all tests pass

# After Submitting

If your PR had any user-facing changes, update [the
documentation](https://github.com/nushell/nushell.github.io) after the
PR is merged, if necessary. This will help us keep the docs up to date.

---
## [HWSensum/Skyrat-tg](https://github.com/HWSensum/Skyrat-tg)@[e3435943f8...](https://github.com/HWSensum/Skyrat-tg/commit/e3435943f8357df864247ee0e6a2b445cc4d0d3d)
#### Saturday 2023-01-28 14:47:08 by SkyratBot

[MIRROR] Allows Chaplain's Spirit Sword To Redo Name If Invalid [MDB IGNORE] (#18723)

* Allows Chaplain's Spirit Sword To Redo Name If Invalid (#72642)

## About The Pull Request

The current behavior doesn't let the sword re-choose their name if they
screw it up the first time and it turns out to be filtered or sanitized
out for whatever reason. That's silly in my opinion, so I changed it to
be more like holoparasite name-selection behavior, where you get the
text to choose your name until you get it right.

I moved the re-naming portion of the sword to be after all of the
important RegisterSignal steps as well, just to be safe as we sleep as
they plug in different names they might want.
## Why It's Good For The Game

You shouldn't be stuck as "spirit of the blade" permanently if you
accidentally balls up the word filter, let's have it be more like
holoparasite behavior to be nicer.
## Changelog
:cl:
qol: Spirits of possessed blades (Chaplain's Null Rod Option) will be
able re-try selecting their name if it ends up to be filtered for any
reason.
/:cl:

* Allows Chaplain's Spirit Sword To Redo Name If Invalid

Co-authored-by: san7890 <the@san7890.com>

---
## [schnoddelbotz/science-and-scientists](https://github.com/schnoddelbotz/science-and-scientists)@[3771359f69...](https://github.com/schnoddelbotz/science-and-scientists/commit/3771359f696a4854d85def6b4a9f88acd0f26b4e)
#### Saturday 2023-01-28 17:41:23 by Jan Hacker

Why USA is no democracy and twitter no service

My experience over last two years, watching both closely. #FreeAssange ignored, every idea that was good stolen from me without saying thanks, suspending me for sharing truth -- now suspending me for citing "Little Ghetto Boy" Lyrics from WuTang 1:1 - as I used some of their words myself. Well - The end of science is here. Thank you Joe Biden & Elon Musk. You finished Trump's work in my today's view. It would be SOOOO hard for you to improve. Yeah.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[d780511b72...](https://github.com/mrakgr/The-Spiral-Language/commit/d780511b72ea2943eeaede324efb8191b1bb4fe6)
#### Saturday 2023-01-28 18:17:12 by Marko Grdinić

"3pm. Just a bit more and I will resume. I am feeling a good amount of fear. But that is good. If posting a simple video is enough to put me this much in daze, think about how hard having to talk with people would suck.

3:25pm. Let me resume.

https://boards.4channel.org/biz/thread/53471429/is-this-just-modern-day-slavery-20-cut-on-your

///

Yes, is 20% but just for the first $500 you make, then is 10% until you reach $10,000, then is 5%. You only need two long-term clients and you are set, and if they like your work they will probably take you out of the platform.

> Designerfag making $150k in Upwork, created a network there and then got hired as a contractor in two Fortune 500 companies

///

Is this how it works? I wondered about that, and I guess this might be a route.

3:30pm. Let me start. Focus me, focus.

Let me start recording.

3:55pm. Done. This is really easy. With Camtasia, I can just record off the cuff, and then come in and edit out the pauses and taking of breaths.

4pm. Another masterpiece, let me go with it. It is also 1.5 minutes long.

4:05pm. https://youtu.be/9y4vkCoKgEI
Price comparison of Paperspace and competing cloud providers

Here it is.

4:10pm. Now let me make a video on how to start a gradient notebook.

4:20pm. Done recording the third video. Let me edit it.

Oh, almost forgot to shut down the machine.

5:35pm. An hour of editing for a 3.5 minutes video. But I am done. Let me render it.

5:45pm. Reviewed the video. It is good enough to post on Youtube.

6:25pm. Done with lunch. I've made a repo and uploaded the script to it.

6:35pm. I can't put in clickable links and have to mess with Google security.

6:50pm. I figured it out and now the video is up.

https://youtu.be/tapbr8kltyo
The easiest way to start a free tier notebook on Paperspace

Here it is.

6:55pm. I'll close here. I spent the whole day just to produce 6 minutes of video, but it is satisfying nonetheless. My problem is that I am speaking too quickly and without enough thought put into it. I can afford to have longer pauses between in order to load up the next few sentences properly. I need to learn to speak in a more determined manner. I need to put more thought into each of my words.

The way to achieve that is to recognize that video editing gives me time to catch my breath and think. I can take as long as I need between sentences. So that is the key.

Tomorrow I will do better at this. Today was ideal as an ice breaker though. Today I was far better than in the last two days.

7pm. I need to do better. Right now it is hardly better than doing a robo voiceover. I need to vividly visualize each of the sentences before firing them out. This will ease up the editing process afterwards. If I can do this I will be able nail those future interviews. Or so the theory goes.

Let me rest here.

7:10pm. It sure would be nice if this ends up being popular. I think I could make something promoting Paperspace on Youtube, as well as AI companies and such.

I can't imagine this sort of effort being less popular than Heaven's Key. That should be something to look forward to. Just pursue it. Pursue the passion, pursue the possibilities and pursue the dreams.

If I ever get the computational power that I desire, there will be time to make something of Simulacrum. If not, who cares. It will just be a possibility of the Singularity that never manifested. That I make money and the computational resources is more important than writing the story. That is the way to go."

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[2a4ef2367d...](https://github.com/tgstation/tgstation/commit/2a4ef2367dd7db73ba0adfdc300a5093678b7746)
#### Saturday 2023-01-28 20:16:39 by san7890

Basic Mobs Now Actually Have A Deathgasp (#72950)

## About The Pull Request

Pretty obviously an oversight since we only checked for simple_animal
for this, but should also factor in the fact that we could now be a
basic mob.

Actually I tested it on Sybil just now and deathgasps just never worked.
We were setting death_message for... I guess when they die? It's just
fucked but it works on my local now. blurgh
## Why It's Good For The Game

Ported simple animals that are now basic mobs were able to deathgasp
this time last year. Silly that they aren't able to do that now.
## Changelog
:cl:
fix: Basic Mobs are now able to deathgasp.
/:cl:

Let me know if the new variable name for the string is cringe, I just
settled on that since it mirrored the type of check we run in
select_message_type().

---
## [TheAMM/mpv](https://github.com/TheAMM/mpv)@[f4e89dde36...](https://github.com/TheAMM/mpv/commit/f4e89dde36644edec7d09856ac83140317f0b687)
#### Saturday 2023-01-28 20:42:30 by Dudemanguy

wayland: simplify render loop

This is actually a very nice simplification that should have been
thought of years ago (sue me). In a nutshell, the story with the
wayland code is that the frame callback and swap buffer behavior doesn't
fit very well with mpv's rendering loop. It's been refactored/changed
quite a few times over the years and works well enough but things could
be better. The current iteration works with an external swapchain to
check if we have frame callback before deciding whether or not to
render. This logic was implemented in both egl and vulkan.

This does have its warts however. There's some hidden state detection
logic which works but is kind of ugly. Since wayland doesn't allow
clients to know if they are actually visible (questionable but
whatever), you can just reasonably assume that if a bunch of callbacks
are missed in a row, you're probably not visible. That's fine, but it is
indeed less than ideal since the threshold is basically entirely
arbitrary and mpv does do a few wasteful renders before it decides that
the window is actually hidden.

The biggest urk in the vo_wayland_wait_frame is the use of
wl_display_roundtrip. Wayland developers would probably be offended by
the way mpv abuses that function, but essentially it was a way to have
semi-blocking behavior needed for display-resample to work. Since the
swap interval must be 0 on wayland (otherwise it will block the entire
player's rendering loop), we need some other way to wait on vsync. The
idea here was to dispatch and poll a bunch of wayland events, wait (with
a timeout) until we get frame callback, and then wait for the compositor
to process it. That pretty much perfectly waits on vsync and lets us
keep all the good timings and all that jazz that we want for mpv. The
problem is that wl_display_roundtrip is conceptually a bad function. It
can internally call wl_display_dispatch which in certain instances,
empty event queue, will block forever. Now strictly speaking, this
probably will never, ever happen (once I was able to to trigger it by
hardcoding an error into a compositor), but ideally
vo_wayland_wait_frame should never infinitely block and stall the
player. Unfortunately, removing that function always lead to problems
with timings and unsteady vsync intervals so it survived many refactors.

Until now, of course. In wayland, the ideal is to never do wasteful
rendering (i.e. don't render if the window isn't visible). Instead of
wrestling around with hidden states and possible missed vblanks, let's
rearrange the wayland rendering logic so we only ever draw a frame when
the frame callback is returned to use (within a reasonable timeout to
avoid blocking forever).

This slight rearrangement of the wait allows for several simplifications
to be made. Namely, wl_display_roundtrip stops being needed. Instead, we
can rely entirely on totally nonblocking calls (dispatch_pending, flush,
and so on). We still need to poll the fd here to actually get the frame
callback event from the compositor, but there's no longer any reason to
do extra waiting. As soon as we get the callback, we immediately draw.
This works quite well and has stable vsync (display-resample and audio).
Additionally, all of the logic about hidden states is no longer needed.
If vo_wayland_wait_frame times out, it's okay to assume immediately that
the window is not visible and skip rendering.

Unfortunately, there's one limitation on this new approach. It will only
work correctly if the compositor implements presentation time. That
means a reduced version of the old way still has to be carried around in
vo_wayland_wait_frame. So if the compositor has no presentation time,
then we are forced to use wl_display_roundtrip and juggle some funny
assumptions about whether or not the window is hidden or not. Plasma is
the only real notable compositor without presentation time at this stage
so perhaps this "legacy" mechanism could be removed in the future.

---
## [Addust/Voidcrew-LRP-1](https://github.com/Addust/Voidcrew-LRP-1)@[a05d69d10a...](https://github.com/Addust/Voidcrew-LRP-1/commit/a05d69d10a26b502d8ef6fe86b023fd95025ca0f)
#### Saturday 2023-01-28 21:04:59 by Addust

oh my fucking god I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JS…

---
## [LyamBRS/BRS_Python_Libraries](https://github.com/LyamBRS/BRS_Python_Libraries)@[ffe46e7eba...](https://github.com/LyamBRS/BRS_Python_Libraries/commit/ffe46e7eba48bc589aec347ac5b3de1273cc9e0c)
#### Saturday 2023-01-28 21:18:19 by Lyam[BRS]

KivyMD cards successfully implemented.

- SVG Still a massive pain in the ass. Like bruh. Wtf. You telling me that they can't implement proper support for SVG files in something that allows canvas drawing. Fuck off

---
## [starpit/kui](https://github.com/starpit/kui)@[5973a6f3ac...](https://github.com/starpit/kui/commit/5973a6f3acabfdd38743ca9f4f516fea787a4779)
#### Saturday 2023-01-28 23:28:50 by Nick Mitchell

fix: improved fix for externalizing electron/remote

- We should be using the `webpackIgnore: true` magic comment, rather than the silly hack we had from #9265
- #9265 missed the second import of electron/remote

---
## [tcharding/rust-bitcoin](https://github.com/tcharding/rust-bitcoin)@[f6d983b2ef...](https://github.com/tcharding/rust-bitcoin/commit/f6d983b2ef4dfacd53499fd9f1d77058c0f396ff)
#### Saturday 2023-01-28 23:48:04 by Andrew Poelstra

Merge rust-bitcoin/rust-bitcoin#1532: Improve Psbt error handling

e7bbfd391353fd03d60550c768364e9de5d3e8c5 Improve Psbt error handling (DanGould)

Pull request description:

  ## Separate `encode::Error` and `psbt::Error` recursive dependency

  This initial work attempts to fix #837's first 2 points

  > - The current psbt::serialize::Deserialize has an error type of consensus::encode::Error. I think we should cleanly separate consensus encoding errors from application-level encoding errors like psbt.
  > - There is a recursive dependence between encode::Error and psbt::Error which would need to be cleanly dissected and separated so that there is no dependence or only one-way dependence.

  ## Better `ParseError(String)` types

  arturomf94 how compatible do your #1310 changes look to address #837's third point with this design?

  > - There are a lot ParseError(String) messages that could use a better type to downflow the information.

  I think your prior art would completely address this issue now.

  ## On handling `io::Error` with an associated error

  `encode::Error` has an `Io` variant. now that `Psbt::deserialize` returns `psbt::Error` and produces an `io::Error`, we need an `Io` variant on `psbt::Error`. Except that doing so breaks  `#[derive(Eq)]` and lots of tests for `psbt::Error`.

  Kixunil, I'm trying to understand your feedback regarding a solution to this problem.

  > I believe that the best error untangling would be to make decodable error associated.

  > I meant having associated `Error` type at `Decodable` trait. Encoding should only fail if the writer fails so we should have `io::Error` there (at least until we have something like `genio`).
  >
  > > [it] is a problem to instantiate consensus::encode::Error in [the psbt] module for `io::Error`?
  >
  > It certainly does look strange. Maybe we should have this shared type:
  >
  > ```rust
  > /// Error used when reading or decoding fails.
  > pub enum ReadError<Io, Decode> {
  >     /// Reading failed
  >     Io(Io),
  >     /// Decoding failed
  >     Decode(Decode), // consensus and PSBT error here
  > }
  > ```
  >
  > However this one will be annoying to use with `?` :( We could have `ResultExt` to provide `decode()` and `io()` methods to make it easier.
  >
  > If that's not acceptable then I think deduplicated IO error is better.

  Kixunil didn't we just get rid of Psbt as `Decodable`? Would this make more sense to have as an error associated with `Deserialize`? Or did we do the opposite of what we should have by making Psbt only `Serialize`/`Deserialize` because of #934, where only consensus objects are allowed to be `Decodable`? I wonder if we prioritized that strict categorization and are stuck with worth machinery because of it. My goal with #988 was to get to a point where we could address #837 and ultimately implement PSBTv2.

ACKs for top commit:
  tcharding:
    ACK e7bbfd391353fd03d60550c768364e9de5d3e8c5
  apoelstra:
    ACK e7bbfd391353fd03d60550c768364e9de5d3e8c5

Tree-SHA512: 32975594fde42727ea9030f46570a1403ae1a108570ab115519ebeddc28938f141e2134b04d6b29ce94817ed776c13815dea5647c463e4a13b47ba55f4e7858a

---

