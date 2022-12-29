## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-12-28](docs/good-messages/2022/2022-12-28.md)


1,938,991 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,938,991 were push events containing 2,690,101 commit messages that amount to 173,835,184 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 45 messages:


## [Iamgoofball/-tg-station](https://github.com/Iamgoofball/-tg-station)@[3c187487b1...](https://github.com/Iamgoofball/-tg-station/commit/3c187487b1884040608ba23b0a89aa8b0176c2aa)
#### Wednesday 2022-12-28 00:06:25 by MrMelbert

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
## [mattkime/kibana](https://github.com/mattkime/kibana)@[afb09ccf8a...](https://github.com/mattkime/kibana/commit/afb09ccf8a61d610e8e3d8beb2c80f413f1b33c5)
#### Wednesday 2022-12-28 00:15:05 by Spencer

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
## [etra0/litcher](https://github.com/etra0/litcher)@[95e678da5c...](https://github.com/etra0/litcher/commit/95e678da5cd326b6bb3fcc4f0645f2b4c9b82d6a)
#### Wednesday 2022-12-28 00:21:00 by Sebastián Aedo

Changed InputFloat for Drag for Position

As requested for our lord and savior, Jim2Point0, The Legendary
Fortographer, it would be more convenient for more the position to be
draggables.

Despite the current despair of our society, screenshots should be a top
priority of every peasant in this world, and so this commit had to be
made.

This is god's law.

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[50929f054b...](https://github.com/tgstation/tgstation/commit/50929f054b89cab80a1e501b7a01bc74c79163d7)
#### Wednesday 2022-12-28 00:55:11 by GuillaumePrata

Goliath dna infusion (#71657)

## About The Pull Request
This is a baseline version of the organs and I intend on polishing them
more in the future (Hopefully after other faunas get added to the
infuser.)

Now, this PR adds goliaths to the DNA infuser at genetics. It gives 4
organs and a final bonus effect.

1- Goliath eyes: Simple mostly filler organ that gives night vision.
2- Goliath lungs: Allow miners to breath either lavaland or the default
air mix. As a side effect they can't breath pure O2 anymore so internals
can't be used. Stay away from N2O or use your gas mask properly.
3- Goliath heart: Give miner ash storm protection
4- Goliath brain: Turns one of the miner's arm into a tendril goliath
hammer that can be used to mine. Like the mounted chainsaw it cannot be
dropped, it has slower atk speed, deals 20 damage by default and a bonus
80 to lavaland fauna, it also acts as a baseball bat against fauna so
you can dodge being hit back with good timing.
As a side effect, you can't equip gloves as your hand is a big ass
hammer...

The extra effect for having all 4 organs is lava immunity for now, I
really want to turn it into something more interesting later.

GAGS organs and bonus coderspriter arm:
![goliath
sprites](https://user-images.githubusercontent.com/55374212/205477889-22cfa586-dd43-405d-80cf-3981b31304e1.png)
If I have time I might animate the arm later.
## Why It's Good For The Game
This add some useful tools for miners if they opt into asking genetics
for help and bother to drag a goliath corpses to it.
The organs can be useful on the station, but they will only really shine
at lavaland.

We were brainstorming more things that miners can get from the station
on their downtime waiting the cargo shuttle to bring their bought gear,
this would be a simple and easy power up for miners that can have some
small (ignoring the hammer arm) bonus to miners, but small power ups
pile up.

I also wrote a hackMD around these organs, their goals, non goals,
future possibilities for fauna organs (goliath and others) etc.
https://hackmd.io/@GuillaumePrata/goliath_infusion_organs

## Changelog
:cl: Guillaume Prata
add: Geneticists figured out how to infuse goliath DNA into humanoids!
(Many monkeys were harmed in the process!)
add: Goliath eyes for nightvision, lungs to breath at lavaland safely,
heart to protect you from ash storms and the brain which turns one of
your arms into a tendril hammer.
add: Tendril hammer: Your arm becomes a giant mass of plate and tendril
but it won't fit on gloves anymore. While slow to swing around, you can
obliterate fauna/megafauna with it, 20 base dmg + 80 bonus damage to
fauna/megafauna with a bonus knockback.
/:cl:

---
## [PalJohnson/cmss13](https://github.com/PalJohnson/cmss13)@[639765b0c6...](https://github.com/PalJohnson/cmss13/commit/639765b0c69faddeec405080ab4fde79503fcf5d)
#### Wednesday 2022-12-28 01:10:21 by Skegal

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
## [PalJohnson/cmss13](https://github.com/PalJohnson/cmss13)@[0c2b070039...](https://github.com/PalJohnson/cmss13/commit/0c2b070039afaa0d18a8bbdeb9c28e8333e16470)
#### Wednesday 2022-12-28 01:10:21 by Stan_Albatross

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
## [newstools/2022-metro](https://github.com/newstools/2022-metro)@[6e5ed803ca...](https://github.com/newstools/2022-metro/commit/6e5ed803ca9c15f9ffaf8a719a37c170fd800d4d)
#### Wednesday 2022-12-28 01:27:53 by Billy Einkamerer

Created Text For URL [metro.co.uk/2022/12/27/billie-eilishs-brother-finneas-addresses-age-gap-with-her-new-boyfriend-18003225/]

---
## [jlsnow301/tgstation](https://github.com/jlsnow301/tgstation)@[b174af7661...](https://github.com/jlsnow301/tgstation/commit/b174af7661cbfaf564292caabfccca18619bda23)
#### Wednesday 2022-12-28 01:52:26 by Jacquerel

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
#### Wednesday 2022-12-28 01:52:26 by Fikou

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
## [uniphil/patch-rs](https://github.com/uniphil/patch-rs)@[364897dae8...](https://github.com/uniphil/patch-rs/commit/364897dae8599cdb758c00fdc8dacd1645959070)
#### Wednesday 2022-12-28 02:00:56 by phil

separate filename and metadata by tabs 🤦🏻‍♀️

soooooooooooooo thank you @keith for raising this in #11. turns out _every_ sample diff uses a tab character to separate the filename. git definitely always does. i haven't yet found any counter-examples (except those generated from this library 🤦🏻‍♀️🤦🏻‍♀️🤦🏻‍♀️).

well, there's one very annoying counter-example: one of the examples on gnu.org's written description of the format.

- full example (uses tabs): https://www.gnu.org/software/diffutils/manual/html_node/Example-Unified.html
- detailed description (uses spaces, doesn't specify): https://www.gnu.org/software/diffutils/manual/html_node/Detailed-Unified.html

i'm going to assume that the detailed description contains an error and ignore it 🙃. this library will switch to expect (and render) a tab character. not sure how else to handle it, but if new counter-examples come up, i'll think about thinking more about it with thoughts.

-----

would be so nice if there was an actual spec for diffs. and other fantasies.

---
## [CFC-Servers/gm_express_bindings](https://github.com/CFC-Servers/gm_express_bindings)@[71958ba832...](https://github.com/CFC-Servers/gm_express_bindings/commit/71958ba83297e924950d2b021e0e325163c8be74)
#### Wednesday 2022-12-28 02:15:21 by Brandon Sturgeon

Timers are fucking stupid who the hell made it work like this

---
## [dokku/dokku](https://github.com/dokku/dokku)@[142791876a...](https://github.com/dokku/dokku/commit/142791876aff6afb1abccded8dd1dc01e50a2511)
#### Wednesday 2022-12-28 02:51:13 by Jose Diaz-Gonzalez

fix: only skip "allows-persistence" port maps

I honestly don't remember what this does and kinda think I'll need to rip it out since it seems inscrutable...

---
## [Bobthe28th/tgstation](https://github.com/Bobthe28th/tgstation)@[99537d0123...](https://github.com/Bobthe28th/tgstation/commit/99537d0123167a07b242c33dad7c23ec9a5becef)
#### Wednesday 2022-12-28 03:54:30 by LemonInTheDark

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
## [SomeRandomOwl/Skyrat-tg](https://github.com/SomeRandomOwl/Skyrat-tg)@[cd13fcdf46...](https://github.com/SomeRandomOwl/Skyrat-tg/commit/cd13fcdf467b1a9fe5d8fc5256552b0601284dca)
#### Wednesday 2022-12-28 05:39:05 by Jolly

[MODULAR] contraband.dmi is no longer a hard override on posters (#18106)

* hhngh

* dunks this fucking dmi

* fuck you

---
## [Offroaders123/NBTify](https://github.com/Offroaders123/NBTify)@[960db873db...](https://github.com/Offroaders123/NBTify/commit/960db873db4d35afa3269ece1c2da0a76103e6d3)
#### Wednesday 2022-12-28 06:51:09 by Offroaders123

Writer Allocate Method

Redid the `#accommodate()` method on `NBTWriter`, which now has an inspired feel from the new `NBTReader` `#allocate` method.

I remembered that Node has the `Buffer.alloc()` method name, and I've been wanting to rename `#accommodate` for a while now (It didn't feel like a very specific name to me originally), so I took inspiration from that and made the new `NBTReader` method, and the original `NBTWriter` method and renamed them to use that wording instead! Allocating sounds more like what it's doing, to me, and I like that it sticks in your mind better as to what the function call is doing, when it's called.

I tidied up the function body a bit to match my more recent personal code structuring. Some of the functionality is a bit mystical to me still, so I'm going to try reimplementing it after this commit, since I didn't want to break anything with this commit.

https://www.reddit.com/r/ProgrammerHumor/comments/zv2qd5/it_shall_not_be_touched/j1o1zv4/?context=8&depth=9 (Reminded me of a post on Reddit I found about this, I find myself trying to do it more and more! Cool to hear that other people do it that way too.)

---
## [codetriage/CodeTriage](https://github.com/codetriage/CodeTriage)@[f83f74475b...](https://github.com/codetriage/CodeTriage/commit/f83f74475b131279507dbc5471247063bac611f0)
#### Wednesday 2022-12-28 08:15:22 by Richard Schneeman

Random via cached ID

The easiest way to work with random values is to call `order("RANDOM()")` but this is very bad for database performance. There's hacks to get faster lookups but they all come with caveats. Mostly in terms of guarantees, either they'll return no data, or less than the data you want. You've got to  retry queries, but if you do that in an unbounded way then you might end up an an infinite loop.

This approach attempts to give the maximum flexibility of full order("random()") but with non-awful performance. The cost here is that the values persist for the given time frame. Also since we're still using `order("RANDOM()")` the first query is still expensive.

It works like this: The SQL of the query is used to generate a cache key. The query is then made and the resulting IDs are returned. Then those IDs are used to query the original model.

I'm still not in love with it, but it's okay for now.

I think for more complex logic there's got to be a better way to handle this kind of processing. But 🤷‍♂️

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[8812c246fe...](https://github.com/treckstar/yolo-octo-hipster/commit/8812c246fee5415ef54179add9fd7184562ee3ca)
#### Wednesday 2022-12-28 08:22:04 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [mishu11/Books-Notes](https://github.com/mishu11/Books-Notes)@[14ae635583...](https://github.com/mishu11/Books-Notes/commit/14ae63558353c018c2e1dfcbbf8738bac31d3f94)
#### Wednesday 2022-12-28 09:32:00 by Aman Ahmed

Update XP: Kent Beck

XP->EXTREME PROGRAMMING EXPLAINED BY KENT BACK.

Chapter 1. What is XP?



Prepare for success. Don’t protect yourself from success by holding back. Do your best and then deal with the consequences. That’s extreme.


 In XP you only do what you need to do to create value for the customer. You can’t carry a lot of baggage and move fast. However, there is no freeze-dried software process. The body of technical knowledge necessary to be an outstanding team is large and growing.



XP means giving up old habits of working for new ways tailored to today’s reality.




XP assumes that you see yourself as part of a team, ideally one with clear goals and a plan of execution.


 The business changes. The technology changes. The team changes. The team members change. The problem isn’t change, because change is going to happen; the problem, rather, is our inability to cope with change.


Bridging the gap between values and practices are principles

 Marigolds naturally repel some of the bugs that eat strawberries. Planting them together is a practice. Companion planting is the principle.


. First you have to garden, then join the community of gardeners, then teach others to garden. Then you are a gardener.


 XP embraces five values to guide development: communication, simplicity, feedback, courage, and respect.

COMMUNICATION--->	
	when you don't have a proper communication or lack
	of communication than problem arises in development.

example of me and Akash doing thing and at that time if i hesitate to ask how to do this things,than i never came to know that this type of shortcut exist.


SIMPLICITY-->
		Simplicity only makes sense in context. If I’m writing a parser with a team that understands parser generators, then using a parser generator is simple. If the team doesn’t know anything about parsing and the language is simple, a recursive descent parser is simpler.



FEEDBACK-->
		Being satisfied with improvement rather than expecting instant perfection, we use feedback to get closer and closer to our goals. Feedback comes in many forms:



Courage-->
		Sometimes courage manifests as a bias to action. If you know what the problem is, do something about it. Sometimes courage manifests as patience. If you know there is a problem but you don’t know what it is, it takes courage to wait for the real problem to emerge distinctly.


Respect--> 
	If members of a team don’t care about each other and what they are doing, XP won’t work. If members of a team don’t care about a project, nothing can save it.




Communication preferred over long documents


Mutual Benefit is important in XP .Both the 2 person involved in XP
are getting benefits when they are spending time each other.

If you want people to take your advice, you need to solve more problems than you create.


The principle of diversity suggests that the programmers should work together on the problem and both opinions should be valued.


. Reflection comes after action. Learning is action reflected. To maximize feedback, reflection in XP teams is mixed with doing.



Learn to see problems as opportunities for change. This isn’t to say there are no problems in software development. However, the attitude of “survival” leads to just enough problem solving to get by. To reach excellence, problems need to turn into opportunities for learning and improvement, not just survival.

You might not know what to do about a problem. You might want more time to think about what to do. Sometimes the desire for more time is a mask worn to protect from the fear of the consequences of getting going. Sometimes, though, patience solves a problem by itself.

It maximizes strengths and minimizes weaknesses. Can’t make accurate long-term plans? Fine—have a quarterly cycle during which you refine your long-term plans. A person alone makes too many mistakes? Fine—program in pairs. The practices are effective precisely because they address the enduring problems of people developing software together.


Projects don’t go faster by accepting lower quality. They don’t go slower by demanding higher quality. Pushing quality higher often results in faster delivery; while lowering quality standards often results in later, less predictable delivery.




********Primary Practice*****************
1.Sit Together-->
			no matter what the client says the problem is, it is always a people problem. Technical fixes alone are not enough. The other lesson I took was how important it is to sit together, to communicate with all our senses.

Lets say you are having a problem ,than do travelling and than we can start.


Include on the Team people with all skills and persppectives necessary for the project to succedd.This is really nothing more than the old idea of cross-functional teams.

How we can say that it is successfull team
	When people feel :
						1. We belong
						2. We are in this together
						3. We support each other's work,growth and learning.

12 members are good enough in team.

Informative Workspace--->
						Make your workspace about your work.An interested observer should be able to walk into the team space and get a general idea of how the project is going in 15 sec.


Energized work--> Work only as many hours as you can be productive and only as many hours you can sustain.

Pair Programming-->
		Pair programmers:

			 Keep each other on task.

			 Brainstorm refinements to the system.

			 Clarify ideas.

			 Take initiative when their partner is stuck, thus lowering frustration.

			 Hold each other accountable to the team’s practices.



Corollary(PROVEN) Practices
----------------------
		About how you develop. If they don’t yet, they will soon. When you act trustworthy and have nothing to hide, you are more productive. (Think of all the time you no longer have to spend hiding or covering up.) When you are ready with accurate estimates and low defect rates, including customers in the development process fosters trust and encourages continued improvement.

Team Continuity
		 Value in software is created not just by what people know and do but also by their relationships and what they accomplish together. Ignoring the value of relationships and trust just to simplify the scheduling problem is false economy

Taiichi Ohno has a simple exercise for this last step, the Five Whys. Ask five times why a problem occurred. So, for example,

1. Why did we miss this defect? Because we didn’t know the balance could be negative overnight.

2. Why didn’t we know? Because only Mrs. Crosby knows and she isn’t part of the team.

3. Why isn’t she part of the team? Because she is still supporting the old system and no one else knows how.

4. Why doesn’t anyone else know how? Because it isn’t a management priority to teach anyone.

5. Why isn’t it a management priority? Because they didn’t know that a $20,000 investment could have saved us $500,000.

After Five Whys, you find the people problem lying at the heart of the defect (and it’s almost always a people problem). Addressing that problem and the other problems encountered along the way will give you some reassurance that you won’t ever have to deal with this particular mistake again.


Shared Code
			Anyone on the team can improve any part of the system at any time.
			 If something is wrong with the system and fixing it is not out of 
			 scope for what I’m doing right now, I should go ahead and fix it.




Daily Deployment
			Put new software into production every night. Any gap between what 	is on a programmer’s desk and what is in production is a risk. A programmer out of sync with the deployed software risks making decisions without getting accurate feedback about those decisions.

			Daily deployment is a corollary practice because it has so many prerequisites. The defect rate must be at most a handful per year. The build environment must be smoothly automated



How do you implement daily deployment when you have projects that take weeks or months before they are usable? 
			There are many tasks involved in a big project: restructuring the database, implementing new features, and changing the user interface. As long as you don’t change the user’s experience of the system, you can deploy all the rest of that work.



Best example is Pay per use like for eg. company ask for money to customer for every message he is going to send.

So in software industry it is like pay-per-release

=========================================================================================================================================

***********************The Whole XP Team*********************

Testers
	Testers on an XP team help customers choose and write automated system-level tests in advance of implementation and coach programmers on testing techniques.

How can you say Team's health in Good Condition.
	1.
		The first is the number of defects found after development. An XP team should have dramatically fewer defects in its first deployment and make rapid progress from there. Some XP teams that have been on the path of improvement for several years see only a handful of defects per year. No defect is acceptable; each is an opportunity for the team to learn and improve.
	2.
		The second metric I use is the time lag between the beginning of investment in an idea and when the idea first generates revenue. Even small organizations typically find they take more than a year from investment to return. Gradually reducing the time from investment to return increases the amount and timeliness of feedback available to the whole team.


==========================================================================================================================================

	Planning: Managing Scope
		Planning makes goals and directions clear and explicit. Planning in XP starts with putting the current goals, assumptions, and facts on the table	


		Part of planning is deciding what to do next out of all the possibilities. Planning is complicated because the estimates of the cost and value of stories are uncertain.

		When choosing which stories to implement next, sort them several ways. The act of laying the stories out spatially provides new insight into the relationships between the stories and smooths the selection process. You could put risky stories towards the left and valuable stories towards the top. You could put all the performance tuning stories in one corner of the table and all the new functionality stories in another corner. Whenever I get lost while planning, I gather all the stories up off the table, shuffle them, and lay them out fresh

---
## [Smlchinaza/learning-projects](https://github.com/Smlchinaza/learning-projects)@[63768e8885...](https://github.com/Smlchinaza/learning-projects/commit/63768e8885a15d629e2dcbea516455d385a9afec)
#### Wednesday 2022-12-28 10:21:46 by Chukwuemeka, Samuel Chinaza

Add files via upload

This happens to be my best and most advanced project of 2022 because I got what I want. It took me so much time (about 5 weeks) to start and complete it. I'm so happy that I am able to complete it the way I want despite all the challenges and I learnt a whole lot of new lessons and experience. Some of the inspirations about the contents came from Burger King and I'm grateful to them.

---
## [LemonInTheDark/tgstation](https://github.com/LemonInTheDark/tgstation)@[e5a2b0f16e...](https://github.com/LemonInTheDark/tgstation/commit/e5a2b0f16e2bb47b0ed60e487e3c6b2dd32f81dc)
#### Wednesday 2022-12-28 10:32:19 by LemonInTheDark

Micros the lighting subsystem (Saves a second of init) (#69838)


About The Pull Request

Micros lighting objects, and their creation

We save a good bit of time by not walking space turfs adjacent to new objects.
We also save some time with micros in the actual underlay update logic.

I swear dude we spend like 0.8 seconds of init applying the underlay. I want threaded maptick already

Micros lighting sources, and corner creation

A: Corners were being passed just A turf, and then expected to generatecorners based on that. This is pointless.
It is better to instead pass in the coords of the bottom left turf, and then build in a circle. This saves like 0.3 seconds

B: We use so many damn datum vars in corner application that we just do not need to.
This resolves that, since it pissed me off. It's pointless. Lets cache em instead

There's some misc datum var caching going on here too. Lemme see...
Oh and a bit of shortcutting for a for loop, since it was a tad expensive on its own.

Also I removed the turfs list, because it does fucking nothing. Why is this still here.

All my little optimizations save about 1 second of init I think
Not great, but not bad, and plus actual lighting work is faster now too
Why It's Good For The Game

Speed

---
## [LemonInTheDark/tgstation](https://github.com/LemonInTheDark/tgstation)@[cb20ec99f9...](https://github.com/LemonInTheDark/tgstation/commit/cb20ec99f9cac1f0ca60da1b9dc912ea4e9eebba)
#### Wednesday 2022-12-28 10:34:26 by san7890

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
## [harryob/cmss13](https://github.com/harryob/cmss13)@[a742c64df9...](https://github.com/harryob/cmss13/commit/a742c64df98ec4f23eaa64162a2518a91c642ead)
#### Wednesday 2022-12-28 11:27:16 by carlarctg

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
## [dopamiin0/tgstation](https://github.com/dopamiin0/tgstation)@[590847bdf7...](https://github.com/dopamiin0/tgstation/commit/590847bdf742b1e53f05ea700d48ec0676cdcf43)
#### Wednesday 2022-12-28 11:49:06 by Andrew

Biogenerator tweaks, leather makes more belts and clothing (#71175)

## About The Pull Request

### Revamped the biogenerator UI:


https://user-images.githubusercontent.com/3625094/200973283-b703f21b-c747-493e-98d9-043eef86d410.mp4

### Changed biogenerator icon to use layers and see the biomass level:


https://user-images.githubusercontent.com/3625094/201396065-caeaa412-6676-46f6-875e-efa2dca34985.mp4

### Biogenerator rebalance:

- Now you don't need the beaker to print solid products.
- Biogenerator now accepts all food, not just plants.
- Biogenerator now treats all nutriment subtypes as nutriments, so
vitamins and proteins also turn into biomass.
- Biomass now has the same units as other reagents (you get 5 biomass
from 5 nutrient with tier 1 parts).
- Doubled the cost of all items and reagents. (biomass generation
reduced by 10 and prices - by 5)
- Chemicals output amounts are now in units and you can select how much
you want to output exactly. It will not let you specify more than the
size of container or above 50 units with one button click.
- Reduced the amount of stored items and introduced a limit to the
biomass, both tied to the matter bin tier.

### Recipes changes:

Made biogenerator more dumb by moving the clothing out from the
biogenerator designs, and extending leather recipes instead.

The biogenerator is a grinder/recycler style machine so it doesn't make
sense that it outputs clothing.
Also you need to make leather to craft the toolbelt, while you can't do
the same to craft job-specific belts.
Now you can print leather in biogenerator and craft the leather clothing
by using the leather in-hand.
And the rice hat is now crafted from bamboo, instead of biogenerator.

Also added paper to the biogenerator recipes as it makes stuff from
cellulose and barely anyone knows that you can craft paper from 1 log
and 50 water. And paper is needed in large quantities to craft some
items, like paper frames.

And it doesn't output a pack of rolling paper. It's dumb now. It prints
the rolling paper sheets instead.

## Why It's Good For The Game

Biogenerator had terrible UX and backend logic. I didn't improve much on
BE though, but now it should be less frustrating to use.

Also I hate how biogenerator is superior to all other means of obtaining
its products. It doesn't make sense to grow and grind wheat, for
instance, when you can just throw shit into biogenerator and get the
flour fast. And the costs are ridiculous - you can get a couple of
bottles of fertilizers just from one medium potato.

It honestly begs for more nerfing, at least to make the nutriment -
chemicals exchange rate 1:1.

The reason for the biomass cap is because people use it as a sink for
veggies and generate infinite biomass. Maybe the limit will make them
care more about the part upgrade and offload some of the veggies to the
fridge for the Cook.

Also it was weird that biogenerator could tailor some things, while
others have to be crafted in-hand. Now you can print leather and craft
all types of belts and leather clothing.

## Changelog
:cl:
refactor: biogenerator UI revamped
qol: biogenerator no longer requires beaker for materials, monkey cubes
and nori
balance: biogenerator accepts all food, not just plants
balance: biogenerator treats all nutriment subtypes as nutriments
(vitamins, protein, etc.)
balance: biogenerator product prices doubled
balance: biogenerator biomass storage is limited depending on the level
of matter bins
balance: cowboy boots recipe moved from crafting to leather recipes
balance: leather clothing & belt recipes moved from biogenerator to
leather recipes
balance: rice hat recipe moved from biogenerator to bamboo recipes
balance: biogenerator now outputs rolling paper sheets instead of a pack
add: biogenerator can now print paper
imageadd: biogenerator icons now use overlays, have emissive layer and
indicate the biomass volume
/:cl:

---
## [MMMiracles/tgstation](https://github.com/MMMiracles/tgstation)@[e766444468...](https://github.com/MMMiracles/tgstation/commit/e766444468445f084d3714b515003d3f40bbce69)
#### Wednesday 2022-12-28 12:48:27 by LemonInTheDark

Changes our map_format to SIDE_MAP (#70162)


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

Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

---
## [KristonCosta/bevy](https://github.com/KristonCosta/bevy)@[4847f7e3ad...](https://github.com/KristonCosta/bevy/commit/4847f7e3adc835053a8907dd578c342b4bd395e2)
#### Wednesday 2022-12-28 13:03:19 by ira

Update codebase to use `IntoIterator` where possible. (#5269)

Remove unnecessary calls to `iter()`/`iter_mut()`.
Mainly updates the use of queries in our code, docs, and examples.

```rust
// From
for _ in list.iter() {
for _ in list.iter_mut() {

// To
for _ in &list {
for _ in &mut list {
```

We already enable the pedantic lint [clippy::explicit_iter_loop](https://rust-lang.github.io/rust-clippy/stable/) inside of Bevy. However, this only warns for a few known types from the standard library.

## Note for reviewers
As you can see the additions and deletions are exactly equal.
Maybe give it a quick skim to check I didn't sneak in a crypto miner, but you don't have to torture yourself by reading every line.
I already experienced enough pain making this PR :) 


Co-authored-by: devil-ira <justthecooldude@gmail.com>

---
## [OrionTheFox/Skyrat-tg](https://github.com/OrionTheFox/Skyrat-tg)@[ae02bd97ff...](https://github.com/OrionTheFox/Skyrat-tg/commit/ae02bd97ff71d2f4714b4ea7c8076acf21ed06c6)
#### Wednesday 2022-12-28 13:13:37 by OrionTheFox

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
## [SanjayrajD/C-Training-course](https://github.com/SanjayrajD/C-Training-course)@[9ac78e92e6...](https://github.com/SanjayrajD/C-Training-course/commit/9ac78e92e669e69e70d18c9819cc148292491297)
#### Wednesday 2022-12-28 13:16:33 by Sanjayraj D

Create The Chronicles of Narnia

Four kids Peter,Susan,Edmond and Lucy travel through a wardrobe to the land of Narnia. Narnia is a fantasy world of magic with mythical beasts and talking animals.While exploring the land of narnia Lucy found Mr.Tumnus the two legged stag ,and she followed it, down a narrow path .She and Mr.Tumnus became friends and he offered a cup of coffee to Lucy in his small hut.It was time for Lucy to return to her family and so she bid good bye to Mr.Tumnus and while leaving Mr.Tumnus told that it is quite difficult to find the route back as it was already dark.He told her to see the trees while returning back and said that the first tree with two digits number will help her find the way and the way to go back to her home is the sum of digits of the tree and that numbered way will lead her to the tree next to the wardrobe where she can find the others.Lucy was already confused, so pls help her in finding the route to her home.... 

Input Format:
Input consists of an integer corresponding to the 2-digit number.
Output Format:
Output consists of an integer corresponding to the sum of its digits.

Sample Input
23

Sample Output
5

---
## [MnlPhlp/aoc22](https://github.com/MnlPhlp/aoc22)@[d2ebdede4c...](https://github.com/MnlPhlp/aoc22/commit/d2ebdede4cf97a428ccab5d2670751194a2f5095)
#### Wednesday 2022-12-28 13:54:38 by MnlPhlp

finally fixed stupid error (wrong start)
Note to myself: Remember to read the Task precisely

---
## [ThePlank/PlankEngine](https://github.com/ThePlank/PlankEngine)@[f31bdf4d87...](https://github.com/ThePlank/PlankEngine/commit/f31bdf4d87bf4665cbb59e83892c980b611826b1)
#### Wednesday 2022-12-28 13:58:11 by ThePlank

yoo pog splashscreen????

also turns out strawberry input fucking sucks so i need to replace it (please @ArdoDev-stupid dont suggest anything)

---
## [Helg2/tgstation](https://github.com/Helg2/tgstation)@[cba002fa91...](https://github.com/Helg2/tgstation/commit/cba002fa912f07112fbbedcab330a35e2bffeab7)
#### Wednesday 2022-12-28 13:59:00 by Sol N

converts contraband file into poster file, makes holiday posters work (kind of) (#72131)

## About The Pull Request

The first part of this is just something that bothered me when I was
messing around with something that I will PR in the new year,
contraband.dm and dmi is ONLY posters. There's nothing else in there and
there are plenty of official posters, and if with #71717 we will also
add holiday posters to the mix then I think that its time to retire
contraband and make it poster.

Some small things I did while messing with it was change some variables
that were single letters into actual variable names, but overall this
part of the pr is not a player facing change.

That said, speaking of #71717 I think that it didn't work? Or didn't
work the way that it was supposed to? All of the spawned posters aren't
instances of festive posters, they are instances of normal posters, so
the code on initialize was not doing anything and the only reason the
holiday_none poster was showing up was because of the proc in randomize
spawning the posters in as those other posters. Because it didn't
actually _become_ poster/official/festive it never could do the proc
that turns it into a poster for the holiday that is actually occurring.

But then when I made it work and it turned into the generic posters I
decided that it would be better if instead of 30% of all posters being a
half finished mess, that if there wasn't a holiday poster it just
wouldn't replace them at all. I have poster Ideas and Dreams so I will
try to help with adding to more holiday posters but not in this PR.

What IS in this PR though, is a new traitor poster that appears during
the holidays.

![dreamseeker_MxxBzXIxiy](https://user-images.githubusercontent.com/116288367/208793262-9d4a45dc-f7bb-4208-b3c3-78cb68cf9af5.png)

This is a generic evil holiday poster that will replace normal evil
posters in the evil poster objective, because I agree with #72003 that
it should be a feature.

## Why It's Good For The Game

Contraband file is just posters already, this is easier for people to
find the posters.
I like holiday posters and think that we should have them and add more,
it is a fun easy thing to add to a lot of the microholidays to make them
more visible in addition to the name generation, but I don't want to see
the unfinished holiday poster so I do think that it's better to only
have them spawn if the holiday actually has a poster. Looking forward to
febuary!

## Changelog

:cl:
add: during holidays the spread syndicate propaganda through posters
objective has a chance of spawning evil holiday poster
fix: framework for holiday posters is more functional and modular
code: contraband.dm file and contraband.dmi file are both now poster.dm
and poster.dmi
/:cl:

---
## [Helg2/tgstation](https://github.com/Helg2/tgstation)@[47ec8ecd38...](https://github.com/Helg2/tgstation/commit/47ec8ecd386f028ee8b2697412c89f00c9cd139f)
#### Wednesday 2022-12-28 13:59:00 by Rhials

Adds the Sandstorm random event, directional meteor functionality, space sand. (#71802)

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

---
## [Thunder12345/tgstation](https://github.com/Thunder12345/tgstation)@[63561ca455...](https://github.com/Thunder12345/tgstation/commit/63561ca455933a38f3390f7fcfa6266fda3c53b3)
#### Wednesday 2022-12-28 14:13:06 by san7890

Guards against uplink failsafe code being the same as unlock code (#72113)

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

---
## [metabrainz/listenbrainz-server](https://github.com/metabrainz/listenbrainz-server)@[7d80b1ddd4...](https://github.com/metabrainz/listenbrainz-server/commit/7d80b1ddd4d0a8245e7769221b8123a568d06496)
#### Wednesday 2022-12-28 14:40:23 by Monkey Do

YIM22: Implement YIM22 page component

I fucked my local git history thoroughly and then force pushed like an idiot, so this commit contains  all the changes i made in the original yim-22-frontend branch.
We're not losing any interested or important history form there thankfully.

---
## [Floofies/tgstation](https://github.com/Floofies/tgstation)@[176f7a0e42...](https://github.com/Floofies/tgstation/commit/176f7a0e422b8417456e1ab65fa59e7ee88a16c5)
#### Wednesday 2022-12-28 15:01:40 by san7890

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
## [Perkedel/perkedel-astro](https://github.com/Perkedel/perkedel-astro)@[3a3c53e9c0...](https://github.com/Perkedel/perkedel-astro/commit/3a3c53e9c09ff4c518d6d076eb88f42fa5285a0c)
#### Wednesday 2022-12-28 15:26:28 by Joel Robert Justiawan

Well obviously

pervert in mean of content creations
not that thingy irl, just never!!! not even other someones, ew!!!
realize your imaginations instead.

Last time I saw Mommy long legs, Mario stuffs, and uh.. I think that's it.
will Model Resources saves us?
pls do, coz people like this
shall not have internet at all, either because
of her parent or what the hell
sacred-ass poops all this.
Believe me, this is karen.
way way too far!

Ray, look that this, that person even had blacklist. Yep,
typical genophobic.
genus means category
phobic means fear.
fear of certain category of people, yuck!
libigenophobic, This.. virgin.
libid means lewd.

---
## [siku2/rust-monaco](https://github.com/siku2/rust-monaco)@[cac3ea13d4...](https://github.com/siku2/rust-monaco/commit/cac3ea13d4467966ac3d969d5b9c3c949209f637)
#### Wednesday 2022-12-28 16:00:28 by Zoltan Nagy

Fix (?) `CodeEditorLink`

When attempting to use `CodeEditorLink::with_editor`, in my use-case the
callback would never be invoked, and `with_editor` would always return
`None`. When printing the value of the link, I saw it *did* have a
`Some(...)` in there, so I suspect something was up with the way `Rc` /
borrows were used? I tried to understand exactly what's
happening, but got lost in the `Scope` / `Rc` / `RefCell` soup. Another
guess is that the `Scope` that got stored in the `Rc<RefCell>>` on
`CodeEditorLink` wasn't actually linked (heh) to the *real* scope, since
that was a copy of the `Scope`.

I'm kinda experimenting my way through a fairly big design space, and I
have *some* experience messing with `Rc` and friends, but I'm completely
new to Yew, so I'll document my thought process so you can more easily
tell me if / how I'm wrong.

## Attempt 1

* We only ever store `CodeEditorModel` inside an
  `Rc<RefCell<Option<CodeEditorModel>>>`. This smart pointer gets cloned
  to each new `CodeEditorLink` (instead of storing some reference to a
  `Scope`). This makes it easy to reason about
  what's going on - exactly the data we need is passed around, and it
  has a single place of storage.
* I dropped the feature of allowing a `CodeEditorLink` to be passed in,
  for two reasons:
  * `CodeEditorLink` didn't expose a public constructor, and the `.0`
    field is private, so there is in fact no way (AFAICT) to create a
    `CodeEditorLink`. This means the feature ... never worked? I think?
  * `ctx.prop()` gives us an &-reference, so to update the data in the
    `CodeEditorLink` passed in via props, we need internal mutability,
    which complicates things further. Dropping this allows the
    implementation to be simple, and user code can still store the
    `CodeEditorLink` instance received in the `on_editor_created`
    callback.

This however has a drawback: if user code wants to store the
`CodeEditorLink`, then (at least in functional components) we kinda
enforce double-rendering at startup: there's no clean way of saying
"re-render if the link changes, except the first time when I store some
special `None` value in the state". So:

## Attempt 2

* Added a public constructor
* Re-added the `link` property
* Wrapped the data in `CodeEditorModel` into a `RefCell` to enable
  internal mutability (no need for another wrapping `Rc`)

This is close, but there's *still* double-rendering in some
circumstances. The core problem is: we don't have anything in
`CodeEditorLink` for a stable comparison across rendering passes,
*only* the reference to the model. Since that changes once the editor
is created, the `CodeEditorLink` is also considered to have changed.

I messed around with a synthetic id, but didn't manage to get the
behavior I wanted; ended up using `TextModel` instead to get the text
out of the editor.

Again, this is not perfect; in particular, if `on_editor_created`
depends on the `CodeEditorLink`, then we get double-rendering. But I
figure it's an improvement still, so submitting the PR.

---
## [TianWalkzzMiku/SuperRyzen-4.19-sdm660](https://github.com/TianWalkzzMiku/SuperRyzen-4.19-sdm660)@[8d968b46e8...](https://github.com/TianWalkzzMiku/SuperRyzen-4.19-sdm660/commit/8d968b46e8e1d49d5ab519bf1ba788c32e8d0b1a)
#### Wednesday 2022-12-28 16:31:07 by Jason A. Donenfeld

random: use linear min-entropy accumulation crediting

commit c570449094844527577c5c914140222cb1893e3f upstream.

30e37ec516ae ("random: account for entropy loss due to overwrites")
assumed that adding new entropy to the LFSR pool probabilistically
cancelled out old entropy there, so entropy was credited asymptotically,
approximating Shannon entropy of independent sources (rather than a
stronger min-entropy notion) using 1/8th fractional bits and replacing
a constant 2-2/√𝑒 term (~0.786938) with 3/4 (0.75) to slightly
underestimate it. This wasn't superb, but it was perhaps better than
nothing, so that's what was done. Which entropy specifically was being
cancelled out and how much precisely each time is hard to tell, though
as I showed with the attack code in my previous commit, a motivated
adversary with sufficient information can actually cancel out
everything.

Since we're no longer using an LFSR for entropy accumulation, this
probabilistic cancellation is no longer relevant. Rather, we're now
using a computational hash function as the accumulator and we've
switched to working in the random oracle model, from which we can now
revisit the question of min-entropy accumulation, which is done in
detail in <https://eprint.iacr.org/2019/198>.

Consider a long input bit string that is built by concatenating various
smaller independent input bit strings. Each one of these inputs has a
designated min-entropy, which is what we're passing to
credit_entropy_bits(h). When we pass the concatenation of these to a
random oracle, it means that an adversary trying to receive back the
same reply as us would need to become certain about each part of the
concatenated bit string we passed in, which means becoming certain about
all of those h values. That means we can estimate the accumulation by
simply adding up the h values in calls to credit_entropy_bits(h);
there's no probabilistic cancellation at play like there was said to be
for the LFSR. Incidentally, this is also what other entropy accumulators
based on computational hash functions do as well.

So this commit replaces credit_entropy_bits(h) with essentially `total =
min(POOL_BITS, total + h)`, done with a cmpxchg loop as before.

What if we're wrong and the above is nonsense? It's not, but let's
assume we don't want the actual _behavior_ of the code to change much.
Currently that behavior is not extracting from the input pool until it
has 128 bits of entropy in it. With the old algorithm, we'd hit that
magic 128 number after roughly 256 calls to credit_entropy_bits(1). So,
we can retain more or less the old behavior by waiting to extract from
the input pool until it hits 256 bits of entropy using the new code. For
people concerned about this change, it means that there's not that much
practical behavioral change. And for folks actually trying to model
the behavior rigorously, it means that we have an even higher margin
against attacks.

Cc: Theodore Ts'o <tytso@mit.edu>
Cc: Dominik Brodowski <linux@dominikbrodowski.net>
Cc: Greg Kroah-Hartman <gregkh@linuxfoundation.org>
Reviewed-by: Eric Biggers <ebiggers@google.com>
Reviewed-by: Jean-Philippe Aumasson <jeanphilippe.aumasson@gmail.com>
Signed-off-by: Jason A. Donenfeld <Jason@zx2c4.com>
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

---
## [ctm/Bataan-Memorial-Death-March](https://github.com/ctm/Bataan-Memorial-Death-March)@[9cee0b02a3...](https://github.com/ctm/Bataan-Memorial-Death-March/commit/9cee0b02a3ebdf870384db17af1a05fec5636925)
#### Wednesday 2022-12-28 16:51:34 by Clifford T. Matthews

Includes my "speed" run from this morning.

Took 400mg of ibuprofen due to my left knee and my right foot hot-spot.  The
knee never complained (although it might have, had I not taken the ibuprofen).
My hot-spot, on the other hand, gave me a bunch of trouble.  It was lightly
raining and warm (warm for this time of year).

I'm mildly disappointed with my performance today.  This is better than
three of the last six years I've trained, but significantly worse than
the other three years.  OTOH, I didn't fall.  I do believe my left knee is
slowly recovering and will not be holding back my training.  The hot-spot,
on the other hand, seems to be shifting around a bit and is reining in my
distance.  I don't, for example, yet know if I'll do the 50k on Sunday
or choose a shorter distance.  I have a lot of experience recovering from
knee injuries; I have no experience recovering from persistent hot-spots.

---
## [Mezque/VRC-Music-Py](https://github.com/Mezque/VRC-Music-Py)@[30fedd8822...](https://github.com/Mezque/VRC-Music-Py/commit/30fedd882214c1ae9138b04514f651cf610410a6)
#### Wednesday 2022-12-28 18:06:40 by Micah

ClientID and Secret saving works?

I hope it does cause its working for me but the last one also worked for me but not my friend. I have changed to using ' with open ' instead of just ' open '

also fixed a stupid bug my friend was getting with os.mkdir("Settings") where windows said nah bitch the directory exists already and would crash python, I hate windows. ( why didn't this error happen to me :trollface: )

---
## [carlarctg/cmss13](https://github.com/carlarctg/cmss13)@[15af7f1ee5...](https://github.com/carlarctg/cmss13/commit/15af7f1ee5e7dbd568ea01b53c993e127b4bdb12)
#### Wednesday 2022-12-28 18:29:08 by ThePiachu

Cargo ammo and ammo box mapping (re-up) (#1759)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

## About The Pull Request

Previous version of this PR ( #1650 ) claimed to have changed 384 files,
which would be impossible to review. So re-uploading this PR with
hopefully a sane amount of files changed...

---

When I was playing cargo I spent a good half an hour in a round just
mindlessly packing ammo magazines into boxes in squad prep. It didn't
put a dent in the squad prep supply, and I barely got a handful of
boxes. So I thought to myself that this is pretty much a waste of time
for cargo and decided to code a better solution:

https://www.youtube.com/watch?v=cnXcEYAV8P4

So now select vendors (opt-in via `VEND_LOAD_AMMO_BOXES`) support ammo
consolidation. They count the number of ammo magazines you have and from
that they derive the number of magazine boxes you can vend. If you vend
a magazine, it updates the number of boxes available, and if you vend a
box, it updates the number of magazines available (as well as all
derived boxes - see the 3 pack of grenades and 25 pack box).

The `item_to_box_mapping` tracks ammo boxes (minus loose ammo), grenade
boxes, grenade packets and mine boxes.

Most notable affected vendors - Requisition ammo vendor, Requisition
vendor that features grenades, Squad vendors that have ammo in them.

So now Requisition will be able to easily raid Squad Vendors to stock up
their ammo drops and save countless hours of mind-numbing cargo work.

This code ALSO correctly works when you're re-stocking a vendor with
either individual magazines or magazine boxes. Correct amounts are
updated everywhere. So you *could* take a magazine box, put it in a
vendor and thus let people vend 16 magazines out of it seemlessly.
Really useful just incase you need to restock Requisitions with
individual ammo or something...

Other notes:
- Boxes of magazines are put directly under the corresponding ammo so
you can vend them in larger amounts easier. Useful for 3-packs of
grenades
- We should add a Shotgun Shell Box Box so we can also handle those
easily...
- Nailgun ammo box had to be converted from being /smg/ since that
created an invalid ammo box that nobody used.
- Nulled out a magazine type for an intermediary box that later gets
used for MREs and all that

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

Gameplay around loading magazines into ammo boxes is not interesting, so
cutting it down to minimum is for the best.

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->

## Changelog

<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->

:cl:
add: Added an automated ammo box management system to various vendors
stocking bulk ammo and grenades. It will automatically combine ammo
magazine into boxes, and divide boxes into individual magazines (or
grenades, MRE packets, etc.). The boxes will appear at the bottom of the
vendor (yes, this also includes the regular grenade boxes that used to
be higher).
qol: Cargo will no longer need to pack individual vended ammo magazines
into boxes thanks to the ammo box management system. Your chains have
been broken!
qol: Requisitions vendor now stocks 3-packs of grenades as well as
individual HEDP grenades.
qol: Requisitions ammo vendor now can vend a lot more individual
magazines (actual number of magazines remains unchanged, just the ammo
boxes have been consolidated into magazines).
qol: Requisition vendors now vend to floor when they are not vending to
the front desks. This will make filling crates of ammo boxes or rappels
easier.
code: Minor changes to code around some ammo boxes to remove one phantom
box and prevent intermediate box types from being indexed when they
shouldn't be.
code: Refactored the code that checks whether items are in mint enough
condition to re-stock.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->

---
## [boot2big/immersive_vehicles_vanity](https://github.com/boot2big/immersive_vehicles_vanity)@[04d28f88bd...](https://github.com/boot2big/immersive_vehicles_vanity/commit/04d28f88bd263e854f0720e930ce6c17c64ba46e)
#### Wednesday 2022-12-28 18:51:48 by boot2big

Fuck you Github.
Merge branch 'main' of https://github.com/boot2big/immersive_vehicles_vanity into main

---
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[ab5f1fcb45...](https://github.com/cmss13-devs/cmss13/commit/ab5f1fcb45311e9a4fff9f6250ec180207c6271e)
#### Wednesday 2022-12-28 20:04:57 by carlarctg

Fixed entering APC being 0.1 seconds instead of 1 (#2117)

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
Fixed entering APC being 0.1 seconds instead of 0.5

It had '1' instead of '1 SECONDS'. This isn't intentional because of the
outdated comment and as stated below

# Explain why it's good for the game

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->

Sometimes bugs and oversights are elevated into features, this is
effectively one but in practice it means that marines have way too much
freedom of movement and versatility entering it, it's less like a
clunky, bulky, cassettepunk APC and more like a Ferrari convertile. It
also allows them to instantly enter the APC while being killed by a
Xeno, which is stupid and lame.

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
fix: Fixed entering APC being 0.1 seconds instead of 1 second.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [Buildstarted/linksfordevs](https://github.com/Buildstarted/linksfordevs)@[d6fcf5d9a1...](https://github.com/Buildstarted/linksfordevs/commit/d6fcf5d9a1e191953f0fb3c70274a715ae938a2d)
#### Wednesday 2022-12-28 23:08:18 by Ben Dornis

Updating: 12/28/2022 11:00:00 PM

 1. Added: ReDoS "vulnerabilities" and misaligned incentives
    (https://blog.yossarian.net/2022/12/28/ReDoS-vulnerabilities-and-misaligned-incentives)
 2. Added: The Catch-22 of Democracy - Pravesh Koirala
    (https://praveshkoirala.com/2022/12/28/the-catch-22-of-democracy/)
 3. Added: How I spent two months doing nothing
    (https://proofinprogress.com/posts/2022-12-28/How-I-spent-two-months-doing-nothing.html)
 4. Added: Data Science and Software Engineering (I)
    (https://www.amolas.dev/blog/about-data-science-and-software-engineering-i/)
 5. Added: Rehearsing a sabbatical · Max Gorin
    (https://mxgrn.com/blog/rehearsing-a-sabbatical)
 6. Added: Stop the Scroll: How Muting Everyone on Social Media Can Put You Back in Control
    (https://seanbolton.dev/2022/12/28/stop-the-scroll-how-muting-everyone-on-social-media-can-put-you-back-in-control/)
 7. Added: Sick Day Part 2
    (https://nicky.bearblog.dev/sick-day-part-2/)
 8. Added: Rack Mounting Home Assistant Yellow
    (https://johnzanussi.com/posts/rack-mounting-home-assistant-yellow)
 9. Added: This is what free, ad-supported Uber rides might look like. Mockups, economics, and analysis. at andrewchen
    (https://andrewchen.com/this-is-what-free-ad-supported-uber-rides-might-look-like-mockups-economics-and-analysis/)
10. Added: Boring work
    (https://www.borislav.me/boring-work)
11. Added: Human-Oriented Automatic Theorem Proving
    (https://wtgowers.github.io/human-style-atp/)
12. Added: Introducing Helix
    (https://miserlou.github.io/Helix/misc/2022/12/27/introducing-helix.html)
13. Added: Steps Lead to More Steps - Can's blog
    (https://canolcer.com/post/steps-lead-to-more-steps/)
14. Added: Ups and Downs of A Side Project
    (https://jereze.com/blog/4-year-side-project/)

Generation took: 00:08:07.3197865
 Maintenance update - cleaning up homepage and feed

---
## [beProsto/fennet](https://github.com/beProsto/fennet)@[9860ee6791...](https://github.com/beProsto/fennet/commit/9860ee679196e5a17354e467a5eb932f65eb116d)
#### Wednesday 2022-12-28 23:08:20 by beProsto

Some things get better, you just need to find a way to make them get better. Standing in place trying to let them go away on their own, with time brings you nothing, it will only make it all worsen. It will make the wounds cut deeper, with time making you succomb to the wounds as opposed to letting them heal. What you need to do, is act. I've found that out the wrong way. But now, they're starting to heal. I will finally be able to rest assured i don't feel like there's a 5 ton ball of steel laying on my chest, not letting me move, not letting me talk, only letting me cry. I hope for this episode of my life to be forgotten, i hope to not have to go through anything like that ever again. I finally have someone with me. Someone i can trust, someone i can talk with. Someone who understands. Someone i can laugh with, someone i can cry to. Someone who won't let me cry because of them. Someone i love. I want to dedicate myself to making both our lives better from now on. It's not the way of  anymore. It's about the dedication i ought to put into making it get better. I opened up, i let the motions go. I finally feel at least partially free from them. I will make them fully go away. I will do it. I will power through the rest of the challenges i get thrown at. Because i finally have someone, who i know outghts to support me, rather than undermine me. I trust them, i hope they can trust me too. I hope we get to show each other this support forever from now on. We'll do it. I can feel it. I love you, rf. <3

---
## [Gofawful5/Skyrat-tg](https://github.com/Gofawful5/Skyrat-tg)@[24ae11ad6f...](https://github.com/Gofawful5/Skyrat-tg/commit/24ae11ad6f6af9c0b6dab12986b95943f0cdf1f8)
#### Wednesday 2022-12-28 23:21:08 by SkyratBot

[MIRROR] Adds a reagent injector component and BCI manipulators to all circuit labs [MDB IGNORE] (#17617)

* Adds a reagent injector component and BCI manipulators to all circuit labs (#71236)

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

Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>

* Adds a reagent injector component and BCI manipulators to all circuit labs

Co-authored-by: RikuTheKiller <88713943+RikuTheKiller@users.noreply.github.com>
Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>
Co-authored-by: Paxilmaniac <paxilmaniac@gmail.com>

---

