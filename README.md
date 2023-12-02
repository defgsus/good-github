## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-12-01](docs/good-messages/2023/2023-12-01.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 5,348,699 were push events containing 6,418,773 commit messages that amount to 318,764,010 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 74 messages:


## [LeeroysHub/RM-Flipper](https://github.com/LeeroysHub/RM-Flipper)@[8184d1b324...](https://github.com/LeeroysHub/RM-Flipper/commit/8184d1b324dc497b6da7d995ba2df04db7253c58)
#### Friday 2023-12-01 00:08:45 by Leeroy

Rollback Keyloq to 5 months ago! Bloody regressions making my daily life shit!

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[2e0597d055...](https://github.com/tgstation/tgstation/commit/2e0597d055fc105037a904355726139434f36b3a)
#### Friday 2023-12-01 00:21:25 by Vekter

Replaces the fake monkey cube in Birdshot tool storage with a less lethal one, adds something else fun (#80030)

## About The Pull Request
One of the "monkey cubes" in Birdshot's tool storage was actually a
gorilla cube. This was funny up until people realized it was a thing and
now people are using it intentionally to grief. I'd rather not.

It's a different cube now. I don't want to spoil it but it won't kill
anyone, just make people laugh.

I added a different fun item to another tile in tool storage. Again, no
spoilers, read the code if you really want to know what it was.

## Why It's Good For The Game
I like the "cube says it's a monkey but it's not" joke. It was funny
when people thought it was a monkey, used it, and got killed by it.
Problem is, people know what it is now and have used it for grief
purposes, so we can't have nice things. Gorillas are stupid hard to kill
and will de-limb people by looking at them.

I wanted to add something else fun to replace it that isn't just the
exact same joke but now it won't kill you, so I did.

## Changelog
:cl: Vekter
del: Replaced the "monkey cube" in Birdshot's tool storage with a
different "monkey cube".
add: Added a fun surprise item to Birdshot's tool storage to compensate
for the above change.
/:cl:

---
## [chipturner/pytorch](https://github.com/chipturner/pytorch)@[ddf1cb7870...](https://github.com/chipturner/pytorch/commit/ddf1cb78705dcf79fe8c8df01f6f18ca4a218c55)
#### Friday 2023-12-01 00:22:38 by voznesenskym

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
## [ridethru/x86-manual-mapper](https://github.com/ridethru/x86-manual-mapper)@[1f5802a811...](https://github.com/ridethru/x86-manual-mapper/commit/1f5802a811cbb20467bc4f9b424bea7a632ddeb7)
#### Friday 2023-12-01 00:23:26 by ridethru

i dont even remember what i changed but i forgot to make a commit for it. if my classes want to give me 5 fuckin minutes to live my life maybe i will get around to making x86_64 build

---
## [kvm-x86/linux](https://github.com/kvm-x86/linux)@[c52ffadc65...](https://github.com/kvm-x86/linux/commit/c52ffadc65e28ab461fd055e9991e8d8106a0056)
#### Friday 2023-12-01 00:24:59 by Sean Christopherson

KVM: x86: Don't unnecessarily force masterclock update on vCPU hotplug

Don't force a masterclock update when a vCPU synchronizes to the current
TSC generation, e.g. when userspace hotplugs a pre-created vCPU into the
VM.  Unnecessarily updating the masterclock is undesirable as it can cause
kvmclock's time to jump, which is particularly painful on systems with a
stable TSC as kvmclock _should_ be fully reliable on such systems.

The unexpected time jumps are due to differences in the TSC=>nanoseconds
conversion algorithms between kvmclock and the host's CLOCK_MONOTONIC_RAW
(the pvclock algorithm is inherently lossy).  When updating the
masterclock, KVM refreshes the "base", i.e. moves the elapsed time since
the last update from the kvmclock/pvclock algorithm to the
CLOCK_MONOTONIC_RAW algorithm.  Synchronizing kvmclock with
CLOCK_MONOTONIC_RAW is the lesser of evils when the TSC is unstable, but
adds no real value when the TSC is stable.

Prior to commit 7f187922ddf6 ("KVM: x86: update masterclock values on TSC
writes"), KVM did NOT force an update when synchronizing a vCPU to the
current generation.

  commit 7f187922ddf6b67f2999a76dcb71663097b75497
  Author: Marcelo Tosatti <mtosatti@redhat.com>
  Date:   Tue Nov 4 21:30:44 2014 -0200

    KVM: x86: update masterclock values on TSC writes

    When the guest writes to the TSC, the masterclock TSC copy must be
    updated as well along with the TSC_OFFSET update, otherwise a negative
    tsc_timestamp is calculated at kvm_guest_time_update.

    Once "if (!vcpus_matched && ka->use_master_clock)" is simplified to
    "if (ka->use_master_clock)", the corresponding "if (!ka->use_master_clock)"
    becomes redundant, so remove the do_request boolean and collapse
    everything into a single condition.

Before that, KVM only re-synced the masterclock if the masterclock was
enabled or disabled  Note, at the time of the above commit, VMX
synchronized TSC on *guest* writes to MSR_IA32_TSC:

        case MSR_IA32_TSC:
                kvm_write_tsc(vcpu, msr_info);
                break;

which is why the changelog specifically says "guest writes", but the bug
that was being fixed wasn't unique to guest write, i.e. a TSC write from
the host would suffer the same problem.

So even though KVM stopped synchronizing on guest writes as of commit
0c899c25d754 ("KVM: x86: do not attempt TSC synchronization on guest
writes"), simply reverting commit 7f187922ddf6 is not an option.  Figuring
out how a negative tsc_timestamp could be computed requires a bit more
sleuthing.

In kvm_write_tsc() (at the time), except for KVM's "less than 1 second"
hack, KVM snapshotted the vCPU's current TSC *and* the current time in
nanoseconds, where kvm->arch.cur_tsc_nsec is the current host kernel time
in nanoseconds:

        ns = get_kernel_ns();

        ...

        if (usdiff < USEC_PER_SEC &&
            vcpu->arch.virtual_tsc_khz == kvm->arch.last_tsc_khz) {
                ...
        } else {
                /*
                 * We split periods of matched TSC writes into generations.
                 * For each generation, we track the original measured
                 * nanosecond time, offset, and write, so if TSCs are in
                 * sync, we can match exact offset, and if not, we can match
                 * exact software computation in compute_guest_tsc()
                 *
                 * These values are tracked in kvm->arch.cur_xxx variables.
                 */
                kvm->arch.cur_tsc_generation++;
                kvm->arch.cur_tsc_nsec = ns;
                kvm->arch.cur_tsc_write = data;
                kvm->arch.cur_tsc_offset = offset;
                matched = false;
                pr_debug("kvm: new tsc generation %llu, clock %llu\n",
                         kvm->arch.cur_tsc_generation, data);
        }

        ...

        /* Keep track of which generation this VCPU has synchronized to */
        vcpu->arch.this_tsc_generation = kvm->arch.cur_tsc_generation;
        vcpu->arch.this_tsc_nsec = kvm->arch.cur_tsc_nsec;
        vcpu->arch.this_tsc_write = kvm->arch.cur_tsc_write;

Note that the above creates a new generation and sets "matched" to false!
But because kvm_track_tsc_matching() looks for matched+1, i.e. doesn't
require the vCPU that creates the new generation to match itself, KVM
would immediately compute vcpus_matched as true for VMs with a single vCPU.
As a result, KVM would skip the masterlock update, even though a new TSC
generation was created:

        vcpus_matched = (ka->nr_vcpus_matched_tsc + 1 ==
                         atomic_read(&vcpu->kvm->online_vcpus));

        if (vcpus_matched && gtod->clock.vclock_mode == VCLOCK_TSC)
                if (!ka->use_master_clock)
                        do_request = 1;

        if (!vcpus_matched && ka->use_master_clock)
                        do_request = 1;

        if (do_request)
                kvm_make_request(KVM_REQ_MASTERCLOCK_UPDATE, vcpu);

On hardware without TSC scaling support, vcpu->tsc_catchup is set to true
if the guest TSC frequency is faster than the host TSC frequency, even if
the TSC is otherwise stable.  And for that mode, kvm_guest_time_update(),
by way of compute_guest_tsc(), uses vcpu->arch.this_tsc_nsec, a.k.a. the
kernel time at the last TSC write, to compute the guest TSC relative to
kernel time:

  static u64 compute_guest_tsc(struct kvm_vcpu *vcpu, s64 kernel_ns)
  {
        u64 tsc = pvclock_scale_delta(kernel_ns-vcpu->arch.this_tsc_nsec,
                                      vcpu->arch.virtual_tsc_mult,
                                      vcpu->arch.virtual_tsc_shift);
        tsc += vcpu->arch.this_tsc_write;
        return tsc;
  }

Except the "kernel_ns" passed to compute_guest_tsc() isn't the current
kernel time, it's the masterclock snapshot!

        spin_lock(&ka->pvclock_gtod_sync_lock);
        use_master_clock = ka->use_master_clock;
        if (use_master_clock) {
                host_tsc = ka->master_cycle_now;
                kernel_ns = ka->master_kernel_ns;
        }
        spin_unlock(&ka->pvclock_gtod_sync_lock);

        if (vcpu->tsc_catchup) {
                u64 tsc = compute_guest_tsc(v, kernel_ns);
                if (tsc > tsc_timestamp) {
                        adjust_tsc_offset_guest(v, tsc - tsc_timestamp);
                        tsc_timestamp = tsc;
                }
        }

And so when KVM skips the masterclock update after a TSC write, i.e. after
a new TSC generation is started, the "kernel_ns-vcpu->arch.this_tsc_nsec"
is *guaranteed* to generate a negative value, because this_tsc_nsec was
captured after ka->master_kernel_ns.

Forcing a masterclock update essentially fudged around that problem, but
in a heavy handed way that introduced undesirable side effects, i.e.
unnecessarily forces a masterclock update when a new vCPU joins the party
via hotplug.

Note, KVM forces masterclock updates in other weird ways that are also
likely unnecessary, e.g. when establishing a new Xen shared info page and
when userspace creates a brand new vCPU.  But the Xen thing is firmly a
separate mess, and there are no known userspace VMMs that utilize kvmclock
*and* create new vCPUs after the VM is up and running.  I.e. the other
issues are future problems.

Reported-by: Dongli Zhang <dongli.zhang@oracle.com>
Closes: https://lore.kernel.org/all/20230926230649.67852-1-dongli.zhang@oracle.com
Fixes: 7f187922ddf6 ("KVM: x86: update masterclock values on TSC writes")
Cc: David Woodhouse <dwmw2@infradead.org>
Reviewed-by: Dongli Zhang <dongli.zhang@oracle.com>
Tested-by: Dongli Zhang <dongli.zhang@oracle.com>
Link: https://lore.kernel.org/r/20231018195638.1898375-1-seanjc@google.com
Signed-off-by: Sean Christopherson <seanjc@google.com>

---
## [drisspg/pytorch](https://github.com/drisspg/pytorch)@[5f504d1de7...](https://github.com/drisspg/pytorch/commit/5f504d1de74a5189f93e65aa9283fc4607b8631c)
#### Friday 2023-12-01 01:02:10 by Pedro Caldeira

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
## [Pr0methean/oxipng](https://github.com/Pr0methean/oxipng)@[ecf3ce8fc2...](https://github.com/Pr0methean/oxipng/commit/ecf3ce8fc21ab20eb73ef8618f8b86f95f0104cc)
#### Friday 2023-12-01 01:10:23 by Alejandro González

Revamp CI workflow to upload artifacts, cross-compile ARM64 binaries, and more (#534)

As commented in issues https://github.com/shssoichiro/oxipng/issues/444
and https://github.com/shssoichiro/oxipng/issues/518, there is some user
interest for distributing binaries for each unstable commit, and target
ARM64 platforms. Personally, I think both suggestions are useful for the
project, as uploading binary artifacts for each commit might help
interested users to catch regressions and give feedback earlier, and
powerful ARM64 platforms are becoming increasingly popular due to some
cloud services (e.g., Amazon EC2, Azure VMs, Oracle Cloud) offering
cheaper plans for this hardware, in addition to the well-known push for
ARM by Apple with their custom M1 chips.

These changes make the CI target ARM64 as a first-class citizen. Because
the public GitHub actions runners can only be hosted on x64 for now, I
resorted to cross-compilation, [Debian's
multiarch](https://elinux.org/images/d/d8/Multiarch_and_Why_You_Should_Care-_Running%2C_Installing_and_Crossbuilding_With_Multiple_Architectures.pdf),
and QEMU to build, get ARM64 C library dependencies, and run tests,
respectively.

When the CI workflow finishes, a release CLI binary artifact is now
uploaded, which can be downloaded from the workflow run page on the
GitHub web interface.

In addition, these changes also introduce some cleanup and miscellaneous
improvements and changes to the CI workflow:

- Tests are run using [`nextest`](https://nexte.st/) instead of `cargo
test`, which substantially speeds up their execution. (On my development
workstation, `cargo test --release` takes around 10.67 s, while `cargo
nextest run --release` takes around 6.02 s.)
- The dependencies on unmaintained `actions-rs` actions were dropped in
favor of running Cargo commands directly, or using
`giraffate/clippy-action` for pretty inline annotations for Clippy. This
gets rid of the deprecation warnings for each workflow run.
- Most CI steps are run with a nightly Rust toolchain now, which allows
to take advantage of the latest Clippy lints and codegen improvements.
In my experience, when not relying on specific nightly features or
compiler internals, Rust does a pretty good job at making it possible to
rely on a rolling-release compiler for CI, as breakage is extremely rare
and thus offset by the improved features.
- The MSRV check was moved to a separate job with less steps, so that it
takes less of a toll on total workflow run minutes.

- [x] Generate universal macOS binaries with `lipo` (i.e., containing
both `aarch64` and `x64` code)
- [x] Tirelessly fix the stupid errors that tend to happen when
deploying a new CI workflow for the first time
- [x] Think what to do with the `deploy.yml` workflow. Should it fetch
artifacts from the CI job instead of building them again?
- [x] Maybe bring back 32-bit Windows binaries. Are they actually useful
for somebody, or just a way to remember the good old days?

---------

Co-authored-by: Josh Holmer <jholmer.in@gmail.com>

---
## [tlm/juju](https://github.com/tlm/juju)@[9332e8c436...](https://github.com/tlm/juju/commit/9332e8c4361fe8860cbda185e0f1597431ea3e0f)
#### Friday 2023-12-01 01:30:33 by Juju bot

Merge pull request #16611 from tlm/model-config-api

https://github.com/juju/juju/pull/16611

With this commit we are introducing a new global table to the controller database to describe model defaults that should be applied to all models in the controller.

Previously in Juju we have not had this notion of controller wide model defaults. They have always been scoped to the cloud or cloud region. However secretly under the covers we have been living a life of shame where we have been taking the controller models config and using that as a controller wide default source.

It is time to rise up out of the shadows of this murky controller model defaults world and own our desire for a controller wide model defaults source. No longer should lesser models live in shame and more importantly no longer should the controller model be treated as some special case model that acts as a source of truth.

A perfect example of this is we use the controller model to find the Juju system ssh key that is created during bootstrap. Every model needs ssh key added to it at creation time. We currently interrogate the controller model for the key. We are going to stop doing this so that the controller model can have the exact same logic applied to it as every other model in Juju.

## Checklist

- [x] Code style: imports ordered, good names, simple structure, etc
- [x] Comments saying why design decisions were made
- ~[ ] Go unit tests, with comments saying what you're testing~
- ~[ ] [Integration tests](https://github.com/juju/juju/tree/main/tests), with comments saying what you're testing~
- ~[ ] [doc.go](https://discourse.charmhub.io/t/readme-in-packages/451) added or updated in changed packages~

## QA steps

No tests for this change. I am just proposing the DDL. The next PR that wires up the state layer will offer the tests for this DDL.

## Documentation changes

None. We are not going to offer this defaults source as a user configurable component via the cli or API. We are just going to store bootstrap generated concerns in the table at the moment where we know a key is going to be needed for every model regardless of what cloud it is for.

## Links

**Jira card:** JUJU-5046

---
## [rodolphito/bevy](https://github.com/rodolphito/bevy)@[ab300d0ed9...](https://github.com/rodolphito/bevy/commit/ab300d0ed9990972679629af3ef18fd37c0e106c)
#### Friday 2023-12-01 01:36:17 by Connor King

Gizmo Arrows (#10550)

## Objective

- Add an arrow gizmo as suggested by #9400 

## Solution

(excuse my Protomen music)


https://github.com/bevyengine/bevy/assets/14184826/192adf24-079f-4a4b-a17b-091e892974ec

Wasn't horribly hard when i remembered i can change coordinate systems
whenever I want. Gave them four tips (as suggested by @alice-i-cecile in
discord) instead of trying to decide what direction the tips should
point.

Made the tip length default to 1/10 of the arrow's length, which looked
good enough to me. Hard-coded the angle from the body to the tips to 45
degrees.

## Still TODO

- [x] actual doc comments
- [x] doctests
- [x] `ArrowBuilder.with_tip_length()`

---

## Changelog

- Added `gizmos.arrow()` and `gizmos.arrow_2d()`
- Added arrows to `2d_gizmos` and `3d_gizmos` examples

## Migration Guide

N/A

---------

Co-authored-by: Nicola Papale <nicopap@users.noreply.github.com>

---
## [GPeckman/tgstation](https://github.com/GPeckman/tgstation)@[d31c21ff1b...](https://github.com/GPeckman/tgstation/commit/d31c21ff1b57ba7003f9bbdcf51171d3215a0774)
#### Friday 2023-12-01 02:00:32 by jimmyl

new space ruin, the biological research outpost (#79149)

## About The Pull Request

![2023-10-21 18 02
39](https://github.com/tgstation/tgstation/assets/70376633/5829e939-3b04-465f-a186-095ceb360bba)

adds this ruin to space ruin pool
this is a shady (as NT always is) bioresearch outpost that got fucked up
by an experiment
this has like some puzzle aspect to it since you gotta find keycards and
shit and press buttons to unlock shield gates
this ends with you fighting a heart which if you defeat, destroys the
blockade that prevents you from entering the outpost vault

also you can no longer literally just cut indestructible grilles or
unanchor indestructible windows

### new puzzle elements or something idk
variant of pressure plate that you cannot remove and it sends a puzzle
signal
cooler red puzzle doors that look very foreboding or something idk
theyre for this ruin
also puzzle blockades, which are indestructible dense objects that are
destroyed if they receive a puzzle signal
and also buttons and keycard pads for puzzles


https://github.com/tgstation/tgstation/assets/70376633/c98807ec-1e7b-49c4-a757-cdbb76a1b566



https://github.com/tgstation/tgstation/assets/70376633/9d5d9dd1-5868-44e6-a978-5ea57b30c298

stuff that throws electric shocks in a pattern, ignores insuls and only
knocks down, and no you cannot just run past


https://github.com/tgstation/tgstation/assets/70376633/5772917c-a963-48a4-a743-b0f610801d25

### enemies
living floor, it can only attack stuff on top of it and it attacks until
the victim is dead
it is invincible to all but a crowbar, and it cannot move, and it
remains hidden until a victim is in range


https://github.com/tgstation/tgstation/assets/70376633/aa1d54f6-b259-4e58-9d44-e393d2131acf

living flesh, it can replace your limbs with itself
the conditions for that are; the limb must have 20 or more brute, victim
must be alive and dismemberable, the limb may not be torso or head, or
the limb may not be living flesh
alternatively it can replace a missing limb
these are all checked with every attack
they have 20 hp
the limbs in question will sometimes act up, while passively draining
nutrition, arms will randomly start pulling nearby stuff, legs may step
randomly
limbs when detached, turn into mobs and reactivate AI 2 seconds later.
if the host is shocked, all living flesh limbs will detach, or if the
host dies they will also do that


https://github.com/tgstation/tgstation/assets/70376633/765cc99e-c800-4efb-aabe-d68817bbd7ae



## Why It's Good For The Game

ruin variety is cool i think
also the other things i added should be useful for other mappers for
bitrunning or whatever

also bug bad for that one fix
## Changelog
:cl:
add: living floor, living flesh, and other stuff for the bioresearch
outpost ruin
add: bioresearch outpost ruin
fix: you may not defeat indestructible grilles and windows with mere
tools
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [Yungryota/PSA](https://github.com/Yungryota/PSA)@[f0f8244688...](https://github.com/Yungryota/PSA/commit/f0f8244688b45c94907dbd7ffa4a802260ac5ed4)
#### Friday 2023-12-01 02:11:08 by Javiera

muestra primera temperatura en angular

From sprinkler splashes to fireplace ashes
I gave my blood, sweat, and tears for this
I hosted parties and starved my body
Like I'd be saved by a perfect kiss
The jokes weren't funny, I took the money
My friends from home don't know what to say
I looked around in a blood-soaked gown
And I saw something they can't take away
'Cause there were pages turned with the bridges burned
Everything you lose is a step you take
So make the friendship bracelets
Take the moment and taste it
You've got no reason to be afraid

---
## [cyberitsolutions/bootstrap2020](https://github.com/cyberitsolutions/bootstrap2020)@[c521b4f059...](https://github.com/cyberitsolutions/bootstrap2020/commit/c521b4f05955e06d964631c275c95f9135f8b6c0)
#### Friday 2023-12-01 02:31:09 by Trent W. Buck

UKI: refactor in-house ukify for readability

17:25 <twb> mike: how do you feel about this refactoring to avoid "magic" numbers?
17:26 <mike> What magic numbers are you avoiding? O.o
17:26 <twb> 7, 2, 3
17:26 <twb> The 16 is still there but has a comment now
17:27 <mike> Oh, just the column splits, ok.
             You haven't really avoided the need for them, just
             changed how the vars are set so you don't have to actually write the number.
17:27 <twb> Right
17:28 <mike> I'm not against what you've done, but I don't think it was worth the time to do it. 🤷
17:28 <twb> I basically wrote that while trying to understand the existing code.
17:28 <mike> Ok
17:28 <twb> If my version isn't MORE confusing for you, I'd like to keep it
17:29 <mike> Yeah is fine to keep

---
## [minetest/minetest_game](https://github.com/minetest/minetest_game)@[4bb4a2a818...](https://github.com/minetest/minetest_game/commit/4bb4a2a8187d036325482bb727a65b899f8991bd)
#### Friday 2023-12-01 02:46:23 by Yaya - Nurul Azeera Hidayah @ Muhammad Nur Hidayat Yasuyoshi

Update Malay translations
1. Added missing translation to the following files:
  beds.ms.tr, creative.ms.tr, default.ms.tr, farming.ms.tr,
  fire.ms.tr, sethome.ms.tr
2. Changes some translation as per following:
  a. beds.ms.tr
    - Leave Bed changed from Bangun (wake up) to Tinggalkan Katil
      (leave bed, in literal sense) just because the button would
      be interpreted by some people as 'wake up on next morning'
      (ie. skipping night) instead of 'wake up interrupting current
      sleep progress' which is the intended meaning.
  b. boats.ms.tr
    - Boat cruise mode changed from Mod bot layar makan angin to
      Mod jelajah bot, the original translation is more like direct
      translation, and this has been changed to more natural one
      to make sure player know that the mode is a cruise control.
    - Reset changed from Set semula to Tetap semula, this is for
      standardizing with existing term used in various places.
  c. default.ms.tr
    - Page \@1 of \@2 changed from the short form to the long form.
    - Mese Crystal Fragment had missing word 'Kristal' re-added.
  d. dye.ms.tr
    - Dark Grey changed from Kelabu Gelap to Kelabu Tua to make it
      standardized with the colour name elsewhere.
    - Dark Green changed from Hijau Gelap to Hijau Tua to make it
      standardized with the colour name elsewhere.
    - Magenta changed from Merah Lembayung to Magenta, because the
      colour Merah Lembayung is now used to refer to purplish red
      and no longer equal to magenta, the loanword is used instead.
  e. game_commands.ms.tr
    - respawn changed from lahir semula (reborn) to jelma semula
      (reappear), this is to make it consistent with the language
      used in multiple other games that had similar respawning
      system, and avoiding the religious context of life that is
      implied by the use of previous translation.
    - spawnpoint changed from titik permulaan (starting point) to
      titik jelma ((re)appear point), see previous point.
  f. tnt.ms.tr
    - Gun Powder changed from Serbuk Senjata Api (firearms powder)
      to Serbuk Letupan (explosion powder) because that is the
      proper translation, the latter is still the term used even
      when talking about actual firearm, the former didn't exist
  g. vessels.ms.tr
    - item changed from barang (thing) to item, this is mainly
      because some of the 'item' that could be stored are not
      some solid 'thing' where the word barang could be used for,
      so using the word item here keep it neutral.
  h. wool.ms.tr
    - Dark Grey changed from Kelabu Gelap to Kelabu Tua to make it
      standardized with the colour name elsewhere.
    - Dark Green changed from Hijau Gelap to Hijau Tua to make it
      standardized with the colour name elsewhere.
    - Magenta changed from Merah Lembayung to Magenta, because the
      colour Merah Lembayung is now used to refer to purplish red
      and no longer equal to magenta, the loanword is used instead.

---
## [dianakarpeev/mutsu](https://github.com/dianakarpeev/mutsu)@[f90c2a7838...](https://github.com/dianakarpeev/mutsu/commit/f90c2a783823b3162b857c5af72ace39e16e0e7c)
#### Friday 2023-12-01 02:55:56 by Mel Hynes

Data store functionality (#72)

* Beginning Storage Progress
- Started a UserIngredientsRepository and dataStorage. My goal is to set up information that'll be easy to edit, to reflect current vs needed ingredients. It's entirely too late to be thinking this through in any meaningful way, though -M

* Setup Proto Schemas
- Updated and significantly modified the app build.gradle file to allow for Proto DataStore
- Created Recipe.proto as a starting point for data storage serialization.

!!! NOT CLEAN CODE !!!
This code isn't compiling at this moment. There are more steps I have to work on. This commit's used as a save point before making more progress (toward glory or toward insanity, only Fate knows)

* IngredientsName Class
- Created a class and map to facilitate creating and eventually saving ingredients, taking a step away from the hard-coded values used throughout the app.

* Save Point
- Ugh -M

* Progress toward Storing
- Got the Gradle File to work as intended
- Made progress on reworking the Ingredients View Model to use the IngredientsNameRepository

* IT WORKS OH MY GODS IT WORKS
- Got storage working and fixed the Grocery List view model to work with the storage as well

* Renamed storage.proto file to fix app-breaking bug

* Update build.gradle.kts
- Changed a plugin implementation to be in line with Main

* Update MainActivity.kt
- Made some silly errors in previous fix while trying to merge main and datastore-functionality, hopefully this should fix.

* Fixed some issues with IngredientsViewModel not seeding -M

---
## [UBCFormulaElectric/Consolidated-Firmware](https://github.com/UBCFormulaElectric/Consolidated-Firmware)@[48ee00ec77...](https://github.com/UBCFormulaElectric/Consolidated-Firmware/commit/48ee00ec772e45a997365bdf7dadaecc117a31e9)
#### Friday 2023-12-01 03:32:01 by Gus Tahara-Edmonds

Make CAN signal names unique (#1019)

### Summary
<!-- Quick summary of changes, optional -->

Currently CAN signal names are not unique. This is not a problem when
using PCAN or writing code, since signals are categorized by their CAN
message. However, this is not the case when uploading data to Influx,
since then only signal names are uploaded. This means that there are
weird conflicts between signals of the same name. For example, `State`
for the BMS and the DCM.

This PR changes so signal names are prefixed by their board, and then we
enforce all signals are unique across all boards. To avoid ridiculously
long CAN setters/getters in the firmware, only the signal name is now
used.

For example:
| | Before | After |

|-----------|--------------------------------------------|---------------------------------|
| Message | `BMS_Contactors` | `BMS_Contactors` |
| Signal | `AirPositive` | `BMS_AirPositive` |
| TX Setter | `App_CanTx_BMS_Contactors_AirPositive_Set` |
`App_CanTx_BMS_AirPositive_Set` |

The board name prefixes are also now added automatically to
messages/signals, so they've been removed from the `*_tx.json` files.

### Changelist 
<!-- Give a list of the changes covered in this PR. This will help both
you and the reviewer keep this PR within scope. -->

- Change `jsoncan` Python to support these changes
- Rename all signals
- Removed a few unused signals

Note: This diff is huge because of the autogenerated example code in
`jsoncan`. I should really remove this and add proper unit tests
instead.

### Testing Done
<!-- Outline the testing that was done to demonstrate the changes are
solid. This could be unit tests, integration tests, testing on the car,
etc. Include relevant code snippets, screenshots, etc as needed. -->

- [x] Validated on car

### Resolved Issues
<!-- Link any issues that this PR resolved like so: `Resolves #1, #2,
and #5` (Note: Using this format, Github will automatically close the
issue(s) when this PR is merged in). -->

### Checklist
*Please change `[ ]` to `[x]` when you are ready.*
- [x] I have read and followed the code conventions detailed in
[README.md](../README.md) (*This will save time for both you and the
reviewer!*).
- [x] If this pull request is longer then **500** lines, I have provided
*explicit* justification in the summary above explaining why I *cannot*
break this up into multiple pull requests (*Small PR's are faster and
less painful for everyone involved!*).

---
## [Kitsunemitsu/lobotomy-corp13](https://github.com/Kitsunemitsu/lobotomy-corp13)@[e23ea7b596...](https://github.com/Kitsunemitsu/lobotomy-corp13/commit/e23ea7b5965a446e5b34f30baa0d4e4dc2d5b868)
#### Friday 2023-12-01 04:36:23 by Táculo

Updates La Luna, Pinnochio for Rcorp and playables, gives minions NV on Rcorp AND moves CheckCombat to simple_animal. (#1621)

* Adds Everything

adds nv combat checks to
nosferatu bats
ml slimes
censored minis
tbird spawns
la luna spawned mob

adds mind transfer to pinocchio and la luna
add check for combat to initialize ai controllers for pinocchio, gives him a seclite on rcorp
add check for combat to spawn the breached la luna mob on its position instead of in a random department and to disable the timer.

makes pino ai disabled while a client is possesing it.

* removes one line

* Changes CheckCombat location, applies it to all minions.

* Makes button refuse pino.

fuck you pinocchio

* moves blocking code to pinocchio's

* moves the nightvision checks to simple_animal

moves the nightvision checks to simple_animal

removes the checks from censored, luna, tbird, ml, nosferatu

---
## [Kitsunemitsu/lobotomy-corp13](https://github.com/Kitsunemitsu/lobotomy-corp13)@[294f764ad0...](https://github.com/Kitsunemitsu/lobotomy-corp13/commit/294f764ad01a99c63b46dfea3dac7e5cfe14cd7d)
#### Friday 2023-12-01 04:36:23 by Coxswain

Adds distorted form (#1435)

adds some basic features

new 1% sprite dropped

text update

Finished work mechanics

adds basic breaching

should fix linters a bit

It works!!!! Kinda...

adds crumbling armor and hammer of light (beta)

adds cool and important stuff

does a thing

adds apostle and tutorial abnorms

adds the stuff

might fix linters

adds a console proc

adds crumbling armor's proper attack and red queen

does some things

should fix linters

adds a blubbering toad transformation

adds more attacks

brings the tier up

adds big boy attacks

updates some sfx, fixes bugs

adds jump attacks

why does linters care about indentation on comments?

adds suggested changes

should fix some stuff

adds info

adjusts damage numbers

updates an effects and fixes transformations

updates blacklist

lowers stack damage

lowers max qlip to 3

adds bloodbath

adds a new AOE attack

adds halberd apostle

blacklists DF from pink midnight

fixes weirdness

requested changes and sound design improvement

removes armortype

removes armortype for real

damage coeff update

makes suggested changes

updates comments

adds procs

adds stuff

---
## [yogstation13/Yogstation](https://github.com/yogstation13/Yogstation)@[75c13f4eff...](https://github.com/yogstation13/Yogstation/commit/75c13f4effbd82c8dc661c6b3bbc0146de44fded)
#### Friday 2023-12-01 04:52:31 by cowbot92

[PORT] Adds several more signs for the bar to use (#20997)

* yo fuck emisssives

that shit sucks

* sure the rest of these can come too

I guess

* no 100% orange juice

sorry

---
## [Stutternov/f13tbd](https://github.com/Stutternov/f13tbd)@[f996624f34...](https://github.com/Stutternov/f13tbd/commit/f996624f34bd17872783cf0757300c93cc116f38)
#### Friday 2023-12-01 05:54:24 by foxymegneil

Enclave Marineification (#251)

## About The Pull Request

Changes all the icons and items of Enclave enlisted rank tabs (officer
tabs are the same between the Army and Marines) to be that of the Marine
Corps, while also adding some new ones that can be used for RP or
whatever. Also appropriately hands out said tabs. Private tab is GONE,
because it doesn't exist in the Marine Corps. You also may notice a
Petty Officer Third Class tab. What's that for? Well, it was originally
going to be for the Navy Corpsman loadout for the Specialist, however
loadouts seem to suffer with terminally low storage, so I wasn't able to
fit a rank tab into either of the loadouts. The item and icon are being
left in, however, just in case someone smarter than me can fix it.

Anyway, here are the sprites:

![sprites](https://github.com/f13babylon/f13babylon/assets/85942538/8b239726-1efb-43d3-a15d-731453df4a30)

## Why It's Good For The Game

We're Marines now! To hell with those Army tabs!
It's more immersive, and gosh darn it, that's all we Enclave players
have left. Immersion.

## Pre-Merge Checklist
- [x] You tested this on a local server.
- [x] This code did not runtime during testing.
- [x] You documented all of your changes.


## Changelog


:cl:
add: Adds some brand new Marine Corps tabs.
del: Old Army tabs that aren't needed anymore.
tweak: Changes some of the old tabs to new ones.
imageadd: New tabs!
imagedel: Old ones are gone.
/:cl:

---
## [Hatterhat/tgstation](https://github.com/Hatterhat/tgstation)@[9112509abd...](https://github.com/Hatterhat/tgstation/commit/9112509abd9507974928ea5d02676d0d0a58cbec)
#### Friday 2023-12-01 06:20:22 by KingkumaArt

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
## [mylove90/pc_ginkgo](https://github.com/mylove90/pc_ginkgo)@[3508678b60...](https://github.com/mylove90/pc_ginkgo/commit/3508678b601ff8b2e8682572e531ee1489648e79)
#### Friday 2023-12-01 06:35:05 by Jason A. Donenfeld

random: credit cpu and bootloader seeds by default

[ Upstream commit 846bb97e131d7938847963cca00657c995b1fce1 ]

This commit changes the default Kconfig values of RANDOM_TRUST_CPU and
RANDOM_TRUST_BOOTLOADER to be Y by default. It does not change any
existing configs or change any kernel behavior. The reason for this is
several fold.

As background, I recently had an email thread with the kernel
maintainers of Fedora/RHEL, Debian, Ubuntu, Gentoo, Arch, NixOS, Alpine,
SUSE, and Void as recipients. I noted that some distros trust RDRAND,
some trust EFI, and some trust both, and I asked why or why not. There
wasn't really much of a "debate" but rather an interesting discussion of
what the historical reasons have been for this, and it came up that some
distros just missed the introduction of the bootloader Kconfig knob,
while another didn't want to enable it until there was a boot time
switch to turn it off for more concerned users (which has since been
added). The result of the rather uneventful discussion is that every
major Linux distro enables these two options by default.

While I didn't have really too strong of an opinion going into this
thread -- and I mostly wanted to learn what the distros' thinking was
one way or another -- ultimately I think their choice was a decent
enough one for a default option (which can be disabled at boot time).
I'll try to summarize the pros and cons:

Pros:

- The RNG machinery gets initialized super quickly, and there's no
  messing around with subsequent blocking behavior.

- The bootloader mechanism is used by kexec in order for the prior
  kernel to initialize the RNG of the next kernel, which increases
  the entropy available to early boot daemons of the next kernel.

- Previous objections related to backdoors centered around
  Dual_EC_DRBG-like kleptographic systems, in which observing some
  amount of the output stream enables an adversary holding the right key
  to determine the entire output stream.

  This used to be a partially justified concern, because RDRAND output
  was mixed into the output stream in varying ways, some of which may
  have lacked pre-image resistance (e.g. XOR or an LFSR).

  But this is no longer the case. Now, all usage of RDRAND and
  bootloader seeds go through a cryptographic hash function. This means
  that the CPU would have to compute a hash pre-image, which is not
  considered to be feasible (otherwise the hash function would be
  terribly broken).

- More generally, if the CPU is backdoored, the RNG is probably not the
  realistic vector of choice for an attacker.

- These CPU or bootloader seeds are far from being the only source of
  entropy. Rather, there is generally a pretty huge amount of entropy,
  not all of which is credited, especially on CPUs that support
  instructions like RDRAND. In other words, assuming RDRAND outputs all
  zeros, an attacker would *still* have to accurately model every single
  other entropy source also in use.

- The RNG now reseeds itself quite rapidly during boot, starting at 2
  seconds, then 4, then 8, then 16, and so forth, so that other sources
  of entropy get used without much delay.

- Paranoid users can set random.trust_{cpu,bootloader}=no in the kernel
  command line, and paranoid system builders can set the Kconfig options
  to N, so there's no reduction or restriction of optionality.

- It's a practical default.

- All the distros have it set this way. Microsoft and Apple trust it
  too. Bandwagon.

Cons:

- RDRAND *could* still be backdoored with something like a fixed key or
  limited space serial number seed or another indexable scheme like
  that. (However, it's hard to imagine threat models where the CPU is
  backdoored like this, yet people are still okay making *any*
  computations with it or connecting it to networks, etc.)

- RDRAND *could* be defective, rather than backdoored, and produce
  garbage that is in one way or another insufficient for crypto.

- Suggesting a *reduction* in paranoia, as this commit effectively does,
  may cause some to question my personal integrity as a "security
  person".

- Bootloader seeds and RDRAND are generally very difficult if not all
  together impossible to audit.

Keep in mind that this doesn't actually change any behavior. This
is just a change in the default Kconfig value. The distros already are
shipping kernels that set things this way.

Ard made an additional argument in [1]:

    We're at the mercy of firmware and micro-architecture anyway, given
    that we are also relying on it to ensure that every instruction in
    the kernel's executable image has been faithfully copied to memory,
    and that the CPU implements those instructions as documented. So I
    don't think firmware or ISA bugs related to RNGs deserve special
    treatment - if they are broken, we should quirk around them like we
    usually do. So enabling these by default is a step in the right
    direction IMHO.

In [2], Phil pointed out that having this disabled masked a bug that CI
otherwise would have caught:

    A clean 5.15.45 boots cleanly, whereas a downstream kernel shows the
    static key warning (but it does go on to boot). The significant
    difference is that our defconfigs set CONFIG_RANDOM_TRUST_BOOTLOADER=y
    defining that on top of multi_v7_defconfig demonstrates the issue on
    a clean 5.15.45. Conversely, not setting that option in a
    downstream kernel build avoids the warning

[1] https://lore.kernel.org/lkml/CAMj1kXGi+ieviFjXv9zQBSaGyyzeGW_VpMpTLJK8PJb2QHEQ-w@mail.gmail.com/
[2] https://lore.kernel.org/lkml/c47c42e3-1d56-5859-a6ad-976a1a3381c6@raspberrypi.com/

Cc: Theodore Ts'o <tytso@mit.edu>
Reviewed-by: Ard Biesheuvel <ardb@kernel.org>
Signed-off-by: Jason A. Donenfeld <Jason@zx2c4.com>
Signed-off-by: Sasha Levin <sashal@kernel.org>

---
## [Lakszy/cap](https://github.com/Lakszy/cap)@[7c8d2ac197...](https://github.com/Lakszy/cap/commit/7c8d2ac197f7634ceace15d3ad3dde03efd9302c)
#### Friday 2023-12-01 07:07:17 by Lakshay Khattar

Add Email Validation Feature to HomePage.tsx

**Pull Request Description:**

**Description:**
This incredible masterpiece of code introduces a groundbreaking feature to the `HomePage` component – the ability to make users actually enter their email addresses. Say goodbye to the days of mysterious, empty submissions from users who apparently communicate telepathically.

**Changes Made:**
- Added state (`emailError`) to track email validation error messages.
- Updated the `handleSubmit` function to check for empty emails and display an error message if necessary.
- Modified JSX to display the error message in red, ensuring users get a hint about the existence of their keyboards.

**How to Test:**
1. Navigate to the `HomePage` component.
2. Attempt to submit the form without entering an email.
3. Witness the magic of a red error message gracefully reminding users to type something meaningful.

**Screenshots:**
Behold the beauty of an error message that tells users, "Your email is missing, genius!"

**Additional Notes:**
- Ensure you have sunglasses on when viewing the mesmerizing red error message.
- This groundbreaking feature has the potential to revolutionize the way we collect user data.

**Related Issue:**
Solve issue #8 

**Checklist:**
- [x] The code follows the project's coding standards because who needs standards?
- [x] Tests have been added because we love living on the edge.
- [x] The documentation has been updated because who doesn't love reading?

**Bounty Request:**
In recognition of the heroic effort put into solving this groundbreaking issue, I kindly request a bounty of one imaginary golden unicorn. If golden unicorns are in short supply, I will also accept a virtual high-five.

**Closing Note:**
May this code be forever remembered as the turning point in human-computer interaction history. Your gratitude and virtual unicorns are appreciated : )

---
## [Stalkeros2/Skyrat](https://github.com/Stalkeros2/Skyrat)@[8d69a6b49d...](https://github.com/Stalkeros2/Skyrat/commit/8d69a6b49df26a323e0a32f7a51ff7033fa5fd5a)
#### Friday 2023-12-01 07:43:27 by SkyratBot

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
## [Anushkadubeyy/Annnie-codes](https://github.com/Anushkadubeyy/Annnie-codes)@[2cdf3fbb82...](https://github.com/Anushkadubeyy/Annnie-codes/commit/2cdf3fbb8235b2a2f2c2eb853a091723575fc550)
#### Friday 2023-12-01 08:13:10 by Anushkadubeyy

Add files via upload

Welcome to our front-end website dedicated to showcasing the incredible talents of artists and photographers! Step into a world of artistic wonders as you explore our carefully curated collection of captivating images.

Our website is designed to provide a visually immersive experience, inviting you to dive into different artistic divisions such as art and photography. Each division offers a unique perspective, allowing you to appreciate the diverse forms of artistic expression.

Within the art division, you'll discover a rich tapestry of paintings, illustrations, and sculptures that showcase the boundless creativity of artists. From vibrant abstract compositions to intricate portraits and thought-provoking installations, these artworks will ignite your imagination and spark conversations.

In the photography division, you'll embark on a visual journey through captivating landscapes, mesmerizing portraits, and stunning moments frozen in time. Each photograph tells a story, capturing the essence of a fleeting moment or evoking powerful emotions.

As you navigate through our website, you'll find an intuitive navigation system that allows you to seamlessly switch between divisions. Immerse yourself in the world of art or delve into the realm of photography — the choice is yours. Discover new perspectives, find inspiration, and experience the beauty of art in its various forms.

To enhance your browsing experience, we've incorporated a preview feature that allows you to click on any image to open a larger view. Dive deeper into the details, appreciate the textures, and soak in the intricate nuances of each artwork or photograph.

We believe that art has the power to inspire, provoke thought, and foster connections. Our website aims to create a space where artists and art enthusiasts can come together, appreciate the beauty of creativity, and celebrate the talents of individuals who shape our artistic landscape.

Whether you're an artist seeking inspiration, a photography admirer, or simply someone who appreciates the beauty of art, we invite you to experience the magic of our front-end website. Open your eyes to a world of visual splendor, where art and photography intertwine, and be captivated by the limitless possibilities of human creativity.

Welcome to our artistic haven. Enjoy your exploration!

---
## [cowprotocol/services](https://github.com/cowprotocol/services)@[1fe4c4485a...](https://github.com/cowprotocol/services/commit/1fe4c4485a2d5d8a557ff663a5163c9d83f9ec25)
#### Friday 2023-12-01 09:46:52 by Martin Beckmann

Reduce memory consumption of `RecentBlockCache` (#2102)

# Description
Our `RecentBlockCache` works like this:
1. somebody requests liquidity
2. cache checks if it's already known
3. if it's not in the cache query the blockchain
4. store in cache
5. remember requested liquidity source for updating it in the background

Whenever we see a new block we fetch the current liquidity for all the
liquidity sources and write them to the cache together with their block.
We have a max cache duration. Whenever the cached state exceeds that
duration we remove the oldest entries.

This implementation uses unnecessarily much memory in 2 ways:
1. We can fetch liquidity for quotes. For those requests it's okay to
return liquidity that is not 100% up-to-date. However, we still remember
the requested liquidity source for future updates. This is not great
because we can receive quote requests for all sorts of random tokens
we'll never see again.
2. We cache state for the same liquidity source for multiple blocks. But
the cache only has 2 access patterns:
    * "Give me the most recent available on the blockchain"
    * "Give me the most recent available in the cache"
There is no access pattern "Give me cached liquidity specifically from
an older block with number X"
That means it's enough to keep the most recent data for any liquidity
pool cached at any point.
    
We can see these 2 things at play with this
[log](https://production-6de61f.kb.eu-central-1.aws.cloud.es.io/app/discover#/?_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:'2023-11-28T16:18:27.243Z',to:'2023-11-28T17:55:08.577Z'))&_a=(columns:!(log),filters:!(),grid:(columns:('@timestamp':(width:164))),index:c0e240e0-d9b3-11ed-b0e6-e361adffce0b,interval:auto,query:(language:kuery,query:'mainnet%20and%20driver%20and%20(log:%20%22the%20cache%20now%20contains%20entries%22%20or%20log:%20%22fetched%20liquidity%20sources%22)'),sort:!(!('@timestamp',desc)))).
After ~1h of operation it shows a single `RecentBlockCache` holding ~20K
items. On an average auction we can fetch ~800 uni v2 sources. We
currently have a configuration where we cache up to 10 blocks worth of
data. Meaning we have roughly 8K cache entries for liquidity that is
needed in auction and 12K entries that's only needed for quotes.
Also this is only for a single univ2 like liquidity source. In total we
have 4 different ones configured in our backend.

# Changes
We address `1` by not remembering liquidity sources for background
updates for quote requests.
We address `2` by throwing away all the duplicated data.

## How to test
I did a manual set up where I run an autopilot locally in shadow mode
(fetch auction from prod mainnet) and a driver with all liquidity
sources enabled.
I collected 3 graphs in total to measure the impact of this change on
the memory.
1. This graph is the status quo (very noisy and not really reproducable
across runs)
<img width="1617" alt="0_current_no_optimizations"
src="https://github.com/cowprotocol/services/assets/19190235/0997b34f-8f30-43c4-a797-5e3cf7bccbbf">

2. This graph applies one optimization that is not part of this PR to
make the memory consumption more predictable across runs. I want to
merge that optimization as well but right now it's very hacky. However,
I will include this optimization in all my graphs because it makes the
impact of each optimization easier to spot.
<img width="1420" alt="1_with_univ2_call_optimization"
src="https://github.com/cowprotocol/services/assets/19190235/6f259fa4-4fcd-45dd-ba37-160962065ab3">

3. The effects of this PR's optimization. The memory usage is more
stable over all and grows less over time.
<img width="1607" alt="2_cache_eviction"
src="https://github.com/cowprotocol/services/assets/19190235/ec5b5712-e4e3-4c4e-8feb-dc46e2cfa3f3">

---
## [jorisvandenbossche/arrow](https://github.com/jorisvandenbossche/arrow)@[3beb93af36...](https://github.com/jorisvandenbossche/arrow/commit/3beb93af36b3388a6871846365502c36ae4cfaa4)
#### Friday 2023-12-01 10:11:27 by Kevin Gurney

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
## [openedev/kernel](https://github.com/openedev/kernel)@[a06a4dc3a0...](https://github.com/openedev/kernel/commit/a06a4dc3a08201ff6a8a958f935b3cbf7744115f)
#### Friday 2023-12-01 10:50:54 by Neil Horman

kmod: add init function to usermodehelper

About 6 months ago, I made a set of changes to how the core-dump-to-a-pipe
feature in the kernel works.  We had reports of several races, including
some reports of apps bypassing our recursion check so that a process that
was forked as part of a core_pattern setup could infinitely crash and
refork until the system crashed.

We fixed those by improving our recursion checks.  The new check basically
refuses to fork a process if its core limit is zero, which works well.

Unfortunately, I've been getting grief from maintainer of user space
programs that are inserted as the forked process of core_pattern.  They
contend that in order for their programs (such as abrt and apport) to
work, all the running processes in a system must have their core limits
set to a non-zero value, to which I say 'yes'.  I did this by design, and
think thats the right way to do things.

But I've been asked to ease this burden on user space enough times that I
thought I would take a look at it.  The first suggestion was to make the
recursion check fail on a non-zero 'special' number, like one.  That way
the core collector process could set its core size ulimit to 1, and enable
the kernel's recursion detection.  This isn't a bad idea on the surface,
but I don't like it since its opt-in, in that if a program like abrt or
apport has a bug and fails to set such a core limit, we're left with a
recursively crashing system again.

So I've come up with this.  What I've done is modify the
call_usermodehelper api such that an extra parameter is added, a function
pointer which will be called by the user helper task, after it forks, but
before it exec's the required process.  This will give the caller the
opportunity to get a call back in the processes context, allowing it to do
whatever it needs to to the process in the kernel prior to exec-ing the
user space code.  In the case of do_coredump, this callback is ues to set
the core ulimit of the helper process to 1.  This elimnates the opt-in
problem that I had above, as it allows the ulimit for core sizes to be set
to the value of 1, which is what the recursion check looks for in
do_coredump.

This patch:

Create new function call_usermodehelper_fns() and allow it to assign both
an init and cleanup function, as we'll as arbitrary data.

The init function is called from the context of the forked process and
allows for customization of the helper process prior to calling exec.  Its
return code gates the continuation of the process, or causes its exit.
Also add an arbitrary data pointer to the subprocess_info struct allowing
for data to be passed from the caller to the new process, and the
subsequent cleanup process

Also, use this patch to cleanup the cleanup function.  It currently takes
an argp and envp pointer for freeing, which is ugly.  Lets instead just
make the subprocess_info structure public, and pass that to the cleanup
and init routines

Signed-off-by: Neil Horman <nhorman@tuxdriver.com>
Reviewed-by: Oleg Nesterov <oleg@redhat.com>
Cc: Andi Kleen <andi@firstfloor.org>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>

---
## [zxaber/tgstation](https://github.com/zxaber/tgstation)@[9229adc934...](https://github.com/zxaber/tgstation/commit/9229adc934b9575a8528b6efc0074fcc2921cc33)
#### Friday 2023-12-01 11:05:15 by DaydreamIQ

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
## [zxaber/tgstation](https://github.com/zxaber/tgstation)@[8c0becb4f0...](https://github.com/zxaber/tgstation/commit/8c0becb4f08ec50e00ed758022e18fb1381f4f25)
#### Friday 2023-12-01 11:05:15 by Da Cool Boss

Makes oculine taste slightly better (#79919)

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

---
## [openedev/kernel](https://github.com/openedev/kernel)@[4d6fa57b4d...](https://github.com/openedev/kernel/commit/4d6fa57b4dab0d77f4d8e9d9c73d1e63f6fe8fee)
#### Friday 2023-12-01 11:30:30 by Jason A. Donenfeld

macsec: avoid heap overflow in skb_to_sgvec

While this may appear as a humdrum one line change, it's actually quite
important. An sk_buff stores data in three places:

1. A linear chunk of allocated memory in skb->data. This is the easiest
   one to work with, but it precludes using scatterdata since the memory
   must be linear.
2. The array skb_shinfo(skb)->frags, which is of maximum length
   MAX_SKB_FRAGS. This is nice for scattergather, since these fragments
   can point to different pages.
3. skb_shinfo(skb)->frag_list, which is a pointer to another sk_buff,
   which in turn can have data in either (1) or (2).

The first two are rather easy to deal with, since they're of a fixed
maximum length, while the third one is not, since there can be
potentially limitless chains of fragments. Fortunately dealing with
frag_list is opt-in for drivers, so drivers don't actually have to deal
with this mess. For whatever reason, macsec decided it wanted pain, and
so it explicitly specified NETIF_F_FRAGLIST.

Because dealing with (1), (2), and (3) is insane, most users of sk_buff
doing any sort of crypto or paging operation calls a convenient function
called skb_to_sgvec (which happens to be recursive if (3) is in use!).
This takes a sk_buff as input, and writes into its output pointer an
array of scattergather list items. Sometimes people like to declare a
fixed size scattergather list on the stack; othertimes people like to
allocate a fixed size scattergather list on the heap. However, if you're
doing it in a fixed-size fashion, you really shouldn't be using
NETIF_F_FRAGLIST too (unless you're also ensuring the sk_buff and its
frag_list children arent't shared and then you check the number of
fragments in total required.)

Macsec specifically does this:

        size += sizeof(struct scatterlist) * (MAX_SKB_FRAGS + 1);
        tmp = kmalloc(size, GFP_ATOMIC);
        *sg = (struct scatterlist *)(tmp + sg_offset);
	...
        sg_init_table(sg, MAX_SKB_FRAGS + 1);
        skb_to_sgvec(skb, sg, 0, skb->len);

Specifying MAX_SKB_FRAGS + 1 is the right answer usually, but not if you're
using NETIF_F_FRAGLIST, in which case the call to skb_to_sgvec will
overflow the heap, and disaster ensues.

Signed-off-by: Jason A. Donenfeld <Jason@zx2c4.com>
Cc: stable@vger.kernel.org
Cc: security@kernel.org
Signed-off-by: David S. Miller <davem@davemloft.net>

---
## [stormbreaker-project/kernel_realme_salaa](https://github.com/stormbreaker-project/kernel_realme_salaa)@[110c3f3021...](https://github.com/stormbreaker-project/kernel_realme_salaa/commit/110c3f3021b0c4f23634799e5cd58e54658475ad)
#### Friday 2023-12-01 12:31:38 by Wang Han

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

---
## [Jasminlpz/app-dev.](https://github.com/Jasminlpz/app-dev.)@[dfbba8f23b...](https://github.com/Jasminlpz/app-dev./commit/dfbba8f23ba855996178d3b24de239cee2f591f6)
#### Friday 2023-12-01 13:10:11 by Jasminlpz

Update README.md

Bella Swan has always been a little bit different. Never one to run with the crowd, Bella never cared about fitting in with the trendy girls at her Phoenix, Arizona high school. When her mother remarries and Bella chooses to live with her father in the rainy little town of Forks, Washington, she doesn't expect much of anything to change. But things do change when she meets the mysterious and dazzlingly beautiful Edward Cullen. For Edward is nothing like any boy she's ever met. He's nothing like anyone she's ever met, period. He's intelligent and witty, and he seems to see straight into her soul. In no time at all, they are swept up in a passionate and decidedly unorthodox romance - unorthodox because Edward really isn't like the other boys. He can run faster than a mountain lion. He can stop a moving car with his bare hands. Oh, and he hasn't aged since 1918. Like all vampires, he's immortal. That's right - vampire. But he doesn't have fangs - that's just in the movies. And he doesn't drink human blood, though Edward and his family are unique among vampires in that lifestyle choice. To Edward, Bella is that thing he has waited 90 years for - a soul mate. But the closer they get, the more Edward must struggle to resist the primal pull of her scent, which could send him into an uncontrollable frenzy. Somehow or other, they will have to manage their unmanageable love. But when unexpected visitors come to town and realize that there is a human among them Edward must fight to save Bella? A modern, visual, and visceral Romeo and Juliet story of the ultimate forbidden love affair - between vampire and mortal.

---
## [Sonic-Geared/Scarlet-Engine](https://github.com/Sonic-Geared/Scarlet-Engine)@[ed8e108868...](https://github.com/Sonic-Geared/Scarlet-Engine/commit/ed8e1088682fdadacacca018f021627ba51aa4c6)
#### Friday 2023-12-01 13:24:19 by Geared

sorry but the Mario & Luigi Dream Team OST goes even harder

Github won't let me revert commits so this is the way we handle shit for here =/

---
## [NightSlasher35/Bot](https://github.com/NightSlasher35/Bot)@[496f658f6b...](https://github.com/NightSlasher35/Bot/commit/496f658f6bec62078a35f9a4930647acdf6cd744)
#### Friday 2023-12-01 13:29:22 by NightSlasher35

does it work? we'll find out if someone fucking uses this shit

---
## [jstenmark/ChatCopyCat](https://github.com/jstenmark/ChatCopyCat)@[8e855c9175...](https://github.com/jstenmark/ChatCopyCat/commit/8e855c91754a7e475881c25917cc7223abeb66da)
#### Friday 2023-12-01 13:36:30 by JStenmark

Woody: What's going on, Mr. Peterson?
Norm:  Let's talk about what's going *in* Mr. Peterson.  A beer, Woody.
		-- Cheers, Paint Your Office

Sam:  How's life treating you?
Norm: It's not, Sammy, but that doesn't mean you can't.
		-- Cheers, A Kiss is Still a Kiss

Woody:  Can I pour you a draft, Mr. Peterson?
Norm:   A little early, isn't it Woody?
Woody:  For a beer?
Norm:   No, for stupid questions.
		-- Cheers, Let Sleeping Drakes Lie

---
## [cly-build/kernel_xiaomi_rosemary](https://github.com/cly-build/kernel_xiaomi_rosemary)@[84a710d7e2...](https://github.com/cly-build/kernel_xiaomi_rosemary/commit/84a710d7e2c5a76c9a2d3c87e7707b8f2efd4b61)
#### Friday 2023-12-01 13:50:09 by Peter Zijlstra

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
Change-Id: Idd54334615da4c78698ca8b3b12b514ae9d8360f
Signed-off-by: Alexander Winkowski <dereference23@outlook.com>

---
## [M-D-Team/ait-fabric-1.20.1](https://github.com/M-D-Team/ait-fabric-1.20.1)@[f67567540d...](https://github.com/M-D-Team/ait-fabric-1.20.1/commit/f67567540dbfffb6eebd97529babba7a9c8f636c)
#### Friday 2023-12-01 13:55:53 by Loqor

uhhh, fuck you? cope, seethe, mald?
added borealis console, emission, texture, blah blah blah. i dont know how to do the animation state stuff, and its genuinely starting to piss me off bad.
5 things i want finished before i come back to working on this:
- datagen is FIXED
- the components (except for the radio) are REMOVED and REDONE
- the animations for the borealis console WORK, and make sense
- using collections instead of immutableMaps to store the exteriors/consoles so we can actually use them properly and change them out.
_ and finally the console entities work and spawn with the console.

---
## [JbYvonne/app-dev](https://github.com/JbYvonne/app-dev)@[c1c4f2ce26...](https://github.com/JbYvonne/app-dev/commit/c1c4f2ce2650e365058b2e2405eb02cef938f04f)
#### Friday 2023-12-01 14:07:08 by JbYvonne

Update README.md

Elemental

Elemental is a new animated rom-com drama film by Disney Pixar,Despite being warm and colorful in its visuals and seeming like a kids’ film at first glance, Elemental does talk about real-world issues and struggles that many youngsters grow up around in this modern day.
Eventually, though, the couple comes across a rundown house with water pipes leaking all over it that has been put up for sale. Bernie immediately decides to buy the house and settle his family here.Also However, she has to face an even more difficult task when a horrible water leak in their basement threatens the very existence of their eatery.




Moana 2016


An adventurous teenager sails out on a daring mission to save her people. During her journey, Moana meets the once-mighty demigod Maui, who guides her in her quest to become a master wayfinder. Together, they sail across the open ocean on an action-packed voyage, encountering enormous monsters and impossible odds. Along the way, Moana fulfills the ancient quest of her ancestors and discovers the one thing she always sought, her own identity.

Squid games

A story of people who fail at life for various reasons, but suddenly receive a mysterious invitation to participate in a survival game to win more than 38 million US dollars. The game takes place on an isolated island and the participants are locked up until there is a final winner. The story incorporates popular Korean children's games from the 1970s and 1980s, such as squid game, the literal translation of its Korean name, which is a type of tag where offense and defense use a squid-shaped board drawn in the dirt.


Shes dating with the gangster

It all started when 17-year-old Athena Dizon unwittingly plays a trick on resident heartthrob and bad boy, Kenji de los Reyes. All of a sudden, she finds herself pretending-unwillingly at that-to be his girlfriend to make his ex jealous. Now, not only does she have to deal with dirty looks from the girls in school who want Kenji for themselves, but her supposed boyfriend is getting on her nerves. He's hotheaded, never seems to agree with her on anything-and everything about him screams gangster.

---
## [TwistedCicrularConvexLens/tgstation](https://github.com/TwistedCicrularConvexLens/tgstation)@[08ab5d2731...](https://github.com/TwistedCicrularConvexLens/tgstation/commit/08ab5d27312d236593eabdb27fb23dccbf8283e6)
#### Friday 2023-12-01 14:47:46 by Mothblocks

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
## [Cellzawy/WATCH-IT-JAVA](https://github.com/Cellzawy/WATCH-IT-JAVA)@[0fc92b4e58...](https://github.com/Cellzawy/WATCH-IT-JAVA/commit/0fc92b4e58e883896057b37759fee0dbeb1651eb)
#### Friday 2023-12-01 15:13:35 by Alinist

WE FUCKING DID IT !!!!!!
as we said before....WE ARE FREEEEEEE!!!!!

by ali and ali
and fuck you all

---
## [IFuckedUpMerging/Shiptest](https://github.com/IFuckedUpMerging/Shiptest)@[223dc74ef1...](https://github.com/IFuckedUpMerging/Shiptest/commit/223dc74ef1f528e2c29b0e62271ddaf7b68d79d8)
#### Friday 2023-12-01 15:23:32 by retlaw34

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
## [IFuckedUpMerging/Shiptest](https://github.com/IFuckedUpMerging/Shiptest)@[389d1e5669...](https://github.com/IFuckedUpMerging/Shiptest/commit/389d1e566990682f173066df4c16f25b3a1858c0)
#### Friday 2023-12-01 15:23:32 by Erika Fox

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
## [IFuckedUpMerging/Shiptest](https://github.com/IFuckedUpMerging/Shiptest)@[88e683cec6...](https://github.com/IFuckedUpMerging/Shiptest/commit/88e683cec669624228d5204d7e3da06e6075d158)
#### Friday 2023-12-01 15:23:32 by zevo

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
## [SWE-B5/SpottingSmallPrints](https://github.com/SWE-B5/SpottingSmallPrints)@[3b18914e48...](https://github.com/SWE-B5/SpottingSmallPrints/commit/3b18914e488aa00c76f987e42b78ea0a4ca196bd)
#### Friday 2023-12-01 15:27:44 by Philogex

Merge branch 'bitmap' of https://github.com/SWE-B5/SpottingSmallPrints into Level3
i hate my life

---
## [civilCornball/misc-city-changes](https://github.com/civilCornball/misc-city-changes)@[2defb31817...](https://github.com/civilCornball/misc-city-changes/commit/2defb31817005f7790e9586ace0c4e77c23d7f06)
#### Friday 2023-12-01 16:03:03 by vampirebat74

Adds Red Shoes (#901)

Mr. Heavenly's Abnormality Jam Entry #1

Records

uncommented weapon

Finishing touches

Design rework

adds ego gift and inhands

New sprites!

uncommented sfx

insanity fix

quieter sound loop

Fixes some shit

fix linters

requested changes

Adds Red Shoes

Mr. Heavenly's Abnormality Jam Entry #1

Records

uncommented weapon

Finishing touches

Design rework

adds ego gift and inhands

New sprites!

uncommented sfx

insanity fix

quieter sound loop

Fixes some shit

fix linters

requested changes

Update code/modules/mob/living/simple_animal/abnormality/he/red_shoes.dm

fixes suit check in assimilate() proc

Co-authored-by: [̸R̵e̵d̴a̴c̶t̸e̸d̴]̵ <61567407+LanceSmites328@users.noreply.github.com>

Update code/modules/mob/living/simple_animal/abnormality/he/red_shoes.dm

fixes dismembering

Co-authored-by: [̸R̵e̵d̴a̴c̶t̸e̸d̴]̵ <61567407+LanceSmites328@users.noreply.github.com>

Update code/modules/mob/living/simple_animal/abnormality/he/red_shoes.dm

Co-authored-by: [̸R̵e̵d̴a̴c̶t̸e̸d̴]̵ <61567407+LanceSmites328@users.noreply.github.com>

breach is more dangerous

compiles

bug fix

fixes simple mob

bug fixes

Panic fixed!!!!

stuff

wayward records

Update code/modules/paperwork/records/info/he.dm

Co-authored-by: [̸R̵e̵d̴a̴c̶t̸e̸d̴]̵ <61567407+LanceSmites328@users.noreply.github.com>

Update code/modules/mob/living/simple_animal/abnormality/he/red_shoes.dm

Co-authored-by: [̸R̵e̵d̴a̴c̶t̸e̸d̴]̵ <61567407+LanceSmites328@users.noreply.github.com>

attribute bonus

requested changes

Co-authored-by: Mr.Heavenly <davidx3adamhunt@gmail.com>

---
## [thozza/osbuild-images](https://github.com/thozza/osbuild-images)@[6c07ef12e1...](https://github.com/thozza/osbuild-images/commit/6c07ef12e19d27f24c10db9083149f11e7ba522d)
#### Friday 2023-12-01 16:03:08 by Tomáš Hozza

distro/el9: refactor package sets to again use `@core` pkg group

Previously, we used a fixed package list from RHEL-9.0 times, instead of
the `@core` pkg group, for all images which previously used it. The
motivation is that some packages got removed from the group in 9.0
(specifically tuned), which went almost unnoticed. The reasoning is that
a fixed list would give us more control over the package set and prevent
unexpected package removals.

However, with COMPOSER-2074 [1], it turned out that this also meant that
any new packages added to the `@core` group won't be automatically added
to any image which previously used the package group. People still have
(anyhow incorrect) expectation that `@core` pkg group is always
installed on RHEL images and thus that adding a package to the group
would also add it to vanilla RHEL images.

We discussed this shortly within the team and reverting back to using
`@core` package group, instead of a fixed package list, seems like the
lesser evil.

Modify package set definitions, which used `coreOsCommonPackageSet()` to
use `@core` package group instead. Modify the exclude lists accordingly
to achieve almost the same image content as before. There are a few
exceptions:

 - `rhc` package is now installed, which is desired.
 - `insights-client` is now installed on some images where it was
   previously not. This is OK, since RHEL is aiming for a "connected
   experience" by default. This also results in a few additional
   packages to be pulled in as dependencies, specifically:
   - `python3-file-magic`
   - `policycoreutils-python-utils`
   - `tar`
   - `pciutils`
 - `initscripts-rename-device` is now installed. This sub-package has
   been split out of the `initscripts` pakcage on el9, but it was not
   included in the `@core` group definition, when we created the fixed
   pkg list. Howver, it is now the default member of the group. The
   functionality was previously installed by default on el8 images via
   the `initscripts` package. After talking to the maintainer, I kept it
   in the images as a new package.

Affected images by this change:
 - ami
 - gce
 - gce_rhui
 - image_installer
 - oci
 - openstack
 - ova
 - qcow2
 - vmdk

[1] https://issues.redhat.com/browse/COMPOSER-2074

Signed-off-by: Tomáš Hozza <thozza@redhat.com>

---
## [MoonlightCapital/MoonlightBot-docs](https://github.com/MoonlightCapital/MoonlightBot-docs)@[ef85b0786a...](https://github.com/MoonlightCapital/MoonlightBot-docs/commit/ef85b0786a35edc45c5220f93769cdf775cd7096)
#### Friday 2023-12-01 16:09:03 by MoonlightCapital

Update server location in pivacy policy following host change

oh as you can see, there are no abortion rights,
and when trump will be jailed, you will all begin screaming

you can buy many guns, and not use kilograms,
when you know you have failed, (idk how to continue here)

and the commies' red flags, the bombs bursting on land,
gave us proof through the night, that america is bad

oh turn that star-spangled banner for god's sake,
on the grave of the free, and the home of the slave

---
## [privatevoid-net/depot](https://github.com/privatevoid-net/depot)@[993cb7f967...](https://github.com/privatevoid-net/depot/commit/993cb7f967b15c36a626573d98f0fbecabdbfa8c)
#### Friday 2023-12-01 17:34:43 by Max

cluster/services/hercules-ci-multi-agent: disable AWS IMDS lookups

so this was the reason hci has been so fucking slow substituting things

fuck you, jeff

---
## [unclamped/aoc-2023](https://github.com/unclamped/aoc-2023)@[e110695781...](https://github.com/unclamped/aoc-2023/commit/e1106957810388cb2c3fffda6e651acb0f33d1a6)
#### Friday 2023-12-01 17:51:04 by unclamped

i fucking hated this so much

i was happy, happy as fucking fuck, until I realized in part 2 that my solution was wrong. I checked and checked and couldn't realize why, until I saw in the input something. `oneight`. I wondered "wait, is this supposed to be 1, 8 or 1?
after asking, the worst outcome came true. it was 1 8. at the time I was using regex, so I started looking for ways of somehow making the regex match overlaps. that took me probably an hour or two, and then after I found how it was supposed to be done (capture group lookahead), it worked in the sense of it detecting the overlapping numbers through an array, but it would return them as fucking null. i spent probably another hour trying to figure out why, and then I gave up on regex altogether.
another hour or two, and I made the monster that is part2's code. regex by fucking hand, iterating through each single fucking character by myself, i don't even care about trying to make this look pretty or polished or finished or optimized, I'm fucking done with this exercise. i am completing the rest of this advent because I am not a pussy, but MY FUCKING GOD if the rest of the exercises end up being this same shit, I am not touching it with a pole ever again.
the worst part is that not even the examples in the aoc page accounted for this, so they never made an example where you had something like `oneight`, that was a big mistake.
i am also not ever using javascript again on this advent, fuck you js.

---
## [lalalilac/Lalaina-Chandanais](https://github.com/lalalilac/Lalaina-Chandanais)@[8edf736044...](https://github.com/lalalilac/Lalaina-Chandanais/commit/8edf7360448745c8a667f297edc55da62fd5b348)
#### Friday 2023-12-01 18:06:50 by lalalilac

Update gh-pages

Autumn Evenings: This is a sketch I made where I first played around with the concept of inserting images into my p5.js sketches. I added an image of myself in my Halloween costume this year, as well as an image of daisies that you can move and contort. Atop everything is a gif image of golden cartoon sparkles to tie the piece together.
Flashy Spice: This was by far the most complex sketch I have made this semester, as it uses the library _p5.speak_ to use voice recognition software and listen for specific keywords in order to perform an action. I made it so that if the system hears the words "green" or "orange", it will turn those colors and repeat the words back to you.
Snow in the Night: This sketch was where I made an infinite loop of small snow particles falling from a certain point on the canvas and covered that point with contorted ellipses to appear like a snow cloud.

---
## [lalalilac/Lalaina-Chandanais](https://github.com/lalalilac/Lalaina-Chandanais)@[45ba86c798...](https://github.com/lalalilac/Lalaina-Chandanais/commit/45ba86c798a9805340bb43b47355f836d3fccdcc)
#### Friday 2023-12-01 18:15:10 by lalalilac

Create README.md

Autumn Evenings: This is a sketch I made where I first played around with the concept of inserting images into my p5.js sketches. I added an image of myself in my Halloween costume this year, as well as an image of daisies that you can move and contort. Atop everything is a gif image of golden cartoon sparkles to tie the piece together.
Flashy Spice: This was by far my most complex sketch I have made this semester, as it uses the library _p5.speak_ to use voice recognition software and listen for specific keywords in order to perform an action. I made it so that if the system hears the words "green" or "orange", it will turn those colors and repeat the words back to you.
Snow in the Night: This sketch was where I made an infinite loop of small snow particles falling from a certain point on the canvas and covered that point with contorted ellipses to appear like a snow cloud.

---
## [panzerr1944/f13tbd](https://github.com/panzerr1944/f13tbd)@[ccb9ce38a7...](https://github.com/panzerr1944/f13tbd/commit/ccb9ce38a7e26763f93c089bd0a65c9e35b70243)
#### Friday 2023-12-01 18:28:14 by panzerr1944

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
## [panzerr1944/f13tbd](https://github.com/panzerr1944/f13tbd)@[9bc0add065...](https://github.com/panzerr1944/f13tbd/commit/9bc0add065315cba3de80a2cc1feac5fe08e9fed)
#### Friday 2023-12-01 18:28:14 by Stutternov

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
## [panzerr1944/f13tbd](https://github.com/panzerr1944/f13tbd)@[830db814f3...](https://github.com/panzerr1944/f13tbd/commit/830db814f3104bfe595db02eea0759766eb2cd10)
#### Friday 2023-12-01 18:28:14 by GreytidePanda

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
## [kleinerm/Psychtoolbox-3](https://github.com/kleinerm/Psychtoolbox-3)@[c0de7b4462...](https://github.com/kleinerm/Psychtoolbox-3/commit/c0de7b4462c99b5a22664ce4633ad6b47c80d872)
#### Friday 2023-12-01 19:15:53 by Mario Kleiner

IOPort: Fix 'OpenSerialPort' bugs where default settings override user settings.

As GitHub user @qx1147 found out during a code review, there is a flaw in
the handling of serial port options, where default serial port options may
override user provided configuration options, so the wrong settings are
silently applied! This only happens if the user script provides different
settings in IOPort('OpenSerialPort', ..., settings), ie. on initial port
open. Calls to IOPort('ConfigureSerialPort', ..., settings) are not
affected.

Patch this up by reordering the if-else ladders for Unix and Windows:
Default settings must come as the last else-if-else block before the
error handling for invalid parameters. This way, user provided non-default
settings for serial port parameters take precedence over the built in
defaults, as intended.

Luckily (dumb luck!), only a few options were mishandled, and most of these
are rarely changed by user scripts, specifically:

ProcessingMode=Cooked would get ignored, and raw mode used instead. Rarely
used on Linux/macOS and not supported on Windows anyways. Low impact.

BreakBehaviour=Ignore would be used instead of Flush or Zero. Not a
problem on Windows, as that is the only supported option. The fact that
this went unnoticed on Linux/macOS suggests not much use of Flush or Zero
by users scripts. No use by PTB itself. Low expected impact. Note that the
implementation of 'Flush' on the Unixes is of questionable use, as Flush
would not only flush read/write buffers, but also send a SIGINT, which may
end in unexpected ways on Unix, as we don't handle SIGINT specifically.

StopBits=2 would get ignored and the default of 1 stop bits would be used.
Unclear how many devices want 2 stop bits, but I haven't ever seen one, so
probably low expected impact.

DataBits=16 would get ignored on MS-Windows only and replaced by 8 bits,
whereas other settings are fine, and 16 bits is unsuported on Linux/macOS,
so probably rarely if ever used. Low expected impact.

FlowControl=None will be used instead of hardware or software flow control.
This can be a real bummer with potential real impact, as some devices do
support or recommend active flow control! In the case of PTB, the
CedrusResponseBox() driver for Cedrus response box devices would have
liked that setting.


Audit of Psychtoolbox internal user of IOPort, and of the demos, only
shows one bad case where things went sideways: CedrusResponseBox.m
This driver requested hardware flow control, but silently got instead NO
flow control! This is interesting, because during my testing I found
communication with Cedrus boxes always rather unreliable, and now I have
to wonder if this was because of the accidental lack of hardware flow
control? I can't find out, as I lost access to Cedrus devices long ago.

This whole parameter handling is somewhat fragile, and could do with an
improved implementation, but due to the severe lack of financial funding
for PTB, this is not an option in the foreseeable future. Not even code
review or testing of 3rd party contributions, if there were any. Luckily
this part of the driver is mostly static since years, so I guess we can
drag our feet longer and sit it out.

Another problem pointed out by @qx1147 is indeed that wrong options, e.g.,
due to typos in users experiment scripts, would not lead to an error abort
or warning, but would get silently ignored in many cases. Not great at all,
but lack of funding will leave this problems also unsolved in the near- to
midterm, possibly forever. Life sucks...

See also PR #262 for discussion. Thanks to @qx1147 for catching this!

Work time spent on IOPort improvements: 5 hours, resulting in loss of
at least 1000 Euros of billable time to the project!

---
## [osbuild/images](https://github.com/osbuild/images)@[7152886364...](https://github.com/osbuild/images/commit/715288636474b85551fdf53478754d931c6fafa8)
#### Friday 2023-12-01 19:24:23 by Tomáš Hozza

distro/el9: refactor package sets to again use `@core` pkg group

Previously, we used a fixed package list from RHEL-9.0 times, instead of
the `@core` pkg group, for all images which used it on el8. The
motivation was that some packages got removed from the group in 9.0
(specifically tuned), which went almost unnoticed. The reasoning was that
a fixed list would give us more control over the package set and prevent
unexpected package removals.

However, with COMPOSER-2074 [1], it turned out that this also meant that
any new packages added to the `@core` group won't be automatically added
to any image which previously used the `@core` group. People still have
(anyhow incorrect) expectation that `@core` pkg group is always
installed on RHEL images and thus that adding a package to the group
will also add it to vanilla RHEL images.

We discussed this shortly within the team and reverting back to using
`@core` package group, instead of a fixed package list, seems like the
lesser evil.

Modify package set definitions, which used `coreOsCommonPackageSet()` to
use `@core` package group instead. Modify the exclude lists accordingly
to achieve almost the same image content as before. There are a few
exceptions:

 - `rhc` package is now installed, which is desired.
 - `insights-client` is now installed on some images where it was
   previously not. This is OK, since RHEL is aiming for a "connected
   experience" by default. This also results in a few additional
   packages to be pulled in as dependencies, specifically:
   - `python3-file-magic`
   - `policycoreutils-python-utils`
   - `tar`
   - `pciutils`
 - `initscripts-rename-device` is now installed. This sub-package has
   been split out of the `initscripts` package on el9, but it was not
   included in the `@core` group definition, when we created the fixed
   pkg list. However, it is now the default member of the group. The
   functionality was previously installed by default on el8 images via
   the `initscripts` package. After talking to the maintainer, I kept it
   in the images as a new package.

Affected images by this change:
 - ami
 - gce
 - gce_rhui
 - image_installer
 - oci
 - openstack
 - ova
 - qcow2
 - vmdk

Some of the listed images already contained `rhc` or `insights-client`,
but now, these are consistently installed on all of them. This is the
case since 9.2, when `rhc` was added to the `@core` group.

`initscripts-rename-device` has been added to all of these image types,
inlcuding on CentOS Stream 9 images.

[1] https://issues.redhat.com/browse/COMPOSER-2074

Signed-off-by: Tomáš Hozza <thozza@redhat.com>

---
## [silencer-pl/cmss13](https://github.com/silencer-pl/cmss13)@[2011c229f9...](https://github.com/silencer-pl/cmss13/commit/2011c229f9a37de8fa67a74d8e40974515724cde)
#### Friday 2023-12-01 20:05:46 by stalkerino

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
## [silencer-pl/cmss13](https://github.com/silencer-pl/cmss13)@[f367771f57...](https://github.com/silencer-pl/cmss13/commit/f367771f5799b87257d92cb79db71bcd85b62f75)
#### Friday 2023-12-01 20:05:46 by Birdtalon

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
## [silencer-pl/cmss13](https://github.com/silencer-pl/cmss13)@[a955791561...](https://github.com/silencer-pl/cmss13/commit/a955791561d5aeab0ff0640923fe1192ad377830)
#### Friday 2023-12-01 20:05:46 by fira

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
## [kartiksahu82/Code-Soft](https://github.com/kartiksahu82/Code-Soft)@[25f90c1e4f...](https://github.com/kartiksahu82/Code-Soft/commit/25f90c1e4f5e17d04d7cab10094ed1361fe8b7d1)
#### Friday 2023-12-01 20:23:43 by Kartik Sahu

Add files via upload

🚀 Welcome to my GitHub repository showcasing a practical calculator project created during my internship at #codesoft!

🧮 Project Overview:
Explore this functional calculator developed using Java, HTML, and CSS. It's more than just numbers; it’s a blend of calculations, interactive elements with transitions, and CSS styles that make calculations an engaging experience.

🎨 Design Elements:
Discover how transitions, transforms, and CSS styles elevate this calculator, making it both visually appealing and user-friendly.

💡 Key Features:
Experience the seamless functionality of this calculator, where Java handles calculations while HTML and CSS bring the design to life.

🔍 Internship Impact:
The #codesoft internship empowered me to apply Java in a practical setting, combining it with front-end technologies to create a useful and captivating tool.

🌟 Future Innovations:
Continuously refining my skills to develop more innovative projects that merge functionality with aesthetics.

📧 Get in Touch:
For collaborations, feedback, or discussions, feel free to reach out via email. Your insights are valuable!

Thank you for exploring this repository! Let's continue building practical and engaging projects together! 🌟

---
## [chirag127/adfilt](https://github.com/chirag127/adfilt)@[e08e13557c...](https://github.com/chirag127/adfilt/commit/e08e13557cc0bb9f2a8b7b625d942dcd688a19b2)
#### Friday 2023-12-01 20:27:52 by Imre Kristoffer Eilertsen

Update AntiCorruptSportsList.txt

The phrase "Fuck this shit" is warranted by now. Professional diplomatic language be damned.

---
## [Latentish/Shiptest](https://github.com/Latentish/Shiptest)@[caa19d2a6f...](https://github.com/Latentish/Shiptest/commit/caa19d2a6f8014c2d34663c7c63685921bc0218a)
#### Friday 2023-12-01 20:28:05 by GenericDM

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
## [clayne/Depth3D](https://github.com/clayne/Depth3D)@[8f5b8af1a0...](https://github.com/clayne/Depth3D/commit/8f5b8af1a07fe94071ff0fd5179c12240ab0476b)
#### Friday 2023-12-01 21:09:22 by BlueSkyDefender

Update 3.9.9

Re Worked How weapon Hands are handled when using secondary options.

 Weapon ZPD was set to a constant internal Value of 0.030 Since it was not used anyways. This old value just fell out of use.

It was Replaced with Weapon Near much more useful in modern games.

Near Plane Based Range Boost now goes up to 4x.

FPS Focus was reworked now you can control Weapon and World options separately and it goes up 8 steps.

Internal code changes
Simple Menu Masking now can be made more stick.

Weapon Distance From Bottom control was added.

Overwatch

Added Options to control all new options.

Overwatch Profiles

+FATAL Frame Mask oft he Lunar
+FATAL Frame Maiden of the Black Water

Profiles Updated
+Half-Life 2
+Tiny Tina's Wonderlands
+Wolfenstein: The New Order
+Wolfenstein: The Old Blood
+Resident Evil 7
+Gold Source AKA Half-Life games
+Sinned

---
## [clayne/oiio](https://github.com/clayne/oiio)@[b8723ec691...](https://github.com/clayne/oiio/commit/b8723ec6918b9204d040c495eba8c8d21484df53)
#### Friday 2023-12-01 21:30:50 by Larry Gritz

fix(oiiotool): --autocc bugfix and color config inventory cleanup (#4060)

The important bug fix is in oiiotool image input when autocc is used,
where we reversed the sense of a test and did the autocc-upon-input if
the file's color space was equivalent to the scene_linear space
(pointlessly), and skipped the conversion if they were different (oh no,
big bug!).

Along the way:

* Add missing try/catch around OCIO call that should have had it.

* Some very ugly SPI-specific recognize-by-name color space heuristics.
I hate this, sorry, but it solves a really important problem for me.

* A bunch of additional debugging messages during color space inventory,
enabled only when debugging, so nobody should see these but me.

* A couple places where we canonicalize the spelling of
"oiio:ColorSpace".

Note that there is still an issue with the color space classification
using OCIO 2.3+'s identification of built-in equivalents by name. These
are shockingly expensive. I will return to this later.

Signed-off-by: Larry Gritz <lg@larrygritz.com>

---
## [kartiksahu82/Code-Soft](https://github.com/kartiksahu82/Code-Soft)@[f94f52ddf6...](https://github.com/kartiksahu82/Code-Soft/commit/f94f52ddf608649a605c1488bcaf629b6fb4d230)
#### Friday 2023-12-01 21:36:02 by Kartik Sahu

Add files via upload

🚀 Welcome to my GitHub repository showcasing my tribute page project developed during my #codesoft internship!

🌟 Project Overview:
Explore my tribute page, a culmination of creativity and skills developed during the internship. Crafted using HTML, CSS, and JavaScript, this project highlights unique hover effects, transitions, and transforms, creating an engaging and visually appealing site.

🛠️ Technologies Used:
HTML laid the foundation, CSS stylized elements, and JavaScript added interactivity. Together, these technologies brought life to the tribute page, showcasing the power of frontend development.

🎨 Design Elements:
Experience intriguing hover effects and captivating transitions, demonstrating a blend of creativity and technical expertise in crafting an interesting and interactive web experience.

🔍 Internship Impact:
The #codesoft internship provided the platform to explore innovative techniques and apply them to real projects. This project reflects the skills honed during this valuable learning experience.

📁 Future Plans:
Continuously enhancing this tribute page and exploring new ways to incorporate advanced features. Stay tuned for updates as I push the boundaries of web design!

🌟 Connect and Collaborate:
Feel free to explore, provide feedback, or collaborate on this project. I'm open to discussions and eager to collaborate on exciting projects!

📧 Contact:
For inquiries or collaborations, reach out via email. Your insights and contributions are greatly appreciated!

Thank you for visiting my tribute page repository! Let's continue crafting intriguing and innovative web solutions together! 🌟

---
## [clayne/ripgrep](https://github.com/clayne/ripgrep)@[082245dadb...](https://github.com/clayne/ripgrep/commit/082245dadb3854238e62b91aa95a46018cf16ef1)
#### Friday 2023-12-01 21:40:02 by Andrew Gallant

cli: replace clap with lexopt and supporting code

ripgrep began it's life with docopt for argument parsing. Then it moved
to Clap and stayed there for a number of years. Clap has served ripgrep
well, and it probably could continue to serve ripgrep well, but I ended
up deciding to move off of it.

Why?

The first time I had the thought of moving off of Clap was during the
2->3->4 transition. I thought the 3.x and 4.x releases were great, but
for me, it ended up moving a little too quickly. Since the release of
4.x was telegraphed around when 3.x came out, I decided to just hold off
and wait to migrate to 4.x instead of doing a 3.x migration followed
shortly by another 4.x migration. Of course, I just never ended up doing
the migration at all. I never got around to it and there just wasn't a
compelling reason for me to upgrade. While I never investigated it, I
saw an upgrade as a non-trivial amount of work in part because I didn't
encapsulate the usage of Clap enough.

The above is just what got me started thinking about it. It wasn't
enough to get me to move off of it on its own. What ended up pushing me
over the edge was a combination of factors:

* As mentioned above, I didn't want to run on the migration treadmill.
This has proven to not be much of an issue, but at the time of the
2->3->4 releases, I didn't know how long Clap 4.x would be out before a
5.x would come out.
* The release of lexopt[1] caught my eye. IMO, that crate demonstrates
exactly how something new can arrive on the scene and just thoroughly
solve a problem minimalistically. It has the docs, the reasoning, the
simple API, the tests and good judgment. It gets all the weird corner
cases right that Clap also gets right (and is part of why I was
originally attracted to Clap).
* I have an overall desire to reduce the size of my dependency tree. In
part because a smaller dependency tree tends to correlate with better
compile times, but also in part because it reduces my reliance and trust
on others. It lets me be the "master" of ripgrep's destiny by reducing
the amount of behavior that is the result of someone else's decision
(whether good or bad).
* I perceived that Clap solves a more general problem than what I
actually need solved. Despite the vast number of flags that ripgrep has,
its requirements are actually pretty simple. We just need simple
switches and flags that support one value. No multi-value flags. No
sub-commands. And probably a lot of other functionality that Clap has
that makes it so flexible for so many different use cases. (I'm being
hand wavy on the last point.)

With all that said, perhaps most importantly, the future of ripgrep
possibly demands a more flexible CLI argument parser. In today's world,
I would really like, for example, flags like `--type` and `--type-not`
to be able to accumulate their repeated values into a single sequence
while respecting the order they appear on the CLI. For example, prior
to this migration, `rg regex-automata -Tlock -ttoml` would not return
results in `Cargo.lock` in this repository because the `-Tlock` always
took priority even though `-ttoml` appeared after it. But with this
migration, `-ttoml` now correctly overrides `-Tlock`. We would like to
do similar things for `-g/--glob` and `--iglob` and potentially even
now introduce a `-G/--glob-not` flag instead of requiring users to use
`!` to negate a glob. (Which I had done originally to work-around this
problem.) And some day, I'd like to add some kind of boolean matching to
ripgrep perhaps similar to how `git grep` does it. (Although I haven't
thought too carefully on a design yet.) In order to do that, I perceive
it would be difficult to implement correctly in Clap.

I believe that this last point is possible to implement correctly in
Clap 2.x, although it is awkward to do so. I have not looked closely
enough at the Clap 4.x API to know whether it's still possible there. In
any case, these were enough reasons to move off of Clap and own more of
the argument parsing process myself.

This did require a few things:

* I had to write my own logic for how arguments are combined into one
single state object. Of course, I wanted this. This was part of the
upside. But it's still code I didn't have to write for Clap.
* I had to write my own shell completion generator.
* I had to write my own `-h/--help` output generator.
* I also had to write my own man page generator. Well, I had to do this
with Clap 2.x too, although my understanding is that Clap 4.x supports
this. With that said, without having tried it, my guess is that I
probably wouldn't have liked the output it generated because I
ultimately had to write most of the roff by hand myself to get the man
page I wanted. (This also had the benefit of dropping the build
dependency on asciidoc/asciidoctor.)

While this is definitely a fair bit of extra work, it overall only cost
me a couple days. IMO, that's a good trade off given that this code is
unlikely to change again in any substantial way. And it should also
allow for more flexible semantics going forward.

Fixes #884, Fixes #1648, Fixes #1701, Fixes #1814, Fixes #1966

[1]: https://docs.rs/lexopt/0.3.0/lexopt/index.html

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[c9d2c940d8...](https://github.com/tgstation/tgstation/commit/c9d2c940d87f5205bdf882280af074b132e1af6c)
#### Friday 2023-12-01 21:53:14 by Vekter

Ports feral cats and feral cat grenades from Hippie (#80031)

## About The Pull Request
Feral Cats are just a hostile variant of cats that will fuck you up if
they see you. They are added solely for the sake of feral cat grenades -
a new, interesting, and fuzzy way to get out of a jam or just wreak
havoc around you. Each one costs 5 TC and spawns 5 really pissed off
cats to chase down assistants in the hallway.

They don't currently ignore traitors or the person who threw them - I
haven't worked out how to do that with our faction system (Hippie gave
them the syndicate faction but traitors don't get that on our codebase).
If anyone wants to contribute or help me suss that out it'll be cool,
otherwise just don't be around if there's nobody else for them to maul.

## Why It's Good For The Game
They're funny.

## Changelog
:cl: Vekter
add: Added a new hostile variant of cats, "feral cats".
add: Added a new traitor item, "feral cat grenades". For 5 TC, you too
can throw a grenade at someone and make five cats maul them to death.
/:cl:

---
## [littlefs-project/littlefs](https://github.com/littlefs-project/littlefs)@[db8f08cdbe...](https://github.com/littlefs-project/littlefs/commit/db8f08cdbe99a3a3e6779db585922e3d60c9970e)
#### Friday 2023-12-01 22:05:37 by Christopher Haster

WIP Adopted lazy orphaned mdir drops

This ended up being much less of a simplification than I hoped it would.

It's still easier/more efficient to revert to a relocation in most cases
when dropping in an mdir split, and the small gain from simplifying how
drops/commits interact is overshadowed by the code duplication necessary
to separate lfsr_mdir_drop out from lfsr_mdir_commit:

            code          stack
  before:  30952           2528
  after:   31280 (+1.1%)   2648 (+4.7%)

Still, this does at least simplify the logical corner cases (we don't
need to abort commits when droppable anymore), and lfsr_mdir_drop is
ultimately necessary for supporting lazy file creation.

Also having a fix-orphans step during mount allows other littlefs
implementations the option to create orphanned mdirs without compat
issues. So this ends up the more flexible approach.

It _might_ be worth having both eager mdir drops and an explicit
lfsr_mdir_drop for lazy file creation in the future, but I doubt this
will end up worth the code duplication...

---

Oh right, I forgot to actually describe this change.

This trades eager mdir drops:

1. Drop mdirs from the mtree immediately as soon as their weight goes
   to zero.

For lazy mdir drops:

1. Drop mdirs from the mtree in a second commit.
2. Scan and drop orphaned mdirs on the first write after mount.

This sounds very similar to the previous "deorphan" scan, which risked
an extreme performance cost during mount, but it should be noted this
orphan scan only needs to touch every mdir once. This makes it no worse
than the overhead of actually mounting the filesystem.

We can also keep an eye out for orphaned mdirs when we mount, so no
extra scan is needed unless there was an unlucky powerloss.

Eager mdir dropping sounds simpler, but thanks to deferred commits
introduces some subtle complexity around aborting commits that would
drop an mdir to zero. Remember commits are viewable on-disk as soon as a
commit completes.

In _theory_, lazy mdir drops simplify the logic around committing to
mdirs.

Though the real kicker is that lazy mdir drops are required for lazy file
creation.

The current idea for lazy file creation involves tracking mid-less
opened-but-not-yet-created files. These files can have bshrubs, so they
need space on an mdir somewhere. But they aren't actually created yet,
so they don't have an mid.

This is fine (though it's probably going to be tricky) as long as we
allocate an mid on file sync, but there is always a risk of losing power
with mdirs that contain only RAM-backed files. Fortunately, no-mids
means no orphaned files, but it does mean orphaned mdirs with no synced
contents.

Long story short, lazy mdir drops are currently a necessary evil, and
logical simplification, that unfortunately comes with some cost.

---
## [EasyApp-RPI/EasyApp](https://github.com/EasyApp-RPI/EasyApp)@[4521f74c7b...](https://github.com/EasyApp-RPI/EasyApp/commit/4521f74c7b7e9c2a932601c3cb03ca461fa5759d)
#### Friday 2023-12-01 22:10:55 by Anthony Fabius

Working Interests and SkillsComp

The amount of blood sweat and tears I put into this commit is not funny. Thought I was gonna have to switch majors if this shit didn't work ngl.

---
## [devnexen/miri](https://github.com/devnexen/miri)@[0b1e434b2b...](https://github.com/devnexen/miri/commit/0b1e434b2bac8e79909357df3f627c8a728cdbe4)
#### Friday 2023-12-01 22:28:21 by bors

Auto merge of #117611 - Nadrieril:linear-pass-take-4, r=cjgillot

Rewrite exhaustiveness in one pass

This is at least my 4th attempt at this in as many years x) Previous attempts were all too complicated or too slow. But we're finally here!

The previous version of the exhaustiveness algorithm computed reachability for each arm then exhaustiveness of the whole match. Since each of these steps does roughly the same things, this rewrites the algorithm to do them all in one go. I also think this makes things much simpler.

I also rewrote the documentation of the algorithm in depth. Hopefully it's up-to-date and easier to follow now. Plz comment if anything's unclear.

r? `@oli-obk` I think you're one of the rare other people to understand the exhaustiveness algorithm?

cc `@varkor` I know you're not active anymore, but if you feel like having a look you might enjoy this :D

Fixes https://github.com/rust-lang/rust/issues/79307

---
## [h-lame/advent-of-code](https://github.com/h-lame/advent-of-code)@[539794017a...](https://github.com/h-lame/advent-of-code/commit/539794017aa9b3192ccba875d5471fa38e6e1789)
#### Friday 2023-12-01 22:34:43 by Murray Steele

2023 - Day 1

Examples + solution.

Reusing the structure I tried in 2021 with a solution and normaliser.  It's a bit much, but here we are.

Part 1 pretty easy, but part 2 stumped me for too long given it's Day 1.  First pass I simply gsubbed: one,two, etc... and replaced with 1,2 but this didn't deal with overlapping numbers.  I spotted those in the examples (although not that it mattered in the example) and assumed I had to handle.  Used positive lookahead in my gsub, but I forgot about twone so got the wrong answer again.  I really thought I was missing something so after bashing my head for a bit I went to reddit.  Read a bunch of solutions in python, java, kotlin, etc... that all seemed to just do what I was doing but worked.  Then I found one in ruby and it seemed _exactly_ like mine.  Finally I went back to look and realised my mistake.

As ever, a great re-inforcement of "you should write more test cases" as once I'd identified the overlap I should have written some exhaustive test cases to prove out my implementation.  I didn't and went mad for a bit.

Grrr.

Added one now though.

---
## [crawl/crawl](https://github.com/crawl/crawl)@[dffb6e3712...](https://github.com/crawl/crawl/commit/dffb6e3712f7bc9ff45b6ae244928f1d806afe75)
#### Friday 2023-12-01 22:55:33 by regret-index

Brain Feed -> Brain Bite (minor damage + mp drain, no int drain)

Brain Feed is an extremely weird monster spell in most games. With so
little stat drain around by default in a three-rune game, individual hits
against a stat approach 0 extremely rarely unless a player has next to
none, which is influenced heavily by character start combo and very little
by normal character growth. The relatively minor hit of intelligence also
does very little for its use on higher Int characters aside from slightly
worsening spell success rates, which works weirdly against the flavour of
various brain-eating monsters not actually caring about the quality of
brain so much as just killing those with incidentally little of it.

It's kind of difficult to tell what this spell should do. It'd be entirely
possible to make it drain a lot more intelligence or percentage-based +
flat intelligence to make actually effect more characters, but while
strategic damage of a restorable sort would be more mechanical diversity,
screwing with spell success chances and non-tangible damage rolls aren't
mechanics we've kept to the present day (c.f. skilldrain, old sap magic).
So, I'm sidestepping the original effect of the spell entirely, while
focusing still on its theme.

Brain Feed is now revised into Brain Bite, a mildly-experimental mix of half
a Smite plus a percentile version of Draining Gaze- 4-8 irresistable direct
damage doubled if you have no mp, then draining 20% of one's max mp (rounded
down). (This now also works on monsters, dealing damage checking on antimagic
and then applying antimagic.) The percentage part lets it scale across the
game (compared to Draining Gaze rapidly heavily draining most player mp), and
irresistable but restrained damage sources are currently pretty reserved
designs (Smiting, Damnation, usually Torment) that could be iterated further
upon.

(It'd be good to think over what the point of statdrain even is outside
of Hell, Tomb, and klown pies. Possibly a variant of flaying but only
for stats would be interesting, possibly making an even shorter para but
with brief stat-zero would be an interesting revision of current para.
This is kind of out of this particular commit's scope, though- getting
to stat zero via Brain Feed didn't really happen for a very large number
of character combinations, so concerns over that are minimal.)

Tile update uses the old mimic teeth tile by coolio, modified by jpeg,
on top of the current Brain Feed icon by snw-0.

---
## [KathrinBailey/coyote-bayou](https://github.com/KathrinBailey/coyote-bayou)@[42161ed83b...](https://github.com/KathrinBailey/coyote-bayou/commit/42161ed83b86d78c15b6cd0cdab556b0afdfabbc)
#### Friday 2023-12-01 23:14:37 by Lynx

Mapping/Balance - Joint-Shop and Tribe Deathclaw

Made the shop near nash a little more interesting! It now has a more "Shoppy"-ish appearance? And has unqiue Strong Radroaches inside that I might use in other areas. They aren't too dangerous. Still die in one shot to [MOST] weapons, some weaker weapons might not be ideal for them. I tested combat against them early on with energy weapons. We'll see.

I changed the health and damage of the Deathclaw under the Sulphur Bottom camp as well; It deals significantly more varied ranges of damage 25-50 and is tankier over all. A big roll on luck when fighting the Deathclaw, which I think is a very interesting feel for actually sending people down there to fight it, and players who are very tanky will struggle killing it as it can occasionally nail some BIG damage on you.

I also increased the size of the Deathclaw arena, so that the deathclaw can actually BREAK shit like its intended to do when it reaches its enraged point! I really look forward to seeing fights in here become a lot more of a FIGHT rather than an endurance test. The rewards remain the same.

Literally changed one spot for the oven in a log cabin a little south east of Nash.

---
## [k21971/NetHack37](https://github.com/k21971/NetHack37)@[0473fff5b5...](https://github.com/k21971/NetHack37/commit/0473fff5b5908896ac12829afb523ad6d614af4f)
#### Friday 2023-12-01 23:54:55 by Michael Meyer

Make destruction of altar incite its god's wrath

This is for completely destroying an altar with extra-powerful magical
digging -- the normal altar_wrath() punishment didn't seem sufficient
for such an outrage to me, so skip straight to slinging the lightning
bolts.  Destroying an altar is unlikely to happen by accident (though
it's possible with poorly timed usage of a drum of earthquake).

---

