## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-08-31](docs/good-messages/2022/2022-08-31.md)


2,179,989 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,179,989 were push events containing 3,240,358 commit messages that amount to 249,290,307 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 41 messages:


## [postgresql-cfbot/postgresql](https://github.com/postgresql-cfbot/postgresql)@[7fed801135...](https://github.com/postgresql-cfbot/postgresql/commit/7fed801135bae14d63b11ee4a10f6083767046d8)
#### Wednesday 2022-08-31 00:01:14 by Tom Lane

Clean up inconsistent use of fflush().

More than twenty years ago (79fcde48b), we hacked the postmaster
to avoid a core-dump on systems that didn't support fflush(NULL).
We've mostly, though not completely, hewed to that rule ever since.
But such systems are surely gone in the wild, so in the spirit of
cleaning out no-longer-needed portability hacks let's get rid of
multiple per-file fflush() calls in favor of using fflush(NULL).

Also, we were fairly inconsistent about whether to fflush() before
popen() and system() calls.  While we've received no bug reports
about that, it seems likely that at least some of these call sites
are at risk of odd behavior, such as error messages appearing in
an unexpected order.  Rather than expend a lot of brain cells
figuring out which places are at hazard, let's just establish a
uniform coding rule that we should fflush(NULL) before these calls.
A no-op fflush() is surely of trivial cost compared to launching
a sub-process via a shell; while if it's not a no-op then we likely
need it.

Discussion: https://postgr.es/m/2923412.1661722825@sss.pgh.pa.us

---
## [KDr2/rust](https://github.com/KDr2/rust)@[15e2e5185a...](https://github.com/KDr2/rust/commit/15e2e5185a22207b18d2cbc47a48b39e63e84cd0)
#### Wednesday 2022-08-31 00:02:40 by Dylan DPC

Rollup merge of #100473 - compiler-errors:normalize-the-fn-def-sig-plz, r=lcnr

Attempt to normalize `FnDef` signature in `InferCtxt::cmp`

Stashes a normalization callback in `InferCtxt` so that the signature we get from `tcx.fn_sig(..).subst(..)` in `InferCtxt::cmp` can be properly normalized, since we cannot expect for it to have normalized types since it comes straight from astconv.

This is kind of a hack, but I will say that `@jyn514` found the fact that we present unnormalized types to be very confusing in real life code, and I agree with that feeling. Though altogether I am still a bit unsure about whether this PR is worth the effort, so I'm open to alternatives and/or just closing it outright.

On the other hand, this isn't a ridiculously heavy implementation anyways -- it's less than a hundred lines of changes, and half of that is just miscellaneous cleanup.

This is stacked onto #100471 which is basically unrelated, and it can be rebased off of that when that lands or if needed.

---

The code:
```rust
trait Foo { type Bar; }

impl<T> Foo for T {
    type Bar = i32;
}

fn foo<T>(_: <T as Foo>::Bar) {}

fn needs_i32_ref_fn(f: fn(&'static i32)) {}

fn main() {
    needs_i32_ref_fn(foo::<()>);
}
```

Before:
```
   = note: expected fn pointer `fn(&'static i32)`
                 found fn item `fn(<() as Foo>::Bar) {foo::<()>}`
```

After:
```
   = note: expected fn pointer `fn(&'static i32)`
                 found fn item `fn(i32) {foo::<()>}`
```

---
## [YGOREV001/ygorev](https://github.com/YGOREV001/ygorev)@[ffcfbb35bc...](https://github.com/YGOREV001/ygorev/commit/ffcfbb35bcd979cea252b778b0b5d1c581fa3f8a)
#### Wednesday 2022-08-31 01:09:02 by YGOREV001

Ajustes 20220830

Bugs:

Change Slime -> Ajuste texto BD	OK
Archfiend Marmot of Nefariousness -> Ajuste texto BD	OK
Unknown Warrior of Fiend -> Ajuste texto BD	OK
Hero of the East -> Ajuste LV en BD	OK
Fiend Reflection #1 y #2 -> Ajustes texto BD	OK
Winged Egg of New Life -> Ajuste texto BD	OK

******************
Cambios Stats:

Warrior Lady of Tradition -> Cambio ATK: 2150 > 1900	OK

******************
Cambios Efectos:

Fire-eating Giant Tutrle:
Antes: ●[OPT] You can Tribute 1 FIRE monster from your hand or field; this card gains 800 ATK until the end of the next turn. ●If this card in Attack Position is attacked: You can change it to Defense Position, and if you do, inflict 800 damage to your opponent.
Despues: ●[OPT] You can Tribute 1 FIRE monster from your hand or field; this card gains 1000 ATK until the end of the next turn. ●If this card in Attack Position is attacked: You can change it to Defense Position, and if you do, inflict 1500 damage to your opponent.

Garvas:
Antes: ●If this card battles a DARK or EARTH monster, this card gains 1000 ATK/DEF during damage calculation only.
Despues: ●[OPT] At the start of the Damage Step, if this card battles a face-up DARK or EARTH monster: Destroy that monster.

Turtle Tiger:
Antes: ●If this card destroys an opponent's monster by battle and sends it to the Graveyard: You can add 1 Level 4 or lower Beast or WATER monster from your Deck to your hand.
Despues: ●If this card destroys an opponent's monster by battle and sends it to the Graveyard: You can add 1 Level 4 or lower Beast or Beast-Warrior monster from your Deck to your hand.

Flower Wolf:
Antes:●If this card destroys an opponent's monster by battle and sends it to the Graveyard: Inflict 1000 damage to your opponent.
Despues:●If this card destroys an opponent's monster by battle and sends it to the Graveyard: Inflict 1500 damage to your opponent.

Two-Headed King Rex:
Antes: ●Gains 200 ATK for each monster your opponent controls.
Despues: ●Gains 200 ATK for each card your opponent controls.

Twin-Headed Thunder Dragon:
ADD: ●[OPT] You can reveal 1 Thunder monster from your hand, until the End Phase; this card can make a second attack during each Battle Phase this turn.

Skull Knight:
ADD: ●[OPT] You can discard 1 card; Special Summon 1 Level 3 Fiend or Warrior monster from your hand or Deck in Defense Position.

Thousand-Eyes Restrict:
Antes: ●"Relinquished" must be on the field to Fusion Summon this card.
Despues: ●All Fusion Materials must to be on the field to Fusion Summon this card.

---
## [xfnw/solanum](https://github.com/xfnw/solanum)@[a90f22c92d...](https://github.com/xfnw/solanum/commit/a90f22c92d23160b6949df4770c839994fcd6a93)
#### Wednesday 2022-08-31 01:26:40 by Aaron Jones

OpenSSL: Support configuration of TLSv1.3 ciphersuites

The OpenSSL developers decided, during the OpenSSL 1.1.1 development
phase, to use a different API and different set of lists for TLSv1.3
ciphersuites, than for every TLS version preceeding it.

This is stupid, but we have to work with it.

This commit also improves configuration fault resilience. The reason
is that if you don't pass any valid old-style ciphersuites, OpenSSL
will not negotiate an older protocol at all. However, when they
implemented the new API, they decided that lack of any valid
ciphersuites should result in using the defaults. This means that if
you pass a completely invalid ciphersuite list (like "foo"), OR if
you pass a TLSv1.2-only ciphersuite list, TLSv1.3 continues to work.
This is not mirrored; passing a TLSv1.3-only ciphersuite list will
break TLSv1.2 and below.

Therefore we work around this lack of mirroring by falling back to
the default list for each protocol. This means that if
ssl_cipher_list is complete garbage, the default will be used, and
TLS setup will succeed for both protocols. This is logged, so that
administrators can fix their configuration.

I prefer this approach over explicitly disabling the protocols if
their respective ciphersuite lists are invalid, because it will
result in unusable TLSv1.3 if people run newer solanum with their
older charybdis/solanum configuration files that contain custom
ssl_cipher_list definitions. Hindering TLSv1.3 adoption is not an
option, in my opinion.

The downside of this is that it is no longer possible to disable a
protocol family by not including any of its ciphersuites. This could
be remedied by an ssl_protocol_list configuration directive if it is
decided that this functionality is ultimately necessary.

This work is not required for either of the other TLS backends,
because neither of those libraries yet support TLSv1.3, and in the
event that they eventually do, I expect them to allow configuration
of newer ciphersuites with the existing APIs. This can be revisited
if it turns out not to be the case.

Signed-off-by: Aaron Jones <me@aaronmdjones.net>
Tested-by: Aaron Jones <me@aaronmdjones.net>

---
## [killer7luis/lobotomy-corp13](https://github.com/killer7luis/lobotomy-corp13)@[bcef210058...](https://github.com/killer7luis/lobotomy-corp13/commit/bcef210058640bacf0979fb9be47fbe4ae1f1dc9)
#### Wednesday 2022-08-31 01:39:28 by Killer7luis

my beloved

aaa

We can change anything abno

We can change anything!

If you're creative enough, even a tool abno like this fucking garbage can be fun!

i forgor...

gigachad fix

im awesome

more change fixes

Update zayin.dm

amazing

Update suit.dmi

---
## [botisan-ai/vf-general-runtime](https://github.com/botisan-ai/vf-general-runtime)@[5722ab44e2...](https://github.com/botisan-ai/vf-general-runtime/commit/5722ab44e2ab100cd8c68840083861c47afa1567)
#### Wednesday 2022-08-31 02:15:32 by Tyler Han

fix: api debug messages (VF-3263) (#309)

<!-- You can erase any parts of this template not applicable to your Pull Request. -->

**Fixes or implements VF-3263**

### Brief description. What is this change?
So it turns out when you `stringify` a `VError` you actually don't get the error message, but everything else, which is kinda stupid. 

BEFORE:
![Screen Shot 2022-04-16 at 12 35 07 AM](https://user-images.githubusercontent.com/5643574/163676644-717b2998-7dd4-49b8-a0d8-bffd04151e47.png)


AFTER:
![Screen Shot 2022-04-16 at 12 31 32 AM](https://user-images.githubusercontent.com/5643574/163661454-767cd019-57c7-4630-9e59-4d48e1adaf64.png)

I also updated the debug message so if you get a >400 response on the API call, we show the body too.

---
## [Sharkalien/Godot-YOU-THERE.-BOY.-Walkaround](https://github.com/Sharkalien/Godot-YOU-THERE.-BOY.-Walkaround)@[033f3a1f61...](https://github.com/Sharkalien/Godot-YOU-THERE.-BOY.-Walkaround/commit/033f3a1f61eb0138c8adccbbd4cb275837e9df1d)
#### Wednesday 2022-08-31 02:19:43 by Leo Esc

Delete stupid fucking bullshit from stupid fucking GitHub bullcrap

---
## [Knightfall5/Citadel-Station-13-RP](https://github.com/Knightfall5/Citadel-Station-13-RP)@[24aca0ae55...](https://github.com/Knightfall5/Citadel-Station-13-RP/commit/24aca0ae55ce2204474ec23fed6d23cb46b6645e)
#### Wednesday 2022-08-31 02:25:49 by LordPapalus

Cargonia, but with less weapons (#4370)

* Cargonia is no more

Fuck you

* PLEASE

* Zandario, I will suck your PP

---
## [oxen-io/oxen-core](https://github.com/oxen-io/oxen-core)@[9c9552380d...](https://github.com/oxen-io/oxen-core/commit/9c9552380ddecc57965e2e393454ef9d880cb803)
#### Wednesday 2022-08-31 02:45:56 by Jason Rhinelander

Make hooks use exceptions on error rather than bool returns

bool returns suck in general, but in most cases here they are also a
pain in the ass because *each* place that returns false is also issuing
a log statement.  If only there were a way to return error information
to the common caller to have the common caller handle it... oh wait,
there is!

---
## [ammarfaizi2/linux-fork](https://github.com/ammarfaizi2/linux-fork)@[89ca3ca008...](https://github.com/ammarfaizi2/linux-fork/commit/89ca3ca0080282d9b0880e64a1262edeb5fbb2ba)
#### Wednesday 2022-08-31 02:51:05 by Johannes Weiner

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
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[2a0d41e2f8...](https://github.com/pytorch/pytorch/commit/2a0d41e2f8c0c99ff25335a1a51091c2b847c4c0)
#### Wednesday 2022-08-31 03:00:38 by Andrew Gu

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
## [theBowja/PoringWorldBot](https://github.com/theBowja/PoringWorldBot)@[4b2f4a09d5...](https://github.com/theBowja/PoringWorldBot/commit/4b2f4a09d5946df8ab99d87b97c35b6bb5e38be5)
#### Wednesday 2022-08-31 05:25:24 by gws-bots

Update aliases.js

Listed some items that do not synch but because of next tier it has a name change. 

Check line 82 and 91, since I am not sure if you didn't mention the first tier item in case people wanted to do -refine 15 -alias. Not sure if it will matter much since some first tiers can only go up to refine level 10 but I am not sure on those two items. However, line 94 Floral Bracelet can go up to refine 15 and I have seen people get pings for it but they really are looking for a 15 Rosa Bracelet/Chain since Floral Bracelet will drop 2 refine levels. Just not sure your preference. 

Last, not sure if you will like it // POTION - EFFECT but those are the new boxes we can get from Comodo Dungeon and they are a bit annoying to spell since they have dashes, true spelling are "Military Exploit Chest - Off-hand" and "Military Exploit Chest - Armor". I don't think that the average joe remembers to not use dashes when listing a name of an item.

---
## [kittstone/better](https://github.com/kittstone/better)@[4761f3ab50...](https://github.com/kittstone/better/commit/4761f3ab50e39255872b8720ea400fd0010e3b1f)
#### Wednesday 2022-08-31 06:23:21 by kittstone

screw with input system also fix options n shit
because fuck you!!!

---
## [mcabbott/julia](https://github.com/mcabbott/julia)@[62e0729dbc...](https://github.com/mcabbott/julia/commit/62e0729dbc5f9d5d93d14dcd49457f02a0c6d3a7)
#### Wednesday 2022-08-31 06:36:06 by Mirek Kratochvil

avoid using `@sync_add` on remotecalls (#44671)

* avoid using `@sync_add` on remotecalls

It seems like @sync_add adds the Futures to a queue (Channel) for @sync, which
in turn calls wait() for all the futures synchronously. Not only that is
slightly detrimental for network operations (latencies add up), but in case of
Distributed the call to wait() may actually cause some compilation on remote
processes, which is also wait()ed for. In result, some operations took a great
amount of "serial" processing time if executed on many workers at once.

For me, this closes #44645.

The major change can be illustrated as follows: First add some workers:

```
using Distributed
addprocs(10)
```

and then trigger something that, for example, causes package imports on the
workers:

```
using SomeTinyPackage
```

In my case (importing UnicodePlots on 10 workers), this improves the loading
time over 10 workers from ~11s to ~5.5s.

This is a far bigger issue when worker count gets high. The time of the
processing on each worker is usually around 0.3s, so triggering this problem
even on a relatively small cluster (64 workers) causes a really annoying delay,
and running `@everywhere` for the first time on reasonable clusters (I tested
with 1024 workers, see #44645) usually takes more than 5 minutes. Which sucks.

Anyway, on 64 workers this reduces the "first import" time from ~30s to ~6s,
and on 1024 workers this seems to reduce the time from over 5 minutes (I didn't
bother to measure that precisely now, sorry) to ~11s.

Related issues:
- Probably fixes #39291.
- #42156 is a kinda complementary -- it removes the most painful source of
  slowness (the 0.3s precompilation on the workers), but the fact that the
  wait()ing is serial remains a problem if the network latencies are high.

May help with #38931

Co-authored-by: Valentin Churavy <vchuravy@users.noreply.github.com>

---
## [MKLab-ITI/hugomklab](https://github.com/MKLab-ITI/hugomklab)@[a02bcd3378...](https://github.com/MKLab-ITI/hugomklab/commit/a02bcd3378b91d8c8c64a81e23e5e632230f4885)
#### Wednesday 2022-08-31 07:06:22 by drania24

Update Publication “2022-05-06-water-quality-issues-can-we-detect-a-creeping-crisis-with-social-media-data”

---
## [opengauss-mirror/openGauss-server](https://github.com/opengauss-mirror/openGauss-server)@[9cb7462667...](https://github.com/opengauss-mirror/openGauss-server/commit/9cb74626671fdb92aa915f4449a4f47b128d8ea0)
#### Wednesday 2022-08-31 07:22:46 by pujr

合并PG社区PR，更改数据结构，改善cache miss。

* Replace the data structure used for keyword lookup.

Previously, ScanKeywordLookup was passed an array of string pointers.
This had some performance deficiencies: the strings themselves might
be scattered all over the place depending on the compiler (and some
quick checking shows that at least with gcc-on-Linux, they indeed
weren't reliably close together).  That led to very cache-unfriendly
behavior as the binary search touched strings in many different pages.
Also, depending on the platform, the string pointers might need to
be adjusted at program start, so that they couldn't be simple constant
data.  And the ScanKeyword struct had been designed with an eye to
32-bit machines originally; on 64-bit it requires 16 bytes per
keyword, making it even more cache-unfriendly.

Redesign so that the keyword strings themselves are allocated
consecutively (as part of one big char-string constant), thereby
eliminating the touch-lots-of-unrelated-pages syndrome.  And get
rid of the ScanKeyword array in favor of three separate arrays:
uint16 offsets into the keyword array, uint16 token codes, and
uint8 keyword categories.  That reduces the overhead per keyword
to 5 bytes instead of 16 (even less in programs that only need
one of the token codes and categories); moreover, the binary search
only touches the offsets array, further reducing its cache footprint.
This also lets us put the token codes somewhere else than the
keyword strings are, which avoids some unpleasant build dependencies.

While we're at it, wrap the data used by ScanKeywordLookup into
a struct that can be treated as an opaque type by most callers.
That doesn't change things much right now, but it will make it
less painful to switch to a hash-based lookup method, as is being
discussed in the mailing list thread.

Most of the change here is associated with adding a generator
script that can build the new data structure from the same
list-of-PG_KEYWORD header representation we used before.
The PG_KEYWORD lists that plpgsql and ecpg used to embed in
their scanner .c files have to be moved into headers, and the
Makefiles have to be taught to invoke the generator script.
This work is also necessary if we're to consider hash-based lookup,
since the generator script is what would be responsible for
constructing a hash table.

Aside from saving a few kilobytes in each program that includes
the keyword table, this seems to speed up raw parsing (flex+bison)
by a few percent.  So it's worth doing even as it stands, though
we think we can gain even more with a follow-on patch to switch
to hash-based lookup.

John Naylor, with further hacking by me

Discussion: https://postgr.es/m/CAJVSVGXdFVU2sgym89XPL=Lv1zOS5=EHHQ8XWNzFL=mTXkKMLw@mail.gmail.com

---
## [DamienDoury/pokecrystal-mobile-en](https://github.com/DamienDoury/pokecrystal-mobile-en)@[209446808b...](https://github.com/DamienDoury/pokecrystal-mobile-en/commit/209446808b55263e948777f8f42fa44e96b44b91)
#### Wednesday 2022-08-31 08:11:50 by SUGO-SG-13-DAMI\Damien

Input constraints done.

Notes:
- As the zipcode is saved as a list of indexes from the char pools, and as the char pools differ from one region to another, the zipcodes will be broken from one region to another. This could be fixed server-side, or by encoding/decoding the indexes into VRAM indexes (the alphabet is constant between most regions, except asian ones) when opening/leaving the Profile menu.
- The macros I created are old and ugly (rgbds 0.3.8), and should be udpated when updating RGBDS.
- My code is kinda quick and dirty, as several lists are duplicated when they could be used once. I'm thinking about the "Zipcode_CharPoolForStringIndex" arrays, which could save several dozen bytes if optimized.
- A special case case for the alignment of the AUS region codes has been made, because the string length is not constant. This doubles the "Prefectures" array, which adds 173 bytes to the rom bank.
- With that being said, we are far from running out of space in the ROM $12.

---
## [6165-MSET-CuttleFish/TeamTrack](https://github.com/6165-MSET-CuttleFish/TeamTrack)@[c8f1c3a458...](https://github.com/6165-MSET-CuttleFish/TeamTrack/commit/c8f1c3a4587ae0bb68fa9d2152d5b018d2914f14)
#### Wednesday 2022-08-31 08:57:37 by jiru-shan

okay delete button is done i hate everything especially my sleep schedule

i love egirl asmr & playing Azur Lane at 1AM in the morning. It's very fun and is definitely not me coping while having to write dogshit code that may or may not work. Also the cloud function is a slight(larger) vulnerability, but I wrote some potential fixes in comments on index.ts.

---
## [MASQ-Project/Node](https://github.com/MASQ-Project/Node)@[b0e9bb484e...](https://github.com/MASQ-Project/Node/commit/b0e9bb484effc32ed164eb4bef51b624c3d7982a)
#### Wednesday 2022-08-31 09:41:49 by dnwiebe

GH-625: Log message enhancements, plus clippy appeasement (#153)

* Log message enhancements, plus clippy appeasement

* GH-627: Clippy should be happy again by now

* GH-627: one line was silly

* GH-627: starting ignoring the troublesome test again

* GH-627: there was a formatting issue

* handles_startup_and_shutdown_integration now doesn't run in Actions on Windows

* handles_startup_and_shutdown_integration now doesn't run in Actions on Windows

* Added import

* GH-625: Formatting

* GH-625: Remember to return

Co-authored-by: Bert <Bert@Bert.com>

---
## [Cactusinhand/git](https://github.com/Cactusinhand/git)@[5beca49a0b...](https://github.com/Cactusinhand/git/commit/5beca49a0b1f3c6d05a4437ca037ab2123a2de57)
#### Wednesday 2022-08-31 10:33:33 by Ævar Arnfjörð Bjarmason

test-lib: simplify by removing test_external

Remove the "test_external" function added in [1]. This arguably makes
the output of t9700-perl-git.sh and friends worse. But as we'll argue
below the trade-off is worth it, since "chaining" to another TAP
emitter in test-lib.sh is more trouble than it's worth.

The new output of t9700-perl-git.sh is now:

	$ ./t9700-perl-git.sh
	ok 1 - set up test repository
	ok 2 - use t9700/test.pl to test Git.pm
	# passed all 2 test(s)
	1..2

Whereas before this change it would be:

	$ ./t9700-perl-git.sh
	ok 1 - set up test repository
	# run 1: Perl API (perl /home/avar/g/git/t/t9700/test.pl)
	ok 2 - use Git;
	[... omitting tests 3..46 from t/t9700/test.pl ...]
	ok 47 - unquote escape sequences
	1..47
	# test_external test Perl API was ok
	# test_external_without_stderr test no stderr: Perl API was ok

At the time of its addition supporting "test_external" was easy, but
when test-lib.sh itself started to emit TAP in [2] we needed to make
everything surrounding the emission of the plan consider
"test_external". I added that support in [2] so that we could run:

	prove ./t9700-perl-git.sh :: -v

But since then in [3] the door has been closed on combining
$HARNESS_ACTIVE and -v, we'll now just die:

	$ prove ./t9700-perl-git.sh :: -v
	Bailout called.  Further testing stopped:  verbose mode forbidden under TAP harness; try --verbose-log
	FAILED--Further testing stopped: verbose mode forbidden under TAP harness; try --verbose-log

So the only use of this has been that *if* we had failure in one of
these tests we could e.g. in CI see which test failed based on the
test number. Now we'll need to look at the full verbose logs to get
that same information.

I think this trade-off is acceptable given the reduction in
complexity, and it brings these tests in line with other similar
tests, e.g. the reftable tests added in [4] will be condensed down to
just one test, which invokes the C helper:

	$ ./t0032-reftable-unittest.sh
	ok 1 - unittests
	# passed all 1 test(s)
	1..1

It would still be nice to have that ":: -v" form work again, it
never *really* worked, but even though we've had edge cases test
output screwing up the TAP it mostly worked between d998bd4ab67 and
[3], so we may have been overzealous in forbidding it outright.

I have local patches which I'm planning to submit sooner than later
that get us to that goal, and in a way that isn't buggy. In the
meantime getting rid of this special case makes hacking on this area
of test-lib.sh easier, as we'll do in subsequent commits.

The switch from "perl" to "$PERL_PATH" here is because "perl" is
defined as a shell function in the test suite, see a5bf824f3b4 (t:
prevent '-x' tracing from interfering with test helpers' stderr,
2018-02-25). On e.g. the OSX CI the "command perl"... will be part of
the emitted stderr.

1. fb32c410087 (t/test-lib.sh: add test_external and
   test_external_without_stderr, 2008-06-19)
2. d998bd4ab67 (test-lib: Make the test_external_* functions
   TAP-aware, 2010-06-24)
3. 614fe015212 (test-lib: bail out when "-v" used under
   "prove", 2016-10-22)
4. ef8a6c62687 (reftable: utility functions, 2021-10-07)

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [owid/owid-static](https://github.com/owid/owid-static)@[be6c822a86...](https://github.com/owid/owid-static/commit/be6c822a8649482e29333960ecf063198b49166c)
#### Wednesday 2022-08-31 10:42:40 by owidbot

Deploy 2022-08-31T10:34:16.531Z
Updating chart children-who-experience-violent-discipline-boys-vs-girls
Updating chart fertility-rate-vs-share-of-women-between-25-and-29-years-old-with-no-education
Updating chart co2-per-capita-vs-renewable-electricity
Updating chart percentage-of-households-using-solid-fuels-for-cooking-rural-vs-urban
Updating chart open-defecation-in-rural-areas-vs-urban-areas
Updating chart antibiotic-use-in-livestock-vs-meat-supply-per-capita

Co-authored-by: Fiona Spooner <fiona@ourworldindata.org>
Co-authored-by: Fiona Spooner <fiona@ourworldindata.org>
Co-authored-by: Fiona Spooner <fiona@ourworldindata.org>
Co-authored-by: Fiona Spooner <fiona@ourworldindata.org>
Co-authored-by: Fiona Spooner <fiona@ourworldindata.org>
Co-authored-by: Fiona Spooner <fiona@ourworldindata.org>

---
## [SLASHEM-Extended/SLASHEM-Extended](https://github.com/SLASHEM-Extended/SLASHEM-Extended)@[efc886471f...](https://github.com/SLASHEM-Extended/SLASHEM-Extended/commit/efc886471fdf82b8f8bf1beb502c55c10d4c68a7)
#### Wednesday 2022-08-31 10:55:00 by AmyBSOD

Code most of the new traps

Bah, this is such a fucking pain in the butt, and I didn't even finish yet (the monster generator remains to be done)! But anyway all the cunts who hate my game because of a few rare "offensive" features can all jump off a bridge because they don't even know how much work it is to make a NetHack variant. If they were to construct a castle in real life, I'll say it sucks just to spite the amount of work they put into it.

---
## [haenkel/shortcircuit-xt](https://github.com/haenkel/shortcircuit-xt)@[03f420b560...](https://github.com/haenkel/shortcircuit-xt/commit/03f420b5604199877ba44d01dd681cb409c55557)
#### Wednesday 2022-08-31 11:42:55 by Paul

Beginning a path to engine cleanup (#297)

The engine was ported and working, but the code had never really
been visited, analyzed, cleaned up, etc... and that's kinda what
I want to do this week. Start by deleting some distracting stuff
which was unused and cleaning up some of the expedient hacks
from the very first port, including the windows compat layer in 
favor of std types and removing the python bindings which we no
longer need.

---
## [Fedoraware/Fedoraware](https://github.com/Fedoraware/Fedoraware)@[f370cbf8ed...](https://github.com/Fedoraware/Fedoraware/commit/f370cbf8edda9593758c3d24244b985d7c993735)
#### Wednesday 2022-08-31 12:31:53 by Baan

fix.

the beep beep beep beep beep beep shit was fucking annoying as on god.

---
## [dvsdude2/doom](https://github.com/dvsdude2/doom)@[469acac8b0...](https://github.com/dvsdude2/doom/commit/469acac8b0d3fe32fc15489bc1fe5958f4e3d392)
#### Wednesday 2022-08-31 13:41:23 by dvsdude2

enough changes warrented update

@@ -2,6 +2,7 @@ ;; try running with out indent, don't believe it's
usefull here
@@ -143,10 +144,17 @@ => added shortcut to the fallback +dashboard for
the new journal module installed
@@ -156,6 +164,10 @@ => set default folder for new journal
@@ -197,6 +209,10 @@ => made personal org-capture-template of A file I
call organizer
@@ -220,13 +236,14 @@ => added an after macro here thought it should
have one, thinking it may help...did not see any big change but left it
on anyways
@@ -332,13 +349,15 @@ => revisted keychordss and 3 new ones, fine tune
delay, may need more tuning
@@ -819,10 +838,19 @@ => this should keep the workstation tab bar
visable more. don't all ways remember that I'm in a seperate workspace.
this should help that may need to change the face, bright-pink little
distracting
@@ -865,8 +893,8 @@ => changed declutter-engine, seem to be expensive
using rdrview, maybe it would get better but as of now not needed. eww
should work for how i've used it
@@ -907,7 +935,7 @@ => this use to work but then stopped. after a little
digging it appeared that the command visual-motion was deprecated and
found state was more widly used. appears to have worked. yay i guess.
@@ -944,7 +972,7 @@ => trying settings to see what I prefer
@@ -1006,6 +1034,7 @@ => was sure this use to work before, but it failed
when I went to use it, prompting me to add this, didn't seem nessesary
before?
@@ -1201,9 +1229,8 @@ Elfeed => this is work in progress, me fuckin with
shit. in hide site I believe it was just paticulare websites.
@@ -1228,6 +1255,7 @@ Elfeed => experimenting with keybindings for
elfeed-show-mode
@@ -1248,10 +1276,45 @@ Elfeed => this is two experiments in one.
first is a hook to start elfeed-summary, every time elfeed is started.
this has worked and I may keep for a while.
the second is a new package that I discovered, the code sound like
something interesting, wanted to see it in action. still working on it.
@@ -1361,6 +1424,9 @@ Elfeed => this is hook #2 chained to the first
hook. the way this should work and does is:
start elfeed => hook#1 starts elfeed-summary => hook#2 updates feed.
this seems to work, well enough. one of the reasons for this is I get to
see the updates progress, know exactly when it has finished. no real
indicator that I could tell in elfeed when it was finished. now I can.
did read that it slows the process down a lot but it's doesn't seem that
bad? so far I consider this a success.
@@ -1460,6 +1526,7 @@ open source map => this is a test. it is a bunch
of predefind commands for the shell-dwim package. not sure if this will
just pollute things or not if so I'll remove it and just run the couple
I have used, yes I have used this package and it worked perfect. so more
is better ....maybe...maybe not.
@@ -1507,3 +1574,4 @@ open source map => this was left here just to
ponder it .... long story .

---
## [andreasuvia/proyectorutadelvino](https://github.com/andreasuvia/proyectorutadelvino)@[d97291c38f...](https://github.com/andreasuvia/proyectorutadelvino/commit/d97291c38fe91f4974e7885b6192b2f5d07b6163)
#### Wednesday 2022-08-31 14:36:40 by Andrea Suvia

Tercer commit, intentando arreglar las cagadas tuyas Git fuck you

---
## [GriceTurrble/recipes.riceprower.com](https://github.com/GriceTurrble/recipes.riceprower.com)@[f486fd1cd0...](https://github.com/GriceTurrble/recipes.riceprower.com/commit/f486fd1cd0dbb2c757b4c6ecc39d1a194d14f7f7)
#### Wednesday 2022-08-31 16:27:16 by Galen Rice

feat: site search with Algolia

Adjusts the index page to show the list of recipes
with search options set up using Algolia.

CI workflow has been updated to push content
to the search index using jekyll-algolia plugin.

And styles have been updated to accommodate the new containers
(for the search box widget, hits, and pagination).

There is no longer a need for an `/r/all` endpoint now,
so that link redirects back to the index again.

Finally, we're adjusting our basic fonts to Work Sans
with an optional serif font of Modern Antiqua.
These are ones my lovely spouse chose for her portfolio,
and frankly, I like em. Thanks hun!

---
## [AlexMeuer/moneytime](https://github.com/AlexMeuer/moneytime)@[11112f4ff7...](https://github.com/AlexMeuer/moneytime/commit/11112f4ff736ff08ede70349276382f8a1a807b1)
#### Wednesday 2022-08-31 17:03:51 by Alex Meuer

Initial Commit

The code in this first draft is awful, but a friend of mine wanted to
get his hands on this ASAP for the laugh.

---
## [equestrianvault/horsebooks-data](https://github.com/equestrianvault/horsebooks-data)@[235a104bf3...](https://github.com/equestrianvault/horsebooks-data/commit/235a104bf3923c90f174252033b4d8597554893d)
#### Wednesday 2022-08-31 17:37:27 by KeystrokeCascade

Update books.json

Added Friendship is Optimal
Added The Mare Who Once Lived on the Moon
Added A Stallion for the Time Being
Added Better Living Through Science and Ponies
Added Why am I Pinkie Pie?!
Updated details for Fallout: Equestria - Heroes
Updated details for The Enchanted Library
Updated details for Fallout: Equestria (MoI)
Updated details for Fallout Equestria: Project Horizons
Un-expired Princess Celestia: The Changeling Queen with signup form
Added The King of Love Bugs
Added Best Hell Ever & Heaven of a Hell
Changed Make Love Not War entry to make more sense

---
## [fabiocosta88/new-revolution](https://github.com/fabiocosta88/new-revolution)@[fbd70d116c...](https://github.com/fabiocosta88/new-revolution/commit/fbd70d116c260a94902c2e0164ceca94023f2f28)
#### Wednesday 2022-08-31 18:46:19 by rigis1

Fixes and add blood brothers quest till mission 4 (#753)

Fix:
• electric sparks
• baking
• filling fluids container
• the hunt for the sea serpent quest

Add:
• questlog entry for blood brothers quest, the hunt for the sea serpent quest and grave danger quest
• storages for blood brothers quest, the hunt for the sea serpent quest and grave danger quest
• keywords for blood brothers quest, the hunt for the sea serpent quest and grave danger quest
• condition to harlow travel to vengoth
• holy water to henricus shop
• food for blood brothers quest
• spawn npc ortheus and jack springer, monster gaffir
• npc jack springer 
• ugly monster loot
• events to gaffir and ugly monster
• ice cracking
• basic events for bosses Sir Nictros and Sir Baeloc
• basic spawn boss for levers
• access to falcon bastion

---
## [DavidRaab/Queue](https://github.com/DavidRaab/Queue)@[8c63dc16ca...](https://github.com/DavidRaab/Queue/commit/8c63dc16ca7d0eef0425696aae2ed795435f360e)
#### Wednesday 2022-08-31 18:47:23 by David Raab

CHANGED License

Switched from MIT to Do what The Fuck You Want License.

---
## [zulip/zulip-mobile](https://github.com/zulip/zulip-mobile)@[0af1d1133c...](https://github.com/zulip/zulip-mobile/commit/0af1d1133c50f38057877eba063f837f82b961bd)
#### Wednesday 2022-08-31 18:53:13 by Chris Bobbe

UnicodeEmoji [nfc]: Reduce to just what we use; cut out r-n-vector-icons

Emojis aren't icons, so even from its name, it's not clear that
react-native-vector-icons is best suited to render them, even if it
has turned out to be convenient for a subset of emoji (Unicode
emoji).

Like avatars, emojis are a mode of freeform user expression (think
of the "thank you" emoji). Icons, on the other hand, are a palette
of UI elements that UI designers use to convey UI meaning and make
the UI more approachable. ("Ah, a star icon, I bet that'll take me
to starred messages if I press it.")

The createIconSet function from r-n-vector-icons is designed to give
us such a palette of UI elements: we're to call it once, at module
top-level, and and it'll give us a React component that can render
any one of a static menu of icons. We've co-opted that into "a
static menu of Unicode emoji," but that's worked fine so far.

But, with #2956, we don't want a static menu, we want a menu that's
defined by the server. That's a breaking point for continuing to use
createIconSet here. We'd have to handle these constraints:
  - We can't call createIconSet at module top-level anymore, since
    we don't have the server data at that time.
  - We'd have to call it before it's time to render a Unicode emoji.
…And that seems like too much trouble to keep around something that
isn't designed for this use case anyway.

So, as a first step, in this commit, take part of createIconSet's
returned component [1] -- just enough to preserve current behavior
-- and define it in a separate file. It's pretty small, so, go ahead
and convert to a function component while we're at it. After this,
it'll be an easy switch to consume data from Redux, with
useSelector.

[1] node_modules/react-native-vector-icons/lib/create-icon-set.js

---
## [wangandi/materialize](https://github.com/wangandi/materialize)@[305082a6a9...](https://github.com/wangandi/materialize/commit/305082a6a99ee063839975c86bd1e821a2af0e23)
#### Wednesday 2022-08-31 19:20:49 by Daniel Harrison

persist: commit state updates to durable storage incrementally

Before, there was pressure to keep the size of state down, because it
was rewritten entirely on each command application. In particular, this
created a tension in compaction tuning between being aggressive about
fewer batches (smaller state) and compacting small batches lazily
(smaller write amplification).

Writing state updates as incremental diffs means that size of a
Consensus writes for each command is independent of the total size of
state. We should be able leverage this to make the entire
`WriteHandle::compare_and_append_batch` latency constant w.r.t. the size
of state and thus independent of compaction. This lets us tune
compaction entirely for where we want to be in its more intrinsic
tradeoff between read, write, and space amplification.

(NB: This commit doesn't quite get us to constant latencies, there's
some elbow grease left. I've proven concretely that it can get down to
`O(log(num state batches))`, but that included some hacks that didn't
make this PR. This would be lovely followup work once we get a chance.)

As persist metadata changes over time, we make its versions (each
identified by a [SeqNo]) durable in two ways:
- `rollups`: Periodic copies of the entirety of [State], written to
  [Blob].
- `diffs`: Incremental [StateDiff]s, written to [Consensus]. The
following invariants are maintained at all times:
- A shard is initialized iff there is at least one version of it in
  Consensus.
- The first version of state is written to `SeqNo(1)`. Each successive
  state version is assigned its predecessor's SeqNo +1.
- `current`: The latest version of state. By definition, the largest
  SeqNo present in Consensus.
- As state changes over time, we keep a range of consecutive versions
  available. These are periodically `truncated` to prune old versions
  that are no longer necessary.
- `earliest`: The first version of state that it is possible to
  reconstruct.
  - Invariant: `earliest <= current.seqno_since()` (we don't garbage
    collect versions still being used by some reader).
  - Invariant: `earliest` is always the smallest Seqno present in
    Consensus.
    - This doesn't have to be true, but we select to enforce it.
    - Because the data stored at that smallest Seqno is an incremental
      diff, to make this invariant work, there needs to be a rollup at
      either `earliest-1` or `earliest`. We choose `earliest` because it
      seems to make the code easier to reason about in practice.
    - A consequence of the above is when we garbage collect old versions
      of state, we're only free to truncate ones that are `<` the latest
      rollup that is `<= current.seqno_since`.
- `live diffs`: The set of SeqNos present in Consensus at any given
  time.
- `live states`: The range of state versions that it is possible to
  reconstruct: `[earliest,current]`.
  - Because of earliest and current invariants above, the range of `live
    diffs` and `live states` are the same.
- The set of known rollups are tracked in the shard state itself.
  - For efficiency of common operations, the most recent rollup's Blob
    key is always denormalized in each StateDiff written to Consensus.
    (As described above, there is always a rollup at earliest, so we're
    guaranteed that there is always at least one live rollup.)
  - Invariant: The rollups in `current` exist in Blob.
    - A consequence is that, if a rollup in a state you believe is
      `current` doesn't exist, it's a guarantee that `current` has
      changed (or it's a bug).
  - Any rollup at a version `< earliest-1` is useless (we've lost the
    incremental diffs between it and the live states). GC is tasked with
    deleting these rollups from Blob before truncating diffs from
    Consensus. Thus, any rollup at a seqno < earliest can be considered
    "leaked" and deleted by the leaked blob detector.
  - Note that this means, while `current`'s rollups exist, it will be
    common for other live states to reference rollups that no longer
    exist.

---
## [JackAKirk/llvm](https://github.com/JackAKirk/llvm)@[15f3cd6bfc...](https://github.com/JackAKirk/llvm/commit/15f3cd6bfc670ba6106184a903eb04be059e5977)
#### Wednesday 2022-08-31 19:36:37 by Matheus Izvekov

[clang] Implement ElaboratedType sugaring for types written bare

Without this patch, clang will not wrap in an ElaboratedType node types written
without a keyword and nested name qualifier, which goes against the intent that
we should produce an AST which retains enough details to recover how things are
written.

The lack of this sugar is incompatible with the intent of the type printer
default policy, which is to print types as written, but to fall back and print
them fully qualified when they are desugared.

An ElaboratedTypeLoc without keyword / NNS uses no storage by itself, but still
requires pointer alignment due to pre-existing bug in the TypeLoc buffer
handling.

---

Troubleshooting list to deal with any breakage seen with this patch:

1) The most likely effect one would see by this patch is a change in how
   a type is printed. The type printer will, by design and default,
   print types as written. There are customization options there, but
   not that many, and they mainly apply to how to print a type that we
   somehow failed to track how it was written. This patch fixes a
   problem where we failed to distinguish between a type
   that was written without any elaborated-type qualifiers,
   such as a 'struct'/'class' tags and name spacifiers such as 'std::',
   and one that has been stripped of any 'metadata' that identifies such,
   the so called canonical types.
   Example:
   ```
   namespace foo {
     struct A {};
     A a;
   };
   ```
   If one were to print the type of `foo::a`, prior to this patch, this
   would result in `foo::A`. This is how the type printer would have,
   by default, printed the canonical type of A as well.
   As soon as you add any name qualifiers to A, the type printer would
   suddenly start accurately printing the type as written. This patch
   will make it print it accurately even when written without
   qualifiers, so we will just print `A` for the initial example, as
   the user did not really write that `foo::` namespace qualifier.

2) This patch could expose a bug in some AST matcher. Matching types
   is harder to get right when there is sugar involved. For example,
   if you want to match a type against being a pointer to some type A,
   then you have to account for getting a type that is sugar for a
   pointer to A, or being a pointer to sugar to A, or both! Usually
   you would get the second part wrong, and this would work for a
   very simple test where you don't use any name qualifiers, but
   you would discover is broken when you do. The usual fix is to
   either use the matcher which strips sugar, which is annoying
   to use as for example if you match an N level pointer, you have
   to put N+1 such matchers in there, beginning to end and between
   all those levels. But in a lot of cases, if the property you want
   to match is present in the canonical type, it's easier and faster
   to just match on that... This goes with what is said in 1), if
   you want to match against the name of a type, and you want
   the name string to be something stable, perhaps matching on
   the name of the canonical type is the better choice.

3) This patch could expose a bug in how you get the source range of some
   TypeLoc. For some reason, a lot of code is using getLocalSourceRange(),
   which only looks at the given TypeLoc node. This patch introduces a new,
   and more common TypeLoc node which contains no source locations on itself.
   This is not an inovation here, and some other, more rare TypeLoc nodes could
   also have this property, but if you use getLocalSourceRange on them, it's not
   going to return any valid locations, because it doesn't have any. The right fix
   here is to always use getSourceRange() or getBeginLoc/getEndLoc which will dive
   into the inner TypeLoc to get the source range if it doesn't find it on the
   top level one. You can use getLocalSourceRange if you are really into
   micro-optimizations and you have some outside knowledge that the TypeLocs you are
   dealing with will always include some source location.

4) Exposed a bug somewhere in the use of the normal clang type class API, where you
   have some type, you want to see if that type is some particular kind, you try a
   `dyn_cast` such as `dyn_cast<TypedefType>` and that fails because now you have an
   ElaboratedType which has a TypeDefType inside of it, which is what you wanted to match.
   Again, like 2), this would usually have been tested poorly with some simple tests with
   no qualifications, and would have been broken had there been any other kind of type sugar,
   be it an ElaboratedType or a TemplateSpecializationType or a SubstTemplateParmType.
   The usual fix here is to use `getAs` instead of `dyn_cast`, which will look deeper
   into the type. Or use `getAsAdjusted` when dealing with TypeLocs.
   For some reason the API is inconsistent there and on TypeLocs getAs behaves like a dyn_cast.

5) It could be a bug in this patch perhaps.

Let me know if you need any help!

Signed-off-by: Matheus Izvekov <mizvekov@gmail.com>

Differential Revision: https://reviews.llvm.org/D112374

---
## [EsmaelAwad/The-Data-Repository](https://github.com/EsmaelAwad/The-Data-Repository)@[a6f7087cb4...](https://github.com/EsmaelAwad/The-Data-Repository/commit/a6f7087cb4c783c9499ab0509b1d8fe82544c75b)
#### Wednesday 2022-08-31 19:49:42 by EsmaelAwad

Regular Expressions to the rescue

 Your data model is so lovely, created with love and care.

However, someone did not appreciate that and decided to give you the new data in a messed-up format

(changed the order of the columns, names, or even values order!).

This could lead to computation errors if you are retyping a script that gets specific numbers from a particular column, you merged data on a specific set of columns, or even errors if your data model is in a power query or something.

We want to pass the data in an acceptable way, where every single value knows its way home.

We have two methods to accomplish that, an easy way and the hard way.

but before discussing ways let's see the first steps to thinking and fixing that problem:

we need for each row, a single list that represents each element in that row, then we need to pass each value to its beloved column.

and we do not know the names of the columns, we only know the structure of the new data, any number of rows, 4 columns.

Skills Used:
	1.Python
	2.Pandas
	3.re module
	4.Regular Expressions

you can find an article about this issue: https://theveryamateuredatascientist.blogspot.com/2022/07/assign-data-to-columns-using-regular.html

---
## [oxidecomputer/opte](https://github.com/oxidecomputer/opte)@[d906c9d5df...](https://github.com/oxidecomputer/opte/commit/d906c9d5dfb725e11abb95ba1c3ab8525eb5f4c3)
#### Wednesday 2022-08-31 20:22:56 by Ryan Zezeski

HeaderAction::Modify should not panic on missing metadata (#241)

The main thrust of this commit is to fix #241 by allowing a
`HeaderAction` to return an error result. Some other stuff came along
for the ride.

- add some basic kstats support (#23)

  With yet another possible runtime error I thought it was high time
  we had some kstats support. There is already good SDT support in
  OPTE, but if you're not running DTrace when an error occurs, you're
  not going to know it happened. Having kstats allows us to track
  historical failures/errors and provide a clue as to where to look
  when debugging live.

  While trying to implement kstats I realized that I need to change
  the locking scheme in OPTE. OPTE was my first real Rust project; a
  packet transformation engine running Rust in the illumos kernel --
  it was a lot to take on for a first Rust project. I brought a lot of
  my previous knowledge to bear from working on the illumos networking
  stack, particularly the mac module. From this past knowledge my
  initial architecture relied on a lot of Arc + fine-grained locks
  inside of the engine, as this is the structure I was used to seeing
  inside illumos.

  When trying to implement kstats I realized that I would have to wrap
  a mutex around a group of named kstats...and that just felt weird
  compared to how we do it in most illumos network drivers.
  Furthermore, the fine-grained locking I had in place wasn't actually
  completely correct, and relied on some hard-to-understand comments
  and non-idiomatic Rust code. Then I had the thought that I should
  really be treating an individual Port more like a Tx/Rx ring that you
  would find in a network driver, where the entire ring is locked
  during processing. In this sense the entire Port should be wrapped
  in a mutex, knowing that any state changed inside that Port is
  atomic in respect to a given packet (or chain of packets). If and
  when this proves to be a limiting factor, you can then start
  breaking things out at a higher level, like having each Port broken
  out into concurrent streams for different protocol types: like TCP,
  UDP, and Other. If that becomes a bottleneck you could then possibly
  break each protocol out further into rings, assuming you could find
  a way to consistently hash flows to their appropriate ring.
  Furthermore, the happy path for an active flow is always hitting the
  UFT. There may be ways to structure the UFT such that it can be
  queried without a mutex, perhaps with some type of scheme that uses
  asynchronous updates of a persistent (read functional) data structure
  plus atomic pointer swaps. The point being, there are higher-level
  ways to reduce contention than the fine grained locking scheme I had
  used up to this point.

- Renamed `ModActionArg` to `ModifyActionArg`, because I kept
  confusing `Mod` with "module" in my head, and I wrote this damn
  code!

- Renamed `HT` to `HdrTransform` to make it a bit more obvious what it
  refers to.

---
## [rothquel/OK-Diver](https://github.com/rothquel/OK-Diver)@[22ad514941...](https://github.com/rothquel/OK-Diver/commit/22ad514941d46475f4f3f40b941955d666f52014)
#### Wednesday 2022-08-31 21:15:05 by Camila Contreras Barrera

honestly im sorry i cant remember what I did but I think I changed avatar, review card, and maybe some small details here and there ...:(

---
## [rothquel/OK-Diver](https://github.com/rothquel/OK-Diver)@[631ede3e40...](https://github.com/rothquel/OK-Diver/commit/631ede3e403b8f93b363c315264ccb7c11cc22b0)
#### Wednesday 2022-08-31 21:15:05 by Nic Rothquel

Merge pull request #112 from rothquel/adding_avatar_class_in_avatar_of_review

honestly im sorry i cant remember what I did but I think I changed av…

---
## [psf/black](https://github.com/psf/black)@[0019261abc...](https://github.com/psf/black/commit/0019261abcf6d9e564ba32d3cc15534b9026f29e)
#### Wednesday 2022-08-31 21:56:49 by Richard Si

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
## [chickells/css-landing-page](https://github.com/chickells/css-landing-page)@[221fd3e41d...](https://github.com/chickells/css-landing-page/commit/221fd3e41d412e69c407dd5b5064c70b21a2b025)
#### Wednesday 2022-08-31 22:11:32 by Chase

CLOSE ENOUGH
lol fucking sick of this shit. can't figure out how to set max
width for all content but to let bg colors extend to edge

also for some reason 'quote' bg color has a small border....?
idk i give up I WANT TO DO BACKEND SHIT

---
## [Fikou/tgstation](https://github.com/Fikou/tgstation)@[5dc17bd865...](https://github.com/Fikou/tgstation/commit/5dc17bd86556c01cc0f81f54a6ce270169c00088)
#### Wednesday 2022-08-31 22:52:31 by san7890

Security's Scaling Departmental Accesses - More Pop, More Problems (#68534)

lternative to #68527
About The Pull Request

Hey there,

This is an alternative PR that I concocted based on talking with Goof on that PR. Basically, we already have a nicely complicated system to track and balance the number of security officers we have in a shift based on some config coefficient setting, by which we can set the amount of lockers that spawn in on the start of a round, as well as determine truly how many security officers we have.

image

So, I've decided to leverage this in another way. Basically, based on the number of security officers in a shift, their specific departmental officers will also get more (elevated) accesses. They already start with a certain amount of access, but they can get more if it is a low-pop shift with the mechanic introduced in this PR. For example, an Engineering Security Officer can access Atmospherics and Engineering departments by default, but they can't access Telecommunications unless there is a lower population of players AT SHIFT START. Same for a Medical Security Officer accessing Medbay, but not Plumbing.

Update: I have made it such that there are three system that server operators can set:

They can use the Scaling System that operates in the same method outlined in the rest of the PR.
They can disable giving departmental security officers "elevated access" (such as access beyond the "front doors") to these officers.
Finally, they can also just always ensure that departmental security officers get the maximal accesses possible.

The default setting is the "Scaling System" outlined in this PR, which is already dependent on the general Security Officer Scaling Co-Efficient.
Why It's Good For The Game

I think it's better to involve some more nuanced config scaling that we already have present in the game. The major theme that we want to avoid is that departmental security officers having maximal accesses when there is an already large number of persons on the security force will result in "miserable" shifts for the common person working within a department (security metaprotections). However, some server operators (as well as server cultures) tend to have very wide ranges in how many security officers they have on a shift-by-shift basis. One day, you could have 0-2 security officers, the next, you could have 4-6. It's all variable on who's playing (as always). There is also a significant variation between server to server in regards to how many security officer slots you tend to have on spawn, but this is already manageable by the security officer co-efficient in config.

I believe this PR is an acceptable proposal within the bounds of #68527 (comment) , although it may bend certain aspects of it, I definitely do see where some people may be coming from. I believe I've adjusted the accesses to a "sane"/justifiable amount, but I'll come back to think on everything.

"Red-tiding" may or may not be a problem, but there's always just going to be something inherently silly with a security officer being able to walk into plumbing to start plumbing. I hoped that this would be seen as a positive as opposed to a negative, but I can see how it could negatively impact player experience. HOWEVER, interplayer experience should not be handled by the codebase in all aspects, which is why I've also passed in the associated config variables, so that server operators (who should handle the interplayer experience with their level of discretion and nuance) can.
What accesses are where?

The general philosophy as I thought through designing this would be that the security officer should at the very least have general "front-door" access into a department, and maybe something benign. If we had even more per-door accesses, this could definitely be a bit more granular (one example I can think of would only atmospherics technicians having access to the "Pump Room", while Security Officers would not. However, this is for a later date). So, you have the "default" access you always get, and a potential to get "elevated" access as a Departmental Security Officer.

The balances are as such:

The Cargo Security Officer will have access to the Cargo Bay, Mining Section, and the Shipping Room. The first two are rather general areas, with the Shipping Room being a rather good help for rescuing (or "rescuing") flushed crewmembers when the cargo techies can't get to it/no AI. The Auxiliary Base is not essential to the security officer's functions, and the mining station helps restrict access further on stations like IceBox. This would also grant them extra access to the Lavaland base, so let's snip that out.

The Engineering Security Officer should have access to only general Engineering and Atmospherics. Construction pertains to certain rooms in maintenance I believe, and Engine-Equipment should be the one that grants access to APCs (lol). I don't think a security officer should have the latter one to be honest, but I think we'll be stretching the scope of this PR. Telecommunications is a bit weird, it's a critical station function, but I think you also shouldn't be able to nick one goon's ID and have access, so let's give it to them only when it's "needed".

The Medical Security Officer should have access to only the general Medbay Area and the Morgue, in case someone starts trotting on the doctor's turf, or if there's someone doing unsavory things to the bodies while the doctors are away. They will not have access to the specialized (dangerous) areas unless the ratio of secoffs to the population is low enough should it necessitate it (Plumbing Room, Pharmacy, Virology). I also added Surgery to the scaling access, but I'm iffy on that one. I don't particularly see why they should have it as a base access, but I also do see there being some need in dire straits (in relation to helping people, not tiding).

The Science Security Officer definitely got a huge cut. They now only have general access to R&D and normal scientist areas like the lathe room, circuits lab (presumably)since these are generally trafficked areas, but I definitely clamped down on additional access they might get in a "normally balanced" situation (no ordnance+storage, no xenobio, no genetics, no to robotics, etc.) They don't have a particular use in these areas and can even be a bit obstructive to flow in normal circumstances, but if abnormal circumstances arise and there's not a lot of security hands-on-deck, then their access is expanded.

Honestly, balancing this both makes sense and is conversely rather odd. I'm just running off what we already hold to be true and expected (or at least as of the last two months), and we can go from there.
Changelog

cl
balance: Nanotrasen realized that the more access they had on their cards was costing them a pretty penny, so they trimmed back the number of accesses a certain departmental Security Guard might have. However, any given guard will get back a greater amount of accesses depending on how many security guards there are in relation to the population.
config: Hey server operators, listen! We've changed up how Departmental Security Officers get their accesses, so be sure to review the DEPSEC_ACCESS_LEVEL config number to see what you want to work best for your server.
/cl

Also, every single line of code found in 4533f07 that is now presently in this PR is deliberate

---

