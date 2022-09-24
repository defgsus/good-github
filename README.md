## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-09-23](docs/good-messages/2022/2022-09-23.md)


2,130,480 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,130,480 were push events containing 3,139,645 commit messages that amount to 239,930,333 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 29 messages:


## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[d34fa4c642...](https://github.com/tgstation/tgstation/commit/d34fa4c642839215df5ba985d098a04e4d555b5b)
#### Friday 2022-09-23 00:03:06 by LemonInTheDark

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
## [r-barnes/pytorch](https://github.com/r-barnes/pytorch)@[afcc7c7f5c...](https://github.com/r-barnes/pytorch/commit/afcc7c7f5c7cef740241ff0abdae8d4f2ad22a03)
#### Friday 2022-09-23 00:59:33 by Andrew Gu

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
## [vercel/next.js](https://github.com/vercel/next.js)@[1bbd264216...](https://github.com/vercel/next.js/commit/1bbd2642164098ceb9cebfb36deba9aed7e8a53b)
#### Friday 2022-09-23 01:14:23 by abdennor

Add additional fix in hydration error document (#40675)

I had the same issue, so the fix that worked for me was pulled from this
thread https://stackoverflow.com/a/71870995

I have been experiencing the same problem lately with NextJS and i am
not sure if my observations are applicable to other libraries. I had
been wrapping my components with an improper tag that is, NextJS is not
comfortable having a p tag wrapping your divs, sections etc so it will
yell "Hydration failed because the initial UI does not match what was
rendered on the server". So I solved this problem by examining how my
elements were wrapping each other. With material UI you would need to be
cautious for example if you use a Typography component as a wrapper, the
default value of the component prop is "p" so you will experience the
error if you don't change the component value to something semantic. So
in my own opinion based on my personal experience the problem is caused
by improper arrangement of html elements and to solve the problem in the
context of NextJS one will have to reevaluate how they are arranging
their html element

<!--
Thanks for opening a PR! Your contribution is much appreciated.
To make sure your PR is handled as smoothly as possible we request that
you follow the checklist sections below.
Choose the right checklist for the change that you're making:
-->


## Documentation / Examples

- [x] Make sure the linting passes by running `pnpm lint`
- [ ] The "examples guidelines" are followed from [our contributing
doc](https://github.com/vercel/next.js/blob/canary/contributing/examples/adding-examples.md)

Co-authored-by: JJ Kasper <jj@jjsweb.site>

---
## [SmileycorpMC/Blood-Smeltery](https://github.com/SmileycorpMC/Blood-Smeltery)@[6d907e6049...](https://github.com/SmileycorpMC/Blood-Smeltery/commit/6d907e60491903b52ac1a1c44a5ea037fd0236b8)
#### Friday 2022-09-23 02:00:39 by Smileycorp

add features for 1.1.5

~ fixed bug with fluid capability in tartaric gems
+ readded support for tartaric gems to be filled with will fluid in the casting table
~ removed the requirement for demonic will crystals in the sentient modifier
+ new modifier which adds the abilities of the divination sigil to your tool
+ second tier to the modifier which adds the additional abilities of the seer's sigil
+ new tinkers tool material blood-rune made from the existing blood-seared stone fluid
	which repairs itself using your soul network's lp, reduces the cost of repairing for each blood-rune part in a tool
+ new tinkers tool material bloodbrass made from copper and life essence
	which gives a player lp in their soul network when they kill a monster
~ rebalanced blood-seared stone to match better with it's blood magic/tinkers counterparts
+ vexes can be melted in the smeltery into demonic will

---
## [eun0115/android_kernel_samsung_universal7904](https://github.com/eun0115/android_kernel_samsung_universal7904)@[9789d43c26...](https://github.com/eun0115/android_kernel_samsung_universal7904/commit/9789d43c268a5cdf9dbd5f2d515a1d54fe887de1)
#### Friday 2022-09-23 02:19:48 by Masahiro Yamada

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
[nc: Omit rpmsg, sdw, fslmc, tbsvc, and typec as they don't exist here
     Add of to avoid backporting two larger patches]
Signed-off-by: Nathan Chancellor <natechancellor@gmail.com>
Signed-off-by: Sasha Levin <sashal@kernel.org>

---
## [AlteredIntelligence/alteredintelligence.github.io](https://github.com/AlteredIntelligence/alteredintelligence.github.io)@[ea3906a016...](https://github.com/AlteredIntelligence/alteredintelligence.github.io/commit/ea3906a016009e1360ac679ec31f6648aa546b95)
#### Friday 2022-09-23 02:46:47 by donuts-are-good

Meantime, in the slums below Ronnie's Ranch, Cynthia feels as if some one
has made voodoo boxen of her and her favorite backplanes. On this fine
moonlit night, some horrible persona has been jabbing away at, dragging
magnets over, and surging these voodoo boxen.  Fortunately, they seem to
have gotten a bit bored and fallen asleep, for it looks like Cynthia may
get to go home.  However, she has made note to quickly put together a totem
of sweaty, sordid static straps, random bits of wire, flecks of once meaniful
oxide, bus grant cards, gummy worms, and some bits of old pdp backplane to
hang above the machine room.  This totem must be blessed by the old and wise
venerable god of unibus at once, before the idolatization of vme, q and pc
bus drive him to bitter revenge.  Alas, if this fails, and the voodoo boxen
aren't destroyed,  there may be more than worms in the apple. Next, the
arrival of voodoo optico transmitigational magneto killer paramecium, capable
of teleporting from cable to cable, screen to screen, ear to ear and hoof
to mouth...

---
## [anarazel/postgres](https://github.com/anarazel/postgres)@[1c27d16e6e...](https://github.com/anarazel/postgres/commit/1c27d16e6e5c1f463bbe1e9ece88dda811235165)
#### Friday 2022-09-23 03:42:22 by Tom Lane

Revise tree-walk APIs to improve spec compliance & silence warnings.

expression_tree_walker and allied functions have traditionally
declared their callback functions as, say, "bool (*walker) ()"
to allow for variation in the declared types of the callback
functions' context argument.  This is apparently going to be
forbidden by the next version of the C standard, and the latest
version of clang warns about that.  In any case it's always
been pretty poor for error-detection purposes, so fixing it is
a good thing to do.

What we want to do is change the callback argument declarations to
be like "bool (*walker) (Node *node, void *context)", which is
correct so far as expression_tree_walker and friends are concerned,
but not change the actual callback functions.  Strict compliance with
the C standard would require changing them to declare their arguments
as "void *context" and then cast to the appropriate context struct
type internally.  That'd be very invasive and it would also introduce
a bunch of opportunities for future bugs, since we'd no longer have
any check that the correct sort of context object is passed by outside
callers or internal recursion cases.  Therefore, we're just going
to ignore the standard's position that "void *" isn't necessarily
compatible with struct pointers.  No machine built in the last forty
or so years actually behaves that way, so it's not worth introducing
bug hazards for compatibility with long-dead hardware.

Therefore, to silence these compiler warnings, introduce a layer of
macro wrappers that cast the supplied function name to the official
argument type.  Thanks to our use of -Wcast-function-type, this will
still produce a warning if the supplied function is seriously
incompatible with the required signature, without going as far as
the official spec restriction does.

This method fixes the problem without any need for source code changes
outside nodeFuncs.h/.c.  However, it is an ABI break because the
physically called functions now have names ending in "_impl".  Hence
we can only fix it this way in HEAD.  In the back branches, we'll have
to settle for disabling -Wdeprecated-non-prototype.

Discussion: https://postgr.es/m/CA+hUKGKpHPDTv67Y+s6yiC8KH5OXeDg6a-twWo_xznKTcG0kSA@mail.gmail.com

---
## [10088/free-programming-books](https://github.com/10088/free-programming-books)@[5fd70502a0...](https://github.com/10088/free-programming-books/commit/5fd70502a063c46914fd444d2511c8233f81777f)
#### Friday 2022-09-23 04:31:54 by Mathieu FONTAINE

Update free-programming-cheatsheets.md - React (#7095)

I suggested a React cheat sheet that I use very often. It is one of the most exhaustive and qualitative in my opinion.

---
## [fiqri19102002/android_kernel_xiaomi_mojito](https://github.com/fiqri19102002/android_kernel_xiaomi_mojito)@[4fc39299f6...](https://github.com/fiqri19102002/android_kernel_xiaomi_mojito/commit/4fc39299f644d7da8b675428e134fd8d8dadc5dc)
#### Friday 2022-09-23 06:29:42 by Peter Zijlstra

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
Signed-off-by: Fiqri Ardyansyah <fiqri15072019@gmail.com>

---
## [Cassumbra/cocks-conquest](https://github.com/Cassumbra/cocks-conquest)@[f75ad4b953...](https://github.com/Cassumbra/cocks-conquest/commit/f75ad4b95349d3263f9530033d1cf1652c716b67)
#### Friday 2022-09-23 07:15:51 by Cassumbra

Wonkyness fixed!

Yeaaaaah
Problem was on my side all along.
Its a wonder that the thing managed to work things long when it was fucked up like this.
Truly bizarre.

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[931233db0e...](https://github.com/treckstar/yolo-octo-hipster/commit/931233db0e2099fc961ccd03e06b7009f4ac2366)
#### Friday 2022-09-23 07:22:02 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [CHOMPStation2/CHOMPStation2](https://github.com/CHOMPStation2/CHOMPStation2)@[cf301c6346...](https://github.com/CHOMPStation2/CHOMPStation2/commit/cf301c6346bbc9f9d9d4cae4d62799c9570f63dc)
#### Friday 2022-09-23 07:32:39 by Razgriz

[Manual MIRROR] Release Bugfixes and changes (MERGE BEFORE RELEASE)

Unfucks https://github.com/CHOMPStation2/CHOMPStation2/pull/5019 due to yet another github merge conflict with a god damn .dmi file. Missing map files, but that's ok because that's for virgo specific maps.

---
## [Offroaders123/NBT-Parser](https://github.com/Offroaders123/NBT-Parser)@[c07bc56def...](https://github.com/Offroaders123/NBT-Parser/commit/c07bc56defcef1fe05d0bacd01eead7f8dcace21)
#### Friday 2022-09-23 09:38:34 by Offroaders123

Experimental Module Type Definitions

Additions:
- Started doing some more advanced testing with TypeScript! I want to continue writing the library in JavaScript, but also provide types for TypeScript users, as well as just to provide more documentation for use in your text editor. I like not having to need a compile step, so that's my main reason for trying to stray away from simple TypeScript. I like the bare bones nature of vanilla JS, and being able to write once and run everywhere, thanks to feature checking and things like that.
- I started looking more into adding stricter TypeScript-like checking for vanilla JS files, and it actually works really well! I'm still trying to find the sweet spot though, and this isn't quite right yet. It is MUCH closer to what I want though, and I'm *super* stoked about that! I essentially want something like JSDoc, but with using TypeScript syntax instead. I don't mind writing the types in separate files, as they are more for autocompletion and IntelliSense than anything else. I mostly just want to make sure they are accurate before turning down the level of strictness back to normal JS. I imagine with time, I may end up liking TypeScript a lot, and it could just be growing pains, but I also don't want to leave the standards-land that comes along with vanilla JS. I know TypeScript is open source and all, but JavaScript is for sure here to stay. Well, at least as much as the web is, and that sounds pretty trustworthy to me. I am starting to like the benefits of TypeScript, but not sure if it is worth it enough personally to depend on it, and fully dive all of my codebases into it. Eventually there will be something else that we might want to rework into in the future anyways, haha. The JS ecosystem is definitely known to grow a lot! I can't wait to see where we are in the next few years, especially with the vanilla JS type declaration proposal from a few months ago :)
- This next iteration of type definitions isn't fully battle tested, nor is it compelete either, so take it with a grain of salt! I'm just doing some more learning to figure out how I want this to work, haha.

A lot more help! Thanks to people online in general, it still amazes me how much you can learn from out there, just by looking in the right places :D
https://stackoverflow.com/questions/38370549/how-to-use-typescript-definitions-to-get-intellisense-for-my-own-javascript-serv
https://stackoverflow.com/questions/46678663/add-custom-typings-file-in-a-javascript-vscode-project
https://stackoverflow.com/questions/51060207/declare-interfaces-in-typings-file-for-javascript#57322323
(These first three led me to my eventual working demo for what I have been trying to figure out, which these next ones also helped me with)
https://www.stefanjudis.com/today-i-learned/vs-code-supports-jsdoc-powered-type-checking/
https://github.com/tc39/proposal-type-annotations
https://stackoverflow.com/questions/29474144/using-typedef-to-define-a-specific-function-type
https://stackoverflow.com/questions/49836644/how-to-import-a-typedef-from-one-file-to-another-in-jsdoc-using-node-js
https://dev.to/briwa/how-strict-is-typescript-s-strict-mode-311a
https://bobbyhadz.com/blog/typescript-object-destructuring-function-parameters
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment

P.S.
Listened to Test for Echo today, I still really love that album!

---
## [Offroaders123/NBT-Parser](https://github.com/Offroaders123/NBT-Parser)@[b97fc03fa5...](https://github.com/Offroaders123/NBT-Parser/commit/b97fc03fa537e5e5599dbaf0f100d9780ca9f601)
#### Friday 2022-09-23 09:45:18 by Offroaders123

Tag Byte Type + Type Naming + GetTagByte

Lots of cool stuff! This is edging a bit closer to being API-like now :)

I keep reminding myself that I haven't even touched the writing half yet though, haha! These classes will makes things a lot easier though, the object structure actually feel like something maybe trustworthy at this point.

I can't wait to make something with this! I'm definitely going to add NBT editing as plain text to STE, that was one of my original use case ideas for this project. That also led me to work on NumText a bit some more a while back. Those changes haven't made it into stable yet, but a lot of my projects have moved forward, especially thanks to the more recent things I've looked into.

The biggest things in my JS dev world at the moment:
Web Components, ES6 Classes, ES Modules, Node (yes, I finally am getting used to that, haha), Promises / Async - Await, Compression Streams, TypedArrays (byte streams as a whole), Endianness (DEFINITELY deserves it's own category), and very recently, TypeScript! (.d.ts, and now full .ts)

These have been huge steps forward for me, and I really see how far it is pushing me forward from my projects just a short time ago. I look back at my practices before, and so many things have added together to make a big giant upgrade for my personal experience. I really like what can be done with all of these, and with how great learning these have been, I can't wait to eventually come back around to look at things like WebRTC. When I first looked into it, it was a bit over my head I think, and now that I understand the language structure a bit further, I have a bigger step up to wrap my head around it.

This library as a whole has been a great project for me, and it pretty much added a majority of those things I just listed to my experience catalog.

Well, thanks for vising my "blog", hope you like the writing XD

*Note: I also want to look into making my own page for my profile as an artist too, so like a landing page for album showcases and things like that. I have a lot of fun making artwork for my songs, and having an awesomely-styled website to go along with them sounds super cool to work on. Expect that eventually down the road too! Maybe Markdown would work best there :)

*Edit: Oh yeah, with this commit I decided to go back to the original string names for when the tag classes get stringified. I found these ones make a bit more sense with what you write for other JSON files. The class names are in PascalCase, and most of the time JSON is in camelCase, like JS tends to be. It also seemed a bit weird to write the names like the class names when I tried manually making an NBT JSON tree, to try it. Sometimes you can just stick with what works! (Eyouw, that would totally break all of the things I've done with this library in the last few weeks, HAHA. I am definitely not following the "If it ain't broke, don't fix it". I just got a gut feeling that it may bite me, but you gotta take the plunge sometimes!)

---
## [Offroaders123/NBT-Parser](https://github.com/Offroaders123/NBT-Parser)@[195acf3ba2...](https://github.com/Offroaders123/NBT-Parser/commit/195acf3ba20b76447d24d5ba91b6b2830c818c42)
#### Friday 2022-09-23 09:45:18 by Offroaders123

The Next Stage - Crazy rewrite!

Ok, so I almost have it all working, but not quite yet. There's gonna be a few more reworks, as I want to have it fully working and stable, both with the new features and API structure. Since so much is changing with the whole project at the moment, I'll officially go over all the changes once I have it working stable again.

Sorry there are so many crazy branches! With time, I definitely do want to get everything back into the one main branch.

*Edit later:
Yes, I'm coming back to go over this, haha

**Edit later later:
There was a demo for these changes that was fairly similar, and it had a better changelog for everything new, better than the one above this. I thought I'd keep that one, and add it below as a reference:

Crazy rewrite!

Added classes, and a ton of things.
Not quire working yet, so I'm gonna do yet another write with these changes *(this is the commit that this line references XD)*, just to reverse engineer the bugs before they get added, since the current stable implementation is, well, stable XD
I mostly did all of this yesterday, but I'm commiting it today since I want to kind of start fresh with it *(Aug 15, in regards to the original commit for this message. It was right before I added "The Reset", over on another branch though)*.

This library is essentially a complex combo of NBT.js, Prismarine-NBT, nbt-ts, and the NBT module in anvil-parser all combined. I like some parts from each of those, so I'm trying to make it exactly how I want it to work!

https://github.com/sjmulder/nbt-js
https://github.com/PrismarineJS/prismarine-nbt
https://github.dev/janispritzkau/nbt-ts
https://github.dev/Geoige/anvil-parser

A few other links that helped out a bit:
https://www.typescriptlang.org/docs/handbook/2/objects.html
https://stackoverflow.com/questions/56969950/optional-typed-immediately-destructured-parameters

---
## [Offroaders123/NBT-Parser](https://github.com/Offroaders123/NBT-Parser)@[af83701ff8...](https://github.com/Offroaders123/NBT-Parser/commit/af83701ff82077040a56d8541a96b7b36754210d)
#### Friday 2022-09-23 09:47:01 by Offroaders123

Here We Go!

This is the start date for when I started the rewrite that will appear in the next commit which follows this one. I worked on the changes for about a week and a half, off and on. I was doing a lot of experimentation and reworks overall, so I didn't keep commits for each step along the way, just the end result of my testing. TypeScript helped so much to get this going well! I really love it now. I think it will start to use it fully, across more of my projects now too. I also just recently found out about GitHub Packages, and I am hoping to use that as an alternative to npm! I want to try and keep everything all in once place, mainly the repo, but we'll see if that's doable, just like how the strict-JS with JSDoc wasn't quite up to the same level of magic that TypeScript provides. Maybe I'll give in and go to npm. We'll see!

---
## [Offroaders123/NBT-Parser](https://github.com/Offroaders123/NBT-Parser)@[2405eb8d6c...](https://github.com/Offroaders123/NBT-Parser/commit/2405eb8d6c48ff55481c48f96520774c911027e7)
#### Friday 2022-09-23 09:47:01 by Offroaders123

Back to TS!

Ok, while it is doable to have a dual JS-TS kind of workflow, plain TypeScript is just too nice not to use on it's own! I really love how streamlined it is to write in TS. It's so nice, I think I may have to just fully jump right into it! I am really glad I tried the mixed workflow too though. That could definitely be a valid workflow for a smaller project that doesn't need to be written as type-safe. I want this one to be very tight though, so TS will be a great way to make that happen!

Ok, and down to the changes. It's not just bringing it back to TypeScript, I actually rewrote everything from scratch! I found how a few other JS NBT libraries made it work, and it inspired me even more on how to make mine work. Part of the drive behind the new library structure and being in TypeScript, is that I realized that it will be very cool to use my new TypeScript knowledge, and to write type definitions for in-game NBT files (like the Bedrock level.dat, or a player save data file), and be able to use them safely typed, in strict JavaScript or TypeScript (the mixed setup with JS, or either a regular TS workflow). Alright, here we go:

Additions:
- Created a new NBTData wrapper class, and it holds metadata about the contained NBT object, such as what endianness and compression type it used in the original ArrayBuffer. This makes it so you can read an NBT ArrayBuffer, detect its file format, and be able to save it directly back to that same format without having to manually keep a reference to what format it used. Now the library makes it visible to you!

Changes:
- Modified all tags that JavaScript equivalents to now use those, instead of implementing a custom primitive wrapper object for each one. Now only primitives with no JavaScript equivalents have custom primitive wrapper classes. Those include the Byte, Short, Int, and Float primitive types.
- This tag change makes it so the values for the tag types are the tags themselves, rather than being an object which holds "type" and "value" keys. To check their types, now the library uses things like typeof or instanceof to check the tag's type.
- This also greatly simplifies the reading and writing methods on each the Reader and Writer classes, as now they only have to deal with the primitive itself, and it doesn't have to generate the primitive wrapper object for it anymore.
- If what I think this is, is what it is, I think it makes the data more declaratively structured, if that's the right term for it. Now you can just define a TypeScript interface type for the data, and it will document the data like a plain object, since that's what it is! If my description of that didn't make enough sense, I will be working on demos for that fairly soon!
- Re-gzipped the example bigtest.nbt file, as it appears to have used a different gzip format back from a few years ago. It was making my read-to-write checks fail, even though the actual NBT output ArrayBuffer was the exact same. So now those checks will work the same, since both the import file and export file use the gzip format used in Chrome/NodeJS, whatever that may be. Not sure what flavor of gzip Notch used to compress the original file, but it has a bit different of a header, causing the tests to fail.

Removals:
- Removed the existing API JSDoc comments, I am going to write new ones from scratch to reflect all of the new changes I made in this new rewrite.

---
## [maxdekrieger/SimpleArmory](https://github.com/maxdekrieger/SimpleArmory)@[7b781b8af6...](https://github.com/maxdekrieger/SimpleArmory/commit/7b781b8af627f20c5bd59c7b3981c777ad4cce28)
#### Friday 2022-09-23 09:51:43 by Antoine Pietri

Rework Reputation page UI

The previous design had several issues that made it hard to know what
your concrete progress was for reputations:

- There were red colors even when you had completed a reputation, which
  made it hard to quickly understand at a glance which things weren't
  exalted yet.
- The size of the reputation bars changed depending on the reputation
  tiers. Some special reputations with unusual tiers (Chromie,
  Fisherfriends, Ember Court etc) would have a progress bar with a
  smaller size, which made them stand out.
- There was a horrible hack to special-case the Tillers from MOP to
  properly display their friendship tiers by hardcoding their reputation
  IDs. However, this was partially broken and unusable for different
  tiers.

This commit tries to address these issues by doing several things.

1. Bars all have the same fixed max width. All the different friendship
   tiers make the bar widths automatically adjust as a ratio of
   the maximum reputation attainable.

2. The full bar is always shown, with all the reputation tiers.
   Obtaining reputation just makes the bar increasingly "fill" its
   background color.

3. The bar is now fully colored in the color of the maximum reputation
   attainable. This is easier to the eye, as it is easy to quickly check
   at a glance which reps are not completed yet.

4. Names of reputation tiers are only shown when hovering the individual
   bar segments. The current tier is shown to the right, in the same
   color as the bar itself.

---
## [aplaice/anki-ultimate-geography](https://github.com/aplaice/anki-ultimate-geography)@[6a5205fb72...](https://github.com/aplaice/anki-ultimate-geography/commit/6a5205fb7289ccc25bc5aabb77443e79dcb29d40)
#### Friday 2022-09-23 12:35:29 by Adam Plaice

Expand SADR country info mentioning alternative names

Fix #561.

As discussed in #561, saying that "Sahara Zachodnia" (Western Sahara)
is also known as SADR (in the Polish version), is ambiguous and
potentially misleading, since Western Sahara is both the name of the
geographic area (ignoring political associations) and one of the names
used for the partially recognised state.  However, AFAICT, we have the
exact same situation for Artsakh, in Polish, (Górski
Karabach (Nagorno-Karabakh) also known as Artsakh, where
Nagorno-Karabakh can refer both to the country and the geographical
area.).  Also, since we're generally dealing with countries, here, it
should be clear that we mean Western Sahara (the country) rather than
WS (the area), so I think my initial worry was overblown.

I'm not 100% sure if I have the correct gender for conosciuto in
Italian (should it agree with Repubblica.. or with stato?).

The same question holds for Czech — should známý agree with
..republika or with stát?

I've gone with agreement with stát for Czech (male) and with
republic (female) for Italian, because in the former the second clause
is separated only with a comma, while in the latter it's separated by
a semicolon.  The choice of separator was based on precedence in other
cases (Faroe islands and Taiwan).

---
## [kesor/dwm](https://github.com/kesor/dwm)@[67d76bdc68...](https://github.com/kesor/dwm/commit/67d76bdc68102df976177de351f65329d8683064)
#### Friday 2022-09-23 13:09:06 by Chris Down

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
## [tchelovilar/grafana-meme-dashboard](https://github.com/tchelovilar/grafana-meme-dashboard)@[9c9b525e3a...](https://github.com/tchelovilar/grafana-meme-dashboard/commit/9c9b525e3abe13fbd347228f618ff9ae2765ea0d)
#### Friday 2022-09-23 13:47:47 by meme-bot

New meme: "I hate my life" *2 hours later* "oh.." https://t.co/zoQlxXZHH5 https://t.co/N9KtI0ifNa

---
## [Dalekamistoso/duckstation](https://github.com/Dalekamistoso/duckstation)@[f9212363d3...](https://github.com/Dalekamistoso/duckstation/commit/f9212363d3370efcdb97d4f7de010b5f17bd5c5e)
#### Friday 2022-09-23 14:21:15 by IlDucci

Spanish translation overhaul + Addition of es-ES alternative

In its current state, the Spanish translations for Duckstation are a mess of different dialects, multiple translations for the same terms, mistranslations or excessively literal translations, and typos.

It's a shame, because you could feel that the initial translations were done with care, but were muddled with future revisions.

This commit tries to solve all of these and also change the initial decision of the first translator to have an "universal" "neutral" Spanish, as time has proven it's not possible without a dedicated translator who actually wants to have one Spanish language for all Spanish-speakers across the globe.

I'm not going to be that one, so the next option would be to duplicate the Spanish translations into two: one for the Spanish-speaking American people (called "Latin American Spanish", "español de Hispanoamérica", code es-419") and one for the European Spanish speakers (called "Spanish (Spain)", "español de España", code es-ES).

This distinction is used in multiple software applications that managed to have translators for different languages, and should also funnel any future Latin American Spanish and European Spanish translators to the corresponding file.

I have tried to follow as many existing terms and constructions as possible, restoring and/or rewording any phrasal constructions that were disunified by the multiple translators.

Since I have a limited experience with Latin American Spanish, this commit should be sent as a draft for additional revisions. I'm open to stick to having a single Spanish language, but it has to be done RIGHT.

This is an overview of changes across the board:
 - Added missing translations for QT and Android builds.
 - Unified translations between those.
 - Updated the QT file with the latest string values.
 - Massive removal of Title Uppercasing inherited from English in menu strings (the rules set by the Royal Academy of the Spanish Language, or RAE, limit the areas where Title Uppercasing is considered correct in Spanish. Menu names and window header texts are not within those areas).
 - Unified the treatment of users in the Latin American version to formal "ustedeo". This treatment could be modified with additional input.
 - Removed any gendering assumptions from any string directed towards the user (Are you sure...?, changed ¿Está/s seguro...? with ¿Seguro que...?)
 - Naturalization rewrites.
 - Typo corrections.
 - Gender corrections over definitive terms.
 - Adding missing NBSPs after required mathemathical characters or units.
 - Mass replacement of double/single quotes with angled quotes (the ones approved for Spanish).
 - Quoted non-Spanish, non-proper noun English words as dictated by RAE.
 - Removal of unwanted hyphens to join words (Auto-detectar with Detección automática, post-procesamiento with posprocesamiento). In Spanish, hyphens tend to separate, rather than join.
 - Revision of the compound forms, unified depending on Latin American Spanish or European Spanish.
 - Lowercased the first word of a text between parenthesis (Spanish rules dictate that they should be considered a continuation of the phrase, and thus, they should start with lowercase unless it's a proper noun or a word that must be uppercased) and corrected the positions between periods and parentheses.
 - Unified the accentuation rules for the adverb solo/sólo and the demostrative pronouns (este/ese/aquel) by removing all accents in European Spanish (following the RAE's 2010 suggestions) or keeping/adding them for Latin American Spanish (the 2010 rule ended up being a suggestion because while Spain has mostly deprecated those accents, it appears that the Latin American countries have not). To discuss?
 - Tweaked the key shortcuts for the QT menu to minimize duplicates.
 - Terms unified (this list doesn't represent the entirety of the changes):
    - Failed to (Fallo al/Error al): Fallo al
    - Hardcore Mode (Modo Hardcore/Modo Difícil): «hardcore» mode (Foreign non-proper nouns should be quoted, RetroAchievements does not have an official Spanish translation, so the term should be kept in English)
    - Enable/Disable (habilitado/deshabilitado/activado/desactivado/activo/inactivo): habilitado/deshabilitado
    - host (host/anfitrión/sistema): sistema, TO BE DETERMINED AND UNIFIED
    - Signed (numbers; firmados): (números) con signo
    - scan (verb and noun; escanear): buscar/búsqueda
    - Clear (something, like bindings or codes; despejar, limpiar): borrar/quitar
    - requirement (of a system, requisito/requerimento): requisito
    - input (of a controller, control): entrada
    - Threaded X (hilo de X): X multihilo
    - Frame Pacing (frame pacing): duración de fotogramas
    - XX-bit (XX-bit): XX bits (proper form)
    - Widescreen (screens, widescreen hacks; pantalla ancha, pantalla panorámica): pantalla panorámica
    - Antialiasing (anti-aliasing): Antialiasing (considered a proper noun by NVidia, doesn't need that hyphen)
    - hash: «hash» (could be discussed as "sumas de verificación", like on Dolphin)
    - Focus Loss (perder el foco): ir/entrar en segundo plano
    - toggle (verb for hotkeys, activar): alternar (as the key alternates between enabling and disabling the function, while "activate" might sound like it's just the enable part)
    - Rewind (function; retrocediendo, retrocedimiento): rebobinado (to discuss on LATAM Spanish)
    - shader (shader/sombreado): sombreador
    - resume (resumir): reanudar, continuar (resumir is a false friend)
    - Check (verb; chequear/revisar/comprobar): chequear (LATAM Spanish), comprobar (European Spanish)
    - Add (something; añadir/agregar): agregar (LATAM Spanish, to discuss) or añadir (European Spanish)
    - Enter/Input (ingrese, inserte): ingresar (LATAM Spanish) or introducir (European Spanish)
    - mouse (device; mouse/ratón): mouse (LATAM Spanish), ratón (European Spanish)
    - Auto-Detect (Auto-detectar): Detección automática
    - Controller (control): mando (for European Spanish only)
    - run (a game, the emulator; correr): ejecutar, funcionar (for European Spanish only)

---
## [AtariDreams/terminal](https://github.com/AtariDreams/terminal)@[b4b6636b49...](https://github.com/AtariDreams/terminal/commit/b4b6636b4952ac8ff6a9864f641973bb49d91ce4)
#### Friday 2022-09-23 14:43:35 by Mårten Rånge

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
## [RimiNosha/Skyrat-tg](https://github.com/RimiNosha/Skyrat-tg)@[e7230e8b4a...](https://github.com/RimiNosha/Skyrat-tg/commit/e7230e8b4a6d60e1b6c025b52b9f3d2fc26577a5)
#### Friday 2022-09-23 16:14:47 by SkyratBot

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
## [Fongang-Fonju-Boniface/Real-Gitt](https://github.com/Fongang-Fonju-Boniface/Real-Gitt)@[5fb0e76099...](https://github.com/Fongang-Fonju-Boniface/Real-Gitt/commit/5fb0e760997b6a37558ab4148780382f6a83d74a)
#### Friday 2022-09-23 17:17:36 by Skinny

now h2 says fuck you

Signed-off-by: Skinny <bonifacefongang9@gmail.com>

---
## [meow6969/i-am-a-gamer-epic-i-love-osu-wtf](https://github.com/meow6969/i-am-a-gamer-epic-i-love-osu-wtf)@[0e1b607815...](https://github.com/meow6969/i-am-a-gamer-epic-i-love-osu-wtf/commit/0e1b607815bb79791b65cbe309c3cfa3f04a025d)
#### Friday 2022-09-23 17:41:35 by meow6969

got minecraft blocked fuck you im not solving anything tday

---
## [ThakaSartu/saa2](https://github.com/ThakaSartu/saa2)@[83d98454c5...](https://github.com/ThakaSartu/saa2/commit/83d98454c5f91507b0d0587d96fd2b1025b6c72e)
#### Friday 2022-09-23 18:37:26 by ThakaSartu

Wisdom Body Lyrics
[Intro]
No, man, all bitches are the same, just like my hoes, you know?
I keep 'em broke, wake up one morning with some money
They're subject to go crazy, you know?
I keep 'em looking good, pretty and all that, you know, but no dough
When I get a bitch, I got a bitch (Right on)

---
## [petrelharp/pyslim](https://github.com/petrelharp/pyslim)@[3571a25e1f...](https://github.com/petrelharp/pyslim/commit/3571a25e1f8500f1a036f3a8a9deb1730c580e55)
#### Friday 2022-09-23 22:15:38 by andrewkern

added slim clone and compile to GH actions

alter when to run actions for dev

add windows to list of oses

pip failing

conditional on slim build

add slim windows build rule

MORE WINDOZE

adding SLiM depends

debugging

think we are working?

still debugging

still futzing

thrash

adding autotools to msys2 install stuff

thrash

add conda

thrash

get rid of tmate

thrash

dont' need source proffile?

ugh

tmate revenge

adding conditional on tmate

removed source from build

tmatey

setup auto conda env

updated tests

moar tests

typo

mamba

no pip?

ugh

back to miniconda

pwr

yml

moar

mamba redux?

blurg

yarg

still going

last one

Update tests.yml

blag2

altering conda vs pip balance

urg

jkhj

shell nightmare

try another change

which pip

moving stuff

adsf

dsfk

asd

adsfdasf

msys shell madness

asdfasdf

Update tests.yml

as;dlkfj

sadf

happy windows filepaths from conf

sdafdsa

passing tests!

remove dev branch action

removed print

comment out slim build step on osx/ubuntu

Update tests.yml

comments

refactor test actions

trying to limit matrix of sys / env

exclude rather than include

arrays

less is more

even fewer jobs?

kjh

sdf

more excludes?

last one for the night

jhlkj

asd

jkhkj

lkjlkj

sad

tmate

adfasdf

which dot file?

why isn't conda working?

try again

asdfasdf

bump cache

no base

asdf

fast debug

mamba with osx

micro

fixing micromamba

try cache on micro

add linux in

oops should have been ubuntu

actually try tests for a min

okay here we go windoze

conditions

now with tests

even cleaner

cache slim

true

cache2

cawde

undo cache

parathenses

asdfsad

cache redux

final clean

moar

new cache path

tmate to find windows path

cache path again

zstd

path again

sdfasd

kjhglghj

more zstd

adfs

ugh

add zstd to conda reqs

add workaround for windows cache

pinning cache action

holy shit caching is working?!?

ha

add back macos, ubuntu

ready for prime time

---
## [Knifa/msp-osd](https://github.com/Knifa/msp-osd)@[1b8b4b6f67...](https://github.com/Knifa/msp-osd/commit/1b8b4b6f67e471360be4560071d0edbc5a8a5205)
#### Friday 2022-09-23 23:20:06 by Brian Ledbetter

Fakehd and Config Options (#52) - thank you @benlumley

* Squashed commit of the following:

commit b9bcccbf76974e34c672b0e39c1443bb6ac84af9
Author: Ben Lumley <ben@benlumley.co.uk>
Date:   Tue Sep 20 22:48:35 2022 +0100

    switch to config

commit c50d23104e4fb4f6e6a25b2bb0b72fcecc6128f7
Author: Ben Lumley <ben@benlumley.co.uk>
Date:   Tue Sep 20 14:16:24 2022 +0100

    changed mind; y direction doesn't need the 1 offset - nicer to have it near the edge; then you can get things inline with the goggles own osd at the bottom

commit 4af3df6c126ac273b03e9191699b92513e1b3f2d
Author: Ben Lumley <ben@benlumley.co.uk>
Date:   Mon Sep 19 20:47:59 2022 +0100

    Battery symbols flash when in warning state; so can't use them to trigger centering :(

commit 689384f0449daed42929d90f19c1946368fd0a31
Author: Ben Lumley <ben@benlumley.co.uk>
Date:   Mon Sep 19 10:26:58 2022 +0100

    In from the edges a bit; we have spare rows/cols - in my opinion it looks better not to have everything literally touching the sides

commit db06e4885c93a9a0350ffab6afa08fcb068fd63a
Author: Ben Lumley <ben@benlumley.co.uk>
Date:   Fri Sep 16 19:39:50 2022 +0100

    Docs review + add fakehd

commit b6f20c0cf2e74e6bca98555c731ea4b11f41d6f4
Author: Ben Lumley <ben@benlumley.co.uk>
Date:   Thu Sep 15 22:49:18 2022 +0100

    Debugged/working

commit 8000b88d022fb40e30e0aa7f03df0613c637ece8
Author: Ben Lumley <ben@benlumley.co.uk>
Date:   Fri Sep 2 00:15:28 2022 +0100

    Attempt at proof of concept to 'spread' the SD osd to the corners + middle of the HD OSD.

    Not managed to get it running to test. But here's the idea:

    BF grid is 16 * 30
    HD is 18 * 50

    BF Rows 1-5 -> HD Rows 1-5
    BF Rows 6-10 -> HD Rows 7-11
    BF Rows 11-16 -> HD Rows 12-18

    BF Cols 1-10 -> HD Cols 1-10
    BF Cols 11-20 -> HD Cols 20 - 30
    BF Cols 21-30 -> HD Cols 40 - 50

    Visually, divide the OSD into a 3*3 grid and stretch it to the top/bottom/left/right corners.

    I tend to put osd elements in the bottom corners, bottom middle + the warnings in the middle. So for me at least; this is useful.

    Obvious drawback; the menus gonna look weird!

    fix for force hd not working because BF never even sends the MSP command; it needs to default to it earlier.
    also add 2 unsplit rows for wider elemenets - i like warnings in the middle of the screen

    Add full display info; attempt to detect menu/post flight stats and switch to centering in this case

    Remove testing code

    make code paths simpler

    Find the center trigger instead of hard coding

    configurable; with a file for now

commit 60215e0240cbe5d34d0db447b01d948808705ed2
Author: bri3d <brian@brianledbetter.com>
Date:   Tue Sep 20 22:24:16 2022 -0600

    forgot an important directory...

commit 1c5ed2a88feb03bf209e4ed3c3ac4ed277681f47
Author: bri3d <brian@brianledbetter.com>
Date:   Thu Sep 15 21:51:48 2022 -0600

    add goggles config file

commit cfe24e265e8a3bfa92c34d6fc0e9594b63f98928
Author: bri3d <brian@brianledbetter.com>
Date:   Thu Sep 15 21:23:00 2022 -0600

    add JSON config support

* add fake HD to schema

* add ability to disable AU data overlay, add comments, cleanup

* add proper ipk deps and readme

Co-authored-by: Ben Lumley <ben@benlumley.co.uk>

---

