## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-05-07](docs/good-messages/2022/2022-05-07.md)


1,519,311 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,519,311 were push events containing 2,275,109 commit messages that amount to 123,566,315 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 44 messages:


## [AnmolS1/SpamStudy](https://github.com/AnmolS1/SpamStudy)@[7f4fd6b22b...](https://github.com/AnmolS1/SpamStudy/commit/7f4fd6b22b6e8872fabcffd280e4a08ee48788dc)
#### Saturday 2022-05-07 00:00:10 by Anmol Saxena

more done

finished tidying the data, it's practically ready to upload to the cloud. i'll make changes based on whatever dr. munyaka wants tomorrow. final step is uploading the data to the ibm database. honestly this was incredible. i haven't slept since sunday night (it's wednesday morning now), and i've hardly eaten. it's just been pushing and pushing to get this done before monday next week, and it looks like i just might be able to do this And get all my other work done. props to me lol.

---
## [by22dgb/autotrimps3](https://github.com/by22dgb/autotrimps3)@[f7b39ffdb5...](https://github.com/by22dgb/autotrimps3/commit/f7b39ffdb51d3a4ae1748556e0767ccd67539602)
#### Saturday 2022-05-07 00:18:41 by SadAugust

Fixing bugs and adding universe selection feature

Heyy, I made a few modification to graphs for my AT fork and figured I might as well share since it fixes a few bugs that I've at least been annoyed by quite a bit. If you want to test it out first to make sure it's all working you can test it on https://SadAugust.github.io/AutoTrimps_Local. Changed I've made are listed below, I've only done minimal testing but haven't found any issues with it.

Removed minified version of code to make it readable

Added option to select Universe which will visibility of U1 and U2 graphs depending on the selection. Reduces a ton of unnecessary settings from cluttering the list and figured I'd make it easier to expand for if we do get more universes.

Remembers graph selection when reloading the page instead of defaulting to helium/radon per hour

Hides portals from other universes showing so if U2 graphs are being looked at you won't see U1 portals in the sidebar, should fix bugs like void maps being unreadable when there's a significant difference in portals between the 2 universes.

Fixed it not drawing graphs properly when reopening Graphs after the initial load as it was a nuisance having to go to another graph and back to get it to display anything.

---
## [Loathing-Associates-Scripting-Society/TourGuide](https://github.com/Loathing-Associates-Scripting-Society/TourGuide)@[54adb80bd1...](https://github.com/Loathing-Associates-Scripting-Society/TourGuide/commit/54adb80bd100c4da91d793641c1d9382d70cffb7)
#### Saturday 2022-05-07 00:41:10 by Aaron McGuire

Merge pull request #43 from Loathing-Associates-Scripting-Society/removeUsedOptions

okay i am pushing a new release (finally). i am pushing version to 2.0.0 because we've added a shitload of changes since the last version push. this version includes:

- fixes for several option availability glitches in grey you
- a tile for the unbreakable umbrella
- a new option that lets you be more facestabby w/ bowling ball

specifically, if you run `set tourGuideBowlingBallSupernag=true;` in the CLI, there will be an alert that floats on top of tourguide reminding you that your bowling ball is un-thrown until you throw it. it will not happen unless you set that option though, so most users will not see it.

happy speedrunning folks!

---
## [KuzscoTech/NGCP_Embedded_SDK](https://github.com/KuzscoTech/NGCP_Embedded_SDK)@[bad9edb9b1...](https://github.com/KuzscoTech/NGCP_Embedded_SDK/commit/bad9edb9b117a47befae8308a236d2d0358fb022)
#### Saturday 2022-05-07 00:43:47 by George Yu

stupid fucking bullshit doesnt fucking work fuck shit stupid piece of fucking shit

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[0504c0a2b4...](https://github.com/tgstation/tgstation/commit/0504c0a2b466d617efd4dcc77b092fcdbdad24be)
#### Saturday 2022-05-07 00:52:49 by LemonInTheDark

Improper forced qdel cleanup,  some expanded del all verbs (#66595)

* Removes all supurfolus uses of QDEL_HINT_LETMELIVE

This define exists to allow abstract, sturucturally important things to
opt out of being qdeleted.
It does not exist to be a "Immune to everything" get out of jail free
card.
We have systems for this, and it's not appropriate here.

This change is inherently breaking, because things might be improperly
qdeling these things. Those issues will need to be resolved in future,
as they pop up

* Changes all needless uses of COMSIG_PARENT_PREQDELETED

It exists for things that want to block the qdel. If that's not you,
don't use it

* Adds force and hard del verbs, for chip and break glass cases
respectively

The harddel verb comes with two options before it's run, to let you
tailor it to your level of fucked

* Damn you nova

Adds proper parent returns instead of . = ..()

Co-authored-by: Seth Scherer <supernovaa41@gmx.com>

* Ensures immortality talismans cannot delete their human if something goes fuckey. Thanks ath/oro for pointing this out

Co-authored-by: Seth Scherer <supernovaa41@gmx.com>

---
## [Imaginos16/tgstation](https://github.com/Imaginos16/tgstation)@[ce1bdb0205...](https://github.com/Imaginos16/tgstation/commit/ce1bdb0205e1428fccff7c81cb67cb3d0a68f1a3)
#### Saturday 2022-05-07 01:07:38 by itseasytosee

Stops floating mobs from being affected by slowndown bulky_drag and human_carry (#66610)

Put simply, removes the slowdown from pulling bulky items as well and fireman carrying (and piggyback rides) while in zero gravity.

This also fixes some weirdness, like how slowdowns from aggressive grabs are negated in zero g, but because bulky_drag is NOT negated, you can still be slowdown in zero gravity if your target is laying down. or in a neck grab or higher because they are then automatically floored. Which makes zero consistant sense given the context.

Also, while testing this, I noticed that it was faster to drift while pulling a bulky object in space rather than fly with a jetpack because of the  slowdown and how drifting works, which also makes no god damn sense. This should fix that too.

Fixes the consistency errors mentioned above, also adds an interesting change of game state in zero gravity which seems fun. (see: faster to drag away downed friendlies during a space battle, or perhaps kidnap a downed enemy)

Fixes #62600 (aggressively grabbing a body in space makes you move faster than passively grabbing them)


You can now pull bulky things in zero gravity at full speed
The slowdown from neck grabs is now properly negated in zero gravity.

---
## [Sonic121x/Skyrat-tg](https://github.com/Sonic121x/Skyrat-tg)@[f6ce903dea...](https://github.com/Sonic121x/Skyrat-tg/commit/f6ce903deade160357e23b927d376851f0dbdd2c)
#### Saturday 2022-05-07 01:18:25 by SkyratBot

[MIRROR] Makes glass floors override platings. Fixes glass floor openspace bug. [MDB IGNORE] (#13226)

* Makes glass floors override platings. Fixes glass floor openspace bug. (#66301)

About The Pull Request

Fixes #63868. Actual one liner fix for this one here. If this pr dies feel free to atomize this one.
AND it turns out to not be tim's fault.

Fixes #63548. But i really shouldnt say fixed. The original implementation was causing the invincible plating bug. When tim's refactor got in it instead relies on the element state, which was broken from the get go, removing the invincible plating bug which was in a sense "intended" its all messy man I hate this code. Thats why im removing the plating thing. Let the turf handle the turf change themselves this complicates things.

Mapped in glass floors have openspace (now baseturf bottom) as their baseturfs, while built ones have plating under them. Which doesnt make sense to be honest. Why would things be visible if a plating is under the glass. They are also crowbarrable on top of this, which to be fair is my main reasoning behind the PR.

To solve this, I am instead making glass floors replace the plating instead of building over it. This is made to be generalizable for every tile in game, as long as their initial baseturf is the same and the tile wants it to happen.

do after of three seconds is completely arbitrary. If any maint want it changed let me know.
Why It's Good For The Game

First one solves a bug
Second one makes more sense
And er, icebox is currently using the glass floors in sec, they can be crowbarred very easily. This might be a good idea from a gameplay perspective.
Changelog

cl
del: Removed adding glass floors to plating
balance: Allows you to replace plating with glass floors instead. 3 second timer.
del: Removed deconstructing the glass floors. No replacement for this one, use a rcd.
fix: Fixed metastation glassfloor spawning a weird turf when crowbarred.
/cl

* Makes glass floors override platings. Fixes glass floor openspace bug.

Co-authored-by: vincentiusvin <54709710+vincentiusvin@users.noreply.github.com>

---
## [jeffday/dayzserver](https://github.com/jeffday/dayzserver)@[04a981be50...](https://github.com/jeffday/dayzserver/commit/04a981be50c3eef3ff3df18e0496bae6cfa3aacf)
#### Saturday 2022-05-07 02:18:31 by Jeff Day

jesus christ i am a fucking idiot i was looking at an unrelated types file, the one included with the damn mod is fine

---
## [nikhilsoni1/sample_microservice](https://github.com/nikhilsoni1/sample_microservice)@[eab3524437...](https://github.com/nikhilsoni1/sample_microservice/commit/eab35244376a1d73d2f5de005a652294000fea80)
#### Saturday 2022-05-07 02:20:18 by nikhilsonilctwn

deleted all files from Sonu Sharma's tutorial (too fucking weird), moved on to Paurakh Sharma - https://dev.to/paurakhsharma/microservice-in-python-using-fastapi-24cc. Both the tutorials are by Sharmas, are they brothers? I guess that mystery can be solved but not worth solving

---
## [timothymtorres/tgstation](https://github.com/timothymtorres/tgstation)@[27946f516d...](https://github.com/timothymtorres/tgstation/commit/27946f516dd77faa071576499bb700c6fa22fbab)
#### Saturday 2022-05-07 02:21:18 by san7890

Update Comments and Adjusts Incorrect Variables for Map Defines and Map Config (#66540)

Hey there,

These comments were really showing their age, and they gave the false impression that nothing had changed (there was a fucking City of Cogs mention in this comment!). I rewrote a bit of that, and included a blurb about using the in-game verb for Z-Levels so people don't get the wrong impressions of this quick-reference comment (they always do).

I also snooped around map_config.dm and I found some irregularities and rewrote the comments there to be a bit more readable (in my opinion). Do tell me if I'm a cringe bastard for writing what I did.

Also, we were using the Box whiteship/emergency shuttle if we were missing the MetaStation JSON. Whoops, let's make sure that's fixed.

People won't have to wander in #coding-general/#mapping-general asking "WHAT Z-LEVEL IS X ON???". It's now here for quick reference, as well as a long-winded section on why you shouldn't trust said quick reference.

---
## [itShirb/shirb.dev](https://github.com/itShirb/shirb.dev)@[dc8d6c6f14...](https://github.com/itShirb/shirb.dev/commit/dc8d6c6f14e713fed7a6031a9f7b5e220f43abe7)
#### Saturday 2022-05-07 02:23:20 by itShirb

HOLY SHIT IM RETARDED AS FUCK I DIDN'T MAKE IT ASYNC AIHILAGJKLGJS

---
## [k21971/EvilHack](https://github.com/k21971/EvilHack)@[63a7b41c92...](https://github.com/k21971/EvilHack/commit/63a7b41c9267b1fef2cffe3b31159f5aedd03b13)
#### Saturday 2022-05-07 04:00:34 by k21971

Fix: enchant armor selection and dragon scales; wishing for dragon scale mail.

A couple fixes that revolves around dragon scales:

1) Before dtsund-DSM was implemented, players had the option to select
which piece of armor to enchant if multiple pieces were worn, which is a
nice 'quality of life' feature. The dtsund implementation had it so that
if scales were worn, it bypassed any selection and focused the
enchantment on it alone. This caused a number of issues, especially if
the player already had dragon-scaled armor and were wearing another set
of scales as a cloak. This commit effectively gets rid of the bypass.

2) Another quirk of dtsund-DSM - wishing up '<foo> dragon scale mail'
would produce nothing. Twice now, I've watched players not aware or
not familiar with dtsund-DSM try to wish up dragon scale mail and burn a
number of wishes trying to get it, only to wind up with nothing. They
thought they had misspelled the wish or something. Frustrating as hell
to say the least. Now, if the player wishes for '<foo> dragon scale
mail', they'll receive 'a set of <foo> dragon scales' instead. They may
still be a bit confused if they're unaware of the dtsund changes, but at
least they'll pretty much get what they wished for. This will catch the
muscle memory wishes as well for those who know about dtsund-DSM and
just forgot/are on autopilot.

---
## [TheUnholyWrath/oaa](https://github.com/TheUnholyWrath/oaa)@[841368b6b0...](https://github.com/TheUnholyWrath/oaa/commit/841368b6b064c700c6194d8e46d798e0d4494ed1)
#### Saturday 2022-05-07 04:09:13 by Darko V

Modifiers changes (May 2022) (#3351)

* Cycled Out modifiers: Hyper Lifesteal, Blood Magic, Healer and Brute.
* Randomize button will no longer randomize the 'None' option.
* Buffed Timeless Relic modifier from 25% to 30%.
* Telescope modifier now also provides 400 bonus vision (day/night).
* Fixed Telescope modifier cast range bonus not stacking with other cast range bonuses.
* Fixed Creed of Omniscience and Telescope neutral items cast range bonuses not stacking with Octarine Core or Far Sight cast range bonuses.
* Random Draft number of banned heroes increased from 70 to 75.
1) Added Aghanim, Nimble and Sorcerer modifiers.
2) Updated tooltip for Wisdom modifier.
3) Bonus AoE/Radius modifier now ignores:
- Arc Warden Flux search radius
- Drow Ranger agility range penalty
- Monkey King Wukong's Command
- Phantom Assassin Blur
- Spectre Desolate
4) Bonus AoE/Radius now improves Sohei's Dash width.
5) Diarrhetic auto-poop-ward check-for-wards-radius increased from 200 to 300. This means auto-pooped wards will be farther from each other.
6) Explosive Death modifier will now proc on Tempest Doubles and heroes that are reincarnating.
7) Attack Range Switch modifier bonus attack range reduced from 600 to 500.
8) Attack Range Switch modifier bonus projectile speed increased from 900 to 1100.
9) Added Max Power modifier
10) Fixed tooltip for modifiers saying undefined when 'Random' option is selected.

---
## [WillNilges/letmein2](https://github.com/WillNilges/letmein2)@[e2c40a1304...](https://github.com/WillNilges/letmein2/commit/e2c40a13042851402935e0ad36a2ab490c386d05)
#### Saturday 2022-05-07 04:22:40 by Will Nilges

Oh god I totally fucked up the CAD file

I really ought to re-do it in a less stupid way.

---
## [WillNilges/letmein2](https://github.com/WillNilges/letmein2)@[e90b5b1ae1...](https://github.com/WillNilges/letmein2/commit/e90b5b1ae1ff19bb49babf43c12777f88f726f60)
#### Saturday 2022-05-07 04:22:40 by Will Nilges

Beeg refactor

Move a lot of shit out of the global scope, into the main function, and
also break out a lot of shit into a class. I tried to move the MQTT
stuff but it got mad when I did that. I'd like to see if that can move,
but not sure if it's a big deal.

I'm sure I violated a ton of Python design patterns because I'm stupid.
Enjoy.

---
## [byz7day/rathena_webservice](https://github.com/byz7day/rathena_webservice)@[d617d9f083...](https://github.com/byz7day/rathena_webservice/commit/d617d9f08381442b14cb69da6ef5251a12817cd3)
#### Saturday 2022-05-07 04:37:28 by Aleos

Updates SC_CHANGEUNDEAD behavior (#6867)

* Fixes #6834.
* Versus Players
- Animation will be properly displayed for Blessing/Increase Agility when the target has Change Undead active (buffs are not applied even though animation is displayed).
- Target can no longer be killed through the single damage applied by Blessing/Increase Agility and Change Undead.
- If the target has Curse and Stone active, only Curse is removed by Blessing first (buffs are not applied).
- Shadow or Undead armor have no impact on Blessing or Increase Agility at all.
* Versus Monsters
- Blessing is applied normally to the target as long as it's not an Undead element or Demon race.
- Blessing does not cancel out Curse or Stone.
Thanks to @Playtester!

---
## [null2264/dotfiles](https://github.com/null2264/dotfiles)@[e5ba0534aa...](https://github.com/null2264/dotfiles/commit/e5ba0534aadda1b5ec05665badf927e335a5e6e1)
#### Saturday 2022-05-07 06:35:06 by ziro

+ FUCKING GOOGLE AND THEIR SHITTY FUCKING SOFTWARE
ANDROID_SDK_HOME is deprecated so i removed it, now AVD won't launch
apparently i can use ANDROID_PREFS_ROOT! so much pain just to fix this
one fucking software, as expected from software managed by Google

---
## [Shahars71/OOP-Y1S2-project](https://github.com/Shahars71/OOP-Y1S2-project)@[43aa6b6cc9...](https://github.com/Shahars71/OOP-Y1S2-project/commit/43aa6b6cc98036c080d41921e3cb4e73ae64d229)
#### Saturday 2022-05-07 06:58:50 by Shahars71

Just rewrote the entire fucking game. Why must pointers make me suffer?

Polymorphism is just at the tippy tip of my god damn fingers.

---
## [ImSynthex/Skyrat-Code-Moment](https://github.com/ImSynthex/Skyrat-Code-Moment)@[c2a88900c6...](https://github.com/ImSynthex/Skyrat-Code-Moment/commit/c2a88900c67fe6db78c3e17631270c05be14d9af)
#### Saturday 2022-05-07 07:16:47 by SkyratBot

[MIRROR] Updates The Derelict to some modern standards, also some turf edits [MDB IGNORE] (#12859)

* Updates The Derelict to some modern standards, also some turf edits (#66045)

Brings The Derelict up to speed with some of our new mapping tools and stuff.
This also places nearstation turf in certain areas, as well as general turf clean up.
Also cleans up the absurdly placed black holes of light that were over space tiles.
Girder/Grill spawners were placed in certain locations (mostly on external girlls).
I also remapped the main AI chambers SMES power to not go through the fucking wall, as a trade off, its no longer wired round start, and the two pieces of cable that are automatically in the room have been swapped out for two (2) five cables each. Its not enough to reach the main area, but god fuck wires running through walls.

As an aside, some of plating on the outside, walls include, does look weird being full bright like this. I'm neutral for the most part. Theres a weird fine balance that needs to be maintained with some of the areas being open to space, I've opted to keep lattice as nearstation and any thing plating and above as turfed (excluding plating that is solely in space).

I'll be redoing the turfs of this later, sprite wise.

Images

* Updates The Derelict to some modern standards, also some turf edits

Co-authored-by: Jolly <70232195+Jolly-66@users.noreply.github.com>

---
## [PhantomEpicness/cmss13-design-docs](https://github.com/PhantomEpicness/cmss13-design-docs)@[2dc78c4391...](https://github.com/PhantomEpicness/cmss13-design-docs/commit/2dc78c4391e2fe20ab9b6cef1e1cd0b4a196c5ea)
#### Saturday 2022-05-07 07:56:01 by Bigboyyo

I'm so sick of things preventing me from getting this merged holy fuck

---
## [Camille-Claudel/depaumeur](https://github.com/Camille-Claudel/depaumeur)@[13b6cd460d...](https://github.com/Camille-Claudel/depaumeur/commit/13b6cd460db8b3045cd31888c48d3f2ea73d89de)
#### Saturday 2022-05-07 10:22:56 by Remi Mazhar

Created UnitTests project

created a method to test calibration points, it's kind of a test of test, like i wanted to test how unit tests work
yeah fuck you, recursive testing

---
## [Ujjwal2017099/CodeForces](https://github.com/Ujjwal2017099/CodeForces)@[65e6d1cb21...](https://github.com/Ujjwal2017099/CodeForces/commit/65e6d1cb21068d10237296c7ae5a8e175f51f0b2)
#### Saturday 2022-05-07 10:53:29 by Ujjwal2017099

Detective Task - 1675C

Polycarp bought a new expensive painting and decided to show it to his n friends. He hung it in his room. n of his friends entered and exited there one by one. At one moment there was no more than one person in the room. In other words, the first friend entered and left first, then the second, and so on.

It is known that at the beginning (before visiting friends) a picture hung in the room. At the end (after the n-th friend) it turned out that it disappeared. At what exact moment it disappeared — there is no information.

Polycarp asked his friends one by one. He asked each one if there was a picture when he entered the room. Each friend answered one of three:

no (response encoded with 0);
yes (response encoded as 1);
can't remember (response is encoded with ?).
Everyone except the thief either doesn't remember or told the truth. The thief can say anything (any of the three options).

Polycarp cannot understand who the thief is. He asks you to find out the number of those who can be considered a thief according to the answers.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[3983ae5d8e...](https://github.com/mrakgr/The-Spiral-Language/commit/3983ae5d8e4518d71b40db1fbd924297687b9d38)
#### Saturday 2022-05-07 11:08:19 by Marko Grdinić

"9:20am. Let me chill a bit and then I will start.

9:40am. Let me start. I've made my resolve.

https://www.youtube.com/watch?v=04TCID4cDBo
Easy Guide to HardOPS and Boxcutter for Beginners - Part 1 - Blender Tutorial

Instead of watching anime as I should, I watched this yesterday. The main obstacle before me is not necessarily anything complicated - I simply have to get used to these plugins. I saw them being used before, but that is not enough to properly internalize them. I should just play with them for a bit and it will come to me. Yesterday's failure will serve as motivation to get better today.

9:45am. Focus me. I need to remind myself that my goal is to get to 3/5 rather than 5/5 so I can be excused for not knowing some things about 3d. For 3/5 Blender will be enough. If I keep pushing I should be able to reach this in a few months time. So that is why I should.

Just a bit more and then I can start grinding 2d and music.

9:45am. Let me watch it again. It was past 10pm yesterday so I did not get the chance to properly focus.

https://youtu.be/kIupMZgE5qc
HARDENED normals vs WEIGHTED normals in Blender - which one to use?

Let me watch this.

10:15am. So harden normals just puts sharp after the bevel is done. Ok, good.

Let me watch what I should be watching.

https://youtu.be/04TCID4cDBo?t=564

I figured out how to do immutable bevels on individual edges using vertex groups. Blender really needs edge groups badly though.

11:15am. Holy shit, Youtube is putting in ads that I can't skip!

What the hell happened? Shouldn't ublock deal with this?

Ok, it seems I can skip them after 5s.

https://helpdeskgeek.com/help-desk/ublock-origin-not-blocking-youtube-and-twitch-ads-11-ways-to-fix/

12:45pm. https://youtu.be/ftqaEZjMXJc
PRO RENDER gone bad?

https://youtu.be/pHpTSLZKIC4
Hard Surface Tutorial for Blender - BOOLEAN to SUBD Workflow.

https://youtu.be/4scXty1hsto
Knife Tool Tutorial for Blender 3.0

There doesn't seem to be a part 3, but I think I know enough at this point to try the rig again.

12:50pm. https://youtu.be/ftqaEZjMXJc?t=187
> At first glance you probably don't see what the hell I am talking about, but basically this is absolute, fucking garbage.

1:05pm. Let me stop here for a bit. Time for breakfast."

---
## [Kepixbro/Kepixbro](https://github.com/Kepixbro/Kepixbro)@[06d13dc9b2...](https://github.com/Kepixbro/Kepixbro/commit/06d13dc9b2fe021f923e2329f68f5a467cb1b9b4)
#### Saturday 2022-05-07 11:23:32 by Kepixbro

My own Malware/joke

Has been updated more and has more features And if you got anything to ask me u can its still in progress i guess
btw its not harmful it only a joke malware but it does shutdown ur pc and make txt files
but yeah thats it, i am sorry if this is poorly written.

---
## [evanonline/Dynamic-Pokemon-Expansion-Hisui-Update](https://github.com/evanonline/Dynamic-Pokemon-Expansion-Hisui-Update)@[3dd2cde0b8...](https://github.com/evanonline/Dynamic-Pokemon-Expansion-Hisui-Update/commit/3dd2cde0b84a61e1aa16d227dc2a2c49833b70f7)
#### Saturday 2022-05-07 12:03:22 by evanonline

Gender dimorphism confirmed.

This update adds all of the various minute gender dimorphism instances - 93 Pokemon now properly have different male or female sprites on top of the pre-existing differences set up for Pyroar, Hippopotas, Hippowdon, Unfezant, Frillish and Jellicent. This includes Hisuian Sneasel.

Some notes:
-My understanding is that the entries in Evolution Table.c for female Hippopotas and Frillish to evolve into female Hippowdon and Jellicent are non-essential placeholders. As such, I didn't go to the trouble of adding placeholders for the new dimorphic sprites. Honestly - I'm not sure much of what I've added is essential to get this working aside from defining the sprites in the Back Pic, Front Pic and Icon tables and adding them all to updated_code.c, but I wanted to be thorough to make sure it all lines up with the existing gender differences in DPE.

-For the icon sprites, you may notice that there are only a few added. In mainline Pokemon, gender differences tend not to be reflected in the icon sprites, but I did a few that I felt were particularly notable. This was also something of a space-saving measure. I think some of the sprite definitions could be a little more efficient, particularly the back sprites - not every Pokemon's gender differences are visible in the back, so the existing male sprites could have perhaps been pointed to instead of adding new, redundant graphics. Doing it this way was honestly just easier to keep track of, though.

---
## [Aruato/moob](https://github.com/Aruato/moob)@[5c2bae1ad3...](https://github.com/Aruato/moob/commit/5c2bae1ad3c2f2d88e7a46e50e3816a7a22504f8)
#### Saturday 2022-05-07 13:50:05 by Peter Zijlstra

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

---
## [gokulkgm/device_xiaomi_alioth](https://github.com/gokulkgm/device_xiaomi_alioth)@[e255e30a3b...](https://github.com/gokulkgm/device_xiaomi_alioth/commit/e255e30a3bf0e40636e35a5770f9582cc610a1e7)
#### Saturday 2022-05-07 14:00:54 by Omkar Chandorkar

fuck you xiaomi

Signed-off-by: Omkar Chandorkar <gotenksIN@aosip.dev>

---
## [larauwuowo/furrytailholeuwu](https://github.com/larauwuowo/furrytailholeuwu)@[cee687cb70...](https://github.com/larauwuowo/furrytailholeuwu/commit/cee687cb707da7cea2b9d6df0e5688e55c4259bc)
#### Saturday 2022-05-07 14:02:13 by meow

added more sex fucking sex fuck fuck i love sex so much SEEEEEEEEEEXX YIFFY BALLS MILKY COCKS MMMMMM SEX DONUT ASS SEEEEX!!!!!!!!!

---
## [tannerhelland/PhotoDemon](https://github.com/tannerhelland/PhotoDemon)@[9dea56340e...](https://github.com/tannerhelland/PhotoDemon/commit/9dea56340e82e33d43d27621b6dd9d8498979d98)
#### Saturday 2022-05-07 14:25:09 by Tanner

First draft of `Edit > Content-Aware Fill` tool

Holy shit, friends - this actually works.  I'm honestly a little (okay a LOT) astonished to see the functional content-aware fill behavior in action, because part of me thought this was never going to work in a reasonably good way.

But it works, and it works *well*.  Like, this will be a tool that people actually use!

There's a ton of clean-up and refinement left to do (and I still need to build a UI) but that's easy-peasy compared to just getting the damn algorithm working in the first place.

---
## [tannerhelland/PhotoDemon](https://github.com/tannerhelland/PhotoDemon)@[bcc4e689ee...](https://github.com/tannerhelland/PhotoDemon/commit/bcc4e689eea716a315f8f88871511c4ef386f05c)
#### Saturday 2022-05-07 14:25:09 by Tanner

pdInpaint: a new solution for content-aware fill

Photoshop has a borderline-magical feature called "content-aware fill":

https://helpx.adobe.com/photoshop/using/content-aware-fill.html

I want something similar for PhotoDemon, so here we gooooooo!

The best reference I've seen on texture synthesis (which is what content-aware fill does - it attempts to "synthesize" a new "texture" that can be used to seamlessly "fill" over the top of an unwanted object) is Paul Harrison's PhD Thesis, "Image Texture Tools: Texture Synthesis, Texture Transfer, and Plausible Restoration":

https://www.logarithmic.net/pfh-files/thesis/dissertation.pdf

Using the concepts from his thesis, Paul would go on to release the "Resynthesize" plugin that provides content-aware fill in GIMP.  Resynthesize is still available as a GIMP plugin, but unfortunately it is under a new maintainer now and it is very challenging to build for Windows (and the source code is GPL anyway, so I can't use it in PhotoDemon even if I wanted to).

Fortunately, Paul's thesis is very comprehensive.  He lays out pretty much everything you need to consider when writing a texture synthesizer, and he cites many other author's takes on the topic (which are also useful references, with good ideas to be taken from all).

From these various references, I have now completed my first draft of a texture synthesizer for PhotoDemon.  This first draft is not actually a content-aware fill tool - that will come later - but it *is* a seamless tile generator, which provides a simple test ground for the underlying algorithm.  Basically, given an input image, the code tries to construct a novel output image that is capable of seamless tiling, using only pixel data from the original image as its reference.  From this, it's easy to study how the algorithm handles complexity and sampling, and whether it's capable of generating representative textures from a variety of inputs.

As it stands today, this code is slow, but it works well - very well, even - and I'm now at a stage where I comfortable committing it so I have a good backup reference before I start writing a UI for it.  (A UI is needed for further testing, since there are a number of parameters you can toggle to trade-off between quality and performance, and I need to ensure PD's algorithm works well across the entire spectrum.)

I don't have an ETA for final merge into PD, but it shouldn't be long - I'm thinking a measurement in days possibly weeks, not months.

---
## [llvm/llvm-project](https://github.com/llvm/llvm-project)@[c2c259224b...](https://github.com/llvm/llvm-project/commit/c2c259224bb30b089206dd69dc44aefddffec2f4)
#### Saturday 2022-05-07 14:41:00 by Amaury Séchet

const char* for LLVMTargetMachineEmitToFile's argument

The `LLVMTargetMachineEmitToFile` takes a `char* Filename` right now, but it doesn't modify it.
This is annoying to use in the case where you want to pass a const string, because you either have to remove the const, or copy it somewhere else and pass that. Either way, it's not very nice.

I added a const and clang formatted it. This shouldn't break any ABI in my opinion.
I'm sorry but I didn't know whom to put as reviewer for this, so I chose someone with a lot of commits from the .cpp file.

Reviewed By: deadalnix

Differential Revision: https://reviews.llvm.org/D124453

---
## [Lambda-13/Civ13](https://github.com/Lambda-13/Civ13)@[20b320a949...](https://github.com/Lambda-13/Civ13/commit/20b320a949e6bd50e25ec505df3023405ce90dd6)
#### Saturday 2022-05-07 15:34:52 by savethetreez

Adds missing conflicted icons

Fuck you again, Odisurin!

---
## [newstools/2022-express](https://github.com/newstools/2022-express)@[243165adbc...](https://github.com/newstools/2022-express/commit/243165adbcd5337b936cf5730aa01005dba866f1)
#### Saturday 2022-05-07 17:06:09 by Billy Einkamerer

Created Text For URL [www.express.co.uk/celebrity-news/1606372/Danni-Menzies-boyfriend-soldier-relationship-love-life-A-Place-In-The-Sun-news-latest]

---
## [Little-W/android_kernel_xiaomi_alioth](https://github.com/Little-W/android_kernel_xiaomi_alioth)@[d7a707647f...](https://github.com/Little-W/android_kernel_xiaomi_alioth/commit/d7a707647ff8f1f13ad87698a43fc7710f90a7cf)
#### Saturday 2022-05-07 17:17:55 by George Spelvin

lib/sort: make swap functions more generic

Patch series "lib/sort & lib/list_sort: faster and smaller", v2.

Because CONFIG_RETPOLINE has made indirect calls much more expensive, I
thought I'd try to reduce the number made by the library sort functions.

The first three patches apply to lib/sort.c.

Patch #1 is a simple optimization.  The built-in swap has special cases
for aligned 4- and 8-byte objects.  But those are almost never used;
most calls to sort() work on larger structures, which fall back to the
byte-at-a-time loop.  This generalizes them to aligned *multiples* of 4
and 8 bytes.  (If nothing else, it saves an awful lot of energy by not
thrashing the store buffers as much.)

Patch #2 grabs a juicy piece of low-hanging fruit.  I agree that nice
simple solid heapsort is preferable to more complex algorithms (sorry,
Andrey), but it's possible to implement heapsort with far fewer
comparisons (50% asymptotically, 25-40% reduction for realistic sizes)
than the way it's been done up to now.  And with some care, the code
ends up smaller, as well.  This is the "big win" patch.

Patch #3 adds the same sort of indirect call bypass that has been added
to the net code of late.  The great majority of the callers use the
builtin swap functions, so replace the indirect call to sort_func with a
(highly preditable) series of if() statements.  Rather surprisingly,
this decreased code size, as the swap functions were inlined and their
prologue & epilogue code eliminated.

lib/list_sort.c is a bit trickier, as merge sort is already close to
optimal, and we don't want to introduce triumphs of theory over
practicality like the Ford-Johnson merge-insertion sort.

Patch #4, without changing the algorithm, chops 32% off the code size
and removes the part[MAX_LIST_LENGTH+1] pointer array (and the
corresponding upper limit on efficiently sortable input size).

Patch #5 improves the algorithm.  The previous code is already optimal
for power-of-two (or slightly smaller) size inputs, but when the input
size is just over a power of 2, there's a very unbalanced final merge.

There are, in the literature, several algorithms which solve this, but
they all depend on the "breadth-first" merge order which was replaced by
commit 835cc0c8477f with a more cache-friendly "depth-first" order.
Some hard thinking came up with a depth-first algorithm which defers
merges as little as possible while avoiding bad merges.  This saves
0.2*n compares, averaged over all sizes.

The code size increase is minimal (64 bytes on x86-64, reducing the net
savings to 26%), but the comments expanded significantly to document the
clever algorithm.

TESTING NOTES: I have some ugly user-space benchmarking code which I
used for testing before moving this code into the kernel.  Shout if you
want a copy.

I'm running this code right now, with CONFIG_TEST_SORT and
CONFIG_TEST_LIST_SORT, but I confess I haven't rebooted since the last
round of minor edits to quell checkpatch.  I figure there will be at
least one round of comments and final testing.

This patch (of 5):

Rather than having special-case swap functions for 4- and 8-byte
objects, special-case aligned multiples of 4 or 8 bytes.  This speeds up
most users of sort() by avoiding fallback to the byte copy loop.

Despite what ca96ab859ab4 ("lib/sort: Add 64 bit swap function") claims,
very few users of sort() sort pointers (or pointer-sized objects); most
sort structures containing at least two words.  (E.g.
drivers/acpi/fan.c:acpi_fan_get_fps() sorts an array of 40-byte struct
acpi_fan_fps.)

The functions also got renamed to reflect the fact that they support
multiple words.  In the great tradition of bikeshedding, the names were
by far the most contentious issue during review of this patch series.

x86-64 code size 872 -> 886 bytes (+14)

With feedback from Andy Shevchenko, Rasmus Villemoes and Geert
Uytterhoeven.

Link: http://lkml.kernel.org/r/f24f932df3a7fa1973c1084154f1cea596bcf341.1552704200.git.lkml@sdf.org
Signed-off-by: George Spelvin <lkml@sdf.org>
Acked-by: Andrey Abramov <st5pub@yandex.ru>
Acked-by: Rasmus Villemoes <linux@rasmusvillemoes.dk>
Reviewed-by: Andy Shevchenko <andriy.shevchenko@linux.intel.com>
Cc: Rasmus Villemoes <linux@rasmusvillemoes.dk>
Cc: Geert Uytterhoeven <geert@linux-m68k.org>
Cc: Daniel Wagner <daniel.wagner@siemens.com>
Cc: Don Mullis <don.mullis@gmail.com>
Cc: Dave Chinner <dchinner@redhat.com>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: Yousef Algadri <yusufgadrie@gmail.com>
Signed-off-by: Panchajanya1999 <panchajanya@azure-dev.live>
Signed-off-by: Forenche <prahul2003@gmail.com>
Signed-off-by: Little-W <1405481963@qq.com>

---
## [jimtheflash/betfinder](https://github.com/jimtheflash/betfinder)@[106006c944...](https://github.com/jimtheflash/betfinder/commit/106006c94459b71fee15e2715f088a169c080983)
#### Saturday 2022-05-07 17:19:29 by jimtheflash

update nba player lu with dmelton, and fuck you whichever book did that

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[d979cc18f1...](https://github.com/mrakgr/The-Spiral-Language/commit/d979cc18f10274f7cbabdd6f313ad3114306a19f)
#### Saturday 2022-05-07 17:59:26 by Marko Grdinić

"2:45pm. Let me resume. I think I should have enough to start right now, but let me watch some more.

https://youtu.be/pHpTSLZKIC4?t=354

How does he do this. In fact, this is one of the things I need to put the circle where I need it to be, but it hasn't worked for me.

https://youtu.be/pHpTSLZKIC4?t=317
> Snapping dots

https://youtu.be/pHpTSLZKIC4?t=325
> If you want to watching a video on snapping dots and grid, I released a video a few days ago.

Let me track it down.

https://youtu.be/7SF3yCu53Q0
Boxcutter Tutorial for Blender 3.0 - Precision Booleans

I am guessing this is the one.

I actually got the shortcuts pdf.

https://youtu.be/7SF3yCu53Q0?t=52

Oh, I see. I was really missing this kind of capability moving into Blender from Moi. Moi will always show the midpoints, centers and endpoints (amongst others) and snap to them. This is super useful for precision work, which I in fact need in some places. It is really great that hopscutter has this.

3pm. I am having some difficulty. Let me focus more intently. Just how do I turn this feature on. I thought that Ctrl would work.

3:05pm. This is amazing. When I do a boolean cut in edit mode, it does not extrude the box past the other side of the solid. This would be particularly useful for making holes.

This addon really is useful. It would in fact save me a lot of time during modeling. Right now I can easily make cuts, but if I had to do this with booleans by hand, it would be much more tedious.

3:10pm. Oh, snap grid is more useful that I thought it would be at first glance. It would be one thing if it just snapped to grid, but what it in fact does is create a construction plane on the selected face. It is even sized so that the endpoints connect with it...Actually, it seems that was accidental.

But being able to bring up a contruction plane like this would be really useful.

https://youtu.be/7SF3yCu53Q0?t=100

Oh right, the dots respond even if the boolean is not baked in.

3:25pm. https://youtu.be/7SF3yCu53Q0?t=355

Ah, this is not just for dots. Holding alt to make it start in the middle works in general. Nice.

https://youtu.be/7SF3yCu53Q0?t=495

Let me try it out.

https://youtu.be/7SF3yCu53Q0?t=526

Hmmm, this could be useful for those grate patterns in the side. It would be annoying to set up the arrays for those kinds of things. Hmmm, maybe dots would work with arrays?

https://youtu.be/7SF3yCu53Q0?t=638

It is possible to turn off snapping, and then Ctrl + double LMB will repeat the cut on the exact spot rather than the dot.

I do love this.

https://youtu.be/7SF3yCu53Q0?t=662

Oh right, ther eis this as well. Too bad it is not possible to use dots when moving and scaling.

...Hmmm, maybe it would be possible in multi edit?

https://boxcutter-manual.readthedocs.io/en/latest/hotkeys/

Let me go through the hotkeys. I started those earlier.

4:20pm. https://youtu.be/uCAUpqBK6FE?t=110

Let me try immitating this. I do not understand what he has done here.

4:25pm. https://youtu.be/uCAUpqBK6FE?t=101

I do not get it. What the hell is he doing here?

4:40pm. I am starting to get distracted. Does local mode do something special here.

4:45pm. https://youtu.be/uCAUpqBK6FE?t=28

I got tricked so hard here. It turns out that boxcutter's inset, and Hops inset are not the same thing. The latter applies the booleans (incorrectly) before doing an inset, but the later duplicates the modifiers.

4:50pm. Let me take a break.

5:05pm. Let me resume.

https://youtu.be/uCAUpqBK6FE?t=206

This is cool. I really can't figure out how to fix it in the same way he did.

5:40pm. Insets are a bit convoluted and brittle in the way the work currently.

https://youtu.be/aUd_Ufvfc4U
This is Blender's Best Modeling Tool

This one is by Arrimus.

https://youtu.be/v50cXf6B-2k
boxcutter 718_9: - HOPS Knife Switchblade Off

This is a grand model.

https://youtu.be/v50cXf6B-2k?t=38

Oh, this causes it to reconnect.

6:05pm. Lunch time.

6:25pm. https://youtu.be/4scXty1hsto
Knife Tool Tutorial for Blender 3.0

Done with lunch. Let me watch this.

https://youtu.be/4scXty1hsto?t=82

I had no idea that angle snapping was a thing.

https://youtu.be/4scXty1hsto?t=135

I had no idea it was possible to make multiple cuts like this either.

https://youtu.be/4scXty1hsto?t=196

This really has a lot of functionality I had no idea about.

6:40pm. https://youtu.be/pHpTSLZKIC4?t=320

Now let me go back to this earlier video and I will finish for the day. I feel like I've gotten acclimated with boolean operations in Hops and Boxcutter. I should be able to use it effectively now to do that rig.

https://youtu.be/pHpTSLZKIC4?t=831

I did not know that by pressing P it was possible to adjust the bevel profile.

https://youtu.be/pHpTSLZKIC4?t=1125

Edit multi tool has a join tool.

7:15pm. Figured out what the relative option in inset does.

7:25pm. I am just doing some light mental reviewing. I'll close here for the day. At this point my Blender education should be complete. I'll deal with the rig, the rest of the room and think of what I'll do next with my path.

7:50pm. Maybe if Heaven's Key turns out to be particularly successful that will give me the leeway to cultivate 3d more deeply.

I said I'd try to shot for 4/5 and 5/5 eventually. But honestly this is a huge drag, and it has come in conflict with my desire to actually spend my time productively as opposed to just learning and perfecting my technique.

I am going to shot for 3/5 and not really bother both archmage status in 3d, at least not until I get AI assistants.

Right now, me using 3d to augment my 2d skills, while writing and doing music would be enough to satisfy me.

7:45pm. I feel like I've gone overboard or rather, these topology concerns while working with polygons have taken the wind out of my sails. And topology ends up being interlinked with UV unwrapping and hence texturing. Not to mention shading.

I want to get as far away from that as possible.

I want to ramp up my productivity way up instead of getting stuck pushing vertices around all day like I have for the past half year.

7:50pm. I do not want to dive any deeper into complexity. I want to start getting good at making actual art whether it be 3d or 2d.

7:55pm. I want to let go and just focus the art making. For the past six months it feels like I've just spent my time going through endless tutorials. Who has the will for that?

Enough is enough. I really couldn't avoid having to spend today getting acclimated with Hops and Boxcutter, but from here on out, I will start cranking out the content. I will not give up until I am done.

After I am done with the room, I will loosen the requirements a little and purposely move to a simpler style for the sake of speed. If I can get to an accemptable rate of quality per time, I can consider myself an successful artist."

---
## [Pickle-Coding/tgstation](https://github.com/Pickle-Coding/tgstation)@[d411393e72...](https://github.com/Pickle-Coding/tgstation/commit/d411393e72586ba70ac45b8af19d9b3b701e58c9)
#### Saturday 2022-05-07 18:16:22 by Zytolg

NukeOps Firebase Rework (#66149)

Attention Recruit: Welcome to Firebase Balthazord
Here you will lean how to:
-Kill corpo scum
-Kill corpo scum
-Kill corpo scu-

This has been on my docket for months. Ever since gave the Holding Facility a much needed facelift. I have been eyeballing the nukie base, waiting for that stroke of inspiration to hit me. It finally did. Gone are the aging walls of the old encampment. Nukies finally have what well-funded corpo-terrorists always dream of- a home.

It's more than a Home. This is a sweeping rework that is part of a series of reworks to revisit old locations and not only bring them up to date with our current asset roster, but to make them properly belong within the game world. The Nuke-Ops base may ultimately be a tiny chunk of the overall SS13 experience, but I'll be damned if it isn't a defining one. It's also a location that has the capacity to do one thing that I have always wanted to do. Purchase Property. You heard me right, you get to buy rooms now. The newly expanded Nuke-Ops base features, with @Mothblocks blessing, further expansions that you can purchase from your local Syndicate Uplink. Spend your TC, expand your capabilities, and utilize your expertise in order to create
the most mind-boggling disky heists there are.

Possible expansions to your terrorism suite include:
-Ordinance Lab
-Bio-Terrorism Lab
-Chemical Manufacturing Plant

Definite expansions to your Nuke-Ops Firebase include:
-Crew Bunks
-Lab Wing
-War Table
-Upgraded "Disembarkment" Bay"

---
## [Pickle-Coding/tgstation](https://github.com/Pickle-Coding/tgstation)@[b86cf89125...](https://github.com/Pickle-Coding/tgstation/commit/b86cf89125a425ad650abedf436bb02918c36dcd)
#### Saturday 2022-05-07 18:16:22 by Aleksej Komarov

tgui: API improvements + docs (#65943)


About The Pull Request

This pull request improves tgui API in many ways.

Using TGUI for custom HTML popups

This standardizes and simplifies the process of HTML popup creation and DM <-> JS communication.

Makes tgui window API a perfect alternative for old-style browser panels. It will be super useful for @Iamgoofball since he wanted to make a lightweight browser element that plays background music, and this will make his life a lot easier.

It is now possible to create tgui windows with fully inlined JS and CSS, which can be used to make unkillable tgui-based UIs (can't white/blue screen due to network errors). You can split files into JS and CSS, and still serve a single HTML file using this.

Moved sendMessage function to the Byond API object, where it rightfully belongs, and now supports a shorthand form: Byond.sendMessage(type, payload). This shortens and simplifies a lot of code.

Refactored window.update to no longer be public. Now to subscribe to incoming messages, you should use new public APIs: Byond.subscribe(fn) and Byond.subscribeTo(type, fn), and TGUI internally uses these functions as well, which reduces boilerplate in index.js.

Renamed window.__windowId__ to Byond.windowId (old variable is still available for backwards compatibility).

Byond API now supports null id, e.g. Byond.winget(null, 'url'), which makes things like this possible:

// Fetch URL of a currently connected server
Byond.winget(null, 'url').then((serverUrl) => {
  // Connect to this server (opens a new dreamseeker instance)
  Byond.call(serverUrl);
  // Close this client because new instance is connecting
  Byond.command('.quit');
});

Certain polyfills are now statically compiled (commited into git) and are baked into tgui.html. The downside is that HTML went 16 kB -> 50 kB. The upside is that you can now use a relatively modern level API with full support for IE8 when writing plain old html UIs using /datum/tgui_window directly. They are committed into git, because polyfills will never need to be updated (unless of course we randomly decide to get rid of ie8.js and html5shiv.js).
Breaking Changes

No breaking changes. This should be tested for regressions. Upgrading is simple if you're on a relatively up-to-date branch - copy paste all affected tgui files and you're good.

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[a0d2d63757...](https://github.com/treckstar/yolo-octo-hipster/commit/a0d2d63757ab9cae3f907e41fe9d5540a5690b41)
#### Saturday 2022-05-07 18:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [kispython-ru/kissinger](https://github.com/kispython-ru/kissinger)@[a0eae722c7...](https://github.com/kispython-ru/kissinger/commit/a0eae722c7efc0c66c346b5a188609c2bf6dbb78)
#### Saturday 2022-05-07 19:12:46 by Aleksey Poluyanov

Я больше не хочу спамить коммитами, я просто хочу быть счастливым...

Hello world page integrated into telegram bot. How cool is that!

Oops, dockerfile broken

Playing with jinja

Rename html file

Make kispython async again

Oops

Hm, will it make a webpage better?

new: Beautiful button

mainbutton part 2

attempt 3

really?!

This button should work

Now i think autodeploy was stupid idea in my case

Trying to change label

Trying to apply theme settings

I want to expand it!

testing web_data

Update task.html

Update task.html

On, let's try another one

And update server too

Python is too abstract imho

Oops

Summary (required)

Update main.py

I need new dependency for async functions

By the way, let's catch errors client-side

fix tgapi request

yafix

ace editor embeeding

Ok, i will use CDN version

Other CDN

Trying to fix it

Update task.html

Now let's try codejar editor

Change CDN

Still trying to embeed codejar

Switch to python

Wanna make it better looking

Change sample

Pass code to telegram bot

Temp disable feature

🤔

🤔

fix

hm

restore dropped function

Let's turn it on

fix

Update task.html

Update task.html

Update main.py

Let's try to check it

Update main.py

typo

🤬

Костыль, чтобы flask и aiogram работали вместе

😤

Update main.py

---
## [nbdd0121/linux](https://github.com/nbdd0121/linux)@[213d266ebf...](https://github.com/nbdd0121/linux/commit/213d266ebfb1621aab79cfe63388facc520a1381)
#### Saturday 2022-05-07 21:37:06 by Linus Torvalds

gpiolib: acpi: use correct format characters

When compiling with -Wformat, clang emits the following warning:

  gpiolib-acpi.c:393:4: warning: format specifies type 'unsigned char' but the argument has type 'int' [-Wformat]
                        pin);
                        ^~~

So warning that '%hhX' is paired with an 'int' is all just completely
mindless and wrong. Sadly, I can see a different bogus warning reason
why people would want to use '%02hhX'.

Again, the *sane* thing from a human perspective is to use '%02X. But
if the compiler doesn't do any range analysis at all, it could decide
that "Oh, that print format could need up to 8 bytes of space in the
result". Using '%02hhX' would cut that down to two.

And since we use

        char ev_name[5];

and currently use "_%c%02hhX" as the format string, even a compiler
that doesn't notice that "pin <= 255" test that guards this all will
go "OK, that's at most 4 bytes and the final NUL termination, so it's
fine".

While a compiler - like gcc - that only sees that the original source
of the 'pin' value is a 'unsigned short' array, and then doesn't take
the "pin <= 255" into account, will warn like this:

  gpiolib-acpi.c: In function 'acpi_gpiochip_request_interrupt':
  gpiolib-acpi.c:206:24: warning: '%02X' directive writing between 2 and 4 bytes into a region of size 3 [-Wformat-overflow=]
       sprintf(ev_name, "_%c%02X",
                            ^~~~
  gpiolib-acpi.c:206:20: note: directive argument in the range [0, 65535]

because gcc isn't being very good at that argument range analysis either.

In other words, the original use of 'hhx' was bogus to begin with, and
due to *another* compiler warning being bad, and we had that bad code
being written back in 2016 to work around _that_ compiler warning
(commit e40a3ae1f794: "gpio: acpi: work around false-positive
-Wstring-overflow warning").

Sadly, two different bad compiler warnings together does not make for
one good one.

It just makes for even more pain.

End result: I think the simplest and cleanest option is simply the
proposed change which undoes that '%hhX' change for gcc, and replaces
it with just using a slightly bigger stack allocation. It's not like
a 5-byte allocation is in any way likely to have saved any actual stack,
since all the other variables in that function are 'int' or bigger.

False-positive compiler warnings really do make people write worse
code, and that's a problem. But on a scale of bad code, I feel that
extending the buffer trivially is better than adding a pointless cast
that literally makes no sense.

At least in this case the end result isn't unreadable or buggy. We've
had several cases of bad compiler warnings that caused changes that
were actually horrendously wrong.

Fixes: e40a3ae1f794 ("gpio: acpi: work around false-positive -Wstring-overflow warning")
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: Andy Shevchenko <andriy.shevchenko@linux.intel.com>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[98f32035d8...](https://github.com/tgstation/tgstation/commit/98f32035d8dbd6b925700e9934652d03739f024b)
#### Saturday 2022-05-07 21:59:50 by LemonInTheDark

Parallax but better: Smooth movement cleanup (#66567)

* Alright, so I'm optimizing parallax code so I can justify making it do a
bit more work

To that end, lets make the checks it does each process event based.
There's two. One is for a difference in view, which is an easy fix since
I added a view setter like a year back now.

The second is something planets do when you change your z level.
This gets more complicated, because we're "owned" by a client.
So the only real pattern we can use to hook into the client's mob's
movement is something like connect_loc_behalf.

So, I've made connect_mob_behalf. Fuck you.

This saves a proc call and some redundant logic

* Fixes random parallax stuttering

Ok so this is kinda a weird one but hear me out.

Parallax has this concept of "direction" that some areas use, mostly
the shuttle transit ones. Set when you move into a new area.
So of course it has a setter. If you pass it a direction that it doesn't
already have, it'll start up the movement animation, and disable normal
parallax for a bit to give it some time to get going.

This var is typically set to 0.

The problem is we were setting /area/space's direction to null in
shuttle movement code, because of a forgotten proc arg.

Null is of course different then 0, so this would trigger a halt in
parallax processing.

This causes a lot of strange stutters in parallax, mostly when you're
moving between nearspace and space. It looks really bad, and I'm a bit
suprised none noticed.

I've fixed it, and added a default arg to the setter to prevent this
class of issue in future. Things look a good bit nicer this way

* Adds animation back to parallax

Ok so like, I know this was removed and "none could tell" and whatever,
and in fairness this animation method is a bit crummy.

What we really want to do is eliminate "halts" and "jumps" in the
parallax moveemnt. So it should be smooth.

As it is on live now, this just isn't what happens, you get jumping
between offsets. Looks frankly, horrible. Especially on the station.

Just what I've done won't be enough however, because what we need to do
is match our parallax scroll speed with our current glide speed. I need
to figure out how to do this well, and I have a feeling it will involve
some system of managing glide sources.

Anyway for now the animation looks really nice for ghosts with default
(high) settings, since they share the same delay.

I've done some refactoring to how old animation code worked pre (4b04f9012d1763df625e9e4ae75e4cf4bd1f3771). Two major
changes tho.

First, instead of doing all the animate checks each time we loop over a
layer, we only do the layer dependant ones. This saves a good bit of
time.

Second, we animate movement on absolute layers too. They're staying in
the same position, but they still move on the screen, so we do the same
gental leaning. This has a very nice visual effect.

Oh and I cleaned up some of the code slightly.

---
## [Kimi898246/Grasscutter](https://github.com/Kimi898246/Grasscutter)@[5aaa68669a...](https://github.com/Kimi898246/Grasscutter/commit/5aaa68669a3685173fcbe24a7c06933f5dd35c14)
#### Saturday 2022-05-07 22:25:50 by Kimi

another translation patches because i fucked it up

i hate myself

---
## [delvh/gitea](https://github.com/delvh/gitea)@[3725fa28cc...](https://github.com/delvh/gitea/commit/3725fa28ccc01ab08060f591f894ea6443a348e8)
#### Saturday 2022-05-07 23:58:56 by Gusted

Improve UI on mobile (#19546)

Start making the mobile experience not painful and be actually usable. This contains a few smaller changes to enhance this experience.

- Submit buttons on the review forms aren't columns anymore and are now allowed to be displayed on one row.
- The label/milestone & New Issue buttons were given each own row even tough, there's enough place to do it one the same row. This commit fixes that.
- The issues+Pull tab on repo's has a third item besides the label/milestone & New Issue buttons, the search bar. On desktop there's enough place to do this on one row, for mobile it isn't, currently it was using for each item a new row. This commits fixes that by only giving the searchbar a new row and have the other two buttons on the same row.
- The notification table will now be show a scrollbar instead of overflow.
- The repo buttons(Watch, Star, Fork) on mobile were showing quite big and the SVG wasn't even displayed on the same line, if the count of those numbers were too high it would even overflow. This commit removes the SVG, as there isn't any place to show them on the same row and allows them to have a new row if the counts of those buttons are high.
- The admin page can show you a lot of interesting information, on mobile the System Status + Configuration weren't properly displayed as the margin's were too high. This commit fixes that by reducing the margin to a number that makes sense on mobile.
- Fixes to not overflow the tables but instead force them to be scrollable.
- When viewing a issue or pull request, the comments aren't full-width but instead 80% and aligned to right, on mobile this is a annoyance as there isn't much width to begin with. This commits fixes that by forcing full-width and removing the avatars on the left side and instead including them inline in the comment header.

---

