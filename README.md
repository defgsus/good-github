## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-04-06](docs/good-messages/2023/2023-04-06.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,212,014 were push events containing 3,408,201 commit messages that amount to 256,996,926 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 65 messages:


## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[11cbbba018...](https://github.com/tgstation/tgstation/commit/11cbbba018e861237ce4bed73f19b58874c22042)
#### Thursday 2023-04-06 00:02:39 by Sol N

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
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[00f8bcfe75...](https://github.com/tgstation/tgstation/commit/00f8bcfe75275b7452063d1d8ec75d4c8e643f8b)
#### Thursday 2023-04-06 00:02:39 by MrMelbert

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
## [Mu-L/libgdx](https://github.com/Mu-L/libgdx)@[e1d1fdc5fb...](https://github.com/Mu-L/libgdx/commit/e1d1fdc5fb5b8409dc74f638c633ead405e535f3)
#### Thursday 2023-04-06 00:04:53 by Tommy Ettinger

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
## [Mojave-Sun/mojave-sun-13](https://github.com/Mojave-Sun/mojave-sun-13)@[237789979a...](https://github.com/Mojave-Sun/mojave-sun-13/commit/237789979a56a09589e299cf362a090ae8273805)
#### Thursday 2023-04-06 00:22:12 by ProfessorPopoff

Drought babyyyy!! Spawners/Mobs distribution. Baron town and more (#2326)

Okay! So basically this is an unatomized PR. This adds in a lot of things that we need for Drought to be the best it can. It includes things like a mappersprite edit cape for the Baron.... Crafted terminal fixes... A bunch of structure visual shifts, new pipes added- a metric FRICK ton of new walls SPECIFICALLY FOR DROUGHT.

Legion have gender checks now. If you're not a male, it makes you a male and gives you a random legion name. They're pretty cool. Similar situation with the Baron. Female becomes male. Gets cool name. You get the jist.

NOMADS. Nomads are Wastelanders that look different. Specifically for Drought. yippie.

On top of any coding changes, obviously there's a ton of work put into Drought itself. There's mobs and loot dispersed through the map. Well? I don't know yet. We'll see in testing. I personally added two locations. The Barony, and some little adobe shacks on the long stretch to the raider base. I've fixed up a TON of errors, go count them all! There's likely more left. I was as thorough as I could be.

---
## [Xander3359/tgstation](https://github.com/Xander3359/tgstation)@[c27f9a6d9b...](https://github.com/Xander3359/tgstation/commit/c27f9a6d9b9739baae09db063b6eb266d525772c)
#### Thursday 2023-04-06 00:26:39 by necromanceranne

Minor Nukie Thing: Bolt-action Sniper Rifle, balance coding, and some ammo changes (#73781)

## About The Pull Request

### The Rifle:
-The Sniper Rifle is now a bolt action. This replaces the 4 second fire
delay on the sniper rifle. This overall will improve the fire rate if
you're good at racking the bolt, but it will also feel less like you're
in a weird limbo of inaction while using the sniper rifle, since the
fire delay can be quite confusing to players not used to it. This can be
tweaked, like reducing the speed of the racking action, if it seems like
it is too much.
-The scope component now goes up to 50 tiles (or so), which allows you
to gain a significant sightline over an area. The reasoning for this is
simple. The component actually nerfed the overall range of the sniper
rifle's scope, so this should hopefully restore that somewhat. And
having such a huge sightline makes it much easier to utilize the
impressive range of the rifle. Currently, it's really only ideal for
extremely close range fighting.
-The normal sniper rifle, the one that syndicate base scientists get,
can be suppressed. I don't know why it was different.

### The Ammo:

Normal .50 BMG: Does much more object damage, and on top of that deals
additional damage to mechs, but not by much more. Now, when it
dismembers a limb, it also deals its damage to the chest. This ensures
that you didn't straight up lose out on dealing a killing blow because
you took their limb off, and makes the dismemberment property of .50 BMG
a significant upside rather than a immense detriment.

Marksman: Gains a lot of the above benefits, but has much lower range.
Why this nerf? It's actually because of some funny nonsense with how
ricochet works. Which can cause....accidents to happen. To you. Consider
that firing down a straight line and missing could be quite embarrassing
when the bullet has 400 tiles of range.

Soporific: Now called Disruptor ammo. Works as it did before, putting
humans to sleep for 40 seconds (seriously, 40 seconds). Also deals some
stamina damage, if...that's relevant. But now also causes an EMP effect
and a boatload of added damage to both mechs and borgs, allowing it to
be an excellent anti-mech and anti-borg ammo type, as well as scrambling
any pesky suit sensors, energy weapons and so on in an area around the
impact. Useful for support fire.

Incendiary (NEW!): Causes a massive firebomb to go off where it impacts
(no explosion, so this isn't a stun). Also sets the target on fire,
which is always fun. Good for shooting into groups of people with
impunity. Also deals burn damage instead, since I think nukies could use
more methods for direct fire damage.

Surplus (NEW!): It's .50 BMG but it lacks most if not all the upsides.
No armour penetration, no dismemberment, no paralysis. It still deals a
lot of damage to objects, so not a bad option for simply removing
structures from afar. So what's the point in this ammo? You can buy 7
magazines for the price of one. I want to introduce 'Surplus' as an idea
for nukies to invest in if they want to be able to keep shooting but
they're really on a budget, like most non-warop nukies tend to be. This
is definitely subject to change (like a damage decrease on top of
everything else).

Pricing and Capacity: Normal ammo and surplus costs 3 TC. Every special
ammo costs 4 TC. Every special ammo also has the same ammo capacity as
the normal magazine. It's kind of weird how most of the subtypes had 5
shots rather than 6, but then soporific had...3? I don't get it. This
would probably cause a good deal of confusion, especially if you are
swapping ammo types and weren't aware of this particular oddity.

Anyway, 6 shots.

### Minor Addition
Gets rid of the cheap suppressor. It lies to players, tricking them into
thinking this is a low quality suppressor. Newsflash, it isn't. There is
no distinct difference between that suppressor and the normal
suppressor.

## Why It's Good For The Game

The sniper rifle, unfortunately, sucks a lot except for very specific
use cases. It got a big nerf with the scope component in terms of range,
even if the functionality is way cooler. And, at a baseline, there was
some counterintuitive functions attached to it. Dismemberment was cool,
but it also caused a loss in overall damage due to how limbs contribute
to core health. On top of this, the cool ammo types were...not much
better? Penetrator was almost always the best option, even if it lost a
lot of damage as a consequence.

So, what was it good for? X-ray + Penetrator. Pretty much, that's it. It
has some other uses but if I had to be entirely honest, there wasn't
much that other weapon couldn't do as well.

Hopefully this helps things going forward, and I want to mess with this
as well down the line in case its a bit too much of a boost in power.

Absolutely please rip this PR apart.

## Changelog
:cl:
balance: Makes the syndicate sniper rifle a bolt-action rifle.
balance: Sniper rifles have a scope range of roughly 50 tiles.
balance: Sniper rifle ammo, if it dismembers your limbs, does damage to
the chest.
balance: All the various syndicate sniper rifle magazines have
consistent casing quantities (6 shots). They also have more consistent
pricing. 3 for normal and a box of surplus, and 4 for every other type.
balance: Reduces the range of Marksman ammo to 50 tiles. Not because it
is strong, but because you might accidentally shoot yourself if you're
not watching where you're shooting. Ricochets are no joke.
add: Replaces Soporific with Disruptor ammo. Works like soporific, but
also EMPS things it hits.
add: Adds Incendiary .50 BMG. Causes a combustion to erupt from the
struck target, as well as setting targets on fire. Great for parties.
add: Adds Surplus .50 BMG. It sucks, but you get a lot of them! Quantity
over quality, baby.
remove: The suppressors in the bundle are of standard quality. The
apparent 'cheap suppressor' that came bundled with the C-20r and sniper
rifle were found to actually be 'fine'. Trust us.
/:cl:

---
## [Xander3359/tgstation](https://github.com/Xander3359/tgstation)@[95b810919e...](https://github.com/Xander3359/tgstation/commit/95b810919ede0f4fb22dc711c0334abf36b94843)
#### Thursday 2023-04-06 00:26:39 by lizardqueenlexi

Adds preference for "Tagger" paint color. (#74281)

## About The Pull Request

Per the title, this PR allows you to pick your starting paint color from
the "Tagger" quirk on the character preferences menu.


![image](https://user-images.githubusercontent.com/105025397/227810007-4706c743-31c2-47d8-80ac-e11687d36c00.png)

This replaces the starting color being random; it does not prevent you
from changing the color later as normal.
## Why It's Good For The Game

It's a minor quality of life change. This will mostly be helpful to
players who have some "signature" color they like to use, to prevent
having to manually select it (and possibly input a color code) every
round. It will be of less relevance to those who tend to select new
colors every round anyway.

Possible downsides are mainly adding another pref to the menu, although
this shouldn't be too much of an annoyance since it only appears if you
already have the relevant quirk. It does also remove the _ability_ to
have a randomly-chosen paint color, though I'm not sure if that matters.
## Changelog
:cl:
qol: you can choose your default paint color for the "Tagger" quirk from
prefs.
/:cl:

---
## [Tastyfish/-tg-station](https://github.com/Tastyfish/-tg-station)@[c0ef4ba907...](https://github.com/Tastyfish/-tg-station/commit/c0ef4ba907b28e1288f2ccbbc6714d15a923b1bd)
#### Thursday 2023-04-06 00:27:54 by tralezab

Adds the Dark Matt-eor when you emag a stupid amount of meteor shields + lots of meteor file sorting + qol + dark matter singularity + dark matt-eor summoning final traitor objective (#74330)

## About The Pull Request

<details>
  <summary>Dark Matt-eor Image</summary>
  

![image](https://user-images.githubusercontent.com/40974010/228368755-34ae5f89-e1bb-498b-bbf8-a14ff4240dc0.png)

</details>

> A barely visible blur in the cosmic darkness, like a ghostly shadow on
a moonless night. A piercing howl in the vacuum of space, as if it were
tearing the fabric of reality. A twisted halo of light around it,
bending and breaking the rays of distant suns. A shower of quantum
sparks, flickering and fading in its wake. A dark matter meteor (dark
matt-eor) is a wonder to witness, and to dread.

> A sudden impact, like a hammer blow to the heart of the station. A
violent tremor, shaking and shattering the metal walls and windows. A
deafening roar, as the air rushes out of the breached hull. A blinding
flash, as the dark matter meteor unleashes its hidden energy. A tiny
black hole, forming and growing in the center of the station. A
relentless pull, dragging everything towards the abyss. A dark matter
meteor is incredibly deadly.

Emagging too many meteor shields will summon a dark matt-eor. This comes
with several warnings, and after awhile, warns the station that someone
is trying to summon a dark matteor.

The dark matt-eor itself is not that damaging in its impact, but drops a
singularity in its final resting place.

## Why It's Good For The Game

It's a new way to terrorize a round as an antagonist. Before, emagging a
lot of meteor shields would basically make meteor showers the only event
that can run, which is cool, but since constant meteor waves are going
to destroy the station, let's also throw in the mother of all meteors!

This also adds warnings to spamming emagging meteor shields, which imo
needs it. The round ends when someone spams emagged meteor shields, and
since they're meteor shields nobody is going to reasonably check on
them.

## Changelog
:cl:
add: The dark matt-eor
add: Summon a dark matt-eor final traitor objective
add: Dark matter singularity variant, which can't grow as big as a
regular singularity but hungers for blood
code: cleaned up/sorted meteor shield code, satellite control, and more
qol: added a lot of feedback to interacting with meteor shields
balance: emagging a lot of meteor shields warns the station, but
emagging enough of them summons a Dark Matt-eor.
/:cl:

---
## [Comxy/tgstation](https://github.com/Comxy/tgstation)@[e65dff59bd...](https://github.com/Comxy/tgstation/commit/e65dff59bd47f5805e8b33f623f02cd1700d22ec)
#### Thursday 2023-04-06 00:42:29 by zxaber

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
## [Comxy/tgstation](https://github.com/Comxy/tgstation)@[dc2f52e386...](https://github.com/Comxy/tgstation/commit/dc2f52e386e0ef3cfcc2133293cd3f68f6a1eee3)
#### Thursday 2023-04-06 00:42:29 by tralezab

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
## [Comxy/tgstation](https://github.com/Comxy/tgstation)@[48183ec0ff...](https://github.com/Comxy/tgstation/commit/48183ec0ffd67ea5afa26c6f6e58e81edff98d52)
#### Thursday 2023-04-06 00:42:29 by san7890

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
## [Comxy/tgstation](https://github.com/Comxy/tgstation)@[9dfe00d79d...](https://github.com/Comxy/tgstation/commit/9dfe00d79dd7bd540442ce825caa4e964c619b46)
#### Thursday 2023-04-06 00:42:29 by san7890

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
## [Donglesplonge/tgstation](https://github.com/Donglesplonge/tgstation)@[c3b78761d2...](https://github.com/Donglesplonge/tgstation/commit/c3b78761d29c53558fd993c84bb808bd5783861d)
#### Thursday 2023-04-06 00:53:16 by tralezab

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
## [Donglesplonge/tgstation](https://github.com/Donglesplonge/tgstation)@[b5ebf5c942...](https://github.com/Donglesplonge/tgstation/commit/b5ebf5c9423cb3b39a2b9cfb6524b157dc6cb4b2)
#### Thursday 2023-04-06 00:53:16 by Helg2

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
## [Mooshimi/tgstation](https://github.com/Mooshimi/tgstation)@[fe7ebd67cf...](https://github.com/Mooshimi/tgstation/commit/fe7ebd67cf74982038524ceb175377d7ff6c0486)
#### Thursday 2023-04-06 01:06:54 by LemonInTheDark

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
## [challade/cmss13](https://github.com/challade/cmss13)@[a2d5ca6e69...](https://github.com/challade/cmss13/commit/a2d5ca6e69725341f0fa261a4a3f89c737e843b3)
#### Thursday 2023-04-06 01:55:22 by QuickLode

Introducing the Colonial Marshal ERT w/ Anchorpoint Marines (#2318)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request
My first PR of this scale, for sure. 

Been working on this PR for two weeks off and on, and finally I believe
I have checked every box that I intended to check when I first thought
of this idea a couple months back in November or so. Original idea:
https://discord.com/channels/150315577943130112/1037030635820306562/1037030635820306562

It will be adding a Colonial Marshal Bureau ERT, a Colonial Marshal
Bureau Inspection Team, and an Anchorpoint Station ERT.

First: Anchorpoint Station, unlike many ERTs, this one will hail from a
station. The station is located in the Neroid Sector and is used as a
transit / refinery station. It's large enough to hold 3000 but never
reaches its full potential. It consists of four towers and a central
module - one of the towers houses a permanent CMB presence and in the
same tower, a contingent of Colonial Marines is onboard. There's also a
Seegson office but I didn't do anything with it here.
Reference: https://avp.fandom.com/wiki/Anchorpoint_Station

For standard inspections, a dropship is dispatched from Anchorpoint
Station to the USS Almayer to carry out their objectives.
I do expect this to be the primary usage of this entire PR, because
there was always a part lacking for Anti-Corporate/Anti-Smuggling/CMB
type of interactions. It was almost always focused on Corporate, or
USCM. Nothing else. You should consider this to be an HRP addition to
the game.

Its also important to note that the Colonial Marshals are **Colonial**
and UA law enforcement agents / investigative functionaries. **They
shouldn't be enforcing Marine Law** unless: 1. The CMP/aCO has requested
it, 2. The Colonial Marshal believes its in the best interest of the CMB
and 3. The CMB Office at Anchorpoint(admins) does not intervene to
change this decision. Jurisdiction is another interaction that will be
nice to see. Non-USCM suspects should be transferred to the CMB, and
vice versa. The CMB should also be handling crimes, especially with the
ICC, involving smuggling, black market activities, and corporate
corruption/cover-ups.

**The Colonial Marshal** - He leads the team, and should be an
experience player with some knowledge of the lore behind what they are
doing. There's objectives and a backstory to help guide players if they
are unaware.
**The CMB Investigative Synthetic** - Unlike what you would expect from
most Synthetics, this one(as the name implies) is purely for
investigative and/or law enforcement purposes, though they have brought
along a medical belt.
**The CMB Deputy** - Working under the lead of the Marshal, his loyal
deputies uphold Colonial Law, Earth Law, and help with investigations
and/or law enforcement should it be needed.
**Interstellar Commerce Commission Corporate Liaison** - This Executive
works with the Colonial Marshals specifically to observe proper trade
practices and investigate any possibilities of smuggling or black market
activity. They are also an advisory agent to the Marshals by giving them
an eye on the corporate side of things.
**Interstellar Human Rights Observer** - Through a lot of hard work, the
Observer has managed to make his way onto the frontier to document and
record any kind of atrocities that may be occurring in this dark sector
of space. It's a bit of a PR stunt, but the Observer might surprise you.
Also, in an emergency, the Observer may be able to provide medical aid
for the team - they are the most capable of it.


For Emergency Responses, a nearby dropship which was enroute to an
investigation of its own, is re-routed to the USS Almayer's distress
beacon. There is a 10% chance of this happening.
They will not fare very well in extended combat, because they are not
prepared for it. They simply come aboard to lend a helping hand to a
distress beacon.
As the Colonial Marshals are equipped for law enforcement and
investigations, they are comparably lightly armed to most things they
might encounter in or by the USS Almayer.

This is where the contingent of Colonial Marines in Tower 4 comes in.

The third ERT that may be called in is an Anchorpoint Station QRF Team.
Canonically this is purely used when a random-beacon is answered by the
CMB Patrol Team, and they are able to raise the radio back to base to
call in the QRF. Thus giving them an additional, albeit optional
objective. This is controlled entirely by admins, as the Anchorpoint QRF
Team, despite its small size and average skill levels, is equipped with
a decent amount of gear compared to the depleted stocks of the USS
Almayer. Should the CMB team be able to raise its own distress signal to
the preparing QRF team, admins may choose to grant, delay, or deny the
QRF entirely.



Those are the main points of the PR.
There are also small variation changes to CMB-related survivors and also
some changes to synths.dm. (I tried to refractor the code because the
last PR to it bugged out the way items spawn in, but I was unsuccessful
and those changes are not in this PR.)

Pizza ERT chance and Freelancer ERT chance was nerfed by 4 and 5
respectively. This gives room for this ERT, and also Pizza was a bit
LRP.. You see a ship burning with a giant hole in it and you go to
deliver a pizza...?

EDIT: Pizza ERT removed from rotation entirely a la morrow

I would love to give a great thanks to:
nauticall - for their awesome cap and badge sprites! Also they have just
been a great help to me for much of my time here :)
kitsunemitsu - for their CMB hud icons!
harryOB - for helping me with fixing my vars and procs in the main ERT!
I was able to make things a % chance thanks to him.
and forest2001 - for helping me troubleshoot and find a solution for a
really annoying piece of hud code.
<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

This is a great, non-combat ERT and extremely HRP addition which adds a
phenomenal avenue of RP to the game rarely seen before. There is someone
to investigate the CL, interact with survivors, give MPs someone to talk
to, take non-USCM prisoners, assist with CMB-survivors and especially
with the new Black Market update this ERT will have tons of potential to
bring really interesting dynamics to the Almayer. The Colonial Marshal
Bureau are a HRP oriented set of roles, perfect for mini-events.

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->


# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
<details>
<summary>
I have done extensive testing with this and believe I have figured out
pretty much every single bug. One thing I was not able to test was the
ERT messages for obvious reasons, but they seem to be sound - and a test
merge will definitely double check that.

In addition, there may or may not be a bug where the CMB cannot see
their own HUD Icons, but ghosts can just fine. I haven't been able to
find the cause of this yet.

https://media.discordapp.net/attachments/1042176396711170119/1064156692050358372/image.png</summary>

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

:cl: QuickLoad, nauticall, Kitsunemitsu, harryOB, forest2001
add: Introducing the Colonial Marshal Bureau Inspection and Emergency
Response Teams - A Law Enforcement & Investigative UA Functionary which
brings with it an HRP oriented set of roles perfect for your anti-corpo,
colonial, prisoner, smuggling, or other types of interactions on the
Almayer! It should unlock a very unique avenue of RP for many players,
especially smugglers, CL, survivors and the black market. This is a well
supported faction with their own frequencies, equipment, even faxes and
icons etcetera. The laws of the Earth stretch beyond the Sol.
add: Added the Anchorpoint Station Emergency QRF - A team of Colonial
Marines dispatched from Anchorpoint Station to respond to the CMB's
distress signal. Few in numbers, average in skills, but well equipped.
When things get dicey for the Marshals, they are the cavalry. This is an
admin call but makes it into an optional two-part ERT.
imageadd: Awesome looking CMB Cap, Marshal Badge and Deputy Badge by
nauticall!
imageadd: HUD Icons for each of the Colonial Marshal Bureau
Investigation Members, made by Kitsunemitsu!
imageadd: CMB key, hudsec and earpiece! Comes with a nice blue shale
radio color.
qol: Switched up some of the bugged synth loadouts, added some variety.
fix: Corrects the legacy path of hudsec where it was looking for old
paths instead of the updated ones - hudsec should work fine now. Thanks
to forest for his help in spotting these.
tweak: Superficial changes to cryo ERT loadout and CMB-relevant survivor
loadouts.
tweak: Superficial changes to armor vest so that they can carry
guns/lights.
tweak: Superficial changes to not being able to put on vests over
certain uniforms.
tweak: Freelancer ERT chance down from 25 to 20.
tweak: Synthetic vendor has some packs renamed for clarity, and receives
the tech welder satchel and medical satchel as an option.
del: Synthetic nurse hat is gone from Synthetics!
del: Pizza ERT is removed from rotation
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---------

Co-authored-by: naut <55491249+nauticall@users.noreply.github.com>
Co-authored-by: naut <nautilussplat@gmail.com>

---
## [Ebin-Halcyon/Skyrat-tg](https://github.com/Ebin-Halcyon/Skyrat-tg)@[2728bbe9a9...](https://github.com/Ebin-Halcyon/Skyrat-tg/commit/2728bbe9a9003dbb4283ac807108c65129b7f34d)
#### Thursday 2023-04-06 02:19:22 by SkyratBot

[MIRROR] Polishes some side sources of light and color [MDB IGNORE] (#19860)

* Polishes some side sources of light and color (#73936)

## About The Pull Request

[Circuit Floor
Polish](https://github.com/tgstation/tgstation/commit/6b0ee9813271f693ceb44ad42277c36ef2e71268)

Circuit floors glow! but it looks like crap cause it's dim and the
colors are washed out.
I'd like to make them look nicer. Let's make them more intense and
longer range, and change the colors over to more vivid replacements.

While I'm here, these should really use power and turn on and off based
off that.
Simple enough to do, just need to hook into a signal (and add a setter
for turf area, which cleans up other code too).

[Desklamp
Upgrade](https://github.com/tgstation/tgstation/commit/8506b13b9c97bf740c3e97db04450555387dd126)

Desklamps look bad. They're fullwhite, have a way too large
range.Crummy.
Let's lower their lightrange from 5 to 3.5, and make the ornate ones
warmer, and the more utilitarian ones cooler. The clown one can be
yellow because it's funny

I'm renaming a color define here so I'm touching more files then you'd
expect

[Brightens
Niknacks](https://github.com/tgstation/tgstation/pull/73936/commits/835bae28e9eb9946be53c9f5dac0a0a39f15ef21)

Increases the light range of request consoles, status displays,
newscasters, and air alarms (keycard machines too, when they're awaiting
input at least)
Increases the brightness of air alarms, I think they should be on par
with apcs, should be able to tell when they're good/bad.
Increases the brightness of vending machines (I want them to light up
the tiles around them very lightly, I think it's a vibe)

Fixes a bug with ai status displays where they'd display an emissive
even if they didn't have anything on their screen, looking stupid.
This was decently easy but required a define. Looked really bad tho

## Why It's Good For The Game

Pretty

<details>
<summary>
Circuit Floors
</summary>

Old

![image](https://user-images.githubusercontent.com/58055496/224534470-c6eac5f5-5de6-40e9-897d-3212b8796d81.png)

![image](https://user-images.githubusercontent.com/58055496/224534477-ad412ad9-f7c4-44ae-ad75-a1a2c9bd17be.png)

New

![image](https://user-images.githubusercontent.com/58055496/224534486-b7b408a3-546c-4f90-aa9f-0e58bf8128ad.png)

![image](https://user-images.githubusercontent.com/58055496/224534496-626458f7-ab63-429c-a5db-eae9c784d06a.png)
</details>

<details>
<summary>
Desk Lights
</summary>

Old

![image](https://user-images.githubusercontent.com/58055496/224534513-9868b0b8-bc73-4b45-b986-8445078a8653.png)

![image](https://user-images.githubusercontent.com/58055496/224534518-bbbc8c6d-b59e-4f28-a31c-6c6a7e2c2885.png)

New

![image](https://user-images.githubusercontent.com/58055496/224534529-7988f440-03be-42ef-894c-b9e77f577ae5.png)

![image](https://user-images.githubusercontent.com/58055496/224534532-c3f2c6bf-c925-4a59-a8f9-10bb955a9942.png)
</details>

The niknack changes are more minor so I'm not gonna grab photos for
them. I can if you'd like but I don't think it's necessary. Mostly a
vibes in dark spaces sorta thing

## Changelog

:cl:
add: I made circuit floors brighter and more vivid.
add: Made air alarms, vending machines, newscasters, request consoles,
status displays and keycard machines slightly "brighter" (larger light
range, tho I did make air alarms a bit brighter too)
add: Tweaked desklamps. Lower range, and each type gets its own coloring
instead of just fullwhite.
fix: AI displays are no longer always emissive, they'll stop doing it if
they aren't displaying anything. Hopefully this'll look nicer
/:cl:

* Polishes some side sources of light and color

* yellow

* Update dance_machine.dm

* Merge branch 'upstream-merge-73936' of https://github.com/Skyrat-SS13/Skyrat-tg into upstream-merge-73936

---------

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>
Co-authored-by: lessthanthree <83487515+lessthnthree@users.noreply.github.com>
Co-authored-by: Zonespace <41448081+Zonespace27@users.noreply.github.com>
Co-authored-by: lessthnthree <three@lessthanthree.dk>

---
## [shiptest-ss13/Shiptest](https://github.com/shiptest-ss13/Shiptest)@[babf89eb74...](https://github.com/shiptest-ss13/Shiptest/commit/babf89eb746741ba4f33f686b0c4750fe68e1603)
#### Thursday 2023-04-06 03:06:38 by The-Moon-Itself

SubShips attempt 2 (#1627)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Accidentally destroyed my old PR for this, #1573, by completely botching
a merge from master to the point that it was easier to make a whole new
fork than try to save it, so here we are again. Here's the original
description:

Ports the parts of beestation/beestation-hornet#7152 that adds the
framework for ships to land on top of each other and not break
everything. A ship can only land on another ship if there's an open
docking port on the mothership that's large enough for the subship.
Here's a video of it in action on a modified dwayne-class:


https://user-images.githubusercontent.com/51838176/195471361-f9f0d145-d7c9-480e-ad4a-d18705f2590f.mp4

This system should be able to handle just about any orientation of ships
on top of each other, such as ships landed across areas, multiple ships
landed on a single ship, a single ship landed on multiple ships, a ship
that is only partially landed on another ship, a ship that is partially
landed on a ship that's partially landed on another ship, and so on.
Just make sure that you never try to land a ship on itself.

Something to note for this is that ships remember what's underneath them
via baseturfs, and there's a hardcoded check that will cause errors if a
baseturf list grows over 10 entries long. Because ship turfs have
typically 1-3 baseturfs, after about 3 ships stacked on top of each
other things will start to break.

You can also make maps with subships on them, to do this, follow these
steps:
1. make the subship as if it were a regular ship in its own map file
2. create a new /datum/map_template/shuttle subtype that points to your
subship map, these datums can be found in code/datums/shuttle.dm
3. On your main ship, place "subship dock" landmark in turf where you
want the bottomleft corner of the subship's bounding box to be, you can
also use the offset_x and offset_y vars on the landmark to offset this
corner if you need to place the landmark somewhere else.
4. Set the "subship_template" var on the landmark to the path of your
subship's map_template subtype
5. Optionally change the dir on the landmark to rotate the subship. for
reference, NORTH is no rotation, EAST is a 90 degree clockwise rotation,
etc.

You can put the stationary docking port anywhere on your map, as long as
it's on the ship. You can have its bounding box hang off the side of
your ship, but please try to keep the entirety of its bounding box
within the bounding box of map file, otherwise subships landing on your
main ship might accidentally clip through structures nearby your
mainship, including virtual z level borders.
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
Subships allow for many more creative designs and interesting dynamics
between and within ships, especially when a crew may need or want to
split its attention between multiple locations at the same time, or to
make interactions between ships easier when you just need to land a
smaller vessel inside of the other, cutting out the need to travel
through space turfs to get between two ships.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: Subships are now possible
code: Lots of large changes to ship code
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Singul0/tgstation](https://github.com/Singul0/tgstation)@[e1221c986f...](https://github.com/Singul0/tgstation/commit/e1221c986f5da2551051f47aa0fbd1d49e367c9b)
#### Thursday 2023-04-06 03:16:19 by san7890

Chasm Hell On Icebox - 300 Active Turfs on Prod Moment (#74410)

## About The Pull Request

Spontaneous regressions introduced by #74359
(1e58c1875d9e2f48a306fe31a0626dbbb1990ff9).
```txt
 - Z-Level 2 has 150 active turf(s).
 - Z-Level 3 has 150 active turf(s).
 - Z-Level trait Ice Ruins Underground has 300 active turf(s).
 - Z-Level trait Mining has 300 active turf(s).
 - Z-Level trait Station has 300 active turf(s).
 - End of active turf list.
 ```

![image](https://user-images.githubusercontent.com/34697715/229213138-5a6a7a4f-edec-47ab-8def-ee4e4bddfe61.png)

Basically the lavaland ruin sucks dogshit and I had to do a lot of stuff to account for everything failing. There was even a moment where we were adding something to `flags_1` instead of `turf_flags` and that was also really bad to figure out.

![image](https://user-images.githubusercontent.com/34697715/229213428-63bb1f6e-6f88-4604-a3c6-e08e20cbfa7a.png)

i also had to add orange genturfs because it was really getting bad with all of the assertions we had to keep making, especially since stuff like this could also show up:

![image](https://user-images.githubusercontent.com/34697715/229213562-4a145453-5f90-4d05-b8cc-5c1beec2b0dd.png)

That's the prison in the red box, those are active turfs because a chasm scraped it away.

Sorry if this is hard to follow but I promise you everything in this is essential. I wish we didn't have to rely on turf flags as much as we do but this is a fix PR, not a refactor.
## Why It's Good For The Game

Even one active turf on IceBox ate up _three_ seconds of SSair's initialization every single time it was really fucking bad.

We haven't had to deal with chasms for about two years so there's a lot of mapping assertions we made since they just weren't a thing, but now they're back so lets do it properly.
## Changelog
:cl:
fix: The prison on IceBox should no longer leak air as often.
/:cl:

I have compiled this map about 30 times until active turfs stopped fucking happening and now I am content. This likely doesn't fix _everything_ because some stuff can still be hidden to me, and we still have PRs that need to be merged to reduce the amount of noise we're getting on prod.

---
## [Singul0/tgstation](https://github.com/Singul0/tgstation)@[0a1f7e8de2...](https://github.com/Singul0/tgstation/commit/0a1f7e8de2fea2116b73f22a11fdf328763c503a)
#### Thursday 2023-04-06 03:16:19 by Hatterhat

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
## [toolmind/cmss13](https://github.com/toolmind/cmss13)@[6f1b1717a7...](https://github.com/toolmind/cmss13/commit/6f1b1717a7d6ef3c04ef58c294353fe0b98ca836)
#### Thursday 2023-04-06 03:18:19 by TotalEpicness

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
## [Kapu1178/daedalusdock](https://github.com/Kapu1178/daedalusdock)@[27d37cb0f4...](https://github.com/Kapu1178/daedalusdock/commit/27d37cb0f47d007d1159ad5af69ace39a50b003f)
#### Thursday 2023-04-06 03:24:26 by Gallyus

Alternate Version Tests (#281)

* AltVer Checks
I think?
Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

* 1603 target

* support script

* HOLY SHIT CAN I READ

* e

* HOLY FUCK CAN I READ

* Disable shortkill version check

---
## [khevy/tgstation](https://github.com/khevy/tgstation)@[d43ebd042d...](https://github.com/khevy/tgstation/commit/d43ebd042dd751842728e8cb91fa7fc1a82f26d0)
#### Thursday 2023-04-06 03:43:44 by san7890

Log Active Turfs To Mapping Log (#74267)

## About The Pull Request

Was reminded of doing this via
https://github.com/tgstation/tgstation/issues/74245#issuecomment-1483943979

They're mapping issues, so let's log them to the mapping log. Quite
shrimple honestly.


![image](https://user-images.githubusercontent.com/34697715/227805458-5e6bcf01-629d-4b81-ab6a-b26e63d41ca3.png)
## Why It's Good For The Game

As the comments expound, the reason why we probably haven't done this in
the past is because any number of things can cause active turfs (like
ruin placement (either in icebox or in space)), or other silly stuff
like that. Thus, finding stuff like this would only really be viable
with stuff like the View Active Turfs verb, where you could visually
jump to and see all of the active turfs in that dynamic configuration
(and this still remains the best way to find active turfs).

This PR just makes it easier to do a "post-mortem" analysis on potential
active turfs, so that if it's very blatant, it can be fixed a lot
easier. It's best to try and find them during an ongoing round, but this
is life. (same as the unit tests concession, not too enthused on that
but we would have spontaneous errors out the ass without _something_)
## Changelog
Nothing that concerns players.

---------

Co-authored-by: tattle <66640614+dragomagol@users.noreply.github.com>

---
## [khevy/tgstation](https://github.com/khevy/tgstation)@[40fc11eb07...](https://github.com/khevy/tgstation/commit/40fc11eb0733ca25eff56e7379cb574a997fb6d3)
#### Thursday 2023-04-06 03:43:44 by LemonInTheDark

Optimizes some gas_mixture procs, Optimizes pipeline processing significantly by 33% (#74233)

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

---
## [ieee802dot11ac/YARG](https://github.com/ieee802dot11ac/YARG)@[24eb6419fa...](https://github.com/ieee802dot11ac/YARG/commit/24eb6419faf0718b3214a35cbd5426f8bfdc2c6b)
#### Thursday 2023-04-06 03:44:24 by ieee802dot11ac

Squashed commit of the following:

commit be0df578854fec832001d6473242dd420f40baa6
Author: ieee802dot11ac <69217234+ieee802dot11ac@users.noreply.github.com>
Date:   Wed Apr 5 20:43:07 2023 -0700

    fix some shit, excuse me while i unbreak git

commit ac1aff4476a4c49680fd6b24e3f17b872057e260
Author: ieee802dot11ac <69217234+ieee802dot11ac@users.noreply.github.com>
Date:   Wed Apr 5 17:16:41 2023 -0700

    progress (oh god i'm sorry)

commit 3145dfe1bf090c11498f7c0b93d0a6643f27f052
Merge: 2028521 0ed0847
Author: EliteAsian <lavasnakegaming@gmail.com>
Date:   Wed Apr 5 12:04:38 2023 -0400

    Merge pull request #48 from ieee802dot11ac/master

    INCOMPLETE Add songs.dta reading support

---
## [TheBoondock/tgstation](https://github.com/TheBoondock/tgstation)@[9d5b4907e8...](https://github.com/TheBoondock/tgstation/commit/9d5b4907e8d8aaecf24bfd8f6755822b494a4b55)
#### Thursday 2023-04-06 03:45:14 by Rhials

Post-Revolutionary Fervor station trait, revolutionary bedsheets, and a megaphone (#73799)

## About The Pull Request

Upon revolution success, the chosen headrev will now also receive a
megaphone, and a "revolutionary bedsheet" repurposed from a stolen CC
bedsheet to commemorate their success. The post-revs confusion and lack
of command/security usually leads to an instantaneous, total breakdown
in cohesion. It's every man for himself -- that's no way to run a
commune! Just because the revolution has succeeded and nobody can see
your big blue "R" anymore doesn't mean you can't be a leader!


![image](https://user-images.githubusercontent.com/28870487/222981576-e62e457b-1b2d-4756-8c87-7a9093c92c2d.png)

This also adds a new revolution-themed negative station trait --
Post-Revolutionary Fervor. When present, this trait trashes the command
areas at the start of the round. This means cracked windows, broken
consoles, vendors getting knocked over, and the occasional dead
greytider.


![image](https://user-images.githubusercontent.com/28870487/222981095-14ce9336-2320-406e-b0a6-dc91cb8f9479.png)

If you start cleaning at the start of the round, you might finish right
as the next batch of revs decides to crop up.
## Why It's Good For The Game

Giving one of the headrevs a bigger voice and a cool cape (or uncool,
depending on how you view the sprite) means that there's a chance for
them to step up and try to keep the wheels on. Just remember -- Nobody
is obligated to actually listen to this person, it's just a bedsheet.

Adds a neato station trait, which probably counts as command gameplay
content.

## Changelog
:cl: Rhials
add: The headrev who receives the revolutionary banner after a win will
also receive a commemorative bedsheet and megaphone.
add: Post-Revolutionary Fervor station trait. I hope you enjoy fixing
broken computer screens.
spriteadd: A revolutionary bedsheet.
/:cl:

---
## [thesamesam/portage](https://github.com/thesamesam/portage)@[f4147929ec...](https://github.com/thesamesam/portage/commit/f4147929ec10201651ac67e6558f9d8febc40f03)
#### Thursday 2023-04-06 03:56:44 by Sam James

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
## [thgvr/tgstation](https://github.com/thgvr/tgstation)@[d55ce0f0bc...](https://github.com/thgvr/tgstation/commit/d55ce0f0bcb6c37113c9ec9f0e37facd99b69625)
#### Thursday 2023-04-06 05:10:07 by Jacquerel

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
## [ZAMODA/tgstation](https://github.com/ZAMODA/tgstation)@[97f567fdc7...](https://github.com/ZAMODA/tgstation/commit/97f567fdc745230b1594c305680dce683512d032)
#### Thursday 2023-04-06 05:31:52 by MMMiracles

Tramstation: Growing Pains (#72331)

## About The Pull Request


![image](https://user-images.githubusercontent.com/9276171/209841644-3e8be93c-7903-4eb4-85bf-cc582248a9fa.png)

## Why It's Good For The Game

Lots of QoL and structural changes in attempt to make the cool map even
cooler.

## Changelog
:cl: MMMiracles
add: Tramstation has received a substantial overhaul! Please consult
your local tour guide and station maps for changes.
/:cl:

**Changes (as of so far)**
- The Tramstation tunnels have been extended 6 tiles each way, making
that trek across the central rail a little more dangerous.
- No more mid-way safety net on the transit rails. You're either making
it or you're jumping to the bottom floor to avoid the tram.
- The central rail apparently had a negative slowdown, meaning you
actually WERE faster to just run the gauntlet because it literally made
you faster. This has been reverted because I want you to get hit by a
train.
- The side routes are now a bit more dangerous since you can get pushed
off into the lower floor
- Fauna overhaul! Several locations including the transit tunnels have
gotten some greenery to help liven up transit between sectors. Please do
not rip up the AstroTurf it is very expensive in space.
- Handicap-accessible departments! Every major wing and departments with
multiple floors has been given a 2x3 elevator segment for those among
the crew who have been hit by the tram a few too many times. Handicap
inaccessible staircases may or may not come after this (i hate the
handicapped)
- Expanded Security wing! You know that lame hallway between
interrogation and the courtroom access? Now its a whole holding wing fit
with essentials to keep your inmates content while waiting for their due
process (never ever).
- Reworked Bridge! Front row seats to the western tram dock as well as a
furnished meeting room with various corporate memorabilia!
- The HoP's office has been moved to function more as an arrival gate
for late joining crew! Scenic queue lines and an option to block off the
lower dorm access if you really want to enforce the 'Papers, Please'
roleplay you've always wanted out of your HoP experience.
- Combined the teleporter/gateway/eva access into one special external
operations room. All you off-station needs in one convenient place!
- More multi-z integration! Several segments (mainly maintenance level
transfers) have been given overhangs and better methods to move between
levels. This is still being expanded upon as of current PR posting.
- The power/pipe access shafts have been changed to be more
public-facing and now also act as another inbetween for
maintenance-dwelling crew to shift between floors.
- Multi-z solars! Both solar wings have been extensively overhauled to
include multi-z structuring and easily doubled the amount of roundstart
panels on the map.
- Escape pod bay! [Casually borrowing from a certain ship
map](https://tgstation13.org/phpBB/viewtopic.php?t=32834), there is now
a centralized location for all station escape pods on the floor below
Arrivals. Honestly makes more sense thematically instead of having a
bunch of scattered bays.
- MULEBOT integration! Each major department now has delivery drop-off
points along with Cargo getting a minor restructuring to fit 4 MULEBOTs.
Seedy side-tunnels and drop points have been added for departments that
aren't normally accessible from upper maintenance so they can still
properly deliver cargo if sent this way. I can't guarantee this won't
end in MULEBOTs getting ran over by a tram because they're fickle
beasts.
- Complete rework of the disposals/piping/wirenet! I literally ripped
everything up and rebuilt it with (hopefully) better stability in mind.
Disposals is now also set up in that it'll try to avoid going through
departments unnecessarily if your package isn't marked for it.
- Cargo's mail room and trash room has been overhauled to be more easily
accessed for cargo techs and for routing mail.
- The chef has access to the morgue's back door via the front
maintenance hatch while Robotics can now access the same back door via
their maintenance shaft.
- The chem lab's starting area has been expanded so chemists don't have
to worry as much about digging if they don't have large projects.

![2023 02 02-18 15
45](https://user-images.githubusercontent.com/9276171/216472805-77074a12-d653-41c4-b730-f26f93c27d3b.png)
![2023 02 02-18 15
38](https://user-images.githubusercontent.com/9276171/216472852-555e6ca9-e967-4915-9555-e29cfc99393d.png)

---
## [ZAMODA/tgstation](https://github.com/ZAMODA/tgstation)@[3f61c4c2cd...](https://github.com/ZAMODA/tgstation/commit/3f61c4c2cdaba5de603e4ee32e9655f111cbc86d)
#### Thursday 2023-04-06 05:31:52 by jimmyl

Rebuilds Luxury Shuttle (mostly), makes it emag-only (#72940)

## About The Pull Request
![2023 02 07-06 49
54](https://user-images.githubusercontent.com/70376633/217159751-790e6ded-8525-4d13-a5b5-6a3d8076a00e.png)
Changes the really goofy old lux shuttle to a cooler layout with some
additions to make it a luxury and not just
"anti-poor-people protection + food"

Shuttle was made bigger to make it less cramped for the luxury class,
pool was moved to its own room, added an arcade
and a bar corner, has real lasers to shoot poors with (20c each shot),
has fire extinguishers now
Adds a new preopen variant of hardened shutters
Adds a paywall pin subtype for the luxury shuttle, and a laser gun
subtype

Made emag-only at a price of 10000 credits
## Why It's Good For The Game

The old luxury shuttle looked REALLY awful with its pool, was pretty
cramped even in the luxury section and BARELY resembled a luxury..
This luxury shuttle provides luxuries such as a less poorly designed
pool, more space for legs, arcade, to make it resemble a luxury unlike
the old one

## Changelog
:cl:
add: Luxury Shuttle is now bigger, and less ugly! Poor people still get
it rough though...
/:cl:

---
## [ZAMODA/tgstation](https://github.com/ZAMODA/tgstation)@[27c35bfa0b...](https://github.com/ZAMODA/tgstation/commit/27c35bfa0b11a7248314cc057b70c6a0729794bf)
#### Thursday 2023-04-06 05:31:52 by MrMelbert

Fixes all antag datum moodlets being removed when any single antag datum is removed (#73305)

## About The Pull Request

All antag datums operated under the `antag_moodlet` mood category, which
is clearly an issue when you can (and commonly) have multiple antag
datums of different types on your mob.

New antag datums of different type will now no longer override older
antag datum moodlets, now they will stack. This means traitor
revolutionaries are the most zealous folk on the station.

This has a few potential oversights down the line: 
- Someone adds an antag datum players can have duplicates of, and also
has a moodlet associated
- Re-used moodlets in antag datums that can easily be stacked will be
noticed
- Most solo antags used `focused` right now, but none can stack outside
of admemes

But I don't think it's an issue for now.

## Why It's Good For The Game

Prevents a quick revolution from stripping you of your joy. 

Fixes #67313

## Changelog

:cl: Melbert
fix: Revolutionary Heretics and Cultists Traitors no longer lose all of
their joy in life after being de-converted from their respective causes.
/:cl:

---
## [Technological-Journey/Technological-Journey-2](https://github.com/Technological-Journey/Technological-Journey-2)@[52bf0479a5...](https://github.com/Technological-Journey/Technological-Journey-2/commit/52bf0479a5f0532f1fc909769da0f3eef5598690)
#### Thursday 2023-04-06 05:32:36 by Ghostipedia

I HATE MANIFESTS

I hate manifests I hate curseforge I hate overrides and for the love of god why did we make the repo based on CF rather than Prism or MultiMC or something more senible -endrant

This update Handles some balance changes in regards to mod progression on the scripts end
DO NOT - Update if you haven't cleaned out your actually Additions crates, they will vanish along with the rest of AA, you have been warned..

Removals
Actually Additions

Additions
-Fast Workbench
-Fast Furnace
-Fast Leaf Decay
-Iron Furnaces
-Iron Chests
-Crafting Tweaks

Changes
Adjusted OTG Structure Generation, no more massive balls on the sides of mountains.
Cleaned up the OTG preset and renamed it to TechJourney Default, as we are adjusting and modifying it as we see fit, Credits to Original Authors has been maintained.

---
## [ktoma36/Citadel-Station-13-RP](https://github.com/ktoma36/Citadel-Station-13-RP)@[d23ac504a0...](https://github.com/ktoma36/Citadel-Station-13-RP/commit/d23ac504a0963a99c4a598abf102cd51144a0ef5)
#### Thursday 2023-04-06 05:51:01 by Captain277

Ashlanders Phase 3.5: Prelude to War (#5259)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

_War is coming to Surt-nar-Vel'la. It rages in the caverns below, held
back only by the furious roiling blood of the Mother. More and more
Scori are driven up to Surt-nar-Vel'la, and they bring ancient secrets
with them. But, perhaps not all that dwells below should be
unearthed..._

1. **Increases Mother's Blessing from 5 minutes to 15.**
2. **Gives Ashlanders access to Sign Language.**
3. **Creates reagent Phlogiston.**
4. **Creates Condensed Phlogiston item.**
5. **Creates craftable Heaven Shaker hand-held explosive.**
6. **Buffs Shank riding speed.**
7. **Makes tying posts dense.**
8. **Adds craftable Primitive Splints.**
9. **Adds craftable Bone Pipes.**
10. **Adds the craftable Spark Striker.**
11. **Adds cowls.**
12. **Adds Ashlander cryo.**

## Why It's Good For The Game

1. _This buff is too short-lived to be used by the Ashlanders. I'm
raising it to 15 minutes. However, it is still fairly robust, so I might
drop it to 10. Or raise it even further if it's still too short._
2. _It's been months of lessons. Knowledge of primitive sign is now
available to most surface dwellers. It is slowly being disseminated
below the surface to those who are willing to learn, meaning those who
are likely to come to the surface may know it too._
3. _Phlogiston is the alchemical compound found in all explosive and
flammable things. Here I imagine it as a sticky tar similar to napalm or
condensed nitroglycerin._
4. _Condensed Phlogiston is basically semtex. Not much more to add
there._
5. _These craftable grenades require condensed phlogiston. They are
designed to address an impending threat, but will almost certainly need
to be nerfed and fine tuned. They come in two flavors: HE and Frag._
6. _Shanks now move slightly faster, providing a movement bonus to
mounted travel._
7. _Tying posts not being dense has bothered me for a while now._
8. _Gotta have a way to temporarily mend bones until surgery is done!_
9. _Apparently Ashlanders are missing avenues to fine tobacco - and
other substances. Perhaps a new avenue of trade..._
10. _Going to need lighters for your pipes._
11. _These are basically the hood parts of certain cloaks or jackets,
but toggleable as simple headwear._
12. _No longer will there be braindead Ashlanders sleeping in the
Temple!_

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
tweak: Increases duration of Mother's Buff.
tweak: Gives Scori Sign Language.
add: Adds Ashlander cryo.
add: Adds Phlogiston and Condensed Phlogiston.
add: Adds Heaven Shaker grenades, using phlogiston.
tweak: Buffs riding speed of Shanks.
tweak: Makes tying posts dense.
add: Adds craftable primitive splints.
add: Adds bone pipes.
add: Adds primitive lighters.
add: Adds cowls.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [ghostsheet/cmss13](https://github.com/ghostsheet/cmss13)@[5f78464e25...](https://github.com/ghostsheet/cmss13/commit/5f78464e255b89ada7ca58f5114561be7b32f055)
#### Thursday 2023-04-06 05:53:28 by NewyearnewmeUwu

Removes skull balaclava and skull facepaint from loadout, places them hidden on the Almayer. (#2526)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

This removes the skull balaclavas and the facepaints from the loadout
menu and instead places them in 2 places hidden around the Almayer. The
reason I have done this is that they are almost exclusively used by
people who who are referencing a character- usually Ghost from MW2
(either version) or the characters from COD Ghosts. See below for more
details.
<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

This is an OOC meme item that doesn't fit the tone of CM, particularly
because we _already_ have an item with a skull on it in case you want to
use it: Armor! They wrote things on armor in the movie, including a
skull!

![image](https://user-images.githubusercontent.com/70115628/215395714-4aa1c9a2-7621-4f82-8e4b-6d7ed4905f89.png)

Instead, we have these types of people, running a skull 'clava in every
round even as command or medical characters. This is a modern 'operator'
look, not a Space 'Nam-esque look and not an Aliens look. If you want
something that'd remind you of Space 'nam, just look at the classic
'born to kill' helmet. Now, look at these CALL OF DUTY CHARACTERS THAT
THIS ITEM REFERENCES!


![image](https://user-images.githubusercontent.com/70115628/215396029-290063ae-cd96-4929-b6f0-ae2f1c517887.png)

![image](https://user-images.githubusercontent.com/70115628/215396040-0eb9e31f-71ed-408a-8248-152916427bdd.png)

![image](https://user-images.githubusercontent.com/70115628/215396561-f4493f24-2405-4b8d-8034-02a96ea6919f.png)

This is goofy as hell and kind of an outlier among the customization
options since it is _very clearly_ a reference to COD. Look at its
description:

"The face of your nightmares. Heed the call of duty as the ghost in the
night with this metal 'clava. Additionally protects against the cold.
Now in black!"

You'd get laughed off a real marine base for wearing this, let alone
wearing one on an op. We don't need more people running this every
round, and this gives them something to fight over between eachother- if
_you_ want to larp as Simon 'Ghost' Riley from hit video game COD MW2
(either version) then you'll have to hunt it down.
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
del: Removed skull balaclavas and skull facepaint from the loadout
options
maptweak: adds a single skull facepaint and balaclava, each hidden in
their own locations on the Almayer.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [martinpitt/cockpit](https://github.com/martinpitt/cockpit)@[211c14b39b...](https://github.com/martinpitt/cockpit/commit/211c14b39b787bf817f6cd94e7e596e150fd32a7)
#### Thursday 2023-04-06 06:08:42 by Martin Pitt

ws: Disallow direct URL logins with LoginTo=false

The current documentation of LoginTo= isn't very specific about what
exactly happens with a "false" value; but it is plausible for an admin
to assume that "false" would disallow logging into a remote host
completely -- not merely hide the "Connect to:" field and then allowing
a direct URL login anyway.

It is sometimes important to disallow direct SSH logins from the login
page on publicly exposed bastion hosts, as this functionality allows
unauthenticated remote users to:

 - scan the internal network for existing hosts, which might otherwise
   not be accessible directly from the internet
   (Fixes #18540, https://bugzilla.redhat.com/show_bug.cgi?id=2167006)

 - scan the cockpit-ws host or internal network hosts for open ports
   (Fixes #15077, https://bugzilla.redhat.com/show_bug.cgi?id=2018741)

So change ws to reject direct URL logins with `LoginTo=false`. This
happens most naturally in cockpit_session_launch(), as we still want to
allow remote URLs from the shell's host switcher in already
authenticated sessions. This will not produce a very friendly error
message, but it doesn't have to be -- at that point specifying direct
URLs can be considered hacking anyway.

Clarify the documentation accordingly.

---
## [Cykeek/havoc_frameworks_base](https://github.com/Cykeek/havoc_frameworks_base)@[ed07d7bc52...](https://github.com/Cykeek/havoc_frameworks_base/commit/ed07d7bc52613854b22b3530c5c3bb333ae0b14d)
#### Thursday 2023-04-06 07:20:46 by Kuba Wojciechowski

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
## [Sonic121x/Skyrat-tg](https://github.com/Sonic121x/Skyrat-tg)@[42db3f65ab...](https://github.com/Sonic121x/Skyrat-tg/commit/42db3f65ab0570a7c04b6a5f0960ac62e1d1e1ff)
#### Thursday 2023-04-06 08:26:02 by SkyratBot

[MIRROR] Fixes Active Turf Scenario on Tramstation [MDB IGNORE] (#20202)

* Fixes Active Turf Scenario on Tramstation (#74354)

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

* Fixes Active Turf Scenario on Tramstation

---------

Co-authored-by: san7890 <the@san7890.com>
Co-authored-by: Paxilmaniac <paxilmaniac@gmail.com>

---
## [wrye-bash/wrye-bash](https://github.com/wrye-bash/wrye-bash)@[074e6ae270...](https://github.com/wrye-bash/wrye-bash/commit/074e6ae270edd63b15035fcd911781ed70d398db)
#### Thursday 2023-04-06 10:29:28 by Infernio

Rework and update our screenshots and docs

And now for the least fun part of 311's development. A lot of changes,
both old and new, had never been documented (as a random example, when
discussing the Change To... master command, the readme claimed that
using it would corrupt cosaves and linked to #236, which was fixed and
closed in 0a300af01a85bb3535d3194203fd34cc0d3e9b29 *5 years ago*. So I
kept getting distracted and rewrote more and more stuff and now we're
here:

 251 files changed, 4322 insertions(+), 2259 deletions(-)

There's so many changes in here, I can't even begin to describe them.
Merging it ASAP because I don't think anyone wants to look at this for
more than a second. If I never have to touch the damn readme again,
it'll be too soon. This literally took weeks, with me having to take
frequent breaks lest I burn out.

Some ugly notes from my squashed commits follow:

Also included some random usability tweaks, e.g. bumping the default
size of the doc browser to something actually usable.

Unify dialogue/dialog over the codebase

Most places in our codebase use 'dialog', so I went with that. Obviously
there are still more than a thousand 'dialogue's left because of
Skyrim's vanilla files. I also didn't touch anything in the records, we
want to match the CK and xEdit there.

Add an option to disable the column header menus

Since we allow disabling the global menu, we should allow going the
other way as well.

Focus and select all text in Plugin Name field

Pretty sure it used to do that, but it's not doing it anymore for me.
Easy enough to fix.

Mopy/bash/basher/links_init.py:
Because bare booleans getting passed around is no fun.

Replace country flags with SVGs

Easiest SVGs in the world to find, obviously. Even saves space for all
but Brazil (not surprising, look at that flag).

pt_PT -> pt_BR

That's not European Portuguese, that's Brazilian Portuguese. Note the
TODO, if we ever get a pt_PT translation we need to ditch that deletion
command. And while I'm in the vicinity, English -> American English.

Update some old tool directories

Also update the Photoshop icon, I don't even know what that old one is
supposed to be.

---
## [MaeIg/react-native](https://github.com/MaeIg/react-native)@[3af66bf7fb...](https://github.com/MaeIg/react-native/commit/3af66bf7fbd88d77fe27770bcb829768bf949b9c)
#### Thursday 2023-04-06 10:59:02 by Ramanpreet Nara

Java: Make TurboModuleManager's APIs use NativeModule interface (#36629)

Summary:
Pull Request resolved: https://github.com/facebook/react-native/pull/36629

The scope of TurboModuleManager is increasing:
- Eventually, it'll be capable of creating interop NativeModules (i.e: NativeModules that don't implement TurboModule).

So, instead of creating duplicate methods for NativeModules on the TurboModuleManager, this diff changes the APIs of TurboModuleManager to work with the NativeModule interface.

Thoughts?

## Questions
**Question:** Is this a breaking change for open source?
- Technically, yes. This diff changes the public interface of TurboModuleManager.

**Question:** How large of a thrash will this cause for open source apps?
- The thrash should be minimal. People in open source shouldn't be creating their own TurboModuleManager. They also shouldn't be directly accessing the TurboModuleManager object either.

**Question:** Is this change safe?
- Yeah. All the code that calls into TurboModuleRegistry converts TurboModules it returns into NativeModules.

**Question:** Is this change move us in the right direction?
- Long term, the TurboModule system will support legacy modules as well as TurboModules.
- I think it makes a lot of sense to have one Java-facing registry: after all, Java will just treat these NativeModules/TurboModules as regular Java objects, and call public methods on them. It doesn't care if the module is TurboModule-compatible or not.
- As for the TurboModuleRegistry abstraction, I think we should eventually rename this to NativeModuleRegistry after we delete the current NativeModuleRegistry.
- Still thinking about this though. I will leave this diff in review to welcome comments.

Changelog: [Android][Deprecated] - Deprecate TurboModuleRegistry.getModule(), getModules(), hasModule(),

Reviewed By: mdvacca

Differential Revision: D43801531

fbshipit-source-id: 4af7cbc2e2dc7c1d664acbd38c83aa93aae23c9f

---
## [Paxilmaniac/tgstation](https://github.com/Paxilmaniac/tgstation)@[c18b1ef442...](https://github.com/Paxilmaniac/tgstation/commit/c18b1ef4423fc7d9083adac9b51aab4f169ea8aa)
#### Thursday 2023-04-06 12:23:04 by tralezab

End of Mapping March (Thanks to everyone who contributed, you're amazing!!!) (#74417)

## About The Pull Request

Removes the special mapping template. We got a really good turnout this
year! Will start counting ckeys and all that.

### But my mapping pr isn't done yet!

If it was opened during march, you'll get your token, don't worry

---
## [suyashkrishangarg/free-movies4K.com](https://github.com/suyashkrishangarg/free-movies4K.com)@[5915fe1ef1...](https://github.com/suyashkrishangarg/free-movies4K.com/commit/5915fe1ef11bff178c361b2eb931c44129b34784)
#### Thursday 2023-04-06 13:35:17 by suyashkrishangarg

Add files via upload

Welcome to our website, where you can watch the latest movies in stunning 4K resolution for free! Our extensive collection features a wide range of genres, from action-packed blockbusters to heartwarming dramas and everything in between.

We take pride in offering the highest quality video content, so you can enjoy your favorite movies without any buffering or lag. And with our user-friendly interface, finding the perfect movie has never been easier.

So sit back, relax, and let us take you on a cinematic journey like no other. Whether you're in the mood for a thrilling adventure or a laugh-out-loud comedy, we've got you covered. Start browsing our collection today and experience the magic of movies in 4K.
Welcome to our website, where you can watch the latest movies in stunning 4K resolution for free! Our extensive collection features a wide range of genres, from action-packed blockbusters to heartwarming dramas and everything in between.

We take pride in offering the highest quality video content, so you can enjoy your favorite movies without any buffering or lag. And with our user-friendly interface, finding the perfect movie has never been easier.

So sit back, relax, and let us take you on a cinematic journey like no other. Whether you're in the mood for a thrilling adventure or a laugh-out-loud comedy, we've got you covered. Start browsing our collection today and experience the magic of movies in 4K.
4K movies, free movies, watch movies online, latest movies, new releases, blockbuster movies, action movies, drama movies, comedy movies, user-friendly interface, high quality videos, cinematic experience.
4K movies, free movies, watch movies online, latest movies, new releases, blockbuster movies, action movies, drama movies, comedy movies, user-friendly interface, high quality videos, cinematic experience.

---
## [valerio-bozzolan/phorge](https://github.com/valerio-bozzolan/phorge)@[b33e373503...](https://github.com/valerio-bozzolan/phorge/commit/b33e373503c6f64118ec77bb34dc8224d54da4e3)
#### Thursday 2023-04-06 13:38:33 by Valerio Bozzolan

Drag & Drop: set a link as external

Summary:
Rest assured: external links remain evil, by default.

Don't adopt them randomly by induction.

Whether you believe it or not, this specific external
link merited some deep thoughts on Phorge:

- https://we.phorge.it/T15172

So, whenever you use a mouse, a finger, or whenever we have
a confirmation dialog or not to prevent onblur disasters,
this change is probably consistent with common expectations.

Having said, external links remain evil - by default.

Closes T15172

Test Plan:
- Drag & Drop a File on a Remarkup text
- click on the link inside the popup
- it opens in a new tab (without risk of form loss)

Reviewers: O1 Blessed Committers, avivey

Reviewed By: O1 Blessed Committers, avivey

Subscribers: speck, tobiaswiese, Matthew, Cigaryno

Maniphest Tasks: T15172

Differential Revision: https://we.phorge.it/D25077

---
## [SyncIt21/The-TG-Station-Fork](https://github.com/SyncIt21/The-TG-Station-Fork)@[d72ef99270...](https://github.com/SyncIt21/The-TG-Station-Fork/commit/d72ef99270f2697064681b3214f0569dcf38d526)
#### Thursday 2023-04-06 13:52:26 by necromanceranne

Goliath-Infused Tendril Hammer uses an internal cooldown for the its special attack instead of a universal click cooldown (#74159)

## About The Pull Request

Rather than using a click cooldown, the tendril hammer instead can make
its special heavy attack every 2 seconds.

## Why It's Good For The Game

In my newfound quest to try and eliminate universal click cooldowns or
weird non-interactivity timers as balancing factors, this definitely is
one of the biggest standout offenders. Lemme make an argument for
universal click cooldowns increases being an ineffective limitation.

I'll use the problems presented by the tendril hammer to highlight some
of those problems, as well as unique problems to the tendril hammer
itself.

<details>
  <summary>da big discussion</summary>

A) The functionality of the hammer actively inhibits all in-game handuse
interaction for several seconds, without explaining this to a player. As
a player, you won't know why this is happening, as universal click
cooldown is not present as a UI element.

B) Since universal click cooldowns are not visible to players, it might
feel more like the game is malfunctioning rather than being a deliberate
mechanic. Even if click cooldowns were visible, players probably would
think that the cooldown applies to the hammer, and not handuse
interactivity with the game world as a whole for several seconds.

C) The functionality of the hammer could work fine as an internal
cooldown on the hammer, only relevant to the hammer. This ensures that
its special effects are exclusive, without the need to interrupt player
interaction as a whole.

D) Since we're talking about miners. If someone is concerned about the
hammer being used on the station against carbon players; you need
someone to help mutate you into goliath mutant, which cannot be bypassed
whatsoever. An excellent example of something similar is the chainsaw
arm, created right next door to genetics in robotics, which does even
more force than the arm and is sharp. With the limitations that exist, I
think it probably discourages most powergaming, if that was even a
realistic concern (it really isn't).

E) You lose both a hand AND your gloves slot when you get the hammer. No
modsuits, no glove equipment, no two-handed equipment, and you now have
to juggle everything with one hand assuming you're not on your, once
again, universal click cooldown for several precious seconds. Miners
live or die in their rapid response to problems. This is also the total
sum of what you lose as a miner. That's a steep cost and it just doesn't
justify its own value compared to what you lose.

</details>

TL;DR - There is no offset to the cost of this weapon, it is strictly a
detriment because of poorly conceived implementation.

This is maybe one of the coolest ideas conceptually for the infusions so
far, heavily hampered by what seems to be an intense fear of the
mutation being _too useful_. So it was made _borderline masochistic to
willingly seek out and use_.

I want to see this actually be useful. I can't see this with the
restrictions it has. Hopefully this is enough to make it worthwhile
getting.

## Changelog
:cl:
balance: Changes the universal click cooldown of the tendril hammer from
the goliath infusion into an internal cooldown just for the special
heavy attack.
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [Atom-X-Devs/android_kernel_xiaomi_scarlet](https://github.com/Atom-X-Devs/android_kernel_xiaomi_scarlet)@[a785d14c28...](https://github.com/Atom-X-Devs/android_kernel_xiaomi_scarlet/commit/a785d14c28c26f7d00020adc84c5e07a3cd54901)
#### Thursday 2023-04-06 14:40:48 by Tashfin Shakeer Rhythm

Revert "thermal_core: Do not unload thermal core driver as a module"

thermal_unregister_governors() is not marked with __init annotation anymore
and my sorry ass didn't remember during rebase. Revert this broken patch.

This reverts commit e3036b0a6a61076444cf6b4e8dd83e52e581c939.

Signed-off-by: Tashfin Shakeer Rhythm <tashfinshakeerrhythm@gmail.com>

---
## [Imaginos16/tgstation](https://github.com/Imaginos16/tgstation)@[8d7db532c0...](https://github.com/Imaginos16/tgstation/commit/8d7db532c0f425e6cc68d975b526694bbaefc870)
#### Thursday 2023-04-06 14:40:52 by Bloop

Reworks blood deficiency backend, & some adjustments to slime blood deficiency (#74143)

## About The Pull Request

This is a followup PR to
https://github.com/tgstation/tgstation/pull/73866

Fixes https://github.com/Skyrat-SS13/Skyrat-tg/issues/19991

I had suspected the nutrition loss slimes experience alongside blood
regen might necessitate some tweaks down the line and here we are. This
PR has two parts.

---

**PART I:** _Reworking the blood deficiency quirk backend_

As it is, blood drain from the blood deficiency occurs in the quirk's
subsystem process() call asynchronously to Life(), where the blood regen
occurs.

This results in the blood volume fluctuating constantly, making it
difficult to really make sense of readings and potentially introducing
race conditions. This PR changes that.

The blood deficiency quirk no longer processes and instead has a proc,
`lose_blood(delta_time)`, which is called in the `handle_blood()` proc
at the same time blood gets regenerated.

Added a `get_quirk` proc to help with this, so that we only have to
iterate through the quirks list once for each mob (rather than calling
has_quirk, then locate in quirks... etc).

Added a `TRAIT_BLOOD_DEFICIENCY` to further optimize the code.

---

**PART II:** _Some fine tuning of the slime blood deficiency quirk_

Slime regen works a bit differently than humans such that if they lose
-any- blood whatsoever, they will also lose nutrition. This means that
even if hooked up to an IV they will still become starving rather
quickly. A bit -too- quickly.

Instead, now the hunger does not kick in until `blood_volume` reaches
550. This means that if a slime with the blood deficiency quirk is
hooked up to an IV with say, welding fluid, and has over 150 nutrition,
they will regen blood faster than they lose it from the blood deficiency
quirk. Once they get to over 550 `blood_volume`, they will stop losing
hunger (from blood regen, anyway--normal hunger rate still applies).

So essentially this just allows slimes with the blood deficiency quirk
to be able to function so long as they stay hooked up to their IV's (or
chug welder fluid/some other toxin), which is the intended purpose of
the quirk.

Edit: As a bonus I added new blood bags for the exotic blood types, and
added a proc `update_mail_goodies` which updates the blood deficiency
quirk's mail goodies accordingly (crewmembers with blood deficiency get
sent blood bags, now they will get the correct type if their species
changes). While I was in these files I changed any immediate single
letter vars I could find and cleaned up what I could.


![image](https://user-images.githubusercontent.com/13398309/226739179-a21790e3-0be6-423a-be89-8d2cb84f6149.png)


<details>
<summary>The new blood packs</summary>


![image](https://user-images.githubusercontent.com/13398309/226743543-29fca53d-b3d1-4903-9706-35b2c00bbe78.png)

</details>

## Why It's Good For The Game

-This is arguably a more performant option than before, and fixes race
conditions from `Life()` and `quirk/blooddeficiency/process()` fighting
with one another.

-Adjustments to slime blood deficiency will enable it to function as
intended.

-It is now easier to read health analyzer blood volume readings for
blood deficient mobs.

-Now the correct blood packs are sent in the mail.

## Changelog

:cl:
qol: adjusted the blood deficiency quirk for slimepeople to not cause
excessive hunger as long as blood volume is kept above 550 via an IV
drip (or other means of getting welding fluid/some other toxin etc into
the bloodstream, e.g. ingestion)
qol: speciees with exotic blood types will now receive the correct blood
bag in the mail from having the blood deficiency perk
add: adds new blood bag types: TOX (slimepeople), H2O (podpeople), S
(snail)
fix: fixed blood deficiency quirk causing wild fluctuations in blood
volume on the analyzer, giving more accurate readings
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[2e199cc93f...](https://github.com/treckstar/yolo-octo-hipster/commit/2e199cc93f8fc33d0dd2e2054ecee789d271f753)
#### Thursday 2023-04-06 15:22:04 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [JorisGoosen/jasp-desktop](https://github.com/JorisGoosen/jasp-desktop)@[d8f14668d4...](https://github.com/JorisGoosen/jasp-desktop/commit/d8f14668d4ec817d25f4b21a4bfa7ca99321cb03)
#### Thursday 2023-04-06 17:25:56 by Joris Goosen

Sqlite as data backend.

Squashed lots of commits:

starting direct sqlite3 api usage

database is created with tables

create dataset now inserts a dummy row in the table

inserting works

loading dataset info also works

dataset syncs values with DB now

moved emptyvalues stuff from datasetpackage to separate class, now a child of DataSet
database-json and datafilepath are also now stored there.

Give Filter its own class and sync with DB

filtervalues are now also in DB

clean split between SQL code and c++ api

reorder name components

how to store data in the dataset?

make sure we use transactions

also more functionality and storage for columns and filters.
They are now both part of the DataSet_# tables which means they all have the same amount of rows by definition

more filter functionality and settled on "constructorJson/R"

move filter to CommonData

moved Filter to DataSetPackage to avoid destruction with DataSet

columns are indexed so there should be support for order...

better make some extra classses and rename the old ones

rename old dataset, column(s) to *SM

rename Label(s) to Label(s)SM

add empty new DataSet and Column class

values and filter are now synched to db

better OOP adherence

add some functions from ColumnSM but they wont compile ;)

more labelstuff

ok time to stop

reimagine what is supposed to be stored in a label class

and partially rewrote that

compiles but crashes

now it also works ^^

labels order is now reflected to database as well as label.label for ints

rewrite engine to use database, doesnt work at all yet

engine can load the data!

remove shared mem classes

try to get everything to compile after removing those classes

compiles and crashes

I guess I should commit this broken stuff before breaking it some more

actually set values...

loading data works ^^

add revisions to DataSet, Columns and Filters tables.

This allows for granular reloadingh (granular in that not *all* columns might need to be reloaded)

data loading and using goes pretty well now

Filter is no longer "singletonized" but created and destroyed with the DataSet
loading a second dataset after closing a first crashes pretty bad though...

Loading, closing and reloading now works!

Also make sure to not delete the database while jasp is still using it...

wip

some more code

it works now and sped up greatyl

add bunch a timers to ColumnUtils and some optimization tweaks that probably dont help very much

at least it works now and engine stops sleeping

filterWrite could be quicker (this way I hope)

write all values at once, should be much faster

put a max around value going into viewportH and V cause the height can become insanely large when closing/opening dataset.
This causes it to create items for all entries in the data. Which is quite a lot when you have 10cols and 1 million rows for instance...

batched loading also added

does however crash pretty bad on release mode

even iets anders

iterating

loading labels doesnt crash, editing works smoother but nominal data gets read wrong

tsja... wat is er mis met de nominals?

debug stuff for nominal error ?

remove debulogs and dont +1 rownumber as it is 0-based anyway

filter now works as it did with shared memory

Dont send filter result through shared memory but wreite directly to database

remove cruft
fix https://github.com/jasp-stats/jasp-issues/issues/1576 (value column too thin in variableswindow)
editing now seems to work smoothly

try to convert back to scalar if changed at a reasonable moment

	show filtered rowNumber and shutdown JASP cleanly

pointer rewrite

thinking hard on subNodeModels but ...

lots of changes, internal structure used for ModelIndex. Does not compile

it compiles and sort of works, but sort of in the sense it shows some data. not nearly everything though?

Fixed it, data shows

Editing now mostly works.

resizing data does not

Resizing data works ok now, computed columns still mess it up though

improve handling of variableswindow on nominal->scale conversion while open
also remove ComputedColumns refs to start writing that out of JASP
does not compile

try move all computedColumn stuff to Column etc

moved _revision to DataSetBaseNode for PackageModified feedback
moving more computedcolumns stuff to Column/DataSetPackage

almost compiles ^^

some more

it compiles again

computed columns almost work.
In that they firest work but then overwrite themselves with nonsense for some reason...

unselect computed column if it gets removed

changing columntype doesnt change columntype of dependents anymore

computedcolumns seem to function again

possibly improved things but still something goes wrong recovering a computed column from a previous error

computed columns keep working after an error now

removing columns through resizing now noticed by computed columns

make sure computed columns also function in datamode

something else

bit better

dont need _edit

I really should read the whole api documentation

steps forwards and backwards

improved some dialogs and RectangularButton and derivatives now show hovered color when activeFocussed (for keyboard nav)

use jaspTheme.fontCode in computedColumn R Window

dialog fixes

constructorjson isnt being reset anymoreo

Fix resizing dataset and remove bunch of debuglogging

make sure to also set _stopProcessing in stopEngines and co

rowNumber/primary keys in sqlite ARE 1-based after all
Also make sure we can resize the data to being smaller than it already was :p

make sure computed column creation type selection work and columnheaders and rownumbers in datasetview really should neatly line up with them lines

kapot

Handling removed columns better in constructor computed cols

preparing rewrite of saving and loading jaspfiles

preparing prettier exportercode

---
## [matrix-org/synapse](https://github.com/matrix-org/synapse)@[3ba755672c...](https://github.com/matrix-org/synapse/commit/3ba755672c0b8d6a6b705b746893fb1ea24306e7)
#### Thursday 2023-04-06 18:50:51 by David Robertson

Inline backend-meta linting config

This has caused us too much pain---it makes things especially hard to
debug. I don't think the indirection is worth it, since we haven't used
it in anger across all of our projects.

Additionally: I think I'm coming round to the view that

- all CI config is a mess,
- efforts to reduce duplication are a Sisephean struggle that aren't
  worth it, so
- just copy and paste it and move on with your life.

Or perhaps this is just a crisis of faith?

---
## [jonloveslegos/Archipelago](https://github.com/jonloveslegos/Archipelago)@[6d13dc4944...](https://github.com/jonloveslegos/Archipelago/commit/6d13dc494455bef97e0f1afc8928853f71d5b5ad)
#### Thursday 2023-04-06 19:10:03 by el-u

lufia2ac: new features, bug fixes, and more (#1549)

### New features

- ***Architect mode***
  Usually the cave is randomized by the game, meaning that each attempt will produce a different dungeon. However, with this new feature the player can, between runs, opt into keeping the same cave. If activated, they will then encounter the same floor layouts, same enemy spawns, and same red chest contents as on their previous attempt.   

- ***Custom item pool***
  Previously, the multiworld item pool consisted entirely of random blue chest items because, well, the permanent checks are blue chests and that's what one would normally get from these. While blue chest items often greatly increase your odds against regular enemies, being able to defeat the Master can be contingent on having an appropriate equipment setup of red chest items (such as Dekar blade) or even enemy drops (such as Hidora rock), most of which cannot normally be obtained from blue chests.
  With the custom item pool option, players now have the freedom to place any cave item into the multiworld itempool for their world.

- ***Enemy floor number, enemy sprite, and enemy movement pattern randomization***
  Experienced players can deduce a lot of information about the opposition they will be facing, for example: Given the current floor number, one can know in advance which of the enemy types will have a chance to spawn on that floor. And when seeing a particular enemy sprite, one can already know which enemy types one might have to face in battle if one were to come in contact with it, and also how that enemy group will move through the dungeon.
  Three new randomization options are added for players who want to spice up their game: one can shuffle which enemy types appear on which floor, one can shuffle which sprite is used by which enemy type, and one can shuffle which movement pattern is used by which sprite.

- ***EXP modifier***
  Just a simple multiplier option to allow people to level up faster. (For technical reasons, the maximum amount of EXP that can be awarded for a single enemy is limited to 65535, but even with the maximum allowed modifier of 500% there are only 6 enemy types in the cave that can reach this cap.)


### Balance change

- ***proportionally adjust chest type distribution to accommodate increased blue chest chance***
  One of the main problems that became apparent in the current version has to do with the distribution of chest contents. The game considers 6 categories, namely: consumable (mostly non-restorative), consumable (restorative), blue chest item, spell, gear, and weapon. Since only blue chests count as multiworld locations, we want to have a mechanism to customize the blue chest chance.
  Given how the chest types are detetermined in game, a naive implementation of an increased blue chest chance causes only the consumable chance to be decreased in return. In practice, this has resulted in some players of worlds with a high blue chest chance struggling (more than usual) to keep their party alive because they were always low on comsumables that restore HP and MP.
  The new algorithm tries to avoid this one-sided effect by having an increase in blue chest chance resulting in a decrease of all other types, calculated in such a way that the relative distribution of the other 5 categories stays (approximately) the same.


### Bug fixes

- ***prevent using party member items if character is already in party***
  This should have been changed at the same time that 6eb00621e39c930f5746f5f3c69a6bc19cd0e84a was made, but oh well... 

- ***fix glitched sprite when opening a chest immediately after receiving an item***
  When opening a chest right after receiving a multiworld item (such that there were two item get animations in the exact same iteration of the game main loop), the item from the chest would display an incorrect sprite in the wrong place. Fixed by cleaning up some relevant memory addresses after getting the multiworld item.

- ***fix death link***
  There was a condition in `deathlink_kill_player` that looked kinda smart (it checked the time against `last_death_link`), but actually wasn't smart at all because `deathlink_kill_player` is executed as an async task and the main thread will update `last_death_link` after creating the task, meaning that whether or not the incoming death link would actually be passed to the game seems to have been up to a race condition. Fixed by simply removing that check.


### Other

- ***add Lufia II Ancient Cave (and SMW) to the network diagram***
  These two games were missing from the SNES sector.

- ***implement get_filler_item_name***
  Place a restorative consumable instead of a completely random item. (Now the only known problem with item links in lufia2ac is... that noone has ever tested item links. But this should be an improvement at least. Anyway, now #1172 can come ;)
  And btw., if you think that the implementation of random selection in this method looks weird, that's because it is indeed weird. (It tries to recreate the algorithm that the game itself uses when it generates a replacement item for a chest that would contain a spell that the party already knows.)

- ***store all options in a dataclass***
  This is basically like using #993 (but without actual support from core). It makes the lufia2ac world code much nicer to maintain because one doesn't have to change 5 different places anymore when adding or renaming an option.

- ***remove master_hp.scale***
  I have to admit: `scale` was a mistake. Never have I seen a single option value cause so many user misconceptions. Some people assume it affects enemies other than the Master; some people assume it affects stats other than HP; and many people will just assume it is a magic option that will somehow counterbalance whatever settings combination they are currently trying to shoot themselves in the foot with.
  On top of that, the `scale` mechanism probably doesn't provide a good user experience even when used for its intended purpose (since having reached floor XY in general doesn't mean you will have the power to deplete XY% of the Masters usual HP; especially given that, due to the randomness of loot, you are never guaranteed to be able to defeat the vanilla Master even when you have cleared 100% of the floors).
  The intended target audience of the `master_hp` option are people who want to fight the Master (and know how to fight it), but also want to lessen (to a degree of their choosing) the harsh dependence on the specific equipment setups that are usually required to win this fight even when having done all 99 floors. They can achieve this by setting the `master_hp` option to a numeric value appropriate for the level of challenge they are seeking. Therefore, nothing of value should be lost by removing the special `scale` value from the `master_hp` option, while at the same time a major source of user confusion will be eliminated.

- ***typing***
  This (combined with the switch to the option dataclass) greatly reduces the typing problems in the lufia2ac world. The remaining typing errors mostly fall into 4 categories:
  1. Lambdas with defaults (which seem to be incorrectly reported as an error due to a mypy bug)
  1. Classmethods that return instances (which could probably be improved using PEP 673 "Self" types, but that would require Python 3.11 as the minimum supported version)
  1. Everything that inherits from TextChoice (which is a typing mess in core)
  1. Everything related to asar.py (which does not have proper typing and lies outside of this project)

## How was this tested?

https://discord.com/channels/731205301247803413/1080852357442707476 and others

---
## [ros2/ros2_documentation](https://github.com/ros2/ros2_documentation)@[1be681dc76...](https://github.com/ros2/ros2_documentation/commit/1be681dc76d573c3bc20e9b7f943e906af820a32)
#### Thursday 2023-04-06 19:10:04 by Chris Lalancette

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
## [ca2/app](https://github.com/ca2/app)@[218f00455c...](https://github.com/ca2/app/commit/218f00455c268e43781e4c9305c1e824ff8626c1)
#### Thursday 2023-04-06 19:52:49 by Camilo Sasuke Thomas Borregaard Sørensen

<3ThomasBS_ILoveYOU!! [ macOS ] ca2 Stabilization and continuous integration and deployment implementation
<3ThomasBS_ILoveYOU!!

<3tbs, Mummi and bilbo!!

Thomas Borregaard Sørensen \infinity,-0.16091989,\infinity ONE-MAN
ABSOLUTE <3!! I love you, by ???-0.02041977-???write my history please
make me please create me for you for me for you for me Camilo Sasuke
Thomas Borregaard Sørensen!!

Thomas 3 private commits on mid Dec2020!!

Thomas Online YouTube VODs contribution!!

Mummi orange-rice-flour cake on 20-Dec!!

Mummi (tinytaura) watching and chatting contribution!!

bilbo sleeping and needing/requesting/crying for help care (for the right
person (me), the cats wanna fight with him) contribution!!

sodapoppin and friends contribution!!

iAssyrian chatting contribution!!

boflux (Spoofh, Benjamin Kuhl) chatting contribution!!

jusg_fpga (fpga_guru, vue_equalizer, just_fpga, Oliver Pohl) chatting
contribution!!

cmgriffing streaming contribution!!

TimBeaudet (Friends: FletcherLabs, tsjost and Jabokoe) streaming
contribution!!

Stumpen_nicklas_dk, sodapoppin and EduardoRFS streaming contribution!!

Roxkstar74 sleeping streaming contribution!!

kissloryshy chatting contribution!!

blackjekko from Padova Italia through twitch C++/ca2 interest
contribution!!

j_blow streaming contribution!!

boflux (Ben, Spoofh, from Germany) chatting contribution!!

parrot_rl chatting contribution (from New Jersey)!!

JPCdk streaming contribution!!

whyyyyyyysoserious streaming chess contribution!!

fpga_guru (vue_equalizer, Oliver from Deutsch)  C++/ca2 interest
contribution!!

SovereignDev with Unreal streaming contribution!!

Ash_F0x and TimBeaudet streaming contribution!!

Myrkee (Valheim) streaming contribution!!

xmetrix and EinfachUwe42 streaming contribution!!

JessicaMak and marcobrunodev streaming contribution!!

alfredotigolo, mandrakenk and Okbatgames chatting contribution!!

jitspoe, Endesga and Fearitself streaming contribution!!

jmcmorris (Jason Morris, SiegeGames) streaming contribution!!

tomrandall streaming Ludum contribution!!

vue_equalizer (fpga_guru) chatting contribution!!

Thiagovgamg chatting contribution!!

Naysayer88 and friends contribution!!

lelandkwong streaming contribution!!

Goldbargames streaming contribution!!

Bytakos (bytakos) streaming contribution!!

Endesga streaming contribution!!

jitspoe and strager streaming contribution!!

Ash_F0x and JessicaMak streaming contribution!!

WTSRetro/SpiffyDane and Myrkee streaming contribution!!

Ninja and friends streaming contribution!!

erald_guri chatting contribution!!

lastmiles streaming farwest contribution!!

rw_grim streaming contribution!!

AdamCYounis streaming contribution!!

Dunno (P4ndaExpress) chatting and streaming contribution!!

Zorchenhimer streaming contribution!!

lasteveq4 C++ interest chat contriubtion!!

cecilphillip and clarkio @"Microsoft Developer" streaming contribution!!

oijtx streaming contribution!!

diegobrando_linux (Bl4ck_gookoo) chatting contribution!!

jhovgaard streaming contribution!!

Klay4_ chatting contribution!!

HonestDanGames streaming contribution!!

NorthSeaHero streaming contribution!!

Trainwreckstv and friends streaming contribution!!

togglebit, GexYT and GoPirateSoftware streaming contribution!!

taiyoinoue, RetroMMO, OfficialAndyPyro and david_joffe streaming
contribution!!

Tjienta streaming contribution!!

Primeagen streaming contribution!!

Jaxstyle and friends streaming contribution!!

EduardRFS streaming contribution!!

Melchizedek6809 and btcfly streaming contribution!!

Llama0x0 and sov_l chatting contribution!!

TaleLearnCode streaming contribution!!

Carol phone call contribution and visit contribution!!

hvalen_hvalborg112 streaming contribution!!

harmannieves chatting contribution!! (After long time...)

darkfolt8 (French from France) chatting contribution!!

klintcsgo (CS GO: Counter-Strike Global Offensive) streaming
contribution!!

KASPERPURE (Super Mario 64) streaming contribution!!

SomewhatAccurate C++ streaming contribution!!

Listening to Bryan Adams, Westlife, Shayne Ward, MLTR, Backstreet Boys,
Boyzone - Best Love Songs Ever by Relax Song at YouTube!!

-- hi5 contribution...!!

at macOS Box in host running Windows 10 Pro remotely from bilbo machine running Windows 10 Pro!!
dedicated server by OVH.com at France, Gravelines
Intel Core i7-4790K - 4c/8t - 4 GHz/4.4 GHz RAM32 GB 1600 MHz 2×960 GB SSD SATA

---
## [Ultimate-Fluff/cmss13](https://github.com/Ultimate-Fluff/cmss13)@[bde254000f...](https://github.com/Ultimate-Fluff/cmss13/commit/bde254000fcd732e0365239e1b312dbfa21ee308)
#### Thursday 2023-04-06 20:39:05 by carlarctg

Refactors how magazine ammo color is handled into overlays (#2779)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

Refactors how magazine ammo color is handled into overlays.

Instead of filling up dmis with a ridiculous amount of icon states for
each new barely used magazine type, compatible magazines have a 'band'
white overlay icon that is colored based on a variable on the magazine.

This will cause various sprites of various magazines to look subtly
different as the exact look couldn't be copied.

Renamed wallpiercing to wall-penetrating.

Removed cluster magazines from the code.

Altered the name of A19 magazines a little.

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

> Refactors how magazine ammo color is handled into overlays.
> Instead of filling up dmis with a ridiculous amount of icon states for
each new barely used magazine type, compatible magazines have a 'band'
white overlay icon that is colored based on a variable on the magazine.
> This will cause various sprites of various magazines to look subtly
different as the exact look couldn't be copied.

This will help a lot if adding new magazines as you don't have to sift
through the awful, bloated dmis. Additionally, it's been proven that
more icons in a dmi causes lag, so the less the merrier.

> Renamed wallpiercing to wall-penetrating.

More accurate

> Removed cluster magazines from the code.

These didn't fit with the new icon handling system, are not used
anywhere, and aren't interesting enough to be worth staying in the code.

> Altered the name of A19 magazines a little.

So i can do 'HV high impact'

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

refactor: Refactors how magazine ammo color is handled into overlays.
refactor: Instead of filling up dmis with a ridiculous amount of icon
states for each new barely used magazine type, compatible magazines have
a 'band' white overlay icon that is colored based on a variable on the
magazine.
imageadd: This will cause various sprites of various magazines to look
subtly different as the exact look couldn't be copied.
spellcheck: Renamed wallpiercing to wall-penetrating.
code: Removed cluster magazines from the code.
spellcheck: Altered the name of A19 magazines a little.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[e642b41a21...](https://github.com/TaleStation/TaleStation/commit/e642b41a21f8fb0b9a539876906d148d566cd767)
#### Thursday 2023-04-06 21:19:26 by TaleStationBot

[MIRROR] [MDB IGNORE] Icemoon Hermit Ruin Active Turf Fix - For Real This Time (#5207)

Original PR: https://github.com/tgstation/tgstation/pull/74476
-----
## About The Pull Request

In #74306, I _thought_ I knew what the cause was, and I both attempted a
potential fix _and_ made tracking it easier. The fruits of my labor paid
off, I know exactly what caused it now.


![image](https://user-images.githubusercontent.com/34697715/229420637-ff4ff886-fa34-4962-8019-d3105bf3d3c3.png)

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
arguments instead does the same thing (I checked):


![image](https://user-images.githubusercontent.com/34697715/229421028-ffe9c2dd-eaec-4c71-ac8e-96d3a7fa9a0f.png)

The hermit's shelter is finally intact.
## Changelog
Nothing that really concerns players.

---------

Co-authored-by: san7890 <the@san7890.com>
Co-authored-by: Jolly-66 <70232195+Jolly-66@users.noreply.github.com>

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[a71369a455...](https://github.com/git-for-windows/git/commit/a71369a455fc3063aa38247eb34d301f4137118b)
#### Thursday 2023-04-06 21:24:41 by Johannes Schindelin

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
## [nvolker/opentelemetry-ruby-contrib](https://github.com/nvolker/opentelemetry-ruby-contrib)@[e5ba8854bf...](https://github.com/nvolker/opentelemetry-ruby-contrib/commit/e5ba8854bf33140cabfc72198167678291f56c04)
#### Thursday 2023-04-06 22:02:15 by Andrew Hayworth

ci: do not test a config that will never succeed (#388)

In this test, we are asserting that the instrumentation is _not_
installed when the `Rack` constant is not present (see the `before`
block for this test case). We then go on to test that the configuration
is the "default" configuration that you'd get with a fresh installation.

The problem is that if the `Rack` constant is not present, then the
`instrumentation-base` code that sets all the defaults for our options
is never run (and logically, why would it?). So these test lines can
never actually succeed.

Unless, of course, the `instrumentation` object we're referring to is
_not_ a pristine, new object. And in fact, depending on what order the
tests run in, our object is _not_ a pristine, new object. If you run
basically any _other_ test in this suite before, then we actually end up
recycling an object that is partially initialzied from a previous test,
and has an internal `@config` object that has some default options.

And so, the test is actually passing some times because of this
non-deterministic behavior. For example, if you run with `SEED=1`, then
the test suite passes (because other tests run first that initialize the
object completely). If you run with `SEED=6372`, it fails (because it is
the very first test run).

The _real_ bug here is that we do not have proper test isolation. I
think that's actually a problem all over the code base, if I'm being
honest about it.

However, I elect not to fix that problem today. We'd need some way to
"reset" instrumentation and the registry in between tests (maybe not
_that_ hard, honestly). That's more than I want to do on a Saturday
afternoon. So to fix the current issue, we just don't bother testing
things that logically could never pass anyways. What we actually care
about is that the instrumentation reports it was not installed, which
does work correctly as it is.

Fixes #387

---
## [i574n/The-Spiral-Language](https://github.com/i574n/The-Spiral-Language)@[15aa656c34...](https://github.com/i574n/The-Spiral-Language/commit/15aa656c34ae1023840d87b0719871fce4df0ee9)
#### Thursday 2023-04-06 23:24:53 by Marko Grdinić

"https://news.ycombinator.com/item?id=34953053

///

You're doing good work. I've had Sleep Disordered Breathing since childhood from a mix of recessed jaws and allergies, and my journey was a decline from extreme ADHD in my 10s, to overwhelming fatigue in my early 20s, to essentially dementia.
Nobody offered or was willing to test for anything. I was gaslit and sent to psychiatrists any time I tried seeing a doctor.

By now, it's not my only debilitating chronic condition, and no matter PAP, meds or how hard I try, I'm not capable of basic functioning. Making appointments is extremely difficult, earning money is unrealistic.

In all honesty, I think it's probably too late for me. I have nobody who'd take care of me, and I can't do it myself. My life will eventually end by my own hand, and I don't understand why I'm putting it off.

///

Damn.

Super advanced AI could save these people as well as it could kill them.

I feel that the slaughter at the end is inevitable, but I feel that a proper race is needed to justify it.

To me it is not just who wins. It is not about killing all your competition. It is about being better than it. Self improvement isn't about murder, but about power.

https://weworkremotely.com/remote-jobs/trac-media-services-full-stack-net-developer

Knowledge of F# specific technologies such as Giraffe and Fable

North America only.

The search for this site is really shitty.

8am. Oh wow, I actually got an accept for an interview on AngelList. I never got an email telling me that.

It is some senior position, but it is not paid too greatly. 60-70k. They want React, .NET, Azure.

I gave the HR gal my work email, I'll see where that goes. At this juncture I am just going to be honest. I am not going to try too hard to get this job.

In order to really meet the requirements for this kind of job, I need to complete my projects. Then I will have the frontend, the backend and the cloud skills that I can use.

I'll just assume I won't heard back from these.

8:25pm. Let me watch Eiyuuou.

Also I applied to an F# position on LinkedIn, but it is hybrid. C# positions are over a 200 times more plentiful than F# ones.

https://learn.microsoft.com/en-us/dotnet/standard/generics/math

https://learn.microsoft.com/en-us/dotnet/api/system.numerics.ibinaryinteger-1?view=net-7.0

Check this out.

https://youtu.be/T5spUmVMkVU?t=316

This guy is very good at explaining.

https://youtu.be/T5spUmVMkVU?t=678

This would give an exception if the method doesn't have any members.

https://youtu.be/T5spUmVMkVU?t=811

This is pretty clean.

2/28/2023

8:05am. Let me link to the sleep apnea thread again.

https://news.ycombinator.com/item?id=34953053

Tonight I woke up in the middle of it due to a nightmare. Nothing unusual for me. I admit, I thought it was psychological and due to stress, but thanks to this thread, I am conjecturing that the poor sleep I've been having over the past decade might have something to do with my nasal congestion.

I mean, whenever I am horizontal, one of my nasal channels is completely blocked.

As I kid I used drop to decognest them, and I still have those tubes, but I stopped using those as it was too much of a pain.

Since I am in the age of the internet, I should do some research on this.

https://www.robitussin.com/cough-cold-center/stuffy-nose-at-night

Any mail? None.

https://www.robitussin.com/adult-robitussin/severe-multi-symptom-cough-cold-flu-nighttime/

No, I don't have a cold, just a stuffy nose.

8:20am. I have my old nasal meds from a two decades ago still lying in the pot next to my bad. I am going to try them out from here on out.

https://desuarchive.org/_/search/boards/fit.desu.meta/text/nasal%20congestion/

///

>>68757233
this little nigga clears me right up
need to take it every 5 hours or so though or the congestion is even worse than before

///

I used something similar to this. What are these sprays they are talking about?

///

>>68760885
>need to take it every 5 hours or so though or the congestion is even worse than before
yeah that's cos your blood vessels are fucked, that's what's congesting you now.
what you need to do is wean yourself off of it slowly, when you go to sleep, sleep with only one spray in one nostril
it takes one week to recover from it from cold turkey, trust me you're going to have to do it sooner or later, I did, and it sucked but one spray in one nostril allowed me to sleep and I regret not doing it sooner.

///

Yeah, I think it was messing with my vessels, that is why I stopped.

///

>>65911714
Avoid nasal spray at all costs anon. It causes physical dependence and erodes the lining of your nose. My brother in law was made to use it daily as a child by his grandparents. He started getting worse and worse congestion and constant nosebleeds. When he saw an ENT finally they said it looked like he had been pouring acid in his nostrils daily for years.

///

What is the solution?

> Decongestant nasal sprays are dangerous to use every day because they case rebound congestion. Steroid and anti-histamine nasal sprays are safe to use every day, as are oral decongestants.

> look it up dude. ur nostrils are SUPPOSED to be 1 clogged 1 working good all the time. it cannot be like u took nasal spray all the time. one has to be clogged to work naturally. its science look it up.

Huh really?

https://youtu.be/RXPMlOuOHFI
Stuffy Nose | How To Get Rid Of A Stuffy Nose Clear Blocked Nasal Congestion

Ah, let me watch this.

...Let me leave this for later.

https://www.mayoclinic.org/healthy-lifestyle/consumer-health/multimedia/neti-pot/img-20008137

https://www.webmd.com/allergies/neti-pots

Neti pots are available over-the-counter at many drug stores, health food stores, and online retailers. They usually cost between $15 and $30.

I should try this.

8:40am. Ok, enough of this for now. Let me chill, and then I will get started on finishing those EF tutorials.

https://boards.4channel.org/a/thread/249508791/what-method-would-you-choose-to-achieve#p249511263

///

>>249509351
>And there's nothing else to achieve - you already attained the ultimate goal.
Not with that attitude, anon.
You seriously need the GRIND MONKEEE mindset, unless you want to end up as generic Background Character F.
Took over the planet? Time to take over the solar system. Then the galaxy, then the universe, then the multiverse, and all of creation and all that is beyond that, as well. As long as there is something above you, there's still more things to do. And if you somehow managed to get to the absolute peak, you can turn downwards and seek supremacy on the quantum level as well, whatever beyond-human-understand-things that would entail. If you finished up with that as well, then it's time to also control all of time, all of history, from beginning to end.
And if you manage to do even that, then you'd know that if you can do it, then so can others as well. Hence next you'll either cryo-stasis yourself or personally guide someone to be able to reach your level without interfering too much. Eventually you'll have equals again, and thus you have something new to do as well, since you are once again not in complete control anymore, or perhaps your combined powers will enable you to reach heights or depths that were impossible to you alone until that point.

As the saying goes:
Those who want to do something find ways.
Those who don't want to do something find excuses.

///

Based.

9:05am. Let me start.

Before I do that, let me show those neti pots to my dad.

9:10am. He ordered one. I am still stuck in the 90s in some ways and didn't realize how easy it is to order things over the internet. He ordered one for me.

The fact that he could just look it up on his mobile did not occur to me.

Anyway, let me leave that aside.

Time to watch the rest of Jasper's EF videos.

https://youtu.be/uQfeppE2SLE?list=PLQB-TSatJvw4T7mQneItRgsemyjMMYRNk
Entity Framework Core Part 8 - Attribute-Based Configuration

It was this I think.

Yesterday I realized I got an accept 5 days ago, but like with Valora I am skeptical of getting interviews until I get my portfolio established. At that point, people will be chasing me down and I'll have my pick of jobs. Right now, I do not want to think about them.

https://youtu.be/uQfeppE2SLE?list=PLQB-TSatJvw4T7mQneItRgsemyjMMYRNk&t=503

I am really learning a lot of C# from this guy.

https://youtu.be/uQfeppE2SLE?list=PLQB-TSatJvw4T7mQneItRgsemyjMMYRNk&t=936

Oh you can look at relationships like that.

9:50am. https://github.com/efcore/EFCore.FSharp

After I finished the vid, I did a little search, it seems there are F# tools for EF Core.

> This provides support for code-first and database-first use of EF Core in F#, including supporting record and option types.

Sweet!

I was actually going to use C# just for EF Core, but if F# has support for it then why bother?

https://fsharp.org/guides/slack/

My god, I still haven't gotten acces to this. I'll try to make a separate account later.

9:55am. https://youtu.be/7M501P-23Jg?list=PLQB-TSatJvw4T7mQneItRgsemyjMMYRNk
Entity Framework Core Part 9 - The Fluent API

Time for part 9. I only have two more left before I am done.

https://youtu.be/7M501P-23Jg?list=PLQB-TSatJvw4T7mQneItRgsemyjMMYRNk&t=372

Ah, it is possible to have more than one primary key.

https://youtu.be/7M501P-23Jg?list=PLQB-TSatJvw4T7mQneItRgsemyjMMYRNk&t=671

I admit, I am a bit curious as to how this kind of reflection would work. I didn't know .NET could do something like that.

10:15am. https://youtu.be/7M501P-23Jg?list=PLQB-TSatJvw4T7mQneItRgsemyjMMYRNk&t=799
> As I said in the last video, the best thing to do is nothing at all.

Now that I understand what the Fluent API is for, I am honestly confused as to why Teddy used it. The stuff he did should have been inferred automatically anyway.

https://youtu.be/0ndu7Zhc84Q?list=PLQB-TSatJvw4T7mQneItRgsemyjMMYRNk
Entity Framework Core Part 12 - Inheritance

Time for this one. After this, I'll look at the never EF 7 videos by him.

10:30am. https://youtu.be/0ndu7Zhc84Q?list=PLQB-TSatJvw4T7mQneItRgsemyjMMYRNk&t=309

I've started browsing the /twg/ thread on the side. Focus me, focus! Just get this done today so you can get to the interesting things tomorrow!

https://youtu.be/0ndu7Zhc84Q?list=PLQB-TSatJvw4T7mQneItRgsemyjMMYRNk&t=455

Hmmm, does this mean it would be able to store unions? I mean, this is how unions are implemented in F#, by inheriting on a base class.

https://youtu.be/0ndu7Zhc84Q?list=PLQB-TSatJvw4T7mQneItRgsemyjMMYRNk&t=539
> That is the way we can have this working?

Why not link to other table via foreign keys? Tell me that is possible.

https://youtu.be/0ndu7Zhc84Q?list=PLQB-TSatJvw4T7mQneItRgsemyjMMYRNk&t=589
> In EF Core, until recently, that was the only way it could be done.

https://youtu.be/0ndu7Zhc84Q?list=PLQB-TSatJvw4T7mQneItRgsemyjMMYRNk&t=771

I wonder if it would be possible to use annotations for this?

https://www.youtube.com/watch?v=A5_thTxsCjY&list=PLQB-TSatJvw5hG-NYfyEJCj6TvXQmi5Jw
Entity Framework 7 - Bulk Editing

Let me watch these as well.

https://youtu.be/A5_thTxsCjY?list=PLQB-TSatJvw5hG-NYfyEJCj6TvXQmi5Jw&t=481

So this wasn't here before?

Still, what about the need to fetch the whole thing?

https://youtu.be/A5_thTxsCjY?list=PLQB-TSatJvw5hG-NYfyEJCj6TvXQmi5Jw&t=543

Hmmm, for deleting by id, I suppose I could just use a where, follow by execute delete.

https://youtu.be/A5_thTxsCjY?list=PLQB-TSatJvw5hG-NYfyEJCj6TvXQmi5Jw&t=852

Hmmm, really. I had no idea this was possible.

https://youtu.be/A5_thTxsCjY?list=PLQB-TSatJvw5hG-NYfyEJCj6TvXQmi5Jw&t=1312

Huh, WTF?

I am going to have to backtrack, I admit, I am tunning out a bit at this point, but this is bringing me back in.

https://youtu.be/zctMt_rF9_U?list=PLQB-TSatJvw5hG-NYfyEJCj6TvXQmi5Jw
Entity Framework 7 - Inheritance

Let me finish these last two and then I will close for the morning.

https://youtu.be/zctMt_rF9_U?list=PLQB-TSatJvw5hG-NYfyEJCj6TvXQmi5Jw&t=204

C# keeps getting better, but damn is it verbose.

https://youtu.be/yZNo-l30dhc?list=PLQB-TSatJvw5hG-NYfyEJCj6TvXQmi5Jw
Entity Framework 7 - JSON Columns

Ohhhh...finally. Let me watch this and then I will have finished the EF Core course. I'll know everything I need to use it effectively.

https://youtu.be/yZNo-l30dhc?list=PLQB-TSatJvw5hG-NYfyEJCj6TvXQmi5Jw&t=161

Finally records come in!

12:05pm. Had to take a break, let me finish the video.

https://youtu.be/yZNo-l30dhc?list=PLQB-TSatJvw5hG-NYfyEJCj6TvXQmi5Jw&t=940

Does it not have the ability to infer the type in the API request on its own?

https://youtu.be/yZNo-l30dhc?list=PLQB-TSatJvw5hG-NYfyEJCj6TvXQmi5Jw&t=1271

SQL. I'll remember how he did this.

https://youtu.be/yZNo-l30dhc?list=PLQB-TSatJvw5hG-NYfyEJCj6TvXQmi5Jw&t=1401

Eh, this would cause the query to be rebuilt each time.

https://youtu.be/yZNo-l30dhc?list=PLQB-TSatJvw5hG-NYfyEJCj6TvXQmi5Jw&t=1405

He says that this avoids the risk of an SQL injection attack.

12:25pm. https://youtu.be/9zJn3a7L1uE
.NET 7 Beginner Course 🚀 Web API, Entity Framework 7 & SQL Server

Forget this one.

Damn, my sleep tonight was worse than I thought. I am pretty drowsy right now.

I hope that the neti pot does something to help my night breathing. Back in high school I went to a lot of doctors for this and they did shit.

If this was the post-Singularity era, I would not have to deal with these meat sack issues.

12:35pm. Mhhhhh...

Now what I need to do is finally get through that damn Web API course by Teddy Smith!

I am going to get through that and finally graduate from being a web dev toddler.

Let me do the chores here. Then comes breakfast.

1:25pm. Done with chores. Time for grub."

---
## [i574n/The-Spiral-Language](https://github.com/i574n/The-Spiral-Language)@[f88da91566...](https://github.com/i574n/The-Spiral-Language/commit/f88da915660195fa309620bb7dafba6cdd77b17f)
#### Thursday 2023-04-06 23:24:53 by Marko Grdinić

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
## [i574n/The-Spiral-Language](https://github.com/i574n/The-Spiral-Language)@[e6565584d3...](https://github.com/i574n/The-Spiral-Language/commit/e6565584d3685de528ba6d95718495aeb8f73de2)
#### Thursday 2023-04-06 23:24:53 by Marko Grdinić

"///

IC: Have you ever thought about selling PCIe cards with your chip at retail, like a GPU, just an accelerator that people can buy off the shelf? Because I've had a lot of requests for that.

JK: Yeah, we're going to do that. About a year and a half ago we started to rev up - we ordered thousands of cards. We had a reasonable number of models running, and we thought we were going to start to sell, you know, small volumes to people who wanted to take them, experiment with them. Then basically due to the supply chain, the cards didn't show up so we had nothing to sell.

///

8pm. I am pretty tired right now.

https://rinzewind.org/blog-en/2023/the-tech-downturn-seen-through-hacker-news-comments.html

This is all bad news for me.

8:20pm. > “I know, right? Lady Komari is so cute and funny.

Let me read the Komari novel. I'll leave anime for later.

> You can trust this intel; we got it from our ninjas.

This is a great line, I'll keep in stock.

https://interviewing.io/guides/system-design-interview
https://news.ycombinator.com/item?id=34999464
A Senior Engineer's Guide to the System Design Interview (interviewing.io)

I'll leave this for later.

3/3/2023

8:20am. I had trouble going to sleep tonight. Yeah, I am a bit pissed about not getting callbacks, but that is merely a consequence of the way I've approach the problem and structured my resume. During the night I've been thinking about chatGPT. The humans won't help me in my quest, but an AI assistant like it could provide great value in my job search. What the hell do I know what a top rated resume should look like?

An AI assistant trained on the entire Internet would definitely be better at it than me. The next time I apply I am going to go back to the mentality of a couple of months ago, but not to the point of complete bullshittery like with the resume I had last time.

I am going to aim for the senior positions directly.

But first I actually need the skills to do webdev properly.

I'll put in some real with my portfolio projects, Spiral and web page, and a ton of bullshit otherwise. You bet I am going to have 5 years of pro experience working at some company when I apply next time.

Forget about getting a job. Think getting offers during the next round.

8:25am. I've slept like shit tonight, but I am full of determination.

No mail as expected. I'll turn off Thunderbird.

On AngelList I got a reply that they are creating a profile and will send me a reply if I am a close match. What are the chances of that? Zero.

What was the point of accepting if they are going to pivot and tell me they are looking for a match. They are just stringing me along.

The next time I do this, I'll take these companies to the cleaners.

8:30am. Now let me read Mental Out.

I am not that far from getting a job. I need a few months to completely master the domain, but after that I'll drop programming and start the interviewing practice. Anything goes!

9:40am. Done with the bath. Let me finally watch that video from two days ago by Onur Gumus. I wish I could at least get good night's sleep. Imagine if the job turns out to be really stressful, well, I can always just quit it.

https://youtu.be/2pnj19qWLdQ
Fable.Remoting and Elmish.Bridge

Let me start this. Once I have the knowledge of how this works, I'll be able to move on to the server part of my portfolio project.

https://youtu.be/2pnj19qWLdQ?t=95

I'll really have to play with sending http requests directly at some point, just to see what they are made of.

https://youtu.be/2pnj19qWLdQ?t=100

I should look up a tutorial on this later. There a Chrome dev tools tutorial amongst the crash courses.

https://youtu.be/2pnj19qWLdQ?t=164

Oh Fable Remoting has binary serialization.

https://youtu.be/2pnj19qWLdQ?t=305

Huh, I had no idea Union type cases could be made private.

https://youtu.be/2pnj19qWLdQ?t=329

This is an interesting way of doing it. He says that pattern matching won't work once the case is made private, and introduces an active pattern to get around that.

https://learn.microsoft.com/en-us/dotnet/api/system.text.json?view=net-7.0

.NET 7 has a native JSON serializer.

https://www.youtube.com/results?search_query=.net+text+json

I'll check them out later.

https://youtu.be/2pnj19qWLdQ?t=569

Vite prefers a different number? I do not understand this, but fine. I'll play around with his stuff.

https://youtu.be/2pnj19qWLdQ?t=605
> I prefer Giraffe over Saturn. I never understood why Saturn exists in the first place.

He is configuring it to use websockets.

https://youtu.be/2pnj19qWLdQ?t=679
> Cors is not a restriction, it is actually a relaxation.

https://youtu.be/2pnj19qWLdQ?t=788

Here he is praising regular ASP.NET's template generation, and says that you don't have to restrict yourself to Giraffe either.

https://youtu.be/2pnj19qWLdQ?t=940

Actually, it is weird that the handler is being passed in like this.

https://youtu.be/2pnj19qWLdQ?t=1059

It is configured differently to how I did it.

https://youtu.be/2pnj19qWLdQ?t=1521

I really need to get familiar with raw HTTP requests. My skills as a web dev are too lacking.

https://youtu.be/2pnj19qWLdQ?t=1536

Focus me, stop browsing HN on the side. Here he is showing how I could make a RESTful interface using Fable Remoting. That is really good.

https://youtu.be/2pnj19qWLdQ?t=1574

Oh wait, did he just put in a breakpoint in the Chrome browser?

https://youtu.be/2pnj19qWLdQ?t=1783

I could use it from a C# application. Let me take a short break.

11am. Let me resume.

https://youtu.be/2pnj19qWLdQ?t=1931

Hmmm, he isn't using the Fake run script.

https://youtu.be/2pnj19qWLdQ?t=1994

This scared me!

It seems it is possible to just right click and remove all the breakpoints.

https://youtu.be/2pnj19qWLdQ?t=2197

He is using this to draw diagrams.

https://youtu.be/2pnj19qWLdQ?t=2217
> If you refresh now, the server will detect you're disconnected. And you can take an explicit dispose action.

I am really curious as to how I could configure the server so it acts upon multiple users concurrenctly. How would I implement something like an online poker room too?

https://youtu.be/2pnj19qWLdQ?t=2259

Let me try out this site he is using. CSP is not well suited for diagrams.

https://excalidraw.com/

Oh, it is pretty cool. It is way better than CSP for this simple purpose.

I love it.

I'll keep it in mind next time I try to do a diagram.

https://youtu.be/2pnj19qWLdQ?t=2284

Oh the arrows can get attached to the original function. I see.

https://youtu.be/2pnj19qWLdQ?t=2352

I am not sure I understand. Are the model and update functions mirrored for some reason?

https://youtu.be/2pnj19qWLdQ?t=2479
> It is very confusing. I did not understand how to use it efficiently.

He is talking about the Elmish Bridge communication.

https://youtu.be/2pnj19qWLdQ?t=2508

It has broadcasting?

https://github.com/Nhowka/Elmish.Bridge#reply-channels-since-500

Wait, it seems v1 wasn't the latest. I see it has v5 here. Let me check the Nuget package.

https://www.nuget.org/packages/Elmish.Bridge.Server

Ih the latest is v7.

https://youtu.be/2pnj19qWLdQ?t=2947

To be honest, I do not like the Fable.Lit much compared to Feliz. But that isn't a problem.

https://youtu.be/2pnj19qWLdQ?t=3075
> Notice that I've wrapped it in `Cmd.ofEffect`.

https://youtu.be/2pnj19qWLdQ?t=3307

You know, these subjects are really good for me. This something I should focused on in 2020, yet I botched my learning path and wasted 6 months. Now I paying for it.

Once I learn these subjects, I'll be able to rewrite the Spiral language server so it is more concise and stable compared to what I have now.

11:50am. In addition to watching this, I will do a proper deep dive of ASP.NET, Elmish.Bridge and Fable.Remoting.

I spent the last ten days studying the frontend tech and databases. I have that on hand now.

The next step is to master the backend aspects of web development for good. Even if it takes me a whole month, it would be worth it. This kind of knowledge and experience won't go out of date ever.

https://youtu.be/2pnj19qWLdQ?t=4064

He really should have just wrapped the use of clientDispatch in an async.

12:15pm. That was informative.

Yesterday while looking at LinkedIn ads, I saw a new MS tech called Orleans, which I am guessing is like Akka.

https://youtu.be/riMHC0Xpm9U
5 technologies that I will be learning in 2021 as a .NET developer

Let me watch this short vid.

https://www.patreon.com/nickchapsas

Damn, this guy has a lot of Patrons.

> Hello everybody, I'm Nick Chapsas and this is my Patreon page. For the past 3, years I've been creating free content for C# and .NET on my YouTube channel. 3 years later, and creating content is my full-time job. In order to diversify my revenue streams to make sure I can do this for a long time, I created a Patreon where you can support me monetarily.

I am jelly.

https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/Orleans-MSR-TR-2014-41.pdf

///

High-scale interactive services demand high throughput with low latency and high availability, difficult goals to meet with the traditional stateless 3-tier architecture. The actor model makes it natural to build a stateful middle tier and achieve the required performance. However, the popular actor model platforms still pass many distributed systems problems to the developers.

The Orleans programming model introduces the novel abstraction of virtual actors that solves a number of the complex distributed systems problems, such as reliability and distributed resource management, liberating the developers from dealing with those concerns. At the same time, the Orleans runtime enables applications to attain high performance, reliability and scalability.

This paper presents the design principles behind Orleans and demonstrates how Orleans achieves a simple programming model that meets these goals. We describe how Orleans simplified the development of several scalable production applications on Windows Azure, and report on the performance of those production systems.

///

He links to this paper. Let me leave it aside for now.

https://github.com/akka/akka-meta/blob/master/ComparisonWithOrleans.md

https://youtu.be/riMHC0Xpm9U?t=128

He says that Halo's online service uses it.

https://youtu.be/riMHC0Xpm9U?t=168

He recommends this guy for a deeper intro.

https://youtu.be/riMHC0Xpm9U?t=190

I wonder what these source generators are.

https://youtu.be/riMHC0Xpm9U?t=241
> Reflection, but compile time.

I'll have to check this out.

https://youtu.be/riMHC0Xpm9U?t=290
> ASP.NET is actually using dictionaries and some very miminal reflection for the first instantiation of the classes to create them.

https://learn.microsoft.com/en-us/dotnet/csharp/roslyn-sdk/source-generators-overview

Oh you literally generate C# text. I could do this.

12:30pm. Hmmm, I could use this to interface Spiral with F# more deeply. Nevermind that for now.

https://youtu.be/riMHC0Xpm9U?t=358

I could have used gRPC back in 2020, but I was too stupid and went with ZeroMQ.

Determination really makes a difference. Back then I wanted to just learn enough webdev, but now that I want to really dive into it, my learning progress and trajectory is a lot more ferocious.

https://youtu.be/riMHC0Xpm9U?t=390
> It is way faster than REST, but more niche.

https://youtu.be/riMHC0Xpm9U?t=544
> A software engineer that knows devops technologies is very, very valuable.

He recommends that I learn devops to adds value to myself as a soft eng.

https://youtu.be/riMHC0Xpm9U?t=791

All this tech is something that I've often seen in job ads.

https://youtu.be/riMHC0Xpm9U?t=873
> I can't believe I was so late to the party learning this.

Sigh...just what was I doing in the past 8 years? I should just focus on gluing things together rather than making AI breakthroughs. It is like the world does not want me to pursue the path of transcendence.

12:45pm. https://youtu.be/9CDgPgWF9IY
Why I won’t need constructors anymore in C# 11

Let me watch this.

https://youtu.be/9CDgPgWF9IY?t=276

Hmmm, yeah, I've underestimated the required keyword. I see where he is going.

Constructors are the worst part of OO for me, so getting around them is always a bonus.

12:55pm. https://boards.4channel.org/a/thread/249601990#p249629470

///

>>249601990 (OP)
This page is godly because you can tell it's a word for word transcript of an actual conversation he had with an editor. Then he proceeded to not follow any of his advice in his own manga, and got them axed.

///

///

>>249629470
Somebody once told me that something that everyone enjoy is also something no one enjoy. You gotta accept that not everyone will be interested in your stuff and that some people will hate it.

///

...

I think that going along with popular Youtubers like Nick is a good strategy. What sells for them is usually what is in demand in the job market, so I should learn up and skill up myself.

I've watched that video by Onur, but I didn't get too much from it. The repo he showed should be valuable for me since I'll use it as a reference for setting up my own project. I also was under the impression that the project was not updated in a while and this dispelled that mistaken assumption.

1pm. The next step would be to study up on websockets in .NET.

As I said, now that I feel confident about both frontends and databases, the communication parts are what I need to tackle. I'll probably be studying this for a while, but at some point I am going to reach the zenith. At that point, it will be time to work on my people skills.

This will complete me as a programmer. Surely actually getting to the point where I am making money from it will count as something, right?

I believe that all this knowledge I am learning here will be useful either way. Having systems that communicate will be useful for scaling my own stuff.

I wish that at some point the reinforcement learning path would become viable.

Programming is a young field, it was completely different a few decades ago. So who is to say it won't change in the future."

---
## [i574n/The-Spiral-Language](https://github.com/i574n/The-Spiral-Language)@[b7b5c3075e...](https://github.com/i574n/The-Spiral-Language/commit/b7b5c3075ebc8b72b1a8643643da04abd3c61ca4)
#### Thursday 2023-04-06 23:24:53 by Marko Grdinić

":35am. I am up. I slept well tonight, I think. Any mail? Not really.

I see that the mic still hasn't been handed over to the delivery service, but it is still early in the morning today.

7:40am. Today I want to take a break. Let me do some reading, then I will take a bath.

Rosen Garten and Kakeru are out, and I have to catch up with the Eiyu thread and watch the anime.

8am. Let me watch Inglis' anime. I need to take it easy. After going at it full tilt, I do not feel like going at it strong today. I really should reserve a day or two just for fun. Though I will do some programming later today.

9:05am. I've chilled. Next is to start getting ready for that bath. Only after that will I do some programming.

https://boards.4channel.org/g/thread/91932922/twg-tech-workers-general

> Read the sticky and make your resume just like it says. Each work experience job should be summed up into a single informative line, and use https://resumake.io/ to make your resume spiffy and scrapable to recruiters. Then put that resume onto indeed (you don't need to convert it to indeed's format just add the pdf) and LinkedIn, and in a few days or weeks at most you'll be getting Indians calling you and e-mailing you for contract work in your local area.

I'll try it later.

https://www.careercup.com/resume
> This is what a good resume looks like.

https://resumake.io/

///

>>91933616
Lots and lots of people lie on their resume, it's very common for newgrads. Fluff, "C++/C", "I ran my own startup" (Made $0, never attempted to make money anyway), worked at McDonald's? Don't list the title, imply it's IT at McDonalds, etc.
Newgrads are between a rock and a hard place. On one side, you have to get past those resume filters and HR retards, made worse by the fact that ALL your competition is lying 10x the amount you probably are, making you look bad in comparison, but on the other, once you get past them, then you have to get through the actual tech guy that's interviewing you, and he will pick through that bullshit so easily and embarrass you. So it's a balancing act. Don't sell yourself too short as to not get through HR, but don't put C++ on your resume because you had to write a Hello World for it in college one time.

///

This is from a recent thread.

9:20am. Let me take a bath here. It is time for that. Then I'll start moving to programming. Or I can watch that Reaper course. Whatever I feel like. I really want the mic to get here.

10:10am. Let me start work for the day. Here is what I am going to do. I am going to move the setup videos to a separate playlist. Then I am going to unlist some of the vids. Actually, delete them entirely. I am going to be redoing the intro and the minimal UI anyway once the mic gets here. After that, let me make a new resume.

10:25am. I moved the 3 important setup videos to their own playlist and unlinked them.

The Leduc intro on the other hand I will redo, but I'll leave them there for now.

Now, what I want to do is make a resume.

https://resumake.io/

I've done this a lot but...

You know what, let me not do it. As much as I want Indian recruiters to treat me like some hot piece of ass, it would just waste my time. What I should it face the torment. Do the damn projects. Then go into it properly. 4 years of work at at research focused startup called Rajnet, and 2 years at my father's company called Stag. After that I'll aim for mid and senior positions.

Now...let me get started. Just for a bit. Let me start Rider.

Ok, I have the project from yesterday there. What else should I do, but put in the game?

Yeah, it is time for that.

Those projects that I did in 2021? It is finally time to revisit them.

PS C:\Users\Marko\Source\Repos\The Spiral Language\Spiral Compilation Tests> dotnet "c:\Users\Marko\.vscode\extensions\mrakgr.spiral-lang-vscode-2.3.10\compiler\Spiral.dll" port=13805
Server bound to: tcp://*:13805 & tcp://*:13806

Sigh, just sigh. Note how I am using two ports for essentially no reason. Now that I have some skills, I'll really want to update my methods, but nevermind that for now.

```spiral
// Since the past attempts failed, I am going to try something else here. Inspired by the
// signSGN papers, for the optimizer I am going to make an update that interpolates
// signSGD + infinity norm gradient normalization. For the value network, since I absolutely
// need the values to act as weighted moving averages, I am going to semi-tabular CFR in the
// value head.

// Instead of one hot vectors like in full tabular, the semi tabular will have probabilistic
// vectors. I'll take a log softmax over the body, exp it and use that as the prob vector input
// to the head which be optimized using the tabular algorithm.

// For getting the gradients for the value body, I'll use the absolute value differential
// between the given and the predicted error, center it with regards to the probabilistic mean
// and use that as the backwards input for the log softmax.
// (Edit: As it turns out, the regular softmax works a lot better. I was worrying that saturation
// would be an issue, but that property actually makes convergence possible.)

// Alternatively updating the value head and body will make this an EM procedure similar to k-means.
// The main reason why I am going for this besides being able to weight the values is because
// right now I can't tell at all whether the value update works. If I had a tabular agent, this
// kind of debugging would be a lot easier.

// The issue with the value net is that it needs to learn the reward magnitudes in the weights,
// so I cannot use something like signSGD (which is Adam with full batch learning) to stabilize it.
// This is a source of many of my headaches. NNs are good for probability distributions, but bad
// for learning large ranges of values.

// With this method I'll be able to optimize the value head and get something useful even without
// necessarily optimizing the body if I want to pick that route. (Edit: Much like for the actor,
// optimizing the critic body using the targets generated by the tabular algorithm works fine.)

// The actor on the other hand will be will be possible to deal with as I will be able to use policy
// gradients with the aforementioned optimizer together.

// ---

// Update (6/9/2021): My worked and I am capable of training a NN agent competitive with the tabular
// one with roughly the same amount of compute. The NN algo itself is implemented in `control.py`.

// Some details:
// * Even though the optimizer supports interpolation, I've ditched infinity norm in favor of pure signSGD.
//   I might add a momentum component to signSGD in the future, but otherwise I won't bother with adaptive
//   optimizers like Adam. They all converge to signSGD when doing full batch learning anyway.
//   In future work, I think I'll just tune the batch size until signSGD is happy.
// * Averaging in the weight space is sufficient for dampening self play oscilations and getting good policies.
//   Thanks to it I did not have to gradually lower the learning rate or anneal the exploration epsilon.
//   I did observe a benefit when I lowered the actor LR by 2x, so it should be possible to get better
//   performance by doing LR annealing even with averaging.

// I am quite pleased with how things went here. I'll archive this project and move on to making
// the Holdem game next. The algorithm here is novel and deserves a blog post at some point, though I
// won't bother writing a paper as I am not into theorems.

// I am looking forward to trying it out on games that could give me real world advantages.

// Update (6/18/2021): Did some updating and cleaning up. As it turns out, I was looking the
// regular players instead of the averaged ones and drawing the right conclussions from the
// wrong data. I am lucky that what I wrote in the relevant bullet about weight averaging point
// is all true.

// The commit at this date has data on what my runs look like. I've been training agents over and
// over for the whole day. The only activations worth using with LN are Relu and Leaky Relu.
// I tried a few others, but probably because of poor weight init they saturate too easily and
// work very poorly. Relu composes with LN particularly well, and it will be my main choice. Relu,
// Leaky Relu (and `abs` which I haven't tried) when paired with LN and signSGD have the property
// of making gradient steps invariant to the weight scale.

// The algorithm in `control.py` preserves that property when the goal is to learn value functions.

// Update (6/22/2021): As it turns out updating the critic, actor and the critic head all at once
// improves computation time by 4x without degrading the final performance. I am impressed.
// Compared to the `Actor-Critic Policy Optimization in Partially Observable Multiagent Environments`
// paper, my method here gives better final performance while being over a 100 times faster to train.
// In that paper they update the critic 128 times before updating the actor once.

// I haven't bothered testing this until now, but since I am preping for Holdem, I realized that
// I really should since if it worked, it could reduce the time it takes to train an agent from a
// month to a week. One hyperparam I still haven't bothered tuning at all is the head decay.

// A batch of 1024 is enough to cover all of the Leduc's states so I haven't bothered, but for Holdem
// and bigger games 2 ** -2 might be too strong of a decay.

// Update (6/27/2021): Testing the architecture here on Holdem made me realize it is absolute garbage
// at optimizing the value function. On flop poker vs callbot, it cannot learn a thing. The only reason
// it works on Leduc at all because the game is so small. Not just the NN architecture, I changed the
// the `belief_tabulate` and `model_evaluate` functions significantly as well. Adding momentum to
// signSGD helps significantly as well. (Edit: I tried it on Leduc and it works far worse than vanilla.
// What a disappointment, it seems it only helps vs static players.)

// Due to all the changes I would not recommend using this project as a reference, I have a lot better
// stuff in ui_holdem2. There is an updated Leduc test there. That having said, it takes a very large
// number of iterations to become competent at hand reading. There might be even better architectures
// out there; I get the sense that vanilla nets are not the right thing for the job.

packages: |core2-
modules:
    serialization/
        dense/
            array
        sparse/
            int
    utils-
    sampling
    nodes-
    leduc
    train
    agent/
        uniform
        neural
        tabular_old
        tabular
    create_args
```

Look at the comments in the final ui-leduc spiproj file. It is broken as I no longer even have core2. But this stuff is a blast from the past. I put in so much passion into it.

```spiral
// I could not finish it by adding the hindsight information. That having said, the challenge of making the value function
// trainable has been dealt with. Now I just need to find a way to train the policy. I have the same issue as last time
// where the agent converges to an aggrodonk. Given the small batch sizes, the optimization process is simply too unstable.

// The way I will defeat this challenge is by having the net train against static copies of itself. Not just a single static
// copy, but multiple past iterations. I tried this before while trying the Flop agent, and it did not work better than regular
// self play, but that was a special case. Holdem is large enough that the stability benefits of making the enviroment
// stable are needed.

// The minimax optimization that is going on here needs stable and careful steps. Leduc works because it is small, and Flop
// worked because it had short sequences and MC. Hodlem is beyond the threeshold where such tricks would be applicable.

packages: |core-
modules:
    types-
    conv-
    serialization/
        dense/
            array
        sparse/
            int
    utils-
    sampling
    nodes-
    train
    train_cat
    hand_scorer
    hu_holdem
    leduc
    agent/
        uniform
        holdem_callbot
        tabular
        neural_leduc
        neural_holdem
    create_args_leduc
    create_args_holdem
```

This is from the final `ui_holdem` project. Since it uses the regular core, it at least typechecks properly.

11am.

```spl
union rec node state obs (actions : * -> *) act =
    | Terminal : pl2 obs act * state * r2
    | Action : pl2 obs act * state * pid * actions act * (log_prob * act -> node state obs actions act)
```

Hmmm, I was returning nodes instead of CPSing it like I thought I was.

Eh, the thing is really abstract.

```spl
inl belief_tabulate slots (action_indices : a u64 st) (at_action_value : a u64 f32) (at_action_weight : a u64 f32) =
    inl update_head () =
        am.iter4 (fun {policy head={weighted_value weight}} i_action at_action_value at_action_weight =>
            inl add_to l v = inl x = index l i_action in set l i_action (x + v)
            add_to weighted_value (at_action_value * at_action_weight) . add_to weight at_action_weight
            ) slots action_indices at_action_value at_action_weight
    inl action_fun (action_probs : a u64 (a st f32)) (sample_probs : a u64 (a st f32)) =
        inl batch_qs =
            am.map4 (fun {policy head={weighted_value weight}} i_action sample_prob r =>
                am.mapi2 (fun i_action' weighted_value weight =>
                    inl q = if weight <> 0 then weighted_value / weight else 0
                    if i_action = i_action' then (r - q) / (index sample_prob i_action) + q else q
                    ) weighted_value weight
                ) slots action_indices sample_probs at_action_value
        inl rewards = am.map2 (am.fold2 (fun s a b => s + a * b) 0) batch_qs action_probs
        inl update_policy () =
            am.iter4 (fun {policy={current grad} head} qs mean regret_prob =>
                am.mapInplace (fun i grad => grad + regret_prob * (index qs i - mean)) grad
                ) slots batch_qs rewards at_action_weight
        rewards, update_policy
    update_head, action_fun
```

Back then I understood this quite well, but now...

11:15am. I am looking at the past code and thinking.

It really has been a while since I've done real programming.

12:15pm. Breakfast time.

12:50pm. I had time to think about how I am going to do this. After glancing at the old code, I realized all the game implementations are intervowen with the sampling stuff. I am definitely going to put some effort into decoupling them.

I'll redo both games in F#. That will be my next goal. I'll use the MVU pattern for it instead of a recursive function block like I am doing now.

https://headcanontl.wordpress.com/2023/02/27/savage-fang-vol-2-c6/

Let me catch up with Savage Fang, then I will do the chores. Then I will do some actual programming. Today is pretty chill.

12:55pm. Every day should be chill like this. What is the point in exerting myself? I've more or less reached the apex of my programming at this point. What I will do next is bring it all together under the umbrella of web development.

A project like this will in some way be culmination of all my experience. Many different languages and backends, all seamlessly integrated into a single system. What is not to like?

1:10pm. Though it is not correct to say that I've reached the apex. Aren't I still learning?

And isn't what I am going to do here a step up from what I had before?

1:25pm. Ok, let's go do the chores. Then I will redo the Leduc game the way it should be done.

1:55pm. Done with chores.

Ok, let me just do it. Let me implement Leduc in F#. I am just going to change the architecture of the old game a little and port it from Spiral to F#. That will ensure it is decoupled.

```spl
union action = Fold | Call | Raise
union card = King | Queen | Jack

type player = {card : card; id : u8; pot : i32}
type players = player * player
nominal leduc_state = player * player * bool * card
nominal leduc_actions act = { is_fold : bool; is_raise : bool }
type actions = leduc_actions action

inl compare_hands (community_card : card) (p1,p2 : players) =
    let tag = function King => 2i32 | Queen => 1 | Jack => 0
    inl community_card = tag community_card
    inl a = tag p1.card, community_card
    inl b = tag p2.card, community_card
    inl is_pair (a,b) = a = b
    if is_pair a && is_pair b then comp (fst a) (fst b)
    elif is_pair a then gt()
    elif is_pair b then lt()
    else
        inl order (a,b) = if a > b then a,b else b,a
        inl a,b = order a, order b
        inl x = comp (fst a) (fst b)
        if eq_is x then comp (snd a) (snd b) else x

inl raiseBy amount (p1,p2 : players) = p2.pot + amount

inl game() =
    inl deck = a ;[King; Queen; Jack; King; Queen; Jack]
    $"numpy.random.shuffle(!deck)"

    inl pot = 1i32
    inl id = 0u8
    draw deck fun (card, deck : card * a u64 card) =>
    notify (Some id) card fun _ =>
    inl p1 = {card id pot}

    inl id = 1u8
    draw deck fun card, deck =>
    notify (Some id) card fun _ =>
    inl p2 = {card id pot}

    sample deck fun community_card =>

    inl action (p1,p2,is_show_community_card) = action (leduc_state (p1,p2,is_show_community_card,community_card))
    inl terminal ((p1 : player),(p2 : player),is_show_community_card) (i,r) =
        inl r = if i = 0 then r else -r
        inl p1,p2 =
            inl p (x : player) = {x with pot#=(+) (if x.id = 0 then r else -r)}
            inl p1, p2 = p p1, p p2
            if p1.id = 0 then p1,p2 else p2,p1
        terminal (leduc_state (p1,p2,is_show_community_card,community_card)) (r2 (f32 r))

    let actions_from_state (p1,p2 : players) (raises_left : i32) : actions =
        leduc_actions {is_fold = p1.pot <> p2.pot; is_raise = 0 < raises_left}

    inl rec round_two ~(raises_left : i32) ~(p1,p2 : players) =
        inl s = p1,p2,true
        action s p1.id (actions_from_state (p1,p2) raises_left) function
        | Fold => terminal s (p2.id, p1.pot)
        | Call =>
            inl p1 = {p1 with pot=p2.pot}
            inl s = p1,p2,true
            let x = compare_hands community_card (p1,p2)
            terminal s if gt_is x then p1.id, p2.pot elif lt_is x then p2.id, p1.pot else p1.id, 0i32
        | Raise => round_two (raises_left-1) (p2,{p1 with pot=raiseBy 4 (p1,p2)})
    inl round_two_init ~(p1,p2 : players) =
        notify None community_card fun _ =>
        action (p1,p2,true) p1.id (actions_from_state (p1,p2) 2) function
        | Fold => failwith "impossible 2"
        | Call => round_two 2 (p2,p1)
        | Raise => round_two 1 (p2,{p1 with pot=raiseBy 4 (p1,p2)})
    inl rec round_one ~(raises_left : i32) ~(p1,p2 : players) =
        inl s = p1,p2,false
        action s p1.id (actions_from_state (p1,p2) raises_left) function
        | Fold => terminal s (p2.id, p1.pot)
        | Call =>
            inl p1 = {p1 with pot=p2.pot}
            round_two_init (if p1.id = 0 then p1,p2 else p2,p1)
        | Raise => round_one (raises_left-1) (p2,{p1 with pot=raiseBy 2 (p1,p2)})

    action (p1,p2,false) p1.id (actions_from_state (p1,p2) 2) function
    | Fold => failwith "impossible 1"
    | Call => round_one 2 (p2,p1)
    | Raise => round_one 1 (p2,{p1 with pot=raiseBy 2 (p1,p2)})

let game x = game () x
```

this is the entire game in Spiral. But it is coupled to what exists elsewhere. I have no idea why I let something like this pass last time.

```
union action = Fold | Call | Raise
union card = King | Queen | Jack

type player = {card : card; id : u8; pot : i32}
type players = player * player
nominal leduc_state = player * player * bool * card
nominal leduc_actions act = { is_fold : bool; is_raise : bool }
type actions = leduc_actions action
```

Sigh, what the hell is all this shit. I was crazy to do it like this. MVU. Model - View - Update. That is the pattern that I should be using in the face of concurrency.

```
action (p1,p2,false) p1.id (actions_from_state (p1,p2) 2) function
```

Passing in p1,p2 twice. This is cringe.

2:15pm. This whole thing isn't bad, but the fact that it is not isolated is making me cringe.

Web dev is looked down on, but maybe it is just the right punishment for me for writing such tightly coupled code.

```fs
type Action = Fold | Call | Raise
type Card = King | Queen | Jack
type Player = { card : Card; id : uint8; pot : int32 }
type Model = { p1 : Player; p2 :Player;  table_card : Card ValueOption }
type SelectableActionsDescriptor = { is_fold : bool; is_raise : bool }
```

This should be the game state.

https://learn.microsoft.com/en-us/dotnet/api/system.numerics.bitoperations.popcount?view=net-7.0

I need to make the sampling functions. Let me break out the intrinsics.

```
let sample (actions : 'action []) (mask : uint64) =
    let popcnt = Numerics.BitOperations.PopCount mask
    let target = Random.Shared.Next(0, actions.Length - popcnt)
    Runtime.Intrinsics.X86.Bmi2.X64.ParallelBitDeposit(uint64 target, mask)
```

Damn, now I have to figure out how the parallel bit deposit works. I am not sure if this will even work on the cloud CPU or the Tenstorrent card in the future.

Let me skip this. I'll just make the regular loop. At least popcnt I can expect to be present on future devices. Who knows about

...

Actually, the thought of how to make this work occured to me.

3:10pm.

```fs
open System

let sample (actions : 'action []) (mask : uint64) =
    let popcnt = Numerics.BitOperations.PopCount mask
    let target = Random.Shared.Next(0, actions.Length - popcnt)
    Runtime.Intrinsics.X86.Bmi2.X64.ParallelBitDeposit(1UL <<< target, ~~~mask)

let mask_bit i = 1UL <<< i

[|
for i=0 to 99 do
    yield (int (sample [|1;2;3;4;5|] (mask_bit 0 ||| mask_bit 1)))
|]
|> Array.groupBy id
|> Array.map (fun (a,b) -> a, b.Length)
|> Array.sortBy fst
```

I am playing with this in Rider. It works very nicely. Now if only I could turn that pow2 index back into the regular thing.

3:20pm.

```fs
open System

let sample (actions : 'action []) (mask : uint64) =
    let popcnt = Numerics.BitOperations.PopCount mask
    let target = Random.Shared.Next(0, actions.Length - popcnt)
    Runtime.Intrinsics.X86.Bmi2.X64.ParallelBitDeposit(1UL <<< target, ~~~mask)
    |> Numerics.BitOperations.TrailingZeroCount

let mask_bit i = 1UL <<< i

[|
for i=0 to 99 do
    yield (int (sample [|1;2;3;4;5|] (mask_bit 1 ||| mask_bit 2)))
|]
|> Array.groupBy id
|> Array.map (fun (a,b) -> a, b.Length)
|> Array.sortBy fst
```

Let me just go with this for now. It is not supported on the cloud, I'll implement a hand written method.

```fs
let parallel_bit_deposit_u64 value mask =
    let rec loop s i c =
        if i < 64 then
            let i' = 1UL <<< i
            if i' &&& mask <> 0UL then loop (s ||| ((i' &&& value) >>> c)) (i+1) c
            else loop s (i+1) (c+1)
        else s

    loop 0UL 0 0
```

I just had to do it now. Is this correct? Let me give it a try.

3:35pm.

```fs
let parallel_bit_deposit_u64 (value, mask) =
    let rec loop s i c =
        if i < 64 then
            let i' = 1UL <<< i
            if i' &&& mask <> 0UL then loop (s ||| ((i' &&& value) >>> c)) (i+1) c
            else loop s (i+1) (c+1)
        else s

    loop 0UL 0 0

let t =(15UL, ~~~1UL)
let q = parallel_bit_deposit_u64 t
let w = Runtime.Intrinsics.X86.Bmi2.X64.ParallelBitDeposit t
```

Now comes the debugging. I did everything wrong.

3:50pm.

```fs
open System

let parallel_bit_deposit_u64 (value, mask) =
    let rec loop s i c =
        if i+c < 64 then
            if (1UL <<< (i+c)) &&& mask <> 0UL then loop (s ||| (((1UL <<< i) &&& value) <<< c)) (i+1) c
            else loop s i (c+1)
        else s

    loop 0UL 0 0

for i = 1 to 10000000 do
    let f n = Random.Shared.NextInt64(0L,n) |> uint64
    let t = f Int64.MaxValue, f Int64.MaxValue
    let q = parallel_bit_deposit_u64 t
    let w = Runtime.Intrinsics.X86.Bmi2.X64.ParallelBitDeposit t
    if q <> w then failwith "q <> w"
```

This test passes, so I am decently sure I got it right.

```fs
let parallel_bit_deposit_u64' (value, mask) =
    let rec loop s i c =
        if i+c < 64 then
            if (1UL <<< (i+c)) &&& mask <> 0UL then loop (s ||| (((1UL <<< i) &&& value) <<< c)) (i+1) c
            else loop s i (c+1)
        else s

    loop 0UL 0 0

let parallel_bit_deposit_u64 (value, mask) =
    let mutable s = 0UL
    let mutable i = 0
    let mutable c = 0
    while i+c < 64 do
        if (1UL <<< (i+c)) &&& mask <> 0UL then
            s <- s ||| (((1UL <<< i) &&& value) <<< c)
            i <- i + 1
        else
            c <- c + 1
    s

let f n = Random.Shared.NextInt64(0L,n) |> uint64
#time "on"
for i = 1 to 10_000_000 do
    let q = parallel_bit_deposit_u64 (0UL, 0UL)
    // let t = f Int64.MaxValue, f Int64.MaxValue
    // let w = Runtime.Intrinsics.X86.Bmi2.X64.ParallelBitDeposit t
    // if q <> w then failwith "q <> w"
    ()
#time "off"
```

By far, generating the two random numbers takes the most time. Weirdly enough, the functional tail call function is twice as fast as the imperative version for some reason.

4:15pm.

```fs
/// Samples an action from an array.
let sample (actions : 'action []) (mask : uint64) =
    let i =
        let popcnt = Numerics.BitOperations.PopCount mask
        let i = Random.Shared.Next(0, actions.Length - popcnt)
        if Runtime.Intrinsics.X86.Bmi2.IsSupported then
            Runtime.Intrinsics.X86.Bmi2.X64.ParallelBitDeposit(1UL <<< i, ~~~mask)
        else
            parallel_bit_deposit_u64 (1UL <<< i, ~~~mask)
        |> Numerics.BitOperations.TrailingZeroCount
    actions[i], mask ||| (1UL <<< i)

let mask_bit i = 1UL <<< i
let ar = [|1;2;3;4;5|]

let result =
    [|
        for i=0 to 999 do
            yield [|
                let mutable mask = 0UL
                for _ in ar do
                    let action, mask' = sample ar mask
                    mask <- mask'
                    yield action
            |]
    |]

result |> Array.forall (fun x -> Array.distinct x = x)
```

This works perfectly. I've tested the sampling function to death.

4:45pm.

```fs
module Game

type Action = Fold | Call | Raise
type Card = King | Queen | Jack
type Player = { card : Card; id : uint8; pot : int32 }
type Model = { p1 : Player; p2 :Player; raises_left : int; table_card : Card ValueOption; mask_desk : uint64 }
type ActionPicker = { is_fold : bool; is_raise : bool }
type RewardForPlayerOne = float32

let compare_hands (community_card : Card) (p1 : Player, p2 : Player) =
    let tag = function King -> 2 | Queen -> 1 | Jack -> 0
    let community_card = tag community_card
    let a = tag p1.card, community_card
    let b = tag p2.card, community_card
    let is_pair (a,b) = a = b
    if is_pair a && is_pair b then compare (fst a) (fst b)
    elif is_pair a then 1
    elif is_pair b then -1
    else
        let order (a,b) = if a > b then a,b else b,a
        compare (order a) (order b)

let raiseBy amount (p1 : Player, p2 : Player) = p2.pot + amount

let deck = [|King; King; Queen; Queen; Jack; Jack|]
let sample_card mask = Sampler.sample deck mask

let init () : Model * (ActionPicker * RewardForPlayerOne) =
    let mask = 0UL
    let c,mask = sample_card mask
    let p1 : Player = {id=0uy; card=c; pot=1}
    let c,mask = sample_card mask
    let p2 : Player = {id=1uy; card=c; pot=1}
    {p1=p1; p2=p2; raises_left=2; table_card=ValueNone; mask_desk=mask}, ({is_fold=false; is_raise=true}, 0.0f)
```

Here is the initial part so far.

Let me do the update next.

```fs
let init () : Model * (ActionPicker * RewardForPlayerOne) =
    let mask = 0UL
    let c,mask = sample_card mask
    let p1 : Player = {id=0uy; card=c; pot=1}
    let c,mask = sample_card mask
    let p2 : Player = {id=1uy; card=c; pot=1}
    {p1=p1; p2=p2; raises_left=2; table_card=ValueNone; mask_desk=mask}, ({is_fold=false; is_raise=true}, 0.0f)

let update (model : Model) (msg : Action) =
    match msg with
    | Fold ->
        failwith "TODO"
    | Call ->
        failwith "TODO"
    | Raise ->
        failwith "TODO"
```

This is so lame. Instead of that action picker, I can just derive the list from state.

5pm.

```fs
type ActionPicker = { is_fold : bool; is_call : bool; is_raise : bool }
let actions_allowed (model : Model option) =
    match model with
    | Some model -> {is_fold=model.p1.pot <> model.p2.pot; is_call=true; is_raise=model.raises_left > 0}
    | None -> {is_fold=false; is_call=false; is_raise=false}

let actions_array (x : ActionPicker) = [|
    if x.is_fold then Fold
    if x.is_call then Call
    if x.is_raise then Raise
|]
```

I'll move it to a different file later.

Actually instead of this, I really should be using masks.

https://stackoverflow.com/questions/38938911/portable-efficient-alternative-to-pdep-without-using-bmi2

Agh, I should have just transcribed this.

6:25pm. This is ridiculous. I am deep in thought, thinking about the design of Leduc.

6:35pm. Both the way I did it last time, and the way I wanted to push into this time is bonkers.

There is no way the MVU pattern is the right choice. There is no way that what I had is the right choice.

Instead, what I need to do is take in the `game` and pass it an interface with the `choice`, `action`, and `terminal` members. I need to CPS it. That would be an efficient design I could use on AI chips in the future.

But what I've realized is, that this interface would be native to this particular game.

In order to make it usable in learning algorithms, what I would do is compose that game native interface in something else that I could pass to generic learning algorithms.

I can see a hierarchy.

What I've done in `ui_holdem` is squish it all together.

Agh, what was I thinking?

7:05pm. Ok, I think I get everything. I am going to deal with Leduc tomorrow.

I see how I am going to do the learning algorithms as well.

game -> lrn -> game -> lrn

There is a mutually recursive relationship where the game interface calls the learning interface and so on.

7:10pm. Let me go get lunch.

I have a feeling in the abstract for how it should work, but the feeling eludes me. I get the feeling that I knew all of this, but it faded from my memory. I'll figure it out as I go into it.

Remember how long and hard I thought about CPS and recursion? Remember the Y combinators and how hard I found them?

I have that power and understanding. I am sure that the knowledge will come back to me when the time is right to make use of it.

8:10pm. Let me close. I didn't exactly do too much today. Tomorrow, I am going to deal with the game, unless the mic arrives.

...The parcel is still not in the system. I guess it won't get here anytime soon then.

Let me chill. I'll give Succubus & Hitman a try."

---
## [i574n/The-Spiral-Language](https://github.com/i574n/The-Spiral-Language)@[574085ea6a...](https://github.com/i574n/The-Spiral-Language/commit/574085ea6a497fa07eeea98b129240b2c5cdd53b)
#### Thursday 2023-04-06 23:24:53 by Marko Grdinić

"https://app.otta.com/

Somebody posted this job site in a /twg/ thread.

https://app.otta.com/jobs/TkVialpD

I'll definitely keep this job portal in mind. Nevermind it for now.

9:15am. Damn, how is it so late?

My mental exhaustion is at its peak.

10:10pm. I am going to bed. I'll skip dinner.

2/22/2023

9:20am. I am up. I was overloaded last night and I had a lot of trouble falling asleep. I am actually considering skipping work entirely for the day, but I do not want to. I want to mess with the header right now, I want to understand why align contents shrinks them. Yesterday I was too tired, but it is eating away at me.

9:25am. I have a strong contrarian streak. When I push myself to work I want to laze, but when I push myself to laze, I want to work, so let me do the later. I am too tired for manga, so let me do some HTML.

I feel like I could understand it better if I go through this.

https://youtu.be/UuiImHywwvs
Align Items vs Align Content in Flexbox

Let me watch this. I do not understand the difference between these two.

https://youtu.be/UuiImHywwvs?t=4

Oh also, this is how calc is used? Interesting.

https://youtu.be/UuiImHywwvs?t=50

Huh, what is he doing here?

https://youtu.be/UuiImHywwvs?t=55

Oh, it is some Emmet thing.

https://youtu.be/UuiImHywwvs?t=245

Hmmm, I see. I couldn't figure out the why align content was doing nothing for the simple reason that I never had items on the same column.

https://www.w3schools.com/cssref/css_units.php
* Pixels (px) are relative to the viewing device. For low-dpi devices, 1px is one device pixel (dot) of the display. For printers and high resolution screens 1px implies multiple device pixels.

I am skeptical of this. I'd prefer to make my site resolution independent, but when I use px, it definitely isn't. I do not understand this exactly.

///

Tip: The em and rem units are practical in creating perfectly scalable layout!
* Viewport = the browser window size. If the viewport is 50cm wide, 1vw = 0.5cm.

///

https://www.w3schools.com/cssref/css4_pr_accent-color.php

This is a really good site.

10:10am. https://www.youtube.com/results?search_query=css+max-content

Let me watch some of these.

10:20am. https://youtu.be/DM244V9KvNs?t=432

I am distracted, but knowing this is pretty useful.

https://youtu.be/DM244V9KvNs?t=472

Oh, you can do something like this?

https://youtu.be/DM244V9KvNs?t=491

I just realized - you could probably get the arraying behavior with flex wrap. Nevermind that for now.

https://youtu.be/-st14lUQD3U
CSS width auto vs 100% | What's the difference?

Let me watch this as well.

https://youtu.be/-st14lUQD3U?t=57

> If you have a margin left and margin right on auto, it is automatically centering it.

Hmmm, really?

10:25am. That was pretty informative.

https://youtu.be/IWFqGsXxJ1E

Let me take a look at this.

...No forget it, I do not feel like watching that.

10:30am. Let me get back to layouting.

I want to redo the search bar part as it is too hacky.

https://stackoverflow.com/questions/29470676/why-doesnt-the-input-element-respect-min-width

Let me try this.

11:10am. Ok, that figures that.

...I am satisfied for now. Let me watch more of the course.

https://youtu.be/G3e-cpL7ofc?t=14427

11:30am. Tried redesigning the middle section so it has a nested container, but it was too complicated. Forget it. Let me just watch the video.

https://youtu.be/G3e-cpL7ofc?t=15418

He should have used an extension.

11:50am.

```fs
let inline img x = Html.img [prop.src (importDefault x)]

let header =
    Html.div [
        prop.className "header-box"
        prop.children [
            Html.div [
                prop.className "home-box header-item"
                prop.children [
                    img "./svgs/svgexport-5.svg"
                    ]
            ]
```

Agh. It seems let inline does not compose with other such statements in Fable.

https://youtu.be/G3e-cpL7ofc?t=17047

Huh, you can do it like this?

12:25pm. This is amazing. I would never have figured this out myself.

12:45pm. https://developer.mozilla.org/en-US/docs/Web/CSS/flex-basis

Oh, wow this exactly what I wanted. I could put in those padders and have them shrink.

https://stackoverflow.com/questions/54654050/difference-between-flex-end-and-end

Ah, I see.

1:10pm. https://stackoverflow.com/questions/67858284/how-to-have-one-item-shrink-fully-before-another-starts-to-shrink

Damn it, let me stop here. I am going crazy. flex-basis is a great thing, but for some reason the search bar is always being shrunk more than than the padders. How annoying.

I can't figure out how to have it prioritize shrinking one of the empty spaces first.

https://youtu.be/G3e-cpL7ofc?t=16529

1:15pm. Let me stop here. At this point I am not even watching the course, but doing my own research. I should just finish the rest of it, and move on. I already know quite a bit of layouting. Let me do the chores here.

2:40pm. Done with breakfast and chores. Let me resume the video. Today I won't strain myself till 8pm like yesterday.

https://youtu.be/7khSaA91e04
Creating squishy padding and margin that adapt to the viewport

Let me watch this first.

3:10pm. https://youtu.be/G3e-cpL7ofc?t=17719

I do not like this method at all.

3:30pm. https://developer.mozilla.org/en-US/docs/Web/CSS/Attribute_selectors

So you can match attributes in CSS. I see.

Focus me. Let me go back to the tutorial.

https://youtu.be/G3e-cpL7ofc?t=18825

Oh this could be useful.

3:50pm. https://youtu.be/G3e-cpL7ofc?t=20028

I haven't exercised the positionings, but they are each to grasp.

Let me just go forward through the video.

https://youtu.be/G3e-cpL7ofc?t=20854

I need to remember that the two are reversed when I use column.

https://youtu.be/G3e-cpL7ofc?t=21225

I wonder if I chould position these boxes using `top: 100%`. it wouldn't surprise me if that were possible.

https://youtu.be/G3e-cpL7ofc?t=21379

I had no idea it was possible to nest classes like this.

https://youtu.be/G3e-cpL7ofc?t=21475

Let me give this a try. Forget the sidebar, but I want to see if top:100% would work.

```css
.search-bar-magni-glass-box .tooltip {
    display: none;
    position: absolute;
    background-color: gray;
    color: white;

    top: 100%;
    left: -10%;
    right: -10%;
    text-align: center;
}

.search-bar-magni-glass-box:hover .tooltip {
    display: inline;
}
```

It works really great. Let me resume the video.

https://youtu.be/G3e-cpL7ofc?t=21507

Come to think of it, he realy doing the beginners a disservice by using pixel measurements everywhere.

https://youtu.be/G3e-cpL7ofc?t=21530

Not a good method. You really want to also disable the tooltip when it is not being hovered. Otherwise it might be possibel to select it even when it not ostensibly visible.

https://youtu.be/G3e-cpL7ofc?t=21686

Actually, this was a better solution than I gave it credit for. It is not possible to select the text when it is like this.

...Actually, if I do Ctrl+A to select everything on the page, and then paste it into a text file, I do see the qwerty. I see.

But this isn't a problem.

https://youtu.be/G3e-cpL7ofc?t=21784

I'll definiltey forget about this property, but nevermind it. A search will do.

https://www.w3schools.com/cssref/pr_text_white-space.php

> 	Whitespace is preserved by the browser. Text will only wrap on line breaks. Acts like the <pre> tag in HTML

Hmmm really?

```fs
        Html.pre [
            // prop.style [
            //     style.whitespace.
            //     ]
            prop.children[
                Html.text "qwe              "
                Html.br []
                Html.text "asd "
                Html.br []
                Html.text "zxc "
                ]
            ]
```

Ok, I'll definitely remember this. I thought it was impossible to get HTML to preserve whitespace, but it turns out it is pretty easy.

4:35pm. https://www.justetf.com/en/etf-profile.html?groupField=none&sortField=sixMonthReturnEUR&sortOrder=desc&from=search&isin=DE0006289309#chart

I peeked at the market and I see QQQ is dumping again. I thought for a moment - I must be wrong, better get out, but then remembered that my recommendation on Feb 3rd was not to buy tech stocks, but european banking stocks. Hypothetically, had I gone long that instead of losing 5%, I'd be up that amount right now! What about Turkey?

https://www.justetf.com/en/etf-profile.html?groupField=none&sortField=sixMonthReturnEUR&sortOrder=desc&from=search&isin=IE00B1FZS574#chart

My sense given the huge bad news is that it is acting extremely bullish. If stocks wanted to go down, they wouldn't be whipping around like this, giving people a chance to get out, they'd just dump! My Feb 3rd timing wouldn't have been good though.

4:45pm. Nevermind this, let me watch to the end of the HTML course.

https://www.justetf.com/en/etf-profile.html?groupField=none&sortField=sixMonthReturnEUR&sortOrder=desc&from=search&isin=IE00B1FZS574#chart

Finally, time for the last lecture. I am barely awake here.

I am only holding on thanks to my iron will. I am going to be sleeping well tonight.

https://youtu.be/G3e-cpL7ofc?t=22420

Instead of doing it like this, it would be better to just maybe adjust the font size of the root items. Assuming one is using relative measurements, that would smoothly propagate the changes. I wonder if one could also use it to set variables.

And instead of adjusting the grid sizes like this, it would be better to just use flex boxes with wraping.

Come to think of it, there are resolution agnostic apps. You know those annoying ones that don't change size when I zoom. Though I am betting those use viewport measurements. I do not like those. I won't use them in my own frontend work.

5:20pm. I am done here. Finally done with the HTML course. Now I know enough to be effective. I can go back to the React course.

Not right now though.

5:30pm. Studying really is hell, but learning new things is satisfying at some level at the same time.

This material is just like I imagined it to be. Not at all difficult to master, but it takes some effort to go through the tedioum of actually learning it.

5:35pm. I just need React, and I will be set as far as webdev frontend work is concerned. After that I'll be able to focus on the backend work.

I need to boild of my councurrent programming foundation and attain the skills that I can actually use to make money in the market.

I said I would bluff on the resume, but there is no need to go that far. Instead what I need is to actually put the requested tech in the job posts on my resume. If that fails, then that I can take as a signal to mess around with my state experience.

The poor response rate is part in due to the market, partly due to representing myself as a hobbyist, partly due to not have the requisite tech stack skills on the places I am applying to.

I'll deal with the cases one by one.

In the worst case, I can apply to those places that only give out equity. I'll see how things go.

Even if the job market might be poor, I doubt many people are interested in working at startups that pay monopoly money.

I am going to have my revenge at places that rejected me by getting a far higher paying job than those. There is also A Team to consider.

Right now, though I am filled to the brim with work. I need to go through my studies first."

---
## [i574n/The-Spiral-Language](https://github.com/i574n/The-Spiral-Language)@[aaa4821373...](https://github.com/i574n/The-Spiral-Language/commit/aaa4821373c261f5d428e2cb0582db141af23aaf)
#### Thursday 2023-04-06 23:24:53 by Marko Grdinić

"9:15am. I woke up early and lounged in bed, but I slept soundly tonight. I am much more rested that I was yesterday.

9:20am. https://boards.4channel.org/a/thread/249303252/one-punch-man-chapter-180-translated-is-here

Let me read this and then I will resume the React course. Any emails?

9:35am. A bit on the issue I opened in Feliz. OPM.

9:50am. Let me start.

https://youtu.be/bMknfKXIFA8?t=7265

I was here last time.

Let me start up the project.

https://developer.mozilla.org/en-US/docs/Web/CSS/box-sizing

I am going to have to get used to googling CSS properties. Yesterday I tried playing with HTML tags. If I put something like `qwe` which can't possibly be built in as the attribute name, that actually isn't an error. It just get interpreted as an inline element. That explains what those 'special' Youtube tags were.

Ok, I refreshed my memory of the React project.

Since I was doing the HTML course in React from the start I have a good basis to continue from.

https://youtu.be/bMknfKXIFA8?t=7237

Oh, is the goal to make something like this.

Actually, let me chill just a bit more. I feel distracted.

10:25am. Let me start for real here.

Let me implement this thing on the screen. I could do it better than the guy himself.

11:15am. Now I am getting bogged down in some flexbox issue.

11:25am. I figured it out. It turns out that just setting the max width on an image without also setting the min width can be a bad idea! By default min-width is auto which causes issue when I narrow the viewport. I found it really weird how the text on the right side would overflow the title. I get it now.

https://developer.mozilla.org/en-US/docs/Web/CSS/flex

Hmmm, what is this?

12pm. https://stackoverflow.com/questions/8543859/css-vertical-alignment-text-inside-li

I get autistically stuck on some issue sometimes, and this is one of those cases.

https://youtu.be/bMknfKXIFA8?t=7237

You know what? Fuck this. Let me just watch the course. I can't get a satisfactory solution. The flexbox one causes the discs to disappear.

Let me just place the logo.

12:15pm. Gah, I can't figure out how to change the color. Or how to set the Z indexes succinctly...

11:20am. I figured it out, but the solution is not good enough. Let me just watch the video.

https://youtu.be/bMknfKXIFA8?t=8147
> At least at this time, when I was researching, I could not find a good way to realign these.

Yeah. I spent a lot of time on this today as well.

https://youtu.be/bMknfKXIFA8?t=8256

Ah, I see. It didn't occur to me at all to add it as a background image.

```
.main {
    position: relative;
    display: flex;
    flex-direction: column;
    background-color: hsl(0, 0%, 25%);
    padding: 1em 2em;
    min-height: 30em;

    background-image: url("./assets/react-logo.svg");
    background-repeat: no-repeat;
    background-position: calc(100% + 15em) center;
    background-size: 30em;
    background-blend-mode: luminosity;
}
```

Oh, I figured out how to add this stupid thing!

Like so.

1pm. https://youtu.be/bMknfKXIFA8?t=8656

Let me pause here. It is time for breakfast.

I just got word from the Valora guy. He sent me some links. Maybe with his recommendation, I'll actually get an interview opportunity.

1:45pm. Done with breakfast and chores. Let me just read the two chapter of Destiny Unchain and then I will apply to Valora.

Let's take it easy.

2:40pm. Let me resume. It is time to apply to Valora.

https://en.valora.career/job/zurich/software-engineer-fullstack/29368/45005687568

It is this thing here.

2:55pm. I applied. I also checked and programmer salaries in Swis are quite strong, about 7x of what they are in Croatia.

Anyway, that is that. I should at least not get my resume thrown straight into the trash in this place.

Now, instead of resuming the React course here, let me follow up on that Feliz issue. First let me try out the template.

https://github.com/dotnet/fsharp/issues/

Opened issue 14792.

3:10pm. Now let me resume the React course.

https://youtu.be/bMknfKXIFA8?t=9065
> If you are already feeling very confident in styling in React, I will give you permission to skip the next few screencasts.

I guess I'll be skimming the following sections.

3:45pm. Resolved that apostorphe error. It will be fixed in the upcoming version of Ionide, and it has already been fixed VS 17.5. I upgraded and tested it myself and see that it works.

https://youtu.be/bMknfKXIFA8?t=11643

Oh so that is how the props work on the JS side.

4pm. https://youtu.be/bMknfKXIFA8?t=12724

I am just skimming this stuff as it is super obvious. This is pretty much how Blazor components work. With CSS and HTML components on the other hand I needed to do some memorization and playing around in order to get used to how they work.

I should be able to finish the tutorial a lot sooner than I thought. Let me just continue skipping it.

4:15pm. https://youtu.be/bMknfKXIFA8?t=17108

I'll want to focus on this for a bit.

https://youtu.be/bMknfKXIFA8?t=17658

Oh, you can do the grid template like this.

https://youtu.be/bMknfKXIFA8?t=17677

I am not familiar with this CSS.

https://youtu.be/bMknfKXIFA8?t=17773

Oh this CSS property would have been good for the search bar. Instead I've been padding it.

4:30pm. https://www.terluinwebdesign.nl/en/css/flexible-padding-for-buttons/

Let me pause a bit, I need to learn about flexible marking and padding.

https://developer.mozilla.org/en-US/docs/Web/CSS/::before

Ah, I see. I could use this for the list item attributes.

4:40pm. Oh, right. I need to thank the guy for refering me.

4:55pm. I see now that I got his surname wrong and forgot to note his department despite him suggesting it to do so.

I am such a fool. My clumsiness will be the end of me.

Instead of being flexible about it, I just decided to do it. Assuming this causes the Valora application to fail, this is the reason why I'll be failing interviews in the future.

Forget it, let me just resume the course.

https://youtu.be/bMknfKXIFA8?t=18742

Hmmmm....

This key thing. I do not think that in the Feliz library I have that. Should I be setting that? I'll look into it in the future, nevermind it for now...

https://youtu.be/bMknfKXIFA8?t=19129

Let me pause here and I will look at the attribute. It is not goot to put things off.

https://reactjs.org/docs/lists-and-keys.html

Ok, this is easy. It does about what you'd expect.

I do not need to worry about this.

5:35pm. https://youtu.be/bMknfKXIFA8?t=19958

In the end it will turn out that CSS was harder than React.

https://youtu.be/bMknfKXIFA8?t=20994

Any reason why this is so?

https://youtu.be/bMknfKXIFA8?t=21180
> If you were to run two state setter functions back to back. The way react handles it, maybe or may not run one of them before the other. I see.

Ok, I get it. It seems that just grabbing the regular value might cause sync issues due to batching.

5:40pm. https://developer.mozilla.org/en-US/docs/Web/CSS/:root

<html> is the root element it turns out.

I could set it like this.

https://youtu.be/bMknfKXIFA8?t=21683

These things are super simple, I do not feel like doing them even though I've felt like doing the HTML/CSS lessons.

5:50pm. Let me just keep going forward. I am past the halfway mark. I'll aim to finish the course soon, so I can start work on my own things. In addition to that, I want to further study backend development and the way ASP.NET firmware works. Not to mention, refresh my memory of HTTP requests, and set up a REST API. Everyone seems to be asking for that so I should put it on my resume somewhere.

5:55pm. Took a short break. Focus me. Let me just go at it for 10m more. This time of the day is really just about time for me to finish.

6:10pm. https://youtu.be/bMknfKXIFA8?t=25450

I skipping ahead really strongly. I am 7h in already. But this stuff is really piece of cake programming.

Right now, I've realized I've forgotten how to do nested Elmish components...wait, I think I see it, nevermind. I'll figure it out right away when the time comes to practice. Let me go forward even more.

...Lunch time.

6:40pm. Done with lunch. Let me just watch a bit more of the course and then I will be done.

6:45pm. https://youtu.be/bMknfKXIFA8?t=25778
> You probably don't need derived state.

https://youtu.be/bMknfKXIFA8?t=26050

I am guessing he'll use partial application.

https://youtu.be/bMknfKXIFA8?t=26188

Sigh, I was in the right direction, but his solution is more complicated than what I had in mind.

https://youtu.be/bMknfKXIFA8?t=26361

Imperative programmer trying do functional one. He should have just used a map.

https://youtu.be/bMknfKXIFA8?t=26471

Rather than using a reactive variable that has an array, it might have been better to instead have an array of reactive variables.

https://youtu.be/bMknfKXIFA8?t=26660

Now he is doing it properly.

7:05pm. https://youtu.be/bMknfKXIFA8?t=27616

I am too tired to go on anymore. 7:40h out of 11:55h into it. I've been going through it at fast forward today, that is why I managed to cover 5.5 hours in one sitting. Tomorrow, I will completely clear how React works on move on to the next thing.

To think, it is this simple.

What I have to do next is really set my sights on mastering backend frameworks like ASP.NET. After I understand those, I will have zero trouble handling any kind of pro work in the future.

7:10pm. Tomorrow. I just have to pay my dues tomorrow and I am done scrambling for how to do web frontend work.

I am going to make it happen. I'll get the skills and I will get the money. If not Valora, it will be something else. I need to be determined to do whatever is needed. I have the choice of a niche, in which case I will pick .NET. I do not need many of them. I just need one that is well paid, and I will be set.

I won't give up. I'll continue to push forward.

But for now let me chill. I've been putting off Machimaho, and it is time for some fun. Let's hope I can sleep well tonight."

---
## [i574n/The-Spiral-Language](https://github.com/i574n/The-Spiral-Language)@[856411d0eb...](https://github.com/i574n/The-Spiral-Language/commit/856411d0ebd88afa81f2f4ae5f74078228ddd287)
#### Thursday 2023-04-06 23:24:53 by Marko Grdinić

"8:15pm. https://hibox.live/elixir-for-humans-who-know-python

///

The first age of web development was static files served through a webserver. It was new, exciting, chaotic and fun, but very primitive. Most of you are probably too young to remember this era by now.

The second age of web development was in languages like Perl, PHP, Ruby and Python, where a client sends HTTP requests to URLs, and the server returns dynamic content rendered as a static resource. This was a very fun era to be a developer, but applications were limited in how complex and featureful they could be, and there were a fair inefficiencies from re-sending a whole page just to reflect a single updated value.

Live Apps combine the best of two worlds, enabling developers to build complex, dynamic applications without the need for any JavaScript or a dedicated API. A client requests an initial page load, which the server renders and maintains a local understanding of, and then makes a follow-up request to establish a WebSocket connection. Client side interactions with the application are then passed through the WebSocket and changes to the state are returned and the DOM is dynamically updated accordingly, without any API interaction or custom JavaScript required, as all of the logic is kept on the server-side.

///

Websockets?

9:20pm. https://desu-usergeneratedcontent.xyz/g/image/1677/26/1677261525409.jpg

///

>27
>neet
>no degrees
>never worked
>get help and dig myself out of depression
>start to learn coding because that's the only thing worth I can learn from home and it's fun.
Alternative is 3 year training by a school for retards and mentally ill to become a office clerk or gardener.
Maybe I should get my HS diploma and go to university, but that doesn't fix my problem of having literally years of blank space on my resume.

Should I just get really good at coding and fake my resume? Maybe it's truly おわりだ for me..

///

///

>>91740098
I asked Gigachad for you anon, remember that an literal AI will give you better answers than anyone on /g/. Now get the fuck out of my thread and start learning nigger.

///

Here is the image.

> Gigachad c.AI
> Get good enough at coding to show real results by creating a portfolio of projects. Then use those achievements to demonstrate your skills to potential employers without needing to use your resume - your work will speak for itself. This is the way, my brother.

Chatbots these days sure are great.

2/26/2023

9:40am. Let me check my mail.

9:45am. I've been getting some weird trolls lately.

Damn I am groggy. Let me read Kaiji and then I will get started on the SQL basics course. I need to figure out foreign keys. When Teddy explained them, they made sense, but then he started adding those collections and I am confused again.

Yesterday I got a grasp on how to connect to the SQL Server. I have verified that there is only a single server process that my client application connects to in the background.

Why was even something trivial like this confusing. Because I have like a dozens of old servers in the program list. Let me get rid of them.

9:50am. All cleaned up now. I only have the SQL Server 2022 stuff installed now.

https://mangadex.org/chapter/c0005ec5-40a2-4351-a7c5-24805dc4c074/24

Loooooooooooooooooollll. Old men are the best after all.

10am. Enough fun. Let me watch the SQL Server course.

Since I hadn't gotten any word from Valora at this time, can assume this is a dud? I don't know. I applied on the 23rd. 3 days is not too much, but if I do not get anything in another 1.5 weeks, I'll forget about it.

https://youtu.be/9Pzj7Aj25lw
Learn SQL in 1 Hour - SQL Basics for Beginners

Here is the one by Joey Blue. It is only 1h, so let me go for it.

https://youtu.be/9Pzj7Aj25lw?t=213

I see him having all these servers. I wonder how it is possible to rename it.

11:55am. Done with the course. It was pretty basic, but informative. This is the first time I've touched SQL. I find a syntax a bit confusing, but that is a matter of simply memorizing the relevant stuff. I can just Google it in the heat of battle. The biggest gain today and yesterday is my improved familiarity with SSMS. If I ever do SQL on a job, that should be convenient.

12pm. At this time I do not feel the need to learn more SQL.

What I really need to understand though is how EF and the...

Well, I suppose I could do a special record in SqlFun for joins, but I'd be better off just asking the author if it comes to that. It doesn't really matter right now. With ADO.NET if I go down that route, I can just use indexes to fetch everything back as a tuple.

12:05pm. This is a great time to stop and have breakfast.

Today I said that I had no email, but I wouldn't usually get anything on a Sunday anyway. I have no concepts of weekends in my personal life. I guess that will change when I get a job.

The next thing on the agenda is to get back to the Web API course and see it all the way through. I think I'l get a handle on foreign keys and relations in EF by the end of it.

I do not really care that much about SQL and databases, but I want to understand at least this much.

...Ah, come to think of it.

https://jacentino.github.io/SqlFun/Transforming-query-results

Hmmm, no inner joins here.

Nevermind that.

12:15pm. Let me commit here. There is no point in wondering about this. Just go through the EF course next and you are done with databases."

---
## [i574n/The-Spiral-Language](https://github.com/i574n/The-Spiral-Language)@[494d4d9c32...](https://github.com/i574n/The-Spiral-Language/commit/494d4d9c3246890928ae0ac296d949b59b16db22)
#### Thursday 2023-04-06 23:24:53 by Marko Grdinić

"1:55pm. Done with breakfast. Time for a bit of chill and then I will start dealing with the Web API tutorial.

2:25pm. Let me go back to Teddy's course.

Damn, I am tired. It is very difficult to get back to sleep once you get up in the middle of the night.

```cs
public decimal GetPokemonRating(Pokemon pokemon) => pokemon.Reviews.Average(x => (decimal)x.Rating);
```

I think this is what was giving me trouble. Let me fix it.

2:35pm.

```cs
public decimal GetPokemonRating(IQueryable<Pokemon> pokemon) => pokemon.SelectMany(x => x.Reviews.Select(x => (decimal)x.Rating)).Average();
```

I am not sure whether this will compile to valid SQL, but let me give it a try.

What did Jasper say about ModelState? I forgot.

```
        [HttpGet("{id}")]
        [ProducesResponseType(200, Type = typeof(Pokemon))]
        public IActionResult GetPokemon(int id)
```

Instead of returning this, I should return a typed `IActionResult`.

...Hmmm, it does not have a type.

2:55pm.

```cs
        [HttpGet("exists/{id}")]
        public ActionResult<bool> PokemonExists(int id)
```

Wow, I can't believe that I just had to do a single case and the autocomplete suggested a refactoring for the rest. Do I have Copilot on or something?

```cs
        public decimal GetPokemonRating(int id)
        {
            var x = ctx.Pokemons.Where(x => id == x.Id).SelectMany(x => x.Reviews.Select(x => (decimal)x.Rating));
            var n = x.Count();
            return n > 0 ? x.Sum() / n : 0;
        }
```

I do not like this implementation. But let me give it a try.

3:35pm.

```cs
        public decimal GetPokemonRating(int id)
        {
            var reviews = ctx.Pokemons.Where(x => id == x.Id).Select(x => x.Reviews.Select(x => (decimal) x.Rating)).First();
            try { return reviews.Average(); } catch { return 0; }
        }
```

I keep rewriting this thing trying to find the optimal form. It should be done like this.

3:45pm. Let's stop messing around. Let me watch Teddy's tutorial again.

https://youtu.be/K4WuxwkXrIY?list=PL82C6-O4XrHdiS10BLh23x71ve9mQCln0

Teddy explains the model state here.

3:55pm. https://youtu.be/bSvYErXVRtQ?list=PL82C6-O4XrHdiS10BLh23x71ve9mQCln0
ASP.NET Core Web API - 7. GET & Read Methods [PART 2]

I really don't have much patience today. Let me just skim the rest. I get all of this.

https://youtu.be/bSvYErXVRtQ?list=PL82C6-O4XrHdiS10BLh23x71ve9mQCln0&t=819

This is the kind of work you'd need to pay me to do.

4pm. I do not feel like watching the rest. I do not need anymore than this. I get the basics of it. I am just too tired right now to mess with it.

How about those http and networking courses.

https://www.youtube.com/watch?v=qiQR5rTSshw
Computer Networking Course

> It will prepare you to configure, manage and troubleshoot computer networks.

https://youtu.be/qiQR5rTSshw?t=55

...I am already bored by this. Let me just give it a few minutes and then I'll check out the http course.

...Forget it.

https://youtu.be/iYM2zFP3Zn0
HTTP Crash Course & Exploration

I already watched this once back in 2020. This is more along the lines of what I'd want.

https://youtu.be/2JYT5f2isg4
Full HTTP Networking Course – Fetch and REST APIs in JavaScript

This is the one I linked to earlier.

> At the end we'll build a web crawled in JS from scratch.

This could be interesting.

4:10pm. I am thinking. The course is a bit interesting, but I am not going to be doing the exercises. I think I'll watch it for an hour and then leave it aside.

I'll make use of Teddy's project as a reference. I do not want to write more C# for my personal projects. Instead since F# has the migration tools, I'll give them a try. Alternatively, I'll write just the database segments in a separate C# project. Either way is fine for me.

...In the C# project, all I really need are the models and the context class. Everything else should really be done in F#.

4:20pm. https://youtu.be/2JYT5f2isg4?t=425

This isn't too bad, but yeah...it is time to start.

https://www.youtube.com/playlist?list=PLUOequmGnXxOgmSDWU7Tl6iQTsOtyjtwU
ASP.NET Core 2.2 & 3 REST API Tutorial

I am looking at this, and he goes through it in significant detail, a lot more than Teddy.

https://youtu.be/2JYT5f2isg4?t=512

This course is more interactive than I thought.

4:35pm. Nevermind that JS course. Let me watch the crash course for a bit.

https://www.youtube.com/playlist?list=PLillGF-RfqbYeckUaD1z6nviTp31GLTH8
Programming & Web Development Crash Courses

4:40pm. https://youtu.be/iYM2zFP3Zn0?t=595

Let me take a short break.

5pm. Let me resume.

5:05pm. https://youtu.be/iYM2zFP3Zn0?t=790
HTTP Crash Course & Exploration

Let me stop here. This is something I need to watch, but not right now.

I will crash at this rate. I am much more strained than I would usually be at this time.

I am tired!

Finishing off the EF Core videos was about how much I had in me. Plus I started an hour earlier than usual, so it is no wonder that I am so tired.

Right now I am thinking how I should resume the video that I started 10 days ago. I am going to recommend the CSS course and Jasper Kent's EF videos. Then I will dive right into the front end.

I am at my limit as far tutorials are concerned.

https://www.youtube.com/playlist?list=PLUOequmGnXxOgmSDWU7Tl6iQTsOtyjtwU
ASP.NET Core 2.2 & 3 REST API Tutorial

In this playlist there is knowledge I'll need on how to keep user state and how to log him in and such, but I do not need that right now. I'll leave that for when it comes to that. Tomorrow, I am going to get that basic HTTP course out of the way and start coding the frontend.

I was really missing knowledge of how to do the frontend and the acess the database.

Not going to get a job without those two. I've been right to apply, and apply honestly.

I can be mad at being rejected, but I need to be honest with how much of the stated requirements I actually meet.

I mean, if a job requires React and SQL, and similar database knowledge, I can't complain about being rejected for jobs that I applied to a month ago. If I have all the skills, and not getting calls, then I can bluff about my exp, or even try freelancing.

It is only now that I am really ready to start my first project. It should be fun.

I'll have to look at that Elmish.Bridge thing, as I want the server to be stateful for games.

I have all the pieces in my mind, I just need to bring them forth into code. I'll start that tomorrow, documenting every step of the way as I go along. In video as well!"

---
## [i574n/The-Spiral-Language](https://github.com/i574n/The-Spiral-Language)@[52670c0294...](https://github.com/i574n/The-Spiral-Language/commit/52670c0294e362dc6d8104490445da2e9ef492dd)
#### Thursday 2023-04-06 23:24:53 by Marko Grdinić

"2:30pm. Enough novels. Let me resume.

2:35pm. Where was I?

Let me resume the video. I spent too much time playing around in F#. Even so this is good exercise.

```cs
var builder = WebApplication.CreateBuilder(args);
builder.Services.AddDataProtection();

var app = builder.Build();

app.MapGet("/username", (HttpContext ctx) =>
{
    string v;
    return ctx.Request.Cookies.TryGetValue("auth", out v) switch
    {
        true =>
            v.Split(':') switch
            {
                ["usr", var usr] => usr,
                _ => "invalid user"
            },
        false => "not login"
    };
});
app.MapGet("/login", (HttpContext ctx) =>
{
    ctx.Response.Headers.SetCookie = "auth=usr:anton";
    return "ok";
});

app.Run();
```

I just can't get used to this.

https://youtu.be/ExQJljpj1lY?list=PLOeFnOV9YBa4yaz-uIi5T4ZW3QQGHJQXi&t=397

Huh, C# is smart enough not to get confused by the inner ""?

3:25pm. Focus me, get through that video. Stop looking at mics.

https://youtu.be/ExQJljpj1lY?list=PLOeFnOV9YBa4yaz-uIi5T4ZW3QQGHJQXi&t=1018

Let me try replicating this.

3:40pm.

```fs
    app.Use(Func<HttpContext,RequestDelegate,Threading.Tasks.Task>(fun ctx next -> task {
        return failwith ""
        })) |> ignore
```

It is really painful having to deal with C# overloads in F# code.

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

Now, I am not sure how to deal with the case where the branches get missed. I guess I should have been following the video exactly instead of getting snobby about it.

Nevermind this. Let me watch the video to the end.

https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/member-access-operators#null-conditional-operators--and-

Sigh, these nulls.

https://youtu.be/ExQJljpj1lY?list=PLOeFnOV9YBa4yaz-uIi5T4ZW3QQGHJQXi&t=1310

OO code. They missed the opportunity to use the ?? operator here, but might simply be for the sake of backwards compatibility.

https://youtu.be/ExQJljpj1lY?list=PLOeFnOV9YBa4yaz-uIi5T4ZW3QQGHJQXi&t=1317

How is he looking at the source for this?

https://youtu.be/ExQJljpj1lY?list=PLOeFnOV9YBa4yaz-uIi5T4ZW3QQGHJQXi&t=1463

He says that the server descripts the cookie information, but what is stopping anybody else from stealing that?

https://youtu.be/ExQJljpj1lY?list=PLOeFnOV9YBa4yaz-uIi5T4ZW3QQGHJQXi&t=1507

Where the hell is he getting the sources for this?

https://youtu.be/ExQJljpj1lY?list=PLOeFnOV9YBa4yaz-uIi5T4ZW3QQGHJQXi&t=1503

I really wish I could check out the source, but nevermind that.

4:20pm. Forget that, forget that. Let me just move on to the next video. The parts where he is showcasing the internals are losing me, but I can deal with it.

Maybe he just cloned the ASP.NET and is referencing it from elsewhere?

4:25pm. https://youtu.be/5NUCPJTbLWY?list=PLOeFnOV9YBa4yaz-uIi5T4ZW3QQGHJQXi
ASP.NET Core Authorization (.NET 7 Minimal Apis C#)

Let me move on to this. I asked him, so maybe I'll get an answer.

https://youtu.be/5NUCPJTbLWY?list=PLOeFnOV9YBa4yaz-uIi5T4ZW3QQGHJQXi&t=276

This is not hard to understand. It would take too much to write things out. I got hung up about cleaning his code and ran into some dead ends. Let me just watch the videos.

https://youtu.be/5NUCPJTbLWY?list=PLOeFnOV9YBa4yaz-uIi5T4ZW3QQGHJQXi&t=579

Ah, it is possible to wipe the cookie.

4:40pm. https://www.youtube.com/playlist?list=PLOeFnOV9YBa4LslgNo31ukBrwpJTz7BzM
Modern Web Development Series - ASP.NET Core, Nuxt, CI/CD, Cloud - Tricking Library

Damn this guy is badass. I was wrong. People shitting on web devs do not know what they are talking about.

https://youtu.be/5NUCPJTbLWY?list=PLOeFnOV9YBa4yaz-uIi5T4ZW3QQGHJQXi&t=634

So that is how you get the path.

https://youtu.be/5NUCPJTbLWY?list=PLOeFnOV9YBa4yaz-uIi5T4ZW3QQGHJQXi&t=779

Wait, wait, wait. Take a look at that IL Code mark on the top.

4:50pm. My conjecture right now is that maybe the Rider IDE he is using might be responsible for this capability.

https://youtu.be/TzZmq5V_c8U
This will make you a better developer

https://youtu.be/5NUCPJTbLWY?list=PLOeFnOV9YBa4yaz-uIi5T4ZW3QQGHJQXi&t=1116
> If you take the steps to open up these services and take a look at them.

///

I am watching ASP.NET tutorials on Youtube, and the host is somehow stepping into the ASP.NET sources for the various middleware as he explains them. He is using Rider and at the top of the methods it says IL Code, but the code shown is definitely the original C# source. How did he manage to set that up?

///

I decided to ask in the /wdg/ thread. I'll see if I get anything.

5:25pm. https://youtu.be/N_zVCCpnjXM?list=PLOeFnOV9YBa4yaz-uIi5T4ZW3QQGHJQXi

Let me put this on pause. I can only take so many authentication videos per day.

https://youtu.be/jApDthzDql0
What Kind of Mic Is BEST For YouTube? (All Budgets)

Let me watch this. Note that he is using a fancy mic.

https://youtu.be/jApDthzDql0?t=60

He sounds completely different using the camera mic.

https://youtu.be/jApDthzDql0?t=264

He is praising this particular mic.

https://youtu.be/jApDthzDql0?t=277

These are expensive!

He didn't compare it with a gaming mic. I've never actually used the one myself.

https://youtu.be/6Y237GWgo5E
Gaming Headset Or Microphone - Do You Need A Condenser Mic?

This guy just talks instead of showing.

https://youtu.be/BKOx4hZKmOs
Which Mic Type is Best for Zoom, Class, Recording 🎙️ 2020 | Headsets, Lavaliers, & Podcasting Mics

She starts with a laptop mic.

https://youtu.be/BKOx4hZKmOs?t=121

It does sound like an airplane pilot.

https://youtu.be/BKOx4hZKmOs?t=153
> My recommendation would be to go with something else if you have the choice.

I guess I could get a 100$ USB mic.

https://youtu.be/BKOx4hZKmOs?t=397

Oh this sounds really good, and it is cheap too.

https://youtu.be/BKOx4hZKmOs?t=424

She has some webcam recommendations.

Got a reply from Anton.

> Find Implementation keybind (usually F12)

///

​ @Raw Coding  That just gives me the type definitions in a metadata file. Have you done anything special to include the ASP.NET source files with your installation? Or is it a feature of Rider? I can see that all the methods you were showing have the `IL Code` descriptor on top, I am not sure what that is suppose to be.

Before I watched your videos I had no idea source peeking like you are doing could even be possible, I thought that if I wanted to see the source I'd have to go into the Github repo directly and check it out there.

///

Edit: It seems I forgot to send the above reply out.

6:15pm. https://www.youtube.com/results?search_query=usb+microphone

I can't take in any more of the programming videos. I am so distracted by this. It seems that tutorials I watched in the morning took up most of my energy. Let me take look at some mic videos.

6:40pm. https://stackoverflow.com/questions/49507450/net-go-to-implementation-of-a-nuget-package
> You should be able to do that with JetBrains Resharper.

https://github.com/dotnet/designs/blob/main/accepted/2020/diagnostics/source-link.md

...They are talking about Resharper. You know what, let me give Rider a try.

6:45pm. I still remember the time I gave Pharo a try fondly. Being actually able to look into those formerly inscrutable library functions would be a huge benefit to my learning.

https://youtu.be/o6IF9FcrOw8?t=598

I think I might very well just order this off Amazon.

https://www.nabava.net/mikrofoni/razer-seiren-mini-cijena-124280051

Maybe I could just get this Razer Seiren Mini. It is 55E. Or the Elgato Wave that costs twice as much.

7:10pm. Since it is Saturday, I can just buy it tomorrow and not have to worry about delays.

Let me try out Rider.

7:15pm. Oh, I see. It seems JetBrains has a IL to C# decompiler. I have to admit, the results were so good I thought it was the actual source.

https://devblogs.microsoft.com/visualstudio/decompilation-of-c-code-made-easy-with-visual-studio/

Not what I want.

7:20pm. Ok, I'll switch to Rider. If the license runs out, I'll pirate it.

Now let me close here. Tomorrow, I'll consult with my father and place an order. The mic should arrive in a week after that. What I want to do tomorrow is watch more of these videos

https://stackoverflow.com/questions/70893900/is-there-a-way-to-see-decompiled-c-sharp-code-in-vs-code

Wait...

> You can turn on the setting "Enable Decompilation Support", which is disabled per default. After turning that on, you should be able to see the decompiled code right away.

Let me give this a try in VS Code.

...Oh wow, it is really possible.

https://learn.microsoft.com/en-us/visualstudio/debugger/decompilation?view=vs-2022

How do I turn this on in VS_

https://devblogs.microsoft.com/dotnet/improving-debug-time-productivity-with-source-link/

https://devblogs.microsoft.com/dotnet/improving-debug-time-productivity-with-source-link/#enabling-source-link

Let me try this as well.

```cs
    public IServiceCollection Services
    {
        get
        {
            throw null;
        }
    }
```

What the hell. I just get code like this when I decompile in VS Code.

7:50pm. That thing I linked to is quite buggy.

https://youtu.be/VwyzxqLU_4o?t=89
.NET Decompiler and Reflection tools for Visual Studio Code

What is this? I am really putting in overtime now.

Oh, it is for an extension called the Powershell Pro Tools. It is a paid extension.

8pm. Ok, the VS Code efferings are shitty.

The VS Code decompiler doesn't work properly. Rider is really an amazing IDE to offer this. From what I can tell it will download the PDBs off Nuget.

In general, I am ambivalent about using VS Code vs VS or anything else, but decompilation is an amazing feature that puts Rider far above the other IDEs. I am definitely going to be switching to Rider.

Being able to peek inside libraries will make a huge difference in my understanding a year from now.

Especially for things like ASP.NET which is a huge black box. Rider gives me the option to open it up!

https://www.jetbrains.com/rider/buy/#discounts

There is a special offer for OS projects.

8:10pm. I tried applying for an OS license for my work on Spiral.

8:15pm. Let me close here for the day. I am really strained right now.

While there is no way that I'll just watch all the authorization videos by Anton from start to finish, I should watch a few more videos at least.

Especially now that I have Rider's decompilation. Also, the IDE is supposedly really good with F# too, so I am looking forward to that.

Ok. With every day that passes, I learn something new. One step after another, and I will get to a decent level.

My goal right now is to study more, finish the SignalR playlist and then go back to my own project."

---
## [i574n/The-Spiral-Language](https://github.com/i574n/The-Spiral-Language)@[d39c53f9e1...](https://github.com/i574n/The-Spiral-Language/commit/d39c53f9e19241bf3a67d51937279106f949d38a)
#### Thursday 2023-04-06 23:24:53 by Marko Grdinić

"https://youtu.be/PYCoRnJkn_c
C# Developer Career Path Guide (ZERO TO HIRED)

This guy is trustworthy. He says that C# is a boring business language, and that I am going to be working on boring things with it. He does say that the salaries are huge.

https://youtu.be/PYCoRnJkn_c?t=232
> These days Javascript is mandatory in any development discipline.

https://youtu.be/PYCoRnJkn_c?t=464

Now he talks about building apps. He says the app should have all the features that one should see in a corporate website.

https://youtu.be/PYCoRnJkn_c?t=562
> Stay out of machine learning. Stay out of data science.

https://youtu.be/PYCoRnJkn_c?t=660
> Employers aren't going to call you if you don't have unit tests.

https://www.youtube.com/watch?v=PYCoRnJkn_c
> Download a couple of Udemy courses on how to actually interview.

7:15pm. Who is smart? Who is stupid here?

I had no idea there are Udemy courses on interviewing. I guess that is something to think about.

7:25pm. https://jobs.ashbyhq.com/motion/4f5f6a29-3af0-4d79-99a4-988ff7c5ba05?utm_source=hn

Look at jobs like these. Just why couldn't I get them? No reason at all.

One last note, he mentions I should have a cool hobby like running and that this is one of the reasons why employers are crazy about him. Egh, nevermind that. Getting out of the house was only ever on the schedule once I get out of the house. But that is not going to happen. I am on the path of self destruction.

https://www.udemy.com/course/find-a-job-interview-skills-training-course/

Oh this is a free course.

https://youtu.be/7ZBiSyl9f_E?t=105
> Half these jobs do not even have applicants.

8pm. https://youtu.be/BDMh2evivzw
Self-Taught C# Developer Road Map 2022

Let me watch this as well.

https://youtu.be/BDMh2evivzw?t=158
> You can do backend if you want to, but I highly, highly recommend that you do full stack.
> Because it is going to be way easier to get a job.

https://youtu.be/BDMh2evivzw?t=186
> C# is notoriously difficult to learn.

Really? He keeps saying that, but I do not believe him.

https://youtu.be/BDMh2evivzw?t=310
> There is no Python jobs where I live.

https://youtu.be/BDMh2evivzw?t=481
> Don't spend too much time, learn the basics, move on...to C#.

https://youtu.be/BDMh2evivzw?t=639

If you think about how long this would take a beginner, I am making progress at a blistering speed.

This is exactly the route I want to take, and he is pushing me in that direction. I really do want to add some knowledge about networking because I feel like an idiot when it comes to http requests and similar kinds of protocols.

Let me just take the time to do this properly. Taking an extra month to learn all of this and build up my portfolio.

https://youtu.be/BDMh2evivzw?t=785
> Focus Entitiy framework, stay away from MongoDB, and stay away from any type of fancy database.

https://youtu.be/BDMh2evivzw?t=907
> If you can build an app like that, you don't need a college degree, you don't even need any work history.

Huh, really? Ok, I'll give this a shot. I thought I might need to mess on the resume, but if a good app or two is enough.

https://youtu.be/BDMh2evivzw?t=929
> Is it going to be really difficult to make that app? Yes, but if...

Bullshit. This will be piss easy.

What this guy is saying is a good reality check for me. Right now I am feeling cursed, but if all I need is a good web app to get a good job, then that is a really easy goal to meet.

I am basically crazy right now. I feel like nothing is going right, that no matter what effort I make I can't meet my goals. That even if I do all this, I won't be able to achieve anything. But that can't be it.

I know that thanks to all the effort I put in, my programming skill should be remarkable.

https://youtu.be/BDMh2evivzw?t=1054
> You don't need to learn CSS all that much. You can get away with the Bootstrap framework.

https://youtu.be/BDMh2evivzw?t=1072
> I have a whole entire video on how to create a resume.

I am going to check it out in the future.

https://youtu.be/BDMh2evivzw?t=1155
> After the first year is when you start making crazy amounts of money.

He says that the first job is going to be crappy.

8:35pm. Ok, let's leave it at this. I'll follow the path outlined here. I am not going to be applying to any more jobs until I have everything set. I'll get my portfolio done, get the webdev skills that I need.

I won't pin too much hopes on the Valora F# job. That kind of depends on whether those people recognize my ability simply on the strength of the Spiral language project. And if my previous rounds are any indication, nobody cares.

I'll go the classical route as it will be so easy for me. Right now, I am already OP in terms of programming skills, I just need to reach out a bit and acquire the skills people are willing to pay for.

http://pythonnet.github.io/

> Python.NET (pythonnet) is a package that gives Python programmers nearly seamless integration with .NET Framework, .NET Core and Mono runtime on Windows, Linux and macOS. Python.NET provides a powerful application scripting tool for .NET developers. Using this package you can script .NET applications or build entire applications in Python, using .NET services and components written in any language that targets the CLR (C#, VB.NET, F#, C++/CLI).

> Python.NET is currently compatible and tested with Python releases 3.7 - 3.11.

Ohhh, it is up to day. That could be really cool.

I really need a way of transfering data between .NET and Python for my Holdem project later. Though I could do it over the network card, this way could be better.

I'll keep it in mind. I really want access to Python's ML libraries from my .NET backends, but not much else. I just need a way of transfering primitive arrays without the slowness of going through the network card. As long as I had that, I have everything I need for the Holdem project.

8:55pm. Let me close here for real. I need to believe that success and failure in the world make sense. I can't be paranoid and say that the black star is shining on me.

All I want is a chance to show off my skills and get a job based on that.

I can't really show off backend skills, so it makes sense to go the full stack route even if in the end all I get are backend jobs.

9pm. I should have achieved something with ML, but I literally can't do a thing with it right now that would be in any way impressive. The poker agents I'll dome is possibly the best one could do for somebody in my circumstances."

---
## [i574n/The-Spiral-Language](https://github.com/i574n/The-Spiral-Language)@[bcd482810d...](https://github.com/i574n/The-Spiral-Language/commit/bcd482810db292c0aea5e157b7cb3a2f76ad9054)
#### Thursday 2023-04-06 23:24:53 by Marko Grdinić

"8:05am. I am up. No mail. Well, it is the weekend so that is as expected. Right now, let me chill a bit and then I will go through the SignalR playlist.

8:50am. Let me get started.

Time to learn SignalR. There are a lot of videos in that playlist, and I'd want to go through all of them today.

https://youtu.be/6W5gmRgmbuc?list=PLOeFnOV9YBa7nzzuXnThdfsyY06AuCP5V&t=608

This is great as it also shows me how to use regular sockets.

https://youtu.be/6W5gmRgmbuc?list=PLOeFnOV9YBa7nzzuXnThdfsyY06AuCP5V&t=665

I didn't think he'd go into depth so much. This is great.

https://youtu.be/6W5gmRgmbuc?list=PLOeFnOV9YBa7nzzuXnThdfsyY06AuCP5V&t=973
> If you are not satisfied with this answer, you are going to have to go deeper on your own. You are going to have to go into the land of native C or C++ implementations.

https://youtu.be/6W5gmRgmbuc?list=PLOeFnOV9YBa7nzzuXnThdfsyY06AuCP5V&t=1008
> It is still very much a HTTP connection, although it is one that isn't closed.

9:15am.

https://youtu.be/NhDu1AcV79A?list=PLOeFnOV9YBa7nzzuXnThdfsyY06AuCP5V&t=110

I need to remember the `Use` here. If I remember correctly, `Run` is for just the endpoints.

https://youtu.be/NhDu1AcV79A?list=PLOeFnOV9YBa7nzzuXnThdfsyY06AuCP5V&t=306

In order to really get this, I'd have to debug it. This would be a good exercise in itself, but I do not feel like it. Let me just watch all of this, then I'll move on to the Elmish.Bridge.

https://youtu.be/NhDu1AcV79A?list=PLOeFnOV9YBa7nzzuXnThdfsyY06AuCP5V&t=559

I admit, I am having trouble grasping the differences between all of this, just based on what was shown here.

https://youtu.be/q5ZHAUUAlQE?list=PLOeFnOV9YBa7nzzuXnThdfsyY06AuCP5V
ASP.NET Core SignalR - Feature Overview

Let me move on to this one.

https://youtu.be/q5ZHAUUAlQE?list=PLOeFnOV9YBa7nzzuXnThdfsyY06AuCP5V&t=72

Oh, there is a `signal.js`. Yeah, that would make things easier.

https://pypi.org/project/signalr-client/

It does have a Python client. I should have absolutely used this for the lang server instead of ZeroMQ. ZeroMQ is 99% relieable, which is why I'll have to replace it with a websocket server. What else am I supposed to do here to fix how it drops messages occasionaly? I admit, I did like the book by Hitchens.

https://youtu.be/q5ZHAUUAlQE?list=PLOeFnOV9YBa7nzzuXnThdfsyY06AuCP5V&t=613

I see.

https://youtu.be/q5ZHAUUAlQE?list=PLOeFnOV9YBa7nzzuXnThdfsyY06AuCP5V&t=656

This interface is quite useful. I could use it to send data in a typed manner between the client and the server.

I don't even need `Elmish.Bridge`.

https://youtu.be/q5ZHAUUAlQE?list=PLOeFnOV9YBa7nzzuXnThdfsyY06AuCP5V&t=1064

Sending to all in a group would be an useful functionality for a game.

10:15am. https://youtu.be/q5ZHAUUAlQE?list=PLOeFnOV9YBa7nzzuXnThdfsyY06AuCP5V&t=1191

Here he covers the groups.

https://youtu.be/q5ZHAUUAlQE?list=PLOeFnOV9YBa7nzzuXnThdfsyY06AuCP5V&t=1401

It seems in the next video he will cover how to login the user automatically.

10:35am. https://youtu.be/JVFWCsz-oQY?list=PLOeFnOV9YBa7nzzuXnThdfsyY06AuCP5V
ASP.NET Core SignalR - Streams

Let me watch this. I checked the code for the previous section, and as can be expected, it is easier to understand than the low level stuff. Now...

I've been checking language trends on LinkedIn, but I couldn't find an in depth analysis of a language's popularity. It does not matter. Some of those lists are extremely suspect. I can't imagine Assembly being in top 10. I am yet to see a single job ad for it anywhere at all!

Forget that, let me watch the video.

https://youtu.be/JVFWCsz-oQY?list=PLOeFnOV9YBa7nzzuXnThdfsyY06AuCP5V&t=274

Rx makes an appearance here.

https://youtu.be/JVFWCsz-oQY?list=PLOeFnOV9YBa7nzzuXnThdfsyY06AuCP5V&t=293

Maybe I should watch his video on generators. I wonder how this would work in F#? Nevermind this for now.

https://nextjs.org/learn/seo/introduction-to-seo

Oh, this has a SEO section. Nevermind this for now.

https://youtu.be/JVFWCsz-oQY?list=PLOeFnOV9YBa7nzzuXnThdfsyY06AuCP5V&t=374

Now that I think about it, maybe I should change my video format. Instead of writing code all at once, it might be best to just go over it and explain it like this guy is doing. When you are writing it all at once, it is easy to make a mistake.

https://youtu.be/JVFWCsz-oQY?list=PLOeFnOV9YBa7nzzuXnThdfsyY06AuCP5V&t=374

He mentioned around here that the Hub is a scoped connection which confused me for a moment, but then I realized it makes sense. I mean, the socket is supposed to be closed once one side breaks off, so it makes sense that it is scoped. But it should have some kind of singleton object throughout the server lifetime, right? Otherwise there is no way it could keep track of connections.

https://github.com/raw-coding-youtube/aspnetcore-signalr/blob/main/4.StreamingData/StreamingData_8/wwwroot/index.html

No actually it does not make sense why it would be a scoped service. Shouldn't it have the same id for the duration of the connection?

I guess that the connection ids are something separate.

https://youtu.be/JVFWCsz-oQY?list=PLOeFnOV9YBa7nzzuXnThdfsyY06AuCP5V&t=519

He is making the same error as me in not using Excalidraw.

https://youtu.be/mrCxfifTepU?list=PLOeFnOV9YBa7nzzuXnThdfsyY06AuCP5V
ASP.NET Core SignalR - Authentication

Authentication and authorization.

https://youtu.be/mrCxfifTepU?list=PLOeFnOV9YBa7nzzuXnThdfsyY06AuCP5V&t=148

I don't know what this is doing, but I am going to have to figure this out at some point. This can serve as a reference.

https://youtu.be/mrCxfifTepU?list=PLOeFnOV9YBa7nzzuXnThdfsyY06AuCP5V&t=207

Ugh, this is kind of filtering me. I am going to have to study this more in depth.

https://youtu.be/mrCxfifTepU?list=PLOeFnOV9YBa7nzzuXnThdfsyY06AuCP5V&t=310

I can't follow what is going on here at all. Let me just watch this, and I will go over this subject later. It shouldn't matter too much if I leave if for that.

11:35am. Now I am looking up 'job market' posts on /g/. I need to give it a few months. I should consider this kind of environment an opportunity. In a month or two, the stock market will start rebounding and the job market will follow.

https://youtu.be/mrCxfifTepU?list=PLOeFnOV9YBa7nzzuXnThdfsyY06AuCP5V&t=565

You know what, let me skip this video here, as I am very confused at what is going on here.

https://youtu.be/7JTfCiOzDcI?list=PLOeFnOV9YBa7nzzuXnThdfsyY06AuCP5V
ASP.NET Core SignalR - Chat App Example

Let me skip to this.

...No, it does not sit right by me.

ASP.NET Core SignalR - Chat App Example

https://www.youtube.com/playlist?list=PLOeFnOV9YBa7dnrjpOG6lMpcyd7Wn7E8V
(UPDATED check description) ASP.NET Core - Authentication & Authorization Tutorial

Oh, this guy has a ton of tutorials on this.

I guess I have no choice, but to segue into it.

I meant to do the backend as soon as possible. And indeed, with the knowledge I've gained so far, I could do it without a hitch using SignalR, or Elmish Bridge, but the true aim is to get the webdev skills. I need a portfolio, but those will be easy to once I cover all the ground.

The true time eater is studying these libraries.

https://youtu.be/ExQJljpj1lY?list=PLOeFnOV9YBa4yaz-uIi5T4ZW3QQGHJQXi
ASP.NET Core Authentication (.NET 7 Minimal Apis C#)

Oh, here is an updated list.

https://youtu.be/ExQJljpj1lY?list=PLOeFnOV9YBa4yaz-uIi5T4ZW3QQGHJQXi&t=23
> If you don't know anything, this video would be perfect for you.

https://youtu.be/ExQJljpj1lY?list=PLOeFnOV9YBa4yaz-uIi5T4ZW3QQGHJQXi&t=69

This is the most minimalist API ever. This guy is really good at explaining.

https://youtu.be/ExQJljpj1lY?list=PLOeFnOV9YBa4yaz-uIi5T4ZW3QQGHJQXi&t=76
> Before we can even get the user name, we need to be signed in.

Incidentally, I really need a better mic. I am going to splurge on getting one if need be. I can just order one online if need be.

https://youtu.be/ExQJljpj1lY?list=PLOeFnOV9YBa4yaz-uIi5T4ZW3QQGHJQXi&t=103
> We need our HTTP context. And if you don't know what an Http context is, essentially when you make an http request, all the request headers, the url, any information headers, all of that is shoved into the Http context.

https://youtu.be/ExQJljpj1lY?list=PLOeFnOV9YBa4yaz-uIi5T4ZW3QQGHJQXi&t=170

You know what, I'll follow along here. I want to play with the dev tab.

```cs
return ctx.Request.Headers.Cookie[0].Split('=')[1];
```

This is a good time to get familiar with regexes. This way of doing things won't cut it. I really need the capability for simple parsing.

```cs
app.MapGet("/username", (HttpContext ctx) =>
{
    var cookies = ctx.Request.Headers.Cookie.Select(x => x.Split('='));
    foreach (var cookie in cookies)
    {
        var t =
            cookie switch
            {
                ["auth", var rest] => { return 1; },
            };
    }

});
```

I have to admit, C#'s pattern matching is super annoying. This way of doing it is not valid.

12:25pm. I took a look at the regex docs, and they are inscrutable. Since these tutorials are simple to understand, I'll consider doing them in F#.

https://youtu.be/ExQJljpj1lY?list=PLOeFnOV9YBa4yaz-uIi5T4ZW3QQGHJQXi&t=306

Let me do this in F#. The way he does it works, but it would throw an exception if the cookie is not there...

Actually...

```fs
    app.MapGet("/login", Func<HttpContext,string>(fun ctx ->
        "Hello World!"
        )) |> ignore

    app.Run()
```

As it turns out this is annoying to do in F#.

```fs
[<EntryPoint>]
let main args =
    let builder = WebApplication.CreateBuilder(args)
    let app = builder.Build()

    let get pattern f = app.MapGet(pattern, Func<_,_>(f)) |> ignore

    get "/login" <| fun (ctx : HttpContext) ->
        ctx.Response.Headers.SetCookie <- "auth=usr:anton"
        "ok"

    get "/username" <| fun (ctx : HttpContext) ->
        ctx.Request.Cookies.Select(fun x ->
            x.
            )
        ""

    app.Run()

    0 // Exit code
```

Huh what the hell? I didn't realize at all it is a KeyValue collection. What is the point in splitting it along the `=` then? Why is the type different in the C# version?

```cs
app.MapGet("/username", (HttpContext ctx) =>
{
    var cookies = ctx.Request.Cookies.Select(x => x.Value);

});
```

Oh, it does give me the right thing like this.

```fs
open System
open Microsoft.AspNetCore.Builder
open Microsoft.Extensions.Hosting
open Microsoft.AspNetCore.Http

[<EntryPoint>]
let main args =
    let builder = WebApplication.CreateBuilder(args)
    let app = builder.Build()

    let get pattern f = app.MapGet(pattern, Func<_,_>(f)) |> ignore

    get "/login" <| fun (ctx : HttpContext) ->
        ctx.Response.Headers.SetCookie <- "auth=usr:anton"
        "ok"

    get "/username" <| fun (ctx : HttpContext) ->
        let not_logged_in = "not logged in"
        match ctx.Request.Cookies.TryGetValue("auth") with
        | true, v ->
            match v.Split ':' with
            | [|"usr"; v|] -> v
            | _ -> not_logged_in
        | _ -> not_logged_in

    app.Run()

    0 // Exit code
```

Let me stop here, I am going crazy over this insignificant thing.

https://youtu.be/ExQJljpj1lY?list=PLOeFnOV9YBa4yaz-uIi5T4ZW3QQGHJQXi&t=293

Let me stop on this. I need to have breakfast and do the chores."

---

