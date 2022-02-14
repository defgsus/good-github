## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-02-13](docs/good-messages/2022/2022-02-13.md)


1,310,648 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,310,648 were push events containing 1,889,309 commit messages that amount to 114,735,392 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 31 messages:


## [jakosimov/shoestringMergeSort](https://github.com/jakosimov/shoestringMergeSort)@[b4b47f98d0...](https://github.com/jakosimov/shoestringMergeSort/commit/b4b47f98d0a150f665323adca5e8c2e759cd75b4)
#### Sunday 2022-02-13 00:10:33 by xt0r3

Dissed Rokas in the comments of plotDemand
This is very rude of me and I am a horrible person.
I hate myself.
I hate you too.

---
## [Ironnhawk/Skyrat-tg](https://github.com/Ironnhawk/Skyrat-tg)@[d504fe76f4...](https://github.com/Ironnhawk/Skyrat-tg/commit/d504fe76f4935518b45f3ba1ec6d935af5f16b55)
#### Sunday 2022-02-13 00:41:33 by SkyratBot

[MIRROR] Fixes harddels in pinned module code, cleans up a musty pattern that I want to die [MDB IGNORE] (#11319)

* Fixes harddels in pinned module code, cleans up a musty pattern that I want to die (#64674)

* Please stop typecasting target, noooooooooooooooooo

* Fixes harddels in pinned module code

The logic for pinned modules was intentionally hanging references to the
mob that pinned the action button. I have depression.

The pinned_to list also was never fully cleared, but that would have
just exasperated the issue. I've converted its use of mobs to refs, and
its use of the module var into something better managed

(Friendly reminder that actions will persist in your nightmares forever
unless they are manually qdel'd, this code wasn't doing that.

Also cleaned up how the pinned_to list is managed, hopefully it's a bit
more action centered now

* Fixes harddels in pinned module code, cleans up a musty pattern that I want to die

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [Amrabol/tgstation](https://github.com/Amrabol/tgstation)@[a2fa7799f3...](https://github.com/Amrabol/tgstation/commit/a2fa7799f3f27025b43413314c34f595f4316cac)
#### Sunday 2022-02-13 00:45:00 by Jeremiah

Removes swarmers from the game (#63989)

What the title says. But why?
I generally have a rule when making a contribution, that is "don't make the game less fun"
I'm not salting, I didn't die to a swarmer.
... Yet that's the problem. Swarmers are the griefiest antag in the game, but when you complain that they're annoying or unfun, you're doomed to hear "lol they can't even hurt you though."

WELL THAT ACTUALLY MAKES THEM WORSE. I would rather die to a hundred xenos and space dragons than be forced to untie myself in maintenance for 45 seconds while the shuttle leaves.
Why It's Good For The Game

Unfun game modes should be removed from the game.

    Being griefed by swarmers is annoying
    Playing as a swarmer is not very exciting either. Click on iron.

lastly, because oranges authorized it
Changelog

cl
del: Removes swarmers! The griefiest, lowest fun value antagonist is removed from the game.
/cl

---
## [sunamo/sunamo](https://github.com/sunamo/sunamo)@[e851083d1f...](https://github.com/sunamo/sunamo/commit/e851083d1fba27690e5b1dcf41500fa682f0b6f3)
#### Sunday 2022-02-13 00:55:48 by Radek Jancik

I've always thought that the most extraordinary special effect you could do is to buy a child at the moment of its birth, sit it on a little chair and say, 'You'll have three score years and ten,' and take a photograph every minute. 'And we'll watch you and photograph you for ten years after you die, then we'll run the film.' Wouldn't that be extraordinary? We'd watch this thing get bigger and bigger, and flower to become extraordinary and beautiful, then watch it crumble, decay, and rot.  - Barker, Clive

---
## [jakosimov/shoestringMergeSort](https://github.com/jakosimov/shoestringMergeSort)@[3c5cac9cbd...](https://github.com/jakosimov/shoestringMergeSort/commit/3c5cac9cbdbc324074b6cafd36de9972f75c7375)
#### Sunday 2022-02-13 01:33:11 by xt0r3

I am very nostalgic and I have decided to go to lake Balaton in the summer and spend some time doing only what I feel like doing.
It is going to be amazing.
I love my life.
I love you too.

I removed dissing Rokas.
I also made some modifications to the project and plotting works now.

---
## [ThEyg0wWhEnTheRs/Stockfish](https://github.com/ThEyg0wWhEnTheRs/Stockfish)@[cb9c2594fc...](https://github.com/ThEyg0wWhEnTheRs/Stockfish/commit/cb9c2594fcedc881ae8f8bfbfdf130cf89840e4c)
#### Sunday 2022-02-13 02:41:41 by Tomasz Sobczyk

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
## [GForceTF/tgstation](https://github.com/GForceTF/tgstation)@[906fb0682b...](https://github.com/GForceTF/tgstation/commit/906fb0682bab6a0975b45036001c54f021f58ae7)
#### Sunday 2022-02-13 02:54:41 by necromanceranne

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
## [ncrecc/jumper4real](https://github.com/ncrecc/jumper4real)@[666adf7b7c...](https://github.com/ncrecc/jumper4real/commit/666adf7b7c5372f59a12ae8faf8bfbe3d61dcd46)
#### Sunday 2022-02-13 03:38:54 by wibi

lots of stuff holy shit

added new built-in "showcase" levelset that describes a lot about how the game works and contains most currently present features
level is now its own class
levels now reset when you die via holding a "base" version of themselves and cloning it whenever they'd die, instead of directly reading from the level file again after death. this could potentially be useful for really big levels
added "magic number" tiles, which are invisible and do nothing in-game, but determine what state an object should be in when the level begins
win tiles are now two separate tiles: the win tile itself, and a magic number on the layer above that determines which exit to take (win defaults to exit #1 if there's no magic number)
win tiles on borders now make the border nonsolid in that spot and require ogmo to go through it to win
added a rudimentary "past edge scan" to mobtools
ogmos on borders now have animations where they enter the level from off-screen
whether or not an ogmo spawns into a level can be controlled by magic numbers. taking exit #n to level foo means that only ogmos with the magic number n (or no number whatsoever) will spawn in foo
added hint blocks/textboxes, and "hints" section to level files
objects can now pass a function to collisionscans that must return true in order for an obstruction to be considered
gost blocks now collide with other gost blocks
gost blocks can now "duck"; they don't change height but will stop moving
added "interact" button (defaults to A); update or delete controls.txt in appdata/roaming/love/jumper4real for it to work
solid objects now always render above non-solid objects
added doors, which are like win tiles but you have to interact with them
resprited some of the slope tiles to not just be half of the wall graphic
added "darkness" and "lightness" tiles
pressing r no longer makes the death sound once for every player in the level (new function, audio.playsfxonce(), that plays the requested sound effect once audio updates again and ignores duplicate requests)
audio now updates *after* the current state updates
levelsets now have their levels inside a "levels" subfolder
changed "save/load" textfield in editor to be a separate "levelset" field and a "level" field
textfields can now have forbidden characters; levelset/level textfields no longer allow you to type characters that are problematic on windows (and levelset textfield doesn't allow you to type /)
changed ctrl+s to save levels to ctrl+shift+s because i got paranoid about saving a level as something instead of loading it
window no longer changes size when testing from editor (it got annoying and slow since love actually restarts the window every time you change its size)
scroll wheel can now be used to rotate symbols in the editor, in addition to , and .
typing in a valid cheat now makes a sound
added a few more cheats
Added more facts, because really, where can you go wrong with more facts?
fixed "todo: you died, but you're already dead?" - game events like death would occasionally occur twice due to relying on the level being swapped out before they can occur again  ocasionally the game managed to get an update out before the swap actually occurred.. this has been fixed by "freezing" the active level when a level change is queued
moved "docs" to "randomcrap" and put legend.txt in a new "documentation" folder
removed bootsy loop.ogg and roller 1 loop.ogg for now since they're pretty large and never used
and other changes, maybe. there were a lot of changes here wow

-bert

---
## [PhilRunninger/nvim_config](https://github.com/PhilRunninger/nvim_config)@[9997283eac...](https://github.com/PhilRunninger/nvim_config/commit/9997283eac14ca664dcae78715b04af5068daba4)
#### Sunday 2022-02-13 04:09:13 by PhilRunninger

Use background=dark on Windows. Don't show splash screen on startup.

Neovim is apparently not getting the terminal's background color when in
Windows (works fine in iTerm on Mac), so always set to dark. If I want a
light background, I can use my other keyboard shortcuts: Win+Shift+L
(Windows Terminal: change to Tango Light palette) and `yob`
(vim-unimpaired: toggle background setting).

As cool as they are, my splash screens are kinda annoying, so I
commented out the autocmd VimEnter.

---
## [cpdt/NorthstarLauncher](https://github.com/cpdt/NorthstarLauncher)@[db0af63704...](https://github.com/cpdt/NorthstarLauncher/commit/db0af63704a6fbc57e80a9db01bbc01b79339d9f)
#### Sunday 2022-02-13 06:05:34 by Emma Miler

Added code for chathooks

This may not seem like much to a passing observer, but this commit took me 30 hours of blood, sweat, tears, IDA debugging, server crashes, and insanity.

---
## [osamuaoki/qmk_firmware](https://github.com/osamuaoki/qmk_firmware)@[0d4e85f4a1...](https://github.com/osamuaoki/qmk_firmware/commit/0d4e85f4a13da9dad17c334917f59d17139d94b1)
#### Sunday 2022-02-13 10:30:18 by Osamu Aoki

Format update and note

Note: Although these 2 lines should move to // Magic section, doinso may
cause trouble.  (My development time vague memory:  Back slash and back
space became swapped.  Since others had MAGIC_TOGGLE_CONTROL_CAPSLOCK
here, I assume this is the least invasive (but ugly patch.)

Signed-off-by: Osamu Aoki <osamu@debian.org>

---
## [mosra/magnum](https://github.com/mosra/magnum)@[efa02d46df...](https://github.com/mosra/magnum/commit/efa02d46df690dbb1b539b0b04adc86566fd4d5f)
#### Sunday 2022-02-13 11:15:57 by Vladimír Vondruš

Trade: refresh MeshData docs slightly.

It was rather discouraging to start "Basic usage" with a boring-ass long
snippet. On the other hand showing just compile() first would lead
people to think it's all some opaque magic, so trying to balance that a
bit.

Also why the hell was the compile() snippet showing the horrendous GL
way of specifying attribute formats? This is not great either but at
least not redundant.

---
## [Koi-3088/ForkBot.NET](https://github.com/Koi-3088/ForkBot.NET)@[0bc27c13a7...](https://github.com/Koi-3088/ForkBot.NET/commit/0bc27c13a750c68a86eaa7da3959069406849cd9)
#### Sunday 2022-02-13 12:13:07 by Koi

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
## [E-MonaRhg/Shiptest](https://github.com/E-MonaRhg/Shiptest)@[5e29827ceb...](https://github.com/E-MonaRhg/Shiptest/commit/5e29827cebbb7cd08d4bf5b210675526f324bf6d)
#### Sunday 2022-02-13 13:24:52 by Zephyr

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
## [crimsonthunder/IronKernel](https://github.com/crimsonthunder/IronKernel)@[54d95d35b8...](https://github.com/crimsonthunder/IronKernel/commit/54d95d35b845eff849f2979e42c81d0fcce80edb)
#### Sunday 2022-02-13 13:33:32 by Thomas Gleixner

tick: Upstream fixes

 * Addresses the issue of timers being scheduled on offline CPUs.

tick: Don't invoke tick_nohz_stop_sched_tick() if the cpu is offline

commit 5b39939a4 (nohz: Move ts->idle_calls incrementation into strict
idle logic) moved code out of tick_nohz_stop_sched_tick() and missed
to bail out when the cpu is offline. That's causing subsequent
failures as an offline CPU is supposed to die and not to fiddle with
nohz magic.

Return false in can_stop_idle_tick() if the cpu is offline.

Reported-and-tested-by: Jiri Kosina <jkosina@suse.cz>
Reported-and-tested-by: Prarit Bhargava <prarit@redhat.com>
Cc: Frederic Weisbecker <fweisbec@gmail.com>
Cc: Borislav Petkov <bp@alien8.de>
Cc: Tony Luck <tony.luck@intel.com>
Cc: x86@kernel.org
Link: http://lkml.kernel.org/r/alpine.LFD.2.02.1305132138160.2863@ionos
Signed-off-by: Thomas Gleixner <tglx@linutronix.de>

timers: Consolidate base->next_timer update

Another bunch of mindlessly copied code. All callers of
internal_add_timer() except the recascading code updates
base->next_timer.

Move this into internal_add_timer() and let the cascading code call
__internal_add_timer().

Signed-off-by: Thomas Gleixner <tglx@linutronix.de>
Cc: Peter Zijlstra <peterz@infradead.org>
Cc: Gilad Ben-Yossef <gilad@benyossef.com>
Cc: Frederic Weisbecker <fweisbec@gmail.com>
Link: http://lkml.kernel.org/r/20120525214819.189946224@linutronix.de

timers: Create detach_if_pending() and use it

Most callers of detach_timer() have the same pattern around
them. Check whether the timer is pending and eventually updating
base->next_timer.

Create detach_if_pending() and replace the duplicated code.

Signed-off-by: Thomas Gleixner <tglx@linutronix.de>
Cc: Peter Zijlstra <peterz@infradead.org>
Cc: Gilad Ben-Yossef <gilad@benyossef.com>
Cc: Frederic Weisbecker <fweisbec@gmail.com>
Link: http://lkml.kernel.org/r/20120525214819.131246037@linutronix.de

timers: Add accounting of non deferrable timers

The code in get_next_timer_interrupt() is suboptimal as it has to run
through the cascade to find the next expiring timer. On a completely
idle core we should only do that when there is an active timer
enqueued and base->next_timer does not give us a fast answer.

Add accounting of the active timers to the now consolidated
attach/detach code. I deliberately avoided sanity checks because the
code is fully symetric and any fiddling with timers w/o using the API
functions will lead to cute explosions anyway. ulong is big enough
even on 32bit and if we really run into the situation to have more
than 1<<32 timers enqueued there, then we are definitely not in a
state to go idle and run through that code.

This allows us to fix another shortcoming of get_next_timer_interrupt().

Signed-off-by: Thomas Gleixner <tglx@linutronix.de>
Cc: Peter Zijlstra <peterz@infradead.org>
Cc: Gilad Ben-Yossef <gilad@benyossef.com>
Cc: Frederic Weisbecker <fweisbec@gmail.com>
Link: http://lkml.kernel.org/r/20120525214819.236377028@linutronix.de

timers: Improve get_next_timer_interrupt()

Gilad reported at

 http://lkml.kernel.org/r/1336056962-10465-2-git-send-email-gilad@benyossef.com

"Current timer code fails to correctly return a value meaning that
 there is no future timer event, with the result that the timer keeps
 getting re-armed in HZ one shot mode even when we could turn it off,
 generating unneeded interrupts.

 What is happening is that when __next_timer_interrupt() wishes
 to return a value that signifies "there is no future timer
 event", it returns (base->timer_jiffies + NEXT_TIMER_MAX_DELTA).

 However, the code in tick_nohz_stop_sched_tick(), which called
 __next_timer_interrupt() via get_next_timer_interrupt(),
 compares the return value to (last_jiffies + NEXT_TIMER_MAX_DELTA)
 to see if the timer needs to be re-armed.

 base->timer_jiffies != last_jiffies and so tick_nohz_stop_sched_tick()
 interperts the return value as indication that there is a distant
 future event 12 days from now and programs the timer to fire next
 after KTIME_MAX nsecs instead of avoiding to arm it. This ends up
 causing a needless interrupt once every KTIME_MAX nsecs."

Fix this by using the new active timer accounting. This avoids scans
when no active timer is enqueued completely, so we don't have to rely
on base->timer_next and base->timer_jiffies anymore.

Change-Id: I5226bcca6ef059260bd41d2bce6090ecbc2492fa
Reported-by: Gilad Ben-Yossef <gilad@benyossef.com>
Signed-off-by: Thomas Gleixner <tglx@linutronix.de>
Cc: Peter Zijlstra <peterz@infradead.org>
Cc: Frederic Weisbecker <fweisbec@gmail.com>
Link: http://lkml.kernel.org/r/20120525214819.317535385@linutronix.de

---
## [v4lkyr/whyred](https://github.com/v4lkyr/whyred)@[427cec6948...](https://github.com/v4lkyr/whyred/commit/427cec6948fd852a4a4f1287dd636dc6f9e81829)
#### Sunday 2022-02-13 14:15:47 by Peter Zijlstra

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
Signed-off-by: v4lkyr <valkyr23@gmail.com>

---
## [RandomTales/Naruto_Ninpou](https://github.com/RandomTales/Naruto_Ninpou)@[41313d9d7e...](https://github.com/RandomTales/Naruto_Ninpou/commit/41313d9d7e350d8192fb024fec099d317638e39a)
#### Sunday 2022-02-13 14:26:54 by AkatsukiGhost

Random

Haven't Done:

- Fixed transformation silence bug
- Fixed permanently paused unit bug
- Fixed Sasori ring gold cooldown being global
- Fixed Onooki Q movespeed issue
- Fixed bug with -autobuy not doing the correct stat build if you used -swap, type -autonew to refresh after swap and then -autobuy
- Fixed Edo Tobirama being paused longer then he should in his W
- Fixed Yata Mirror pause still pausing if the invulnerability is purged
- Added Light Attack passive to the perfect ultimate weapons
- Changed Spirit Orbs damages or adjusted % a little (spirit effects are all the same for Ultimate / Elemental Weapons)
	- Splash Damage (passive, 50 damage bonus in 300 radius)
	- Bash (passive, 15% chance to stun for 1s)
	- Chilling Attack (passive, 50% slow for 1.5s)
	- Corrosive Attack (passive, -10 armor)
	- Chain Lightning (passive, 5% chance to deal 300 damage)
	- Critical Strike (passive, 15% to deal 6 x damage)
	- Light Attack (passive, 10% chance to silence for 1s)
- Dark Totsuka now causes -10 armor on auto attacks
- Fixed Executioner Blade being unable to get picked up from your box
- Thunder Totsuka now has a 5% chance to proc chain lightning
- Heaven Stone corrosive attacks from -25 to -15
- Reduced Shinigami Mask corrosive attacks from -15 to -10

---
## [karthik990/kernel_oneplus_sm8350](https://github.com/karthik990/kernel_oneplus_sm8350)@[d2be9e450a...](https://github.com/karthik990/kernel_oneplus_sm8350/commit/d2be9e450aa7bd0aa01f58c731ba8ca81c1c5980)
#### Sunday 2022-02-13 15:22:11 by alk3pInjection

techpack: display: Handle dim for udfps

Apparently, los fod impl is better than udfps cuz it
has onShow/HideFodView hook, which allows us to toggle
dimlayer seamlessly.

Since udfps only partially supports the former one,
we'd better kill dim in kernel. This is kinda a hack
but it works well, bringing perfect fod experience
back to us.

Also implement a panel status check to ensure that
the dim layer dies when display is off.

Co-authored-by: Art_Chen <Chenxy0201@qq.com>
Change-Id: I14d028a821e4a776bc62feb5836b3fe012bc808e

---
## [ammarfaizi2/linux-block](https://github.com/ammarfaizi2/linux-block)@[d37d5fcbbc...](https://github.com/ammarfaizi2/linux-block/commit/d37d5fcbbc8abca07cf77cdb787132666b07d321)
#### Sunday 2022-02-13 16:22:03 by Jason A. Donenfeld

random: use max-period LFSR for irq accumulation

>>>  WORK IN PROGRESS, NOT YET FOR SUBMISSION, DO NOT REVIEW  <<<
>>> I may well never submit this. Disregard all of the below. <<<

The current fast_mix() function is a piece of classic mailing list
crypto, where it just sort of sprung up without a lot of real analysis
of what precisely it was accomplishing. As a permutation of only two
rounds, there are some easily searchable differential trails in it, and
as a means of preventing malicious irqs, it completely fails, since it
xors new data into the entire state every time. It can't really be
analyzed as a random permutation, because it clearly isn't, and it
can't be analyzed as an interesting linear algebraic structure either,
because it's also not that. There really is very little one can say
about it in terms of entropy accumulation. It might diffuse bits, some
of the time, maybe, we hope, I guess. But for the most part, it fails to
accomplish anything concrete.

As a reminder, the simple goal of add_interrupt_randomness() is to
simply accumulate entropy until ~64 interrupts have elapsed, and then
dump it into the main input pool, which uses a cryptographic hash.

It would be nice to have something cryptographically strong in this
context, in case a malicious irq compromises a per-cpu fast pool within
the 64 interrupts / 1 second window, and then inside of that same window
somehow can control its return address and cycle counter, even if that's
a bit far fetched. However with a very CPU cycle limited budget,
actually doing that remains an active research project (and perhaps
there'll be something useful for Linux to come out of it). And while the
abundance of caution would be nice, this isn't *currently* the security
model, and we don't yet have a fast enough solution to make it our
security model. Plus there's not exactly a pressing need to do that.
(And for the avoidance of doubt, the actual cluster of 64 accumulated
irqs still gets dumped into our cryptographically secure input pool.)

So, for now we are going to stick with the existing irq security model,
which assumes that each cluster of 64 irq cycle counter samples are
mostly non-malicious and not colluding with an infoleaker. With this as
our goal, we can then endeavor to simply accumulate entropy linearly,
discarding the least amount of it, and make sure that accumulation is
sound, unlike the current fast_mix().

It turns out that this security model is also the trade off that other
operating systems have taken. The NT kernel, for example, uses something
very simple to accumulate entropy in interrupts, `x = ror32(x, 5) ^ m`.
Dodis et al. analyzed this in <https://eprint.iacr.org/2021/523>, and
found that rotation by 7 would have been better than 5, but that
otherwise, simple linear constructions like this can be used as an
entropy collector.  However, when considering this for our four-word
accumulation, versus NT's one-word, we run into potential problems
because the words don't contribute to each other, and some may well be
fixed, which means we'd need something to schedule on top.

However, a simple LFSR actually serves the same purpose as the single
word rotate-xor, but easily extends to larger state sizes, and has the
advantage that it only has the trivial invariant subspace, rather than
quite a few invariant subspaces like rotate-xor, which means we benefit
from the analysis of <https://eprint.iacr.org/2021/1002>, which gives
proofs that these types of linear structures make very good entropy
accumulators, arguably better than rotate-xor.

So this commit chooses a very fast and high diffusion max-period LFSR,
implemented in a Feistel-like fashion, which pipelines quite well. On an
i7-11850H, this takes 35 cycles, versus the original's 65 cycles.
(Though, as a note for posterity: if later this is replaced with some
sort of cryptographic hash function, I'll still be keeping 65 cycles as
my target 😋.) This MAGMA script, <https://xn--4db.cc/V1nFTMYE/magma>,
or the equivalent Sage script, <https://xn--4db.cc/LpZhTYIh/sage>,
proves that this construction does indeed yield a max-period LFSR with a
primitive polynomial for our 4 pool words.

I mention "high diffusion" above, because that apparently was the single
discernible design goal of the original fast_mix(), even though that
didn't wind up helping anything with it. Nonetheless, we take care to
choose an LFSR with pretty high diffusion, perhaps even higher than the
original fast_mix(), which we can quantify by computing that the minimum
weight of the linear code is 10, versus around 8 if we treat the
original fast_mix() as linear as well. In other words, we probably don't
regress at all from a perspective of diffusion, even if it's not really
a design goal anyway.

In sum, the security model of this is unchanged from before, yet its
implementation now fixes that model much more rigorously.  Plus the
performance is better, which perhaps matters in irq context.

As a final note, the previous fast_mix() was contributed by an anonymous
author, which, I've been told, has made some legally-minded people a bit
uncomfortable and is also against the kernel project's "real name"
policy.

Cc: Dominik Brodowski <linux@dominikbrodowski.net>
Cc: Theodore Ts'o <tytso@mit.edu>
Cc: Greg Kroah-Hartman <gregkh@linuxfoundation.org>
Signed-off-by: Jason A. Donenfeld <Jason@zx2c4.com>

---
## [Michaelleojacob/cv-project](https://github.com/Michaelleojacob/cv-project)@[2e1bd66ddf...](https://github.com/Michaelleojacob/cv-project/commit/2e1bd66ddfbdcba4e7774eca43fb71d3c7c8499f)
#### Sunday 2022-02-13 16:36:18 by Michael

I think i'm going to call it a wrap for now.

I would like to add more placeholders, such as having placeholders for social media links, and an example project and experience in the preview. But honestly i'm so over this project I can't be bothered. I would absolutely want to refactor my code for readability and re do the file structure if I were to keep going. As far as making the place holders, Those are things I have already done, so it's just a matter of redoing them.

---
## [ammarfaizi2/linux-block](https://github.com/ammarfaizi2/linux-block)@[fcef38efb0...](https://github.com/ammarfaizi2/linux-block/commit/fcef38efb054afc431c0dc16f032f42346c5c179)
#### Sunday 2022-02-13 16:51:56 by Jason A. Donenfeld

random: use max-period LFSR for irq accumulation

>>>  WORK IN PROGRESS, NOT YET FOR SUBMISSION, DO NOT REVIEW  <<<
>>> I may well never submit this. Disregard all of the below. <<<

The current fast_mix() function is a piece of classic mailing list
crypto, where it just sort of sprung up without a lot of real analysis
of what precisely it was accomplishing. As a permutation of only two
rounds, there are some easily searchable differential trails in it, and
as a means of preventing malicious irqs, it completely fails, since it
xors new data into the entire state every time. It can't really be
analyzed as a random permutation, because it clearly isn't, and it
can't be analyzed as an interesting linear algebraic structure either,
because it's also not that. There really is very little one can say
about it in terms of entropy accumulation. It might diffuse bits, some
of the time, maybe, we hope, I guess. But for the most part, it fails to
accomplish anything concrete.

As a reminder, the simple goal of add_interrupt_randomness() is to
simply accumulate entropy until ~64 interrupts have elapsed, and then
dump it into the main input pool, which uses a cryptographic hash.

It would be nice to have something cryptographically strong in this
context, in case a malicious irq compromises a per-cpu fast pool within
the 64 interrupts / 1 second window, and then inside of that same window
somehow can control its return address and cycle counter, even if that's
a bit far fetched. However with a very CPU cycle limited budget,
actually doing that remains an active research project (and perhaps
there'll be something useful for Linux to come out of it). And while the
abundance of caution would be nice, this isn't *currently* the security
model, and we don't yet have a fast enough solution to make it our
security model. Plus there's not exactly a pressing need to do that.
(And for the avoidance of doubt, the actual cluster of 64 accumulated
irqs still gets dumped into our cryptographically secure input pool.)

So, for now we are going to stick with the existing irq security model,
which assumes that each cluster of 64 irq cycle counter samples are
mostly non-malicious and not colluding with an infoleaker. With this as
our goal, we can then endeavor to simply accumulate entropy linearly,
discarding the least amount of it, and make sure that accumulation is
sound, unlike the current fast_mix().

It turns out that this security model is also the trade off that other
operating systems have taken. The NT kernel, for example, uses something
very simple to accumulate entropy in interrupts, `x = ror32(x, 5) ^ m`.
Dodis et al. analyzed this in <https://eprint.iacr.org/2021/523>, and
found that rotation by 7 would have been better than 5, but that
otherwise, simple linear constructions like this can be used as an
entropy collector.  However, when considering this for our four-word
accumulation, versus NT's one-word, we run into potential problems
because the words don't contribute to each other, and some may well be
fixed, which means we'd need something to schedule on top. In addition,
this works for 2-monotone distributions, which the cycle counter is, but
not the registers and return addresses that we're also capturing.
(Whether capturing anything beyond the cycle counter in the interrupt
handler is even adding much is a question for a different time.)

However, a simple LFSR actually serves the same purpose and beyond, but
easily extends to larger state sizes and more complex distributions.
Importantly, it has the advantage that it only has the trivial invariant
subspace (0 -> 0), rather than quite a few invariant subspaces like
rotate-xor, which means we benefit from the analysis of
<https://eprint.iacr.org/2021/1002>, which gives proofs that these types
of linear structures make very good entropy accumulators.

So this commit chooses a very fast and high diffusion max-period LFSR,
implemented in a Feistel-like fashion, which pipelines quite well. On an
i7-11850H, this takes 35 cycles, versus the original's 65 cycles.
(Though, as a note for posterity: if later this is replaced with some
sort of cryptographic hash function, I'll still be keeping 65 cycles as
my target 😋.) This MAGMA script, <https://xn--4db.cc/V1nFTMYE/magma>,
or the equivalent Sage script, <https://xn--4db.cc/LpZhTYIh/sage>,
proves that this construction does indeed yield a max-period LFSR with a
primitive polynomial for our 4 pool words.

I mention "high diffusion" above, because that apparently was the single
discernible design goal of the original fast_mix(), even though that
didn't wind up helping anything with it. Nonetheless, we take care to
choose an LFSR with pretty high diffusion, perhaps even higher than the
original fast_mix(), which we can quantify by computing that the minimum
weight of the linear code is 10, versus around 8 if we treat the
original fast_mix() as linear as well. In other words, we probably don't
regress at all from a perspective of diffusion, even if it's not really
a design goal anyway.

In sum, the security model of this is unchanged from before, yet its
implementation now fixes that model much more rigorously. Plus the
performance is better, which perhaps matters in irq context.

As a final note, the previous fast_mix() was contributed by an anonymous
author, which, I've been told, has made some legally-minded people a bit
uncomfortable and is also against the kernel project's "real name"
policy.

Cc: Dominik Brodowski <linux@dominikbrodowski.net>
Cc: Theodore Ts'o <tytso@mit.edu>
Cc: Greg Kroah-Hartman <gregkh@linuxfoundation.org>
Signed-off-by: Jason A. Donenfeld <Jason@zx2c4.com>

---
## [ammarfaizi2/linux-block](https://github.com/ammarfaizi2/linux-block)@[3d6da9d7d6...](https://github.com/ammarfaizi2/linux-block/commit/3d6da9d7d6d672279cd73c99b117593676b633c0)
#### Sunday 2022-02-13 17:17:15 by Jason A. Donenfeld

random: use linear max-period irq entropy accumulator

>>> WORK IN PROGRESS, NOT YET FOR SUBMISSION, DO NOT REVIEW <<<

The current fast_mix() function is a piece of classic mailing list
crypto, where it just sort of sprung up without a lot of real analysis
of what precisely it was accomplishing. As a permutation of only two
rounds, there are some easily searchable differential trails in it, and
as a means of preventing malicious irqs, it completely fails, since it
xors new data into the entire state every time. It can't really be
analyzed as a random permutation, because it clearly isn't, and it
can't be analyzed as an interesting linear algebraic structure either,
because it's also not that. There really is very little one can say
about it in terms of entropy accumulation. It might diffuse bits, some
of the time, maybe, we hope, I guess. But for the most part, it fails to
accomplish anything concrete.

As a reminder, the simple goal of add_interrupt_randomness() is to
simply accumulate entropy until ~64 interrupts have elapsed, and then
dump it into the main input pool, which uses a cryptographic hash.

It would be nice to have something cryptographically strong in this
context, in case a malicious irq compromises a per-cpu fast pool within
the 64 interrupts / 1 second window, and then inside of that same window
somehow can control its return address and cycle counter, even if that's
a bit far fetched. However with a very CPU cycle limited budget,
actually doing that remains an active research project (and perhaps
there'll be something useful for Linux to come out of it). And while the
abundance of caution would be nice, this isn't *currently* the security
model, and we don't yet have a fast enough solution to make it our
security model. Plus there's not exactly a pressing need to do that.
(And for the avoidance of doubt, the actual cluster of 64 accumulated
irqs still gets dumped into our cryptographically secure input pool.)

So, for now we are going to stick with the existing irq security model,
which assumes that each cluster of 64 irq cycle counter samples are
mostly non-malicious and not colluding with an infoleaker. With this as
our goal, we can then endeavor to simply accumulate entropy linearly,
discarding the least amount of it, and make sure that accumulation is
sound, unlike the current fast_mix().

It turns out that this security model is also the trade off that other
operating systems have taken. The NT kernel, for example, uses something
very simple to accumulate entropy in interrupts, `x = ror32(x, 5) ^ m`.
Dodis et al. analyzed this in <https://eprint.iacr.org/2021/523>, and
found that rotation by 7 would have been better than 5, but that
otherwise, simple linear constructions like this can be used as an
entropy collector.  However, when considering this for our four-word
accumulation, versus NT's one-word, we run into potential problems
because the words don't contribute to each other, and some may well be
fixed, which means we'd need something to schedule on top. In addition,
this works for 2-monotone distributions, which the cycle counter is, but
not the registers and return addresses that we're also capturing.
(Whether capturing anything beyond the cycle counter in the interrupt
handler is even adding much is a question for a different time.)

However, a simple LFSR actually serves the same purpose and beyond, but
easily extends to larger state sizes and more complex distributions.
Importantly, it has the advantage that it only has the trivial invariant
subspace (0 -> 0), rather than quite a few invariant subspaces like
rotate-xor, which means we benefit from the analysis of
<https://eprint.iacr.org/2021/1002>, which gives proofs that these types
of linear structures make very good entropy accumulators.

So this commit chooses a very fast and high diffusion max-period LFSR,
implemented in a Feistel-like fashion, which pipelines quite well. On an
i7-11850H, this takes 35 cycles, versus the original's 65 cycles.
(Though, as a note for posterity: if later this is replaced with some
sort of cryptographic hash function, I'll still be keeping 65 cycles as
my target 😋.) This Magma script, <https://xn--4db.cc/V1nFTMYE/magma>,
or the equivalent Sage script, <https://xn--4db.cc/LpZhTYIh/sage>,
proves that this construction does indeed yield a max-period LFSR with a
primitive polynomial for our 4 pool words.

I mention "high diffusion" above, because that apparently was the single
discernible design goal of the original fast_mix(), even though that
didn't wind up helping anything with it. Nonetheless, we take care to
choose an LFSR with pretty high diffusion, perhaps even higher than the
original fast_mix(), which we can quantify by computing that the minimum
weight of the linear code is 10, versus around 8 if we treat the
original fast_mix() as linear as well. In other words, we probably don't
regress at all from a perspective of diffusion, even if it's not really
a design goal anyway.

In sum, the security model of this is unchanged from before, yet its
implementation now fixes that model much more rigorously. Plus the
performance is better, which perhaps matters in irq context.

As a final note, the previous fast_mix() was contributed by an anonymous
author, which, I've been told, has made some legally-minded people a bit
uncomfortable and is also against the kernel project's "real name"
policy.

Cc: Dominik Brodowski <linux@dominikbrodowski.net>
Cc: Theodore Ts'o <tytso@mit.edu>
Cc: Greg Kroah-Hartman <gregkh@linuxfoundation.org>
Signed-off-by: Jason A. Donenfeld <Jason@zx2c4.com>

---
## [ammarfaizi2/linux-block](https://github.com/ammarfaizi2/linux-block)@[861f0442ba...](https://github.com/ammarfaizi2/linux-block/commit/861f0442bab8a935f499e4a96991349817124e8d)
#### Sunday 2022-02-13 17:27:05 by Jason A. Donenfeld

random: use linear max-period irq entropy accumulator

>>> WORK IN PROGRESS, NOT YET FOR SUBMISSION, DO NOT REVIEW <<<

The current fast_mix() function is a piece of classic mailing list
crypto, where it just sort of sprung up without a lot of real analysis
of what precisely it was accomplishing. As a permutation of only two
rounds, there are some easily searchable differential trails in it, and
as a means of preventing malicious irqs, it completely fails, since it
xors new data into the entire state every time. It can't really be
analyzed as a random permutation, because it clearly isn't, and it
can't be analyzed as an interesting linear algebraic structure either,
because it's also not that. There really is very little one can say
about it in terms of entropy accumulation. It might diffuse bits, some
of the time, maybe, we hope, I guess. But for the most part, it fails to
accomplish anything concrete.

As a reminder, the simple goal of add_interrupt_randomness() is to
simply accumulate entropy until ~64 interrupts have elapsed, and then
dump it into the main input pool, which uses a cryptographic hash.

It would be nice to have something cryptographically strong in this
context, in case a malicious irq compromises a per-cpu fast pool within
the 64 interrupts / 1 second window, and then inside of that same window
somehow can control its return address and cycle counter, even if that's
a bit far fetched. However with a very CPU-limited budget, actually
doing that remains an active research project (and perhaps there'll be
something useful for Linux to come out of it). And while the abundance
of caution would be nice, this isn't *currently* the security model, and
we don't yet have a fast enough solution to make it our security model.
Plus there's not exactly a pressing need to do that. (And for the
avoidance of doubt, the actual cluster of 64 accumulated irqs still gets
dumped into our cryptographically secure input pool.)

So, for now we are going to stick with the existing irq security model,
which assumes that each cluster of 64 irq cycle counter samples are
mostly non-malicious and not colluding with an infoleaker. With this as
our goal, we can then endeavor to simply accumulate entropy linearly,
discarding the least amount of it, and make sure that accumulation is
sound, unlike the current fast_mix().

It turns out that this security model is also the trade off that other
operating systems have taken. The NT kernel, for example, uses something
very simple to accumulate entropy in interrupts, `x = ror32(x, 5) ^ m`.
Dodis et al. analyzed this in <https://eprint.iacr.org/2021/523>, and
found that rotation by 7 would have been better than 5, but that
otherwise, simple linear constructions like this can be used as an
entropy collector.  However, when considering this for our four-word
accumulation, versus NT's one-word, we run into potential problems
because the words don't contribute to each other, and some may well be
fixed, which means we'd need something to schedule on top. In addition,
this works for 2-monotone distributions, which the cycle counter is, but
not the registers and return addresses that we're also capturing.
(Whether capturing anything beyond the cycle counter in the interrupt
handler is even adding much is a question for a different time.)

However, a simple LFSR actually serves the same purpose and beyond, but
easily extends to larger state sizes and more complex distributions.
Importantly, it has the advantage that it only has the trivial invariant
subspace (0 -> 0), rather than quite a few invariant subspaces like
rotate-xor, which means we benefit from the analysis of
<https://eprint.iacr.org/2021/1002>, which gives proofs that these types
of linear structures with only trivial invariant subspaces make very
good entropy accumulators.

So this commit chooses a very fast and high diffusion max-period LFSR,
implemented in a Feistel-like fashion, which pipelines quite well. On an
i7-11850H, this takes 35 cycles, versus the original's 65 cycles.
(Though, as a note for posterity: if later this is replaced with some
sort of cryptographic hash function, I'll still be keeping 65 cycles as
my target 😋.) This Magma script, <https://xn--4db.cc/V1nFTMYE/magma>,
or the equivalent Sage script, <https://xn--4db.cc/LpZhTYIh/sage>,
proves that this construction does indeed yield a max-period LFSR with a
primitive polynomial for our 4 pool words.

I mention "high diffusion" above, because that apparently was the single
discernible design goal of the original fast_mix(), even though that
didn't wind up helping anything with it. Nonetheless, we take care to
choose an LFSR with pretty high diffusion, perhaps even higher than the
original fast_mix(), which we can quantify by computing that the minimum
weight of the linear code is 10, versus around 8 if we treat the
original fast_mix() as linear as well. In other words, we probably don't
regress at all from a perspective of diffusion, even if it's not really
a design goal anyway.

In sum, the security model of this is unchanged from before, yet its
implementation now fixes that model much more rigorously. Plus the
performance is better, which perhaps matters in irq context.

As a final note, the previous fast_mix() was contributed by an anonymous
author, which, I've been told, has made some legally-minded people a bit
uncomfortable and is also against the kernel project's "real name"
policy.

Cc: Dominik Brodowski <linux@dominikbrodowski.net>
Cc: Theodore Ts'o <tytso@mit.edu>
Cc: Greg Kroah-Hartman <gregkh@linuxfoundation.org>
Signed-off-by: Jason A. Donenfeld <Jason@zx2c4.com>

---
## [thoughtbot/hotwire-example-template](https://github.com/thoughtbot/hotwire-example-template)@[49e901ccc7...](https://github.com/thoughtbot/hotwire-example-template/commit/49e901ccc7014f3135ffb3fe7bcd3e6559b9aad3)
#### Sunday 2022-02-13 17:29:49 by Sean Doyle

Loading the Tooltip Asynchronously

Fortunately, optimizing these requests is really easy. All we need to do is add a `loading` attribute and have it set to `"lazy"` to [lazy-load][] the tooltips.

This means the request to the tooltip endpoint will be made only when the `<turbo-frame>` becomes visible in the viewport. This is because `loading="lazy"` is using the [Intersection Observer API][] [under the hood][].

```diff
 <!-- app/views/users/_user.html.erb -->
 <div id="<%= dom_id user %>" class="scaffold_record">
   <p>
     <strong>Name:</strong>
     <%= user.name %>
   </p>

   <p class="relative">
     <%= link_to "Show this user", user, class: "peer", aria: { describedby: dom_id(user, :tooltip) } %>
     <!--
       Right now we're hiding each frame and its children
       with the `hidden` class. We're revealing each frame
       and its children with the `peer-hover:block` class.
      -->
     <turbo-frame id="<%= dom_id user, :tooltip %>" target="_top" role="tooltip"
                  src="<%= user_tooltip_path(user, turbo_frame: dom_id(user, :tooltip)) %>"
                  class="hidden absolute translate-y-[-150%] z-10
                         peer-hover:block peer-focus:block hover:block focus-within:block"
+                 loading="lazy"
     >
       <!-- The tooltip will be added here. -->
     </turbo-frame>
   </p>
 </div>
```

If you go back to `http://localhost:3000/users` you'll notice that a network request is only made once you hover over the link.

![Hovering over each link loads the tooltip asynchronously](https://images.thoughtbot.com/blog-vellum-image-uploads/rVXa8PJ9Sq2u3G3WXTEZ_hw-2.gif)

Right now we're hiding each frame with the `hidden` class and then revealing it with the `peer-hover:block` class. Both of these classes are provided to us by [Tailwind][] and are a nice abstraction of the [general sibling combinator][]. Even though a `<turbo-frame>` may be in the viewport, the fact that it's not visible prevents the network request from being made. It's only when the `<turbo-frame>` is revealed via CSS that the request is made.

![The Tailwind classes used to abstract the general sibling combinator and reveal the tooltip](https://images.thoughtbot.com/blog-vellum-image-uploads/n8yQbPEhSrClaUTcZ1ve_hw-3.png)

In order to test this, try removing the `hidden` class from the `<turbo-frame>`. You'll notice the tooltips are still lazy-loaded, except this time they are loaded once they come into the viewport.

```diff
 <!-- app/views/users/_user.html.erb -->
 <div id="<%= dom_id user %>" class="scaffold_record">
   <p>
     <strong>Name:</strong>
     <%= user.name %>
   </p>

   <p class="relative">
     <%= link_to "Show this user", user, class: "peer", aria: { describedby: dom_id(user, :tooltip) } %>
     <!--
       Right now we're hiding each frame and its children
       with the `hidden` class. We're revealing each frame
       and its children with the `peer-hover:block` class.
      -->
     <turbo-frame id="<%= dom_id user, :tooltip %>" target="_top" role="tooltip"
                  src="<%= user_tooltip_path(user, turbo_frame: dom_id(user, :tooltip)) %>"
-                 class="hidden absolute translate-y-[-150%] z-10
+                 class="absolute translate-y-[-150%] z-10
                         peer-hover:block peer-focus:block hover:block focus-within:block"
                  loading="lazy"
     >
       <!-- The tooltip will be added here. -->
     </turbo-frame>
   </p>
 </div>
```

![Displaying the frame will load the tooltip once it's in the viewport.](https://images.thoughtbot.com/blog-vellum-image-uploads/dQLMVeagQjuj15wOIuAd_hw-4.gif)

[lazy-load]: https://turbo.hotwired.dev/reference/frames#lazy-loaded-frame
[Tailwind]: https://tailwindcss.com/
[general sibling combinator]: https://developer.mozilla.org/en-US/docs/Web/CSS/General_sibling_combinator
[Intersection Observer API]: https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API
[under the hood]: https://github.com/hotwired/turbo/blob/8bce5f17cd697716600d3b34836365ebcdc04b3f/src/observers/appearance_observer.ts
[aria-describedby]: https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes/aria-describedby
[ARIA WAI specification for tooltips]: https://www.w3.org/TR/wai-aria-practices-1.1/#tooltip

<h2>Takeaways</h2>

There are two main takeaways from this simple demonstration that extend beyond Hotwire and Tailwind.

<h3>Lazy-load content when you can</h3>

There's a cost to each network request, and not all user's will be viewing your application on the latest hardware or on a stable internet connection. Consider lazy-loading content that's not critical to the initial page load, especially if that content is not in the viewport.

Turbo makes this easy with its `loading` attribute, but this is not a Turbo specific concept.

<h3>CSS can be leveraged to drive interactions</h3>

In our example we're able to reveal the tooltip by hovering over the tooltip's sibling. This may seem like the result of some magical property provided by Tailwind via the [peer class][], but in reality it's just the result of the [general sibling combinator][] (which has been around since Internet Explorer 7) in combination with [user action pseudo-classes][]. This is an incredibly powerful yet under utilized feature of CSS, and is often unnecessarily replicated with JavaScript.

Tailwind has exposed some of the most powerful features that CSS has to offer, but remember that they're just abstractions around existing CSS specifications.

[peer class]: https://tailwindcss.com/docs/hover-focus-and-other-states#styling-based-on-sibling-state
[general sibling combinator]: https://developer.mozilla.org/en-US/docs/Web/CSS/General_sibling_combinator
[user action pseudo-classes]: https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-classes#user_action_pseudo-classes

---
## [thoughtbot/hotwire-example-template](https://github.com/thoughtbot/hotwire-example-template)@[26ba727a02...](https://github.com/thoughtbot/hotwire-example-template/commit/26ba727a02d0e624d8b54d3defb947aac5d69e3c)
#### Sunday 2022-02-13 17:31:51 by Sean Doyle

Hiding the results when inactive

Now that we're overlaying our results on top of the rest of the page,
we'll only want to do so when the end-user is actively searching. We'll
also want to avoid needless requests to the server with empty query
text.

Lucky for us, browsers provide a built-in mechanism to prevent bad
`<form>` submissions and to surface a field's correctness: [Constraint
Validations][]!

In our case, there are two ways that a search can be invalid:

1. The query `<input>` element is completely blank.
2. The query `<input>` element has a value, but that value is comprised
   of entirely empty text characters.

To consider those states invalid, render the `<input>` with [required][]
and [pattern][] attributes:

```diff
--- a/app/views/layouts/application.html.erb
+++ b/app/views/layouts/application.html.erb
       <form action="<%= searches_path(turbo_frame: "search_results") %>" data-turbo-frame="search_results">
         <label for="search_query">Query</label>
-        <input id="search_query" name="query" type="search">
+        <input id="search_query" name="query" type="search" pattern=".*\w+.*" required>
```

By default, browsers will communicate a field's invalidity by
rendering a field-local tooltip message. While it's important to
minimize the number of invalid HTTP requests sent to our server, a
type-ahead search box works best when users can incrementally make
changes to the query string. In our case, a validation message could
disruptive or distract a user mid-search.

To have more control over the validation experience, we'll need to write
some JavaScript. Let's create
`app/javascript/controllers/form_controller.js` to serve as a [Stimulus
Controller][]:

```javascript
import { Controller } from "@hotwired/stimulus"

export default class extends Controller {
}
```

Next, we'll need to listen for browsers' built-in [invalid][] events to
fire. When they do, we'll route them to the `form` controller as a
[Stimulus Action][] named `hideValidationMessage`:

```diff
--- a/app/views/layouts/application.html.erb
+++ b/app/views/layouts/application.html.erb
     <header>
-      <form action="<%= searches_path(turbo_frame: "search_results") %>" data-turbo-frame="search_results">
+      <form action="<%= searches_path(turbo_frame: "search_results") %>" data-turbo-frame="search_results"
+        data-controller="form" data-action="invalid->form#hideValidationMessage:capture">
         <label for="search_query">Query</label>
```

One quirk of [invalid][] events is that they _do not_ [bubble up][]
through the [DOM][]. To account for that, our `form` controller will
need to act on them during the capture phase. Stimulus supports the
[`:capture` suffix][capture] as a directive to hint to our action
routing that the controller's action should be invoked during the
capture phase of the underlying event listener.

Once we're able to act upon the [invalid][] event, we'll want the
`form#hideValidationMessage` action to [prevent the default behavior][]
to stop the browser from rendering the validation message.

```diff
--- a/app/javascript/controllers/form_controller.js
+++ b/app/javascript/controllers/form_controller.js
 import { Controller } from "@hotwired/stimulus"

 export default class extends Controller {
+  hideValidationMessage(event) {
+    event.stopPropagation()
+    event.preventDefault()
+  }
 }
```

When an ancestor `<form>` element contains fields that are invalid, it
will match the [:invalid][] pseudo-selector. By rendering the search
results `<turbo-frame>` element as a [direct sibling][] to the `<form>`
element, we can incorporate the `:invalid` state into the sibling
element's style, and hide it.

```diff
--- a/app/assets/stylesheets/application.css
+++ b/app/assets/stylesheets/application.css
*= require_tree .
*= require_self
*/
+
+.empty\:hidden:empty                                { display: none; }
+.peer:invalid ~ .peer-invalid\:hidden               { display: none; }

--- a/app/views/layouts/application.html.erb
+++ b/app/views/layouts/application.html.erb
    <header>
-      <form action="<%= searches_path(turbo_frame: "search_results") %>" data-turbo-frame="search_results"
+      <form action="<%= searches_path(turbo_frame: "search_results") %>" data-turbo-frame="search_results" class="peer"
        data-controller="form" data-action="invalid->form#hideValidationMessage:capture">
        <label for="search_query">Query</label>

--- a/app/views/layouts/application.html.erb
+++ b/app/views/layouts/application.html.erb
-      <turbo-frame id="search_results" target="_top"></turbo-frame>
+      <turbo-frame id="search_results" target="_top" class="empty:hidden peer-invalid:hidden"></turbo-frame>
    </header>
```

[Constraint Validations]: https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5/Constraint_validation
[required]: https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/required
[pattern]: https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/pattern
[invalid]: https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/invalid_event
[capture]: https://stimulus.hotwire.dev/reference/actions#options
[Stimulus Controller]: https://stimulus.hotwire.dev/handbook/hello-stimulus#controllers-bring-html-to-life
[Stimulus Action]: https://stimulus.hotwire.dev/handbook/building-something-real#connecting-the-action
[bubble up]: https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Events#Bubbling_and_capturing_explained
[DOM]: https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model
[prevent the default behavior]: https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Events#preventing_default_behavior
[:invalid]: https://developer.mozilla.org/en-US/docs/Web/CSS/:invalid
[Tailwind CSS]: https://tailwindcss.com/
[variant]: https://tailwindcss.com/docs/hover-focus-and-other-states
[direct sibling]: https://developer.mozilla.org/en-US/docs/Web/CSS/General_sibling_combinator

---
## [FiendsOfTheElements/FF1Randomizer](https://github.com/FiendsOfTheElements/FF1Randomizer)@[acf3894385...](https://github.com/FiendsOfTheElements/FF1Randomizer/commit/acf3894385a4a8f4eb9a80ad6c5c10c6787575c0)
#### Sunday 2022-02-13 18:02:09 by mhn65536

Mhn65536/mpool (#804)

* Tournament Item magic Pool
Lower Thief Agility Settings
Buff Tier1 Damage Spells

* fix

* oops

* i hate my life

* guaranteed tent

* alter magic pool

Co-authored-by: x.y <x.y@z>

---
## [DrUm78/scummvm](https://github.com/DrUm78/scummvm)@[dc4cfa05fe...](https://github.com/DrUm78/scummvm/commit/dc4cfa05fe77224adf8c806309145e881d4ea8b9)
#### Sunday 2022-02-13 19:08:35 by Torbjörn Andersson

SCUMM: Display Loom Overture Timing value as time, not a magic number

It makes it less obvious what the default was, but I think this is a lot
more user friendly. For some reason, it looks awful in RTL languages,
but I have no idea how to fix that.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[77adec6281...](https://github.com/mrakgr/The-Spiral-Language/commit/77adec628147d71f83aea2be853b019dfc661293)
#### Sunday 2022-02-13 19:52:48 by Marko Grdinić

"10:40am. This is actually earlier than I thought I would wake up given how late to I went to bed yesterday. Let me skip the morning session. Let me chill, do the chores, have breakfast and then I'll finally deal with the modeling phase.

12:50pm. Let me finally start the modeling adventure. I'll get that rack done promptly.

1:05pm. I have that post. Now let me do the hooks.

1:30pm. The hook is turning out harder than I thought it would.

1:40pm. I asked in the general. It turns out that the sweep node produces intersecting geometry. The mesh it folding in on itself. This is quite annoying. What do I do about it? Rather than just waiting for an answer, I am going to have to do some research by myself. Maybe I should have done this in Blender after all.

1:55pm. I remembered the PolyDoctor node from the time I tried fixing the normals and that did the trick. It did not fix the self intersection though.

2pm. You know what, let me ignore this problem otherwise my whole day will be eaten away by it. Now that I've fixed the artefact it literally does not matter.

2:10pm. Actually, let me make a curve less vicious. I think I'd get this problem in Blender as well. Let me smooth it out a bit.

2:15pm. A wasted effort. I can't fix this.

Forget it. Let me move on. The next come pool improvements.

2:30pm. https://houdinihelp.ru/nodes/SOP/intersectionanalysis.html

Oh, wait, this actually looks for self intesections. And I had an idea, I could just blast the curve points that are near to the corner. I actually hand't even thought of this.

Ok, even if I have the intersecting points, I have no idea what to do with them.

2:45pm. Ok, I blasted the points around the sharp corners and then I beveled the edges. This is the solution. Sigh.

2:50pm. This wasted so much of my time. Let me focus on the pool.

Ok, I need the pool front group, and I need it before it has been extruded.

I should try the facet node.

Also some of the edge tools I should check out here. I am not happy with blasting the hook.

3:20pm. Holy shit, how I hate that the input geometry to copy to curves is the second input. Couldn't they have fixed this early on?

3:40pm. Ok, let me do the pool ladder. I did the nibs, but for all I know my proportions could be badly off. but it is fine. I am doing everything procedurally, so it will be easy to change things.

The ladder. Let me get to it.

5pm. Did the ladder, but after doing the booleans on the pool, now I notice that the ngons are messing up the lighting in unnatural ways. Let me deal with this.

https://youtu.be/eD-W9jh9hJE
Grouping Ngons (or Quads or Triangles) and Fixing them

Let me go with this. Yes, this, not the Cop Craft thread.

5:20pm. None of that stuff did jack. What did was settting up the normals so that they resemble flat shading.

5:25pm. Ok, that is enough of that. Doing it by face area works well enough. The issue is that after the boolean ops, the topology got messed up. Had I done this by hand, this would not have happened.

But it would have been annoying to do. Let me just move on.

The last thing that I need to deal with is the walkway. I did the HellProto logo, but I do not think it is suitable to put it there. I should be using the pool segment as a guide.

6:35pm. Had to leave for lunch. Let me have this fruit and then I'll do the walkway.

6:55pm. Let me resume. I want to figure out how to make the cross section for sweep. It is a real pain in the ass.

7:05pm. I've gotten the hang of how to do the cross section.

8:05pm. https://www.hipflask.how/geometry-essentials-03
> 9. Using the Carve Node to Shorten the Curve

I need to check out the carve node. The way I am currently makign the curves shorter is ridiculous.

8:10pm. Damn it, how do you get the length of a spline? If I could figure that out, I could get rid of all the uses of boolean curve SOP.

8:30pm. I figured it out. Measure outputs the perimeter. I used this before, but then completely forgot about it.

8:35pm. >  Warning  Local variable 'primnum' not found.

Enough. I'll figure out how to use primnum tomorrow. I have no idea why it is failing for me. I'll have to take a look at the carve examples first. Right now, I do not feel like it and keep looking for shortcuts.

Actually, let me just try if I can use the attribute directly.

Nope. Also I am not wrong. I found in the cookbook that @primnum is the right way to get the primitive local number.

8:50pm. Let me play Fallout. Forget geomentry nodes."

---
## [jdugan6240/kak-dap](https://github.com/jdugan6240/kak-dap)@[1841a4ef84...](https://github.com/jdugan6240/kak-dap/commit/1841a4ef8421133bf11f4893d16ea208b4f31fc9)
#### Sunday 2022-02-13 21:38:04 by James Dugan

Reverted session passing to happen via command line args.

On second thought, passing the Kakoune session via environment variables was a mistake.
While we can guarantee that certain command line arguments be passed to the application,
we can't guarantee that environment variables will be set. This necessitated ugly
fallbacks when the environment variable wasn't defined that would not work in 100%
of cases (if the session happened to be named "none", kak-dap would fail). Reverting to
using command line arguments to pass the session to the program allows us to check if the
necessary command line argument was defined, and if not, abort the application.

The biggest question now is how we're going to pass the currently set breakpoints to kak-dap
(for this initial release, we aren't going to allow changing the breakpoints at runtime).
The current best idea I have at the moment is to dump them into a file that kak-dap then
reads to retrieve the initial breakpoint data. This would be a temp file, since we would then
need to clean it up after the breakpoints are read. While this solution seems a tad clunky
and inelegant, I can't come up with a better approach at present.

---
## [garrett-laroy-johnson/diagrammatic](https://github.com/garrett-laroy-johnson/diagrammatic)@[5d17075d79...](https://github.com/garrett-laroy-johnson/diagrammatic/commit/5d17075d7937f07f20940fc0f33c491d43d15b08)
#### Sunday 2022-02-13 21:39:58 by garrett laroy johnson

Update readwrite.js

file successfully written. bugs are that:

1. this.filelist is not populating with filenames (blame "Add objects features")

2. "add objects feature" doesn't clear files from loader after adding.

3. "add objects feature" doesn't create tabs to edit images etc.

4. "add objects feature" fucking sucks let's change this shit

---
## [JoeBidenWhatAreYouHiding/kx](https://github.com/JoeBidenWhatAreYouHiding/kx)@[08617de495...](https://github.com/JoeBidenWhatAreYouHiding/kx/commit/08617de495cfb0c93361ae3380637e3c6a26cac2)
#### Sunday 2022-02-13 23:00:45 by AmCath

alt Tammany portrait should they say fuck you democracy

---

