## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-09-10](docs/good-messages/2022/2022-09-10.md)


1,753,592 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,753,592 were push events containing 2,351,379 commit messages that amount to 133,707,428 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 29 messages:


## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[d065a7133f...](https://github.com/pytorch/pytorch/commit/d065a7133f52b0127394b14a298d4180cbca5ddf)
#### Saturday 2022-09-10 00:05:41 by Andrew Gu

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

Differential Revision: [D39293429](https://our.internmc.facebook.com/intern/diff/D39293429)

[ghstack-poisoned]

---
## [sjp38/linux](https://github.com/sjp38/linux)@[2f2c9aaf9f...](https://github.com/sjp38/linux/commit/2f2c9aaf9ff5fa978d572b7e849c8ae50a8c7e19)
#### Saturday 2022-09-10 00:18:52 by Johannes Weiner

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
## [ToppleTheNun/WoWAnalyzer](https://github.com/ToppleTheNun/WoWAnalyzer)@[8b85d56482...](https://github.com/ToppleTheNun/WoWAnalyzer/commit/8b85d5648234dfc2beaa9e22ce566eac8ed96ce4)
#### Saturday 2022-09-10 00:19:25 by Richard Harrah

second pass on demon hunter

clean out changelog entries referencing
abilities that are removed in DF

add sigils to HDH abilities list

clean out entries in SPELLS/demonhunter that are
present in TALENTS/demonhunter

add support for Charred Warblades

add getTalentRank function for Combatant

correct locations of multiple analyzers in the
statistics tab

add support for Misery in Defeat class talent

add support for Retaliation talent

add Buffs module for Vengeance to make frailty
support easier, given that it can now be applied by
three different abilities.

add support for Painbringer talent

add Blur and Darkness to Vengeance

---
## [Rosso-Mugello/free-programming-books](https://github.com/Rosso-Mugello/free-programming-books)@[97016edd67...](https://github.com/Rosso-Mugello/free-programming-books/commit/97016edd6791285128758dd91904b343d1f3b0fd)
#### Saturday 2022-09-10 01:25:22 by David Ordás

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
## [Sonic121x/Skyrat-tg](https://github.com/Sonic121x/Skyrat-tg)@[f0ceecff46...](https://github.com/Sonic121x/Skyrat-tg/commit/f0ceecff46f9b600dfe8e60199f354f61d63a0a4)
#### Saturday 2022-09-10 02:03:41 by SkyratBot

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
## [Jupiterson/Throne-of-Lorraine](https://github.com/Jupiterson/Throne-of-Lorraine)@[a7b24ffea1...](https://github.com/Jupiterson/Throne-of-Lorraine/commit/a7b24ffea10c16d695b2899b3dd529bed91570fa)
#### Saturday 2022-09-10 02:13:14 by WelshSlateMiner

Merge pull request #112 from WelshSlateMiner/AIDs

GO FUCK YOURSELF LOCALISZTION ASS CHEEK

---
## [spaderthomas/tdbuild](https://github.com/spaderthomas/tdbuild)@[6eb2f2f952...](https://github.com/spaderthomas/tdbuild/commit/6eb2f2f9526c7fa9d423d032fec3be952dd45bbe)
#### Saturday 2022-09-10 03:14:08 by spaderthomas

i hate this stupid fucking ecosystem. what an unredeemable piece of shit.

---
## [QueenOfSquiggles/godot-mono-better-inspector](https://github.com/QueenOfSquiggles/godot-mono-better-inspector)@[47f9992666...](https://github.com/QueenOfSquiggles/godot-mono-better-inspector/commit/47f99926663f170e533145ae52d9b56effb7193f)
#### Saturday 2022-09-10 04:00:29 by QueenOfSquiggles

Got some basic BBCode support in a really janky way!

So basically the default tooltip node for the editor inspector is a kind of stripped down RichTextLabel. I need to do some research to figure out exactly what's happening, but just by external probing, I was able to insert terminating tags for the bold and underline that is forced for the tooltip, then I can just append any standard BBCode tooltip entries I like.
Somewhere in the internals, the terminating bold and underline are appended to the tooltip, which leaves a weird tag at the end, but I just put a few new lines before it to make it very separate from the rest of the text.
Realistically, it works. It's hella jank, but it works and I can have FORMATTED TOOLTIPS FOR CUSTOM EXPORT VARS.
Like holy hell that is being added in Godot 4 and I just fucking made it in a day

---
## [pizie11/orbstation](https://github.com/pizie11/orbstation)@[3b2cf65d59...](https://github.com/pizie11/orbstation/commit/3b2cf65d59aa5ae22876b0ebabecb564ccb912d0)
#### Saturday 2022-09-10 04:03:02 by san7890

Rocking The Boat, er, Map Vote (#69561)

* Rocking The Boat, er, Map Vote

Hey there,

A while ago, I spooke (typo intentional) to some other people. One frustration I heard was the fact that people would sometimes sneak through map votes during the very start of a shift, during a high-paced portion, or just as a meme. People in OOC would then flood the vote, putting in any given station. However, if a vote happens 10 minutes in- and the round goes for 70 minutes and not many of the original players are around, then it's not particularly fair to those who have to play next shift on a map they bemoan.

So, we can rock the vote! If a player isn't particularly chuffed with the hand they are given, they can poll the players to see if they want to change the map as well. If rocking the vote goes through, huzzah, you get the ability to vote for the map again. If it doesn't go through: tough luck. You can rock the vote one time per shift by default, and server operators can change the amount of times you can call to rock the map vote at their discretion. Calling to rock the vote either successfully or non-successfully counts as a "call", and when that limit is exceeded: no more calls.

Does this mean that we will only rotate between two maps because pissants will keep rocking the vote until they get what they like? Maybe? I still see people bemoan getting Tram or shit the bed over IceBox, but I think enough people get sick of bread-on-butter to take the server where it need to go. If operators don't really like seeing only two maps play, they can always adjust the config to ensure it doesn't happen.

* makes the grammar grammar

it would be "Rock the Vote vote" otherwise

---
## [Knuxfan24/Sonic-06-Randomiser-Suite](https://github.com/Knuxfan24/Sonic-06-Randomiser-Suite)@[93cde08c08...](https://github.com/Knuxfan24/Sonic-06-Randomiser-Suite/commit/93cde08c0882d16df3df868bf49e8f72f2ae4f65)
#### Saturday 2022-09-10 05:34:32 by Knux

Knux you fucking idiot

Yeah well done genius don't actually check for the value FUCK

---
## [Fedoraware/Fedoraware](https://github.com/Fedoraware/Fedoraware)@[50a54973e7...](https://github.com/Fedoraware/Fedoraware/commit/50a54973e76ff2315320cab53235f3a91da053c8)
#### Saturday 2022-09-10 06:29:27 by Baan

Merge pull request #693 from Radeon0078/patch-1

fuck you this is better kys 130 fov sucks balls

---
## [JoeBidenWhatAreYouHiding/kx](https://github.com/JoeBidenWhatAreYouHiding/kx)@[40edce3053...](https://github.com/JoeBidenWhatAreYouHiding/kx/commit/40edce3053b209fb34592f360c3a249080d5bf20)
#### Saturday 2022-09-10 06:53:10 by generalguneric

new provinces for Madagascar; properly aligned its provinces with rivers. fuck your save games!

---
## [ChoGGi/SurvivingMars_CheatMods](https://github.com/ChoGGi/SurvivingMars_CheatMods)@[ddd37f3e99...](https://github.com/ChoGGi/SurvivingMars_CheatMods/commit/ddd37f3e99843ffcf497f5e496ec0ce7e203881c)
#### Saturday 2022-09-10 08:16:18 by ChoGGi

Mods:

Base Walls 0.7:
Log spam (thanks Spyro_Dragonite).

Build Mystery Rewards 0.8:
Fix for launching/salvaging crystals.
Cleans up borked salvage crystals.

Disable Annoying Sounds 0.7:
Added Support Struts.

Fix Bugs 2.8:
Removed Fix Landscaping Freeze.
Added mod option for No Planetary Anomaly Breakthroughs when B&B is installed.
Added a "fix" for the Uneven Terrain bug we've come to know and love (see mod option tooltip).
v2.7
Cleaned up some code.

Fix Mirror Graphics 0.8:
Asteroids/Underground should all be sandy/rocky (probably).

Game Rule Apocalypse Run 0.3:
Made into game rule, and changed title.

Show All Textures 0.4:
Removes rocks/vegetation.

Stop Auto-Rovers During Storms 0.8:
Added Immediate Abort: As soon as storm starts rovers will flee/idle (default off).
Code cleanup.

Unit Thoughts 0.7:
Log spam (thanks Spyro_Dragonite).

github@choggi.org

---
## [DidgetMidget/ScriptsAA](https://github.com/DidgetMidget/ScriptsAA)@[569810d86d...](https://github.com/DidgetMidget/ScriptsAA/commit/569810d86d0f0027e2c4b6fc5b39b608285f0e79)
#### Saturday 2022-09-10 09:20:08 by ZeroPixel

Hey ApronAG,

i found your script and it is really nice i have to say. 

I was just a bit annoyed that it wasnt 100% reliable because sometimes the teleporter wouldnt teleport with the error 
"error 769 teleport failed" 

And i just threw an ez fix on that (i am not a lua developer by any means i work in IT and also studying computer science yeah but just mosty C# and Java things) -This isnt my main Github account either if you are wondering

-I am sorry about the indententation changes but the indententation wasnt quite right

---
## [vlggms/lobotomy-corp13](https://github.com/vlggms/lobotomy-corp13)@[f0e6476eb0...](https://github.com/vlggms/lobotomy-corp13/commit/f0e6476eb051d781f7e4d0be7976dff0ff72fda0)
#### Saturday 2022-09-10 10:19:01 by Lance

The Great Workening

Attribute Levels Displayed

No thoughts were had, thoughts injected.

Attribute Levels go brrr

Requested Change Made

WHOOPS WRONG PARENTHESIS

I swear I know how Clamps work

Holy shit how did this not get found out earlier

---
## [zenosa/android_kernel_xiaomi_msm8956](https://github.com/zenosa/android_kernel_xiaomi_msm8956)@[995e42ed19...](https://github.com/zenosa/android_kernel_xiaomi_msm8956/commit/995e42ed1940cd130d4499205a1ab850c1453197)
#### Saturday 2022-09-10 10:21:01 by Masahiro Yamada

modpost: file2alias: go back to simple devtable lookup

commit ec91e78d378cc5d4b43805a1227d8e04e5dfa17d upstream.

Commit e49ce14150c6 ("modpost: use linker section to generate table.")
was not so cool as we had expected first; it ended up with ugly section
hacks when commit dd2a3acaecd7 ("mod/file2alias: make modpost compile
on darwin again") came in.

Given a certain degree of unknowledge about the link stage of host
programs, I really want to see simple, stupid table lookup so that
this works in the same way regardless of the underlying executable
format.

Signed-off-by: Masahiro Yamada <yamada.masahiro@socionext.com>
Acked-by: Mathieu Malaterre <malat@debian.org>
[nc: Omit rpmsg, sdw, tbsvc, and typec as they don't exist here]
Signed-off-by: Nathan Chancellor <natechancellor@gmail.com>
Signed-off-by: Sasha Levin <sashal@kernel.org>

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[a5581313b2...](https://github.com/mrakgr/The-Spiral-Language/commit/a5581313b2dc0045355dde7473271e1367a52324)
#### Saturday 2022-09-10 10:48:34 by Marko Grdinić

"9:40am. Yesterday it was getting colder, but it is freezing right now in my room. I've had to bring in a heater.

Anyway, I've been lounging in bed for a bit too long today. Today I'll take it easy. First of all, let me chill, then I will do some test posts on Patreon.

It seems I've reached level 3 on Royal Road.

...Only a single view on what I've posted yesterday. It really doesn't bode well at all for my writing career. Maybe it is hopeless, but I'll execute the plan and see where it leads me.

9:45am. Hmmm, this is a problem. When I log into Patreon it puts me on the page I opened. Was that Patreon page supposed to be a central page for all my work? Can't I have multiple Patreon pages?

https://www.reddit.com/r/patreon/comments/4x6nft/patreon_and_multiple_pages_with_one_account/

9:55am. What a pain in the ass. Nevermind that for now, let me just chill a little. Then I will post all the chapter 8 pieces on Patreon.

10:35am. Let me start. I had time to think about what I want to do. First of all, let me post chapter 8 on the Patreon page.

I'll create two accounts, with 5/month subscriptions. I've imagined linking the accounts, but nevermind that for now.

https://www.patreon.com/simulacrum_heavens_key

Here is the Patreon page, I've changed its name. I'll have to update the two links later. For now, let me just figure out how to post things on Patreon.

10:40am. Sigh, Patreon is butchering my formatting!

10:45am. https://www.reddit.com/r/patreon/comments/vdt3pk/copying_from_any_text_editor_into_patreon_and/

This is so annoying.

10:55am. Sigh. So far the only way to post text properly on Patreon is to first post it into RR and the copy paste it to Patreon.

https://www.royalroad.com/forums/thread/122239

Kek, he is doing better than me.

///

Yes. Views aren't indicative of anything.

Views basically mean how many people clicked when your chapter appeared on the latest updates.

It's entirely random numbers that vary even if you have updates scheduled to post automatically, since you can't predict how many people are looking at the page at given time. While the first chapter has most views since it is the first thing everyone sees, rest is pretty much random, depending on unpredictable variables and circumstances saying nothing about the popularity of your story. You can actually guess which cover attracts most views, assuming you change covers regularly, but even then it is a stretch.

What is indicative is how many followers you gain every update. Followers are people who showed interest in your story, even if temporarily.

///

Hmmm, interesting.

11:15am. https://www.royalroad.com/forums/thread/122332

///

I've written a fair bit of my own story, and am trying to post it on Patreon.

When I copy paste it there, it looks a bit like on RR without clean paste enabled. The way I do on RR is that I right click and copy it as plain text. On RR it just works, but on Patreon I get ugly gaps between paragraphs. It works a bit better when I copy it to RR and then from there to Patreon as RR eliminates superfluous gaps, but I sometimes lose formatting on indented text.

This is really annoying. How do you pros do it?

Shouldn't there be a clean way of doing this? Is there a better site similar to Patreon which allow me to properly paste text?

///

I've opened this thread. You'd think that just posting some text would be easy, but it is anything but that.

11:30am. https://www.disciplemedia.com/community-monetizations/patreon-alternatives/

https://ko-fi.com/

How could the platform even work if it has no fees?

...Ah, whatever. Let me start a page.

> Connect to PayPal

Ugh.

11:35am. https://youtu.be/34ltAowKUvU
What to Know Before Starting Patreon

This is so annoying. I just want to paste text, and it is going to waste my whole day at this rate.

The way things are going, even my journal is going to end up having to be uploaded as a pdf.

https://www.patreon.com/posts/new-feature-29012102

It has markdown?

11:45am. This is going to be annoying.

https://www.patreon.com/posts/using-markdown-29519541

This probably has what I want, but of course, it is paywalled.

https://youtu.be/NHmB7O87ViY
How to post content on Patreon

11:45am. I give up.

https://support.google.com/docs/answer/1663349?hl=en&co=GENIE.Platform%3DDesktop

Let me instead target the Docs themselves.

12pm. I didn't expect that such a serious platform such as Patreon would have such poor text support.

I understand what is wrong.

In Docs, I can set the paragraph spacing to 2x, and it will look the same as in Patreon.

https://bestfriendsclub.ca/ko-fi-vs-patreon/

I am reading this, and it makes it look like there is zero reason for me to pick Patreon over Ko-fi. Patreon just charges higher fees, but offers nothing when it comes to getting more readers.

12:10pm. https://pinepage.com/

I've seen this advertized on Quora.

https://pinepage.com/

I am wondering if I could somehow monetize the gamesoftranscendi blog. Why do the tiers have limits on the number of paying members here.

https://re-library.com/translations/blade-maiden/

This site makes use of Patreon, but it does not host everything there.

https://www.patreon.com/ProjectGB

I wasn't really ready to make my own site.

12:20pm. No. While having the files be on Google Drive is an option, having to manually manage permissions would be a pain in the ass.

Do membership tiers have to be tiered. It would not be bad if I could have separate accessibility...

Yeah, I can actually check the box and select only the Aleator and not the Episteme. That way I could require the members to subscribe to just Heaven's Key or just my blog.

https://www.royalroad.com/forums/thread/122332

Got a reply. He is suggesting that I use PDFs.

Ok, why not. Looking at the amount of achievements these guy has I guess using pdfs hasn't hurt him.

12:35pm. Ok, let me go with that.

12:40pm. Let me get breakfast. I think I understand what I need to do. I'll create two tiers, one for just Simulacrum, one for the Spiral blog priced at 5$/month each.

I'll just use pdfs as that guy suggests. The readers will get used to it at some point. Better for me to do this, than to have to endlessly struggle with formatting.

That is a nice and simple way of doing it.

Having two different accounts would also be hard. Better I keep it all in one place.

...I'll need to make sure to appropriately tag my posts so readers can easily look for them. I'll also make a pinned public post.

12:45pm. Let me have breakfast.

I shouldn't choose Patreon just like that.

https://pinepage.com/

I linked to this before. The mid tier costs 30$ a month which might seem like a lot, but if I had a 100 patrons paying 5$/month each that would cost me 7% a month.

Actually, this site is really cheap if you have a lot of Patrons. 50/month for somebody with 100s of subscribers would be nothing. It is the mid tier that is troublesome.

But why not Ko-fi? Do I have a reason not to pick it over Patreon?

This will take me a while. I should register to Ko-fi and take a look at how it works."

---
## [walternewtz/android_kernel_xiaomi_sdm845](https://github.com/walternewtz/android_kernel_xiaomi_sdm845)@[4faf523cfb...](https://github.com/walternewtz/android_kernel_xiaomi_sdm845/commit/4faf523cfbb2051cce29b3d74c2ccb9c0b121361)
#### Saturday 2022-09-10 12:18:00 by Francis Yan

BACKPORT: tcp: instrument tcp sender limits chronographs

This patch implements the skeleton of the TCP chronograph
instrumentation on sender side limits:

	1) idle (unspec)
	2) busy sending data other than 3-4 below
	3) rwnd-limited
	4) sndbuf-limited

The limits are enumerated 'tcp_chrono'. Since a connection in
theory can idle forever, we do not track the actual length of this
uninteresting idle period. For the rest we track how long the sender
spends in each limit. At any point during the life time of a
connection, the sender must be in one of the four states.

If there are multiple conditions worthy of tracking in a chronograph
then the highest priority enum takes precedence over
the other conditions. So that if something "more interesting"
starts happening, stop the previous chrono and start a new one.

The time unit is jiffy(u32) in order to save space in tcp_sock.
This implies application must sample the stats no longer than every
49 days of 1ms jiffy.

saalim :- Drop rate_app_limited from tcp header (already present)
original :- https://github.com/danascape/kernel-msm-4.14/commit/05b055e89121394058c75dc354e9a46e1e765579#diff-4ddfd98f3453244962e17ac121bea6162887af47d0531ba6e2cf49a941edf2c9

Signed-off-by: Francis Yan <francisyyan@gmail.com>
Signed-off-by: Yuchung Cheng <ycheng@google.com>
Signed-off-by: Soheil Hassas Yeganeh <soheil@google.com>
Acked-by: Neal Cardwell <ncardwell@google.com>
Signed-off-by: David S. Miller <davem@davemloft.net>
Signed-off-by: danascape <saalimquadri1@gmail.com>
Signed-off-by: PainKiller3 <ninadpatil100@gmail.com>

---
## [ProjectIgnis/CardScripts](https://github.com/ProjectIgnis/CardScripts)@[cc8f36cb12...](https://github.com/ProjectIgnis/CardScripts/commit/cc8f36cb12c9f1ca1b064c5294a1e09651992bca)
#### Saturday 2022-09-10 14:34:03 by pyrQ

Various script fixes/updates

Official:
- Armed Dragon Blitz: General script polish.
- Blackwing - Chinook the Snowstrike: The Quick version of its effect should be usable in the Damage Step.
- Blackwing - Twin Shadow: Added a hint timing for the opponent's End Phase.
- Chorus in the Sky: Small typo in the code regarding target redirection effects.
- Cipher Spectrum: Shouldn't activate if the Xyz Monster was sent to the GY by an effect but wasn't destroyed.
- Earth Golem @Ignister: Small typo in the code regarding target redirection effects.
- Ebon High Magician: Match the strings used in its script with the ones in its database entry.
- Evil★Twin Ki-sikil: Should check that you control an appropriate monster only when the effect would be activated.
- Evil★Twin Lil-la: Should check that you control an appropriate monster only when the effect would be activated.
- Fire Formation - Yoko: Shouldn't be considered an effect that destroys if the player doesn't target anything when activating it + general script polish.
- Flower Bloom of the Vernusylph: The last effect now uses the correct string.
- Gishki Chain: Adding a card to the hand and re-arranging the order of the rest shouldn't happen at the same time.
- Jurrac Meteor: If the effect doesn't successfully destroy anything then the player shouldn't be able to Special Summon a Tuner.
- Legendary Six Samurai - Enishi: Should also check the condition on resolution + general script polish.
- Live☆Twin Lil-la: Should check that you control no other monsters only when the effect would be activated.
- Live☆Twin Ki-sikil: Should check that you control no other monsters only when the effect would be activated.
- Lovely Labrynth of the Silver Castle: Should only protect Normal Trap Card activations, not Normal Traps' effects' activations.
- Shock Troops of the Ice Barrier: Shouldn't destroy the target if it's not a WATER monster anymore when this card's effect resolves.
- Star-Crossed Meeting: Should be able to negate its GY effect with something like "Solemn Warning".
- Virtual World Hime - Nyannyan: The Special Summoning restriction should be applied even if it's not Special Summoned successfully + general script polish.
- Wrath of Neos: Shuffling and destroying should be simultaneous + general script polish.

Unofficial/Rush:
- Monster Reborn (Rush): Should use the value indicating that it's a summon with "Monster Reborn".
- Speed Spell - Monster Reborn: Should use the value indicating that it's a summon with "Monster Reborn".

---
## [pauliesnug/OneConfig](https://github.com/pauliesnug/OneConfig)@[f6cf5bde15...](https://github.com/pauliesnug/OneConfig/commit/f6cf5bde158f635e3fb2000de64f050e13426a86)
#### Saturday 2022-09-10 15:24:33 by Wyvest

Joan was quizzical
Studied pataphysical science in the home
Late nights all alone with a test tube
Oh, oh, oh, oh
Maxwell Edison, majoring in medicine
Calls her on the phone
"Can I take you out to the pictures, Joa-o-o-oan?"
But as she's getting ready to go
A knock comes on the door
Bang! Bang! Maxwell's silver hammer
Came down upon her head
Clang! Clang! Maxwell's silver hammer
Made sure that she was dead
Back in school again, Maxwell plays the fool again
Teacher gets annoyed
Wishing to avoid an unpleasant scene
She tells Max to stay when the class has gone away
So he waits behind
Writing fifty times "I must not be so"
But when she turns her back on the boy
He creeps up from behind
Bang! Bang! Maxwell's silver hammer
Came down upon her head
Clang! Clang! Maxwell's silver hammer
Made sure that she was dead
P. C. Thirty-One
Said "We caught a dirty one"
Maxwell stands alone
Painting testimonial pictures
Oh, oh, oh, oh
Rose and Valerie, screaming from the gallery
Say he must go free (Maxwell must go free)
The judge does not agree, and he tells them so
But as the words are leaving his lips
A noise comes from behind
Bang! Bang! Maxwell's silver hammer
Came down upon his head
Clang! Clang! Maxwell's silver hammer
Made sure that he was dead
Wo-wo-wo-woh
Silver hammer man

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[eca2181328...](https://github.com/mrakgr/The-Spiral-Language/commit/eca21813284bde92f6e0c117904518c1b01349ee)
#### Saturday 2022-09-10 16:39:46 by Marko Grdinić

"https://www.patreon.com/simulacrum_post_singularity_story

I am back to this.

1:40pm. I am almost done with breakfast. Let me chill just a bit more and I will resume.

I've decided what I want to do if I go with Patreon, but I should open a Ko-fi page.

The reason Paypal makes me groan is because I vaguely remember having some trouble with it almost a decade ago, and haven't used it since. I'll just do the same thing as with AWS and use my work email, and sign up again. Now that I have my bank accounts in order, there is nothing stopping me from doing this. Literally everything uses Paypal, so I should just go over this dumb hurdle.

2:15pm. Almost done with the last chapter of Witch and the Beast.

2:30pm. Let me start.

Signing up to Paypal. Isn't it great that I actually have a mobile this time?

2:50pm. > Adult or sexually explicit content including but not limited to:
> Literature, imagery (including illustrative), videos, links to external sites or content containing such material; and

Ko-fi tries to be a clean site.

///

In a Nutshell
Do not use Ko-fi.com for Illegal or Adult content.
Only use Ko-fi.com in legal, genuine and positive ways.

///

This might be troublesome in the future, as I'd want to do some NSFW parts in the next arcs. Unlike last time, I'll separate them out from the main story.

I'll have to check whether Patreon allow R18 material.

> Something went wrong

I click on Agree and Connect and I get the above error.

...Yeah, this is the Paypal that I know and love. Something went wrong? What exactly?

3pm. I tried it again and it passed. Maybe I was lingering for too long reading the terms.

https://www.patreon.com/policy/legal

Let me also read Patreon's terms of use. I do not want to get started with it only to get banned down the road.

3:05pm. https://techcrunch.com/2021/09/22/patreon-to-roll-out-tools-to-help-its-adult-creators-meet-mastercards-new-standards/#:~:text=Currently%2C%20Patreon%20allows%20certain%20kinds,blatantly%20bans%20pornographic%20material%20and%20%E2%80%9C

I am starting to hear thunder outside. Don't tell me weather is going to wreck my day again. This kind of weather is the classic end of summer. In September you get these contant rains.

3:10pm. Had to do a chores. I am back again. I am going to have to ask about adult content on sites like Patreon.

But before that, let me just see if Kofi's text posting is better than Patreons. Terms of service are one thing, but it depends how permissive the sites are. In practice they can always find a reason to ban you for anything if they want to.

Kofi is the same shit as Patreon. They have almost the same interface too.

The difference is that Kofi does not have tiers like Patreon.

https://help.ko-fi.com/hc/en-us/articles/360007937553-Illegal-Adult-and-NSFW-Content

With these terms, they can basically find a reason to ban you for anything.

https://ko-fi.com/ghostlike4331

Forget Kofi. It is no good.

https://writingcooperative.com/what-the-heck-are-so-many-writers-crying-about-9c447f95e47c

Substack?

https://www.patreon.com/written_fantasy

Ok, it seems this guy is definitely writing porn. I guess Patreon will have to do.

https://www.disciplemedia.com/community-monetizations/patreon-alternatives/

https://gumroad.com/

Hmmm, Gumroad? Oh, it has fiction books section.

https://gumroad.gumroad.com/p/clarifying-what-is-and-isn-t-allowed-on-gumroad

> Another type of content people often complain about is sexual content. To be clear: sexual content is allowed on Gumroad (including illustrations, comics and erotic prose), though NSFW products should be tagged as such.

> Explicit pornography is not allowed on Gumroad, due to policies from our banking partners. You can read about that on our page about adult content.

3:35pm. Ok, Patreon it is with Gumroad as the second option.

Payment processors really have the content providers by the balls don't they? I suddenly realize what cryptocurrencies could be useful for.

Really, the best thing when it comes to estimating what is allowed and isn't on a particular site is to look at what is already there. Words are just words.

https://blog.appsumo.com/patreon-alternatives/
https://www.merchantmaverick.com/patreon-alternatives/

> Here’s a crowdfunding solution that ensures you won’t have to pay a platform fee to anybody: You can just directly solicit donations from those who enjoy your work.

It seems I can just put a Paypal button on my own website and avoid the platform fees that way.

3:45pm. Ok, enough. I'll go with Patreon. I'll use pdfs as has been suggested. The users will simply have to get used to it.

Now let me download the entire chapter 8 as pdf.

Hmmm, no TOC.

I guess from here on out, I'll have to add the TOCs manually. Ok.

Very well.

3:55pm. I'll go this path and only change things when I have a reason to. If I by some chance I get a lot of Patrons in the future, I'll look into setting up my own things. For now the big challenge is to keep it flowing.

Right now it is not worth wasting my time, when I am making 0$.

Now, let me post the entirety of ch 8 on Patreon.

Actually first, let me edit the tiers.

I must make sure to tag the posts appropriately.

///

While I was working on the Spiral language I became accustomed to writing a journal in my commit entries.

https://github.com/mrakgr/The-Spiral-Language

You can see what I mean if you dig through the commits on this repo. Currently I am working on Heaven's Key, and all the drafts for it will be in it. Since it would not be fair to Patrons who are willing to pay for early access to have the drafts out on a programming language repo for free, I will be moving the blog here to Patreon. Here you will be able to see all of my work exactly as it gets written. The other tier will get it as soon as I am done proofreading the chapters. Royal Road readers get it last after some time has passed.

This is a trier for journal posts only, so you won't have it neatly sorted and accessible like in the other tier. This is the raw, bleeding-edge of Simulacrum. For hardcore fans only.

///

https://www.patreon.com/posts/chapter-8-sense-71787031?utm_medium=clipboard_copy&utm_source=copyLink&utm_campaign=postshare_creator

4:40pm. Here it is. I given a tangible benefit to being an Aleator tier member. Mhhhhhh...Now, what I need to do is put the rest of the chapters online.

As well as the author's notes. Chapter 1 in particular has some images. I need to go back and organize all of that properly as some of it is RR exclusive right now. I need to put it first on Google Drive.

4:45pm. Fixed a typo. At any rate, I am quite tired right now and don't really feel like doing anything. I need to take a break.

Today the only thing I've really accomplished is putting a single chapter on Patreon, but it required some thought. I have the workflow down now. I'll put the rest of the chapters up, maybe tomorrow, and then start writing the next chapter. As soon as I have that started I'll move the blog over to Patreon as well.

5:15pm. Done with the break.

Let me do some work. First let me fix chapter one. Thankfully that one is the only which has images.

5:25pm. It turns out adding images to documents is really easy.

5:30pm. Ah, I just notice that RR has a Paypal button on it. Ok...

Once I finish processing the files and posting then on my Patreon I'll look into how to link RR to my Paypal account. That would be a step forward.

5:45pm. Ok, good. I've merged all the pdfs with their author's notes.

Now to post them on Patreon. I'll do it all in a single post.

https://www.patreon.com/posts/chapters-1-7-71789687?utm_medium=clipboard_copy&utm_source=copyLink&utm_campaign=postshare_creator

Here it is.

I might as well make this one public.

5:55pm. Time for lunch. Let me take care of that and I'll check out how to add a paypal link.

6:25pm. Done with lunch Paypal.

Hmmm...where is the setting to put in the Paypal link? I can't find the Patreon link either.

6:30pm. This is so annoying. Where the fuck is it!?

Forget it. I'll figure out where the setting is tomorrow. Right now I want to rest.

https://www.royalroad.com/support/knowledgebase/107

> You need to go to your Donation Settings in the author dashboard

Holy shit, was it well hidden.

https://www.paypal.com/buttons/

I'll figure this out tomorrow. For now, good work me. Tomorrow I'll get this final bit of drudgery out of the way and then start writing chapter 9. I am starting to hit my stride as an author, so it should not be too long before I am done with it. I am hyped about the first scene, but I'll have to think about how rest will go."

---
## [sthagen/psf-black](https://github.com/sthagen/psf-black)@[0019261abc...](https://github.com/sthagen/psf-black/commit/0019261abcf6d9e564ba32d3cc15534b9026f29e)
#### Saturday 2022-09-10 16:50:40 by Richard Si

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
## [I2pRandom/Cataclysm-DF](https://github.com/I2pRandom/Cataclysm-DF)@[3dd5fbed93...](https://github.com/I2pRandom/Cataclysm-DF/commit/3dd5fbed9357a47db81ffcf0b359019b87ab0e4d)
#### Saturday 2022-09-10 18:13:29 by I2pRandom

another update to the buttplug item.

this joke has gone beyond a joke to an actual item addition, cus fuck it.
Added the "ONLY_ONE" flag, Removed the cover tag so that it's 'socketless' with (ty Kheir), and finally redefined the description for one that feels better.
still no idea how to apply the 'fun' artifact effect to the item as a stand-in for a custom morale bonus.

---
## [RahulMJaiswar/Commonwealth-Game-2022](https://github.com/RahulMJaiswar/Commonwealth-Game-2022)@[34353de0f1...](https://github.com/RahulMJaiswar/Commonwealth-Game-2022/commit/34353de0f10b72c980389d17454cc94d1a208c03)
#### Saturday 2022-09-10 18:15:21 by Rahul Jaiswar

Add files via upload

Some special points in the Commonwealth Games 2022 are different from every last few years
1.	 
•	Steeplechase is a sport where Kenya wins every year from 1998-2018 from bronze to Gold Kenya won all Medals
•	But this year we had a miracle, Avinash Sable won the Silver Medals in Steeplechase 
•	He made a new National Record
2.	Sharath kamal
•	Some people want much more than 1 medal. even after winning a gold, medal they say "Yeh Dil Mange More"
•	India table tennis star Sharath Kamal is one of them he won not only 1 but 4 medals for India CWG
•	Let me tell you Sharath Kamal is 40 years old and has won medals before too
•	We think an athlete loses his skills as he ages, reactions are slower and young players get more medals than older players
•	But Sharath Kamal has proved everyone wrong
 
3.	Vinesh Phogat :
•	By winnings a gold medal Vinesh Phogat earned a hat trick of gold
•	She is the first Indian woman to win 3 consecutive golds at CWG
•	And her achievement is quite special because she lost her quarterfinal bout at Tokyo Olympic
•	Ans she admitted she was in poor mental and physical health she thought of quitting wrestling  but she didn’t quit
•	Coming back from that low to win gold is a huge stamp
PV Sindhu
•	   PV Sindhu had an injury to her left ankle even then she got gold medals for the country.
 
4.	Women's T20 Cricket
•	Women's T20 cricket made a debut in the CWG this time and we all Indian love cricket but only men's cricket
•	Women's cricket does not get the same respect but this is now slowly changing
•	After the 2017 Women's World Cup our perspective towards women's cricket changed this was cemented in CWG this year that our girls are no less
•	England and Australia dominate every year team in women's cricket but we defeat England in the Semi-Finals match and we enter the gold medals match.
•	And we came too close to defeating Australia as well we came so close to winning the gold medals 
 
5.	Can a Tailor brings home medals in weightlifting?
•	This is the story of Achinta Sheuli
•	He comes from Deulpur in West Bengal
•	His father drove a van and he passed away in 2013 leaving a little to the family
•	His mother started embroidery to keep the family afloat
•	Even they did not have money for their father's last rites
•	Achinta's elder brother Alok himself was a weightlifter but looking at their financial condition he understood the family could not support 2 athlete so athletes other gave up his weightlifting dream and ask his younger brother to dream big 
 
6.	We won double medals in the triple jump event gold and silver
•	Eldhose Paul won gold medals and create history whereas Abdulla won the silver medals
•	Only our Indian jumpers crossed the 17m mark in the contest
•	Indians don’t generally dominate any athletics event
•	We don’t have Genetics advantages like African and we don't have developed training facilities
•	But yet our athletes win medals even in such adverse situations our respect for them does double
 
7.	Para Athletes
•	Our Para Athlete's also made their mark at the CWG
•	We won our first medals in para powerlifting and that to was  a good
•	Sudhir won the gold in heavyweight powerlifting (212 Kg)
•	We saw our para-athlete might at the paralympic last year and they made a mark at the CWG as well
 
8.	Can India have a 100%-win record in a sport
•	Sound Impossible!
•	But this happened in CWG this time
•	We won most medals in wrestling this time
•	The most amazing thing is that 12 athletes participated in wrestling and all of them won medals .12/12 meaning a 100% success rate
•	Along with some legends like Bajrang Punia of the wrestling world we get to cheer for some never names as well (Naveen Malik)
 
9.	Lawn Balls
•	We never heard a game about Lawn Balls but our women's team defeated South Africa in the  finals
•	There are small balls called either jack or kitty
•	You have to ensure your bowls are close to the jack than the opponents
•	It looks simple but it isn't so it's quite exciting when you think about it that the sport which majority of Indians had not even heard of was one these athlete's made their career in and they won a gold medal as well
 
10.	In 2010 we won 101 medals and we were in 2nd rank
•	In shooting we get the most number of medals as compared to the other country but in the 2022 commonwealth Games, there is no shooting game. Australia is the highest medals taker in 2022 but suppose to think if there is no swimming game in CWG 2022 then supposed what was the Australia conditions or Australia medals tally look like

---
## [Rohail33/RealKing-kernel-SM8250](https://github.com/Rohail33/RealKing-kernel-SM8250)@[b6ca0753dd...](https://github.com/Rohail33/RealKing-kernel-SM8250/commit/b6ca0753ddf36ef6fabe5014e710237d9a74cd21)
#### Saturday 2022-09-10 19:04:47 by George Spelvin

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

---
## [Rohail33/RealKing-kernel-SM8250](https://github.com/Rohail33/RealKing-kernel-SM8250)@[557f7e7285...](https://github.com/Rohail33/RealKing-kernel-SM8250/commit/557f7e728587c10b0cbcd7f6bedadd9805baecf8)
#### Saturday 2022-09-10 19:04:47 by George Spelvin

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
## [MaybeMaru/Maru3D-OTLA](https://github.com/MaybeMaru/Maru3D-OTLA)@[6865765129...](https://github.com/MaybeMaru/Maru3D-OTLA/commit/68657651295cd2d7cdf7cf9bbb07ea6360e40802)
#### Saturday 2022-09-10 20:40:08 by MaybeMaru

0.5 Update

* Obj Sequences Support
* Textured Materials Support
* Improved exported materials structure
* Removed examples cuz fuck you
* Faster code
* Organised some stuff
* Fixed bug of material names showing up incorrectly

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[a4bfe65cb1...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/a4bfe65cb1caece1e3e6a4635fa17d39f1aa3478)
#### Saturday 2022-09-10 21:06:50 by SkyratBot

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
## [chickells/javascript-basic-projects](https://github.com/chickells/javascript-basic-projects)@[c6f353a6a0...](https://github.com/chickells/javascript-basic-projects/commit/c6f353a6a0ae943d997e165fb9cefcd9b20264e6)
#### Saturday 2022-09-10 22:31:09 by Chase

// load initial item
window.addEventListener('DOMContentLoaded', function() {
  const item = reviews[currentItem];

  // YO I FINALLY LEARNED HOW THIS WORKS
  // setting 'item' above lets me target
  // '.img' / '.name' / etc OF that item
  // in the array above.

  // THEN the left side targets the existing
  // html content and replaces it with
  // the data from the array.
  // DAMN BRO THIS SHIT IS LIT
  // OKAYYYY IT'S ALL MAKING A LITTLE SENSE NOW

  // there are fucking TONS of these
  // built in selector functions to learn tho

  img.src = item.img;
  author.textContent = item.name;
  job.textContent = item.job;
  info.textContent = item.text;
});

---

