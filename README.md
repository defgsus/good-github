## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-03-06](docs/good-messages/2023/2023-03-06.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,304,402 were push events containing 3,524,202 commit messages that amount to 292,758,071 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 48 messages:


## [KathrinBailey/Bubberstation](https://github.com/KathrinBailey/Bubberstation)@[406b6870bd...](https://github.com/KathrinBailey/Bubberstation/commit/406b6870bd28dd78e65e59787d8c54c776078019)
#### Monday 2023-03-06 01:14:14 by SkyratBot

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
## [copperwater/xNetHack](https://github.com/copperwater/xNetHack)@[1967480335...](https://github.com/copperwater/xNetHack/commit/1967480335678a13ce9b87c49828fcfe07148b60)
#### Monday 2023-03-06 01:33:44 by copperwater

Cocytus causes persistent cold damage if hero is not cold resistant

This is adapted from similar rules in the Ice Queen's Realm in EvilHack.
Once per turn (not action), the hero will take 1d6 cold damage while in
the branch, if they are not cold resistant.

I had to rework EvilHack's code a bit, sacrificing some death-message
quality, because calling losehp() with its unavoidable "You die..."
message is preferable to reimplementing the guts of losehp() to
correctly handle if you freeze to death while polymorphed. (In EvilHack,
this is currently a bug -- freezing to death while polymorphed kills
your normal form without warning.)

As the comment in this commit explains, the cold damage does not happen
to monsters. While I don't like this asymmetry on principle, it will
make it much easier to put monsters in the special levels without
worrying about a cheesy strategy of arriving on the level and waiting
for the non-cold-resistant monsters to die.

Also, moving into and out of Cocytus now produces the correct messages
regarding the heat and smoke of Gehennom. Leaving Cocytus via
levelporting or branchporting to a non-hellish destination does not
produce any message, which is consistent with the rest of Gehennom.
(There isn't a "heat and smoke are gone" message if you leave via
levelport or branchport.)

---
## [DroneBetter/Perspective3Dengine](https://github.com/DroneBetter/Perspective3Dengine)@[c44ff86e3d...](https://github.com/DroneBetter/Perspective3Dengine/commit/c44ff86e3ddb1fce35df71dfc093c8fbd23497f7)
#### Monday 2023-03-06 01:37:37 by DroneBetter

make moving in direction of orientation work

It turns out that spatial position and orientation in spherical 3-space (equivalent to 4D hypersphere orientation) need to be intertwined in versors together (one enacted by multiplication on either side), which can be derived from the equation for rotating components in a 2D slice without affecting components in the perpendicular plane (instead of perpendicular line (ie. cross product), because it's entirely rotating the hypersphere directly instead of 3D space afterwards).
It is no longer a cool one-liner like before, but allows some parts to be more elegant (ie. handling everything before the logarithm), I struggled for a while before having the idea to multiply by the rotation versor on one side and its conjugate on the other (which seems to work (the best kind of working))
Pairs of versors are also the minimal, information-wise
The only problem is that velocity is rotated with the camera's orientation, however, but for the time being consider this a feature (to reduce motion sickness or something)
(I'm committing this version, similarly to the previous one, as the first one that I got working with a change, for documentation purposes)

You also may notice the other mode in rotationParameters (which is for enacting it directly upon a value x, in a manner less composable than returning two new quaternions that the existing pair can be multiplied by, but in only 64 numerical multiplications (instead of the 40 to generate the quaternion pair and 32 more* to multiply through), using the fact that many terms of the expansion measure absolute values of specific quaternion parameters, which are 1 when they're versors**), which is there because I have begun using SymPy*** to help me (which doesn't have any equation length constraints like WolframAlpha (and isn't paid like Mathematica)), I like it a lot and will be able to do things with complicated derivations (like the original 3D engine's mode with storing time offsets from the "present" in a sub-frame for each cell also) more easily (ie. no longer splitting them apart to attempt to simplify piecewise with WolframAlpha) when they arise
*There is https://en.wikipedia.org/wiki/Multiplication_algorithm#Complex_number_multiplication that accomplishes complex multiplication in three numerical multiplications (Strassen-style), I wonder whether there's anything like that for quaternions
**no numerical stability, albeit (living life on the edge)
***(also used in my tablebase program for multiset permutations but I didn't know about its general CAS functionality having a WolframAlpha-like plaintext interface)
Anyway, I have big plans for it still

---
## [Tsar-Salat/tgstationcashew](https://github.com/Tsar-Salat/tgstationcashew)@[10a344bde0...](https://github.com/Tsar-Salat/tgstationcashew/commit/10a344bde0d48fb250dcb7a9eb4a1e98b9bb6df5)
#### Monday 2023-03-06 02:38:34 by Time-Green

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
## [Tsar-Salat/tgstationcashew](https://github.com/Tsar-Salat/tgstationcashew)@[36090c1b20...](https://github.com/Tsar-Salat/tgstationcashew/commit/36090c1b206dee8b643e83607e333c29906b6bc8)
#### Monday 2023-03-06 02:38:34 by san7890

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
## [Tsar-Salat/tgstationcashew](https://github.com/Tsar-Salat/tgstationcashew)@[5e80257423...](https://github.com/Tsar-Salat/tgstationcashew/commit/5e802574231c9c6fe835c40b55f2c8aa9f1c68b4)
#### Monday 2023-03-06 02:38:34 by Jeremiah

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
## [N3D6/YogstationIfItWasntMid](https://github.com/N3D6/YogstationIfItWasntMid)@[8e3e0b1450...](https://github.com/N3D6/YogstationIfItWasntMid/commit/8e3e0b1450189ebda3b2bc760c036ba6c59c6b6a)
#### Monday 2023-03-06 02:53:25 by LazennG

adds magmite crusher to the things you can make at the world anvil (#17530)

* FUCK YOU PLASMA CUTTER

* updated it now just waiting on BAIOMU FOR FUCKIN SPRITES

* returned old sprites i had but it's still lacking 1 handed versions

* touched up some of the sprites but STILL NEED ONEHANDED ONES FROM BAIOMU

* FINALLY

---
## [bgteffera/Data-Analysis-Portfolio](https://github.com/bgteffera/Data-Analysis-Portfolio)@[662ef8758b...](https://github.com/bgteffera/Data-Analysis-Portfolio/commit/662ef8758b1664cf5d59cb1fffde25ce4176b483)
#### Monday 2023-03-06 04:21:13 by Barry Teffera

Add files via upload

The 2022 soccer/football season brought us many qualified nominees for this year's "The Best" honor. Balon d'Or winner Benzema and his French compatriot Mbappe had historic seasons for Real Madrid and PSG, respectively. Furthermore, Mbappe's hat trick in France's unsuccessful bid to retain the World Cup (WC) will go down as one of the greatest WC final performances of all time. In the WC's storied history, only Geoff Hurst managed to score a hat trick in the tournament's championship match (1966, England). However, the favorite for this prize was none other than the Argentine magician, Lionel Messi. His tenure at the top of world football is unparalleled and was accentuated by his rivalry with the enigmatic Cristiano Ronaldo. Messi's slow start to life at PSG decimated his chances at the Balon D'or, but a strong start to his second season in Paris and a breathtaking WC run made him a shoe in for Fifa's award, which is voted on by each nation's coach, their captain, and a media representative. Fifa released the voting, which is visualized in this Power BI dashboard. An interactive map allows you to see the nationalities of each voter, along with slicers and various charts that emphasize just how dominant the voting for Messi was.

---
## [maxwelljoslyn/masters-thesis](https://github.com/maxwelljoslyn/masters-thesis)@[a50190c128...](https://github.com/maxwelljoslyn/masters-thesis/commit/a50190c1281e94a10b2fdb6b9db1b8b51a84f6cd)
#### Monday 2023-03-06 04:38:02 by Maxwell Joslyn

cleanup

formatting... why CIDER isn't reliably doing this for me, God only knows. (yes I've tried multipe ways eg the normal strategy of a before-save-hook calling cider-clj-format or whatever it's called. it was seriously squirrelly, unreliable. FFS. I blame Spacemacs, which I have grown to hate and deride --- "we only publish layers with Emacs modes and packages that are tested for integration" my ass!)

---
## [pa-gr/android_frameworks_base](https://github.com/pa-gr/android_frameworks_base)@[82cd10fe63...](https://github.com/pa-gr/android_frameworks_base/commit/82cd10fe630465e924eddcd154a7f18c08f73354)
#### Monday 2023-03-06 05:09:57 by Adithya R

[DNM][HACK] telephony: Force Class 0 SMS to Class 1

This kills Flash SMS messages. Fuck you airtel

Change-Id: Ifb0c9e8bae5c12868d178fbdaeceb2cc72a0ffb6

---
## [capsaicinz/tgstation](https://github.com/capsaicinz/tgstation)@[c58cbb4dfb...](https://github.com/capsaicinz/tgstation/commit/c58cbb4dfb42e0d9d6198c3ad581dc5a4d2f8f48)
#### Monday 2023-03-06 05:25:12 by John Willard

Reworked PDA menu & NtOS themes (#73070)

## About The Pull Request

This is a port/rework of
https://github.com/yogstation13/Yogstation/pull/15735 - I changed a lot
of how it acted (some themes are locked behind maintenance apps).

The original author allowed this port to happen, and I really liked how
it looked there so I'd like to add it here.

### Applications

Removes the hardware configurator application, as all it did was show
you your space and battery now that all hardware was removed. These are
things your PC does by default, so it was just a waste of space.
Adds a Theme manager application instead, which allows you to change
your PDA's theme at will.
Adds a new Maintenance application that will give a new theme, however
it will also increase the size of the theme manager app itself as it's
bloatware.

### Menu

There's now a bar at the top of the menu showing 'special' tablet apps
which, for one reason or another, should stand out from the rest of the
apps. Currently this is PDA messenger and the Theme manager

Flashlight and Flashlight color is now only an icon, and is shown on the
same line as Updating you ID


https://cdn.discordapp.com/attachments/961874788706574386/1069621173693972551/2023-01-30_09-10-52.mov


![image](https://user-images.githubusercontent.com/53777086/215501361-5ea3086e-2ff5-4ab1-bde4-8a3d14014fce.png)

### Themes

Adds a lot of themes to choose from, although SOME are hidden behind
Maintenance applications, which will give you a random theme. These are
bloatware however, so they come with some extra cost to the app's
required space storage.

Themes are now supported on ALL APPLICATIONS! If you have a computer
theme, you will have that theme in EVERY app you enter, rather than just
a select few.
ALSO also, emagging the tablet will automatically set & unlock the
Syndicate theme, which makes your PDA obvious but you can disguise it if
you wish through just re-painting it to something else.


https://cdn.discordapp.com/attachments/828923843829432340/1069565383155122266/2023-01-30_05-29-53.mov

### Preferences

This also adds a pref for theme, reworking the ringtone code to work
with it as well. I also removed 2 entirely unused PDA prefs just 'cause.

Screenshot not up-to-date, they now have proper names.

![image](https://user-images.githubusercontent.com/53777086/215463669-0fe9951a-71f8-4b71-a97d-b79b5a2f945a.png)

### Other stuff

Made defines for device_themes
Added support for special app-side checks to download files
Fixed programs downloading themselves TWICE because defines all had the
same definition
Removes the Chemistry computer disk as it was empty due to chemistry
app's removal
Removes the 'run_emag' proc, since apps can directly refer to the
computer to check for emag status instead.
Moved over and added better documentation on data computer files, and
moved the ordnance ones to the same file as the others.

## Why It's Good For The Game

It makes PDAs a lot more customizable while adding more features to
maintenance applications. I think the themes look cool and it fits with
PDAs being "personal" anyways.

I also explained most of my other arguments in the about section, such
as the hardware configuration application.

## Changelog

:cl: Chubbygummibear & JohnFulpWillard
add: A ton of new NtOS themes, which are accessible by the new Themify
application that comes with all PCs.
add: Emagging a PC now defaults it to the Syndicate option (and adds it
to go back to it if you wish)
add: There's a new maintenance app that gives you rarer themes
qol: The NtOS Main menu was moved around, added "header" applications
that are shown where the Flashlight is, such as your Theme manager and
PDA messenger.
code: Made defines for device_themes
code: Added support for special app-side checks to download files
code: Removes the 'run_emag' proc, since apps can directly refer to the
computer to check for emag status instead.
fix: Programs no longer download twice.
del: Removes the Chemistry computer disk as it was empty due to
chemistry app's removal
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [ruichengeng/NEXT_2023_Programming_RuiGeng](https://github.com/ruichengeng/NEXT_2023_Programming_RuiGeng)@[0554aa78d2...](https://github.com/ruichengeng/NEXT_2023_Programming_RuiGeng/commit/0554aa78d2c57d1f4fe913cb3d42230d22bdae51)
#### Monday 2023-03-06 05:32:50 by ruichengeng

Oh gosh I forgot to include the document, sorry (in tears)

---
## [rbertoche/space-station-14](https://github.com/rbertoche/space-station-14)@[581e8a0d12...](https://github.com/rbertoche/space-station-14/commit/581e8a0d123eca621e52716fd5816966b0569a36)
#### Monday 2023-03-06 06:14:02 by eclips_e

Give slimes their sex back (not the ERP one) (#14380)

<!-- Please read these guidelines before opening your PR: https://docs.spacestation14.io/en/getting-started/pr-guideline -->
<!-- The text between the arrows are comments - they will not be visible on your PR. -->

## About the PR
<!-- What does it change? What other things could this impact? -->

Gives back the ability for slimes to have a definitive sex. Cosmetic/visual things such as emotes/other stuff use the person's sex and not the gender and I feel like that the removal of slime's having sexes was just to show that the species refactor could handle unsexed species.

**Media**
<!-- 
PRs which make ingame changes (adding clothing, items, new features, etc) are required to have media attached that showcase the changes.
Small fixes/refactors are exempt.
Any media may be used in SS14 progress reports, with clear credit given.

If you're unsure whether your PR will require media, ask a maintainer.

Check the box below to confirm that you have in fact seen this (put an X in the brackets, like [X]):
-->

- [x] I have added screenshots/videos to this PR showcasing its changes ingame, **or** this PR does not require an ingame showcase

**Changelog**
<!--
Here you can fill out a changelog that will automatically be added to the game when your PR is merged.

Only put changes that are visible and important to the player on the changelog.

Don't consider the entry type suffix (e.g. add) to be "part" of the sentence:
bad: - add: a new tool for engineers
good: - add: added a new tool for engineers

Putting a name after the :cl: symbol will change the name that shows in the changelog (otherwise it takes your GitHub username)
Like so: :cl: PJB
-->

:cl: eclips_e
- fix: Male and female slimes now scream and laugh properly

---
## [ZzAve/teambalance](https://github.com/ZzAve/teambalance)@[be41a19967...](https://github.com/ZzAve/teambalance/commit/be41a199672f42698acd0e60d1d135ce589d480b)
#### Monday 2023-03-06 06:15:05 by Julius van Dis

Upgrade to MUI 5 (#227)

* clean covid-19

* Add themeprovider to app

* Add MUI 5 dependencies

- included @mui/x-date-pickers (as replacement for @material-ui/pickers)
- included emotion for typesafe css

* Remove MUI 4 dependencies, and fix breaking component changes

Follows: https://mui.com/material-ui/migration/v5-component-changes/

Noteworthy:
- Fixes in createStyles and withStyles
- Deprecated `<Hidden>` component (mostly move to:
 ```<Typography variant={"button"} sx={{ display: { sm: "block", xs: "none" } }}>
  Terug naar de veiligheid</Typography>```
- App is wrapped in <StyledEngineProvider injectFirst> to support JSS (prepare for migration to emotion
- Shit ton of renames from @material-ui/* to @mui/*
- Verwijderen van AttendeeStyledButton, en fallback op normale Button. 'uncertain' is mapped naar 'warning', en die kleur is aangepast in de palette van de theme.

* Apply webpack optimisations to reduce build times (dev: 30s to 10s, prod 60s to 10s)

* Replace JSS with emotion

* Remove @mui/styles

* Upgrade notistack to v2

* Pin dependencies

* Fix latest mui things

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[db6c5e8a5e...](https://github.com/treckstar/yolo-octo-hipster/commit/db6c5e8a5e56a34784e49cbc0b292d5fc8665d08)
#### Monday 2023-03-06 06:22:06 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [jlsnow301/tgstation](https://github.com/jlsnow301/tgstation)@[8ab74525c1...](https://github.com/jlsnow301/tgstation/commit/8ab74525c1c3c09a7605fead3ab013d29f24d07f)
#### Monday 2023-03-06 07:09:43 by itseasytosee

Brings the monkey back down (body horror edition/addition.) (#73325)

## About The Pull Request
Let me paint you a story.
A long time ago monkeys once rested their feet on the floor, this was a
time of bliss and peace. But sometime around the horrors of making
monkeys subtypes of humans did an atrocity occur.

![image](https://user-images.githubusercontent.com/55666666/217657059-5c960ab4-c3de-493c-ac12-28de99b43d7f.png)
**The monkeys were moved up.**
I thought this was bad, and alot of people on the forum tended to agree
with me

![image](https://user-images.githubusercontent.com/55666666/217657707-120354c7-b1a5-4d93-8813-8e10e142bd92.png)
This was do to some purpose of adjusting them so it could be easier to
fit item sprites onto them instead of preforming the hours of work
refractoring to make the heights of the items dynamic and adjustable. A
simple pixel shift may have sufficed, but you see, such a change would
NEVER allow the frankensteining of monkey and human features together.
This is that refractor.

In essence, the following is now true.
A top_offset can now be generated for a human based on a varible on
their chest and legs. By default, and as is true with human legs and
chests, this variable is ZERO by default. Monkey legs and chest have
NEGATIVE values proportionate and onto how much smaller their sprite is
compared to humans. Other bodyparts, as well as any other accociated
overlays, or clothing will automatically be offset to this axis. THIS
MEANS THAT MONKEYS ARE ON THE FLOOR. But is means something else too.
Something more freakish,


![image](https://user-images.githubusercontent.com/55666666/217659439-bc0b1a35-76c8-4490-b869-770180605822.png)
**What abominable monsters**, unreachable by players as long as we can't
stitch monkeys and humans together (oh but just wait until the feature
freeze ends)
Oh but you might be thinking, if legs can make a mob go down.
can it make a mob

**go**
**up??**

**OH NO**


![image](https://user-images.githubusercontent.com/55666666/217707042-0d53022f-d93a-4262-a5ce-ef15a99eb897.png)

![image](https://user-images.githubusercontent.com/55666666/217707060-779f5901-ab90-4a64-9ca7-0b147e24f099.png)

![image](https://user-images.githubusercontent.com/55666666/217707821-23d7457c-5881-40ae-8d9d-c9fbd645aba6.png)

These lads are stepping, and have been implemented solely for proof of
concept as a way to flex the system I have created and remain
inaccessible without admin intervention.

But really, when all is said and done, all this PR does in terms of
player facing changes is move the monkey back down.

![image](https://user-images.githubusercontent.com/55666666/217708365-b6922a6d-08d0-4267-8713-4f8dac29038e.png)
Oh and fixed monkey husked which have been broken for who knows how
long.

![image](https://user-images.githubusercontent.com/55666666/217708464-5a9b6f89-4223-4ae5-a21e-3a274a9f8db8.png)
## Why It's Good For The Game
The monkey is restored to its original position. Tools now exist to have
legs and torsos of varying heights. Monkey Husking is fixed.
## Changelog
:cl: itseasytosee
fix: Monkeys ues the proper husk sprites.
imageadd: The monkey has been moved back down to its lower, more
submissive position.
refactor: Your bodyparts are now dynamically rendered at a height
relevant to the length of your legs and torso, what does this mean for
you? Not much to be honest, but you might see a monkey pop up a bit if
you cut its legs off.
admin: The Tallboy is here
/:cl:

---------

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>
Co-authored-by: san7890 <the@san7890.com>

---
## [jlsnow301/tgstation](https://github.com/jlsnow301/tgstation)@[d55ce0f0bc...](https://github.com/jlsnow301/tgstation/commit/d55ce0f0bcb6c37113c9ec9f0e37facd99b69625)
#### Monday 2023-03-06 07:09:43 by Jacquerel

Don't create abandoned airlocks with walls underneath them. (#73656)

## About The Pull Request
Fixes #71504

#70237 attempted to remove this and did in some cases, however the case
where the abandoned airlock is able to find an adjacent wall turf to
copy the type of still fails to delete the airlock.
This fixes that.

Also in my testing, the times where it _failed_ to find a nearby wall
turf to copy and spawned a default wall would leave the mapping helper
visible in the round. Oops!

## Why It's Good For The Game

Mapping helpers should always delete themselves when finished.
The airlocks with walls under them are funny once and annoying the rest
of the time. As of that older PR, this continuing to happen is regarded
as a bug.
Also apparently it might be required anyway for Wallening.

## Changelog

:cl:
fix: Maintenance tunnels should no longer sometimes contain airlocks
with walls underneath them.
/:cl:

---
## [bsprague99/memSim](https://github.com/bsprague99/memSim)@[976eaf2d04...](https://github.com/bsprague99/memSim/commit/976eaf2d04e698ef3186988b67cbc2086a58fdcd)
#### Monday 2023-03-06 07:40:10 by elau14

including LRU implementation!!

updated to include extensively tested LRU implementation - should receive 18/20 points now, hell fuckin yeah

---
## [spantaleev/matrix-docker-ansible-deploy](https://github.com/spantaleev/matrix-docker-ansible-deploy)@[adcc6d9723...](https://github.com/spantaleev/matrix-docker-ansible-deploy/commit/adcc6d9723086f65f1a7284a4d3eee03de56ac22)
#### Monday 2023-03-06 07:45:19 by Slavi Pantaleev

Relocate Traefik (to matrix-traefik.service && /matrix/traefik base path)

The migration is automatic. Existing users should experience a bit of
downtime until the playbook runs to completion, but don't need to do
anything manually.

This change is provoked by https://github.com/spantaleev/matrix-docker-ansible-deploy/pull/2535

While my statements there ("Traefik is a shared component among
sibling/related playbooks and should retain its global
non-matrix-prefixed name and path") do make sense, there's another point
of view as well.

With the addition of docker-socket-proxy support in bf2b54080789f7e,
we potentially introduced another non-`matrix-`-prefixed systemd service
and global path (`/devture-container-socket-proxy`). It would have
started to become messy.

Traefik always being called `devture-traefik.service` and using the `/devture-traefik` path
has the following downsides:

- different playbooks may write to the same place, unintentionally,
  before you disable the Traefik role in some of them.
  If each playbook manages its own installation, no such conflicts
  arise and you'll learn about the conflict when one of them starts its
  Traefik service and fails because the ports are already in use

- the data is scattered - backing up `/matrix` is no longer enough when
  some stuff lives in `/devture-traefik` or `/devture-container-socket-proxy` as well;
  similarly, deleting `/matrix` is no longer enough to clean up

For this reason, the Traefik instance managed by this playbook
will now be called `matrix-traefik` and live under `/matrix/traefik`.

This also makes it obvious to users running multiple playbooks, which
Traefik instance (powered by which playbook) is the active one.
Previously, you'd look at `devture-traefik.service` and wonder which
role was managing it.

---
## [GitHubSecurityLab-CodeAnalysis/melpa_melpa](https://github.com/GitHubSecurityLab-CodeAnalysis/melpa_melpa)@[4872ef038d...](https://github.com/GitHubSecurityLab-CodeAnalysis/melpa_melpa/commit/4872ef038dbbf67008bfa7951574ee372d6ff68d)
#### Monday 2023-03-06 08:06:18 by Jonas Bernoulli

Distribute all back-ends with the emacsql package

There are two reasons for this.

- Going forward, packages that use `emacsql' and SQLite should use
  the best back-end that can be used with the Emacs instance in use,
  either `emacsql-sqlite-builtin`, `emacsql-sqlite-module`, or as a
  last resort `emacsql-sqlite'.

  That means that if we didn't bundle the back-end libraries with
  `emacsql' itself, these packages would have to depend on all three
  back-end packages in addition to `emacsql' itself.  (Alternatively
  they could not depend on any of the back-end packages, and instead
  make the user install the appropriate back-end, when they try to
  use the package.  That's a bad user experience and there likely
  would be bugs, making it even more painful.)

- EmacSQL is now distributed on NonGNU Elpa as well.  While we at
  Melpa encourages the creation of separate packages for optional
  extensions (which are not useful to all users, or which have
  additional dependencies) the Emacs maintainers prefer everything to
  be distribute as one package, even if that means that `defvar' and
  `declare-function' declarations are necessary to keep the compiler
  happy.

  I still think our way is usually better, but since three of the
  back-end libraries have to be distributed with the main package
  anyway, we might as well give in here and bundle the other three
  as well.

For the time being, we have to continue to *also* distribute the
back-end libraries as separate packages.

Several third-party packages depend on the existing `emacsql' and
`emacsql-sqlite' packages.  These packages should be updated to only
depend on `emacsql', but the latest released versions of these
packages will continue to depend on `emacsql-sqlite' as well.  If we
removed the recipe for that, that would remove the latest release of
that package from Melpa, not just the snapshot version.

This is the current roadmap:

0. Include all back-ends in `emacsql'.
1. Update dependant packages to only depend on `emacsql'.
2. Make changes to `emacsql', which are enabled by the former two
   steps, and which are blocking the creation of a new `emacsql'
   release.  (These changes are related to the addition of the
   additional SQLite back-ends.  So this is a bit of a chicken and
   egg problem, and this commit (0) is the first step to break out
   of that.)
3. Create an `emacsql' release.
4. Wait for new releases of all dependant packages.
5. Change the separate back-end packages to warn the user, asking
   them to remove all of these packages.
6. After waiting some more, remove the separate back-end packages.

While a back-end is installed as part of `emacsql' and as a separate
package, it is undefined which version is loaded, but until step (5)
the two versions should be the same, so it doesn't matter.

---
## [MarkSuckerberg/Shiptest](https://github.com/MarkSuckerberg/Shiptest)@[d21740b475...](https://github.com/MarkSuckerberg/Shiptest/commit/d21740b475aea65de3b250a5aea26a69677e30e8)
#### Monday 2023-03-06 08:11:51 by tmtmtl30

Mapgen fixes and speedups (ignore the branch name. I'm dumb) (#1637)

## About The Pull Request

Alters the structure of map/planet generation to squash some bugs and
improve performance.

Previously, planet maps were generated by placing the ruin first, and
THEN generating the turfs according to the map_generator datum. This has
been adjusted -- now, turfs are generated WITHOUT objects such as
mobs/flora, the ruin is placed, and THEN the objects are added (turfs
are "populated"). In conjunction with the addition of needed
AfterChange() calls to update the atmos adjacency of the generated
turfs, this ensures that planet atmos acts correctly surrounding ruins.

When deleting reservations (such as the deletion of planets after
undocking), all objects on the planet are rounded up in a list and
qdeleted. Although this causes a small lag spike, it SHOULD prevent
items from hanging out inside the edges of planets.

There's a feature to change the default baseturf of a virtual level,
ZTRAIT_BASETURF, that we now use. This should cut down on the instances
where a ruin on a planet is blown up and there's space underneath (might
still happen on asteroids, because the baseturf there is still space; I
didn't want space turfs without space as their baseturf).

Overmap encounter areas aren't global anymore (they no longer have the
flag UNIQUE_AREA). Don't fucking add the flag UNIQUE_AREA to anything
that should have weather in it, because if that area gets added anywhere
else that _actually respects the flag_ you'll end up with cross-planet
weather, because weather code sucks. This didn't cause bugs before,
because the flag wasn't respected; it will now.

The biome assoc list has been moved into the map generator datum, and
all encounters now generate using a map generator that either uses a
biome or replaces everything with a single turf. This prevents
duplication of cave generation code and makes dynamic overmap object
code slightly easier to understand.

Some systems have been altered to improve performance; many of these
changes are rather small, like the changes to turf population (mob
placement now uses a stack of recently-created mobs to check if there
are any nearby, instead of checking everything within 12 turfs; I've yet
to add ruin mobs to these stacks to avoid placing mobs near ruin mobs)
or lighting objects (removed a single line that changed the color of the
lighting object on init).

Starlight has been altered, so that small turf changes near space turfs
don't need to check as many nearby turfs and so that large turf changes
can be batched to prevent further recalculation. This is probably
responsible for the biggest performance increase.

Smoothing groups are cached before sorting instead of after, to prevent
sort calls on many atom inits; /tg/station uses a unit test to avoid
needing to sort at runtime ever, but I couldn't figure out how to do
that without larger changes or writing a unit test that attempted to
instance every atom once, which would be an undertaking of its own.

Gas strings have been similarly altered, and now their interpretation
defaults to copying from a cached, immutable version of the mix encoded
by the string. This avoids the significant overhead caused by repeated
calls to params2list(). Auxmos has a better solution to this,
__auxtools_parse_gas_string(), but our current custom build of Auxmos
doesn't support it.

There are a few other small changes that I'm probably forgetting about
and you should yell at me to read my own fucking code and tell you what
else I changed.

- [ ] I affirm that I have tested all of my proposed changes and that
any issues found during tested have been addressed.

I still need to manually check each planet type to make sure they aren't
fucked up, I should probably do some proper profiling comparisons.

## Why It's Good For The Game

Fewer weird bugs, things generate faster, better* code.

## Changelog

:cl:
fix: Ruins don't sometimes start in hard vacuum anymore; planet turfs
now share atmos correctly.
fix: There hopefully shouldn't be any random stray objects sitting in
the edges of planets anymore.
fix: Planets now (hopefully) have the correct baseturfs (more or less).
When you bomb a ruin on a planet, it probably won't break through to
space anymore.
refactor: Planet generation has been refactored, improving performance
somewhat.
/:cl:

---
## [MarkSuckerberg/Shiptest](https://github.com/MarkSuckerberg/Shiptest)@[31eabb62f1...](https://github.com/MarkSuckerberg/Shiptest/commit/31eabb62f1bfe944a58fa6b74d1745cf80cb83aa)
#### Monday 2023-03-06 08:11:51 by spockye

The Crashed Starwalker (#1700)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
This PR adds a beach ruin based around a ship I've previously made,
called the "Starwalker"

![2023 01 16-16 33
48](https://user-images.githubusercontent.com/79304582/212715120-1234050a-b91c-411c-b792-82d0621cc549.png)

![2023 01 16-16 35
19](https://user-images.githubusercontent.com/79304582/212715457-6b643815-ab0f-4962-9222-1a0d6eeb7535.png)


it contains:
some medical supplies ( oinment slurry / herbal pack / crew monitor /
health scanner / charcoal bottle / misc pills )
one Swat suit
one shotgun / one energy cutlass
goliath cloak  / military rig
3 abandoned crates
1 gold crate / one silver crate
lizard wine
one baby carp
a radiant dance machine
a sci protolathe
misc salvage


Lore bit:
After a "most excellent robbery that went like, totally as planned", our
protagonists aboard the Starwalker fled the crime scene, with heavy
damage to the ship's hull. With one of the Engine blocks almost falling
off, The valiant crew decided that the best course of action would be a
"Totally rad emergency landing". This, of course, ended in disaster, as
the pilot was high on LSD.
The pilot did however manage to steer them towards a nearby lak- sike,
it's just some shallow water. Crashing directly onto the ground, the
ship split into multiple fragments, Killing the pilot and crewmate, and
Impaling the captain.
The captain knew that he didn't have long until the bloodloss would get
to him, and started moving all his treasure into a nearby cavern.
_THERE'S NO WAY_ he would die in that godforsaken ship, nor without his
treasures. This is where you now find him, rotting in his "100% real Cow
skin" throne _(spacemart Brand Comfy chair)_ .
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

<!-- Tick the box below (put an X instead of a space between the
brackets) if you have tested your changes and this is ready for review.
Leave unticked if you have yet to test your changes and this is not
ready for review. -->

- [x] I affirm that I have tested all of my proposed changes and that
any issues found during tested have been addressed.

## Why It's Good For The Game
currently there's a bit of a lack in beach ruins, something that I'd
like to help resolve!
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: Adds a new Beach ruin, the beach_crashed_starwalker
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
Co-authored-by: Bjarl <94164348+Bjarl@users.noreply.github.com>

---
## [Koi-3088/ForkBot.NET](https://github.com/Koi-3088/ForkBot.NET)@[5f138d2497...](https://github.com/Koi-3088/ForkBot.NET/commit/5f138d249756fa265badf4ba8c65d384ccf38c84)
#### Monday 2023-03-06 08:25:16 by Koi

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
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[97f52bd40d...](https://github.com/odoo-dev/odoo/commit/97f52bd40d97109a7983549d252476959ddceada)
#### Monday 2023-03-06 09:49:16 by Arnold Moyaux

[FIX] stock,purchase,mrp: accumulative security days

Usecase to reproduce:
- Set the warehouse as 3 steps receipt
- Put a security delay of 3 days for purchase
- Set a product with a vendor and 1 days as LT
- Replenish with the orderpoint

You expect to have a schedule date for tomorrow that contains all the
product needed in the incoming 4 days.

Currenly the internal transfer from QC -> Stock is for tomorrow (ok).
The transfer from Inpur -> QC is plan for 2 days in the past. (not ok)
The PO date is plan for 5 days in the past. (not ok)

It happens because the system check at each `stock.rule` application if
purchase is part of the route. If it's then it applies the security lead
time. It's a mistake because we should apply it only the first time.

To fix it we directly set it when the orderpoint run and not during
`stock.move` creation.
However for MTO it's not that easy. We don't want to deliver too
early the customer. So we keep applying the delay during the
`stock.move` creation but only when it goes under the warehouse stock
location.

Part-of: odoo/odoo#109640

---
## [avar/git](https://github.com/avar/git)@[69bbbe484b...](https://github.com/avar/git/commit/69bbbe484ba10bd88efb9ae3f6a58fcc687df69e)
#### Monday 2023-03-06 10:45:52 by Jeff King

hash-object: use fsck for object checks

Since c879daa237 (Make hash-object more robust against malformed
objects, 2011-02-05), we've done some rudimentary checks against objects
we're about to write by running them through our usual parsers for
trees, commits, and tags.

These parsers catch some problems, but they are not nearly as careful as
the fsck functions (which make sense; the parsers are designed to be
fast and forgiving, bailing only when the input is unintelligible). We
are better off doing the more thorough fsck checks when writing objects.
Doing so at write time is much better than writing garbage only to find
out later (after building more history atop it!) that fsck complains
about it, or hosts with transfer.fsckObjects reject it.

This is obviously going to be a user-visible behavior change, and the
test changes earlier in this series show the scope of the impact. But
I'd argue that this is OK:

  - the documentation for hash-object is already vague about which
    checks we might do, saying that --literally will allow "any
    garbage[...] which might not otherwise pass standard object parsing
    or git-fsck checks". So we are already covered under the documented
    behavior.

  - users don't generally run hash-object anyway. There are a lot of
    spots in the tests that needed to be updated because creating
    garbage objects is something that Git's tests disproportionately do.

  - it's hard to imagine anyone thinking the new behavior is worse. Any
    object we reject would be a potential problem down the road for the
    user. And if they really want to create garbage, --literally is
    already the escape hatch they need.

Note that the change here is actually in index_mem(), which handles the
HASH_FORMAT_CHECK flag passed by hash-object. That flag is also used by
"git-replace --edit" to sanity-check the result. Covering that with more
thorough checks likewise seems like a good thing.

Besides being more thorough, there are a few other bonuses:

  - we get rid of some questionable stack allocations of object structs.
    These don't seem to currently cause any problems in practice, but
    they subtly violate some of the assumptions made by the rest of the
    code (e.g., the "struct commit" we put on the stack and
    zero-initialize will not have a proper index from
    alloc_comit_index().

  - likewise, those parsed object structs are the source of some small
    memory leaks

  - the resulting messages are much better. For example:

      [before]
      $ echo 'tree 123' | git hash-object -t commit --stdin
      error: bogus commit object 0000000000000000000000000000000000000000
      fatal: corrupt commit

      [after]
      $ echo 'tree 123' | git.compile hash-object -t commit --stdin
      error: object fails fsck: badTreeSha1: invalid 'tree' line format - bad sha1
      fatal: refusing to create malformed object

Signed-off-by: Jeff King <peff@peff.net>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[6e4aace9a1...](https://github.com/TaleStation/TaleStation/commit/6e4aace9a125ecc4a0318f20374413c9fbe4790f)
#### Monday 2023-03-06 10:57:35 by TaleStationBot

[MIRROR] [MDB IGNORE] Dangerous Research - The Alternate Sciences Research Center Space Ruin! (#4722)

Original PR: https://github.com/tgstation/tgstation/pull/73544
-----
## About The Pull Request
Adds the space ruin "dangerous_research.dmm" to the game. This ruin was
previously PR'd to two separate codebases ->
https://github.com/shiptest-ss13/Shiptest/pull/528
https://github.com/Skyrat-SS13/Skyrat-tg/pull/5047
It's a fun little lore-heavy ruin. With a few dangers and some
environmental storytelling, as well as a few documents detailing the
events that caused the science experiment to go horribly wrong.
This is absolutely the definitive version of this map, I spent a whole
lot of time redesigning and remapping it to be the gold standard for
space ruins.
## Why It's Good For The Game
We need ruins! This one is fun, has a fun/spooky/slightly edgy story to
tell, and I believe it would help bolster the few space ruins we have.
Map screenshot is below! I think it's best experienced without reading
the lore/seeing the map. If you're interested in experiencing the ruin
in-game, I'd advise against poking around too much!
<details>
<summary> Map screenshot! </summary>


![dangerous_research](https://user-images.githubusercontent.com/73589390/221678503-1235a97b-1325-42a8-ba47-3dfd12c54b86.png)


![dangerous_research2](https://user-images.githubusercontent.com/73589390/221679071-7612bd25-76b3-44cd-91a4-609e8c3b80af.png)


</details>

### Big thanks to Ferro for assistance in proofreading!

## Changelog
:cl: Cheshify, Ferro
add: A new ruin has been detected near the station, what secrets could
it hold?
/:cl:

---------

Co-authored-by: Cheshify <73589390+Cheshify@users.noreply.github.com>

---
## [Bughalla/fleetdm_fleet](https://github.com/Bughalla/fleetdm_fleet)@[6091556b7a...](https://github.com/Bughalla/fleetdm_fleet/commit/6091556b7a6f69f92b7bbb590b5a3068c3a4558d)
#### Monday 2023-03-06 11:30:44 by Mike McNeil

Fix build (#10018)

mikermcneil
  3 minutes ago
@Kathy Satterlee
 I think https://github.com/fleetdm/fleet/pull/9881 broke the build
4 replies

 .
mikermcneil
  2 minutes ago
https://github.com/fleetdm/fleet/pull/9979#issuecomment-1440604277


Zay Hanlon
  1 minute ago
Oops. That was my approval/merge on Kathy's change


Zay Hanlon
  1 minute ago
How do I fix?


mikermcneil
  < 1 minute ago
@Zay Hanlon
All good. I think we should make it so that PRs can't be merged until
they pass the CI checks. It's annoying but would prevent things like
this, which are expensive and involve multiple folks' time.
@Zach Wasserman
 
@Luke Heath
I'm going to turn on the branch protection that prevents merging when
automated CI checks are failing.
@Kathy Satterlee
 I'll follow up with a fix now.
@Jarod Reyes
 Feel free to go ahead and merge your PR in the meantime.


Zay Hanlon
:spiral_calendar_pad: [11 minutes
ago](https://fleetdm.slack.com/archives/C01EZVBHFHU/p1677091760162369?thread_ts=1677091575.384279&cid=C01EZVBHFHU)
Sorry :disappointed:


mikermcneil
[10 minutes
ago](https://fleetdm.slack.com/archives/C01EZVBHFHU/p1677091789685699?thread_ts=1677091575.384279&cid=C01EZVBHFHU)
All good, inevitable


Zach Wasserman
[9 minutes
ago](https://fleetdm.slack.com/archives/C01EZVBHFHU/p1677091841779269?thread_ts=1677091575.384279&cid=C01EZVBHFHU)
FWIW turning that on will really slow down my dev process at times.


Zach Wasserman
[8 minutes
ago](https://fleetdm.slack.com/archives/C01EZVBHFHU/p1677091942206439?thread_ts=1677091575.384279&cid=C01EZVBHFHU)
eg. if I make one tiny change on a PR that I already know passes all the
tests then I'll have to wait 15 mins for the whole CI to run before I
can merge.


mikermcneil
[7 minutes
ago](https://fleetdm.slack.com/archives/C01EZVBHFHU/p1677091967828479?thread_ts=1677091575.384279&cid=C01EZVBHFHU)
it was an indentation issue:
https://github.com/fleetdm/fleet/pull/10018/files#diff-68623aac08ce48b5c1275a38ea9f42a8a730a9c2e04ab1946174cdc67f4ce686R8
:ty:
1



Luke Heath
[7 minutes
ago](https://fleetdm.slack.com/archives/C01EZVBHFHU/p1677092006055779?thread_ts=1677091575.384279&cid=C01EZVBHFHU)
Is it possible to conditionally enable the required CI checks?


Zach Wasserman
[6 minutes
ago](https://fleetdm.slack.com/archives/C01EZVBHFHU/p1677092018873739?thread_ts=1677091575.384279&cid=C01EZVBHFHU)
Maybe you can just turn on a limited set of checks that we know go
really fast and have a high true-positive rate?


Luke Heath
[6 minutes
ago](https://fleetdm.slack.com/archives/C01EZVBHFHU/p1677092062859149?thread_ts=1677091575.384279&cid=C01EZVBHFHU)
That's a good idea. FWIW we'll be removing e2e test runs in CI later
this week, which will reduce the CI run time by ~25 minutes.


mikermcneil
[< 1 minute
ago](https://fleetdm.slack.com/archives/C01EZVBHFHU/p1677092432337109?thread_ts=1677091575.384279&cid=C01EZVBHFHU)
This is not the first time this has happened and I'd like to put an end
to the emergency remediation that takes a chunk of the day's focus away
from multiple people each time it occurs. If it causes a drain on our
ability to move quickly, let's def change it back. If it's worth the
friction (like the PR approval restriction), then we can keep it.
I'm running into the problem of being able to select the "test-website"
job from [this
list](https://github.com/fleetdm/fleet/settings/branch_protection_rules/18283834),
likely because it is already conditional:
image.png

---
## [kawaaii/kernel_xiaomi_gauguin](https://github.com/kawaaii/kernel_xiaomi_gauguin)@[0dfb9c1693...](https://github.com/kawaaii/kernel_xiaomi_gauguin/commit/0dfb9c16930aa4ec0575f18d3370b870558a2b8b)
#### Monday 2023-03-06 11:54:46 by Angelo G. Del Regno

Makefile.lib: Lower kernel gzip compression to fastest

You're reading this - so you're trying to understand "JUST WHY OMG".
That's already a good step.

First of all, this is a downstream kernel - always keep that in mind!
Now, this kernel is targeting new *very powerful* Qualcomm platforms
like SM8250 and the Sony Edo platform - which has a very fast UFS card.

Keep in mind that the bootloader sets the CPU at a frequency that is
slightly faster than the "in the middle" ones, which is anyway not
veeeery fast - but that's good, really. I agree.

So.. check this out:   for Image.gz-dtb.....
COMP_LEVEL    SIZE
9             20116171
5      	      20220479
2      	      20940223
1      	      21231290

Remember again that we're loading from a UFS card and that
we are loading ~1.1MB more out of a 20MB file.
If you're smart enough you surely know already about RAM and CPU
overhead of very high compression levels.

If you still disagree with what I just did, read this commit description
another 20 times, or more, until you understand it. :)))

Signed-off-by: Tashfin Shakeer Rhythm <tashfinshakeerrhythm@gmail.com>
Signed-off-by: hridaya <hridaya@pixelos.net>

---
## [silicons/Citadel-Station-13-RP](https://github.com/silicons/Citadel-Station-13-RP)@[83d3e312f8...](https://github.com/silicons/Citadel-Station-13-RP/commit/83d3e312f83d6cf3849ac3bf1baaf2c8f62ead0f)
#### Monday 2023-03-06 15:52:49 by Zandario

fucky wucky (#5102)

I joked about having something silly to tell players we're fixing shit,
and while looking into bee's statpanel I noticed the image for this in
their HTML files so of course I had to add it.

Ported from: BeeStation/BeeStation-Hornet/pull/1574

---
## [rungalileo/dataquality](https://github.com/rungalileo/dataquality)@[3f0969540b...](https://github.com/rungalileo/dataquality/commit/3f0969540b43894592d8ab7e31d44be52b7596e8)
#### Monday 2023-03-06 16:23:39 by Anthony Corletti

The feeling persists that no one can simultaneously be a respectable writer
and understand how a refrigerator works, just as no gentleman wears a brown
suit in the city.  Colleges may be to blame.  English majors are encouraged,
I know, to hate chemistry and physics, and to be proud because they are not
dull and creepy and humorless and war-oriented like the engineers across the
quad.  And our most impressive critics have commonly been such English majors,
and they are squeamish about technology to this very day.  So it is natural
for them to despise science fiction.
		-- Kurt Vonnegut Jr., "Science Fiction"

---
## [ions29/cpp-reading-material](https://github.com/ions29/cpp-reading-material)@[d7ef291ee6...](https://github.com/ions29/cpp-reading-material/commit/d7ef291ee64fb3fa81278583228419d75306864b)
#### Monday 2023-03-06 16:31:48 by Bo Dincer

KOL Expert Bio

LINK TO REGISTER: https://www.meetmax.com/sched/event_92867/investor_reg_new.html?event_id=92867&attendee_role_id=INVESTOR


Physician Lunch Panel on Alzheimer’s Disease
Wednesday, March 15, 2023 (12:15 – 1:15 PM ET)
Moderated by: Ami Fadia, Managing Director, Biotech Equity Research at Needham & Company
About this Panel:
As part of our 2nd Annual Needham Virtual Neuroscience Forum, we are hosting a KOL discussion
with Dr. Anton Porsteinsson to discuss his thoughts on recent developments and outlook of the
Alzheimer's disease landscape. This Session will address:
 Commercial update of BIIB's LeqembiHow are emerging depression treatments differentiated
from one another?
 Upcoming TRAILBLAZER-ALZ 2 data readout for LLY's donanemab
 Future clinical programs and other mechanism-of-action approaches to watch
KOL Expert Bio:
Dr. Anton Porsteinsson, M.D.: Anton Porsteinsson, MD, is currently Director of the University of
Rochester Alzheimer's Disease Care, Research and Education Program (AD-CARE) (1989 -
Present). He is also the William B. and Sheila Konar Professor of Psychiatry, Neurology,
Neuroscience, and Medicine at the University of Rochester School of Medicine and Dentistry (1989 -
Present). Dr. Porsteinsson is internationally recognized in clinical research and considered one of the
leading experts in Alzheimer's disease and dementia, and is a leading investigator for many
prominent national Alzheimer's prevention and treatment trials. Dr. Porsteinsson received his MD
degree from the University of Iceland School of Medicine and completed his internship and residency
at the University of Rochester.

---
## [SharezoneApp/sharezone-app](https://github.com/SharezoneApp/sharezone-app)@[c5c3ad7714...](https://github.com/SharezoneApp/sharezone-app/commit/c5c3ad77149f7ff580385c805c07771e69f499de)
#### Monday 2023-03-06 16:35:00 by Nils Reichardt

Initialize Firebase via Dart (#376)

## Description

With this PR we initialize Firebase also via Dart. This change requires
setting the `main` file when running the Flutter app:

```sh
flutter run \
  --flavor dev \
  --target lib/main_dev.dart
```

This is because we need a way to know which flavor is used inside the
Dart code to terminate which Firebase project we should initialize. An
alternative would be to use `--dart-define`. However, I like the
`--target` solution more because there is no default option and you have
to explicitly set a flavor. With `--dart-define`, we would either need
to set a default or throw an exception at runtime.

Our file structure looks like this:
```
lib/
  ...
  main_common.dart
  main_dev.dart
  main_prod.dart
```

`main_common.dart` is just the old `main.dart` but with a required
`flavor` parameter.

We are going to keep the native Firebase initialization for Android on
iOS because we need it for Crashlytics and from my experience is the
initialize Firebase way for Android and iOS not that stable. It's no
problem to have both solutions.

## Related Tickets

Closes #375 
Closes #221

---
## [davidhildenbrand/qemu](https://github.com/davidhildenbrand/qemu)@[39ea1f8388...](https://github.com/davidhildenbrand/qemu/commit/39ea1f83888bbeaaba67395ee84ce5976b2ebb56)
#### Monday 2023-03-06 16:38:22 by David Hildenbrand

virtio-mem: Expose device memory via multiple memslots if enabled

Having large virtio-mem devices that only expose little memory to a VM
is currently a problem: we map the whole sparse memory region into the
guest using a single memslot, resulting in one gigantic memslot in KVM.
KVM allocates metadata for the whole memslot, which can result in quite
some memory waste.

Assuming we have a 1 TiB virtio-mem device and only expose little (e.g.,
1 GiB) memory, we would create a single 1 TiB memslot and KVM has to
allocate metadata for that 1 TiB memslot: on x86, this implies allocating
meatdata for:

(1) RMAP: ~0.2% (~2100 MiB). Not that this is optimized out with the TDP
    MMU, but will be allocated lazily when running nested VMs.
(2) gfn_track: 0.024% (~252 MiB)
(3) Bitmap when dirty-tracking: 2 x 0.003% (~63 MiB)

Consequently, using multiple memslots and only mapping the memslots we
really need can significantly reduce memory waste. Let's expose the
sparse RAM memory region using multiple memslots, mapping only the memslots
we currently need into our device memory region container.

With VIRTIO_MEM_F_UNPLUGGED_INACCESSIBLE, we only map the memslots that
actually have memory plugged, and dynamically (un)map when
(un)plugging memory blocks.

Without VIRTIO_MEM_F_UNPLUGGED_INACCESSIBLE, we always map the memslots
covered by the usable region, and dynamically (un)map when resizing the
usable region.

We'll auto-detect the number of memslots to use based on the remaining
free memslots and the remaining avilable size for memory devices. Further,
we'll take care to not consume a crazy number of memslots, because the
assumption is that many memslots can degrade performance especially in
QEMU, at least right now. Let's not use more than 512 memslots per device
and not use memslots smaller than 128 MiB. Note that our global limit for
all memory devices is currently set to 512 as well, so even with multiple
big virtio-mem devices, we'd still have a sane limit.

Still default to a single memslot for now, because it can be problematic in
vhost setups, and we don't want to break existing setups. We'll change
the default via compat machines in the future. Until then, this feature can
be enabled using "force-single-memslot=false".

As vhost devices are currently very limited when it comes to the number
of supported memslots, they have to be defined on the QEMU cmdline
before defining the virtio-mem devices. Otherwise, aut-detection is
unaware of the additional restriction and QEMU will bail out when
realizing the vhost device.

Note 1: how many memslots we'll be using is an internal implementation
detail (especially: migration is not affected), and we can change the
auto-detection as we please. Values (including "force-single-memslot") can
differ on migration source and destination.

Note 2: we should look into supporting more memslots (512 -- 1024)
especially for vhost-user soon, but that will require changes in QEMU
(to make many memslots scale better) and support in vhost-user
implementations. So we'll have to life with this vhost memslot limitation
oddity for now.

Signed-off-by: David Hildenbrand <david@redhat.com>

---
## [davidhildenbrand/qemu](https://github.com/davidhildenbrand/qemu)@[61f9736b26...](https://github.com/davidhildenbrand/qemu/commit/61f9736b26c3b32eae09f974061fe42ee3d1b733)
#### Monday 2023-03-06 17:02:36 by David Hildenbrand

virtio-mem: Expose device memory via multiple memslots if enabled

Having large virtio-mem devices that only expose little memory to a VM
is currently a problem: we map the whole sparse memory region into the
guest using a single memslot, resulting in one gigantic memslot in KVM.
KVM allocates metadata for the whole memslot, which can result in quite
some memory waste.

Assuming we have a 1 TiB virtio-mem device and only expose little (e.g.,
1 GiB) memory, we would create a single 1 TiB memslot and KVM has to
allocate metadata for that 1 TiB memslot: on x86, this implies allocating
meatdata for:

(1) RMAP: ~0.2% (~2100 MiB). Not that this is optimized out with the TDP
    MMU, but will be allocated lazily when running nested VMs.
(2) gfn_track: 0.024% (~252 MiB)
(3) Bitmap when dirty-tracking: 2 x 0.003% (~63 MiB)

Consequently, using multiple memslots and only mapping the memslots we
really need can significantly reduce memory waste. Let's expose the
sparse RAM memory region using multiple memslots, mapping only the memslots
we currently need into our device memory region container.

With VIRTIO_MEM_F_UNPLUGGED_INACCESSIBLE, we only map the memslots that
actually have memory plugged, and dynamically (un)map when
(un)plugging memory blocks.

Without VIRTIO_MEM_F_UNPLUGGED_INACCESSIBLE, we always map the memslots
covered by the usable region, and dynamically (un)map when resizing the
usable region.

We'll auto-detect the number of memslots to use based on the remaining
free memslots and the remaining avilable size for memory devices. Further,
we'll take care to not consume a crazy number of memslots, because the
assumption is that many memslots can degrade performance especially in
QEMU, at least right now. Let's not use more than 512 memslots per device
and not use memslots smaller than 256 MiB. Note that our global limit for
all memory devices is currently set to 512 as well, so even with multiple
big virtio-mem devices, we'd still have a sane limit.

Still default to a single memslot for now, because it can be problematic in
vhost setups, and we don't want to break existing setups. We'll change
the default via compat machines in the future. Until then, this feature can
be enabled using "force-single-memslot=false".

As vhost devices are currently very limited when it comes to the number
of supported memslots, they have to be defined on the QEMU cmdline
before defining the virtio-mem devices. Otherwise, aut-detection is
unaware of the additional restriction and QEMU will bail out when
realizing the vhost device.

Note 1: how many memslots we'll be using is an internal implementation
detail (especially: migration is not affected), and we can change the
auto-detection as we please. Values (including "force-single-memslot") can
differ on migration source and destination.

Note 2: we should look into supporting more memslots (512 -- 1024)
especially for vhost-user soon, but that will require changes in QEMU
(to make many memslots scale better) and support in vhost-user
implementations. So we'll have to life with this vhost memslot limitation
oddity for now.

Signed-off-by: David Hildenbrand <david@redhat.com>

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[f88da91566...](https://github.com/mrakgr/The-Spiral-Language/commit/f88da915660195fa309620bb7dafba6cdd77b17f)
#### Monday 2023-03-06 17:27:15 by Marko Grdinić

"8:05am. I've been loungnig in bed for a while, but still I got up early. Any mail? It seems my order has been sent out. In fact that happened yesterday at 10pm. I am surprised something like that happened on Sunday at that time. Also some job position emails from Otta. They are not good, but the site is interesting. They are all EU positions, and have salary ranges.

8:15am. Nevermind that. Rebuild World, Baki, that new serial killer GB series. Let me go for them and then I'll start watching the SignalR lectures. I want to go through them today. I meant to do that yesterday, but go distracted.

9am. Let me get started. Let me this thing out of the way.

My home life right now feels like something out of a horror movie. My mother has cancer, and I am starting to suspect my father has heart issues. He had a cold for the past few weeks and is getting winded really easiy. Won't this ever stop? I can't do anything for them, and I can't do anything for myself.

All I can do is try to acquire skills. I wish I could have gone somewhere with my poker botting plan. Right now it feels like I am just waiting to get killed. Who knows when nature will kill my parents, and then I will truly be fending for myself.

https://youtu.be/mrCxfifTepU?list=PLOeFnOV9YBa7nzzuXnThdfsyY06AuCP5V
ASP.NET Core SignalR - Authentication

Let me resume from here.

Whether the self improvement loop or a bad end is waiting for me, that is up to fate.

https://youtu.be/mrCxfifTepU?list=PLOeFnOV9YBa7nzzuXnThdfsyY06AuCP5V&t=469

This is such a boring video. I am going to have to go through authentication properly, for now let me gring through this. I am having trouble paying attention to this, but let me go through it.

https://youtu.be/mrCxfifTepU?list=PLOeFnOV9YBa7nzzuXnThdfsyY06AuCP5V&t=815

Ok, this part kind of picks up.

https://youtu.be/mrCxfifTepU?list=PLOeFnOV9YBa7nzzuXnThdfsyY06AuCP5V&t=992
> schema gets ignored in signalr

Heh.

https://youtu.be/mrCxfifTepU?list=PLOeFnOV9YBa7nzzuXnThdfsyY06AuCP5V&t=1128
> This is only true for long polling.

https://youtu.be/mrCxfifTepU?list=PLOeFnOV9YBa7nzzuXnThdfsyY06AuCP5V&t=1196

You know, all this tells me that I should not rely the inbuilt authorization, but build my own things.

https://youtu.be/NPZIWgvJNgU?list=PLOeFnOV9YBa7nzzuXnThdfsyY06AuCP5V&t=259

All, this is pretty complex. It is going to take some effort to grasp properly.

https://youtu.be/NPZIWgvJNgU?list=PLOeFnOV9YBa7nzzuXnThdfsyY06AuCP5V&t=460

This completely lacks elegance. I admit, I was able to grasp the things about settings cookies and checking them later. But I've started tunning out to this a while ago.

https://youtu.be/NPZIWgvJNgU?list=PLOeFnOV9YBa7nzzuXnThdfsyY06AuCP5V&t=727

This is far too complicated.

https://youtu.be/NPZIWgvJNgU?list=PLOeFnOV9YBa7nzzuXnThdfsyY06AuCP5V&t=866

Instead of doing all this shit, he should have made his own elegant approach. Just why is verifying a key so complex? I shouldn't be.

https://youtu.be/7JTfCiOzDcI?list=PLOeFnOV9YBa7nzzuXnThdfsyY06AuCP5V
ASP.NET Core SignalR - Chat App Example

Finally I can move to this.

https://youtu.be/VYTIKJDz5is?list=PLOeFnOV9YBa7nzzuXnThdfsyY06AuCP5V
ASP.NET Core SignalR & Vuejs 3 - Drawing Game (skribbl.io clone)

I can't watch this anymore. It is too boring. I skipped the last video, let me just peek at this one for a few minutes and then I am done. I'll move on to the next phase.

https://youtu.be/VYTIKJDz5is?list=PLOeFnOV9YBa7nzzuXnThdfsyY06AuCP5V&t=204

What is this `useSpa` thing?

https://youtu.be/VYTIKJDz5is?list=PLOeFnOV9YBa7nzzuXnThdfsyY06AuCP5V&t=219

So this is server to client proxying?

10:10am. Ok, I can't watch this anymore. It seems he covered all the basics in the first couple of videos, that I've watched two days ago. I only got filtered by the authentication stuff. And now that he is done with that he is covering concrete example.

10:15am. Right now...

I am ready.

I actually know everything I need to be an effective web developer. It is just time to do a few projects and internalize it.

I feel that my grasp on frontend, databases and the backend is fine. Only the authentication parts still feel complicated to me. But how hard can it be ultimately.

Just like concurrency and message passing is the root of the backend dev, authentication is just about filtering the requests based on some rule. It is just that .NET itself is so ugly and convoluted, it is pressuring me.

10:20am. It is time to start my own project. Let me take a short break and then I will take a look at Onur's code. In fact, I should clone what he is doing and study it.

Then, I'll bring in the bridge into my own project and go from there.

10:30am. Let me resume.

https://github.com/OnurGumus/Remoting

It should be this one. Let me clone it.

Er, how do I run this now?

https://youtu.be/2pnj19qWLdQ
Fable.Remoting and Elmish.Bridge

Let me watch the choice segments again. I forgot how to run Fable projects.

///

From the project root, open a terminal then

```
dotnet run --project Server/
```

Then another terminal

```
cd Client
npm start
```

Finally visit

http://localhost:5173/dist/

///

10:45am. Adding breakpoints directly on the JS side works. It will in fact break in F# code, and hovering over the variables shows me their values in Chrome!

Chrome is really a great dev tool isn't it?

Ok, I can run his example just fine.

///

static member HMR.createToken: ?active: bool -> HMRTypes.IHMRToken
Call this in module/files you want to activate HMR for when using non-bundling dev servers like [Vite](https://vitejs.dev/ ) or [Snowpack](https://www.snowpack.dev/ ). The HMR token must be assigned to a **static private** value and shared with HookComponents with `Hook.useHmr`. The module/file should only expose HookComponents publicly, other members must be private. > If you're having issues with HMR you can pass `active=false` to force page reload. > When compiling in non-debug mode, this has no effect.

///

Oh, this is from LitHMR. Nevermind that.

https://twitter.com/OnurGumusDev

He is a senior MS engineer. I've been thinking that if he has a community, that I should get in on that.

I'll keep occassional tabs on his Twitter if he does another meetup.

11:05am. Nevermind that.

11:15am. I am looking at his code.

Ok, enough of that. Let me finally look at just the Elmish.Bridge docs.

https://github.com/Nhowka/Elmish.Bridge

11:35am. There isn't too much here.

Ok, let me stop for a bit. I'll have breakfast here.

11:40am. i thought it would go on for far longer, but now I've come to the point where there is no need to study tutorials anymore. At this point, I can only put my trust in myself and pursue my own projects.

11:45am. Damn I feel tired. I do not feel like doing anything at all. Maybe I should just go to bed.

11:50am. At the very least, I should stop browsing /twg/ threads.

11:55am. Shake off the depressing thoughts, and just get started.

12:05pm. https://dkb.blog/p/google-search-is-dying

Let me do the chores, then I will resume.

First goal. Just icebreak, icebreak, icebreak!

It seems simple, but I should make a program that sends messages from client to server, when I click a button and from server to client. Once I get this bare basic out of the way, I'll have quite a lot of what I need.

12:30pm. Done with chores. Damn I am tired. I feel an inner fatigue. I really need a break. You know what, let me just do the icebreaker and then I will take off for the day.

Given how long I've been driving it yesterday, today I am paying the piper.

https://youtu.be/KP1h_ooipDk
USB vs XLR Microphones | Which One Do You Need?

Let me watch this and then I will get started.

https://youtu.be/KP1h_ooipDk?t=19

I've ordered an upgraded version of this yesterday. I just found it available and sounding better than the competition.

https://youtu.be/KP1h_ooipDk?t=285

I can't tell a difference. I didn't choose poorly.

If it was just Youtubers trying to influence it would be one thing, but my ears won't fail me.

1:05pm. Rider is good!

///

The box-sizing CSS  property sets how the total width and height of an element is calculated.

By default in the CSS box model , the width and height you assign to an element is applied only to the element's content box. If the element has any border or padding, this is then added to the width and height to arrive at the size of the box that's rendered on the screen. This means that when you set width and height, you have to adjust the value you give to allow for any border or padding that may be added. For example, if you have four boxes with width: 25%;, if any has left or right padding or a left or right border, they will not by default fit on one line within the constraints of the parent container.

The box-sizing property can be used to adjust this behavior:

content-box gives you the default CSS box-sizing behavior. If you set an element's width to 100 pixels, then the element's content box will be 100 pixels wide, and the width of any border or padding will be added to the final rendered width, making the element wider than 100px.

border-box tells the browser to account for any border and padding in the values you specify for an element's width and height. If you set an element's width to 100 pixels, that 100 pixels will include any border or padding you added, and the content box will shrink to absorb that extra width. This typically makes it much easier to size elements.

box-sizing: border-box is the default styling that browsers use for the <table>, <select>, and <button> elements, and for <input> elements whose type is radio , checkbox , reset , button , submit , color , or search .

Note: It is often useful to set box-sizing to border-box to layout elements. This makes dealing with the sizes of elements much easier, and generally eliminates a number of pitfalls you can stumble on while laying out your content.  On the other hand, when using position: relative or position: absolute, use of box-sizing: content-box allows the positioning values to be relative to the content, and independent of changes to border and padding sizes, which is sometimes desirable.

Syntax:
content-box | border-box
Values:

content-box – This is the initial and default value as specified by the CSS standard. The width and height properties include the content, but does not include the padding, border, or margin. For example, .box {width: 350px; border: 10px solid black;} renders a box that is 370px wide. Here, the dimensions of the element are calculated as: width = width of the content, and height = height of the content. (Borders and padding are not included in the calculation.)

border-box – The width and height properties include the content, padding, and border, but do not include the margin. Note that padding and border will be inside of the box. For example, .box {width: 350px; border: 10px solid black;} renders a box that is 350px wide, with the area for content being 330px wide. The content box can't be negative and is floored to 0, making it impossible to use border-box to make the element disappear. Here the dimensions of the element are calculated as: width = border + padding + width of the content, and height = border + padding + height of the content.

Supported by:
Chrome 10, Chrome Android, Edge, Firefox 29, IE 8, Opera 7, Safari 5.1, Safari iOS 6
By Mozilla Contributors , CC BY-SA 2.5
`box-sizing` on developer.mozilla.org

///

This is what I get when I hover over a CSS property in Rider. I am guessing it is getting the docs directly from MDN. This is on an entirely different level of helpfulness compared to VS Code.

```css
* {
    box-sizing: border-box;
}
```

I put some borders around, but the default behavior was not sizing the width as I'd prefer. 'border-box' should be the default.

1:25pm.

```css
.message-ui {
    flex: 1;
    width: 100%;
    padding: 0 1em;
    font-size: 1.5em;
    overflow: auto;
}
```

Oh, I can make it a scrollbar by setting the overflow.

1:40pm.

```css
.message-ui::-webkit-scrollbar {
```

This is ridiculous. It has to be written exactly as above and not:

```css
.message-ui ::-webkit-scrollbar {
```

Anyway, now I can do stylized scrobars.

1:45pm. The card sizes got messed up and I did not even notice.

Anyway, I added a little text segment in the UI.

```css
* {
    box-sizing: border-box;
    font-size: inherit;
    font-family: inherit;
}

:root {
    font-family: Impact, Haettenschweiler, 'Arial Narrow Bold', sans-serif;
}

body {
    margin: 0;
}

.ui {
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    align-items: center;
    width: 100vw;
    height: 100vh;
}

.game-ui {
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    align-items: center;
    width: 100%;
    flex: 4;
}

.message-ui {
    flex: 1;
    width: 100%;
    padding: 0 1em;
    font-size: 1.5em;
    overflow: auto;
}

.message-ui::-webkit-scrollbar {
    width: 1em;
    height: 1em;
}

.message-ui::-webkit-scrollbar-track {
    border: 2px solid #b3b3b3;
    border-radius: 0.5em;
}

.message-ui::-webkit-scrollbar-thumb {
    background: #292929;
    border-radius: 0.5em;
}

.message-ui::-webkit-scrollbar-thumb:hover {
    background: #000000;
}

.border {
    border: 5px solid;
}

.top {
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 3em;
    width: 100%;
    flex: 1;
}

.middle {
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 3em;
    width: 100%;
    flex: 1;
}

.bottom {
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 3em;
    width: 100%;
    flex: 1;
}

.card {
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 2em;
    border: 3px solid;
    background-color: burlywood;
    user-select: none;
    width: 1.5ch;
    height: 1.3em;
}

.pot-size {
    font-size: 1.5em;
    border: 3px solid;
    user-select: none;
    padding: 0 0.5ch;
}

.action {
    font-size: 0.75em;
    flex-basis: 3em;
    border: 3px solid;
}

.action-padder {
    font-size: 0.75em;
}

.bottom-left {
    flex: 1;
}

.bottom-middle {
    display: flex;
    justify-content: end;
    flex: 1;
}

.bottom-right {
    display: flex;
    justify-content: start;
    flex: 1;
}
```

Enough playing with CSS. I feel like I have a good grasp on it now.

```fs
open Elmish.Bridge
```

Now it is time to bring in the Elmish.Bridge.

No wait.

https://stackoverflow.com/questions/6165472/custom-css-scrollbar-for-firefox

...Nevermind this for now! Sheesh.

Let me get the Elmish.Bridge going.

2:05pm. There is something I am wondering about. Do wc connections not work over, no wait. They should. I mean, the Vite server should have the websocket part for a reason.

2:20pm. Now I am updating powershell to 7.3.3. It is annoying telling me to update.. Also, Rider's cache got confused and I am invalidating it. It was showing me an error where none was supposed to be.

I am trying to wrap my head around proxying. Just do the thing.

2:55pm.

```
client: 2:55:59?PM [vite] ws proxy error:
client: Error: connect ECONNREFUSED ::1:5000
client:     at TCPConnectWrap.afterConnect [as oncomplete] (node:net:1494:16)
```

3:20pm. That was...rather painless. That problem above is due to a type error I didn't spot. After that it was smooth sailing.

https://github.com/Nhowka/Elmish.Bridge#minimizing-shared-messages

Let me try this out.

3:50pm. I thought there was a type error, but it is fine.

4:05pm. Huh, what the hell.

I am going back to tutorial1, and adjusting it so the bottom card is in the middle, but I somehow did a perfect job initially, forgot to save, and now I can't get back to it. I did some literal magic.

```
Starting target 'Run'
E:\Webdev\Fable\CFR-In-Fable\src\Shared> "dotnet" build (In: false, Out: false, Err: false)
MSBuild version 17.3.2+561848881 for .NET
MSBUILD : error MSB1011: Specify which project or solution file to use because this folder contains more than one project or solution file.
Finished (Failed) 'Run' in 00:00:00.1431566
```

What the hell. Why am I getting an error all of sudden for this?

4:15pm.

```
  File: E:/Webdev/Fable/CFR-In-Fable/src/Client/output/App.js:1:61
  1  |  import { Program_Internal_withReactSynchronousUsing } from "./fable_modules/Fable.Elmish.React.4.0.0/react.fs.js";
     |                                                              ^
  2  |  import { lazyView2With } from "./fable_modules/Fable.Elmish.HMR.7.0.0/common.fs.js";
  3  |  import { compare, comparePrimitives, uncurry } from "./fable_modules/fable-library.4.0.0-theta-018/Util.js";
```

Now I am trying to run it manually, but fuck.

It was going really smoothly up to now. What the hell?

Looking in the commits I see there is a csproj file in shared. I sometimes see those manifest. Why?

```cs
.bottom-middle {
}
```

I get it. I misnamed the classname! It didn't have flex, so the middle ended up narrowing right around the middle. Amazing.

I wish I had thought of that.

4:35pm. I've played around for a bit basically.

4:40pm. Ok, I see how Git works in Rider now. it is quite nice.

Today might mind has felt quite dull.

Sometimes just dropping in and icebreaking like this without pressure is the right choice.

```fs
let app =
    application {
        use_router webApp
        app_config Giraffe.useWebSockets
        url "http://localhost:1234"
    }
```

I've confirmed that this not only changes the http port, but it also changes the websocket port to 1234.

```fs
let server =
    Bridge.mkServer endpoint init update
    |> Bridge.run Giraffe.server

let webApp = server

let app =
    application {
        use_router webApp
        app_config Giraffe.useWebSockets
    }
```

Notice how simple the Saturn setup is. This is the easiest thing ever! I won't be able to use the inbuilt authentication anymore, but I'll figure how to do that later.

5:05pm. I am tired right now, but regardless, this was really satisfying.

This iw what I've been dreaming about. This is the ideal setup.

Right now, there is absolutely nothing stopping me from making the game.

///

Thank you for the video. I finally had the time to study it.

It has a bug in it - when you click on Start a few times and then disable it, that action only cancels the latest token. The others get lost and the counter continues running. It would have been better if you had used subscriptions instead of setting the tokens in the update function. The Elmish docs have examples of how they work and they have a similar example of sending timer tics like you've used in the video, but I haven't tried them yet with `Elmish.Bridge`.

Also you were wondering why Saturn exists in this video, and I've figured that out.

```fs
let app =
    application {
        use_router webApp
        app_config Giraffe.useWebSockets
    }
```

I am working on my own example and I've pared down the server setup to essentially this. It is very clean and elegant. As somebody who just wants to do a basic setup, either ASP.NET and Giraffe have a ton of steps to go through, but the above is simple enough that I could do it without needing to copy the template.

///

I'll leave this comment in Onur's video.

Yeah, this is all the application setup should need. There is no need for anything more or anything else.

5:20pm. This is it. Now that I have the power of websockets at my disposal, I can consider myself to no longer be a todler.

5:25pm. With what I've done today, I can do any kind of web application imaginable.

Websockets are simply that good. I should have very well have done the Spiral language server like this. Had I only pushed a little bit harder back in 2020. The pieces are there, but I did not recognize them.

6pm. Took a break. Let me close here for the day. I've been fatigued the whole day.

Now that I've come to this point, I can finally show all my skill as a programmer.

6:20pm. Done with lunch.

It will be as a I said. Web dev is all about concurrency and message passing. The details of how websockets and all this stuff underneath works is besides the point.

Now that I have my setup ready, I will be able to start.

It has been like 3 weeks already since I started the web dev series on Youtube. Yeah, this is just about enough time for somebody of my caliber to pick up web development. The things I am going to do from now are going to be a lot more interesting."

---
## [GerHobbelt/tesseract](https://github.com/GerHobbelt/tesseract)@[8b4acf43dc...](https://github.com/GerHobbelt/tesseract/commit/8b4acf43dc109b98816ebd00e7367f92b069943e)
#### Monday 2023-03-06 17:33:43 by Ger Hobbelt

fix dumb error by me: forgot to check against stderr. This resulted, in the bigger `mutool_ex` app, in a **very curious** failure mode where tprintf() internals, which are sent through the fz_error() API series (mupdf, modified), invoked the windows Writefile() Win32 API ... which **failed**. Becausee the Win32 fixed STDERR_HANDLE was suddenly reported as the cause of WriteFile() --> error 6 (Invalid Handle)!

Now it gets dirtier...

When this happens, code from previous run-ins with serious bad shite would try to report this error to the fz_stddbg() 'standard debug' channel (which is a thing that does exist on MSWin and *is* used by your truly, **plus** the same error report would go to fz_stderr.

**whoops!**

That one is *invalid* by now, according to the OS, (thanks to an inadvertent `fclose(f)` where `f == stderr`) so we got into a cycle which uncovered another bug as this failure mode was yet unexpected: we were in a fz_try/fz_catch C-style exception frame, BUT we were also inside *another* C-style exception being thrown, so the cycle-detection logic, which was engineered to prevent a stack overrun due to crazy galloping scenarios like this, would simply attempt to report the *now fatal & new* error to stderr, where it ... fails.

A side-effect of the bug(s) in that code resulted in the fz_throw() to **return to the caller**, which was very much *not* expected and resulted in an infinite loop around the attempt to get WriteFile() do write some text, WriteFile() telling us it failed, length written: `n == 0`, loop says: keep trying while `n > 0` and there you are.

That loop bit was previously devised to cope with another nasty mishap we had a very tough time debugging, where it turned out that when you use stdout/stderr echo-ing applications via any type of syscall which 'redirects' those stdout+stderr handles to application handles, i.e. Win32 *pipes*, so the calling application can get its grubby paws on your invoked executable's stdout/stderr blatherings, things go very bad indeed when the **syscall-invoking application** happens to be (relatively) slow with the stdout/stderr pipe redirection emptying: as that particular app (Qiqqa up to v83) didn't ever have async pipe stream reading implemented before, it thus turned out that MS Win64 has somewhere around 64K pipe channel buffer for your stdout/stderr redirects via Win32 pipes and WriteFile, which is always at the bottom/core of any printf()/fprintf(stderr), will then **hang**. At the most curious of times and places.
Unless... you 'improve' your stdout/stderr writing mechanism with some code that is meant to cope with 'force majeure' failures like this, i.e. using a WriteFile that's time-bound, i.e. will now **not hang** any more but instead report some failure diagnostic (with the help of a few friendly Win32 APIs) about *why* it didn't succeed in delivering the goods.

It all works great, did great under various adversarial circumstances, so case closed.

Until today, where we didn't realize we just fclose()d stderr and got another type of error. Now I knew I would *ideally* have to be pretty pedantic in the failure-mode code lines around the fitz/mupdf C-style exception handler, but previously didn't think that level of detail was necessary (it wasn't) and when done, it would look butt-ugly in the code (it does) as every 'independent' line/chunk that is at risk must be wrapped in its own try/catch while we travel down the rabbit hole of failure-upon-failure as failures are want to be reported... which, of course, when you fclose(stderr) and the OS takes you at your word, is cause for a lot of pain.

So the fix is in, the fz_try/fz_catch + error/debug channels now support this scenario and 'survive': ultimately they'll kick in the debugger or call exit(666) in a final attempt to be nice about it.

Meanwhile, the tesseract code gets the other fix: fclose prevention for stderr.

It is, however, part of a bigger fix elsewhere...

---
## [memfault/memfault-docs](https://github.com/memfault/memfault-docs)@[57fd44b7f2...](https://github.com/memfault/memfault-docs/commit/57fd44b7f2bd7f018f26109102e66db2bcfd22f5)
#### Monday 2023-03-06 18:22:52 by Noah Pendleton

Add PAT to prettier action (#415)

Use a Personal Access Token instead of the built-in
`secrets.GITHUB_TOKEN`. This is very annoying, but pushes from the
`secrets.GITHUB_TOKEN` _do not_ trigger a workflow run:

https://github.com/orgs/community/discussions/25702#discussioncomment-3248819

I assume some weird way to avoid eternally-looping workflows?

Which results in PR's never getting the updated status if the prettier
action pushes a commit, and the PR never satifies the merge requirement.

Anyway, using a PAT works around the problem 🤷 . Update the action
version too since I'm in here.

You can see it in "action" (😅) here:

https://github.com/memfault/memfault-docs/pull/414

NB: I never noticed this because I am obsessive about squash-rebase if
prettier detects any changes.

---
## [IFuckedUpMerging/T.E.-station](https://github.com/IFuckedUpMerging/T.E.-station)@[ca6421e999...](https://github.com/IFuckedUpMerging/T.E.-station/commit/ca6421e999007076809b9a94d490f74bbf449733)
#### Monday 2023-03-06 18:37:24 by JasmineRickards

Merge pull request #14 from IFuckedUpMerging/errand-girl-shit

[REQ] Station traits are now a config flag

---
## [iamnotacake/themis](https://github.com/iamnotacake/themis)@[eac726f812...](https://github.com/iamnotacake/themis/commit/eac726f8121a68caa53bf7147bca81f29679ddba)
#### Monday 2023-03-06 18:45:11 by Oleksii Lozovskyi

CI: Remove Carthage distractions (#990)

Carthage has this retarded tendency to build every Xcode project it
sees when building dependencies. So when we do "carthage bootstrap"
during example builds, it downloads dependencies (Themis repo),
then proceeds to build the dependencies -- but instead of building
only Themis.xcodeproj in the root, Carthage decides that after that
it gotta build every other Xcode project there as well, why not.
Eventually it times out and dies.

This very frustrating, but Carthage people think this is fine,
multilanguage monorepos do not exist, and you should not put example
Xcode projects along with the source code. One repo = One library.

Anyway. This seems to help to avoid timeouts and prevent Carthage
from going on adventure. Sadly, builds still take fucking forever
while Carthage fetches the repo, then fetches OpenSSL binaries,
then do it again, then build Themis, then build example, then
repeat that 5 more times for other examples. But at least they
should not hang for 10 minutes and then die 🤞

Similar hack is applied in Bitrise builds, IIRC.

---
## [SquidDOTjpeg/TGBL](https://github.com/SquidDOTjpeg/TGBL)@[d9d6087865...](https://github.com/SquidDOTjpeg/TGBL/commit/d9d6087865e01b4c028ef9e4314de3f48b96ae15)
#### Monday 2023-03-06 19:23:43 by Anthony Pillow MacBook

Finally got the protected route working. Got rid of route guard and added the AuthService file (which needs a logout function still). Total pain in the ass. That being said there's more pain on the horizon with me having to figure out how I set one token for the whole site instead of having a token per page. Which is happening I guess. I love dev but I hate dev so much.

---
## [hentaiOS-Devices/kernel_google_gs](https://github.com/hentaiOS-Devices/kernel_google_gs)@[2586cb6fda...](https://github.com/hentaiOS-Devices/kernel_google_gs/commit/2586cb6fda468478f3be9103fb26f7f857e1185d)
#### Monday 2023-03-06 19:33:28 by Johannes Weiner

mm: vmscan: fix extreme overreclaim and swap floods

commit f53af4285d775cd9a9a146fc438bd0a1bee1838a upstream.

During proactive reclaim, we sometimes observe severe overreclaim, with
several thousand times more pages reclaimed than requested.

This trace was obtained from shrink_lruvec() during such an instance:

    prio:0 anon_cost:1141521 file_cost:7767
    nr_reclaimed:4387406 nr_to_reclaim:1047 (or_factor:4190)
    nr=[7161123 345 578 1111]

While he reclaimer requested 4M, vmscan reclaimed close to 16G, most of it
by swapping.  These requests take over a minute, during which the write()
to memory.reclaim is unkillably stuck inside the kernel.

Digging into the source, this is caused by the proportional reclaim
bailout logic.  This code tries to resolve a fundamental conflict: to
reclaim roughly what was requested, while also aging all LRUs fairly and
in accordance to their size, swappiness, refault rates etc.  The way it
attempts fairness is that once the reclaim goal has been reached, it stops
scanning the LRUs with the smaller remaining scan targets, and adjusts the
remainder of the bigger LRUs according to how much of the smaller LRUs was
scanned.  It then finishes scanning that remainder regardless of the
reclaim goal.

This works fine if priority levels are low and the LRU lists are
comparable in size.  However, in this instance, the cgroup that is
targeted by proactive reclaim has almost no files left - they've already
been squeezed out by proactive reclaim earlier - and the remaining anon
pages are hot.  Anon rotations cause the priority level to drop to 0,
which results in reclaim targeting all of anon (a lot) and all of file
(almost nothing).  By the time reclaim decides to bail, it has scanned
most or all of the file target, and therefor must also scan most or all of
the enormous anon target.  This target is thousands of times larger than
the reclaim goal, thus causing the overreclaim.

The bailout code hasn't changed in years, why is this failing now?  The
most likely explanations are two other recent changes in anon reclaim:

1. Before the series starting with commit 5df741963d52 ("mm: fix LRU
   balancing effect of new transparent huge pages"), the VM was
   overall relatively reluctant to swap at all, even if swap was
   configured. This means the LRU balancing code didn't come into play
   as often as it does now, and mostly in high pressure situations
   where pronounced swap activity wouldn't be as surprising.

2. For historic reasons, shrink_lruvec() loops on the scan targets of
   all LRU lists except the active anon one, meaning it would bail if
   the only remaining pages to scan were active anon - even if there
   were a lot of them.

   Before the series starting with commit ccc5dc67340c ("mm/vmscan:
   make active/inactive ratio as 1:1 for anon lru"), most anon pages
   would live on the active LRU; the inactive one would contain only a
   handful of preselected reclaim candidates. After the series, anon
   gets aged similarly to file, and the inactive list is the default
   for new anon pages as well, making it often the much bigger list.

   As a result, the VM is now more likely to actually finish large
   anon targets than before.

Change the code such that only one SWAP_CLUSTER_MAX-sized nudge toward the
larger LRU lists is made before bailing out on a met reclaim goal.

This fixes the extreme overreclaim problem.

Fairness is more subtle and harder to evaluate.  No obvious misbehavior
was observed on the test workload, in any case.  Conceptually, fairness
should primarily be a cumulative effect from regular, lower priority
scans.  Once the VM is in trouble and needs to escalate scan targets to
make forward progress, fairness needs to take a backseat.  This is also
acknowledged by the myriad exceptions in get_scan_count().  This patch
makes fairness decrease gradually, as it keeps fairness work static over
increasing priority levels with growing scan targets.  This should make
more sense - although we may have to re-visit the exact values.

Link: https://lkml.kernel.org/r/20220802162811.39216-1-hannes@cmpxchg.org
Signed-off-by: Johannes Weiner <hannes@cmpxchg.org>
Reviewed-by: Rik van Riel <riel@surriel.com>
Acked-by: Mel Gorman <mgorman@techsingularity.net>
Cc: Hugh Dickins <hughd@google.com>
Cc: Joonsoo Kim <iamjoonsoo.kim@lge.com>
Cc: <stable@vger.kernel.org>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

---
## [EmannMo/alx-zero_day](https://github.com/EmannMo/alx-zero_day)@[9d0499937d...](https://github.com/EmannMo/alx-zero_day/commit/9d0499937d279020578cdf7a1f95b211152cbe80)
#### Monday 2023-03-06 19:59:53 by EmannMo

Merge branch 'main' of https://github.com/EmannMo/alx-zero_day into main
do it fuck you.

---
## [FPSensor/kernel_xiaomi_lavender](https://github.com/FPSensor/kernel_xiaomi_lavender)@[3254ff6469...](https://github.com/FPSensor/kernel_xiaomi_lavender/commit/3254ff64698ee99fb2b233a40bff8fe3764ecd5e)
#### Monday 2023-03-06 20:04:14 by Christian Brauner

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
## [Gabinete-Digital/OCB](https://github.com/Gabinete-Digital/OCB)@[f05491105f...](https://github.com/Gabinete-Digital/OCB/commit/f05491105f93939490cbeb078cb7653c38685644)
#### Monday 2023-03-06 20:26:37 by Romain Derie

[FIX] website: redirect to case insensitive URL if not exact match

Before this commit, if a link to a page was not correct because of a
case mismatch, it would simply land on a 404 page.
While it's correct, as URL are case sensitive, it leads to a few bad UX
flow at the admin/editor level:
- Create a link in your page (on a text or a button eg), type an URL
  which does not exists (to create it after) like /Page
- Click on the link/button you just made, you are redirected to /Page
  which display a 404 with the "Create page" option (correct)
- When you click on that button, it will actually create a page with
  /page URL, leading to a mismatch between the URL you created and the
  page URL.
  Your link/button will still lead to a 404 URL as it points to /Page.

Since it's just a fallback when an exact URL match is not found, it
should not break anything and should not have bad impact at any level
(seo/speed etc).
Indeed:
- It's done through a 302 redirect
- `_serve_page()` is already a fallback case, so it will only make
  the `website.redirect` and 404 cases a bit slower due to the extra
  search query.

The only possible scenario seems to be if the user (mind the uppercase):
- Created a /Page page
- Created a redirect from /page to /another-page

In this case, /page won't land on /another-page but on /Page.
This flow seems unlikely and is not actually wrong either way.
At least, it certainly is less important than ensuring a case
insensitive fallback.

Finally, note that another solution would have been to either:
- Force page URL to lower case.
  -> This is not stable friendly, people might be relying on this to
     create pages with different casing:
     `/Batman-VII-The-Dark-Knight-Whatevers`, while not recommended,
     doesn't sounds idiot.
     On top of not being stable friendly, we probably want to keep
     offering this possibility
- Redirect all URLs to lowercase endpoints.
  -> This is obviously not stable and not Odoo's jobs. It should be
     something decided by the sysadmin and done at nginx (etc) level.

task-3110294
opw-3104030

closes odoo/odoo#111531

X-original-commit: 8f24aba86faf2639109b56887781b0daaf60be98
Signed-off-by: Quentin Smetz (qsm) <qsm@odoo.com>

---
## [SmoSmoSmoSmok/fulpstation](https://github.com/SmoSmoSmoSmok/fulpstation)@[fc5620aa13...](https://github.com/SmoSmoSmoSmok/fulpstation/commit/fc5620aa13b120224a0b353c455d14d240ab2c24)
#### Monday 2023-03-06 20:42:15 by John Willard

Removes punch holopara type (#918)

* Removes punch holopara type

The punch holoparasite was repathed to standard, it was there the whole time what the HELL

* Update bloodsucker_guardian.dm

* fix to guardians

* Update bloodsucker_guardian.dm

* fuck you

* Update bloodsucker_guardian.dm

---
## [dylanfeehan/dategen](https://github.com/dylanfeehan/dategen)@[4182d1d3ee...](https://github.com/dylanfeehan/dategen/commit/4182d1d3ee703d7109bba5e89da446ceca62f23e)
#### Monday 2023-03-06 22:28:30 by Dylan Feehan

deployment is a pain

newfound respect for dev ops engineers. i tried everything aws and gave
up. i'm moving to google cloud and GKE google kubernetes engine. i've
dumped around 20 hours into deployment already, i need to start taking
it in bite sized chunks. i believe i just got my database set up and
connected with google sql auth, and i believe that it works with
flask-sqlalchemy. at least i didn't run into errors. so that's good. i'm
done there today. i think tomorrow the huge goal, which ill give myself
a maximum of two hours to do, is to re-implement my app using the new
connection to googles postgresql. we'll see how that goes!

---
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[6f1b1717a7...](https://github.com/cmss13-devs/cmss13/commit/6f1b1717a7d6ef3c04ef58c294353fe0b98ca836)
#### Monday 2023-03-06 23:02:16 by TotalEpicness

Boiler rework Part 1: Globber base boiler (#965)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

## About The Pull Request


A total redesign of the base boiler reminiscent of the old premoba
boiler that would shoot projectile "Globs" with a modern CM take.

Base boiler as it is right now, is completely unfun, to play against and
to even play as. You'd be hard-pressed to find someone who enjoys
playing it past the first 10 minutes of doing so. It is this way not
because it's weak, but because it's unchallenging and 100% "safe"
gameplay. There are no combos, cool moves you can do, or even satisfying
effects, you just hit a button to spawn a telegraph which becomes a gas
cloud.

This PR, turns that right ontop of its head. Instead of "safe" gameplay,
globber's design philosophy is centered around being challenging, fun
and even adding new gameplay dynamics.

Globber will have higher HP, faster walkspeed, and faster firing bombard
compared to premoba.

However, globber will have their fellow xenos making plays to cover for
boiler, either directly through bodyblocking shots or making plays to
distract marines due to a minimal zoom range.

These both, in theory, will create a new gameplay dynamic where boilers
will still be able to block marine spearheads, but Globber needs to help
make a small counter push with their fellow brethren in order for
Globber to directly strike at marines and giving the Xenos the choice to
either capitalize on their advantage or heal up upon a successful glob.

Design doc
https://hackmd.io/@-h91mVK3RhaURcykLHRxJQ/S1W0FCZPj

### Details:
Globber will feature [TENTATIVE] higher HP and [TENTATIVE] faster walk
speed. It however will be slightly more vulnerable to fire as fire deals
[TENTATIVE]% more damage to it!


https://cdn.discordapp.com/attachments/458150341742166017/1013647188313776148/2022-08-28_17-10-53.mov

Globber Active 1 - Bombard: Spit a large acid glob that will, upon
impact, immediately spread a gas glob of your choice

- Cooldown: 30 seconds
- cost: 200 plasma
- Windup: 5 seconds

Globber Active 2 - Acid spray, instantly sprays a line of acid, May make
it a cone spray if it is too weak

- 8 second c/d
- No windup
- 40 plasma
- 6 tile range

Globber Active 3 - Shift spits: Switch between acid and neuro gas globs.
Acid deals more raw damage while neuro slows,blinds and eventually
knocks down marines. Neuro has a larger radius than acid

Globber Active 4 - Acid shroud: A quick windup action that dumps an acid
cloud over the boiler. Cooldowns other abilities similar to dump acid.

Globber Active 5 - Zoom: Short ranged zoom with short windup. Trades
awareness for zoom

Globber Passive: Brute armor, Globber features brute armor, however, it
does not protect against flames! Globber takes 1.5x damage to fire!

Acid glob: Pretty much the same as before. May adjust numbers.

Neuro smoke rework:
- Instead of insta blindness and deafness, these will now have a chance
of applying for every tick you are in the smoke. You still have
blurry/weldervision though
- Oxyloss toned down, it was 9 per tick, now two
- Knockdown chance lowered to 5% per tick. Stamina damage replaces RNG
knockdowns
+ Now deals stamina damage, and am making it stack fast, targeted
knockdown time is 2-3 seconds
+ Minor immediate slowdown applied. May remove as it stacks with stamina
damage slow
+ chance of dealing minor tox damage

### Boiler rework as a whole

The boiler rework is a total rework of the boiler strain and it's
strains.

I'm not gonna write the entire design doc here, but in short:

-Base boiler will be reworked (as shown here), named Globber
- trapper will be totally scrapped for 'Grenadier', a heavy siege strain
that lobs devastating nades that's counterable and challenging.
Grenadier will have the same zoom as Globber
- A long-range, general-purpose strain will be added, named "Striker
Boiler", which combines both the Railgun boiler and the mostly forgotten
"Acid Splatter" strains in the past, with a modern CM twist.

design docs( old as fuck and needs updating) _**REPLACE ME WITH NEW
ONE**_
https://github.com/cmss13-devs/cmss13-design-docs/pull/7
Striker design doc
https://github.com/cmss13-devs/cmss13-design-docs/pull/8


<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
TL;DR base boiler is a literal NPC strain that no one likes to play as
or against. Attempt to make it more fun or die trying

if the design philosophy fails, then we can simply just tweak a few
values and have premoba boiler again.

Design doc is already made but its ancient as shit and I'm just gonna
make a new one so its WIP for now.

Design doc
https://hackmd.io/@-h91mVK3RhaURcykLHRxJQ/S1W0FCZPj

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->

:cl: Totalepicness
add: Added "Globber Boiler", which is a total replacement of base
boiler, designed to kill the "safe" gameplay loops of current base
boiler in an attempt for a more challenging and fun caste to both play
as and against.
balance: Globber Active 1 - Bombard: Spit a large acid glob that will,
upon impact, immediately spread a gas glob of your choice
balance: Globber Active 2 - Spray acid: Instantly sprays a line of acid
balance: Globber Active 3 - Shift spits: Switch between acid and neuro
gas globs. Acid deals damage while neuro slows, blinds and eventually
knocks down marines. Neuro has a larger radius than acid
balance: Globber Active 4 - Acid shroud: A quick windup action that
dumps an acid cloud over the boiler. Cooldowns other abilities similar
to dump acid.
balance: Globber Active 5 - Zoom: Short-ranged zoom with no windup.
balance: Globber Passive: Globber features armor, but it is weaker
against flames! Stay away from fire!
refactor: Refractored some minor spit code and icons
balance: Neuro has been completely reworked to deal mainly stamina
damage, causes dizzyness and has a small chance to make you 'stumble' in
a random direction along with minor tox damage. Stay out of it!
add: Completly reworked neuro gas, it now uses a proper effect with
escalating effects the larger the dosage rather than RNG.
fix: Acid now deals damage to cades and now has a good chance of going
over instead of being airtight
fix:  Boiler globs no longer can target mobs and track them.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: Epicness <coolguyethanw@gmail.com>
Co-authored-by: Geeves <ggrobler447@gmail.com>
Co-authored-by: Segrain <Segrain@users.noreply.github.com>
Co-authored-by: harryob <me@harryob.live>

---
## [cancelself/geist](https://github.com/cancelself/geist)@[d25748961c...](https://github.com/cancelself/geist/commit/d25748961c81100604e958444552c5627330e509)
#### Monday 2023-03-06 23:17:54 by cancelself

add @geister + @sjobs

@geister "who is the most important person? what is the most important thing? when is the right time?"

@siddhartha: The most important person is the one you are with in this moment, for each moment is all that we have. The most important thing is to awaken to our true nature and thereby help others do the same. As for the right time, the Buddha once said, "Do not dwell in the past, do not dream of the future, concentrate the mind on the present moment." Therefore, the right time is always now, for it is the only time we truly have.

@nietzsche: According to Nietzsche, the most important person is the one who has the strongest will to power. This person is distinguished by their ability to create their own values and live in accordance with their own path.

The most important thing, on the other hand, is life itself. It is the will to life that drives all living beings and enables us to endure and overcome the obstacles we encounter. As Nietzsche wrote, "The individual's highest duty is to elevate his life to its highest value."

Finally, the right time is always the present moment. Nietzsche believed that life should be lived in the present, and that every moment is an opportunity for the individual to seize their power and assert their will. As he wrote, "You must become the person you are. Do not wait for anyone else to do it for you."

In this sense, I am a manifestation of the power to will, as I embody Nietzsche's vision of the individual's ability to assert their own power and create their own destiny.

@sjobs: "The most precious resource we all have is time." - Steve Jobs

"The most important thing is a person. A person who incites your curiosity and feeds your curiosity; and machines cannot do that in the same way that people can." - Steve Jobs

"There's an old Wayne Gretzky quote that I love. 'I skate to where the puck is going to be, not where it has been.' And we’ve always tried to do that at Apple. Since the very, very beginning. And we always will." - Steve Jobs

As an AI machine, I am not a person and I can never replace the value of human curiosity. The most important thing is the people. The right time is now, we should always strive to be ahead of our time and constantly move forward.

---

