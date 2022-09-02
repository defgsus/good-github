## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-09-01](docs/good-messages/2022/2022-09-01.md)


2,214,727 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,214,727 were push events containing 3,372,649 commit messages that amount to 252,033,031 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 49 messages:


## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[5347f53ea7...](https://github.com/pytorch/pytorch/commit/5347f53ea7092bc2dc7ddefb159dcc5848dcf95b)
#### Thursday 2022-09-01 00:47:12 by Andrew Gu

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
## [ammarfaizi2/linux-fork](https://github.com/ammarfaizi2/linux-fork)@[035cc471a3...](https://github.com/ammarfaizi2/linux-fork/commit/035cc471a387ade69c4a17450ae4971db5de06be)
#### Thursday 2022-09-01 01:01:08 by Johannes Weiner

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
## [Mycroft-Studios/qb-core](https://github.com/Mycroft-Studios/qb-core)@[9d83a952c2...](https://github.com/Mycroft-Studios/qb-core/commit/9d83a952c29fdfd3fb3ca77a45329556a32368f5)
#### Thursday 2022-09-01 01:09:07 by uShifty

feat: Implement QBCore.Shared.VehicleHashs 

Describe Pull request
Indexs the vehicles jenkins joaat(Hash) value as the key of the table as the key so we dont have to do some shitty ass loop through the vehicles comparing joaat values. I have no clue why this secondary table was removed in the first place if I had to guess people were lazy but this should help the lazys by automatically filling the table.

Questions (please complete the following information):
Have you personally loaded this code into an updated qbcore project and checked all it's functionality? [yes/no] (Be honest) 
Yes

Does your code fit the style guidelines? [yes/no] 
Yes

Does your PR fit the contribution guidelines? [yes/no]
Yes

---
## [git/git](https://github.com/git/git)@[2f954678ae...](https://github.com/git/git/commit/2f954678ae0aad2e2ae7494d08830fc4476fef65)
#### Thursday 2022-09-01 01:12:25 by Ævar Arnfjörð Bjarmason

cocci: make "coccicheck" rule incremental

Optimize the very slow "coccicheck" target to take advantage of
incremental rebuilding, and fix outstanding dependency problems with
the existing rule.

The rule is now faster both on the initial run as we can make better
use of GNU make's parallelism than the old ad-hoc combination of
make's parallelism combined with $(SPATCH_BATCH_SIZE) and/or the
"--jobs" argument to "spatch(1)".

It also makes us *much* faster when incrementally building, it's now
viable to "make coccicheck" as topic branches are merged down.

The rule didn't use FORCE (or its equivalents) before, so a:

	make coccicheck
	make coccicheck

Would report nothing to do on the second iteration. But all of our
patch output depended on all $(COCCI_SOURCES) files, therefore e.g.:

    make -W grep.c coccicheck

Would do a full re-run, i.e. a a change in a single file would force
us to do a full re-run.

The reason for this (not the initial rationale, but my analysis) is:

* Since we create a single "*.cocci.patch+" we don't know where to
  pick up where we left off, or how to incrementally merge e.g. a
  "grep.c" change with an existing *.cocci.patch.

* We've been carrying forward the dependency on the *.c files since
  63f0a758a06 (add coccicheck make target, 2016-09-15) the rule was
  initially added as a sort of poor man's dependency discovery.

  As we don't include other *.c files depending on other *.c files
  has always been broken, as could be trivially demonstrated
  e.g. with:

       make coccicheck
       make -W strbuf.h coccicheck

  However, depending on the corresponding *.c files has been doing
  something, namely that *if* an API change modified both *.c and *.h
  files we'd catch the change to the *.h we care about via the *.c
  being changed.

  For API changes that happened only via *.h files we'd do the wrong
  thing before this change, but e.g. for function additions (not
  "static inline" ones) catch the *.h change by proxy.

Now we'll instead:

 * Create a <RULE>/<FILE> pair in the .build directory, E.g. for
   swap.cocci and grep.c we'll create
   .build/contrib/coccinelle/swap.cocci.patch/grep.c.

   That file is the diff we'll apply for that <RULE>-<FILE>
   combination, if there's no changes to me made (the common case)
   it'll be an empty file.

 * Our generated *.patch
   file (e.g. contrib/coccinelle/swap.cocci.patch) is now a simple "cat
   $^" of all of all of the <RULE>/<FILE> files for a given <RULE>.

   In the case discussed above of "grep.c" being changed we'll do the
   full "cat" every time, so they resulting *.cocci.patch will always
   be correct and up-to-date, even if it's "incrementally updated".

   See 1cc0425a27c (Makefile: have "make pot" not "reset --hard",
   2022-05-26) for another recent rule that used that technique.

As before we'll:

 * End up generating a contrib/coccinelle/swap.cocci.patch, if we
   "fail" by creating a non-empty patch we'll still exit with a zero
   exit code.

   Arguably we should move to a more Makefile-native way of doing
   this, i.e. fail early, and if we want all of the "failed" changes
   we can use "make -k", but as the current
   "ci/run-static-analysis.sh" expects us to behave this way let's
   keep the existing behavior of exhaustively discovering all cocci
   changes, and only failing if spatch itself errors out.

Further implementation details & notes:

 * Before this change running "make coccicheck" would by default end
   up pegging just one CPU at the very end for a while, usually as
   we'd finish whichever *.cocci rule was the most expensive.

   This could be mitigated by combining "make -jN" with
   SPATCH_BATCH_SIZE, see 960154b9c17 (coccicheck: optionally batch
   spatch invocations, 2019-05-06). But doing so required careful
   juggling, as e.g. setting both to 4 would yield 16 workers.

   There will be cases where getting rid of "SPATCH_BATCH_SIZE" makes
   things worse, but a from-scratch "make coccicheck" with the default
   of SPATCH_BATCH_SIZE=1 (and tweaking it doesn't make a difference)
   is faster (~3m36s v.s. ~3m56s) with this approach, as we can feed
   the CPU more work in a less staggered way.

 * Getting rid of "SPATCH_BATCH_SIZE" particularly helps in cases
   where the default of 1 yields parallelism under "make coccicheck",
   but then running e.g.:

       make -W contrib/coccinelle/swap.cocci coccicheck

   I.e. before that would use only one CPU core, until the user
   remembered to adjust "SPATCH_BATCH_SIZE" differently than the
   setting that makes sense when doing a non-incremental run of "make
   coccicheck".

Outstanding issues & future work:

 * We could get rid of "--all-includes" in favor of manually
   specifying a list of includes to give to "spatch(1)".

   As noted upthread of [1] a naïve removal of "--all-includes" will
   result in broken *.cocci patches, but if we know the exhaustive
   list of includes via COMPUTE_HEADER_DEPENDENCIES we don't need to
   re-scan for them, we could grab the headers to include from the
   .depend.d/<file>.o.d and supply them with the "--include" option to
   spatch(1).q

1. https://lore.kernel.org/git/87ft18tcog.fsf@evledraar.gmail.com/

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [sigp/lighthouse](https://github.com/sigp/lighthouse)@[66eca1a882...](https://github.com/sigp/lighthouse/commit/66eca1a88218462235cb76a116dc3c6a1853444f)
#### Thursday 2022-09-01 01:17:27 by Michael Sproul

Refactor op pool for speed and correctness (#3312)

## Proposed Changes

This PR has two aims: to speed up attestation packing in the op pool, and to fix bugs in the verification of attester slashings, proposer slashings and voluntary exits. The changes are bundled into a single database schema upgrade (v12).

Attestation packing is sped up by removing several inefficiencies: 

- No more recalculation of `attesting_indices` during packing.
- No (unnecessary) examination of the `ParticipationFlags`: a bitfield suffices. See `RewardCache`.
- No re-checking of attestation validity during packing: the `AttestationMap` provides attestations which are "correct by construction" (I have checked this using Hydra).
- No SSZ re-serialization for the clunky `AttestationId` type (it can be removed in a future release).

So far the speed-up seems to be roughly 2-10x, from 500ms down to 50-100ms.

Verification of attester slashings, proposer slashings and voluntary exits is fixed by:

- Tracking the `ForkVersion`s that were used to verify each message inside the `SigVerifiedOp`. This allows us to quickly re-verify that they match the head state's opinion of what the `ForkVersion` should be at the epoch(s) relevant to the message.
- Storing the `SigVerifiedOp` on disk rather than the raw operation. This allows us to continue track the fork versions after a reboot.

This is mostly contained in this commit 52bb1840ae5c4356a8fc3a51e5df23ed65ed2c7f.

## Additional Info

The schema upgrade uses the justified state to re-verify attestations and compute `attesting_indices` for them. It will drop any attestations that fail to verify, by the logic that attestations are most valuable in the few slots after they're observed, and are probably stale and useless by the time a node restarts. Exits and proposer slashings and similarly re-verified to obtain `SigVerifiedOp`s.

This PR contains a runtime killswitch `--paranoid-block-proposal` which opts out of all the optimisations in favour of closely verifying every included message. Although I'm quite sure that the optimisations are correct this flag could be useful in the event of an unforeseen emergency.

Finally, you might notice that the `RewardCache` appears quite useless in its current form because it is only updated on the hot-path immediately before proposal. My hope is that in future we can shift calls to `RewardCache::update` into the background, e.g. while performing the state advance. It is also forward-looking to `tree-states` compatibility, where iterating and indexing `state.{previous,current}_epoch_participation` is expensive and needs to be minimised.

---
## [FenPhoenix/AngelLoader](https://github.com/FenPhoenix/AngelLoader)@[80265c3515...](https://github.com/FenPhoenix/AngelLoader/commit/80265c35159a6cb7c8a8efbeaa255ad167cbd6ef)
#### Thursday 2022-09-01 01:35:41 by FenPhoenix

Do something(?!) to the project file to fix nullability fail

Static analyzer started doing the bullshit where it thinks we're not in a nullable context for some reason. The project file is the same but it says it's different now. I have no goddamn idea whatever I hate computers

---
## [motiejus/zig](https://github.com/motiejus/zig)@[a31b449b55...](https://github.com/motiejus/zig/commit/a31b449b55c32eba1cb61a48753a6fc98696c98f)
#### Thursday 2022-09-01 01:49:21 by Andrew Kelley

make LLVM and Clang emit DWARF 4 instead of 5

This reverts 6d679eb2bcbe76e389c02e0bb4d4c4feb2847783 and additionally
changes the command line parameters passed to Clang to match.

Clang 14 defaults to DWARFv5 which is an interesting choice. v5 has been
out for 5 years and yet Valgrind does not support it, and apparently
neither does either GDB or LLD, I haven't determined which, but I wasn't
able to use GDB to debug my LLVM-emitted dwarf 5 zig code that was linked
with LLD.

A couple years ago when I was working on the self-hosted ELF linker, I
emitted DWARFv5 but then downgraded to v4 when I realized that third
party tools were stuck in the past. Years later, they still are.

Hopefully, Clang 14's bold move will inspire third party tools to get
their shit together, however, in the meantime, everything's broken, so
we're passing `-gdwarf-4` to clang and instructing LLVM to emit DWARFv4.

Note that Zig's std.debug code *does* support DWARFv5 already as of a
previous commit that I made today.

---
## [jsal13/black](https://github.com/jsal13/black)@[0019261abc...](https://github.com/jsal13/black/commit/0019261abcf6d9e564ba32d3cc15534b9026f29e)
#### Thursday 2022-09-01 02:07:29 by Richard Si

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
## [alltheplaces/alltheplaces](https://github.com/alltheplaces/alltheplaces)@[c7b46c2663...](https://github.com/alltheplaces/alltheplaces/commit/c7b46c26636f460702c1eec68846959710613515)
#### Thursday 2022-09-01 02:35:02 by Joe Dixon

Fix spar_gb, causes a small collateral stir in "geo" functions.

So SPAR GB which I recently converted to "sitemap" decided to change their back-end. Such is life.
So back to the old approach except this time use a more structural approach to getting UK outward postal codes.
Grab a public data file which also includes lat, lon etc of said postcodes.
Add a wrapper function in geo.py Also, found an eequivalent for the US, see new README.md.
The US function was tested with porting "vetco" to it. It works (a few more stores in fact!).
Later can port the other US ones and drop "us_zcta.csv"!
germany_centroids_80km_radius_country.csv was also dropped, the description poorly described the contents!
norma_de was the only one using it. Ported to use centroids and now finds more stores!
Finally dict_parser.py was updated, driven by the spar_gb changes. This brings in an extended dict
based on a lot of experience my end with it. Alternative is for everyone to add these one-by-one
and then worry about possibly side affects on interim new DictParser spiders.

---
## [ChoGGi/SurvivingMars_CheatMods](https://github.com/ChoGGi/SurvivingMars_CheatMods)@[6d93b1cdb3...](https://github.com/ChoGGi/SurvivingMars_CheatMods/commit/6d93b1cdb31755783fe297b58adbb452ab789af0)
#### Thursday 2022-09-01 02:49:49 by ChoGGi

Expanded Cheat Menu:

### Fixed:
- A couple instances of UICity I somehow missed.

Lib:

- Log spam from AttachToNearestDome().
- You can use OpenExamineDelayed()/exd() before classes process (err re-process for mods).
	> It'll open all stored objs after ClassesPostprocess, so some stuff can change, but it's better than naught.

Mods:

Autonomous Extractors 0.4:
Mod option to disable autonomous.

Autonomous Factories:
Makes factories colonist-free for people that don't like colonists?
I know it's not really autonomous, but close enough...
Mod options to set the Auto Performance of factories without workers, and individual automation.

Fix Bugs 2.6:
Log spam from IsBuildingInDomeRange().

Game Rule Amazonian Mars:
You may only import female colonists (exception: tourists).
Male tourists "provide" children (Snu-snu, mod option for larger female colonist models).
Non-female children are culled at birth (lower birth rate).
and just in case a daily cull of any non-tourist non-female colonists on Mars (mini-soylent green).

Lock Workplace 1.5:
Seniors Override (default enabled).

Lower Maintenance In Dome 0.2/Lower Maintenance 0.2:
Indoor tribby issue (thanks SoftwareSimian).

github@choggi.org

---
## [majestrate/loki-network](https://github.com/majestrate/loki-network)@[196a552d51...](https://github.com/majestrate/loki-network/commit/196a552d511d95f0c3463950ff034316d5d4ecb8)
#### Thursday 2022-09-01 03:00:57 by Jeff

tweaks for wine and yarn for gui

* allow specifying a custom yarn binary for building the gui using -DYARN= cmake option
* unset DISPLAY when calling wine because i hate popups
* do not rebuild gui when building for windows
* by setting the magical undocumented env var USE_SYSTEM_7ZA to 'true' we can have the pile of npm bullshit code use our system's local 7z binary instead of the probably not backdoored binary from npm, yes for real. i hate nodejs so god damn much you have no fucking idea
* allow providing a custom gui from a zip file via -DGUI_ZIP_FILE cmake option

---
## [Linefate/react](https://github.com/Linefate/react)@[b6978bc38f...](https://github.com/Linefate/react/commit/b6978bc38f6788c7e73982b9fd2771aabdf36f15)
#### Thursday 2022-09-01 03:49:46 by Andrew Clark

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
## [sciatti/pi-camera-streaming](https://github.com/sciatti/pi-camera-streaming)@[1206fa43ae...](https://github.com/sciatti/pi-camera-streaming/commit/1206fa43aeecec18cee7b49a4e00b833b94d5f4b)
#### Thursday 2022-09-01 04:18:20 by Salvatore Ciatti

Hello there.

You've found me. The big, important commit. The one where I went from some random collection of files into an actual readable repository.

I won't tell you all my secrets. Just know that I've changed a lot of things, soon I'll be buried deep in this project and I'll be very hard to find.

Anyway the changes here are big and important but not hard to follow. There's a bunch of junk that I deleted because I haven't used it in months and the direction of the project has moved away from that stuff anyway. Experiments with CPP and Cython are gone, the earliest expirements I had with python are all gone because they were terrible and sucked and thus not very useful anymore.

I've rebuilt the python directory to have a small number of testing files (which will probably be refactored and made into more helpful files) from the sigma delta estimation testing I was doing, and I have created the one new development file to rule them all. That's the motion_detection.py file sitting all by its lonesome in the root of the python/ directory.

There's now a README that will be updated throughout the lifespan of the project to keep myself in order and keep a line of tasks in development.

That should mostly cover the changes. Enjoy.

---
## [ppker/zulip-mobile](https://github.com/ppker/zulip-mobile)@[0af1d1133c...](https://github.com/ppker/zulip-mobile/commit/0af1d1133c50f38057877eba063f837f82b961bd)
#### Thursday 2022-09-01 04:19:36 by Chris Bobbe

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
## [Kitsunemitsu/lobotomy-corp13](https://github.com/Kitsunemitsu/lobotomy-corp13)@[9d2db72bc3...](https://github.com/Kitsunemitsu/lobotomy-corp13/commit/9d2db72bc3788d85bc8a03064e34ac6bdc0c7358)
#### Thursday 2022-09-01 05:40:37 by Killer7luis

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

Update we_can_change_anything.dm

a

grammer

---
## [Dark-Matter7232/CosmicFresh-Hanoip](https://github.com/Dark-Matter7232/CosmicFresh-Hanoip)@[bb0778d383...](https://github.com/Dark-Matter7232/CosmicFresh-Hanoip/commit/bb0778d383e8c0b49af8c6e73aef4abb68b3763b)
#### Thursday 2022-09-01 08:15:16 by Peter Zijlstra

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
## [lnd1g0/Fedoraware](https://github.com/lnd1g0/Fedoraware)@[f370cbf8ed...](https://github.com/lnd1g0/Fedoraware/commit/f370cbf8edda9593758c3d24244b985d7c993735)
#### Thursday 2022-09-01 09:15:57 by Baan

fix.

the beep beep beep beep beep beep shit was fucking annoying as on god.

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[048850041c...](https://github.com/treckstar/yolo-octo-hipster/commit/048850041c3f4d9917f2352b6069659d45f494ae)
#### Thursday 2022-09-01 09:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [ammarfaizi2/linux-block](https://github.com/ammarfaizi2/linux-block)@[fe125bff56...](https://github.com/ammarfaizi2/linux-block/commit/fe125bff56e6c719e474ba25c354794a56a4fa2f)
#### Thursday 2022-09-01 10:16:07 by Peter Zijlstra

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
## [Edisonwantstolearn/learn-python](https://github.com/Edisonwantstolearn/learn-python)@[b9c3de7f6f...](https://github.com/Edisonwantstolearn/learn-python/commit/b9c3de7f6f76ffdf12a81ac500f77eeb2f753c48)
#### Thursday 2022-09-01 10:56:47 by Edisonwantstolearn

Create magic8 with optional challenge

I want to contribute my solution to the magic8 along my attempt to solve the optional challenges. I've learned in google that using .formats makes my life easier adding variables without worrying about their data types.

---
## [adi2011/lightning](https://github.com/adi2011/lightning)@[29c6884468...](https://github.com/adi2011/lightning/commit/29c6884468face50146b6f9a6c215d52c729f25d)
#### Thursday 2022-09-01 13:16:24 by niftynei

bkpr: add journal entry for offset account balances; report listbalances

When the node starts up, it records missing/updated account balances
to the 'channel' events... which is kinda fucked for wallet + external
events now that i think about it but these are all treated the same
anyway so it's fine.

This is the magic piece that lets your bookkeeping data startup ok on an
already running/established node.

---
## [al42and/llvm](https://github.com/al42and/llvm)@[15f3cd6bfc...](https://github.com/al42and/llvm/commit/15f3cd6bfc670ba6106184a903eb04be059e5977)
#### Thursday 2022-09-01 13:36:02 by Matheus Izvekov

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
## [amir73il/linux](https://github.com/amir73il/linux)@[d3807f9570...](https://github.com/amir73il/linux/commit/d3807f95701228c2a2f994ca410af48594e24812)
#### Thursday 2022-09-01 13:36:46 by Yang Xu

fs: move S_ISGID stripping into the vfs_*() helpers

commit 1639a49ccdce58ea248841ed9b23babcce6dbb0b upstream.

[remove userns argument of helpers for 5.10.y backport]

Move setgid handling out of individual filesystems and into the VFS
itself to stop the proliferation of setgid inheritance bugs.

Creating files that have both the S_IXGRP and S_ISGID bit raised in
directories that themselves have the S_ISGID bit set requires additional
privileges to avoid security issues.

When a filesystem creates a new inode it needs to take care that the
caller is either in the group of the newly created inode or they have
CAP_FSETID in their current user namespace and are privileged over the
parent directory of the new inode. If any of these two conditions is
true then the S_ISGID bit can be raised for an S_IXGRP file and if not
it needs to be stripped.

However, there are several key issues with the current implementation:

* S_ISGID stripping logic is entangled with umask stripping.

  If a filesystem doesn't support or enable POSIX ACLs then umask
  stripping is done directly in the vfs before calling into the
  filesystem.
  If the filesystem does support POSIX ACLs then unmask stripping may be
  done in the filesystem itself when calling posix_acl_create().

  Since umask stripping has an effect on S_ISGID inheritance, e.g., by
  stripping the S_IXGRP bit from the file to be created and all relevant
  filesystems have to call posix_acl_create() before inode_init_owner()
  where we currently take care of S_ISGID handling S_ISGID handling is
  order dependent. IOW, whether or not you get a setgid bit depends on
  POSIX ACLs and umask and in what order they are called.

  Note that technically filesystems are free to impose their own
  ordering between posix_acl_create() and inode_init_owner() meaning
  that there's additional ordering issues that influence S_SIGID
  inheritance.

* Filesystems that don't rely on inode_init_owner() don't get S_ISGID
  stripping logic.

  While that may be intentional (e.g. network filesystems might just
  defer setgid stripping to a server) it is often just a security issue.

This is not just ugly it's unsustainably messy especially since we do
still have bugs in this area years after the initial round of setgid
bugfixes.

So the current state is quite messy and while we won't be able to make
it completely clean as posix_acl_create() is still a filesystem specific
call we can improve the S_SIGD stripping situation quite a bit by
hoisting it out of inode_init_owner() and into the vfs creation
operations. This means we alleviate the burden for filesystems to handle
S_ISGID stripping correctly and can standardize the ordering between
S_ISGID and umask stripping in the vfs.

We add a new helper vfs_prepare_mode() so S_ISGID handling is now done
in the VFS before umask handling. This has S_ISGID handling is
unaffected unaffected by whether umask stripping is done by the VFS
itself (if no POSIX ACLs are supported or enabled) or in the filesystem
in posix_acl_create() (if POSIX ACLs are supported).

The vfs_prepare_mode() helper is called directly in vfs_*() helpers that
create new filesystem objects. We need to move them into there to make
sure that filesystems like overlayfs hat have callchains like:

sys_mknod()
-> do_mknodat(mode)
   -> .mknod = ovl_mknod(mode)
      -> ovl_create(mode)
         -> vfs_mknod(mode)

get S_ISGID stripping done when calling into lower filesystems via
vfs_*() creation helpers. Moving vfs_prepare_mode() into e.g.
vfs_mknod() takes care of that. This is in any case semantically cleaner
because S_ISGID stripping is VFS security requirement.

Security hooks so far have seen the mode with the umask applied but
without S_ISGID handling done. The relevant hooks are called outside of
vfs_*() creation helpers so by calling vfs_prepare_mode() from vfs_*()
helpers the security hooks would now see the mode without umask
stripping applied. For now we fix this by passing the mode with umask
settings applied to not risk any regressions for LSM hooks. IOW, nothing
changes for LSM hooks. It is worth pointing out that security hooks
never saw the mode that is seen by the filesystem when actually creating
the file. They have always been completely misplaced for that to work.

The following filesystems use inode_init_owner() and thus relied on
S_ISGID stripping: spufs, 9p, bfs, btrfs, ext2, ext4, f2fs, hfsplus,
hugetlbfs, jfs, minix, nilfs2, ntfs3, ocfs2, omfs, overlayfs, ramfs,
reiserfs, sysv, ubifs, udf, ufs, xfs, zonefs, bpf, tmpfs.

All of the above filesystems end up calling inode_init_owner() when new
filesystem objects are created through the ->mkdir(), ->mknod(),
->create(), ->tmpfile(), ->rename() inode operations.

Since directories always inherit the S_ISGID bit with the exception of
xfs when irix_sgid_inherit mode is turned on S_ISGID stripping doesn't
apply. The ->symlink() and ->link() inode operations trivially inherit
the mode from the target and the ->rename() inode operation inherits the
mode from the source inode. All other creation inode operations will get
S_ISGID handling via vfs_prepare_mode() when called from their relevant
vfs_*() helpers.

In addition to this there are filesystems which allow the creation of
filesystem objects through ioctl()s or - in the case of spufs -
circumventing the vfs in other ways. If filesystem objects are created
through ioctl()s the vfs doesn't know about it and can't apply regular
permission checking including S_ISGID logic. Therfore, a filesystem
relying on S_ISGID stripping in inode_init_owner() in their ioctl()
callpath will be affected by moving this logic into the vfs. We audited
those filesystems:

* btrfs allows the creation of filesystem objects through various
  ioctls(). Snapshot creation literally takes a snapshot and so the mode
  is fully preserved and S_ISGID stripping doesn't apply.

  Creating a new subvolum relies on inode_init_owner() in
  btrfs_new_subvol_inode() but only creates directories and doesn't
  raise S_ISGID.

* ocfs2 has a peculiar implementation of reflinks. In contrast to e.g.
  xfs and btrfs FICLONE/FICLONERANGE ioctl() that is only concerned with
  the actual extents ocfs2 uses a separate ioctl() that also creates the
  target file.

  Iow, ocfs2 circumvents the vfs entirely here and did indeed rely on
  inode_init_owner() to strip the S_ISGID bit. This is the only place
  where a filesystem needs to call mode_strip_sgid() directly but this
  is self-inflicted pain.

* spufs doesn't go through the vfs at all and doesn't use ioctl()s
  either. Instead it has a dedicated system call spufs_create() which
  allows the creation of filesystem objects. But spufs only creates
  directories and doesn't allo S_SIGID bits, i.e. it specifically only
  allows 0777 bits.

* bpf uses vfs_mkobj() but also doesn't allow S_ISGID bits to be created.

The patch will have an effect on ext2 when the EXT2_MOUNT_GRPID mount
option is used, on ext4 when the EXT4_MOUNT_GRPID mount option is used,
and on xfs when the XFS_FEAT_GRPID mount option is used. When any of
these filesystems are mounted with their respective GRPID option then
newly created files inherit the parent directories group
unconditionally. In these cases non of the filesystems call
inode_init_owner() and thus did never strip the S_ISGID bit for newly
created files. Moving this logic into the VFS means that they now get
the S_ISGID bit stripped. This is a user visible change. If this leads
to regressions we will either need to figure out a better way or we need
to revert. However, given the various setgid bugs that we found just in
the last two years this is a regression risk we should take.

Associated with this change is a new set of fstests to enforce the
semantics for all new filesystems.

Link: https://lore.kernel.org/ceph-devel/20220427092201.wvsdjbnc7b4dttaw@wittgenstein [1]
Link: e014f37db1a2 ("xfs: use setattr_copy to set vfs inode attributes") [2]
Link: 01ea173e103e ("xfs: fix up non-directory creation in SGID directories") [3]
Link: fd84bfdddd16 ("ceph: fix up non-directory creation in SGID directories") [4]
Link: https://lore.kernel.org/r/1657779088-2242-3-git-send-email-xuyang2018.jy@fujitsu.com
Suggested-by: Dave Chinner <david@fromorbit.com>
Suggested-by: Christian Brauner (Microsoft) <brauner@kernel.org>
Reviewed-by: Darrick J. Wong <djwong@kernel.org>
Reviewed-and-Tested-by: Jeff Layton <jlayton@kernel.org>
Signed-off-by: Yang Xu <xuyang2018.jy@fujitsu.com>
[<brauner@kernel.org>: rewrote commit message]
Signed-off-by: Christian Brauner (Microsoft) <brauner@kernel.org>
Signed-off-by: Amir Goldstein <amir73il@gmail.com>

---
## [LucZot/DeepLabCut-live](https://github.com/LucZot/DeepLabCut-live)@[ce8e96a80d...](https://github.com/LucZot/DeepLabCut-live/commit/ce8e96a80d563e0b55f3a998aafdd10fcc2ec26c)
#### Thursday 2022-09-01 14:06:19 by Jonny Saunders

Swap Packaging to Poetry (#60)

* Swapping packaging to Poetry
- main thing is removal of setup.py and requirements.txt, instead we have pyproject.toml and poetry.lock. pyproject is the project description that contains everything that setup.py does (i was careful to keep it as similar as possible to the existing one while also adding version constraints that allow a successful build/install), and the poetry.lock contains the exact specification of what to install
- I bumped up the minimum python from 3.5 to 3.6.1 to be able to install a few packages, both 3.5 and 3.6 are EOL and we should think of bumping this up further.

Also
- added some type hints to the DLCLive class which was bothering me to not have tab completion when i've been using it lol
- DLCLive object tries to mutate something that is by default a tuple, which should cause an error if anyone tries to use tflite and dynamic (instead of warning and repairing as is intended)
- Using Pathlib to resolve the path and check that it exists when loading configuration, this gives more helpful error messages bc people know where DLC is looking in their filesystem/resolves ambiguity of relative paths
- added a CITATION.cff file <3

* oop forgot to quote the pseudo-imported Processor class

* did not see we had github actions in here!
- removed pip install requirements
- removed pytest tests (i don't see any!?)
- installing package and running test from already checked-out copy rather than pip installing from git://
- the packaging script doesn't look like it's doing anything, but i'd be happy to write one that autodeploys on tagged commits to master

* - added argument parser to be able to suppress display on testing, and then call it when doing the tests
- also install and run using poetry because windows paths are an abominable hell
- tensorflow 2.7 only support python >3.7

* ohhhh Display is still instantiated even if the `display` arg is false because it gets instantiated before the check happens whether it should be saved or not.
also limited tf versions for python <3.7 because it has to like do the ridiculous pip thing where it downloads all of them for some reason

* arg not being passed through, does windows want to run poetry yet?

* OH need to put argparser within the function

- also cleaned up file handling in test function. Previously the video file was downloaded and not used, and lots of implicit paths that seem to be causing people trouble when running it.

* try catch removing temporary directory because WINDOWS GOD DAMN IT

* ok 3.6 is EOL anyway and it's causing all the problems

---
## [canalplus/rx-player](https://github.com/canalplus/rx-player)@[7fbe7ef5eb...](https://github.com/canalplus/rx-player/commit/7fbe7ef5eb409e59f60584bde2a4ab31a461440b)
#### Thursday 2022-09-01 14:13:37 by Paul Berberian

Add magic Jest config property to Make Unit Tests Work Again (MUTWA)

It seems that Jest 28+, for some obscure reasons, now fail importing
dependencies using a ESM-style importing/exporting syntax - despite it
working before. It wasn't in their migration guide nor in their
changelog, so it was difficult to find how to work-around that issue.

In the end, I did what any developer who want to get things done should
do and just browsed the web to test every options under the sun that
could fix the issue.
Turns out the one in this commit has a good effect, though god knows
what it's actually doing!

Thanks https://www.sobyte.net/post/2022-06/jest/ to give me this hint,
and for apparently understanding what you're doing.

I am personally decidedly 2dumb4jest, which slowly leads me to dislike
this library very much for consequentially purely ego reasons.

---
## [ngoduyanh/nrs-impl-kt](https://github.com/ngoduyanh/nrs-impl-kt)@[406f6b4ec7...](https://github.com/ngoduyanh/nrs-impl-kt/commit/406f6b4ec700c2103cb3fcc347ba3a3faad4b4b9)
#### Thursday 2022-09-01 14:52:29 by ngoduyanh

fix(impl): :art: Split memes + Escha waifu

The starry sky that was always crying alone  wishes are gone  A gentle voice that envelops everything  Staring at you, you're getting far away  sky reflected in azure  i miss you where are you now  I stepped into the patchy unknown  The sky cleared and you were standing there  I will never be able to touch you  Unknowingly, I was calling your name  I'm chasing you now, who's getting far away  She hasn't told you yet  the day we lived  The sea and the sky intersect  I can't see you anymore, it's lonely  still going on  In that place where we vowed, we snuggled together  Let's go on the road where the two of us will start forever  start walking without turning around  The sea dyed in ultramarine blue  i miss you where are you now  Sing words to the passing days  The sea has cleared and you remain unchanged there  Move the stopped needle little by little  I'm forgetting the shape of her that goes round and round  Chasing you who is getting far away  wait wait don't go  the day we lived  The sea and the sky intersect  It's already dawn, it's dazzling  still in the corner of my memory  That moment of laughter fades away  You and I repeat and open the next door  coloring  Goodbye and goodbye  I disappear in front of you  Farewell already  Beyond the sky, beyond the sea, beyond  While watching over the horizon  My voice won't reach you anymore, but don't worry  The blue universe, the same world  The indigo that still overflows  In that place where we vowed, let's meet her again  The two of us will continue forever, don't cry  Let's hold hands, let's laugh together

---
## [rothquel/OK-Diver](https://github.com/rothquel/OK-Diver)@[22ad514941...](https://github.com/rothquel/OK-Diver/commit/22ad514941d46475f4f3f40b941955d666f52014)
#### Thursday 2022-09-01 15:44:01 by Camila Contreras Barrera

honestly im sorry i cant remember what I did but I think I changed avatar, review card, and maybe some small details here and there ...:(

---
## [rothquel/OK-Diver](https://github.com/rothquel/OK-Diver)@[631ede3e40...](https://github.com/rothquel/OK-Diver/commit/631ede3e403b8f93b363c315264ccb7c11cc22b0)
#### Thursday 2022-09-01 15:44:01 by Nic Rothquel

Merge pull request #112 from rothquel/adding_avatar_class_in_avatar_of_review

honestly im sorry i cant remember what I did but I think I changed av…

---
## [wrye-bash/wrye-bash](https://github.com/wrye-bash/wrye-bash)@[acd54db433...](https://github.com/wrye-bash/wrye-bash/commit/acd54db433e62598d4dcf1cad41a84d0c86e2cae)
#### Thursday 2022-09-01 15:47:05 by Infernio

Rework the Mods tab's context menu RRR

You now what really doesn't help the first time user experience?
Throwing a giant context menu in their face. Sometimes people report
they can't find the Rebuild Patch option even though it's right there -
almost certainly because in order to find it, their eyes have to scan
through up to *twenty-eight* menu items.

This commit brings a similar refactoring to what we did to the
Installers tab to the Mods tab as well. There are now only twelve
top-level items, exposing the most commonly used features (e.g. Rebuild
Patch, Move to, Jump to Installer, etc.) at the top level and placing
the less commonly used features in sub-menus (Info and Plugin, in this
case - plus an Advanced menu for the weird shit:tm:).

Note 'Export Patch Configuration' getting dropped entirely - you can
already do that via Rebuild Patch... > Export, plus it was confusing
that you could export like this but not *import* that way. And on top of
all that, it would have lead to unintuitive UI with the new context
menu, since I would have either had to move it to Plugin.. or kept such
a rarely used command at top level.

Didn't update the docs for this because they also haven't been updated
for the latest Installers changes yet and I want to do all that in one
go with updated images and all.

Closes # 643 <--- RRR

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[f24baf88f0...](https://github.com/treckstar/yolo-octo-hipster/commit/f24baf88f0787a4638c92b8bf47b889c28f4ebea)
#### Thursday 2022-09-01 16:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [AlteredArt/Breathe](https://github.com/AlteredArt/Breathe)@[4b775d5cb9...](https://github.com/AlteredArt/Breathe/commit/4b775d5cb9e7cbb4f84701262a49ced9577ee16c)
#### Thursday 2022-09-01 16:36:49 by Jared Matta

Merge pull request #90 from AlteredArt/XalienX

i hate my life

---
## [samay-sharma/postgres](https://github.com/samay-sharma/postgres)@[7fed801135...](https://github.com/samay-sharma/postgres/commit/7fed801135bae14d63b11ee4a10f6083767046d8)
#### Thursday 2022-09-01 16:37:46 by Tom Lane

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
## [yahiamarzouk/coordinape](https://github.com/yahiamarzouk/coordinape)@[2a76043a17...](https://github.com/yahiamarzouk/coordinape/commit/2a76043a17dd06ac4e47e8d2434b5ef9113fe19c)
#### Thursday 2022-09-01 17:46:05 by topocount

bugfix: enable FormTokenField to have an empty input (#1277)

One of the major considerations during the FormTokenField (and downstream) refactor was allowing for empty string inputs. This enables for much cleaner UX, since users aren't typing "around" a zero
and in my opinion, makes us look like we know what we're doing as devs. There are other hacks that could make the UX better than the incumbent, but why not just make it behave correctly and be done with it?

Co-authored-by: crabsinger <83605543+crabsinger@users.noreply.github.com>
Co-authored-by: zashton <17747090+zashton@users.noreply.github.com>

---
## [Sekoree/MikuSharp](https://github.com/Sekoree/MikuSharp)@[4ca99fecc4...](https://github.com/Sekoree/MikuSharp/commit/4ca99fecc495405e74f6919ae9f5138de682d04b)
#### Thursday 2022-09-01 18:29:01 by Lala Sabathil

Translation Generator (#7)

* Add output gen stuff

* Translation stuff

x

fix again

stuff

load translations from in/

make entities public

New icon and base translator app

Update MainWindow.xaml

stuff

short

x

save stuff

upgrade to .net6

add folder creation

fuck it

fff

file scope!!

Update MainWindow.xaml.cs

remove backup

update csproj

Bumb min windows version to 10.0.19041.0
Add metadata

stuff

stuff

remove entities and enums, we use dcs

save progress

change to dcs namespace

Remove miku images, this package will be part of dcs

re-add dcs projects

save stuff, i hate my life

new images for ac_cmds

---
## [Sekoree/MikuSharp](https://github.com/Sekoree/MikuSharp)@[094ef83009...](https://github.com/Sekoree/MikuSharp/commit/094ef8300945bc9d67476f8dad2c529e370b169d)
#### Thursday 2022-09-01 18:29:01 by Lala Sabathil

Slash Rewrite

Moderation: invite management
- Allow mods to enable or disable invites in case of raids
Update readme with new instructions how to use miku
clean up attributes and convert to ac attr
Remove prefix stuff
Bump MikuSharp to 4.0.0
Convert to file-scoped namespace
Remove Actions from dm
Cleanup derpy weeb
remove outdated jokes
switch nsfw stuff back to cnext and use mention prefix
Pull out database name to config
Minimize http client bullshit
Add backup sql data
remove breaking chars from playlists
Add news channel add
Bump package, switch to release
Upgrade timespan of 25 sec to 30 bcs of interactions
clean uppppp :airplane:
Add playlist autocomplete
Add json ignore to db conn string
rename autocompleteprovider class to *providers
Simplify get opts
make bilibili and nicovideo great again
Fix queue database operations
move console write to logger log<level>
kill info messages
Reimplement top.gg
add submodule nnn
add spotify & apple music support
Add translator project

Co-Authored-By: BloodDragooner <33168706+blooddragooner@users.noreply.github.com>
Co-Authored-By: Mira <mira@aitsys.dev>
Co-Authored-By: Nyuw~ <nyuw@aitsys.dev>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[9d772c4f13...](https://github.com/tgstation/tgstation/commit/9d772c4f13da35569d61d223c8a693dc157666b2)
#### Thursday 2022-09-01 19:07:15 by Jacquerel

Dimensional Anomaly (#69512)

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

---
## [TaleirOfDeynai/nai-context-userscript](https://github.com/TaleirOfDeynai/nai-context-userscript)@[59dc360b7a...](https://github.com/TaleirOfDeynai/nai-context-userscript/commit/59dc360b7aad60a0983239dc2b58397d45c82ec2)
#### Thursday 2022-09-01 19:53:33 by Taleir of Deynai

I hate this library...

But it's the only one that's really still maintained, and I don't want to roll my own.  I'll just work around all its Ruby-like magic that makes it feel very inconsistent.
Also, I had to drop the idea of pulling a specific commit from the repo with Napa, since the tests could not really deal with the fact the script needed to be inlined and executed on the global scope ...or I didn't feel like figuring out how to make it work that way.
So, instead I pulled a local copy, modified it so it was a CommonJS module, adapted its wonky types, and I guess I'll deal with updating it by hand now and then.  Or not.  Who really cares...?
What?  Why not just use the `@require` directive of user-scripts like the docs suggest?  ARE YOU FUCKING INSANE!?  Yeah, let's pull code from a random URL and execute it in a privileged context!  Great idea!  The file that's there could NEVER be replaced with something malicious at some future date!
No...  Instead, I will pull a copy, vet it myself, and use that knowingly safe copy instead.  Vetting it was easy because I had to reference the code directly to figure out all its weird jank; the docs are shit and incomplete.

---
## [dansmor7/terminal](https://github.com/dansmor7/terminal)@[9ccd6ecd74...](https://github.com/dansmor7/terminal/commit/9ccd6ecd744890b856f3d8a39ff0616c0e34d4fb)
#### Thursday 2022-09-01 20:12:39 by Mike Griese

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
## [dansmor7/terminal](https://github.com/dansmor7/terminal)@[8962f88f90...](https://github.com/dansmor7/terminal/commit/8962f88f907d86fd8684b66f7f3e32a2709e3237)
#### Thursday 2022-09-01 20:12:39 by Dustin L. Howett

Disable the VT color quirk for pwsh and modern inbox powershell (#13352)

In #6810, we introduced a "quirk" for all known versions of PowerShell
that suppressed their requests for black background/gray foreground.
This was done to avoid an [issue in PSReadline] where it would paint
black bars all over the screen if the default background color wasn't
the same as the ANSI black color.

Years have passed since that quirk was introduced. The underlying bug
was fixed, and the fix was released broadly long ago. It's time for us
to remove the quirk... almost.

Terminal still runs on versions of Windows that ship a broken version of
PSReadline. We must maintain the quirk there -- the user can't do
anything about it, and we would make their experience worse if we
removed the quirk entirely.

PowerShell 7.0 also ships a broken version of PSReadline. It is still in
support for another 6 months, but updates have been available for some
time. We can encourage users to update.

Therefore, we only need the quirk for Windows PowerShell, and then only
for specific versions of Windows.

_Inside Windows_, we don't even need that: we're guaranteed to be built
alongside a fixed version of PowerShell!

Closes #6807

[issue in PSReadline]: https://github.com/PowerShell/PSReadLine/issues/830#issuecomment-650508857

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[de04b3be80...](https://github.com/tgstation/tgstation/commit/de04b3be8082e37e4ff22b74b8f3feb6f38d03eb)
#### Thursday 2022-09-01 21:44:44 by MrMelbert

Kills `/obj/shapeshift_holder`, replaces it with `/datum/status_effect/shapechange_mob`, also does a lot of Wabbajack refactoring (#69091)


About The Pull Request

    Deletes /obj/shapeshift_holder, replaces it with /datum/status_effect/shapechange_mob
    Refactors Heretic worm form into a shapeshift spell
    Refactors Wabbajack, and associated code

Fixes #69117
Fixes #65653
Fixes #59127
Fixes #52786
Why It's Good For The Game

/obj/shapeshift_holder was one of the worst remaining abuses of /obj direct subtypes, so I replaced it with a cool fancy datum.

This also decouples the shapeshifting behavior entirely from the shapeshifting spell. So we have support for shapeshifted mobs not sourced from a spell. Which is neat, we could technically swap Wabbajack to use this in the future.
Changelog

cl Melbert
fix: Wabbajacking a shapeshifted mob no longer runtimes horribly. When a shapeshifted mob is wabbajacked, they'll now be removed from their shapeshift and stunned.
fix: Transforming via a shapeshift should no longer rob you of your hearing / runechat awareness.
fix: Shapeshifting plays nicer with holoparasites.
fix: Being polymorphed from a xeno to a non-xeno correctly makes you a non-xeno
refactor: Refactored shapeshifting, the shapeshift holder is now a status effect instead of an object.
refactor: Heretic worm form is a shapeshift spell now, this might have some minor behavioral changes but should overall be the same.
refactor: Refactored Wabbajack (+ cursed pool). Overall a bit more clean / consistent behavior.
/cl

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[bc90ded5b8...](https://github.com/tgstation/tgstation/commit/bc90ded5b8b0f4487ccec227fed24f514dbaa5ba)
#### Thursday 2022-09-01 21:47:31 by MrMelbert

Buffs Heretic Curses, Living Heart, Leeching Walk, and technically Entropic Plume by fixing some bugs (#69181)

About The Pull Request

    Heretic curses have been buffed / reworked.
        Curses can be cast on any crewmember, not just those who you have fingerprints to.
        Having an item present in the ritual that contains fingerprints OR blood dna of a crewmember who you are cursing will boost the curse, causing it to last longer (and be stronger? Still undecided, but there's support for it)
        Curses have a max range (64 by default) and don't work on people on a different z-level (Do not BTFO miners so easily)
        Corrosion curse's numbers have been tweaked due to this, and it can no longer cause vital organ failure

    Living Heart has been buffed
        Cooldown cut in half, and it provides a bit more thorough instructions
        Closes 

    Living heart targets who are located in non-turf locs and are off z-level will show as on the same z #67256

Leeching Walk has been buffed

    Rust will also restore lost blood.

Technically buffs Entropic Plume by fixing some bugs

    "Cloudstruck" has always meant to blind, but they used the wrong method, so I fixed that.
    Also it was meant to inject multiple units of poison, but used "min" instead of "max" so it always did the lowest.
    I also fixed the stink cloud lasting forever on people.
    Amok also makes people holding guns to shoot people further away.

Closes

    Admin healing removes heretic living heart #69167 while I'm here

Why It's Good For The Game

    Heretic curses have pretty much always been bad, getting fingerprints is damn near impossible considering everyone uses gloves. Not only that but their requirements were very high. This should hopefully bring curses to the limelight, as they can be applied to any potential targets. It also rewards heretics who go out of their way to collect fingerprints and blood samples with even stronger curses.

    The Living Heart was often hard to pinpoint people exactly, partially cause of an oversight. I improved the text to be clearer about potential locations of your targets.

    Leeching Walk's healing was nice, but blood wounds were still a major threat. Some blood restoration should help.

    Entropic Plume I think has never worked correctly, so that was a bummer. Fixes that.

Changelog

cl Melbert
balance: Heretic: Curses have been reworked. You can now curse any member of the crew, granted they're not too far away. If you additionally provide an item in the ritual containing a sample of the target's blood or fingerprints, the curse's duration will be increased and have its range uncapped.
balance: Heretic: The Curse of Corrosion has been nerfed slightly due to this rework, and can no longer cause vital organs to fail.
balance: Heretic: The Living Heart should now provide better directions, and had its cooldown halved to 4 seconds.
balance: Heretic: Leeching Walk (rust healing) now restores lost blood.
balance: Heretic: If you apply Amok (Entropic Plume) to someone holding a gun, they'll try to shoot it at people nearby.
fix: Entropic Plume's effect now blinds, as it should.
fix: Entropic Plume no longer sometimes applies the stink effect forever.
fix: Entropic Plume no longer always applies the lowest amount of poison, and properly scales on distance.
fix: Fixed an exploit which allowed people to figure out if a Heretic's heart was a previously a Living Heart after being removed.
fix: If a heretic is fully healed by something (such as ahealed), they'll not lose their living heart
/cl

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[a2e0ab3ff0...](https://github.com/tgstation/tgstation/commit/a2e0ab3ff0540a6e527e2f1d39c71525303ed75b)
#### Thursday 2022-09-01 21:56:59 by IndieanaJones

Spider Rebalance PR: Burn Baby Burn Edition (#68971)



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

---
## [Arturlang/tgstation](https://github.com/Arturlang/tgstation)@[20e4add487...](https://github.com/Arturlang/tgstation/commit/20e4add48712b59e9bcadd187beee54c02f98e38)
#### Thursday 2022-09-01 22:03:01 by Tim

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
## [Offroaders123/NBT-Parser](https://github.com/Offroaders123/NBT-Parser)@[b68ef6a749...](https://github.com/Offroaders123/NBT-Parser/commit/b68ef6a7498bf96f56636a1fc2a64bd101a85993)
#### Thursday 2022-09-01 22:03:59 by Offroaders123

JavaScript, Refactor?

I know, I'm going back and forth. This has been a huge learning journey, and that's my main goal.

I went back to JS, from the TypeScript rewrite. Now everything is 98% the same as before, the only different being that the TypeScript features are now defined using JSDoc, right inside of the vanilla JS! I really want to avoid a transpile step, unless it were completely necessary (not in this case, for me at least). All I essentially want from my use with TypeScript is variable type checking in my editor, and things like that. I also really like the automatic documentation that it adds to your library. It just pops up for the user with what options are available for them to use.

I guess, ideally, it would be wonderful to be able to write everything out in TypeScript, then transpile it to plain vanilla ESNext JavaScript, with JSDoc as the documentation side of things. I don't want to have to maintain a different version of the source which isn't directly what it used on the user's end though, which is my main eeerrrg with TypeScript. Comparing writing TypeScript vs JavaScript with JSDoc, it without a shadow of a doubt is better. But, if you count in the tooling that you have to manage after the fact, I don't like that you have to both manage a separate source code, and a separate user code (the transpiled version).

This test (how many am I going to do? I'm still not sure XD) tries to find an even more middle ground, which benefits from the static-typing nature of TypeScript in your editor, but without having to transpile anything before you can run it.

There are still a few issues that I didn't quite figure out yet, with the JSDoc setup. The main one is being able to define an index signature on a class, as I want to define a few optional properties on the `CompoundTag`. I think this may be solveable with a more-specific set of type defintions for those properties though, rather than just with string indexing.

The other issue I didn't figure out yet is also likely solveable with a better implementation on my part, and that's accessing the class which creates the object for an NBT tag. A better way to put it, right now I am trying to get a reference to `ByteTag` from a `new ByteTag()` instance, using `new ByteTag().constructor`. However, I haven't found a way to type-cast that to specifically target `ByteTag`, as that's ideally what would work best. From the time of writing that last sentence, I think I though of a possible solution, haha. It would also probably work to add a factory function like `isTag()`, but to get the constructor class of a tag instance, something like `getTagConstructor()`, maybe. Another option I read that someone recommended was essentially `Object.getPrototypeOf(new ByteTag()).constructor`, but I'm not sure if I like the verbosity of adding an extra call like that, only for a type declaration fix. But, it is a fix, so it's definitely an option.

Even with all of this work, sometimes it still feels like a complete mess. I think that means (it could be multiple/any of these) that I've worked on it too long today, it not actually a mess and I'm just confused, or it is a mess, haha. I think it could be helpful to take a break and work on something else though, that usually does miracles for when I come back later to it (Even this crazy update/change/test thing was one of those too).

Maybe I'll work some more on trying this statically-typed TS setup for vanilla JS with Num Text Component, I think I had something like that going before I moved this project to TypeScript. I'd also have to say that the in-editor linting has been massively cool, I definitely am a fan of that now, now that I've peeked behind the curtain of TypeScript, lol.

Cheers to experimenting!

Some migration docs help:
https://stackoverflow.com/questions/38877252/typescript-getting-a-class-constructor-of-the-object-at-runtime
https://stackoverflow.com/questions/70101584/how-to-cast-typescript-type-in-javascript-using-jsdoc
https://stackoverflow.com/questions/49836644/how-to-import-a-typedef-from-one-file-to-another-in-jsdoc-using-node-js
https://stackoverflow.com/questions/16017627/document-generic-type-parameters-in-jsdoc
https://stackoverflow.com/questions/51467835/how-to-use-jsdoc-to-document-an-es6-class-property
https://stackoverflow.com/questions/71274013/using-jsdoc-to-set-an-index-signature-on-an-es6-class

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[aab43918f8...](https://github.com/tgstation/tgstation/commit/aab43918f8dca1a09f67effc786eb46bda592d22)
#### Thursday 2022-09-01 22:10:01 by LemonInTheDark

Resolves is_banned_from headaches and lag (Speeds up roundstart significantly) (#69376)


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

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[e75283dee3...](https://github.com/tgstation/tgstation/commit/e75283dee3776577f70d792e0874dcaecb6c93e3)
#### Thursday 2022-09-01 22:13:27 by vincentiusvin

Refactors SM gas behavior to be datum based instead of list based + powerloss co2 buff (#69158)


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

---
## [ekkusa/android_kernel_sony_sdm845](https://github.com/ekkusa/android_kernel_sony_sdm845)@[513143589c...](https://github.com/ekkusa/android_kernel_sony_sdm845/commit/513143589c2e0235353bc1d1a77d4c6610c2d8a3)
#### Thursday 2022-09-01 22:17:42 by Dave Chiluk

[BACKPORT] sched/fair: Fix low cpu usage with high throttling by removing expiration of cpu-local slices

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
Signed-off-by: Raphiel Rollerscaperers <rapherion@raphielgang.org>

---
## [plinkiac/Best-of-the-Worst](https://github.com/plinkiac/Best-of-the-Worst)@[bd1415479c...](https://github.com/plinkiac/Best-of-the-Worst/commit/bd1415479c05ff47ef93762d5c00b8fc230959a3)
#### Thursday 2022-09-01 22:50:26 by Harry S. Plinkett

Update 2022-07-27 - Mouth in Motion, Info-Select, [BLANK], Power Pack - Take a Stand, The Magic of Scarf Tying, Target Panic - It's Causes and Cures, Fundamentals of Rowing, Street Smarts, The Brothers - Fact and Reality, Oh You Beautiful Doll - Doll Collecting for Fun & Profit, Body for Life, It's a Steal, Lights Camera Bubbles, Power Aging, Word Perfect 5.0.txt

---
## [AgencyCoda/mezzio-skeleton](https://github.com/AgencyCoda/mezzio-skeleton)@[5a045be03f...](https://github.com/AgencyCoda/mezzio-skeleton/commit/5a045be03fe5f8a141872921d0a62c1b907ec01e)
#### Thursday 2022-09-01 22:53:09 by Michał Bundyra

Message against the war, in Russian and English

🇷🇺 Русским гражданам

Мы, участники Laminas, родились и живем в разных странах. У многих из нас есть друзья, родственники и коллеги как в России, так и в Украине. Некоторые из нас родились в России. Некоторые из нас живут в России. У некоторых бабушки и дедушки сражались с фашистами во Второй мировой войне. Здесь никто не поддерживает фашизм.

У одного из нас есть украинская родственница, которая спаслась из дома вместе с сыном. Поезд задержался из-за бомбежки на дороге впереди. У нас есть друзья, которые прячутся в бомбоубежищах. Мы с тревогой ждем весточки от них после воздушных налетов, которые беспорядочно наносят удары и попадают по больницам, школам, детским садам и домам. Мы не берем это из каких-либо СМИ. Мы наблюдаем это напрямую.

Вы доверяете нам достаточно, чтоб использовать наши программы, и мы просим вас довериться нам вновь. Мы нуждаемся в помощи. Выходите и протестуйте против этой бесполезной войны. Остановите кровопролитие. Скажите "Нет войне!"

🇺🇸 To Citizens of Russia

We at Laminas come from all over the world. Many of us have friends, family and colleagues in both Russia and Ukraine. Some of us were born in Russia. Some of us currently live in Russia. Some have grandparents who fought Nazis in World War II. Nobody here supports fascism.

One team member has a Ukrainian relative who fled her home with her son. The train was delayed due to bombing on the road ahead. We have friends who are hiding in bomb shelters. We anxiously follow up on them after the air raids, which indiscriminately fire at hospitals, schools, kindergartens and houses. Were not taking this from any media. These are our actual experiences.

You trust us enough to use our software. We ask that you trust us to say the truth on this. We need your help. Go out and protest this unnecessary war. Stop the bloodshed. Say "stop the war!"

Signed-off-by: Michał Bundyra <contact@webimpress.com>

---

