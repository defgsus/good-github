## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-12-27](docs/good-messages/2022/2022-12-27.md)


1,929,859 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,929,859 were push events containing 2,694,268 commit messages that amount to 177,573,947 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 66 messages:


## [voc/jev22_schedule](https://github.com/voc/jev22_schedule)@[4fd6974dbf...](https://github.com/voc/jev22_schedule/commit/4fd6974dbf109ea8ec1f78c97172983142f7e686)
#### Tuesday 2022-12-27 00:20:13 by viri

version 2022-12-27 01:20; FireShonks 0.29; Reconnect To Chaos! 2.1; Hellarious: Hacking in Hell 0.4 final; Curious Community Labs Chaos Experience 0.2.0; xrelog22: Independent Multiverses 1.7; Wintergalaktische Club Mate Party 0.5; ChilyConChaos 2022-12-27 01:20; Winterchaos 0.4; Hacking in Parallel 0.10; Forum für Freiräume - Gib Uns Mehr! 0.37; End-of-Year event 0.2; DWeb NY Pre-kickoff + RemoteCCC @ Woodbine 0.1

---
## [WilldooIT/odoo](https://github.com/WilldooIT/odoo)@[61270ee8bf...](https://github.com/WilldooIT/odoo/commit/61270ee8bffb6e85f8ff0d19c7a3889fdce2f486)
#### Tuesday 2022-12-27 00:21:30 by qsm-odoo

[FIX] website, *: allow to re-edit company team snippet images

*: website_sale

Since [1], it was not possible to edit a company team snippet image
anymore as soon as the page was saved once. Indeed that commit added
o_not_editable/contenteditable="false" on the parent column to make sure
no text can be added in that column and contenteditable="true" on the
images so that they are still editable (even though HTML-specs-wise
adding contenteditable="true" on images probably does not mean much as
images are self-closing tags, our editor understand that as the ability
to edit the image anyway). That contenteditable="true" part is however
removed when leaving edit mode... and was not restored upon entering
edit mode again.

This fixes the problems with a specific JS patch, we'll review to see if
better can be done in master.

Funny enough, that bug was actually gone in 15.0... by mistake. A recent
bug fix actually reintroduced that isolated bug at [2] (by reintroducing
the fact that images in a non-editable environment are not possible to
edit). The 3 opened tickets this commit mentions were actually reported
for 15.0 immediately after that, while the 14.0 being broken about this
since the beginning apparently did not bother anyone.

Note: as a forward-ported fix, this also takes the opportunity to clean
a bit what was done at [3]. (calling `_super`, no duplicated code,
adding comments, ...).

[1]: https://github.com/odoo/odoo/commit/656cac1bf21c7c5a56aa569008aac58436c747fb
[2]: https://github.com/odoo/odoo/commit/e113bae04a64a8bd341a80736086ab7c25079dd3
[3]: https://github.com/odoo/odoo/commit/e2f7b8fad76dc816b2f6864340d3740446117cdb

opw-3031217
opw-3032482
opw-3035289

closes odoo/odoo#104193

X-original-commit: e7c8fed8e373d7005c16c88d3a7bad6f425d13e5
Signed-off-by: Romain Derie (rde) <rde@odoo.com>
Signed-off-by: Quentin Smetz (qsm) <qsm@odoo.com>

---
## [voc/jev22_schedule](https://github.com/voc/jev22_schedule)@[4818eb03d8...](https://github.com/voc/jev22_schedule/commit/4818eb03d80628210c45f1b10c2f6340db57ac11)
#### Tuesday 2022-12-27 01:00:13 by viri

version 2022-12-27 02:00; FireShonks 0.29; Reconnect To Chaos! 2.1; Hellarious: Hacking in Hell 0.4 final; Curious Community Labs Chaos Experience 0.2.0; xrelog22: Independent Multiverses 1.7; Wintergalaktische Club Mate Party 0.5; ChilyConChaos 2022-12-27 02:00; Winterchaos 0.4; Hacking in Parallel 0.10; Forum für Freiräume - Gib Uns Mehr! 0.37; End-of-Year event 0.2; DWeb NY Pre-kickoff + RemoteCCC @ Woodbine 0.1

---
## [Justice12354/tgstation](https://github.com/Justice12354/tgstation)@[0747099063...](https://github.com/Justice12354/tgstation/commit/074709906301e3e396179c861ca0af068c3f36ec)
#### Tuesday 2022-12-27 01:12:07 by RikuTheKiller

Adds a reagent injector component and BCI manipulators to all circuit labs (#71236)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

This PR adds a reagent injector component that's exclusive to BCIs.
(Requested to be integrated into BCIs by Mothblocks.)
When outside of a circuit, the component itself stores the reagents.
However, if it's inside of a BCI, the storage is moved to the BCI. The
storage can contain up to 15u of reagents and acts like an open
container. (However, it won't spill even if you throw it, it just acts
like an open container code-wise, don't worry about it.)
You can only have one reagent injector in a circuit. Trying to insert
multiple will give you an error message.
The entire dose is administered at once. (Requirement set by
Mothblocks.)

Please don't try to dispute any of the specific limitations in the
comments as they're out of my control. They're reasonable anyways.

Reagent Injector Input/Output:
Inject (Input Signal) - Administers all reagents currently stored inside
of the BCI into the user.
Injected (Output Signal) - Triggered when reagents are injected. Not
triggered if the reagent storage is empty.

New BCI Input:
Show Charge Meter (Number) - Toggles showing the charge meter action.
(Adds some capacity for stealth.)

Install Detector Outputs: (Added following a comment about having to use
weird workarounds for proper loops.)
Current State (Number) - Outputs 1 if the BCI is implanted and 0 if it's
not.
Installed (Signal) - Triggered when the BCI is implanted into it's user.
Removed (Signal) - Triggered when the BCI is removed from it's user.

This PR also adds BCI manipulation chambers to all currently present
circuit labs. (Solution proposed by Mothblocks.)
Yes I had to do some other mapping changes to allow for this. No I don't
have any mapping experience, why do you ask?

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

One small step for BCIs, one giant leap for circuit kind. (First
"proper" circuit to human interaction in the entire game!)

This allows for some funky stuff and also makes it less of a pain in the
ass to use BCIs. What's not to love?

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

:cl:
add: Added a reagent injector component and BCI manipulators to all
circuit labs. (+ install detector component)
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

---
## [Justice12354/tgstation](https://github.com/Justice12354/tgstation)@[bf582cb833...](https://github.com/Justice12354/tgstation/commit/bf582cb833d89b7121b4fefa37e8da1773783245)
#### Tuesday 2022-12-27 01:12:07 by Profakos

Trophy case update (#71015)

## About The Pull Request

I have been chipping away/procrastinating at this since May, but after
several years, I have finally updated how Trophy Cases work.

So, what this PR does is the following:

- Standardized everything in persistence.dm to use snake case, and added
basic autodocs
- Automatically moves trophies from data/npc_saves/TrophyItems.json to
data/trophy_items.json. Removed legacy .sav conversion by request, it
has been a long time.
- Trophy cases are opened and loaded the same way you would open a
regular ID locked display case (used curator access, relevant access
autodoc has been updated)
- Instead of cheap plastic replicas that turn to dust anyways, trophy
cases use holograms, which can be dispelled by hand
- Trophy data gets saved if an item stays in the trophy case when the
shuttle arrives to centcom, and the item has a description set. This is
in line with paintings, which has to still hang on the wall at round
end.
- You can edit the description of new trophies by using the librarian's
key to unlock History Mode
- When you click on a closed trophy case, it will open a tgui, and will
not display the case description. It will still do for open cases.
Vendatrays have been updated to do the same.
- The UI's icon uses icon2base64(getFlatIcon(showpiece, no_anim=TRUE)).
Vendatrays have been updated similarly, so items with directions and
animations are displayed properly. The base64 strings are updated in
update_static_data.
- Fixes vendatrays from displaying some characters in strange ways, such
as displaying /improper.
- Renames some one letter, or nonindicate argument and var names in
trophy case code
- Adds a trophy management admin panel, where admins can finally delete
all the curator ID cards swallowed over the years. Or, they can replace
the paths with funny new paths.
- If an entry has an incorrect, no longer existing path, it will be
marked red in the management panel
- Adds MAX_PLAQUE_LEN define, which 144 characters
- Removes start_showpieces from trophy cases, as it was completely
unused. The start_showpiece_type var is still around.
- Moves trophy_message var to trophy cases. Only a dice collector
display case used them in the Snowdin map.

What this PR does not do

- Sadly, it still only saves the base image of an item, and no layers or
altered image states. This has to come in the future.

<details>
<summary>Click here to see various states of the trophy tgUI</summary>
 

![kép](https://user-images.githubusercontent.com/2676196/199545412-e5b7e7a8-59fb-41e6-aca5-6b07ba33501c.png)
Locked history mode, existing item.


![kép](https://user-images.githubusercontent.com/2676196/199545574-9e705603-9b7a-457d-9575-2d4145ad940d.png)
Unlocked history mode, but holographic trophy is present.


![kép](https://user-images.githubusercontent.com/2676196/199545883-45c3916b-011f-462a-8296-6eb13db32158.png)
Locked history mode, no item.


![kép](https://user-images.githubusercontent.com/2676196/199545967-a33e2501-aa5f-473b-b79f-ebd950df2afc.png)
Unlocked history mode, no item.


![kép](https://user-images.githubusercontent.com/2676196/199546100-718bd639-3199-4df7-ad77-ed3dbf27b290.png)
Unlocked history mode, item placed, default text. (Note: this picture is
out of date. The typo has been fixed, and "record a message" is now
"record a description" for consistency)
 

![kép](https://user-images.githubusercontent.com/2676196/199546202-5ebbbd28-907c-4f2d-b7cd-29d2ef21c7f3.png)
Unlocked history mode, item placed, new text.

</details>

<details>
<summary>Click here to see the admin panel</summary>


![kép](https://user-images.githubusercontent.com/2676196/199553349-8684f23f-4699-42f2-a27e-15cccad29d0b.png)


</details>

## Why It's Good For The Game

Less curator ID's stuck in the Trophy Cases, and the existing ones can
be cleaned up. A more immersive Trophy Case user experience, in general.

## Changelog


:cl:
refactor: refactored trophy cases, to be more user friendly
admin: created a trophy managment admin panel
/:cl:

---
## [voc/jev22_schedule](https://github.com/voc/jev22_schedule)@[d69e7cbaa1...](https://github.com/voc/jev22_schedule/commit/d69e7cbaa16031ed07f2c5da10019301f8ac9ed4)
#### Tuesday 2022-12-27 01:20:12 by viri

version 2022-12-27 02:20; FireShonks 0.29; Reconnect To Chaos! 2.1; Hellarious: Hacking in Hell 0.4 final; Curious Community Labs Chaos Experience 0.2.0; xrelog22: Independent Multiverses 1.7; Wintergalaktische Club Mate Party 0.6; ChilyConChaos 2022-12-27 02:20; Winterchaos 0.4; Hacking in Parallel 0.10; Forum für Freiräume - Gib Uns Mehr! 0.37; End-of-Year event 0.2; DWeb NY Pre-kickoff + RemoteCCC @ Woodbine 0.1

---
## [ArcaneMusic/TG-Station-Arcane-Remix](https://github.com/ArcaneMusic/TG-Station-Arcane-Remix)@[c1f0141967...](https://github.com/ArcaneMusic/TG-Station-Arcane-Remix/commit/c1f01419671ad084a6c048ec7900d008de53bfe2)
#### Tuesday 2022-12-27 01:52:46 by LemonInTheDark

Fixes mineral turfs having weird lighting (#71219)

## About The Pull Request

Pixel offsets, unlike transforms, offset overlays too. this was breaking
lighting overlays for mineral walls.

We did pixel offsets to save on init time, but we can acomplish the same
thing using an initial matrix. It's static, so there's no additional
cost. S free

Damn moth

## Changelog
:cl:
fix: Mining walls won't have fucked lighting anymore
/:cl:

---
## [pedr69/vgstation13](https://github.com/pedr69/vgstation13)@[e6156a8d91...](https://github.com/pedr69/vgstation13/commit/e6156a8d91d8a24ebe6437f07198713f76946fc1)
#### Tuesday 2022-12-27 02:13:14 by samo priimek

pulse demon tweaks (#33690)

* remove the stupid maxcharge tweak

* sneed

* comment unused stuff

* revert everything

* prevent you from killing yourself stupidly

* suck SMES faster, gain maxcharge when sucking APC's

* remove the capacity upgrade

* tweak the ability costs and upgrades

---
## [Ryll-Ryll/tgstation](https://github.com/Ryll-Ryll/tgstation)@[cf02f62298...](https://github.com/Ryll-Ryll/tgstation/commit/cf02f622986932af8fb09e48cbdf5ec0ac567cf5)
#### Tuesday 2022-12-27 02:18:39 by LemonInTheDark

useless update_appearance reduction, emissive_blocker micro optimization (saves a second of init) (#71658)

## About The Pull Request

[Saves 0.2 seconds of init time. 50% of emissive
blockers](https://github.com/tgstation/tgstation/commit/8318b648f6d32844aacbfb4c309152cd45801f5c)

Emissive blockers are a decent expense during init, even these, which
are the ones that update outside of initialize.
I've inlined them, removed some redundant vars and checks, reduced the
arg count, and shifted some things around. This ends up saving 200ms, or
50% of its total cost.

I also shifted mutable_appearance about a bit. it's not a massive
saving, but it is technically faster

[Prevents a few redundant appearance_updates, saves 0.8 seconds of
init](https://github.com/tgstation/tgstation/commit/5475cd778b66b22b1e2c8d86b2c6d59fb84f219a)

Prequisit info: update_appearance is decently expensive
It's good then to only do it if we have a reason to, right?

Me and moth were shooting the shit about just general init time, and we
came up with the idea of tracking which update_appearances actually
"worked" and which didn't.

That bit comes later, let's enjoy the fruits of that work first

First, holograms were calling update_appearance on process, for almost
no reason.
I patched the one event they don't already "react" to, and then locked
it behind a change decection if.
good for live, doesn't impact init.

Next, decals. If you add a decal to something before it inits, it'll
react to the after successful init signal.
The trouble is the same atom could have its appearance updated from this
MORE then once, since decals can be stacked on tiles, and signal
unregisters don't work once the signal is sent.
So we add a flag to track if we've had this happen to us or not, so it
only happens once.
saves 80 ms

Power! lots of things call power_change on init, often more then once.
We'll update appearance for each of those calls, even if only one is an
actual change.
That's silly, better to track what sort of power we're using for our
appearance and go off that changing

This was taking about 300ms. Really stupid

Icon smoothing. After emissive blockers were added, any change to
something's icon smoothing would lead to an update_appearance call.
Nasty shit, specially cause of walls, which don't even use emissive
blockers.
Ok then, so we'll always update appearance for movables, and will allow
turfs that are interested to hook it manually.
Not many of those anyhow
This is slightly a dev ux thing, but it saves 600ms so I think it's
worth it. Rare case anyway

Telecomms:
telecomm machines were updating appearance on process. This is to cover
for them turning on/off on process.
Better then to just check if on actually changed.
This cost adds up midgame, doesn't impact init tho

Materials:
There's this update_appearance call in material on_apply. it doesn't do
anything.
The logs will lie to you and say it does, but it's just like reapplying
emissives. It doesn't need to exist
Saves like 50ms

Canisters:
Live thing, lots of time wasted updating appearance for no reason, lets
see if we change anything first yes?

[Uses defines to wrap update_appearance for
tracking](https://github.com/tgstation/tgstation/commit/4fa82e1c9d93577aadb3c743f17196331f62e67c)

[Undoes _update_appearance changes, instead reccomends 2 regexes to
use](https://github.com/tgstation/tgstation/commit/a8c8fec57a4e43d1fa636b5ac68459903faa9fc5)

I need file and line number for my tracking, so I need to override
update_appearance calls, and also preferably not require every override
of update_appearance to handle dummy file + line args.

So instead, I created a wrapper proc that checks to see if appearanaces
match (they're unique remember, the two of the same visual appearance
will be equivalent)
The trouble is I can't intercept JUST proc calls, or JUST function
definitions with defines. it needs to be both.

So I renamed the /update_appearance proc to /_update_appearance

this way I can capture old uses, and don't need to worry about merge/dev
brain skew

~~It does mean that all update_appearance proc definitions now look
weird tho.
My profiling is leaking into dev ux. I wish I had better templating.~~

**The above is no longer being pr'd**, it's instead just recommended via
a few regexes adjacent to the define.
Smelled wrong anyhow

[Adds a setter for panel_open, so I can update_appearance on
it](https://github.com/tgstation/tgstation/pull/71658/commits/cf1df8a69fc1a816391d085ee7419b14f9fe9167)

## Why It's Good For The Game

Speed

---
## [Ryll-Ryll/tgstation](https://github.com/Ryll-Ryll/tgstation)@[176f7a0e42...](https://github.com/Ryll-Ryll/tgstation/commit/176f7a0e422b8417456e1ab65fa59e7ee88a16c5)
#### Tuesday 2022-12-27 02:18:39 by san7890

Traitor UI only shows Unlock/Failsafe Code if you have it (#72114)

## About The Pull Request

There are cases in which you don't have an unlock code (if the uplink is
implanted in you from the start) and you obviously don't always start
with with a failsafe code (need to buy it). So, let's only fill in this
fields in the UI should they exist.

There might be something to be said about wanting to ensure that people
remember that they can check this UI screen to find the failsafe code
should they lose it later, and I wouldn't mind changing the string to be
something like "Failsafe: None" in that case. However, I just think that
keeping it as:

```txt
Code:
Failsafe:
```

is silly and should be changed somehow.
## Why It's Good For The Game


![image](https://user-images.githubusercontent.com/34697715/208604758-d7ff3ae9-e552-4dd2-998d-81715cd06ffc.png)

Note: That white box isn't part of the UI, that's a part of the edit I
did to the screenshot in the area where the stuff... isn't? What was i
thinking

I think the UI looks a lot cleaner for those cases when you just don't
have anything.
## Changelog
:cl:
qol: The Traitor's Antagonist Panel's Unlock and Failsafe entries will
only appear if there is an Unlock/Failsafe Code to display.
/:cl:

---
## [ZephyrTFA/tgstation](https://github.com/ZephyrTFA/tgstation)@[99537d0123...](https://github.com/ZephyrTFA/tgstation/commit/99537d0123167a07b242c33dad7c23ec9a5becef)
#### Tuesday 2022-12-27 02:31:04 by LemonInTheDark

Fixes parallax on >2 level maps going fucky with optimized multiz (#72169)

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

---
## [HandsomeMichael/BuilderTDM](https://github.com/HandsomeMichael/BuilderTDM)@[393102866d...](https://github.com/HandsomeMichael/BuilderTDM/commit/393102866d87831ddb9b58d35abe0ec0efbdee08)
#### Tuesday 2022-12-27 02:51:44 by Handsome Michael

make the repo look better so people know this mod 

The Industrial Revolution and its consequences have been a disaster for the human race. They have greatly increased the life-expectancy of those of us who live in “advanced” countries, but they have destabilized society, have made life unfulfilling, have subjected human beings to indignities, have led to widespread psychological suffering (in the Third World to physical suffering as well) and have inflicted severe damage on the natural world. The continued development of technology will worsen the situation. It will certainly subject human beings to greater indignities and inflict greater damage on the natural world, it will probably lead to greater social disruption and psychological suffering, and it may lead to increased physical suffering even in “advanced” countries.

---
## [Lamella-0587/Skyrat-tg](https://github.com/Lamella-0587/Skyrat-tg)@[ae02bd97ff...](https://github.com/Lamella-0587/Skyrat-tg/commit/ae02bd97ff71d2f4714b4ea7c8076acf21ed06c6)
#### Tuesday 2022-12-27 03:21:42 by OrionTheFox

Gunset case resprite (#18119)

* Noice Icons

* smol

* ccode 4 icon

* Fuck it. We Webedit.

* Oh this should go too

* i hate commas anyways

Co-authored-by: Tom <8881105+tf-4@users.noreply.github.com>

Co-authored-by: Tom <8881105+tf-4@users.noreply.github.com>

---
## [jlsnow301/tgstation](https://github.com/jlsnow301/tgstation)@[b174af7661...](https://github.com/jlsnow301/tgstation/commit/b174af7661cbfaf564292caabfccca18619bda23)
#### Tuesday 2022-12-27 03:48:09 by Jacquerel

Basic Mob Carp Part VIII: Basic Mob Carp (#72073)

## About The Pull Request

Wow we're finally here. This turns carp into Basic Mobs instead of
Simple Animals.
They use a variety of behaviours added in previous PRs to act in a
marginally more interesting way than they used to.
But don't worry there's still 2 or 3 PRs to follow this one until I'm
done with space fish.

Changes in this PR:
Carp will try to run away if they get below 50% health, to make use of
their "regenerate if not attacked" component.
Magicarp have different targetting behaviour for spells depending on
their spell;
- Ressurecting Carp will try to ressurect allied mobs.
- Animating Carp will try to animate nearby objects.
- Door-creating Carp will try to turn nearby walls into doors.

You can order Magicarp to cast their spell on something if you happen to
manage to tame one.
The eating element now has support for "getting hurt" when you eat
something. Carp eating can rings and hating it was too soulful not to
continue supporting.

## Why It's Good For The Game

Carp are iconic beasts and I think they should be more interesting.
Also we just want to turn mobs into basic mobs anyway.

## Changelog

:cl:
add: Carp will now run away if their health gets low, meaning they may
have a chance to regenerate.
add: Lia will now fight back if attacked instead of letting herself get
killed, watch out!
balance: Magicarp will now aim their spells more intelligently.
add: Tame Magicarp can be ordered to use their spells on things.
refactor: Carp are now "Basic Mobs" instead of "Simple Mobs"
fix: Dehydrated carp no longer give you a bad feeling when they're your
friend and a good feeling when they're going to attack you.
balance: Tamed carp are now friendly only to their tamer rather than
their whole faction, which should make dehydrated carp more active.
Order them to stay or follow you if you want them to behave around your
friends.
/:cl:

---
## [jlsnow301/tgstation](https://github.com/jlsnow301/tgstation)@[125745d232...](https://github.com/jlsnow301/tgstation/commit/125745d232163406c107d3947b87d6d406ac3a17)
#### Tuesday 2022-12-27 03:48:09 by Fikou

guardian death checks (#72251)

## About The Pull Request
if a guardian summoner is dead during the summoner setting process, we
(the guardian) now kill ourselves since itd mean a guardian that cant
die
to combat some fucked upness of it (if you inject a guardian and it only
spawns after you died and then dusts you), the process of spawning a
guardian from the playerside guardian creator stuff gets canceled if
youre dead or dont exist

## Why It's Good For The Game
yeah that seems good

## Changelog
:cl:
fix: guardian spirits check for death before they add themselves to you
/:cl:

---
## [i3roly/CMI8788](https://github.com/i3roly/CMI8788)@[001b775bf9...](https://github.com/i3roly/CMI8788/commit/001b775bf9580bb94421c74b175e1b8ddbf7d5a1)
#### Tuesday 2022-12-27 03:54:57 by gagan sidhu

move trigger,adjust volumehandler db val, TIM COOK WENT FULL <you know what>

- the reason there is no volume control for the output is because i fucked up the DB scale.
	-it seems APPUL is using a weird approach; their example code sets a maxDB value of 22.5 by (22 << 16) + 32768, where their vol range is 65535 (https://opensource.apple.com/source/IOAudioFamily/IOAudioFamily-183.4.2/Examples/Templates/SamplePCIAudioDriver/SamplePCIAudioDevice.cpp.auto.html)
		- is each DB equivalent to 65535 or something?
			-still thinking about this. if 255 is our max, then maybe the min should be -6000*(max - min) (??)

- i think the reason the kernel panics when loading the driver and selecting an input device (in volume controls) is how i configured the controls, so this will require testing.

- i moved trigger to after we activate the engine, see the comments.

i've been preoccupied with this dope u-boot @danielschwierzdeck made. trying to get the httpd daemon on it. god it's so fucking sick.
	-piece of shit fucking maxlinear @prpl-foundation refuse to share a working driver because they don't want to be an accessory to the ARM murder that is going to follow
		-interaptiv is going to beat that ass and everyone knows it.

and of course, ol' block-head, four eyes, suspender-slapper TIMMAY (literally TIMMAY from south park) went FULL YOU KNOW WHAT, riding shotty with his fat ride-or-die bitch OPRAH gorging on that APPUL stock.

https://www.youtube.com/watch?v=X6WHBO_Qc-Q

(love u long time ben)

what an insult to the OSX operating system philosophy, fucking block-head.

---
## [warithr621/Comp-Programming](https://github.com/warithr621/Comp-Programming)@[34c45325b9...](https://github.com/warithr621/Comp-Programming/commit/34c45325b9a5213d8e346956ca0c2d279b060bde)
#### Tuesday 2022-12-27 04:10:13 by warithr621

virtual 1772 ABCDEF + upsolve 1760 E

lmao there's no way I should've been able to answer 6 on that contest :skull:
- A: ez
- B: ez
- C: interesting constructive algo
- D: weird NT
- E: goofy game theory (dec 2022 flashbacks)
- F: oh my god I hate implementation and writing like six quintillion lines of code

;-;

---
## [nikothedude/Skyrat-tg](https://github.com/nikothedude/Skyrat-tg)@[460ab7adf5...](https://github.com/nikothedude/Skyrat-tg/commit/460ab7adf560856148d46233e3cde565d05354a4)
#### Tuesday 2022-12-27 04:10:43 by SkyratBot

[MIRROR] JPS Optimization (Light Botcode) [MDB IGNORE] (#17669)

* JPS Optimization (Light Botcode) (#70623)

## About The Pull Request

Alright. So.
Right now, JPS works like this:
```
code requests path
we enter the actual pathfinding
pathfinding sleeps when it overruns a tick
if it sleeps, it'll then wake up before the mc starts
continue
```
This has annoying side effects. Primarily that we have no real control
over JPS, we just sorta have to eat its cost.
So if there's like 10 different things pathfinding at once, the mc will
have no time to do anything. Hell we might even end up eating into
maptick's time if the jps work is expensive enough (note the cost of
sleeping is not accounted for, and that has overhead)
This has happen before, usually when someone makes a lot of bots, and
it's really annoying.

So then, lets put JPS on a subsystem. That way the MC has control over
it.
But wait, existing code expects to yield and get back a path list, and
that's a sane request.
This is solvable, but requires abusing pass by reference lists, and the
ability to make callbacks into partials (preinsert arguments into them
before they're called, and accept other args later)

Because of this, we can now pass callbacks into pathfinders, allowing
for async use, rather then JUST yielding.

Of note: I've removed the 10 pathfinding datums limit, since
ratelimiting like that is handled nicely by the MC.
I've also removed the 15 second timeout, since mc yielding would trigger
it too often. I'm unsure if this means we don't have exit conditions for
pathfinding, need to talk to ryll. (@ Ryll-Ryll what happens if jps just
like, fails to find a path?)

Also of note: I think bots will fire off more then one pathfinding
attempt at a time if their first takes too long to complete. This is
dumb, why do we do this?

Optimizes JPS by more then 40% by removing redundant for(thing in turf)
loops, and avoiding making proc calls if objects are non dense.
This makes things slightly more fragile, but saves a LOT of time. I
think it's worth it, tho talking to mso it might be possible to do
better. Maybe I should do a LINDA system style thing. (I did a linda
system style thing I fixed it)

Optimizes botscanning, fixes bots not seeing things adjacent to them
The list of types could be a cached typecache
We could inline both checkscan and check_bot
check_bot SHOULD NOT BE CALLED ON EVERY OBJECT IN VIEW HOLY SHIT WHY
We don't need to process adjacent and the shuffled view separately, it's
in fact easier to process them in one block
Renames a var

Moves bot's pathing images to above most floor objects, so they're
visible in maint

## Why It's Good For The Game

Speed. Also manuel will stop killing their server by placing 20000
medibots (fucking icebox man every time)

## Changelog

:cl:
fix: Bots will now "notice" you if you're standing right next to them
fix: Bot paths will now draw above things like pipes, rather then below
them
refactor: Changed how pathfinding paths get generated
refactor: Made pathfinding and bot searching significantly faster
/:cl:

Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>

* JPS Optimization (Light Botcode)

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>
Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>

---
## [Mmellet/Blank](https://github.com/Mmellet/Blank)@[36380bc31e...](https://github.com/Mmellet/Blank/commit/36380bc31ea2203d3dad31068f29eb800c055b94)
#### Tuesday 2022-12-27 04:32:35 by Margot Mellet

Let me but escape into my laboratory door, give me but a second or two to mix and swallow the draught that I had always standing ready; and whatever he had done, Edward Hyde would pass away like the stain of breath upon a mirror; and there in his stead, quietly at home, trimming the midnight lamp in his study, a man who could afford to laugh at suspicion, would be Henry Jekyll.

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[47fc3048fa...](https://github.com/treckstar/yolo-octo-hipster/commit/47fc3048fae7c2ac7d0b9c56a3febe93b231fc9a)
#### Tuesday 2022-12-27 05:22:04 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [Offroaders123/Librar.io](https://github.com/Offroaders123/Librar.io)@[2af5169111...](https://github.com/Offroaders123/Librar.io/commit/2af51691112da93e711d9a815ddf41b160dfff0e)
#### Tuesday 2022-12-27 05:42:40 by Offroaders123

TS Refactor!

Well, kinda. It's JSDoc JavaScript, haha. Now that I have editor type-safety, I redid a buch of the code where it was starting to stink XD

Found some confusing recursive function calls along the way, and having type checking made it much easier to tell what the kinds of data I was working with. Some examples of this were the interactions between `readdir()` and `dirtree()`, which had some extra handling and recursive calls that weren't needed anymore. I removed the `Array.prototype.flat(Infinity)` calls alongside that too, and that helped slim things down. I wasn't using the recursive option anywhere in the codebase, so it didn't have to be around anymore. It was making those two functions more complicated than they had to be, too, and now it's more straightforward as to what they each do.

I also simplified the `DirTree` interface, now it only has the `value` property, rather than two optional properties, `value` and `handle`, which would appear in separate situations. Now it's simply just a union type!

I love it! Opening up this codebase again is really cool, I've learned a lot about a ton of different things since I started making this, so now I'm thinking of how I can build this app in a different way now, in a more TypeScript-y way or something, haha.

This was my first ESM-based web app structure, so I had only scratched the surface of breaking up the different app components into modules. Now I have a much better idea of what should be grouped together, and what shouldn't. It also makes way more sense of how to hook differnt things together, and how you should break them apart. This was a big slow down for STE I think, looking back at it now. I would write big functions that do a lot of things, and then call each of those from the top level. If the stuff the function did had to be used somewhere else, I had to add a different access point into the function. Now I try to build my things more modularly, so then you can use the smaller parts in other places, rather than only on the inside of the implementation. Hopefully that makes sense? I think that's one of the best things I've learned with ESM actually, how to break up your code into recyclable pieces, rather than having to tape together the outside so it can fit into tons of different locations. Something like that! (Thanks, Marco)

Learned about how to narrow types with `Array.prototype.filter()` and TypeScript/JSDoc! It's not too complex on the TypeScript side, since you have Generic parameters, but I couldn't figure out how to pass a type param to a `.filter()` call using JSDoc. These links present a very similar way to narrow the type returned by the `.filter()` call, it's extra smart!

https://github.com/microsoft/TypeScript/issues/20812#issuecomment-493622598
https://www.typescriptlang.org/docs/handbook/advanced-types.html#using-type-predicates (Just the TS docs for Type Predicates)
https://stackoverflow.com/questions/43118692/typescript-filter-out-nulls-from-an-array/51577579#51577579

I was trying to do the same thing with something like `(fileHandle: FileSystemHandle) => fileHandle is not null`, but `is not` isn't a thing you can do. The inverse works just the same, and it's actually more explicit! `(fileHandle: FileSystemHandle) => fileHandle is FileSystemHandle` Yay!

---
## [aberja/HeroicGamesLauncher](https://github.com/aberja/HeroicGamesLauncher)@[3f6541c8a7...](https://github.com/aberja/HeroicGamesLauncher/commit/3f6541c8a700511cea9f0c9b572a5d2138ee76e3)
#### Tuesday 2022-12-27 07:06:02 by Mathis Dröge

Improve README and developer experience (#1807)

* Update VSCode configuration

* Lots of README changes

- Update our bages; might've overdone it a little, but they're fun to add :^)
- Add badges for Web Technologies used
- Rewrite & bump up system requirements a bit
- Wrap the Language list, Development in a container, and Screenshots in
  <details>; this makes the page load faster and makes it seem less
  daunting
- Add a Flathub badge to the Flatpak section
- Unify Linux install instructions (as much as possible)
- Remove 3rd-party APT repository
  In my opinion, we have enough distribution formats already, and the
  install instructions are a little dodgy
- Add Beta AUR package to the list
- Clarify Windows install instructions by splitting up WinGet and manual
  install
- Make "Development environment" its own section
- Remove Beta and Alpha notes on Windows and macOS build instructions
- Explain what exactly is happening when you run `yarn dev` and in which
  scenarios you might want to use it
- Move the "Back to top" badge to the actual bottom of the page

* Add a Content Security Policy

This doesn't really do much in our situation:
- Just in case someone ever manages to load a website in Heroic's main
  window, no JS can run inside it
- Gets rid of the warning in the console when testing with `yarn dev`

I've tested the Webviews (unaffected) and links to ProtonDB and such
(also unaffected, not sure why though). Please test if this breaks
anything

---
## [arnodorian-r/frameworks_base_](https://github.com/arnodorian-r/frameworks_base_)@[7265abe77a...](https://github.com/arnodorian-r/frameworks_base_/commit/7265abe77a76f848a316640b5da106e882bdbc8a)
#### Tuesday 2022-12-27 07:09:25 by Christopher Tate

Be increasingly aggressive about fstrim if it isn't being run

The current heuristics depend on devices being alive at midnight+ in
order to run periodic background fstrim operations.  This unfortunately
means that people who routinely turn their devices off overnight wind
up with their devices *never* running fstrim, and this causes major
performance and disk-life problems.

We now backstop this very-friendly schedule with an increasingly
aggressive one.  If the device goes a defined time without a background
fstrim, we then force the fstrim at the next reboot.  Once the
device hits the midnight+ idle fstrim request time, then we already
aggressively attempt to fstrim at the first available moment
thereafter, even if it's days/weeks later without a reboot.

'Available' here means charging + device idle.  If the device never
becomes idle then we can't do much without rendering an in-use device
inoperable for some number of minutes -- but we have no evidence of
devices ever failing to run fstrim due to this usage pattern.

A new Settings.Global element (type 'long', called
"fstrim_mandatory_interval") is the source of the backstop time.  If
this element is zero or negative, no mandatory boot-time fstrim will
ever be performed.  If the element is not supplied on a given device,
the default backstop is 3 days.

Adds a new string to display in the upgrading dialog when doing
the fstrim.  Note it is too late for this to be localized, but since
this operation can take a long time it is probably better to have
it show *something* even if not localized, rather than just sit there.

Bug 18486922

Change-Id: I5b265ca0a65570fb8931251aa1ac37b530635a2c

---
## [vincentiusvin/tgstation](https://github.com/vincentiusvin/tgstation)@[cb20ec99f9...](https://github.com/vincentiusvin/tgstation/commit/cb20ec99f9cac1f0ca60da1b9dc912ea4e9eebba)
#### Tuesday 2022-12-27 07:46:18 by san7890

[MDB Ignore] Unit Tests for Invalid Space Turfs (Area Bullshit Edition) (#70967)

## About The Pull Request

So, there's some bullshit with the map loader(?) sometimes where it'll
let space turfs spawn in spots where we REALLY don't want space turfs.
Or, it could also just be a mapper screwing up. Anyways, we might miss
these, so let's set up a broad Unit Test that checks and verifies that
these round-ruining snagglers do _not_ exist.

In order to help me to do this, I standardized and fixed the
nomenclature such that `/area/ruin/space` is default for any map file in
`_maps/RandomRuins/SpaceRuins`, as well as it's subtypes. I also touched
up how we handle shuttle areas in these scenarios. This got a lot of
Unit Test noise filtered out, and is crucial for its functioning. It
should also be how we did it from the start anyways. I added in an
UpdatePaths for any compatible change, but it was completely
non-workable for some of the area type updates.

I also fixed any organic bugs that didn't require an areas type update.
Cool.

Placing space turfs on IceBox:

![image](https://user-images.githubusercontent.com/34697715/199177940-21c64964-1808-41b0-9a92-bf5b82eee2fa.png)

Organically found issues:

![image](https://user-images.githubusercontent.com/34697715/199177972-b27a89de-0e1a-41e5-8fa4-3bee1763b9da.png)

I also added a `planetary` variable to `/datum/map_config` because I
didn't like the hack I was using to see if we had a planetary map, and
I'd rather it just be an explicit variable in the map's JSON.

## Why It's Good For The Game

The less times we get Space Turfs showing up on IceBoxStation, the
better. It also standardizes areas a bit more, which I like (we were
using some incorrect ones in the wrong spots, so those were touched up
in this PR as well). Like, if it's a space ruin, we don't need to use
the lengthy `/area/ruin/unpowered/no_grav` when `/area/ruin/space` does
the same thing.
## Changelog
Nothing in here should concern a player (unless I broke something)

Expect a few commits as I spam unit tests a few times and play
whack-a-mole with bugs.

---
## [threader/hwp6s-kernel](https://github.com/threader/hwp6s-kernel)@[512d73c133...](https://github.com/threader/hwp6s-kernel/commit/512d73c1335a1705bdc80899b67fc0cff8e3a1fd)
#### Tuesday 2022-12-27 07:48:48 by Stephen Boyd

arm: Translate delay.S into (mostly) C

In the next patch we're going to allow machines to override the
__delay() implementation at runtime so they can implement a timer
based __delay() routine. It's easier to do this using C, so lets
write udelay and friends in C.

We lose the #if 0 code, which according to Russell is used "to
make the delay loop more stable and predictable on older CPUs"
(see http://article.gmane.org/gmane.linux.kernel/888867 for more
info). We shouldn't be too worried though, since the next patch
adds functionality to allow a machine to set the __delay() loop
themselves, therefore allowing machines to resurrect the
commented out code if they need it.

bloat-o-meter shows an increase of 12 bytes. Further inspection
of the assembly shows GCC copying the loops_per_jiffy pointer and
the magic HZ value to the ends of __const_udelay() and _delay()
thus contributing an extra 4 and 8 bytes of data to each
function. These two values weren't taken into account in the
delay.S version since they weren't part of the function in nm's
eyes. This means we only really gained an extra 4 bytes due to
GCC's decision to duplicate the loops_per_jiffy pointer in
__const_udelay.

 $ scripts/bloat-o-meter vmlinux.orig vmlinux.new
 add/remove: 0/0 grow/shrink: 2/0 up/down: 12/0 (12)
 function                                     old     new   delta
 __udelay                                      48      56      +8
 __const_udelay                                40      44      +4

Change-Id: Ibfaab52d0f5e09471571be082232db04726d5532
Signed-off-by: Stephen Boyd <sboyd@codeaurora.org>
Reviewed-by: Saravana Kannan <skannan@codeaurora.org>
(cherry picked from commit 8d5868d8205d10a0a8e423f53e9cc9bb3e9d1a34)

Conflicts:

	arch/arm/kernel/armksyms.c
	arch/arm/lib/delay.S
(cherry picked from commit 05df919cc7cd0e92d381699cc71fb3c6d3c9513e)
(cherry picked from commit ed3a5466df0ffdbda1b4551406ddb6d9babee1f1)

---
## [threader/hwp6s-kernel](https://github.com/threader/hwp6s-kernel)@[d3d102751c...](https://github.com/threader/hwp6s-kernel/commit/d3d102751c928a66e479954de11c79783bef9306)
#### Tuesday 2022-12-27 07:48:48 by Stephen Boyd

arm: Move to upstream udelay via timer implementation

This is a squash of a handful of changes and reverts of the
Qualcomm specific implementation:

  Revert "arm: Implement a timer based __delay() loop"

  This reverts commit 976eafa8b18252876e15f861944acf693b07ce7e.

  Revert "arm: Allow machines to override __delay()"

  This reverts commit bc0ef8ab167272890f1aab62928b04a9aeb87ce9.

  Revert "arm: Translate delay.S into (mostly) C"

  This reverts commit 8d5868d8205d10a0a8e423f53e9cc9bb3e9d1a34.

  ARM: 7451/1: arch timer: implement read_current_timer and get_cycles

  This patch implements read_current_timer using the architected timers
  when they are selected via CONFIG_ARM_ARCH_TIMER. If they are detected
  not to be usable at runtime, we return -ENXIO to the caller.

  Furthermore, if read_current_timer is exported then we can implement
  get_cycles in terms of it for use as both an entropy source and for
  implementing __udelay and friends.

  Tested-by: Shinya Kuribayashi <shinya.kuribayashi.px@renesas.com>
  Reviewed-by: Stephen Boyd <sboyd@codeaurora.org>
  Signed-off-by: Will Deacon <will.deacon@arm.com>
  Signed-off-by: Russell King <rmk+kernel@arm.linux.org.uk>

  ARM: 7452/1: delay: allow timer-based delay implementation to be
  selected

  This patch allows a timer-based delay implementation to be selected by
  switching the delay routines over to use get_cycles, which is
  implemented in terms of read_current_timer. This further allows us to
  skip the loop calibration and have a consistent delay function in the
  face of core frequency scaling.

  To avoid the pain of dealing with memory-mapped counters, this
  implementation uses the co-processor interface to the architected timers
  when they are available. The previous loop-based implementation is
  kept around for CPUs without the architected timers and we retain both
  the maximum delay (2ms) and the corresponding conversion factors for
  determining the number of loops required for a given interval. Since the
  indirection of the timer routines will only work when called from C,
  the sa1100 sleep routines are modified to branch to the loop-based delay
  functions directly.

  Tested-by: Shinya Kuribayashi <shinya.kuribayashi.px@renesas.com>
  Reviewed-by: Stephen Boyd <sboyd@codeaurora.org>
  Signed-off-by: Will Deacon <will.deacon@arm.com>
  Signed-off-by: Russell King <rmk+kernel@arm.linux.org.uk>

  ARM: delay: set loops_per_jiffy when moving to timer-based loop

  The delay functions may be called by some platforms between switching to
  the timer-based delay loop but before calibration. In this case, the
  initial loops_per_jiffy may not be suitable for the timer (although a
  compromise may be achievable) and delay times may be considered too
  inaccurate.

  This patch updates loops_per_jiffy when switching to the timer-based
  delay loop so that delays are consistent prior to calibration.

  Signed-off-by: Will Deacon <will.deacon@arm.com>

  ARM: delay: add registration mechanism for delay timer sources

  The current timer-based delay loop relies on the architected timer to
  initiate the switch away from the polling-based implementation. This is
  unfortunate for platforms without the architected timers but with a
  suitable delay source (that is, constant frequency, always powered-up
  and ticking as long as the CPUs are online).

  This patch introduces a registration mechanism for the delay timer
  (which provides an unconditional read_current_timer implementation) and
  updates the architected timer code to use the new interface.

  Signed-off-by: Jonathan Austin <jonathan.austin@arm.com>
  Signed-off-by: Will Deacon <will.deacon@arm.com>

  ARM: export default read_current_timer

  read_current_timer is used by get_cycles since "ARM: 7538/1: delay:
  add registration mechanism for delay timer sources", and get_cycles
  can be used by device drivers in loadable modules, so it has to
  be exported.

  Without this patch, building imote2_defconfig fails with

  ERROR: "read_current_timer" [crypto/tcrypt.ko] undefined!

  Signed-off-by: Arnd Bergmann <arnd@arndb.de>
  Cc: Stephen Boyd <sboyd@codeaurora.org>
  Cc: Jonathan Austin <jonathan.austin@arm.com>
  Cc: Will Deacon <will.deacon@arm.com>
  Cc: Russell King <rmk+kernel@arm.linux.org.uk>

Change-Id: If1ad095d6852f5966ea995856103e06de6ab2f59
Signed-off-by: Stephen Boyd <sboyd@codeaurora.org>
(cherry picked from commit 2e7486da162e8535f02ffdcaa2943353b738087f)
(cherry picked from commit d9d369383f30506ee7105abc1374fc03028678c1)

---
## [threader/hwp6s-kernel](https://github.com/threader/hwp6s-kernel)@[c74ed8a7b6...](https://github.com/threader/hwp6s-kernel/commit/c74ed8a7b66ac9bfc1f1fe4b7a60808494f5ddb6)
#### Tuesday 2022-12-27 07:48:48 by Stephen Boyd

arm: Implement a timer based __delay() loop

udelay() can be incorrect on SMP machines that scale their CPU
frequencies independently of one another (as pointed out here
http://article.gmane.org/gmane.linux.kernel/977567). The delay
loop can either be too fast or too slow depending on which CPU the
loops_per_jiffy counter is calibrated on and which CPU the delay
loop is running on. udelay() can also be incorrect if the
CPU frequency switches during the __delay() loop, causing the loop
to either terminate too early, or too late.

We'd rather not fix udelay() by forcing it to run on one CPU or
take the penalty of a rather large loops_per_jiffy being used in
udelay() when the CPU is actually running slower. Instead we
solve the problem by making __delay() into a timer based loop
which should be unaffected by CPU frequency scaling. Therefore,
implement a timer based __delay() loop which can be used in place
of the current register based __delay() if a machine so chooses.

The kernel is already prepared for a timer based approach
(evident by the read_current_timer() function). If an arch
implements read_current_timer(), calibrate_delay() will use a
timer based function, calibrate_delay_direct(), to calculate
loops_per_jiffy (in which case loops_per_jiffy should really be
renamed to timer_ticks_per_jiffy). Since the loops_per_jiffy will
be based on timer ticks, __delay() should be implemented as a
loop around read_current_timer().

Doing this makes the expensive loops_per_jiffy calculation go
away (saving ~150ms on boot time on my machine) and fixes
udelay() by making it safe in the face of independently scaling
CPUs. The only prerequisite is that read_current_timer() is
monotonically increasing across calls (and doesn't overflow
within ~2000us).

There is a downside to this approach though. BogoMIPS is no
longer "accurate" in that it reflects the BogoMIPS of the timer
and not the CPU. On most SoC's the timer isn't running anywhere
near as fast as the CPU so BogoMIPS will be ridiculously low (my
timer runs at 4.8 MHz and thus my BogoMIPS is 9.6 compared to my
CPU's 800). This shouldn't be too much of a concern though since
BogoMIPS are bogus anyway (hence the name).

This loop is pretty much a copy of AVR's version made more generic.

Change-Id: I1a80718d93a4821ea55bde99ff0f9cd1c19990ae
Signed-off-by: Stephen Boyd <sboyd@codeaurora.org>
Reviewed-by: Saravana Kannan <skannan@codeaurora.org>
(cherry picked from commit 976eafa8b18252876e15f861944acf693b07ce7e)
(cherry picked from commit 00c3464f49f8ab0f50558cc9b82f70d6822601b8)
(cherry picked from commit ab766f4d27707ea561c4e1e9070613b73aaa9294)

---
## [Erol509/Skyrat-tg](https://github.com/Erol509/Skyrat-tg)@[1c76ea5334...](https://github.com/Erol509/Skyrat-tg/commit/1c76ea533439dcd7fca15a2dd500a44dc6158883)
#### Tuesday 2022-12-27 07:54:23 by SkyratBot

[MIRROR] Changes our map_format to SIDE_MAP [MDB IGNORE] (#18070)

* Changes our map_format to SIDE_MAP (#70162)

## About The Pull Request

This does nothing currently, but will allow me to test for layering
issues on LIVE, rather then in just wallening.
Oh also I'm packaging in a fix to one of my macros that I wrote wrong,
as a joke

[removes SEE_BLACKNESS usage, because we actually cannot use it
effectively](https://github.com/tgstation/tgstation/pull/70162/commits/c9a19dd7cce95038340ebd5c1a6e4cb27ee7c9ee)

[c9a19dd](https://github.com/tgstation/tgstation/pull/70162/commits/c9a19dd7cce95038340ebd5c1a6e4cb27ee7c9ee)

Sidemap removes the ability to control it on a plane, so it basically
just means there's an uncontrollable black slate even if you have other
toggles set.

This just like, removes that, since it's silly

[fixes weird layering on solars and ai portraits. Pixel y was casuing
things to render below who
shouldn't](https://github.com/tgstation/tgstation/pull/70162/commits/3885b9d9ed634cdc4c8041b19df5b5ea9a1a37ae)

[3885b9d](https://github.com/tgstation/tgstation/pull/70162/commits/3885b9d9ed634cdc4c8041b19df5b5ea9a1a37ae)

[Fixes flicker
issues](https://github.com/tgstation/tgstation/pull/70162/commits/2defc0ad20a0ee7d12e0b071f6d31b6127b8765d)

[2defc0a](https://github.com/tgstation/tgstation/pull/70162/commits/2defc0ad20a0ee7d12e0b071f6d31b6127b8765d)

Offsetting the vis_contents'd objects down physically, and then up
visually resolves the confliciting that was going on between the text
and its display.

This resolves the existing reported flickering issues

[fixes plated food not appearing in
world](https://github.com/tgstation/tgstation/pull/70162/commits/28a34c64f830660d7fb1cc669b9fc3ed9f5c7d61)

[28a34c6](https://github.com/tgstation/tgstation/pull/70162/commits/28a34c64f830660d7fb1cc669b9fc3ed9f5c7d61)

pixel_y'd vis_contents strikes again. It's a tad hacky but we'll just
use pixel_z for this

[Adds wall and upper wall plane
masters](https://github.com/tgstation/tgstation/pull/70162/commits/89fe2b4eb40edc36879e4e1954dee8616be94522)

[89fe2b4](https://github.com/tgstation/tgstation/pull/70162/commits/89fe2b4eb40edc36879e4e1954dee8616be94522)

We use these + the floor and space planes to build a mask of all the
visible turfs.
Then we take that, stick it in a plane master, and mask the emissive
plane with it.

This solves the lighting fulldark screen object getting cut by emissives
Shifts some planes around to match this new layering. Also ensures we
only shift fullscreen objects if they don't object to it.

[compresses plane master
controllers](https://github.com/tgstation/tgstation/pull/70162/commits/bd64cc196a4265d42809eebbd1afa46fa33a576d)

[bd64cc1](https://github.com/tgstation/tgstation/pull/70162/commits/bd64cc196a4265d42809eebbd1afa46fa33a576d)

we don't use them for much rn, but we might in future so I'm keeping it
as a convienince thing

:cl:
refactor: The logic of how we well, render things has changed. Make an
issue report if anything looks funky, particularly layers. PLEASE USE
YOUR EYES
/:cl:

Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>

* Changes our map_format to SIDE_MAP

* Modular!

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>
Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>
Co-authored-by: Funce <funce.973@gmail.com>

---
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[0c2b070039...](https://github.com/cmss13-devs/cmss13/commit/0c2b070039afaa0d18a8bbdeb9c28e8333e16470)
#### Tuesday 2022-12-27 08:19:32 by Stan_Albatross

Acid vest TGUI (#2050)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

converts the acid vest config to TGUI

this took a long time to do because the way it's set up was somewhat
annoying

# Explain why it's good for the game

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->

fuck  nanoui


![image](https://user-images.githubusercontent.com/66756236/208936729-7814c386-320d-4ae3-85b5-d7da44e9cedf.png)

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
ui: converted the A.C.I.D. harness to use TGUI
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

Co-authored-by: Stan_Albatross <swt91a@gmail.com>

---
## [yngrdyn/kibana](https://github.com/yngrdyn/kibana)@[afb09ccf8a...](https://github.com/yngrdyn/kibana/commit/afb09ccf8a61d610e8e3d8beb2c80f413f1b33c5)
#### Tuesday 2022-12-27 08:33:36 by Spencer

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
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[639765b0c6...](https://github.com/cmss13-devs/cmss13/commit/639765b0c69faddeec405080ab4fde79503fcf5d)
#### Tuesday 2022-12-27 08:46:02 by Skegal

Loadout - Sniper facepaint (#2015)

# About the pull request

This PR is here to add the sniper facepaint into the loadout for 4
points like the skull facepaint.
 
 I tested it and it worked well as expected.
 
I saw a lot of marines asking the sniper for their bodypaint recently,
and i thought, that since it doesnt change anything game-wise we could
give it on the loadout, as the sniper isnt always here and sometime even
throw it to the trash...also people wont annoy the sniper for his paint
too.

((sorry for the webedit i ran into some problem doing the PR with visual
code studio))

# Explain why it's good for the game

I think its good because it add more customisation to characters with
one more good looking facepaint and like i said earlier, i saw some
marines asking the sniper for it (talked about it on discord and people
seemed to be ok with it)


# Testing Photographs and Procedure

<details>
<summary>Screenshots & Videos</summary>

i posted the pic here
https://discord.com/channels/150315577943130112/1054515157923020842 (if
in the pic you see the facepaint above the other paint its normal, i
tested it with the code above the other but it should appear under the
skull paint in the pr)

</details>


# Changelog

:cl: Skegal
add: Added Full Body Paint to Loadout
/:cl:

---
## [BeagleGaming1/cmss13](https://github.com/BeagleGaming1/cmss13)@[70bcd3b6fb...](https://github.com/BeagleGaming1/cmss13/commit/70bcd3b6fbcf17b4c26640321f23c83da0ab80a3)
#### Tuesday 2022-12-27 09:29:50 by carlarctg

Queen eye shuffles weed sprites when passing over them. (#1901)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

Queen eye shuffles weed sprites when passing over them.

Fixed some single letter vars so the mantainer agenda can't delay this
PR from merging.



<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game


> Queen eye shuffles weed sprites when passing over them.

It's a way for marines to know there's an entire queen eye looking over
them. Basically means an MD isn't 100% necessary to know the queen will
broadcast the location of your flank to the entire hive.

https://streamable.com/kmnd72

It's more subtle than i wanted it to be, but WCYD. Also doesn't work on
corner sprites.

Also, it looks fucking creepy as hell! It's awesome.

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
add: Queen eye shuffles weed sprites when passing over them.
fix: Fixed some single letter vars so the mantainer agenda can't delay
this PR from merging.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[471a228147...](https://github.com/mrakgr/The-Spiral-Language/commit/471a22814793f18fa4f24f70042b272e78e0b607)
#### Tuesday 2022-12-27 09:53:57 by Marko Grdinić

"https://youtu.be/p_sLhKeo6ys?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy&t=86
> 8Gb+ 128 DPUs.

8/128=0.0625

So 64mb then. Exactly how I calculated it based off memory. Fuck. I really am unhinged.

I seem to be interveawing intense brilliance with equaly intense idiocy. Let me close that issue that I opened.

https://github.com/upmem/dpu_demo/issues/

Closed issue 14 here. Let me check the email. No reply from support, not that it matters at this point.

Anyway, going back to that program from yesterday it started giving trouble once I moved above 64mb. Indeed, it is exactly what it said. It can't allocate more that 64mb, and I was trying to allocate 128. It makes sense now, but it didn't make sense to me because I was expecting to be able to allocate 8gb.

9:40am. Ok, now that I am back to sanity, it seems I will be able to write a regular article about UPMEM in the end. And I'll be able to create a useful backend for the device without slinging caustic acid at the company in it.

9:45am. The fact that I burned the bridge with the lead dev does not matter in the least. UPMEM is at the bottom of my list, and if I could control these kinds of emotions, I wouldn't have been having the trouble that I had. They just have to run their course. In my case, poor sleep has been getting old. I'd have been a laughing stock had I continued on my previous course and published the article I intended on HN.

9:50am. Right...

Today I am too out of it to bother doing anything.

During the night, I have been thinking about doing the Graphcore backend. Usually, I wouldn't but since it available on Paperspace, if I really wanted to program, why not give it a try? I've improved the language significantly since last time so it might not be bad to do that during the next programming binge. Right now, I am only missing how to get the MRAM_HEAP_POINTER on the Python side, and then I'll be able to complete the backend.

I should be able to figure out how to get that thing once I fire up VS Code in WSL and take a look at the Python library. It will not be a problem. I've also figured out how to move results back and forth. And now I am over my perplexity.

Since points do not need to be 64-bit I'll scrap my plan for a kernel that uses statically allocated arrays. Though I will show an example that just pushes the offsets directly into the kernel.

10:05am. In order to transfer the results, I am going to make another op so I can turn int tag literals into symbols. I'll have to use records to keep track of vars coming in and out, and I'll need that to create the keys for them. The `VarTag` op will be the first step in that.

10:10am. I'd falled into a trap. Searching my memories, I do not think it said anywhere that a single DPU is 64mb. Or maybe it did, and I ignored it. Remember that slide which showed WRAM to be 64kb and IRAM to be 24kb? I think that one should have had the MRAM at 64Mb. But I probably skipped that mentally. Let me try tracking it down.

https://youtu.be/p_sLhKeo6ys?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy&t=782

What does 40 ranks mean here? Nevermind that for now.

https://youtu.be/p_sLhKeo6ys?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy&t=822

In this older system it seems that DPUs at 128mb. Still, what the hell are these ranks?

https://sdk.upmem.com/2021.4.0/02_HelloWorld.html?highlight=rank

```
dpu_alloc allocates a set of UPMEM DPU ranks. One set contains several DPU ranks and each rank contains several DPUs, the number depending on the target:
* with the simulator, the rank contains 1 DPU.
* with other targets it can vary, even between 2 ranks of the same target.
```

Ok, even if I understand that now, does the rank transfer interface make sense?

10:15am. https://sdk.upmem.com/2021.4.0/032_DPURuntimeService_HostCommunication.html

```
When the DPU set contains multiple DPUs:
* dpu_broadcast_to will copy the same buffer to all DPUs in the set
* dpu_copy_from will return DPU_ERR_INVALID_DPU_SET
* dpu_push_xfer: see Section Rank Transfer Interface
```

https://sdk.upmem.com/2021.4.0/032_DPURuntimeService_HostCommunication.html#rank-transfer-interface

This is confusing after all. I can't see a way to transfer to a specific DPU at all.

///

https://sdk.upmem.com/2021.4.0/032_DPURuntimeService_HostCommunication.html#rank-transfer-interface

If every DPU is 64mb, just how is memory transferred to the individual DPUs? The rank transfer interface groups them together

///

Wait, before I fire that email, just how many DPUs can there be in a single ranks. Probably not enough to go over 4gb.

https://youtu.be/p_sLhKeo6ys?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy&t=782

Going back to this slide, a single chip would have 2 ranks.

16 DPUs spread across 2 ranks is 8 DPUs. The total memory of 8 DPUs in this case would be 512mb.

That seems to low. 20 DIMMs * 16 chips = 320 DPUs. Not right.

Since the total system is 2560 that means that each chip has 8 DPUs. 20 DIMMs * 16 chips * 8 DPUs = 2560 DPUs.

That would put a single chip at 512mb of memory. 8 chips would then have exactly 4gb. Exactly to fit a single rank.

So I can assume that a single rank is 4gb exactly.

Still that is not completely right.

https://sdk.upmem.com/2021.4.0/080_AboutDPULLDB.html?highlight=address%20space#memory-mapping

```
All the memories of the DPU are mapped in a single address space for dpu-lldb:

* WRAM: 0x00000000 - 0x00010000
* MRAM: 0x08000000 - 0x0c000000
* IRAM: 0x80000000 - 0x80008000
```

I saw this yesterday and MRAM doesn't take even half the available 32-bit address space here. Ah, wait, it says DPU. So that is only for a single DPU. Yes this would be enough in that case. Also it is not half the adress space. 0x0c000000 - 0x08000000 = 2 ** 26 = 1024 * 1024 * 64 = 64mb.

Damn it, I got tricked the hell out of me!

10:40am. I wasted so much time on this! Had I been in the course, the instructor would have explained it to me right way. Or that shitfaced dev should have 10 days ago. I missed all the clues. Whoever is playing me must have rolled a few nat 1s in a row.

10:45am. Let me chill. I'll commit here. Let me see if any of my follows are out. Actually, let me publish a new Spiral version now.

PS C:\Users\Marko\Source\Repos\The Spiral Language\VS Code Plugin> vsce publish minor
v2.4.0
npm WARN config global `--global`, `--local` are deprecated. Use `--location=global` instead.

Damn it, I aborted this, but I should have picked patch instead.

10:55am. Pushed v2.3.1 out. Good.

Now let me chill."

---
## [FernandoJ8/tgstation](https://github.com/FernandoJ8/tgstation)@[a811adac74...](https://github.com/FernandoJ8/tgstation/commit/a811adac74513494a620fae631da95d2626b1be7)
#### Tuesday 2022-12-27 09:58:43 by Epic

Changes Admin Prison to be Anti-Telekinesis: Walls off equipment rooms, replaces computers, and makes the tables tidy (#71433)

First PR, may require some changes or something because I don't know how
to do anything bleh
## About The Pull Request

We already had issues with crewmembers with telekinesis making changes
to the security records (purging them and what not). And, nothing has
been done about it, not yet, anyway. Not only record computers are a
problem as well.


![image](https://user-images.githubusercontent.com/106710384/203241399-8314bcba-d2d0-44af-9360-30ff58dbc39e.png)
Previously, prisoners can access the sec vendor with telepathy, and,
since the vendor is free, spam the vendor and be an annoyance. Sure, I
believe that it is not as big of a problem as purging the security
records, but I feel like it's against what the prison is supposed to
stand for; It's supposed to stop them and get them to listen to ahelps
thrown at them.

I've decided to make a bit of changes to the prison to make it so that
people with telekinesis won't fuck up things as much. This replaces real
computers with nonfunctional ones, adding walls to equipment areas to
make sure prisoners don't spam the vendor, and deletes guns/weapons from
the tables so they won't grab them.

## Why It's Good For The Game


![image](https://user-images.githubusercontent.com/106710384/203241465-833f79da-58a3-4feb-87b0-091fbb846e93.png)
This PR is more tailored to admins dealing with no-good-doers, and goes
for the vibe of "HEY, SOMEONE IS PMING YOU, REPLY TO THEM INSTEAD!" Of
course, this leads to prisoners not interacting with the current round,
and, less chance of them going insane and breaking all the windows with
a telekinesis auto-rifle.

Plus, this can always be reverted in-case someone comes up with coding
stuff in instead. I'm all through with that and willing to work with
whoever to solve the issue.

Also, of course, Closes #60967

## Changelog

:cl:
admin: Nanotrashen made some top-of-the-line changes to their
top-of-the-line prison by walling off their equipment area and removing
some spare guns they somehow left on the tables. We also stole the
security computers, so people with telekinesis can't access them.
/:cl:

---
## [FernandoJ8/tgstation](https://github.com/FernandoJ8/tgstation)@[c185dffda0...](https://github.com/FernandoJ8/tgstation/commit/c185dffda0cc30d8187fa1ba37e5784b8d630ba4)
#### Tuesday 2022-12-27 09:58:43 by Jacquerel

Basic Mob Carp Bonus Part: Wall smashing (#71524)

## About The Pull Request

Atomisation of #71421 
This moves the attack function of "environment smash" flags which allow
simple mobs to attack walls into an element, so that we can put it on
other things later.
For some reason while working on carp I convinced myself that they had
"environment_smash" flags, which they do not, so this actually is not
relevant to carp in any way.

While implementing this I learned that the way wall smashing works is
stupid, because walls don't have health and so resultingly if a mob can
attack walls it deletes them in a single click. If we ever decide to
change this then it should be easier in an element than in three
different `attack_animal` reactions.
This is especially silly with the "wumborian fugu" item which allows any
mob it is used on to instantly delete reinforced walls, and also to
destroy tables if they click them like seven or eight times (because it
does not increase their object damage in any way).

## Why It's Good For The Game

Eventually someone will port a basic mob which does use this behaviour
(most of the mining ones for instance) and then this will be useful.
If we ever rebalance wall smashing to not instantly delete walls then
this will also be useful.
Admins can apply this to a mob to allow it to delete walls if they
wanted to do that for some reason, they probably shouldn't to be honest
at least until after we've done point two unless they trust the player
not to just use it to deconstruct the space station.

## Changelog
:cl:
refactor: Moves wall smashing out of simple mob code and into an element
we can reuse for basic mobs later
/:cl:

---
## [FernandoJ8/fulpstation](https://github.com/FernandoJ8/fulpstation)@[ca0fedc60f...](https://github.com/FernandoJ8/fulpstation/commit/ca0fedc60f17f19520b8fa064c396129ad68b633)
#### Tuesday 2022-12-27 09:58:50 by John Willard

Sol is now a Subsystem, Coffins lock themselves, Bloodsuckers don't constantly die, probably (#862)

* Turns Sol into a Subsystem & Many more

Turns Sol into a subsystem and hooks Bloodsuckers onto it via signals instead of doing a ton of for() loops anywhere. This made Sol incredibly fucking fast, so I halved the speed so it only ticks every 2 seconds.

I also improved the sunlight hud to update with regular bloodsucker updates to avoid some useless proc overhead and fixed Coffins not locking by themselves.

* Torpor now ends, moves exiting torpor to its proper place

* round it

* fix comment

* fix CI

---
## [lvefjord/ck3-old-valyria-mod](https://github.com/lvefjord/ck3-old-valyria-mod)@[ea0f5891be...](https://github.com/lvefjord/ck3-old-valyria-mod/commit/ea0f5891becc45764b0391830046bf55b48d9296)
#### Tuesday 2022-12-27 10:31:44 by lvefjord

[list]
[*]Lotta fixing mistakes here and there, e.g. "northmen" into "northman" and had to add riverlander because I had just been using crownlander for it and cheated in the loc.
[*]Fixed Orys' DNA. Black of hair, the seed is strong.
[*]Figured out how to give the iron throne title equal primogeniture at 867.
[*]Made Dragonstone de jure part of iron throne.
[*]Added nickname "the King who Knelt" for Torrhen once you conquer the North.
[*]Nerfed some of the on game start effects, like some provinces getting decked out in buildings.
Tried to nerf a bunch of stuff and even more tries to buff the old kings.
It's way too easy to conquer the kingdoms, but I'm going in the right direction making it more balanced.
[*]You marry Orys to the Storm Kings daughter if she's still alive when you finish the war, as it was told in the holy scriptures.
[*]Significantly reduced the effects of failing the bloodmagic decision, it no longer bricks your character. It's pretty much lunatic or possessed.
[*]Made some new characters, most importantly 2 more generations of Gardener/Lannisters. I was trying to figure out how to make a strong alliance between them and needed the marriage, for lore reasons and to maybe slow down the conquest and balance it a bit.
[/list]
Think that's about it.

---
## [VDP-noclip/noclip](https://github.com/VDP-noclip/noclip)@[93d80795ec...](https://github.com/VDP-noclip/noclip/commit/93d80795ecaeeeb73a1a8358ac98558a389bb847)
#### Tuesday 2022-12-27 10:56:16 by bottolo

Loading screen implementation (#209)

### Welcome, Narrative Section
I know what you're thinking: this is a PR made for loading screens. 
You couldn't be more *wrong*. 

This is actually a fake loading screen. We made the timer go along with
a pre-determined time to give the illusion of a loading screen, where it
actually serves as a narration sequence.

### Recap
- Added loading screen.
- Added loading animation.
- Whenever loading is finished, you can press any button to continue.
- Added a scriptable object to better control which text to be shown in
a given level.

### What's left
- Dialogue: we'll have to consult with @AleDeNic in order to finalize
this aspect.
- Clunky fade-in: we'll have to investigate further ways to fade text.
- Typewriter effect. A subtle effect will have to be added to better
reflect tutorial prompts.

Co-authored-by: stefanofossati <10569836@mail.polimi.it>

---
## [harryob/cmss13](https://github.com/harryob/cmss13)@[a742c64df9...](https://github.com/harryob/cmss13/commit/a742c64df98ec4f23eaa64162a2518a91c642ead)
#### Tuesday 2022-12-27 11:55:38 by carlarctg

Fix entering a ghosted xeno not removing ghostize sleep. (#2076)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

Fix entering a ghosted xeno not removing ghostize sleep.

# Explain why it's good for the game

This sucks ass! Let me wake up!!!!! can KILL you if you enter a xeno in
a difficult situation!!!!!!

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
fix: Fix entering a ghosted xeno not removing ghostize sleep.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [tsvdh/InfoVis](https://github.com/tsvdh/InfoVis)@[885d875e25...](https://github.com/tsvdh/InfoVis/commit/885d875e25ed57da1d388c07a56f64f088db3788)
#### Tuesday 2022-12-27 11:56:04 by William Narchi

Fuck sensibility (see description)

So I want to use WSL for this because fuck Visual Studio. However, the file picker that is used by default is not usable on WSL without some major modifications because the mechanism it uses to detect the default file explorer doesn't work on WSL because of the lack of a proper desktop portal, so fuck you I made my own file picker with drop-downs and confirmation buttons

---
## [boiscljo/BedWars](https://github.com/boiscljo/BedWars)@[3b4a762202...](https://github.com/boiscljo/BedWars/commit/3b4a762202942db6d6c736f0007b51c4de7e1fed)
#### Tuesday 2022-12-27 12:24:28 by Misat11

some fixes and changes to 1.8.8 bossbars (see description)

There are 2 configurable backend entities for bossbars (invalid value fallbacks to wither)
- `wither` (default)
  - Everything works great except that fucking fog (it's ok for games in the evening or in night)
- `ender_dragon` (other possible values are `dragon` and `ender`)
  - Normal sky however it's randomly flickering even if not moving and the dragon does not want to be invisible, so it can be seen in void worlds.

---
## [chmcax/android_kernel_samsung_gta4xl](https://github.com/chmcax/android_kernel_samsung_gta4xl)@[7112098b69...](https://github.com/chmcax/android_kernel_samsung_gta4xl/commit/7112098b69d5922b7d34c1f6088dad4b0507214e)
#### Tuesday 2022-12-27 12:26:45 by Jason A. Donenfeld

random: credit cpu and bootloader seeds by default

[ Upstream commit 846bb97e131d7938847963cca00657c995b1fce1 ]

This commit changes the default Kconfig values of RANDOM_TRUST_CPU and
RANDOM_TRUST_BOOTLOADER to be Y by default. It does not change any
existing configs or change any kernel behavior. The reason for this is
several fold.

As background, I recently had an email thread with the kernel
maintainers of Fedora/RHEL, Debian, Ubuntu, Gentoo, Arch, NixOS, Alpine,
SUSE, and Void as recipients. I noted that some distros trust RDRAND,
some trust EFI, and some trust both, and I asked why or why not. There
wasn't really much of a "debate" but rather an interesting discussion of
what the historical reasons have been for this, and it came up that some
distros just missed the introduction of the bootloader Kconfig knob,
while another didn't want to enable it until there was a boot time
switch to turn it off for more concerned users (which has since been
added). The result of the rather uneventful discussion is that every
major Linux distro enables these two options by default.

While I didn't have really too strong of an opinion going into this
thread -- and I mostly wanted to learn what the distros' thinking was
one way or another -- ultimately I think their choice was a decent
enough one for a default option (which can be disabled at boot time).
I'll try to summarize the pros and cons:

Pros:

- The RNG machinery gets initialized super quickly, and there's no
  messing around with subsequent blocking behavior.

- The bootloader mechanism is used by kexec in order for the prior
  kernel to initialize the RNG of the next kernel, which increases
  the entropy available to early boot daemons of the next kernel.

- Previous objections related to backdoors centered around
  Dual_EC_DRBG-like kleptographic systems, in which observing some
  amount of the output stream enables an adversary holding the right key
  to determine the entire output stream.

  This used to be a partially justified concern, because RDRAND output
  was mixed into the output stream in varying ways, some of which may
  have lacked pre-image resistance (e.g. XOR or an LFSR).

  But this is no longer the case. Now, all usage of RDRAND and
  bootloader seeds go through a cryptographic hash function. This means
  that the CPU would have to compute a hash pre-image, which is not
  considered to be feasible (otherwise the hash function would be
  terribly broken).

- More generally, if the CPU is backdoored, the RNG is probably not the
  realistic vector of choice for an attacker.

- These CPU or bootloader seeds are far from being the only source of
  entropy. Rather, there is generally a pretty huge amount of entropy,
  not all of which is credited, especially on CPUs that support
  instructions like RDRAND. In other words, assuming RDRAND outputs all
  zeros, an attacker would *still* have to accurately model every single
  other entropy source also in use.

- The RNG now reseeds itself quite rapidly during boot, starting at 2
  seconds, then 4, then 8, then 16, and so forth, so that other sources
  of entropy get used without much delay.

- Paranoid users can set random.trust_{cpu,bootloader}=no in the kernel
  command line, and paranoid system builders can set the Kconfig options
  to N, so there's no reduction or restriction of optionality.

- It's a practical default.

- All the distros have it set this way. Microsoft and Apple trust it
  too. Bandwagon.

Cons:

- RDRAND *could* still be backdoored with something like a fixed key or
  limited space serial number seed or another indexable scheme like
  that. (However, it's hard to imagine threat models where the CPU is
  backdoored like this, yet people are still okay making *any*
  computations with it or connecting it to networks, etc.)

- RDRAND *could* be defective, rather than backdoored, and produce
  garbage that is in one way or another insufficient for crypto.

- Suggesting a *reduction* in paranoia, as this commit effectively does,
  may cause some to question my personal integrity as a "security
  person".

- Bootloader seeds and RDRAND are generally very difficult if not all
  together impossible to audit.

Keep in mind that this doesn't actually change any behavior. This
is just a change in the default Kconfig value. The distros already are
shipping kernels that set things this way.

Ard made an additional argument in [1]:

    We're at the mercy of firmware and micro-architecture anyway, given
    that we are also relying on it to ensure that every instruction in
    the kernel's executable image has been faithfully copied to memory,
    and that the CPU implements those instructions as documented. So I
    don't think firmware or ISA bugs related to RNGs deserve special
    treatment - if they are broken, we should quirk around them like we
    usually do. So enabling these by default is a step in the right
    direction IMHO.

In [2], Phil pointed out that having this disabled masked a bug that CI
otherwise would have caught:

    A clean 5.15.45 boots cleanly, whereas a downstream kernel shows the
    static key warning (but it does go on to boot). The significant
    difference is that our defconfigs set CONFIG_RANDOM_TRUST_BOOTLOADER=y
    defining that on top of multi_v7_defconfig demonstrates the issue on
    a clean 5.15.45. Conversely, not setting that option in a
    downstream kernel build avoids the warning

[1] https://lore.kernel.org/lkml/CAMj1kXGi+ieviFjXv9zQBSaGyyzeGW_VpMpTLJK8PJb2QHEQ-w@mail.gmail.com/
[2] https://lore.kernel.org/lkml/c47c42e3-1d56-5859-a6ad-976a1a3381c6@raspberrypi.com/

Cc: Theodore Ts'o <tytso@mit.edu>
Reviewed-by: Ard Biesheuvel <ardb@kernel.org>
Signed-off-by: Jason A. Donenfeld <Jason@zx2c4.com>
Signed-off-by: Sasha Levin <sashal@kernel.org>

---
## [Paxilmaniac/Skyrat-tg](https://github.com/Paxilmaniac/Skyrat-tg)@[67ca6389d0...](https://github.com/Paxilmaniac/Skyrat-tg/commit/67ca6389d031e7b12813af27fe89ced9ce633a3c)
#### Tuesday 2022-12-27 12:44:55 by SkyratBot

[MIRROR] Adds the Sandstorm random event, directional meteor functionality, space sand. [MDB IGNORE] (#18338)

* Adds the Sandstorm random event, directional meteor functionality, space sand. (#71802)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

![sandstorm](https://user-images.githubusercontent.com/28870487/206070641-80d37afc-a365-4f5e-ad48-e8cdf0153ac9.png)

Hey guys, it's your boy. Back at it again with another meteor-adjacent
event PR.

Adds the Sandstorm random event, inspired by the long-unused admin only
one. It picks a direction to approach from, alerts the crew of its
imminent arrival, and after a little over a minute of preparatory time,
sends waves of sand and dust to grind down everything in that direction.

To accomplish this, some minor adjustments had to be made to meteor
generation code. They can now be passed an optional arg for a direction
to be thrown from, and will pick a random one if no direction is given.

Also introduces the newest addition to our cast of meteors -- space
sand! It's even weaker than space dust, and shows up exclusively in this
event. Space sand is **ineffective against rwalls**, and will not damage
the arrivals area's high-tech sand-resistant glass. This is to prevent
this event from venting one of the most dust-vulnerable areas on the
station, and to make sure new players aren't shafted into firelock hell
when the right angle is picked.

I did a lot of testing and tweaking of numbers to get the damage to
average at about the level I'm comfortable with. This is meant to be a
high-impact event that isn't as destructive (or unavoidable) as a meteor
wave. Speaking of avoidance, let's talk about mitigation:

You get an early warning and a direction the sand will come from. You
have time to grab repair supplies, move to safety, get a MODsuit. You
can make worthwhile repairs as the sand comes in from inside (or
outside, if you're brave enough) with nothing more than a welder and
iron sheets. If you're feeling particularly spicy, you can leverage your
prep time setting up shield generators, which spawn in engineering and
have been added to the maintenance machines loot pool. Anyone can
contribute, so do your part as a good crewmate and help out!

All that being said, the event can't be prevented entirely. Shit's going
to get shredded, especially on the outside of the station. Damage will
vary heavily based on the station and direction, ranging from
inconsequential to threatening. It should happen late enough into the
round that, at the bare minimum, the crew shouldn't be caught
unprepared.

For those of you who are worried, the ORIGINAL sandstorm admin event is
still with us too. It's been moved from the space dust file into the
Sandstorm event file. This PR also makes a very minor change to the
naming of the space _dust_ events, for better menuing.

So, to sum it all up: Sand hits grinds down one side of the station, you
get a minute of warning, shield generators now spawn in maintenance. Be
a good crewmate and help where you can.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

More event variety is good, and events that give the players agency on
how bad the impact will be is even better.

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

:cl: Rhials
add: Sandstorm random event! A random side of the station is pummeled by
an onslaught of sand and dust. If you hear that one is approaching, grab
a welder and some iron to help with repairs!
add: Space sand! It's weak and doesn't hurt reinforced walls, but
shouldn't be underestimated in high quantities.
code: You can now pass a start direction to the
spawn_meteors/spawn_meteor global procs.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

* Adds the Sandstorm random event, directional meteor functionality, space sand.

Co-authored-by: Rhials <Datguy33456@gmail.com>

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[cd13fcdf46...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/cd13fcdf467b1a9fe5d8fc5256552b0601284dca)
#### Tuesday 2022-12-27 12:48:11 by Jolly

[MODULAR] contraband.dmi is no longer a hard override on posters (#18106)

* hhngh

* dunks this fucking dmi

* fuck you

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[08291a6dbb...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/08291a6dbb3249d9acbca4f539eb82900d299f26)
#### Tuesday 2022-12-27 12:48:11 by SkyratBot

[MIRROR] Guards against uplink failsafe code being the same as unlock code [MDB IGNORE] (#18275)

* Guards against uplink failsafe code being the same as unlock code (#72113)

## About The Pull Request

There's probably a better way to do this to be honest, but I think it's
silly for both to potentially be the same and this should work alright.
## Why It's Good For The Game

Fixes #71446.

I don't think the Syndicate is that stupid.
## Changelog
:cl:
fix: After a recent mishap with a high-ranking Syndicate operative, the
uplink's unlock code and failsafe code (the one that makes it blow up if
you say it) should never turn out to be the same.
/:cl:

* Guards against uplink failsafe code being the same as unlock code

Co-authored-by: san7890 <the@san7890.com>

---
## [n-ham/n-ham.github.io](https://github.com/n-ham/n-ham.github.io)@[f704520248...](https://github.com/n-ham/n-ham.github.io/commit/f70452024894723fda1631454c9cbbd8261fd59e)
#### Tuesday 2022-12-27 14:27:48 by n-ham

fuck you vile rapists and everyone onside with them

---
## [BramGruneir/cockroach](https://github.com/BramGruneir/cockroach)@[8ae602660d...](https://github.com/BramGruneir/cockroach/commit/8ae602660d16be76331c6705b748eb3ba7799cb0)
#### Tuesday 2022-12-27 15:18:08 by craig[bot]

Merge #89613 #93985 #93989

89613: gossip: remove frequent gossiping of gossip client connections r=irfansharif a=a-robinson

These gossip-clients keys make up two thirds or more of the gossip traffic in various large clusters I've inspected, consuming almost an entire CPU core in the worst case I've seen. They don't provide enough value to justify that sort of ongoing cost, so this commit removes them entirely as well as the periodic logging of the gossip network and the crdb_internal.gossip_network table, both of which relied on them.

These gossip-clients keys make up two thirds or more of the gossip
traffic in various large clusters I've inspected, consuming almost an
entire CPU core in the worst case I've seen. They don't provide enough
value to justify that sort of ongoing cost, so this commit removes them
entirely as well as the periodic logging of the gossip network and the
crdb_internal.gossip_network table, both of which relied on them.

Release note (backward-incompatible change): We've stopped
supporting/populating the crdb_internal.gossip_network table. It was an
internal table with no API guarantees (so perhaps no meriting a release
note?).

Release note (performance improvement): Significantly reduced CPU usage
of the underlying gossip network in large clusters.

---

Informs #51838 (largely fixes it for practical purposes, although there's likely still more that could be done)

This is clearly going to break [the gossip roachtest](https://github.com/cockroachdb/cockroach/blob/master/pkg/cmd/roachtest/tests/gossip.go#L50-L58), but between `@irfansharif` kindly volunteering to fix that up separately and his existing TODO in that file I've left that out of this change.

I don't know if completely removing the gossip_network table is really the best idea or if it should just be left in and only populated with the clients from the local node. For example, when run in a mixed version cluster does `debug zip` run all of its sql commands against the local node or does it run some against remote nodes? If an old node ever tries to query the `gossip_network` table on a different node it could have a bad time.

`@irfansharif` `@kvoli` 

93985: ui: degrade gracefully when regions aren't known r=matthewtodd a=matthewtodd

Part of #89949

Previously, when a tenant SQL instance had spun down (leaving us no way to remember which region it had been in), the SQL Activity pages would claim that statements and transactions had occurred in an "undefined" region.

This change moves from saying "undefined" to saying nothing at all, a slightly nicer user experience.

This broader problem of losing the region mapping has been described in #93268; we'll begin addressing it shortly.

Release note: None

93989: leaktest: exclude long running logging goroutines r=srosenberg a=nicktrav

The `leaktest` package detects potential goroutine leaks by snapshotting the set of goroutines running when `leaktest.AfterTest(t)` is called, returning a closure, and comparing the set of goroutines when the closure is called (typically `defer`'d).

A race condition was uncovered in #93849 whereby logging-related goroutines that are scheduled by an `init` function in `pkg/util/logging` can sometimes be spawned _after_ the `AfterTest` function is run. When the test completes and the closure is run, the test fails due to a difference in the before / after goroutine snapshots.

This mode of failure is deemed to be a false-positive. The intention of the logging goroutines are that they live for the duration of the process. However, exactly _when_ the goroutines scheduled in the `init` functions actually start run, and hence show up in the goroutine snapshots, is non-deterministic.

Exclude the logging goroutines from the `leaktest` checks to reduce the flakiness of tests.

Closes #93849.

Release note: None.

Epic: CRDB-20293

Co-authored-by: Alex Robinson <arobinson@cloudflare.com>
Co-authored-by: Matthew Todd <todd@cockroachlabs.com>
Co-authored-by: Nick Travers <travers@cockroachlabs.com>

---
## [godmod9/RbxJs2016](https://github.com/godmod9/RbxJs2016)@[d085bb886a...](https://github.com/godmod9/RbxJs2016/commit/d085bb886a05315980dc72444a5d83a11874f5eb)
#### Tuesday 2022-12-27 15:18:16 by godmod9

FUCK YOU NODEGIT!!!!!!!!!!

FUCK YOU NODEGIT!!!!!!!!!!

---
## [avar/git](https://github.com/avar/git)@[f1c903debd...](https://github.com/avar/git/commit/f1c903debdcbf6aaf8fd3abf222fa941b42d5d31)
#### Tuesday 2022-12-27 15:24:55 by Ævar Arnfjörð Bjarmason

cocci: make "coccicheck" rule incremental

Optimize the very slow "coccicheck" target to take advantage of
incremental rebuilding, and fix outstanding dependency problems with
the existing rule.

The rule is now faster both on the initial run as we can make better
use of GNU make's parallelism than the old ad-hoc combination of
make's parallelism combined with $(SPATCH_BATCH_SIZE) and/or the
"--jobs" argument to "spatch(1)".

It also makes us *much* faster when incrementally building, it's now
viable to "make coccicheck" as topic branches are merged down.

The rule didn't use FORCE (or its equivalents) before, so a:

	make coccicheck
	make coccicheck

Would report nothing to do on the second iteration. But all of our
patch output depended on all $(COCCI_SOURCES) files, therefore e.g.:

    make -W grep.c coccicheck

Would do a full re-run, i.e. a a change in a single file would force
us to do a full re-run.

The reason for this (not the initial rationale, but my analysis) is:

* Since we create a single "*.cocci.patch+" we don't know where to
  pick up where we left off, or how to incrementally merge e.g. a
  "grep.c" change with an existing *.cocci.patch.

* We've been carrying forward the dependency on the *.c files since
  63f0a758a06 (add coccicheck make target, 2016-09-15) the rule was
  initially added as a sort of poor man's dependency discovery.

  As we don't include other *.c files depending on other *.c files
  has always been broken, as could be trivially demonstrated
  e.g. with:

       make coccicheck
       make -W strbuf.h coccicheck

  However, depending on the corresponding *.c files has been doing
  something, namely that *if* an API change modified both *.c and *.h
  files we'd catch the change to the *.h we care about via the *.c
  being changed.

  For API changes that happened only via *.h files we'd do the wrong
  thing before this change, but e.g. for function additions (not
  "static inline" ones) catch the *.h change by proxy.

Now we'll instead:

 * Create a <RULE>/<FILE> pair in the .build directory, E.g. for
   swap.cocci and grep.c we'll create
   .build/contrib/coccinelle/swap.cocci.patch/grep.c.

   That file is the diff we'll apply for that <RULE>-<FILE>
   combination, if there's no changes to me made (the common case)
   it'll be an empty file.

 * Our generated *.patch
   file (e.g. contrib/coccinelle/swap.cocci.patch) is now a simple "cat
   $^" of all of all of the <RULE>/<FILE> files for a given <RULE>.

   In the case discussed above of "grep.c" being changed we'll do the
   full "cat" every time, so they resulting *.cocci.patch will always
   be correct and up-to-date, even if it's "incrementally updated".

   See 1cc0425a27c (Makefile: have "make pot" not "reset --hard",
   2022-05-26) for another recent rule that used that technique.

As before we'll:

 * End up generating a contrib/coccinelle/swap.cocci.patch, if we
   "fail" by creating a non-empty patch we'll still exit with a zero
   exit code.

   Arguably we should move to a more Makefile-native way of doing
   this, i.e. fail early, and if we want all of the "failed" changes
   we can use "make -k", but as the current
   "ci/run-static-analysis.sh" expects us to behave this way let's
   keep the existing behavior of exhaustively discovering all cocci
   changes, and only failing if spatch itself errors out.

Further implementation details & notes:

 * Before this change running "make coccicheck" would by default end
   up pegging just one CPU at the very end for a while, usually as
   we'd finish whichever *.cocci rule was the most expensive.

   This could be mitigated by combining "make -jN" with
   SPATCH_BATCH_SIZE, see 960154b9c17 (coccicheck: optionally batch
   spatch invocations, 2019-05-06).

   There will be cases where getting rid of "SPATCH_BATCH_SIZE" makes
   things worse, but a from-scratch "make coccicheck" with the default
   of SPATCH_BATCH_SIZE=1 (and tweaking it doesn't make a difference)
   is faster (~3m36s v.s. ~3m56s) with this approach, as we can feed
   the CPU more work in a less staggered way.

 * Getting rid of "SPATCH_BATCH_SIZE" particularly helps in cases
   where the default of 1 yields parallelism under "make coccicheck",
   but then running e.g.:

       make -W contrib/coccinelle/swap.cocci coccicheck

   I.e. before that would use only one CPU core, until the user
   remembered to adjust "SPATCH_BATCH_SIZE" differently than the
   setting that makes sense when doing a non-incremental run of "make
   coccicheck".

 * Before the "make coccicheck" rule would have to clean
   "contrib/coccinelle/*.cocci.patch*", since we'd create "*+" and
   "*.log" files there. Now those are created in
   .build/contrib/coccinelle/, which is covered by the "cocciclean" rule
   already.

Outstanding issues & future work:

 * We could get rid of "--all-includes" in favor of manually
   specifying a list of includes to give to "spatch(1)".

   As noted upthread of [1] a naïve removal of "--all-includes" will
   result in broken *.cocci patches, but if we know the exhaustive
   list of includes via COMPUTE_HEADER_DEPENDENCIES we don't need to
   re-scan for them, we could grab the headers to include from the
   .depend.d/<file>.o.d and supply them with the "--include" option to
   spatch(1).q

1. https://lore.kernel.org/git/87ft18tcog.fsf@evledraar.gmail.com/

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>
Signed-off-by: Taylor Blau <me@ttaylorr.com>

---
## [mullenpaul/cmss13](https://github.com/mullenpaul/cmss13)@[1a226283e5...](https://github.com/mullenpaul/cmss13/commit/1a226283e5c108dffcb74746af5d36ba29d51058)
#### Tuesday 2022-12-27 15:56:01 by Diegoflores31

vamp lurker strain (#955)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

## About The Pull Request

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->
Adds a new strain for lurker (vampire is the name for now but i can be
changed i just lack the creativity) has less health than the average
lurker but its faster and slashes faster but deals less damage .

**### BASE STATS**
health : 390
armor : 20 
slash damage : 35
speed : 0.1 faster than base lurker // for reference cloaked speed is
0.2
slash speed : 2


Vamp lurker cannot cloak but has a larger kit of abilities focused on
dealing damage and healing making it a high risk high reward backliner
with skill based abilities rather than just stun.
### **Abilities :**

**Rush:** 
Shorter version of pounce (4 tiles) instead of stunning it will daze and
slightly screenshake the target .
damage : 30
cooldown : 6 seconds and 3 if you land it.

**Flurry:**
AOE attack that deals damage to the targets in front of you in a 1x3
area . if landed it will heal you by the same amount and apply a small
slow for the user ( very short second slow)
damage: 30
heal : 30
cooldown : 3 seconds if missed 

**Tail Jab:**
Targeted attack will deal a small amount of damage to the target and
knock him away from you . if you use it on a target in critical state it
will execute it healing you a LOT.
damage : 30
Execution damage : 80 with penetration
cooldown : 7 seconds 
heal : 150
critical state : this occurs when the target either paincrits or falls
INCONCIOUS

## Why It's Good For The Game

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->
Lurker lacks strains and i looked up in the Trello that Lurker strain
was required . i tried to follow the indicators but kinda ended up with
something else i guess but i really like how it ended so i am making
this PR to see what you think about it.


## Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->

:cl: diegoflores31
add: Added a new strain for lurker "Vampire".
add: Vampire Lurker exchanges all of your abilities for a fast paced
combat style more focused into dealing damage and
mobility.
add: Active 1 : Rush . Pounces for a maximun of 4 tiles and slashes the
objetive once on impact . applying a screenshake and daze to the target
. Landing this ability reduces the cooldown by half. (cooldown 6
seconds)
add: Active 2 . Flurry : unleashes a 1X3 slash at the targeted direction
that slows your enemies on impact healing you by 30 hp . (cooldown 3
seconds)
add: Active 3 : Tail Jab : Attacks your enemies from a maximun of 2
tiles away while dealing a small amount of damage ( 20) and knocking
them down . if you attack a enemy that is on critical state it will deal
80 damage with penetration and heal you by 150 hp. (cooldown 7 seconds)
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

Co-authored-by: Shad0vvs <rtwdevelopment@gmail.com>
Co-authored-by: harryob <me@harryob.live>

---
## [korbal/portfolio](https://github.com/korbal/portfolio)@[d177d6054d...](https://github.com/korbal/portfolio/commit/d177d6054d7abd8a72c12198f077b1b64c00902a)
#### Tuesday 2022-12-27 16:20:05 by korbal

experience section done. wonky af on mobile because there is a top gap for some fucking reason

---
## [bentusi16/SWLOR_Haks](https://github.com/bentusi16/SWLOR_Haks)@[6ffa92d6cc...](https://github.com/bentusi16/SWLOR_Haks/commit/6ffa92d6cc5883cce0bc077245f3f7d5a9f1a75f)
#### Tuesday 2022-12-27 17:07:53 by Scott Finlay

Patch for Head Pack 4 (#146)

- Re-added overwritten head 54, now as Head 100. Over-wrote ugly old NWN head that nobody used because I didn't want to fuck with IDs

- Adjusted scaling on Male Hum/Mir/Chi/Ech 50 & 51

---
## [uebelack/uebelacker.ch](https://github.com/uebelack/uebelacker.ch)@[8a96993c8d...](https://github.com/uebelack/uebelacker.ch/commit/8a96993c8dc46f3b092fd0103ea1ac7795438842)
#### Tuesday 2022-12-27 17:20:33 by David Uebelacker

:whale: Never tell.  Not if you love your wife ... In fact, if your old lady walks
in on you, deny it.  Yeah.  Just flat out and she'll believe it: "I'm
tellin' ya.  This chick came downstairs with a sign around her neck `Lay
On Top Of Me Or I'll Die'.  I didn't know what I was gonna do..."
		-- Lenny Bruce

---
## [Workbench-Team/space-station-14](https://github.com/Workbench-Team/space-station-14)@[c0a13f6269...](https://github.com/Workbench-Team/space-station-14/commit/c0a13f626980fc61e8664b2a6d2a34ccca24c98d)
#### Tuesday 2022-12-27 17:45:54 by Mr0maks

Голопроекторы почти как на tgstation (#36)

* First work on holo

* End of my pain in ass

* Oh shit im sorry

---
## [Matrix20232023/godel](https://github.com/Matrix20232023/godel)@[c6dc93c126...](https://github.com/Matrix20232023/godel/commit/c6dc93c1263e6cc15279cd69436f4254da34392c)
#### Tuesday 2022-12-27 18:29:06 by Tamer Kılıç

Golden Protocol FAQ

Golden Protocol FAQ
Learn about the Golden Protocol and how you can help build the worlds largest decentralized knowledge graph.
Status and progress
Golden is on a mission to map all human knowledge. 
We  as a  in San Francisco. We  from leading investors ranging from a16z to Balaji to Founders Fund and many others. Since the Fall 2021, we have been ramping up efforts to create a web3 version of Golden to increase the speed that the knowledge graph can be built. 
Golden is building a permissionless, open source  that incentivizes the collection and verification of canonical knowledge, which it will offer to the public for free and charge commercial entities.
User growth: 10’s of thousands of users (growing daily) have connected wallets to Golden and are submitting data into the protocol.
Data collection: users have contributed millions of data triples to Golden so far, and we have started the process of the verification of these triples.
Protocol development: We are developing a protocol, , and APIs for submitting and verifying triples.  is in the process of being optimized for full web3 integration.
Whitepaper: We have written our whitepaper, which is currently in review to be made public soon.
Hiring: We are hiring fast and have . Please apply or share.
I am new here, how can I help?
Start by  and following the guide to 
 ( → connect wallet). If you have already made a Golden.com account, just connect your wallet.
Sign in to the Golden dApp by following: 
.
Help grow the knowledge graph by  to  entity pages. Follow our  to get started.
Submit triples: Users that submit fact triples that go on to be accepted will be eligible for an airdrop when the Golden token is released. Please note, there is no need to paste edits of data triples and citations into Discord, we have a log of your efforts!
Verify triples: Users can become eligible for a future airdrop by verifying triples that get accepted by the protocol on . Please follow our  when verifying.
Are you a builder (developer, data scientist etc.) that can help us? Let us know in Discord by .
Share the project! Tell your friends, developers, or family.  and invite like-minded people to .
What’s the TLDR on how the protocol works?
Tokens for submission and verification: Tokens are earned by submitters and verifiers for loading and verifying true facts (triples) into the knowledge graph. E.g. ‘Apple’ ‘was founded in’ ‘1976’. Verifiers confirm the correctness of the triples by voting. Once the number of votes reaches a statistical threshold, the ‘fact’ is accepted by the knowledge graph and immutably stored. As the knowledge graph grows, the data itself can be used to aid verification. Submitters and verifiers gain a reputation score as triples are accepted.
Data NFTs, fractional ownership, and revenue share incentives: NFTs are used to organize fractional ownership between the creators of the data associated with each unique entity. Various canonical data can be associated with the unique data NFTs including triples, natural language in various translations, canonical images, or otherwise. These NFTs will assist with disambiguation and allow fractionalized ownership for the submitters, verifiers, and the protocol. Revenue shared from commercial data usage can be distributed to the creators of the data and protocol. Copyright law is used to protect intellectual property and afford commercial usage of the data while allowing free usage by the public.
Anti-gaming: A Sybil attack resistance, game-theoretic approach is used to provide asymmetric costs to gaming the protocol. Slashing staked collateral is a mechanic used to prevent submitters and verifiers from incorrectly submitting or voting. Reputation scores are implemented to increase efficiency in staking and slashing. Voting is blind.
V0 system design:
When will a token be released?
There is currently no Golden token and no set date for release. The team will clearly communicate this release well in advance of the launch.
⚠️ Important: We will *never* directly message you about the token sale, so please do not interact with any such messages, as they are spam. When we launch the token, we will do so on multiple marketing channels including core discord announcements channels, Twitter, and our blog.
The team is working aggressively towards a mainnet launch. Currently, we are creating our protocol and  on the testnet. We will announce an estimated launch date as we further build the protocol. We are building Golden in an SEC-compliant manner and are not cutting corners with compliance.
How will airdrops be awarded?
At this time, performing the following tasks will make you eligible for an airdrop:
submitting triples that go on to be accepted
performing correct verification
developing the protocol code
adding a citation to a triple that exists on Golden that doesn’t have a citation already
Up to 1% of the token treasury will be awarded to the community for correct data submission and verification.
How can I perform triple submission tasks?
You can use our infobox editor  to edit triples. Please follow our . We are currently only accepting triples in the English language, though we plan to expand this as soon as possible.
How can I perform verification tasks?
The  covers mechanics and common questions around verification.
I have been adding triples, are my efforts being counted?
Yes! You will eligible for an airdrop reward relative to the number of correct triples you have submitted when we launch our token on the mainnet.
Note: for additions to be counted towards airdrop rewards they must follow the  and not attempt to game the protocol.
I have been adding citations, are my efforts being counted?
Yes! Adding valid citations to any triple that is missing a citation will qualify you for a special airdrop, and will help the triples you have cited become verified. Citations should be focused around triples that are not URL predicates, especially triples added after the launch of .
Will any contribution to  count for a future airdrop?
No. We are focused on triples that go on to be verified along with citations for triples. As of February 16, 2022, natural language and prose in articles will not be rewarded. If you still wish to contribute prose, please follow our . We are currently only accepting prose in the English language, though we plan to expand this as soon as possible.
What is the difference between  and the  (Golden.xyz)?
​ is the current place to register your user account, connect your wallet and submit triple data (with citations). The  is a minimal dApp on testnet with a focused UI around verification.
Initial testnet point allocations will not be included in a future airdrop
The initial testnet points that are allocated when a user joins the dApp are used as an initial staking mechanic by the protocol to enable triple submission and verification. This initial testnet point allocation will NOT be considered in a future mainnet airdrop reward. Testnet points are designed to reward users for taking positive actions in the protocol.
How can I find my position on the leaderboard?
You may be able to find your current position on the leaderboard. If the number of ‘submissions’ and ‘accepted triples’ you see associated with your wallet seem lower than expected, this is because your submissions from  are still being imported and verifiers still need to vote on them.
Why is Golden the right team to build this?
Golden’s team has crypto enthusiasts dating back to 2011, some being early users and supporters of BTC. Golden's investors have also been at the heart of many crypto projects we see in the market today.
Do I need to paste the edit I have done into Discord?
No, we have full logs of all edits being made on  and the .
When are other languages going to be supported?
We want to prove the unit economics and security of the system first in English (the language of our original team). If it works, we want to open up to multiple languages (as it should be!). Please don’t make non-English edits at this point, as we don’t support it yet.
I want to be a mod in Discord, how should I approach Golden?
We are still configuring Discord for mass scale. At this time, please refrain from DMing team members as this will only slow the protocol development down. However, long term, we are interested in mods. If you have experience in this area, please add that to your introduction in the "introductions" channel. We are booting up moderators in a careful way to prevent security issues.
Can I change the eth account address associated with my  account / used to login into dapp.golden.xyz?
You cannot change the eth account address associated with your  account or that you used to login into dapp.golden.xyz. This would cause issues with how attribution for effort is tracked. To use a new .eth account, please create a new account on .
We plan to explore how we can help users not lose previous work in the case of wallet hacks, loss of login information, etc., in the context of these technical constraints.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[5b847818c1...](https://github.com/mrakgr/The-Spiral-Language/commit/5b847818c1506765d025d3edb88d6b10bf9919a1)
#### Tuesday 2022-12-27 19:07:23 by Marko Grdinić

"https://youtu.be/p_sLhKeo6ys?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy&t=1247

Here is the 64mb bank. Sigh, I have no idea what was wrong with me.

https://youtu.be/zF70xuhesME?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy&t=404

I think I need to think in terms of banks, but I am not sure how that works.

https://youtu.be/zF70xuhesME?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy&t=563

`v8 = DpuSet(nr_dpus=1, binary=f'kernels/g{v7}.dpu')`

So this is literally the number of dpus, not the number of ranks?

https://youtu.be/zF70xuhesME?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy&t=794

I hate this company so much it is unreal.

https://youtu.be/zF70xuhesME?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy&t=1244

How do ranks come into this?

12:55pm. It does not matter how they comes into it. I am 100% sure that I need to be thinking in terms of individual DPU banks when passing in data. Though it does make it confusing to me as how this would work when the array cannot be split into equal chunks. Knowing UPMEM it probably wouldn't.

1:15pm. Let me do the chores here. Then I'll do some more work in the C backend. I need to make sure that the UPMEM backend calls the buddy allocator. I forgot about that.

2pm. Let me plug in that buddy allocator.

2:10pm.

```fs
    let malloc, free =
        match backend_type with
        | Prototypal -> "malloc", "free"
        | UPMEM_C_Kernel _ -> "buddy_malloc", "buddy_free"

    let print_decref s_fun name_fun type_arg name_decref =
        line s_fun (sprintf "void %s(%s * x){" name_fun type_arg)
        let _ =
            let s_fun = indent s_fun
            line s_fun (sprintf "if (x != NULL && --(x->refc) == 0) { %s(x); %s(x); }" name_decref free)
        line s_fun "}"
```

Piece of cake. I had to fold `print_decref` in, but that was not a problem.

2:10pm. Now what do I do for the rest of the day?

I caught up to my reads, but my stress is very high. I'd be a lot more motivated to program if the UPMEM contact matched some of my energy, but right now...

Let me switch.

Let me do some writing for a couple of days. I've programming like a madman for the past 10 days. Right now everything is set, but I just don't feel like going at it. I hate this kind of responsibility that has uncertain payoff.

It is not like owe it to UPMEM to finish it.

I've been losely thinking of doing a Graphcore backend instead.

But no. I should at least do the map kernel to completion

Ok, let me write for a few hours. It is important to let the programming stuff linger for a few days. Right now I feel sick of it, but later I won't be able to stop myself from doing it. There is no point in pushing myself.

Times like these are painful, because I 'want' to program, but I can't for psychological reasons. I want to keep going, but I feel shackled by mental fatigue.

'Those are just feelings.' You might say. But stress is very much a real thing. I remember how in the 2015-2017 I used to just push through. And then I started thinking that the lump in my stomach was an actual illness and went around seeing doctors.

2:30pm. Forget that, let me write for a few days until I really want to program again.

2:45pm. I had an idea. Let me just test whether I can read from the `DPU_MRAM_HEAP_POINTER`. The `mram_read` functions do not have offsets.

```py
>>> 1048576
1048576
>>> hex
<built-in function hex>
>>> hex(1048576)
'0x100000'
```

Python is so convenient. I wanted to know what the pointer is in hexadecimal, but didn't even have look up the documentation to get it to work. The interpreter is so fast to start too. Ok, I love Python all of a sudden.

```
printf("%u\n",DPU_MRAM_HEAP_POINTER+1);
```

Pushing it forward increments the offset linearly.

```c
int32_t main(){
    __dma_aligned uint8_t v0[512];
    printf("%u\n",DPU_MRAM_HEAP_POINTER+1);
    mram_read(DPU_MRAM_HEAP_POINTER, v0, sizeof(v0));
    return 0l;
}
```

This could work. I need to make sure to align the offsets on byte 8 addresses, but other than that it will be fine.

I won't need to print out global static arrays thankfully.

I'll have to figure out how to copy it on the Python end, but I should be able to figure that out. Forget that.

Writing.

3:10pm. Or more precisely peeking at the UPMEM Python library. It was easy to get PyLance to do what I want. Thought I had to first set the env and then run `code .`. Going straight into editor did not work.

`profile: str = '',`

Here is the profile. This is what I should be passing into the function.

```
    def copy(
            self,
            dst: DpuCopyBuffer,
            src: DpuCopyBuffer,
            size: Optional[int] = None,
            offset: int = 0,
            async_mode: Optional[bool] = None):
        """
        Copy data between the Host and the DPUs

        Args:
            dst (DpuCopyBuffer): the destination buffer for the copy.
                If the buffer is on the Host, this must be a bytearray, or a list of optional bytearrays.
                If the buffer is on the DPUs, this must be a str, representing a DPU symbol, or directly a DpuSymbol.
            src (DpuCopyBuffer): the source buffer for the copy.
                If the buffer is on the Host, this must be a bytearray, or a list of optional bytearrays.
                If the buffer is on the DPUs, this must be a str, representing a DPU symbol, or directly a DpuSymbol.
            size (Optional[int]): number of bytes to transfer.
                By default set to None, which will use the length of the Host buffer. If multiple Host buffers are
                provided, all buffers must have the same size.
            offset (int): offset in bytes for the DPU symbol.
                By default set to 0.
            async_mode (Optional[bool]): override the default behavior set in the constructor.

        Raises:
            DpuError: if the copy fails, because of invalid arguments, unknown symbols or out-of-bound accesses
        """
```

It turns out the UPMEM has good documentation.

Let me check out `DpuSymbol`s.

```
class DpuSymbol():
    """
    Symbol in a DPU program

    Attributes:
        name (str): the name of the symbol
    """

    def __init__(self, name: str,
                 c_symbol: Union[ffi.struct_dpu_symbol_t, Tuple[int, int]]):
        self.name = name
        if isinstance(c_symbol, ffi.struct_dpu_symbol_t):
            self.c_symbol = c_symbol
        else:
            self.c_symbol = ffi.struct_dpu_symbol_t()
            self.c_symbol.address = c_symbol[0]
            self.c_symbol.size = c_symbol[1]

    def value(self) -> int:
        """
        Fetch the symbol value (ie. when done on a variable, its address)

        Returns:
            int: the symbol value
        """
        return self.c_symbol.address

    def size(self) -> int:
        """
        Fetch the symbol size

        Returns:
            int: the symbol size
        """
        return self.c_symbol.size
```

Oh you can in fact get the address. I'll have to test whether `DPU_MRAM_HEAP_POINTER` works as a symbol. I should try doing a search.

Let me just try it out. What the hell.

3:35pm.

```py
#!/usr/bin/env python3

from dpu import DpuSet
from dpu import ALLOCATE_ALL

BUFFER_SIZE = 1 << 16

def populate_mram(dpus):

    buffer = bytearray([1,2,3,4])
    dpus.copy('buffer', buffer)

with DpuSet(1, binary = "trivial_checksum_example") as dpus:

    populate_mram(dpus)
    dpus.exec()

    checksum = [bytearray(4) for _ in dpus]
    dpus.copy(checksum, 'checksum')
    print("Computed checksum = 0x%08x" %(int.from_bytes(checksum[0], 'little')))
```

This works. But when I try my own example it does not.

```c
#include <mram.h>
#include <stdbool.h>
#include <stdint.h>

#define CACHE_SIZE 256
#define BUFFER_SIZE (1 << 16)

__mram_noinit uint8_t buffer[BUFFER_SIZE];
__host uint32_t checksum;

int main() {
  __dma_aligned uint8_t local_cache[CACHE_SIZE];
  checksum = 0;

  for (unsigned int bytes_read = 0; bytes_read < BUFFER_SIZE;) {
    mram_read(&buffer[bytes_read], local_cache, CACHE_SIZE);

    for (unsigned int byte_index = 0; (byte_index < CACHE_SIZE) && (bytes_read < BUFFER_SIZE); byte_index++, bytes_read++) {
      checksum += (uint32_t)local_cache[byte_index];
    }
  }

  return checksum;
}
```

Why is the symbol defined when I try this example, but not my own?

```c
__mram_noinit uint8_t buffer[128];
__host uint32_t checksum;

int main() {
    __dma_aligned uint8_t local_cache[CACHE_SIZE];
    mram_read(&buffer[0], local_cache, CACHE_SIZE);
}
```

Ah. I get it. I think it will get pevaled away if it is not used. UPMEM can be annoying like that. I have to `mram_read` it in order to prevent that from happening.

But how do I use the heap pointer from Python?

3:55pm. I sent an email to support asking them about it. My luck with interacting with others has been attrocious lately, but maybe they will field this question. If not it does not matter, I'll just create symbol to take the place of that pointer. Right now I have what I need to make what I need work.

4pm. Let me try writing again. I should assume I have everything set. Forget about that crappy pointer.

7:45pm. 34.8k. Let me stop writing here. It has been a while since I uploaded anything new to Patreon so let me do it now.

7:50pm. Looking at the Heaven's Key dashboard I see that views are at 5,990. Avg at 133. 509 pages. Followers at 29 and faves at 8.

It is more bearable to look at this slow progression every few days. I am not going to get anywhere as a writer, so it good to mix up the two hobbies. It really felt refreshing writing this.

It is important to find a writing style that feels natural. Trying to write like a robot would be too hard for a human like me.

How much have I written today?

Oh, over 2.8k words. Yeah. this is why breaks are good. It is easier to get a release when I you are pent up.

The reason why I botched the social interaction with the UPMEM guy was due to overabundance of programming energy. It will be a good lesson for when I interact with other companies.

I am changing my plans a little. I am only going to do the generic map kernel. After that I'll wrap up the UPMEM backend and write a short article about it. My main target is the Tenstorrent discord where my old post is squating, but I'll also fish on HN, the PL sub and the Python one. That will give me time to look at the Graphcore device. It would be a better expenditure of my time that doing more stuff for UPMEM. Finishing the Python kernel was useful for me because it gave me the change to tighten up the language, but working on more kernels will not gain me anything. Instead that Graphcore free instance on Paperspace is what I should be looking for.

It just can't be helped that it came to this with UPMEM. I write nasty things in this journal and that is how it should be. My based spirit is here for all to see!"

---
## [GeoB99/reactos](https://github.com/GeoB99/reactos)@[a7989514a6...](https://github.com/GeoB99/reactos/commit/a7989514a62d4f448fde2eb8110c8c63ae5f6222)
#### Tuesday 2022-12-27 19:32:34 by George Bișoc

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
## [vijithassar/bisonica](https://github.com/vijithassar/bisonica)@[5151b4a2f2...](https://github.com/vijithassar/bisonica/commit/5151b4a2f265a2b081f04aec5f5d6b89cc7db1bf)
#### Tuesday 2022-12-27 19:33:49 by Vijith Assar

chore(core): don't use typeof in undefined checks

Removes typeof checks everywhere a conditional checks for an undefined value. This was once a historical best practice because it used to be possible to change the value of undefined, but that's no longer the case in modern browsers. This change also means that an undefined check with a variable that has not been declared will throw a ReferenceError. That used to be sort of scary, but it's more disciplined to allow them – those errors should be early and catastrophic so as to encourage code styles where they are still impossible because they are appropriately guarded against.

In theory, this does make it a bit harder to get inside the conditionals where errors are thrown, which is a bit of a shame – instead of the helpful error message text, you'd get a cryptic ReferenceError, because the ReferenceError blocks the code path into the better error message!

But none of this matters, because the linter should prevent this kind of mistake anyway.

---
## [TheWolfbringer/tgstation](https://github.com/TheWolfbringer/tgstation)@[9e69e5d6ac...](https://github.com/TheWolfbringer/tgstation/commit/9e69e5d6acae10bf0941155c418ea3b9194668e5)
#### Tuesday 2022-12-27 19:44:04 by LemonInTheDark

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
## [Seth7171/EkrutClient](https://github.com/Seth7171/EkrutClient)@[2326756814...](https://github.com/Seth7171/EkrutClient/commit/2326756814963d2b9abd86c6a3da6ae92db7a85d)
#### Tuesday 2022-12-27 19:45:21 by Seth7171

Fuck you -> goodbye
and added javadocs to the project

---
## [Rombuilding-X00TD/android_kernel_asus_sdm660](https://github.com/Rombuilding-X00TD/android_kernel_asus_sdm660)@[1f7d4ee20e...](https://github.com/Rombuilding-X00TD/android_kernel_asus_sdm660/commit/1f7d4ee20edb979cfb128dd42a8346e7de16b67b)
#### Tuesday 2022-12-27 20:00:23 by Christian Brauner

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
## [SkullNightMegaFan/LOZClone](https://github.com/SkullNightMegaFan/LOZClone)@[9630d36f3f...](https://github.com/SkullNightMegaFan/LOZClone/commit/9630d36f3fa0b311cae64e7882b60a6d8ea041f6)
#### Tuesday 2022-12-27 20:52:02 by Brenton

I have added the working prototype that I have already. Below are the things that I want to add to the project. When all of these things are in the game this project will be "complete"
Being able to attack with the wooden sword when picked up.
Music playing at the appropriate time.
Enemies being spawned in when a player enters a room.
Bombs and rupee's dropping when the player defeats enemies.
The secrets in the original zelda map.
The ability to go to and fro, different rooms.
Fixing Link's sprites. It's not an immediate issue but super annoying.
Adding items like the magic rod, boomerang, etc.
Adding different enemy types.
Adding a proper game over screen. (includes animation)
A save function

That's all I can think of, but those are the main things. I will be continuing to edit this until we have a complete replication of the original legend of zelda.

---
## [kperdue2002/mojave-sun-13](https://github.com/kperdue2002/mojave-sun-13)@[a6c05d5f86...](https://github.com/kperdue2002/mojave-sun-13/commit/a6c05d5f86f26fb30be08eeb64d50215d6977653)
#### Tuesday 2022-12-27 21:30:40 by Iamgoofball

Removes the fucking 20 second stunlock rng from tourettes because it's fucking stupid and I just had the most agonizing thirty fucking minutes of my goddamn life, holy shit (#64416)

Removes the 20 second stunlock from tourettes

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[da4a3ea34d...](https://github.com/TaleStation/TaleStation/commit/da4a3ea34d61faabaeaccc0868e7737d3e9d8887)
#### Tuesday 2022-12-27 22:03:19 by Jolly

Backports Loadouts QoL/Refactor, whatever the fuck we wanna call it (#3793)

* wew would you look at that, i can backport code WITHOUT it being halfassed to high hell and back

* let me be clear (i half assed this okay)

* commnets this code out because its stupid

---
## [pizie11/orbstation](https://github.com/pizie11/orbstation)@[6dd4839ef3...](https://github.com/pizie11/orbstation/commit/6dd4839ef321aa0a997549d1ae07fe7ccbba59ed)
#### Tuesday 2022-12-27 22:21:11 by carshalash

Gatfruit will no longer drop from ice portals. (#72048)

## About The Pull Request

For some god-forsaken reason, somebody decided that ice portals should
be able to drop one of the most disruptive items in the game. This PR
amends this by removing it from the drop pool.

## Why It's Good For The Game

In 2013 gatfruit was introduced in the following PR #2000 . This was
almost a decade ago at this point, repeatedly through the PR the creator
states his belief that this item should only ever be obtainable through
admin intervention due to its ridiculous capabilities. At the time
everyone in the PR agreed it was a reasonable item to add **as it was
unobtainable without admin intervention**. Over the years, it has crept
its way to become more prevalent and openly obtainable, the most
offensive of these options is the ice moon portal. As is, there is a 1
in 28 chance of obtaining the seeds, this sounds pretty inoffensive
right? That's just 3.44% probability. Now, let us search the instances
of the portal that spawns this.


![image](https://user-images.githubusercontent.com/16896032/208220173-bbefe604-0885-44a5-9add-b5f0c62067cc.png)

That is a big number, a lot of chances to get that seed packet and other
gamer looters. Now, let's take a look at the probability of being able
to get these seeds, assuming you wipe out all of the portals.


![image](https://user-images.githubusercontent.com/16896032/208220460-3f59a2ac-d936-4f3a-aa14-9c637af6a9d7.png)

92.8% chance to be able to get these seeds each shift if you focus
entirely on gaming the portals. That's a pretty insane probability of
being able to obtain the gatfruit seeds.

While I dislike people who sprint to the seed vault, there is at least
the possibility of a pod person telling them to fuck off when they
demand their _free_ gamer seed. There is also the fact that the ruin
isn't a guaranteed spawn every shift.

## Changelog

:cl:
balance: Gatfruit seeds will no longer drop from ice portals.
/:cl:

---
## [pizie11/orbstation](https://github.com/pizie11/orbstation)@[00e7d5d746...](https://github.com/pizie11/orbstation/commit/00e7d5d7465211ccf0e3d604e566e2c08775cd20)
#### Tuesday 2022-12-27 22:21:11 by GoldenAlpharex

*hand, or That /One/ Emote You Always Felt Was Missing (#71600)

## About The Pull Request
It's happened to me _repeatedly_ that I'd see someone down on the floor,
and wanted to just, give them a hand, so they could take it and get up
that way, without just, directly clicking on them, since that's a little
bland. I've also wanted to just, offer my hand to someone so they could
grab it, so that I could pull them alongside me, rather than just
targeting one of their arms and ctrl-clicking them.

I've had this idea for a _long_ time, and only just decided to do this
today.

Now, I know what you might say. "Golden, that's a lot of code for
something this simple!" You're not wrong. _However_. I decided to go
along and to give some more love to the `/datum/status_effect/offering`
status effect and the offering-related alerts, to make them a lot more
versatile and a lot less hardcoded. Hence the whole "refactoring" part
of this.

Of course, when I add something, I don't do it half-way. So, the way the
emote works is much like the `*slap` emote, except that:

- When you click on someone, it does the exact same as if you were
offering the item to them, except that it's targeted (much like
ctrl-shift-click).
- If there's nobody directly adjacent to you, it won't do anything.
- If there's at least one person lying down around you, you will offer
them your help to get up. Should they take your hand and let you help
them up, you will both receive a simple memory about being helped up (or
helping up), as well as a 45-seconds-long small mood buff, because it
feels nice to be on either end of such a friendly gesture. If they get
up, they automatically get disqualified from being offered some help
standing up, and likewise, if you lie down, that offer goes away as
well.
- If there's at least one person around you, you will instead extend
your hand in their direction, for them to grab onto it. Should they do
so, you will then grab them by their arms and pull them.

I reworked the offering status effect to no longer have a hardcoded
`can_hold_items()` check, so that kisses and the hand offering would no
longer need you to have free hands to complete. The logic here is that
you can still pull someone even with both hands filled, so I figured I'd
leave it this way.

Note: If anyone would like to give the item a better sprite, by all
means, go ahead, that'd be amazing. I'm just not really a great spriter
and couldn't be bothered to waste hours making a very _meh_ hand.

## Why It's Good For The Game
It's fluff, and nice fluff at that. It makes it easier for people to be
nice to one-another without having to necessarily spend so long writing
up an emote that the person on the floor will already have gotten back
up. I'm sure the MRP folks will like it, and I'm certain the HRP
downstreams will love it too ;)

## Changelog

:cl:
add: Added the *hand emote, which you can offer to someone standing up
in order to give them the possibility to grab onto your hand and let you
drag them away, or to someone lying down to help them back up, which
always makes everyone involved a little happier!
refactor: De-hardcoded and genericized a lot of the offering status
effect and alert code, to make it require a lot less copy-paste to
handle new cases.
fix: Offering a kiss no longer requires the receiver to have free hands
to accept said kiss!
/:cl:

---

