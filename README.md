## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2021-06-29](docs/good-messages/2021/2021-06-29.md)


3,149,732 events, 1,510,894 push events, 2,464,899 commit messages, 193,987,459 characters


## [hb432/storyteller@99324ba1f6...](https://github.com/hb432/storyteller/commit/99324ba1f6df222ef6fe3f12ef37058dfe3ff6a7)
##### 2021-06-29 04:18:43 by hb432

when the impostor is F I X E D
yeah i fixed that stupid default wav file issue lmao
(and a ton of stuff too)
- promises are no longer sussy
- made overworld associations map private because nobody aint got time for dat shit
- added "absolute" method on overworld and undertaleGame because we need to be able to get the in-game position of the bottom left corner of the rendered area for overlays and stuff
- made render code less sussy by moving zero calculation to outside for loop
- 'draw' event now fired on all rendered objects just before canvas application, could be used to inject stuff before draw
- a HUGE issue with XSheet fixed (it was alwayhs blanking the texture before)
- another HUGE issue with XRoom entity delete fixed, it was LITERALLY RECURSIVE ERROR 100% of the time!!! (so sus)
- metadata is defined sorta now? idk seems kinda garbo1234 if you ask me
- attributes instead of style for rectangle variable name becuase W H Y N O T lmao
- removed dumbo overworld layer in UndertaleGame it was rather sus
- dialogue push function in undertaleGame now works with no content (epic saucy?)
- oh yeah i guess i added a battler thing too idk its kinda cool i guess

---
## [CB-Mdk/CB-Mdk.github.io@98b2bbbb00...](https://github.com/CB-Mdk/CB-Mdk.github.io/commit/98b2bbbb00eb4dc64586633ca1fdc264a241c3b6)
##### 2021-06-29 04:40:25 by unknown

I FUCKING HATE YOU. IF THIS SHIT DOESNT APPEARS IN @gitlost I SWEAR I WILL  KMS

---
## [TotallyNotNero/terminal@1fc0997969...](https://github.com/TotallyNotNero/terminal/commit/1fc09979698a2ed5de674630171cd63c4599ef74)
##### 2021-06-29 07:10:22 by Mike Griese

Add a context menu entry to "Open Windows Terminal here" (#6100)

## Summary of the Pull Request

![image](https://user-images.githubusercontent.com/18356694/82586680-94447680-9b5d-11ea-9cf1-a85d2b32db10.png)

I went with the simple option - just open the Terminal with the default profile in the selected directory. I'd love to add another entry for "Open Terminal here with Profile...", but that's going to be follow-up work, once we sort out pulling the Terminal Settings into their own dll.

## References
* I'm going to need to file a bunch of follow-ups on this one.
  - We should add another entry to let the user select which profile
  - We should add the icon - I've got to do it in `dllname.dll,1` format, which is annoying.
  - These strings should be localized.
  - Should this only appear on <kbd>Shift</kbd>+right click? Probably! However, I don't know how to do that.
* [A Win7 Explorer Command Sample](https://github.com/microsoft/Windows-classic-samples/tree/master/Samples/Win7Samples/winui/shell/appshellintegration/ExplorerCommandVerb) which hasn't aged well
* [cppwinrt tutorial](https://docs.microsoft.com/en-us/windows/uwp/cpp-and-winrt-apis/author-coclasses) on using COM in cppwinrt
* [This is PowerToys' manifest](https://github.com/microsoft/PowerToys/blob/d2a60c7287eb5667b5282a519c92b759664c9e30/installer/MSIX/appxmanifest.xml#L53-L65) and then [their implementation](https://github.com/microsoft/PowerToys/blob/d16ebba9e0f06e7a0d41d981aeb1fd0a78192dc0/src/modules/powerrename/dll/PowerRenameExt.cpp) which were both helpful
* [This ](https://docs.microsoft.com/en-us/windows/apps/desktop/modernize/desktop-to-uwp-extensions#instructions) was the sample I followed for how to actually set up the manifest, with the added magic that [`desktop5` lets you specify "Directory"](https://docs.microsoft.com/en-us/uwp/schemas/appxpackage/uapmanifestschema/element-desktop5-itemtype)

## PR Checklist
* [x] Closes #1060
* [x] I work here
* [ ] Tests added/passed
* [n/a] Requires documentation to be updated

## Detailed Description of the Pull Request / Additional comments

This adds a COM class that implements `IExplorerCommand`, which is what lets us populate the context menu entry. We expose that type through a new DLL that is simply responsible for the shell extension, so that explorer doesn't need to load the entire Terminal just to populate that entry.

The COM class is tied to the application through some new entries in the manifest. The Clsid values are IMPORTANT - they must match the UUID of the implementation type. However, the `Verb` in the manifest didn't seem important.

---
## [naveenjohnsonv/kernel_xiaomi_sm8150@921be92355...](https://github.com/naveenjohnsonv/kernel_xiaomi_sm8150/commit/921be923551be5d7849bdc488617baacd39e2e4e)
##### 2021-06-29 11:25:45 by Maciej Żenczykowski

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
## [bhalevy/scylla@7014da9404...](https://github.com/bhalevy/scylla/commit/7014da9404abf6fafc03c051b27569500f9f1b30)
##### 2021-06-29 15:19:51 by Pavel Emelyanov

storage_service: Unregister disk error handlers on stop

Storage service install disk error handlers in constructor and these
connections are not unregistered. It's not a problem in real life,
because storage service is not stopped, but in some tests this can
lead to use-after-frees.

The sstables_datafile_test runs some of the testcases in cql_test_env
which starts and (!) stops the storage service. Other testcases are
run in a lightweight sstables_test_env which does not mess with the
storage service at all. Now, if a case of the 2nd kind is run after
the one of the 1st and (for whatever reason) generates a disk error
it will trigger use-after-free -- after the 1st testcase the storage
service disk error registration would remain, but the storage service
itself would already be stopped, thus triggering the disk error will
try to access stopped sharded storage service inside the .isolate().

The fix is to keep the scoped connection on the storage service list
of various listeners. On stop it will go away automagically.

tests: unit(dev), sstables_datafile_test with forced disk error

Signed-off-by: Pavel Emelyanov <xemul@scylladb.com>
Message-Id: <20210625062648.27812-1-xemul@scylladb.com>

---
## [jak6jak/bevy@c893b99224...](https://github.com/jak6jak/bevy/commit/c893b992240fc058fd118c8247c70233931ec759)
##### 2021-06-29 15:55:23 by Daniel McNab

Optional `.system` (#2398)

This can be your 6 months post-christmas present.

# Objective

- Make `.system` optional
- yeet
- It's ugly
- Alternative title: `.system` is dead; long live `.system`
- **yeet**

## Solution

- Use a higher ranked lifetime, and some trait magic.

N.B. This PR does not actually remove any `.system`s, except in a couple of examples. Once this is merged we can do that piecemeal across crates, and decide on syntax for labels.

---
## [pytorch/pytorch@9134b0e42f...](https://github.com/pytorch/pytorch/commit/9134b0e42fd6aad420d610f3786f90786079d559)
##### 2021-06-29 16:36:50 by Brian Hirsh

add a boxed CPU fallback kernel (#58065)

Summary:
Pull Request resolved: https://github.com/pytorch/pytorch/pull/58065

This PR replaces the existing code-generated CPU fallback kernels that XLA uses with a single boxed CPU fallback.

Current state: there are a couple different design ideas that I want to point out, but the logic for the actually kernel is mostly done and passing tests.

### Design

To preface, I'm not 100% tied to the current design and I'm putting the PR up now for opinions and totally open to alternatives, some of which I listed below. Actually after writing this description, I'm leaning toward the following changes:
* Confirm whether or not we can remove all C++ logging info directly in the yaml.

**Current Design**

All of the CPU fallback codegen is deleted. In its place, XLA (and other external backends, later) can choose to opt into a CPU fallback by adding the following code in a C++ file. I have an corresponding [xla-side PR with the xla changes](https://github.com/pytorch/xla/pull/2945/files#diff-1a005c10039f0cb11130a3b740f5de716d2f10acaea121017016025861886798R1).

There's no actual requirement to split up the code into a .h and .cpp file, but that's necessary in the XLA case because they sometimes need to call the fallback directly from their handcrafted kernels.

```
// xla_cpu_fallback.h
#include <ATen/native/CPUFallback.h>
...
void xla_cpu_fallback(const c10::OperatorHandle& op, torch::jit::Stack* stack);
...
```
```
// xla_cpu_fallback.cpp
#include "torch_xla/csrc/aten_cpu_fallback.h"
...
void xla_cpu_fallback(const c10::OperatorHandle& op, torch::jit::Stack* stack) {
  // Do custom logging here
  ...
  // Call the actual boxed CPU fallback.
  at::native::cpu_fallback(op, stack);
}

TORCH_LIBRARY_IMPL(_, XLA, m) {
  m.fallback(torch::CppFunction::makeFromBoxedFunction<&xla_cpu_fallback>());
}
```

Now that the fallback is exposed in the backend, they can call it directly. Doing so requires converting from an unboxed to a boxed context, which we provide a utility function before. E.g.:
```
#include <ATen/native/CPUFallback.h>

at::Tensor addmm(const at::Tensor& self,const at::Tensor& mat1,const at::Tensor& mat2,const at::Scalar& beta,const at::Scalar& alpha) {
  ....
  if (...call_fallback...) {
    return at::native::call_fallback_fn<&xla_cpu_fallback, decltype(at::addmm)>::call("aten::addmm", self, mat1, mat2, beta, alpha);
  }
  ...
}
```

That `decltype(at::addmm)` logic isn't actually used everywhere in the xla-side PR yet, since you hit issues with overloads. I could use it everywhere once #58092 lands.

**Alternatives: The API for calling the CPU fallback directly is ugly, can we make it nicer?**
We could change the api to use `at::redispatch`, which would make it look something like this:
```
at::Tensor addmm(const at::Tensor& self,const at::Tensor& mat1,const at::Tensor& mat2,const at::Scalar& beta,const at::Scalar& alpha) {
  ....
  if (...call_fallback...) {
    return at::redispatch::addmm(c10::DispatchKeySet(c10::DispatchKey::CPUFallback), self, mat1, mat2, beta, alpha);
  }
  ...
}
```
Which definitely feels cleaner, but also requires adding a new DispatchKey just for this use case. Conditionally calling the CPU fallback doesn't sound like a hugely important use case, so I don't know if giving up one of our 64 dispatch key slots is worth the API improvement. Totally open to other opinions though!

Another more mild improvement that would avoid having to pass operator string names (including overloads) around would be to codegen (yet another) namespaced API. Something like this:
```
at::Tensor addmm(const at::Tensor& self,const at::Tensor& mat1,const at::Tensor& mat2,const at::Scalar& beta,const at::Scalar& alpha) {
  ....
  if (...call_fallback...) {
    return at::fallback::addmm<&xla_cpu_fallback>(self, mat1, mat2, beta, alpha);
  }
  ...
}
```

Writing that out actually I actually like it more (I think it'll let us get rid of `decltype(...)`). Maybe that is nice enough to warrant a new codegen API - I haven't tried adding that yet, but if people like it I'm happy to try it out.

**More alternatives**
The current design also involves the backend manually writing and registering the boxed fallback themselves, but an alternative would be for us to do it in codegen too: they would just need to pass in all of the C++ logging that they want done in the fallback, directly through the yaml. The main downsides:
* Backend code that wants to call the fallback needs to abide by whatever convention our codegen uses to name the generated boxed fallback.
* Passing custom C++ logging through yaml is just more fragile: right now xla uses an `iostream` to log each tensor arg in the operator, so we'd have to either force other backends into the same convention or figure something else out later.

To be fair, we actually already do that: XLA has custom per-tensor-arg logging for all of the generated `out` wrappers in the codegen, which we do by passing their C++ logging info through the yaml. This seems unnecessary though, since `out` wrappers just call into a functional kernel, which is hand written with its own custom logging. So my take is: try to remove custom C++ logging from the yaml, and if it turns out to be really necessary, then we may as well take advantage of that to codegen the fallback.

### Performance impact

While ops that fall back to CPU aren't exactly hot path, we probably don't want to use a boxed fallback if it turns out to be an absolute perf killer.

I ran my benchmarks using callgrind, benchmarking both `at::add` and `at::add_out` run on XLA. My callgrind benchmark for `at::add` can be found here (the add_out benchmark looks basically the same): https://www.internalfb.com/phabricator/paste/view/P415418587. I created the benchmark by hacking the existing xla C++ test build scripts and throwing in a reference to callgrind.

I also attached the full callgrind output for each benchmark; the full output is actually pretty noise and hard to parse, but I focused on everything underneath the `at::add()` call in the output, which was much more stable. My guess is that it's due to some heavyweight async startup processing that xla does.

`at::add`:
before: 88,505,130 instructions. Full output: https://www.internalfb.com/phabricator/paste/view/P415421001
after: 102,185,654 instructions. Full output: https://www.internalfb.com/phabricator/paste/view/P415421273
delta: ~15.5% increase

`at::add_out`:
before: 63,897,395 instructions. Full output: https://www.internalfb.com/intern/everpaste/?handle=GBrrKwtAPlix9wUEAOZtrFXpdO5UbsIXAAAz
after: 73,170,346 instructions. Full output: https://www.internalfb.com/phabricator/paste/view/P415423227
delta: ~14.5% increase

High level takeaway: A framework overhead increase of 10-20% doesn't seem too horrible for the CPU fallback use case.

For structured, functional ops that requires a CPU fallback, we're actually in an unfortunate situation: we're doing even more work than necessary. Our codegen automatically creates a `CompositeExplicitAutograd` kernel which calls into the `out` operator. So the extra work that we end up doing is:
* An extra dispatcher hop: (at::add -> CompositeExplicitAutograd -> CPUFallback -> at::native::add) instead of (at::add -> CPUFallback -> at::native::add)
* An unnecessary tensor allocation (the CompositeExplicitAutograd kernel uses at::empty() to create an output tensor, which is immediately overwritten by the CPU fallback)
* An unnecessary meta() call (the CompositeExplicitAutograd kernel calls it to create the output tensor, but we call it again in the CPU kernel).
* unboxing->boxing->unboxing logic (this is the only strictly required piece)

There are definitely ways to avoid the unnecessary work explained above: one would be to give the boxed fallback higher priority than composite keys (there's [an issue for it here](https://github.com/pytorch/pytorch/issues/55104)), and codegen fallthroughs for all composite ops. It'll require more infra to set up, so I see it as more of a perf knob that we can apply if we need it later.

Unfortunately I couldn't dig much deeper into the differences aside from the aggregate change in instructions, since it looks like callgrind fudged some of the instruction attribution (`at::to_cpu` takes up a ton of instructions, but I don't see any attribution for the `at::native::add` kernel anywhere).

Test Plan: Imported from OSS

Reviewed By: jbschlosser

Differential Revision: D28833085

Pulled By: bdhirsh

fbshipit-source-id: 537ebd5d7fb5858f1158764ff47132d503c3b92b

---
## [aaaa1023/fulpstation@f4a04ca124...](https://github.com/aaaa1023/fulpstation/commit/f4a04ca1248ebd02b7f682f57a8770436097116e)
##### 2021-06-29 16:57:31 by SgtHunk

Updates Selenestation with directionals (#172)

* a lot of directional

commiting before i experiment more

* stuff before i continue

* SHOULD BE ALL???

* i dont want to play with you anymore

updatepaths my beloved locket gif

* yo mama

gets rid of strays and fixes a few fucked-up displays

Co-authored-by: Enricode <SgtHunk@users.noreply.github.com>

---
## [bingis-khan/BobiAutomata@20b520bfec...](https://github.com/bingis-khan/BobiAutomata/commit/20b520bfecb0155d67c0731ae1045edef113b7b9)
##### 2021-06-29 18:22:38 by bingis-khan

I'm kinda bored.

A lot of things - big and small. I didn't make commits, because I was
experimenting with a lot of stuff.
1. I finished the "user" part of the application - it's possible to
actually run it now like a normal human being. Wow.
2. I understand Gradle better (like 1% overall, compared to 0.01%
before) - got the build file cleaned up a bit.
3. Oh, right. New task 'executable' to compile the whole thing to a
sorta independent executable. The task adds a custom, jlinked JRE,
launch4j's .exe and sample automata to a single folder.* Kinda cool.
4. Added sample automatas.

----------------------------------------------------------------------

On that note, I'm kinda bored of this project.

What's left:
1. More flexible / less repetetive functions might never be implemented
(for example, right now, the 'is' is part of the 'sum' function and
every function returns boolean. Functions also can't overlap - something
like 'north is [state]' and 'north west is [state]' is not possible - a
task perfect for some kind of a FSM).
2. Speed up the simulation. This project might actually be interesting
to try and implement 'hashlife' in.
For evaluating expressions, maybe something like a bytecode VM? That
last one is probably overkill, it would be better after porting to C/C++
or even Rust (as a learning exercise)?
3. Improve the language. When trying to write a simple fluid simulation,
I had to repeat a lot of cases (ex. 5 lines with 'FULL:' for example).
So, a general 'switch-case' structure? A lot of writing, basically. It's
interesting, because the language might be the greatest barrier in
creating some interesting cellular automata.

(3) is similar to (1) in a way, that we can increase the expressiveness
of this language by better implementing function definitions.
Instead of 4 times 'north is GOES_DOWN and random 1 in n chance ->
[state]'
Adding better functions can change it to: 'north is GOES_DOWN -> choose
GOES_UP, GOES_DOWN, GOES_LEFT, GOES_RIGHT', where 'choose' is of type
State.


What's left, but might actually be implemented, because I'm not as tired
of this project as I thought:
1. Toroidal-ness.
2. Setting (maximum) simulation speed. It ain't that fast and I don't
know no 'hashlife'. Git outta here!
3. Remove requirement for specyfing neighborhood type (like, it's not
needed if the CA is not using it - random walk for example).
4. Change the order of color definitions - originally there, because of
code reuse (laziness) and that it kinda makes sense that states are
differentiated by color first (what you see), then the state it belongs
to (what it actually is). It breaks down on something like Langton's
Ant, where multiple states are red. So, yeah, one-to-many: [state] is
[color].
5. Custom color, represented by a leading '#', then 6 hex digits. Should
be added after implementing (4), because it'll look bad otherwise (ex.
'#00FF00 is ON' vs 'ON is #00FF00').
6. Parameters (and a system to handle them) to configure all these.
7. Images instead of colors. The framework is there (State uses
BufferedImage by default), but we might have to decouple creating states
from parsing? (Suppose we specify the default image folder in 'Defualts'
and reference images only by filename. We can do it while parsing, but
it'll lead to some 'half-parameters' which are only valid inside the
Parser object and would need to be removed after.)
8. And, as always, finish pretty printing for error reporting. (^^^^^ to
underline errors).

-----------------------------------------------------------------------

*I experimented with two ways to bundle an executable.
1. Official - Making an installer. Why I didn't go for it? I don't feel
like this manlet of an application should require a whole installation
process.

2. Hacky - Something called 'sfx' (self-extracting archive). I actually
ended up making it work (manually), but, because it seems to be an
untrustoworthy format
(https://en.wikipedia.org/wiki/Self-extracting_archive#Disadvantages ),
Windows always shows its password prompt, which is really annoying. So,
I scrapped it, but the idea for both a JRE and a program bundled into a
single executable (without it being obvious it uses a virtual machine)
is interesting.
Also, the fact that the jlink Gradle plugin also supports jpackage and
creating the whole "image" structure, which I used for sfx, is a welcome
surprise. (I'm not sure if this 'image structure' is the jpackage's or
the plugin's doing.)

---
## [LeandroBoog/gameification@c5203a36e7...](https://github.com/LeandroBoog/gameification/commit/c5203a36e795b6829eb80f256f4643d45efa4d4c)
##### 2021-06-29 19:49:29 by Leandro Boog

Oh my fucking god, teamstats now finally has own table like jesus christ why is sql so annoying, why was this so hard

---
## [SwanX1/Swans-CI@afec415a80...](https://github.com/SwanX1/Swans-CI/commit/afec415a80ff16b9340791083baa94d0fb763b59)
##### 2021-06-29 23:08:44 by SwanX1

Rawr x3 *nuzzles* how are you *pounces on you* you're so warm o3o *notices you have a bulge* o: someone's happy ;) *nuzzles your necky wecky~* murr~ hehehe *rubbies your bulgy wolgy* you're so big :oooo *rubbies more on your bulgy wolgy* it doesn't stop growing ·///· *kisses you and lickies your necky* daddy likies (; *nuzzles wuzzles* I hope daddy really likes $: *wiggles butt and squirms* I want to see your big daddy meat~ *wiggles butt* I have a little itch o3o *wags tail* can you please get my itch~ *puts paws on your chest* nyea~ its a seven inch itch *rubs your chest* can you help me pwease *squirms* pwetty pwease *sad face* I need to be punished *runs paws down your chest and bites lip* like I need to be punished really good~ *paws on your bulge as I lick my lips* I'm getting thirsty. I can go for some milk *unbuttons your pants as my eyes glow* you smell so musky :v *licks shaft* mmmm~ so musky *drools all over your cock* your daddy meat I like *fondles* Mr. Fuzzy Balls hehe *puts snout on balls and inhales deeply* oh god im so hard~ *licks balls* punish me daddy~ nyea~ *squirms more and wiggles butt* I love your musky goodness *bites lip* please punish me *licks lips* nyea~ *suckles on your tip* so good *licks pre of your cock* salty goodness~ *eyes role back and goes balls deep* mmmm~ *moans and suckles* o3o

---

