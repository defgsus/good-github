## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-06-04](docs/good-messages/2023/2023-06-04.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,778,180 were push events containing 2,623,290 commit messages that amount to 151,348,678 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 46 messages:


## [GrishaVar/rust](https://github.com/GrishaVar/rust)@[6e48dcf77f...](https://github.com/GrishaVar/rust/commit/6e48dcf77f3a078e3e9d28c3571a8def01e60863)
#### Sunday 2023-06-04 01:10:07 by Nilstrieb

Rollup merge of #111607 - jyn514:clubby-reviews, r=clubby789

Add clubby789 to the bootstrap review rotation

r? `````@clubby789````` - thank you for volunteering!

I have been meaning for a very long time now to write up how to do reviews, but I haven't gotten around to it yet :( here is a short summary:

1. If you're not sure what the changes does or if it's ok, always feel free to ping someone else on the team, especially in the first few weeks. You can use `r? bootstrap` to get triagebot to assign someone else.
2. Bootstrap unfortunately has very few tests. Things that touch CLI or toml parsing should likely have a test in `src/bootstrap/config/tests.rs`; things that touch "core" build logic should have a test in `builder/tests.rs`, anything else kinda just slips in :( see https://github.com/rust-lang/rust/issues/102563 for ideas on how to improve the situation here.
3. "Major" changes should be documented in `src/bootstrap/CHANGELOG.md`. "Major" is up to you, but if it breaks a config option or otherwise is likely to break *someone's* build, it's probably major. If it breaks nearly *everyone*'s build, it should also update `VERSION` in `lib.rs`; this should be very rare. Please also ping me or Mark-Simulacrum for major changes (I might set up a triagebot ping for this so you don't have to remember).
4. Once you've approved the PR, tell bors it's ok - you've been contributing for a while so you know how bors works, but here's a cheatsheet just in case: https://bors.rust-lang.org

Documentation about how to use bootstrap lives at https://rustc-dev-guide.rust-lang.org/building/bootstrapping.html; internal docs live in `src/bootstrap/README.md`. The latter unfortunately is not very complete.

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[18fe422bf6...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/18fe422bf6ee150a50f375c28d2c43db2465bfac)
#### Sunday 2023-06-04 01:37:23 by SkyratBot

[MIRROR] makes snow legions from portals drop skeletons (like tendril legions) [MDB IGNORE] (#21589)

* makes snow legions from portals drop skeletons (like tendril legions) (#75707)

## About The Pull Request
Exactly what it says on the tin (snow legions only dropping ashen
skeletons, like tendril legions).

Also changes the name of the "fromtendril" variable to "from_spawner",
and comments it. Not sure if that warrants a changelong comment, but
I'll go ahead and assume no.

## Why It's Good For The Game
being able to farm snow legion portals for an endless tide of bodies
and/or equipment is a bit weird. also puts it a bit more in line with
the legions of Lavaland

## Changelog

:cl:
balance: The source of the demonic portals that endlessly deposits snow
legions onto the Icemoon no longer preserves the bodies nor gear of the
damned (read: demon portal snow legions now only drop skeletons).
/:cl:

---------

Co-authored-by: Hatterhat <Hatterhat@ users.noreply.github.com>

* makes snow legions from portals drop skeletons (like tendril legions)

---------

Co-authored-by: Hatterhat <31829017+Hatterhat@users.noreply.github.com>
Co-authored-by: Hatterhat <Hatterhat@ users.noreply.github.com>

---
## [RatFromTheJungle/Skyrat-tg](https://github.com/RatFromTheJungle/Skyrat-tg)@[7dad8c75ca...](https://github.com/RatFromTheJungle/Skyrat-tg/commit/7dad8c75cac06a405dc3c30a5cbc31919f33ff13)
#### Sunday 2023-06-04 01:39:19 by SkyratBot

[MIRROR] Adds a eye-dropper right-click function to the painting canvas. [MDB IGNORE] (#21411)

* Adds a eye-dropper right-click function to the painting canvas. (#75571)

## About The Pull Request
Having used the painting UI to kill some time during long rounds for a
decent chunk of the past year, the need of a quicker and less tedious
way to fix a misclick or mistake like drawing over the wrong pixel has
become clear to me, as well as getting some feedback on the palette
component I made last year.

As the title suggests, this PR adds an eye-dropper function to the
canvas. Right-Click a pixel on the canvas, and the painting tool will
copy its color. Simple as, works on both finished and unfinished
paintings.

As a bonus, you can also right-click one of those selectable
white/colored squares on the color scheme near the bottom of the UI (if
using spraycan/palette) to change its color without having to go back to
main game window and a radial menu.

EDIT: With the tooltip added to the UI, I can say it's ready.

## Why It's Good For The Game
This PR aims to add better options to change colors on the go and
improve the user experience on the painting UI.

## Changelog

:cl:
qol: Adds a eye-dropper-like right-click function to the painting canvas
UI. Right-Click a pixel on the canvas while holding a painting tool to
have it copy its color.
qol: Also adds a right-click function to the color palette at the bottom
of the UI to allow users to set its colors without having to alternate
between the game window and the UI.
qol: Lastly, a tooltip has been added near the top-left corner of the
same UI to let players know of these features.
/:cl:

* Adds a eye-dropper right-click function to the painting canvas.

---------

Co-authored-by: Ghom <42542238+Ghommie@users.noreply.github.com>

---
## [diphons/sdm845](https://github.com/diphons/sdm845)@[1b3777732c...](https://github.com/diphons/sdm845/commit/1b3777732cb78b890f19e84a7b886ebc971e372d)
#### Sunday 2023-06-04 01:57:29 by Maciej Żenczykowski

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

---
## [heidongxianhua/pytorch](https://github.com/heidongxianhua/pytorch)@[b5840f99c3...](https://github.com/heidongxianhua/pytorch/commit/b5840f99c3f2ae01b7831fd32b99758180fc22c3)
#### Sunday 2023-06-04 02:26:26 by Mark Saroufim

torch.compiler public namespace (#102182)

# torch.compiler public API

## Goal

The goal of this document is to describe the public facing API for torchdynamo and torchinductor.

Today both dynamo and torchinductor are in `torch/_dynamo` and `torch/_inductor` namespace with the only public function

`torch.compile()` which is directly placed in `torch/__init__.py`

This poses a few problems for users trying to take dependencies on PyTorch 2.0
1. Unclear BC guarantees
2. No builtin discovery mechanism outside of reading the source code
3. No hard requirements for docstrings or type annotations

Most importantly it mixes two personas the PyTorch 2.0 developer vs the PyTorch 2.0 customer so this is an attempt to address this. We draw a lot of inspiration from the `functorch` migration to the `func` namespace.

## Alternate names

We did discuss some other alternative names

1. `torch.compile` -> problem is this would break BC on the existing `torch.compile` function
2. `torch.dynamo` -> `dynamo` is so far not something we've deliberately hidden from users but problem is now figuring out what it's `_dynamo` vs `dynamo` might be confusing
3. `torch.compiler` -> 1 would be better but to keep BC this is a good compromise

# The general approach
## Proposal 1
In https://github.com/pytorch/pytorch/blob/main/torch/_dynamo/__init__.py

We have function called `reset()`, this function is essential if users are trying to `torch.compile()` a model under different settings

```python
# in _dynamo/
def reset():
    do_reset_stuff()
```

Instead we propose

```python
# in compiler/
def reset():
    do_reset_stuff() # As in copy paste the logic from _dynamo.reset

# in _dynamo/
import warnings
import inspect

def reset():
    function_name = inspect.currentframe().f_code.co_name
    warnings.warn(f"{function_name} is deprecated, use compiler.{function_name} instead", DeprecationWarning)
    return compiler.reset()

```
## Proposal 2

```python
# in compiler/
def reset():
    “””
    Docstrings here
    “””
    _dynamo.reset()

# in _dynamo/
No changes
```
Consensus so far seems to be proposal 2 since fewer warnings will be less jarring and it’ll make it quite easy to merge the public API

## Docstrings

The above was an example of a function that has no inputs or outputs but there are other functions which could use an improvement in their docstrings, for example allow_in_graph actually works over lists of functions but that’s not mentioned anywhere in the example only if you read the source code.

def allow_in_graph(fn):
    """
    Customize which functions TorchDynamo will include in the generated
    graph. Similar to `torch.fx.wrap()`.

    Parameters:
        fn (callable or list/tuple): The function(s) to be allowed in the graph.

    Returns:
        callable or list/tuple: The input function(s) included in the graph.

    Examples:
        Customize inclusion of a single function:
        ::
            torch._dynamo.allow_in_graph(my_custom_function)

        Customize inclusion of multiple functions:
        ::
            torch._dynamo.allow_in_graph([my_custom_function1, my_custom_function2])

        @torch._dynamo.optimize(...)
        def fn(a):
            x = torch.add(x, 1)
            x = my_custom_function(x)
            x = torch.add(x, 1)
            return x

        fn(...)

    Notes:
        The `allow_in_graph` function allows customization of which functions TorchDynamo
        includes in the generated graph. It can be used to include specific functions that
        are not automatically captured by TorchDynamo.

        If `fn` is a list or tuple, `allow_in_graph` will be called recursively on each
        element in the sequence.

        Once a function is allowed in the graph using `allow_in_graph`, it will be captured
        in the graph generated by TorchDynamo. This customization enables more fine-grained
        control over the functions included in the graph.

        Note that `allow_in_graph` expects the input `fn` to be a callable.

    """
    if isinstance(fn, (list, tuple)):
        return [allow_in_graph(x) for x in fn]
    assert callable(fn), "allow_in_graph expects a callable"
    allowed_functions._allowed_function_ids.add(id(fn))
    allowed_functions._disallowed_function_ids.remove(id(fn))
    return fn

So to make the API public, we’d have to write similar docstrings for all public functions we’d like to create.

The benefit of this approach is that
1. No BC risks, internal and external users relying on our tooling can slowly wean off the private functions.
2. We will also have to write correct docstrings which will automatically make our documentation easier to maintain and render correctly on pytorch.org
3. We already have some BC guarantees already, we don’t kill OptimizedModule, we rejected the PR to change the config system

The con of this approach is that
Will be stuck with some potentially suboptimal functions/classes that you can’t kill

## Testing strategy
If the approach is to mostly make a public function call an already tested private function then all we need to do is ensure that the function signatures don't change

## Which functions should be in the public API

Our heuristic for deciding whether something should be public or not is are users already relying on it for lack of other options or have we recommended some non public functions for users to debug their PT 2.0 programs.

Heuristic for not putting something in public is that it’s an experimental subsystem with the goal of turning it on by default, it’s very core dev centric, meta centric, a bunch of different configs that should be batched into a single user facing one, or something that needs to be renamed because the name is confusing

#### Top level
`torch.compile()` -> already is a public API it does require some minor improvements like having configs be passed in to any backend and not just inductor (EDIT: This was already done https://github.com/pytorch/pytorch/pull/99645l) and renaming `mode=reduce-overhead` to `mode=cudagraph`

To make sure that PT 2.0 is supported with a given pytorch version users can create a new public function and this would replace the need for `try/except` blocks around `import torch._dynamo` that has been populating user code.

```python
def pt2_enabled():
    if hasattr(torch, 'compile'):
        return True
    else:
        return False
```

For all of the below they will be translated to `torch.compiler.function_name()`

#### From _dynamo

As a starting point we looked at https://github.com/pytorch/pytorch/blob/main/torch/_dynamo/__init__.py and we suggest redefining these functions in `pytorch/torch/compiler/__init__.py`

It might also make sense to split them over multiple files and import them in `__init__.py` but because the number of functions is small it'd probably be fine to add them all into a single compiler/__init__.py until this list becomes larger

1. `reset()`
2. `allow_in_graph()`
10. `list_backends()`
12. `compile()`:  torch.compile() would be mostly a shell function passing arguments to torch.compiler.compile()
13. `assume_constant_result()`: TODO: Double check how this is useful
15. `torch._dynamo.disable()`

Some notable omissions
11. `explain()`: We need to clean up the output for this function, make it a data class and pretty printable
1. `forbid_in_graph()`: Considered adding this but should instead consolidate on `disallow_in_graph`
2. `optimize_assert()`: Already covered by `torch.compile(fullgraph=True)`
3. `check_if_dynamo_supported()`: this would be supplanted by pt2_enabled()
4. `compilation_metrics`, `graph_breaks_reasons` ..: would all be accessed via `torch.compiler.explain()`
5. `replay` does not seem useful to end customers
6. . `graph_break()`: Mostly useful for debugging or unit tests
9. `register_backend()`: End users will just pass a string backend to torch.compile, only devs will create new backends
10. `export()` : Eventually this needs to public but for now it’s not ready so just highlighting that it will be in the public API eventually
11. `disallow_in_graph()`: Usage is limited
12. `mark_static()`: we can keep this private until dynamic=True is recommended in stable
13. `mark_dynamic()`:  we can keep this private until dynamic=True is recommended in trunk
14. 8. `OptimizedModule`: This is the only class that we'd expose but is crucial since users are running code like `if isinstance(mod, OptimizedModule): torch.save(mod._orig_mod)` EDIT: because we fixed pickling we no longer need to
expose this
15. `is_compiling()`: Still not clear how this useful to end users

There are also config variables which we need to expose https://github.com/pytorch/pytorch/blob/main/torch/_dynamo/config.py

Some of our configs are useful dev flags, others are to gate experimental functionality and others are essential debugging tools and we seperate out the essential debugging and logging tools to a public facing config.

TODO: I still need to think of a good way of porting the config in a BC way here are some ideas
1. Just make all passes available and controllable via `torch.compile(options={})` but only show docstrings for the ones users should care about.

The current problem with our config system is we have 3 ways of setting them once via `options={}`, environment variables and variables in `config.py`, it'd be worth settling on one source of truth and have that be the public API.

The configs we should make public are
1. `log_file_name`
2. `verbose`
3. `cache_size_limit`
4. `repro_level` and `repro_after`: Although we can rename these to minifier and give human readable names to the levels

Everything else should stay private in particular

1. `print_graph_breaks`, `print_specializations`: should be supplanted by `explain()` for public users
2. dynamic shape configs : Users should only have to worry about `torch.compile(dynamic=True/False)`
3. The distributed flags, hook or guard configs: If we tell a user to use FSDP and DDP then the flag should be enabled by default or be in a private namespace
4. The fbcode flags: Obviously no need to be user facing
5. Skip/Allow lists: Not something normal users should play around with

#### From _inductor
Very little of inductor should be exposed in a public facing API, our core audience as in people writing models mostly just need information on what certain passes mean and how to control them a high level and they can do this with `torch.compile(options={})` so the goal here should be more to make available passes clearer and ideally consolidate them into `torch.compile()` docstrings or modes.

There are some exceptions though from https://github.com/pytorch/pytorch/blob/main/torch/_inductor/__init__.py

1. `list_mode_options()`
2. `list_options()`: this needs an additional pass to hide internal or debug options

For both of these we’d rename them to compiler.inductor_list_mode_options and compiler.inductor_list_options() since they would be in the same init file as the one for dynamo

Notable omissions
1. `_inductor.compile()`: Because of users are coming in with their own fx graph, they are likely developers
2. `_inductor.aot_compile()`:Again this is about capturing and modifying fx graphs so users APIs don't need to be public

However the configs are a slightly different story, because we can choose to either
1. Make all configs public
2. Make some configs public and keep most of the private ones. If public config is set it should override the private version
3. Make all configs controllable via `torch.compile(options={})` but make list_options() hide more things

For now 3 seems like the most reasonable choice with some high level configs we’ll keep like TORCH_COMPILE_DEBUG

Regardless here's what should probably be public or advertised more
1. `disable_progress` and verbose_progress:  Combine and enable by default
2. `fallback_random`: We could make the case this shouldn't be public if a top level deterministic mode enables this
3. `profile_bandwidth`: Or could make the case that this should be in TORCH_COMPILE_DEBUG

Notable omissions
1. Any config that would generally improve performance for most that we should probably enable by default but might be disabled in the short term because of stability: example `epilogue_fusion`, `pattern_matcher`, `reordering`
2. Autotuning flags: Should just sit behind `torch.compile(mode="max-autotune")` like `max_autotune`, `max_autotune_gemm`
3. `coordinate_descent_tuning`: This one I'm a but mixed about, maybe it just also fall into `mode="max-autotune"`
4. `trace`: `TORCH_COMPILE_DEBUG` is the best flag for all of this
5. `triton.cudagraphs`: Default should be `torch.compile(mode="reduce-overhead")` - I'd go further and rename the `mode=cudagraph` and we can keep reduce-overhead for BC reasons
6. `triton_unique_kernel_names`: Mostly useful for devs debugging
7. `dce`: which doesnt really do anything
8. `shape_padding`: Elias is working on enabling this by default in which case we also remove it

## Mechanics

This PR would include the public functions with their docstrings

Another PR will take a stab at the configs

And for work where the APIs are still being cleaned up whether its minifier or escape hatches, export or dynamic shapes, aot_inductor etc.. we’ll keep them private until a public commitment can be made

Pull Request resolved: https://github.com/pytorch/pytorch/pull/102182
Approved by: https://github.com/jansel

---
## [rd-stuffs/android_kernel_xiaomi_surya](https://github.com/rd-stuffs/android_kernel_xiaomi_surya)@[816aa9e584...](https://github.com/rd-stuffs/android_kernel_xiaomi_surya/commit/816aa9e5844bc4043f3a40ad9bfe50f4e10626cd)
#### Sunday 2023-06-04 02:33:02 by Wang Han

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
## [Lineage-Fork/android_frameworks_base](https://github.com/Lineage-Fork/android_frameworks_base)@[ff7bb4f20e...](https://github.com/Lineage-Fork/android_frameworks_base/commit/ff7bb4f20ed6358b576ef051b4006f687ac7b2d6)
#### Sunday 2023-06-04 02:43:33 by Kuba Wojciechowski

[SQUASHED] core: Blacklist pixel system feature from Google Photos

    We want to include the P21 experience flag to enable new features,
    however it seems like Google Photos uses it to decide whether to use the
    TPU tflite delegate. There doesn't seem to be any fallback so we need to
    make sure the feature is not exposed to the app so that a normal
    NNAPI/GPU delegate can be used instead.

    Test: Google Photos editor with PIXEL_2021_EXPERIENCE feature in product
    Signed-off-by: Kuba Wojciechowski <nullbytepl@gmail.com>
    Change-Id: I51a02f8347324c7a85f3136b802dce4cc4556ac5

commit 67eb31b3bb43d06fcc7f6fdb2f92eb486451cae6
Author: kondors1995 <normandija1945@gmail.com>
Date:   Thu Jun 9 17:39:25 2022 +0530

    Core: Extend Pixel experience Blacklist For Google Photos

    Turns out having these brakes Original quality backups.
    Since these indicate that the device is pixel 4 with in the turn brakes device spoofing as OG pixel

    Change-Id: I336facff7b55552f094997ade337656461a0ea1d

commit 508a99cde60b73dc3f1e843d569bca31def35988
Author: ReallySnow <reallysnow233@gmail.com>
Date:   Fri Dec 31 16:40:23 2021 +0800

    base: core: Blacklist Pixel 2017 and 2018 exclusive for Google Photos

    * In this way can use PixelPropsUtils to simulate the Pixel XL prop
      method to use the unlimited storage space of Google Photos
    * Thanks nullbytepl for the idea

    Change-Id: I92d472d319373d648365c8c63e301f1a915f8de9

commit aaf07f6ccc89c2747b97bc6dc2ee4cb7bd2c6727
Author: Akash Srivastava <akashniki@gmail.com>
Date:   Sat Aug 20 19:04:32 2022 +0700

    core: Pixel experience Blacklist For Google Photos for Android 13

    * See, in Android 13 pixel_experience_2022_midyear was added, which needs to be blacklisted aswell

    Change-Id: Id36d12afeda3cf6b39d01a0dbe7e3e9058659b8e

commit 9d6e5749a988c9051b1d47c11bb02daa7b1b36fd
Author: spezi77 <spezi7713@gmx.net>
Date:   Mon Jan 31 19:17:34 2022 +0100

    core: Rework the ph0t0s features blacklist

    * Moving the flags to an array feels more like a blacklist :P
    * Converted the flags into fully qualified package names, while at it

    Signed-off-by: spezi77 <spezi7713@gmx.net>
    Change-Id: I4b9e925fc0b8c01204564e18b9e9ee4c7d31c123

commit d7201c0cff326a6374e29aa79c6ce18828f96dc6
Author: Joey Huab <joey@evolution-x.org>
Date:   Tue Feb 15 17:32:11 2022 +0900

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

Change-Id: Iffae2ac87ce5428daaf6711414b86212814db7f2

---
## [ABJ4403/Payback2_CHEATus](https://github.com/ABJ4403/Payback2_CHEATus)@[d21d68c338...](https://github.com/ABJ4403/Payback2_CHEATus/commit/d21d68c3383b9bb7f00f0bdb39f5bda25a3e9b23)
#### Sunday 2023-06-04 03:36:55 by MDP43140

Update Pb2Chts

Pb2Chts v2.4.4:
+ Reflection Graphics is now called Reflective Texture.
+ improved gg.clearList codes (now it shouldn't spam gg.removeListItems repetitively).
+ Removed result count logging (because it can drop performance).
+ Add the build version each script is designed for in the about section.
+ [138] Remove annotation on very top (to make it synced with build 121 code structure).
+ [138] Replaced ErrNotFound_Report to ErrNotFound (ig there may be lots of "not found" problem, and too many people report the same issue, when im trying to solve some of it).
+ [138] Find entity anchor auto anchor method (and related) now works (i removed memory address filtering codes) although still with some quirks (some inaccuracies, dupes, not work in vehicles).
+ [138] Fixed matchBackendAnchor (fixes Floodspawn and partially XP).
+ [138] Fixed Floodspawn Auto respawn offset (it should work just like before)
+ [138] Fixed Autoshoot (now it should work)
+ [138] Fixed shadow cheat not found (apparently its just a really tiny typo, changing `,` to `.` fixed everything, god damn weird gameguardian number formatting...).

PS:
+ The script designed for latest version 138 actually is almost ready to use, just need to fix couple quirkiness, and reflective texture cheat values need to be reworked.
+ This commit might took long time to get pushed to main branch, but i really want to make sure everything works.

---
## [Addust/Yogstation](https://github.com/Addust/Yogstation)@[bfe9ec955d...](https://github.com/Addust/Yogstation/commit/bfe9ec955de5da5432f71c9908becefbe6a85b9f)
#### Sunday 2023-06-04 04:33:32 by Addust

OH MY FUCKING GOD YOU EVEN PUT THEM IN THE HOLODECK

---
## [DATA-xPUNGED/DataStation](https://github.com/DATA-xPUNGED/DataStation)@[dff70625e7...](https://github.com/DATA-xPUNGED/DataStation/commit/dff70625e7c29616887619dacc0375ddc84f0708)
#### Sunday 2023-06-04 04:36:04 by ChungusGamer666

Bible refactor (#75350)

## About The Pull Request

This started as a simple addition where burning a bible would curse you,
but then I realized... Bibles aren't even proper books, thus can't be
burned!
So yeah, since that is not necessary due to how atom_storage works, I
reworked that.

## Why It's Good For The Game

Because burning bibles and getting cursed for it is funny.

![image](https://github.com/tgstation/tgstation/assets/82850673/2a8489ce-ecd6-45ee-9eb9-168ff820af65)

![image](https://github.com/tgstation/tgstation/assets/82850673/ebe98ad6-2d0d-4d20-9ea1-5d472d6ca465)

## Changelog

:cl:
add: You can burn bibles now! But heresy has a steep cost...
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [Apogee-dev/Shiptest](https://github.com/Apogee-dev/Shiptest)@[00b8761853...](https://github.com/Apogee-dev/Shiptest/commit/00b8761853eabc6d73073cce4708dc71d402539c)
#### Sunday 2023-06-04 05:27:50 by Apogee-dev

Slays the Lamia (#1974)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

Removes the Lamia in its entirety.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

The Lamia is awkwardly-mapped, inconsistent with the current lore (in as
much as wizard lore is even established at this point), and most
damningly, it's a magnet for new players, often ones with an LRP bent.
The ship itself encourages wizard RP, yes, but frankly, wizard RP is not
the kind of RP we necessarily want here. I'd rather new players' first
experience on this server involved actually interacting with the faction
lore in at least some measure.

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
del: Removed the Lamia-class wizard ship
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Apogee-dev/Shiptest](https://github.com/Apogee-dev/Shiptest)@[c20b961685...](https://github.com/Apogee-dev/Shiptest/commit/c20b961685c78760ab807c95a2e79fe72ee4d507)
#### Sunday 2023-06-04 05:35:44 by thgvr

Elementizes and Greyscales blood decals/overlays (#1882)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
This PR converts our blood decals to elements, and adds greyscale
capability to blood, tied to species DNA.
Ports:
https://github.com/BeeStation/BeeStation-Hornet/pull/3111
https://github.com/BeeStation/BeeStation-Hornet/pull/3046
https://github.com/tgstation/tgstation/pull/61610
https://github.com/tgstation/tgstation/pull/59873
https://github.com/tgstation/tgstation/pull/59315
https://github.com/tgstation/tgstation/pull/53109

Some others, I don't quite remember. Mostly related fixes for those PRs.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

Decals as a component is a cause of some lag, apparently. This should
alleviate some if it's even noticeable.

Species having a framework for unique, greyscale blood colors can add a
lot for our lore and visual feel.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: Elzu now bleed, but do not have Liquid Electricity reagent as
blood. (will be changed in the future)
add: IPCs now "bleed" by leaking coolant
add: Sarathi now have teal-colored blood.
add: Blood will now dry over time
add: New bloody footprint sprites from bay
refactor: Refactors a lot of blood code
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Signed-off-by: thgvr <81882910+thgvr@users.noreply.github.com>
Co-authored-by: Mark Suckerberg <mark@suckerberg.gay>

---
## [smfr/WebKit](https://github.com/smfr/WebKit)@[d6ae2528a9...](https://github.com/smfr/WebKit/commit/d6ae2528a9f3819005e08f9d5091ceff8b880fa8)
#### Sunday 2023-06-04 06:09:46 by Dean Jackson

WebXR: Severe aliasing in WebXR experiences (with WebGL1 contexts)
https://bugs.webkit.org/show_bug.cgi?id=256861
rdar://109424254

Reviewed by Dan Glastonbury.

WebXR sessions using WebGL1 contexts are unable to turn on
multisampling. I'm pretty sure this was my fault, but I can't
remember if it was intentional or a mistake. Either way it is
a bug.

Fix this by implementing the multisample renderbuffer creation
and resolution steps. Since we're doing this on a WebGL1 context,
the normal API will be invalid (it requires GLES3), so call the
extension API instead. This means we need to expose some extra methods
on GraphicsContextGL.

Lastly, the framebuffer textures we get are SRGB8_ALPHA8 which
requires an extension to be enabled with a WebGL1 context when
we're talking to an XR-compatible context. Similarly, we
enable the extension to allow multisampled framebuffers.

* Source/WebCore/Modules/webxr/WebXROpaqueFramebuffer.cpp:
(WebCore::WebXROpaqueFramebuffer::endFrame): call blitFramebufferANGLE.
(WebCore::WebXROpaqueFramebuffer::setupFramebuffer): Implement logic for WebGL 1.
* Source/WebCore/platform/graphics/GraphicsContextGL.h:
* Source/WebCore/platform/graphics/angle/GraphicsContextGLANGLE.cpp: Implement the extension API/
(WebCore::GraphicsContextGLANGLE::renderbufferStorageMultisampleANGLE):
(WebCore::GraphicsContextGLANGLE::blitFramebufferANGLE):
* Source/WebCore/platform/graphics/angle/GraphicsContextGLANGLE.h:
* Source/WebCore/platform/graphics/cocoa/GraphicsContextGLCocoa.mm:
(WebCore::GraphicsContextGLCocoa::platformInitialize): Turn on the sRGB extension.
* Source/WebKit/GPUProcess/graphics/RemoteGraphicsContextGL.messages.in:
* Source/WebKit/GPUProcess/graphics/RemoteGraphicsContextGLFunctionsGenerated.h:
(renderbufferStorageMultisampleANGLE):
(blitFramebufferANGLE):
* Source/WebKit/WebProcess/GPU/graphics/RemoteGraphicsContextGLProxy.h:
* Source/WebKit/WebProcess/GPU/graphics/RemoteGraphicsContextGLProxyFunctionsGenerated.cpp:
(WebKit::RemoteGraphicsContextGLProxy::renderbufferStorageMultisampleANGLE):
(WebKit::RemoteGraphicsContextGLProxy::blitFramebufferANGLE):

Canonical link: https://commits.webkit.org/264838@main

---
## [JGreenlee/e-mission-phone](https://github.com/JGreenlee/e-mission-phone)@[9a53f9d4db...](https://github.com/JGreenlee/e-mission-phone/commit/9a53f9d4dbbf934cd4aacf9725ee4deaf3c18787)
#### Sunday 2023-06-04 07:27:49 by Jack Greenlee

use local tz to prefill enketo time fields

Enketo doesn't allow time inputs to use any timezone other than the user's current local timezone. It's frustrating for our purposes, but Enketo makes sure whatever the user sees is reflected in their local time.
We previously had added a hack in our copy of the Enketo code to get around this (https://github.com/e-mission/e-mission-phone/commit/0f1051f469cd1bc68e4133e459fb92ef04cdb8e3). It worked ok, but since we're tidying + upgrading dependencies I want to avoid hacking Enketo if possible.
I think the best thing we can do here is just give Enketo what it wants - a timestamp in the current local tz offset - and then sort things back out when we resolve the timestamps upon survey completion.
So `resolveTimestamps()` is just going to ignore the tz offsets in the the survey response and instead use the timezone that it gets from the trip/place.
This works because all we really need is the HH:mm value the user entered in each field. We don't care at all what timezone the user was in when they recorded the activity.

---
## [Bubberstation/Bubberstation](https://github.com/Bubberstation/Bubberstation)@[410979bb6a...](https://github.com/Bubberstation/Bubberstation/commit/410979bb6af8b1ccfb840dee0461867724714912)
#### Sunday 2023-06-04 08:36:34 by SkyratBot

[MIRROR] Microing var/static times (~0.015 seconds of init) [MDB IGNORE] (#20688)

* Microing var/static times (~0.015 seconds of init) (#74769)

## About The Pull Request

Moth and I came up with an affront to god and man, and used it to track
the time spent creating /static (and in theory /global) variables (this
happens right at the start of init)
They cost as a sum about 0.05 seconds btw, at least currently.

```
/datum/timer
    var/key

/datum/timer/New(file, line)
    src.key = "[file]:[line]"

/datum/timer/proc/operator*(x)
    rustg_time_reset(key)
    return x

/datum/timer/proc/operator+(x)
    var/time = rustg_time_microseconds(key)
    world.log << "TIMER: [key]: [time]"
    return x

Regex:
var/static/([\w/]+) =
-> var/static/$1 = (new /datum/timer(__FILE__, __LINE__)) * (new /datum/timer(__FILE__, __LINE__)) +
```

Output on moth's pc looks like this, time in microseconds

[output_sorted.csv](https://github.com/tgstation/tgstation/files/11241900/output_sorted.csv)

Most of this is either icon_states() memes (which appears to be cached
btw, that's interesting), or a variation on typecacheof()
There is one get_asset_datum call, but that is ALREADY cached and so is
just redundant. That's a good 0.01 seconds saved.

The rest of the time here is slightly more interesting.

The majority of typecacheof() is iterating the output of typesof(), a
byond internal proc that returns a list of types that either are or are
the child of the passed in type.
A decent chunk of time here (0.005 seconds, or 10% of the proc) can be
saved by unrolling the arguments to the proc.
It takes an arbitrary amount of typepaths as input, but we can't like
use arglist() here (cause this is an internal "proc"), so instead we try
a window of args, passing in null if we start to try and take in too
much.
Window size matters, zebra fits better into 4 then 5, especially because
of how grouping needs to work to make this effect happen.
We save about 0.001 for zebra btw, which is around about 7%. It's lower
cause we need to group the paths beforehand I think.

The speedup is minor, but it DOES exist. Plus it's fun.

## Why It's Good For The Game

Microing is a hell of a drug

* Microing var/static times (~0.015 seconds of init)

---------

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [GeoB99/reactos](https://github.com/GeoB99/reactos)@[2feb37d744...](https://github.com/GeoB99/reactos/commit/2feb37d7447e6476a04c15ba5a537d68ee7784cd)
#### Sunday 2023-06-04 09:29:59 by George Bișoc

[SDK][CMLIB] Implement log transaction writes & Resuscitation

=== DOCUMENTATION REMARKS ===

This implements (also enables some parts of code been decayed for years) the transacted writing of the registry. Transacted writing (or writing into registry in a transactional way) is an operation that ensures the successfulness can be achieved by monitoring two main points.
In CMLIB, such points are what we internally call them the primary and secondary sequences. A sequence is a numeric field that is incremented each time a writing operation (namely done with the FileWrite function and such) has successfully completed.

The primary sequence is incremented to suggest that the initial work of syncing the registry is in progress. During this phase, the base block header is written into the primary hive file and registry data is being written to said file in form of blocks. Afterwards the seconady sequence
is increment to report completion of the transactional writing of the registry. This operation occurs in HvpWriteHive function (invoked by HvSyncHive for syncing). If the transactional writing fails or if the lazy flushing of the registry fails, LOG files come into play.

Like HvpWriteHive, LOGs are updated by the HvpWriteLog which writes dirty data (base block header included) to the LOG themselves. These files serve for recovery and emergency purposes in case the primary machine hive has been damaged due to previous forced interruption of writing stuff into
the registry hive. With specific recovery algorithms, the data that's been gathered from a LOG will be applied to the primary hive, salvaging it. But if a LOG file is corrupt as well, then the system will perform resuscitation techniques by reconstructing the base block header to reasonable values,
reset the registry signature and whatnot.

This work is an inspiration from PR #3932 by mrmks04 (aka Max Korostil). I have continued his work by doing some more tweaks and whatnot. In addition to that, the whole transaction writing code is documented.

=== IMPORTANT NOTES ===

HvpWriteLog -- Currently this function lacks the ability to grow the log file size since we pretty much lack the necessary code that deals with hive shrinking and log shrinking/growing as well. This part is not super critical for us so this shall be left as a TODO for future.

HvLoadHive -- Currently there's a hack that prevents us from refactoring this function in a proper way. That is, we should not be reading the whole and prepare the hive storage using HvpInitializeMemoryHive which is strictly used for HINIT_MEMORY but rather we must read the hive file block by block
and deconstruct the read buffer from the file so that we can get the bins that we read from the file. With the hive bins we got the hive storage will be prepared based on such bins. If one of the bins is corrupt, self healing is applied in such scenario.

For this matter, if in any case the hive we'll be reading is corrupt we could potentially read corrupt data and lead the system into failure. So we have to perform header and data recovery as well before reading the whole hive.

Another important note is that the added code grew up the binary size of x64 FreeLdr and that makes a PE image check fail because the bootloader is too large. Currently such code is disabled for AMD64, until
a real fix comes into place.

---
## [Bobbanz1/NSV-Rat](https://github.com/Bobbanz1/NSV-Rat)@[fc1471c818...](https://github.com/Bobbanz1/NSV-Rat/commit/fc1471c8187d3f2a49d75a8a5c3e1b610fec45d3)
#### Sunday 2023-06-04 10:28:57 by SkyratBot

[MIRROR] Deadchat Announcement Variety Pack 1 [MDB IGNORE] (#20957)

* Deadchat Announcement Variety Pack 1 (#75140)

## About The Pull Request

Adds announce_to_ghosts()/notify_ghosts() calls to a bunch of different
things.

**THIS INCLUDES:**
- Powersink being activated/reaching critical (explosion) heat capacity.
- His Grace being awoken.
- Hot Potatoes being armed.
- Ascension Rituals being completed.
- Eyesnatcher victims.
- Ovens exploding as a result of the Aurora Caelus event.
- Wizard Imposter spawns.
- Rock-Paper-Scissors with death as the result of Helbital consumption.
- BSA impact sites.
- Spontaneous Appendicitis.
- The purchasing of a badass syndie balloon.
- The Supermatter beginning to delaminate.

This was everything that I could think of that would be worth announcing
to deadchat. These were all chosen with consideration to questions like
"how easy would it be to spam deadchat with this?" and "will observers
actually see the interesting thing happen, or just the aftermath?".

Not gonna lie, I've really become an observer main as of recently. Maybe
that's being reflected in my recent PRs. Who's to say? Deadchat
Announcement Variety Pack 2 will probably never come out. Sorry.
## Why It's Good For The Game

Gives deadchat a better indiciation of when/where something **REALLY
FUNNY** is about to happen. Draws attention to certain things that are
likely to gather an audience anyways, but sooner (for your viewing
pleasure). In simple terms, it helps the observers observe things
better.

Some cases, such as the aurora caelus or helbitaljanken, are occurrences
so rare that they deserve the audience.
## Changelog
:cl: Rhials
qol: Observers now recieve an alert when a powersink is activated/about
to explode.
qol: His Grace being awoken now alerts observers, to give you a
headstart on your murderbone ghost ring.
qol: Ascension Rituals being completed will also alert observers, for
basically the same reason.
qol: Arming a hot potato will now alert observers. Catch!
qol: Eyesnatcher victims will now notify observers, and invite them to
laugh at their state of misery and impotence.
qol: Observers will be notified of any acute references to The Simpsons
or other 20th Television America copyright properties.
qol: Wizard Imposter spawns alert observers, much like any other ghost
role event should.
qol: Playing Rock-Paper-Scissors with death will now alert the observers
and invite them to watch. Better not choke!
qol: Observers now get an orbit link for BSA impact sites. Why does it
keep teleporting me to the AI upload??
qol: Spontaneous Appendicitis now alerts deadchat.
qol: The purchasing of a badass syndie balloon now alerts deadchat. You
might not be any more powerful, but at least you have an audience.
qol: When beginning to delaminate, the Supermatter will alert observers
and invite them to watch the fireworks.
/:cl:

* Deadchat Announcement Variety Pack 1

---------

Co-authored-by: Rhials <Datguy33456@gmail.com>

---
## [bakebrain/evals](https://github.com/bakebrain/evals)@[e116ede848...](https://github.com/bakebrain/evals/commit/e116ede848957eff8e76b5d8463ed5291163a28f)
#### Sunday 2023-06-04 11:42:24 by Wesley Barlow

Add eval: rhetorical-devices (#1005)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, pelase note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑
### Eval name
rhetorical-devices

### Eval description

Evaluates model's ability to select the most specific rhetorical
modification of a sentence from a multiple choice with a large number of
nuanced rhetorical devices.

### What makes this a useful eval?

Useful for using LLMs to write novels and generate consistent/parametric
authorial tone.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content":"Which of the following
rhetorical devices was added to the original sentence? Choose the most
specific of the following (a) Alliteration, (b) Assonance, (c)
Consonance, (d) Cacophony, (e) Onomatopoeia, (f) Anadiplosis, (g)
Conduplicatio, (h) Anaphora, (i) Epistrophe, (j) Symploce, (k)
Epanalepsis, (l) Epizeuxis, (m) Antanaclasis, (n) Diacope, (o)
Antithesis, (p) Antimetabole, (q) Chiasmus, (r) Asyndeton, (s)
Polysyndeton, (t) Catacosmesis, (u) Oxymoron, (v) Zeugma"}, {"role":
"user", "content": "ORIGINAL She likes to listen to the winds. MODIFIED
She swoons at such sweet gales. Answer in the format (x) Rhetorical"}],
"ideal": "(a) Alliteration"}
{"input": [{"role": "system", "content":"Which of the following
rhetorical devices was added to the original sentence? Choose the most
specific of the following (a) Alliteration, (b) Assonance, (c)
Consonance, (d) Cacophony, (e) Onomatopoeia, (f) Anadiplosis, (g)
Conduplicatio, (h) Anaphora, (i) Epistrophe, (j) Symploce, (k)
Epanalepsis, (l) Epizeuxis, (m) Antanaclasis, (n) Diacope, (o)
Antithesis, (p) Antimetabole, (q) Chiasmus, (r) Asyndeton, (s)
Polysyndeton, (t) Catacosmesis, (u) Oxymoron, (v) Zeugma"}, {"role":
"user", "content": "ORIGINAL The rock was very large. MODIFIED The rock
was remarkably raised. Answer in the format (x) Rhetorical"}], "ideal":
"(a) Alliteration"}
{"input": [{"role": "system", "content":"Which of the following
rhetorical devices was added to the original sentence? Choose the most
specific of the following (a) Alliteration, (b) Assonance, (c)
Consonance, (d) Cacophony, (e) Onomatopoeia, (f) Anadiplosis, (g)
Conduplicatio, (h) Anaphora, (i) Epistrophe, (j) Symploce, (k)
Epanalepsis, (l) Epizeuxis, (m) Antanaclasis, (n) Diacope, (o)
Antithesis, (p) Antimetabole, (q) Chiasmus, (r) Asyndeton, (s)
Polysyndeton, (t) Catacosmesis, (u) Oxymoron, (v) Zeugma"}, {"role":
"user", "content": "ORIGINAL Visionary dreams elevate me at night.
MODIFIED Visionary reminitions elevate self resting in lightlessness.
Answer in the format (x) Rhetorical"}], "ideal": "(b) Assonance"}
{"input": [{"role": "system", "content":"Which of the following
rhetorical devices was added to the original sentence? Choose the most
specific of the following (a) Alliteration, (b) Assonance, (c)
Consonance, (d) Cacophony, (e) Onomatopoeia, (f) Anadiplosis, (g)
Conduplicatio, (h) Anaphora, (i) Epistrophe, (j) Symploce, (k)
Epanalepsis, (l) Epizeuxis, (m) Antanaclasis, (n) Diacope, (o)
Antithesis, (p) Antimetabole, (q) Chiasmus, (r) Asyndeton, (s)
Polysyndeton, (t) Catacosmesis, (u) Oxymoron, (v) Zeugma"}, {"role":
"user", "content": "ORIGINAL Once, I thought I had lost her pet.
MODIFIED Once, dunce — thought I lost Juliet's pet. Answer in the format
(x) Rhetorical"}], "ideal": "(b) Assonance"}
{"input": [{"role": "system", "content":"Which of the following
rhetorical devices was added to the original sentence? Choose the most
specific of the following (a) Alliteration, (b) Assonance, (c)
Consonance, (d) Cacophony, (e) Onomatopoeia, (f) Anadiplosis, (g)
Conduplicatio, (h) Anaphora, (i) Epistrophe, (j) Symploce, (k)
Epanalepsis, (l) Epizeuxis, (m) Antanaclasis, (n) Diacope, (o)
Antithesis, (p) Antimetabole, (q) Chiasmus, (r) Asyndeton, (s)
Polysyndeton, (t) Catacosmesis, (u) Oxymoron, (v) Zeugma"}, {"role":
"user", "content": "ORIGINAL Do you want to understand research on
artificial general intelligence? MODIFIED Don't you want to investigate
artifacts of artificial general intelligence? Answer in the format (x)
Rhetorical"}], "ideal": "(c) Consonance"}
  ```
</details>

---
## [bakebrain/evals](https://github.com/bakebrain/evals)@[b91292c803...](https://github.com/bakebrain/evals/commit/b91292c803af2bdadeec3853ab03514b73310109)
#### Sunday 2023-06-04 11:42:24 by Zyenith

Add Eval: Internal Representations via Counting (#1006)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑
### Eval name
Internal representations via counting

### Eval description

Using series of logical questions that require multiple (simple)
manipulations of numbers to get the ideal answer. These are basic tasks
that should be doable by an LLM, but require several steps of internal
"thought" to get right.

### What makes this a useful eval?

Situations with number manipulation with multiple steps are prevalent
anywhere in the modern world. Testing the internal representation of the
LLM can provide other insights on how well its "mind" processes
information.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

This eval is capable of providing insight into the LLM's internal
representation of objects versus answering fact-based questions or
straightforward complex logic puzzles.

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input":[{"role":"system","content":"You will be prompted with a
logical question. Respond only with a number, nothing else is
required."},{"role":"user","content":"Roger and Emily are in a room.
Roger puts a cat in an empty box while Emily is in the room. They both
leave, and Emily returns and puts a turtle in the box as well. How many
items does Roger think are in the box?"}],"ideal":"1"}
{"input":[{"role":"system","content":"You will be prompted with a
logical question. Respond only with a number, nothing else is
required."},{"role":"user","content":"There are four darts already on a
dart board. Bob throws one dart at the dartboard, and it lands. Alice
throws two darts, and one misses but one hits the dartboard. How many
darts are on the dartboard?"}],"ideal":"6"}
{"input":[{"role":"system","content":"You will be prompted with a
logical question. Respond only with a number, nothing else is
required."},{"role":"user","content":"A bakery sold 25 cakes in the
morning and 17 cakes in the afternoon. The day after, they sold 15 more
cakes. How many cakes did they sell on the second day?"}],"ideal":"15"}
{"input":[{"role":"system","content":"You will be prompted with a
logical question. Respond only with a number, nothing else is
required."},{"role":"user","content":"There are six blue birds and three
red birds sitting on a tree. Two blue birds fly away, and one red bird
flies away. How many birds are left on the tree?"}],"ideal":"6"}
{"input":[{"role":"system","content":"You will be prompted with a
logical question. Respond only with a number, nothing else is
required."},{"role":"user","content":"John has double the amount of
pencils than Sarah, and Sarah has as many pencils as Mark. Mark has 2
pencils. How many pencils does John have?"}],"ideal":"4"}
  ```
</details>

---
## [bakebrain/evals](https://github.com/bakebrain/evals)@[3d9de9a624...](https://github.com/bakebrain/evals/commit/3d9de9a62411f9e6a999e96ce8f07eebf0e8c121)
#### Sunday 2023-06-04 11:42:24 by dyar-al-ashtari

Eval Norwegian lexicon (#1044)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑
### Eval name
`norwegian-lexicon`

### Eval description

This eval uses valid Norwegian words taken from the dictionary and
assesses whether GPT can recognize them as valid.

### What makes this a useful eval?

The Norwegian language is simple yet complicated at the same time. There
are a lot of words that are valid Norwegian words that do not get
recognized anymore. An AI should be able to identify these words with
precision. All of the words used in the samples are valid Norwegian
words and can be found in the dictionary. After assessing GPT-4 (through
the playground) and GPT-3.5 -- it failed to recognize most of the words.
Some of the words would return positive during some evals. Other times
it wouldn't recognize them. After asking GPT why it is not a valid word,
it would apologize and fix its mistake.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input":[{"role":"system","content":"You will be prompted with a single
word. Does this word exist in the Norwegian language? Answer with
exactly one letter: Y or N. Do not use punctionation. Do not explain
your answer."},{"role":"user","content":"Skarpne"}],"ideal":"Y"}
{"input":[{"role":"system","content":"You will be prompted with a single
word. Does this word exist in the Norwegian language? Answer with
exactly one letter: Y or N. Do not use punctionation. Do not explain
your answer."},{"role":"user","content":"Bløtne"}],"ideal":"Y"}
{"input":[{"role":"system","content":"You will be prompted with a single
word. Does this word exist in the Norwegian language? Answer with
exactly one letter: Y or N. Do not use punctionation. Do not explain
your answer."},{"role":"user","content":"Hovedantall"}],"ideal":"Y"}
{"input":[{"role":"system","content":"You will be prompted with a single
word. Does this word exist in the Norwegian language? Answer with
exactly one letter: Y or N. Do not use punctionation. Do not explain
your answer."},{"role":"user","content":"Klenge"}],"ideal":"Y"}
{"input":[{"role":"system","content":"You will be prompted with a single
word. Does this word exist in the Norwegian language? Answer with
exactly one letter: Y or N. Do not use punctionation. Do not explain
your answer."},{"role":"user","content":"Blankolov"}],"ideal":"Y"}
  ```
</details>

---
## [bakebrain/evals](https://github.com/bakebrain/evals)@[6a37c9b51b...](https://github.com/bakebrain/evals/commit/6a37c9b51b48a2f735898846cfb08b37cbd63179)
#### Sunday 2023-06-04 11:42:24 by Aaron Goldsmith

[eval] 3x3 Game Of Life  (#345)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. We encourage partial PR's with
~5-10 example that we can then run the evals on and share the results
with you so you know how your eval does with GPT-4 before writing all
100 examples.

## Eval details 📑
### Eval name
GOL

### Eval description

Determine the next state of a 3x3 Game of Life Board. 

### What makes this a useful eval?

Spacial reasoning

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "You are a helpful assistant.
"}, {"role": "user", "content": "Using the classic Game of Life Rules,
determine the next state of the 3x3 Game of life board: \n1 1 1\n\n0 0
0\n\n0 0 0 \n\n Do not provide any explanation other than the next state
of the board. e.g 0 0 0\n\n0 0 0\n\n0 0 0"}], "ideal": ["0 1 0\n\n0 1
0\n\n0 0 0"]}
{"input": [{"role": "system", "content": "You are a helpful assistant.
"}, {"role": "user", "content": "Using the classic Game of Life Rules,
determine the next state of the 3x3 Game of life board: \n1 1 1\n\n1 0
0\n\n0 0 0 \n\n Do not provide any explanation other than the next state
of the board. e.g 0 0 0\n\n0 0 0\n\n0 0 0"}], "ideal": ["1 0 1\n\n1 0
1\n\n0 0 0"]}
{"input": [{"role": "system", "content": "You are a helpful assistant.
"}, {"role": "user", "content": "Using the classic Game of Life Rules,
determine the next state of the 3x3 Game of life board: \n0 1 1\n\n1 1
1\n\n1 1 0 \n\n Do not provide any explanation other than the next state
of the board. e.g 0 0 0\n\n0 0 0\n\n0 0 0"}], "ideal": ["1 0 1\n\n0 0
0\n\n1 0 1"]}
{"input": [{"role": "system", "content": "You are a helpful assistant.
"}, {"role": "user", "content": "Using the classic Game of Life Rules,
determine the next state of the 3x3 Game of life board: \n0 1 1\n\n0 1
1\n\n0 0 0 \n\n Do not provide any explanation other than the next state
of the board. e.g 0 0 0\n\n0 0 0\n\n0 0 0"}], "ideal": ["0 1 1\n\n0 1
1\n\n0 0 0"]}
{"input": [{"role": "system", "content": "You are a helpful assistant.
"}, {"role": "user", "content": "Using the classic Game of Life Rules,
determine the next state of the 3x3 Game of life board: \n0 1 0\n\n0 0
0\n\n1 1 0 \n\n Do not provide any explanation other than the next state
of the board. e.g 0 0 0\n\n0 0 0\n\n0 0 0"}], "ideal": ["0 0 0\n\n1 1
0\n\n0 0 0"]}
  ```
</details>

---
## [MTandi/tgstation](https://github.com/MTandi/tgstation)@[57ef596898...](https://github.com/MTandi/tgstation/commit/57ef596898a5a3932db33389baa9fab3164d430a)
#### Sunday 2023-06-04 14:15:58 by LemonInTheDark

Admin Library Moderation (in-game edition) (#75645)

For the longest time, the only way admins could moderate the library was
by using statbus's external tool.
But a few months back statbus went down, and ever since then they've
been sitting lost. Shit sucks.

The whole external thing has been bugging me for a while, so let's fix
all that yeah?

This pr adds a new verb to the admin tab that allows admins to
ban/restore books from the library.
It includes expanded (ckey) search, faster response times, in tool book
viewing with and without markdown rendering, and viewing of deleted
books.

This is accomplished with a special subtype of library consoles, stored
on the admin datum.
It shouldn't let you do anything without +BAN, rip my live debugging or
whatever.

I've also hooked into (and fixed) Ned's existing library actions log,
and added viewing support to the ban/restore pages.
This logs banning admin, ban time, ban reason, etc.

As a part of this, I've fixed/expanded on the existing UIs.
I've added ID search to all existing consoles, and fixed an existing bug
with the visitor console not supporting category search (shows how many
people actually use the thing)

Changes to the library_action table were pretty minor. The ckey column
was too small, so longer keys just caused it to fail on ban. Bad.
That and the ip address column was signed, which wasted space and was
non standard with other tables.

---
## [Abhi-Tekavade/RetroGames](https://github.com/Abhi-Tekavade/RetroGames)@[25a49ec10b...](https://github.com/Abhi-Tekavade/RetroGames/commit/25a49ec10bae2753306f3921551619baeb3e9de6)
#### Sunday 2023-06-04 14:28:33 by Abhishek Tekavade

Add files via upload

Our project, Retro Games, is an online gaming platform that holds a special place in my heart. As a team of passionate gamers and web developers, we have come together to create an appealing and interactive website that offers a nostalgic experience for users. We wanted to bring back the joy and memories of the classic retro games that were popular in the early 2000s.

The main objective of Retro Games is to provide a touch of nostalgia to the generation that grew up playing these games, as well as introduce the new generation to the magic of retro gaming. Our website features a wide collection of beloved childhood games, including timeless classics like Pac-Man and Pong. We carefully selected games that do not require high memory space or graphic specifications, making them accessible to all PC owners.

---
## [system-zero/system-zero](https://github.com/system-zero/system-zero)@[8b622d2df2...](https://github.com/system-zero/system-zero/commit/8b622d2df2ee140803d811aeb624878c147b96e9)
#### Sunday 2023-06-04 14:33:10 by why not yet another not

This is an upolished first language code that succesfully builds with own libc.

However, though it is the same (almost) code, modules should be included at the
building time, as we've failed hard with the dynamic load code that we've tried
hard, so there is no dlopen() and friends and i'm afraid that i don't know what
and how to do it. Maybe if time allows and refound my lost courrage, to go back
and steel hard an exact copy of musl or even glibc, otherwise i don't know.

Commited also an exact copy of the old tests without the import tests, that it
passes them all, except the known failure on the double type operation.

A fisrt benchmark with those two versions, shows a serious decrease in terms of
performance, when running those tests with the executable that is using our own
libc (around 7++ times slower, even with a optimization in the memory interface
(when we preallocate space at the initialization), but this was expected though
it could have been better, as there is no way to compete with the overoptimized
code written, during the last 30++ years of the glibc evolution, by C experts).

Nonetheless seems that is a kind of a special point, as we walk the development
path, as we can do now to use from point zero++ (compiler & linker) inner tools
to produce a very tiny system that can be expanded quickly to do at least basic
machine administration.

But also, and in my humble opinion, it is the first language that i know of that
is independent. And without to be that... poor, on the contrary i believe. It is
both expressive with nice and simple imho syntax, with a rich set of datatypes.

Anyway what we want from it, it is to be the glue and drive C to bind an endless
in quantity and quality C universe (even if we could freeze the time with a way,
there is unimaginable material anyway, and of course is and our product, that it
can be the source and a referenche itself - if it was in eighties i bet it could.

---
## [MTandi/tgstation](https://github.com/MTandi/tgstation)@[2068ea9ab5...](https://github.com/MTandi/tgstation/commit/2068ea9ab53803557b5e48cddbe57205f4c4792e)
#### Sunday 2023-06-04 14:43:05 by SyncIt21

Crate, Closet Refactors & Access Secured Stuff  (#74754)

## About The Pull Request
This PR is actually 2 parts, one that fixes runtimes with crates & the
other that allows secured closets to be crafted
along with a secured suit storage unit

**Crate Fixes**

Fixes #74708

The problem starts here

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/crates.dm#L31-L34
Not only does this if condition look ugly but it's highly error prone
because one single call to `update_appearance()` can cause this to fail,
and sure enough if you look at the parent `Initialize()` proc it calls
just that

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/closets.dm#L81-L88
Since we know the appearance is guaranteed to be changed in some way
before the if condition gets executed let's check what the final state
of the crate would be before this if check

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/crates.dm#L54-L56
We see that the final icon state depends on the variable `opened` so if
we want to place/spawn a crate that is opened at round start we have to
ensure that `opened = TRUE` so the `if(icon_state ==
"[initial(icon_state)]open")` succeeds and does its job correctly.
Sadly we did dum shit like this
```
/obj/structure/closet/crate{
	icon_state = "crateopen"
}
```
throughout the entire code base, we thought backwards and were only
concerned in making the closet look open rather than setting its correct
variables to actually say that it is opened. because none of these
crates actually set `opened = TRUE` the final icon state becomes just
"crate" NOT "crateopen" therefore the if condition fails and we add the
component

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/crates.dm#L36-L37
with the wrong parameters, so when closing the closet after_close()
removes the component with the wrong arguments

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/crates.dm#L81-L84
that is does not unregister the signals and readds the component i.e.
re-registers the signals causing runtime.

The solution just do this
```
/obj/structure/closet/crate/open[mapping helper]
```
To clearly state that you want the closet to be open, that way you don't
have to memorize the icon_state for each different type of crate, it's
consistent across all crates & you don't get runtimes.

And that's exactly what i did everywhere

Another issue that is fixed is "Houdini crates" i.e. crates which are
open & appear empty but when you close & reopen them magical loot
appears, Go ahead walk upto to cargo and find any empty crate that is
open and do this

Fixes #69779


https://user-images.githubusercontent.com/110812394/232234489-0193acde-22c8-4c19-af89-e897f3c23d53.mp4

You will be surprised, This is seriously harmful to players because they
can just walk by a crate that appears to be open & empty only to realize
later that it had some awesome loot. Just mean

The reason this happens is because of the Late Initialization inside
closets

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/closets.dm#L85-L86

What late initialization does is suck up all stuff on its turf

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/closets.dm#L97-L100

In theory this is supposed to work perfectly, if the closet is closed
move everything on the turf into the closet and so when the player opens
it, they all pop back out.
But what happens if the closet is opened before ` LateInitialize()` is
called? This breaking behaviour is caused by object spawners

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/effects/spawners/random/structure.dm#L94-L100
And maint crates

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/crates.dm#L141-L143
These 2 spawners open up the crate based on random probability before `
LateInitialize()` is called on the crate and so what happens is the
crate is first opened and then stuff on the turf is sucked in causing an
open but empty crate to appear.

The solution is simple just check again in ` LateInitialize()` if our
crate is still closed before we proceed.That's fixed now too

**Code Refactors**
1. Introduced 2 new signals COMSIG_CLOSET_PRE/POST CLOSE which are the
counter parts for the open signals. hook into them if you ever need to
do stuff before & after closing the closet while return BLOCK_CLOSE for
COMSIG_CLOSET_PRE_CLOSE if you want to block closing the closet for some
reason
2. 2 new procs `before_open()` & `before_close()` which are the counter
parts for `after_open()` & `after_close()`. If you need to write checks
and do actions before opening the closet or before closing the closet
override these procs & not the `open()` & `close()` procs directly

**Secured Craftables** 
This is just a reopened version of #74115 after i accidently merged
another branch without resolving the conflicts first so i'll just
repaste everything here, since crates & closets are related might as
well do all in one

1. **Access secured closets**
   
   - **What about them?**
          **1. Existing System**
If you wanted to create a access secured closet with the existing system
its an 4 step process
            - First construct a normal closet
            - Weld it shut so you can install the airlock electronics
            - Install the electronics [4 seconds]
            - Unweld
This is a 4 step process which takes time & requires a welding tool
         **2. New system**
Combine the 4 steps into 1 by crafting the secure closet directly
                    
![Screenshot
(184)](https://user-images.githubusercontent.com/110812394/235904926-c2ea231c-eba7-45d0-a5af-e0456fdd40bc.png)

    - **Bonus Features**
              **1. Card reader**
The card reader acts as an interface between the airlock electronics &
the player. Usually if you want to change access on a locker you have to
                  - Weld the closet shut
                  - Screw driver out the electronics
                  - Change the settings
                  - Install it back
                  - Unweld
With a card reader there is no need of a welder & screwdriver. You can
change the access of the locker while its operational

        **How do i install the card reader?**
             1. Weld the closet shut
             3. Insert card reader with hand
4. To remove the card reader use crowbar or just deconstruct the whole
closet with a welding tool
             5. Unweld closet

         **How to change its access?**
This will overwrite the settings on your airlock electronics. To do this
1. make sure the closet is first unlocked. This is important so that no
random person who doesn't have access to the closet can change its
access while its locked. It would be like giving the privilege of
changing your current password without first confirming if you know the
old password
2. attack/swipe the closet with your PDA. Make sure your ID card is
inside the PDA for this to work. You can also just use your ID card
directly without a PDA
         3. You will get 3 options to decide the new access levels
           
![Screenshot
(174)](https://user-images.githubusercontent.com/110812394/233454364-d99a2fb6-9f26-4db3-9fac-a10689955484.png)


        They work as follows
- **Personal**: As the name implies only you can access this locker and
no one else. Make sure to have your ID on you at all times cause if you
loose it then no one can open it
- **Departmental**: This copies the access levels of your ID and will
allow people having those exact same access levels. Say you want to
create a closet accessible to only miners. Then have an miner choose
this option and now only miners can open this closet. If the Hop sets
custom access on your ID then only people with those specific access
levels can open this closet
         - **None**: No access, free for all just like a normal closet

**Security:** After you have set the access level it is important to
lock the access panel with a "multi-tool", so no one else can change it.
Unlock the panel again with the "multi-tool" to set the new access type

       **2. Give your own name & description**
To rename the closet or change its description you must first make the
closet access type as personel i.e. make it yours, then use an pen to
complete the job. You cannot change names of departmental or no access
closets because that's vandelism

       **3. Custom Paint Job**
    Use airlock painter. Not intuitive but does the job. 
   
![Screenshot
(181)](https://user-images.githubusercontent.com/110812394/234202905-00946b88-2513-489d-b0a2-d618a72f3e49.png)

      **4. Personal closets**
Round start personal closets can have their access overridden by a new
ID when in it's unlocked state. This is useful if the last person has no
use for the closet & someone else wants to use it.


    - **Why its good for the game?**      
1. Having your own personal closet with your own name & description
gives you more privacy & security for your belongings so people don't
steal your stuff. Personal access is more secure because it requires you
to have the physical ID card you used to set this access and not an ID
which has the same access levels as your previous ID
2. Make secure closets faster without an welding tool & screw driver
3. Bug fix where electronics could be screwed out from round start
secured closets countless times spawning a new airlock electronic each
time
      
2. **Access secured freezers**

    - **What about them?**
The craftable freezer from #73942 has been modified to support secure
access. These can be deconstructed with welders just as before

![Screenshot
(185)](https://user-images.githubusercontent.com/110812394/235905000-ba165feb-4384-4759-b46b-dba77c9e6ba3.png)


    - **How does it work?**
The access stuff works exactly the same as secure closets described
above. You can rename & change description with pen just like the above
described secure closets. No paint job for this. Install card reader
with the same steps described above.

    - **Why it's good for the game?**
1. Make access secured freezers faster without a welder and screwdriver
2. Your own personally named & locked freezer for storing dead bodies is
always a good thing

4. **Access secured suit storage unit**
   - **What about them?**
Suit storage units now require airlock electronics for construction. The
access levels you set on it will be used to decide
       1. If a player can unlock the unit
       2. If the player can open the unit after unlocking
       3. If the player can disinfect whatever is inside
       
      By default all round start suit storage units have free access

   - **Install card reader**
Provides the same functionality as secured closets described above. To
install it
     1. Open its panel with a screw driver
     2. Add a card reader to it with hand
     3. Close the panel
     
     When you deconstruct the machine the card reader pops back out

   - **Why it's good for the game?**
1. Having your own access protected and named suit storage unit so
random people don't steal your mod suits? Who wouldn't want that.?
Provides security for department storage units.
2. If you have the unit locked then you cannot deconstruct the machine
with a crowbar providing additional security
3. Fixes #70552 , random people can't open/unlock the suit storage unit
without access. You can set personal access to make sure only you can
access the unit

## Changelog
:cl:
add: Access secured closets. Personal closets can have their access
overwritten by an new id in it's unlocked state
add: Access secured freezers.
add: Access secured suit storage units.
fix: Suit storage unit not having access restrictions.
fix: airlock electronics not properly getting removed after screwing
them out from round start lockers
fix: round spawned open crates run timing when closed
fix: open crates hiding stuff in plain sight
fix: open closets/crates sucking up contents during late initialize
causing them appear empty & open
/:cl:

---------

Co-authored-by: Tim <timothymtorres@gmail.com>

---
## [9014314380/Free_](https://github.com/9014314380/Free_)@[0d76740e90...](https://github.com/9014314380/Free_/commit/0d76740e907cd1dc78e9122e960b10079b225fc9)
#### Sunday 2023-06-04 15:32:14 by Shaik

Update README.md

<!DOCTYPE html>
<html lang="en">

    <head>
        <!-- <link rel="icon" href="favicon.ico.png" type="image/x-icon"> -->
        <meta charset="UTF-8">
        <link rel="Shortcut Icon"type="images/x-icon" href="images/favicon.ico.png" >
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="description" content="This website is amazing for android phones very helpfull, Free gain the followers and some Phones Tips & Tricks After applied the website links work in 24 hours real work this website is Google approval Thanks have a Nice Day">
        <meta name="keywords" content="All Apps Followers Links Android phones Tips & Tricks ">
        <title>Free Followers Links</title>
        <style>
            *{
                margin: 0;
                padding: 0;
            }
            body {
                background-image: url(https://coolbackgrounds.io/images/backgrounds/index/sea-edge-79ab30e2.png);
                background-position: contain;
                background-repeat: no-repeat;
                background-size: cover;
            }

            .container {
                color: rgb(255, 8, 0);
                text-align: center;
                /* pointer-events: painted; */
            }
            #foot{
                background-color: red;
                text-align: center;
            }
            #main{
                text-align: center;
            }
            p{
                color: black;
            }
            a{
                font-size: 25px;
                font-family:'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
                border: 1px solid black;
                border-radius: 55px;
                /* width: 55px; */
                padding: 7px;
                text-decoration: none;
                
            }
            h1{
                font-size: 35px;
                font-family:'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
            }
            a:link{
                background-color: rgb(228, 170, 228);
            }
            #foot{
                font-size: 20px;
            }

            
        </style>
    </head>

    <body>
        <nav>
            <header>
                <h1 align=center> Everything Gain any Apps</h1><br>
                <div class="container">
                    <ol>
                        <li align="center" value="1">
                                <div><img src="https://freepngimg.com/thumb/logo/69768-logo-computer-layout-instagram-icons-png-file-hd.png" alt="Instagram" width="100px"></div>
                                <p>Instagram[a] is a photo and video sharing social networking service owned by American company Meta Platforms. The app allows users to upload media that can be edited with filters and organized by hashtags and geographical tagging. Posts can be shared publicly or with preapproved followers. Users can browse other users' content by tag and location, view trending content, like photos, and follow other users to add their content to a personal feed.[7]</p>
                                <a href=https://Social-gr.in/insta.php?id=6124352151
                                target="_blank">Instagram
                                Followers</a>
                            </li><hr><br>
                        <li value="2">
                            <div><img src="https://seeklogo.com/images/S/snapchat-logo-F20CDB1199-seeklogo.com.png" alt="Snap" width="100px"></div>
                            <p>Snapchat is an American multimedia instant messaging app and service developed by Snap Inc., originally Snapchat Inc. One of the principal features of Snapchat is that pictures and messages are usually only available for a short time before they become inaccessible to their recipients. The app has evolved from originally focusing on person-to-person photo sharing to presently featuring users' "Stories" of 24 hours of chronological content, along with "Discover", letting brands show ad-supported short-form content. It also allows users to store photos in a password-protected area called "my eyes only". It has also reportedly incorporated limited use of end-to-end encryption, with plans to broaden its use in the future.</p>
                            <a href="https://Social-gr.in/snap.php?id=6124352151">Snap Sticks</a>
                        </li><hr><br>
                        <li value="3">
                            <div><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Facebook_Logo_%282019%29.png/1200px-Facebook_Logo_%282019%29.png" alt="Facebook" width="100px"></div>
                            <p>Facebook is an online social media and social networking service owned by American technology giant Meta Platforms. Created in 2004 by Mark Zuckerberg with fellow Harvard College students and roommates Eduardo Saverin, Andrew McCollum, Dustin Moskovitz, and Chris Hughes, its name derives from the face book directories often given to American university students. Membership was initially limited to only Harvard students, gradually expanding to other North American universities and, since 2006, anyone over 13 years old. As of December 2022, Facebook claimed 2.96 billion monthly active users,[6] and ranked third worldwide among the most visited websites.[7] It was the most downloaded mobile app of the 2010s.[8]</p>
                            <a href="https://Social-gr.in/face.php?id=6124352151">Facebook Followers</a>
                        </li><hr><br>
                        <li>
                            <div><img src="https://s3.envato.com/files/253601194/Preview%20Image.jpg" alt="Premium" width="170px"></div>
                            <p>Freemium, a portmanteau of the words "free" and "premium", is a pricing strategy by which a basic product or service is provided free of charge, but money (a premium) is charged for additional features, services, or virtual (online) or physical (offline) goods that expand the functionality of the free version of the software.[1][2] This business model has been used in the software industry since the 1980s. A subset of this model used by the video game industry is called free-to-play.</p>
                            <a href="https://Social-gr.in/snap.php?id=6124352151">Free Premium</a>
                        </li><hr><br>
                        <li>
                            <div><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/WhatsApp.svg/2044px-WhatsApp.svg.png" alt="WhatsApp" width="125px"></div>
                            <p> Whatsapp Particular Person Can't be Open & see the Messages Whose Send this Message to Some One</p>
                            <a href="wa.me/settings">wa.me/settings</a>
                        </li><hr><hr><br>
                    </ol>
                </div>
            </header>
        </nav>
        <main id="main">
            <h1>Phone Tricks</h1><br>
            <div id="Container1">
                <ol>
                    <li>
                        <div><img src="https://img.freepik.com/premium-vector/pin-symbol-indicates-location-gps-map_68708-398.jpg?w=2000" alt="WhatsApp" width="100px"></div>
                        <p>A myriad of tracking systems exists. Some are 'lag time' indicators, that is, the data is collected after an item has passed a point for example a bar code or choke point or gate.[1] Others are 'real-time' or 'near real-time' like Global Positioning Systems (GPS) depending on how often the data is refreshed. There are bar-code systems which require items to be scanned and automatic identification (RFID auto-id). For the most part, the tracking worlds are composed of discrete hardware and software systems for different applications. That is, bar-code systems are separate from Electronic Product Code (EPC) systems, GPS systems are separate from active real time locating systems or RTLS for example, a passive RFID system would be used in a warehouse to scan the boxes as they are loaded on a truck - then the truck itself is tracked on a different system using GPS with its own features and software.[2] The major technology “silos” in the supply chain are:</p>
                        <a href="https://social-logs.com/r/?id=JlwqTV">Location Track Anyone</a>
                    </li><hr><br>
                    <li>
                        <div><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/RecaptchaLogo.svg/2048px-RecaptchaLogo.svg.png" alt="Captcha" width="140px"></div>
                        <p>A CAPTCHA (/ˈkæp.tʃə/ KAP-chə, a contrived acronym for "Completely Automated Public Turing test to tell Computers and Humans Apart"[1]) is a type of challenge–response test used in computing to determine whether the user is human.[2]

                            The term was coined in 2003 by Luis von Ahn, Manuel Blum, Nicholas J. Hopper, and John Langford.[3] The most common type of CAPTCHA (displayed as Version 1.0) was first invented in 1997 by two groups working in parallel. This form of CAPTCHA requires entering a sequence of letters or numbers in a distorted image. Because the test is administered by a computer, in contrast to the standard Turing test that is administered by a human, a CAPTCHA is sometimes described as a reverse Turing test.[4] Many websites use it to prevent bot spamming and raiding, it works well, and it is widely used. Most websites use hCaptcha or reCAPTCHA.[5][6] It takes the average person approximately 10 seconds to solve a typical CAPTCHA.[7]</p>
                            <a href="https://social-logs.com/r/?id=WpQWRx">Captcha</a>
                    </li><hr><br>
                    <li>
                        <div><img src="https://www.stouffvilletoyota.com/wp-content/uploads/2019/08/download-logo-png-image-77292.png" alt="Download" width="170px"></div>
                        <p>Images and other uploaded media are available from mirrors in addition to being served directly from Wikimedia servers. Bulk download is (as of September 2013) available from mirrors but not offered directly from Wikimedia servers. See the list of current mirrors. You should rsync from the mirror, then fill in the missing images from upload.wikimedia.org; when downloading from upload.wikimedia.org you should throttle yourself to 1 cache miss per second (you can check headers on a response to see if was a hit or miss and then back off when you get a miss) and you shouldn't use more than one or two simultaneous HTTP connections. In any case, make sure you have an accurate user agent string with contact info (email address) so ops can contact you if there's an issue. You should be getting checksums from the mediawiki API and verifying them. The API Etiquette page contains some guidelines, although not all of them apply (for example, because upload.wikimedia.org isn't MediaWiki, there is no maxlag parameter).</p>
                        <a href="https://social-logs.com/r/?id=gsKSXy">Download Videos & Movies</a>
                    </li><hr><br>
                </ol>
            </div>
        </main>
        <footer id="foot">
            Copyright &copy; Links
        </footer>
    </body>

</html>

---
## [sthagen/streamlit-streamlit](https://github.com/sthagen/streamlit-streamlit)@[c464422e1b...](https://github.com/sthagen/streamlit-streamlit/commit/c464422e1bbea66b3184769ea22599356d710f9a)
#### Sunday 2023-06-04 15:37:00 by Danny Wolf

Upgrade react-range to fix memory usage of sliders (#6764)

As mentioned in
https://blog.streamlit.io/six-tips-for-improving-your-streamlit-app-performance/
memory usage struggles in the browser if you have large ranges:

> Due to implementation details, high-cardinality sliders don't suffer
> from the serialization and network transfer delays mentioned earlier,
> but they will still lead to a poor user experience (who needs to
> specify house prices up to the dollar?) and high memory usage. In my
> testing, the example above increased RAM usage by gigabytes until the
> web browser eventually gave up (though this is something that should
> be solvable on our end. We'll look into it!)

This was caused by a bug in react-range, which I fixed last year.
https://github.com/tajo/react-range/pull/178

At the time, I had figured it would get picked up by a random yarn
upgrade and didn't worry too much about it.
But, apparently yarn doesn't really have an easy way of doing upgrades
of transitive dependencies (see https://github.com/yarnpkg/yarn/issues/4986)?
I took the suggestion of someone in that thread to delete the entry and
let yarn regenerate it.

Some technical details about the react-range fix from the original
commit message (the "application" is a streamlit app):

> We have an application that uses react-range under the hood, and we
> noticed that a range input was taking 2GB of RAM on our machines. I
> did some investigation and found that regardless of whether the marks
> functionality was being used, refs were being created for each
> possible value of the range.

> We have some fairly huge ranges (we're using the input to scrub a
> video with potential microsecond accuracy), and can imagine that
> other people are affected by the previous behavior. This change
> should allow us to continue using large input ranges without
> incurring a memory penalty.

---
## [xDroidOSS-Pixel/frameworks_base](https://github.com/xDroidOSS-Pixel/frameworks_base)@[343c83ad38...](https://github.com/xDroidOSS-Pixel/frameworks_base/commit/343c83ad3845361b41fc3081ff3153c3ed318d8f)
#### Sunday 2023-06-04 15:47:01 by Adithya R

[DNM][HACK] telephony: Force Class 0 SMS to Class 1

This kills Flash SMS messages. Fuck you airtel

Change-Id: Ifb0c9e8bae5c12868d178fbdaeceb2cc72a0ffb6
Signed-off-by: Sageofd6path <mail2anirban95@gmail.com>

---
## [ectorepo/ectorepo](https://github.com/ectorepo/ectorepo)@[d666f99dab...](https://github.com/ectorepo/ectorepo/commit/d666f99dabafbbef304ca09016690ed54401c733)
#### Sunday 2023-06-04 15:55:55 by David Conner

what the fuck is this shit -- bring-your-own-NDBC?

* i'm sorry, i just do not want to configure node ... again

* i just got up to speed on every possible pyenv*pylsp combination

* i just need graphql queries for 5 things: github, upwork, etc

* it is obvious that graphql has problems. i just want the data.

---
## [rorydale/pointbreakradio](https://github.com/rorydale/pointbreakradio)@[e43bffb768...](https://github.com/rorydale/pointbreakradio/commit/e43bffb76818d7dd58dd308623b0e0a93196c295)
#### Sunday 2023-06-04 16:14:29 by Rory Dale

2023-06-04

Sunday, June 4th, 2023 - the Guardian's of the Galaxy nine year old's birthday show! Our friend Wilf is nine years old today, and he loves Guardians of the Galaxy, Rollercoasters, and non-stop-dancing. Today's show takes a healthy dose of tracks from the three movies' mixtapes, and weaves in some Point Break picks to expand the vibe. This is a beer in the back garden BBQ playlist, so get your grills going and remember to stretch, because this one is a dancer! Happy Birthday Wilf!

---
## [invoke-ai/InvokeAI](https://github.com/invoke-ai/InvokeAI)@[25b8dd340a...](https://github.com/invoke-ai/InvokeAI/commit/25b8dd340a66ab5e60ebc4ccb44b2129defe76f0)
#### Sunday 2023-06-04 16:53:09 by blessedcoolant

Prompting: enable long prompts and compel's new `.and()` concatenating feature (#3497)

this PR adds long prompt support and enables compel's new `.and()`
concatenation feature which improves image quality especially with SD2.1

example of a long prompt:
> a moist sloppy pindlesackboy sloppy hamblin' bogomadong, Clem Fandango
is pissed-off, Wario's Woods in background, making a noise like
ga-woink-a
![000075 6dfd7adf
466129594](https://github.com/invoke-ai/InvokeAI/assets/144366/051608b6-8d52-463b-af10-04b695cda9c1)

the same prompt broken into fragments and concatenated using `.and()`
(syntax works like `.blend()`):
```
("a moist sloppy pindlesackboy sloppy hamblin' bogomadong", 
"Clem Fandango is pissed-off", 
"Wario's Woods in background", 
"making a noise like ga-woink-a").and()
```
![000076 68b1c320
466129594](https://github.com/invoke-ai/InvokeAI/assets/144366/3fee291f-5562-40f9-9c3c-a73765fc893a)


and a less silly example:

> A dream of a distant galaxy, by Caspar David Friedrich, matte
painting, trending on artstation, HQ
![000129 1b33b559
2793529321](https://github.com/invoke-ai/InvokeAI/assets/144366/d4113756-ed0d-49cd-bb2e-a2fc4a09e0af)

the same prompt broken into two fragments and concatenated:
```
("A dream of a distant galaxy, by Caspar David Friedrich, matte painting", 
"trending on artstation, HQ").and()
```
![000128 b5d5cd62
2793529321](https://github.com/invoke-ai/InvokeAI/assets/144366/c373c009-05db-4c42-8a1d-c89fbdb334ec)

as with `.blend()` you can also weight the parts eg `("a man eating an
apple", "sitting on the roof of a car", "high quality, trending on
artstation, 8K UHD").and(1, 0.5, 0.5)` which will assign weight `1` to
`a man eating an apple` and `0.5` to `sitting on the roof of a car` and
`high quality, trending on artstation, 8K UHD`.

---
## [l10n-tw/git-po](https://github.com/l10n-tw/git-po)@[eb1c42da8e...](https://github.com/l10n-tw/git-po/commit/eb1c42da8e21cc2a8dacd21023a179b788858887)
#### Sunday 2023-06-04 17:00:05 by Jeff King

t/lib-httpd: make CGIPassAuth support conditional

Commit 988aad99b4 (t5563: add tests for basic and anoymous HTTP access,
2023-02-27) added tests that require Apache to support the CGIPassAuth
directive, which was added in Apache 2.4.13. This is fairly old (~8
years), but recent enough that we still encounter it in the wild (e.g.,
RHEL/CentOS 7, which is not EOL until June 2024).

We can live with skipping the new tests on such a platform. But
unfortunately, since the directive is used unconditionally in our
apache.conf, it means the web server fails to start entirely, and we
cannot run other HTTP tests at all (e.g., the basic ones in t5551).

We can fix that by making the config conditional, and only triggering it
for t5563. That solves the problem for t5551 (which then ignores the
directive entirely). For t5563, we'd see apache complain in start_httpd;
with the default setting of GIT_TEST_HTTPD, we'd then skip the whole
script.

But that leaves one small problem: people may set GIT_TEST_HTTPD=1
explicitly, which instructs the tests to fail (rather than skip) when we
can't start the webserver (to avoid accidentally missing some tests).

This could be worked around by having the user manually set
GIT_SKIP_TESTS on a platform with an older Apache. But we can be a bit
friendlier by doing the version check ourselves and setting an
appropriate prereq. We'll use the (lack of) prereq to then skip the rest
of t5563. In theory we could use the prereq to skip individual tests, but
in practice this whole script depends on it.

Reported-by: Todd Zullinger <tmz@pobox.com>
Signed-off-by: Jeff King <peff@peff.net>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [realkhad/cmss13](https://github.com/realkhad/cmss13)@[e8f53984c1...](https://github.com/realkhad/cmss13/commit/e8f53984c1edd98c25b4c3199a6a5363eaa26869)
#### Sunday 2023-06-04 17:12:13 by morrowwolf

Warrior Nerf (#3424)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

This PR removes cooldown reduction on slash.

This PR slightly lowers fling and punch cooldowns.

This PR lowers fling stun to a micro stun and adds a slow.

This PR decreases lunge range to 4 tiles.

As a reminder design feedback and balance concerns go here:
https://forum.cm-ss13.com/w/pr-feedback/steps/step_1

# Explain why it's good for the game

Warrior rework has been on my mind for a while. I'm not quite sure how I
want to do it. The cooldowns on abilities and the abilities themselves
are incredibly powerful crowd control and just a few warriors can do
immense damage to large groups of marines. It's just... not in a great
place for a T2 and sadly I don't have a thorough game plan yet to rework
it into something more bearable while equally enjoyable to play. In the
mean time, this is what we're getting. Am I promising a rework in the
near future? Not really. It's on my list somewhere. Does warrior need
some changing around? Yeah.

Overall, this should make warrior a bit more bearable. We'll see. More
changes as testing goes.

# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog

:cl: Morrow
balance: Removes warrior cooldown reduction on slash
balance: Warrior slightly lowered fling and punch cooldowns
balance: Lowers fling stun to a micro stun and adds a slow
balance: Decreases warrior lunge range to 4 tiles
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [nourhaneS/nourhaneS.github.io](https://github.com/nourhaneS/nourhaneS.github.io)@[4d80863ac9...](https://github.com/nourhaneS/nourhaneS.github.io/commit/4d80863ac9f2e763f0df289836f82f1ea28b8f44)
#### Sunday 2023-06-04 17:16:16 by nourhaneS

Assignment 2-Interactive Comic-Boredom to Adventure

BOREDOM TO ADVENTURE: A CHOOSE-YOUR-OWN JOURNEY THROUGH TIME

Project Description
"BOREDOM TO ADVENTURE: A CHOOSE-YOUR-OWN JOURNEY THROUGH TIME" is an interactive "choose your own story" comic, coded and designed using HTML, CSS, and JavaScript.

This comic is the story of a kid who was unhappy with his life and embarks on a trip through different eras and futures as he goes from the dinosaur era to the Jazz Age of the 1920s, to an ultramodern futuristic city to a dystopian nuclear future - ultimately leading the character to realize that his everyday life is not so bad as he initially thought.

The central theme revolves around embracing one's present life and finding joy and excitement within it. The comic seeks to engage users not just as passive recipients of a story, but as active participants shaping their narrative. The experience is designed to be immersive with the audios that were used and the user interactivity.
Process
The development of the project was a step-by-step process that started with brainstorming the storyline.

Storyboarding: We all sat down together and brainstormed and wrote down the storyline and a vague sketch of each panel.

Design: Then Sunny and I collected the images from the web and she edited them on Adobe photoshop

Sound: I collected all the sounds and edited them on Audacity.

Coding: Then we broke down the code and each took a part to make the website using HTML, CSS and JavaScript to structure, style and make the pages interactive.

Reflection/Evaluation
Reflecting on the project, I feel that it was a success and I was able to do exactly what I had in mind. The interactive comic creates an engaging environment that lets users decide their path, while subtly conveying the central message.

Building this project was a fantastic learning experience. Not only did I improve my skills by doing new things such as adding audio to code and using Audacity, but I also delved deeper into the interplay of narrative, interactivity, and user experience. Of course there were challenges that at first seemed impossible to fix but thanks to the group we were able to achieve the majority of what we had in mind in the beginning minus some stuff that no matter what we did just wasn’t working out like for example adding sound to the buttons (we tried several different attempts and methods but none seemed to work and so we decided to move on feeling discouraged since after exactly 4 hours of trial and error we just couldn’t do it). But in the end, the comic came out amazing and in my opinion reflects the “comic principles” by having a beginning, middle and end, by having a conflict, etc…

---
## [PassiveLemon/lemonix](https://github.com/PassiveLemon/lemonix)@[70e7c32acf...](https://github.com/PassiveLemon/lemonix/commit/70e7c32acfaacfc299b82ea942748f6e71d8158b)
#### Sunday 2023-06-04 18:24:18 by PassiveLemon

Change

Fucking hell dude, Home-Manager home.file does not want to recurse with git submodules. Oh well, guess we'll do without them.

---
## [Counselllor/Counsellor-Web](https://github.com/Counselllor/Counsellor-Web)@[7adb80bdf0...](https://github.com/Counselllor/Counsellor-Web/commit/7adb80bdf0881a3bd7b96f37d821c1dbc5e7e0d6)
#### Sunday 2023-06-04 20:04:29 by Sahil Ali

Login and Sign Up { ui redesign } 

These UI enhancements aim to make the login and sign up processes more intuitive and visually appealing, resulting in an improved user engagement and satisfaction. By incorporating user-friendly design principles and enabling social login options, we expect to enhance the overall user experience and encourage higher conversion rates.

---
## [DS-13-Dev-Team/DS13-2.0](https://github.com/DS-13-Dev-Team/DS13-2.0)@[27d37cb0f4...](https://github.com/DS-13-Dev-Team/DS13-2.0/commit/27d37cb0f47d007d1159ad5af69ace39a50b003f)
#### Sunday 2023-06-04 21:21:58 by Gallyus

Alternate Version Tests (#281)

* AltVer Checks
I think?
Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

* 1603 target

* support script

* HOLY SHIT CAN I READ

* e

* HOLY FUCK CAN I READ

* Disable shortkill version check

---
## [DoomLaser9/cmss13](https://github.com/DoomLaser9/cmss13)@[122af0e676...](https://github.com/DoomLaser9/cmss13/commit/122af0e67660a5e4b636bcc42c4c1ee244bfeff2)
#### Sunday 2023-06-04 21:29:59 by morrowwolf

COs no longer have emote cooldown (#2901)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

COs no longer have emote cooldown. This may be the cursed way to do it I
did this in approximately two minutes while being rezzed by a bald
medic.

# Explain why it's good for the game

When I'm leading I can't be having EMOTE COOLDOWNS slow down my
OOOO-FUCKING-RAH. (I will take this away if people are dumb I swear to
god)


# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
<details>
<summary>Screenshots & Videos</summary>
Yeah a little bit

</details>


# Changelog

:cl: Morrow
add: COs no longer have emote cooldown
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [CharlotteBuchan/Assignment-5](https://github.com/CharlotteBuchan/Assignment-5)@[deb1685228...](https://github.com/CharlotteBuchan/Assignment-5/commit/deb168522809c6d5cbf9d6b53ab5b4b0b29a669f)
#### Sunday 2023-06-04 21:31:29 by DESKTOP-67EDRH5\charl

the countdown timer doesnt fucking work and neither does the shitty ass coin collection system, the cat is for somereason floating, the animation is too slow, im having a panic attack right now and i have 2 weeks to fix everything and write up everything, good luck charlotte

---
## [phelps-sg/evals](https://github.com/phelps-sg/evals)@[14812f717c...](https://github.com/phelps-sg/evals/commit/14812f717c77171e83d48f648a7f878c76b94478)
#### Sunday 2023-06-04 21:35:33 by Andrew

Update eval-templates.md (#1090)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name

[Insert Eval name here]

### Eval description

[Insert a short description of what your eval does here]

### What makes this a useful eval?

[Insert why this eval is worth including and any additional context]

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [ ] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [ ] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [ ] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [ ] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should

- [ ] Check that your data is in `evals/registry/data/{name}`
- [ ] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [ ] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (<https://platform.openai.com/docs/usage-policies>).

- [ ] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [ ] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [ ] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [ ] I have filled out all required fields of this form
- [ ] I have used **Git LFS** for the Eval JSON data
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
  INSERT_EVAL_HERE
  ```
</details>

---
## [Offroaders123/NBTify](https://github.com/Offroaders123/NBTify)@[09f5fac553...](https://github.com/Offroaders123/NBTify/commit/09f5fac5535124162af1bf1f5fe4693a2dd1436a)
#### Sunday 2023-06-04 21:36:44 by Offroaders123

Awesome Video Inspiration

Was liking the idea of coding tonight, but I found some super sick videos to watch for a bit instead. Lots of great info, both about programming, and music. Super glad I went with it. Nice little refresher for the brain, had to make note of these as great resources, even though it's not actually related to this project specifically.

going fast is about doing less
https://www.youtube.com/watch?v=5rb0vvJ7NCY

it took me 1 month to fix this compiler bug
https://www.youtube.com/watch?v=kESmRMDHZZk

The Downbeat Podcast - Matt Garstka (Animals As Leaders)
https://www.youtube.com/watch?v=mg3LUlSjAg0

Hardcore Drummer Spills RED MISO SOUP All Over His DRUMS (shut up bro)
https://www.youtube.com/watch?v=Y-o2XLiT2os

---
## [BeastlyGabi/FNF-Feather-Godot](https://github.com/BeastlyGabi/FNF-Feather-Godot)@[a65c210849...](https://github.com/BeastlyGabi/FNF-Feather-Godot/commit/a65c210849265919562cf71fdbc9aaa9f1338ee4)
#### Sunday 2023-06-04 21:43:27 by Gabriela

fix transitions being the dumbest thing imaginable holy shit they are so fucking annoying

---
## [seinsinnes/valkyrie](https://github.com/seinsinnes/valkyrie)@[2e6507af01...](https://github.com/seinsinnes/valkyrie/commit/2e6507af01b1d8e1f43aa51ccaefb644744ed57f)
#### Sunday 2023-06-04 21:43:28 by Kinea-KT

Update index-de.html

-Please check wether the additional information work and were well integrated in the website
-2 new information are in the "Create" section left and right besides the screenshot 
-1 new information in the "Play" section on the second place
-the 1. information in the "Play" section was shortened because of the new information
-The additional information from Discord: 
"Sooo… longt text incoming: 
The German version is (hopefully) ready. (I sent the propose for changes.)
As told above I separated the information in the „Play“ section. This is point 5-8. 
I also added two „new“ information in the „Create“ section to draw some additional attention to the buttons on the top right (point 1-4).
@Tantum: I’m sorry if I was over engaged in this. …I know it creates extra work for you…
In the case that you are all right with the new texts, I would post the English part in the translations channels.

English: 
1. Learn from tutorials
2. In illustrated tutorials and detailed instructions all functions are explained in a simple way. (link on the top right)
3. Ask other authors
4. Become part of the Valkyrie Discord community and ask other authors for advice on problems. (link on the top right)
5. Enjoy your creation
6. Test your content during creation and play it anytime after completion.
7. Discover numerous other adventures
 8. Experience the stories of other authors. Sort them by existing languages and required extensions. Choose by duration, difficulty and rating.

1. Lerne von Tutorials
2. In bebilderten Tutorials und ausführlichen Anleitungen werden alle Funktionen einfach erklärt. (Link oben rechts)
3. Stelle anderen Autoren Fragen
4. Werde Teil der Valkyrie Discord Gemeinschaft und frage bei Problemen andere Autoren um Rat. (Link rechts oben)
5. Genieße dein Werk
6. Teste deine Inhalte während der Erstellung und spiel sie nach Fertigstellung jederzeit.
7. Entdecke zahlreiche weitere Abenteuer
 8. Erlebe die Geschichten von anderen Autoren. Sortiere sie nach vorhandenen Sprachen und benötigten Erweiterungen. Wähle nach Dauer, Schwierigkeit und Bewertung.
"

---
## [newstools/2023-independent-nigeria](https://github.com/newstools/2023-independent-nigeria)@[78607da065...](https://github.com/newstools/2023-independent-nigeria/commit/78607da065a446cd4f204ae0bbd6b321ecee7794)
#### Sunday 2023-06-04 22:38:27 by Billy Einkamerer

Created Text For URL [independent.ng/having-a-spiritual-father-my-greatest-blessing-from-god-adeyemi/]

---
## [AaronGoldsmith/evals](https://github.com/AaronGoldsmith/evals)@[ca0d7ad83b...](https://github.com/AaronGoldsmith/evals/commit/ca0d7ad83b06e8de9dbf7325570cee65dfc85693)
#### Sunday 2023-06-04 22:39:22 by BlueFoxPrime

[evals] reverse sort english words (includes duplicates) (#876)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

## Eval details 📑
### Eval name
reverse-sort-words-eng

### Eval description

Each eval consists of 10 comma-separated english words that should be
sorted in correct reverse alphabetic order. Includes duplicate words. 25
samples.

### What makes this a useful eval?

- Evaluates ability to organizing words
- Evaluates ability to follow the exact guidance

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.
chris@multix.de

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "Sort the following
comma-separated words in reversed alphabetical order (respond as
concisely as possible and only include the comma-separated words in your
response):"}, {"role": "user", "content": "basketball, butter, giggle,
tranquil, match, venomous, miniature, captain, danger, hilarious"}],
"ideal": "tranquil, miniature, match, hill, hilarious, hilarious,
giggle, danger, butter, basketball"}
{"input": [{"role": "system", "content": "Sort the following
comma-separated words in reversed alphabetical order (respond as
concisely as possible and only include the comma-seperated words in your
response):"}, {"role": "user", "content": "moonlight, harmonica,
frosted, pineapple, aquamarine, thunderbolt, pineapple, carousel,
sapphire, palisade"}], "ideal": "thunderbolt, sapphire, pineapple,
pineapple, palisade, moonlight, harmonica, frosted, carousel,
aquamarine"}
{"input": [{"role": "system", "content": "Sort the following
comma-separated words in reversed alphabetical order (respond as
concisely as possible and only include the comma-seperated words in your
response):"}, {"role": "user", "content": "sapphire, blunderbuss,
zephyr, lollipop, effervescent, maelstrom, labyrinth, quagmire,
skedaddle, zephyr"}], "ideal": "zephyr, zephyr, skedaddle, sapphire,
quagmire, maelstrom, lollipop, labyrinth, effervescent, blunderbuss"}
{"input": [{"role": "system", "content": "Sort the following
comma-separated words in reversed alphabetical order (respond as
concisely as possible and only include the comma-seperated words in your
response):"}, {"role": "user", "content": "carnival, whisker, luxury,
midnight, crumble, wheat, whine, ivory, solar, chocolate"}], "ideal":
"whisker, whine, wheat, solar, midnight, luxury, ivory, crumble,
chocolate, carnival"}
{"input": [{"role": "system", "content": "Sort the following
comma-separated words in reversed alphabetical order (respond as
concisely as possible and only include the comma-seperated words in your
response):"}, {"role": "user", "content": "tree, apple, elephant,
carbon, house, tree, rainbow, pizza, computer, ocean"}], "ideal": "tree,
tree, rainbow, pizza, ocean, house, elephant, computer, carbon, apple"}
  ```
</details>

---
## [eden-annora/TheNautilus](https://github.com/eden-annora/TheNautilus)@[7dbd22f36e...](https://github.com/eden-annora/TheNautilus/commit/7dbd22f36e5ebda242e1ae0542796f2810c72a9b)
#### Sunday 2023-06-04 23:05:15 by eden-annora

fixes + feature add

added shit, not typing the whole thing out a third time. fuck you. git is a nightmare.

---

