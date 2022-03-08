## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-03-07](docs/good-messages/2022/2022-03-07.md)


1,790,926 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,790,926 were push events containing 2,842,641 commit messages that amount to 210,158,453 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 43 messages:


## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[ac21ef9078...](https://github.com/tgstation/tgstation/commit/ac21ef9078d88f51a4e198e394ed56e3cc731b45)
#### Monday 2022-03-07 00:02:32 by Pickle-Coding

No, we don't want radiation getting released in large pipenets fuck you fuckr uyu! (#65212)

* Make it harder to release radiation in large pipenets. Squares the volume / 2,500 thingy, and adds the requirements to the proto-nitrate bz response and proto-nitrate tritium response gas reactions to release radiation. This will make it significantly harder to release radiation in large pipenets, because releasing radiation in large pipenets makes it harder for people to identify the cause on why they are getting irradiated, which is bad and goes against the modern radiation goals.

Squaring is not enough for deranged people that know we don't want radiation released in large pipenets. Cubes the requirement instead. If someone could get enough gases reacting at once after this, then there is a bigger problem with atmos.

Who had fun seeing everything green, then getting irradiated and not even knowing why? I don't know, because I don't know who put the gases in waste and why we must suffer.

---
## [vchong/linux](https://github.com/vchong/linux)@[a50e1fcbc9...](https://github.com/vchong/linux/commit/a50e1fcbc9b85fd4e95b89a75c0884cb032a3e06)
#### Monday 2022-03-07 00:04:19 by Josef Bacik

btrfs: do not WARN_ON() if we have PageError set

Whenever we do any extent buffer operations we call
assert_eb_page_uptodate() to complain loudly if we're operating on an
non-uptodate page.  Our overnight tests caught this warning earlier this
week

  WARNING: CPU: 1 PID: 553508 at fs/btrfs/extent_io.c:6849 assert_eb_page_uptodate+0x3f/0x50
  CPU: 1 PID: 553508 Comm: kworker/u4:13 Tainted: G        W         5.17.0-rc3+ #564
  Hardware name: QEMU Standard PC (Q35 + ICH9, 2009), BIOS 1.13.0-2.fc32 04/01/2014
  Workqueue: btrfs-cache btrfs_work_helper
  RIP: 0010:assert_eb_page_uptodate+0x3f/0x50
  RSP: 0018:ffffa961440a7c68 EFLAGS: 00010246
  RAX: 0017ffffc0002112 RBX: ffffe6e74453f9c0 RCX: 0000000000001000
  RDX: ffffe6e74467c887 RSI: ffffe6e74453f9c0 RDI: ffff8d4c5efc2fc0
  RBP: 0000000000000d56 R08: ffff8d4d4a224000 R09: 0000000000000000
  R10: 00015817fa9d1ef0 R11: 000000000000000c R12: 00000000000007b1
  R13: ffff8d4c5efc2fc0 R14: 0000000001500000 R15: 0000000001cb1000
  FS:  0000000000000000(0000) GS:ffff8d4dbbd00000(0000) knlGS:0000000000000000
  CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
  CR2: 00007ff31d3448d8 CR3: 0000000118be8004 CR4: 0000000000370ee0
  Call Trace:

   extent_buffer_test_bit+0x3f/0x70
   free_space_test_bit+0xa6/0xc0
   load_free_space_tree+0x1f6/0x470
   caching_thread+0x454/0x630
   ? rcu_read_lock_sched_held+0x12/0x60
   ? rcu_read_lock_sched_held+0x12/0x60
   ? rcu_read_lock_sched_held+0x12/0x60
   ? lock_release+0x1f0/0x2d0
   btrfs_work_helper+0xf2/0x3e0
   ? lock_release+0x1f0/0x2d0
   ? finish_task_switch.isra.0+0xf9/0x3a0
   process_one_work+0x26d/0x580
   ? process_one_work+0x580/0x580
   worker_thread+0x55/0x3b0
   ? process_one_work+0x580/0x580
   kthread+0xf0/0x120
   ? kthread_complete_and_exit+0x20/0x20
   ret_from_fork+0x1f/0x30

This was partially fixed by c2e39305299f01 ("btrfs: clear extent buffer
uptodate when we fail to write it"), however all that fix did was keep
us from finding extent buffers after a failed writeout.  It didn't keep
us from continuing to use a buffer that we already had found.

In this case we're searching the commit root to cache the block group,
so we can start committing the transaction and switch the commit root
and then start writing.  After the switch we can look up an extent
buffer that hasn't been written yet and start processing that block
group.  Then we fail to write that block out and clear Uptodate on the
page, and then we start spewing these errors.

Normally we're protected by the tree lock to a certain degree here.  If
we read a block we have that block read locked, and we block the writer
from locking the block before we submit it for the write.  However this
isn't necessarily fool proof because the read could happen before we do
the submit_bio and after we locked and unlocked the extent buffer.

Also in this particular case we have path->skip_locking set, so that
won't save us here.  We'll simply get a block that was valid when we
read it, but became invalid while we were using it.

What we really want is to catch the case where we've "read" a block but
it's not marked Uptodate.  On read we ClearPageError(), so if we're
!Uptodate and !Error we know we didn't do the right thing for reading
the page.

Fix this by checking !Uptodate && !Error, this way we will not complain
if our buffer gets invalidated while we're using it, and we'll maintain
the spirit of the check which is to make sure we have a fully in-cache
block while we're messing with it.

CC: stable@vger.kernel.org # 5.4+
Signed-off-by: Josef Bacik <josef@toxicpanda.com>
Signed-off-by: David Sterba <dsterba@suse.com>

---
## [k0ck/chrome-extension-aw](https://github.com/k0ck/chrome-extension-aw)@[c255749615...](https://github.com/k0ck/chrome-extension-aw/commit/c255749615988d817f5b01b2788ad887ecdc898a)
#### Monday 2022-03-07 00:10:32 by k0ck

Gallery align marshalled. Race condition improvement. Also fuck you Putin, you stupid cunt/2

---
## [Zonespace27/Skyrat-tg](https://github.com/Zonespace27/Skyrat-tg)@[d96e7b7e27...](https://github.com/Zonespace27/Skyrat-tg/commit/d96e7b7e278dd0226a4de8d9463edda37af709f9)
#### Monday 2022-03-07 00:21:49 by SkyratBot

[MIRROR] Makes Ants glow, puts a min on ant screaming & shoe permeability, & other ant-related things. [MDB IGNORE] (#11821)

* Makes Ants glow, puts a minimum on ant screaming and shoe permeability, and other ant-related things. (#64786)

I found out how emissives work and my first thought was "damn ants should glow that would look sick"
So now they do.

Also, having less than 5u ants in your body will make you not scream, so 0.0001u ants will no longer have that tiny chance of making someone scream for their life.

If an ant pile has a max damage value less than 1, then they won't be able to bite through your shoes. This is the same threshold as the second tier ant icon.

Makes the giant ant a hostile mob with the neutral faction, meaning they will attack anything not in the neutral faction.

* Makes Ants glow, puts a min on ant screaming & shoe permeability, & other ant-related things.

Co-authored-by: Wallem <66052067+Wallemations@users.noreply.github.com>

---
## [alyshanjahani-crl/cockroach](https://github.com/alyshanjahani-crl/cockroach)@[fe416fd5a8...](https://github.com/alyshanjahani-crl/cockroach/commit/fe416fd5a85229652e0ab352bf342d6e27afaef5)
#### Monday 2022-03-07 00:36:24 by craig[bot]

Merge #75957 #75961 #76003

75957: sql: update SHOW GRANTS ON TYPE to include grant options r=RichardJCai a=ecwall

refs https://github.com/cockroachdb/cockroach/issues/73394

Release note (sql change): SHOW GRANTS ON TYPE includes is_grantable column

75961: dev: integrate `bazel-remote` with `dev` r=rail a=rickystewart

* Add a new command `dev cache` which prepares the local cache.
  `dev cache --down` tears down the local cache, and `dev cache --reset`
  reboots it. My thinking is that we can extend the `dev cache` command
  with more stuff when we have it (e.g. remote caching).
* To this end we take the PID of the cache process and write it to a
  file in the cache directory. There's also a config file that users can
  manually update if they want.
* I request that people put this in their `~/.bazelrc`. It shouldn't be
  a problem if this applies to every Bazel workspace on the user's
  machine, it's just a cache.
* `dev doctor` now sets up the cache. It will now also fail unless your
  `~/.bazelrc` contains the string `--remote_cache=`. You can disable
  this with `--no-cache` or `DEV_NO_REMOTE_CACHE`.

Release note: None

76003: sql/catalog/bootstrap,*: allow system table IDs to be dynamic r=ajwerner a=ajwerner

This change is relatively small in terms of logic changes but it has large
implications for tests. The crux of the change is that we want to allow system
tables to not specify their IDs explicitly in their definition. The reason for
this is that we only reserved IDs 10-49 before handing out IDs to users. This
has the implication that new system tables in excess of 49 could overlap with
existing user descriptors. To cope with that, we'll need to use the descriptor
ID generator we normally use for user descriptors also for new system
descriptors in migrations.

Now, that could be the end of the story. The problem is that we really like
using data driven tests and we rather like printing out our keys, which
include descriptor IDs. If we were to carry on without changing the point
at which we started generating user descriptors, we'd run into real pain
every time we try to add another system table. All those datadriven tests
would have to change (and some other non-datadriven tests too).

This commit goes through that pain so hopefully for many years nobody else
has to. It does so by moving the first user descriptor we'll generate in a
newly bootstrapped cluster (or tenant) up to 100. This constant is not exported
and we can add mechanisms to override it later. This constant is chosen because
it still falls into the magical realm where the keys remain the same size.
It's also rather aesthetic. We could go bigger, but we'd pay a price for the
key for the first table you introduce. This probably doesn't matter, but I
don't want to be the one to do it.

Release note: None

Co-authored-by: Evan Wall <wall@cockroachlabs.com>
Co-authored-by: Ricky Stewart <ricky@cockroachlabs.com>
Co-authored-by: Andrew Werner <awerner32@gmail.com>

---
## [flesh-cube/flesh-and-blood-cards](https://github.com/flesh-cube/flesh-and-blood-cards)@[c86bad2061...](https://github.com/flesh-cube/flesh-and-blood-cards/commit/c86bad2061957ce28f95dc5643bd817c82a49479)
#### Monday 2022-03-07 00:40:57 by Tyler Luce

- Fix various data issues with Over Loop, Hamstring Shot, Salvage Shot, Become the Arknight, Forked Lightning, Command and Conquer, Life for a Life, Enchanting Melody, Eirina’s Prayer, Arknight Shard, Massacre, Blessing of Serenity, Zephyr Needle, Heron’s Flight, Cintari Saber, Dauntless, Hit and Run, Absorption Dome, High Speed Impact, Combustible Courier, Kavdaen, Trader of Skins, Feign Death, Dread Triptych, Rattle Bones, Mauvrion Skies, Meat and Greet, Cindering Foresight, Gambler’s Gloves, Spears of Surreality, Dimenxxional Gateway, Seeping Shadows, Seeds of Agony, Tremor of iArathael, Oaken Old, Cold Wave, Rejuvenate, Chill to the Bone, Wild Ride, Bad Beats, Nerves of Steel, Twin Twisters, Blood on Her Hands, Oath of Steel, Slice and Dice, Outland Skirmish, Dissolution Sphere, T-Bone, Zoom In, Release the Tension, Revel in Runeblood, Veiled Intentions, and Life of the Party

---
## [nickclason/Senior-Design](https://github.com/nickclason/Senior-Design)@[8500ca087a...](https://github.com/nickclason/Senior-Design/commit/8500ca087afa2099bef4888e601747eeb932674d)
#### Monday 2022-03-07 01:13:48 by Nick Clason

Finally fucking figure out chart styling

i hate my life

---
## [quotefox/Hyper-Station-13](https://github.com/quotefox/Hyper-Station-13)@[5d96c13de2...](https://github.com/quotefox/Hyper-Station-13/commit/5d96c13de288fd1d735a392ceffd991d7ecc17f2)
#### Monday 2022-03-07 01:19:23 by sarcoph

holy fucking shit i am so tired of refactoring

to do list:
- ensure all useBackends use context instead of props
- ensure all uis that need it get their `{ act, data, config }` from useBackend(context)
- fix the rest of the bugs

i do not have the energy for this.

---
## [san7890/bruhstation](https://github.com/san7890/bruhstation)@[eeb5465931...](https://github.com/san7890/bruhstation/commit/eeb546593148ce940e9adac2c663c453d6557247)
#### Monday 2022-03-07 01:46:18 by vincentiusvin

Ordnance Content Update: Scientific Papers (#62284)

How do I play/test/operate this?

Download NT Frontier on any modular computers. It should debrief you on what experiments are available and how to publish.
If you want to do a bomb experiment, make sure it's captured by the doppler array (as usual) and then print the experiments into a disk and publish it.
If you want to do a gas experiment, make the gas and either pump it into a tank and 1) overpressurize it with a "clear" gas like N2 or 2) overpressurize tanks with the gas itself. Make sure you do the overpressurizing in the compressor machine. When tanks are destroyed/ejected leaked gas will get recorded. Print it into a disk and publish it.
For publication, the file needs to be directly present inside the computer's HDD. This means you need to copy it first with the file manager.
Fill the data (if desired, it will autofill with boiler plate if you dont) and send away!
Doing experiments unlock nodes, while doing them well unlocks boosts (which are discounts but slightly more restrictive) which are purchaseable with NT Frontier.
If you are testing this and have access to admin tools, there are various premade bombs under obj/effect/spawner/newbomb

A doc I wrote detailing the why and what part of this PR.
https://hackmd.io/JOakSYVMSh2zU2YL5ju_-Q

---

# Intro

## The Problem(s)

Ordnance, (previously toxins) seems to lack a lot of content and things to do. The gameplay loop consists of making a bomb and then sending it off for credits or using it to refine cores. Ordnance at it's inception originally relies on players experimenting and finding the perfect mix over multiple rounds, but once the recipe for a "do-everything" mix got out, the original charm of individual discoveries becomes meaningless.

Another issue with ordnance is the odd difficulty curve. As a new player, ordnance is almost impossible to decipher, but once you watch a tutorial or read a wiki and can mail a 50k into space, there pretty much isn't anything else to do. Most players will be satisfied at this point without the gameplay loop encouraging them to understand or play more. The only thing you can do afterwards is to sink your teeth in and understand why that particular mix explodes the way it does. This again has a significant difficulty curve, but if you do that, the department doesn't acknowledge or reward that in any way. There are pretty much two huge spikes, with the latter one not really existing inside the department.

TLDR:
* The content being same-y over rounds.
* Odd difficulty curve: 
    1. A new player is oblivious to everything. 
    2. Those in the middle can repeat the final goal consistently without needing to understanding why
    3. There is nothing to justify spending more time in the department after reaching the midgame.

## Abstract

Scientific Papers aim to add a framework to run multiple experiments in ordnance. Adding more experiments scattered across various atmospheric aspects might allow players of various knowledge levels to still have something engaging to do. A new player should have an easier challange than to mail a 50K. While those that already can make bombs should have an easier time understanding why their bombs explode the way it does. Once they fully understand why, they can set their sights on taking advantage of another reaction to set their bomb off or hone one particular reaction down.

## Goals

* Have some intro-level challanges for new players.
* Have some semblance of late-game challanges for more experienced players.
* Explain the mechanics better for those in the middle of the road.
* Incentivize trying new things out in the department.
* Better integrate Ordnance with Experisci

## Boundaries / Dont's

* Do not incentivize people to learn ordnance by using PvP loots.
* Do not shake or change the reaction system by a huge amount.
* Disincentivize having a single god-mix that does everything.
****

# Main design pillars

## A. Framework surrounding the experiments

### A.1. New experiments

Add new experiments to the ExperiSci module. These will come in two flavours: New explosions to do, and various gas synthesis experiments. Both of these are actually supported by the map layout of ordnance right now, but there is no reason to do anything outside of making a 50k as fast as possible.

### A.2. Rewards for experiments: Cash and Techweb Boosts.

Scientific papers will add a separate experiment handling system. A single experiment will be graded into various tiers, each tier corresponding to the explosion size or amount of gas made.  Doing any tier of a specific experiment will unlock the discount for that specific reactions. A single explosion **WILL NOT** do multiple experiments (or even tiers) at once.

On publication, a partner can be selected. A single partner only has a specific criteria of experiments they want. The experiments will then be graded on "how good they are done", with the criteria being more punishing as tier increases. Publication will then reward scientific cooperation with the partnered partner. Players can spend this cooperation on techweb boosts. Techweb boosts are meant to be subservient to discount from experiments and will not shave a node's price to be lower than 500 points.

**Experiments will only unlock nodes, discounts are handled through this boost system.**
This is more for maintainability than anything.

### A.3. On Tedium

*This is a note on implementation more than anything, but I think this helps explains why several things are done.*

Due to the nature of atmospheric reactions in the game (they're all linear), tedium is a very important thing to consider. An experiment should have a sweet spot to aim for, but there should not be a point where further mastery is stopped dead on it's track with a reward cap.

Scientific Papers attempts to discourage this behaviour by having the "maximum score" scale off to infinity but with the rewards being smaller and smaller. The sweet spot is always there to aim for and should be well communicated with players, but on their last submission of an experiment topic players should be encouraged to do their best. There should always be a reward for pushing the system to it's limit as long as it doesn't completely nullify the other subdepartments. This is the reason why there is a hard limit on the number of publications and why the score calculation is a bit more complex than it needed to be.

## B. Gas Synthesis (Early-Mid Game)

Scientific papers will add one new machine that requests a tank to release x amounts of y gas. This will be accomplished by adding a tank pumping machine which will either burst or explode a tank, releasing the gas inside. The gas currently requested are BZ, Nitryl, Halon and Nob.

The overarching goal of this compressor machine is to present a gas synthesis challange for the players and to get them more accustomed to how a tank explodes. The gas synthesis part can always be changed in order to reflect the current state of atmospheric reactions.

## C. Explosion Changes (Mid-Late Game)

### C.1 Cause and effect.

The main theme of the explosion changes is establishing cause and effect of explosions. Reactions that happens inside a tank that's going to explode will be recorded and forwarded to a doppler array. Some experiments will require only a single cause to be present (think of it as isolating a variable). This is currently implemented for nobliumformation and pressure based bombs. Having other reactions occuring besides noblium formation will fail the first one, while having any reactions at all will fail the second one. 

Adding more explosions here will be a slight challange because as of now the game has only two reactions that can reliably make an explosion.

### C.2 Tools upgrade.

Doppler array has now been retrofitted to state the probable cause of an explosion, be it reactions or just overpressurization on gas merging. These should help intermediate players figure out what is causing an explosion.

Added a new functionality to the implosion compressor:
Basically performs the gas merging and reaction that TTV does in a machine and reports the results back as if someone uses an analyzer on them. Here to give players feedback so they can try and understand what is actually going on in a bomb.

## D. Player Interaction

There should be more room for more than 1 player to play ordnance simultaneously. Previously players are also able to split tasks, but this rarely happens because tritium synthesis needs only the gas chamber to be reconfigured. Now, different players can pick different experiments and work on them. Players can also do joint tasks on one single experiment. Gases like noblium will need tritium production and also a cooling module online.

Ordnance can also coordinate with their parent department on what they really need, be it money or research bonuses.

# Potential Changes

The best-case changes that can be implemented if the current roster of content isn't enough is more reactions that can be used in bombs. Eliminating bombs entirely goes against the spirit of the subdepartment, while adding new ones will need a lot of care and consideration.

Another possible change is to implement a "gas payload" bomb. Bombs that has a set number of unreacting gas inside that will increase the heat capacity, reduce the payload, and neccesitates more bespoke mixes.

Adding more gas synthesis experiments is discouraged. The main focus of ordnance should be bombs, with gas synthesis being a side project for ordnance. These are present to ease the introduction to bombs and provide some side content. 
There should be a somewhat well-justified goal in adding new synthesis experiments: e.g. BZ is there as a "tutorial" gas, Nitryl to introduce players to cooling/heating mixes, Halon to a more efficient tritium production, and Nob as a nudge to nobformation bombs and mastery over other aspects.

# Conclusion / Summary

Add more experiments to ordnance that players can take, accomplish this by:
1. Making the players perform gas synthesis or make bombs.
2. Have them collect the data, see if it fits the criteria. Explain why if it fits and why if it doesn't.
3. Have the player publish a paper.

Reward them based on how well did they do, give players agency both on the experiment phase and also publication phase.


---
TLDR: Added new experiment to toxins, added the framework for those experiments existing. Experiments comes in gas synthesis and also bombs but with more parameters. Experiments needs to be published through papers, various choices to be made there.

Implementation notes:

Because of how paper works, ordnance experiments are handled outside of experiment_handler components. My reasoning for this is twofold:

The experiments will be completed manually on publication and if the experiment isn't unlocked yet it will still be completed.
Experiment handler datums have several procs which require an atom-level parent, and I figured this is the most sensible and cleanest way to implement this without changing the experiment handler datum too much.

Small change to /obj/machinery/proc/power_change() signal ordering to adjust the state first and then send the signal. Didn't found any other usage of this signal except mine but barge down my door if it broke something.

Rewrote the ttv merge_gases() code to be slightly more readable.
A small code improvement for thermomachine to use tofixed (my fault).

Ordnance have been updated to enable the publication of papers
Several new explosive and gas synthesis experiments have been added to ordnance
Anomaly compressor has been TGUIzed and now supports simulating the reaction of the gases inside the ttv.
New tank compressor machine for toxins. You can overpressurize tanks with exotic gases and complete experiments.
Several techweb nodes are locked and require toxin experiments to complete.
Toxins can purchase boosts for various techweb nodes.
You no longer need to anchor doppler arrays for it to work.
Doppler array and implosion compressor now supports deconstruction, implosion compressor construction added.
Doppler now emits a red light to denote it's direction and it being on. Doppler not malf.
Implosion compressor renamed to anomaly refinery.
Created a new program tab "Science" for the downloader app. Removed Robotics.
Reworked the code for bombspawner (used in the cuban pete arcade game)

---
## [yt-xmati/dave-and-bambi-psych](https://github.com/yt-xmati/dave-and-bambi-psych)@[fdaf85f612...](https://github.com/yt-xmati/dave-and-bambi-psych/commit/fdaf85f612d7aa1b837db1a0230afb09a4b964c4)
#### Monday 2022-03-07 01:51:54 by xmati

package;  import flixel.graphics.FlxGraphic; #if desktop import Discord.DiscordClient; #end import Section.SwagSection; import Song.SwagSong; import WiggleEffect.WiggleEffectType; import flixel.FlxBasic; import flixel.FlxCamera; import flixel.FlxG; import flixel.FlxGame; import flixel.FlxObject; import flixel.FlxSprite; import flixel.FlxState; import flixel.FlxSubState; import flixel.addons.display.FlxGridOverlay; import flixel.addons.effects.FlxTrail; import flixel.addons.effects.FlxTrailArea; import flixel.addons.effects.chainable.FlxEffectSprite; import flixel.addons.effects.chainable.FlxWaveEffect; import flixel.addons.transition.FlxTransitionableState; import flixel.graphics.atlas.FlxAtlas; import flixel.graphics.frames.FlxAtlasFrames; import flixel.group.FlxGroup.FlxTypedGroup; import flixel.math.FlxMath; import flixel.math.FlxPoint; import flixel.math.FlxRect; import flixel.system.FlxAssets.FlxShader; import flixel.system.FlxSound; import flixel.text.FlxText; import flixel.tweens.FlxEase; import flixel.tweens.FlxTween; import flixel.ui.FlxBar; import flixel.util.FlxCollision; import flixel.util.FlxColor; import flixel.util.FlxSort; import flixel.util.FlxStringUtil; import flixel.util.FlxTimer; import haxe.Json; import lime.utils.Assets; import openfl.Lib; import openfl.display.BlendMode; import openfl.display.Shader; import openfl.display.StageQuality; import openfl.filters.BitmapFilter; import openfl.filters.ShaderFilter; import openfl.utils.Assets as OpenFlAssets; import editors.ChartingState; import editors.CharacterEditorState; import flixel.group.FlxSpriteGroup; import flixel.input.keyboard.FlxKey; import openfl.events.KeyboardEvent; import Achievements; import StageData; import FunkinLua; import DialogueBoxPsych; import Shaders;  #if sys import sys.FileSystem; #end  using StringTools;  class PlayState extends MusicBeatState { 	public static var STRUM_X = 42; 	public static var STRUM_X_MIDDLESCROLL = -278;  	public static var ratingStuff:Array<Dynamic> = [ 		['skill issue', 0.2], //From 0% to 19% 		['what', 0.4], //From 20% to 39% 		['noob', 0.5], //From 40% to 49% 		['i br', 0.6], //From 50% to 59% 		['ratio', 0.69], //From 60% to 68% 		['funny', 0.7], //69% 		['ratio counter', 0.8], //From 70% to 79% 		['cool', 0.9], //From 80% to 89% 		['SICK TRICKS DAVE!', 1], //From 90% to 99% 		['i broke my phone!!', 1] //The value on this one isn't used actually, since Perfect is always "1" 	]; 	 	public var modchartTweens:Map<String, FlxTween> = new Map<String, FlxTween>(); 	public var modchartSprites:Map<String, ModchartSprite> = new Map<String, ModchartSprite>(); 	public var modchartTimers:Map<String, FlxTimer> = new Map<String, FlxTimer>(); 	public var modchartSounds:Map<String, FlxSound> = new Map<String, FlxSound>(); 	public var modchartTexts:Map<String, ModchartText> = new Map<String, ModchartText>(); 	public var shader_chromatic_abberation:ChromaticAberrationEffect; 	public var camGameShaders:Array<ShaderEffect> = []; 	public var camHUDShaders:Array<ShaderEffect> = []; 	public var camOtherShaders:Array<ShaderEffect> = []; 	//event variables 	private var isCameraOnForcedPos:Bool = false; 	#if (haxe >= "4.0.0") 	public var boyfriendMap:Map<String, Boyfriend> = new Map(); 	public var dadMap:Map<String, Character> = new Map(); 	public var gfMap:Map<String, Character> = new Map(); 	#else 	public var boyfriendMap:Map<String, Boyfriend> = new Map<String, Boyfriend>(); 	public var dadMap:Map<String, Character> = new Map<String, Character>(); 	public var gfMap:Map<String, Character> = new Map<String, Character>(); 	#end  	public var BF_X:Float = 770; 	public var BF_Y:Float = 100; 	public var DAD_X:Float = 100; 	public var DAD_Y:Float = 100; 	public var GF_X:Float = 400; 	public var GF_Y:Float = 130;  	public var songSpeedTween:FlxTween; 	public var songSpeed(default, set):Float = 1; 	public var songSpeedType:String = "multiplicative"; 	 	public var boyfriendGroup:FlxSpriteGroup; 	public var dadGroup:FlxSpriteGroup; 	public var gfGroup:FlxSpriteGroup; 	public var shaderUpdates:Array<Float->Void> = []; 	public static var curStage:String = ''; 	public static var isPixelStage:Bool = false; 	public static var SONG:SwagSong = null; 	public static var isStoryMode:Bool = false; 	public static var storyWeek:Int = 0; 	public static var storyPlaylist:Array<String> = []; 	public static var storyDifficulty:Int = 1;  	public var vocals:FlxSound;  	public var dad:Character; 	public var gf:Character; 	public var boyfriend:Boyfriend;  	public var notes:FlxTypedGroup<Note>; 	public var unspawnNotes:Array<Note> = []; 	public var eventNotes:Array<Dynamic> = [];  	private var strumLine:FlxSprite;  	//Handles the new epic mega sexy cam code that i've done 	private var camFollow:FlxPoint; 	private var camFollowPos:FlxObject; 	private static var prevCamFollow:FlxPoint; 	private static var prevCamFollowPos:FlxObject;  	public var strumLineNotes:FlxTypedGroup<StrumNote>; 	public var opponentStrums:FlxTypedGroup<StrumNote>; 	public var playerStrums:FlxTypedGroup<StrumNote>; 	public var grpNoteSplashes:FlxTypedGroup<NoteSplash>;  	public var camZooming:Bool = false; 	private var curSong:String = "";  	public var gfSpeed:Int = 1; 	public var health:Float = 1; 	public var combo:Int = 0;  	private var healthBarBG:AttachedSprite; 	public var healthBar:FlxBar; 	var songPercent:Float = 0;  	private var timeBarBG:AttachedSprite; 	public var timeBar:FlxBar; 	 	public var sicks:Int = 0; 	public var goods:Int = 0; 	public var bads:Int = 0; 	public var shits:Int = 0; 	 	private var generatedMusic:Bool = false; 	public var endingSong:Bool = false; 	private var startingSong:Bool = false; 	private var updateTime:Bool = true; 	public static var changedDifficulty:Bool = false; 	public static var chartingMode:Bool = false;  	//Gameplay settings 	public var healthGain:Float = 1; 	public var healthLoss:Float = 1; 	public var instakillOnMiss:Bool = false; 	public var cpuControlled:Bool = false; 	public var practiceMode:Bool = false;  	public var botplaySine:Float = 0; 	public var botplayTxt:FlxText;  	public var iconP1:HealthIcon; 	public var iconP2:HealthIcon; 	public var camHUD:FlxCamera; 	public var camGame:FlxCamera; 	public var camOther:FlxCamera; 	public var cameraSpeed:Float = 1;  	var dialogue:Array<String> = ['blah blah blah', 'coolswag']; 	var dialogueJson:DialogueFile = null;  	var halloweenBG:BGSprite; 	var halloweenWhite:BGSprite;  	var phillyCityLights:FlxTypedGroup<BGSprite>; 	var phillyTrain:BGSprite; 	var blammedLightsBlack:ModchartSprite; 	var blammedLightsBlackTween:FlxTween; 	var phillyCityLightsEvent:FlxTypedGroup<BGSprite>; 	var phillyCityLightsEventTween:FlxTween; 	var trainSound:FlxSound;  	var limoKillingState:Int = 0; 	var limo:BGSprite; 	var limoMetalPole:BGSprite; 	var limoLight:BGSprite; 	var limoCorpse:BGSprite; 	var limoCorpseTwo:BGSprite; 	var bgLimo:BGSprite; 	var grpLimoParticles:FlxTypedGroup<BGSprite>; 	var grpLimoDancers:FlxTypedGroup<BackgroundDancer>; 	var fastCar:BGSprite;  	var upperBoppers:BGSprite; 	var bottomBoppers:BGSprite; 	var santa:BGSprite; 	var heyTimer:Float;  	var bgGirls:BackgroundGirls; 	var wiggleShit:WiggleEffect = new WiggleEffect(); 	var bgGhouls:BGSprite;  	public var songScore:Int = 0; 	public var songHits:Int = 0; 	public var songMisses:Int = 0; 	public var scoreTxt:FlxText; 	var timeTxt:FlxText; 	var scoreTxtTween:FlxTween;  	public static var campaignScore:Int = 0; 	public static var campaignMisses:Int = 0; 	public static var seenCutscene:Bool = false; 	public static var deathCounter:Int = 0;  	public var defaultCamZoom:Float = 1.05;  	// how big to stretch the pixel art assets 	public static var daPixelZoom:Float = 6; 	private var singAnimations:Array<String> = ['singLEFT', 'singDOWN', 'singUP', 'singRIGHT'];  	public var inCutscene:Bool = false; 	public var skipCountdown:Bool = false; 	var songLength:Float = 0;  	#if desktop 	// Discord RPC variables 	var storyDifficultyText:String = ""; 	var detailsText:String = ""; 	var detailsPausedText:String = ""; 	#end  	//Achievement shit 	var keysPressed:Array<Bool> = []; 	var boyfriendIdleTime:Float = 0.0; 	var boyfriendIdled:Bool = false;  	// Lua shit 	public static var instance:PlayState; 	public var luaArray:Array<FunkinLua> = []; 	private var luaDebugGroup:FlxTypedGroup<DebugLuaText>; 	public var introSoundsSuffix:String = '';  	// Debug buttons 	private var debugKeysChart:Array<FlxKey>; 	private var debugKeysCharacter:Array<FlxKey>; 	 	// Less laggy controls 	private var keysArray:Array<Dynamic>;  	override public function create() 	{ 		Paths.clearStoredMemory();  		// for lua 		instance = this;  		debugKeysChart = ClientPrefs.copyKey(ClientPrefs.keyBinds.get('debug_1')); 		debugKeysCharacter = ClientPrefs.copyKey(ClientPrefs.keyBinds.get('debug_2'));  		keysArray = [ 			ClientPrefs.copyKey(ClientPrefs.keyBinds.get('note_left')), 			ClientPrefs.copyKey(ClientPrefs.keyBinds.get('note_down')), 			ClientPrefs.copyKey(ClientPrefs.keyBinds.get('note_up')), 			ClientPrefs.copyKey(ClientPrefs.keyBinds.get('note_right')) 		];  		// For the "Just the Two of Us" achievement 		for (i in 0...keysArray.length) 		{ 			keysPressed.push(false); 		}  		if (FlxG.sound.music != null) 			FlxG.sound.music.stop();  		// Gameplay settings 		healthGain = ClientPrefs.getGameplaySetting('healthgain', 1); 		healthLoss = ClientPrefs.getGameplaySetting('healthloss', 1); 		instakillOnMiss = ClientPrefs.getGameplaySetting('instakill', false); 		practiceMode = ClientPrefs.getGameplaySetting('practice', false); 		cpuControlled = ClientPrefs.getGameplaySetting('botplay', false);  		 		 		shader_chromatic_abberation = new ChromaticAberrationEffect(); 		 		 		 		 		 		// var gameCam:FlxCamera = FlxG.camera; 		camGame = new FlxCamera(); 		camHUD = new FlxCamera(); 		camOther = new FlxCamera(); 		camHUD.bgColor.alpha = 0; 		camOther.bgColor.alpha = 0;  		FlxG.cameras.reset(camGame); 		FlxG.cameras.add(camHUD); 		FlxG.cameras.add(camOther); 		grpNoteSplashes = new FlxTypedGroup<NoteSplash>();  		FlxCamera.defaultCameras = [camGame]; 		CustomFadeTransition.nextCamera = camOther; 		//FlxG.cameras.setDefaultDrawTarget(camGame, true);  		persistentUpdate = true; 		persistentDraw = true;  		if (SONG == null) 			SONG = Song.loadFromJson('tutorial');  		Conductor.mapBPMChanges(SONG); 		Conductor.changeBPM(SONG.bpm);  		#if desktop 		storyDifficultyText = CoolUtil.difficulties[storyDifficulty];  		// String that contains the mode defined here so it isn't necessary to call changePresence for each mode 		if (isStoryMode) 		{ 			detailsText = "Story Mode: " + WeekData.getCurrentWeek().weekName; 		} 		else 		{ 			detailsText = "Freeplay"; 		}  		// String for when the game is paused 		detailsPausedText = "Paused - " + detailsText; 		#end  		GameOverSubstate.resetVariables(); 		var songName:String = Paths.formatToSongPath(SONG.song);  		curStage = PlayState.SONG.stage; 		//trace('stage is: ' + curStage); 		if(PlayState.SONG.stage == null || PlayState.SONG.stage.length < 1) { 			switch (songName) 			{ 				case 'spookeez' | 'south' | 'monster': 					curStage = 'spooky'; 				case 'pico' | 'blammed' | 'philly' | 'philly-nice': 					curStage = 'philly'; 				case 'milf' | 'satin-panties' | 'high': 					curStage = 'limo'; 				case 'cocoa' | 'eggnog': 					curStage = 'mall'; 				case 'winter-horrorland': 					curStage = 'mallEvil'; 				case 'senpai' | 'roses': 					curStage = 'school'; 				case 'thorns': 					curStage = 'schoolEvil'; 				default: 					curStage = 'stage'; 			} 		}  		var stageData:StageFile = StageData.getStageFile(curStage); 		if(stageData == null) { //Stage couldn't be found, create a dummy stage for preventing a crash 			stageData = { 				directory: "", 				defaultZoom: 0.9, 				isPixelStage: false, 			 				boyfriend: [770, 100], 				girlfriend: [400, 130], 				opponent: [100, 100] 			}; 		}  		defaultCamZoom = stageData.defaultZoom; 		isPixelStage = stageData.isPixelStage; 		BF_X = stageData.boyfriend[0]; 		BF_Y = stageData.boyfriend[1]; 		GF_X = stageData.girlfriend[0]; 		GF_Y = stageData.girlfriend[1]; 		DAD_X = stageData.opponent[0]; 		DAD_Y = stageData.opponent[1];  		boyfriendGroup = new FlxSpriteGroup(BF_X, BF_Y); 		dadGroup = new FlxSpriteGroup(DAD_X, DAD_Y); 		gfGroup = new FlxSpriteGroup(GF_X, GF_Y);  		switch (curStage) 		{ 			case 'stage': //Week 1 				var bg:BGSprite = new BGSprite('stageback', -600, -200, 0.9, 0.9); 				add(bg);  				var stageFront:BGSprite = new BGSprite('stagefront', -650, 600, 0.9, 0.9); 				stageFront.setGraphicSize(Std.int(stageFront.width * 1.1)); 				stageFront.updateHitbox(); 				add(stageFront);  				if(!ClientPrefs.lowQuality) { 					var stageLight:BGSprite = new BGSprite('stage_light', -125, -100, 0.9, 0.9); 					stageLight.setGraphicSize(Std.int(stageLight.width * 1.1)); 					stageLight.updateHitbox(); 					add(stageLight); 					var stageLight:BGSprite = new BGSprite('stage_light', 1225, -100, 0.9, 0.9); 					stageLight.setGraphicSize(Std.int(stageLight.width * 1.1)); 					stageLight.updateHitbox(); 					stageLight.flipX = true; 					add(stageLight);  					var stageCurtains:BGSprite = new BGSprite('stagecurtains', -500, -300, 1.3, 1.3); 					stageCurtains.setGraphicSize(Std.int(stageCurtains.width * 0.9)); 					stageCurtains.updateHitbox(); 					add(stageCurtains); 				}  			case 'spooky': //Week 2 				if(!ClientPrefs.lowQuality) { 					halloweenBG = new BGSprite('halloween_bg', -200, -100, ['halloweem bg0', 'halloweem bg lightning strike']); 				} else { 					halloweenBG = new BGSprite('halloween_bg_low', -200, -100); 				} 				add(halloweenBG);  				halloweenWhite = new BGSprite(null, -FlxG.width, -FlxG.height, 0, 0); 				halloweenWhite.makeGraphic(Std.int(FlxG.width * 3), Std.int(FlxG.height * 3), FlxColor.WHITE); 				halloweenWhite.alpha = 0; 				halloweenWhite.blend = ADD;  				//PRECACHE SOUNDS 				CoolUtil.precacheSound('thunder_1'); 				CoolUtil.precacheSound('thunder_2');  			case 'philly': //Week 3 				if(!ClientPrefs.lowQuality) { 					var bg:BGSprite = new BGSprite('philly/sky', -100, 0, 0.1, 0.1); 					add(bg); 				} 				 				//addShaderToCamera('game', chromAb); 				//chromAb.setChrome(0.01);  				var city:BGSprite = new BGSprite('philly/city', -10, 0, 0.3, 0.3); 				city.setGraphicSize(Std.int(city.width * 0.85)); 				city.updateHitbox(); 				add(city);  				phillyCityLights = new FlxTypedGroup<BGSprite>(); 				add(phillyCityLights);  				for (i in 0...5) 				{ 					var light:BGSprite = new BGSprite('philly/win' + i, city.x, city.y, 0.3, 0.3); 					light.visible = false; 					light.setGraphicSize(Std.int(light.width * 0.85)); 					light.updateHitbox(); 					phillyCityLights.add(light); 				}  				if(!ClientPrefs.lowQuality) { 					var streetBehind:BGSprite = new BGSprite('philly/behindTrain', -40, 50); 					add(streetBehind); 				}  				phillyTrain = new BGSprite('philly/train', 2000, 360); 				add(phillyTrain);  				trainSound = new FlxSound().loadEmbedded(Paths.sound('train_passes')); 				CoolUtil.precacheSound('train_passes'); 				FlxG.sound.list.add(trainSound);  				var street:BGSprite = new BGSprite('philly/street', -40, 50); 				add(street);  			case 'limo': //Week 4 				var skyBG:BGSprite = new BGSprite('limo/limoSunset', -120, -50, 0.1, 0.1); 				add(skyBG);  				if(!ClientPrefs.lowQuality) { 					limoMetalPole = new BGSprite('gore/metalPole', -500, 220, 0.4, 0.4); 					add(limoMetalPole);  					bgLimo = new BGSprite('limo/bgLimo', -150, 480, 0.4, 0.4, ['background limo pink'], true); 					add(bgLimo);  					limoCorpse = new BGSprite('gore/noooooo', -500, limoMetalPole.y - 130, 0.4, 0.4, ['Henchmen on rail'], true); 					add(limoCorpse);  					limoCorpseTwo = new BGSprite('gore/noooooo', -500, limoMetalPole.y, 0.4, 0.4, ['henchmen death'], true); 					add(limoCorpseTwo);  					grpLimoDancers = new FlxTypedGroup<BackgroundDancer>(); 					add(grpLimoDancers);  					for (i in 0...5) 					{ 						var dancer:BackgroundDancer = new BackgroundDancer((370 * i) + 130, bgLimo.y - 400); 						dancer.scrollFactor.set(0.4, 0.4); 						grpLimoDancers.add(dancer); 					}  					limoLight = new BGSprite('gore/coldHeartKiller', limoMetalPole.x - 180, limoMetalPole.y - 80, 0.4, 0.4); 					add(limoLight);  					grpLimoParticles = new FlxTypedGroup<BGSprite>(); 					add(grpLimoParticles);  					//PRECACHE BLOOD 					var particle:BGSprite = new BGSprite('gore/stupidBlood', -400, -400, 0.4, 0.4, ['blood'], false); 					particle.alpha = 0.01; 					grpLimoParticles.add(particle); 					resetLimoKill();  					//PRECACHE SOUND 					CoolUtil.precacheSound('dancerdeath'); 				}  				limo = new BGSprite('limo/limoDrive', -120, 550, 1, 1, ['Limo stage'], true);  				fastCar = new BGSprite('limo/fastCarLol', -300, 160); 				fastCar.active = true; 				limoKillingState = 0;  			case 'mall': //Week 5 - Cocoa, Eggnog 				var bg:BGSprite = new BGSprite('christmas/bgWalls', -1000, -500, 0.2, 0.2); 				bg.setGraphicSize(Std.int(bg.width * 0.8)); 				bg.updateHitbox(); 				add(bg);  				if(!ClientPrefs.lowQuality) { 					upperBoppers = new BGSprite('christmas/upperBop', -240, -90, 0.33, 0.33, ['Upper Crowd Bob']); 					upperBoppers.setGraphicSize(Std.int(upperBoppers.width * 0.85)); 					upperBoppers.updateHitbox(); 					add(upperBoppers);  					var bgEscalator:BGSprite = new BGSprite('christmas/bgEscalator', -1100, -600, 0.3, 0.3); 					bgEscalator.setGraphicSize(Std.int(bgEscalator.width * 0.9)); 					bgEscalator.updateHitbox(); 					add(bgEscalator); 				}  				var tree:BGSprite = new BGSprite('christmas/christmasTree', 370, -250, 0.40, 0.40); 				add(tree);  				bottomBoppers = new BGSprite('christmas/bottomBop', -300, 140, 0.9, 0.9, ['Bottom Level Boppers Idle']); 				bottomBoppers.animation.addByPrefix('hey', 'Bottom Level Boppers HEY', 24, false); 				bottomBoppers.setGraphicSize(Std.int(bottomBoppers.width * 1)); 				bottomBoppers.updateHitbox(); 				add(bottomBoppers);  				var fgSnow:BGSprite = new BGSprite('christmas/fgSnow', -600, 700); 				add(fgSnow);  				santa = new BGSprite('christmas/santa', -840, 150, 1, 1, ['santa idle in fear']); 				add(santa); 				CoolUtil.precacheSound('Lights_Shut_off');  			case 'mallEvil': //Week 5 - Winter Horrorland 				var bg:BGSprite = new BGSprite('christmas/evilBG', -400, -500, 0.2, 0.2); 				bg.setGraphicSize(Std.int(bg.width * 0.8)); 				bg.updateHitbox(); 				add(bg);  				var evilTree:BGSprite = new BGSprite('christmas/evilTree', 300, -300, 0.2, 0.2); 				add(evilTree);  				var evilSnow:BGSprite = new BGSprite('christmas/evilSnow', -200, 700); 				add(evilSnow);  			case 'school': //Week 6 - Senpai, Roses 				GameOverSubstate.deathSoundName = 'fnf_loss_sfx-pixel'; 				GameOverSubstate.loopSoundName = 'gameOver-pixel'; 				GameOverSubstate.endSoundName = 'gameOverEnd-pixel'; 				GameOverSubstate.characterName = 'bf-pixel-dead';  				var bgSky:BGSprite = new BGSprite('weeb/weebSky', 0, 0, 0.1, 0.1); 				add(bgSky); 				bgSky.antialiasing = false;  				var repositionShit = -200;  				var bgSchool:BGSprite = new BGSprite('weeb/weebSchool', repositionShit, 0, 0.6, 0.90); 				add(bgSchool); 				bgSchool.antialiasing = false;  				var bgStreet:BGSprite = new BGSprite('weeb/weebStreet', repositionShit, 0, 0.95, 0.95); 				add(bgStreet); 				bgStreet.antialiasing = false;  				var widShit = Std.int(bgSky.width * 6); 				if(!ClientPrefs.lowQuality) { 					var fgTrees:BGSprite = new BGSprite('weeb/weebTreesBack', repositionShit + 170, 130, 0.9, 0.9); 					fgTrees.setGraphicSize(Std.int(widShit * 0.8)); 					fgTrees.updateHitbox(); 					add(fgTrees); 					fgTrees.antialiasing = false; 				}  				var bgTrees:FlxSprite = new FlxSprite(repositionShit - 380, -800); 				bgTrees.frames = Paths.getPackerAtlas('weeb/weebTrees'); 				bgTrees.animation.add('treeLoop', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], 12); 				bgTrees.animation.play('treeLoop'); 				bgTrees.scrollFactor.set(0.85, 0.85); 				add(bgTrees); 				bgTrees.antialiasing = false;  				if(!ClientPrefs.lowQuality) { 					var treeLeaves:BGSprite = new BGSprite('weeb/petals', repositionShit, -40, 0.85, 0.85, ['PETALS ALL'], true); 					treeLeaves.setGraphicSize(widShit); 					treeLeaves.updateHitbox(); 					add(treeLeaves); 					treeLeaves.antialiasing = false; 				}  				bgSky.setGraphicSize(widShit); 				bgSchool.setGraphicSize(widShit); 				bgStreet.setGraphicSize(widShit); 				bgTrees.setGraphicSize(Std.int(widShit * 1.4));  				bgSky.updateHitbox(); 				bgSchool.updateHitbox(); 				bgStreet.updateHitbox(); 				bgTrees.updateHitbox();  				if(!ClientPrefs.lowQuality) { 					bgGirls = new BackgroundGirls(-100, 190); 					bgGirls.scrollFactor.set(0.9, 0.9);  					bgGirls.setGraphicSize(Std.int(bgGirls.width * daPixelZoom)); 					bgGirls.updateHitbox(); 					add(bgGirls); 				}  			case 'schoolEvil': //Week 6 - Thorns 				GameOverSubstate.deathSoundName = 'fnf_loss_sfx-pixel'; 				GameOverSubstate.loopSoundName = 'gameOver-pixel'; 				GameOverSubstate.endSoundName = 'gameOverEnd-pixel'; 				GameOverSubstate.characterName = 'bf-pixel-dead';  				/*if(!ClientPrefs.lowQuality) { //Does this even do something? 					var waveEffectBG = new FlxWaveEffect(FlxWaveMode.ALL, 2, -1, 3, 2); 					var waveEffectFG = new FlxWaveEffect(FlxWaveMode.ALL, 2, -1, 5, 2); 				}*/ 				var posX = 400; 				var posY = 200; 				if(!ClientPrefs.lowQuality) { 					var bg:BGSprite = new BGSprite('weeb/animatedEvilSchool', posX, posY, 0.8, 0.9, ['background 2'], true); 					bg.scale.set(6, 6); 					bg.antialiasing = false; 					add(bg);  					bgGhouls = new BGSprite('weeb/bgGhouls', -100, 190, 0.9, 0.9, ['BG freaks glitch instance'], false); 					bgGhouls.setGraphicSize(Std.int(bgGhouls.width * daPixelZoom)); 					bgGhouls.updateHitbox(); 					bgGhouls.visible = false; 					bgGhouls.antialiasing = false; 					add(bgGhouls); 				} else { 					var bg:BGSprite = new BGSprite('weeb/animatedEvilSchool_low', posX, posY, 0.8, 0.9); 					bg.scale.set(6, 6); 					bg.antialiasing = false; 					add(bg); 				} 		}  		if(isPixelStage) { 			introSoundsSuffix = '-pixel'; 		}  		add(gfGroup);  		// Shitty layering but whatev it works LOL 		if (curStage == 'limo') 			add(limo);  		add(dadGroup); 		add(boyfriendGroup); 		 		if(curStage == 'spooky') { 			add(halloweenWhite); 		}  		#if LUA_ALLOWED 		luaDebugGroup = new FlxTypedGroup<DebugLuaText>(); 		luaDebugGroup.cameras = [camOther]; 		add(luaDebugGroup); 		#end  		if(curStage == 'philly') { 			phillyCityLightsEvent = new FlxTypedGroup<BGSprite>(); 			for (i in 0...5) 			{ 				var light:BGSprite = new BGSprite('philly/win' + i, -10, 0, 0.3, 0.3); 				light.visible = false; 				light.setGraphicSize(Std.int(light.width * 0.85)); 				light.updateHitbox(); 				phillyCityLightsEvent.add(light); 			} 		}   		// "GLOBAL" SCRIPTS 		#if LUA_ALLOWED 		var filesPushed:Array<String> = []; 		var foldersToCheck:Array<String> = [Paths.getPreloadPath('scripts/')];  		#if MODS_ALLOWED 		foldersToCheck.insert(0, Paths.mods('scripts/')); 		if(Paths.currentModDirectory != null && Paths.currentModDirectory.length > 0) 			foldersToCheck.insert(0, Paths.mods(Paths.currentModDirectory + '/scripts/')); 		#end  		for (folder in foldersToCheck) 		{ 			if(FileSystem.exists(folder)) 			{ 				for (file in FileSystem.readDirectory(folder)) 				{ 					if(file.endsWith('.lua') && !filesPushed.contains(file)) 					{ 						luaArray.push(new FunkinLua(folder + file)); 						filesPushed.push(file); 					} 				} 			} 		} 		#end 		  		// STAGE SCRIPTS 		#if (MODS_ALLOWED && LUA_ALLOWED) 		var doPush:Bool = false; 		var luaFile:String = 'stages/' + curStage + '.lua'; 		if(FileSystem.exists(Paths.modFolders(luaFile))) { 			luaFile = Paths.modFolders(luaFile); 			doPush = true; 		} else { 			luaFile = Paths.getPreloadPath(luaFile); 			if(FileSystem.exists(luaFile)) { 				doPush = true; 			} 		}  		if(doPush)  			luaArray.push(new FunkinLua(luaFile)); 		#end  		if(!modchartSprites.exists('blammedLightsBlack')) { //Creates blammed light black fade in case you didn't make your own 			blammedLightsBlack = new ModchartSprite(FlxG.width * -0.5, FlxG.height * -0.5); 			blammedLightsBlack.makeGraphic(Std.int(FlxG.width * 2), Std.int(FlxG.height * 2), FlxColor.BLACK); 			var position:Int = members.indexOf(gfGroup); 			if(members.indexOf(boyfriendGroup) < position) { 				position = members.indexOf(boyfriendGroup); 			} else if(members.indexOf(dadGroup) < position) { 				position = members.indexOf(dadGroup); 			} 			insert(position, blammedLightsBlack);  			blammedLightsBlack.wasAdded = true; 			modchartSprites.set('blammedLightsBlack', blammedLightsBlack); 		} 		if(curStage == 'philly') insert(members.indexOf(blammedLightsBlack) + 1, phillyCityLightsEvent); 		blammedLightsBlack = modchartSprites.get('blammedLightsBlack'); 		blammedLightsBlack.alpha = 0.0;  		var gfVersion:String = SONG.gfVersion; 		if(gfVersion == null || gfVersion.length < 1) { 			switch (curStage) 			{ 				case 'limo': 					gfVersion = 'gf-car'; 				case 'mall' | 'mallEvil': 					gfVersion = 'gf-christmas'; 				case 'school' | 'schoolEvil': 					gfVersion = 'gf-pixel'; 				default: 					gfVersion = 'gf'; 			} 			SONG.gfVersion = gfVersion; //Fix for the Chart Editor 		}  		gf = new Character(0, 0, gfVersion); 		startCharacterPos(gf); 		gf.scrollFactor.set(0.95, 0.95); 		gfGroup.add(gf); 		startCharacterLua(gf.curCharacter);  		dad = new Character(0, 0, SONG.player2); 		startCharacterPos(dad, true); 		dadGroup.add(dad); 		startCharacterLua(dad.curCharacter); 		 		boyfriend = new Boyfriend(0, 0, SONG.player1); 		startCharacterPos(boyfriend); 		boyfriendGroup.add(boyfriend); 		startCharacterLua(boyfriend.curCharacter); 		 		var camPos:FlxPoint = new FlxPoint(gf.getGraphicMidpoint().x, gf.getGraphicMidpoint().y); 		camPos.x += gf.cameraPosition[0]; 		camPos.y += gf.cameraPosition[1];  		if(dad.curCharacter.startsWith('gf')) { 			dad.setPosition(GF_X, GF_Y); 			gf.visible = false; 		}  		switch(curStage) 		{ 			case 'limo': 				resetFastCar(); 				insert(members.indexOf(gfGroup) - 1, fastCar); 			 			case 'schoolEvil': 				var evilTrail = new FlxTrail(dad, null, 4, 24, 0.3, 0.069); //nice 				insert(members.indexOf(dadGroup) - 1, evilTrail); 		}  		var file:String = Paths.json(songName + '/dialogue'); //Checks for json/Psych Engine dialogue 		if (OpenFlAssets.exists(file)) { 			dialogueJson = DialogueBoxPsych.parseDialogue(file); 		}  		var file:String = Paths.txt(songName + '/' + songName + 'Dialogue'); //Checks for vanilla/Senpai dialogue 		if (OpenFlAssets.exists(file)) { 			dialogue = CoolUtil.coolTextFile(file); 		} 		var doof:DialogueBox = new DialogueBox(false, dialogue); 		// doof.x += 70; 		// doof.y = FlxG.height * 0.5; 		doof.scrollFactor.set(); 		doof.finishThing = startCountdown; 		doof.nextDialogueThing = startNextDialogue; 		doof.skipDialogueThing = skipDialogue;  		Conductor.songPosition = -5000;  		strumLine = new FlxSprite(ClientPrefs.middleScroll ? STRUM_X_MIDDLESCROLL : STRUM_X, 50).makeGraphic(FlxG.width, 10); 		if(ClientPrefs.downScroll) strumLine.y = FlxG.height - 150; 		strumLine.scrollFactor.set();  		var showTime:Bool = (ClientPrefs.timeBarType != 'Disabled'); 		timeTxt = new FlxText(STRUM_X + (FlxG.width / 2) - 248, 19, 400, "", 32); 		timeTxt.setFormat(Paths.font("vcr.ttf"), 32, FlxColor.WHITE, CENTER, FlxTextBorderStyle.OUTLINE, FlxColor.BLACK); 		timeTxt.scrollFactor.set(); 		timeTxt.alpha = 0; 		timeTxt.borderSize = 2; 		timeTxt.visible = showTime; 		if(ClientPrefs.downScroll) timeTxt.y = FlxG.height - 44;  		if(ClientPrefs.timeBarType == 'Song Name') 		{ 			timeTxt.text = SONG.song; 		} 		updateTime = showTime;  		timeBarBG = new AttachedSprite('timeBar'); 		timeBarBG.x = timeTxt.x; 		timeBarBG.y = timeTxt.y + (timeTxt.height / 4); 		timeBarBG.scrollFactor.set(); 		timeBarBG.alpha = 0; 		timeBarBG.visible = showTime; 		timeBarBG.color = FlxColor.BLACK; 		timeBarBG.xAdd = -4; 		timeBarBG.yAdd = -4; 		add(timeBarBG);  		timeBar = new FlxBar(timeBarBG.x + 4, timeBarBG.y + 4, LEFT_TO_RIGHT, Std.int(timeBarBG.width - 8), Std.int(timeBarBG.height - 8), this, 			'songPercent', 0, 1); 		timeBar.scrollFactor.set(); 		timeBar.createFilledBar(0xFF000000, 0xFFFFFFFF); 		timeBar.numDivisions = 800; //How much lag this causes?? Should i tone it down to idk, 400 or 200? 		timeBar.alpha = 0; 		timeBar.visible = showTime; 		add(timeBar); 		add(timeTxt); 		timeBarBG.sprTracker = timeBar;  		strumLineNotes = new FlxTypedGroup<StrumNote>(); 		add(strumLineNotes); 		add(grpNoteSplashes);  		if(ClientPrefs.timeBarType == 'Song Name') 		{ 			timeTxt.size = 24; 			timeTxt.y += 3; 		}  		var splash:NoteSplash = new NoteSplash(100, 100, 0); 		grpNoteSplashes.add(splash); 		splash.alpha = 0.0;  		opponentStrums = new FlxTypedGroup<StrumNote>(); 		playerStrums = new FlxTypedGroup<StrumNote>();  		// startCountdown();  		generateSong(SONG.song); 		#if LUA_ALLOWED 		for (notetype in noteTypeMap.keys()) 		{ 			var luaToLoad:String = Paths.modFolders('custom_notetypes/' + notetype + '.lua'); 			if(FileSystem.exists(luaToLoad)) 			{ 				luaArray.push(new FunkinLua(luaToLoad)); 			} 			else 			{ 				luaToLoad = Paths.getPreloadPath('custom_notetypes/' + notetype + '.lua'); 				if(FileSystem.exists(luaToLoad)) 				{ 					luaArray.push(new FunkinLua(luaToLoad)); 				} 			} 		} 		for (event in eventPushedMap.keys()) 		{ 			var luaToLoad:String = Paths.modFolders('custom_events/' + event + '.lua'); 			if(FileSystem.exists(luaToLoad)) 			{ 				luaArray.push(new FunkinLua(luaToLoad)); 			} 			else 			{ 				luaToLoad = Paths.getPreloadPath('custom_events/' + event + '.lua'); 				if(FileSystem.exists(luaToLoad)) 				{ 					luaArray.push(new FunkinLua(luaToLoad)); 				} 			} 		} 		#end 		noteTypeMap.clear(); 		noteTypeMap = null; 		eventPushedMap.clear(); 		eventPushedMap = null;  		// After all characters being loaded, it makes then invisible 0.01s later so that the player won't freeze when you change characters 		// add(strumLine);  		camFollow = new FlxPoint(); 		camFollowPos = new FlxObject(0, 0, 1, 1);  		snapCamFollowToPos(camPos.x, camPos.y); 		if (prevCamFollow != null) 		{ 			camFollow = prevCamFollow; 			prevCamFollow = null; 		} 		if (prevCamFollowPos != null) 		{ 			camFollowPos = prevCamFollowPos; 			prevCamFollowPos = null; 		} 		add(camFollowPos);  		FlxG.camera.follow(camFollowPos, LOCKON, 1); 		// FlxG.camera.setScrollBounds(0, FlxG.width, 0, FlxG.height); 		FlxG.camera.zoom = defaultCamZoom; 		FlxG.camera.focusOn(camFollow);  		FlxG.worldBounds.set(0, 0, FlxG.width, FlxG.height);  		FlxG.fixedTimestep = false; 		moveCameraSection(0);  		healthBarBG = new AttachedSprite('healthBar'); 		healthBarBG.y = FlxG.height * 0.89; 		healthBarBG.screenCenter(X); 		healthBarBG.scrollFactor.set(); 		healthBarBG.visible = !ClientPrefs.hideHud; 		healthBarBG.xAdd = -4; 		healthBarBG.yAdd = -4; 		add(healthBarBG); 		if(ClientPrefs.downScroll) healthBarBG.y = 0.11 * FlxG.height;  		healthBar = new FlxBar(healthBarBG.x + 4, healthBarBG.y + 4, RIGHT_TO_LEFT, Std.int(healthBarBG.width - 8), Std.int(healthBarBG.height - 8), this, 			'health', 0, 2); 		healthBar.scrollFactor.set(); 		// healthBar 		healthBar.visible = !ClientPrefs.hideHud; 		healthBar.alpha = ClientPrefs.healthBarAlpha; 		add(healthBar); 		healthBarBG.sprTracker = healthBar;  		iconP1 = new HealthIcon(boyfriend.healthIcon, true); 		iconP1.y = healthBar.y - 75; 		iconP1.visible = !ClientPrefs.hideHud; 		iconP1.alpha = ClientPrefs.healthBarAlpha; 		add(iconP1);  		iconP2 = new HealthIcon(dad.healthIcon, false); 		iconP2.y = healthBar.y - 75; 		iconP2.visible = !ClientPrefs.hideHud; 		iconP2.alpha = ClientPrefs.healthBarAlpha; 		add(iconP2); 		reloadHealthBarColors();  		scoreTxt = new FlxText(0, healthBarBG.y + 36, FlxG.width, "", 20); 		scoreTxt.setFormat(Paths.font("vcr.ttf"), 20, FlxColor.WHITE, CENTER, FlxTextBorderStyle.OUTLINE, FlxColor.BLACK); 		scoreTxt.scrollFactor.set(); 		scoreTxt.borderSize = 1.25; 		scoreTxt.visible = !ClientPrefs.hideHud; 		add(scoreTxt);  		botplayTxt = new FlxText(400, timeBarBG.y + 55, FlxG.width - 800, "skill issue mode", 32); 		botplayTxt.setFormat(Paths.font("vcr.ttf"), 32, FlxColor.WHITE, CENTER, FlxTextBorderStyle.OUTLINE, FlxColor.BLACK); 		botplayTxt.scrollFactor.set(); 		botplayTxt.borderSize = 1.25; 		botplayTxt.visible = cpuControlled; 		add(botplayTxt); 		if(ClientPrefs.downScroll) { 			botplayTxt.y = timeBarBG.y - 78; 		}  		strumLineNotes.cameras = [camHUD]; 		grpNoteSplashes.cameras = [camHUD]; 		notes.cameras = [camHUD]; 		healthBar.cameras = [camHUD]; 		healthBarBG.cameras = [camHUD]; 		iconP1.cameras = [camHUD]; 		iconP2.cameras = [camHUD]; 		scoreTxt.cameras = [camHUD]; 		botplayTxt.cameras = [camHUD]; 		timeBar.cameras = [camHUD]; 		timeBarBG.cameras = [camHUD]; 		timeTxt.cameras = [camHUD]; 		doof.cameras = [camHUD];  		// if (SONG.song == 'South') 		// FlxG.camera.alpha = 0.7; 		// UI_camera.zoom = 1;  		// cameras = [FlxG.cameras.list[1]]; 		startingSong = true;  		// SONG SPECIFIC SCRIPTS 		#if LUA_ALLOWED 		var filesPushed:Array<String> = []; 		var foldersToCheck:Array<String> = [Paths.getPreloadPath('data/' + Paths.formatToSongPath(SONG.song) + '/')];  		#if MODS_ALLOWED 		foldersToCheck.insert(0, Paths.mods('data/' + Paths.formatToSongPath(SONG.song) + '/')); 		if(Paths.currentModDirectory != null && Paths.currentModDirectory.length > 0) 			foldersToCheck.insert(0, Paths.mods(Paths.currentModDirectory + '/data/' + Paths.formatToSongPath(SONG.song) + '/')); 		#end  		for (folder in foldersToCheck) 		{ 			if(FileSystem.exists(folder)) 			{ 				for (file in FileSystem.readDirectory(folder)) 				{ 					if(file.endsWith('.lua') && !filesPushed.contains(file)) 					{ 						luaArray.push(new FunkinLua(folder + file)); 						filesPushed.push(file); 					} 				} 			} 		} 		#end 		 		var daSong:String = Paths.formatToSongPath(curSong); 		if (isStoryMode && !seenCutscene) 		{ 			switch (daSong) 			{ 				case "monster": 					var whiteScreen:FlxSprite = new FlxSprite(0, 0).makeGraphic(Std.int(FlxG.width * 2), Std.int(FlxG.height * 2), FlxColor.WHITE); 					add(whiteScreen); 					whiteScreen.scrollFactor.set(); 					whiteScreen.blend = ADD; 					camHUD.visible = false; 					snapCamFollowToPos(dad.getMidpoint().x + 150, dad.getMidpoint().y - 100); 					inCutscene = true;  					FlxTween.tween(whiteScreen, {alpha: 0}, 1, { 						startDelay: 0.1, 						ease: FlxEase.linear, 						onComplete: function(twn:FlxTween) 						{ 							camHUD.visible = true; 							remove(whiteScreen); 							startCountdown(); 						} 					}); 					FlxG.sound.play(Paths.soundRandom('thunder_', 1, 2)); 					gf.playAnim('scared', true); 					boyfriend.playAnim('scared', true);  				case "winter-horrorland": 					var blackScreen:FlxSprite = new FlxSprite().makeGraphic(Std.int(FlxG.width * 2), Std.int(FlxG.height * 2), FlxColor.BLACK); 					add(blackScreen); 					blackScreen.scrollFactor.set(); 					camHUD.visible = false; 					inCutscene = true;  					FlxTween.tween(blackScreen, {alpha: 0}, 0.7, { 						ease: FlxEase.linear, 						onComplete: function(twn:FlxTween) { 							remove(blackScreen); 						} 					}); 					FlxG.sound.play(Paths.sound('Lights_Turn_On')); 					snapCamFollowToPos(400, -2050); 					FlxG.camera.focusOn(camFollow); 					FlxG.camera.zoom = 1.5;  					new FlxTimer().start(0.8, function(tmr:FlxTimer) 					{ 						camHUD.visible = true; 						remove(blackScreen); 						FlxTween.tween(FlxG.camera, {zoom: defaultCamZoom}, 2.5, { 							ease: FlxEase.quadInOut, 							onComplete: function(twn:FlxTween) 							{ 								startCountdown(); 							} 						}); 					}); 				case 'senpai' | 'roses' | 'thorns': 					if(daSong == 'roses') FlxG.sound.play(Paths.sound('ANGRY')); 					schoolIntro(doof);  				default: 					startCountdown(); 			} 			seenCutscene = true; 		} else { 			startCountdown(); 		} 		RecalculateRating();  		//PRECACHING MISS SOUNDS BECAUSE I THINK THEY CAN LAG PEOPLE AND FUCK THEM UP IDK HOW HAXE WORKS 		CoolUtil.precacheSound('missnote1'); 		CoolUtil.precacheSound('missnote2'); 		CoolUtil.precacheSound('missnote3');  		#if desktop 		// Updating Discord Rich Presence. 		DiscordClient.changePresence(detailsText, SONG.song + " (" + storyDifficultyText + ")", iconP2.getCharacter()); 		#end  		if(!ClientPrefs.controllerMode) 		{ 			FlxG.stage.addEventListener(KeyboardEvent.KEY_DOWN, onKeyPress); 			FlxG.stage.addEventListener(KeyboardEvent.KEY_UP, onKeyRelease); 		}  		Conductor.safeZoneOffset = (ClientPrefs.safeFrames / 60) * 1000; 		callOnLuas('onCreatePost', []); 		 		super.create();  		Paths.clearUnusedMemory(); 	}  	function set_songSpeed(value:Float):Float 	{ 		if(generatedMusic) 		{ 			var ratio:Float = value / songSpeed; //funny word huh 			for (note in notes) 			{ 				if(note.isSustainNote && !note.animation.curAnim.name.endsWith('end')) 				{ 					note.scale.y *= ratio; 					note.updateHitbox(); 				} 			} 			for (note in unspawnNotes) 			{ 				if(note.isSustainNote && !note.animation.curAnim.name.endsWith('end')) 				{ 					note.scale.y *= ratio; 					note.updateHitbox(); 				} 			} 		} 		songSpeed = value; 		return value; 	}  	public function addTextToDebug(text:String) { 		#if LUA_ALLOWED 		luaDebugGroup.forEachAlive(function(spr:DebugLuaText) { 			spr.y += 20; 		});  		if(luaDebugGroup.members.length > 34) { 			var blah = luaDebugGroup.members[34]; 			blah.destroy(); 			luaDebugGroup.remove(blah); 		} 		luaDebugGroup.insert(0, new DebugLuaText(text, luaDebugGroup)); 		#end 	}  	public function reloadHealthBarColors() { 		healthBar.createFilledBar(FlxColor.fromRGB(dad.healthColorArray[0], dad.healthColorArray[1], dad.healthColorArray[2]), 			FlxColor.fromRGB(boyfriend.healthColorArray[0], boyfriend.healthColorArray[1], boyfriend.healthColorArray[2])); 			 		healthBar.updateBar(); 	}  	public function addCharacterToList(newCharacter:String, type:Int) { 		switch(type) { 			case 0: 				if(!boyfriendMap.exists(newCharacter)) { 					var newBoyfriend:Boyfriend = new Boyfriend(0, 0, newCharacter); 					boyfriendMap.set(newCharacter, newBoyfriend); 					boyfriendGroup.add(newBoyfriend); 					startCharacterPos(newBoyfriend); 					newBoyfriend.alpha = 0.00001; 					startCharacterLua(newBoyfriend.curCharacter); 				}  			case 1: 				if(!dadMap.exists(newCharacter)) { 					var newDad:Character = new Character(0, 0, newCharacter); 					dadMap.set(newCharacter, newDad); 					dadGroup.add(newDad); 					startCharacterPos(newDad, true); 					newDad.alpha = 0.00001; 					startCharacterLua(newDad.curCharacter); 				}  			case 2: 				if(!gfMap.exists(newCharacter)) { 					var newGf:Character = new Character(0, 0, newCharacter); 					newGf.scrollFactor.set(0.95, 0.95); 					gfMap.set(newCharacter, newGf); 					gfGroup.add(newGf); 					startCharacterPos(newGf); 					newGf.alpha = 0.00001; 					startCharacterLua(newGf.curCharacter); 				} 		} 	}  	function startCharacterLua(name:String) 	{ 		#if LUA_ALLOWED 		var doPush:Bool = false; 		var luaFile:String = 'characters/' + name + '.lua'; 		if(FileSystem.exists(Paths.modFolders(luaFile))) { 			luaFile = Paths.modFolders(luaFile); 			doPush = true; 		} else { 			luaFile = Paths.getPreloadPath(luaFile); 			if(FileSystem.exists(luaFile)) { 				doPush = true; 			} 		} 		 		if(doPush) 		{ 			for (lua in luaArray) 			{ 				if(lua.scriptName == luaFile) return; 			} 			luaArray.push(new FunkinLua(luaFile)); 		} 		#end 	}  	 	   public function addShaderToCamera(cam:String,effect:ShaderEffect){//STOLE FROM ANDROMEDA 	   	   	   		switch(cam.toLowerCase()) { 			case 'camhud' | 'hud': 					camHUDShaders.push(effect); 					var newCamEffects:Array<BitmapFilter>=[]; // IT SHUTS HAXE UP IDK WHY BUT WHATEVER IDK WHY I CANT JUST ARRAY<SHADERFILTER> 					for(i in camHUDShaders){ 					  newCamEffects.push(new ShaderFilter(i.shader)); 					} 					camHUD.setFilters(newCamEffects); 			case 'camother' | 'other': 					camOtherShaders.push(effect); 					var newCamEffects:Array<BitmapFilter>=[]; // IT SHUTS HAXE UP IDK WHY BUT WHATEVER IDK WHY I CANT JUST ARRAY<SHADERFILTER> 					for(i in camOtherShaders){ 					  newCamEffects.push(new ShaderFilter(i.shader)); 					} 					camOther.setFilters(newCamEffects); 			case 'camgame' | 'game': 					camGameShaders.push(effect); 					var newCamEffects:Array<BitmapFilter>=[]; // IT SHUTS HAXE UP IDK WHY BUT WHATEVER IDK WHY I CANT JUST ARRAY<SHADERFILTER> 					for(i in camGameShaders){ 					  newCamEffects.push(new ShaderFilter(i.shader)); 					} 					camGame.setFilters(newCamEffects); 			default: 				if(modchartSprites.exists(cam)) { 					Reflect.setProperty(modchartSprites.get(cam),"shader",effect.shader); 				} else if(modchartTexts.exists(cam)) { 					Reflect.setProperty(modchartTexts.get(cam),"shader",effect.shader); 				} else { 					var OBJ = Reflect.getProperty(PlayState.instance,cam); 					Reflect.setProperty(OBJ,"shader", effect.shader); 				} 			 			 				 				 		} 	   	   	   	     }    public function removeShaderFromCamera(cam:String,effect:ShaderEffect){ 	   	   		switch(cam.toLowerCase()) { 			case 'camhud' | 'hud':      camHUDShaders.remove(effect);     var newCamEffects:Array<BitmapFilter>=[];     for(i in camHUDShaders){       newCamEffects.push(new ShaderFilter(i.shader));     }     camHUD.setFilters(newCamEffects); 			case 'camother' | 'other':  					camOtherShaders.remove(effect); 					var newCamEffects:Array<BitmapFilter>=[]; 					for(i in camOtherShaders){ 					  newCamEffects.push(new ShaderFilter(i.shader)); 					} 					camOther.setFilters(newCamEffects); 			default:  				camGameShaders.remove(effect); 				var newCamEffects:Array<BitmapFilter>=[]; 				for(i in camGameShaders){ 				  newCamEffects.push(new ShaderFilter(i.shader)); 				} 				camGame.setFilters(newCamEffects); 		} 		 	     } 	 	 	   public function clearShaderFromCamera(cam:String){ 	   	   		switch(cam.toLowerCase()) { 			case 'camhud' | 'hud':  				camHUDShaders = []; 				var newCamEffects:Array<BitmapFilter>=[]; 				camHUD.setFilters(newCamEffects); 			case 'camother' | 'other':  				camOtherShaders = []; 				var newCamEffects:Array<BitmapFilter>=[]; 				camOther.setFilters(newCamEffects); 			default:  				camGameShaders = []; 				var newCamEffects:Array<BitmapFilter>=[]; 				camGame.setFilters(newCamEffects); 		} 		 	     } 	 	 	 	 	function startCharacterPos(char:Character, ?gfCheck:Bool = false) { 		if(gfCheck && char.curCharacter.startsWith('gf')) { //IF DAD IS GIRLFRIEND, HE GOES TO HER POSITION 			char.setPosition(GF_X, GF_Y); 			char.scrollFactor.set(0.95, 0.95); 		} 		char.x += char.positionArray[0]; 		char.y += char.positionArray[1]; 	}  	public function startVideo(name:String):Void { 		#if VIDEOS_ALLOWED 		var foundFile:Bool = false; 		var fileName:String = #if MODS_ALLOWED Paths.modFolders('videos/' + name + '.' + Paths.VIDEO_EXT); #else ''; #end 		#if sys 		if(FileSystem.exists(fileName)) { 			foundFile = true; 		} 		#end  		if(!foundFile) { 			fileName = Paths.video(name); 			#if sys 			if(FileSystem.exists(fileName)) { 			#else 			if(OpenFlAssets.exists(fileName)) { 			#end 				foundFile = true; 			} 		}  		if(foundFile) { 			inCutscene = true; 			var bg = new FlxSprite(-FlxG.width, -FlxG.height).makeGraphic(FlxG.width * 3, FlxG.height * 3, FlxColor.BLACK); 			bg.scrollFactor.set(); 			bg.cameras = [camHUD]; 			add(bg);  			(new FlxVideo(fileName)).finishCallback = function() { 				remove(bg); 				if(endingSong) { 					endSong(); 				} else { 					startCountdown(); 				} 			} 			return; 		} else { 			FlxG.log.warn('Couldnt find video file: ' + fileName);                         if(endingSong) { 		                endSong(); 		        } else { 				startCountdown(); 			} 		} 		#end 		if(endingSong) { 			endSong(); 		} else { 			startCountdown(); 		} 	}  	var dialogueCount:Int = 0; 	public var psychDialogue:DialogueBoxPsych; 	//You don't have to add a song, just saying. You can just do "startDialogue(dialogueJson);" and it should work 	public function startDialogue(dialogueFile:DialogueFile, ?song:String = null):Void 	{ 		// TO DO: Make this more flexible, maybe? 		if(psychDialogue != null) return;  		if(dialogueFile.dialogue.length > 0) { 			inCutscene = true; 			CoolUtil.precacheSound('dialogue'); 			CoolUtil.precacheSound('dialogueClose'); 			psychDialogue = new DialogueBoxPsych(dialogueFile, song); 			psychDialogue.scrollFactor.set(); 			if(endingSong) { 				psychDialogue.finishThing = function() { 					psychDialogue = null; 					endSong(); 				} 			} else { 				psychDialogue.finishThing = function() { 					psychDialogue = null; 					startCountdown(); 				} 			} 			psychDialogue.nextDialogueThing = startNextDialogue; 			psychDialogue.skipDialogueThing = skipDialogue; 			psychDialogue.cameras = [camHUD]; 			add(psychDialogue); 		} else { 			FlxG.log.warn('Your dialogue file is badly formatted!'); 			if(endingSong) { 				endSong(); 			} else { 				startCountdown(); 			} 		} 	}  	function schoolIntro(?dialogueBox:DialogueBox):Void 	{ 		inCutscene = true; 		var black:FlxSprite = new FlxSprite(-100, -100).makeGraphic(FlxG.width * 2, FlxG.height * 2, FlxColor.BLACK); 		black.scrollFactor.set(); 		add(black);  		var red:FlxSprite = new FlxSprite(-100, -100).makeGraphic(FlxG.width * 2, FlxG.height * 2, 0xFFff1b31); 		red.scrollFactor.set();  		var senpaiEvil:FlxSprite = new FlxSprite(); 		senpaiEvil.frames = Paths.getSparrowAtlas('weeb/senpaiCrazy'); 		senpaiEvil.animation.addByPrefix('idle', 'Senpai Pre Explosion', 24, false); 		senpaiEvil.setGraphicSize(Std.int(senpaiEvil.width * 6)); 		senpaiEvil.scrollFactor.set(); 		senpaiEvil.updateHitbox(); 		senpaiEvil.screenCenter(); 		senpaiEvil.x += 300;  		var songName:String = Paths.formatToSongPath(SONG.song); 		if (songName == 'roses' || songName == 'thorns') 		{ 			remove(black);  			if (songName == 'thorns') 			{ 				add(red); 				camHUD.visible = false; 			} 		}  		new FlxTimer().start(0.3, function(tmr:FlxTimer) 		{ 			black.alpha -= 0.15;  			if (black.alpha > 0) 			{ 				tmr.reset(0.3); 			} 			else 			{ 				if (dialogueBox != null) 				{ 					if (Paths.formatToSongPath(SONG.song) == 'thorns') 					{ 						add(senpaiEvil); 						senpaiEvil.alpha = 0; 						new FlxTimer().start(0.3, function(swagTimer:FlxTimer) 						{ 							senpaiEvil.alpha += 0.15; 							if (senpaiEvil.alpha < 1) 							{ 								swagTimer.reset(); 							} 							else 							{ 								senpaiEvil.animation.play('idle'); 								FlxG.sound.play(Paths.sound('Senpai_Dies'), 1, false, null, true, function() 								{ 									remove(senpaiEvil); 									remove(red); 									FlxG.camera.fade(FlxColor.WHITE, 0.01, true, function() 									{ 										add(dialogueBox); 										camHUD.visible = true; 									}, true); 								}); 								new FlxTimer().start(3.2, function(deadTime:FlxTimer) 								{ 									FlxG.camera.fade(FlxColor.WHITE, 1.6, false); 								}); 							} 						}); 					} 					else 					{ 						add(dialogueBox); 					} 				} 				else 					startCountdown();  				remove(black); 			} 		}); 	}  	var startTimer:FlxTimer; 	var finishTimer:FlxTimer = null;  	// For being able to mess with the sprites on Lua 	public var countdownReady:FlxSprite; 	public var countdownSet:FlxSprite; 	public var countdownGo:FlxSprite;  	public function startCountdown():Void 	{ 		if(startedCountdown) { 			callOnLuas('onStartCountdown', []); 			return; 		}  		inCutscene = false; 		var ret:Dynamic = callOnLuas('onStartCountdown', []); 		if(ret != FunkinLua.Function_Stop) { 			generateStaticArrows(0); 			generateStaticArrows(1); 			for (i in 0...playerStrums.length) { 				setOnLuas('defaultPlayerStrumX' + i, playerStrums.members[i].x); 				setOnLuas('defaultPlayerStrumY' + i, playerStrums.members[i].y); 			} 			for (i in 0...opponentStrums.length) { 				setOnLuas('defaultOpponentStrumX' + i, opponentStrums.members[i].x); 				setOnLuas('defaultOpponentStrumY' + i, opponentStrums.members[i].y); 				//if(ClientPrefs.middleScroll) opponentStrums.members[i].visible = false; 			}  			startedCountdown = true; 			Conductor.songPosition = 0; 			Conductor.songPosition -= Conductor.crochet * 5; 			setOnLuas('startedCountdown', true); 			callOnLuas('onCountdownStarted', []);  			var swagCounter:Int = 0;  			if (skipCountdown){ 				Conductor.songPosition = 0; 				Conductor.songPosition -= Conductor.crochet ; 				swagCounter = 3; 			} 			startTimer = new FlxTimer().start(Conductor.crochet / 1000, function(tmr:FlxTimer) 			{ 				if (tmr.loopsLeft % gfSpeed == 0 && !gf.stunned && gf.animation.curAnim.name != null && !gf.animation.curAnim.name.startsWith("sing")) 				{ 					gf.dance(); 				} 				if(tmr.loopsLeft % 2 == 0) { 					if (boyfriend.animation.curAnim != null && !boyfriend.animation.curAnim.name.startsWith('sing')) 					{ 						boyfriend.dance(); 					} 					if (dad.animation.curAnim != null && !dad.animation.curAnim.name.startsWith('sing') && !dad.stunned) 					{ 						dad.dance(); 					} 				} 				else if(dad.danceIdle && dad.animation.curAnim != null && !dad.stunned && !dad.curCharacter.startsWith('gf') && !dad.animation.curAnim.name.startsWith("sing")) 				{ 					dad.dance(); 				}  				var introAssets:Map<String, Array<String>> = new Map<String, Array<String>>(); 				introAssets.set('default', ['ready', 'set', 'go']); 				introAssets.set('pixel', ['pixelUI/ready-pixel', 'pixelUI/set-pixel', 'pixelUI/date-pixel']);  				var introAlts:Array<String> = introAssets.get('default'); 				var antialias:Bool = ClientPrefs.globalAntialiasing; 				if(isPixelStage) { 					introAlts = introAssets.get('pixel'); 					antialias = false; 				}  				// head bopping for bg characters on Mall 				if(curStage == 'mall') { 					if(!ClientPrefs.lowQuality) 						upperBoppers.dance(true); 	 					bottomBoppers.dance(true); 					santa.dance(true); 				}  				switch (swagCounter) 				{ 					case 0: 						FlxG.sound.play(Paths.sound('intro3' + introSoundsSuffix), 0.6); 					case 1: 						countdownReady = new FlxSprite().loadGraphic(Paths.image(introAlts[0])); 						countdownReady.scrollFactor.set(); 						countdownReady.updateHitbox();  						if (PlayState.isPixelStage) 							countdownReady.setGraphicSize(Std.int(countdownReady.width * daPixelZoom));  						countdownReady.screenCenter(); 						countdownReady.antialiasing = antialias; 						add(countdownReady); 						FlxTween.tween(countdownReady, {/*y: countdownReady.y + 100,*/ alpha: 0}, Conductor.crochet / 1000, { 							ease: FlxEase.cubeInOut, 							onComplete: function(twn:FlxTween) 							{ 								remove(countdownReady); 								countdownReady.destroy(); 							} 						}); 						FlxG.sound.play(Paths.sound('intro2' + introSoundsSuffix), 0.6); 					case 2: 						countdownSet = new FlxSprite().loadGraphic(Paths.image(introAlts[1])); 						countdownSet.scrollFactor.set();  						if (PlayState.isPixelStage) 							countdownSet.setGraphicSize(Std.int(countdownSet.width * daPixelZoom));  						countdownSet.screenCenter(); 						countdownSet.antialiasing = antialias; 						add(countdownSet); 						FlxTween.tween(countdownSet, {/*y: countdownSet.y + 100,*/ alpha: 0}, Conductor.crochet / 1000, { 							ease: FlxEase.cubeInOut, 							onComplete: function(twn:FlxTween) 							{ 								remove(countdownSet); 								countdownSet.destroy(); 							} 						}); 						FlxG.sound.play(Paths.sound('intro1' + introSoundsSuffix), 0.6); 					case 3: 						if (!skipCountdown){ 						countdownGo = new FlxSprite().loadGraphic(Paths.image(introAlts[2])); 						countdownGo.scrollFactor.set();  						if (PlayState.isPixelStage) 							countdownGo.setGraphicSize(Std.int(countdownGo.width * daPixelZoom));  						countdownGo.updateHitbox();  						countdownGo.screenCenter(); 						countdownGo.antialiasing = antialias; 						add(countdownGo); 						FlxTween.tween(countdownGo, {/*y: countdownGo.y + 100,*/ alpha: 0}, Conductor.crochet / 1000, { 							ease: FlxEase.cubeInOut, 							onComplete: function(twn:FlxTween) 							{ 								remove(countdownGo); 								countdownGo.destroy(); 							} 						}); 						FlxG.sound.play(Paths.sound('introGo' + introSoundsSuffix), 0.6); 						} 					case 4: 				}  				notes.forEachAlive(function(note:Note) { 					note.copyAlpha = false; 					note.alpha = note.multAlpha; 					if(ClientPrefs.middleScroll && !note.mustPress) { 						note.alpha *= 0.5; 					} 				}); 				callOnLuas('onCountdownTick', [swagCounter]);  				swagCounter += 1; 				// generateSong('fresh'); 			}, 5); 		} 	}  	function startNextDialogue() { 		dialogueCount++; 		callOnLuas('onNextDialogue', [dialogueCount]); 	}  	function skipDialogue() { 		callOnLuas('onSkipDialogue', [dialogueCount]); 	}  	var previousFrameTime:Int = 0; 	var lastReportedPlayheadPosition:Int = 0; 	var songTime:Float = 0;  	function startSong():Void 	{ 		startingSong = false;  		previousFrameTime = FlxG.game.ticks; 		lastReportedPlayheadPosition = 0;  		FlxG.sound.playMusic(Paths.inst(PlayState.SONG.song), 1, false); 		FlxG.sound.music.onComplete = finishSong; 		vocals.play();  		if(paused) { 			//trace('Oopsie doopsie! Paused sound'); 			FlxG.sound.music.pause(); 			vocals.pause(); 		}  		// Song duration in a float, useful for the time left feature 		songLength = FlxG.sound.music.length; 		FlxTween.tween(timeBar, {alpha: 1}, 0.5, {ease: FlxEase.circOut}); 		FlxTween.tween(timeTxt, {alpha: 1}, 0.5, {ease: FlxEase.circOut}); 		 		#if desktop 		// Updating Discord Rich Presence (with Time Left) 		DiscordClient.changePresence(detailsText, SONG.song + " (" + storyDifficultyText + ")", iconP2.getCharacter(), true, songLength); 		#end 		setOnLuas('songLength', songLength); 		callOnLuas('onSongStart', []); 	}  	var debugNum:Int = 0; 	private var noteTypeMap:Map<String, Bool> = new Map<String, Bool>(); 	private var eventPushedMap:Map<String, Bool> = new Map<String, Bool>(); 	private function generateSong(dataPath:String):Void 	{ 		// FlxG.log.add(ChartParser.parse()); 		songSpeedType = ClientPrefs.getGameplaySetting('scrolltype','multiplicative');  		switch(songSpeedType) 		{ 			case "multiplicative": 				songSpeed = SONG.speed * ClientPrefs.getGameplaySetting('scrollspeed', 1); 			case "constant": 				songSpeed = ClientPrefs.getGameplaySetting('scrollspeed', 1); 		} 		 		var songData = SONG; 		Conductor.changeBPM(songData.bpm); 		 		curSong = songData.song;  		if (SONG.needsVoices) 			vocals = new FlxSound().loadEmbedded(Paths.voices(PlayState.SONG.song)); 		else 			vocals = new FlxSound();  		FlxG.sound.list.add(vocals); 		FlxG.sound.list.add(new FlxSound().loadEmbedded(Paths.inst(PlayState.SONG.song)));  		notes = new FlxTypedGroup<Note>(); 		add(notes);  		var noteData:Array<SwagSection>;  		// NEW SHIT 		noteData = songData.notes;  		var playerCounter:Int = 0;  		var daBeats:Int = 0; // Not exactly representative of 'daBeats' lol, just how much it has looped  		var songName:String = Paths.formatToSongPath(SONG.song); 		var file:String = Paths.json(songName + '/events'); 		#if sys 		if (FileSystem.exists(Paths.modsJson(songName + '/events')) || FileSystem.exists(file)) { 		#else 		if (OpenFlAssets.exists(file)) { 		#end 			var eventsData:Array<Dynamic> = Song.loadFromJson('events', songName).events; 			for (event in eventsData) //Event Notes 			{ 				for (i in 0...event[1].length) 				{ 					var newEventNote:Array<Dynamic> = [event[0], event[1][i][0], event[1][i][1], event[1][i][2]]; 					var subEvent:Array<Dynamic> = [newEventNote[0] + ClientPrefs.noteOffset - eventNoteEarlyTrigger(newEventNote), newEventNote[1], newEventNote[2], newEventNote[3]]; 					eventNotes.push(subEvent); 					eventPushed(subEvent); 				} 			} 		}  		for (section in noteData) 		{ 			for (songNotes in section.sectionNotes) 			{ 				var daStrumTime:Float = songNotes[0]; 				var daNoteData:Int = Std.int(songNotes[1] % 4);  				var gottaHitNote:Bool = section.mustHitSection;  				if (songNotes[1] > 3) 				{ 					gottaHitNote = !section.mustHitSection; 				}  				var oldNote:Note; 				if (unspawnNotes.length > 0) 					oldNote = unspawnNotes[Std.int(unspawnNotes.length - 1)]; 				else 					oldNote = null;  				var swagNote:Note = new Note(daStrumTime, daNoteData, oldNote); 				swagNote.mustPress = gottaHitNote; 				swagNote.sustainLength = songNotes[2]; 				swagNote.gfNote = (section.gfSection && (songNotes[1]<4)); 				swagNote.noteType = songNotes[3]; 				if(!Std.isOfType(songNotes[3], String)) swagNote.noteType = editors.ChartingState.noteTypeList[songNotes[3]]; //Backward compatibility + compatibility with Week 7 charts 				 				swagNote.scrollFactor.set();  				var susLength:Float = swagNote.sustainLength;  				susLength = susLength / Conductor.stepCrochet; 				unspawnNotes.push(swagNote);  				var floorSus:Int = Math.floor(susLength); 				if(floorSus > 0) { 					for (susNote in 0...floorSus+1) 					{ 						oldNote = unspawnNotes[Std.int(unspawnNotes.length - 1)];  						var sustainNote:Note = new Note(daStrumTime + (Conductor.stepCrochet * susNote) + (Conductor.stepCrochet / FlxMath.roundDecimal(songSpeed, 2)), daNoteData, oldNote, true); 						sustainNote.mustPress = gottaHitNote; 						sustainNote.gfNote = (section.gfSection && (songNotes[1]<4)); 						sustainNote.noteType = swagNote.noteType; 						sustainNote.scrollFactor.set(); 						unspawnNotes.push(sustainNote);  						if (sustainNote.mustPress) 						{ 							sustainNote.x += FlxG.width / 2; // general offset 						} 						else if(ClientPrefs.middleScroll) 						{ 							sustainNote.x += 310; 							if(daNoteData > 1) 							{ //Up and Right 								sustainNote.x += FlxG.width / 2 + 25; 							} 						} 					} 				}  				if (swagNote.mustPress) 				{ 					swagNote.x += FlxG.width / 2; // general offset 				} 				else if(ClientPrefs.middleScroll) 				{ 					swagNote.x += 310; 					if(daNoteData > 1) //Up and Right 					{ 						swagNote.x += FlxG.width / 2 + 25; 					} 				}  				if(!noteTypeMap.exists(swagNote.noteType)) { 					noteTypeMap.set(swagNote.noteType, true); 				} 			} 			daBeats += 1; 		} 		for (event in songData.events) //Event Notes 		{ 			for (i in 0...event[1].length) 			{ 				var newEventNote:Array<Dynamic> = [event[0], event[1][i][0], event[1][i][1], event[1][i][2]]; 				var subEvent:Array<Dynamic> = [newEventNote[0] + ClientPrefs.noteOffset - eventNoteEarlyTrigger(newEventNote), newEventNote[1], newEventNote[2], newEventNote[3]]; 				eventNotes.push(subEvent); 				eventPushed(subEvent); 			} 		}  		// trace(unspawnNotes.length); 		// playerCounter += 1;  		unspawnNotes.sort(sortByShit); 		if(eventNotes.length > 1) { //No need to sort if there's a single one or none at all 			eventNotes.sort(sortByTime); 		} 		checkEventNote(); 		generatedMusic = true; 	}  	function eventPushed(event:Array<Dynamic>) { 		switch(event[1]) { 			case 'Change Character': 				var charType:Int = 0; 				switch(event[2].toLowerCase()) { 					case 'gf' | 'girlfriend' | '1': 						charType = 2; 					case 'dad' | 'opponent' | '0': 						charType = 1; 					default: 						charType = Std.parseInt(event[2]); 						if(Math.isNaN(charType)) charType = 0; 				}  				var newCharacter:String = event[3]; 				addCharacterToList(newCharacter, charType); 		}  		if(!eventPushedMap.exists(event[1])) { 			eventPushedMap.set(event[1], true); 		} 	}  	function eventNoteEarlyTrigger(event:Array<Dynamic>):Float { 		var returnedValue:Float = callOnLuas('eventEarlyTrigger', [event[1]]); 		if(returnedValue != 0) { 			return returnedValue; 		}  		switch(event[1]) { 			case 'Kill Henchmen': //Better timing so that the kill sound matches the beat intended 				return 280; //Plays 280ms before the actual position 		} 		return 0; 	}  	function sortByShit(Obj1:Note, Obj2:Note):Int 	{ 		return FlxSort.byValues(FlxSort.ASCENDING, Obj1.strumTime, Obj2.strumTime); 	}  	function sortByTime(Obj1:Array<Dynamic>, Obj2:Array<Dynamic>):Int 	{ 		return FlxSort.byValues(FlxSort.ASCENDING, Obj1[0], Obj2[0]); 	}  	private function generateStaticArrows(player:Int):Void 	{ 		for (i in 0...4) 		{ 			// FlxG.log.add(i); 			var targetAlpha:Float = 1; 			if (player < 1 && ClientPrefs.middleScroll) targetAlpha = 0.35;  			var babyArrow:StrumNote = new StrumNote(ClientPrefs.middleScroll ? STRUM_X_MIDDLESCROLL : STRUM_X, strumLine.y, i, player); 			babyArrow.downScroll = ClientPrefs.downScroll; 			if (!isStoryMode) 			{ 				babyArrow.y -= 10; 				babyArrow.alpha = 0; 				FlxTween.tween(babyArrow, {y: babyArrow.y + 10, alpha: targetAlpha}, 1, {ease: FlxEase.circOut, startDelay: 0.5 + (0.2 * i)}); 			} 			else 			{ 				babyArrow.alpha = targetAlpha; 			}  			if (player == 1) 			{ 				playerStrums.add(babyArrow); 			} 			else 			{ 				if(ClientPrefs.middleScroll) 				{ 					babyArrow.x += 310; 					if(i > 1) { //Up and Right 						babyArrow.x += FlxG.width / 2 + 25; 					} 				} 				opponentStrums.add(babyArrow); 			}  			strumLineNotes.add(babyArrow); 			babyArrow.postAddedToGroup(); 		} 	}  	override function openSubState(SubState:FlxSubState) 	{ 		if (paused) 		{ 			if (FlxG.sound.music != null) 			{ 				FlxG.sound.music.pause(); 				vocals.pause(); 			}  			if (!startTimer.finished) 				startTimer.active = false; 			if (finishTimer != null && !finishTimer.finished) 				finishTimer.active = false; 			if (songSpeedTween != null) 				songSpeedTween.active = false;  			if(blammedLightsBlackTween != null) 				blammedLightsBlackTween.active = false; 			if(phillyCityLightsEventTween != null) 				phillyCityLightsEventTween.active = false;  			if(carTimer != null) carTimer.active = false;  			var chars:Array<Character> = [boyfriend, gf, dad]; 			for (i in 0...chars.length) { 				if(chars[i].colorTween != null) { 					chars[i].colorTween.active = false; 				} 			}  			for (tween in modchartTweens) { 				tween.active = false; 			} 			for (timer in modchartTimers) { 				timer.active = false; 			} 		}  		super.openSubState(SubState); 	}  	override function closeSubState() 	{ 		if (paused) 		{ 			if (FlxG.sound.music != null && !startingSong) 			{ 				resyncVocals(); 			}  			if (!startTimer.finished) 				startTimer.active = true; 			if (finishTimer != null && !finishTimer.finished) 				finishTimer.active = true; 			if (songSpeedTween != null) 				songSpeedTween.active = true;  			if(blammedLightsBlackTween != null) 				blammedLightsBlackTween.active = true; 			if(phillyCityLightsEventTween != null) 				phillyCityLightsEventTween.active = true; 			 			if(carTimer != null) carTimer.active = true;  			var chars:Array<Character> = [boyfriend, gf, dad]; 			for (i in 0...chars.length) { 				if(chars[i].colorTween != null) { 					chars[i].colorTween.active = true; 				} 			} 			 			for (tween in modchartTweens) { 				tween.active = true; 			} 			for (timer in modchartTimers) { 				timer.active = true; 			} 			paused = false; 			callOnLuas('onResume', []);  			#if desktop 			if (startTimer.finished) 			{ 				DiscordClient.changePresence(detailsText, SONG.song + " (" + storyDifficultyText + ")", iconP2.getCharacter(), true, songLength - Conductor.songPosition - ClientPrefs.noteOffset); 			} 			else 			{ 				DiscordClient.changePresence(detailsText, SONG.song + " (" + storyDifficultyText + ")", iconP2.getCharacter()); 			} 			#end 		}  		super.closeSubState(); 	}  	override public function onFocus():Void 	{ 		#if desktop 		if (health > 0 && !paused) 		{ 			if (Conductor.songPosition > 0.0) 			{ 				DiscordClient.changePresence(detailsText, SONG.song + " (" + storyDifficultyText + ")", iconP2.getCharacter(), true, songLength - Conductor.songPosition - ClientPrefs.noteOffset); 			} 			else 			{ 				DiscordClient.changePresence(detailsText, SONG.song + " (" + storyDifficultyText + ")", iconP2.getCharacter()); 			} 		} 		#end  		super.onFocus(); 	} 	 	override public function onFocusLost():Void 	{ 		#if desktop 		if (health > 0 && !paused) 		{ 			DiscordClient.changePresence(detailsPausedText, SONG.song + " (" + storyDifficultyText + ")", iconP2.getCharacter()); 		} 		#end  		super.onFocusLost(); 	}  	function resyncVocals():Void 	{ 		if(finishTimer != null) return;  		vocals.pause();  		FlxG.sound.music.play(); 		Conductor.songPosition = FlxG.sound.music.time; 		vocals.time = Conductor.songPosition; 		vocals.play(); 	}  	public var paused:Bool = false; 	var startedCountdown:Bool = false; 	var canPause:Bool = true; 	var limoSpeed:Float = 0;  	override public function update(elapsed:Float) 	{ 		/*if (FlxG.keys.justPressed.NINE) 		{ 			iconP1.swapOldIcon(); 		}*/  		callOnLuas('onUpdate', [elapsed]);  		switch (curStage) 		{ 			case 'schoolEvil': 				if(!ClientPrefs.lowQuality && bgGhouls.animation.curAnim.finished) { 					bgGhouls.visible = false; 				} 			case 'philly': 				if (trainMoving) 				{ 					trainFrameTiming += elapsed;  					if (trainFrameTiming >= 1 / 24) 					{ 						updateTrainPos(); 						trainFrameTiming = 0; 					} 				} 				phillyCityLights.members[curLight].alpha -= (Conductor.crochet / 1000) * FlxG.elapsed * 1.5; 			case 'limo': 				if(!ClientPrefs.lowQuality) { 					grpLimoParticles.forEach(function(spr:BGSprite) { 						if(spr.animation.curAnim.finished) { 							spr.kill(); 							grpLimoParticles.remove(spr, true); 							spr.destroy(); 						} 					});  					switch(limoKillingState) { 						case 1: 							limoMetalPole.x += 5000 * elapsed; 							limoLight.x = limoMetalPole.x - 180; 							limoCorpse.x = limoLight.x - 50; 							limoCorpseTwo.x = limoLight.x + 35;  							var dancers:Array<BackgroundDancer> = grpLimoDancers.members; 							for (i in 0...dancers.length) { 								if(dancers[i].x < FlxG.width * 1.5 && limoLight.x > (370 * i) + 130) { 									switch(i) { 										case 0 | 3: 											if(i == 0) FlxG.sound.play(Paths.sound('dancerdeath'), 0.5);  											var diffStr:String = i == 3 ? ' 2 ' : ' '; 											var particle:BGSprite = new BGSprite('gore/noooooo', dancers[i]…

---
## [fsociety-tribute/sunfish](https://github.com/fsociety-tribute/sunfish)@[3a4df37220...](https://github.com/fsociety-tribute/sunfish/commit/3a4df37220fbafff3b8666159a7d9299ef29bc47)
#### Monday 2022-03-07 02:02:48 by Peter Zijlstra

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
## [wastingmylife/kernel_xiaomi_vince](https://github.com/wastingmylife/kernel_xiaomi_vince)@[a418e810c6...](https://github.com/wastingmylife/kernel_xiaomi_vince/commit/a418e810c6d593ff651a09abf94b2ddd0de3893e)
#### Monday 2022-03-07 02:50:05 by Dave Chiluk

sched/fair: Fix low cpu usage with high throttling by removing expiration of cpu-local slices

It has been observed, that highly-threaded, non-cpu-bound applications
running under cpu.cfs_quota_us constraints can hit a high percentage of
periods throttled while simultaneously not consuming the allocated
amount of quota. This use case is typical of user-interactive non-cpu
bound applications, such as those running in kubernetes or mesos when
run on multiple cpu cores.

This has been root caused to cpu-local run queue being allocated per cpu
bandwidth slices, and then not fully using that slice within the period.
At which point the slice and quota expires. This expiration of unused
slice results in applications not being able to utilize the quota for
which they are allocated.

The non-expiration of per-cpu slices was recently fixed by
'commit 512ac999d275 ("sched/fair: Fix bandwidth timer clock drift
condition")'. Prior to that it appears that this had been broken since
at least 'commit 51f2176d74ac ("sched/fair: Fix unlocked reads of some
cfs_b->quota/period")' which was introduced in v3.16-rc1 in 2014. That
added the following conditional which resulted in slices never being
expired.

if (cfs_rq->runtime_expires != cfs_b->runtime_expires) {
	/* extend local deadline, drift is bounded above by 2 ticks */
	cfs_rq->runtime_expires += TICK_NSEC;

Because this was broken for nearly 5 years, and has recently been fixed
and is now being noticed by many users running kubernetes
(https://github.com/kubernetes/kubernetes/issues/67577) it is my opinion
that the mechanisms around expiring runtime should be removed
altogether.

This allows quota already allocated to per-cpu run-queues to live longer
than the period boundary. This allows threads on runqueues that do not
use much CPU to continue to use their remaining slice over a longer
period of time than cpu.cfs_period_us. However, this helps prevent the
above condition of hitting throttling while also not fully utilizing
your cpu quota.

This theoretically allows a machine to use slightly more than its
allotted quota in some periods. This overflow would be bounded by the
remaining quota left on each per-cpu runqueueu. This is typically no
more than min_cfs_rq_runtime=1ms per cpu. For CPU bound tasks this will
change nothing, as they should theoretically fully utilize all of their
quota in each period. For user-interactive tasks as described above this
provides a much better user/application experience as their cpu
utilization will more closely match the amount they requested when they
hit throttling. This means that cpu limits no longer strictly apply per
period for non-cpu bound applications, but that they are still accurate
over longer timeframes.

This greatly improves performance of high-thread-count, non-cpu bound
applications with low cfs_quota_us allocation on high-core-count
machines. In the case of an artificial testcase (10ms/100ms of quota on
80 CPU machine), this commit resulted in almost 30x performance
improvement, while still maintaining correct cpu quota restrictions.
That testcase is available at https://github.com/indeedeng/fibtest.

Fixes: 512ac999d275 ("sched/fair: Fix bandwidth timer clock drift condition")
Signed-off-by: Dave Chiluk <chiluk+linux@indeed.com>
Signed-off-by: Peter Zijlstra (Intel) <peterz@infradead.org>
Reviewed-by: Phil Auld <pauld@redhat.com>
Reviewed-by: Ben Segall <bsegall@google.com>
Cc: Ingo Molnar <mingo@redhat.com>
Cc: John Hammond <jhammond@indeed.com>
Cc: Jonathan Corbet <corbet@lwn.net>
Cc: Kyle Anderson <kwa@yelp.com>
Cc: Gabriel Munos <gmunoz@netflix.com>
Cc: Peter Oskolkov <posk@posk.io>
Cc: Cong Wang <xiyou.wangcong@gmail.com>
Cc: Brendan Gregg <bgregg@netflix.com>
Link: https://lkml.kernel.org/r/1563900266-19734-2-git-send-email-chiluk+linux@indeed.com
Signed-off-by: celtare21 <celtare21@gmail.com>
Signed-off-by: Poebe S.A <darkaccent69@gmail.com>

---
## [the-Awakening-of-god/sfx](https://github.com/the-Awakening-of-god/sfx)@[369cc91255...](https://github.com/the-Awakening-of-god/sfx/commit/369cc91255102efa027e2000d177c544bfb2df2d)
#### Monday 2022-03-07 03:12:51 by Garrett Seaba

the last mesage took forever to write and it didn't work so fuck you

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[f04b90b6e8...](https://github.com/odoo-dev/odoo/commit/f04b90b6e856bd8c1679cc728255f53fc788f8fd)
#### Monday 2022-03-07 04:29:37 by Julien Castiaux

[REF] core: HTTPocalypse (12) web ir.http & login

This commit is the 12th commit of a comprehensive refactor of our HTTP
framework. See odoo/odoo#78857 for complete historic, discussions and
rationnals.

The web module is twofold, on one side there are many controllers: /,
/web, /web/login, /web/database/selector, /web/dataset/call_kw, etc, on
the other side there is `session_info`: the method responsible to create
the web client's environ.

This module is kinda an exception as it is (with base) a server wide
module. In the case of the HTTP framework, it means that the controllers
of web are always accessible, i.e. going to / or /web/login will never
return a 404 Not Found even if the user is not connected to a database.

This is both a blessing and a curse. It is a blessing because the
controllers are always accessible it means that a new users can freely
access those routes. It is a curse because *any* user can access them,
even user who don't have a session yet thus who are not connected to a
database yet. From a developer standpoint, we have to put extra care to
correct serve users with and without a database. An example is the
/web/login route, the login/password pair is stored in a database,
without database it is impossible to validate a user login but users can
still access this route without db.

To solve this problem, there is the `ensure_db` function. This function
attempts to find a database using various sources (?db= query-string,
session db, mono db) and to save it on the user session. In case no db
is found, the user is redirected to the database selector. In a way,
this function grants a database to the user in a seamingly experience.
In a way, this function brings a welcome differentiation between
`auth='none'` with a database and `auth='none'` without a database. Such
differentiation only matters for the server wide modules as "regular"
module controllers are only accessible via the ir.http routing map, i.e.
it is not possible to declare a nodb controller outside of server wide
modules.

An important changement is the `session.authenticate` method, before it
was possible to call the method when the cursor was not yet initialized,
authenticate would open a cursor against the given database, setup a
registry and an environment and ultimately save everything on the
current request. Because the cursor is now greedily created, it is no
more possible to update the request environment when authenticating on
another database.

PR: odoo#78857
Task: 2571224

---
## [Balkoth-dev/WOTR_PATH_OF_RAGE](https://github.com/Balkoth-dev/WOTR_PATH_OF_RAGE)@[c3d1773505...](https://github.com/Balkoth-dev/WOTR_PATH_OF_RAGE/commit/c3d177350528b101735795a0d19899040e70ee3b)
#### Monday 2022-03-07 05:20:33 by Balkoth-dev

Demon Lord aspects fix removed as it was fixed in 1.2
Fixes autometamagic so that it will work on spells that are not originally part of a spellbook but added later. This is important for Arcane Bloodline for Bloodragers.
Adds a new mythic ability called Mighty Demonrage. This allows you to cast a demon spell of fourth level or lower as a swift action while Demon Raging.
Demon Rage changed to allow you to turn it off and on in the same turn, allowing you to rage-cycle using Demon Rage.

---
## [stickbear2015/sc-sounds](https://github.com/stickbear2015/sc-sounds)@[b40298b6c2...](https://github.com/stickbear2015/sc-sounds/commit/b40298b6c2bd2f798c64926b17fa87b91bcd2d76)
#### Monday 2022-03-07 05:54:25 by munchkinbear

fine vipmud, since you won't parce URL's in say strings properly, a big fuck you to you by the way, We'll just make users actually have to read readme.txt to get the URL!

---
## [xinyiZzz/incubator-doris](https://github.com/xinyiZzz/incubator-doris)@[ef2ea1806e...](https://github.com/xinyiZzz/incubator-doris/commit/ef2ea1806e4fb77369ab17a02d20fc8a286be43e)
#### Monday 2022-03-07 07:42:21 by HB

[docs] Improve the chapter on debugging FE in doc.  (#7309)

At present, there are defects in the chapter on debugging FE in doc. My colleagues and I stepped on the pit when 
building the debugging environment, so I want to improve this chapter in combination with my own stepping on the pit 
experience.

The following is my explanation of the changes: 

1. mkdir -p ./thirdparty/installed/bin
explain: When I downloaded versions 0.14 and 0.15, there were no files under thirdparty, so I didn't know whether to 
create it myself or what to do. Finally, I decided to create it myself. I think it's necessary to add instructions here.

2. Add installation thrift@0.13.0 Failed handling method. 
explain: My colleagues and I failed to find the installation package when executing the installation command, and finally 
found a solution on GitHub. Therefore, I added the handling method of the problem to avoid other Mac users from 
getting stuck in this place.

3. Fixed an error in the generated code description.
explain: Before I finished building the code, I debugged FE, and I failed all the time. Idea hints that no files can be found. 
Later, after consulting with morningman in wechat group, it was understood that `mvn install -DskipTests` does not 
need to execute `mvn generate-sources` after execution. This is inconsistent with the description in the document and 
needs to be corrected.

---
## [SpForks/free-programming-books](https://github.com/SpForks/free-programming-books)@[97016edd67...](https://github.com/SpForks/free-programming-books/commit/97016edd6791285128758dd91904b343d1f3b0fd)
#### Monday 2022-03-07 08:28:22 by David Ordás

Add CodingFantasy's CSS coding interactive games (#5490)

* Add "Knights of the Flexbox table" game

Welcome to the Knights of the Flexbox table. A game where you can help Sir Frederic Flexbox and his friends to uncover the treasures hidden in the Tailwind CSS dungeons.
You can navigate the knight through the dungeon by changing his position within the dungeon using Flexbox and Tailwind CSS.

* Add "Flex Box Adventure" game

Once upon a time, there was a King Arthur. He ruled his kingdom fair and square. But Arthur had one problem. He was a very naive person. So one sunny day, three alchemist brothers offered Arthur to exchange all his Gold Coins for coins made of a more valuable new metal that they had invented - Bit Coins.

Arthur believed them and gave them all his gold. The brothers took the gold and promised to give the bit coins back to Arthur in seven days.

Seven days passed. The brothers have not turned up. Arthur realized he had been scammed. He is angry and intends to take revenge on them. Let's help him do it with our weapon – CSS Flex Box!

We made this game for You
1. You often stumble and try to figure out which combination of Flex Box properties makes the browser do what you want it to do.

2. You want to create complex web layouts without constantly looking at the web page after every Cmd/Ctrl+S press in the code editor.

3. You have tried to learn Flex Box with video tutorials and articles but still don't fully understand how some parts of it work.

4*. Or, if you are a master of CSS Flex Box, we have something interesting and for you too (read further).

Have you found yourself there? Then you definitely want to learn or improve your Flex Box skills. So we have good news for you, really good news...

Learn Flex Box by Playing Game
No more boring videos, tutorials and courses. Learn Flex Box in a completely new, fun, effective and revolutionary way. By playing Flex Box coding game!

* Add "Grid Attack" coding game

In an ancient Elvish prophecy, it was said that one day a man would be born with an incredible power that predicts the future – "Marketi Predictori." And another will come to take this power. But the years went by and nothing happened. Until one day, a little elf was born. He was named Luke.

From an early age, he surprised his parents and his sister Rey by guessing the price of apples at the farmer's market before they even reached it. Every year his power rose and his predictions became more and more accurate. But there was one thing Luke could not predict. The coming of the demon Valcorian. It was the one from the prophecy that was to come and take Luke's power. One day Valcorian and his army attacked the town where Luke had lived and kidnapped him to make a ritual of stealing his power.

Go on a dangerous quest with Luke's sister Rey and find her brother. Defeat Valcorian and all his demons using a secret weapon – CSS Grid.

We made this game for You?
1. You often stumble and try to figure out which combination of Grid properties makes the browser do what you want it to do.

2. You are scared by the number of properties a CSS Grid has, and you feel uncomfortable when you need to create a grid layout.

3. You want to create complex web layouts using Grid, but without constantly looking at the web page after every "Cmd/Ctrl+S" press in the code editor.

4. You have tried to learn CSS Grid with video tutorials and articles but still don't fully understand how some parts of it work.

5. You use a Flex Box where Grid is required because you don't feel confident in using it.

Have you found yourself there? Then you definitely want to learn or improve your Grid skills. So we have good news for you, really good news...

Learn Grid by Playing CSS Game
No more boring videos, courses and articles. Learn Grid in a revolutionary new, fun, and effective way. By playing a Grid coding game!

---
## [sobotka/blender](https://github.com/sobotka/blender)@[2e146df515...](https://github.com/sobotka/blender/commit/2e146df51589281ac2cacef117f5f94fcbb4c7b7)
#### Monday 2022-03-07 08:50:25 by Joseph Eagar

temp-vertex-paint: Vertex paint branch

I have successully ported vertex paint's
draw brush to C++ thanks to the magic
of templates.  It's amazing how easy
this is.

---
## [Perkedel/Kaded-fnf-mods](https://github.com/Perkedel/Kaded-fnf-mods)@[7c36069eab...](https://github.com/Perkedel/Kaded-fnf-mods/commit/7c36069eabcc92ab7ec02a8339f53e84bd41461c)
#### Monday 2022-03-07 10:14:18 by Joel Robert Justiawan

[skip ci] The way I was treated, The negativity I reminds rather the most

NEW!!! SONG END function in this Modchart both Lua & haxe hscript yey! this executes when the song ends right before those script modchart goes unloaded whoahow!!!!! yo!!!

Message from Golik Derragan:
The way I  was treated, harsh. toxic, entitled convervative-ass.
Awaken my days back when in my young days in school, streets, and houses around me.
I was taught to think negative by the world. Forget positive, coz eventually they'll betray or at least forget you.
Quitting is no longer impactful as many of them had done so. I need damage. unique. big. devastating, all to sooididal level.
Do it for me, and I will admire your spectacularity. signed, Golik. MWUAHAHAHAHAHAHAHAHAHAAAA!!!!

Oh My God, that's screwed up bro, I'm really so sorry about that life. I am too, but can we have a better way than just to terroristically destroy those stuff to death?? No? I understand. but please don't do that. Let's not have revenge and admire somebody that did revenge for us okay? Not funny to see somebody once that blocked me on Twitter found flat in their own house somewhere no matter what history did they do, or uh somebody once that blammed my question for that thingy for seriously nonsense reason, or wha wha, those people who involved in this quite harrasment projects that causes it this gone, yea you know basically it.

kurirkrkrkrkrkarirkairakrairakrairkariarkairakrkirikr

---
## [Perkedel/Kaded-fnf-mods](https://github.com/Perkedel/Kaded-fnf-mods)@[bc15eb0659...](https://github.com/Perkedel/Kaded-fnf-mods/commit/bc15eb06591085c21df2c7dc452e59bc80e495e2)
#### Monday 2022-03-07 10:14:18 by Joel Robert Justiawan

[skip ci] NOBUBAB

what if this. one guy got rid of you. God angery, curse that guy. guy's friend eventually got all went wrong, one by one. eventually no connection. THEORY. let's forget about this.

https://github.com/Perkedel/Kaded-fnf-mods/issues/32 hbd text! here. put names, month, and day. if you got more than 1 person the same hbd date, put comma on it! say
you got
```
JOELwindows7:2:7
```
and you had another friend in the same birthdate! do like this!
```
JOELwindows7,arfaleg:2:7
```
like that.
and when the date match the time for, it pops out hbd in toast yay!

moar preps! https://github.com/Perkedel/Kaded-fnf-mods/issues/30#issuecomment-994760516

ohups! saubo note mine wrong! here I rerendered correct which layer.
also refactor note. Yep, we got to get all of those out from folder. Copy them just to be safe.

new! CarryAround class. you can carry this arround! just pick one variable you need to be refered or edited. they all are static yeah!!!

okay here we goh

---
## [Perkedel/Kaded-fnf-mods](https://github.com/Perkedel/Kaded-fnf-mods)@[cf529de9f3...](https://github.com/Perkedel/Kaded-fnf-mods/commit/cf529de9f333d9c9d1e2e340c828ebbbb9b58e4c)
#### Monday 2022-03-07 10:14:18 by Joel Robert Justiawan

[skip ci] omeren

newested library

Yoinkered https://github.com/EnigmaEngine/EnigmaEngine & https://github.com/ShadowMario/FNF-PsychEngine/ . WHOAHOW!!! there's alot!!! Most importantly to begin Enigma kinda of compatibility of something, including Hscript hookx to system functionality beyond gamplay modchart yess. not yet there, but we've started yoinkered them.

change font for song title progress meter bar into Ubuntu Mono due to that vcr font we have here in FNF doesn not have international support. Yep, that Simple Dimple song title in Russian Cyrilic.

Gave up! modCore still not realize the lua script over there. WOrkaround, just put only the modchart.lua directly into the main data/song/yoursongID there. Yeah this is bad, but at least FileDaddy can still have mods & manual direct to main injection. Hybrid mod!

 Loading bar trouble!!! I need help! I cannot make the Textfield in the LoadingBar sprite to show!!! https://github.com/Perkedel/Kaded-fnf-mods/issues/29 for now, we're just gonna mirror the text into the KadeEngineFPS text data too aswell. ah it works. Yeah just this OpenFl sprite doesn't want to show up at all 😡😡😡😡😡😡😡 PLS HELP HOW DO I OPEN FL DO THIS?!??!?!?!

https://github.com/Perkedel/Kaded-fnf-mods/issues/28 Okay here it is, the legacy Kade Lua modchart yey. You can enable this in Option menu, category Gameplay wow!!! maybe move to another category?? idk.. it's related to Gameplay, and it's that Lua gameplay modchart.

OKAY!!! NOW don't forget since you've made the compatible platform to have VLC as background video, the Modchart both Lua & Haxe script also has to know which Video handler did it used.

---
## [oleksandr-kuzmenko/MHDDoS](https://github.com/oleksandr-kuzmenko/MHDDoS)@[9b4b9d5719...](https://github.com/oleksandr-kuzmenko/MHDDoS/commit/9b4b9d57199fe5d84eec16b0bcce9a72e4f36726)
#### Monday 2022-03-07 11:37:00 by Oleksandr

[Russian warship, go fuck yourself] Add urls randomization

---
## [domob1812/namecoin-core](https://github.com/domob1812/namecoin-core)@[619f8a27ad...](https://github.com/domob1812/namecoin-core/commit/619f8a27ad0f6a44f0ad1a1e55a0aaaef7a91312)
#### Monday 2022-03-07 12:23:29 by MarcoFalke

Merge bitcoin/bitcoin#24304: [kernel 0/n] Introduce `bitcoin-chainstate`

2c03cec2ff8cdbfd5da92bfb507d218e5c6435b0 ci: Build bitcoin-chainstate (Carl Dong)
095aa6ca37bf0bd5c5e221bab779978a99b2a34c build: Add example bitcoin-chainstate executable (Carl Dong)

Pull request description:

  Part of: #24303

  This PR introduces an example/demo `bitcoin-chainstate` executable using said library which can print out information about a datadir and take in new blocks on stdin.

  Please read the commit messages for more details.

  -----

  #### You may ask: WTF?! Why is `index/*.cpp`, etc. being linked in?

  This PR is meant only to capture the state of dependencies in our consensus engine as of right now. There are many things to decouple from consensus, which will be done in subsequent PRs. Listing the files out right now in `bitcoin_chainstate_SOURCES` is purely to give us a clear picture of the task at hand, it is **not** to say that these dependencies _belongs_ there in any way.

  ### TODO

  1. Clean up `bitcoin-chainstate.cpp`
     It is quite ugly, with a lot of comments I've left for myself, I should clean it up to the best of my abilities (the ugliness of our init/shutdown might be the upper bound on cleanliness here...)

ACKs for top commit:
  ajtowns:
    ACK 2c03cec2ff8cdbfd5da92bfb507d218e5c6435b0
  ryanofsky:
    Code review ACK 2c03cec2ff8cdbfd5da92bfb507d218e5c6435b0. Just rebase, comments, formatting change since last review
  MarcoFalke:
    re-ACK 2c03cec2ff8cdbfd5da92bfb507d218e5c6435b0 🏔

Tree-SHA512: 86e7fb5718caa577df8abc8288c754f4a590650d974df9d2f6476c87ed25c70f923c4db651c6963f33498fc7a3a31f6692b9a75cbc996bf4888c5dac2f34a13b

---
## [oleksandr-kuzmenko/MHDDoS](https://github.com/oleksandr-kuzmenko/MHDDoS)@[0ad595ea98...](https://github.com/oleksandr-kuzmenko/MHDDoS/commit/0ad595ea9830c2ed56ac3e7cfb362a56a902a46d)
#### Monday 2022-03-07 12:28:07 by Oleksandr

[Russian warship, go fuck yourself] Fix urls randomization

---
## [icanalesm/dwm](https://github.com/icanalesm/dwm)@[67d76bdc68...](https://github.com/icanalesm/dwm/commit/67d76bdc68102df976177de351f65329d8683064)
#### Monday 2022-03-07 13:48:50 by Chris Down

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
## [k1sul1/k1kit](https://github.com/k1sul1/k1kit)@[0673624998...](https://github.com/k1sul1/k1kit/commit/06736249987f0653ad28a39c9a546144e8b4dd2c)
#### Monday 2022-03-07 15:22:43 by Christian Nikkanen

FUCK YOU SEO FRAMEWORK

For a long fucking time I've locked myself to a 2.x version of the seo framework because it took a turn in a shit direction in3, broke a lot of stuff and had HORRIBLE changelogs and NO MIGRATION GUIDE. 4.x has been out for some time and 2.x has started erroring in newer WP, so decied to give a shot at migrating...

Literal quote from changelog: Deprecated: with alternatives, refer to the source (search for your old method)

AND THEN YOU HAVE TO LOOK FOR THE SOURCE, USE THE SHITTY GITHUB SEARCH, GIVE UP AND DO THIS INSTEAD.

I'D MAKE A BETTER SEO PLUGIN IN A DAY BUT I DO NOT GIVE A SHIT ANYMORE

---
## [MinArchie/Shithole](https://github.com/MinArchie/Shithole)@[a44e1621a2...](https://github.com/MinArchie/Shithole/commit/a44e1621a23fedbdac7099088572202c77661d0b)
#### Monday 2022-03-07 15:44:16 by MinArchie

IGNORE PREVIOUS!! "finished ver"

THIS ONE is the finished ver. the other one had a mistake lol. anyway if you get time pleaseee look through it to find any bugs. and I did a horrible job of centering and placing the text and buttons so forgive me

---
## [ruchirK/materialize](https://github.com/ruchirK/materialize)@[3af43e2538...](https://github.com/ruchirK/materialize/commit/3af43e25388609cb43b7ab352ffe03d34f89d552)
#### Monday 2022-03-07 15:49:54 by Nikhil Benesch

coord: allow SELECTing from unmaterialized sources

This commit allows `SELECT` queries to depend, directly or indirectly,
on unmaterialized sources. This was previously disallowed because we
didn't track the `since` frontier of unmaterialized sources; now we do.

Users will no longer see errors like

    unable to automatically determine a query timestamp

which is a huge upgrade in the user experience, in my opinion. The
downside is that users are not careful, a one-off query may result in
e.g. re-reading an entire Kafka source from the upstream broker. If it
becomes a problem, we can consider introducing a "safe mode" (maybe via
a session variable) that disallows queries that would re-instantiate a
source.

This new behavior facilitates making tables unmaterialized by default
(#10883). That change goes down more easily if you can `SELECT` from an
unmaterialized table.

---
## [huggingface/datasets](https://github.com/huggingface/datasets)@[a8fa7cfe95...](https://github.com/huggingface/datasets/commit/a8fa7cfe95e06c8a667c4d7c5b7c7287b7e9ac4f)
#### Monday 2022-03-07 16:29:01 by RenChu Wang

Multi-GPU support for `FaissIndex` (#3721)

* 🎉 This commit fixes huggingface/datasets#3716

This commit adds handling for faiss indices that run on multiple GPUs.

* 🤕 Stupid mistake in that index isn't returned in the function handling device.

Now it's fixed. Hopefully the PR isn't merged yet!

* 🗎 Updated documents to reflect changes I made in the code.

Update `device`'s document to include negative numbers and lists.

* 1️⃣ The line should not exceed length: 119

It seems that this is what circle CI checked anyways.

* 🥴 Apply suggestions from code review

Missed it the first time :)

Co-authored-by: Albert Villanova del Moral <8515462+albertvillanova@users.noreply.github.com>

* 🛠️ Fixed my fixes.

Updated code to address concerns.

* 🇫 Update src/datasets/search.py

Using f-strings in docs.

Co-authored-by: Quentin Lhoest <42851186+lhoestq@users.noreply.github.com>

Co-authored-by: Albert Villanova del Moral <8515462+albertvillanova@users.noreply.github.com>
Co-authored-by: Quentin Lhoest <42851186+lhoestq@users.noreply.github.com>

---
## [adeGambit/adeGambit.github.io](https://github.com/adeGambit/adeGambit.github.io)@[ee25cdacfe...](https://github.com/adeGambit/adeGambit.github.io/commit/ee25cdacfef58a1c11e4abc7076954b6da01e124)
#### Monday 2022-03-07 17:51:18 by ADE

Update TextTemplate.txt

attempt 17(ish), I still require more tinkering and syncing with VS, Git, CMD and much, much, more. HOWEVER: we're making progress and hopefully this will stay saved on branch3 unlike my work from last night that disappeared this morning ( i saved improperly this morning or something of that nature, surely)

---
## [bgcngm/android_kernel_fxtec_msm8998](https://github.com/bgcngm/android_kernel_fxtec_msm8998)@[d886690515...](https://github.com/bgcngm/android_kernel_fxtec_msm8998/commit/d886690515730420861c6d4750e325de4bb07a6a)
#### Monday 2022-03-07 17:54:18 by Maciej Żenczykowski

FROMGIT: bpf: Do not change gso_size during bpf_skb_change_proto()

This is technically a backwards incompatible change in behaviour, but I'm
going to argue that it is very unlikely to break things, and likely to fix
*far* more then it breaks.

In no particular order, various reasons follow:

(a) I've long had a bug assigned to myself to debug a super rare kernel crash
on Android Pixel phones which can (per stacktrace) be traced back to BPF clat
IPv6 to IPv4 protocol conversion causing some sort of ugly failure much later
on during transmit deep in the GSO engine, AFAICT precisely because of this
change to gso_size, though I've never been able to manually reproduce it. I
believe it may be related to the particular network offload support of attached
USB ethernet dongle being used for tethering off of an IPv6-only cellular
connection. The reason might be we end up with more segments than max permitted,
or with a GSO packet with only one segment... (either way we break some
assumption and hit a BUG_ON)

(b) There is no check that the gso_size is > 20 when reducing it by 20, so we
might end up with a negative (or underflowing) gso_size or a gso_size of 0.
This can't possibly be good. Indeed this is probably somehow exploitable (or
at least can result in a kernel crash) by delivering crafted packets and perhaps
triggering an infinite loop or a divide by zero... As a reminder: gso_size (MSS)
is related to MTU, but not directly derived from it: gso_size/MSS may be
significantly smaller then one would get by deriving from local MTU. And on
some NICs (which do loose MTU checking on receive, it may even potentially be
larger, for example my work pc with 1500 MTU can receive 1520 byte frames [and
sometimes does due to bugs in a vendor plat46 implementation]). Indeed even just
going from 21 to 1 is potentially problematic because it increases the number
of segments by a factor of 21 (think DoS, or some other crash due to too many
segments).

(c) It's always safe to not increase the gso_size, because it doesn't result in
the max packet size increasing.  So the skb_increase_gso_size() call was always
unnecessary for correctness (and outright undesirable, see later). As such the
only part which is potentially dangerous (ie. could cause backwards compatibility
issues) is the removal of the skb_decrease_gso_size() call.

(d) If the packets are ultimately destined to the local device, then there is
absolutely no benefit to playing around with gso_size. It only matters if the
packets will egress the device. ie. we're either forwarding, or transmitting
from the device.

(e) This logic only triggers for packets which are GSO. It does not trigger for
skbs which are not GSO. It will not convert a non-GSO MTU sized packet into a
GSO packet (and you don't even know what the MTU is, so you can't even fix it).
As such your transmit path must *already* be able to handle an MTU 20 bytes
larger then your receive path (for IPv4 to IPv6 translation) - and indeed 28
bytes larger due to IPv4 fragments. Thus removing the skb_decrease_gso_size()
call doesn't actually increase the size of the packets your transmit side must
be able to handle. ie. to handle non-GSO max-MTU packets, the IPv4/IPv6 device/
route MTUs must already be set correctly. Since for example with an IPv4 egress
MTU of 1500, IPv4 to IPv6 translation will already build 1520 byte IPv6 frames,
so you need a 1520 byte device MTU. This means if your IPv6 device's egress
MTU is 1280, your IPv4 route must be 1260 (and actually 1252, because of the
need to handle fragments). This is to handle normal non-GSO packets. Thus the
reduction is simply not needed for GSO packets, because when they're correctly
built, they will already be the right size.

(f) TSO/GSO should be able to exactly undo GRO: the number of packets (TCP
segments) should not be modified, so that TCP's MSS counting works correctly
(this matters for congestion control). If protocol conversion changes the
gso_size, then the number of TCP segments may increase or decrease. Packet loss
after protocol conversion can result in partial loss of MSS segments that the
sender sent. How's the sending TCP stack going to react to receiving ACKs/SACKs
in the middle of the segments it sent?

(g) skb_{decrease,increase}_gso_size() are already no-ops for GSO_BY_FRAGS
case (besides triggering WARN_ON_ONCE). This means you already cannot guarantee
that gso_size (and thus resulting packet MTU) is changed. ie. you must assume
it won't be changed.

(h) changing gso_size is outright buggy for UDP GSO packets, where framing
matters (I believe that's also the case for SCTP, but it's already excluded
by [g]).  So the only remaining case is TCP, which also doesn't want it
(see [f]).

(i) see also the reasoning on the previous attempt at fixing this
(commit fa7b83bf3b156c767f3e4a25bbf3817b08f3ff8e) which shows that the current
behaviour causes TCP packet loss:

  In the forwarding path GRO -> BPF 6 to 4 -> GSO for TCP traffic, the
  coalesced packet payload can be > MSS, but < MSS + 20.

  bpf_skb_proto_6_to_4() will upgrade the MSS and it can be > the payload
  length. After then tcp_gso_segment checks for the payload length if it
  is <= MSS. The condition is causing the packet to be dropped.

  tcp_gso_segment():
    [...]
    mss = skb_shinfo(skb)->gso_size;
    if (unlikely(skb->len <= mss)) goto out;
    [...]

Thus changing the gso_size is simply a very bad idea. Increasing is unnecessary
and buggy, and decreasing can go negative.

Fixes: 6578171a7ff0 ("bpf: add bpf_skb_change_proto helper")
Signed-off-by: Daniel Borkmann <daniel@iogearbox.net>
Cc: Dongseok Yi <dseok.yi@samsung.com>
Cc: Willem de Bruijn <willemb@google.com>
Link: https://lore.kernel.org/bpf/CANP3RGfjLikQ6dg=YpBU0OeHvyv7JOki7CyOUS9modaXAi-9vQ@mail.gmail.com
Link: https://lore.kernel.org/bpf/20210617000953.2787453-2-zenczykowski@gmail.com

(cherry picked from commit 364745fbe981a4370f50274475da4675661104df https://git.kernel.org/pub/scm/linux/kernel/git/bpf/bpf-next.git/commit/?id=364745fbe981a4370f50274475da4675661104df )
Test: builds, TreeHugger
Bug: 158835517
Bug: 188690383
Signed-off-by: Maciej Żenczykowski <maze@google.com>
Change-Id: I0ef3174cbd3caaa42d5779334a9c0bfdc9ab81f5

---
## [san7890/bruhstation](https://github.com/san7890/bruhstation)@[de8411d838...](https://github.com/san7890/bruhstation/commit/de8411d838f9193f9f442c61a75d4fabe3138a23)
#### Monday 2022-03-07 18:18:05 by san7890

Mapper's Delight: Directional Poster Spawners [MDB IGNORE]

A lot of my PRs have been focused on having a fire lit under the seat of my pants. However, this PR is based off one conversation I had with someone.

"Haha, mapper. All you do is var_edits."

It was a bit more verbose than that, but it really did get me thinking about how fucking massive our files our thanks to these var_edits. This PR adds directional helpers to both A) Help mappers map the correct things with as little var edits as possible and B) Lessen the amount of space each fucking map file is thanks to however many extra bytes are taken up with pixel_x = 32. we have a lot of posters.

Bluntly put, this PR adds directional helpers to all generic /random poster spawners. i would add them to every single poster in the game, but that's a lot of work for unique posters, and someone can probably come up with a better idea. Good luck with that, this is just a good first step.

---
## [neighbourhoodie/couchdb](https://github.com/neighbourhoodie/couchdb)@[77f34a1bbc...](https://github.com/neighbourhoodie/couchdb/commit/77f34a1bbc7c76aefa59777da21e2e76e79f7ec8)
#### Monday 2022-03-07 19:10:41 by Adam Kocoloski

Refactor Jenkins to dynamically generate stages

This is one of those situations where you go in to make a small change,
see an opportunity for some refactoring, and get sucked into a rabbit
hole that leaves you wondering if you have any idea how computers
actually work. My initial goal was simply to update the Erlang version
used in our binary packages to a modern supported release. Along the
way I decided I wanted to figure out how to eliminate all the copypasta
we generate for making any change to this file, and after a few days of
hacking here we are. This rewrite has the following features:

* Updates to use Debian 11 (current stable) as the base image for
  building releases and packaging repos.

* Defaults to Erlang 23 as the embedded Erlang version in packages. We
  avoid Erlang 24 for now because Clouseau is not currently compatible.

* Dynamically generates the parallel build stages used to test and
  package CouchDB on various OSes. This is accomplished through a bit
  of scripted pipeline code that relies on two new methods defined at
  the beginning of the Jenkinsfile, one for "native" builds on macOS
  and FreeBSD and one for container-based builds. See comments in the
  Jenkinsfile for additional details.

* Expands commands like `make check` into a series of steps to improve
  visibility. The Jenkins UI will now show the time spent in each step
  of the build process, and if a step (e.g. `make eunit`) fails it will
  only expand the logs for that step by default instead of showing the
  logs for the entire build stage. The downside is that if we do make
  changes to the series of targets underneath `check` we need to
  remember to update the Jenkinsfile as well.

* Starts per-stage timer _after_ agent is acquired. Previously builds could
  fail with a 15m timeout when all they did was sit in the build queue.

This is a cherry-pick of 9b6454b with the following modifications:

- Drop the MINIMUM_ERLANG_VERSION to 20
- Drop the packaging ERLANG_VERSION to 23
- Add the weatherreport-test as a build step
- Add ARM and POWER back into the matrix using a new buildx-based
  multi-architecture container image.

---
## [SPLURT-Station/S.P.L.U.R.T-Station-13](https://github.com/SPLURT-Station/S.P.L.U.R.T-Station-13)@[2f9272dc4b...](https://github.com/SPLURT-Station/S.P.L.U.R.T-Station-13/commit/2f9272dc4b26209129e47a226276deb360818203)
#### Monday 2022-03-07 19:57:28 by Ludox

FUCK YOU

AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

---
## [SPLURT-Station/S.P.L.U.R.T-Station-13](https://github.com/SPLURT-Station/S.P.L.U.R.T-Station-13)@[0f50447ce2...](https://github.com/SPLURT-Station/S.P.L.U.R.T-Station-13/commit/0f50447ce293ce87b087bb0e043515be9c3066e2)
#### Monday 2022-03-07 19:57:28 by BongaTheProto

Merge pull request #237 from The-Sun-In-Splendour/cowkini

FUCK YOU

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[3040a05183...](https://github.com/mrakgr/The-Spiral-Language/commit/3040a05183195ed2d920bb38ac988e06027a4533)
#### Monday 2022-03-07 20:01:49 by Marko Grdinić

"9:45am. Went to bed quite late and got up early. Let me try some things yesterday night instead of watching anime I was reading the Houdini docs.

9:50am. https://www.sidefx.com/tutorials/game-tools-mesh-tiler/

Let me watch this as an appetizer.

10:10am. This could be quite useful if I was doing a game. But I have no interest in it right now. I'll keep it in mind though.

Now let me chill just for a bit.

10:15am. When it is time to start, what I will do is.

https://youtu.be/zsxg3eWkNYM
Introduction to Vray for Houdini Tutorial

I'll go with this instead of the Mantra tutorial. Since it is 40m while the Mantra one will take a while, I want to get it done first.

10:35am. Let me start. Let me watch that thing. Right now I am still bothered by not knowing where the light options are in V-Ray. Let me take care of my concerns.

https://www.youtube.com/results?search_query=v-ray+settings

Let me watch some of the things here first.

11am. https://youtu.be/-Uj_wg7MHq8
V-RAY Render Setup for TEST & FINAL Rendering

Let me watch this as well. There isn't much on this. I seriously cannot find the light bounce controls like in Blender's Cycles.

https://www.chaos.com/blog/v-ray-gpu-adds-support-for-nvidia-rtx

So RTX speeds things up by 40% on average.

This is not too bad.

11:10am. https://youtu.be/375X0m-PllA
GTC 2021: From Production Rendering with V-Ray GPU to Real-Time Ray Tracing with Chaos Vantage

I won't watch this.

https://youtu.be/-Uj_wg7MHq8?t=109

This is helpful. I did not realize that 50% option.

Nope, I do not actually have that option. I'd need to override the camera settings.

11:20am. Nevermind those settings, I can't seem to find the answer to the question I am interested in.

I suppose I do not need to care about it.

https://youtu.be/zsxg3eWkNYM?t=313

Let me resume this from yesterday.

https://youtu.be/zsxg3eWkNYM?t=746

I had no idea that there were so many presets.

11:55am. https://youtu.be/zsxg3eWkNYM?t=1040

Let me stop this here because I am not paying enough attention to it.

Today if I play my cards right I will be able to finish the Mantra tutorial. After that I should be able to start work on my own scene tomorrow.

So let me focus on going through the playlist. Focused tutorials is more up my alley right now.

https://youtu.be/uK4t414wwwc?list=PLFkMNnEYa3APIjPiwdEFL6BOJWLLqk7_S
Rounded Edge Shader: Fake Bevel + Basics of Procedural Tear and Wear — Mantra Getting Started ep. 08

12:45pm. https://www.sidefx.com/docs/houdini/nodes/sop/measure.html

Instead of watching the tutorial, I am trying to wrap my head around curvature. I think I have it, but I am not sure how to use this. I'll have to watch some math tutorials as well.

Nevermind this for now.

https://www.sidefx.com/docs/houdini/nodes/sop/groupfromattribboundary.html

I'll also leave studying this for later.

https://youtu.be/uK4t414wwwc?list=PLFkMNnEYa3APIjPiwdEFL6BOJWLLqk7_S&t=475

I admit, I haven't quite grasped that rounded edges should be there for the sake of highlighting small details. I thought they were bad at rounding corners yesterday and left it at that.

12:55pm. How did I get the round edge shader to work yesterday. Right now I am not sure where to plug it in.

...Right, it needs to come after the standard material.

https://youtu.be/uK4t414wwwc?list=PLFkMNnEYa3APIjPiwdEFL6BOJWLLqk7_S&t=612

Let me stop here, I've gotten sidetracked.

1:55pm. Done with chores. Time for food.

2:35pm. Let me read the chap of Scarlet and then I will resume.

2:45pm. Let me start. I'll leave those other chores for later.

Huh, I had to stop and focus on this. He actually intends to use the fake bevel to simulate wear and tear?

https://youtu.be/uK4t414wwwc?list=PLFkMNnEYa3APIjPiwdEFL6BOJWLLqk7_S&t=964

I hate these normal mapping tricks. The edges always give it way.

https://youtu.be/uK4t414wwwc?list=PLFkMNnEYa3APIjPiwdEFL6BOJWLLqk7_S&t=1258

Now this is nice. I am more fan of the effects that you can actually see that the almost imperceptible stuff.

https://youtu.be/JtDQaYWkSsk?list=PLFkMNnEYa3APIjPiwdEFL6BOJWLLqk7_S&t=2
Surface Imperfections: Dirt mask & Occlusion mask — Procedural Material Creation with Mantra ep. 09

Let me think about the round edge shader for a bit.

The one covered in Matra is pretty good, but what am I going to do with the V-Ray one? That one takes in a material and outputs a material. It migth have been better if it just output the intensity. Right now I can't really make use of it to make wear and tear.

3:10pm. One anon on /3/ asked about the measure SOP. How curvature relates to angle, what is its range and so on are good questions.

Let make it my study target. Forget the later vids for now. It is better to master one subject than peruse 10.

https://youtu.be/sf6vKicsgIc
Decimate Curve by Curvature

This is quite interesting. Remember how much trouble that hook gave me. If I could decimate by sharp angles that could resolve things...

While this did teach me something it is not quite what I had in mind.

https://www.youtube.com/results?search_query=houdini+curvature

https://www.youtube.com/watch?v=1aD6lFWIzJU
Size Matters: The New Measure SOP | Fianna Wong | GDC 2019

Let me watch this.

https://www.youtube.com/watch?v=6dXZ6lpjGuI
SideFX Houdini - worn edges via measure/curvature

Actually this is only 2m, so let me watch it first. No audio. Nwm.

https://youtu.be/pWewn4qGK-4
Houdini - Procedural Modeling Tips! - Finding Curvature

I'll leave this as the next vid.

https://youtu.be/1aD6lFWIzJU?t=257

I had no idea this was possible. You learn something new everyday.

https://youtu.be/1aD6lFWIzJU?t=493

Hmmm, what is this? Select by normals. Never saw that before.

3:55pm. Why does measure stop working when I bake it into output...

4pm. Why is this so unituitive? I have zero idea what those Measure options are supposed to be doing.

4:20pm. This node is buggy as fuck. I have no idea what is going on with it. The scale normalization does not work properly and blows past 1 frequently. I click the buttons and the visualization gets messed up.

4:40pm. I am getting a handle on it. It seems that clicking the bake visualize into the output makes the visualization work again. It crashed though when I was fiddling with scale independence.

5:25pm. I have a handle on it. I just realized that the viewport is pretty dark though. I think the scale normalization does not normalize it into the max norm, but by something like the variance. That would make sense. Let me finish the talk.

https://youtu.be/1aD6lFWIzJU?t=1509

Using the output of measure to control the activity of PolyReduce is an interesting idea.

6:25pm. https://youtu.be/pWewn4qGK-4
Houdini - Procedural Modeling Tips! - Finding Curvature

Let me watch this. I've been playing with the Measure SOP for hours now.

7:05pm. Done with lunch. Let me resume. I still haven't watched it.

https://youtu.be/pWewn4qGK-4?t=229

Oh, this makes the curvature really easy to understand.

7:15pm. https://youtu.be/pWewn4qGK-4?t=569

Ah, why did I not think of this way of putting in handrails?

https://youtu.be/pWewn4qGK-4?t=290

This technique is really good as well.

Though rather than using the measure SOP, maybe taking the dot product of the current and previous normal would have worked just as well.

7:30pm. That with that video. Let me keep going. Let me read the docs for the Measure SOP again. I just about figured out the curvature. What about volume and the rest?

https://www.sidefx.com/docs/houdini/nodes/sop/measure.html

Hmmm, I could use the Laplacian to smooth out the color. Let me give it a try...

Nope, I can't use that for more than a single attribute.

8:40pm. Let me close here. I've bene playing too much with the measure SOP today, but I think I have a handle on both it and the Labs Measure Curvature SOP. For this later one to get the `curvature` attribute, you just add them up. They are both positive and at most add up to 1.

The visualizers for both of them are buggy as hell, and the Measure SOP in particular is full of minefields when it comes to adjusting its parameters. But it works. That is certainly the case.

One thing that confuses me is how poor the Gaussian curvature is on a simple box. It only detects the corners for whatever reason and not the regular edge. The Curvedness is much better in that regard, but it does not matter what I end up using.

I am thinking that maybe the ideal measure would be to take the log of the Curvedness measure, center it, normalize it, and only then reproject it back.

...No, that would to instabilities when the measure is zero. Forget it.

9pm. I am really into it when I should not be. I could have finished the playlist today, but instead I spent the whole day fiddling with curvature SOPs. Tomorrow, I am going to get it done - I will finish the playlist. Right now let me finally put Win 10 on that old PC and I will clear up that assignment."

---
## [adeGambit/adeGambit.github.io](https://github.com/adeGambit/adeGambit.github.io)@[8a492263ea...](https://github.com/adeGambit/adeGambit.github.io/commit/8a492263eac2fe00c7b1a45f76313bfc6480ddf3)
#### Monday 2022-03-07 20:24:20 by adeGambit

<!DOCTYPE html> <html> <head> <meta charset ="utf-8" />     <!--(^this*) i honestly don't know what this(*) does but it's been so helpful since i LEFT it there.         i like to think of it as a good luck charm or a totem--> <title>The ADE Experience</title><!--the title took a little doing but eventually fell in line--> </head> <body>        <h1 style="color:White;">Welcome</h1><!--special thanks to Robin-->     <p>         Thank You! <hr>         Please feel free to reach out & don't forget to inquire about THE MERCH <hr />         Merch landing soon across several sites, social medium and on the streets!     </p>      <!IMG src=(https://user-images.githubusercontent.com/97244700/156807238-15e2c868-ec70-49a6-aa5f-621cb8ad286d.PNG) />     <IMG src="https://user-images.githubusercontent.com/97244700/156807238-15e2c868-ec70-49a6-aa5f-621cb8ad286d.PNG" alt="Suited" style="width:350px;height:777px;">          <a href="https://www.tiktok.com/@adegambit7/">FGotta TikTok? Check out some goofy short vids here!</a>         <a href="https://www.youtube.com/channel/UC534D0kLREw8mHMSF7eJYkQ/">Gotta YouTube? Check out some weird art and music here!</a>     <body style="background-color:LightGray;">    </body>      </html>

---
## [morgoth1145/advent-of-code](https://github.com/morgoth1145/advent-of-code)@[4f72ee088d...](https://github.com/morgoth1145/advent-of-code/commit/4f72ee088dec7662a6eed99fa399aa694d424ea4)
#### Monday 2022-03-07 20:48:27 by Patrick Hogg

2017 Day 18 Part 2

Holy crap everything fell apart here! I thought this would be a fun little coroutine problem, but nooooo.

I started out writing a simple Python coroutine that I'd instantiate twice and run, but it was running forever. Dismayed I then thought that maybe this was an icky reverse engineering problem. It isn't, but I still spent a ton of time reverse-engineering the code to find that it's a bubble sort of 127 values.

So I tried counting the steps for bubble sort for the generated sequence. It sort of worked, at least in confirming on the site that that was the right ballpark. However, the numbers I got were wrong. (Don't really know or care why.)

Then I reimplemented the *entire* thing with a class for easier debugging. Surprisingly the number of values passed between them did *not* stay at 127, so something was clearly going very wrong!

After *way* too long debugging I finally found two really, really stupid bugs:
1) When parsing the instructions I forgot to convert parameter 0 of jgz to int if it wasn't a letter, breaking the program.
2) I also implemented jgz with a simple equality check against zero, not checking for greater than zero!

Honestly, if I'd have done those right initially I'd have saved so much time. This was an absolute disaster.

An hour past the end of the part 2 leaderboard :(

Time: 1:40:10.073833

---
## [niftynei/lightning](https://github.com/niftynei/lightning)@[cb48532608...](https://github.com/niftynei/lightning/commit/cb48532608cec84216d6f0a7aef59185cf85fc23)
#### Monday 2022-03-07 20:57:45 by niftynei

bkpr: add journal entry for offset account balances; report listbalances

When the node starts up, it records missing/updated account balances
to the 'channel' events... which is kinda fucked for wallet + external
events now that i think about it but these are all treated the same
anyway so it's fine.

This is the magic piece that lets your bookkeeping data startup ok on an
already running/established node.

---
## [jhamil64/Walking-Challenge-RPG](https://github.com/jhamil64/Walking-Challenge-RPG)@[2513c1e95c...](https://github.com/jhamil64/Walking-Challenge-RPG/commit/2513c1e95cbd2eb99b851c5fb0ec4f8669d26006)
#### Monday 2022-03-07 21:28:35 by Jaymes Hamilton

Through lots of hard work (and sweat, and tears) I managed to implement a battle system that does not crash no matter what you do! Oh yeah! There is still a lot more I want to do but now that the framework is complete I can reuse the function for literally any kind of battle. Since tapping the enemy is required I could even implement multiple enemies at once if I can figure out the logic.

---
## [oranche-manufacturing/ArcCW-Everyman](https://github.com/oranche-manufacturing/ArcCW-Everyman)@[e294f606a8...](https://github.com/oranche-manufacturing/ArcCW-Everyman/commit/e294f606a8dda3d26d7e9e0f3361fb77b81a94b9)
#### Monday 2022-03-07 22:36:23 by oranchepopsicle

actual theming, resisting autism

god fuck fuck fucking fucking shit fuck fucking fuck

---
## [mozsearch/mozsearch](https://github.com/mozsearch/mozsearch)@[03535421c7...](https://github.com/mozsearch/mozsearch/commit/03535421c7169fc65d1d536040f94fe7d652595a)
#### Monday 2022-03-07 23:57:48 by Andrew Sutherland

Bug 1758394, Bug 1748959 - Go to definition for XPIDL should go to the IDL file.

- crossref.rs will now consider "IDL" kinds prior to "def" kinds when emitting
  jump records.
- output-file's HTML files will now also include a "path" that looks like
  `path/to/file#line-number` in the `ANALYSIS_DATA` at the bottom of the file.
` context-menu.js will now use the `path` data to build a direct link to the
  definition instead of going through the `define` CGI route/endpoint that
  `router.py` handles.
  - This fixes bug 1748959 and should massively improve the searchfox
    experience when moving around giant source files which would otherwise be
    reloaded every time "go to definition" is used.  This is particularly
    relevant for rlbox files.
  - See the bug for more discussion, but this does mean that the UX may be
    slightly worse when going to a definition for something and the current
    HTML file is not from the current searchfox run that will be served.  It
    does also mean that anyone who previously right-clicked on the `define`
    to get a persistent link they could paste for a symbol can no longer
    easily do that.  However, I think I may have been the only person who has
    done this in general, and I think we can otherwise improve the UX for
    acquiring / having stable links.

Test-wise:
- This adds a new `xpidl_cpp_consumer.cpp` file that generates a "use" for our
  canonical test method, `testOctet` so that we can see "go to definition"
  work for IDL purposes.
- Getting this to work required creating a bunch of very hacky stubs so that
  we could include the (imported from mozilla-central) XPIDL-generated header
  file.  Happily, our test files don't have to run, just sorta compile!

---

