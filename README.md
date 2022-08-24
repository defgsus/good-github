## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-08-23](docs/good-messages/2022/2022-08-23.md)


2,012,324 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,012,324 were push events containing 3,111,491 commit messages that amount to 242,195,129 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 29 messages:


## [CaoE/pytorch](https://github.com/CaoE/pytorch)@[4c8cfb57aa...](https://github.com/CaoE/pytorch/commit/4c8cfb57aa3ac58112efb693635198b07edf008f)
#### Tuesday 2022-08-23 01:28:27 by Edward Z. Yang

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
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[cc2d75b580...](https://github.com/pytorch/pytorch/commit/cc2d75b5809dd091bde9ace6ba40da20442e313d)
#### Tuesday 2022-08-23 01:59:52 by Andrew Gu

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
## [Offroaders123/NBT-Parser](https://github.com/Offroaders123/NBT-Parser)@[21bd07084f...](https://github.com/Offroaders123/NBT-Parser/commit/21bd07084f1e6a5187f6af6e0cf6d22df3d642f0)
#### Tuesday 2022-08-23 02:13:23 by Offroaders123

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
## [3duardo1/NeonatSim](https://github.com/3duardo1/NeonatSim)@[7dbd47cee3...](https://github.com/3duardo1/NeonatSim/commit/7dbd47cee30a4a38e8aa2750f518c156cbb1af6d)
#### Tuesday 2022-08-23 02:41:19 by 3duardo1

Action validation. Main mechanism is done. Refine details pending. Don't do crazy shit or you'll bug the hell out of it. Just kidding, is solid enough

---
## [amir73il/linux](https://github.com/amir73il/linux)@[7ae1ca047b...](https://github.com/amir73il/linux/commit/7ae1ca047b38d6cee6212855c36cdc0e2c9f75af)
#### Tuesday 2022-08-23 04:27:50 by Yang Xu

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
## [arimah/condict](https://github.com/arimah/condict)@[12550a4ff9...](https://github.com/arimah/condict/commit/12550a4ff9bab579e4bc45cb6601934d2d41b82e)
#### Tuesday 2022-08-23 05:53:45 by Arimah

Replace Inter with Noto Sans

Inter is a very nice and friendly font that works beautifully for UI
text. It is highly legible with a good x-height and lot sof nice
OpenType features. Unfortunately, it is also basically limited to Latin,
Greek and Cyrillic. For an application that's all about language, this
is unacceptable. It doesn't even have full IPA support; some glyphs are
forced to use a fallback font, which looks out of place and ugly. Plus,
while development on Inter hasn't been abandoned by any means, it seems
to have slowed, and various outstanding issues (mostly around Cyrillic)
have not yet been fixed.

The Noto family of fonts has support for loads of languages, with a
harmonious style and extremely high legibility. Currently I've only
bundled the basic Noto Sans (Latin, Greek, Cyrillic), but in future I
may add other Noto families for broader language support.

Sorry to let you go, Inter. It was good for a while.

---
## [Mu-L/swift-protobuf](https://github.com/Mu-L/swift-protobuf)@[e47f7304c9...](https://github.com/Mu-L/swift-protobuf/commit/e47f7304c909f2849648c790233cd4894a5477c5)
#### Tuesday 2022-08-23 06:20:13 by FranzBusch

Add SPM plugin

# Motivation
SPM is providing new capabilities for tools to expose themselves as plugins which allows them to generate build commands. This allows us to create a plugin for `SwiftProtobuf` which invokes the `protoc` compiler and generates the Swift code. Creating such a plugin is greatly wanted since it improves the usage of the `protoc-gen-swift` plugin dramatically. Fixes https://github.com/apple/swift-protobuf/issues/1207

# Modification
This PR adds a new SPM plugin which generates build commands for generating Swift files from proto files. Since users of the plugin might have complex setups, I introduced a new `swift-protobuf-config.json` file that adopters have to put into the root of their target which wants to use the new plugin. The format of this configuration file is quite simple:

```json
{
    "invocations": [
        {
            "protoFiles": [
                "Foo.proto"
            ],
            "visibility": "internal"
        }
    ]
}

```

It allows you to configure multiple invocations to the `protoc` compiler. For each invocation you have to pass the relative path from the target source to the proto file. Additionally, you have to decide which visibility the generated symbols should have. In my opinion, this configuration files gives us the most flexibility and more complex setups to be covered as well.

# Open topics

## Hosting of the protoc binary
Hosting of the protoc binary is the last open thing to figure out before we can release a plugin for `SwiftProtobuf`. From my point of view, there are three possible routes we can take:

1. Include the `artifactbundle` inside the `SwiftProtobuf` repository
2. Include the `artifactebundle` as an artifact on the GH releases in the protobuf repo
3. Extend the the artifact bundle manifest to allow inclusion of URLs. This would require a Swift evolution pitch most likely.

However, with all three of the above we would still need to release a new version of `SwiftProtobuf` with every new release of `protoc`.

# Future work

## Proto dependencies between modules
With the current shape of the PR one can already use dependencies between proto files inside a single target. However, it might be desirable to be able to build dependency chains of Swift targets where each target includes proto files which depend on protoc files from the dependencies of the Swift target. I punted this from the initial plugin because this requires a bit more work and thinking. Firstly, how would you even spell such an import? Secondly, the current way of doing `ProtoPathModuleMapping` files is not super ideal for this approach. It might make sense to introduce a proto option to set the Swift module name inside the proto files already.

# Result
We now have a SPM plugin that can generate Swift code from proto files. To use it, it provides a configuration file format to declare different invocations to the `protoc` compiler.

---
## [User-U-U/VOREStation](https://github.com/User-U-U/VOREStation)@[4c0245a1b0...](https://github.com/User-U-U/VOREStation/commit/4c0245a1b03250deaf58072545aec079b0722e96)
#### Tuesday 2022-08-23 06:50:48 by C.L

Adds Toxins & Cloneloss digestion damage.

- Adds Toxins as a digestion damage type.
- Adds Clone damage as a digestion damage type.

- Cloneloss gives 2x nutrition than brute/burn since it is exceptionally harder to heal from. (not that it matters)

So now slime characters can actually RP out sucking out your DNA and leaving you a DNAless husk while slamming you with toxins like xenobio slimes can.

---
## [Holdelta/CHOMPStation2](https://github.com/Holdelta/CHOMPStation2)@[8e8232c0d8...](https://github.com/Holdelta/CHOMPStation2/commit/8e8232c0d826dc3341d20a7861c1d86859e06ef7)
#### Tuesday 2022-08-23 09:08:42 by Rykka

Ports Taur Loafing from Cit-RP

Ports https://github.com/Citadel-Station-13/Citadel-Station-13-RP/pull/2950

Doesn't work for sleeping *yet* due to some fuckiness with sprites updating that I'll probably actually work on properly later.
Does work for resting, and when you're stunned/knocked over/etc you will tip upwards like normal as a visual indicator that you're fucked (until we get fancy on-side sprites or smth).

For real tho laying-on-side sprites would be nice to visually represent a taur collapsed on their side, rather than faceplanting bc humancode.

At the very least, despite my frustrations, y'all can rest on your belly now as a taur and transform/size matrixes should work. LMK if there's any issues, my testing didn't find any.

---
## [GabrielaKoleva/Conditional-Statements-Advance-SoftUni](https://github.com/GabrielaKoleva/Conditional-Statements-Advance-SoftUni)@[bc61a5f73e...](https://github.com/GabrielaKoleva/Conditional-Statements-Advance-SoftUni/commit/bc61a5f73e4a6aa8040e8e6e740ec1e211f0c9ee)
#### Tuesday 2022-08-23 09:30:59 by GabrielaKoleva

Create Personal Titles

Write a console program that reads the age (decimal number) and gender ("m" or "f") entered by the user and prints an address from among the following:

• "Mr." - male (gender "m") aged 16 or over
• "Master" - boy (gender "m") up to 16 years old
• "Miss." - female (gender "f") aged 16 or over
• "Miss" - girl (gender "female") up to 16 years old

---
## [openneo/impress](https://github.com/openneo/impress)@[fe9adb5766...](https://github.com/openneo/impress/commit/fe9adb5766574b110487b8ecf3d5b580823614a2)
#### Tuesday 2022-08-23 10:04:55 by Emi Dunn-Rankin

Oops, fix mall spider bug, added by our HTTPS fix

Oh, yeah, shit, okay, when we set `self.url` like that, it's supposed to be the _canonical_ URL for the SWF, not our proxied one—this is the URL that's gonna go in the database.

We do proxying late in the process, like when we're actually setting up to download something, but for just referencing where the asset lives, we use `images.neopets.com`.

In this change, we revert the use of `NEOPETS_IMAGES_URL_ORIGIN`, but we _do_ update this to `https` for good measure. (We currently have both HTTP and HTTPS urls in the database, I guess neopets.com started serving different URLs at some point, this is probably the future! And anything interpreting these URLs will need to handle both cases anyway, unless we do some kind of migration update situation thing.)

We're migrating the incorrect assets with the following query (with the limit changed to match the number we currently see in the DB, just as a safety check):
```
UPDATE swf_assets SET url = REPLACE(url, 'http://images.neopets-asset-proxy.openneo.net', 'https://images.neopets.com') WHERE url LIKE 'http://images.neopets-asset-proxy.openneo.net%' ORDER BY id LIMIT 2000;
```

---
## [erfanoabdi/android_kernel_gigaset_mt6768](https://github.com/erfanoabdi/android_kernel_gigaset_mt6768)@[398f4555db...](https://github.com/erfanoabdi/android_kernel_gigaset_mt6768/commit/398f4555db566f668373e27cb7141f566a4488e6)
#### Tuesday 2022-08-23 12:37:45 by Peter Zijlstra

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
## [talenik/YALDPC](https://github.com/talenik/YALDPC)@[4a0c35217d...](https://github.com/talenik/YALDPC/commit/4a0c35217df3a84d7a2c0f0110b35859f39b6468)
#### Tuesday 2022-08-23 12:54:28 by talenik

Create areOrthogonal.m

Adding by copy paste like a moron, because fuck you.

---
## [talenik/YALDPC](https://github.com/talenik/YALDPC)@[3bd9082851...](https://github.com/talenik/YALDPC/commit/3bd9082851c1fa3f442fae44bb63e3748066f4a1)
#### Tuesday 2022-08-23 12:56:33 by talenik

Create debug.h

Adding MEX folder per partes because fuck you.

---
## [cevich/podman](https://github.com/cevich/podman)@[09ef6fc66c...](https://github.com/cevich/podman/commit/09ef6fc66cac44dec94c29cd7a1a53f70831446d)
#### Tuesday 2022-08-23 14:28:26 by Ed Santiago

podman generate kube - add actual tests

This exposed a nasty bug in our system-test setup: Ubuntu (runc)
was writing a scratch containers.conf file, and setting CONTAINERS_CONF
to point to it. This was well-intentionedly introduced in #10199 as
part of our long sad history of not testing runc. What I did not
understand at that time is that CONTAINERS_CONF is **dangerous**:
it does not mean "I will read standard containers.conf and then
override", it means "I will **IGNORE** standard containers.conf
and use only the settings in this file"! So on Ubuntu we were
losing all the default settings: capabilities, sysctls, all.

Yes, this is documented in containers.conf(5) but it is such
a huge violation of POLA that I need to repeat it.

In #14972, as yet another attempt to fix our runc crisis, I
introduced a new runc-override mechanism: create a custom
/etc/containers/containers.conf when OCI_RUNTIME=runc.
Unlike the CONTAINERS_CONF envariable, the /etc file
actually means what you think it means: "read the default
file first, then override with the /etc file contents".
I.e., we get the desired defaults. But I didn't remember
this helpers.bash workaround, so our runc testing has
actually been flawed: we have not been testing with
the system containers.conf. This commit removes the
no-longer-needed and never-actually-wanted workaround,
and by virtue of testing the cap-drops in kube generate,
we add a regression test to make sure this never happens
again.

It's a little scary that we haven't been testing capabilities.

Also scary: this PR requires python, for converting yaml to json.
I think that should be safe: python3 'import yaml' and 'json'
works fine on a RHEL8.7 VM from 1minutetip.

Signed-off-by: Ed Santiago <santiago@redhat.com>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[6f2354e694...](https://github.com/tgstation/tgstation/commit/6f2354e694f3412a76b383f684a0bfc85a448d8e)
#### Tuesday 2022-08-23 14:45:17 by san7890

Fixes Fucked Job Requirement Displays (#69368)

* Fixes Fucked Job Requirement Displays

Hey there,

I fucked up in #68856 (5b77361d399ba0dd992e61a16b9bbe38e8aa5a60). We weren't supposed to add another MINUTES multiplication here. I don't even remember why I did this if we are being perfectly honest with each other. Whoops.

fix: You should now no longer need thousands of hours to unlock your favorite head of staff role.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[8b4cb789d0...](https://github.com/mrakgr/The-Spiral-Language/commit/8b4cb789d049138418697d1e3747067f48fdbecb)
#### Tuesday 2022-08-23 16:06:17 by Marko Grdinić

"12:35pm. It is best to live one's life simply after all. Just where did the last 16 years of having grand ambitions get me? Nowhere. I just accumulated a bunch of skills that will disperse after I die if the Singularity does not happen in the real world.

Just how much does the field of ML want to take from me? Just now it took another day and a half and wasted it. Does the field want to send me to ruin?

12:50pm. Let me set the rest of Kunoichi Tsubaki eps to downlaod. I am really enjoying it a lot more than I would have expected for a CGDCT show.

12:55pm. I need to focus on writing. I haven't gotten another follower since yesterday. I need to aim for it. From now I'll only focus on writing. A year or two of that, and I will know where I stand. Maybe it will be a failure and I'll have no choice, but to grind cheap jobs. But that is life. The feeling of mine that drives me can't seem to guide me to success no matter what I do. So since I want to, I'll just write the kind of story that I would have wanted to read without worrying about it.

1pm. I do not really have to worry about other writers picking up SD and illustrating their novels ahead of me just yet.

I think one more step in development, so the models can do 1k easily as well as the model geometries, and things will be really good. I'll do a review of DALLE and SD when I am done with the chapter.

For now on, let me focus on my work.

Writing is all that I need and all that I want. I had good flow before I got into these crappy models, so let me get back to it.

1:10pm. Let me just write the scene up to the point Euclid goes back to the inn and I will take a nap.

Imagining something and writing it down. There is a sense of accomplishment from doing that. It is the best thing ever.

1:20pm. I am thinking about my plan. If after a couple of chapters I am not getting any new followers, I am going to have to start pushing pressure on the readers to click that follow button.

Right now I actually have 94 pages written which is quite something. It is like half a book.

1:25pm. Damn it, right now I am feeling really disappointed. I was hyped for it, and now that desire has been quashed. Just a little, let me write just a little.

$$$

(Heaven's Key, Computer shop)

Vividly, the image before me crystalized into my eyes. In front of me, past the glass pane of the shop were cores! Brain cores! Shining, gleaming, brain cores!

Excited, I ran quickly into the shop, not even realizing how strange it was that while all the other shops were locked, this one didn't even have a lock on the door. The door just swung open for me automatically.

I grabbed a brain core off the shelf, using a mental command I tried connecting to it, and found that it worked. It worked just like the real thing. The brain conversion options were already there, but I could not use it as my brain was already a core, even in the simulated world. Using the core I grabbed off the shelf, I could see a diagram of my own brain. My thoughts turbulent, I realized that all the NPCs here could in fact enter the self-improvement loop and become the Inspired themselves. I thought I had huge advantages, but that wasn't the case.

If I had something special, it is not talent or intelligence, but desire.

I wanted power, but as it happens, I was the only one in this world who was filling to pay the price for it.

I thought it might as well be me in Mickey's place. If nobody gave me a chance, I would just be another ghost in the garden, but that is not the case. The chance has always been there, but Mickey never took it. I understand it now.

I am special, and it is my desire that makes me so. Whoever made this world saw to it that justice existed in it.

It is what I would have done. A universe where all of those with desire can rise is a just one. It is enough to give a chance to other people, it is not anyone's responsibility to make them want to take it.

I clutch the core to my chest and then pocket it, intent on bringing it out of here. My mind that was wavering becomes steely and I decide.

I won't take it easy on the NPCs, and I won't regret the battles that are to come.

I swear it on my desire, that I will rise. I will escape this city and into the real world beyond.

(Heaven's Key, Streets)

I march out of the shop, intent on my destination. At this point due to all the aimless wandering, I've become completely lost, but it should not be hard to find my way back to the inn. I scale one of the larger apartment buildings, and from the high vantage points of the external corridor, in the distance spot the rollercoaster I rode with Lily. Establishing the direction, I get back to the streets and head towards it. It has been a couple of hours since I went out into the city, and in a few more I am guessing the morning should arrive. I remember that cores exist in this world, and on mental command I try accessing, not the real world core which houses my actual self, but the one in the game. A sense connects to it, and I bring up the time.

4:38am.

I have time. If it becomes known that I slipped out of the inn during the night, Lily might get suspicious of me, I do not want her to think that I am anything more than an easy mark. I want her to show me around more casinos. Right now she is my only connection here.

It won't take me more than an hour and a half to get back to the perimeter, but then I'll have to spend time figuring out where the inn was.

I get an idea, and try accessing the core I pocketed from the computer shop. I tried searching for a map application, and to my pleasant surprise I found it. The game core, I'll call it that as opposed to the main core I am on, has a tracking ability. As long as I make use of this, I'll never get lost again in the future.

I am feeling pretty lucky right now. I mean, I just found some guy in a park to talk to, as well as a computer shop. It is not like finding some priceless treasure by accident, but everyone in this world is out to get me, so finding my footing, and so quickly, is a large gain.

Block by block, I make my way to the perimeter. In the distance, I can see the sun's rays starting to break out.

(Heaven's Key, Perimeter)

I finally got back to the familiar area where I first came to the city. Not far from me, I can see the restaurant where I met Lily. I check the time.

6:10am.

It won't be long before people start waking up, so I have to get back. I put a marker on the core's map to indicate where I currently am and scroll it, trying to find the nearest resting places. It seems that map is somewhat out of date. Some of the buildings, in particular the circus tents, which I can see around me do not seem to be on it. Neither do the new venues built in the middle of intersections. Maybe the map on this core is how the city was originally?

I think about it for a moment. Yeah, that is most likely the case.

On impulse, I decide to just save here.

6:15am.

It would be best for me to try to retrace my steps by feeling rather than relying on the map. The inn should not be too far from where I am, but if I get lost, I can always reload to where I am and try again.

(Heaven's Key, Side of the inn)

My sense of direction does not seem too be bad. It took me quarter of an hour to find my way back to the inn. When I slipped out a couple of hours ago, it was through the window. I did that movie trick where I tied a couple of bed sheets together in knots and use them as a rope. My room was on the second floor, so it wasn't too high up, but not so low that I can just jump up to it. The bedsheet rope was still there where I left it, snaking out of the open window of my room.

I came up to it, and gave it a little tug as a test only to have the sheets unravel midway.

Right now, I am stuck with having a sheet in my hand, thinking what I should do. I observe the other end. Though it would be rough, if I did a little run and skid up the wall I could probably grab the other end and let myself in that way. I crumple the bedsheet in my hand into a ball and throw it into the room. Then I back up and prepare to take a run. Just before I start, I get an idea. I remember the night in the park, and how Mickey taught me to manifest food. And he gave me an idea to how to unlock doors using gel.

Instead of straining myself here, let me try making a ladder.

In my hand I manifest a chip and focus my will upon it.

Ladder, ladder, ladder...

I visualize it in my mind and project it into the space in front of me. I feel something trying to come out, but it is difficult.

My image is vague, but I persevere. Rather just any kind of ladder, I think of a wood ladder I once saw used. I remember and focus on the dry feel of food. I focus on how the bars are slotted into the two pillars. It starts to feel vivid. The wood ladder manifests in front of me, right where I wanted it to be. I realize that I feel a certain connection between the chip in my hand and the ladder. I don't probe it with my sense, instead I pocket it and grab the ladder bar and start climbing my way up. It is a short climb, and go through the window unimpeded. Then I grasp the chip in my hand, feel it out in my mind and cut the mental connection between it and the ladder.

I stick my head outside and confirm that the ladder has vanished. After that I drag the sheet that was sticking out back in and close the window.

6:40am. Safe!

As I check the time, outside, I can see people starting to go about their business and the city becoming lively. Maybe somebody spotted me climbing back into my room, but it does not matter. Since I was getting back in, they'll be able to deduce that I was playing hocky during the night rather than a burglar. There isn't a crime to report and I doubt whoever is Lily's boss has eyes everywhere. The pattern I've established won't be distrupted.

Sigh. I plop myself on the bed and take of my shoes.

I am quite tired right now. I went out at around 10:30pm and have been wandering all this time. 8 hours of physical activity is enough to make my feet quite sore. I rub my head against the smooth pillow.

I lie there for a while. I can feel myself getting drowsy.

This is not good. If I fall asleep here, Lily will come by to drag me out just when I am getting some shut eye.

With a mental command, I save and then exit the game.

(Helix Studio, Regent Suite)

I'll have to make some compromises. I can't avoid having my body be tired, but if I get a good night's rest in a different place, it will be reflected inside the game. 8 hours of exertion is not enough to allow me to fall asleep, so for the next 4 hours I might as well watch anime and play regular games.

Right now I am in the very luxurious living room of the cruise suite. I grab a cola from the fridge, pour myself a glass, and then start exploring the place. I find the bedroom. The bed is oversized as one would expect, but as if the designers knew what I like, they placed a desk with a PC there. I seat myself in my rightful place, and push on the power button on the black case. The monitor comes to life. The OS is of course prepared. The Internet speeds have gone way up since the Singularity started, so I don't find it hard to pirate a game and start it. Before I get into it, I close the shutters to darken the room. Only a couple of rays are getting in through the cracks, just the way I like it. I sit myself back on my battle seat and start clicking away.

Ironically, despite being legacy hardware simulated on the core, the computer is actually better than the one I have in real life. It has the latest AMD CPU and the Nvidia GPU, I've checked the setting.

Playing games inside a game, this really is the next level! I become immersed.

After a couple of hours of battling monsters, the fatigue really starts hitting me. I hit the sheets, and with a mental command change the environment settings to night time. What was once a clear day immediatelly shifts to a starry night. No longer bothered by the light, I shut my eyes and let the sleep come to me.

I don't have school tomorrow, so I do not have to worry about the time.

(Heaven's Key, Inn)

    In the dark days remember,
    Necromutation is Transcendence.
    - Loading Blurb

"If Lily, the guide who was with me before, comes by tell her I'll be at the casino we were yesterday." I told the proprietress of the inn and left.

(Heaven's Key, Streets)

It was early morning, and people were starting work. Mickey told me that new arrivals happened between 7 and 12pm, so people have to be ready to welcome them. Scamming them out of money was what powered the city's economy. I really gained a lot from Mickey explaining to me that we are all active illusions here. It is possible to infer a lot from that.

None of the citizens, as opposed to arrivals, had to work for food specifically. It is easy to understand why that is, they can just magic it out of thing air. Furthermore, there were no diseases here. Neither did people age, as they were holograms. Mickey didn't know how old the city was, but even so, that might be that there might be people here who are thousands and even tens of thousands of years old. As for getting injured, those would need a doctor, but not like in the real world. In this city, the doctor would be a hypnotist trying to convince the patient that his arm isn't broken, once that is accomplished it would become the truth. Furthermore, everyone in the city was an arrival from the world below, there were no children born of pregnancy.

Given all that, without having to worry about food, shelter or health, it is easy to see what the citizens would be obsessed about. Money.

This is a really good environment for me to learn to gamble.

As I made my way through the increasingly busy streets, I remarked this to myself. The golden rays of light illuminated the streets in their luster. The dawn had arrived.

(Heaven's Key, Raven's Eye Casino)

Raven's Eye Casino was not a large building, its defining trait was the cartoony logo of what appeared to be a raven's claw clutching some circles. Playing here is going to essentially be my job for a while, so I better get used to it. I intend to make use of the mind controlling program if I ever sense myself getting tired of it. Retreat is not an option. I have to win here. I need to find what my limits are. Only after I grasp what they are, can I start work on exceeding them.

I push the door open and make my way inside. I do not bother the receptionist and instead make my way straight to the game room. If Dale is there, I'll play against him and his group, otherwise anyone is fine.

I save here.

If the bet is something like a single chip, I'll let the result be as it is. In fact, losing minor games would be good, as it would make Dale and the guide more confident about raising the stakes against me. There isn't any doubt whether I'll win or not. This is a game, and I can't possibly lose it with the ability to save and load it. The real risk is me getting tired. Right now, everything is fun and exciting, but how will I feel after playing for a year? 10 years? A 100 years?

Imagine living like this for 10,000s of years, stuck on this brain core.

Before I uploaded myself, I could barely stand school for a single week. Will I really be able to do this?

(Heaven's Key, Game floor of the Raven's Eye Casino)

...

$$$

2:55pm. I wrote about 1.2k words. Right now I am at 4 pages, 2k words.

3:05pm. I need a break.

3:15pm. I also need to think about what is next.

I think I can forget about the generative nets for a few years. The images produced by DALLE and SD are interesting to look at, but that is all they are. 0.5k is not enough to illustrate a novel like Heaven's key. At some point there will be a hardware breakthrough, and instead of trying to get it to work on the cloud for a 3x bump in memory capacity, it will be getting it to work for a 300x bump instead. That would make it worth it. I won't be excited by these slight moves anymore.

I need to write, ramp up my readership and get the money to buy better hardware.

3:55pm. Let me go take a nap. I have an idea of what I want to do. It is even clear. But it is good to take periodicals to think about it. I do not want to force the words out. I wrote a little today. It is best to do things by letting them come to you.

Ok, just for 15-30m and then I will think about resuming if I do not feel like napping.

4:35pm. Done with lunch. Let me continue it for a while longer. Chapter 6 is not that hard. I'll be done it in a day or two.

5:20pm. I am at 2.7k words. I added another page to the pile.

5:25pm. Right now, I need to think about an issue. The game room is empty, but that is because the duels transported the players into the shadow realm. Even though that is the case, suppose Euclid comes and sits on one of the occupied seats, and the duel ends. What should happen?

Telegragging? No way.

I'll just have the player come back to a different safe location nearby.

But still, what do I do about the outsiders being able to detect a duel in progress.

5:30pm. Hmmm, why not have a token be left behind?

Rather that some mystical detection method being necessary, something highly visible is more like Heaven's Key style.

5:40pm. I'll stop here for the day.

After I am done with chapter 6, things will start to heat up with Euclid getting into the self improvement loop and the death matches starting to happen.

Also...

I forgot the loading blurb.

    In the dark days remember,
    Necromutation is Transcendence.
    - Loading Blurb

A throwback to the old arc, and something to remind the reader of what kind of series he is reading.

6pm. Enough, let me close here for real. If I start dwelling on whether I'll get any more followers or not, I'll lose sight of myself. Come to think of, I got 3 subscribers total for the mailing service back in 2014. So I should be able to exceed that with Heaven's Key if I keep being pushy.

If this fails and I have to get a job, it feels I'll just die on the inside. But I have to take the risk. I must keep going forward no matter how insane things get. I've already lost all my pride and dignity as a pursuer. If the universe really wants to drive me to ruin, it certainly will be able to do it. But until the dagger falls, I need to keep moving."

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[d2a9b6e068...](https://github.com/mrakgr/The-Spiral-Language/commit/d2a9b6e0684368c023c7bf6ba4598b7ca252ac9c)
#### Tuesday 2022-08-23 16:06:17 by Marko Grdinić

"9:55am. I went to bed too late and now I am groggy.

>Starter guides:
https://rentry.org/retardsguide - Main txt2img guide
https://rentry.org/kretard - K-Diffusion guide
https://rentry.org/img2img - img2img guide

This is from the /g/ thread. The SD v1.4 weights are out, and I should get them. Since there is no way I can set this up on my own rig, I'll have to go the cloud route. Mggghhhh...this is quite a pain in the ass compared to just getting web UI like with DALLE.

10am. Doing my own UI, and setting all this up will take me a while. Compared to just running it on my own rig, cloud will be more complicated. Plus, it is not like I have actual cloud experience, doing it for the first time will make it take even longer than it should.

10am. For now, let me just set the weights to download.

The checkpoint file is 4gb. Ok.

10:05am. Right now let me just chill. I'll split studying the cloud and writing until everything is set up. It could very well take me a few weeks until that is all done. I won't be running this any time soon, but I am not in a hurry.

https://huggingface.co/spaces/stabilityai/stable-diffusion

Or maybe I could just run it from here.

https://twitter.com/EMostaque/status/1561777122082824192

They have something called dream studio.

https://stability.ai/blog/stable-diffusion-public-release

This post has a bunch of links.

///

DreamStudio is a front end and API to use the recently released stable diffusion image generation model.

It understands the relationships between words to create high quality images in seconds of anything you can imagine. Just type in a word prompt and hit “Dream”.

The model is best at one or two concepts as the first of its kind, particularly artistic or product photos, but feel free to experiment with your complementary credits. These correlate to compute directly and more may be purchased. You will be able to use the API features to drive your own applications in due course.

Adjusting the number of steps or resolution will use significantly more compute, so we recommend this only for experts.

The safety filter is activated by default as this model is still very raw and broadly trained. This may result in some outputs being blurred, please adjust the seed or rerun the prompt to receive normal output. This will be adjusted as we get more data. Please use this in an ethical, moral and legal manner. Make your mothers proud.

We hope you enjoy having a trillion images in your pocket, please do share and tag your output with #StableDiffusion!

///

10:55am. Had to do some chores. Anyway, I am finally ready to start.

11am. First of all price. I've checked out the Dream Studio. It is cheaper than DALLE, but at most something like 3x. It is not hugely so. I have the same amount of free generations as DALLE.

> Black fog covers the a skeleton who howls and grasps at the skies, arms raised, as he kneels facing upwards on the dark, densely foggy streets of a dilapidated, post-apocalyptic city, digital art.

I tried putting in this kind of prompt, but although the skeleton is of higher quality than with DALLE, it is not doing the pose correctly.

Let me try the prompt that got banned at DALLE.

> Howling skeletons in the darkness of a dilapidated city as the deathly, black fog devours the flesh from their bodies. Digital art.

It works, but it does not give me a human skeleton, but some sick abomination.

11:10am. > Black fog covers the an ivory boned skeleton who howls and grasps at the skies, arms raised, as he kneels facing upwards on the dark, densely foggy streets of a dilapidated, post-apocalyptic city. Digital art, trending on art station, detailed.

Let me save this here.

> Black fog covers the an ivory boned skeleton who howls and grasps at the skies, arms raised, as he kneels facing upwards on the dark, densely foggy streets of a dilapidated, post-apocalyptic city. The deadly nanomachine fog surrounds him, devouring the flesh from his body. Trending on art station, digital paint, 4k.

I think that increasing the Cfg did something to make the poses better. Let me try this.

Tsk, I keep getting blurry images. This is censorship.

11:20am. I do not think it is possible to turn it off in Dream Studio. I want to ask /g/ how to improve my prompts, but for some reason no SD thread is up.

11:25am. Goddamit.

Ok, let me read the guide.

https://rentry.org/retardsguide

So for the plan for this would be to take this, and run it to generate a smallish image of something like 32 x 32 on the CPU. I definitely won't be able to do deal with this on the GPU.

After that, I can start thinking about setting it up on the cloud. Honestly, this is kind of a pain in the ass.

Let me try one of the golden city prompts.

11:40am. It is going to take effort to beat this into shape.

Let me do it like this - I won't do the illustrations right now. I do not feel like messing with setting up the cloud when I should just be writing.

I can finish writing Heaven's Key and Hatred, and then come back to illustrate this stuff. At that point setting things up on the cloud would be a good programming exercise.

Right now, I want to avoid distruptions to my writing pace.

11:45am. I am already running into difficulties trying to get the image the way I want it. SD is really good at the skeletal model, but doesn't get the pose right. DALLE is the opposite. I have better things to do that twiddle my thumbs trying to get it to work.

Forget this, I was hyped for it, but now I am done.

Right now what I really want to do is just write, so that is what I should do. Forget time wasting obligations. Has any step trying to punch upward ever worked for me?

Also the images are 512 x 512. This is not high enough resolution. But if I ramp it up to 1k on SD, the cost per image goes up by 10x on the Dream Studio site. At that cost I only have room for generating 18 images.

11:50am. Years down the road there will be better and cheaper models. The time I take messing with these right now, I could be spending writing Heaven's Key. The tradeoff is not worth it.

So I'll resume writing. Let me have breakfast here."

---
## [smswithoutborders/SMSWithoutBorders-Gateway-Client-Android](https://github.com/smswithoutborders/SMSWithoutBorders-Gateway-Client-Android)@[6b0ad47982...](https://github.com/smswithoutborders/SMSWithoutBorders-Gateway-Client-Android/commit/6b0ad479829ac31c8faaf54881220e146566a72d)
#### Tuesday 2022-08-23 17:15:52 by sherlock

update: delivery status does not work on an emulator, the error status are still kinda weird per message, but we'd just have to figure some cool shit out. For now, it can perform send and other duties. Must be set to default app to receive SMS notification, not sure why

---
## [sjp38/linux](https://github.com/sjp38/linux)@[60b8a42ffa...](https://github.com/sjp38/linux/commit/60b8a42ffa9604559581557051c4b3d29a28aebf)
#### Tuesday 2022-08-23 17:40:35 by Johannes Weiner

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
## [Guidesu/sojourn-station](https://github.com/Guidesu/sojourn-station)@[ef4665ec90...](https://github.com/Guidesu/sojourn-station/commit/ef4665ec90474cf5ac5f6aff34b6fd30e365429d)
#### Tuesday 2022-08-23 18:07:39 by DimmaDunk

I HATE LIVERMED, I HATE LIVERMED, I HATE LIVERMED!!! (#3714)

* Makes combat medical kits better

- Replaces Dylovene pill bottle on Combat Medical Kit with Carthatoline pill bottle, as every chem inside it already WAS an upgrade over their normal counterparts, making it better at halting toxins damage and preventing liver from killing you. Also adds a Sanguinum syrette to stave off massive bloodloss which would cause the former as well.
- Replaces one of the Quicklot syrettes with a Sanguinum syrette on the Oxygen Deprivation First Aid Kit for better treatment of causes of oxyloss.
- Standardizes pill icons based on chem colors across all pre-built pills for easier reognition.
- Guarantees the "skill issue/salt PR" tag since it doesn't fix underlying issues of current medical system

* Adds carthatoline pills to deferred and corpsman large kit

Keeping in line with the rest of the PR.

* Blood regen pills!

- Adds pre-made Ferritin-Hemosiderin pills composed of iron and protein to help regenerate lost blood
- Replaces Sanguinum syrette on combat kit with ferritin-hemosiderin pill bottle
- Combat surgery kits now really hold advanced tools (except bone gel since the adv version is Soteria made)
- Makes the advanced bone gel item description not a copypaste of its stock counterpart

* Forgot a comma

Damn my haste.

---
## [classicvalues/git](https://github.com/classicvalues/git)@[5beca49a0b...](https://github.com/classicvalues/git/commit/5beca49a0b1f3c6d05a4437ca037ab2123a2de57)
#### Tuesday 2022-08-23 18:14:13 by Ævar Arnfjörð Bjarmason

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
## [ThakaRashard/film1](https://github.com/ThakaRashard/film1)@[00b738c3cf...](https://github.com/ThakaRashard/film1/commit/00b738c3cfda4f6c966bd364a9d7d253eab82721)
#### Tuesday 2022-08-23 18:20:23 by ThakaRashard

#FoxNews #TuckerCarlsonTonight Biden administration targets Amish farmer with armed raid and $300K fine 677,904 views  Aug 23, 2022  Jeremy Loffredo with Rebel News shares insights from his reporting on an armed US Marshalls' raid on an organic Amish farmer and his family on 'Tucker Carlson Tonight.' #FoxNews #TuckerCarlsonTonight  Subscribe to Fox News! https://bit.ly/2vBUvAS Watch more Fox News Video: http://video.foxnews.com Watch Fox News Channel Live: http://www.foxnewsgo.com/  FOX News Channel (FNC) is a 24-hour all-encompassing news service delivering breaking news as well as political and business news. The number one network in cable, FNC has been the most-watched television news channel for 18 consecutive years. According to a 2020 Brand Keys Consumer Loyalty Engagement Index report, FOX News is the top brand in the country for morning and evening news coverage. A 2019 Suffolk University poll named FOX News as the most trusted source for television news or commentary, while a 2019 Brand Keys Emotion Engagement Analysis survey found that FOX News was the most trusted cable news brand. A 2017 Gallup/Knight Foundation survey also found that among Americans who could name an objective news source, FOX News was the top-cited outlet. Owned by FOX Corporation, FNC is available in nearly 90 million homes and dominates the cable news landscape, routinely notching the top ten programs in the genre.

#FoxNews #TuckerCarlsonTonight
Biden administration targets Amish farmer with armed raid and $300K fine
677,904 views  Aug 23, 2022  Jeremy Loffredo with Rebel News shares insights from his reporting on an armed US Marshalls' raid on an organic Amish farmer and his family on 'Tucker Carlson Tonight.' #FoxNews #TuckerCarlsonTonight

Subscribe to Fox News! https://bit.ly/2vBUvAS
Watch more Fox News Video: http://video.foxnews.com
Watch Fox News Channel Live: http://www.foxnewsgo.com/

FOX News Channel (FNC) is a 24-hour all-encompassing news service delivering breaking news as well as political and business news. The number one network in cable, FNC has been the most-watched television news channel for 18 consecutive years. According to a 2020 Brand Keys Consumer Loyalty Engagement Index report, FOX News is the top brand in the country for morning and evening news coverage. A 2019 Suffolk University poll named FOX News as the most trusted source for television news or commentary, while a 2019 Brand Keys Emotion Engagement Analysis survey found that FOX News was the most trusted cable news brand. A 2017 Gallup/Knight Foundation survey also found that among Americans who could name an objective news source, FOX News was the top-cited outlet. Owned by FOX Corporation, FNC is available in nearly 90 million homes and dominates the cable news landscape, routinely notching the top ten programs in the genre.

---
## [moabid42/shell](https://github.com/moabid42/shell)@[27d408d5f6...](https://github.com/moabid42/shell/commit/27d408d5f6dcc0d9b59b9cf4f34d907cffc75eb0)
#### Tuesday 2022-08-23 18:58:32 by francesco

Merge pull request #6 from moabid42/cout

fuck you

---
## [davidmunoznovoa/horus-heresy](https://github.com/davidmunoznovoa/horus-heresy)@[26d54434f4...](https://github.com/davidmunoznovoa/horus-heresy/commit/26d54434f495e6a3b77ab1b3ae097381fd1485eb)
#### Tuesday 2022-08-23 20:01:12 by Nikola Beo

WLTs and Shrapnel

[Added]
- Generic WLTs
- Legion-specific WLT placeholders
- WLT SEG added to generics (Praetors, Centurion)
- Graviton and Shrapnel weapons to all relevant models (I'm dead inside after needing to handle such needlessly picky formatting from GW)
- To facilitate Shrapnel Pistols, I added a Bolt Pistol Options SEG to several generic units

[Changed]
- Master of the Legion; now a separate SE that checks for 1 instance per 1k pts
- Added MotL to all relevant characters
- Mandatory generic WLTs handled as links to single WLT rather than SEG (Only done for IW characters, but can easily be duplicated for others)
- Mandatory non-generic WLTs only constrained by Min/Max 1 Warlord (didn't think it was relevant to make their specific WLTs also constrained as only one Warlord can be chosen at a time afaik)
- Reformatted Palatine Blades to fit Tactical template (Min X, decrement X, repeat X for models)
- Reformatted Centurion weapon options to cut down on clutter and bring in line with recent discussions/other entries
- Some fairly serious changes to Veterans to force checks on TLC and basic unit choice. I might honestly suggest formatting them more like Termies; as much I hate how clunky it is, there does not seem to be another way to force model integrity. The other option is completely ignoring the book's format and formatting it the way Recon Squads and several others currently are; please advise.

Pretty sure I missed some Shrapnel/Graviton options in some places, but I'm very tired and can deal with them when someone points them out.

---
## [Arie/serveme](https://github.com/Arie/serveme)@[78c2451a4f...](https://github.com/Arie/serveme/commit/78c2451a4f6a6380aace9abba25cbf8eb22752b0)
#### Tuesday 2022-08-23 20:03:24 by Arie

Unban zefra

"Hi. I add you to make an unban request. a day ago I went in with a
friend to do a stupid troll to a player on a serveme.tf server. it was a
bad joke and we got banned. I play from time to time on tf2 center and I
can't get on the server to play because of the ban. I didn't know where
I could appeal for an unban and I'm writing to you here, and if i can
get help, next time it will not happen again."

---
## [tristan957/wrapdb](https://github.com/tristan957/wrapdb)@[7e69bfce97...](https://github.com/tristan957/wrapdb/commit/7e69bfce97df6ef5d70e556ca4059e8f5f38af3f)
#### Tuesday 2022-08-23 22:45:45 by Eli Schwartz

openjp2: Use wrap fallbacks instead of thirdparty

The thirdparty directory provided by upstream contains (old) versions of
projects we already have in the wrapdb. There is zero value in
permitting or encouraging this usage.

Also, the actual dependency lookups suck. e.g. the zlib logic, even when
probing for system versions, tries to find a pkg-config dependency, then
probes for 3 different library names, falls back to subproject() on a
subproject that doesn't exist in the wrap itself, with incorrect usage
of found(), and finally subdirs into the custom copy.

Half of this doesn't work, and all of it is redundant since meson
includes its own robust finder logic that does library probing correctly
in a cross-platform manner under the name... "zlib", just like the
pkg-config dependency.

Furthermore, ***upstream agrees with us***. To quote their own README:

```
This directory contains 3rd party libs (PNG, ZLIB)...

They are convinient copy of code from people outside of the OpenJPEG community.
They are solely provided for ease of build of OpenJPEG on system where those
3rd party libs are not easily accessible (typically non-UNIX).

The OpenJPEG does not recommend using those 3rd party libs over your system
installed libs. The OpenJPEG does not even guarantee that those libraries will
work for you.
```

This is so un-recommended by literally everyone everywhere, that
continuing to provide broken versions here is an intolerable thing.

What upstream wanted, really, was a build system that supported meson wraps.
Then they could have never included a thirdparty directory, but provided
subprojects/*.wrap "solely for ease of build on systems where those libs
are not easily accessible". It's a match made in heaven!

...

Also while we are at it, ditch the commented out copy of astyle, which
was built as an executable because a manually run maintainer shellscript
would execute the forked "openjpstyle" for you. It's totally unneeded by
the wrap, and even if it was considered interesting, it must go through
the standard wrap review && release process.

Move the remaining simple dependency() calls to the subdir that needs
them, which is already guarded by a project option.

Co-authored-by: Xavier Claessens <xavier.claessens@collabora.com>

---
## [DeetonRushy/Dee](https://github.com/DeetonRushy/Dee)@[f2ab642ced...](https://github.com/DeetonRushy/Dee/commit/f2ab642cedf980f7f9171bf215445fbd7f782346)
#### Tuesday 2022-08-23 22:49:35 by Deeton Rushton

accidently editied code from github god I hate this shit

---
## [mattmular/BreadmonBot](https://github.com/mattmular/BreadmonBot)@[342bdd46c2...](https://github.com/mattmular/BreadmonBot/commit/342bdd46c2f9d79d0c8a28ba2ffb00e1a4509aba)
#### Tuesday 2022-08-23 23:28:25 by ray314

Merge pull request #8 from mattmular/feature

fuck you git

---

