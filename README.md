## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-09-29](docs/good-messages/2022/2022-09-29.md)


2,118,414 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,118,414 were push events containing 3,218,083 commit messages that amount to 258,058,403 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 42 messages:


## [grafana/tanka](https://github.com/grafana/tanka)@[904a7c53e8...](https://github.com/grafana/tanka/commit/904a7c53e8a1afec5af8b05bb11f7da846595a09)
#### Thursday 2022-09-29 00:15:15 by Julien Duchesne

Fix `getSnippetHash` not considering all files (#765)

* Fix `getSnippetHash` not considering all files
Made a stupid mistake in the previous PR: https://github.com/grafana/tanka/pull/759

This fixes it and adds another benchmark test to ensure it doesn't happen again.
I also removed the Github Actions benchmark test, as it's not really useful, anytime we change the tests, we'll get erroneous results which will be annoying.
Instead, I added the benchmark tests to the Drone run, we can compare whenever we want.

* linting

* Add changelog, will release straight away

---
## [swig/swig](https://github.com/swig/swig)@[9908f9f310...](https://github.com/swig/swig/commit/9908f9f310aeadb129b41d14d40de9f2163ffa24)
#### Thursday 2022-09-29 00:21:43 by Olly Betts

[php] Fix testcase segfaults with PHP 8.0

These testcases were segfaulting:

prefix
director_using_member_scopes
virtual_poly

The fix here is admittedly a hack - we perform the initialisation
of EG(class_table) from CG(class_table) which PHP will do, but
hasn't yet.

PHP doesn't seem to clearly document which API calls are actually
valid in minit or other initialisation contexts, but the code we're
generating works with all PHP 7.x and PHP 8.x versions aside from PHP
8.0 so it seems this is a bug in PHP 8.0 rather than that we're doing
something invalid, and we need to work with existing PHP 8.0 releases
so this hack seems a necessary evil.  It will at least have a limited
life as PHP 8.0 is only in active support until 2022-11-26, with
security support ending a year later.

Fixes #2383.

---
## [natleethe3rd/AutoRpg](https://github.com/natleethe3rd/AutoRpg)@[24340b128a...](https://github.com/natleethe3rd/AutoRpg/commit/24340b128a6aaa319c8514f145c14aae2cc593db)
#### Thursday 2022-09-29 00:28:48 by Natalee Lee

init

fuckin goddamn unity piece of shit mother fucker i gonna kill u

---
## [lgritz/OpenShadingLanguage](https://github.com/lgritz/OpenShadingLanguage)@[ce8bea7805...](https://github.com/lgritz/OpenShadingLanguage/commit/ce8bea78058d87fdc91eb9849fed0d79937a5121)
#### Thursday 2022-09-29 00:56:55 by Larry Gritz

LLVM 15.0 support

* A variety of changes to get a clean build and passing tests when
  using LLVM 15.0.

* I've noticed problems when using LLVM 15 but building with earlier
  clang, so the cmake scripts now print a warning in that case, so if
  users encounter trouble they have a hint about what to do to fix it.

* For our CI tests on Mac, force the MacOS-11 test to use llvm 14,
  and the MacOS-12 test to use llvm 15.

IMPORTANT TO-DO / CAVEATS:

1. When doing JIT at optlevel 12 or 13, I had to disable a number of
   passes that don't seem to exist anymore in LLVM 15. This is enough
   to get it working, and to be honest, I don't know if anybody uses
   these opt levels.  But we need to revisit this, because I don't
   know if there these are cases where the names of the passes merely
   changed or that new passes take their place (in which case we
   should add the new passes, not stop after merely disabling the
   deprecated ones). For that matter, optlevel modes 11, 12, 13 are
   supposed to match what clang does for -O1, -O2, -O3, and that
   changes from one release to the next, so we should probably revisit
   this list and make sure it's matching clang's current choices
   (which I assume are crafted and periodically revised by clang's
   authors).

2. LLVM 15 switches to "opaque pointers". It still supports typed
   pointers...  for now. But as you can see in the diffs, I had to
   disable a variety of deprecation warnings and take some other
   actions to put LLVM 15 in the old "opaque ptr" mode to match our
   use of LLVM <= 14. But this is only temporary, because the typed
   pointer mode is expected to be removed entirely in LLVM 16. So at
   some point in the next few months, we are going to need to support
   opaque pointers in our use of LLVM. (Also note: for a while, we're
   going to have a bunch of ugly `#if` guards or other logic to
   support both opaque pointers for users with llvm >= 16 and also
   typed pointers for users with llvm <= 14, until such time as our
   LLVM minimum is at least 15, which I expect is not a reasonable
   assumption for at least a couple years.)

Signed-off-by: Larry Gritz <lg@larrygritz.com>

---
## [ValoTheValo/CEV-Eris](https://github.com/ValoTheValo/CEV-Eris)@[1908bd88a8...](https://github.com/ValoTheValo/CEV-Eris/commit/1908bd88a830c18782406694e4d5e1ed0dd40a68)
#### Thursday 2022-09-29 01:13:48 by Valo

i hate my pc

i crashed and lost all my god damn progress again

---
## [ValoTheValo/CEV-Eris](https://github.com/ValoTheValo/CEV-Eris)@[29430253ff...](https://github.com/ValoTheValo/CEV-Eris/commit/29430253ffa7c3394df438c922c3827bfbf79f51)
#### Thursday 2022-09-29 02:23:32 by maikilangiolo

Levergun re do (#7587)

* update timer (#7501)

* FUCK YOU FUCK YOUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU

* Update code/modules/projectiles/guns/projectile/battle_rifle/levergun.dm

Co-authored-by: hyperioo <64754494+hyperioo@users.noreply.github.com>

---
## [timothymtorres/tgstation](https://github.com/timothymtorres/tgstation)@[d34fa4c642...](https://github.com/timothymtorres/tgstation/commit/d34fa4c642839215df5ba985d098a04e4d555b5b)
#### Thursday 2022-09-29 02:58:11 by LemonInTheDark

Macro optimizes SSmapping saving 50%  (#69632)

* 'optimizes' space transitions by like 0.06 seconds, makes them easier to read tho, so that's an upside

* ''''optimizes'''' parsed map loading

I'm honestly not sure how big a difference this makes, looked like small
percentage points if anything
It's a bit more internally concistent at least, which is nice. Also I
understand the system now.

I'd like to think it helped but I think this is kinda a "do you think
it's easier to read" sort of situation. if it did help it was by the
skin of its teeth

* Saves 0.6 seconds off loading meta and lavaland's map files

This is just a lot of micro stuff.
1: Bound checks don't need to be inside for loops, we can instead bound the iteration counts
2: TGM and DMM are parsed differently. in dmm a grid_set is one z level,
   in tgm it's one collumn. Realizing this allows you to skip copytexts and
   other such silly in the tgm implemenentation, saving a good bit of time
3: Min/max bounds do not need to be checked inside for loops, and can
   instead be handled outside of them, because we know the order of x
   and y iteration. This saves 0.2 seconds

I may or may not have made the code harder to read, if so let me know
and I'll check it over.

* Micro ops key caching significantly. Fixes macros bug

inserting \ into a dmm with no valid target would just less then loop
the string. Dumb

Anyway, optimizations. I save a LOT of time by not needing to call
find_next_delimiter_position for every entry and var set. (like maybe 0.5
seconds, not totally sure)
I save this by using splittext, which is significantly faster. this
would cause parsing issues if you could embed \n into dmms, but you
can't, so I'm safe.

Lemme see uh, lots of little things, stuff that's suboptimal or could be
done cheaper. Some "hey you and I both know a \" is 2 chars long sort of
stuff

I removed trim_text because the quote trimming was never actually used,
and the space trimming was slower then using the code in trim. I also
micro'd trim to save a bit of time. this saves another maybe 0.5.

Few other things, I think that's the main of it. Gives me the fuzzy
feelings

* Saves 50% of build_coordinate's time

Micro optimizing go brrrrr
I made turf_blacklist an assoc list rather then just a normal one, so
lookups are O(log n) instead of O(n). Also it's faster for the base case
of loading mostly space.

Instead of toggling the map loader right before and right after New()
calls, we toggle at the start of mapload, and disable then reenable if
we check tick. This saves like 0.3 seconds

Rather then tracking an area cache ourselves, and needing to pass it
around, we use a locally static list to reference the global list of
area -> type. This is much faster, if slightly fragile.

Rather then checking for a null turf at every line, we do it at the
start of the proc and not after. Faster this way, tho it can in theory
drop area vvs.

Avoids calling world.preloader_setup unless we actually have a unique
set of attributes. We use another static list to make this comparison
cheap. This saves another 0.3

Rather then checking for area paths in the turf logic, or vis versa, we
assume we are creating the type implied by the index we're reading off.
So only the last type entry will be loaded like a turf, etc.
This is slightly unsafe but saves a good bit of time, and will properly
error on fucked maps.

Also, rather then using a datum to hold preloader vars, we use 2 global
variables. This is faster.

This marks the end of my optimizations for direct maploading. I've
reduced the cost of loading a map by more then 50% now. Get owned.

* Adds a define for maploading tick check

* makes shuttles load again, removes some of the hard limits I had on the reader for profiling

* Macro ops cave generation

Cave generation was insanely more expensive then it had any right to be.
Maybe 0.5 seconds was saved off not doing a range(12) for EVERY SPAWNED
MOB.
0.14 was saved off using expanded weighted lists (A new idea of mine)
This is useful because I can take a weighted list, and condense it into
weight * path count. This is more memory heavy, and costs more to
create, but is so much faster then the proc.

I also added a naive implementation of gcd to make this a bit less bad.
It's not great, but it'll do for this usecase.

Oh and I changed some ChangeTurfs into New()s. I'm still not entirely
sure what the core difference between the two is, but it seems to work
fine.
I believe it's safe because the turf below us hasn't init'd yet, there's
nothing to take from them. It's like 3 seconds faster too so I'll be sad
when it turns out I'm being dumb

* Micros river spawning

This uses the same sort of concepts as the last change, mostly New being
preferable to ChangeTurf at this level of code.
This bit isn't nearly as detailed as the last few, I honestly got a bit
tired. It's still like 0.4 seconds saved tho

* Micros ruin loading

Turns out it saves time if you don't check area type for every tile on a
ruin. Not a whole ton faster, like 0.03, but faster.

Saves even more time (0.1) to not iterate all your ruin's turfs 3 times
to clear away lavaland mobs, when you're IN SPACE who wrote this.

Oh it also saves time to only pull your turf list once, rather then 3
times

---
## [VincentDellmar/SY22-23](https://github.com/VincentDellmar/SY22-23)@[8f12d0c283...](https://github.com/VincentDellmar/SY22-23/commit/8f12d0c2836d0d9cf18152512ed8dd7cfc84216e)
#### Thursday 2022-09-29 02:59:18 by Vincent Dellmar

Collision Engine Still Sucks, But it Works.

Yeah Sprite Sheet Works, Collisions kinda work... could implement basic gameplay, probably will-- but that's tomorrows goal. Then I will make it so multiple objects can spawn, then I will make the collision engine better. then I will add even more objects.

---
## [Wyste/hekili](https://github.com/Wyste/hekili)@[6023ecd8b5...](https://github.com/Wyste/hekili/commit/6023ecd8b56aad73c9b5a3bd5c53aabab94a4290)
#### Thursday 2022-09-29 03:03:42 by Wyste

Update prot war for build 45779

- Talents regenerated from skeleton
- Avatar from 20 to 15 rage gen
- Thunderous roar gens 10 rage (was previously nothing in my version, but should have been 20)
- Piercing Verdict talent modifies Spear of Bastion ability:  went from 50% extra rage gen to 100%
- Shield Slam now gets CD reduction from Honed Reflexes
- Pummel now gets CD reduction from Honed Reflexes (in addition to Concussive Blows too!)

Renames:
- Outburst (talent) renamed to Violent Outburst ( verified spellID did not change )
- Quick Thinking renamed to Wild Strikes (talent)
- The Wall renamed to Impenetrable Wall (talent)
- Spiked Shield renamed to Tough as Nails (talent)
- Siphoning Strikes renamed to Leeching Strikes (talent)

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[f04ab5b5f3...](https://github.com/treckstar/yolo-octo-hipster/commit/f04ab5b5f3b0e3800473a5478fb6eab20522d3fe)
#### Thursday 2022-09-29 03:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[1eab5a8364...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/1eab5a8364114dce9f63c97852461b6e4f27d7b0)
#### Thursday 2022-09-29 03:29:28 by SkyratBot

[MIRROR] Heretics cannot be converted, and are immune to cult stun hands. Instead, the cult is rewarded for sacrificing them with the bloody bastard sword, an oversized SPIN2WIN funblade. + Soul Stealing Fantasy Affix [MDB IGNORE] (#16486)

* Heretics cannot be converted, and are immune to cult stun hands. Instead, the cult is rewarded for sacrificing them with the bloody bastard sword, an oversized SPIN2WIN funblade. + Soul Stealing Fantasy Affix (#69725)

About The Pull Request

Heretics can no longer be converted to a cult, as they follow their own Forgotten Gods.
Instead, Nar'Sie will reward the cult for managing to sacrifice one, with the bastard sword.
The bloody bastard sword has been cleaned up codewise and all that. Because it is a free reward instead of a (removed) progression mechanic of cult, it swings just a bit slower during the spin and doesn't have a jaunt. It's still a !fun! swinging sword of hilarity and death.
BLOODY BASTARD https://www.youtube.com/watch?v=ukznXQ3MgN0
Fantasy weapons can now roll "soul-stealing" weapons. They, on killing something, capture its soul inside the item.

    Add fail conditions that instantly end a spin2win, ala how

    Mimes can now hold a baguette like a sword by right clicking it #69592 works

Why It's Good For The Game

Bloody bastard sword was fun, it made no sense that heretics were valid converts when they're already worshipping a DIFFERENT evil god granting them powers. Should be in a good spot as a nice little antag to antag special interaction. I fucking love antag to antag special interactions, we should have more of 'em

Fantasy affixes are always a neat thing to throw a new component into
Changelog

cl
add: Heretics can no longer be converted to cult. But sacrificing them is very valuable to Nar'Sie, and she will grant special weapons if you manage to do so.
add: Fantasy affixes can also include soul-stealing items!
/cl

* Heretics cannot be converted, and are immune to cult stun hands. Instead, the cult is rewarded for sacrificing them with the bloody bastard sword, an oversized SPIN2WIN funblade. + Soul Stealing Fantasy Affix

Co-authored-by: tralezab <40974010+tralezab@users.noreply.github.com>
Co-authored-by: Tastyfish <crazychris32@gmail.com>

---
## [Superlagg/coyote-bayou](https://github.com/Superlagg/coyote-bayou)@[8a27b0fe9d...](https://github.com/Superlagg/coyote-bayou/commit/8a27b0fe9d5f5f30d2db06246970d76c74cfe00d)
#### Thursday 2022-09-29 04:20:15 by bearrrrrrrrr

i'm KILLING you. i am KILLING y ou. i don't care about anything else i don't give a SHIT about anything else. my programming is just, 'GET THAT FUCKING GUY'

---
## [drawpile/Drawdance](https://github.com/drawpile/Drawdance)@[2d11ed7c87...](https://github.com/drawpile/Drawdance/commit/2d11ed7c87aec27ce0181034bfee91bb5ec4c6ad)
#### Thursday 2022-09-29 04:21:56 by askmeaboutloom

Replace CMocka with custom TAP library

Because CMocka doesn't work properly with Emscripten, reports leaks even
when an assertion fires and is kinda annoying to build. I couldn't find
any sane test framework that I liked, so here's a custom one, sorry. It
can either be run through ctest or through some TAP harness, such as
prove. It doesn't currently fork individual test functions into separate
processes or anything, but there's provisions for producing individual
scripts for each test.

---
## [cooljackal/pytorch](https://github.com/cooljackal/pytorch)@[afcc7c7f5c...](https://github.com/cooljackal/pytorch/commit/afcc7c7f5c7cef740241ff0abdae8d4f2ad22a03)
#### Thursday 2022-09-29 04:37:45 by Andrew Gu

[FSDP] Generalize prefetching; lower unshard/reshard to handle (#83665)

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

Differential Revision: [D39293429](https://our.internmc.facebook.com/intern/diff/D39293429)
Pull Request resolved: https://github.com/pytorch/pytorch/pull/83665
Approved by: https://github.com/zhaojuanmao

---
## [sevenrock/android_kernel_motorola_msm8998](https://github.com/sevenrock/android_kernel_motorola_msm8998)@[d05da58c9c...](https://github.com/sevenrock/android_kernel_motorola_msm8998/commit/d05da58c9c757e68ec1d103ec9b25c0e2757aacf)
#### Thursday 2022-09-29 05:29:35 by Christian Brauner

BACKPORT: signal: add pidfd_send_signal() syscall

The kill() syscall operates on process identifiers (pid). After a process
has exited its pid can be reused by another process. If a caller sends a
signal to a reused pid it will end up signaling the wrong process. This
issue has often surfaced and there has been a push to address this problem [1].

This patch uses file descriptors (fd) from proc/<pid> as stable handles on
struct pid. Even if a pid is recycled the handle will not change. The fd
can be used to send signals to the process it refers to.
Thus, the new syscall pidfd_send_signal() is introduced to solve this
problem. Instead of pids it operates on process fds (pidfd).

/* prototype and argument /*
long pidfd_send_signal(int pidfd, int sig, siginfo_t *info, unsigned int flags);

/* syscall number 424 */
The syscall number was chosen to be 424 to align with Arnd's rework in his
y2038 to minimize merge conflicts (cf. [25]).

In addition to the pidfd and signal argument it takes an additional
siginfo_t and flags argument. If the siginfo_t argument is NULL then
pidfd_send_signal() is equivalent to kill(<positive-pid>, <signal>). If it
is not NULL pidfd_send_signal() is equivalent to rt_sigqueueinfo().
The flags argument is added to allow for future extensions of this syscall.
It currently needs to be passed as 0. Failing to do so will cause EINVAL.

/* pidfd_send_signal() replaces multiple pid-based syscalls */
The pidfd_send_signal() syscall currently takes on the job of
rt_sigqueueinfo(2) and parts of the functionality of kill(2), Namely, when a
positive pid is passed to kill(2). It will however be possible to also
replace tgkill(2) and rt_tgsigqueueinfo(2) if this syscall is extended.

/* sending signals to threads (tid) and process groups (pgid) */
Specifically, the pidfd_send_signal() syscall does currently not operate on
process groups or threads. This is left for future extensions.
In order to extend the syscall to allow sending signal to threads and
process groups appropriately named flags (e.g. PIDFD_TYPE_PGID, and
PIDFD_TYPE_TID) should be added. This implies that the flags argument will
determine what is signaled and not the file descriptor itself. Put in other
words, grouping in this api is a property of the flags argument not a
property of the file descriptor (cf. [13]). Clarification for this has been
requested by Eric (cf. [19]).
When appropriate extensions through the flags argument are added then
pidfd_send_signal() can additionally replace the part of kill(2) which
operates on process groups as well as the tgkill(2) and
rt_tgsigqueueinfo(2) syscalls.
How such an extension could be implemented has been very roughly sketched
in [14], [15], and [16]. However, this should not be taken as a commitment
to a particular implementation. There might be better ways to do it.
Right now this is intentionally left out to keep this patchset as simple as
possible (cf. [4]).

/* naming */
The syscall had various names throughout iterations of this patchset:
- procfd_signal()
- procfd_send_signal()
- taskfd_send_signal()
In the last round of reviews it was pointed out that given that if the
flags argument decides the scope of the signal instead of different types
of fds it might make sense to either settle for "procfd_" or "pidfd_" as
prefix. The community was willing to accept either (cf. [17] and [18]).
Given that one developer expressed strong preference for the "pidfd_"
prefix (cf. [13]) and with other developers less opinionated about the name
we should settle for "pidfd_" to avoid further bikeshedding.

The  "_send_signal" suffix was chosen to reflect the fact that the syscall
takes on the job of multiple syscalls. It is therefore intentional that the
name is not reminiscent of neither kill(2) nor rt_sigqueueinfo(2). Not the
fomer because it might imply that pidfd_send_signal() is a replacement for
kill(2), and not the latter because it is a hassle to remember the correct
spelling - especially for non-native speakers - and because it is not
descriptive enough of what the syscall actually does. The name
"pidfd_send_signal" makes it very clear that its job is to send signals.

/* zombies */
Zombies can be signaled just as any other process. No special error will be
reported since a zombie state is an unreliable state (cf. [3]). However,
this can be added as an extension through the @flags argument if the need
ever arises.

/* cross-namespace signals */
The patch currently enforces that the signaler and signalee either are in
the same pid namespace or that the signaler's pid namespace is an ancestor
of the signalee's pid namespace. This is done for the sake of simplicity
and because it is unclear to what values certain members of struct
siginfo_t would need to be set to (cf. [5], [6]).

/* compat syscalls */
It became clear that we would like to avoid adding compat syscalls
(cf. [7]).  The compat syscall handling is now done in kernel/signal.c
itself by adding __copy_siginfo_from_user_generic() which lets us avoid
compat syscalls (cf. [8]). It should be noted that the addition of
__copy_siginfo_from_user_any() is caused by a bug in the original
implementation of rt_sigqueueinfo(2) (cf. 12).
With upcoming rework for syscall handling things might improve
significantly (cf. [11]) and __copy_siginfo_from_user_any() will not gain
any additional callers.

/* testing */
This patch was tested on x64 and x86.

/* userspace usage */
An asciinema recording for the basic functionality can be found under [9].
With this patch a process can be killed via:

 #define _GNU_SOURCE
 #include <errno.h>
 #include <fcntl.h>
 #include <signal.h>
 #include <stdio.h>
 #include <stdlib.h>
 #include <string.h>
 #include <sys/stat.h>
 #include <sys/syscall.h>
 #include <sys/types.h>
 #include <unistd.h>

 static inline int do_pidfd_send_signal(int pidfd, int sig, siginfo_t *info,
                                         unsigned int flags)
 {
 #ifdef __NR_pidfd_send_signal
         return syscall(__NR_pidfd_send_signal, pidfd, sig, info, flags);
 #else
         return -ENOSYS;
 #endif
 }

 int main(int argc, char *argv[])
 {
         int fd, ret, saved_errno, sig;

         if (argc < 3)
                 exit(EXIT_FAILURE);

         fd = open(argv[1], O_DIRECTORY | O_CLOEXEC);
         if (fd < 0) {
                 printf("%s - Failed to open \"%s\"\n", strerror(errno), argv[1]);
                 exit(EXIT_FAILURE);
         }

         sig = atoi(argv[2]);

         printf("Sending signal %d to process %s\n", sig, argv[1]);
         ret = do_pidfd_send_signal(fd, sig, NULL, 0);

         saved_errno = errno;
         close(fd);
         errno = saved_errno;

         if (ret < 0) {
                 printf("%s - Failed to send signal %d to process %s\n",
                        strerror(errno), sig, argv[1]);
                 exit(EXIT_FAILURE);
         }

         exit(EXIT_SUCCESS);
 }

/* Q&A
 * Given that it seems the same questions get asked again by people who are
 * late to the party it makes sense to add a Q&A section to the commit
 * message so it's hopefully easier to avoid duplicate threads.
 *
 * For the sake of progress please consider these arguments settled unless
 * there is a new point that desperately needs to be addressed. Please make
 * sure to check the links to the threads in this commit message whether
 * this has not already been covered.
 */
Q-01: (Florian Weimer [20], Andrew Morton [21])
      What happens when the target process has exited?
A-01: Sending the signal will fail with ESRCH (cf. [22]).

Q-02:  (Andrew Morton [21])
       Is the task_struct pinned by the fd?
A-02:  No. A reference to struct pid is kept. struct pid - as far as I
       understand - was created exactly for the reason to not require to
       pin struct task_struct (cf. [22]).

Q-03: (Andrew Morton [21])
      Does the entire procfs directory remain visible? Just one entry
      within it?
A-03: The same thing that happens right now when you hold a file descriptor
      to /proc/<pid> open (cf. [22]).

Q-04: (Andrew Morton [21])
      Does the pid remain reserved?
A-04: No. This patchset guarantees a stable handle not that pids are not
      recycled (cf. [22]).

Q-05: (Andrew Morton [21])
      Do attempts to signal that fd return errors?
A-05: See {Q,A}-01.

Q-06: (Andrew Morton [22])
      Is there a cleaner way of obtaining the fd? Another syscall perhaps.
A-06: Userspace can already trivially retrieve file descriptors from procfs
      so this is something that we will need to support anyway. Hence,
      there's no immediate need to add another syscalls just to make
      pidfd_send_signal() not dependent on the presence of procfs. However,
      adding a syscalls to get such file descriptors is planned for a
      future patchset (cf. [22]).

Q-07: (Andrew Morton [21] and others)
      This fd-for-a-process sounds like a handy thing and people may well
      think up other uses for it in the future, probably unrelated to
      signals. Are the code and the interface designed to permit such
      future applications?
A-07: Yes (cf. [22]).

Q-08: (Andrew Morton [21] and others)
      Now I think about it, why a new syscall? This thing is looking
      rather like an ioctl?
A-08: This has been extensively discussed. It was agreed that a syscall is
      preferred for a variety or reasons. Here are just a few taken from
      prior threads. Syscalls are safer than ioctl()s especially when
      signaling to fds. Processes are a core kernel concept so a syscall
      seems more appropriate. The layout of the syscall with its four
      arguments would require the addition of a custom struct for the
      ioctl() thereby causing at least the same amount or even more
      complexity for userspace than a simple syscall. The new syscall will
      replace multiple other pid-based syscalls (see description above).
      The file-descriptors-for-processes concept introduced with this
      syscall will be extended with other syscalls in the future. See also
      [22], [23] and various other threads already linked in here.

Q-09: (Florian Weimer [24])
      What happens if you use the new interface with an O_PATH descriptor?
A-09:
      pidfds opened as O_PATH fds cannot be used to send signals to a
      process (cf. [2]). Signaling processes through pidfds is the
      equivalent of writing to a file. Thus, this is not an operation that
      operates "purely at the file descriptor level" as required by the
      open(2) manpage. See also [4].

/* References */
[1]:  https://lore.kernel.org/lkml/20181029221037.87724-1-dancol@google.com/
[2]:  https://lore.kernel.org/lkml/874lbtjvtd.fsf@oldenburg2.str.redhat.com/
[3]:  https://lore.kernel.org/lkml/20181204132604.aspfupwjgjx6fhva@brauner.io/
[4]:  https://lore.kernel.org/lkml/20181203180224.fkvw4kajtbvru2ku@brauner.io/
[5]:  https://lore.kernel.org/lkml/20181121213946.GA10795@mail.hallyn.com/
[6]:  https://lore.kernel.org/lkml/20181120103111.etlqp7zop34v6nv4@brauner.io/
[7]:  https://lore.kernel.org/lkml/36323361-90BD-41AF-AB5B-EE0D7BA02C21@amacapital.net/
[8]:  https://lore.kernel.org/lkml/87tvjxp8pc.fsf@xmission.com/
[9]:  https://asciinema.org/a/IQjuCHew6bnq1cr78yuMv16cy
[11]: https://lore.kernel.org/lkml/F53D6D38-3521-4C20-9034-5AF447DF62FF@amacapital.net/
[12]: https://lore.kernel.org/lkml/87zhtjn8ck.fsf@xmission.com/
[13]: https://lore.kernel.org/lkml/871s6u9z6u.fsf@xmission.com/
[14]: https://lore.kernel.org/lkml/20181206231742.xxi4ghn24z4h2qki@brauner.io/
[15]: https://lore.kernel.org/lkml/20181207003124.GA11160@mail.hallyn.com/
[16]: https://lore.kernel.org/lkml/20181207015423.4miorx43l3qhppfz@brauner.io/
[17]: https://lore.kernel.org/lkml/CAGXu5jL8PciZAXvOvCeCU3wKUEB_dU-O3q0tDw4uB_ojMvDEew@mail.gmail.com/
[18]: https://lore.kernel.org/lkml/20181206222746.GB9224@mail.hallyn.com/
[19]: https://lore.kernel.org/lkml/20181208054059.19813-1-christian@brauner.io/
[20]: https://lore.kernel.org/lkml/8736rebl9s.fsf@oldenburg.str.redhat.com/
[21]: https://lore.kernel.org/lkml/20181228152012.dbf0508c2508138efc5f2bbe@linux-foundation.org/
[22]: https://lore.kernel.org/lkml/20181228233725.722tdfgijxcssg76@brauner.io/
[23]: https://lwn.net/Articles/773459/
[24]: https://lore.kernel.org/lkml/8736rebl9s.fsf@oldenburg.str.redhat.com/
[25]: https://lore.kernel.org/lkml/CAK8P3a0ej9NcJM8wXNPbcGUyOUZYX+VLoDFdbenW3s3114oQZw@mail.gmail.com/

Cc: "Eric W. Biederman" <ebiederm@xmission.com>
Cc: Jann Horn <jannh@google.com>
Cc: Andy Lutomirsky <luto@kernel.org>
Cc: Andrew Morton <akpm@linux-foundation.org>
Cc: Oleg Nesterov <oleg@redhat.com>
Cc: Al Viro <viro@zeniv.linux.org.uk>
Cc: Florian Weimer <fweimer@redhat.com>
Signed-off-by: Christian Brauner <christian@brauner.io>
Reviewed-by: Tycho Andersen <tycho@tycho.ws>
Reviewed-by: Kees Cook <keescook@chromium.org>
Reviewed-by: David Howells <dhowells@redhat.com>
Acked-by: Arnd Bergmann <arnd@arndb.de>
Acked-by: Thomas Gleixner <tglx@linutronix.de>
Acked-by: Serge Hallyn <serge@hallyn.com>
Acked-by: Aleksa Sarai <cyphar@cyphar.com>

(cherry picked from commit 3eb39f47934f9d5a3027fe00d906a45fe3a15fad)

Conflicts:
        arch/x86/entry/syscalls/syscall_32.tbl - trivial manual merge
        arch/x86/entry/syscalls/syscall_64.tbl - trivial manual merge
        include/linux/proc_fs.h - trivial manual merge
        include/linux/syscalls.h - trivial manual merge
        include/uapi/asm-generic/unistd.h - trivial manual merge
        kernel/signal.c - struct kernel_siginfo does not exist in 4.14
        kernel/sys_ni.c - cond_syscall is used instead of COND_SYSCALL
        arch/x86/entry/syscalls/syscall_32.tbl
        arch/x86/entry/syscalls/syscall_64.tbl

(1. manual merges because of 4.14 differences
 2. change prepare_kill_siginfo() to use struct siginfo instead of
kernel_siginfo
 3. use copy_from_user() instead of copy_siginfo_from_user() in copy_siginfo_from_user_any()
 4. replaced COND_SYSCALL with cond_syscall
 5. Removed __ia32_sys_pidfd_send_signal in arch/x86/entry/syscalls/syscall_32.tbl.
 6. Replaced __x64_sys_pidfd_send_signal with sys_pidfd_send_signal in arch/x86/entry/syscalls/syscall_64.tbl.)

Bug: 135608568
Test: test program using syscall(__NR_pidfd_send_signal,..) to send SIGKILL
Change-Id: I34da11c63ac8cafb0353d9af24c820cef519ec27
Signed-off-by: Suren Baghdasaryan <surenb@google.com>
Signed-off-by: electimon <electimon@gmail.com>

---
## [zoey-on-github/zoey-on-github.github.io](https://github.com/zoey-on-github/zoey-on-github.github.io)@[7c46a0fabc...](https://github.com/zoey-on-github/zoey-on-github.github.io/commit/7c46a0fabc1d8f9cc9ce1865780a7112deda4d01)
#### Thursday 2022-09-29 05:59:54 by zoey-on-github

Update index.html

replaced my ig with my  new new one(fuck you mark zuckerburg)

---
## [ImeevMA/tarantool](https://github.com/ImeevMA/tarantool)@[66ca6252c4...](https://github.com/ImeevMA/tarantool/commit/66ca6252c428ca7a369e24faaa833e3520e809d6)
#### Thursday 2022-09-29 06:41:31 by Alexander Turenko

console: don't mix stdout/stderr with readline prompt

The idea is borrowed from [1]: hide and save prompt, user's input and
cursor position before writing to stdout/stderr and return everything
back afterwards.

Not every stdout/stderr write is handled this way: only tarantool's
logger (when it writes to stderr) and tarantool's print() Lua function
performs the prompt hide/show actions. For example,
`io.stdout:write(<...>)` Lua call or `write(STDOUT_FILENO, <...>)` C
call may mix readline's prompt with actual output. However the logger
and print() is likely enough for the vast majority of usages.

The readline's interactive search state (usually invoked by Ctrl+R) is
not covered by this patch. Sadly, I didn't find a way to properly save
and restore readline's output in this case.

Implementation details
----------------------

Several words about the allocation strategy. On the first glance it may
look worthful to pre-allocate a buffer to store prompt and user's input
data and reallocate it on demand. However rl_set_prompt() already
performs free() plus malloc() at each call[^1], so avoid doing malloc()
on our side would not change the picture much. Moreover, this code
interacts with a human, which is on many orders of magnitude slower that
a machine and will not notice a difference. So I decided to keep the
code simpler.

[^1]: Verified on readline 8.1 sources. However it worth to note that
      rl_replace_line() keeps the buffer and performs realloc() on
      demand.

The code is organized to make say and print modules calling some
callbacks without knowledge about its origin and dependency on the
console module (or whatever else module would implement this interaction
with readline). The downside here is that console needs to know all
places to set the callbacks. OTOH, it offers explicit list of such
callbacks in one place and, at whole, keep the relevant code together.

We can redefine the print() function from every place in the code, but I
prefer to make it as explicit as possible, so added the new internal
print.lua module.

We could redefine _G.print on demand instead of setting callbacks for a
function assigned to _G.print once. The downside here is that if a user
save/capture the old _G.print value, it'll use the raw print() directly
instead of our replacement. Current implementation seems to be more
safe.

Alternatives considered
-----------------------

I guess we can clear readline's prompt and user input manually and don't
let readline know that something was changed (and restore the
prompt/user input afterwards). It would save allocations and string
copying, but likely would lean on readline internals too much and repeat
some of its functionality. I considered this option as unstable and
declined.

We can redefine behavior for all writes to stdout and stderr. There are
different ways to do so:

1. Redefine libc's write() with our own implementation, which will call
   the original libc's write()[^2]. It is defined as a weak symbol in
   libc (at least in glibc), so there is no problem to do so.
2. Use pipe(), dup() and dup2() to execute our own code at
   STDOUT_FILENO, STDERR_FILENO writes.

[^2]: There is a good article about pitfalls on this road: [2]. It is
      about LD_PRELOAD, but I guess everything is very similar with
      wrapping libc's function from an executable.

In my opinion, those options are dangerous, because they implicitly
change behavior of a lot of code, which unlikely expects something of
this kind. The second option (use pipe()) adds more user space/kernel
space context switches, more copying and also would add possible
implicit fiber yield at any `write(STD*_FILENO, <...>)` call -- unlikely
all user's code is ready for that.

Fixes #7169

[1]: https://metacpan.org/dist/AnyEvent-ReadLine-Gnu/source/Gnu.pm
[2]: https://tbrindus.ca/correct-ld-preload-hooking-libc/

NO_DOC=this patch prevents mixing of output streams on a terminal and it
       is what a user actually expects; no reason to describe how bad
       would be his/her life without it

---
## [hexagon-geo-surv/linux-leica](https://github.com/hexagon-geo-surv/linux-leica)@[adee8f3082...](https://github.com/hexagon-geo-surv/linux-leica/commit/adee8f3082b01e5dab620d651e3ec75f57c0c855)
#### Thursday 2022-09-29 06:56:56 by Peter Zijlstra

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
## [SatoriHoshiAiko/openvpn-install-kali-multiple-users](https://github.com/SatoriHoshiAiko/openvpn-install-kali-multiple-users)@[f417b50be9...](https://github.com/SatoriHoshiAiko/openvpn-install-kali-multiple-users/commit/f417b50be95b5c6e280031099ce0c1cf7cfe1d97)
#### Thursday 2022-09-29 07:29:31 by Satori Hoshi-Aiko

Update openvpn-install.sh

Thanks to @nyr for the best script. Just added a few touches as a Kali Debian user, as well as the introduction of duplicate-cn in the server.conf

This helps to add Kali support (but breaks Pre Debian 9, so be careful. Ideally, We are well past using Debian 8 or lower though, all honesty. We could almost call it deprecated except for the backwards compatibility, so be forewarned.

The duplicate-cn in servers.conf is something that should be there anyway, I don't see the average person only wishing to make a single connection without breaking the rest of their connections. If I try to add this to a second device, I can block the original from using the tunnel.

While we can create separate tunnels, this one flag is sufficient to allow the multiple connections we need from other locations. Obviously that is bad for IPsec, because anyone that gets ahold of the servers.conf can have open access to your server of linux host. That is the case anyway, so you really don't want to let your .ovpn get out of your hands. Adding multiple connection effectively broadens the ability for this leaks to become threatening.

Personally, I trust how I store this information, and handle it very carefully, where it isn't already well place in the /root directory anyway. I transfer the .ovpn over an SFTP tunnel, and store it on an encrypted drive in case I need it later.

Absolutely wonderful to have this script!! I am able to use this server's IP address and tunnel  other servers' outbound traffic while also use the same VPN at home. I don't pay for a VPN anymore, but being able to use it and also re-use it simultaneously is, well, amazing.

MY server is a 64GB RAM 12 CPU, and is now my beautiful security OS (Kali, with a lot of custom fireballing, etc) and I can traffic all my connection to my 'work' IP address when desired. This script worked well in comparison to some other examples I tried. I can install it on a VPN router and select devices to traffic to work. And my other server also can reuse it, to proxy one server connection as another, while still being able to have the VPN at home on our router.

I hope these changes were helpful.

@SatoriHoshiAiko

---
## [drahnr/seeding](https://github.com/drahnr/seeding)@[83722b2365...](https://github.com/drahnr/seeding/commit/83722b236504884895555ed8a427c55178859b90)
#### Thursday 2022-09-29 08:52:11 by Kian Paimani

Membership Request (#14)

# Membership Request 

Hi, I am Kian Paimani, known as @kianenigma. I have been working on Polkadot/Kusama through Parity since February 2019 and I can categorize my main contributions to Polkadot's ecosystem as follows: 

1. Maintaining and developing the staking sub-system.
2. General FRAME development, especially testing and quality assurance. 
3. Polkadot-native side-projects. 
4. Education 

> My first contribution to Polkadot is also indeed related to staking: https://github.com/paritytech/substrate/pull/1915

### Staking system

I joke as the Polkadot staking to be both my blessing and my curse over the years. I started working on it since the first days that I joined this ecosystem and the work [is ongoing ever since](https://github.com/orgs/paritytech/projects/33/views/9). In the past, I focused on making sure that the staking system is secure and to some extent scalable. More recently, I coordinated the (imminent) launch of Nomination Pools. Nowadays I also put an extra effort on making sure that this sub-system of Polkadot is *sustainable*, through code refactor and educating other core developers. 

Lastly, I have been the main author of the [Polkadot staking newsletter](https://gist.github.com/kianenigma/aa835946455b9a3f167821b9d05ba376), which is my main attempt at making the entire complexity and development of this part of the protocol transparent to the end-users.

I expect myself to contribute *directly* to the staking system for at least another ~12, if not more, and afterwards having the role of an advisor. 

Some notable contributions: 

- https://github.com/paritytech/substrate/pull/4517
- https://github.com/paritytech/substrate/pull/7910
- https://github.com/paritytech/substrate/issues/6242
- https://github.com/paritytech/substrate/pull/9415
- https://github.com/paritytech/polkadot/pull/3141
- https://github.com/paritytech/substrate/pull/11212
- https://github.com/paritytech/substrate/pull/12129

### FRAME 

Historically, I have contributed a variety of domains in FRAME, namely: 

- Early version of the weight system https://github.com/paritytech/substrate/pull/3816 https://github.com/paritytech/substrate/pull/3157
- Early version of the transaction fee system
- Primitive arithmetic types https://github.com/paritytech/substrate/pull/3456
- Council election pallet https://github.com/paritytech/substrate/pull/3364

Many of which were, admittedly, a PoC at most, if not considered "poor". I am happy that nowadays many of the above have been refactored and are being maintained by new domain experts. 

These days, I put most of my FRAME focus on testing and quality assurance. Through my work in the staking system, I have had to deal with the high sensitivity and liveness requirement of protocol development first hand (I believe I had to do among the [very first storage migrations](https://github.com/paritytech/substrate/pull/3948) in Kusama) and consequently I felt the need to make better testing facilities, all of which have been formulated in https://forum.polkadot.network/t/testing-complex-frame-pallets-discussion-tools/356. Some relevant PRs:

- https://github.com/paritytech/substrate/pull/8038
- https://github.com/paritytech/substrate/pull/9788
- https://github.com/paritytech/substrate/pull/10174

Regardless of wearing the staking hat, I plan to remain a direct contributor to FRAME, namely because I consider it to be an important requirements of successfully delivering more features to Polkadot's ecosystem. 

### Polkadot-Native Side Projects

I have started multiple small, mostly non-RUST projects in the polkadot ecosystem that I am very happy about, and I plan to continue doing so. I have not yet found the time to make a "polished product" out of any of these, but I hope that I can help foster our community such that someday a team will do so. I consider my role, for the time being, to *put ideas out there* through these side projects. 

- https://github.com/substrate-portfolio/polkadot-portfolio/
- https://github.com/kianenigma/polkadot-basic-notification/
- https://github.com/paritytech/polkadot-scripts/
- https://github.com/paritytech/substrate-debug-kit/

### Education 

Lastly, aside from having had a number of educational talks over the years (all of which [are listed](https://hello.kianenigma.nl/talks/) in my personal website), I am a big enthusiast of the newly formed Polkadot Blockchain Academy. I have [been an instructor](https://singular.app/collectibles/statemine/16/2) in the first cohort, and continue to contribute for as long and as much as I can, whilst still attending to the former 3 duties. 

---

With all of that being said and done, I consider myself at the beginning of the path to Dan 4, but happy to start at a lower one as well.

Co-authored-by: Bastian Köcher <git@kchr.de>

---
## [aslenofarid/kernel_asus_sdm660](https://github.com/aslenofarid/kernel_asus_sdm660)@[df3c435c42...](https://github.com/aslenofarid/kernel_asus_sdm660/commit/df3c435c42e14af1dd4a7768512e8ba8bd0174f5)
#### Thursday 2022-09-29 09:12:40 by Dan Pasanen

power: don't ever reboot to verity red

* We get it, shit's broken. We're flashing custom stuff, shit's bound
  to break. Don't pop this annoying screen up, we're not even using
  verity anyway.

Change-Id: Icd77b70ec1df9108a4ba9e7fd8cb9623b35b78db
Signed-off-by: Albert I <kras@raphielgang.org>
Signed-off-by: aslenofarid <yoniasleno.farid14@gmail.com>

---
## [ImGGAAVVIINN/Aleph-0](https://github.com/ImGGAAVVIINN/Aleph-0)@[d41f4ae0d6...](https://github.com/ImGGAAVVIINN/Aleph-0/commit/d41f4ae0d66807ab4f343308c8edaf9fa11a4804)
#### Thursday 2022-09-29 11:14:40 by Happy GrassBlock

Add a whole ton of shit and Fly hack

Added fuck tons of things to the client, and also added fly hack! :D
To enable it, press the 'n' key in survival mode. and double click space bar. Then off you go!

---
## [Stalkeros2/Skyrat-tg](https://github.com/Stalkeros2/Skyrat-tg)@[deb87e9ec0...](https://github.com/Stalkeros2/Skyrat-tg/commit/deb87e9ec07fb6caff47cabaa8b5fdd760ea975b)
#### Thursday 2022-09-29 12:13:51 by SkyratBot

[MIRROR] Fixes gravity pulse and transparent floor plane sharing a layer [MDB IGNORE] (#16446)

* Fixes gravity pulse and transparent floor plane sharing a layer (#70124)

fixes gravity pulse and transparent floor plane sharing a layer

Broken by #69642 , sorry
I'll open up a seperate PR later today with a unit test to catch these cases
(my later today is in like 10 hours)

closes #70123 (weird fucking floors)

* Fixes gravity pulse and transparent floor plane sharing a layer

Co-authored-by: Time-Green <timkoster1@hotmail.com>

---
## [LikeLion-at-Skhu-10/Play_in_Youth](https://github.com/LikeLion-at-Skhu-10/Play_in_Youth)@[00c68e3f15...](https://github.com/LikeLion-at-Skhu-10/Play_in_Youth/commit/00c68e3f151631788f6e261f43c2df8c201da39d)
#### Thursday 2022-09-29 13:02:36 by 김수진

entire_commit_Don't touch this file if you touch this file and then fuck you

---
## [krovostok/defeated-sanity](https://github.com/krovostok/defeated-sanity)@[0d69ab12bf...](https://github.com/krovostok/defeated-sanity/commit/0d69ab12bfbc2116df4bda5da896d28f7c4c87fc)
#### Thursday 2022-09-29 13:11:56 by olezha baranov

make eyes add and spit blood tears every 1s
also make fuck tomas mom

---
## [dongbinghua/terminal](https://github.com/dongbinghua/terminal)@[9ccd6ecd74...](https://github.com/dongbinghua/terminal/commit/9ccd6ecd744890b856f3d8a39ff0616c0e34d4fb)
#### Thursday 2022-09-29 13:16:54 by Mike Griese

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
## [JuniorNovoa1/Nike-Engine](https://github.com/JuniorNovoa1/Nike-Engine)@[7bb175ce77...](https://github.com/JuniorNovoa1/Nike-Engine/commit/7bb175ce77e23df4d9c4af011e66cb698d23c082)
#### Thursday 2022-09-29 14:55:38 by BushsHaxs

Revert "Fuck Online me and the boys hate online i also added polymod mods"

This reverts commit 9bde8697eae91b6657afefd3afce2ed9e66ef604.

---
## [MarcoFalke/bitcoin-core](https://github.com/MarcoFalke/bitcoin-core)@[3a7e0a210c...](https://github.com/MarcoFalke/bitcoin-core/commit/3a7e0a210c86e3c1750c7e04e3d1d689cf92ddaa)
#### Thursday 2022-09-29 16:33:19 by glozow

Merge bitcoin/bitcoin#24513: CChainState -> Chainstate

00eeb31c7660e2c28f189f77a6905dee946ef408 scripted-diff: rename CChainState -> Chainstate (James O'Beirne)

Pull request description:

  Alright alright alright, I know: we hate refactors. We especially hate cosmetic refactors.

  Nobody knows better than I that changing broad swaths of code out from under our already-abused collaborators, only to send a cascade of rebase bankruptcies, is annoying at best and sadistic at worst. And for a rename! The indignation!

  But just for a second, imagine yourself. Programming `bitcoin/bitcoin`, on a sandy beach beneath a lapis lazuli sky. You go to type the name of what is probably the most commonly used data structure in the codebase, and you *only hit shift once*.

  What could you do in such a world? You could do anything. [The only limit is yourself.](https://zombo.com/)

  ---

  So maybe you like the idea of this patch but really don't want to deal with rebasing. You're in luck!

  Here're the commands that will bail you out of rebase bankruptcy:

  ```sh
  git rebase -i $(git merge-base HEAD master) \
    -x 'sed -i "s/CChainState/Chainstate/g" $(git ls-files | grep -E ".*\.(py|cpp|h)$") && git commit --amend --no-edit'
  # <commit changed?>
  git add -u && git rebase --continue
  ```

  ---

  ~~Anyway I'm not sure how serious I am about this, but I figured it was worth proposing.~~ I have decided I am very serious about this.

  Maybe we can have nice things every once in a while?

ACKs for top commit:
  MarcoFalke:
    cr ACK 00eeb31c7660e2c28f189f77a6905dee946ef408
  hebasto:
    ACK 00eeb31c7660e2c28f189f77a6905dee946ef408
  glozow:
    ACK 00eeb31c7660e2c28f189f77a6905dee946ef408, thanks for being the one to propose this
  w0xlt:
    ACK https://github.com/bitcoin/bitcoin/pull/24513/commits/00eeb31c7660e2c28f189f77a6905dee946ef408

Tree-SHA512: b828a99780614a9b74f7a9c347ce0687de6f8d75232840f5ffc26e02bbb25a3b1f5f9deabbe44f82ada01459586ee8452a3ee2da05d1b3c48558c8df6f49e1b1

---
## [Striders13/tgstation](https://github.com/Striders13/tgstation)@[d45e244401...](https://github.com/Striders13/tgstation/commit/d45e244401425d34edc38e3dd2f3c2bbdbcec7ce)
#### Thursday 2022-09-29 16:52:28 by san7890

Crab-17 No Longer Breaks Economy If You Swipe Too Fast (#70094)

Hey there,

Remember swiping credit cards, before everything was chipped? You know how sometimes if you went too slow, the transaction might fail, the cashier had to plonk in some digits on their machine, and you had to go again? That kinda sucked.

If you're too young to get that reference, just imagine the card swiping task in AMONG US. Doesn't that minigame suck? You know exactly what that is. Same principle.

Anyways, that's pretty much what was going on here. The reason why SS.Economy would break so god damn hard if you swiped an ID before the machine's "boot up" slowflake animation was complete is probably due to the line where it starts fast processing. I added an early return to check for if the animation was complete by leveraging a var we already set at the end of the process, because I am lazy.

There's probably a few other ways you can tackle this issue, but this feels right to me in a thematic sense. I'm willing to change it if needed though.

---
## [Striders13/tgstation](https://github.com/Striders13/tgstation)@[9b9337de49...](https://github.com/Striders13/tgstation/commit/9b9337de493ec62927f15b0ee18f9342cd3c2d04)
#### Thursday 2022-09-29 16:52:28 by Tim

Add speech modifier to zombie tongue (#69899)


About The Pull Request

A zombie rotten tongue has a complex language modifier.
The language modifier works by:

    All occurrences of characters "eiou" (case-insensitive) are replaced with "r".
    All characters other than "zhrgbmna .!?-" (case-insensitive) are stripped.
    Multiple spaces are replaced with a single.
    Lower-case "r" at the end of words replaced with "rh".
    An "a" or "A" by itself will be replaced with "hra".
    The first character is capitalised.

Some interesting dialogue examples:

    Bab, am gaa habbah abah zah namrh ah Bh!rh!b?
    Bob, are you happy about the death of Philip?

    Zah bang bang man ganna harm mah zambah?
    Will the Zombie Hunter attack me?

    Mah zambah nah harm brazzarz.
    I do not hurt brothers.

    Mah zambah ganna gangbang harmanz zammarrar.
    I will kill humans tomorrow.

    Mah zambah am nah habbah, an mah zambah gab, -Graaaagh!-
    I am not happy, and I say "Graaaagh!"

The language idea was taken from a zombie game back in 2005 called Urban Dead. It's no longer developed and I made all the code myself while following the given language rule structures.

Zombie Speech Translator
Zombie Language Examples
Zombie Dictionary
Why It's Good For The Game
Abracadabra - The Steve Miller Band

    Ah raab zha brahnz ahn zarh hagh, (I love the brains in your head)
    Ah ganna barg abgrah gangbang, (I'm gonna eat them when you're dead)
    Az rahnah zarh ranz ahn hahg ahahz, (Now as you run and hide away)
    Zarh harh mah zambah az hah zahz: (You hear my zombie as he says:)
    Abra-abra-gababra, (Abra-abra-cadabra)
    Ah ganna rahg arg ahn grab zarh! (I'm gonna reach out and grab ya!)
    Abra-abra-gababra, (Abra-abra-cadabra)
    Ah ganna rahg arg ahn grab zarh! (I'm gonna reach out and grab ya!)

Changelog

cl
add: Rotten zombie tongue has a new speech modifier that converts spoken language into zombie sentences. If the person speaking is a high-functioning zombie this is bypassed.
/cl

---
## [Plum-but-gayer/Skyrat-tg](https://github.com/Plum-but-gayer/Skyrat-tg)@[79b4a74a6e...](https://github.com/Plum-but-gayer/Skyrat-tg/commit/79b4a74a6e6f13128779f88cb784ecb1e5989524)
#### Thursday 2022-09-29 16:57:43 by RimiNosha

[MODULAR] Fixes That Stupid Language Reset Bug That's Been Here Since Newprefs (#15802)

* I hate coders
This includes myself.

* Web edit~

* I give up, this is the best I got

* Make species take their alternate language instead of uncommon! Make language selection reflect foreigner, if selected!

* Remove code that assumed old foreigner add proc was called

* whyaremidroundspawnshandleddifferentlythanroundstartswhatthefuck

* Apply suggestion!

Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>

* Address last review at long last

* Apply suggestions!

Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>

Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>

---
## [Maurlcio/holbertonschool-low_level_programming](https://github.com/Maurlcio/holbertonschool-low_level_programming)@[61b51d086f...](https://github.com/Maurlcio/holbertonschool-low_level_programming/commit/61b51d086f731b2d4fe8ac9a43bf60e49edb0a13)
#### Thursday 2022-09-29 17:09:54 by Maurlcio

computes the absolute value of any integer, which is basically just saying 'is this positive? no? well fuck you now you are'

---
## [EsotericUnderstandings/My-teacher-made-me-do-this](https://github.com/EsotericUnderstandings/My-teacher-made-me-do-this)@[da639695fe...](https://github.com/EsotericUnderstandings/My-teacher-made-me-do-this/commit/da639695feadbee728f2b0d251c934ba6352b322)
#### Thursday 2022-09-29 18:41:15 by EsotericUnderstandings

My teacher cant fucking spell for shit

AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH...

---
## [gadget-inc/dateilager](https://github.com/gadget-inc/dateilager)@[4348da1c34...](https://github.com/gadget-inc/dateilager/commit/4348da1c3488187e0d209ebd89a69ffa5adad753)
#### Thursday 2022-09-29 19:23:47 by Harry Brundage

Recover from arbitrary errors writing files by removing the thing we're about to write

I encountered a sequence of changes that DL didn't expect where I was creating a symlink at a path that was previously a folder full of files. There's a bunch of other annoying cases like this, where we should be able to go from any state on disk to any new incoming object type. The existing strategy did a bit of checking to see if stuff wasn't quite right, but I think we aught to be a bit more robust. The recovery strategy is always the same if we have a new incoming object: delete whatever is there so we can just write the new thing on top. If we're gonna do that, I think we can do it a bit more blindly. Instead of checking ahead of time for erroneous conditions (which also requires another syscall every write), we just blindly try to do the thing we need to do, and if it fails, remove whatever is there and try again. That way, we don't need to anticipate whatever fucked up case is on disk at the time and instead just blow it away. I also like this because it makes the fast path a bit faster where we do less checking up front and just let the kernel tell us we're doing something weird.

---
## [ellingtonia/ellingtonia](https://github.com/ellingtonia/ellingtonia)@[b9a43fa4ac...](https://github.com/ellingtonia/ellingtonia/commit/b9a43fa4ace8ea382c38e0458e0aad244b089361)
#### Thursday 2022-09-29 20:07:27 by Charlie Dyson

Changed the ordering of DE2812a-c to place "The Mooche" at "c". This matches the Centennial edition.

CD:
The ordering of DE2812a-f [in your Centennial document] doesn't match what's on
Ellingtonia. e.g. Ellingtonia has DE2812a as The Mooch but you have it as Santa
Claus. I suspect Ellingtonia is wrong here and The Mooch needs moving down to
after "I done Caught" / before "I can't give"?

EC:

I used as a reference, the New DESOR Correction Sheets 3002, 3003, 3004m that
list the RCA Centennial Edition.
Here is pasted from NDCS 3002 the track list of the first two CDs: in bold I highlighted the 2812 session.

A01·If You Can't Hold The Man You Love(2701b):A02-Washington Wabble(2708b);A03·Washington Wabble(2708c):A04-Black And TanFantasy(2709a):A05-Washington Wabble(2709b):A06-Creole Love Call(2709c):A07-The Blues I Love To Sing(2709d):A08·The Blues Love To Sing(270ge):A09-Harlem River Quiver(2712a):AI0·Harlem River Quiver(2712b);AII-Harlem River Quiver(2712c):A12·East St.Louis Toodle·O(2712d):A13·Blue Bubbles(2712e):A14·Blue Bubbles(2712f);A15·Black Beauty(2805a):A16-Jubilee Stomp(2805b); A17·Got Everything But You(2805c):**A18-Santa Claus,Bring My Man Back To Me(2812a):A19-I Done Caught You Blues(2812b):A20·The Mooche(2812c) .

B01·I Can't Give You Anything But Love(2812d);B02·No Papa No(2812e)**;B03·No Papa No(2812f);B04-I Can't Give You Anything ButLove(2813a);B05·Bandanna Babies(2814a):B06-Diga Diga Doo(2814b);B07-I Must Have -rhat Man(2814c):B08-St.Louis Blues(2819a); B09·St.Louis Blues(2819b):B10·St.Louis Blues(2819c);Bll-Flaming Youth(2902a);B12-Flaming Youth(2902b):B13-Saturday Night Function(2902c) ;B14-High Life(2902d);B15-Doin' The Voom Voom(2902e):B16-Doin' 'rhe Voom Voom(2902f):B17·Japanese Dream(2903a) :B18·Harlemania(2903b) .

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[845b3ae598...](https://github.com/treckstar/yolo-octo-hipster/commit/845b3ae598423328a8cd6d43318de31322ef6503)
#### Thursday 2022-09-29 20:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [swordcube/FNF-Plasma-Engine](https://github.com/swordcube/FNF-Plasma-Engine)@[998c3be3c7...](https://github.com/swordcube/FNF-Plasma-Engine/commit/998c3be3c7ba5282216205f17377bf02a8d57ccc)
#### Thursday 2022-09-29 20:36:40 by swordcube

using yoshi crafter flixel lib now, it's so much fucking faster holy shit

---
## [microsoft/terminal](https://github.com/microsoft/terminal)@[b4b6636b49...](https://github.com/microsoft/terminal/commit/b4b6636b4952ac8ff6a9864f641973bb49d91ce4)
#### Thursday 2022-09-29 20:56:31 by Mårten Rånge

Relax shader strictness in RELEASE mode (#13998)

Disables strictness and warnings as errors for custom pixel shaders in
RELEASE. Windows terminal is not telling the user why the shader won't
compile which makes it very frustrating for the shader hacker.

After trying the recent preview none of my shaders loaded anymore in
Windows Terminal Preview which made me very sad. I had no idea what was
wrong with them. After cloning the git repo, building it, fighting an
issue that prevent DEBUG SDK from being used I finally was able to
identify some issues that were blocking my shaders.

> error X3556: integer modulus may be much slower, try using uints if possible.
> error X4000: use of potentially uninitialized variable (rayCylinder)

While the first one is a good warning I don't think it is an error and
the tools I use didn't flag it so was hard to know.

The second one I was staring at the code and was unable to identify what
exactly was causing the issues, I fumbled with the code a few times and
just felt the fun drain away.

IMHO: I want it to be fun to develop shaders for windows terminal.
Fighting invisible errors are not fun. I am not after building
production shaders for Windows Terminal, I want some cool effects. So
while I am as a .NET developer always runs with Warning as errors I
don't think it's the right option here. Especially since Windows
Terminal doesn't tell what is the problem.

However, I understand if the shaders you ship with Windows Terminal
should be free of errors and silly mistakes, so I kept the stricter
setting in DEBUG mode.

## Validation Steps Performed

Loaded Windows Terminal in RELEASE and DEBUG mode and validated that
RELEASE mode had reduced strictness but DEBUG retained the previous more
restrictive mode.

---
## [RosieSapphire/Hungover](https://github.com/RosieSapphire/Hungover)@[da9277f7c7...](https://github.com/RosieSapphire/Hungover/commit/da9277f7c745d77b0030a6db78fc0b18d62e90a0)
#### Thursday 2022-09-29 21:45:10 by Rosie Sapphire

Holy fucking shit we have normal mapping now. For reals this time

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[ee1aba7a32...](https://github.com/tgstation/tgstation/commit/ee1aba7a32d73a32694fcf904e166e7985df6676)
#### Thursday 2022-09-29 21:53:07 by John Willard

pumping your heart doesnt require to be conscious (#63290)

Simply removes the requirement to be conscious to pump your blood with a cursed heart.
Why It's Good For The Game

Entering crit or falling asleep is basically a life sentence since you are unable to pump your blood while asleep. The player still is manually pumping it, I don't see any reason why the user has to be awake for it.
This also means medical can't revive you, as you'll instantly lose all your blood before you have enough time to wake up to start pumping again. The only IC fix would be to remove your heart entirely, something most doctors wouldn't even notice.
Changelog

cl
fix: You can manually pump your blood while asleep/in crit, rather than instantly lose all your blood and die forever.
/cl

---
## [darcys22/loki-core](https://github.com/darcys22/loki-core)@[6920fbe637...](https://github.com/darcys22/loki-core/commit/6920fbe637e460142ccb00ae681dd75c3d8d69cf)
#### Thursday 2022-09-29 21:55:35 by Jason Rhinelander

Add garbage to make it work on a garbage OS

- Don't touch <fmt/std.h> because it touches std::filesystem which makes
  macOS throw a hissy fit and refuse to compile.
- int_to_string is broken on macOS because it uses std::to_chars which
  makes macos throw a hissy fit like a cranky old female cat seeing a
  kitten if it sees it.
- wallet3 was using std::filesystem and std::visit, both of which make
  macos throw a hissy fit.  (There is a pattern here).  Apply the dumb
  fs::path and var::visit workarounds needed to appease this garbage OS.
- use var::get (from oxenc/variant.h) instead of std::get because, oh
  yeah, we need to support a garbage OS that Apple themselves don't even
  properly support.  Yay!

---
## [justinpryzby/postgres](https://github.com/justinpryzby/postgres)@[25a98dcbe7...](https://github.com/justinpryzby/postgres/commit/25a98dcbe7e143c17d69d17a2051ff1f7ec76c18)
#### Thursday 2022-09-29 22:28:52 by Tomas Vondra

Showing applied extended statistics in explain

Hi,

With extended statistics it may not be immediately obvious if they were
applied and to which clauses. If you have multiple extended statistics,
we may also apply them in different order, etc. And with expressions,
there's also the question of matching expressions to the statistics.

So it seems useful to include this into in the explain plan - show which
statistics were applied, in which order. Attached is an early PoC patch
doing that in VERBOSE mode. I'll add it to the next CF.

A simple example demonstrating the idea:

======================================================================

  create table t (a int, b int);
  insert into t select mod(i,10), mod(i,10)
    from generate_series(1,100000) s(i);

  create statistics s on a, b from t;
  analyze t;

test=# explain (verbose) select * from t where a = 1 and b = 1;
                          QUERY PLAN
---------------------------------------------------------------
 Seq Scan on public.t  (cost=0.00..1943.00 rows=10040 width=8)
   Output: a, b
   Filter: ((t.a = 1) AND (t.b = 1))
   Statistics: public.s  Clauses: ((a = 1) AND (b = 1))
(4 rows)

test=# explain (verbose) select 1 from t group by a, b;
                              QUERY PLAN
----------------------------------------------------------------------
 HashAggregate  (cost=1943.00..1943.10 rows=10 width=12)
   Output: 1, a, b
   Group Key: t.a, t.b
   ->  Seq Scan on public.t  (cost=0.00..1443.00 rows=100000 width=8)
         Output: a, b
         Statistics: public.s  Clauses: (a AND b)
(6 rows)

======================================================================

The current implementation is a bit ugly PoC, with a couple annoying
issues that need to be solved:

1) The information is stashed in multiple lists added to a Plan. Maybe
there's a better place, and maybe we need to invent a better way to
track the info (a new node stashed in a single List).

2) The deparsing is modeled (i.e. copied) from how we deal with index
quals, but it's having issues with nested OR clauses, because there are
nested RestrictInfo nodes and the deparsing does not expect that.

3) It does not work for functional dependencies, because we effectively
"merge" all functional dependencies and apply the entries. Not sure how
to display this, but I think it should show the individual dependencies
actually applied.

4) The info is collected always, but I guess we should do that only when
in explain mode. Not sure how expensive it is.

5) It includes just statistics name + clauses, but maybe we should
include additional info (e.g estimate for that combination of clauses).

6) The clauses in the grouping query are transformed to AND list, which
is wrong. This is easy to fix, I was lazy to do that in a PoC patch.

7) It does not show statistics for individual expressions. I suppose
examine_variable could add it to the rel somehow, and maybe we could do
that with index expressions too?

regards

--
Tomas Vondra
EnterpriseDB: http://www.enterprisedb.com
The Enterprise PostgreSQL Company

From 4629d1d9b1fc5f6c3bc93e0544b0c022345086c9 Mon Sep 17 00:00:00 2001
From: Tomas Vondra <tomas.vondra@postgresql.org>
Date: Thu, 18 Mar 2021 15:09:24 +0100
Subject: [PATCH] show stats in explain

---

