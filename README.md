## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-06-27](docs/good-messages/2022/2022-06-27.md)


1,669,861 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,669,861 were push events containing 2,493,197 commit messages that amount to 195,730,691 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 36 messages:


## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[707fbfac7e...](https://github.com/tgstation/tgstation/commit/707fbfac7e11837865d70587011aa8197b1d0c35)
#### Monday 2022-06-27 00:01:52 by san7890

[MDB Ignore] Shifts all (sane) varedited signs to directionals  (#68004)

* [MDB Ignore] Shifts all (sane) varedited signs to directionals

Hey there,

So we have these cool new sign directionals now, but we still have all of the old pixel-shifted pre-fabrications lying around. So, I added an UpdatePaths (as well as Updated the Paths) to be a bit better at using directionals, because directionals are pretty neato.

This should update every single var_edit that used the proper 32 pixelshift (some of them used 28, and I'm unable to account for that automatically with current tooling) into a proper subtype. Mappers tend to learn by looking at well established maps, so it's always important to ensure that the well-established maps use the most recent tooling (i.e.: bring them up to the surface) and avoid needless excess lines in maps.

* The Commit With All The Maps

OH GOD OH FUCK

* Renames the UpdatePaths

---
## [Will-Bohlen/Paradise](https://github.com/Will-Bohlen/Paradise)@[6082c95eb3...](https://github.com/Will-Bohlen/Paradise/commit/6082c95eb300a9f05b5422060db79f55fe91b9b3)
#### Monday 2022-06-27 00:34:29 by LightFire53

Relocates The Entertainment Offices and Custodial Closet on DeltaStation (#17480)

* Location, Location, Location!

* Lights and Pipes

I am so sorry for how hacky that disposal piping is

* TFW Disposals

* Oh god, what if there is a fire?!

* And a light switch...

Maybe the final commit? Taking bets on if I managed to forget something else

* If you bet on the requests console

You would be right.

* Bigger, Better, Janitor

* Bloody requests console...

---
## [ArcaneMusic/TG-Station-Arcane-Remix](https://github.com/ArcaneMusic/TG-Station-Arcane-Remix)@[20e4add487...](https://github.com/ArcaneMusic/TG-Station-Arcane-Remix/commit/20e4add48712b59e9bcadd187beee54c02f98e38)
#### Monday 2022-06-27 01:18:03 by Tim

Change healing by sleeping to be affected by sanity, darkness (or blindfold), and earmuffs. (#65713)


About The Pull Request

Depending on the mob's sanity level, it can have a positive or negative boost to healing effects while sleeping. Sleeping in darkness, wearing a blindfold, and using earmuffs also counts as a healing bonus. Beauty sleep is very important for 2D spessmen.
Why It's Good For The Game

This is a small gameplay change that rewards players for keeping their sanity at good levels. Also depression has also been linked with impeding wound healing in real life. The placebo effect on peoples minds is strenuously documented and I think it would be cool to see it in the game.
Changelog

cl
expansion: Healing by sleeping is now affected by sanity, sleeping in darkness (or using a blindfold), and using earmuffs. The healing from sleeping in a bed was slightly decreased.
/cl

---
## [awaffle1/tspfv](https://github.com/awaffle1/tspfv)@[2c5c37b038...](https://github.com/awaffle1/tspfv/commit/2c5c37b0385fdf8b0e14809f3a57c4ff85aa4066)
#### Monday 2022-06-27 01:30:51 by im_a_waffle1

everything broke because i put a comma i think

War. War never changes.
Since the dawn of humankind, when our ancestors first discovered the killing power of rock and bone, blood has been spilled in the name of everything: from God to justice to simple, psychotic rage.

---
## [RandomGamer123/tgstation](https://github.com/RandomGamer123/tgstation)@[8f0df7816b...](https://github.com/RandomGamer123/tgstation/commit/8f0df7816bae3c5dedf599611cda3e6039024e14)
#### Monday 2022-06-27 01:35:35 by Kylerace

(code bounty) The tram is now unstoppably powerful. it cannot be stopped, it cannot be slowed, it cannot be reasoned with. YOU HAVE NO IDEA HOW READY YOU ARE (#66657)

ever see the tram take 10 milliseconds per movement to move 2100 objects? now you have
https://user-images.githubusercontent.com/15794172/166198184-8bab93bd-f584-4269-9ed1-6aee746f8f3c.mp4
About The Pull Request

fixes #66887

done for the code bounty posted by @MMMiracles to optimize the tram so that it can be sped up. the tram is now twice as fast, firing every tick instead of every 2 ticks. and is now around 10x cheaper to move. also adds support for multiz trams, as in trams that span multiple z levels.

the tram on master takes around 10-15 milliseconds per movement with nothing on it other than its starting contents. why is this? because the tram is the canary in the coal mines when it comes to movement code, which is normally expensive as fuck. the tram does way more work than it needs to, and even finds new ways to slow the game down. I'll walk you through a few of the dumber things the tram currently does and how i fixed them.

    the tram, at absolute minimum, has to move 55 separate industrial_lift platforms once per movement. this means that the tram has to unregister its entered/exited signals 55 times when "the tram" as a singular object is only entering 5 new turfs and exiting 5 old turfs every movement, this means that each of the 55 platforms calculates their own destination turfs and checks their contents every movement. The biggest single optimization in this pr was that I made the tram into a single 5x11 multitile object and made it only do entering/exiting checks on the 5 new and 5 old turfs in each movement.
    way too many of the default tram contents are expensive to move for something that has to move a lot. fun fact, did you know that the walls on the tram have opacity? do you know what opacity does for movables? it makes them recalculate static lighting every time they move. did you know that the tram, this entire time, was taking JUST as much time spamming SSlighting updates as it was spending time in SStramprocess? well it is! now it doesnt do that, the walls are transparent. also, every window and every grille on the tram had the atmos_sensitive element applied to them which then added connect_loc to them, causing them to update signals every movement. that is also dumb and i got rid of that with snowflake overrides. Now we must take care to not add things that sneakily register to Moved() or the moved signal to the roundstart tram, because that is dumb, and the relative utility of simulating objects that should normally shatter due to heat and conduct heat from the atmosphere is far less than the cost of moving them, for this one object.
    all tram contents physically Entered() and Exited() their destination and old turfs every movement, even though because they are on a tram they literally do not interact with the turf, the tram does. also, any objects that use connect_loc or connect_loc behalf that are on the same point on the tram also interact with each other because of this. now all contents of the tram act as if theyre being abstract_move()'d to their destination so that (almost) nothing thats in the destination turf or the exit turf can react to the event of "something laying on the tram is moving over you". the rare things that DO need to know what is physically entering or exiting their turf regardless of whether theyre interacting with the ground can register to the abstract entered and exited signals which are now always sent.
    many of the things hooked into Moved(), whether it be overrides of Moved() itself, or handlers for the moved signal, add up to a LOT of processing time. especially for humans. now ive gotten rid of a lot of it, mostly for the tram but also for normal movement. i made footsteps (a significant portion of human movement cost) not do any work if the human themselves didnt do the movement. i optimized has_gravity() a fair amount, and then realized that since everything on the tram isnt changing momentum, i didnt actually need to check gravity for the purposes of drifting (newtonian_move() was taking a significant portion of the cost of movement at some points along the development process). so now it simply doesnt call newtonian_move() for movements that dont represent a change in momentum (by default all movements do).

also i put effort into 1. better organizing tram/lift code so that most of it is inside of a dedicated modules folder instead of scattered around 5 generic folders and 2. moved a lot of behavior from lift platforms themselves into their lift_master_datum since ideally the platforms would just handle moving themselves, while any behavior involving the entire lift such as "move to destination" and "blow up" would be handled by the lift_master_datum.

also
https://user-images.githubusercontent.com/15794172/166220129-ff2ea344-442f-4e3e-94f0-ec58ab438563.mp4
multiz tram (this just adds the capability to map it like this, no tram does this)
Actual Performance Differences

to benchmark this, i added a world.Profile(PROFILER_START) and world.Profile(PROFILER_START) to the tram moving, so that it generates a profiler output of all tram movement without any unrelated procs being recorded (except for world.Profile() overhead). this made it a lot easier to quantify what was slowing down both the tram and movement in general. and i did 3 types of tests on both master and my branch.

also i should note that i sped up the "master" tram test to move once per tick as well, simply because the normal movement speed seems unbearably slow now. so all recorded videos are done at twice the speed of the real tram on master. this doesnt affect the main thing i was trying to measure: cost for each movement.

the first test was the base tram, containing only my player mob and the movables starting on the tram roundstart. on master, this takes around 13 milliseconds or so on my computer (which is pretty close to what it takes on the servers), on this branch, it takes between 0.9-1.3 milliseconds.

ALSO in these benchmarks youll see that tram/proc/travel() will vary significantly between the master and optimized branches. this is 100% because there are 55 times more platforms moving on master compared to the master branch, and thus 55x more calls to this proc. every test was recorded with the exact same amount of distance moved

here are the master and optimized benchmark text files:
master
master base tram.txt
https://user-images.githubusercontent.com/15794172/166210149-f118683d-6f6d-4dfb-b9e4-14f17b26aad8.mp4
also this shows the increased SSlighting usage resulting from the tram on master spamming updates, which doesnt happen on the optimized branch

optimized
optimization base tram.txt
https://user-images.githubusercontent.com/15794172/166206280-cd849aaa-ed3b-4e2f-b741-b8a5726091a9.mp4

the second test is meant to benchmark the best case scaling cost of moving objects, where nothing extra is registered to movement besides the bare minimum stuff on the /atom/movable level. Each of the open tiles of the tram had 1 bluespace rped filled with parts dumped onto it, to the point that the tram in total was moving 2100 objects. the vast majority of these objects did nothing special in movement so they serve as a good base case. only slightly off due to the rped's registering to movement.

on master, this test takes over 100 milliseconds per movement
master 2000 obj's.txt
https://user-images.githubusercontent.com/15794172/166210560-f4de620d-7dc6-4dbd-8b61-4a48149af707.mp4

when optimized, about 10 milliseconds per movement
https://user-images.githubusercontent.com/15794172/166208654-bc10086b-bbfc-49fa-9987-d7558109cc1d.mp4
optimization 2000 obj's.txt

the third test is 300 humans spawned onto the tram, meant to test all the shit added on to movement cost for humans/carbons. in retrospect this test is actually way too biased in favor of my optimizations since the humans are all in only 3 tiles, so all 100 humans on a tile are reacting to the other 99 humans movements, which wouldnt be as bad if they were distributed across 20 tiles like in the second test. so dont read into this one too hard.

on master, this test takes 200 milliseconds
master 300 catgirls.txt

when optimized, this takes about 13-14 milliseconds.
optimization 300 catgirls on ram ranch.txt
Why It's Good For The Game

the tram is literally 10x cheaper to move. and the code is better organized.
currently on master the tram is as fast as running speed, meaning it has no real relative utility compared to just running the tracks (except for the added safety of not having to risk being ran over by the tram). now the tram of which we have an entire map based around can be used to its full potential.

also, has some fixes to things on the tram reacting to movement. for example on master if you are standing on a tram tile that contains a banana and the TRAM moves, you will slip if the banana was in that spot before you (not if you were there first however). this is because the banana has no concept of relative movement, you and it are in the same reference frame but the banana, which failed highschool physics, believes you to have moved onto it and thus subjected you to the humiliation of an unjust slipping. now since tram contents that dont register to abstract entered/exited cannot know about other tram contents on the same tile during a movement, this cannot happen.

also, you no longer make footstep sounds when the tram moves you over a floor
TODO

mainly opened it now so i can create a stopping point and attend to my other now staling prs, we're at a state of functionality far enough to start testmerging it anyways.

add a better way for admins to be notified of the tram overloading the server if someone purposefully stuffs it with as much shit as they can, and for admins to clear said shit.
automatically slow down the tram if SStramprocess takes over like, 10 milliseconds complete. the tram still cant really check tick and yield without introducing logic holes, so making sure it doesnt take half of the tick every tick is important
go over my code to catch dumb shit i forgot about, there always is for these kinds of refactors because im very messy
remove the area based forced_gravity optimization its not worth figuring out why it doesnt work
fix the inevitable merge conflict with master lol
create an icon for the tram_tunnel area type i made so that objects on the tram dont have to enter and exit areas twice in a cross-station traversal

    add an easy way to vv tram lethality for mobs/things being hit by it. its an easy target in another thing i already wanted to do: a reinforced concept of shared variables from any particular tram platform and the entire tram itself. admins should be able to slow down the tram by vv'ing one platform and have it apply to the entire tram for example.

Changelog

cl
balance: the tram is now twice as fast, pray it doesnt get any faster (it cant without raising world fps)
performance: the tram is now about 10 times cheaper to move for the server
add: mappers can now create trams with multiple z levels
code: industrial_lift's now have more of their behavior pertaining to "the entire lift" being handled by their lift_master_datum as opposed to belonging to a random platform on the lift.
/cl

---
## [Koi-3088/ForkBot.NET](https://github.com/Koi-3088/ForkBot.NET)@[8825debea5...](https://github.com/Koi-3088/ForkBot.NET/commit/8825debea5875d7f149546950cabd4dae74bc63b)
#### Monday 2022-06-27 02:44:03 by Koi

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
## [Stevanus-Christian/terminal](https://github.com/Stevanus-Christian/terminal)@[77215d9d77...](https://github.com/Stevanus-Christian/terminal/commit/77215d9d77b99b48d1ee8302736178f2ec9f3a77)
#### Monday 2022-06-27 07:23:07 by Mike Griese

Fix `ShowWindow(GetConsoleWindow())` (#13118)

A bad merge, that actually revealed a horrible bug.

There was a secret conflict between the code in #12526 and #12515. 69b77ca was a bad merge that hid just how bad the issue was. Fixing the one line `nullptr`->`this` in `InteractivityFactory` resulted in a window that would flash uncontrollably, as it minimized and restored itself in a loop. Great. 

This can seemingly be fixed by making sure that the conpty window is initially created with the owner already set, rather than relying on a `SetParent` call in post. This does pose some complications for the #1256 future we're approaching. However, this is a blocking bug _now_, and we can figure out the tearout/`SetParent` thing in post. 

* fixes #13066.
* Tested with the script in that issue.
* Window doesn't flash uncontrollably.
* `gci | ogv` still works right
* I work here.
* Opening a new tab doesn't spontaneously cause the window to minimize
* Restoring from minimized doesn't yeet focus to an invisible window
* Opening a new tab doesn't yeet focus to an invisible window
* There _is_ a viable way to call `GetAncestor` s.t. it returns the Terminal's hwnd in Terminal, and the console's in Conhost


The `SW_SHOWNOACTIVATE` change is also quite load bearing. With just `SW_NORMAL`, the pseudo window (which is invisible!) gets activated whenever the terminal window is restored from minimized. That's BAD.


There's actually more to this as well. 


Calling `SetParent` on a window that is `WS_VISIBLE` will cause the OS to hide the window, make it a _child_ window, then call `SW_SHOW` on the window to re-show it. `SW_SHOW`, however, will cause the OS to also set that window as the _foreground_ window, which would result in the pty's hwnd stealing the foreground away from the owning terminal window. That's bad.

`SetWindowLongPtr` seems to do the job of changing who the window owner is, without all the other side effects of reparenting the window. 

Without `SetParent`, however, the pty HWND is no longer a descendant of the Terminal HWND, so that means `GA_ROOT` can no longer be used to find the owner's hwnd. For even more insanity, without `WS_POPUP`, none of the values of `GetAncestor` will actually get the terminal HWND. So, now we also need `WS_POPUP` on the pty hwnd. To get at the Terminal hwnd, you'll need

```c++
GetAncestor(GetConsoleWindow(), GA_ROOTOWNER)
```

---
## [Stevanus-Christian/terminal](https://github.com/Stevanus-Christian/terminal)@[9ccd6ecd74...](https://github.com/Stevanus-Christian/terminal/commit/9ccd6ecd744890b856f3d8a39ff0616c0e34d4fb)
#### Monday 2022-06-27 07:23:07 by Mike Griese

Manually copy trailing attributes on a resize (#12637)

## THE WHITE WHALE

This is a fairly naive fix for this bug. It's not terribly performant,
but neither is resize in the first place.

When the buffer gets resized, typically we only copy the text up to the
`MeasureRight` point, the last printable char in the row. Then we'd just
use the last char's attributes to fill the remainder of the row.

Instead, this PR changes how reflow behaves when it gets to the end of
the row. After we finish copying text, then manually walk through the
attributes at the end of the row, and copy them over. This ensures that
cells that just have a colored space in them get copied into the new
buffer as well, and we don't just blat the last character's attributes
into the rest of the row. We'll do a similar thing once we get to the
last printable char in the buffer, copying the remaining attributes.

This could DEFINITELY be more performant. I think this current
implementation walks the attrs _on every cell_, then appends the new
attrs to the new ATTR_ROW. That could be optimized by just using the
actual iterator. The copy after the last printable char bit is also
especially bad in this regard. That could likely be a blind copy - I
just wanted to get this into the world.

Finally, we now copy the final attributes to the correct buffer: the new
one.  We used to copy them to the _old_ buffer, which we were about to
destroy.

## Validation

I'll add more gifs in the morning, not enough time to finish spinning a
release Terminal build with this tonight.

Closes #32 🎉🎉🎉🎉🎉🎉🎉🎉🎉
Closes #12567

(cherry picked from commit 855e1360c0ff810decf862f1d90e15b5f49e7bbd)

---
## [davidbrochart/nbformat](https://github.com/davidbrochart/nbformat)@[68e399a8c0...](https://github.com/davidbrochart/nbformat/commit/68e399a8c0efa91dfd0e45ef38449cacf712df3c)
#### Monday 2022-06-27 07:34:10 by Jason Grout

Allow notebook format version 4.1 mimebundle keys ending in `+json` to have arbitrary JSON

There are a number of people posting issues with nbformat 5 being stricter about validating notebook format 4.1, including:

https://github.com/jupyter/nbformat/issues/160
https://github.com/jupyter/nbformat/issues/161
https://github.com/jupyter-widgets/ipywidgets/issues/2553
https://github.com/jupyter-widgets/ipywidgets/issues/2788


Essentially, nbformat package version 4.x allowed noncompliant format 4.1 notebooks to be verified as valid, leading to many notebooks in the wild having major/minor format version 4.1, but with widgets and other json outputs that were technically invalid.

Upgrading to nbformat package 5.x correctly flagged these notebook as noncompliant. This is correct technically. However, practically it means that all these notebooks files tagged as format 4.1 that were working fine suddenly won't even open after upgrading to nbformat version 5. This is a pain.

This retroactively upgrades the format 4.1 schema to allow json in these cases, since in practice there are lots of notebooks labeled as format 4.1, I think by official Jupyter software, that have json in the mimebundle output. Essentially, this acknowledges that in the official implementations from Jupyter, notebook format 4.1 has indeed had arbitrary JSON values in mimebundles, and we cannot in good conscience decree it invalid.

---
## [jeremygurr/dcss-minor](https://github.com/jeremygurr/dcss-minor)@[1352289c90...](https://github.com/jeremygurr/dcss-minor/commit/1352289c90d15a53f9c472dac9343ad61d9104a7)
#### Monday 2022-06-27 08:53:19 by Nicholas Feinberg

New species: Meteoran

Time pressure often creates exciting gameplay and interesting
tradeoffs. Baseline Dungeon Crawl uses the Zot Clock to add a
very weak form of time pressure, but there's so much variety
between the playstyles of different species and backgrounds
that a tight clock for some would be almost impossible for
others.

So, let's try limiting that gameplay to just one species!
Meteorae have an exciting variety of bonuses - great attributes
and aptitudes across the board, passive mapping, and exploration
healing, regaining HP and MP when viewing new territory. In
exchange, they have one big downside: instead of getting 6,000
turns of Zot clock for each floor, they get 600!

The big concern here is whether this species can be made fun
without also being made wildly, boringly 'overpowered'. Lots of
levers and knobs to tweak, so let's give it a shot!

Extra notes:
- Meteorae are humanoid beings. (In the night sky, they look
  like dots because they're very far up.) Hat tip to Neil Gaiman's
  Stardust.
- This commit has a silly 'flavour' gimmick where Meteorae's LOS
  radius decreases by 2 when they have less than 50 turns left
  of Zot clock, and again when they have less than 10. Darkness
  is closing in...
- Meteorae glow in the dark. Permanent backlit status (not halo!):
  +enemy to hit, -stealth, disables invis. Suppressed in forms.
  Seems funny.

Credit to hellmonk for the initial version of this species and
pushing to make 'em happen. :)

---
## [metabase/metabase](https://github.com/metabase/metabase)@[9c4e73899e...](https://github.com/metabase/metabase/commit/9c4e73899e8914fd41e85987d4a652a9b6058d8a)
#### Monday 2022-06-27 09:52:16 by dpsutton

Enterprise settings (#23441)

* Allow for disabling settings

Disabled settings will return their default value (else nil if no
default is set). This allows us to have enterprise override settings and
use them from regular OSS code without classloaders, extra vars,
remembering to check if the feature is enabled, etc.

Motivating examples are the appearance settings. We allow
`application-font` setting to change the font of the application. This
is an enterprise feature, but anyone can post to
`api/setting/application-font` and set a new value or startup as
`MB_APPLICATION_FONT=comic-sans java -jar metabase.jar` and have the
functionality.

Same thing for application colors in static viz. The calling code just
calls `(settings/application-colors)` and uses them but doesn't check if
the enterprise settings are enabled. To do this correctly, you have to
remember to implement the following onerous procedure:

A whole namespace for a setting
```clojure
(ns metabase-enterprise.embedding.utils
  (:require [metabase.models.setting :as setting :refer [defsetting]]
            [metabase.public-settings :as public-settings]
            [metabase.public-settings.premium-features :as premium-features]
            [metabase.util.i18n :refer [deferred-tru]]))

(defsetting notification-link-base-url
  (deferred-tru "By default \"Site Url\" is used in notification links, but can be overridden.")
  :visibility :internal
  :getter (fn []
            (when (premium-features/hide-embed-branding?)
              (or (setting/get-value-of-type :string :notification-link-base-url)
                  (public-settings/site-url)))))
```

And then in the calling code you have to do the procedure to
conditionally require it and put it behind a var that can handle it
being nil:

```clojure
;; we want to load this at the top level so the Setting the namespace defines gets loaded
(def ^:private site-url*
  (or (u/ignore-exceptions
        (classloader/require 'metabase-enterprise.embedding.utils)
        (resolve 'metabase-enterprise.embedding.utils/notification-link-base-url))
      (constantly nil)))

;; and then the usage
(defn- site-url
  "Return the Notification Link Base URL if set by enterprise env var, or Site URL."
  []
  (or (site-url*) (public-settings/site-url)))
```

Far nicer to just place the following into the regular public-settings
namespace:

```clojure
(defsetting notification-link-base-url
  (deferred-tru "By default \"Site Url\" is used in notification links, but can be overridden.")
  :visibility :internal
  :enabled?    premium-features/hide-embed-branding?)
```

Then no need for a custom namespace to hold this setting, no need to
have an extra var to point to the setting else a fallback value.

Note that this feature is not required on every enterprise feature we
have. We a namespace `metabase-enterprise.sso.integrations.sso-settings`
that has 24 settings in it, all of which are enterprise features. But
these features are used in our enterprise sso offerings and are directly
referenced from the enterprise features. No need for the extra var to
point to them and the flag checks happen in other parts.

* Mark the UI/UX customization settings as requiring whitelabeling

Mark the following settings as requiring
premium-settings/enable-whitelabeling? (aka token check)

- application-name
- loading-message (override of "doing science")
- show-metabot (override of showing our friendly metabot)
- application-colors
- application-font
- application-logo-url
- application-favicon-url

Updates the helper functions for colors to use the setting rather than
feeling entitled to use a lower level `setting/get-value-of-type`. We
need the higher level api so it takes into account if its enabled or
not.

* Move notification-link-base-url into regular settings with enabled?

* Cleanup ns

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[e86dbe8d99...](https://github.com/mrakgr/The-Spiral-Language/commit/e86dbe8d999d96639986ac727d19d68a69c7acf5)
#### Monday 2022-06-27 10:11:51 by Marko Grdinić

"10am. Let me do the chores here for a bit. I finally got up earlier.

10:25am. Done with chores. Let me chill for a bit and then I will start grinding drawings. What I am going to do here is the simplest thing ever, just trace over the model, color and then shade it.

Also I've decided to change the intro scene a bit. Rather than the foggy halo which looks like an UFO is beaming up the city, I am going to do a bloom effect. and maybe some sun beams after that. That will get me what I want. Instead of using the renderer, I'll use the compositor to make the scene properly impactful.

https://youtu.be/SN8nJXn7CqI
How to add BLOOM effect in CYCLES with ease - Blender

Let me refresh my memory of this.

https://youtu.be/SN8nJXn7CqI?t=94

He is using glare, not blur. This is the only thing I wasn't really sure of.

10:35am. Ok, I see. Let me chill a bit here and then I will start.

10:50am. Let me start. It is time to draw this. Genshin Impact is downloading in the background. And at 5pm I have an appointment with a haircutter. I'll leave that out of mind and just get cracking. Let me draw Gnosis and Luna. This should not be that difficult if I use vector lines.

10:55am. This is really strange, why is it rotating with the left mouse button all of a sudden?

11:20am. Yesterday I said: 'How difficult can it be?'

Right now, even with tracing I think it is very difficult in fact.

Let me focus on just the face. Forget the body. I'll zoom in the 3d camera so I have proper room.

Also forget the vector lines. Let me try being loose and seeing where that gets me. If I can grasp the face, I'll be able to grasp anything else. If I can't do it, I'll just go back to Blender and make some 3d models. I am sure I could do those. Maybe I'll use Genshin Impact as inspiration.

11:40am. No, forget it. I am giving up on 2d.

Take programming, my skills in it at a very high level, and the way I reason out programs is not something I'd ever be able to teach anybody else. It is like my brain has a MCTS engine built in that it uses to sample possible programs and it gradually builds up features, guiding me towards the completed product.

As I write code, there is a feedback loop between that internal process and writing. The code on the screen acts as another form of memory, and this greatly resembles sketching in art.

I am not sure if even 1 in a 1,000 people could do it at my level. And since that is the case, it is not strange for me that my brain wiring might not be suitable in other domains such as art, while others' could. It is suitable for one thing, and might not be suitable for another thing. If drawing or painting was that easy, I bet a lot of the RR writers would be doing it. I am probably not the only one who had this great entrepreneurial idea. I was just the one willing to put in effort.

11:50am. I have the high level vision, but it is really difficult convert that into an actual drawing.

This is not to say that the high level features are useless, just that process itself is difficult. I've put all my effort in the past 9 months into 3d, and there is little transfer between that and 2d. I am not going to be able to draw unless I spend a significant time practicing it.

Forget it. There are other paths I can take. I'll just just put 'blender anime head' into Youtube and move from there. I already know how to sculpt heads, and will be able to use that skill as the basis.

12pm. https://www.youtube.com/results?search_query=blender+anime+head

Isn't 2022 grand. Imagine trying to take this path 10 years ago. I'd have gotten nowhere and needed to give up.

https://www.youtube.com/watch?v=t1O7LpOTBfM
Jade Moon Upon a Sea of Clouds - Disc 1: Glazed Moon Over the Tides｜Genshin Impact

This OST is 10/10. I actually downloaded and installed the game just because of it, but I won't run it right now otherwise I'd just spend the rest of the day playing it. Right now it is time for breakfast.

After that it is the usual - a ton of tutorials. All of these are hour long so it will take me a few days to go through them, but after that I'll have my charas done and ready.

12:05pm. You know, while I am at it, why not investigate Genshin's style? And that Arcana thing which made waves? I've never watched it. I might as well properly get into the 3d anime style.

Giving up has bad connotations, but if you are going to give up, it is best to do that quickly. It is like selling a stock that is down only 10%. You might taken a loss, but you still have 90% of the capital that you can put into something else. It is better to take a 10% loss and put it into a potential winner than hold it for years and lose 50% and more.

12:10pm. Ok, breakfast."

---
## [Crozzers/screen_brightness_control](https://github.com/Crozzers/screen_brightness_control)@[55566fd5b9...](https://github.com/Crozzers/screen_brightness_control/commit/55566fd5b9604081443a74cddc6d0a0a5b8a767c)
#### Monday 2022-06-27 10:56:22 by Crozzers

Enable cross platform documentation building regardless of OS specific imports.

So when Pdoc would try to import `windows.py`, it would fail if you were building docs on Linux because `windows.py` imports various Windows only libraries that aren't available on Linux.
Furthermore, some of these Windows only objects are used in type hints which are evaluated by Pdoc, meaning I cannot just do what I did in commit 5d5d085.

What we do instead is override Pdoc's module import function (`pdoc.extract.load_module`) to intercept ImportError/ModuleNotFoundError exceptions. Using the exception we then can figure
out what it is that cannot be imported, eg: `from ctypes.wintypes import BOOL`. Once we know this, we then create a fake library in a temporary directory like so:

dummy_imports/dummies/
|-- ctypes/
   |-- __init__.py
   |-- wintypes.py

These fake libraries contain module-level `__getattr__` functions that respond to any request (eg: `from ctypes.wintypes import BOOL`) and return a dummy object that looks like
what you asked for, but is worthless. This allows OS specific imports and type hints to exist as long as the dummy objects are never used within actual code.
This is roughly how these fake modules and dummy objects behave:
```
from ctypes import rando_object
type(rando_object)
> <class 'dummy_imports.DummyObject'>
repr(rando_object)
> 'ctypes.rando_object'
```

Honestly, this is a hack but it's kinda cool at the same time.

---
## [TymurShatillo/Yogstation](https://github.com/TymurShatillo/Yogstation)@[a297304eff...](https://github.com/TymurShatillo/Yogstation/commit/a297304effcf85d7ba9828021df218ffea8f51b3)
#### Monday 2022-06-27 11:13:56 by LazennG

makes some of the recent megafauna drops less shit (#14455)

* this is everything i think idk it's 330am

* polishes some things for now therell probably be more later

* Update miscellaneous.dm

* fuck it critical heal

* you're able to the body entirely

---
## [nekoyoubi/bitburner](https://github.com/nekoyoubi/bitburner)@[45eab596d9...](https://github.com/nekoyoubi/bitburner/commit/45eab596d90987a8edc5004fb593136679e1d558)
#### Monday 2022-06-27 11:38:25 by Nekoyoubi

1.2 - 2.1 - 4.3 - 5.1 - [6.1] - 10.1

- not sure how my gang management script wasn't in there, but it is now... o.0
  - consolidated gang scripts, and added a fair amount of content... whoops  ;x
- server buying stopped assuming norms
- the `Overview` UI script got rid of the preemptive Intelligence display
  - I love that the real one was apparently a dead-ringer for my vision  ;p
  - made Karma tracking more of an average of time; tooltips still give raw numbers
- updated the attack script to affect the market, decrease hack amount, and add a thread min of 1 to avoid over-hack
- created an augmentation listing/buying script because I was tired of forgetting the red pill
- made a script to go and backdoor everything; pretty useless, really
- updated the carpet bomber to be more in-line with my other attack scripts
  - I wanted `loic.js` and `carpet.js` to have similar outcomes
- increased the threshold on buying `SQLInject.exe`
- made the faction script stop Kool-Aid-Man-ing other tasks to hack the auto-hacks
- wrote a terrible little market script; I have some serious work to do there...
- started working on a sleeve script, but they're honestly too much fun to not handle manually right now
- wrote a target script to ease the burden of custom targeting
- made a workout script that I aliased as "gym" for some reason... may rename in the future

---
## [alphagov/govuk-prototype-kit](https://github.com/alphagov/govuk-prototype-kit)@[c012f0ae9e...](https://github.com/alphagov/govuk-prototype-kit/commit/c012f0ae9e9fbd97eb915b55b4b81b7a4fcbac27)
#### Monday 2022-06-27 12:04:31 by Laurence de Bruxelles

Change tests to generate a release archive only once

Use a lockfile to make sure that if the test helper `mkReleaseArchive()`
is called more than once, it won't create more than one
`create-release-archive` process. The behaviour we want is that it all
calls will block until the initial process has finished.

The way I figured to do that was that all calls try and acquire a
lockfile (atomically), if that lockfile is already held that means
another call is already creating the release archive. When the lockfile
is released, the process should have successfully created a release
archive, so no extra work is needed.

Unfortunately, in Node.js it seems there is no way to block waiting for
a lockfile to be released, so we have to rewrite the test utils and all
relevant tests to be asynchronous. To be fair they should have been
asynchronous in the first place, but it was still a very painful
process.

Note that I haven't rewritten the scripts in `cypress/scripts` to use
async functions; without the use of top-level await it was a bit more
effort than I was prepared to do, compounded with the fact that
there doesn't seem to be an easy way to await `child_process.spawn()`
(`util.promisify` doesn't work), and async `child_process.exec()` and
`child_process.execFile()` don't do `stdio: 'inherit'`. Maybe the only
way around it is to use the `execa` library (: Anyway I couldn't be
dealing with that, so now we have to deal with duplication in
`__tests__/util`. There are ...ways... to reduce the duplication
(proper-lockfile does this with its `lib/adapter` module) but they are a
bit magic, and plus it means writing our code using callbacks, which is
just... woof. No.

Anyway as you can tell this is has been a great learning opporunity :')
Just use async the first time and save myself the pain later!!

---
## [james-wallace-ghub/mame](https://github.com/james-wallace-ghub/mame)@[ba63081d10...](https://github.com/james-wallace-ghub/mame/commit/ba63081d109c904902958c6324b013cb10b42732)
#### Monday 2022-06-27 12:18:33 by 0kmg

gameboy.xml: Added 21 more prototypes. (#9962)

* gameboy.xml: Added 21 more prototypes.

New working software list additions
-----------------------------------
Astérix (earlier prototype) [VGHF, Hidden Palace]
Astérix (early prototype) [VGHF, Hidden Palace]
Asteroids (prototype) [VGHF, Hidden Palace]
Barbie - Game Girl (prototype) [VGHF, Hidden Palace]
Battle Ships (Spain, prototype) [VGHF, Hidden Palace]
Blaster Master Boy (USA, prototype) [VGHF, Hidden Palace]
Bomb Jack (earlier prototype) [VGHF, Hidden Palace]
Bomb Jack (later prototype) [VGHF, Hidden Palace]
Bonk's Adventure (USA, prototype) [VGHF, Hidden Palace]
Bubble Ghost (prototype) [VGHF, Hidden Palace]
Catrap (prototype) [Forest of Illusion, Swanhubstream]
Cosmo Tank (USA, prototype) [VGHF, Hidden Palace]
Dropzone (prototype, alt) [VGHF, Hidden Palace]
Gauntlet II (prototype) [Forest of Illusion, Rezrospect]
Ghostbusters II (prototype) [VGHF, Hidden Palace]
Kung-Fu Master (prototype) [Forest of Illusion, FNeogeo]
Mysterium (prototype) [Forest of Illusion, Rezrospect]
Obélix (Europe, French / German, prototype) [Forest of Illusion]
Prince of Persia (prototype) [Forest of Illusion, FNeogeo]
The Blues Brothers (prototype) [Forest of Illusion, FNeogeo]
Triumph (prototype) [Gaming Alexandria]

---
## [RocketChat/Rocket.Chat](https://github.com/RocketChat/Rocket.Chat)@[5a37518e42...](https://github.com/RocketChat/Rocket.Chat/commit/5a37518e42dec114e0ed1a71b5d103b4a62e9b58)
#### Monday 2022-06-27 12:49:10 by Ben Wiederhake

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
## [canalplus/rx-player](https://github.com/canalplus/rx-player)@[ebfaf7498c...](https://github.com/canalplus/rx-player/commit/ebfaf7498c0803b0dc38ffdea3096c8422d388ef)
#### Monday 2022-06-27 13:40:23 by Paul Berberian

Update most dependencies but Jest

This commit update almost all dependencies but jest.

This is because Jest 28 seems to break while running code, presumably
due to `import`/`export` declarations in imported RxJS files (but I do
not think RxJS is at fault here) that lead to an `unexpected token` when
running through Jest.

You could think that the fault is linked to node not understanding
`import`/`export` (linked to CommonJS/ES6 import shenanigans) but it is
even trickier than that as Jest already performed some JavaScript
transformation at that point, which made the import/export inside an
IIFE - and I'm not sure that this is supported anywhere.

After taking ~a day (much more time than I should) trying to play around
to remove that issue, I gave up and avoided updating Jest to its v28.

In the future, I guess we should either:

  - understand what we're supposed to do here to make it work with Jest
    28 (Jest documentation was poor - even without considering the
    sometimes incomprehensible google-translated french one I get each
    time by default on their docusaurus-based documentation)

    Opened GitHub issues were 100% for angular-based applications - as it
    seems the RxJS+TypeScript cocktail is very majoritarily those. Those
    have their own "fix" through another magical angular dependency.

    Moreover, it does not help that Jest's philosophy seems to be trying to be
    extremely simple for users at the cost of some complex behaviors (as an
    example, it looks like it auto-picks a `babel.config.js` file if it
    sees one at the root of the project. If like us you have multiple build
    files at the root depending on the building context, it is not a good
    idea to silently pick random files like that by default).

    I couldn't understand under an acceptable time where the issue was - and
    at which step it happened.
    I just browsed dozens of doc pages, GitHub and StackOverflow issues
    which just proposed to add yet other automagic dependencies (looked like a
    parody of what JavaScript haters talk about!) - which all seemed to have
    no effect whatsoever.

    I also asked for help from other teams at Canal+, but those in the
    same situation (TypeScript and RxJS) also seem to have random issue
    preventing them from doing the switch.

  - Remove RxJS from the code. It's presumably not its fault yet we
    already started doing that, so maybe we'll just raise the jest
    version once RxJS is definitely removed from the RxPlayer.

  - Wait for some kind of Jest fix or new way of handling those?

  - Remove Jest and go with another testing framework.

    I almost did that due to being fed-up with Jest, but it might no be
    as easy as it seems, mostly the module-mocking part as I'm unsure of
    how other framework handle that now and if it is as convenient as
    Jest's way.

---
## [tannerhelland/PhotoDemon](https://github.com/tannerhelland/PhotoDemon)@[8442fbcb41...](https://github.com/tannerhelland/PhotoDemon/commit/8442fbcb41967c7ace2dfb4658ba62147470b868)
#### Monday 2022-06-27 13:41:40 by Tanner

Language file editor: start overhaul to prepare for legit auto-translation capabilities

I'm tired of shipping semi-complete localizations for languages that used to have regular contributors, but no longer do.  Machine translation has come a long way and can likely help, but instead of my past garbage efforts like scraping Google translate results, I want to actually use a proper translation service (DeepL) via a formal API.

Before setting that up, however, I need to rework PD's language editor a bit.  I have now removed the Language Editor dialog from PD's localizer - this means the dialog will always appear in en-US, and the option for localized text on this dialog will not even appear in PD's language files.  I'm doing this because this dialog contains a *lot* of text (almost 700 words - nearly 6% of PhotoDemon's total word count!) and I don't want volunteer translators wasting time here.  This this dialog will only be used by a handful of people, and we know they will already be semi-fluent in en-US (because that's a prerequisite for translating PD's native en-US text).  My sincerest apologies to translators who already localized text here.  I should have resolved this sooner.

After this commit, I'm going to look at using curl to interface with DeepL's API (because curl is what I'm most familiar with; I don't have a lot of experience with native WAPI interfaces for Rest APIs alas).  This should finally provide me with the ability to auto-translate missing phrases with a higher degree of quality.  Note that like any service, DeepL requires you to create an account before handing out an API key - I won't be shipping my API key, obviously, but this will still allow volunteer translators an option to use the "suggest translation" feature if they don't mind grabbing their own API key.  (I'll add an option for this to the UI as part of overhauling the auto-translator.)

Reworking the underlying engine for this dialog could also finally allow me to add things like a "report a localization bug" to all dialogs in nightly builds, which would remove another barrier to long-term language maintenance...

---
## [rrthomas/fontoxpath](https://github.com/rrthomas/fontoxpath)@[8508f2f42b...](https://github.com/rrthomas/fontoxpath/commit/8508f2f42be29cef13056625b50042f05d2a9c15)
#### Monday 2022-06-27 15:37:07 by Martin Middel

[minor] Add a new ResultType.ALL_RESULTS that does no magic

The ANY result type is annoying. It returns a single node, empty arrays, filled arrays, objects,
etcetera.

This was a mistake from the beginning on. While it is very cool to have an XPath 'just work', it
causes bugs and the ugly pattern `if (!Array.isArray(result)) {result = [result])`. Also, attribute
nodes are atomized.

No longer! Just use the ALL_RESULTS type that does _what you expect_. This also deprecates the ANY
result type. FontoXPath 4.0 _will_ drop support for ANY!

---
## [greenbueller/lef-legacy-of-48](https://github.com/greenbueller/lef-legacy-of-48)@[970181d5a7...](https://github.com/greenbueller/lef-legacy-of-48/commit/970181d5a719e294f0d70a943b04a94a8c043862)
#### Monday 2022-06-27 16:02:41 by RanWithAPlan

Removed Jam's shitfuckery

This mod is called Liberty, Egality, Fraternity: legacy of '48. It is based of a world where mnay of the 1848 revolutions succeed, which leads to a weaker europe and a vey different world. This mod was produced with the help and assisstance of RanWithAPlan, (put your name here) and we hope you'll enjoy it.
Have fun,
    The Dev Team

---
## [dcunited001/ellipsis](https://github.com/dcunited001/ellipsis)@[2ac58183e0...](https://github.com/dcunited001/ellipsis/commit/2ac58183e0b76e4e7bd812eaa3c5372c2a4c9773)
#### Monday 2022-06-27 16:08:47 by David Conner

you don't collect on exponential gains if you stop

see? i stopped. i was this close. if you're forced to turn
your linux/emacs upside down, you don't make gains. i'll
forget pretty much everything. there are 10000 things i've
learned that i haven't tried or habituated yet:

+ org-noter + org-ref + a doi-indexed folder structure
+ org-latex with snippets
+ snippets for anything, really (snippets help me habituate
  code patterns since i can't remember shit unless i surround
  with cheatsheets that become disorganized the second i move
  my laptop)
+ custom kernel builds. build farm.
+ accessing remote directories with tramp (req. ssh)
+ accessing I2C/serial terminals via a comint-mode derivative
+ finally configuring an LSP server ..... literally any LSP server
+ actually using clojure

improperly configuring the lexical-binding for my emacs config gave
mode than 12 months of crashes in sway and emacs ..... now it actually
works. but if i stop. that meaningless pain and self-imposed isolation
without an IRL convo about emacs? it remains meaningless.

... but now sympy and TF work within julia.

(and i haven't hit a conda lib or patched bin in conda path yet...)

---
## [cockroachdb/cockroach](https://github.com/cockroachdb/cockroach)@[0a3447944a...](https://github.com/cockroachdb/cockroach/commit/0a3447944ae259b725ebff7d84cecd1b6a1de19c)
#### Monday 2022-06-27 17:39:12 by craig[bot]

Merge #80894 #81200 #81330 #81406

80894: build,gcp: enable nightly config to run GCP unit tests r=adityamaru a=adityamaru

Previously, the `pkg/cloud/gcp` tests package was skipped on CI
because most of the tests require credentials, and we risked exfiltration
of these secrets when running on public teamcity agents.

With the ability to run tests on agents that are not part of the public
pool we now have a `Cloud Unit Test` config that runs these tests nightly.
This change adds the script invoked by the config and cleans up the unit
tests to be more uniform in their authentication and environment variable
checks.

Informs: https://github.com/cockroachdb/cockroach/issues/80877

Release note: None

81200: ui: Improve time picker keyboard input r=jocrl a=jocrl

Fixes #80655, mostly.

Previously, users had to type `1:03 PM (UTC)` in order to enter text into the time picker.

This commit modifies the time picker so that users would instead type either
- `1:03`, or
- `01:03`

to enter text into the time picker. Copying and re-pasting the text from a time picker still works.

Alternate approaches not pursued (these are not needed with the removal of AM/PM).

1) Make our own time picker component, and style it to look like antd's. There's
a general issue of antd's components not being keyboard friendly:
https://github.com/ant-design/ant-design/issues/5685

2) Upgrade to `antd` version 4, and use an undocumented prop type. `antd`'s time
picker uses the time picker from the `rc-picker` library under the hood. In
`rc-picker`, the `format` prop is of type `String | String[]`, where if it's an
array the first value will be used for display and the remaining ones will be
used for parsing, as documented [here](https://react-component.github.io/picker). In theory, `antd` passes `format`
(and also any remaining, additional props in addition to the specified ones) to
the `rc-picker` component. So even though the `antd` `TimePicker` component
`format` prop is not documented to take in a string array, one might think that
passing in a string array anyway would work. In practice, passing in a string
array works in `antd` version `4.20.4`, as tested in the [antd sandbox](https://ant.design/docs/react/getting-started) 
(render `<TimePicker format={
["h:mm A", "h:mma"]}/>`). However, this does not work in our codebase
(which installs `antd` `v3.25.2`), or in the `antd` version `3.x` [sandbox](https://3x.ant.design/docs/react/getting-started). The errors that appear in
these two situations are different, and in a way demonstrate the potential for
breakage from using an undocumented feature in future upgrades from a version
that we've to work. If we do this, we should add a test.

3) Dead end: The `antd` `TimePicker` component takes an `onChange` prop with a
second `timeString` paramater. However, `onChange` only fires if the input is
of the correct, parsable format. The specific code that ignores text input that
is not of a parsable format is in `rc-picker`, [here](https://github.com/react-component/picker/blob/5306c8938aded49c5d6f6b6d4761ddab25e3cce9/src/Picker.tsx#L237).
This prevents us from being the one to do the fuzzy matching and passing the
value back to the component.

Release note (ui): The time picker component has been improved such that users
can use keyboard input to select a time without having to type `" (UTC)"`

81330: authors: add annrpom to authors r=annrpom a=annrpom

Release note: None

81406: geomfn: check NaN coordinates for ST_MinimumBoundingCircle r=rafiss a=otan

Resolves #81277

Release note (bug fix): Fix a bug where ST_MinimumBoundingCircle with
NaN coordinates could panic.

Co-authored-by: Aditya Maru <adityamaru@gmail.com>
Co-authored-by: Josephine Lee <josephine@cockroachlabs.com>
Co-authored-by: Annie Pompa <annie.pompa@cockroachlabs.com>
Co-authored-by: Oliver Tan <otan@cockroachlabs.com>

---
## [The-Aerec/LSB](https://github.com/The-Aerec/LSB)@[ccf500070d...](https://github.com/The-Aerec/LSB/commit/ccf500070d4448d1e2acbdb711190d5b4e21c4e6)
#### Monday 2022-06-27 18:15:27 by neuromancerxi

Add scripts and adjust plumbing for many temp items (#670)

* Add scripts and adjust plumbing for many temp items

Adds Scripts for items.
Adds Effect scripts for X_BOOST_II
Updates Effect scripts for the following:

ACCURACY_BOOST
ATTACK_BOOST
INTENSION
MAGIC_SHIELD
MULTI_STRIKES
MULTI_SHOTS
PAX
PHYSICAL_SHIELD
POTENCY
RAMPART

Adjusts item_usable use times to 1s.

Notes on effects:

Ascetics Tonic/Gambir - +25/+50 MATT/MACC
A big Thank You to Nyu for confirming the Intension effect for MACC.
https://www.bg-wiki.com/bg/Ascetic's_Tonic
https://www.bg-wiki.com/bg/Ascetic's_Gambir

Bravers Drink - +15 to All Stats
https://www.bg-wiki.com/bg/Braver's%20Drink
Reference to Icons/Effects - https://youtu.be/JYT5a_pTA3o?t=20

Champions Tonic - +15 Haste / +3 Crit rate
Champions Drink/Gambir - +18 Haste / +5% Crit rate
Expected Haste effect to be Magic pool based on BG comment (18 and 15)
Critical Hit rate, no data available from community sources, conservative value of 5 (Drink/Gambir) 3 (Tonic)
Both BG and 'clopedia sources confirm Critical Hit Rate (as does the effect description), however, only BG has a reference to Haste value.
https://www.bg-wiki.com/bg/Champion's_Tonic

Gnostics Drink - Enmity -10
No community resources confirm this value, using SCH Animus Minuo as an reference.
https://www.bg-wiki.com/bg/Gnostic's%20Drink
https://www.bg-wiki.com/bg/Animus_Minuo

Monarchs Drink - Regain +3 (30/1000 per tick) for 3 minutes.
https://www.bg-wiki.com/bg/Monarch's_Drink

Stalwart's Tonic/Gambir - ACC/RACC 50/100 ATTP/RATTP 25/50
A big Thank You to Nyu for confirming the effects apply ACC/RACC and ATTP/RATTP across two effects.
https://www.bg-wiki.com/bg/Stalwart's_Tonic
https://www.bg-wiki.com/bg/Stalwart's_Gambir

Berserker's Tonic/Drink - DA 50/100
Thanks to Nyu for confirming the MULTI_STRIKES effect and 1m duration.
https://ffxiclopedia.fandom.com/wiki/Berserker%27s_Drink
No full data on DA rate, minus 'clopedia which has verification tags. Working on the expectation that this follows a good portion of the other items and follows the half potency values for the lesser item.

Swiftshot Tonic/Drink - Double Shot 50/100
https://www.ffxiah.com/forum/topic/28603/fools-tonic-broken#1749569

Dusty Scroll of Reraise - Reraise III, 10m duration.
https://www.bg-wiki.com/bg/Dusty_Reraise

Spiritual Incense/Fools Drink/Tonic/Powder: See effects/magic_shield
Carnal Incense/Fanatics Drink/Tonic/Powder: See effects/physical_shield

* Removed copypasta subp and trailing whitespace.

* Item script clean-up and move effect functions to item_utils.

* Resolve Conflicts

Convert namespace in scripts from item_utils to xi.item_utils
PHYS_ABSORB to Percent from 10000 Scale

---
## [WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER](https://github.com/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER)@[d2e5bc799f...](https://github.com/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/commit/d2e5bc799f4cdca0fc4d5a34b30ec8cfb80abb70)
#### Monday 2022-06-27 19:00:23 by WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER

SCHEDULE OF FINES >> SORRY THIS P.O.S. LAPTOP IS GOING TO BE THE END OF THIS GROUP.

USC 18,§215. Receipt of commissions or gifts for procuring loans

    (a) Whoever-
        (1) corruptly gives, offers, or promises anything of value to any person, with intent to influence or reward an officer, director, employee, agent, or attorney of a financial institution in connection with any business or transaction of such institution; or
        (2) as an officer, director, employee, agent, or attorney of a financial institution, corruptly solicits or demands for the benefit of any person, or corruptly accepts or agrees to accept, anything of value from any person, intending to be influenced or rewarded in connection with any business or transaction of such institution;
        -shall be fined not more than $1,000,000 or three times the value of the thing given, offered, promised, solicited, demanded, accepted, or agreed to be accepted, whichever is greater, or imprisoned not more than 30 years, or both, but if the value of the thing given, offered, promised, solicited, demanded, accepted, or agreed to be accepted does not exceed $1,000, shall be fined under this title or imprisoned not more than one year, or both.
    (c) This section shall not apply to bona fide salary, wages, fees, or other compensation paid, or expenses paid or reimbursed, in the usual course of business.
    (d) Federal agencies with responsibility for regulating a financial institution shall jointly establish such guidelines as are appropriate to assist an officer, director, employee, agent, or attorney of a financial institution to comply with this section. Such agencies shall make such guidelines available to the public.

        FILED WITH THE SECURITIES AND EXCHANGE COMMISSION IN 2021,

            UNDER CIK FILER 93715, (1) STATE FARM ASSURANCES FUNDS TRUST.
            - DISCLOSE (2) STATE FARM LIFE INSURANCE COMPANY AS AN OUTSIDE BUSINESS IN THEIR FIRMS CRD FILINGS WITH FINRA, THE SAME ENTITY THAT NOTARIZED AND COUNTERSIGNED ON LOAN 50074, DUALLY BY (3) DONALD ZUCKER WAS EXECUTED ON MAY 13, 2020 - REPRESENTED BY THE ATTORNEYS ON BEHALF OF (4) SULLIVAN PROPERTIES, LP, BELOW FOR CONVENIENCE.

        THE DIRECTORS OF STATE FARM, WHO FILED WITH THE SECURITIES AND EXCHANGE COMISSION.

            BY:     (5) DAVID MOORE, (6) JOESEPH MONK, (7)PAUL J SMITH, AND UNDER (8)TERRENCE LUDWIG [AND OTHER DIRECTORS OF STATE FARM]

        THE DIRECTORS OF STATE FARM, WHO FILED WITH THE FINANCIAL INDUSTRY REGULATORY AUTHORITY ON BEHALF OF (16) STATE FARM VP MANAGEMENT CORP.

            BY: (8) TERRENCE LUDWIG

                        A TOTAL AMOUNT WAS ACCEPTED FOR A "SUCCESSFUL MERGER",

                        APPROXIMATELY $412,500 USD IN COMPENSATION WAS FILED WITH THE SEC.

USC 18, §241. Conspiracy against rights.
    - If two or more persons conspire to injure, oppress, threaten, or intimidate any person in any State, Territory, Commonwealth, Possession, or District in the free exercise or enjoyment of any right or privilege secured to him by the Constitution or laws of the United States, or because of his having so exercised the same; or
    - If two or more persons go in disguise on the highway, or on the premises of another, with intent to prevent or hinder his free exercise or enjoyment of any right or privilege so secured—


            EXHIBITS FILED AND ANNEXED IN THE DOCKETS IN NY SUPREME COURT CIVIL MATTER

            NYSCEF 153974/2020

USC 18,§225. Continuing financial crimes enterprise
    (a) Whoever-
        (1) organizes, manages, or supervises a continuing financial crimes enterprise; and
        (2) receives $5,000,000 or more in gross receipts from such enterprise during any 24-month period
    -shall be fined not more than $10,000,000 if an individual, or $20,000,000 if an organization, and imprisoned for a term of not less than 10 years and which may be life.
    (b) For purposes of subsection (a), the term "continuing financial crimes enterprise" means a series of violations under section 215, 656, 657, 1005, 1006, 1007, 1014, 1032, or 1344 of this title, or section 1341 or 1343 affecting a financial institution, committed by at least 4 persons acting in concert.        
              [ LOAN 50074: $6,000,000 ] ANNEXED IN DOCKETS 309-315 IN NYSCEF MATTER 153974/2020

                    ANNEXED IN NY SUPREME COURT MATTER 153974/2020
                    REPRESENTATIVES OF (9) SULLIVAN PROPERTIES LP, (10) SULLIVAN GP LLC, (11) MANHATTAN SKYLINE MANAGEMENT CORP.
                   

                    BY:     (12) SHARI LASKOWITZ, (13) ASHLEY HUMPHRIES, (14) CORY WEISS, AND (15) PAUL REGAN

                        DOCKETS ANNEXED IN NYSCEF 153974/2020 AND ALSO FILED WITH THE NY DEPT OF FINANCE.

                    OBO:     (3) DONALD ZUCKER, (17) LAURIE ZUCKER, AND OTHERS WHO I AM UNFAMILIAR TO THEIR RESPECTIVE SHARES HELD AS LIMITED PARTNERS OF SULLIVAN PROPERTIES LP.

                    UNLAWFULLY (USC 18.21) PRESENTED THE IMPLIED RETURNS FOR 6 PROPERTIES WHICH WERE ALSO FILED, AND
                    >PUBLICLY AVAILABLE TO ALL REGULAR /COMPETENT PERSONS.

                    USED TO PROCURE AND OBTAIN A LOAN FOR $6,000,000.00 ( SIX MILLION US DOLLARS) AND USED THE FOLLOWING ENTITY ON THE COVER PAGE:

                    (18) THE ZUCKER ORGANIZATION LLC
USC 18, § 373 - Solicitation to commit a crime of violence

(a) Whoever, with intent that another person engage in conduct constituting a felony that has as an element the use, attempted use, or threatened use of physical force against property or against the person of another in violation of the laws of the United States, and under circumstances strongly corroborative of that intent, solicits, commands, induces, or otherwise endeavours to persuade such other person to engage in such conduct, shall be imprisoned not more than one-half the maximum term of imprisonment or (notwithstanding section 3571) fined not more than one-half of the maximum fine prescribed for the punishment of the crime solicited, or both; or if the crime solicited is punishable by life imprisonment or death, shall be imprisoned for not more than twenty years.

                (15)<voicemail attached>

(b) It is an affirmative defence to a prosecution under this section that, under circumstances manifesting a voluntary and complete renunciation of his criminal intent, the defendant prevented the commission of the crime solicited. A renunciation is not "voluntary and complete" if it is motivated in whole or in part by a decision to postpone the commission of the crime until another time or to substitute another victim or another but similar objective. If the defendant raises the affirmative defence at trial, the defendant has the burden of proving the defence by a preponderance of the evidence.
    (c) It is not a defence to a prosecution under this section that the person solicited could not be convicted of the crime because he lacked the state of mind required for its commission, because he was incompetent or irresponsible, or because he is immune from prosecution or is not subject to prosecution.
USC 18 [ FORFEITURES ] >> RISKS HELD UNDER STATE FARM AT THE OBSTRUCTION OF THE COUNSELORS IN NYSCEF 153974/2020

§229B. Criminal forfeitures; destruction of weapons
    (a) Property Subject to Criminal Forfeiture.
    -Any person convicted under section 229A(a) shall forfeit to the United States irrespective of any provision of State law-
        (1) any property, real or personal, owned, possessed, or used by a person involved in the offense;
        (2) any property constituting, or derived from, and proceeds the person obtained, directly or indirectly, as the result of such violation; and
        (3) any of the property used in any manner or part, to commit, or to facilitate the commission of, such violation.

    The court, in imposing sentence on such person, shall order, in addition to any other sentence imposed pursuant to section 229A(a), that the person forfeit to the United States all property described in this subsection. In lieu of a fine otherwise authorized by section 229A(a), a defendant who derived profits or other proceeds from an offense may be fined not more than twice the gross profits or other proceeds.
    (b) Procedures.-
        (1) General.
        -Property subject to forfeiture under this section, any seizure and disposition thereof, and any administrative or judicial proceeding in relation thereto, shall be governed by subsections (b) through (p) of section 413 of the Comprehensive Drug Abuse Prevention and Control Act of 1970 (21 U.S.C. 853), except that any reference under those subsections to-
            (A) "this subchapter or subchapter II" shall be deemed to be a reference to section 229A(a); and
            (B) "subsection (a)" shall be deemed to be a reference to subsection (a) of this section.
        (2) Temporary restraining orders.-
            (A)     In general.-For the purposes of forfeiture proceedings under this section, a temporary restraining order may be entered upon application of the United States without notice or opportunity for a hearing when an information or indictment has not yet been filed with respect to the property, if, in addition to the circumstances described in section 413(e)(2) of the Comprehensive Drug Abuse Prevention and Control Act of 1970 (21 U.S.C. 853(e)(2)), the United States demonstrates that there is probable cause to believe that the property with respect to which the order is sought would, in the event of conviction, be subject to forfeiture under this section and exigent circumstances exist that place the life or health of any person in danger.
            (B)     Warrant of seizure.-If the court enters a temporary restraining order under this paragraph, it shall also issue a warrant authorizing the seizure of such property.
            (C)     Applicable procedures.-The procedures and time limits applicable to temporary restraining orders under section 413(e)(2) and (3) of the Comprehensive Drug Abuse Prevention and Control Act of 1970 (21 U.S.C. 853(e)(2) and (3)) shall apply to temporary restraining orders under this paragraph.   
    (c) Affirmative Defense.
        -It is an affirmative defense against a forfeiture under subsection (b) that the property-
        (1) is for a purpose not prohibited under the Chemical Weapons Convention; and
        (2) is of a type and quantity that under the circumstances is consistent with that purpose.
    (d) Destruction or Other Disposition.-The Attorney General shall provide for the destruction or other appropriate disposition of any chemical weapon seized and forfeited pursuant to this section.
    (e) Assistance.
    (f) Owner Liability.
        -The owner or possessor of any property seized under this section shall be liable to the United States for any expenses incurred incident to the seizure, including any expenses relating to the handling, storage, transportation, and destruction or other disposition of the seized property
USC 18, §218. Voiding transactions in violation of chapter; recovery by the United States

    In addition to any other remedies provided by law the President or, under regulations prescribed by him, the head of any department or agency involved, may declare void and rescind any contract, loan, grant, subsidy, license, right, permit, franchise, use, authority, privilege, benefit, certificate, ruling, decision, opinion, or rate schedule awarded, granted, paid, furnished, or published, or the performance of any service or transfer or delivery of any thing to, by or for any agency of the United States or officer or employee of the United States or person acting on behalf thereof, in relation to which there has been a final conviction for any violation of this chapter, and the United States shall be entitled to recover in addition to any penalty prescribed by law or in a contract the amount expended or the thing transferred or delivered on its behalf, or the reasonable value thereof.


NOTE: I OFFERED THE DEFAULT CLAUSE OF THE LOAN SO THAT STATE FARM CAN CANCEL THE LOAN, EXECUTED AND FILED THE SAME AS EXHIBIT 420 IN NYSCEF MATTER 153974/2020. NONE OF THE INDIVUALS FROM STATE FARM HAVE RESPONDED TO THIS EFFECT SINCE THEN, AND MOST RECENTLY, MR. DAVID MOORE ATTEMPTED TO PLACE A CO-WORKER IN HIS PLACE, MISS JANNA UNDERWOOD WHO I UNDERSTAND IS NOT A DIRECTOR OF STATE FARM, ON THE BASIS OF FILINGS AND DOCUMENTS THAT ARE AVAILABLE, PER THE FINANCIAL INDUSTRY REGULATORY AUTHORITY AND THE SECURITIES AND EXCHANGE COMMISSION UNDER CIK FILER 93715, AND CIK FILER 1516523.


USC 18, §216. Penalties and injunctions
    (a) The punishment for an offense under section 203, 204, 205, 207, 208, or 209 of this title is the following:
        (1) Whoever engages in the conduct constituting the offense shall be imprisoned for not more than one year or fined in the amount set forth in this title, or both.
        (2) Whoever willfully engages in the conduct constituting the offense shall be imprisoned for not more than five years or fined in the amount set forth in this title, or both.
    (b)     The Attorney General may bring a civil action in the appropriate United States district court against any person who engages in conduct constituting an offense under section 203, 204, 205, 207, 208, or 209 of this title and, upon proof of such conduct by a preponderance of the evidence, such person shall be subject to a civil penalty of not more than $50,000 for each violation or the amount of compensation which the person received or offered for the prohibited conduct, whichever amount is greater. The imposition of a civil penalty under this subsection does not preclude any other criminal or civil statutory, common law, or administrative remedy, which is available by law to the United States or any other person.
    (c) If the Attorney General has reason to believe that a person is engaging in conduct constituting an offense under section 203, 204, 205, 207, 208, or 209 of this title, the Attorney General may petition an appropriate United States district court for an order prohibiting that person from engaging in such conduct. The court may issue an order prohibiting that person from engaging in such conduct if the court finds that the conduct constitutes such an offense. The filing of a petition under this section does not preclude any other remedy which is available by law to the United States or any other person.


A LITTLE WIGGLE ROOM HERE IN THIS GREY AREA.

§246. Deprivation of relief benefits
    Whoever directly or indirectly deprives, attempts to deprive, or threatens to deprive any person of any employment, position, work, compensation, or other benefit provided for or made possible in whole or in part by any Act of Congress appropriating funds for work relief or relief purposes, on account of political affiliation, race, color, sex, religion, or national origin, shall be fined under this title, or imprisoned not more than one year, or both.


§220. Illegal remunerations for referrals to recovery homes, clinical treatment facilities, and laboratories
(a) Offense.-Except as provided in subsection (b), whoever, with respect to services covered by a health care benefit program, in or affecting interstate or foreign commerce, knowingly and willfully-
    (1) solicits or receives any remuneration (including any kickback, bribe, or rebate) directly or indirectly, overtly or covertly, in cash or in kind, in return for referring a patient or patronage to a recovery home, clinical treatment facility, or laboratory; or
    (2) pays or offers any remuneration (including any kickback, bribe, or rebate) directly or indirectly, overtly or covertly, in cash or in kind-
        (A) to induce a referral of an individual to a recovery home, clinical treatment facility, or laboratory; or
        (B) in exchange for an individual using the services of that recovery home, clinical treatment facility, or laboratory,
    -shall be fined not more than $200,000, imprisoned not more than 10 years, or both, for each occurrence.

(b) Applicability.-Subsection (a) shall not apply to-
    (1) a discount or other reduction in price obtained by a provider of services or other entity under a health care benefit program if the reduction in price is properly disclosed and appropriately reflected in the costs claimed or charges made by the provider or entity;
    (2) a payment made by an employer to an employee or independent contractor (who has a bona fide employment or contractual relationship with such employer) for employment, if the employee's payment is not determined by or does not vary by-
        (A) the number of individuals referred to a particular recovery home, clinical treatment facility, or laboratory;
        (B) the number of tests or procedures performed; or
        (C) the amount billed to or received from, in part or in whole, the health care benefit program from the individuals referred to a particular recovery home, clinical treatment facility, or laboratory;
    (3) a discount in the price of an applicable drug of a manufacturer that is furnished to an applicable beneficiary under the Medicare coverage gap discount program under section 1860D–14A(g) of the Social Security Act (42 U.S.C. 1395w–114a(g));
    (4) a payment made by a principal to an agent as compensation for the services of the agent under a personal services and management contract that meets the requirements of section 1001.952(d) of title 42, Code of Federal Regulations, as in effect on the date of enactment of this section;
    (5) a waiver or discount (as defined in section 1001.952(h)(5) of title 42, Code of Federal Regulations, or any successor regulation) of any coinsurance or copayment by a health care benefit program if-
        (A) the waiver or discount is not routinely provided; and
        (B) the waiver or discount is provided in good faith;
    (6) a remuneration described in section 1128B(b)(3)(I) of the Social Security Act (42 U.S.C. 1320a–7b(b)(3)(I));
    (7) a remuneration made pursuant to an alternative payment model (as defined in section 1833(z)(3)(C) of the Social Security Act) or pursuant to a payment arrangement used by a State, health insurance issuer, or group health plan if the Secretary of Health and Human Services has determined that such arrangement is necessary for care coordination or value-based care; or
    (8) any other payment, remuneration, discount, or reduction as determined by the Attorney General, in consultation with the Secretary of Health and Human Services, by regulation.
    
    (c) Regulations.
    -The Attorney General, in consultation with the Secretary of Health and Human Services, may promulgate regulations to clarify the exceptions described in subsection (b).
    (d) Preemption.-
        (1) Federal law.-This section shall not apply to conduct that is prohibited under section 1128B of the Social Security Act (42 U.S.C. 1320a–7b).
        (2) State law.-Nothing in this section shall be construed to occupy the field in which any provisions of this section operate to the exclusion of State laws on the same subject matter.

    (e) Definitions.-In this section-
        (1) the terms "applicable beneficiary" and "applicable drug" have the meanings given those terms in section 1860D–14A(g) of the Social Security Act (42 U.S.C. 1395w–114a(g));
        (2) the term "clinical treatment facility" means a medical setting, other than a hospital, that provides detoxification, risk reduction, outpatient treatment and care, residential treatment, or rehabilitation for substance use, pursuant to licensure or certification under State law;
        (3) the term "health care benefit program" has the meaning given the term in section 24(b);
        (4) the term "laboratory" has the meaning given the term in section 353 of the Public Health Service Act (42 U.S.C. 263a); and
        (5) the term "recovery home" means a shared living environment that is, or purports to be, free from alcohol and illicit drug use and centered on peer support and connection to services that promote sustained recovery from substance use disorders.

 – SO I HOPE YOU UNDERSTAND WHERE THIS ALSO PRESENTS A CONFLICT, AS HE BELIEVES THIS TO BE TRUE.
1_u.s._v._brian_benjamin_indictment (1).pdf
-------- Forwarded Message --------
Subject: 	Voicemail from Mr. PAUL regan
Date: 	Sun, 26 Jun 2022 16:51:47 -0400
From: 	BO DINCER <bondstrt007@gmail.com>
To: 	customerservice@nypost.com, espnfrontrow@espn.com, teschmann@mskyline.com, Joseph Giamboi, ESQ <joseph.giamboi@brooklaw.edu>, LZUCKER@mskyline.com, sgo2107@columbia.edu, letters@nypost.com, Laskowitz, Shari <slaskowitz@ingramllp.com>, dallas-reserve-mgmt@dal.frb.org, 23pctdvo@nypd.com, 23pctyco@nypd.org, 1pctdvo@nypd.org, 1pctyco@nypd.org, praghuram2@bloomberg.net, PRIYA.RAGHURAM@MORGANSTANLEY.COM <PRIYA.RAGHURAM@morganstanley.com>, JAMES GORMAN [MORGAN STANLEY] <james.gorman@morganstanley.com>, Dow Jones <wsjprosupport@dowjones.com>, paul.jones@tudor.com, Paul Regan <LEGAL@mskyline.com>, LEGALASST@mskyline.com, MSKYLINE <anne@thehighlandpartners.com>, cweiss@ingramllp.com, info@statefarm.com, State Farm <mutualfunds@statefarm.com>, David Moore <david.moore.ct95@statefarm.com>, hillary.davis@latimes.com, Scott Holcomb <scott@holcombward.com>, SOHO HOUSE <membership@sohohouse.com>
CC: 	KATHY HOCHUL <governor.hochul@exec.ny.gov>, BBO 121 <ms60710444266@yahoo.com>, MIT Sloan Executive Education <executive_education@mailsvc.sloan.mit.edu>, Marc Lavigne <tessier3@stanford.edu>, NYSCEF PROCESS HD <oca_hd_processor@nycourts.gov>, The New York Times <help@nytimes.com>, administration@mskyline.com, MANHATTAN SKYLINE, LLC. <ADMINISTRATOR@mskyline.com>


I am terrified, where is he ? Touching himself or making videos with my Glamour shots.

Thats actually a compound, in the scope of avoidance to prosecution. 

Truly a delusional group, never met them.

---
## [WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER](https://github.com/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER)@[0a5062184e...](https://github.com/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/commit/0a5062184ea1450f59a97f0a4db39bba7f757f0c)
#### Monday 2022-06-27 19:20:29 by WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER

USC 18, §216. Penalties and injunctions

USC 18. VIOLATIONS ANNEXED IN NYSCEF 153974/2020 [ LOAN 50074 ]

§21. Stolen or counterfeit nature of property for certain crimes defined
    (a) Wherever in this title it is an element of an offense that-
        (1) any property was embezzled, robbed, stolen, converted, taken, altered, counterfeited, falsely made, forged, or obliterated; and
        (2) the defendant knew that the property was of such character;
            -such element may be established by proof that the defendant, after or as a result of an official representation as to the nature of the property, believed the property to be embezzled, robbed, stolen, converted, taken, altered, counterfeited, falsely made, forged, or obliterated.
            -(b) For purposes of this section, the term "official representation" means any representation made by a Federal law enforcement officer (as defined in section 115) or by another person at the direction or with the approval of such an officer.


    §2. - Principals (a) Whoever commits an offense against the United States or aids, abets, counsels, commands, induces or procures its commission, is punishable as a principal. (b) Whoever willfully causes an act to be done which if directly performed by him or another would be an offense against the United States, is punishable as a principal.

    §3. - Accessory after the fact Whoever, knowing that an offense against the United States has been committed, receives, relieves, comforts or assists the offender in order to hinder or prevent his apprehension, trial or punishment, is an accessory after the fact. Except as otherwise expressly provided by any Act of Congress, an accessory after the fact shall be imprisoned not more than one-half the maximum term of imprisonment or (notwithstanding section 3571) fined not more than one-half the maximum fine prescribed for the punishment of the principal, or both; or if the principal is punishable by life imprisonment or death, the accessory shall be imprisoned not more than 15 years.

    §4. Misprision of felony Whoever, having knowledge of the actual commission of a felony cognizable by a court of the United States, conceals and does not as soon as possible make known the same to some judge or other person in civil or military authority under the United States, shall be fined under this title or imprisoned not more than three years, or both.

USC 18,§215. Receipt of commissions or gifts for procuring loans

    (a) Whoever-
        (1) corruptly gives, offers, or promises anything of value to any person, with intent to influence or reward an officer, director, employee, agent, or attorney of a financial institution in connection with any business or transaction of such institution; or
        (2) as an officer, director, employee, agent, or attorney of a financial institution, corruptly solicits or demands for the benefit of any person, or corruptly accepts or agrees to accept, anything of value from any person, intending to be influenced or rewarded in connection with any business or transaction of such institution;
        -shall be fined not more than $1,000,000 or three times the value of the thing given, offered, promised, solicited, demanded, accepted, or agreed to be accepted, whichever is greater, or imprisoned not more than 30 years, or both, but if the value of the thing given, offered, promised, solicited, demanded, accepted, or agreed to be accepted does not exceed $1,000, shall be fined under this title or imprisoned not more than one year, or both.
    (c) This section shall not apply to bona fide salary, wages, fees, or other compensation paid, or expenses paid or reimbursed, in the usual course of business.
    (d) Federal agencies with responsibility for regulating a financial institution shall jointly establish such guidelines as are appropriate to assist an officer, director, employee, agent, or attorney of a financial institution to comply with this section. Such agencies shall make such guidelines available to the public.

        FILED WITH THE SECURITIES AND EXCHANGE COMMISSION IN 2021,

            UNDER CIK FILER 93715, (1) STATE FARM ASSURANCES FUNDS TRUST.
            - DISCLOSE (2) STATE FARM LIFE INSURANCE COMPANY AS AN OUTSIDE BUSINESS IN THEIR FIRMS CRD FILINGS WITH FINRA, THE SAME ENTITY THAT NOTARIZED AND COUNTERSIGNED ON LOAN 50074, DUALLY BY (3) DONALD ZUCKER WAS EXECUTED ON MAY 13, 2020 - REPRESENTED BY THE ATTORNEYS ON BEHALF OF (4) SULLIVAN PROPERTIES, LP, BELOW FOR CONVENIENCE.

        THE DIRECTORS OF STATE FARM, WHO FILED WITH THE SECURITIES AND EXCHANGE COMISSION.

            BY:     (5) DAVID MOORE, (6) JOESEPH MONK, (7)PAUL J SMITH, AND UNDER (8)TERRENCE LUDWIG [AND OTHER DIRECTORS OF STATE FARM]

        THE DIRECTORS OF STATE FARM, WHO FILED WITH THE FINANCIAL INDUSTRY REGULATORY AUTHORITY ON BEHALF OF (16) STATE FARM VP MANAGEMENT CORP.

            BY: (8) TERRENCE LUDWIG

                        A TOTAL AMOUNT WAS ACCEPTED FOR A "SUCCESSFUL MERGER",

                        APPROXIMATELY $412,500 USD IN COMPENSATION WAS FILED WITH THE SEC.

USC 18, §241. Conspiracy against rights.
    - If two or more persons conspire to injure, oppress, threaten, or intimidate any person in any State, Territory, Commonwealth, Possession, or District in the free exercise or enjoyment of any right or privilege secured to him by the Constitution or laws of the United States, or because of his having so exercised the same; or
    - If two or more persons go in disguise on the highway, or on the premises of another, with intent to prevent or hinder his free exercise or enjoyment of any right or privilege so secured—


            EXHIBITS FILED AND ANNEXED IN THE DOCKETS IN NY SUPREME COURT CIVIL MATTER

                    NYSCEF 153974/2020

USC 18,§225. Continuing financial crimes enterprise
    (a) Whoever-
        (1) organizes, manages, or supervises a continuing financial crimes enterprise; and
        (2) receives $5,000,000 or more in gross receipts from such enterprise during any 24-month period
    -shall be fined not more than $10,000,000 if an individual, or $20,000,000 if an organization, and imprisoned for a term of not less than 10 years and which may be life.
    (b) For purposes of subsection (a), the term "continuing financial crimes enterprise" means a series of violations under section 215, 656, 657, 1005, 1006, 1007, 1014, 1032, or 1344 of this title, or section 1341 or 1343 affecting a financial institution, committed by at least 4 persons acting in concert.        
              [ LOAN 50074: $6,000,000 ] ANNEXED IN DOCKETS 309-315 IN NYSCEF MATTER 153974/2020

                    ANNEXED IN NY SUPREME COURT MATTER 153974/2020
                    REPRESENTATIVES OF

                    (9) SULLIVAN PROPERTIES LP, (10) SULLIVAN GP LLC, (11) MANHATTAN SKYLINE MANAGEMENT CORP.
                   

                    BY:     COUNSELORS FOR PLAINTIFFS IN NYSCEF 153974/2020 [ ANNEXED THEREIN ] THE VIOLATION OF PRIVACY, AS SUPPLEMENT...

                    (12) SHARI LASKOWITZ, (13) ASHLEY HUMPHRIES, (14) CORY WEISS, AND (15) PAUL REGAN

                        DOCKETS ANNEXED IN NYSCEF 153974/2020 AND ALSO FILED WITH THE NY DEPT OF FINANCE.

                    OBO:     (3) DONALD ZUCKER, (17) LAURIE ZUCKER, AND OTHERS WHO I AM UNFAMILIAR TO THEIR RESPECTIVE SHARES HELD AS LIMITED PARTNERS OF SULLIVAN PROPERTIES LP.

                    UNLAWFULLY (USC 18.21) PRESENTED THE IMPLIED RETURNS FOR 6 PROPERTIES WHICH WERE ALSO FILED, AND
                    >PUBLICLY AVAILABLE TO ALL REGULAR /COMPETENT PERSONS.

                    USED TO PROCURE AND OBTAIN A LOAN FOR $6,000,000.00 ( SIX MILLION US DOLLARS) AND USED THE FOLLOWING ENTITY ON THE COVER PAGE:

                    (18) THE ZUCKER ORGANIZATION LLC
USC 18, § 373 - Solicitation to commit a crime of violence

(a) Whoever, with intent that another person engage in conduct constituting a felony that has as an element the use, attempted use, or threatened use of physical force against property or against the person of another in violation of the laws of the United States, and under circumstances strongly corroborative of that intent, solicits, commands, induces, or otherwise endeavours to persuade such other person to engage in such conduct, shall be imprisoned not more than one-half the maximum term of imprisonment or (notwithstanding section 3571) fined not more than one-half of the maximum fine prescribed for the punishment of the crime solicited, or both; or if the crime solicited is punishable by life imprisonment or death, shall be imprisoned for not more than twenty years.

                (15)    <voicemail attached>

(b) It is an affirmative defence to a prosecution under this section that, under circumstances manifesting a voluntary and complete renunciation of his criminal intent, the defendant prevented the commission of the crime solicited. A renunciation is not "voluntary and complete" if it is motivated in whole or in part by a decision to postpone the commission of the crime until another time or to substitute another victim or another but similar objective. If the defendant raises the affirmative defence at trial, the defendant has the burden of proving the defence by a preponderance of the evidence.
    (c) It is not a defence to a prosecution under this section that the person solicited could not be convicted of the crime because he lacked the state of mind required for its commission, because he was incompetent or irresponsible, or because he is immune from prosecution or is not subject to prosecution.
USC 18 [ FORFEITURES ] >> RISKS HELD UNDER STATE FARM AT THE OBSTRUCTION OF THE COUNSELORS IN NYSCEF 153974/2020

§229B. Criminal forfeitures; destruction of weapons
    (a) Property Subject to Criminal Forfeiture.
    -Any person convicted under section 229A(a) shall forfeit to the United States irrespective of any provision of State law-
        (1) any property, real or personal, owned, possessed, or used by a person involved in the offense;
        (2) any property constituting, or derived from, and proceeds the person obtained, directly or indirectly, as the result of such violation; and
        (3) any of the property used in any manner or part, to commit, or to facilitate the commission of, such violation.

    The court, in imposing sentence on such person, shall order, in addition to any other sentence imposed pursuant to section 229A(a), that the person forfeit to the United States all property described in this subsection. In lieu of a fine otherwise authorized by section 229A(a), a defendant who derived profits or other proceeds from an offense may be fined not more than twice the gross profits or other proceeds.
    (b) Procedures.-
        (1) General.
        -Property subject to forfeiture under this section, any seizure and disposition thereof, and any administrative or judicial proceeding in relation thereto, shall be governed by subsections (b) through (p) of section 413 of the Comprehensive Drug Abuse Prevention and Control Act of 1970 (21 U.S.C. 853), except that any reference under those subsections to-
            (A) "this subchapter or subchapter II" shall be deemed to be a reference to section 229A(a); and
            (B) "subsection (a)" shall be deemed to be a reference to subsection (a) of this section.
        (2) Temporary restraining orders.-
            (A)     In general.-For the purposes of forfeiture proceedings under this section, a temporary restraining order may be entered upon application of the United States without notice or opportunity for a hearing when an information or indictment has not yet been filed with respect to the property, if, in addition to the circumstances described in section 413(e)(2) of the Comprehensive Drug Abuse Prevention and Control Act of 1970 (21 U.S.C. 853(e)(2)), the United States demonstrates that there is probable cause to believe that the property with respect to which the order is sought would, in the event of conviction, be subject to forfeiture under this section and exigent circumstances exist that place the life or health of any person in danger.
            (B)     Warrant of seizure.-If the court enters a temporary restraining order under this paragraph, it shall also issue a warrant authorizing the seizure of such property.
            (C)     Applicable procedures.-The procedures and time limits applicable to temporary restraining orders under section 413(e)(2) and (3) of the Comprehensive Drug Abuse Prevention and Control Act of 1970 (21 U.S.C. 853(e)(2) and (3)) shall apply to temporary restraining orders under this paragraph.   
    (c) Affirmative Defense.
        -It is an affirmative defense against a forfeiture under subsection (b) that the property-
        (1) is for a purpose not prohibited under the Chemical Weapons Convention; and
        (2) is of a type and quantity that under the circumstances is consistent with that purpose.
    (d) Destruction or Other Disposition.-The Attorney General shall provide for the destruction or other appropriate disposition of any chemical weapon seized and forfeited pursuant to this section.
    (e) Assistance.
    (f) Owner Liability.
        -The owner or possessor of any property seized under this section shall be liable to the United States for any expenses incurred incident to the seizure, including any expenses relating to the handling, storage, transportation, and destruction or other disposition of the seized property
USC 18, §218. Voiding transactions in violation of chapter; recovery by the United States

    In addition to any other remedies provided by law the President or, under regulations prescribed by him, the head of any department or agency involved, may declare void and rescind any contract, loan, grant, subsidy, license, right, permit, franchise, use, authority, privilege, benefit, certificate, ruling, decision, opinion, or rate schedule awarded, granted, paid, furnished, or published, or the performance of any service or transfer or delivery of any thing to, by or for any agency of the United States or officer or employee of the United States or person acting on behalf thereof, in relation to which there has been a final conviction for any violation of this chapter, and the United States shall be entitled to recover in addition to any penalty prescribed by law or in a contract the amount expended or the thing transferred or delivered on its behalf, or the reasonable value thereof.


NOTE.     I OFFERED THE DEFAULT CLAUSE OF THE LOAN SO THAT STATE FARM CAN CANCEL THE LOAN, EXECUTED AND FILED THE SAME AS EXHIBIT 420 IN NYSCEF MATTER 153974/2020. NONE OF THE INDIVUALS FROM STATE FARM HAVE RESPONDED TO THIS EFFECT SINCE THEN, AND MOST RECENTLY, MR. DAVID MOORE ATTEMPTED TO PLACE A CO-WORKER IN HIS PLACE, MISS JANNA UNDERWOOD WHO I UNDERSTAND IS NOT A DIRECTOR OF STATE FARM, ON THE BASIS OF FILINGS AND DOCUMENTS THAT ARE AVAILABLE, PER THE FINANCIAL INDUSTRY REGULATORY AUTHORITY AND THE SECURITIES AND EXCHANGE COMMISSION UNDER CIK FILER 93715, AND CIK FILER 1516523.
USC 18, §216. Penalties and injunctions

    (a) The punishment for an offense under section 203, 204, 205, 207, 208, or 209 of this title is the following:
        (1) Whoever engages in the conduct constituting the offense shall be imprisoned for not more than one year or fined in the amount set forth in this title, or both.
        (2) Whoever willfully engages in the conduct constituting the offense shall be imprisoned for not more than five years or fined in the amount set forth in this title, or both.
    (b)     The Attorney General may bring a civil action in the appropriate United States district court against any person who engages in conduct constituting an offense under section 203, 204, 205, 207, 208, or 209 of this title and, upon proof of such conduct by a preponderance of the evidence, such person shall be subject to a civil penalty of not more than $50,000 for each violation or the amount of compensation which the person received or offered for the prohibited conduct, whichever amount is greater. The imposition of a civil penalty under this subsection does not preclude any other criminal or civil statutory, common law, or administrative remedy, which is available by law to the United States or any other person.
    (c) If the Attorney General has reason to believe that a person is engaging in conduct constituting an offense under section 203, 204, 205, 207, 208, or 209 of this title, the Attorney General may petition an appropriate United States district court for an order prohibiting that person from engaging in such conduct. The court may issue an order prohibiting that person from engaging in such conduct if the court finds that the conduct constitutes such an offense. The filing of a petition under this section does not preclude any other remedy which is available by law to the United States or any other person.


*****    *****    *****    *****    *****     *****    *****    *****

GREY AREA


HERE IN THIS GREY AREA, WITH THE PROPER RESOURCES TO FURTHER THE CHARGES THAT WERE FILED WITH THE NEW YORK SUPREME COURT, CIVIL PART AND THE SECURITIES AND EXCHANGE COMMISSION ARE PROBABLE FOR CAUSE.

§25. Use of minors in crimes of violence
    (a) Definitions.-In this section, the following definitions shall apply:
        (1) Crime of violence.-The term "crime of violence" has the meaning set forth in section 16.
        (2) Minor.-The term "minor" means a person who has not reached 18 years of age.
        (3) Uses.-The term "uses" means employs, hires, persuades, induces, entices, or coerces.

    (b) Penalties.
    -Any person who is 18 years of age or older, who intentionally uses a minor to commit a crime of violence for which such person may be prosecuted in a court of the United States, or to assist in avoiding detection or apprehension for such an offense, shall-
        (1) for the first conviction, be subject to twice the maximum term of imprisonment and twice the maximum fine that would otherwise be authorized for the offense; and
        (2) for each subsequent conviction, be subject to 3 times the maximum term of imprisonment and 3 times the maximum fine that would otherwise be authorized for the offense.

§151. Definition

    As used in this chapter, the term "debtor" means a debtor concerning whom a petition has been filed under title 11.

    §152. Concealment of assets; false oaths and claims; bribery
    A person who-
        (1) knowingly and fraudulently conceals from a custodian, trustee, marshal, or other officer of the court charged with the control or custody of property, or, in connection with a case under title 11, from creditors or the United States Trustee, any property belonging to the estate of a debtor;
        (2) knowingly and fraudulently makes a false oath or account in or in relation to any case under title 11;
        (3) knowingly and fraudulently makes a false declaration, certificate, verification, or statement under penalty of perjury as permitted under section 1746 of title 28, in or in relation to any case under title 11;
        (4) knowingly and fraudulently presents any false claim for proof against the estate of a debtor, or uses any such claim in any case under title 11, in a personal capacity or as or through an agent, proxy, or attorney;
        (5) knowingly and fraudulently receives any material amount of property from a debtor after the filing of a case under title 11, with intent to defeat the provisions of title 11;
        (6) knowingly and fraudulently gives, offers, receives, or attempts to obtain any money or property, remuneration, compensation, reward, advantage, or promise thereof for acting or forbearing to act in any case under title 11;
        (7) in a personal capacity or as an agent or officer of any person or corporation, in contemplation of a case under title 11 by or against the person or any other person or corporation, or with intent to defeat the provisions of title 11, knowingly and fraudulently transfers or conceals any of his property or the property of such other person or corporation;
        (8) after the filing of a case under title 11 or in contemplation thereof, knowingly and fraudulently conceals, destroys, mutilates, falsifies, or makes a false entry in any recorded information (including books, documents, records, and papers) relating to the property or financial affairs of a debtor; or
        (9) after the filing of a case under title 11, knowingly and fraudulently withholds from a custodian, trustee, marshal, or other officer of the court or a United States Trustee entitled to its possession, any recorded information (including books, documents, records, and papers) relating to the property or financial affairs of a debtor,
    -shall be fined under this title, imprisoned not more than 5 years, or both.

§246. Deprivation of relief benefits

    Whoever directly or indirectly deprives, attempts to deprive, or threatens to deprive any person of any employment, position, work, compensation, or other benefit provided for or made possible in whole or in part by any Act of Congress appropriating funds for work relief or relief purposes, on account of political affiliation, race, color, sex, religion, or national origin, shall be fined under this title, or imprisoned not more than one year, or both.
§220. Illegal remunerations for referrals to recovery homes, clinical treatment facilities, and laboratories

(a) Offense.-Except as provided in subsection (b), whoever, with respect to services covered by a health care benefit program, in or affecting interstate or foreign commerce, knowingly and willfully-
    (1) solicits or receives any remuneration (including any kickback, bribe, or rebate) directly or indirectly, overtly or covertly, in cash or in kind, in return for referring a patient or patronage to a recovery home, clinical treatment facility, or laboratory; or
    (2) pays or offers any remuneration (including any kickback, bribe, or rebate) directly or indirectly, overtly or covertly, in cash or in kind-
        (A) to induce a referral of an individual to a recovery home, clinical treatment facility, or laboratory; or
        (B) in exchange for an individual using the services of that recovery home, clinical treatment facility, or laboratory,
    -shall be fined not more than $200,000, imprisoned not more than 10 years, or both, for each occurrence.

(b) Applicability.-Subsection (a) shall not apply to-
    (1) a discount or other reduction in price obtained by a provider of services or other entity under a health care benefit program if the reduction in price is properly disclosed and appropriately reflected in the costs claimed or charges made by the provider or entity;
    (2) a payment made by an employer to an employee or independent contractor (who has a bona fide employment or contractual relationship with such employer) for employment, if the employee's payment is not determined by or does not vary by-
        (A) the number of individuals referred to a particular recovery home, clinical treatment facility, or laboratory;
        (B) the number of tests or procedures performed; or
        (C) the amount billed to or received from, in part or in whole, the health care benefit program from the individuals referred to a particular recovery home, clinical treatment facility, or laboratory;
    (3) a discount in the price of an applicable drug of a manufacturer that is furnished to an applicable beneficiary under the Medicare coverage gap discount program under section 1860D–14A(g) of the Social Security Act (42 U.S.C. 1395w–114a(g));
    (4) a payment made by a principal to an agent as compensation for the services of the agent under a personal services and management contract that meets the requirements of section 1001.952(d) of title 42, Code of Federal Regulations, as in effect on the date of enactment of this section;
    (5) a waiver or discount (as defined in section 1001.952(h)(5) of title 42, Code of Federal Regulations, or any successor regulation) of any coinsurance or copayment by a health care benefit program if-
        (A) the waiver or discount is not routinely provided; and
        (B) the waiver or discount is provided in good faith;
    (6) a remuneration described in section 1128B(b)(3)(I) of the Social Security Act (42 U.S.C. 1320a–7b(b)(3)(I));
    (7) a remuneration made pursuant to an alternative payment model (as defined in section 1833(z)(3)(C) of the Social Security Act) or pursuant to a payment arrangement used by a State, health insurance issuer, or group health plan if the Secretary of Health and Human Services has determined that such arrangement is necessary for care coordination or value-based care; or
    (8) any other payment, remuneration, discount, or reduction as determined by the Attorney General, in consultation with the Secretary of Health and Human Services, by regulation.
    
    (c) Regulations.
    -The Attorney General, in consultation with the Secretary of Health and Human Services, may promulgate regulations to clarify the exceptions described in subsection (b).
    (d) Preemption.-
        (1) Federal law.-This section shall not apply to conduct that is prohibited under section 1128B of the Social Security Act (42 U.S.C. 1320a–7b).
        (2) State law.-Nothing in this section shall be construed to occupy the field in which any provisions of this section operate to the exclusion of State laws on the same subject matter.

    (e) Definitions.-In this section-
        (1) the terms "applicable beneficiary" and "applicable drug" have the meanings given those terms in section 1860D–14A(g) of the Social Security Act (42 U.S.C. 1395w–114a(g));
        (2) the term "clinical treatment facility" means a medical setting, other than a hospital, that provides detoxification, risk reduction, outpatient treatment and care, residential treatment, or rehabilitation for substance use, pursuant to licensure or certification under State law;
        (3) the term "health care benefit program" has the meaning given the term in section 24(b);
        (4) the term "laboratory" has the meaning given the term in section 353 of the Public Health Service Act (42 U.S.C. 263a); and
        (5) the term "recovery home" means a shared living environment that is, or purports to be, free from alcohol and illicit drug use and centered on peer support and connection to services that promote sustained recovery from substance use disorders.
USC 18, §214. Offer for procurement of Federal Reserve bank loan and discount of commercial paper

    Whoever stipulates for or gives or receives, or consents or agrees to give or receive, any fee, commission, bonus, or thing of value for procuring or endeavoring to procure from any Federal Reserve bank any advance, loan, or extension of credit or discount or purchase of any obligation or commitment with respect thereto, either directly from such Federal Reserve bank or indirectly through any financing institution, unless such fee, commission, bonus, or thing of value and all material facts with respect to the arrangement or understanding therefor shall be disclosed in writing in the application or request for such advance, loan, extension of credit, discount, purchase, or commitment, shall be fined under this title or imprisoned not more than one year, or both.


*****    *****    *****    *****    *****     *****    *****    *****


*****    *****    *****    *****    *****     *****    *****    *****


**** YOU'LL HAVE TO ASK THE FBI/NSA TO SEE IF THEY WILL VERIFY THIS *****

*****    USC 18, §208. Acts affecting a personal financial interest
    (a) Except as permitted by subsection (b) hereof, whoever, being an officer or employee of the executive branch of the United States Government, or of any independent agency of the United States, a Federal Reserve bank director, officer, or employee, or an officer or employee of the District of Columbia, including a special Government employee, participates personally and substantially as a Government officer or employee, through decision, approval, disapproval, recommendation, the rendering of advice, investigation, or otherwise, in a judicial or other proceeding, application, request for a ruling or other determination, contract, claim, controversy, charge, accusation, arrest, or other particular matter in which, to his knowledge, he, his spouse, minor child, general partner, organization in which he is serving as officer, director, trustee, general partner or employee, or any person or organization with whom he is negotiating or has any arrangement concerning prospective employment, has a financial interest-
    -Shall be subject to the penalties set forth in section 216 of this title.
    (b) Subsection (a) shall not apply-
        (1) if the officer or employee first advises the Government official responsible for appointment to his or her position of the nature and circumstances of the judicial or other proceeding, application, request for a ruling or other determination, contract, claim, controversy, charge, accusation, arrest, or other particular matter and makes full disclosure of the financial interest and receives in advance a written determination made by such official that the interest is not so substantial as to be deemed likely to affect the integrity of the services which the Government may expect from such officer or employee;
        (2) if, by regulation issued by the Director of the Office of Government Ethics, applicable to all or a portion of all officers and employees covered by this section, and published in the Federal Register, the financial interest has been exempted from the requirements of subsection (a) as being too remote or too inconsequential to affect the integrity of the services of the Government officers or employees to which such regulation applies;
        (3) in the case of a special Government employee serving on an advisory committee within the meaning of the Federal Advisory Committee Act (including an individual being considered for an appointment to such a position), the official responsible for the employee's appointment, after review of the financial disclosure report filed by the individual pursuant to the Ethics in Government Act of 1978, certifies in writing that the need for the individual's services outweighs the potential for a conflict of interest created by the financial interest involved; or
        (4) if the financial interest that would be affected by the particular matter involved is that resulting solely from the interest of the officer or employee, or his or her spouse or minor child, in birthrights-
            (A) in an Indian tribe, band, nation, or other organized group or community, including any Alaska Native village corporation as defined in or established pursuant to the Alaska Native Claims Settlement Act, which is recognized as eligible for the special programs and services provided by the United States to Indians because of their status as Indians,
            (B) in an Indian allotment the title to which is held in trust by the United States or which is inalienable by the allottee without the consent of the United States, or
            (C) in an Indian claims fund held in trust or administered by the United States,
        -if the particular matter does not involve the Indian allotment or claims fund or the Indian tribe, band, nation, organized group or community, or Alaska Native village corporation as a specific party or parties.
    (c)(1) For the purpose of paragraph (1) of subsection (b), in the case of class A and B directors of Federal Reserve banks, the Board of Governors of the Federal Reserve System shall be deemed to be the Government official responsible for appointment.
    (2) The potential availability of an exemption under any particular paragraph of subsection (b) does not preclude an exemption being granted pursuant to another paragraph of subsection (b).
    (d)(1) Upon request, a copy of any determination granting an exemption under subsection (b)(1) or (b)(3) shall be made available to the public by the agency granting the exemption pursuant to the procedures set forth in section 105 of the Ethics in Government Act of 1978. In making such determination available, the agency may withhold from disclosure any information contained in the determination that would be exempt from disclosure under section 552 of title 5. For purposes of determinations under subsection (b)(3), the information describing each financial interest shall be no more extensive than that required of the individual in his or her financial disclosure report under the Ethics in Government Act of 1978.
    (2) The Office of Government Ethics, after consultation with the Attorney General, shall issue uniform regulations for the issuance of waivers and exemptions under subsection (b) which shall-
        (A) list and describe exemptions; and
        (B) provide guidance with respect to the types of interests that are not so substantial as to be deemed likely to affect the integrity of the services the Government may expect from the employee.

*****    §118. Interference with certain protective functions
    Any person who knowingly and willfully obstructs, resists, or interferes with a Federal law enforcement agent engaged, within the United States or the special maritime territorial jurisdiction of the United States, in the performance of the protective functions authorized under section 37 of the State Department Basic Authorities Act of 1956 (22 U.S.C. 2709) or section 103 of the Diplomatic Security Act (22 U.S.C. 4802) shall be fined under this title, imprisoned not more than 1 year, or both.

*****    §119. Protection of individuals performing certain official duties
    (a) In General.
        -Whoever knowingly makes restricted personal information about a covered person, or a member of the immediate family of that covered person, publicly available-
            (1) with the intent to threaten, intimidate, or incite the commission of a crime of violence against that covered person, or a member of the immediate family of that covered person; or
            (2) with the intent and knowledge that the restricted personal information will be used to threaten, intimidate, or facilitate the commission of a crime of violence against that covered person, or a member of the immediate family of that covered person,
        -shall be fined under this title, imprisoned not more than 5 years, or both.
        (b) Definitions.-In this section-
            (1) the term "restricted personal information" means, with respect to an individual, the Social Security number, the home address, home phone number, mobile phone number, personal email, or home fax number of, and identifiable to, that individual;
            (2) the term "covered person" means-
                (A) an individual designated in section 1114;
                (B) a grand or petit juror, witness, or other officer in or of, any court of the United States, or an officer who may be, or was, serving at any examination or other proceeding before any United States magistrate judge or other committing magistrate;
                (C) an informant or witness in a Federal criminal investigation or prosecution; or
                (D) a State or local officer or employee whose restricted personal information is made publicly available because of the participation in, or assistance provided to, a Federal criminal investigation by that officer or employee;
            (3) the term "crime of violence" has the meaning given the term in section 16; and
            (4) the term "immediate family" has the meaning given the term in section 115(c)(2).


*****    §115. Influencing, impeding, or retaliating against a Federal official by threatening or injuring a family member
    (a)(1) Whoever-
        (A) assaults, kidnaps, or murders, or attempts or conspires to kidnap or murder, or threatens to assault, kidnap or murder a member of the immediate family of a United States official, a United States judge, a Federal law enforcement officer, or an official whose killing would be a crime under section 1114 of this title; or
        (B) threatens to assault, kidnap, or murder, a United States official, a United States judge, a Federal law enforcement officer, or an official whose killing would be a crime under such section,
    -with intent to impede, intimidate, or interfere with such official, judge, or law enforcement officer while engaged in the performance of official duties, or with intent to retaliate against such official, judge, or law enforcement officer on account of the performance of official duties, shall be punished as provided in subsection (b).

    (2) Whoever assaults, kidnaps, or murders, or attempts or conspires to kidnap or murder, or threatens to assault, kidnap, or murder, any person who formerly served as a person designated in paragraph (1), or a member of the immediate family of any person who formerly served as a person designated in paragraph (1), with intent to retaliate against such person on account of the performance of official duties during the term of service of such person, shall be punished as provided in subsection (b).

    §(b)
    (1)     The punishment for an assault in violation of this section is-
            (A) a fine under this title; and
            (B)
                (i)     if the assault consists of a simple assault, a term of imprisonment for not more than 1 year;
                (ii)     if the assault involved physical contact with the victim of that assault or the intent to commit another felony, a term of imprisonment for not more than 10 years;
                (iii)     if the assault resulted in bodily injury, a term of imprisonment for not more than 20 years; or
                (iv)     if the assault resulted in serious bodily injury (as that term is defined in section 1365 of this title, and including any conduct that, if the conduct occurred in the special maritime and territorial jurisdiction of the United States, would violate section 2241 or 2242 of this title) or a dangerous weapon was used during and in relation to the offense, a term of imprisonment for not more than 30 years.
    (2)        A kidnapping, attempted kidnapping, or conspiracy to kidnap in violation of this section shall be punished as provided in section 1201 of this title for the kidnapping or attempted kidnapping of, or a conspiracy to kidnap, a person described in section 1201(a)(5) of this title.
        (3) A murder, attempted murder, or conspiracy to murder in violation of this section shall be punished as provided in sections 1111, 1113, and 1117 of this title.
        (4) A threat made in violation of this section shall be punished by a fine under this title or imprisonment for a term of not more than 10 years, or both, except that imprisonment for a threatened assault shall not exceed 6 years.
        (c) As used in this section, the term-
            (1) "Federal law enforcement officer" means any officer, agent, or employee of the United States authorized by law or by a Government agency to engage in or supervise the prevention, detection, investigation, or prosecution of any violation of Federal criminal law;
            (2) "immediate family member" of an individual means-
                (A) his spouse, parent, brother or sister, child or person to whom he stands in loco parentis; or
                (B) any other person living in his household and related to him by blood or marriage;
            (3) "United States judge" means any judicial officer of the United States, and includes a justice of the Supreme Court and a United States magistrate judge; and
            (4) "United States official" means the President, President-elect, Vice President, Vice President-elect, a Member of Congress, a member-elect of Congress, a member of the executive branch who is the head of a department listed in 5 U.S.C. 101, or the Director of the Central Intelligence Agency.
        (d) This section shall not interfere with the investigative authority of the United States Secret Service, as provided under sections 3056, 871, and 879 of this title.
        (e) There is extraterritorial jurisdiction over the conduct prohibited by this section.
§116. Female genital mutilation

***** YOU'LL HAVE TO ASK THE FBI/NSA TO SEE IF THEY WILL VERIFY THIS *****



 

– I HOPE YOU UNDERSTAND WHERE THIS ALSO PRESENTS A CONFLICT, AS HE BELIEVES THIS TO BE TRUE.
                                                    1_u.s._v._brian_benjamin_indictment (1).pdf

    NYSCEF MATTER 153974/2020
    - SHARED ADDRESS WITH THE WILSON ELSER LAW FIRM, BELOW.

    Filing User Shari Laskowitz | slaskowitz@ingramllp.com | 2129079600

    150 East 42nd Street 19th Floor, New York, NY 10017 Filed: 07/21/2020

-------- Forwarded Message --------
Subject: 	Voicemail from Mr. PAUL regan
Date: 	Sun, 26 Jun 2022 16:51:47 -0400
From: 	BO DINCER <bondstrt007@gmail.com>
To: 	customerservice@nypost.com, espnfrontrow@espn.com, teschmann@mskyline.com, Joseph Giamboi, ESQ <joseph.giamboi@brooklaw.edu>, LZUCKER@mskyline.com, sgo2107@columbia.edu, letters@nypost.com, Laskowitz, Shari <slaskowitz@ingramllp.com>, dallas-reserve-mgmt@dal.frb.org, 23pctdvo@nypd.com, 23pctyco@nypd.org, 1pctdvo@nypd.org, 1pctyco@nypd.org, praghuram2@bloomberg.net, PRIYA.RAGHURAM@MORGANSTANLEY.COM <PRIYA.RAGHURAM@morganstanley.com>, JAMES GORMAN [MORGAN STANLEY] <james.gorman@morganstanley.com>, Dow Jones <wsjprosupport@dowjones.com>, paul.jones@tudor.com, Paul Regan <LEGAL@mskyline.com>, LEGALASST@mskyline.com, MSKYLINE <anne@thehighlandpartners.com>, cweiss@ingramllp.com, info@statefarm.com, State Farm <mutualfunds@statefarm.com>, David Moore <david.moore.ct95@statefarm.com>, hillary.davis@latimes.com, Scott Holcomb <scott@holcombward.com>, SOHO HOUSE <membership@sohohouse.com>
CC: 	KATHY HOCHUL <governor.hochul@exec.ny.gov>, BBO 121 <ms60710444266@yahoo.com>, MIT Sloan Executive Education <executive_education@mailsvc.sloan.mit.edu>, Marc Lavigne <tessier3@stanford.edu>, NYSCEF PROCESS HD <oca_hd_processor@nycourts.gov>, The New York Times <help@nytimes.com>, administration@mskyline.com, MANHATTAN SKYLINE, LLC. <ADMINISTRATOR@mskyline.com>


I am terrified, where is he ? Touching himself or making videos with my Glamour shots.

Thats actually a compound, in the scope of avoidance to prosecution. 

Truly a delusional group, never met them.

---
## [WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER](https://github.com/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER)@[08aa928f35...](https://github.com/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/commit/08aa928f3580e2c32382dfccee3df312ca10e534)
#### Monday 2022-06-27 19:27:23 by WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER

Truly a delusional group, never met them.

101 west 55th street, new york, ny 10019
103 west 55th street, new york, ny, 10019
150 east 42nd street, new york, ny 10017

USC 18. VIOLATIONS ANNEXED IN NYSCEF 153974/2020 [ LOAN 50074 ], also filed with the Financial Industry Regulatory Authority, and the Securities and Exchange Commission - Notwithstanding the New York State Supreme Court, the New York Department of Finance, and the NYC Finance Register - as referenced below.


§21. Stolen or counterfeit nature of property for certain crimes defined
    (a) Wherever in this title it is an element of an offense that-
        (1) any property was embezzled, robbed, stolen, converted, taken, altered, counterfeited, falsely made, forged, or obliterated; and
        (2) the defendant knew that the property was of such character;
            -such element may be established by proof that the defendant, after or as a result of an official representation as to the nature of the property, believed the property to be embezzled, robbed, stolen, converted, taken, altered, counterfeited, falsely made, forged, or obliterated.
            -(b) For purposes of this section, the term "official representation" means any representation made by a Federal law enforcement officer (as defined in section 115) or by another person at the direction or with the approval of such an officer.


    §2. - Principals (a) Whoever commits an offense against the United States or aids, abets, counsels, commands, induces or procures its commission, is punishable as a principal. (b) Whoever willfully causes an act to be done which if directly performed by him or another would be an offense against the United States, is punishable as a principal.

    §3. - Accessory after the fact Whoever, knowing that an offense against the United States has been committed, receives, relieves, comforts or assists the offender in order to hinder or prevent his apprehension, trial or punishment, is an accessory after the fact. Except as otherwise expressly provided by any Act of Congress, an accessory after the fact shall be imprisoned not more than one-half the maximum term of imprisonment or (notwithstanding section 3571) fined not more than one-half the maximum fine prescribed for the punishment of the principal, or both; or if the principal is punishable by life imprisonment or death, the accessory shall be imprisoned not more than 15 years.

    §4. Misprision of felony Whoever, having knowledge of the actual commission of a felony cognizable by a court of the United States, conceals and does not as soon as possible make known the same to some judge or other person in civil or military authority under the United States, shall be fined under this title or imprisoned not more than three years, or both.
USC Title 18, §1962. Prohibited activities

(a) It shall be unlawful for any person who has received any income derived, directly or indirectly, from a pattern of racketeering activity or through collection of an unlawful debt in which such person has participated as a principal within the meaning of section 2, title 18, United States Code, to use or invest, directly or indirectly, any part of such income, or the proceeds of such income, in acquisition of any interest in, or the establishment or operation of, any enterprise which is engaged in, or the activities of which affect, interstate or foreign commerce. A purchase of securities on the open market for purposes of investment, and without the intention of controlling or participating in the control of the issuer, or of assisting another to do so, shall not be unlawful under this subsection if the securities of the issuer held by the purchaser, the members of his immediate family, and his or their accomplices in any pattern or racketeering activity or the collection of an unlawful debt after such purchase do not amount in the aggregate to one percent of the outstanding securities of any one class, and do not confer, either in law or in fact, the power to elect one or more directors of the issuer.

(b) It shall be unlawful for any person through a pattern of racketeering activity or through collection of an unlawful debt to acquire or maintain, directly or indirectly, any interest in or control of any enterprise which is engaged in, or the activities of which affect, interstate or foreign commerce.

(c) It shall be unlawful for any person employed by or associated with any enterprise engaged in, or the activities of which affect, interstate or foreign commerce, to conduct or participate, directly or indirectly, in the conduct of such enterprise's affairs through a pattern of racketeering activity or collection of unlawful debt.

(d) It shall be unlawful for any person to conspire to violate any of the provisions of subsection (a), (b), or (c) of this section.

USC Title 18, §1963. Criminal penalties

(a) Whoever violates any provision of section 1962 of this chapter shall be fined under this title or imprisoned not more than 20 years (or for life if the violation is based on a racketeering activity for which the maximum penalty includes life imprisonment), or both, and shall forfeit to the United States, irrespective of any provision of State law- (1) any interest the person has acquired or maintained in violation of section 1962; (2) any- (A) interest in; (B) security of; (C) claim against; or (D) property or contractual right of any kind affording a source of influence over; any enterprise which the person has established, operated, controlled, conducted, or participated in the conduct of, in violation of section 1962; and (3) any property constituting, or derived from, any proceeds which the person obtained, directly or indirectly, from racketeering activity or unlawful debt collection in violation of section 1962. The court, in imposing sentence on such person shall order, in addition to any other sentence imposed pursuant to this section, that the person forfeit to the United States all property described in this subsection. In lieu of a fine otherwise authorized by this section, a defendant who derives profits or other proceeds from an offense may be fined not more than twice the gross profits or other proceeds. (b) Property subject to criminal forfeiture under this section includes- (1) real property, including things growing on, affixed to, and found in land; and (2) tangible and intangible personal property, including rights, privileges, interests, claims, and securities.



USC Title 18, 18,§215. Receipt of commissions or gifts for procuring loans

    (a) Whoever-
        (1) corruptly gives, offers, or promises anything of value to any person, with intent to influence or reward an officer, director, employee, agent, or attorney of a financial institution in connection with any business or transaction of such institution; or
        (2) as an officer, director, employee, agent, or attorney of a financial institution, corruptly solicits or demands for the benefit of any person, or corruptly accepts or agrees to accept, anything of value from any person, intending to be influenced or rewarded in connection with any business or transaction of such institution;
        -shall be fined not more than $1,000,000 or three times the value of the thing given, offered, promised, solicited, demanded, accepted, or agreed to be accepted, whichever is greater, or imprisoned not more than 30 years, or both, but if the value of the thing given, offered, promised, solicited, demanded, accepted, or agreed to be accepted does not exceed $1,000, shall be fined under this title or imprisoned not more than one year, or both.
    (c) This section shall not apply to bona fide salary, wages, fees, or other compensation paid, or expenses paid or reimbursed, in the usual course of business.
    (d) Federal agencies with responsibility for regulating a financial institution shall jointly establish such guidelines as are appropriate to assist an officer, director, employee, agent, or attorney of a financial institution to comply with this section. Such agencies shall make such guidelines available to the public.

        FILED WITH THE SECURITIES AND EXCHANGE COMMISSION IN 2021,

            UNDER CIK FILER 93715, (1) STATE FARM ASSURANCES FUNDS TRUST.
            - DISCLOSE (2) STATE FARM LIFE INSURANCE COMPANY AS AN OUTSIDE BUSINESS IN THEIR FIRMS CRD FILINGS WITH FINRA, THE SAME ENTITY THAT NOTARIZED AND COUNTERSIGNED ON LOAN 50074, DUALLY BY (3) DONALD ZUCKER WAS EXECUTED ON MAY 13, 2020 - REPRESENTED BY THE ATTORNEYS ON BEHALF OF (4) SULLIVAN PROPERTIES, LP, BELOW FOR CONVENIENCE.

        THE DIRECTORS OF STATE FARM, WHO FILED WITH THE SECURITIES AND EXCHANGE COMISSION.

            BY:     (5) DAVID MOORE, (6) JOESEPH MONK, (7)PAUL J SMITH, AND UNDER (8)TERRENCE LUDWIG [AND OTHER DIRECTORS OF STATE FARM]

        THE DIRECTORS OF STATE FARM, WHO FILED WITH THE FINANCIAL INDUSTRY REGULATORY AUTHORITY ON BEHALF OF (16) STATE FARM VP MANAGEMENT CORP.

            BY: (8) TERRENCE LUDWIG

                        A TOTAL AMOUNT WAS ACCEPTED FOR A "SUCCESSFUL MERGER",

                        APPROXIMATELY $412,500 USD IN COMPENSATION WAS FILED WITH THE SEC.

USC 18, §241. Conspiracy against rights.
    - If two or more persons conspire to injure, oppress, threaten, or intimidate any person in any State, Territory, Commonwealth, Possession, or District in the free exercise or enjoyment of any right or privilege secured to him by the Constitution or laws of the United States, or because of his having so exercised the same; or
    - If two or more persons go in disguise on the highway, or on the premises of another, with intent to prevent or hinder his free exercise or enjoyment of any right or privilege so secured—


            EXHIBITS FILED AND ANNEXED IN THE DOCKETS IN NY SUPREME COURT CIVIL MATTER

                    NYSCEF 153974/2020

USC 18,§225. Continuing financial crimes enterprise
    (a) Whoever-
        (1) organizes, manages, or supervises a continuing financial crimes enterprise; and
        (2) receives $5,000,000 or more in gross receipts from such enterprise during any 24-month period
    -shall be fined not more than $10,000,000 if an individual, or $20,000,000 if an organization, and imprisoned for a term of not less than 10 years and which may be life.
    (b) For purposes of subsection (a), the term "continuing financial crimes enterprise" means a series of violations under section 215, 656, 657, 1005, 1006, 1007, 1014, 1032, or 1344 of this title, or section 1341 or 1343 affecting a financial institution, committed by at least 4 persons acting in concert.        
              [ LOAN 50074: $6,000,000 ] ANNEXED IN DOCKETS 309-315 IN NYSCEF MATTER 153974/2020

                    ANNEXED IN NY SUPREME COURT MATTER 153974/2020
                    REPRESENTATIVES OF

                    (9) SULLIVAN PROPERTIES LP, (10) SULLIVAN GP LLC, (11) MANHATTAN SKYLINE MANAGEMENT CORP.
                   

                    BY:     COUNSELORS FOR PLAINTIFFS IN NYSCEF 153974/2020 [ ANNEXED THEREIN ] THE VIOLATION OF PRIVACY, AS SUPPLEMENT...

                    (12) SHARI LASKOWITZ, (13) ASHLEY HUMPHRIES, (14) CORY WEISS, AND (15) PAUL REGAN

                        DOCKETS ANNEXED IN NYSCEF 153974/2020 AND ALSO FILED WITH THE NY DEPT OF FINANCE.

                    OBO:     (3) DONALD ZUCKER, (17) LAURIE ZUCKER, AND OTHERS WHO I AM UNFAMILIAR TO THEIR RESPECTIVE SHARES HELD AS LIMITED PARTNERS OF SULLIVAN PROPERTIES LP.

                    UNLAWFULLY (USC 18.21) PRESENTED THE IMPLIED RETURNS FOR 6 PROPERTIES WHICH WERE ALSO FILED, AND
                    >PUBLICLY AVAILABLE TO ALL REGULAR /COMPETENT PERSONS.

                    USED TO PROCURE AND OBTAIN A LOAN FOR $6,000,000.00 ( SIX MILLION US DOLLARS) AND USED THE FOLLOWING ENTITY ON THE COVER PAGE:

                    (18) THE ZUCKER ORGANIZATION LLC
USC 18, § 373 - Solicitation to commit a crime of violence

(a) Whoever, with intent that another person engage in conduct constituting a felony that has as an element the use, attempted use, or threatened use of physical force against property or against the person of another in violation of the laws of the United States, and under circumstances strongly corroborative of that intent, solicits, commands, induces, or otherwise endeavours to persuade such other person to engage in such conduct, shall be imprisoned not more than one-half the maximum term of imprisonment or (notwithstanding section 3571) fined not more than one-half of the maximum fine prescribed for the punishment of the crime solicited, or both; or if the crime solicited is punishable by life imprisonment or death, shall be imprisoned for not more than twenty years.

                (15)    <voicemail attached>

(b) It is an affirmative defence to a prosecution under this section that, under circumstances manifesting a voluntary and complete renunciation of his criminal intent, the defendant prevented the commission of the crime solicited. A renunciation is not "voluntary and complete" if it is motivated in whole or in part by a decision to postpone the commission of the crime until another time or to substitute another victim or another but similar objective. If the defendant raises the affirmative defence at trial, the defendant has the burden of proving the defence by a preponderance of the evidence.
    (c) It is not a defence to a prosecution under this section that the person solicited could not be convicted of the crime because he lacked the state of mind required for its commission, because he was incompetent or irresponsible, or because he is immune from prosecution or is not subject to prosecution.
USC 18 [ FORFEITURES ] >> RISKS HELD UNDER STATE FARM AT THE OBSTRUCTION OF THE COUNSELORS IN NYSCEF 153974/2020

§229B. Criminal forfeitures; destruction of weapons
    (a) Property Subject to Criminal Forfeiture.
    -Any person convicted under section 229A(a) shall forfeit to the United States irrespective of any provision of State law-
        (1) any property, real or personal, owned, possessed, or used by a person involved in the offense;
        (2) any property constituting, or derived from, and proceeds the person obtained, directly or indirectly, as the result of such violation; and
        (3) any of the property used in any manner or part, to commit, or to facilitate the commission of, such violation.

    The court, in imposing sentence on such person, shall order, in addition to any other sentence imposed pursuant to section 229A(a), that the person forfeit to the United States all property described in this subsection. In lieu of a fine otherwise authorized by section 229A(a), a defendant who derived profits or other proceeds from an offense may be fined not more than twice the gross profits or other proceeds.
    (b) Procedures.-
        (1) General.
        -Property subject to forfeiture under this section, any seizure and disposition thereof, and any administrative or judicial proceeding in relation thereto, shall be governed by subsections (b) through (p) of section 413 of the Comprehensive Drug Abuse Prevention and Control Act of 1970 (21 U.S.C. 853), except that any reference under those subsections to-
            (A) "this subchapter or subchapter II" shall be deemed to be a reference to section 229A(a); and
            (B) "subsection (a)" shall be deemed to be a reference to subsection (a) of this section.
        (2) Temporary restraining orders.-
            (A)     In general.-For the purposes of forfeiture proceedings under this section, a temporary restraining order may be entered upon application of the United States without notice or opportunity for a hearing when an information or indictment has not yet been filed with respect to the property, if, in addition to the circumstances described in section 413(e)(2) of the Comprehensive Drug Abuse Prevention and Control Act of 1970 (21 U.S.C. 853(e)(2)), the United States demonstrates that there is probable cause to believe that the property with respect to which the order is sought would, in the event of conviction, be subject to forfeiture under this section and exigent circumstances exist that place the life or health of any person in danger.
            (B)     Warrant of seizure.-If the court enters a temporary restraining order under this paragraph, it shall also issue a warrant authorizing the seizure of such property.
            (C)     Applicable procedures.-The procedures and time limits applicable to temporary restraining orders under section 413(e)(2) and (3) of the Comprehensive Drug Abuse Prevention and Control Act of 1970 (21 U.S.C. 853(e)(2) and (3)) shall apply to temporary restraining orders under this paragraph.   
    (c) Affirmative Defense.
        -It is an affirmative defense against a forfeiture under subsection (b) that the property-
        (1) is for a purpose not prohibited under the Chemical Weapons Convention; and
        (2) is of a type and quantity that under the circumstances is consistent with that purpose.
    (d) Destruction or Other Disposition.-The Attorney General shall provide for the destruction or other appropriate disposition of any chemical weapon seized and forfeited pursuant to this section.
    (e) Assistance.
    (f) Owner Liability.
        -The owner or possessor of any property seized under this section shall be liable to the United States for any expenses incurred incident to the seizure, including any expenses relating to the handling, storage, transportation, and destruction or other disposition of the seized property
USC 18, §218. Voiding transactions in violation of chapter; recovery by the United States

    In addition to any other remedies provided by law the President or, under regulations prescribed by him, the head of any department or agency involved, may declare void and rescind any contract, loan, grant, subsidy, license, right, permit, franchise, use, authority, privilege, benefit, certificate, ruling, decision, opinion, or rate schedule awarded, granted, paid, furnished, or published, or the performance of any service or transfer or delivery of any thing to, by or for any agency of the United States or officer or employee of the United States or person acting on behalf thereof, in relation to which there has been a final conviction for any violation of this chapter, and the United States shall be entitled to recover in addition to any penalty prescribed by law or in a contract the amount expended or the thing transferred or delivered on its behalf, or the reasonable value thereof.


NOTE.     I OFFERED THE DEFAULT CLAUSE OF THE LOAN SO THAT STATE FARM CAN CANCEL THE LOAN, EXECUTED AND FILED THE SAME AS EXHIBIT 420 IN NYSCEF MATTER 153974/2020. NONE OF THE INDIVUALS FROM STATE FARM HAVE RESPONDED TO THIS EFFECT SINCE THEN, AND MOST RECENTLY, MR. DAVID MOORE ATTEMPTED TO PLACE A CO-WORKER IN HIS PLACE, MISS JANNA UNDERWOOD WHO I UNDERSTAND IS NOT A DIRECTOR OF STATE FARM, ON THE BASIS OF FILINGS AND DOCUMENTS THAT ARE AVAILABLE, PER THE FINANCIAL INDUSTRY REGULATORY AUTHORITY AND THE SECURITIES AND EXCHANGE COMMISSION UNDER CIK FILER 93715, AND CIK FILER 1516523.
USC 18, §216. Penalties and injunctions

    (a) The punishment for an offense under section 203, 204, 205, 207, 208, or 209 of this title is the following:
        (1) Whoever engages in the conduct constituting the offense shall be imprisoned for not more than one year or fined in the amount set forth in this title, or both.
        (2) Whoever willfully engages in the conduct constituting the offense shall be imprisoned for not more than five years or fined in the amount set forth in this title, or both.
    (b)     The Attorney General may bring a civil action in the appropriate United States district court against any person who engages in conduct constituting an offense under section 203, 204, 205, 207, 208, or 209 of this title and, upon proof of such conduct by a preponderance of the evidence, such person shall be subject to a civil penalty of not more than $50,000 for each violation or the amount of compensation which the person received or offered for the prohibited conduct, whichever amount is greater. The imposition of a civil penalty under this subsection does not preclude any other criminal or civil statutory, common law, or administrative remedy, which is available by law to the United States or any other person.
    (c) If the Attorney General has reason to believe that a person is engaging in conduct constituting an offense under section 203, 204, 205, 207, 208, or 209 of this title, the Attorney General may petition an appropriate United States district court for an order prohibiting that person from engaging in such conduct. The court may issue an order prohibiting that person from engaging in such conduct if the court finds that the conduct constitutes such an offense. The filing of a petition under this section does not preclude any other remedy which is available by law to the United States or any other person.


*****    *****    *****    *****    *****     *****    *****    *****

GREY AREA


HERE IN THIS GREY AREA, WITH THE PROPER RESOURCES TO FURTHER THE CHARGES THAT WERE FILED WITH THE NEW YORK SUPREME COURT, CIVIL PART AND THE SECURITIES AND EXCHANGE COMMISSION ARE PROBABLE FOR CAUSE.

§25. Use of minors in crimes of violence
    (a) Definitions.-In this section, the following definitions shall apply:
        (1) Crime of violence.-The term "crime of violence" has the meaning set forth in section 16.
        (2) Minor.-The term "minor" means a person who has not reached 18 years of age.
        (3) Uses.-The term "uses" means employs, hires, persuades, induces, entices, or coerces.

    (b) Penalties.
    -Any person who is 18 years of age or older, who intentionally uses a minor to commit a crime of violence for which such person may be prosecuted in a court of the United States, or to assist in avoiding detection or apprehension for such an offense, shall-
        (1) for the first conviction, be subject to twice the maximum term of imprisonment and twice the maximum fine that would otherwise be authorized for the offense; and
        (2) for each subsequent conviction, be subject to 3 times the maximum term of imprisonment and 3 times the maximum fine that would otherwise be authorized for the offense.

§151. Definition

    As used in this chapter, the term "debtor" means a debtor concerning whom a petition has been filed under title 11.

    §152. Concealment of assets; false oaths and claims; bribery
    A person who-
        (1) knowingly and fraudulently conceals from a custodian, trustee, marshal, or other officer of the court charged with the control or custody of property, or, in connection with a case under title 11, from creditors or the United States Trustee, any property belonging to the estate of a debtor;
        (2) knowingly and fraudulently makes a false oath or account in or in relation to any case under title 11;
        (3) knowingly and fraudulently makes a false declaration, certificate, verification, or statement under penalty of perjury as permitted under section 1746 of title 28, in or in relation to any case under title 11;
        (4) knowingly and fraudulently presents any false claim for proof against the estate of a debtor, or uses any such claim in any case under title 11, in a personal capacity or as or through an agent, proxy, or attorney;
        (5) knowingly and fraudulently receives any material amount of property from a debtor after the filing of a case under title 11, with intent to defeat the provisions of title 11;
        (6) knowingly and fraudulently gives, offers, receives, or attempts to obtain any money or property, remuneration, compensation, reward, advantage, or promise thereof for acting or forbearing to act in any case under title 11;
        (7) in a personal capacity or as an agent or officer of any person or corporation, in contemplation of a case under title 11 by or against the person or any other person or corporation, or with intent to defeat the provisions of title 11, knowingly and fraudulently transfers or conceals any of his property or the property of such other person or corporation;
        (8) after the filing of a case under title 11 or in contemplation thereof, knowingly and fraudulently conceals, destroys, mutilates, falsifies, or makes a false entry in any recorded information (including books, documents, records, and papers) relating to the property or financial affairs of a debtor; or
        (9) after the filing of a case under title 11, knowingly and fraudulently withholds from a custodian, trustee, marshal, or other officer of the court or a United States Trustee entitled to its possession, any recorded information (including books, documents, records, and papers) relating to the property or financial affairs of a debtor,
    -shall be fined under this title, imprisoned not more than 5 years, or both.

§246. Deprivation of relief benefits

    Whoever directly or indirectly deprives, attempts to deprive, or threatens to deprive any person of any employment, position, work, compensation, or other benefit provided for or made possible in whole or in part by any Act of Congress appropriating funds for work relief or relief purposes, on account of political affiliation, race, color, sex, religion, or national origin, shall be fined under this title, or imprisoned not more than one year, or both.
§220. Illegal remunerations for referrals to recovery homes, clinical treatment facilities, and laboratories

(a) Offense.-Except as provided in subsection (b), whoever, with respect to services covered by a health care benefit program, in or affecting interstate or foreign commerce, knowingly and willfully-
    (1) solicits or receives any remuneration (including any kickback, bribe, or rebate) directly or indirectly, overtly or covertly, in cash or in kind, in return for referring a patient or patronage to a recovery home, clinical treatment facility, or laboratory; or
    (2) pays or offers any remuneration (including any kickback, bribe, or rebate) directly or indirectly, overtly or covertly, in cash or in kind-
        (A) to induce a referral of an individual to a recovery home, clinical treatment facility, or laboratory; or
        (B) in exchange for an individual using the services of that recovery home, clinical treatment facility, or laboratory,
    -shall be fined not more than $200,000, imprisoned not more than 10 years, or both, for each occurrence.

(b) Applicability.-Subsection (a) shall not apply to-
    (1) a discount or other reduction in price obtained by a provider of services or other entity under a health care benefit program if the reduction in price is properly disclosed and appropriately reflected in the costs claimed or charges made by the provider or entity;
    (2) a payment made by an employer to an employee or independent contractor (who has a bona fide employment or contractual relationship with such employer) for employment, if the employee's payment is not determined by or does not vary by-
        (A) the number of individuals referred to a particular recovery home, clinical treatment facility, or laboratory;
        (B) the number of tests or procedures performed; or
        (C) the amount billed to or received from, in part or in whole, the health care benefit program from the individuals referred to a particular recovery home, clinical treatment facility, or laboratory;
    (3) a discount in the price of an applicable drug of a manufacturer that is furnished to an applicable beneficiary under the Medicare coverage gap discount program under section 1860D–14A(g) of the Social Security Act (42 U.S.C. 1395w–114a(g));
    (4) a payment made by a principal to an agent as compensation for the services of the agent under a personal services and management contract that meets the requirements of section 1001.952(d) of title 42, Code of Federal Regulations, as in effect on the date of enactment of this section;
    (5) a waiver or discount (as defined in section 1001.952(h)(5) of title 42, Code of Federal Regulations, or any successor regulation) of any coinsurance or copayment by a health care benefit program if-
        (A) the waiver or discount is not routinely provided; and
        (B) the waiver or discount is provided in good faith;
    (6) a remuneration described in section 1128B(b)(3)(I) of the Social Security Act (42 U.S.C. 1320a–7b(b)(3)(I));
    (7) a remuneration made pursuant to an alternative payment model (as defined in section 1833(z)(3)(C) of the Social Security Act) or pursuant to a payment arrangement used by a State, health insurance issuer, or group health plan if the Secretary of Health and Human Services has determined that such arrangement is necessary for care coordination or value-based care; or
    (8) any other payment, remuneration, discount, or reduction as determined by the Attorney General, in consultation with the Secretary of Health and Human Services, by regulation.
    
    (c) Regulations.
    -The Attorney General, in consultation with the Secretary of Health and Human Services, may promulgate regulations to clarify the exceptions described in subsection (b).
    (d) Preemption.-
        (1) Federal law.-This section shall not apply to conduct that is prohibited under section 1128B of the Social Security Act (42 U.S.C. 1320a–7b).
        (2) State law.-Nothing in this section shall be construed to occupy the field in which any provisions of this section operate to the exclusion of State laws on the same subject matter.

    (e) Definitions.-In this section-
        (1) the terms "applicable beneficiary" and "applicable drug" have the meanings given those terms in section 1860D–14A(g) of the Social Security Act (42 U.S.C. 1395w–114a(g));
        (2) the term "clinical treatment facility" means a medical setting, other than a hospital, that provides detoxification, risk reduction, outpatient treatment and care, residential treatment, or rehabilitation for substance use, pursuant to licensure or certification under State law;
        (3) the term "health care benefit program" has the meaning given the term in section 24(b);
        (4) the term "laboratory" has the meaning given the term in section 353 of the Public Health Service Act (42 U.S.C. 263a); and
        (5) the term "recovery home" means a shared living environment that is, or purports to be, free from alcohol and illicit drug use and centered on peer support and connection to services that promote sustained recovery from substance use disorders.
USC 18, §214. Offer for procurement of Federal Reserve bank loan and discount of commercial paper

    Whoever stipulates for or gives or receives, or consents or agrees to give or receive, any fee, commission, bonus, or thing of value for procuring or endeavoring to procure from any Federal Reserve bank any advance, loan, or extension of credit or discount or purchase of any obligation or commitment with respect thereto, either directly from such Federal Reserve bank or indirectly through any financing institution, unless such fee, commission, bonus, or thing of value and all material facts with respect to the arrangement or understanding therefor shall be disclosed in writing in the application or request for such advance, loan, extension of credit, discount, purchase, or commitment, shall be fined under this title or imprisoned not more than one year, or both.

GREY AREA

*****    *****    *****    *****    *****     *****    *****    *****






*****


**** YOU'LL HAVE TO ASK THE FBI/NSA TO SEE IF THEY WILL VERIFY THIS *****

*****    USC 18, §208. Acts affecting a personal financial interest
    (a) Except as permitted by subsection (b) hereof, whoever, being an officer or employee of the executive branch of the United States Government, or of any independent agency of the United States, a Federal Reserve bank director, officer, or employee, or an officer or employee of the District of Columbia, including a special Government employee, participates personally and substantially as a Government officer or employee, through decision, approval, disapproval, recommendation, the rendering of advice, investigation, or otherwise, in a judicial or other proceeding, application, request for a ruling or other determination, contract, claim, controversy, charge, accusation, arrest, or other particular matter in which, to his knowledge, he, his spouse, minor child, general partner, organization in which he is serving as officer, director, trustee, general partner or employee, or any person or organization with whom he is negotiating or has any arrangement concerning prospective employment, has a financial interest-
    -Shall be subject to the penalties set forth in section 216 of this title.
    (b) Subsection (a) shall not apply-
        (1) if the officer or employee first advises the Government official responsible for appointment to his or her position of the nature and circumstances of the judicial or other proceeding, application, request for a ruling or other determination, contract, claim, controversy, charge, accusation, arrest, or other particular matter and makes full disclosure of the financial interest and receives in advance a written determination made by such official that the interest is not so substantial as to be deemed likely to affect the integrity of the services which the Government may expect from such officer or employee;
        (2) if, by regulation issued by the Director of the Office of Government Ethics, applicable to all or a portion of all officers and employees covered by this section, and published in the Federal Register, the financial interest has been exempted from the requirements of subsection (a) as being too remote or too inconsequential to affect the integrity of the services of the Government officers or employees to which such regulation applies;
        (3) in the case of a special Government employee serving on an advisory committee within the meaning of the Federal Advisory Committee Act (including an individual being considered for an appointment to such a position), the official responsible for the employee's appointment, after review of the financial disclosure report filed by the individual pursuant to the Ethics in Government Act of 1978, certifies in writing that the need for the individual's services outweighs the potential for a conflict of interest created by the financial interest involved; or
        (4) if the financial interest that would be affected by the particular matter involved is that resulting solely from the interest of the officer or employee, or his or her spouse or minor child, in birthrights-
            (A) in an Indian tribe, band, nation, or other organized group or community, including any Alaska Native village corporation as defined in or established pursuant to the Alaska Native Claims Settlement Act, which is recognized as eligible for the special programs and services provided by the United States to Indians because of their status as Indians,
            (B) in an Indian allotment the title to which is held in trust by the United States or which is inalienable by the allottee without the consent of the United States, or
            (C) in an Indian claims fund held in trust or administered by the United States,
        -if the particular matter does not involve the Indian allotment or claims fund or the Indian tribe, band, nation, organized group or community, or Alaska Native village corporation as a specific party or parties.
    (c)(1) For the purpose of paragraph (1) of subsection (b), in the case of class A and B directors of Federal Reserve banks, the Board of Governors of the Federal Reserve System shall be deemed to be the Government official responsible for appointment.
    (2) The potential availability of an exemption under any particular paragraph of subsection (b) does not preclude an exemption being granted pursuant to another paragraph of subsection (b).
    (d)(1) Upon request, a copy of any determination granting an exemption under subsection (b)(1) or (b)(3) shall be made available to the public by the agency granting the exemption pursuant to the procedures set forth in section 105 of the Ethics in Government Act of 1978. In making such determination available, the agency may withhold from disclosure any information contained in the determination that would be exempt from disclosure under section 552 of title 5. For purposes of determinations under subsection (b)(3), the information describing each financial interest shall be no more extensive than that required of the individual in his or her financial disclosure report under the Ethics in Government Act of 1978.
    (2) The Office of Government Ethics, after consultation with the Attorney General, shall issue uniform regulations for the issuance of waivers and exemptions under subsection (b) which shall-
        (A) list and describe exemptions; and
        (B) provide guidance with respect to the types of interests that are not so substantial as to be deemed likely to affect the integrity of the services the Government may expect from the employee.

*****    §118. Interference with certain protective functions
    Any person who knowingly and willfully obstructs, resists, or interferes with a Federal law enforcement agent engaged, within the United States or the special maritime territorial jurisdiction of the United States, in the performance of the protective functions authorized under section 37 of the State Department Basic Authorities Act of 1956 (22 U.S.C. 2709) or section 103 of the Diplomatic Security Act (22 U.S.C. 4802) shall be fined under this title, imprisoned not more than 1 year, or both.

*****    §119. Protection of individuals performing certain official duties
    (a) In General.
        -Whoever knowingly makes restricted personal information about a covered person, or a member of the immediate family of that covered person, publicly available-
            (1) with the intent to threaten, intimidate, or incite the commission of a crime of violence against that covered person, or a member of the immediate family of that covered person; or
            (2) with the intent and knowledge that the restricted personal information will be used to threaten, intimidate, or facilitate the commission of a crime of violence against that covered person, or a member of the immediate family of that covered person,
        -shall be fined under this title, imprisoned not more than 5 years, or both.
        (b) Definitions.-In this section-
            (1) the term "restricted personal information" means, with respect to an individual, the Social Security number, the home address, home phone number, mobile phone number, personal email, or home fax number of, and identifiable to, that individual;
            (2) the term "covered person" means-
                (A) an individual designated in section 1114;
                (B) a grand or petit juror, witness, or other officer in or of, any court of the United States, or an officer who may be, or was, serving at any examination or other proceeding before any United States magistrate judge or other committing magistrate;
                (C) an informant or witness in a Federal criminal investigation or prosecution; or
                (D) a State or local officer or employee whose restricted personal information is made publicly available because of the participation in, or assistance provided to, a Federal criminal investigation by that officer or employee;
            (3) the term "crime of violence" has the meaning given the term in section 16; and
            (4) the term "immediate family" has the meaning given the term in section 115(c)(2).


*****    §115. Influencing, impeding, or retaliating against a Federal official by threatening or injuring a family member
    (a)(1) Whoever-
        (A) assaults, kidnaps, or murders, or attempts or conspires to kidnap or murder, or threatens to assault, kidnap or murder a member of the immediate family of a United States official, a United States judge, a Federal law enforcement officer, or an official whose killing would be a crime under section 1114 of this title; or
        (B) threatens to assault, kidnap, or murder, a United States official, a United States judge, a Federal law enforcement officer, or an official whose killing would be a crime under such section,
    -with intent to impede, intimidate, or interfere with such official, judge, or law enforcement officer while engaged in the performance of official duties, or with intent to retaliate against such official, judge, or law enforcement officer on account of the performance of official duties, shall be punished as provided in subsection (b).

    (2) Whoever assaults, kidnaps, or murders, or attempts or conspires to kidnap or murder, or threatens to assault, kidnap, or murder, any person who formerly served as a person designated in paragraph (1), or a member of the immediate family of any person who formerly served as a person designated in paragraph (1), with intent to retaliate against such person on account of the performance of official duties during the term of service of such person, shall be punished as provided in subsection (b).

    §(b)
    (1)     The punishment for an assault in violation of this section is-
            (A) a fine under this title; and
            (B)
                (i)     if the assault consists of a simple assault, a term of imprisonment for not more than 1 year;
                (ii)     if the assault involved physical contact with the victim of that assault or the intent to commit another felony, a term of imprisonment for not more than 10 years;
                (iii)     if the assault resulted in bodily injury, a term of imprisonment for not more than 20 years; or
                (iv)     if the assault resulted in serious bodily injury (as that term is defined in section 1365 of this title, and including any conduct that, if the conduct occurred in the special maritime and territorial jurisdiction of the United States, would violate section 2241 or 2242 of this title) or a dangerous weapon was used during and in relation to the offense, a term of imprisonment for not more than 30 years.
    (2)        A kidnapping, attempted kidnapping, or conspiracy to kidnap in violation of this section shall be punished as provided in section 1201 of this title for the kidnapping or attempted kidnapping of, or a conspiracy to kidnap, a person described in section 1201(a)(5) of this title.
        (3) A murder, attempted murder, or conspiracy to murder in violation of this section shall be punished as provided in sections 1111, 1113, and 1117 of this title.
        (4) A threat made in violation of this section shall be punished by a fine under this title or imprisonment for a term of not more than 10 years, or both, except that imprisonment for a threatened assault shall not exceed 6 years.
        (c) As used in this section, the term-
            (1) "Federal law enforcement officer" means any officer, agent, or employee of the United States authorized by law or by a Government agency to engage in or supervise the prevention, detection, investigation, or prosecution of any violation of Federal criminal law;
            (2) "immediate family member" of an individual means-
                (A) his spouse, parent, brother or sister, child or person to whom he stands in loco parentis; or
                (B) any other person living in his household and related to him by blood or marriage;
            (3) "United States judge" means any judicial officer of the United States, and includes a justice of the Supreme Court and a United States magistrate judge; and
            (4) "United States official" means the President, President-elect, Vice President, Vice President-elect, a Member of Congress, a member-elect of Congress, a member of the executive branch who is the head of a department listed in 5 U.S.C. 101, or the Director of the Central Intelligence Agency.
        (d) This section shall not interfere with the investigative authority of the United States Secret Service, as provided under sections 3056, 871, and 879 of this title.
        (e) There is extraterritorial jurisdiction over the conduct prohibited by this section.
§116. Female genital mutilation

***** YOU'LL HAVE TO ASK THE FBI/NSA TO SEE IF THEY WILL VERIFY THIS *****



 

– I HOPE YOU UNDERSTAND WHERE THIS ALSO PRESENTS A CONFLICT, AS HE BELIEVES THIS TO BE TRUE.
                                                    1_u.s._v._brian_benjamin_indictment (1).pdf

    NYSCEF MATTER 153974/2020
    - SHARED ADDRESS WITH THE WILSON ELSER LAW FIRM, BELOW.

    Filing User Shari Laskowitz | slaskowitz@ingramllp.com | 2129079600

    150 East 42nd Street 19th Floor, New York, NY 10017 Filed: 07/21/2020

-------- Forwarded Message --------
Subject: 	Voicemail from Mr. PAUL regan
Date: 	Sun, 26 Jun 2022 16:51:47 -0400
From: 	BO DINCER <bondstrt007@gmail.com>
To: 	customerservice@nypost.com, espnfrontrow@espn.com, teschmann@mskyline.com, Joseph Giamboi, ESQ <joseph.giamboi@brooklaw.edu>, LZUCKER@mskyline.com, sgo2107@columbia.edu, letters@nypost.com, Laskowitz, Shari <slaskowitz@ingramllp.com>, dallas-reserve-mgmt@dal.frb.org, 23pctdvo@nypd.com, 23pctyco@nypd.org, 1pctdvo@nypd.org, 1pctyco@nypd.org, praghuram2@bloomberg.net, PRIYA.RAGHURAM@MORGANSTANLEY.COM <PRIYA.RAGHURAM@morganstanley.com>, JAMES GORMAN [MORGAN STANLEY] <james.gorman@morganstanley.com>, Dow Jones <wsjprosupport@dowjones.com>, paul.jones@tudor.com, Paul Regan <LEGAL@mskyline.com>, LEGALASST@mskyline.com, MSKYLINE <anne@thehighlandpartners.com>, cweiss@ingramllp.com, info@statefarm.com, State Farm <mutualfunds@statefarm.com>, David Moore <david.moore.ct95@statefarm.com>, hillary.davis@latimes.com, Scott Holcomb <scott@holcombward.com>, SOHO HOUSE <membership@sohohouse.com>
CC: 	KATHY HOCHUL <governor.hochul@exec.ny.gov>, BBO 121 <ms60710444266@yahoo.com>, MIT Sloan Executive Education <executive_education@mailsvc.sloan.mit.edu>, Marc Lavigne <tessier3@stanford.edu>, NYSCEF PROCESS HD <oca_hd_processor@nycourts.gov>, The New York Times <help@nytimes.com>, administration@mskyline.com, MANHATTAN SKYLINE, LLC. <ADMINISTRATOR@mskyline.com>


I am terrified, where is he ? Touching himself or making videos with my Glamour shots.

Thats actually a compound, in the scope of avoidance to prosecution. 

Truly a delusional group, never met them.

---
## [OhMyVenyx/kernel_xiaomi_ysl](https://github.com/OhMyVenyx/kernel_xiaomi_ysl)@[bc18d64ba1...](https://github.com/OhMyVenyx/kernel_xiaomi_ysl/commit/bc18d64ba16ed06117f137d378b33c0c7d5e2a59)
#### Monday 2022-06-27 19:57:39 by Angelo G. Del Regno

Merge: Performance improvements.

This patchset brings some performance improvements and the addition of the LZO-RLE
algorithm to the kernel, also usable in zram (yup, tested, works but LZ4 is still ok for us).

The main performance improvement is for SWAP space: the locking has changed and
the swap cache is now split in 64MB trunks.
This gives us a reduction of the median page fault latency of 375%, from 15uS to 4uS,
and an improvement of 192% on the swap throughput (this includes "virtual" swap
devices, like zRAM!). The real world user experience improvement of this on a mobile
device is seen after a day or two of usage, where it usually starts losing just a little
performance due to the large amount of apps kept open in background: now I cannot
notice any more performance loss and the user experience is now basically the same as
if the phone was in its first 2 hours of boot life.

Other performance improvements include, in short:

    UDP v4/v6: 10% more performance on single RX queue
    Userspace applications will be faster when checking running time of threads
    2-5% improvements on heavy multipliers (yeah, not a lot, but was totally free...)
    Improvements on rare conditions during sparsetruncate of about 0.3% to a
    way more rare around 20% improvement (that's never gonna happen, but there
    is no performance drop anywhere).

Tested on SoMC Tama Akatsuki RoW

This was taken from
Repo:
https://github.com/sonyxperiadev/kernel
PR: 2039 ([2.3.2.r1.4] Performance improvements)

Signed-off-by: R.A.P <rhmd.19801@gmail.com>

---
## [dashpay/dash](https://github.com/dashpay/dash)@[67ceda1b5a...](https://github.com/dashpay/dash/commit/67ceda1b5aa0c51f1fdce4fb71ccba1922e880f6)
#### Monday 2022-06-27 19:58:35 by fanquake

Merge #18295: scripts: add MACHO lazy bindings check to security-check.py

5ca90f8b598978437340bb8467f527b9edfb2bbf scripts: add MACHO lazy bindings check to security-check.py (fanquake)

Pull request description:

  This is a slightly belated follow up to #17686 and some discussion with Cory. It's not entirely clear if we should make this change due to the way the macOS dynamic loader appears to work. However I'm opening this for some discussion. Also related to #17768.

  #### Issue:
  [`LD64`](https://opensource.apple.com/source/ld64/) doesn't set the [MH_BINDATLOAD](https://opensource.apple.com/source/xnu/xnu-6153.11.26/EXTERNAL_HEADERS/mach-o/loader.h.auto.html) bit in the header of MACHO executables, when building with `-bind_at_load`. This is in contradiction to the [documentation](https://opensource.apple.com/source/ld64/ld64-450.3/doc/man/man1/ld.1.auto.html):
  ```bash
  -bind_at_load
       Sets a bit in the mach header of the resulting binary which tells dyld to
       bind all symbols when the binary is loaded, rather than lazily.
  ```

  The [`ld` in Apples cctools](https://opensource.apple.com/source/cctools/cctools-927.0.2/ld/layout.c.auto.html) does set the bit, however the [cctools-port](https://github.com/tpoechtrager/cctools-port/) that we use for release builds, bundles `LD64`.

  However; even if the linker hasn't set that bit, the dynamic loader ([`dyld`](https://opensource.apple.com/source/dyld/)) doesn't seem to ever check for it, and from what I understand, it looks at a different part of the header when determining whether to lazily load symbols.

  Note that our release binaries are currently working as expected, and no lazy loading occurs.

  #### Example:

  Using a small program, we can observe the behaviour of the dynamic loader.

  Conducted using:
  ```bash
  clang++ --version
  Apple clang version 11.0.0 (clang-1100.0.33.17)
  Target: x86_64-apple-darwin18.7.0

  ld -v
  @(#)PROGRAM:ld  PROJECT:ld64-530
  BUILD 18:57:17 Dec 13 2019
  LTO support using: LLVM version 11.0.0, (clang-1100.0.33.17) (static support for 23, runtime is 23)
  TAPI support using: Apple TAPI version 11.0.0 (tapi-1100.0.11)
  ```

  ```cpp
  #include <iostream>
  int main() {
  	std::cout << "Hello World!\n";
  	return 0;
  }
  ```

  Compile and check the MACHO header:
  ```bash
  clang++ test.cpp -o test
  otool -vh test
  ...
  Mach header
        magic cputype cpusubtype  caps    filetype ncmds sizeofcmds      flags
  MH_MAGIC_64  X86_64        ALL LIB64     EXECUTE    16       1424   NOUNDEFS DYLDLINK TWOLEVEL WEAK_DEFINES BINDS_TO_WEAK PIE

  # Run and dump dynamic loader bindings:
  DYLD_PRINT_BINDINGS=1 DYLD_PRINT_TO_FILE=no_bind.txt ./test
  Hello World!
  ```

  Recompile with `-bind_at_load`. Note still no `BINDATLOAD` flag:
  ```bash
  clang++ test.cpp -o test -Wl,-bind_at_load
  otool -vh test
  Mach header
        magic cputype cpusubtype  caps    filetype ncmds sizeofcmds      flags
  MH_MAGIC_64  X86_64        ALL LIB64     EXECUTE    16       1424   NOUNDEFS DYLDLINK TWOLEVEL WEAK_DEFINES BINDS_TO_WEAK PIE
  ...
  DYLD_PRINT_BINDINGS=1 DYLD_PRINT_TO_FILE=bind.txt ./test
  Hello World!
  ```

  If we diff the outputs, you can see that `dyld` doesn't perform any lazy bindings when the binary is compiled with `-bind_at_load`, even if the `BINDATLOAD` flag is not set:
  ```diff
  @@ -1,11 +1,27 @@
  +dyld: bind: test:0x103EDF030 = libc++.1.dylib:__ZNKSt3__16locale9use_facetERNS0_2idE, *0x103EDF030 = 0x7FFF70C9FA58
  +dyld: bind: test:0x103EDF038 = libc++.1.dylib:__ZNKSt3__18ios_base6getlocEv, *0x103EDF038 = 0x7FFF70CA12C2
  +dyld: bind: test:0x103EDF068 = libc++.1.dylib:__ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEE6sentryC1ERS3_, *0x103EDF068 = 0x7FFF70CA12B6
  +dyld: bind: test:0x103EDF070 = libc++.1.dylib:__ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEE6sentryD1Ev, *0x103EDF070 = 0x7FFF70CA1528
  +dyld: bind: test:0x103EDF080 = libc++.1.dylib:__ZNSt3__16localeD1Ev, *0x103EDF080 = 0x7FFF70C9FAE6
  <trim>
  -dyld: lazy bind: test:0x10D4AC0C8 = libsystem_platform.dylib:_strlen, *0x10D4AC0C8 = 0x7FFF73C5C6E0
  -dyld: lazy bind: test:0x10D4AC068 = libc++.1.dylib:__ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEE6sentryC1ERS3_, *0x10D4AC068 = 0x7FFF70CA12B6
  -dyld: lazy bind: test:0x10D4AC038 = libc++.1.dylib:__ZNKSt3__18ios_base6getlocEv, *0x10D4AC038 = 0x7FFF70CA12C2
  -dyld: lazy bind: test:0x10D4AC030 = libc++.1.dylib:__ZNKSt3__16locale9use_facetERNS0_2idE, *0x10D4AC030 = 0x7FFF70C9FA58
  -dyld: lazy bind: test:0x10D4AC080 = libc++.1.dylib:__ZNSt3__16localeD1Ev, *0x10D4AC080 = 0x7FFF70C9FAE6
  -dyld: lazy bind: test:0x10D4AC070 = libc++.1.dylib:__ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEE6sentryD1Ev, *0x10D4AC070 = 0x7FFF70CA1528
  ```

  Note: `dyld` also has a `DYLD_BIND_AT_LAUNCH=1` environment variable, that when set, will force any lazy bindings to be non-lazy:
  ```bash
  dyld: forced lazy bind: test:0x10BEC8068 = libc++.1.dylib:__ZNSt3__113basic_ostream
  ```

  #### Thoughts:
  After looking at the dyld source, I can't find any checks for `MH_BINDATLOAD`. You can see the flags it does check for, such as MH_PIE or MH_BIND_TO_WEAK [here](https://opensource.apple.com/source/dyld/dyld-732.8/src/ImageLoaderMachO.cpp.auto.html).

  It seems that the lazy binding of any symbols depends on whether or not [lazy_bind_size](https://opensource.apple.com/source/xnu/xnu-6153.11.26/EXTERNAL_HEADERS/mach-o/loader.h.auto.html) from the `LC_DYLD_INFO_ONLY` load command is > 0. Which was mentioned in [#17686](https://github.com/bitcoin/bitcoin/pull/17686#issue-350216254).

  #### Changes:
  This PR is one of [Corys commits](https://github.com/theuni/bitcoin/commit/7b6ba26178d2754568a1308d3d44e038e9ebf450), that I've rebased and modified to make build. I've also included an addition to the `security-check.py` script to check for the flag.

  However, given the above, I'm not entirely sure this patch is the correct approach. If the linker no-longer inserts it, and the dynamic loader doesn't look for it, there might be little benefit to setting it. Or, maybe this is an oversight from Apple and needs some upstream discussion. Looking for some thoughts / Concept ACK/NACK.

  One alternate approach we could take is to drop the patch and modify security-check.py to look for `lazy_bind_size` == 0 in the `LC_DYLD_INFO_ONLY` load command, using `otool -l`.

ACKs for top commit:
  theuni:
    ACK 5ca90f8b598978437340bb8467f527b9edfb2bbf

Tree-SHA512: 444022ea9d19ed74dd06dc2ab3857a9c23fbc2f6475364e8552d761b712d684b3a7114d144f20de42328d1a99403b48667ba96885121392affb2e05b834b6e1c

---
## [macownersclub/melpa](https://github.com/macownersclub/melpa)@[570bde6b4b...](https://github.com/macownersclub/melpa/commit/570bde6b4b89eb74eaf47dda64004cd575f9d953)
#### Monday 2022-06-27 20:14:04 by Jonas Bernoulli

Cosmetic changes to numerous recipes

This commit only touches recipes whose `:files' property contains an
`:exclude' element, because I had to look at all those recipes for an
only marginally related reason.

To an extend these changes only reflect my own personal preference, so
I will explain the types of changes I have made.  This should serve as
a starting point for a future discussion in case we want to encourage
a certain style or even enforce it.

- Lines should be intended as `indent-for-tab-command' would, except
  in special-cases such as in the recipe of `use-package', which is
  also a macro with special indentation rules; we override those
  because the `use-package' in use-package's recipe is not that macro,
  it is just a symbol appearing as the first element of a data list.

- I prefer it if there is a newline between the package symbol (the
  car) and the plist that follows, but usually only add it to existing
  recipes when lines would otherwise get to long.  I also do not
  change this if I am not making any other changes that affect more
  than one line.

- Either the complete list should be on a single line or each line
  should contain only one key/value pair.  The first pair may share a
  line with the package symbol (see previous point).  If the recipe
  needs more than one line, then two key/value pairs should never
  appear on one line.  Newline characters are cheap enough these days.

- `:fetcher' should come before `:url' or `:repo', not least because
  the former dictates which of the latter two is required/valid.  You
  can also think of the fetcher as the type or class of the recipe,
  which IMO should come first, like in code: (git-fetcher :url val).

- The most common keywords should be specified in this order:
  `:fetcher', `:url'/`:repo', `:files'.  Other keywords should go
  either before or after `:files' (but preferable not on both sides
  of that for any given recipe).

- A common value of `:files' is: (:defaults (:exclude "...")).
  This could be split across multiple lines, but writing everything
  on one line makes it easier to read it as 'use the defaults, except
  exclude "..."':

    :files (:defaults (:exclude "..."))

- If the value of `:files' is too long for one line, then place
  newlines "semantically", instead of trying to "save space".  For
  example any element that is a list should appear on its own line.
  Two sibling lists should never appear on the same line.  String
  siblings should also not appear on one line in many cases, though
  it might makes sense (but isn't my preference) to group them by
  "type" as in:

    (:defaults
     "foo/*.el" "bar/*.el"
     "docs/foo/*.texi" "docs/bar/*.texi"
     (:exclude "..."))

- While there may be multiple (:exclude ...) elements, I've merged
  them into one.  Mostly for future proofing.

- The position of `:exclude' elements in `:files' value is significant
  in theory.  However in most cases it already appears at the very end
  and I have moved it there in cases where the order is not
  significant.  Mostly for future proofing.

---
## [AttorneyOnline/akashi](https://github.com/AttorneyOnline/akashi)@[01fb5c143b...](https://github.com/AttorneyOnline/akashi/commit/01fb5c143b1cff7a3d7ae43438e8c0d3b4129d48)
#### Monday 2022-06-27 20:47:10 by Salanto

For the love of all that is holy why the fuck do you not work

---
## [newstools/2022-express](https://github.com/newstools/2022-express)@[371e219e8b...](https://github.com/newstools/2022-express/commit/371e219e8bfb2e4a167c4a0582710dfdc9dde1d7)
#### Monday 2022-06-27 21:22:22 by Billy Einkamerer

Created Text For URL [www.express.co.uk/sport/tennis/1631311/Does-Emma-Raducanu-have-a-boyfriend-British-star-love-life-tennis-news]

---
## [fighterslam/Pariah-Station](https://github.com/fighterslam/Pariah-Station)@[23aef65ad5...](https://github.com/fighterslam/Pariah-Station/commit/23aef65ad58754e8327151ece4c0efa6d810e1ed)
#### Monday 2022-06-27 22:18:34 by SabreML

Refactors how legs are displayed so they no longer appear above one-another when looking EAST or WEST (#66607) (#704)

So, for over 5 years, left legs have been displaying over right legs. Never noticed it? Don't blame you.
Here's a nice picture provided by #20603 (Bodypart sprites render with incorrect layering), that clearly displays the issue that was happening:

It still happened to this day.
Notice how the two directions don't look the same? That's because the left leg is always displaying above the right one.

Obviously, that's no good, and I was like "oh, that's a rendering issue, so there's nothing I can do about it, it's an issue with BYOND".

Until it struck me.

"What if we used a mask that would cut out the parts of the right leg, from the left leg, so that it doesn't actually look as if it's above it?"

Here I am, after about 25 hours of work, 15 of which of very painful debugging due to BYOND's icon documentation sucking ass.

So, how does it work?

Basically, we create a mask of a left leg (that'll be explained later down the line), more specifically, a cutout of JUST the WEST dir of the left leg, with every other dir being just white squares. We then cache that mask in a static list on the right leg, so we don't generate it every single time, as that can be expensive. All that happens in update_body_parts(), where I've made it so legs are handled separately, to avoid having to generate limb icons twice in a row, due to it being expensive. In that, when we generate_limb_icon() a right leg, we apply the proper left leg mask if necessary.

Now, why masking the right leg, if the issue was the left leg?
Because, see, when you actually amputated someone, and gave them a leg again, it would end up being that new leg that would be displayed below the other leg. So I fixed that, by making it so that bodyparts would be sorted correctly, before the end of update_body_parts(). Which means that right legs ended up displaying above left legs, which meant that I had to change everything I had written to work on right legs rather than left legs.

I spent so much time looking up BYOND documentation for MapColors() and filters and all icon and image vars and procs, I decided to make a helper proc called generate_icon_alpha_mask(), because honestly it would've saved me at least half a day of pure code debugging if I had it before working on this refactor.

I tried to put as much documentation down as I could, because this shit messes with your brain if you spend too long looking at it. icon and image are two truly awful classes to work with, and I don't look forward to messing with them more in the future.

Anyway. It's nice, because it requires no other effort from anyone, no matter what the shape of the leg is actually like. It's all handled dynamically, and only one per type of leg, meaning that it's not actually too expensive either, which is very nice. Especially since it's very downstreams-friendly from being done this way.


It fixes #20603 (Bodypart sprites render with incorrect layering), an issue that has been around for over half a decade, as well as probably many more issues that I just didn't bother sifting through.

Plus, it just looks so much better.

Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>

---
## [fighterslam/Pariah-Station](https://github.com/fighterslam/Pariah-Station)@[95db2c6bfc...](https://github.com/fighterslam/Pariah-Station/commit/95db2c6bfc84871f2fa51eeef253f681dc46a632)
#### Monday 2022-06-27 22:18:34 by Kapu1178

Makes glass floors override platings. Fixes glass floor openspace bug. (#66301) (#696)

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

Co-authored-by: vincentiusvin <54709710+vincentiusvin@users.noreply.github.com>

---
## [gitster/git](https://github.com/gitster/git)@[9c986917b0...](https://github.com/gitster/git/commit/9c986917b00fd81bc7427ff46da768582f518633)
#### Monday 2022-06-27 23:02:29 by Glen Choo

setup.c: create `discovery.bare`

There is a known social engineering attack that takes advantage of the
fact that a working tree can include an entire bare repository,
including a config file. A user could run a Git command inside the bare
repository thinking that the config file of the 'outer' repository would
be used, but in reality, the bare repository's config file (which is
attacker-controlled) is used, which may result in arbitrary code
execution. See [1] for a fuller description and deeper discussion.

A simple mitigation is to forbid bare repositories unless specified via
`--git-dir` or `GIT_DIR`. In environments that don't use bare
repositories, this would be minimally disruptive.

Create a config variable, `discovery.bare`, that tells Git whether or
not to die() when it discovers a bare repository. This only affects
repository discovery, thus it has no effect if discovery was not
done, e.g. if the user passes `--git-dir=my-dir`, discovery will be
skipped and my-dir will be used as the repo regardless of the
`discovery.bare` value.

This config is an enum of:

- "always": always allow bare repositories (this is the default)
- "never": never allow bare repositories

If we want to protect users from such attacks by default, neither value
will suffice - "always" provides no protection, but "never" is
impractical for bare repository users. A more usable default would be to
allow only non-embedded bare repositories ([2] contains one such
proposal), but detecting if a repository is embedded is potentially
non-trivial, so this work is not implemented in this series.

[1]: https://lore.kernel.org/git/kl6lsfqpygsj.fsf@chooglen-macbookpro.roam.corp.google.com
[2]: https://lore.kernel.org/git/5b969c5e-e802-c447-ad25-6acc0b784582@github.com

Signed-off-by: Glen Choo <chooglen@google.com>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---

