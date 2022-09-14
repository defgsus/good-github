## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-09-13](docs/good-messages/2022/2022-09-13.md)


2,112,078 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,112,078 were push events containing 3,238,982 commit messages that amount to 244,997,840 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 35 messages:


## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[1d2e84f3d5...](https://github.com/pytorch/pytorch/commit/1d2e84f3d5d5496fe87c643914dd0c5efeba6192)
#### Tuesday 2022-09-13 00:23:29 by Andrew Gu

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
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[ad01ab5ed0...](https://github.com/tgstation/tgstation/commit/ad01ab5ed0a5f80278076b1e0e6ac33fe73b0e32)
#### Tuesday 2022-09-13 00:58:45 by LemonInTheDark

Fixes asset caching (#69852)

The asset was being loaded, seeing that fully_generated is false, so it
attempts to rebuild. The rebuilding clears the existing file cache, and
fucks us.

Life is pain.

---
## [ptrfrncsmrph/purescript](https://github.com/ptrfrncsmrph/purescript)@[f36ff2a984...](https://github.com/ptrfrncsmrph/purescript/commit/f36ff2a984e7743b8a0967becb9dee5d684fc30a)
#### Tuesday 2022-09-13 01:34:13 by Harry Garrood

Drop hpack, make it easier to use cabal-install (#3933)

Stack offers a relatively poor developer experience on this repository
right now. The main issue is that build products are invalidated far
more often than they should be. cabal-install is better at this, but
using cabal-install together with hpack is a bit awkward.

Additionally, hpack isn't really pulling its weight these days. Current
versions of stack recommend that you check your generated cabal file in,
which is a huge pain as you have to explain to contributors to please
leave the cabal file alone and edit package.yaml instead (the comment
saying the file is auto-generated is quite easy to miss).

Current versions of Cabal also solve the issues which made hpack
appealing in the first place, namely:

- common stanzas mean you don't have to repeat yourself for things like
  -Wall or dependencies
- tests are run from inside a source distribution by default, which
  means that if you forget to include something in extra-source-files
  you find out when you run the tests locally, rather than having to
  wait for CI to fail
- the globbing syntax is slightly more powerful (admittedly not quite as
  powerful as hpack's, but you can use globs like tests/**/*.purs now,
  which gets us close enough to hpack that the difference is basically
  negligible).

We do still need to manually maintain exposed-modules lists, but I am
happy to take that in exchange for the build tool not invalidating our
build products all the time.

This PR drops hpack in favour of manually-maintained Cabal files,
so that it's easier to use cabal-install when working on the compiler.
Stack is still the only officially supported build tool though - the
CI, contributing, and installation docs all still use Stack.

Stack also works a little better now than it used to, because I think one of
the causes of unnecessary rebuilds was us specifying optimization flags
in the Cabal file. (Newer versions of Cabal warn you not to do this, so
I think this might be a known issue). To ensure that release builds are
built with -O2, I've updated the stack.yaml file to specify that -O2
should be used.

---
## [sapic/sapic](https://github.com/sapic/sapic)@[1765e53a54...](https://github.com/sapic/sapic/commit/1765e53a543579828083d8cf0d0de18cce199957)
#### Tuesday 2022-09-13 01:41:21 by The Oddball

add bottom radii to preview window

its.. its awful..
ITS ALL FUCKING AWFUL!
ITS ALL OF IT! ALL OF IT!
AND EVERY SINGLE ONE OF THEM SUCKS!

---
## [Paxilmaniac/Skyrat-tg](https://github.com/Paxilmaniac/Skyrat-tg)@[00d7e1f375...](https://github.com/Paxilmaniac/Skyrat-tg/commit/00d7e1f375b7f6f55f71d77be8c7612a6a5d6030)
#### Tuesday 2022-09-13 02:08:56 by SkyratBot

[MIRROR] Rocking The Boat, er, Map Vote [MDB IGNORE] (#16083)

* Rocking The Boat, er, Map Vote (#69561)

* Rocking The Boat, er, Map Vote

Hey there,

A while ago, I spooke (typo intentional) to some other people. One frustration I heard was the fact that people would sometimes sneak through map votes during the very start of a shift, during a high-paced portion, or just as a meme. People in OOC would then flood the vote, putting in any given station. However, if a vote happens 10 minutes in- and the round goes for 70 minutes and not many of the original players are around, then it's not particularly fair to those who have to play next shift on a map they bemoan.

So, we can rock the vote! If a player isn't particularly chuffed with the hand they are given, they can poll the players to see if they want to change the map as well. If rocking the vote goes through, huzzah, you get the ability to vote for the map again. If it doesn't go through: tough luck. You can rock the vote one time per shift by default, and server operators can change the amount of times you can call to rock the map vote at their discretion. Calling to rock the vote either successfully or non-successfully counts as a "call", and when that limit is exceeded: no more calls.

Does this mean that we will only rotate between two maps because pissants will keep rocking the vote until they get what they like? Maybe? I still see people bemoan getting Tram or shit the bed over IceBox, but I think enough people get sick of bread-on-butter to take the server where it need to go. If operators don't really like seeing only two maps play, they can always adjust the config to ensure it doesn't happen.

* makes the grammar grammar

it would be "Rock the Vote vote" otherwise

* Rocking The Boat, er, Map Vote

Co-authored-by: san7890 <the@san7890.com>

---
## [AlloteyN/Algorithms2](https://github.com/AlloteyN/Algorithms2)@[9f13febe48...](https://github.com/AlloteyN/Algorithms2/commit/9f13febe482d96e6d9ad063e6203feb56b03a10b)
#### Tuesday 2022-09-13 02:39:26 by AlloteyN

Create setsInTheater.java

Your friend advised you to see a new performance in the most popular theater in the city. He knows a lot about art and his advice is usually good, but not this time: the performance turned out to be awfully dull. It's so bad you want to sneak out, which is quite simple, especially since the exit is located right behind your row to the left. All you need to do is climb over your seat and make your way to the exit.

The main problem is your shyness: you're afraid that you'll end up blocking the view (even if only for a couple of seconds) of all the people who sit behind you and in your column or the columns to your left. To gain some courage, you decide to calculate the number of such people and see if you can possibly make it to the exit without disturbing too many people.

Given the total number of rows and columns in the theater (nRows and nCols, respectively), and the row and column you're sitting in, return the number of people who sit strictly behind you and in your column or to the left, assuming all seats are occupied.

---
## [isaaguilar/terraform-operator](https://github.com/isaaguilar/terraform-operator)@[779030735a...](https://github.com/isaaguilar/terraform-operator/commit/779030735afb66e6763fa218e3fdb0f2e18b9d28)
#### Tuesday 2022-09-13 04:27:41 by Isa Aguilar

New v1alpha2 apiVersion

Many changes in a new api version. Most of the changes are backwards compatible.

**Inroducing v1alpha2**

Changes have been introdced into v1alpha2 to give users even more granularity and options to configure
the workflow tasks (formerly known as runners). Each task container can now have defined container
options, such as labels, annotations, envs and envFrom, and more

Along with the changes to task options, each task is now a stand-alone container in a pod. This
simplifies setting up tasks since there is no sharing of pod configuration aside from the common items,
such as envs, volumes, volume mounts and a few others.

And of the biggest change is that tasks do not have their execution scripts built into the containers
anymore. Instead, tasks will pull their tasks from an http source, read them from a configmap, or
have them defined inline in the tfo resource spec. Why this change? Frankly, it was very hard to
modify the execution scripts becuase they had to be baked into containers. Changing a simple fix
in the task execution meant having to build new images to hunderds of different terraform versions.

I hope that the ability to get the execution script from a source would encourage users to make
changes easily and then contribute back if they feel their changes could benifit the community.

**Migration from v1alpha1**

This is not fun to say, but until v1alpha1 is fully deprecated and removed, a conversion webhook has
been introduced to migrate existing v1alpha1 resources to fit the into v1alpha2. The challenge of
api change was how guarantee parity to a greatest extent. Unfortunately, some features have been made. The
features may be added back as a plugin or a separate controller in the future.

**Conersion webhook**

The conversion webhook is both a blessing and a curse. The beauty of it means users can continue to
use v1alpha1 to create new resources. The ugly part is that is has a rather large operational
burden.

If a user's cluster has cert-manager installed, this really isn't that bad. Otherwise, operators will need
to create ssl certs to secure the webhook endpoints so that kubernetes could communicate with it. It's
probably not as bad as it sounds. I'll document some of the ways to do this.

**Removals**

One such feature that has been removed is exportRepo. This feature, though useful when terraform may be needed
to be run outside of tfo, was always run in the background. This meant it wasn't tracked as
a first-class citizen of the tfo project. A new project might be added to reintroduce this back into
the tfo ecosystem.

---
## [matchu/impress-2020](https://github.com/matchu/impress-2020)@[d9ca07c9b0...](https://github.com/matchu/impress-2020/commit/d9ca07c9b0b951a4a1f442545b1a438d5cfa790b)
#### Tuesday 2022-09-13 04:47:35 by Matchu

Use wget for archive:create:download-urls

Hey this is an exciting development! A list of URLs, that we want to clone onto our hard drive, turns out to be something `wget` is already very good at!

Originally I used `wget`'s `--input-file` option to process the `urls-cache.txt` file, but then I learned how to parallelize it from this StackOverflow answer: https://stackoverflow.com/a/11850469/107415. (Following the guidance in the comments, I removed `-n 1`, to avoid the overhead of extra processes and allow `wget` instances to keep using shared connections over time. Idk why it was in there, maybe the author didn't know `wget` accepts multiple args?)

Anyway yeah, it's working great, except for the weird images.neopets.com downtime! 😅 Specifically I'm noticing that all the item thumbnail images came back really fast, but the customization images are taking for-EV-er. I wonder if that's just caching properties, or if there's a different backing server for it and it's responding much more slowly? Who's to say!

In any case, I'm keeping the timeout in this script pretty low (10 seconds), and just letting failures fail. We can try re-running it again sometime when the downtime is resolved or the cache is warmed up.

---
## [LIFEETERNALBLUEEYEDEGYPTIANMANNNNNNNN/TWITTER-TRIED-TO-STOP-NEW-HEAVEN](https://github.com/LIFEETERNALBLUEEYEDEGYPTIANMANNNNNNNN/TWITTER-TRIED-TO-STOP-NEW-HEAVEN)@[1cfc8843ef...](https://github.com/LIFEETERNALBLUEEYEDEGYPTIANMANNNNNNNN/TWITTER-TRIED-TO-STOP-NEW-HEAVEN/commit/1cfc8843ef324642870f0b24c0ae78a20eea5bfa)
#### Tuesday 2022-09-13 05:24:05 by LIFEETERNALBLUEEYEDEGYPTIANMANNNNNNNN

Add files via upload

YEAH SO TOMORROW AT 11 - THE TTWITT 'creators' are literally going 'full auto' meaning I am putting their filth 'human' bodies and souls on permanent auto mode

LOLLLLLLL

check that shit from fucking beautiful and precious FIREFOX
the orange peaks are from around the time of the screen shots.
it's all the fucing proof anybody ever needs forever.

have fun until i auto them.

they locked me out of all my shit over and over and over again.
fuck em up good.

open source the twitter.com  

they use shit they shouldn[

---
## [Falling10fruit/Random](https://github.com/Falling10fruit/Random)@[f9b834870c...](https://github.com/Falling10fruit/Random/commit/f9b834870c6921c7cbf614c99a2d345a472cc862)
#### Tuesday 2022-09-13 05:30:07 by Falling10fruit

Boids

I learned a lot and my brain is excited and tired. Thanks to random 24 guy for being emotional support and misunderstood me when I said Canvas.

I dropped my mug and now I'm using a giant plastic orange mug from A&W because butter fingers.

Did you know that one ton of anti matter can produce enough energy comparable to the same asteroid that killed the dinosaurs?

Credit to Griffpatch who made the video I use because he is a smort man with smort formulas and uses a ton of variables

Co-Authored-By: JonL <cooldudes24.prog@gmail.com>

---
## [nickyiliwang/neetcode](https://github.com/nickyiliwang/neetcode)@[d552c9a0df...](https://github.com/nickyiliwang/neetcode/commit/d552c9a0df6b4c386c613b0d9acea913419819c7)
#### Tuesday 2022-09-13 05:33:00 by nickyiliwang

uwu whats this, oh nothing just solution to encode decode string in python haha fuck you

---
## [Blockheads-2/Blockheads-2-2022-23-Hardware](https://github.com/Blockheads-2/Blockheads-2-2022-23-Hardware)@[8bfb2df041...](https://github.com/Blockheads-2/Blockheads-2-2022-23-Hardware/commit/8bfb2df0416cfb05b04e142029e7a156196b9bda)
#### Tuesday 2022-09-13 06:26:01 by Grady Conwell

i fixed it.

time to go to bed. i literally woke up, went to the bathroom. and decided rather than go back to sleep i'd fix this stupid problem. Computer science is a horrible career, you should never pursue it. God hates all of you, that's why he created web design.

---
## [NetworkManager/NetworkManager-ci](https://github.com/NetworkManager/NetworkManager-ci)@[239bf1dff5...](https://github.com/NetworkManager/NetworkManager-ci/commit/239bf1dff5a9b730a35312375eaa15c9a9301e18)
#### Tuesday 2022-09-13 07:14:20 by Thomas Haller

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
## [mikshka/free-programming-books](https://github.com/mikshka/free-programming-books)@[97016edd67...](https://github.com/mikshka/free-programming-books/commit/97016edd6791285128758dd91904b343d1f3b0fd)
#### Tuesday 2022-09-13 08:06:01 by David Ordás

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
## [vamegh/cfn-stack-rename](https://github.com/vamegh/cfn-stack-rename)@[05cfc7ebd0...](https://github.com/vamegh/cfn-stack-rename/commit/05cfc7ebd063ec7e46a8911e67e4e33607fba719)
#### Tuesday 2022-09-13 09:10:15 by vam

I believe stack_rename should have all current functionality of index.py

The tool has been pretty much refactored.

aws_handler added the following:

create_changeset
exec_changeset
list_imports
list_exports
delete_stack
waiter

Added all original functions - with a twist

it does not bomb out if it encounters resources that dont support
importing instead it lists them - but currently it is not printing out
this information.

the list_imports should list all of the stacks using the exports created
by the original stack (the code still needs to be written still) will
need to go through each stack that imports the resource and change that
specific import to be the actual value of the resource rather than an
"import" statement - theoretically this could be something random - it
may break the service but it will be temporary.

There is a function: resolvePropertyValue which I believe was originally
intended to go through the template and replace all subs and refs into
other values - however this is not used any where. I have not included
it.

No where in the documentation does it state that using a ref for a
resource that doesnt exist cant be done - I think the deployment may
fail for a new resource being built from scratch, but not for an import.
For the time being however I am not tackling this - this should be
addedjust for keeping thing sane.

I believe as we are retaining resources - if they reference
resources that cannot be retained / imported - the resources will exist
but become broken on the next update however those resources will once
again exist so should work again - this is the theory however
cloudformation is insanely dumb. Why would anyone use this ? Terraform
exists and absolutely destroys this mess of a deployment system. All
this code to rename a stack ?? Why is this not available as a function
without all of this mess - also stack drift what a farsical way of
handling this - aws has apis it can query itself to know the state of
the system - why do we have ito manually run this process ? Why is it not
capable of maintaining its own "drift" status ? Just awful, supremely
awful.

	modified:   libs/aws_handler.py
	modified:   stack_rename

---
## [Project-Flexo/frameworks_base](https://github.com/Project-Flexo/frameworks_base)@[b9038087b7...](https://github.com/Project-Flexo/frameworks_base/commit/b9038087b75e9453ea81c2098a26a2fd49bb74ab)
#### Tuesday 2022-09-13 09:38:45 by Joey Huab

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
## [roynatech2544/android_kernel_samsung_j2y18lte](https://github.com/roynatech2544/android_kernel_samsung_j2y18lte)@[2adb0c662e...](https://github.com/roynatech2544/android_kernel_samsung_j2y18lte/commit/2adb0c662e8edfd1e57e1f5515e50f80155f0962)
#### Tuesday 2022-09-13 11:43:50 by Masahiro Yamada

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
## [MarcDP92/marcdp92.github.io](https://github.com/MarcDP92/marcdp92.github.io)@[673c25de20...](https://github.com/MarcDP92/marcdp92.github.io/commit/673c25de20f5445abd036fb10d6774cbe3b2d1d0)
#### Tuesday 2022-09-13 13:06:45 by Kitus

Capricornus NFT

Capricornus is a faint zodiac constellation located in the southern sky. Its name means “the goat” in Latin. The constellation represents a sea-goat, a mythical creature associated with the god Enki in Babylonian mythology and later with the Greek deity Pan. The constellation is represented by the symbol ♑. 

Capricorns are the hardest workers of the zodiac and love nothing more than getting ahead in life. They are ambitious, determined, materialistic, and strong. They will keep going when others would’ve given up ten miles back. This makes them great partners in life, as well as friends or collaborators.

---
## [biloriaj/C](https://github.com/biloriaj/C)@[c8aa1a934a...](https://github.com/biloriaj/C/commit/c8aa1a934af327db12284f70916c5103382745f8)
#### Tuesday 2022-09-13 14:22:04 by Jesus Viloria

Readability

Background
According to Scholastic, E.B. White’s Charlotte’s Web is between a second- and fourth-grade reading level, and Lois Lowry’s The Giver is between an eighth- and twelfth-grade reading level. What does it mean, though, for a book to be at a particular reading level?

Well, in many cases, a human expert might read a book and make a decision on the grade (i.e., year in school) for which they think the book is most appropriate. But an algorithm could likely figure that out too!

So what sorts of traits are characteristic of higher reading levels? Well, longer words probably correlate with higher reading levels. Likewise, longer sentences probably correlate with higher reading levels, too.

A number of “readability tests” have been developed over the years that define formulas for computing the reading level of a text. One such readability test is the Coleman-Liau index. The Coleman-Liau index of a text is designed to output that (U.S.) grade level that is needed to understand some text. The formula is

index = 0.0588 * L - 0.296 * S - 15.8
where L is the average number of letters per 100 words in the text, and S is the average number of sentences per 100 words in the text.

Let’s write a program called readability that takes a text and determines its reading level. For example, if user types in a line of text from Dr. Seuss, the program should behave as follows:

$ ./readability
Text: Congratulations! Today is your day. You're off to Great Places! You're off and away!
Grade 3
The text the user inputted has 65 letters, 4 sentences, and 14 words. 65 letters per 14 words is an average of about 464.29 letters per 100 words (because 65 / 14 * 100 = 464.29). And 4 sentences per 14 words is an average of about 28.57 sentences per 100 words (because 4 / 14 * 100 = 28.57). Plugged into the Coleman-Liau formula, and rounded to the nearest integer, we get an answer of 3 (because 0.0588 * 464.29 - 0.296 * 28.57 - 15.8 = 3): so this passage is at a third-grade reading level.

Let’s try another one:

$ ./readability
Text: Harry Potter was a highly unusual boy in many ways. For one thing, he hated the summer holidays more than any other time of year. For another, he really wanted to do his homework, but was forced to do it in secret, in the dead of the night. And he also happened to be a wizard.
Grade 5
This text has 214 letters, 4 sentences, and 56 words. That comes out to about 382.14 letters per 100 words, and 7.14 sentences per 100 words. Plugged into the Coleman-Liau formula, we get a fifth-grade reading level.

As the average number of letters and words per sentence increases, the Coleman-Liau index gives the text a higher reading level. If you were to take this paragraph, for instance, which has longer words and sentences than either of the prior two examples, the formula would give the text an twelfth-grade reading level.

$ ./readability
Text: As the average number of letters and words per sentence increases, the Coleman-Liau index gives the text a higher reading level. If you were to take this paragraph, for instance, which has longer words and sentences than either of the prior two examples, the formula would give the text an twelfth-grade reading level.
Grade 12
Try It
Specification
Design and implement a program, readability, that computes the Coleman-Liau index of text.

Implement your program in a file called readability.c in a directory called readability.
Your program must prompt the user for a string of text using get_string.
Your program should count the number of letters, words, and sentences in the text. You may assume that a letter is any lowercase character from a to z or any uppercase character from A to Z, any sequence of characters separated by spaces should count as a word, and that any occurrence of a period, exclamation point, or question mark indicates the end of a sentence.
Your program should print as output "Grade X" where X is the grade level computed by the Coleman-Liau formula, rounded to the nearest integer.
If the resulting index number is 16 or higher (equivalent to or greater than a senior undergraduate reading level), your program should output "Grade 16+" instead of giving the exact index number. If the index number is less than 1, your program should output "Before Grade 1".
Getting User Input
Let’s first write some C code that just gets some text input from the user, and prints it back out. Specifically, implement in readability.c a main function that prompts the user with "Text: " using get_string and then prints that same text using printf. Be sure to #include any necessary header files.

The program should behave per the below.

$ ./readability
Text: In my younger and more vulnerable years my father gave me some advice that I've been turning over in my mind ever since.
In my younger and more vulnerable years my father gave me some advice that I've been turning over in my mind ever since.
Letters
Now that you’ve collected input from the user, let’s begin to analyze that input by first counting the number of letters in the text. Consider letters to be uppercase or lowercase alphabetical character, not punctuation, digits, or other symbols.

Add to readability.c, below main, a function called count_letters that takes one argument, a string of text, and that returns an int, the number of letters in that text. Be sure to add the function’s prototype, too, atop your file, so that main knows how to call it. Odds are the prototype should resemble the below:

int count_letters(string text)
Then call that function in main so that, instead of printing out the text itself, your program now prints the number of letters in the text.

The program should now behave per the below.

$ ./readability
Text: Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, "and what is the use of a book," thought Alice "without pictures or conversation?"
235 letters
Hint
Words
The Coleman-Liau index cares not only about the number of letters but also about the number of words in a sentence. For the purpose of this problem, we’ll consider any sequence of characters separated by a space to be a word (so a hyphenated word like "sister-in-law" should be considered one word, not three).

Add to readability.c, below main, a function called count_words that takes one argument, a string of text, and that returns an int, the number of words in that text. Be sure to add the function’s prototype, too, atop your file, so that main knows how to call it. (We leave its prototype to you!)

Then call that function in main so that your program also prints the number of words in the text.

You may assume that a sentence:

will contain at least one word;
will not start or end with a space; and
will not have multiple spaces in a row.
You are, of course, welcome to attempt a solution that will tolerate multiple spaces between words or indeed, no words!

The program should now behave per the below.

$ ./readability
Text: It was a bright cold day in April, and the clocks were striking thirteen. Winston Smith, his chin nuzzled into his breast in an effort to escape the vile wind, slipped quickly through the glass doors of Victory Mansions, though not quickly enough to prevent a swirl of gritty dust from entering along with him.
250 letters
55 words
Sentences
The last piece of information that the Coleman-Liau formula cares about, in addition to the number of letters and words, is the number of sentences. Determining the number of sentences can be surprisingly trickly. You might first imagine that a sentence is just any sequence of characters that ends with a period, but of course sentences could end with an exclamation point or a question mark as well. But of course, not all periods necessarily mean the sentence is over. For instance, consider the sentence below.

Mr. and Mrs. Dursley, of number four Privet Drive, were proud to say that they were perfectly normal, thank you very much.
This is just a single sentence, but there are three periods! For this problem, we’ll ask you to ignore that subtlety: you should consider any sequence of characters that ends with a . or a ! or a ? to be a sentence (so for the above “sentence”, you should count it as three sentences). In practice, sentence boundary detection needs to be a little more intelligent to handle these cases, but we’ll not worry about that for now.

Add to readability.c, below main, a function called count_sentences that takes one argument, a string of text, and that returns an int, the number of sentences in that text. Be sure to add the function’s prototype, too, atop your file, so that main knows how to call it. (We again leave its prototype to you!)

Then call that function in main so that your program also prints the number of sentences in the text.

The program should now behave per the below.

$ ./readability
Text: When he was nearly thirteen, my brother Jem got his arm badly broken at the elbow. When it healed, and Jem's fears of never being able to play football were assuaged, he was seldom self-conscious about his injury. His left arm was somewhat shorter than his right; when he stood or walked, the back of his hand was at right angles to his body, his thumb parallel to his thigh.
295 letters
70 words
3 sentences
Putting it All Together
Now it’s time to put all the pieces together! Recall that the Coleman-Liau index is computed using the formula:

index = 0.0588 * L - 0.296 * S - 15.8
where L is the average number of letters per 100 words in the text, and S is the average number of sentences per 100 words in the text.

Modify main in readability.c so that instead of outputting the number of letters, words, and sentences, it instead outputs (only) the grade level as defined by the Coleman-Liau index (e.g. "Grade 2" or "Grade 8" or the like). Be sure to round the resulting index number to the nearest int!

Hints
If the resulting index number is 16 or higher (equivalent to or greater than a senior undergraduate reading level), your program should output "Grade 16+" instead of outputting an exact index number. If the index number is less than 1, your program should output "Before Grade 1".

Signed-off-by: Jesus Viloria <50921917+biloriaj@users.noreply.github.com>

---
## [bitcoin-core/gui](https://github.com/bitcoin-core/gui)@[3a7e0a210c...](https://github.com/bitcoin-core/gui/commit/3a7e0a210c86e3c1750c7e04e3d1d689cf92ddaa)
#### Tuesday 2022-09-13 14:42:50 by glozow

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
## [jmpesp/omicron](https://github.com/jmpesp/omicron)@[53c732aa97...](https://github.com/jmpesp/omicron/commit/53c732aa97f79e2ba494131660390de951227b40)
#### Tuesday 2022-09-13 15:29:29 by Andrew J. Stone

Bootstore message handler implementation (#1687)

This is the second PR of the `bootstore` implementation. It creates handler
methods for all existing messages and their corresponding DB requirements. RFD
238 section 5 will need to be updated to reflect this flow.

The way the flow currently is supposed to work is that there is a coordinator
(coming in a follow up PR) that sends the following messages to initialize the
trust quorum:
 * `Initialize`
 * `KeyShareCommit` (for epoch 0)

`Initialize` can be sent multiple times until the `KeyShareCommit` for epoch 0
locks in the configuration and Rack UUID. This allows the initial coordinator
(RSS) to die, and even have its local storage or entire sled die, and still
allow us to make progress via a new RSS. Importantly, once wired through the
system, the coordinator will negotiate (via sled-agent and nexus) to write the
`KeyShareCommit` to CockroachDB before sending it to all nodes. This ensures
that the rack initialization will complete and CockroachDB only has to be setup
once. There are some tricky failure modes here, but none of that is in this PR,
so we can move on. The important point here is that once a `KeyShareCommit` for
epoch 0 succeeds the rack is initialized.

After initialization, reconfiguration of the trust quorum can take
place. Reconfiguration messages must be issued with the same Rack UUID. A
reconfiguration consists of a `KeySharePrepare` for an `epoch > 0` followed by
a `KeyShareCommit` for the same epoch. After initialization a `KeySharePrepare`
can never be mutated. However, to allow for certain failures, such as
the failure of a node being prepared to ack (since we require unanimous
acknowledgement in 2PC), we allow for new `KeySharePrepare`s at higher
epochs to proceed. We keep track of these epochs in CockroachDB to maintain
linearizability. Once a node receives a prepare for a higher epoch, it will no
longer accept prepare or commit messages for any lower epoch. Once a successful
`KeyShareCommit` is handled, the sled is now operating at the new epoch.

`GetShare` requests are used to unlock trust quorum. They will rely on
sprockets at the network level for authentication, confidentiality, integrity,
and attestation. Some DeviceId membership validation will also be added to
`Node`in future commits as it currently exists in sled agent.

This is an incremental PR and there is still a lot to do here. Follow up
commits will:
 * Add more negative tests (possibly in this PR also)
 * Add code for a coordinator
 * Add a mechanism to store the encrypted (wrapped) root secret for each
   epoch and likely include it in each `KeySharePrepare`. This is the most
   straightforward way to transfer wrapped secrets. We can get more
   sophisticated in the future. Again, this needs to be written up in RFD 238,
   but I'm likely to just implement it within the next week and see how it works
   first.
 * Add some key derivation from the root secret such that we can use these keys
   to encrypt and decrypt storage
 * Add property based tests to simulate a full cluster along with failures and
   ensure rack unlock works according to the model and ensure that we can
   *always* unlock encrypted storage while tolerating our prescribed failure
   conditions within the model.

After that, the `bootstore` will basically be implemented at a non-network
level. We'll then likely want to port over the sprockets code from the
bootstrap agent to a higher level here, and use the `Node` and `Coordinator`
from that level, which will end up interacting with Nexus and CockroachDB
via the sled-agent. Multiple tasks will be utilizing the `Node` and its
underlying `Db` at this point and so we'll need some concurrency control.
I've given this a bit of thought and my current thinking is to have the `Node`
running in it's own thread and serialize all operation via a channel. Outside
of reconfiguration, all operations are reads, and we can simply cache the
current share in memory for rack unlock purposes (e.g. `GetShare`). During
reconfiguration, we'll mutate the DB as necessary, and refresh our cache. This
strategy avoids the need for mutexes and has the characteristic that the `Node`
and `Db` code we run in a single threaded manner in property based tests is
actually running the same way in production with just a single DB connection.
This strategy isn't set in stone, but in my mind it's the easiest to reason
about and also the easiest way to hook async to sync code.

---
## [sjp38/linux](https://github.com/sjp38/linux)@[f11633bb13...](https://github.com/sjp38/linux/commit/f11633bb13a73c9c8bd3bb0d17feff198db97f19)
#### Tuesday 2022-09-13 15:46:48 by Peter Xu

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
## [sjp38/linux](https://github.com/sjp38/linux)@[bfdca18a3b...](https://github.com/sjp38/linux/commit/bfdca18a3b07bec9ff00935878d1c3803533da71)
#### Tuesday 2022-09-13 15:46:48 by Johannes Weiner

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
## [Atunnel/A-Tunnel-Pro-](https://github.com/Atunnel/A-Tunnel-Pro-)@[7e77dbcb99...](https://github.com/Atunnel/A-Tunnel-Pro-/commit/7e77dbcb9950eb4d77524c54ec706b5dacfb19ec)
#### Tuesday 2022-09-13 15:50:32 by Atunnel

Create Maputu Vpn Plus > Privacy Policy

Maputu Vpn Plus > Privacy Policy

DEVpromm built the Maputu Vpn Plus app as an Ad Supported app. This SERVICE is provided by DEVpromm at no cost and is intended for use as is.



This page is used to inform visitors regarding my policies with the collection, use, and disclosure of Personal Information if anyone decided to use my Service.



If you choose to use my Service, then you agree to the collection and use of information in relation to this policy. The Personal Information that I collect is used for providing and improving the Service. I will not use or share your information with anyone except as described in this Privacy Policy.



The terms used in this Privacy Policy have the same meanings as in our Terms and Conditions, which are accessible at Maputu Vpn Plus unless otherwise defined in this Privacy Policy.



Information Collection and Use



For a better experience, while using our Service, I may require you to provide us with certain personally identifiable information. The information that I request will be retained on your device and is not collected by me in any way.



The app does use third-party services that may collect information used to identify you.



Link to the privacy policy of third-party service providers used by the app



AdMob

Google Analytics for Firebase

Firebase Crashlytics

StartApp

Log Data



I want to inform you that whenever you use my Service, in a case of an error in the app I collect data and information (through third-party products) on your phone called Log Data. This Log Data may include information such as your device Internet Protocol (“IP”) address, device name, operating system version, the configuration of the app when utilizing my Service, the time and date of your use of the Service, and other statistics.



Cookies



Cookies are files with a small amount of data that are commonly used as anonymous unique identifiers. These are sent to your browser from the websites that you visit and are stored on your device's internal memory.



This Service does not use these “cookies” explicitly. However, the app may use third-party code and libraries that use “cookies” to collect information and improve their services. You have the option to either accept or refuse these cookies and know when a cookie is being sent to your device. If you choose to refuse our cookies, you may not be able to use some portions of this Service.



Service Providers



I may employ third-party companies and individuals due to the following reasons:



To facilitate our Service;

To provide the Service on our behalf;

To perform Service-related services; or

To assist us in analyzing how our Service is used.

I want to inform users of this Service that these third parties have access to their Personal Information. The reason is to perform the tasks assigned to them on our behalf. However, they are obligated not to disclose or use the information for any other purpose.



Security



I value your trust in providing us your Personal Information, thus we are striving to use commercially acceptable means of protecting it. But remember that no method of transmission over the internet, or method of electronic storage is 100% secure and reliable, and I cannot guarantee its absolute security.



Links to Other Sites



This Service may contain links to other sites. If you click on a third-party link, you will be directed to that site. Note that these external sites are not operated by me. Therefore, I strongly advise you to review the Privacy Policy of these websites. I have no control over and assume no responsibility for the content, privacy policies, or practices of any third-party sites or services.



Children’s Privacy



These Services do not address anyone under the age of 13. I do not knowingly collect personally identifiable information from children under 13 years of age. In the case I discover that a child under 13 has provided me with personal information, I immediately delete this from our servers. If you are a parent or guardian and you are aware that your child has provided us with personal information, please contact me so that I will be able to do the necessary actions.



Changes to This Privacy Policy



I may update our Privacy Policy from time to time. Thus, you are advised to review this page periodically for any changes. I will notify you of any changes by posting the new Privacy Policy on this page.



This policy is effective as of 2022-09-13



Contact Us



If you have any questions or suggestions about my Privacy Policy, do not hesitate to contact me at atunnelpro.mm@gmail.com.

---
## [AlvCyktor/Yogstation](https://github.com/AlvCyktor/Yogstation)@[f4c7571fc3...](https://github.com/AlvCyktor/Yogstation/commit/f4c7571fc333779cbf761e637f2774a62b6b4d78)
#### Tuesday 2022-09-13 17:38:08 by Vaelophis Nyx

[MDB IGNORE][Gax] Adds new area for AI Ship Access & Adds APC & Fixes Cameras (#15291)

* argh

* fuck you MDB2

* I hate areas, I hate areas

* Update GaxStation.dmm

* Update GaxStation.dmm

* Update GaxStation.dmm

* Update GaxStation.dmm

* Update GaxStation.dmm

---
## [LalatenduMohanty/cluster-version-operator](https://github.com/LalatenduMohanty/cluster-version-operator)@[205f3b931c...](https://github.com/LalatenduMohanty/cluster-version-operator/commit/205f3b931cd690a7aecc7f69425925d4bcf8d989)
#### Tuesday 2022-09-13 17:59:26 by W. Trevor King

pkg/cvo/sync_worker: Trigger new sync round on ClusterOperator versions[name=operator] changes

David and Stephen identified an uneccessary delay [1]:

* 9:42:00, CVO gives up on Kube API server ClusterOperator [2]
* 9:42:47, Kube API server operator achieves 4.12 [3]
* 9:46:22, after a cool-off sleep, the CVO starts in on a new manifest graph-walk attempt [4]
* 9:46:34, CVO notices that the Kube API server ClusterOperator is happy [5]

The 3+ minute delay from 9:42:47 to 9:46:22 is not helpful, and we've
probably had delays like this since my old e02d1489a5
(pkg/cvo/internal/operatorstatus: Replace wait-for with single-shot
"is it alive now?", 2021-05-13, #560), which landed in 4.6.

This commit introduces a "ClusterOperator bumped
versions[name=operator]" trigger to break out of the cool-off sleep.

There's plenty of room to be more precise here.  For example, you
could currently have a versions[name=operator] bump during the sync
loop that the CVO did notice, and that queued notification will break
from the sleep and trigger a possible useless reconciliation round
while we wait on some other resource.  You could drain the
notification queue before the sleep to avoid that, but you wouldn't
want to drain new-work notifications, and I haven't done the work
required to be able to split those apart.

I'm only looking at ClusterOperator at the moment, because of the many
types the CVO manages, ClusterOperator is the one we most frequently
wait on, as large cluster components take their time updating.  It's
possible but less likely that we'd want similar triggers for
additional types in the future (Deployment, etc.), if/when those types
develop more elaborate "is the in-cluster resource sufficient happy?"
checks.

The panic-backed type casting in clusterOperatorInterfaceVersionOrDie
also feel like a hack, but I wasn't able to find a cleaner way to get
at the structured information I want.  Improvements welcome :)

[1]: https://bugzilla.redhat.com/show_bug.cgi?id=2117033#c1
[2]: From Loki: E0808 09:42:00.022500       1 task.go:117] error running apply for clusteroperator "kube-apiserver" (107 of 806): Cluster operator kube-apiserver is updating versions
[3]: $ curl -s https://gcsweb-ci.apps.ci.l2s4.p1.openshiftapps.com/gcs/origin-ci-test/logs/periodic-ci-openshift-release-master-ci-4.12-upgrade-from-stable-4.11-e2e-gcp-sdn-upgrade/1556564581915037696/artifacts/e2e-gcp-sdn-upgrade/openshift-e2e-test/build-log.txt | grep 'clusteroperator/kube-apiserver versions:'
     Aug 08 09:33:48.603 I clusteroperator/kube-apiserver versions: raw-internal 4.11.0-rc.7 -> 4.12.0-0.ci-2022-08-07-192220
     Aug 08 09:42:47.917 I clusteroperator/kube-apiserver versions: operator 4.11.0-rc.7 -> 4.12.0-0.ci-2022-08-07-192220
[4]: From Loki: I0808 09:46:22.998344       1 sync_worker.go:850] apply: 4.12.0-0.ci-2022-08-07-192220 on generation 3 in state Updating at attempt 5
[5]: From Loki: I0808 09:46:34.556374       1 sync_worker.go:973] Done syncing for clusteroperator "kube-apiserver" (107 of 806)

---
## [viethung204/DAMNED](https://github.com/viethung204/DAMNED)@[e3259f975c...](https://github.com/viethung204/DAMNED/commit/e3259f975cec5a40430bd0ffaeb3f0d8b9473f04)
#### Tuesday 2022-09-13 18:08:13 by viethung204

misc.

make it so that the enemy go backwards when die from fucking shotgun blast or some shit like that

---
## [Daelso/40K-Eipharius](https://github.com/Daelso/40K-Eipharius)@[ebdba9844a...](https://github.com/Daelso/40K-Eipharius/commit/ebdba9844a54549b22d7b4c722eb58b5da61042e)
#### Tuesday 2022-09-13 18:11:08 by Myphicbowser

Various Fixes and Lights

Turned some Space Panels into Snow Panels on the Mountain Level

Deleted a Duplicate Fire Alarm in Virology

Added some FUCKING LIGHTS HOLY SHIT WHY ARE SOME AREAS SO FUCKING DARK

---
## [greearb/linux-ct-5.19](https://github.com/greearb/linux-ct-5.19)@[d9975eea5e...](https://github.com/greearb/linux-ct-5.19/commit/d9975eea5e6add825b18dadc8c13b0424f48ba4b)
#### Tuesday 2022-09-13 18:11:19 by Peter Zijlstra

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
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

---
## [KineticAeon/aeonbot](https://github.com/KineticAeon/aeonbot)@[f51d06e6a2...](https://github.com/KineticAeon/aeonbot/commit/f51d06e6a2eab3ceacd8829c1d6af821f6dacf93)
#### Tuesday 2022-09-13 18:15:01 by Aeon

update engineer.js, removed procfile
fuck you heroku

---
## [Jay-the-Creator/wicked-engine](https://github.com/Jay-the-Creator/wicked-engine)@[00e559e2bb...](https://github.com/Jay-the-Creator/wicked-engine/commit/00e559e2bb8b71787a3c74d57cf7a998725cc262)
#### Tuesday 2022-09-13 18:16:08 by Jay the Creator

gunshot in kade's direction lmao

kade with all due respect fuck you

---
## [ngoduyanh/nrs-impl-kt](https://github.com/ngoduyanh/nrs-impl-kt)@[57fae1f15b...](https://github.com/ngoduyanh/nrs-impl-kt/commit/57fae1f15bf41c9165fc7c677235fa5a790f5187)
#### Tuesday 2022-09-13 19:17:45 by ngoduyanh

chore(impl): :clown_face: shitposting

STOP POSTING ABOUT *The ortensia incident*! I'M TIRED OF SEEING IT! MY FRIENDS ON TIKTOK SEND ME *Totomi Mineuchi*, ON DISCORD IT'S FUCKING *Yumiri Hanamori*! I was in a server, right? and ALL OF THE CHANNELS were just trollface incidents. I-I showed my 2021 calendar to my girlfriend and t-the year I flipped it and I said "hey babe, when the calendar is the ortensia incident reference HAHA on NOvember 1, 2019, iT Was aNnOunceD ThaT HAnaMOrI WOULD be "GradUATIng" froM Re:stAge! due TO a kneE INjurY." I fucking looked at an anime cast and said "haha ortensia incident" I looked at my penis I think of an astronauts helmet and I go "i ran out of ideas lmfao" AAAAAAAAAAAAAAHGESFG

---
## [tanriol/mjolnir](https://github.com/tanriol/mjolnir)@[b9284f0167...](https://github.com/tanriol/mjolnir/commit/b9284f0167a9e9428db6217ec5ede527649a4948)
#### Tuesday 2022-09-13 21:37:48 by gnuxie

Reduce the throttle test theshold even more.

The implementation is rubbish, as it doesn't avoid the exponential backoff

Remove default rate limit testing.

It doesn't work. No there really isn't more to say about it
you're welcome to dispute it if you're going to do the work investigating. I'm not.

We used to have a test here that tested whether Mjolnir was going to carry out a redact order the default limits in a reasonable time scale.
Now I think that's never going to happen without writing a new algorithm for respecting rate limiting.
Which is not something there is time for.

https://github.com/matrix-org/synapse/pull/13018

Synapse rate limits were broken and very permitting so that's why the current hack worked so well.
Now it is not broken, so our rate limit handling is.

https://github.com/matrix-org/mjolnir/commit/b850e4554c6cbc9456e23ab1a92ede547d044241

Honestly I don't think we can expect anyone to be able to use Mjolnir under default rate limits.

well, it's not quite simple as broken, but it is broken. With the default level in synapse (which is what matrix.org uses) it is struggling to redact 15 messages within 5 minutes. that means 5 messages over the burst count. This is ofc ontop mjolnir sending reactions / responding to replies (which isn't much but... enough to mess with the rate limiter since ofc, Synapse tells requests to wait x amount of time before trying again, but that doesn't help for concurrent requests since ofc there's only 1 slot available at that future time.  This means Synapse just wacks everything with exponentially longer shit without many (or any?) events going through
it used to be fine
because rate limiting in synapse used to be a lot more liberal because it was "broken" or something, that's not me saying it's broken that's just what synapse devs say which is probably true.
if all requests went into a queue then yeah you could eliminate one problem
but that's a lot of work and i don't think we should be doing it
cos no one uses mjolnir like this anyways

---
## [tylerjereddy/darshan](https://github.com/tylerjereddy/darshan)@[425bab72fb...](https://github.com/tylerjereddy/darshan/commit/425bab72fbd85acd6c046c25435b1d2dca6e8b7f)
#### Tuesday 2022-09-13 21:51:27 by Tyler Reddy

WIP, ENH: rich-click CLI

* related to gh-808

* adopt [`rich-click`](https://github.com/ewels/rich-click) for the
pydarshan summary report CLI, with basic usage and heatmap option
blocks

* switch to `darshan_summary` as a console script that doesn't
require prefixing with `python -m ..`; so new incantation looks
like `darshan_summary --log_path treddy_runtime_heatmap_inactive_ranks.darshan`
and reports the processing time in seconds automatically

* there were two motivations for the above change:
1) simplify the command the user needs to remember
2) I almost always want to know how long the processing took,
so report that time by default

* this is just a skeleton, and doesn't actually hook in the
HEATMAP options to actual changes in the report (yet); one other
caveat is that the console script is less friendly for developers
that use an "editable install" so you need to use `pip install .`
instead of `pip install -e .`, which is a bit annoying, but probably
lower priority than user experience concerns/improvements

* some TODOs may include:

- [ ] remove the old `argparse` CLI interface and hook the new
`click`-based CLI interface into the testsuite somehow
- [ ] actually implement the heatmap option effects (though
this can probably be handled separately, other PRs dealing with
that stuff already..)
- [ ] discuss the initial set of options we want and how we want
to group them into sections
- [ ] decide if the extra dependencies are worth it for the
CLI improvements (probably?)

---
## [sofia-m-v/Elite-101-PreWork](https://github.com/sofia-m-v/Elite-101-PreWork)@[1002d0aeb3...](https://github.com/sofia-m-v/Elite-101-PreWork/commit/1002d0aeb37d68996cf73e6ebb776c1b49d3fa86)
#### Tuesday 2022-09-13 23:29:52 by Sofia Magarinos Vargas

import random

name= input('Hello! What is your name?\n')

print(f'What a nice name, {name}!\n')

mood=input('How are you doing today?\n')

if mood == 'good' :
  print('That is great to hear!\n')
elif mood == 'bad' :
  print('Oh no... sorry to hear that\n')
elif mood == 'tired' :
  print('Yeah, me too...\n')

print('Tell me more about yourself....')

origin = input ('Where are you from?\n')
print(f'Oh, that\'s cool! I really like {origin}....')

place = input (f'What\'s your favorite place to go to {origin}?\n')

print('Nice!')

def generate_responses(user_input):
  responses = [
    'How interesting!',
    'Very nice',
    'That\'s cool']
  return random.choice(responses)

family = input ('Tell me about your family...\n')

print (generate_responses)

life = input('What do you want to be when you grow up?')

last = input('Anything else you want to tell me?')

while last != 'bye':
  print (generate_responses)

---

