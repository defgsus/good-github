## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-11-29](docs/good-messages/2023/2023-11-29.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 3,715,017 were push events containing 4,987,296 commit messages that amount to 309,266,750 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 85 messages:


## [KDr2/pytorch](https://github.com/KDr2/pytorch)@[ddf1cb7870...](https://github.com/KDr2/pytorch/commit/ddf1cb78705dcf79fe8c8df01f6f18ca4a218c55)
#### Wednesday 2023-11-29 00:03:50 by voznesenskym

AOTAutograd: handle set_(), detect metadata mutations that cancel out (#111554)

This should be enough to get @voznesenskym 's FSDP branch to plumb `set_()` through AOTAutograd properly and have everything properly no-op out. Main changes are:

(1) graph break on `aten::set_.source_Tensor_storage_offset` (we could support it but it isn't needed, seems safer to graph break)

(2) Functionalization: add a "proper" functionalization kernel for `aten::set_.source_Tensor`. The previous one we had was codegen'd and it was wrong (it would just clone() and call set_(), which does not do the right thing). I also manually mark on the `FunctionalTensorWrapper` when a given tensor has been mutated by a `set_()` call.

(3) AOTAutograd: I added a new field, `InputAliasInfo.mutates_storage_metadata`, so we can distinguish between "regular" metadata mutations, and metadata mutations due to `set_()` calls. This is mainly because at runtime, one requires calling `as_strided_()` to fix up metadata, while the other requires calling `set_()`.

(4) Made AOTAutograd's detection for metadata mutations / set_() mutations smarter and detect no-ops (if the storage and metadata are all the same).

I also killed `was_updated()` and `was_metadata_updated()`, and replaced them with (existing) `has_data_mutation() ` and (new) `has_data_mutation()`, which can more accurately distinguish between data-mutation vs. `set_()` calls vs. metadata-mutation

**This PR is still silently correct in one case though**, which I'd like to discuss more. In particular, this example:
```
def f(x):
    x_view = x.view(-1)
    x.set_(torch.ones(2))
    x_view.mul_(2)
    return
```

If you have an input that experiences both a data-mutation **and** a `x_old.set_(x_new)` call, there are two cases:

(a) the data mutation happened on the storage of `x_new`. This case should be handled automatically: if x_new is a graph intermediate then we will functionalize the mutation. If x_new is a different graph input, then we will perform the usual `copy_()` on that other graph input

(b) the data mutation happened on the storage of `x_old`. This is more of a pain to handle, and doesn't currently work. At runtime, the right thing to do is probably something like:
```

def functionalized_f(x):
    x_view = x.view(-1)
    # set_() desugars into a no-op; later usages of x will use x_output
    x_output = torch.ones(2)
    # functionalize the mutation on x_view
    x_view_updated = x.mul(2)
    x_updated = x_view_updated.view(x.shape)
    # x experienced TWO TYPES of mutations; a data mutation and a metatadata mutation
    # We need to return both updated tensors in our graph
    return x_updated, x_output
def runtime_wrapper(x):
    x_data_mutation_result, x_set_mutation_result = compiled_graph(x)
    # First, perform the data mutation on x's old storage
    x.copy_(x_data_mutation_result)
    # Then, swap out the storage of x with the new storage
    x.set_(x_set_mutation_result)
```

There are two things that make this difficult to do though:

(1) Functionalization: the functionalization rule for `set_()` will fully throw away the old `FunctionalStorageImpl` on the graph input. So if there are any mutations to that `FunctionalStorageImpl` later on in the graph, the current graph input won't know about it. Maybe we can have a given `FunctionalTensorWrapper` remember all previous storages that it had, and track mutations on all of them - although this feels pretty complicated.

(2) AOTAutograd now needs to know that we might have *two* graph outputs that correspond to a single "mutated input", which is annoying.

It's worth pointing out that this issue is probably extremely unlikely for anyone to run into - can we just detect it and error? This feels slightly easier than solving it, although not significantly easier. We would still need `FunctionalTensorWrapper` to keep track of mutations on any of its "previous" storages, so it can report this info back to AOTAutograd so we can raise an error.

Pull Request resolved: https://github.com/pytorch/pytorch/pull/111554
Approved by: https://github.com/ezyang
ghstack dependencies: #113926

---
## [RunKittenzRComing/tgstationprivate](https://github.com/RunKittenzRComing/tgstationprivate)@[10f194781d...](https://github.com/RunKittenzRComing/tgstationprivate/commit/10f194781db0a6b2e71d2769a07fca7d5960c21f)
#### Wednesday 2023-11-29 00:04:10 by Jacquerel

It is now possible to survive the Mansus  (#79131)

## About The Pull Request

Fixes #79113

There were a handful of bugs with the Mansus realm, this PR fixes them.

Firstly an most importantly, a refactor to damage handling touched the
"unholy determination" effect incorrectly (and I'm not even sure why?),
causing it to damage you instead of healing you most of the time. This
damage was not avoidable, so most people would be crit shortly after
entering the area and stay there.

Secondly, some of the heretic realms were unlit. A change to when
lazyloaded template atmosphere initialises means that the bonfires were
trying to light themselves with no air. Now they do this in
late_initialize instead, giving time for air to arrive.

Thirdly, the spooky hands were runtiming when passing through transit
tiles outside of the bounds of the heretic map. They shouldn't be
effected by shuttle drag anyway, so now they aren't.

Fourthly, I removed a row of empty space at the edge of the heretic map,
just because it annoyed me slightly.

Finally, while I was touching the heretic buff I made it heal you 1/4 as
much as it originally did. This is a balance change rather than a fix,
I'll atomise it out if it is controversial but I don't really expect it
to be.
In the future I would like to come back to these and make each realm
more specific to the path, because I think we could make these both more
exciting and more characterful.

## Why It's Good For The Game

Once it is working properly, the hand dodging minigame is actually
extremely forgiving, even if you don't move very much and get frequently
hit. This means some of those hits might actually add some tension.

## Changelog

:cl:
fix: You should be revived properly when entering the mansus realm
following a heretic sacrifice
fix: The buff which is supposed to heal you in the mansus realm will now
do that instead of unavoidably damaging you
balance: The mansus realm's healing buff heals for 25% as much as it did
before it was broken
/:cl:

---
## [theselfish/Bubberstation](https://github.com/theselfish/Bubberstation)@[b5e095e380...](https://github.com/theselfish/Bubberstation/commit/b5e095e380e729793628d254bb441f51ecdb046b)
#### Wednesday 2023-11-29 00:06:00 by Waterpig

[MODULAR] Refactors (hopefully) all borg modular changes into one module, adds raptor borgs (#777)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

Originally I was supposed to only add raptor borgs, but I am simply too
insane to let this shitcode slide.

Moves most if not all borg modular changes into one module folder
because by god these were spread out over like 8 files.
Improves modularity a bit by moving some borg related bubber edits on
skyrat into our modular files.
Adds raptor borgs

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

<!-- Please make sure to actually test your PRs. If you have not tested
your PR mention it. -->

## Why It's Good For The Game

Modularity good.
Code organizing good.

https://en.wikipedia.org/wiki/Technical_debt

Also new borg sprites are cool, I guess. See icondiff bot for those
<!-- Argue for the merits of your changes and how they benefit the game,
especially if they are controversial and/or far reaching. If you can't
actually explain WHY what you are doing will improve the game, then it
probably isn't good for the game in the first place. -->

## Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. You can read up on GBP
and it's effects on PRs in the tgstation guides for contributors. Please
note that maintainers freely reserve the right to remove and add tags
should they deem it appropriate. You can attempt to finagle the system
all you want, but it's best to shoot for clear communication right off
the bat. -->

:cl:
image: New borg sprites: Raptor
refactor: Moved most if not all bubber borg code into one modular folder
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

<!-- By opening a pull request. You have read and understood the
repository rules located on the main README.md on this project. -->

---
## [temporalio/temporal](https://github.com/temporalio/temporal)@[1be76e3583...](https://github.com/temporalio/temporal/commit/1be76e3583ef01ba9f79503e81fed5b7c9ab389c)
#### Wednesday 2023-11-29 00:30:10 by Tim Deeb-Swihart

Replace gogo/protobuf with google/protobuf (#5032)

**What changed?**

gogo/protobuf has been replaced with Google's official go compiler. 

**Why?**

gogo/protobuf has been deprecated for some time and the community is
moving on, building new tools (like vtproto) atop google's v2 compiler.

**How did you test it?**

`make test`

**Potential risks**

1. The change from embedded gogo-generated-structs to
google-generated-pointers-to-structs created a risk of nil pointer
exceptions. I've fixed all the ones our tests found but it's possible
there are more lurking in the new code.
2. This change may cause our performance to decrease. Certainly
encoding/deconding of proto objects will become slower, but the overuse
of pointers by the google compiler may negatively affect our overall
performance. We'll need to keep an eye on the GC stats
3. This breaks the HTTP API. We will not support [shortand payload
encoding](https://github.com/temporalio/proposals/blob/master/api/http-api.md#payload-formatting)
in this first pass; that will come once this initial work is in testing.

**Breaking changes for developers**

- `*time.Time` in proto structs will now be
[timestamppb.Timestamp](https://pkg.go.dev/google.golang.org/protobuf@v1.31.0/types/known/timestamppb#section-documentation)
- `*time.Duration` will now be
[durationpb.Duration](https://pkg.go.dev/google.golang.org/protobuf/types/known/durationpb)
- V2-generated structs embed locks, so you cannot dereference them. `go
vet` will scream at you about this. If you need a copy, use
`proto.Clone`.
- If the performance of this sucks then I will either update our code
generator to add shallow-clone methods or hand-roll the ones we need
- Proto enums will, when formatted to JSON, now be in
`SCREAMING_SNAKE_CASE` rather than `PascalCase`. We decided (in
discussion with the SDK team) that now was as good a time as any to rip
the bandage off.
- Proto objects, or objects embedding protos, cannot be compared using
`reflect.DeepEqual` or _anything_ that uses it. This includes `testify`
and `mock` equality testers!
- You will need to use the `common/testing/protorequire`,
`common/testing/protoassert`, or `common/testing/protomock` packages
instead. I've implemented proto-compatible matchers and assertions there
for all cases I've encountered
- If you need `reflect.DeepEqual` for any reason you can use
`go.temporal.io/api/temporalproto.DeepEqual` instead

Note that history loading will not be impacted by the JSON changes: I
rewrote history loading to dynamically fix incoming history JSON data
(like all our other sdks); you can find this code in [my fork of our go
API](https://github.com/tdeebswihart/temporal-api-go/blob/master/internal/temporalhistoryv1/load.go)
alongside its tests.

**🚨Sharp Edges Introduced🚨**

Beware `*timestamppb.Timestamp.AsTime()`. If you need to extract a time
value from a proto time (timestamppb) **always** make sure to check
whether it's nil first. When the proto object is `nil` `AsTime()` will
return a non-zero time at the proto epoch: UTC midnight on January 1,
1970.

I've made this mistake multiple times during this transition and each
time it's been a pain to debug

**Is hotfix candidate?**

No.

---
## [dsellers94/Unfracture](https://github.com/dsellers94/Unfracture)@[a4451905db...](https://github.com/dsellers94/Unfracture/commit/a4451905db9297f5dd07dadd68ab48673063bdb3)
#### Wednesday 2023-11-29 00:33:48 by dsellers94

Discovered and fixed a MAJOR bug with the pushing actor generation, any rotations that crossed the Z axis were scrambled and it was a pain in the ass to fix.
Finally ended up generating the quaternion between each separation vector and the average, seems to do the trick.
Now I just need to optimize a bit by only doing all this vector math if the relevant mesh datahas changed. Then I could call this thing feature complete and move on with my damn life.

---
## [FalloutFalcon/Shiptest](https://github.com/FalloutFalcon/Shiptest)@[caa19d2a6f...](https://github.com/FalloutFalcon/Shiptest/commit/caa19d2a6f8014c2d34663c7c63685921bc0218a)
#### Wednesday 2023-11-29 00:36:02 by GenericDM

Assorted cringe removal pt.whatever (#2534)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Removes more cringe I found laying around.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
/tg/ was on some WILD shit.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
del: removes tail club
del: removes all flavors of tail whip
del: removes lizardskin clothing
del: removes 'Genetic Purifier'
tweak: makes bunny ears desc not incredibly sexist
tweak: change up wording in magic mirror gender change
del: removes 'genuine' cat ears
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [TheVekter/tgstation](https://github.com/TheVekter/tgstation)@[bed92e193c...](https://github.com/TheVekter/tgstation/commit/bed92e193ce4a79824fd4fd30a900245dca870ae)
#### Wednesday 2023-11-29 00:39:35 by san7890

Further Prevention of Disposals Qdeletion (#79714)

## About The Pull Request

Fixes the consequences of #79629 - Verdict is still out on what the root
issue is

This has been an issue for the last two years and everything I go
bananas trying to get a consistent reproduction case to figure out the
root issue. After three session of picking, I think it's just a
consequence of certain thing in disposals code sleeping due to
`addtimer()` and whatnot so I'm just throwing in the towel and just
making it so we stop sending atoms to nullspace for no reason.

`target_turf` is typically always a present arg, but regardless we are
guaranteed to get a valid turf to send people to instead of the deleted
mob room. We still `stack_trace()` whenever this happens, so tracking
this issue doesn't change any more than the present status quo- we just
don't keep torturing mobs by sending them to the shadow realm.
## Why It's Good For The Game

One day we'll figure out why we keep getting `null` passed into
`forceMove()` like this but today is not that day. i know turfs
technically can't be deleted but it's just there as a safety since we
nullcheck anyways (which is the whole point of this fix). Let's just
stop screwing with players for the time being

also the code looks much better
## Changelog
:cl:
fix: Safeties in the code have been added to prevent things in disposals
going into nullspace whenever they get ejected from a pipe - you will
just magically spawn at the turf that you were meant to be flung
towards.
/:cl:

---
## [TheVekter/tgstation](https://github.com/TheVekter/tgstation)@[5175ae0637...](https://github.com/TheVekter/tgstation/commit/5175ae06374450b87324bb280c754e53880b7b16)
#### Wednesday 2023-11-29 00:39:35 by John Willard

TGUI Destructive Analyzer (#79572)

## About The Pull Request

I made this to help me move more towards my goals [laid out
here](https://hackmd.io/XLt5MoRvRxuhFbwtk4VAUA) which currently doesn't
have much interest.

This makes the Destructive Analyzer use a little neat TGUI menu instead
of its old HTML one. I also touch a lot of science stuff and a little
experimentor stuff, so let me explain a bit:
Old iterations of Science had different items that you can use to boost
nodes through deconstruction. This has been removed, and its only
feature is the auto-unlocking of nodes (that is; making them visible to
the R&D console). I thought that instead of keeping this deprecated code
around, I would rework it a little to make it clear what we actually use
it for (unhiding nodes).
All vars and procs that mentioned this have been renamed or reworked to
make more sense now.

Experimentor stuff shares a lot with the destructive analyzer, so I had
to mess with that a bit to keep its decayed corpse of deprecated code,
functional.

I also added context tips to the destructive analyzer, and added the
ability to AltClick to remove the inserted item. Removing items now also
plays a little sound because it was kinda lame.
Also, balloon alerts.

## Why It's Good For The Game

Moves a shitty machine to TGUI so it is slightly less shitty, now it's
more direct and compact with more player-feedback.
Helps me with a personal project and yea

### Video demonstration

I show off connecting the machine to R&D Servers, but I haven't changed
the behavior of that and the roundstart analyzers are connected to
servers by default.


https://github.com/tgstation/tgstation/assets/53777086/65295600-4fae-42d1-9bae-eccefe337a2b

## Changelog

:cl:
refactor: Destructive Analyzers now have a TGUI menu.
/:cl:

---
## [pjsoni/terminal](https://github.com/pjsoni/terminal)@[86fb9b4478...](https://github.com/pjsoni/terminal/commit/86fb9b44787accd09c5943a506e27eb4c8e573c0)
#### Wednesday 2023-11-29 00:45:19 by Dustin L. Howett

Add a magic incantation to tell the Store we support Server (#16306)

I find it somewhat silly that (1) this isn't documented anywhere and (2)
installing the "desktop experience" packages for Server doesn't
automatically add support for the `Windows.Desktop` platform...

Oh well.

I'm going to roll this one out via Preview first, because if the store
blows up on it I would rather it not be during Stable roll-out.

---
## [GenericDM/Shiptest](https://github.com/GenericDM/Shiptest)@[4d4aa72e33...](https://github.com/GenericDM/Shiptest/commit/4d4aa72e33bd20077d09d320f07a0a5608298cb2)
#### Wednesday 2023-11-29 00:51:49 by lizardqueenlexi

Removes "fat" status and everything related. (#2516)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

As the title says, eating too much no longer makes you "fat". You suffer
no slowdown or mood debuff from eating too much, and in general, the
game will not take every opportunity to make fun of you.

Notable removals/changes:
- The "fat sucker" machine is totally gone.
- Shady Slim's cigarettes have been removed (since they only existed to
interact with this mechanic).
- Lipoplasty surgery is gone.
- The nutrition setting of scanner gates is gone.

There are a couple of other removals too, like Gluttony's Wall, that I
think were already not in use on this codebase.

One thing I'm not completely satisfied with was the change to mint
toxin, which now does quite literally nothing. I don't think this is
especially a problem, it just makes its existence a bit vestigial.

Also includes an UpdatePaths script to delete all removed objects, just
in case.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game


![image](https://github.com/shiptest-ss13/Shiptest/assets/105025397/a1dd0981-94fc-4766-a34d-cce31a42b412)

Basically, removes some shitty "jokes" about fat people. It's an
extremely mean-spirited feature that serves no actual purpose, and
punishes you for clicking on a burger one time too many. It could
potentially be replaced later with a less mean-spirited "overeating"
mechanic, but I'm dubious as to whether that would be any fun either.

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
del: Removed the "fat" status - overeating now has no negative effects.
del: Removed lipoplasty surgery.
del: Removed the fat sucker machine.
tweak: Scanner gates no longer have a "nutrition" option available.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [842974287/pytorch](https://github.com/842974287/pytorch)@[5f504d1de7...](https://github.com/842974287/pytorch/commit/5f504d1de74a5189f93e65aa9283fc4607b8631c)
#### Wednesday 2023-11-29 00:59:52 by Pedro Caldeira

Check for boolean values as argument on pow function.  (#114133)

Hello everyone! 😄
Also @lezcano , nice to meet you! :)

Sorry if I miss anything, this is my first time around here. 🙃

This PR basically makes the same behaviour for cuda when using `torch.pow`. Basically Python considers True as 1 and False as 0. I just added this check into `pow` function. From what I understood, when I do `.equal` for `Scalar` that is boolean, I'm sure that types match so that won't cause more trouble.

I know that the issue suggest to disable this case but that could be a little more complicated, in my humble opinion. And that can create some compability problems too, I guess.

My argument is that code below is correct for native language, so I guess it does makes sense sending booleans as Scalar.

```
$ x = True
$ x + x
2
```

This was my first test:
```
Python 3.12.0 | packaged by Anaconda, Inc. | (main, Oct  2 2023, 17:29:18) [GCC 11.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import torch
>>> torch.pow(torch.tensor([1, 2], device='cuda'), True)
tensor([1, 2], device='cuda:0')
>>> torch.pow(torch.tensor([1, 2]), True)
tensor([1, 2])
>>> torch.pow(torch.tensor([1, 2]), False)
tensor([1, 1])
>>> torch.pow(torch.tensor([1, 2], device='cuda'), False)
tensor([1, 1], device='cuda:0')
```

I've run `test_torch.py` and got following results, so my guess is that I didn't break anything. I was just looking for a test that uses linear regression, as suggested.

```
Ran 1619 tests in 52.363s

OK (skipped=111)
[TORCH_VITAL] Dataloader.enabled		 True
[TORCH_VITAL] Dataloader.basic_unit_test		 TEST_VALUE_STRING
[TORCH_VITAL] CUDA.used		 true

```
(I can paste whole log, if necessary)

If this is a bad idea overall, dont worry about it. It's not a big deal, it's actually a two line change 😅  so can we talk of how do things in a different strategy.

For the record I've signed the agreement already. And I didn't run linter because it's not working 😞 . Looks like PyYaml 6.0 is broken and there's a 6.0.1 fix already but I have no idea how to update that 😅

Fixes #113198

Pull Request resolved: https://github.com/pytorch/pytorch/pull/114133
Approved by: https://github.com/lezcano

---
## [bend-n/rust](https://github.com/bend-n/rust)@[c3a6b376a4...](https://github.com/bend-n/rust/commit/c3a6b376a43e1ce10c6f17872fd48e99ee294388)
#### Wednesday 2023-11-29 01:13:02 by bors

Auto merge of #11800 - blyxyas:meow-meow, r=Centri3

Removing @Centri3 from reviewer rotation

Catherine decided that the best course of action would be to (maybe temporarily) remove her from the reviewer's rotation (but not unassign her from her current reviews). This PR does that. She'll always be welcomed back if she wants to review some more :heart:

> Alejandra González: [youremyfrennow.mp4](https://rust-lang.zulipchat.com/user_uploads/4715/7nE2W6cb8Q02gcK-vubvmsPM/youremyfrennow.mp4)
>
>Catherine, Fred (`@xFrednet` ) noticed that you aren't as active as in the summer, and proposed that maybe you preferred to be removed from the reviewer rotation. Don't worry, you aren't being taken out of the team, just wanted to know if you maybe preferred to not have those reviews pilling up (they can be pretty stressful to see).
>
>If you decide to step out of the reviewers rotation, you wouldn't be removed from the team, you just wouldn't have that responsability. Everyone takes break and that's fine, so yeah, if you want to not have to review PRs, let me know!
>
>So yeah, from weird teenager transfem to (probably weird) teenager transfem, the choice is in your hand.
>
>Alejandra González: meow meow ^•ﻌ•^
>
>Catherine (Centri3): Yeah that's probably best now, I'll still try with any I'm currently assigned to but I would prefer not to get anymore until then
>Catherine (Centri3): meow meow :3

changelog:none

r? `@Centri3`

---
## [capsaicinz/Skyrat-tg](https://github.com/capsaicinz/Skyrat-tg)@[58be66a653...](https://github.com/capsaicinz/Skyrat-tg/commit/58be66a6539c6e5b45588c8e1ed6c4b526e1d5ee)
#### Wednesday 2023-11-29 01:16:46 by SkyratBot

[MIRROR] Nukie Update Followup: Returns CQC to the previous price range, Core Gear kit for newbies, hat stabilizers for everyone [MDB IGNORE] (#24679)

* Nukie Update Followup: Returns CQC to the previous price range, Core Gear kit for newbies, hat stabilizers for everyone (#79232)

## About The Pull Request

Brings the CQC kit back down to the same price range of 14 TC (it's 1
more than before weapon kits). It feels like currently that CQC is
overpriced, even with the stealth box coming along with it, and by
comparison the energy sword and shield got a huge value increase by
combining the two. They're both melee styles and also equally difficult
play styles. It isn't really necessary to make one more expensive than
the other. Also now comes with syndicate smokes. It's a whatever change,
ops get these for free on the base.

Adds a core gear kit in the weapon category. This kit comes with a
doormag, a freedom implant, stimpack and c-4 charge. All of these are
items almost every nukie buys if they want to succeed, so let's inform
newer players by putting it RIGHT on top of the list. This isn't at any
discount, this is mostly to help inform players what items help make you
successful.

Hat stabilizers are now a part of every syndicate modsuit for FREE. It
comes built in, can't be removed, and has no complexity cost. Now
everyone can wear their wacky hats as they operate.

## Why It's Good For The Game

CQC felt like it got shafted waaay too hard with the weapon case
changes. Definitely don't believe that it is punching at the same weight
as many of the other high cost weapons. So we've dropped it down a
category. 14 TC is still a large upfront cost, even if it comes bundled
with a lot of goods.

Melbert gave me the idea of a core bundle kit to help newer players and
I was really taken with that. So I added it as part of this followup.

I want people to wear their hats goddamnit, and I didn't learn my
mistake with the tool parcels. So now everyone has hat stands on their
suits. WEAR THE SOMBRERO YOU **FUCK**.

### THIS IS NOW A THREAT.

## Changelog
:cl:
balance: Operatives can once again read about the basics of CQC at a
reasonable price of 14 TC.
qol: All Syndicate MODsuits come with the potent ability to wear hats on
their helmets FOR FREE. No longer does any operative need be shamed by
their bald helmet's unhatted state when they spot the captain, in their
MODsuit, wearing a hat on their helmet. The embarrassment has resulted
in more than a few operatives prematurely detonating their implants! BUT
NO LONGER! FASHION IS YOURS!
qol: There is now a Core Gear Box, containing a few essential pieces of
gear for success as an operative. This is right at the top of the
uplink, you can't miss it! Great for those operatives just starting out,
or operatives who need all their baseline equipment NOW.
/:cl:

* Nukie Update Followup: Returns CQC to the previous price range, Core Gear kit for newbies, hat stabilizers for everyone

---------

Co-authored-by: necromanceranne <40847847+necromanceranne@users.noreply.github.com>

---
## [capsaicinz/Skyrat-tg](https://github.com/capsaicinz/Skyrat-tg)@[0923ef2b26...](https://github.com/capsaicinz/Skyrat-tg/commit/0923ef2b264d7ee02b47c145249e90a69a49b554)
#### Wednesday 2023-11-29 01:16:46 by SkyratBot

[MIRROR] Basic Pirate NPCs [MDB IGNORE] (#24654)

* Basic Pirate NPCs (#79284)

## About The Pull Request

Converts hostile pirate NPCs to basic mobs - specifically, a subtype of
trooper. As their behavior is not meaningfully distinct from other
troopers, this conversion mostly just sticks them on the existing AI
behavior while keeping the rest the same.

Pirates do have one new thing going for them, though, to differentiate
them from other troopers. They use the new **plundering attacks**
component, which means that every time they land a melee attack, they
steal money from the bank account of whoever they hit. This requires the
target to be wearing an ID with a linked bank account, so it's not the
hardest thing in the world to hide your money from them - but it's still
something to be wary of! If killed, any mob with this component will
drop everything they've stolen in a convenient holochip.
## Why It's Good For The Game

Takes down 5 more simplemobs, and (I think) converts the last remaining
trooper-type enemy to be a basic trooper. (It's possible there's more
I've forgotten that could use the same AI, though.)

The money-stealing behavior is mostly good because I think it's funny,
but it also makes the pirates something a little distinct from "yet
another mob that runs at you and punches you until you die". They still
do that, but now there's a little twist! This can be placed on other
mobs too, if we want to make any other sorts of thieves or brigands.
## Changelog
:cl:
refactor: Pirate NPCs now use the basic mob framework. They'll be a
little smarter in combat, and if you're wearing your ID they'll siphon
your bank account with every melee attack! Beware! Please report any
bugs.
/:cl:

* Basic Pirate NPCs

* Modular paths

---------

Co-authored-by: lizardqueenlexi <105025397+lizardqueenlexi@users.noreply.github.com>
Co-authored-by: Giz <13398309+vinylspiders@users.noreply.github.com>

---
## [zzzmike/cmss13](https://github.com/zzzmike/cmss13)@[2011c229f9...](https://github.com/zzzmike/cmss13/commit/2011c229f9a37de8fa67a74d8e40974515724cde)
#### Wednesday 2023-11-29 01:19:35 by stalkerino

Readds skull facemask and facepaint (#5042)

# About the pull request
It readds two items that were removed in the past for no valid reason
(in my opinion), since it was a targeted PR against a specific player I
do not think it should've been removed.

# Explain why it's good for the game

It looks nice and fits the atmosphere, adding it will help players
customize their characters without being too loud.
The removal reason of "You'd get laughed at for wearing it IRL" is
invalid, a lot of military and law enforcement people wear skull masks,
punisher emblems and etcetra - this is especially evident in America
(We're UA)

https://discord.com/channels/150315577943130112/746325423289401395/1168350579307860078

https://discord.com/channels/150315577943130112/827156857566265375/1145494273568022588
https://files.catbox.moe/4o3ag1.png

https://discord.com/channels/150315577943130112/604397850675380234/1094357565317586964
-- the person who made it admitting it was targeted.


# Testing Photographs and Procedure
I don't think it needs testing
</details>


# Changelog
:cl: stalkerino
add: readds skull facepaint and skull balaclava (blue and black)
/:cl:

---
## [f13babylon/f13babylon](https://github.com/f13babylon/f13babylon)@[3c052bcd6d...](https://github.com/f13babylon/f13babylon/commit/3c052bcd6d3ff02680c3fe1f15151549154eb162)
#### Wednesday 2023-11-29 01:21:13 by Mazzinsanity

Main Fallout13 Medicine Rework (#113)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

<!-- NOTE: This format is NOT REQUIRED for things like runtime fixes,
code fixes and optimizations. In those instances you should try to give
a description of what is being fixed or optimized but are not required
to fill out the complete changelog. -->
<!-- Adjusting things like armor or weapon values for balance, while
they may be 'fixes' in their own way, are not considered code fixes as
described above and require the use of the Pull Request format below.-->


## About The Pull Request
This PR aims to bring a number of changes to the way the main Fallout13
medicines function.

Stims remain the vanilla videogame healing item they were, stronger than
tribal medicine at healing brute and burn damage, but lacking in
specialization. On the other hand, tribal medicine has been given a new
breath of life in the form of excelling in certain damage types and
increased healing from wounds.

Activation delays for certain healing items have been changed:
- Hydra/Med-X/Psycho/Turbo - 1 second on yourself / 3 seconds on others
- All forms of gauze/sutures/mesh/ointment - 3 seconds for yourself / 1
second on others

Using the stimpak as a base, here are the healing rates for brute/burn
healing for the healing items:
1. Super stimpak - 225% of base stimpak strength
2. Imitation super stimpak - 188% of base stimpak strength (75% of super
stimpak strength)
3. Bitter drink -180% of base stimpak strength for tribals / 133% for
non-tribals
4. Healing poultice - 115% of base stimpak strength for tribals / 87.5%
for non-tribals
5. Imitation stimpak - 75% of base stimpak strength
6. Healing powder - 75% of base stimpak strength for tribals / 55% for
non-tribals

All medicine now heals burn damage at 75% of its healing power for brute
damage.

Powder/poultice/bitters/hydra will not heal when any stimpak fluid
variant is in the system. Stimpak fluid will not heal when
powder/poultice/bitters are the system.

Only one medicine is able to heal at a time. This medicine must be the
weakest one currently in the system:
- For example, if super stim fluid is present in the body, and regular
stim fluid is introduced, then the super stim fluid will stop healing,
while the regular stim fluid heals.
- If imitation stim fluid is added, then regular stim fluid stops
healing, and only imitation stim fluid can heal.
- If at any point powder/poultice/bitters are added, no medicine will
heal.
- The same logic follows for powder/poultice/bitters.

All stimpaks have lost the ability to additionally heal bodyparts with
each wound applied to that bodypart. The logic behind this property has
been reworked and moved to tribal medicine.

All stimpaks have retained their ability to clot active pierce/slash
wounds, reducing their bleed rates.

All medicine has lost its crit stabilizing properties.

Bitter drink no longer heals radiation and has reduced toxin and oxyloss
healing rates.

Healing poultice now excels at healing radiation and toxin damage, as
strong as the super stimpak brute healing rate. Healing powder now
excels at healing oxyloss damage, as stong as the super stimpak brute
healing rate.

The overdose effects for all main healing medicines have had their
damage values tweaked and additional drawbacks added.

Using stims as Legion now causes serious side-effects, including
vomiting, confusion, dizzyness and jitteriness. Using
Med-X/Psycho/Buffout/Jet/Turbo as Legion/NCR/BoS/Enclave now also causes
these side-ffects. As such, Psycho and Turbo have been removed from
Enclave loadouts.

2 new negative quirks are now available for selection: Stim Intolerance
and Straight Edge:
- Stim Intolerance makes you vomit, causes dizziness, jitteriness and
confusion whenever any variant of stim fluid enters your body.
- Straight Edge makes you have the same effects but with Fallout chems
like Psycho/Med-X etc.

New positive quirk available for selection: Herbal Affinity:
- Grants bonus healing from tribal medicine and removes the negative
side-effects

Roles that start with these quirks already allocated to them
(NCR/Legion/BoS/Enclave) cannot select these quirks for free points.

Small miscellaneous tweaks and fixes, such as crafting time changes for
medicine, are present as well.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
The current roster of Fallout13 medicine is somewhat unbalanced and
needs a little love. This aims to do that by making superstims act as
vanilla jack-of-all-trades healing items, while making the tribal
medicines specialize in certain damage types to fill the gaps left by
their inability to use chem machines while also making them grow
stronger as the user gains more wounds, taking into account the low
wound armor and hit-and-run, all-or-nothing gameplay that Tribal and
Legion roles have.

The side-effects changes for Med-X/Psycho/Turbo/Buffout were made to
counteract powergaming and circumvent factions breaking their lore in
order to gain an upper hand in a fight.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Pre-Merge Checklist
<!-- Don't bother filling these in while creating your Pull Request,
just click the checkboxes after the Pull Request is opened and you are
redirected to the page. -->
- [x] You tested this on a local server.
- [x] This code did not runtime during testing.
- [x] You documented all of your changes.
<!-- Neither the compiler nor workflow checks are perfect at detecting
runtimes and errors. It is important to test your code/feature/fix
locally. -->


## Changelog
<!-- This is mostly optional for small Pull Requests, but if you value
being credited for your work in-game be sure to fill it out. To opt-out,
remove everything below including the start and end :cl: brackets. -->

<!-- If your Pull Request includes a minor single line variable edit,
probably do not fill out this changelog. -->
<!-- However, if your pull request includes massive or immediately
noticeable changes, briefly describe those changes in some way in this
changelog. -->

:cl:
add: Added side-effects for the 4 major factions upon Fallout chem use
add: Added side-effects for Legion upon stim use
add: Added 2 new negative quirks - Stim Intolerance and Straight Edge
tweak: Tweaked medicine crafting times
tweak: Tweaked time delays on medicine application
balance: Rebalanced the main Fallout13 healing chemicals
fix: Fixed incorrect poultice x50 batch crafting requirements
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: Yawet330 <65188584+Yawet330@users.noreply.github.com>

---
## [Ethan-Raborn-CSC/Battleship-AI](https://github.com/Ethan-Raborn-CSC/Battleship-AI)@[ec731da212...](https://github.com/Ethan-Raborn-CSC/Battleship-AI/commit/ec731da212d4286f2f6a43f9eb04b0b1ed95f6e3)
#### Wednesday 2023-11-29 01:37:41 by Ethan-Raborn-CSC

Added Readme

I hate readmes. If you need more info, just contact me for god's sake. And if someone adds to this readme, I claim no responsibility for what they write.

---
## [Zoxc/rust](https://github.com/Zoxc/rust)@[a660516334...](https://github.com/Zoxc/rust/commit/a6605163346d7680502d8e2c1e5aaf1dc3229e41)
#### Wednesday 2023-11-29 01:39:54 by Matthias Krüger

Rollup merge of #117596 - thomcc:core_macro_diag_items, r=Nilstrieb

Add diagnostic items for a few of core's builtin macros

Specifically, `env`, `option_env`, and `include`. There are a number of reasons why people might want to look at these in lints (For example, to ensure that things behave consistently, detect things that might make builds less reproducible, etc).

Concretely, in PL/Rust (well, `plrustc`) we have lints that forbid these (which I'd like to [add to clippy as restriction lints](https://rust-lang.zulipchat.com/#narrow/stream/257328-clippy/topic/Landing.20a.20flotilla.20of.20lints.3F) eventually), and `dylint` also has [lints that look for `env!`/`option_env!`](https://github.com/trailofbits/dylint/blob/109a07e9f27a9651ef33b6677ccaddd21466e97a/examples/general/env_cargo_path/src/lib.rs) (although perhaps not `include`), which would benefit from this.

My experience is that it's pretty annoying to (robustly) check uses of builtin macros without these IME, although that's perhaps just my own fault (e.g. I could be doing it wrong).

At `@Nilstrieb's` suggestion, I've added a comment that explains why these are here, even though they are not used in the compiler. This is mostly to discourage removal, although it's not a big deal if it happens (I'm certainly not suggesting the presence of these be in any way stable).

---

In theory this is a library PR (in that it's in library/core), but I'm going to roll compiler because the existence of this or not is much more likely something they care about rather than libs. Hopefully nobody objects to this.

r? compiler

---
## [izzygomez/mac-setup-scripts](https://github.com/izzygomez/mac-setup-scripts)@[417bed7dcd...](https://github.com/izzygomez/mac-setup-scripts/commit/417bed7dcdd97b4818a5e4ee8d9c90b9e6126193)
#### Wednesday 2023-11-29 01:41:40 by Izzy Gomez

remove `beardedspice` cask; see below for deets

there is an annoying bug (feature?!) where if beardedspice is active & spotify
is open on my desktop, when my laptop goes to sleep (or, to be more precise,
within ~1.5 minute window after laptop sleeps) the Spotify content is paused.
this was the source of the "phantom" pauses that I was experiencing with Spotify,
even when I was playing it on a different device (e.g. phone). so I'm removing
this cask. IIRC I initially installed this in order to force stop the play/pause
button on my macbook from opening the iTunes/Music app; I remember this being
the cleanest solution from my research back then. but interestingly even after
uninstalling this cask, I still no longer see the button-opens-app behavior, so
I wonder why this is the case. anyways, for now, just going to remove to stop
stupid bug described above, & can reconsider reinstalling if undesired keyboard
behavior comes back.

---
## [HeresKozmos/cmss13](https://github.com/HeresKozmos/cmss13)@[f367771f57...](https://github.com/HeresKozmos/cmss13/commit/f367771f5799b87257d92cb79db71bcd85b62f75)
#### Wednesday 2023-11-29 01:58:35 by Birdtalon

Eggsac carrier revival (#4716)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

[Forum Thread](https://forum.cm-ss13.com/t/eggsac-carrier-revival/4711)

# About the pull request

The concept of this PR is to find a middle ground between the current
eggsac carrier and the pre #4459 eggsac carrier.

This PR will make the following changes. (From this point "normal weeds"
can be substituted for "off hive weeds" Placing eggs on hive weeds is
**unchanged**.)

- Eggsac carrier can once again place eggs on normal weeds.
- Eggsac carrier can only place 4 eggs at once on normal weeds.
- If the Eggsac places more than 4 eggs on normal weeds, their oldest
placed egg will die. No hugger release.
- Eggs placed on normal weeds have a maximum lifetime of 5 MINUTES after
which they will die. No hugger release.
- Eggs placed on normal weeds have a 1 MINUTE life whilst the carrier is
further than 14 tiles away from them.
- If the carrier dies, all of their sustained eggs die.

# Explain why it's good for the game

Eggsac carrier at the moment is in a bit of a poor place and has gone
from being very strong to quite poor. Considering the limitation of
having to place only on hive weeds.
The majority of feedback I read against eggsac carrier was with the
quantity of eggs able to be placed, as well as the locations they can be
placed in, all across the map and with impunity.

This PR aims to address those concerns to make the eggsac both less
infuriating to play against while still being satisfying to play as a
frontline support or as a stealthy trapper.

Eggs can no longer be placed all over the map because of the 4 egg limit
off weeds, so the carrier has to think where they want to impact the
map. The carrier also has to stay within a reasonable distance to where
they are impacting with their eggs which localises their impact to their
immediate play area. The carrier also has to be more reactive to current
events as they cannot place an egg which then becomes useful 30 minutes
later.

Killing the carrier also has a small reward as in addition to removing a
xeno from the game, the eggs they are sustaining are cleared. If a
carrier is supporting the front and dies, the marines don't then have to
clear X number of eggs AFTER the kill.

# Testing Photographs and Procedure

1. Spawn as egg carrier.
2. Plant egg on normal weeds.
3. Move 15+ tiles away.
4. Wait 1 minute
5. OR Wait 5 minutes within 14 tiles.
6. Kill the carrier.

The 5 minute lifetime of the eggs will also clear the eggs in the case
that the carrier is admin deleted, or some other weird stuff happens
which doesn't result in a death. This will also catch carriers
de-evolving

<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
label your changes in the changelog. Please note that maintainers freely
reserve the right to remove and add tags should they deem it
appropriate. You can attempt to finagle the system all you want, but
it's best to shoot for clear communication right off the bat. -->
<!-- If you add a name after the ':cl', that name will be used in the
changelog. You must add your CKEY after the CL if your GitHub name
doesn't match. Maintainers freely reserve the right to remove and add
tags should they deem it appropriate. -->

:cl:
add: Eggsac carrier can now place eggs on normal weeds to a maximum of 4
eggs.
add: Eggsac carrier eggs on normal weeds have an expiry date.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [HeresKozmos/cmss13](https://github.com/HeresKozmos/cmss13)@[a955791561...](https://github.com/HeresKozmos/cmss13/commit/a955791561d5aeab0ff0640923fe1192ad377830)
#### Wednesday 2023-11-29 01:58:35 by fira

/tg/ Status effects part 1 - fluid status updates (#4828)

![image](https://github.com/cmss13-devs/cmss13/assets/604624/38cdd1a0-e13c-4d69-b893-49cea2a8113f)
CM Dev figured it out 9 years ago and nobody listened and kept tacking
illogical conditions

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

Builds on previous "prelude" PRs in the following steps:
 * Ports /tg/ body_position and mobility_flags
* Fixes some interaction requirements to use stun/mobility rather than
lying/knocked_down
* Ports /tg/ granular status updates, ie. status propagating through
handlers and signals. This includes changes to resting, buckling, and
lying down human transforms.
 * Wires our status effect system to it directly
* Removes `update_canmove` from existence completely as not needed
anymore

Because step 1 and 2 require updating all the gameplay logic using them,
this PR modifies a lot of files.

Part 2 will move the actual status effects to /tg/ status_effects,
resolving our timing problems.

# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
<details>
<summary>Testing Checklist!</summary>

- [x] Basic Movement
- [x] Admin Freeze Prevents Movement
- [x] Resting, Getting Up
- [x] Xenos change icon when resting
- [x] Buckling, including bed rotation and propelled chairs
- [x] Crawling Movement including sprite movement
- [x] Aggressive, Choke Grabbing, and Fireman carry apply rotation
- [x] Xeno Pounce and Abduct properly freeze both target and caster 
- [x] Double dropship seats density update
- [x] Explosive knockout on Humans
- [x] Xeno burrow density and movement interactions
- [x] Xeno nest interactions, specifically confirm density changes work
- [ ] Xeno nest bullet hits doublecheck with snowflake trait check
- [x] Combat Xeno ~~knockouts~~ knockdown and sprite updates
- [x] ~~Sleeping, Waking up, Usage of items while sleeping~~ - Can't
really test this we have almost no sleep code
- [x] Arbitrary buckling rotations
- [x] Admin-set transforms work with buckling/lying
- [ ] All the broken objects that will only be found out in Testmerge

</details>


# Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
label your changes in the changelog. Please note that maintainers freely
reserve the right to remove and add tags should they deem it
appropriate. You can attempt to finagle the system all you want, but
it's best to shoot for clear communication right off the bat. -->
<!-- If you add a name after the ':cl', that name will be used in the
changelog. You must add your CKEY after the CL if your GitHub name
doesn't match. Maintainers freely reserve the right to remove and add
tags should they deem it appropriate. -->

:cl:
code: Ported basic /tg/ Status Backend.
add: Human transform changes such as lying down, knock down, buckling,
are now animated.
fix: Some statuses will now take effect immediately instead of waiting
for a life tick, notably Resting.
balance: Many interaction requirements were changed to eg. fail upon
stuns rather than if lying down.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [ReturnToZender/ReturnsBubber](https://github.com/ReturnToZender/ReturnsBubber)@[52f69b96ee...](https://github.com/ReturnToZender/ReturnsBubber/commit/52f69b96eebfbe14a763ae9c5a8dd7ef156c4582)
#### Wednesday 2023-11-29 02:07:55 by The-Sun-In-Splendour

mid-round salt pr about EMP mold because being repeatedly shocked 500 times in a row unless you get charcoal (now called syniver or whatever fuck new chems) is not what I consider to be fun gameplay (#755)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
emp mold mosquitoes no longer put you in shock stunlock hell because
that shit is not funny
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

<!-- Please make sure to actually test your PRs. If you have not tested
your PR mention it. -->

## Why It's Good For The Game
it made me mad and this is a salt pr

![image](https://github.com/Bubberstation/Bubberstation/assets/70348069/b5002caa-d401-478a-9d48-fbc772c05b3e)

<!-- Argue for the merits of your changes and how they benefit the game,
especially if they are controversial and/or far reaching. If you can't
actually explain WHY what you are doing will improve the game, then it
probably isn't good for the game in the first place. -->

## Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. You can read up on GBP
and it's effects on PRs in the tgstation guides for contributors. Please
note that maintainers freely reserve the right to remove and add tags
should they deem it appropriate. You can attempt to finagle the system
all you want, but it's best to shoot for clear communication right off
the bat. -->

:cl:
balance: emp mold mosquitoes no longer shock you all the time until you
have a stroke irl over the annoyance
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

<!-- By opening a pull request. You have read and understood the
repository rules located on the main README.md on this project. -->

---
## [mldriscoll/AOAB](https://github.com/mldriscoll/AOAB)@[d71046aa55...](https://github.com/mldriscoll/AOAB/commit/d71046aa5517b18b07122d0427029a7516373602)
#### Wednesday 2023-11-29 02:29:27 by mldriscoll

Series.json Update
8th Loop for the Win 1-2
Late Start Tamer 9
Bibliophile Princess Manga 7
Butareba 1-2
Fake It to Break It 1-2
Full Clearing Another World 11
Escape from Princess Lessons Manga 1-2
Capped at Level 1 3
Karate Master 4
Making Magic 6
Private Tutor 11
One Step at a Time 4
Brilliant Healer 1-2
Zero Subjects 1-2
Zero Subjects Blue Dias and Alna 3
Invincible Little Lady (Manga) 1-2
Demon King Academy 6
Skull Dragon's PRecious Daughter 4
You Were Experienced 1-2

---
## [eedwards4/disk_scheduler](https://github.com/eedwards4/disk_scheduler)@[dfbc190b8e...](https://github.com/eedwards4/disk_scheduler/commit/dfbc190b8ec99d8917f7d54d4c010488be05222f)
#### Wednesday 2023-11-29 02:55:36 by Ethan Edwards

Starting conversion to linked-lists. I hate my life kill me please

---
## [sjp38/linux](https://github.com/sjp38/linux)@[28e39425f0...](https://github.com/sjp38/linux/commit/28e39425f0b4c5ae42c345a86108d23223d503d7)
#### Wednesday 2023-11-29 03:04:58 by SeongJae Park

==== DAMOS: Introduce Aim-Oriented Feedback-driven Quota Auto Tuning ====

Subject: [PATCH] mm/damon: Let users feed and tame DAMOS

Introduce a new way for tuning DAMOS, namely aim-oriented
feedback-driven aggressiveness auto tuning.  It allows users repeatedly
tell DAMOS how far it is from the users' aiming goal.  Based on the
feedback, DAMOS self-adjusts its aggressiveness to meet the goal.

DAMOS Control Difficulty
========================

DAMOS helps users easily implementing access pattern aware system
operations.  However, controlling DAMOS in wild is not that easy.

The basic way for DAMOS control is specifying the target access pattern.
In this approach, the user is assumed to well understanding the access
pattern and the characteristic of the system and the workloads.  Though
some good tools including DAMON can help that, it requires time and
resource depending on the complexity and the dynamicity of the system
and workloads.  After all, the access pattern consists of three ranges,
namely access rate, age, and size of the regions.  It means users need
to tune six parameters.  Tuning six parameters itself is not simple.

To let users at least avoid the worst case, DAMOS allows users to set
the upper-limit of the schemes's aggressiveness, namely DAMOS quota.
DAMOS further provides its best-effort under the limit by prioritizing
regions based on the access pattern of the regions.  For example, users
can ask DAMOS to page out up to 100 MiB of memory regions per second.
Then DAMOS pages out regions that not accessed longer time (colder)
first under the limit.  This allows users to set access pattern bit
naively, and focus on only the one parameter, the quota.  In other
words, the number of parameters to tune with special care can be reduced
from six to one.

Still, however, the optimum value for the quota depends on the system
and the workloads' characteristics, so not that simple.  The number of
parameters to tune can also increase again if the user needs to run
multiple schemes.

Aim-oriented Feedback-driven DAMOS Quota Auto Tuning
====================================================

Most users would start using DAMOS since there is something they want to
achieve using DAMOS.  Asking users to inform DAMOS their aim of the use,
and how close DAMOS is achieving it could be a reasonable request.
Having measurable metrics and the target values of the metric that
represents such information (e.g., SLO) is indeed not rare in the
industry.  Then, DAMOS could tune its aggressiveness, namely the quota,
on its own, based on the users' feedback and the current aggressiveness.
This patchset implements the idea.

Implementation
--------------

The implementation asks users to represent the feedback with score
numbers.  The scores could be anything including user-space specific
metrics like latency/throughput of special user-space workloads, and
system metrics like free memory ratio, memory pressure stall time (PSI),
and/or active to inactive memory ratio.

The feedback scroes and the aggressiveness of the given DAMOS scheme are
assumed to be positively proportional, though.  Selecting metrics of the
assumption is the users' responsibility.

The core logic implementation uses below simple feedback loop algorithm.
It gets next aggressiveness of the scheme from the current
aggressiveness and the feedback (target_score and current_score) for the
current aggressiveness.  It calculates the compensation for next
aggressiveness as a proportion of current aggressiveness and distance to
the target score.  As a result, it fastly goes close to the goal using
big steps when its far from the goal, but avoid making mistakes using
small steps whne its near to the goal.

    f(n) = max(1, f(n - 1) * ((target_score - current_score) / target_score + 1))

Example Use Cases
-----------------

If users want to reduce memory footprint of the system as much as
possible as long as the time spent for handling the resulting memory
pressure is within a threshold, they could use DAMOS scheme that
reclaims cold memory regions while setting the memory pressure stall
time of the threshold as the goal, and repeatedly provide the current
memory pressure stall time ratio as the feedback.

If users want to avoid reclamation when there is no memory pressure but
want the active/inactive LRU lists well balanced to reduce the
performance impact due to possible memory pressure, they could use two
schemes.  The first one would set to locate hot pages in active LRU
list, aiming specific active-to-inactive LRU list size ratio, say, 70%.
The second one would set to locate cold pages in inactive LRU list,
aiming specific inactive-to-active LRU list size ratio, say, 30%.  Then,
DAMOS will balance the two schemes based on the goal and feedback.  As a
result, in this example, DAMOS will make active LRU list to have hottest
70% of memory in use, and therefore protect the 70% hottest memory from
future memory pressure.

Evaluation: PSI-based proactive reclamation auto tuning
-------------------------------------------------------

To show if the implementation works as expected, we prepare four
different system configurations on AWS i3.metal instances.  The first
setup (original) runs the workload without any DAMOS scheme.  The second
setup (not-tuned) runs the workload with virtual address space-based
proactive reclamation scheme that pages out memory regions that not
accessed for five seconds or more.  The third setup (offline-tuned) runs
the same proactive reclamation DAMOS scheme, but after making it tuned
for each workload in offline, using our previous user-space driven
automatic tuning approach, namely DAMOOS[1].  The fourth and final setup
(online-tuned) runs the scheme that same to that of 'not-tuned' setup,
but making DAMOS to do online auto-tuning, aiming 0.5% of 'some' memory
pressure stall time (PSI) per 10 seconds.

For each setup, we run realistic workloads from PARSEC3 and SPLASH-2X
benchmark suites.  For each run, we measure RSS and runtime of the
workload, and 'some' memory pressure stall time (PSI) of the system.
We repeat the runs five times and use averaged measurements.

For simple comparison of the results, we normalize the measurements to
those of 'original'.  In case of the PSI, though, the measurement for
'original' was zero, so we normalize the value to that of 'not-tuned'
scheme's result.  The normalized results are shown below.

            Not-tuned         Offline-tuned     Online-tuned
    RSS     0.622688178226118 0.787950678944904 0.740093483278979
    runtime 1.11767826657912  1.0564674983585   1.0910833880499
    PSI     1                 0.727521443794069 0.308498846350299

The 'not-tuned' scheme acheives about 38.7% memory saving but incur about
11.7% runtime slowdown.  The offline-tuned scheme achieves about 22.2%
memory saving with about 5.5% runtiem slowdown.  It also achieves about
28.2% memory pressure stall time saving.  The online-tuned scheme
achieves about 26% memory saving with about 9.1% runtime slowdown.  It
also achieves about 69.1% memory pressure stall time saving.  We repeat
this test multiple times, and get consistent results.

Apparently the aggressiveness of 'online-tuned' setup is somewhere
between those of 'not-tuned' and 'offline-tuned' setup, since its memory
saving and runtime overhead are between those of the other two setups.
The difference in memory saving and performance degradation are not
significant, though.  Actually we set the memory pressure stall time
goal aiming this middle aggressiveness.  However, it shows significant
saving of the memory pressure stall time, which was the goal of the
auto-tuning, among the three variants.  Hence, we conclude the automatic
tuning is working as expected.

Please note that the setup may not appropriate for production
environment.  In production, less memory pressure stall time would be
more appropriate to be set as a goal.

The test code is also available[2], so you could reproduce it on your
system and workloads.

[1] https://www.amazon.science/publications/daos-data-access-aware-operating-system
[2] https://github.com/damonitor/damon-tests/commit/3f884e61193f0166b8724554b6d06b0c449a712d

Patches Sequence
================

The first four patches implement the core logic and user interfaces for
the auto tuning.  The first patch implements the core logic for the auto
tuning, and the API for DAMOS users in the kernel space.  The second
patch implements basic file operations of DAMON sysfs directories and
files that will be used for setting the goals and providing the
feedback.  The third patch connects the quota goals files inputs to the
DAMOS core logic.  Finally the fourth patch implements a dedicated DAMOS
sysfs command for efficiently committing the quota goals feedback.

Two patches for simple test of the logic and interfaces follow.  The
fifth patch implements the core logic unit test.  The sixth patch
implements a selftest for the DAMON Sysfs interface for the goals.

Finally, two patches for documentation follows.  The seventh patch
documents the design of the feature.  The final eighth patch updates the
usage document for the features.

Signed-off-by: SeongJae Park <sj@kernel.org>

---
## [rootfan/android_kernel_moto_shamu](https://github.com/rootfan/android_kernel_moto_shamu)@[f3edfea2d9...](https://github.com/rootfan/android_kernel_moto_shamu/commit/f3edfea2d9c0d889554efba673dc79c4d65267bb)
#### Wednesday 2023-11-29 03:26:22 by Maciej Żenczykowski

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
Signed-off-by: Daniel Borkmann <daniel@iogearbox.net>
Cc: Dongseok Yi <dseok.yi@samsung.com>
Cc: Willem de Bruijn <willemb@google.com>
Link: https://lore.kernel.org/bpf/CANP3RGfjLikQ6dg=YpBU0OeHvyv7JOki7CyOUS9modaXAi-9vQ@mail.gmail.com
Link: https://lore.kernel.org/bpf/20210617000953.2787453-2-zenczykowski@gmail.com

(cherry picked from commit 364745fbe981a4370f50274475da4675661104df https://git.kernel.org/pub/scm/linux/kernel/git/bpf/bpf-next.git/commit/?id=364745fbe981a4370f50274475da4675661104df )
Test: builds, TreeHugger
Bug: 158835517
Bug: 188690383
Signed-off-by: Maciej Żenczykowski <maze@google.com>
Change-Id: I0ef3174cbd3caaa42d5779334a9c0bfdc9ab81f5

---
## [edenlewis/Parent-Connect](https://github.com/edenlewis/Parent-Connect)@[8af1f77e34...](https://github.com/edenlewis/Parent-Connect/commit/8af1f77e34555106c3484de793dffba2a059ee8d)
#### Wednesday 2023-11-29 04:02:18 by uraniumrainbow

Delete server/node_modules directory

Call me Ishmael. Some years ago—never mind how long precisely—having little or no money in my purse, and nothing particular to interest me on shore, I thought I would sail about a little and see the watery part of the world. It is a way I have of driving off the spleen and regulating the circulation. Whenever I find myself growing grim about the mouth; whenever it is a damp, drizzly November in my soul; whenever I find myself involuntarily pausing before coffin warehouses, and bringing up the rear of every funeral I meet; and especially whenever my hypos get such an upper hand of me, that it requires a strong moral principle to prevent me from deliberately stepping into the street, and methodically knocking people’s hats off—then, I account it high time to get to sea as soon as I can. This is my substitute for pistol and ball. With a philosophical flourish Cato throws himself upon his sword; I quietly take to the ship. There is nothing surprising in this. If they but knew it, almost all men in their degree, some time or other, cherish very nearly the same feelings towards the ocean with me.

There now is your insular city of the Manhattoes, belted round by wharves as Indian isles by coral reefs—commerce surrounds it with her surf. Right and left, the streets take you waterward. Its extreme downtown is the battery, where that noble mole is washed by waves, and cooled by breezes, which a few hours previous were out of sight of land. Look at the crowds of water-gazers there.

Circumambulate the city of a dreamy Sabbath afternoon. Go from Corlears Hook to Coenties Slip, and from thence, by Whitehall, northward. What do you see?—Posted like silent sentinels all around the town, stand thousands upon thousands of mortal men fixed in ocean reveries. Some leaning against the spiles; some seated upon the pier-heads; some looking over the bulwarks of ships from China; some high aloft in the rigging, as if striving to get a still better seaward peep. But these are all landsmen; of week days pent up in lath and plaster—tied to counters, nailed to benches, clinched to desks. How then is this? Are the green fields gone? What do they here?

But look! here come more crowds, pacing straight for the water, and seemingly bound for a dive. Strange! Nothing will content them but the extremest limit of the land; loitering under the shady lee of yonder warehouses will not suffice. No. They must get just as nigh the water as they possibly can without falling in. And there they stand—miles of them—leagues. Inlanders all, they come from lanes and alleys, streets and avenues—north, east, south, and west. Yet here they all unite. Tell me, does the magnetic virtue of the needles of the compasses of all those ships attract them thither?

Once more. Say you are in the country; in some high land of lakes. Take almost any path you please, and ten to one it carries you down in a dale, and leaves you there by a pool in the stream. There is magic in it. Let the most absent-minded of men be plunged in his deepest reveries—stand that man on his legs, set his feet a-going, and he will infallibly lead you to water, if water there be in all that region. Should you ever be athirst in the great American desert, try this experiment, if your caravan happen to be supplied with a metaphysical professor. Yes, as every one knows, meditation and water are wedded for ever.

But here is an artist. He desires to paint you the dreamiest, shadiest, quietest, most enchanting bit of romantic landscape in all the valley of the Saco. What is the chief element he employs? There stand his trees, each with a hollow trunk, as if a hermit and a crucifix were within; and here sleeps his meadow, and there sleep his cattle; and up from yonder cottage goes a sleepy smoke. Deep into distant woodlands winds a mazy way, reaching to overlapping spurs of mountains bathed in their hill-side blue. But though the picture lies thus tranced, and though this pine-tree shakes down its sighs like leaves upon this shepherd’s head, yet all were vain, unless the shepherd’s eye were fixed upon the magic stream before him. Go visit the Prairies in June, when for scores on scores of miles you wade knee-deep among Tiger-lilies—what is the one charm wanting?—Water—there is not a drop of water there! Were Niagara but a cataract of sand, would you travel your thousand miles to see it? Why did the poor poet of Tennessee, upon suddenly receiving two handfuls of silver, deliberate whether to buy him a coat, which he sadly needed, or invest his money in a pedestrian trip to Rockaway Beach? Why is almost every robust healthy boy with a robust healthy soul in him, at some time or other crazy to go to sea? Why upon your first voyage as a passenger, did you yourself feel such a mystical vibration, when first told that you and your ship were now out of sight of land? Why did the old Persians hold the sea holy? Why did the Greeks give it a separate deity, and own brother of Jove? Surely all this is not without meaning. And still deeper the meaning of that story of Narcissus, who because he could not grasp the tormenting, mild image he saw in the fountain, plunged into it and was drowned. But that same image, we ourselves see in all rivers and oceans. It is the image of the ungraspable phantom of life; and this is the key to it all.

---
## [SM45H/f13babylon](https://github.com/SM45H/f13babylon)@[830db814f3...](https://github.com/SM45H/f13babylon/commit/830db814f3104bfe595db02eea0759766eb2cd10)
#### Wednesday 2023-11-29 04:05:03 by GreytidePanda

Expanded Mall (#171)

## About The Pull Request
The northwest mall was an area scraped together from an older mall
building and expanded on by me well over a year ago, but it was always
unfinished as I left Sunset before I submitted the final version. You
can really tell this if you look at some of the suspiciously empty rooms
on the upper levels.

The finished version has been sitting on my harddrive for a long time so
I've copied it in and made a few changes to fit the server. I'm not sure
if the mall is staying with future map changes, but at least for now I
want to be judged on my completed work.

- References to 'Mall of Wyoming' are now 'Mall of Utah'
- A lot of rooms are now less claustrophobic and use their space better
- More loot and detail (no crazy loot - it was always intended as a
fairly beginner friendly zone)
- Now far more vertical - an underground parking lot, and accessible
roof
- Removed the 'requires_power' flag from the mall area tag - no other
ruin uses it
- Fixed the instrument shop shutter not working (I can't believe this
bug has existed for over a year)

## Why It's Good For The Game
Better locations are always good for the game!

## Pre-Merge Checklist
- [x] You tested this on a local server.
- [x] This code did not runtime during testing.
- [x] You documented all of your changes.


## Changelog
:cl:
add: The Mall of Utah now offers an even bigger shopping experience.
/:cl:

---
## [the-furry-hubofeverything/hubble-systems](https://github.com/the-furry-hubofeverything/hubble-systems)@[8c912b522c...](https://github.com/the-furry-hubofeverything/hubble-systems/commit/8c912b522ce51a0421e1f103da41b98289b4741f)
#### Wednesday 2023-11-29 04:54:54 by the-furry-hubofeverything

hyprland: remove

https://web.archive.org/web/20231106052720/https://blog.vaxry.net/articles/2023-inclusiveActivists

I don't like this.

Personally, I don't agree with the justification given here. Yes, we're all people, but respectfully, I don't agree with people needing to be strong and tough to be on the internet.

Also, in my opinion, there were way better ways of dealing with this than condemnation and projection of frustrations.

The internet lets people be who they are while having control over what they share of their real lives. It leads to great things, like the socially anxious experimenting with their identity, and terrible things, like cyberbullying and hate speech.

It's hard to be nice to people. But some people don't even try, and that's sad.

In my opinion, it's harder to listen and be open to change rather than tough and resilient. Being tough all the time is not healthy.

I'm glad to see that there's a bit of an effort in the CoC, though there's seems to be a vocal part of the group who still pushes for no rules. (issue 3366 on hyprland)

I firmly believe that, an inclusive community cannot be tolerant of all behaviour. That's what the rules are made for - punishing by the basis of non-inclusive behaviour, and not by the people themselves. I feel a lot of people conflate that.

We don't exclude people because they are people, we never should. But when people hurt others, that should be taken seriously. Sometimes that even means giving consequences to the people who do these practices.

Vaxry, if you do see this somehow - let's have a chat. I want to hear your story. But, looking at the community right now, I don't feel comfortable being a part of it. Sorry.

---
## [dyrone/git-cooking](https://github.com/dyrone/git-cooking)@[8f23432b38...](https://github.com/dyrone/git-cooking/commit/8f23432b38d9b122be8179295a56688391dc8ad6)
#### Wednesday 2023-11-29 04:57:50 by Johannes Schindelin

windows: ignore empty `PATH` elements

When looking up an executable via the `_which` function, Git GUI
imitates the `execlp()` strategy where the environment variable `PATH`
is interpreted as a list of paths in which to search.

For historical reasons, stemming from the olden times when it was
uncommon to download a lot of files from the internet into the current
directory, empty elements in this list are treated as if the current
directory had been specified.

Nowadays, of course, this treatment is highly dangerous as the current
directory often contains files that have just been downloaded and not
yet been inspected by the user. Unix/Linux users are essentially
expected to be very, very careful to simply not add empty `PATH`
elements, i.e. not to make use of that feature.

On Windows, however, it is quite common for `PATH` to contain empty
elements by mistake, e.g. as an unintended left-over entry when an
application was installed from the Windows Store and then uninstalled
manually.

While it would probably make most sense to safe-guard not only Windows
users, it seems to be common practice to ignore these empty `PATH`
elements _only_ on Windows, but not on other platforms.

Sadly, this practice is followed inconsistently between different
software projects, where projects with few, if any, Windows-based
contributors tend to be less consistent or even "blissful" about it.
Here is a non-exhaustive list:

Cygwin:

	It specifically "eats" empty paths when converting path lists to
	POSIX: https://github.com/cygwin/cygwin/commit/753702223c7d

	I.e. it follows the common practice.

PowerShell:

	It specifically ignores empty paths when searching the `PATH`.
	The reason for this is apparently so self-evident that it is not
	even mentioned here:
	https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_environment_variables#path-information

	I.e. it follows the common practice.

CMD:

	Oh my, CMD. Let's just forget about it, nobody in their right
	(security) mind takes CMD as inspiration. It is so unsafe by
	default that we even planned on dropping `Git CMD` from Git for
	Windows altogether, and only walked back on that plan when we
	found a super ugly hack, just to keep Git's users secure by
	default:

		https://github.com/git-for-windows/MINGW-packages/commit/82172388bb51

	So CMD chooses to hide behind the battle cry "Works as
	Designed!" that all too often leaves users vulnerable. CMD is
	probably the most prominent project whose lead you want to avoid
	following in matters of security.

Win32 API (`CreateProcess()`)

	Just like CMD, `CreateProcess()` adheres to the original design
	of the path lookup in the name of backward compatibility (see
	https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessw
	for details):

		If the file name does not contain a directory path, the
		system searches for the executable file in the following
		sequence:

		    1. The directory from which the application loaded.

		    2. The current directory for the parent process.

		    [...]

	I.e. the Win32 API itself chooses backwards compatibility over
	users' safety.

Git LFS:

	There have been not one, not two, but three security advisories
	about Git LFS executing executables from the current directory by
	mistake. As part of one of them, a change was introduced to stop
	treating empty `PATH` elements as equivalent to `.`:
	https://github.com/git-lfs/git-lfs/commit/7cd7bb0a1f0d

	I.e. it follows the common practice.

Go:

	Go does not follow the common practice, and you can think about
	that what you want:
	https://github.com/golang/go/blob/go1.19.3/src/os/exec/lp_windows.go#L114-L135
	https://github.com/golang/go/blob/go1.19.3/src/path/filepath/path_windows.go#L108-L137

Git Credential Manager:

	It tries to imitate Git LFS, but unfortunately misses the empty
	`PATH` element handling. As of time of writing, this is in the
	process of being fixed:
	https://github.com/GitCredentialManager/git-credential-manager/pull/968

So now that we have established that it is a common practice to ignore
empty `PATH` elements on Windows, let's assess this commit's change
using Schneier's Five-Step Process
(https://www.schneier.com/crypto-gram/archives/2002/0415.html#1):

Step 1: What problem does it solve?

	It prevents an entire class of Remote Code Execution exploits via
	Git GUI's `Clone` functionality.

Step 2: How well does it solve that problem?

	Very well. It prevents the attack vector of luring an unsuspecting
	victim into cloning an executable into the worktree root directory
	that Git GUI immediately executes.

Step 3: What other security problems does it cause?

	Maybe non-security problems: If a project (ab-)uses the unsafe
	`PATH` lookup. That would not only be unsafe, though, but
	fragile in the first place because it would break when running
	in a subdirectory. Therefore I would consider this a scenario
	not worth keeping working.

Step 4: What are the costs of this measure?

	Almost nil, except for the time writing up this commit message
	;-)

Step 5: Given the answers to steps two through four, is the security
	measure worth the costs?

	Yes. Keeping Git's users Secure By Default is worth it. It's a
	tiny price to pay compared to the damages even a single
	successful exploit can cost.

So let's follow that common practice in Git GUI, too.

Signed-off-by: Johannes Schindelin <johannes.schindelin@gmx.de>
Signed-off-by: Pratyush Yadav <me@yadavpratyush.com>

---
## [misterghast/Skyrat-tg-Ghastified](https://github.com/misterghast/Skyrat-tg-Ghastified)@[35cf52a0f9...](https://github.com/misterghast/Skyrat-tg-Ghastified/commit/35cf52a0f97f5f4292a70ad2f83844d32a2a81c4)
#### Wednesday 2023-11-29 05:04:31 by SkyratBot

[MIRROR] The Inversenning : Superior Healing Medications [MDB IGNORE] (#25315)

* The Inversenning : Superior Healing Medications (#79342)

Introducing new inverse reagents for existing superior healing
medications! This push includes...

**Benzoic Acid** : Inverse of Salicylic Acid. Robust fertilizer that
provides a decent range of benefits for plant life.

**Oxymetholone** : Inverse of Oxandrolone. Anabolic steroid that
promotes the growth of muscle during and after exercise.

**Bamethan** : Inverse of Salbutamol. Blood thinner that drastically
increases the chance of receiving bleeding wounds.

**Pendetide** : Inverse of Pentetic Acid. An unusual bioradioactive drug
that purges basic radiation healing chems. Also increases the severity
of radiation poisoning.

**Hyoscyamine** : Inverse of Atropine. Heals heart and stomach damage,
and slowly removes minor toxin damage.

**Ammoniated Sludge** : Inverse of Ammoniated Mercury. A ghastly looking
mess of mercury by-product which causes bursts of manic hysteria.

**Inreziniver** : Inverse of Rezadone. Makes the user horribly afraid of
all things related to carps.

This is an effort to add more variety to the existing inverse reagent
system within chemistry. Not only should this variety serve to provide
additional options for a Chemist to experiment with, they should also
broaden the possibilities for already existing strategies.

* The Inversenning : Superior Healing Medications

---------

Co-authored-by: MGOOOOOO <97645027+MGOOOOOO@users.noreply.github.com>

---
## [kraj/binutils-gdb](https://github.com/kraj/binutils-gdb)@[a393b15517...](https://github.com/kraj/binutils-gdb/commit/a393b155174d20d3d120b5012b87c5438ab9e3d4)
#### Wednesday 2023-11-29 06:15:58 by Andrew Burgess

gdb/python: display errors from command completion

This commit makes the gdb.Command.complete methods more verbose when
it comes to error handling.

Previous to this commit if any commands implemented in Python
implemented the complete method, and if there were any errors
encountered when calling that complete method, then GDB would silently
hide the error and continue as if there were no completions.

This makes is difficult to debug any errors encountered when writing
completion methods, and encourages the idea that Python extensions can
be broken, and GDB will just silently work around them.

I don't think this is a good idea.  GDB should encourage extensions to
be written correctly, and robustly, and one way in which GDB can (I
think) support this, is by pointing out when an extension goes wrong.

In this commit I've gone through the Python command completion code,
and added calls to gdbpy_print_stack() or gdbpy_print_stack_or_quit()
in places where we were either clearing the Python error, or, in some
cases, just not handling the error at all.

One thing I have not changed is in cmdpy_completer (py-cmd.c) where we
process the list of completions returned from the Command.complete
method; this routine includes a call to gdbpy_is_string to check a
possible completion is a string, if not the completion is ignored.

I was tempted to remove this check, attempt to complete each result to
a string, and display an error if the conversion fails.  After all,
returning anything but a string is surely a mistake by the extension
author.

However, the docs clearly say that only strings within the returned
list will be considered as completions.  Anything else is ignored.  As
such, and to avoid (what I think is pretty unlikely) breakage of
existing code, I've retained the gdbpy_is_string check.

After the gdbpy_is_string check we call python_string_to_host_string,
if this call fails then I do now print the error, where before we
ignored the error.  I think this is OK; if GDB thinks something is a
string, but still can't convert it to a string, then I think it's OK
to display the error in that case.

Another case which I was a little unsure about was in
cmdpy_completer_helper, and the call to PyObject_CallMethodObjArgs,
which is when we actually call Command.complete.  Previously, if this
call resulted in an exception then we would ignore this and just
pretend there were no completions.

Of all the changes, this is possibly the one with the biggest
potential for breaking existing scripts, but also, is, I think, the
most useful change.  If the user code is wrong in some way, such that
an exception is raised, then previously the user would have no obvious
feedback about this breakage.  Now GDB will print the exception for
them, making it, I think, much easier to debug their extension.  But,
if there is user code in the wild that relies on raising an exception
as a means to indicate there are no completions .... well, that code
is going to break after this commit.  I think we can live with this
though, the exceptions means no completions thing was never documented
behaviour.

I also added a new error() call if the PyObject_CallMethodObjArgs call
raises an exception.  This causes the completion mechanism within GDB
to stop.  Within GDB the completion code is called twice, the first
time to compute the work break characters, and then a second time to
compute the actual completions.

If PyObject_CallMethodObjArgs raises an exception when computing the
word break character, and we print it by calling
gdbpy_print_stack_or_quit(), but then carry on as if
PyObject_CallMethodObjArgs had returns no completions, GDB will
call the Python completion code again, which results in another call
to PyObject_CallMethodObjArgs, which might raise the same exception
again.  This results in the Python exception being printed twice.

By throwing a C++ exception after the failed
PyObject_CallMethodObjArgs call, the completion mechanism is aborted,
and no completions are offered.  But importantly, the Python exception
is only printed once.  I think this gives a much better user
experience.

I've added some tests to cover this case, as I think this is the most
likely case that a user will run into.

Approved-By: Tom Tromey <tom@tromey.com>

---
## [Whomstbing/Skyrat-tg](https://github.com/Whomstbing/Skyrat-tg)@[8d69a6b49d...](https://github.com/Whomstbing/Skyrat-tg/commit/8d69a6b49df26a323e0a32f7a51ff7033fa5fd5a)
#### Wednesday 2023-11-29 06:31:51 by SkyratBot

[MIRROR] Codifies male goats not having an udder [MDB IGNORE] (#25030)

* Codifies male goats not having an udder (#79722)

## About The Pull Request

This was addressed in #78759 (1b1fde4908826ef5c54ffc0734e74028270af3fd)
and reviewed (and merged even though I didn't respond to it, oh well),
but I half-assed it because the whole point was to prevent male goats
from having an udder, but I only added it to the subtype of Pete i made
in that PR. Let's expand that to all male goats now.
## Why It's Good For The Game

It doesn't make biological nor morphological sense as to why a male goat
can provide milk. Ideally this should be like this for all animals
(because that's real life) but that's a later issue with further balance
implication.

I think it's still an interesting idea that Nanotrasen will just send
you any old goat despite it being "useless" beyond being very good at
eating plants. Maybe cargo should have a way to guarantee getting a
female goat in the future? It's just like real life where zoos and farms
have to constantly dealw ith female animals (such as giraffes or other
exotic stuff) tending to be far rarer/cost far more than their male
variants due to the potential to generate offspring (there's more nuance
to husbandry than this but just play along)... and in space, every
animal is "exotic".

It still remains possible to biogenerate milk, which tends to be far
faster than feeding/milking goats- which is something that the cook
should have access to anyways.
## Changelog
:cl:
balance: Male Goats should no longer spawn with an udder, instead of it
just being Pete.
/:cl:

---------

Co-authored-by: Ghom <42542238+Ghommie@ users.noreply.github.com>

* Codifies male goats not having an udder

---------

Co-authored-by: san7890 <the@san7890.com>
Co-authored-by: Ghom <42542238+Ghommie@ users.noreply.github.com>

---
## [21-ayush/50JsProjects](https://github.com/21-ayush/50JsProjects)@[e525cc1850...](https://github.com/21-ayush/50JsProjects/commit/e525cc1850c82d0a35e2c27b6dfa4f517ce09747)
#### Wednesday 2023-11-29 06:42:29 by Ayush

Add files via upload

A whimsical web project crafted with HTML, CSS, and JS. Experience the joy of  humor with a simple click. Press the button, and voilà! A new dad joke appears, ready to brighten your day. It's quick, it's fun, and it's your go-to source for instant laughter. Dad jokes, one click away!

---
## [Machad3x/android_kernel_oneplus_sm8450](https://github.com/Machad3x/android_kernel_oneplus_sm8450)@[65aefa1fd8...](https://github.com/Machad3x/android_kernel_oneplus_sm8450/commit/65aefa1fd8bb2f07b2a232f5d9f3a9a34a7b5132)
#### Wednesday 2023-11-29 06:47:14 by Peter Zijlstra

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
## [Ahcai2006/Index.html](https://github.com/Ahcai2006/Index.html)@[33071928e7...](https://github.com/Ahcai2006/Index.html/commit/33071928e7359819866a8ecb73716fbb3c375ac6)
#### Wednesday 2023-11-29 07:22:35 by Ahcai2006

Update issue templates

{"prefix":{"title":"Hi 👋, I'm","currentWork":"🔭 I’m currently working on","currentLearn":"🌱 I’m currently learning","collaborateOn":"👯 I’m looking to collaborate on","helpWith":"🤝 I’m looking for help with","ama":"💬 Ask me about","contact":"📫 How to reach me","resume":"📄 Know about my experiences","funFact":"⚡ Fun fact","portfolio":"👨‍💻 All of my projects are available at","blog":"📝 I regularly write articles on"},"data":{"title":"linqingcai","subtitle":"A passionate frontend developer from Vietnam","currentWork":"","currentLearn":"","collaborateOn":"","helpWith":"","ama":"","contact":"","funFact":"","twitterBadge":false,"visitorsBadge":false,"badgeStyle":"flat","badgeColor":"0e75b6","badgeLabel":"Profile views","githubProfileTrophy":false,"githubStats":false,"githubStatsOptions":{"theme":"","titleColor":"","textColor":"","bgColor":"","hideBorder":false,"cacheSeconds":null,"locale":"en"},"topLanguages":false,"topLanguagesOptions":{"theme":"","titleColor":"","textColor":"","bgColor":"","hideBorder":false,"cacheSeconds":null,"locale":"en"},"streakStats":false,"streakStatsOptions":{"theme":""},"devDynamicBlogs":false,"mediumDynamicBlogs":false,"rssDynamicBlogs":false},"link":{"currentWork":"Tiktok","collaborateOn":"","helpWith":"","portfolio":"","blog":"","resume":""},"social":{"github":"","dev":"","linkedin":"","codepen":"","stackoverflow":"","kaggle":"","codesandbox":"","fb":"","instagram":"","twitter":"","dribbble":"","behance":"","medium":"","youtube":"","codechef":"","hackerrank":"","codeforces":"","leetcode":"","topcoder":"","hackerearth":"","geeks_for_geeks":"","discord":"","rssurl":""},"skills":{"11ty":false,"amplify":false,"android":true,"angular":false,"angularjs":false,"apachecordova":false,"appwrite":false,"arduino":false,"aws":false,"azure":false,"babel":false,"backbonejs":false,"bash":false,"blender":false,"bootstrap":false,"bulma":false,"c":true,"canvasjs":false,"cassandra":false,"chartjs":false,"circleci":false,"clojure":false,"cockroachdb":false,"codeigniter":false,"coffeescript":false,"couchdb":false,"cplusplus":false,"csharp":false,"css3":false,"cypress":false,"d3js":false,"dart":false,"django":false,"docker":false,"dotnet":false,"elasticsearch":false,"electron":false,"elixir":false,"ember":false,"erlang":false,"express":false,"figma":false,"firebase":false,"flask":false,"flutter":false,"framer":false,"gatsby":false,"gcp":false,"git":false,"go":false,"grafana":false,"graphql":false,"gridsome":false,"gtk":false,"gulp":false,"hadoop":false,"haskell":false,"heroku":false,"hexo":false,"hive":false,"html5":true,"hugo":false,"ifttt":false,"illustrator":false,"invision":false,"ionic":false,"jasmine":false,"java":false,"javascript":false,"jekyll":false,"jenkins":false,"jest":false,"kafka":false,"karma":false,"kibana":false,"kotlin":false,"kubernetes":false,"laravel":false,"linux":false,"mariadb":false,"materialize":false,"matlab":false,"middleman":false,"mocha":false,"mongodb":false,"mssql":false,"mysql":false,"nativescript":false,"nestjs":false,"nextjs":false,"nginx":false,"nim":false,"nodejs":true,"nuxtjs":false,"objectivec":false,"opencv":false,"openresty":false,"oracle":false,"pandas":false,"perl":false,"photoshop":false,"php":false,"postgresql":false,"postman":false,"pug":false,"puppeteer":false,"python":false,"pytorch":false,"qt":false,"quasar":false,"rabbitMQ":false,"rails":false,"react":false,"reactnative":false,"realm":false,"redis":false,"redux":false,"ruby":false,"rust":false,"sapper":false,"sass":false,"scala":false,"scikit_learn":false,"scully":false,"sculpin":false,"seaborn":false,"selenium":false,"sketch":false,"solr":false,"spring":false,"sqlite":false,"svelte":false,"swift":false,"symfony":false,"tailwind":false,"tensorflow":false,"travisci":false,"typescript":false,"unity":false,"unreal":false,"vagrant":false,"vuejs":true,"vuepress":false,"vuetify":false,"webpack":false,"wx_widgets":false,"xamarin":false,"xd":false,"zapier":false},"support":{"buyMeACoffee":""}}

---
## [khushboosharma94/Facebook_Data_Analysis](https://github.com/khushboosharma94/Facebook_Data_Analysis)@[5579355288...](https://github.com/khushboosharma94/Facebook_Data_Analysis/commit/5579355288649e3b49ce47878c022af66505577f)
#### Wednesday 2023-11-29 07:35:51 by khushboosharma94

Update README.md

Facebook Data Analysis
 Create table facebook 

To see all csv files available in HDFS :
ls -l
csv file path: hdfs dfs -put /home/mavricbdhnov0433/pseudo_facebook.csv 

[mavricbdhnov0433@ip-10-1-1-204 ~]$ hdfs dfs -put /home/mavricbdhnov0433/pseudo_facebook.csv                                           
put: `pseudo_facebook.csv': File exists                                                                                                
[mavricbdhnov0433@ip-10-1-1-204 ~]$

 

Create database :
Hive>   create database khusboosharma;
show databases like '*khushboo*';
hive> show databases like '*khushboo*';                                                                                                
OK                                                                                                                                     
Time taken: 0.434 seconds
hive> use khusboosharma;                                                                                                               
OK                                                                                                                                     
Time taken: 0.04 seconds  
Create fb_data table in khusboosharma database  :
Hive>   create table fb_data(id int, age int, day int, year int, month int, gender string, tenure int, friends int,
friend_init int, likes int, likes_recd int,mlikes int, mlikes_recd int, wlikes int, wlikes_recd int)
row format delimited 
fields terminated by ',';
OK                                                                                                                                     
Time taken: 0.435 seconds
To load the data into Hive:
LOAD DATA local INPATH 'pseudo_facebook.csv' OVERWRITE INTO TABLE fb_data;
To see table structure:
describe fb_data;
To see the table data:
select * from fb_data limit 50;
1. Find out the total number of users in this dataset.
select count(*) from fb_data;

 

 Q2: Find out the no of users above the age of 25

select count(*) from fb_data where age>25;

 


 Q3: Do male face book users tend to have more friends or female users

select gender,avg(friends) from fb_data group by gender;


 

4. How many likes do young people recieve on facebook opposed to older people.
select avg(likes_recd) from fb_data where age>=13 AND age<=25; 

select avg(likes_recd) from fb_data where age>25;

 

 

5. Find out the count of facebook users for each birthday month.
select month,count(*) from fb_data group by month;


 

6. Do young members use mobile phones or computer for fb browsing?
select avg(mlikes),avg(wlikes) from fb_data where age>=13 AND age<=25;


 


7. Do adult members use mobile phones or computer for fb browsing?
select avg(mlikes),avg(wlikes) from fb_data where age>=35;

---
## [pompororo/VR_Project](https://github.com/pompororo/VR_Project)@[4f1b22d92d...](https://github.com/pompororo/VR_Project/commit/4f1b22d92d933159f05aa792c5222c9a7d5d039c)
#### Wednesday 2023-11-29 07:39:22 by pompororo

Fuck you

Co-Authored-By: FrozenTEAR <85834370+froz4d@users.noreply.github.com>

---
## [MGOOOOOO/tgstation](https://github.com/MGOOOOOO/tgstation)@[9ff9e4b9a8...](https://github.com/MGOOOOOO/tgstation/commit/9ff9e4b9a849e4a50bf500aaaeca5e020e7677d6)
#### Wednesday 2023-11-29 08:18:15 by necromanceranne

Scatter laser shells now use the scatter laser beam, and makes them significantly easier to make. Projectiles can now have damage falloff. (#78927)

## About The Pull Request

Allows for damage falloff to apply to more than just shotgun pellets.
Now any projectile can have a damage falloff defined.

Scatter Laser shells no longer use the minigun beams to determine their
damage. Instead they use the actually defined scatter laser beams. Those
beams do 7.5 damage per pellet, times by 6 pellets.

Scatter laser beams now have damage falloff, a separately defined
(positive) wounding power from normal beams, and wound falloff.

Scatter laser shells can be printed from security protolathes once you
have weapon tech.

Scatter laser shells _may_ be damaged by EMPs based on severity. The
result is that it fires a practically useless volley of laser fire. They
cause a honk sound when they hit, so you know when you've shot one of
these.

## Why It's Good For The Game

Well, we want shotguns universally to not be defined by their damage
output (especially extreme damage output) but by niche.

What does the scatter laser shell currently occupy as a niche?

The single highest damage output of any projectile weapon in direct
damage. The thing we don't want of shotguns, and it is reigning champion
of all guns.

Okay, that's a bit misleading, because obviously it is competing with
the likes of .50 BMG which does 70 damage outright and dismembers limbs,
potentially doing upwards of 90 damage if it does, and also hard stuns
people. Obviously _that_ is technically a stronger bullet.

But not for raw damage, because the scatter laser does 90 damage out the
gate, barring any potential wounding that might occur which increases
the damage multiplicatively. No gimmicks, no extra procs, nothing. It's
just 15 force lasers (with no damage dropoff) split between 6 beams.

And the reason for this is because this shell has been nerfed once prior
by making it not fire 6 normal laser shots into someone. That was 120
damage at the time, 120 to 90 was...I guess a nerf during the taser era.
Depends on how you viewed it. Buckshot was doing like 80 at the time,
believe me it was a wild period. But anyway, when we did the whole
damage rearrangement over the course of the laser few years, every other
shell got touched except this one for some reason. Even pulse slugs lost
10 damage while this was still sitting on 90 force point blank.

So what is the new niche? Well, it's laser buckshot. That's not a niche
but crew don't get buckshot, so this is their buckshot. It wounds real
good. Real goddamn good. And its is a laser. It fits the aesthetic,
obviously.

Okay, thanks.

## Changelog
:cl:
balance: Scatter laser shells actually utilize the _real_ scatter laser
beam. This comes with damage changes. And wounding power.
feature: EMPs can potentially damage scatter laser shells.
refactor: All projectiles can now have damage falloff defined. Yay.
balance: Scatter laser shells can be printed when weapons technology is
researched.
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [MGOOOOOO/tgstation](https://github.com/MGOOOOOO/tgstation)@[071f6063e6...](https://github.com/MGOOOOOO/tgstation/commit/071f6063e69d39e1403eca917a395191339f353a)
#### Wednesday 2023-11-29 08:18:15 by carlarctg

Adds charges to omens and omen smiting. Reduces omen bad luck if nobody's nearby. (#78899)

## About The Pull Request

refactor: Adds charges to omens and omen smiting rather than only being
permanent or one-use. Mirrors now grant seven bad luckers.

qol: Reduces omen bad luck if nobody's nearby to witness the funny.
(Ghosts are included in the check!)

fix: Fixed an issue where a monkey check in doorcrushing was never
actually able to pass. Also they screech now.

## Why It's Good For The Game

> refactor: Adds charges to omens and omen smiting rather than only
being permanent or one-use. Mirrors now grant seven bad luckers.

Allows for someone to get between 1-infinity omen accidents. Seriously
why wasnt this a thing before

> qol: Reduces omen bad luck if nobody's nearby.

I LOVE this quirk, but trying to do antything at all except 'Suffer
Miserably' is nigh impossible. To alleviate life a little, making it so
that you have a lesser chance of suffering misfortune if nobody's around
will be the perfect compromise. It makes life easier but doesn't
compromise funny moments.

Any client in viewrange will disable the reduction. This includes
ghosts.

## Changelog

:cl:
refactor: Adds charges to omens and omen smiting rather than only being
permanent or one-use. Mirrors now grant seven bad luckers.
qol: Reduces omen bad luck if nobody's nearby to witness the funny.
(Ghosts are included in the check!)
fix: Fixed an issue where a monkey check in doorcrushing was never
actually able to pass. Also they screech now.
/:cl:

---------

Co-authored-by: Ghom <42542238+Ghommie@users.noreply.github.com>

---
## [MGOOOOOO/tgstation](https://github.com/MGOOOOOO/tgstation)@[0d5f9907a2...](https://github.com/MGOOOOOO/tgstation/commit/0d5f9907a24346554f4da78199138f4cdcca8de5)
#### Wednesday 2023-11-29 08:18:15 by Jacquerel

Shapechange health transfer tweaks (#79009)

## About The Pull Request

Fixes #78721
This PR does a handful of things behind the scenes to increase the
consistency of shapechange health tracking.

First of all we adjust the order of operations taken when you restore
the original body. The implementation as-was would remove the status
effect midway through and null a bunch of variables we tried to continue
using. This would result in several runtimes and code failing to run,
with the upshot that untransforming upon death would leave the caster
completely alive, with the corpse of its transformed shape at its feet.
Oops.

Additionally while testing this I realised that transferring the damagew
as also kind of fucked.
We wouldn't bother to do it at _all_ if you died, which is a shame, so I
made it simply heal you instead of reviving you so we can always do it.
Then as noted in the linked issue, we were applying all transferred
damage to a single limb, which could exceed the health of the limb and
remove damage. Now we spread it around the body.

Finally, applying damage to a human using the "force" flag would often
actually apply less damage to their _health_ than expected. This is
because arms and legs contribute only 75% of their damage taken to a
mob's overall health.
Now instead of reading `health` we read `total damage` which ignores the
limb damage modifier.

The end result of this is that if you transform into a corgi, take 50%
of your health, and transform back then you will have 50% of your health
as a human.
Previously the result would be that you'd have ~63%, then transforming
into a corgi would leave you with ~63% of a corgi's health, then
transforming back into a human would leave you at about 71%... and so on
and so forth. Now it doesn't do that.

## Changelog

:cl:
fix: Dying when using (most) shapeshift spells will now kill you rather
than having you pop out of the corpse of your previous form.
fix: Damage will now be accurately carried between forms rather than
being slightly reduced upon each transformation.
/:cl:

---
## [iprtel/cppfront](https://github.com/iprtel/cppfront)@[cdf71bdca6...](https://github.com/iprtel/cppfront/commit/cdf71bdca64536a005f2491d8c19f1d05a1c62f6)
#### Wednesday 2023-11-29 08:19:39 by Herb Sutter

Correct copy/move for `union`

By writing separate construction and assignment, plus the new feature of suppressing assignment to a member by writing `member = _ ;` (now allowed only in assignment operators).

I do realize that's an "opt-out" which I normally prefer to avoid, but:

- I considered and decided against (for now) the alternative of not having assignment be memberwise by default. I want to keep the (new to Cpp2) default of memberwise semantics for assignment as with construction. I think that's a useful feature, and normally if you do assign to a member it doesn't arise, and so I think it makes sense to explicitly call out when we're choosing not to do any assignment at all to a member before doing other assignment processing. We'll get experience with how it goes.

- `_` is arguably natural here, since it's pronounced "don't care." There too, we'll see if that is natural generalized, or feels strained. For now it feels natural to me.

---
## [moul/gno](https://github.com/moul/gno)@[24d89a4f5d...](https://github.com/moul/gno/commit/24d89a4f5debd3c1ae711e98587e1e32980e4347)
#### Wednesday 2023-11-29 08:56:19 by Morgan

feat(examples): add p/demo/seqid (#1378)

A very simple ID generation package, designed to be used in combination
with `avl.Tree`s to push values in order.

The name was originally `seqid` (sequential IDs), but after saying it a
few times I realised it was close to "squid" and probably would be more
fun if I named it that way ;)

There's another piece of functionality that I want to add, which is a
way to create simple base32-encoded IDs. This depends on #1290. These
would also guarantee alphabetical ordering, so a list of them can be
easily sorted and you'd get it in the same order they were created. They
would likely be 13 characters long, but I'm also thinking of making a
compact version which works from [0,2^35) which is 7 chracters, and then
smoothly transitions over to the 13 characters version when the ID is
reached.

(I've experience with both base64 and base32 encoded IDs as 64-bit
numbers, as I used both systems. The advantage of base32 is that it
makes IDs case insensitive, all the while being at most 13 bytes instead
of 11 for base64.)

In GnoChess, we used simple sequential IDs combined with
[`zeroPad9`](https://github.com/gnolang/gnochess/blob/7e841191a4a0a94c0d46bc977458bd6b757eab5e/realm/chess.gno#L287-L296)
to create IDs which were both readable and sortable. I want to make a
more "canonical" solution to this which does not have a upper limit at 1
billion entries.

---
## [elunna/HACKEM-MUCHE](https://github.com/elunna/HACKEM-MUCHE)@[87bea4e8cd...](https://github.com/elunna/HACKEM-MUCHE/commit/87bea4e8cda89d1785737dc3b693db66633e058e)
#### Wednesday 2023-11-29 09:14:14 by Erik Lunna

Implement behavior for cursed potion of gain ability (from xNetHack).

I had originally implemented the cursed gain ability effect from slashem-up, but I found that xnh just did it better, and in a less harmful way - so we'll use that instead.

From xNetHack commit ac43b0c182bf:

'This potion doing nothing whatsoever if you drink it when cursed is
pretty weak. It ought to have some effect, even if the effect isn't
particularly great in keeping with how cursed effects usually are.

This implements an idea by FIQ that the potion should gain you an
ability point by stealing the point from elsewhere. The trick is that it
will always grant to the lowest score, and steal from the highest -
which could make it situationally useful for raising low ability scores
when your highest score is not of particular importance (think very high
Charisma or 18/xx Strength) and you lack the resources to uncurse or
bless the potion.'

---
## [johncowen/kuma-gui](https://github.com/johncowen/kuma-gui)@[4ef8003e2c...](https://github.com/johncowen/kuma-gui/commit/4ef8003e2c7d164ba225a87abe7c243c2db579d1)
#### Wednesday 2023-11-29 09:59:19 by John Cowen

feat(dataplanes): Add ServiceTraffic component (#1807)

This PR adds 2 things:

1. A `ServiceTraffic` component and related sub-components. This is the component only and is not hooked up to any data.
2. In order to be able to build/PR/merge the above component in isolation without adding it to our actual application. I've added a very rough sandbox in our docs that can be seen via `yarn docs:dev` (we can add PR previews at a later date which will be much better)

## ServiceTraffic component

I'm looking for feedback on the component itself, plus its subcomponents. Hopefully it's clear where the data will be plugged into this in a later PR and finally integrated into our application.

## Docs/Component Sandbox

I wanted to start getting this in as I would really like to use this more for building/manually testing/previewing our reusable components. It has the additional benefit of being able to work on, PR and merge components that aren't yet used in our application. Almost like feature flags but instead of feature flagging our in-production application, we just use a completely different application. In the future we should be able to gradually build entire features in isolation using this sandbox application, then just enable them in production when we want to.

As you can see the code here is very much in-progress. I went out of my way not to alter any of our application code just yet, but I think some injection related things will change ever so slightly to allow us to reuse things better.

Lastly I'd be happy to close this PR either way and wait for everything to be integrated, but I wanted to get feedback early on both of the above features and I also wanted to do a final CI check on the sandbox stuff and start thinking about CI integration. Let me know either way. I'd also be happy splitting these features into separate PRs, but really in order to test/experience one you need the other.

---------

Signed-off-by: John Cowen <john.cowen@konghq.com>

---
## [MarkSuckerberg/Shiptest](https://github.com/MarkSuckerberg/Shiptest)@[389d1e5669...](https://github.com/MarkSuckerberg/Shiptest/commit/389d1e566990682f173066df4c16f25b3a1858c0)
#### Wednesday 2023-11-29 10:54:26 by Erika Fox

Does Penance So The Ghosts Go Away (#2442)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

"This is AI c-Caldwell - Reporting return of essential station functions
to Minya League Installation 'Trifuge' following pirate attack -
**///far too long ago///** - All vessels are invited to dock and partake
of our services, including an active Ore Refinery, world class bar, and
purchasable storefronts **//please come, I'm so lonely///** The Minya
League, and myself, would like to extend our gratitude to **///-who else
but me?///**. Installation 'Trifuge' is located in orbit of the Star
'Anselhome', at the L5 point of Anselhome and habitable world, 'Hofud'.
Noting active travel advisory - Hofud is currently **///nothing but ash
left by monsters///**. Independent Vessels are advised to avoid landing
until Minya League Ships can deliver disaster relief to the planet
**///not that they'll be coming....///**"

"This message will repeat in approximately 20 galactic standard minutes"

Remaps the shitty outpost 1 (indie space) outpost that I made like 6
months ago. it sucks. Anyone who doesn't think it sucks probably has
stockholm symdromed themselves into liking it. Also this one has lore
and room for expansion.
It's main features are: 
- Decent amount of maint for outpost antics
- REASONABLE amount of storefronts
-abandoned feel
- bar
- Ore refinery so my holy mandate can be implemented when I decide I'm
done with my break.

![2023-10-30 22 34
33](https://github.com/shiptest-ss13/Shiptest/assets/94164348/de3d93e2-e43b-478a-9d8c-7b44c972433d)
![2023-10-30 22 34
35](https://github.com/shiptest-ss13/Shiptest/assets/94164348/770109d4-1ab8-46b2-b3b8-e96c575cdde4)
There are your screenshots.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
I'd like the voices in my walls to stop whispering to me about the
horrific mistakes I've made. They seem pretty upset about this one.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: Erika Fox
add: Outpost 1 has been remapped into something fathomably less ass.
It's a bit smaller, probably, but I'm going to call that a good thing.
add: random number spawner. It's good for hull numbers that shouldn't be
static.
imageadd: a really bad sprite for a service directions sign.
add: Another elevator template (coincidentally demonstrating how that
system works in code)

/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: spockye <79304582+spockye@users.noreply.github.com>

---
## [MarkSuckerberg/Shiptest](https://github.com/MarkSuckerberg/Shiptest)@[88e683cec6...](https://github.com/MarkSuckerberg/Shiptest/commit/88e683cec669624228d5204d7e3da06e6075d158)
#### Wednesday 2023-11-29 10:54:26 by zevo

Massive Ruin Fixes + Removals PR (#2334)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
This PR is made so I can stop getting angry at the ruins beyond saving
that are still ingame. My criteria for a ruin being removed is if
another ruin already does its niche better, if the ruin is outdated
and/or the ruin is excessively small or unbalanced. For ruins that dont
meet this criteria but are still outdated, they will be getting balance
fixes and touch ups or a total remap.

This PR is a draft for now because I will need to update the PR
changelog and description as I make changes and communicate with the
maptainers on what stays and what goes.

Adds departmental RND lootdrop spawners for circuit imprinters,
protolathes and techfabs. Excludes omnisci and basic boards from the
drops.
Fixed a space tile under a door and replaced the omnilathe with a
medical lathe on dangerousresearch
Fixed the whitesands saloon not spawning which may have caused some
sandplanets to spawn without a ruin
Fixed harmfactory's nonfunctional traps to now be as lethal as intended.
Also changed the loot in the vault to better reflect the ruin's theme
and difficulty (cargo techfab board instead of omnilathe, adv plasma
cutter instead of combat medkit, less gold more cash, kept the cyberarm
implant).
Fixed provinggrounds magical SMES FINALLY by adding a terminal on the
back. The map should finally function as intended.
Fixed a few dirs on fire extinguisher cabinets and blast door assemblies
in singularity_lab
Removed mechtransport.dmm for being small and bad
Removed some leftover gasthelizards.dmm cruft (VILE)
Removed nucleardump for being an utter mess of an oldcode ruin
Removed gondolaasteroid for being large and empty besides gondolas.
better suited for a jungle planet IMO.
Removed Jungle_Spider. Literally just a box with spiders and cloning
equipment. Small, bad, hard to find, unjustified loot.
Removed Golem_Hijack. Like jungle spider but it was free rnd, an AI
core, a full BSRPED and three golem corpses. With no enemies or
obstacles.
Removed rockplanet_clock for being a tiny lootbox that doesnt fit with
the lore. Also had a quantumn pad.
Removed whitesands_surface_youreinsane. Its a silly little reference to
an old event that unfortunately resulted in a subpar ruin. Could return
as a wasteplanet greeble ruin, but it has to go for now.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
Normally I'm all for remapping instead of removing ruins, but some ruins
are very much beyond saving. Clearing out space for better ruins to take
the spotlight is always nice. Some older ruins are fine but are missing
certain things or have loot that worked fine in the past, but doesn't
reflect the balance we want for ruins in the present.

I will be PR'ing ruins to replace the ones I remove.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: departmental RND lootdrop spawners for imprinters, protolathes and
techfabs
fix: dangerous_research.dmm now no longer has a space tile under a door
and a medical lathe instead of an omnilathe
fix: whitesands_surface_camp_saloon can now spawn again after its remap
into a functional ruin
fix: harmfactory.dmm's traps now work and loot has been adjusted to fit
the ruin better
fix: provinggrounds.dmm now has a working SMES and power
fix: singularity_lab fire extinguishers and a few poddoors now have
correct dirs
del: mechtransport.dmm and associated code
del: gasthelizards areas
del: nucleardump.dmm and associated code
del: gondolaasteroid.dmm and associated code
del: jungle_spider.dmm and associated code
del: whitesands_golem_hijack.dmm and associated code
del: rockplanet_clock.dmm and associated code
del: whitesands_surface_youreinsane.dmm and associated code
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Signed-off-by: zevo <95449138+Zevotech@users.noreply.github.com>

---
## [lizardqueenlexi/orbstation](https://github.com/lizardqueenlexi/orbstation)@[9229adc934...](https://github.com/lizardqueenlexi/orbstation/commit/9229adc934b9575a8528b6efc0074fcc2921cc33)
#### Wednesday 2023-11-29 11:02:31 by DaydreamIQ

Touches up Moffuchi's pizzeria  (#79899)

## About The Pull Request
I've given the icebox pizzeria ruin a few small improvements:
- Firstly, The kitchen is actually stocked with tomatoes from the get
go. Along with a few mothic themed ingredients for those signature
mothic pizzas we all know and love (And hate for being such a pain to
make)
- The discarded air alarm frames have been replaced with working ones
(I'm unsure if this was intentional or not)
- Some drinking glasses have been added to the bar
- And finally a pacman has been placed in the backroom along with some
plasma to power the place
## Why It's Good For The Game
This place gets overlooked a lot because its completely powerless, and
doesn't actually give you enough from the get go to make even a basic
pizza besides the tomato seeds a lot of people are gonna miss. This
gives the ruin just a little more life to maybe be worth trekking out
for. And having mothic themed ingredients in the **MOFFIC** Pizzeria
just makes sense even if they are a bitch to make.

Not sure if this counts as a balance change or a QOL so feel free to
yell at me if I've labelled this wrong, I have been advised that this
SHOULD be the latter at least.
## Changelog
:cl:
qol: Mothuchi's pizzeria has been improved slightly! Order yourself a
fresh mothic pizza today!
/:cl:

---
## [TheBronJameOffical/lobotomy-corp13](https://github.com/TheBronJameOffical/lobotomy-corp13)@[33ec2cf7cf...](https://github.com/TheBronJameOffical/lobotomy-corp13/commit/33ec2cf7cf4aafeb3888ac65f26572a385fafdd9)
#### Wednesday 2023-11-29 11:26:45 by The Bron Jame Offical

new content babey

i ahve made a severe lapse in my judgement and I do not expect to be forgiven. yadda yadda something reaping what i've sown something

Claw stuff

Claw sounds

CLAW ARMORRRRRRR

claw antag

please work

some of egors fixes

visual updates

new antag things

justice mod

fuckin, 1 god damn character change

---
## [stackrox/oauth2](https://github.com/stackrox/oauth2)@[a835fc4358...](https://github.com/stackrox/oauth2/commit/a835fc4358f6852f50c4c5c33fddcd1adade5b0a)
#### Wednesday 2023-11-29 11:46:22 by Brad Fitzpatrick

oauth2: move global auth style cache to be per-Config

In 80673b4a4 (https://go.dev/cl/157820) I added a never-shrinking
package-global cache to remember which auto-detected auth style (HTTP
headers vs POST) was supported by a certain OAuth2 server, keyed by
its URL.

Unfortunately, some multi-tenant SaaS OIDC servers behave poorly and
have one global OpenID configuration document for all of their
customers which says ("we support all auth styles! you pick!") but
then give each customer control of which style they specifically
accept. This is bogus behavior on their part, but the oauth2 package's
global caching per URL isn't helping. (It's also bad to have a
package-global cache that can never be GC'ed)

So, this change moves the cache to hang off the oauth *Configs
instead. Unfortunately, it does so with some backwards compatiblity
compromises (an atomic.Value hack), lest people are using old versions
of Go still or copying a Config by value, both of which this package
previously accidentally supported, even though they weren't tested.

This change also means that anybody that's repeatedly making ephemeral
oauth.Configs without an explicit auth style will be losing &
reinitializing their cache on any auth style failures + fallbacks to
the other style. I think that should be pretty rare. People seem to
make an oauth2.Config once earlier and stash it away somewhere (often
deep in a token fetcher or HTTP client/transport).

Change-Id: I91f107368ab3c3d77bc425eeef65372a589feb7b
Signed-off-by: Brad Fitzpatrick <bradfitz@golang.org>
Reviewed-on: https://go-review.googlesource.com/c/oauth2/+/515675
TryBot-Result: Gopher Robot <gobot@golang.org>
Reviewed-by: Roland Shoemaker <roland@golang.org>
Reviewed-by: Adrian Dewhurst <adrian@tailscale.com>
Reviewed-by: Michael Knyszek <mknyszek@google.com>

---
## [alphagov/signon](https://github.com/alphagov/signon)@[d448c0d873...](https://github.com/alphagov/signon/commit/d448c0d873720798036c2498f1885e4d11822981)
#### Wednesday 2023-11-29 11:47:51 by James Mead

Extract page for mandating 2SV for a user

Trello: https://trello.com/c/caETStGa

This is a step on the journey to move the edit user page to use the
GOV.UK Design System. The new design calls for separate pages for
different operations on a user and this is the next one.

The `require_2sv` checkbox was previously only displayed on the "edit
user" page (from `app/views/users/_form_fields.html.erb`) when
`User#require_2sv?` was `false` and thus it was only ever possible to
use this checkbox to *mandate* 2SV; it was not possible to use it to
*unset* the `User#require_2sv` attribute.

Unlike in commits like this one [1] where we first split out the new
page and then separatly moved the new page to use the Design System,
here I've created the new page using the Design System in one go,
because there wasn't much markup in the "edit user" page to extract.

The new `app/views/users/two_step_verification_mandations/edit.html.erb`
template is based on other similar pages which we've recently extracted,
e.g. `app/views/users/two_step_verification_resets/edit.html.erb`. I
decided not to include a checkbox on the new page, because as mentioned
above, this page should only ever be needed to *mandate* 2SV.

The new `Users::TwoStepVerificationMandationsController` is closely
based on the relevant bits of code from `UsersController`, even though
some of it is probably overkill in the new context, i.e. the use of
`UserUpdate`. However, I thought it was worth keeping this step as small
as possible. I've hard-coded `user_params` to `{ require_2sv: true }`,
since there's no checkbox in the form.

I'm using `UserPolicy#mandate_2sv?` for the authorization in the new
`Users::TwoStepVerificationRequirementsController`, because that seems
to make the most sense. You could argue that I should also check
`UserPolicy#edit?` & `UserPolicy#update?` like I did in
`Users::OrganisationsController` in this commit [2], but I've gone off
that idea (sorry, @chrisroos!). Instead I've matched what I did in
`Users::TwoStepVerificationResetsController` in this commit [3].

There weren't *any* tests in `UsersControllerTest` for this behaviour,
so I had to write `Users::TwoStepVerificationMandationsControllerTest`
from scratch, but I based it closely on other similar controller tests.
Luckily there was an integration test
(`test/integration/managing_two_step_verification_test.rb`) covering the
behaviour which I've been able to fixup to work with the new UI.

Rather than creating a combinatorial explosion of tests in
`Users::TwoStepVerificationRequirementsControllerTest` relating to
whether a user with all the different roles can edit another user with
all the different roles, I've resorted to stubbing `UserPolicy.new` and
`UserPolicy#mandate_2sv?`. Although this is a bit ugly, since
`UserPolicy` is thoroughly tested in `UserPolicyTest`, it seems like a
pragmatic option.

I'm using the `error_summary` component in combination with identical
code we've used elsewhere on the off-chance there's a validation error,
because the controller action does re-render the form in that case. Note
that in normal operation there are unlikely to be validation errors on
this page, but since it's theoretically possible I thought it was worth
adding the error summary. We might want to consider changing this to
work more like `Users::TwoStepVerificationResetsController` which raises
an exception if there is a validation error. This makes sense
particularly given that the only validation on `User#require_2sv` only
applied on record creation.

[1]: https://github.com/alphagov/signon/commit/899a8a16356ad3b9e3434feaf99f5e5f2bf8a243
[2]: https://github.com/alphagov/signon/commit/bf207efe2769c0ae48102b40bb6df8e4f7ce7770
[3]: https://github.com/alphagov/signon/commit/1baf6856c34f857d71466ec3cb11e974a141175d

---
## [demogorgon22/dnethack-observation-center](https://github.com/demogorgon22/dnethack-observation-center)@[574959a482...](https://github.com/demogorgon22/dnethack-observation-center/commit/574959a482252cee418c6ea9da1c799d57c2e4be)
#### Wednesday 2023-11-29 12:50:11 by Ron Nazarov

Allow specifying figurine/statue gender and show more info in dump

Statue/figurine gender changes:
-You can now specify the gender of figurines/statues in wishes, as
 well as the gender of pets summoned with candles of invocation.
--"male/female figurine/statue of an X" and
  "male/female X statue/figurine" both work, but
  "statue/figurine of a male/female X" does not
---NetHack 3.7 fixes this but its wish parser differs so I can't just
   copy from it.  3.7 also supports specifying gender of corpses but
   I don't know if dNetHack even stores that, and, if so, where.
-There are now MM_MALE/MM_FEMALE makemon flags.  These are required
 for gendered figurines to have the same starting inventory:
 previously gender was set after makemon so they would have the wrong
 starting inventory, but this wasn't an issue in practice because they
 were unobtainable outside of wizmode.  This isn't an issue for
 statues because they don't get starting inventory.

More info in enlightenment and end-of-game dump:
-uacinc is now shown, and exact uacinc and protection are always
 shown: the player always knows their own AC/DR so there is no reason
 to hide them.
--Study is also always shown for the same reason.
-Madnesses are now always shown in the end-of-game dump, even if you
 had clear thoughts or 100 sanity.
-Old wizmode spirit count is removed.  It's redundant.
-Inherited artifact is shown in end-of-game dump.
-Information that was previously wizmode-only is shown in end-of-game
 dump.  There's no reason to hide information in the end-of-game dump.
--Exact alignment record, alignment max, sins, various keter counts,
  quest stag/leader backstab status.
---Should this even be restricted to wizmode/final only?

Other changes:
-Wishing for "amulet versus evil eyes" now works, along with several
 alternate spellings.

---
## [mbondyra/kibana](https://github.com/mbondyra/kibana)@[cd909f03b1...](https://github.com/mbondyra/kibana/commit/cd909f03b1d71da93041a0b5c184243aa6506dea)
#### Wednesday 2023-11-29 12:54:19 by Kyle Pollich

[Fleet] Fix inability to upgrade agents from 8.10.4 -> 8.11 (#170974)

## Summary

Closes https://github.com/elastic/kibana/issues/169825

This PR adds logic to Fleet's `/api/agents/available_versions` endpoint
that will ensure we periodically try to fetch from the live product
versions API at https://www.elastic.co/api/product_versions to make sure
we have eventual consistency in the list of available agent versions.

Currently, Kibana relies entirely on a static file generated at build
time from the above API. If the API isn't up-to-date with the latest
agent version (e.g. kibana completed its build before agent), then that
build of Kibana will never "see" the corresponding build of agent.

This API endpoint is cached for two hours to prevent overfetching from
this external API, and from constantly going out to disk to read from
the agent versions file.

## To do
- [x] Update unit tests
- [x] Consider airgapped environments

## On airgapped environments

In airgapped environments, we're going to try and fetch from the
`product_versions` API and that request is going to fail. What we've
seen happen in some environments is that these requests do not "fail
fast" and instead wait until a network timeout is reached.

I'd love to avoid that timeout case and somehow detect airgapped
environments and avoid calling this API at all. However, we don't have a
great deterministic way to know if someone is in an airgapped
environment. The best guess I think we can make is by checking whether
`xpack.fleet.registryUrl` is set to something other than
`https://epr.elastic.co`. Curious if anyone has thoughts on this.

## Screenshots


![image](https://github.com/elastic/kibana/assets/6766512/0906817c-0098-4b67-8791-d06730f450f6)


![image](https://github.com/elastic/kibana/assets/6766512/59e7c132-f568-470f-b48d-53761ddc2fde)


![image](https://github.com/elastic/kibana/assets/6766512/986372df-a90f-48c3-ae24-c3012e8f7730)

## To test

1. Set up Fleet Server + ES + Kibana
2. Spin up a Fleet Server running Agent v8.11.0
3. Enroll an agent running v8.10.4 (I used multipass)
4. Verify the agent can be upgraded from the UI

---------

Co-authored-by: Kibana Machine <42973632+kibanamachine@users.noreply.github.com>

---
## [Janardhankola11/E-Commerce-web-page](https://github.com/Janardhankola11/E-Commerce-web-page)@[bf93df7ed3...](https://github.com/Janardhankola11/E-Commerce-web-page/commit/bf93df7ed36e6f63a103a1a74fba3ebcfe7f8a68)
#### Wednesday 2023-11-29 13:04:11 by Janardhankola11

Add files via upload

Creating an engaging and user-friendly eCommerce webpage involves designing an intuitive interface that seamlessly guides users through product categories, an efficient search functionality, and a secure checkout process. Incorporating visually appealing product displays, high-quality images, and concise yet compelling product descriptions enhances the overall shopping experience. Integration of secure payment gateways, responsive design for mobile compatibility, and personalized recommendations contribute to customer satisfaction. Additionally, optimizing the site for fast loading speeds and incorporating social proof elements like reviews and ratings can further boost trust and encourage conversions.

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[3505e5502b...](https://github.com/TaleStation/TaleStation/commit/3505e5502b4793bfe72148df4477e41c68794c21)
#### Wednesday 2023-11-29 13:21:06 by TaleStationBot

[MIRROR] [MDB IGNORE] Makes oculine taste slightly better (#8785)

Original PR: https://github.com/tgstation/tgstation/pull/79919
-----
## About The Pull Request
Changes oculine's taste from 'dull toxin' to 'earthy bitterness'.
Probably deserves the no GBP tag.
## Why It's Good For The Game
Oculine is a benign/helpful chem that naturally occurs in carrots. This
means it's in all carrot based food the chef cooks, and if the carrots
cross pollinate with another plant it's in those too. This is currently
a problem, because it means the chef's carrot sticks taste like poison
and this tends to freak out new players who don't know that's just what
oculine tastes like.

Oculine has no negative effects besides potentially triggering a medical
allergy quirk, it can't even be overdosed. So if you see a worrying "you
taste dull toxin" message, there's actually no reason to be concerned.
Still, I see players who are *convinced* the chef is poisoning their
carrot cakes fairly regularly. This should cut down on wasted multiver
and lynched chefs.

I changed it to "earthy bitterness" because that's what some species of
carrot taste like, and "bitterness" implies medicine. The paranoid can
still assume they're being dosed with morphine or something, but they're
not being misled into thinking this. For people chugging medicine
bottles from chemistry, oculine stands out a little less too.
## Changelog
:cl:
qol: Oculine now tastes bitter, and not like toxin.
/:cl:

---------

Co-authored-by: Da Cool Boss <142358580+DaCoolBoss@users.noreply.github.com>

---
## [K4rlox/f13babylon](https://github.com/K4rlox/f13babylon)@[ccb9ce38a7...](https://github.com/K4rlox/f13babylon/commit/ccb9ce38a7e26763f93c089bd0a65c9e35b70243)
#### Wednesday 2023-11-29 13:45:29 by panzerr1944

no mans land; kebob changes (#166)

## About The Pull Request

![image](https://github.com/f13babylon/f13babylon/assets/76122712/cb2a0acd-9aa7-4a0c-bc3a-651c2b0104d4)
Kebab now has renegades. And it's loot increased / fixed.


https://github.com/f13babylon/f13babylon/assets/76122712/22a30f2e-354c-4988-8ac7-e39e9fce9c51

## Why It's Good For The Game
NML's town is no longer free loot. Rather, an optional bunker that the
other factions might jump you at. Kind of like normal bunkers in that
way, except with current NML rules you aren't going to lose your
everything. Just your life until someone revives you. I like the no gear
looting in NML rule, it's kinda funny.

## Pre-Merge Checklist
- [ Y ] You tested this on a local server.
- [ Y ] This code did not runtime during testing.
- [ Y ] You documented all of your changes.

## Changelog
ADDED MOBS:
1x pa claw
6x r. docs
3x r. snipers
2x r. meisters
4x r. defenders
6x r. soldiers
10x r. grunts
9x r. prospects
2x r. engies
3x r. guardians
(Total: 46)
REMOVED MOBS:
4x Legendary Ghouls
6x Legendary Mutants
2x Legendary Deathclaws
(Total: 12)
ADDED/EDITED LOOT:
2x Superhigh Ballistic Spawners
1x Mid-High E-Weapon Spawner
1x Mid-High Ballistic Weapon Spawner
1x Mid E-Weapon Spawner
1x Mid Ballistic Spawner
1x NVG Spawner
1x Gauss Rifle Spawner
1x Deluxe Stock Parts Spawner
1x (x10) Strange Seeds Spawner
1x Unique Weapon Spawner
1x High Ballistic Print
1x VHigh Ballistic Print
1x DC Medicine Journal
1x Chemistry Book
1x Random Armor Spawner
1x T4 Armor Spawner
1x Bowl of Fruit
CHANGED TERRAIN / WALLS / MISC:
Sandbags on the main road
Sandbags at the farm and graveyard
Indestructible Walls for south-side to prevent cheese
Replaced see-through airlock with high-sec one in clinic for d-claw
-
Everything else is unedited from current Kebab to my knowledge.

---
## [K4rlox/f13babylon](https://github.com/K4rlox/f13babylon)@[9bc0add065...](https://github.com/K4rlox/f13babylon/commit/9bc0add065315cba3de80a2cc1feac5fe08e9fed)
#### Wednesday 2023-11-29 13:45:29 by Stutternov

Locks Legion Combat Roles to Male Only (+ Other Legion Changes) (#176)

## About The Pull Request

Does the following:
- Locks all combat roles to male only - like they used to be prior to
Sunset changes.
- Locks Priestess of Mars to females only, as is in lore.
- Unlocks servant loadout on slave from being female only (real subtle
there guys)

Tl;dr - Females are relegated to slave, camp follower, auxilla,
forgemaster, or priestess. Males are able to be any role baring
priestess.

This is basically already 'rule enforced' so should just be re-added
code wise anyway.

## Why It's Good For The Game

Fits Fallout lore, the servers lore, and keeps the Legion's faction
design at least faithful to their purpose. (Hate telling people this but
- maybe........ legion aren't good people........)

## Pre-Merge Checklist
<!-- Don't bother filling these in while creating your Pull Request,
just click the checkboxes after the Pull Request is opened and you are
redirected to the page. -->
- [ ] You tested this on a local server.
- [ ] This code did not runtime during testing.
- [ ] You documented all of your changes.
<!-- Neither the compiler nor workflow checks are perfect at detecting
runtimes and errors. It is important to test your code/feature/fix
locally. -->


## Changelog
<!-- This is mostly optional for small Pull Requests, but if you value
being credited for your work in-game be sure to fill it out. To opt-out,
remove everything below including the start and end :cl: brackets. -->

<!-- If your Pull Request includes a minor single line variable edit,
probably do not fill out this changelog. -->
<!-- However, if your pull request includes massive or immediately
noticeable changes, briefly describe those changes in some way in this
changelog. -->

:cl:
adds: Locks roles in Legion based off gender restrictions.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [K4rlox/f13babylon](https://github.com/K4rlox/f13babylon)@[a2491a3c89...](https://github.com/K4rlox/f13babylon/commit/a2491a3c89e4fa54e2c112902162278493f10945)
#### Wednesday 2023-11-29 13:45:29 by Mazzinsanity

Enables Podpeople as a Roundstart Species (May need to be enabled on the box) (#194)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

<!-- NOTE: This format is NOT REQUIRED for things like runtime fixes,
code fixes and optimizations. In those instances you should try to give
a description of what is being fixed or optimized but are not required
to fill out the complete changelog. -->
<!-- Adjusting things like armor or weapon values for balance, while
they may be 'fixes' in their own way, are not considered code fixes as
described above and require the use of the Pull Request format below.-->


## About The Pull Request

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->
Makes a WEAKENED version of Podpeople selectable as a roundstart
species. Their maluses and bonuses are as follows:
- 1.25 damage modifiers for Brute/Burn
- Restore 2 hunger and heal 0.2 Brute, 0.2 Burn, 0.1 Toxin when in
light.
- Reverse effects in darkness.

Changes podpeople bloodtype to EZ Nutrient
## Why It's Good For The Game
This lets people play as anthropomorphic Broc flowers.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Pre-Merge Checklist
<!-- Don't bother filling these in while creating your Pull Request,
just click the checkboxes after the Pull Request is opened and you are
redirected to the page. -->
- [x] You tested this on a local server.
- [x] This code did not runtime during testing.
- [x] You documented all of your changes.
<!-- Neither the compiler nor workflow checks are perfect at detecting
runtimes and errors. It is important to test your code/feature/fix
locally. -->


## Changelog
<!-- This is mostly optional for small Pull Requests, but if you value
being credited for your work in-game be sure to fill it out. To opt-out,
remove everything below including the start and end :cl: brackets. -->

<!-- If your Pull Request includes a minor single line variable edit,
probably do not fill out this changelog. -->
<!-- However, if your pull request includes massive or immediately
noticeable changes, briefly describe those changes in some way in this
changelog. -->

:cl:
add: enabled podpeople as a roundstart species
balance: rebalanced weak podpeople healing
tweak: changed podpeople bloodtype to EZ Nutrient
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [WinstonBeYY/PsychonautStation](https://github.com/WinstonBeYY/PsychonautStation)@[31afabc9af...](https://github.com/WinstonBeYY/PsychonautStation/commit/31afabc9afae2252fc22958d07f12f7148d6963d)
#### Wednesday 2023-11-29 14:17:50 by Jacquerel

Adds missing default biotypes to some damage procs (#79102)

## About The Pull Request

I noticed by complete coincidence because I happened to glance at the
channel a bunch of people complaining about blobbernauts not taking any
damage when leaving the blob in manuel round end chat.
Did anyone report this bug, even after prompting? No. Not even the game
admin who was playing as the blob.

Makes you wonder how many other bugs people are perfectly willing to
spend 15 minutes posting "i fucking hate coders" about without actually
telling anyone they exist. Sucks to be them I guess.

Anyone the cause is that some of these procs didn't have a default
biotype, so they would never take the toxin damage they were being
assigned. Now they will.

## Changelog

:cl:
fix: Blobbernauts will once again take damage when not on blob tiles.
/:cl:

---
## [WinstonBeYY/PsychonautStation](https://github.com/WinstonBeYY/PsychonautStation)@[ece51a1a9d...](https://github.com/WinstonBeYY/PsychonautStation/commit/ece51a1a9d6896a54b878563d9c33002bc8f3688)
#### Wednesday 2023-11-29 14:17:50 by nikothedude

[NO GBP] Fixes scream for me, and also fixes literally EVERY INSTANCE of non-random puncture wounds (#79043)

## About The Pull Request

Closes https://github.com/tgstation/tgstation/issues/79017

So turns out, I

1. Had a pair of inverted more/less than operators in a crucial area. I
DONT KNOW HOW THIS WORKED. SHIT is a FUCKING mystery.
2. Used a non-existant define which DM converted into a string because
Byond
## Why It's Good For The Game

bugsgs badagfd
## Changelog
:cl:
fix: Scream for me, the spell, now works
fix: Non-random puncture wounds can now be applied
/:cl:

---------

Co-authored-by: Ghom <42542238+Ghommie@users.noreply.github.com>

---
## [SSensum/tgstation](https://github.com/SSensum/tgstation)@[ef52047274...](https://github.com/SSensum/tgstation/commit/ef520472740e57f253545c24c7526e45e47b5ec2)
#### Wednesday 2023-11-29 14:26:46 by necromanceranne

[READY] The Tackleling: Unarmed bonuses and features contribute to tackle success and failure, significant outcome overhaul, among other things (#79721)

## About The Pull Request

### Tackling Outcomes

Tackling now determines success based on outcome categories. These are
derived from the typical attacker/defender roll that would have
previously determined the outcome on its own. A negative roll results in
a negative outcome, a positive roll a positive outcome, and a result of
exactly 0 resulting in a neutral outcome.

The result of your roll are then passed along to the relevant proc to
determine severity. The derived roll is multiplied by 10 (or -10 for the
negative roll to get a positive value to roll with). Then we see if our
final roll fits a severity bracket. Negative outcomes will roll to
determine their outcome, and potentially could roll a less severe
outcome than what our first roll would suggest.

For positive outcomes, the defender's melee armor reduces the severity
of the outcome.
For negative outcomes, the attacker's melee armor improves the potential
outcome and at least prevents more severe backlash. It'll still be
negative, you can't move from a negative outcome to a positive outcome
just from good armor.

Most of the outcomes are fairly similar to the current outcomes, but
with the inclusion of staggering one or both parties to make the
subsequent potential grabs _stickier_, if that makes sense.

Neutral is now a mutual stagger, but also the tackler being left
upright. It's effectively net zero.

### Blocking

Blocking is checked on impact, and results in a neutral outcome if the
defender successfully blocks. This means our tackler isn't too severely
impacted from an unsuccessful tackle

### Additional Changes

Your arms ``unarmed_effectiveness`` now contributes to the attack mod
and defense mod of tackles. For humans tackling humans, this often
results in a net neutral result. But if you have a better arm, or the
tackle target has worse arms, this can alter the outcome significantly.

Any tackler with the trait TRAIT_NOGUNS (like bezerkers, Sleeping Carp
users or the very unlikely chance ninjas are tackling while wearing
their armor) gains a bonus to their tackles.

Any suit that prevents shove knockdowns grants an attack bonus, and not
just riot armor. This now includes Mk.1 Swat suits, the ones from the
SWAT crate in cargo.

Settlers are vulnerable to tackles, much like their dwarf cousins.
They're also just as bad at tackles.

Security lockers come with gripper gloves, and the sec vendor has 5 sets
of gripper gloves as standard items. They also have a +1 skill bonus.
This should encourage people to use tackling a bit more without having
to always seek out the best gear to accomplish the task. (particularly
since security is inherently pretty good at tackling with the outcome
changes).

The HoS gets a pair of gorilla gloves in his garment bag. If he wants
them.

The shove slowdown is now a new status effect, Staggered. This is just
better functionality overall. Any instance of adding the shove slowdown
now makes our target staggered.

## Why It's Good For The Game

Tackling is a bit outdated, to say the least. Not much content has been
added for a while that isn't strictly meme content. With these changes,
tackling should be slightly more nuanced, considering elements such as
unarmed effectiveness, the presence of martial arts, and actually
properly checking block rather than notionally checking block. There is
also more opportunity to protect yourself from tackle outcomes, both
positive and negative.

It also should be a little fairer to be on the receiving end of tackles
if you have taken the time to layer up defenses against it. Attackers
often overwhelmed defenders due to numbers favoring attackers more than
defenders.

Closes some really outdated design that was resulting in some really
bizarre behaviour with regards to layered defenses against attack not
having the same meaning against tackles, if only because it was looking
for the wrong things and not even the correct parts of what it was
looking for. Namely, blocking and shielding.

The inclusion of more gripper gloves and a good outcome from using them
will hopefully incentivize people to consider tacking as a useful tool,
if a bit risky still due to the splat mechanics.

## Changelog
:cl:
balance: Judo Joe, archnemesis of Maint Khan, has begun re-airing his
midnight infomercials shilling his extremely expensive Tackle Supreme
Judo Karate Training video tapes. Unable to pass up a 'bargain',
Nanotrasen has purchased these tapes en masse. Tackling techniques have
started to improve, as well as Nanotrasen's tackling instructional
algorithms within tackle gloves.
balance: The outcomes for tackling are more equalized. It isn't as feast
or famine, and should be somewhat more controllable without becoming too
severe.
add: Blocking successfully against a tackle will force the tackle to be
a neutral outcome.
add: Unarmed effectiveness from arms now contributes to attacking with
and defending from tackles.
add: Those who refuse to use firearms (like Sleeping Carp users and
insane unholy berzerkers) are better at tackling others.
add: Riot specialized armor, and not just riot armor, now contributes
meaningfully to tackling effectiveness.
balance: MK.1 Swat Suits, the ones that come in SWAT crates, now
functions similarly to riot armor.
add: Settlers from the outer rims have noticed they aren't very good at
protecting themselves against Judo Joe's clearly discriminatory tackling
techniques.
add: Security lockers come with gripper gloves, security vendors now
sell them as standard items, and the HoS' garment bag now has a pair of
gorilla gloves. Gripper gloves have a positive skill bonus to tackling.
add: Being insane also makes you INSANELY good at tackling but also
INSANELY likely to eat shit on a whiff. DO OR DIE, BITCH.
refactor: Shoving slowdown and all its implementations now use a status
effect, Staggered.
/:cl:

---
## [MKLab-ITI/hugomklab](https://github.com/MKLab-ITI/hugomklab)@[6faa299482...](https://github.com/MKLab-ITI/hugomklab/commit/6faa29948282d0661001efede487d0f05703668b)
#### Wednesday 2023-11-29 15:02:42 by thalakidiama

Update Publication “2022-05-06-water-quality-issues-can-we-detect-a-creeping-crisis-with-social-media-data”

---
## [R-JunmingChen/arrow](https://github.com/R-JunmingChen/arrow)@[3beb93af36...](https://github.com/R-JunmingChen/arrow/commit/3beb93af36b3388a6871846365502c36ae4cfaa4)
#### Wednesday 2023-11-29 16:05:28 by Kevin Gurney

GH-37815: [MATLAB] Add `arrow.array.ListArray` MATLAB class (#38357)

### Rationale for this change

Now that many of the commonly-used "primitive" array types have been added to the MATLAB interface, we can implement an `arrow.array.ListArray` class.

This pull request adds a new `arrow.array.ListArray` class which can be converted to a MATLAB `cell` array by calling the static `toMATLAB` method.

### What changes are included in this PR?

1. Added a new `arrow.array.ListArray` MATLAB class.

*Methods*

`cellArray = arrow.array.ListArray.toMATLAB()`
`listArray = arrow.array.ListArray.fromArrays(offsets, values)`

*Properties*

`Offsets` - `Int32Array` list offsets (uses zero-based indexing)
`Values` - Array of values in the list (supports nesting)

2. Added a new `arrow.type.traits.ListTraits` MATLAB class.

**Example**
```matlab
>> offsets = arrow.array(int32([0, 2, 3, 7]))

offsets = 

[
  0,
  2,
  3,
  7
]

>> values = arrow.array(["A", "B", "C", "D", "E", "F", "G"])

values = 

[
  "A",
  "B",
  "C",
  "D",
  "E",
  "F",
  "G"
]

>> arrowArray = arrow.array.ListArray.fromArrays(offsets, values)

arrowArray = 

[
  [
    "A",
    "B"
  ],
  [
    "C"
  ],
  [
    "D",
    "E",
    "F",
    "G"
  ]
]

>> matlabArray = arrowArray.toMATLAB()

matlabArray =

  3x1 cell array

    {2x1 string}
    {["C"     ]}
    {4x1 string}

>> matlabArray{:}

ans = 

  2x1 string array

    "A"
    "B"

ans = 

    "C"

ans = 

  4x1 string array

    "D"
    "E"
    "F"
    "G"

```

### Are these changes tested?

Yes.

1. Added a new `tListArray.m` test class.
2. Added a new `tListTraits.m` test class.
3. Updated `arrow.internal.test.tabular.createAllSupportedArrayTypes` to include `ListArray`.

### Are there any user-facing changes?

Yes.

1. Users can now create an `arrow.array.ListArray` from an `offsets` and `values` array by calling the static `arrow.array.ListArray.fromArrays(offsets, values)` method. `ListArray`s can be converted into MATLAB `cell` arrays by calling the static `arrow.array.ListArray.toMATLAB` method.

### Notes

1. We chose to use the "missing-class" `missing` value as the `NullSubstitutionValue` for the time being for `ListArray`. However, we eventually want to add `arrow.array.NullArray`, and will most likely want to use the "missing-class" `missing` value to represent `NullArray` values in MATLAB. So, this could cause some ambiguity in the future. We have been thinking about whether we should consider introducing some sort of special "sentinel value" to represent null values when converting to MATLAB `cell` arrays. Perhaps, something like `arrow.Null`, or something to that effect, in order to avoid this ambiguity. If we think it makes sense to do that, we may want to retroactively change the `NullSubstitutionValue` to be `arrow.Null` and break compatibility. Since we are still in pre-`0.1`, we don't think the impact of such a behavior change would be very large.
2. Implementing `ListArray` is fairly involved. So, in the spirit of incremental delivery, we chose not to include an implementation of `arrow.array.ListArray.fromMATLAB` in this initial pull request. We plan on following up with some more changes to `arrow.array.ListArray`. See #38353, #38354, and #38361.
3. Thank you @ sgilmore10 for your help with this pull request!

### Future Directions

1. #38353
2. #38354
3. #38361
4. Consider adding a null sentinel value like `arrow.Null` for conversion to MATLAB `cell` arrays.
* Closes: #37815 

Lead-authored-by: Kevin Gurney <kgurney@mathworks.com>
Co-authored-by: Sarah Gilmore <sgilmore@mathworks.com>
Signed-off-by: Kevin Gurney <kgurney@mathworks.com>

---
## [damonitor/linux](https://github.com/damonitor/linux)@[b460d9625f...](https://github.com/damonitor/linux/commit/b460d9625f14e5285c6444ca7b153ca8d260e785)
#### Wednesday 2023-11-29 16:06:32 by SeongJae Park

==== DAMOS: Introduce Aim-Oriented Feedback-driven Quota Auto Tuning ====

Subject: [PATCH] mm/damon: Let users feed and tame DAMOS

Introduce a new way for tuning DAMOS, namely aim-oriented
feedback-driven aggressiveness auto tuning.  It allows users repeatedly
tell DAMOS how far it is from the users' aiming goal.  Based on the
feedback, DAMOS self-adjusts its aggressiveness to meet the goal.

Patchset Changelog
==================

From RFC
(https://lore.kernel.org/damon/20231112194607.61399-1-sj@kernel.org/)
- Wordsmith commit messages and cover letter

DAMOS Control Difficulty
========================

DAMOS helps users easily implementing access pattern aware system
operations.  However, controlling DAMOS in wild is not that easy.

The basic way for DAMOS control is specifying the target access pattern.
In this approach, the user is assumed to well understanding the access
pattern and the characteristic of the system and the workloads.  Though
some good tools including DAMON can help that, it requires time and
resource depending on the complexity and the dynamicity of the system
and workloads.  After all, the access pattern consists of three ranges,
namely access rate, age, and size of the regions.  It means users need
to tune six parameters.  Tuning six parameters itself is not simple.

To let users at least avoid the worst case, DAMOS allows users to set
the upper-limit of the schemes's aggressiveness, namely DAMOS quota.
DAMOS further provides its best-effort under the limit by prioritizing
regions based on the access pattern of the regions.  For example, users
can ask DAMOS to page out up to 100 MiB of memory regions per second.
Then DAMOS pages out regions that not accessed longer time (colder)
first under the limit.  This allows users to set access pattern bit
naively, and focus on only the one parameter, the quota.  In other
words, the number of parameters to tune with special care can be reduced
from six to one.

Still, however, the optimum value for the quota depends on the system
and the workloads' characteristics, so not that simple.  The number of
parameters to tune can also increase again if the user needs to run
multiple schemes.

Aim-oriented Feedback-driven DAMOS Quota Auto Tuning
====================================================

Most users would start using DAMOS since there is something they want to
achieve using DAMOS.  Asking users to inform DAMOS their aim of the use,
and how close DAMOS is achieving it could be a reasonable request.
Having measurable metrics and the target values of the metric that
represents such information (e.g., SLO) is indeed not rare in the
industry.  Then, DAMOS could tune its aggressiveness, namely the quota,
on its own, based on the users' feedback and the current aggressiveness.
This patchset implements the idea.

Implementation
--------------

The implementation asks users to represent the feedback with score
numbers.  The scores could be anything including user-space specific
metrics like latency/throughput of special user-space workloads, and
system metrics like free memory ratio, memory pressure stall time (PSI),
and/or active to inactive memory ratio.

The feedback scroes and the aggressiveness of the given DAMOS scheme are
assumed to be positively proportional, though.  Selecting metrics of the
assumption is the users' responsibility.

The core logic implementation uses below simple feedback loop algorithm.
It gets next aggressiveness of the scheme from the current
aggressiveness and the feedback (target_score and current_score) for the
current aggressiveness.  It calculates the compensation for next
aggressiveness as a proportion of current aggressiveness and distance to
the target score.  As a result, it fastly goes close to the goal using
big steps when its far from the goal, but avoid making mistakes using
small steps whne its near to the goal.

    f(n) = max(1, f(n - 1) * ((target_score - current_score) / target_score + 1))

Example Use Cases
-----------------

If users want to reduce memory footprint of the system as much as
possible as long as the time spent for handling the resulting memory
pressure is within a threshold, they could use DAMOS scheme that
reclaims cold memory regions while setting the memory pressure stall
time of the threshold as the goal, and repeatedly provide the current
memory pressure stall time ratio as the feedback.

If users want to avoid reclamation when there is no memory pressure but
want the active/inactive LRU lists well balanced to reduce the
performance impact due to possible memory pressure, they could use two
schemes.  The first one would set to locate hot pages in active LRU
list, aiming specific active-to-inactive LRU list size ratio, say, 70%.
The second one would set to locate cold pages in inactive LRU list,
aiming specific inactive-to-active LRU list size ratio, say, 30%.  Then,
DAMOS will balance the two schemes based on the goal and feedback.  As a
result, in this example, DAMOS will make active LRU list to have hottest
70% of memory in use, and therefore protect the 70% hottest memory from
future memory pressure.

It could also be useful for general balancing-required access aware
system operations such as system memory auto scalaing[3] and tiered
memory management[4].  The example usages would need additional DAMOS
action developments, though.

Evaluation: PSI-based proactive reclamation auto tuning
-------------------------------------------------------

To show if the implementation works as expected, we prepare four
different system configurations on AWS i3.metal instances.  The first
setup (original) runs the workload without any DAMOS scheme.  The second
setup (not-tuned) runs the workload with virtual address space-based
proactive reclamation scheme that pages out memory regions that not
accessed for five seconds or more.  The third setup (offline-tuned) runs
the same proactive reclamation DAMOS scheme, but after making it tuned
for each workload in offline, using our previous user-space driven
automatic tuning approach, namely DAMOOS[1].  The fourth and final setup
(online-tuned) runs the scheme that same to that of 'not-tuned' setup,
but making DAMOS to do online auto-tuning, aiming 0.5% of 'some' memory
pressure stall time (PSI) per 10 seconds.

For each setup, we run realistic workloads from PARSEC3 and SPLASH-2X
benchmark suites.  For each run, we measure RSS and runtime of the
workload, and 'some' memory pressure stall time (PSI) of the system.
We repeat the runs five times and use averaged measurements.

For simple comparison of the results, we normalize the measurements to
those of 'original'.  In case of the PSI, though, the measurement for
'original' was zero, so we normalize the value to that of 'not-tuned'
scheme's result.  The normalized results are shown below.

            Not-tuned         Offline-tuned     Online-tuned
    RSS     0.622688178226118 0.787950678944904 0.740093483278979
    runtime 1.11767826657912  1.0564674983585   1.0910833880499
    PSI     1                 0.727521443794069 0.308498846350299

The 'not-tuned' scheme acheives about 38.7% memory saving but incur about
11.7% runtime slowdown.  The offline-tuned scheme achieves about 22.2%
memory saving with about 5.5% runtiem slowdown.  It also achieves about
28.2% memory pressure stall time saving.  The online-tuned scheme
achieves about 26% memory saving with about 9.1% runtime slowdown.  It
also achieves about 69.1% memory pressure stall time saving.  We repeat
this test multiple times, and get consistent results.

Apparently the aggressiveness of 'online-tuned' setup is somewhere
between those of 'not-tuned' and 'offline-tuned' setup, since its memory
saving and runtime overhead are between those of the other two setups.
The difference in memory saving and performance degradation are not
significant, though.  Actually we set the memory pressure stall time
goal aiming this middle aggressiveness.  However, it shows significant
saving of the memory pressure stall time, which was the goal of the
auto-tuning, among the three variants.  Hence, we conclude the automatic
tuning is working as expected.

Please note that the setup may not appropriate for production
environment.  In production, less memory pressure stall time would be
more appropriate to be set as a goal.

The test code is also available[2], so you could reproduce it on your
system and workloads.

Patches Sequence
================

The first four patches implement the core logic and user interfaces for
the auto tuning.  The first patch implements the core logic for the auto
tuning, and the API for DAMOS users in the kernel space.  The second
patch implements basic file operations of DAMON sysfs directories and
files that will be used for setting the goals and providing the
feedback.  The third patch connects the quota goals files inputs to the
DAMOS core logic.  Finally the fourth patch implements a dedicated DAMOS
sysfs command for efficiently committing the quota goals feedback.

Two patches for simple test of the logic and interfaces follow.  The
fifth patch implements the core logic unit test.  The sixth patch
implements a selftest for the DAMON Sysfs interface for the goals.

Finally, two patches for documentation follows.  The seventh patch
documents the design of the feature.  The final eighth patch updates the
usage document for the features.

References
==========

[1] DAOS paper:
    https://www.amazon.science/publications/daos-data-access-aware-operating-system
[2] Evaluation code:
    https://github.com/damonitor/damon-tests/commit/3f884e61193f0166b8724554b6d06b0c449a712d
[3] Memory auto scaling RFC idea:
    https://lore.kernel.org/damon/20231112195114.61474-1-sj@kernel.org/
[4] DAMON-based tiered memory management RFC idea:
    https://lore.kernel.org/damon/20231112195602.61525-1-sj@kernel.org/

Signed-off-by: SeongJae Park <sj@kernel.org>

---
## [Maybe-Anton/Shiptest](https://github.com/Maybe-Anton/Shiptest)@[70463ae71b...](https://github.com/Maybe-Anton/Shiptest/commit/70463ae71b7d639eecea572d3251562c5ffef68b)
#### Wednesday 2023-11-29 16:22:13 by Mirag1993

Reworks The Visuals Of Independent And Nanotrasen Captains (#2453)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

Does what it says in the title. This is a demented PR that touches a lot
of things, but its main benefit is that now regular independent
captains, cowboy independent captains, and nanotrasen captains have a
unique identity.

Of those changed, it includes:

- The Nanotrasen Captain (parade)

![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/48a31cb1-b266-43cb-9b6e-525028893011)

- The Nanotrasen Captain (regular)

![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/799c88f0-b7ce-4736-956d-2e9c0a096433)

- The Independent Captain (regular/parade)

![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/17ecb3d3-5f2f-4ce0-a518-81366945ebdf)

- The Independent Captain (western)

![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/a56a798c-5adf-41d7-917a-730661f306ed)

The PR also axes a bunch of unused, or frankly quite basic lieutenant
outfits that were nothing more than set dressing with not much substance
behind them. The roles were not removed for now, and they have
appropriate outfits as a placeholder pending a full removal.

This also means that the Head of Personnel was slightly touched up,
mostly by having a coat and hat similar to the western captain's when
appropriate. The role itself is pending a full visual rework for later
that is beyond the scope of this PR.

Speaking of removals, this also means that captain outfits/roles that
were there as a legacy of removed ships, were finally axed for good.
Goodbye deserter captain for Riggs variant number 4, you will not be
missed.

This PR also touches several (a lot) of maps, mostly adding/removing
outfits that were either missing, or didn't fit with the dress code of
the vessel.

Also the PR fixes an oversight by @MarkSuckerberg by making the BYOND
version warning an actual warning, instead of an error when compiling.
Etto bleh.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

Visual cohesion is important, and dear fucking god if I see one more
independent western captain not wearing the duster because it wasn't in
the ship, I will weep, and my weeping will cause a biblical deluge.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

:cl: PositiveEntropy
imageadd: Outfits for independent and Nanotrasen captains have been
violently reworked.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Opentrons/opentrons](https://github.com/Opentrons/opentrons)@[30425f7a3b...](https://github.com/Opentrons/opentrons/commit/30425f7a3bd4a7ddb8ba9d3c14b05cdff13ccf34)
#### Wednesday 2023-11-29 17:32:08 by Seth Foster

feat(app): Update robots from USB flash drive (#13923)

* feat(app-shell-odd): watch for USB drives

The Flex operating system automatically mounts the filesystems of
well-formatted USB drives (FAT and ext4 and maybe ntfs but that's a bit
iffy) to /media when those USB drives are inserted on the robot. In
theory it will in fact do this for _any_ kind of media that presents a
filesystem interface.

To that end, add a node task that will use a node filesystem watch to
keep an eye on /media, and
- when something that looks like a USB drive (/media/sd\w\d+) appears,
notify via redux actions
   - then enumerate all the files on it and notify those via redux
   actions
- when something we were keeping an eye on disappears, notify via
redux actions

The redux actions don't alter state and so don't need new reducers or
selectors; they exist because it's a handy mechanism to talk between our
components.

This code is very tightly coupled to the way the node fs interfaces work
and so I don't see a lot of point in unit tests for it; it's almost
entirely fs calls originating everything and providing all of the data,
and all the complexity is from working around weirdnesses in those calls
and in the underlying system. For instance,
- There's a little bit of time in between when the fs watch on /media
fires and when you can actually find the contents of the newly-present
directory; if you readdir before that you'll get an empty list, so we
wait a second
- The node fs.watch interface looks very fully features but is
absolutely chock-full of warnings about various features not being
reliable. A lot of that unreliability is _probably_ across systems and
everything works as we expect on linux, but just in case we have a lot
of fallbacks for if our callback doesn't get filepaths, etc

* fix(app-shell-odd): handle errors in readstreams in http.post

We have our custom http interface that wraps around node-fetch that
provides things like "doing your own read stream when posting a file",
and "mapping everything into the promise interface", which is nice,
but has an issue specifically for that read stream: we don't monitor
errors on it. Read streams surface errors by emitting an 'error' event;
we hook up a listener to that error event _while we're creating the
stream_, but then we disconnect it. So if you have an error in the
stream - for instance, you're reading from a file on a USB flash drive
and the user unplugs the flash drive - then the error will never get
surfaced.

Unfortunately the fix to this is a bit fiddly. We can hook up an error
listener fine, but it needs to do something; specifically, it needs to
turn the error from a callback into a promise rejection. That means it
needs to have a promise to reject that has the same lifetime as the
stream itself. http.post didn't provide that because it returns a whole
big promise chain, and each time you move a link in that chain the old
promise is gone and a new one happens, so we'd need to move the listener
around.

Since promises are monadic, a better fix is to have post return a single
promise and do all the promise chaining _inside_ that promise; then, the
read stream error handler can reject the outer promise directly, while
relying on promises bubbling up rejections to preserve error handling
capability for the promises in the internal chain.

* fix(app): Poll for updates on the ODD

Though we have everything set up to automatically fetch, prompt for, and
execute robot updates from the ODD, we weren't actually _checking_ for
those updates except once on boot (which then wouldn't work if the robot
wasn't internet-connected during boot). This means in particular that
the software updates during onboarding were guaranteed to fail.

We can use the same hook in the ODD app root that we do in the desktop
app route, but if we're going to do that then we better remove a log
message that suddenly becomes extremely spammy.

* feat(app-shell-odd): Supply "system updates" from flash drives

Adds the capability to provide system updates from flash drives to the
ODD app-shell.

These are "system updates" in that the app-shell determines their
availability and provides it to the app, rather than the user indicating
the presence of a file alongside their intent to update. The app-shell
will advertise the flash drive updates in the same way it advertises
internet-discovered updates, with a RobotUpdateInfo redux message; since
those now provide the path to the file they mean, it will be easy for
the app to specify the system update to load.

We can duplicate the logic that we use for system updates by adding a
second let cache for the "current update"; the system-updates code will
then prefer an update in the mass storage update cache to an update in
the old system updates cache, and send new robot update info messages in
all the state changes between neither cache being full; either cache
being full; and both caches being full.

The determination that a flash drive system update is present is
triggered by a mass storage enumerated message; when that flash drive
gets removed, we'll get a removal message.

To figure out whether updates are actually present, we can the list of
files that just got enumerated for things that end with .zip, and then
try to open them as zip files and read the VERSION.json information out
of them. This is a somewhat fraught process; the file could not be a zip
file, it could be a zip file but corrupted, it could be a zip file but
not an update, it could be an update but it's for an OT-2,  and we need
to handle all that, so there's a pretty excessive amount of error
handling in here. Once we're sure that there are one or more zip files
containing robot system updates, we can provide something to redux; we
provide the highest-version update present.

There is one way in which updates from flash drives differ from system
updates found on the internet, however: plugging in a flash drive
requires user intent, while checking for updates on the internet
doesn't. Therefore, if the user plugs in a flash drive with an update
file, we always want to make that update file available no matter the
relative versions of the robot and the update file. So we can add a bool
to the system update message (and then to the update state) that shows
that this is a "forced notification" update, and the app can know to
display it without caring about the upgrade/downgrade/reinstall state.

Since there's a lot of duplication, we can also factor out some common
logic to make it feel a little better.

That process of duplication also fixes a bug that would have prevented
the ODD from ever prompting for updates. The function that gets
information about updates used the same promise to read the release
notes and provide the update information; but we overrode the downloaded
release files to null out the release notes, meaning that promise would
always fail, and we'd never get the notification. We no longer override
the release notes to be null, and we also treat reading the release
notes separately from reading the rest of the update.

* feat(app): allow robot updates from USB files

Now that the odd app-shell provides us with notifications of updates
from USB flash drives, we can allow the user to install them. While the
redux mechanisms allow this pretty easily - a system update is a system
update, after all, and with the force mechanism the app wouldn't even
know if the update was a downgrade or anything - we ran into a problem
where the general robot update machinery in the ODD was very tightly
bound with the onboarding experience for the ODD, since that's the
context in which it was developed.

This commit extracts the robot update mechanisms from onboarding by
- Hoisting onboarding-related logic out of lower level components and
instead injecting that logic into the organisms code from the top level
page
- Moving the current update page to a new one that is focused on
onboarding at a new route, and copying just the update-related code to
a generic RobotUpdate page

This means that the two pages - RobotUpdate and
RobotUpdateDuringOnboarding - share most of the same code but are bound
to different routes and can have different top level behavior by
injecting different contexts to the finish and error handling behaviors
of the update. RobotUpdateDuringOnboarding sets the unfinished
onboarding page breadcrumbs appropriately, and uses display language
appropriate to the update being just a component of the larger workflow,
and moves on to estop handling when cancelled; RobotUpdate doesn't touch
any of that, and goes back to the settings page when cancelled, and uses
wording more appropriate to being its own topline flow.

Closes RAUT-829

---
## [blocovermelho/mod](https://github.com/blocovermelho/mod)@[cdbb6321d9...](https://github.com/blocovermelho/mod/commit/cdbb6321d94376ce5814fb9a3c51a9fabc11b430)
#### Wednesday 2023-11-29 17:40:37 by Alice Isabel

Use shadowJar instead of includeApi

For whatever reason it doesn't work for me, and what it matters most is that it works. If its unsupported or, dare I say "legacy", I don't care.

If it compiles it's good. I'd commit crimes to have cargo on kotlin, I swear to god that gradle may have led people to insanity at best, suicide at worst.

And the worst part is that it's not the worst offender, java build tools can always get worse.

---
## [mattirizarry/CS360-Project](https://github.com/mattirizarry/CS360-Project)@[bf4b1f33ee...](https://github.com/mattirizarry/CS360-Project/commit/bf4b1f33ee7eae8893a224b1c46119560b9eed31)
#### Wednesday 2023-11-29 17:48:06 by Matthew Irizarry

I think i fucking finally fixed the god damn firebase issues.

---
## [Arman1817/Skill-Sync-Interns-Web-Development](https://github.com/Arman1817/Skill-Sync-Interns-Web-Development)@[f915f945c0...](https://github.com/Arman1817/Skill-Sync-Interns-Web-Development/commit/f915f945c0c47b9a06c7cc4f6678a5941e232b58)
#### Wednesday 2023-11-29 18:39:55 by Arman Salmani

Add files via upload

In Task 3, we dedicated our efforts to crafting a visually stunning and user-friendly interface that mirrors the Netflix magic. 🎬✨

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[4372be3bd4...](https://github.com/TaleStation/TaleStation/commit/4372be3bd4d69572d2ca16cb2063d6cb0953c7e8)
#### Wednesday 2023-11-29 19:31:44 by TaleStationBot

[MIRROR] [MDB IGNORE] The Inversenning : Superior Healing Medications (#8826)

Original PR: https://github.com/tgstation/tgstation/pull/79342
-----
## About The Pull Request

Please read the contents of my HackMD to see what my PR does, as well as
further elaboration on why it's good for the game.

https://hackmd.io/MGO/r1idU4cza

## Contents
Introducing new inverse reagents for existing superior healing
medications! This push includes...

**Benzoic Acid** : Inverse of Salicylic Acid. Robust fertilizer that
provides a decent range of benefits for plant life.

![ss13-1](https://github.com/tgstation/tgstation/assets/97645027/6d624397-f860-47f2-9702-a073c2a936c2)

**Oxymetholone** : Inverse of Oxandrolone. Anabolic steroid that
promotes the growth of muscle during and after exercise.

![ss13-2](https://github.com/tgstation/tgstation/assets/97645027/4a4c941a-e5d1-4aed-9785-9c0f702ede2a)

**Bamethan** : Inverse of Salbutamol. Blood thinner that drastically
increases the chance of receiving bleeding wounds.

![ss13-3](https://github.com/tgstation/tgstation/assets/97645027/1ae9c6be-a181-42e6-b2e4-45e7dbee694e)

**Pendetide** : Inverse of Pentetic Acid. An unusual bioradioactive drug
that purges basic radiation healing chems. Also increases the severity
of radiation poisoning.

![ss13-4](https://github.com/tgstation/tgstation/assets/97645027/6ad81590-69bb-4f09-b166-1e34c5db168a)

**Hyoscyamine** : Inverse of Atropine. Heals heart and stomach damage,
and slowly removes minor toxin damage.

![ss13-7](https://github.com/tgstation/tgstation/assets/97645027/5823d8dd-11d6-4225-96e6-2ace673474a4)

**Ammoniated Sludge** : Inverse of Ammoniated Mercury. A ghastly looking
mess of mercury by-product which causes bursts of manic hysteria.

![ss13-6](https://github.com/tgstation/tgstation/assets/97645027/a1966766-673d-49cc-a3f0-f103d733c7b5)

**Inreziniver** : Inverse of Rezadone. Makes the user horribly afraid of
all things related to carps.

![ss13-8](https://github.com/tgstation/tgstation/assets/97645027/1e6f926b-50d3-47c7-bdde-60cb5da6409a)

## Why It's Good For The Game

This is an effort to add more variety to the existing inverse reagent
system within chemistry. Not only should this variety serve to provide
additional options for a Chemist to experiment with, they should also
broaden the possibilities for already existing strategies.

## Changelog
:cl:MGO
add: Introduces new inverse reagents for Salicylic Acid, Oxandrolone,
Salbutamol, Pentetic Acid, Atropine, Ammoniated Mercury and Rezadone!
/:cl:

---------

Co-authored-by: MGOOOOOO <97645027+MGOOOOOO@users.noreply.github.com>

---
## [RatiuCristian1/handyMan](https://github.com/RatiuCristian1/handyMan)@[e1ac07bd03...](https://github.com/RatiuCristian1/handyMan/commit/e1ac07bd03581d75d72b1498b913a83a77a3ced8)
#### Wednesday 2023-11-29 20:13:35 by Cristian Ratiu

Fuck this stupid fucking piece of shit world with the fucking chat-gpt FUUUUUCKKKKKK

---
## [mlads15/atividades-3-bimestre-algoritmos](https://github.com/mlads15/atividades-3-bimestre-algoritmos)@[8f4c48d0df...](https://github.com/mlads15/atividades-3-bimestre-algoritmos/commit/8f4c48d0df0aaece8908c092c907859abb1f12f7)
#### Wednesday 2023-11-29 20:55:07 by luiza

Create html atualizado naosei

?????????????? didnt work but um nvm imma just live w that bc thats how live works and i might ask for help but im not sure bc im a egoist dumb bitch that doesnt know how to ask for help bc i want to do things on my own and um that literally makes me flunk in every disciple at school EVER and well imma get killed by my that haha thats so funny isnt it :D HAHAHAHAHHAHAHAHHAHAHHAHAHAHHAHAHAHAHHAHAHAHAHHAHAHAHHAHA

---
## [yevagami/Midstone-Flat-Eathers](https://github.com/yevagami/Midstone-Flat-Eathers)@[787a599d4f...](https://github.com/yevagami/Midstone-Flat-Eathers/commit/787a599d4ff6586ce8d703754bb15fb1167f4847)
#### Wednesday 2023-11-29 20:59:58 by worflor

tons of mini things

1. added a defaultHealth variable in Body
2. removed ALL HEALTH FROM PLAYERBODY as its literally in Body and did nothing
3. changed the takeDamage to temp store the damageTaken as a double so we can print it and see it in the console
4. playerHealth stops at 0 instead of going into negative
4.5 playerHealthTracker now turns red at 0 health lmao.
5. added a frick ton of getters, setters, and SetTo's in PlayerBody
6. removed hard coding from the player shielding state
6.5 changed the spelling of Defense to Defence (cuz we're canadian and american english is stupid and stinky)
7. in PLAYSCENE:
- added fps tracking
- made some buttons togglable instead of normie buttons (some weirdness but its "intentional")
- added healing cheat
- added god mode cheat
8. in tracker.h/cpp
- added 4 more trackers

IF THERE ARE ANY SPELLING MISTAKES IM SORRY

---
## [CelMetal/CelMetal](https://github.com/CelMetal/CelMetal)@[5cc10b8918...](https://github.com/CelMetal/CelMetal/commit/5cc10b89181f4723411c5a8a4070d0ad87d64d44)
#### Wednesday 2023-11-29 21:11:11 by CelMetal

Update README.md

In a strong effort to help artist get that promotion & booking, HellNRock have created next level promotions campaign that is sure to help boost the notoriety of the artist, their music, and their brand.

Media Promotion, Booking, Touring Management.
Music PR, Press & Blogs

Our Artist Development Program has been built by industry professionals, designed with their real-world experience to help you get the most out of your development. We understand that no two artists are the same, so tailor our services specifically to suit your needs.
When it comes to music marketing, we promise to deliver tangible and REAL results using industry and innovative marketing techniques.
Campaigns start from as little as and stretch across social media marketing, online streaming, radio and press.

---
## [macroscopicentric/social_media_backup](https://github.com/macroscopicentric/social_media_backup)@[c65de71f8d...](https://github.com/macroscopicentric/social_media_backup/commit/c65de71f8d7dbadde5cd2466b71b98b9c4199cfe)
#### Wednesday 2023-11-29 21:32:18 by Rachel King

Update to manage config via anyway_config

This may be a mistake, we'll see. anyway_config is poorly documented
and annoyingly automagical for me. I'm hoping it will help me manage
the config as it (theoretically) gets longer for more social media
profiles.

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[08ab5d2731...](https://github.com/tgstation/tgstation/commit/08ab5d27312d236593eabdb27fb23dccbf8283e6)
#### Wednesday 2023-11-29 22:02:53 by Mothblocks

Blood brothers is now a single person conversion antagonist (#79971)

## About The Pull Request
Instead of choosing 2-3 brothers, *one* person will be selected and
given a flash which can convert one other person over. In accordance to
the existing 10% chance for 3 members, there is a 10% chance that the
first person converted will receive a flash of their own.

Expectation is people will flash a friend or a robust guy or whatever.
My intent is primarily to see if this kind of blood brothers is more
enjoyable to play with/against, and if their inclusion in a round
increases the general chaos of it. My theory is that since most likely
blood brothers will be people who know each other, that it can become
more consistently interesting to the rest of the crew. That or they just
murderbone together idk

Fikou and head admins said they wanted this to replace rather than add
which I agree with.

## Why It's Good For The Game
Keeps the sandboxy aspect of blood brothers (no uplink) while likely
making it more enjoyable to play. Conversion is equally as simple as
revs for the user, and is just as intuitive to the one being converted
since there are no new mechanics thrown in your face.

Blood brothers is currently disabled everywhere on the main servers
except for MRP. I think this form will be more appealing to all
rulesets. If left enabled, Dynamic now has more antagonists to make
rounds diverse with and I want that

## Changelog

:cl:
add: Instead of teaming up random people together, blood brothers will
now start out with one player and let them convert a single other person
over to blood brother using a flash.
/:cl:

---
## [Burzah/Paradise](https://github.com/Burzah/Paradise)@[6a109ade7f...](https://github.com/Burzah/Paradise/commit/6a109ade7f7cd612dcd371f64c4485340ab963d9)
#### Wednesday 2023-11-29 22:13:28 by Henri215

Moves a few sprites out of items.dmi (#23301)

* fuck you items.dmi

* banhammer

---
## [Zevotech/Shiptest](https://github.com/Zevotech/Shiptest)@[40dfaf3734...](https://github.com/Zevotech/Shiptest/commit/40dfaf3734000b5e74e4101ab86516702f59425f)
#### Wednesday 2023-11-29 22:23:20 by Imaginos16

Reworks The Visuals Of Independent And Nanotrasen Captains (#2453)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Does what it says in the title. This is a demented PR that touches a lot
of things, but its main benefit is that now regular independent
captains, cowboy independent captains, and nanotrasen captains have a
unique identity.

Of those changed, it includes:

- The Nanotrasen Captain (parade)

![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/48a31cb1-b266-43cb-9b6e-525028893011)

- The Nanotrasen Captain (regular)

![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/799c88f0-b7ce-4736-956d-2e9c0a096433)

- The Independent Captain (regular/parade)

![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/17ecb3d3-5f2f-4ce0-a518-81366945ebdf)

- The Independent Captain (western)

![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/a56a798c-5adf-41d7-917a-730661f306ed)

The PR also axes a bunch of unused, or frankly quite basic lieutenant
outfits that were nothing more than set dressing with not much substance
behind them. The roles were not removed for now, and they have
appropriate outfits as a placeholder pending a full removal.

This also means that the Head of Personnel was slightly touched up,
mostly by having a coat and hat similar to the western captain's when
appropriate. The role itself is pending a full visual rework for later
that is beyond the scope of this PR.

Speaking of removals, this also means that captain outfits/roles that
were there as a legacy of removed ships, were finally axed for good.
Goodbye deserter captain for Riggs variant number 4, you will not be
missed.

This PR also touches several (a lot) of maps, mostly adding/removing
outfits that were either missing, or didn't fit with the dress code of
the vessel.

Also the PR fixes an oversight by @MarkSuckerberg by making the BYOND
version warning an actual warning, instead of an error when compiling.
Etto bleh.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
Visual cohesion is important, and dear fucking god if I see one more
independent western captain not wearing the duster because it wasn't in
the ship, I will weep, and my weeping will cause a biblical deluge.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: PositiveEntropy
imageadd: Outfits for independent and Nanotrasen captains have been
violently reworked.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [samskivert/moped](https://github.com/samskivert/moped)@[20c02498e5...](https://github.com/samskivert/moped/commit/20c02498e5684cfdb2577031dd092858dba0d763)
#### Wednesday 2023-11-29 22:32:55 by Michael Bayne

Machinery for using tree-sitter for code highlighting.

Right now it's wildly inefficient, reparsing and restyling the entire buffer on
every keystroke. Lol! There are many steps toward efficiency that I can take,
with increasing degrees of PITA:

1. Reparse the whole buffer with tree-sitter on change, but only update the
styles and syntaxes of the lines that changed.

2. Save the tree-sitter tree from each parse, use the tree edit mechanism to
update that tree when buffer changes come in, and then pass in the old tree to
presumably make the reparsing process more efficent. I think this is possible
with the current Java tree-sitter bindings.

3. Figure out how to wrangle JNI into wrapping a C API that takes a pointer to
a callback function which returns a pointer into unmanaged memory to enable
tree-sitter to operate on (as close as possible to) the raw data for each line
stored in MutableLine's internal char arrays, instead of having to concatenate
the entire buffer into a string and convert that to UTF-16 bytes every time we
make a single change to the buffer. This kind of two-way back and forth across
the VM boundary is difficult and annoying, but OMG turning the whole buffer
into a string on every keystroke is egregious.

Also all of this relies on a local build of java-tree-sitter because the
published build does not work on M1 Macs, yay. But if I have to hack that
project's JNI bindings, I'll be needing my own version anyway, at least until
such time as I can get the additions merged upstream and fix their build to
build a fat library for macOS. Fun? No, not fun.

---
## [Tex2002ans/online](https://github.com/Tex2002ans/online)@[3185307c7a...](https://github.com/Tex2002ans/online/commit/3185307c7afa5e76bd10b76a2d97ecbdbc97455a)
#### Wednesday 2023-11-29 22:37:21 by Skyler Grey

Stop hiding both menu and notebookbar softlocking

Previously, when using the Collapse_Notebookbar postmessage or
equivalent ui_defaults (SpreadsheetToolbar=false, etc.), particularly in
compact mode, it was possible to additionally hide the menu bar. As the
button to show the menu bar is on the notebookbar, this meant that you
couldn't reactivate either notebookbar or menubar until you refreshed
the page. This is particularly annoying in integrators that may not
provide an easy way to reload the page

This commit makes it so that hiding the menu bar automatically
uncollapses the notebookbar and won't let it be collapsed again. Whether
the notebook bar should be collapsed (the last thing done to it was a
collapse) is remembered and restored after the menu bar is shown again,
so if you send a postmessage that will affect the state of the
notebookbar after the menu is shown (even though it will not affect the
notebookbar's state immediately)

Caveats:
- If you are hiding the notebookbar to limit the control the user has,
  that's broken by this commit as it makes it impossible to hide both
  the menu and notebook bars at the same time.
- The notebook bar will be hidden again when re-showing the menu bar,
  however there still isn't a way to hide the notebook bar in normal
  use (i.e. without using either postmessage or ui_defaults) while in
  compact mode (although there is a workaround to show it- switching
  into tabbed mode and then back!). It might be nice to have one.

Other considered solutions:
- We could add a new button that allowed you to reopen the menu if both
  menu and notebookbar were hidden
  - Not sure there's much benefit to this over just doing what we're
    doing here, and it's harder to implement
- We could disable the button to hide the menu bar when the notebookbar
  is collapsed
  - As far as I know, there's no button in the UI to show the notebook
    bar. This would make it impossible to hide the menu bar if the
    notebookbar was hidden via postmessage or ui_defaults

Signed-off-by: Skyler Grey <skyler.grey@collabora.com>
Change-Id: Ieab6d72a6be181aba88e9a5b21dda16a369b9e54

---
## [LuciliusMothboy/Men-love-me-fish-fear-me](https://github.com/LuciliusMothboy/Men-love-me-fish-fear-me)@[bf869a0ded...](https://github.com/LuciliusMothboy/Men-love-me-fish-fear-me/commit/bf869a0ded3a3ca5e00500ef5ad856bcb7f012dd)
#### Wednesday 2023-11-29 22:39:28 by Bloop

[MISSED MIRROR] Fixes runtime relating to hard TGS reboots (PROBABLY WON'T FIX REBOOT CRASHES) (#25185)

Fixes runtime relating to hard TGS reboots (PROBABLY WON'T FIX REBOOT CRASHES) (#77309)

## About The Pull Request

Servers are crashing on every round restart and I have absolutely no
idea where to start, but I noticed this so I figure I'll throw up a PR
to fix it.

This is the runtime (only found in dd.log, sorry non-admin/maintainer
gamers
https://[tgstation13.org/raw-logs/sybil/data/logs/2023/08/01/round-211577/dd.log](https://tgstation13.org/raw-logs/sybil/data/logs/2023/08/01/round-211577/dd.log)
)

```txt
[00:07:07] Runtime in code/modules/logging/log_holder.dm,166: Attempted to call shutdown_logging twice!
  proc name: shutdown logging (/datum/log_holder/proc/shutdown_logging)
  src: /datum/log_holder (/datum/log_holder)
  call stack:
  /datum/log_holder (/datum/log_holder): shutdown logging()
  shutdown logging()
  world: Reboot(0, 0)
  Ticker (/datum/controller/subsystem/ticker): Reboot("Round ended.", "proper completion", 600)
```

This is the full log:


![image](https://github.com/tgstation/tgstation/assets/34697715/af938235-3076-41d5-98b2-02907dedb6d5)

This is the code:


![image](https://github.com/tgstation/tgstation/assets/34697715/371b11cb-3bc9-4a99-a17c-73968ded308d)

For some reason, even though we invoke `TGSEndProcess`, we still
continue on in this `if()` chain. I don't know why we keep executing DM
code after TGS is supposed to be shut down (which may be why no one has
ever included a `return` here, but let's be safe instead of sorry.

If you really want to investigate why TGS is running DM code after we
end the process, I am amenable to including a stack trace or crash of
this phenomenon instead.
## Why It's Good For The Game

Since we aren't invoking `LOG_CLOSE_ALL` to rust-g twice (which seems to
be really unwanted per the code I read), hopefully thing no crash?
Rust-g had two breaking changes (one with logs, and one with SQL), so
I'm presuming that this might be related to the log one (which is why we
didn't see this sorta thing happen pre-#77307)... Worst case scenario
less runtimes in the funny runtime log.

I hope this wasn't loadbearing either... Likely requires testmerging
since TGS and I don't get along on my machine.
## Changelog
:cl:
server: Added a preventative measure to prevent calling both
TGSHardRestart and TGSReboot, as well as potentially invoking sensitive
procs that are only meant to be called once.
/:cl:

TL;DR- I do not definitively know why servers are crashing but I noticed
this runtime so I'll put out this open flame while I have the time to do
so.

Co-authored-by: san7890 <the@san7890.com>

---
## [Jacquerel/orbstation](https://github.com/Jacquerel/orbstation)@[9112509abd...](https://github.com/Jacquerel/orbstation/commit/9112509abd9507974928ea5d02676d0d0a58cbec)
#### Wednesday 2023-11-29 23:10:43 by KingkumaArt

Stops rebar crossbow crashing dreamseeker when fired at point blank. (NO GBP) (#79803)

## About The Pull Request

Simply put, due to how "caseless" is an element added to the ammo when
it hits something, but ammo is qdeleted upon hitting someone. If shot
point blank without combat mode (for some reason) it tries to add
caseless to an ammo that no longer exists. For some reason, the result
of this is to just fucking crash DS instead of aborting the adding of
the element. The ammo isnt reusable anymore, but I'll take that over
crashing.

## Why It's Good For The Game

Removes a game-breaking bug. I hate gun ammo code so much. 

## Changelog



:cl:
fix: Stopped a DS crash when shooting a rebar crossbow in specific
circumstances.
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [BogCreature/Shiptest](https://github.com/BogCreature/Shiptest)@[223dc74ef1...](https://github.com/BogCreature/Shiptest/commit/223dc74ef1f528e2c29b0e62271ddaf7b68d79d8)
#### Wednesday 2023-11-29 23:26:11 by retlaw34

Eoehoma Firearms (& friends) (#2315)

## About The Pull Request


![Screenshot_5451](https://github.com/shiptest-ss13/Shiptest/assets/58402542/08f9b0ee-15db-4091-a974-6d887cd85259)

Holy shit, this should not have taken a year to make

Adds the E-10, E-11, E-40, E-50, and E-60 to the game. Weapons
manufactured by defunct firearms company Eoehoma Firearms.

Founded in 77 FS, Eoehoma was a early pioneer of ‘hybrid’ Solarian and
Kalixcian laser weapons. The company went bankrupt due to increasingly
poor and risky decision making, and all of it's patents were bought out
by Nanotrasen. While Nanotrasen's Emitters bear a striking resemblance
to the E-50, otherwise Nanotrasen has not produced any of Eoehoma's old
weapons, instead focusing on Sharplite designed weapons.

Other changes:
- NT and Sharplite weapons have different fire sounds from each other
- Laser weapons buffed to 20 -> 25 damage
- Pulse shots don't destroy walls and are now 50 -> 40 damage
- Emitter shots now do 30 -> 60 damage
- Various grammar fixes
- Removes some non-lore compliant mentions
- Adds a manufacturer indicator to many guns
- Ports https://github.com/tgstation/tgstation/pull/60353
- Resprites various laser weaponry, notably the pulse guns.
- Deathsquad and ERT/LP hardsuits have been redone

## Why It's Good For The Game


![image](https://github.com/shiptest-ss13/Shiptest/assets/58402542/c5df7029-95da-4041-b8b1-e4cfd35436dd)

![image](https://github.com/shiptest-ss13/Shiptest/assets/58402542/f72a3672-e996-4fdd-a68d-4553655f1a0c)

![image](https://github.com/shiptest-ss13/Shiptest/assets/58402542/7bd2dc53-ab29-49e8-8f90-87d4c72583f9)

![image](https://github.com/shiptest-ss13/Shiptest/assets/58402542/4bdc6493-4c94-49d0-995b-2a450d738211)
ceredits to tetrazeta for the unfinished deathsquad sprite, i simply
finished it and touched it up

![image](https://github.com/shiptest-ss13/Shiptest/assets/58402542/517b72e3-c72b-4875-a6fb-84c017105908)

One of the last things i remember the old leads planned was to buff
lasers to make them stand up to the various ballistics better. Also
allows Pulse Rifles to be more used in events by nerfing them to not be
comedically overpowered. Now they are just Overpowered.

More ruin content and such. I'm sure the maptainers will make good use
of this stuff.

And sprites, i fucking love sprites

## Changelog

:cl: retlaw34, tetrazeta
add: Eoehoma Firearms, a new guns manufacturer!
add: ERT and "Asset Protection" Hardsuits have gotten a new look!
add: New laser fire sounds

balance: Lasers now do slightly more damage
balance: Pulse rifles don't destroy walls anymore and do slightly less
damage, and have lost their stun mode.
balance: Emitters do 60 damage and create turf fires on hitting a
non-supermatter object.
fix: Various laser weapons that had broken autofire (E-TAR and the Tesla
Cannon) now work

spellcheck: Grammar on some descriptions was corrected.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Signed-off-by: retlaw34 <58402542+retlaw34@users.noreply.github.com>
Co-authored-by: Mark Suckerberg <mark@suckerberg.gay>
Co-authored-by: thgvr <81882910+thgvr@users.noreply.github.com>

---
## [EchterAlsFake/Porn_Fetch](https://github.com/EchterAlsFake/Porn_Fetch)@[edb0eb28e8...](https://github.com/EchterAlsFake/Porn_Fetch/commit/edb0eb28e80f42bade48e26780a6040b16f44e75)
#### Wednesday 2023-11-29 23:34:47 by Johannes Habel

I just fucked up my code and I can now work the whole day getting it fixed.

So learn from my stupid mistakes and commit your god damn changes every second so that you don't get into this mess like me -_-

---
## [Lector/DSA5maptool](https://github.com/Lector/DSA5maptool)@[795a5be792...](https://github.com/Lector/DSA5maptool/commit/795a5be792521f0b51182ef76649e512fd776ca5)
#### Wednesday 2023-11-29 23:37:52 by Lector

Update to maptool v1.14.2:
- our old makro getIllumination() is now supported by maptool itself. We renamed our macro to getVisibilityMod.mts so the names don not conflict.
  our macro now uses getIllumination() to determine the visibility modifier. This works in DAY and NIGHT maps and also supports magical darkness.
  This should also solve the flickering problem when playing with lots of light sources and is a huge boost in performance.
- Borders now look like they did before. The height of the borders was adjusted slightly. (not sure why this happened...)

---

