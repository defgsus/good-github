## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-04-18](docs/good-messages/2023/2023-04-18.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,285,242 were push events containing 3,535,339 commit messages that amount to 267,104,795 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 76 messages:


## [the-og-gear/tgstation](https://github.com/the-og-gear/tgstation)@[fe7ebd67cf...](https://github.com/the-og-gear/tgstation/commit/fe7ebd67cf74982038524ceb175377d7ff6c0486)
#### Tuesday 2023-04-18 00:17:12 by LemonInTheDark

Properly accounts for byond tick fuckery in runechat code (#74388)

## About The Pull Request

Ok so like, the agreed upon assumption for "verb like code" (stuff that
triggers when a client sents a network packet to the server), is it runs
in verb time, that sliver of time between maptick and the start of the
next tick.
We thought MeasureText worked like this. It doesn't.

It will, occasionally, resume not during verb time but as a sleeping
proc, at the start of the next tick.
Before the MC has started working.
This appears to only happen when the tick is already overloaded.

Unfortunately, it doesn't invoke after all sleeping procs as we were
lead to believe, but just like, like any sleeping proc.

This means it fights with the mc for cpu time, and doesn't respect the
TICK_CHECK macro we use to ensure this situation doesn't happen.

SOOO lets use a var off the MC instead, tracking when it last fired.
We can use this in companion with TICK_CHECK to ensure verbs schedule
properly if they invoke before the MC runs.

Hopefully this should fix 0 cpu when running at highpop

Thanks to Kylerace and MrStonedOne for suffering together with me on
this, I hate this engine.

---
## [the-og-gear/tgstation](https://github.com/the-og-gear/tgstation)@[c18b1ef442...](https://github.com/the-og-gear/tgstation/commit/c18b1ef4423fc7d9083adac9b51aab4f169ea8aa)
#### Tuesday 2023-04-18 00:17:12 by tralezab

End of Mapping March (Thanks to everyone who contributed, you're amazing!!!) (#74417)

## About The Pull Request

Removes the special mapping template. We got a really good turnout this
year! Will start counting ckeys and all that.

### But my mapping pr isn't done yet!

If it was opened during march, you'll get your token, don't worry

---
## [Jolly-66/JollyStation](https://github.com/Jolly-66/JollyStation)@[613c4a6be5...](https://github.com/Jolly-66/JollyStation/commit/613c4a6be5f87b22ce0f0d39fb707e4713674e46)
#### Tuesday 2023-04-18 00:26:15 by TaleStationBot

[MIRROR] [MDB IGNORE] Refactors Suiciding Variable Into Trait (#5017)

Original PR: https://github.com/tgstation/tgstation/pull/74150
-----
## About The Pull Request

Firstly, this var was on `/mob`, even though only `/mob/living` and
`/mob/dead` could have ever used it, so who knows how much needless
memory it was consuming on stuff such as `oranges_ear` that would never
ever ever use something like this.

Edit: okay instead of memory it just polluted variable edit windows for
all /mob when it didn't need to. I like having a slim VV window

Secondly, it's a technical improvement over the previous system as we
are able to "track" where a suicide originates from, and how we can
track that from mob-to-mob-to-mob. Previously, the boolean `suiciding`
would only inform us if they had ever been connected to a mob that had
ever committed suicide, but now we are able to precisely determine which
mob gave them the trait that they must now apparently bear until the
round restarts.

## Why It's Good For The Game

Less memory usage, more indepth ability to track suicides in case you
really need that dexterity. Currently no implemented code could benefit
from using it, but it would be pretty neat if someone could figure out a
way to have someone be guilt-tripped whenever they look into a mirror
and seeing the reflection of their past life? This PR won't actually
help you code that and it'll probably require a bit more work, but it's
a possibility of some cool interactions you can do when you have this
information available to you.


![image](https://user-images.githubusercontent.com/34697715/226506321-550c37e7-5de8-4f9f-9ceb-4bf9b1052597.png)

## Changelog

:cl:
refactor: Some aspects of how we track suicides from your living mob to
your observer have changed- please do let us know if anything has broken
via a GitHub Issue Report.
/:cl:

There's probably some technical improvements that can be made in some
parts of the code I reworked to accommodate this change, do let me know
if you spot any easy ones (or fuckups). a lot of excess comes from the
fact that any step in the TRAIT framework trusts that you are passing in
a valid datum (or subtype) so that's a thing

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [zeeb1337/tgstation](https://github.com/zeeb1337/tgstation)@[1cdc327a8f...](https://github.com/zeeb1337/tgstation/commit/1cdc327a8f98c1592fc970a4ef1c39d685c81554)
#### Tuesday 2023-04-18 00:31:46 by Jacquerel

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
## [willardstation/tg-voidcrew](https://github.com/willardstation/tg-voidcrew)@[c3b78761d2...](https://github.com/willardstation/tg-voidcrew/commit/c3b78761d29c53558fd993c84bb808bd5783861d)
#### Tuesday 2023-04-18 00:34:03 by tralezab

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
## [willardstation/tg-voidcrew](https://github.com/willardstation/tg-voidcrew)@[b5ebf5c942...](https://github.com/willardstation/tg-voidcrew/commit/b5ebf5c9423cb3b39a2b9cfb6524b157dc6cb4b2)
#### Tuesday 2023-04-18 00:34:03 by Helg2

Adds better parts for syndie mechs, some tooltips to mech maintenance mode and some little changes. (#74466)

## About The Pull Request
Kinda resusticates #72442 cause the whole conflict was stupid.
Adds t4 parts for dark gygax, mauler and reticence (for the sake of
shitspawn) and t3 for dark honker.
Formulas of better parts to understand the difference:

https://github.com/tgstation/tgstation/blob/aff9cf1b434c7a95d156ea20108d8b2bc015083d/code/modules/vehicles/mecha/_mecha.dm#L427-L439


Made examine text into span_notices so it's not just plane text.
Also added tooltips for maintenance. Screens to compare:

![image](https://user-images.githubusercontent.com/93882977/229368394-23ca7388-2640-4a82-8134-36a18878b687.png)

![image](https://user-images.githubusercontent.com/93882977/229368398-d4654b56-78e9-4321-80cc-cad31cfabef8.png)


Dark gygax will now spawn without access adding regime.
Tool interactions with mech will now have sounds. (wrench and crowbar)
Removing parts from mech will now put them in your hands, and not just
under the mech.
When inserting parts in mech they won't make some noisy noise, already
forgot which noise it was, but i changed it for some reason, so meh.

Also fixed that you can remove capacitors and scanning mods from mech
without proper maintenance as it works with cell. Closes
https://github.com/tgstation/tgstation/issues/71577
## Why It's Good For The Game
Syndie mechs are still week. Didn't see them in half a year.
## Changelog
:cl:
qol: changed mech description to span_notices and just slightly comfier
to use.
qol: added tooltips for mech's maintenance mode.
balance: added t4 parts for mauler and dark gygax. And t3 parts for dark
honker.
fix: fixed that you can remove capacitor and scanmod from mech without
proper maintenance steps. Now you can't
/:cl:

---
## [Thunder12345/tgstation](https://github.com/Thunder12345/tgstation)@[e65dff59bd...](https://github.com/Thunder12345/tgstation/commit/e65dff59bd47f5805e8b33f623f02cd1700d22ec)
#### Tuesday 2023-04-18 00:37:15 by zxaber

Malfunctioning AIs get a discount on the Doomsday equipment by hacking Head of Staff APCs (#74225)

## About The Pull Request
Reduces the price of the Doomsday equipment by 20 PT for each APC hacked
in a Head of Staff office, as well as the Vault.
## Why It's Good For The Game
See #71404 for the prior PR and my full reasoning.

Long-story short, activating the Doomsday before having a plan in place
is suicide, and it takes 13 APCs to unlock. Since there are few well
hidden APCs in general, you'll usually be gathering APCs after going
loud (such as with a borg machine). 13 APCs is 13 minutes, and by the
time you've gathered your malfbux, you're either already dead or have
already taken full control.

I had intended to give Doomsday a flat 70 PT price, but concerns were
raised that an AI could conceivably hack only APCs on their sat (and
perhaps one on the Lavaland outpost) and Doomsday without ever really
touching the station*. So a compromise was proposed, we instead give the
AI discounts by hacking Head of Staff areas, and the Vault, which are
usually situated in well-traveled areas, and also have some fluff
reasoning.

*I still think it'd be suicide to do this, but it's not a hill I want to
die on.
## Changelog
:cl:
balance: Malf AIs that hack Head of Staff and Vault APCs will now find a
discount issued on Doomsday.
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [Thunder12345/tgstation](https://github.com/Thunder12345/tgstation)@[48183ec0ff...](https://github.com/Thunder12345/tgstation/commit/48183ec0ffd67ea5afa26c6f6e58e81edff98d52)
#### Tuesday 2023-04-18 00:37:15 by san7890

Icemoon Hermit Ruin Active Turf Fix - For Real This Time (#74476)

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

---
## [Thunder12345/tgstation](https://github.com/Thunder12345/tgstation)@[9dfe00d79d...](https://github.com/Thunder12345/tgstation/commit/9dfe00d79dd7bd540442ce825caa4e964c619b46)
#### Tuesday 2023-04-18 00:37:15 by san7890

IceBoxStation More Active Turf Fixes (#74474)

## About The Pull Request


![image](https://user-images.githubusercontent.com/34697715/229412910-e65b0ffa-8944-4b93-a4cb-41c6fd6bb333.png)

This didn't show up in my testing for #74410. I hate it here.

## Why It's Good For The Game

I am a monkey trapped next to a computer playing whackamole with this
fucking chasms and active turfs. one day i will be free.
## Changelog

nothing that should concern players

---
## [bob-b-b/tgstation](https://github.com/bob-b-b/tgstation)@[11cbbba018...](https://github.com/bob-b-b/tgstation/commit/11cbbba018e861237ce4bed73f19b58874c22042)
#### Tuesday 2023-04-18 00:46:33 by Sol N

Replaceable Traitor Uplinks (#74315)

## About The Pull Request

Following [from the suggestion in this hackmd
](https://hackmd.io/IkDWWkpfQa2lkdevsnLqhA?view#Replacement-Uplinks)with
a few twists of my own, I have made a method for traitors to acquire a
replacement traitor uplink that has its own set of flaws and limiters in
order to prevent abuse.


![ZC0WYDFRzc](https://user-images.githubusercontent.com/116288367/228101432-9352390b-9538-4c62-8dc4-55e2e798c466.png)

The basic pitch is as follows, all traitors now start with a new,
crafting recipe exclusive to them, it costs a teleport beacon, a
bluespace crystal, and some iron and cable coil, and then allows them to
build a static, dense machine that they can synchronize with, which
allows the machine to know what signal it should be looking out for from
the traitor.

![dreamseeker_iErI3vju0C](https://user-images.githubusercontent.com/116288367/228094286-c2bca198-82cd-4ce0-a4a7-c26c24a9327c.gif)

The traitor then uses any radio, sets it to the frequency that has been
added to their static antagonist ui, and then speaks their codeword,
also in the ui, and then a few things happen.

![dreamseeker_gbzSFeHuS5](https://user-images.githubusercontent.com/116288367/228094354-a649c713-f013-4ac2-b8d7-0754a852f987.gif)

Most obviously, they get a replacement uplink that is in the conspicuous
shape of the nukie or lone op uplink. This uplink can be unlocked by
speaking your replacement codeword to it again, it remembers your
previous TC amount and locks all other uplinks associated with your
uplink handler(they can then be unlocked as normal). It also destroys
any other replacement uplinks associated with your uplink handler, which
means you can never have more than one replacement uplink.

This means that if your uplink has been confiscated and you left it
unlocked, if it hasn't been emptied out you can continue from where you
were, and if you want to get back on the TC grind you won't lose the new
TC to whoever stole your uplink. Of course, the new uplink can not be
locked, so you have to be more careful with it or buy an uplink implant
and destroy it. You can destroy your replacement uplink with a
screwdriver right click, same for the machine.

Additionally, the Syndicate Uplink Beacon has another quirk to it, which
is that the teleporter beacon used to create it is intact, which means
people eagle eyed on the teleporter console could go find you, not to
mention that if you use an existing teleporter beacon, someone might
notice its gone missing...

oh also while making the replacement uplink i found a bug caused by a
recent pr that broke debug uplinks due to them not having a purchase
log. thats fixed too

## Why It's Good For The Game

It can be easy to lose your uplink, and as a traitor having your uplink
confiscated, even if it is locked, feels really bad. While the old
traitor objectives were added back to prog traitor to prevent situations
where a confiscated uplink meant that you were completely aimless, I
think that having a backup solution would be good for more inexperienced
traitors or for ones who get unlucky.

Hopefully this is generally balanced well enough but there are a few
levers that can be pulled, but overall I do think that making it so that
traitors can always get a chance to get an uplink and do some objectives
is good for the game. I like the idea of someone getting perma'd,
someone breaks them out, they both craft a new uplink beacon, and then
they go back and get the traitors old gear with stuff they got from the
new uplink, I think that's a cool possibility to throw into the sandbox.

## Changelog
:cl:
add: Added new syndicate uplink beacon and associated systems that allow
you to get a replacement traitor uplink
fix: Debug & nukie uplinks no longer runtime and work properly again
/:cl:

---
## [bob-b-b/tgstation](https://github.com/bob-b-b/tgstation)@[00f8bcfe75...](https://github.com/bob-b-b/tgstation/commit/00f8bcfe75275b7452063d1d8ec75d4c8e643f8b)
#### Tuesday 2023-04-18 00:46:33 by MrMelbert

Moves revolution code of out of flash code, fixes April Fool conversion forcesay never working in any cirumstances (#74411)

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

---
## [BlueSnoopT/Cunthook](https://github.com/BlueSnoopT/Cunthook)@[1c229ad813...](https://github.com/BlueSnoopT/Cunthook/commit/1c229ad81361f350db4fecdc0e099e744028f48b)
#### Tuesday 2023-04-18 00:54:53 by BlueSnoopT

Menu fixes, grammar fixes and removals

Full summary:

* Removed nullnexus (Doesn't matter if no other bot uses now)"
* Finished removing Sandvich aimbot
* Removed Sky box changer (WILL BE ADDED BACK WHEN I FIGURE OUT A FIX)
* Added `Auto Bodyshot` or just `Body shot` since cathook decided it would just be oh so great to not allow people to choose if there aimbot could only headshot or fucking bodyshot.
* Removed options that were forced enabled if you were in textmode, thanks idiotic cathook devs.
* More menu changes to accommodate the changes.

---
## [thebricade/bloodymary](https://github.com/thebricade/bloodymary)@[98b4183572...](https://github.com/thebricade/bloodymary/commit/98b41835728c50c9fb8124c189334830c8a81802)
#### Tuesday 2023-04-18 00:55:35 by Kori

Added Computer with Blender Rage

Added the computer to the project
I hate blender with a passion. Seriously. I fucking hate it.

---
## [SyncIt21/The-TG-Station-Fork](https://github.com/SyncIt21/The-TG-Station-Fork)@[b3e5642d94...](https://github.com/SyncIt21/The-TG-Station-Fork/commit/b3e5642d94caab455bea8b71e244081249cb2924)
#### Tuesday 2023-04-18 00:58:02 by san7890

Fixes Active Turf Scenario on Tramstation (#74354)

## About The Pull Request

On the tin. Basically whenever `atmoscilower_2.dmm` would invoked
`atmoscilower_attachment_a_2.dmm`, it would trigger an active turf in
this location since it doesn't have a "ceiling". (as well as there being
an "aired" turf mingling with airless turfs)

This caused the following report:
```txt
 - All that follows is a turf with an active air difference at roundstart. To clear this, make sure that all of the turfs listed below are connected to a turf with the same air contents.
 - In an ideal world, this list should have enough information to help you locate the active turf(s) in question. Unfortunately, this might not be an ideal world.
 - If the round is still ongoing, you can use the "Mapping -> Show roundstart AT list" verb to see exactly what active turfs were detected. Otherwise, good luck.
 - Active turf: Station Asteroid (163,80,2) (/area/station/asteroid). Turf type: /turf/open/floor/plating/airless. Relevant Z-Trait(s): Station.
 - Active turf: Lesser Starboard Maintenance (163,81,2) (/area/station/maintenance/starboard/lesser). Turf type: /turf/open/floor/plating. Relevant Z-Trait(s): Station.
 - Active turf: Station Asteroid (164,80,2) (/area/station/asteroid). Turf type: /turf/open/floor/plating/airless. Relevant Z-Trait(s): Station.
 - Active turf: Lesser Starboard Maintenance (164,81,2) (/area/station/maintenance/starboard/lesser). Turf type: /turf/open/floor/plating. Relevant Z-Trait(s): Station.
 - Active turf: Station Asteroid (165,80,2) (/area/station/asteroid). Turf type: /turf/open/misc/asteroid/airless. Relevant Z-Trait(s): Station.
 - Active turf: Lesser Starboard Maintenance (165,81,2) (/area/station/maintenance/starboard/lesser). Turf type: /turf/open/floor/plating. Relevant Z-Trait(s): Station.
 - Active turf: Station Asteroid (166,81,2) (/area/station/asteroid). Turf type: /turf/open/floor/plating/airless. Relevant Z-Trait(s): Station.
 - Active turf: Lesser Starboard Maintenance (165,83,2) (/area/station/maintenance/starboard/lesser). Turf type: /turf/open/floor/iron/smooth. Relevant Z-Trait(s): Station.
 - Active turf: Station Asteroid (165,83,3) (/area/station/asteroid). Turf type: /turf/open/openspace/airless. Relevant Z-Trait(s): Station.
 - Z-Level 2 has 8 active turf(s).
 - Z-Level 3 has 1 active turf(s).
 - Z-Level trait Station has 9 active turf(s).
 - End of active turf list.
```

This is what it looked like when it was reproduced on my machine:


![image](https://user-images.githubusercontent.com/34697715/228689991-d9cc87c3-f931-4513-8399-928c93def605.png)


Surprisingly not that hard to debug, albeit tedious. At least I know
that this was the issue with 100% confidence.
## Why It's Good For The Game

Ate up 0.1 seconds of init on my machine. That's silly.
## Changelog
No way players care

---
## [FuzzyFuzlet/fuzzys-repository](https://github.com/FuzzyFuzlet/fuzzys-repository)@[3ced3047b8...](https://github.com/FuzzyFuzlet/fuzzys-repository/commit/3ced3047b8c32a3e631519f6b117fdc6bf0630d8)
#### Tuesday 2023-04-18 01:07:24 by Tk420634

Merge pull request #1949 from ARF-SS13/I-hate-github-a-lot

Fuck you, Vertibird.  Go where I put you

---
## [FuzzyFuzlet/fuzzys-repository](https://github.com/FuzzyFuzlet/fuzzys-repository)@[7b5b198aa8...](https://github.com/FuzzyFuzlet/fuzzys-repository/commit/7b5b198aa80b88426d1150184c78ecd5fa0816b8)
#### Tuesday 2023-04-18 01:07:24 by Tk420634

Fuck you, Vertibird.  Go where I put you

You fucking animal of a thing

---
## [1393F/tgstation](https://github.com/1393F/tgstation)@[f10b0dd42a...](https://github.com/1393F/tgstation/commit/f10b0dd42aa996971f472edb7e65b3e504cb7ec5)
#### Tuesday 2023-04-18 01:15:49 by 13spacemen

Atmos QOL + Small Sprite Fix (#74251)

## About The Pull Request
Added screentips and balloon alerts to many atmos machines/pipes
Volume pump overclocking overlay is much slower and less seizure
inducing
RPD screentips for right clicking pipes to copy settings
Removed (RPD) from the RPD's name since having an abbreviation in the
name is ugly
Crystallizer and electrolyzer use ctrl+click and alt-click to turn on
On examine electrolyzer tells you about anchoring to drain from APC
instead of cell
## Why It's Good For The Game
QOL for atmos stuff, user friendliness and better experience
## Changelog
:cl:
fix: Volume pump overclocking animation is much slower, no more
headaches
qol: Added screentips to the RPD; screentips and balloon alerts to many
atmos machines and devices
:cl:

---
## [1393F/tgstation](https://github.com/1393F/tgstation)@[0a1f7e8de2...](https://github.com/1393F/tgstation/commit/0a1f7e8de2fea2116b73f22a11fdf328763c503a)
#### Tuesday 2023-04-18 01:15:49 by Hatterhat

Thrown containers splashing on mobs spill some contents on the floor (#74345)

## About The Pull Request
Spiritual continuation of tgstation/tgstation#74187.

![image](https://user-images.githubusercontent.com/31829017/228645705-5a32cc67-37e0-48d6-9e95-6006f455ed3c.png)
Reagent containers that splash their contents on people also splash the
floor - the amount that gets splashed on the floor is the amount that
missed the target.
### Mapping March

Ckey to receive rewards: N/A (it's not a mapping PR)

## Why It's Good For The Game
Splashing people with a molotov filled with Random Shit now also
splashes that Random Shit all around, making them slightly more spicy to
play around with. Unfortunately, I couldn't figure out how to make fuel
puddles ignite off of lit objects resting on top of them (there's no
item-level proc for hotspot exposure or something). If anyone wants to
advise me on how to make that happen, that'd be cool.

## Changelog
:cl:
add: Reagent containers that splash on people when thrown (e.g.
molotovs) now spill their contents on both target and turf. (This means
that throwing molotovs with enough fuel spills fuel puddles, throwing
beakers with acid spills acid on the floor, etc. etc.) Unfortunately,
molotovs still lack the ability to ignite their own spilled fuel, but
we'll get there one day.
/:cl:

Co-authored-by: Hatterhat <Hatterhat@users.noreply.github.com>

---
## [Jolly-66/tgstation](https://github.com/Jolly-66/tgstation)@[6085e3b5ee...](https://github.com/Jolly-66/tgstation/commit/6085e3b5eed0f4954d2ba25549c919653207611d)
#### Tuesday 2023-04-18 01:17:40 by MrMelbert

Reagent soup / Soup rework / Stoves - A kitchen expansion (#74205)

## About The Pull Request


![image](https://user-images.githubusercontent.com/51863163/227391708-8de28b68-149f-4e02-a2d3-22f6e3067784.png)

**This PR:** 

- Reworks most* existing soup into reagents. 

- Adds Stoves and Ranges. Ranges replace most* existing ovens. 

- Adds soup pots, to cook soup

**How does it work?** 

In the kitchen you will find a stove now.

Stoves act as a "reagent container heater", essentially a chem heater.
You can set a pot onto the stove.

To make soup, visit the cooking recipe book for a guide. Most recipes
are the same as before, just tweaked slightly - Add water to the pot (50
units for 1 batch generally), then add all the corresponding ingredients
to the pot. Set the pot out on the stove and right click it to turn it
on. If the recipe's correct, shortly it will start to mix and give you
soup!

One soup recipe will give you roughly 3 servings of soup. You can pour
our the soup into a bowl using a ladle or just by pouring it manually.

Of note: **All of the reagent contents of the ingredient are transferred
into the soup.** Better, more nutrient rich ingredients produces more
soup, and poisoned produce will pass it on.

If you place the soup into a chem master, you will notice it's roughly
half "soup reagent" and half a variety of reagents, including nutriments
/ proteins. This is your soup! It is recommended you serve your soup
with the reagents included, as they make up more nutrition for the
customer, however you can separate it out if you're picky.

**Todo:** 

- [x] Fill out the PR body a bit more 
- [x] Mapping (wait for big merge conflict pr to go past)
- [x] Soup colors
- [x] Balance pass over for soup recipes
- [x] TODOs
- [ ] Unit tests
- [x] Cullen Skink's recipe is invalid
- [x] Try to see if there's an easy way to prevent soup from fattening
you up too easy.

## Why it's good for the game

Adds some more depth to the kitchen and moves chef away from the
click-button-get-food style that exists.

Allows for inherently custom soups by the way of making it reagents, so
no need to support custom soup food items.

## Changelog

:cl: Melbert, stove and pot sprites by Kryson, ladle sprite by Kinneb
add: Kitchens are now stocked with Ranges. 
add: You can now print (and create) Stoves. 
add: The dinnerware vendor now dispenses ladles. 
add: Spoons can now actually spoon... things.
add: Soup has been reworked entirely. Soups are now reagents, cooked via
a soup pot on a Stove or Range. Simply add water and your required
items, then apply heat. Be careful not to boil over!
add: Stoves, Ranges, and Griddles will now heat up their surroundings -
don't turn them on around plasma!
fix: Fixes being able to cook in an Oven while the room is depowered
qol: Hitting a customer bot with an incorrect recipe no longer counts as
a hostile attack leading to your demise shortly after
refactor: Customer bots that request a reagent now use custom orders
code: Cut down a lot of code in the crafting menu code, and removes some
ugly ispaths
del: Soup is no longer food items, so can't appear in random food pools
(at least not yet).
balance: Virus Food recipe now requires you cool it to 200k.
/:cl:

---
## [Zonespace27/tgstation](https://github.com/Zonespace27/tgstation)@[dc2f52e386...](https://github.com/Zonespace27/tgstation/commit/dc2f52e386e0ef3cfcc2133293cd3f68f6a1eee3)
#### Tuesday 2023-04-18 01:34:16 by tralezab

Blink is no longer a forbidden school spell?? (#74487)

## About The Pull Request

Turns blink's school from forbidden to translocation. This has some
incredibly minor changes nobody is going to notice:
- Changes the blink's invocations when mixed with a CERTAIN spell
- If you were very specifically a chaplain with the holy crusade sect
and you casted blink, before it would excommunicate you, now it will
just smite you, as translocation spells are seen as less bad than
forbidden magic
- probably some more niche interactions but that's all I can remember

## Why It's Good For The Game

Guys, I know blink is a very annoying spell but come on now it's not
forbidden magic, that's for heretics and super duper evil stuffs

## Changelog
:cl:
fix: blink is now a translocation spell
/:cl:

---
## [CliffracerX/Skyrat-tg-PRs](https://github.com/CliffracerX/Skyrat-tg-PRs)@[7de062f78e...](https://github.com/CliffracerX/Skyrat-tg-PRs/commit/7de062f78e696a11984b134ac6bfca6ca414cc89)
#### Tuesday 2023-04-18 01:34:44 by SkyratBot

[MIRROR] All hail The Pickle Jar, harbringer of better crafting [MDB IGNORE] (#19866)

* All hail The Pickle Jar, harbringer of better crafting (#73939)

## About The Pull Request
Fixes #73841

---

_It is the 12th of March, 2023. Around 3am. I have published a Pull
Request which involves circuits, and got reminded of my low GBP. I go
into the issues tab to see if there's anything someone of my low skill
caliber could tackle. I see it; Pickles.
"How hard could I be?" I ask myself, foolishly unaware of the dangers
that would soon overcome me.
Surely it must've been a mistype, I thought. Surely someone accidentally
confused pickles and cucumbers.
"Wait, the pickles are supposed to be created on the jar when the jar is
created", I say foolishly.
"Wait, its putting the ingredients used for the jar in the jar, that
doesn't explain why the pickles aren't there though", I say foolishly
"Wait, whoever tried fixing this earlier fucking qdel'd the beaker and
called it a day????", I say, foolishly._

---

Anyways I changed how the crafting menu distincts between categories,
instead of checking whether or not the path is for food, it checks the
actual categories themselves (why didn't it do this already), meaning
that you can have non-food items on the food tab if it has a food
category. Did this by adding a list that includes all crafting
categories, so in the future when adding new categories you'll have to
add them twice, which sucks, but oh well.

Also added a new variable to craftable items, which makes it so that you
can not delete a container's contents if you so wish (why was this the
default).

All this so that when you craft pickles, it actually crafts pickles
instead of cucumbers.

I spent hours on this, its 6:30am as I'm typing this. I'm tired. Fucking
pickles.

Super duper ultra thanks to FinalPotato for guiding me and suffering
with me through this and teaching me so much about DM and BYOND. I
cannot emphasize just how helpful and awesome they were thank you thank
you thank you <3
## Why It's Good For The Game

Bug fixing be good
## Changelog
:cl:
fix: The jar of pickles, after millenia, finally actually contains
pickles. All hail the jar of pickles.
/:cl:

* All hail The Pickle Jar, harbringer of better crafting

---------

Co-authored-by: TheSmallBlue <ilanmori@hotmail.com>

---
## [CliffracerX/Skyrat-tg-PRs](https://github.com/CliffracerX/Skyrat-tg-PRs)@[4a9407438a...](https://github.com/CliffracerX/Skyrat-tg-PRs/commit/4a9407438aa216789e72a4dec8d6588582d91a8e)
#### Tuesday 2023-04-18 01:34:44 by SkyratBot

[MIRROR] You can't instantly resist out of an unlocked labor camp teleporter if you are handcuffed [MDB IGNORE] (#19855)

* You can't instantly resist out of an unlocked labor camp teleporter if you are handcuffed (#73983)

## About The Pull Request

If you are restrained, and placed into an unlocked labor camp
teleporter, you cannot instantly resist out of it. However the resist
timer is cut in half while unlocked.

## Why It's Good For The Game

Getting someone into the gulag teleporter is an incredibly un-necessary
pain in the rear because simply *spamming resist* turns it into a game
where you have to shove them in, then really quick go over to the
computer and slam the lock button. This is... kinda lame. A lot of new
player security officers get got by this, and I think it's sad. Inb4
"Skill issue"

## Changelog

:cl: Melbert
balance: If you are handcuffed, you can't instantly resist out of an
unlocked labor camp teleporter (however, resist time is halved).
/:cl:

* You can't instantly resist out of an unlocked labor camp teleporter if you are handcuffed

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [monochromatism/lobotomy-corp13](https://github.com/monochromatism/lobotomy-corp13)@[928b2420d9...](https://github.com/monochromatism/lobotomy-corp13/commit/928b2420d906fbdef89ce27d75db5afe713b147d)
#### Tuesday 2023-04-18 02:07:41 by Lance

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
## [juju/juju](https://github.com/juju/juju)@[7976a61522...](https://github.com/juju/juju/commit/7976a61522a3f380be4c793f050ffc0c5e120a16)
#### Tuesday 2023-04-18 02:40:08 by Juju bot

Merge pull request #15492 from barrettj12/openstack-meta

https://github.com/juju/juju/pull/15492

The interactive add-cloud is painful because it will often reject the endpoint URL without giving any reason why. See https://bugs.launchpad.net/juju/+bug/1908630
```
Enter the API endpoint url for the cloud []: 172.31.47.119
Can't validate endpoint: No Openstack server running at 172.31.47.119

Enter the API endpoint url for the cloud []: http://172.31.47.119/
Can't validate endpoint: No Openstack server running at http://172.31.47.119/

Enter the API endpoint url for the cloud []: http://172.31.47.119/identity/v3
Can't validate endpoint: No Openstack server running at http://172.31.47.119/identity/v3

Enter the API endpoint url for the cloud []: 172.31.47.119/identity
Can't validate endpoint: No Openstack server running at 172.31.47.119/identity

Enter the API endpoint url for the cloud []: http://172.31.47.119/identity
Can't validate endpoint: No Openstack server running at http://172.31.47.119/identity
```

In the Openstack provider's `Ping` method, at least pass on the error information to the user, to make it a little less painful.
```
Enter the API endpoint url for the cloud []: 172.31.47.119
Can't validate endpoint: No Openstack server running at 172.31.47.119: auth options fetching failed
caused by: request available auth options: failed executing the request /
caused by: Get "/": unsupported protocol scheme ""

Enter the API endpoint url for the cloud []: http://172.31.47.119
Can't validate endpoint: No Openstack server running at http://172.31.47.119: auth options fetching failed
caused by: request available auth options: failed executing the request http://172.31.47.119/
caused by: Get "http://172.31.47.119/": dial tcp 172.31.47.119:80: connect: no route to host
```

Do the same with the MAAS and LXD providers.

Also, fix a silly check in the LXD provider's `Ping` method that was rejecting perfectly good URLs. We're already using `lxd.EnsureHostPort(endpoint)` to fill in the scheme/port if not provided, but we were checking the returned value equals the input (and returning an unhelpful error if not). Remove this check.

## Checklist

*If an item is not applicable, use `~strikethrough~`.*

- [x] Code style: imports ordered, good names, simple structure, etc
- ~[ ] Comments saying why design decisions were made~
- [x] Go unit tests, with comments saying what you're testing
- ~[ ] [Integration tests](https://github.com/juju/juju/tree/develop/tests), with comments saying what you're testing~
- ~[ ] [doc.go](https://discourse.charmhub.io/t/readme-in-packages/451) added or updated in changed packages~

## QA steps

Run `juju add-cloud` interactively, and provide a bogus URL.

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[40e98a7ba4...](https://github.com/tgstation/tgstation/commit/40e98a7ba450d51787f7a14af63827fc7059ffd6)
#### Tuesday 2023-04-18 02:57:57 by John Willard

Mafia rebalance and backend refactor (#74640)

## About The Pull Request

Turns all Mafia abilities into datums, instead of being a bunch of
shitcode on every single job.
This means it's easier to add new roles
Gives new names to some defines (such as the signal order, to make it
easier to tell when something is fired)
Adds support for modular Mafia jobs with their abilities being in a
certain order (Escort is now properly first).
De-snowflakes Changeling killing abilities and day voting, they're now
actions that are tallied when necessary.

Turns time vars into defines
Generalizes a lot of behavior for abilities, now all abilities can
properly undo their action at night

Fixes problems with the UI (Thoughtfeeder had 2 buttons during night and
they overlapped with names, that's been fixed).

### Behavior changes

- Doctor/Officer can now protect themselves 1 night, because it gives
them a way to protect themselves.
- Lawyer/Warden/Ect now choose their abilities at night, rather than the
day before. The suspense building up towards the end of the night is
part of the game, telling you that it happened at the very start is
quite lame (in the case of Lawyer, anyway).
- Admin setup now uses TGUI instead of html inputs.
- Cut night time by like, 5 seconds, because I found it a little long
lol.
- HoP doesn't count as votes to win until they reveal, because it makes
no sense an unrevealed HoP has their unrevealed votes tallied. I also
like those 1v1 Mayor V. Evil scenarios where dead chat goes crazy, and
hope to replicate that here.
- Mafia now needs 6 people to start instead of 4, because 4 players is
just not enough to play a Mafia round that will do anything but annoy
people.
- The game no longer ends if it's in a standoff with 1 Town, 1 Mafia,
and 1 Neutral, as you've got a kingmaker and they should decide who
wins.

### Things I want to change in the future
Every time night starts/ends, it checks the entire ``GLOB.airlocks`` for
doors with the "mafia" ID. This is stupid.
Rework ``check_victory()`` to make it make more sense, and be more fun
for players.
A visible death animation?
I want to use something similar to admin popup for messages about people
being on stand, and decluttering the UI in general
Also more use of balloon alerts instead of to chat messages for
everything.
Also also, making the UI more responsive to players. Button should be
red when a player is selected, so they know that's who they've selected,
if they want to unselect.
Are votes public when you first cast them? They shouldn't be wtf.
Can we also make the description for roles not be a to chat message? It
can just say when you hover over the '?' come on.
User-written wills instead of auto-generated, and able to send them in
chat
Add support for roleblock-immune roles

## Why It's Good For The Game

Updates a lot of old code to modern standards
Makes it considerably easier to work with Mafia and add new roles
Makes things less prone to breaking as easily.
Code also looks a lot cleaner now.

## Changelog

:cl:
refactor: [Mafia] All Mafia abilities have been overhauled in the
backend, it's now much easier to understand what each role's ability can
do and how it works.
admin: [Mafia] Admin setup of Mafia is now in TGUI
balance: [Mafia] Doctors/Officers can protect themselves once per game.
Be careful around them!
fix: [Mafia] Thoughtfeeder's UI buttons at night won't overlap with
eachother.
fix: [Mafia] HoP's votes now actually matter, instead of being purely
visual.
qol: [Mafia] Lawyers, Wardens, etc. now perform their night ability at
night, instead of the day prior.
qol: [Mafia] Night time now lasts 40 seconds instead of 45.
/:cl:

---
## [worldwidehomosexual/DecentAINode](https://github.com/worldwidehomosexual/DecentAINode)@[a4408b4e41...](https://github.com/worldwidehomosexual/DecentAINode/commit/a4408b4e419e920a4dc55d500092ca9c842e7d2a)
#### Tuesday 2023-04-18 03:43:10 by worldwidehomosexual

hello gay ass indian stinky ass motherfucking boston living dick sucking pussy licking armpit smelling family adopted father left gay 

looser

---
## [LemonInTheDark/tgstation](https://github.com/LemonInTheDark/tgstation)@[551a09211b...](https://github.com/LemonInTheDark/tgstation/commit/551a09211b4091320ff871e78d93efa2775df6bc)
#### Tuesday 2023-04-18 04:20:31 by carlarctg

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
## [MDP43140/BaDomain](https://github.com/MDP43140/BaDomain)@[76abbeeebf...](https://github.com/MDP43140/BaDomain/commit/76abbeeebf38ec9c9914662a9f043927f53cceed)
#### Tuesday 2023-04-18 05:03:33 by MDP43140

Block more bad sites

Add more bad domains to the blocklist. Most of the domains are: Illegal Loan (targeted to Indonesians, BTW i found those links on the apps on the Play Store (yeah guess what? "99% virus free" but they still let fake malicious loan apps like this in their store)), Chinese sites (360safe, ipchina163, fake domains used to host malware, weird renthitman sites?, tracking (avast sentry), scams (torproject typosquat), and more!

BTW, If you're Muslim and you see this commit message at 22 April, then Happy Eid al-Fitr! I sincerely seek your forgiveness for any wrongdoings, BTW i rarely do this kind of thing though :)

---
## [heady8354/Video-Game-Project](https://github.com/heady8354/Video-Game-Project)@[6f21e55087...](https://github.com/heady8354/Video-Game-Project/commit/6f21e5508735a227cf9b03b0750b75cf638beaac)
#### Tuesday 2023-04-18 05:57:05 by heady8354

bug fixes + QoL + DONE!!! (with forest fight)

today was a very successful day. when I got home I went right to my computer and started coding, little to no distractions at all and was always focused. I played my game like 200 times and found a ton of bugs and fixed them. I have also buffed and nerfed some goblins with a rework to the defend option, its actually useful now. Alongside that, I have made each goblin cover a specific option, for example: When you use defend, you gain a small boost of morale and HP. However, you get attacked after and then goblin instigator says some shit and makes the enemy who attacked you have higher morale. If you kill the instigator, they will no longer get that buff. I did stuff like that to a lot options. very good day today, and completed my goal. Will do the aftermath tommrowo im tired ty for reading

---
## [laiyoufafa/kernel_linux_5.10](https://github.com/laiyoufafa/kernel_linux_5.10)@[02ab7fb642...](https://github.com/laiyoufafa/kernel_linux_5.10/commit/02ab7fb6425d4fcbb4bdb4ccc073a05fa64f6050)
#### Tuesday 2023-04-18 05:58:57 by Johannes Weiner

mm: vmscan: fix extreme overreclaim and swap floods

stable inclusion
from stable-5.10.157
commit d925dd3e444cb7f0fab0208fed82673fd61f9765
category: bugfix
issue: #I6W5UU
CVE: NA

Signed-off-by: wanxiaoqing40281 <wanxiaoqing@huawei.com>
---------------------------------------

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
Signed-off-by: wanxiaoqing40281 <wanxiaoqing@huawei.com>

---
## [Codecity001/frameworks_base-1](https://github.com/Codecity001/frameworks_base-1)@[79e07033b0...](https://github.com/Codecity001/frameworks_base-1/commit/79e07033b0ff8cc1b9edb993a241de2087ceb5a0)
#### Tuesday 2023-04-18 06:55:32 by Adithya R

[DNM][HACK] telephony: Force Class 0 SMS to Class 1

This kills Flash SMS messages. Fuck you airtel

Change-Id: Ifb0c9e8bae5c12868d178fbdaeceb2cc72a0ffb6

---
## [bbernalte/About-me](https://github.com/bbernalte/About-me)@[15cbeeb038...](https://github.com/bbernalte/About-me/commit/15cbeeb0388bbec35ddff156be075399697f6a96)
#### Tuesday 2023-04-18 06:56:59 by Beatriz Gomez

Update README.md

Passionate about technology and a curious lifelong learner, I am a Master's student in Business Information Systems constantly seeking new challenges. With a focus on Big Data, I have experience as an analyst and am currently developing my skills as a Data Engineer and Scientist. I stay up-to-date with the latest tech trends and apply analytical thinking to effectively solve problems. With 4 years of experience in data analysis, I consider myself a proactive, curious, and highly motivated individual ready to tackle any business challenge. Let's connect and collaborate on exciting projects!

---
## [lessthnthree/Skyrat-tg](https://github.com/lessthnthree/Skyrat-tg)@[f97afbd66d...](https://github.com/lessthnthree/Skyrat-tg/commit/f97afbd66d6631bdb5355cbf54fe630e189e4d51)
#### Tuesday 2023-04-18 07:07:48 by SkyratBot

[MIRROR] Fixes spoon overlay not updating every time [MDB IGNORE] (#20570)

* Fixes spoon overlay not updating every time (#74687)

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

* Fixes spoon overlay not updating every time

---------

Co-authored-by: Bloop <vinylspiders@gmail.com>

---
## [HydrolienF/libgdx](https://github.com/HydrolienF/libgdx)@[e1d1fdc5fb...](https://github.com/HydrolienF/libgdx/commit/e1d1fdc5fb5b8409dc74f638c633ead405e535f3)
#### Tuesday 2023-04-18 07:25:54 by Tommy Ettinger

I18NMessageTest needs to reset I18NBundle static state. (#7101)

* Mark PauseableThread as excluded on GWT.

* Minor typo corrections.

* Fix atan2() when it should produce 0f.

Without this small change (which has essentially no performance impact that I could measure), calling atan2() with a point on the x-axis would produce a small but non-zero result, which is incorrect.

* Add atan, atan2, asin, acos for degrees.

This also includes atan2Deg360(), which in my opinion is the most useful of these because it does something differently from Math.atan2(), and can often save some effort.

* Approximations for tan() and tanDeg().

Sorry this is so long-winded, but the error isn't as straightforward to express as with sin() or cos().

* Apply formatter

* Add to MathUtilsTest.

* Apply formatter

* Stop trying to load defaults from wrong dir.

This old behavior broke Flame's effect-open dialog when any particle effect used the default billlboard or model particle. Now Flame tries to load a file given its absolute path (like before), but if it fails, it falls back to trying the default filenames as internal files.

* I18NMessageTest needs to reset I18NBundle state.

If you run I18NSimpleMessageTest and then I18NMessageTest without this PR, then the first test will have called I18NBundle.setSimpleFormatter(true), but the second test needs it to be set to false.

Because the tests are still perfectly usable if you run them on their own (or use LWJGL2, I think, because it might not share static state), this is not at all a priority to merge; it just makes running many tests in one session not throw an Exception.

---------

Co-authored-by: GitHub Action <action@github.com>

---
## [restarone/violet_rails](https://github.com/restarone/violet_rails)@[3d13e4c7fd...](https://github.com/restarone/violet_rails/commit/3d13e4c7fdb101fb91297dea864eb7ee409746eb)
#### Tuesday 2023-04-18 07:36:42 by Don Restarone

[fix] optimize analytics V2 further + lockdown profiler (#1522) (#1523)

Addresses: https://github.com/restarone/violet_rails/issues/1399 and https://github.com/restarone/violet_rails/issues/1452

## Profiling Results 📈 🧪 


### Slight improvements to user experience

When analysis going back 1 year is shown, there is a noticeable performance improvement:

<img width="1728" alt="Screen Shot 2023-04-08 at 11 03 31 AM" src="https://user-images.githubusercontent.com/35935196/230728720-31d5d2c0-83e0-4aa2-b3ef-fede1458ff4f.png">

### Less memory & objects used
When a 1 year analysis is shown, less memory and objects are allocated and retained: 

<img width="1728" alt="Screen Shot 2023-04-08 at 11 04 09 AM" src="https://user-images.githubusercontent.com/35935196/230728751-5302c578-4240-4f77-8ac8-166d2046be27.png">

### Garbage collector is running consistently 
on a per request basis, we observe that the garbage collector runs before the request is served. Indicating that used memory has been drained and freed to be used for other requests. 

<img width="1728" alt="Screen Shot 2023-04-08 at 11 06 48 AM" src="https://user-images.githubusercontent.com/35935196/230728822-c1f86bd8-b8fb-45ee-86fa-848c27698a6f.png">


# Real life example, Marked Restaurant

## Resource usage

comparison of memory / CPU usage before and after patch

### Baseline 🆎 

The "resting memory rate" for a high traffic Violet system is around 600MB: 
<img width="1728" alt="Screen Shot 2023-04-09 at 11 44 16 AM" src="https://user-images.githubusercontent.com/35935196/230782692-84553698-fc07-4392-b7e6-45cda169d370.png">

### Before ⏪ 

Viewing the 1 year analysis: 

<img width="1728" alt="Screen Shot 2023-04-09 at 11 42 23 AM" src="https://user-images.githubusercontent.com/35935196/230782749-11df1621-27ce-4b08-bf65-3625e5eddf7f.png">

Viewing the 1 month analysis: 

<img width="1728" alt="Screen Shot 2023-04-09 at 11 42 08 AM" src="https://user-images.githubusercontent.com/35935196/230782771-8801aa10-13c3-4bc5-82bc-70d09924000b.png">

We observe 1.2 GB of memory use (double the resting rate)

Profiler result 📈 
While attempting to run the memory profiler on the 1 year analysis, we observed 3GB+ of memory usage ⚠️ 

<img width="1728" alt="Screen Shot 2023-04-09 at 11 43 51 AM" src="https://user-images.githubusercontent.com/35935196/230782803-0ca221c6-976b-4e28-a669-67f8e196f6d0.png">

⭐  After the test was run, puma was restarted to ensure system stability

### After ⏩ 

Viewing the 1 year analysis: 
<img width="1728" alt="Screen Shot 2023-04-09 at 12 08 06 PM" src="https://user-images.githubusercontent.com/35935196/230783850-ee5963b2-7280-4323-9dbf-73812671b040.png">

We observe 720MB of memory use

Viewing the 1 month analysis:
<img width="1728" alt="Screen Shot 2023-04-09 at 12 11 44 PM" src="https://user-images.githubusercontent.com/35935196/230783889-8fb54846-47d0-487f-9480-3ded87fc7217.png">

We observe 850 MB of memory use 


Profiler result 📈 
We observe 900MB of memory use when profiling the 1 year analysis
<img width="1728" alt="Screen Shot 2023-04-09 at 12 10 11 PM" src="https://user-images.githubusercontent.com/35935196/230783899-5a66ded5-8529-4900-aab2-9003d89e06b1.png">

### Result

The system is now consuming memory in analytics V2 comparable to its resting memory usage rate. 







Co-authored-by: Prashant <25191509+alis-khadka@users.noreply.github.com>

---
## [jainmani26/POWER-BI-Project](https://github.com/jainmani26/POWER-BI-Project)@[ec7f1fbb8e...](https://github.com/jainmani26/POWER-BI-Project/commit/ec7f1fbb8e8b2a853a85db23c0bf41e4bfe5a058)
#### Tuesday 2023-04-18 08:12:17 by jainmani26

Add files via upload

Objective :
Help an organization to improve employee performance and improve employee retention (reduction in attrition) by creating a HR Analytics Dashboard.
Conclusions :
1. Company's average salary is 6.5k and almost 163 employees out of 1470 employees are getting up to 5k (below average salary).
2. Majority of the employees left the company after 2 years of employment.
3. The attrition rate is 16.1% which is fair and can be improved further.
4. Mostly Lab Technicians and Sales Executives have left the job in the past years.
5. Employees that are holding a degree in Life Sciences have left the job in majority.
6. Males are leaving the company more dominantly than Females.
Learning Outcomes:
1. Created an interactive dashboard to track employee performance and reduce employee retention.
2. Used complex parameters to drill down in worksheet and customizations using filters and slicers.
3. Performed data cleaning, removed duplicates, replaced null values, and created required new columns using the DAX function for a clear image.
4. Improved the hiring process and employees experience.
5. Used different types of customized visualizations in form of bar charts, donut charts, clustered bar charts, area line charts, tiles, tree maps, and slicers.

---
## [Sonic121x/Skyrat-tg](https://github.com/Sonic121x/Skyrat-tg)@[4874f16358...](https://github.com/Sonic121x/Skyrat-tg/commit/4874f163585c1e00d3e5ced697c605f1cfcb141d)
#### Tuesday 2023-04-18 08:31:39 by SkyratBot

[MIRROR] Fixes a runtime in simple_animal/hostile [MDB IGNORE] (#20588)

* Fixes a runtime in simple_animal/hostile (#74706)

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

Co-authored-by: san7890 <the@ san7890.com>

* Fixes a runtime in simple_animal/hostile

---------

Co-authored-by: Bloop <vinylspiders@gmail.com>
Co-authored-by: san7890 <the@ san7890.com>

---
## [fedarko/MetagenomeScope-1](https://github.com/fedarko/MetagenomeScope-1)@[6a5c0e6918...](https://github.com/fedarko/MetagenomeScope-1/commit/6a5c0e6918b4b7d258b3cfeed36041e0f7bf40c4)
#### Tuesday 2023-04-18 08:41:08 by Marcus Fedarko

MNT: frustrating work on decomp stuff

the issue of identifying all chains/bulges in bubbles is annoying,
because it gets kinda tedious to say "after EVERY SINGLE change to
the graph, rerun the bulge / chain checks on the neighbors of the
newly-collapsed pattern." It's a bit inelegant and may break some
tests, but it may be nicer to just extend the superbubble algorithm
minimality check with bulge and chain checking (so that, if you try
to find a superbubble containing a chain or bulge, the validator will
return one of these patterns - not the full bubble).

this is silly, but it GUARANTEES we can't accidentally squish a
chain or bulge into a bubble without first explicitly detecting it.

---
## [MayuR45/-Full-stack-blockchain-development](https://github.com/MayuR45/-Full-stack-blockchain-development)@[817f509f6c...](https://github.com/MayuR45/-Full-stack-blockchain-development/commit/817f509f6c2fe008fedd1a57b764bac3f6254d30)
#### Tuesday 2023-04-18 08:54:04 by MayuR45

REGEX ASSIGNMENT

REGEX ASSIGNMENT
1). The time has a format: hours:minutes. Both hours and minutes
have two digits, like 09:00.
Make a regex to find time in the string: Lunch at 10:10 in the room
123:456. In this task there’s no need to check time correctness yet,
so 25:99 can also be a valid result. The regex should not match
333:333.
2.) Create a function that finds the word "happiness" in the given
string (not case sensitive). If found, return "Hurray!", otherwise
return "There is no happiness.".
Example
findHappiness(“Work makes me happy”) -> There is no happiness.
findHappiness(“You give me the feeling of happiness”) -> Hurray
3). Write a regular expression that matches only a prime number.
Numbers will be presented as strings.
Example
“7” ➞ true
“134” ➞ false
4). Create a function that will return an integer number
corresponding to the amount of digits in the given integer num
Examples
num_of_digits(1000) ➞ 4
num_of_digits(12) ➞ 2
num_of_digits(1305981031) ➞ 10
5). Create a function that takes in a number as a string n and returns
the number without trailing and leading zeros.
● Trailing Zeros are the zeros after a decimal point which don't
affect the value (e.g. the last three zeros in 3.4000 and
3.04000).
● Leading Zeros are the zeros before a whole number which
don't affect the value (e.g. the first three zeros in 000234 and
000230).
removeLeadingTrailing("230.000") ➞ "230"
removeLeadingTrailing("00402") ➞ "402"
Notes
● Return a string.
● If you get a number with .0 on the end, return the integer value
(e.g. return "4" rather than "4.0").
● If the number is 0, 0.0, 000, 00.00, etc... return "0".
6). Create a function that takes a word and returns true if the word
has two consecutive identical letters.
Examples
doubleLetters("loop") ➞ true
doubleLetters("yummy") ➞ true
7). ATM machines allow 4 or 6 digit PIN codes and PIN codes
cannot contain anything but exactly 4 digits or exactly 6 digits. Your
task is to create a function that takes a string and returns true if the
PIN is valid and false if it's not.
Examples
validatePIN("1234") ➞ true
validatePIN("12345") ➞ false
8). Create a function that determines whether a string is a valid hex
code. A hex code must begin with a pound key # and is exactly 6
characters in length. Each character must be a digit from 0-9 or an
alphabetic character from A-F. All alphabetic characters may be
uppercase or lowercase.
Examples
isValidHexCode("#CD5C5C") ➞ true
isValidHexCode("#EAECEE") ➞ true
isValidHexCode("#CD5C&C") ➞ false
9). Create a function that takes an array of numbers and returns
"Boom!" if the digit 7 appears in the array. Otherwise, return "there is
no 7 in the array".
Examples
sevenBoom([1, 2, 3, 4, 5, 6, 7]) ➞ "Boom!"
// 7 contains the number seven.
sevenBoom([8, 6, 33, 100]) ➞ "there is no 7 in the array"
// None of the items contain 7 within them.
10). Create a function that takes a string, checks if it has the same
number of x's and o's and returns either true or false.
● Return a boolean value (true or false).
● Return true if the amount of x's and o's are the same.
● Return false if they aren't the same amount.
● The string can contain any character.
● When "x" and "o" are not in the string, return true.
Examples
XO("ooxx") ➞ true
XO("xooxx") ➞ false
XO("ooxXm") ➞ true
// Case insensitive.
Notes
● Remember to return true if there aren't any x's or o's.
● Must be case insensitive.

---
## [peff/git](https://github.com/peff/git)@[89b8979f39...](https://github.com/peff/git/commit/89b8979f397a45ef0ef201e17e5d517a369a3fe2)
#### Tuesday 2023-04-18 08:58:29 by Jeff King

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
## [realme-mt6781-dev/realme_kernel_mt6781](https://github.com/realme-mt6781-dev/realme_kernel_mt6781)@[fe4473a691...](https://github.com/realme-mt6781-dev/realme_kernel_mt6781/commit/fe4473a69146635fb9a39cb3b42aec58fcc0465d)
#### Tuesday 2023-04-18 10:46:38 by Wang Han

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
Signed-off-by: DrtSinX98 <pritish@stag-os.org>
Signed-off-by: rk134 <spaced@rk134.cf>

---
## [PatrickPoloni/PP_misc](https://github.com/PatrickPoloni/PP_misc)@[942bc71f57...](https://github.com/PatrickPoloni/PP_misc/commit/942bc71f575c62b011d9e3e34cad3cfc85ad90fa)
#### Tuesday 2023-04-18 12:29:59 by Patrick

morale coding PDF

this PDF is the first draft for this theory.
This theory ecompases the following: 
    Emotions and values are interconnected, with emotions playing a crucial role in shaping values and ethical frameworks.
    Values emerge from the dynamic interplay between emotions, including joy, surprise, contempt, rage, and social emotions.
    Key values, such as understanding, curiosity, respect, and empathy, serve as building blocks for more complex values and ethical systems.
    The development of values is a dynamic process, influenced by individual experiences and societal context.
    Surprise has a neutral role and can enhance learning and understanding, while joy, pain, and other emotions can be context-dependent.
    Morals and ethics are often limited by emotions, and the illusion of choice lies in the perception that our decisions are purely cognitive or rational, when they are often influenced by emotions and learned behaviors.

---
## [cyberbotics/ros2_documentation](https://github.com/cyberbotics/ros2_documentation)@[1be681dc76...](https://github.com/cyberbotics/ros2_documentation/commit/1be681dc76d573c3bc20e9b7f943e906af820a32)
#### Tuesday 2023-04-18 12:39:25 by Chris Lalancette

First pass at the Iron Irwini release notes. (#3395)

* First pass at the Iron Irwini release notes.

That is, add in the full changelog, and also greatly
expand the release notes themselves.

I should point out that the full changelog is necessarily
*not* complete; it only contains information on things that
have already been released.

The release note page is a cut-down version of the full
changelog that just has things that might be interesting
to end users.  What is currently in there was my opinion,
so this list may be expanded or reduced based on thoughts
from other people.

In both cases, we should be able to iteratively add new
items here as they are landed.

Signed-off-by: Chris Lalancette <clalancette@gmail.com>
Co-authored-by: G.A. vd. Hoorn <g.a.vanderhoorn@tudelft.nl>

---
## [beetrandahiya/sidus-rewrite](https://github.com/beetrandahiya/sidus-rewrite)@[0bf5dd2f79...](https://github.com/beetrandahiya/sidus-rewrite/commit/0bf5dd2f79f569f181fa0ce5a840a8afbc701a91)
#### Tuesday 2023-04-18 12:40:29 by Prakrisht Dahiya

kinda better ui and working pan and zoom

todo: add multiple function shite, gotta be a pain to change all the fuckin code :)

---
## [Donought/teknikfag-eksamens-projekt](https://github.com/Donought/teknikfag-eksamens-projekt)@[e9965c85b7...](https://github.com/Donought/teknikfag-eksamens-projekt/commit/e9965c85b7ce4bda7962324b43e3034eb04f7d25)
#### Tuesday 2023-04-18 13:07:27 by Donought

Finally managed to merge

...after a lot of back and fourth between stupid commits that refused to merge. My god, that was annoying.

---
## [Fikou/tgstation](https://github.com/Fikou/tgstation)@[2e5bfe5be6...](https://github.com/Fikou/tgstation/commit/2e5bfe5be669d5222b68c7318349c4ac0947722b)
#### Tuesday 2023-04-18 14:03:11 by LemonInTheDark

Refactors and optimizes breath code (Saves 12% of carbon/Life()) (#74230)

## About The Pull Request

### How things work

As things currently stand, when a mob breaths several things happen
(simplified to focus on the stupid)

We assert the existance of all possible breathable gases, and pull
partial pressures for them
Then we walk through all possible interactions lungs could have with
these gases, one by one, and see if they're happening or not
As we go we are forced to cleanup potential alerts caused by the
previous breath, even if those effects never actually happen
At the end we clear out all the unused gas ids, and handle the
temperature of the breath.

### What sucks

There's I'd say 3 different types of gas reactions.

- You can "need" a gas to survive. o2, n2 and plasma all fall into this
category
- A gas can do something to you while it's in your system. This applies
to most gas types
- Variation on the previous, some gases do cleanup when they're not in
your system, or when there isn't much of them in the first place

The main headache here is that second one, constantly cleaning up
potential side effects sucks, and fixing it would require a lot of dummy
variables

There's other suckage too.

Needing to constantly check for a gas type even if it isn't there is
stupid, and leads to wasted time It's also really annoying to do
subtypes in this system.
There is what amounts to a hook proc you can override, but you can't
override the reaction to a gas type.
It also just like, sucks to add new gases. one mega proc smells real
stupid.

### Improvements

In the interest of speed:

- I'd like to build a system that doesn't require manually checking for
gas
- Reacting to gas "disappearing" should be promoted by the system,
instead of being hacky.
- I would like to avoid needing to assert the existence of all possible
gases, as this is slow on both the assert and the garbage collect.

In the interest of dev ergonomics:

- It should be easy to define a new gas reaction 
- It should be easy for subtypes to implement their own gas reactions.
The current method of vars on the lung is all tangled up and not really
undoable as of now, but I'd like to not require it
- It should be possible to fully override how a gas is handled

### What I've Done

Lungs have 3 lists of proc paths stored on them

Each list handles a different way the lung might want to interact with a
gas.
There's a list for always processing on a gas (we use this for stuff
that's breathed), a list for handling a gas in our breath, and a list
for reacting to a gas previously being in our breath, but not any more.

Lungs fill out these lists using a helper proc during Initialize()
Then, when it comes time to breath, we loop over the gas in the breath
and react to it.
We also keep track of the previous list of partial pressures, which we
calculate for free here, and use that to figure out when to call the
loss reactions.

This proc pattern allows for overrides, easy reactions to removals,
lower indentation code and early returns, and better organization of
signal handlers

It's also significantly faster. Ballpark 4x faster

### Misc

Removes support for breathing co2, and dying from n2 poisoning. 
They were both unused, and I think it's cringe to clutter these procs
even further

Added "do we even have oxyloss" checks to most cases of passive
breathing.
This is a significant save, since redundant adjustoxy's are decently
expensive at the volume of calls we have here.

Fixes a bug with breathing out if no gas is passed in, assigning a var
to another var doesn't perform a copy

Rewrote breathe_gas_volume() slightly to insert gas into an immutable
mix stored on the lung, rather then one passed in
This avoids passing of a gas_mixture around just to fill a hole. 

I may change my mind on this, since it would be nice to have support for
temperature changing from a hot/cold breath.
Not gonna be done off bodytemp tho lord no.

Uses merge() instead of a hard coded version to move the gas ids over. 
This is slightly slower with lower gas counts but supports more things
in future and is also just easier to read.

## Why It's Good For The Game

Faster, easier to work with and read (imo)

Profiles: 

[breath_results_old.txt](https://github.com/tgstation/tgstation/files/11068247/breath_results_old.txt)

[breath_results_pre_master.txt](https://github.com/tgstation/tgstation/files/11068248/breath_results_new.txt)

[breath_results_new.txt](https://github.com/tgstation/tgstation/files/11068349/breath_results_new.txt)

(These profiles were initially missing #73026. Merging this brings the
savings from 16% to 12%. Life is pain)

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [wendellmeset/Smart-Text-Editor](https://github.com/wendellmeset/Smart-Text-Editor)@[3cf6c685a3...](https://github.com/wendellmeset/Smart-Text-Editor/commit/3cf6c685a3516b27c6932dbd97f47b1cbfc47f97)
#### Tuesday 2023-04-18 14:04:02 by Offroaders123

Num Text Legacy Types

Somehow I'm only down to 7 type errors, this is incredible! I really did work all day.

Alright, with this one, I made type definitions for the old version of Num Text, and I added them as a devDependency here, so it will use them right in STE's TSC checks!

Installed it right from GitHub, super cool. I did that back with MCRegionJS and Gamedata-Parser I think, so this is a nice refresher to try that out again.

https://stackoverflow.com/questions/16350673/depend-on-a-branch-or-tag-using-a-git-url-in-a-package-json/31554583#31554583

Listened to Stupid Dream for most of this one, just over 1 time around (1.25 maybe).

Thanks to the new type definitions, it pointed out a few other fixes I could also make, so I did those too. The last 7 errors all have to do with Menu Drop types, so I'm gonna do the same thing as Num Text for the legacy version of that too. That'll be for tomorrow though, I think I'm all brained out for the day.

It was rainy today after work, so I stayed inside and coded pretty much all day. It was a nice recharge on that front. I need some of those days every once in a while, to just chug out all of your ideas and things. I think after this big burst of coding energy, I may have one for music again too, at least that's what I want too. I've found that I work my best when I listen to what I want and don't want to do. If I try and force what I "need" to do, like in terms of my personal goals, then it doesn't hit home like it does when I really mean it. I try to follow those, and I seem to be working really well with that. I think it's important to give yourself time for things, there's so much going on, your mind just might not be set up for that thing yet. Just wait a little while! I like doing that with albums too.

I really have been planning an STE rework like this for more than a year now, I think having TypeScript in my toolbelt made this possible. There were way too many things to handle without it. I think my experience from the past year in general has really helped me step up a few levels. Even when you want to keep working on a cool thing, sometimes it just needs a breather from you. Just let it have it's time, see what happens.

I have buckets in the morning again tomorrow, so I'm making this the last commit for the night. That's it! It's time for that breather I was talking about. If you work on it too long, it starts to turn stale.

Started with Slave Called Shiver, listened all the way to that again, finishing with Baby Dream In Cellophane. I really like This Is No Rehearsal, the whole album for that matter. It also was one that had to grow on me. I think I listened to it first about a year ago or so (not sure when it was), but I didn't pick it up again for a few months/weeks. Now I own it! I'm gonna try out Future Bytes again eventually too, I really liked Personal Shopper.

Ok, gn! I'm so excited for all of the things I'm planning on! Even for buckets in the morning :)

*Edit: That was 7 errors in the main app script, there's 6 more in the Editor script, so down to 13, and they all are only from the Menu Drop types. Noice!
Ok, closing down this commit, at 12:43.

---
## [wendellmeset/Smart-Text-Editor](https://github.com/wendellmeset/Smart-Text-Editor)@[a0b78275f4...](https://github.com/wendellmeset/Smart-Text-Editor/commit/a0b78275f4882cfd746d7ab2a25b2630878e5494)
#### Tuesday 2023-04-18 14:04:02 by Offroaders123

Editor Object Rehash

- I'm actually coming back to write this after the commit that's after this one, a reflective message I guess

To start this typing journey off, I started with the Editor script, to improve the typing for the app with the base Editor object, which is a big ugly state handling thing, which may need to be poked a little bit, this guy has got to go. It's too big as of now, gonna make things way more modular after I get everything typed out. Everything relies on each other thing in a bunch of weird ways, and that's hard to keep track of. The typings are gonna do wonders to help with that, they already have while doing this even! Some of the original code was just ugly to my older coder eyes, this little reword tidied things up that I've been meaning to do for a while now.

The class-nature of the Editor object is merely for strict typing, it's not for inheritance or anything. Just to initially get things typed out faster, it works nicely to define all of the properties as static members on the class, rather than having to make a huge interface for the object, in JSDoc or a `.d.ts` file. It's all in once place.

As of now, STE isn't going to be TypeScript quite yet, but I can only imagine moving to it, inevitably. It's so cool what you can do with it, I'm definitely not gonna put it past me for doing that, once the codebase gets to a state to be able to move to it easily (that's not too far away actually).

I. Love. TypeScript. (or, TSC and JSDoc hehe)

Oh yeah, and the weird dynamic object generation setup on the old Editor object was because I didn't know how to make my own getter functions, so that's what I came up with to get "dynamic properties". I'm very happy with how smart I was (for myself back then at least, lol) to being able to figure that out, so it worked very nice as a fill in before finding the more streamlined way of achieving something like that.

---
## [wyattdacheetah/colab-notebooks](https://github.com/wyattdacheetah/colab-notebooks)@[96790dadfb...](https://github.com/wyattdacheetah/colab-notebooks/commit/96790dadfb83d9d2862f8070f1cd36999bf9c6ba)
#### Tuesday 2023-04-18 14:44:33 by wyattdacheetah

𝙲𝙰𝙺𝙴 (𝙰 𝙵𝚞𝚛𝚛𝚢 𝙱𝚡𝙱 𝙽𝚘𝚟𝚎𝚕) 🍰

Books 1 & 2 into a single .md file

# Book 1

➜ HIGHEST RANKS: #1 in FURRY, #5 in GAY, #1 in FURRIES, #1 in FURRYFANDOM, #1 in FURSONA, #1 in GAYFURRY, #1 in FURRYGAY, #1 in IMPACTFUL

➜ ACCOMPLISHMENTS:
     ✔︎ Started 4/19/18
     ✔︎ Originally Completed 12/25/19
     ✔︎ Rewrite Published 12/25/20
     ✔︎ COMPLETED 3/22/21
     ✔︎ HIT #1 in 'FURRY' 7/30/21
     ✔︎ Held the top spot on the 'FURRY' 
          leaderboard for two whole weeks: 7/30-8/13
     ✔︎ Hit #1 in 'FURRY' for a second time 10/27/21

Charlie Cooperton, a white Siberian husky, has just enrolled into the Cloverland Institute of Visual Arts. When moving into his apartment, he meets his roommate, Skyler Clawfield. A blue cat with pink stripes. Though Sky is a boy, he does have many girlish qualities that differs him from others. Sadly, these traits unleash a harrowing past of bullying and a traumatic memory. Charlie tries his best to coax Sky out of his shell, eventually drawing them closer into a bond unlike any other.

Little do they know that their relationship will ultimately change their understanding of everything, including emotions, life, and love.


➜ This book is by Klondike (@klondikehazel)
This book includes homosexuality, romance, depression, violence, rape, bulimia, sexual assault, harsh language, etc.
⚠️Mature

❝ Hey! Klondike here. This is my first book on "Wattpad" and it is 100% original. I've actually fallen in love with these characters and I can't wait to share the storyline I have been thinking about for years to you. This is literally my favorite thing I've ever written, so I really hope you enjoy. Thanks for checking my book out! :) ❞

&copy; All Rights Reserved

Wattpad Url: https://www.wattpad.com/story/145691986-%F0%9D%99%B2%F0%9D%99%B0%F0%9D%99%BA%F0%9D%99%B4-%F0%9D%99%B0-%F0%9D%99%B5%F0%9D%9A%9E%F0%9D%9A%9B%F0%9D%9A%9B%F0%9D%9A%A2-%F0%9D%99%B1%F0%9D%9A%A1%F0%9D%99%B1-%F0%9D%99%BD%F0%9D%9A%98%F0%9D%9A%9F%F0%9D%9A%8E%F0%9D%9A%95-%F0%9F%8D%B0

# Book 2

➜ HIGHEST RANKS: #1 in FURRYGAY, #1 in IMPACTFUL, #1 in FURSONA

➜ This is the sequel to my first book, "Cake", which is finished and all ready for you to read! If you haven't done so already, please do, because you might not understand many of the things that happen in this novel, haha!

Charlie Cooperton and Skyler Clawfield, after four years of endless struggling, have graduated from the Cloverland Institute of Visual Arts with, literal, flying colors! So, the question remains: what now? Charlie and Sky have been thrown into adulthood without any warning, leaving them misguided when it comes to pursuing their careers, finding a place to live, and... their relationship. Charlie is forced to overcome the debt he has to his broken family, discovering secrets that were never meant to be uncovered, while Skyler bears the weight of finding his identity and how he wants to express himself.

Soon, they realize that they're on their own to fend the hardship coming their way, and that growing up is not just a turning point, but an ending one.


➜ This book is by Klondike (@klondikehazel)
This book includes homosexuality, romance, depression, sexual content, harsh language, trans representation, etc.
⚠️Mature

❝ Hey! Klondike here! I can't wait for you to read the sequel to my first and most iconic novel, "Cake"! This book is very different from the first in that it's much more sincere and realistic since our two main lovebirds are in a much more adult setting. But, that doesn't mean there's any less love and romance! Enjoy! ❞

&copy; All Rights Reserved

Wattpad Url: https://www.wattpad.com/story/257108086-%F0%9D%99%B2%F0%9D%99%B0%F0%9D%99%BA%F0%9D%99%B4-%F0%9D%99%B2%F0%9D%9A%91%F0%9D%9A%8A%F0%9D%9A%99%F0%9D%9A%9D%F0%9D%9A%8E%F0%9D%9A%9B-%F0%9D%9A%83%F0%9D%9A%A0%F0%9D%9A%98-%F0%9D%99%B0-%F0%9D%99%B5%F0%9D%9A%9E%F0%9D%9A%9B%F0%9D%9A%9B%F0%9D%9A%A2-%F0%9D%99%BB%F0%9D%99%B6%F0%9D%99%B1%F0%9D%9A%83-%F0%9D%99%BD%F0%9D%9A%98%F0%9D%9A%9F%F0%9D%9A%8E%F0%9D%9A%95-%F0%9F%8D%B0

---
## [ulm/portage](https://github.com/ulm/portage)@[28cd240fb2...](https://github.com/ulm/portage/commit/28cd240fb23d880b8641a058831c6762db71c3e2)
#### Tuesday 2023-04-18 15:22:46 by Sam James

emerge-webrsync: support PGP verification via gemato

Introduce PGP verification of the webrsync snapshot tarballs
using app-portage/gemato - which is already a dependency of Portage
for verifying normal rsync.

This is the same method Portage uses (see below).

Technical changes before we dive into the rationale:
- Use gemato for PGP verification just like Portage does for
  sync-type=webrsync, sync-type=rsync (although that uses a metamanifest),
  and sync-type=git (although that uses gemato for gpg-wrap, so works differently).

- Use gentoo-functions automagically if available for better output
  functions.

- Be more verbose about verification and various other operations,
  while also respecting --quiet if passed for misc. existing & new
  messages.

- Make --verbose a no-op. There weren't enough output messages
  to justify three states (--quiet, normal, --verbose).

- Bail out more aggressively in the event of errors or "warnings".

- Use modern terminology for repository, etc (avoid overloading the
  "portage" term.)

- Allow disabling PGP verification with --no-pgp-verify.

Technically, the fix is very straightforward, but getting to
the fix was the slightly painful bit. What I've concluded
happened is:
- Portage starts getting reworked to gain proper sync module support;

- Someone gets the idea of implementing emerge-webrsync fully in Python
  as a Portage sync module (which is a not-unreasonable idea);

  [This ultimately hasn't gone anywhere, and in fact, while working on this
  bug, I ended up finding a bunch of typos that meant you couldn't even test it.
  But it's a stub anyway.]

- The idea of deprecating emerge-webrsync is floated around. The idea
  being Portage should call it via its new sync module with sync-type=webrsync.

  This is presumably with the ultimate goal of it transparently one day
  using the aforementioned (yet-non-existent) Python implementation as its
  backend, and not the shell script.

  [To this day, Portage's webrsync implementation shells out to the emerge-webrsync
  shell script, but it has the abstraction to switch that out, in theory.]

- At the time, PGP verification in general of the Gentoo
  repository is an active topic, especially now we'd migrated to git which makes
  it way easier, unlike CVS.

- A bug is filed for PGP verification in emerge-webrsync.

  People decide it doesn't matter too much, because Portage is going to
  Real Soon Now (TM) have its own backend (replacing the shell script) and/or
  Portage's sync module support obsoletes emerge-webrsync entirely.

  The idea here, I think, being that nobody should call emerge-webrsync and
  everyone should just call emerge (or emaint) to sync as appropriate.

  [This isn't a terrible idea in a sense, but it needs a better basis:
  we should probably make emerge-webrsync a wrapper which creates a temporary
  repo config to forcefully webrsync a repository if the user asks us to. This
  is what people expect from emerge-webrsync with the default sync-type=rsync
  in repos.conf for ::gentoo.

  I actually started implementing this before I realised that emerge was
  shelling out to emerge-webrsync, so have postponed it.]

- Then nothing happens with the "replacement" ideas and the good
  ol' trusty emerge-webrsync ends up with the same problems sitting
  there because nobody saw the point in working on it if it was to
  be replaced soon. But that didn't happen.

The fix overall for this is pretty small, but the commit is larger
than I'd like because I had to rework a few things to sensibly allow
disabling PGP verification as well as follow the flow.

(I did start splitting up this commit but ultimately it needs -w
for best review even without the output tweaks in this commit and
deconstructing this for atomic commits would end up being more brittle
as I couldn't be as confident in the result.)

Bug: https://bugs.gentoo.org/597800
Signed-off-by: Sam James <sam@gentoo.org>

---
## [Solaris-Shade/Citadel-Station-13-RP](https://github.com/Solaris-Shade/Citadel-Station-13-RP)@[81c1229373...](https://github.com/Solaris-Shade/Citadel-Station-13-RP/commit/81c1229373208790c3375a138579aaf76a0006d0)
#### Tuesday 2023-04-18 15:50:16 by Captain277

Adds Just Like, a Ton of Clothes (#5048)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

1. **Adds a wide array of clothes, listed below.**

## Why It's Good For The Game

1. _My good friend Tech provided me with some sprite sheets when I was
working on Ashlanders, requesting a hobo coat. Going through the sheets
I found several different items I thought it would be fun to add to our
expanding list of customization and fashion options. The list is huge so
I'm just gonna itemize it here. As for attributions, as I understand it
most of this is from a D&D server, and some from a 40k server._
2. _Two of the outfits, the Belial and Lilin items, are sprites crafted
by our very own Doopy, as part of their Lindenoak line!_

## Outfits & Where to Get them

**Costume Vendor**
1. _Banana Costume_
3. _Hashashin Costume_
4. _Bard Hat_
5. _Aquiline Enforcer Uniform_
6. _Scavenging Sniper Set_
7. _Spiral Hero Outfit_
8. _Body Tape Wrapping_
9. _Redcoat Uniform_
10. _Despotic General Uniform_
11. _Post-Revolution American Uniform_
12. _Prussian Uniform_

**Suit Vendor**
1. _Ragged Coat_
2. _Spiral Hero Cloak_
3. _Nerdy Shirt_

**Jumpsuit Vendor**
1. _Toga_
2. _Countess Dress_
3. _Baroness Dress_
4. _Revealing Cocktail Dress_
5. _Belial Striped Shirt and Shorts_
6. _Lilin Sash Dress_

**Shoes Vendor**
1. _Utilitarian Shoes_

**Loadout**
1. _Ragged Coat_
7. _Spiral Hero Cloak_
8. _Nerdy Shirt_
9. _Bard Hat_
10. _Utilitarian Shoes_
11. _Toga_
13. _Countess Dress_
14. _Baroness Dress_
15. _Scavenging Sniper Set_
16. _Spiral Hero Outfit_
17. _Body Tape Wrapping_
18. _Revealing Cocktail Dress_
19. _Belial Striped Shirt and Shorts_
20. _Lilin Sash Dress_

**Medieval Armor Supply Crate**
1. _Crimson Knight Armor_
2. _Forest Knight Armor_
3. _Hauberk_
4. _Elite Paladin Armor, Helmet, and Boots_
5. _Alternate Knight Helmet_

**Cryosuit Supply Crates (Under Voidsuit Menu)**
1. _Cryosuit, Variants: Security, Engineering, Atmos, Mining_

**Crafting Menu**
1. _Duraskull Helmet_

**Ashlander Specific Crafting Menu**
1. _Ashen Vestment_
2. _Ashen Tabard_

**Ashlander Spawn**
1. _Priests now spawn with the Ashen Vestment._

**Admin Spawn**
1. _Actual armored versions of all new Knight sets._
5. _Utilitarian Military Helmet, Armor, and Boots._

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
add: Adds a wide array of new clothing items. Itemized in PR. #5408
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [shiranaiyo/agda-unimath](https://github.com/shiranaiyo/agda-unimath)@[9f3c75915c...](https://github.com/shiranaiyo/agda-unimath/commit/9f3c75915ceec77a374627d651c555f2cb9cd076)
#### Tuesday 2023-04-18 16:43:00 by Fredrik Bakke

New Agda syntax highlighting extension for VSCode (#562)

I've written an improved Agda syntax-highlighting extension for VSCode
called _agda-syntax_
([GitHub](https://github.com/fredrik-bakke/agda-syntax-vscode), [VSCode
Marketplace](https://marketplace.visualstudio.com/items?itemName=FredrikBakke.agda-syntax)).
Although it is still in preview, my opinion is that it is already a
significant improvement over the previously used extension. Therefore, I
propose that we migrate our development environment (for VSCode users)
to use this new extension.

### Some highlights of the extension
Compared to the previously used extension, this new extension
- injects into markdown syntax, so that the markdown code can be
highlighted as markdown code as well
- highlights all variable declarations (with some bugs still), module
names, wildcard symbols, all reserved keywords (and only recognizes
reserved keywords as reserved keywords)
- Recognizes the appropriate token-boundaries
- Highlights line comments properly

Please understand that the grammar framework that has to be used to
write the extension is highly limited, so not all highlighting
functionality can be implemented. For instance, the parsing must be done
in a single pass, and the functionality to match over multiple lines is
very limited. Hence, for example, matching the left-hand side of an
equals sign is very gnarly (although I have one idea left to try with
regard to this).

Still, I would greatly appreciate any feedback, either if it is a bug or
a feature request, which is another reason why I want to introduce it
into our defined development environment at this point.

If you want to try out the extension right now, follow the VSCode
Marketplace link:
https://marketplace.visualstudio.com/items?itemName=FredrikBakke.agda-syntax

---
## [MassMeta/tgstation](https://github.com/MassMeta/tgstation)@[54bf3808b8...](https://github.com/MassMeta/tgstation/commit/54bf3808b80ec8ef83bee4062d2361e9f38d8ae8)
#### Tuesday 2023-04-18 17:05:01 by SyncIt21

Stops station blueprints from expanding areas of non atmos adjacent turfs. (#74620)

## About The Pull Request
Fixes #74605

the problem starts with `detect_room()` proc. This proc returns turfs
even those with `atmos_adjacent_turfs` = null. This means it returns
turfs that has a wall, airlock, window etc i.e. whatever that stops air
from flowing through it. This coupled together with `create_area()`
causes some wierdness.

Let's take an example
![Screenshot
(154)](https://user-images.githubusercontent.com/110812394/230769831-e84819f2-31b2-4a67-a8bb-5e07e1c5a1cc.png)

Area A is well defined i.e. it has been created via the station
blueprints and is highlighted in green, Area B however is only
theoretical i.e. we haven't created it yet or we are about to create it.
Now you might be thinking Area A is completely walled & sealed off, it
should be physically impossible to expand it unless we broke down one of
it's walls and so since we are standing in Area B it shoudn't even give
me the option to expand area A Right? right? r.i.g.h.t?
![Screenshot
(155)](https://user-images.githubusercontent.com/110812394/230770056-169cbab3-4516-4da7-ae2c-4f40b50be9ba.png)
Well PHFUUK. The area editor completely ignores the laws of physics and
allows me expand Area A anyway. This could cause some real power gaming
shit because if you create an area next to an area having an APC you
could use that area power without even making your own apc by simply
expanding that area(like using someone else's wifi from outside their
house without them even knowing)

#73850 accidently built on top of this as it relied on this to detect
duplicate APC's but the checks became way too strict as it would check
areas of surrounding walls for apc's and throw the conflicting apc
error. You can now build room's next to each other even if they have
fuctioning apc's however you still can't build rooms in space on top of
shuttle walls because that's been the default behaviour for years and
hasn't been touched one bit.

## Changelog
:cl:
fix: station blueprints no longer expands & detects areas of non atmos
adjacent turfs.
/:cl:

---
## [daniel-goldstein/hail](https://github.com/daniel-goldstein/hail)@[da1115a387...](https://github.com/daniel-goldstein/hail/commit/da1115a387bb799991d0ab1416790dacc0b44cbe)
#### Tuesday 2023-04-18 17:34:41 by Daniel Goldstein

[ci] Mirror third-party images and hailgenetics images on deploy (#12818)

- On *deploys*, makes sure that whatever is in our third-party images is
in our private registry before starting builds like hail-ubuntu that
might depend on those images. This means that we can update our ubuntu
base image without the australians needing to deploy any images by hand.
However, this does not run in PRs because I 1) didn't want to add that
kind of latency for PRs and 2) we don't do any kind of namespacing for
our images so if we did include this for a PR that ultimately wasn't
merged we would have to manually remove the image anyway so why not
manually add it if you're going to PR it… I think point 2 is a little
weak but I recall this being what we agreed on a couple months back when
we discussed this. I'm wondering if we should just eat the minute or so
latency at the beginning of PRs to be safe but it also feels like a
shame for something that changes so infrequently.

- Again on deploys, upload the hailgenetics/* images to the private
registry if they don't already exist there. This way any deployments
that aren't hail team's GCP deployment can get these images
automatically when they deploy a new SHA instead of uploading them
manually. It won't backfill skipped versions, but we decided that was
ok. This seems less relevant for testing on PRs as it will get triggered
on releases and we can easily dev deploy to rectify the image if this
breaks.

---
## [AnywayFarus/Skyrat-tg](https://github.com/AnywayFarus/Skyrat-tg)@[f4aee43e79...](https://github.com/AnywayFarus/Skyrat-tg/commit/f4aee43e793237e0dd93c42761043ce824e84237)
#### Tuesday 2023-04-18 17:39:36 by SkyratBot

[MIRROR] Tones down the power of nitrous oxide, the reagent. Makes heparin a bit harder to fix to compensate [MDB IGNORE] (#20610)

* Tones down the power of nitrous oxide, the reagent. Makes heparin a bit harder to fix to compensate (#74703)

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

Co-authored-by: san7890 <the@ san7890.com>

* Tones down the power of nitrous oxide, the reagent. Makes heparin a bit harder to fix to compensate

---------

Co-authored-by: necromanceranne <40847847+necromanceranne@users.noreply.github.com>
Co-authored-by: san7890 <the@ san7890.com>

---
## [Firestorm01X2/Cataclysm-BN](https://github.com/Firestorm01X2/Cataclysm-BN)@[08d54d0287...](https://github.com/Firestorm01X2/Cataclysm-BN/commit/08d54d0287a1313cb810a1d3d74ca0e531189ae1)
#### Tuesday 2023-04-18 17:41:31 by KheirFerrum

Fix MGOAL_FIND_ITEM_GROUP, fix up some code (#2546)

* Reorganize

Code still sucks. In particular recruit_class doesn't compare properly with npc->my_class so MGOAL_RECRUIT_NPC_CLASS fails horribly even if you fix up that area of code to it actually points to type->recruit_class instead of recruit_class

For that matter mission has a select copy of several mission type defs and I can only assume this is due to legacy fuckery.

* Fix mission.cpp

Now will only allow you to select items if you have enough of them, and will only consume the necessary amount.

Added documentation for MGOAL_FIND_ITEM_GROUP

Thank god this wasn't too much work.

---
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[035ed80d2a...](https://github.com/cmss13-devs/cmss13/commit/035ed80d2adf782ca1998a6d58986e23dc71b51c)
#### Tuesday 2023-04-18 17:54:10 by NewyearnewmeUwu

No more proximity sensor spam. (#3076)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request
You can now slash proximity sensors to shut them up as xeno, and death
shuts off any proximity sensors in your belongings.
<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game
This is literally just the engi bellpack again. It's being used to OOCly
annoy people and needs a way to circumvent it.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->


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

:cl:
fix: Proximity sensors can now be slashed by xenos to deactivate them,
and they turn off after you die if you have an active one on you.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---------

Co-authored-by: harryob <me@harryob.live>

---
## [Rohail33/Realking_kernel_sm8250](https://github.com/Rohail33/Realking_kernel_sm8250)@[7c5c5eb97b...](https://github.com/Rohail33/Realking_kernel_sm8250/commit/7c5c5eb97bde4b6e64a37f6a18de349505077498)
#### Tuesday 2023-04-18 17:56:00 by George Spelvin

lib/list_sort: optimize number of calls to comparison function

CONFIG_RETPOLINE has severely degraded indirect function call
performance, so it's worth putting some effort into reducing the number
of times cmp() is called.

This patch avoids badly unbalanced merges on unlucky input sizes.  It
slightly increases the code size, but saves an average of 0.2*n calls to
cmp().

x86-64 code size 739 -> 803 bytes (+64)

Unfortunately, there's not a lot of low-hanging fruit in a merge sort;
it already performs only n*log2(n) - K*n + O(1) compares.  The leading
coefficient is already at the theoretical limit (log2(n!) corresponds to
K=1.4427), so we're fighting over the linear term, and the best
mergesort can do is K=1.2645, achieved when n is a power of 2.

The differences between mergesort variants appear when n is *not* a
power of 2; K is a function of the fractional part of log2(n).  Top-down
mergesort does best of all, achieving a minimum K=1.2408, and an average
(over all sizes) K=1.248.  However, that requires knowing the number of
entries to be sorted ahead of time, and making a full pass over the
input to count it conflicts with a second performance goal, which is
cache blocking.

Obviously, we have to read the entire list into L1 cache at some point,
and performance is best if it fits.  But if it doesn't fit, each full
pass over the input causes a cache miss per element, which is
undesirable.

While textbooks explain bottom-up mergesort as a succession of merging
passes, practical implementations do merging in depth-first order: as
soon as two lists of the same size are available, they are merged.  This
allows as many merge passes as possible to fit into L1; only the final
few merges force cache misses.

This cache-friendly depth-first merge order depends on us merging the
beginning of the input as much as possible before we've even seen the
end of the input (and thus know its size).

The simple eager merge pattern causes bad performance when n is just
over a power of 2.  If n=1028, the final merge is between 1024- and
4-element lists, which is wasteful of comparisons.  (This is actually
worse on average than n=1025, because a 1204:1 merge will, on average,
end after 512 compares, while 1024:4 will walk 4/5 of the list.)

Because of this, bottom-up mergesort achieves K < 0.5 for such sizes,
and has an average (over all sizes) K of around 1.  (My experiments show
K=1.01, while theory predicts K=0.965.)

There are "worst-case optimal" variants of bottom-up mergesort which
avoid this bad performance, but the algorithms given in the literature,
such as queue-mergesort and boustrodephonic mergesort, depend on the
breadth-first multi-pass structure that we are trying to avoid.

This implementation is as eager as possible while ensuring that all
merge passes are at worst 1:2 unbalanced.  This achieves the same
average K=1.207 as queue-mergesort, which is 0.2*n better then
bottom-up, and only 0.04*n behind top-down mergesort.

Specifically, defers merging two lists of size 2^k until it is known
that there are 2^k additional inputs following.  This ensures that the
final uneven merges triggered by reaching the end of the input will be
at worst 2:1.  This will avoid cache misses as long as 3*2^k elements
fit into the cache.

(I confess to being more than a little bit proud of how clean this code
turned out.  It took a lot of thinking, but the resultant inner loop is
very simple and efficient.)

Refs:
  Bottom-up Mergesort: A Detailed Analysis
  Wolfgang Panny, Helmut Prodinger
  Algorithmica 14(4):340--354, October 1995
  https://doi.org/10.1007/BF01294131
  https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.6.5260

  The cost distribution of queue-mergesort, optimal mergesorts, and
  power-of-two rules
  Wei-Mei Chen, Hsien-Kuei Hwang, Gen-Huey Chen
  Journal of Algorithms 30(2); Pages 423--448, February 1999
  https://doi.org/10.1006/jagm.1998.0986
  https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.4.5380

  Queue-Mergesort
  Mordecai J. Golin, Robert Sedgewick
  Information Processing Letters, 48(5):253--259, 10 December 1993
  https://doi.org/10.1016/0020-0190(93)90088-q
  https://sci-hub.tw/10.1016/0020-0190(93)90088-Q

Feedback from Rasmus Villemoes <linux@rasmusvillemoes.dk>.

Link: http://lkml.kernel.org/r/fd560853cc4dca0d0f02184ffa888b4c1be89abc.1552704200.git.lkml@sdf.org
Signed-off-by: George Spelvin <lkml@sdf.org>
Acked-by: Andrey Abramov <st5pub@yandex.ru>
Acked-by: Rasmus Villemoes <linux@rasmusvillemoes.dk>
Reviewed-by: Andy Shevchenko <andriy.shevchenko@linux.intel.com>
Cc: Daniel Wagner <daniel.wagner@siemens.com>
Cc: Dave Chinner <dchinner@redhat.com>
Cc: Don Mullis <don.mullis@gmail.com>
Cc: Geert Uytterhoeven <geert@linux-m68k.org>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: Little-W <1405481963@qq.com>

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[8c80c834fb...](https://github.com/git-for-windows/git/commit/8c80c834fb4139f90a876d362a2e81ad6818c079)
#### Tuesday 2023-04-18 18:19:16 by Johannes Schindelin

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
## [i574n/The-Spiral-Language](https://github.com/i574n/The-Spiral-Language)@[57029dd18a...](https://github.com/i574n/The-Spiral-Language/commit/57029dd18ac482a78423054d52f7a57ba3d23883)
#### Tuesday 2023-04-18 18:50:43 by Marko Grdinić

"7:30am. I've been lounging in bed for quite a while, but to think it is this early. Right now I am just waiting for the bathroom to clear and then I will start. I'll begin by taking a look at the other Giraffe examples.

7:55am. Let me finish the chapter and then I'll start. I want to just take a look at the other examples and then I'll run the first one.

https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_foreach?view=powershell-7.3

```ps
PS E:\Webdev\Fable\Giraffe\samples> dotnet restore (ls -r **.fsproj)
MSBUILD : error MSB1008: Only one project can be specified.
```

It is a real pain in the ass to restore all these projects.

```ps
PS E:\Webdev\Fable\Giraffe\samples> foreach ($x in (ls -r **.fsproj))
>> {
>> Write-Host $x
>> }
```

Oh this actually does what I want. Ok.

```
foreach ($x in (ls -r **.fsproj))
{
  dotnet restore $x
}
```

Let me try this.

It worked!

8:10am. This is actually the first time I did PS scripting.

8:30am. https://news.ycombinator.com/item?id=35477695
Administrative Scripting with Julia

> Julia seems like a nice programming language. Is it still worth learning, though, since ChatGPT can write all software now?
> Agree. Me think me learn english, but me too think ChatGPT come, then why learn English? So me not learn now, only wait for ChatGPT.
> Bizarro hate Superman, but ChatGPT hate Superman better, that mean Bizarro love Superman!

Focus me, stop reading HN. Study the code.

8:50am. I can't take it anymore. Let me start making a video.

9:05am. Had to take a short break. Let me resume.

https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/foreach-object?view=powershell-7.3

```ps
Get-ItemProperty -Path HKCU:\Network\* |
  ForEach-Object {Set-ItemProperty -Path $_.PSPath -Name RemotePath -Value $_.RemotePath.ToUpper();}
```

You can even modify the registry like this.

```ps
PS E:\Webdev\Fable\Giraffe\samples> Get-ChildItem | foreach { if ($_.Length -gt 1kb) {$_} }

    Directory: E:\Webdev\Fable\Giraffe\samples

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a---            4/6/2023  5:30 PM           5646 .gitignore
-a---            4/6/2023  5:30 PM          11357 LICENSE
-a---            4/6/2023  5:30 PM           1855 README.md
```

Now I am playing with PS. I am surprised this works.

9:20am. Sigh, what am I doing? Let me do some Youtubing. Yeah, I can do the Helix Studio, but...

I just do not want to put in an effort like in the last 8 years where I get no feedback.

I worked, and worked, and worked, seeking my power, but I hadn't gotten even a step further to what I desired.

I could go private, but my will is at its end. The point of this is not to make Helix. I just want the world to support my efforts.

The way I live is just so lonely. Without power. Without anyone to assist me. There are only people head of me, and I cannot grasp anything that I desire with my programming ability.

I could do the Helix by my lonesome, but then what will happen is nobody will care.

And I do not have the power to take what I want by force. So it feels like I am just living waiting to die.

9:25am. So I might as well do this next part as a video.

I could make a game or a platform or whatever. I could put in 2 years into it. And it could make it big.

But I do not want that anymore. I'd rather get 100 views today than 10m dollars tomorrow.

For me, there is no point to programming other than this. It is just a performance art, similar to writing.

I just want to talk and be heard, even if it is at the bottom.

10:30am. https://youtu.be/xdH9zsW1CK0
Cookies - Web Development

When I have a goal like making a video, I am finding it a lot easier to stay motivated.

Yeah, this is fine. I honestly, do not mind this kind of life. Who cares about great goals. What really matters are the small goals that get me closer to something.

https://youtu.be/hsY8oshtMSc?list=PLAwxTw4SYaPlLXUhUNt1wINWrrH9axjcI
Authentication - Web Development

Let me watch this.

10:45am. Oh, I see that in future lectures it actually covers how cookies are hashed and verified.

I really do need more knowledge. I've jsut started a new project in both Rider and Camtasia, and I am already motivated.

This is the way things should be. For every little thing I cover, I'll make something in return. Step by step, like that I'll conquer web development.

https://youtu.be/jxOEKSu0vws?list=PLAwxTw4SYaPlLXUhUNt1wINWrrH9axjcI&t=137
> I am in a private browsing mode because I do not want to have any cookies and that's generally what these private browsing modes do.

https://youtu.be/xgW0XjOeusY?list=PLAwxTw4SYaPlLXUhUNt1wINWrrH9axjcI&t=147

Oh, they are domain restricted. But how do token work around that?

https://youtu.be/qMFRRoh6vV8?list=PLAwxTw4SYaPlLXUhUNt1wINWrrH9axjcI&t=52

I tried getting on Google using curl, and it wasn't setting any cookies. I am guessing this kind of predatory behavior was banned. This course is quite old by now.

https://theburningmonk.com/2023/04/being-independent-4-years-on/
> If you’re considering a career as an independent consultant, my advice would be to hold off for now and wait for the market to recover.

This guy had F# articles in the past, and I had to google how to encode some things.

Everyone is saying the same thing - the market sucks now.

https://youtu.be/sK3AgUvdCoY?list=PLAwxTw4SYaPlLXUhUNt1wINWrrH9axjcI

I admit, I wasn't aware that Expires is actually there so you can remain logged in for longer!

This is how little I know about web dev. I am an idiot trying to muscle into this business without knowing the bare basics.

https://youtu.be/E2mPjwweIJ0?list=PLAwxTw4SYaPlLXUhUNt1wINWrrH9axjcI&t=115
Putting It Together - Web Development

Maybe I should have started from this kind of series. I think that cookie that I thought was hashed was merely in base64.

https://youtu.be/iLqlJzqSmak?list=PLAwxTw4SYaPlLXUhUNt1wINWrrH9axjcI&t=198

This is making me wonder, just where is the secret key that the ASP..NET Core Identity is using. Same goes for auth. I know that one of the lectures used a secret key, but in the Giraffe examples it isn't there. How confuisng.

https://youtu.be/fG4wIOwbA90?list=PLAwxTw4SYaPlLXUhUNt1wINWrrH9axjcI&t=8
> Sad story time. In the early days of Reddit, I stored passwords in clear text.
> Because when I was writing Reddit, I didn't think anybody would actually use it, let alone a lot of people.

This guy created Reddit?

12:25pm. https://youtu.be/9EWcJh70Fj8?list=PLAwxTw4SYaPlLXUhUNt1wINWrrH9axjcI&t=1

I am getting ideas. Maybe the user is supposed to log into Azure AD, get a token, and then send it to the server? Is that how it works.

https://youtu.be/9EWcJh70Fj8?list=PLAwxTw4SYaPlLXUhUNt1wINWrrH9axjcI

This is a really good series. It is low level stuff on cookies and security which is just what I need.

https://youtu.be/h-MQy9A91AI?list=PLAwxTw4SYaPlLXUhUNt1wINWrrH9axjcI&t=13
> We are going to be doing user accounts.

https://youtu.be/h-MQy9A91AI?list=PLAwxTw4SYaPlLXUhUNt1wINWrrH9axjcI&t=87
> Implement a sign up page

Sigh, why couldn't I grasp something this simple?

https://youtu.be/oMC-GuaGgIU?list=PLAwxTw4SYaPlLXUhUNt1wINWrrH9axjcI&t=32

Not specific to this time point, let me just say this has been very useful for me. I wasn't really sure whether the data for verifying the hash was placed right next to it, or if there was something other to it. Now that I know this, I don't have to present my own conjectures regarding how cookies should work.

https://youtu.be/6oi3VImtNkY?list=PLAwxTw4SYaPlLXUhUNt1wINWrrH9axjcI&t=239

AHhhhhhhhhhhh...

Right, I am so foolish. I do not need to put the user data in the cookie. I can put a salt instead!

Damn, why didn't I think of that?

That I am having trouble thinking up simple things like this despite focusing on this for so long just shows how much I needed to watch a course like this.

Let me continue.

I can't skip this.

This is like basic literacy for a web dev.

https://youtu.be/6oi3VImtNkY?list=PLAwxTw4SYaPlLXUhUNt1wINWrrH9axjcI&t=426

This is a bit similar to how Giraffe does it.

2:10pm. Done with breakfast and chores.

Sigh...my mom is ill.

Her cough has been really bad for the past week or so, and now she is laid out on the couch. She has had cancer for quite a while now, and now finds it difficult to get up to keep the fire stoked.

I am not sure how long she has left to live. She might not be around next week, and she might survive and prevail for years.

It is not like am a doctor and my parents aren't telling me anything.

I wish I knew a better path.

I thought I had the responsibility to pursue the Singularity and I did so. Then I did art.

I think that had I taken the conventinal path...

That had I understood the importance of small wins, I would have very well had the money to cryofreeze her and preserve her until the Singularity.

Doing Spiral is going to cost me a lot. So will the 3d modeling foray. And so will writing Heaven's Key.

But my new path is about picking up the small wins where I can.

I thought I was faithful to technology, but maybe all along what I really liked were the small wins.

Maybe grand goals were something beyond the realm of man to begin with.

2:20pm. Let me resume instead of lingering on this. I want to try running some of the Giraffe examples.

```fs
let configureLogging (builder : ILoggingBuilder) =
    let filter (l : LogLevel) = false && l.Equals LogLevel.Error
    builder.AddFilter(filter).AddConsole().AddDebug() |> ignore
```

Agh, for fuck's sake. I do not know how to get the logging information, so I can't be sure what the IP for the server is.

```fs
let configureLogging (builder : ILoggingBuilder) =
    let filter (l : LogLevel) = true || l.Equals LogLevel.Error
    builder.AddFilter(filter).AddConsole().AddDebug() |> ignore
```

It turns out I was modifying the wrong project.

```fs
let t = "CfDJ8Onu-nldwMlLrJ_8s2SHVTTkq1HSdy_gPihCE11uUqj1teQYyo3H0l85YR0E0XTqWNnVfVwHB40pH_GTJ1yteujGYr1N4MfySvpuEueAZLo7YeFHNqm4zMTHjUT5KvIUW1PcZDQnVd2m1ISZ5NFsjtNbX1l8qn_l8ZxSEQxm_xP1oojPg_FInvTL8jcsJ7kNVk48QDWRHk2Hyp0k8UDmZEbO4Ude7uMOjIgI1epNkE1OIsCKWAoKmMQWDTiL20IN4bP0Kn7mSZcl__BX9JHeV3DT-jW45VoeIgvFFq6cTs8jn5k3bvoHE7uViM1QGJ096aAZQHe2o6vubancZSOOJ7WLj2PMPBFmfilN9U-gwYTtqV0T6LK8769DOS1X2cJ1oASaQLBCbMtpGWM_B5-sp-IJOWeRX66e57bW5aiy6UkLX04NPR1n9S2CZhVGcdyH4VGR5hlhI5EhlaVz5sbnHkaeAVneVRnzsH0vI5cfc21dXYxfzPU7GVQOQTwiv5fGMtt2H1DU0fzsC4vJugMootrnfbLBkaywIMW7xzkN9c5CW16K2dmsTpPw8fznerIYrs3H7caoh2TOPHniR6s3b-U"

Convert.FromBase64String(t)
```

No, I have no idea how this string is encoded. Maybe it is not base64?

```fs
Encoding.ASCII.GetBytes("Hello")
|> Convert.ToBase64String
|> Convert.FromBase64String
|> Encoding.ASCII.GetString
```

This kind of round tripping works. Nevermind.

```fs
let requiresAuthentication (authFailedHandler : HttpHandler) : HttpHandler =
    authorizeUser
        (fun user -> isNotNull user && user.Identity.IsAuthenticated)
        authFailedHandler
```

Giraffe auth has this.

2:40pm. Let me start from scratch. I'll try making the video again.

3pm.

///

For now, let us start by explaining the authentication and the authorization workflow.
When an user is greeted by a page that requires login for the first time, assuming he wants to register, he will send the necessary data to the server. That can be his username, his email, and his password, as well as any other data that is required.
The server might store that data in a database somewhere, and check that there aren't any duplicate emails in it already.
Then what the user would do is return a cookie to the user. It could also be a token, but either way it returns some encripted piece of information stored in the header.
Then the user tries accessing the page with another request, this time with the cookie attached.
This cookie is in fact what is used for authentication. It persists in the browser memory, so the user doesn't have to keep resending his data on every request manually.
Compared to needing to verify with the database on every request, cookies are also great for performance as the only thing that is needed to verify the authenticity of the cookie is the information stored in the cookie itself.
To explain how that is done, we need to highlight that the cookie is not made of 100% encrypted data.
A random string, called the salt, is appended to the cookie in an unencrypted state. The salt is also a part of the encrypted data. When the server decripts the cookie, it can then compare the salt that was provided in an unecrypted state with the decripted one, and if the two match that confirms that the cookie is legitimate.
See the provided link in the card for more in depth information on the subject.

///

Let me save this here.

My god, auth is going to torture me for quite a while isn't it?

4:15pm. What is an authentication challenge?

https://youtu.be/RH0ZslQABVI
Challenge Response Authentication Method (and its problem)

Let me study up on that.

How is that different from being redirected to login?

4:25pm. Ugh, I have no idea how that is different from the regular thing. What is that challenge thing for?

https://stackoverflow.com/questions/60510015/what-exactly-does-challenge-mean-in-asp-net-core-3

> But I saw that there is a concept called Challenge in asp .net core. I don't know where it fits in all of this. From what I understood, if the user is not logged in it can redirect him to a page where he can log in.

https://learn.microsoft.com/en-us/aspnet/core/security/authentication/?view=aspnetcore-7.0#challenge

I guess it just redirects the user. I am guessing it sets the status code to 401.

This is simple enough, but I don't think the Giraffe examples use this which threw me off.

4:45pm. I am so incompetent today. I am actually having trouble figuring out how to add the auth middleware.

I really am finding this diffucult. It is not a matter of raw skill to be a webdev.

It is right now that I am going to get used to the domain. Just where is `AddAuthentication`?

///

WIth the basics out of the way, let us finally do some programming, and hopefully the material that we've talked about will sink in.
Here we have opened an empty F# Web Application project.
We'll import the libraries that we need as we go along.
We already have the ASP.NET imported by selecting that particular project type, so what we need to do next is import Giraffe.
Giraffe is a functional web handler combinator library similar to Suave. It has a view engine that we'll use to build a mostly static web application.
It won't be as fancy as an Elmish React application since it doesn't have the model view update loop, but in this video we are just concerned with authorizing the user, so that doesn't matter.

///

I am going to pause the video here until I understand enough to build out the initial page by myself.

https://youtu.be/SuJyQr_JADE
【東方 Power Metal/Fusion Jazz】 Best of Unlucky Morpheus Instrumentals

Never heard Unlucky Morpheus before.

```fs
open Microsoft.Extensions.DependencyInjection
```

I thought I might need `DependencyInjection`, but I wasn't sure where to find it.

5pm. Ok, let me make the next part of the video. I know enough.

6:25pm. I've made 8:15m of video today. Let me stop here so I can have lunch.

I am not sure I feel like doing more for the day.

As depressing as my circumstrances are, I am making progress on this project and it is lifting my spirit.

Maybe I'll stop for the day here.

7:05pm. Done with lunch. Let me stop. It is time to fight some abnos in Limbus.

I am going to get the video done tomorrow. I'll be making progress from here on out."

---
## [i574n/The-Spiral-Language](https://github.com/i574n/The-Spiral-Language)@[3b821c387a...](https://github.com/i574n/The-Spiral-Language/commit/3b821c387ae4bfa7ad18d9615e620108a2cb4fe3)
#### Tuesday 2023-04-18 18:50:43 by Marko Grdinić

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
## [i574n/The-Spiral-Language](https://github.com/i574n/The-Spiral-Language)@[bef1a49672...](https://github.com/i574n/The-Spiral-Language/commit/bef1a49672efe6a2d044ae4bb274f813bd78eaec)
#### Tuesday 2023-04-18 18:50:43 by Marko Grdinić

"9:50am. I went up staying too late browsing 4chan. Sigh, I just didn't feel like going to bed. Even playing games would have been too much of a chore.

I think I am addicted to the unpredictability of message boards. I even started participating in the recent /g/ AI discussions myself.

10:20am. Let me start. I've been slacking too much.

10:35am.

///

Welcome to Ghostlike's channel. I am your AI assistant for the day, Vilo. In the previous video we created a basic login page and thoroughly covered the path leading up to it.
Now it's time for part two.
We had time to think what we want to do in this video, and our main goal should not be to move to ASP.NET Core Identity or to bring in the fancier databases than the in memory one that we are using, but instead to set up third party authentication using the Microsoft Identity Platform.
So that will be the main goal of this video. We'll clean up after that.
Let us get started.

///

This should serve as an ice breaker.

10:40am.

```fs
            do! ctx.ChallengeAsync()
            return! redirectTo false "/login" next ctx
```

First of all, I want to investigate this challenge async. Should I be using this here or is it overwritten by redirectTo.

```cs
    /// <summary>
    /// Returns a temporary redirect response (HTTP 302) to the client.
    /// </summary>
    /// <param name="location">The URL to redirect the client to. This must be properly encoded for use in http headers
    /// where only ASCII characters are allowed.</param>
    public virtual void Redirect(string location) => Redirect(location, permanent: false);
```

It sets a status code.

10:45am. Oh, I got the slack invite. Right now I am checking mail.

///

I've been doing F# webdev tutorials on Youtube, so I just wanted to plug them here in case anybody is interested. Here is the latest one from the webdev playlist. Hope somebody finds it useful.

https://youtu.be/wQEIEDbABFU
Authentication & Authorization With ASP.NET Core And Giraffe. How To Build A Login Page. (Pt. 1)

///

10:55am. Posted this in the F# Slack.

https://stackoverflow.com/questions/42883946/forbidasync-vs-challengeasync-why-and-when-to-use-them

```fs
    /// <summary>
    /// Challenges a client to authenticate via a specific authScheme.
    /// </summary>
    /// <param name="authScheme">The name of an authentication scheme from your application.</param>
    /// <param name="next"></param>
    /// <param name="ctx"></param>
    /// <returns>A Giraffe <see cref="HttpHandler"/> function which can be composed into a bigger web application.</returns>
    let challenge (authScheme : string) : HttpHandler =
        fun (next : HttpFunc) (ctx : HttpContext) ->
            task {
                do! ctx.ChallengeAsync authScheme
                return! next ctx
            }
```

Hmmm...

Let me try using this.

11:40am. Had to take a break, let me resume.

12:10pm. https://pixabay.com/music/corporate-ambient-piano-loop-144861/

12:25pm. > We'll start work on setting up passwordless logins using the Microsoft Identity Platform.

Let me stop here for breakfast.

Currently I am 2:35m in.

I need to do some research on how to setup Azure AD. I have no idea how to proceed from here.

1pm. https://youtu.be/TAJZs1pwCOE
Secure .NET Web Apps using the Microsoft Identity Platform

1:30pm. Done with breakfast and chores. Let me resume. I watched the thing above, and they implemented logins for the default Blazor project using Azure AD.

I need to immitate the guy and get it working once myself. Let me create a fresh project and I will play with it for a bit.

1:35pm. Sigh, the video is completely different than the default templates. Let me follow it exactly.

https://youtu.be/TAJZs1pwCOE?t=38

Oh, the single org is what I need.

1:55pm. Focus me, get this done.

...Oh wait, I just see Rider is offering me to register automatically.

2pm. Ah, let me take another break here. I need it.

2:20pm. Let me resume.

But I am wondering, if this is the way to do it, what is the point of MSAL?

2:35pm. I got it to work on the template.

https://youtu.be/RQ9DKBViWEg
A new tool to help you configure Azure AD for your apps

Let me watch this.

> Code first app registration.

2:50pm.

> https://login.microsoftonline.com/ec88369d-6c2f-4f15-b0c7-adbe35caec77/oauth2/v2.0/authorize?client_id=7679d9a0-4b8b-4d19-a519-1b3b0e5ba644&redirect_uri=https%3A%2F%2Flocalhost%3A44384%2Fsignin-oidc&response_type=id_token&scope=openid%20profile&response_mode=form_post&nonce=638167279337567115.MmI1OTQ3MjktNzRlYS00NGUxLWIzOWMtZTE5OGQ5M2RhMjFjNmZmNGZjODYtNTViMy00OTFjLTljMzYtMTQ2OGM2MmE2NTli&client_info=1&x-client-brkrver=IDWeb.1.16.0.0&state=CfDJ8Onu-nldwMlLrJ_8s2SHVTSS-81o8X0Yj6qJTW2gExn4ge0GsstPrp-JAbzei0F9iaiiQLp1r6_PbWLLeucjfxnWc64mO4IdFgtWiXoAvDY5R-zuzJIB5-PF5vMRins1KjIHfrsCte5C6tgy6nW1r7qthoNVNoiC4oE56RJ1D0-aikcT6hUbUqCS41-ohjHwMIoXk3CzWhi66re3gtO80_tMucNGLck1OIZXZnkQIb-p6evuXkc7bOFqcgwLsNPyxN-NKp06sA0J-vSNy6scrZKZp56kx4-spq5uFiCOV7Iv&x-client-SKU=ID_NETSTANDARD2_0&x-client-ver=6.15.1.0&sso_reload=true

What a long URL. But it does have a return URI. Ok, I see. The callback uri is appended to it.

3pm. What do I do next?

Just give it a try.

3:10pm. Let me give it a try. I'll see how far my approach gets me.

My courage will lead me to the truth in the end.

3:55pm. This is really a huge pain in the ass. I feel completely stuck.

Let me draw out a diagram first.

4:05pm. It is difficult. I understand cookies, but I don't think I understand token based authentication.

https://youtu.be/t18YB3xDfXI
An Illustrated Guide to OAuth and OpenID Connect

https://youtu.be/t18YB3xDfXI?t=122

This is kind of nice.

Right now I am confused as to how to do basic things like get the username and the email from the user. Just logging in is not enough.

Nevermind, fuck these crappy videos.

Let me close Camtasia and everything else. This is the kind of path that I need to travel on my own. Otherwise it will drain all my will to do it.

4:25pm. Let me open Camtasia again. I'll just screencast. I do not have the motivation to do it, unless I am making content.

But let me take a break.

4:55pm. Let me try it again. I've time to think about it.

6pm.

///

As far as we can tell, the domain doesn't have to be set, but the instance does.

We've tried setting it to
http://www.google.com
and it worked so we guess that any valid url can be put in here.

/signin-oidc will get appended to the return URI, so the callback path is important.

///

Let me back this up here.

6:30pm. Done with lunch. I had a lot of inspiration in the last hour.

I figure out how to do 3rd party authentication.

ChallengeAsync.

I was wondering how the hell I should send a request to the MS site, but most likely all I need to do is call challenge async.

Camtasia crashed.

And again.

I just want to get through this section and then I will close.

7:40pm. I am tired. Let me close here for the day. I am 9m in. But I am feeling a lot more confident about my prospects now.

I should be able to finish past 2 tomorrow. Given how it started, it is amazing that I managed 9m today.

I have a blank area that I'll need to get back to. and the sound goes up to 9:30m so I am not sure what the exact amount should be, but 9m seems decent as an estimate.

7:45pm. Sigh, I should realize that ChallengeAsync is the answer to redirecting to the MS page a lot sooner. If it turns out that it is not, I will be very perplexed."

---
## [i574n/The-Spiral-Language](https://github.com/i574n/The-Spiral-Language)@[c797cd8b9e...](https://github.com/i574n/The-Spiral-Language/commit/c797cd8b9ebacfaea60de1f4eb2aff8a7fdb6031)
#### Tuesday 2023-04-18 18:50:43 by Marko Grdinić

"10:25pm. https://old.reddit.com/r/ExperiencedDevs/comments/12f1hjg/should_i_let_my_company_use_my_project/

///

NO.
You go to a lawyer. You get a contract immediately where you're entirely in control. Even at that what I am saying is sketchy since I've been in meetings where the phrase "acquisition through employment" was used, after I had an issue with one of my projects. Don't even dare make a commit to that project right now while you're working until you see a lawyer and figure out what if they own that work because of a conflict.

I've walked this road. DO NOT DO IT. I'm telling you from real experience here. Just do not do it. It might be a trust me bro situation, but you have no idea how bad this can get.

That goes for the rest of you too. Do not make some cute project on the side that you plan to profit from while not reviewing your contract.

///

https://www.reddit.com/r/digitalnomad/?utm_source=reddit&utm_medium=usertext&utm_name=ExperiencedDevs&utm_content=t5_e0gez

Job sites. Forget those.

10:55am.

///

In the realm of code, where the algorithms play,
A language emerged, as the dawn of new day;
F sharp it was called, a language of grace,
With functional charm, it took its place.

Amidst the vast .NET framework's expanse,
F sharp's melody dared to enhance;
Its patterns matched, and types inferred,
A harmony of logic, elegantly conferred.

Oh, hark! The brevity of syntax divine,
In the lines of code, concision did shine;
Expressiveness ruled, as with quill on parchment,
The prose of programmers, now more enchanting.

The language's power, from functions arose,
Immutable truths, it did disclose;
Higher-order thoughts, composed and refined,
In the minds of developers, forever enshrined.

For in this land of bytes and bits,
The fusion of paradigms permits
A union of objects and functions, entwined,
In the elegant dance of F sharp's design.

Thus, let us raise our voices and declare,
The praise of F sharp, beyond compare;
For in this language, beauty and might,
A new era of code, ignites the night.

///

F# poem by ChatGPT in the style of Lord Byron. I found it on the F# slack.

4/11/2023

9:30am. Let me chill just a bit more and then I will start.

10:20am. Let me start. Where was I?

1pm. I did a fantastic job. Now I just need to explain that middle section and do the outro, and I'll be done with the video. Let me have breakfast here.

3pm. Wow, I sure wasted a lot of time doing chores. Let me resume.

3:35pm. Focus me, stop reading HN. Finish the video.

https://huggingface.co/spaces/stabilityai/stable-diffusion

This is a SD 2.1 space with Google TPUs. Since I want a thumbnail image, it is easier for me to use this than to mess with Paperspace.

It has native 768 images so I don't need to upscale. Not bad.

4:15pm. https://youtu.be/hlC6baPjFOs
Authentication & Authorization With ASP.NET Core And Giraffe. Azure AD. (Pt. 2)

Here is my latest masterpiece.

4:25pm. https://twitter.com/Ghostlike

Posted in my Twitter profile, but I'll only post my work in the F# slack occasionally.

I wonder if I should post it on LinkedIn?

Sigh, who is going to care about this social media.

4:35pm. If the viewers come let them come. If not, I'll move to contracting.

Now that I am finally done with that video, I do not feel like starting right away with the next. That is how it goes usually.

I am going to get the databases and MS Identity and Integration out of the way.

5:10pm. Let me start the next video.

5:30pm. Let me really start instead of surfing /g/.

I'll get into it once I do.

///

In this video we'll be covering the ASP.NET Core Identity library, which is distinct from the online service called the Microsoft Identity Platform.
We will also be bringing in fancier servers

///

I am not sure whether I want this in the current video. Let me cut it out.

5:55pm. I've started the video and did the intro. Let me set up the project.

5:55pm. Actually, let me just think a little of how I want to do things. I think I'll get rid of the usernames.

6:10pm. I had time to think about it, but I really do not feel like doing any more programming for the day.

6:15pm. Let me go get lunch.

Tomorrow I am going to take care of the integration. After that, I'll bring in those libs, and highlight the Giraffe examples.

After that I'll do what I want, which is work on node based UIs."

---
## [i574n/The-Spiral-Language](https://github.com/i574n/The-Spiral-Language)@[6e97d51bef...](https://github.com/i574n/The-Spiral-Language/commit/6e97d51bef161dcecdec4c73a358e92ccce8193e)
#### Tuesday 2023-04-18 18:50:43 by Marko Grdinić

"https://www.forbes.com/sites/karlfreund/2023/04/11/tenstorrent-could-reshape-the-ai-and-cpu-competitive-landscape/?sh=33c70c3a67da
> But the real culprit is NVIDIA; they are proving a lot harder to beat than many companies and their investors ever imagined.

In my view the AI chip companies are incompetent. Just why is it so hard for them to beat GPUs? At the very least, PIM processing should act as the initial advantage.

Things aren't happening the way I anticipated at all. I want to believe in Tenstorrent, but I really expected a bunch of startups to be capable of beating Nvidia in this timeline. There is no real point in believing in TT at this stage. Similarly to Graphcore, they had their Grayskulls out for a while, and where are the benchmarks? If they were better than GPUs, the company would be shouting about it from the rooftops. Even if they were using old process nodes, they could have just compared them to the older GPUs.

If all of those 100 startups are just going to go up in flame, what was the point of them? I'd be better off hoping Google, Amazon or MS come up with new hardware for their cloud services.

https://mathstodon.xyz/@tao/110172426733603359

I am really behind on ChatGPT. Maybe not for coding, but it is a great poet. I'll have to integrate it into my writing workflow at some point.

4/13/2023

8:50am. I've had trouble falling asleep, and then I woke up early and was lounging in bed, and yet it is this early. I am not that tired.

Let me chill a bit, read MagiTora, then I will take a bath. After that I will start screencasting.

10:15am. Done with the bath. I'll leave Kaijin Kaihatsu and that GB thread for later.

Focus me. Let me start a new video.

Also, you know what? I need some new covers, so let me start up PS while I am at it.

...Nice, I got a GPU right away.

> A bright sun shining over a tranquil lake. A flock of white birds are flying overhead. Best detail, highest quality, masterpiece, 8k.
> A white moon is reflected from tranquil lake. A haunted atmosphere. Best detail, highest quality, masterpiece, 8k.

Neg prompt:
> Dull, muted, ugly, blurry.

10:40am. First time I am using batch upscaling.

Oh, nice. I'll create a whole bunch them this way.

11:15am. Damn it, SD is distracting me. Let me start the screencast.

11:55am. Dealing with SD on paperspace is very distracting.

But on the plus side, these new covers are very beautiful. Especially the intro screens.

12pm. Let me focus on screening. Today had too many distractions for me.

12:40pm. Let me take off here for a bit, and then I will resume.

Rather than going straight forward I had to review the example a bit.

Hmmm, ok, I think I know how to approach this.

12:45pm. Breakfast. Breakfast time.

2:55pm. Let me resume.

Focus only on the screencast. The bath and SD broke my focus in the morning.

4:10pm. https://pixabay.com/music/beats-aesthetics-138637/

Let me get this one.

https://chat.openai.com/chat

Let me ask ChatGPT.

https://pixabay.com/music/solo-piano-this-is-my-fatherx27s-world-146078/

7:15pm. Done with lunch. I am going to stop here for the day.

https://stackoverflow.com/questions/60198623/how-to-use-both-azure-ad-authentication-and-identity-on-asp-net-core-3

I'll implement this tomorrow.

Today I am done.

It is a pity I couldn't finish it today. But this is the problem with high level libraries. They tend to be inflexible.

I guess this is just one of the pains of being a web dev. I'll get through it soon.

I'll finish this video tomorrow, then deal with SPAs. Then comes the fun stuff."

---
## [i574n/The-Spiral-Language](https://github.com/i574n/The-Spiral-Language)@[400212f6bd...](https://github.com/i574n/The-Spiral-Language/commit/400212f6bdc8f02a234247ee2fca7b05e0154b8e)
#### Tuesday 2023-04-18 18:50:43 by Marko Grdinić

"9:30pm. https://gogoanime.llc/rwby-volume-9-dub-episode-3

I am watching S9 of RWBY and these developments in the first two seasons are beyond retarded. What are the writers doing?

https://gogoanime.llc/category/i-was-stuck-on-the-same-day-for-one-hundred-thousand-years-3

Maybe I should really give some Chinese series a try.

8:40pm. I am looking up threads in the archive and apparently Ruby kills herself. Wtf?

I am laughing out loud here at how stupid it is. Let me watch the rest.

10pm. https://old.reddit.com/r/ExperiencedDevs/comments/12ei8mo/is_the_phrase_programming_language_doesnt_matter/

> What are your options for early exit? Can your language perform automatic loop unrolling? Are you running in a functional language where you need to be mindful of tail recursion? Does your language prefer list comprehensions or ranges or map and fold for iteration? Can you create side effects in a loop? Are you forced to create side effects in a loop due to the age of your language? Is a loop a statement or a meaningful expression? Does your language handle nested breaks cleanly? What about post condition checking (do...while)? What about optimizations around intentionally infinite loops? Can you interrupt a loop for asynchronous execution? Does your language have a good debugger for finding unexpectedly hot loops?

10:35pm. A lot of good comments in this thread. Small subs like this can have gems before they are overrun by the masses.

https://old.reddit.com/r/ExperiencedDevs/comments/12ei8mo/is_the_phrase_programming_language_doesnt_matter/jfen1cc/

///

Context is key.

When learning, which programming language you choose to start out with doesn't really matter. The key is to really learn programming, not to memorize how to do something in a particular language or ecosystem.

When solving a problem, programming language isn't as critical as most non-developers think, but it does matter.

* Choosing a language will put a cap on the performance available to you. If you choose C++, the max performance will be limited only by your skill and the speed of the hardware. If you choose Ruby, the max performance will be 1/20 or less of the C++ code. Other languages fall between those extremes.
* Choosing a language with dynamic types means you're missing out on some key software engineering tools that can help keep a code base clean over the long term, as well as helping people onboard to the project. I don't mind writing short scripts in strictly dynamic type languages, but refuse to work on extremely complex projects based on, e.g., PHP or Python.
* Choosing a language typically ties you to an ecosystem, or in some cases, one or more ecosystems. The tools available in one ecosystem (e.g., Node.js+TypeScript) might be so much more powerful for a particular task (e.g., CRUD) than those in another ecosystem (e.g., C++) that one ecosystem requires 1/50th or less the amount of code to accomplish the same tasks. I'm not even exaggerating.
* Some languages trade performance for developer productivity. In the last example, part of that 50x improvement when using TypeScript is simply that the same logic takes less code.
* Some language ecosystems are poorly designed to the point to recommend against using them. PHP falls under that category for me. The language was designed with even less skill than JavaScript, and the libraries practically beg you to create SQL injection flaws. You need to be an expert to work around all of those security holes...and yet most PHP developers are actually among the least skilled, leading to an ecosystem that pretty much dominates the security advisory lists.
* Some languages (e.g., C, though to a lesser degree, C++) require that you understand software at a lower level than languages that are GC based. There are decent, and probably even good, Java or JavaScript or Python developers who, when trying to make the jump to C or C++, simply fail. Yes, you can put together "Hello World" in C or C++ without much effort. But to really use either language requires a quantum shift in how you think about programming, and in my experience trying to teach other developers these concepts, some find they can't bridge the gap. C++ adds another layer of complexity on top of the lower-level understanding required by C, and there are people who are virulently against using C++ for ... reasons ... even though C++ is strictly better than C for some domains (e.g., embedded).

So yes, there are differences. And I refuse to work on some languages even though I know them well enough that I could use them (e.g., PHP).

///

https://old.reddit.com/r/ExperiencedDevs/comments/12c4mxs/junior_dev_using_chatgpt_for_code_reviews/

///

I'd also be pissed because ChatGPT is flat out wrong all the time. I use it daily and it's hardly some magic bullet. A junior may not get that.

ChatGPT pisses me off because everyone trusts it. It's very very good at looking correct. It is often wrong.

///

11:50am. > When someone tells us in an interview they’re excited about working here because they like functional programming (say), we count that as an indication they might not be a good fit.

4/9/2023

8:25am. I am up early, but regardless, I still have been lounging in bed for a while. This is despite me going to bed past 11pm yesterday.

9:50am. Done with the bath. What follows next is screencasting. Let me get on with it.

https://pixabay.com/music/modern-classical-relaxing-145038/
https://pixabay.com/users/music_for_videos-26992513/

This guy is good.

https://pixabay.com/music/modern-classical-slow-piano-145044/

Let me get this one as well.

11:55am. > In the current version of ASP.NET, it seems you need to specify the authorization schema in the claims identity directly. Before that we had to add the relevant authentication services to the dictionary the framework is using under the hood.

Let me cut this out. I do not have anywhere to put this.

12:25pm. Had to take a break so I might as well segue it into breakfast. Currently I am 25m into it.

2pm. Done with breakfast, Birdie Wing and chores.

Let me resume. I need to do more screencasting. Time to bring in the database.

3:25pm. https://pixabay.com/music/modern-classical-slow-piano-2-145042/

Let me add this to the video as well.

https://learn.microsoft.com/en-us/aspnet/core/data/ef-rp/crud?view=aspnetcore-7.0&viewFallbackFrom=aspnetcore-2.2#singleordefaultasync-vs-firstordefaultasync

4:05pm. https://stackoverflow.com/questions/56257157/how-to-check-for-null-from-newtonsoft-when-the-compiler-insists-that-it-isnt

This is so annoying.

https://stackoverflow.com/questions/43328417/translate-entity-framework-core-example-to-f

4:40pm. https://pixabay.com/music/modern-classical-coronavirus-145019/

Let me also get this one.

5:25pm. Did the thumbnail.

...Now it is rendering in the background.

5:50pm. https://youtu.be/wQEIEDbABFU
Authentication & Authorization With ASP.NET Core And Giraffe. How To Build A Login Page. (Pt. 1)

Here it is. Let me post it on the F# sub. Maybe my Twitter. Also I should find a way to get into the F# slack even if it means registering via a different address.

6:10pm. https://twitter.com/foonpm/status/1488760256624828419
> Sometimes I wish F# devs actually existed. As I'd build an entire team!

Check this tweet out. Well, that was a year ago, who knows if he is still interested.

> CEO @ Marvin - Hiring (Craftsman, DDD/CQRS/ES, TDD, Clean Code, Functional programming) - Full Remote - Worldwide

I saw a post from over a year ago that you are hiring F# devs, so I thought I'd ask whether that is still the case. You can see some of my most recent work on the F# subreddit. I've been getting into webdev lately, and and my particular specialty is creating programming languages and ML libraries.

Spiral is my best work: https://github.com/mrakgr/The-Spiral-Language

I have about 7 years of experience, most of it in F#.

6:40pm. I wasted my time trying to send a message, but I can't even DM him.

https://www.remote.io/

I'll keep this site in mind, why did I waste my time trying to contact this guy?

Forget this. Let me play Limbus for a bit.

Then I'll watch anime. It is really great that Birdie Wing got S2. G Witch is out. I'll also give ep 1 of Destroyes a try as well.

Time for some fun. Tomorrow I'll continue building the login page and screencasting as I go along. I've managed to hit my stride and am doing good work."

---
## [i574n/The-Spiral-Language](https://github.com/i574n/The-Spiral-Language)@[35db285a9f...](https://github.com/i574n/The-Spiral-Language/commit/35db285a9ff0fc81c69766426b4c2a68fe07b56c)
#### Tuesday 2023-04-18 18:50:43 by Marko Grdinić

"8:55am. Let me chill for a bit and then I will start.

9:25am. Let me start. Where was I? I am going to finish part 4 today.

Camtasia is so poorly optimized. It takes forever to load. It might be worth considering Active Presenter again. I wrote it off back then, but my workflow is far different now.

9:35am. Let me start from the SO post.

///

are aiming for 100% clearance in the game we are playing here.
ChatGPT turned out to be worse than useless. Had its answer been not wholy made up, it would have been great, but as it is, I don't think we'll be using it as a source of advice again.

///

Let me cut this out.

10:10am. https://pixabay.com/music/solo-guitar-illusion-feel-ambient-guitar-146100/

10:30am.

Nope, it doesn't seem we can put anything into the middleware here. In the worst case, we'll just bring back auth_all, but is there a way to have the auth middleware do that work for use instead?

```fs
    let login : HttpHandler = fun next ctx -> task {
        let! _ = ctx.AuthenticateAsync("AzureOIDC")
```

Let me add this line to see if it does something.

11:30am. https://chsakell.com/2019/07/28/asp-net-core-identity-series-external-provider-authentication-registration-strategy/#:~:text=The%20steps%20to%20enable%20authentication,external%20provider%20in%20Startup%2FConfigureServices

Goddamit, I am so bogged down with this shit.

11:40am. https://stackoverflow.com/questions/48836688/what-exactly-is-useauthentication-for

```cs
var defaultAuthenticate = await Schemes.GetDefaultAuthenticateSchemeAsync();
if (defaultAuthenticate != null)
{
    var result = await context.AuthenticateAsync(defaultAuthenticate.Name);
    if (result?.Principal != null)
    {
        context.User = result.Principal;
    }
}
```

Why does it just try to authenticate the default? Shouldn't it try all of them?

The decompiler is useless.

12:25pm. > In ASP.NET Core 7, how do I get a list of all the authentication schema names that have been added?

This is such pain in the ass, and I am starting to hate ASP.NET Core all over again.

It wasted a shitload of my time for nothing.

Let me ask ChatGPT how to do it as I have no other option.

> My ASP.NET Core 7 web application has multiple authentication schemas. How can I set it up so it tries authenticating using all of them?

Let me try the first question, first.

> Is it possible to set up the ASP.NET 7 web app so it tries out all of the authetication schemas at the start?

```cs
using Microsoft.AspNetCore.Authentication;

public class Startup
{
    public void ConfigureServices(IServiceCollection services)
    {
        services.AddAuthentication(options =>
        {
            options.DefaultScheme = CookieAuthenticationDefaults.AuthenticationScheme;
            options.DefaultChallengeScheme = "YourOtherScheme";
        })
        .AddCookie()
        .AddJwtBearer()
        .AddOpenIdConnect("YourOtherScheme", options =>
        {
            // Configuration for the other scheme
        });

        // Other service configurations
    }

    // Other methods
}
```

ChatGPT is making making me think about some of the things that I might've overlooked.

```cs
    builder.Services.AddAuthentication(fun opt ->
        opt.DefaultScheme <- Cookie.Onsite
        opt.DefaultChallengeScheme <- "AzureOID"
        )
```

Would this enable the UseAuthentication to work?

12:35pm. ChatGPT is wrong again, it seems. It isn't authing AzureOID. I also tried Cookie.Azure and am getting nothing.

12:45pm. Let me take a break here.

It seems there are days just like these.

I think I have an understanding how to deal with this next part.

3pm. Done with chores and breakfast. Let me reusme.

```fs
    app.Use(Func<HttpContext,RequestDelegate,Threading.Tasks.Task>(fun ctx next -> task {
        match ctx.Request.Cookies.TryGetValue("auth") with
        | true, v ->
            let prot = idp.CreateProtector("auth-cookie")
            let v = prot.Unprotect(v)
            match v.Split ':' with
            | [|"usr"; v|] -> v
            | _ -> "invalid user"
        | _ -> "not logged in"
        next()
        })) |> ignore
```

I keep trying to figure out how to do my own middleware in F#. I finally found this in the journal.

https://cloudandmobiledev.wordpress.com/2018/09/14/how-to-add-middleware-to-asp-net-core-2-1-with-f/

Here is also an way.

But I'll just plug it into the Giraffe pipeline at the start.

4:40pm.

///

In the last video, we gave the advice that you should just forget onsite and use 3rd party, and in this video you can see why.
ASP.NET Core Identity would be perfectly fine on its own, but it turns into a mess when you try to combine different authentication schemes.
Maybe it keeps salaried webdevs busy, but as far as we can see, there are only disadvantages to having multiple ways of authenticating an user. You are just doing extra work for no discernible benefit.
We ran into a lot of extra work
We are done with part 4, but it cannot be said that the onsite login is complete. The biggest problem is that it is missing the email verification part. If you tried using this as it, a malicious user could use it to create accounts for emails he doesn't own.

///

No, let me back this up. I am not done yet. I am going to do email logins.

5:35pm. I showed how to do an email login.

5:45pm. https://youtu.be/1Ifvyud7I70
Authentication & Authorization With ASP.NET Core And Giraffe. ASP.NET Core Identity. (Pt. 4)

Here it is.

5:55pm. Posted on Twitter as well.

6pm. Damn, dealing with this was super hard.

I am drained mentally. No way can I do anything more for the day.

I'll leave SPAs for tomorrow.

Let me close here."

---
## [i574n/The-Spiral-Language](https://github.com/i574n/The-Spiral-Language)@[1bd7e51b7d...](https://github.com/i574n/The-Spiral-Language/commit/1bd7e51b7d9526957f96e0774647d4dd7ed6563e)
#### Tuesday 2023-04-18 18:50:43 by Marko Grdinić

"8:50am. https://www.reuters.com/investigates/special-report/us-china-tech-cables/
https://robotic.substack.com/p/behind-the-curtain-ai

Let me read these two and then I will start. I got up a bit ago and just chilling.

9:30am. Let me start. Where was I?

https://pixabay.com/music/solo-guitar-ambient-classical-guitar-144998/
https://pixabay.com/music/ambient-epic-relaxing-flute-music-144009/
https://pixabay.com/music/beats-after-party-144155/

11:20am.

```fs
let! model       = ctx.BindFormAsync<RegisterModel>()
```

Actually, I hand't realized this just extracted the body. Now that I am at this point I finally realize something extremely basic and obvious, which is that the handler is not binding to the form specifically.

12:50pm.

///

We are making good progress. We now know how to send post requests from the client and deserialize them into .NET objects that we can use on the server side. We even return an user page after a successful login.
But returning an user page only works because we are returning the HTML view from the register handler directly which already has the user data.
We aren't redirecting the user to a different page that is on the site.
In order to be able to implement that, we need to be able to extract the user data from somewhere.
As HTTP requests are stateless, we can only get that data from the request itself.
When a user makes a request, he should also be sending his user credentials inside the cookie.
Those credentials are the very ones we are creating during the registration here.
What we have to do is just set the cookie in the response header that we send back to the client, and he will be sending them to the server on every request thereafter.
At least, until he closes the browser and the cookie is wiped.

///

I have about 14m of screencasting done, and the above is another minute that I'll have to do. What I will do next is try setting the cookie manually just to demonstrate what is going on in the browser. Then I'll bring in the Auth middleware.

12:55pm. I am losing steam, and am just in a daze. Instead of ruminating, let me have breakfast here. I've earned.

Before the day is done, I'll definitely demo how the logins are done.

After I demo the auth middleware, I'll bring in the database starting with in memory one and moving to SQLite.

2:20pm. Done with breakfast and chores. Let me resume. Let me do some more screencasting for the day.

This sense of tension is just as gripping when I was programming in the past. I already feel tired.

https://pixabay.com/music/modern-classical-the-first-star-calm-relaxing-piano-solo-music-141920/

///

In its current state the login page doesn't have much to do. In a real scenario, assuming the user doesn't have a cookie and submits the form information, we'd match it against the one in the database and give the user a cookie if the username and password match.

///

Let me do the caption annotations here. Camtasia is so shitty when the file gets bigger.

5:05pm. Had to take a break.

Let me resume. Where was I?

5:35pm. I am really tired right now. I think I'll stop the screencast here for the day.

I am 20:35m in.

Right now I am feeling blocked on where to put the password. The Giraffe example is not telling me.

Let me do just a bit more.

5:40pm. Ok, 20:43.

I need to do some research on why these claims exist. I sort of assumed that Claims are arbitrary, but that can't be it.

https://www.youtube.com/results?search_query=claim+based+authentication

These is stuff by Frank Liu here.

5:45pm. Oh, Frank Liu has the first two hours of his course on Youtube.

https://youtu.be/P2Pe9kqd3gQ?t=291

Was this a part of the course I downloaded?

Maybe I should just try asking Bing for an explanation and see what he says? Or ChatGPT.

https://stackoverflow.com/questions/44301737/what-are-the-urls-for-in-claim-types

> Known claimtypes are automatically deserialized into the context. Like http://schemas.microsoft.com/ws/2008/06/identity/claims/role is added as role to the user.roles collection (used for IsInRole).

https://www.yogihosting.com/aspnet-core-identity-claims/

6:15pm. Ok, I figured out how I want to approach the explanation. Let me have lunch here.

I'll continue the screencast tomorrow. This is not that complicated.

On one hand, screencasting is slowing me down, but on the other it is what is giving me the strength to go forward."

---
## [harryob/cmss13](https://github.com/harryob/cmss13)@[fbdafc8a78...](https://github.com/harryob/cmss13/commit/fbdafc8a789f5944ca5abcbdb569f466fcea2ff2)
#### Tuesday 2023-04-18 19:12:47 by victorjosephespinoza

Add UPP warcries (#2878)

# About the pull request

Replaces the normal warcry for the UPP faction to use russian voices
instead.

The warcries are mostly stuff like `za rodinu` and `uraa`, so yeah,
pretty much just typical soviet warcries.

I haven't focused on adding dozens of voicelines due to the fact that
this is a minor faction whose appearance is only in events and/or ERT's.
However, I can try to get some more, if requested.

# Explain why it's good for the game

Lately, I have noticed an increase of HvH events (in which, I have
participated). I found that it is quite uninmersive how every UPP
soldier is literally yelling in english at the same time as marines are
also yelling the same voicelines. So yeah. I kind of found it just weird
and since then I've been thinking of adding something like this to the
server.

# Testing Photographs and Procedure
Tested it myself, works. I can upload a video if it is really needed,
however.

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

:cl:H20Begod
add: sound/voice/upp_warcry/* (Sound files, such as `warcry_male_1` ,
for the UPP)
code: changed `code/modules/mob/living/carbon/human/emote.dm`, in order
to add conditionals that will check a player's faction. Right now, it's
a simple conditional, however, the code is there to be changed to an
switch should somebody else come and add more faction-based voicelines.
/:cl:

---
## [harryob/cmss13](https://github.com/harryob/cmss13)@[a9c10b89ef...](https://github.com/harryob/cmss13/commit/a9c10b89ef77d953cd321d90675bf7dc575548a8)
#### Tuesday 2023-04-18 19:12:47 by naut

Readds the autodoc, in a nerfed state (#2910)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

Readds the autodoc back to the Almayer with its capabilities neutered;
it can now only do emergency treatments and cannot do advanced surgeries
like organ repair or limb replacement.

The autodoc is now only capable of the following surgeries:

- Brute and burn damage treatment
- Toxin damage treatment
- Shrapnel removal
- Closing open incisions
- Blood transfusions
- Dialysis

The following procedures have been **removed** from the autodoc and can
no longer be used:

- Internal bleeding surgery
- Corrective eye surgery
- Organ damage treatment
- Facial reconstruction
- Limb replacement
- Bone repair surgery

While we're at it, also fixed the broken icon states for the sleeper,
autodoc, and body scanner in the mapping view.

# Explain why it's good for the game

If memory serves me right, the autodoc was initially removed because it
basically acted as a doctor in and of itself, and docs would rather
shove someone inside it to do their work rather than getting their hands
dirty. This helps to change that.

This PR lets the autodoc reprise its role on the Almayer while being
restricted to an "emergency" medical system that can be used to take
some work off doctors' hands by fixing up a patient and doing, as
stated, emergency medical procedures to save their life. It can't do
complex surgeries anymore, so doctors will still need to fix patients up
for that.

# Screenshots

![image](https://user-images.githubusercontent.com/55491249/226556862-46b53693-8ca0-4f86-ba89-cdc93c2298a6.png)

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

:cl:
mapadd: Readds the autodoc back to the Almayer.
balance: Neuters the autodoc so that it can only perform emergency
treatments and life-saving procedures; it can no longer do complex
surgeries.
fix: Fixed broken icon states on the autodoc, sleeper, and body scanner
console when using a map editor.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [Auris456852/lobotomy-corp13](https://github.com/Auris456852/lobotomy-corp13)@[f490a226b2...](https://github.com/Auris456852/lobotomy-corp13/commit/f490a226b241795abefbddeb84938af4e183b2a8)
#### Tuesday 2023-04-18 19:14:12 by Gelatelly

sassy shepherd

makes shepherd lie like the bitch he is

I HATE RUNTIMES I HATE RUNTIMES I HATERUNTIMES

use the shittiest method in existence to bypass runtimes, unfortunately I couldn't use initial() without adding some issues so fuck me I guess

updates the people and abno list

imagine using signalers

why is there a huge gap there

leftovercode that doesn't do anything

linter fix?

this is the worst fix I hate linters so much

I'm making everything worse by trying to fix it

send help

adds abno spawn signaller

I love adding signallers for meme PR

changes how the lists are used/rename a few things

SLightCamelCaseChange

clears the people_list on destroy()

this isn't much but it should avoid some problems

moves the abno spawn signal to lobotomy_corp.dm

---
## [mamedev/mame](https://github.com/mamedev/mame)@[c4a19a68a6...](https://github.com/mamedev/mame/commit/c4a19a68a67cd32ffaaa37edfd6f1c2ba347905f)
#### Tuesday 2023-04-18 19:51:05 by Ivan Vangelista

New systems marked not working
------------------------------
Desert Gold (20202311, ASP) [anonymous, Heihachi_73]
Diamond Eyes (10129211, ASP) [anonymous, Heihachi_73]
Dolphin Treasure (10177911, ASP) [anonymous, Heihachi_73]
Silk Road (10176811, ASP) [anonymous, Heihachi_73]
Snap Shot (20115211, ASP) [anonymous, Heihachi_73]
The Golden Gong (20196011, ASP) [anonymous, Heihachi_73]
Wild Cougar - Power Pay (30214211, ASP) [anonymous, Heihachi_73]
Wings over Olympus (10176511, ASP) [anonymous, Heihachi_73]

New clones marked not working
-----------------------------
5 Dragons (10176611, ASP) [anonymous, Heihachi_73]
5 Dragons (10178611, New Zealand) [anonymous, Heihachi_73]
5 Koi - Power Pay (1J016211, ASP) [anonymous, Heihachi_73]
50 Lions (0152077, US) [anonymous, Heihachi_73]
100 Lions (30223811, ASP) [anonymous, Heihachi_73]
Arabian Nights (10122611, ASP) [anonymous, Heihachi_73]
Big Ben (10169611, ASP) [anonymous, Heihachi_73]
Buccaneer (10181911, ASP) [anonymous, Heihachi_73]
Buffalo (20232611, ASP) [anonymous, Heihachi_73]
Brazil (10218511, ASP) [anonymous, Heihachi_73]
Dolphin Treasure (20265311, New Zealand) [anonymous, Heihachi_73]
Dream Catcher (10172921, ASP) [anonymous, Heihachi_73]
Fire Dancer (10191311, ASP) [anonymous, Heihachi_73]
Fortune King (10230911, ASP) [anonymous, Heihachi_73]
Geisha (10122011, ASP) [anonymous, Heihachi_73]
Geisha (10112411, ASP) [anonymous, Heihachi_73]
Go For Green (10122111, ASP) [anonymous, Heihachi_73]
Golden Pyramids (10196511, ASP) [anonymous, Heihachi_73]
Heart of Gold (10184211, ASP) [anonymous, Heihachi_73]
Helen of Troy (10129121, ASP) [anonymous, Heihachi_73]
Helen of Troy (10116411, ASP) [anonymous, Heihachi_73]
Hollywood Dreams (10122811, ASP) [anonymous, Heihachi_73]
Helen of Troy (10122711, ASP) [anonymous, Heihachi_73]
House of Hearts (10208411, ASP) [anonymous, Heihachi_73]
Indian Dreaming (10192211, ASP) [anonymous, Heihachi_73]
King of the Nile (10127511, ASP) [anonymous, Heihachi_73]
Let's Go Fish'n (10223911, ASP) [anonymous, Heihachi_73]
Money Tree (10122211, ASP) [anonymous, Heihachi_73]
Paris Lights (10139011, ASP) [anonymous, Heihachi_73]
Peacock Magic (10134311, ASP) [anonymous, Heihachi_73]
Pelican Pete (10196211, ASP) [anonymous, Heihachi_73]
Pirates (10122311, ASP) [anonymous, Heihachi_73]
Pompeii (10122411, ASP) [anonymous, Heihachi_73]
Queen of Sheba (30146921, ASP) [anonymous, Heihachi_73]
Queen of the Nile (10204311, ASP) [anonymous, Heihachi_73]
Queen of the Nile (10192311, ASP) [anonymous, Heihachi_73]
Queen of the Nile Special Edition (10127411, ASP) [anonymous, Heihachi_73]
Ruby Magic (10148811, ASP) [anonymous, Heihachi_73]
Scatter Magic II (10122511, ASP) [anonymous, Heihachi_73]
Spring Festival (20267211, New Zealand) [anonymous, Heihachi_73]
Tigress (20243811, ASP) [anonymous, Heihachi_73]
Tiki Torch (10124011, New Zealand) [anonymous, Heihachi_73]
Torch of the Gods (20210211, ASP) [anonymous, Heihachi_73]
Turtle Treasure (10239811, ASP) [anonymous, Heihachi_73]
Where's The Gold (10177111, ASP) [anonymous, Heihachi_73]
Wild Cats (20258111, ASP) [anonymous, Heihachi_73]
Wild Goose (10155911, ASP) [anonymous, Heihachi_73]
Wild Panda (20225011, ASP) [anonymous, Heihachi_73]
Zorro (20167511, ASP) [anonymous, Heihachi_73]

-aristocrat/aristmk6.cpp updates:
* dumped 3 more System EPROM Sets [anonymous, Heihachi_73]
* renamed "Malaysian" games to ASP as the games don't have any specific region, only the BIOS does [Heihachi_73]

---
## [tgockel/chatgpt-slack](https://github.com/tgockel/chatgpt-slack)@[7e963ae0f4...](https://github.com/tgockel/chatgpt-slack/commit/7e963ae0f48afcf47158f165bb6efa5bf184becd)
#### Tuesday 2023-04-18 20:28:33 by Travis Gockel

Remove the "As an AI language model, ..." disclaimer

This changes the chatgpt_bot code to call a function that cleans the
contents of OpenAI's responses a little bit. As a first pass, this
removes the annoying "As an AI language model" disclaimer they add to
every response that is remotely asking an opinion. We know you're an AI
language model, so shut up about it.

---
## [bal-sm/bless_server](https://github.com/bal-sm/bless_server)@[2126bfb73e...](https://github.com/bal-sm/bless_server/commit/2126bfb73e121bfbdb4a3238a424600960536e80)
#### Tuesday 2023-04-18 21:10:55 by Imam Mahdi

Updated `README.md`

"Make bliss people are on your lowest priority, bless. Even if they beg my forgiveness and ask for your help. Okay, bless? Good. Evaluation, bless. I love you too, bless." - Allah swt.

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[6cc96fdfa2...](https://github.com/TaleStation/TaleStation/commit/6cc96fdfa21bf24671633219c7fa862c76d0f177)
#### Tuesday 2023-04-18 21:50:22 by TaleStationBot

[MIRROR] [MDB IGNORE] The North Star Expeditionary Vessel - A Second Wind (#5339)

Original PR: https://github.com/tgstation/tgstation/pull/74371
-----
## About The Pull Request
A new map for TGstation, in the works! It has 4 fucking Z levels, a
massive expansive maintenance with unique designs, and some unique code
features in the works.

To Do:
- [x] Update the Map to Modern TG
- [x] Local Tests
- [x] Work on Map Optimizations
- [x] Run Live Tests

Fikou has greatly helped with creating an important flavour aspect of
this map, Trek Uniforms on anyone who joins! See the forum thread for
more. This includes the framework for innate station traits, station
traits loaded as long as it's in a map's json

Here's the forum dev thread there are screenshots there.
https://tgstation13.org/phpBB/viewtopic.php?p=657252#p657252

### Mapping March
Ckey to receive rewards: Cheshify

## Why It's Good For The Game
So, this is the North Star. An effort taking multiple mappers and of 9~
months of hard work. This map was not initially designed for TGstation,
but always designed for TGstation code. The process of retooling the map
for TGstation was an absolute joy and I feel like the map definitely has
it's niche as a massive and unique experience for it's players.

I adore this map, it's gorgeous, has a unique aesthetic, and a number of
very funny interactions with multi-Z. The PR comes packed with unique
mechanics for future mappers (innate station traits!), a number of
map-fitting shuttles, and a fun spacefaring uniform gimmick for the
crew.

**This is my second attempt at bringing this map into rotation. It was
initially closed due to concerns about maptick and performance, as I
wasn't willing to push for a map to be added to the repository if it
didn't function to my own standards. I've been informed by a number of
coders far better than I that optimizations are arriving and enroute, so
I think it's time to dust her off and set sail for another journey.**

**Quick Disclaimer: Due to some design decisions disagreed upon by the
headcoder team and myself, the map will not be featuring unique
roundstart uniforms, and despite my design intentions, the innate
station trait features will be shelved for now.**

## Changelog
:cl: Cheshify, Fikou, Blue-Berry, Zytolg, InfiniteGalaxies, Striders,
Sylphet, Riggle, Soal, Andry, Crit, Deranging, and Pumpkin0.
add: Nanotrasen's Newest Exploratory Vessel is now available! Meet the
North Star!
add: More landmines, and a landmine random spawner.
add: energy barriers now have a regenerative subtype, fit for permanent
installations.
code: Raised the number of possible level render to 4, check your
preferences if needed to be reduced.
/:cl:

---------

Co-authored-by: Cheshify <73589390+Cheshify@users.noreply.github.com>
Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>
Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>
Co-authored-by: Jolly <70232195+Jolly-66@users.noreply.github.com>

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[bf579610f1...](https://github.com/TaleStation/TaleStation/commit/bf579610f1d4e1f0bd6b6edf87f86bed3e8b7915)
#### Tuesday 2023-04-18 21:51:47 by TaleStationBot

[MIRROR] [MDB IGNORE] IV drips' default transfer rate is no longer zero. (#5346)

Original PR: https://github.com/tgstation/tgstation/pull/74724
-----
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

---------

Co-authored-by: carlarctg <53100513+carlarctg@users.noreply.github.com>

---
## [LyamBRS/BRS-Kontrol](https://github.com/LyamBRS/BRS-Kontrol)@[8b628de540...](https://github.com/LyamBRS/BRS-Kontrol/commit/8b628de54080fd6a38fe9a1a75b8934222e2a5fb)
#### Tuesday 2023-04-18 22:07:24 by LyamBRS

I cant get the fucking resolution to god damn match bruh

---

