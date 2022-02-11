## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-02-10](docs/good-messages/2022/2022-02-10.md)


1,496,238 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,496,238 were push events containing 2,332,730 commit messages that amount to 179,021,811 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 38 messages:


## [kaka-jpn/tgstation](https://github.com/kaka-jpn/tgstation)@[7bead07444...](https://github.com/kaka-jpn/tgstation/commit/7bead0744491b9beb91689d34ac12d142aca5b31)
#### Thursday 2022-02-10 00:32:06 by John Willard

General pAI code improvements (#63688)

Fikou said they would've made MODsuits be controllable by pAI's rather than AI's, if pAI code wasn't as bad.

But pAI code ISN'T AS BAD AS AI CODE LIKE HOLY SHIT WHAT THE FUCK MAN???

Anyways, this is just general code improvements for pAIs that I thought would be nice to have.

Documents previously undocumented vars
Moves loose vars to be where they should be
Removes single-letter variables
Makes pAI a defined job
Moves vars around to where they should be while removing unused ones.
Makes pAI abilities its own .dm file
Replaces var/silent with Stun() (like cyborgs)
Reworks pAI's doorjack to not have a ton of procs, copy paste, and a reliance on Life(), instead it just uses a do_after()
Moves screwdrivering radios from attackby to screwdriver_act

Just general code improvement for Silicon, the thing no one likes or wants to touch.

---
## [Monkestation/MonkeStation](https://github.com/Monkestation/MonkeStation)@[040b7ff839...](https://github.com/Monkestation/MonkeStation/commit/040b7ff839d51d4db2ce1747f92312e0925bccd2)
#### Thursday 2022-02-10 00:35:28 by Zonespace

Adds Flavor Text (#48)

* lgtm

* aaaAAAA

* might be better idk

* flavor-examine

* info

* haaa fuck you github

---
## [adacovsk/vgstation13](https://github.com/adacovsk/vgstation13)@[b879dddba0...](https://github.com/adacovsk/vgstation13/commit/b879dddba0f6a2afcf72a77f4696f3e9c031ecb5)
#### Thursday 2022-02-10 00:45:58 by rob

adds sound effects to surgery steps (#31850)

* the everything

* nmb

* ok

* dfdffdfsds

* ssssssssssssssssssssskurfusr

* fuck yoiu damian fuck you!!!!!

* DAMIANNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN

* D

---
## [facebook/hhvm](https://github.com/facebook/hhvm)@[2cfb1bcbf2...](https://github.com/facebook/hhvm/commit/2cfb1bcbf20c3a00bdef5bc0402d3b1773eea4b9)
#### Thursday 2022-02-10 01:01:25 by Lucian Wischik

I think we don't need commit_batch

Summary:
These are the ONLY PLACES in the entire codebase that use "commit/revert on the stack of local changes" in SharedMem.ml. I find that a hard-to-understand mechanism, and I believe this use of the mechanism isn't needed, so I think we can get rid of it...

I believe the significance of these lines is that we've decided not to use the "batch" mechanism at all.

Let's spell it out. Prior to this diff, if "stop_at_errors" was true, then if there were parse-errors in any IDE files then we'd refrain from committing those errorfull versions into Ast_provider or Fixme_provider. Moreover, if there were parse-errors in any files disk or IDE, then we'd refrain from committing those changes into File_provider.

The intent of this was that even if there were parse errors, well, the various heaps would still have "known good previous versions" in them. Kasper spelled out a motivation in D3854040 (https://github.com/facebook/hhvm/commit/4d6bb20991d334033961d764b8edff976f87fa9d): "
We don't want mid-typing parse error to trigger invalidation of large swaths of dependent declarations. To achieve this, for IDE files we don't update parse trees if they had errors (so there will be no change to declarations)."

I assume he specifically meant that if we kept the last-known-good Ast around, then even while there's a parse error in a decl, we'd end up decl-diffing against the last-known-good Ast and therefore wouldn't find any decl-diffs and therefore wouldn't compute any big fanout.

(Is that really true? I wonder what happens to fanout calculation now when you're in the IDE and you typed a character which invalidates a declaration? Does it do decl-diffing and find that the declaration has changed? Does it calculate a big fanout? What stops it from checking that big fanout? -- jakebailey says that with shallow fanout we no longer do phase 2. So what happens to fanout in this case must be controlled by the logic in ServerTypeCheck.LazyCheck.)

Anyway, after this diff, all that goes out the window. Let's spell out what happens now:

(1) Line 290 pushes the stack for Files, Asts, Fixmes:
```
  if stop_at_errors then (
    File_provider.local_changes_push_sharedmem_stack ();
    Ast_provider.local_changes_push_sharedmem_stack ();
    Fixme_provider.local_changes_push_sharedmem_stack ()
  );
```

(2) Line 340 commits those stacks for all changes to ide and disk files. (Ide and disk files are just a split/partition of "to_check".) The only thing we don't commit is `File_provider.commit_batch disk_files.`. NOTE: the only changes we ever expect to see in File, Ast and Fixme are those that came from ide/disk files!
```
  if stop_at_errors then (
    File_provider.local_changes_commit_batch ide_files;
    Ast_provider.local_changes_commit_batch ide_files;
    Fixme_provider.local_changes_commit_batch ide_files;
    Ast_provider.local_changes_commit_batch disk_files;
    Fixme_provider.local_changes_commit_batch disk_files;
```

(3) Line 347 removes the stack:
```
... if stop_at_errors then ( ...
	    File_provider.local_changes_pop_sharedmem_stack ();
    Ast_provider.local_changes_pop_sharedmem_stack ();
    Fixme_provider.local_changes_pop_sharedmem_stack ();
```

If we're creating a stack, and then committing every single change in our stack, and then abandoning the stack -- then there was no point even having a stack in the first place.

NOTE... The one wildcard here is about File_provider. We're deliberately not keeping any disk_files that we rechecked in the File_provider. I assume this is either to save space, or because of an oversight when it was first introduced. But in any case, it should all be immaterial, since the File_heap is going away.

Differential Revision: D33543406

fbshipit-source-id: fc554e0ffeda49c2fc9750c890a0d48981cf1503

---
## [Koi-3088/ForkBot.NET](https://github.com/Koi-3088/ForkBot.NET)@[efb3c38855...](https://github.com/Koi-3088/ForkBot.NET/commit/efb3c3885532a8a0c6defb294adc1c5ef21a16c6)
#### Thursday 2022-02-10 01:20:30 by Koi

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
## [chevyboys/Mizuchi](https://github.com/chevyboys/Mizuchi)@[125857e935...](https://github.com/chevyboys/Mizuchi/commit/125857e935210ac6c058cd8e529322ec62502358)
#### Thursday 2022-02-10 02:01:19 by mayorsporky42

More memes added from Discord

Memes added: Jin slider, Keras Selyrian is right behind you, Keras Ancestry Test, baby; sword for scale, Internal Tengine error, corin blood stealer, Styles of Keras, Cockatrice lies, book titles, ishy angel devil, patrick lightning is a weapon, Keras dual sword body pillow, keras mask, AA I'd die for you, AA children yelling mcdonalds, can I copy your homework AA, AA distinguished gay, airfryer keras, Kerek Shrelyrian, Keras impaled, baby sword sword baby for scale

---
## [san7890/bruhstation](https://github.com/san7890/bruhstation)@[906fb0682b...](https://github.com/san7890/bruhstation/commit/906fb0682bab6a0975b45036001c54f021f58ae7)
#### Thursday 2022-02-10 02:20:00 by necromanceranne

Ballistic to Energy: Autorifles for Thermal Pistols; Adds .38 Crate to Cargo (#64280)

About The Pull Request
The design doc behind this PR, which is only mildy been deviated from on some of the end particulars. Cobby-Approved! Maintainer Discussed!
https://hackmd.io/@6DbtsAKCTtW_9MByKFjZqg/r1xYKCNOt

Cargo Changes
Cargo has had all WT-550's removed and replaced with Thermal Pistols.
Cargo can now order Thermal Pistols, a kind of energy/ballistic hybrid weapon shooting chunks of altered nanites into people. We couldn't use them in people, so maybe we'll use them as bullets! Magma/Ice bullets, to be exact.
You can, after paying a whopping 4K on a goodie pack (you have to pay from your own personal account) buy a .38 revolver. This is mostly to help some poor detective who lost their revolve in what I'm sure will be an inevitable scramble for ballistics. If even the 4K pricetag isn't enough, at least it requires detective access to open the pack...I hope.
Some of the crates that contained autorifle related items have been changed/removed.

unknown (2)

securarevolver 4 0

Science Changes
Ballistic Weaponry node no longer exists, and has been replaced with Exotic Ammo as both the pre-requisite to other nodes, as well as being able to be researched as soon as the Weaponry node is unlocked and not Advanced Weaponry.

Thermal Pistols
-Fairly average bullet statistics; 10 AP but shooting into Energy armor. 20 damage (Brute for cryo, Burn for inferno). Decent wounding potential, but individually much lower ammo counts than lasers.
-Bought in twinned pairs in a two gun holster (just for normal sized energy guns). They're normal sized.
-Each gun has 8 shots (thereabouts). 16 between two.
-Cryo pistols do a knockdown and extra damage against extremely hot targets. Inferno pistols do an explosion cantered on the target against extremely cold targets.
-The guns are EMP-proof.

Why It's Good For The Game
The current gameplay loop of crew combatants is them relying on backup and retreating as necessary to reload their weapons during fights. The ability to repeatedly harry opponents in the field reloads is something that should be moved away from for crew equipment, as it emphasizes lone wolf tactics and one-man army problems, with boxes full of spare ammo usually allowing any single combatant to outlast multiple foes. In addition, ballistics often are not subject to the same (interesting) limitations of energy weapons, so they're typically a no-brainer choice. We shouldn't have such an easy choice be readily available like that.

The thermal pistols present a more challenging weapon to use as a solo combatant but become far more versatile and potent when paired with a decent buddy and basic level co-ordination. They're not a straightforward choice for every situation, but instead are a weapon employed given the right circumstances for them to shine.

In addition to the gameplay issues that ballistics pose, we're in a goddamn spacegame. Unless the ballistics are noticeably weird (they're not), we should expect that our more advanced research station has some pretty odd guns of the energy variety.

Changelog
🆑 Necromanceranne, quin
add: Adds the Inferno and Cryo Pistols. A hybrid energy/ballistic weapon, to cargo. It can be purchased in either a goodies pack or a normal crate order.
add: Thermal Pistols do more damage and a special based on temperature of the target hit.
add: Inferno pistols cause an explosion when they hit a severely cold target.
add: Cryo pistols cause a knockdown and extra damage if they hit a severely hot target.
add: There is a special nanite pistol, which is admin spawned. Don't tell anyone about the forbidden ballistic energy gun.
add: You can order a .38 revolver as a goodie pack. It is expensive.
del: Removes WT-550's from cargo and related content from the techweb/protolathes.
balance: Exotic Ammo is now much earlier in the tech web to take the place of Ballistic Weaponry.
/🆑

---
## [Sea-of-Lost-Souls/Tannhauser-Gate](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate)@[da30e9df00...](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate/commit/da30e9df0084a82e0f32df493d11ccaae7ad2aca)
#### Thursday 2022-02-10 02:37:27 by SkyratBot

[MIRROR] Should fix shuttles leaving without sections [MDB IGNORE] (#11407)

* Should fix shuttles leaving without sections(#64764)

Should(tm)

This was a suggestion by @ Mothblocks and it seemed easy to implement

Fixes #64546 (Icebox evac will sometimes leave without sections)
Fixes #64653 (You might have fixed the kilo whiteship by making it move, but you didn't fix all of it)

Uh people won't just randomly get yeeted into space with half of a shuttle.
Kinda funny for people watching but not if you die of pressure loss or get stuck on the station
Runtime man bad

(Sleeping in here in general is like admitting that we're ok with missing a few atoms, which is what this runtime is. S just missing is better then overtime. Supposedly --Lemon)

* Should fix shuttles leaving without sections

Co-authored-by: Jeremiah <42397676+jlsnow301@users.noreply.github.com>

---
## [matrigato/dwm](https://github.com/matrigato/dwm)@[67d76bdc68...](https://github.com/matrigato/dwm/commit/67d76bdc68102df976177de351f65329d8683064)
#### Thursday 2022-02-10 04:36:27 by Chris Down

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
## [Monkestation/MonkeStation](https://github.com/Monkestation/MonkeStation)@[bf30299f16...](https://github.com/Monkestation/MonkeStation/commit/bf30299f165d9a4ffcc0e14308484b675307dec0)
#### Thursday 2022-02-10 04:52:45 by nednaZ

Florida Man Antagonist (#54)

* Florida Man Antagonist Definition

Adds the Florida Man antagonist, the event to spawn them in and a define file with possible objectives.

Sometimes it ain't so bad
Sometimes it ain't so good
I takes it all in stride
'Cause my livin's in the woods
Ain't got much crime or violence
An' we never had no drugs
But the moon comes through the pines
In mason jars and gallon jugs.

* Objective, Ability, Spawnpoints

Florida Man's objective generation has been expanded and improved, he has been given a WIP ability to bust down doors and has four different methods of arriving to the station.

Florida Cracker cows are one of the oldest and rarest breeds of cattle in United States.
Descended from Spanish stock imported to the continent in the 16th century, Florida Cracker cows are a small, horned breed that quickly adapted to the Florida landscape and have long been prized for their resistance to parasites and other hardy traits.
They weigh generally under 900 pounds (400 kg), come in many colors, and both males and females are horned.
They can be dappled-grey/blue, dappled-brown, solid brown, solid white, white with black spots, white with brown spots, all black, or in some cases, a pure golden palomino. They tend to be more docile and easier to manage by humans, making them a popular choice for cattle roping competitions and for recreational cow-raising activities, such as 4-H.

* Yes, I somehow did that.

Always run your code through an environment check before committing, kids.

* Entry Methods & Outfits

Gives Florida Man four ways to enter the map, ventcrawling, outfits they can spawn in, and generally cleans up some text.

The Floridian peninsula is a porous plateau of karst limestone sitting atop bedrock known as the Florida Platform. The emergent portion of the platform was created during the Eocene to Oligocene as the Gulf Trough filled with silts, clays, and sands. Flora and fauna began appearing during the Miocene. No land animals were present in Florida prior to the Miocene.

The largest deposits of rock phosphate in the United States are found in Florida. Most of this is in Bone Valley.

* Sounds, Icons & Modularization

Splits off each part of the update into it's own files, gives proper sound effects for abilities and antag acquisition, adds icons to the abilities and changes up the objective generation a bit.

Florida has the longest coastline (1,197 statute miles) in the contiguous United States, with 825 miles of accessible beaches to enjoy.
It’s the only state that borders both the Atlantic Ocean and the Gulf of Mexico.
Wherever you are in Florida, you're never more than 60 miles from the nearest body of salt water.
The state’s highest natural point, Britton Hill, is only 345 feet above sea level -- the lowest high point of any state in America.
Key West is the southernmost point in the continental United States.

* Sprites & Ability Changes

Adds in new sprites made by Ook for Florida Man's abilities.

Decreases the cooldown of Lesser Narcotimancy to make rolling for drugs a bit less painful.

Increases the possible number of chemicals that Lesser Narcotimancy can provide.

The U.S. state of Florida is home to the world’s most dangerous tree – the Manchineel tree. All parts of the tree contain strong toxins.
Mere contact with the sap from this tree can cause blisters on the skin. The tree is also known as “the beach apple” and “little apple of death.

* Better rename proc

* Tony Brony

Florida Man has a 1% chance to be renamed Tony Brony.
Why? Because the stream was going to shoot a horse if I didn't add this.

* Made the pods appear in the pod launcher

* Traitor Panel Compatibility

Moves the Florida Man ability & trait addition to the on_gain datum for the antagonist itself.

Florida is the boating and fishing capital of the world.

It has more than 7,700 lakes, 11,000 miles of rivers, 2,276 miles of tidal shoreline, and has produced more than 900 world fishing records, more than any other state, or country.

Co-authored-by: Merlin1230 <76177064+Merlin1230@users.noreply.github.com>

---
## [ChoGGi/SurvivingMars_CheatMods](https://github.com/ChoGGi/SurvivingMars_CheatMods)@[a918f214a5...](https://github.com/ChoGGi/SurvivingMars_CheatMods/commit/a918f214a53b905d5518db014c63493640d878cd)
#### Thursday 2022-02-10 05:03:42 by ChoGGi

Lib:
- Added class name to examine>parents for ease of copying name.
- Added limit count to RetMapBreakthroughs().
- Fixed issue examining certain strings.

Mods:

Allow BB Buildings 0.5:
Updated for some picard update (Thanks McKaby).
v0.4
Log spam.

Delete Object:
Adds a button to forcefully delete the selected object.
Mod option to turn off the button.

Faster UI:
Remove some animations: build menu/pins/overview/map switch.

Find Map Locations 0.9:
Added limit to number of breakthroughs (needs lib v10.9).

Fix BB Bugs 0.5:
Removed some fixes from mod added to Below & Beyond Content Update #2 - Hotfix 3:
Stuck notifications for last war.
Explorer disappearing when going underground.
Mystery Log stuck on screen from mini mysteries.

Fix Farm Oxygen:
If you remove a farm that has an oxygen producing crop (workers not needed) the oxygen will still count in the dome.
This will also update existing domes.

Fix Floating Rubble:
On load move any floating underground rubble to within reach of drones (might have to "push" drones to make them go for it).

Game Rules Permanent Disasters 1.4:
Fixed rockets not launching (thanks Xorn).

Omega Unlocks All 0.3:
Made sure it only happens when omega is unlocked (incase func used for other stuff).

RC Transport Cheats:
Transports in auto mode will pick up any loose resources (excluding those within range of drone hubs/commanders).
Mod option to change storage amount / speed it takes to harvest from surface

Remove SupplyPod Limit 0.5:
Log spam.

Selectable Cables Pipes 0.6:
Added cheats pane (for when cheats are enabled).

Surface Resource Markers:
Add mini markers to surface resources.
Toggle in mod options.

View Colony Map 1.8:
Added limit to number of breakthroughs (needs lib v10.9).

github@choggi.org

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[dd747fcc5a...](https://github.com/tgstation/tgstation/commit/dd747fcc5a46df051a5fe0e42950c46c72269244)
#### Thursday 2022-02-10 05:26:12 by MrMelbert

BIDDLE HERETICS: Heretic revamp! (Shadow Realm, UI Overhaul, Refactoring, and Murderhoboing Tweaks)  (#64658)

About The Pull Request

This PR seeks to revamp heretic in it's almost entirety.

Closes #58435
Closes #62114
Closes #63605

image
Gameplay changes:

    The heretic no longer starts with a Codex Cicatrix or a Living Heart.
        Heretics now draw transmutation runes by using any writing tool while having Mansus Grasp active.
            The Mansus Grasp can be used to remove heretic runes.
        Draining influences can be done with "right click".
            While draining, people who examine you may get a message hinting that you're interacting with an influence.
            Drained influences can also be dispersed with anomaly neutralizers!
        The Codex Cicatrix is now a researchable item that lets you gain additional knowledge from influences.
            The Codex can still draw and remove runes, and does it faster.
        The Living Heart is now the heretic's heart. Literally. It's the heart in their chest. Their heart takes on the appearance of a living heart, and they can pulse it on demand to track their targets. This makes an audible noise.
            If your heart is lost (you're disemboweled or whatever), you need to do a ritual to regain it!

    Casting any heretic spell (besides Grasp) requires a Focus.
        A Heretic Focus is a neck item they can transmute.
        Heretic robes also function as a focus when toggled up.
        Ascending also disables the need for a focus, because of course.

    Heretics now gain 1 knowledge point passively every 20 minutes.

    Sacrificing has been revamped entirely.
        A heretic now gains four sacrifice targets on spawn.
            One random crewmember
            One member of their department
            One member of security
            One member of command (a "high value" sacrifice)
        You can sacrifice people who are in in soft-crit, hard-crit, or dead.
        Sacrificing someone will cuff them (if they are not), HEAL them, revive them, and set them unconscious. After a short time. they will be sent to a shadow realm. This shadow realm is themed to your heretic type.
            The shadow realm is a 2 minute long survival challenge where the sacrificee is subject to a constant barrage of shadowy hands.
            If they survive, they are teleported back to a random turf with no memory of how they got there. They'll also slur a TON to get the point across.
            If they die, their corpse is teleported back to a random turf on the station.

    No more multi-hearting! Your targets are your own.
        BUT adds a knowledge that allows heretics to reroll their sacrifice targets with a ritual.

    Each path now has a "Rituals of Knowledge". These are randomly generated rituals that may be difficult to complete but awards knowledge points in return.

    Ascending now has some requirements.
        To learn the ascension ritual, you need to complete all of the objective you are assigned.
        The ascension ritual now each have a varied requirement, instead of "needing 3 bodies" only.

    Other minor gameplay changes:
        Lots of balance tweaking.
            Buffed some summons.
            Buffed the Lord of the Night very slightly.
            Nerfed the Madness Mask.
        Put a limit on the amount of blade transmutations possible at once. 3 for flesh, 2 for other paths.
        Logs of BUG fixing.
        Rust Grasp is now based on right click for surfaces instead of combat mode.
        General grammar and flavor tweaks a ll around.

Admin / code changes:

    Revamped the way heretics appear within the traitor panel.
        You can now easily see who they're targeting for sacrifice and what they have researched
        Also adds some helpful buttons to heretics, like giving them points!
    Refactored much, much of heretic code
        LIKE ALL OF HERETIC CODE WAS IN 4 FILES.
            Split up all the knowledge, spells, and items that belong to the heretic into their own files and folders.
        Not only that, but everything internally was still named "Eldritch Cultist" and similar.
            Almost every mention of "Eldritch Cultist" has been properly replaced by "Heretic".
    Much better reference handling all around.
    General code improvements over heretic stuff.
    Unit tests, because of course.

Todo

Sprites for the focus

    Look at adding 1-2 other objectives prior to ascension. Theft? Special rituals? ("Rust [x] tiles to be able to ascend")

Why It's Good For The Game
Okay but why?

Heretics are not in a good place at the moment, this much is clear. They've been completely disabled on MRP for this reason.

The reasoning is simple: A lot of murder.
There's nothing inherently wrong with an antagonist heavy with murder, but the Heretic really missed the mark.
Gib, gib, gib, then ascend so you can keep killing.

In the background, the Heretic was FULL of flavorful spells, rituals, and "lore" stolen from Cultist Simulator that was unfortunate enough to be shackled to the heretic's gameplay loop.

So, this revamp aims to amend that:

Dial back the heretic's focus on mass murder and put more focus on the heretic's interesting flavor.
Spooky maintenance rituals, knowledge seeking maniac.

    Sacrifice no longer outright kills / requires murder, meaning a heretic can progress without racking up a bodycount.
    Influence is gained passively over time, so they can spend influence on more interesting side paths.
    Side paths are required to progress to ascension, so they're encouraged to explore new things.

Ultimately, while there still may be a little way to go, this PR seeks to take a good leap in starting it.
Changelog

cl Melbert
add: Large scale heretic revamp!
expansion: The Codex Cicatrix is no longer a roundstart heretic item. Research is handled through their antag info UI. Rune drawing is done by using a writing tool with Mansus Grasp active in your offhand. The actual Codex is an unlockable ritual item now.
expansion: The Living Heart is no longer a roundstart heretic item - their actual heart now becomes their Living Heart, and it makes a sound when triggered. Losing your heart (being disemboweled) will require you to do a ritual to regain it.
expansion: The Hereic Antag UI has been overhauled, and now hosts much of their mechanics as well as providing some helpful tips for newer players.
expansion: Most heretic spells now require a focus to cast. All heretics can make a basic focus necklace, and some heretic equipment also functions as a focus. (Credit to Imaginos for the focus sprite!)
expansion: Heretics now passively gain +1 influence every 20 minutes.
expansion: Heretic sacrificing has been reworked. You can now sacrifice people who are in soft crit or weaker. Sacrificing someone heals them, cuffs them, and teleports them to the SHADOW REALM, where they must dodge a barrage of hands to survive. Survive long enough and you return without memory - die, and your body will be thrown back.
expansion: Heretics now have a few new rituals, including the Ritual of Knowledge, a randomly generated ritual that awards knowledge points.
expansion: Heretic ascension now has a few requirements - you must complete your objectives assigned to you prior to learning the final ritual, and all the final rituals have been changed a bit!
qol: Using the Heretic's Mansus Grasp on surfaces (EX: Rust Grasp) now works on right-click, instead of combat mode.
qol: Used heretic influences can now be removed with a Anomaly Neutralizers.
balance: Some heretic rituals are now limited in the amount they can make. You can only have up to 2 heretic blades crafted at once (3 if you are Path of Flesh).
balance: The Lord of the Night has been buffed to be a little scarier. Did you know the Lord of the Night can eat arms to regain body parts and heal?
balance: Buffed some heretic summons - mostly their health pools.
balance: Nerfed the heretic's Mask of Madness. It can no longer infinite stam-crit you.
balance: Nerfed the heretic's ash mark.
balance: Nerfed a bunch of on-hit-heretic-blade effects. Many effects only apply on mark detonation now: Void blade silence, flesh blade wounds, ash blade gasp cooldown refund.
fix: Fixed quite a few bugs and unintended behaviors with heretic code.
refactor: Refactored and improved much of Heretic code. Improved the file structure dramatically.
admin: The heretic's traitor panel has been beefed up a bit.
/cl

---
## [OrionTheFox/tgstation](https://github.com/OrionTheFox/tgstation)@[079f8ac515...](https://github.com/OrionTheFox/tgstation/commit/079f8ac51554bb338ac5826c9d06c8d4bc10be80)
#### Thursday 2022-02-10 08:04:13 by LemonInTheDark

Adds moveloop bucketing, uses queues for the singulo rather then sleeps (#64418)

Adds a basic bucketing system to move loops.

This should hopefully save a lot of cpu time, and allow for more load while gaining better smoothness.

The idea is very similar to SStimer, but my implementation is much more simple, since I have to worry less about long delays and redundant buckets.
Insertion needs to be cheaper too, since I'm making a system that by design holds a lot of looping things

It comes with some minor tradeoffs, we can't have constant rechecking of loops if a move "fails", not that we really want that anyway
We also lose direct control over the timer var, but I think that's better, don't want people manipulating that directly
Not that it even really worked very well back when we did have it
Removes the sleep from singularity code

Rather then using sleep to store the state of our iteration, we instead queue the iteration in a list.
We then use a custom singulo processing subsystem to call our "digest" proc several times per full eat, with the hope of staying on top of
our queue
This rarely happens because the queue is too large, god why is a sm powered singulo 24x24 tiles.

I've also A: cached our dist checks, and B: Added dist checks to prevent attempting to pull things out of range
This might look a bit worse, but it saves a lot of work

Oh right and I made the singulo unable to eat while it still has tiles to digest. The hope is to prevent
overwork and list explosion.

Hopefully this will prevent singulo server stoppage, though I've seen some other worrying things in testing.

---
## [liamjones/flipper](https://github.com/liamjones/flipper)@[dc1cf7a3e3...](https://github.com/liamjones/flipper/commit/dc1cf7a3e3332361ed3c738521538e175c63be60)
#### Thursday 2022-02-10 08:16:18 by Pascal Hartig

Lint for british spelling

Summary:
I hate when I have to comment on a diff and tell somebody to please not use
Her Majesty's Spelling, so I'll let the computer do the shouting.

Mixing two ways of spelling the same thing just isn't fun. I had to
work with an Android library that insisted on spelling it `colour`,
leading to awkward code like `colour: COLORS.BLUE` which is just annoying
and hard to remember.

Reviewed By: lblasa

Differential Revision: D30015807

fbshipit-source-id: 9f913e72617301273dbe12c60b9cdba8cea05537

---
## [kristian/neonbee](https://github.com/kristian/neonbee)@[0d4a0c9dd0...](https://github.com/kristian/neonbee/commit/0d4a0c9dd06fa7c6a82be4bb7a26c61e3bc6360d)
#### Thursday 2022-02-10 08:28:00 by Kristian Kraljic

feat: improve `Launcher`, `Deployable`, `EntityModelManager` and more

This change is huge... I am sorry, but here is a video of me explaining why the change got so huge [1]. Sorry? Good news tough: All changes have been made interface and thus downwards compatible to the old NeonBee version, thus no adaptions to existing functionality should become necessary. Let me go into detail what changed and which quality of life / boy scout rule improvements have been made:

- Many NeonBee methods had been introduced in a pre-Vert.x 4-era. Meaning they did not take advantage of the futurization process Vert.x went through. This change rewrites many methods and simplifies them by switching the futurized methods, instead of methods using handlers.

- Improved the NeonBee bootstrap by making it more asynchronous, by changing the structure of method calls throughout the boot process and wrapping blocking code in `AsyncHelper.executeBlocking` calls.

- Simplified implementation of the `Launcher` class. Instead of manually defining and parsing all options in the launcher to get to a `NeonBeeOption` instance, instead switching to Vert.x's annotation-based `CLIConfigurator` implementation. Annotations are now defined directly in the `NeonBeeOptions` and injected into the `NeonBeeOptions` instance by the `CLIConfigurator`. This makes it much simpler and less error prone to define options and makes it also clear: everything that is in `NeonBeeOptions` can be defined through the command-line or environment. For the latter a `EnvironmentAwareCommandLine` was introduced, that also considers the environment variables if no options are set as arguments, deprecating all "helper methods" that have been there for only this reason.

- Added a new `development_conventions.md` document, that elaborates many "hidden rules" that we came up over the years, when it comes to coding conventions, such as: naming conventions for NeonBee variables, whether to use an instance to `NeonBee` or to `Vertx`, where to place `Context` variables in method signatures and how to properly correlate log messages. Then, in this change, a couple of old methods have been cleaned up to fit this new guiding document.

- The old naming choice for the "/verticles" subfolder does no longer make sense, because not only verticles are deployed by the `DeployerVerticle`, but full "modules". Thus, introduced a new `getModulesDirectory` method to `NeonBeeOptions` and deprecated the old `getVerticlesDirectory`. Two `DeployerVerticle` will now take care to deploy the old and the new directory if necessary (present).

- Introduced a new --module-jar-paths option to NeonBee options, that allows to define paths to module JARs, that will get deployed during the bootstrap phase of NeonBee into own self-first class-loaders. Previously the only option to deploy modules was through NeonBees `DeployerVerticle`, that was watching the `verticles` sub-directory for changes. The new option grants to also deploy modules that are not physically in that folder.

- Split up `EntityModelManager` into its (previously embedded) sub-classes by introducing a package private `EntityModelLoader` class. Futurized many of its methods and improved the concept for registering "external models": Previously modules did register / unregister models to the `EntityModelManager` by using their module identifier as a unique key. The `EntityModelManager` kept a private map of these IDs (`BUFFERED_MODULE_MODELS`) mapping to a set of compiled `EntityModel` objects. Now the concept was changed by introducing a new `EntityModelDefinition` object, that can be used to influence compilation of models of the `EntityModelManager`. Whenever a `EntityModelDefinition` is added / removed from the `EntityModelManager` it will attempt to compile a new "global" set of models. This allows for inter-dependent models and sets up the `EntityModelManager` for an upcoming change to be completely remodeled in order to support versioned models going forward (see the roadmap). It also makes managing the "external models" more easy, because no longer we need to hold a map of identifiers, but only a `Set<EntityModelDefinition>` to be maintained by the `EntityModelManager`. This makes it useful not only to modules, but any object that needs to deal with model generation can now supply a `EntityModelDefinition`.

- Removed `NeonBeeModule` in favor of a new `DeployableModule`. The `Deployable` interface was thought to become a generic object. Everything that can be deployed to NeonBee should inherit `Deployable`. `NeonBeeModule` violated this pattern and implemented much the same logic. Now the whole `io.neonbee.internal.deploy` package is consistent again, by introducing a `DeployableModels` (that can deploy `EntityModelDefinition` object), `DeployableModule` (that parses JAR files and splits them up into `DeployableModels` and `DeployableVerticles`) and a generic `Deployables` class, that handles deployments of multiple `Deployable` objects. This makes the whole deployment much cleaner, as for NeonBee everything is now a `Deployable` and the logic, whether it is a module, or a verticle, or a model that is being deployed, is now completely hidden away inside of the respective `Deployable` implementation. After deployment, everything results in the same `Deployment` instance, that can be undeployed again in the same fashion.

- Quality of life improvements to `AsyncHelper` by introducing runnables, cosumers and suppliers that can throw an exception. This allowed to replace existing calls like `AsyncHelper.executeBlocking(vertx, () -> { try { ... } catch (e) { return failedFuture(e); } })` with `AsyncHelper.executeBlocking(vertx, () -> ...)`.

- Simplified `ClassPathScanner` and introduced a new `CloseableClassPathScanner` that closes the underlying `URLClassLoader` to stop leaking resources.

- Introduced a new `ThreadHelper` class, that can be used to retrieve the calling or own class, as well as the class-loader of the current thread.

- Made `NeonBeeProfile` behave the same as for `moduleJarPaths` when getting parsed, meaning that you can define multiple profiles separated by comma.

- Renamed CollectionsHelper to CollectionHelper, because it was the only helper with a plural name.

- Improve many tests (esp. Deployable ones) mainly by mocking more and spying less.

- Made `setEnvironment` and `withEnvironment` work on Windows, to be able to remove `@DisableOnOS` annotation for tests changing environment variables.

[1] https://www.youtube.com/watch?v=AbSehcT19u0

---
## [HumabHatterZed/WhistleWindLobotomyMod](https://github.com/HumabHatterZed/WhistleWindLobotomyMod)@[b1f0f560dc...](https://github.com/HumabHatterZed/WhistleWindLobotomyMod/commit/b1f0f560dc32badd5f95e63a8a69de69fb8d22a9)
#### Thursday 2022-02-10 08:40:36 by HumabHatterZed

Fixed Slime ability, added fix to WhiteNight event to prevent potential softlocks (untested), added Protector ability, reworked Army in Black, Army in Pink, Magical Girl S, moved special ability despair to RULEBOOK_ status, added Roots to totem pool, updated readme.md, added some sprites and emissions

---
## [soltysh/api](https://github.com/soltysh/api)@[5b82635ef1...](https://github.com/soltysh/api/commit/5b82635ef101e7c10b5fcbbcfb81315bb7a0da20)
#### Thursday 2022-02-10 09:13:30 by W. Trevor King

config/v1/types_cluster_version: Add capabilties properties

Roughly as described in [enhancement].  After discussion with Ben and
David, we've made the following changes:

# spec

## capabilities

The [enhancement] didn't have an opinion on whether or not this should
be a pointer.  I've gone with pointer, because I'm fine allowing folks
to leave this unset.  The docs for this pointer property point out
that there's no distinction between nil (Go, or for JSON, null) and an
empty object (&ClusterVersionCapabilitiesSpec{} in Go, {} in JSON), so
we don't have to rehash all the ClusterVersionCapabilitiesSpec
children defaults here, where they'd likely go stale as folks update
defaults within ClusterVersionCapabilitiesSpec or add new child
properties.

### baselineCapabilitySet

David prefered this name to the [enhancement]'s inclusionDefault, and
Ben and I are fine with that name.

David also prefered None to Exclude and vCurrent to Include, with
additional values like v4.11 for "give me the 4.11 stuff, but not new
4.12 stuff, until I have time to look that over after I update to
4.12".  That seems overly complicated to me, and also like we coulld
add v4.11 later if folks felt None and vCurrent weren't convenient
enough, but David wanted v4.11 out of the gate.  We can always see how
it plays out in production, and we can stop adding new v4.y forms if
they aren't popular enough to be worth maintaining.  There's an enum
type to make it easy to validate, and hard to typo, these values.

There's also a map, so consumers like the cluster-version operator who
vendor the API repository can get the API-maintainer-intended
capability membership for each set, now that those semantics are more
complicated than all or nothing.

There were a few ways we could have taken the property default here:

a. Explicit +kubebuilder:default:=... .  No option for folks to sit on
   the fence, or to adjust existing clusters later without the admin's
   explicit buy-in.  But no ambiguity about what happens if the user
   has no opinion.

b. omitempty, and docs for "we'll pick a sane default if you don't
   care", that don't commit to a specific default.  Great for when we
   decide to change our default preference, because we don't need to
   hunt down buy-in from admins that have deferred to us.  Not great
   for folks who are mildly curious about our current choice, but who
   still trust us to evolve the default (I think this set is nearly
   empty).

c. omitempty, and docs for "the current default is A, but who knows
   tomorrow".  Effectively (b), but also gives folks some information
   that's not actionable which can go stale as soon as they close
   their eyes.

(a) makes sense if we are confident we will never want to change our
default, and that seems plausible in this case.  (b) makes sense when
we think we might change our default, and I'm fine with that in this
case too.  I don't really understand the use case for (c), but as
David points out, even if we do change the default, we don't expect to
change it often, so maybe my personal take is off and there are a
bunch of folks who are mildly curious about our current choice, but
who still trust us to evolve the default.  Anyhow, David's the
approver, so we're going with (c).

### additionalEnabledCapabilities

David prefered this name to the [enhancement]'s inclusionDefault, and
Ben and I are fine with that name.

In the [enhancement], Ben had intended to distribute the ability to
create new capabilities to all manifest-providing repositories, simply
by declaring the capability.openshift.io/name annotation.  David was
worried about validation, and also possibly about insufficiently
scoped names between separate teams, so this pull request declares a
central enum where API maintainers can review and approve new
capability names, and work them into the appropriate entries in the
set maps.  The installer and cluster-version operator will have to
bump their vendored API version after each addition to pick up the new
changes, but new capability additions shouldn't be too frequent to
make that particularly painful.

### exclude

The [enhancement] also provided a way to drop specific capabilities
from the selected set (inclusionDefault or baselineCapabilitySet).
Ben still feels like that will be popular, but David is skeptical, and
because we can always add a property in this space later without
breaking backwards compatibility, we're leaving it off for now.

# status

## capabilities

The [enhancement] didn't have an opinion on whether or not this should
be a pointer.  I've gone with non-pointer, because we will always
declare at least some capabilities (e.g. knownCapabilities), so users
will be able to discover additional capabilities which they might want
to enable in their cluster.

### enabledCapabilities

David prefered this name to the [enhancement]'s include, and Ben's ok
with that name.  I'm not wild about 'Capabilities' in:

  status:
    capabilities:
      enabledCapabilities: ...

but David was committed, citing the example of:

  FeatureGateSelection.FeatureSet

Although FeatureGateSelection is consumed with less context:

  type FeatureGateSpec struct {
	FeatureGateSelection `json:",inline"`
  }

I'd pushed back against the stuttering in [stutterPrecedent], but
without success, and :shrug:, doesn't matter all that much if folks
have to type a few redundant characters to use this property.

### knownCapabilities

The [enhancement] had floated 'exclude'.  There are a few capability
sets in play for the status listings:

* A is the set of all caps.
* I is the set of included caps.
* E is the set of excluded caps.
* Each cap must be either included or excluded, so I and E are disjoint, and the union of I and E is A.

So you can take any two of those three sets and construct the one
you're missing:

* A = I ∪ E
* E = A - I
* I = A - E

If we have to pick two to include in status, picking I and E gives us
all the data we need, and saves a few bytes by excluding the largest,
which is A.  But David preferred picking I (as enabledCapabilities)
and A (as knownCapabilities) [knownCapabilities], so that's what we're
doing in this commit.

### inclusionDefault

The [enhancement] also provided a way to echo the spec set in an
inclusionDefault status property.  I've left that out of the status
structure, because I'm using explicit, exhaustive list for
enabledCapabilities and knownCapabilities there.  The exhaustive lists
will provide a convenient set (via A - I set subtraction) of "things
you don't have right now, but which you could choose to install right
now", so admins don't have to guess about their options there.  With
the exhaustive lists, reflecting the default setting didn't seem to
add much useful information.  And we can always add that property to
the status structure later if we do decide it would be useful.

## conditions

I have not created a constant with the status.conditions[] type that
will be used to declare "we are installing a capability you have not
asked for, because we don't support uninstalling capabilities, and
that one was tainted in via your cluster's history".  We can come back
and declare that constant later if we want, although that's somewhat
complicated by the fact that we use ClusterOperatorStatusCondition,
and the new condition type would not be something that makes sense for
ClusterOperator.

[enhancement]: https://github.com/openshift/enhancements/blob/88cb7438f3ac0a8121e3cef87cb144097ece8cda/enhancements/installer/component-selection.md
[knownCapabilities]: https://github.com/openshift/api/pull/1106#discussion_r799819632
[validation]: https://book.kubebuilder.io/reference/generating-crd.html#validation
[statusPropertyNames]: https://github.com/openshift/api/pull/1106#discussion_r799819632
[stutterPrecedent]: https://github.com/openshift/api/pull/1106#discussion_r799879689

---
## [grafma8/next.js](https://github.com/grafma8/next.js)@[91146b23a2...](https://github.com/grafma8/next.js/commit/91146b23a21e33d54332a469f30afe6e6156cd65)
#### Thursday 2022-02-10 09:52:03 by Glenn Gijsberts

Make adjustment to cache config of with-apollo example (#32733)

## Description
This year we implemented the new Apollo config using this example. We recently moved to `getServerSideProps` as well, however, this was giving us some cache problems. The issue was that the cache was older than the actual data that was coming from the server side query. 

Because the `merge` of the cache in `apolloClient.js` is merging the existingCache in the initialState it will overwrite the "fresh" initialState with properties that already exists. This means that if you have something in your cache from previous client render, for example `user` with the value `null`, and you go to a new page and do a new query on the server which returns a value for the `user` field, it will still return `null` because of that `merge` function.

Since this was weird in our opinion, we've changed this in our own environment by always overwriting the existing cache with the new initialState, so that the initialState that is coming from a fresh server side query is overwriting. We thought it was a good idea to reflect this also in this example, because we couldn't think of a reason why the existing cache should overwrite fresh queries.

I've added a reproduction that shows what this is exactly about. I hope my description makes sense, let me know what you think!

## Reproduction of old scenario
Created a reproduction branch here: https://github.com/glenngijsberts/with-apollo-example. Using a different API than in the example, because of https://github.com/vercel/next.js/issues/32731.

1. checkout the example
2. yarn
3. yarn dev
4. visit http://localhost:3000/client-only
5. Hit "Update name". This will run a mutation that will update the cache automatically. Because I use a mocked API, the actual value on the API won't be updated, but this is actually the perfect scenario for the problem because in reality data can already change in the meantime when you're doing a new request.
6. Go to the SSR page
7. This will display two values: one is coming from the server side request (which is the latest data, because no cache is used in `getServerSideProps`) and the other is using the cache, which is outdated at that point, yet it's still returned because the old way of merging the cache was picking the existing cache over the initialState that was coming from the fresh server side query.

## Documentation / Examples

- [x] Make sure the linting passes by running `yarn lint`

---
## [Ryan-Bernardo/Ryan-Bernardo](https://github.com/Ryan-Bernardo/Ryan-Bernardo)@[0827fda604...](https://github.com/Ryan-Bernardo/Ryan-Bernardo/commit/0827fda604763c7b0c3f5666eb1bf1cc14f525fc)
#### Thursday 2022-02-10 11:12:20 by Ryan-Bernardo

About me

I enjoy being able to create something through code and bringing it to life, I've been coding for a while now and ever day I feel good when a line of code runs with no errors.
When I run code that has errors I feel great when I'm able to debug fix those errors.

I am currently from Cape Town - 21 Erie road Retreat.
I love learning new and exciting things especially when it comes to coding, there's so much more I'd like to learn. 
I'm hardworking and committed to any project I take on.

---
## [pedromdpereira/Warcraft-Guardians-of-Azeroth-2](https://github.com/pedromdpereira/Warcraft-Guardians-of-Azeroth-2)@[a5946f267b...](https://github.com/pedromdpereira/Warcraft-Guardians-of-Azeroth-2/commit/a5946f267be861fb53cb265317e24ec064fc5b6a)
#### Thursday 2022-02-10 11:15:20 by Loralius

holy site modifiers; amani, pandaren, jinyu doctrines

Ula-Tek and Karazhan now grant positive opinion from rulers of different faiths. Arcane is now shunned by Amani. Pandaren and Jinyu ignore life magic.

---
## [ElecarnoYT/Bismuth](https://github.com/ElecarnoYT/Bismuth)@[27713a8790...](https://github.com/ElecarnoYT/Bismuth/commit/27713a8790367fde3f0938500b950d941a52253b)
#### Thursday 2022-02-10 14:49:18 by Jachdich

fucked up shit fucking hell I dont have the sanity to do anything i m going to explod

---
## [k21971/EvilHack](https://github.com/k21971/EvilHack)@[a4e0378bb5...](https://github.com/k21971/EvilHack/commit/a4e0378bb510209b72eafd3dcfa0d7d4caf8c638)
#### Thursday 2022-02-10 15:22:44 by k21971

Fix: cursed light vs worn light.

From NetHack 3.7 git commit e8341dc (modified, with bug fixes from
commit a1feac4):

'Another gold dragon scales/mail issue, reported bu vultur-cadens:
reading a cursed scroll of light extinguishes carried light sources
except for wielded Sunsword and worn gold dragon scales/mail; there
was a special message for Sunsword (preventing the hero from being in
darkness) but no such message for gold dragon scales/mail.  Replace
the special message with a more generic one applicable to both cases.

Also, implement the suggestion that cursed light degrade the amount
of light being emitted (which varies by bless/curse state) for those
two cases.  Sunsword has a 75% chance to resist, gold dragon scales
25% chance.  And add the inverse:  blessed scroll of light might
increase the amount of light by improving their bless/curse state.
The resistance check applies here too and isn't inverted; Sunsword
is still fairly likely to resist.

Uncursed scroll of light, spell of light regardless of skill, zapped
or broken wand of light have so such effect.'

This affects EvilHack's shield of light also.

---
## [bytewax/bytewax](https://github.com/bytewax/bytewax)@[c53b329d0c...](https://github.com/bytewax/bytewax/commit/c53b329d0c364b99c97ab7893576a137a3be4f5c)
#### Thursday 2022-02-10 17:01:48 by David Selassie

Renaming of stateful operators

Here's a prototype of a set of slightly different, and hopefully more
uniform, stateful operators. I took a long look at how we used
`exchange`, `accumulate`, `state_machine`, and `aggregate` in our
existing examples and also what kind of interfaces the build in Python
types give us.

I'm excited that things fell into a shape that has some nice parallel
construction and I think that means these will hopefully be easier to
understand.

`exchange` is banished. My current thinking is that it's a "scheduling
implementation detail" that shouldn't be user visible. I don't like
that it was possible to write a dataflow that worked with a single
worker, then broke with multiple workers. Every time we previously
used `exchange`, we really wanted a "group by" operation, so these
changes make this first class. (I understand the concept of exchange
needs to be there, but I think it's something that should only be
exposed when you're writing Timely operators and actively coming up
with a way to orchestrate state.)

If we want to support both mutable and immutable types as state
aggregators, we have to have our function interface return updated
state and not modify in place. I don't think we should force users to
do things like

```python
class Counter:
    def __init__(self):
        self.c = 0
```

just to count things, so keep immutables working. Thankfully, Python
has the `operator` package which lets you have access to `+` as a
function and all the operators return updated values. This makes it
possible to write in the functional style necessary without much
boilerplate. But you can still write out lambdas or helper functions
too.

Many of our stateful examples are of the form "collect some items and
stop at some point". Since this is a dataflow, the stream could be
endless, so we need a way to signal that the aggregator is complete.
Noting that the epoch is complete is super common "is complete" case
and we can include that for convenience, but the general case exists
too. Since they're similarly shaped problems, make sure the interface
looks similar.

So what happened?

I want to put forth `key_fold`, `key_fold_epoch`,
`key_fold_epoch_local`, and `key_transition` as the state operators. I
wrote out usage docstrings and updated examples, but tl;dr:

- They all start with `key` because they require `(key, value)` as
  input and group by key and exchange automatically. They output
  `(key, aggregator)` too.

- The ones with `fold` do a "fold": build an initial aggregator, then
  incrementaly add new values as you see them, then return the entire
  aggregator.

- The ones with `epoch` automatically stop folding at the end of each
  epoch since that's such a common use case. Otherwise you provide a
  function to designate "complete".

- `local` means only aggregate within a worker. We haven't found a use
  case for this yet that isn't a performance optimisation (and one
  that maybe could be done automatically?).

- `transition` isn't a "fold" in that it's always emitting events (not
  just when the aggregation is complete).

- Input comes in undefined order within an epoch, but in epoch order
  if multiple epochs.

If you feel like you know the shape of the old versions, then:
`key_fold_epoch ~= aggregate`, `key_transition ~= state_machine`,
`key_fold` is `state_machine` but shaped like `aggregate`, and
`key_fold_epoch_local` is `accumulate` but shaped like `aggregate`.

I've updated the examples too. I wanted to try out seeing how concise
you could get using the built in types to see how the library might
feel in that dimension. But I understand that some of these examples
might be a bit too terse. We don't have to necessarily go that way in
the docs, but it's cool to see that it can work and you can count like:

```python
flow.key_fold_epoch(lambda: 0, operator.add)
```

Let me know what you think!

---
## [Jebaitedneko/android_kernel_xiaomi_vayu](https://github.com/Jebaitedneko/android_kernel_xiaomi_vayu)@[afa97afaf8...](https://github.com/Jebaitedneko/android_kernel_xiaomi_vayu/commit/afa97afaf83481bce88eb93664cca4626c7238c6)
#### Thursday 2022-02-10 18:28:17 by Wang Han

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
Signed-off-by: Carlos Jimenez (JavaShin-X) <javashin1986@gmail.com>
Signed-off-by: Jebaitedneko <Jebaitedneko@gmail.com>

---
## [cpcallen/blockly](https://github.com/cpcallen/blockly)@[42c4ef7b3d...](https://github.com/cpcallen/blockly/commit/42c4ef7b3d10ef1669e38854661e022d32d1a4eb)
#### Thursday 2022-02-10 18:41:55 by Christopher Allen

Experimental conversion of blockly.js to ES Module

To see if my theory about module loading was correct, and that we
would be fine so long as the module loader didn't attempt to
load any goog.module after the first ES Module, I have converted
blockly.js to ESM.

The conversion is a terrible quick hack; all the stuff concerning
get/set accessors is totally broken and there are lots of other
problems, but it is functional otherwise.

And module loading does appear to be working correctly.

There is a problem, however: doing

    var Blockly = goog.require('Blockly');

in blockly_uncompiled.js doesn't work, because (curse you, base.js!)
goog.require only returs the module export object when called from
a goog.module (or ES module, presumably), not when called from a
script.

I've tried to work around this using goog.module.get but for some
reason it is also just returning null.  Further investigation
required!

---
## [official-stockfish/Stockfish](https://github.com/official-stockfish/Stockfish)@[cb9c2594fc...](https://github.com/official-stockfish/Stockfish/commit/cb9c2594fcedc881ae8f8bfbfdf130cf89840e4c)
#### Thursday 2022-02-10 18:57:28 by Tomasz Sobczyk

Update architecture to "SFNNv4". Update network to nn-6877cd24400e.nnue.

Architecture:

The diagram of the "SFNNv4" architecture:
https://user-images.githubusercontent.com/8037982/153455685-cbe3a038-e158-4481-844d-9d5fccf5c33a.png

The most important architectural changes are the following:

* 1024x2 [activated] neurons are pairwise, elementwise multiplied (not quite pairwise due to implementation details, see diagram), which introduces a non-linearity that exhibits similar benefits to previously tested sigmoid activation (quantmoid4), while being slightly faster.
* The following layer has therefore 2x less inputs, which we compensate by having 2 more outputs. It is possible that reducing the number of outputs might be beneficial (as we had it as low as 8 before). The layer is now 1024->16.
* The 16 outputs are split into 15 and 1. The 1-wide output is added to the network output (after some necessary scaling due to quantization differences). The 15-wide is activated and follows the usual path through a set of linear layers. The additional 1-wide output is at least neutral, but has shown a slightly positive trend in training compared to networks without it (all 16 outputs through the usual path), and allows possibly an additional stage of lazy evaluation to be introduced in the future.

Additionally, the inference code was rewritten and no longer uses a recursive implementation. This was necessitated by the splitting of the 16-wide intermediate result into two, which was impossible to do with the old implementation with ugly hacks. This is hopefully overall for the better.

First session:

The first session was training a network from scratch (random initialization). The exact trainer used was slightly different (older) from the one used in the second session, but it should not have a measurable effect. The purpose of this session is to establish a strong network base for the second session. Small deviations in strength do not harm the learnability in the second session.

The training was done using the following command:

python3 train.py \
    /home/sopel/nnue/nnue-pytorch-training/data/nodes5000pv2_UHO.binpack \
    /home/sopel/nnue/nnue-pytorch-training/data/nodes5000pv2_UHO.binpack \
    --gpus "$3," \
    --threads 4 \
    --num-workers 4 \
    --batch-size 16384 \
    --progress_bar_refresh_rate 20 \
    --random-fen-skipping 3 \
    --features=HalfKAv2_hm^ \
    --lambda=1.0 \
    --gamma=0.992 \
    --lr=8.75e-4 \
    --max_epochs=400 \
    --default_root_dir ../nnue-pytorch-training/experiment_$1/run_$2

Every 20th net was saved and its playing strength measured against some baseline at 25k nodes per move with pure NNUE evaluation (modified binary). The exact setup is not important as long as it's consistent. The purpose is to sift good candidates from bad ones.

The dataset can be found https://drive.google.com/file/d/1UQdZN_LWQ265spwTBwDKo0t1WjSJKvWY/view

Second session:

The second training session was done starting from the best network (as determined by strength testing) from the first session. It is important that it's resumed from a .pt model and NOT a .ckpt model. The conversion can be performed directly using serialize.py

The LR schedule was modified to use gamma=0.995 instead of gamma=0.992 and LR=4.375e-4 instead of LR=8.75e-4 to flatten the LR curve and allow for longer training. The training was then running for 800 epochs instead of 400 (though it's possibly mostly noise after around epoch 600).

The training was done using the following command:

The training was done using the following command:

python3 train.py \
        /data/sopel/nnue/nnue-pytorch-training/data/T60T70wIsRightFarseerT60T74T75T76.binpack \
        /data/sopel/nnue/nnue-pytorch-training/data/T60T70wIsRightFarseerT60T74T75T76.binpack \
        --gpus "$3," \
        --threads 4 \
        --num-workers 4 \
        --batch-size 16384 \
        --progress_bar_refresh_rate 20 \
        --random-fen-skipping 3 \
        --features=HalfKAv2_hm^ \
        --lambda=1.0 \
        --gamma=0.995 \
        --lr=4.375e-4 \
        --max_epochs=800 \
        --resume-from-model /data/sopel/nnue/nnue-pytorch-training/data/exp295/nn-epoch399.pt \
        --default_root_dir ../nnue-pytorch-training/experiment_$1/run_$run_id

In particular note that we now use lambda=1.0 instead of lambda=0.8 (previous nets), because tests show that WDL-skipping introduced by vondele performs better with lambda=1.0. Nets were being saved every 20th epoch. In total 16 runs were made with these settings and the best nets chosen according to playing strength at 25k nodes per move with pure NNUE evaluation - these are the 4 nets that have been put on fishtest.

The dataset can be found either at ftp://ftp.chessdb.cn/pub/sopel/data_sf/T60T70wIsRightFarseerT60T74T75T76.binpack in its entirety (download might be painfully slow because hosted in China) or can be assembled in the following way:

Get the https://github.com/official-stockfish/Stockfish/blob/5640ad48ae5881223b868362c1cbeb042947f7b4/script/interleave_binpacks.py script.
Download T60T70wIsRightFarseer.binpack https://drive.google.com/file/d/1_sQoWBl31WAxNXma2v45004CIVltytP8/view
Download farseerT74.binpack http://trainingdata.farseer.org/T74-May13-End.7z
Download farseerT75.binpack http://trainingdata.farseer.org/T75-June3rd-End.7z
Download farseerT76.binpack http://trainingdata.farseer.org/T76-Nov10th-End.7z
Run python3 interleave_binpacks.py T60T70wIsRightFarseer.binpack farseerT74.binpack farseerT75.binpack farseerT76.binpack T60T70wIsRightFarseerT60T74T75T76.binpack

Tests:

STC: https://tests.stockfishchess.org/tests/view/6203fb85d71106ed12a407b7
LLR: 2.94 (-2.94,2.94) <0.00,2.50>
Total: 16952 W: 4775 L: 4521 D: 7656
Ptnml(0-2): 133, 1818, 4318, 2076, 131

LTC: https://tests.stockfishchess.org/tests/view/62041e68d71106ed12a40e85
LLR: 2.94 (-2.94,2.94) <0.50,3.00>
Total: 14944 W: 4138 L: 3907 D: 6899
Ptnml(0-2): 21, 1499, 4202, 1728, 22

closes https://github.com/official-stockfish/Stockfish/pull/3927

Bench: 4919707

---
## [Clancey/Maui](https://github.com/Clancey/Maui)@[ac6befcbee...](https://github.com/Clancey/Maui/commit/ac6befcbee23fae2bd358d9ed3217757029a9d1f)
#### Thursday 2022-02-10 19:05:44 by Jonathan Peppers

[controls] Brush.Foo should return immutable instances (#3824)

When profiling a `dotnet new maui` app, with this package:

https://github.com/jonathanpeppers/Mono.Profiler.Android

The `alloc` report shows:

    Allocation summary
    Bytes      Count  Average Type name
    39984        147 2 72     Microsoft.Maui.Controls.SolidColorBrush

Stack trace:

    38352 bytes from:
    (wrapper runtime-invoke) object:runtime_invoke_void (object,intptr,intptr,intptr)
    Microsoft.Maui.Controls.VisualElement:.cctor ()
    (wrapper runtime-invoke) object:runtime_invoke_void (object,intptr,intptr,intptr)
    Microsoft.Maui.Controls.Brush:.cctor ()

Reviewing the `Brush` class, there are indeed 147 `SolidColorBrush`
created on startup that are stored in fields.

But what is weird about this, is that `SolidColorBrush` is mutable!

    public Color Color
    {
        get => (Color)GetValue(ColorProperty);
        set => SetValue(ColorProperty, value);
    }

So I could literally write code like:

    Brush.Blue.Color = Colors.Red;

Blue is red! (insert evil laughter?)

I think the appropriate fix here is that all of these `static
readonly` fields should just be properties that return a new
`ImmutableBrush`. We can cache the values in fields on demand. Then
someone can't do something evil like change `Blue` to `Red`?

I reviewed WPF source code to check what they do, and they took a
similar approach:

https://github.com/dotnet/wpf/blob/5e8187344b2b561ef08b9ca2735cd89cbdd3c11e/src/Microsoft.DotNet.Wpf/src/PresentationCore/System/Windows/Media/brushes.cs#L33-L1586

We should make this API change now before MAUI is stable, and we have
the side benefit to save 39984 bytes of memory on startup?

I added tests for these scenarios, and discovered 3 typos for `Brush`
colors that listed the wrong color.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[af2db3e378...](https://github.com/mrakgr/The-Spiral-Language/commit/af2db3e37881c52d392b3a04fe94389c083bf2e3)
#### Thursday 2022-02-10 19:08:04 by Marko Grdinić

"10:45am. Let me start. I want to figure out how to select groups based on their position.

10:50am. This was much easier than I thought it would be. `@P.y > 0.2` All I had to do was put something like that into a Group Expression SOP.

This makes me wonder, how could I use VEX to find points inside another object?

https://forums.odforce.net/topic/24402-vex-is-point-inside-geometry/
> I don't think so. You would have to find the closest spot on any primitive with XYZDistVOP, evaluate N attribute at this point with Primitive attribute VOP and check with dot product if hit vector (from point in question to hit position) and evaluated normal have the same orientation. If they are opposite, you are outside an object, inside otherwise.

I do not understand the reasoning behind this. My geometry knowledge is lacking.

https://en.wikipedia.org/wiki/Point_in_polygon
> One simple way of finding whether the point is inside or outside a simple polygon is to test how many times a ray, starting from the point and going in any fixed direction, intersects the edges of the polygon. If the point is on the outside of the polygon the ray will intersect its edge an even number of times. If the point is on the inside of the polygon then it will intersect the edge an odd number of times. The status of a point on the edge of the polygon depends on the details of the ray intersection algorithm.

Hmmm, I see. But this method is pretty complicated actually because I'd need to check pairs of primitives.

```vex
@group_group1 &= @P.y > 0.2;
```

Wow, you really can do an intersection like this. And the prefix `@group_` was not an accident. Amazing that this works even though I am running over primitives. I am guess it compares them based on the centroids.

Ok, good enough. Let me go back to the pool scene.

11:30am. Whops, I forgot about something. I meant to pack the flowers, but wouldn't that get rid of their group information?

11:30am. Yeah, if I pack it, bad things happen.

11:40am. How do I generate random ints in Houdini?

12:10pm. I am having trouble with loops in Houdini again. Why the hell is it not assigning the correct iteration number to the variant. It worked fetching the detail in the channel. Why is it not working in the attribute wrangle?

```vex
i@variant = detail("../foreach_count1/","iteration",-1);
```

No, in the first place, it is not like it is getting -1, which is what would happen if the input was missing. Rather, it is assigning 0 for some reason.

```vex
i@variant = detail("../foreach_couqnt1/","iterationq",33);
```

No, I get zero even if I do something like this. That 33 should be the default value if the input is missing.

12:15pm. Ok, if I do an attribute create, and put the detail in a vex expression there it works. But it does not obey the default field. Let me ask about this.

1:05pm.

///

>>874422 (OP)
```
i@variant = detail("../foreach_count1/","iteration",-1);
```

I have this inside of an Attribute Wrangle inside loop block and it does not work for some reason. When I try to put `detail("../foreach_count1/","iteration",-1)` inside an Attribute Create it starts working. To make things really confusing, `detail` is ignoring its third argument which is supposed to be the default when it cannot find the input.

Why is this happening?

>>881418 (You)
> The last argument is always ignored. It is just there so you can change a prim/point/vertex call (which each have an element number argument) to a detail call by changing the name without having to change the arguments as well.
That last argument is not the default argument like I had assumed. It says in the docs that it is always ignored, but the wrangle breaks when I set it to anything other than 0.

>>881420 (You)
```
i@variant = detail(1,"iteration");
```

I got it to work like this. I connected the metadata loop node to the attribute wrangle which allowed me to use it as an index. Why did passing a path not work?

///

This retarded loop issue blasted my brain straight out of me. Houdini is not that well designed. Two very important functions work completely differently in expressions and wrangles. Sigh.

1:45pm.

```
ERROR
Traceback (most recent call last):
  File "C:/PROGRA~1/SIDEEF~1/HOUDIN~1.498/houdini/python3.7libs\viewerstate\utils.py", line 1026, in wrapper
    return func(*args,**kwargs)
  File "C:/PROGRA~1/SIDEEF~1/HOUDIN~1.498/houdini/python3.7libs\viewerstate\interface.py", line 173, in onEnter
    state.onEnter(kwargs["args"])
  File "Sop/scatteralign, ViewerStateModule", line 86, in onEnter
  File "Sop/scatteralign, ViewerStateModule", line 77, in _reloadSurfaceGeo
  File "C:/PROGRA~1/SIDEEF~1/HOUDIN~1.498/houdini/python3.7libs\hou.py", line 39421, in setGeometry
    return _hou.GeometryDrawable_setGeometry(self, geometry)
hou.OperationFailed: The attempted operation failed.
Advanced Drawables only support polygonal geometry
```

I keep getting this error every time I click on the scatter and align node.

1:50pm. Let me stop here. I am long overdue for breakfast and chores.

I really need to figure out how to deal with the above error. It it super annoying to have it pop up every time I click on a node.

3:05pm. Done with breakfast and chores. Let me read a chapter of Netto Chara and I'll start.

3:10pm. Let me start. First let me make sure that having a merge object with a packed instance is what is causing trouble.

3:15pm. Let me try updating Houdini.

3:25pm. This update is taking way too long. Didn't you say only 5mb.

3:45pm. Let me resume. The regular scatter node is nice and quiet, but now it is time to try the align version again.

And it has been fixed! Thank you, thank you!

3:55pm. Now I need to figure out the next step.

4pm. I need to check out Attribute from Pieces. I think it is a problem that the main vines do not have leaves. The branches have the same problem.

I need to make is so that both the main vines and the branches have a certain % of leaves.

But doing that is actually complicated.

I need something to help me better manage pieces. Let me work on that now.

https://youtu.be/N7CDHwgWKVo?t=558
Advanced Scattering in Houdini 18.5

I think it should start around here. Youtube search actually goes over the transcripts.

https://youtu.be/N7CDHwgWKVo?t=730

No, not quite what I wanted.

4pm. Ah, I see that `Attribute from Pieces` node has a random mode. And inside there, it has a weight attribute. Yes, this it!

I've been wondering whether I could assign a weight inside the library pieces, and this is exactly tailor made for such a purpose!

4:15pm. Today the lunch is quite early, but I already ate 2h ago so I'll pass it until after 6pm.

///

Houdini’s workflow for automatically creating large numbers of objects in a scene (such as trees in a forest, rocks and pebbles in a desert, or buildings in a city) is as follows:

* Build the surface you want to scatter the objects across.

* Use the Scatter and Align node to scatter points across the surface.

* Scatter and Align has many high-level controls for how to distribute the points, avoid certain areas, add variety in size and orientation, and so on.

* Build the set of models you want to copy onto the points. For example, a set of different types and shapes of trees to make a forest.

* Use the Copy to Points node to copy the objects onto the points.

Copy to Points has a Piece Attribute parameter that chooses which of the set of models to copy onto each point based on the value of an attribute on the point.

This node is a powerful and flexible way to create the “piece” attribute used by Copy to Points to decide which model to copy onto each point. It lets you assign the pieces randomly, or according to various rules. For example, you could make deciduous trees more likely at lower elevations and conifer trees more likely at higher elevations on a mountain.

///

I am going to have to play with this node for a bit. I want to see how it would be possible to deal with multiple piece attribute. Alternatively, I'll go back to strings now that I know how to inject them.

Why is there a connectivity node in the example image?

> You can create a piece attribute on geometry using the Connectivity node to automatically create a piece attribute).

The docs for this node are quite in depth.

```vex
s@variant = "Branch" + itoa(detail(1,"iteration"));
```

Here is one way. That will allow me to have multiple loops.

4:40pm. Oh, it is possible to autofill pieces. That having said, the weight attribute is not working for me.

It says that weight is the average of the primitives for that pices. So it should be a primitive attribute. Ok, let me do it that way.

4:45pm.

```vex
Branch`detail("../foreach_count1/","iteration",0)`
```

Great. This is in fact the way to set the attribute in attribute create.

4:50pm. Perfect. This gives me just the kind of control I want.

5:20pm. That bug I was thankful for being fixed? Actually that did not happen.

Ah, I am such fool. In scatter and align and I did not at all see the min and max radius. No, nevermind that for now.

6:25pm. Ok, enough. I did what I set out to do, though it was a handful.

One of the side effects of this is that now baking the node tree is instantaneous.

6:30pm. Enough for real. It looks great now. I think at this point I've internalized how to scatter stuff around quite well. Let me get lunch.

7:20pm. That revived me. I was really starving towards the end there. Well, let me close here for the day. I was in the zone throughout today even though I only managed to finish the vines. I still deal with that annoying error. Let me investigate it a bit more.

7:25pm. No, I can't figure it out. Maybe my file uses the old version of the node for some reason. In the newer file it got fixed. At any rate, I won't have to mess with this. In the future what I could simply do is separate the geometry and copy those bulbs to points separately. That would have made things simpler as I would not have needed to care about the curveu attribute.

Hmmm, even in Blender I merged objects to haphazardly.

I'll do this last bit of cleaning up tomorrow. Doing this would also be a good change to put in some variation in the bulbs. Some bulbs could stand to be more open.

7:30pm. This is art, but at the rate I am going I really might end up getting a job. I won't pressure myself over this. I am making slow progress, but I've been in the zone the whole time today and am learning at a steady pace. You don't go into the zone when doing repetitive things, but when breaking new ground in a sustainable manner.

And so step by step, expertise is built. I think I should be able to move to props tomorrow.

7:50pm. Ah, I was wrong. It just occurred to me that the perfect way to do this is to have the flower HDA output 3 geometries: a packed instance, a point cloud, and the last point. Each of these would have the right attributes that I need to copy to points.

This would resolve the issues with merging geometries with different attributes together, and I would not have the current issue with scatter and align. That I am getting that error is a sign I am not using it correctly.

I thought that I need to output groups, but I hadn't thought that through well enough. Damn. Structuring it in terms of passes like I had envisioned yesterday is not ideal.

Hmmm, no, it needn't necessarily be a point cloud. The way I am doing it now has a great advantage of putting less density on smaller branches. The second output could simply be an unpacked mesh.

Right now I have a bunch of geometry that is going to go into rendering unpacked, but I could pack that part, but have the unpacked part be used for scattering. I do not even have to have it as a group. I slice the body off and pass that instead of the point clould. To make that work, I'd need to generate the normals before hand otherwise scatter and align won't know which way is in and out.

Actually, that might not even be an issue. Houdini seems to understand facing well enough simply based off the vertices.

8pm. Let me close here. I put in a little extra thinking session. I am going to redo what I did today tomorrow and seal the deal with these vines. This really seminds me of my programming days. Houdini really is programming after all. Right now, I am not necessarily learning new technique, but how to express myself within the limitations of a language such as it. I've made a bunch of mistakes, but I can finally see the way to move properly.

Even though I've been studying Houdini for a while, it is only in the last week that I've really started to understand how to use it.

I need to do it properly to real internalize the lessons. If I had just gone with the first version, I'd never have realized in which way the group scheme is wrong."

---
## [shiptest-ss13/Shiptest](https://github.com/shiptest-ss13/Shiptest)@[5e29827ceb...](https://github.com/shiptest-ss13/Shiptest/commit/5e29827cebbb7cd08d4bf5b210675526f324bf6d)
#### Thursday 2022-02-10 19:52:00 by Zephyr

Spacemandmm fixes (#799)

* do it

Signed-off-by: Matthew <matthew@tfaluc.com>

* little more detail here

Signed-off-by: Matthew <matthew@tfaluc.com>

* put it in the wrong dmi

Signed-off-by: Matthew <matthew@tfaluc.com>

* Update code/game/objects/items/tools/chisel.dm

Copy paste gp BRRR

Co-authored-by: PrefabQuasar <78622038+PrefabQuasar@users.noreply.github.com>

* resolve some issues that spacemandmm is complaining about because got fucking damn is it annoying when I am trying to code something and I get nonstop errors about stupid issues. also did you know that people though rand was exclusive on the high end? its actually not, both params are inclusive, which is stupid since this is different to almost every other god damn language

Signed-off-by: Matthew <matthew@tfaluc.com>

Co-authored-by: PrefabQuasar <78622038+PrefabQuasar@users.noreply.github.com>

---
## [willior/Action_RPG_1](https://github.com/willior/Action_RPG_1)@[3b57cf9b63...](https://github.com/willior/Action_RPG_1/commit/3b57cf9b634960d5fc06b974e257c4688f91e1e6)
#### Thursday 2022-02-10 20:01:25 by willior

re doing AnimationState system

before, i was using function calls (attack_animation_finished()) at the end of attack animations to determine what animation to travel to next. there is a very brief moment while this is happening which seems to have an unpredictable order of operations, because the animation playback head remains stopped at the end of the animation for an indiscernably small amount of time, during which the function under it seems to get called every frame. not once. which is such colossal bullshit i can't even imagine why it's taken me this long to realize how fucked up this system is. anyways i have to re-do it now using the AtEnd switch mode and auto-advance for attack/recovery animation nodes. i anticipate this will break some of the logic regarding attacks, so i will have to do a lot of bug fixing/reprogramming to make sure it's working as intended.
on the plus side, it seems like this is a more "proper" way to use the AnimationTree/AnimationStateMachine, but i felt like i had more control over the code when doing function calls as i was.
... on the other hand, this is kind of un-fucking-believable, because i just had the program open, functioning properly. closed it, and re-opened it without changing ANYTHING, and it is now broken again. this type of unpredictability is the worst thing you can encounter, because not only is there seemingly no logical reason for it to exist, there is no logical place to begin looking to debug this sort of absolutely fucking garbage bullshit.
anyways, i THINK i have figured out the AtEnd switch_mod/auto-advance/advance_condition garbage. it works like this:
SwordAttack1, 2 & 3 by default auto-advance to the SwordRecovery AnimationNode (switch_mode: AtEnd) with a default priority of 1. meaning, when an attack animation finishes, by default we travel automatically to the SwordRecovery animation.
the transitions from SwordAttack1 to 2 and from 2 to 3 both have the advance condition, "attack_queued". to access this condition: animationTree.get("parameters/conditions/attack_queued").
before, we checked a Player variable, attack_queued, when we called attack_animation_finished(). now, Player.attack_queued is somewhat vestigal: its purpose now exists to call a setter function when it is changed, and it is this setter function that flags the AnimationTree's advance_condition parameter, "attack_queued", to true. because of this, there is no reason why we can't bypass the player.attack_queued flag altogether and simply set the AnimationTree's attack_queued flag ourselves. but, i suppose the code is more readable this way.
so this is the proper way to use the AnimationStateMachine. i was using a kind of roundabout method that wasn't taking advantage of the AnimationTree's capabilities, because i thought it was a bit too complicated to tackle, and the documentation for it is unfortunately extremely vague. but, i'm learning, it's a process, and it's time-consuming, and it's frustrating, but progress is being made. so in the end, it's good.
on the other hand, the animations played using the old system are bound to be even more buggy, now. i'm not worried about this. it can all be fixed and reintegrated when the animations are complete.
anyways, a brief explanation:
if we press "attack" while in the ATTACK state (eg. during SwordAttack1 animation), we flag self.attack_queued to true, which calls the setter function, set_attack_queued(), which sets the AnimationTree's advance_condition "attack_queued" to true. when the animation finishes, it advances to SwordAttack2 because of the combination of the advance_condition and its auto-advance priority. each attack animation auto-advances to SwordRecovery by default with a priority of 1. the transitions from attack1 to 2 and 2 to 3 have a priority of 0, meaning that transition will be favoured if auto-advance is flagged by the advance_condition. on attack_animation_finished(), we check attack_queued, and set it to false if it's true.
with this new system, the previous problem of being able to queue attacks during attack3 and the 2 bandaid conditions it needed to prevent a softlock should disappear.

---
## [Cenrus/Shiptest](https://github.com/Cenrus/Shiptest)@[031c0866ed...](https://github.com/Cenrus/Shiptest/commit/031c0866ed35af71a3ac4782fe4d6aa9e6464f53)
#### Thursday 2022-02-10 20:03:06 by SweetBlueSylveon

Nanotrasen Deserter Vault Ruin (#732)

* Nanotrasen Deserter Vault Ruin

A ruin based around a Nanotrasen ultra secure vault. It should spawn on the ice planet. This commit adds everything.

* Map Changes

-Replaces Glockroach family with Jack and Jill, Slaughter and Laughter demons.
-Replaces Sniper Rifle with Particle Acceleration Rifle.
-Replaces Sniper Rifle ammo with a single upgraded weapon power cell.
-Adds a sentience potion and cns rebooter implant to vault safe since there were only mats in it otherwise.

* Minor commit

Removes a cybernetic that should have been removed before the last commit.

* Update code/game/area/areas/ruins/icemoon.dm

I'm dumb and didn't realize I did this. Also didn't realize linters was the code checker, so I didn't realize to check the code. I know now! Thanks for the help.

Co-authored-by: Zephyr <12817816+ZephyrTFA@users.noreply.github.com>

* Adds the knight gear design disk.

Adds the "magical disk of smithing" to the safe.

* Unmodularizes your Modularization

Moves the datum to an unmodularized folder.

Co-authored-by: Zephyr <12817816+ZephyrTFA@users.noreply.github.com>

---
## [ivg/bap](https://github.com/ivg/bap)@[368286012d...](https://github.com/ivg/bap/commit/368286012d31312cfc785d940dd89e1f882c7bff)
#### Thursday 2022-02-10 20:41:20 by Ivan Gotovchits

relaxes the Apply.binop function to allow not well-typed operations (#1422)

We are not changing the typing rules of BIL or Core Theory, but
providing a well-defined behavior for application of binary operations
on bitvectors with unequal lengths. Before that, the behavior was
undefined and the precondition of the function was clearly specifying
that the inputs should be of equal lengths.

The new behavior is to promote words to the equal length, (much like
in C, which implicitly coerces the narrow type to the wider type).

The motivation is simple. It is hard to ensure this precondition in
general. Yes, our lifters produce well-typed code, so there are no
issues when we interpret code from the lifters. But we also have a lot
of different interpreters, extensible via primitives. And those
interpreters sometimes don't have any means (or at least efficient
means) to ensure that all binary operations have matching widths. A
concrete example of such interpreter is Veri that is used for
bi-interpretation of traces and BIL programs for
verification. Sometimes, the tracers organically produce ill-typed
code, as they rely on their own typing rules. For example, qemu-based
tracer just represent every register (including flags) and every
number (including bools) with a word-sized bitvector. We still want to
be able to perform calculations on such inputs and, to be honest, the
results are quite well-defined, no hacks required. In other words,
this change tries to follow the robustness principle, i.e., "be
conservative in what you do, be liberal in what you accept from
others". Our lifters, i.e., the code that we produce, are still much
conservative, but our interpreters tend to be more liberal and
understand even the ill-typed code, especially if this code has clear
semantics.

---
## [kollibroman/SpotifyCLI](https://github.com/kollibroman/SpotifyCLI)@[9c40df78b7...](https://github.com/kollibroman/SpotifyCLI/commit/9c40df78b710a97467527bf1798d19de563f626c)
#### Thursday 2022-02-10 21:01:48 by Filip

Finished All basic functions

Fix for forgotten bugs

Actions update

Fixing errors with actions

Stuggling

This commit will be merged but yes

Why this is not working

Meh

this will be merged with others

pls kill me

ugh

my creativity is dying

MERGING

Fighting with actions

Still fighting

pppppp

ooooo

:DDDD

sbcabviuwbl

fucking merge me

mehhhhh

fuck this

pain

final try

arghhhhh

fuck me

kkkkkkkkkk

LAST ONE

Fully fixed actions

now it works

bullshit

pain

---
## [willior/Action_RPG_1](https://github.com/willior/Action_RPG_1)@[00f7d41c71...](https://github.com/willior/Action_RPG_1/commit/00f7d41c717e1690a2db8539d3ad07aa5a651045)
#### Thursday 2022-02-10 21:24:47 by willior

adjusting enemy collisions

the various enemy collisions are not set up in a very organized way. sometimes, we transform the position.y of the hitbox(area), sometimes its the hitbox's child(collisionshape), etc. there needs to be a uniform fashion in which these things are set up. this needs to be fixed across all enemies.
also a weird thing occurs where changing targets on the FormulaTargetScreen does not always make the target/reticle red as it should. i don't know why this happens, because again, it only happens occasionally. it's not predictable and follows now logical pattern. which, of course, is fucking bullshit and a fucking waste of time trying to figure out why the fuck it happens randomly.
also kind of realized that the hide/show_outline() Global methods might be... completely useless? since we can hide/show  outlines directly from the player. i think i did this because sometimes the outline node on objects exists in a different child pattern than other types of objects, eg. ingredient pickups vs. enemies. either way it's a simple fix.

---
## [freedesktop/NetworkManager](https://github.com/freedesktop/NetworkManager)@[c65e586624...](https://github.com/freedesktop/NetworkManager/commit/c65e586624a9487d42603598c5e3e6115a0f99fe)
#### Thursday 2022-02-10 21:27:10 by Thomas Haller

platform: support IPv6 mulitpath routes and fix cache inconsistency

Background:
-----------

Route are hard. We have NMPlatform which is a cache of netlink objects.
That means, we have a hash table and we cache objects based on some
identity (nmp_object_id_equal()). So those objects must have some immutable,
indistinguishable properties that determine whether an object is the
same a different one.

For routes and routing rules, this identifying property is basically a subset
of the attributes (but not all!). That makes it very hard, because tomorrow
kernel could add an attribute that becomes part of the identity, and NetworkManager
wouldn't recognize it, resulting in cache inconsistency by wrongly
thinking two different routes are one and the same. Anyway.

The other point is that we rely on netlink events to maintain the cache.
So when we receive a RTM_NEWROUTE we add the object to the cache, and
delete it during RTM_DELROUTE. When you do `ip route replace`, kernel
might replace a (different!) route, but only send one RTM_NEWROUTE message.
We handle that by somehow finding the route that was replaced/deleted. It's
ugly. Did I say, that routes are hard?

Also, for IPv4 routes, multipath attributes are just a part of the
routes identity. That is, you add two different routes that only differ
by their multipath list, and then kernel does as you would expect.
NetworkManager does not support IPv4 multihop routes and just ignores
them. As the multipath attribute is part of the identity of an IPv4
route, we can get away with pretending that multipath IPv4 routes don't
exist.

Not so for IPv6. When you add (`ip route append`) an IPv6 route that is
identical to an exist route -- except their multipath attribute -- then it
behaves as if the existing route was modified and the result is the
merged route with more next-hops. Note that in this case kernel will
only send a RTM_NEWROUTE message with the full multipath list. If we
would treat the multipath list as part of the route's identity, this
would be as if kernel deleted one routes and created a different one (the
merged one), but only sending one notification. It would be nightmare to
find out which route was thereby replaced.
Likewise, when you delete a route, then kernel will "subtract" the
next-hop and sent a RTM_DELROUTE notification only about the next-hop that
was deleted. To handle that, you would have to find the full multihop
route, and replace it with the subtracted result.

NetworkManager so far ignored IPv6 routes with more than one next-hop, this
means you can start with one single-hop route (that NetworkManger sees
and has in the platform cache). Then you create a similar route (only
differing by the next-hop). Kernel will merge the routes, but not notify
NetworkManager that the single-hop route is not longer a single-hop
route. This can easily cause a cache inconsistency and subtle bugs. For
IPv6 we MUST handle multihop routes.

Kernels behavior makes little sense, if you expect that routes have an
immutable identity and want to get notifications about addition/removal.
We can however make sense by it by pretending that all IPv6 routes are
single-hop! With only the twist that a single RTM_NEWROUTE notification
might notify about multiple routes at the same time. This is what the
patch does.

The Patch
---------

Now one RTM_NEWROUTE message can contain multiple IPv6 routes
(NMPObject). That would mean that nmp_object_new_from_nl() needs to
return a list of objects. But it's not implemented that way. Instead,
we still call nmp_object_new_from_nl(), and the parsing code can
indicate that there is something more, indicating the caller to call
nmp_object_new_from_nl() again in a loop to fetch more objects.

In practice, I think all RTM_DELROUTE messages for IPv6 routes are
single-hop. Still, we implement it to handle also multi-hop messages the
same way.

Note that we just parse the netlink message again from scratch. The alternative
would be to parse the first object once, and then clone the object and
only update the next-hop. That would be more efficient, but probably
harder to understand/implement.

https://bugzilla.redhat.com/show_bug.cgi?id=1837254#c20

---
## [EmanuelCN/android_kernel_lge_sdm845](https://github.com/EmanuelCN/android_kernel_lge_sdm845)@[865dd13861...](https://github.com/EmanuelCN/android_kernel_lge_sdm845/commit/865dd13861034e80db3de1baebed353adc08c0c0)
#### Thursday 2022-02-10 21:31:58 by George Spelvin

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

---
## [StephenCleary/comments.stephencleary.com](https://github.com/StephenCleary/comments.stephencleary.com)@[b2e4bcca53...](https://github.com/StephenCleary/comments.stephencleary.com/commit/b2e4bcca53e337ddf05d2ba23b414ff4eac89def)
#### Thursday 2022-02-10 23:23:58 by Comment Bot

(Staticman) joa: http://drsantyjatto.wixsite.com/website
 increase your penis sizes really matters in a relationship, i was facing difficulties in all my sex life i was humiliated because of my small penis and premature ejaculation problem i couldn't satisfy my partner during sex, i was so ashamed of my self until i was doing some research on bigger penis i saw some articles about this dr called santy jatto that he has remedy that can increase penis from 3 to 9 inches my own was 5 inches when erect i quickly contacted him through his whatsapp number on the articles he respond to me and send me the remedy through DHL, my first experience during the first week of usage was awesome right now i have a bigger penis 9.5 inches my sex partner do enjoyed me more during sex all thanks to dr santy jatto contact him now via whatsapp +2348145243120 email dr.santyjatto@ gmail. com    He has cure for all sickness and diseases and solutions to relationship problems like getting your ex lover back, divorce spell, death spell to avenge your enemies.
               SICKNESS AND DISEASES
 1 ALS
2 diabetes cure
3 premature ejaculation
4 herpes cure
5 warts cure
6 HPV cure
7 fibroid
8 penis enlargement
9 Muscular dystrophy
10 cancer

https://blog.stephencleary.com/2012/07/dont-block-on-async-code.html#comment-85292040-8ac8-11ec-8a78-e5a5e9f0bdc9

---
## [EmanuelCN/android_kernel_lge_sdm845](https://github.com/EmanuelCN/android_kernel_lge_sdm845)@[85cff46137...](https://github.com/EmanuelCN/android_kernel_lge_sdm845/commit/85cff46137376acaba0eb76f5936a8a53f0faec4)
#### Thursday 2022-02-10 23:24:53 by George Spelvin

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

---

