## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-09-06](docs/good-messages/2022/2022-09-06.md)


2,263,202 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,263,202 were push events containing 3,416,062 commit messages that amount to 252,229,918 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 38 messages:


## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[3b2cf65d59...](https://github.com/tgstation/tgstation/commit/3b2cf65d59aa5ae22876b0ebabecb564ccb912d0)
#### Tuesday 2022-09-06 00:02:29 by san7890

Rocking The Boat, er, Map Vote (#69561)

* Rocking The Boat, er, Map Vote

Hey there,

A while ago, I spooke (typo intentional) to some other people. One frustration I heard was the fact that people would sometimes sneak through map votes during the very start of a shift, during a high-paced portion, or just as a meme. People in OOC would then flood the vote, putting in any given station. However, if a vote happens 10 minutes in- and the round goes for 70 minutes and not many of the original players are around, then it's not particularly fair to those who have to play next shift on a map they bemoan.

So, we can rock the vote! If a player isn't particularly chuffed with the hand they are given, they can poll the players to see if they want to change the map as well. If rocking the vote goes through, huzzah, you get the ability to vote for the map again. If it doesn't go through: tough luck. You can rock the vote one time per shift by default, and server operators can change the amount of times you can call to rock the map vote at their discretion. Calling to rock the vote either successfully or non-successfully counts as a "call", and when that limit is exceeded: no more calls.

Does this mean that we will only rotate between two maps because pissants will keep rocking the vote until they get what they like? Maybe? I still see people bemoan getting Tram or shit the bed over IceBox, but I think enough people get sick of bread-on-butter to take the server where it need to go. If operators don't really like seeing only two maps play, they can always adjust the config to ensure it doesn't happen.

* makes the grammar grammar

it would be "Rock the Vote vote" otherwise

---
## [hexagon-geo-surv/linux-stable](https://github.com/hexagon-geo-surv/linux-stable)@[adee8f3082...](https://github.com/hexagon-geo-surv/linux-stable/commit/adee8f3082b01e5dab620d651e3ec75f57c0c855)
#### Tuesday 2022-09-06 00:22:04 by Peter Zijlstra

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
## [RichGibson/hellodrinkbot](https://github.com/RichGibson/hellodrinkbot)@[ce50defbd8...](https://github.com/RichGibson/hellodrinkbot/commit/ce50defbd8cd12e62534be0f5197000095c135b6)
#### Tuesday 2022-09-06 01:44:12 by Rich Gibson

We have a more or less functional Bender: Martini or fuck you. With thanks to Erin.

---
## [gustavwilliam/nollbricka](https://github.com/gustavwilliam/nollbricka)@[a467689975...](https://github.com/gustavwilliam/nollbricka/commit/a4676899753da8de01e4205ed4fc486bf861f5e6)
#### Tuesday 2022-09-06 01:47:13 by Gustav Odinger

Add basic structure of the project

The code is *wonerful* and *clean* and *well-written*. Truly
astonishing, if I may say so myself. Pure HTML+CSS+JS. Always a
wonderful experience for the ideomatician with a goal. That does sound
almost like magician whose big secret is that he follows the ideomatic
ways of doing things. Is that what he is? I do not yet know. However, we
shall fight to find out the truth of the matter! We shall fight day and
night, in rain and sunshine, in good and in bad. We shall fight until
the day that I shall cease to write wonderful commit messages like this.

---
## [Ebin-Halcyon/Skyrat-tg](https://github.com/Ebin-Halcyon/Skyrat-tg)@[e1839f0e37...](https://github.com/Ebin-Halcyon/Skyrat-tg/commit/e1839f0e375a2169c8d80d942376dddb8be1958d)
#### Tuesday 2022-09-06 02:08:22 by SkyratBot

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
## [RigoLigoRLC/reactos](https://github.com/RigoLigoRLC/reactos)@[4471ee4dfa...](https://github.com/RigoLigoRLC/reactos/commit/4471ee4dfaddb2440601fd61c01542b586b7c2d0)
#### Tuesday 2022-09-06 03:08:38 by George Bișoc

[NTOS:SE] Properly handle dynamic counters in token

On current master, ReactOS faces these problems:

- ObCreateObject charges both paged and non paged pool a size of TOKEN structure, not the actual dynamic contents of WHAT IS inside a token. For paged pool charge the size is that of the dynamic area (primary group + default DACL if any). This is basically what DynamicCharged is for.
For the non paged pool charge, the actual charge is that of TOKEN structure upon creation. On duplication and filtering however, the paged pool charge size is that of the inherited dynamic charged space from an existing token whereas the non paged pool size is that of the calculated token body
length for the new duplicated/filtered token. On current master, we're literally cheating the kernel by charging the wrong amount of quota not taking into account the dynamic contents which they come from UM.

- Both DynamicCharged and DynamicAvailable are not fully handled (DynamicAvailable is pretty much poorly handled with some cases still to be taking into account). DynamicCharged is barely handled, like at all.

- As a result of these two points above, NtSetInformationToken doesn't check when the caller wants to set up a new default token DACL or primary group if the newly DACL or the said group exceeds the dynamic charged boundary. So what happens is that I'm going to act like a smug bastard fat politician and whack
the primary group and DACL of an token however I want to, because why in the hell not? In reality no, the kernel has to punish whoever attempts to do that, although we currently don't.

- The dynamic area (aka DynamicPart) only picks up the default DACL but not the primary group as well. Generally the dynamic part is composed of primary group and default DACL, if provided.

In addition to that, we aren't returning the dynamic charged and available area in token statistics. SepComputeAvailableDynamicSpace helper is here to accommodate that. Apparently Windows is calculating the dynamic available area rather than just querying the DynamicAvailable field directly from the token.
My theory regarding this is like the following: on Windows both TokenDefaultDacl and TokenPrimaryGroup classes are barely used by the system components during startup (LSASS provides both a DACL and primary group when calling NtCreateToken anyway). In fact DynamicAvailable is 0 during token creation, duplication and filtering when inspecting a token with WinDBG. So
if an application wants to query token statistics that application will face a dynamic available space of 0.

---
## [153974-HSI-OXLEY-BANKS-40ACT/Peeping-Toms-of-Zucker](https://github.com/153974-HSI-OXLEY-BANKS-40ACT/Peeping-Toms-of-Zucker)@[f844abb7e5...](https://github.com/153974-HSI-OXLEY-BANKS-40ACT/Peeping-Toms-of-Zucker/commit/f844abb7e572a89f85ae4f42f29a136d76e03d77)
#### Tuesday 2022-09-06 04:27:52 by 153974-HSI-OXLEY-BANKS-40ACT

My toilet was packed with shit i dunno why they wanted to smell that anyways.

Subject: USC TITLE 18.225, 18.215, 18.21, 18.4, 18.3, 18.2, combine
+ SECURITIES FRAUD,
+ VIOLATION OF CIVIL RIGHTS PROCEDURE,
+ DUCKING FELONIES FOR THE GREATER OF TWO YEARS.

KNOWN, AIDED, AND ABETTED BY ALL IN THE MATTER OF 153974/2020, SEE ALSO DOCKET 53 IF THERE'S ANY QUESTION.

THANK YOU. TWO DOWN 5 TO GO AT 117TH AND BROADWAY.

Under USC 18.225.each person:

'...imprisoned for a term of not less than 10 years and which may be life."

https://github.com/BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER/blob/BSCPGROUPHOLDINGSLLC-EMAIL-DOCKETS/ms-pwc-dicker


Those papers confer a violation of the Sarbanes-Oxley 2002 Rev.
-- questions?


https://github.com/BSCPGROUPHOLDINGSLLC/WILSON-ELSER-DICKER-LASKOWITZ-MOV/find/8209-filed

MAKESMALLBIGGER
^ 1 REFERENCE
https://github.com/BSCPGROUPHOLDINGSLLC/AIDED-LIKE-BERNIE/raw/main/2020_05_27%20-%20INDEX%20and%20PAPERS.pdf




On 8/17/2022 10:47 AM, Bo Dincer wrote:

Plus they think five o is soft? I don't think so...

---
## [SmileWideSDK/Gamejam-2022-Newbies](https://github.com/SmileWideSDK/Gamejam-2022-Newbies)@[7170161790...](https://github.com/SmileWideSDK/Gamejam-2022-Newbies/commit/71701617901100c2a1f4e67a2320b866710493a7)
#### Tuesday 2022-09-06 04:49:40 by lemonlatke

fucking shit game i fucking hate this fucking ggamea go kys

---
## [trym-b/WWU](https://github.com/trym-b/WWU)@[583af91417...](https://github.com/trym-b/WWU/commit/583af91417256e4fb7bace56712db18a7b1c1703)
#### Tuesday 2022-09-06 04:59:12 by Vawser

Magic

- Added magic schools to the magic system.
 - Each school has its own spells.
 - After learning to become a spellcaster, you can select which school your ruler will follow.
  - Which are available depends on the possibility your ruler would be exposed to it (e.g. Fel will only appear if you have a Fel province or a Fel natio has a +25 opinion of you)

- Magic schools:
 - Arcane
 - Holy
 - Chi
 - Voodoo
 - Nature
 - Necromancy
 - Shamanism
 - Fel
 - Draconic
 - Corruption (Old God)
 - Shadow
 - Runic (Vrykul)
 - Nightmare
 - Earth (Elemental)
 - Fire (Elemental)
 - Water (Elemental)
 - Wind (Elemental)

- Spells for the new schools are WIP

---
## [ARF-SS13/coyote-bayou](https://github.com/ARF-SS13/coyote-bayou)@[69a80c2479...](https://github.com/ARF-SS13/coyote-bayou/commit/69a80c2479ea4e76b5b1c96883b9e903cdfbfe50)
#### Tuesday 2022-09-06 05:04:47 by Tk420634

Fixes stack.dm runtime

fuck you, stack.dm runtime.  All my homies hate runtimes.  The commented out code can be revisited later, but for now this solves that nasty little bugger real good.

---
## [queercpu/script](https://github.com/queercpu/script)@[0f29db471e...](https://github.com/queercpu/script/commit/0f29db471ecdb4f88cda41d53deb01863e8ec6e6)
#### Tuesday 2022-09-06 05:43:09 by home.cpu

the workload today was all over the place. the answer to my paranoia around trees was all of them combined... the inspiration from the museum painting + the bush from shemune + the trees from d2.. all of them combined was the breakthrough tree design I was wanted to see.  Im feeling extremely confident about 3d suddenly, like a burst of inspiration and ability and feeling able to do it all... feeling again, this deep feeling in my soul that im a 3d artist to the core...i sometimes say im a writer to the core, i guess i shift around, something just speaks home about 3d..ofc and writing...ofc and music. i dont know what im rambling for. i transcribed a few pages into the script main. im thinking about starting my 3d phase and not finish the script so hardcore.  im thinking abt doing twigs first, and plan her carefully and make sketch concepts etc go all out to help the 3d easier...

---
## [NetworkManager/NetworkManager-ci](https://github.com/NetworkManager/NetworkManager-ci)@[1a368ac7eb...](https://github.com/NetworkManager/NetworkManager-ci/commit/1a368ac7ebe7d1e3d4896e1e935d62e9c5e836b4)
#### Tuesday 2022-09-06 07:46:17 by Thomas Haller

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
## [RajaKunalPandit1/CodeForces_Questions](https://github.com/RajaKunalPandit1/CodeForces_Questions)@[28d865dd34...](https://github.com/RajaKunalPandit1/CodeForces_Questions/commit/28d865dd34b0992e4ce5a995ebe65e10984c90a6)
#### Tuesday 2022-09-06 14:08:57 by Raja Kunal Pandit

Create 822A - I'm bored with life.cpp

Output Status : 

By Rajakunalpandit, contest: Codeforces Round #422 (Div. 2), problem: (A) I'm bored with life, Accepted


Holidays have finished. Thanks to the help of the hacker Leha, Noora managed to enter the university of her dreams which is located in a town Pavlopolis. It's well known that universities provide students with dormitory for the period of university studies. Consequently Noora had to leave Vičkopolis and move to Pavlopolis. Thus Leha was left completely alone in a quiet town Vičkopolis. He almost even fell into a depression from boredom!

Leha came up with a task for himself to relax a little. He chooses two integers A and B and then calculates the greatest common divisor of integers "A factorial" and "B factorial". Formally the hacker wants to find out GCD(A!, B!). It's well known that the factorial of an integer x is a product of all positive integers less than or equal to x. Thus x! = 1·2·3·...·(x - 1)·x. For example 4! = 1·2·3·4 = 24. Recall that GCD(x, y) is the largest positive integer q that divides (without a remainder) both x and y.

Leha has learned how to solve this task very effective. You are able to cope with it not worse, aren't you?

Input
The first and single line contains two integers A and B (1 ≤ A, B ≤ 109, min(A, B) ≤ 12).

Output
Print a single integer denoting the greatest common divisor of integers A! and B!.

Example
inputCopy
4 3
outputCopy
6
Note
Consider the sample.

4! = 1·2·3·4 = 24. 3! = 1·2·3 = 6. The greatest common divisor of integers 24 and 6 is exactly 6.

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[c8afdf8156...](https://github.com/treckstar/yolo-octo-hipster/commit/c8afdf81565cd3234f3026f92fbebbfaabfd1266)
#### Tuesday 2022-09-06 15:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[e69428e3f1...](https://github.com/pytorch/pytorch/commit/e69428e3f1ee10a06dfc48f25f3dc86659be7a7d)
#### Tuesday 2022-09-06 15:33:44 by Andrew Gu

Update base for Update on "[FSDP] Generalize prefetching; lower unshard/reshard to handle"


### Additional Constructor Changes
- `self.sharding_strategy`
    - If the world size is 1, I clamp the sharding strategy to `NO_SHARD`, regardless of the passed-in sharding strategy, since the behavior is fully equivalent. This absolves the need for `p._is_sharded or self.world_size == 1` checks in the core code. Once we fully shift the paradigm to using handles, this should result in a clear net positive. However, for now, we still have some places where we interface directly with the `FlatParameter`, in which case we have some temporary hacky code.
- `HandleConfig`
    - As a part of the new design abstraction, much logic is lowered to the `FlatParamHandle`. This requires the handle be aware of mixed precision, CPU offloading, sharding strategy, and the process group (for world size > 1). To be less error-prone, I re-defined the `dataclass`s and `enum`s for the handle. These can be removed and coalesced with the existing ones.
    - The drawback is that the `FlattenParamsWrapper` constructor now takes in the `HandleConfig` to forward it to the `FlatParamHandle` constructor. I tolerate this since we plan to retire the FPW. For now, the handle's process group attributes are set later when we call `handle.shard()`.
    - We will dive into this logic lowering later. For now, the idea is we need to pass some extra info to the handle, which must go through the FPW.
- `FullyShardedDataParallel._shard_parameters()` -> `FlatParamHandle.shard()`
- [Important] Generalizing attributes to remove the 1 `FullyShardedDataParallel` : 1 `FlatParameter` assumption
    - **Before:** `_fsdp_graph_order`, `_pre_backward_hook_full_params_prefetched`, `_forward_full_params_prefetched`, `reshard_after_forward` are with respect to 1 `FullyShardedDataParallel`
    - **After:** (1) We use `FlatParamHandle` in place of `FullyShardedDataParallel`. (2) The atomic unit for forward and pre-backward is a _group_ of handles involved in the same module's forward/pre-backward. This is represented as `Tuple[FlatParamHandle, ...]`. For now, this is **always a singleton tuple**, but this shift enables a module having multiple FSDP parameters (which we have use cases for).
- `_reset_lazy_init()` attributes
    - The prefetched flags are merged into `self._handles_prefetched`, which is directly defined in the constructor. `reshard_after_forward` is retired since it can be fully determined by other attributes (`_is_root` and `sharding_strategy`).

## FSDP Runtime: Unshard

The first step is to read the existing `_rebuild_full_params()`. A few notable observations:
- It returns `Tuple[Tensor, bool]`. The first element is the _padded unsharded flattened parameter_, and the second element is whether we can free it upon exiting `summon_full_params()`. This return value is **only used in `summon_full_params()`**.
- If parameter mixed precision is enabled and the `FlatParameter` is already unsharded, then the low precision shard (`_mp_shard`) is still re-allocated on GPU. (It is freed at the end of the method.)
- If CPU offloading is enabled and the `FlatParameter` is already unsharded, then there is a no-op `p.data = p.data.to(self.compute_device, non_blocking=True)`.
- Inside `summon_full_params()`, `mixed_precision_cast_ran` is always `False`. Therefore, the return value for the `not p._is_sharded and mixed_precision_cast_ran` branch is unused.
-`summon_full_params()` can only be called (before forward or after backward) or (between forward and backward). Given this, I cannot think of a case where we call `summon_full_params()`, the `FlatParameter` is already unsharded, but `reshard_after_forward` is `True`. The `FlatParameter` should be sharded (before forward or after backward), and the `FlatParameter` may only be unsharded (between forward and backward) if `reshard_after_forward` is `False`.
- If parameter mixed precision is enabled and the sharding strategy is a sharded one, then inside `summon_full_params()`, the `FlatParameter` is unsharded in full precision. This involves allocating a new padded unsharded flattened parameter on GPU in full precision since `_full_param_padded` is in the low precision.

Some comments:
- Ideally, we reduce the complexity of the core code path: i.e. unshard for forward and pre-backward. If the return value is only used for `summon_full_params()`, we should consider if we can compartmentalize that logic.
- The branching is complex, and some return values are never used, where this fact is not immediately obvious. We should see if we can reduce the branch complexity.

Disclaimer: The difference in attribute semantics between `NO_SHARD` and the sharded strategies makes it challenging to unify the cases. This PR does not attempt to address that since it requires more design thought. However, it does attempt to reduce the complexity for the sharded strategies.

### Unshard: Core Code Path
Let us trace through the new logical unshard.
1. `FullyShardedDataParallel._unshard(self, handles: List[FlatParamHandle], prepare_gradient: bool)`
    - This iterates over the handles and calls `handle.pre_unshard()`, `handle.unshard()`, and `handle.post_unshard(prepare_gradient)` in the all-gather stream.
2. `FlatParamHandle.needs_unshard(self)`
    - We take an aside to look at this key subroutine.
    - For `NO_SHARD`, this returns `False`.
    - For sharded strategies, this checks if the padded unsharded flattened parameter is allocated. The padded unsharded flattened parameter is the base tensor for the unpadded unsharded flattened parameter, which is a view into the padded one. Thus, the padded one's allocation fully determines if the `FlatParameter` is unsharded.
    - For sharded strategies, to accommodate the parameter mixed precision + `summon_full_params()` case, we introduce `_full_prec_full_param_padded`, which is the padded unsharded flattened parameter in full precision. The helper `_get_padded_unsharded_flat_param()` takes care of this casing and returns the padded unsharded flattened parameter. Instead of allocating a new tensor each time, we manually manage `_full_prec_full_param_padded`'s storage just like for `_full_param_padded`.
3. `FlatParamHandle.pre_unshard(self)`
    - For sharded strategies, the postcondition is that the handle's `FlatParameter` points to the tensor to all-gather. This should be on the communication device and in the desired precision. The allocation and usage of the low precision shard for parameter mixed precision and the CPU -> GPU copy for CPU offloading both classify naturally in the pre-unshard.
    - For sharded strategies, if the `FlatParameter` does not need to be unsharded, `pre_unshard()` is a no-op. This avoids unnecessarily allocating and freeing the low precision shard.
    - For `NO_SHARD`, we simply preserve the existing semantics.
4. `FlatParamHandle.unshard(self)`
    - If the handle was resharded without freeing the padded unsharded flattened parameter (e.g. `summon_full_params()` between forward and backward when `reshard_after_forward=False`), then the `FlatParameter` points to the sharded flattened parameter. We need to switch to using the unsharded parameter. This is a design choice. Alternatively, we may not switch to using the sharded flattened parameter in `reshard()` if we do not free the padded unsharded flattened parameter. However, the postcondition that the `FlatParameter` points to the sharded flattened parameter after `reshard()` is helpful logically, so I prefer this approach.
    - Otherwise, this allocates the padded unsharded flattened parameter, all-gathers, and switches to using the unpadded unsharded flattened parameter.
    - In the future, we may add an option to `unshard()` that additionally all-gathers the gradient.
5. `FlatParamHandle.post_unshard(self, prepare_gradient: bool)`
    - For sharded strategies, if using parameter mixed precision, this frees the low precision shard. More generally, this should free any sharded allocations made in `pre_unshard()` since the all-gather has been launched. If using CPU offloading, the GPU copy of the local shard goes out of scope after `unshard()` and is able to be garbage collected. **We should understand if there is any performance difference between manually freeing versus deferring to garbage collection since our usage is inconsistent.** For now, I preserve the existing semantics here.
    - `prepare_gradient` is meant to be set to `True` for the pre-backward unshard and `False` for the forward unshard. This runs the equivalent logic of `_prep_grads_for_backward()`.
    - This post-unshard logic (notably the gradient preparation) now runs in the all-gather stream, which is fine because we always have the current stream wait for the all-gather stream immediately after `FullyShardedDataParallel._unshard()`. IIUC, we do not need to call `_mp_shard.record_stream(current_stream)` (where `current_stream` is the default stream) because `_mp_shard` is allocated and freed in the same (all-gather) stream.
    - A postcondition is that the `FlatParameter` is on the compute device. It should also have the unpadded unsharded size (though I do not have a check for this at the moment).

### Unshard: `summon_full_params()`
Now that we see how the logical unshard has been reorganized for the core code path, let us dive into `summon_full_params()`. 

The two constraints are:
1. If using parameter mixed precision, we should unshard in full precision.
2. We must determine if we should free the padded unsharded flattened parameter upon exiting.

The first constraint is addressed as described before in the core unshard code path, so it remains to explore the second constraint.

I propose a simple rule: **We free iff we actually unshard the `FlatParameter` in `summon_full_params()`** (i.e. it was not already unsharded). We perform a case analysis:

**Parameter mixed precision enabled:**
* `NO_SHARD`: `flat_param.data` points to `flat_param._local_shard`, which is the full precision unsharded flattened parameter. This is **not safe to free**.
* `FULL_SHARD` / `SHARD_GRAD_OP`: We force full precision and all-gather to `_full_prec_full_param_padded`. We do not support `nested summon_full_params()`, so `_full_prec_full_param_padded` must be unallocated. We unshard, and it is **safe to free**.

**Parameter mixed precision disabled:**
* `NO_SHARD`: This is the same as with mixed precision enabled. This is **not safe to free**.
* `FULL_SHARD` / `SHARD_GRAD_OP`: We all-gather to `_full_param_padded`. It may already be unsharded.
    * Already unsharded: The unshard is a no-op. This is **not safe to free**.
        * For `FULL_SHARD`, this can happen for the root FSDP instance after `forward()` but before backward.
        * For `SHARD_GRAD_OP`, this can happen for all FSDP instances after `forward()` but before backward.
    * Needs unshard: We unshard. This is **safe to free**.

Therefore, we see that it is not safe to free when using `NO_SHARD` and when using a sharded strategy but the `FlatParameter` is already unsharded. This is precisely the proposed rule.

There were two notable edge cases that the existing code did not address.
1. The existing code tests if the `FlatParameter` is already unsharded by checking the allocation status of `_full_param_padded`. When using parameter mixed precision, this is the incorrect tensor to check. If `_full_param_padded` is allocated (e.g. when `reshard_after_forward=False` and calling `summon_full_params()` between forward and backward), the already-unsharded check is a false positive, and `summon_full_params()` does not correctly force full precision. https://github.com/pytorch/pytorch/issues/83068
    - This PR's `needs_unshard()` check correctly routes to the appropriate padded unsharded flattened parameter depending on the calling context (i.e. if it needs to force full precision or not).
2. The existing code does not free the GPU copy of the padded unsharded flattened parameter when calling `summon_full_params(offload_to_cpu=True)`. It unshards the `FlatParameter`, moves the padded unsharded flattened parameter to CPU, and sets the `FlatParameter` data to be the appropriate unpadded view into the padded unsharded flattened parameter on CPU. However, `_full_param_padded` still points to the all-gathered padded unsharded flattened parameter on GPU, which is kept in memory. https://github.com/pytorch/pytorch/issues/83076
    - This PR frees the GPU copy and reallocates it upon exiting `summon_full_params()`. This is essential for avoiding peak GPU memory usage from increasing as we recurse through the module tree. There may be some cases where we can avoid reallocation altogether, but that can be addressed in a follow-up PR.
    - This PR offloads the *unpadded* unsharded flattened parameter to CPU directly instead of the *padded* one. As far as I can tell, there is no need to include the padding since unflattening the original parameters does not require the padding.
    - The relevant code is in the context manager `FlatParamHandle.to_cpu()`.

### Unshard: Mixed-Precision Stream

This PR removes the mixed precision stream usage. As is, I do not think there is any extra overlap being achieved by the stream usage.

The low precision shard is allocated and copied to in the mixed precision stream ([code](https://github.com/pytorch/pytorch/blob/1f99bdfcc4a3f97d28471a531d2b69def762f6ba/torch/distributed/fsdp/fully_sharded_data_parallel.py#L1401-L1412)), and the current stream (in this case the all-gather stream) waits for the mixed precision stream ([code](https://github.com/pytorch/pytorch/blob/1f99bdfcc4a3f97d28471a531d2b69def762f6ba/torch/distributed/fsdp/fully_sharded_data_parallel.py#L1414)). However, we immediately schedule an all-gather that communicates that exact low precision shard ([code](https://github.com/pytorch/pytorch/blob/1f99bdfcc4a3f97d28471a531d2b69def762f6ba/torch/distributed/fsdp/fully_sharded_data_parallel.py#L3338)) with no other meaningful computation between. If we remove the mixed precision stream, the low precision shard is allocated and copied to in the all-gather stream (including the non-blocking CPU -> GPU copy if using CPU offloading). 

Under this PR's design, we may consider a "pre-unshard" stream for all logical pre-unshard data transfers if we want to overlap in the future. IIUC, the overlap opportunity exists if there are multiple `FlatParameter`s per module, and we only have the all-gather stream wait for the data transfer corresponding to the local shard it communicates, not the others.

If we agree on removing the mixed-precision stream for now, I will remember to delete it from `_init_streams()`.

## FSDP Runtime: Reshard

Like with unshard, the first step is the look at the existing `_free_full_params()` and `_use_param_local_shard()`. A few notable observations:
- For only `NO_SHARD`, `_free_full_params()` includes a call to `_free_mp_shard()`.
- For `summon_full_params()`, there is a separate `_free_full_params_and_use_local_shard()` that duplicates the main logic of `_free_full_params()` and calls `_use_param_local_shard()`.
- In `forward()`, if `reshard_after_forward=True`, we call `_free_full_params()` and then `_free_mp_shard()`. Hence, for `NO_SHARD`, the `_free_mp_shard()` is a no-op.
- In the post-backward hook, we typically call `_free_full_params()` and `_free_mp_shard()`. The `_free_mp_shard()` is a no-op for `NO_SHARD` and if `reshard_after_forward=True`.

Some comments:
- The code certainly works, but some of the no-ops are subtle. When possible, we should make it clear when calls are no-ops or not. It is good that the existing code documents that `_free_mp_shard()` is a no-op in the post-backward hook when `reshard_after_forward=True`. However, there are still some non-obvious no-ops (around `NO_SHARD`).
- We should see if we can avoid the duplicate `_free_full_params_and_use_local_shard()`.

Let us trace through the logical reshard:
1. `FullyShardedDataParallel._reshard(self, handles: List[FlatParamHandle], free_unsharded_flat_params: List[bool])`
    - The two args should have the same length since they are to be zipped.
    - The goal of having `free_unsharded_flat_params` is that the caller should be explicit about whether the (padded) unsharded flattened parameter should be freed. The low precision shard is always meant to be freed (as early as possible), so there is no corresponding `List[bool]`.
2. `FlatParamHandle.reshard(self, free_unsharded_flat_param: bool)`
    - This frees the (padded) unsharded flattened parameter if `free_unsharded_flat_param` and switches to using the sharded flattened parameter.
    - Echoing back to forcing full precision in `summon_full_params()`, `_free_unsharded_flat_param()` frees the correct tensor by using `_get_padded_unsharded_flat_parameter()`.
3. `FlatParamHandle.post_reshard(self)`
    - I am not fully content with the existence of this method, but this seems to be an unavoidable consequence of `NO_SHARD`. Perhaps, this may be useful in the future for other reasons though.
    - Right now, this method is only meaningful for `NO_SHARD` + parameter mixed precision + outside `summon_full_params()`. `_mp_shard` is not freed in the post-unshard since it is also the low precision _unsharded_ flattened parameter, so we must delay the free until the the post-reshard.

Below the `FlatParamHandle.reshard()` and `post_reshard()` layer, there should not be any no-ops.

One final comment I will mention is that I like the `pre_unshard()`, `unshard()`, `post_unshard()`, and `reshard()`, `post_reshard()` organization because it makes it clear what the boundaries are and their temporal relationship. Through that, we can set pre- and post-conditions. Furthermore, we can eventually convert logic to hooks that may be registered on the `FlatParamHandle` (for `pre_unshard()`, `post_unshard()`, and `post_reshard()`). This may improve the customizability of FSDP.

 ## FSDP Runtime: `forward()`

- This PR reorganizes `forward()` in preparation for non-recursive wrapping, which uses pre-forward and post-forward hooks that expect the signature `hook(module, input)`. For FSDP, the `module` and `input` arguments are not used.
- This PR creates a new method `_fsdp_root_pre_forward()` to handle the logic only the root FSDP should run.

## FSDP Prefetching

Finally, we dive into the prefetching changes. Some highlights:
1. This PR unifies the execution order validation and prefetching implementations.
    - Both involve the execution order and can be unified to share some boilerplate.
2. Execution order validation only runs when the distributed debug level is `INFO`.
    - We have yet to have one success case where we actually catch an unintended source of dynamism. The warning is also too verbose. Hence, we are gating it by the `INFO` level.
3. This PR moves prefetching to be with respect to groups of handles (as mentioned in the constructor comment).
    - This is essential for supporting prefetching with non-recursive wrapping.
4. This PR does not include "bubbles", i.e. modules with no handles, in the recorded execution order(s). This deviates from the existing implementation.
    - This makes prefetching possibly more aggressive (when there are such bubbles), but it should not have significant performance implications either way.
5. This PR changes backward prefetching to reset the post-forward order each iteration (as intended).
6. This PR changes forward prefetching to use the first iteration's pre-forward order instead of the first iteration's post-forward order. (We can discuss whether we want this in this PR or not. Otherwise, I can keep it as using the post-forward order to preserve the existing semantics.) This PR also removes the `all_gather_stream.wait_stream(current_stream)` before forward prefetching because it does not help with high GPU reserved memory. We can add that back if desired.


### Appendix
#### Reverse Post-Forward Order Is Not Always the Pre-Backward Order
The existing PT-D FSDP pre-backward prefetching uses the reverse post-forward order.
<details>
  <summary>Model Code</summary>

  ```
  class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.block1 = nn.Sequential(
            nn.Conv2d(3, 4, kernel_size=3),
            nn.BatchNorm2d(4),
            nn.ReLU(inplace=True),
        )
        self.block2 = nn.Sequential(
            nn.Conv2d(4, 4, kernel_size=3),
            nn.BatchNorm2d(4),
            nn.ReLU(inplace=False),
        )
        self.block3 = nn.Linear(12, 8)
        self.head = nn.Sequential(
            nn.AdaptiveAvgPool2d(output_size=(1, 1)),
            nn.Flatten(),
            nn.Linear(4, 10),
        )

    def forward(self, x):
        x = self.block1(x)
        x = self.block2(x)
        x = self.block3(x)
        return self.head(x)

  model = Model().cuda()
  fsdp_kwargs = {}
  model.block1[1] = FSDP(model.block1[1], **fsdp_kwargs)  # BN2d
  model.block2[1] = FSDP(model.block2[1], **fsdp_kwargs)  # BN2d
  model.block1 = FSDP(model.block1, **fsdp_kwargs)
  model.block2 = FSDP(model.block2, **fsdp_kwargs)
  model.block3 = FSDP(model.block3, **fsdp_kwargs)
  model = FSDP(model, **fsdp_kwargs)
  ```
</details>

<details>
  <summary>Execution Orders </summary>

  ```
  Pre-backward hook for ('head.2.weight', 'head.2.bias') 140339520587136 (model)
  Pre-backward hook for ('weight', 'bias') 140339461194656 (block3)
  Pre-backward hook for ('0.weight', '0.bias') 140339520589776 (block2)
  Pre-backward hook for ('weight', 'bias') 140339520587664 (block2 BN)
  Pre-backward hook for ('weight', 'bias') 140339520586656 (block1 BN)
  Pre-backward hook for ('0.weight', '0.bias') 140339520588768 (block1)
  
  Pre-forward order:
  ('head.2.weight', 'head.2.bias') 140339520587136 (model)
  ('0.weight', '0.bias') 140339520588768 (block1)
  ('weight', 'bias') 140339520586656 (block1 BN)
  ('0.weight', '0.bias') 140339520589776 (block2)
  ('weight', 'bias') 140339520587664 (block2 BN)
  ('weight', 'bias') 140339461194656 (block3)
  
  Reverse post-forward order:
  ('head.2.weight', 'head.2.bias') 140339520587136 (model)
  ('weight', 'bias') 140339461194656 (block3)
  ('0.weight', '0.bias') 140339520589776 (block2)
  ('weight', 'bias') 140339520587664 (block2 BN)
  ('0.weight', '0.bias') 140339520588768 (block1)
  ('weight', 'bias') 140339520586656 (block1 BN)
  ```
</details>



[ghstack-poisoned]

---
## [plinkiac/Movie-Talk](https://github.com/plinkiac/Movie-Talk)@[6e00428186...](https://github.com/plinkiac/Movie-Talk/commit/6e004281864d293bf033214183a9a93be5728eec)
#### Tuesday 2022-09-06 15:57:24 by Harry S. Plinkett

Update 2015-01-10 - Fuck You, It's January (2015).txt

---
## [newstools/2022-new-york-post](https://github.com/newstools/2022-new-york-post)@[c6d83236bd...](https://github.com/newstools/2022-new-york-post/commit/c6d83236bd1f7d55edb303556f0d1f27318df35a)
#### Tuesday 2022-09-06 16:22:46 by Billy Einkamerer

Created Text For URL [nypost.com/2022/09/06/dear-abby-i-told-my-girlfriend-she-ordered-too-much-at-her-birthday-dinner/]

---
## [digitalocean/cadence-client](https://github.com/digitalocean/cadence-client)@[f5e0fd25e4...](https://github.com/digitalocean/cadence-client/commit/f5e0fd25e4347c85b28dac87f51b532700455d2c)
#### Tuesday 2022-09-06 16:31:31 by Steven L

Sharing one of my favorite "scopes" in intellij, and making it easier to add more (#1182)

Goland is nice, and the type-based navigation is wildly superior to gopls-driven
stuff in my experience, so I tend to lean hard on it when I'm able.

By default though, Goland searches *everything*.  All the time.
That's totally reasonable as a default, but we can do better:

- Tests are not usually all that interesting when trying to understand and navigate code.
  (perhaps they should be, but that's more a platonic ideal than a reality)
- Generated RPC code is almost never useful to dive into.  The exposed API surface is sufficient,
  if it compiles, it's correct.
- Non-Go files are just less interesting in a Go project.

So this scope excludes ^ all that.
To add more shared ones, just check the "share through vcs" box and commit it.

To use it, just select the scope from the dropdown when you search.  E.g. "find in files" ->
change from "in project" to "scope" -> change the dropdown.  This custom scope will now appear,
and it'll remember what you last used, so it's a nice default.

This also works in "call hierarchy", "go to implementations" (open it in a panel to configure it,
with the gear on the side.  it's awful UI but it works), etc quite a lot of places.

This same kinda-obtuse search-scope query language can be used to mark things as generated or test
related, which will also help other parts of the IDE mark things as more or less relevant for you.
It's worth exploring a bit, scopes and filters can be used to do a lot: https://www.jetbrains.com/help/idea/scope-language-syntax-reference.html

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[69b3fa1a66...](https://github.com/mrakgr/The-Spiral-Language/commit/69b3fa1a66faedab39d569ef703bd51e2bc9474d)
#### Tuesday 2022-09-06 16:41:54 by Marko Grdinić

"2:05pm. I have the rest of the chapter planned out, and just have to draw the world out. I should be able to finish it tomorrow I think. How much do I have writen so far?

7.5k. This is quite a bit actually. Where was I yesterday? 5.7k. Ok, it is not too much. I still have a lot in me left.

Let me just focus on writing.

$$$

(Heaven's Key, Heavenly realm)

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

"No, I don't think so. But it doesn't mean that he necessarily has to lose even against a superior opponent. We careful note down how many chips the newcomers have won for a reason. As long as he has more than the opponent, he can put pressure on him and seek to break up the match."

...

$$$

4:35pm. I am running out of steam a bit. How far have I gotten thus far.

5:55pm. > Maybe it was because I am too used against playing versus unintelligent NPCs in normal computer games, but nonetheless I didn't think about this.

Let me back up this quote.

6:25pm. Done with lunch. How much have I writen so far? 10.4k. I started the day out at 5.7k. So I've writen 4.7k words today. Not bad.

6:30pm. I think given how on fire I am, I should be able to finish the chapter tomorrow. After that I'll proof it and split it into two as it is a bit long.

6:35pm. It is good that the chapters are long as it allows me to post twice a week. Well, let me close here. Good work today, me."

---
## [atere21/alx-system_engineering-devops](https://github.com/atere21/alx-system_engineering-devops)@[cef2264bb0...](https://github.com/atere21/alx-system_engineering-devops/commit/cef2264bb07f1bcb2ee6e5cd3615bf052c70e73f)
#### Tuesday 2022-09-06 16:43:16 by Atere Oluwatosin

Tasks 📃

0. Where am I?

0-current_working_directory: Bash script that prints the absolute pathname of the current working directory.

1. What’s in there?

1-listit: Bash script that displays the contents list of current directory

2. There is no place like home

2-bring_me_home: Bash script that changes the working directory to the user's home directory.

3. The long format

3-listfiles: Bash script that displays current directory contents in long format.

4. Hidden files

4-listmorefiles: Bash script that displays current directory contents, including hidden files, using long format.

5. I love numbers

5-listfilesdigitonly: Bash script that displays current directory contents, including hidden files, as follows:
Long format.
User and group ID's displayed numerically.

6. Welcome 

6-firstdirectory: Bash script that creates a directory named my_first_directory in the /tmp/ directory.

7. Betty in My first directory 

7-movethatfile: Bash script that moves the file betty from /tmp/ to /tmp/my_first_directory

8. Bye bye Betty

8-firstdelete: Bash script that deletes the file betty in /tmp/my_first_directory

9. Bye bye my first directory 

9-firstdirdeletion: Bash script that deletes the directory school in the /tmp directory.

10. Back to the future

10-back: Bash script that changes the working directory to the previous one.

11. Lists

11-lists: Bash script that lists all files, including hidden files, in the current directory, parent of the working directory, and /boot directory, using long format.

12. File type

12-file_type: Bash script that prints the type of the file named iamafile located in the /tmp directory.

13. We are symbols, and inhabit symbols

13-symbolic_link: Bash script that creates a symbolic link to /bin/ls, named __ls__.

14. Copy HTML files

14-copy_html: Bash script that copies all HTML files from the current working directory to the parent of the working directory, but only those that did not exist in the parent directory or were newer than the versions in the parent working directory.

15. Let’s move

15-lets_move: Bash script that moves all files beginning with an uppercase letter to the directory /tmp/u.

16. Clean Emacs

16-clean_emacs: Bash script that deletes all files in the current working directory that end with the character ~.
17. Tree

17-tree: Bash script that creates the directories welcome/, welcome/to/ and welcome/to/school in the current directory.

18. Life is a series of commas, not periods

18-commas: Bash script that lists all files and directories of the current directory, including hidden ones, as follows:
Separated by commas (,).
Directory names end with a slash (/).
Alpha-ordered, except for the directories . and .. which are listed at the beginning.
Only digits and letters are used to sort - digits come first.

19. File type: School

School.mgc: A magic file that can be used with the command file to detect school data files.

---
## [ivanmixo/BeeStation-Hornet](https://github.com/ivanmixo/BeeStation-Hornet)@[3249b4560b...](https://github.com/ivanmixo/BeeStation-Hornet/commit/3249b4560b568fe762f2a695a6427bab7c56c649)
#### Tuesday 2022-09-06 16:48:40 by DrDuckedGoose

Lasso Fix (#7345)

* Merge https://github.com/BeeStation/BeeStation-Hornet into annoying-thing Merge conflicts :)

* Initial - 23 7 22

- Doesn't allow dead mobs to be ridden
- Space walk is now specific to the mob

* Actually Fix It - 23 7 22

* Fuck - 23 7 22

- Fix being able to tame human
- Fix being able to tame the dead

* Update carp_lasso.dm

* You boys fucked buckle code - 23 7 22

* Update carp_lasso.dm

* Update riding.dm

* fix icon - 24 7 22

* Review Changes - 24 7 22

---
## [sjp38/linux](https://github.com/sjp38/linux)@[eef1848f0a...](https://github.com/sjp38/linux/commit/eef1848f0ada80a15ef5c1bb25faa9a9a9c04760)
#### Tuesday 2022-09-06 16:59:26 by Johannes Weiner

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
## [plinkiac/Movie-Talk](https://github.com/plinkiac/Movie-Talk)@[bf6631429b...](https://github.com/plinkiac/Movie-Talk/commit/bf6631429bb2ad3fafe3fb666bfa27eadb1b1056)
#### Tuesday 2022-09-06 17:10:58 by Harry S. Plinkett

Update 2017-01-12 - Fuck You, It's January (2017).txt

---
## [Paxilmaniac/Skyrat-tg](https://github.com/Paxilmaniac/Skyrat-tg)@[a4bfe65cb1...](https://github.com/Paxilmaniac/Skyrat-tg/commit/a4bfe65cb1caece1e3e6a4635fa17d39f1aa3478)
#### Tuesday 2022-09-06 17:38:33 by SkyratBot

[MIRROR] Dimensional Anomaly [MDB IGNORE] (#15974)

* Dimensional Anomaly (#69512)

About The Pull Request

Everyone has been asking: "When will there be an anomaly like the bioscrambler, but for the space station? Please, we need more things which replace objects with different objects from the same typepath."
Well I made it and it looked like ass because non-tiling floor and walls look terrible, so then I made this instead.
Dimensional.mp4

The "dimensional anomaly" shifts matter into a parallel dimension where objects are made out of something else.
Like the Bioscrambler anomaly, it does not expire on its own and only leaves when someone signals it or uses an anomaly remover.
When it spawns it picks a "theme" and converts terrain around it until it covers a 7x7 square, then it teleports somewhere else and picks a new theme.

A lot of these themes are relatively benign like "meat", "fancy carpet", or "gold". Some of them are kind of annoying like "icebox" because it creates floor which slows you down, or "clown" because bananium is intentionally annoying. Some of them are actively dangerous, mostly "uranium" and "plasma".
The main problem this will usually cause for crewmembers is decreasing area security. When it replaces doors it replaces them with ones which don't have any access control, and it will also replace RWalls with normal and much more vulnerable walls which will make breaking and entering significantly easier until someone has taken the time to fix the damage. But also sometimes it will irradiate them, you never know.

The fact that sometimes the changes are benign (or provide uncommon materials) and might be happening in places you don't care about access to might encourage people to push their luck and leave it alone until it starts turning the captain's office into a bamboo room or repainting medbay a fetching shade of flammable purple, which I would consider a success.
Armour.mp4

If you successfully harvest the anomaly core you can place it into the reactive armour to get Reactive Barricade Armour, which shifts your dimension when you take damage and attempts to place some randomised (not terribly durable) objects between you and hopefully your attacker (it really just picks up to four random unoccupied tiles next to you). If you're EMPed then the changes it make to the environment will often be as unpleasant for you as they are for a pursuer, and significantly more likely to harm both of you rather than just provide obstacles.

Other changes:
I split anomalies out into their own dmi file, seems to be all the rage lately.
I moved the anomaly placing code into a datum instead of the event because I wanted to reuse it but if you have a better idea about where I could have put it let me know.
This also fixes a bug where the material spreader component wasn't working when I applied plasma materials to something, the extra whitespace was parsing as another argument for some reason and meant it would runtime.
Supermatter delamination was still pointing to Delimber anomalies instead of Bioscrambler.

* Dimensional Anomaly

* Fixes the upstream merge skew

Co-authored-by: Jacquerel <hnevard@gmail.com>
Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>
Co-authored-by: GoldenAlpharex <jerego1234@hotmail.com>

---
## [Caldony/lobotomy-corp13](https://github.com/Caldony/lobotomy-corp13)@[e77a47e95d...](https://github.com/Caldony/lobotomy-corp13/commit/e77a47e95d751470b8edda214e82b350fb0807c6)
#### Tuesday 2022-09-06 17:48:00 by Gelatelly

I HATE RUNTIMES I HATE RUNTIMES I HATERUNTIMES

use the shittiest method in existence to bypass runtimes, unfortunately I couldn't use initial() without adding some issues so fuck me I guess

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[f0ceecff46...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/f0ceecff46f9b600dfe8e60199f354f61d63a0a4)
#### Tuesday 2022-09-06 17:53:50 by SkyratBot

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
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[e7230e8b4a...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/e7230e8b4a6d60e1b6c025b52b9f3d2fc26577a5)
#### Tuesday 2022-09-06 17:53:50 by SkyratBot

[MIRROR] Resolves is_banned_from headaches and lag (Speeds up roundstart significantly) [MDB IGNORE] (#16001)

* Resolves is_banned_from headaches and lag (Speeds up roundstart significantly) (#69376)

About The Pull Request

Just to be clear, when I refer to time here, I am not talking about cpu time. I'm talking about real time.
This doesn't significantly reduce the amount of work we do, it just removes a lot of the waiting around we need to do for db calls to finish.

Adds queuing support to sql bans, so if an ongoing ban retrieval query is active any successive ban retrieval attempts will wait for the active query to finish

This uses the number/blocking_query_timeout config option, I hope it's still valid

This system will allow us to precache ban info, in parallel (or in batches)
With this, we can avoid needing to setup all uses of is_banned_from to support parallelization or eat the cost of in-series database requests

Clients who join after initialize will now build a ban cache automatically

Those who join before init is done will be gathered by a batch query sent by a new subsystem, SSban_cache.

This means that any post initalize uses of is_banned_from are worst case by NATURE parallel (since the request is already sent, and we're just waiting for the response)

This saves a lot of headache for implementers (users) of the proc, and saves ~0.9 second from roundstart setup for each client (on /tg/station)

There's a lot of in series is_banned_from calls in there, and this nukes them. This should bring down roundstart join times significantly.

It's hard to say exactly how much, since some cases generate the ban cache at other times.
At base tho, we save about 0.9 seconds of real time per client off doing this stuff in parallel.
Why It's Good For The Game

    When I use percentages I'm speaking about cost per player

I don't like how slow roundstart feels, this kills about 66% of that. the rest is a lot of misc things. About 11% (it's actually 16%) is general mob placing which is hard to optimize. 22% is manifest generation, most of which is GetFlatIcons which REALLY do not need to be holding up the main thread of execution.

An additional 1 second is constant cost from a db query we make to tell the server we exist, which can be made async to avoid holding the proc chain.

That's it. I'm bullying someone into working on the manifest issue, so that should just leave 16% of mob placing, which is really not that bad compared to what we have now.
Changelog

cl
code: The time between the round starting and the game like, actually starting has been reduced by 66%
refactor: I've slightly changed how ban caches are generated, admins please let me know if anything goes fuckey
server: I'm using the blocking_query_timeout config. Make sure it's up to date and all.
/cl

* Resolves is_banned_from headaches and lag (Speeds up roundstart significantly)

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [arezaii/chapel](https://github.com/arezaii/chapel)@[1b5d5a5140...](https://github.com/arezaii/chapel/commit/1b5d5a5140309b41f569904e73fb9974afcae5b5)
#### Tuesday 2022-09-06 19:41:31 by Brad Chamberlain

Merge pull request #20616 from bradcray/range-docs-tidying

Tidy up range docs

[reviewed by @bmcdonald3 — thanks!]

While reviewing my the range docs after my changes to its behavior
last night, I found some pre-existing bugs that needed fixing,
that the operators were now being generated by chpldoc, and some
other opportunities for cleanup.  Summarizing, they were:

* the expected output from the alignedLow/High docs wasn't printing
  (and hadn't been in previous releases either)

* the signatures on the param/type queries in the spec used illegal
  syntax (though now they fall prey to the poor spacing when
  rendered by Sphinx on Chrome.

* I squashed the chpldocumentation of the operators because they're
  already described in the text of the spec, which does a better job
  of it.  That said, going forward, I think we'd like to find a way to
  integrate operator signatures into these sections of the spec so
  that people can see what the overloads are.  Not today's task though.

* I tried to clarify some wordings and descriptions.

* removed the "more descriptive" clause that I'd applied to the
  alignedLow/High queries yesterday because it sounded like more of
  a value judgement or preference than I'd intended.

* I more uniformly set ``true`` and ``false`` off using code
  formatting.

* I more uniformly started entries with "Returns" rather than "Return"

* I more uniformly ended descriptions with periods

---
## [lunaruan/react](https://github.com/lunaruan/react)@[b6978bc38f...](https://github.com/lunaruan/react/commit/b6978bc38f6788c7e73982b9fd2771aabdf36f15)
#### Tuesday 2022-09-06 20:35:55 by Andrew Clark

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
## [SuitableEmu/PowerShell](https://github.com/SuitableEmu/PowerShell)@[5961f316a0...](https://github.com/SuitableEmu/PowerShell/commit/5961f316a09b94155488c5f983bdb985c540f454)
#### Tuesday 2022-09-06 20:39:50 by SuitableEmu

Outlook-to-Excel

This script searches your inbox for an e-mail and grabs the body of that e-mail. and basically lets you do what you want with it. It can be slow if you have thousands of e-mails because it does unfortunately search through all of them.

I tried to find something similar through google but didnt have any luck. Apparently other people have been searching for something like this as well so here is my shot at it.

I'm sorry for the spaghetti code, i had to remove a lot of stuff from the script as the original script is well over 1000 lines of code at this point. I tried to make it as easy to read as possible and as easy to understand and edit. It can probably be a lot more optimized,.

The reason the Clean-Memory function is there is because i kept running out of memory, this can also probably be fixed by better code. :) But i'm not that good.

I didnt find a way to automatically have it select the next row in excel so if and elseif is used here.

If you have any questions or want to help make the script better please let me know :) Thank you

---
## [WaffleLapkin/mbkb](https://github.com/WaffleLapkin/mbkb)@[533b957c9c...](https://github.com/WaffleLapkin/mbkb/commit/533b957c9c4edb791716025cd494ef792298a642)
#### Tuesday 2022-09-06 20:56:49 by Maybe Waffle

Add support for leds (kinda)

This adds support for reading leds (like caps lock).
Num Lock and Caps Lock were tested and work.
Other lends (Scroll Lock, Compose, Kana) couldn't be tested because my
computer refuses to enable them (in case of Kana I couldn't even press
it...).

I hate this cursed world.

---
## [Xyce/Xyce](https://github.com/Xyce/Xyce)@[faf2ef48dd...](https://github.com/Xyce/Xyce/commit/faf2ef48dd2226203bc94222bbc7bbdb3c1d73dd)
#### Tuesday 2022-09-06 21:14:59 by Tom Russo

Remove an ancient, windows-specific kludge from BSIM4

Years ago, we were defining an M_PI macro as "2.0*atan(1)" if a system
header did not define it for us.  This was bad, because it was not
properly set up with parentheses --- which was awful if one *divided*
by M_PI   1/M_PI would become 1/2*atan(1) (or 0.25*pi) instead of
1/(2*atan(1)) (1/pi).  This error was present in the code from the
beginning commit 13969fa4 in 2000.

This went on for years leading to a superstition that something was
wrong specifically on windows (the only system that didn't have M_PI
defined in system headers), and a habit of doing funny things whenever
M_PI was used in the code (like saving it into a variable before doing
things with it, or putting extraneous parens into expressions).  The
BSIM4 has just such an expression and a big block of comments
explaining it.

In commit b57a07a in 2013 this bug was finally detected and fixed, but
we did not go back and undo all the goofy, superstitious hacks that
had been put into the code in an attempt to stave off the problems it
caused.

Since I'm working in the BSIM4 today, I am removing them now.

Note that the use of a function call and multiplication to get M_PI if
it is undefined was done away with altogether in commit 3b253df just
last month, and now it's a straight floating point constant.

Tangientially related to Xyce/backlog/project-backlog#419

---
## [Chima-Peter/alx-system_engineering-devops](https://github.com/Chima-Peter/alx-system_engineering-devops)@[7cb35458af...](https://github.com/Chima-Peter/alx-system_engineering-devops/commit/7cb35458af989fcf36d65846ff241c55a6209755)
#### Tuesday 2022-09-06 21:24:43 by Chima-Peter

forgive me but im tired as crazy and my head isnt in thw right place. Fuck man

---
## [Buildstarted/linksfordevs](https://github.com/Buildstarted/linksfordevs)@[2fc8823835...](https://github.com/Buildstarted/linksfordevs/commit/2fc8823835e491aa630e5eb649107309eb77fad0)
#### Tuesday 2022-09-06 22:06:49 by Ben Dornis

Updating: 9/6/2022 10:00:00 PM

 1. Added: Vulnerability Management for Go - The Go Programming Language
    (https://go.dev/blog/vuln)
 2. Added: 30 thoughts on turning 30
    (https://herman.bearblog.dev/turning-30/)
 3. Added: Say no to restricting Internet by using open API - YottaAnswers Blog
    (https://blog.yottaanswers.com/say-no-to-restricting-internet-by-using-open-api/)
 4. Added: HTTP Timeouts
    (https://steve.dignam.xyz/2022/09/04/http-timeouts/)
 5. Added: Electric Bike, Stupid Love of My Life
    (https://craigmod.com/essays/electric_bikes/)
 6. Added: One Year With the Framework Laptop and NixOS
    (https://blog.tjll.net/one-year-with-nixos-on-framework/)
 7. Added: It's time to leave Bitwarden
    (https://blog.notesnook.com/its-time-to-leave-bitwarden/)
 8. Added: Winding numbers using a Cauchy integral, with WebGL
    (https://benoit.paris/posts/winding-cauchy-integral/)
 9. Added: What Is A Blockchain
    (https://decentralizedthoughts.github.io/2022-09-05-what-is-a-blockchain/)
10. Added: Compressing global illumination with neural networks
    (https://juretriglav.si/compressing-global-illumination-with-neural-networks/)
11. Added: Privacy architectural changes in the web are coming
    (https://blog.lukaszolejnik.com/privacy-architectural-changes-coming/)
12. Added: I sold my SaaS for $800,000
    (https://isora.me/i-sold-saas-for-800k/)
13. Added: Machine Learning at the edge | Мои IT-заметки
    (https://my-it-notes.com/2022/09/machine-learning-at-the-edge/)
14. Added: fxhash - Lessons Learned from Implementing "Wave Function Collapse"

    (https://www.fxhash.xyz/article/lessons-learned-from-implementing-%22wave-function-collapse%22)
15. Added: NASA Selects SiFive and Makes RISC-V the Go-to Ecosystem for Future Space Missions - SiFive
    (https://www.sifive.com/press/nasa-selects-sifive-and-makes-risc-v-the-go-to-ecosystem)
16. Added: Modern alternatives to BEM
    (https://daverupert.com/2022/08/modern-alternatives-to-bem/)
17. Added: Manually generating a Zoom link
    (https://huey.xyz/posts/2022-07-27-zoom-link/)
18. Added: How I Take Book Notes — Simon Berens
    (https://simonberens.me/blog/how-i-take-book-notes)
19. Added: Replicant: Reproducing a Fault Injection Attack on the Trezor One
    (https://voidstarsec.com/blog/replicant-part-1)
20. Added: Perfect Notes or My Journey to Obsidian
    (https://mnaoumov.wordpress.com/2022/05/08/perfect-notes-or-my-journey-to-obsidian/)

Generation took: 00:06:38.6949213
 Maintenance update - cleaning up homepage and feed

---
## [yilei/black](https://github.com/yilei/black)@[0019261abc...](https://github.com/yilei/black/commit/0019261abcf6d9e564ba32d3cc15534b9026f29e)
#### Tuesday 2022-09-06 22:44:54 by Richard Si

Update stable branch after publishing to PyPI (#3223)

We've decided to a) convert stable back into a branch and b) to update
it immediately as part of the release process. We may as well automate
it. And about going back to a branch ...

Git tags are not the right tool, at all[^1]. They come with the
expectation that they will never change. Things will not work as
expected if they do change, doubly so if they change regularly. Once
you pull stable from the remote and it's copied in your local
repository, no matter how many times you run git pull you'll never see
it get updated automatically. Your only recourse is to delete the tag
via `git tag -d stable` before pulling.

This gets annoying really quickly since stable is supposed to be the
solution for folks "who want to move along as Black developers deem
the newest version reliable."[^2] See this comment for how this impacts
users using our Vim plugin[^3]. It also affects us developers[^4]. If
you have stable locally, once we cut a new release and update the stable
tag, a simple `git pull` / `git fetch` will not pull down the updated
stable tag. Unless you remember to delete stable before pulling, stable
will become stale and useless.

You can argue this is a good thing ("people should explicitly opt into
updating stable"), but IMO it does not match user expectations nor
developer expectations[^5]. Especially since not all our integrations
that use stable are bound by this security measure, for example our
GitHub Action (since it does a clean fetch of the repository every time
it's used). I believe consistency would be good here.

Finally, ever since we switched to a tag, we've been facing issues with
ReadTheDocs not picking up updates to stable unless we force a rebuild.
The initial rebuild on the stable update just pulls the commit the tag
previously pointed to. I'm not sure if switching back to a branch will
fix this, but I'd wager it will.

[^1]: https://git-scm.com/docs/git-tag#_on_re_tagging

[^2]: https://black.readthedocs.io/en/stable/contributing/release_process.html#moving-the-stable-tag

[^3]: https://github.com/psf/black/issues/2503#issuecomment-1196357379

[^4]: In fairness, most folks working on Black probably don't use the
      `stable` ref anyway, especially us maintainers who'd know what is
      the latest version by heart, but it'd still be nice to make it
      usable for local dev though.

[^5]: Also what benefit does a `stable` ref have over explicit version
      tags like `22.6.0`? If you're going to opt into some odd pin
      mechanism, might as well use explicit version tags for clarity
      and consistency.

---
## [CharlesWedge/Citadel-Station-13-RP](https://github.com/CharlesWedge/Citadel-Station-13-RP)@[24aca0ae55...](https://github.com/CharlesWedge/Citadel-Station-13-RP/commit/24aca0ae55ce2204474ec23fed6d23cb46b6645e)
#### Tuesday 2022-09-06 23:26:59 by LordPapalus

Cargonia, but with less weapons (#4370)

* Cargonia is no more

Fuck you

* PLEASE

* Zandario, I will suck your PP

---
## [mjay88/midcitysecuritydistrict.org](https://github.com/mjay88/midcitysecuritydistrict.org)@[a407e9a083...](https://github.com/mjay88/midcitysecuritydistrict.org/commit/a407e9a083233b738c5f904cfc64487eaaad59e7)
#### Tuesday 2022-09-06 23:49:27 by Michael W Jarrett

Merge pull request #80 from mjay88/development

fuck you

---
## [Yourrrrlove/obsidian-1](https://github.com/Yourrrrlove/obsidian-1)@[b30ea94d47...](https://github.com/Yourrrrlove/obsidian-1/commit/b30ea94d477e5e3e1bb5569809fb5b9142ec700e)
#### Tuesday 2022-09-06 23:49:58 by The Arctesian

Rm `$` from install.md

Lets do this the proper way shall we. The $ in front is kinda annoying, makes you have to ctrl a then ctrl d which is not fun and for nubes having to arrow all the way back is a pain

---

