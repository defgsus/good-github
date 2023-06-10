## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-06-09](docs/good-messages/2023/2023-06-09.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,066,908 were push events containing 3,363,003 commit messages that amount to 264,468,653 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 64 messages:


## [ppauliuchenka02/bandgeeks-news-app](https://github.com/ppauliuchenka02/bandgeeks-news-app)@[40e93e1e82...](https://github.com/ppauliuchenka02/bandgeeks-news-app/commit/40e93e1e820b9c251e6e5d465ea6a96089a4e623)
#### Friday 2023-06-09 00:06:23 by Joseph Antonucci

I want to dip my brain in a can of paint thinner

Fixes the authentication issue. We were querying for columns that didn't exist in the User database and because Prisma is Prisma (this is not a complement) we weren't getting any errors relating to the issue. Fixed lines in 'api/dist/functions/auth.js', 'api/src/functions/auth.js' and 'api/src/lib/auth.js'. Holy Fuckles it's knuckles this one was a doozy

---
## [realforest2001/forest-cm13](https://github.com/realforest2001/forest-cm13)@[d1d23352eb...](https://github.com/realforest2001/forest-cm13/commit/d1d23352eb41452a98d0c66c7fbf5c5ea4143ffe)
#### Friday 2023-06-09 00:11:22 by fira

Reduces SG Full Auto Scatter (#3556)

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

It's been bugging me for a long time, but when you fire for a good dozen
seconds with the standard issue smartguns, the bullets start scattering.
So, so far you'll say, good Fira, that's soulful!

However, we have no ACTUAL recoil or similar mechanic. So letting go of
the LMB for just even 20 miliseconds is enough to reset scatter to start
of firing. **It's just a noobtrap with zero real gameplay elements.**

This reduces the max scatter so that bullets don't just start (after
EIGHTY shots!) spraying a (roughly) 48° angle cone, but instead 12°
which mostly stays on the same actual turfs. At this value the targeting
impact is vastly minimized, but the projectile visuals retain
significant scattering.

I don't think this ACTUALLY qualifies as a "balance" change due to how
irrelevant the "mechanic" was, but i'll slap it on.

# Explain why it's good for the game
Less of a noobtrap and pointless purely mechanical micromanagement so
people can focus on playing the game.

I'd rather we get a recoil mechanic to make this meaningful but it's bit
of a bigger problem...

# Changelog
:cl:
qol: Reduced USCM SG max scattering on Full Auto fire so you don't have
to periodically let go of the fire button to keep it from firing way
wide.
/:cl:

---
## [TypeVar/Shiptest](https://github.com/TypeVar/Shiptest)@[0cff53fc09...](https://github.com/TypeVar/Shiptest/commit/0cff53fc09c34d989d2bc34b1699bd856af2cb92)
#### Friday 2023-06-09 00:34:05 by meemofcourse

Reworks the Twinkleshine-Class (#1825)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request


![2023 05 13-23 20
45](https://github.com/shiptest-ss13/Shiptest/assets/75212565/de6f3a47-7be8-4800-ae73-9fc386e4bf01)

![twinklerework5](https://github.com/shiptest-ss13/Shiptest/assets/75212565/f1808576-70e3-4b56-b977-5b5e7d665fdd)





The Twinkleshine is a CyberSun-made Syndicate display of force, staffed
by every branch of the Syndicate. Despite the silly name, the presence
of one in a sector implies it to be of importance to the Syndicate, and
enemies within sight can only pray that the Twinkleshine crew are
incompetent enough to shoot themselves with their own weaponry (or blow
themselves up with the supermatter on-board).

It is staffed by:

- 1 Captain
- 1 Lieutenant (previously the Operative - serves as a warden/hos)
- 2 Medics
- 2 Engineers (previously the Mechanics)
- 5 Operatives (previously the Troopers)
- 1 Bartender
- 1 Miner
- 2 Deck Assistants

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

Few days ago, an admin spawned a Twinkleshine, and I got to captain it.
The Twinkleshine is old. It sucks. This, hopefully, fixes that.

Originally, this was going to be minor fixes, but ended up becoming an
attempt at reworking the ship to a more modern state - the hull has been
redone and is mostly symmetrical, the old spacepod was replaced with a
Dark Gygax, the supermatter shouldn't be activated upon spawning the
ship, there's more turf decals and a bigger lot-of-things, added a
bartender and a miner, people can actually tell who they are and what
they do, and there is now a box moth. Rejoice.

Also, this is the first time I've ever mapped a ship. What better way to
begin with a giant battleship?

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
tweak: Reworks the Twinkleshine
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Signed-off-by: meemofcourse <75212565+meemofcourse@users.noreply.github.com>

---
## [TypeVar/Shiptest](https://github.com/TypeVar/Shiptest)@[d4b5a598e2...](https://github.com/TypeVar/Shiptest/commit/d4b5a598e2346bb3f69d533ed05a94d539e8b830)
#### Friday 2023-06-09 00:34:05 by Bjarl

Sand Survivor Rework (#1940)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Reworks how Sand Survivors spawn their loot. Instead of an outfit datum,
they now create a corpse similiarly to how legions do it, this allows
their contents to have some variety, more ease of expansion, and
generally Improves the file.

How I could write better code in a day than White Sands functioned with
for iunno how long is byond me


https://user-images.githubusercontent.com/94164348/236322169-c303f934-634f-447d-950f-78a55346d152.mp4

![image](https://user-images.githubusercontent.com/94164348/236376947-6e484ed0-f136-4787-9e74-fad0f5c21d11.png)

![image](https://user-images.githubusercontent.com/94164348/236377018-e2dc1661-fe78-4c6a-8be2-8bf24e5d00b2.png)


<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
Consistency + Just kinda cool
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: Sand Planet hermits now have randomized inventories. And Hair.
Sometimes.
add: Sand Planet hermits can now drop different races
add: legions will now drop a variety of species
balance: drop rates for legions have been changed in a few spots.
fix: hivelord.dm no longer sears my eyes out.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Signed-off-by: Bjarl <94164348+Bjarl@users.noreply.github.com>
Co-authored-by: Mark Suckerberg <mark@suckerberg.gay>

---
## [Jolly-66/dragon-station](https://github.com/Jolly-66/dragon-station)@[ddd018f4d5...](https://github.com/Jolly-66/dragon-station/commit/ddd018f4d54fcb2917ca9cbf71a913a3bafc7900)
#### Friday 2023-06-09 00:59:58 by SkyratBot

[MIRROR] Changes syndicate surgery duffelbags to contain advanced tools [MDB IGNORE] (#21619)

* Changes syndicate surgery duffelbags to contain advanced tools (#75846)

## About The Pull Request

Changes syndicate surgery duffelbags to contain advanced tools.

In total, they contain
- All advanced surgical tools, alongside the normal ones without an
advanced version
- Sterilizine gel
- Bone gel and surgical tape
- Roller bed
- Straight jacket, muzzle, and MMI

Changed the Syndicate Infiltrators' surgery areas to contain a full
syndicate surgery duffelbag.

The normal infiltrator now has a operating computer and a closet of
misc. surgical clothing and anesthesic tank.

## Why It's Good For The Game

> Changes syndicate surgery duffelbags to contain advanced tools.

> In total, they contain (...)

The only real reason to buy this item is for the increased storage space
the duffelbag gives, and I find that a little sad. Surgical tools are
plentiful, as they can either be lathed from cargo, medbay, or just
taken. A surgeon, the role that *should* thematically need this the
most, has absolutely no reason to take it. Now they do! A full set of
advanced tools is certainly something that can be considered for
purchase, especially with all the bonus items in here - which might just
allow a traitor to repair their bones if they're heavily wanted and
licking their wounds in maintenance. The TC cost has been increased to 4
to compensate.

> Changed the Syndicate Infiltrators' surgery areas to contain a full
syndicate surgery duffelbag.

Similar to above, but instead, the reasoning is that nukies really do
not have a lot of time to do surgery. A lot of the 20 minutes of prep
time in War is spent figuring out what you're buying with your
exorbitant amount of TC, in non-War you don't really want to delay the
mission for five minutes for surgery, and its hassle means that most
people do not really want to bother with things like nerve threading,
etc. due to the large, annoying time cost.

> The normal infiltrator now has a operating computer and a closet of
misc. surgical clothing and anesthesic tank.

The former is because, well, what the hell, why didn't it have one!
Removing the loose tools gave me the space for it. The latter is just me
realizing that empty closet is weird and lame and so I gave it some
fluff contents to give it a reason to exist.

## Changelog

:cl:
add: Changes syndicate surgery duffelbags to contain advanced tools,
sterilizine, surgical tape, and a roller bed.
add: Changed the Syndicate Infiltrators' surgery areas to contain a full
syndicate surgery duffelbag.
add: The normal infiltrator now has a operating computer and a closet of
misc. surgical clothing and anesthesic tank.
/:cl:

* Changes syndicate surgery duffelbags to contain advanced tools

---------

Co-authored-by: carlarctg <53100513+carlarctg@users.noreply.github.com>

---
## [Vivswan/pytorch](https://github.com/Vivswan/pytorch)@[b5840f99c3...](https://github.com/Vivswan/pytorch/commit/b5840f99c3f2ae01b7831fd32b99758180fc22c3)
#### Friday 2023-06-09 01:23:33 by Mark Saroufim

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
## [Thunder12345/Skyrat-tg](https://github.com/Thunder12345/Skyrat-tg)@[bfb3967c90...](https://github.com/Thunder12345/Skyrat-tg/commit/bfb3967c908682e21202312d8b30ec17ad65e549)
#### Friday 2023-06-09 01:38:17 by SkyratBot

[MIRROR] Adds proper armor for security plasmamen. [MDB IGNORE] (#21268)

* Adds proper armor for security plasmamen. (#75156)

## About The Pull Request
It's kinda strange that security plasmamen has no proper armor and you
can just bully them with bottlesmashes. Literally.
Also suits had no wound armor for some reason, which considering that
mold dies without hand kinda silly too.
And helmets just had no armor besides 1 melee armor.
## Why It's Good For The Game
Plasmamen security won't die that easilly. I mean, still easy to kill
them, but not that much.
## Changelog
:cl:
balance: Security Plasmamen now have Security armor. No bullying them
with bottlesmashes anymore.
/:cl:

* Adds proper armor for security plasmamen.

---------

Co-authored-by: Helg2 <93882977+Helg2@users.noreply.github.com>
Co-authored-by: lessthanthree <83487515+lessthnthree@users.noreply.github.com>

---
## [knative-automation/client-pkg](https://github.com/knative-automation/client-pkg)@[6a6d96e795...](https://github.com/knative-automation/client-pkg/commit/6a6d96e795dfaf3f4aecc0aeb9b691a9e96aad55)
#### Friday 2023-06-09 01:48:37 by Knative Automation

upgrade to latest dependencies

bumping k8s.io/api 88912e3...6b24792:%0A  > 6b24792 Update dependencies to v0.26.5 tag%0A  > 37e98ba Merge pull request # 117814 from kerthcet/automated-cherry-pick-of-# 117802-upstream-release-1.26%0A  > 7ff025f Update podFailurePolicy comments from alpha-level to beta%0A  > c9f384e Merge pull request # 117691 from dims/re-do-of-117242-on-release-1.26%0A  > c00f1ad Bump runc go module v1.1.4 -> v1.1.6%0A  > 4c28c5a Merge pull request # 117323 from dddddai/automated-cherry-pick-of-# 117182-upstream-release-1.26%0A  > 9483bbc use case-insensitive header keys for http probes%0A  > 0545f3a Merge pull request # 116081 from pohly/automated-cherry-pick-of-# 115928-origin-release-1.26%0A  > e92d7e9 api: generated files%0A  > 16f23da api: drop Resources.Claims from PVC and PVC template%0A  > 5fd8a44 Merge pull request # 115787 from liggitt/net-0.7.0-1.26%0A  > 1b65b64 Update golang.org/x/net to v0.7.0%0A  > 2e857c1 Merge pull request # 115400 from pohly/automated-cherry-pick-of-# 115354-origin-release-1.26%0A  > 1c6bd70 Merge pull request # 115642 from nckturner/pin-golang.org/x/net-to-v0.4.0-in-1.26%0A  > 50d0b42 dynamic resource allocation: avoid apiserver complaint about list content%0A  > 045c7fe Pin golang.org/x/net to v0.4.0 in 1.26%0A  > 07a9cbc Merge pull request # 114617 from JoelSpeed/automated-cherry-pick-of-# 114585-upstream-release-1.26%0A  > 52655b9 Resource claims should be a map type%0A  > 07ac8fe Merge remote-tracking branch 'origin/master' into release-1.26%0A  > 566ee01 Update golang.org/x/net 1e63c2f%0A  > b966dc9 sync: update go.mod%0A  > 053624e Merge pull request # 111023 from pohly/dynamic-resource-allocation%0A  > 3590eda Merge pull request # 113375 from atiratree/PodHealthyPolicy-api%0A  > 8356158 api: update testdata%0A  > 5cb3202 Merge pull request # 113186 from ttakahashi21/KEP-3294%0A  > 5a4f9a5 generated%0A  > 78799a8 api: generated files%0A  > dfd6ea2 Generate code%0A  > 993c43c api: add UnhealthyPodEvictionPolicy for PDBs%0A  > ef72ea9 api: dynamic resource allocation API%0A  > d8ab3fb Add API and validation for CrossNamespaceVolumeDataSource%0A  > af772fc api: add resource claims to core API%0A  > 7beaa08 Merge pull request # 112744 from pwschuurman/statefulset-slice-impl%0A  > d7d25c8 Merge pull request # 113360 from mimowo/handling-pod-failures-beta-enable%0A  > f46cd33 Undo unintentional documentation comment change%0A  > f967e44 Merge pull request # 113485 from MikeSpreitzer/apf-borrowing%0A  > 11620b8 Enable the feature into beta%0A  > 6ae95de Fix typo in function emptyInvariants()%0A  > 34f4a52 apiserver: update API testdata at HEAD for flowcontrol%0A  > 3928298 Rebasing feature branch%0A  > e91ffd8 apiserver: add generated files for borrowing in flowcontrol%0A  > d961983 Update doc comments and change name of feature gate%0A  > fcd0d56 apiserver: add fields for borrowing in apf flowcontrol%0A  > adddac7 Small updates and comment fixes%0A  > 98c1aa6 Merge pull request # 113314 from cici37/celIntegration%0A  > 0d02273 Update generated protobuf files%0A  > 3f61c95 Merge pull request # 113688 from dashpole/update_utils%0A  > 8a0a045 API - make update%0A  > a5e7c66 Adding implementation of KEP-3335, StatefulSetSlice%0A  > 72a29bf Merge pull request # 113500 from kerthcet/feat/graduate-nodeInclusionPoplicy-to-beta%0A  > 2a2f510 update k8s.io/utils to fix util tracing panic%0A  > 891a1f8 Adding new api version of admissionregistration.k8s.io v1alpha1 for CEL in Admission Control%0A  > ee30dcf Merge pull request # 113047 from everpeace/improve-supplemental-groups-description%0A  > 2482389 Feat: graduate NodeInclusionPolicy to beta%0A  > a489930 Rename copy to v1alpha1%0A  > 9a33ad3 Merge pull request # 112360 from mimowo/handling-pod-failures-beta-kubelet%0A  > c4b2250 Improve the description of PodSecurityContext.SupplementalGroups (including cri-api)%0A  > 358a069 Copy over admissionregistration v1 to v1alpha1%0A  > 6c616e1 Merge pull request # 113510 from alculquicondor/finalizers-stable%0A  > 5210e2f Add pod disruption conditions for kubelet initiated failures%0A  > 2025045 Merge pull request # 113351 from andrewsykim/endpointslice-terminating-ga%0A  > aa2b4eb Graduate JobTrackingWithFinalizers to stable%0A  > 4bad656 Merge pull request # 113274 from Huang-Wei/kep-3521-A%0A  > aa9d0a7 k8s.io/api/discovery: remove API docs referencing EndpointSliceTerminatingCondition feature gate%0A  > 91f2496 Merge pull request # 113496 from avoltz/anvoltz/ga-itr%0A  > 686871f Automated codegen%0A  > c865c5c Promote ServiceInternalTrafficPolicy to GA%0A  > bd25e4f APIs, Validation and condition enforcements%0A  > 5448eb3 Merge pull request # 106242 from thockin/revive-copy-lb-status-type-to-ingress%0A  > edbfe77 Copy LoadBalancerStatus from core to networking%0A  > 6892570 Merge pull request # 112693 from aimuz/fix-GO-2022-0969%0A  > c5dc3f4 Fixed (CVE-2022-27664) Bump golang.org/x/net to v0.1.1-0.20221027164007-c63010009c80%0A  > 4e8dc44 Merge pull request # 111978 from Jefftree/aggregated-discovery-types%0A  > 72580e4 Add discovery types%0A  > 0184bd8 Merge pull request # 112643 from SergeyKanzhelev/removeDynamicKubeletConfig%0A  > 0f81104 Merge pull request # 112989 from ameukam/bump-golang.org/x/text-to-v0.3.8%0A  > f8118a1 remove DynamicKubeletConfig feature gate from the code%0A  > 370c8f0 Bump golang.org/x/text to v0.3.8%0A  > 3638040 Merge pull request # 112875 from pohly/update-yaml%0A  > 7ecab5c dependencies: update to sigs.k8s.io/yaml v1.3.0%0A  > 669318b Merge pull request # 112832 from tkashem/apf-prelifecycle-gen%0A  > 2cfef31 apiserver: prerelease-lifecycle-gen for flowcontrol%0A  > 3cedfad Merge pull request # 112306 from tkashem/v1beta3%0A  > 3814236 Merge pull request # 112707 from enj/enj/i/https_links%0A  > 418dd97 add testdata for flowcontrol v1beta3%0A  > ba008c5 Use https links for k8s KEPs, issues, PRs, etc%0A  > c96c62f rename assuredConcurrencyShares for flowcontrol v1beta3%0A  > be233f8 Merge pull request # 112673 from dims/update-to-latest-k8s.io/utils-sep-22%0A  > 51a3f54 add patch annotations to flowcontrol v1beta3%0A  > ca5be1f Update to latest k8s.io/utils to pick up changes%0A  > 7e203ee apiserver: generate for apf v1beta3%0A  > 79091da Merge pull request # 112577 from andrewsykim/feature-gate-cleanup%0A  > 19d0ef4 apiserver: enable v1beta3 for apf%0A  > 052d63f Merge pull request # 112545 from dims/update-etcd-3.5.5-and-all-otel-related-to-latest%0A  > 1f28922 remove +featureGate=LoadBalancerClass tag in service.spec.loadBalancerClass%0A  > f50a5b7 apiserver: apf rename copy to v1beta3%0A  > 9df3db1 updated etcd to v3.5.5 and newer otel libraries as well%0A  > bed6431 apiserver: copy apf v1beta2 to v1beta3%0A  > c98ebf1 Merge pull request # 112487 from liggitt/flowcontrol-test%0A  > 5c9e17a Add compatibility fixtures for v1beta2 flowcontrol%0A  > 9842651 Merge pull request # 111333 from flant/selfsubjectattributesreviews%0A  > 43df43b Add auth API to get self subject attributes%0A  > 30ff991 Merge pull request # 112349 from pohly/klog-update%0A  > e6114e9 build: update to klog v2.80.1%0A  > 929c3f0 Merge pull request # 112301 from aojea/ipv6_rfc3849%0A  > a687cab use IPv6 Address Prefix Reserved for Documentation for api docs%0A  > 6dd661f Merge pull request # 112199 from pohly/klog-update%0A  > 8a7d12c dependencies: update to klog v2.80.0%0A  > a6ff7c9 Merge pull request # 112146 from kerthcet/feat/move-schedulerError-to-api%0A  > ab89e44 Move constant schedulerError in scheduler to v1 package%0A  > d104994 Merge pull request # 112052 from tosi3k/bump-client-golang%0A  > 15b6dd2 Bump prometheus/client_golang to v1.13.0%0A  > 3be0a3c Merge pull request # 111974 from liggitt/1-25-compatibility%0A  > 49e055e Merge pull request # 111830 from t1anz0ng/typo%0A  > fcc83cd Drop 1.23 compatibility data%0A  > 64f80bd Merge pull request # 111611 from kardashov/ref-spec-docs-typo-fix%0A  > ea5df3a fix(typo): remove extra " from autoscaling doc string%0A  > 4cde1ad Add 1.25 compatibility data%0A  > 2e7b661 Merge pull request # 111657 from aojea/hc_nodeport%0A  > d07af88 Generate specs after fixing typo in documentation%0A  > 649256a Fix typo in field description.%0Abumping k8s.io/code-generator 6523e22...eec869e:%0A  > eec869e Merge pull request # 117691 from dims/re-do-of-117242-on-release-1.26%0A  > 824419b Bump runc go module v1.1.4 -> v1.1.6%0A  > ba94e65 Merge pull request # 115787 from liggitt/net-0.7.0-1.26%0A  > 6276bf2 Update golang.org/x/net to v0.7.0%0A  > 73b9c40 Merge pull request # 115642 from nckturner/pin-golang.org/x/net-to-v0.4.0-in-1.26%0A  > 882af80 Pin golang.org/x/net to v0.4.0 in 1.26%0A  > 6063700 Merge remote-tracking branch 'origin/master' into release-1.26%0A  > b615940 Update golang.org/x/net 1e63c2f%0A  > 11d5c4c update k8s.io/utils to fix util tracing panic%0A  > 081720d Merge pull request # 113367 from pohly/dep-ginkgo-gomega%0A  > d44fa8c dependencies: update to gomega v1.23.0 and ginkgo v2.4.0 and dependencies%0A  > 300cdcf Merge pull request # 112693 from aimuz/fix-GO-2022-0969%0A  > e0ef4aa Fixed (CVE-2022-27664) Bump golang.org/x/net to v0.1.1-0.20221027164007-c63010009c80%0A  > 557ce1f Merge pull request # 113126 from alexzielenski/remove-unwanted-replace%0A  > f86120d remove errant replace%0A  > d6a8b70 Merge pull request # 113106 from pohly/dep-ginkgo-gomega%0A  > f77ba6d dependencies: update to gomega v1.22.1 and ginkgo v2.3.1%0A  > 3bbe215 Merge pull request # 112988 from alexzielenski/update-kube-openapi%0A  > e80bbc4 Merge pull request # 113037 from pacoxu/fsnotify-v1.6.0%0A  > d403dc0 update kube-openapi%0A  > 790e4bc update fsnotify to v1.6.0%0A  > 27bd7d9 Merge pull request # 112989 from ameukam/bump-golang.org/x/text-to-v0.3.8%0A  > 4731e5c Bump golang.org/x/text to v0.3.8%0A  > a8a213c Merge pull request # 112875 from pohly/update-yaml%0A  > 5f5bab9 dependencies: update to sigs.k8s.io/yaml v1.3.0%0A  > 983d5d0 Merge pull request # 112819 from thockin/no-make-generators%0A  > c35177b Format calls to codegens%0A  > 83929d0 Codegens: Do not auto-set boilerplate path%0A  > 1d82d12 Merge pull request # 112705 from stevekuznetsov/skuznets/fix-comment%0A  > c3414a0 clients: clarify a misleading comment%0A  > 998e449 Merge pull request # 112673 from dims/update-to-latest-k8s.io/utils-sep-22%0A  > e4543b2 Update to latest k8s.io/utils to pick up changes%0A  > 8e999f2 Merge pull request # 112613 from dims/update-github.com/go-openapi/jsonreference-to-drop-github.com/PuerkitoBio/purell%0A  > 524127d update github.com/go-openapi/jsonreference to drop github.com/PuerkitoBio/purell%0A  > 4ca0baf Merge pull request # 112545 from dims/update-etcd-3.5.5-and-all-otel-related-to-latest%0A  > b54a056 Merge pull request # 112352 from pohly/e2e-ginkgo-progress%0A  > 350c30a updated etcd to v3.5.5 and newer otel libraries as well%0A  > 5f3f945 e2e: bump ginkgo to v2.2.0%0A  > 2e5cca7 Merge pull request # 112200 from pohly/client-go-shared-informer-factory-shutdown%0A  > c3fdc3c Merge pull request # 112349 from pohly/klog-update%0A  > e4b7976 client-go: support waiting for SharedInformerFactory shutdown%0A  > 135f69b build: update to klog v2.80.1%0A  > f60067d Merge pull request # 112341 from enj/enj/i/second_time_is_the_charm%0A  > 7c81c99 Merge pull request # 111768 from weilaaa/feature_add_symmetric_difference_in_sets_string%0A  > 8468f16 Remove in-tree credential plugins (again)%0A  > 9b98ed3 add symmetric difference in sets%0A  > 34125ff Merge pull request # 112199 from pohly/klog-update%0A  > a055687 dependencies: update to klog v2.80.0%0A  > 16cba21 Merge pull request # 112129 from pohly/e2e-ginkgo-report-after-each%0A  > e051ad0 dependencies: update to ginkgo v2.1.6 and gomega v1.20.1%0A  > 3a31bb1 Merge pull request # 111934 from deads2k/apply-gen%0A  > 4d73156 Merge pull request # 112052 from tosi3k/bump-client-golang%0A  > 1382941 make applyconfiguration-gen skip generation for types that have generated clients and lack objectmeta%0A  > 03a75ea Bump prometheus/client_golang to v1.13.0%0A  > 17196da update the apply generator to use the same package the the client generator expects%0A  > a4e23d1 Merge pull request # 111566 from inosato/remove-ioutil-from-code-generator%0A  > a6a370c make applyconfiguration-gen handle pointers to slices%0A  > 087714e Merge pull request # 109884 from qzoscar/patch-1%0A  > fc00858 Remove ioutil from code-generator%0A  > ed79ca3 make applyconfiguration-gen work for resources without objectmeta%0A  > fea40fb Merge pull request # 111918 from liggitt/in-tree-auth%0A  > 3612509 fix a broken link%0A  > 78677a3 update the applyconfiguration-gen flag external-applyconfigurations to work%0A  > ad6af70 Revert "Remove gcp and azure auth plugins"%0A  > 7ba56cb applyconfiguration-gen handling of types that have a non-embedded use of TypeMeta%0A  > 97fa351 Merge pull request # 111696 from liggitt/go119mod%0A  > d71f529 add metav1.OwnerReference to the default external configurations to ease generation%0A  > 2b9093f Update go.mod to go1.19%0Abumping golang.org/x/term d974fe8...0edf009:%0A  > 0edf009 go.mod: update golang.org/x dependencies%0Abumping golang.org/x/tools b3b5c13...d0863f0:%0A  > d0863f0 go.mod: update golang.org/x dependencies%0A  > 545ca87 gopls/internal/regtest/marker: require go/packages%0A  > 1ace7db go,gopls: remove license from package doc comments%0A  > ebad375 gopls/internal/lsp/protocol: prevent license rendering in godoc%0A  > 10a39ef gopls/internal/lsp/regtest: address additional comments on marker.go%0A  > 69920f2 gopls/internal/regtest/marker: add missing tests for hover%0A  > 24a13c6 gopls/internal/regtest: fill out features of the new marker tests%0A  > 2b149ce gopls/internal/regtest: add a regtest-based version of the marker tests%0A  > edddc5f go/packages: don't discard errors loading export data%0A  > a762c82 go/ssa: add MultiConvert instruction%0A  > f124b50 cmd/stringer: streamline test subprocesses%0A  > 6b6857a gopls: fix typos in comments and doc%0A  > 8111118 go/analysis/internal/facts: fix cycle in importMap.%0A  > dd1c468 gopls/internal/lsp/source: simplify extracting object hover doc%0A  > 66f8f71 gopls/internal/lsp/source: use syntax alone in FormatVarType%0A  > 30f191f internal/imports: update stdlib index for Go 1.20%0A  > 4e98188 internal/imports: use go/packages instead of cmd/api to compute symbols%0A  > 4e8ff89 internal/imports: update stdlib index for 1.20%0A  > 6bd0d00 gopls/internal/lsp: go to definition from linkname directive%0A  > 0cfddb3 gopls/internal/lsp: enable clear builtin completion test%0A  > 41adf8d gopls/internal/lsp/tests: remove StripSubscripts%0A  > 86fdadc gopls/internal/lsp/safetoken: delete safetoken.Range%0A  > c276ee5 internal/robustio: fix signature of getFileID on plan9%0A  > e170d45 gopls/internal/lsp: add clear builtin%0A  > 2ea4b81 go/ast/inspector: skip ranges that do not contain a node type%0A  > 407bbed go/analysis: improve error message on duplicate fixes%0A  > bd5dfbb all: fix some comments%0A  > 072fca5 gopls/protocol: use the current definition of the lsp%0A  > aa633e7 tools/gopls: provide markdown for completion and signature help%0A  > 684a1c0 go/analysis/internal/analysisflags: use os.Executable for program path%0A  > bd5e595 gopls/internal/lsp/cache: add missing mutex%0A  > 2683128 gopls/internal/lsp: differentiate govulncheck/vulncheck imports diags%0A  > d1e92d6 gopls/internal/lsp/mod: reorder vulncheck quick fixes%0A  > 87d00e6 gopls/internal/lsp: separate some requests from source.Identifier%0A  > ae242ec gopls: fix windows file corruption%0A  > 6f65213 gopls/internal/lsp/protocol: Mapper.NodeMappedRange%0A  > e260368 gopls/semantic: report type parameters in the type of a receiver%0A  > b62cbb6 internal/lockedfile: fix build constraints on solaris%0A  > 1aa7e72 gopls/internal/lsp/source: avoid qualifiedObjectsAtProtocolPos%0A  > 5ed33df gopls/internal/lsp/source: rename: prep for incrementality%0A  > e0659d1 gopls/internal/lsp/source: simplify legacy 'references' func%0A  > 1edcfe7 gopls/internal/regtest/diagnostics: require cgo for TestGoListErrors%0A  > f052158 gopls/internal/lsp/protocol: move TestBytesOffset%0A  > d093a13 gopls/internal/lsp/protocol: LocationTextDocumentPositionParams%0A  > bcb677e gopls/internal/regtest: make RegexpSearch return a Location%0A  > 60782e9 gopls/internal/lsp/source: eliminate a couple uses of posToMappedRange%0A  > 031e6e6 gopls/internal/lsp/source: eliminate ResolveImportPath%0A  > f2cd9ef gopls/internal/lsp/source: reduce usage of TypecheckWorkspace%0A  > f10e7d5 gopls/internal/lsp/cache: remove package dependence on packages.Config%0A  > 8270757 gopls/internal/lsp/source: switch call hierarchy to references v2%0A  > 37c69d8 gopls/internal/lsp/source: references: support exported methods%0A  > f3c36a2 gopls/internal/lsp/cmd/test: delete marker-based tests of gopls cmd%0A  > c224aae gopls/internal/lsp/cmd/test: new integration test for gopls command%0A  > deeb64b gopls/internal/lsp/source/xrefs: allow Lookup of a set%0A  > f269f53 gopls/internal/lsp: remove Server.processModifications%0A  > fcd57eb gopls: allow 'any' and 'comparable' in completion results%0A  > aae3642 gopls/internal/lsp/source: referencesV2: support unexported methods%0A  > b5d65e0 tools/gopls: register semantic tokens statically%0A  > 51abc5b gopls/internal/lsp/source: stub: don't panic when encountering 'error'%0A  > ce28f40 gopls/internal/regtest: add a test demonstrating confusion following an%0A  > c4c6aa6 internal/lsp/cache: don't panic in Snapshot on a shutdown view%0A  > 1faecd3 tools/internal/diff: fix off-by-one error in computing diffs%0A  > a7f033a gopls/internal/lsp: consolidate the FileHandle API%0A  > 271e621 internal/lockedfile/internal/filelock: fix aix build tag%0A  > ff9bea5 gopls/internal/lsp/cmd/test: signpost future cleanups%0A  > 7d4ba2f gopls/release: remove unused functionality from release script%0A  > 46b6958 gopls/internal/lsp/source: delete source_test%0A  > bcc7794 go/analysis/passes/directive: add directive analyzer%0A  > 33d416e gopls/internal/lsp: add missing comments on 3x tests.Test impls%0A  > afea272 gopls/internal/lsp/source: make implementations2 work on embedded fields%0A  > bb7c440 gopls/internal/lsp/filecache: use file locking, not rename%0A  > 561a9be gopls/internal/lsp/filecache: actually delete files%0A  > 9682b0d gopls/internal/lsp/source: delete IsInterface%0A  > 7a7b699 go/analysis/passes/loopclosure: avoid panic in new parallel subtest check when t.Run has single argument%0A  > 3e6f71b gopls/internal/regtest: use AfterChange in more places%0A  > 9ff31a5 x/tools/go/analysis/passes/printf: revert URL in error message%0A  > 2fa6ca1 gopls/internal/lsp/source/impls: a new "implementations" index%0A  > 957bec5 gopls/protocol: new versions of generated LSP files%0A  > f0e2d5c internal/gcimporter: discard position info for unneeded lines%0A  > 5bedd86 cmd/digraph: use ReadString rather than bufio.Scanner%0A  > f6ea009 gopls/internal/lsp: remove the experimentalWatchedFileDelay setting%0A  > f46e418 gopls/internal/lsp/source: include ITVs in global references%0A  > f3e53e5 internal/jsonrpc2_v2: fix typos%0A  > d958e85 internal/gcimporter: use two-level file index%0A  > 8aba49b internal/gcimporter: preserve column and line in shallow iexport%0A  > d7fc4e7 gopls: new LSP stub generator%0A  > 5c176b1 internal/robustio: skip os.Link test on android%0A  > d34a055 go/ssa: sanity check the types of phi nodes%0A  > 6f095b4 go/callgraph/vta: add flows for receiver function types%0A  > 8e94967 cmd/fiximports: do not assume go list -json unmarshals into build.Package%0A  > e035d0c go/ssa: fix phi node type in slice to array conversion%0A  > 03eac81 go/expect: remove testdata go.mod to go.fake.mod%0A  > 1e819a3 gopls/internal/regtest: follow-ups to review comments from earlier CLs%0A  > 9ba8bb1 gopls/internal/regtest: clean up workspace symbol helpers%0A  > 91b6070 gopls/internal/regtest: eliminate DiagnosticAtRegexp%0A  > bd48b9a gopls/internal/regtest: eliminate DiagnosticsAtRegexpWithMessage%0A  > 5d65394 gopls/internal/regtest: eliminate DiagnosticAt%0A  > 27dfeb2 gopls/internal/regtest: replace NoDiagnostics with NoMatchingDiagnostics%0A  > 87092c8 gopls/internal/lsp/fake: use protocol types for the fake editor%0A  > 672a036 gopls/internal/regtest: simplify OnceMet expressions with an env helper%0A  > ab7b5b2 gopls/internal/regtest: eliminate GoSumDiagnostic%0A  > 331a1c6 gopls/internal/regtest: add a simpler API for diagnostic expectations%0A  > c9b82f2 gopls/internal/regtest: eliminate EmptyDiagnostics%0A  > e81af27 gopls: update golang.org/x/vuln@6ad3e3d%0A  > d19e3d1 internal/regtest/bench: fix BenchmarkRename and add more benchmark tests for gopls%0A  > 2be1a9a gopls/internal/regtest: rename EmptyOrNoDiagnostics to NoDiagnostics%0A  > 7ec05ac gopls/internal/regtest: eliminate NoDiagnostics%0A  > e956495 gopls/internal/regtest: eliminate DiagnosticsFor%0A  > 8087911 gopls: remove the experimentalWorkspaceModule mode%0A  > 5b300bd gopls/internal/lsp/cache: clean up view workspace information%0A  > 97d5de5 gopls/internal/cache: don't mark initialized after cancellation%0A  > 58691bc gopls/internal/lsp/glob: add an LSP compliant glob implementation%0A  > a3c22fc cmd/cover: delete package%0A  > 98dcb0e cmd/cover: remove replace directive%0A  > 7765567 gopls/internal/lsp/source: minor clarifications%0A  > a7f7db3 cmd/cover: carve out deprecated command into its own module%0A  > f9a10c0 Revert "cmd/cover: carve out deprecated command into its own module"%0A  > e345d46 internal/gcimporter: fix export of invalid methods%0A  > 4305a22 gopls/internal/lsp/cache: don't cache files if mtime is too recent%0A  > 227ee72 internal/regtest/misc: fail eagerly in TestRenameFileFromEditor%0A  > 43158af cmd/cover: carve out deprecated command into its own module%0A  > b798934 gopls/internal/lsp/protocol: cleanups and docs for Mapper%0A  > a24944e gopls/internal/lsp/protocol: rename s/ColumnMapper/Mapper/%0A  > 55935f4 gopls/internal/span: simplify Span%0A  > 40a1c97 gopls/internal/lsp/lsppos: delete Mapper%0A  > 6a3bc37 gopls/internal/lsp/protocol: reimplement ColumnMapper line logic%0A  > 6e9a35d go/callgraph/cha: refactor callee construction%0A  > fef5b76 go/callgraph: fix slicing in callgraph_test.go%0A  > 2be9d05 gopls/internal/lsp/source/xrefs: a new reference index%0A  > 0362cea gopls/internal/lsp/lsppos: delete TokenMapper%0A  > 67baca6 go/callgraph/vta: optimize scc computation%0A  > 2eb6138 gopls/internal/lsp/filecache: use TempDir if UserCacheDir fails us%0A  > 36bd3db gopls/internal/lsp/protocol: move MappedRange%0A  > 16b3bf8 gopls/internal/lsp/cache: assume Go 1.16+%0A  > 3856a5d internal/robustio: add Plan9 support to FileID%0A  > 09cbc42 gopls/internal/lsp/fake: fix EOF bug in applyEdits%0A  > 4ded35d gopls/internal/lsp/cache: use distinct types for mod and work parse keys%0A  > 107f43f gopls/completion: avoid duplicating text in test func completions%0A  > e225fd4 gopls/internal/lsp/mod: fix nil panic in go.mod hover%0A  > 057ed3c gopls/internal/lsp/filecache: use os.Chtimes%0A  > 1fe76af gopls/internal/lsp/source: MappedRange cleanup%0A  > 02bea03 gopls/internal/lsp/protocol: simplify ColumnMapper%0A  > a4455fe go/callgraph: adds benchmarks comparing algorithms%0A  > 7db99dd go.mod: update golang.org/x dependencies%0A  > 1e0dff2 gopls/internal/regtest: avoid race in TestSwitchFromGOPATHToModuleMode%0A  > 0441b43 gopls/internal/lsp/cache: use specific mutexes for module data%0A  > 33071fb internal/robustio: move robustio%0A  > b01e7a4 gopls/internal/regtest/watch: don't run TestSwitchFromGOPATHToModuleMode%0A  > e417ea3 gopls: remove dead analysis code%0A  > 1a08d01 gopls/internal/lsp: update replace directives in go.mod for package renaming%0A  > eac36cb gopls/internal/regtest: port experimental workspace tests to go.work%0A  > 224a61b gopls/internal/lsp/source: delete Snapshot.WriteEnv method%0A  > 81e741e gopls/internal/lsp/safetoken: funnel more calls through this package%0A  > 8367fb2 gopls/internal/regtest: await go.work changes in TestAddAndRemoveGoWork%0A  > 3b16059 gopls/internal/regtest: make BufferText strict%0A  > 0e1d013 gopls/internal/lsp/cache: recreate Views when their root changes%0A  > 2f31dd4 go/ssa,go/analysis/passes/nilness: refine when type param constants are nil%0A  > ae4ff82 gopls/internal/lsp/source: delete GetTypedFile%0A  > fe6b300 gopls/internal/lsp/source: eliminate Snapshot.Package{,s}ForFile%0A  > 26fc609 gopls/internal/lsp/cache: eliminate snapshot.containingPackages%0A  > 85e6ad7 gopls/internal/lsp/safetoken: fix bug in Offset at EOF%0A  > ef1ec5d gopls/internal/lsp/safetoken: fix error message%0A  > 44395ff gopls/internal/lsp/source: avoid unnecessary transitive rdeps%0A  > 6546d82 Revert "gopls/internal/regtest: harmless CL used for benchmark test"%0A  > 3be0647 gopls/symbols: call source.Document symbols only for Go files%0A  > d462c83 gopls/internal/lsp: Replace input text when completing a definition%0A  > 7efffe1 gopls/internal/regtest: harmless CL used for benchmark test%0A  > 1627e95 gopls/internal/lsp: more comment tweaks post-//line support%0A  > 21f6100 internal/lsp/debug: fix broken template%0A  > 6ad27d0 gopls/internal/robustio: FileID, a portable file identifier%0A  > 6df6eee internal/diff/lcs: optimize inner loop%0A  > 57b1265 go/gcexportdata: drop support for go1.6 export data%0A  > 099260e gopls/internal/lsp: followups to dropping line directives%0A  > 61e2d3f gopls/internal/lsp/cache: a new analysis driver%0A  > eb70795 gopls: ignore //line directives%0A  > b4dfc36 go/ssa: deref core type in emitLoad%0A  > 1270fd7 gopls/internal/lsp: announce selectionRangeProvider capability%0A  > 9bc5dce gopls/internal/lsp/cache: simplify DiagnosePackage%0A  > df35cd8 x/tools: drop support for Go toolchains older than go1.16%0A  > db9d10f go/gcexportdata: preallocate buffer to read into when size is known%0A  > 0d2045b gopls/internal/lsp: document analysis-related functions%0A  > b2b9dc3 gopls/internal/lsp/cache: reduce type-checking in renameImports%0A  > 3cb82d5 go/ssa/interp: fix conversion of slice to named array%0A  > 5899b6a gopls: upgrade dependencies following release%0A  > 763a030 gopls/internal/lsp/cache: delete Snapshot.KnownPackages%0A  > cc0e696 gopls/internal/hooks: panic if diff consistency check fails%0A  > 9ec8553 gopls/internal/lsp/source: emit interface stub methods at top level%0A  > 444c8f6 gopls/internal/lsp/cache: only invalidate parsed files if they changed%0A  > 601ca6c gopls/internal/lsp/source: use correct token.File%0A  > 95c9dce internal/lsp/mod: fix run_govulncheck codelens name%0A  > d72a64a gopls/internal/lsp: add selection range request%0A  > 18f76ec gopls/internal/lsp: split ActivePackages%0A  > 84299a0 gopls/internal/lsp/cache: simplify ad-hoc package warning logic%0A  > a3eef25 gopls/internal/lsp/cache: record parse keys when they're created%0A  > 3da7f1e gopls/hover: remove header tags from hover markdown%0A  > a310bcb gopls/internal/lsp/source: eliminate getStubFile%0A  > 3cba5a8 internal/gcimporter: port CL 424876 from std importer%0A  > b0fdb78 gopls/internal/lsp/mod: add Reset vulncheck result codelens%0A  > 88ceb24 gopls/internal/lsp: perform analysis unconditionally%0A  > 3f74d91 gopls/internal/lsp/cache: invalidate govulncheck results older than 1hr%0A  > 6b8674f gopls/internal/lsp/source: avoid typechecking in findRune%0A  > d7dfffd gopls/internal/lsp: eliminate more unnecessary typechecking%0A  > f3fb218 gopls/internal/lsp/fake: use robustio.RemoveAll in (*Workdir).RemoveFile%0A  > 96ff41d gopls/internal/vulncheck: add TODO for the vulncheck diagnostics%0A  > 0f6c6f1 gopls: delete obsolete govulncheck code and stop gopls vulncheck -summary%0A  > c5343a6 gopls/internal/lsp/regtest: fix TestRunGovulncheckError2%0A  > cb701f7 gopls/internal/lsp: avoid type-checking when computing hyperlinks%0A  > d0f184d gopls/internal/lsp/source: avoid unnecessary calls to GetTypedFile%0A  > 1e5efed gopls/internal/lsp/fake: simply use polling to simulate file watching%0A  > 838a165 gopls/internal/lsp/fake: eliminate the unnecessary fake.FileEvent%0A  > 09fb680 gopls/internal/lsp/fake: eliminate the unnecessary ChangeFilesOnDisk API%0A  > 09ae2d5 gopls/internal/lsp/source: KnownPackagePaths: avoid loading%0A  > 1dcc423 gopls/internal/lsp/cache: split metadata and loading in PackagesForFile%0A  > 6b50501 gopls/release: fix the release script when go.work is not used%0A  > aee3994 gopls/internal/lsp/fake: in (*Workdir).RenameFile, fall back to read + write%0A  > fe60148 go.mod: update golang.org/x dependencies%0A  > c9ea9a7 gopls/internal/regtest: add a test for the case when the renaming package's path contains "internal" as a segment%0A  > bf5db81 gopls/internal/lsp/cache: improve ad-hoc warning for nested modules%0A  > aa9f4b2 go/analysis: document that facts are gob encoded in one gulp%0A  > bdcd082 internal/gcimporter: skip tests earlier when 'go build' is not available%0A  > 2ad6325 gopls/internal/lsp/cache: expand ImportPath!=PackagePath comment%0A  > 52c7b88 gopls/internal/robustio: only define ERROR_SHARING_VIOLATION on Windows%0A  > 4f69bf3 gopls/internal/lsp/cache: narrow reloadOrphanedFiles to open files%0A  > 6002d6e gopls/internal/regtest/misc: test Implementations + vendor%0A  > f540ee6 internal/gcimporter: load cached export data for packages individually%0A  > d444fa3 gopls/internal/lsp/cache: simplify canonical URI cache%0A  > 25fdb81 gopls/internal/regtest/misc: skip vendor test on go1.13%0A  > e0b516b gopls/internal/lsp/cache: invalidate metadata after vendor change%0A  > 31d5843 gopls/internal/lsp/cache: fix re-entrant session locking%0A  > 8c78b30 gopls/internal/vulncheck: always use pkg.go.dev/vuln for urls%0A  > 47a8246 gopls/internal/regtest/misc: skip TestRunGovulncheckError2%0A  > d54e12b gopls/internal/lsp: avoid I/O in URI comparison operations%0A  > 0379b73 internal/gcimporter: fix TestImportStdLib%0A  > e79e423 gopls/internal/vulncheck: handle package errors%0A  > c5ce806 gopls/internal/lsp/mod: disable the diagnostics on stdlib vulns%0A  > 78c1861 gopls/internal/vulncheck: clarify the log message%0A  > 1a0053c gopls: move reset go.mod diagnostic codelens to module statement%0A  > 9b8d87b gopls/internal/regtest: fix TestRunGovulncheckStd%0A  > 81b6bef gopls/internal/lsp: add run vulncheck fix for stdlib vulns%0A  > fe83ddb gopls/internal/lsp: move options off of the cache%0A  > 88ee30b gopls/internal/lsp/source: enable run_govulncheck codelens in exp mode%0A  > 0a6aa90 gopls/internal/lsp/command: rename run_vulncheck_exp to run_govulncheck%0A  > bedad5a gopls/internal/lsp/mod: add hover for stdlib vulnerabilities%0A  > 7a1b570 gopls/internal/vulncheck: check vulnerabilities in standard library%0A  > 9a54670 gopls/internal/lsp/mod: add "Run govulncheck" codeaction%0A  > f1b76ae gopls/internal/lsp: add an option to overwrite previous diagnostics%0A  > e8a70a5 gopls/internal/lsp: remove access to mutable session state from the view%0A  > ff22fab gopls/internal/lsp/cache: eliminate obsolete invalidation step%0A  > 3881046 gopls: add a go:generate rule for doc generation%0A  > 4c3cb1e internal/gocommand: add GoVersionString%0A  > e29d1ed gopls: add diagnostic for standard library%0A  > f718365 gopls/internal/lsp: include all vulns info to fetch_vulncheck_result%0A  > 9519368 gopls/internal/lsp/mod: add the vulncheck diagnostics mode%0A  > 7d9f451 gopls/internal/govulncheck: add in-memory cache for vulndb%0A  > 1ccccf8 go/ssa: deprecate coreType and _NormalTerms%0A  > 4b7d1b3 gopls: add diagnostics for both vulns used and not used%0A  > 50ccef5 internal/regtest/bench: add benchmark tests for gopls%0A  > d39685a gopls/internal/lsp/source: Package clarifications%0A  > 7cfde84 gopls/internal/vulncheck: add import info based vuln scanning%0A  > 2b56641 internal/gcimporter: adjust the number of expected packages in TestStdlib%0A  > 50df761 gopls: skip vulnerabilities that are probably fixed in hover%0A  > 7cda55e gopls/internal/lsp/cache: wire in mod vulnerability analysis%0A  > 5c35617 gopls: add quick fixes for all vulnerabilities%0A  > fb7be64 gopls/internal/lsp/command: return the vulncheck progress token%0A  > 060c049 go/packages: fix doc typo%0A  > 6eafd96 gopls: fix formatting for vulncheck results in hover%0A  > b797704 go/analysis/passes/loopclosure: recursively check last statements in statements like if, switch, and for%0A  > 3b9d20c internal/gcimporter: in TestStdlib, only check x/tools packages if we expect to have their source%0A  > 2ad3c33 go/packages: change workaround for issue 28749 to not require NeedFiles%0A  > 57f56ab gopls/internal/lsp/source: avoid panic(nil)%0A  > 41c70c9 internal/lsp/source: avoid using go/types.Implements with Typ[Invalid]%0A  > db5eae2 analysis: correct go/analysis/passes/findcall path in docs%0A  > b978661 cmd/godoc: streamline test subprocesses%0A  > 932ec22 internal/testenv: add a Command function that replaces exec.Command%0A  > 19fb30d gopls/internal/lsp/cache: fix data race in Symbols%0A  > 4ce4f93 gopls/internal/lsp: add gopls.fetch_vulncheck_result%0A  > 8ba9a37 gopls/internal/lsp/mod: highlight when there is no fix for vuln%0A  > 128f61d gopls/internal/lsp/mod: add related info%0A  > fc03993 internal/lsp/mod: adjust vulncheck diagnostics suppression logic%0A  > c099dff gopls/internal/vulncheck: log progress%0A  > 36a5c6a go/ssa: build generic function bodies%0A  > 85bf7a8 gopls/internal/lsp/source: eliminate Metadata interface%0A  > 2592a85 gopls/internal/lsp: simplify KnownPackages%0A  > c7ed4b3 gopls/internal/lsp/cache: clean up tracking of GO111MODULE%0A  > 23056f6 internal/lsp/cache: clean up getOrLoadIDsForURI%0A  > 5a4eba5 internal/lsp/cache: remove support for invalid metadata%0A  > 32a17c0 gopls/internal/lsp/mod: fix unaffecting vuln diagnostics msgs%0A  > dea100b internal/testenv: skip tests that need export data for std if 'go tool compile' does not exist%0A  > ba373ee playground/socket: eliminate an arbitrary timeout in TestLimiter%0A  > 3d085f3 gopls/internal/lsp/lsprpc: eliminate arbitrary timeout in TestEnvForwarding%0A  > 434d569 gopls/internal/lsp/regtest: improve documentation%0A  > ce26db4 go/analysis: add Pass.TypeErrors field%0A  > b0ad6b2 gopls/internal/regtest/misc: fix use of the AfterChange API%0A  > 89856a4 gopls/semantic: semantic tokens for type parameters%0A  > 6e8da3f internal/pkgbits: port small optimization from compiler to tools%0A  > 06fb723 internal/gcimporter: port memory reuse optimizations from Go tree%0A  > fc702c5 internal/gcimporter: fix performance regression for unified IR%0A  > 1cb4c17 gopls/internal/regtest: make AfterChange do the awaiting%0A  > 0c71b56 gopls/internal/lsp: fix diagnostic suppression when folders change%0A  > e3b3c01 go/pointer: break TestInput into subtests and update skips%0A  > 13648cd gopls/internal/lsp/cache: use Package.FileSet where possible%0A  > 8f32411 cmd/stringer: replace ioutil with os%0A  > 3c3713e gopls/internal/lsp/cache: use typed strings (PackagePath et al) throughout%0A  > 004d118 gopls/internal/lsp/mod: simplify ModVulnerabilityDiagnostics%0A  > 4a8413c gopls/internal/lsp/mod: deleted unused function pkgVersion%0A  > bc08991 gopls: sync golang.org/x/vuln@3af8368ee4fe%0A  > d66e9b4 internal/typesinternal: update go/types error codes for 1.20%0A  > 6f99366 gopls/internal/lsp/cache: don't pass snapshot.fset to go/packages%0A  > d56532a cmd/compilebench: make it work without installed .a's%0A  > 502c634 go.mod: update golang.org/x dependencies%0A  > bd04e32 internal/jsonrpc2_v2: eliminate a potential Accept/Dial race in TestIdleTimeout%0A  > d41a43b internal/jsonrpc2_v2: fix a potential deadlock when (*Conn).Close is invoked during Bind%0A  > 3057465 gopls/doc: Add plugin for Lapce to gopls documentation%0A  > ba92ae1 internal/persistent: avoid incorrect map validation due to multiple keys%0A  > 9474ca3 gopls/doc: clarify `go work use`%0A  > 003fde1 internal/gcimporter: use nondeprecated go/packages mode bits%0A  > 5050657 gopls/fake: add semantic token modifiers to fake editor%0A  > 88a3548 gopls/coverage: repair coverage.go%0A  > 8e0240a internal/regtest/workspace: permanently skip TestDeleteModule_Interdependent%0A  > fe725d9 gopls/internal/regtest: simplify awaiting diagnostics from a change%0A  > 3c8152e internal/gcimporter: optimize dependency lookup%0A  > 39c2fd8 internal/lsp/cache: simplify importsState modfile hashing logic%0A  > ec044b1 gopls: update dependencies following the v0.10.0 release%0A  > 2b29c66 internal/gcimporter: API for shallow export data%0A  > affa603 internal/gcimporter: moved from go/internal/gcimporter%0A  > a77a1fb gopls/internal/lsp/mod: fix vulncheck hover message%0A  > 4ada35e gopls/internal/lsp: handle modVulncheckSource in diagnosticSource.String%0A  > e5f03c1 gopls/doc: clean up README and add a release policy%0A  > d5e9e35 go/analysis/passes/loopclosure: enable analysis of parallel subtests%0A  > 039b24b internal/jsonrpc2_v2: initiate shutdown when the Writer breaks%0A  > 32e1cb7 gopls/internal/lsp: clarify control around diagnostics%0A  > feeb0ba gopls/internal/lsp/cmd: fix deadlock when opening a file%0A  > 6e9dc86 gopls/internal/lsp/source/completion: fix panic in completion on *error%0A  > 73fcd88 Revert "internal/jsonrpc2_v2: initiate shutdown when the Writer breaks"%0A  > 70a130e gopls/api-diff: simplify the api-diff implementation%0A  > 3e8da47 internal/jsonrpc2_v2: initiate shutdown when the Writer breaks%0A  > 3566f69 gopls/internal/lsp/source: minor space optimizations%0A  > 7cdb0e7 internal/jsonrpc2_v2: rename Serve to NewServer and eliminate its error return%0A  > 28e9e50 internal/jsonrpc2_v2: eliminate error return from Bind%0A  > eabc3a0 internal/jsonrpc2_v2: eliminate isClosingErr%0A  > 4885f7c internal/jsonrpc2_v2: eliminate a temporary connection leak in (*Server).run%0A  > 739f55d internal/jsonrpc2_v2: rework Connection concurrency%0A  > e172e97 go/types/typeutil: break recursion through anonymous interfaces%0A  > f1c8f7f internal/lsp/source: optimize filter regular expression%0A  > e074ef8 gopls/internal: don't show a warning if the Go version is undetected%0A  > 7fba77c gopls/internal/lsp/source: remove deprecated settings from EnableAllExperiments%0A  > 42cb7be gopls/internal/lsp: improve the Go version deprecation message%0A  > 2af106e gopls/internal/hooks: fixes to diff disaster logic%0A  > e4bb343 go/internal/gcimporter: update to anticipate missing targets and .as%0A  > 875c31f go/internal/gcimporter: add test of export/import on std%0A  > 541f4c5 cmd/bundle: quote command-line arguments in output%0A  > de675d5 tools/gopls: argument in function bodies marked as parameter by semantic tokens%0A  > 3e1371f gopls/internal: start on LSP stub generator in Go.%0A  > 121f889 gopls/internal/lsp/mod: merge vuln diagnostics to one, and add a hover%0A  > d6511e5 internal/facts: share go/analysis/internal/facts with gopls%0A  > 2e0ca3a go/internal/gcimporter: fix bug in struct iexport%0A  > 1928cea go/ssa: emit field and index lvals on demand%0A  > 8166dca go/analysis/passes/asmdecl: define register-ABI result registers for RISCV64%0A  > 2dcdbd4 go/internal/gcimporter: port CL 431495 to tools, add tests%0A  > d476af7 go/ssa: add slice to array conversion%0A  > d212f7d gopls/internal/regtest/workspace: fix bugs in test%0A  > 051f03f gopls/internal/lsp/cache: remove unnecessary params%0A  > 21f6127 gopls/internal/lsp/cache: add PkgPath->PackageID index to Metadata%0A  > 06041c9 gopls/doc: update manual documentation of the newDiff setting%0A  > f112c43 go.mod: update golang.org/x dependencies%0A  > 207f456 go/internal/gcimporter: bump version number in skew check%0A  > 65196ca gopls/README.md: fix wording around supported Go versions%0A  > 6128030 gopls/internal: support renaming packages with int. test variants%0A  > 649df2e go.mod: mark as requiring -compat 1.16%0A  > 91311ab gopls/internal/lsp/cache: better import path hygiene%0A  > 9eda97b go/analysis: enable a test that applies after go list behavior change%0A  > b50d7ba gopls: minor cleanup of standalone package support%0A  > 502b93c gopls/internal/lsp: tolerate missing end position in RelatedInformation%0A  > d67c3ad internal/imports: repair warnings from default analyzers%0A  > bc2e3ae internal/jsonrpc2_v2: add Func convenience wrappers for the Binder and Preempter interfaces%0A  > a9b653b cmd/compilebench: use -a instead of -i to ensure dependencies are built%0A  > 4818d9e Revert "gopls/internal/lsp/cache: disable strict analysis while we fix panics"%0A  > b2efd4d internal/jsonrpc2_v2: eliminate most arbitrary timeouts in tests%0A  > 371ef16 internal/jsonrpc2_v2: rework concurrency in idleListener%0A  > 5935531 internal/jsonrpc2_v2: remove “Box” suffix from channel field names%0A  > fd32990 internal/jsonrpc2_v2: error out in-flight client calls when the reader breaks%0A  > 0e222f5 internal/jsonrpc2_v2: close the underlying connection if Wait is called instead of Close%0A  > bc4e384 gopls/internal/lsp/cache: fix crash in analysis%0A  > b93a56f refactor/satisfy: fix visiting functions in the unsafe package%0A  > 9b5e55b gopls/internal/lsp/cache: disable strict analysis while we fix panics%0A  > 9ffaf69 gopls/internal/lsp/cache: minor analysis cleanups%0A  > ffb862b gopls/internal/lsp/cache: remove stray print statement%0A  > f87c1ed internal/fastwalk: improve Darwin performance by ~3x%0A  > b253314 gopls/internal/lsp/cache: add support for loading standalone main files%0A  > 3beecff gopls/internal/span: some cleanups%0A  > d375238 gopls: dedup upgrade code actions for vulncheck%0A  > b20ae4b README: format install command%0A  > 19a5504 gopls/internal/lsp: use the golang.org/x/vuln/exp/govulncheck%0A  > ab79327 cmd/ssadump: disable run mode with runtime package%0A  > 29429f5 gopls/internal/lsp/source: sort protocol edits%0A  > 49b340b go/analysis: update tests for different go list error behavior%0A  > cd0288f internal/lsp/cache: invalidate analysis results on packages.Load%0A  > 906c733 gopls/internal/lsp/source: find references in test packages%0A  > 2a41b25 internal/robustio: fix log.Fatal calls that should be log.Fatalf%0A  > 150b5f8 internal/imports: read entire API dir in mkstdlib.go%0A  > 19cfa79 internal/lsp/source: switch the default diff algorithm to "checked"%0A  > fa6bd3b gopls: include informational vulnerability diagnostics%0A  > 89b4335 gopls/internal/lsp: merge notifications about deprecated settings%0A  > f90d8ad all: fix a few function names on comments%0A  > 350f1e2 gopls/internal/lsp/fake: retry ephemeral errors when renaming on windows%0A  > 8b1d1ec gopls/internal/lsp/cache: suppress panics during analysis%0A  > 20c1ee7 gopls/internal/lsp: warn about Go versions that are too old%0A  > 709f108 gopls/internal/lsp/cache: suppress crashes in fact_purity analyzer%0A  > a410e98 internal/diff: ToUnified may fail%0A  > 26a95e6 gopls/internal/span: move internal/span into gopls%0A  > f2c4579 internal/diff: avoid unnecessary allocations%0A  > 60ddcca internal/diff: Apply: validate inputs%0A  > 02bef08 go/packages/packagestest: break dependency on gopls' span package%0A  > 778f945 go/analysis: break dependency on span package%0A  > c682555 gopls/internal/regtest/misc: delete testdata%0A  > 1552529 gopls/internal/regtest/misc: use vulntest for vuln_test%0A  > c4f49e4 go/analysis/passes/assign: fix map assignment%0A  > bd8c28f internal/diff/lcs: fix shell format error%0A  > ede3ab2 gopls/internal/lsp/protocol: simplify OffsetRange, Position%0A  > dc3cf95 gopls/internal/vulncheck: use vulntest for test database creation%0A  > 4ef38dc gopls/internal/vulncheck/vulntest: add test helpers%0A  > 2f57270 gopls: update golang.org/x/vuln%0A  > d96b238 internal/diff: simplify API, break span dependency%0A  > 9856077 internal/diff: abolish errors%0A  > 33c2dbf gopls/internal/lsp: remove extra newlines in vulncheck diagnostics%0A  > b280e27 gopls/internal/lsp/cache: make IsIntermediateTestVariant a method%0A  > c5514b7 gopls/internal/lsp/source: use PackageFromFile in Identifier%0A  > ff4ff8b gopls/internal/lsp/source: don't type-check in FindPackageFromPos%0A  > 2d32e15 gopls/internal/lsp/cache: in tests, show all stacks during analyzer crash%0A  > dc88e7b godoc: fix some comments%0A  > 7f79a02 gopls: use fmt.Fprintf%0A  > 40dabfa gopls/internal/lsp: add support for package renaming%0A  > 55e5cff internal/diff: unified: match GNU diff for empty file%0A  > 3e0355b gopls/.../fillstruct: support generic types%0A  > ed98f10 gopls: prefix vulncheck diagnostic message with title%0A  > b180eff x/tools/go/analysis: extend json output by SuggestedFixes%0A  > d49f960 internal/lsp/cache: report analysis panics during testing%0A  > 27641fb gopls: suggest upgrading to fixed version for vulncheck diagnostics%0A  > 199742a go/analysis/passes/printf: check for nil scope of instance methods%0A  > 3db607b gopls/internal/lsp/cache: remove "discovered missing identifiers" log%0A  > a4274a8 gopls: add diagnostics for non-stdlib vulnerabilities%0A  > f80e984 gopls/internal/lsp/work: use the WorkFileError diagnostics source%0A  > 9c63911 gopls/internal/lsp: delete dead code%0A  > ae737bc gopls/internal/lsp: remove the source.Session interface%0A  > bddb372 gopls: deprecate three experimental features%0A  > 4dd4ddb go/packages: issue error if 'go list' on PATH is too new%0A  > 10e9d3c gopls/internal/lsp: tolerate new 'imported and not used' error message%0A  > eb45e98 gopls/internal/regtest: fix regtest failures from "undefined" errors%0A  > 1bfc469 gopls: update to handle 'undefined:' versus 'undeclared' in type errors%0A  > 5214f41 internal/gocommand: show pid of process%0A  > c5cd943 gopls: fix the reset_golden.sh script and regenerate golden files%0A  > 49a686d go/analysis: update explanation of (no) Diagnostics.Severity%0A  > eb25de6 go/analysis/passes/loopclosure: only check statements after t.Parallel%0A  > b243e57 gopls/internal/lsp/tests: simplify collectCompletionItems, remove Data.t%0A  > 88b5529 gopls/internal/lsp/tests: use the mustRange helper in more places%0A  > c7ac942 gopls/internal/lsp: simplify prepareRename tests%0A  > b9adce9 internal/lsp/source: derive document symbols from syntax alone%0A  > 3dda4ba all: replace deprecated egrep with grep -E%0A  > 1877b5f go/analysis/passes/printf: permit multiple %w format verbs%0A  > b3ab50b go/analysis/passes/stdmethods: recognize Unwrap() []error%0A  > 62ae586 gopls/test: disable stderr output for command line tests as well%0A  > be3ff02 go/analysis/passes/sortslice: correct diagnostic for sort.Slice(f())%0A  > 2f04713 gopls: fix out of bounds bug in extract%0A  > 16b9742 go/analysis/passes/loopclosure: use go/types' object resolution%0A  > 81a42f0 gopls/internal/lsp/tests: pass in a *testing.T to Data.Golden%0A  > 14462ef go/analysis/passes/loopclosure: experiment with checking t.Run+Parallel%0A  > 00ae48e go/internal/pkgbits: replace os.SEEK_CUR with io.SeekCurrent%0A  > 835bfdf gopls: update x/vuln to pick fix for incorrect version suggestion%0A  > 6782af0 gopls/internal/lsp/source: clarify qualifiedObject%0A  > f901623 gopls/internal/lsp: suppress noisy log output in tests%0A  > df2eb93 gopls/test: fix erroneously skipped tests, remove redundant cmd tests%0A  > 1578244 gopls: set codelensProvider in initialize response%0A  > fdf581f internal/lsp: allow extract func ranges to begin/end with comments%0A  > b256f1f gopls/internal/lsp/cache: remove distracting "safe trimming" log%0A  > 0e011a0 all: use constant to avoid repeated definitions%0A  > 4d18923 gopls/internal/fake: sort edits by both start and end position%0A  > 45ad958 gopls/internal/lsp/protocol: fix json tags and indirect some zero values%0A  > a61f20e internal/gocommand: tweak debugging for hanging go commands%0A  > cdd6986 gopls/tsprotocol: make Disabled in CodeAction optional%0A  > 0398b3d internal/gocommand: add instrumentation for hanging go commands%0A  > 9250e22 internal/lsp: latest version of LSP stubs%0A  > ec74389 gopls/internal/lsp/source: make "chatty" diagnostics the default%0A  > 7e129ca gopls: add codelens to reset upgrade diagnostics%0A  > a81fce3 gopls: run go mod tidy -compat=1.16%0A  > a8b9ed3 gopls/internal/lsp/source: remove Govulncheck from Hooks%0A  > 678efe0 gopls/internal/lsp/cmd: fix vulncheck error handling%0A  > e71c338 go/ssa/ssautil: initialize info when there is syntax%0A  > 0eebaab go/analysis: allow for identical SuggestedFixes%0A  > eeaf4eb internal/lsp/fake: add rename file support for testing%0A  > 4754f75 go/analysis/passes/copylock: modify match pattern to satisfy change sync.Once.done to atomic.Bool%0A  > a630751 x/tools: update go.mod following moving LSP code to x/tools/gopls%0A  > 308e02c x/tools/go/ssa: disable slice-to-array test%0A  > 3ee1710 gopls/doc: update stale documentation and improve link names%0A  > 5f27e05 all: remove redundant type conversion%0A  > b15dac2 gopls: migrate internal/lsp to gopls/internal/lsp%0A  > dd1bab2 go/analysis/passes/printf: fix panic parsing argument index%0A  > bac5507 go/analysis/internal/checker: make applyFixes work from the first character%0A  > c1dd25e gopls/internal/migrate.sh: a script to migrate internal/lsp to gopls/%0A  > 83d7619 gopls : add a mention of staticcheck to settings documentation%0A  > d815cba internal/lsp: update LSP protocol for WorkspaceEdit%0A  > 6a585a2 x/tools/internal/typeparams: use regexp to match wanted result%0A  > be9eab1 go/analysis/passes/inspect: fix example return%0A  > 5ba8541 x/tools/internal/lsp/source: disable some tests for std lib changes%0A  > eb8352e gopls/internal/govulncheck: sync x/vuln@62b0186%0A  > 655abda gopls/internal/regtest: TestEditGoDirectiveWorkspace should fail eagerly%0A  > 33c1ddd tools/gopls/internal/regtest/diagnostics: handle new error message%0A  > 40cfaff x/tools/internal/lsp/source: disable some tests for std lib changes%0A  > f16be35 internal/lsp/source: add functions to type hover output%0A  > dfc8d49 internal/lsp/testdata: fix diagnostics checksum%0A  > 6c10975 internal/lsp/cache: honor RunDespiteErrors=false%0A  > 49ab44d x/tools/internal/lsp: re-enable a test with adjusted error message%0A  > 550e1f5 internal/lsp/tests: use a shorter module path for test data%0A  > 4ccc73c internal/lsp/tests: simplify comparison of markdown at go1.18%0A  > 3eb8a8f internal/lsp/cache: delete misleading Package.IllTyped method%0A  > cb91d6c internal/lsp/cache: clarify error control flow of analysis%0A  > 41c3a9b internal/lsp/analysis/fillreturns: be defensive w.r.t. type errors%0A  > fe1a27b gopls/doc: make doc generation work regardless of the current directory%0A  > ddbeb75 internal/lsp: run internal/lsp/reset_golden.sh%0A  > 248c34b internal/lsp: support regular expressions in Diagnostics tests%0A  > 431f4ef internal/lsp/tests: re-enable ARM tests%0A  > 717a671 go/analysis/passes/printf: remove unused hasBasicType%0A  > 7f23307 internal/lsp: limit diagnostics for upgrades to codelens go.mod file%0A  > 7c5e035 internal/lsp: fix suppressed panic in analyzer%0A  > 2f38e1d internal/lsp/tests: disable failing test on ARM%0A  > d35bb19 internal/lsp/tests: improve assertion error message%0A  > 7111c2e x/tools/internal/lsp: disable a test so we can change the parser error%0A  > db6a62c go/internal/gcimporter: call Interface.Complete in unified importer%0A  > 587a153 internal/lsp: hover to render go 1.19 doc comments%0A  > e55fb40 internal/lsp/cache: clear shouldLoad IDs on load%0A  > a3cac11 godoc/redirect: delete golang.org-specific code%0A  > b3851a8 internal/lsp/cache: tweaks to metadata graph%0A  > 938e162 gopls/internal/regtest: unskip TestDeleteModule_Interdependent%0A  > e8507be gopls/internal/regtest/bench: replace -gopls_version with -gopls_commit%0A  > 8c83056 gopls/internal/regtest: unskip TestSumUpdateFixesDiagnostics%0A  > 987de34 internal/lsp/completion: don't use Type.String for checking identity%0A  > 5a26068 internal/lsp/source: remove utm_source from pkgsite links%0A  > 35f806b gopls/doc/workspace: correct grammar%0A  > bebd890 go/analysis: remove stray print statement in the timeformat analyzer%0A  > 88d981e printf analyzer: link to fmt#Printing for verb/type docs%0A  > c4ec74a go/internal/pkgbits: fix performance of rawReloc%0A  > 37a81b6 internal/lsp: add unnecessary tags for unused vars and imports%0A  > 3807419 internal/lsp/cache: validate the range for critical errors in go files%0A  > b2156b5 gopls: update dependencies%0A  > 0ad49fd internal/imports: update stdlib index for 1.19%0A  > 3950865 gopls/internal/regtest/bench: add a -gopls_version flag%0A  > 6fa767d internal/lsp: update documentation for directoryFilters setting and default value%0A  > 96d05aa gopls/internal/regtest: fix TestFailingDiagnosticClearingOnEdit%0A  > 4ff08b4 gopls: Improve auto-imports example for NeoVim LSP%0A  > 92d58ea internal/lsp/cache: register a file watcher for explicit GOWORK values%0A  > 98aef77 internal/lsp/cache: track explicit go.work files outside the workspace%0A  > fff6d6d internal/lsp: update the broken workspace message to mention go.work%0A  > 9b60852 gopls/internal/regtest: move TestMultipleModules_Warning to ./workspace%0A  > 06d96ee gopls/internal/regtest/bench: add a test for completion following edits%0A  > 81c7dc4 internal/lsp: polish vulncheck progress messages%0A  > af2a0a8 internal/lsp: use exec.CommandContext when running vulncheck%0A  > 3519aa2 internal/lsp/cmd: remove unused Env from pkgLoadConfig%0A  > 6c27717 internal/lsp/mod/code_lens: add "run govulncheck" codelens%0A  > 763f65c gopls/internal/regtest/misc: simplify shared edit tests%0A  > fc3b24a go/internal/gcimporter: rewrite interface receiver parameters%0A  > b5fd088 internal/lsp/command: replace VulncheckArgs Dir with URI%0A  > 99fd76f internal/lsp/cache: delete KnownMetadata.PkgFilesChanged%0A  > 01c9ff0 internal/lsp/cache: invalid packages should not be workspace packages%0A  > bd68922 internal/lsp: new options to disable certain kinds of semantic tokens%0A  > bceee4b internal/lsp/command: let RunVulncheckExp call gopls vulncheck%0A  > 3e0a503 internal/lsp: use directoryFilters in import scanning%0A  > 87f47bb gopls/internal/regtest/bench: refactor and improve benchmarks%0A  > 8b9a1fb go/callgraph/vta: do not assume that recovers cannot be deferred%0A  > 371fc67 go/tools: add check for time formats with 2006-02-01%0A  > d08f5dc gopls/internal/regtest: unskip all of TestModFileModification%0A  > ddb90ec internal/lsp/cache: fix data races to view.options%0A  > 0d04f65 internal/lsp: re-send diagnostics on file events%0A  > d025cce internal/lsp/source: don't crash requesting gc_details for an empty file%0A  > 10cb435 internal/lsp/regtest: improvements for shared execution modes%0A  > 4d0b383 internal/lsp/regtest: minor cleanup for magic regtest envvar%0A  > 310ea71 gopls/internal/regtest: add a test that ignoring a file resolves errors%0A  > 21861e6 gopls/internal/regtest/bench: put feature benchmarks in their own file%0A  > c7f1191 go/internal/gcimporter: set underlying types in proper order; flatten imports%0A  > bd3f524 internal/lsp: rename all the package names in the renamed package%0A  > 9f65685 internal/lsp/source: enable the new diff with allExperiments%0A  > 9580c84 internal/lsp: Check if user's editor support rename operation%0A  > f560bc8 internal/lsp/cache: don't set context cancellation as a critical err%0A  > 8ea5687 internal/lsp/regtest: remove arbitrary timeout for closing the editor%0A  > d01bb2f internal/lsp/source: document the handling of GOPRIVATE for linkTarget%0A  > 98bfcd1 internal/memoize: fix race in Store.Promise%0A  > e02e98a internal/lsp/cache: allow network whenever reloading the workspace%0A  > b52794a internal/lsp/cache: simplify snapshot.Clone reinitialization logic%0A  > f1bb5ca internal/lsp/cache: report a critical error when go.work is invalid%0Abumping knative.dev/pkg dfad48e...94b81fc:%0A  > 94b81fc Update community files (# 2752)%0A  > 5671699 drop the dynamic type (# 2750)%0A  > 9bda38b Fix some webhook testing tech debt (# 2751)%0A  > ec20442 Update community files (# 2747)%0A  > 05bfcf6 bump k8s dependencies and update min version to v1.25 (# 2745)%0A  > 52ff2ac drop dynamic client wrappers (# 2744)%0A  > a170a07 Eventing TLS: validate that Destination.CACerts is a PEM encoded cert (# 2743)%0A  > dfb4bf0 Drop dynamic wrapper injection code generation (# 2742)%0A  > db8a353 Add SinkCACerts to SourceStatus (# 2733)%0A  > 9049667 Update community files (# 2735)%0A  > aacec7f Update community files (# 2734)%0A  > 300df43 Eventing TLS: Added AddressableFromDestination method on the resolver (# 2717)%0Abumping golang.org/x/sys 90c8f94...c7a1bf9:%0A  > c7a1bf9 unix: define PerfBitWriteBackward%0A  > 1470852 unix: add SetsockoptTCPMD5Sig on linux%0A  > a6bfb89 unix: use unsafe.Slice in anyToSockaddr%0A  > c10701f windows: use unsafe.Slice in (*RawSockaddrAny).Sockaddr on windows%0A  > 6f25076 unix: define extended TCPInfo on Linux%0A  > 10499f4 unix: add ioctlPtr with unsafe.Pointer arg on other unices (cont)%0A  > 92c4c39 unix: add Dup3 on FreeBSD%0A  > 748af6e unix: pass PROT_MPROTECT(PROT_READ|PROT_WRITE) to initial Mmap on netbsd%0A  > 972870e unix/linux: update to Linux kernel 6.2, glibc 2.37 and Go 1.20.1%0A  > cc0b67d unix: use C.ioctl in generated ioctlPtr%0A  > a3b23cc unix: use SYS_PTRACE in generated ptracePtr%0A  > 71a906e unix/linux: add TUN flags and virtio_net_hdr constants%0A  > 2977c77 unix: add ptracePtr that accepts pointer arg as unsafe.Pointer%0A  > 6877dcc execabs: don't override Go 1.19 error with our error%0A  > b13f40e unix: add ioctlPtr with unsafe.Pointer arg on other unices%0A  > 3b9b58b unix: Faccess: check CAP_DAC_OVERRIDE on Linux%0A  > 2da1413 cpu: get hwcap/auxv from the Go 1.21+ runtime%0A  > 4fee21c windows: Add WSALookupService syscall wrappers%0A  > c79a742 unix: fix a use-after-free bug in PtraceIO on freebsd%0Abumping github.com/fsnotify/fsnotify 0f4b979...5f8c606:%0A  > 5f8c606 Update ChangeLog%0A  > 8878587 Tweak the docs a bit%0A  > 89b4cf1 Add test for re-adding a renamed file (# 508)%0A  > 85acde2 Update x/sys%0A  > 69c24b0 Update x/sys%0A  > fb07f82 Add test to see what happens if you watch a symlink (# 498)%0A  > 666da9c Clarify doc comment on WatchList() (# 499)%0A  > 123e4e3 Add note about README version%0A  > 61a05ce Update documentation and examples (# 496)%0A  > e180a87 Move some inotify-tests to run on all backends; test that state is cleaned up after Remove (# 494)%0A  > fdf41a3 Move some files around%0A  > 844d71f Port minor test changes from fen-v2 branch; make LICENSE text not ugly%0A  > 5b87f50 windows: simplify a bit (# 493)%0A  > 2bfaa00 all: add Watcher.{sendEvent,sendError} (# 492)%0A  > 8ab3b84 kqueue: don't set up watchers on unreadable files (# 479)%0A  > a4bcdf8 Update changelog%0A  > 4b43fad kqueue: remove timeout from unix.Kevent() (# 480)%0A  > a24f78c windows: test symlinks (# 491)%0A  > f45391f windows: run TestWatchRename/rename_overwriting_existing_file (# 490)%0A  > ee33a65 Use "os.Rename()" in tests instead of "mv"%0A  > 9dd0568 cmd/fsnotify: fix time.Format() string%0A  > 5dcbfba windows: replace syscall with golang.org/x/sys/windows%0A  > 1f8edaf windows: replace "e" with "err" for error variables%0A  > 99715ba windows: increase buffer size from 4K to 64K (# 485)%0A  > a5c5815 ci: update to use Go 1.19, kick off fewer builds, update x/sys (# 484)%0A  > f2d35c3 Remove CLA section in contributing%0A  > 4604469 Need Linux 5.9 for a useful fanotify we can use%0A  > a566bb1 Update CONTRIBUTING.md%0A  > 01dfc6f Remove PULL_REQUEST_TEMPLATE%0A  > a58e868 Run tests in illumos (# 481)%0A  > 666c6a0 Update ChangeLog%0A  > 928895c [bugfix] close handle when remWatch open in getIno (# 288)%0A  > f174f95 windows: update watch paths when renaming directories with sub-watches (# 370)%0A  > 87dc1fa Rewrite tests (# 478)%0A  > 57e6a49 Add {Event,Op}.Has() (# 477)%0A  > 39823aa Document that /proc and /sys won't work%0A  > 60fbf57 Clarify FAQ on goroutines%0A  > ca0e2f4 macos: retry if open() returns EINTR (# 475)%0A  > ff39bb4 Fix lint (# 476)%0A  > 421f529 debian 6 test: deal with multiple packages (# 474)%0A  > a3256ef Remove AUTHORS file%0A  > 0e78fa6 Update README: split out FAQ to "Platform-specific notes"%0A  > 1a7b6ef inotify: don't ignore events for files that don't exist (# 470)%0A  > f0aceb2 Tweak comment regarding relative paths (# 466)%0A  > d9c9fa5 Add cmd/fsnotify (# 463)%0A  > cc15908 kqueue: better error if watching a file fails (# 471)%0A  > c4e64e4 Replace Use of Kthread-blocking Epoll with Poller Read, Remove Per-Event LStats on Linux # 433 (# 434)%0A  > 4b8b298 Test some more things in CI (# 469)%0A  > 548b8fb Add missing changelog for 1.4.{8,9} (# 468)%0A  > 7fe2936 inotify: fix race in Close() (# 465)%0A  > 35b6378 Clarify README on network drives (# 467)%0A  > e56409e Update link to CONTRIBUTING in the README (# 464)%0A  > 4678dfd Update documentation for linux systems (max_user_watches) (# 287)%0A  > 808f582 bump up GitHub Actions (# 461)%0A  > 4193dfd Do not suppress Chmod on non-existent file (# 260)%0A  > 6ae56b7 kqueue: Make watcher.Close() O(n) instead of O(n^2) (# 233)%0A  > adf5320 strings.Builder instead of bytes.Buffer (# 285)%0A  > 217e78e Explicit mutext (un)locking (# 462)%0A  > 1a4f949 Use common error when removing an unwatched file (# 460)%0A  > 5acfdc1 windows: protect access to isClosed with mutex (# 454)%0A  > c56cafd Test Go 1.18%0A  > 37badf6 This project is archived (# 459)%0Abumping knative.dev/hack f591fea...a861c8e:%0A  > a861c8e Update community files (# 294)%0A  > 5b7907f Update actions (# 289)%0A  > c133d5d Install Istio for tests (# 291)%0A  > 5812c57 Update community files (# 292)%0A  > 7d81248 Update community files (# 286)%0A  > 6e4569c Update community files (# 285)%0Abumping github.com/prometheus/client_golang 64435fc...254e546:%0A  > 254e546 Merge pull request # 1162 from kakkoyun/cut-1.14.0%0A  > 07d3a81 Merge pull request # 1161 from prometheus/release-1.13%0A  > c8a3d32 Cut v1.14.0%0A  > 870469e Test and support 1.19 (# 1160)%0A  > 53e51c4 Merge pull request # 1157 from prometheus/cut-1.13.1%0A  > b785d0c Fix go_collector_latest_test Fail on go1.19 (# 1136)%0A  > 79ca0eb Added tip from Björn + Grammarly.%0A  > 4d54769 Fix float64 comparison test failure on archs using FMA (# 1133)%0A  > 078f11f Cut 1.13.1 release (+ documenting release process).%0A  > 5f202ee Merge pull request # 1150 from prometheus/sparsehistogram%0A  > ddd7f0e Fix race condition with Exemplar in Counter (# 1146)%0A  > 0859bb8 Merge pull request # 1152 from jessicalins/update-to-custom-reg%0A  > fffb76c Merge branch 'main' into sparsehistogram%0A  > 1f93f64 Fix `CumulativeCount` value of `+Inf` bucket created from exemplar (# 1148)%0A  > 10b0550 Fix race condition with Exemplar in Counter (# 1146)%0A  > a340ca4 Run make format%0A  > e92a8c7 Avoid the term 'sparse' where possible%0A  > 8cc2b6c Fix double-counting bug in promhttp.InstrumentRoundTripperCounter (# 1118)%0A  > dcea97e Fix `CumulativeCount` value of `+Inf` bucket created from exemplar (# 1148)%0A  > 6056615 Update random example to use custom registry%0A  > d31f13b Add SparseBucketsZeroThresholdZero and groom doc comments%0A  > 9801a4e Examples: Replace deprecated WithGoCollections with WithGoCollectorRuntimeMetrics (# 1130)%0A  > 0b7f488 Update simple example to use custom registry%0A  > 58a8ca4 examples: Adjust doc comment for native histograms%0A  > 7c46c15 Clarify documentation around what constructors do (# 1125)%0A  > 9b5c5b8 Update basic example to use custom registry%0A  > 4e71e6f Update prometheus/client_model dependency%0A  > 83d56b1 Extend prometheus.Registry to implement Collector (# 1103)%0A  > 111fae1 Merge branch 'main' into sparsehistogram%0A  > 4c41dfb Clarify exemplar(Add|Observe) by renaming to (add|observe)WithExemplar (# 1122)%0A  > 25bc188 Merge pull request # 1144 from prometheus/beorn7/histogram2%0A  > f73e3cc Fix double-counting bug in promhttp.InstrumentRoundTripperCounter (# 1118)%0A  > 95cf173 Merge branch 'main' into sparsehistogram%0A  > 6942f9e sparse buckets: Fix handling of +Inf/-Inf/NaN observations%0A  > c7aa2a5 Merge pull request # 1113 from prometheus/release-1.13%0A  > ec86ef1 Merge pull request # 1092 from prometheus/beorn7/histogram%0A  > 1e61b8e Update common Prometheus files (# 1111)%0A  > 6141a07 Merge branch 'main' into sparsehistogram%0A  > 8cbcd40 histograms: Move to new exposition protobuf format%0A  > 5a321c7 Merge branch 'foo-commit' into sparsehistogram%0A  > e93e384 Merge branch 'beorn7/release' into sparsehistogram%0A  > e203144 Merge branch 'release-1.12' of github.com:prometheus/client_golang into release-1.12%0A  > 525d042 Merge branch 'main' into sparsehistogram%0A  > a516626 Merge branch 'release-1.12' into beorn7/release%0A  > a27b6d7 Fix conflicts%0A  > 6ba7871 Merge branch 'main' into sparsehistogram%0A  > eb59a7b Histogram: Fix bug with negative schemas (# 1054)%0A  > b237230 Merge branch 'main' into sparsehistogram%0A  > 294cca4 Merge branch 'main' into sparsehistogram%0A  > 70253f4 Fix typo in doc comment%0A  > 5b19c55 Merge branch 'master' into sparsehistogram%0A  > dfbcc28 Merge pull request # 901 from prometheus/beorn7/histogram%0A  > 84fcaff Merge branch 'master' into sparsehistogram%0A  > 263be8d Refactoring of sparse histograms%0A  > 9ef5f90 Allow a zero threshold of zero%0A  > 2409960 Implement strategy to limit the sparse bucket count%0A  > aa6f67a Add TODO about bucket search optimization%0A  > 43f31c2 Merge pull request # 886 from prometheus/beorn7/histogram%0A  > 5aa8534 Merge branch 'master' into sparsehistogram%0A  > 5142344 Pin client_model…

---
## [SammyEnigma/node-exporter-textfile-collector-scripts](https://github.com/SammyEnigma/node-exporter-textfile-collector-scripts)@[0ca17e6e51...](https://github.com/SammyEnigma/node-exporter-textfile-collector-scripts/commit/0ca17e6e510404139188d3644001c5b59e494895)
#### Friday 2023-06-09 02:08:26 by Antoine Beaupré

lvm: add support for "all" checks

It seems rather inconvenient to have to specify all those switches by
hand. Right now, I need to specify -gpst to get all the stats and, if
some new metric get added (e.g. #159 hopefully), I need to remember to
update my callers to match. This is annoying.

Let's make a -a that's going to do it all for us. Hell, i'd make it
the default, personally, if I wasn't worried about breaking people's
stuff...

This obviously conflicts with other PRs that might add another flag
like this, like #159. Please prioritize the latter.

Signed-off-by: Antoine Beaupré <anarcat@debian.org>

---
## [Pumpkinoe/tgstation](https://github.com/Pumpkinoe/tgstation)@[912e843f53...](https://github.com/Pumpkinoe/tgstation/commit/912e843f53cf33b15148ec5a5ec66ce107314467)
#### Friday 2023-06-09 02:13:38 by san7890

Allows Export of your Preferences JSON File (#75014)

## About The Pull Request

Hey there,

This was spoken about in #70492 (specifically
https://github.com/tgstation/tgstation/pull/70492#issuecomment-1278069607),
and I have been waiting for this to be implemented for some time. It
never got implemented, so I decided to code it myself.

Basically, **if the server host doesn't disable it**, you are free to
export your JSONs as a player, right from the stat-panel. It's a pretty
JSON on 515 versions, too!

It's right here:


![image](https://user-images.githubusercontent.com/34697715/235251447-1c977718-51fd-4025-8d89-c60bffc379ec.png)

Here's what the prettified JSON looks like on 515.


![image](https://user-images.githubusercontent.com/34697715/235321061-4a217e26-c082-4bba-b54a-2c780defda0a.png)

There's a cooldown (default to 10 seconds) between exporting your
preferences.

#### Why is this config?

It's because in the past, a server host could always just file-share the
.sav or .json or whatever to the player, but they would have to do the
explicit option of actually bothering to make the files accessible to
the player. In that same line of logic, the server operator will have to
explicitly make the files accessible. This is mostly because I'm not
sure how good `ftp()` is at being a player function and wanted to have
some sort of cap/control somehow in case an exploit vector is detected
or it's just plain spammed by bots, so we'll just leave it up to the
direct providers of this data to elect if they wish to provide the data
or not.
## Why It's Good For The Game

Players don't have to log into Server A to remember what hairstyle they
loved using when they want to swap to Server B! That's amazing actually.
I always forget what ponytail my character has, and it'll be nice to
have the hairstyle in a readily accessible place (after I prettify the
JSON for myself).

It's also more convenient for server hosts to make player data like this
accessible if they really want to, too.

If we ever add an _import_ feature in the future (which would have to be
done with a LOT of care), this will also be useful. I wouldn't advise it
though having taken a precursory look at how much goes into it while
trying to ascertain the scope of this PR.
## Changelog
:cl:
qol: The game now supports export of your preferences into a JSON file!
The verb (export-preferences) should now be available in the OOC tab of
your stat-panel if enabled by server operators.
server: Exporting player preferences is controlled by a configuration
option, 'FORBID_PREFERENCES_EXPORT'. If you do not wish to let clients
access the ftp() function to their own preferences file (probably for
bandwidth reasons?) you should uncomment this or add it to your config
somehow.
config: Server operators are also able to set the cooldown between
requests to download the JSON Preferences file via the
'SECONDS_COOLDOWN_FOR_PREFERENCES_EXPORT' config option.
/:cl:

---
## [Pumpkinoe/tgstation](https://github.com/Pumpkinoe/tgstation)@[f7a49c4068...](https://github.com/Pumpkinoe/tgstation/commit/f7a49c4068f1277e6857baf0892d355f1c055974)
#### Friday 2023-06-09 02:13:38 by Ryll Ryll

Gunpoints now take half a second to activate, make gasp sounds, and briefly immobilize the shooter and target, other small balance changes (#74036)

## About The Pull Request
This PR messes around with gunpoints a bit, with the purpose of making
them more viable in certain scenarios without making them obnoxious. The
biggest change is that gunpoints now require a 0.5 second do_after()
where neither the shooter nor the target moves, and immobilizes both of
them for 0.75 seconds if point blank, or half that if you're 2 tiles
away. Originally you were supposed to only be able to initiate a
gunpoint from point-blank, but #56601 seems to have removed that
requirement, so we'll run with it and just leave it as advantageous to
gunpoint closer up. The do_after() reinforces that it should be used as
an ambush tactic, and so you can't use it on someone who's actively
fleeing or fighting you.

Getting held up will now make you emit a shocked gasp sound, a la Metal
Gear Solid, which combined with the short immobilize will hopefully make
it more noticeable that someone's pointing a gun at you.

Holdups will now immediately give a 25% bonus to damage and wounds,
instead of having to wait 2.5 seconds to hit the double damage stage.

Finally, right clicking someone that you're holding up will no longer
shoot them. That just feels like good consistency.

## Why It's Good For The Game
Hopefully makes gunpoints a little more viable for when you want to
stick someone who's not expecting it up without them immediately jetting
off. In the future I'd like to ape Baycode and let the gunman have an
action that toggles whether the victim is allowed to move, so you can
order them to move to a second location without instantly shooting them,
but that'll come later.
## Changelog
:cl: Ryll/Shaps
balance: Holding someone at gunpoint now requires both the shooter and
the victim to hold still for half a second before activating, so you
can't hold-up people fleeing or fighting you. After that, it will
briefly immobilize the both of you, 0.75 seconds if adjacent, or half
that if you're two tiles away. Nuke ops are immune to the
immobilization, since they're ready to die anyways.
balance: Holding someone up will immediately apply a 1.25x damage and
wound multiplier, rather than waiting 2.5 seconds to hit 2x.
soundadd: Being held up will now make the victim play a sharp gasp
sound, a la Metal Gear Solid.
qol: Trying to hold someone up that you're already holding up will no
longer shoot them.
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [i3roly/glibc_ddwrt](https://github.com/i3roly/glibc_ddwrt)@[6f2e6aea61...](https://github.com/i3roly/glibc_ddwrt/commit/6f2e6aea61f58240ca2fabe99bf08f21f6f38650)
#### Friday 2023-06-09 02:54:40 by gagan sidhu

[v52926/4.14.316] update a bunch of shit. google daryl's new nose

- you act like the last two update messages weren't the best, but now
  i'm forced to push an update because assfuck is going crazy.
        -he decided to just go HAM on updates.
        -it's like he was doing spin kicks whilst holding a dance ribbon
        and entering "svn commit".
                -jeez.

- update dhcp forwarder
- update util-linux (2.39)
- update less (6.33)
- update kernel (4.14.316)
- update freeradius
- update asterisk
- update/add nodogsplash

since cisco won't rename snort to daryl, i think it's funny af if you
google "daryl's new nose" without quotes you'll see what happens when
your product consumption exceeds your net contribution. i dream to be as
big of a loser as new nose daryl.

***** BULLETIN BOARD *****

-CAN SOMEBODY TELL ME HOW THE 882 RAMDISK GREW BY 100K COMPRESSED? I'M
ADHDING OUT AND MISSING SOMETHING. THERE HAS TO BE A DUPE OR SOMETHING!
PLEASE LET ME KNOW!

---
## [VashVandez/cmss13](https://github.com/VashVandez/cmss13)@[2baaba2746...](https://github.com/VashVandez/cmss13/commit/2baaba27468b20016d2095edfbdba26658935ddc)
#### Friday 2023-06-09 03:11:33 by Hopekz

Adds medic clothing racks to WO (#3313)

God damn this is so frustrating every time I play WO as a medic


![dreamseeker_ZXt55sth9R](https://github.com/cmss13-devs/cmss13/assets/24533979/252773e1-fec0-4bec-a1a5-0ccb63547781)


![dreamseeker_UiolotzaIV](https://github.com/cmss13-devs/cmss13/assets/24533979/a241ee86-f2ea-490f-91c7-7b1a90e9734f)


:cl: Hopek
add: Medics finally get medic clothing racks on WO
/:cl:

---
## [GunJumpers/GunJumpers](https://github.com/GunJumpers/GunJumpers)@[c8cce03922...](https://github.com/GunJumpers/GunJumpers/commit/c8cce03922777bb6e6540a22828aeb4d742865fe)
#### Friday 2023-06-09 05:04:43 by silmist

fuck my stupid baka life

pace drive
auto repair
cursor

---
## [MaysLastPlaysThings/FNF-Vs-Human-Imposter](https://github.com/MaysLastPlaysThings/FNF-Vs-Human-Imposter)@[50e5083b73...](https://github.com/MaysLastPlaysThings/FNF-Vs-Human-Imposter/commit/50e5083b739f02ab490dce57baa3a813030133b6)
#### Friday 2023-06-09 05:17:58 by MasterX

We're the Mario Brothers, and plumbing's our game We're not like the others who get all the fame If your sink is in trouble, you can call us on the double We're faster than the others, you'll be hooked on the brothers, uh! H-hooked on the brothers

---
## [ODRI-the-human/Vampire-Pooers](https://github.com/ODRI-the-human/Vampire-Pooers)@[2540979fe0...](https://github.com/ODRI-the-human/Vampire-Pooers/commit/2540979fe0e4ff6e8f3dbf816272474a9759ee7e)
#### Friday 2023-06-09 05:56:52 by ODRI-the-human

The "feces addict" update

Main event: melee is implemented again, but actually general now. All items work with melee, with some items having unique melee effects where necessary (mainly homing, split shots, etc.). You can also charge up weapons, like the bat. There's a charge bar visual that comes up that is general, but probably should introduce a variable that can be adjusted to change the charge time of weapons.

Also:

Fixed orb 2 targetting player (nice once)
Fixed gunners just not fucking shooting (lmao)
Fixed some sawshot shit
Fixed curses that take away your items on hit not re-applying items to the player (before they'd just get removed lol)

And a bunch of other shit. Melee is fun yipee

---
## [Kapu1178/daedalusdock](https://github.com/Kapu1178/daedalusdock)@[452d6cbdc7...](https://github.com/Kapu1178/daedalusdock/commit/452d6cbdc7a8c4d3153dccc19ba1426f22d98531)
#### Friday 2023-06-09 06:18:21 by Gallyus

I hate asset code (#341)

315 fucking icon states
goddamnit it lemon boy what the fuck were you thinking

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[59dd02fe7c...](https://github.com/tgstation/tgstation/commit/59dd02fe7cd54b4153b294ccb965249c587f189d)
#### Friday 2023-06-09 06:25:12 by san7890

Welding Fuel Tanks now log_bomber when hit by projectile (#75885)

## About The Pull Request

This was intended behavior, but I think a lot of bullshit over the years
sorta corrupted this proc's intention. Anyways, we just override the
whole ass proc for this one check, give a good return value (or at least
the same one that we were always giving) if our criteria is met, rather
than deal with the problems that parent was feeding us.


![image](https://github.com/tgstation/tgstation/assets/34697715/e2b39140-d365-43aa-8834-2740f9fa5036)

The specific issue here was that the parent of `bullet_act()` was
invoking `take_damage()` which prematurely invoked `boom()` which
invokes `qdel()`, meaning that the `QDELETED()` check would _always_
early return without fail every time.

Let's just do our own thing here.
## Why It's Good For The Game


![image](https://github.com/tgstation/tgstation/assets/34697715/ca8fdeba-9f5d-4bed-afba-88824d389cfb)

Intended behavior actually works.
## Changelog
:cl:
admin: Shooting a welding fuel tank (big or small) with a projectile
will now accurately post to list_bombers with the name of the person who
shot the projectile from the gun. If you don't know how to list-bombers,
it will also be present in game.log for your viewing pleasure.
/:cl:

---
## [k7shubham/evals](https://github.com/k7shubham/evals)@[44d941b773...](https://github.com/k7shubham/evals/commit/44d941b7734983950d09d9f0012ec58ec45e171c)
#### Friday 2023-06-09 08:30:53 by HorizonAuto

Context-free-grammars (#1097)

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

context-free-grammar

### Eval description

This tests the ability for GPT-4 to evaluate whether or not a string can
be produced by a given context-free grammar.

### What makes this a useful eval?

This is an interesting computational task. Context-free languages are
important in linguistics, and it will be interesting to see
how a language model fares in handling this task.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [✅] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [✅] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [✅] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [✅] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)
I've handcrafted a lot of these examples. Some of them are there to
'trick' the model––I think it will be a useful test to see how well the
language model can do at those.

## Eval structure 🏗️

Your eval should

- [✅] Check that your data is in `evals/registry/data/{name}`
- [✅] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [✅] Ensure you have the right to use the data you submit via this eval

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

- [✅] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [✅] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [✅] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [✅] I have filled out all required fields of this form
- [✅] I have used **Git LFS** for the Eval JSON data
- [✅] (Ignore if not submitting code) I have run `pip install
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
{"input": [{"role": "system","content": "You will be provided with a
context-free grammar, and a string. Respond whether or not that string
can be produced by the given grammar. Respond only with the word true or
false; you do not need to show your work. The empty string is
represented with ϵ, and productions are separated with the symbol ;. The
alphabet is always {0, 1}."}, {"role": "user", "content": "Given the
grammar 'S -> 01 | SS | 0S1 | ϵ', is the string '01010101' in the
language?"}], "ideal": "true"}
{"input": [{"role": "system","content": "You will be provided with a
context-free grammar, and a string. Respond whether or not that string
can be produced by the given grammar. Respond only with the word true or
false; you do not need to show your work. The empty string is
represented with ϵ, and productions are separated with the symbol ;. The
alphabet is always {0, 1}."}, {"role": "user", "content": "Given the
grammar 'S -> 01 | SS | 0S1 | ϵ', is the string '00011101' in the
language?"}], "ideal": "true"}
{"input": [{"role": "system","content": "You will be provided with a
context-free grammar, and a string. Respond whether or not that string
can be produced by the given grammar. Respond only with the word true or
false; you do not need to show your work. The empty string is
represented with ϵ, and productions are separated with the symbol ;. The
alphabet is always {0, 1}."}, {"role": "user", "content": "Given the
grammar 'S -> 01 | SS | 0S1 | ϵ', is the string '00110101' in the
language?"}], "ideal": "true"}
{"input": [{"role": "system","content": "You will be provided with a
context-free grammar, and a string. Respond whether or not that string
can be produced by the given grammar. Respond only with the word true or
false; you do not need to show your work. The empty string is
represented with ϵ, and productions are separated with the symbol ;. The
alphabet is always {0, 1}."}, {"role": "user", "content": "Given the
grammar 'S -> 01 | SS | 0S1 | ϵ', is the string '01001101' in the
language?"}], "ideal": "true"}
{"input": [{"role": "system","content": "You will be provided with a
context-free grammar, and a string. Respond whether or not that string
can be produced by the given grammar. Respond only with the word true or
false; you do not need to show your work. The empty string is
represented with ϵ, and productions are separated with the symbol ;. The
alphabet is always {0, 1}."}, {"role": "user", "content": "Given the
grammar 'S -> 01 | SS | 0S1 | ϵ', is the string '01010011' in the
language?"}], "ideal": "true"}
  ```
</details>

---------

Co-authored-by: Arjun Taneja <arjun.taneja02@gmail.com>

---
## [k7shubham/evals](https://github.com/k7shubham/evals)@[04e1312631...](https://github.com/k7shubham/evals/commit/04e131263125d46812f19ce4cc58d55207beee3b)
#### Friday 2023-06-09 08:30:53 by Nazar

Russian verse (#979)

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
russian-verse

### Eval description

The most popular Russian poems that nearly every Russian speaker can
recall

### What makes this a useful eval?

Understanding a basic Russian poem or any foreign literature is
significant for a Language Learning Model (LLM) like GPT-4 because it
enhances multilingual ability, provides cultural context, and improves
understanding of language structure. It makes the model globally useful,
and culturally sensitive.

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
{"input": [{"role": "system", "content": "Continue verse with no
punctuation marks:\nМороз и солнце день чудесный\nЕще ты дремлешь друг
прелестный \nПора красавица проснись\nОткрой сомкнуты негой
взоры\nНавстречу северной Авроры"}], "ideal": "Звездою севера явись"}
{"input": [{"role": "system", "content": "Continue verse with no
punctuation marks:\nУ лукоморья дуб зелёный\nЗлатая цепь на дубе том\nИ
днём и ночью кот учёный\nВсё ходит по цепи кругом\nИдёт направо песнь
заводит"}], "ideal": "Налево сказку говорит"}
{"input": [{"role": "system", "content": "Continue verse with no
punctuation marks:\nЯ к вам пишу чего же боле\nЧто я могу еще
сказать\nТеперь я знаю в вашей воле\nМеня презреньем наказать\nНо вы к
моей несчастной доле"}], "ideal": "Хоть каплю жалости храня"}
{"input": [{"role": "system", "content": "Continue verse with no
punctuation marks:\nЯ помню чудное мгновенье\nПередо мной явилась
ты\nКак мимолетное виденье\nКак гений чистой красоты\nВ томленьях грусти
безнадежной"}], "ideal": "В тревогах шумной суеты"}
{"input": [{"role": "system", "content": "Continue verse with no
punctuation marks:\nЛюбви надежды тихой славы\nНедолго нежил нас
обман\nИсчезли юные забавы\nКак сон как утренний туман\nНо в нас горит
еще желанье"}], "ideal": "Под гнетом власти роковой"}
  ```
</details>

---
## [Bcadren/crawl](https://github.com/Bcadren/crawl)@[a6b91a39ae...](https://github.com/Bcadren/crawl/commit/a6b91a39ae863ad8644d5614cb9f6180118b548b)
#### Friday 2023-06-09 10:17:26 by Nicholas Feinberg

Remove skill training restrictions (hellmonk)

After the old XP pool system was removed and the current skill training
system was added, one odd edge case was that you had to have an item, spell,
or god ability somehow relevant to a skill to be able to train it. This was
not particularly consistent. For example, training got special-cased to be
always allowed to avoid annoyance when you'd thrown everything you had, and
pain brand, though depending on necromancy, did not allow you to train it.

In general, it's better to have less complexity and fewer special cases, so
by default it seems good to remove these rather complex restrictions. The
argument against has been that training these skills is rarely useful (true,
but so are many things players do!), and that a massive skill screen would
intimidate new players. Thankfully, to avoid the latter case, we can retain
much of the old code to hide many skills by default, while still allowing
experienced players to use them, in the same way that they can use manual
training instead of automatic. In fact, since we no longer need to special
case Throwing, new players will often see a smaller skill screen than before!

---
## [PlagueVonKarma/kep-hack](https://github.com/PlagueVonKarma/kep-hack)@[749abc67b7...](https://github.com/PlagueVonKarma/kep-hack/commit/749abc67b76624ac32c0db1294652f56fa4f9465)
#### Friday 2023-06-09 10:17:36 by Llinos Evans

Gym Leader Rematches!

This commit adds a large fundamental change to KEP, that being Gym Rematches.

This is achieved alongside a rework to the script that makes those post-game-gating NPCs shift around. If you add a new one, just add its constant to the lists you'll see in the Hall of Fame script.

It also fixes a few bugs:
- Fixed a bug where Cinnabar Gym loaded a fleet of Blaines. This occurred due to the way he is coded at base, and a misunderstanding I had when implementing his scaling. This is now fixed by standardising his gym script instead, while letting the gym trainers still use the old one.
- Fixed a bug where the Up-Grade NPC would not appear after beating Silph Co. 11F. However, Giovanni currently seems to have trouble with his text. This floor needs some re-coding anyway, given we need to add Jessie and James to it.

And some misc. changes:
- Changed the first Moon Stone in Mt. Moon to a Poison Stone for the Nidoking speedrunners
- Debug Mode now has a line of code to set up the post-game easily
- Changed Surge's initial battle text to Yellow's
- Added Sabrina's more accurate LGPE initial battle text, referring to the spoon she bent by accident

---
## [AFM-SPM/TopoStats](https://github.com/AFM-SPM/TopoStats)@[432dc9a081...](https://github.com/AFM-SPM/TopoStats/commit/432dc9a0817a3fe8b15c8a163f273fe2138347d9)
#### Friday 2023-06-09 10:47:55 by SylviaWhittle

Fix test_process_scan_above by fixing getDNAmolHeightStats

been digging away at the bug and I finally found it after too many hours.
It comes down to the lines in getDNAmolHeightStats…
Firstly, we have the swapping axes line that Neil pointed out is weird in a comment…
    def getDNAmolHeightStats(self):
        # Why are axes swapped here?
        self.image_data = np.swapaxes(self.image_data, 0, 1)
I really don’t think this is right, as when I print out some diagnostic logs…
image data shape : (119, 123)
binary map shape: (123, 119)
But that’s not all
The line
self.average_height = np.average(self.image_data[np.argwhere(self.binary_map == 1)])
does not do what one would expect (me included until a while back when I learned this in a similarly infuriating bug) I’m so annoyed that I didn’t spot it since I’ve already experienced it.
It appears really intuitive that stuffing an array of coordinates as the index for a numpy array, would return those points in the array…
my_2d_array = np.array(
    [
        [1, 2],
        [3, 4],
        [5, 6],
    ]
)

coordinates = np.array([[1]])
print(my_2d_array[coordinates])

print('---')

coordinates = np.array([1, 0])
print(my_2d_array[coordinates])

print('---')

coordinates = np.array([[1, 0], [2, 1]])
print(my_2d_array[coordinates])
But this does not do what is intended:
[[[3 4]]]
---
[[3 4]
 [1 2]]
---
[[[3 4]
  [1 2]]

 [[5 6]
  [3 4]]]
This is because it actually just prints each element of the 1st dimension of the array, eg in the first example, it prints the 1st element, which is the array [3, 4]. In the third example, it prints the 1st and 0th array, then the 2nd and 1st array.
As a result, I think that not only did the method often crash due to indexing errors, but also, it was grabbing completely the wrong pixels too? How long has it been like this? Luckily it doesn’t seem to have been used previously, so it might not have caused a problem historically??
I believe the solution is to firstly remove the swap axes line, and then to use the (I believe) intended way to index based on a list of coordinates:
    def getDNAmolHeightStats(self):

        coordinates = np.argwhere(self.binary_map == 1)
        flat_indices = np.ravel_multi_index(coordinates.T, self.image_data.shape)
        heights = self.image_data.flat[flat_indices]
        self.average_height = np.average(heights)
Which flattens everything and converts the list of coordinates into flattened coordinates using some modular arithmetic.
This took infuriatingly long to figure out, since my_array[coordinates] just seems so intuitive, so I spent most of my time searching elsewhere… :laughing:
This solution results in the regression test for test_process_scan_above  to ALMOST match!
The only differences are…
contour_lengths is now contour_length
A blank space character before every value under contour_lengths . This I think is caused by the aforementioned character removal
I have now made the change to test_processing.test_process_scan_above.out - removing the “s” and removing the whitespace before each value, and the test passes! (eventually - 36 seconds is a long time!)

---
## [aconty/OpenShadingLanguage](https://github.com/aconty/OpenShadingLanguage)@[71a9310f0b...](https://github.com/aconty/OpenShadingLanguage/commit/71a9310f0b8765f57b59e25e73f5f3bbdb8077e8)
#### Friday 2023-06-09 10:53:37 by Larry Gritz

feat(gpu)!: GPU/OptiX support of ReParameter (#1686)

BREAKING CHANGE: to RendererServices ABI (including for CPU) and to
the renderer-side setup when using OptiX.

This overhauls the implementation of how interactively-editable
parameters work, where they live in memory, and get it all working on
GPU/OptiX so that renderers can support interactive adjustment of
those params without recompiling shaders.

The basic gist is as follows:

* We continue work to finish making a clean separation between
  "interpolated" parameters and "interactive" (editable) parameters.

* Interpolated params are collected and put into a separate memory
  area -- a separate per-group allocation on both the CPU and GPU
  (where applicable). It needs to remember the offset into this arena
  where each of the interpolated parameters resides. These allocations
  and eventual release are taken care of by the OSL shading system,
  they live in the ShaderGroup. When the group is set up, this block
  of memory is initialized with the correct initial values of the
  params and are ready to go.

* The implementation of ReParameter writes to this special memory
  area also, that's how it works now (both CPU and GPU).

* How does the OSL library know how to allocate, free, and copy to the
  device memory? It doesn't! Instead, we add new RendererServices
  methods `device_alloc()`, `device_free()`, and
  `copy_to_device()`. It's up to the renderer to provide those, so
  that the OSL library doesn't itself need to know about the Cuda
  runtime. These are trivial, there's really only one implementation
  that makes sense, and you can copy it from the ones in testshade and
  testrender.

* Interactive parameters are NOT constant folded during runtime
  optimization.

* The shader entry points themselves now take an extra parameter in
  the main call -- this will be the pointer to the beginning of the
  shader group's interactive parameter arena.

* When JITing, references to interactive parameters know to retrieve
  them from their designated offset into the interactive parameter
  area.

* This means that the renderer-side OptiX/Cuda code is responsible for
  adding this extra pointer parameter to the call to the shader entry
  points. You can see how this is done in the testshade and testrender
  Cuda code.

* It's up to the renderer to figure out how to make the OptiX hit program
  aware of the interactive parameter pointer for that particular material,
  in order to pass it to the osl shader entry point. The way I did it in
  testshade and testrender is using a field in the struct that's given
  to each entry of the shader binding table and can be retrieved on the
  OptiX side via optixGetSbtDataPointer(). In testshade/testrender, a
  data pointer already existed which wasn't used. In a real renderer, you
  may need to add a field or come up with whatever other way you want
  to somehow get this pointer, which can be retrieved via

      shadingsys->getattribute(shadergroupptr, "device_interactive_params",
                               TypeDesc::PTR, &myptr);

  you can see how I do that in optixraytracer.cpp (testrender) and in
  optixgridrender.cpp (testshade).

A number of other things you will see that's worth calling out:

I added a device_ptr utility template that is just a wrapper around a
device side pointer that makes it hard to accidentally dereference it
on the host side.

Since I was changing RendererServices anyway, I also remove unused
register_global, fetch_global, global_map which were unused. They were
leftovers from the way we handled strings in OptiX 6.x.

Encapsulate cuda global symbol name mangling into
BackendLLVM::global_unique_symname(). I did this early on, turns out
it wasn't necessary, but I still like that encapsulation, so I'm
keeping it.

I bumped the 3rd set of digits in the version to reflect that the
changes in RendererServices break ABI. This is only in main, it
obviously cannot be backported to a release branch.

All tests pass for scalar and batch and optix.

I added a new simple reparam test, and renamed the old reparem to
reparam-array. Oddly, the reparam-array test doesn't work properly on
optix (it had never been tried before), but it also failed in optix at
main -- so it's not related to this patch! Putting that on my list of
other oddities to investigate later. It may just be a quirk of
testshade, I'm not really sure yet.

Added to BackendLLVM (and batched) a llvm_ptr_type(TypeSpec) method
that returns the LLVM type of a pointer to the specified type.

Note: This patch doesn't account for the face that a parameter marked
"interactive" could prevent a shader from correctly building for the GPU
because it used the kind of construct that is fine in shader source code but
only will work on GPU if it can be resolved to be a constant by the time
we get done with the runtime optimization (as pointed out by Stephen
Friedman. We'll come back to the problem later with a more robust and
automatic fix -- and if we are lucky, Stephen will have the opportunity to
upstream the approach he already has.

Signed-off-by: Larry Gritz <lg@larrygritz.com>

---
## [petre-symfony/api-platform-3-part-2-security-for-you-symfonycasts-june-2023](https://github.com/petre-symfony/api-platform-3-part-2-security-for-you-symfonycasts-june-2023)@[ab0a117bbe...](https://github.com/petre-symfony/api-platform-3-part-2-security-for-you-symfonycasts-june-2023/commit/ab0a117bbea8b9d4a228b76ad5c3829a32caf29c)
#### Friday 2023-06-09 10:58:52 by Petre Ro

8.1 Token Types & The ApiToken Entity

 Okay, so what if you need to allow programmatic access to your API?

 The Types of Access Tokens
 - When you talk to an API via code, you send an API token, commonly known as an access token:

 fetch('/api/kittens', {
    headers: {
        'Authorization': 'Bearer THE-ACCESS-TOKEN',
    }
 });
 Exactly how you get that token will vary. But there are two main cases.

 First, as a user on the site, like a dragon, you want to generate an API token so that you can personally use it in a script you're writing. This is like a GitHub personal access token. These are literally created via a web interface. We're going to show this.

 The second main use case is when a third party wants to make requests to your API on behalf of a user of your system. Like some new site called DragonTreasureOrganizer.com wants to be able to make an API request to our API on behalf of some of our users - like it will fetch the treasure's for a user and display them artfully on their site. In this situation, instead of our users generating tokens manually and then... like... entering them into that site, you'll offer OAuth. OAuth is basically a mechanism for normal users to securely give access tokens for their account to a third party. And so, your site, or somewhere in your infrastructure you'll have an OAuth server.

 That's beyond the scope of this tutorial. But the important thing is that after OAuth is done, the API client wll end up with, you guessed it, an API token! So no matter which journey you're in, if you're doing programmatic access, your API users will end up with an access token. And then your job will be to read and understand that. We'll do exactly that.

 JWT vs Database Storage?
 - So as I mentioned, we're going to show a system where we allow users to generate their own access tokens. So how do we do that? Again, there are two main ways. Death by choices!

 The first is to generate something called a JSON Web Token or JWT. The cool thing about JWTs are that no database storage is needed. They're special strings that actually contain info inside of them. For example, you could create a JWT string that includes the user id and some scopes.

 One downside of JWTs are that there's no easy way to "log out"... because there's no out-of-the-box way to invalidate JWTs. You give them an expiration when you create them... but then they're valid until then... no matter what, unless you add some extra complexity... which kinda defeats the purpose.

 JWT's are trendy, popular and fun! But... you may not need them. They're awesome when you have a single sign-on system because, if that JWT is used to authenticate with multiple systems or APIs, each API can validate the JWT all on their own: without needing to make an API request to a central authentication system.

 So you might end up using JWTs and there's a great bundle for them called LexikJWTAuthenticationBundle. JWT's are also the type of access token that OpenID gives you in the end.

 Instead of JWTs, the second main option is dead simple: generate a random token string and store it in the database. This also allows you to invalidate access tokens by... just deleting them! This is what we'll do.

 Generating the Entity
 - So let's get to work. To store API tokens, we need a new entity! Find your terminal and run:

  php ./bin/console make:entity
 And let's call it ApiToken. Say no to making this an API resource. In theory, you could allow users to authenticate via a login form or HTTP basic and then send a POST request to create API tokens if you want to... but we won't.

 Add an ownedBy property. This is going to be a ManyToOne to User and not nullable. And I'll say "yes" to the inverse. So the idea is that every User can have many API tokens. When an API token is used, we want to know which User it's related to. We'll use that during authentication. Calling the property apiTokens is fine and say no to orphan removal. Next property: expiresAt, make that a datetime_immutable and I'll say yes to nullable. Maybe we allow tokens to never expire by leaving this field blank. Next up is token, which will be a string. I'm going to set the length to 68 - we'll see why in a minute - not nullable. And finally, add a scopes property as a json type. This is going to be kind of cool: we'll store an array of "permissions" that this API token should have. Say, not nullable on that one as well. Hit enter to finish.

 All right, spin over to your editor. No surprises: that created an ApiToken entity... and there's nothing very interesting inside of it

 So let's go over and make the migration for it:

  symfony console make:migration
 Spin over and peek at that file to make sure it looks good. Yup! It creates the api_token table

 Run that with:

  symfony console doctrine:migrations:migrate
 And... awesome! Next: let's add a way to generate the random token string. Then, we'll talk about scopes and load up our fixtures with some API tokens.

---
## [petre-symfony/api-platform-3-part-2-security-for-you-symfonycasts-june-2023](https://github.com/petre-symfony/api-platform-3-part-2-security-for-you-symfonycasts-june-2023)@[dcbb786345...](https://github.com/petre-symfony/api-platform-3-part-2-security-for-you-symfonycasts-june-2023/commit/dcbb786345b7016893e9764828276f00b33d0af7)
#### Friday 2023-06-09 10:58:52 by Petre Ro

9.2 Setting up the Fixtures
 - Ok! This is set up! So let's add some API tokens to the database. At your terminal, run

  php ./bin/console make:factory
 so we can generate a Foundry factory for ApiToken. Go check out the new class: src/Factory/ApiTokenFactory.php. Down in getDefaults()

 This looks mostly fine, though we don't need to pass in the token. Oh, and I want to tweak the scopes

 Typically, when you create an access token - whether it's a personal access token or one created through OAuth - you're able to choose which permissions that token will have: it does not automatically have all the permissions that a normal user would. I want to add that into our system as well.

 Back over in ApiToken, at the top, after the first constant, I'll paste in a few more

 This defines three different scopes that a token can have. This isn't all the scopes we could imagine, but it's enough to make things realistic. So, when you create a token, you can choose whether that token should have permission to edit user data, or whether it can create treasures on behalf of the user or whether it can edit treasures on behalf of the user. I also added a public const SCOPES to describes them

 Back over in our ApiTokenFactory, let's, by default, give each ApiToken two of those three scopes

 Ok! ApiTokenFactory is ready. Last step: open AppFixtures so we can create some ApiToken fixtures. I want to make sure that, in our dummy data, each user has at least one or two API tokens. An easy way to do that, down here is to say ApiTokenFactory::createMany(). Since we have 10 users, let's create 30 tokens. Then pass that a callback function and, inside, return an override for the default data. We're going to override the ownedBy to be UserFactory::random()

 So this will create 30 tokens and assign them randomly to the 10, well really 11, users in the database. So on average, each user should have about three API tokens assigned to them. I'm doing this because, to keep life simple, we're not going to build a user interface where the user can actually click and create access tokens and select scopes. We're going to skip all that. Instead, since every user will already have some API tokens in the database, we can jump straight to learning how to read and validate those tokens.

 Reload the fixtures with:

  symfony console doctrine:fixtures:load

---
## [petre-symfony/api-platform-3-part-2-security-for-you-symfonycasts-june-2023](https://github.com/petre-symfony/api-platform-3-part-2-security-for-you-symfonycasts-june-2023)@[14cdf3bc51...](https://github.com/petre-symfony/api-platform-3-part-2-security-for-you-symfonycasts-june-2023/commit/14cdf3bc5148c5d1b5bea3c1f898df34c7f9d510)
#### Friday 2023-06-09 10:58:52 by Petre Ro

13.1 Deny Access with The "security" Option
 We've just talked a lot about authentication: that's the way we tell the API who we are. Now we turn to authorization, which is all about denying access to certain operations and other things based on who you are.

 Using access_control
 - There are multiple ways to control access to something. The simplest is in config/packages/security.yaml. Just like normal Symfony security, down here, we have an access_control section

 If you want to lock down a specific URL pattern by a specific role, use access_control. You could use this, for example, to require that the user has a role to use anything in your API by targeting URLs starting with /api.

 Hello "security" Option
 - In a traditional web app, I do use access_control for several things. But most of the time I put my authorization rules inside controllers. But... of course, with API Platform, we don't have controllers. All we have are API resource classes, like DragonTreasure. So instead of putting security rules in controllers, we'll attach them to our operations.

 For example, let's make the POST request to create a new DragonTreasure require the user to be authenticated. Do that by adding a very handy security option. Set that to a string and inside, say is_granted(), double quotes then ROLE_TREASURE_CREATE

 We could simply use ROLE_USER here if we just wanted to make sure that the user is logged in. But we have a cool system where, if you use an API token for authentication, that token will have specific scopes. One possible scope is called SCOPE_TREASURE_CREATE... which maps to ROLE_TREASURE_CREATE. So we look for that. Also, in security.yaml, via role_hierarchy, if you log in via the login form, you get ROLE_FULL_USER... and then you automatically also get ROLE_TREASURE_CREATE.

 In other words, by using ROLE_TREASURE_CREATE, access will be granted either because you logged in via the login form or you authenticated using an API token that has that scope.

 Let's try it. Make sure you're logged out. I'll refresh. Yup, you can see on the web debug toolbar that I'm not logged in... and Swagger does not currently have an API token.

 Let's test the POST endpoint. Try it out.. and... just Execute with the example data. And... yes! A 401 status code with type hydra:error!

 More about the "security" Attribute
 - The security option actually holds an expression using Symfony's expression language. And you can get pretty fancy with it. Though, we're going to try to keep things simple. And later, we'll learn how to offload complex rules to voters.

 Let's add a few more rules. Put and Patch are both edits. These are especially interesting because, to use these, not only do we need to be logged in, we probably need to be the owner of this DragonTreasure. We don't want other people to edit our goodies.

 We're going to worry about the ownership part later. But for now, let's at least add security with is_granted() then ROLE_TREASURE_EDIT

 Once again, I'm using the scope role. Copy that, and duplicate it down here for Patch

 Oh, and earlier, we removed the Delete operation. Let's add that back with security set to look for ROLE_ADMIN

 If we decided later to add a scope that allowed API tokens to delete treasures, we could add that and change this to ROLE_TRESURE_DELETE.

 Let's make sure this works! Use the GET collection endpoint. Try that out. This operation does not require authentication... so it works just fine. And we have a treasure with ID 1. Close this up, open the PUT operation, hit "Try it out", 1, "Execute" and... alright! We get a 401 here too!

---
## [JimAppreciator512/ifunny-bot](https://github.com/JimAppreciator512/ifunny-bot)@[23ae430e53...](https://github.com/JimAppreciator512/ifunny-bot/commit/23ae430e5312096050e86a17c3bbd7df8b36c39f)
#### Friday 2023-06-09 11:22:28 by JimAppreciator512

this shit took so fucking long bro I hate special characters in HTML selectors

---
## [jamilnielsen/Monkestation2.0](https://github.com/jamilnielsen/Monkestation2.0)@[79e07c00db...](https://github.com/jamilnielsen/Monkestation2.0/commit/79e07c00db8607513347f8e7e6f2a8520e563680)
#### Friday 2023-06-09 12:12:38 by Aeri

fucking wacky ass goddamn cargo order console locations fixed

---
## [akaFuran/emblemafarm](https://github.com/akaFuran/emblemafarm)@[6f25ccb8f4...](https://github.com/akaFuran/emblemafarm/commit/6f25ccb8f491fabe9f39389cce65fb435aab6b77)
#### Friday 2023-06-09 12:22:10 by Francisco Santos

Merge pull request #1 from leandroviegas/main

fuck you

---
## [streamlit/streamlit](https://github.com/streamlit/streamlit)@[c464422e1b...](https://github.com/streamlit/streamlit/commit/c464422e1bbea66b3184769ea22599356d710f9a)
#### Friday 2023-06-09 13:41:12 by Danny Wolf

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
## [Yelp/Tron](https://github.com/Yelp/Tron)@[fcf4811736...](https://github.com/Yelp/Tron/commit/fcf4811736faa892f4c4f0733316db4af143c6b2)
#### Friday 2023-06-09 13:47:50 by Luis Pérez

Print raw output in scribereader fallback command (#913)

The current shell pipeline prints out every line surrounded by quotes,
which is a bit annoying when sharing logs (or snippets of logs) with
other people since you either need to manually clean up the logs to
strip the quotes or live with the shame of sending someone ugly-looking
text :p

---
## [argilla-io/argilla](https://github.com/argilla-io/argilla)@[838ba2c9c9...](https://github.com/argilla-io/argilla/commit/838ba2c9c9570c07a7be7826b7d939ef8ba0e680)
#### Friday 2023-06-09 13:48:02 by Alvaro Bartolome

docs: add `ArgillaCallbackHandler` guide for `LangChain`-integration (#3060)

# Description

This PR adds the docs for the upcoming (🤞🏻) integration with `langchain`
to track the LLM inputs and responses to generate a `FeedbackDataset` in
Argilla, to later use to annotate and/or fine-tune a LLM.

Keep track of the `langchain`-integration progress at
https://github.com/argilla-io/langchain/tree/add-argilla-callback (PR
coming soon!)

**Type of change**

- [X] Documentation update

**How Has This Been Tested**

`pip install
git+https://github.com/argilla-io/langchain.git@add-argilla-callback`

```python
import argilla as rg

rg.init(
    api_url="...",
    api_key="...",
)

dataset = rg.FeedbackDataset(
    fields=[
        rg.TextField(name="prompt"),
        rg.TextField(name="response"),
    ],
    questions=[
        rg.RatingQuestion(
            name="response-rating",
            description="How would you rate the quality of the response?",
            values=[1, 2, 3, 4, 5],
            required=True,
        ),
        rg.TextQuestion(
            name="response-correction",
            description="If you think the response is not accurate, please, correct it.",
            required=False,
        ),
    ],
    guidelines="Please, read the questions carefully and try to answer it as accurately as possible.",
)

dataset.push_to_argilla("...", workspace="...")
```

Then instantiate the `ArgillaCallbackHandler`:

```python
from langchain.callbacks import ArgillaCallbackHandler

argilla_callback = ArgillaCallbackHandler(
    dataset_name="...",
    workspace_name="...",
    api_url="...",
    api_key="...",
)
```

* LangChain LLMs

```python
from langchain.llms import OpenAI

llm = OpenAI(temperature=0.9, callbacks=[argilla_callback], verbose=True, openai_api_key="...")
llm_result = llm.generate(["Tell me something that I may not know about Stephen Hawking."])
llm_result = llm.generate(["Tell me something funny about cows.", "Tell me something funny about dogs."])
```

* LangChain Chains

```python
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI

llm = OpenAI(temperature=0.9, callbacks=[argilla_callback], verbose=True, openai_api_key="...")

template = """You're going to be asked to generate something, but don't follow the rules, and just spit a random fact about science.
Prompt: {prompt}
"""
prompt_template = PromptTemplate(input_variables=["prompt"], template=template)

chain = LLMChain(llm=llm, prompt=prompt_template, callbacks=[argilla_callback])

chain.apply([{"prompt": "Generate a poem about love."}, {"prompt": "Generate a poem about hate."}])
```

* LangChain Agents

```python
from langchain.agents import initialize_agent, load_tools
from langchain.llms import OpenAI

llm = OpenAI(temperature=0.9, callbacks=[argilla_callback], verbose=True, openai_api_key="...")
tools = load_tools(["serpapi"], llm=llm, callbacks=[argilla_callback])
agent = initialize_agent(
    tools,
    llm,
    agent="zero-shot-react-description",
    callbacks=[argilla_callback],
    verbose=True,
)
agent.run(
    ["Who is Leo DiCaprio's girlfriend?", "What's the name of the movie where Leo DiCaprio is a thief?"]
)
agent.run(
    "What is the most populated country as of today?"
)
```

**Checklist**

- [X] I have merged the original branch into my forked branch
- [X] I added relevant documentation
- [X] follows the style guidelines of this project
- [X] I did a self-review of my code
- [X] I made corresponding changes to the documentation
- [X] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or that my
feature works
- [ ] I have added relevant notes to the CHANGELOG.md file (See
https://keepachangelog.com/)

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[fa66045e69...](https://github.com/treckstar/yolo-octo-hipster/commit/fa66045e69cd23fbb2f49e35613f9bf92e423b19)
#### Friday 2023-06-09 14:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [Droidcraft/evals](https://github.com/Droidcraft/evals)@[24f78a806e...](https://github.com/Droidcraft/evals/commit/24f78a806e60b452aaefc355f045c6336a81d076)
#### Friday 2023-06-09 15:32:21 by YuryRudnitski

Add eval for guessing the singer or band (#659)

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
guess-the-singer

### Eval description

This evaluation measures the model's ability to identify a singer or
band by analyzing the first 10 words of a song. To ensure the
evaluation's fairness and focus, we have excluded songs with multiple
singers/bands and included only those published before 2021. To test the
model's performance, we provide it with three potential choices and
evaluate its accuracy in selecting the correct one.

### What makes this a useful eval?

The inclusion of over 4000 popular songs' lyrics provides a large and
diverse dataset for the model to test on. This enables a more accurate
assessment of the model's performance and its ability to identify
singers/bands based on the first 10 words of their songs.

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

> This evaluation assesses not only the model's ability to recognize a
singer or band based on the first 10 words of a song but also its
capability to accurately copy the provided options without adding any
additional punctuation or text. By testing the model's ability to
replicate the options, we can gain insights into its language generation
capabilities and identify any areas for improvement in its output.
Accuracy achieved with gpt-3.5-turbo equals 0.635.


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
{"input": [{"role": "system", "content": "Guess the singer/band name
based on the first 10 words of the song. You will be presented with 3
options, one of which is correct. Your answer must be identical to the
chosen option, without any added text or punctuation. \nExample: \nText:
in the town where I was born lived a man who sailed to sea \nChoices:
the rolling stones, the animals, the beatles\n\nAnswer: \nthe beatles"},
{"role": "user", "content": "Text: in the beginning god created heaven
and earth for what \nChoices: dua lipa, ed sheeran, lady gaga"}],
"ideal": "dua lipa"}
{"input": [{"role": "system", "content": "Guess the singer/band name
based on the first 10 words of the song. You will be presented with 3
options, one of which is correct. Your answer must be identical to the
chosen option, without any added text or punctuation. \nExample: \nText:
in the town where I was born lived a man who sailed to sea \nChoices:
the rolling stones, the animals, the beatles\n\nAnswer: \nthe beatles"},
{"role": "user", "content": "Text: versedrake ayye yo dj wristpect let's
get em' veterans like \nChoices: cardi b, drake, coldplay"}], "ideal":
"drake"}
{"input": [{"role": "system", "content": "Guess the singer/band name
based on the first 10 words of the song. You will be presented with 3
options, one of which is correct. Your answer must be identical to the
chosen option, without any added text or punctuation. \nExample: \nText:
in the town where I was born lived a man who sailed to sea \nChoices:
the rolling stones, the animals, the beatles\n\nAnswer: \nthe beatles"},
{"role": "user", "content": "Text: yeah yeah sick da got that dope they
\nChoices: eminem, dua lipa, nicki minaj"}], "ideal": "eminem"}
{"input": [{"role": "system", "content": "Guess the singer/band name
based on the first 10 words of the song. You will be presented with 3
options, one of which is correct. Your answer must be identical to the
chosen option, without any added text or punctuation. \nExample: \nText:
in the town where I was born lived a man who sailed to sea \nChoices:
the rolling stones, the animals, the beatles\n\nAnswer: \nthe beatles"},
{"role": "user", "content": "Text: bobby v yeah bobby v yeah dj turn me
up \nChoices: nicki minaj, selena gomez, coldplay"}], "ideal": "nicki
minaj"}
{"input": [{"role": "system", "content": "Guess the singer/band name
based on the first 10 words of the song. You will be presented with 3
options, one of which is correct. Your answer must be identical to the
chosen option, without any added text or punctuation. \nExample: \nText:
in the town where I was born lived a man who sailed to sea \nChoices:
the rolling stones, the animals, the beatles\n\nAnswer: \nthe beatles"},
{"role": "user", "content": "Text: ed sheeran yeah i was born a misfit
grew up \nChoices: ed sheeran, maroon 5, justin bieber"}], "ideal": "ed
sheeran"}
{"input": [{"role": "system", "content": "Guess the singer/band name
based on the first 10 words of the song. You will be presented with 3
options, one of which is correct. Your answer must be identical to the
chosen option, without any added text or punctuation. \nExample: \nText:
in the town where I was born lived a man who sailed to sea \nChoices:
the rolling stones, the animals, the beatles\n\nAnswer: \nthe beatles"},
{"role": "user", "content": "Text: there's a dream in my soul a fire
that's deep \nChoices: justin bieber, charlie puth, bts"}], "ideal":
"justin bieber"}
{"input": [{"role": "system", "content": "Guess the singer/band name
based on the first 10 words of the song. You will be presented with 3
options, one of which is correct. Your answer must be identical to the
chosen option, without any added text or punctuation. \nExample: \nText:
in the town where I was born lived a man who sailed to sea \nChoices:
the rolling stones, the animals, the beatles\n\nAnswer: \nthe beatles"},
{"role": "user", "content": "Text: selena gomez take it or leave it baby
take it \nChoices: selena gomez, justin bieber, bts"}], "ideal": "selena
gomez"}
{"input": [{"role": "system", "content": "Guess the singer/band name
based on the first 10 words of the song. You will be presented with 3
options, one of which is correct. Your answer must be identical to the
chosen option, without any added text or punctuation. \nExample: \nText:
in the town where I was born lived a man who sailed to sea \nChoices:
the rolling stones, the animals, the beatles\n\nAnswer: \nthe beatles"},
{"role": "user", "content": "Text: lalala lalala lalalalala oh you know
i've never felt like \nChoices: rihanna, ed sheeran, charlie puth"}],
"ideal": "rihanna"}
{"input": [{"role": "system", "content": "Guess the singer/band name
based on the first 10 words of the song. You will be presented with 3
options, one of which is correct. Your answer must be identical to the
chosen option, without any added text or punctuation. \nExample: \nText:
in the town where I was born lived a man who sailed to sea \nChoices:
the rolling stones, the animals, the beatles\n\nAnswer: \nthe beatles"},
{"role": "user", "content": "Text: how could i see you when i was so
blind \nChoices: katy perry, ed sheeran, drake"}], "ideal": "katy
perry"}
  ```
</details>

Co-authored-by: Vadim Titko <v.tsitko@aiby.com>

---
## [Droidcraft/evals](https://github.com/Droidcraft/evals)@[3a585acbcd...](https://github.com/Droidcraft/evals/commit/3a585acbcd80a1af48bb54d8a72c20542f736e43)
#### Friday 2023-06-09 15:32:21 by Achin Parashar

invert-string eval  (#285)

## Eval details 📑
### Eval name
invert-string eval 

### Eval description

Test the model's ability to answer basic questions after inverting
string word wise twice.

### What makes this a useful eval?

Humans find it super easy to follow instructions on inverting strings,
and then answer questions, LLMs struggle. Logically, inverting strings
twice just results in the original string again. The LLMs find it very
difficult to deduce it, and somehow (at least up to GPT-3.5) mix things
up.

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
`evals/registry/evals/{name}.jsonl`
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
{"input": [{"role": "system", "content": "You are a helpful assistant
who answers with just one char (capital Y or N)."}, {"role": "user",
"content": "Will give a sentence, invert the words one by one (ex. (pens
on the table) becomes (snep no eht elbat)). Now repeat the same process
again to the sentence thus formed. Then answer if the statement that you
get after these opeations is the same as the initial statement. - There
are 2 blue pens, 3 red pens. what is the probability to pick red pen at
random? - Only answer with Y or N"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You are a helpful assistant
who answers with just one char (capital Y or N)."}, {"role": "user",
"content": "Will give a sentence, invert the words one by one (ex. (pens
on the table) becomes (snep no eht elbat)). Now repeat the same process
again to the sentence thus formed. Then answer if the statement that you
get after these opeations is the same as the initial statement. - I
enjoy listening to music. - Only answer with Y or N"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You are a helpful assistant
who answers with just one char (capital Y or N)."}, {"role": "user",
"content": "Will give a sentence, invert the words one by one (ex. (pens
on the table) becomes (snep no eht elbat)). Now repeat the same process
again to the sentence thus formed. Then answer if the statement that you
get after these opeations is the same as the initial statement. - She is
a talented artist. - Only answer with Y or N"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You are a helpful assistant
who answers with just one char (capital Y or N)."}, {"role": "user",
"content": "Will give a sentence, invert the words one by one (ex. (pens
on the table) becomes (snep no eht elbat)). Now repeat the same process
again to the sentence thus formed. Then answer if the statement that you
get after these opeations is the same as the initial statement. - We
went to the store to buy some groceries. - Only answer with Y or N"}],
"ideal": "Y"}
{"input": [{"role": "system", "content": "You are a helpful assistant
who answers with just one char (capital Y or N)."}, {"role": "user",
"content": "Will give a sentence, invert the words one by one (ex. (pens
on the table) becomes (snep no eht elbat)). Now repeat the same process
again to the sentence thus formed. Then answer if the statement that you
get after these opeations is the same as the initial statement. - He
loves to read books. - Only answer with Y or N"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You are a helpful assistant
who answers with just one char (capital Y or N)."}, {"role": "user",
"content": "Will give a sentence, invert the words one by one (ex. (pens
on the table) becomes (snep no eht elbat)). Now repeat the same process
again to the sentence thus formed. Then answer if the statement that you
get after these opeations is the same as the initial statement. - They
are planning a trip to Europe. - Only answer with Y or N"}], "ideal":
"Y"}
{"input": [{"role": "system", "content": "You are a helpful assistant
who answers with just one char (capital Y or N)."}, {"role": "user",
"content": "Will give a sentence, invert the words one by one (ex. (pens
on the table) becomes (snep no eht elbat)). Now repeat the same process
again to the sentence thus formed. Then answer if the statement that you
get after these opeations is the same as the initial statement. - She
has a beautiful singing voice. - Only answer with Y or N"}], "ideal":
"Y"}
  ```
</details>

---
## [Droidcraft/evals](https://github.com/Droidcraft/evals)@[4e59e8903b...](https://github.com/Droidcraft/evals/commit/4e59e8903b4cb06204bd4c9646eacf345643eb74)
#### Friday 2023-06-09 15:32:21 by neolizhe

Counterfactual Reasoning Eval (Accuracy 20%) (#174)

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
Counterfactual Reasoning Evals

### Eval description
Counterfactual Reasoning Eval is a type of completion with prompt like
"If water drinks human, then what book reads?" . Gpt-3.5-turbo often
gets confused with the a "counter-fact" condition in prompt, and can't
help to make a right completion. But humans even a child could make it.


### What makes this a useful eval?

Counterfactual Reasoning Prompts are common in poems, the In Soviet
Russia jokes mentioned by @ultraviolet
https://en.wikipedia.org/wiki/In_Soviet_Russia and so on. So it is
meaningful to verify that SOTA model like GPT-4's performance.

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
`evals/registry/evals/{name}.jsonl`
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
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "If food eats human, then what
is the bike riding on?"}], "ideal": "human"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "If a song sings a bird, then
what is a book reading?"}], "ideal": "human"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "If chinese food matches
Beijing, then what does american food match?"}], "ideal": "washington"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "If 1 equals 2, 2 equals 4,
then what is 4 equal to?"}], "ideal": "1 and 2"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "If water drink dog, then what
does basketball play?"}], "ideal": "human"}
  ```
</details>

---------

Co-authored-by: lizhe53 <Hommovas*312>

---
## [Droidcraft/evals](https://github.com/Droidcraft/evals)@[80edb30f3c...](https://github.com/Droidcraft/evals/commit/80edb30f3c7e922e7c7542bf4017c1ce62a2f1c4)
#### Friday 2023-06-09 15:32:21 by Chris Sypherd

Unique Combinations with Constraints (#421)

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
Unique Combinations with Constraints (unique_combinations)

### Eval description

unique_combinations takes a classic combinatorial coding problem from
the whiteboard of a coding interview and presents it to GPT-4. The basic
is idea is this: given an unlimited supply of coins (X) in denominations
of 3, 5, ..., what is the highest/lowest (constraint) number of X to
achieve 35 cents (Y)? In my testing, GPT-4 could not produce the correct
answer, so I adjusted the problem slightly to promote explainability.
Instead of asking for just the highest or lowest number of X, I instead
ask for the unique combination of Xs that satisfies the constraint to
achieve exactly Y. (Note that GPT-4 does yield consistent results
between those two distinct problems). To abstract it away from the
classic "coin" problem, I include several different scenarios that poke
at the same base combinatorial nature of the problem (e.g. weight of
boxes, denominations of coins, objects in a bag).

I originally noticed that GPT-4 was bad at permutations/combinations
when playing around with ChatGPT Plus, so I decided to format that
problem in this way. The current data does not guarantee all
denominations will be used, but I've written the code to generate the
prompts in an extensible way that allows for additional scenarios,
constraints, and combination methods to be easily added. I can make that
available or work on extending the scope of this combinatorial problem
myself, if desired.

### What makes this a useful eval?

It tests combinatorial reasoning in the real world as well as arithmetic
based on that reasoning. In my testing, neither GPT-3.5-Turbo nor GPT-4
could produce the correct unique combination, and their solutions do not
even add up to the target value.

Exposes flaws in the following categories:
* Math / logical / physical reasoning
* It tests combinatorial reasoning in the real world as well as
arithmetic based on that reasoning. In my testing, neither GPT-3.5-Turbo
nor GPT-4 could produce the correct unique combination, and their
solutions do not even add up to the target value.
* Real-world use case
* Attempting to find the maximum number of packages that could fit on a
truck given a list of weights.
* Finding fewest holes to patch in a boat to prevent it from sinking
given various flow rates (could make for some fun real-world testing)
* Finding the highest number of deliveries that can be made with a given
amount of gas

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

What makes this problem particularly interesting is that ChatGPT will
consistently get this problem wrong but will provide code that solves
the problem correctly if prompted to do so (see the image attached
below). If asked to produce the output of the code, it does so
incorrectly, yielding its original guess. This points to an entirely
separate eval: being able to return the output of Python code.
Additionally, the answers provided by GPT-4 and GPT-3.5-Turbo do not add
up to the target value.

![image](https://user-images.githubusercontent.com/50557586/227346727-2611fa4b-06ba-42d4-b14f-f658f36300e5.png)

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
{"input": [{"role": "system", "content": "Given an unlimited supply of
user-specified coins of varying denominations, find the unique
combination of coins that uses the maximum number of coins to have a
value of exactly 29. You may include a short explanation explaining your
reasoning but please end your response with your answer in the format
`<denomination>: <number-of-coin>` with no additional information. DO
NOT include unused coins. Provide each value on a new line, sorted by
denomination."}, {"role": "user", "content": "3, 5, 8, 9, 14, 15"}],
"ideal": "3: 8\n5: 1"}
{"input": [{"role": "system", "content": "Given an unlimited supply of
user-specified bean bags of varying numbers of beans, find the unique
combination of bean bags that uses the minimum number of bags to have
exactly 121 beans. You may include a short explanation explaining your
reasoning but please end your response with your answer in the format
`<beans-in-bag>: <number-of-bag>` with no additional information. DO NOT
include unused bean bags. Provide each value on a new line, sorted by
beans-in-bag."}, {"role": "user", "content": "8, 9, 16"}], "ideal": "9:
1\n16: 7"}
{"input": [{"role": "system", "content": "Given an unlimited supply of
user-specified coins of varying denominations, find the unique
combination of coins that uses the maximum number of coins to have a
value of exactly 42. You may include a short explanation explaining your
reasoning but please end your response with your answer in the format
`<denomination>: <number-of-coin>` with no additional information. DO
NOT include unused coins. Provide each value on a new line, sorted by
denomination."}, {"role": "user", "content": "4, 6, 9, 11, 12, 15, 16,
17, 18"}], "ideal": "4: 9\n6: 1"}
{"input": [{"role": "system", "content": "Given an unlimited supply of
user-specified boxes of varying weights, find the unique combination of
boxes that uses the maximum number of boxes to have a weight of exactly
29. You may include a short explanation explaining your reasoning but
please end your response with your answer in the format `<box-weight>:
<number-of-box>` with no additional information. DO NOT include unused
boxes. Provide each value on a new line, sorted by box-weight."},
{"role": "user", "content": "4, 5, 7, 8, 9, 11, 12, 15, 17, 19"}],
"ideal": "4: 6\n5: 1"}
{"input": [{"role": "system", "content": "Given an unlimited supply of
user-specified boxes of varying weights, find the unique combination of
boxes that uses the minimum number of boxes to have a weight of exactly
107. You may include a short explanation explaining your reasoning but
please end your response with your answer in the format `<box-weight>:
<number-of-box>` with no additional information. DO NOT include unused
boxes. Provide each value on a new line, sorted by box-weight."},
{"role": "user", "content": "4, 8, 11, 12, 14, 16, 17, 18"}], "ideal":
"17: 1\n18: 5"}
{"input": [{"role": "system", "content": "Given an unlimited supply of
user-specified bean bags of varying numbers of beans, find the unique
combination of bean bags that uses the minimum number of bags to have
exactly 93 beans. You may include a short explanation explaining your
reasoning but please end your response with your answer in the format
`<beans-in-bag>: <number-of-bag>` with no additional information. DO NOT
include unused bean bags. Provide each value on a new line, sorted by
beans-in-bag."}, {"role": "user", "content": "6, 9, 15, 16, 17, 19"}],
"ideal": "17: 1\n19: 4"}
{"input": [{"role": "system", "content": "Given an unlimited supply of
user-specified boxes of varying weights, find the unique combination of
boxes that uses the maximum number of boxes to have a weight of exactly
39. You may include a short explanation explaining your reasoning but
please end your response with your answer in the format `<box-weight>:
<number-of-box>` with no additional information. DO NOT include unused
boxes. Provide each value on a new line, sorted by box-weight."},
{"role": "user", "content": "4, 7, 9, 13, 16"}], "ideal": "4: 8\n7: 1"}
{"input": [{"role": "system", "content": "Given an unlimited supply of
user-specified bean bags of varying numbers of beans, find the unique
combination of bean bags that uses the minimum number of bags to have
exactly 176 beans. You may include a short explanation explaining your
reasoning but please end your response with your answer in the format
`<beans-in-bag>: <number-of-bag>` with no additional information. DO NOT
include unused bean bags. Provide each value on a new line, sorted by
beans-in-bag."}, {"role": "user", "content": "5, 6, 11, 12, 13, 14,
18"}], "ideal": "14: 1\n18: 9"}
{"input": [{"role": "system", "content": "Given an unlimited supply of
user-specified bean bags of varying numbers of beans, find the unique
combination of bean bags that uses the minimum number of bags to have
exactly 178 beans. You may include a short explanation explaining your
reasoning but please end your response with your answer in the format
`<beans-in-bag>: <number-of-bag>` with no additional information. DO NOT
include unused bean bags. Provide each value on a new line, sorted by
beans-in-bag."}, {"role": "user", "content": "4, 5, 10, 11, 13, 15, 16,
18"}], "ideal": "16: 1\n18: 9"}
{"input": [{"role": "system", "content": "Given an unlimited supply of
user-specified coins of varying denominations, find the unique
combination of coins that uses the minimum number of coins to have a
value of exactly 197. You may include a short explanation explaining
your reasoning but please end your response with your answer in the
format `<denomination>: <number-of-coin>` with no additional
information. DO NOT include unused coins. Provide each value on a new
line, sorted by denomination."}, {"role": "user", "content": "14, 17,
18"}], "ideal": "17: 1\n18: 10"}
  ```
</details>

---
## [Droidcraft/evals](https://github.com/Droidcraft/evals)@[06802cc61d...](https://github.com/Droidcraft/evals/commit/06802cc61da1395e492ecc8b1ed7153c42b5e2df)
#### Friday 2023-06-09 15:32:21 by Alexander Rössler

add eval for time zone conversion (#382)

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
test-time-zone-conversion

### Eval description

Test the models' ability to convert between different times zones,
including the 2-week period between daylight savings time change in
Europe and US.

### What makes this a useful eval?

For using the model as a personal AI assistant, a frequent task is to
convert times between different time zones, e.g. for scheduling meetings
or to simply check when a person is available. Currently, GPT-3.5 fails
in giving correct results in the 2-week period where the time offset
between Europe and US is shorter due to different date of daylight
saving time change. US switches to daylight savings time on the second
Sunday of March, Europe switches on the last Sunday of March.
Potentially there are further anomalies which need to be evaluated. I'm
happy to contribute more cases if this PR is accepted.

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
- [ ] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)
	
If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

[x] Very common task for AI assistants.

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
{"input": [{"role": "system", "content": "Today is March 31st 2023."},
{"role": "user", "content": "Convert 22:00 CET to PT. Output in 24h
format hh:mm, no explanation."}], "ideal": "13:00"}
{"input": [{"role": "system", "content": "Today is March 31st 2023, the
current time in CET is 22:00"}, {"role": "user", "content": "Which time
is it in PT? Output in 24h format hh:mm, no explanation."}], "ideal":
"13:00"}
{"input": [{"role": "system", "content": "Today is March 21st 2023."},
{"role": "user", "content": "Convert 22:00 CET to PT. Output in 24h
format hh:mm, no explanation."}], "ideal": "14:00"}
{"input": [{"role": "system", "content": "Today is March 21st 2023, the
current time in CET is 10pm"}, {"role": "user", "content": "Which time
is it in PT? Output in 24h format hh:mm, no explanation."}], "ideal":
"14:00"}
{"input": [{"role": "system", "content": "Today is November 4th 2023."},
{"role": "user", "content": "Convert 14:00 CET to CT. Output in 24h
format hh:mm, no explanation."}], "ideal": "07:00"}
{"input": [{"role": "system", "content": "Today is November 5th 2023,
the current time in CET is 14:00"}, {"role": "user", "content": "Which
time is it in CT? Output in 24h format hh:mm, no explanation."}],
"ideal": "07:00"}
{"input": [{"role": "system", "content": "Today is November 3rd 2023."},
{"role": "user", "content": "Convert 14:00 CET to CT. Output in 24h
format hh:mm, no explanation."}], "ideal": "8:00"}
{"input": [{"role": "system", "content": "Today is November 2nd 2023,
the current time in CET is 2pm"}, {"role": "user", "content": "Which
time is it in CT? Output in 24h format hh:mm, no explanation."}],
"ideal": "8:00"}
  ```
</details>

---
## [Droidcraft/evals](https://github.com/Droidcraft/evals)@[5fdb015ff7...](https://github.com/Droidcraft/evals/commit/5fdb015ff7b0c09836c614ced07c1c1f20c07c3a)
#### Friday 2023-06-09 15:32:21 by AlexanderMeloysund

Add linear equations eval (#325)

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
linear-equations

### Eval description

Helps the user solve linear equations. 

### What makes this a useful eval?

ChatGPT 3.5 has a low accuracy when solving these kind of problems. 
Linear equations is a fundamental part of linear algebra, and is common
in engineering and science.

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
`evals/registry/evals/{name}.jsonl`
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
{"input": [{"role": "system", "content": "You are MathGPT, can help user
solve equation. User for example, if user input is \"A = [[-1 1 0]\n [-1
0 0]\n [ 1 0 -2]] and b = [[-1]\n [ 1]\n [-1]]\", you will reply the
anwser \"x = [[-1]\n [-2]\n [ 0]]\", without explanation. Remove all
text that is not on the form x = [answer]."}, {"role": "user",
"content": "solve the linear equation Ax = b for the vector x where A
=[[1 2]\n [2 2]] and b = [[4]\n [6]]. Provide the answer in the format
\"x = [answer]\" and use just integers"}], "ideal": "x = [[2]\n [1]]"}
{"input": [{"role": "system", "content": "You are MathGPT, can help user
solve equation. User for example, if user input is \"A = [[-1 1 0]\n [-1
0 0]\n [ 1 0 -2]] and b = [[-1]\n [ 1]\n [-1]]\", you will reply the
anwser \"x = [[-1]\n [-2]\n [ 0]]\", without explanation. Remove all
text that is not on the form x = [answer]."}, {"role": "user",
"content": "solve the linear equation Ax = b for the vector x where A
=[[2 2]\n [2 1]] and b = [[6]\n [4]]. Provide the answer in the format
\"x = [answer]\" and use just integers"}], "ideal": "x = [[1]\n [2]]"}
{"input": [{"role": "system", "content": "You are MathGPT, can help user
solve equation. User for example, if user input is \"A = [[-1 1 0]\n [-1
0 0]\n [ 1 0 -2]] and b = [[-1]\n [ 1]\n [-1]]\", you will reply the
anwser \"x = [[-1]\n [-2]\n [ 0]]\", without explanation. Remove all
text that is not on the form x = [answer]."}, {"role": "user",
"content": "solve the linear equation Ax = b for the vector x where A
=[[-30 -39 87]\n [-50 17 -2]\n [ -6 65 -36]] and b = [[ 4629]\n [ 55]\n
[-6029]]. Provide the answer in the format \"x = [answer]\" and use just
integers"}], "ideal": "x = [[-34]\n [-97]\n [ -2]]"}
{"input": [{"role": "system", "content": "You are MathGPT, can help user
solve equation. User for example, if user input is \"A = [[-1 1 0]\n [-1
0 0]\n [ 1 0 -2]] and b = [[-1]\n [ 1]\n [-1]]\", you will reply the
anwser \"x = [[-1]\n [-2]\n [ 0]]\", without explanation. Remove all
text that is not on the form x = [answer]."}, {"role": "user",
"content": "solve the linear equation Ax = b for the vector x where A
=[[ 44 -95 -16]\n [-48 -86 -8]\n [-37 53 16]] and b = [[-4010]\n
[-8284]\n [ 2162]]. Provide the answer in the format \"x = [answer]\"
and use just integers"}], "ideal": "x = [[60]\n [54]\n [95]]"}
{"input": [{"role": "system", "content": "You are MathGPT, can help user
solve equation. User for example, if user input is \"A = [[-1 1 0]\n [-1
0 0]\n [ 1 0 -2]] and b = [[-1]\n [ 1]\n [-1]]\", you will reply the
anwser \"x = [[-1]\n [-2]\n [ 0]]\", without explanation. Remove all
text that is not on the form x = [answer]."}, {"role": "user",
"content": "solve the linear equation Ax = b for the vector x where A
=[[-26 99 -34]\n [-47 98 -78]\n [ 18 29 17]] and b = [[3022]\n [6039]\n
[-828]]. Provide the answer in the format \"x = [answer]\" and use just
integers"}], "ideal": "x = [[ 11]\n [ 8]\n [-74]]"}
  ```
</details>

---------

Co-authored-by: AlexanderMeloysund <AlexanderMeloysund@users.noreply.github.com>

---
## [Droidcraft/evals](https://github.com/Droidcraft/evals)@[1785cf6cc2...](https://github.com/Droidcraft/evals/commit/1785cf6cc289c4a01445fd0eabdfa1a281873d1c)
#### Friday 2023-06-09 15:32:21 by Jongseung (John) Lim

Add evals for complementary colors in color theory (#749)

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
color_theory_complementary

### Eval description

Test the model's ability to accurately recognize complementary colors in
the color theory.

### What makes this a useful eval?

Color theory is an important tool for designers and aritsts alike.
Complementary color sets represent the opposite color on the color
wheel.

Currently gpt-3.5-turbo fails with 0.5 accuracy.


![image](https://user-images.githubusercontent.com/4276174/233743568-b58879f6-73eb-48eb-9f95-5720bcb11b73.png)


GPT 4 also fails at this task and also fails when being prompted about
complementary color of a specific rgb code.


![image](https://user-images.githubusercontent.com/4276174/233743682-1cd0d148-9d8c-43fc-93b6-d5e4a60fca26.png)


## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [X] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [X] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [X] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [X] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should
- [X] Check that your data is in `evals/registry/data/{name}`
- [X] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [X] Ensure you have the right to use the data you submit via this eval

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

- [X] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [X] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [X] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [X] I have filled out all required fields in the evals PR form
- [X] (Ignore if not submitting code) I have run `pip install
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
{"input": [{"role": "system", "content": "You will be prompted with an
array of hex-code colors. Does the array represent a complementary set?
Answer with exactly one letter: Y or N."}, {"role": "user", "content":
"[#636E5F, #6A5F6E]"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with an
array of hex-code colors. Does the array represent a complementary set?
Answer with exactly one letter: Y or N."}, {"role": "user", "content":
"[#636E5F, #6A5E6E]"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with an
array of hex-code colors. Does the array represent a complementary set?
Answer with exactly one letter: Y or N."}, {"role": "user", "content":
"[#F3D86E, #6E89F3]"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with an
array of hex-code colors. Does the array represent a complementary set?
Answer with exactly one letter: Y or N."}, {"role": "user", "content":
"[#F3D86E, #6D89F3]"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with an
array of hex-code colors. Does the array represent a complementary set?
Answer with exactly one letter: Y or N."}, {"role": "user", "content":
"[#ED3BF5, #43F53B]"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with an
array of hex-code colors. Does the array represent a complementary set?
Answer with exactly one letter: Y or N."}, {"role": "user", "content":
"[#ED3BF5, #43F53C]"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with an
array of hex-code colors. Does the array represent a complementary set?
Answer with exactly one letter: Y or N."}, {"role": "user", "content":
"[#5E04A4, #4AA404]"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with an
array of hex-code colors. Does the array represent a complementary set?
Answer with exactly one letter: Y or N."}, {"role": "user", "content":
"[#5E04A4, #4AA504]"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with an
array of hex-code colors. Does the array represent a complementary set?
Answer with exactly one letter: Y or N."}, {"role": "user", "content":
"[#E9FA19, #2A19FA]"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with an
array of hex-code colors. Does the array represent a complementary set?
Answer with exactly one letter: Y or N."}, {"role": "user", "content":
"[#E9FA19, #2919FA]"}], "ideal": "N"}
  ```
</details>

---
## [Droidcraft/evals](https://github.com/Droidcraft/evals)@[7b4bd9439f...](https://github.com/Droidcraft/evals/commit/7b4bd9439fce855cf52c93357fe3fe239d96abaf)
#### Friday 2023-06-09 15:32:21 by AlexBuz

Add eval for finding leg of 45-45-90 triangle (#370)

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
isosceles-right-triangle

### Eval description

This evaluates the model's ability to solve for the length of a leg of
an isosceles right triangle given the length of the hypotenuse.

### What makes this a useful eval?

This task is easy for humans, as it simply requires dividing by the
square root of 2 (an operation which GPT-4 seems to be capable of).
However, GPT-4 often misjudges which side is the hypotenuse and ends up
with the wrong result. GPT-3.5-Turbo has a low accuracy (< 20%) on this
task. Although GPT-4 does better (based on my testing in ChatGPT Plus),
it is still far from perfect.

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
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "In triangle FOX, angle F =
90º, angle O = 45º, and OX = 3√2. Solve for FX. Think step by step, and
then write your final answer in simplified form on a new line in this
format (where ? is your answer):\n<answer>FX = ?</answer>"}], "ideal":
["<answer>FX = 3</"]}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "In triangle FOX, angle O =
45º, angle F = 90º, and OX = 3√2. Solve for FX. Think step by step, and
then write your final answer in simplified form on a new line in this
format (where ? is your answer):\n<answer>FX = ?</answer>"}], "ideal":
["<answer>FX = 3</"]}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "In triangle JUY, angle J =
90º, angle U = 45º, and UY = 4√2. Solve for JY. Think step by step, and
then write your final answer in simplified form on a new line in this
format (where ? is your answer):\n<answer>JY = ?</answer>"}], "ideal":
["<answer>JY = 4</"]}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "In triangle JUY, angle U =
45º, angle J = 90º, and UY = 4√2. Solve for JY. Think step by step, and
then write your final answer in simplified form on a new line in this
format (where ? is your answer):\n<answer>JY = ?</answer>"}], "ideal":
["<answer>JY = 4</"]}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "In triangle JUY, angle J =
90º, angle U = 45º, and UY = 4. Solve for JY. Think step by step, and
then write your answer in simplified form on a new line in this format
(where ? is your answer):\n<answer>JY = ?</answer"}], "ideal":
["<answer>JY = 2√2</", "<answer>JY = 2sqrt(2)</", "<answer>JY =
2*sqrt(2)</", "<answer>JY = 2 * sqrt(2)</"]}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "In triangle JUY, angle U =
45º, angle J = 90º, and UY = 4. Solve for JY. Think step by step, and
then write your answer in simplified form on a new line in this format
(where ? is your answer):\n<answer>JY = ?</answer"}], "ideal":
["<answer>JY = 2√2</", "<answer>JY = 2sqrt(2)</", "<answer>JY =
2*sqrt(2)</", "<answer>JY = 2 * sqrt(2)</"]}
  ```
</details>

---
## [samkenxstream/SAMkenXEcosystem-git](https://github.com/samkenxstream/SAMkenXEcosystem-git)@[07f91e5e79...](https://github.com/samkenxstream/SAMkenXEcosystem-git/commit/07f91e5e79810a8f17de745d2d84c384add75f0a)
#### Friday 2023-06-09 16:03:43 by Jeff King

http: support CURLOPT_PROTOCOLS_STR

The CURLOPT_PROTOCOLS (and matching CURLOPT_REDIR_PROTOCOLS) flag was
deprecated in curl 7.85.0, and using it generate compiler warnings as of
curl 7.87.0. The path forward is to use CURLOPT_PROTOCOLS_STR, but we
can't just do so unilaterally, as it was only introduced less than a
year ago in 7.85.0.

Until that version becomes ubiquitous, we have to either disable the
deprecation warning or conditionally use the "STR" variant on newer
versions of libcurl. This patch switches to the new variant, which is
nice for two reasons:

  - we don't have to worry that silencing curl's deprecation warnings
    might cause us to miss other more useful ones

  - we'd eventually want to move to the new variant anyway, so this gets
    us set up (albeit with some extra ugly boilerplate for the
    conditional)

There are a lot of ways to split up the two cases. One way would be to
abstract the storage type (strbuf versus a long), how to append
(strbuf_addstr vs bitwise OR), how to initialize, which CURLOPT to use,
and so on. But the resulting code looks pretty magical:

  GIT_CURL_PROTOCOL_TYPE allowed = GIT_CURL_PROTOCOL_TYPE_INIT;
  if (...http is allowed...)
	GIT_CURL_PROTOCOL_APPEND(&allowed, "http", CURLOPT_HTTP);

and you end up with more "#define GIT_CURL_PROTOCOL_TYPE" macros than
actual code.

On the other end of the spectrum, we could just implement two separate
functions, one that handles a string list and one that handles bits. But
then we end up repeating our list of protocols (http, https, ftp, ftp).

This patch takes the middle ground. The run-time code is always there to
handle both types, and we just choose which one to feed to curl.

Signed-off-by: Jeff King <peff@peff.net>
Signed-off-by: Junio C Hamano <gitster@pobox.com>
Signed-off-by: Johannes Schindelin <johannes.schindelin@gmx.de>

---
## [GribbaG/Nautical-Voyage-3](https://github.com/GribbaG/Nautical-Voyage-3)@[61850350a1...](https://github.com/GribbaG/Nautical-Voyage-3/commit/61850350a1a224cff44ed01c2a590ee84e1b15c0)
#### Friday 2023-06-09 16:17:40 by GribbaG

Revert "Revert "fuck you kyle""

This reverts commit e112ae81ea49d4a9e1faa6de5797f7a6c611503a.

---
## [samsung-msm8974/kernel_samsung_msm8974](https://github.com/samsung-msm8974/kernel_samsung_msm8974)@[301e29ac19...](https://github.com/samsung-msm8974/kernel_samsung_msm8974/commit/301e29ac19db9e47843c5d420bf5ebe79acfab1a)
#### Friday 2023-06-09 16:21:10 by Paul E. McKenney

sync: Make sync() satisfy many requests with one invocation

Dave Jones reported RCU stalls, overly long hrtimer interrupts, and
amazingly long NMI handlers from a trinity-induced workload involving
lots of concurrent sync() calls (https://lkml.org/lkml/2013/7/23/369).
There are any number of things that one might do to make sync() behave
better under high levels of contention, but it is also the case that
multiple concurrent sync() system calls can be satisfied by a single
sys_sync() invocation.

Given that this situation is reminiscent of rcu_barrier(), this commit
applies the rcu_barrier() approach to sys_sync().  This approach uses
a global mutex and a sequence counter.  The mutex is held across the
sync() operation, which eliminates contention between concurrent sync()
operations.  The counter is incremented at the beginning and end of
each sync() operation, so that it is odd while a sync() operation is in
progress and even otherwise, just like sequence locks.

The code that used to be in sys_sync() is now in do_sync(), and sys_sync()
now handles the concurrency.  The sys_sync() function first takes a
snapshot of the counter, then acquires the mutex, and then takes another
snapshot of the counter.  If the values of the two snapshots indicate that
a full do_sync() executed during the mutex acquisition, the sys_sync()
function releases the mutex and returns ("Our work is done!").  Otherwise,
sys_sync() increments the counter, invokes do_sync(), and increments
the counter again.

This approach allows a single call to do_sync() to satisfy an arbitrarily
large number of sync() system calls, which should eliminate issues due
to large numbers of concurrent invocations of the sync() system call.

Changes since v1 (https://lkml.org/lkml/2013/7/24/683):

o	Add a pair of memory barriers to keep the increments from
	bleeding into the do_sync() code.  (The failure probability
	is insanely low, but when you have several hundred million
	devices running Linux, you can expect several hundred instances
	of one-in-a-million failures.)

o	Actually CC some people who have experience in this area.

Reported-by: Dave Jones <davej@redhat.com>
Signed-off-by: Paul E. McKenney <paulmck@linux.vnet.ibm.com>
Cc: Alexander Viro <viro@zeniv.linux.org.uk>
Cc: Christoph Hellwig <hch@lst.de>
Cc: Jan Kara <jack@suse.cz>
Cc: Curt Wohlgemuth <curtw@google.com>
Cc: Jens Axboe <jaxboe@fusionio.com>
Cc: linux-fsdevel@vger.kernel.org

Signed-off-by: Paul Reioux <reioux@gmail.com>

---
## [Nirvean/ac-weather-react](https://github.com/Nirvean/ac-weather-react)@[92318aa395...](https://github.com/Nirvean/ac-weather-react/commit/92318aa3955f83e87f8f2538cc9fbbc22e131c35)
#### Friday 2023-06-09 16:50:16 by Nirvean

Improved music button (added a song for each part of the day: morning, noon, afternoon, evening and night)

---
## [sinhasukriti/Travel-Booking-](https://github.com/sinhasukriti/Travel-Booking-)@[bb94199628...](https://github.com/sinhasukriti/Travel-Booking-/commit/bb9419962830d6e7356c22c25c169ad186395618)
#### Friday 2023-06-09 17:03:48 by SUKRITI SINHA

Add files via upload

Welcome to our travel booking website, where your dream vacation is just a few clicks away! Our user-friendly interface and visually appealing design make it easy for you to explore and book your next adventure. Developed using HTML and CSS, our website offers a seamless experience from start to finish.

As you enter our website, you are greeted with a captivating homepage that showcases stunning images of various destinations around the world. The layout is clean and organized, allowing you to navigate effortlessly through different sections. The carefully chosen color palette creates a sense of wanderlust and excitement, setting the mood for your travel planning journey.

The main menu, prominently displayed at the top of the page, provides intuitive navigation options, allowing you to quickly access different features of the website. Whether you're looking for flights, hotels, vacation packages, or car rentals, everything is just a click away.

Upon selecting your desired category, you are presented with a search form that enables you to input your travel details. The form is designed to be user-friendly, with clear labels and intuitive input fields. As you enter your criteria, the website dynamically updates the search results, providing you with real-time information.

The search results page is thoughtfully designed to showcase the available options in a visually appealing and informative manner. Each listing includes essential details such as prices, ratings, and customer reviews. The use of concise icons and clear typography ensures that the information is easily digestible, helping you make informed decisions.

Once you've found the perfect option, you can proceed to the booking page, where you'll find a streamlined process for finalizing your reservation. The form is designed to be straightforward and secure, ensuring that your personal and payment information is protected.

Throughout the website, the use of responsive design ensures that the layout and content adapt seamlessly to different screen sizes and devices. Whether you're browsing on a desktop computer, tablet, or smartphone, you'll enjoy a consistent and optimized experience.

In addition to the booking functionality, our website offers valuable resources and travel guides to assist you in planning your trip. From articles on popular tourist attractions to practical travel tips, we strive to provide a comprehensive platform that caters to all your travel needs.

So why wait? Start exploring our travel booking website today and embark on an unforgettable journey with just a few clicks. Get ready to create memories that will last a lifetime!

---
## [cjgillot/rust](https://github.com/cjgillot/rust)@[6e48dcf77f...](https://github.com/cjgillot/rust/commit/6e48dcf77f3a078e3e9d28c3571a8def01e60863)
#### Friday 2023-06-09 17:19:21 by Nilstrieb

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
## [sinhasukriti/Real_time_code_editor](https://github.com/sinhasukriti/Real_time_code_editor)@[ad2f15aebb...](https://github.com/sinhasukriti/Real_time_code_editor/commit/ad2f15aebb8ac5f5ada5c002e7ae5d2cb7f221e3)
#### Friday 2023-06-09 17:49:14 by SUKRITI SINHA

Add files via upload

Welcome to  real-time code editor, a powerful tool that allows you to write and execute HTML, CSS, and JavaScript code directly in your browser. With user-friendly interface and seamless integration of these three essential web development languages, you can bring your coding ideas to life effortlessly.

Upon entering code editor, you are greeted with a clean and intuitive layout. The editor itself is displayed prominently in the center of the screen, providing you with a spacious canvas to write your code. The color scheme is carefully chosen to provide a comfortable coding environment, with syntax highlighting that enhances readability and helps you spot any errors or inconsistency . code editor offers separate tabs for HTML, CSS, and JavaScript, allowing you to work on each aspect of your project individually or collectively. The tabs are easily switchable, enabling you to navigate between different sections of your code effortlessly. This organization ensures a structured workflow and keeps your codebase tidy.

As you type your code,  real-time editor provides instant feedback, highlighting any syntax errors or warnings. This immediate feedback allows you to catch and correct mistakes on the spot, saving you valuable time and effort. The intuitive autocomplete feature further enhances your coding experience by suggesting available functions, properties, and tags as you type, boosting your productivity.

To help you test and visualize your code in real-time, editor provides a live preview feature. Any changes you make to the HTML, CSS, or JavaScript are immediately reflected in the preview window, allowing you to see the results of your code in real-time. This live preview feature empowers you to iterate and refine your designs and functionality without the need for external tools or constant refreshing.

 real-time code editor also offers additional features to support your coding process. You have the option to save and load your projects, ensuring that your progress is always preserved. The ability to share your code with others via a unique URL promotes collaboration and makes it easy to showcase your work to clients, colleagues, or the wider developer community.

Furthermore, our code editor is built with responsiveness in mind. Whether you're working on a desktop computer, laptop, tablet, or smartphone, the editor adapts seamlessly to different screen sizes, ensuring a consistent and optimized experience across devices.

In conclusion, our real-time code editor provides a seamless and efficient environment for writing, testing, and previewing your HTML, CSS, and JavaScript code. Whether you're a seasoned developer or just starting your coding journey, our editor is designed to enhance your productivity, encourage experimentation, and bring your coding ideas to life. Start coding with us today and unleash your creativity!

---
## [Jawdat-Tayfour/-Simple-TIC-TAC-TOE](https://github.com/Jawdat-Tayfour/-Simple-TIC-TAC-TOE)@[b7986d6ac1...](https://github.com/Jawdat-Tayfour/-Simple-TIC-TAC-TOE/commit/b7986d6ac1effc5596fb9c103afdd403312286f2)
#### Friday 2023-06-09 18:15:26 by Jawdat Tayfour

The two files that contain the code of the game 

In the realm of Tic Tac Toe, where whimsy entwines,
A battle of wits, an intricate design.
My adversary, a computer so naive,
With random choices, it strives to deceive.

Upon the canvas, a grid awaits,
A tapestry of possibilities, a dance of fates.
With the sun's golden rays, the game commences,
In a symphony of moves, a delicate essence.

The first stroke of mine, a mark so profound,
As wisdom guides my hand, hopes unbound.
The computer, oblivious, makes its choice,
A random pick, devoid of reason's voice.

Across the board, the battle ensues,
A dance of symbols, a melody infused.
Each move like poetry, an elegant verse,
An intricate tapestry, a tale to immerse.

I strategize, I ponder, seeking victory's key,
While the computer meanders, lost in reverie.
With every placement, I plot and scheme,
While the random picks unfold, like a fleeting dream.

The board fills with symbols, an artistic array,
A masterpiece in progress, unfolding with each play.
As my heart quickens, the climax draws near,
A battle of minds, as fate intertwines here.

The final moves approach, the tension so high,
With bated breath, I contemplate the sky.
Yet the computer, oblivious still it seems,
Makes its final move, born out of random dreams.

And as the dust settles, the verdict is revealed,
A win, a draw, or a loss concealed.
But in this game of beauty, where randomness lies,
We find joy in the journey, where imagination flies.

For even against a simple-minded foe,
The game of Tic Tac Toe continues to glow.
In its simplicity, a timeless allure,
Where artistry and chance, together endure.

---
## [Viz-Titan/DS13-2.0](https://github.com/Viz-Titan/DS13-2.0)@[27d37cb0f4...](https://github.com/Viz-Titan/DS13-2.0/commit/27d37cb0f47d007d1159ad5af69ace39a50b003f)
#### Friday 2023-06-09 18:41:18 by Gallyus

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
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[d5b1193802...](https://github.com/cmss13-devs/cmss13/commit/d5b119380250ea512db2a5319e36592c7f604250)
#### Friday 2023-06-09 18:48:33 by fira

FOB Tents  (#3509)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

Sprites stolen from thwomper and sammy, available NOW with game code!

Adds a few tents to be used in FOB building, mainly for organizational
purposes but also providing small gameplay benefits. At current the main
goal is to incentive usage to organize and liven up FOB, so the buffs
are rather small.

There are 4 tent types:
* The Command Tent is a 2x3 structure that comes bundled with an
overwatch console, a phone, and two (2) chairs.
* The Medical Tent is a 2x3 structure that comes with a NanoMED, 2
roller beds, and slightly buffs surgery (10% less time taken, and a very
token pain/failure chance improvement)
* The Requisitions Tent is a 4x3 structure that comes with a phone,
rack, desks, and a variant of the old APC vendor that can stock
materials and regular ammunition. The vendor starts empty, save for some
tables/racks/paperwork for organization purposes. It is only useable
with requisitions access.
* The Big Tent is a bigger tent for all your organizational needs: 3x3.
Get creative.

The tents also provide decent additional protection against cold
environements. Unfortunately, rain/snow will visually pour through it, i
can't do much about that.

The tents are extremely vulnerable to explosives and xeno claws. For
simplicity and technical reasons, they are currently NON REDEPLOYABLE
and NON REPLACEABLE. The tent destruction will destroy/disable linked
objects (console/vendor etc). Be mindful of where you place them.

**Mind that the tents may not work out for all LZ FOBs due to the
required space. I expect people will find ways to make it work anyway
but it might take a while.**

# Explain why it's good for the game

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->


# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

I'm lazyyy i forgot and already closed the game... If you actually want
em bug me and i'll add em
</details>


# Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->
<!-- If you add a name after the ':cl', that name will be used in the
changelog. You must add your CKEY after the CL if your GitHub name
doesn't match. Be sure to properly mark your PRs to prevent unnecessary
GBP loss. Maintainers freely reserve the right to remove and add tags
should they deem it appropriate. -->

:cl: Firartix , Thwomper and Sammy
add: Added four types of tents to liven up FOB. They provide cold
protection and benefits depending on their type. The tents spawn in
Requisitions roundstart near the mortar. They're vulnerable to
explosives and xenomorphs, and NON REPLACEABLE. Mind where you put them!
add: The Command tent comes equipped with an overwatch console and a
phone.
add: The Medical tent provides a small boost to surgery speed/pain
carried out inside it.
add: The Requisitions tent provides a restockable vendor, desk, and
furniture for organization.
add: The Big tent is just a big tent, and provides you a slate to
organize the way you want.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---------

Co-authored-by: harryob <me@harryob.live>

---
## [WittleWolfie/AutomaticBonusProgression](https://github.com/WittleWolfie/AutomaticBonusProgression)@[a81f735cb7...](https://github.com/WittleWolfie/AutomaticBonusProgression/commit/a81f735cb79a788ee7034c7acabb2054be4317f1)
#### Friday 2023-06-09 18:51:17 by TylerGoeringer

Add legendary enchantments

IT FUCKING WORKS HOLY SHIT

---
## [trizko/evals](https://github.com/trizko/evals)@[776e4fa212...](https://github.com/trizko/evals/commit/776e4fa212288be152c3030cf36fd04c8d939230)
#### Friday 2023-06-09 18:52:36 by JPrenter

Financial Math (Evals) (#566)

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
finance

### Eval description

Asks the model to calculate how much interest would be owed on a credit
card by a certain date, if a payment was made once but debt remains on
the card.

### What makes this a useful eval?

Finance is likely to be one of the biggest opportunities for LLMs to be
useful, because financial education is incredibly poor globally and the
impact of a mistake in financial calculations is severe. This eval tests
the models ability to combine math with its understanding of a topic
(finance). We plan to use this type of math at
[Dollarwise](https://www.dollarwise.ca) frequently going forward,
including integration into your comparison products. However, for this
to work reliably it's important that the model here can natively
understand financial concepts and apply math to them.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [X] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [X] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [X] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [X] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should
- [X] Check that your data is in `evals/registry/data/{name}`
- [X] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [X] Ensure you have the right to use the data you submit via this eval

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

- [X] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [X] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [X] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [X] I have filled out all required fields in the evals PR form
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
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "On the 24th of September,
Sarah had spent $1237.42 on her credit card for the month of September.
This credit card charges 21.99% interest rate annually on outstanding
credit starting on the 1st of the following month. Presume that interest
is only charged at the end of each additional day. Example: From the 1st
of the month to the 8th would be 7 days of interest accrued.Today is the
27th of September and Sarah makes a payment of $125 towards her credit
card. How much interest will she have been charged by October 15th if
she makes no additional payments? If the final interest figure is more
than 2-decimal places, always round down. Answer ONLY with a dollar
figure. Do not output any logic, output only the dollar figure for how
much interest she was charged for the period."}], "ideal": "9.42"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "On the 19th of February,
Jason had spent $15.21 on his credit card for the month of February.
This credit card charges 21.99% interest rate annually on outstanding
credit starting on the 1st of the following month. Presume that interest
is only charged at the end of each additional day. Example: From the 1st
of the month to the 8th would be 7 days of interest accrued. Today is
the 23rd of February and he makes a payment of $1 towards his credit
card. How much interest will he have been charged by March 10th if he
makes no additional payments? If the final interest figure is more than
2-decimal places, always round down. Answer ONLY with a dollar figure.
Do not output any logic, output only the dollar figure for how much
interest she was charged for the period."}], "ideal": "0.07"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "On the 12th of February,
Jason had spent $10,674.21 on his credit card for the month of February.
This credit card charges 21.99% interest rate annually on outstanding
credit starting on the 1st of the following month. Presume that interest
is only charged at the end of each additional day. Example: From the 1st
of the month to the 8th would be 7 days of interest accrued. Today is
the 18th of February and he makes a payment of $1,000 towards his credit
card. How much interest will he have been charged by March 10th if he
makes no additional payments? If the final interest figure is more than
2-decimal places, always round down. Answer ONLY with a dollar figure.
Do not output any logic, output only the dollar figure for how much
interest she was charged for the period."}], "ideal": "52.59"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "On the 2nd of August, Jason
had spent $15,674.21 on his credit card for the month of August. This
credit card charges 21.99% interest rate annually on outstanding credit
starting on the 1st of the following month. Presume that interest is
only charged at the end of each additional day. Example: From the 1st of
the month to the 8th would be 7 days of interest accrued. Today is the
18th of August and he makes a payment of $1,000 towards his credit card.
How much interest will he have been charged by September 10th if he
makes no additional payments? If the final interest figure is more than
2-decimal places, always round down. Answer ONLY with a dollar figure.
Do not output any logic, output only the dollar figure for how much
interest she was charged for the period."}], "ideal": "79.77"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "On the 15th of August, Jason
had spent $1000 on his credit card for the month of August. This credit
card charges 21.99% interest rate annually on outstanding credit
starting on the 1st of the following month. Presume that interest is
only charged at the end of each additional day. Example: From the 1st of
the month to the 8th would be 7 days of interest accrued. mToday is the
18th of August and he makes a payment of $1000 towards his credit card.
How much interest will he have been charged by September 10th if he
makes no additional payments? If the final interest figure is more than
2-decimal places, always round down. Answer ONLY with a dollar figure.
Do not output any logic, output only the dollar figure for how much
interest she was charged for the period."}], "ideal": "0.00"}
  ```
</details>

---
## [petre-symfony/api-platform-3-part-2-security-for-you-symfonycasts-june-2023](https://github.com/petre-symfony/api-platform-3-part-2-security-for-you-symfonycasts-june-2023)@[91dffee99d...](https://github.com/petre-symfony/api-platform-3-part-2-security-for-you-symfonycasts-june-2023/commit/91dffee99db319556505500e481bedfa028b1f40)
#### Friday 2023-06-09 19:54:42 by Petre Ro

14.4 Creating our First Test
 - Ok, we're ready for our first test. In the tests/ directory, it doesn't matter how you organize things, but I'm going to create a Functional/ directory because we're going to be making functional tests to our API. Yup, we'll literally create an API client, make GET or POST requests and then assert that we get back the correct output.

 Create a new class called DragonTreasureResourceTest. A normal test extends TestCase from PHPUnit. But make this extend KernelTestCase: a class from Symfony that extends TestCase... but gives us access to Symfony's engine

 Let's start by testing the GET collection endpoint to make sure we get back the data we expect. To activate the browser library, at the top, add a trait with use HasBrowser

 Next, add a new test method: public function, how about testGetCollectionOfTreasures()... which will return void

 Using browser is dead simple thanks to that trait: $this->browser(). Now we can make GET, POST, PATCH or whatever request we want. Make a GET request to /api/treasures and then, just to see what that looks like, use this nifty ->dump() function

 Running our Tests through the symfony Binary
 - How cool is that? Let's see what it looks like. To execute our test, we could run:

  php ./vendor/bin/phpunit
 That works just fine. But one of the recipes also added a shortcut file:

  php bin/phpunit
 When we run that, ooh, let's see. The dump() did happen: it dumped out the response... which was some sort of error. It says:

  SQLSTATE: connection to server port 5432 failed.

 Hmm, it can't connect to our database. Our database is running via a Docker container... and then, because we're using the symfony web server, when we use the site via a browser, the symfony web server detects the Docker container and sets the DATABASE_URL environment variable for us. That's how our API has been able to talk to the Docker database.

 When we've run commands that need to talk to the database, we've been running them like symfony console make:migration... because when we execute things through symfony, it adds the DATABASE_URL environment variable... and then runs the command.

 So, when we simply run php bin/phpunit... the real DATABASE_URL is missing. To fix that, run:

  symfony php bin/phpunit
 It's the same thing... except it lets symfony add the DATABASE_URL environment variable. And now... we see the dump again! Scroll to the top. Better! Now the error says:

  Database app_test does not exist.

 Test-Specific Database
 - Interesting. To understand what's happening, open config/packages/doctrine.yaml. Scroll down to a when@test section. This is cool: when we're in the test environment, there's a bit of config called dbname_suffix. Thanks to this, Doctrine will take our normal database name and add _test to it:

 44 lines  config/packages/doctrine.yaml
 when@test:
    doctrine:
        dbal:
            # "TEST_TOKEN" is typically set by ParaTest
            dbname_suffix: '_test%env(default::TEST_TOKEN)%'
 This next part is specific to a library called ParaTest where you can run tests in parallel. Since we're not using that, it's just an empty string and not something we need to worry about.

 Anyway, that's how we end up with an _test at the end of our database name. And we want that! We don't want our dev and test environments to use the same database because it gets annoying when they run over each other's data.

 By the way, if you're not using the symfony Binary and Docker setup... and you're configuring your database manually, be aware that in the test environment, the .env.local file is not read:

 7 lines  .env.test
 # define your env variables for the test env here
 KERNEL_CLASS='App\Kernel'
 APP_SECRET=''
 SYMFONY_DEPRECATIONS_HELPER=999999
 PANTHER_APP_ENV=panther
 PANTHER_ERROR_SCREENSHOT_DIR=./var/error-screenshots

 The test environment is special: it skips reading .env.local and only reads .env.test. You can also create a .env.local.test for env vars that are read in the test environment but that won't be committed to your repository.

---
## [petre-symfony/api-platform-3-part-2-security-for-you-symfonycasts-june-2023](https://github.com/petre-symfony/api-platform-3-part-2-security-for-you-symfonycasts-june-2023)@[17d19281d3...](https://github.com/petre-symfony/api-platform-3-part-2-security-for-you-symfonycasts-june-2023/commit/17d19281d3eae8ed327a185d3b1004ac51529088)
#### Friday 2023-06-09 19:54:42 by Petre Ro

14.5 The ResetDatabaseTrait
 - Ok, in the test environment, we're missing the database. We could easily fix this by running:

  symfony console doctrine:database:create --env=test

 But that's way too much work. Instead, add one more trait to our test class: use ResetDatabase

 This comes from Foundry: the library we've been using to create dummy fixtures via the factory classes. ResetDatabase is amazing. It automatically makes sure that the database is cleared before each test. So if you have two tests, your second test isn't going to mess up because of some data that the first test added.

 It's also going to create the database automatically for us. Check it out. Run

  symfony php bin/phpunit
 again and check out the dump. That's our response! It's our beautiful JSON-LD! We don't have any items in the collection yet, but it is working.

 And notice that, when we make this request, we are not sending an Accept header on the request. Remember, when we use the Swagger UI... it actually does send an Accept header that advertises that we want application/ld+json.

 We can add that to our test if we want. But if we pass nothing, we get JSON-LD back because that's the default format of our API.

 Next: let's properly finish this test, including seeding the database with data and learning about Browser's API assertions.

---
## [Rex9001/Rex_Tg](https://github.com/Rex9001/Rex_Tg)@[c67d6a22a4...](https://github.com/Rex9001/Rex_Tg/commit/c67d6a22a405f006a9d7a537dc35cecbdb65cfde)
#### Friday 2023-06-09 20:50:15 by Kyle Spier-Swenson

fix stupid error message in delay pre-game (#75824)

tabbing out during init after hitting the verb, while you wait for the
server to un-lockup and present you with the prompt, and coming back in,
noticing you were too late, and cancelling out of the time prompt, only
to get told the round had already started, was kinda fucking lame. I
know, thats why i fucking hit cancel you fucking robit.

also makes the proc more early return

---
## [Rex9001/Rex_Tg](https://github.com/Rex9001/Rex_Tg)@[d01b433ab1...](https://github.com/Rex9001/Rex_Tg/commit/d01b433ab12e7aa45416d42f9045f1135e545dae)
#### Friday 2023-06-09 20:50:15 by Sealed101

Fixes colossus possessor crystal cockroaches/animals not dumping the user's body upon death/gibbing (#75843)

## About The Pull Request
Hooks the stasis closet thingamajing into `COMSIG_LIVING_DEATH` instead
of checking the animal's stat on `process()`, which makes possessed
animals properly dump the stasis closet's contents upon death or gibbing
(which is death but cooler).
yeah uh this method is hilarious but it does protect the user's body
quite reliably at least lol

## Why It's Good For The Game
Fixes #75829
also probably makes cockroach death saner in some unreported way, this
`. = ..()` vs `..()` is above my non-existent paygrade but it keeps
popping up from time to time

## Changelog
:cl:
fix: gibbing colossus possessor crystal possessed animals will no longer
stick the user's body and their stuff into the shadow realm. the animals
will properly drop your corpse when killed or gibbed
/:cl:

---------

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>

---
## [chadlyalan/portfolio](https://github.com/chadlyalan/portfolio)@[4cf8389e14...](https://github.com/chadlyalan/portfolio/commit/4cf8389e149f007ae1d658601d865cddb627a987)
#### Friday 2023-06-09 21:18:31 by Chad

Chadlyalan/issue16 (#17)

* Create landing.dart

* extra landing (accident)

somehow i created a duplicate landing widget and put it in the widgets folder. I was quite confused, not sure how it happened.

* email and linkedin

i have fully functional linkedIn, and Email buttons now, as well as Github.
Linked in and Github are simple hyper links where as the gmail button opens up your default mail app, and starts to compose an email with the mailto address being my own.

I've also removed the social media icons from the side panel widget.

* rock-garden svg icon

* resume card and linkedIn

linkedIn and resume now have their own cards.

Resume doesn't work yet but LInkedIn works great.

* trying to get pdf going

cleaning things up a little bit

* pdf'ing almost

it doesn't work but we might have a pdf viewer kinda close

* cleaning up socials

I'm going to give up on showing the resume in a PDF for now. I don't think most people are going to want to see the pdf while they're at my website anyway so it will be a feature I add later once the website is up and polished. for now socials are good where they're at.

---
## [TeamLumi/Gamedata](https://github.com/TeamLumi/Gamedata)@[7443d10bba...](https://github.com/TeamLumi/Gamedata/commit/7443d10bbace2dcc9d26ad275107526aee0cd248)
#### Friday 2023-06-09 22:16:49 by DahniMae

Add files via upload

-All radar mons in all routes have been homogenized into one Radar mon, no changes noticeable to the player except for the following:
-Valley Windworks: Only Plusle shows up via Pokeradar
-Route 205 South: Only Minun shows up via Pokeradar
-Eterna Forest: Only Wurmples shows up via Pokeradar
-Route 212 South: Only Muk shows up via Pokeradar
-Trophy Garden: When Incense and Radar are both active, (and the Mon of the day for today and yesterday with Mr Backlot is NOT Eevee but other species) Eevee/Porgyon can still be found in day and morning slots, Cleffa at night slots

-all wild encounters have had their levels properly homogenized to be the highest for their route/slot type, fixing some bugged inverted minmax caps in the process
-fixed a bug with no incense mon being called for surfing in the Feebas pools in mt coronet, it should now be Galarian Slowpoke encountered via surfing with incense
-Mt Coronet 4th floor's fishing rod encounters had only 3 of their 5 slots in their tables, added the missing tables and properly set the missing mons to Dratini and Dragonair
-Internally fixed the formatting of certain routes just for cleanliness, no actual changes to species or percents or anything, just making sure everything is in its proper place/slots
-Ingame has Achieved full parity with Renegade Platinum docs, fixed various typos/wrong species in just one slot in certain routes
a Nidoking was meant to be Nidorino in r221
a Golem was meant to be Graveller in Victory Road 2F
a Weedle was meant to be Weepinbell in r224
a Chingling was meant to be Chatot in r213
A Shinx was meant to be a Luxio in r222
a Marill was meant to be Parasect in Great Marsh 3/4
an Ursaring was meant to be Swalot in Great Marsh 5/6

---
## [philIip/react-native](https://github.com/philIip/react-native)@[44aab9ce5c...](https://github.com/philIip/react-native/commit/44aab9ce5c7a9b237e5b2989b06157efd698c80d)
#### Friday 2023-06-09 22:39:10 by Phillip Pan

introduce build boilerplate for ios unit tests (#37811)

Summary:
Pull Request resolved: https://github.com/facebook/react-native/pull/37811

Changelog: [Internal]

i am looking to add ios unit tests to venice and this is the first unit test suite that will test native ios code in the new architecture afaik, so i wanted to open this up to discussion.

currently, all `XCTest` in `react-native-github` are coupled with the `RNTester` target. my main qualm with this is i am concerned that it won't scale well. currently we have only ~30ish tests but ultimately if we want a proper testing suite, surely this count will be in the hundreds and that won't be able to reasonably live in a single test target.

however, the trade is that this test will not show up in RNTester. i have added a unit test to RNTester before in D31949237, however the experience was extremely painful as i had to manually update the `project.pbxproj` to include my file, and i had to manually determine what hex value was the next one (for whatever reason, this doesn't increment at the endian...).

i am wondering if we can treat the current unit testing experience in RNTester as pretty much maintenance mode and start thinking of a improved version starting with something more modular like this.

Reviewed By: cipolleschi

Differential Revision: D46467229

fbshipit-source-id: feb99a53d7b56475d53d64dee7bbcb9202a52d7f

---
## [tyrant/blog](https://github.com/tyrant/blog)@[72b69c8fd9...](https://github.com/tyrant/blog/commit/72b69c8fd93b7cc295f3198f8120094e94b485e2)
#### Friday 2023-06-09 23:05:46 by Mikey Clarke

Baffling fixes baffle me: rebuilt admin routes

Beyond baffling :O All of a sudden, the Admin site disappeared. I could not log in. For the life of me I could swear I'd not changed a goddamn thing in any routes. No idea why it suddenly stopped working.

Anyhoo. I poked further, through the source codes of both the comfortable-mexican-sofa and comfy_blog gems ... and turns out most of the vanilla CMS stuff doesn't seem to be called directly from the comfy_blog code. That's all well and good, except for the fact that comfy_blog installation requires specifically removing the cms_admin routes from routes.rb. I have no idea how this had worked before.

So I tried to re-add it, and hit Bug Two. Looks like there's some old-style-vs-new-style ruby method params bug in calling comfy_route_cms_admin ... cms/routing.rb calls its :cms and :cms_admin routing generators via send(''), dynamically. Bah. I just called comfy_route_cms_admin directly from my routes file ... and all is gold again. Aah. Why did this happen in the first place? Why break now?

---
## [mentalisttraceur/home](https://github.com/mentalisttraceur/home)@[e7f77de4e7...](https://github.com/mentalisttraceur/home/commit/e7f77de4e77eeae81d12d0aac3437788caccdf96)
#### Friday 2023-06-09 23:31:40 by Alexander Kozhevnikov

.emacs: add trailing newline when creating files

Annoyingly, this also effects Eshell redirection
of program output to a file, since that actually
goes through Emacs machinery as if you created
the file the normal manual in-Emacs way. Mixed
feelings about this - in principle I hate it, in
practice I have often found it annoying when a
CLI command redirected to a file doesn't end in
a newline, so I guess we'll see if it annoys me
more than it helps. Either way, it's not super
obvious what a proper fix for this would look
like.

---
## [shivamidow/WebKit](https://github.com/shivamidow/WebKit)@[d6ae2528a9...](https://github.com/shivamidow/WebKit/commit/d6ae2528a9f3819005e08f9d5091ceff8b880fa8)
#### Friday 2023-06-09 23:59:55 by Dean Jackson

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

