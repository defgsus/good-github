## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-09-14](docs/good-messages/2022/2022-09-14.md)


2,180,447 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,180,447 were push events containing 3,435,065 commit messages that amount to 241,758,361 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 33 messages:


## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[ad01ab5ed0...](https://github.com/tgstation/tgstation/commit/ad01ab5ed0a5f80278076b1e0e6ac33fe73b0e32)
#### Wednesday 2022-09-14 00:03:06 by LemonInTheDark

Fixes asset caching (#69852)

The asset was being loaded, seeing that fully_generated is false, so it
attempts to rebuild. The rebuilding clears the existing file cache, and
fucks us.

Life is pain.

---
## [KDr2/pytorch](https://github.com/KDr2/pytorch)@[afcc7c7f5c...](https://github.com/KDr2/pytorch/commit/afcc7c7f5c7cef740241ff0abdae8d4f2ad22a03)
#### Wednesday 2022-09-14 00:03:40 by Andrew Gu

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
## [All-Blockchains/bitcoin](https://github.com/All-Blockchains/bitcoin)@[3a7e0a210c...](https://github.com/All-Blockchains/bitcoin/commit/3a7e0a210c86e3c1750c7e04e3d1d689cf92ddaa)
#### Wednesday 2022-09-14 00:10:16 by glozow

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
## [InsightfulParasite/lobotomy-corp13](https://github.com/InsightfulParasite/lobotomy-corp13)@[f0e6476eb0...](https://github.com/InsightfulParasite/lobotomy-corp13/commit/f0e6476eb051d781f7e4d0be7976dff0ff72fda0)
#### Wednesday 2022-09-14 00:13:48 by Lance

The Great Workening

Attribute Levels Displayed

No thoughts were had, thoughts injected.

Attribute Levels go brrr

Requested Change Made

WHOOPS WRONG PARENTHESIS

I swear I know how Clamps work

Holy shit how did this not get found out earlier

---
## [libretro/glsl-shaders](https://github.com/libretro/glsl-shaders)@[0c3d862e0d...](https://github.com/libretro/glsl-shaders/commit/0c3d862e0d361b043d11f7b1e42be24134fe362b)
#### Wednesday 2022-09-14 00:54:22 by mudlord

Deobfuscated shit TV shader. Feel free to cannibalize. (#179)

* It's been a long time.
We shouldn't of left you.
Without a dope beat to step to.
Time's up.

* fuck.

---
## [Pas2704/PluginHub](https://github.com/Pas2704/PluginHub)@[016e22a0c7...](https://github.com/Pas2704/PluginHub/commit/016e22a0c7393f2709f37cc38f8ef256f5428125)
#### Wednesday 2022-09-14 01:24:22 by BipolarExpedition

Adding GPS Helper Mod with author permission

Adding GPS Helper Mod with author permission 

Kaito  [author] Jul 1 @ 1:20pm 
No, I had not considered it yet. Feel free to have a look. I'm kinda busy irl right now, so it would be a while before I could look.

In theory it all runs on the client, but you'll have to check the API.

Doc1979 Jun 28 @ 4:37pm 
Does this use server only commands? If not, have you thought of making it into a PluginLoader plugin? I was thinking of looking at your github to see if I could convert it myself, but if its already on your todo list, I'll wait

---
## [ammarfaizi2/linux-fork](https://github.com/ammarfaizi2/linux-fork)@[9867ab2259...](https://github.com/ammarfaizi2/linux-fork/commit/9867ab2259d938b5650738e9a339ce9211ec567a)
#### Wednesday 2022-09-14 02:41:09 by Peter Xu

mm/x86: use SWP_TYPE_BITS in 3-level swap macros

Patch series "mm: Remember a/d bits for migration entries", v4.


Problem
=======

When migrating a page, right now we always mark the migrated page as old &
clean.

However that could lead to at least two problems:

  (1) We lost the real hot/cold information while we could have persisted.
      That information shouldn't change even if the backing page is changed
      after the migration,

  (2) There can be always extra overhead on the immediate next access to
      any migrated page, because hardware MMU needs cycles to set the young
      bit again for reads, and dirty bits for write, as long as the
      hardware MMU supports these bits.

Many of the recent upstream works showed that (2) is not something trivial
and actually very measurable.  In my test case, reading 1G chunk of memory
- jumping in page size intervals - could take 99ms just because of the
extra setting on the young bit on a generic x86_64 system, comparing to
4ms if young set.

This issue is originally reported by Andrea Arcangeli.

Solution
========

To solve this problem, this patchset tries to remember the young/dirty
bits in the migration entries and carry them over when recovering the
ptes.

We have the chance to do so because in many systems the swap offset is not
really fully used.  Migration entries use swp offset to store PFN only,
while the PFN is normally not as large as swp offset and normally smaller.
It means we do have some free bits in swp offset that we can use to store
things like A/D bits, and that's how this series tried to approach this
problem.

max_swapfile_size() is used here to detect per-arch offset length in swp
entries.  We'll automatically remember the A/D bits when we find that we
have enough swp offset field to keep both the PFN and the extra bits.

Since max_swapfile_size() can be slow, the last two patches cache the
results for it and also swap_migration_ad_supported as a whole.

Known Issues / TODOs
====================

We still haven't taught madvise() to recognize the new A/D bits in
migration entries, namely MADV_COLD/MADV_FREE.  E.g.  when MADV_COLD upon
a migration entry.  It's not clear yet on whether we should clear the A
bit, or we should just drop the entry directly.

We didn't teach idle page tracking on the new migration entries, because
it'll need larger rework on the tree on rmap pgtable walk.  However it
should make it already better because before this patchset page will be
old page after migration, so the series will fix potential false negative
of idle page tracking when pages were migrated before observing.

The other thing is migration A/D bits will not start to working for
private device swap entries.  The code is there for completeness but since
private device swap entries do not yet have fields to store A/D bits, even
if we'll persistent A/D across present pte switching to migration entry,
we'll lose it again when the migration entry converted to private device
swap entry.

Tests
=====

After the patchset applied, the immediate read access test [1] of above 1G
chunk after migration can shrink from 99ms to 4ms.  The test is done by
moving 1G pages from node 0->1->0 then read it in page size jumps.  The
test is with Intel(R) Xeon(R) CPU E5-2630 v4 @ 2.20GHz.

Similar effect can also be measured when writting the memory the 1st time
after migration.

After applying the patchset, both initial immediate read/write after page
migrated will perform similarly like before migration happened.

Patch Layout
============

Patch 1-2:  Cleanups from either previous versions or on swapops.h macros.

Patch 3-4:  Prepare for the introduction of migration A/D bits

Patch 5:    The core patch to remember young/dirty bit in swap offsets.

Patch 6-7:  Cache relevant fields to make migration_entry_supports_ad() fast.

[1] https://github.com/xzpeter/clibs/blob/master/misc/swap-young.c


This patch (of 7):

Replace all the magic "5" with the macro.

Link: https://lkml.kernel.org/r/20220811161331.37055-1-peterx@redhat.com
Link: https://lkml.kernel.org/r/20220811161331.37055-2-peterx@redhat.com
Signed-off-by: Peter Xu <peterx@redhat.com>
Reviewed-by: David Hildenbrand <david@redhat.com>
Reviewed-by: Huang Ying <ying.huang@intel.com>
Cc: Hugh Dickins <hughd@google.com>
Cc: "Kirill A . Shutemov" <kirill@shutemov.name>
Cc: Alistair Popple <apopple@nvidia.com>
Cc: Andrea Arcangeli <aarcange@redhat.com>
Cc: Minchan Kim <minchan@kernel.org>
Cc: Andi Kleen <andi.kleen@intel.com>
Cc: Nadav Amit <nadav.amit@gmail.com>
Cc: Vlastimil Babka <vbabka@suse.cz>
Cc: Dave Hansen <dave.hansen@intel.com>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>

---
## [ammarfaizi2/linux-fork](https://github.com/ammarfaizi2/linux-fork)@[14cac88d73...](https://github.com/ammarfaizi2/linux-fork/commit/14cac88d73d469d0b8c475adc4d4f0ad37fdf615)
#### Wednesday 2022-09-14 02:41:09 by Johannes Weiner

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
## [matchu/impress-2020](https://github.com/matchu/impress-2020)@[d9ca07c9b0...](https://github.com/matchu/impress-2020/commit/d9ca07c9b0b951a4a1f442545b1a438d5cfa790b)
#### Wednesday 2022-09-14 02:52:21 by Matchu

Use wget for archive:create:download-urls

Hey this is an exciting development! A list of URLs, that we want to clone onto our hard drive, turns out to be something `wget` is already very good at!

Originally I used `wget`'s `--input-file` option to process the `urls-cache.txt` file, but then I learned how to parallelize it from this StackOverflow answer: https://stackoverflow.com/a/11850469/107415. (Following the guidance in the comments, I removed `-n 1`, to avoid the overhead of extra processes and allow `wget` instances to keep using shared connections over time. Idk why it was in there, maybe the author didn't know `wget` accepts multiple args?)

Anyway yeah, it's working great, except for the weird images.neopets.com downtime! 😅 Specifically I'm noticing that all the item thumbnail images came back really fast, but the customization images are taking for-EV-er. I wonder if that's just caching properties, or if there's a different backing server for it and it's responding much more slowly? Who's to say!

In any case, I'm keeping the timeout in this script pretty low (10 seconds), and just letting failures fail. We can try re-running it again sometime when the downtime is resolved or the cache is warmed up.

---
## [Recoherent/Shiptest](https://github.com/Recoherent/Shiptest)@[4d3770e4c1...](https://github.com/Recoherent/Shiptest/commit/4d3770e4c17ec5a4818775896ba3c705e3e5fa6f)
#### Wednesday 2022-09-14 04:34:32 by Recoherent

stupid little tail

dumb tail shits still regrowing idiot get clipped nerd

---
## [e-kwsm/git](https://github.com/e-kwsm/git)@[5beca49a0b...](https://github.com/e-kwsm/git/commit/5beca49a0b1f3c6d05a4437ca037ab2123a2de57)
#### Wednesday 2022-09-14 05:59:02 by Ævar Arnfjörð Bjarmason

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
## [timdev/mezzio-flash](https://github.com/timdev/mezzio-flash)@[9e07ce683e...](https://github.com/timdev/mezzio-flash/commit/9e07ce683ead671c0ee2be9ea26ea1e24d2b6808)
#### Wednesday 2022-09-14 08:03:45 by Michał Bundyra

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
## [nationalarchives/ds-caselaw-public-ui](https://github.com/nationalarchives/ds-caselaw-public-ui)@[0889e25786...](https://github.com/nationalarchives/ds-caselaw-public-ui/commit/0889e25786166645c4dfecc79ef9d6e4fce59cb9)
#### Wednesday 2022-09-14 08:54:34 by Tim Cowlishaw

Fix 'back to top' UI bug.

As reported on trello ticket 391 - on short judgements (eg https://caselaw.nationalarchives.gov.uk/ewhc/comm/2011/68#js-phase-banner), the 'back to top' link appears above the site header.

This ticket fixes this by only displaying the link when the length of the judgement itself exceeds the size of the viewport.

(In addition, i've changed the .editorconfig file to respect what appears to be the norm in the existing code of useing 4 spaces for tabs in js files, without this my editor tends to mangle every file I touch with whitespace changes - hope this is ok!)

While this is a very small change I'd appreciate review, particularly on the following two points:

1) Is this an appropriate place to be using JQuery? I'm basing this decision on the recommendation in [TNA's developer gude](https://github.com/nationalarchives/front-end-development-guide/blob/master/development-guide.md) as things like viewport dimensions tend in my experience to be a cross-browser compatibility can of worms. Very happy to revise in vanilla JS if that's more appropriate here.

2) I'm not 100% happy with adding a second ".hidden" class to the link and managing the state of both a 'shown' and 'hidden' class independently - however, this is necessary to ensure that the 'back to top' link is not shown at all on short judgements (it's rather unsightly and redundant even at the bottom of the page) when JS is enabled, while also ensuring that it's shown and is functional when js is not enabled or not loaded.

Anyway, sorry for the ridiculous commit-message to lines-changed ratio, I'll be briefer about these things when I've got settled in :-)

Many thanks!

Tim

---
## [digitalservicebund/ris-backend-service](https://github.com/digitalservicebund/ris-backend-service)@[67af6e26c7...](https://github.com/digitalservicebund/ris-backend-service/commit/67af6e26c7b4d1ab7ae68f9003d4666eddbba66b)
#### Wednesday 2022-09-14 09:59:03 by Thore Strassburg

Feat(web): introduce typed input field approach

The `InputGroup` component allows to specify a list of inputs that
should be rendered and mound their model values to an object. So far
this only works for text inputs (using the `TextInput` component). The
goal is to make this more flexible and allow also other types of inputs.

To support this higher level goal, a generic `InputElement` component
has been added. The idea of this component is to act like the standard
HTML `<input />` component, but use our custom input components. Thereby
it receives the attribute `type` (as `<input />` does). This property
defines which actual input component will be rendered. In forwards the
model value bound to itself to the input component. Furthermore it can
receive any further attributes for the specific input which it will bind
to the component instance.
These two properties, the type and the input specific attributes are now
part of the definition of an input field. Thereby the `InputGroup` can
simply instantiate the `InputElement`.

To support this "generic" feature with more typing constraints, several
interfaces and types have been defined. As these types are part of the
higher level concept, they are part of the `domain`. This concept of
having objects with editable (or not) properties of different kind and
the rendering into forms, is independent of the actual visual frontend
implementation. It is not Vue specific and would still be valid and
working if we would switch to React or Angular.
The types are quite straight forward in an extending manner. One of the
first and strongest benefits is, that it allows us to type-check our
field definitions. These have been split into separate TypeScript files
to keep them more organized and, more importantly, being typed. The type
interference is so smart, once a field defines the requires `type`
property TypeScript will check the whole field definition if it is
compatible, has missing properties, correct property types etc.
Furthermore do this types used in the Vue components which implement
this higher level concept. The components do no more define these types
locally in a top-down-dependency manner. Rather we have a dependency
inversion to the domain now.

Unfortunately is Vue not (yet) powerful to support fully generic
components. And even to the degree it is possible, it is
a hack/workaround that leads to ugly code that is still not fully
generic. In result it is currently not possible to provide 100% type
safeness. It is not (yet) possible to tell the `InputElement` that if
`type` is of a specific enumeration entry, the `modelValue` must be of
a specific type. E.g. for a text type, the value is a string. But for
a checkbox a boolean. The same goes for the input related attributes.
Nevertheless the typing got restricted to some degree. Further
improvements planned as soon as possible. After all, even with the old
feature set only, the typing it stronger than before.

Please note that the current file-directory-structure under `domain/`
is still quite chaotic. But it was so too before. What the "domain"
actually is for the front-end, still has to be defined completely.
Therefore the most simple and flat approach has been chosen. Anyway,
an `index.ts` is used now to represent the `domain` more as a complete
module rather than individual parts. Other parts of the code base should
not know about the internal details.

After of all, this commit is too big and should have been split at least
into two. My apologizes for this mistake.

RISDEV-311

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[b3b85cae9b...](https://github.com/odoo-dev/odoo/commit/b3b85cae9b1951b82053d7c6b55e559cbc48307d)
#### Wednesday 2022-09-14 09:59:07 by Xavier Morel

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

closes odoo/odoo#99458

Signed-off-by: Xavier Morel (xmo) <xmo@odoo.com>

---
## [Romeo-PHILLIPS/alltheplaces](https://github.com/Romeo-PHILLIPS/alltheplaces)@[c7b46c2663...](https://github.com/Romeo-PHILLIPS/alltheplaces/commit/c7b46c26636f460702c1eec68846959710613515)
#### Wednesday 2022-09-14 10:12:54 by Joe Dixon

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
## [LemonInTheDark/tgstation](https://github.com/LemonInTheDark/tgstation)@[46d50c8100...](https://github.com/LemonInTheDark/tgstation/commit/46d50c81009b292db7668eea800873b80d5fd55a)
#### Wednesday 2022-09-14 11:17:01 by LemonInTheDark

Airlock open delay audit

A: Mineral doors no longer take 6 SECONDS to open if you bump anything
beforehand. Holy shit why would you do this.
B: Airlocks no longer require you to have not bumped anything in a
second, lowered to 0.3 seconds. This is safe because I've moved shock
immunity to its own logic. This should make opening doors feel less
horrible

---
## [david-rowley/postgres](https://github.com/david-rowley/postgres)@[7fed801135...](https://github.com/david-rowley/postgres/commit/7fed801135bae14d63b11ee4a10f6083767046d8)
#### Wednesday 2022-09-14 11:44:31 by Tom Lane

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
## [Heroic-Games-Launcher/HeroicGamesLauncher](https://github.com/Heroic-Games-Launcher/HeroicGamesLauncher)@[3f6541c8a7...](https://github.com/Heroic-Games-Launcher/HeroicGamesLauncher/commit/3f6541c8a700511cea9f0c9b572a5d2138ee76e3)
#### Wednesday 2022-09-14 12:22:42 by Mathis Dröge

Improve README and developer experience (#1807)

* Update VSCode configuration

* Lots of README changes

- Update our bages; might've overdone it a little, but they're fun to add :^)
- Add badges for Web Technologies used
- Rewrite & bump up system requirements a bit
- Wrap the Language list, Development in a container, and Screenshots in
  <details>; this makes the page load faster and makes it seem less
  daunting
- Add a Flathub badge to the Flatpak section
- Unify Linux install instructions (as much as possible)
- Remove 3rd-party APT repository
  In my opinion, we have enough distribution formats already, and the
  install instructions are a little dodgy
- Add Beta AUR package to the list
- Clarify Windows install instructions by splitting up WinGet and manual
  install
- Make "Development environment" its own section
- Remove Beta and Alpha notes on Windows and macOS build instructions
- Explain what exactly is happening when you run `yarn dev` and in which
  scenarios you might want to use it
- Move the "Back to top" badge to the actual bottom of the page

* Add a Content Security Policy

This doesn't really do much in our situation:
- Just in case someone ever manages to load a website in Heroic's main
  window, no JS can run inside it
- Gets rid of the warning in the console when testing with `yarn dev`

I've tested the Webviews (unaffected) and links to ProtonDB and such
(also unaffected, not sure why though). Please test if this breaks
anything

---
## [Sem104/abyss-lab](https://github.com/Sem104/abyss-lab)@[575859630f...](https://github.com/Sem104/abyss-lab/commit/575859630f36c5bbc655cd045b45697b6eb47632)
#### Wednesday 2022-09-14 13:13:26 by Sem104

Finally we're done

YESSSSSSSSSSSSSSSSSSSSSSSSS, THE LAST CHANGE WORKED

We were only missing the spacebar/mouse click input "[ \ s ]" cuz I didn't think about it yesterday but hell fucken yeah chapter 0 is finally done

---
## [Jeansonancheta/filite](https://github.com/Jeansonancheta/filite)@[c33872ace6...](https://github.com/Jeansonancheta/filite/commit/c33872ace6a028e745930b148dbddfb81465b220)
#### Wednesday 2022-09-14 13:39:32 by Jeansonancheta

Legit Bank Wire Transfer Logs Hack PayPal Cashapp 

****SHOP IS OPEN AND NOW SELLING****
 
Hello all new customers, I now have for sale all types online offers.  
Buy secured Hacked PayPal accounts, Bank logins , Westen union transfer, credit card top-up, cvv, smtp, rdp, virus, rat, inbox mailer, email leads, msr tracks 1and2, dumps, pin leads, warez, spot option merchant accounts, Money Booker, skrill account all with very high balance all with proofs of transactions and secured source. I have secured a well balance merchant company account which is capable of running multiple transfers cashing out with zero theft and no traces of future charges securing a long term business partnership. Add me up via Telegram Signal WhatsApp Skype ICQ on +17197894109
 
All transactions are secured and with zero theft and no charge back.
Contact me for long time business partnership and top class service..
 
Contact:
 
Email: Jeansonancheta007@gmail.com
 
Phone number: +1 7197894109
 
Skype : Jeanson Ancheta
 
iTunes Accounts, Dumps, warez and fullz info are also available
I have a strong chain of prestigious customers all over the world which i have vowed never to break this chain..
 
Western Union Transfer is with maximum western union transfer limit.
I make transfer to countries all over the world and it takes
1- 12hours maximum to get MTCN and info .
Transfer charges requirements and rate are below..
 
1: Full name 
 2: Cell number (Not Necessary) 
 3: City  
4: Country
5: Valid email for sending you MTCN info..
 
 
Transfer Rates :
 
$1800 = $150
$3000 = $250
$4500 = $350
$5000 = $400
 
Bank Transfers : My bank transfer services is from an offshore server allowing you have neither trace back nor charge back. It is my
responsibility to transfer the required amount into your account and you shall have no difficulty to handle the bankers because it will be safe on your side. Transferring to any bank all over the
world..
 
Info needed for Bank transfers :-
1: Bank name
2: Bank address
3: Zip code
4: Account Holder Name
5: Account number
6: Account Type
7: Routing number
 
Bank transfer will take maximum 6hour for reflection and safe cash out of money in bank account.
 
Bank Transfer rates-:
 
$5000   = $450
$15000 = $800
$20000 = $1000
$30000 = $1500
$50000 = $2000
 
PayPal Transfer :- Using hacked and verified PayPal accounts to transfer PayPal account to account transfer. Being a genius, you can
easily penetrate PayPal and enjoy big free online money from it.
this depends on you and this is the most safest way to
earn money. (transferring all over the world except
banned/blacklisted countries)
 
 
PayPal Transfer Rates :
 
$3500 = $250
$5000 = $400
$10000 = $800
$15000  = $1000
$25000 = $1500
 
 
Credit-card Top Up Rates:-
 
$1800 = $150
$3000 = $250
$5000 = $350
$10000 = $800
$15000 = $1200
 
 
ATM SKIMMERS PRICE LIST
 
Wincor with keypad $700
Atm skimmer wincor nixdorf : $3500
Atm skimmer wincor: $3500
Atm skimmer slimm: $3000
Atm skimmer slim : $2500
Atm skimmer ncr: $3000
Atm skimmer die-bold opteva: $2500
Atm skimmer die bold: $2300
Atm skimmer universal: $3500
Atm skimmer small: $2000
 
***Also selling RDP, SMTP SERVERS, WEB-MAILS, MAILERS, BULK MAILS
(US/UK based) DATING ACCOUNTS, c Panel HOSTING, Hacked Panels,
CC dumps.
 
 
**NOTE
 
Transactions are totally secured and transfer rates can't be compromised
ensuring the chain of partnership appreciates.
 
 
*** TERMS AND CONDITIONS***
Please read offers carefully and note that we do not offer any free nor test transactions and no pranks.. Let's keep this professional..
 
 
Contact:
 
Skype : Jeanson Ancheta
 
Email: Jeansonancheta007@gmail.com
 
Phone number: +1 7197894109
 
Our fidelity is our word of honor which is our bond and guarantee of best service
to all customers from anywhere in the world..
 
CUSTOMERS SATISFACTION, OUR DELIGHT..!
 
 
****100 % SECURED AND PROOF OF TRANSACTIONS****
                     VERIFIED BY ADMIN

---
## [sypneiwski/pytorch](https://github.com/sypneiwski/pytorch)@[4c8cfb57aa...](https://github.com/sypneiwski/pytorch/commit/4c8cfb57aa3ac58112efb693635198b07edf008f)
#### Wednesday 2022-09-14 15:18:48 by Edward Z. Yang

Convert SymInt tracing to mode based tracing (#83380)

We're on our way to deleting ProxyTensor entirely (see https://github.com/pytorch/pytorch/pull/83330 ), but before we can do that, we have to delete ProxySymInt first. Here's the plan.

Changes in torch.fx.experimental.symbolic_shapes

* The general idea is to do mode based tracing. This means we need a mode that can interpose on all SymInt operations. There are a few ways to do this, but I've done it the easy way: (1) I have a separate mode for SymInt operations specifically called SymDispatchMode, and (2) this mode operates on PySymInt (and not the basic SymInt which is user visible). I elided Int from the name because if we add SymFloats I want to use the same mode to handle those as well, and I used Dispatch rather than Function because this is the "inner" dispatch operating PySymInt and not SymInt (this is not a perfect analogy, but SymFunctionMode definitely seemed wrong as you still must go through the C++ binding.) The mode is entirely implemented in Python for ease of implementation. We could have implemented this more symmetrically to TorchFunctionMode in C++, but I leave that as later work; this API is unlikely to get used by others (unlike TorchFunctionMode). One downside to not doing the mode in C++ is that we still have to do the hop via a preexisting PySymInt to wrap; this is currently not a big deal as conversion to SymInts only really happens when there is already another SymInt floating around. SymDispatchMode is pared down from TorchDispatchMode; there is no ancestor tracking since I don't expect people to be mixing up SymDispatchModes.
*  I made some improvements for tracing. When I invoke the SymDispatchMode handler, I would like constants to show up as constants, so they can be directly inlined into the FX graph (rather than going through a wrapping process first, and then the wrapped SymInt being used in the operation). To do this, I directly track if a PySymInt is a constant at construction time. Only wrapped PySymInts are constants.
* For convenience, PySymInts now support all magic methods that regular SymInts do. This is so that redispatch inside the SymDispatchMode can be written the idiomatic way `func(*args, **kwargs)` where func is an operator. The original names are retained for direct C++ calls.

Changes in torch.fx.experimental.proxy_tensor

* OK, so we got a new SymDispatchMode, so we define a ProxySymDispatchMode and activate it when we start tracing. This mode is currently unconditionally activated although technically we only need to activate it when doing symbolic tracing (it doesn't matter either way as there are no SymInts if you are not doing symbolic tracing).
* We delete ProxySymInt. To do this, we must now record the proxy for the SymInt some other way. Based on discussion with Chillee, it is more intuitive to him if the proxies are still recorded on the SymInt in some way. So we store them in the `__dict__` of the PySymInt, indexed by Tracer. An improvement is to make this a weak map, so that we remove all of these entries when the tracer dies. In an original version of this PR, I keyed on the mode itself, but tracer is better as it is accessible from both modes (and as you will see, we will need to fetch the map from both the ProxySymDispatchMode as well as the ProxyTorchDispatchMode.) The implementation of SymDispatchMode now simply retrieves the proxies, performs the underlying operation as well as the FX graph recording, and then records the output proxy to the PySymInt. Note that FX tracing does not work with proxies and SymInts, so we manually call `call_function` to ensure that the correct operations get recorded to the graph. This means conventional FX retracing with proxies only will not work with these graphs, but there wasn't really any reason to do this (as opposed to `make_fx` retracing) anyway. Constants are detected and converted directly into Python integers.
* SymInts can show up as arguments to tensor operations, so they must be accounted for in ProxyTorchDispatchMode as well. This is done by searching for SymInt arguments and converting them into proxies before the proxy call. This can be done more efficiently in a single `tree_map` but I'm lazy. The helper `unwrap_symint_proxy` conveniently implements the unwrapping in one place given a tracer; unfortunately it cannot be shared with SymDispatchMode as SymDispatchMode gets PySymInts, but ProxyTensorMode gets SymInts. Similarly, tensors that are returned from tensor operations can have SymInts in their shapes, which need fresh proxies allocated. To avoid leaking internal details of SymInt shape computation to the tensor operation graph, these SymInts are always given proxies derived from `x.size(dim)` call on their return tensor. We also need to do this for strides and numel but have not done so yet. Furthermore, we must avoid tracing internal SymInt calls while we run meta operations on the true operation; this is achieved by also disabling SymInt tracing on the inside of tensor tracing. This is analogous to how tensor tracing is disabled inside the implementation of tracing mode, but unfortunately we are unable to use the same mechanism (this would have been easier if the two modes could be combined somehow, and I am amenable to suggestions to try harder to achieve this.)
* Because there are no more ProxySymInts, we no longer need to do anything to unwrap SymInt. Furthermore, we do not need to reallocate ProxySymInts on class creation.
* If a bare SymInt without a Proxy is encountered, it is assumed that this must be a constant. `create_arg` handles this case. Non-constant free SymInts result in an assert error.
* The initial input handling in `dispatch_trace` involves traversing all of the input tensors, traversing over their shapes, and assigning proxies for the SymInts in shapes in the same way we handle proxies for the output tensors.

The preexisting testing is inadequate but will be better after I rebase past https://github.com/pytorch/pytorch/pull/82209

Signed-off-by: Edward Z. Yang <ezyang@fb.com>
Pull Request resolved: https://github.com/pytorch/pytorch/pull/83380
Approved by: https://github.com/samdow

---
## [vincentiusvin/tgstation](https://github.com/vincentiusvin/tgstation)@[6f2354e694...](https://github.com/vincentiusvin/tgstation/commit/6f2354e694f3412a76b383f684a0bfc85a448d8e)
#### Wednesday 2022-09-14 16:28:04 by san7890

Fixes Fucked Job Requirement Displays (#69368)

* Fixes Fucked Job Requirement Displays

Hey there,

I fucked up in #68856 (5b77361d399ba0dd992e61a16b9bbe38e8aa5a60). We weren't supposed to add another MINUTES multiplication here. I don't even remember why I did this if we are being perfectly honest with each other. Whoops.

fix: You should now no longer need thousands of hours to unlock your favorite head of staff role.

---
## [reticent-rem/syndicate-business](https://github.com/reticent-rem/syndicate-business)@[147d324215...](https://github.com/reticent-rem/syndicate-business/commit/147d32421503e1b6cd0888fd4975b0e0bd5b5cee)
#### Wednesday 2022-09-14 18:49:52 by reticent-rem

New Syndicate Business Missions

##Preface
I did my best to follow the (quality](https://github.com/endless-sky/endless-sky/wiki/QualityChecklist)/[mission](https://github.com/endless-sky/endless-sky/wiki/CreatingMissions) guidelines, but as this is my first PR, I apologize ahead of time for any weird formatting or if I've forgotten anything.

#Summary
This is the part 1 of a proposed 4 part stand-alone mission series in Syndicate space with the 2 goals of:
1. Fleshing out being an investor in the Syndicate via the player being involved with a Syndicate subsidiary business
2. Creating a purposefully inefficient way to convert credits into a cashflow stream (the investment of 1M credits generates only 300-500 credits a day, resulting in a net negative for the first 5-9 years before the player is out of the red)

I have seen comments elsewhere lamenting the lack of a way to generate passive income besides FW campaign or dominating planets, so I wanted to create another method that is a rather poor way to make money, but still something that a lazy player might use to maintain cashflow. 

If this first mission set proves uncontroversial, I plan to expand the mission set to have comparable or less efficient investments at the 10M, 100M, and 1B credit marks, and more developed branches where the player has the option to ruthlessly sacrifice the environment and human rights to maximize their returns, or take a lower financial return but getting more intangible rewards of thankful people and a noticeable improvement in worker and environmental conditions in Syndicate space. 

I also wanted the follow the [StyleGoals](https://github.com/endless-sky/endless-sky/wiki/StyleGoals) as portraying at least low level Syndicate as generally nice but with fewer scruples than most people, and also getting the player to make decisions about personal gain vs moral good.

#Quality Checklist
 - [x] Text should be as concise as possible. -- I tried my best while having lots of confirmations on the investment 
 - [x] The "yes, I want this mission" choice in a conversation should usually come first in the list (so it is the default).
 - [x] Conversations should not imply that the player is a certain gender or use gendered pronouns for the player (call them "kid" or "Captain" or <first> instead).

---
## [Project-Flexo/frameworks_base](https://github.com/Project-Flexo/frameworks_base)@[38473d14a2...](https://github.com/Project-Flexo/frameworks_base/commit/38473d14a25940520f8e91cf0edfdde0b9efdaa0)
#### Wednesday 2022-09-14 18:55:08 by Joey Huab

core: Refactor Pixel features

* Magic Eraser is wonky and hard to
  enable and all this mess isn't really worth
  the trouble so just stick to the older setup.

* Default Pixel 5 spoof for Photos and only switch
  to Pixel XL when spoof is toggled.

* We will try to bypass 2021 features and Raven
  props for non-Pixel 2021 devices as apps usage
  requires TPU.

* Remove P21 experience system feature check

---
## [Jackal-boop/tgstation](https://github.com/Jackal-boop/tgstation)@[3b2cf65d59...](https://github.com/Jackal-boop/tgstation/commit/3b2cf65d59aa5ae22876b0ebabecb564ccb912d0)
#### Wednesday 2022-09-14 20:02:40 by san7890

Rocking The Boat, er, Map Vote (#69561)

* Rocking The Boat, er, Map Vote

Hey there,

A while ago, I spooke (typo intentional) to some other people. One frustration I heard was the fact that people would sometimes sneak through map votes during the very start of a shift, during a high-paced portion, or just as a meme. People in OOC would then flood the vote, putting in any given station. However, if a vote happens 10 minutes in- and the round goes for 70 minutes and not many of the original players are around, then it's not particularly fair to those who have to play next shift on a map they bemoan.

So, we can rock the vote! If a player isn't particularly chuffed with the hand they are given, they can poll the players to see if they want to change the map as well. If rocking the vote goes through, huzzah, you get the ability to vote for the map again. If it doesn't go through: tough luck. You can rock the vote one time per shift by default, and server operators can change the amount of times you can call to rock the map vote at their discretion. Calling to rock the vote either successfully or non-successfully counts as a "call", and when that limit is exceeded: no more calls.

Does this mean that we will only rotate between two maps because pissants will keep rocking the vote until they get what they like? Maybe? I still see people bemoan getting Tram or shit the bed over IceBox, but I think enough people get sick of bread-on-butter to take the server where it need to go. If operators don't really like seeing only two maps play, they can always adjust the config to ensure it doesn't happen.

* makes the grammar grammar

it would be "Rock the Vote vote" otherwise

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[dd7636488e...](https://github.com/treckstar/yolo-octo-hipster/commit/dd7636488e28900faea30f5e14a4ed9d14aec7cb)
#### Wednesday 2022-09-14 20:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [griffin-experimental/android_kernel_motorola_msm8996](https://github.com/griffin-experimental/android_kernel_motorola_msm8996)@[2019fb6195...](https://github.com/griffin-experimental/android_kernel_motorola_msm8996/commit/2019fb6195109729caad632c3b79a97f5d5a42d9)
#### Wednesday 2022-09-14 21:11:16 by Masahiro Yamada

BACKPORT: modpost: file2alias: go back to simple devtable lookup

Commit e49ce14150c6 ("modpost: use linker section to generate table.")
was not so cool as we had expected first; it ended up with ugly section
hacks when commit dd2a3acaecd7 ("mod/file2alias: make modpost compile
on darwin again") came in.

Given a certain degree of unknowledge about the link stage of host
programs, I really want to see simple, stupid table lookup so that
this works in the same way regardless of the underlying executable
format.

Change-Id: I3d1201177711fd3e2935336d592970a90923d54f
Signed-off-by: Masahiro Yamada <yamada.masahiro@socionext.com>
Acked-by: Mathieu Malaterre <malat@debian.org>
Link: https://git.kernel.org/linus/ec91e78d378cc5d4b43805a1227d8e04e5dfa17d
Signed-off-by: Nathan Chancellor <natechancellor@gmail.com>

---
## [DangItJason/LisaPrice](https://github.com/DangItJason/LisaPrice)@[a1dfc436c6...](https://github.com/DangItJason/LisaPrice/commit/a1dfc436c6ee4170440155fd101545b2c04ac232)
#### Wednesday 2022-09-14 21:14:14 by lprice789

Update events.html

1. changed "free consultation" to first session free: "Deciding if Spiritual Coaching is right for you? Schedule a FREE session with me where we can explore your needs."
2. removed "30-minute" in "each session comes w lecture, classwork, 30-min meditation, and homework"
3. removed "spiritual" in "spiritual awakening program" heading
4. changed FROM "Sure, you can read all of the self-help books in the world, and this is a perfectly fine means to improve your life or yourself in some ways. However, to this extent it's all theory."... TO "Sure, you can read all of the self-help books in the world, and this is a perfectly fine means to learn and improve your life but unless you use the information, it's all theory."
4. removed "meaning" in "the result is living life with more meaning, joy, and acceptance.

---
## [ThakaSartu/huma](https://github.com/ThakaSartu/huma)@[5af640c0da...](https://github.com/ThakaSartu/huma/commit/5af640c0da6c13c0ce45a6c13d0f514094989a5a)
#### Wednesday 2022-09-14 21:19:50 by ThakaSartu


## ሳቲዚ ጀብዱዚ ሙና ዐሪካ ላራ ከሊላ
[Marriage Practices Among The Gidda Oromo,Northern Wollega, Ethiopia](http://www.njas.helsinki.fi/pdf-files/vol15num3/beyene.pdf)	by [Gemechu Beyene](https://www.researchgate.net/scientific-contributions/Gemechu-Beyene-36094326) & [Assefa Tolera](https://www.semanticscholar.org/author/Assefa-Tolera/114598861)
<img src="https://www.rct.uk/sites/default/files/styles/rctr-scale-1300-500/public/collection-online/e/5/1032675-1622115262.jpg?itok=gaFb1-Qp">

### Three Types of Oromo Marriage
Marriage is one of the most important rituals in Oromo culture. The custom of marriage differs in various parts of the world and every civilization produces a marriage pattern appropriate to itself (Ludlow, 1965, cited in Gemechu & Assefa., 2006). Among the Oromo society also the type, name and ceremonies differ to some degree from place to place. Generally, there are three types of marriage among the Oormo.

## Brief piece by Tigist Geme*.

Marriage is one of the most important rituals in Oromo culture. The custom of marriage differs in various parts of the world and every civilization produces a marriage pattern appropriate to itself (Ludlow, 1965, cited in Gemechu & Assefa., 2006). Among the Oromo society also the type, name and ceremonies differ to some degree from place to place. Generally, there are three types of marriage among the Oromo.

### a) Formal marriage

This type of marriage has different names in different parts of Oromia: ‘kadhaa’ (Nuro,1989), or fuudha baal-tokkee (Hussen 2000) around Arsi, ‘cida’ (Lemmesa, 2007) around Showa, and ‘Naqataa’ (Gemetchu & Assefa, 2006) in Wallaga. ‘Kadhaa’ or ‘naqataa’ is the most typical and prevalent form of marriage where the ceremony starts at the moment when marriage is first thought of and even continues after the marriage is concluded (Gemetchu & Assefa, 2006).

Traditionally, it is arranged by family and before the match takes place, they make sure that the girl’s family does not have members who are lepers, chawa-clan, crafts men such as tanner, potter etc. The groom’s parents research back seven generations to make sure that the families are not related by blood, to avoid haraamuu or incest taboo. Once this has been done, the boy’s parents then make contact with the girl’s parents through a mediator. The girl’s parents often impose conditions and the mediator will take the message to the boys parents. When the parents have reached an agreement, the man and woman get engaged (betrothed). The parent then set a wedding date and they meet all the wedding expenses (Nuro,1989, Gemechu & Assefa 2006).

### b) Informal Marriage

## i) Hawwii

According to Gemechu & Assefa (2006), this mode of marriage occurs when the boy happens to remain qeerroo (bachelor) for several reasons. Either because he is not handsome, or he is from a family of low social status, and therefore cannot pay the dowry. The boy has no consent of the family of the girl to wait long and to meet the financial and social demands of the girl’s parents. Sometimes, the girl’s mother is involved in arranging marriage of her daughter through hawwee. It is common among poor people. Youngsters resort to this kind of marriage after a lot of period of courtship that the boy approaches whom he thinks can keep secret to act on a go-between. There are places where the boy and the girl with their company can mostly wait each other. She signs an agreement saying that she was not taken against her will and she will be taken to one of the boy’s relatives until his parent prepares feast for marriage (Gemechu & Assefa2006, Nuro,1989), and that her parents are solemnly informed about her safety by elders.

## ii) Buttaa/Butii

This type of marriage takes of the following two forms. The first is when the girl has consented she is induced to be abducted. The second is accomplished by compulsion without any prior knowledge of the abduction (unlike the first form) on the part of the girl (Gemechu & Assefa, 2006).

As Gemechu and Assefa point it out in their co-authored article on the Western Macca Oromo Marriage Style, marriage by abduction is taken as option when:

- 1) a boy falls in love and she is not aware at all.

- 2) a girl’s parent is affriad that their daoughter might agree to the proposed marriage,they consprice with the would be husband to take her by force.

- 3) a girl’s parent are unwilling to agree to the proposed marriage, abduction would be resorted by boy’s family to show that they have a power to take her by force evenif her parents refused (Gemechu & Assefa, 2006; Nuro, 1989).

This informal marriage was also observable among the Salale before the government intervention and the customary law became renewed in a way committed to preserving women’s right and security.

## iii) Aseennaa

This type of marriage employs peaceful, but cunning means. According to Nuro (1989), when a girl could not get anybody who seeks her hand in marriage because she may be an ugly or her parent has an evil eye “as said to be” by the society, she chooses anyone whom she thinks would marry her. And she directly goes to his parent’s house. Gemechu & Assefa (2006) also explained that, for a women to remain unmarried into her twenties is incomprehensible, though, she must go beyond herself, called aseennaa. Therefore, when a girl is left unmarried or when her father wants to give her to some one whom she does not like, she chooses unmarried young man and runs a way to his house withought the knoweledge of the man mostly in the evening.

## iv) Conditional marriage

This type of marriage depends on the occurrence of certain incidents.

# a) Dhaala

Dhaala is a type of marriage between a women and a brother of a deceased husband or levirate (Gemechu & Assefa 2006). Among such a patrilineal community where marriage secures children to perpetuate the father’s line, it is usual for widow to be inherited by a brother of a deceased husband (Nuro,1989).

# b) Mambeeto (manbeeto)

Its conditionality is the death of one’s wife. The younger sister or relative of the late wife would be given to the widower as soon as the first wife dies (Nuro, 1989). It is known as manbeeto or mambeeto among Arsi. Among the Oromo of Tulama and Macca it is known as hirpha, literally, to ‘compensate’.

————————-

*Tigist Geme is formerly a lecturer at Addis Ababa University. This article is an excerpt from her thesis titled “Themes and Patterns of Traditional Oromo Marriage Counseling” </p>	



<img src="https://ilr.law.uiowa.edu/print/volume-99-issue-3/how-to-lie-with-rape-statistics-americas-hidden-rape-crisis/">
<img src="https://forum.12ozprophet.com/uploads/monthly_2020_04/image.png.14c87c06fc77f757887ae34cc3cd8be0.png">

<hr>

---
## [microsoft/terminal](https://github.com/microsoft/terminal)@[b4b6636b49...](https://github.com/microsoft/terminal/commit/b4b6636b4952ac8ff6a9864f641973bb49d91ce4)
#### Wednesday 2022-09-14 21:29:04 by Mårten Rånge

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
## [GerHobbelt/qiqqa-technology-tests](https://github.com/GerHobbelt/qiqqa-technology-tests)@[2f5cc53d5a...](https://github.com/GerHobbelt/qiqqa-technology-tests/commit/2f5cc53d5a930169f613373f4866f0803cade5a0)
#### Wednesday 2022-09-14 21:51:52 by Ger Hobbelt

adding Technology Test sample/test app: checking forking cleans up memory leaks.cpp() on Windows. Turns out that's a no-go (been away too long from Win32 API work; had forgotten that bit :-( ), so sample code checks behaviour what to do for a self-monitoring Windows executable.

Turns out debugging is a bastard as you're hard up against the wall to debug the *child* that's invoked via CreateProcess.
Besides, the initial sample code grabbed off the Microsoft site had the nasty "side effect" of causing infinite instantiations when patched that way, so the conclusion for the future is: better to have a separately named 'monitor' application, which keeps N child applications afloat.

Example code is still a mess, as all things that were looked at, include Counting Semaphores to help keep track of the number of child instances, etc. is all still in there.

Conclusions:

- name monitor and child apps differently, so you can have the solution open in TWO MSVC instances and debug the monitor in one, while debugging the child in another.
- do NOT use Counting Semaphores (or any other 'obvious' stuff) for keeping track of the number of children alive: when they *terminate*, through Win32API ExitProcess, TerminateProcess or hard crash, ANYTHING that's not `exit(X)`, you're toast as the application WILL NOT invoke class destructors or any handlers you can hook into when that happens, resulting in the **inability to guarantee** that any semaphore signaling will be matched by appropriate release at end-of-child-life.

  Consequently, the only viable way to make sure you can count the children alive at point of decision to kick one more alive or not is to use a system which **completes entirely** at start of child app: the way this is done here is to use a Named Mutex (all we need is a critical section, no counting done at this level, so not a semaphore but a mutex instead), which protects a critical section in all parties involved, where the OS is queried for a processes snapshot (a la `ps -ax` if you're into UNIX) and then scan the executable names for a match. Once that scan is done, the critical section ends and the Mutex is released, so we CAN guarantee proper global mutex handling now (as long as our OS process scan code doesn't *crash* ;-) )

  Then, when the count of 'live children' is high enough, the creation of yet anotheer one is skipped.
- extra lesson: Named Mutexes and Named Semaphores on Win32/64 can have a 'Global\' prefix, if you read their API docs. DO NOT DO THAT. Turns out that the verbiage at the Microsoft site is not clear enough for *me*, at least, to grok that this prefix is ONLY legal when running Terminal Services, which is Windows Server stuff and I bet you're not running research UI applications on a Windows Server license, surely!  ;-P

  That bit took another couple of hours off my life. !@#$%^

- extra lesson: DO read ('empty') your child's STDOUT pipe CONTINUOUSLY and RIGOROUSLY, when you've redirected its stdio to you, the parent/monitor. If you don't (and the original Microsoft sample code didn't because it didn't have to, as it didn't have any "debugging printf statements" in there! !@#$%^) to child process will BLOCK, waiting indefinitely for the parent to finally do some ReadFile(handle) work and empty the buffer.

  In the current example code, this has been resolved by kicking an extra *thread* alive in the *monitor* (`ThreadProc`) which' sole purpose is continuously waiting for stdout data from the child.

  I could have gone the whole hog and written asynchronous I/O code for that instead, but this was done faster, WORKS, and wasn't the main subject at time of writing.

- extra lesson: call the `FlushFileBuffers()` API on your parent/child pipes (redirected stdin + stdout): that *also* wasn't in the original sample code from MS, but is absolutely mandatory if you don't want to wonder why the Heck your collected log looks brutally truncated on app exit.

  The MS sample code got away with it, because it matched write and read buffer for buffer, so that really is an edge case of using redirected stdio.

- use OutputDebugStr to *really* printf-debug your code, because the child's printf() is, of course, *redirected*, and if you're debugging pipes it DOES NOT help when you're first trying to fill & choke the buggers only faster: you won't see nuttin', only a stuck bunch of applications. ;-)

  Use SysInternals OutputDebug monitor UI app (Debug64.exe) for this as MSVC *only* grabs OutputDebugStr output from the executable currently being debugged: that being only one half of the story underway, you will quickly understand that other means to read your debug output are mandatory here.

---
## [Caldony/lobotomy-corp13](https://github.com/Caldony/lobotomy-corp13)@[f490a226b2...](https://github.com/Caldony/lobotomy-corp13/commit/f490a226b241795abefbddeb84938af4e183b2a8)
#### Wednesday 2022-09-14 22:53:43 by Gelatelly

sassy shepherd

makes shepherd lie like the bitch he is

I HATE RUNTIMES I HATE RUNTIMES I HATERUNTIMES

use the shittiest method in existence to bypass runtimes, unfortunately I couldn't use initial() without adding some issues so fuck me I guess

updates the people and abno list

imagine using signalers

why is there a huge gap there

leftovercode that doesn't do anything

linter fix?

this is the worst fix I hate linters so much

I'm making everything worse by trying to fix it

send help

adds abno spawn signaller

I love adding signallers for meme PR

changes how the lists are used/rename a few things

SLightCamelCaseChange

clears the people_list on destroy()

this isn't much but it should avoid some problems

moves the abno spawn signal to lobotomy_corp.dm

---

