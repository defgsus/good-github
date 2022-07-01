## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-06-30](docs/good-messages/2022/2022-06-30.md)


1,729,468 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,729,468 were push events containing 2,509,183 commit messages that amount to 186,018,201 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 43 messages:


## [fbescodam/webserv](https://github.com/fbescodam/webserv)@[b88d0fa31e...](https://github.com/fbescodam/webserv/commit/b88d0fa31e352a204e59c1a9ebe74598d60a2141)
#### Thursday 2022-06-30 00:02:16 by TheBriar

getcontentype weird ass linker error fixed, shits fucked

Co-authored-by: Freek Bes <FreekBes@users.noreply.github.com>
Co-authored-by: W2Wizard <W2Wizard@users.noreply.github.com>

---
## [Offroaders123/NBT-Parser](https://github.com/Offroaders123/NBT-Parser)@[e642d2c41b...](https://github.com/Offroaders123/NBT-Parser/commit/e642d2c41b7aedf2ea11aeed7e4d2a849376fa48)
#### Thursday 2022-06-30 00:08:51 by Offroaders123

Read Function + Browser Checks

Additions:
- Added improved parameter type validation to the `read` function and `Reader` constructor.
- I am also planning to look into TypeScript type declarations in the next few updates! I'll use `d.ts` files for the types rather than moving the project over to TypeScript, because I like that everything works with only vanilla JS out of the box! No need to build for Node or the browser, it already works directly for both (Of couse, using a bundler to make adding it easier is always a great option though, I just don't want it to be mandatory to run the library).

Changes:
- Restructued the `read` function to fully include all of it's own logic! Now it doesn't need help from the additional  hidden `runReader` function.

Fixes:
- Tested support for the parser within the browser, and fixed a few issues that allow you to either read NBT by passing an `ArrayBuffer`, or `TypedArray`. It was working as expected with `TypedArrays`, but I had to add a few wrappers to allow you to input `ArrayBuffers` as well. This was also the case for Node, but you usually deal with `Buffer` over there, and that's an instance of `Uint8Array`, so you wouldn't encounter the `ArrayBuffer` issues. The reader logic essentially just wasn't expecting to have an `ArrayBuffer` as an entry, and that's what I fixed.
- Adjusted the Bedrock Level header check logic, as it appeared to be throwing double negatives unexpectedly. I accidentally made it less accurate with the last update, so that's fixed now.

Oh yeah!
- Forgot to mention this for some time now, but I actually completely replaced Chrome OS on my Chromebook, and now it runs full Ubuntu! It's a great experience, it's convinced me that the next laptop I get will be for solely Linux (probably Ubuntu), as it has been so nice to install things on here for my dev work. It honestly feels like what I would *wish* macOS could be. The fact of how many things I can change to my liking are so fun and relieving, it's such a nice user experience. GNOME has been very awesome, I got it to be exactly how I want it to work, and the toucpad gestures are also a great bonus.
- I made the jump back around the beginning of May, and I forgot to mention it in any of my commit logs (Since that seems to be my blog post setup for some reason, haha).
- If you have an old Chromebook that you don't have a use for anymore, try looking into if you want to get Linux on there, mine has a brand new life with Ubuntu, it's actually unbelievable what it can do now! The only thing I don't like about it is just that my Chromebook is't quite to powerful and it only has 16GB of onboard storage, so I live at about 90% of it full with a gig left for programming. Not the best at times, but hey, this Chromebook was only $20 after my senior year, and it just had it's Chrome OS end of life a few days ago (sometime in June), and he's still got much more to go after this, thanks to Linux :)

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[8ffe0ac276...](https://github.com/odoo-dev/odoo/commit/8ffe0ac2761f64ebcab57853fd7c390885b66be5)
#### Thursday 2022-06-30 00:14:03 by Habib (ayh)

[fix] web: the new arch parser sucks - so I do something stupid to prove to JS team that we do support editing a one2many - I'd like to find a solution that doesn't require the <tree> arch - but for now this is the only way...why? because basic_model does not seem to allow  records to a   without the damn arch

---
## [Jolly-66/Skyrat-tg](https://github.com/Jolly-66/Skyrat-tg)@[a1fe30230b...](https://github.com/Jolly-66/Skyrat-tg/commit/a1fe30230baaef9736cebee442c902180ff85ce5)
#### Thursday 2022-06-30 00:58:41 by SkyratBot

[MIRROR] [MDB Ignore] Shifts all (sane) varedited signs to directionals  [MDB IGNORE] (#14549)

* [MDB Ignore] Shifts all (sane) varedited signs to directionals  (#68004)

* [MDB Ignore] Shifts all (sane) varedited signs to directionals

Hey there,

So we have these cool new sign directionals now, but we still have all of the old pixel-shifted pre-fabrications lying around. So, I added an UpdatePaths (as well as Updated the Paths) to be a bit better at using directionals, because directionals are pretty neato.

This should update every single var_edit that used the proper 32 pixelshift (some of them used 28, and I'm unable to account for that automatically with current tooling) into a proper subtype. Mappers tend to learn by looking at well established maps, so it's always important to ensure that the well-established maps use the most recent tooling (i.e.: bring them up to the surface) and avoid needless excess lines in maps.

* The Commit With All The Maps

OH GOD OH FUCK

* Renames the UpdatePaths

* [MDB Ignore] Shifts all (sane) varedited signs to directionals

* updates all our maps

Co-authored-by: san7890 <the@san7890.com>
Co-authored-by: Jolly-66 <70232195+Jolly-66@users.noreply.github.com>

---
## [0kmg/mame](https://github.com/0kmg/mame)@[ba63081d10...](https://github.com/0kmg/mame/commit/ba63081d109c904902958c6324b013cb10b42732)
#### Thursday 2022-06-30 01:01:37 by 0kmg

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
## [Petuuuhhh/pokemon-showdown-client](https://github.com/Petuuuhhh/pokemon-showdown-client)@[be9a95cbc6...](https://github.com/Petuuuhhh/pokemon-showdown-client/commit/be9a95cbc683c04c6ead95d5643c7ea551607a56)
#### Thursday 2022-06-30 01:10:09 by Guangcong Luo

Fix bugs caused by Preact update

The new Preact version seems to have broken a lot of low-level
magic we used. We plausibly shouldn't be using such low-level magic
in the first place, but that's a conversation for another day.

In particular:

1. `preact.render` seems to replace all of `containerNode`'s contents
   if `replaceNode` isn't passed (previously, it would append a child).
   This is an insane thing to change without any documentation... Maybe
   I'm misunderstanding it?

2. Making a button value an uncontrolled form was a pretty big hack
   in the first place, but at least it worked. Now that it doesn't,
   we're giving up and switching to controlled forms, which makes the
   code a lot nicer, fixes a bug, and I should probably have just done
   in the first place.

---
## [Spyroshark/Pariah-Station](https://github.com/Spyroshark/Pariah-Station)@[c77fb1e795...](https://github.com/Spyroshark/Pariah-Station/commit/c77fb1e7959bec41276673ba903da1625be8b68e)
#### Thursday 2022-06-30 03:06:36 by Octus

Parallax but better: Smooth movement cleanup (#66567) (#724)

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

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [Spyroshark/Pariah-Station](https://github.com/Spyroshark/Pariah-Station)@[70a87f9510...](https://github.com/Spyroshark/Pariah-Station/commit/70a87f95100c290699ce5b92bb099d2f56bbb336)
#### Thursday 2022-06-30 03:06:36 by Gallyus

HOLY SHIT SHUT UP (#742)

* HOLY SHIT SHUT UP

* Apply suggestions from code review

* seeba sauce

---
## [t-toasted/goonstation](https://github.com/t-toasted/goonstation)@[e7149b1537...](https://github.com/t-toasted/goonstation/commit/e7149b153782292bd9d01a82c984a51d8cbae74b)
#### Thursday 2022-06-30 03:09:53 by t-toasted

first pass at lights. Funny note: had to remove a figure because it attacked itself and crashed my client somehow god bless

---
## [krunalbhandekar/Youtube-Clone](https://github.com/krunalbhandekar/Youtube-Clone)@[fbd6166680...](https://github.com/krunalbhandekar/Youtube-Clone/commit/fbd616668077bd48b11f49ac4e8c7b91e3aba5db)
#### Thursday 2022-06-30 05:21:17 by Krunal Bhandekar

Youtube clone

Enjoy the videos and music you love with friends, family.

---
## [Koi-3088/ForkBot.NET](https://github.com/Koi-3088/ForkBot.NET)@[7bb0bd3050...](https://github.com/Koi-3088/ForkBot.NET/commit/7bb0bd3050b8f72ca32d8e495b6d653b02f778e3)
#### Thursday 2022-06-30 06:10:44 by Koi

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
## [LoganMercadillo/seo-climatiq](https://github.com/LoganMercadillo/seo-climatiq)@[d0254fb872...](https://github.com/LoganMercadillo/seo-climatiq/commit/d0254fb87257ddb11e869e10b3108d9728a98e7e)
#### Thursday 2022-06-30 06:32:58 by LoganMercadillo

FIXED convert JSON to DataFrame in climate.py

I'm too exhausted to write a complete, detailed
account of what I've done. Simple version is that
I wasted a bunch of time trying to flatten nested
dictionaries with my own function. I finally saw
that I could use pandas.json_normalize() to do it
for me. I feel like an idiot, but it's a
"learning experience," like Anthony told me at
1:30am. I did it!

[Ticket: fuck you shut up]

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[6f41a9eb0c...](https://github.com/treckstar/yolo-octo-hipster/commit/6f41a9eb0ce90a4fe7c3142df716a476135c430a)
#### Thursday 2022-06-30 08:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [Offroaders123/NBT-Parser](https://github.com/Offroaders123/NBT-Parser)@[11f40c59fd...](https://github.com/Offroaders123/NBT-Parser/commit/11f40c59fd7fe485ada681b84c8c6597cfc0a9a8)
#### Thursday 2022-06-30 08:45:52 by Offroaders123

A New Writer-Up

Additions:
- Added checks to the start of the `write` function and `Writer` constructor. TypeScript type definitions coming soon! I have a tab open about it right now :)

Changes:
- Rewrote the `write` function and `Writer` class, a similar set of changes as to what I did over on the reading side of things yesterday.
- One of the bigger changes to the write methods, now each one has all of it's logic built in, as now there's no more `write` method, only each method for writing each type. It is a little more code, but it is a bit better at showing what each function does.
- For each of the write methods with for loops, each one now uses either `for of` or `for in` loops where possible, rather than just a standard `for` loop. I like the simplicity of those a lot, and I realized that they could apply great here too.
- Added a few more variables to break up some of the looping functions, as it was pretty complex to comprehend what each section was selecting. It should also be a bit easier to debug with those in there too, since you can just add a `console.log()` to see what the variable's value is, rather than having to write the call out again to break part of it up to get the intermediate values in there.

Oh yeah!
- Listening to Closure / Continuation for the second time through as of now, "Of The New Day" right now! First time listening to it yesterday afternoon, wow did they do a great job! Can't believe PT is releasing new material again.
- Finally found a nice version of Insignificance on YouTube, so that will probably be my copy of that eventually. I also will be getting Yellow Hedgerow Dreamscape too, the album that is. The song is epic, and the extra hard to find compilation album is an extension of that. There are more and more cool hidden gems out there, you just have to look a little harder to find them!
- Oh yeah, and I came across their first concert on Bandcamp too, that is also a likely must buy! Back in 1993, at Nag's Head, an extra epic venue that used to be around. Just read that they turned it into flats in 2018 I heard, bummer! The sound quality on the recording was great, even for coming up on 30 years ago. I was -10 :O
- Ok, and I have to mention how much I love Up the Downstair, just gotta say...

---
## [jak-sdk/OfficeDocs-Exchange](https://github.com/jak-sdk/OfficeDocs-Exchange)@[b258c0d83e...](https://github.com/jak-sdk/OfficeDocs-Exchange/commit/b258c0d83e34b4e47365e103ffb8379d2d24c7ed)
#### Thursday 2022-06-30 10:34:51 by Jak

Add more emphasis to risks of extending SPF

Hi,

I believe there should be slightly more warning as to the full impact of adding a new IP address to the SPF record.

This documentation is slightly misleading as it implies at several points in Option 2 that this doesn't allow sending to external recipients, e.g. Line 200 in the "Limitations of direct send"
> Direct send cannot be used to deliver email to external recipients
Whereas following the steps and adding the IP address to the SPF record is sufficient to authorise any users of that IP address to send to external recipients and represent the domain (I'm not mentioning DKIM here because neither does the documentation and we can't assume that all organisations make use of it or enforce it via DMARC).

My real-world experience is that in our company, we were looking at implementing Option 2 to enable a multi-function printer to scan-to-email. The IP address in use is the public IP of our office, which all traffic goes through via NAT. We also have a guest WiFi network that allows guests to access the internet without having access to our office network, but it uses the same NAT IP.
The problem with Option 2 is that any guest WiFi user could send email as any user of our domain, which is a breach of our security requirements.

Step 1 does make reference to the risk:
> You can share your static IP address with other devices and users, but don't share the IP address with anyone outside of your company.

But I'm concerned that it's not highlighted, and other references in Option 2 to direct send not being able to send externally are a little misleading and undermine the message that there is a security risk when adding new IP addresses to the SPF record.

Interested to hear your thoughts,

Thanks,
Jak

---
## [gsora/xous-core](https://github.com/gsora/xous-core)@[6745206303...](https://github.com/gsora/xous-core/commit/67452063034ea98c6fe318c67e7c7109806c5a60)
#### Thursday 2022-06-30 10:41:49 by bunnie

mulling this pile of OpenSK code to see what we should cut, what we should keep

alright. the composite device problem is solved. The bigger issue I'm
mulling is if I should try to port the Google OpenSK FIDO2 stack into
Xous, or if I should just do a limited U2F implementation.

Poking around at the OpenSK stuff...porting looks possible, but, it's
going to be vendoring in all of the source from the OpenSK project. So
it'll be tough to apply patches if they happen; on the other hand, the
OpenSK implementation is FIDO2 certified, and the stable branch hasn't
moved since Nov 2021.

The main downsides of the OpenSK implementation are:

- it uses nightly. I think it can be stripped out, though; I haven't
  seen a "good reason" for it yet, it's mostly because Tock uses
  nightly. There's only one alarming use of it and it's in the crypto
  crates but those will be stripped out because....
- the crypto libraries are in fact not suitable for use. I dug into
  them and they definitely need to be gutted and replaced with the
  community-blessed crypto libraries and APIs. which is one big reason
  why once this goes into Xous land it doesn't go back easily into
  OpenSK land -- they actually have slightly different crypto
  APIs. more modern ones, to be fair, but, they haven't been reviewed.
- the implementation has "too many features"...for example, I don't
  think we'll ever realistically do authenticator attestation as it
  requires signing NDAs and provisioning secret keys that we can't
  share with users. But that code is there, and we'll either have to
  gut or bodge it.

The plusses are:

- it's FIDO2 certified. So, at least the protocol stack is probably
  complete and fully implemented, which means for features we don't
  use today I can just leave hooks or dummy values there for a fast
  migration path.
- Looks like they aren't changing things too fast in the dev
  branch...so this probably is not like riding a greased pig
- Looks like a couple of paid professionals wrote the code...better
  than what we have going on here
- I think I see a path to carve out their "persistent store" and glom
  it into the PDDB; a path to adapt their crypto traits into
  Xous-native traits; and a path to connect their CTAP protocol engine
  to the Xous HID server. So it seems feasible. But they baked in some
  bad API assumptions deeply enough that they are one-way streets I
  think to get these ports done.

I'm going to sleep on this, but I'm leaning toward trying to pull in
the OpenSK code because even tho it is a bit painful it probably gets
a bigger feature scope and so far it looks like I wouldn't be changing
any protocol-level stuff for the port, I would just be monkeying
around with the internal storage, crypto, and USB implementations, so
ideally the end result is we get a certified FIDO2 protocol engine for
the effort.

I think the main concern I have going in this direction is I don't see
a way to do this and simultaneously be able to absorb upstream patches
into this vendored code, because their API assumptions are too
different. Any bug fixes or patches would have to be manually applied
and merged. But maybe that's not such a big deal...?

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[084ef76fa0...](https://github.com/mrakgr/The-Spiral-Language/commit/084ef76fa0475b8f2c882fb8d7c10768f98bc778)
#### Thursday 2022-06-30 11:48:53 by Marko Grdinić

"7:50am. I came back from doing the chores 10m ago and have just been chilling. I am not sure when I got up, but it must have been something like 6am.

8am. Ugh, let me go to bed. I do not feel like even reading manga right now.

9:45am. I was in bed less than I thought. But I do feel less groggy now.

Regarding the sculpting task, I am starting to feel a bit inspired. I'll rant about it later. Let me chill for now.

10:55am. Let me have breakfast here. I feel hung over right now despite haven't having a drop of alchohol.

11:40am. Done with breakfast. Let me finish ch 636 of Legendary Mechanic and I will get started. I want to do some icebreaking.

12:05pm. Done with grapes as well. I've revived a little.

...Ok, let me rant a bit.

When I went to bed at 8am, my thoughts wondered for a bit and then I started thinking about sculpting and got some motivation.

It weird when I think about it. I was really proud for getting the base mesh looking as well as it did last year, but now that I am analyzing my overall worflow, I see that it is all over the place.

This time, my project rather than being a sulpt of a body is a skeleton.

With that goal in mind, I've comparing my old sculpting techniques from last year with my recent ones and I can see immediatelly what the problem is.

I visualize the skeleton in my mind, and immediatelly get lethargic, but once I replaced all the bones with boxes, I start to feel a sense of energy.

This is what my problem was last time - in 2021 I was just starting out and everything was overwhelming. I was just moving along while feeling things out.

12:25pm. I feel so tired again, but let push on with the rant. Maybe after that I'll take a nap for the rest of the day.

What I want to say is - last year I struggled a lot just to grasp the basic things. But right now I am thinking how I could make the skeleton out of tiny boxes and am thinking: 'This won't be hard.'

After that, it is not a big deal to union the them and go into sculpting to make the polished result.

I used to feel that the hard part was in the tiny details, but now I think that the initial block out is where the 80% of the work is.

I want to test this theory. Last year I fiddled so much, a full month just to get the base mesh done.

But now what I want to do is bring my organic sculpting inline with my hard surface skills. It needs to be simple and straightforward.

I have a vision of what the ideal workflow should be. You start out rough with big boxes, and gradually subdivide them and add detail.

Imagine if I tried doing the skeleton like I had the body last year. I'd never get anywhere!

Imagine snake hooking the ribs off the sternum! That would be such a mess. And yet that is how I did the fingers, and yes it was hard.

12:30pm. There are better and worse ways of doing things. By far the worst way is the one used by the anime head guy.

The best way is what I am suggesting here - assemble the body out of primitives, boolean them together and then use sculpting to integrate the parts and do the detailing.

I know Flycat did this on one mesh, but he showcased various different ways of doing it, some of them worse.

Yan does it like I've suggested and does not mess around.

12:35pm. At my present level, I have zero reason to be proud of sculpting. This is in contrast to my Moi work.

If I do the base mesh again and take a month to do it, that would be a disaster.

Instead I will take my hard surface skills, and make them an integral part of the block out phase, making it so that by the time I get to sculpting only the easy stuff is left.

12:40pm. Also doing it like this will mark a change in attitude. I will do this while studying the Anatomy For Sculptors book.

I am going to internalize and master each and every part of the body as I go along.

12:40pm. Come to think it the way he did the base mesh is by starting from a single cube, extruding and subdividing it. When I did my own imitation I took the same approach.

Back then I contrasted that approach with doing the individual block out pieces and booleaning them. The former approach felt more succinct to me, but now I see that I was wrong.

The proper way to do it is to piece it together, only that approach gives you the flexibility of doing sketching in 3d.

The single cube deformation approach gets you into the mindset of thinking about the body as a single large mass and that is not good.

That way of doing it, while not extreme as the anime head guy's is a performance. It is no different from Kim Jung Gi xeroxing stuff from his mind directly onto paper.

You absolutely can't immitate such a thing if you are a regular person. Practice is not enough.

I'd rather find the right workflows that anybody could immitate. Better tools, better techniques - that is how you get better as a programmer, and that is how I intend to get better in art as well. Practice matters too, but without the tools and the techniques to cultivate, you'd only reach a low level.

Well, something like drawing is fundamentally about putting lines on paper, so with strong talent and experience you can reach astonishing heights of skill like Kim.

But in programming this would not work. Imagine if you were the best assembly programmer - you'd still be far behind in productivity compared to a mediocre Python programmer.

12:50pm. Some tools are easier and harder to use.

The manual mode of the Scatter 5 plugin is revolutionary for that reason - even if I don't use it for a few years and then come back, it would be very easy to remember what the scatter brushes do. It is like trying to ride a bike again. But getting a grasp on geo nodes and Houdini's scattering would be a pain in the ass.

I was simply ignorant.

I had no idea that in ray tracing mode Blender could display more poly than using the workbench engine. What a surprise that was. Now that I know the tricks to scattering, I have much less need for Clarisse or Houdini.

1:25pm. Had to take a short break.

Let me conclude the rant - it annoys me to have to work so hard.

Who feels like doing dozens of illustrations, compose music and do writing for a negligible chance to reaching financial security.

I do not want to be burdened with all of that.

And I do not want to burden myself with sculpting a bunch of charas for the next few months.

Who cares about all of that.

In programming I managed to create Spiral by taking it one step at a time.

In art, instead of going forward and trying to churn out things faster, what I want to do is take a step back and cover the missing fundamentals.

In past 9 months I've done a great big tour, so it will be almost a letdown what I am going to do, but it is essential if I want to bring my sculpting to the next level.

Rather than grand ambitions, what I need to cultivate here is a dissatisfaction with a single aspect of my art and laser focus on it.

Regarding the anime style, I've had an idea. Figures.

https://store.crunchyroll.com/collections/figures

It slipped my mind, but I bet I could find some good 3d references for them somewhere.

This is what I've been missing as my drawing target - a complete 3d model. The CSP model is not enough and is just leading me down the wrong track. If I want to learn to draw 2d anime, what I should use as references are figures such as these.

1:45pm. Let me go to bed. I'll step away from the screen for the rest of the day, till about 5-6pm and then watch Birdie Wing and play Genshin Impact after that. Fuck this shit, I can always get a job if I run out of time for real. Until then I should just take it easy and focus on one thing at a time. So what if I can't get to a full pro level so easily, I've already come a decent amount. I am certainly better than when I started.

Maybe tomorrow I'll manage to cultivate enough desire to begin for real."

---
## [dave-tucker/linux](https://github.com/dave-tucker/linux)@[b9364eed92...](https://github.com/dave-tucker/linux/commit/b9364eed9232f3d2a846f68c2307eb25c93cc2d0)
#### Thursday 2022-06-30 11:51:30 by Douglas Anderson

drm/msm/dpu: Move min BW request and full BW disable back to mdss

In commit a670ff578f1f ("drm/msm/dpu: always use mdp device to scale
bandwidth") we fully moved interconnect stuff to the DPU driver. This
had no change for sc7180 but _did_ have an impact for other SoCs. It
made them match the sc7180 scheme.

Unfortunately, the sc7180 scheme seems like it was a bit broken.
Specifically the interconnect needs to be on for more than just the
DPU driver's AXI bus. In the very least it also needs to be on for the
DSI driver's AXI bus. This can be seen fairly easily by doing this on
a ChromeOS sc7180-trogdor class device:

  set_power_policy --ac_screen_dim_delay=5 --ac_screen_off_delay=10
  sleep 10
  cd /sys/bus/platform/devices/ae94000.dsi/power
  echo on > control

When you do that, you'll get a warning splat in the logs about
"gcc_disp_hf_axi_clk status stuck at 'off'".

One could argue that perhaps what I have done above is "illegal" and
that it can't happen naturally in the system because in normal system
usage the DPU is pretty much always on when DSI is on. That being
said:
* In official ChromeOS builds (admittedly a 5.4 kernel with backports)
  we have seen that splat at bootup.
* Even though we don't use "autosuspend" for these components, we
  don't use the "put_sync" variants. Thus plausibly the DSI could stay
  "runtime enabled" past when the DPU is enabled. Techncially we
  shouldn't do that if the DPU's suspend ends up yanking our clock.

Let's change things such that the "bare minimum" request for the
interconnect happens in the mdss driver again. That means that all of
the children can assume that the interconnect is on at the minimum
bandwidth. We'll then let the DPU request the higher amount that it
wants.

It should be noted that this isn't as hacky of a solution as it might
initially appear. Specifically:
* Since MDSS and DPU individually get their own references to the
  interconnect then the framework will actually handle aggregating
  them. The two drivers are _not_ clobbering each other.
* When the Qualcomm interconnect driver aggregates it takes the max of
  all the peaks. Thus having MDSS request a peak, as we're doing here,
  won't actually change the total interconnect bandwidth (it won't be
  added to the request for the DPU). This perhaps explains why the
  "average" requested in MDSS was historically 0 since that one
  _would_ be added in.

NOTE also that in the downstream ChromeOS 5.4 and 5.15 kernels, we're
also seeing some RPMH hangs that are addressed by this fix. These
hangs are showing up in the field and on _some_ devices with enough
stress testing of suspend/resume. Specifically right at suspend time
with a stack crawl that looks like this (from chromeos-5.15 tree):
  rpmh_write_batch+0x19c/0x240
  qcom_icc_bcm_voter_commit+0x210/0x420
  qcom_icc_set+0x28/0x38
  apply_constraints+0x70/0xa4
  icc_set_bw+0x150/0x24c
  dpu_runtime_resume+0x50/0x1c4
  pm_generic_runtime_resume+0x30/0x44
  __genpd_runtime_resume+0x68/0x7c
  genpd_runtime_resume+0x12c/0x20c
  __rpm_callback+0x98/0x138
  rpm_callback+0x30/0x88
  rpm_resume+0x370/0x4a0
  __pm_runtime_resume+0x80/0xb0
  dpu_kms_enable_commit+0x24/0x30
  msm_atomic_commit_tail+0x12c/0x630
  commit_tail+0xac/0x150
  drm_atomic_helper_commit+0x114/0x11c
  drm_atomic_commit+0x68/0x78
  drm_atomic_helper_disable_all+0x158/0x1c8
  drm_atomic_helper_suspend+0xc0/0x1c0
  drm_mode_config_helper_suspend+0x2c/0x60
  msm_pm_prepare+0x2c/0x40
  pm_generic_prepare+0x30/0x44
  genpd_prepare+0x80/0xd0
  device_prepare+0x78/0x17c
  dpm_prepare+0xb0/0x384
  dpm_suspend_start+0x34/0xc0

We don't completely understand all the mechanisms in play, but the
hang seemed to come and go with random factors. It's not terribly
surprising that the hang is gone after this patch since the line of
code that was failing is no longer present in the kernel.

Fixes: a670ff578f1f ("drm/msm/dpu: always use mdp device to scale bandwidth")
Fixes: c33b7c0389e1 ("drm/msm/dpu: add support for clk and bw scaling for display")
Signed-off-by: Douglas Anderson <dianders@chromium.org>
Reviewed-by: Abhinav Kumar <quic_abhinavk@quicinc.com>
Tested-by: Jessica Zhang <quic_jesszhan@quicinc.com> # RB3 (sdm845) and
Reviewed-by: Stephen Boyd <swboyd@chromium.org>
Reviewed-by: Dmitry Baryshkov <dmitry.baryshkov@linaro.org>
Patchwork: https://patchwork.freedesktop.org/patch/487884/
Link: https://lore.kernel.org/r/20220531160059.v2.1.Ie7f6d4bf8cce28131da31a43354727e417cae98d@changeid
Signed-off-by: Abhinav Kumar <quic_abhinavk@quicinc.com>

---
## [sam-devteam/sam-devteam.github.io](https://github.com/sam-devteam/sam-devteam.github.io)@[fbd7fae118...](https://github.com/sam-devteam/sam-devteam.github.io/commit/fbd7fae1184dfdb0541f57b93c7a5d1c2652731e)
#### Thursday 2022-06-30 12:51:16 by Samuel

Merge pull request #3 from fuck-you-rory/patch-2

Update index.html

---
## [sam-devteam/sam-devteam.github.io](https://github.com/sam-devteam/sam-devteam.github.io)@[dee07cd8ae...](https://github.com/sam-devteam/sam-devteam.github.io/commit/dee07cd8aeaae85cef6a2e0e7eae662f70c2a678)
#### Thursday 2022-06-30 12:51:44 by Samuel

Merge pull request #2 from fuck-you-rory/patch-1

Delete index.html

---
## [sam-devteam/sam-devteam.github.io](https://github.com/sam-devteam/sam-devteam.github.io)@[73cdc29705...](https://github.com/sam-devteam/sam-devteam.github.io/commit/73cdc297058c0eb630d432ea3166dc627935ca5f)
#### Thursday 2022-06-30 12:52:21 by fuck-you-rory

Merge pull request #1 from fuck-you-rory/fuck-you-rory-patch-1

Create awesome.cs

---
## [sam-devteam/sam-devteam.github.io](https://github.com/sam-devteam/sam-devteam.github.io)@[6f42d5b0d4...](https://github.com/sam-devteam/sam-devteam.github.io/commit/6f42d5b0d43922db4b96aec33cdbd2323eccb945)
#### Thursday 2022-06-30 12:52:21 by Samuel

Merge pull request #1 from fuck-you-rory/main

Update index.html

---
## [sam-devteam/sam-devteam.github.io](https://github.com/sam-devteam/sam-devteam.github.io)@[7543a892b9...](https://github.com/sam-devteam/sam-devteam.github.io/commit/7543a892b96298b870596986e4a2a97127d4b3ae)
#### Thursday 2022-06-30 12:52:37 by Samuel

Merge pull request #4 from fuck-you-rory/patch-3

Update main.css

---
## [skyline75489/terminal](https://github.com/skyline75489/terminal)@[9ccd6ecd74...](https://github.com/skyline75489/terminal/commit/9ccd6ecd744890b856f3d8a39ff0616c0e34d4fb)
#### Thursday 2022-06-30 13:56:08 by Mike Griese

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
## [cockroachdb/cockroach](https://github.com/cockroachdb/cockroach)@[0a3447944a...](https://github.com/cockroachdb/cockroach/commit/0a3447944ae259b725ebff7d84cecd1b6a1de19c)
#### Thursday 2022-06-30 14:16:37 by craig[bot]

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
## [atlgeek007/ATM-7](https://github.com/atlgeek007/ATM-7)@[8bff1fe476...](https://github.com/atlgeek007/ATM-7/commit/8bff1fe4769e3ecd98814c640bc44640ee6e9f1a)
#### Thursday 2022-06-30 14:53:54 by 90

Add more starting books

Tome now also includes guides/READMEs from Blood Magic, Evilcraft, RFTools, Roots Classic, SecurityCraft, Silent Gear, Spice of Life: Carrot Edition, The One Probe and The Twilight Forest.

---
## [h-vetinari/scipy](https://github.com/h-vetinari/scipy)@[0b53fc4c9c...](https://github.com/h-vetinari/scipy/commit/0b53fc4c9c593ee524a003296da6be83c9d41a28)
#### Thursday 2022-06-30 15:03:39 by Tyler Reddy

MAINT: SCIPY_USE_PROPACK

* this is effectively a forward port and modernization
of the release branch `PROPACK` shims that were added in
gh-15432; in short, `PROPACK` + Windows + some linalg backends
was causing all sorts of trouble, and this has never been resolved

* I've switched to `SCIPY_USE_PROPACK` instead of `USE_PROPACK`
for the opt-in, since this was requested, though the change
between release branches may cause a little confusion (another
release note adjustment to add maybe)

* I think the issues are painful to reproduce; for my part,
I did the following just to check the proper skipping/accounting
of tests:

- `SCIPY_USE_PROPACK=1 python dev.py -j 20 -t scipy/sparse/linalg`
  - `932 passed, 172 skipped, 8 xfailed in 115.57s (0:01:55)`
- `python dev.py -j 20 -t scipy/sparse/linalg`
  - `787 passed, 317 skipped, 8 xfailed in 114.80s (0:01:54)`

* why am I doing this now? well, to be frank the process of manually
backporting this for each release is error-prone, and may cause
additional confusion/debate, which I'd like to avoid. Besides, if it
is broken in `main` we may as well have the shims there as well. I would
point out that you may want to add `SCIPY_USE_PROPACK` to 1 or 2 jobs
in CI? The other reason is that if usage of `PROPACK` spreads, I don't
want to be manually applying more skips/shims on each release (which
I already had to do here with two new tests it seems)

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[ad654e76b4...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/ad654e76b4c5dd3972cd2a07eb2d4f9658965807)
#### Thursday 2022-06-30 15:20:10 by Nerevar

[Modular] Snails & Blushing Fix (again!) (#14604)

* snails fucking again holy shit

* wew

Co-authored-by: Snakebittenn <12636964+Snakebittenn@users.noreply.github.com>

---
## [matthiaskrgr/rust](https://github.com/matthiaskrgr/rust)@[15871b20bc...](https://github.com/matthiaskrgr/rust/commit/15871b20bcc15fad27809d0332a55e4586482289)
#### Thursday 2022-06-30 16:42:52 by Matthias Krüger

Rollup merge of #98717 - RalfJung:make-tidy-less-annoying, r=jyn514

get rid of tidy 'unnecessarily ignored' warnings

I think these warnings are quite pointless: when I say `allow(foo)` in my code, that doesn't necessarily mean that I expect `foo` to happen -- it just means that I am okay with `foo` happening.

For example, having to add and remove `ignore-tidy-linelength` as the longest line in the file keeps growing and shrinking is just annoying and doesn't benefit anyone, IMO. This usually incurs *two* CI roundtrips: first CI tells you that line lengths in your test file are ignored unnecessarily, so you go and remove that attribute; then CI tells you that now your line numbers changed, so you re-bless your tests (often takes >5min if parts of rustc need rebuilding because `./x.py fmt` changed something somewhere). That's just a lot of wasted effort and time and patience.

---
## [chooglen/git](https://github.com/chooglen/git)@[a1323d963f...](https://github.com/chooglen/git/commit/a1323d963f917df661a8701c305d84e781a8f550)
#### Thursday 2022-06-30 17:29:35 by Glen Choo

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

---
## [hypothesis/lms](https://github.com/hypothesis/lms)@[829fbca8fd...](https://github.com/hypothesis/lms/commit/829fbca8fda46bfc59347f8dad976348e055a7ca)
#### Thursday 2022-06-30 18:30:48 by Sean Hammond

Don't run the functests on Jenkins

This is a pain because it apparently requires there to be a separate
`make functests-only` target (is that really necessary?).

But anyway: I don't think there's any benefit to running the functests
on Jenkins after we've already run them on GitHub Actions. It's just
more code to maintain and more waiting around for Jenkins to finish.
The idea originally was that Jenkins runs the tests actually inside the
Docker container so it's more similar to production than GitHub Actions
which doesn't run the tests in Docker. But I don't think there's ever
been a case of the tests passing on GitHub Actions and then Jenkins
catching a problem with its second run of the tests. So in practice I
think this is silly.

I think there are better steps that we could take to control
CI-versus-prod differences if we wanted to do that:

- Use the same OS in production as we use on CI.
  We could change CI to Alpine.
  But I'd recommend changing production to Ubuntu instead then we'd have
  Ubuntu on prod, CI and dev. And people recommend Debian over Alpine
  anyway:
  https://pythonspeed.com/articles/base-image-python-docker-images/

- Install the app into a virtualenv within the production Docker
  container so that it's isolated from the container's OS's Python
  packages

---
## [DoggingBot/poc](https://github.com/DoggingBot/poc)@[daaba203d3...](https://github.com/DoggingBot/poc/commit/daaba203d37feae99c26d9e83f9dbdbc6238a31e)
#### Thursday 2022-06-30 18:33:24 by kmatsumari

Massive refactor to utilize a database

Many functions have been rewritten to accommodate the new methods to work with a database, many functions and variables have been removed due to immediate deprecation, and many new functions, services, event handlers, and command handlers have been added. The code still needs to be documented and properly commented, as well as undergo a full naming rework for variables utilized within the Discord.js API to eliminate confusion on expected data being passed and worked with. Discord.js version is still using API v12 instead of v13 (which contains breaking changes).

Database uses serverID_TableName convention per server that is configured, and all configurations are held in the table 'config'. 'retorts' contains a list of all the snarky responses the bot will use when bothered in DM.
Structures for tankees, sips, invites, invite_uses, and buffers can be found in configCommand.
Structure for retorts is a keyless single column labelled 'line'.
Structure for 'config' is as follows:

  'serverID' VARCHAR(20) NOT NULL PRIMARY KEY,
  'commandPrefix' VARCHAR(1) NOT NULL DEFAULT('.')
  'botMasterRole' VARCHAR(20) NULL DEFAULT(NULL)
  'botUserRole' VARCHAR(20) NULL DEFAULT(NULL)
  'drunktankRole' VARCHAR(20) NULL DEFAULT(NULL)
  'tankChannel' VARCHAR(20) NULL DEFAULT(NULL)
  'logChannel' VARCHAR(20) NULL DEFAULT(NULL)
  'invitesChannel' VARCHAR(20) NULL DEFAULT(NULL)
  'namesChannel' VARCHAR(20) NULL DEFAULT(NULL)
  'modlogChannel' VARCHAR(20) NULL DEFAULT(NULL)
  'bypassGMU' VARCHAR(419) NOT NULL
  'rolesToIgnore' VARCHAR(419) NULL DEFAULT(NULL)
  'rolesICannotTank' VARCHAR(419) NULL DEFAULT(NULL)
  'tankUOM' VARCHAR(7) NOT NULL DEFAULT("hours")
  'tankDuration' SMALLINT(5) UNSIGNED NOT NULL DEFAULT(12)
  'writeMessageToDrunkTank ' TINYINT(1) UNSIGNED NOT NULL DEFAULT(0)
  'warnAuthorizedUsage' TINYINT(1) UNSIGNED NOT NULL DEFAULT(0)
  'startServer' TINYINT(1) UNSIGNED NOT NULL DEFAULT(0)

All Discord Snowflake numbers are strings due to the inability to utilize BigInt() in our bot. All snowflakes when passed as numbers, integers, or any large number datatype, always truncate digits to the right when the value exceeds javascript's MAX_SAFE_INTEGER, which is 2^53-1 (9007199254740991). Because Snowflakes are up to 20 digits and make up a value that can be up to the max unsigned value of a 64-bit integer, we cannot rely on anything other than strings, and we are never able to perform any mathematical operations nor use any mathematical comparisons with snowflakes within our bot.

commandPrefix was decided by Sindrah to currently be limited to a single character, so as to not have issues with overlapping or word usage.

large VarChar sizes were chosen for comma-separated lists of snowflake IDs, and huge sizes (blob types are not required as the max message size of a Level 3 boosted server is 4000 UTF8 characters) for messages buffered.

TinyInt(1) is for boolean values.

ALL occurrences of injectConfig() are now Deprecated and Removed. injection functions, and some other functions/variables, are currently commented out (or may still exist but are not exported any longer) and are to be blown out on next code beautification.

main.js
  set default to use druncord_linux
  moved service instantiation to occur after database connection occurs and all server configuration has been obtained
  implements database callable
  moved config into the global namespace so it can be seen from all includes without injecting it. This allows changes from one service/command/event to be reflected in other later-called services that would otherwise need to be re-injected.
  config is now an Object sorted by server ID with individual and independent server configurations.
  bot now has retorts (stored in database) that it randomly responds with when DM'd out of context (to be reworked where no retort is issued for manual tanking responses in DM by botUsers, or Deprecated altogether if problematic)
  main script now listens to the following new events:
    inviteCreate,
    inviteDelete,
    userUpdate -> fed to memberUpdateEvent for handling. currently only used for tracking username changes, and uses existing code to respond to it the same way it would for a nickname change from a GuildMember object.
  all caught events that ultimately require some kind of configuration in order to move forward will first check if the server configuration not only exists but that every required part of the configuration has been configured, otherwise it responds that the server has not been configured yet, and instructs the user to use the configuration commands.

package.json
  new version "1.0.0" for breaking and major changes, currently in production
  testserver now stacktraces warnings and errors
  testserver_linux contained a colon character that prevented it from being properly read as an index
  new packages were added: mysql2, bluebird (promises)
  nodeVersion added by npm

package-lock.json
  reflects dependencies and changes found in package.json

config/
  druncord_linux.js
  hard-coded configurations for the server have been removed, except for the bot token access code and bot name
  included database connection details pulled from .env (keeps the credentials secret using .gitignore when cloned)

managers/
  dbConnectionManager.js
    new file. handles all database connections, single transaction mode within an async promise, returns results of query.
    utilizes prepared statements with parameterized SQL to prevent SQL injection without having to sanitize any data.
    limited DDL/DML query functions permitted in order to prevent injection by 2nd order (using unions or stored functions).
    all query components are standardized to be handled without allowing any code to manipulate the query string. all query data is built based on the existence of the passed data, and the query string is strictly assembled based on the named properties of the object passed to the querybuilder.

events/
  memberJoinEvent.js
    logs joining users with their account details and the Invite they used to join (and references the invite creator's details)
    tank persistence rewritten due to database usage instead of JSON flatfile.
    if tanked user comes back after time is served, untank procedure is automatically called to untank them.

  memberLeaveEvent.js
    rewritten checktank to still show user in tank after they leave (future update to label the user as not in server so auto-untank happens if/when they return without botUser involvement)
    logs user leaving in special log with user information (ID, user.tag, current mention handle, account age, time in server, and invite used as well as inviter).
    notates if the user was kicked, banned, or left on their own.
    banned users that were tanked have their tank record closed with reason "Banned".

  memberUpdateEvent.js
    now tracks username changes, nickname changes, and tracks all roles given or taken that aren't involving the drunktankRole
    reworked logic for checking if the user being manipulated with drunktankRole was in the tank records before working on a tank record, otherwise outputs message that the user was not in the tank.
    removed the exception catch() that only sent a warning to the console if the audit log entry couldn't be found. Eventually will reinstate when all unhandled promise rejections are explicitly handled.

  inviteEvent.js
    new file. simply determines the data of an invite caught by the event trigger, and determines whether it was newly added or deleted, then adds/updates the record in the DB accordingly.

services/
  drunktankService.js
    refactored the way users are handled in each function and procedure within to accommodate for the DB.
    handles tank command upon a tanked user to just close out their current tank record with reason "Already tanked - retanking" then open a new tanking record for the tanked user.

  guildService.js
    writeToChannel function refactored to consider a message that may be buffered or just lost entirely if the channel is not valid. No longer receives a channel ID, instead receives a channel namespace found in a server's config that is used to get the channel ID by the name as an index.
    buffer message true by default, pass explicit false as third arg to override message buffering.
    getMemberFromCache now returns the entire guildMember object that is fetched
    setRolesForMember() has a fix where an empty string as only role in .roles occurs when they have no roles (by setting it to an empty array), and properly the newly refreshed GuildMember Object or null if the guildMember is not found.
    reworded console log output from getExecutorForRoleChangeFromAuditLog()
    notated API v13 updated method to diconnect a user from voice channel (preemptive).

  persistenceService.js
    massive refactor of saveTanking() and saveUntanking() to make use of a DB, and redesigned the tankee object to not record usernames or nicknames (unnecessary, this data can be obtained via their ID and guildService appropriately, and username/nickname are now logged for posterity)
    saveUserLeaving() and saveUserJoining() functions are now Deprecated and no longer used, as the bot now handles role persistence for the drunktankRole on its own using the database records.
    getTankedUsers() function is used for all instances of obtaining tankee records, and can be have the query filter the results to only currently tanked users or limit the records to a specific user that is currently tanked.
    getTankHistory Deprecated. uses getTankedUsers() without filtering
    getUser() Deprecated. uses getTankedUsers() by filtering and passing a specific userID.
    getUserHistorical() Deprecated. combine getTankedUsers() with filter by userID and guildService.guild.member(id) to determine if the tanked user is still here or not.
    addSip() has been reworked for Database usage. Sips, along with any other allowed string (considered a "sipstring"), are stored in a table by UserID, lastSip, and each further column is named the sipString which holds the integer sipcount for that sipstring.
    addSip() now throttles users from being able to spam a sip command (currently hardcoded to 7000ms compared from their loast recorded sip). Currently the column for lastSip is compared for all sipStrings, so the throttle is applied to the entire sipCommand usage regardless of what string is passed.

  tankStatsService.js
    reworked to make use of Database fetched results, and includes new stats for untankings (Staff that care).
    added function filterTankStats(guild, user) to allow for searching the tank records based on a specific user.
    minor capitalization changes in output message, and altered typed occurrence of "Mod" to "Staff" (to reduce the notion that Barbacks are Mods within Druncord).
    changed the output of staff nicknames to be their mention handles instead. NOTE: if staff get annoyed being tagged by tankstats to the point of needing a change, implement a blank message to be sent first, get that message ID, then edit that message with the built content being sent out so pings don't occur but the tags reflect username/nickname changes.

  inviteService.js
    new file. handles obtaining all current guild invites and the stored invite data from the DB, performs some checks on usage counts, considers the fact that invites may predate the bot's recording of invites, and accounts for that using a dummy counter (number of uses on an invite prior to tracking by the bot). Handles determining which invite was most recently incrememnted by one compared to the previously known counts.
    if an incremented invite cannot be ascertained, and the used invite of a joiner is unknown, all invites in the DB will have their dummy counts fixed to reflect proper counts and uses.
    There are 2 tables containing invite data: one for the invite itself (contains invite code, inviter user ID, tracked uses, dummy count, and whether the invite has been deleted), the other table has a list of invite uses (arranged by joindatetime, code, and userID).

  bufferService.js
    new file. averts errors of invalid channel, and prevents loss of the output log messages, by saving message content for a log channel when that channel doesn't actually exist (deleted channel). When the server config has a valid channel for a particular log group, all saved messages are sent to the valid log channel, and the records are purged from the buffers table in the DB.

  syncTankService.js
    Deprecated, and unchanged. may be repurposed for auto-untanking after time served.

commands/
  checkTankCommand.js
    refactored to handle the data organized from the database records. data gets organized a little different now to make searching and iterating through it all a bit faster and easier. for data structure, see persistenceService.getTankedUsers().
    due to explicit handling of what userID is used when a tanking botUser doesn't exist, which should be impossible anyway, the conditional check of obj.tanked_by == "Unknown" will never be true, so the output of the bot "learning" about an unknown tankee won't ever happen. consider removing it or move it to a promise rejection handler.

  commandParser.js
    updated countedStrings to reference only the columns in the sips table (except userID and lastSip). This effectively configures a server's sipStrings allowed by simply tracking them.
    There is currently no handler or command to add, update, or remove a sipString - needs to be handled in the DB manually by altering the table structure itself. Might eventually implement botMasterRole to be allowed to use such a command.
    considering Deprecating the catch of mistakes (double prefix, prefix + space, prefix + p) as we simply don't handle anything that isn't a case of command.
    reworked the test of whether a user has the right to use the bot based on botUserRole, botMasterRole, or if they have the Administrator privilege.
    added case for "config" command.
    case "syncTank" Deprecated and removed (commented). Considering repurpose of command to be an automated process to untank users that have served their time (triggered on every handled event).
    no longer need to inject config to anything, now deprectaed and removed (commented).
    wrote an explicit check whereby an unconfigured server doesn't respond to commands at all, unless the command is specifically ".configure" (default prefix with "configure", not "config") and it is used by a user that has Administrator. This configure command only works whilst the server has not fully been configured, and assists in setting up the default configs and walks the admin through the process of getting the server ready.

  helpCommand.js
    used another variable to short reference the server configured command prefix for cleaner and shorter code.
    added help entry for "config" command.
    "synctank" command Deprecated and removed (commented out).

  sipCommand.js
    implemented sipCommand use throttling (hard-coded wait time set in persistenceService.addSip())
    hard-coded responses when sip is throttled.
    refactored existing responses for sips to reference the string that triggered the command (in case other words are allowed) NOTE: due to how the English language is, it may be beneficial to include a table of the sip strings with their permutations of past-tense/plural/present-tense-ing/etc so the proper references don't have to be hard-coded with a ton of regex cases that try to figure out how to properly spell the word (such as trying to figure out how not to mispell sipping and farting, etc.).
    added an ego-boosting message that gets triggered when Sindrah triggers the sipCommand, but the command only responds as though the string is "sip". NOTE: Sindrah has never had sip counts, and doesn't care to, but decided to make this message just in case anyone ever asked him what his sip count is, and decided it would be better and funnier instead of abusing DB access and setting his own sipcount to some godawful number. Stevie_pricks had a sipcount and still uses the command, so no ego-boosting message was implemented (yet).
    sip command is ignored if sent in the tankChannel of the server. By logic flow, Sindrah's personal ego boosting message response can be performed in the tank channel (can be moved under the tankChannel check if it bugs anyone).

  sipStatsCommand.js
    refactored for structure and data coming from the database.
    output shows Display name in server with user tag in parentheses and their count (recently hotfixed from using @mention handlers in order to close a flaw whereby a user could spam tag the top 5).

  tankCommand.js
    moved the variables that fetch a member object for tankee, author, and the drunktankRole, to occur after we validate the arguments are correct in count. nothing bad really happens the original way, but there is no reason to continue if the command is invalid.

  tankStatsCommand.js
    command handle now accepts a second argument to be a user mention handle or a user ID (checked in that order). If a valid user is passed, will pass the user ID obtained from the command to filter the tankstats records by that user as the tanker or the tankee, otherwise just performs normal tankstats with the new untank data.

  untankCommand.js
    altered how we check for valid token length (now checks if first array element of tokens is an empty string -- failing to provide anything after the command results in a single element array that contains an empty string, which will pass as true in the previous method).
    wrote a check for when the user mention cannot be utilized due to the user leaving before the untnak command gets run (the user mention fails because the handle now contains a bang character after the @ sign, and message.mentions.users only contains users that are still in the guild).
    If the check determines the user is gone, we also need to bypass the function validateMentions() because there won't be a valid mention in the command. Instead, their ID number is sifted by stripping the opening and closing bracket characters for the mention handle in the message (that contains a "!").
    Modify untank message to not show as much detail as normal. Single line saying "author.mention untanked tankee.user.tag (ID), but they aren't in the server anymore.", then close out their tank record with reason "Time served - Cleanup user not in server".
    removed output mention of running synctank command (command Deprecated).

  configCommand.js
    new file. handles all aspects of .configure (unconfigured server and run by Admin) and .config (configured and running server and executed by botMasterRole or Admin).
    allows altering of server configuration without having to stop/restart the bot.
    using .config(ure) help produces the current server configuration and its available command options
    Each command option has its own help output for usage and guidance.
    configuring a server generates unique tables for recording all data by this bot.
    allows explicit reloading of server configuration for the server the command is executed on.

  syncTankCommand.js
    Deprecated, and unchanged. may be repurposed for auto-untanking after time served.

helpers/
  helpers.js
    added fisherYates() shuffle algorithm
    updated validateMentions to properly respond generically instead of explicitly assuming the command used was "tank", and properly includes whether a reason is required or optional (based on command used).
    changed the the term "@'d" to "@mentioned"
    doesUserHaveRole() Deprecated and removed (no longer in file). This function is highly unnecessary due to the passing of the very object that can be checked inline using .includes() with less characters than it takes to call this function.
    getAtString Deprecated and removed (commented out). Another function that takes more characters to call than just doing it inline and provides no logical checking.
    updated algorithm for removeRoleFRomArray to use the .forEach() method instead of a plain for loop, and we return the roleArray after whatever is done, if anything. Empty array is returned if we get undefined at the start, which happens when there are no roles.
    added convertDataFromDB() function to normalize the data types coming from the database and implicitly set default values if anything is invalid.
    NOTE: Need to double check for any more functions that are not called or used anymore that were not specifically mentioned as being Deprecated, and identify functions that are written with a narrow usage for a single service/command/event and move them to that file; no reason to have a single-purpose function get bumped around.

  messages.js
    altered confirm_message to confirm_tank_message
    all functions referencing a user's name in any way now have the user/guildmember object itself, and make use of a user mention or their in server Display Name and include tag and ID.
    confirmation messages don't tag the botUser, they use guildMember.displayName.
    Tanked/Untanked messages in the log channel mention both the tanker and tankee, and now include user.tag and user.id of the botUser for posterity (staff changed their names frequently, and on odd occaisions, lots of staff set their name to the same name for a fun time, this would have been utter chaos if everyone had the same name at the time).
    log_blue_untank_msg now implements untank reason (default "Assumed Time Served" set by function calling this function).
    tank_msg now @mentions the tanked user
    added user_leave_msg, user_join_msg, user_name_change, and log_role_change to handle special logging of user information when they leave, join, change their name, or a role is granted/removed outside of tanking/untanking.

  logger.js
    no changes.

  KNOWN ISSUES
  .configure command on an unconfigured server did not work to initially configure a server (had to manually create the tables and manually insert the server configuration due to a hasty bot swapover). The entire command did work in testing when hosted on a PC using GIT-CLI, but failed miserably when hosted on the production linux server. Requires further testing with another discord server and debugging.

  many events are being fired twice (and subsequently caught twice), or are being retriggered after getting handled (such as Tank/Untank messages being sent twice, one for the botUser as the tanker, the second as TankCommander being the Tanker, or users joining/leaving are generating duplicate join/leave logs). This is benign and does not affect the recorded data of the occurrences, but it can be annoying to have double logs for each action that may contain mention handles, plus it may just serve to clog up the log channels. Need to look into why a second triggering occurs and come up with a way to identify duplicate triggered events and just drop them.

  tankStats was designed to allow for searching tank records by a specific user and would show stats for that user (such as how many times they were tanked, what staff members tanked them, etc) and if that user was staff it would show all users they tanked and provide stats based on that. Probably something silly and simple, but specific tankstats are not working.

  checktank will display users that are still serving time but have left or been banned (except when a ban is issued with a tanked user still in server, their record gets closed as part of the catch). Users that were kicked or left are intentionally displayed at this time to show who is still serving time, in case they return, but banned users that already left don't get picked up (not a bug, it's due to how we handle and catch bans by comparing the banlist after a user leaves rather than listening for a GuildBanAdd event - which was not working during testing so that emthod was abandoned). The best idea to combat this shortcoming so botUsers don't have to manually .untank banned users stuck in the tank is to implement an auto-untank procedure on all time-served records, which also makes botUser's work less involved by not having to untank people that serve their time.

  invites are not getting properly handled when it involves the vanity URL. This could not be tested due to lacking boost level 3 on a test server - this will be difficult to test without having to restart the bot on every change/attempt. If we are to truly test this, either we need to boost a test server, find a way to have our services/commands reloaded on each event trigger so the bot doesn't have to be restarted after a testing change, or we will need to test it using another bot in the boosted server.

  bufferService has not been tested in the production server environment, just the testing environment (worked well, but considering some things worked in testing and failed completely in production, this needs attention).

  ClientService has not been implemented yet (not certain what it was supposed to be for, but my best guess is moving all the client.on() listeners from main.js to its own service).

  There are tons of occurrences that result in Promise Rejections, which are being deprecated and will result in terminating our node.js process (fully blow up the bot and require a manual restart). Top Priority is to write explicit promise rejection handlers and exception handlers for EVERYTHING before this change occurs.

  If there is anything I forgot or failed to discover thus far, I'll open a ticket on it.

---
## [blakestanger/Writing-Projects](https://github.com/blakestanger/Writing-Projects)@[47ea6e6427...](https://github.com/blakestanger/Writing-Projects/commit/47ea6e6427f49be55a8586c734bf9c6d23e8321d)
#### Thursday 2022-06-30 18:55:57 by blakestanger

Deveon? What the fuck is marin's boyfriends name? Anyway the part where she shows up wiht the chocolate cake and gets fuuuuuuuuuuucked.

---
## [interactions-py/autosharder](https://github.com/interactions-py/autosharder)@[d0a7232a2d...](https://github.com/interactions-py/autosharder/commit/d0a7232a2dea87ad8df3827b3c5a9b7803047dc8)
#### Thursday 2022-06-30 19:04:33 by EdVraz

fuck you <@709135116819103865> for making me do this it is hell

---
## [yuzefovich/cockroach](https://github.com/yuzefovich/cockroach)@[e37a2dd31a...](https://github.com/yuzefovich/cockroach/commit/e37a2dd31a85624a5f30293901b3b3e2d6c559b4)
#### Thursday 2022-06-30 19:07:06 by Yahor Yuzefovich

sql: make sure to close the reserved account for each session

I speculate that previously it was possible for the "reserved" memory
account for each new connection to "leak" memory from the memory
accounting system, and now this has been fixed by ensuring that this
account is closed when the connection is.

The idea with this "reserved" account is that when a new connection
is being spun up, we allocate 21KiB (with default values for some
things) upfront from the "conn" monitor. Later, this "reserved"
account is used as a pool for other monitors created on behalf of
the connection (e.g. "session" and "session root"). When those monitors
get `Stop`ped, then the reserved memory account is cleared which in
theory should return all allocations from "reserved" back to the ""
monitor.

However, during `BoundAccount.Clear` in `BytesMonitor.adjustBudget` we
might choose to not shrink the "conn" monitor's budget leading to a leak
in order to allow some "margin" between "allocated" and "reserved".

To be honest, my understanding is that the leak should be limited by
100KiB for a single "conn", and we should have a single "conn" monitor
in a node, so I cannot explain how this would lead to leaks on the order
of MBs. Still, this commit makes things more clear and intuitive, so
I think it makes sense to proceed.

Release note: None

---
## [ULTRA-HOI/HOI4-ULTRA-Project](https://github.com/ULTRA-HOI/HOI4-ULTRA-Project)@[31b5b6cb9b...](https://github.com/ULTRA-HOI/HOI4-ULTRA-Project/commit/31b5b6cb9bb628e42f0b9e88665228d5b6b5c0c0)
#### Thursday 2022-06-30 19:37:55 by T3rm1dor

Big changes to soviet NF tree

- Removed Cg modifiers in five year plans but made PE gives +5 cg more so initially there is no change. The other cg changes is remove the extra 5 on third year plan but to compensate we will achieve a higher yield is 2% cg reduction and no cg bonus from the collectivization effort. This is probably a sligth buff, but considering the propaganda campaing run for 2 years and that the current +5cg debuff from 3rd year plan can be consider a noob trap as you are only making mils so I'll say it is an improvement.
- On the air tree, I have make most focus that improve red airforce 5 weeks instead of three. Also, I've added an extra -10% efficiency to red airforce but made intensify air pilot training give 10% efficiency while giving less bonuses and not beibg exclusive of intensify aircraft production, with both this focus and the modern air war taking 49 days and can't be taken beforre barb . So now while at war it takes 3 months to fix air mission efficiency, which isn't that much of an issue but should compete a bit with army buffs. It isn't that big of a nerf, but it should make getting those green airs a bit harder to get early on.
- Army changes is making penal battalions improve MP recovery rate like an extra tech and make for the motherland spirit require order 227, which is now moved to desperate measures.
- Red fleet initial focuses are cheaper do getting the initial dockyard decision is more viable.
- Focuses under collectivist science now take 35 days again
- Molotov and Stalin line no longer mutually exclusive but each take 35 days. Molotov line isn't that great to begin with but if a player considers that the opportunity cost is worth it they should go for it.
- On ideas: Soviet land shock recovered the attack debuff
- Propaganda military buffs have overall be nerfed. Metal campaing now gives 4 extra steel and 4 extra aluminium bc the campaing was useless before. The partisan campaing no longer stop enemy strategic redeployment but instead give better combat bonuses.

---
## [Perkedel/Kaded-fnf-mods](https://github.com/Perkedel/Kaded-fnf-mods)@[fc4f275bbe...](https://github.com/Perkedel/Kaded-fnf-mods/commit/fc4f275bbeb7d26ed33cb8ad3d171b41dab761a7)
#### Thursday 2022-06-30 19:50:29 by Joel Robert Justiawan

[skip ci] tokan

proposed assignable death sounds, witness death, and rise up again.

man, progress is slowing down. We've had alot of issues in here. we got bunch of unluckiness stretching from last month 30, diagonally streaking right upon. that week was sunday (RIP Kimchi), next monday (RIP my young sister's amazing arts & project files, ransomwared because she was desperate finding cracked Zbrush), next tuesday (I think this was the one?), next wednesday, so on and so forth until uh it goes saturday and believe it or not.,.. idk. nothing yet, **it's uncertain**.

So, since the release is long, we should consider to anytime roll the release. How do we tell this? What I know, edit description on all mod pages possible, tell how to join this rolling release, and uh.. umm yeah.

makepkg all the way up!

oops! the capital letter, almost leaked Gamejolt secret API. luckily .gitignore is cap agnostic. But we had both filled `GJKeys.hx` which already ignored long, and this newly empty template `GJkeys.hx` notice the `k` is small letter.

Why scary? This repo right now is in Windows NTFS, where usually Capital differentiation is disabled by default. IT PECKING HAPPENED ON THIS NTFS!! If Windows saw this while this entire repo folder hadn't set the special cap differentiation parameter on, it could explode entire file system. No good!!! We're not in Linux file system where cap differentiation is built in.

Right so, we fixed it. just remove the empty GameJolt keys, leave the filled one if you had. yeas.

Folks, we have bad news. My mom going to receive Bonus yey good news! but the bad news affromentioned, is that the Bonus is paltry. WAY TOO PALTRY. coz already salaried higher and whatever manouver due to pandemic. It's only IDR 20 Million. DAMN IT!!! MY PC BUDGET REQUIRES MORE THAN THAT!!! What do we get for me & my sister shared 20 Million? Balancingly, we'll have an enhanced potato PC, STILL TOO LAGGY, NOT APPROPRIATE FOR ANYTHING GAMING OR EVEN CREATOR ART!!! Not to mention, that's not even gonna cut the motherboard, because I want the best motherboard, it costs 15 20 million ish. I don't want to stay in the older version, Agustus around already have AM5 Ryzen came out likely. AH C'MON!!! DON'T EVER TELL ME TO FIND MONEY!!! I HAVE NO IDEA AT ALL HOW!!! MY ODYSEE MONETIZATION IS CONSIDERABLY DEDD THANCC TO BAS8888 SEC!!! Download Tebenge on Google Play for $0 Right now!!! donate https://cointr.ee/joelwindows7 !!!!

video cutscener disablement message toast to tell if there should've been video but unrealized you disabled it.

gross count net

I tried to bring it somewhere close

Hyundai IONIQ 6 revealed. Basically it's Model S. yep, Sedan. also the steering wheel has LED on the H morse wow!!!

coincidentally, this Little Nightmare protagonist is called `six`. idk help. OH WAIT!!!

maybe we that's the way we divert the brand towards? no, not too fast. I am not fan of sedan. slow down! we must think the fate of Little Nightmare fanfic things here. Should we continue or not?

speaking of Little Nightmare & Six, I think we should move all our modules as bunch of addons instead, each serves 1 purpose. You know, UNIX philosophy. Almalgamating features into 1 app is kinda heavy. idk. just... help!

we should yoink this guy! https://gamebanana.com/mods/384783 https://github.com/BoloVEVO/Kade-Engine-Public he got effects, like... osu game modifier kinda stuff, you know. go check it out!

boffer

---
## [DonatoHorn/glossary](https://github.com/DonatoHorn/glossary)@[bd2fef677f...](https://github.com/DonatoHorn/glossary/commit/bd2fef677f42e5234fca9e13c288f30766890fb9)
#### Thursday 2022-06-30 19:58:22 by DonatoHorn

Update _index.md

In my opinion, in the line 128,  makes more sense, to use *tiver* instead of  `tive` like i have sugested first, but no problem. 
---
 Se *tive* alguma dúvida, entre em contato no canal
---
Sorry for the trouble, i'm a newbie.

---
## [UdjinM6/dash](https://github.com/UdjinM6/dash)@[67ceda1b5a...](https://github.com/UdjinM6/dash/commit/67ceda1b5aa0c51f1fdce4fb71ccba1922e880f6)
#### Thursday 2022-06-30 20:08:47 by fanquake

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
## [Capsandi/tgstation](https://github.com/Capsandi/tgstation)@[763a10d1cc...](https://github.com/Capsandi/tgstation/commit/763a10d1cc44c91720101d422d8709ad1aa0644d)
#### Thursday 2022-06-30 20:11:26 by distributivgesetz

Resonance cascade polishening, bugfixes and better logging (#67488)

This PR rewrites almost all messages related to cascade events. Some messages felt kinda clunky to read or could have been written better. Overall, the new messages add to the experience as a cascade being a terrifying event in a way that I felt the old ones missed, and they make the event feel overall a lot sharper.

While looking at the resonance cascade code, I noticed that there a lot of stuff about cascades in the air which was not touched on. So, as I do, this PR evolved into a polish and roundup PR for cascades. There was a lot of stuff still hanging out relating to the event, and although the big backend of it sits, there was still a bit left to be completed. Therefore this PR deserves more the title of the "Resonance cascade POLISHENING" instead of the "REFLAVAHRING". But yeah, you ever go on a massive tangent before?

---
## [jascoproducts/firmware](https://github.com/jascoproducts/firmware)@[d0a66b113c...](https://github.com/jascoproducts/firmware/commit/d0a66b113cdcf3d9e8ef3d0dc9d9a80cdc3e9625)
#### Thursday 2022-06-30 20:18:24 by jascoproducts

Thursday mini-update

Due to the holiday weekend, we will not be issuing our usual Friday major update this week.

What was originally hoped to be tomorrow's major update should come to be our final batch of firmware uploaded by end-of-week next week. In the meantime, we are discussing what the future of this repository will look like since we have continued to enjoy this community-facing experience.

Enjoy this mini-update, however, if you are a user of:
	- Enbrighten-GE
		- ZW3004\14296 - In-Wall Smart Toggle Dimmer (Lt. Alm)

Other fixes:

2. Documented the existence of pre-6.51.06 SDK-developed firmware releases for some of our Jasco-branded products

3. Updated several readmes and repackaged into new .zip archives

---
## [buyrs/metabase](https://github.com/buyrs/metabase)@[9c4e73899e...](https://github.com/buyrs/metabase/commit/9c4e73899e8914fd41e85987d4a652a9b6058d8a)
#### Thursday 2022-06-30 22:14:46 by dpsutton

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
## [TheonlyIcebear/Bloxflip-Smart-Bet](https://github.com/TheonlyIcebear/Bloxflip-Smart-Bet)@[cbb0088e0e...](https://github.com/TheonlyIcebear/Bloxflip-Smart-Bet/commit/cbb0088e0e161ac126e33f81279a40c41a1c7163)
#### Thursday 2022-06-30 23:34:43 by WaterBongo

reverted all my damn changes icebear stop being a fucking retard get your shit toeghter

---

