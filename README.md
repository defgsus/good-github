## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-09-08](docs/good-messages/2022/2022-09-08.md)


2,035,093 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,035,093 were push events containing 3,074,115 commit messages that amount to 224,728,111 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 36 messages:


## [JoeBidenWhatAreYouHiding/kx](https://github.com/JoeBidenWhatAreYouHiding/kx)@[40edce3053...](https://github.com/JoeBidenWhatAreYouHiding/kx/commit/40edce3053b209fb34592f360c3a249080d5bf20)
#### Thursday 2022-09-08 00:20:32 by generalguneric

new provinces for Madagascar; properly aligned its provinces with rivers. fuck your save games!

---
## [hangrydave/InfraredBrickTower](https://github.com/hangrydave/InfraredBrickTower)@[02b9eb4f8c...](https://github.com/hangrydave/InfraredBrickTower/commit/02b9eb4f8c28d27bfaed294d593d659f9ad07e25)
#### Thursday 2022-09-08 00:54:17 by David Reidsma

Abstracted all the things (#1)

I yoinked the core logic for PBrick stuff and tower stuff out of the main project into separate ones. What a horrible experience this was, C++ development is fraught with unhelpful error messages.

* working on abstraction of logic

* pbricklogic is now it's own thing, stuffs abstracted

* it doesn't work and i hate it

* PROOF OF CONCEPT: BUILDS AND RUNS RUNNING CODE IN BUILT .lib

* it works now! life is sometimes ok, ya love to see it

* got rid of unnecessary file

---
## [ammarfaizi2/linux-fork](https://github.com/ammarfaizi2/linux-fork)@[e9e055ff24...](https://github.com/ammarfaizi2/linux-fork/commit/e9e055ff2471f8f61eb3ebc78e7f5726ed83659c)
#### Thursday 2022-09-08 01:01:04 by Johannes Weiner

mm: vmscan: fix extreme overreclaim and swap floods

During proactive reclaim, we sometimes observe severe overreclaim, with
several thousand times more pages reclaimed than requested.

This trace was obtained from shrink_lruvec() during such an instance:

    prio:0 anon_cost:1141521 file_cost:7767
    nr_reclaimed:4387406 nr_to_reclaim:1047 (or_factor:4190)
    nr=[7161123 345 578 1111]

While he reclaimer requested 4M, vmscan reclaimed close to 16G, most of it
by swapping.  These requests take over a minute, during which the write()
to memory.reclaim is unkillably stuck inside the kernel.

Digging into the source, this is caused by the proportional reclaim
bailout logic.  This code tries to resolve a fundamental conflict: to
reclaim roughly what was requested, while also aging all LRUs fairly and
in accordance to their size, swappiness, refault rates etc.  The way it
attempts fairness is that once the reclaim goal has been reached, it stops
scanning the LRUs with the smaller remaining scan targets, and adjusts the
remainder of the bigger LRUs according to how much of the smaller LRUs was
scanned.  It then finishes scanning that remainder regardless of the
reclaim goal.

This works fine if priority levels are low and the LRU lists are
comparable in size.  However, in this instance, the cgroup that is
targeted by proactive reclaim has almost no files left - they've already
been squeezed out by proactive reclaim earlier - and the remaining anon
pages are hot.  Anon rotations cause the priority level to drop to 0,
which results in reclaim targeting all of anon (a lot) and all of file
(almost nothing).  By the time reclaim decides to bail, it has scanned
most or all of the file target, and therefor must also scan most or all of
the enormous anon target.  This target is thousands of times larger than
the reclaim goal, thus causing the overreclaim.

The bailout code hasn't changed in years, why is this failing now?  The
most likely explanations are two other recent changes in anon reclaim:

1. Before the series starting with commit 5df741963d52 ("mm: fix LRU
   balancing effect of new transparent huge pages"), the VM was
   overall relatively reluctant to swap at all, even if swap was
   configured. This means the LRU balancing code didn't come into play
   as often as it does now, and mostly in high pressure situations
   where pronounced swap activity wouldn't be as surprising.

2. For historic reasons, shrink_lruvec() loops on the scan targets of
   all LRU lists except the active anon one, meaning it would bail if
   the only remaining pages to scan were active anon - even if there
   were a lot of them.

   Before the series starting with commit ccc5dc67340c ("mm/vmscan:
   make active/inactive ratio as 1:1 for anon lru"), most anon pages
   would live on the active LRU; the inactive one would contain only a
   handful of preselected reclaim candidates. After the series, anon
   gets aged similarly to file, and the inactive list is the default
   for new anon pages as well, making it often the much bigger list.

   As a result, the VM is now more likely to actually finish large
   anon targets than before.

Change the code such that only one SWAP_CLUSTER_MAX-sized nudge toward the
larger LRU lists is made before bailing out on a met reclaim goal.

This fixes the extreme overreclaim problem.

Fairness is more subtle and harder to evaluate.  No obvious misbehavior
was observed on the test workload, in any case.  Conceptually, fairness
should primarily be a cumulative effect from regular, lower priority
scans.  Once the VM is in trouble and needs to escalate scan targets to
make forward progress, fairness needs to take a backseat.  This is also
acknowledged by the myriad exceptions in get_scan_count().  This patch
makes fairness decrease gradually, as it keeps fairness work static over
increasing priority levels with growing scan targets.  This should make
more sense - although we may have to re-visit the exact values.

Link: https://lkml.kernel.org/r/20220802162811.39216-1-hannes@cmpxchg.org
Signed-off-by: Johannes Weiner <hannes@cmpxchg.org>
Reviewed-by: Rik van Riel <riel@surriel.com>
Acked-by: Mel Gorman <mgorman@techsingularity.net>
Cc: Hugh Dickins <hughd@google.com>
Cc: Joonsoo Kim <iamjoonsoo.kim@lge.com>
Cc: <stable@vger.kernel.org>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>

---
## [bellomia/matlab-multiple-dispatch](https://github.com/bellomia/matlab-multiple-dispatch)@[6c955dfa4a...](https://github.com/bellomia/matlab-multiple-dispatch/commit/6c955dfa4a134280c3a2b526775d13541b8fd2e6)
#### Thursday 2022-09-08 02:03:20 by Gabriele Bellomia

Add functional handle constructor: h = obj.activate; h(varargin)

> to allow calling the generic interface just as a function, instead of
  using the ugly obj.dispatch() syntax

⚠️ Note that if a method is added to the object, the handle would NOT
   access it unless the user "reloads" it by running again <activate>.

EXAMPLE
————————————————————————————————————————————————————————————————————————
>> % init the interface object,
>> % there are no methods at first
>> % (but there would be a one-shot constructor eventually)
>> f = interface

f =

  interface with properties:

    method_list: {}

>> % Add a specialized implementation,
>> % by providing a lambda function
>> % (or a handle of course) and the type signature...
>> f = f.add_method(@(x,y)(x+y),["numeric","numeric"])

f =

  interface with properties:

    method_list: {@(x,y)(x+y)  ["numeric"    "numeric"]}

>> h = f.activate % emit a function handle to allow nice calling

h =

  function_handle with value:

    @(varargin)dispatch(self,varargin{:})

>> h(3,3) % test... and works!

ans =

     6
>>
>> % NOW, imagine this is what the library exports
>> % to the user, not just h(), but also the object f
>> % what we want now is to allow extending f, and
>> % eventually h(), of course....
>>
>> % So let's add another method
>> f = f.add_method(@sin,"numeric")

f =

  interface with properties:

    method_list: {@(x,y)(x+y) ["numeric", "numeric"]  @sin  ["numeric"]}

>> h(pi/2) % If I don't "reload" it is not accessed by the handle
>> %         (but this could make sense I guess...)
Error using interface/dispatch (line 59)
no method found

Error in interface>@(varargin)dispatch(self,varargin{:}) (line 34)
        handle = @(varargin) dispatch(self,varargin{:});

>> h = f.activate % So let's activate again the interface

h =

  function_handle with value:

    @(varargin)dispatch(self,varargin{:})

>> h(pi/2)

ans =

     1

>> % hell yeah, successfully added another method,
>> % /dynamically/, which is the crucial requirement.
————————————————————————————————————————————————————————————————————————

---
## [010blckswan420/friendly-journey](https://github.com/010blckswan420/friendly-journey)@[7dcff7485f...](https://github.com/010blckswan420/friendly-journey/commit/7dcff7485f19e7a40ea6ad141140899e5c589b51)
#### Thursday 2022-09-08 02:19:11 by 010blckswan420

Merge pull request #1 from 010blckswan420/010blckswan420

sudo su && fuck you

---
## [Tastyfish/-tg-station](https://github.com/Tastyfish/-tg-station)@[3b2cf65d59...](https://github.com/Tastyfish/-tg-station/commit/3b2cf65d59aa5ae22876b0ebabecb564ccb912d0)
#### Thursday 2022-09-08 03:10:06 by san7890

Rocking The Boat, er, Map Vote (#69561)

* Rocking The Boat, er, Map Vote

Hey there,

A while ago, I spooke (typo intentional) to some other people. One frustration I heard was the fact that people would sometimes sneak through map votes during the very start of a shift, during a high-paced portion, or just as a meme. People in OOC would then flood the vote, putting in any given station. However, if a vote happens 10 minutes in- and the round goes for 70 minutes and not many of the original players are around, then it's not particularly fair to those who have to play next shift on a map they bemoan.

So, we can rock the vote! If a player isn't particularly chuffed with the hand they are given, they can poll the players to see if they want to change the map as well. If rocking the vote goes through, huzzah, you get the ability to vote for the map again. If it doesn't go through: tough luck. You can rock the vote one time per shift by default, and server operators can change the amount of times you can call to rock the map vote at their discretion. Calling to rock the vote either successfully or non-successfully counts as a "call", and when that limit is exceeded: no more calls.

Does this mean that we will only rotate between two maps because pissants will keep rocking the vote until they get what they like? Maybe? I still see people bemoan getting Tram or shit the bed over IceBox, but I think enough people get sick of bread-on-butter to take the server where it need to go. If operators don't really like seeing only two maps play, they can always adjust the config to ensure it doesn't happen.

* makes the grammar grammar

it would be "Rock the Vote vote" otherwise

---
## [newstools/2022-sowetan-live](https://github.com/newstools/2022-sowetan-live)@[8a73eec2df...](https://github.com/newstools/2022-sowetan-live/commit/8a73eec2df6001b975d6fe5d581decbda4af5889)
#### Thursday 2022-09-08 03:50:48 by Billy Einkamerer

Created Text For URL [www.sowetanlive.co.za/news/2022-09-07-man-who-killed-girlfriend-and-stabbed-her-suspected-lover-gets-life-sentence/]

---
## [newstools/2022-the-citizen](https://github.com/newstools/2022-the-citizen)@[f6420ac586...](https://github.com/newstools/2022-the-citizen/commit/f6420ac586eb6e439d583e95d7c6c065e1e09011)
#### Thursday 2022-09-08 04:20:32 by Billy Einkamerer

Created Text For URL [www.citizen.co.za/news/3192122/jealous-boyfriend-murders-girlfriend-and-brutally-attacks-her-alleged-lover-september-2022/]

---
## [matttheficus/Paradise](https://github.com/matttheficus/Paradise)@[6082c95eb3...](https://github.com/matttheficus/Paradise/commit/6082c95eb300a9f05b5422060db79f55fe91b9b3)
#### Thursday 2022-09-08 05:32:24 by LightFire53

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
## [Dylan-DPC/rust](https://github.com/Dylan-DPC/rust)@[1c35596762...](https://github.com/Dylan-DPC/rust/commit/1c3559676265f2c320f4e361fece080b0f464f97)
#### Thursday 2022-09-08 06:25:10 by Dylan DPC

Rollup merge of #101455 - thomcc:why-is-this-here, r=jyn514

Avoid UB in the Windows filesystem code in... bootstrap?

This basically a subset of the changes from https://github.com/rust-lang/rust/pull/101171. I didn't think to look in src/bootstrap for more windows filesystem API usage, which was apparently a mistake on my part. It's kinda goofy that stuff like this is in here, but what are you gonna do, computers are awful.

I also added `winbase` to the `winapi` dep -- I tested this in a tmp crate but needed to add this to your Cargo.toml -- you `use winapi::stuff::winbase` in this function, but are relying on something else turning on that feature.

---
## [BetterPixelmon/BetterPixelmonSpawner](https://github.com/BetterPixelmon/BetterPixelmonSpawner)@[9c97088cfb...](https://github.com/BetterPixelmon/BetterPixelmonSpawner/commit/9c97088cfbf14387c1cfcf4076f2859958974a33)
#### Thursday 2022-09-08 06:48:46 by Lypaka

Fucking Generations and their stupid ass methods for movement AI

---
## [NovaGitHubFNF/GFwN-Source-Code-but-this-shit-lua](https://github.com/NovaGitHubFNF/GFwN-Source-Code-but-this-shit-lua)@[29efa2ecbd...](https://github.com/NovaGitHubFNF/GFwN-Source-Code-but-this-shit-lua/commit/29efa2ecbd9aea328124dcf66a1e3c2ddf66002a)
#### Thursday 2022-09-08 07:05:36 by Nova

Add Lua Stage

Fuck you, I'm on a sleep call while writing this

---
## [dearmochi/Paradise](https://github.com/dearmochi/Paradise)@[ab7a358506...](https://github.com/dearmochi/Paradise/commit/ab7a35850672da159eea98085cf6fade7d595340)
#### Thursday 2022-09-08 07:44:58 by Farie82

Makes setting a machine GC properly if not unset properly (#17840)

* Makes setting a machine GC properly if not unset properly

* Forgot one. Fuck you borer code

---
## [OrionTheFox/Skyrat-tg](https://github.com/OrionTheFox/Skyrat-tg)@[e1839f0e37...](https://github.com/OrionTheFox/Skyrat-tg/commit/e1839f0e375a2169c8d80d942376dddb8be1958d)
#### Thursday 2022-09-08 08:23:48 by SkyratBot

[MIRROR] Spider Rebalance PR: Burn Baby Burn Edition [MDB IGNORE] (#15997)

* Spider Rebalance PR: Burn Baby Burn Edition (#68971)

This is a remake of #66106, with more thought put into the underlying balance. The main goal of this PR is to make fighting spiders more accessible and interesting for the majority of the crew while nerfing the extremely strong and boring option of simply using freezing temps to kill spiders. Also fixes #67765. The changes are as follows:

NEW SPIDER COUNTERS

    Fly swatters now deal 25 damage to spiders on hit, increased from 1
    Pesticide now deals massive stamina damage to spiders and a little bit of physical damage as well (the damage portion not added by this PR)
    Spiders can now be caught on fire through any traditional mean of catching something on fire. Spiders will automatically put themselves out after a time. This was done instead of an active action because AI spiders are also subject to this change as well, and I don't feel like bloating the simple mob AI with putting themselves out

SPIDER CHANGES

NERFS

    Toxin injection has been removed from all spiders except for the hunter, flesh spiders and the viper
    Hunter toxin (used by hunters and flesh spiders) now only brings the afflicted down to 40 health, and will stop taking effect once the afflicted reaches that threshold. Should the afflicted still have the toxin in their system and get healed, the toxin will begin dealing damage again until the afflicted is at 40 health or below again
    Viper toxin now only brings the afflicted down to 10 health, but also has the hallucination effects of Mindbreaker toxin. This hallucination effect is applied regardless of target health. It also no longer generates other harmful chemicals into the afflicted's system, but is much more potent at base
    Flesh spiders cannot regenerate while on fire

BUFFS

    Time it takes for spiders to normalize their temperature cut by half. While they will react faster when in cold or hot environments, when they leave said environments it will take less time to return to normal temperature
    Unsuitable temperature damage reduced to 4 from 8
    You can no longer push spiders by running into them
    Webbing heat damage threshold increased from 300 to 350 (same temp where spiders also take damage)
    Broodmother egg laying time reduced to 12 seconds from 15
    Broodmother web laying time multiplier reduced to 0.5 from 1
    Broodmother health increased to 60 from 40
    Broodmother damage increased to 10 - 15 from 5 -10

BEHIND THE SCENES CHANGES

    You can now make any simple mob able to be caught on fire by setting flammable to true
    How fast a simplemob stops burning is controlled by fire_stack_removal_speed
    Can now now control how fast simplemobs regulate their temperature using temperature_normalization_speed. Before this PR, this value was hard-coded at 10, I have set the default to 5 as 10 was too long in almost any case. This will notably affect slimes, who could easily die to being cold long after being removed from the cold area. I see this as purely beneficial
    Toxins now have a health_required value. The afflicted has to be above this health value in order to take damage from the toxin. Only used in the spider toxins currently
    When I was setting up simplemobs to be flammable, I noticed basic mobs can be glitchily set on fire, so I fixed it to where they can't be set on fire.

Why It's Good For The Game

    Spacing something is very easy, but not very fun or interesting compared to starting and controlling a fire. Swapping spiders' temperature weakness from spacing to fire is beneficial to the fun of fighting them and playing as them, allowing more creativity and resourcefulness on both sides. Ideally, this should allow for atmosians and chemists to use their skills in a fun way.
    Currently, ignoring spacing them, the only people who can reasonably take on spiders is security, since they have lasers which do burn and stuns to slow the spiders down. However, this small subset of players cannot normally destroy a spider infestation without spacing them, so letting fly swatters and pesticide be used to combat spiders allows other crewmembers to fight back, letting them actually enjoy facing spiders as a threat and allowing the crew to defend themselves.
    Being killed by spider toxin after fighting off a horde isn't fun. The changes still make it a threat you have to be aware of, but not one which detracts as much from the combat loop. This also forces spiders to secure the kill themselves, which is more fun than having the toxin do it for you.
    Broodmothers in their current state are incredibly weak by themselves, which is intentional by design. However, the new changes hope to make playing as a broodmother easier and hopefully allow more broodmothers to get the spider infestation started properly. After all, Dynamic is their common source now, and they should be consistently worth the threat cost to spawn them.
    Previously, spider structures would seemingly vanish for no reason if the room was heated to be greater than 300 but less than 350, as the spiders would not be able to tell that it was too hot. Now, if the structures are taking damage, spiders will also be taking damage, so understanding what's going on should be easier now.
    Pushing spiders into a corner by running into them was not a fun tactic to deal with as a spider and didn't make much sense seeing how big the spiders are.

Changelog

cl
add: Spiders can now be caught on fire
add: Spiders take significant damage from fly swatters and stamina damage from pesticide
balance: Spiders have been re-balanced. Their toxins can no longer kill but they are not as susceptible to freezing
balance: General stats of spider broodmothers have been buffed with more health, damage, and faster web and egg placement
balance: Flesh spiders cannot regenerate whilst on fire
balance: Simplemobs change their internal temperature twice as fast
fix: Basic mobs no longer glitchily catch on fire.
/cl

* Spider Rebalance PR: Burn Baby Burn Edition

Co-authored-by: IndieanaJones <47086570+IndieanaJones@users.noreply.github.com>

---
## [ceccopierangiolieugenio/pyTermTk](https://github.com/ceccopierangiolieugenio/pyTermTk)@[12ee3463b9...](https://github.com/ceccopierangiolieugenio/pyTermTk/commit/12ee3463b918919478147aadbbb0adce7ebcf34f)
#### Thursday 2022-09-08 10:21:34 by Eugenio Parodi

Removed an import that the FUCKING pylance added automatically, FUCK YOU!!!

---
## [matrix-org/uniffi-rs](https://github.com/matrix-org/uniffi-rs)@[ae00abada1...](https://github.com/matrix-org/uniffi-rs/commit/ae00abada1d9a5ab6b9dc6b673722f9de426c5f3)
#### Thursday 2022-09-08 10:45:59 by Ben Dean-Kawamura

Store macro metadata in the cdylib file

The nice thing about this system is that the metadata is always bundled
together with the build output.  This makes it easier to ensure that the
generated scaffolding matches up with the dylib that it's going to be link to.
This avoids the work that `rebuild_metadata()` needed to do.  Metadata
is serialized with bincode to keep the binary size reasonable.

The downside is that we need to parse a dylib, which feels slightly
risky. However, it seems less risky overall to me, since we don't have
to worry about tracking the JSON files -- especially after fixing the
recent the sccache issue.  Also, extracting the symbol data with the
goblin crate is not that bad, see `macro_metadata/extract.rs` for how
it's done.

In order to use the macro metadata, you now need to specify `--cdylib
[path-to-library]` when running `uniffi-bindgen`.  This is annoying, but it
will be simpler once the proc-macros can handle all parts of the interface.
At that point, we can make `uniffi-bindgen` accept either a UDL path or a cdylib
path as it's positional arg.

I didn't add support for external bindings to pass in a cdylib path, since
adding an argument to that function would be a breaking change, then we would
need to do another breaking change to make the param `udl_or_cdylib_file`.  If
external bindings really want to, they can call
`uniffi_bindgen::interface::macro_metadata::add_to_ci` directly.

Added the `uniffi-bindgen dump-json` command that inputs a cdylib path and
prints the matadata as JSON.

I tested that `dump-json` works properly on the following targets:
  - x86_64-unknown-linux-gnu (ELF 64-bit)
  - i686-unknown-linux-gnu (ELF 32-bit)
  - x86_64-apple-darwin (Mach-O 64-bit)
  - x86_64-pc-windows-gnu (DLL 64-bit)
  - i686-pc-windows-gnu (DLL 32-bit)

This seems like good enough coverage to me, although there are a lot of other
systems that would be nice to test on.  The limiting factor was setting up the
cross-compilation toolchains on my machine.  Maybe we should add some more CI
platforms that just run macro-metadata-related tests.

Updated the testing code to pass the cydlib path, rather than the
directory that contains it.

Added an enum that covers all Metadata types.  This is what we serialize
in the cdylib.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[178a45be06...](https://github.com/mrakgr/The-Spiral-Language/commit/178a45be06d1f85f68c86feb9403da147aaf8d12)
#### Thursday 2022-09-08 11:30:44 by Marko Grdinić

"11:45pm. https://youtu.be/1lsg1G4d05s?t=768

I had no idea that Skalds have such good synergies with natural attacks. I didn't think that the claw and bite attacks from beast totem would stack with animal companions. Ever since Rovagug wrecked me, I've been thinking how I could buff my party more effectively. Sacred Hearth is out of the question as only Sarenrae has the community domain. But I am thinking of respecing Harrim as an evangelist to give him the bard bonus. I also need to remember to use the attack bonus of the madness domain before tackling tough bosses. The bard bonus plus that would increase Reg's attack by literally 10.

https://youtu.be/1lsg1G4d05s?t=807
> This will actually stack with Skald Rage.

Holy shit. I should have been casting this on Amiri before sending her into battle.

https://www.reddit.com/r/Pathfinder_Kingmaker/comments/py2n4q/how_are_people_getting_an_attack_bonus_and_ac_of/

9/8/2022

10:50am. A couple of days ago, I made a mistake of going overboard and getting obsessed about specing out Nok Nok. What happened now is that I got obsessed about beating Spawn of Rovagug with my current party.

I can't beat him on Unfair, his AC is just too high for me to blitz him, and he has 1500hp, I've read that it is actually 3k on Unfair. I did get him down 30% before he wiped my whole party. On the second highest difficulty though, I killed him in two rounds though, but it left a sour taste in my mouth. I've looked for strategies online - Jubilost's Holy Bombs, Paladin's Mark of Justice, Kineticist walls. There are ways of getting around the Spawn's high AC.

Ever since I figured out that it is possible to share personal spells using the right feats, I've been aware I've been playing very suboptimally.

What I've done is respec Harrim into an Evangelist Cleric with spell sharing. That will allow him to cast Divine Power (+5) + bard song (+3) + Madness Domain first ability (+7) on Reg who is a Slayer Archer. He is my main damage dealer. As well as Amiri. This should allow them to hit consistently even on Unfair and hopefully kill the boss before he starts dispeling the hell out of me. That boss is like my anthi-thesis because of his dispells.

11:10am. The fact that Xelliren shows up during the fight and has an even higher AC that then boss is just icing on the cake. I'll send Harrim's pet and a few summons to tie him up while I deal with the boss. That should earn me my win on Unfair.

11:15am. But enough of that. Let me just chill here. Today I'll spend some time in bed just thinking. I need to get rid of my obsession.

11:40am. Actually, let me get started. I feel like doing some writing right now.

$$$

(Heaven's Key, Heavenly realm)

    You aren't responsible for the beginning, but you can be responsible for the ending.
    Complete the work that nature started.
    -Loading Blurb

Slowly, out of the pocket of his trenchcoat, the revolver came out. To my eyes, the movement seemed impossibly smooth and ethereal. I had a sense of time and could see exactly the trail the gun followed and as he raised it, where it would go. As if to draw out the tension, the white haired guy lifted the gun straight up, paused it a bit and then swung it down until it was pointed straight at me. He had a grin on his face. I perfect slow motion, I could see him put his finger on the trigger.

I knew what would happen next.

The last time I was here I got shot to death. This time, my mind is whirring a lot faster, so I even though I have a second in game time until the trigger gets squeezed, I have 27h to think about my next move. If this wasn't a game running at 10,000x speed, but the real world I'd have 30 years. Before I had started the game, the controller me did a memory merge, so I understood everything that I'd missed while I was crossing the Street. Right now I have the programming and the ML skills of the controller, and the optimized mind of the instance that beat the Street game, as well as the memories of both.

I understand what the controller wants, which is to beat this white haired dude with my newly found superintelligence.

But as I am staring down the barrel of the gun, I am really wondering what I could do here.

Make my body resistant to bullets? Make them phase through my body? Regenerate the wounds?

I am racking my brain here, but I don't know how to do this. I try to do an act of will here. I picture a rock in very vivid detail and try to manifest it in front of me. My mind is working too fast for the body to react, so I do not make any movements, but nonetheless I try to focus all of my mental abilities into making something happen.

...

As expected, nothing is happening. I do not know how the white haired dude is doing it, but there must be some other trick to it than just wanting magic to work really badly. Expanding my mind and speeding it up, didn't do much to change the situation from where I was a human. I am going to get a few new holes either way.

[Gnosis check DC 1.9 Succeeded - Sampled 2.76]

Imminent death facing me, I get a sudden burst of inspiration. I realize that if I just let things as they stand, I am just going to get shot like last time. It is inevitable. So I might as well quit the game now and go to an earlier save. There is no point in letting the events unfold. That much is obvious, but...is it really? I seriously consider eating a few bullets and then realize something.

Was I really killed last time?

This situation is just too weird. Last time I took it at face value, but it is strange that the game would allow one of the players to kill another. Last time, I just aborted the game due to shock once the darkness overtook me, but had I actually gotten a notification that I died from the game itself?

I do not think that happened. Did I abort the game too quickly to get that notice? Did I simply miss it in my panic? Or is there something deeper to this?

I can't help, but to loathe myself for what I am going to do, but let's eat a few bullets to make sure of what is going on.

Bang...

I put all my willpower into not escaping to an earlier state and let the lead object pierce my chest. Damn it, it hurts! Like last time, I look at it in horror, and on cue the white haired guy empties the rest of the magazine.

Bang...bang...bang...bang...bang...

The speed at which my mind works now really drew out the horror of this moment.

I sprawl out on the table, waiting for death to come to me. Like before, I can see my blood pooling out on the table until it covered my two face down cards. And then my vision became hazy and dark. Like last time, I couldn't make out what the white haired dude was saying. It felt distant...

Like that, I slipped into unconsciousness and death.

But...since this was a game, while it can simulate many things, it can't literally simulate the absence of life. Not without killing me in the real world as well. And now that I am keeping my emotions in order, I realize that despite being dead, I can still think just fine. I can't hear anything, I can't see anything, I can't touch anything. But my mind is working.

I feel out with my senses and I realize that I still have the connection with my chip pile. I wait a while in that senseless space, and there is no change. While I can't feel anything else, my life chips are still there. And I don't get a death notification from the game itself. Meaning, the game was still on.

Experiment - success!

I save the game here and exit it.

I should have noticed this last time, but that is the weakness of the mind controlling program that I used to get rid of my fear. It is one thing to be calm, but creativity requires an active and restless mind. It is easy to notice what is there when you are calm, but hard to notice what isn't. I guess that is the difference between what you need to be a member of society and what you need to conquer it.

(Heaven's Key, Inn room)

I go back to one of the earlier save states. This point in time is exactly the time before sliped out in secret out of my room through the window and explored the city. It was the dead of night and I wasn't tired enough to sleep, so that is why I did it. It was that time I met Mickey in the park of ghosts.

I remember what that translucent old ghost told me. That we are all holograms here. And the system is what determines what exists based on our inner state.

Right now I am sitting on my bed with the lights turned off in the room. I close the courtains and flip them on. Then I manifest a body sized mirror and sit in front of it, pondering.

I need to figure out the trick to becoming translucent. Mickey did it somehow and if I could do it as well, it would give me a hint for how to deal with bullets. I'll go about it scientifically. I do not really know how to trick the system into doing it, but it is not like I can't interface with it at all.

For example...I take out one of the chips, place it on the floor in front of me and using it as a focus, manifest a bottle of water.

Rather than asking how I should change my body, why not instead start by asking how I did this obvious bit of magic?

This gives me a lot of information about the system. It is commonly believed that VR works by hijacking your senses, but if it was just that, then how would movement work? Obviously it has to capture a lot more from the brain in order to be able to do those. But why stop there?

That I could manifest this bottle as I'd imagined it, that is proof that the system understand my desires... and in the dueling realms, it rejects them. Well, Mickey told me as much, but I am thinking things through and confirming them as I go along.

Then the next step would be, rather than just my desires, my true beliefs...

I spend a few minutes thinking about it from various angles.

Honestly, I have no idea how I'd do this if I were a human. If I were a human it'd literally be like trying to develop psychic powers. I'd have to try out all sorts of drugs in order to get something going, messing myself up in the process. Maybe get into the occult mindset. It is dumb.

But as I am now, the various perspectives are all converging to one conclussion. It should actually be pretty easy.

I have access to the entirety of my mind, and thought is merely the transfer of high dimensional vectors throughout the system. A small part of that data describes whether for example I am looking at a water bottle or just imagining a water bottle. It makes sense, otherwise I wouldn't be able to tell my own imagination and reality apart. This is a very good thing, since in the real world, the perception does not affect reality, but here the system is literally basing a part of it on what it sees in my mind.

So if I mess with those thought vectors and conventiently erase the part of the data that tells me what the imagination is, I should make my first step on becoming a reality warper.

Doing this unhindered is dangerous as I'd completely lose track of what is real and isn't.

I understand where things are going with this though. If I could make it safe, I would receive a strong power. Right now even though I've increased my intelligence significantly, my emotional system is still that of a human. When I lost to the white haired guy the first time, I swore that I'd challenge him as a player, not as a character in a game.

This capability of tricking myself to think my imagination is reality should not be in my own hands, but the player's. But there is no reason why I couldn't automate the process eventually. It is like how computer programs become a part of you once you get rid of the interface obstructions, one day the player and the character might be one. Furthermore, now that I've moved from the human model of cognition to my own streamlined one, the tool I was using to regulate my emotions before has become unusable. I need to recover its capabilities by making my own.

I am still a beginner, my capability is nowhere near close enough to the person who made this game. The game is here to teach me.

Anyway, what I have to do is straightforward now that I've planned it out. The first thing I have to get out of the way is the player. The one who is currently supervising me is no good. I need him to have at least my level of capability otherwise he won't be able to keep up.

I really need the controller to help me in this because my own measure of what is sane and isn't will become distorted once I start relying on this power, and I don't mean that in the based, anti-normie way.

I need to account for any and all risks.

Having made my decision, I open up a text editor and compose a message to the controller. After that I save the game, and as a show of will, I terminate my own process.

(Helix Studio, Regent Suite, Bedroom)

I was using the emotion controlling tool to keep my focus up, so I was in fact paying attention to what was going on. Still, it is not like I can read my other self's thoughts. So far, I saw him get shot by the white haired guy, reload back a week ago, and then spend a few minutes staring at himself in the mirror. Then he terminated himself, which shocked me enough to curse. I was really perplexed as to what was going on and started thinking that something might have gone wrong in the optimization process to make him mentally unstable. My thoughts went in that direction for a few seconds and then I realized I got a message from him.

> Subject: Self-Improvement Step Request

What followed is a report by him that went into great detail regarding his thinking since he started the game. It hadn't even occured to me to think about that he deliberated whether to load back right away or get shot purposely. It went on for couple of pages and by the end I got the gist of what he wanted to develop and why he wanted to replace me with somebody more fitting.

> You won't be able to keep up, I need somebody more fitting for the role.

He literally said as much directly to me. Sigh. I didn't think my turn would come so quickly. I've been expecting him to challenge Lily's group without relying on saveloading and was looking forward to seeing how he does it, but it seems a lot of action has happened in his head that I've been unaware of.

...It is just too soon, so let me compromise. The report he wrote demonstrated his intelligence to me, so I no longer have any doubts about him broken in some way. But nonetheless, I want to see him in action before I just hand him the reigns to everything. If something goes wrong, who is going to take the responsibility of explaining that to the main me who is currently sleeping in the real world?

Maybe the role of the controller is too much, but I need to spend a while observing. So I'll do that.

I copy his paused process and do a memory merge. Then I make the necessary setup and start him in a different Helix Studio limbo. Now he should have what he needs to act as a controller. He'll be able to fork himself and start the game.

If this was a real self-improvement step, I'd erase myself here, but I am not going to do that, not yet. He is asking me to literally kill myself for him, so it is fair that I take some time to observe before deciding if I want to go forth with it. The report he sent me was pretty interesting. I'll have him do a writeup at the end of every day. At his speed of thought it shouldn't take him more than a few seconds, and it really gives me an insight into what is going on.

(Helix Studio, Skylark Island)

> Hello, welcome to the Skylark Island. Whereas most character limbos tend to be obvious, this one is heavily inspired by the Simulacrum scenario Wordly Abyss, and it is magic based. In order to acclimate the host, the tutorial messages will show up as you explore the areas. For now, keep in mind that you can access the spell list whenever you wish for it.

Before I copied myself, I wasn't aware of what I would pick, so this limbo is new to me. I remmeber seeing it in passing during past selections. The controller me picked something weird this time. I guess he didn't want to duplicate the Regent Suite.

This place was interesting, it was like a cottage made of wood. There was a table, chairs for it. It wasn't too big, certainly smaller than the Regent Suite. But whereas regular wood cottage were made of modular wood planks and boards, walls, the floors, and the ceiling and indeed the furniture seems to be made of composite wood, as if it were grown. It was how I'd imagine a fantasy druid would build it. He wouldn't use saws and nails, but magic to guide nature into the shape he desired. Looking behind me, I realize what I see is a bed.

It isn't really obvious at first glance, as it looked like some furry, green plant. It had some oversized leaves that felt like animal fur to my touch and bended flexibly as I'd moved it. The pillows were some kind of membranes and I could see liquid inside. I poke it a bit and realize that while it is flexible, it is also tough and wouldn't burst easily. It felt smooth to the touch. I tried the bed out a bit and found that it felt comfortable to rest here.

I like this place. As I walked, I noted than unlike the regular floor, this one was a slightly uneven due to being bark. My first thought that this would make it difficult to position furniture, but when I tried out the chair and sat on it, I found that it had a bit of springiness, that ensured its seat was always balanced horizontally.

The table itself, unlike the floor was made of smooth polished wood. I brushed my hand along its surface, liking how it feels.

This is a really nice feeling of adventure. It is like being a child during its first days in the world.

I take a look at the windows from my sets in the middle of the room, and realize that instead of glass, they seemed to be some kind of translucent membrane. I come up to it, touch it a bit, push it and note how flexible it is. I give it a punch. My fist sinks into it, but the membrane does not tear, instead it bounces me backwards and comes into the original straight position. I approve, it feels reliable as a window.

Looking through the window I realize that the place I am in is quite high up. My cotage in particular is high in the island, but beyond the island it feels like it is a very deep drop given how high it is. It reminds me looking over the edge of the city in Heaven's Key, though not quite that high. In the distance I can see the sea, the mountains and the forests. Sunlight gleams off it, and I get the impression of looking at another natural wonder.

In the minds of people, when people think of techology, they think of steel and concrete. Cars, robots, machines. Guns, tanks, airplanes. Skyscrappers.

But maybe that is wrong. They haven't realized it yet, but maybe the true form of techology is celestial in nature. These simulated worlds. Can breathtaking wonders that I've seen, and the powers that I am trying to attain be anything other than divine?

The brain cores that I've gotten are supposedly mostly made of carbon. Experiencing them from the inside, they don't feel technological in nature at all.

I brush away these thoughts and come to the door. It doesn't have a handle, but two wooden hook on the side. I detatch them and the door slides inward as it were a measuring tape. Like the windows, it the door was made of sturdy and flexible biological material that looked like wood, but was more like plant matter that I'd guess doesn't exist in the real world.

I poke my head outside and realize there is a huge drop below. As I imagine splattering myself below, I get a sense of vertigo and take a step backward.

> If you want to exit the building to explore the rest of the island, please use the Wings spell.

I get a helpful notification and do as instructed. As I do some large fairy wings manifest themselves on my back, and my body feels weightless. This reminds me of being a disembodied entity in the Heaven's Key title menu, and I find that it is much the same. Rather than having to beat them against the air to take flight, they are more like an antigravity device attached to my back.

I have no trouble controlling my flight and exit the room to explore the island beyond.

I spend some time playing like that and then I create a fork of myself and plug it into the game.

(Heaven's Key, Inn room)

"I am visualizing my hands at twice their usual size. How are my recordings?" I ask the controller back at the the Skylark Island.

Back in the game, I am seated in front of the big mirror. I have my hands raised in front. I think it is due to the latest batch of improvements, but my imagination is very vivid compared to before. I can almost see my enlarged hands overlaid over my regular ones as if they were real. No amount of desiring they are real will be enough to make it so. instead the controller me has to be the one to make the step. While I am focusing on visualization, right now he shuold be looking directly at my brain studying the neural messaging as it occurs.

"I've recorded it, but it is a bit hard. Instead try imagining yourself pinching your hand." I do as instructed.

"Good, now actually pinch yourself lightly." I do it just enough to be a bit painful.

"I see it. Now relax. Don't try to think of anything." I do so. What happens next is that I get a bizzare feeling of having my hand in front of me and pinching it with the other. It feels a bit dissonant, but eventually that fixes itself by me focusing on it. Just like before, I seem to be imagining pinching myself, but there is an obsessive streak to it. I am finding it difficult to focus on anything else. After a bit I get relieved.

"Good. I've aborted the program, how is your mental state?" He messages me.

"I seem to be fine." I reply. "The obsession is gone."

"Is that how it feels like? Anyway, I'll try the actual pinching next."

"Ah!" Feeling being pinched, I raise my hand to look at it. I expected to see some pain, but I am surprised to see that my skin is physically twisted. It is as if an invisble hand was pinching it. I try to relax the skin with my other hand, but it does not help. The feeling of my skin being pulled remains and after I remove it, I see the pinching fold again. "Are you seeing this?" I show it triumphantly.

"It is a success! I think I understand this. Let's try the hands again. This is like hacking memory states to cheat in games. Focus on the hands and I'll try edit the relevant thought vectors based on the previous recording. I don't want to make everything real."

I raised my hands in front of me and focus, imagining them to be oversized. As I do so something in me shifts, and to my surprise, it works. What was once imagination turns into reality. I clench and unclench them, marveling at the unfamiliar sensations. I try using them to lift the water bottle and unscrew the bottle. It feels so weird, but they aren't clumsy. I take a gulp, and screw the cap back on.

"This is pretty cool." I show of my hands in front of me. The controller can't see or feel anything my senses can't. He doesn't have direct access to them through his own mind, instead he is looking at what I am seeing through the screen. Eventually what we have planned is to integrate the rest of the senses into him, so he can feel directly what I feel through separate neural channels. If the controller had that kind of ability, it would make his work a lot easier. At the end of that road, what the controller will become is a higher order consciousness for myself, able to control me as I would a video game character.

At that point, we'll be able to do these transformations instinctively. For now...

"This is cool, but let's turn them back. I'll imagine them being normal. You do your thing." I message him.

I look at my hands and imagine them being as same as before. As I watch, I again get that strange impulse like a gear in my head has skipped a turn and the hands transform back into their previous shape. I flex them to test them out and satisfied, I let out a breath.

"Phew. We've got it!"

That white hair dude is going to get what is coming to him. Right now I could go back to that dead end, and try to resurrect myself. Except, it is one thing to imagine my hands changing shape, but quite another to imagine having a living body. I am getting to ahead of myself. We did just the very first step. The program we have is not capable of flexible whole-identity transformations. We should challenge him when we are ready.

Right now, how about we beat on some noobs?

I think back to Lily and Dale's group.

They are the ideal testing ground to develop our skills at programming the language of the mind.

Back then I just scammed them out of a ton of chips, but then they sent the tough white haired guy after me. This time I am not going to do it using saveloading, but with my own skills. Maybe if I did it that way, something different will happen.

Me and the controller burned the candle late into the night, creating some simple cheating methods and trying out what we would call the True Belief Modification. It wasn't until later that we realize that the method we invented was the legendary hallmark of the stories of the Inspired. Their titular ability was called the Inspired Desire. This was its embryonic form.

(Heaven's Key, Raven's Eye Casino, Shadow realm)

"Fold." On the small button, Lily folded.
"Check." The thin guy who has been looking down on me, follows up.
"Fold."
"Fold." The two guys behind me toss away their cards.
"Call." I limp into the pot. I look to my left, and see Dale deliberating. He raises from 4 to 12. I look at his face down card, and mased on the red markings, I note that he has suited AhTh.

My own hand is crap, an unsuited Jd 7h. To Dale's left, the thin guy thinks for a bit and folds. Unlike Dale's card, only one of his cards had a marking. Even though my hand is weaker than Dale's, since I know what he is holding it is hugely beneficial to enter the pot regardless, so I call.

The flop manifests.

Ks Qc Tc.

There is a flush draw on this board, but Dale has hearts rather than clubs. He hit a low pair. A very dangerous flop for him. I do not hesitate and lead out by betting 20 into the pot. Dale hesitates and stupidly makes a call, bringing it up to 70.

On the turn, 5c comes out. Not hesitating, I shove my entire pile and go all in.

Dale stares at me for a while, trying to read my mind.

"Fold." He makes the sensible decision, and I increase my pile by 38 chips.

In this hand, I happened to have a straight draw, but I'd have played it the same way regardless of what I was holding.

The hands we are holding get purged, and the next round starts promptly. I get dealt two cards, and luckily, they don't have markings on them. I check my hand to see what it is, 2d 9c, and silently message the controller.

> Manifest the UV pigment on my fingertips.

I feel the familiar feel of something skipping in my brain and with a light touch put two marks in the right places. With a light brush, as I move the cards, I make two angular lines at 30-60 degree angle to either of the edges. That way if the card is rotated, I won't be confused as to which is the rank and which is the suit marking.

As I look at the group, each them is covered in a film of blue, or more more to the point, my entire vision is that way. I've modified my eyes so I am capable of seeing in UV. It wasn't too difficult, it used to be the case that laser surgery of cataract got rid of the membrane protecting the lens, which allowed the patients to see UV. I had to study the structure of the eyeball for a while, but after that I modified my true belief to change the structure and got the ability to see in UV. After that it was just a matter of doing research on pigments and finding the right one.

Thanks to this cheating method, I can take it easy during the first few revolutions, just marking cards and only playing strong preflop hands. After that once the blinds go up, I can loosen and jump into the fray to land a sneak attack.

A few days ago, I started the matched at 240 chips, and now I am up to 600. My winnings are a lot slower than when I was saveloading, but I am really happy regardless. This is real power! I worked hard to get to this point and my reward is that now I can beat these people. It might be possible to use something like this in real life, but the method is too unrefined and would easily be found out in a casino. Here I have my improved eyes, and can manifest the pigment directly on my fingers. If I had to carry around a can of it in my pocket, it would quickly get spend. Moreover, I wouldn't want to damage my eyes just to cheat at cards. My vision might be crap so there is no need to make it even worse. But if I came to the table wearing fancy UV glasses, it would raise some eyebrows.

Using this method in reality is beneath me. I have much better things planned.

Anyway, I continue playing and notice that things are moving quicker this time. Whereas before the party tried really hard to bust me, now that I am winning using what looks like actual good play, the party is close to breaking. I can tell that the others are hesitating and exhanging looks when I propose duels.

A few days earlier than last time, Lily doesn't arrive and her place is instead taken by an old guy named Geoffrey.

After a few games with him, I get the sense that rather than focusing on winning, he is instead watching me like a hawk, not really caring about any of the other players. He radiates an aura as if he is preparing to strike me, but nothing happens and I just end up making some money off him. This is fine, I guess.

(Report by Geoffrey to the Enforcement Department)

Subject: Aleator-level enforcement request

One of the newcomers from about a week ago is currently in possession of 680 chips. I've played him personally, and in my estimation, he is at least a low ranked Aleator who possesses the ability to mark cards, probably via UV markings. He does a little move where he brushes over the cards after looking at them. He employs a strategy of playing strong hands at the start, and once the cards have been marked, he loosens up and picks the other players off. He has decent gameplaying skills from what I've observed even without the use of cheats.

We've done extensive background checking and confirmed that he is a newcomer, he should be easy prey for an experienced Aleator.

In the attachments are the report I received from my subordinate guide as well as my own. The reports have extensive recordings of our games with him.

(Heaven's Key, Streets)

Night comes, I go back to the inn, and then once the morning gets around it is time for action again.

The next day I play with Dale's group again, but they've started to clam up. Once I realize that I switch to bluffing more often and take the money off them that way. I was uncomfortable of going all out, but the controller did some modifications and spiked my confidence, allowing me to execute the strategy properly. I blitzed the table, and it felt good picking on those weakling with my strong bets. Hell, yeah!

That day, as the sun was falling beyond the horizon in the background, I exit the casino in high spirits, swinging a pair of big ones.

> Be on guard. I think that guy Geoffrey was responsible for sending that white haired guy after us last time.

I get a message from the controller. We are a dream team, me and him. My own skill at both manifesting my imagination and poker is growing, while on his own end, I can sense he is getting new insights about the mind. We've already recovered a lot of the functionality of the mind controlling app over the last week.

Doing as he instructed, I unwind a bit and take note of the surroundings. Gleaming golden buildings enter my attention. The rays the light look quite beautiful at this time of day, painting the town in a crimson tint. The work day is starting to wind down and I can see people returning to their places. The usual boisterous atmosphere of the golden city is starting to quiet. Compared to the real world, where you usually have some insects chirping at night, when it gets quiet here, it becomes deathly quiet.

As I walk the streets, the previous scenario repeats itself. Not the white haired guy, but some other one walks around the corner and moves straight towards me, looking me straight in the eyes like he wants to kill.

Bang!

(Heaven's Key, Shadow realm)

After the bullet was fired from a gun, I find myself in the familiar duel space. Looking around, I am surprised that the background is the familiar deep space with bluish nebulas. I thought that resolution matches would be different, but maybe the reason for the background change last time was different. I take a good look at my assailant. Unlike the white haired guy, I am not going to let this guy off. I am going to send him straight to the grave. I am going to kill for the first time.

As I think that, my killing intent surges. Forget those tiny duels against Dale's group. This is what a real match should feel like.

My chips here are my life and blood. Even if I beg, the assassin is not going to let me off. There is only way to survive, and that is to kill him first.

I calm myself down and take a deep breath. As I do, the well dressed pig on the other side gives a snort and takes a glance at his hand. He looks like a stereotypical NEET, but rather than grease stained sweaters and years-old clothing frayed around the edges, he is wearing a fresh monochrome suit. I think it looks quite decent on him, I myself am wearing the same casual clothes as in the real world, so I lose out versus him on the fashion front. Still, he should consider getting a diet. I am not sure if that is even possible in this city though. He was probably a NEET before he died and got stuck in this form.

So then...that probably gives me a good estimate of his ability. Since people wouldn't want to look like him, and he himself would probably want to change his appearance to something better, I am guessing he can't do form changing using True Belief Modification like I can. This is just a conjecture rather than an actual fact, I can only interpret this situation as making it more likely than if he had regular body mass.

"Check." He does the move. I

> Modifying the eyes.

As I get a message from the controller, the world becomes covered in a thin layer of blue, which is the UV light as I perceive it.

Using my thumb to twist the cards upwards, I take a peek at my hand. Trash unsuited 2s 9h. As I close it, I make sure to put the red UV markings on it. Rather than stamping my fingers on the cards, through practice I've managed to make it look natural, and I can mark the pigments using only a light brush. My enhanced dexterity is realy convenient here. It would have taken a lot of practice to make it inconspicous otherwise.

I decide to fold this particular hand and we move to the next round.

8d 4h. I mark it again, the NEET guy calls, and we move on to the flop. We check all the way to the river and I lose to a T in his hand.

The cards and the board demanifest, vanishing as if they were getting vacuumed into another dimension. Then two cards get spat out of the air to land right directly in front of me. The same happens for the NEET guy.

"Check." He take a look at his hand and checks, looking at my reaction.

Ac 3d. On the button, I see that I got dealt a decent HU hand. During the couple of years I spent programming, I did have time to spend some of it playing against my agents, so I at least have the basics of various forms of poker down. As a player I am actually a lot worse than my own trained agents, but I can immitate them to a degree.

"Raise." Making sure to leave the marking on my hand, I pick out the 3 chips from my phantasmal pile of 735, and place them on the table and min-raise to 4.

"Call." The flop comes out next, the cards gently manifesting themselves on the table.

Ac Js 5s. The NEET guy checks, not hesitating, I put in a pot sized bet. He thinks for a bit and then folds.

Poker tends to be like that most of the time. Long periods of folding followed by brief bursts of intense action. It won't be long before the antes go up and become a significant part of our stack. At that point, the markings will play a decisive role. The quickly increasing antes are like the water level threatening to drown the players. The only way to stay above the water is to take the other players by the shoulder and lift yourself up.

Qc 6s...
3d 9d...
7s Jc...
2h 4h...
6d 6c...

The cards continue flowing, and I continue marking them. It won't be long until I have a decisive advantage against my opponent. HU situations really favor me, with Dale's group by the time I've finished marking the cards, the antes tend to have risen high. A lot of the time I've gotten put into a situation of having a good hand, but the interference from having too many players on the table caused the situation to go out of control. 1-on-1 you are never waiting for a good hand preflop, and the action is always flowing. This will maximize my edge.

(Geoffrey POV - Heaven's Key, House in the suburbs)

"Here you go." My host and friend, Walter placed a cup of tea in front of me. Seated at a table, the sweet aroma from it wafted into my nose. It takes some skill to make exotic teas really come to life, the ones manifested using the system tend to get stale after a while. I take a sip. "The flavor of your tea is as good as ever."

"Thank you. I haven't seen you in a while Geoff. It must have been a few years. What have you been up to?"

"Just my work. Since I put in that request, I thought I'd come by and talk to you about it. I am curious who you sent after Euclid." The enforcement requests aren't that frequent of an occurence, they usually happen one every few years on average. They are especially rare against newcomers, usually it is the citizens which get tired that start causing trouble.

Walter, a grey haired dandy like myself, tastes his own drink. After a bit he answers.

"You've met him a few times, I think. It was Louis." Louis, Louis...I remember him.

"Ah, I remember. He is the young man who came by a few times. Wasn't he just starting out his training?" I start to feel concern and show it on my face. "Are you sure about sending him out? Will he be fine?"

Walter looks at me for a bit, and laughs lightly at my expense. It seems my grasp on time must be more tenuous than I thought.

"Good one, Geoff. He finished his training over a 100 years ago. I think it was 150 years ago when I first introduced him to you." It is like thunder is running through me. I'll never not be shocked in situations such as these. I've lived in this city for a long time, and it seems it is true what they say about old people. Some of them can't remember yesterday, but can remember 20 years ago as if it were that.

"That is good to hear. What is his rank now?"

"Mid-Aleator." Very few people have the talent to become Epistemes, and most of the Introspects in the city couldn't reach even the level of an Aleator no matter how hard they tried. I myself couldn't. I remember being arrogant in my youth, but I realized that talent is something beyond people's control eventually. That was a long time ago. Now I can accept people as they come.

"I suppose there is nothing to worry about against a newcomer then." I enjoyed my tea. The most important thing in life is to flow along. Even if you don't have talent, you can still live, and if real trouble arises, the Epistemes will take care of it. I used to think it was a tragedy that my desire could only get me so far, but then I turned around and realized that it would be hell if everyone were allowed to rise. If everyone had the talent of an Episteme, this world would long have ended. I used to hear stories how the city was at the beginning, and am glad I wasn't there to witness it.

"If you don't mind telling me Walter, what is his speciality?" I inquired.

"Are you curious?" He teased me, raising his eyebrow.

"Of course." I smiled.

"His eyes. It took him 30 years, but he managed to improve his vision to a level where a reflection in another person's pupil is as good to him as we see regularly." Peering Walter's gray pupils as he said that, I could see a light reflection of myself.

(Heaven's Key, Shadow realm, Resolution duel with Louis)

Ghhhh...

The blinds have doubled twice and I've marked most of the cards, but I am not winning. I've started the game at 750, but since then I've fallen to 520.

The button comes over to me, and I get dealt my cards. I do not even have to look at them to know what they are Kc Qh, a good preflop hand heads-up. On the other side I see that he got Ks 2d. If I could get a king pair, I could take some of my losses back.

"Check."
"Raise." I min-raise to 16, he calls and we get taken to the flop. I hope that a king comes out there.

3s 5c Kd.

"Check." The NEET guy checks after thinking about it for a bit. It wouldn't be unusual for a player to bet anywhere between half a pot to a pot here. His hand is pretty strong, but it seems he is slow playing it for some reason. In that case I'll do it.

"Raise." I bet 16 chips, half a pot. I am keeping a poker face, but I expect he would at least call here. This bet is not unusual for me, I usually put in this much on both bluffs and value bets.

"Fold." What the hell? That was such a good setup, I should have won at least 50 chips on this hand. How is it possible that he folded this? Usually he plays like a calling station, just waiting for me to put money in. Most of my losses so far came from trying to bluff him out of a low pair. Why is he folding a high pair.

I've been looking at him this whole time, it doesn't seem like he is doing any kind of marking.

> Hey, what is my mental state? Is it possible that I am giving out some kind of tell? This fold was too good.

I ask the controller. It is his reponsibility to take care of this.

> No, you are fine. You are a bit frustrated at being down so much, but I've been keep hold of your facial expressions and body language. Absolutely nothing should be showing up.

I can't do anything but trust him. If he got it wrong, I am prepared to die here, but otherwise I'll reason as if nothing is wrong on my face.

The next couple of hands proceed as usual. The chips clank as they are moved around, and each of us folds to some light bets after missing the board. The blinds double from 4/8 to 8/16. I can already feel my entire stack being at risk. While at the start I was over 350bb deep, right now I have only 32bb to bet. If the blinds keep doubling, in a couple of revolutions, winning a hand will become a pure coin flip.

A new round starts. I am on the button and get dealt Ts Th. I look at what he has and see him holding 6c 6d. This is really good, my hand is dominating his. If we went all in preflop I'd be 80% favorite to win.

"Check."

In response, I min-raise him to 32. He calls.

6s Tc Td.

...Holy shit. I admit, if I'd been playing as a normal human, I'd have definitely given off a tell in this situation. I'd have straight up jumped out of my seat. Instead, I experience the expert work of the controller, and keep it perfectly cool at this huge stroke of luck in a death match.

I have quads, while he has a full house. Unless he can really see what I have, there is no way he can avoid going all in here.

"Check." I honestly feel annoyed that is slowplaying this particular hand.

"Raise." I bet 32 chips into a pot of 64.

"Fold." He just throws his hand away like it was trash.

Shivers run through me, and it feels like somebody splashed a bucket of cool water over me. I feel dizzy.

It seems my dumb cheating method will not work. I am going to die.

(Geoffrey POV - Heaven's Key, House in the suburbs)

"So Goeff, you've played with the kid. What is he like?" Walter asks me.

"He is very talented, probably a genius." I remark. "But a genius without experience is still just an ordinary person here. For example..."

To make my point, I manifest a deck of cards and place them on the table. I pick one of the cards and place it next to the deck. Then with one of my fingers pointed, drag it along the surface of the card making a red mark across its back.

"Introspects can't do anything, but once they figure out how flexible their being is, they start to think up ways to cheat. Of course, the very first thing they do is mark cards in various ways." I say to Walter. "I remember when I came here, I couldn't really manifest the figment directly so I took to manifesting cans directly on my person because it was easier. And I had these UV shades..."

I manifest a pair of slick shades and put them on, grinning.

"Heh heh heh, I did that as well." Walter remarked.

"The next day I'd get called out as it was quite obvious. I'd be reaching into my pocket every once in a while when the UV paint dried, and everyone could see it."

"It is better to just manifest the pigment on your hands directly."

"Yeah, the low level Aleators quickly figure out how to do that. This kind of cheating is a lot more reliable. You can go a bit far in private games that way until the rest wise up."

"In the Heaven's Key tournament it doesn't matter if the other know if you are cheating or not. Even just being a low level Aleator is enough to survive on your own without the loss of chips. To get into the money you just need to survive the first round, and these kinds of methods are more than good enough. The trouble for Introspects is that even if they know how to cheat, they have no way of bringing it into the dueling space. They can only train their skills the regular way."

I nod to him.

"Yes. The next level is to start transmuting your body in order to enhance it. Instead of wearing shades, you change your eyeballs so they can see UV. That is much less obvious."

"And Euclid is at that level?" Walter asked.

"Yes, but he is not as good as Louis."

"You said in your report he is a newcomer. Are you sure? Because being able to do this in your first week is unheard of. Maybe I should have sent somebody better, but it was time for Louis to take on some actual work rather than just training."

"Yeah, definitely. And because of a newcomer, Louis will be able to win because of that." I reassured him. "It is not just because of the eyes. Euclid is relying on marks to cheat, and such marks.."

I point at the card. Whereas before I dragged my finger across it to paint a mark, this time I just do it across the air without coming close to the card. Like casting a spell, he red mark I made on the card disappears.

"...can be erased. Mid ranked Aleators also do not need to rely on their body directly to cheat." I do a swish in the air with my finger and the mark gets painted across the card again.

I look outside the window and note the time. The sun had set, and according to reply the enforcer is supposed to challenge Euclid at this time.

"Right now Euclid should be sweating..."

(Heaven's Key, Shadow realm, Resolution duel with Louis)

For the first time, my opponent makes a reaction. I see his lips curve into a slight grin.

He can see into my hand. Absolutely. I look at my cards and note the marks I put on them myself. It might be because of this. I could get rid of them, but then I wouldn't be able to know what cards my opponent has himself. While I was thinking along that direction, out of the corner of my eye I spy some movement. My opponent twirls one of his fingers, and my two cards become covered in a layer of UV paint. The marks I have put on are completely overpainted and rubbing my fingers against it, I realize that the paint is fully dried. I can't clean it off.

I look at my opponent and I see that on his side, he did the same thing as well. The marks on his cards are unreadable.

I realize what this means. He is not going to let me use the UV painting method anymore. In future hands, I will be flying blind!

I start to feel the approaching doom. Right now, I feel a tangible sense of threat from my opponent. He is on a completely different level from Lily and Dale's group.

(Geoffrey POV - Heaven's Key, House in the suburbs)

"So the kid will definitely lose..." Walter remarked. "Well, it is too bad for him." He immerses himself in tea.

Something in his comment stirs something in me, and I start thinking about it.

"Well, it is not absolute. There is a very small chance that I've misjudged Euclid, and he has the latent abilities of an Episteme. Unlike the Introspects who have known talents, he is a newcomer. I just didn't have enough time to judge him fully."

"Hmmm..." Walter looks at me askance.

"I am just speculating how Euclid could win. Don't tell Louis about it afterwards." I urge him.

"I won't. So how could it go?"

"Have you ever played against an Episteme?"

"I've been placed at their table plenty of times in the Heaven's Tournament. It ends up as a slaughter. At that level you can't call the game poker anymore. It is more like fighting a wizard casting spells at you."

"I once went up against Gray one-on-one." I admitted. I didn't need to explain who Gray was. All the Epistemes were famous throughout the city.

"Really? What happened?"

"Gray loves using the trick of pulling out a gun and firing it at his opponent." I pause as I recall how it went.

"Did he shoot you?" Walter asked.

"He shot at me for about half an hour straight."

"That's nasty." Walter grimmaced.

"There I was at the table, trying to disbelieve the bullets so they don't hit me otherwise they will knock me out. Sweat is pouring down my face and I can't even look at my hand due to intense concentration required. I haven't played a single hand the entire time, instead the system folded me automatically every 5 minutes. Gray himself had no trouble making raises."

"So he shot you in the end."

"Eventually I got tired and one of the bullets came through. At that point I blanked out and when I woke up it was in a hospital room. Thankfully it was not a resolution match, but a regular duel otherwise I would have gotten killed."

"I see."

"That is how Euclid could win even if he was outclassed if he really is an Episteme." I pointed a finger gun at Walter. "Just manifest some kind of weapon and blast away until the other side crumbles. The way Gray did. It doesn't require too much skill or grace assuming he knows how to make a working gun and has the sheer ability needed to manifest it."

"..." Walter looks at me in silence.

"The most horrifying thing for an Aleator is to go into a resolution match against what he thinks is a lower rank, only to have it turn out he is facing an Episteme."

(Heaven's Key, Shadow realm, Resolution duel with Louis)

I won't guve up with just this. Let me bring out all my aces in the hole. We'll go all out!

> Let's try the gun. Just like the white hair guy did.

I message the controller, and feel my senses start change.

I raise my hand and per my will, a polished, gray revolver manifests in it. I open the magazine, and with a mental trigger manifest a clip of 6 yellow bullets before inserting them into the slots. I point the gun at my opponent and on his face, I see a sign of visible alarm.

Bang!

I blast the bullet directly down the middle of his forehead. My mind is fast, so I can see the bullet in strong slow motion as it travels its path to where I intended it. But as soon as it came close to touching his skin, rather than piercing, the bullet instead disappears. If I were a human, at this point I might have simply concluded that I missed, but I could see every single inch the bullet traversed, so I am sure there is no chance of that.

Bang! Bang! Bang! Bang! Bang!

Not having anything better to do, I empty the rest of the magazine into the guy, but the results are the same. I am not sure whether to stop or to continue with this, but as I look at the terror on the face of my opponent, it induces me to do more of it. I open the magazine, let the spent casing fall out, manifest another clip in my hand and reload the gun.

Bang! Bang! Bang! Bang! Bang! Bang!

Nothing happens, but my enemy is afraid so I continue doing it.

Bang! Bang! Bang! Bang! Bang! Bang!

Reload.

Bang! Bang! Bang! Bang! Bang! Bang!

Reload. Like so the silence at the table is punctuated by a constant barrage of gunshots.

I continue repeating that for a few minutes, but nothing is happening. And while I gave him a great scare at the start, he catches his bearings and calms down.

The look on his face pretty cool now.

I could do this for as long as necessary, but it doesn't seem shoting my opponent will is doing me any good here. I guess it is how in RPGs the bosses are immune to sleep and paralysis effects, anything that would kill them outright on a failed roll. I am guessing he has some technique that renders him immune to this cheap method of winning.

Plus, going further with this method will do me no good in real life. The same goes for saveloading.

I toss away the revolver into the abyss below, not taking my eyes away from my target. I carefully note my opponent's reaction and if he is feeling relieved to see me do that, he is good at hiding it. I won't work after all.

> It won't work. The guy is as cool as in a freezer now. He got used to it.

I message the controller.

> We'll go to the next stage of enhancing our senses. We made this during the night, and we'll put it to use now. Here is the Enhanced Biological Eye.

I feel my vision start to warp and take off my glasses. Since I won't be needing them I treat the same as the revolver and dump them into the abyss. I blink a bit as I become disoriented due to the barrage of information coming from my eyes, but I quickly adjust and the world comes into focus. When I look at my opponent's face now, I see every little pore on his face. It really magnifies his ugliness. But instead of focusing on that I focus on his beady, pig eyes and see my own reflection in them.

"Check." Since it is my turn, I take a look at my hand before checking and wait for my opponent's response. He min raises, and I fold my trash hand.

The next round starts and we both get dealt new hands.

For a few moments it feels like we are in a standoff, each waiting for the other to check his hand first. Making no movement, I wait for him to start and he yields, seeing no reason to delay further. Each of us can only check their own cards or the opponent's so it does not matter which one of us does it first. Only in the case that we both do it at the same time, we won't get any information.

He does so, and reflected in his eyes, I see his hand.

Ah Kh. A premium hand.

He raises off the button to 24. I take a look at my hand and then chuck it without needing to think about it much.

Last night, me and the controller worked on a new eye model. We took the eagle as reference, and then had an evolutionary algorithm optimize the cross between it and the human eye. With my newly improved eye, I'd have no trouble spotting a mouse far in the distance from the top of a mountain. Or a slight reflection of the cards in my opponent's eye.

But at this point at best, I've closed the gap with him.

In order to win, I need to deny him the advantage of looking at my own hand, assuming that is what he is doing.

Last night after we'd finished designing the eye, we thought that we might run into an opponent trying to take advantage of lens reflectivity, so we did an anti-reflective version as well.

> It works. Make the pupil anti-reflective next.

I don't detect any changes to my vision, but I get a message saying it has been done.

The NEET assassin looks at his hand, I see it as trash Js 5c in his eye's reflection. He finishes his peek and turns to observe my reaction. It is a request to which I oblige. 2c 3c. The hand itself is worthless in this HU situation, but the look on his face after I finish is priceless. Whereas he was merely scared when I started to shoot at him, right now he is slack jawed open.

Now it is my turn to grin. This is quite satisfying, more than just moving chips around after winning a hand, this moment is when I truly experience victory.

Are wondering what my hand is? Well, keep wondering!

I haven't tried out all of my trump cards, so I am looking forward to it. I appreciate this guy as an adversary. Though the white guy is tougher, I wouldn't have gained as much fighting him.

As I start to wonder what he is going to do next, my bet is on him manifesting some anti-reflecting shades to equalize the field. I had a response planned for that.

Somehow what he did next should have been entirely obvious, but it came completely as a surprise to me anyway.

(Geoffrey POV - Heaven's Key, House in the suburbs)

"So if Euclid is an Episteme, would Louis have any chance to win?" Walter queried.

"No, I don't think so. But it doesn't mean that he necessarily has to lose even against a superior opponent. We carefuly note down how many chips the newcomers have won for a reason. As long as he has more than the opponent, he can put pressure on him and seek to break up the match. It is putting game theory into practice."

(Heaven's Key, Shadow realm, Resolution duel with Louis)

"All-in!" My exuberant mood was immediatelly dampened once my opponent did this.

Oh, no.

"Fold." He had J5, and I had 23, so he was 62.5% sure to win if I called him here. The fold was easy. But...

"All-in." He didn't even bother looking at what his hand was. Instead he manifested and pushed in his entire stack. And for the first time, I could see exactly how many chips he had. The game itself was aiding my ability to detect chip amount, so I could tell that he had exactly 5322. He started at 5000 exactly, and took 322 from me along the way, and now I was at 418. It was a great pile that dwarfed my tiny stack. I'd have to win 4 times in a row just to get to a safe position. If I lost, I'd die. But he on the hand, if he lost would just lose some chips. It is not a big deal to him.

In this realm of shadows, that golden pile glimmered with a radiance, representing absolute power.

I looked at my hand, and saw that I had Qh Qc. If I was playing poker in the real world rather than a game, this would be a very easy call. But even if he had something like 36 or J5, any two lower than the queens, I'd still only be 80% certain to win. In other words, I have a 20% chance of dying. And now that this is an outcome, I realize that the chip amounts do not matter.

What is going to happen next...

"You are too much for me, champ. You are really good." My adversary buttered me up. "Let's stop the match here."

"..." I pondered his words intently.

"You've managed to get 300 chips from Dale's group. And with your skills you don't have anything to fear from the Heaven's Key tournament."

"..."

"From here on out, I'll be shoving blind. If you wait for an opportunity you can make the call where you are 70% ahead. But that just means you are 30% likely to die. Risking your life on these all ins is not worth it." He was doing his best to keep a confident demeanor. "In order to take all of my chip, you'd need to win 4 all-ins. Even you are 70% ahead, the odds of you doing that 4 times in a row is only 25%. Meaning, if you decide to face me here you are 75% likely to die."

"..." He is right. He is right, but even though I agree with him, why am I starting to feel livid? This feeling inside of me is pure rage.

"Do the right thing. As long as you hide and keep quiet, the other enforcers won't bother you."

I hate him for snatching my victory away from me, just as soon as I gained an advantage. In my mind, I keep going between thinking of these people as NPCs and real, but it is right now that I realize just how smart they really are. I should have all the advantages in this match and yet, I am the one being pressured now.

I hate him so much I could die!

That is how I feel right now. Like some beast, I feel like growing at him to show him just how much I hate him!

Maybe I am a fool. I haven't thought about this aspect of the game at all. Last night I've been focusing on how to cheat. I spent all that time designing eyes. I even came up with a design that I'll be able to use in the real world once I improve my nanofabrication skills. I can't replicate biological organs, but with the nanofog it would be possible to make nanomachine organs better that the biological ones.

That is my real goal. My goal is not actually to beat Heaven's Key, but to have it serve as launching pad for beating the real world.

This also the reason why I was not eager to challenge the white haired guy again. What point is there in fighting somebody who pulls out a gun at the table? That is not going to happen in a real world casino! I simply don't care about the advantages in the game that I cannot make use of in the real world.

This is why I am so disgusted at this situation. It is forcing me to care.

Suppose I do the rational thing, and we abort the match. I'll be able to get on with my life in this city. But they'll send somebody better than this guy who is capable of countering my current tricks. Then suppose I manage to gain an advantage. All-in! I imagine him doing just the same thing as my current opponent. I'll have to break up the match again, all for the sake of rationality. I'll really be an easy target to play against, an experimental pig for them to see how much it would take to break me. I'd get a neverending stream of opponents I can never beat as they pluck my chips away one by one.

In that case, wouldn't it be better to just die here, than having to endure living such a life?

[Gnosis check DC 2 Succeeded - Sampled 2.85]

Life is a paradox. The highest goal is to attain omnipotence, but if you care about own life you can never accomplish it. I'll put my pride ahead of rationality and just die. I'd rather die like a lion, that live like a mouse!

I check my hand and see that it is Ah 5d.

It is good enough. I'd call a random hand with this in the real world.

With a mental command I manifest my entire pile in the air amove me. Then I smash it down on the table in front. As the chips land the table shakes in a satisfying manner, and peering into my opponent, I can see his eyes widen in fear. Yeah, this is what I want to see. Sweat you pig! Gazing at my opponent with undisguised bloodlust, I grab a few chips from the pile and play with them as I think.

I've already decided, I am going to fight until one of us dies.

As I gather the will to call, I start getting inspiration. Is it really necessary for me to die here? Have I really exhausted every possibility there is at this table?

I have some more abilities I haven't used, but those wouldn't help me at all in this situation. I have two problems:

* My opponent's cards are hidden.
* The community cards which are going to come out on the table are hidden.

If I could break these two problems, I could win even in this scenario.

If I was a real Inspired, I'd have control over nanomachine clouds. I could control those tiny machines to sneak under the opponent's cards and read them out to me. As for the deck, who knows what I could do about it. Since the game transports me to a different place once the duel starts, most likely the cards held in a different realm by the system and transported here. But since the markings get preserved, I can be sure that the cards aren't simply being manifested as needed. The deck definitely exists somewhere.

Still controlling nanofogs like in the stories is far beyond me at the moment. I could exit the game here, and spend a few decades training myself in this, but who is going to put this amount of effort just to beat this game. It is not worth it. What is the point of playing a game if you need to be max level at the start? That is more like real life.

If I am going to win, it has to be with my current abilities.

Do I have any possibility of doing that? I don't but...I suddenly recall what my opponent did. A little while ago he waved his finger and erased the marks on my side of the table.

...How did he do that? I didn't really care about that until now, but now I am suspicious of that.

Nanomachines? Of course not, there is no way a human would ever have the ability to control something of that sophistication.

Rather...I start to think about the cards. When they are dealt, it is not like they materialize right where they are. Instead, it is like there is an invisible dealer at the table...No, not like that. If there was an actual person the trajectory the cards would not be like that. Rather, it is like there is an invisible vacuum at the table.

I visualize that sort of household appliance. But if it was literally a vacuum, there would be more air movement, but instead only the cards are affected. So some kind of telekinesis?

Yes. I feel like I am finally paying the game the respect it deserves and thinking about it. A lot of the things in this game are very weird so I haven't felt like doing that. Like how is there air in this place? There are weird rules everywhere, and I'd rather not waste my brain cells on something that doesn't have a physical basis. I wouldn't be able to use it in the real world. But now I'll give it a good think. The game has upset me enough to warrant it. And besides, I have a lot more brain cells than I used to have.

(Geoffrey POV - Heaven's Key, House in the suburbs)

"Though it is policy, I question the …

---
## [TimCollins/free-programming-books](https://github.com/TimCollins/free-programming-books)@[97016edd67...](https://github.com/TimCollins/free-programming-books/commit/97016edd6791285128758dd91904b343d1f3b0fd)
#### Thursday 2022-09-08 11:58:45 by David Ordás

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
## [NetworkManager/NetworkManager-ci](https://github.com/NetworkManager/NetworkManager-ci)@[9ac2992392...](https://github.com/NetworkManager/NetworkManager-ci/commit/9ac29923926146ad061e066fb3d17b3f706acff7)
#### Thursday 2022-09-08 12:26:34 by Thomas Haller

prepare: drop "get_online_state" check

I proposed this before ([1]), but it was rejected back then. Here again.

When having a container, there is no eth0 or global connectivity managed
by NetworkManager. This check will then fail, unless we activate a suitable
profile in NetworkManager. Sure, maybe some tests require such an eth0 interface
too, and the test would still fail without it, however that is
probably something that should be fixed and not reject by "envsetup.sh".

This check really does not belong to "envsetup.sh". If you buy into the
notion that "envsetup.sh" has a defined purpose, then it's probably to
prepare the environment. Checking for connectivity via NetworkManager is
not part of that, in particular, when we will have environments where
this is not a given.

Each CI test needs to check itself that it's pre-conditions,
test-conditions and post-conditions are satisfied. But "get_online_state"
is not a condition that concerns all tests, and such checks don't belong
to "envsetup.sh" anyway.

Also, "prepare/envsetup.sh" wrote a state file to "/tmp/nmcli_general", which
is then printed by "run/runtest.sh". So part of the API of "envsetup.sh"
was to (maybe) generate such a file. That's really ugly, and alone for
that it has to die.

[1] https://gitlab.freedesktop.org/NetworkManager/NetworkManager-ci/-/merge_requests/1075#note_1421829

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[2395be24ab...](https://github.com/odoo-dev/odoo/commit/2395be24ab6cb99420f693d49c37c6f8c45d4a43)
#### Thursday 2022-09-08 12:48:49 by Xavier Morel

[IMP] *: owlify password meter and convert change password to real wizard

The changes in `auth_password_policy` are largely the owlification of
the password meter widget:

- modernize the password policy module and convert it to an
  odoo-module (note: now exports a pseudo-abstract class which is
  really a policy, for the sake of somewhat sensibly typing
  `recommendations`)
- replace the implementation of the Meter and PasswordField widgets by
  owl versions

The changes to web and base stem from taking a look at converting the
ChangePassword wizard, and finding that it would be a pain in the ass
but also... unnecessary? It seems to have been done as a wizard
completely in javascript despite being backend-only for legacy
reasons: apparently one of the very old web clients (v5 or v6
probably) implemented it as a "native action" which was directly part
of the client's UI, and so it had to be implemented entirely in the
client.

Over time it was moved back into the regular UI (and moved around
quite a bit), hooked as a client action to maintain access to the
existing UI / dialog.

But since it's been an action opened via a button for years it can
just... be a normal wizard, with password fields, which
auth_password_policy can then set the widget of.

So did that:

- removed the old unnecessary JS, and its dedicated endpoint (which is
  *not* used by portal, portal has its own endpoint)
- used check_identity for the "old password check"
- split out `change_password` with an internal bit so we can have a
  safer (and logged) "set user password" without needing to provide
  the old password, which is now used for the bulk password change
  wizard as well
- added a small wizard which just takes a new password (and
  confirmation), for safety a given change password wizard is only
  accessible to their creator (also the wizard is restricted to
  employees though technically it would probably be fine for portal
  users as well)

Rather than extensive messy rewrite / monkeypatching (the original
wizard was 57 LOC, though also 22 LOC of template, the auth_policy
hooking / patching was 33, plus 8 lines of CSS),
`auth_password_policy` just sets the widget of the `new_password`
field in the new wizard, much as it did the bulk wizard.

Also improve the "hide meter if field is empty" feature by leveraging
`:placeholder-shown`. This requires setting a placeholder, and while
empty works fine in firefox, it doesn't work in chrome. So the
placeholder needs to be a single space. Still, seems better than
updating a fake attribute or manipulating a class for the sake of
trivial styling.

Notes on unlink + transient vacuum

Although the wizard object is only created when actually calling
`change_password`, and is deleted on success, it is possible for the
user to get an error and fail to continue (it should be unlikely
without overrides since the passwords are checked while creating /
saving but...).

While in that case the `new_password` in the database is not the
user's own, it could be their *future* password, or give evidence as
to their password-creation scheme, or some other signal useful to
attack that front of the user's life and behavior. As such, quickly
removing leftovers from the database (by setting a very low transient
lifetime) seems like a good idea.

This is compounded by the `check_identity` having a grace period of 10
minutes. 0.1 is 6 minutes, but because the cron runs every 10 the user
effectively has 6~10 minutes between the moment they create an
incorrect / incomplete version of the wizard and the moment where it
is destroyed if they just leave it.

---
## [jwellan1/graspologic](https://github.com/jwellan1/graspologic)@[240b913560...](https://github.com/jwellan1/graspologic/commit/240b913560c6dc7437750fc6a519645453556b3c)
#### Thursday 2022-09-08 13:36:05 by Dwayne Pryce

THE GRAND RENAMING HAS BEGUN (#481)

* THE GRAND RENAMING HAS BEGUN but holy crap it still doesn't work because of some nbsphinx thing that I don't know how to even begin troubleshooting

* Update .github/PULL_REQUEST_TEMPLATE.md

I am the goo0dest typer

Co-authored-by: Benjamin Pedigo <benjamindpedigo@gmail.com>

* Update README.md

Co-authored-by: Benjamin Pedigo <benjamindpedigo@gmail.com>

* Make the build status badge less obnoxious

* Made a sentence actually make sense

* Ah the last merge from dev must have overwritten some of the changes I made.  This should be fixed now.

* Found another instance of graspy in the issue template

* Some last second changes, including a fix to the utils init file because the __all__ value was being populated by identifier names not string representations of those identifier names

* I approve of black hating the single quotes for a string because I also hate it but it's still pythonic even if I wish it weren't so

Co-authored-by: Benjamin Pedigo <benjamindpedigo@gmail.com>

---
## [jwellan1/graspologic](https://github.com/jwellan1/graspologic)@[020e451ee6...](https://github.com/jwellan1/graspologic/commit/020e451ee61c83fbb3effc67a6a30781dddff900)
#### Thursday 2022-09-08 13:36:05 by Dwayne Pryce

Suitably dynamic versioning (#467)

* Suitably dynamic versioning

The following versioning code bypasses a few problems with python module versions.  The following scenarios are plausible:
- A user clones `graspologic` and runs `pip install -r requirements.txt` then executes `python` in the project directory, accessing the graspologic library by python's local folder structure.
- A users clones `graspologic` and runs `python setup.py install` in the environment of their choice, accessing the graspologic library either by the local folder structure or the .egg in their site-packages, depending on their current working directory.
- A user clones no repository and wants to install the library solely via `pip` via the `pip install ...` command, which has 2 wings to consider:
  - The user wishes to try out the latest prerelease, which is going to be published with a X.Y.ZdevYYYYMMDDBUILDNUMBER style version and can be installed via `pip install graspologic --pre`
  - The user wishes to try out the latest release, which will be published as `X.Y.Z`.

This PR supports those 4 cases (notably, it does not support `pip install .` from the root project directory, which does some super weird stuff and I gave up on trying to solve it a long time ago)

The concept is this: the actual version upon a **build action**, which can be undertaken by:
- CI building a snapshot build
- CI building a release build
- Local user building a local build

These states all require the same thing: a materialized version in a file.  This version should be created at the time of this build action.

In the case of CI, we can populate the file in our CI build process and move on.  It's the case of not being in CI where we need to consider what to do next, which leaves Local user building a local build (and local user using the filesystem as the library).

In these cases, the solution is the following: if we have a populated version.txt file, we use it. If we do not, we materialize a new version based on the `__semver` in version.py and the current time in YYYYMMDDHHmmSS format. This means that if you are running on the filesystem, and you say `import graspy; print(graspy.__version__);`, it will actually tell you the version is `0.1.0dev20200926120000` as an example.  However, when you close the interpreter and do it again, it will tell you that the version is `0.1.0dev20200926120500` - because it will create a version for you at the time of import.

However, if you were to run `python setup.py install`, the setup.py file actually takes it on itself to either get a version number or use the materialized version described above, then to write it to version.txt.  Which means that installing the graspologic library from setuptools will actually lock in the version number in perpetuity.

Gotchas
- version.txt must always be empty in the source tree
- `pip install .` does some weird thing where it registers an entry in site-packages that is like a symlink to the local filesystem anyway so it doesn't actually make an egg which means you get a new version each time and I gave up caring at this point since we got the three primary use cases: developers, users of pre-releases, and users of releases all covered. Users who install by cloning and running pip install are just going to get a weird behavior that probably isn't that important to track down, and regardless they'll get a clear `X.Y.Zdev<timestamp>` in their `graspologic.__version__` which is enough for us to go on if there are any issues raised.

* My testing resulted in filling this file and committing it, like I said not to do

* Updated conf.py for sphinx to be able to find a version it likes.  Or kinda likes.  Maybe likes?

* Forgot I had to add the recursive-include for the version file.

* Making black happy

---
## [Quacken8/C-_MFF_study](https://github.com/Quacken8/C-_MFF_study)@[a92b2c5704...](https://github.com/Quacken8/C-_MFF_study/commit/a92b2c57046f718fa5c01227047c4a869521cf4b)
#### Thursday 2022-09-08 13:52:06 by Ondra Janoška

ok immediatelly i got slapped with 'thats a shit, slow implementation' during the lecture. Kinda funny given how im not even enrolled in that class. Optimized

---
## [facebook/react](https://github.com/facebook/react)@[b6978bc38f...](https://github.com/facebook/react/commit/b6978bc38f6788c7e73982b9fd2771aabdf36f15)
#### Thursday 2022-09-08 14:29:07 by Andrew Clark

experimental_use(promise) (#25084)

* Internal `act`: Unwrapping resolved promises

This update our internal implementation of `act` to support React's new
behavior for unwrapping promises. Like we did with Scheduler, when 
something suspends, it will yield to the main thread so the microtasks
can run, then continue in a new task.

I need to implement the same behavior in the public version of `act`,
but there are some additional considerations so I'll do that in a
separate commit.

* Move throwException to after work loop resumes

throwException is the function that finds the nearest boundary and
schedules it for a second render pass. We should only call it right 
before we unwind the stack — not if we receive an immediate ping and
render the fiber again.

This was an oversight in 8ef3a7c that I didn't notice because it happens
to mostly work, anyway. What made me notice the mistake is that
throwException also marks the entire render phase as suspended
(RootDidSuspend or RootDidSuspendWithDelay), which is only supposed to
be happen if we show a fallback. One consequence was that, in the 
RootDidSuspendWithDelay case, the entire commit phase was blocked,
because that's the exit status we use to block a bad fallback
from appearing.

* Use expando to check whether promise has resolved

Add a `status` expando to a thrown thenable to track when its value has
resolved.

In a later step, we'll also use `value` and `reason` expandos to track
the resolved value.

This is not part of the official JavaScript spec — think of
it as an extension of the Promise API, or a custom interface that is a
superset of Thenable. However, it's inspired by the terminology used
by `Promise.allSettled`.

The intent is that this will be a public API — Suspense implementations
can set these expandos to allow React to unwrap the value synchronously
without waiting a microtask.

* Scaffolding for `experimental_use` hook

Sets up a new experimental hook behind a feature flag, but does not
implement it yet.

* use(promise)

Adds experimental support to Fiber for unwrapping the value of a promise
inside a component. It is not yet implemented for Server Components, 
but that is planned.

If promise has already resolved, the value can be unwrapped
"immediately" without showing a fallback. The trick we use to implement
this is to yield to the main thread (literally suspending the work
loop), wait for the microtask queue to drain, then check if the promise
resolved in the meantime. If so, we can resume the last attempted fiber
without unwinding the stack. This functionality was implemented in 
previous commits.

Another feature is that the promises do not need to be cached between
attempts. Because we assume idempotent execution of components, React
will track the promises that were used during the previous attempt and
reuse the result. You shouldn't rely on this property, but during
initial render it mostly just works. Updates are trickier, though,
because if you used an uncached promise, we have no way of knowing 
whether the underlying data has changed, so we have to unwrap the
promise every time. It will still work, but it's inefficient and can
lead to unnecessary fallbacks if it happens during a discrete update.

When we implement this for Server Components, this will be less of an
issue because there are no updates in that environment. However, it's
still better for performance to cache data requests, so the same
principles largely apply.

The intention is that this will eventually be the only supported way to
suspend on arbitrary promises. Throwing a promise directly will
be deprecated.

---
## [embeddedTS/linux-lts](https://github.com/embeddedTS/linux-lts)@[adee8f3082...](https://github.com/embeddedTS/linux-lts/commit/adee8f3082b01e5dab620d651e3ec75f57c0c855)
#### Thursday 2022-09-08 17:13:23 by Peter Zijlstra

x86/nospec: Unwreck the RSB stuffing

commit 4e3aa9238277597c6c7624f302d81a7b568b6f2d upstream.

Commit 2b1299322016 ("x86/speculation: Add RSB VM Exit protections")
made a right mess of the RSB stuffing, rewrite the whole thing to not
suck.

Thanks to Andrew for the enlightening comment about Post-Barrier RSB
things so we can make this code less magical.

Cc: stable@vger.kernel.org
Signed-off-by: Peter Zijlstra (Intel) <peterz@infradead.org>
Link: https://lkml.kernel.org/r/YvuNdDWoUZSBjYcm@worktop.programming.kicks-ass.net
[bwh: Backported to 5.10: adjust context]
Signed-off-by: Ben Hutchings <benh@debian.org>
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[b2479b46d2...](https://github.com/treckstar/yolo-octo-hipster/commit/b2479b46d288802983a54430ac73caefed6b324f)
#### Thursday 2022-09-08 17:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[f0ceecff46...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/f0ceecff46f9b600dfe8e60199f354f61d63a0a4)
#### Thursday 2022-09-08 17:25:14 by SkyratBot

[MIRROR] Refactors SM gas behavior to be datum based instead of list based + powerloss co2 buff [MDB IGNORE] (#16000)

* Refactors SM gas behavior to be datum based instead of list based + powerloss co2 buff (#69158)

About The Pull Request

Title!
The CO2 thing is there because it makes my job much easier. Can probably find a way to make it move slowly if a maint insist on it. Prefer not to though.

Drafting because I want to make a second PR that have more sweeping changes (clean vars up, make a simpler formula for damage and heat production, delete underused behaviors, etc). Would honestly prefer if both this and that gets merged at the same time but I'm separating it out since it might be rejected. Or maybe ill combine it here we'll see.
Ignore that, looks like i can keep this one absolutely atomic.
Why It's Good For The Game

Had a lot of trouble when trying to document the SM gas interactions into the wiki, the interactions are all scattered and tracking down everything a gas does is extremely annoying. Hopefully this fixes that.
Changelog

cl
balance: CO2 powerloss inhibition now works immediately based on gas composition instead of slowly ramping up.
refactor: refactored how the SM fetches it's gas info and data. No changes expected except for the co2 thing.
/cl

* Refactors SM gas behavior to be datum based instead of list based + powerloss co2 buff

Co-authored-by: vincentiusvin <54709710+vincentiusvin@users.noreply.github.com>

---
## [majestrate/loki-network](https://github.com/majestrate/loki-network)@[e981c9f899...](https://github.com/majestrate/loki-network/commit/e981c9f89983a12cc75d691fc439366703d5bfff)
#### Thursday 2022-09-08 18:25:24 by Jeff

tweaks for wine and yarn for gui

* allow specifying a custom yarn binary for building the gui using -DYARN= cmake option
* unset DISPLAY when calling wine because i hate popups
* do not rebuild gui when building for windows
* by setting the magical undocumented env var USE_SYSTEM_7ZA to 'true' we can have the pile of npm bullshit code use our system's local 7z binary instead of the probably not backdoored binary from npm, yes for real. i hate nodejs so god damn much you have no fucking idea
* allow providing a custom gui from a zip file via -DGUI_ZIP_FILE cmake option

---
## [dmychel/landing-page-project](https://github.com/dmychel/landing-page-project)@[75cf6576b3...](https://github.com/dmychel/landing-page-project/commit/75cf6576b317b1b140025825c3b4f15c4905167f)
#### Thursday 2022-09-08 18:35:20 by odin

UPDATE
I have finished this landing project. I added the last section of the page and finished the CSS requirements Odin gave me.

For this commit I will keep the borders visible so you can see my work and how I managed to align everything, the next commit everything will remain the same but the borders will no longer be visible. To be honest I struggled a bit with this project, it forced me to really understand the box method and how to use flexbox to your advantage. As I was building the page it was getting more and more difficult to keep track of all the <divs> so I decided to build the page in portions: Header, Top, Middle, Bottom, and Call to action. Odin recommends completely building out the HTML first, but that just lead me to confusion and requiring me to scrap everything and do it again. Almost all of the elements have flex so when you change the window size everything should move together, the issue arises when you make the window too small. The format begins to break down and things can look a little wonky. I believe min-width min-height can help prevent this, but I will need to look more into it. I also had trouble making he .call-to-action background color rounded. I tried to use the border-radius but it was not acting as it did with the buttons and images, this is something I will also look at. I feel as I am done for now, but when I learn a bit more, I plan on coming back to this project to make it cleaner and more appealing.

thanks for reading.

---
## [ToppleKek/banter2](https://github.com/ToppleKek/banter2)@[4afd07f428...](https://github.com/ToppleKek/banter2/commit/4afd07f428de4e2597a7cb563ab57b93efd90e14)
#### Thursday 2022-09-08 19:13:28 by ToppleKek

Utils: Fix permission checking in d.js v14

Because they keep changing the fucking API every god
damn version.

---
## [ssbr/rust](https://github.com/ssbr/rust)@[0ffaa59a06...](https://github.com/ssbr/rust/commit/0ffaa59a062729c97b9265ed7987e3dfc2ad2dda)
#### Thursday 2022-09-08 19:40:47 by Devin Jeanpierre

Draft change: add the `#[manually_drop]` attribute.

This attribute is equivalent to `#[lang = "manually_drop"]`, and the behavior of both are
extended to allow the type to define `Drop`, in which case, that will still be run. Only
the field drop glue is suppressed.

This PR should essentially fully implement #100344.

Some additional notes:

### The meaning of `#[manually_drop]`

In this PR, `#[manually_drop]` means "do not destroy the fields automatically during
destruction". That is all.

`ManuallyDrop`, is (or could be) "just"
`#[manually_drop] struct ManuallyDrop<T>(T);`.

The intent is, per the MCP, to allow customization of the drop order, without making the
interface for initializing or accessing the fields of the struct clumsier than a normal
Rust type. It also -- and people did seem excited about this part -- lifts `ManuallyDrop`
from being a special language supported feature to just another user of
`#[manually_drop]`.

### Insignificant Drop

There is the question of how this interacts with "insignificant" drop. I am not sure,
exactly, since the comments are nearly nonexistent, but insignificant drop appears to just
be a static analysis tool, and not something that changes behavior. Since it's unlikely to
be used for `#[manually_drop]` types, I don't think it matters a whole lot. And where a
destructor is defined, it would seem to make sense for `#[manually_drop]` types to match
exactly the behavior of `union`, since they both have the shared property that field drop
glue is suppressed.

### Users that expect `adt.is_manually_drop()` <-> "is `std::mem::ManuallyDrop`"

I looked for all locations that queried for `is_manually_drop` in any form, and found two
difficult cases which are hardcoded for `ManuallyDrop` in particular.

The first is a clippy lint for redundant clones. I don't understand why it special-cases
`ManuallyDrop`, and it's almost certainly wrong for it to special-case `#[manually_drop]`
types in general. However, without understanding the original rationale, I have trouble
figuring the right fix. Perhaps it should simply be deleted altogether.

The second is unions -- specifically, the logic for disabling `DerefMut`.
`my_union.x.y = z` will automatically dereference `my_union.x` if it implements
`DerefMut`, unless it is `ManuallyDrop`, in which case it will not. This is because
`ManuallyDrop` is a pointer back to its content, and so this will automatically call `drop`
on a probably uninitialized field, and is unsafe.

This is true of `ManuallyDrop`, but not necessarily any other `#[manually_drop]` type.
I believe the correct fix would, instead, be a way to mark and detect types which are
a smart pointer whose pointee is within `self`. See, for example, this playground link:

https://play.rust-lang.org/?version=stable&mode=debug&edition=2021&gist=76fb22a6214ce453538fc18ec35a839d

But that needs to wait for a separate RFC. For now, we apply exactly the same restriction
for `ManuallyDrop` and for any other `#[manually_drop]` type, even though it may be
confusing.

## To-do in future PRs

1.  Delete `#[lang = "manually_drop"]`. I'm not sure if anything special needs to be done
    here other than replacing it with `#[manually_drop]` -- is there a compatibility
    guarantee that must be upheld?
2.  (Optional) Fix the redundant clone check to correctly handle `#[manually_drop]`
    structs that aren't `ManuallyDrop`.
3.  When there is more experience with the feature (e.g. in Crubit) create a full RFC
    based on the MCP, and go through the remainder of the stabilization process.

---
## [nspcc-dev/neo-go](https://github.com/nspcc-dev/neo-go)@[d3429201e4...](https://github.com/nspcc-dev/neo-go/commit/d3429201e47b9bdabc933b469ced33bbab814c6d)
#### Thursday 2022-09-08 19:41:40 by Roman Khimov

Makefile: complicate version detection script

We've declared that we are using semantic versioning. We also want to use `git
describe` to make version strings for us because it's very convenient for
development builds (tagged versions are way simpler). The problem is that the
default `git describe` behavior is not semver compliant. If the most recent
tag is v0.99.2 then it'll generate something like '0.99.2-131-g8dc5b385',
which according to semver is a development version _before_ 0.99.2. While it's
obviously a version _after_ 0.99.2.

That's the one and only reason we have vX.Y.Z-pre tags in our repo. We set
them right after the release according to the release process and that gives
us some '0.99.3-pre-131-g8dc5b385' versions we're all used to. But these tags
are ugly as hell and they clutter up our repo over time.

So there is this idea that we can do patch version increment dynamically.
Making '0.99.2-131-g8dc5b385' be '0.99.3-pre-131-g8dc5b385' without any *-pre
tags. This patch implements this. It's ugly as hell as well, but at least
that's an ugliness somewhere inside our Makefile and not directly visible in
our tags. If we're to do this we can then greatly simplify our release process
(and even allow for CHANGELOG patches to be merged normally).

I know this can be done with awk in somewhat easier way, but no, I'm not into
awk, sorry.

---
## [ssbr/rust](https://github.com/ssbr/rust)@[604d8646a2...](https://github.com/ssbr/rust/commit/604d8646a2eecc8017fb765b57c966270778aba7)
#### Thursday 2022-09-08 19:45:10 by Devin Jeanpierre

Add the `#[manually_drop]` attribute.

This attribute is equivalent to `#[lang = "manually_drop"]`, and the behavior of both are
extended to allow the type to define `Drop`, in which case, that will still be run. Only
the field drop glue is suppressed.

This PR should essentially fully implement #100344.

Some additional notes:

### The meaning of `#[manually_drop]`

In this PR, `#[manually_drop]` means "do not destroy the fields automatically during
destruction". That is all.

`ManuallyDrop`, is (or could be) "just"
`#[manually_drop] struct ManuallyDrop<T>(T);`.

The intent is, per the MCP, to allow customization of the drop order, without making the
interface for initializing or accessing the fields of the struct clumsier than a normal
Rust type. It also -- and people did seem excited about this part -- lifts `ManuallyDrop`
from being a special language supported feature to just another user of
`#[manually_drop]`.

### Insignificant Drop

There is the question of how this interacts with "insignificant" drop. I had trouble
understanding the comments, but insignificant drop appears to just be a static analysis
tool, and not something that changes behavior. (For example, it's used to detect if a
language change will reorder drops in a meaningful way -- meaning, reorder the
significant drops, not the insignificant ones.) Since it's unlikely to be used for
`#[manually_drop]` types, I don't think it matters a whole lot. And where a destructor
is defined, it would seem to make sense for `#[manually_drop]` types to match exactly
the behavior of `union`, since they both have the shared property that field drop
glue is suppressed.

### Users that expect `adt.is_manually_drop()` <-> "is `std::mem::ManuallyDrop`"

I looked for all locations that queried for `is_manually_drop` in any form, and found two
difficult cases which are hardcoded for `ManuallyDrop` in particular.

The first is a clippy lint for redundant clones. I don't understand why it special-cases
`ManuallyDrop`, and it's almost certainly wrong for it to special-case `#[manually_drop]`
types in general. However, without understanding the original rationale, I have trouble
figuring the right fix. Perhaps it should simply be deleted altogether.

The second is unions -- specifically, the logic for disabling `DerefMut`.
`my_union.x.y = z` will automatically dereference `my_union.x` if it implements
`DerefMut`, unless it is `ManuallyDrop`, in which case it will not. This is because
`ManuallyDrop` is a pointer back to its content, and so this will automatically call `drop`
on a probably uninitialized field, and is unsafe.

This is true of `ManuallyDrop`, but not necessarily any other `#[manually_drop]` type.
I believe the correct fix would, instead, be a way to mark and detect types which are
a smart pointer whose pointee is within `self`. See, for example, this playground link:

https://play.rust-lang.org/?version=stable&mode=debug&edition=2021&gist=76fb22a6214ce453538fc18ec35a839d

But that needs to wait for a separate RFC. For now, we apply exactly the same restriction
for `ManuallyDrop` and for any other `#[manually_drop]` type, even though it may be
confusing.

## To-do in future PRs

1.  Delete `#[lang = "manually_drop"]`. I'm not sure if anything special needs to be done
    here other than replacing it with `#[manually_drop]` -- is there a compatibility
    guarantee that must be upheld?
2.  (Optional) Fix the redundant clone check to correctly handle `#[manually_drop]`
    structs that aren't `ManuallyDrop`.
3.  When there is more experience with the feature (e.g. in Crubit) create a full RFC
    based on the MCP, and go through the remainder of the stabilization process.

---
## [Rishabh122333/DATA-STRUCTURES-ALGORITHMS](https://github.com/Rishabh122333/DATA-STRUCTURES-ALGORITHMS)@[411e001636...](https://github.com/Rishabh122333/DATA-STRUCTURES-ALGORITHMS/commit/411e001636c16183d7e201965d1de500c820b719)
#### Thursday 2022-09-08 20:46:24 by Rishabh122333

Array Question

Deepak has a limited amount of money that he can spend on his girlfriend. So he decides to buy two roses for her. Since roses are of varying sizes, their prices are different. Deepak wishes to completely spend that fixed amount of money on buying roses for her.
As he wishes to spend all the money, he should choose a pair of roses whose prices when summed up are equal to the money that he has.
Help Deepak choose such a pair of roses for his girlfriend.

NOTE: If there are multiple solutions print the solution that minimizes the difference between the prices i and j. After each test case, you must print a blank line.

Input Format
The first line indicates the number of test cases T.
Then, in the next line, the number of available roses, N is given.
The next line will have N integers, representing the price of each rose, a rose that costs less than 1000001.
Then there is another line with an integer M, representing how much money Deepak has.
There is a blank line after each test case.

Constraints
1≤ T ≤100
2 ≤ N ≤ 10000
Price[i]<1000001

Output Format
For each test case, you must print the message: ‘Deepak should buy roses whose prices are i and j.’, where i and j are the prices of the roses whose sum is equal do M and i ≤ j. You can consider that it is always possible to find a solution. If there are multiple solutions print the solution that minimizes the difference between the prices i and j.

Sample Input
2
2
40 40
80

5
10 2 6 8 4
10
Sample Output
Deepak should buy roses whose prices are 40 and 40.
Deepak should buy roses whose prices are 4 and 6.

---
## [Superlagg/coyote-bayou](https://github.com/Superlagg/coyote-bayou)@[69a80c2479...](https://github.com/Superlagg/coyote-bayou/commit/69a80c2479ea4e76b5b1c96883b9e903cdfbfe50)
#### Thursday 2022-09-08 22:40:41 by Tk420634

Fixes stack.dm runtime

fuck you, stack.dm runtime.  All my homies hate runtimes.  The commented out code can be revisited later, but for now this solves that nasty little bugger real good.

---
## [willior/Action_RPG_1](https://github.com/willior/Action_RPG_1)@[badc878840...](https://github.com/willior/Action_RPG_1/commit/badc878840102aa0105d38876cc0add9c96ed0b5)
#### Thursday 2022-09-08 22:45:21 by willior

hurtbox_entered() refactor... complete?

incoming giant commit

knockback should be calculated as follows:

if the attack has a knockback_vector != null, get the average between knockback_vector and the damage_source.global_position.direction_to(body.global_position); then multiply it by knockback_modifier & some value (16 if bounce, 80 otherwise).
if the attack does NOT have a knockback_vector value set (ie., it's null), use damage_source.global_position.direction_to(body.global_position) ONLY; then multiply it by knockback_modifier & some value (16 if bounce, 96 otherwise).
then, if it's a crit, multiply knockback by 1.2.
then, if it's a killing blow, multiply knockback by 1.2 again.

... so that's done, and it's working. a few other fixes:

moving crit_rate and accuracy variables from enemies' hitboxes to enemies' stats. this is because when we grab those values for the Player, we grab them from PlayerStats; it should be the same for enemies.
to do that, we've given Hitbox (enemies' hitbox) a reference to its body, which is its grandparent, on _ready(): body.get_parent().get_parent(). this allows us to grab crit_rate and accuracy stats in player hit calculation:
Global.hit_calculation(area.body.stats.accuracy, stats.evasion)
Global.crit_calculation(area.body.stats.crit_rate)
enemies' hitbox has also been given a "sharpness" variable which defaults to 0. hurtbox_entered() checks if an attack should "bounce" by comparing damage_source.sharpness against the target body's hardness; if it's less, bounce = true. if sharpness is 0, it will bounce against armor of hardness 1 or higher.
i realize now that this breaks some behaviour. right now, the only enemy that has more than one "attack" is the Green_Slime, and the way his attacks are set up are kind of weird. he has 2 separate Hitboxes, and depending on the attack chosen, its respective hitbox is activated.
the issue is that one of the two attacks' had a crit_rate of 100. this value used to live in the Hitbox, where it wouldn't change, so it was easy to access. now, "crit_rate" is a "stat" that lives in EnemyStats. there are a multitude of options here:
one would be to change stats.crit_rate dynamically depending on the attack chosen by the RNG. kind of risky to do that, in my opinion... but we do it with PlayerStats, so i suppose we can start doing it with EnemyStats. things just get messier, though.
another would be to add a "crit_rate_bonus" to the Hitbox. then, to get crit_rate, we do stats.crit_rate + hitbox.crit_rate_bonus.
or, a combination of the two above ideas: add a crit_rate_bonus stat, and change THAT value dynamically. crit_rate = stats.crit_rate + stats.crit_rate_bonus. overkill?
it's not obvious currently what the correct, ideal solution is.
in the future, enemies - presumably bosses & the like - will have a multitude of attacks, not just 1 or 2. it's at that point i'll have to decide if having multiple hitboxes per enemy is worth it or not. the Player has only ONE hitbox, which is modified dynamically by functions. i suppose it's possible to configure enemies' attacks to behave similarly, and at that point just change the values around in stats.
... and it dawns on me now that enemy accuracy should actually remain in the enemy Hitbox script... what i'll do, however, is i'll change it to utilize signals like PlayerStats and AttackHitbox do.
... which is more troublesome than i'd thought, because unlike PlayerStats, each of which is a Singleton node accessible from anywhere in the program, EnemyStats are declared on EnemyClass._ready() - so signals can't be connected from Hitbox's _ready().
so the signals have to be connected on EnemyClass._ready():

	stats.connect("accuracy_changed", hitbox, "set_accuracy")
	stats.connect("crit_rate_changed", hitbox, "set_crit_rate")

... and it's working. it's messy. when the Player gets hit, we get accuracy and crit_rate from area. when an Enemy gets hit, we get accuracy from damage_source but crit_rate from body.stats. this is because the Player's hitbox does not have a crit_rate variable; their crit_rate is stored in PlayerStats. perhaps we'll give AttackHitbox a crit_rate variable, and set it via signal like accuracy, just for consistency's sake.
and it's done. we needed to add all hitboxes to a "hitboxes" array, which has now been declared on EnemyClass. on _ready(), Hitbox appends itself to the "hitboxes" array. then, we iterate through hitboxes, and connects the stats signals "accuracy_changed" & "crit_rate_changed". everything seems to be working properly, and this makes setting accuracy/crit_rate on a per attack basis very simple. simply write stats.crit_rate = x in the attack's function, and it just works.
brain turning to mush, commit too huge. but everything's working. properly, too, i think.

---

