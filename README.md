## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-09-26](docs/good-messages/2022/2022-09-26.md)


2,154,724 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,154,724 were push events containing 3,224,667 commit messages that amount to 244,316,574 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 48 messages:


## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[d45e244401...](https://github.com/tgstation/tgstation/commit/d45e244401425d34edc38e3dd2f3c2bbdbcec7ce)
#### Monday 2022-09-26 00:07:24 by san7890

Crab-17 No Longer Breaks Economy If You Swipe Too Fast (#70094)

Hey there,

Remember swiping credit cards, before everything was chipped? You know how sometimes if you went too slow, the transaction might fail, the cashier had to plonk in some digits on their machine, and you had to go again? That kinda sucked.

If you're too young to get that reference, just imagine the card swiping task in AMONG US. Doesn't that minigame suck? You know exactly what that is. Same principle.

Anyways, that's pretty much what was going on here. The reason why SS.Economy would break so god damn hard if you swiped an ID before the machine's "boot up" slowflake animation was complete is probably due to the line where it starts fast processing. I added an early return to check for if the animation was complete by leveraging a var we already set at the end of the process, because I am lazy.

There's probably a few other ways you can tackle this issue, but this feels right to me in a thematic sense. I'm willing to change it if needed though.

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[9b9337de49...](https://github.com/tgstation/tgstation/commit/9b9337de493ec62927f15b0ee18f9342cd3c2d04)
#### Monday 2022-09-26 00:07:24 by Tim

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
## [jdl-joseph/Wafflebot](https://github.com/jdl-joseph/Wafflebot)@[da7c290583...](https://github.com/jdl-joseph/Wafflebot/commit/da7c290583a6780860dffc7da2063be1b8591987)
#### Monday 2022-09-26 01:05:04 by fire6945

suck my cock, dpy. you just got L'ed on. you thought you could fucking trip me up like that, huh? well, you were fucking wrong. suck it up, bitch.

---
## [rd-stuffs/msm-4.14](https://github.com/rd-stuffs/msm-4.14)@[4f7b1f6106...](https://github.com/rd-stuffs/msm-4.14/commit/4f7b1f610671210718b8854e079788e83a7ddc51)
#### Monday 2022-09-26 01:23:49 by Wang Han

power: Introduce OnePlus 3 fingerprintd thaw hack

Taken from Oneplus 3, this hack will make fingerprintd recover from suspend quickly.

Small fixes for newer kernels since we're coming from 3.10.108..

Change-Id: I0166e82d51a07439d15b41dbc03d7e751bfa783b
Co-authored-by: Cyber Knight <cyberknight755@gmail.com>
[cyberknight777: forwardport and adapt to 4.14]
Signed-off-by: Shreyansh Lodha <slodha96@gmail.com>
Signed-off-by: Pierre2324 <pdbbasketball@gmail.com>
Signed-off-by: PainKiller3 <ninadpatil100@gmail.com>
Signed-off-by: Dhruv <dhruvgera61@gmail.com>
Signed-off-by: Cyber Knight <cyberknight755@gmail.com>
Signed-off-by: Richard Raya <rdxzv.dev@gmail.com>

---
## [nrober734/hello-kube](https://github.com/nrober734/hello-kube)@[e93637cb63...](https://github.com/nrober734/hello-kube/commit/e93637cb63bd9b44650a8ffe6c1e659eb96f2d22)
#### Monday 2022-09-26 01:56:58 by Nic Roberts II

my whole life whittled away in front of a fucking screen full of shitty fucking config files

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[79b4a74a6e...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/79b4a74a6e6f13128779f88cb784ecb1e5989524)
#### Monday 2022-09-26 02:00:10 by RimiNosha

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
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[afcc7c7f5c...](https://github.com/pytorch/pytorch/commit/afcc7c7f5c7cef740241ff0abdae8d4f2ad22a03)
#### Monday 2022-09-26 02:24:10 by Andrew Gu

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
## [postgresql-cfbot/postgresql](https://github.com/postgresql-cfbot/postgresql)@[1c27d16e6e...](https://github.com/postgresql-cfbot/postgresql/commit/1c27d16e6e5c1f463bbe1e9ece88dda811235165)
#### Monday 2022-09-26 03:40:06 by Tom Lane

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
## [Totktonada/tarantool](https://github.com/Totktonada/tarantool)@[b6dba6c1e0...](https://github.com/Totktonada/tarantool/commit/b6dba6c1e0f551504590795485f9ae0782323a58)
#### Monday 2022-09-26 03:58:42 by Alexander Turenko

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

Aternatives considered
----------------------

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
## [Brawaru/knossos](https://github.com/Brawaru/knossos)@[83f50192d5...](https://github.com/Brawaru/knossos/commit/83f50192d5610f56714e4cfb54ef735a6b51d97d)
#### Monday 2022-09-26 04:11:33 by Sasha Sorokin

Add v-i18n:wrap directive

v-i18n:wrap directive is a directive that only has effect within the
<i18n-formatted> element. It takes an element as a skeleton and allows
to use so-called 'wrappers' in the translations.

Wrappers are extremely useful if translation needs to contain links or
buttons, but it does not make to split text from those to separate
strings.

For example, let's say we have the following HTML:

  Your project was rejected, please check out the <a href="/rules">rules</a>.

Without wrapper elements we would have to resort to the following:

In our translations file,

  {
    "rejection-message": "Your project was rejected, please check out the {rulesLink}.",
    "rejection-message.rules-link": "rules"
  }

In our Vue file,

  <i18n-formatted message-id="rejection-message">
    <a href="/rules" v-i18n:value="'rules-link'">{{ $t('rejection-message.rules-link') }}</a>
  </i18n-formatted>

For translators, this is not very plausable experience because they'd
have to guess what that 'rulesLink' variable actually contains, it's
good that we use good message IDs, but nevertheless, it's confusing
experience.

It also introduces a surface for mistake, translator may not pay close
attention to the message IDs and translate both strings independently.
As English speakers we tend to forget that other languages have more
advanced casing systems, where noun or verb may change depending on what
surrounds it, so in some languages, translating both strings can lead to
mistake.

To demonstrate, let me give you an example from Discord:

Say we have the following strings in original English text:

  {
    "hello-cta": "Say ‘{hello}’ to the {helloTarget}",
    "hello-cta.target": "cat"
  }

Which we can use as such:

  $t('hello-cta', { helloTarget: $t('hello-cta.target') })

But what happens if Ukrainian translator translates `hello-cta.target`
independently of `hello-cta` string. They translate it as such:

  {
    "hello-cta": "Сказати «привіт» {helloTarget}",
    "hello-cta.target": "кіт"
  }

And using code above, the result we will get from these translations:

  'Сказати «привіт» кіт'

Which is incorrect, in this case 'кіт' is supposed be in dative case,
which would change it to 'коту'.

Keeping that in mind, let's look how things would change if we were to
use wrapping syntax:

  {
    "hello-cta": "Сказати «привіт» <target>коту</target>"
  }

This looks like HTML, and if you think about it, it kinda is, but not
quite, it's merely wrapper, like BB-codes, and those do not accept any
arguments, to not complicate things.

In the code we would use `hello-cta` string as such:

  $t('hello-cta', { helloTarget: (parts) => `${parts.map(_ => String(_)).join('')}` }`)

Keep in mind, that in this example we don't do anything fancy yet, you
can see that our wrapper doesn't do anything apart from taking some
parts and later converting them to strings. If we don't use any objects
in our context object, then it will never be not array of strings, but
otherwise it'd contain these objects too in places of variables.

So what do we get when evaluating code above? Well, of corse:

  'Сказати «привіт» коту'

What v-i18n:wrap allows us to do is to create skeleton node, which will
be copied every time the wrapper used, and which children will be
replaced with aforementioned parts.

Let's look at the first example, but using wrappers now:

Here's our changed translation file:

  {
    "rejection-message": "Your project was rejected, please check out the <rules-link>rules</rules-link>."
  }

And here's how we'd change our template:

  <i18n-formatted message-id="rejection-message">
    <a href="/rules" v-i18n:wrap="'rules-link'" />
  </i18n-formatted>

Notice that we self-close our link element, that's because we know that
anything will be replaced anyway, so there is no sense to provide any
children.

And what happens when this string actually gets rendered?

  Your project was rejected, please check out the <a href="/roles">rules</a>.

Exactly what we'd expect.

So there we go, this is the new directive for you, hope this was
insightful and useful to understand the importance and usage of this
feature.

---
## [Brawaru/knossos](https://github.com/Brawaru/knossos)@[679f022378...](https://github.com/Brawaru/knossos/commit/679f0223782a796f68667a06b107f7d58b609e68)
#### Monday 2022-09-26 04:11:33 by Sasha Sorokin

Initial work on the i18n support

Absolutely not ready, just a draft for progress and maybe quick review
whether it's good idea or not.

This commit will be squashed with more meaningful message as the work
goes.

For now things are like this:

- It uses @formatjs/intl which uses ICU Message Format for messages,
  it's the same underlying framework than used in React. However,
  their Vue module is only for Vue 3 and it also not dynamic (means
  you can only initialise it with a single language which is weird),
  so I had to re-do all work by myself.

- Reason not to use vue-i18n: it's weird formatting for translations.
  I agree it's a more mature module, but as translator myself I under
  no circumstance want to translate things like {n} apple | {n} apples.
  ICU Message Format is already an industry standard so there's no good
  reason to re-invent the wooden wheel when people already have alloy
  ones.

- There is no automatic extraction, sadly.

- There is no automatic locale packing. I have no clue how to implement
  Nuxt modules to do this magic, but it's probably very possible, should
  look at https://i18n.nuxtjs.org/ for inspiration, they use some weird
  templates and generate plugins. Oh my oh my.

---
## [abraham-yusuf/next.js](https://github.com/abraham-yusuf/next.js)@[1bbd264216...](https://github.com/abraham-yusuf/next.js/commit/1bbd2642164098ceb9cebfb36deba9aed7e8a53b)
#### Monday 2022-09-26 04:47:08 by abdennor

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
## [shahezad96/Cataclysm-DDA](https://github.com/shahezad96/Cataclysm-DDA)@[344458376f...](https://github.com/shahezad96/Cataclysm-DDA/commit/344458376f780b7ed8bca7e45fdc887eb05ea937)
#### Monday 2022-09-26 04:54:10 by Christian Stadler

Update Sapiovore mood boosts from eating humans (#59077)

* Give psychopathic sapiovores a mood boost when eating human meat.

* Changes, because sapiovores can't be psychopaths at the same time

See also issue #58764

* Forgot the m_good and fixed the indentation.

* Moved sapiovore only chunk up and fixed my broken code.

* Removed one more redundancy

`sapiovore && spiritual` is handled above. No need to check that again.

* No message and no mood boost for Sapiovores without Spiritual.

* Sapiovore and Spiritual combo is now down to +10 morale

Message is "You eat the human flesh, and in doing so, devour their spirit.", similar to `cannibal && psycho && spiritual` but sapiovores don't feast upon it.

* Add "Mmh.  Tastes like venison." as neutral message for sapiovores

---
## [DASHGMR/NewHaven](https://github.com/DASHGMR/NewHaven)@[8559739bf4...](https://github.com/DASHGMR/NewHaven/commit/8559739bf42f01535f21957f438b43716c80b6c8)
#### Monday 2022-09-26 05:00:16 by DASHGMR

Add files via upload

                     -- ROAD TO --
 _   _  _____ _    _   _   _   ___  _   _ _____ _   _ 
| \ | ||  ___| |  | | | | | | / _ \| | | |  ___| \ | |
|  \| || |__ | |  | | | |_| |/ /_\ \ | | | |__ |  \| |
| . ` ||  __|| |/\| | |  _  ||  _  | | | |  __|| . ` |
| |\  || |___\  /\  / | | | || | | \ \_/ / |___| |\  |
\_| \_/\____/ \/  \/  \_| |_/\_| |_/\___/\____/\_| \_/v1.0

                   -- DASHGMR 2022 --

Hey There! Thank you so much for checking out my first ever SMW Hack.
This is a prelude to my expert hack that is on its way titled "NEW HAVEN".

While I've had many test out NEW HAVEN, I noticed that there was a difficulty curb that many
struggled to overcome, so I decided to make a short prelude hack that is beginner friendly with
a difficulty option on each level.

4 Levels, 5 Exits.
King Keys are collectable items that activate Bowser Blocks (! Switch Blocks) and can be de-activated
by re-collecting them from the same location you found them in.

Be Sure to Read the Tutorial for everything.

Best to patch with "Super Mario World (U) [!]"

Good Luck & Have Fun!

=========================================================================================================
Credits:
=========================================================================================================
Game Design:
DASHGMR

Music:
MAIN THEME "Floating" - Jimmy, Pink Gold Peach
MAP "F-Zero - Select Time" - S1Z2
SEASIDE SAUNTER "Radix - Linda's World" - Dippy
SKY-TREE TUSSLE "Plok - Main Theme" - KevinM
GOLDEN HOUR "Prince of Moonlight" - Moose
BOW OUT "VVVVVV - Piercing the Sky" - DanTheVP
THE ODYSSEY "Wii Shop Channel" - KevinM, tssf
BOSS "Midway Boss - Yoshi's Island" - Vitor Vilela, Lui37
BOSS 2 "Be the Hero" - Dark Mario Bros, Moose, Ultima

Testing:
JEZJITZU
DRKRDNK
PIXLRIK
PLAINOLETREY
SHRIKELET
AGATHOR86
PZYKO103
OREOSAREPOOP
SNIPPOAU
SPARKYSIE
JR_87
INKYDOM
RUBY RAWLINS

Coding:
FluxBaserom (bit.ly/FLXBSC)
DASHGMR
SJCharlieTheCat
DtotheFourth
Fernap
TheMario90

Tools:
FluxBaserom
Lunar Magic
YY-CHR
SMWMTE
SHEX

Inspiration:
ACMLM
DRKRDNK
LUSH_50
JEZJITZU
SPARKYSIE
DAN2POINT5
WYATT CROUCHER
CHODONTORE
MY MUM & DAD






Okay Fine...




SOME NERD NAMED JUZCOOK






Special Thanks to:
Andre - Zio Loves You.

---
## [ProjectVelvet/android_kernel_sm6250](https://github.com/ProjectVelvet/android_kernel_sm6250)@[112305a303...](https://github.com/ProjectVelvet/android_kernel_sm6250/commit/112305a303425a1d13841af11c85272a85754607)
#### Monday 2022-09-26 05:01:07 by Maciej Żenczykowski

FROMGIT: bpf: Do not change gso_size during bpf_skb_change_proto()

This is technically a backwards incompatible change in behaviour, but I'm
going to argue that it is very unlikely to break things, and likely to fix
*far* more then it breaks.

In no particular order, various reasons follow:

(a) I've long had a bug assigned to myself to debug a super rare kernel crash
on Android Pixel phones which can (per stacktrace) be traced back to BPF clat
IPv6 to IPv4 protocol conversion causing some sort of ugly failure much later
on during transmit deep in the GSO engine, AFAICT precisely because of this
change to gso_size, though I've never been able to manually reproduce it. I
believe it may be related to the particular network offload support of attached
USB ethernet dongle being used for tethering off of an IPv6-only cellular
connection. The reason might be we end up with more segments than max permitted,
or with a GSO packet with only one segment... (either way we break some
assumption and hit a BUG_ON)

(b) There is no check that the gso_size is > 20 when reducing it by 20, so we
might end up with a negative (or underflowing) gso_size or a gso_size of 0.
This can't possibly be good. Indeed this is probably somehow exploitable (or
at least can result in a kernel crash) by delivering crafted packets and perhaps
triggering an infinite loop or a divide by zero... As a reminder: gso_size (MSS)
is related to MTU, but not directly derived from it: gso_size/MSS may be
significantly smaller then one would get by deriving from local MTU. And on
some NICs (which do loose MTU checking on receive, it may even potentially be
larger, for example my work pc with 1500 MTU can receive 1520 byte frames [and
sometimes does due to bugs in a vendor plat46 implementation]). Indeed even just
going from 21 to 1 is potentially problematic because it increases the number
of segments by a factor of 21 (think DoS, or some other crash due to too many
segments).

(c) It's always safe to not increase the gso_size, because it doesn't result in
the max packet size increasing.  So the skb_increase_gso_size() call was always
unnecessary for correctness (and outright undesirable, see later). As such the
only part which is potentially dangerous (ie. could cause backwards compatibility
issues) is the removal of the skb_decrease_gso_size() call.

(d) If the packets are ultimately destined to the local device, then there is
absolutely no benefit to playing around with gso_size. It only matters if the
packets will egress the device. ie. we're either forwarding, or transmitting
from the device.

(e) This logic only triggers for packets which are GSO. It does not trigger for
skbs which are not GSO. It will not convert a non-GSO MTU sized packet into a
GSO packet (and you don't even know what the MTU is, so you can't even fix it).
As such your transmit path must *already* be able to handle an MTU 20 bytes
larger then your receive path (for IPv4 to IPv6 translation) - and indeed 28
bytes larger due to IPv4 fragments. Thus removing the skb_decrease_gso_size()
call doesn't actually increase the size of the packets your transmit side must
be able to handle. ie. to handle non-GSO max-MTU packets, the IPv4/IPv6 device/
route MTUs must already be set correctly. Since for example with an IPv4 egress
MTU of 1500, IPv4 to IPv6 translation will already build 1520 byte IPv6 frames,
so you need a 1520 byte device MTU. This means if your IPv6 device's egress
MTU is 1280, your IPv4 route must be 1260 (and actually 1252, because of the
need to handle fragments). This is to handle normal non-GSO packets. Thus the
reduction is simply not needed for GSO packets, because when they're correctly
built, they will already be the right size.

(f) TSO/GSO should be able to exactly undo GRO: the number of packets (TCP
segments) should not be modified, so that TCP's MSS counting works correctly
(this matters for congestion control). If protocol conversion changes the
gso_size, then the number of TCP segments may increase or decrease. Packet loss
after protocol conversion can result in partial loss of MSS segments that the
sender sent. How's the sending TCP stack going to react to receiving ACKs/SACKs
in the middle of the segments it sent?

(g) skb_{decrease,increase}_gso_size() are already no-ops for GSO_BY_FRAGS
case (besides triggering WARN_ON_ONCE). This means you already cannot guarantee
that gso_size (and thus resulting packet MTU) is changed. ie. you must assume
it won't be changed.

(h) changing gso_size is outright buggy for UDP GSO packets, where framing
matters (I believe that's also the case for SCTP, but it's already excluded
by [g]).  So the only remaining case is TCP, which also doesn't want it
(see [f]).

(i) see also the reasoning on the previous attempt at fixing this
(commit fa7b83bf3b156c767f3e4a25bbf3817b08f3ff8e) which shows that the current
behaviour causes TCP packet loss:

  In the forwarding path GRO -> BPF 6 to 4 -> GSO for TCP traffic, the
  coalesced packet payload can be > MSS, but < MSS + 20.

  bpf_skb_proto_6_to_4() will upgrade the MSS and it can be > the payload
  length. After then tcp_gso_segment checks for the payload length if it
  is <= MSS. The condition is causing the packet to be dropped.

  tcp_gso_segment():
    [...]
    mss = skb_shinfo(skb)->gso_size;
    if (unlikely(skb->len <= mss)) goto out;
    [...]

Thus changing the gso_size is simply a very bad idea. Increasing is unnecessary
and buggy, and decreasing can go negative.

Fixes: 6578171a7ff0 ("bpf: add bpf_skb_change_proto helper")
Signed-off-by: Maciej Żenczykowski <maze@google.com>
Signed-off-by: Daniel Borkmann <daniel@iogearbox.net>
Cc: Dongseok Yi <dseok.yi@samsung.com>
Cc: Willem de Bruijn <willemb@google.com>
Link: https://lore.kernel.org/bpf/CANP3RGfjLikQ6dg=YpBU0OeHvyv7JOki7CyOUS9modaXAi-9vQ@mail.gmail.com
Link: https://lore.kernel.org/bpf/20210617000953.2787453-2-zenczykowski@gmail.com

(cherry picked from commit 364745fbe981a4370f50274475da4675661104df https://git.kernel.org/pub/scm/linux/kernel/git/bpf/bpf-next.git/commit/?id=364745fbe981a4370f50274475da4675661104df )
Test: builds, TreeHugger
Bug: 188690383
Signed-off-by: Maciej Żenczykowski <maze@google.com>
Change-Id: I0ef3174cbd3caaa42d5779334a9c0bfdc9ab81f5
Signed-off-by: Excalibur-99 <txexcalibur99@gmail.com>

---
## [bonnici/apollo-server](https://github.com/bonnici/apollo-server)@[793de3e230...](https://github.com/bonnici/apollo-server/commit/793de3e2308cc3ec98f14a67801c77a5e6640a7d)
#### Monday 2022-09-26 05:16:19 by Trevor Scheer

Add Jest imports everywhere, remove global availability (#6911)

In ESM mode, the `jest` globals are technically no longer available. For
some reason, we're still getting away with it, but this issue surfaces
in the v29 upgrade PR so I'm going to address it separately.

https://jestjs.io/docs/ecmascript-modules#differences-between-esm-and-commonjs

Ref:
https://github.com/apollographql/apollo-server/pull/6850#issuecomment-1247157466

<!--
First, 🌠 thank you 🌠 for taking the time to consider a contribution to
Apollo!

Here are some important details to follow:

* ⏰ Your time is important
To save your precious time, if the contribution you are making will take
more
than an hour, please make sure it has been discussed in an issue first.
          This is especially true for feature requests!
* 💡 Features
Feature requests can be created and discussed within a GitHub Issue. Be
sure to search for existing feature requests (and related issues!) prior
to
opening a new request. If an existing issue covers the need, please
upvote
that issue by using the 👍 emote, rather than opening a new issue.
* 🔌 Integrations
Apollo Server has many web-framework integrations including Express,
Koa,
Hapi and more. When adding a new feature, or fixing a bug, please take a
peak and see if other integrations are also affected. In most cases, the
fix can be applied to the other frameworks as well. Please note that,
since new web-frameworks have a high maintenance cost, pull-requests for
new web-frameworks should be discussed with a project maintainer first.
* 🕷 Bug fixes
These can be created and discussed in this repository. When fixing a
bug,
please _try_ to add a test which verifies the fix. If you cannot, you
should
still submit the PR but we may still ask you (and help you!) to create a
test.
* 📖 Contribution guidelines
Follow
https://github.com/apollographql/apollo-server/blob/main/CONTRIBUTING.md
when submitting a pull request. Make sure existing tests still pass, and
add
          tests for all new behavior.
* ✏️ Explain your pull request
Describe the big picture of your changes here to communicate to what
your
pull request is meant to accomplish. Provide 🔗 links 🔗 to associated
issues!

We hope you will find this to be a positive experience! Open source
contribution can be intimidating and we hope to alleviate that pain as
much as possible. Without following these guidelines, you may be missing
context that can help you succeed with your contribution, which is why
we encourage discussion first. Ultimately, there is no guarantee that we
will be able to merge your pull-request, but by following these
guidelines we can try to avoid disappointment.
-->

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[b3b85cae9b...](https://github.com/odoo-dev/odoo/commit/b3b85cae9b1951b82053d7c6b55e559cbc48307d)
#### Monday 2022-09-26 05:31:17 by Xavier Morel

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
## [LemonInTheDark/tgstation](https://github.com/LemonInTheDark/tgstation)@[d34fa4c642...](https://github.com/LemonInTheDark/tgstation/commit/d34fa4c642839215df5ba985d098a04e4d555b5b)
#### Monday 2022-09-26 06:13:40 by LemonInTheDark

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
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[223e8bfd96...](https://github.com/tgstation/tgstation/commit/223e8bfd96a7762f0d23dd9b789fa90be1a572ec)
#### Monday 2022-09-26 07:39:57 by Time-Green

Fixes gravity pulse and transparent floor plane sharing a layer (#70124)

fixes gravity pulse and transparent floor plane sharing a layer

Broken by #69642 , sorry
I'll open up a seperate PR later today with a unit test to catch these cases
(my later today is in like 10 hours)

closes #70123 (weird fucking floors)

---
## [chaosvolt/cdda-arcana-mod](https://github.com/chaosvolt/cdda-arcana-mod)@[17a60391fd...](https://github.com/chaosvolt/cdda-arcana-mod/commit/17a60391fdc3120121646732e4558cdd49c616ea)
#### Monday 2022-09-26 09:03:29 by Chaosvolt

Recipe adjustments

* Updated and standardized how plant materials are consumed in the recipes for flame talisman, carmine vulnerary, and scroll of regrowth.
* Allowed saline solution as an alternative to salt water for blood effigy.
* Updated metal demand for divine scrolls of light and darkness to be more on pair with relative demand when used for air talismans.
* Updated mineral demand for scroll of command to be a bit less annoying to fulfill.
* Tweaked ratios of bone used for earth talisman recipe, made bone demands for scroll of sundering recipe scale a bit closer to that.
* Allowed acid chitin for the monster-sacrifice recipe that produces essence, increased fibrous stalk requirement because damn those triffids got hands.
* Adjusted alternative materials for scroll of discord.
* Adjusted organ requirements for air talisman recipe.

---
## [bearrrrrrrr/coyote-bayou](https://github.com/bearrrrrrrr/coyote-bayou)@[8a27b0fe9d...](https://github.com/bearrrrrrrr/coyote-bayou/commit/8a27b0fe9d5f5f30d2db06246970d76c74cfe00d)
#### Monday 2022-09-26 10:18:40 by bearrrrrrrrr

i'm KILLING you. i am KILLING y ou. i don't care about anything else i don't give a SHIT about anything else. my programming is just, 'GET THAT FUCKING GUY'

---
## [ShafiReza/life-story](https://github.com/ShafiReza/life-story)@[398e9258c3...](https://github.com/ShafiReza/life-story/commit/398e9258c3ec076fb9834bdb6ff0d20428064a7b)
#### Monday 2022-09-26 10:45:59 by ShafiReza

ultimate truth of life

My birth is the curse of my family and also my country. I am sorry everyone . I know if I say you that plz forgive me you do not forgive but please give me peace by killing me as you want. I have not enough strength to kill myself . whatever I done in my life is totally a biggest mistake but now plz kill me .

---
## [kavishinsa/Prestige-Park-Grove-In-Whitefield-Bangalore](https://github.com/kavishinsa/Prestige-Park-Grove-In-Whitefield-Bangalore)@[5b7d5407ef...](https://github.com/kavishinsa/Prestige-Park-Grove-In-Whitefield-Bangalore/commit/5b7d5407efa1a3565f2567a47a7fc2ad229ebf38)
#### Monday 2022-09-26 11:37:07 by kavishinsa

Prestige Park Grove Whitefield Bengaluru

Are you planning to buy your dream home at one of the wonderful and luxurious places in Bangalore? Prestige Park Grove is your destination at Whitefield, Bengaluru. This city of your dreams is built exclusively to take care of your happiness and well-being. Not just filled with outstanding conveniences, but the location would be apt for you. This luxury apartment is exclusively designed to make sure you get seamless finishing. You can live with peace in this property as the maintenance staff firmly vigil possessions.

Prestige Group is ruling the industry for a long that’s why it has earned a great name and fame in the marketplace. Prestige Park Grove Bengaluru offers residential apartments 1, 2, & 3 BHK units that will offer you a serene and calm life where you will hear the chirping sound of birds and enjoy fascinating views of the city. 

It offers modern conveniences and services to people at an affordable value. The apartments are designed uniquely and without any errors. For security guards are appointed along with a 24/7 active CCTV scanner. It is convenient to travel from Whitefield to other places with good connectivity using private and public transportation conveniences.

Enjoy modern facilities with comfort and grab the special discounts provided by Prestige Park Grove Bengaluru. The commitment to meeting our customers’ demands for supreme quality has made us a well-known name in the market now.

For More Details:
Visit Here: https://bit.ly/3Cc90eX

---
## [bellegarde-c/android_kernel_oneplus_sm8150](https://github.com/bellegarde-c/android_kernel_oneplus_sm8150)@[00795d438d...](https://github.com/bellegarde-c/android_kernel_oneplus_sm8150/commit/00795d438d04f3578c2668768a0a11a3b1d0e4f6)
#### Monday 2022-09-26 11:46:48 by Peter Zijlstra

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
## [shubham1994s/AppynittyWebApp](https://github.com/shubham1994s/AppynittyWebApp)@[c58b8527f0...](https://github.com/shubham1994s/AppynittyWebApp/commit/c58b8527f02ae7fbb79bb7eb685159097c345d2c)
#### Monday 2022-09-26 13:13:50 by umeshl@appynitty.com

Chnages done By Millioniare persone and its me i will be definelty successfull in this year from tommoro i strat trading meditaion gym with full of decipliend and wakeing up from comfort zone strickly follow my rules to becomeing acheived my goals god please stay with me and forgive for any mistake and negative thoughts please thanku so much for yours support greatest energy of universe

---
## [martinking71/magnum-integration](https://github.com/martinking71/magnum-integration)@[8fdf1479bf...](https://github.com/martinking71/magnum-integration/commit/8fdf1479bf01109d4171ba43496eea9578c120b0)
#### Monday 2022-09-26 13:21:49 by Vladimír Vondruš

package/archlinux: don't build DartIntegration in the dev PKGBUILD.

I'm tired of this thing. The libdart package is in AUR and depends on
a fractal consisitng of about 90 packages, including OSG, blas, TBB and
lapack, many of which take 30+ GB RAM to build and include tests and all
other crap. And then, once I suffer through all that, it will crash
right after start because *the damn thing* sends unaligned allocations
to Eigen AVX code, blowing up.

No. Enough suffering. Not worth my time. The only place where this thing
is built is on a single CI job, and even that is painful. DART has to
fix its dependency tree, it's not my job to do that for them.

---
## [edsantiago/libpod](https://github.com/edsantiago/libpod)@[28b45eb17e...](https://github.com/edsantiago/libpod/commit/28b45eb17e55169a93caa1db17dcea27638852b5)
#### Monday 2022-09-26 15:34:39 by Ed Santiago

Proof of concept: nightly dependency treadmill

As discussed in f2f: this is the cleanest, simplest mechanism
I can think of to auto-test the Big Three dependencies: simply
run go mod edit immediately after git checkout, then run the
entire CI test suite.

If this approach works, we can set up a new CIRRUS_CRON=treadmill
job. I'm expecting it not to work, because Murphy, but want to
see what the unexpected gotchas are.

This differs significantly from the buildah treadmill, in that
buildah is almost impossible to re-vendor without manual intervention.
(In practice, so are these, but let's dream of a world in which
this will run and pass every night). (I want a pony too).

Signed-off-by: Ed Santiago <santiago@redhat.com>

---
## [canedoly/Fedoraware](https://github.com/canedoly/Fedoraware)@[f370cbf8ed...](https://github.com/canedoly/Fedoraware/commit/f370cbf8edda9593758c3d24244b985d7c993735)
#### Monday 2022-09-26 16:09:41 by Baan

fix.

the beep beep beep beep beep beep shit was fucking annoying as on god.

---
## [ShalmonAnandas/MangDL](https://github.com/ShalmonAnandas/MangDL)@[2fc98eee68...](https://github.com/ShalmonAnandas/MangDL/commit/2fc98eee6841cd42984d6c4df8d1d62a5143e4b0)
#### Monday 2022-09-26 16:11:31 by whi~nyaan

This patch is for my lovely boyfriend, bump to `3.0.0.0`

---
## [matrix-org/uniffi-rs](https://github.com/matrix-org/uniffi-rs)@[ae00abada1...](https://github.com/matrix-org/uniffi-rs/commit/ae00abada1d9a5ab6b9dc6b673722f9de426c5f3)
#### Monday 2022-09-26 16:48:12 by Ben Dean-Kawamura

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
## [Malii47/GucluSarp](https://github.com/Malii47/GucluSarp)@[a9db63d22d...](https://github.com/Malii47/GucluSarp/commit/a9db63d22d17c536b51098a49e68de6b13f073d1)
#### Monday 2022-09-26 16:59:24 by FangeLLL

EnemyGun Fixed

-Now he can die. Also he can kill you. But there is no bullet particle. Like I said we are going to delete this shit so that's not a thing.

---
## [the-garlic-os/computer-status-neo](https://github.com/the-garlic-os/computer-status-neo)@[60a822a4da...](https://github.com/the-garlic-os/computer-status-neo/commit/60a822a4da9e7929bbf7f3749bbe0322a51dd35d)
#### Monday 2022-09-26 17:08:55 by Nate

Unholy combination of theme and backend changes

I dont want to separate these two types of changes out. The git diff is so ugly
- Process objects are global now. There is one for printing to the result pane and another (configured differently on the Windows level) for printing to a console window.
- No more raw pointers! :) Found out about QSmartPointer and replaced all my raw pointers with that. Look at that beautiful empty destructor
- Added timeout to executeToResultPane. If something takes longer than 10 seconds (a constant in the .h file) a QTimer object will force kill it. Result-pane processes are not meant to take long; those go in console windows.
- Print to result pane if a command errors out, including console-window commands.
- A development thing in comments for hot-reloading QSS
- Style-loading code changed to support multiple files
- Buttons list moved out to global object so it only has to be computed once
- Inline updateLabelRunningAs because it looks like we're only ever going to run it once per lifecycle
- Working on finally implementing Switch User
- Removed callback support for the process running helper functions because it got annoying to maintain and I don't actually use it

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[51a9840422...](https://github.com/treckstar/yolo-octo-hipster/commit/51a9840422b118223347e32495735ecfe0cc12da)
#### Monday 2022-09-26 17:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [woodsts/linux-stable-rt](https://github.com/woodsts/linux-stable-rt)@[adee8f3082...](https://github.com/woodsts/linux-stable-rt/commit/adee8f3082b01e5dab620d651e3ec75f57c0c855)
#### Monday 2022-09-26 17:47:35 by Peter Zijlstra

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
## [FahimFBA/free-programming-books](https://github.com/FahimFBA/free-programming-books)@[5fd70502a0...](https://github.com/FahimFBA/free-programming-books/commit/5fd70502a063c46914fd444d2511c8233f81777f)
#### Monday 2022-09-26 17:54:56 by Mathieu FONTAINE

Update free-programming-cheatsheets.md - React (#7095)

I suggested a React cheat sheet that I use very often. It is one of the most exhaustive and qualitative in my opinion.

---
## [ammarfaizi2/linux-fork](https://github.com/ammarfaizi2/linux-fork)@[ff2060dac7...](https://github.com/ammarfaizi2/linux-fork/commit/ff2060dac799c873434ee50c027ff95baeedbb56)
#### Monday 2022-09-26 18:02:47 by Johannes Weiner

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
## [philipl/mpv](https://github.com/philipl/mpv)@[096cd08268...](https://github.com/philipl/mpv/commit/096cd08268880e5da77072302fac14904ab18764)
#### Monday 2022-09-26 18:35:44 by Philip Langdale

f_hwtransfer: get rid of the shit list

A few years ago, wm4 got sufficiently annoyed with how vaapi image
format support was being discovered that he flipped the table and
introduced the shit list (which just included vaapi) to hard-code the
set of supported formats.

While that might have been necessary at the time, I haven't been able
to find a situation where the true list of supported formats was unsafe
to use. We filter down the list based on what the vo reports - and the
vo is already doing a thorough testing of formats, and if a format
makes it through that gauntlet, it does actually work.

Interestingly, as far as I can tell, the hwdec_vaapi probing code was
already good enough at the time (also written by wm4), so perhaps the
key difference here is that the driver side of things has improved.

I dug into this because of the support for the 422/444 high bit depth
vaapi formats I added to ffmpeg. These are obviously not in the hard
coded list today, but they work fine.

Finally, although it's positioned as a vaapi thing, it's really just
Intel specific, as the AMD vaapi driver has never exposed support for
anything except the formats used by the decoder/encoder profiles.

---
## [omap-audio/linux-audio](https://github.com/omap-audio/linux-audio)@[b617d3d20c...](https://github.com/omap-audio/linux-audio/commit/b617d3d20c6a5e04642d453f5f0ecaa14e04d5e4)
#### Monday 2022-09-26 18:53:09 by Peter Xu

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
## [mrcreepysos/Eclipse-Difficulty](https://github.com/mrcreepysos/Eclipse-Difficulty)@[1ae64e895f...](https://github.com/mrcreepysos/Eclipse-Difficulty/commit/1ae64e895f39d187d078ab255c39ea7946903b9e)
#### Monday 2022-09-26 19:04:55 by mrcreepysos

rework dozers (again)

no longer stunned by explosives as that was buggy as hell and caused a lot of desync for clients
also basically forced the he slug / grenade launcher meta (kinda cringe :julesno:)

instead their faceplate and visor health now scale with the player count, the more the tankier

---
## [SpaceSmithers/tgstation](https://github.com/SpaceSmithers/tgstation)@[f923f61011...](https://github.com/SpaceSmithers/tgstation/commit/f923f6101103e4ff1aeefd57d0531a3bc437a77a)
#### Monday 2022-09-26 19:28:55 by MMMiracles

Tramstation: Modular Maintenance Insanity (#69000)

About The Pull Request
Every single part of maintenance has been segmented into modules with multiple variants with different themes. As it stands, there are currently 80 modular parts that come together to form the entire maintenance layout for both levels. Part 1 of a 2 part PR set, requires #69486 to have full effect.

Why It's Good For The Game
Maintenance as it stands is a bit barren, not much reason to explore it with boring same-same rooms despite current randomized modules. With these issues in mind, I completely scrapped maintenance as it was and rebuilt it in mind with full modular segments with proper documentation on what each piece is and where it is located. These changes were also designed to make maintenance more friendly for our dark-dwelling antags and xenos alike, as each major module now has an air vent and scrubber.

Fixes #68320

Main Event:

Every single part of maintenance was turned into module chunks. Sections of the map that originally had maintenance was traced out with checkered flooring so mappers can still see the general layout of the tunnels when making larger edits.
Every module has been documented with proper nodes with descriptions of where each module is located on the map.
Each main module has a regular variant and an abandoned variant. Abandoned variants have blocked access routes and look more like unfinished carved out tunnels than regular maintenance.
Each module has 2 attachment points barring 2. Each attachment has 3 potential layouts that are chosen each round. A storage room with construction supplies one round might be a carved out room with minerals the next.
QoL/General Fixes:

Maintenance should have much more xeno/antag spawns to give various mid-round antags better chances at starting.
Camera network has been given a once-over with duplicate/floating cameras fixed.
The helpful bots in the lower tunnel should now actually do full rotations instead of whatever the hell they were doing before.
I still need to do some testing with disposals and final touch ups to make sure there aren't any weird overlaps, but as of right now the actual mapping quality is ready for review.

---
## [discordia-space/CEV-Eris](https://github.com/discordia-space/CEV-Eris)@[29430253ff...](https://github.com/discordia-space/CEV-Eris/commit/29430253ffa7c3394df438c922c3827bfbf79f51)
#### Monday 2022-09-26 20:12:08 by maikilangiolo

Levergun re do (#7587)

* update timer (#7501)

* FUCK YOU FUCK YOUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU

* Update code/modules/projectiles/guns/projectile/battle_rifle/levergun.dm

Co-authored-by: hyperioo <64754494+hyperioo@users.noreply.github.com>

---
## [iriebijudicael/site-plan-rafting.html](https://github.com/iriebijudicael/site-plan-rafting.html)@[9a8dd22ffe...](https://github.com/iriebijudicael/site-plan-rafting.html/commit/9a8dd22ffe5958ef2a8fba3b3d156cc39019be0b)
#### Monday 2022-09-26 20:27:53 by Irie Bi

<!DOCTYPE html>
<html lang="en-us">

<head>
  <meta charset="utf-8" />
  <title>Site Plan</title>
  <link type="text/css" rel="stylesheet" href="styles/site-plan-rafting.css" />
</head>

<body>
  <header>
    <h1>White Water Rafting</h1>
    <h2>Judicael Elvis Irie Bi</h2>
    <h2>WDD 130-30</h2>
    <!-- In the header above, add the name of your site, your name and class number. For example if you are in section 3 you would put WDD 130-03 -->
  </header>
  <main>
    <!-- ------------------------Steps 2-5------------------------------ -->
    <hr />
    <h2>Overview</h2>
    <h3>Purpose</h3>
    <p>This site exploired the relationships that adventure have with the White Water Rafting
      (i.e. emotional response and place attachment) and also stand as proof that thrill and natural motivations led to relaxation and
      a positive affective response towards the adventure activity, which led to a nature wide trip,
      attachment to the adventure destination and positive behavioral outcomes
      and that perceived risk was a significant moderator between thrill and
      affective response. While noted these findings will assist marketers in promoting
      the activities and locations to attract more adventure tourists.</p>
    <!-- change this -->

    <h3>Audience</h3>
    <p>
      Target audience:
    </p>
    <ul>
        <li>Adventurous</li>
        <li>Upper middle class to upper class income</li>
        <li>Healthy lifestyle</li>
        <li>Family oriented for one and two day trips</li>
        <li>Single professionals for week long trips What do they want?</li>
        <li>These people want a fun adventure to share with family or friends/co-workers</li>
        <li>They want to experience something new to them</li>
        <li>By outdoor supplies relating to water activities</li>
    </ul>
    <!-- change this -->

    <hr />
    <h2>Branding</h2>
    <h3>Website Logo</h3>
    <!-- Replace this with some sort of logo for your site.  A logo can be as simple as the name of your site in a nice font :) -->
    <img src="https://byui-wdd.github.io/wdd130/rafting_images/dryoarlogo.png" alt="Logo image" />
    <hr />
    <h2>Style Guide</h2>

    <!-- ------------------------Steps 6-9------------------------------ -->

    <h3>Color Palette</h3>
    <!--  The colors you choose for a website are one of the most important decisions you will make. Follow the instructions on the activity in Canvas then return and replace the color codes below with the hex color codes (the 6 digit numbers that show at the bottom of each color) for the colors you have chosen below.  You should have at least 2 colors but do not have to fill in all 4 if you do not need them.  -->

    <!-- Copy and paste the URL to your finished palette below. Replace the href value that is there with yours. Make sure to paste it into both the href value and the content text of the <a> tag -->
    <p>Palette URL:</p>
    <a href="https://coolors.co/396e94-e7c24f-a43312-381d2a-aabd8c"
      target="_blank">https://coolors.co/396e94-e7c24f-a43312-381d2a-aabd8c</a>

    <table class="colors">
      <tr>
        <th>Primary</th>
        <th>Secondary</th>
        <th>Accent 1</th>
        <th>Accent 2</th>
      </tr>
      <!-- Replace the numbers in the boxes below with your hex color codes. Then switch to the site-plan.css file and change your colors there as well. -->
      <tr>
        <td class="primary">[#396E94]</td>
        <td class="secondary">[#E7C24F]</td>
        <td class="accent1">[#A43312]</td>
        <td class="accent2"></td>
      </tr>
    </table>

    <!-- ------------------------Steps 10-12------------------------------ -->

    <h3>Typography</h3>
    <!-- Choose a font for your paragraphs (body copy) and headlines. What font(s) have you chosen? Think also about which of your colors above you might use for background and font colors. -->

    <h4>
      Heading Font: Montserrat
      <!-- change this -->
    </h4>
    <h4>
      Paragraph Font: Rock Salt
      <!-- change this -->
    </h4>
    <h3>Normal paragraph example</h3>
    <p>
      The best Whitewater Rafting in Colorado, White Water Rafting Company
      offers rafting on the Colorado and Roaring Fork Rivers in Glenwood
      Springs. Since 1974, we have been family owned and operated, rafting the
      Shoshone section of Glenwood Canyon and beyond.
    </p>
    <h3>Colored paragraph example</h3>
    <p class="colored">
      Trips vary from mild and great for families, to trips exclusively for
      physically fit and experienced rafters. No matter what type of river
      adventures you are seeking, White Water Rafting Company can make it
      happen for you.
    </p>

    <!-- ------------------------Step 13------------------------------ -->

    <h3>Navigation</h3>
    <!-- Think about how you want your navigation bar to look. In the site-plan.css file change the colors to your colors to get the look you desire. -->
    <nav>
      <a href="#">Home</a>
      <a href="#">Page2</a>
      <a href="#">Contact Us</a>
    </nav>
    <hr />
    <h2>Site Map</h2>
    <div class="sitemap">
      <div class="sm-home">Home</div>
      <div class="sm-page2">
        [Page2]
        <!-- this page will have a name later -->
      </div>
      <div class="sm-page3">Contact Us</div>

      <div class="top">&nbsp;</div>
      <div class="left">&nbsp;</div>
      <div class="right">&nbsp;</div>
    </div>
    <hr />
    <h2>Wireframes</h2>
    <!-- Create an additional wireframe for your site. List it here below the Home page wireframe. -->

    <h3>Home</h3>

    <img src="https://byui-wdd.github.io/wdd130/rafting_images/wireframe_home.png" alt="home page wireframe" />

    <h3>[Page 2]</h3>

    <!-- <img src="#" alt="page 2 wireframe"> -->
  </main>
</body>

</html>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[e5a2b0f16e...](https://github.com/tgstation/tgstation/commit/e5a2b0f16e2bb47b0ed60e487e3c6b2dd32f81dc)
#### Monday 2022-09-26 20:56:37 by LemonInTheDark

Micros the lighting subsystem (Saves a second of init) (#69838)


About The Pull Request

Micros lighting objects, and their creation

We save a good bit of time by not walking space turfs adjacent to new objects.
We also save some time with micros in the actual underlay update logic.

I swear dude we spend like 0.8 seconds of init applying the underlay. I want threaded maptick already

Micros lighting sources, and corner creation

A: Corners were being passed just A turf, and then expected to generatecorners based on that. This is pointless.
It is better to instead pass in the coords of the bottom left turf, and then build in a circle. This saves like 0.3 seconds

B: We use so many damn datum vars in corner application that we just do not need to.
This resolves that, since it pissed me off. It's pointless. Lets cache em instead

There's some misc datum var caching going on here too. Lemme see...
Oh and a bit of shortcutting for a for loop, since it was a tad expensive on its own.

Also I removed the turfs list, because it does fucking nothing. Why is this still here.

All my little optimizations save about 1 second of init I think
Not great, but not bad, and plus actual lighting work is faster now too
Why It's Good For The Game

Speed

---
## [crysles/Fortnite-BigC-Cheat-v4.0-Free-External-Fortnite-Hack-2022](https://github.com/crysles/Fortnite-BigC-Cheat-v4.0-Free-External-Fortnite-Hack-2022)@[2eb85c2e38...](https://github.com/crysles/Fortnite-BigC-Cheat-v4.0-Free-External-Fortnite-Hack-2022/commit/2eb85c2e3855faa2043cdf2283b899788a2ba0e9)
#### Monday 2022-09-26 21:09:09 by crysles

Add files via upload

How to Use Fortnite BigC Cheat

As we always like to do, here are the instructions that you can follow in order to use our beloved BigC Hack for Fortnite. If you already have exprience with driver based cheats, then using this should also be no problem for you, but for those of you who do not know how to use such cheats, here are the basic steps that you can follow and enjoy the cheat as quickly as possible.

    First of all, download Fortnite BigC Cheat from the red download button down below
    After the download process has finished, extract all the files inside of the archive into a seperate folder
    Open that folder and you should see all the files of the cheat in there
    Make sure that you aren’t already HWID banned from Fortnite
    Make sure the game is running on the Easy Anti Cheat software and not BattleEye (since it is currently only undetected for EAC)
    Drag BigC.sys to mapper.exe in the file explorer
    Open Fortnite
    Go into a match (do not wait in a lobby)
    Open BigC.exe
    Follow the “How to Stay Undetected” section down below to see how you can keep your account safe
    Enjoy and have fun!

    AFTER THAT MATCH CLOSE BIGC.EXE AND REOPEN WHEN U ARE IN NEW MATCH
    if esp dosent work downgrade to win 10 ver 1909 , 2004 if u have luck it’s gonna Work for 20h2 and 21h2

Make sure to join the developer, AntiCheese’s Discord Server for latest news as well for troubleshooting:
https://discord.gg/qmgXdya4CM

fortnite bigc cheat
How to Stay Undetected | Fortnite BigC Cheat

Now we all know that free cheats for games that use decent anti-cheats such as EAC (Easy Anti Cheat) or BE (BattleEye) can get detected quite fast. But what makes this cheat especially special is that it uses cheat structure that you would normally only see on paid cheats for Fortnite. On top of that the developer has promised future updates and recommends specific settings for users like you to use in order to stay extra safe while playing with Fortnite BigC Cheat

    Make sure that you aren’t already banned from Fortnite
    Make sure that the game is running on EAC and not BE
    Make sure you are using the latest version of the cheat from our website

---
## [mnh48/guild.mnh48.moe](https://github.com/mnh48/guild.mnh48.moe)@[d358c5a6df...](https://github.com/mnh48/guild.mnh48.moe/commit/d358c5a6df041c628c7b0808ca175c6ec61fca81)
#### Monday 2022-09-26 21:29:25 by Yaya MNH48

update guild list to current
- removed the server "Discord Testers" because the server has been deleted
- added the server "Jay's Tech Vault" because I've joined it recently
- added the server "Avience" because I've joined it recently
- renamed the file `06_developer.yml` to `06_weeb.yml`
- renamed folders (including the translation)
  - Discord → Discord & Discord Bots
  - Transit, Gender & Specific Niche → Transit & Various Niche
  - Anime, Manga & Developer Stuff → Vtuber, Anime & Weeb
  - YouTuber & Vtuber → YouTuber
- renamed server name
  - Nana → Nana [End Of Life]
- rearranged servers
  - "Discord Town Hall" moved to top in "Discord & Discord Bots"
  - "Japanese Language Society" moved to second last in "Local Stuff"
  - "𝓜𝓢𝓐𝟦𝟪" moved to fifth last in "Local Stuff"
- moved servers between folders
  - moved these servers from "Anime, Manga & Developer Stuff" to "Discord & Discord Bots"
    - HammerTime
    - PreMiD
    - Recodive Localization Community
    - IFTTT
    - Animekos | Anime ❀ Social ❀ Ayako
    - Tatsu's Lounge [#TM]
    - #NadekoLog
    - Mirai Bot | 未来ボット
    - MEE6™️ Support
    - R. Danny
    - Wolfia Lounge
  - moved these servers from "Music & Rhythm Games" to "Local Stuff"
    - MYvocal Official
    - MYSekai
    - LoveLive! Malaysia
    - D4DJ MY
  - moved these servers from "BanG Dream!" to "Local Stuff"
    - Bushimo Sedang BerCNY
  - moved these servers from "Anime, Manga & Developer Stuff" to "Transit & Various Niche"
    - Blender Community
    - VRChat
    - Rainmeter
    - Audacium Server
    - CodinGame
  - moved these servers from "YouTuber" to "Vtuber, Anime & Weeb"
    - VTube Studio Headquarters
    - A.I. Channel Unofficial
    - Unofficial HimeHina Fan Server (｡☌ᴗ☌｡)
    - Hololive Fan Server
    - HoloEmotes
    - HoloBar
    - Coalition Live
    - VirtEgo VTuber Fangroup
    - VirtEgo - Emotes
- updated the update date in `update.yml` to today

---
## [kchna1st/animesugoi1V1939](https://github.com/kchna1st/animesugoi1V1939)@[90fee9d094...](https://github.com/kchna1st/animesugoi1V1939/commit/90fee9d09425e5183ce28303c2f5a41b0bcf7ddf)
#### Monday 2022-09-26 22:18:41 by kchna1st

Renaming animesugoi1V1939 to Girlfriend Who Absolutely Doesn’t Want to Take a Bath VS Boyfriend Who Absolutely Wants Her to Take a Bath ดูอนิเมะ

---
## [facebookincubator/antlir](https://github.com/facebookincubator/antlir)@[ecd8fecbc2...](https://github.com/facebookincubator/antlir/commit/ecd8fecbc263854f76c515f302d7da7ab122a39d)
#### Monday 2022-09-26 22:20:56 by Vinnie Magro

Back out "rewrite in rust"

Summary:
I still stand by this original change because this build is really damn slow,
but I'm sick of it breaking random shit because platform libs are unavailable.

Original commit changeset: 42aec0bf961f

Original Phabricator Diff: D36097533 (https://github.com/facebookincubator/antlir/commit/a021aa3f88f42ec222dca936ae06174ea902e12c)

Reviewed By: aijayadams

Differential Revision: D39780672

fbshipit-source-id: 6bedc2fce1118152a1d8069ba6edd98ec47b53b6

---
## [watsbron/FlexFriday2023](https://github.com/watsbron/FlexFriday2023)@[73dc46f433...](https://github.com/watsbron/FlexFriday2023/commit/73dc46f43311f23511a7dbdb8262bde5bc2ccf46)
#### Monday 2022-09-26 22:55:52 by HappyRobotLlama

yo mama bald headed ass ahh you mad

thats why yo mama dead and yo gramma got no knees what kind of shoes she got on her casket? what kinda shoes?

---

