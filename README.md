## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-10-06](docs/good-messages/2022/2022-10-06.md)


1,959,603 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,959,603 were push events containing 2,911,770 commit messages that amount to 222,486,769 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 27 messages:


## [clayne/oiio](https://github.com/clayne/oiio)@[4ee35351f1...](https://github.com/clayne/oiio/commit/4ee35351f100c79738c77892fb8ccca8ddc004c9)
#### Thursday 2022-10-06 00:48:43 by Aras Pranckevičius

DDS: alpha/luminance format fixes, add & enable more tests (#3581)

* DDS: fixes for A8, L8, A8L8 formats

While developing #3573 at one time I had them working properly, but then
while fixing the address sanitizer failure for 3-channel formats I
botched them again. Note to self: never again do a "yeah I'll add tests
later", since if I had all of them running all the time this would
not have happened. :facepalm:

* DDS: extend test coverage for more formats & channel size cases

With more test images recently added (https://github.com/OpenImageIO/oiio/pull/3459),
start using them for DDS tests. This covers now:
- Alpha, Luminance and Alpha+Luminance formats,
- RGB formats with rarer channel sizes (rgb10 a2, r3g3b2),
- Several "broken" DDS file cases
- Removed usage of sample-DXT1 since it is well covered by others.

---
## [Zergspower/Skyrat-tg](https://github.com/Zergspower/Skyrat-tg)@[74586e2091...](https://github.com/Zergspower/Skyrat-tg/commit/74586e2091b0793b4eca713eff890a76afbd3c89)
#### Thursday 2022-10-06 00:57:06 by SkyratBot

[MIRROR] Upgrades the Modsuit Adapter Shell [MDB IGNORE] (#16669)

* Upgrades the Modsuit Adapter Shell (#70286)

Code improvements are much appreciated as some things may be rather hacky.

Adds more options to the currently very limited modsuit adapter shell. Right now you can only select a module and activate (not deploy) the suit.

This has some major problems as you literally can't even deploy the suit to activate it so that's rendered useless and selecting a module is like... kind of a weird input anyways but I won't judge so I left it in. Please comment down below if you'd like for me to add an "Activate Selected Module" input and "On Module Activated" output as those are certainly possible to do. I was just a little torn on how balanced that would be.

Changes:

"Module to Select" input is now an option. You can still use a string input, but simply inserting it into the suit and activating it, then accessing the circuit that way will give you a list of all modules that the modsuit has.
Modsuit quick deploy (RMB) no longer tries to deploy the rest of the pieces when used while the suit is only partially deployed. It will now instead retract the extended pieces. This makes the "Toggle Deployment" input less prone to errors. (Why was it like this in the first place? Having to manually retract the already extended pieces sucks ass.)
Added Inputs:

"Toggle Deployment" is a new signal input that does exactly what it says it does. It simply tries to extend or retract all pieces of the modsuit depending on it's current state.
Added Outputs:

"Activated" is a new number output that outputs 1 if the suit is activated and 0 if it's not.
"Deployed" is a new number output that outputs 1 if all parts of the suit are extended and 0 if they aren't.
"Deployed Parts" is a new string list output that outputs a list of the names of all currently deployed parts.
"On Deploy" is a new signal output that outputs a signal whenever all parts of the suit are deployed or retracted, regardless of the method used.
"Finished Toggling" is a new signal output that outputs a signal whenever the suit has finished activating or deactivating, regardless of the method used.

* Upgrades the Modsuit Adapter Shell

Co-authored-by: RikuTheKiller <88713943+RikuTheKiller@users.noreply.github.com>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[422accbe4e...](https://github.com/tgstation/tgstation/commit/422accbe4e9b53f075f9a76ba6293435cb3399da)
#### Thursday 2022-10-06 01:51:40 by John Willard

[MDB IGNORE] Shuttle engines part 2: Engines are now machines (#69793)

* Makes engines machines instead of structures

* Updates the maps

* Fixes boards and anchoring

* Removes 2 unused engine types

Router was actually used a total of once, so I just replaced it with propulsion.
I think cutting down on these useless engine types that make no difference in-game would be a nice first step to adding more functionalities to them.

* Don't use power (since shuttles dont have)

Shuttles don't have APCs, instead they just have infinite power, so I'm removing their power usage for now. I'm hoping this can be removed when unique mechanics are added to engines, because I would like them to make use of power like other machines.

* re-organizes vars

* deletes deleted dm file

* Slightly improves cargo selling code

* Renames the updatepaths

* Removes in_wall engines

I hate this stupid engine it sucks it's useless it's used solely for the tram it provides nothing of benefit to the server
replaces them with regular engines

---
## [ChoGGi/SurvivingMars_CheatMods](https://github.com/ChoGGi/SurvivingMars_CheatMods)@[c098c39bad...](https://github.com/ChoGGi/SurvivingMars_CheatMods/commit/c098c39badff13b8a55b670314438cd1dc8ef6a0)
#### Thursday 2022-10-06 02:00:55 by ChoGGi

Mods:

Fix Bugs 3.3
Some buildings don't properly turn off their upgrades which causes them to keep their modifiers on (thanks Lord_Sicarious).
The "fix" is turning off upgrades when a building is demolished, turned off, malfunctioned (might be annoying, mod option to keep it as is).

Game Rule Amazonian Mars 0.6:
Culls male colonists recruited from rivals before landing.

Game Rules Threats Resources 0.5:
Picard.

Larger Depots:
This won't change existing depots, see mod options to change amounts (on new depots only).
There is a height limit on map objects, so I'm sticking with a limit on the storage size (I wouldn't fill the uni depot up on higher plateaus).

RC Transport Cheats 0.9:
Added Storage Amount to building template.

github@choggi.org

---
## [BlueManedHawk/bluemanedhawk.github.io](https://github.com/BlueManedHawk/bluemanedhawk.github.io)@[f8513d1a77...](https://github.com/BlueManedHawk/bluemanedhawk.github.io/commit/f8513d1a77c4f55e01c822d89f7689518f657b49)
#### Thursday 2022-10-06 02:08:20 by Blue-Maned_Hawk

Change of color scheme

It was pointed out to me that the old one is a little hard to read due
to the contrast (thanks to citrons for pointing this out to me), so
i've changed it to this one.  This is significantly more blue and the
 text is now bright instead of dark, and now it kinda looks like an
old-school TUI, which is kinda fun.

I have been thinking of using an actually professional color scheme
instead of just web colors.  I was thinking of Solarized, but i have
several problems with it, and honestly i'm thinking of just making my
own color scheme.  If i do, i'll probably change my page to use it.

---
## [Zergspower/Skyrat-tg](https://github.com/Zergspower/Skyrat-tg)@[1eab5a8364...](https://github.com/Zergspower/Skyrat-tg/commit/1eab5a8364114dce9f63c97852461b6e4f27d7b0)
#### Thursday 2022-10-06 03:13:53 by SkyratBot

[MIRROR] Heretics cannot be converted, and are immune to cult stun hands. Instead, the cult is rewarded for sacrificing them with the bloody bastard sword, an oversized SPIN2WIN funblade. + Soul Stealing Fantasy Affix [MDB IGNORE] (#16486)

* Heretics cannot be converted, and are immune to cult stun hands. Instead, the cult is rewarded for sacrificing them with the bloody bastard sword, an oversized SPIN2WIN funblade. + Soul Stealing Fantasy Affix (#69725)

About The Pull Request

Heretics can no longer be converted to a cult, as they follow their own Forgotten Gods.
Instead, Nar'Sie will reward the cult for managing to sacrifice one, with the bastard sword.
The bloody bastard sword has been cleaned up codewise and all that. Because it is a free reward instead of a (removed) progression mechanic of cult, it swings just a bit slower during the spin and doesn't have a jaunt. It's still a !fun! swinging sword of hilarity and death.
BLOODY BASTARD https://www.youtube.com/watch?v=ukznXQ3MgN0
Fantasy weapons can now roll "soul-stealing" weapons. They, on killing something, capture its soul inside the item.

    Add fail conditions that instantly end a spin2win, ala how

    Mimes can now hold a baguette like a sword by right clicking it #69592 works

Why It's Good For The Game

Bloody bastard sword was fun, it made no sense that heretics were valid converts when they're already worshipping a DIFFERENT evil god granting them powers. Should be in a good spot as a nice little antag to antag special interaction. I fucking love antag to antag special interactions, we should have more of 'em

Fantasy affixes are always a neat thing to throw a new component into
Changelog

cl
add: Heretics can no longer be converted to cult. But sacrificing them is very valuable to Nar'Sie, and she will grant special weapons if you manage to do so.
add: Fantasy affixes can also include soul-stealing items!
/cl

* Heretics cannot be converted, and are immune to cult stun hands. Instead, the cult is rewarded for sacrificing them with the bloody bastard sword, an oversized SPIN2WIN funblade. + Soul Stealing Fantasy Affix

Co-authored-by: tralezab <40974010+tralezab@users.noreply.github.com>
Co-authored-by: Tastyfish <crazychris32@gmail.com>

---
## [Spectrum-Kernel/kernel_xiaomi_sm6250](https://github.com/Spectrum-Kernel/kernel_xiaomi_sm6250)@[09396f73cd...](https://github.com/Spectrum-Kernel/kernel_xiaomi_sm6250/commit/09396f73cda1922dd527004e3fb8ae0d2400b52c)
#### Thursday 2022-10-06 03:21:17 by Maciej Żenczykowski

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
## [containers/buildah](https://github.com/containers/buildah)@[2adbe2a58a...](https://github.com/containers/buildah/commit/2adbe2a58a77b014be59c68abf58b682ad5e5c20)
#### Thursday 2022-10-06 03:42:47 by Ed Santiago

System test cleanup: document, clarify, fix

Primary purpose: fix "preconfigured TARGETARCH/etc" test so
it will work under podman and on multiarch.

Root cause of it not working: I mistakenly advised @flouthoc,
in #4310, to write a containerfile in $TEST_SCRATCH_DIR. I
thought it was an empty directory. Big, big mistake. (Sorry,
Aditya). Document this near the variable definition, and
fix the test once again.

@nalind pointed out that the containerfile doesn't need to
be generated on-the-fly, so, use a static one. In the spirit
of DIE, read the TARGETxxx vars from it. Not that we're
expecting more variables, but, it's just cleaner.

Also, as long as I'm here: in run_buildah, when logging the
command being run, use #/$ prompt for root/rootless. I was
getting too confused looking at logs of root runs.

Signed-off-by: Ed Santiago <santiago@redhat.com>

---
## [danielzfranklin/bpack](https://github.com/danielzfranklin/bpack)@[8153ef3e89...](https://github.com/danielzfranklin/bpack/commit/8153ef3e89bbda92d22b99c59adc31bbcf9677e9)
#### Thursday 2022-10-06 04:25:06 by Daniel Franklin

[mk] Upgrade mapnik to upstream master HEAD

Why master HEAD? Based on a recent substantive PR (4333) by someone very
experienced with mapnik I'm making an informed guess they develop on
master.

Why use my fork, which has no changes? I want to make it easy to make
hacky patches to mapnik without needing to go through the finicky
process of changing submodule upstreams.

Changes:

- Change HEAD of [mapnik-sys/deps/mapnik]
- Change [mapnik-sys/dep_notes.md]:
    - Add instructions for disabling rust-analyzer (& empty vscode prefs
      to simplify)
    - Add step to run mapnik's test suite. NOTE: This is just a reminder
      to think about it. Actually getting it to compile is a future
      project.
    - Disable warnings compiling mapnik: We can't fix them, they make it
      harder to debug errors
    - Scons now supports python3
    - Add step to disable all build flags except a small allowlist
- Update assertion test to new xml
- Add include for new mapnik dep to [build.rs]

Closes #2

---
## [MITK/MITK](https://github.com/MITK/MITK)@[5647a86452...](https://github.com/MITK/MITK/commit/5647a864520b88bd90b843f69008ae4ec5a89f89)
#### Thursday 2022-10-06 04:47:32 by Stefan Dinkelacker

2022 Week 40 (Very Early October)

The following - possibly updated - changelog can be viewed as formatted
article at https://phabricator.mitk.org/w/mitk/changelog/2022.40/.

= 🛠 Third-party dependency changes =

| Dependency | Old version | New version |
| --- | --- | --- |
| GDCM | 3.0.9 (via ITK) | 3.0.14 (standalone) |

= ✨ New features =

- Segmentation tools
  - New Close tool for filling all holes of a connected label region
  - New GrowCut tool for automagically refining coarse and sparse segmentations
  - Improved intuitive behavior of Fill and Erase tools
  - Improved performance of Paint and Wipe tools
  - Icons and cursors are resolution-independent vector graphics now instead of pre-converted pixel graphics
- First experimental release of the mxn multi widget, a more sophisticated and flexible alternative to the standard multi widget
- Linux installers now work also on Linux distros without TCP Wrappers support (e.g. Fedora)

= 🐛 Bugfixes =

- Removed pixel value information from status bar, which was rather incoherent or unreliable in some cases (will be reimplemented in {T29324})
- Fixed an update issue of image position and slice number in the status bar when scrolling
- Fixed handling of invisible reference images in Segmentation View
- Fixed crashes on Windows of some MITK binaries related to static linking of GDCM

= 🔥 API-breaking changes =

In an ongoing cleanup effort, many deprecated or unused classes, methods, and other code snippets were removed or refactored. Migration should be straight forward if necessary at all.

In case you experience any trouble while doing so, please do not hesitate to [[https://www.mitk.org/wiki/MITK_Mailinglist | contact us]].

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[a0cb2cf6a2...](https://github.com/treckstar/yolo-octo-hipster/commit/a0cb2cf6a2acfe82f98e5709d2de7128c3aebf7d)
#### Thursday 2022-10-06 05:22:02 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [tikimcfee/LookAtThat](https://github.com/tikimcfee/LookAtThat)@[dc3de55a7e...](https://github.com/tikimcfee/LookAtThat/commit/dc3de55a7e8002d1af7f8a98e31d22f738663884)
#### Thursday 2022-10-06 05:48:51 by Ivan Lugo

- NOTE: Fixed BackingBuffer by throwing a lock around the incrementer. Oops
-- Classic thread racing to grab new indices ended up with nodes sharing parents
- Change cached matrix to an observable thing
-- Goal is to make it easier for observation attachment to arbitrary nodes
-- setDirty() is a bit ugly
-- TODO: Batching updates is a thing to implement later (lol SCNTransaction...)
- Add some test layouts to RenderPlan to.. test some layouts
-- Force directed does.. stuff? Doesn't quite work. I followed an algorithm but either didnt understand it or implement it correctly. Or maybe just using it wrong. Who knows.
-- Added another simple stack-and-translate based on directories. (lol FocusBox...)
--- Learning some lessons on deleting lots of code.
--- It shouldn't be impossible to bring it back if parenting is updated to actually work (lol matrices...)
- Updated distanceTo() in FileBrowser to do component matches and counts. Again. To be safer. Maybe. Again.
-- The implicit /.. thing is nasty
- Oh yeah there's ForceLayout but hell if I know how to fix it
- Added some directory tests for experiments
-

---
## [U1traStar/free-programming-books](https://github.com/U1traStar/free-programming-books)@[5fd70502a0...](https://github.com/U1traStar/free-programming-books/commit/5fd70502a063c46914fd444d2511c8233f81777f)
#### Thursday 2022-10-06 06:59:04 by Mathieu FONTAINE

Update free-programming-cheatsheets.md - React (#7095)

I suggested a React cheat sheet that I use very often. It is one of the most exhaustive and qualitative in my opinion.

---
## [rust-lang/rust-clippy](https://github.com/rust-lang/rust-clippy)@[9e8f53d09a...](https://github.com/rust-lang/rust-clippy/commit/9e8f53d09af61d38d6de42450dbf6910982d3ea9)
#### Thursday 2022-10-06 07:23:10 by bors

Auto merge of #101986 - WaffleLapkin:move_lint_note_to_the_bottom, r=estebank

Move lint level source explanation to the bottom

So, uhhhhh

r? `@estebank`

## User-facing change

"note: `#[warn(...)]` on by default" and such are moved to the bottom of the diagnostic:
```diff
-   = note: `#[warn(unsupported_calling_conventions)]` on by default
   = warning: this was previously accepted by the compiler but is being phased out; it will become a hard error in a future release!
   = note: for more information, see issue #87678 <https://github.com/rust-lang/rust/issues/87678>
+   = note: `#[warn(unsupported_calling_conventions)]` on by default
```

Why warning is enabled is the least important thing, so it shouldn't be the first note the user reads, IMO.

## Developer-facing change

`struct_span_lint` and similar methods have a different signature.

Before: `..., impl for<'a> FnOnce(LintDiagnosticBuilder<'a, ()>)`
After: `..., impl Into<DiagnosticMessage>, impl for<'a, 'b> FnOnce(&'b mut DiagnosticBuilder<'a, ()>) -> &'b mut DiagnosticBuilder<'a, ()>`

The reason for this is that `struct_span_lint` needs to edit the diagnostic _after_ `decorate` closure is called. This also makes lint code a little bit nicer in my opinion.

Another option is to use `impl for<'a> FnOnce(LintDiagnosticBuilder<'a, ()>) -> DiagnosticBuilder<'a, ()>` altough I don't _really_ see reasons to do `let lint = lint.build(message)` everywhere.

## Subtle problem

By moving the message outside of the closure (that may not be called if the lint is disabled) `format!(...)` is executed earlier, possibly formatting `Ty` which may call a query that trims paths that crashes the compiler if there were no warnings...

I don't think it's that big of a deal, considering that we move from `format!(...)` to `fluent` (which is lazy by-default) anyway, however this required adding a workaround which is unfortunate.

## P.S.

I'm sorry, I do not how to make this PR smaller/easier to review. Changes to the lint API affect SO MUCH 😢

---
## [tvlooy/symfony](https://github.com/tvlooy/symfony)@[338daf25c9...](https://github.com/tvlooy/symfony/commit/338daf25c9589e2b93b4d7d693b4a49f7da677db)
#### Thursday 2022-10-06 07:55:27 by Nicolas Grekas

feature #46751 [VarExporter] Add trait to help implement lazy loading ghost objects (nicolas-grekas)

This PR was merged into the 6.2 branch.

Discussion
----------

[VarExporter] Add trait to help implement lazy loading ghost objects

| Q             | A
| ------------- | ---
| Branch?       | 6.2
| Bug fix?      | no
| New feature?  | yes
| Deprecations? | no
| Tickets       | -
| License       | MIT
| Doc PR        | -

This PR packages an implementation of [lazy loading ghost objects](https://www.martinfowler.com/eaaCatalog/lazyLoad.html) in a single `LazyGhostObjectTrait` (as a reminder, a lazy ghost object is an object that is created empty and that is able to initialize itself when being accessed for the first time.)

By using this trait, ppl can easily turn any existing classes into such ghost object implementations.

I target two use cases with this feature (but ppl are free to be more creative):
1. lazy proxy generation for service containers;
2. lazy proxy generation for entities.

In all cases, the generation itself is trivial using inheritance (sorry `final` classes.) For example, in order to turn a `Foo` class into a lazy ghost object, one just needs to do:
```php
class FooGhost extends Foo implements LazyGhostObjectInterface
{
    use LazyGhostObjectTrait;
}
```

And then, one can instantiate ghost objects like this:
```php
$fooGhost = FooGhost::createLazyGhostObject($initializer);
```

`$initializer` should be a closure that takes the ghost object instance as argument and initializes it. An initializer would typically call the constructor on the instance after resolving its dependencies:
```php
$initializer = function ($instance) use ($etc) {
    // [...] use $etc to compute the $deps
    $instance->__construct(...$deps);
};
```

Interface `LazyGhostObjectInterface` is optional to get the behavior of a ghost object but gives a contract that allows managing them when needed:
```php
    public function initializeLazyGhostObject(): void;
    public function resetLazyGhostObject(): bool;
```

Because initializers are *not* freed when initializing, it's possible to reset a ghost object to its uninitialized state. This comes with one limitation: resetting `readonly` properties is not allowed by the engine so these cannot be reset. The main target use case of this capability is Doctrine's EntityManager of course.

To work around the limitation with `readonly` properties, but also to allow creating partially initialized objects, `$initializer` can also accept two more arguments `$propertyName` and `$propertyScope`. When doing so, `$initializer` is going to be called on a property-by-property basis and is expected to return the computed value of the corresponding property.

Because lazy-initialization is *not* triggered when (un)setting a property, it's also possible to do partial initialization by calling setters on a just-created ghost object.

---

You might wonder why this PR is in the `VarExporter` component? The answer is that it reuses a lot of its existing code infrastructure. Exporting/hydrating/instantiating require using reflection a lot, and ghost objects too. We could consider renaming the component, but honestly, 1. I don't have a good name in mind; 2. changing the name of a component is costly for the community and 3. more importantly this doesn't really matter because this is all low-level stuff usually.

You might also wonder why this trait while we already have https://github.com/FriendsOfPHP/proxy-manager-lts and https://github.com/Ocramius/ProxyManager?

The reason is that the code infrastructure in ProxyManager is heavy. It comes with a dependency on https://github.com/laminas/laminas-code and it's complex to maintain. While I made the necessary changes to support PHP 8.1 in FriendsOfPHP/proxy-manager-lts (and submitted those changes [upstream](https://github.com/Ocramius/ProxyManager/pulls?q=is%3Apr+is%3Aopen+sort%3Aupdated-desc+author%3Anicolas-grekas)), getting support for new PHP versions is slow and complex. Don't take me wrong, I don't blame maintainers, ProxyManager is complex for a reason.

But ghost objects are way simpler than other kind of proxies that ProxyManager can produce: a trait does the job. While the trait itself is no trivial logic, it's at least plain PHP code, compared to convoluted (but needed) code generation logic in ProxyManager.

If you need any other kind of proxies that ProxyManager supports, just use ProxyManager.

For Symfony, having a simple lazy ghost object implementation will allow services declared as lazy to be actually lazy out of the box (today, you need to install proxy-manager-bridge as an optional dependency.) \o/

Commits
-------

27b4325f78 [VarExporter] Add trait to help implement lazy loading ghost objects

---
## [thepauljones/advent-of-code-2021](https://github.com/thepauljones/advent-of-code-2021)@[6e850ef87d...](https://github.com/thepauljones/advent-of-code-2021/commit/6e850ef87d5c1f1ccb94c8a59b9a1c770d0db3c7)
#### Thursday 2022-10-06 08:48:26 by Paul Jones

Jesus fucking christ almighty that was the limit
of my ability, but Michel, look! We're EQUALS! *evil laugh*

---
## [facebook/hhvm](https://github.com/facebook/hhvm)@[cbeeb6fc89...](https://github.com/facebook/hhvm/commit/cbeeb6fc896d862aff10cd75bc42ee79beb962a9)
#### Thursday 2022-10-06 16:10:14 by Lucian Wischik

I believe we never use changes_since_baseline

Summary:
Naming_sqlite stores a table that only ever has a single row: NAMING_LOCAL_CHANGES, whose row contains (1) an ocaml blob of local changes, (2) the revision for this saved-state.

The ocaml blob of local changes had been used for fast incremental naming table generation, as an ugly hack that was faster than generating the entire new naming-table from scratch i.e. writing 6M rows. In D31413518 (https://github.com/facebook/hhvm/commit/8f9e9d2f1568b084660bda8fe87b8725d61674d1) (Oct 2021) bobrenjc93 changed it to a much better technique, namely, inserting/removing only the delta rows. But it left behind the ocaml-blob of local changes. I wrote at the time "We should get rid of it: either in this diff or the next, delete the entire LocalChanges module." What gives us surety that it's okay to delete the ocaml-blob is that I had added telemetry D28839883 (https://github.com/facebook/hhvm/commit/330e97ccd08b144117c21a3ebefa248061d3d5ed) (June 2021) on the code-paths which read the ocaml-blob, and the telemetry shows that we only ever read an empty ocaml-blob.

But what about the second item, "(2) revision for this saved-state"? Do we ever use that? Reading the code shows that the only place "revision-for-saved-state" is ever consumed is by Hulk.v1 in a codepath that appears not to exist any longer, inside Naming_table.choose_local_changes. I think that Hulk.v1 used to provide a naming-table-delta along with the revision that the delta is with respect to, and it used to compare that revision against the naming-table-sqlite that it got from disk, and fail if they were different. This check had been introduced in D18723777 (https://github.com/facebook/hhvm/commit/7c671def9ee84762cf38e16d761c140a4bf01eca) (Nov 2019) for hulk remote workers. My hunch is that we're not using it any longer.

Therefore, this diff adds telemetry on the only codepath that uses "revision-for-saved-state" from the NAMING_LOCAL_CHANGES row. If this telemetry proves that we don't use it, and we already have telemetry which proves that ocaml-blob is always empty, then we'll be confident in deleting NAMING_LOCAL_CHANGES.

Reviewed By: bobrenjc93

Differential Revision: D40118751

fbshipit-source-id: 0b8e2eac4cfe8513cc5d0155184b7d15efd99dc8

---
## [A-Imtiaz/Capstone-news-report-Portfolio](https://github.com/A-Imtiaz/Capstone-news-report-Portfolio)@[ad1161fc52...](https://github.com/A-Imtiaz/Capstone-news-report-Portfolio/commit/ad1161fc5286edef89956b1ffe6adf539d382366)
#### Thursday 2022-10-06 16:11:08 by A-Imtiaz

Future of Journalism  By Imtiaz 

Future of Journalism           
By Imtiaz 

Future of Journalism With an increasing number of a visitor accessing news through mobile devices, news organizations must adopt a “Handy Friendly” model. This means packaging content in a way that is easy to digest on a small size interface. The long narrative print leads could be replaced with a shorter screen. 
For decades, newspapers produced the journalism that did the most to inform public debate and to hold those in power accountable. Even as the media system rapidly evolved over the past 20 years, studies found that newspapers remained at the core of the country’s information. In most regions of the country, because of the decline of local newspapers, the information needs of the public were frequently not being met. In these communities, people often lack a trusted local source of news. Journalism, media, and technology As journalism grows ever weaker financially—The Digital ad revenue in the US topped $100 billion in 2020, according to the Internet Advertising Statistics —and the investments made by PR firms are increasingly able to dwarf those of journalistic entities even in areas like reporting and production capabilities. 
New technologies like artificial intelligence (AI) will also drive greater efficiency and automation across many industries including publishing. In the meantime, it's hard to predict where the future of investigative journalism will be stand. 
Social Media Effects on Journalism Social media Platforms Now became the hotspot for miss information archives. On one side journalists are tried their best to bring facts-based reporting. On the other side numbers of people are attempting to manipulate public view for their benefit. Open web Technology gives those opportunists great maneuverability. At present, anyone can take a web domain, and write anything. Those biased content move around social media platform, and there is no regulation to stop such manipulation. Under the tag of Citizen Journalism, those manipulation increasing rapidly. 
Global tech platforms will took more interventionist approach on unreliable content and greater prominence for trusted news brands – along with greater support. In the end, journalism could be a bit more separated from the mass of information that is published on the internet. Pro and corns of Citizen Journalism The idea behind this citizen journalism is that people without professional Knowledge could create media. This entails that anyone who has access to the web can start a blog or can report some events across the digital world. This is significant in the way that it addresses the gaps within mainstream media. This journalistic innovation is said to help improve local economies, sharing substantial information to remote corners of the Global Citizen journalism offers a great opportunity in countries where the media, especially the mainstream media, are limited. 
One big problem with this type of journalism is that it will be difficult for people to decide what to believe, unlike traditional journalism, where it is safe to assume the information disseminated is factual. This means that citizen media should be checked for accuracy to produce news that is suitable to print. It is important to remember that we are dealing with humans here, which can make unreliable news.                                                                                                                      
 https://www.coursera.org/ Capstone: Create your own professional journalistic portfolio

---
## [LCRERGO/dwm](https://github.com/LCRERGO/dwm)@[67d76bdc68...](https://github.com/LCRERGO/dwm/commit/67d76bdc68102df976177de351f65329d8683064)
#### Thursday 2022-10-06 16:56:20 by Chris Down

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
## [Maurlcio/holbertonschool-low_level_programming](https://github.com/Maurlcio/holbertonschool-low_level_programming)@[2f790a1888...](https://github.com/Maurlcio/holbertonschool-low_level_programming/commit/2f790a18885c5e47045428fed81f6906631984c0)
#### Thursday 2022-10-06 17:11:48 by Maurlcio

holy shit literally thank google for 99% of this if any of this is even correct like what the FUCK

---
## [Shootfast/oiio](https://github.com/Shootfast/oiio)@[4e985f6347...](https://github.com/Shootfast/oiio/commit/4e985f63474e21298974a3f96536597a7306e199)
#### Thursday 2022-10-06 18:23:33 by Larry Gritz

Lay groundwork for unity builds (#3381)

As I learned recently, a "unity" (aka "jumbo") build is where multiple
.cpp files are combined into one translation unit -- imagine a unity.cpp
that simply has

    #include "file1.cpp"
    #include "file2.cpp"
    ...
    #include "fileN.cpp"

and so you compile unity.cpp instead of the separate file?.cpp files
individually.

Turns out that CMake understands this concept and can do it for you
automatically!

The benefit of a unity build is that file1...fileN probably include
most of the same headers, expand the same templates, etc., so a bunch
of the per-file work of the compiler can be done once rather than
redundantly for each file.

There are two potential downsides, however:

1. It may not be safe to concatenate your cpp files! For example, if
   both file1.cpp and file2.cpp each contain a `static int foo;`, that
   may have been safe when compiled separately, but is not allowed to
   happen twice in one compilation unit. Similarly, if you have headers
   that don't have proper guards against multiple includes, etc. So one
   should expect a whole lot of little fix-ups are needed for this to
   work properly. (We'll come back to that topic.)

2. Combining source file into these "jumbo" modules can make heavily
   parallelized builds on many-core machine not be able to load balance
   or keep all the cores busy. (Simplified examples: if you have 16 .cpp
   files on a 16 core machine, each core can compile one cpp file in
   parallel with the others. But if you mash the modules into just one
   huge cpp file, give that to one core, and your other 15 cores are
   idle, so the full build probably takes much longer.)

I tried this out, including the many fixups implied by (1) above, and
at first the unity builds were slower on both my laptop (8 cores) and
workstation at work (32 cores), because of downside (2) explained
earlier -- harder to take advantage of parallel builds when there are
fewer, bigger, compilation units. Some tweaking of strategy got me to
the point where I could always get the unity builds to go faster, but
not by a whole lot when many core were available. Slighty faster, but
not worth the trouble. A bit disappointing, nearly abandoned the whole
idea.

HOWEVER, in situation where you are limited to very few cores (like in our
CI, which allocates 2 cores, and it sure seems more like 1-1.5 for the
Windows and Mac CI runners), the unity builds are substantially faster --
there's already not much parallelism to exploit, so you come out ahead
with the savings of that redundant per-file work we talked about.

So my current thinking is to go ahead and make the changes that allow
unity builds. I don't particularly recommend them when highly parallel
builds are available to you, but it might help to cut our CI
turnaround time down on the GitHub runners. And maybe it will help in
other situations for other people.

Ok, then. The present patch introduces these concepts and makes the
CMake and other build system changes to allow unity builds. (N.B. It
won't WORK yet, so don't try it!) After we get that out of the way, in
subsequent PRs I'll show all the changs to the code that were
necessary to fix all the little things that went wrong when source
files got combined.

---
## [steenax86/OpenShadingLanguage](https://github.com/steenax86/OpenShadingLanguage)@[e4e5088ed6...](https://github.com/steenax86/OpenShadingLanguage/commit/e4e5088ed6dcd4eb636430dcce9fe815e435b1a6)
#### Thursday 2022-10-06 18:44:14 by Larry Gritz

LLVM 15.0 support (#1592)

* A variety of changes to get a clean build and passing tests when
  using LLVM 15.0.

* I've noticed problems when using LLVM 15 but building with earlier
  clang, so the cmake scripts now print a warning in that case, so if
  users encounter trouble they have a hint about what to do to fix it.

* For our CI tests on Mac, force the MacOS-11 test to use llvm 14,
  and the MacOS-12 test to use llvm 15.

IMPORTANT TO-DO / CAVEATS:

1. When doing JIT at optlevel 12 or 13, I had to disable a number of
   passes that don't seem to exist anymore in LLVM 15. This is enough
   to get it working, and to be honest, I don't know if anybody uses
   these opt levels.  But we need to revisit this, because I don't
   know if there these are cases where the names of the passes merely
   changed or that new passes take their place (in which case we
   should add the new passes, not stop after merely disabling the
   deprecated ones). For that matter, optlevel modes 11, 12, 13 are
   supposed to match what clang does for -O1, -O2, -O3, and that
   changes from one release to the next, so we should probably revisit
   this list and make sure it's matching clang's current choices
   (which I assume are crafted and periodically revised by clang's
   authors).

2. LLVM 15 switches to "opaque pointers". It still supports typed
   pointers...  for now. But as you can see in the diffs, I had to
   disable a variety of deprecation warnings and take some other
   actions to put LLVM 15 in the old "opaque ptr" mode to match our
   use of LLVM <= 14. But this is only temporary, because the typed
   pointer mode is expected to be removed entirely in LLVM 16. So at
   some point in the next few months, we are going to need to support
   opaque pointers in our use of LLVM. (Also note: for a while, we're
   going to have a bunch of ugly `#if` guards or other logic to
   support both opaque pointers for users with llvm >= 16 and also
   typed pointers for users with llvm <= 14, until such time as our
   LLVM minimum is at least 15, which I expect is not a reasonable
   assumption for at least a couple years.)

Signed-off-by: Larry Gritz <lg@larrygritz.com>

---
## [DrParadox7/Lost-Era-Modpack](https://github.com/DrParadox7/Lost-Era-Modpack)@[300d72c910...](https://github.com/DrParadox7/Lost-Era-Modpack/commit/300d72c9100474130a177c853b3bf9aef4d0eefa)
#### Thursday 2022-10-06 20:15:33 by TechnoParadox

v1.5.3

-The modpack will check for the user RAM before launch
-Waystones work interdimensionally (includes scrolls)
-Re-enabled thaumcraft 4 metal transmutations
-Disabled Wizardry's Disarmament spells on players
-Disabled unnecessary update checkers
-Reduced the deafening from Waystones by 60%
-Increased visibility while under the night sky
-Gardens are now spreadable but only drop seeds
-Buffed weak food value of some foods
-Hunger is now easier on lower difficulties
-Healing no longer consumes hunger
-GT4 Ores now have tooltips indicating where these are found
-Completely reworked Project Red pipes into Thaumcraft 4 including Thaumonomicon entries
-Added TC4 aspects for dozens of mobs and blocks
-Added dozens of entries to TC4 Crop and meat duplication
-NEI item visibility now handled by INPure
-Nerfed Mek's wind generation at higher altitude but buffed at lower ones
-Buffed Mek's Energy Storage multiblock
-Rework energy consumption of every Mek Machine (mostly lower consumption)
-Minechem can now decompose farmable materials
-Totem of Undying can now be found as loot
-Whitestone is now made from Totem of Undying
-Volcanos are now made of obsidian
-Reduced Grow Light consumption
-Fixed potential Potion ID conflicts
-Fixed Bees spawning harmful flora
-Buffed GT4 ore distribution in specific scenarios
-Fixed GT4 ore generation in the Nether
-Reworked Extra TiC compatibility
-Buffed weak fuels for the Compression and Energizing Dynamos
-Metallurgy metal and Tinker Metals now share the same stats
-Buffed Gas and RF capacity of Compact Machines
-Blacklisted XP Phial from Loonium
-Phantom Hands have a running cost of 10 LP
-Reworked Dagger of Sacrifice and Sacrificial Dagger
-Every instance of Ghast and Blaze now shed their items overtime
-Blaze Lamp cannot be used as furnace fuels anymore as a result of the above
-Soul Campfire no longer can be automated with hoppers
-Buffed TC4 Magic Biomes occurrences
-Disabled Ender Collector (unfixable dupe)
-Disabled Ender Dragon Girl
-Disabled Magnetic Force
-Disabled AE2 quartz tools
-Buffed Ars Magica 2 recipes
-Fixed End Crystal exploit
-Food records no longer persist through death
-Added missing recipes for AE2 Cards
-Extra TiC's Mana Steel parts are obtained by throwing iron parts in a mana pool
-Extra TiC's Thaumium parts are obtained by throwing iron parts in a cauldron with Praecantatio
-Extra TiC's magic materials can no longer be crafted in the Tool Table
-Added Smeltery integration to Extra TiC's magic materials
-Cheaper QED
-Snails are no longer fishes
-Wild Barley has been nerfed to be worst than barley (still grows 3x faster)
-Salt is now created by cooking water buckets
-Additional foods from the drying rack
-Cheaper Safari nets and Porta Spawners
-You can now empty Nuclearcraft capsules
-Remove the necessity of plates in the RF technological tree
-Removed needlesss microcrafting form Steve's Carts

---
## [solanum-ircd/solanum](https://github.com/solanum-ircd/solanum)@[06c5309534...](https://github.com/solanum-ircd/solanum/commit/06c53095343c2756208f6398bb7e00fb2cbe46dd)
#### Thursday 2022-10-06 21:06:29 by Ed Kellett

m_sasl: Remove implicit abort on registration

This doesn't make sense in a world where post-registration SASL is
allowed, and should fix one case of an annoying login desync that's seen
in the real world.

Specifically, when a client sends its final AUTHENTICATE and Atheme
receives it, it sends an SVSLOGIN for that client. If the client sends
us its CAP END *before* we see the SVSLOGIN, the implicit abort will try
to abort the SASL session that's already succeeded.

Atheme interprets this as an instruction to forget about the successful
SASL session; you'll connect unidentified. But it's already sent
SVSLOGIN, which will log the client in ircd-side, causing ircd and
services views to differ until the user authenticates again manually.

I think allowing a SASL session to be aborted when it has already
succeeded is an Atheme bug, and it can still be triggered without this
change. But our behaviour here seems silly anyway.

---
## [ammarfaizi2/linux-fork](https://github.com/ammarfaizi2/linux-fork)@[a7d3b7bfcf...](https://github.com/ammarfaizi2/linux-fork/commit/a7d3b7bfcf8030d6f5062c77fb62abbcec2edfe0)
#### Thursday 2022-10-06 22:01:07 by Johannes Weiner

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
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[7a06b6664f...](https://github.com/treckstar/yolo-octo-hipster/commit/7a06b6664f7f94ddbdb624118e8fce935c0c9723)
#### Thursday 2022-10-06 22:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [Kattusite/linguistics-db](https://github.com/Kattusite/linguistics-db)@[b953c2ba54...](https://github.com/Kattusite/linguistics-db/commit/b953c2ba5421b4d56df216400daabb951fd36875)
#### Thursday 2022-10-06 23:23:26 by Kattusite

Tidy const by adding enum classes & improving docs

Previously, I just shoved all of the important constants into
`const.py`, at the top-level. This kinda works, but it was really ugly.

That approach also failed to capture relationships between constants;
for example, there are many constants which all indicate a particular
type of thing, such as JSON keys, value types, or mapping relationship.

Previously I had been prefixing constants with a `X_` to indicate which
group they belonged to; e.g. `K_` for JSON keys, `D_` for parse dicts
(now renamed to `FuzzySearchTerms`), and so on.

From Python's view, these constants were unrelated, so we'd also end up with
ugly lists of constants, where we'd have to rewrite every valid constant
twice -- once to define its value, and once to register it in the list.

Python provides a much more natural mechanism for doing this -- enums.
This commit rewrites almost all of the constants in const.py so that
they now belong to an appropriate enum, grouped in with other similar
constants of the same kind. In some cases, an enum might not have been
an appropriate choice for whatever reason, and so I used a dataclass, or
just a bare class to act as a Namespace, instead.

A trade-off with the new approach is that descriptive names are way more
verbose than non-descriptive ones. Compare K_NETID with JsonKey.NETID.

To get the best of both worlds, I've aliased the descriptive names to
(nearly) the same short descriptive names as before, by giving most of
these enum classes single letter (or at least, shorter) abbreviations,
such as `K` instead of `JsonKey`, or `T` instead of `ValueType`.
This lets us type K.NETID instead of K_NETID. Not too shabby!

The P_ names stood for "Parameter", which was the old name I'd used for
SurveySpecifications. The P doesn't make a whole bunch of sense in
context anymore, but I kept it for historical reasons. I added a related
alias `Spec` for the SurveySpecification constructor, since it's more
clear than calling a random function called `P`.

This commit does its best to keep older callers up-to-date with the new
constant names, since these constants are widely used. However, legacy
files in the various "old" directories have not been updated. I don't
want to support dead code, so these files will be removed in a
subsequent commit, rather than being updated to use the new names.

This commit also changes the names of all the variables related to the
`parse_dict` / `parse_phrase` logic, which were completely inscrutable.

The `parse_phrase` function has been renamed `fuzzy_match_phrase`,
which is more accurate and better conveys the intended use.

`parse_dict` has been renamed `FuzzySearchTerm`, to tie in better with
the new name above. `fail_list` is renamed `poisoned_search_terms`,
which also might help to convey the meaning a little better.

To tie in with these new names, I've gone through and completely
rewritten the documentation for `fuzzy_match_phrase`, to explain all of
the relevant terminology, define some key terms, and provide a simple
example that illustrates intended use. The new docstring is quite
verbose (perhaps too verbose), but I thought it best to err on the side
of over-explanation, since I wrote the damn thing and even I can't
remember how it works coming back to it after many months or years.

This commit also improves code quality and style in various ways across
the project, including things like removing unused imports, adding type
annotations, and adding better error reporting on areas of the code that
broke when I tried to make changes. (If those error messages had been
there before my life would have been easier...)

---

