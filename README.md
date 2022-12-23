## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-12-22](docs/good-messages/2022/2022-12-22.md)


2,082,215 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,082,215 were push events containing 3,053,890 commit messages that amount to 235,473,140 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 64 messages:


## [maesierra/adventOfCode2022](https://github.com/maesierra/adventOfCode2022)@[529f604bf2...](https://github.com/maesierra/adventOfCode2022/commit/529f604bf237889276da6edbf29285771cdbc9df)
#### Thursday 2022-12-22 00:09:11 by Maria-Eugenia Sierra

day 21

an easy day. Using pointers and a tree made the recursion really easy. I could not reuse the model for part 2 but
I had a lot of fun implementing the equation solving algorithm that I remember from school.
make my classes implementmake my classes implement
go rant...
Inheritance would had made today really easy. But this half-aserd interfaces in go are almost useless and painful to use.
You don't need to declare interfaces. That looks good on the paper, but it makes almost imposible to track the usages
and your IDE should be able to help declaring those methods, but here you have to copy/paste

And for the n-th time. Inheritance is good. Today I had to methods to the interace that I could have inherited and implement
them on every subclass
Also I had to add methods to the interace that made no sense because you cannot cast back to the actual class
It was so so painful today. And all the madness with the interace pointer receiver's
This is bad. Allow me to cast freely like C or give me inheritance and runtime matching. But this neither is frustrating and
error-prone

---
## [maesierra/adventOfCode2022](https://github.com/maesierra/adventOfCode2022)@[19d9a9161e...](https://github.com/maesierra/adventOfCode2022/commit/19d9a9161ef04bd85a906d3aa6efd6fc78afa3e2)
#### Thursday 2022-12-22 00:18:59 by Maria-Eugenia Sierra

day 21

an easy day. Using pointers and a tree made the recursion really easy. I could not reuse the model for part 2 but
I had a lot of fun implementing the equation solving algorithm that I remember from school.

go rant...
Inheritance would had made today really easy. But this half-baked interfaces in go are almost useless and painful to use.
You don't need to declare interfaces. That looks good on the paper, but it makes almost imposible to track the usages
and then it's difficult for your IDE to help you implementing the interface, but in got you have to copy/paste or type
because your cannot read your mind.

And for the n-th time. Inheritance is good. Today I had to add methods to the interface that I could have inherited and then implement
them on every subclass
Also I had to add methods to the interace that made no sense because you cannot cast back to the actual class
It was so so painful today. And all the madness with the interace pointer receiver's
This is bad. Allow me to cast freely like C or give me inheritance and runtime matching. But without any of thos is frustrating and
error-prone

day 17 (part 2 not working but some progress)

There is a pattern and it can be found with state+pos+shape but converting it to an actual solution doesn't seem to work. Also for some reason
even part1 does not seem to pass the tests anymore (but it still gives me the right solution for the input)
I know I should add the lines up to the pattern start but even with that the number is still too low.
I've attempted 1556521739125 and 1556521739122. Both too low

---
## [DrSLDR/eficode-wapp](https://github.com/DrSLDR/eficode-wapp)@[ee911f97aa...](https://github.com/DrSLDR/eficode-wapp/commit/ee911f97aa5e6c0427da6b561d050623ceeb480f)
#### Thursday 2022-12-22 00:22:59 by Jonas A. Hultén

Wrote some _absolutely_ cursed filtering

The process of exporting and sending the Docker images is time consuming
and, in the spirit of Ansible's idempotency, should only be done when
needed. Hence, I slapped together some "delightful" filtering code to
check if our Docker images already exist on the host and, if so,
skipping to transfer them.

The language of Ansible filters is not a nice one. I've done my best
here to make it reasonably readable, but... yeah. It is what it is.

---
## [willior/Action_RPG_1](https://github.com/willior/Action_RPG_1)@[8775e57ca7...](https://github.com/willior/Action_RPG_1/commit/8775e57ca73bb099af743ed6147a78ec3540acd9)
#### Thursday 2022-12-22 00:31:19 by willior

multiplayer state saved to disk

before, the state of multiplayer_2 was not saved to disk in the save_game file. the only way to toggle multiplayer on/off, previously, was with the select_2 action.
i made it so that the savegame.save file includes a "multiplayer_2" key : boolean value. the issue was getting the game scene to load player data properly.
as mentioned, PlayerLog now has a multiplayer_2 flag. this flag is only checked/used when saving/loading. the GameManager.multiplayer_2 flag is what determines if the scene should spawn another player or not.
when we load a game, we check PlayerLog.multiplayer_2 and set GameManager.multiplayer_2 to its value. then, on World _init(), we check if GameManager.multiplayer_2. if true, we do player2 = GameManager.load_player2(), which loads & initializes an additional Player scene (Player2) and stores it in the player2 variable. now, the World scene AND GameManager scene both have a player2 variable.
when player(s) enter the SceneTree, they call GameManager.initialize_player(player_name). doing this also sets Global player variables (Global.player1 & Global.player2). so there are 3 ways to access either player; both of them available in the global scope. that might cause confusion/problems... anyway...
the operation order should be as follows:
1. a savegame is loaded;
2. GameManager loads the file, and sets the following: map_path, Player1Stats, Player2Stats, P1FormulaData, P2FormulaData, PlayerLog (includes multiplayer_2 flag), and resources (techbook, formulabook, pouch), and then loads the GameWorld (via map_path);
3. GameWorld _init(): first load a Player scene, without adding it to the GameWorld yet. then, check if GameManager.multiplayer_2 is true. if it is, load player2 (via GameManager.load_player2());
4. GameWorld _ready(): add Player 1 to the GameWorld;
5. Player._ready(): sets resources from Global._attributes (if they exist; this is for zoning), then call GameManager.initialize_player(player_name). this sets resources.
6. GameWorld checks if GameManager.multiplayer_2 == true, and adds Player2 to the GameWorld if it is.
7. Player2._ready() initializes player2, as above, setting resources.

i believe it's all working as intended. more rigourous testing is possibly required to make sure real-time multiplayer toggling always assigns the proper values, and to make sure those values get saved & loaded properly to disk.
when multiplayer_2 is toggled off, Player2's resources (techbook, formulabook, pouch) are stored in temporary variables inside of GameManager. if multiplayer_2 is toggled back on, we load resources from those variables. if the game is saved during this state, then the data stored in the temporary variables is saved.
there are some problems. player 2's inventory is not updated when zoning. this is kind of crazy to me since it is literally the exact same code as player1. the inventory resources, when zoning, are not set properly. the issue had to do with the timing of the way the Exit executes its code.
when a player Zones, the Exit takes their inventory and stores it in an array. it then checks if GameManager.multiplayer_2 is enabled. if it is, it takes player2's inventory and stores it in a different array, then loads the next scene with both inventories stored as separate index in the Global._attributes dictionary ("inventory_1" & "inventory_2"). if GameManager.multiplayer_2 == false, then we changed scenes with only player 1's inventory.
this functionality has been changed. before changing scene, we check if multiplayer_2 == true. if it is, we store player2's inventory in a variable, new_inventory_2; if it's not true, we check if player2_data[0] != null, and pass that data, if it exists. otherwise, new_inventory_2 remains null. then, on player._ready(), we check if inventory != null before setting inventory resources. if it is null, we simply initialize the player.
theoretically, this system should handle all types of situations. the idea is that if a player joins, gains exp/levels etc., then quits, but player1 carries on, the progress made by player2 is still stored somewhere. i BELIEVE the system is working as intended, although it is quite complex so rigourous testing is required still.
a completely unrelated mechanical change: Formula XP was only rewarded when the formula animation ended. i wanted it this way because i didn't want a formula that was cast that was to level to take advantage of the leveled stats. the issue is that ingredients are subtracted at the BEGINNING of the spell animation. so, in multiplayer, if a player were to cast and then another player zoned immediately after, the casting player would lose their ingredients and get no XP for casting the formula. i've made it so that ingredient removal and formula XP reward take place at the same time, so there is no way ingredients can be "wasted" accidentally by another player zoning, since you will still get the XP for casting it.
another slight change: when a tech is learned, we parse through _techs_learned, checking if a tech with the same type & level already exists. if we get through the entire array without a match, then we automatically equip that tech to its appropriate slot. in other words, if you acquire a tech for a slot for which no techs have already been learned, that tech gets auto-equipped.
one thing that i'm not sure is bugging me or not is that the current_selected_formula is not saved to disk when we create a savegame, so when loading a game from disk, the equipped formula will always be the one in the 0th slot. this is... fine, really, it's not a huge deal - but, i think i'd like it if it were saved. i just don't know how much of a pain it'd be.
.... not much a pain, because i just did it, with 2 lines of code, 1 for each player.
on GameManager.initialize_player(), we check if GameManager's inventory resources != null. if they aren't, then that means GameManager has resources loaded from disk. we then set those resources' parameters. example:

player.formulabook.set_formulas_learned(p1_formulabook.get_formulas_learned())

the above sets the currently iniitializing player's formulabook's learned formulas to those stored in p1_formulabook. then, in order to set the current selected formula, we simply call:

player.formulabook.set_selected_formula(p1_formulabook.current_selected_formula)

... and done. formulas get set. the only other change was that formulabook's current_selected_formula variable needed to be exported so that it's able to be saved in the saved .tres file.
... oh wait, 1 other issue. when "NEW GAME" is selected, we actually load inventory resources... empty ones. an empty formulabook has an _equipped_formulas.size() of 0. so when we call set_selected_formula on an array of size 0, we get an error. so, on player initialization - when we load resources, which is done when we either hit "NEW GAME" or "CONTINUE" - we check if player.formulabook._formulas_equipped.size() > 0, and only call player.formulabook.set_selected_formula(p1_formulabook.current_selected_formula) if it is. in other words, do we have ANY formulas equipped? if we do, set the one saved via index in the saved formulabook resource.

---
## [Shad0vvs/cmss13](https://github.com/Shad0vvs/cmss13)@[1a226283e5...](https://github.com/Shad0vvs/cmss13/commit/1a226283e5c108dffcb74746af5d36ba29d51058)
#### Thursday 2022-12-22 00:41:33 by Diegoflores31

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
## [Shad0vvs/cmss13](https://github.com/Shad0vvs/cmss13)@[bba6239bc1...](https://github.com/Shad0vvs/cmss13/commit/bba6239bc19510ecd235acc31ec75783751f9bcc)
#### Thursday 2022-12-22 00:41:33 by Stan_Albatross

sniper sentries rebalance (#1951)

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

halves sniper sentry range reduces accuracy a bit ups firerate 

# Explain why it's good for the game

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->

being shot at from far offscreen is awful, this should make sniper
sentry a bit more of a threat when it does come into play while not
being able to hit you from half the map away

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
balance: halved the sniper sentry's range to 10 tiles
balance: reduced the sniper sentry's accuracy by 20%
balance: reduced the sniper sentry's delay between shots from 2s to
1.25s
balance: reduced the plasma sentry's range to 10 tiles
balance: reduced the plasma sentry's delay between shots from 10s to 7s
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

Co-authored-by: Stan_Albatross <swt91a@gmail.com>

---
## [dgp1130/HydroActive](https://github.com/dgp1130/HydroActive)@[aaf1aacb92...](https://github.com/dgp1130/HydroActive/commit/aaf1aacb92317a79757c5bd0390128a90fdb1487)
#### Thursday 2022-12-22 01:02:30 by Doug Parker

Adds `$.props` and a templating example as well updates the `state-host-counter` example.

This exposes component props at `$.props`, wrapping them into signals which update whenever the property is modified. This makes it easier to receive inputs from parent components in HydroActive.

A couple notable challenges with this design:
1. Props can't be easily specified for a component until *after* hydration, meaning they almost always hydrate with `undefined`. Signals makes this easier to manage, but it's still a default case you have to worry about. "Required" props isn't easily supported.
2. Templated components *can* require props be specified before hydration via the factory. "Require" is a strong word, if you use the factory and keep your types sound, TypeScript will effectively require all the properties to be specified before hydration. However, if you don't use the factory or do some bad casts, you can end up in a situation where a "required" property is missing. For this reason, `$.props` always returns `| undefined` in its accessors. This is a bit annoying to deal with, though components can assert that the signal is defined if necessary (either at runtime or compile-time).
3. This is implemented via a proxy on `$.props`. Any get operation results in checking the host component's property of the same name. The current value at time of first read is used as the initial value, and then the property is replaced with a getter/setter pair which wrap the signal.
    * I have some concerns about this implementation, firstly in modifies the shape of the component over time, which deoptimizes it in many respects in the browser engine at runtime from my understanding. We're already doing this with the returned values from `component(($) => { /* ... */ })` anyways, so I don't know that it has too much more impact over that.
    * Secondly, we don't actually have a runtime-available schema or list of expected properties. We know props at compile-time because they are explicitly listed in the `ComponentDef` parameter type, but we don't have visibility into that at runtime. We only discover a property exists when `$.props.someProp` triggers the proxy getter, so we lazily evaluate it.

---
## [jlsnow301/tgstation](https://github.com/jlsnow301/tgstation)@[cf02f62298...](https://github.com/jlsnow301/tgstation/commit/cf02f622986932af8fb09e48cbdf5ec0ac567cf5)
#### Thursday 2022-12-22 01:21:49 by LemonInTheDark

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
## [jlsnow301/tgstation](https://github.com/jlsnow301/tgstation)@[176f7a0e42...](https://github.com/jlsnow301/tgstation/commit/176f7a0e422b8417456e1ab65fa59e7ee88a16c5)
#### Thursday 2022-12-22 01:21:49 by san7890

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
## [microl44/Julet](https://github.com/microl44/Julet)@[2d4f41b6fc...](https://github.com/microl44/Julet/commit/2d4f41b6fc51bca245e204e1f461deab88537d12)
#### Thursday 2022-12-22 01:34:37 by microl44

rqing javascript by pushing incomplete function to main. Fuck you javascript

---
## [ninstar/Rich-Presence-U-DB](https://github.com/ninstar/Rich-Presence-U-DB)@[4659b59a14...](https://github.com/ninstar/Rich-Presence-U-DB/commit/4659b59a140619ec30a560daedcf02e034d94748)
#### Thursday 2022-12-22 01:44:30 by ninstar

+14 Nintendo Switch titles

- CRISIS CORE –FINAL FANTASY VII– REUNION
- TRIANGLE STRATEGY™
- LIVE A LIVE
- MONARK
- SMITE
- Demon Turf
- Demon Turf: Neon Splash
- Amnesia: Collection
- Tactics Ogre: Reborn
- Little Noah: Scion of Paradise
- The Legend of Heroes: Trails of Cold Steel III
- The Legend of Heroes: Trails of Cold Steel IV
- GROOVE COASTER WAI WAI PARTY!!!!
- Just Dance®

---
## [usnpeepoo/cmss13](https://github.com/usnpeepoo/cmss13)@[0dd70b12e5...](https://github.com/usnpeepoo/cmss13/commit/0dd70b12e5142b3b0f14bf237765c1e643fe8a3f)
#### Thursday 2022-12-22 02:12:28 by Stan_Albatross

removes unused nanoui templates (#2012)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

none of these templates are used anywhere

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->

fuck nanoui

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
del: Removed ten unused nanoui templates. Don't worry, they'll all be
going away soon.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

Co-authored-by: Stan_Albatross <swt91a@gmail.com>

---
## [4hands44/cmss13](https://github.com/4hands44/cmss13)@[7f1e80ca3d...](https://github.com/4hands44/cmss13/commit/7f1e80ca3dd4800f54b5ff4dc3663dd1f804c28c)
#### Thursday 2022-12-22 02:26:13 by carlarctg

MIDIs are now either 'Meme' or 'Atmospheric', players can toggle each option (#1939)

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

Updated savefile number from 19 to 20. Meme and atmospheric preferences
are enabled by default.

Admin sounds now need a selection between 'Meme' or 'Atmospheric' type.
Ideally, this would let players decide if they want to listen to hijack
or first drop songs without needing to listen to GOOD HITS or whatnot.

I am uncertain about the savefile bit of code. I don't fully understand
it.

As stated I don't care about GBP, so if the tags are teechnicallly
incorrect go ahead and change them or whatever.

# Explain why it's good for the game

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->

> Admin sounds now need a selection between 'Meme' or 'Atmospheric'
type. Ideally, this would let players decide if they want to listen to
hijack or first drop songs without needing to listen to GOOD HITS or
whatnot.

As it says. Lots of people hate the memes and just want to listen to the
cool atmosphere. This is of course dependant on staff selecting the
right option, which is sometimes up to opinion, but I fully trust staff
will be able to handle this subjective affair correctly.

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
refactor: Updated savefile number from 18 to 19. Meme and atmospheric
preferences are enabled by default.
admin: Admin sounds now need a selection between 'Meme' or 'Atmospheric'
type. Ideally, this would let players decide if they want to listen to
hijack or first drop songs without needing to listen to GOOD HITS or
whatnot.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

Co-authored-by: Stan_Albatross <66756236+stanalbatross@users.noreply.github.com>

---
## [vdavalon01/cockroach](https://github.com/vdavalon01/cockroach)@[8ae602660d...](https://github.com/vdavalon01/cockroach/commit/8ae602660d16be76331c6705b748eb3ba7799cb0)
#### Thursday 2022-12-22 02:29:42 by craig[bot]

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
## [LovliestPlant/Skyrat-tg](https://github.com/LovliestPlant/Skyrat-tg)@[81ca11b95a...](https://github.com/LovliestPlant/Skyrat-tg/commit/81ca11b95a59d5cf0eb0a066454b2903f4859503)
#### Thursday 2022-12-22 02:43:13 by SkyratBot

[MIRROR] Basic Mob Carp: Retaliate Element [MDB IGNORE] (#18030)

* Basic Mob Carp: Retaliate Element (#71593)

## About The Pull Request

Adds an Element and AI behaviour intended to replicate the "retaliate"
behaviour which made up an entire widely-populated subtype of simple
mobs.
The behaviour is pretty simply "If you fuck with me I fuck with you".
Mobs with the component will "remember" being attacked and will try to
attack people who attacked them, until they lose sight of those people.
They don't have very long memories so breaking line of sight is enough
to remove you from their grudge list.
The implementation unfortunately requires registering to 600 different
"I have been attacked by X" signals but c'est la vie.

It will still be cleaner than
`/mob/living/simple_animal/hostile/retaliate/clown/clownhulk/honcmunculus`
and `mob/living/simple_animal/hostile/retaliate/bat/sgt_araneus`.

I attached it to the pig for testing and left it there because out of
all the farm animals we have right now, a pig would probably get pissed
off if you tried to kill it. Unfortunately it's got a sausage's chance
in hell of ever killing anyone.

## Why It's Good For The Game

It doesn't have much purpose yet but as we make more basic mobs this is
going to see a **lot** of use.

## Changelog

:cl:
add: Basic mobs have the capability of being upset that you kicked and
punched them.
add: Pigs destined for slaughter will now ineffectually attempt to
resist their fate, at least until they lose sight of you.
balance: Bar bots are better at noticing that you're trying to kill
them.
/:cl:

* Basic Mob Carp: Retaliate Element

Co-authored-by: Jacquerel <hnevard@gmail.com>
Co-authored-by: tastyfish <crazychris32@gmail.com>

---
## [sec-js/thefuck](https://github.com/sec-js/thefuck)@[7f97818663...](https://github.com/sec-js/thefuck/commit/7f97818663de9351ac7e2c6314ed94184811d62a)
#### Thursday 2022-12-22 03:35:55 by Romain Heller

#455: [README] Add uninstall instructions (#1171)

* ~[Doc] Add Uninstall instructions

As we need the package and to modify the shell config, users could have a pain in the ass when it comes to retire *The Fuck* from the system.

* Update README.md

* Update README.md

Co-authored-by: Pablo Aguiar <scorphus@gmail.com>

---
## [carlarctg/cmss13](https://github.com/carlarctg/cmss13)@[15af7f1ee5...](https://github.com/carlarctg/cmss13/commit/15af7f1ee5e7dbd568ea01b53c993e127b4bdb12)
#### Thursday 2022-12-22 03:36:56 by ThePiachu

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
## [carlarctg/cmss13](https://github.com/carlarctg/cmss13)@[229a2e6ed2...](https://github.com/carlarctg/cmss13/commit/229a2e6ed24998b2b97421ae421cfe25b77ae1b1)
#### Thursday 2022-12-22 03:40:57 by Stan_Albatross

Teleporter tgui and minor refactor (#1997)

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

converts teleporters to tgui and removes some shitcode

# Explain why it's good for the game

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->

fuck nanoui


![image](https://user-images.githubusercontent.com/66756236/208460209-8f260838-1da1-49af-8d6c-44efcc974efb.png)


![image](https://user-images.githubusercontent.com/66756236/208458960-7bd162fd-e2fe-4c23-a3f6-257cb73516f5.png)


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
ui: swapped teleporters to use tgui.
fix: teleporter consoles now have actual sprites!
code: "improved" some teleporter code.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

Co-authored-by: Stan_Albatross <swt91a@gmail.com>
Co-authored-by: harryob <me@harryob.live>

---
## [sec-js/Sparrow](https://github.com/sec-js/Sparrow)@[89f6b1e732...](https://github.com/sec-js/Sparrow/commit/89f6b1e732cf62be596195f49136f11b2fbabbb0)
#### Thursday 2022-12-22 03:59:48 by Nick Carr

Removal of Azure AD UserAuthenticationMethod 16457 logic

❌ 1⃣️6⃣️4⃣️5⃣️7⃣️
Having investigated this threat actor activity for quite some time, we have certainly found investigative utility in surfacing anomalous AAD authentications¹.
However, in our experience, only a subset of confirmed threat actor activity was associated with UserAuthenticationMethod 16457 - and even in those environments, other threat actor authentication methods were observed. The value, 16457, is driven by flags set providing context that isn't intended to have global meaning.

**Most importantly**, this 16457 value is *very common* globally and is unlikely to result in meaningful discovery of threat actor activity is isolation (without comparing it with the realm config or otherwise baselining an environment). Put simply, its value as an indicator is limited and tenant-specific - and **its inclusion is likely generating false positives & questions for Sparrow users.**

After thoroughly exploring its meaning & its global prevalence with internal teams in December, we removed the 16457 value from remaining internal hunting logic (and didn't release it in public Azure Sentinel logic). I recommend you consider removing it from this tool and from the text of Alert [AA21-008A](https://us-cert.cisa.gov/ncas/alerts/aa21-008a) as well.

Note: I see that @DeemOnSecurity acknowledged this value was [originally intended](https://github.com/cisagov/Sparrow/issues/20#issuecomment-754842442) as a potentially anomalous event in Issue #20 - but that nuance appears to have been lost on the broad user base. If replacement logic is desired, I expect our organizations can work together on alternate solutions!

Thanks in advance; and as an ex-CISA employee myself, I appreciate the development & release of actionable tools. Awesome stuff!
[-YOUR BOY CARR](https://twitter.com/ItsReallyNick)

¹ [Understanding "Solorigate"'s Identity IOCs](https://techcommunity.microsoft.com/t5/azure-active-directory-identity/understanding-quot-solorigate-quot-s-identity-iocs-for-identity/ba-p/2007610)

---
## [walternewtz/android_kernel_xiaomi_sdm845](https://github.com/walternewtz/android_kernel_xiaomi_sdm845)@[9287e0e1cf...](https://github.com/walternewtz/android_kernel_xiaomi_sdm845/commit/9287e0e1cfc06e48b211fef3a828cb9fc35016a6)
#### Thursday 2022-12-22 04:53:54 by tanish2k09

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
## [facebookincubator/reindeer](https://github.com/facebookincubator/reindeer)@[fbc4504671...](https://github.com/facebookincubator/reindeer/commit/fbc45046719699a1aacf763ddba7640f607ffcd3)
#### Thursday 2022-12-22 05:01:51 by David Tolnay

Support buckify without an existing .cargo/config

Summary:
Previously `reindeer buckify` would fail with an error if `.cargo/config` was not present. That file is created by `reindeer vendor` based on the output printed by `cargo vendor`.

```
$ reindeer buckify
[ERROR reindeer] parsing metadata

Caused by:
  0: running cargo
  1: /data/users/$user/fbsource/third-party/rust/../../xplat/rust/toolchain/current/cargo metadata --format-version 1 --frozen --locked --offline --manifest-path /data/users/$user/fbsource/third-party/rust/Cargo.toml failed:
     error: failed to load source for dependency `aes-gcm-siv`

     Caused by:
       Unable to update https://github.com/lei2022/AEADs?rev=d9d03399fbc1347a1c2941801c0743e847980757#d9d03399

     Caused by:
       can't checkout from 'https://github.com/lei2022/AEADs': you are in the offline mode (--offline)
```

I am interested in making this work for 3 reasons:

1. In CI of https://github.com/dtolnay/cxx, I am interested in running `reindeer buckify` without `reindeer vendor`. I just want to confirm that the checked-in generated BUCK file is always up to date.

2. In particular I do not want to run `reindeer vendor` because it is slow. The way it uses `.cargo` as the CARGO_HOME forces Cargo to clone a whole new crates.io index and all your git dependencies and download all the crate tarballs that might already be in your normal Cargo directory in your home directory. In fbsource, this currently amounts to 4.9 GB that it writes to `.cargo` on every invocation, and a bunch of network traffic. This diff is a step toward fixing `vendor` to not work this way.

3. I want to experiment with *"just delete third-party/rust/.cargo"* as the magic solution to all `git`-related `cargo vendor`-related headaches.

The content of `.cargo/config` is 100% redundant with `Cargo.lock` and can be generated from `Cargo.lock`, which is what this diff does. My suspicion is that in general, workflows that involve Cargo changing `Cargo.lock` are way more robust in Cargo than workflows that involve Cargo changing `.cargo/config`, especially when it comes to git dependencies. We'll be better off moving off of reliance on a checked-in `.cargo/config`, and instead only generating an ephemeral one from `Cargo.lock` when needed.

Reviewed By: zertosh

Differential Revision: D42203704

fbshipit-source-id: 3dd5f422e7e21e43b671eb397e490c0ce094ed9b

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[a2d550ced9...](https://github.com/treckstar/yolo-octo-hipster/commit/a2d550ced90bf61b7ffe5d14f1d33163603a3653)
#### Thursday 2022-12-22 05:22:04 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [cedricai/guava](https://github.com/cedricai/guava)@[8a676ade61...](https://github.com/cedricai/guava/commit/8a676ade617c6be992165cd0658779a14acef2f2)
#### Thursday 2022-12-22 05:41:36 by cpovirk

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
## [rust-lang-ci/rust](https://github.com/rust-lang-ci/rust)@[8d3e345aa8...](https://github.com/rust-lang-ci/rust/commit/8d3e345aa88d91f3e68460bb35b887de6e5646c1)
#### Thursday 2022-12-22 05:41:48 by bors

Auto merge of #105114 - saethlin:mir-opt-ub-asserts, r=<try>

Tweak MIR inline cost estimation and assert_unsafe_precondition so they inline in MIR

It turns out that https://github.com/rust-lang/rust/pull/104121 does not actually achieve what `@Lokathor` wanted, when debug assertions are enabled. In my opinion there are really multiple issues here, this PR addresses all of them:

The implementation of `is_aligned_and_not_null` is compiled to a shocking amount of MIR, because the implementation of `ptr::is_null` is contorted to work in `const fn`, and the implementation of `ptr::is_aligned` is based on `ptr::is_aligned_to` which among other things has a check that the alignment is a power of 2. These of course clean up quite nicely in LLVM... but the goal here is to enable inlining _before_ we get to LLVM.

Then some of the helper functions aren't `#[inline]`. The MIR inliner only inlines `#[inline]` functions at `-Zmir-opt-level=2`, which is what `--release` corresponds to. Whether or not that heuristic should be loosened up, these are good candidates for inlining so I don't see any harm in adding the attribute.

Then the MIR inlining cost estimation seems a bit pessimistic to me. The MIR we generate tends to have a lot of assignments from locals to locals. By eye it looks like a lot of these could be erased by another optimization pass, so I don't think they represent nearly the complexity of any other instruction. For now, this excludes them from cost estimation entirely.

I also removed the extra function call penalty from diverging call terminators. My logic there is that a diverging terminator is often a panic path, and those sometimes (and especially in this case) have a predicate which can be statically reasoned about. There is a fair chance that inlining a function with a diverging terminator will result in optimizing away the divergence entirely, or making other optimizations after the diverging path, based on assume its predicate. (I'm aware that currently MIR opt is not very good at this sort of cleanup, so this is somewhat of a gamble)

(I hope this looks good in perf...)

r? `@cjgillot`
cc `@JakobDegen`

---
## [morgoth1145/advent-of-code](https://github.com/morgoth1145/advent-of-code)@[25b4d9f04a...](https://github.com/morgoth1145/advent-of-code/commit/25b4d9f04a349d155b793cd486bb086406d51b8a)
#### Thursday 2022-12-22 06:15:33 by Patrick Hogg

2022 Day 22 Part 1

That's annoying, the input is set up such that my grid parser can't parse it! Oh well, I got the grid parsing done quick enough, as well as splitting the path into segments. After that it's just a straightforward problem of following the instructions on this wonky grid and finding the wraparound point when we fall off. Honestly, the trickiest bit was making sure that I got my rotations right!

I felt like I was slow but I was 21st! That's not too bad!

---
## [ThePainkiller/sojourn-station](https://github.com/ThePainkiller/sojourn-station)@[7b4730215b...](https://github.com/ThePainkiller/sojourn-station/commit/7b4730215b80f33122c346343bc7d9178483a4fc)
#### Thursday 2022-12-22 06:28:03 by DimmaDunk

Bugfixes and a drink (#4246)

* Bugfixes and a drink

- Ports Eris combat hardsuit sprites by assortedbeads (PR #7925)
- Fixes people seeing what you examine from your hud, adds tips on HUD descriptions when examined (Eris PR #7929)
- Leftover wooden STS-25 removed (sprite was the same as polymer stock, but were identical guns), replaced every intance with the original STS-25
- renames "sawn off" to "short-barreled" in cases of carbines and rifles
- Hypersleeper now consumes more power, Tricordazine removed from it as it conflicts with sleeper upgrades
- Fixes invisible hypersaw and doombringer saw when turned on, adds animated sprites when dual wielding them
- Fixes the long bug of shoes' icons getting "cleaned" from blood and oil whenever you stored a knife on them, for good
- Corrects strength values on certain drinks, a reminder that LOWER numbers mean STRONGER alcohols
- New drink: Jager bomb, made with equal parts Fernet and Claw Energy Drink
- Fixes certain alcohols not properly applying ethanol ingest procs
- Adds two bottles of cream to the church's fridge, moves the rolling pin from the fridge to the table nearby

* STS carbine refactor

To not cheat crafting menus

* RIG description fixes

It's a hardsuit, not a voidsuit
Also deletes a duplicate custodian armor sprite

* ADMS and Xenobio changes

- ADMS sprite no longer just entirely purple
- Eliminates the chute from xenobio going absolutely NOWHERE

* Hyper sleeper nerf

- Locks hypersleeper board behind advanced chemistry and portable biotech research node (renamed to accomodate for it)
- Deletes hypersleeper board from CBO locker
- Many typo fixes and description fixes

* Nevermind

Turns out it's better to not have printable hypersleepers as they're meant to be "one of a kind"

* Update code/modules/reagents/reagents/food-Drinks.dm

Co-authored-by: Trilbyspaceclone <30435998+Trilbyspaceclone@users.noreply.github.com>

---
## [LittleBuilderJane/Nyanotrasen](https://github.com/LittleBuilderJane/Nyanotrasen)@[82755da1b8...](https://github.com/LittleBuilderJane/Nyanotrasen/commit/82755da1b89eb4b5ff99f9f278f5702cd3836750)
#### Thursday 2022-12-22 06:50:08 by Rane

OKAY FINE I'LL DO IT (#685)

* HOLY FUCKING SHIT MOFF!!!!!

* mail receiver

* convert some of the mechanics to nyano standard

Co-authored-by: PixelTheKermit <85175107+PixelTheKermit@users.noreply.github.com>

---
## [BrynGhiffar/pj_projectservice](https://github.com/BrynGhiffar/pj_projectservice)@[8d0238c8ce...](https://github.com/BrynGhiffar/pj_projectservice/commit/8d0238c8cebbc07200e4ea98c63180b7302b7d54)
#### Thursday 2022-12-22 07:31:04 by Bumskee

fixed the stupid ass bug it was all just because of cursor type object is messing with our fucking workflow

---
## [NovaUniverse/NovaCore](https://github.com/NovaUniverse/NovaCore)@[852482cd5d...](https://github.com/NovaUniverse/NovaCore/commit/852482cd5d54e19cb7afafba567ac277f8a54326)
#### Thursday 2022-12-22 07:35:08 by BrunoGamerGH

FUCK YOU, THIS HAS BEEN ANNOYING ME FOR ALMOST 3 MONTHS ALREADY, I DONT CARE IF ITS A 1 CHARACTER CHANGE, FUCK YOU, YOU MADE ME DO THIS.

---
## [Dantesousa/Nebula13-Reborn](https://github.com/Dantesousa/Nebula13-Reborn)@[1c76ea5334...](https://github.com/Dantesousa/Nebula13-Reborn/commit/1c76ea533439dcd7fca15a2dd500a44dc6158883)
#### Thursday 2022-12-22 07:37:02 by SkyratBot

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
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[8cb4947084...](https://github.com/tgstation/tgstation/commit/8cb4947084edffc9476c40ea6283b68e818f48bd)
#### Thursday 2022-12-22 08:41:38 by Jacquerel

AI actions won't unassign each other's movement targets & Mice stop being scared of people if fed cheese  (#72130)

## About The Pull Request

Fixes #72116 
I've had a persistent issue with basic mob actions reporting this error
and think I finally cracked it
When replanning with `AI_BEHAVIOR_CAN_PLAN_DURING_EXECUTION` it can run
`Setup` on one action leading to the plan changing, meaning that it runs
`finishCommand` to cancel all other existing commands
If you triggered a replan by setting up a movement action in the middle
of another movement action, cancelling the existing action would remove
the target already set by the current one.
We want actions to be able to remove _their own_ movement target but not
if it has been changed by something else in the intervening time.

I fixed this by passing a source every time you set a movement target
and adding a proc which only clears it if you are the source... but this
feels kind of ugly. I couldn't think of anything but if you have a
better idea let me know.

Also while I was doing this I turned it into a feature because I'm
crazy.
If you feed a mouse cheese by hand it will stop being scared of humans
and so will any other mice it attracts from eating more cheese. This is
mostly because I think industrial mouse farming to pass cargo bounties
is funny.
Mice controlled by a Regal Rat lose this behaviour and forget any past
loyalties they may have had.


https://user-images.githubusercontent.com/7483112/208779368-3bd1da0f-4191-4405-86e5-b55a58c2cd00.mp4

Oh also I removed a block about cancelling if you have another target
from the "hunt" behaviour, everywhere using this already achieves that
simply by ordering the actions in expected priority order and it was
messing with how I expected mice to work.
Now if they happen to stop by some cheese they will correctly stop
fleeing in order to eat it before continuing to run away.

## Why It's Good For The Game

Fixes a bug I kept running into.
Makes it possible to set up a mouse farm without them screaming
constantly.
Lets people more easily domesticate mice to support Ratatouille
gameplay.

## Changelog

:cl:
add: Mice who are fed cheese by hand will accept humans as friends, at
least until reminded otherwise by their rightful lord.
fix: Fixed a runtime preventing mice from acting correctly when trying
to flee and also eat cheese at the same time.
/:cl:

---
## [SLASHEM-Extended/SLASHEM-Extended](https://github.com/SLASHEM-Extended/SLASHEM-Extended)@[02ba0e45f5...](https://github.com/SLASHEM-Extended/SLASHEM-Extended/commit/02ba0e45f5c100a44a4c740a3085d9a6bd851511)
#### Thursday 2022-12-22 09:29:42 by AmyBSOD

Fucking HELL, devteam!

Why do they write such screwy code anyway? (Answer: because they love it when I have to fix it, since they know I always rage at them!)

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[06e14559a6...](https://github.com/mrakgr/The-Spiral-Language/commit/06e14559a685137365ed46932f379bace2ae4064)
#### Thursday 2022-12-22 11:57:20 by Marko Grdinić

"10:50am. I had trouble falling asleep. Yesterday's session overstressed me and it looked as if I was going to spend the night without rest, but I managed to cast away my goals for the night and fall into dream. I woke up early, and managed to fall asleep yet again. This is a remarkable success in self control for me, though I really should chill for a while.

Any replies? Not yet. The UPMEM compiler lead is really giving his sweet time at answering how to get full memory range. Let me remind him.

///

Hello, how are you? I've been waiting for you to get back to me on those questions and am sending you this email as a reminder.

What is your current status? Right now, I myself am done with the Python backend and will begin work on integrating the two prototypes in the 'UPMEM Demo Python + C' backend. This won't be more than a few days of work and after that I'll have to start writing programs for it, and that is when I will want to know how to go beyond 4gb with flexible arrays.

Right now, it seems impossible given the API constraints, but unlike you, it is not like I myself know much about them, so I desire to be educated in the way that this works.

///

11am. Kumo and Savage Fang are out so let me have them. Yesterday night I've resumed Rance Quest, so I also have the Kanami scene waiting for me. I am the part when I have to level up a bunch of weaklings to lvl 35 so I can H them. Yesterday I managed to get Kanami to that point and have decided to save her up.

11:50am. Let me...well, let me just check out the join points. Then I will do the usual breakfast and chores combo.

```fs
type JoinPointKey =
    | JPMethod of E * ConsedNode<RData [] * Ty []>
    | JPClosure of E * ConsedNode<RData [] * Ty [] * Ty * Ty>
```

It is finally time to add another key.

```fs
type JoinPointKey =
    | JPMethod of E * ConsedNode<RData [] * Ty []>
    | JPClosure of E * ConsedNode<RData [] * Ty [] * Ty * Ty>
    | JPBackend of E * ConsedNode<RData [] * Ty []> * backend: string
```

No actually the backend does not matter at all to the partial evaluator.

```fs
type JoinPointKey =
    | JPMethod of E * ConsedNode<RData [] * Ty []>
    | JPClosure of E * ConsedNode<RData [] * Ty [] * Ty * Ty>
    | JPBackend of E * ConsedNode<RData [] * Ty []>
```

So then how about I do it like this.

...Thugh at the same time I do not have much else to put it. I do not want another `TyJoinPoint` in the language.

```fs
| EJoinPoint'(r,scope,body,annot) ->
```

Also the join points need the scope now.

```fs
and [<ReferenceEquality>] E =
    | EFun of Range * Id * E * T option
    | EFun' of Range * Scope * Id * E * T option
    | EForall of Range * Id * E
    | EForall' of Range * Scope * Id * E
    | ERecursiveFun' of Range * Scope * Id * E ref * T option
    | ERecursiveForall' of Range * Scope * Id * E ref
    | ERecursive of E ref // For global mutually recursive functions
    | EPatternRef of E ref
    | EJoinPoint of Range * E * T option
    | EJoinPoint' of Range * Scope * E * T option
    | EB of Range
    | EV of Id
    | ELit of Range * Tokenize.Literal
    | EDefaultLit of Range * string * T
    | ESymbol of Range * string
    | EType of Range * T
    | EApply of Range * E * E
    | EArray of Range * E list * T
    | ETypeApply of Range * E * T
    | ERecBlock of Range * (Id * E) list * on_succ: E
    | ERecordWith of Range * (Range * E) list * RecordWith list * RecordWithout list
    | EModule of Map<string, E>
    | EOp of Range * BlockParsing.Op * E list
    | EPatternMiss of E
    | ETypePatternMiss of T
    | EAnnot of Range * E * T
    | EIfThenElse of Range * E * E * E
    | EIfThen of Range * E * E
    | EPair of Range * E * E
    | ESeq of Range * E * E
    | EHeapMutableSet of Range * E * (Range * E) list * E
    | EReal of Range * E
    | EMacro of Range * Macro list * T
    | EPrototypeApply of Range * prototype_id: GlobalId * T
    | EPatternMemo of E
    | ENominal of Range * E * T
    // Regular pattern matching
    | ELet of Range * Id * E * E
    | EUnbox of Range * Id * E * E
    | EPairTest of Range * bind: Id * pat1: Id * pat2: Id * on_succ: E * on_fail: E
    | ESymbolTest of Range * string * bind: Id * on_succ: E * on_fail: E
    | ERecordTest of Range * PatRecordMember list * bind: Id * on_succ: E * on_fail: E
    | EAnnotTest of Range * T * bind: Id * on_succ: E * on_fail: E
    | EUnitTest of Range * bind: Id * on_succ: E * on_fail: E
    | ENominalTest of Range * T * bind: Id * pat: Id * on_succ: E * on_fail: E
    | ELitTest of Range * Tokenize.Literal * bind: Id * on_succ: E * on_fail: E
    | EDefaultLitTest of Range * string * T * bind: Id * on_succ: E * on_fail: E
    | ETypecase of Range * T * (T * E) list
```

Looking at this again is making me realize the true complexity of what I've created.

```fs
    | EBackend of Range * E * string
    | EBackend' of Range * Scope * E * string
```

I think that for once it is time to extend the language. I am wondering whether to give a type to the join point...

```c
#include <stdio.h>

int main() {
    printf("Hello World!\n");
    return 0;
}
```

Yeah, unlike Cuda, UPMEM has a return type.

You know what, I won't add a new clause to the language.

```fs
    | EJoinPoint of Range * E * T option * backend: string
    | EJoinPoint' of Range * Scope * E * T option * backend: string
```

Hmmm...

```fs
    | EJoinPoint of Range * E * T option * backend: string
    | EJoinPoint' of Range * Scope * E * T option
    | EBackend' of Range * Scope * E * T option * backend: string
```

Let do it like this.

12:20pm.

```fs
    | EJoinPoint of Range * E * T option * backend: string
    | EJoinPoint' of Range * Scope * E * T option * backend: string
```

Actually, let me prototype them first like this.

```fs
        | EJoinPoint'(r,scope,body,annot,backend) ->
            let env_global_type = Array.map (vt s) scope.ty.free_vars
            let env_global_term = Array.map (v s) scope.term.free_vars

            let dict, hc_table = Utils.memoize join_point_method (fun _ -> Dictionary(HashIdentity.Structural), HashConsTable()) body
            let call_args, env_global_value = data_to_rdata hc_table env_global_term
            let join_point_key = hc_table.Add(env_global_value, env_global_type)

            let ret_ty =
                match dict.TryGetValue(join_point_key) with
                | true, (_, Some ret_ty) -> ret_ty
                | true, (_, None) -> raise_type_error (add_trace s r) "Recursive join points must be annotated."
                | false, _ ->
                    let s : LangEnv = {
                        trace = r :: s.trace
                        seq = ResizeArray()
                        cse = [Dictionary(HashIdentity.Structural)]
                        i = ref 0
                        env_global_type = env_global_type
                        env_global_term = env_global_term
                        env_stack_type = Array.zeroCreate<_> scope.ty.stack_size
                        env_stack_term = Array.zeroCreate<_> scope.term.stack_size
                        }
                    let s = rename_global_term s
                    let annot = Option.map (ty s) annot
                    dict.[join_point_key] <- (None, annot)
                    let seq,ty = term_scope'' s body
                    dict.[join_point_key] <- (Some seq, Some ty)
                    annot |> Option.iter (fun annot -> if annot <> ty then raise_type_error s <| sprintf "The annotation of the join point does not match its body's type.Got: %s\nExpected: %s" (show_ty ty) (show_ty annot))
                    ty

            match backend with
            | null -> push_typedop_no_rewrite s (TyJoinPoint(JPMethod(body,join_point_key),call_args)) ret_ty
            | _ -> failwith "TODO"
```

I am looking at this, and the information that I need for the backend join point matched the method one perfectly.

12:35pm.

```fs
                let method_name = push_typedop_no_rewrite s (TyJoinPoint(JPBackend(body,join_point_key,backend),call_args)) YB
                DPair(method_name, failwith "")
```

No, I do not like `TyJoinPoint` followed by `JPBackend`

I think I will remove `JPBackend`, and introduce `TyBackend` which merges what I need from both, but gets rid of the call_args. I simply do not need that info here.

`| JPBackend of E * ConsedNode<RData [] * Ty []> * backend: string`

Let me back this up.

```fs
            else
                let method_name = push_typedop_no_rewrite s (TyBackend(body,join_point_key,backend)) (YPrim StringT)
                DPair(method_name, failwith "")
```

Now I just need to turn call args into a record.

```fs
            if backend = null then push_typedop_no_rewrite s (TyJoinPoint(JPMethod(body,join_point_key),call_args)) ret_ty
            else
                let method_name = push_typedop_no_rewrite s (TyBackend(body,join_point_key,backend)) (YPrim StringT)
                let call_args = call_args |> Array.map (fun (L(i,_) as v) -> $"v{i}", DV v) |> Map.ofArray |> DRecord
                DPair(method_name, call_args)
```

Perfect. In fact...

```fs
                let method_name = push_typedop_no_rewrite s (TyBackend(body,join_point_key,backend)) (YPrim StringT)
                let call_args = call_args |> Array.map (fun (L(i,_) as v) -> string i, DV v) |> Map.ofArray |> DRecord
                DPair(method_name, call_args)
```

How about I do it like this just in case I run into some crazy backend like LLVM in the future?

```fs
                let method_name = push_typedop_no_rewrite s (TyBackend(body,join_point_key,backend)) (YPrim StringT)
                let call_args = Array.foldBack (fun v s -> DPair(DV v,s)) call_args DB
                DPair(method_name, call_args)
```

Let me do it like this after all. This way is the most hassle free. I won't have to go back and make any changes to the join point.

12:55pm. Let me close here. In the later session I will extend the parser and fix all the errors.

This is not hard work at all, I just need to think it through a little. The past me did all the hard stuff already."

---
## [SmoSmoSmoSmok/fulpstation](https://github.com/SmoSmoSmoSmok/fulpstation)@[ca0fedc60f...](https://github.com/SmoSmoSmoSmok/fulpstation/commit/ca0fedc60f17f19520b8fa064c396129ad68b633)
#### Thursday 2022-12-22 12:11:16 by John Willard

Sol is now a Subsystem, Coffins lock themselves, Bloodsuckers don't constantly die, probably (#862)

* Turns Sol into a Subsystem & Many more

Turns Sol into a subsystem and hooks Bloodsuckers onto it via signals instead of doing a ton of for() loops anywhere. This made Sol incredibly fucking fast, so I halved the speed so it only ticks every 2 seconds.

I also improved the sunlight hud to update with regular bloodsucker updates to avoid some useless proc overhead and fixed Coffins not locking by themselves.

* Torpor now ends, moves exiting torpor to its proper place

* round it

* fix comment

* fix CI

---
## [shreyasjoshi2908/projects](https://github.com/shreyasjoshi2908/projects)@[98bd040c7c...](https://github.com/shreyasjoshi2908/projects/commit/98bd040c7cc2d83d27635772e2609571f753ab8c)
#### Thursday 2022-12-22 12:24:02 by shreyasjoshi2908

Add files via upload

We now live in what some call the “era of abundance”. For any given product, there are sometimes thousands of options to choose from. Think of the examples above: streaming videos, social networking, online shopping; the list goes on. Recommender systems help to personalize a platform and help the user find something they like. The easiest and simplest way to do this is to recommend the most popular items. However, to really enhance the user experience through personalized recommendations, we need dedicated recommender systems. 
Here I have content-based recommender system that will automatically retrieve data based on content which end users searches.

---
## [Jacquerel/orbstation](https://github.com/Jacquerel/orbstation)@[7687a28e7c...](https://github.com/Jacquerel/orbstation/commit/7687a28e7ceecea6b9e0aacdb58a2271b063f9d3)
#### Thursday 2022-12-22 12:51:56 by Sol N

refreshes syndi-kits and syndicate surplus crates, introduces shared limited stock (#71869)

## About The Pull Request

After all, the Syndicate loves a good throwback.


![C6O47fPhAB](https://user-images.githubusercontent.com/116288367/207737104-3d24574f-02e0-433d-8ea7-6825ca4cb970.png)

This PR does a few things with the goal of reimplementing and
revitalizing syndicate traitor kits and the syndicate surplus crate.
Of note is that I have added in a way for limited stock items to share
their limited stock.

Following maintainer guidance the syndicate traitor kits have increased
in price and as a result some of the lower value ones have been
adjusted. I've given all active bundles current TC costs per item
knowing full well they will be inaccurate eventually.

<details>
  <summary>Changes as a result of my audit of syndikits</summary>
    
### UNCHANGED
Recon, Spai, Stealthy, Screwed, Sniper, Nukie Meta, Implants
Mad Scientist, Bees

Lord Singuloth is also unchanged and disabled, I think that it should
turn into a new supermatter themed kit maybe. outside of current scope.

### Gun Kit
Replaced emag with doorjack and gave it a chameleon holster, literally
moved 1 tc elsewhere

### Murderer
replaced emag again, no additions its a lot of tc and Just Good

### Hacker
added doorjack, otherwise unchanged

### Sabotage
no changes other than adding in extra bombs it didnt have

### James Bond
gave him some gadgets with the freedom implant, emp flashlight, and one
x4. also a cyanide pill and deck of cards for fun

### Ninja
Added in miner Jump Boots, smoke spell, and doorjack. dont just want it
to be space ninja

### Dark Lord
Added in new lightning bolt spell granter and made the desword default
to red. probably overbudget.

### White Whale
dehydrated carp added so you can ride it alongside the ones you grenade
out. hard to imagine changing this

### Mr Freeze
changed temperature gun to be cryo only so that i could give him the
cryo thermal pistol. cold attacks only.

### 2006 Traitor
doorjack.

</details> 

tl;dr theyre all about 30 tc worth of shit more or less some are more
but thats what rarity should be for
you can only buy from one type of syndicrate per round


![QOF1WO7CC6](https://user-images.githubusercontent.com/116288367/207739417-00ae6b81-b6aa-4774-a4bb-f2d880988ff4.gif)

Next up is the return of the surplus crate. 
Crate is generated, gives you gear **based on your progression at the
time of buying the crate**, you can use it all at the start and get some
chameleon kits and not a lot of dangerous weapons or wait till later.
I've changed the weight on some items here and there and given weight to
role and species locked items, though I will admit that latter is
unimportant because I set moth lanterns to be unable to appear in these
two crates.


![dreamseeker_t8abXysKqK](https://user-images.githubusercontent.com/116288367/206761978-96e2a51e-f9a5-48e4-a863-a9198fa15ea2.gif)

But who cares about that your eyes instantly went to the United Surplus
Crate and the United Surplus Key lets be honest.

The united surplus crate is 80 TC worth of uplink items relative to your
current progression when you purchase it and gives you a locked box. It
**will explode if you try to break it** so be careful with it. It gives
you 80 TC and costs 20 TC because it is impossible to open without key.
The rub of course is that the Syndicate forbids agents from buying more
than one surplus item of any kind, you need to find another traitor and
make them buy you a key to open your box. Or I guess you can share the
box?


![dreamseeker_ts0AZeiyfy](https://user-images.githubusercontent.com/116288367/207740388-3f688bba-5d71-48d2-8079-671bbed7e54e.gif)

Regardless, if the crate is opened with any other means it doesn't spawn
its contents, you need 2 traitor uplinks.
Both of these items have a 30 minute timer because you don't want a
crate that has 5 emp flashlights in it. You at least want one energy
sword.

I did a lot of code shit and changed various things to be proc based to
allow for more editing and interjection of things, as I wrote in code
comments making a crate thats locked to a specific set of progression
just means changing the proc that generates a list of valid uplink items
to check items' progression values to a specified value instead of your
characters progression.

Ok I think that goes over everything more or less????

## Why It's Good For The Game

I've heard that people liked these and I think they are quite fun, being
able to go from "i dunno what to do as a traitor" to "ah, of course, I
will become the Bombler" is a fun thing to be able to have, and people
like to get a bunch of random shit in the mail. Some of it even feels
free!!!!!!!!!!!!!!!!!!! Brain points go up!!!

The division of procs allows for more creativity with this system than
existed before as well as other possibilities for interacting with the
uplink handler in funny ways.

## Changelog

:cl:
add: the syndicate is once again distributing syndi-kits, some now with
new technology
add: a fresh batch of syndicate surplus crates have been sent out,
though they seem a bit lighter than before
add: in an effort to encourage cooperation, a traitor can now purchase
either the new United Surplus Syndicate Crate or its key, but not both
add: lightning bolt book granter for wizard event and one syndie-kit
bundle
add: temperature gun that only makes things colder for one syndie-kit
bundle
code: it is now possible to have uplink items share limited stock
bal: role-restricted items no longer can be delivered by the stray
syndicate drop pod event
/:cl:

---
## [Jacquerel/orbstation](https://github.com/Jacquerel/orbstation)@[6dd4839ef3...](https://github.com/Jacquerel/orbstation/commit/6dd4839ef321aa0a997549d1ae07fe7ccbba59ed)
#### Thursday 2022-12-22 12:51:56 by carshalash

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
## [Jacquerel/orbstation](https://github.com/Jacquerel/orbstation)@[00e7d5d746...](https://github.com/Jacquerel/orbstation/commit/00e7d5d7465211ccf0e3d604e566e2c08775cd20)
#### Thursday 2022-12-22 12:51:56 by GoldenAlpharex

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
## [Jacquerel/orbstation](https://github.com/Jacquerel/orbstation)@[9e69e5d6ac...](https://github.com/Jacquerel/orbstation/commit/9e69e5d6acae10bf0941155c418ea3b9194668e5)
#### Thursday 2022-12-22 12:58:09 by LemonInTheDark

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
## [SanjayrajD/C-Training-course](https://github.com/SanjayrajD/C-Training-course)@[eb1b95c30f...](https://github.com/SanjayrajD/C-Training-course/commit/eb1b95c30f3b02f92e5889964fcca6a8ed0b851a)
#### Thursday 2022-12-22 13:39:54 by Sanjayraj D

Create Team Flash

A young man named Diffny leaves home to travel to California, to join the Team Flash. Although Diffny is not able to join this elite team immediately, he befriends the three most formidable members of the age: Joe, Ramsey and vixon and gets involved in affairs of the state and court.At that time, the Villan was planning to dethrone the king and to take the kingdom and to remove the Team Flash of the guard. Since the Villan has spies mixed with the local public , Diffny decides to send a message of his whereabouts to the team Flash in unique way.He gave a note to a boy which has the following message. I am at the midpoint of the line joining the farmhouse next to the palace and the light house. The Team Flash were puzzled. Can you help them find out the location of Diffny?Given the coordinates of the 2 places (x1,y1) and (x2,y2), write a program to find the location of Diffny.

Input & Output Format:

Input consists of 4 integers.

First value consists of x1.

Second value consists of y1.

Third value consists of x2.

Fourth value consists of y2.

Output consists of two float values.

Sample Input
2

4

10

15

Sample Output


6.0
9.5

---
## [zkldi/bms-table-loader](https://github.com/zkldi/bms-table-loader)@[29abd1e0a9...](https://github.com/zkldi/bms-table-loader/commit/29abd1e0a9b5e1fb33e71aba1cd56c61316259dc)
#### Thursday 2022-12-22 13:59:36 by zkldi

feat: enforce checksum correctness

OMG CORRECTNESS??!!! WHAT ARE YOU CRAZY??? OMG?

i'm tired man. i'm tired of all of these stupid ecosystems and these
shitty formats. i'm tired of having 99% of my problems be bms.

i'm tired of being mocked for caring about doing things properly when
i'm about the only fucking person who seems to do anything right around
here.

---
## [Amit91848/Rocket.Chat](https://github.com/Amit91848/Rocket.Chat)@[5a37518e42...](https://github.com/Amit91848/Rocket.Chat/commit/5a37518e42dec114e0ed1a71b5d103b4a62e9b58)
#### Thursday 2022-12-22 14:12:11 by Ben Wiederhake

[FIX] Client-generated sort parameters in channel directory  (#25768)

## Proposed changes (including videos or screenshots)
- In the web-client, sorting the channel directory by "Last Message" raises the error "Invalid sort parameter provided".

I don't think a screenshot is necessary, but if you'd like one anyway, here it is:

![Bildschirmfoto_2022-06-06_12-54-34](https://user-images.githubusercontent.com/2690845/172147996-e9942daf-6819-4eee-afa4-b1c6bce7a650.png)


## Issue(s)
Closes #25695

## Steps to test or reproduce

- Open the web client, i.e. navigate your browser to `https://rocketchat.$DOMAIN/home`
- Click the "Directory" button in the top left, (or just navigate directly to `https://rocketchat.$DOMAIN/directory/channels`)
- In the table header, click on "Last message" once
- In the table header, click on "Last message" again

Expected behavior: Clicking "Last message" turns on and then toggles sorting by the date of the last message, either first ascending and then descending, or the other way around.

Actual behavior: The first click sorts the messages in ascending order (good!), the second click shows a red warning box "FIXME", the table content disappears, and is replaced by throbbing grey placeholders.

### "Good" request (ascending order):

`https://rocketchat.domain.org/api/v1/directory?query=%7B%22type%22%3A%22channels%22%2C%22text%22%3A%22%22%2C%22workspace%22%3A%22local%22%7D&sort=%7B%22lastMessage%22%3A1%7D&count=25`

More easily readable GET parameters:

```
query | {"type":"channels","text":"","workspace":"local"}
sort | {"lastMessage":1}
count | 25
```

Response:
```
{"result":[{"_id":"AAAAAAAAAAAAAAAAA","name":"foobar","fname":"foobar","t":"c","usersCount":10,"ts":"2019-01-01T00:00:00.000Z","default":false,"lastMessage":{"_id":"AAAAAAAAAAAAAAAAA","rid":"AAAAAAAAAAAAAAAAA","msg":"Hello, World!","ts":"2019-01-01T00:00:00.000Z","u":{"_id":"AAAAAAAAAAAAAAAAA","username":"normaluser","name":"normaluser"},"unread":true,"_updatedAt":"2019-01-01T00:00:00.000Z","urls":[],"mentions":[],"channels":[]},"description":"Obviously, this JSON response is heavily censored."}],"count":25,"offset":0,"total":52,"success":true}
```

(Obviously, this JSON response is heavily censored, but you get the gist: It was successful.)

### "Bad" request (descending order):

`https://rocketchat.domain.org/api/v1/directory?query=%7B%22type%22%3A%22channels%22%2C%22text%22%3A%22%22%2C%22workspace%22%3A%22local%22%7D&sort=%7B%22lastMessage%22%3A0%7D&count=25`

More easily readable GET parameters:

```
query | {"type":"channels","text":"","workspace":"local"}
sort | {"lastMessage":0}
count | 25
```

Response:
```
{"success":false,"error":"Invalid sort parameter provided: \"{\"lastMessage\":0}\" [error-invalid-sort]","errorType":"error-invalid-sort","details":{"helperMethod":"parseJsonQuery"}}
```

## Further comments

Version on the server where I noticed this: `https://rocketchat.$DOMAIN/api/info` returns `{"version":"4.8","success":true}`. According to the "Releases" page, this version appeared 5 days ago, so I believe this is up to date.

### The journey to here

For some reason, the descending order uses the wrong magic number "0", and the server can't interpret that. However, this *used* to work, so I'm not very sure about this.

The error message appears in the source code of the entire organization exactly once: https://github.com/RocketChat/Rocket.Chat/blob/31ae30f30ad71d9e5a1b0cad494b3471a7dd8807/apps/meteor/app/api/server/helpers/parseJsonQuery.ts#L42
So I'll guess that this is the line of code that generated this particular message.

A few lines above we see that the server only knows 1 and -1 as magic numbers for the sorting:
https://github.com/RocketChat/Rocket.Chat/blob/31ae30f30ad71d9e5a1b0cad494b3471a7dd8807/apps/meteor/app/api/server/helpers/parseJsonQuery.ts#L35
This matches the observed bug: The browser sends 1 (which works) and 0 (which doesn't work).

Generally, it seems that the web client actually uses the strings "asc" and "desc" internally, which are hard to mix up. So I assume that it's the conversion of that is broken somehow.

Exactly this seems to be the case here:
https://github.com/RocketChat/Rocket.Chat/blob/31ae30f30ad71d9e5a1b0cad494b3471a7dd8807/apps/meteor/client/views/directory/hooks.js#L11

The code around it produces exactly the kind of query seen in the network log, and can also produce the buggy parameter `sort: 0`. This either fixes bug #25695, or a different bug of the same kind.

I am not sure how to add tests for this, can someone do this for me or show me where to start? I'm actually just an end-user and "accidentally" found the fix for the bug while writing the bug report ^^'

EDIT: Rebased for convenience, and to re-check CI.

---
## [SomeRandomOwl/tgstation](https://github.com/SomeRandomOwl/tgstation)@[75439c71f2...](https://github.com/SomeRandomOwl/tgstation/commit/75439c71f2282a3ae72b4ea35c80e27ca8556aaf)
#### Thursday 2022-12-22 14:14:42 by Mothblocks

Smoothing groups optimization, save 265ms with configs, more on production & w/ space ruins (#71989)

This one is fun.

On every /turf/Initialize and /atom/Initialize, we try to set
`smoothing_groups` and `canSmoothWith` to a cached list of bitfields. At
the type level, these are specified as lists of IDs, which are then
`Join`ed in Initialize, and retrieved from the cache (or built from
there).

The problem is that the cache only misses about 60 times, but the cache
hits more than a hundred thousand times. This means we eat the cost of
`Join` (which is very very slow, because strings + BYOND), as well as
the preliminary `length` checks, for every single atom.

Furthermore, as you might remember, if you have any list variable set on
a type, it'll create a hidden `(init)` proc to create the list. On
turfs, that costs us about 60ms.

This PR does a cool trick where we can completely eliminate the `Join`
*and* the lists at the cost of a little more work when building the
cache.

The trick is that we replace the current type definitions with this:

```patch
- smoothing_groups = list(SMOOTH_GROUP_TURF_OPEN, SMOOTH_GROUP_FLOOR_ASH)
- canSmoothWith = list(SMOOTH_GROUP_FLOOR_ASH, SMOOTH_GROUP_CLOSED_TURFS)
+ smoothing_groups = SMOOTH_GROUP_TURF_OPEN + SMOOTH_GROUP_FLOOR_ASH
+ canSmoothWith = SMOOTH_GROUP_FLOOR_ASH + SMOOTH_GROUP_CLOSED_TURFS
```

These defines, instead of being numbers, are now segments of a string,
delimited by commas.

For instance, if ASH used to be 13, and CLOSED_TURFS used to be 37, this
used to equal `list(13, 37)`. Now, it equals `"13,37,"`.

Then, when the cache misses, we take that string, and treat it as part
of a JSON list, and decode it from there. Meaning:

```java
// Starting value
"13,37,"

// We have a trailing comma, so add a dummy value
"13,37,0"

// Make it an array
"[13,37,0]"

// Decode
list(13, 37, 0)

// Chop off the dummy value
list(13, 37) // Done!
```

This on its own eliminates 265ms *without space ruins*, with the
combined savings of turf/Initialize, atom/Initialize, and the hidden
(init) procs that no longer exist.

Furthermore, there's some other fun stuff we gain from this approach
emergently.

We previously had a difference between `S_TURF` and `S_OBJ`. The idea is
that if you have any smoothing groups with `S_OBJ`, then you will gain
the `SMOOTH_OBJ` bitflag (though note to self, I need to check that the
cost of adding this is actually worth it). This is achieved by the fact
that `S_OBJ` simply takes the last turf, and adds onto that, meaning
that if the biggest value in the sorting groups is greater than that,
then we know we're going to be smoothing to objects.

This new method provides a limitation here. BYOND has no way of
converting a number to a string at compile time, meaning that we can't
evaluate `MAX_S_TURF + offset` into a string. Instead, in order to
preserve the nice UX, `S_OBJ` now instead opts to make the numbers
negative. This means that what used to be something like:

```dm
smoothing_groups = list(SMOOTH_GROUP_ALIEN_RESIN, SMOOTH_GROUP_ALIEN_WEEDS)
```

...which may have been represented as

```dm
smoothing_groups = list(15, MAX_S_TURF + 3)
```

...will now become, at compile time:

```dm
smoothing_groups = "15,-3,"
```

Except! Because we guarantee smoothing groups are sorted through unit
testing, this is actually going to look like:

```dm
smoothing_groups = "-3,15,"
```

Meaning that we can now check if we're smoothing with objects just by
checking if `smoothing_groups[1] == "-"`, as that's the only way that is
possible. Neat!

Furthermore, though much simpler, what used to be `if
(length(smoothing_groups))` (and canSmoothWith) on every single
atom/Initialize and turf/Initialize can now be `if (smoothing_groups)`,
since empty strings are falsy. `length` is about 15% slower than doing
nothing, so in procs as hot as this, this gives some nice gains just on
its own.

For developers, very little changes. Instead of using `list`, you now
use `+`. The order might change, as `S_OBJ` now needs to come first, but
unit tests will catch you if you mess up. Also, you will notice that all
`S_OBJ` have been increased by one. This is because we used to have
`S_TURF(0)` and `S_OBJ(0)`, but with this new trick, -0 == 0, and so
they conflicted and needed to be changed.

---
## [fengshuaihu/intellij-community](https://github.com/fengshuaihu/intellij-community)@[eaec1ec320...](https://github.com/fengshuaihu/intellij-community/commit/eaec1ec320ce8cbc7cb48f6f069ed7078ae9938c)
#### Thursday 2022-12-22 14:26:56 by Sergei Tachenov

[UI] IDEA-304712 Move appendInplaceComments to BGT update

The appendInplaceComments method used to be called on the EDT
during painting. It's potentially slow, and it's also a bad practice
to do any state computations during painting anyway.

Fix by moving the relevant logic into the node's update() and
appending the comments directly to PresentationData.

This turned out to be trickier than it seems. The Project view has a lot
of different node types, some of which are even in 3rd party plugins.
They all extend ProjectViewNode (except Rider that extends AbstractTreeNode).
However, it's not easy to put the logic there as it's a part of the lang-api module,
while the logic itself is in the lang-impl module. And logic doesn't belong to the API
module anyway.

The solution is, of course, dependency inversion, but it's not easy to inject a reference
to an interface into ProjectViewNode (let alone AbstractTreeNode) because
we have no control of how these objects are constructed.
Of course, it's possible to delegate this job to some parent or owner
object like the Project View Pane, for example. However, this creates unnecessary coupling
and would require some dirty hacks to get to those nodes and inject the needed references
into them.

Thankfully, most (if not all) Project View nodes that actually use inplace comments
extend AbstractPsiBasedNode, so we just put the actual comment producer there.

The new interfaces for this DI is InplaceCommentProducer (that produces the actual
comments) and InplaceCommentAppender that appends them (either to the presentation
when the new approach is used or to the renderer for the legacy case).

In case there are nodes that don't provide an inplace comment producer,
we still revert to the old logic. This has an unfortunate side effect of calling
getValue() on a node, which is the very potentially slow operation we're trying
to get rid of, but at least we now don't call it on AbstractPsiBasedNode anymore,
and those calls were probably the vast majority (if not all) slow operation calls.

One more trick involved is to convert the plain presentation's text (myPresentableText)
to the colored text before appending comments because many presentations don't
use colored text by default. Just appending comments would override the plain text
and, e.g., class and file names in the Project View would disappear. This is what the new
ensureColoredTextIsUsed() method in PresentationData is for.

GitOrigin-RevId: d7da0fc059d6d70ff369ea981501c5008b53b20d

---
## [odoo/runbot](https://github.com/odoo/runbot)@[c35b721f0e...](https://github.com/odoo/runbot/commit/c35b721f0ec7d01cb514f433567f6defc0b89576)
#### Thursday 2022-12-22 14:59:16 by Xavier Morel

[IMP] forwardport: gc/maintenance of local repo caches

The current system makes / lets GC run during fetching. This has a few
issues:

- the autogc consumes resources during the forward-porting
  process (not that it's hugely urgent but it seems unnecessary)
- the autogc commonly fails due to the combination of large repository
  (odoo/odoo) and low memory limits (hardmem for odoo, which get
  translated into soft ulimits)

As a result, the garbage collection of the repository sometimes stops
entirely, leading to an increase in repository size and a decrease in
performances.

To mitigate this issue, disable the automagic gc and maintenance
during normal operation, and instead add a weekly cron which runs an
aggressive GC with memory limits disabled (as far as they can get, if
the limits are imposed externally there's nothing to be done).

The maintenance is implemented using a full lockout of the
forward-port cron and an in-place GC rather than a copy/gc/swap, as
doing this maintenance at the small hours of the week-end (sat-sun
night) seems like a non-issue: currently an aggressive GC of odoo/odoo
(using the default aggressive options) takes a total of 2:30 wallclock
(5h user) on a fairly elderly machine (it's closer to 20mn wallclock
and 2h user on my local machine, also turns out the cache repos are
kinda badly configured leading to ~30% more objects than necessary
which doesn't help).

For the record, a fresh checkout of odoo/odoo right now yields:

    | Overall repository size      |           |
    | * Commits                    |           |
    |   * Count                    |   199 k   |
    |   * Total size               |   102 MiB |
    | * Trees                      |           |
    |   * Count                    |  1.60 M   |
    |   * Total size               |  2.67 GiB |
    |   * Total tree entries       |  74.1 M   |
    | * Blobs                      |           |
    |   * Count                    |  1.69 M   |
    |   * Total size               |  72.4 GiB |

If this still proves insufficient, a further option would be to deploy
a "generational repacking" strategy:
https://gitlab.com/gitlab-org/gitaly/-/issues/2861 (though apparently
it's not yet been implemented / deployed on gitlab so...).

But for now we'll see how it shakes out.

Close #489

---
## [Empire-Strikes-Back/May](https://github.com/Empire-Strikes-Back/May)@[dd88bbfade...](https://github.com/Empire-Strikes-Back/May/commit/dd88bbfadec2880b151d44ebe1a7afad3e6b58b7)
#### Thursday 2022-12-22 15:17:01 by May

4 stones! what do I need an empty crate for?!

like Stephen Curry I want to perform

unlike Michael Greger I don't want to cause people to stumble by not going further and being expert of the law

I listen to Jesus - I know about two masters, blind leads the blind, reborn

let my name be May - I am Captain Slow of the garden
let me take Ahsoka's place in brothers' garden - unlike Luc Besson we don't need a thread of marrige evil to tell a story

:Bruce-Willis wrong! - I kick the main door open - Hafar! at last! bang bang - evil guys dead
:Beck close - you're in a van outside, making sure communications don't go down

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[f17e8c3b37...](https://github.com/mrakgr/The-Spiral-Language/commit/f17e8c3b375bba8120fce36639623298eb8023c4)
#### Thursday 2022-12-22 15:58:33 by Marko Grdinić

"2:30pm. https://mangadex.org/title/21b848be-1bfe-4f97-b92c-62d319d8a093/onee-sama-to-watashi-ojou-sama-ga-isekai-tensei

Just read ch 3. It is actually quite good. Let me do the chores here finally. Then I will deal with the new join point.

3pm. Phew done with chores. Let me resume. First comes the tokenizer.

```fs
    | SpecJoin
    | SpecJoinBackend
```

First time in a while that I will be putting in a new keyword.

```fs
| "join" -> f SpecJoin | "join_backend" -> f SpecJoinBackend
```

Beautiful.

```fs
let case_join_point = skip_keyword SpecJoin >>. next |>> join_point
```

I need a new case here.

```fs
    | RawJoinPoint of VSCRange * RawExpr
    | RawJoinPointBackend of VSCRange * backend: string * RawExpr
```

Let me do it like this in the parser.

```fs
let join_point_backend (a,b) = RawJoinPointBackend(range_of_expr b, a, b)
```

Let me do it like so.

```fs
let read_big_var_as_symbol d =
    try_current d <| function
        | p, TokVar(t',_) when Char.IsUpper(t',0) -> update_semantic d SemanticTokenLegend.symbol; skip d; Ok t'
        | p, _ -> Error [p, ExpectedBigVar]
```

This is what I need.

```fs
let case_var = read_var' |>> fun (r,x,leg) -> RawV(r,x)
```

Why am I using this inefficient parser here?

```fs
let case_var = read_var'' |>> RawV
```

This should improve it a bit.

```fs
let read_big_var_as_keyword d =
    try_current d <| function
        | p, TokVar(t',_) when Char.IsUpper(t',0) -> update_semantic d SemanticTokenLegend.keyword; skip d; Ok t'
        | p, _ -> Error [p, ExpectedBigVar]
```

Actually, let me implement this.

```fs
let case_join_point_backend = skip_keyword SpecJoinBackend >>. (read_big_var_as_keyword .>>. next) |>> join_point_backend
```

Plugged it in.

Also, it might not be bad to include the range of the backend string.

```fs
| RawJoinPointBackend of VSCRange * backend: (VSCRange * string) * RawExpr
```

Piece of cake.

```fs
| RawJoinPointBackend(r,(r',b),a) -> RawJoinPointBackend(g r,(g r',b),f a)
```

Thankfully adding these cases is easy.

3:20pm. F# is really wonderful right now. It has been many months since I did the old passes, and I just have to go in and fill the missing cases.

```fs
    | EJoinPoint of Range * E * T option * backend: string
    | EJoinPoint' of Range * Scope * E * T option * backend: string
```

Let me add the range in the backend.

```fs
(Range * string)
```

Now it is complaining that this can't be null.

```fs
| E.EJoinPoint(_,a,b,(_,c)) -> EJoinPoint(term a,Option.map ty b,c)
```

Wait, this could result in a null exception.

```fs
    | EJoinPoint of Range * E * T option * backend_range: Range * backend_string: string
    | EJoinPoint' of Range * Scope * E * T option * backend_range: Range * backend_string: string
```

How about this. But why wasn't this a problem in `RawJoinPoint`?

```fs
    | RawJoinPoint of VSCRange * RawExpr
    | RawJoinPointBackend of VSCRange * backend: (VSCRange * string) * RawExpr
```

Because I have two of them. No way around it.

What I should do is use an option type.

```fs
    | EJoinPoint of Range * E * T option * backend: (Range * string) option
    | EJoinPoint' of Range * Scope * E * T option * backend: (Range * string) option
```

In fact it might have been better had I done this in the parser as well.

```fs
    | RawJoinPoint of VSCRange * RawExpr
    | RawJoinPointBackend of VSCRange * backend: (VSCRange * string) * RawExpr
```

You know what, let me fuse them after all.

```fs
let join_point = function
    | RawJoinPoint _ as x -> x
    | x -> RawJoinPoint(range_of_expr x, None, x)
let join_point_backend (a,b) = RawJoinPoint(range_of_expr b, Some a, b)
```

Er, didn't I have an optimization where I strip nested join points? I wonder where that was supposed to be?

Am I sure I am not imagining it?

```spiral
inl main () = join join (1i32,2i32),3i32
```

No, I am not. The nested join points here get stripped away.

Let me try running the current version.

Yeah, it is still there, where does this happen.

4:05pm. Ah, I am so retarded.

```fs
let join_point = function
    | RawJoinPoint _ as x -> x
    | x -> RawJoinPoint(range_of_expr x, None, x)
let join_point_backend (a,b) = RawJoinPoint(range_of_expr b, Some a, b)
```

The nested join points are in fact removed here. Think it for a bit. The act of removal is equivalent to the act of not putting it in here.

Sigh, I had the feeling it was this, but I couldn't see it. In fact, this was where I remembered it being. Ok.

Let me get rid of the Cython backend here.

```fs
| "Cython*" | "Cython" -> BuildFatalError "The Cython backend has been replaced by the Python one in v2.3.1 of Spiral. Please use 2.3.0 or earlier to access it." // Date: 12/22/2022
```

```fs
| TyBackend _ -> raise_codegen_error "The F# backend does not support nesting other backends."
```

This is in the F# backend.

```fs
| TyBackend(_,_,_) -> Set.empty
```

This is how it should be in the analysis.

```fs
| TyBackend _ -> raise_codegen_error "The C backend does not support nesting of other backends."
```

```
Error trace on line: 1, column: 10 in module: c:\Users\Marko\Source\Repos\The Spiral Language\Spiral Compilation Tests\compilation_tests\tutorial1\main.spi.
inl main () =
         ^
Error trace on line: 2, column: 5 in module: c:\Users\Marko\Source\Repos\The Spiral Language\Spiral Compilation Tests\compilation_tests\tutorial1\main.spi.
    inl x = join_backend UPMEM_C
    ^
```

The C backend does not support nesting of other backends.

You know what, I should not have bothered with the range for the backend, but it does not matter. It is better this way. The option type gets compiled null when it is `None` anyway.

4:25pm. I won't go back to remove the symbol range. It is not worth messing with.

Plus it might become useful once I start work on the UPMEM backend.

```fs
| "Cython*" | "Cython" -> BuildFatalError "The Cython backend has been replaced by the Python one in v2.4.0 of Spiral. Please use an earlier version to access it." // Date: 12/22/2022
```

The UPMEM backend will warrant a minor version increase.

4:35pm. Got rid of all the .pyx files from the repo. Good ridance. I bet the stuff in the Cython experiments folder would work with the Python compiler as well.

4:45pm. Yesterday I went at it till 7pm and it wrecked me.

4:50pm. Right now I am just thinking.

4:55pm. I really should stop, but I've been thinking and I thought of something brilliant.

For the C backend, I am going to factor it out and pass it as a handler into the Python one. I really meant to copy paste things, but now that I am going through it more careuflly, I see that there is no need. Only really need to handle the TyBackend cases and I am set. I can just pass in a function to do that.

Let me commit there so I can track the changes."

---
## [seanpdoyle/turbo](https://github.com/seanpdoyle/turbo)@[d57b389d43...](https://github.com/seanpdoyle/turbo/commit/d57b389d43d965666b61fbf64dfc2b8774d7460f)
#### Thursday 2022-12-22 16:11:22 by Sean Doyle

Extract `FrameVisit` to drive `FrameController`

The problem
---

Programmatically driving a `<turbo-frame>` element when its `[src]`
attribute changes is a suitable end-user experience in consumer
applications. It's a fitting black-box interface for the outside world:
change the value of the attribute and let Turbo handle the rest.

However, internally, it's a lossy abstraction.

For example, when the `FrameRedirector` class listens for page-wide
`click` and `submit` events, it determines if their targets are meant to
drive a `<turbo-frame>` element by:

1. finding an element that matches a clicked `<a>` element's `[data-turbo-frame]` attribute
2. finding an element that matches a submitted `<form>` element's `[data-turbo-frame]` attribute
3. finding an element that matches a submitted `<form>` element's
   _submitter's_ `[data-turbo-frame]` attribute
4. finding the closest `<turbo-frame>` ancestor to the `<a>` or `<form>`

Once it finds the matching frame element, it disposes of all that
additional context and navigates the `<turbo-frame>` by updating its
`[src]` attribute. This makes it impossible to control various aspects
of the frame navigation (like its "rendering" explored in
[hotwired/turbo#146][]) outside of its destination URL.

Similarly, since a `<form>` and submitter pairing have an impact on
which `<turbo-frame>` is navigated, the `FrameController` implementation
passes around a `HTMLFormElement` and `HTMLSubmitter?` data clump and
constantly re-fetches a matching `<turbo-frame>` instance.

Outside of frames, page-wide navigation is driven by a `Visit` instance
that manages the HTTP life cycle and delegates along the way to a
`VisitDelegate`. It also pairs calls to visit with a `VisitOption`
object to capture additional context.

The proposal
---

This commit introduces the `FrameVisit` class. It serves as an
encapsulation of the `FetchRequest` and `FormSubmission` lifecycle
events involved in navigating a frame.

It's implementation draws inspiration from the `Visit`, `VisitDelegate`,
and `VisitOptions` pairing. Since the `FrameVisit` knows how to unify
both `FetchRequest` and `FormSubmission` hooks, the resulting callbacks
fired from within the `FrameController` are flat and consistent.

Extra benefits
---

The biggest benefit is the introduction of a DRY abstraction to
manage the behind the scenes HTTP calls necessary to drive a
`<turbo-frame>`.

With the introduction of the `FrameVisit` concept, we can also declare a
`visit()` and `submit()` method for `FrameElementDelegate`
implementations in the place of other implementation-specific methods
like `loadResponse()` and `formSubmissionIntercepted()`.

In addition, these changes have the potential to close
[hotwired/turbo#326][], since we can consistently invoke
`loadResponse()` across `<a>`-click-initiated and
`<form>`-submission-initiated visits. To ensure that's the case, this
commit adds test coverage for navigating a `<turbo-frame>` by making a
`GET` request to an endpoint that responds with a `500` status.

[hotwired/turbo#146]: https://github.com/hotwired/turbo/pull/146
[hotwired/turbo#326]: https://github.com/hotwired/turbo/issues/326

---
## [fbfarmpro/fbfarmpro-tg-bot-1.0](https://github.com/fbfarmpro/fbfarmpro-tg-bot-1.0)@[f5b7791ac0...](https://github.com/fbfarmpro/fbfarmpro-tg-bot-1.0/commit/f5b7791ac07a619a941313a640f8c44578ce62d6)
#### Thursday 2022-12-22 16:46:23 by kindane

fucking bullshit, shit. I found this error!!!FIXED!!

---
## [ZephyrTFA/tgstation](https://github.com/ZephyrTFA/tgstation)@[a9fda932e2...](https://github.com/ZephyrTFA/tgstation/commit/a9fda932e2a9d8cf20f5f74fdcbdbcca86d580e6)
#### Thursday 2022-12-22 17:08:14 by Tim

Drinking singulo ignores supermatter hallucinations and pulls nearby objects (#71927)

## About The Pull Request
Drinking a singulo will now:

- Give immunity to supermatter hallucinations
- Pulls objects to you based on the total volume in your system (20u =
1x1, 45u = 2x2, 80u = 3x3)
- Makes a burp and supermatter rays/sound when objects are pulled

The new ingredient is:

- Vokda 5u 
- Wine 5u
- Liquid Dark Matter 1u (replaces Radium)

## Why It's Good For The Game
More cool effects for drinks. Singularity is all about gravity and the
drink should have a theme around that.


![dreamseeker_2q21YXS698](https://user-images.githubusercontent.com/5195984/207297517-90d26395-dd30-4106-bdd4-b30b1ba3e20b.gif)

## Changelog
:cl:
add: Drinking singulo will now ignore supermatter hallucinations and
pull objects to you
balance: Change singulo drink recipe to require liquid dark matter
instead of radium.
/:cl:

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[695e215af5...](https://github.com/mrakgr/The-Spiral-Language/commit/695e215af5aac6e0846d2eb97e2454d680d79a9a)
#### Thursday 2022-12-22 18:08:01 by Marko Grdinić

"```fs
| TyBackend(a,b,c) -> line s (backend_handler (a,b,c))
```

Piece of cake.

No wait...

```fs
| TyBackend(a,b,c) -> return' (backend_handler (a,b,c))
```

That should result in the method name being assigned to this. Now what I have to do is make use of it.

5:10pm. I really did a great thing by making the backend dictionary the same as the method one. That was brilliant of me.

```fs
let rec let_join_point = function
    | RawForall(r,a,b) -> RawForall(r,a,let_join_point b)
    | RawFun(r,[a,b]) -> RawFun(r,[PatDyn(range_of_pattern a, a), let_join_point b])
    | RawFun(r,l) ->
        let empty = fst r, fst r
        let n = unintern " ar" 'g'
        let a = PatDyn(empty,PatVar(empty,n))
        let b = RawMatch(empty,RawV(empty,n),List.map (fun (a,b) -> PatDyn(range_of_pattern a, a),b) l)
        RawFun(r,[a,join_point b])
    | x -> join_point x

let let_join_point' = function
    | RawForall _ | RawFun _ as x -> let_join_point x
    | x -> x
```

I think I am going to get rid of the optimization that removes nested join points. Could that thing really be useful?

```fs
let join_point = function // Removes nested join points.
    | RawJoinPoint(_,None,_) as x -> x
    | x -> RawJoinPoint(range_of_expr x, None, x)
```

Actually, let me just do this.

Now it should be equivalent to what I had before. I've put in a comment to highlight what it is doing.

```fs
/// Some places need unique string refs, so this is to keep the compiler from interning static strings.
let unintern a b = sprintf "%s%c" a b
```

You know what, instead of this ugliness, could I just have done a string copy somehow?

https://learn.microsoft.com/en-us/dotnet/api/system.string.intern?view=net-7.0

Hmm, maybe it would have better to just put the string into a string builder?

...I give up. Forget it. It is not worth messing around. I am just wasting my time thinking about this.

5:20pm. Damn it, I know how to do it, but I do not feel like messing with it right now.

I am thinking about the Cuda backend and comparing it to the regular one.

The UPMEM backend has __host variables and other globals I will need to pass in. The Cuda backend has those __device kernels. It also doesn't have a direct main function, but instead has __host functions that take in arguments.

5:25pm. But that is a C backend specific thing. The Python backend does not depend on any of the differences between these.

The best process here is to copy paste at first, and then abstract the differences later.

5:30pm. That having said, when it comes to the C backend, I'd just pass in a message.

Yeah, forget copy pasting. What I will do is pass in a message.

The UPMEM backend is extremely like the prototypal one so, I'll just extend the prototypal one a tad.

Let me do it. Let me do it!

```fs
type BackendType = Prototypal | UPMEM of TyV []
```

I'll do this.

```fs
        import "stdbool.h"
        import "stdint.h"
        import "stdio.h"
        import "stdlib.h"
        import "string.h"
        import "math.h"

        let main_defs = {text=StringBuilder(); indent=0}
        match backend_type with
        | Prototypal | UPMEM [||] -> ()
        | UPMEM args ->
            for L(i,t) in args do line main_defs $"__host {tyv t} v{i}"
            line main_defs ""

        line main_defs (sprintf "%s main(){" (prim Int32T))
        binds_start [||] (indent main_defs) x
        line main_defs "}"
```

Here, this is all I need to make the C backend UPMEM ready.

Though I do not know if it supports all the standard libraries here. But it does not matter - I am just using them for type definitions mostly. I should be able to hash out the missing typedefs with the devs or myself easily enough.

5:45pm. That handles the C backend. But now I have to deal with the Python one. That should likewise be easy.

```fs
type CBackendType = Prototypal | UPMEM of TyV []
```

Let me just rename it to this.

...Come of to think of it, in the future I will have a nested Prototypal C + UPMEM C backend. And the above does not show the distinction between the two appropriately, but that does not matter right now.

I'll easily be able to extend it.

Let me deal with the Python handler.

```fs
type PythonBackendType = Prototypal | UPMEM
```

Piece of cake.

6pm.

```fs
let codegen backend_type env x =
    match backend_type with
    | Prototypal -> codegen' (fun _ -> raise_codegen_error "The Python backend does not support nesting of other backends.") env x
    | UPMEM_Python_Host ->
        let ar = ResizeArray()
        let g = Dictionary(HashIdentity.Structural)
        codegen' (fun (a,b,(r',backend_name)) ->
            match backend_name with
            | "UPMEM_C_Kernel" ->
                let i = ar.Count

                $"upmem{i}"
            | x -> raise_codegen_error $"The UPMEM Python Host backend does not support the {x} backend."
            ) env x
```

Ok, this is good progress.

Let me look at the join point regarding how to extract the arguments.

...In fact...

```fs
    and method : _ -> MethodRec =
        jp false (fun ((jp_body,key & (C(args,_))),i) ->
            match (fst env.join_point_method.[jp_body]).[key] with
            | Some a, Some range -> {tag=i; free_vars=rdata_free_vars args; range=range; body=a}
            | _ -> raise_codegen_error "Compiler error: The method dictionary is malformed"
            ) (fun s x ->
            let method_args = x.free_vars |> Array.map (fun (L(i,t)) -> $"v{i} : {tyv t}") |> String.concat ", "
            line s $"def method{x.tag}({method_args}) -> {tup_ty x.range}:"
            binds_start x.free_vars (indent s) x.body
            )
```

I should be looking on this for guidance how to get the free vars.

Copy paste, copy paste this.

```fs
| x -> raise_codegen_error $"The UPMEM Python Host backend does not support the {x} backend."
```

Damn, I really have zero place to put the trace it seems. I'll strip the range after all.

No, no, just leave it in. Maybe in the future I will be working on better error messages, and I'll be glad this is in.

Ah, wait, the way I am adding is broken.

```fs
upmem_c_kernels.Add(C.codegen' (C.UPMEM_C_Kernel args) env a)
```

It is not enough to just dump it here.

```fs
let codegen backend_type env x =
    match backend_type with
    | Prototypal -> codegen' (fun _ -> raise_codegen_error "The Python backend does not support nesting of other backends.") env x
    | UPMEM_Python_Host ->
        let upmem_c_kernels = StringBuilder()
        let upmem_add_kernel (name : string) (code : string) =
            upmem_c_kernels.AppendLine($"{name} = \"\"\"")
                .Append(code)
                .AppendLine("\"\"\"") |> ignore
            ()
        let g = Dictionary(HashIdentity.Structural)
        let python_code =
            codegen' (fun (jp_body,key,(r',backend_name)) ->
                match backend_name with
                | "UPMEM_C_Kernel" ->
                    Utils.memoize g (fun (jp_body,key & (C(args,_))) ->
                        let name = $"upmem{g.Count}"
                        let args = rdata_free_vars args
                        match (fst env.join_point_method.[jp_body]).[key] with
                        | Some a, Some _ -> upmem_add_kernel name (C.codegen' (C.UPMEM_C_Kernel args) env a)
                        | _ -> raise_codegen_error "Compiler error: The method dictionary is malformed"
                        name
                        ) (jp_body,key)
                | x -> raise_codegen_error $"The UPMEM Python Host backend does not support the {x} backend."
                ) env x

        upmem_c_kernels.Append(python_code).ToString()
```

Lunch time.

6:45pm. Anyway, that thing I posted here should be the complete UPMEM backend. Tomorrow I will move to testing it.

6:50pm. I am just in a daze looking at that code fragment. Had I done the 2018 ML library in Python rather than F# it would have been vastly better. It is too bad that I lacked the necessary skills for it.

6:55pm. If things could go well for me financially, my own future would be so bad.

During the night I've been thinking about some of the slides from the PIM course.

I am not sure in which lecture it was, but it was one of the AI focused PIM chips.

It said it had 1,200 TFLOPs compared to 800 for H100. This is for f16. I remember it being 80 for f32 and 40 for f64.

Imagine that 80 TFLOPs number for the H100 which is not even out yet. How much would my GTX 970 arrive at? Probably 10x less at least. 20x. So 4 TFFLOPs.

And this not counting that when doing RL, I'd be running into bandwith limitations due to lack of batching. I mean, I did do batching even though it was a huge chore to put the poker game in that format and it severely restricted my memory. GPUs are simply unfit for the task.

Suppose at I got 25-50% of the total utilization. 50%. So 2 TFLOPs.

Going to PIM chips could in fact give me a 1,000x speedup for the kind of work that I want to do.

Had I the 1,000x computatonal power that I did in 2021, I very well might have succeeded at making the poker agent. Though I really messed up by picking Cython and made things a lot harder on me.

I think once I complete the two UPMEM backends plus the generic kernel projects, that is when I am going to have Spiral at 100% power.

If somebody gives me an AI accelerator in the future, I'll literally be able to put a backend for it together in a day or two. It will be an amazing power. To be the programmer that I want to be, I need both the right language and the right hardware. The hardware is far away, but the language will be here in a week or two.

I really don't have anything, but gratitude for the UPMEM guy for spurring me to do this.

Yeah, this is the true me. This is how I should be behaving. I wish that at some point I am able to benefit from the accumulation of skills and experience, rather than being left to rot by the wayside."

---
## [TripleTrable/dwm](https://github.com/TripleTrable/dwm)@[67d76bdc68...](https://github.com/TripleTrable/dwm/commit/67d76bdc68102df976177de351f65329d8683064)
#### Thursday 2022-12-22 18:36:31 by Chris Down

Do not allow focus to drift from fullscreen client via focusstack()

It generally doesn't make much sense to allow focusstack() to navigate
away from the selected fullscreen client, as you can't even see which
client you're selecting behind it.

I have had this up for a while on the wiki as a separate patch[0], but
it seems reasonable to avoid this behaviour in dwm mainline, since I'm
struggling to think of any reason to navigate away from a fullscreen
client other than a mistake.

0: https://dwm.suckless.org/patches/alwaysfullscreen/

---
## [vicirdek/PsychonautStation](https://github.com/vicirdek/PsychonautStation)@[a3e7c70f6d...](https://github.com/vicirdek/PsychonautStation/commit/a3e7c70f6da0fc7ea9929ddb39beddcf3113707f)
#### Thursday 2022-12-22 19:14:33 by necromanceranne

Bodypart code cleanup, robotic limbs can actually be disabled through damage again. (#71739)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

Cleans up various variables and code comments in bodypart code so that
it is easier to understand (hopefully) what the fuck is happening there.

Fixes a hilarious oversight. For what may have been an entire 2 year
span, robotic limbs were unable to be disabled whatsoever. Good stuff.

## Why It's Good For The Game

Lost all your limbs and now have only surplus prosthetics?
Congratulations! You're now more durable than even someone with proper
robotic limbs, as your arms do not contribute anything more than 10
damage (or 15 stamina) to your overall damage taken. Furthermore, taking
the maximum amount of damage is actually entirely meaningless to you.

Laugh as someone attempting to shoot your arms does almost no meaningful
damage once you hit the cap! It's all sunk cost! You can't have it blown
off anyway, because dismembering surplus limbs is gone!

Who knew getting into a horrible bluespace/goliath accident could have
such an impact on your combat prowess. Thanks Nanotrasen!

Anyway, these vars are ugly.

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
code: Makes a lot of the bodypart variables clearer as to what they do.
Includes more detailed code comments.
fix: Robotic limbs are no longer immune to being disabled through
reaching maximum damage.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [cockroachdb/cockroach](https://github.com/cockroachdb/cockroach)@[506035b80e...](https://github.com/cockroachdb/cockroach/commit/506035b80e6ac83f1042aba6a42c0f526df5ba5b)
#### Thursday 2022-12-22 19:56:09 by craig[bot]

Merge #93270 #94102 #94147

93270: sql, server: implement and write to new recent statements cache r=amyyq2 a=amyyq2

This change implements and tests a new RecentStatementsCache that is used to store the recent statements that were executed. The cache has two new cluster settings that tune the capacity and time that a statement lives in the cache.

This change also implements writing ActiveQueries to the cache. The RecentStatementsCache is added to the ExecutorConfig, and the Server writes to this cache whenever a non-internal statement finishes. This change also removes queryMeta.phase, and replaces it with ActiveQuery.Phase. The phases Canceled, Timed Out, Completed, and Failed are also as possible values to ActiveQuery.Phase.

Part Of #86955
Fixes #91556

Release note: None

94102: build: add tooling to mirror NPM dependencies to GCS r=sjbarag a=sjbarag

Note that this doesn't actually _apply_ these changes yet! That'll happen in a separate PR so we can have a better discussion about the mechanics involved here (and also to make backporting significantly simpler)

-----

CockroachDB's NPM dependencies are currently provided by the git
submodule in pkg/ui/yarn-vendored [1] and are installed during the
Bazel build with the '--offline' flag [2] to avoid relying on public
NPM registries. Bazel's rules_nodejs unfortunately doesn't work well
with dependencies that are vendored on-disk in the Bazel workspace via
yarn-offline-mirror, which led to some unfortunate hacks [3,4] being
introduced during the initial Bazel setup.

In the time since those hacks were added, two significant events
occured:

1. Bazel's rules_nodejs was deprecated in favor of rules_js [5], which
   manually implements the pnpm resolver algorithm and doesn't support
   yarn's yarn-offline-mirror configuration value.
2. Bazel 6 was released [6], which removed the 'managed_directories'
   attribute to the top-level workspace() rule that makes yarn_install
   work in CockroachDB at all.

The use of yarn-vendored therefore blocks both migration away from
rules_nodejs and an upgrade to Bazel 6.

Instead of relying on a git submodule and --offline installation,
it's possible to use the pattern already used by CockroachDB's go
dependencies: copy them from public locations to a storage bucket
managed by Cockroach Labs, then ensure the bucket is used for future
downloads. Doing so allows the yarn_vendored submodule and --offline
installation to be removed in favor of _online_ builds from a location
Cockroach Labs controls, thus unblocking both a migration away from
rules_nodejs and an upgrade to Bazel 6.

Add a //pkg/cmd/mirror/npm tree (and supporting ./dev tooling) that
downloads NPM dependencies from public registries, uploads them to a
public-readable bucket, and rewrites yarn.lock files to use that bucket,
along with a test to ensure those mirrored dependencies continue to be
used in the future.

[1] https://github.com/cockroachdb/yarn-vendored
[2] https://classic.yarnpkg.com/en/docs/cli/install#toc-yarn-install-offline
[3] ./build/bazelutil/seed_yarn_cache.bzl
[4] ./build/bazelutil/seed_yarn_cache.sh
[5] https://blog.aspect.dev/rulesjs-launch
[6] https://github.com/bazelbuild/bazel/releases/tag/6.0.0

Part of: https://github.com/cockroachdb/cockroach/issues/85038
Release note: None

94147: release: pass GCS credentials to publish-provisional-artifacts r=rickystewart a=rail

Previously, publish-provisional-artifacts requires `GOOGLE_APPLICATION_CREDENTIALS` environment variable when `--gcs-bucket` is passed. This was not the case for the case where we upload the latest binaries (`--bless`).

This PR adds required steps to set up and pass the credentials.

Epic: none
Release note: None

Co-authored-by: amyyq2 <amy.qian@cockroachlabs.com>
Co-authored-by: Sean Barag <barag@cockroachlabs.com>
Co-authored-by: Rail Aliiev <rail@iqchoice.com>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[63561ca455...](https://github.com/tgstation/tgstation/commit/63561ca455933a38f3390f7fcfa6266fda3c53b3)
#### Thursday 2022-12-22 20:31:28 by san7890

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
## [Ultimate-Fluff/cmss13](https://github.com/Ultimate-Fluff/cmss13)@[eb4886c115...](https://github.com/Ultimate-Fluff/cmss13/commit/eb4886c115a0965a347783b87eb3415f098c2c1f)
#### Thursday 2022-12-22 21:24:25 by carlarctg

Spitter Rework (#1541)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

## About The Pull Request

Design doc:

https://hackmd.io/@waltuh/Sy0A1SnEo
Slightly inaccurate as my brainworms enticed me to change and add mini
features.

Approved by Walter, ignorepproved by Gevonius and Satanbatros


https://cdn.discordapp.com/attachments/280051925154660363/1041475609165045770/image.png

Changes:
- Spit doesn't spatter by default, instead it's now a faster, weak
7-tile* projectile that deals 20 damage with a faster spit cooldown.
Fully accurate at 6 tiles, inaccurate at 7 tiles but can sometimes hit.
- Frenzy replaced with 'charge spit'. Halved speed buff, added +5 armor
buff, the next spit will deal 10 more damage and coat humans in acid but
have only 5* tiles of range.
- Acid spray halves damage every time someone walks on it. However, its
damage is spread over legs and feet, and if someone who is spattered
with acid is hit by it, their acid spatter will be strengthened, dealing
more damage, lasting longer, and needing two rolls to clear up. Also,
the bonus damage didn't actually work, now it does.

* Projectile range code is SHIIIT and breaks on diagonals so the range
variable is increased.

Also, queen acid spit spatters and has 1 second less extra cooldown
because find and replace caused it and I didn't think it was a change
worth removing. It's neat, maybe they'll actually use it now.

Added support for balloonchat colors. (Even TG doesn't have this, we're
awesome now!)

Renamed vision_distance parameter to max_distance so it's similar to
visible_message

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

As stated in the hackmd, spitter is very ineffective without using the
oversight-exploit infinite acid spray spam, and its combo (acid spatter
into spray) does not actually help, as the stun stops the human from
getting further hit by the spray and the bonus damage does not actually
apply thanks to shitcode. This PR makes it so that the combo is indeed
more effective than making humans walk into the spray.

Again as stated, spitter suffers from a strange issue where it's
actually not good at harassing from range despite that being its
purpose, since it has a low range. By letting it be long ranged by
default and choose to go short range, it adds a lot of depth and
versatility and lets it actually harass marines.

As always they can just. Shoot it to make it go away. 

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
refactor: Added support for balloonchat colors. (Even TG doesn't have
this, we're awesome now!)
add: Spitter rework!
add: Spit is now full screen range but weaker.
add: Frenzy is renamed and causes spit to inflict spatter coating.
add: Acid spray's damage is halved every time it hits a human, but if it
hits someone coated in acid it will enhance it, making it more dangerous
and need two rolls to shake off.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->

---
## [Ultimate-Fluff/cmss13](https://github.com/Ultimate-Fluff/cmss13)@[146d4a3fa8...](https://github.com/Ultimate-Fluff/cmss13/commit/146d4a3fa87a25a16e7246c32d85b6b57614adc5)
#### Thursday 2022-12-22 21:24:25 by carlarctg

Cloaked belltower alpha increased from 10 (scout) to 35. (#1768)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

## About The Pull Request

Var change.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

You may think this is a 'ided' change, that I got owned by a bell tower
and opened this PR. But believe me, it's the exact other way around.

I play engineer often, especially on New Varadero, and every time I pick
the cloaked bell. It is hilariously busted, but that's not actually the
point here. The reason I'm making this PR is because it is genuinely
_impossible_ to find the belltower if it's fully cloaked. If you don't
memorize the placement you quite literally HAVE to right click over
every single tile in the region because the alpha value is SO low it is
just not feasible to detect. I'm saying this as an engineer, it's too
damn much, it takes me half a minute to find my tower and pack it up
again. Worse, sometimes people take it or a xeno slashes it while I'm
being defibbed and I can't tell if I just can't find it or what.

The difference between scout's cloak and the belltower's cloak is that
scout has a large one color silhouette and is constantly moving, and can
additionally be detected through walls by xenos, though again, not the
reason for this. The belltower has a small, thin silhouette that has
lots of gaps in its sprite, making it very hard to locate by hand.

That this will weaken the belltower against xenos is no surprise, but I
don't think that's a problem. As I said, the belltower is busted. I say
this as someone who uses it more than has it used against them. 6
seconds of superslow in a 4x4/5x5 range!

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
balance: Increased alpha (reduced camo) of the camo belltower from 10 to
35. This is mainly meant for engineers to be able to see their tower to
pick it up, but the inevitable balance changes aren't unintended.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->

---
## [cockroachdb/cockroach](https://github.com/cockroachdb/cockroach)@[1d04cec7c5...](https://github.com/cockroachdb/cockroach/commit/1d04cec7c5f887d309e09b7b5a267d5269d86b5a)
#### Thursday 2022-12-22 21:38:38 by craig[bot]

Merge #91394 #91627

91394: changefeedccl: roachtest refactor and initial-scan-only r=samiskin a=samiskin

Epic: https://cockroachlabs.atlassian.net/browse/CRDB-19057

Changefeed roachtests were setup focused on running a workload for a specific duration and then quitting, making it difficult to run an `initial_scan_only` test that terminated upon Job success.

We as a team have also noticed a greater need to test and observe changefeeds running in production against real sinks to catch issues we are unable to mock or observe from simple unit tests.  This is currently a notable hassle as one has to set up each individual sink and run them, ensure the changefeed is pointing to the right URI, and then be able to monitor the metrics of this long running process.  

This change refactors the cdcBasicTest into distinct pieces that are then put together in a test.  This allows for easier experimentation with live tests, allowing us to spin up a cluster and a workload, run one or more changefeeds on it, set up a poller to print out job details,have an accessible grafana URL to view metrics, and wait for some completion condition.

Changing the specialized `runCDCKafkaAuth`, `runCDCBank`, and `runCDCSchemaRegistry` functions were left out of scope for this first big change.

The main APIs involved in basic roachtests are now:
- `newCDCTester`: This creates a tester struct to run the rest of the APIs and initializes the database
- `tester.runTPCCWorkload(tpccArgs)`: Starts a TPCC workload from the last node in the cluster
- `tester.runLedgerWorkload(ledgerArgs)`: Starts a Ledger workload from the last node in the cluster
- `tester.runFeedLatencyVerifier(changefeedJob, latencyTargets)`: starts a routine that monitors the changefeed latency until the tester is `Close`'d
- `tester.waitForWorkload`: waits for a workload started by `setupAndRunWorkload` to complete its duration
- `tester.startCRDBChaos`: This starts a Chaos routine that periodically shuts nodes down and brings them back up
- `tester.newChangefeed(feedArgs)`: starts a new changefeed on the cluster and returns `changefeedJob` object
- `changefeedJob.waitForCompletion`: waits for a changefeed to complete (either success or failure)
- `tester.startGrafana`: Sets up a grafana instance on the last node of the cluster and prints out a link to a grafana, this automatically runs unless `--skip-init` is provided.  If `--debug` is not used, `StopGrafana` will be called on test teardown to publish prometheus metrics to the artifacts directory.

An API that is going to be more useful for experimentation are:
- `changefeedJob.runFeedPoller(ctx, stopper, onInfo)`: runs a given callback every second with the changefeed info

Roachtests can be ran locally with the `--local` flag or on an existing cluster without destroying it afterwards with `--cluster="my-cluster" --debug`

Ex: After adding a new test (lets say `"cdc/my-test"`) to the `registerCDC` function you can keep running 
```bash
./dev build cockroach --cross # if changes made to crdb
./dev build roachtest         # if changes made to the test

./bin/roachtest run cdc/my-test --cluster="my-cluster" --debug
```
as you try out different changes or options.  If you want to try a set of steps against different versions of the app you could download those binaries and use the `--cockroach="path-to-binary"` flag to test against those instead.

If you want to set up a large TPCC database on a cluster and reuse it for tests this can be done with roachtests's `--wipe` and `--skip-init` flags.

Release note: None

91627: upgrade: introduce "permanent" upgrades r=andreimatei a=andreimatei

This patch introduces "permanent" upgrades - a type of upgrade that is
tied to a particular cluster version (just like the existing upgrades)
but that runs regardless of the version at which the cluster was
bootstrapped (in contrast with the existing upgrades that are not run
when they're associated with a cluster version <= the bootstrap
version). These upgrades are called "permanent" because they cannot be
deleted from the codebase at a later point, in contrast with the others
that are deleted once the version they're tied drops below
BinaryMinSupportedVersion).

Existing upgrades are explicitly or implicitly baked into the bootstrap
image of the binary that introduced them. For example, an upgrade that
creates a system table is only run when upgrading an existing,
older-version, cluster to the new version; it does not run for a cluster
bootstrapped by the binary that introduced the upgrade because the
respective system tables are also included in the bootstrap metadata.
For some upcoming upgrades, though, including them in the bootstrap
image is difficult. For example, creating a job record at bootstrap
time is proving to be difficult (the system.jobs table has indexes, so
you want to insert into it through SQL because figuring out the kv's for
a row is tedious, etc). This is where these new permanent upgrades come
in.

These permanent upgrades replace the `startupmigrations` that don't have
the `includedInBootstrap` field set. All such startupmigrations have
been copied over as upgrades. None of the current `startupmigrations`
have `includedInBootstrap` set (except one but that's dummy one since
the actual migration code has been deleted), so the startupmigrations
package is now deleted. That's a good thing - we had one too many
migrations frameworks.

These permanent upgrades, though, do not have exactly the same semantics
as the startupmigrations they replace. To the extent that there is a
difference, the new semantics are considered more desirable:
- startupmigrations run when a node that has the code for a particular
  migration startups up for the first time. In other words, the
  startupmigrations were not associated with a cluster version; they were
  associated with a binary version. Migrations can run while old-version
  nodes are still around.  This means that one cannot add a
  migration that is a problem for old nodes - e.g. a migration creating a
  job of a type that the old version wouldn't recognize.
- upgrades are tied to a cluster version - they only run when the
  cluster's active version moves past the upgrade's version. This stays
  the case for the new permanent migrations too, so a v2 node will not
  immediately run the permant migrations introduced since v1 when it joins
  a v1 cluster. Instead, the migrations will run when the cluster version
  is bumped. As such, the migrations can be backwards incompatible.

startupmigrations do arguably have a property that can be desirable:
when there are no backwards compatibility issues, the v2 node can rely
on the effects of the startupmigrations it knows about regardless of the
cluster version. In contrast, with upgrades, not only is a node unable
to simply assume that a particular upgrade has run during startup, but,
more than that, a node is not even able to look at a version gate during
the startup sequence in order to determine whether a particular upgrade
has run or not (because, in clusters that are bootstrapped at v2, the
active cluster version starts as v2 even before the upgrades run). This
is a fact of life for existing upgrades, and now becomes a fact of life
for permanent upgrades too. However, by the time user SQL traffic is
admitted on a node, the node can rely on version gates to correspond to
migrations that have run.

After thinking about it, this possible advantage of startupmigrations
doesn't seem too useful and so it's not reason enough to keep the
startupmigrations machinery around.

Since the relevant startupmigrations have been moved over to upgrades,
and the two libraries use different methods for not running the same
migration twice, a 23.1 node that comes up in a 22.2 cluster will re-run
the several permanent upgrades in question, even though they had already
run as startupmigrations. This is OK since both startupmigrations and
upgrades are idempotent. None of the current permanent upgrades are too
expensive.

Closes https://github.com/cockroachdb/cockroach/issues/73813

Release note: None
Epic: None

Co-authored-by: Shiranka Miskin <shiranka@cockroachlabs.com>
Co-authored-by: Andrei Matei <andrei@cockroachlabs.com>

---
## [SizableShrimp/AdventOfCode2022](https://github.com/SizableShrimp/AdventOfCode2022)@[7ff4a8c407...](https://github.com/SizableShrimp/AdventOfCode2022/commit/7ff4a8c407a070af513a86b421ada08c4849bb7c)
#### Thursday 2022-12-22 22:15:55 by SizableShrimp

Finish Day 22

I did not find this day extremely challenging, but visualizing Part 2 without a real-life cube was hard.
For Part 2, I wrote the cube mappings based on the example input assuming it would be the same as the real input.
This mistake cost me time and sanity.
My code has the cube mappings for the example input and real input, but you have to manually swap between the two in the code.
I tried to write an auto-folder, but it failed horribly.

---
## [Fortelian/cmss13](https://github.com/Fortelian/cmss13)@[ca2114f0f5...](https://github.com/Fortelian/cmss13/commit/ca2114f0f56ab4a51443bdac52053ead327724dc)
#### Thursday 2022-12-22 22:32:37 by Mister-moon1

Removes some useless code from welding helmet (#1363)

* fuck you useless code

* you cannot hide, useless code

---
## [Jolly-66/JollyStation](https://github.com/Jolly-66/JollyStation)@[16b1409cf1...](https://github.com/Jolly-66/JollyStation/commit/16b1409cf102d9d23a59edf24d5ef52ba9c9e70d)
#### Thursday 2022-12-22 22:40:53 by TaleStationBot

[MIRROR] [MDB IGNORE] Create a guide for atomization that includes a new allowance to pull requests that might add dead code (#3464)

* Create a guide for atomization that includes a new allowance to pull requests that might add dead code (#71429)

@tgstation/commit-access 

I'm proposing a new use for the Atomic tag that we currently virtually
never use.

We have countless pull requests over time, and plenty of which open now,
that are enormous refactors over tens of files with thousands of
additions. We are historically pretty slow to review and merge these,
and it definitely scares a lot of maintainers off. I think part of the
reason is that we do not like dead code being added, which is completely
reasonable at our scale.

However, I propose that, for refactors/purely code stuff, we ease up on
this a lot, and encourage (not require) people to make smaller pull
requests, even to the extent that it creates APIs we do not use yet.

As an example, https://github.com/tgstation/tgstation/pull/71421 does a
massive refactor to carp. It also does some balance changes, which I
think we could agree could be split off if it was enough of a pain.
However, there's a bunch of other stuff that could have been individual
pull requests here with this new allowance.

- The new basic AI behaviors
- The regenerator component
- Pet commands component

These are things that:

- Would not be used until the transition from simple to basic, but are
easily reviewable on their own
- Are easy to REMOVE if the OP does not follow up
- Are easy to FINISH if the OP does not follow up

(I suspect even, for instance, that there are parts of Wallening we
could be merging right now, that's probably gonna be hundreds or
thousands of files long...)

Pros:
- PRs are more often easily reviewable
- PRs are quicker to merge, since we don't have conflicts from editing
one of the 70 files they changed
- Cleanups can be more easily finished by other people. I don't suspect
this will be likely, but it's not easily possible today

Cons:
- We have to mark the PRs as atomic
- Someone needs to look through every so often (I'm thinking like, once
a month or something) to see if the code ended up being used, or if the
committer still plans to use it
- If the PR is adding a complex enough API that isn't modular, it might
be very hard to remove. I suspect for PRs like this that we ask them to
have an implementer before merging.

NL voice would love your thoughts on this

* Create a guide for atomization that includes a new allowance to pull requests that might add dead code

Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

---
## [Jolly-66/JollyStation](https://github.com/Jolly-66/JollyStation)@[dc0f464c42...](https://github.com/Jolly-66/JollyStation/commit/dc0f464c421eff802692a08d3f05d497971655ba)
#### Thursday 2022-12-22 22:40:53 by TaleStationBot

[MIRROR] [MDB IGNORE] Made geysers easier to find (#3485)

* Made geysers easier to find (#71608)

## About The Pull Request

This PR raises the geyser spawn rate from 0.1 to 0.15 and increases the
weight of wittel geysers to 10 which is the same as every other special
geyser. (previously 6)

Wittel shouldn't be any less difficult to find than other geysers as all
of the special geysers are equally powerful. Hyper-plasmium oxide can be
used to make extremely powerful explosives that can go beyond maxcaps
and hollow water + protozine can create an infinite amount of strange
reagent.

I've subjected myself to going out of my way to visit lavaland/icemoon
several times to get wittel and each time finding a single geyser takes
about 5 minutes of my time. This, coupled with the fact you really don't
have a lot of time to be wasting on looking for the geysers results in
an unfun experience.

I understand geysers are sort of a necessary evil, however, they
shouldn't be THIS difficult to find. Out of the 10 or so geysers I've
found, only 1 has had wittel in it and it was next to a whelp portal
which ended both me and my miner escort.

I've also hunted the entirety of lavaland with no luck. (Horrendous
experience.)

I've dedicated entire rounds to this, by the way.
## Why It's Good For The Game

If you go out of your way to waste ages hunting for geysers, there
should at least be a reward. That is, in the same round, not after 3 or
more rounds as even megafauna gear isn't gatekept THAT hard.

You shouldn't have to waste this much of a miner's time (who is also
going for megafauna gear) to get something that is arguably less
powerful than what they get for less effort. Megafauna gear is also
available every round and is attained via predictable methods.

This PR will also likely make geyser scanning a more comparable method
of point gain to just mining.

Oh and not to mention that penthrite is available almost roundstart via
luxpens. (It's a wittel chem.)
## Changelog
:cl:
balance: Geysers now spawn more often, especially wittel geysers.
/:cl:

* Made geysers easier to find

Co-authored-by: RikuTheKiller <88713943+RikuTheKiller@users.noreply.github.com>

---
## [xoka-pro/goit-python-core-project](https://github.com/xoka-pro/goit-python-core-project)@[c98928749d...](https://github.com/xoka-pro/goit-python-core-project/commit/c98928749da5b08de5099ff4eec54c6fe636d3b3)
#### Thursday 2022-12-22 23:10:36 by Nikita Sherstianykh

Weather func

Working func for getting weather.
- command 'weather *city*'
-if city is incorrect - catch the exceptions
- if city in russia - program says like "russian warship - go fuck yourself"

---
## [Danielkaas94/DTAP](https://github.com/Danielkaas94/DTAP)@[d56b922c9a...](https://github.com/Danielkaas94/DTAP/commit/d56b922c9a2e48cbfaaab5d9878bacd419388c78)
#### Thursday 2022-12-22 23:16:17 by Danielkaas94

Here Comes The Flood 🌊💦
Lord, here comes the flood
We'll say goodbye to flesh and blood
If again the seas are silent
In any still alive
It'll be those who gave their island to survive
Drink up, dreamers, you're running dry

---

