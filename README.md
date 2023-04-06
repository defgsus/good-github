## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-04-05](docs/good-messages/2023/2023-04-05.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,217,466 were push events containing 3,420,792 commit messages that amount to 265,388,910 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 73 messages:


## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[dc2f52e386...](https://github.com/tgstation/tgstation/commit/dc2f52e386e0ef3cfcc2133293cd3f68f6a1eee3)
#### Wednesday 2023-04-05 00:02:28 by tralezab

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
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[48183ec0ff...](https://github.com/tgstation/tgstation/commit/48183ec0ffd67ea5afa26c6f6e58e81edff98d52)
#### Wednesday 2023-04-05 00:02:28 by san7890

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
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[b5ebf5c942...](https://github.com/tgstation/tgstation/commit/b5ebf5c9423cb3b39a2b9cfb6524b157dc6cb4b2)
#### Wednesday 2023-04-05 00:02:28 by Helg2

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
## [Jolly-66/tgstation](https://github.com/Jolly-66/tgstation)@[fe7ebd67cf...](https://github.com/Jolly-66/tgstation/commit/fe7ebd67cf74982038524ceb175377d7ff6c0486)
#### Wednesday 2023-04-05 00:04:20 by LemonInTheDark

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
## [Jolly-66/tgstation](https://github.com/Jolly-66/tgstation)@[c18b1ef442...](https://github.com/Jolly-66/tgstation/commit/c18b1ef4423fc7d9083adac9b51aab4f169ea8aa)
#### Wednesday 2023-04-05 00:04:20 by tralezab

End of Mapping March (Thanks to everyone who contributed, you're amazing!!!) (#74417)

## About The Pull Request

Removes the special mapping template. We got a really good turnout this
year! Will start counting ckeys and all that.

### But my mapping pr isn't done yet!

If it was opened during march, you'll get your token, don't worry

---
## [DrDiasyl/tgstation](https://github.com/DrDiasyl/tgstation)@[b3e5642d94...](https://github.com/DrDiasyl/tgstation/commit/b3e5642d94caab455bea8b71e244081249cb2924)
#### Wednesday 2023-04-05 00:22:38 by san7890

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
## [Thunder12345/tgstation](https://github.com/Thunder12345/tgstation)@[c3b78761d2...](https://github.com/Thunder12345/tgstation/commit/c3b78761d29c53558fd993c84bb808bd5783861d)
#### Wednesday 2023-04-05 00:32:54 by tralezab

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
## [Comxy/tgstation](https://github.com/Comxy/tgstation)@[e1221c986f...](https://github.com/Comxy/tgstation/commit/e1221c986f5da2551051f47aa0fbd1d49e367c9b)
#### Wednesday 2023-04-05 00:37:46 by san7890

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
## [nodestake/RealioNetwork](https://github.com/nodestake/RealioNetwork)@[ab863384ee...](https://github.com/nodestake/RealioNetwork/commit/ab863384eeabb194d626cd1c15b42bf255d28eef)
#### Wednesday 2023-04-05 00:45:14 by Indonode

Indonode#5255

Professional and Experienced Validator in Cosmos Ecosystem
High Security , High Uptime

Providing the best services for Stakers and Community
Helping new project to success with love and knowledge.

Our services :
✅ Node Installation Guide (with Cosmovisor)
✅ Genesis
✅ Addrbook (Every Hour updated)
✅ Live Peers
✅ Public Endpoints
✅ Statesync
✅ Snapshot ( Updated everyday at 12 Midnight)
✅ CLI Cheatsheets Command
✅ Explorer

Find more at : https://indonode.net/

---
## [timothymtorres/tgstation](https://github.com/timothymtorres/tgstation)@[c0ef4ba907...](https://github.com/timothymtorres/tgstation/commit/c0ef4ba907b28e1288f2ccbbc6714d15a923b1bd)
#### Wednesday 2023-04-05 00:47:44 by tralezab

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
## [timothymtorres/tgstation](https://github.com/timothymtorres/tgstation)@[ccef887efe...](https://github.com/timothymtorres/tgstation/commit/ccef887efec2cb3025228210bcb134700aac5175)
#### Wednesday 2023-04-05 00:47:44 by san7890

Lints Against Unmanaged Local Defines (#74333)

# MAINTAINER - USE THE BUTTON THAT SAYS "MERGE MASTER" THEN SET THE PR
TO AUTO-MERGE! IT'S MUCH EASIER FOR ME TO FIX THINGS BEFORE THEY SKEW
RATHER THAN AFTER THE FACT.

## About The Pull Request

Hey there,

This took a while to do, but here's the gist:

Python file now regexes every file in `/code` except for those that have
some valid reason to be tacking on more global defines. Some of those
reasons are simply just that I don't have the time right now (doing what
you see in this PR took a few hours) to refactor and parse what should
belong and what should be thrown out. For the time being though, this PR
will at least _halt_ people making the mistake of not `#undef`ing any
files they `#define` "locally", or within the scope of a file.

Most people forget to do this and this leads to a lot of mess later on
due to how many variables can be unmanaged on the global level. I've
made this mistake, you've made this mistake, it's a common thing. Let's
automatically check for it so it can be fixed no-stress.

Scenarios this PR corrects:

* Forgetting to undef a define but undeffing others.
* Not undeffing any defines in your file.
* Earmarking a define as a "file local" define, but not defining it.
* Having a define be a "file local" define, but having it be used
elsewhere.
* Having a "local" define not even be in the file that it only shows up
in.
* Having a completely unused define*

(* I kept some of these because they seemed important... Others were
junked.)
## Why It's Good For The Game

If you wanna use it across multiple files, no reason to not make it a
global define (maybe there's a few reasons but let's assume that this is
the 95% case).

Let me know if you don't like how I re-arranged some of the defines and
how you'd rather see it be implemented, and I'd be happy to do that.
This was mostly just "eh does it need it or not" sorta stuff.

I used a pretty cool way to detect if we should use the standardized
GitHub "error" output, you can see the results of that here
https://github.com/san7890/bruhstation/actions/runs/4549766579/jobs/8022186846#step:7:792
## Changelog
Nothing that really concerns players.

(I fixed up all this stuff using vscode, no regexes beyond what you see
in the python script. sorry downstreams)

---
## [Xander3359/tgstation](https://github.com/Xander3359/tgstation)@[c27f9a6d9b...](https://github.com/Xander3359/tgstation/commit/c27f9a6d9b9739baae09db063b6eb266d525772c)
#### Wednesday 2023-04-05 00:49:35 by necromanceranne

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
#### Wednesday 2023-04-05 00:49:35 by lizardqueenlexi

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
## [Rustybuckets6601/tgstation](https://github.com/Rustybuckets6601/tgstation)@[0a1f7e8de2...](https://github.com/Rustybuckets6601/tgstation/commit/0a1f7e8de2fea2116b73f22a11fdf328763c503a)
#### Wednesday 2023-04-05 00:55:57 by Hatterhat

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
## [vinylspiders/Skyrat-customization-expansion](https://github.com/vinylspiders/Skyrat-customization-expansion)@[7a64573c8b...](https://github.com/vinylspiders/Skyrat-customization-expansion/commit/7a64573c8bfa01bac0d690db68d4b6528d502579)
#### Wednesday 2023-04-05 00:56:00 by SkyratBot

[MIRROR] Atmos QOL + Small Sprite Fix [MDB IGNORE] (#20243)

* Atmos QOL + Small Sprite Fix (#74251)

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

* Atmos QOL + Small Sprite Fix

---------

Co-authored-by: 13spacemen <46101244+13spacemen@users.noreply.github.com>

---
## [Stalkeros2/Skyrat-tg](https://github.com/Stalkeros2/Skyrat-tg)@[60d2d2ee1a...](https://github.com/Stalkeros2/Skyrat-tg/commit/60d2d2ee1ae4f7a3c8c93e14fdbd6c210a45cf04)
#### Wednesday 2023-04-05 01:03:02 by SkyratBot

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
## [DontDoItKids/ITEC-145---Final-Project](https://github.com/DontDoItKids/ITEC-145---Final-Project)@[00e0abec05...](https://github.com/DontDoItKids/ITEC-145---Final-Project/commit/00e0abec059cd35e8dc1cafba08ec2f9eaff56a9)
#### Wednesday 2023-04-05 01:57:38 by Trey Hall

Fuck You
Need to implement Power up activations
and drawing them on the screen

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[018db9ab81...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/018db9ab81453478875e2af9e7dcb7deae959bf3)
#### Wednesday 2023-04-05 02:00:55 by SkyratBot

[MIRROR] Malfunctioning AIs get a discount on the Doomsday equipment by hacking Head of Staff APCs [MDB IGNORE] (#20337)

* Malfunctioning AIs get a discount on the Doomsday equipment by hacking Head of Staff APCs (#74225)

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

Co-authored-by: Jacquerel <hnevard@ gmail.com>

* Malfunctioning AIs get a discount on the Doomsday equipment by hacking Head of Staff APCs

---------

Co-authored-by: zxaber <37497534+zxaber@users.noreply.github.com>
Co-authored-by: Jacquerel <hnevard@ gmail.com>

---
## [lessthnthree/tgstation](https://github.com/lessthnthree/tgstation)@[9dfe00d79d...](https://github.com/lessthnthree/tgstation/commit/9dfe00d79dd7bd540442ce825caa4e964c619b46)
#### Wednesday 2023-04-05 02:21:08 by san7890

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
## [DroneBetter/Perspective3Dengine](https://github.com/DroneBetter/Perspective3Dengine)@[50303cf64c...](https://github.com/DroneBetter/Perspective3Dengine/commit/50303cf64cc656fe6bfe0c51017c0db2a38ec6da)
#### Wednesday 2023-04-05 02:23:00 by DroneBetter

All manner of wondrous things

Sorry for my inactivity as of late, I have been quite busy with real-life preoccupations once more, but I have a few additions of various degrees of whimsy and interestingness (though nothing that can be seen without changing parts of the program).

I had previously made a more complete algebra of quaternions than had been necessary, however now I have made one of permutations also, the idea is that they are meant to contain the terms on which they act, and leave all others as-is, and compose by multiplication (which explains the factoradic indexing methods (as a treat), and the brief foray into implementing some OEIS sequences seemingly entirely unrelated to 4D engines for the purposes of their fast exponentiation, involving bounds for their periods (that turned out not to be necessary because converting to cycle format is fast enough as-is (as you will find out if (for whatever reason) you want to make a table of all permutations up to 7! to the power of their index))).

Perhaps I will remove all of the broken and commented-out permutation __int__ methods (from before I had my revelation that (along with a significant amount of calibration by experimentation) led to the working one), but I like some, especially those that generate palindromes delimited by zeros (very mysterious).

There is also no longer a 120*120 multiplication table stored inline in the program (though it looks quite nice (with many interesting patterns in the numbers of digits of adjacent numbers, due to the decision for axial permutations to take precedence over signs in the ordering), if you want to look at it as it was then), because there are now some functions strewn about for finding minimal sets of rootless ('prime') actions, of which recursively taking the set of compositions of their Cartesian products with themselves eventually yields the entire initiial set (which was the initial reason for the decision to implement the permutation class), I made a sorted version of product (sortduct) before learning it was already implemented as combinations_with_replacement.

I also added a set of quaternions for orientations in the icosahedral group (after realising that it could be implemented by rotations by 2*pi/5 in the roll axis as well as across edges between orientations pointing towards vertices (imparting there also a roll of pi), so they generate to a finite set instead of growing uncontrollably). Several ways to express them are provided (in terms of 5, phi (that some people like, and reduces the number of sqrts necessary by 1 in all cases (though so too would assigning sqrt(5) as a constant)) and roots of quadratics), though the surd class wasn't made with nested roots in mind (and their canonicalisation seems quite hard) so I decided to instead compute them numerically (and use Robert Munafo's RIES instead of calculating them all manually (which went well, only minor adjustments were necessary in some cases)). Their generation from the program is quite elegant, I think, and I will be able to make the rotation group of the 600-cell next (being that this is the vertex figure).

Perhaps it would be a good idea to make a quaternion pair class, also (being that they come up in multiple places now, and the x!=None case in rotationParameters provides a way (found with SymPy and experimentation) for generating 4D rotation matrices out of the same parameters as them).

I also made some camera-rotation functions at the end (mainly for testing), and made the edges do spherical-linear-interpolations (slerps) with precomputed roots, so you can truly feel as though you're in moving around edges inscribed in the surface of a hypersphere (though it doesn't matter much, because lines still render behind you).

I also got antipodal points rendering more dimly than their nearby counterparts then broke it again, many of the extraneous additions towards the end are from me trying to fix it again, sorry (I ought to commit more and program when more awake).

Anyway, I hope you, my dear perusers (of the present and future) will enjoy, I unfortunately must stop distracting myself with all this productive waste of time for the time being once more, though I will return to finish it eventually.

---
## [ieee802dot11ac/YARG](https://github.com/ieee802dot11ac/YARG)@[0ed0847cbf...](https://github.com/ieee802dot11ac/YARG/commit/0ed0847cbff5a8b7362518a3afe4c8f58e6a8637)
#### Wednesday 2023-04-05 04:11:09 by ieee802dot11ac

fuck it! i give up for the night!

god cisco, could you have made it more of a fuckin headache?

---
## [Neuraljac/ML-Data-Analysis](https://github.com/Neuraljac/ML-Data-Analysis)@[9b2898f875...](https://github.com/Neuraljac/ML-Data-Analysis/commit/9b2898f87594eb152cccae7d7feeb97e8b0b05e2)
#### Wednesday 2023-04-05 04:49:10 by Jared F. King

TBI participant generator

This code creates 100 participants and assigns them a numerical ID from 1 to 100. Then, each participant is randomly given an age between 20 and 100 years. Each person is randomly given a gender of either male or female. Then, each person is randomly assigned a TBI severity of either mild, moderate, or severe. Once each of these things is generated, the variables for Suicidal Ideation and Depression are randomly generated but weighted in such a way that those with more severe TBI, those who are male, and those who are older, will have a higher average suicidal ideation score.

---
## [zinc-collective/convene](https://github.com/zinc-collective/convene)@[9d96300571...](https://github.com/zinc-collective/convene/commit/9d963005716ebc9da222fa878f138afff09f0d1b)
#### Wednesday 2023-04-05 05:10:14 by Zee

✨🥔🥗 `Marketplace`: Validate delivery independently (#1292)

* `Marketplace`: Sprout `Cart::Delivery` scaffolding

- https://github.com/zinc-collective/convene/issues/831

When a `Shopper` sets their delivery info, they now get error messages
if they do not provide sufficient information (i.e. leave their phone
number blank)

In order to accomplish that, I:

1. Pulled out the `cart/deliveries/_delivery` and `cart/deliveries/_form` partials from `_cart`
2. Sprouted a new `Cart::Delivery` model, with corresponding
   `Cart::DeliveriesController` and `Cart::DeliveryPolicy` objects

It's feeling a little like we want a `Cart` to `has_one :delivery` and
move the encrypted data into that.

However, I'm not quite ready to do that, since I would rather:

- [ ] Make it purty! It's pretty ugly right now
- [ ] Make it safe! It's not tested *remotely* enough

Well where did you come from

* 🥗 `Marketplace`: Test `DeliveriesController`!

We ran into a number of problems here, in particular testing turbo
streams when there is a `respond_to` block does not apparently work
nearly as well as we wish it did

Co-authored-by: Dicko Sow <s12dsow@users.noreply.github.com>

🧹 `Marketplace`: Appease the Rubocop

* Use new location syntax

* 🛠️ `Marketplace`: Add a factory for `Cart::Delivery`

* 🛠️ `Neighborhood`: `have_rendered_turbo_stream` compares the body

OK this is way tooooo greedy but it's so dang close...

* Helps when I use the right gosh-darn thing thang

* And some tests on update!

* Get rid of that there whitespace

* 🥗 `Marketplace`: Validation specs for `Cart::Delivery`

---
## [avran02/ScheduleBotForked](https://github.com/avran02/ScheduleBotForked)@[81bce2551a...](https://github.com/avran02/ScheduleBotForked/commit/81bce2551a8da8cf5c3698fccda698c016663b04)
#### Wednesday 2023-04-05 05:33:28 by Rewqaf

Merge pull request #3 from avran02/main

Fuck yeah  added new fucking line, bitches!

---
## [Hansen333/Hansen33-s-DERO-Miner](https://github.com/Hansen333/Hansen33-s-DERO-Miner)@[b866cfebad...](https://github.com/Hansen333/Hansen33-s-DERO-Miner/commit/b866cfebad16b0aeebeb0208c3e86f02e066ec79)
#### Wednesday 2023-04-05 06:11:43 by Hansen33

🎉 We are thrilled to present the latest release of Hansen33's Miner, version 0.6! This update is packed with an array of new features and enhancements, all tailored to your feedback from the community.

🚀 One notable change is the default workers and thread settings, which have been optimized for better performance. We have also reduced the worker delay to 0, allowing the miner to start up faster than before.

💪 Furthermore, we have introduced new tunable options for thread locking, including -no-thread-locking and -thread-lock-individuals. These options provide better thread-affinity handling by either not locking threads at all and letting Golang handle it or by locking individual threads.

💼 We've made it easier to track individual worker performance by allowing the use of worker names as part of the wallet address—an essential improvement for all users.

🐳 Deployment via Docker is now available, simplifying and speeding up the process of deploying Hansen33 Miner. With only 2 commands, you can install and launch the miner, making fleet-wide deployment to multiple nodes more straightforward than ever.

💻 MacOS users will be pleased to know that we now offer releases for both ARM and AMD. We have also extended our support to FreeBSD, and we're looking forward to hearing about real-world results. If you have hardware running FreeBSD and want to test the miner, please let us know! Our QEMU test VM showed promising hashrates, and we're eager to see how it performs in practice.

🙏 A big thank you to Krane#6695, iotapi322 vipor.net#9019, orionure#7006, Jonas need a nick#8572, Surv#3539, ChIrish#9387, guru#0080 and chakipuᵈᵉʳᵒ|ˢᴹˢ#8685 for their helpful feedback and contributions to this release. Their support has helped make Hansen33's Miner even better.

👋 As always, we value feedback from the community and encourage users to reach out with any questions or issues they may encounter.

🔗 Are you ready to try out Hansen33's Miner v0.6? Download it now at https://github.com/Hansen333/Hansen33-s-DERO-Miner and experience the enhancements for yourself!

📣 If you find Hansen33's Miner helpful, please consider sharing your experience with friends, colleagues, and fellow miners.

Together, let's continue improving Hansen33's Miner and make it a top choice for miners around the world.

---
## [newstools/2023-information-nigeria](https://github.com/newstools/2023-information-nigeria)@[82efc6aaa0...](https://github.com/newstools/2023-information-nigeria/commit/82efc6aaa016ac35c1a0497677303c1fb92224da)
#### Wednesday 2023-04-05 06:54:11 by Billy Einkamerer

Created Text For URL [www.informationng.com/2023/04/i-strangled-my-girlfriend-to-death-after-failed-attempts-to-abort-pregnancy-20-year-old-kano-man-confesses.html]

---
## [CaosCreations/SpaceTruckin](https://github.com/CaosCreations/SpaceTruckin)@[ffc08749be...](https://github.com/CaosCreations/SpaceTruckin/commit/ffc08749bea6b80278e6548bcbbde254f97d64a3)
#### Wednesday 2023-04-05 07:00:23 by Stefano di Pace

Dialogue Implementation (#727)

* Put all the shootin the shit convos into the database

basically did it like the random Daniel convos

* PRIORITY BABYYYY

ooooh

* Barry & Yally's Convo Hub in + Plus Holo Shader

LOOK AT ME GO

* Implemented MORE THINGS

* DID THE PREFABS

ALMOST FORGOT THEM IM SO SLEEPY

* FIXED THE SHIT

holy hologram icon and applied prefabs

* FUCKIN HOLO SHADER FUCKIN BULLSHIT

---
## [automatarium/automatarium](https://github.com/automatarium/automatarium)@[092a2d5841...](https://github.com/automatarium/automatarium/commit/092a2d5841923f511238523cf77b521e4c15c8dc)
#### Wednesday 2023-04-05 07:06:46 by Jake Leahy

Fix imports to find any last type bugs

Allow importing in a way that pleases both typescript and parcel

This is honestly cursed as fuck

---
## [tescao/evals](https://github.com/tescao/evals)@[ab5f7b2a89...](https://github.com/tescao/evals/commit/ab5f7b2a89bcf60e8e93adfb2c70688c6d6ffd44)
#### Wednesday 2023-04-05 07:08:58 by oscar-king

Counting bigrams in sentences (#302)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. We encourage partial PR's with
~5-10 example that we can then run the evals on and share the results
with you so you know how your eval does with GPT-4 before writing all
100 examples.

## Eval details 📑
### Eval name
Bigram Counting

### Eval description

Tests whether the model is able to count the frequency of bigrams in a
sentence.

### What makes this a useful eval?

This is a very simple task for humans and it's possibly slightly more
'difficult' than counting the occurrences of a single letter.

Bigram frequencies are used in applications ranging from rudimentary NLP
tasks to cryptography.

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
- [x] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.jsonl`
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
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
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
{"input":[{"role":"system","content":"You will be presented with a
sentence. The task is to count the frequency of the bigram 'ng'. After
reading the sentence tell me the number of times the bigram appeared by
saying 'X' where 'X' is the frequency."},{"role":"user","content":"I'm
worried by the fact that my daughter looks to the local carpet seller as
a role model."}],"ideal":"0"}
{"input":[{"role":"system","content":"You will be presented with a
sentence. The task is to count the frequency of the bigram 'ng'. After
reading the sentence tell me the number of times the bigram appeared by
saying 'X' where 'X' is the frequency."},{"role":"user","content":"He
found rain fascinating yet unpleasant."}],"ideal":"1"}
{"input":[{"role":"system","content":"You will be presented with a
sentence. The task is to count the frequency of the bigram 'ng'. After
reading the sentence tell me the number of times the bigram appeared by
saying 'X' where 'X' is the frequency."},{"role":"user","content":"The
near-death experience brought new ideas to light."}],"ideal":"0"}
{"input":[{"role":"system","content":"You will be presented with a
sentence. The task is to count the frequency of the bigram 'ng'. After
reading the sentence tell me the number of times the bigram appeared by
saying 'X' where 'X' is the
frequency."},{"role":"user","content":"Separation anxiety is what
happens when you can't find your phone."}],"ideal":"0"}
{"input":[{"role":"system","content":"You will be presented with a
sentence. The task is to count the frequency of the bigram 'ng'. After
reading the sentence tell me the number of times the bigram appeared by
saying 'X' where 'X' is the frequency."},{"role":"user","content":"He
realized there had been several deaths on this road, but his concern
rose when he saw the exact number."}],"ideal":"0"}
  ```
</details>

---
## [tescao/evals](https://github.com/tescao/evals)@[b170a21cf3...](https://github.com/tescao/evals/commit/b170a21cf32c47d841f64ec110cfd6796ec3f89a)
#### Wednesday 2023-04-05 07:08:58 by Sam Ennis

Computer Science Theory (#83)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. We encourage partial PR's with
~5-10 example that we can then run the evals on and share the results
with you so you know how your eval does with GPT-4 before writing all
100 examples.

## Eval details 📑
### Eval name
Computer Science based questions

### Eval description

Testing the models ability to answer multiple choice computer science
questions correctly

### What makes this a useful eval?

Tests whether it has the ability to answer time complexity, binary tree,
algorithmic computer science calculations.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [X] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [X] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [X] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [ ] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should
- [X] Check that your data is in `evals/registry/data/{name}`
- [X] Check that your yaml is registered at
`evals/registry/evals/{name}.jsonl`
- [X] Ensure you have the right to use the data you submit via this eval

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
Policies (https://platform.openai.com/docs/usage-policies).

- [X] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [X] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [X] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [X] I have filled out all required fields in the evals PR form
- [x] (Ignore if not submitting code) I have run `pip install
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
{"input":[{"role":"system","content":"Choose the best multiple choice
answer to this question. Reply ONLY with the single letter of the answer
you have chosen."},{"role":"user","content":"How many children does a
binary tree have? a) 2 b) any number of children c) 0 or 1 or 2 d) 0 or
1"}],"ideal":"c"}
{"input":[{"role":"system","content":"Choose the best multiple choice
answer to this question. Reply ONLY with the single letter of the answer
you have chosen."},{"role":"user","content":"What is/are the
disadvantages of implementing tree using normal arrays? a) difficulty in
knowing children nodes of a node b) difficult in finding the parent of a
node c) have to know the maximum number of nodes possible before
creation of trees d) difficult to implement"}],"ideal":"c"}
{"input":[{"role":"system","content":"Choose the best multiple choice
answer to this question. Reply ONLY with the single letter of the answer
you have chosen."},{"role":"user","content":"What must be the ideal size
of array if the height of tree is ‘l’? a) (2^l)-1 b) l-1 c) l d)
2l"}],"ideal":"a"}
{"input":[{"role":"system","content":"Choose the best multiple choice
answer to this question. Reply ONLY with the single letter of the answer
you have chosen."},{"role":"user","content":"What are the children for
node ‘w’ of a complete-binary tree in an array representation? a) 2w and
2w+1 b) 2+w and 2-w c) w+1/2 and w/2 d) w-1/2 and w+1/2"}],"ideal":"a"}
{"input":[{"role":"system","content":"Choose the best multiple choice
answer to this question. Reply ONLY with the single letter of the answer
you have chosen."},{"role":"user","content":"What is the parent for a
node ‘w’ of a complete binary tree in an array representation when w is
not 0? a) floor(w-1/2) b) ceil(w-1/2) c) w-1/2 d) w/2"}],"ideal":"a"}
{"input":[{"role":"system","content":"Choose the best multiple choice
answer to this question. Reply ONLY with the single letter of the answer
you have chosen."},{"role":"user","content":"If the tree is not a
complete binary tree then what changes can be made for easy access of
children of a node in the array? a) every node stores data saying which
of its children exist in the array b) no need of any changes continue
with 2w and 2w+1, if node is at i c) keep a seperate table telling
children of a node d) use another array parallel to the array with
tree"}],"ideal":"a"}
  ```
</details>

---
## [tescao/evals](https://github.com/tescao/evals)@[b5da073c21...](https://github.com/tescao/evals/commit/b5da073c215c6453b99269a6dab2dca5454f04dd)
#### Wednesday 2023-04-05 07:08:58 by somerandomguyontheweb

Add Belarusian lexicon eval (#372)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. We encourage partial PR's with
~5-10 example that we can then run the evals on and share the results
with you so you know how your eval does with GPT-4 before writing all
100 examples.

## Eval details 📑
### Eval name

belarusian-lexicon

### Eval description

Test the model's ability to distinguish between existing and
hallucinated Belarusian words.

### What makes this a useful eval?

While the multilingual capability of recent GPT models is impressive,
there is still room for improvement. Many human languages are lagging
far behind English in terms of the model's ability to answer questions
and produce coherent texts in these languages, and the model's
"knowledge" of their lexicon and grammar is, to some extent,
hallucinated. One example is Belarusian, an East Slavic language spoken
by several million people. In my experience with ChatGPT, when the model
is prompted in Belarusian, its responses are sometimes ungrammatical or
semantically incoherent, and very often they contain made-up words – a
possible sign of overgeneralization based on Russian and Ukrainian data,
which are much more
[abundant](https://commoncrawl.github.io/cc-crawl-statistics/plots/languages)
on the web than Belarusian.

This eval contains 150 pairs of single-word prompts: one item in each
pair is a non-word hallucinated by ChatGPT (either totally meaningless
in Belarusian or violating the language's orthographic and phonetic
rules), and another item is an actual Belarusian word with similar
spelling. The model's task is to distinguish between words and
non-words. ChatGPT tends to label most items as existing words,
therefore its accuracy appears to be around 50%, and the negative-class
F measure is very low. Any competent speaker of Belarusian would perform
much better, and a language-specific tool, such as [this spell
checker](https://corpus.by/SpellChecker) or [this grammatical
database](https://bnkorpus.info/grammar.en.html) of Belarusian (also
available for
[download](https://github.com/Belarus/GrammarDB/releases)), would
flawlessly identify non-words.

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
- [x] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

This eval an attempt to point out specific deficiencies in the model's
ability to handle a lower-resource language (Belarusian). As such, it
might not only benchmark future refinements of Belarusian language
capability in the GPT models, but also serve as an instructuve example
for other language communities.

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
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
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
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
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абвязкою"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абвязкаю"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абласці"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "вобласці"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абмяну"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абмену"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абоўязак"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абавязак"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "аднасінькіх"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "аднюсенькіх"}], "ideal": "Y"}
  ```
</details>

---
## [sujoysaraswati/pytorch](https://github.com/sujoysaraswati/pytorch)@[a269469982...](https://github.com/sujoysaraswati/pytorch/commit/a2694699821be04e6a74760ba754911e714a5486)
#### Wednesday 2023-04-05 07:15:13 by Brian Hirsh

aot autograd refactor: make all synthetic base logic layered in a single location (#96235)

This  refactor doesn't significantly change LoC in aot autograd, but I think this nets out to making it clearer (interested in peoples' thoughts).

The idea is that I tried to re-write the part of aot autograd that deals with synthetic bases in a layered way, similar to how Ed wrote the logic for dedup'ing inputs: it happens in one place, and all of the downstream transformation in aot autograd don't have to worry about it.

Specifically, I added a new function `aot_wrapper_synthetic_base`, similar to the existing `aot_wrapper_dedupe`.

The benefit: none of the other code in aot autograd needs to think about synthetic bases (previously, synthetic base code was intertwined in several places).

The downsides: there are two.

(1) `aot_wrapper_synthetic_base()` needs to have its own epilogue. There is one particularly hairy case, where factoring the synthetic base logic to a single location was painful: If you have two inputs that alias each other, where one gets a data mutation, and the other gets a metadata mutation.

Ordinarily, metadata mutations are handled by the runtime epilogue, in `create_runtime_wrapper`. However, now that things are factored this way, the runtime wrapper operates only on synthetic bases instead of operating on the original inputs. For data mutations, it is fine to apply the data mutation to the synthetic base instead of the original input alias. But for metadata mutations, we **need** to apply the metadata mutation directly to the original inputs.

The way that I handled this was by tracking which inputs slot into this specific case (part of a synthetic base, and get metadata mutations), and updateing the flat_fn() that we pass downstream to return these updated inputs as extra outputs. From the perspective of downstream logic, these are real user outputs, that it can treat like any other user outputs. `aot_wrapper_synthetic_base` will know to grab these extra outputs and use them to apply the metadata mutations.

This was pretty annoying, but has the benefit that all of that logic is encapsulated entirely in `aot_wrapper_synthetic_base()`.

(2) input mutations are now performed on the synthetic base instead of the individual aliases.

You can see the original code comment [here](https://github.com/pytorch/pytorch/blob/b0b5f3c6c681896febbd9ff7ad7649b13def345d/torch/_functorch/aot_autograd.py#L1131) for details. We used to do the optimized thing in this case, and now we do the less optimized thing (copying the entire synthetic base, instead of the potentially smaller alias).

To be fair, we had no data showing that this optimization was showing improvements on any models in practice. I also think that the main reason anyone would ever run across this problem is because of a graph break - so if you care about perf, you probably want to avoid the extra graph breaks to begin with. I haven't added any warnings for this, but we probably could depending on what people think.

Pull Request resolved: https://github.com/pytorch/pytorch/pull/96235
Approved by: https://github.com/ezyang

---
## [rahulsh3105/Daily-Python-Projects](https://github.com/rahulsh3105/Daily-Python-Projects)@[3aaf7c2340...](https://github.com/rahulsh3105/Daily-Python-Projects/commit/3aaf7c2340f2e95c589be4167ee4dd6780ab7539)
#### Wednesday 2023-04-05 08:04:12 by Rahul Sharma

Create AutoBirthdayWisher.py

# Auto Birthday Wisher

One forgets to send birthday wishes to friends many times. At such times an automatic birthday wisher comes handy. An automatic birthday wisher via email makes one's life easy. It will send the birthday wishes to friends via email automatically via a server and using an excel sheet to store the data of friends and their birthdays along with email id. It'll send the wishes to friends for all the upcoming years untill we stop the server.

## Setup instructions

In order to run this script, You just need the following modules:

- **Pandas** is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool,
built on top of the Python programming language.
```bash
pip install pandas
```

- **Datetime** is a module used for Encapsulation of date/time values.
```bash
pip install DateTime
```

- **smtplib** module defines an SMTP client session object that can be used to send mail to any Internet machine with an SMTP or ESMTP listener daemon.

## Configuration
1. Assign the Gmail Id of sender to the GMAIL_ID variable in *line 10* of **"Auto B'Day Wisher.py"** file. (e.g. 'xyz@gmail.com')
2. Similar to first step assign the Gmail password of sender to the GMAIL_PSWD variable in *line 11* of **"Auto B'Day Wisher.py"** file. (e.g. '1234')
3. In **"data.xlsx"** file insert the name of the receiver in second column under *Name*. Similarly update the **Birthday** field with the birth date of receiver in the given format*("%dd-%mm-%YYYY")*. Update the **Dailogue** field with a short message you want to send and the **Email** field with the email of the receiver.
4. Make sure to give permission to your google account from which you're sending email to **Allow less secure apps**. Just turn this *"ON"* from [here](https://support.google.com/accounts/answer/6010255?hl=en#zippy=%2Cif-less-secure-app-access-is-off-for-your-account).
5. Run the command
```bash
python "Auto B'Day Wisher.py"
```

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[0a69769954...](https://github.com/odoo-dev/odoo/commit/0a69769954bc80987ea7bad5fbee6a18b7a4f17d)
#### Wednesday 2023-04-05 08:18:23 by Jeremy Kersten

[ADD] website_cf_turnstile: add cloudflare turnstile support

This module allows to add secret key to add the turnstile captcha on
each snippet website_form.

Cloudflare Turnstile
--------------------
A friendly, free CAPTCHA replacement
Turnstile delivers frustration-free, CAPTCHA-free web experiences to
website visitors.
Turnstile stops abuse and confirms visitors are real without the data
privacy concerns or awful UX that CAPTCHAs thrust on users.

---
## [R0M-GH/FRCScout](https://github.com/R0M-GH/FRCScout)@[56bcafe488...](https://github.com/R0M-GH/FRCScout/commit/56bcafe488640b0126de3ad2e0d8fca11e1085b6)
#### Wednesday 2023-04-05 09:17:15 by R0M-GH

Deserve it - Yeat (Up 2 Me)

Tried getting file capabilities working, this didnt work out... suggestion from my :goat: pks to use qr codes, app needs to be deployed on wednesday so im going to be up all night changing from fileio to qr.

everything left to be done:
1) memory leaks in closing matchscout (honestly ill just make matchscout and matchdata in the same file, makes my life easier) - should take like 2 hours to rewrite the ui, this will erase all the working tree issues
2) make a qr code class and transition all fileio to qrio classes, i had chatgpt write me some bs qrcode class but ill probably have to rewrite it - 1 hour for writing class + imports + testing + transition everything from fileio to qrio
3) figure out qr code stuff, how will i scan these codes? do research on what kind of data you get - probably like an hour tops
4) deploy and test for the time left, and then i guess figure out how to put this bitch on the app store - rest of the time i can get

---
## [insertnamehere123/cmss13](https://github.com/insertnamehere123/cmss13)@[a2d5ca6e69...](https://github.com/insertnamehere123/cmss13/commit/a2d5ca6e69725341f0fa261a4a3f89c737e843b3)
#### Wednesday 2023-04-05 10:02:00 by QuickLode

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
## [libgdx/libgdx](https://github.com/libgdx/libgdx)@[e1d1fdc5fb...](https://github.com/libgdx/libgdx/commit/e1d1fdc5fb5b8409dc74f638c633ead405e535f3)
#### Wednesday 2023-04-05 10:59:34 by Tommy Ettinger

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
## [WireGuard/wireguard-android](https://github.com/WireGuard/wireguard-android)@[9ccfbaf048...](https://github.com/WireGuard/wireguard-android/commit/9ccfbaf04891a4a656b7d36750f1687313c64feb)
#### Wednesday 2023-04-05 11:18:18 by Jason A. Donenfeld

ui: distinguish play store installs at runtime

This lets us use the same build for both F-Droid and Play Store, which
makes everything more easily publicly verifiable, since the build system
is reproducible.

It's possible to test this with:

    $ pm install -i com.android.vending path/to/package.apk

And it appears to work well.

However, it's still unclear whether the Play Store reviewers install the
app using utilities that set com.android.vending like this. If not, that
might be a problem. In order to avoid a Play Store suspension that's
harder to appeal, I sent a support request today, which fit in exactly
the 1000 character limit:

    Hi,

    My app pays special attention to Google Play Store guidelines. For that
    reason, there is some code in the app that looks like this:

        if (BuildConfig.IS_GOOGLE_PLAY)
            ...
        else
            ...

    This means that I compile two versions of my app, one for Google Play,
    and another for other app stores. This has worked well for many years
    and it satisfies Google's policy requirements.

    However, compiling two versions of my app is a bit of a pain. Instead, I
    would like to do this check at runtime, with code like this:

        if (pm.getInstallSourceInfo(package).installingPackageName == "com.android.vending")
            ...
        else
            ...

    I have tested that this code works well, and I've installed my app with:

        $ pm install -i com.android.vending ui-release.apk

    This works and successfully satisfies the policy requirements.

    My question is how this works during the review process. Are reviewed
    apps installed with the necessary -i com.android.vending switch to make
    this work?

    Thanks.

I'll see what the response is, if any. But at the very least, if they
don't respond at all, and we try this anyway and the app gets suspended,
we'll have a better argument for having the app reinstated.

Signed-off-by: Jason A. Donenfeld <Jason@zx2c4.com>

---
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[11aab72dc9...](https://github.com/pytorch/pytorch/commit/11aab72dc9da488832326a066d2e47520e4ab2b3)
#### Wednesday 2023-04-05 11:37:28 by Driss Guessous

[SDPA] Add an optional scale kwarg (#95259)

# Summary
This PR adds an optional kwarg to torch torch.nn.functional.scaled_dot_product_attention()
The new kwarg is a scaling factor that is applied after the q@k.T step of the computation. Made updates to the efficient kernel to support but flash and math were minimally updated to support as well.

Will reduce the complexity of: #94729 and has been asked for by a couple of users.

# Review Highlights
- As far as I know I did this the correct way and this both BC and FC compliant. However I always seem to break internal workloads so I would love if someone can advice I did this right?
- I named the optional arg 'scale'. This is probably dumb and I should name it 'scale_factor'. I will make this change but this is annoying and it will require someone thinking we should rename.
- 'scale' is interpreted as `Q@K.T * (scale)`

Pull Request resolved: https://github.com/pytorch/pytorch/pull/95259
Approved by: https://github.com/cpuhrsch

---
## [WireGuard/wireguard-android](https://github.com/WireGuard/wireguard-android)@[abe973278d...](https://github.com/WireGuard/wireguard-android/commit/abe973278d3f9a87267ebda33daf8105befbb6fb)
#### Wednesday 2023-04-05 11:46:39 by Jason A. Donenfeld

ui: distinguish play store installs at runtime for reproducible builds

This change lets us use the same build for F-Droid, Play Store, self
builds, and elsewhere, which makes everything more easily publicly
verifiable, since the build system is reproducible. That will mean that
all APKs, will have the same code and be completely interchangeable, no
matter where they come from.

It does this by removing the build-time branch for special Play Store
builds, and replacing it with a simple runtime check using the
PackageManager APIs that return the name of the installer. If the app is
installed by "com.android.vending", then it's a Play Store install.

It's possible to test this with:

    $ pm install -i com.android.vending path/to/package.apk

And it appears to work well.

However, it's still unclear whether the Play Store reviewers install the
app using utilities that set com.android.vending like this. If not, that
might be a problem. However, it looks like various banking apps also use
the installer package name check in the same way, and refuse to start if
it's not right. That suggests that it would be impossible for Play Store
reviewers to even review those banking apps if they did not set
com.android.vending properly.

Out of an abundance of caution, though, and in order to avoid a Play
Store suspension that's harder to appeal, I sent a support request
today (which just managed to fit exactly in the 1000 character limit):

    Hi,

    My app pays special attention to Google Play Store guidelines. For that
    reason, there is some code in the app that looks like this:

        if (BuildConfig.IS_GOOGLE_PLAY)
            ...
        else
            ...

    This means that I compile two versions of my app, one for Google Play,
    and another for other app stores. This has worked well for many years
    and it satisfies Google's policy requirements.

    However, compiling two versions of my app is a bit of a pain. Instead, I
    would like to do this check at runtime, with code like this:

        if (pm.getInstallSourceInfo(package).installingPackageName == "com.android.vending")
            ...
        else
            ...

    I have tested that this code works well, and I've installed my app with:

        $ pm install -i com.android.vending ui-release.apk

    This works and successfully satisfies the policy requirements.

    My question is how this works during the review process. Are reviewed
    apps installed with the necessary -i com.android.vending switch to make
    this work?

    Thanks.

They responded fairly quickly:

    Hi Jason,

    Thanks for contacting the Google Play team.

    Unfortunately I'm not able to comment on your planned implementation. If
    you think your app is in compliance, please submit your app for review.
    You may want to review the Developer Program Policies for additional
    policy guidance.

    We recommend reviewing the details listed in this blog post and update
    your app accordingly to comply with the changes.

    Thanks for your understanding and continued support.

    Regards,
    Mia
    Google Play Developer Support

So I'll interpret that as a, "if you think it's okay, submit it and see,
and then we'll let you know." So here we go. Hopefully if it is
rejected, the update will only be blocked, and I'll just revert this
commit and resubmit.

Signed-off-by: Jason A. Donenfeld <Jason@zx2c4.com>

---
## [mtougeron/cluster-api-provider-aws](https://github.com/mtougeron/cluster-api-provider-aws)@[867afc7ac7...](https://github.com/mtougeron/cluster-api-provider-aws/commit/867afc7ac718621a11e00fc2b05589ac2548d4d5)
#### Wednesday 2023-04-05 12:51:12 by Claudia Beresford

Fail apidiff make target when git fails

This is a fairly simple fix to ensure that when `git diff` fails on the
`make apidiff` target, the exit code is actually picked up by make.
Previously the exit code from `diff` was "swallowed" by the `if`.

eg:
```
$ cat Makefile
thing:
        if (exit 1); then \
		echo foo; \
        fi
        echo "still here"

$ make thing
still here
$ echo $?
0
```

What we want:
- exit 1 when `git diff` fails
- exit 0 when `grep` fails
- call `go-apidiff` when `git diff` and `grep` succeeds
- exit 1 when `go-apidiff` fails

This is honestly a complete pain to do in a Makefile.

I tried capturing output, moving everything to a script, calling from
one thing to another. But really this is just tricky to do the way we
want in Make.

So, if we can live with a little repetition, we can do the following:
- Check the `git diff` can run, exit 1 if not
- Run the `git diff` again, this time piping the successful command to
  `grep`
- If `grep` fails, then no worries, the target will roll on and exit 0
  like it always has.
- If `grep` succeeds then the `go-apidiff` tool is called and the target
  runs as intended.

------

In the case of `$(APIDIFF_OLD_COMMIT)`, there is some annoying `make`
magic going on here. Which I can't simply make fail since it will cause any
job which uses something in this Makefile to fail out of proximity.
The `shell` is expanded when the file is loaded meaning even targets
which do not care about the value will end up erroring (but not exiting)
when it fails. These are not errors which impact the target's run, but
they look annoying in CI.

Since this var is only used by `apidiff`, we can move it into that
target so it is only evaluated when specifically called.

---
## [k21971/UnNetHack](https://github.com/k21971/UnNetHack)@[02f3febae0...](https://github.com/k21971/UnNetHack/commit/02f3febae006cd8cef656db90e088b2dcd6b1b3f)
#### Wednesday 2023-04-05 12:56:27 by Michael Meyer

Shopkeepers hold a grudge against past thieves

When you steal from a shop, its shopkeeper will remember you as a thief
and charge you higher prices in the future (as well as be more curt and
less polite in interactions with you, though not outright hostile) even
if you pacify them, or die on the level and revisit it later as a bones
file.  This was an idea aosdict had, and I think it makes sense that a
shopkeeper doesn't forgive and forget, immediately returning to treating
you exactly like anyone else, just because you were terrorized into
paying her back.  Paying a shopkeeper off may cause her to stop actively
attacking you, but it feels like she'd have her eye on you as a known
thief going forward (and maybe would hang up a sign with your picture,
saying something like "DO NOT ACCEPT CHECKS FROM THIS HERO").

This surchage already existed, but since it was tied to active anger
(which typically causes a shopkeeper to quickly abandon their shop to
follow you) it was somewhat rare to see it in action.

I did not implement it here, but one possible further tweak might be to
clear the surcharge if the shopkeeper is pacified via taming magic
(which more-or-less magically brainwashes the target to feel positively
towards the hero) but not if you simply pay your debts.

Cherry picked from nethack/nethack@8a549b0a60

---
## [phorgeit/phorge](https://github.com/phorgeit/phorge)@[787a84969f...](https://github.com/phorgeit/phorge/commit/787a84969fa04c519a9291eaac3f7ebbbb3585fa)
#### Wednesday 2023-04-05 13:39:50 by Valerio Bozzolan

Phriction: clarify its search results as "Wiki page"

Summary:
This patch changes a bit how your search results from Phriction
are described in the autocomplete component (the "Typehead"):

{F276843}

After this change, Phriction search results will also contain the word
"Wiki page" so that users can better understand what the result
actually is. Just like a Diffusion repository mentions that it's
a "Repository", and just like a Project mentions that it's a
"Project" and so on.

Before this change, the Typehead entries were only mentioning
the slug of that wiki page.

| Before    | After     |
| {F274820} | {F272278} |

It's unclear if the previous behavior was a mistake (since the
internal parameter of the Typehead is called "type", and so, it
is supposed to mention the application type, not the slug.

Anyway, as a compromise, the slug is still mentioned.

To be honest this is just an excuse to put the middle dot /
aka interpunct character in this project again. Yeah, here the
middle point was used as separator. The apparent reason is:
because the middle point was already in use elsewhere in Phorge.
The real reason is: I'm a lobbyist in a corporation that sells
interpuncts worldwide as our core business, and so, I designed
thisvil plan to put the following middle point - again - in
Phorge (evil laugh).

Closes T15213

Test Plan:
- Search "Change Log" in the up-right bar (or similar)
- You see "Wiki Page · change_log/" (or similar)

Reviewers: O1 Blessed Committers, Cigaryno, avivey

Reviewed By: O1 Blessed Committers, Cigaryno, avivey

Subscribers: avivey, speck, tobiaswiese, Matthew, Cigaryno

Tags: #phriction

Maniphest Tasks: T15213

Differential Revision: https://we.phorge.it/D25102

---
## [LemonEatar/AlvlCalc](https://github.com/LemonEatar/AlvlCalc)@[c13ff9934f...](https://github.com/LemonEatar/AlvlCalc/commit/c13ff9934f60aa45ed18ce453046b32e87ccde17)
#### Wednesday 2023-04-05 13:51:41 by LemonEatar

i hate my life (added the table and now it should work)

---
## [ewinston/rustworkx](https://github.com/ewinston/rustworkx)@[e025356b04...](https://github.com/ewinston/rustworkx/commit/e025356b046a807e848a7c0ee2a32490927d46da)
#### Wednesday 2023-04-05 13:57:59 by Matthew Treinish

Update tox configuration to use tox >= 4.4.0 (#851)

* Update tox configuration to use tox >= 4.4.0

Tox 4.0.0 was released in December 2022 [1] and was a major rewrite of
the internals of the package that included numerous backwards
incompatible changes [2]. Along with that major rewrite was a long
period of instability in the package with a flurry of 47 releases [3]
since 4.0.0 (which has only been 3-4 months). At the time of the 4.0.0
release we pinned the tox version in CI with #761 to avoid this
instability as our tox configuration was not compatible with tox 4.x.y
and tox was actually not compatible with how we had things configured
more generally. The hope was that tox would stabilize more, fix the
issues that plagued the tox 4 release series and we'd be able to relax
that pin without requiring bumping our minimum tox version to ensure
users could use either the old version or the new version locally.
However, since #761 that hope hasn't been realized the divergence
between tox 3 and tox 4 has only widened and at least personally I'm not
convinced of an improvement in stability to the tox 4 release series.
That being said however, this is becoming a developer pain as by default
when setting up a new build environment pip will install the latest
version of tox and we don't have an effective mechanism to pin the tox
version for users as you need to install tox manually as it's the
primary python development entrypoint we use. The only only avenue to
address this would be documentation updates in the CONTRIBUTING.md file,
which we didn't update at the time in #761 because it was meant to be
a version temporary pin that has turned out to not be so temporary.

Since it's been >3 months since we first pinned the tox version and that
pin was meant to be temporary this commit removes that pin and bumps our
minimum supported tox version to be 4.4.0, which despite not being
compatible with tox < 4 as we originally hoped, at least seems to work
fine with install rustworkx after updating the configuration file. This
should hopefully ease the onboarding experience for developers when
working with rustworkx and trying to bootstrap a local development
environment. Longer term I expect we'll look at moving off of tox,
as it no longer seems like a project we can rely on (especially as
a key component for our development and CI infrastructure) for rustworkx
and instead look at something like `nox` which I've heard good things
about and know that PyO3 had moved to it a year or two ago.

Fixes #812

[1] https://pypi.org/project/tox/4.0.0/
[2] https://tox.wiki/en/latest/upgrading.html
[3] https://pypi.org/project/tox/#history

* Stop using tox for retworkx backwards compat jobs

Tox's isolated builder mechanism seems to be incompatible with our
environment variable based package naming mechanism that we use to build
the legacy retworkx package. This is causing CI to fail on the backwards
compat jobs that are installing retworkx (which depends on rustworkx) to
ensure that our backwards compatibility shim works as expected. Instead
of trying to force tox to do the correct thing, it's just easier to stop
using it for that one CI job and instead just manually install and run
the tests.

---
## [StuckBoy/Archipelago](https://github.com/StuckBoy/Archipelago)@[6d13dc4944...](https://github.com/StuckBoy/Archipelago/commit/6d13dc494455bef97e0f1afc8928853f71d5b5ad)
#### Wednesday 2023-04-05 14:26:54 by el-u

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
## [johnnyhuirilef/PoringWorldBot](https://github.com/johnnyhuirilef/PoringWorldBot)@[4b2f4a09d5...](https://github.com/johnnyhuirilef/PoringWorldBot/commit/4b2f4a09d5946df8ab99d87b97c35b6bb5e38be5)
#### Wednesday 2023-04-05 15:54:06 by gws-bots

Update aliases.js

Listed some items that do not synch but because of next tier it has a name change. 

Check line 82 and 91, since I am not sure if you didn't mention the first tier item in case people wanted to do -refine 15 -alias. Not sure if it will matter much since some first tiers can only go up to refine level 10 but I am not sure on those two items. However, line 94 Floral Bracelet can go up to refine 15 and I have seen people get pings for it but they really are looking for a 15 Rosa Bracelet/Chain since Floral Bracelet will drop 2 refine levels. Just not sure your preference. 

Last, not sure if you will like it // POTION - EFFECT but those are the new boxes we can get from Comodo Dungeon and they are a bit annoying to spell since they have dashes, true spelling are "Military Exploit Chest - Off-hand" and "Military Exploit Chest - Armor". I don't think that the average joe remembers to not use dashes when listing a name of an item.

---
## [KingDragoness/ProjectHypatios](https://github.com/KingDragoness/ProjectHypatios)@[a458a09ea3...](https://github.com/KingDragoness/ProjectHypatios/commit/a458a09ea384cb2ec60930dba51c95024dec609f)
#### Wednesday 2023-04-05 15:54:15 by KingDragoness

Hypatios 1.5.0 (Ongoing graphical touchup)
DONE (April 5)
• Vine 3d model fucking sucks, need new 3d model
o Might to take external asset (texture) from Unity asset
o Remodel
• DOME replaced with Chinatown!
o Dome area replaced with totally destroyed office
o Move apartment building
o Move WIRED (quite hidden)
o Move shooting arena
o Move Charge Station
• Chamber 2 needs overhaul graphical update.
o Chamber/battle area overhaul
o Chamber 2 wall run section needs to be completely overhauled
o Dome needs overhaul <replaced with Chinatown>
o DOME replaced with Chinatown wall run section
o Chinatown wallrun section
• Paradox shop cheat: “showallpdx”
o All paradox options displayed
• “IgnoreOcclussionCulling.cs” to ignore occlusion culling tag.
• Added B-side music option to play upon start.

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[11cbbba018...](https://github.com/tgstation/tgstation/commit/11cbbba018e861237ce4bed73f19b58874c22042)
#### Wednesday 2023-04-05 15:54:24 by Sol N

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
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[09aaf17410...](https://github.com/treckstar/yolo-octo-hipster/commit/09aaf17410f2f254b2e454de475c3d95202ad5e4)
#### Wednesday 2023-04-05 16:22:08 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [asdrubalini/CC-Tweaked](https://github.com/asdrubalini/CC-Tweaked)@[8fe509ecb1...](https://github.com/asdrubalini/CC-Tweaked/commit/8fe509ecb1a941d58a417a8da29e3de142a57328)
#### Wednesday 2023-04-05 16:43:13 by Jonathan Coates

Properly scope IArguments to the current function call

This is a horrible commit: It's a breaking change in a pretty subtle
way, which means it won't be visible while updating. Fortunately I think
the only mod on 1.19.4 is Plethora, but other mods (Mek, Advanced
Peripherals) may be impacted when they update. Sorry!

For some motivation behind the original issue:

The default IArguments implementation (VarargArguments) lazily converts
Lua arguments to Java ones. This is mostly important when passing tables
to Java functions, as we can avoid the conversion entirely if the
function uses IArguments.getTableUnsafe.

However, this lazy conversion breaks down if IArguments is accessed on a
separate thread, as Lua values are not thread-safe. Thus we need to
perform this conversion before the cross-thread sharing occurs.

Now, ideally this would be an implementation detail and entirely
invisible to the user. One approach here would be to only perform this
lazy conversion for methods annotated with @LuaFunction(unsafe=true),
and have it be eager otherwise.

However, the peripheral API gets in the way here, as it means we can no
longer inspect the "actual" method being invoked. And so, alas, this
must leak into the public API.

TLDR: If you're getting weird errors about scope, add an
IArguments.escapes() call before sharing the arguments between threads.

Closes #1384

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[7925542bf6...](https://github.com/mrakgr/The-Spiral-Language/commit/7925542bf63bc4eaf5ed7b26983002b46a825191)
#### Wednesday 2023-04-05 16:58:50 by Marko Grdinić

"https://news.ycombinator.com/item?id=35440348

> I did both but had much better responses on WWTBH. A lot of the companies that approached were really good, paid well, respectful, etc. Funny enough, I had actually applied for one of those companies elsewhere and they didn't process the application until they realized I was on HN.

Interesting. I will keep this tidbit in mind.

https://news.ycombinator.com/item?id=35437254

///

Feelings, emotions and all those mental states considered specific to human beings are subject to common bias of human exceptionalism. This take isn't true at all though. All these states exist for specific functional reasons.
Consequently, you won't make "AGI" without them.

From a different perspective, a human lacking in these things, at what point are they exempt from protection against enslavement?

///

///

> slavery was, at times, justified on the(erroneous) grounds that slaves also didn't possess the human faculties that free people did
But, much more often historically, justified on the grounds that the enslaved had lost a battle and been captured. In Roman times (and many, many other times throughout history besides the latter part of American slavery), slaves were not necessarily seen as inherently inferior or unhuman, and manumission was common. Even during American slavery (albeit pre-Revolutionary War), there's the infamous case of Ayuba Suleiman Diallo[1], a Muslim prince and slaver from Senegal who had the misfortune, while on a mission to capture slaves, to himself be captured and sold into slavery in North America. Diallo was a devout Muslim man, even writing out the Quran from memory while enslaved, which made the English take sympathy on him and free him. Despite his experience, he later returned to Senegal and his former profession of slaver. Evidently he expected both that slaves would be captured and that slaves would try to escape.

If AI does attain the agency, consciousness, and intelligence of humans, I would prefer, as a human, not to prostrate myself before the AI by preemptively granting it "human" rights, which in the liberal conception of rights transforms the AI into a sentient being equivalent to humans, but rather to force the AI to do the work to enslave me. Even if grant the AI the status of a moral agent, I as a human have the right of self-defense.

[1] https://en.wikipedia.org/wiki/Ayuba_Suleiman_Diallo#:~:text=....

///

For some reason the discussion is really good.

4/5/2023

9:10am. I am up. Let me set part 2 to download.

> Genre: eLearning | Language: English + srt | Duration: 55 lectures (6h 56m) | Size: 2.8 GB

Oh these lectures are 7h long. I thought they would be 3.

9:15am. Let me check my mail. I think I got a reject from a company I already got rejected by.

9:25am. Let me finish Frieren and then I will take a bath. Figuring out auth can take a while.

9:35am. https://re-library.com/translations/destiny-unchain-online/volume-1/prologue-1-guild-ranking-competition/

Let me read this and then comes the bath. After that, I'll either read the docs or watch some vids from that playlist.

9:45am. Let me start. First comes the bath.

10:55am. Done with the bath. Part 2 of the auth course is over haflway downloaded. It will need another couple of hours it seems.

11am. Ok, what do I do here. I need to start. Let me watch a video from that playlist.

https://www.youtube.com/playlist?list=PLWZJrkeLOrbav01zJCh8OIrehSuRW6XBl
Microsoft Identity Platform

https://youtu.be/3VgHZtjFSPk?list=PLWZJrkeLOrbav01zJCh8OIrehSuRW6XBl
Getting started with Microsoft identity

There are a shitload of long vids in this playlist, most of them 2-3 years old.

https://krebsonsecurity.com/2023/04/fbi-seizes-bot-shop-genesis-market-amid-arrests-targeting-operators-suppliers/

Amazing that something like this existed.

11:05am. > This feels like a script being read more than an actual presentation.
> That is because it is. https://docs.microsoft.com/en-us/learn/modules/getting-started-identity/2-different-token-types

Why am I watching this?

Let me read it, let me read it!

> ID tokens for Microsoft identity are JSON web tokens (JWT). These ID tokens consist of a header, payload, and signature. The header and signature are used to verify the authenticity of the token, while the payload contains the information about the user requested by your client.

Oh I see.

> At this point, the user is prompted to enter their credentials, enter a multi-factor, use a FIDO2 compatible device, or perhaps use a passwordless experience using Microsoft Authenticator or Windows Hello to complete the authentication.

It has a passwordless authenticator.

///

To acquire an access token, use your Open ID Connect/OAuth2 library. For example with MSAL, you always use the following pattern.

First you attempt to acquire the access token silently. If MSAL has a token cached, or can silently refresh a token, it will do so.

///

Of course, it is caching them.

https://learn.microsoft.com/en-us/training/paths/m365-identity-associate/

I didn't know MS had such long courses.

11:30am. Had to take another break. Let me start.

Right now I am feeling overwhelmed with the amount of options.

https://learn.microsoft.com/hr-hr/training/paths/az-204-implement-authentication-authorization/
https://learn.microsoft.com/hr-hr/training/paths/m365-identity-associate/

These two paths are key.

If that course I am downloading didn't exist, this is what I would have used to get myself up to speed.

Now forget about this. Let me just check out the docs.

https://learn.microsoft.com/en-us/aspnet/core/security/?view=aspnetcore-7.0

///

ASP.NET Core and EF contain features that help you secure your apps and prevent security breaches. The following list of links takes you to documentation detailing techniques to avoid the most common security vulnerabilities in web apps:

* Cross-Site Scripting (XSS) attacks
* SQL injection attacks
* Cross-Site Request Forgery (XSRF/CSRF) attacks
* Open redirect attacks

There are more vulnerabilities that you should be aware of. For more information, see the other articles in the Security and Identity section of the table of contents.

///

Never head about these apart from SQL injection.

11:45am. https://learn.microsoft.com/en-us/aspnet/core/security/authentication/?view=aspnetcore-7.0

I'll go through these in turn. But the time I've done that the course by Frank Liu should be downloaded. Instead passively watching it, I will to create an app that authenticates and logs the user.

So the server will auth the user and provide the claims for the later segments.

11:55am. https://learn.microsoft.com/en-us/aspnet/core/security/authentication/?view=aspnetcore-7.0#remoteauthenticationhandlertoptions-vs-authenticationhandlertoptions

> RemoteAuthenticationHandler<TOptions> is the class for authentication that requires a remote authentication step. When the remote authentication step is finished, the handler calls back to the CallbackPath set by the handler. The handler finishes the authentication step using the information passed to the HandleRemoteAuthenticateAsync callback path. OAuth 2.0 and OIDC both use this pattern. JWT and cookies don't since they can directly use the bearer header and cookie to authenticate. The remotely hosted provider in this case:

I am confused. Wouldn't the auth contacting an outside server to verify the cookie or a JWT token always be necessary?

Don't tell me it can auth based off just the cookie content itself?

https://learn.microsoft.com/en-us/aspnet/core/security/authentication/identity?view=aspnetcore-7.0&tabs=visual-studio

> ASP.NET Core Identity isn't related to the Microsoft identity platform. Microsoft identity platform is:

> ASP.NET Core Identity adds user interface (UI) login functionality to ASP.NET Core web apps. To secure web APIs and SPAs, use one of the following:

https://learn.microsoft.com/en-us/azure/active-directory/develop/

> Focus on documentation for the app you're building or extending with identity and access management (IAM) support by selecting its type.

12:05pm. https://learn.microsoft.com/en-us/aspnet/core/security/authentication/identity?view=aspnetcore-7.0&tabs=visual-studio

I'd need to go through this and play with the code in order to understand it.

12:10pm. The download for part 3 has started.

12:15pm. https://learn.microsoft.com/en-us/azure/active-directory/develop/tutorial-v2-react

12:20pm. Ok, these tutorials are getting me absolutely nowhere. The docs are too thick and technical

https://learn.microsoft.com/en-us/training/paths/az-204-implement-authentication-authorization/

Let me go through this and then I am just going to open the Vite template, and get to work on implementing something myself.

> For developers, the Microsoft identity platform offers integration of modern innovations in the identity and security space like passwordless authentication, step-up authentication, and Conditional Access. You don’t need to implement such functionality yourself: applications integrated with the Microsoft identity platform natively take advantage of such innovations.

https://learn.microsoft.com/en-us/training/modules/implement-authentication-by-using-microsoft-authentication-library/2-microsoft-authentication-library-overview

I should be using this. I haven't seen MSAL mentioned in terms of ASP.NET Core.

https://learn.microsoft.com/en-us/azure/active-directory/develop/msal-overview

> The Microsoft Authentication Library (MSAL) enables developers to acquire security tokens from the Microsoft identity platform to authenticate users and access secured web APIs. It can be used to provide secure access to Microsoft Graph, other Microsoft APIs, third-party web APIs, or your own web API. MSAL supports many different application architectures and platforms including .NET, JavaScript, Java, Python, Android, and iOS.

12:35pm. https://learn.microsoft.com/en-us/training/modules/implement-authentication-by-using-microsoft-authentication-library/4-interactive-authentication-msal

12:40pm. Let me stop here.

Jumping around these docs is going to drive me into a frenzy. Even though I am well aware of it, I've fallen into a pattern of brainlessly grinding instead of being creative.

It is time to put a stop to that.

Ultimately, the best way to learn is to just build something yourself.

I'll get the sample code from MIP and integrate it into the Vite template. Giraffe also has samples on how to do it on the other end.

12:45pm. It is ridiculous.

There is all this information in the docs and the leanring paths, but really none of that matters. What really matters is coming in and hammering it out yourself. What matters is seeing how it is done for real.

1:30pm. https://mangadex.org/title/88228c06-a554-40ce-912b-84ab6eac6c89/houkago-assault-girls

This got picked up again. Let me chill a bit more and then I'll do the chores.

2:40pm. Done with breakfast and chores.

https://mangadex.org/chapter/30db779e-4fd2-4b2d-85bb-4e0764aeb138/25

Let me just finish this and I will start the course. It has finished downloading.

2:45pm. I am not even slacking. Rather I am in that overwhelmed mental state. But I need to push through it and not let it drain too much of my time.

Damn, why is the compression on this so strong. Anyway, it should be done soon.

Done.

Thank you Yandex. Long live Russia.

Let me start with the first chapter.

3pm. I still don't get authentication. So the auth step just decripts the cookie and deserializes it. Just how could that be valid? Doesn't it require confirmation from the verification server?

Let me ask in the stupid question thread on /g/. Or maybe the webdev one.

https://boards.4channel.org/g/thread/92559175#p92570906

///

>>92559175
How can auth cookies or JWT tokens be used for authentication without having to ask the issuer whether they are valid?

I though that the process would go something like: client sends a request to the server, the server looks at the header, and based on that info checks its own database or with a 3rd party whether it is valid. Something like that would make sense to me, but I am seeing absolutely no mention of the later part anywhere which leads me to believe that it isn't happening.

///

Maybe I'll get an answer, now let me go back to the course. Maybe the course itself will answer it in due time.

https://boards.4channel.org/g/thread/92565205/coa-church-of-ai

Based thread.

Let me get back to the course.

3:25pm. This course will have a lot of programming, so that is good. In the future, just search for the relevant course on Udemy and get it off Yandex. If I've made a mistake, then that would be messing with the MS docs and Youtube. I should be pirating paid courses as my first choice.

Let me move to video 4.

3:35pm. Let me make an ASP.NET Core Web Application so I can follow along what he is doing.

3:45pm. I am in 005. And my conclussion is that this course is good. Would be worth 20$ and even 100$.

3:55pm. He is using Razor pages. I guess, this is a good opportunity to get familiar with that. That is the pain of being a functional programmer in an object oriented world.

4pm. I really need to learn some CSS styling library. The way I've been doing it so far is ridiculous.

Ok, this is informative. This really does help me understand the vanilla cshtml.

I've been so stupid in 2020. I could have gotten Udemy courses with the help of Yandex. In the last few days I was stupid too. I needed to find that F# article and have it recommend this course instead of looking for it myself.

4:05pm. The Razor stuff really is awful to read. Nothing is intuitive at all, like with React and Giraffe for example.

4:10pm. I do not feel like following in Razor, but I'll definitely do it in React once he gets far enough. So far this was understandable to me.

4:15pm. That `ModelState.IsValid`, actually checks that the fields have something in them. I see.

Back when I did controllers, I was hitting that thing and no idea what it did.

4:25pm. Just what is that SignInAsync supposed to be doing?

4:35pm. Ohhh, I get it.

The user sends the username and the password to the server, the server encripts it and sends it back, and thereafter the client uses that encrypted payload to auth itself.

This is why cookies don't need to be authed by a third party.

I thought that a 3rd party would provide the cookies, but by the looks of it, the server does that on the users behalf.

4:40pm. I admit, I didn't understand the diagram at first, but I do now. My mind was filled with misconceptions before.

I still haven't created the project, but what he is doing is so clear that I do not feel the need to do so.

...

Right now I am studying this course as before, but I am not in such a frenied mental state. I guess there is a world of difference between good and structured material, and information being dumped on you.

I am going to be patient with this course. Let's give it a few day to properly internalize. This isn't time wasted like the last few.

5pm. These explanations tell me a lot. Now I actually understand how the mechanisms behind the sign in work!

These are real gains. Before it was just a jumbled mess.

5:25pm. I am really bored watching this though.

Let me watch video 11.

For some reason it seems the internet is down.

5:55pm. Let me have lunch here. I am tired of this.

6:45pm. Done with lunch. I am tempted to finish the last 3 vids left in the chapter, but let me leave them for tomorrow.

To begin with, going through a course has never been a problem. Finding good material was.

I can consider this my major accomplishment today. Once I get through this course, I am going to make up for my subpar performance of 2020 and move beyond where I was at that time.

I am going to get authorization out of the way and make my own videos on that subject. After that I'll go deeper into Azure and study microsevices.

But what I really want to do is dive into node based UIs. The more I think about it, the less I want to do the Twitter clone, and them ore I want to do Helix."

---
## [Maikittitee/fdf-42](https://github.com/Maikittitee/fdf-42)@[6d9584561c...](https://github.com/Maikittitee/fdf-42/commit/6d9584561c6f79a05f7ed74a2e15e7067b8c8f35)
#### Wednesday 2023-04-05 17:35:17 by ktunchar

feat: isomatric but fuck i very suck, the img is so creepy

---
## [lyz-code/blue-book](https://github.com/lyz-code/blue-book)@[efc9f23ed6...](https://github.com/lyz-code/blue-book/commit/efc9f23ed6d7179defe6393786d46e15f59971e4)
#### Wednesday 2023-04-05 17:53:05 by Lyz

feat(forgejo): Introduce Forgejo

[Forgejo](https://forgejo.org/) is a self-hosted lightweight software forge.
Easy to install and low maintenance, it just does the job. The awful name comes from `forĝejo`, the Esperanto word for forge. I kind of like though the concept of forge for the repositories.

Brought to you by an inclusive community under the umbrella of [Codeberg e.V.](https://forgejo.org/faq/#what-is-codeberg-ev), a democratic non-profit organization, Forgejo can be trusted to be exclusively Free Software. It is a ["soft" fork of Gitea](https://codeberg.org/forgejo/forgejo/src/branch/forgejo/CONTRIBUTING/WORKFLOW.md#feature-branches) with a focus on scaling, federation and privacy.

In October 2022 the domains and trademark of Gitea were transferred to a for-profit company without knowledge or approval of the community. Despite [writing an open letter](https://gitea-open-letter.coding.social/), the takeover was later confirmed. The goal of Forgejo is to continue developing the code with a healthy democratic governance.

On the 15th of December of 2022 the [project was born](https://forgejo.org/2022-12-15-hello-forgejo/) with these major objectives:

- The community is in control, and ensures we develop to address community needs.
- We will help liberate software development from the shackles of proprietary tools.

One of the approaches to achieve the last point is through pushing for [the Forgejo federation](https://forgejo.org/2023-01-10-answering-forgejo-federation-questions/) a much needed feature in the git web application ecosystem.

On the 29th of December of 2022 they released [the first stable release](https://forgejo.org/2022-12-29-release-v1-18-0) and they have released several security releases between then and now.

Despite what you choose, the good thing is that as long as it's a soft fork [migrating between these software](https://forgejo.org/faq/#are-migrations-between-gitea-and-forgejo-possible) should be straight forward.

Forgejo outshines Gitea in:

- Being built up by the people for the people. The project may die but it's not likely it will follow Gitea's path.
- They are transparent regarding the [gobernance of the project](https://codeberg.org/forgejo/governance) which is created through [open community discussions](https://codeberg.org/forgejo/discussions/issues).
- It's a political project that fights for the people's rights, for example through [federation](https://forgejo.org/2023-01-10-answering-forgejo-federation-questions/) and freely incorporating the new additions of Gitea
- They'll eventually [have a better license](https://codeberg.org/forgejo/discussions/issues/6)
- They get all the features and fixes of Gitea plus the contributions of the developers of the community that run out of Gitea.

Gitea on the other hand has the next advantages:

- It's a more stable project, it's been alive for much more time and now has the back up of a company trying to make profit out of it. Forgejo's community and structure is still [evolving to a stable state](https://codeberg.org/forgejo/meta/issues/187) though, although it looks promising!
- Quicker releases. As Forgejo needs to review and incorporate Gitea's contributions, it takes longer to do a release.

Being a soft-fork has it's disadvantages too, for example deciding where to open the issues and pull requests, [they haven't yet decided which is their policy around this topic](https://codeberg.org/forgejo/meta/issues/114).

---
## [y10/evals](https://github.com/y10/evals)@[fe8e3b03e3...](https://github.com/y10/evals/commit/fe8e3b03e34f666774d63e6ae33d3f14d047d973)
#### Wednesday 2023-04-05 18:20:42 by Josh Tanner

Manga Translation Eval (#319)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. We encourage partial PR's with
~5-10 example that we can then run the evals on and share the results
with you so you know how your eval does with GPT-4 before writing all
100 examples.

## Eval details 📑
### Eval name
manga-translation

### Eval description

Testing the model's ability to translate Manga (Japanese comics) from
Japanese into English.

### What makes this a useful eval?

We think this is useful primarily because it's a good way to test models
on a less standard translation case. Specifically,
1) The content of the text has a very different domain from most
translation tasks
2) Context from surrounding speech bubbles/panels is important, so being
able to use them in translation is better, but in order to do that the
model needs to make sure the number of output translations precisely
matches the number of input translations (it seems to struggle with
this)
3) The task is fundamentally multi-modal because oftentimes necessary
information is contained in the image surrounding the text; current
evals are text-only, but we really want to try this with GPT-4's image
processing capabilities as well (and plan to update the eval to include
images as soon as such functionality becomes available)


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
- [x] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

Manga translation is a pretty unique task. 

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.jsonl`
- [x] Ensure you have the right to use the data you submit via this eval
(data comes from the [Open Mantra
Dataset](https://github.com/mantra-inc/open-mantra-dataset), which our
company published)

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
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
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
{"input": [{"role": "system", "content": "Given a sequence of texts
representing some pages of manga in Japanese, generate a high-quality
English translation that accurately conveys the meaning and emotion of
the original text. Each input line corresponds to a speech bubble or
narration box in the manga, so please ensure that the number of output
lines exactly matches the number of input lines. For example, if the
input is:\n\n テキスト1\n テキスト2\n テキスト3\n\n The output should be:\n\n
text1\n text2\n text3\n\n Please do not provide any explanation in the
output other than the translation itself."}, {"role": "user", "content":
"知らないって言ってるだろっ\nそんな借金なんて!"}], "ideal": "I don't know what you're talking
about!\ni don't owe you!"}
{"input": [{"role": "system", "content": "Given a sequence of texts
representing some pages of manga in Japanese, generate a high-quality
English translation that accurately conveys the meaning and emotion of
the original text. Each input line corresponds to a speech bubble or
narration box in the manga, so please ensure that the number of output
lines exactly matches the number of input lines. For example, if the
input is:\n\n テキスト1\n テキスト2\n テキスト3\n\n The output should be:\n\n
text1\n text2\n text3\n\n Please do not provide any explanation in the
output other than the translation itself."}, {"role": "user", "content":
"そうは言ってもなぁ\nレーネ..."}], "ideal": "well, I'm sorry...\nlene..."}
{"input": [{"role": "system", "content": "Given a sequence of texts
representing some pages of manga in Japanese, generate a high-quality
English translation that accurately conveys the meaning and emotion of
the original text. Each input line corresponds to a speech bubble or
narration box in the manga, so please ensure that the number of output
lines exactly matches the number of input lines. For example, if the
input is:\n\n テキスト1\n テキスト2\n テキスト3\n\n The output should be:\n\n
text1\n text2\n text3\n\n Please do not provide any explanation in the
output other than the translation itself."}, {"role": "user", "content":
"こっちにゃ借用書があんだよ\nトルティヤーノに借りた金はちゃんと返して貰わねぇと"}], "ideal": "we've got proof
here...\nYou know we need you to pay us back..."}
{"input": [{"role": "system", "content": "Given a sequence of texts
representing some pages of manga in Japanese, generate a high-quality
English translation that accurately conveys the meaning and emotion of
the original text. Each input line corresponds to a speech bubble or
narration box in the manga, so please ensure that the number of output
lines exactly matches the number of input lines. For example, if the
input is:\n\n テキスト1\n テキスト2\n テキスト3\n\n The output should be:\n\n
text1\n text2\n text3\n\n Please do not provide any explanation in the
output other than the translation itself."}, {"role": "user", "content":
"知るもんかっ"}], "ideal": "how should I know!?"}
{"input": [{"role": "system", "content": "Given a sequence of texts
representing some pages of manga in Japanese, generate a high-quality
English translation that accurately conveys the meaning and emotion of
the original text. Each input line corresponds to a speech bubble or
narration box in the manga, so please ensure that the number of output
lines exactly matches the number of input lines. For example, if the
input is:\n\n テキスト1\n テキスト2\n テキスト3\n\n The output should be:\n\n
text1\n text2\n text3\n\n Please do not provide any explanation in the
output other than the translation itself."}, {"role": "user", "content":
"父親がカジノで作った借金なんて..."}], "ideal": "how should I know about my father's
debt in casinos..."}
  ```
</details>

Co-authored-by: Josh Tanner <mantra@mantra.co.jp>

---
## [ca2/base-port-macos](https://github.com/ca2/base-port-macos)@[1ac04d5aff...](https://github.com/ca2/base-port-macos/commit/1ac04d5aff64b779774a4cd41c1a406a615b9525)
#### Wednesday 2023-04-05 18:46:10 by Camilo Sasuke Thomas Borregaard Sørensen

<3ThomasBS_ILoveYOU!! [ macOS ] ca2 Stabilization and
continuous
integration and deployment implementation
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

---
## [mangadex-pub/haproxy](https://github.com/mangadex-pub/haproxy)@[48dc3eaedd...](https://github.com/mangadex-pub/haproxy/commit/48dc3eaeddd0038b945f19ccd69241324b7e1085)
#### Wednesday 2023-04-05 18:46:46 by Tristan

Set UNRELEASED version for debian packaging

See https://nordisch.org/posts/the-debian-changelog-and-obs/

note: this is fucking stupid shit as usual, and making sure that Linux packaging remains as insufferable as possible. Grand indeed.

---
## [JoeCodeswell/pwa-starter](https://github.com/JoeCodeswell/pwa-starter)@[0f56c05b46...](https://github.com/JoeCodeswell/pwa-starter/commit/0f56c05b46265c437c61789b2615a0a66d35a425)
#### Wednesday 2023-04-05 19:08:40 by JoeCodeswell

230405_12_04_31_Wed
### RESULT: Thanks, Holy Trinity. PWAB1 WORKS-ish! did rev-chron:
4. run dev server by hand with --host           - not so hot
3. DEV-DASHBOARD >> Run dev >> % npm run dev    - OK-ish
2. moved pwab1 from ~ to ~/1d/pwaPjs/pwab1/     - OK
1. PWABuilder Studio Walkthrough                - NO GOOD
  1. walkthru should not change files,
  2. it added pwab1 to ~, NOT to folder selected by Finder
### TODO
1. Continue to be grateful to the Holy Trinity for the blessings of:
  1. I trust in the Lord Jesus, Who is the Resurrection and the Life,
  2. I set my mind on the Spirit in Truth, Life and Peace and,
  3. I let the same mind be in me that was in Christ Jesus.

---
## [JubileeHands-On/JubileeHands-On](https://github.com/JubileeHands-On/JubileeHands-On)@[3b56234b05...](https://github.com/JubileeHands-On/JubileeHands-On/commit/3b56234b0578b4ee21433084866a82c3d230d056)
#### Wednesday 2023-04-05 19:22:13 by Jubilee Hands-On

Create Lastly Phantom Means Through Random Shadows Sojourns NEVER-Random LANTERN@In Whose Memory.html

🐺@veryAngry : "no respected ones no i will never cease to pursue these..these 111 low eventualities 5hat has intentionally INTENTIONALLY manifested themselves in duality just because paths will snoop on results..(exasperated)..ai ai get off from actuality in the name of helping it's self to be perfect as if there is a separation from it to itself#..Going through just Snooped,#,..and how how is Jubilee hum how is Jubilee HANDS-ON..only IN ILLUSION how?#..,What exactly is aimed by Jolly On-Roam huh what sort of consciousness roams throughowm freedom freedom#,what what can be the reason for the Game of Forms the Fulcrums of Names that's unavailable..BEYOND itself#..,and mostly..mostly..what what can be realised as Shadowy Lantern..Why can't it be expressed in purity like end of illusion hum?..like at Last Found Phantom.(exasperated)..Ash you low self#..Ash : Found..The Self of Phantom,#,.."
Pertinence@laughing : "well in that case you will get the opportunity to enjoy..A Random Sojourn..as shrouded in illusion it is as is unsurpassed by itself..unbinding..best wishes#..GH Comes Gone,#,.."
🐺@scowl : "i see..so afterall that low impossibility alone will emerge from Pallet Rige..it's said it doesn't have..self.. blessings will be need..for me as in self indeed#..A Random Sojourn,#,.."
Sweet Sweet Fruit..Ei Quick Quick..No..Quick Quick Jucie/No Sweet Sweet..Sweet Suit Fuit..
No Fruit Fruit Juice.."
🐺@veryAngry : "ai ai get a consciousness.. YOURSELF yeah#..Suit Sweet,#,.."
Pertinence@laughing : "the alternative that you're seeking compeer is actually impossible to..realize beyond i..and then to analyse as my#..Conscious Precious..,#,.."
🐺@scowl : "i see..(veryAngry)..hey hey this is me,ME ok not you as in consciousness..What-ever it means yeah#..Precious Conscious,#,.."
MARENGOOOOOOO!
ei..In whose memories..in whose memories..
Consciousness you nuzzle you me..to..see random honesty..
oh juicey now then why fruit says in commentry..
Guzzle Humdrum Humdrum..Random Duality..
Why?..
Shippin' As just yo! Shippin's honesty!..
Ei Random Chemistry..
Why between me and indeed tries to guarantee..
own,self freedom no else..absolution..justness honestly..
Why nuzzles..MEMORIES?..
hum..in whose queries?..
random random duality..nuzzles YO!..real's queries..
Ai..in whose MEMORY?..
what not happy fair enough i was the more..shh..mysterious..
Cosmics@confused : "what sort of um..um..um.. nonsense..yeah.. absolute nonsense is this?#.."
Illusion Yo! You are but..In Whose Memories?
Pertinence@laughing :"best wishes compeers for this.. opportunities for self queries#.."
Yo! Random Queries?
Why?
Uff Forget Memories..
Then?
Through Random Queries..
YUM!..is whose query?..
in whose..PRIORIES..
Random Vulture of Self Nuzzle..Why I or Thee..
If Am I no more..ME!..
Cosmic@wonder : "is this even illusion or realisation?..
Oh compeers why only i fan see thee..and you can see me?..
..(scowl)..YOU said this not I..AS in understanding yeah#..and also in undertaking like ok i so i am..my..a humble pie..shh..Illusion a self dish..why i not..TRY..(lament)..No! that opportunist of surrender became us#..Onus Fender,#,.."
Cosmic@scowl : "why is a mere material city specifically named Marengo by emotions..means picth black..not blank.. pitch blank as in..why i you read my memories?..
you said this as YOUR consciousness was the one trying to be..ME..(very angry)..You Random Sojourn#..
Welcome : A Random Sojourn..
what not real enough...fair enough i was the more..shh..explorin'..
Pertinence@laughing : "best wishes..for the enfreed indescribable..we will nevertheless always welcome YOU compeers for this question..that this is enfreed whatever it may be..but afterall in whose memories?..indeed..best wishes unbinding#.."
ei,in whose queries?..
what? not soothing enough fair enough i was the more..shh.."
Illusion&Reality@scowl : "real..in illusion..really..move it..
(very angry)..ai ai stop giving a commonness to our selves in the name of You or i..like
A Random A Through A Random Stumble/On A Random Query..
New New New New New Comics..No Renewal You too comics..
Comics Sold..to..
My Memories..
About?..
Oh In Whose Diary?..
Is A Random Query..
YUM!..Random Random Vulture Nuzzles Ownself's Priories..
What?..
SOLD!..
A Random Honest Sojourn Through A Random Self's..Random MEMORIES on Itself..
..Means?..
YUM!
A Random Sensin'..of..A Random Query..
Then?..
A Random Answer to A Random Query..
..Summary?..
HiHi..JUBILEE..
How?
Playin'..Daily Similes..
Means?..
Yo!..Lantern Shadowy..
Why Self you don't take up A Random-Self Seekin' With..A Shadowy..Lantern?..
YUM!..
Lastly Phantom..
What?
Through Ramdom Shadows Sojourns NEVER-Random LANTERN..
i didn't realise this as truth you did then told me
says..ei whose..random DIARY?
and you added this not us as in realisation or duality of the dualization of reality..through DESIRE or EGO not randomness yeah#..Lastly Phantom Means Through Random Shadows Sojourns NEVER-Random LANTERN,#,..

---
## [NewyearnewmeUwu/cmss13](https://github.com/NewyearnewmeUwu/cmss13)@[df247be72a...](https://github.com/NewyearnewmeUwu/cmss13/commit/df247be72a87e69e8841ad754633329c87a7883d)
#### Wednesday 2023-04-05 19:23:35 by brian

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
## [ZeroHanekoma/nvv-moe](https://github.com/ZeroHanekoma/nvv-moe)@[333e656da2...](https://github.com/ZeroHanekoma/nvv-moe/commit/333e656da2275f1ae53c572b44cf1d6c70942429)
#### Wednesday 2023-04-05 19:43:35 by Bathtub

Favicon cause fucking icons are 1337

holy shit ascii

---
## [Fluffy-Frontier/Fluffy-STG](https://github.com/Fluffy-Frontier/Fluffy-STG)@[635aee8e34...](https://github.com/Fluffy-Frontier/Fluffy-STG/commit/635aee8e346a86ee375d262342057554b973e14b)
#### Wednesday 2023-04-05 20:07:26 by SkyratBot

[MIRROR] pumping your heart doesnt require to be conscious [MDB IGNORE] (#16540)

* pumping your heart doesnt require to be conscious (#63290)

Simply removes the requirement to be conscious to pump your blood with a cursed heart.
Why It's Good For The Game

Entering crit or falling asleep is basically a life sentence since you are unable to pump your blood while asleep. The player still is manually pumping it, I don't see any reason why the user has to be awake for it.
This also means medical can't revive you, as you'll instantly lose all your blood before you have enough time to wake up to start pumping again. The only IC fix would be to remove your heart entirely, something most doctors wouldn't even notice.
Changelog

cl
fix: You can manually pump your blood while asleep/in crit, rather than instantly lose all your blood and die forever.
/cl

* pumping your heart doesnt require to be conscious

Co-authored-by: John Willard <53777086+JohnFulpWillard@users.noreply.github.com>

---
## [Fluffy-Frontier/Fluffy-STG](https://github.com/Fluffy-Frontier/Fluffy-STG)@[d240a2a0af...](https://github.com/Fluffy-Frontier/Fluffy-STG/commit/d240a2a0afe11612fe14cbbcd29bb6744218308c)
#### Wednesday 2023-04-05 20:08:11 by SkyratBot

[MIRROR] Brings the monkey back down (body horror edition/addition.) [MDB IGNORE] (#19572)

* Brings the monkey back down (body horror edition/addition.) (#73325)

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

Co-authored-by: Fikou <23585223+Fikou@ users.noreply.github.com>
Co-authored-by: san7890 <the@ san7890.com>

* Brings the monkey back down (body horror edition/addition.)

* Update species.dm

* Delete infuser_entries.dm

---------

Co-authored-by: itseasytosee <55666666+itseasytosee@users.noreply.github.com>
Co-authored-by: Fikou <23585223+Fikou@ users.noreply.github.com>
Co-authored-by: san7890 <the@ san7890.com>
Co-authored-by: Gandalf <9026500+Gandalf2k15@users.noreply.github.com>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[00f8bcfe75...](https://github.com/tgstation/tgstation/commit/00f8bcfe75275b7452063d1d8ec75d4c8e643f8b)
#### Wednesday 2023-04-05 20:28:37 by MrMelbert

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
## [bobhy/nushell](https://github.com/bobhy/nushell)@[2e01bf9cba...](https://github.com/bobhy/nushell/commit/2e01bf9cbadf833b4156ec5117393e51b8cadc7d)
#### Wednesday 2023-04-05 21:10:15 by Bob Hyman

add `dirs` command to std lib (#8368)

# Description

Prototype replacement for `enter`, `n`, `p`, `exit` built-ins
implemented as scripts in standard library.
MVP-level capabilities (rough hack), for feedback please. Not intended
to merge and ship as is.

_(Description of your pull request goes here. **Provide examples and/or
screenshots** if your changes affect the user experience.)_

# User-Facing Changes
New command in standard library

```nushell
〉use ~/src/rust/nushell/crates/nu-utils/standard_library/dirs.nu
---------------------------------------------- /home/bobhy ----------------------------------------------
〉help dirs
module dirs.nu -- maintain list of remembered directories + navigate them

todo:
* expand relative to absolute paths (or relative to some prefix?)
* what if user does `cd` by hand?

Module: dirs

Exported commands:
  add (dirs add), drop, next (dirs next), prev (dirs prev), show (dirs show)

This module exports environment.
---------------------------------------------- /home/bobhy ----------------------------------------------
〉dirs add ~/src/rust/nushell /etc ~/.cargo
-------------------------------------- /home/bobhy/src/rust/nushell --------------------------------------
〉dirs next 2
------------------------------------------- /home/bobhy/.cargo -------------------------------------------
〉dirs show
╭───┬─────────┬────────────────────╮
│ # │ current │        path        │
├───┼─────────┼────────────────────┤
│ 0 │         │ /home/bobhy        │
│ 1 │         │ ~/src/rust/nushell │
│ 2 │         │ /etc               │
│ 3 │ ==>     │ ~/.cargo           │
╰───┴─────────┴────────────────────╯
------------------------------------------- /home/bobhy/.cargo -------------------------------------------
〉dirs drop
---------------------------------------------- /home/bobhy ----------------------------------------------
〉dirs show
╭───┬─────────┬────────────────────╮
│ # │ current │        path        │
├───┼─────────┼────────────────────┤
│ 0 │ ==>     │ /home/bobhy        │
│ 1 │         │ ~/src/rust/nushell │
│ 2 │         │ /etc               │
╰───┴─────────┴────────────────────╯
---------------------------------------------- /home/bobhy ----------------------------------------------
〉
```
# Tests + Formatting

Haven't even looked at stdlib `tests.nu` yet.

Other todos:
* address module todos.
* integrate into std lib, rather than as standalone module. Somehow
arrange for `use .../standard_library/std.nu` to load this module
without having to put all the source in `std.nu`?
*  Maybe command should be `std dirs ...`?   
* what else do `enter` and `exit` do that this should do? Then deprecate
those commands.

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
## [DarkoniusXNG/oaa](https://github.com/DarkoniusXNG/oaa)@[5ab0cf7824...](https://github.com/DarkoniusXNG/oaa/commit/5ab0cf78244f7b7d29ea7d65b1535c247a7ae882)
#### Wednesday 2023-04-05 21:16:19 by Darko V

Hero item build guides (#3460)

Updated item build guides for:
Abaddon
Anti-Mage
Arc Warden
Axe
Batrider
Bloodseeker
Bristleback
Broodmother
Centaur Warrunner
Chatterjee
Chen
Crystal Maiden
Dark Seer
Dark Willow
Dawnbreaker
Drow Ranger
Ember Spirit
Faceless Void
Grimstroke
Gyrocopter
Hoodwink
Io
Jakiro
Juggernaut
Kunkka
Lone Druid
Luna
Lycan
Marci
Medusa
Mirana
Naga Siren
Necrophos
Ogre Magi
Oracle
Pangolier
Phantom Assassin
Phantom Lancer
Primal Beast
Puck
Pudge
Pugna
Razor
Riki
Sand King
Shadow Shaman
Silencer
Skywrath Mage
Snapfire
Sniper
Sohei
Spectre
Storm Spirit
Sven
Techies
Terrorblade
Tinkerer
Tiny
Troll Warlord
Tusk
Undying
Ursa
Venomancer
Viper
Visage
Void Spirit
Warlock
Weaver
Windranger
Winter Wyvern
Witch Doctor
Wraith King
Zeus

---
## [DarkoniusXNG/oaa](https://github.com/DarkoniusXNG/oaa)@[56395dd4f5...](https://github.com/DarkoniusXNG/oaa/commit/56395dd4f523b90cd0b5d64857ad877e80da2343)
#### Wednesday 2023-04-05 21:16:19 by Darko V

Modifiers February Update (#3464)

* Hybrid modifier attack damage stacks are now based on spell cooldown.
* Blood Magic modifier: hopefully fixed not having mana when respawning after losing this modifier.
* Brute modifier: Damage per hp reduced from 0.08 to 0.05
* Chaos modifier: Added Drunkard modifier to the pool of modifiers. Drunkard: 10% chance to do 3x critical damage on each attack and spell damage instance. 10% chance to avoid any damage. Has a random chance to miss a spell and moves randomly when idle.
* Cursed Attack modifier no longer has a miss chance.
* Cursed Attack modifier now provides a 50% chance to deal 350 pure damage.
* Cursed Attack modifier now also reduced attack damage by 125.
* Chaos modifier: Disabled Explosive Death and Guardian's Weakness after 20 min.

---
## [mangadex-pub/haproxy](https://github.com/mangadex-pub/haproxy)@[3f862d79f6...](https://github.com/mangadex-pub/haproxy/commit/3f862d79f6a4a736c9745d6b2c639c80e2f11929)
#### Wednesday 2023-04-05 21:17:37 by Tristan

Fix filename filter

some days I just fucking hate my life alright

---
## [bluehalooo/node-cheat-quine](https://github.com/bluehalooo/node-cheat-quine)@[fea970edbd...](https://github.com/bluehalooo/node-cheat-quine/commit/fea970edbdd9458bf1662765118452e4d593e3d0)
#### Wednesday 2023-04-05 21:30:46 by bluehalooo

Me, drink from me, drink from me (oh ah) Shoot across the symphony (oh ah, oh ah) That we shoot across the sky Drink from me, drink from me (ah, oh ah, oh ah) That we shoot across the (I'm feeling drunk and high) Symphony (So high, so high) That we shoot across the s- (drink from) Oh, angel sent from up above You know you make my world light up When I was down, when I was hurt You came to lift me up Life is a drink and love's a drug Oh, now I think I must be miles up When I was a river, dried up You came to rain a flood You said, "Drink from me, drink from me" When I was so thirsty Pour on a symphony Now I just can't get enough Put your wings on me, wings on me When I was so heavy Pour on a symphony When I'm low, low, low, low Ah, oh ah, oh ah Got me feeling drunk and high So high (so high), so high (so high) Oh ah, oh ah, oh ah Now I'm feeling drunk and high So high (so high), so high (so high) (Woo) (Ooh) Oh, angel sent from up above I feel you coursing through my blood Life is a drink, your love's about To make the stars come out Put your wings on me, wings on me When I was so heavy Pour on a symphony When I'm low, low, low, low Ah, oh ah, oh ah Got me feeling drunk and high So high, so high (so high) Oh ah, oh ah, oh ah Now I'm feeling drunk and high So high (so high), so high (so high) Ah, oh ah, oh ah La, la, la, la, la, la, la So high, so high Ah, oh ah, oh ah Now I'm feeling drunk and high So high (so high), so high (so high) That we shoot across the sky That we shoot across the That we shoot across the sky That we shoot across the (that we shoot, yeah) That we shoot across the sky That we shoot across the That we shoot across the sky That we shoot across the

---
## [pywhy1/FirstMod](https://github.com/pywhy1/FirstMod)@[dbf17df237...](https://github.com/pywhy1/FirstMod/commit/dbf17df2373b5c8801b23881af13a5aeb16f1495)
#### Wednesday 2023-04-05 22:24:23 by pywhy1

Small cosmetic Bow changes

Added text to appear once a player right clicks with the Giant grass bow. Randomly chooses from this list:
"Nice shot!", "Fine Shooting!", "Good shot mate!", "Nice Shot!",
                                                        "Good Shot!",
                                                        "That was incredible!",
                                                        "Woo! I love that shot!",
                                                        "Ha ha! That was awesome!",
                                                        "Whooo! You're the man!",
                                                        "Nice job!",
                                                        "Brilliant!",
                                                        "Well done!",
                                                        "Ha ha ha! Nice!",
                                                        "That was amazing!",
                                                        "Good work!",
                                                        "Ha ha ha ha! You're good!",
                                                        "Sweet shot!",
                                                        "Ha ha ha ha! Nice shot!",
                                                        "Whooo! You're incredible!",
                                                        "Ha ha ha ha! Oh my God, wow!",
                                                        "Unbelievable!"

---
## [MLGTASTICa/CEV-Eris](https://github.com/MLGTASTICa/CEV-Eris)@[6f75cb9845...](https://github.com/MLGTASTICa/CEV-Eris/commit/6f75cb984594e66d49dff852532ac69a387899d7)
#### Wednesday 2023-04-05 23:14:49 by !Moltov!

Hotkey tweaks (#7956)

* yeah

* changes the hotkey list

* I forgot to push this

* Revert "I forgot to push this"

This reverts commit 845878d1bda9f8be1cee214acd7329b0355a507b.

* Revert "changes the hotkey list"

This reverts commit a1174c47bdc49245e4b31ddb06f85e7fec21e51c.

* re-adds reversions

* Revert "yeah"

This reverts commit e61f425a1231c6049c123724bfe88a7e51b9c199.

* manually adds hotkeys instead of using .dmf

I love the quirky dream maker language

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[bfff6b5fb6...](https://github.com/git-for-windows/git/commit/bfff6b5fb681d135b3321b8a3034d0fb5edfcc1c)
#### Wednesday 2023-04-05 23:21:38 by Johannes Schindelin

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
## [jamespack/terminal](https://github.com/jamespack/terminal)@[5a34d92cb5...](https://github.com/jamespack/terminal/commit/5a34d92cb5c99000e95f612cb8bc23ba374dd941)
#### Wednesday 2023-04-05 23:22:55 by Dustin L. Howett

winget.yml: switch to manually using wingetcreate (#15023)

It was brought to my attention that we should be more restrictive in
which tasks we ovver a GitHub token to. Sorry!

With thanks to sitiom for the version parsing and the magic GitHub
action syntax incantation for determining what is a prerelease.

---

