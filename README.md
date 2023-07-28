## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-07-27](docs/good-messages/2023/2023-07-27.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,282,612 were push events containing 3,560,529 commit messages that amount to 279,689,406 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 49 messages:


## [Ben10Omintrix/tgstation](https://github.com/Ben10Omintrix/tgstation)@[d875610098...](https://github.com/Ben10Omintrix/tgstation/commit/d875610098a1259a5112d4a0e5afc0b7bd32ff6d)
#### Thursday 2023-07-27 00:19:27 by Rhials

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
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[f8054819a5...](https://github.com/TaleStation/TaleStation/commit/f8054819a5ecb7f7e3c8d3c21d95f3341356b44a)
#### Thursday 2023-07-27 00:20:21 by TaleStationBot

[MIRROR] [MDB IGNORE] Adds in the smoothbore disablers. (#6844)

Original PR: https://github.com/tgstation/tgstation/pull/76773
-----
## About The Pull Request

This PR adds in a craftable smoothbore disabler, a pistol companion to
the lethal laser musket. Unlike the musket, it fires a disabler shot.
Singular. Weak in armor too. After you fire it, you've gotta crank it,
but only one crank.

The good thing about it is that you can simply add more smoothbores to
your inventory, and use 4 of them to take down a target.

The bad thing is that it's a smoothbore (which for an energy weapon,
means no lens is installed). It has 22.5 degrees of inaccuracy. Have
fun.

Militia Men start with a holster containing two of these, fitting with
their equipment. But of course, the Militia General has an upgraded
laser musket, so... He needs a better smoothbore too.

**INTRODUCING THE ELITE SMOOTHBORE DISABLER**
Using ANCIENT TECHNOLOGIES and PURE BLING, you can fire TWO shots, not
be weak against armour AND have actual accuracy (and a +5 damage boost
because i figured why the hell not). This is the strongest upgraded
variant of the shitty maint guns, so the tome to craft it is currently
unavailable. I want someone to figure out a creative way to put it
somewhere that isn't just a random spawn in maintenance.


![image](https://github.com/tgstation/tgstation/assets/13697285/02c396b8-4b72-45f8-b471-a006df132aff)

The Militia General only has one elite smoothbore. It's too rare and
powerful to simply have two. Even though a regular disabler is better in
every way.

Smoothbore Disabler Recipe:
1x Weapon Stock
5x Cable Coil
1x Pipe
1x Micro-Laser
1x Power Cell
1x Mouse Trap
Needs: Screwdriver, Wrench. Takes 10 seconds to make.

Elite Smoothbore Disabler Recipe:
1x Smoothbore Disabler
5x Gold Ingots/Sheets
1x Hyper-Capacity Power Cell
10u Tempomyocin
Needs: Screwdriver. Takes 20 seconds to make.
Recipe requires recipe book.

## Why It's Good For The Game

Having a sidearm to go with your laser musket is neat, alongside the
fact that it just allows following up on someone. I don't have much to
say honestly, I just think it's neat. Also the idea of an assistant
going FULL BLACKBEARD, carrying 4 pistols and having to toss them away
in order to shoot again cracks me up.

Oh and this is the part for coders: I've de-spaghettified some code with
the maint gun recipe granters, and the gun crank is now a component.
It's likely you could use it on any item that sends the proper signal,
so I kind of overbuilt it on purpose.

Also the attack_self on guns now returns parent. This should allow it to
send a signal alongside putting your grubby fingerprints on the weapon
when you switch modes. There could be bugs but they should be easy to
fix if they pop up, mode switching on guns works without a fuss.

## Changelog

:cl:
add: Added the smoothbore disabler and it's prime variant. You can now
craft a disabler with only one shot and terrible accuracy.
code: Gun cranking has been made a component and could theoretically be
used on more than guns.
/:cl:

---------

Co-authored-by: CRITAWAKETS <sebastienracicot@hotmail.com>

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[7e29b9ef63...](https://github.com/TaleStation/TaleStation/commit/7e29b9ef63fa1674b30e1b3298d7aef8e9c1805b)
#### Thursday 2023-07-27 00:20:21 by TaleStationBot

[MIRROR] [MDB IGNORE] Adds a new positive quirk, "Spacer Born".  (#6840)

Original PR: https://github.com/tgstation/tgstation/pull/76809
-----
## About The Pull Request

Adds a new 7 point positive quirk, "Spacer Born". Totally not inspired
by The Expanse, don't look at the branch name.

You were born in space, rather than on a planet, so your physiology has
adapted differently.
You are more comfortable in space, and way less comfortable on a planet.

Benefits:
   - You are slightly taller. (No mechanical effect)
   - You take 20% less damage from pressure damage.
   - You take 20% less damage from cold environments. 
- You move 10% faster while floating (NOT drifting, this is zero gravity
movement while beside a wall).
- You drift 20% faster (Drifting through zero gravity, untethered to
anything)
- While in space (z-level-wise, not turf wise), you lose some disgust
overtime.
- While experiencing no-gravity for an extended period of time, you will
start regenerating stamina and reduce stuns at a very low rate.
- If you are assigned to shaft miner (or the map is Icebox), you are
awarded with a 25% wage bonus (hazard pay).

Downsides:
- While on a planet (Yes, this includes Icebox and planetary maps), you
gain gravity sickness:
- Passive accrue disgust (slightly lessened on Icebox) (Capped at low
levels)
      - Choking, after extended periods (disabled on Icebox)
      - Slower movement 
      - Weaker stamina (disabled on Icebox)
- Suffocation from extended periods (disabled on Icebox) (Lungs aren't
adapted)
      - Mood debuff

(Effects not final)

## Why It's Good For The Game

I'd figure I throw my hat in with the Positive Quirk Curse. 

This is a quirk that improves your ability in a niche circumstance (low
gravity / dangerous pressure), with some downsides that are only
generally in effect if you play a few roles (or it's Icebox).

Because of this I think it'll provide an interesting niche, where Spacer
Born engineers are slightly better than their counterparts due to their
origin (moving faster in space without a jetpack, withstanding
pressure). However, at the same time, if the mining outpost sustains
damage and needs repairs... suddenly your buff over your cohorts
disappears, and you have to brave somewhere hostile to your body.

Ultimately, the goal of the quirk is to encourage people to approach
situations a bit differently.
Or take it as a challenge and play shaft miner. 

## Changelog

:cl: Melbert
add: Adds a new 7 point positive quirk, "Spacer Born". You were born in
space, and as a result your body's adapted to life in artificial
gravity, making you much more effective and comfortable in lower
gravity. However, travelling planet-side is quite a chore, especially if
you're assigned to work there.
add: Adds a chemical: Ondansetron, created by Oil + Nitrogen + Oxygen +
Ethanol catalyst. A powerful Antiemetic (lowers disgust).
/:cl:

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>
Co-authored-by: Jolly-66 <70232195+Jolly-66@users.noreply.github.com>

---
## [Zar000/TerraGov-Marine-Corps-Zaro](https://github.com/Zar000/TerraGov-Marine-Corps-Zaro)@[ca4b66185f...](https://github.com/Zar000/TerraGov-Marine-Corps-Zaro/commit/ca4b66185ffa363692529f8340a43cccab02cbf1)
#### Thursday 2023-07-27 00:22:21 by chizzy376

Gives the Umbilical Tad shutters on side windows. (#13490)

* y

* Update combat_patrol.dm

* Update combat_patrol.dm

Sometimes I think about if life is really worth the hassle, if I really have to deal with so much bs only to then have to believe hard enough to get into heaven. Am I a good person for heaven? Do I deserve it? fuck if i know

* Finish fixing my fuckup

---
## [Chief-Engineer/space-station-14](https://github.com/Chief-Engineer/space-station-14)@[31607a0be0...](https://github.com/Chief-Engineer/space-station-14/commit/31607a0be0e2ef24f4d53c7611172ec6d40a3a2b)
#### Thursday 2023-07-27 00:31:58 by Emisse

hardsuit/firesuit cleanup (#18308)

* real

* hjoly fuck you guy sare annoying

* fix cargo arbitrage idk why tf it changed from editing armor values but fuck my life i guess

* why god

* Update suits.yml

* Update cargo_emergency.yml

---
## [DeeGee22/clovermon-showdown](https://github.com/DeeGee22/clovermon-showdown)@[a7edb0ddbb...](https://github.com/DeeGee22/clovermon-showdown/commit/a7edb0ddbbc1e8056e2e3b4f5cf918b97731e96c)
#### Thursday 2023-07-27 00:52:03 by DeeGee22

Fixes More Wack Moves

Ares Strike
Omoikane
Ramesseum Tentyris
Hieroglyphein
Poseidon Wave
Frigid Heaven
Miracle Reprisal
God's Maw
Volt Bind
Magic Circle
Healing Circle
Steel Casting
Channel
Prophecy
Forecast
Phantom Sword
Steam Scald
Bibliomancy
Astronomy
Poof!
Gadget
Future Passed
Mystery Slayer
Dual Divinity

---
## [shiptest-ss13/Shiptest](https://github.com/shiptest-ss13/Shiptest)@[1b315a616f...](https://github.com/shiptest-ss13/Shiptest/commit/1b315a616ff24e3f1f92c791e4df4dc43ca9aad6)
#### Thursday 2023-07-27 01:14:55 by Thedragmeme

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
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[d2ce9f014e...](https://github.com/TaleStation/TaleStation/commit/d2ce9f014eed4d894b145804ec412bd0d2eab78e)
#### Thursday 2023-07-27 01:14:56 by TaleStationBot

[MIRROR] [MDB IGNORE] Syndicate Duffelbag Rerework (#6981)

Original PR: https://github.com/tgstation/tgstation/pull/77060
-----
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

Co-authored-by: carlarctg <53100513+carlarctg@users.noreply.github.com>
Co-authored-by: Jolly-66 <70232195+Jolly-66@users.noreply.github.com>

---
## [SpringSkipper/Paradise](https://github.com/SpringSkipper/Paradise)@[a3dc32cf34...](https://github.com/SpringSkipper/Paradise/commit/a3dc32cf344dbd441e85f6cbb694b166dc1f5e4b)
#### Thursday 2023-07-27 01:16:16 by ATP-Engineer

Fixes issue where Turret Control sprites arent actually updated in previous PR (#21538)

* Removes actual turret file

FUCK

* Fixes turret controllers not actually being changed

GOD DAMNIT.

---
## [NaN0987/better-quora](https://github.com/NaN0987/better-quora)@[668b0c6373...](https://github.com/NaN0987/better-quora/commit/668b0c6373a2c1419701ae7621540548b106721c)
#### Thursday 2023-07-27 01:30:32 by NaN0987

adds comments of original poster

I swear to fucking god queryselectors are the most annoying shit in the world. With the other stuff in javascript, you can use intellisense and linter errors to figure out what you can and can't do, but with queryselectors it's a giant magic string that either works 70% of the time or gives you an error that tells you your queryselector is wrong without telling you why.
Anyway there's a bug with comments that have a "(more)" button, but once I fix that the bulk of this extension is officially done.

---
## [dragondk53/mimsa](https://github.com/dragondk53/mimsa)@[e26ca2a932...](https://github.com/dragondk53/mimsa/commit/e26ca2a9320e5c59b7b12433bc7d36b2cdfa8b99)
#### Thursday 2023-07-27 02:26:50 by Daniel Harvey

Actually typecheck multiple definitions (#962)

* Test module typechecking more throughly

* Damn this shit is fucked

* We need to make these types stricter

* Skippy

* Nice

---
## [ImFlyTo/VRMocap](https://github.com/ImFlyTo/VRMocap)@[db1481129a...](https://github.com/ImFlyTo/VRMocap/commit/db1481129a211d646ef05bc71636a10d4b89ed52)
#### Thursday 2023-07-27 02:27:09 by Megasteakman

UE5.1.1 - Calibration Mode Overlay

Added a nice new UI overlay to let you know that you are in Calibration Mode after hearing some people get confused about what happens when you first start the system.  If you don't like it, disconnect it in the function for VRPlayerMode_CalibrationMode.

Did a lot of work on the UE5 Manny control rig.  It could be better.  It could be worse.  I find it really hard to tell sometimes, so I did leave the old one in MegaMocapVR\ControlRigs\WIP_ControlRigs\OLD_MMVR_UE5Manny_ControlRig

The UE5 Manny control rig now has a way to lock the arm goals to the chest control, so you can use it for animation/cleanup a bit easier.  This variable is exposed to cinematics, which is a sick feature I want to make more use out of.

I reduced the tick on the editor utility widget.

Revamped the teleprompter, creating a new Teleprompter Screen actor that gets spawned in if you use the new event on the player pawn 'Event_TeleprompterUpdate.

Did some small changes to the metahuman control rig, but... I don't remember what they were.  Again, who knows if its better.  I think I made an 'is valid' check on the iphone name so it wouldn't throw you errors if no iphone was added to the player pawn.

---
## [lpeapnni/dustbowl-blues](https://github.com/lpeapnni/dustbowl-blues)@[9bcf5d42f2...](https://github.com/lpeapnni/dustbowl-blues/commit/9bcf5d42f2da5ab8757867ee8f6b539c43b785e0)
#### Thursday 2023-07-27 02:28:30 by Lyroy

Merge pull request #8 from lpeapnni/OMFG-PASS-THE-FUCKING-TESTS

PASS THE FUCKING CI TESTS YOU STUPID PIECE OF SHIT

---
## [CyanMatter/atlas-2023](https://github.com/CyanMatter/atlas-2023)@[e348042f1c...](https://github.com/CyanMatter/atlas-2023/commit/e348042f1c3bb42abe2a720c1c88100843b2ba31)
#### Thursday 2023-07-27 02:31:43 by Cyan

Replace description of Germany x The Netherlands Kabedon

The current description is meant to be funny, not informative. The two jokes in it are copied comments from a Reddit post; and the statement that the line about 'Duitsland-san' is on the canvas is inaccurate. Half of the description is dedicated to explaining one of the jokes.

This commit proposes to replace the description to include an description of kabedon, the PlaceDE & PlaceNL collaboration, and a visual summary of the boy and the girl.

---
## [SheheryarRamzan/NASCON-WebApplication](https://github.com/SheheryarRamzan/NASCON-WebApplication)@[fbac0b1ef4...](https://github.com/SheheryarRamzan/NASCON-WebApplication/commit/fbac0b1ef491d379a9c0486ea69100685b2570a9)
#### Thursday 2023-07-27 04:00:13 by Sheheryar Ramzan

Add files via upload

The NASCON Web Application is a comprehensive platform designed to facilitate and enhance the experience of participants and administrators in the National Students' Convention (NASCON) organized by FAST. This web application is built with an ASP.NET front-end framework, providing an intuitive and user-friendly interface for participants to sign up for various events and competitions while enabling administrators to efficiently manage customer data and oversee event logistics.

Key Features:

User Registration and Event Signup: Participants can easily register on the platform, creating personalized accounts to explore and sign up for the events of their interest. The application offers a seamless and streamlined event registration process, maximizing user convenience.

Event Details and Schedule: Users can access comprehensive information about the various events and competitions hosted during NASCON. They can view event details, timings, and locations, allowing them to plan their participation effectively.

User Dashboard: Each user is provided with a personalized dashboard where they can track their registered events, view updates, and manage their profile information.

Admin Dashboard: The administrative side empowers event organizers and administrators to manage customer data efficiently. From user registrations to event details, administrators have full control over the application's backend.

Event Management: Administrators can add, edit, or remove events, competitions, and their respective details. This feature ensures that all event information is up-to-date and readily accessible to participants.

Customer Management: The application facilitates easy management of user data, allowing administrators to view, edit, and organize customer information as required.

Communication and Notifications: The platform incorporates a communication system that allows administrators to send notifications, reminders, and updates to registered participants.

Technologies Used:

Front-end: ASP.NET framework
Back-end: SQL Server
Other technologies as needed (HTML, CSS, JavaScript, etc.)

Project Goals:
The primary objective of the NASCON Web Application is to create a centralized platform that optimizes the event experience for both participants and administrators. By providing an intuitive user interface, streamlined event registration, and efficient backend management, the application aims to enhance engagement and accessibility for all stakeholders involved in NASCON. The project serves as an integral tool in fostering a vibrant and dynamic environment for this prestigious annual event.

This repository is an ongoing project that continues to evolve and improve with the changing needs and requirements of NASCON, reflecting the commitment to excellence and technological innovation in supporting the celebration of science and technology at FAST.

How to run this project?

Just create an asp.net project on Visual Studio and copy all the pages files in your project name folder. The folder will be in the same folder as your sln file. Then you are good to go.

---
## [Miiyo/android_kernel_sony_sdm845](https://github.com/Miiyo/android_kernel_sony_sdm845)@[e22711502e...](https://github.com/Miiyo/android_kernel_sony_sdm845/commit/e22711502e2e865b8ab644b57cff9a8273e87f82)
#### Thursday 2023-07-27 06:38:33 by Angelo G. Del Regno

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
5	      20220479
2	      20940223
1	      21231290

Remember again that we're loading from a UFS card and that
we are loading ~1.1MB more out of a 20MB file.
If you're smart enough you surely know already about RAM and CPU
overhead of very high compression levels.

If you still disagree with what I just did, read this commit description
another 20 times, or more, until you understand it. :)))

Signed-off-by: TogoFire <togofire@mailfence.com>
Change-Id: Ic28bff2011b40631fc81b582a25029ac8d12d48e

---
## [AnywayFarus/Skyrat-tg](https://github.com/AnywayFarus/Skyrat-tg)@[dcd2d0e418...](https://github.com/AnywayFarus/Skyrat-tg/commit/dcd2d0e418fbd85c3e990a02f61ab05d2993e1e1)
#### Thursday 2023-07-27 07:03:21 by SkyratBot

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
## [AnywayFarus/Fluffy-STG](https://github.com/AnywayFarus/Fluffy-STG)@[54ce0ae44a...](https://github.com/AnywayFarus/Fluffy-STG/commit/54ce0ae44ae9c1534fe4e4917a7be0e83a69d589)
#### Thursday 2023-07-27 07:03:56 by SkyratBot

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
## [tematikkp/thetm](https://github.com/tematikkp/thetm)@[f8617ff259...](https://github.com/tematikkp/thetm/commit/f8617ff259d6603d6f5f650dedfa0d1d7d525010)
#### Thursday 2023-07-27 07:36:39 by THETM / Tematikkp

4 previous play sessions yesterday, updated

holy sheet it's the wysi date that fes+ is released god damnit

---
## [DataDog/libdatadog](https://github.com/DataDog/libdatadog)@[9d47fc76c9...](https://github.com/DataDog/libdatadog/commit/9d47fc76c97a054041ff8833dae164a090153e0f)
#### Thursday 2023-07-27 08:18:30 by Ivo Anjo

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
## [Flyvs/Game](https://github.com/Flyvs/Game)@[b256a6fc80...](https://github.com/Flyvs/Game/commit/b256a6fc80b60a785b37e596fc9d6677484faeba)
#### Thursday 2023-07-27 08:23:55 by Janek Jahnke

msgbox with \n works; more readable. Holy shit that was annoying

---
## [Volcanware/Envy-Client](https://github.com/Volcanware/Envy-Client)@[e752caf05a...](https://github.com/Volcanware/Envy-Client/commit/e752caf05ab09e137eebffafaba61a605d6ac9d1)
#### Thursday 2023-07-27 08:44:00 by Volcan

Added Baritone Follow to Bot Module || Fuck you Hardline for making me go to sleep

---
## [Tesserium/crawl](https://github.com/Tesserium/crawl)@[b58dd9be76...](https://github.com/Tesserium/crawl/commit/b58dd9be76988dc3a81b0cb9877e484eb7efd520)
#### Thursday 2023-07-27 09:06:57 by Nicholas Feinberg

Feat: magic mapping -> revelation

Magic mapping is a cool item, but I often find it sitting in my
inventory unused for the great majority of a game. I might use it
early on to find a timed portal if I'm having trouble, but after
that, it sits around until Zot. That's not exciting!

Meanwhile, the removal of Ashenzari's Astral Vision in 1891117ce2a
(Sept 2022) left a mechanical gap. We removed the "see through walls"
effect for a variety of UI and bug reasons, but it's still neat.
If the player only saw through walls for a moment, until the end of
their turn, there'd be no problem. So... let's kill two birds with one
scroll!

Scrolls of revelation still map the level, like magic mapping, but
they also reveal everything in LOS radius - monsters, items, unseen
horrors, you name it. This should hopefully create more incentive
to use magic mapping throughout the game - you might want to see
what's inside a scary looking vault or behind a door, for example.

It does break the legendary door vault a bit, but truthfully, that
thing was meant to be broken. If players want to spend a scarce
resource to peek inside, they can do that. :)

UI issue - invisible monsters vanish completely once your turn ends,
so you might want to note them down. Might poke at this at some point.

---
## [DeadlyBag/Yogstation](https://github.com/DeadlyBag/Yogstation)@[d1c7dfdc1a...](https://github.com/DeadlyBag/Yogstation/commit/d1c7dfdc1ae55bfd9fa7f603f415b762ba6a472a)
#### Thursday 2023-07-27 09:27:29 by SapphicOverload

IPC tweaks (#19467)

* funny tv head robot go brrrrr

* Update IPC.dm

* not that fast

* fuck it we ball

---
## [Jvr2022/vscode](https://github.com/Jvr2022/vscode)@[72e342a8a4...](https://github.com/Jvr2022/vscode/commit/72e342a8a4363a45ffd059fdb1d867494a701f36)
#### Thursday 2023-07-27 10:11:54 by Jvr for school

Update bug_report.md


D3D Floating Point Behavior.

Model: Default (GPT-3.5)


Hoe kan ik dit maken in directxshadercompiler Is your feature request related to a problem? Please describe.
There is a difference in specified behavior between floating point rounding behavior between DXBC, LLVM 3.7 and modern LLVM.
For example:
Conversion from float32 (e.g. from shader constants) to float16 may or may not flush float16 denorm to 0, and round to zero is used, per D3D spec for high to low precision float. This doesn't match the llvm specification for floating point rounding behavior.

Describe the solution you'd like
The floating point rounding behavior should exactly match the specifications described in D3D / HLSL. To do this, the underlying implementation may need to change, or the current specification may need to be updated.

ChatGPT
To address the specified behavior related to floating point rounding in DirectXShaderCompiler, you will need to ensure that the compiler follows the correct specifications described in D3D (Direct3D) and HLSL (High-Level Shading Language). This will involve either updating the underlying implementation to match the D3D specifications or updating the current specification if necessary. Below are some steps you can take to try to achieve this:

Review the D3D and HLSL Specifications:
Familiarize yourself with the relevant sections of the D3D and HLSL specifications that define the floating-point rounding behavior. Understand how conversions from higher precision to lower precision (e.g., float32 to float16) are supposed to handle denormals and rounding.

Investigate the Current Behavior:
Analyze the existing behavior of the DirectXShaderCompiler when converting between different precision floating-point types. Identify where the discrepancies exist between the actual behavior and the D3D/HLSL specifications.

Update the Compiler Implementation:
If you have access to the DirectXShaderCompiler source code, you can modify the implementation to adhere to the D3D/HLSL specifications. This may involve adjusting the conversion routines and ensuring that denormals are flushed to zero and rounding is performed as specified.

Contribute to the Project:
If DirectXShaderCompiler is an open-source project, you can contribute your changes to the community. Submit a pull request with your modifications, clearly explaining the changes you made and why they align with the D3D/HLSL specifications.

Work with the DirectXShaderCompiler Team:
If DirectXShaderCompiler is not an open-source project or you're unable to contribute directly, you can try to reach out to the development team responsible for the compiler. Share your findings and insights about the discrepancies in floating-point rounding behavior and advocate for changes to bring it in line with D3D/HLSL specifications.

Consider Alternative Approaches:
If updating the compiler implementation to match D3D/HLSL specifications is not feasible or not permitted, you may need to explore alternative solutions. This could involve performing additional manual steps in your shaders or using custom shader code to achieve the desired rounding behavior explicitly.

Remember that any changes to the compiler behavior should be carefully considered and tested to ensure they do not introduce new issues or break existing code. Also, keep in mind that my knowledge is up to September 2021, and the DirectXShaderCompiler project may have evolved since then. Always refer to the latest documentation and community resources for the most current information.





Ik heb toegang tot de github dus wat moet ik doen

ChatGPT
Als je toegang hebt tot de GitHub-repository van DirectXShaderCompiler, kun je wijzigingen voorstellen en bijdragen aan het project om de floating-point rounding behavior aan te passen volgens de specificaties van D3D/HLSL. Hier zijn de stappen die je kunt volgen:

Clone de Repository:
Begin door de GitHub-repository van DirectXShaderCompiler te clonen naar je lokale ontwikkelomgeving. Dit kan worden gedaan met behulp van de git clone-opdracht.

Maak een Branch:
Voordat je wijzigingen aanbrengt, maak je een nieuwe branch voor je werk. Gebruik een duidelijke naam die het doel van je wijzigingen beschrijft. Dit helpt om wijzigingen georganiseerd en beheersbaar te houden.

Begrijp de Huidige Implementatie:
Bestudeer de huidige implementatie van de compiler om te begrijpen hoe floating-point rounding momenteel wordt afgehandeld. Identificeer de delen van de code die verantwoordelijk zijn voor conversies tussen verschillende precisiepuntsgetallen.

Implementeer de Correcties:
Gebruik de kennis uit de D3D- en HLSL-specificaties om de floating-point rounding behavior aan te passen volgens de gewenste specificaties. Pas de conversieroutines aan om denormals te flushen naar nul en ervoor te zorgen dat het afronden wordt uitgevoerd zoals gespecificeerd.

Test je Wijzigingen:
Zorg ervoor dat je je wijzigingen grondig test om ervoor te zorgen dat ze correct werken en dat ze de gewenste gedragingen van D3D/HLSL reproduceren. Dit omvat unit-tests en integratietests om te controleren of bestaande functionaliteit niet is aangetast.

Dien een Pull Request in:
Nadat je je wijzigingen hebt getest en ervoor hebt gezorgd dat alles correct werkt, dien je een pull request in bij het hoofdrepository van DirectXShaderCompiler. In je pull request-leg je duidelijk uit welke wijzigingen je hebt aangebracht en waarom ze in lijn zijn met D3D/HLSL-specificaties.

Communicatie met de Gemeenschap:
Wees bereid om met de gemeenschap te communiceren over je wijzigingen en eventuele feedback te bespreken. Het kan zijn dat andere ontwikkelaars suggesties hebben om je code te verbeteren, dus wees open voor samenwerking en discussie.

Reviewproces:
De bijdragen aan open-sourceprojecten worden vaak beoordeeld door andere ontwikkelaars voordat ze worden samengevoegd. Houd er rekening mee dat het





Welke bestanden moet ik editen

ChatGPT
In DirectXShaderCompiler zijn er meerdere bestanden betrokken bij het compileren van HLSL-shaders. Als je de floating-point rounding behavior wilt aanpassen, zijn hier enkele bestanden waarin je waarschijnlijk wijzigingen moet aanbrengen:

HLSLConversion.cpp:
Dit bestand bevat de implementatie van conversies tussen verschillende datatypen in HLSL, inclusief conversies tussen verschillende precisiepuntsgetallen (bijvoorbeeld float32 naar float16). Hier kun je de conversieroutines vinden en aanpassen om de gewenste floating-point rounding behavior te bereiken.

dxilconv.hlsl:
Dit bestand bevat HLSL-code voor het converteren van HLSL-shaders naar DXIL (DirectX Intermediate Language). Dit omvat mogelijk conversie-instructies tussen verschillende precisiepuntsgetallen, die relevant kunnen zijn voor de floating-point rounding behavior.

dxilconv.cpp:
In dit bestand wordt de logica voor het uitvoeren van DXIL-conversies geïmplementeerd. Als de conversies tussen precisiepuntsgetallen worden afgehandeld buiten HLSLConversion.cpp, kun je hier ook relevante code vinden.

dxilutil.cpp:
Dit bestand bevat enkele hulpprogrammafuncties die worden gebruikt bij het omgaan met DXIL. Afhankelijk van de implementatie kan hier ook code relevant zijn voor floating-point rounding.

CodeGenHLSL.cpp en CodeGenHLSL.h:
Deze bestanden bevatten de HLSL-codegenerator, die HLSL-shaders vertaalt naar LLVM IR (Intermediate Representation). Als de floating-point rounding behavior van invloed is op de gegenereerde LLVM IR, kun je hier ook relevantie vinden.

Houd er rekening mee dat het mogelijk is dat de codebase sinds mijn laatste kennisupdate (september 2021) is veranderd en dat nieuwe bestanden zijn toegevoegd of dat de structuur is gewijzigd. Het is daarom essentieel om de actuele broncode te bekijken en mogelijke wijzigingen in de codebase te identificeren.

Voor de meest recente en nauwkeurige informatie raad ik aan om de officiële GitHub-repository van DirectXShaderCompiler te raadplegen en eventueel contact op te nemen met de gemeenschap of de ontwikkelaars voor begeleiding bij je bijdragen.





Ik moet die bestanden editen om dit te doen Is your feature request related to a problem? Please describe.
There is a difference in specified behavior between floating point rounding behavior between DXBC, LLVM 3.7 and modern LLVM.
For example:
Conversion from float32 (e.g. from shader constants) to float16 may or may not flush float16 denorm to 0, and round to zero is used, per D3D spec for high to low precision float. This doesn't match the llvm specification for floating point rounding behavior.

Describe the solution you'd like
The floating point rounding behavior should exactly match the specifications described in D3D / HLSL. To do this, the underlying implementation may need to change, or the current specification may need to be updated.

ChatGPT
Om de floating-point rounding behavior in DirectXShaderCompiler aan te passen en ervoor te zorgen dat het exact overeenkomt met de specificaties van D3D/HLSL, moet je inderdaad de relevante bestanden bewerken. Het belangrijkste bestand waar je waarschijnlijk wijzigingen moet aanbrengen, is "HLSLConversion.cpp", omdat dit verantwoordelijk is voor de conversies tussen verschillende datatypen in HLSL, inclusief precisiepuntsgetallen.

Hier zijn de stappen die je kunt volgen om de floating-point rounding behavior aan te passen:

Identificeer Conversiefuncties:
Open het bestand "HLSLConversion.cpp" en identificeer de functies die verantwoordelijk zijn voor de conversies tussen verschillende precisiepuntsgetallen. Deze functies moeten worden aangepast om ervoor te zorgen dat de conversies overeenkomen met de D3D/HLSL-specificaties.

Begrijp de Huidige Implementatie:
Analyseer de bestaande code in de relevante conversiefuncties om te begrijpen hoe de floating-point rounding momenteel wordt afgehandeld. Zoek naar eventuele discrepanties met de D3D/HLSL-specificaties.

Implementeer de Correcties:
Pas de code in de conversiefuncties aan om ervoor te zorgen dat de floating-point rounding behavior exact overeenkomt met de specificaties van D3D/HLSL. Dit omvat het flushen van denormals naar nul en het uitvoeren van het juiste afronden.

Test je Wijzigingen:
Zorg ervoor dat je uitgebreide tests uitvoert om te controleren of de aangepaste conversiefuncties correct werken en dat ze de gewenste gedragingen van D3D/HLSL reproduceren. Test verschillende scenario's, inclusief conversies van float32 naar float16 met verschillende waarden.

Dien een Pull Request in:
Nadat je je wijzigingen lokaal hebt getest en ervoor hebt gezorgd dat alles correct werkt, dien je een pull request in bij het hoofdrepository van DirectXShaderCompiler. Hiermee bied je je wijzigingen aan om te worden beoordeeld en opgenomen in de officiële codebase.

Het is belangrijk om te communiceren met de ontwikkelaarsgemeenschap van DirectXShaderCompiler en feedback te ontvangen op je bijdragen. Houd er rekening mee dat het proces van het aanpassen van de code en het indienen van een pull request enige tijd kan duren, omdat de wijzigingen grondig worden beoordeeld voordat ze worden opgenomen. Volg de richtlijnen van het project en wees geduldig gedurende dit proces.





Kan jij deze bug report template beter maken en nieuwe functies toevoegen ---
name: Bug report
about: Create a report to help us improve
---
<!-- ⚠️⚠️ Do Not Delete This! bug_report_template ⚠️⚠️ -->
<!-- Please read our Rules of Conduct: https://opensource.microsoft.com/codeofconduct/ -->
<!-- 🕮 Read our guide about submitting issues: https://github.com/microsoft/vscode/wiki/Submitting-Bugs-and-Suggestions -->
<!-- 🔎 Search existing issues to avoid creating duplicates. -->
<!-- 🧪 Test using the latest Insiders build to see if your issue has already been fixed: https://code.visualstudio.com/insiders/ -->
<!-- 💡 Instead of creating your report here, use 'Report Issue' from the 'Help' menu in VS Code to pre-fill useful information. -->
<!-- 🔧 Launch with `code --disable-extensions` to check. -->
Does this issue occur when all extensions are disabled?: Yes/No

<!-- 🪓 If you answered No above, use 'Help: Start Extension Bisect' from Command Palette to try to identify the cause. -->
<!-- 📣 Issues caused by an extension need to be reported directly to the extension publisher. The 'Help > Report Issue' dialog can assist with this. -->
- VS Code Version: 
- OS Version: 

Steps to Reproduce:

1. 
2. 

ChatGPT
Sure! I've improved the bug report template and added some new sections for additional information:

markdown
Copy code
name: Bug report
about: Create a report to help us improve

<!-- ⚠️⚠️ Do Not Delete This! bug_report_template ⚠️⚠️ -->
<!-- Please read our Rules of Conduct: https://opensource.microsoft.com/codeofconduct/ -->
<!-- 🕮 Read our guide about submitting issues: https://github.com/microsoft/vscode/wiki/Submitting-Bugs-and-Suggestions -->
<!-- 🔎 Search existing issues to avoid creating duplicates. -->
<!-- 🧪 Test using the latest Insiders build to see if your issue has already been fixed: https://code.visualstudio.com/insiders/ -->
<!-- 💡 Instead of creating your report here, use 'Report Issue' from the 'Help' menu in VS Code to pre-fill useful information. -->
<!-- 🔧 Launch with `code --disable-extensions` to check. -->

**Issue Description:**
<!-- A clear and concise description of what the bug is. -->

**Does this issue occur when all extensions are disabled?:**
<!-- Yes/No -->

**VS Code Version:**
<!-- Provide the version of Visual Studio Code you are using (e.g., 1.60.0). -->

**OS Version:**
<!-- Provide the version of your operating system (e.g., Windows 10, macOS Big Sur, Ubuntu 20.04). -->

**Steps to Reproduce:**
<!-- Provide step-by-step instructions to reproduce the issue. -->
1. 
2. 

**Expected Behavior:**
<!-- A clear and concise description of what you expected to happen. -->

**Actual Behavior:**
<!-- A clear and concise description of what actually happens. -->

**Screenshots / GIFs:**
<!-- If applicable, add screenshots or GIFs to help explain the issue. -->

**Additional Information:**
<!-- Add any additional information that may be helpful in understanding the issue. -->
With these improvements, the bug report template now includes sections for the following information:

Issue Description: A brief description of the bug.
Does this issue occur when all extensions are disabled?: To check if the problem is related to any installed extensions.
VS Code Version: The version of Visual Studio Code you are using.
OS Version: The version of your operating system.
Steps to Reproduce: Detailed steps to reproduce the issue.
Expected Behavior: What you expected to happen.
Actual Behavior: What actually happens.
Screenshots: Optional, for visual representation of the issue.
Additional Information: Any extra details that might help in understanding the problem.

---
## [Seinuve/Seisen](https://github.com/Seinuve/Seisen)@[bf1e31d533...](https://github.com/Seinuve/Seisen/commit/bf1e31d5330e5efd94f38a2e8af92d15f2f89597)
#### Thursday 2023-07-27 10:22:17 by Seinu

fixed some weird error where edit_sei_line was—
expecting an int for a replacement value and not—
a string.

seisen.py updated for the changes above ^
same with vocab.py and words.py

Removed debugging statements that were in add_csep

added replace_vocab_value (holy hell that was suffering)

Fixed a formatting issue in searcher

---
## [ixWatan/acteen-app](https://github.com/ixWatan/acteen-app)@[ce2fe49d2e...](https://github.com/ixWatan/acteen-app/commit/ce2fe49d2ed7ff29d2f4413a8ecf8e044742585f)
#### Thursday 2023-07-27 11:09:17 by Watan Asaad

nevo code for nevo its thursday, its 2:00 pm me and nevo are chilling , the demo day is tommorow , we are all hyped, thank you nevo for this amazing journey, thx to my team PM's and UXers and Designers, i love you all, thx to larine for coding with us, thx lyel for helping us with the code, yossi and ibrahim the amazing TA's, our cordinators, and to this whole journey, about 150 commits of shitty and unreliable code, but at the end, we enjoyed a lot

for the future me and future nevo

WE DID GREAT HABIBI <3

---
## [AbhishekSrivastava2701/OasisInfoByte_Tribute-Page](https://github.com/AbhishekSrivastava2701/OasisInfoByte_Tribute-Page)@[8bed0adafe...](https://github.com/AbhishekSrivastava2701/OasisInfoByte_Tribute-Page/commit/8bed0adafe44c4e3a4b09dfc65d4b17287181cd1)
#### Thursday 2023-07-27 13:08:04 by Abhishek Srivastava

Add files via upload

A Tribute Page is a dedicated page celebrating the life and memory of your loved one. It is a permanent memorial where, you, family and friends can remember your loved one and share many memories and photos to celebrate their life.

---
## [mamedev/mame](https://github.com/mamedev/mame)@[6db28f4041...](https://github.com/mamedev/mame/commit/6db28f40416aa72a75128537e29b20985c26c75d)
#### Thursday 2023-07-27 13:28:42 by A-Noid33

New working software list items (mac - macii) 123 dumps (#11432)

* Initial softlist for mac moof 400/800 floppy disks

* Added mac moof software list support

New working software list items (123 working dumps)
-------------------------------
mac_flop_orig:

Lode Runner (version 1.0) [4AM, Anoid]
Balance of Power (version 1.03) [4AM, Anoid]
Shanghai (version 1.0) [4AM, Anoid]
Skyfox [4AM, Anoid]
Temple of Apshai Trilogy [4AM, Anoid]
The Surgeon (version 1.5) [4AM, Anoid]
Uninvited [4AM, Anoid]
King's Quest (version 1.10) [4AM, Anoid]
Smash Hit Racquetball (version 1.01) [4AM, Anoid]
The Ancient Art of War [4AM, Anoid]
Hacker II [4AM, Anoid]
Rambo: First Blood Part II [4AM, Anoid]
One on One [4AM, Anoid]
Indiana Jones and the Revenge of the Ancients [4AM, Anoid]
Winter Games (version 1985-10-24) [4AM, Anoid]
Winter Games (version 1985-10-31) [4AM, Anoid]
Star Trek: The Kobayashi Alternative (version 1.0) [4AM, Anoid]
Mac Attack [4AM, Anoid]
GATO (version 1.3) [4AM, Anoid]
Dark Castle (version 1.0) [4AM, Anoid]
Oids (version 1.4) [4AM, Anoid]
MacWars [4AM, Anoid]
Shadowgate [4AM, Anoid]
Seven Cities of Gold [4AM, Anoid]
Enchanted Scepters [4AM, Anoid]
Beyond Dark Castle [4AM, Anoid]
Arkanoid (version 1.00) [4AM, Anoid]
The Chessmaster 2000 (version 1.02) [4AM, Anoid]
Maze Survival [4AM, Anoid]
Frogger (version 1.0) [4AM, Anoid]
SimCity (version 1.2, black & white) [4AM, Anoid]
Falcon (version 1.0) [4AM, Anoid]
Cutthroats (release 23 / 840809-C) [4AM, Anoid]
The Witness (release 22 / 840924-C) [4AM, Anoid]
Seastalker (release 15 / 840522-C) [4AM, Anoid]
Zork III (release 17 / 840727-C) [4AM, Anoid]
A Mind Forever Voyaging (release 77 / 850814-E) [4AM, Anoid]
Hollywood Hijinx (release 37 / 861215-I) [4AM, Anoid]
Nord and Bert Couldn't Make Head or Tail of It (release 19 / 870722-I) [4AM, Anoid]
Border Zone (release 9 / 881008-3B) [4AM, Anoid]
The Hitchhiker's Guide to the Galaxy (release 47 / 840914) [4AM, Anoid]
Zork I: The Great Underground Empire (release 76 / 840509) [4AM, Anoid]
Deadline (release 27 / 831005-C) [4AM, Anoid]
Infidel (release 22 / 840522-C) [4AM, Anoid]
Suspect (release 14 / 841005-C) [4AM, Anoid]
Planetfall (release 29 / 840118-B) [4AM, Anoid]
Ballyhoo (release 97 / 851218-G) [4AM, Anoid]
Enchanter (release 24 / 851118-G) [4AM, Anoid]
Spellbreaker (release 63 / 850916-F) [4AM, Anoid]
Trinity (release 11 / 860509-3H) [4AM, Anoid]
Stationfall (release 107 / 870430-G) [4AM, Anoid]
The Lurking Horror (release 203 / 870506-G) [4AM, Anoid]
Alter Ego (male version 1.0) [4AM, Anoid]
Alter Ego (version 1.1 female) [4AM, Anoid]
The Print Shop (version 1.2) [4AM, Anoid]
Flight Simulator (version 1.02) [4AM, Anoid]
Run for the Money [4AM, Anoid]
Master Tracks Pro (version 4.0) [4AM, Anoid]
Where in Time is Carmen Sandiego? (version 1.0) [4AM, Anoid]
Deluxe Music Construction Set (version 1.0) [4AM, Anoid]
Apache Strike (version 1.2) [4AM, Anoid]
Wizardry VI: Bane of the Cosmic Forge [4AM, Anoid]
Harrier Strike Mission [4AM, Anoid]
Airborne! [4AM, Anoid]
Mac Vegas (version 1.1) [4AM, Anoid]
Dragonworld [4AM, Anoid]
MacDraft (version 1.2) [4AM, Anoid]
The Mind Prober (version 1.0) [4AM, Anoid]
The Toy Shop (version 1.1) [4AM, Anoid]
Strategic Conquest (version 1.2) [4AM, Anoid]
The Home Accountant (version 1.01) [4AM, Anoid]
Sub Battle Simulator [4AM, Anoid]
Vegas Video Poker [4AM, Anoid]
The Pawn (version 2.3) [4AM, Anoid]
Downhill Racer [4AM, Anoid]
Dollars and Sense (version 1.3) [4AM, Anoid]
Alternate Reality: The City (version 3.0) [4AM, Anoid]
Borrowed Time [4AM, Anoid]
The Quest [4AM, Anoid]
The Crimson Crown [4AM, Anoid]
Mindshadow [4AM, Anoid]
Pensate (version 1.1) [4AM, Anoid]
Sierra Championship Boxing [4AM, Anoid]
Championship Star League Baseball [4AM, Anoid]
Forbidden Castle [4AM, Anoid]
Defender of the Crown [4AM, Anoid]
The King of Chicago [4AM, Anoid]
Macintosh Pascal (version 1.0) [4AM, Anoid]
Fusillade [4AM, Anoid]
Orb Quest: Part I: The Search for Seven Wards (version 1.04) [4AM, Anoid]
Speed Reader II (version 1.1) [4AM, Anoid]
][ in a Mac (version 2.03) [4AM, Anoid]
Q-Sheet (version 1.0) [4AM, Anoid]
Fontographer (version 2.4.1) [4AM, Anoid]
Mouse Stampede (version 1.00) [4AM, Anoid]
The Mist [4AM, Anoid]
Tass Times in Tonetown [4AM, Anoid]
Pinball Construction Set [4AM, Anoid]
Transylvania [4AM, Anoid]
Déjà Vu: A Nightmare Comes True!! [4AM, Anoid]
Déjà Vu II: Lost in Las Vegas!! [4AM, Anoid]
Rogue (version 1.0) [4AM, Anoid]
Bridge (version 6.0) [4AM, Anoid]
Harrier Strike Mission II (version 1.2) [4AM, Anoid]
Patton vs. Rommel (version 1.05) [4AM, Anoid]
Moebius: The Orb of Celestial Harmony (version 1.03) [4AM, Anoid]
Tesserae (version 1.06) [4AM, Anoid]
Where in Europe is Carmen Sandiego? (version 1.0) [4AM, Anoid]
Shufflepuck Cafe (version 1.0) [4AM, Anoid]
Geometry (version 1.1) [4AM, Anoid]
Physics (version 1.2) [4AM, Anoid]
SimCity (version 1.1) [4AM, Anoid]
Murder by the Dozen [4AM, Anoid]
The Duel: Test Drive II [4AM, Anoid]
Master Tracks Pro (version 1.10) [4AM, Anoid]
Master Tracks Pro (version 2.00h) [4AM, Anoid]
Master Tracks Pro (version 3.4a) [4AM, Anoid]
Squire (version 1.1) [4AM, Anoid]
Millionaire (version 1.0) [4AM, Anoid]
Microsoft File (version 1.04) [4AM, Anoid]
Microsoft Excel (version 1.00) [4AM, Anoid]
The Fool's Errand (version 2.0) [4AM, Anoid]
MacGammon! (version 1.0) [4AM, Anoid]

---------

Co-authored-by: Bob Schultz <bobschultz03@gamil.com>

---
## [lovullo/tame](https://github.com/lovullo/tame)@[61d556c89e...](https://github.com/lovullo/tame/commit/61d556c89e587628f83f6acdf0db8f12788bf071)
#### Thursday 2023-07-27 14:15:44 by Mike Gerwitz

tamer: pipeline: Generate recoverable sum error types

This was a significant undertaking, with a few thrown-out approaches.  The
documentation describes what approach was taken, but I'd also like to
provide some insight into the approaches that I rejected for various
reasons, or because they simply didn't work.

The problem that this commit tries to solve is encapsulation of error
types.

Prior to the introduction of the lowering pipeline macro
`lower_pipeline!`, all pipelines were written by hand using `Lower` and
specifying the applicable types.  This included creating sum types to
accommodate each of the errors so that `Lower` could widen automatically.

The introduction of the `lower_pipeline!` macro resolved the boilerplate and
type complexity concerns for the parsers by allowing the pipeline to be
concisely declared.  However, it still accepted an error sum type `ER` for
recoverable errors, which meant that we had to break a level of
encapsulation, peering into the pipeline to know both what parsers were in
play and what their error types were.

These error sum types were also the source of a lot of tedious boilerplate
that made adding new parsers to the pipeline unnecessarily unpleasant;
the purpose of the macro is to make composition both easy and clear, and
error types were undermining it.

Another benefit of sum types per pipeline is that callers need only
aggregate those pipeline types, if they care about them, rather than every
error type used as a component of the pipeline.

So, this commit generates the error types.  Doing so was non-trivial.

Associated Types and Lifetimes
------------------------------
Error types are associated with their `ParseState` as
`ParseState::Error`.  As described in this commit, TAMER's approach to
errors is that they never contain non-static lifetimes; interning and
copying are used to that effect.  And, indeed, no errors in TAMER have
lifetimes.

But, some `ParseState`s may.  In this case, `AsgTreeToXirf`:

```
impl<'a> ParseState for AsgTreeToXirf<'a> {
  // [...]
  type Error = AsgTreeToXirfError;
  // [...]
}
```

Even though `AsgTreeToXirfError` does not have a lifetime, the `ParseState`
it is associated with _does_`.  So to reference that type, we must use
`<AsgTreeToXirf<'a> as ParseState>::Error`.  So if we have a sum type:

```
enum Sum<'a> {
  //     ^^ oh no!                  vv
  AsgTreeToXirfError(<AsgTreeToXirf<'a> as ParseState>::Error),
}
```

There's no way to elide or make anonymous that lifetime, since it's not
used, at the time of writing.  `for<'a>` also cannot be used in this
context.

The solution in this commit is to use a macro (`lower_error_sum`) to rewrite
lifetimes: to `'static`:

```
enum Sum {
  AsgTreeToXirfError(<AsgTreeToXirf<'static> as ParseState>::Error),
}
```

The `Error` associated type will resolve to `AsgTreeToXirfError` all the
same either way, since it has no lifetimes of its own, letalone any
referencing trait bounds.

That's not to say that we _couldn't_ support lifetimes as long as they're
attached to context, but we have no need to at the moment, and it adds
significant cognitive overhead.  Further, the diagnostic system doesn't deal
in lifetimes, and so would need reworking as well.  Not worth it.

An alternative solution to this that was rejected is an explicitly `Error`
type in the macro application:

```
// in the lowering pipeline
|> AsgTreeToXirf<'a> {  // lifetime
    type Error = AsgTreeToXirfError;   // no lifetime
}
```

But this requires peeling back the `ParseState` to see what its error is and
_duplicate_ it here.  Silly, and it breaks encapsulation, since the lowering
pipeline is supposed to return its own error type.

Yet another option considered was to standardize a submodule convention
whereby each `ParseState` would have a module exporting `Error`, among other
types.  This would decouple it from the parent type.  However, we still have
the duplication between that and an associated type.  Further, there's no
way to enforce this convention (effectively a module API)---the macro would
just fail in obscure ways, at least with `macro_rules!`.  It would have been
an ugly kluge.

Overlapping Error Types
-----------------------
Another concern with generating the sum type, resolved in a previous commit,
was overlapping error types, which prohibited `impl From<E> for ER`
generation.

The problem with that a number of `ParseState`s used `Infallible` as their
`Error` type.  This was resolved in a previous commit by creating
Infallible-like newtypes (variantless enums).

This was not the only option.  `From` fits naturally into how TAMER handles
sum types, and fits naturally into `Lower`'s `WidenedError`.  The
alternative is generating explicit `map_err`s in `lower_pipeline!`.  This
would have allowed for overlapping error types because the _caller_ knows
what the correct target variant is in the sum type.

The problem with an explicit `map_err` is that it places more power in
`lower_pipeline!`, which is _supposed_ to be a macro that simply removes
boilerplate; it's not supposed to increase expressiveness.  It's also not
fun dealing with complexity in macros; they're much more confusing that
normal code.

With the decided-upon approach (newtypes + `From`), hand-written `Lower`
pipelines are just as expressive---just more verbose---as `lower_pipeline!`,
and handles widening for you.  Rust's type system will also handle the
complexity of widening automatically for us without us having to reason
about it in the macro.  This is not always desirable, but in this case, I
feel that it is.

---
## [archy-bold/not-enough-musk-spambot](https://github.com/archy-bold/not-enough-musk-spambot)@[9af13cd797...](https://github.com/archy-bold/not-enough-musk-spambot/commit/9af13cd7979c5c5fd322d56581e2c7d2c5f5c313)
#### Thursday 2023-07-27 14:21:21 by Simon Archer

Zuck is a cuck
Competition is fine, cheating is not
It is infinitely preferable to be attacked by strangers on Twitter, than indulge in the false happiness of hide-the-pain Instagram
I would like to apologize for firing these geniuses. Their immense talent will no doubt be of great use elsewhere.
I propose a literal dick measuring contest 📏
Level 9 is make humanity a multiplanet species & true spacefaring civilization. That is why I am gathering resources.
You are free to be your true self here
Announcing formation of @xAI to understand reality
Looks like this platform may see all time high device user seconds usage this week
Frankly, I love the negative feedback on this platform. Vastly preferable to some sniffy censorship bureau!
X will become the most valuable brand on Earth. Make my words.
To sleep with women endlessly without love is a cursed and hollow life

---
## [harryob/cmss13](https://github.com/harryob/cmss13)@[39cf164c60...](https://github.com/harryob/cmss13/commit/39cf164c6075f21c280bf75aea538a7dd64a3d81)
#### Thursday 2023-07-27 14:36:41 by tool mind

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
## [harryob/cmss13](https://github.com/harryob/cmss13)@[56007685d7...](https://github.com/harryob/cmss13/commit/56007685d77ed8eab65ab2090e347940551fddc4)
#### Thursday 2023-07-27 14:36:41 by Zonespace

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
## [ParadiseSS13/Paradise](https://github.com/ParadiseSS13/Paradise)@[2d10818063...](https://github.com/ParadiseSS13/Paradise/commit/2d1081806334fc023de600338b836d55dd6fa5ee)
#### Thursday 2023-07-27 14:55:54 by ATP-Engineer

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
## [Comxy/tgstation](https://github.com/Comxy/tgstation)@[7e1d97af9e...](https://github.com/Comxy/tgstation/commit/7e1d97af9e4b6b7f90fbacc754fae939b6d16e49)
#### Thursday 2023-07-27 17:16:14 by Justice

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
## [Comxy/tgstation](https://github.com/Comxy/tgstation)@[0d769e0ffa...](https://github.com/Comxy/tgstation/commit/0d769e0ffaaa2b0f2be2edb9659c233860420ec1)
#### Thursday 2023-07-27 17:16:14 by Jacquerel

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
## [PelicanPlatform/pelican](https://github.com/PelicanPlatform/pelican)@[bc56423c42...](https://github.com/PelicanPlatform/pelican/commit/bc56423c4210dfa1e9a480bf5e449edd1acbc000)
#### Thursday 2023-07-27 17:26:51 by Justin Hiemstra

Local lint & Director CLI hookup + bug fixes

PR #7 introduced a framework for including the Director in the Pelican CLI,
toward making all Pelican services available under a single binary. This commit
extends that PR to hook the Director package up to the CLI, the Pelican's
configuration mechanisms, and to actually sort out a few bugs related to the
untested director code.

It should be noted that there are currently a few hacks in the code that need
clearing up before any merge, but as of now the commit makes the following
possible:
`pelican director serve --cache-port 8000`
This will serve the Director's cache-redirection service on port 8000 using a gin
engine. When we've figured out how to handle Origin redirects and implemented an
origin-redirect service, we'll be able to do:
`pelican director serve --cache-port 8000 --origin-port 8001`
to split apart the two endpoints.

As for the local lint... I'm still trying to figure out how to shut that feature
off in my editor. Sorry for the noise!

---
## [morrowwolf/cmss13](https://github.com/morrowwolf/cmss13)@[ce818246c1...](https://github.com/morrowwolf/cmss13/commit/ce818246c107cf97525a05f6f3a66e120117b8c3)
#### Thursday 2023-07-27 17:36:54 by QuickLode

The Hazmat Joe (#3259)

# About the pull request
This pull request resprites the entire Working Joe from toes to head. It
also gives two additional uniforms which are meant for hazardous use,
and this PR should act as a foundation for future implementation of the
Hazmat Joe into CM's gameplay. Additionally, I may just set this to
draft and let it be reviewed while I work on the actual implementation.

They are complete with distinctive loadouts, which focus more on
hazardous situations, repair, and firefighting. Though may tweak things
depending on how its implemented.

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game
This adds a fan favorite variation of your inexpensive, reliable friend!
You've seen him in quite a few places, and now he's coming to CM!

Also, the resprite of the Joe fixes up some minor sprite issues that
were encountered on previous models.

More content, more roleplay possibilities! ARES! Get me some Joes to put
that reactor fire out ASAP!
# Testing Photographs and Procedure

https://cdn.discordapp.com/attachments/490668342357786645/1104748917398175795/image.png

https://media.discordapp.net/attachments/490668342357786645/1105643891107049572/image.png
Ran several tests and they went well.


# Changelog
:cl:QuickLoad,Frans_Feiffer,nauticall
add: Adds The Hazmat Joe with two minor variations. This is a Working
Joe equipped to handle hazardous situations, dangerous repairs and
firefighting! They are complete with their own gear, tasks, job and
purpose. Forget the trashbag, get that wall fixed before we get spaced!
imageadd: Adds a new Working Joe model made by Frans Feiffer!
imageadd: Adds two variations of the Working Joe, aka the Hazmat Joe.
Complete with accessories! Beautiful sprites by Frans Feiffer!
add: Android Maintenance Stations / Synthetic Repair Stations will
remove shrapnel & fix organ damage. Working Joes no longer have knives,
and should report to the stations for repair. Gigantic thanks to
nauticall for her work on this!!
imagedel: Removes(replaces) the old Working Joe model.
add: Working Joes receive some basic equipment, and are slightly
resilient to disarms.
add: Working Joes will start at 3, with a maximum of 6 depending on
population.
add: Joes can access a Synthetic vendor to replace their uniform if it
is damaged.
fix: Minor changes to PO Uniform.
/:cl:

---------

Co-authored-by: naut <nautilussplat@gmail.com>
Co-authored-by: BeagleGaming1 <56142455+BeagleGaming1@users.noreply.github.com>

---
## [kbrock/manageiq-appliance](https://github.com/kbrock/manageiq-appliance)@[5fd9a28e21...](https://github.com/kbrock/manageiq-appliance/commit/5fd9a28e21b3bdf9cf3f179fc85fc2ee543a2779)
#### Thursday 2023-07-27 18:14:07 by Keenan Brock

use shell primitives for /etc/default/evm

using sed and xargs is not that slow, but since we source this
quite a lot, getting every second out of it

this is no longer `sh` friendly, thought to be honest, I'm not
sure if traditional bash (without [[ ]] linking to `test`) exists

---
## [nicholaschiang/site](https://github.com/nicholaschiang/site)@[ae8c04cbf4...](https://github.com/nicholaschiang/site/commit/ae8c04cbf45b2f2c8162cd2977f95fd4abf82334)
#### Thursday 2023-07-27 18:27:28 by Nicholas Chiang

feat(show/og): add show specific social images

This patch adds an OG image generation route for shows. It will generate
an image with the show name and a preview of the first three looks in
the show. This is a better experience than Vogue, in my opinion, as
Vogue simply crops the first look image in an awkward manner (because
the social media image aspect ratio is not very compatible with a look
image ratio).

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[f44adfde1e...](https://github.com/tgstation/tgstation/commit/f44adfde1eaa96b5f565937423603580cb19b3a6)
#### Thursday 2023-07-27 18:41:12 by nikothedude

Refactors vendor tipping and adds 2 new malf modules: Remote vendor tipping, and the ability to roll around and crush anything in your path. (#76635)

## About The Pull Request

Title.

Vendor tipping code is now on /atom/movable, and any movable can fall
over like a vendor does. Things like crits have been moved to
type-specific availability tables, their effects are now held in their
own proc, are now random per crushed item, have probability weights,
etc.

In the process of making this PR I also had to fix another issue, where
a bunch of take_damage() overrides had incorrect args, so that explains
the take_damage changes I made.

Tipping now also attacks any atoms on the target, given they use
integrity.

Adds 2 new malf modules.

1. REMOTE VENDOR TIPPING: A mid-cost and mid-supply module allows malf
AIs to remotely tip a vendor in any of the 8 directions. After 0.5
seconds of delay and a visual indicator (along with other warnings), the
vendor falls over.
1.1. In the process of making this I had to expand a arrow sprite to
have orthogonal directions, which is why you may see the testing dmi
being changed.
2. CORE ROLLING: A mid-cost but low-supply ability that allows the AI to
roll around and crush anything it falls on, including mobs. This has a
5% chance to have a critical hit so it isnt THAT terrible - plus it's
guaranteed to never stunlock. It's real utility lies in the fact the AI
now has limited movement without borgs. Also, the psychological factor.

As a bonus, vendor tipping now uses animate and transforms instead of
replacing matrices.
## Why It's Good For The Game

1. Generifying vendor tipping code is just good, period. It's a very
wacky and silly little piece of code that really doesn't need to be
isolated to vendors exclusively. ANY big and heavy object can fall over
and do a ton of damage.
1.1. Also, adding weights to critical hits is really good, because it
lets things like the headgib finally be a lot less terrifying, as
they're a lot less likely to happen.

2. Remote vendor tipping is a bit of a goofy ability that isn't really
THAT practical but has a chance of catching someone unaware and doing
some serious damage to that person alone.
2.1. Atop of this, vendor tipping isn't that loud of an action as say,
blowing things up, or doing a plasma flood. Even overrides aren't this
silent or a non-giveaway. A vendor falling on someone, though, is a
mundane thing that happens a lot. This is a decent way to assassinate
people before going loud (or at least, damage people) that isn't offered
yet.

4.
3.1. For real though, AIs rolling around is just fucking hilarious. The
ability to move isn't offered right now (which isn't that much of a bad
things), but with sufficiently limited charges (or limits to how many
times you can buy the ability), this can be a funny little t hing that
lets the AI potentially hide somewhere on the sat (or just relatively
close to the sat, such as engineering [it can't go through the
teleporter with this but it can go through transit tubes]) without the
need for borgs.
3.2. Also, it lets the AI sacrifically execute people by blowing up
their brains.

---
## [Ical92/tgstation](https://github.com/Ical92/tgstation)@[a8e16030f8...](https://github.com/Ical92/tgstation/commit/a8e16030f83911aef695ba9f28d565c41c99c3e6)
#### Thursday 2023-07-27 18:44:50 by LemonInTheDark

Optimizes timer insertion by 80% (W QDEL_IN micro) (#76214)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

[Reduces timer insertion cost by
80%](https://github.com/tgstation/tgstation/commit/c9e5b285ed74e60108fddd3f6b45d6d3995c92a8)

Timer name generation involved a LOT of string shit, some in ways where
the string only existed for a moment.
This costs a good bit of time, and can be reduced with only minimal
impacts on the end product, so let's do that. Includes a compile flag to
flip it back if we ever have trouble in future.

This is about 0.1s off init, since we do a lot of timer stuff then too

[Removes STOPPABLE flag from QDEL_IN, moves it to a bespoke
macro](https://github.com/tgstation/tgstation/commit/e7a5d7f2a78fcf0dce4742ced258c9505411b202)

Its a waste most of the time, tho I would LOVE to analyze at compile
time to work out if we care
## Why It's Good For The Game

I like it when we don't spend all of our cpu time just setting the name
var on timers. that's good and not bad.
This saves time fucking everywhere. 15% off explosions, 0.1 seconds off
init, bunch of time off foam. it's just good.

Cherry picked out of #76104 since that was too cluttered (sannnnnn)

<!-- Argue for the merits of your changes and how they benefit the game,
especially if they are controversial and/or far reaching. If you can't
actually explain WHY what you are doing will improve the game, then it
probably isn't good for the game in the first place. -->

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Ical92/tgstation](https://github.com/Ical92/tgstation)@[5c032cc098...](https://github.com/Ical92/tgstation/commit/5c032cc098f9a1d62f9f9dee133ae7c3e4489dca)
#### Thursday 2023-07-27 18:44:50 by LemonInTheDark

Adds border smoothing! (Look ma I'm upstreaming) (#76134)

## About The Pull Request

Ok so we currently have 1 (count em) border object that wants to smooth
with other border objects. That's the tram window.

It currently does this manually, via map edits, but that's kinda crappy
so lets be better.

This pr adds a new smoothing mode to handle border objects. 
Unlike other smoothing modes, it returns a bitfield of directions the
border object connects in.

I do this by memorizing a calculation of which dirs "connect" at init,
and reading out of a global list with border object direction, direction
between objects, and if it's a border object, the other object's dir.

I'm doing this primarily because it's become useful for wallening (a
spriter saw the tram thing and is doing the same thing to pod windows,
and I want to support that)

I do think it's potentially useful in other applications too tho, and I
like dehardcoding tram windows.

Also fun bonus (or maybe downside), it's nearly 0 cost because I pulled
the bitmask smoothing define into 2 subdefines, and am swapping the
handler one out to do what I want.
Oh also I got rid of a for loop in smoothing code, redundant and costs
time in list iteration

[Moves tram windows over to the new border object
smoothing](https://github.com/tgstation/tgstation/commit/114873679c94d680788edee9665fa18dba8108c0)

Also replaces some typepath chicanery with a setDir override, for
redundancy in future
Oh and there's a update paths script too, to be nice

## Why It's Good For The Game

More visual possibility in future, fixes a hack we have currently, and
makes some spriters happy.

## Changelog
:cl:
fix: Dehardcodes some stuff with tram windows, they'll be easier to map
with now
refactor: Border objects can now smooth with each other. I'm sure
something cool will come of this
/:cl:

---
## [nikothedude/tgstation](https://github.com/nikothedude/tgstation)@[746b75844c...](https://github.com/nikothedude/tgstation/commit/746b75844c0e05b521a2973cb0705fca304d287f)
#### Thursday 2023-07-27 18:52:07 by necromanceranne

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
## [nikothedude/tgstation](https://github.com/nikothedude/tgstation)@[9286933739...](https://github.com/nikothedude/tgstation/commit/92869337395a34eb372d7af6b3afaee4be4a7bef)
#### Thursday 2023-07-27 18:52:07 by Jacquerel

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
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[cc57581b73...](https://github.com/tgstation/tgstation/commit/cc57581b73e2979d775dfd9408978e4987b6635b)
#### Thursday 2023-07-27 18:54:10 by Sealed101

Dog wit the butter (feat. a bunch of dog-related code improvements) (#77039)

## About The Pull Request
Adds a `dog_fashion` for the stick of butter.(screenshot is outdated as
Lisa won't have butter no more)
![butter
dawgs](https://github.com/tgstation/tgstation/assets/75863639/a22e702c-98a8-4283-abd9-28d4a9fb3bd0)

Also cleans up dog.dm because it was SHIT and FUCK and MY FUCKING GOD
TWO INITIALIZE()s TWO TIMES IN A SINGLE FILE WHAT IN THE GODDAMN

Most noticeably, Lisa properly won't wear any hats, and puppies properly
can't wear head/back items (by just removing those item slots from the
strip/equip menu. if some admeme wants to fumble around they may still
equip shit there. but otherwise for a normal player those slots are
inaccessible).
Basic mobs now also send signals when they run
`appear_dead`/`appear_alive` procs, which corgis hook into to update
their dead fashion overlays.
The side-effect of getting that to work is that dogs (and any basic mob
that uses `play_dead` ai behavior) are so good at feigning death, that
they fool medical HUDs and other related things. They're just that good.
There's a bunch of other things involved and I was mostly just being
angry at the state of the file so I'll check back when I gather all
things changed.


![strippy](https://github.com/tgstation/tgstation/assets/75863639/ec4d17a2-d4df-401c-bd1f-7c4ee1b95671)


## Why It's Good For The Game


https://github.com/tgstation/tgstation/assets/75863639/b34589cb-94d6-4b80-bf0f-1814c08da100



## Changelog
:cl:
add: dog with a butter on 'em
add: dead dog with da butter on 'em (dogs feigning death are so good at
it, they appear dead to medical HUDs and other things)
add: Nars-Ian now can revive from the dead if he consumes a pet
fix: fixes dog fashion items with no speech modifiers set making dressed
up corgis unable to perform their speech or emote behaviors
fix: fixes old Ian losing his mobility ride when shaved with a razor
fix: fixes pets not dropping their collar when gibbed
fix: butter don't go on Lisa and corgi puppies (Lisa won't wear hats and
corgi puppies can't wear hats and back slot items)
/:cl:

---
## [jacgoudsmit/Steve](https://github.com/jacgoudsmit/Steve)@[0807e507f8...](https://github.com/jacgoudsmit/Steve/commit/0807e507f88cf8f1a5a0c9a5a216d95e65391296)
#### Thursday 2023-07-27 19:21:13 by Jac Goudsmit

Added source code for the library

Steve was born in a fork of the CrystalFontz/CFA10099 repo. I noticed that the CrystalFontz / FTDI / Bridgetek sample code depended on #defines a little too much to my liking. This made it difficult to read through the code and figure out what each macro was for. Also, it made the code type-unsafe: it would be easy to put totally the wrong value into a command or register by mistake, making a program fail silently (without a warning or error from the compiler). Furthermore, I noticed that the macros made it necessary to re-compile the entire source code for every single display, because display parameters (such as width and height) were defined in macros too. Another thing that bothered me a little was that the sample code was Arduino specific.

This inspired me to write a C++ class with code to support the EVE display chips, that fixes those problems. I called it Static Type-safe EVE because the resulting acronym is also a running joke in my family.
* All the "magic values" that are intended for a specific purpose, are declared as enums, for type safety.
* All the values that are specific to a display are stored in a Display Profile class called SteveDisplay. For many displays, an instance of the display class can be created to represent the parameters of the display. For more complicated displays, a subclass can be created with a constructor that changes some parameters from the default.
* The way that the host communicates with the EVE chip is implemented in SteveHAL. For example, when used with Arduino, a program can use the SteveHAL_Arduino class with uses the SPI.h module. If necessary, variations can be created that use QSPI or higher SPI clock frequencies. For other platforms such as Windows with an FTDI 4222H, other HALs can be created.
* At the time of this writing, touch screen code is not implemented yet, but will be added soon. This will be implemented in a separate class, possibly multiple classes depending on which type of touch screen controller is in use. If you don't need touch screen functionality, it won't need to be in your project.
* At the time of this writing, audio is not implemented yet, but will be added soon. This may also be implemented as a separate class.

---
## [RastiWasi/IntroductiontoDataScince](https://github.com/RastiWasi/IntroductiontoDataScince)@[9ae58c646d...](https://github.com/RastiWasi/IntroductiontoDataScince/commit/9ae58c646d162beaea9f28fac892c6d81f841f33)
#### Thursday 2023-07-27 19:38:39 by RastiWasi

Add files via upload

#Assignment: Are Females Bad at Driving, if yes, then how can we improve it, if no, then why do most people have this misconception and what factors contributes?

The assignment aims to prove whether females are Bad at driving; if yes, then how can we improve it; if no, then why do most people have this misconception, and what factors contribute to using data science methodologies? The assignment explores objective evidence, analyzes statistical data, and investigates contributing factors to provide a comprehensive and data-driven perspective on the topic.
##Introduction
This assignment aims to challenge the stereotype that females are bad drivers using data science methodologies. It explores the societal impact of this misconception, the challenges faced by female drivers, and the psychological effects of stereotypes. Through data collection, preprocessing, and analysis, we seek to present objective evidence that dispels the unfounded belief.

##Exploring the Misconception
This section delves into the harmful impact of the stereotype on society, highlighting the challenges and biases faced by female drivers. It sets the stage for the data-driven analysis that follows, emphasizing the importance of data-based conclusions.

##Data Collection and Preprocessing
The process of collecting relevant data on driving skills, accident rates, traffic violations, and other variables is described in this section. Preprocessing steps, such as cleaning and formatting the data, are detailed to ensure it is ready for rigorous analysis.

##Data Analysis and Methodology
This section outlines the data science methodologies employed to analyze the collected data. Statistical techniques, machine learning models, and other analytical methods are discussed to evaluate driving skills based on gender. Assumptions, limitations, and biases associated with the analysis are also addressed.

##Results and Findings
Presenting the results of the data analysis, this section uses visualizations, charts, and tables to illustrate the findings. Any observed patterns, trends, or differences in driving skills between genders are backed by statistical evidence and data science techniques.

##Discussion and Interpretation
The results are interpreted and discussed within the context of the prevailing stereotype. Possible explanations for observed differences are explored, and the significance of findings is evaluated by comparing them with existing literature and research in data science. Informed discussions foster a nuanced understanding of the data.

##Overcoming Stereotypes
This section focuses on strategies to challenge and address biases associated with the stereotype. The role of education, awareness campaigns, and inclusive policies in promoting gender equality in driving is discussed, bolstered by insights from the data analysis.

##Empowering Females
Highlighting the achievements and successes of female drivers, this section emphasizes representation, equal opportunities, and supportive measures. Inspiring stories and initiatives that empower female drivers are showcased, supported by data insights that emphasize the need for diversity and inclusivity.

##Conclusion
In conclusion, the data-driven analysis demonstrates that the stereotype of females being bad drivers is baseless and unfair. Driving skills are not determined by gender, but rather by individual factors such as experience, training, and attentiveness. Promoting equality, challenging stereotypes, and appreciating individual talents is essential in fostering an inclusive society.

##Additional Resources
The Additional Resources section provides recommendations for further reading, encouraging continued exploration of the topic using data science methodologies. Scholarly articles, statistical data sources, and research papers offer valuable insights and support continued research.

##Acknowledgments
This section acknowledges the contributions of researchers, authors, and data sources that have informed the assignment. Their valuable insights have played a crucial role in advancing data-driven analysis.

##License
The License section states the licensing terms for the assignment and any accompanying code or data. It provides information on sharing, usage, and adaptation, ensuring appropriate credit is given to the original source.

##Theoretical Explanation
Understanding the Stereotype: The stereotype that females are bad drivers has persisted through jokes, media portrayals, and anecdotal experiences. This belief is unfounded and rooted in biases and misconceptions, perpetuating discrimination and hindering progress toward gender equality.

###The Reality: Driving skills are not determined by gender but by individual experiences, training, and personal characteristics. Numerous studies have debunked the notion that women are worse drivers. Factors like aggressive driving and impaired driving are stronger predictors of accidents than gender.

###Promoting Equality and Objectivity: Developers have a responsibility to foster an inclusive community. By challenging stereotypes and promoting objectivity, we contribute to an environment that values individuals based on their skills and accomplishments rather than arbitrary characteristics.

###Encouraging Equal Opportunities: Let's promote equal opportunities and support everyone to excel, regardless of gender. Embracing diversity brings unique perspectives that enhance progress and innovation. Recognizing achievements from all backgrounds is essential for inclusivity.

###Conclusion: The stereotype that women are bad drivers is baseless and unfair. Let's appreciate individual talents and skills, fostering equality, respect, and inclusivity in the tech community and beyond.

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[3d225e5ccb...](https://github.com/git-for-windows/git/commit/3d225e5ccb185fc259b34ae4782a5c73852970ea)
#### Thursday 2023-07-27 22:50:55 by Johannes Schindelin

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

