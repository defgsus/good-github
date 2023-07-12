## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-07-11](docs/good-messages/2023/2023-07-11.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,214,347 were push events containing 3,623,972 commit messages that amount to 312,622,871 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 75 messages:


## [Jolly-66/tgstation](https://github.com/Jolly-66/tgstation)@[755fa4db6d...](https://github.com/Jolly-66/tgstation/commit/755fa4db6d5c811770188c340cd2ccb85469d505)
#### Tuesday 2023-07-11 00:01:36 by san7890

Loads Away Missions for Unit Testing (#76245)

## About The Pull Request

Hey there,

A pretty bad bug (#76226) got through, but it was fixed pretty quickly
in #76241 (cf92862daf339e97c76b52c91f31d49ba5113bd4). I realized that if
we were testing all the away missions, that this could theoretically get
caught and not happen again. Regardless, unit testing gateway missions
has been on my to-do list for a while now, and I finally got it nailed
down.

Basically, we just have a really small "station" map with the bare bones
(_teeny_ bit of fluff, maploading is going to take 30 seconds tops
anyways let me have my kicks) with a JSON map datum flag that causes it
to load all away missions in the codebase (which are all in one folder).
Just in case some admins were planning on invoking the proc on
`SSmapping`, I also decided to gate a `tgui_alert()` behind it because
you never can be too sure of what people think is funny these days (it
really does lock up your game for a second or so at a time).

I also alphabetized the maps.txt config because that was annoying me.
## Why It's Good For The Game

Things that break on production could(?) be caught in unit testing? I
don't know if the linked issue I mentioned above would have been caught
in retrospect, but it's likely to catch more than a few upcoming bugs
(like the UO45 atmospherics thing at the very top) and ensure that these
gateway missions, which tend to be the most neglected part of mapping,
stay bug-free.

This is also helpful in case someone makes a new away mission and wants
to see if stuff's broken. Helps out maptainers a bit because very, very
technically broken mapping will throw up runtimes. Neato.
## Changelog
Nothing that players should be concerned about.

Let me know if there's a better way to approach this, but I really think
that having a super-duper light map with the bare basics to load up
gateway missions and then all nine-ish gateway missions can sequentially
load during init. I can't think of a better way to do it aside from some
really ugly `#ifdef` shit. Also also, it has the added benefit of being
a map that will always load your away mission without touching a single
shred of config (and it's not likely to break if you follow sane
practices such as making your own areas)

---
## [Jolly-66/tgstation](https://github.com/Jolly-66/tgstation)@[d1fa50db47...](https://github.com/Jolly-66/tgstation/commit/d1fa50db47dd3d11e44e8ac074ee2850f00edf19)
#### Tuesday 2023-07-11 00:01:36 by atlasle

New space ambient track (#76547)

## About The Pull Request

Adds a new space ambient track made by me to the game, supposed to be a
bit scarier than the others that were recently added as I feel that
they're a bit too happy (not to diss I really like them), also cleaned
up a bit of ambience.dm as the medical portion of it didn't follow the
same rules as the other ones. also also this will only be used for
tgstation so license wise I think this is CC BY-SA 3.0 but I'm not sure
so correct me if I'm wrong, also this is my first PR so yeah. Here's a
link to listen to the track https://voca.ro/18WvrGORDDdR

## Why It's Good For The Game

Variety is the spice of life.

## Changelog

:cl:
sound: A new ambient track will now play in space
/:cl:

---
## [Jolly-66/tgstation](https://github.com/Jolly-66/tgstation)@[48cc57010d...](https://github.com/Jolly-66/tgstation/commit/48cc57010d3ff01c55c53131b9399a4e71656d8d)
#### Tuesday 2023-07-11 00:01:36 by Jacquerel

Various spider fixes (#76528)

## About The Pull Request

Fixes #76484
Then I noticed some weird stuff which slipped through the PR and poked
at that too.

- Spiderlings and Spiders once more have names ending in (###)
- Removed an unused property on Spiderlings.
- Rewrote the descriptions for a bunch of web-abilities and web-objects
to be clearer and have better capitalisation.
- Refactored the "Web Carcass" ability to not extend from "lay web" as
it didn't need to perform most of that behaviour.
- Also I renamed it and made the description give you a hint about why
you would want to instantly spawn a statue.
- The web effigy now despawns at the same rate as the ability cools down
so you're not dumping spider statues all over the place.
- I made spiderlings move at about the same speed as humans except if
they're on webs in which case they're still pretty fast.

To be honest I am not certain an instant statue spawning button is great
to begin with and I didn't even know it was added to the game but I am
not interested in messing much with the balance for now.

This made me look at spiderlings enough that I'm going to try and make a
new sprite for them that isn't awful.

## Why It's Good For The Game

Lets you differentiate individual spiders a little bit.
Makes usage of abilities clearer.

## Changelog

:cl:
balance: Guard spider web statues despawn as the ability comes back off
cooldown.
balance: Spiderlings now only move at light speed if they're on webs,
stay safe little guys.
fix: Spiders once again have random numbers after their names.
/:cl:

---
## [Derpguy3/tgstation](https://github.com/Derpguy3/tgstation)@[e80cf8f358...](https://github.com/Derpguy3/tgstation/commit/e80cf8f3586e5aeb599e8f54bd35ebafb878e101)
#### Tuesday 2023-07-11 00:08:31 by Jacquerel

Improved spider web AI (#76637)

## About The Pull Request

The AI I coded for spiders deciding where to make webs when they aren't
otherwise occupied would do so by finding the _closest_ valid tile,
which seemed like a good idea at the time. The problem with that is that
the "closest" algorithm we use has a predictable search pattern which
meant that spiders would always predictably make a diagonal line of webs
pointing South West, which looked very silly.
I've rewritten how they pick targets to introduce some randomness, which
causes them to properly spread out and make a nicer-looking structure:
which serves purely to annoy spacemen who need to pass through this
area.


![image](https://github.com/tgstation/tgstation/assets/7483112/cb01828f-7653-4010-a4f5-2abc6e10b630)

I'll be honest I mostly did this while bored waiting for other PRs which
I require for my other branch to get merged.

## Why It's Good For The Game

This probably only annoyed me to be quite honest and if you left one
alone for long enough it would fill enough space that you couldn't tell
anyway, but it does look nicer now.

## Changelog

:cl:
add: AI-controlled spiders will make more web-shaped webs.
/:cl:

---
## [SpaceWarpDev/SpaceWarp](https://github.com/SpaceWarpDev/SpaceWarp)@[c554bd8b4e...](https://github.com/SpaceWarpDev/SpaceWarp/commit/c554bd8b4e8d4f3c16ee58d2f5b31120b4c5d6e5)
#### Tuesday 2023-07-11 00:18:08 by David

a much better builder :3

Dear fellow developers and collaborators, I humbly come before you with a sincere plea for forgiveness for the quality of my recent code. I fully acknowledge and deeply regret the shortcomings and mistakes in my implementation. I understand that my code may have caused inconveniences and difficulties, and I am truly sorry for any frustration it may have caused. I assure you that I am committed to improving my skills and knowledge, and I am eager to learn from your expertise and guidance. Please grant me the opportunity to make amends and contribute positively to our shared goals. Thank you for your understanding and kindness in this matter.

---
## [sarkahn/bevy](https://github.com/sarkahn/bevy)@[fb4c21e3e6...](https://github.com/sarkahn/bevy/commit/fb4c21e3e62b3789e8e768ac63dc2205ddec698f)
#### Tuesday 2023-07-11 00:37:47 by Ida "Iyes

bevy_audio: ECS-based API redesign (#8424)

# Objective

Improve the `bevy_audio` API to make it more user-friendly and
ECS-idiomatic. This PR is a first-pass at addressing some of the most
obvious (to me) problems. In the interest of keeping the scope small,
further improvements can be done in future PRs.

The current `bevy_audio` API is very clunky to work with, due to how it
(ab)uses bevy assets to represent audio sinks.

The user needs to write a lot of boilerplate (accessing
`Res<Assets<AudioSink>>`) and deal with a lot of cognitive overhead
(worry about strong vs. weak handles, etc.) in order to control audio
playback.

Audio playback is initiated via a centralized `Audio` resource, which
makes it difficult to keep track of many different sounds playing in a
typical game.

Further, everything carries a generic type parameter for the sound
source type, making it difficult to mix custom sound sources (such as
procedurally generated audio or unofficial formats) with regular audio
assets.

Let's fix these issues.

## Solution

Refactor `bevy_audio` to a more idiomatic ECS API. Remove the `Audio`
resource. Do everything via entities and components instead.

Audio playback data is now stored in components:
- `PlaybackSettings`, `SpatialSettings`, `Handle<AudioSource>` are now
components. The user inserts them to tell Bevy to play a sound and
configure the initial playback parameters.
- `AudioSink`, `SpatialAudioSink` are now components instead of special
magical "asset" types. They are inserted by Bevy when it actually begins
playing the sound, and can be queried for by the user in order to
control the sound during playback.

Bundles: `AudioBundle` and `SpatialAudioBundle` are available to make it
easy for users to play sounds. Spawn an entity with one of these bundles
(or insert them to a complex entity alongside other stuff) to play a
sound.

Each entity represents a sound to be played.

There is also a new "auto-despawn" feature (activated using
`PlaybackSettings`), which, if enabled, tells Bevy to despawn entities
when the sink playback finishes. This allows for "fire-and-forget" sound
playback. Users can simply
spawn entities whenever they want to play sounds and not have to worry
about leaking memory.

## Unsolved Questions

I think the current design is *fine*. I'd be happy for it to be merged.
It has some possibly-surprising usability pitfalls, but I think it is
still much better than the old `bevy_audio`. Here are some discussion
questions for things that we could further improve. I'm undecided on
these questions, which is why I didn't implement them. We should decide
which of these should be addressed in this PR, and what should be left
for future PRs. Or if they should be addressed at all.

### What happens when sounds start playing?

Currently, the audio sink components are inserted and the bundle
components are kept. Should Bevy remove the bundle components? Something
else?

The current design allows an entity to be reused for playing the same
sound with the same parameters repeatedly. This is a niche use case I'd
like to be supported, but if we have to give it up for a simpler design,
I'd be fine with that.

### What happens if users remove any of the components themselves?

As described above, currently, entities can be reused. Removing the
audio sink causes it to be "detached" (I kept the old `Drop` impl), so
the sound keeps playing. However, if the audio bundle components are not
removed, Bevy will detect this entity as a "queued" sound entity again
(has the bundle compoenents, without a sink component), just like before
playing the sound the first time, and start playing the sound again.

This behavior might be surprising? Should we do something different?

### Should mutations to `PlaybackSettings` be applied to the audio sink?

We currently do not do that. `PlaybackSettings` is just for the initial
settings when the sound starts playing. This is clearly documented.

Do we want to keep this behavior, or do we want to allow users to use
`PlaybackSettings` instead of `AudioSink`/`SpatialAudioSink` to control
sounds during playback too?

I think I prefer for them to be kept separate. It is not a bad mental
model once you understand it, and it is documented.

### Should `AudioSink` and `SpatialAudioSink` be unified into a single
component type?

They provide a similar API (via the `AudioSinkPlayback` trait) and it
might be annoying for users to have to deal with both of them. The
unification could be done using an enum that is matched on internally by
the methods. Spatial audio has extra features, so this might make it
harder to access. I think we shouldn't.

### Automatic synchronization of spatial sound properties from
Transforms?

Should Bevy automatically apply changes to Transforms to spatial audio
entities? How do we distinguish between listener and emitter? Which one
does the transform represent? Where should the other one come from?

Alternatively, leave this problem for now, and address it in a future
PR. Or do nothing, and let users deal with it, as shown in the
`spatial_audio_2d` and `spatial_audio_3d` examples.

---

## Changelog

Added:
- `AudioBundle`/`SpatialAudioBundle`, add them to entities to play
sounds.

Removed:
 - The `Audio` resource.
 - `AudioOutput` is no longer `pub`.

Changed:
 - `AudioSink`, `SpatialAudioSink` are now components instead of assets.

## Migration Guide

// TODO: write a more detailed migration guide, after the "unsolved
questions" are answered and this PR is finalized.

Before:

```rust

/// Need to store handles somewhere
#[derive(Resource)]
struct MyMusic {
    sink: Handle<AudioSink>,
}

fn play_music(
    asset_server: Res<AssetServer>,
    audio: Res<Audio>,
    audio_sinks: Res<Assets<AudioSink>>,
    mut commands: Commands,
) {
    let weak_handle = audio.play_with_settings(
        asset_server.load("music.ogg"),
        PlaybackSettings::LOOP.with_volume(0.5),
    );
    // upgrade to strong handle and store it
    commands.insert_resource(MyMusic {
        sink: audio_sinks.get_handle(weak_handle),
    });
}

fn toggle_pause_music(
    audio_sinks: Res<Assets<AudioSink>>,
    mymusic: Option<Res<MyMusic>>,
) {
    if let Some(mymusic) = &mymusic {
        if let Some(sink) = audio_sinks.get(&mymusic.sink) {
            sink.toggle();
        }
    }
}
```

Now:

```rust
/// Marker component for our music entity
#[derive(Component)]
struct MyMusic;

fn play_music(
    mut commands: Commands,
    asset_server: Res<AssetServer>,
) {
    commands.spawn((
        AudioBundle::from_audio_source(asset_server.load("music.ogg"))
            .with_settings(PlaybackSettings::LOOP.with_volume(0.5)),
        MyMusic,
    ));
}

fn toggle_pause_music(
    // `AudioSink` will be inserted by Bevy when the audio starts playing
    query_music: Query<&AudioSink, With<MyMusic>>,
) {
    if let Ok(sink) = query.get_single() {
        sink.toggle();
    }
}
```

---
## [warface1234455/Yoggie](https://github.com/warface1234455/Yoggie)@[d1c7dfdc1a...](https://github.com/warface1234455/Yoggie/commit/d1c7dfdc1ae55bfd9fa7f603f415b762ba6a472a)
#### Tuesday 2023-07-11 00:46:43 by SapphicOverload

IPC tweaks (#19467)

* funny tv head robot go brrrrr

* Update IPC.dm

* not that fast

* fuck it we ball

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[2ee79d7077...](https://github.com/tgstation/tgstation/commit/2ee79d7077804f4e918d6c4bdbe856570cf24a01)
#### Tuesday 2023-07-11 00:55:47 by Jacquerel

Bots no longer require PAIs to become sapient (#76691)

## About The Pull Request

We were talking in the coder channel about what the role of a pAI is,
with a general conclusion that as the name would suggest they should be
_personal assistants_.
This means they should be sticking around their owner, not wandering
away as a holochassis or in the body of a bot.
The former is a matter for a future PR, the latter I am addressing here.

What we also discussed is that clearly some people _want_ to respawn as
a weird quasi-useless mob which wanders aimlessly around the station.
That seems like a fine thing to exist, but it shouldn't be a pAI.

Resultingly: pAI cards can no longer be placed inside bots.
However, you also no longer need to place pAI cards inside bots in order
for them to become sapient, it's a simple toggle on the bot control
menu. Enabling this option will poll ghosts
Toggling the "personality matrix" off while a bot is being controlled by
a ghost will ghost them again, so if they're annoying they're not that
hard to get rid of.


![image](https://github.com/tgstation/tgstation/assets/7483112/ec14c2f2-3c0f-4f03-9dfc-22abca00a477)

Mobs which couldn't have a pAI inserted don't have this option.
Specifically securitrons, ED-209, and Hygienebots (for some reason).

Perhaps most controversially, any bots which are present on the station
when the map loads will have this setting enabled by default. We will
see if players abuse this too much and need their toys taken away, I am
hoping they can be trusted.

Additionally, as part of this change, mobs you can possess now appear in
the spawners menu.

![image](https://github.com/tgstation/tgstation/assets/7483112/7c505471-43de-4e4e-89a5-877dc3086684)
Here is an unusually populated example.

Oh also in the process of doing this I turned the regal rat "click this
to become it" behaviour into a component because it seems generally
useful.

## Why It's Good For The Game

Minor stuff for dead players to do if they want to interact with living
players instead of observe.
Shift pAI back into a more intended role as a personal assistant who
hangs around with their owner, rather than just a generic respawn role.

## Changelog

:cl:
add: PAIs can no longer be inserted into Bots
add: Bots can now have their sapience toggled by anyone with access to
their settings panel
add: Bots which exist on the map at the start of the round automatically
have this setting enabled
qol: Bots, Regal Rats, and Cargorilla now appear in the Spawners menu if
you are dead
qol: Bots can be renamed from their maintenance panel
/:cl:

---
## [S34NW/Paradise](https://github.com/S34NW/Paradise)@[a3dc32cf34...](https://github.com/S34NW/Paradise/commit/a3dc32cf344dbd441e85f6cbb694b166dc1f5e4b)
#### Tuesday 2023-07-11 01:03:19 by ATP-Engineer

Fixes issue where Turret Control sprites arent actually updated in previous PR (#21538)

* Removes actual turret file

FUCK

* Fixes turret controllers not actually being changed

GOD DAMNIT.

---
## [kernel-patches/bpf](https://github.com/kernel-patches/bpf)@[bdd988a858...](https://github.com/kernel-patches/bpf/commit/bdd988a8589cef2f1d3da304a3a699b81b9622ac)
#### Tuesday 2023-07-11 01:19:52 by Daniel Borkmann

bpf: Add fd-based tcx multi-prog infra with link support

This work refactors and adds a lightweight extension ("tcx") to the tc BPF
ingress and egress data path side for allowing BPF program management based
on fds via bpf() syscall through the newly added generic multi-prog API.
The main goal behind this work which we also presented at LPC [0] last year
and a recent update at LSF/MM/BPF this year [3] is to support long-awaited
BPF link functionality for tc BPF programs, which allows for a model of safe
ownership and program detachment.

Given the rise in tc BPF users in cloud native environments, this becomes
necessary to avoid hard to debug incidents either through stale leftover
programs or 3rd party applications accidentally stepping on each others toes.
As a recap, a BPF link represents the attachment of a BPF program to a BPF
hook point. The BPF link holds a single reference to keep BPF program alive.
Moreover, hook points do not reference a BPF link, only the application's
fd or pinning does. A BPF link holds meta-data specific to attachment and
implements operations for link creation, (atomic) BPF program update,
detachment and introspection. The motivation for BPF links for tc BPF programs
is multi-fold, for example:

  - From Meta: "It's especially important for applications that are deployed
    fleet-wide and that don't "control" hosts they are deployed to. If such
    application crashes and no one notices and does anything about that, BPF
    program will keep running draining resources or even just, say, dropping
    packets. We at FB had outages due to such permanent BPF attachment
    semantics. With fd-based BPF link we are getting a framework, which allows
    safe, auto-detachable behavior by default, unless application explicitly
    opts in by pinning the BPF link." [1]

  - From Cilium-side the tc BPF programs we attach to host-facing veth devices
    and phys devices build the core datapath for Kubernetes Pods, and they
    implement forwarding, load-balancing, policy, EDT-management, etc, within
    BPF. Currently there is no concept of 'safe' ownership, e.g. we've recently
    experienced hard-to-debug issues in a user's staging environment where
    another Kubernetes application using tc BPF attached to the same prio/handle
    of cls_bpf, accidentally wiping all Cilium-based BPF programs from underneath
    it. The goal is to establish a clear/safe ownership model via links which
    cannot accidentally be overridden. [0,2]

BPF links for tc can co-exist with non-link attachments, and the semantics are
in line also with XDP links: BPF links cannot replace other BPF links, BPF
links cannot replace non-BPF links, non-BPF links cannot replace BPF links and
lastly only non-BPF links can replace non-BPF links. In case of Cilium, this
would solve mentioned issue of safe ownership model as 3rd party applications
would not be able to accidentally wipe Cilium programs, even if they are not
BPF link aware.

Earlier attempts [4] have tried to integrate BPF links into core tc machinery
to solve cls_bpf, which has been intrusive to the generic tc kernel API with
extensions only specific to cls_bpf and suboptimal/complex since cls_bpf could
be wiped from the qdisc also. Locking a tc BPF program in place this way, is
getting into layering hacks given the two object models are vastly different.

We instead implemented the tcx (tc 'express') layer which is an fd-based tc BPF
attach API, so that the BPF link implementation blends in naturally similar to
other link types which are fd-based and without the need for changing core tc
internal APIs. BPF programs for tc can then be successively migrated from classic
cls_bpf to the new tc BPF link without needing to change the program's source
code, just the BPF loader mechanics for attaching is sufficient.

For the current tc framework, there is no change in behavior with this change
and neither does this change touch on tc core kernel APIs. The gist of this
patch is that the ingress and egress hook have a lightweight, qdisc-less
extension for BPF to attach its tc BPF programs, in other words, a minimal
entry point for tc BPF. The name tcx has been suggested from discussion of
earlier revisions of this work as a good fit, and to more easily differ between
the classic cls_bpf attachment and the fd-based one.

For the ingress and egress tcx points, the device holds a cache-friendly array
with program pointers which is separated from control plane (slow-path) data.
Earlier versions of this work used priority to determine ordering and expression
of dependencies similar as with classic tc, but it was challenged that for
something more future-proof a better user experience is required. Hence this
resulted in the design and development of the generic attach/detach/query API
for multi-progs. See prior patch with its discussion on the API design. tcx is
the first user and later we plan to integrate also others, for example, one
candidate is multi-prog support for XDP which would benefit and have the same
'look and feel' from API perspective.

The goal with tcx is to have maximum compatibility to existing tc BPF programs,
so they don't need to be rewritten specifically. Compatibility to call into
classic tcf_classify() is also provided in order to allow successive migration
or both to cleanly co-exist where needed given its all one logical tc layer and
the tcx plus classic tc cls/act build one logical overall processing pipeline.

tcx supports the simplified return codes TCX_NEXT which is non-terminating (go
to next program) and terminating ones with TCX_PASS, TCX_DROP, TCX_REDIRECT.
The fd-based API is behind a static key, so that when unused the code is also
not entered. The struct tcx_entry's program array is currently static, but
could be made dynamic if necessary at a point in future. The a/b pair swap
design has been chosen so that for detachment there are no allocations which
otherwise could fail.

The work has been tested with tc-testing selftest suite which all passes, as
well as the tc BPF tests from the BPF CI, and also with Cilium's L4LB.

Kudos also to Nikolay Aleksandrov and Martin Lau for in-depth early reviews
of this work.

  [0] https://lpc.events/event/16/contributions/1353/
  [1] https://lore.kernel.org/bpf/CAEf4BzbokCJN33Nw_kg82sO=xppXnKWEncGTWCTB9vGCmLB6pw@mail.gmail.com
  [2] https://colocatedeventseu2023.sched.com/event/1Jo6O/tales-from-an-ebpf-programs-murder-mystery-hemanth-malla-guillaume-fournier-datadog
  [3] http://vger.kernel.org/bpfconf2023_material/tcx_meta_netdev_borkmann.pdf
  [4] https://lore.kernel.org/bpf/20210604063116.234316-1-memxor@gmail.com

Signed-off-by: Daniel Borkmann <daniel@iogearbox.net>

---
## [kernel-patches/bpf](https://github.com/kernel-patches/bpf)@[951d2b3d98...](https://github.com/kernel-patches/bpf/commit/951d2b3d98c5f42213f806ea00c011926610b4f0)
#### Tuesday 2023-07-11 01:19:52 by Daniel Borkmann

bpf: Add generic attach/detach/query API for multi-progs

This adds a generic layer called bpf_mprog which can be reused by different
attachment layers to enable multi-program attachment and dependency resolution.
In-kernel users of the bpf_mprog don't need to care about the dependency
resolution internals, they can just consume it with few API calls.

The initial idea of having a generic API sparked out of discussion [0] from an
earlier revision of this work where tc's priority was reused and exposed via
BPF uapi as a way to coordinate dependencies among tc BPF programs, similar
as-is for classic tc BPF. The feedback was that priority provides a bad user
experience and is hard to use [1], e.g.:

  I cannot help but feel that priority logic copy-paste from old tc, netfilter
  and friends is done because "that's how things were done in the past". [...]
  Priority gets exposed everywhere in uapi all the way to bpftool when it's
  right there for users to understand. And that's the main problem with it.

  The user don't want to and don't need to be aware of it, but uapi forces them
  to pick the priority. [...] Your cover letter [0] example proves that in
  real life different service pick the same priority. They simply don't know
  any better. Priority is an unnecessary magic that apps _have_ to pick, so
  they just copy-paste and everyone ends up using the same.

The course of the discussion showed more and more the need for a generic,
reusable API where the "same look and feel" can be applied for various other
program types beyond just tc BPF, for example XDP today does not have multi-
program support in kernel, but also there was interest around this API for
improving management of cgroup program types. Such common multi-program
management concept is useful for BPF management daemons or user space BPF
applications coordinating internally about their attachments.

Both from Cilium and Meta side [2], we've collected the following requirements
for a generic attach/detach/query API for multi-progs which has been implemented
as part of this work:

  - Support prog-based attach/detach and link API
  - Dependency directives (can also be combined):
    - BPF_F_{BEFORE,AFTER} with relative_{fd,id} which can be {prog,link,none}
      - BPF_F_ID flag as {fd,id} toggle; the rationale for id is so that user
        space application does not need CAP_SYS_ADMIN to retrieve foreign fds
        via bpf_*_get_fd_by_id()
      - BPF_F_LINK flag as {prog,link} toggle
      - If relative_{fd,id} is none, then BPF_F_BEFORE will just prepend, and
        BPF_F_AFTER will just append for attaching
      - Enforced only at attach time
    - BPF_F_REPLACE with replace_bpf_fd which can be prog, links have their
      own infra for replacing their internal prog
    - If no flags are set, then it's default append behavior for attaching
  - Internal revision counter and optionally being able to pass expected_revision
  - User space application can query current state with revision, and pass it
    along for attachment to assert current state before doing updates
  - Query also gets extension for link_ids array and link_attach_flags:
    - prog_ids are always filled with program IDs
    - link_ids are filled with link IDs when link was used, otherwise 0
    - {prog,link}_attach_flags for holding {prog,link}-specific flags
  - Must be easy to integrate/reuse for in-kernel users

The uapi-side changes needed for supporting bpf_mprog are rather minimal,
consisting of the additions of the attachment flags, revision counter, and
expanding existing union with relative_{fd,id} member.

The bpf_mprog framework consists of an bpf_mprog_entry object which holds
an array of bpf_mprog_fp (fast-path structure). The bpf_mprog_cp (control-path
structure) is part of bpf_mprog_bundle. Both have been separated, so that
fast-path gets efficient packing of bpf_prog pointers for maximum cache
efficiency. Also, array has been chosen instead of linked list or other
structures to remove unnecessary indirections for a fast point-to-entry in
tc for BPF.

The bpf_mprog_entry comes as a pair via bpf_mprog_bundle so that in case of
updates the peer bpf_mprog_entry is populated and then just swapped which
avoids additional allocations that could otherwise fail, for example, in
detach case. bpf_mprog_{fp,cp} arrays are currently static, but they could
be converted to dynamic allocation if necessary at a point in future.
Locking is deferred to the in-kernel user of bpf_mprog, for example, in case
of tcx which uses this API in the next patch, it piggybacks on rtnl.

An extensive test suite for checking all aspects of this API for prog-based
attach/detach and link API comes as BPF selftests in this series.

Kudos also to Andrii Nakryiko for API discussions wrt Meta's BPF management.

  [0] https://lore.kernel.org/bpf/20221004231143.19190-1-daniel@iogearbox.net
  [1] https://lore.kernel.org/bpf/CAADnVQ+gEY3FjCR=+DmjDR4gp5bOYZUFJQXj4agKFHT9CQPZBw@mail.gmail.com
  [2] http://vger.kernel.org/bpfconf2023_material/tcx_meta_netdev_borkmann.pdf

Signed-off-by: Daniel Borkmann <daniel@iogearbox.net>

---
## [MattKobayashi/containers](https://github.com/MattKobayashi/containers)@[cc06021016...](https://github.com/MattKobayashi/containers/commit/cc06021016331b0c83ae54111ed9e36e7e2ef777)
#### Tuesday 2023-07-11 01:32:06 by Matthew Kobayashi

Merge pull request #74 from MattKobayashi/actions

Fuck you BuildKit

---
## [draxxthemsklounst56/git](https://github.com/draxxthemsklounst56/git)@[07f91e5e79...](https://github.com/draxxthemsklounst56/git/commit/07f91e5e79810a8f17de745d2d84c384add75f0a)
#### Tuesday 2023-07-11 01:44:47 by Jeff King

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
## [northivanastan/freedoom](https://github.com/northivanastan/freedoom)@[8c076fcba9...](https://github.com/northivanastan/freedoom/commit/8c076fcba9bb94637d22431b21b862a481fff01f)
#### Tuesday 2023-07-11 01:54:35 by mc776

levels: minor Phase 2 fixes. (#964)

* levels: minor Phase 2 fixes.

Mostly for addressing #694.

Map05
Realigned grey hex textures around soulsphere switch. Now the odd one out is the door.

Map09
Fixed up the lighting in the start room.
Reflagged some secret doors as secret rather than hidden.
Consolidated the two W1 Floor to LAC triggers around the yellow key.
The red key rocket launcher sequence could potentially mess someone up who - given the hatchling closet, quite reasonably - avoids grabbing the rocket launcher. It seems needlessly convoluted, but it is a funny prank how the switch makes the red key disappear entirely for a bit. Instead of untangling this I'm just going to add some health bonuses around the rocket launcher so the player will eventually go there.
Tried to mitigate the worst of the various crimes against texture alignment in the crate maze, adding a light source in the process. It would take a *lot* of work to make it actually look good, a lot more than can be done in a batch bugfix PR.

Map10
Lower unpegged sector 70 (red door leading outside) door tracks.
Added matching midtexes to the insides of the fences around the lights by the door leading to the final corridor.
Line 839 (south-southeast red armour behind waterfall) flagged secret and the lines on the other side flagged hidden.

Map11
Realigned grey hexes in corridor around minigunner switch room.
Added an evil eye right in front of the shootwall secret.

Map12
Change line 330 midtex to the new MIDSPCSM with no offset.
Lower-unpegged line 4787 doortrack.

Map13
Sectors 243 no longer uses mismatching TLITE6_5 flat. (Sector 170 actually looks okay ingame.)
Realigned line 260.

Map15
Line 163 W1 changed to WR to prevent a potential softlock.
Aligned COMPSPAN on sector 561 to match surroundings.
Fixed some textures in the green corridor in the west overlooking the nukage. Also set those zombies in there to ambush since that seems to be the intention based on their placement, and made that big block thingy on the east end of that corridor a more normal-looking door.
Touched up greyhex near sector 491.
Flagged linedef 5293 secret.
Sectors 145 and 116 (rock fringe around nukage around red key platform) consolidated into one sector, made non-damaging, and without the invisible blocking lines.

Map16
Changed Line 1089 to SR instead of S1. (Switch that opens the secret to the east)
Realigned all the SUPPORT3s in that little painlord corridor while shrinking the "ribs" a bit; also widened the little exit atrium so the space between the lights is as wide as the door. (After looking at the others I am not going to widen any more corridors at this time.)
Grossly simplified the twisty yellow key corridor, and lowered the ceiling of the outside of the door so the yellow door stripe would fit properly. One doortrack needed to be given the DOORTRAK texture. The remaining "ribs" are recessed further inside the wall so they do not impede movement at all.
Lowered the ceiling above the other yellow marked door as well. The corridor around the corner has been expanded slightly.

Map22
Flagged line 830 secret.

Map23
Fixed candle placement on east end of zombieman corridor.
Consolidated some identical sectors around the big "AGM" floor and lowered the torch platforms so they wouldn't clip into the ceiling.
Raised the ceilings on the techpillars right after the first long lift. The walls in front of them now match their surroundings.
Removed lower unpegged from lines 2066, 2082, 2062, 2075. ("Door"tracks for the route across those pillars in the southeast - they're actually lifts not doors)
SSG secret fixed. (And marked.)

Map28
Lines 2326, 622 lagged secret.
Realigned lines 4594 and 4671.
Realigned scrolling textures around sector 517.
Touched up monster closet around sector 399, changing to to 8 about HAF fast and making the closet a bit taller so there'd be a better natural threshold between those areas. The doortracks were fine, if a bit complex.
Raised sector 474 ceiling to match marble brick seams.
Made sector 147 (cubes hanging over hot rocks) do damage and sectors 91 and 115 (teleport pads) not.

Map29
Swapped out the textures on the sides of the big green skull pad.

* levels: fix up map23 southeast secret textures.

I messed up the texture replacement around the green torch, the extreme sudden darkness ruined the blue AGM text, the pillar lift-doors needed a better division between the tekwall and red rock, and that huge swathe of DOORTRAK hurt to look at in vanilla.

* levels: map07 aesthetic fixes.

Replaced BIGDOOR1 on sector 50 as it was giving tutti-frutti.

Fixed the textures on the lifts in the green area beyond the outdoor area.

Miscellaneous texture alignment fixes and added some more thresholds between materials.

---
## [pexel5/CEV-Eris](https://github.com/pexel5/CEV-Eris)@[b92562ad8f...](https://github.com/pexel5/CEV-Eris/commit/b92562ad8f26c2354730f8a013195a90bbfbe9fd)
#### Tuesday 2023-07-11 02:18:58 by ValoTheValo

Makes the "Gun" Not spawn in maint, makes MK58 fit in holsters (#8200)

* changes item path to be consistent

i hate kegdo

* kegdo code moment

what fucking moron designed this

* fixes MK58 not fitting in holster

pain

* Update holster.dm

* kegdo moment

---
## [knative-automation/kn-plugin-admin](https://github.com/knative-automation/kn-plugin-admin)@[60064f0b77...](https://github.com/knative-automation/kn-plugin-admin/commit/60064f0b77de4e069e78f9a926b66680545bf813)
#### Tuesday 2023-07-11 03:06:05 by Knative Automation

upgrade to latest dependencies

bumping github.com/matttproud/golang_protobuf_extensions c182aff...c182aff:%0Abumping github.com/fsnotify/fsnotify 0f4b979...5f8c606:%0A  > 5f8c606 Update ChangeLog%0A  > 8878587 Tweak the docs a bit%0A  > 89b4cf1 Add test for re-adding a renamed file (# 508)%0A  > 85acde2 Update x/sys%0A  > 69c24b0 Update x/sys%0A  > fb07f82 Add test to see what happens if you watch a symlink (# 498)%0A  > 666da9c Clarify doc comment on WatchList() (# 499)%0A  > 123e4e3 Add note about README version%0A  > 61a05ce Update documentation and examples (# 496)%0A  > e180a87 Move some inotify-tests to run on all backends; test that state is cleaned up after Remove (# 494)%0A  > fdf41a3 Move some files around%0A  > 844d71f Port minor test changes from fen-v2 branch; make LICENSE text not ugly%0A  > 5b87f50 windows: simplify a bit (# 493)%0A  > 2bfaa00 all: add Watcher.{sendEvent,sendError} (# 492)%0A  > 8ab3b84 kqueue: don't set up watchers on unreadable files (# 479)%0A  > a4bcdf8 Update changelog%0A  > 4b43fad kqueue: remove timeout from unix.Kevent() (# 480)%0A  > a24f78c windows: test symlinks (# 491)%0A  > f45391f windows: run TestWatchRename/rename_overwriting_existing_file (# 490)%0A  > ee33a65 Use "os.Rename()" in tests instead of "mv"%0A  > 9dd0568 cmd/fsnotify: fix time.Format() string%0A  > 5dcbfba windows: replace syscall with golang.org/x/sys/windows%0A  > 1f8edaf windows: replace "e" with "err" for error variables%0A  > 99715ba windows: increase buffer size from 4K to 64K (# 485)%0A  > a5c5815 ci: update to use Go 1.19, kick off fewer builds, update x/sys (# 484)%0A  > f2d35c3 Remove CLA section in contributing%0A  > 4604469 Need Linux 5.9 for a useful fanotify we can use%0A  > a566bb1 Update CONTRIBUTING.md%0A  > 01dfc6f Remove PULL_REQUEST_TEMPLATE%0A  > a58e868 Run tests in illumos (# 481)%0A  > 666c6a0 Update ChangeLog%0A  > 928895c [bugfix] close handle when remWatch open in getIno (# 288)%0A  > f174f95 windows: update watch paths when renaming directories with sub-watches (# 370)%0A  > 87dc1fa Rewrite tests (# 478)%0A  > 57e6a49 Add {Event,Op}.Has() (# 477)%0A  > 39823aa Document that /proc and /sys won't work%0A  > 60fbf57 Clarify FAQ on goroutines%0A  > ca0e2f4 macos: retry if open() returns EINTR (# 475)%0A  > ff39bb4 Fix lint (# 476)%0A  > 421f529 debian 6 test: deal with multiple packages (# 474)%0A  > a3256ef Remove AUTHORS file%0A  > 0e78fa6 Update README: split out FAQ to "Platform-specific notes"%0A  > 1a7b6ef inotify: don't ignore events for files that don't exist (# 470)%0A  > f0aceb2 Tweak comment regarding relative paths (# 466)%0A  > d9c9fa5 Add cmd/fsnotify (# 463)%0A  > cc15908 kqueue: better error if watching a file fails (# 471)%0A  > c4e64e4 Replace Use of Kthread-blocking Epoll with Poller Read, Remove Per-Event LStats on Linux # 433 (# 434)%0A  > 4b8b298 Test some more things in CI (# 469)%0A  > 548b8fb Add missing changelog for 1.4.{8,9} (# 468)%0A  > 7fe2936 inotify: fix race in Close() (# 465)%0A  > 35b6378 Clarify README on network drives (# 467)%0A  > e56409e Update link to CONTRIBUTING in the README (# 464)%0A  > 4678dfd Update documentation for linux systems (max_user_watches) (# 287)%0A  > 808f582 bump up GitHub Actions (# 461)%0A  > 4193dfd Do not suppress Chmod on non-existent file (# 260)%0A  > 6ae56b7 kqueue: Make watcher.Close() O(n) instead of O(n^2) (# 233)%0A  > adf5320 strings.Builder instead of bytes.Buffer (# 285)%0A  > 217e78e Explicit mutext (un)locking (# 462)%0A  > 1a4f949 Use common error when removing an unwatched file (# 460)%0A  > 5acfdc1 windows: protect access to isClosed with mutex (# 454)%0A  > c56cafd Test Go 1.18%0A  > 37badf6 This project is archived (# 459)%0Abumping knative.dev/serving 2c1bb07...4c76e3b:%0A  > 4c76e3b Drop workaround pach for Istio (# 14156)%0A  > d97db13 Update net-kourier nightly (# 14160)%0A  > 1559c9b Bump net-certmanager manifests and add kapp ordering overlay (# 14148)%0A  > 52fe24e upgrade to latest dependencies (# 14155)%0A  > a5c8c2e Update community files (# 14154)%0A  > 2a17873 Separate Activator SA (# 14133)%0A  > fc166ac Consolidate webhooks (# 14082)%0A  > b935bea Set QP resource defaults (# 14039)%0A  > 529c5e4 Update net-kourier nightly (# 14150)%0A  > 4ccd1c9 Implement Stringer for nil podTracker (# 14147)%0A  > bd3e5e3 upgrade to latest dependencies (# 14151)%0A  > ebbca26 upgrade to latest dependencies (# 14149)%0A  > bde2f42 Update net-gateway-api nightly (# 14144)%0A  > bb1262e Update net-kourier nightly (# 14129)%0A  > 32ec382 Drop unused ytt patch for Ingress ServiceType (# 14143)%0A  > 4c3b36c Update net-gateway-api nightly (# 14136)%0A  > 9a75a93 Update net-istio nightly (# 14132)%0A  > ca618b7 Update net-certmanager nightly (# 14131)%0A  > ea3e9c3 Update net-contour nightly (# 14130)%0A  > 2e7d6e4 Update community files (# 14128)%0A  > 63fa389 Allow to set QP resources per service (# 14038)%0A  > 9310e4d Update net-kourier nightly (# 14125)%0A  > 0462ce6 Update net-istio nightly (# 14126)%0A  > 2813b9a Update net-gateway-api nightly (# 14119)%0A  > eaf666e Update net-istio nightly (# 14116)%0A  > 53169cd Update net-istio nightly (# 14112)%0A  > e865aa7 Update net-contour nightly (# 14109)%0A  > 921daf8 Update net-certmanager nightly (# 14111)%0A  > bb581cc Update net-kourier nightly (# 14110)%0A  > fbfffc0 upgrade to latest dependencies (# 14108)%0A  > bcf9274 upgrade to latest dependencies (# 14101)%0A  > f085b30 fix: requests are sent to all pods even if cc=1 and the parity of activatorCount and podTracker is different (# 14022)%0A  > 9772417 Update net-kourier nightly (# 14107)%0A  > f6d0c7b Update net-contour nightly (# 14106)%0A  > 560e0ea Update net-certmanager nightly (# 14105)%0A  > 51f4f1e Update net-istio nightly (# 14104)%0A  > 18519b1 Update net-contour nightly (# 14079)%0A  > 38c155e Add chainguard-dev/actions for creating kind cluster (# 14018)%0A  > 74c57d8 Update net-istio nightly (# 14098)%0A  > 5a9c574 Update net-kourier nightly (# 14096)%0A  > 3a6c2b6 upgrade to latest dependencies (# 14095)%0A  > 5a90438 Update net-istio nightly (# 14091)%0A  > dc0692a Update net-istio nightly (# 14088)%0A  > 0fbd780 Update net-certmanager nightly (# 14087)%0A  > 6f63c98 Update net-kourier nightly (# 14086)%0A  > e74f5f4 Update net-gateway-api nightly (# 14085)%0A  > 1587070 Update net-kourier nightly (# 14081)%0A  > 2e00e9f Update net-certmanager nightly (# 14080)%0A  > a3c7864 Update net-istio nightly (# 14078)%0A  > 384b889 Update net-gateway-api nightly (# 14077)%0A  > 7d0f963 Change storage version of DomainMapping to v1beta1 (# 14058)%0A  > e8b6f05 Update net-gateway-api nightly (# 14068)%0A  > 41e4212 Get certificate reconciler from `networking` instead of `control-protocol` (# 14072)%0A  > e71b933 Update net-certmanager nightly (# 14070)%0A  > 8f516b6 Update net-kourier nightly (# 14069)%0A  > a2bb4aa upgrade to latest dependencies (# 14071)%0A  > c95f17b Update community files (# 14067)%0A  > bf48e64 Remove deprecated internalEncryption dependency (# 14064)%0A  > 6b87d67 Update net-istio nightly (# 14065)%0A  > fbecf34 refactor throttler_test.go (# 14055)%0A  > 349b2d6 Change minimum TLS version to 1.3 for internal encryption (between activator and queue-proxy) (# 13887)%0A  > d07bf78 Update net-contour nightly (# 14049)%0A  > aa023e8 Update net-istio nightly (# 14048)%0A  > 8fc4bb9 Update net-gateway-api nightly (# 14047)%0A  > 135be30 Update net-certmanager nightly (# 14046)%0A  > 8da71b5 Update net-kourier nightly (# 14042)%0A  > 13a4e46 poll until timeout - don't error out if the deployment can't be found (# 14027)%0A  > 31c2b7e upgrade to latest dependencies (# 14043)%0A  > 6a6e417 Update net-istio nightly (# 14041)%0A  > 807fc2c Update net-certmanager nightly (# 14040)%0A  > 3c23945 drop safe to evict annotations (# 14035)%0A  > fca5c14 Update net-gateway-api nightly (# 14033)%0A  > c12c917 Update net-contour nightly (# 14034)%0A  > 2da856d Update net-kourier nightly (# 14032)%0A  > d7c8779 Update net-certmanager nightly (# 14031)%0A  > aaf01dc Update net-istio nightly (# 14030)%0A  > bdaa436 RandomChoice 2 policy wasn't random when the number of targets is 2 (with equal weight) (# 14028)%0A  > c91f8c4 Fix metrics reporting period (# 14019)%0A  > 9f60969 Update net-kourier nightly (# 14004)%0A  > 6020cec Update net-istio nightly (# 14025)%0A  > 88cae7f Update net-gateway-api nightly (# 14016)%0A  > a143bf8 Update net-contour nightly (# 14015)%0A  > c2be582 Update net-certmanager nightly (# 14014)%0A  > 3450f0a upgrade to latest dependencies (# 14013)%0A  > 35cfd8f [Automated] Update net-gateway-api nightly (# 14003)%0A  > 08a9708 Update net-istio nightly (# 14009)%0A  > 5074b4c Update net-contour nightly (# 14010)%0A  > e8cb343 upgrade to latest dependencies (# 13999)%0A  > 1261074 Update net-certmanager nightly (# 14002)%0A  > f987ca6 Bump kind to 0.19 (# 14008)%0A  > fbb7fa1 Update community files (# 13998)%0A  > bff1d80 Remove 1.24 kind version (# 14007)%0A  > a657321 Update net-kourier nightly (# 13993)%0A  > d75b0f0 Update net-contour nightly (# 13990)%0A  > 6d26f54 upgrade to latest dependencies (# 13991)%0A  > df5001f Update net-certmanager nightly (# 13992)%0A  > 2594084 upgrade to latest dependencies (# 13989)%0A  > 7c303fa Update cluster-version to 1.25 (# 13988)%0A  > 9e751a2 Update net-certmanager nightly (# 13974)%0A  > 7b35cfb upgrade to latest dependencies (# 13987)%0A  > 99800ed Set default domain to cluster's domain (# 13964)%0A  > c90fabf Metric annotations work with global class config (# 13978)%0A  > da31cd1 Update net-kourier nightly (# 13975)%0A  > f457924 Update net-contour nightly (# 13976)%0A  > 14ad4d1 upgrade to latest dependencies (# 13973)%0A  > 00ddfd9 Update net-kourier nightly (# 13972)%0A  > fc63583 Update net-kourier nightly (# 13966)%0A  > 219285e Update net-kourier nightly (# 13959)%0A  > 2fa05bd Min TLS for tag to digest defaults to 1.2 again and is configurable (# 13962)%0A  > 43df348 Update net-contour nightly (# 13958)%0A  > 50a9f22 Update net-certmanager nightly (# 13961)%0A  > 4e379cb Update net-gateway-api nightly (# 13957)%0A  > 3d53294 Update net-istio nightly (# 13960)%0A  > ea2a6c8 :lipstick: Install ko using setup-ko, from ko-build (# 13951)%0A  > e5070cd upgrade to latest dependencies (# 13950)%0A  > 9778f2d Update net-istio nightly (# 13949)%0A  > f27ba4e Update net-certmanager nightly (# 13944)%0A  > 2840301 Update net-kourier nightly (# 13945)%0A  > 117a642 Update net-gateway-api nightly (# 13943)%0A  > 84a2230 Update net-contour nightly (# 13942)%0A  > 7aa5edb upgrade to latest dependencies (# 13941)%0A  > 01707d8 upgrade to latest dependencies (# 13940)%0A  > b7d5e8d Update net-istio nightly (# 13939)%0A  > 5e056a0 Update net-certmanager nightly (# 13926)%0A  > 35efd12 Update net-contour nightly (# 13929)%0A  > f476717 Update net-istio nightly (# 13935)%0A  > bd8e37c Update net-gateway-api nightly (# 13925)%0A  > 37a7010 Update net-kourier nightly (# 13934)%0A  > f47802d Update community files (# 13933)%0A  > 990d701 Update net-kourier nightly (# 13928)%0A  > ff9f03d Update net-istio nightly (# 13927)%0A  > 690c525 upgrade to latest dependencies (# 13924)%0A  > 1dd07a7 Update community files (# 13923)%0A  > 66141b8 Update net-istio nightly (# 13920)%0Abumping golang.org/x/sys 90c8f94...a1a9c4b:%0A  > a1a9c4b unix/linux: update to Linux kernel 6.4 and Go 1.21rc2%0A  > 0a92922 windows: make TestSystemModuleVersions more tolerant%0A  > d1abdad unix/linux: update TUN flags and virtio_net_hdr constants%0A  > 2b751dd windows/svc/mgr: add Service.RecoveryActionsOnNonCrashFailures%0A  > e0c3b6e unix: add Mremap for linux%0A  > ca096e4 unix: add missing IFLA_* consts on linux%0A  > df9fef2 unix/linux: update to Linux kernel 6.3 and Go 1.20.5%0A  > 55b11dc unix: remove recently introduced debug/elf dependency%0A  > 5059a07 unix: implement Ptrace{Set,Get}Regs using PTRACE_{GET,SET}REGSET for Linux%0A  > 304f187 unix: replace use of strcpy in mkerrors.sh%0A  > 81c8a6c unix: add Getresuid and Getresgid for OpenBSD%0A  > ff98eae unix: remove absolute path of pwd from mkall.sh%0A  > b52f544 unix: add Getresuid, Getresgid for linux%0A  > b5c7a09 unix: update BPF constants with Linux kernel 6.2%0A  > c8ea6b0 windows: fix EnumProcesses to pass the correct array size%0A  > 352d833 cpu: add test for IsBigEndian%0A  > c43fe1e cpu: define IsBigEndian on wasm%0A  > 1911637 windows/svc: use separate (and more descriptive) service names in tests%0A  > ca59eda windows: use unsafe.Add instead of pointer arithmetic on a uintptr%0A  > 6c52899 windows: return error if DecomposeCommandLine parameter contains NUL%0A  > 9524d49 windows/svc/mgr: Service.Control: populate Status when returning certain errors%0A  > 2a33a30 execabs: let hasExec return false on wasip1%0A  > 39c2d6a unix: add UDP socket option constants on linux%0A  > 1fb6828 unix: convert Iovec.Base to *byte in mkpost.go on solaris%0A  > 3125361 unix: allow overriding GOOS using GOOS_TARGET in mkpost.go%0A  > dbd8f99 windows: add Service.ListDependentServices%0A  > f25ff60 windows: add JobObjectInformationClass consts for QueryInformationJobObject%0A  > 64840c1 unix: add bindings for setattrlist() on macOS%0A  > 90abad3 unix: add AT_EACCESS on Darwin%0A  > 94933fc windows: fix constant values for JobObjectInformationClass%0A  > 00d8004 unix: match ioctl req argument type to libc type%0A  > d0781cc unix: make solaris syscall tests less flaky%0A  > ff18efa unix: change Setrlimit/Prlimit to always call syscall functions%0A  > 494aa49 unix: skip ip related tests if EAFNOSUPPORT raised%0A  > c7a1bf9 unix: define PerfBitWriteBackward%0A  > 1470852 unix: add SetsockoptTCPMD5Sig on linux%0A  > a6bfb89 unix: use unsafe.Slice in anyToSockaddr%0A  > c10701f windows: use unsafe.Slice in (*RawSockaddrAny).Sockaddr on windows%0A  > 6f25076 unix: define extended TCPInfo on Linux%0A  > 10499f4 unix: add ioctlPtr with unsafe.Pointer arg on other unices (cont)%0A  > 92c4c39 unix: add Dup3 on FreeBSD%0A  > 748af6e unix: pass PROT_MPROTECT(PROT_READ|PROT_WRITE) to initial Mmap on netbsd%0A  > 972870e unix/linux: update to Linux kernel 6.2, glibc 2.37 and Go 1.20.1%0A  > cc0b67d unix: use C.ioctl in generated ioctlPtr%0A  > a3b23cc unix: use SYS_PTRACE in generated ptracePtr%0A  > 71a906e unix/linux: add TUN flags and virtio_net_hdr constants%0A  > 2977c77 unix: add ptracePtr that accepts pointer arg as unsafe.Pointer%0A  > 6877dcc execabs: don't override Go 1.19 error with our error%0A  > b13f40e unix: add ioctlPtr with unsafe.Pointer arg on other unices%0A  > 3b9b58b unix: Faccess: check CAP_DAC_OVERRIDE on Linux%0A  > 2da1413 cpu: get hwcap/auxv from the Go 1.21+ runtime%0A  > 4fee21c windows: Add WSALookupService syscall wrappers%0A  > c79a742 unix: fix a use-after-free bug in PtraceIO on freebsd%0Abumping golang.org/x/oauth2 e48dfd9...839de22:%0A  > 839de22 google: don't check for IsNotExist for well-known file%0A  > 0690208 go.mod: update golang.org/x dependencies%0A  > 451d5d6 internal: remove repeated definite articles%0A  > cfe200d oauth2: parse RFC 6749 error response%0A  > 3607514 go.mod: update golang.org/x dependencies%0A  > 4abfd87 google: add CredentialsParams.EarlyTokenRefresh%0A  > 1e7f329 oauth2: add ReuseTokenSourceWithExpiry%0A  > 86850e0 oauth2: fix typo%0A  > a6e37e7 google: Updating 3pi documentation%0A  > 54b70c8 google: update missing auth help URL%0A  > 2fc4ef5 README: encourage issues and proposals before changes%0A  > 62b4eed go.mod: update golang.org/x dependencies%0A  > 885f294 google: Add support for OAuth2 token exchange over mTLS%0A  > 6f9c1a1 google: use Credentials instead of deprecated DefaultCredentials%0A  > c82d0e1 google/internal/externalaccount: Removed URL validation for google URLs in ADC files%0A  > adbaf66 go.mod: update golang.org/x dependencies%0A  > e07593a oauth2: remove direct dependency on golang.org/x/net%0A  > 34ffb07 go.mod: update golang.org/x dependencies%0A  > b177c21 go.mod: update golang.org/x dependencies%0A  > 510acbc google/internal/externalaccount: Added check for aws region and security credential environment variables before aws metadata call%0A  > ec4a9b2 google/internal/externalaccount: Adding metadata verification%0A  > 68a41d6 go.mod: update golang.org/x dependencies%0A  > 1a77549 go.mod: update to new compute/metadata module%0Abumping golang.org/x/sync 8fcdb60...1ea3257:%0A  > 1ea3257 singleflight: make the check for exec support in TestPanicDoChan platform-agnostic%0Abumping golang.org/x/term d974fe8...edd9fb7:%0A  > edd9fb7 go.mod: update golang.org/x dependencies%0A  > 88fcf87 term: consistently return zeroes on GetSize error%0A  > f6de4a1 go.mod: update golang.org/x dependencies%0A  > 119f703 go.mod: update golang.org/x dependencies%0A  > 7ae6be6 go.mod: update golang.org/x dependencies%0A  > 0edf009 go.mod: update golang.org/x dependencies%0Abumping knative.dev/pkg dfad48e...5ef4812:%0A  > 5ef4812 Update community files (# 2762)%0A  > 49e2e56 update google cloud deps (# 2758)%0A  > a5e0b92 upgrade to latest dependencies (# 2757)%0A  > 6eb4b40 Update community files (# 2760)%0A  > eb63a40 Support to set qps and burst via env variable (# 2755)%0A  > 74c4be5 Generate kresource duck type codegen (# 2754)%0A  > 4dbc312 fix boilerplate (# 2753)%0A  > 15605c7 Defaulting Controller options for all kind of webhooks (# 2738)%0A  > 94b81fc Update community files (# 2752)%0A  > 5671699 drop the dynamic type (# 2750)%0A  > 9bda38b Fix some webhook testing tech debt (# 2751)%0A  > ec20442 Update community files (# 2747)%0A  > 05bfcf6 bump k8s dependencies and update min version to v1.25 (# 2745)%0A  > 52ff2ac drop dynamic client wrappers (# 2744)%0A  > a170a07 Eventing TLS: validate that Destination.CACerts is a PEM encoded cert (# 2743)%0A  > dfb4bf0 Drop dynamic wrapper injection code generation (# 2742)%0A  > db8a353 Add SinkCACerts to SourceStatus (# 2733)%0A  > 9049667 Update community files (# 2735)%0A  > aacec7f Update community files (# 2734)%0A  > 300df43 Eventing TLS: Added AddressableFromDestination method on the resolver (# 2717)%0Abumping google.golang.org/api a039966...63d06ab:%0A  > 63d06ab chore(main): release 0.124.0 (# 1990)%0A  > 73f57fe feat(all): auto-regenerate discovery clients (# 1991)%0A  > 8c0e6d9 chore: add yoshi-approver ownership (# 1994)%0A  > 7843046 chore(all): update all (# 1992)%0A  > 94c12ed chore(all): update module github.com/google/s2a-go to v0.1.4 (# 1989)%0A  > 0b4f4af feat(all): auto-regenerate discovery clients (# 1988)%0A  > 2721e1f chore: enable GoApiaryCodegen auto-approve (# 1987)%0A  > a241c25 chore: delete broken AutoApprove (# 1986)%0A  > 3e2d6a6 chore: trigger AutoApprove on reopen as well (# 1985)%0A  > a24a28a chore: give AutoApprove job full write (# 1984)%0A  > 8210800 chore(main): release 0.123.0 (# 1975)%0A  > f31b763 feat(all): auto-regenerate discovery clients (# 1982)%0A  > d27f40f feat(all): auto-regenerate discovery clients (# 1978)%0A  > 94d3d73 chore(ci): fix AutoApprove for discogen (# 1981)%0A  > 98b3073 feat(all): auto-regenerate discovery clients (# 1974)%0A  > d5e0fb2 chore(main): release 0.122.0 (# 1972)%0A  > ab64815 feat(all): auto-regenerate discovery clients (# 1973)%0A  > 8b0974e fix: add better support of array of floats (# 1971)%0A  > cf0df64 chore(main): release 0.121.0 (# 1962)%0A  > c2c2b59 feat(all): auto-regenerate discovery clients (# 1963)%0A  > e44a771 chore(all): update module github.com/google/s2a-go to v0.1.3 (# 1965)%0A  > 2068ba5 feat(all): auto-regenerate discovery clients (# 1961)%0A  > c2018e2 chore(main): release 0.120.0 (# 1956)%0A  > 4e35cac feat(all): auto-regenerate discovery clients (# 1960)%0A  > fcd007a feat(all): auto-regenerate discovery clients (# 1958)%0A  > 289b859 feat(all): auto-regenerate discovery clients (# 1957)%0A  > 409bc9d feat(all): auto-regenerate discovery clients (# 1955)%0A  > 0909f16 chore(main): release 0.119.0 (# 1944)%0A  > 2f54150 chore(deps): update s2a-go to v0.1.2 (# 1954)%0A  > 685ec81 feat: add an option to enable DirectPath xDS (# 1942)%0A  > d85769c feat(all): auto-regenerate discovery clients (# 1953)%0A  > 4cb8eb9 feat(all): auto-regenerate discovery clients (# 1952)%0A  > bf9f3ac chore(all): update google.golang.org/genproto digest to daa745c (# 1949)%0A  > e1eda57 feat(all): auto-regenerate discovery clients (# 1948)%0A  > a0dacd5 feat(all): auto-regenerate discovery clients (# 1947)%0A  > e8b93cb chore(deps): update s2a-go to v0.1.1 (# 1945)%0A  > 690068f feat(all): auto-regenerate discovery clients (# 1943)%0A  > 2d6890a chore(main): release 0.118.0 (# 1940)%0A  > 29dc45a feat(all): auto-regenerate discovery clients (# 1941)%0A  > ac94a0f feat(all): auto-regenerate discovery clients (# 1939)%0A  > 8019ef6 chore(main): release 0.117.0 (# 1931)%0A  > 750c7c8 feat(all): auto-regenerate discovery clients (# 1936)%0A  > 3a98290 chore(all): update all (# 1937)%0A  > 3f62830 chore(deps): bump golang.org/x/crypto (# 1930)%0A  > 2219681 feat(all): auto-regenerate discovery clients (# 1935)%0A  > 2efcb2e feat(all): auto-regenerate discovery clients (# 1932)%0A  > 3c61729 feat: add experimental s2a-go integration (# 1874)%0A  > 587b9e5 chore(main): release 0.116.0 (# 1929)%0A  > 28c8cd5 feat(all): auto-regenerate discovery clients (# 1928)%0A  > feafcdc chore(main): release 0.115.0 (# 1922)%0A  > 34781cf feat(all): auto-regenerate discovery clients (# 1927)%0A  > 33a2dfe feat(all): auto-regenerate discovery clients (# 1924)%0A  > 02cfb82 chore(all): update google.golang.org/genproto digest to dcfb400 (# 1925)%0A  > 8930f0e feat(all): auto-regenerate discovery clients (# 1923)%0A  > 1c955e8 feat(all): auto-regenerate discovery clients (# 1913)%0A  > 7f87838 chore(all): update all (# 1918)%0A  > be028cf chore(gensupport): add idempotency header (# 1916)%0A  > 649bfb9 chore(all): update all (# 1914)%0A  > 5ac4fd7 test: update test due to generator change (# 1912)%0A  > f79df48 chore(main): release 0.114.0 (# 1910)%0A  > 2754ab4 feat(all): auto-regenerate discovery clients (# 1907)%0A  > dc4b77d fix: always reference the internal package. (# 1909)%0A  > b8a2a5e chore(main): release 0.113.0 (# 1901)%0A  > fc221ce feat(all): auto-regenerate discovery clients (# 1900)%0A  > e63383f chore(all): update module google.golang.org/protobuf to v1.29.1 [SECURITY] (# 1906)%0A  > 64b6ee4 feat(idtoken): add support for external_account (# 1897)%0A  > 65cafd4 chore(all): update all (# 1902)%0A  > 63c48a6 feat(transport): add support for setting quota project with envvar (# 1892)%0A  > 225fa6b internal: Refactor cert logic to support OAuth2 token exchange over mTLS (# 1886)%0A  > 8d4d70d chore(main): release 0.112.0 (# 1883)%0A  > 89c274a feat(all): auto-regenerate discovery clients (# 1898)%0A  > 9f18671 feat(all): auto-regenerate discovery clients (# 1896)%0A  > e88ee8a feat(all): auto-regenerate discovery clients (# 1893)%0A  > 5da4d6a feat(all): auto-regenerate discovery clients (# 1887)%0A  > 6bd0840 chore(deps): bump golang.org/x/crypto in /internal/kokoro/discogen (# 1890)%0A  > 2f72016 chore(all): update all (# 1888)%0A  > c886360 feat(all): auto-regenerate discovery clients (# 1885)%0A  > 1aee5cd feat(all): auto-regenerate discovery clients (# 1884)%0A  > 15808d7 feat(all): auto-regenerate discovery clients (# 1882)%0A  > e99d0d5 chore(main): release 0.111.0 (# 1860)%0A  > 70d3954 feat(all): auto-regenerate discovery clients (# 1875)%0A  > f32872c chore(all): update google.golang.org/genproto digest to 637eb22 (# 1877)%0A  > c02cff6 feat(all): auto-regenerate discovery clients (# 1873)%0A  > 7d34d41 feat(all): auto-regenerate discovery clients (# 1872)%0A  > d456fd6 chore(deps): bump golang.org/x/net in /internal/kokoro/discogen (# 1870)%0A  > b7ab21d chore(all): update all (# 1868)%0A  > 7f5f40a feat(all): auto-regenerate discovery clients (# 1866)%0A  > 4056319 chore(all): update module golang.org/x/net to v0.7.0 [SECURITY] (# 1867)%0A  > 8b8b195 feat(all): auto-regenerate discovery clients (# 1863)%0A  > c0f2510 chore(all): update vet.sh to go runtime 1.20 (# 1865)%0A  > 895105a feat(all): auto-regenerate discovery clients (# 1861)%0A  > ba3414e feat(all): auto-regenerate discovery clients (# 1859)%0A  > 892811c chore(main): release 0.110.0 (# 1840)%0A  > 1edc79b chore: update x libs (# 1858)%0A  > 929a393 chore(all): update all (# 1853)%0A  > 1147cb8 fix: Update ECP dependency to v0.2.3 (# 1857)%0A  > 689f934 feat(all): auto-regenerate discovery clients (# 1851)%0A  > 8efd00d fix(internal/gensupport): don't prematurely close timers (# 1856)%0A  > 3fb5b61 fix: Improve error handling for enterprise certificate module (# 1848)%0A  > 8980266 feat(all): auto-regenerate discovery clients (# 1850)%0A  > 3fb8cdc feat(all): auto-regenerate discovery clients (# 1841)%0A  > 1651c38 chore(transport): remove support for go runtimes earlier than 1.16 (# 1844)%0A  > 4b4c9d4 feat(all): auto-regenerate discovery clients (# 1838)%0A  > b3b5f17 chore(main): release 0.109.0 (# 1818)%0A  > c13cc35 feat(all): auto-regenerate discovery clients (# 1836)%0A  > 602b6a4 chore(all): update all (major) (# 1806)%0A  > a5d0daa feat(all): auto-regenerate discovery clients (# 1828)%0A  > 50fc7c4 feat(all): auto-regenerate discovery clients (# 1826)%0A  > 6aad438 feat(all): auto-regenerate discovery clients (# 1825)%0A  > 85d0224 feat(all): auto-regenerate discovery clients (# 1822)%0A  > 884a246 feat(all): auto-regenerate discovery clients (# 1821)%0A  > 5935892 feat(all): auto-regenerate discovery clients (# 1819)%0A  > ba3ba78 feat(all): auto-regenerate discovery clients (# 1817)%0A  > 47f66d6 chore(main): release 0.108.0 (# 1811)%0A  > da48b9a feat(all): auto-regenerate discovery clients (# 1816)%0A  > a12685c feat(all): auto-regenerate discovery clients (# 1813)%0A  > 4df52d2 feat(all): auto-regenerate discovery clients (# 1810)%0A  > f74fbb6 chore(main): release 0.107.0 (# 1803)%0A  > d8084e4 feat(all): auto-regenerate discovery clients (# 1809)%0A  > 4dca4e0 feat: re-enable integrations:v1 (# 1801)%0A  > 86e4009 fix: user Timers over time.After (# 1802)%0A  > bcc345c feat(all): auto-regenerate discovery clients (# 1808)%0A  > de06921 feat(all): auto-regenerate discovery clients (# 1807)%0A  > 935ef64 feat(all): auto-regenerate discovery clients (# 1804)%0A  > 93de455 feat(all): auto-regenerate discovery clients (# 1800)%0A  > ac7eb8f chore(main): release 0.106.0 (# 1786)%0A  > 3944e86 feat(all): auto-regenerate discovery clients (# 1794)%0A  > f6dec99 feat(idtoken): add support for impersonated_service_account creds type (# 1792)%0A  > ddb5c65 test: add buffer to both sides of token expiry validation (# 1797)%0A  > b35900a fix(idtoken): configure validator constructor to use no authentication (# 1789)%0A  > ca86833 chore(all): update all (# 1796)%0A  > a6b0739 chore: skip generating integrations:v1 as it fails generation (# 1793)%0A  > 7bd17b3 feat(all): auto-regenerate discovery clients (# 1790)%0A  > 9fb35f5 feat(all): auto-regenerate discovery clients (# 1788)%0A  > 1569e5b feat(option/internaloption): add new EmbeddableAdapter option (# 1787)%0A  > a7f08e2 feat(all): auto-regenerate discovery clients (# 1784)%0A  > 67aaf4e chore(main): release 0.105.0 (# 1774)%0A  > 5b02761 feat(all): auto-regenerate discovery clients (# 1777)%0A  > c58bf4c feat: support set null map entries for non-simple map values (# 1782)%0A  > e4271df feat(googleapi): add response headers to Error reported by CheckMediaResponse (# 1781)%0A  > 6193507 chore: remove uses of obsolete golang.org/x/xerrors (# 1776)%0A  > 37a2e41 feat(all): auto-regenerate discovery clients (# 1773)%0A  > 9255b0b chore(main): release 0.104.0 (# 1748)%0A  > 4238314 chore: ignore some golang.org/x/* dependencies in renovate (# 1772)%0A  > 029b659 chore(all): update all (# 1768)%0A  > f819644 feat(all): auto-regenerate discovery clients (# 1771)%0A  > 2b596d9 feat(all): auto-regenerate discovery clients (# 1767)%0A  > 3195ce1 feat(all): auto-regenerate discovery clients (# 1766)%0A  > 97a9846 feat(all): auto-regenerate discovery clients (# 1760)%0A  > 8d8f0a7 feat(transport): de-experiment google-c2p resolver (# 1757)%0A  > c213153 fix(transport/grpc): separate resolution of creds and certs (# 1759)%0A  > 629e217 fix(idtoken): increase MaxIdleConnsPerHost to 100 in NewClient (# 1754)%0A  > caf7af0 feat(all): auto-regenerate discovery clients (# 1755)%0A  > e18b504 feat(all): auto-regenerate discovery clients (# 1753)%0A  > dd565a4 feat(all): auto-regenerate discovery clients (# 1752)%0A  > a657f19 feat(all): auto-regenerate discovery clients (# 1751)%0A  > 292129c feat(all): auto-regenerate discovery clients (# 1746)%0A  > 02077fd chore(all): update all (# 1749)%0A  > 567070f docs: document limitation of WithUserAgent (# 1747)%0A  > 561b601 chore(main): release 0.103.0 (# 1738)%0A  > 4248dc3 feat(all): auto-regenerate discovery clients (# 1743)%0A  > ee25e29 feat(googleapi): inject gax apierror.APIError into googleapi.Error (# 1730)%0A  > f8efb95 chore(all): update all (# 1740)%0A  > 9695aa1 feat: rm hard dep on x/sys (# 1742)%0A  > bec0f29 chore(.github): force renovate to use 1.19 (# 1741)%0A  > bbd4259 feat(all): auto-regenerate discovery clients (# 1739)%0A  > de99200 feat(all): auto-regenerate discovery clients (# 1737)%0A  > 0d7f97a chore(main): release 0.102.0 (# 1726)%0A  > 0528475 feat: rely on new compute metadata module directly (# 1736)%0A  > ce57a67 feat(all): auto-regenerate discovery clients (# 1734)%0A  > 1e1eab9 feat(all): auto-regenerate discovery clients (# 1727)%0A  > 0ce5403 test(transport/grpc): fix arg for test failure logs (# 1733)%0A  > 06360d8 feat(all): auto-regenerate discovery clients (# 1725)%0A  > 644a13c chore(main): release 0.101.0 (# 1719)%0A  > f4788b3 feat(all): auto-regenerate discovery clients (# 1723)%0A  > 9ea2ceb chore(all): update all (# 1721)%0A  > 9140608 feat(all): auto-regenerate discovery clients (# 1720)%0A  > 453b81a feat(all): auto-regenerate discovery clients (# 1718)%0A  > d530a93 chore(main): release 0.100.0 (# 1714)%0A  > 37f90e9 feat(internal/gensupport): remove DetermineContentType, use gax-go copy (# 1716)%0A  > b235b1f fix(idtoken): Allow missing age in http response header (# 1715)%0A  > f990a2a feat(all): auto-regenerate discovery clients (# 1717)%0A  > f9e15f2 feat(all): auto-regenerate discovery clients (# 1712)%0A  > e74b770 chore(all): update all (# 1713)%0A  > 977e871 chore(main): release 0.99.0 (# 1710)%0A  > 6b81c83 feat(all): auto-regenerate discovery clients (# 1701)%0A  > 1aa1deb chore(all): update all (# 1707)%0A  > 69fb474 chore: Update ECP dependency to 0.2.0 (# 1704)%0A  > a4ae94d chore(main): release 0.98.0 (# 1700)%0A  > 25b7450 feat(all): auto-regenerate discovery clients (# 1699)%0A  > aa775b4 feat(all): auto-regenerate discovery clients (# 1696)%0A  > faa845a chore(main): release 0.97.0 (# 1694)%0A  > 2c3e863 fix(gensupport): allow initial request for resumable uploads to retry w/ non-nil getBody (# 1690)%0A  > f427ee3 feat(internal/gensupport): wrap retry failures with context and prev error (# 1684)%0A  > 6b0515b fix: build script bash error (# 1697)%0A  > b8f2556 feat(all): auto-regenerate discovery clients (# 1695)%0A  > a87400b feat(all): auto-regenerate discovery clients (# 1693)%0Abumping google.golang.org/protobuf 6875c3d...68463f0:%0A  > 68463f0 all: release v1.31.0%0A  > 59a8581 encoding/protodelim: fix handling of io.EOF%0A  > fc47fdd proto: store the size of tag to avoid multiple calculations%0A  > cc524c9 internal/order: fix sorting of synthetic oneofs to be deterministic%0A  > b8fc770 encoding/protodelim: If UnmarshalFrom gets a bufio.Reader, try to reuse its buffer instead of creating a new one%0A  > cf06b0c compiler/protogen: add Semantic.SET to setter annotations%0A  > 05cbe34 encoding: add MarshalAppend to protojson and prototext%0A  > 1bca6d9 types/dynamicpb: add NewTypes%0A  > 736947c all: update protobuf release version to fix macOS tests%0A  > 808c664 all: start v1.30.0-devel%0A  > f221882 all: release v1.30.0%0A  > e344383 protoadapt: helper functions to convert v1 or v2 message to either v1 or v2 message.%0A  > 32efccd all: start v1.29.1-devel%0A  > 771d8c7 all: release v1.29.1%0A  > edaf511 internal/encoding/text: fix parsing of incomplete numbers%0A  > fe5bc54 all: start v1.29.0-devel%0A  > d3c9826 all: release v1.29.0%0A  > eba8b09 cmd/protoc-gen-go: support protobuf retention feature%0A  > fcf5f6c encoding/prototext: allow whitespace and comments between minus sign and number in negative numeric literal%0A  > bc1253a types/descriptorpb: regenerate using latest protobuf v22.0 release%0A  > 246af0d internal,reflect: correct typos%0A  > 49eaa78 all: update links to Protocol Buffer documentation%0A  > e831c33 proto: document Equal behavior of invalid messages%0A  > 358fe40 internal/strs: avoid unnecessary allocations in Builder%0A  > 0430d69 internal/impl: remove the unreachable line of code%0A  > a948118 cmd/protoc-gen-go: make deprecated messages more descriptive%0A  > 31a5920 protobuf: remove the check for reserved field numbers.%0A  > a8d446d types/known/structpb: preallocate map in AsMap%0A  > b2a7dfe reflect/protoreflect: add Value.Equal method%0A  > f0e23c7 proto: revert expose package-private equalField%0A  > 4d6d213 proto: expose package-private equalField.%0A  > 7a48e2b protoreflect: fix list example code%0A  > 494e81b integration test: drop Go 1.11 and Go 1.12%0A  > f930b1d encoding/protojson: fix parsing of google.protobuf.Timestamp%0A  > 692f4a2 types/descriptorpb: update *.pb.go to use latest protoc release, 21.5%0A  > fb0abd9 encoding: add protodelim package%0A  > 0f85348 all: start v1.28.1-devel%0Abumping golang.org/x/text 71a9c9a...e503480:%0A  > e503480 encoding/japanese, language: shorten very long sub-test names%0A  > 2df65d7 all: regenerate for Unicode 15.0.0%0A  > e3c038a all: prepare for Unicode 15.0.0%0A  > 3a7a255 internal/export/idna: make more space for mapping index%0A  > d61dd50 go.mod: delete repeated "indirect"%0A  > efb744f internal/export/idna: fix infinite loop in Go pre-1.10%0A  > 48e4a4a all: fix some comments%0A  > 9db913a go.mod: update to newer x/tools%0A  > 30dadde all: correct comment typos%0Abumping k8s.io/client-go 7226b15...6e9dabb:%0A  > 6e9dabb Update dependencies to v0.26.5 tag%0A  > 038b381 Merge pull request # 117691 from dims/re-do-of-117242-on-release-1.26%0A  > cd83e43 Bump runc go module v1.1.4 -> v1.1.6%0A  > dbfbc03 Merge pull request # 117686 from ardaguclu/automated-cherry-pick-of-# 117495-upstream-release-1.26%0A  > d72dec4 Use absolute path instead requestURI in openapiv3 discovery%0A  > a5144d4 Merge pull request # 117638 from seans3/automated-cherry-pick-of-# 117571-origin-release-1.26%0A  > d6f8d04 Refactors discovery content-type and helper functions%0A  > 2dd0093 Merge pull request # 115899 from odinuge/automated-cherry-pick-of-# 115620-upstream-release-1.26%0A  > f3ae5cb Merge pull request # 116666 from seans3/automated-cherry-pick-of-# 116603-origin-release-1.26%0A  > fffc68d Change where transformers are called.%0A  > 5ebee18 Aggregated discovery resilient to nil GVK%0A  > 8190aa4 client-go/cache: update Replace comment to be more clear%0A  > 87720b3 Merge pull request # 116437 from seans3/automated-cherry-pick-of-# 116145-# 115865-origin-release-1.26%0A  > b667227 client-go/cache: rewrite Replace to check queue first%0A  > fc13749 Removes old discovery hack ignoring 403 and 404%0A  > 30215cd client-go/cache: merge ReplaceMakesDeletionsForObjectsInQueue tests%0A  > f39ba12 Plumb stale GroupVersions through aggregated discovery%0A  > ba35969 client-go/cache: fix missing delete event on replace without knownObjects%0A  > f538edf Merge pull request # 116352 from seans3/automated-cherry-pick-of-# 115978-origin-release-1.26%0A  > 97cf9cb client-go/cache: fix missing delete event on replace%0A  > 5dbbc58 Tolerate empty discovery response in memcache client%0A  > 62133a9 Merge pull request # 115787 from liggitt/net-0.7.0-1.26%0A  > 8ce239f Update golang.org/x/net to v0.7.0%0A  > e6bc0bc Merge pull request # 115566 from enj/automated-cherry-pick-of-# 115315-upstream-release-1.26%0A  > 9112e19 Merge pull request # 115400 from pohly/automated-cherry-pick-of-# 115354-origin-release-1.26%0A  > 0519b53 kubelet/client: collapse transport wiring onto standard approach%0A  > 2e34348 Merge pull request # 115642 from nckturner/pin-golang.org/x/net-to-v0.4.0-in-1.26%0A  > 7be38cd dynamic resource allocation: avoid apiserver complaint about list content%0A  > 4968c4a Pin golang.org/x/net to v0.4.0 in 1.26%0A  > 0c34939 Merge pull request # 114617 from JoelSpeed/automated-cherry-pick-of-# 114585-upstream-release-1.26%0A  > 04b098b Resource claims should be a map type%0A  > b3fff46 Merge pull request # 114415 from hoskeri/automated-cherry-pick-of-# 114404-upstream-release-1.26%0A  > 236db3c Merge pull request # 113988 from liggitt/automated-cherry-pick-of-# 113933-upstream-release-1.26%0A  > a2ef324 Check the correct error in d.downloadAPIs%0A  > 95a14c3 Merge remote-tracking branch 'origin/master' into release-1.26%0A  > ebb499f Limit request retrying to []byte request bodies%0A  > 1a7cd1d Update golang.org/x/net 1e63c2f%0A  > 53f2fea sync: update go.mod%0A  > 968ba8d Merge pull request # 113797 from seans3/force-no-aggregated%0A  > c8ffed3 Merge pull request # 111023 from pohly/dynamic-resource-allocation%0A  > 3ac73ea Adds bool to force non-aggregated discovery%0A  > 61cd728 Merge pull request # 113826 from jsafrane/add-openstack%0A  > 522eaa1 api: generated files%0A  > cfd682c Merge pull request # 113375 from atiratree/PodHealthyPolicy-api%0A  > f2b10f3 Remove OpenStack cloud provider%0A  > acc9fa7 Merge pull request # 113186 from ttakahashi21/KEP-3294%0A  > f1c80d7 generated%0A  > a3d3eb0 Revert "Remove references to openstack and cinder"%0A  > c7bdab2 Generate code%0A  > 0a1f6a8 Merge pull request # 112744 from pwschuurman/statefulset-slice-impl%0A  > 1c7a870 Merge pull request # 113485 from MikeSpreitzer/apf-borrowing%0A  > eed2516 Adding implementation of KEP-3335, StatefulSetSlice%0A  > 7280270 Merge pull request # 113599 from seans3/discovery-client-update%0A  > d4a3675 apiserver: add generated files for borrowing in flowcontrol%0A  > 7694435 Update redacting functionality to redact all sensitive info in config when printing with view (# 109189)%0A  > 25d5761 Aggregated discovery client%0A  > 4b1a9fd Merge pull request # 113314 from cici37/celIntegration%0A  > ea9ec91 Merge pull request # 112905 from alexzielenski/kubectl-apply-csa-migration%0A  > 3a430a4 API - make update%0A  > 3daf180 Merge pull request # 113688 from dashpole/update_utils%0A  > 898b7a3 add FindFieldsOwners util function%0A  > dbe034b update k8s.io/utils to fix util tracing panic%0A  > 4f63b62 add UpgradeManagedFieldsPatch%0A  > 7ed3193 Merge pull request # 111545 from jlsong01/rewrite_signature_of_StartEventWatcher%0A  > c8c6cb5 add OWNERS to csaupgrade%0A  > cbe28cf Merge pull request # 113274 from Huang-Wei/kep-3521-A%0A  > 3467961 rewrite signature of function StartEventWatcher%0A  > a45874a remove kubectl annotation logic from upgrade patch%0A  > 2248bf3 Automated codegen%0A  > d576a35 Merge pull request # 113387 from wojtek-t/refactor_client_indexing%0A  > 4fbef5b Merge pull request # 106242 from thockin/revive-copy-lb-status-type-to-ingress%0A  > 5e7ba1f Minor cleanup of thread safe store%0A  > bc6266d Merge pull request # 103177 from arkbriar/support_cancelable_exec_stream%0A  > 3f162fe Copy LoadBalancerStatus from core to networking%0A  > b69a16c Refactor store index into its structure%0A  > 19b2e89 Merge pull request # 113523 from seans3/content-type-response%0A  > 0563dec Propagate the panic with a channel%0A  > 8ff4970 Get response content-type%0A  > 2362c7b use subtests and defer in TestSPDYExecutorStream%0A  > 0d57396 Merge pull request # 113304 from mimowo/handling-pod-failures-beta-ssa%0A  > 5e0a531 Support cancelable SPDY executor stream%0A  > a232cf0 Merge pull request # 113367 from pohly/dep-ginkgo-gomega%0A  > a191e58 SSA to add pod failure conditions - ready for review%0A  > 984bdbf dependencies: update to gomega v1.23.0 and ginkgo v2.4.0 and dependencies%0A  > f87d047 Merge pull request # 112693 from aimuz/fix-GO-2022-0969%0A  > d236783 Fixed (CVE-2022-27664) Bump golang.org/x/net to v0.1.1-0.20221027164007-c63010009c80%0A  > ef8a2e5 Merge pull request # 113089 from zackzhangkai/fix-doc%0A  > 197e479 Merge pull request # 108959 from astraw99/fix-duplicate-list%0A  > 0945beb fix typo%0A  > 42a0e1c Merge pull request # 113062 from alexzielenski/client-go-json-output%0A  > f549acf Fix duplicate code block of ListAll function%0A  > b6d3c8d Merge pull request # 107278 from harsimranmaan/allow_pagination_in_dynamic_fake_lister%0A  > 624929c address feedback%0A  > 9cc33a4 Merge pull request # 113106 from pohly/dep-ginkgo-gomega%0A  > 0c269b7 remove selflink as per review feedback%0A  > 12cafe2 refactor to use Schema(contentType)%0A  > 9b51067 dependencies: update to gomega v1.22.1 and ginkgo v2.3.1%0A  > fbd8e9a fix failing test assertions%0A  > 8b6ceae add more options for fetching openapiv3 in clients%0A  > fa9ed7f Merge pull request # 112860 from nckturner/remove-log-line%0A  > 1f10368 Preserve metadata for fake dynamic client unstructured lists%0A  > 6b24912 Merge pull request # 112988 from alexzielenski/update-kube-openapi%0A  > 5870c62 Remove log line from expiration cache%0A  > aea20dd Merge pull request # 113037 from pacoxu/fsnotify-v1.6.0%0A  > e3bb48f update kube-openapi%0A  > 1af3711 update fsnotify to v1.6.0%0A  > e6d958c Merge pull request # 112989 from ameukam/bump-golang.org/x/text-to-v0.3.8%0A  > 5e469ba Bump golang.org/x/text to v0.3.8%0A  > f515a4c Merge pull request # 112774 from stevekuznetsov/skuznets/dynamic-client-similar%0A  > b28f6c9 Merge pull request # 112875 from pohly/update-yaml%0A  > 34e8a5d client-go: factor the dynamic client similarly to others%0A  > c9afc73 dependencies: update to sigs.k8s.io/yaml v1.3.0%0A  > f24bd69 Merge pull request # 112306 from tkashem/v1beta3%0A  > ebc7cd4 Merge pull request # 112707 from enj/enj/i/https_links%0A  > 9b97b72 rename assuredConcurrencyShares for flowcontrol v1beta3%0A  > 2f43d37 Merge pull request # 112705 from stevekuznetsov/skuznets/fix-comment%0A  > 1665808 Use https links for k8s KEPs, issues, PRs, etc%0A  > 9bac803 apiserver: generate for apf v1beta3%0A  > 3697342 Merge pull request # 112680 from enj/enj/i/tls_cache_key_comparable%0A  > 956c1ce clients: clarify a misleading comment%0A  > c81636c Merge pull request # 112665 from NoicFank/fix-typo%0A  > cc2441c transport/cache: statically assert that tlsCacheKey is comparable%0A  > be20b2b Merge pull request # 112673 from dims/update-to-latest-k8s.io/utils-sep-22%0A  > 59765b8 fix typo error%0A  > 04dbcd8 Update to latest k8s.io/utils to pick up changes%0A  > 2fd4aac Merge pull request # 112613 from dims/update-github.com/go-openapi/jsonreference-to-drop-github.com/PuerkitoBio/purell%0A  > 47ad72a update github.com/go-openapi/jsonreference to drop github.com/PuerkitoBio/purell%0A  > f7c9c63 Merge pull request # 112545 from dims/update-etcd-3.5.5-and-all-otel-related-to-latest%0A  > b6e72dc Merge pull request # 112226 from aojea/client_go_transport%0A  > 6b5ecad updated etcd to v3.5.5 and newer otel libraries as well%0A  > acfaa39 Merge pull request # 112352 from pohly/e2e-ginkgo-progress%0A  > 1bd914a client-go: test transport generation is goroutine safe%0A  > 037b5fd Merge pull request # 112514 from markmc/patch-1%0A  > ec6c80a e2e: bump ginkgo to v2.2.0%0A  > 3f66212 client-go: remove reference to TPR in examples%0A  > 86ffa32 Merge pull request # 112475 from vatsalparekh/fix-TestRESTClientLimiter%0A  > ece6462 Merge pull request # 112476 from enj/enj/i/list_pager_flake%0A  > bf2b395 Fix Infelicities in TestRESTClientLimiter%0A  > 58155b7 Merge pull request # 112450 from enj/enj/i/exec_tls_cache_holder_cleanup%0A  > 6703098 Check for context cancellation on each buffered chunk%0A  > eecd3e5 Merge pull request # 112091 from xyz-li/master%0A  > 5dab9a0 client-go/transport: drop Dial and GetCert fields in favor of Holders%0A  > f6b8521 Merge pull request # 111333 from flant/selfsubjectattributesreviews%0A  > cc3cc93 kubectl: fix memory leaks in port forwarding client%0A  > b2b55e6 Add auth API to get self subject attributes%0A  > 18c3338 Merge pull request # 112200 from pohly/client-go-shared-informer-factory-shutdown%0A  > 9dae691 Merge pull request # 112309 from shyamjvs/disable-compression%0A  > ec4fedd client-go: support waiting for SharedInformerFactory shutdown%0A  > ab826d2 Merge pull request # 112349 from pohly/klog-update%0A  > 49ac40b Autogen code%0A  > ab0bfda build: update to klog v2.80.1%0A  > b8a8d94 Add DisableCompression option to KubeConfig%0A  > f32861c Merge pull request # 112341 from enj/enj/i/second_time_is_the_charm%0A  > 7d208ba Remove in-tree credential plugins (again)%0A  > e003fa9 Merge pull request # 112017 from enj/enj/i/exec_tls_cache%0A  > 2698e82 Merge pull request # 111967 from alexzielenski/csa-to-ssa%0A  > 6a008ec exec auth: support TLS config caching%0A  > 27c67e7 Merge pull request # 111122 from alexzielenski/informer%0A  > 00d892f correct spacing%0A  > d28c736 Merge pull request # 112022 from JackZxj/release-lock%0A  > a300ae0 return when test is done%0A  > 2efbeaf add boilerplate%0A  > b8b6206 Merge pull request # 112199 from pohly/klog-update%0A  > d04c2ce update lock getter of leaderelection%0A  > 93e5e0e hold listener lock while waiting for goroutines to finish%0A  > dac0826 remove inaccurate comment%0A  > 5a2c3e9 dependencies: update to klog v2.80.0%0A  > e11a988 simplify control flow%0A  > 7634f2e make upgrade modify input instead of deep copying%0A  > 7ccf7b0 Merge pull request # 112134 from apelisse/client-go-valid-segment%0A  > ac7f657 fix spelling%0A  > 9aa7c11 remove fieldsv1 from upgrade body%0A  > d83ec9e Merge pull request # 112129 from pohly/e2e-ginkgo-report-after-each%0A  > a4b84d8 Validate segments with client-go/dynamic%0A  > 0f4a6cf reset listenersStarted%0A  > 703d15e Update staging/src/k8s.io/client-go/util/csaupgrade/upgrade.go%0A  > cac10a8 dependencies: update to ginkgo v2.1.6 and gomega v1.20.1%0A  > 449817f add multithreaded test to shared informer%0A  > 675ca93 refactor if statement%0A  > 46d4284 Merge pull request # 111241 from Abirdcfly/fixtestorsource%0A  > de0b767 remove duplicate test%0A  > cfaca90 address comments%0A  > bdae576 Merge pull request # 112068 from aojea/aojea_client_go%0A  > 9b300de make TestListPager_EachListItem rework%0A  > 0565962 address review comments%0A  > 089614c remove last applied configuration information%0A  > fd22687 add aojea as client-go reviewer%0A  > 5a25eb0 switch listeners to use a map, adapt tests%0A  > efe3789 add more test cases%0A  > 35ead05 Merge pull request # 112052 from tosi3k/bump-client-golang%0A  > 90c6a46 active remove/add tests for event handlers%0A  > 46dc22f clean up test%0A  > 5291ca2 Bump prometheus/client_golang to v1.13.0%0A  > de4dd3a tests for invalid registration removals%0A  > ced85a8 update godoc%0A  > e6538dd Merge pull request # 112024 from cndoit18/remove-redundant-judgment%0A  > 33eff64 apply desired changes for handler registration%0A  > 049ba69 expose FieldsToSet and SetToFields%0A  > bcd2e6c style: remove redundant judgment%0A  > d73e40f rename handle to registration%0A  > aa892ab remove  unused code%0A  > d5e5863 Merge pull request # 111752 from aanm/revert-final-url-template%0A  > b3a61c6 remove informational informer methods again%0A  > 90ef078 dont expose internal methods in implementatoin%0A  > 5feaced Merge pull request # 67782 from dims/yank-in-tree-openstack-cloud-provider%0A  > e9d4627 client-go/rest: check if url is nil to prevent nil pointer dereference%0A  > ecdc8bf support removal of event handlers from SharedIndexInformers%0A  > c364b63 add function to upgrade managedfields CSA to SSA%0A  > 0fdc4f3 Merge pull request # 111684 from 0xff-dev/master1%0A  > 98e81a7 Remove references to openstack and cinder%0A  > c501ee0 Revert "client-go: remove no longer used finalURLTemplate"%0A  > 4faffa8 Merge pull request # 111564 from inosato/remove-ioutil-from-cli-client-go%0A  > c94a539 use constant NamespaceDefault instead of variable namespace%0A  > 2e40408 Merge pull request # 111918 from liggitt/in-tree-auth%0A  > 27de641 Remove ioutil from client-go%0Abumping knative.dev/networking e5d04e8...b2cce92:%0A  > b2cce92 Update community files (# 823)%0A  > 1431d70 Bump google.golang.org/grpc to the latest version (# 821)%0A  > 91821ae Update community files (# 819)%0A  > 3a75df5 upgrade to latest dependencies (# 817)%0A  > b9dd5c2 upgrade to latest dependencies (# 816)%0A  > 68947c5 upgrade to latest dependencies (# 815)%0A  > 14a2bd4 Move `pkg/certificates` from `control-protocol` to `networking` (# 802)%0A  > 2daa483 Update community files (# 813)%0A  > 0dbe4f9 upgrade to latest dependencies (# 812)%0A  > 2a2f7d2 upgrade to latest dependencies (# 810)%0A  > fcbedad Update community files (# 809)%0A  > a44b093 upgrade to latest dependencies (# 808)%0A  > 7c2f7ac upgrade to latest dependencies (# 807)%0A  > 33636d9 Backward compatibility for InternalEncryption (# 806)%0A  > 77975a1 Add the new certificate names for dataplane and controlplane (# 804)%0A  > c3cca43 upgrade to latest dependencies (# 803)%0A  > 3f4627e Add internal trust flag to config (# 778)%0A  > 02055c8 Update community files (# 801)%0A  > 68725bd upgrade to latest dependencies (# 798)%0A  > 1594abb Update community files (# 797)%0Abumping google.golang.org/grpc 1c29e07...5b67e5e:%0A  > 5b67e5e Update version.go to v1.56.1 (# 6386)%0A  > d0f5150 client: handle empty address lists correctly in addrConn.updateAddrs (# 6354) (# 6385)%0A  > 997c1ea Change version to 1.56.1-dev (# 6345)%0A  > 2b6ff72 Change version to 1.56.0 (# 6344)%0A  > 7996425 xds/outlierdetection: fix config handling (# 6361) (# 6367)%0A  > a5ae5c6 weightedroundrobin: cherry-pick 2 commits from master (# 6360)%0A  > 8edfa1a authz: End2End test for AuditLogger (# 6304)%0A  > 2b1d70b xds: enable RLS in xDS by default (# 6343)%0A  > 47f8ed8 interop: Don't fail target if sub-target already failed (# 6332)%0A  > 1f23f6c client: fix Connect to handle channel idleness properly (# 6331)%0A  > 3ea58ce client: disable channel idleness by default (# 6328)%0A  > 6c2529b xds: support pick_first custom load balancing policy (A62) (# 6314)%0A  > 9b9b364 internal/envconfig: Set Custom LB Env Var to true by default (# 6317)%0A  > e325737 alts: Fix flaky ALTS TestFullHandshake test. (# 6300)%0A  > 4d3f221 xds/internal/xdsclient: Add support for String Matcher Header Matcher in RDS (# 6313)%0A  > 157db19 stats/opencensus: Fix flaky test span (# 6296)%0A  > f19266c xds: support built-in Stdout audit logger type (# 6298)%0A  > 59134c3 client: add support for pickfirst address shuffling from gRFC A62 (# 6311)%0A  > a6e1acf grpc: support sticky TF in pick_first LB policy (# 6306)%0A  > 2ae10b2 xdsclient: remove interface check related to ResourceData (# 6308)%0A  > e9799e7 client: support a 1:1 mapping with acbws and addrConns (# 6302)%0A  > 2a266e7 authz: use pointer to to structpb.Struct instead of value (# 6307)%0A  > 511a963 interop: let the interop client send additional metadata, controlled by a flag (# 6295)%0A  > 9b7a947 grpc: support channel idleness (# 6263)%0A  > 098b2d0 xds/internal/balancer/outlierdetection: Switch Outlier Detection to use new duration field (# 6286)%0A  > 417d4b6 examples: add error_handling example; move errors to error_details (# 6293)%0A  > 390c392 authz: Rbac engine audit logging (# 6225)%0A  > 52fef6d authz: Stdout logger (# 6230)%0A  > 92e65c8 test/kokoro: Add custom_lb_test to the xds_k8s_lb job (# 6290)%0A  > 756119c  xds/outlierdetection: forward metadata from child picker (# 6287)%0A  > 8eba9c2 github: upgrade to v3 of checkout & setup-go (# 6280)%0A  > 24fd252 proto: update generated code to match grpc-proto changes (# 6283)%0A  > 4eb88d7 cleanup: use new Duration type in base ServiceConfig (# 6284)%0A  > 1230f0e xds/internal/xdsclient: Split registry up and two separate packages (# 6278)%0A  > 0bdae48 interop: fix interop_test.sh shutdown (# 6279)%0A  > 5dcfb37 interop: hold lock on server for OOB metrics updates; share 30s timeout (# 6277)%0A  > 68381e7 xds: WRR in xDS (# 6272)%0A  > fd376a5 test: fix flaky TimeoutOnDeadServer test; some cleanups (# 6276)%0A  > 1db474c weightedroundrobin: fix duration format in lb config (# 6271)%0A  > 523dcdd weightedroundrobin: fix test race accessing timeNow (# 6269)%0A  > 1536887 interop/xds: Add Custom LB needed for interop test (# 6262)%0A  > 7d61344 examples: fix authz example to receive streaming error properly (# 6270)%0A  > afcbdc9 xds/internal/xdsclient/xdslbregistry: Continue in converter if type not found (# 6268)%0A  > b3fbd87 interop: add ORCA test cases and functionality (# 6266)%0A  > 5e58734 xds: Add support for Custom LB Policies (# 6224)%0A  > 5c4bee5 balancer/weightedroundrobin: add load balancing policy (A58) (# 6241)%0A  > c44f77e grpc: use CallbackSerializer in balancer wrapper (# 6254)%0A  > f193ec0 orca: fix race when calling listeners coincides with updating the run goroutine (# 6258)%0A  > 417cf84 test: deflake TestBalancerProducerHonorsContext (# 6257)%0A  > 1f3fe1c Update ClientStream.SendMsg doc (# 6247)%0A  > ccad7b7 grpc: use CallbackSerializer in resolver_wrapper (# 6234)%0A  > 47b3c55 orca: fix race at producer startup (# 6245)%0A  > 56b33d5 server/transport: send appropriate debug_data in GOAWAY frames (# 6220)%0A  > add9015 orca: allow a ServerMetricsProvider to be passed to the ORCA service and ServerOption (# 6223)%0A  > 40d0147 googledirectpatph: enable ignore_resource_deletion in bootstrap (# 6243)%0A  > ed3ceba balancer: make producer RPCs block until the SubConn is READY (# 6236)%0A  > b153b00 multiple: standardize import renaming for typed structs (# 6238)%0A  > 713bd04 orca: minor cleanups (# 6239)%0A  > 21a339c grpc: handle RemoveSubConn inline in balancerWrapper (# 6228)%0A  > b153827 xds: make glaze happy for test packages (# 6237)%0A  > 019acf2 stubserver: add option for allowing more services to be registered (# 6240)%0A  > cf89a0b authz: Swap to using the correct TypedConfig in audit logger parsing (# 6235)%0A  > df82147 internal: Document gcp/observability 1.0 dependencies in /internal (# 6229)%0A  > da1a5eb tests: nix TestClientDoesntDeadlockWhileWritingErroneousLargeMessages (# 6227)%0A  > e853dbf authz: add conversion of json to RBAC Audit Logging config (# 6192)%0A  > 497436c xds/internal/balancer/outlierdetection: Change string to String (# 6222)%0A  > de11139 clusterresolver: improve tests (# 6188)%0A  > eff0942 xds/internal/xdsclient: Custom LB xDS Client Changes (# 6165)%0A  > 8628e07 xds/internal/balancer/outlierdetection: Add Channelz Logger to Outlier Detection LB (# 6145)%0A  > 83c460b authz: Move audit package (# 6218)%0A  > 8c70261 grpc: ClientConn cleanup in prep for channel idleness (# 6189)%0A  > 2cd95c7 gcp/observability: remove redundant import (# 6215)%0A  > 16651f6 go.mod: update all dependencies (# 6214)%0A  > ca60462 stubserver: Stop server when StartClient failed (# 6190)%0A  > 7dfd718 internal/buffer: add Close method to the Unbounded buffer type (# 6161)%0A  > ebeda75 tests: defalke TestTimerAndWatchStateOnSendCallback (# 6206)%0A  > 0ed709c Change version to 1.56.0-dev (# 6213)%0A  > 875c97a examples/features/observability: use observability module v1.0.0 (# 6210)%0A  > aa8c137 authz: add audit logging APIs (# 6158)%0A  > b91b884 gcp/observability: Have o11y module point to grpc 1.54 and opencensus 1.0.0 (# 6209)%0A  > eab9e20 test/kokoro: increase PSM Security test timeout to 4h (# 6193)%0A  > d90621f remove the unnecessary call to ResetTimer and StopTimer (# 6185)%0A  > fe72db9 testing: add helpers to start test service, and retrieve port (# 6187)%0A  > 5a50b97 Revert "Revert "credentials/alts: defer ALTS stream creation until handshake …" (# 6179)%0A  > 89ec960 grpc: read the service config channel once instead of twice (# 6186)%0A  > 6237dfe internal/stubserver: Close Client Conn in error handling of Start (# 6174)%0A  > 06de8f8 alts: Add retry loop when making RPC in ALTS's TestFullHandshake. (# 6183)%0A  > 6eabd7e server: use least-requests loadbalancer for workers (# 6004)%0A  > 8374ff8 Export the unwrapResource method, to allow callers outside of the package (# 6181)%0A  > efb2f45 test/xds: Fix test_grpc import path (# 6180)%0A  > 81b3092 security/advancedtls: add TlsVersionOption to select desired min/max TLS versions (# 6007)%0A  > 17b693d alts: Perform full handshake in ALTS tests. (# 6177)%0A  > 01f8b86 Add documentation on some anti-patterns (# 6034)%0A  > 3489bb7 xdsclient/test: deflake TestWatchResourceTimerCanRestartOnIgnoredADSRecvError (# 6159)%0A  > bfb57b8 testing: delete internal copy of test service proto, and use canonical one (# 6164)%0A  > 10401b9 stats/opencensus: the backend to Sent. Attempt. and Recv. (# 6173)%0A  > b0a8b1b Use string instead of enum for xds resource type (# 6163)%0A  > 1d5b73a xds: add stop to avoid hanging in TestServeWithStop (# 6172)%0A  > ea0a038 xds/xdsclient: ignore resource deletion as per gRFC A53 (# 6035)%0A  > a51779d xdsclient/test: deflake TestTimerAndWatchStateOnSendCallback (# 6169)%0A  > e979919 internal/grpcsync: move CallbackSerializer from xdsclient/internal to here (# 6153)%0A  > c2899dd examples/features/observability: Point o11y example to latest gcp/observability module (# 6162)%0A  > 113d75f gcp/observability: Add isSampled bool to log entries (# 6160)%0A  > 4a12595 stats/opencensus: Switch helper to return Span Context from context (# 6156)%0A  > c3f1d5e gcp/observability: Set the opencensus_task label only for metrics, not tracing and logging (# 6155)%0A  > 42dd7ac Use anypb.New instead of ptypes.MarshalAny (# 6074)%0A  > 415ccdf go.mod: update all dependencies after 1.54 branch cut (# 6132)%0A  > a357baf status: FromError: return entire error message text for wrapped errors (# 6150)%0A  > 44cebb8 xds: enable XDS federation by default (# 6151)%0A  > c018273 examples: Add observability example (# 6149)%0A  > 277bb64 Revert "credentials/alts: defer ALTS stream creation until handshake time (# 6077)" (# 6148)%0A  > 0fdfd40 gcp/observability: Generate unique process identifier unconditionally (# 6144)%0A  > 1d20f1b security/advancedtls: swap from deprecated pkix.CertificateList to x509.RevocationList (# 6054)%0A  > a8a25ce transport: use prefix logging (# 6135)%0A  > 9c25653 cdsbalancer: improve log messages (# 6134)%0A  > a02aae6 CONTRIBUTING.md: remove duplicated bullet point (# 6139)%0A  > cdab8ae clusterresolver: push empty config to child policy upon removal of cluster resource (# 6125)%0A  > 7651e62 transport: add a draining state check before creating streams (# 6142)%0A  > a2ca46c examples: organize READMEs better (# 6121)%0A  > 4efec30 stats/opencensus: remove leading slash for per call metrics (# 6141)%0A  > 78099db gcp/observability: Switch hex encoding to string() method (# 6138)%0A  > 70c5291 observability: remove import replace directive and switch it to point to latest commit (# 6122)%0A  > 66e3533 status: handle wrapped errors (# 6031)%0A  > a75fd73 Change version to 1.55.0-dev (# 6131)%0A  > b638faf stats/opencensus: Add message prefix to metrics names (# 6126)%0A  > c84a500 credentials/alts: defer ALTS stream creation until handshake time (# 6077)%0A  > 6f44ae8 metadata: add benchmark test for FromIncomingContext and ValueFromIncomingContext (# 6117)%0A  > a1e657c client: log last error on subchannel connectivity change (# 6109)%0A  > 36fd0a4 gcp/observability: Add compressed metrics to observability module and synchronize View data with exporter (# 6105)%0A  > 52ca957 xds: make comparison of server configs in bootstrap more reliable (# 6112)%0A  > 7507ea6 gcp/observability: Change logging schema and set queue size limit for logs and batching delay (# 6118)%0A  > 16c3b7d examples: add example for ORCA load reporting (# 6114)%0A  > b458a4f transport: stop always closing connections when loopy returns (# 6110)%0A  > 11e2506 tests: Scale down keepalive test timings (# 6088)%0A  > 5796c40 interop/observability: Pass interop parameters to client/server as-is (# 6111)%0A  > abd4db2 xdsclient/tests: fix flaky test NodeProtoSentOnlyInFirstRequest (# 6108)%0A  > 3633361 tests: support LRS on the same port as ADS (# 6102)%0A  > 0558239 Update CONTRIBUTING.md (# 6089)%0A  > 2260821 go.mod: upgrade golang.org/x/net to address CVE-2022-41723 (# 6106)%0A  > 60a1aa3 testutils: add support for creating endpoint resources with options (# 6103)%0A  > 92d9e77 xds: NACK route configuration if sum of weights of weighted clusters exceeds uint32_max (# 6085)%0A  > d02039b Deflake the integration test. (# 6093)%0A  > 55d8783 gcp/observability: Link logs and traces by logging Trace and Span IDs (# 6056)%0A  > ad4057f transport: stop returning errors that are always nil (# 6098)%0A  > 558e1b6 examples/authz: add token package docstring (# 6095)%0A  > 33df9fc credentials/xds: improve error message upon SAN matching failure (# 6080)%0A  > 3292193 xdsclient: handle race with watch timer handling (# 6086)%0A  > e83e34b xds/resolver/test: use a non-blocking send instead of closing the channel (# 6082)%0A  > b46bdef interop/observability: add GCP Observability Testing Client/Server (# 5979)%0A  > f311684 stats/opencensus: New uncompressed metrics and align with tracing spec (# 6051)%0A  > cc320bf grpc: Log server trailers before writing status (# 6076)%0A  > b9e6d59 xdsclient: send Node proto only on first discovery request on ADS stream (# 6078)%0A  > ae4a231 ringhash: ensure addresses are consistenly hashed across updates (# 6066)%0A  > 52dcd14 xdsclient: move tests from `e2e_test` to `tests` directory (# 6073)%0A  > d8f80bb stats/opencensus: Added client api latency and upgrade go.mod (# 6042)%0A  > a8b3226 gcp/observability: Disable logging and traces on channels to cloud ops backends (# 6022)%0A  > 20141c2 examples: add an example to illustrate authorization (authz) support (# 5920)%0A  > 8c374f7 clusterresolver: cleanup resource resolver implementation (# 6052)%0A  > 1d16ef5 metadata: Lowercase appended metadata (# 6071)%0A  > 8ba23be cmd/protoc-gen-go-grpc: bump -version to 1.3.0 for release (# 6064)%0A  > a1693ec fakeserver: remove ADS and LRS v2 support (# 6068)%0A  > 832ecc2 channelz: use protocmp.Transform() to compare protos (# 6065)%0A  > 28b6bcf xds/xdsclient: improve failure mode behavior (gRFC A57) (# 5996)%0A  > d53f0ec test: move compressor tests out of end2end_test.go (# 6063)%0A  > dba41ef metadata: fix validation issues (# 6001)%0A  > 75bed1d test: move e2e health checking tests out of end2end_test.go (# 6062)%0A  > 0586c51 internal/transport: reduce running time of test from 5s to 1s (# 6061)%0A  > 7437662 internal/transport: Fix flaky keep alive test (# 6059)%0A  > 681b133 admin/test: split channelz imports (# 6058)%0A  > 1093d3a channelz: remove dependency on testing package (# 6050)%0A  > 3775f63 xdsclient/transport: reduce chattiness of logs (# 5992)%0A  > 6fe609d xdsclient: minor cleanup in eds parsing (# 6055)%0A  > 5353eaa testing: add helpers to configure cluster specifier plugin type (# 5977)%0A  > 8702a2e stats/opencensus: Add top level call span (# 6030)%0A  > 85b95dc gcp/observability: Register new views (# 6026)%0A  > abff344 stats/opencensus: Add per call latency metric (# 6017)%0A  > 0f02ca5 gcp/observability: Switch observability module to use new opencensus instrumentation code (# 6021)%0A  > 6d612a3 resolver: update Resolver.Scheme() docstring to mention requirement of lowercase scheme names (# 6014)%0A  > 30d8c0a xds/internal/xdsclient: NACK empty clusters in aggregate clusters (# 6023)%0A  > 081499f xds: remove support for v2 Transport API (# 6013)%0A  > dd12def stats/opencensus: Add OpenCensus traces support (# 5978)%0A  > f4feddb github: update tests to use go version 1.20 (# 6020)%0A  > 8153410 client: Add dial option to disable global dial options (# 6016)%0A  > 55dfae6 resolver: document handling UpdateState errors by resolvers (# 6002)%0A  > ceb3f07 client: Revert dialWithGlobalOption (# 6012)%0A  > d655f40 internal/transport: fix severity of log when receiving a GOAWAY with error code ENHANCE_YOUR_CALM (# 5935)%0A  > b81e8b6 metadata: slightly improve operateHeaders (# 6008)%0A  > e9d9bd0 tests: reduce the degree of stress testing in long running tests (# 6003)%0A  > f855226 github: update codeQL action to v2 (# 6009)%0A  > f69e9ad stats/opencensus: Add OpenCensus metrics support (# 5923)%0A  > 3151e83 cmd/protoc-gen-go-grpc: export consts for full method names (# 5886)%0A  > d6dabba xds/server: reduce chattiness of logs (# 5995)%0A  > 0954097 server: expose API to set send compressor (# 5744)%0A  > a7058f7 xds/csds: switch tests to use the new generic xdsclient API (# 6000)%0A  > 3711154 xdsclient/bootstrap: reduce chattiness of logs (# 5991)%0A  > d103fc7 xdsclient/xdsresource: reduce chattiness of logs (# 5993)%0A  > 6a707eb client: add an option to disable global dial options (# 5990)%0A  > c813c17 Change version to 1.54.0-dev (# 5985)%0A  > 2a1e934 server: after GracefulStop, ensure connections are closed when final RPC completes (# 5968)%0A  > e2d69aa tests: fix spelling of variable (# 5966)%0A  > a6376c9 xds/resolver: cleanup tests to use real xDS client 3/n (# 5953)%0A  > bf8fc46 xds/resolver: cleanup tests to use real xDS client 5/n (# 5955)%0A  > 3930549 resolver: replace resolver.Target.Endpoint field with Endpoint() method (# 5852)%0A  > 894816c grpclb: rename `grpclbstate` packa…

---
## [Zergspower/effigy-se](https://github.com/Zergspower/effigy-se)@[8788e48378...](https://github.com/Zergspower/effigy-se/commit/8788e483788db2432b9649313efc9426d324379f)
#### Tuesday 2023-07-11 03:32:48 by Time-Green

Shuttle events (#76008)

## About The Pull Request


https://github.com/tgstation/tgstation/assets/7501474/a2d83ce8-eba1-42d9-a1f8-9d73f7c40b21

Adds shuttle events! Stuff can now start to happen outside the shuttle,
either benign or spicy (but usually just fun to watch)!
## Why It's Good For The Game

The shuttle escape sequence is an important part of the game, uniting
about every player surviving player. Recently, #71906 has made the
escape sequence more forgiving as well as more interesting by
conditionally doubling the playing field. The area outside the shuttle
is still mostly empty though, except for the few people being spaced,
daredevils and the occasional epic space fight.

This PR adds adds some space events to spice up the outside of the
shuttle! This both gives people something too look at, making the escape
sequence feel less static and more lively, as well as give people a
reason to go outside and get the full experience of ~being decapitated
by a meteor~ swimming with the fishes!

<details>
  <summary>Shuttle Events</summary>

**Friendly carp swarm**
Spawns a group of carp that flies past the shuttle, completely friendly
unless provoked.

**Friendly meteors**
Spawns a lot of strong meteors, but they all miss the shuttle.
Completely safe as long as you don't go EVA

**Maintenance debris**
Picks random stuff from the maintenance spawn pool and throws it at the
shuttle. Completely benign, unless you get hit in the head by a toolbox.
Could get you some cool stuff though!

**Dust storm**
Spawns a bunch of dust meteors. Has a rare chance to hit the shuttle,
doing minimal damage but can damage windows and might need inflight
maintenance

**Alien queen**
One in every 250 escapes. Spawns a player controlled alien queen and a
ripley mech. RIP AND TEAR!! Really not that dangerous when you realize
the entire crew is on the shuttle and the queen is fat as fuck, but can
still be fun to throw people around a bit before being torn to shreds.

**ANGRY CARP**
Once in every 500 escapes. Spawns 12 normal carp and 3 big carps, who
may just decide to go through the shuttle or try and bust through the
window if you look at them wrong. Somewhat dangerous, you could stay
away from the windows and try to hide, or more likely shoot at them and
weld the windows

**Fake TTV**
Lol

**Italian Storm**
Once in every 2000 rounds. Throws pasta, pizza and meatballs at the
shuttle. Definitely not me going off the rails with a testing event

**Player controlled carp trio**
Once in every 100 escapes. Spawns three player controlled carp to harass
the shuttle. May rarely be a magicarp, megacarp or chaos carp. I can't
honestly see them do anything other than be annoying for 3 seconds and
die

There are some other admin only ones: a group of passive carps going
directly through the shuttle and just being little shits, and a magic
carp swarm
</details>

Events are selected seperately, there isn't a crazy weighting system,
each just has a chance to run, and multiple could run at once. They also
don't immediately trigger, so people can get settled a bit, and to make
sure just waiting out the more dangerous ones is still a valid strategy.

## Changelog
:cl:
add: Adds shuttle events! If shuttle escapes weren't exciting before
(doubtful), they definitely are now! I'm joking it's mostly an
atmosphere thing.
admin: Adds an admin panel to interact with shuttle events, under the
Events tab: Change Shuttle Events
fix: Objects spawned in hyperspace will properly catch hyperspace drift
/:cl:

There's a few things I'd like to do later (another PR) (honestly anyone
can do them because I suck at follow-ups), because this is too big as
is:
- Hijack triggered shuttle events
- More events (got a lot of cool suggestions, but I'm putting most of
them on hold)
- Maybe stration announcements if some more dangerous ones get added
- Structures appearing next to the escape shuttle???

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [tabulon-ext/inxi](https://github.com/tabulon-ext/inxi)@[2434d89d0c...](https://github.com/tabulon-ext/inxi/commit/2434d89d0c75390511b75ee58ef40aba13f3863b)
#### Tuesday 2023-07-11 03:45:00 by Harald Hope

New version, new man. Continuing the Memory info rollout started in 3.3.27.

--------------------------------------------------------------------------------
SPECIAL THANKS:

1. Thanks to linuxquestions.org Slackware forums for poking around a bit at the
new Memory total logic.

--------------------------------------------------------------------------------
KNOWN ISSUES:

1a. MEMORY: The memory total: has to be synthesized in some cases, based on some
math and educated guessing. When these guesses fall outside of predetermined
ranges, inxi will show note: est. to let the user know the total was synthesized
and possibly incorrect. For detected virtual machines, inxi does not try to
synthesize the total because a VM can have any amount of RAM assigned.

If superuser, and -m used, shows the real total from dmidecode if any RAM was
found. Not all systems have DMI RAM data however, or have dmidecode installed.
Will fallback to sythetic method in that case, which is usually right.

1b. MEMORY: With the superuser /proc/iomem method, if on a VM and not using even
GiB sized RAM ollocation, and -M is not triggered (which usually lets inxi know
it's a VM), the total will get rounded up or down based on a set of rules. For
example, 2.5 GiB real would become 3 GiB. I don't see any solution to this,
either assume the /proc/iomem is right but needs rounding up, or assume the /sys
block counts are right, or remove the feature.

Shows note: est. in cases where the rounded total is greater than a dynamic
factor difference from the internal total amount.

2. GENERAL/GRAPHICS: The problem of users showing up, requesting a feature, then
not doing any work, research, supplying energy, interest, and dare I say,
passion - nothing, expecting 'someone else' to do the work for them, continues,
sadly, with the recent request for vulkan data for Graphics. This appears to be
a problem more with the modern generation of free software users, I don't
remember this type of attitude 20 years ago, but I did watch it as it started
getting more common. Demotivating to be honest, but maybe one day someone will
show up who actually cares enough to help get the features they want developed.

While I am leaving that up as a low priority feature request, I am not
personally interested in that feature, nor is anyone else I asked, and given how
much raw data there is, and how difficult it is to parse, I'll just leave it as
an existing issue which might get work in a few years time, or not, basically
will require someone showing up who actually actively cares.

--------------------------------------------------------------------------------
BUGS:

1. DISK: total: used: report could have had wrong results for used:, like used
being > total: because the filter lists were missing some file systems for
exclusion. More of a fix than a bug, but users might see it as a bug.

--------------------------------------------------------------------------------
FIXES:

1. INFO: get_gcc_data(): was showing same GCC version as main and alternate.
Failed to filter out the discovered primary, that is. This is because usually
name is gcc-11 but sometimes it's the whole version, like gcc-11.2.0, the full
version string. This is the case in Slackware for example.

2. SHORT: MEMORY: BSD: did not show '%' for memory used percent, just the
number.

3. DRIVES/PARTITIONS: PartitionItem::set_filters() added many more exclude
types, that will help avoid both creating wrong disk used totals, and also not
show label:/uuid: fields for filesystem types that don't have uuid/labels. There
were a lot missing: encrypted, distributed, stackable, remote. Should clean up
wrong disk used values in some cases.

4a. PARTITIONS: PartitionItem::set_filters(). Added a lot of file systems, many
fuse, distributed, stackable types.

4b. PARTITIONS: Extended remote file system ID by fs, and added fuse fs for
local mounts, like gvfs, mtp, ptp and many other variants, that's things like
mounting apple partition, android, iphone, archives, etc. This should correct an
entire class of source: ERR-102 outputs.

--------------------------------------------------------------------------------
ENHANCEMENTS:

1. BATTERY: Added 'power' to battery report. That's the amount of watts its
using at that moment, so not super useful since it's running inxi at that
moment. But the data was there, so might as well show it. Only for -Bxx since it
will be so variable. Shows after the charge/condition item.

2. SYSTEM: DistroData: added Oracle id and system base. Added Springdale/PUIAS
system base support. Note, unusually, Eurolinux, ScientificLinux 'just worked'
re id and system base even though that had never been explicitly added. This is
because their os-release file contains 'centos' string.

3. SYSTEM: DistroData: Added ubuntu mantic minotaur to ubuntu id matching table.
This only really is used by Mint, but there you have it. Also added Debian 14
codename Forky.

4a. MEMORY: Add total RAM from one of following:

* /sys/devices/system/memory (if it's available). This directory has to be
compiled into kernel, so is not always present. This source has advantage of
being user readable. If out of set bounds, shows note: est. to let user know
it's an estimate.

* If superuser and /proc/iomme, gets the total from /proc/iomem using some
tricks and synthetic methods, which in general is pretty accurate, but when out
of the bounds set, shows note: est. to let user know results are only estimates.
This overrides /sys total.

* If -m and dmidecode data found, uses the real RAM module total. For Linux and
superuser. This overrides iomem and /sys totals.

4b. MEMORY: add iGPU RAM from /proc/iomem when detected. Requires sudo/root.

4c. MEMORY: using the real -m/RAM total for memory total when available, since
that is the actual value we want, not the estimated stuff from /proc/iomem or
/sys/devices/system.

5. RAM: added a long time oversight, lack of per array RAM installed size and
occupied slots (modules). Those are now part of the Array line for each set of
modules. Since total already shows in System RAM line above, the granular per
array installed size total only shows if > 1 array is present, ie, almost never.

6. DRIVES: disk vendors, added more matches and vendors. We'll know the world is
changing in a significant way when no new vendors appear for a while, but that's
unlikely in the near term.

7. CPU: cpu_arch(), a few new ids added.

8. GRAPHICS: new amd, intel, nvidia ids, updates to driver version etc.

--------------------------------------------------------------------------------
CHANGES:

1. SHORT: for Memory:, switched to using MiB/GiB/TiB, these numbers are just
getting too big to be readable. This is also dynamic, if both used and available
are the same unit, shows x/y [unit], otherwise shows x [unit]/y [unit].

2. MEMORY: changed gpu: to igpu: to avoid confusing it with standalone gpu.
Since only raspberry pi had gpu ram data before, almost nobody would have seen
this in general anyway.

--------------------------------------------------------------------------------
DOCUMENTATION:

1. MAN/OPTIONS: Updated for -Bxx, battery power now.

2. MAN: updated to better define where the System RAM: total:.. available etc
come from, and what they refer to. Also added explanation in -m section about
what the stuff is, and what the field names refer to.

2a. DOCS: docs/inxi-ram.txt added, and more info moved from inxi-data.txt and
inxi-resources.txt. Goal is to remove both those files and move all their data,
and any new data, into granular inxi-xxx.txt files. Also moved some RAM data
from inx-unit-handling.txt to inxi-ram.txt.

2b. DOCS: docs/inxi-unit-handling.txt: updated with more ram / memory units,
code, etc, to better fit with the concept of the inxi-unit-handling.txt doc.

2c. DOCS: docs/inxi-partitions.txt: updated, added more sources for partition
file system types, cleaned up, more useful as a reference now.

2d. DOCS: docs/inxi-distros.txt: NEW, merged data from inxi-data.txt,
inxi-resources.txt. Updated and added more info.

2e. DOCS: docs/inxi-tools-mapping.txt split off from inxi-tools.txt, makes it
easier to find the mapping functions and features, which are hard to remember.
Also updated and improved its usability. This is kind of a key document because
it's hard to remember all the mapping tools internally, and this also connects
those tools to their relevant granular inxi-xxx.txt docs. Not that it will help
get helpers for these tedious tasks, but one can always dream, can't one?

3. DATA: data/graphics/ added for first vulkaninfo output file.

--------------------------------------------------------------------------------
CODE:

1a. RAM: Fixed an irregularity, for RamItem, it used MiB as internal unit, this
was silly because inxi uses KiB everywhere else. This correction was relatively
easy to do, and allows the values to be used by other parts of inxi, like
MemoryData.

1b. RAM: Added return of ram total for memory.

2a. INFO/RAM/PROCESSES: When MEMORY active, now uses row reference to create the
fields. For INFO, now uses MemoryData::row() to generate the row fields instead
of doing the logic in the info line generator. This simplifies the processing
and allows for more granular control of output.

2b. INFO/RAM/PROCESSES: Added debugger switches --dbg 53 (show raw KiB/count
values for /sys/devices/system/memory and /proc/iomem. Added --dbg 54, which
shows per line size for iomem, in human readable units, and a final summary
report of iomem and /sys data, this speeds up debugging.

2c. INFO/RAM/PROCESSES: Added --fake iomem, --fake sys-mem for debugging and
testing.

3. MEMORY: MemoryData::short_data(): added so one tool generates output for all
sources for short data. Easier to track and make consistent, and to make more
granular and robust.

4. DRIVES/PARTITIONS: PartitionItem::partition_filters(),
PartitionItem::fs_excludes(): refactored into PartitionItem::get_filters(),
PartitionItem::set_filters(). Cleaned up, organized better, made comments much
more useful. Goes with DOCS 2c updates. Now there's just one sub that does this
filter/exclude work, which makes it easier to maintain long term.

5. GLOBAL: Used a trick I just learned, declaring variables in the bracket scope
of a class, but not inside the package/class declaration. This makes it work
like a static variable, which Perl 5.008 doesn't support. You have to use a sub
inside the bracket scope to return the data outside that scope, but that is easy
to do.

6. MACHINE: Added return of b_vm for VM detection in MEMORY.

7. SYSTEM: CompilerVersion: Failed to properly use references when passing
$compiler around, not actually sure why it worked, but now is consistent.

---
## [SomeRandomOwl/tgstation](https://github.com/SomeRandomOwl/tgstation)@[d85e44c69c...](https://github.com/SomeRandomOwl/tgstation/commit/d85e44c69cc06dbeeb3a0de7f76273de45ee3893)
#### Tuesday 2023-07-11 04:15:55 by ChungusGamer666

SPECIES NUKING 2023: Head flags 3 & Knuckles: Fixes some growing pains with head flags  (#76440)

## About The Pull Request

Fixes https://github.com/tgstation/tgstation/issues/76422
This was caused by me somehow not using the wrapper there and not
noticing it

Also fixes hair gradients and facial hair gradients. I am pretty sure
they were uhh, being hidden behind the actual hair/facial hair. Oops.

Also also fixes spawning yourself as a human as admin and getting random
hair colors. That was just a failure to update the icon after updating
everything, I think?

Additionally, to totally babyproof all of this, ensures that head_flags
involved stuff gets applied AFTER species by creating a new preference
priority, and uses two separate wrappers to apply gradient style and
color.

Here's this absolute hellspawn to prove that everything works.

![image](https://github.com/tgstation/tgstation/assets/82850673/7ed29a68-cb60-4b28-996c-3be0e7331be8)

![image](https://github.com/tgstation/tgstation/assets/82850673/e57128be-0d7c-46ad-90dd-ee25981d0fea)

![image](https://github.com/tgstation/tgstation/assets/82850673/5c3619a8-fe6f-42b3-9fdc-12277d568e8d)

![image](https://github.com/tgstation/tgstation/assets/82850673/fdd13000-2220-47ad-8e02-44bc75a4a907)

Sorry for being so damn good at breaking this codebase.

## Why It's Good For The Game

Bugs are bad they make you mad

## Changelog

:cl:
fix: Hair and facial hair gradients work again now
fix: Facial hair colors apply properly again
fix: Admin spawned characters will get hair color preferences applied
properly
/:cl:

---
## [Bjarl/Shiptest](https://github.com/Bjarl/Shiptest)@[7468161f7e...](https://github.com/Bjarl/Shiptest/commit/7468161f7ec2180c7752cd2cc99b164522a3540a)
#### Tuesday 2023-07-11 05:13:02 by FalloutFalcon

Trickwines! Again! (#1914)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

Trickwines are a set of new reagents aimed at improving tribal/srm style
ships
The core concept are wines crafted out of mob drops and plants that
provide a buff on drinking and a debuff on throwing with bonus effects
against fauna
To facilitate the transfer of booze to target it also adds breakaway
flasks, 50u glass bottles that shatter violently on contact providing
extra throw force as well as a 25u gulp size which forces the user to
choose between buff or debuff
I plan on adding a fair few more Trickwines and the SRM Barrel Class
Brewer Vessel (SRM could really use one then 1 original ship) in later
prs to build on this concept
This HackMD will provide descriptions for the wines as well as a place
of information for all Trickwine-related content
https://hackmd.io/eUIddN2dS3mpeU1CThFGng

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
Adds a fun new option for ships that lack proper chemistry and forces
them to choose which effect they actually want.

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: FalloutFalcon
add: Trickwines
add: Breakaway flasks!
add: Basic Trickwine brewing equipment to the SRM glaive
imageadd: Sprites for breakaway flasks along with trick wine icons for
them!
code: Breakaway_flask_icon_state = null used for the same purpose as the
glass and shot glass versions
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

I DIDNT KNOW IF YOU RENAME A BRANCH IT CLOSES PRS RELATED TO IT?? I
THOUGHT IT JUST KNEW!!
3rd times a charm!

---------

Signed-off-by: FalloutFalcon <86381784+FalloutFalcon@users.noreply.github.com>
Signed-off-by: Mark Suckerberg <mark@suckerberg.gay>
Co-authored-by: Mark Suckerberg <mark@suckerberg.gay>

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[25c4ec7318...](https://github.com/treckstar/yolo-octo-hipster/commit/25c4ec73182b5fed93def56f87aafac626694ff4)
#### Tuesday 2023-07-11 05:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [rfka01/mame](https://github.com/rfka01/mame)@[4a5b8a415f...](https://github.com/rfka01/mame/commit/4a5b8a415fee66df01d57b871a8025d0f1f1a2f6)
#### Tuesday 2023-07-11 06:25:04 by wilbertpol

msx1_cart.xml: Added fourteen working items. (#11412)

* Removed Hopper (Europe) tape-to-cartridge hack.
* Demoted The Holy Quran (v1.00) to not working.

New working software list items (msx1_cart.xml)
-------------------------------
Hole in One Professional (Japan, alt 2) [file-hunter]
Hole in One Professional (Japan, alt 3) [file-hunter]
Hot-Asm (Brazil) [file-hunter]
Hot-Plan (Brazil) [file-hunter]
Hydlide II - Shine of Darkness (Korea) [file-hunter]
Hopper (Arab) [file-hunter]
Hans' Adventure (v1.1) [MSXDev]
Hans' Adventure (v1.0) [MSXDev]
Happy Halloween [Clube MSX]
Happy Square Christmas [303bcn]
Heart Stealer 2 [MSXDev]
Heroes Arena [MSXDev]
Hose Diogo Martinez: The Bussas Quest [MSXDev]
How Many Are The Dumbbells You Lift? [cobinee]

---
## [ClassicBoost/Another-PMD-Fan-Game](https://github.com/ClassicBoost/Another-PMD-Fan-Game)@[d822262cd4...](https://github.com/ClassicBoost/Another-PMD-Fan-Game/commit/d822262cd4750dea8178b9513a4aa0902478e86b)
#### Tuesday 2023-07-11 07:48:28 by ClassicBoost

I'm retarded as hell

enough to break the entire game without knowing what shit I've done. Amazing

---
## [alphagov/di-ipv-core-back](https://github.com/alphagov/di-ipv-core-back)@[76c59498cd...](https://github.com/alphagov/di-ipv-core-back/commit/76c59498cd9192d8dd01740f215ed6aae55a8460)
#### Tuesday 2023-07-11 08:00:26 by Chris Wynne

BAU: Add spotless check to pre-commit

It can be very annoying if you forget to run Spotless, only to find out
when your PR checks fail.

This adds a `spotlessCheck` to pre-commit. It will only check, not fix
for you, so you'd still have to manually run `spotlessApply`. This can
be changed if people think it's better for it to make the changes for
you.

The plugin being used is one I wrote and is a repo in my personal
GitHub. If people thing doing this is a good idea we should transfer to
to alphagov, in case I go under a bus.

---
## [WHOLE-HUMAN-DEVELOPMENT/my-project](https://github.com/WHOLE-HUMAN-DEVELOPMENT/my-project)@[124cc0e1d2...](https://github.com/WHOLE-HUMAN-DEVELOPMENT/my-project/commit/124cc0e1d2a193c51221bf6e7742387a28b20b2e)
#### Tuesday 2023-07-11 08:42:41 by @Arifendryw999

Create index.html for my-project Github Pages

This hackathon project runs a method or system:
1. e-learning from the Pi Network pioneer community so that each region can form a communication forum and friendship ties among fellow pioneers. the purpose of this learning is about the integrity of a person who must always be based on honesty, discipline, know the rules, be trustworthy or trustworthy, with these materials so that character building can be realized. in this case the dominant regarding heart or spiritual development.
2. E-commerce is a tool for each Pi Network pioneer in carrying out activities and is expected to open new jobs in their respective areas so that the core business of the pioneers will be created, which in the end the Pi Network pioneers will have an integrated independent spirit in the pi network utility ecosystem. in this case it is more dominant regarding physical development, especially market or business development rather than new activities in the Pi network ecosystem.
3. e-marketing is a strategy in a market approach where in a global system everything is online so that it requires challenges in responding to technological developments and global market demands. here it tends to be stronger in creating a utility ecosystem among the pioneers of the pi network, which will complement each other, strengthen each other, with the principles of pioneers, for pioneers and for pioneers. I hope that unity and oneness, starting from the pi network pioneers, will create a strong sense of nation and state.


Signed-off-by: @Arifendryw999 <133835563+Alvaromeo999@users.noreply.github.com>

---
## [johnclot69/libgdx](https://github.com/johnclot69/libgdx)@[e1d1fdc5fb...](https://github.com/johnclot69/libgdx/commit/e1d1fdc5fb5b8409dc74f638c633ead405e535f3)
#### Tuesday 2023-07-11 08:43:59 by Tommy Ettinger

I18NMessageTest needs to reset I18NBundle static state. (#7101)

* Mark PauseableThread as excluded on GWT.

* Minor typo corrections.

* Fix atan2() when it should produce 0f.

Without this small change (which has essentially no performance impact that I could measure), calling atan2() with a point on the x-axis would produce a small but non-zero result, which is incorrect.

* Add atan, atan2, asin, acos for degrees.

This also includes atan2Deg360(), which in my opinion is the most useful of these because it does something differently from Math.atan2(), and can often save some effort.

* Approximations for tan() and tanDeg().

Sorry this is so long-winded, but the error isn't as straightforward to express as with sin() or cos().

* Apply formatter

* Add to MathUtilsTest.

* Apply formatter

* Stop trying to load defaults from wrong dir.

This old behavior broke Flame's effect-open dialog when any particle effect used the default billlboard or model particle. Now Flame tries to load a file given its absolute path (like before), but if it fails, it falls back to trying the default filenames as internal files.

* I18NMessageTest needs to reset I18NBundle state.

If you run I18NSimpleMessageTest and then I18NMessageTest without this PR, then the first test will have called I18NBundle.setSimpleFormatter(true), but the second test needs it to be set to false.

Because the tests are still perfectly usable if you run them on their own (or use LWJGL2, I think, because it might not share static state), this is not at all a priority to merge; it just makes running many tests in one session not throw an Exception.

---------

Co-authored-by: GitHub Action <action@github.com>

---
## [rerun-io/rerun](https://github.com/rerun-io/rerun)@[926bf048e2...](https://github.com/rerun-io/rerun/commit/926bf048e28a8f4c637afce3c57d793ec8de8454)
#### Tuesday 2023-07-11 08:45:21 by Emil Ernerfeldt

Use `camino` crate for UTF8 paths in `re_types_builder` (#2637)

### What
TLDR: camino paths are a more ergonomic, since they implement
`to_string`, `as_str` etc. I think we should use it in more places.

From [the docs of `camino`](https://crates.io/crates/camino):

#### Why camino?
`camino`'s `Utf8PathBuf` and `Utf8Path` types are like the standard
library's `PathBuf` and `Path` types, except
they are guaranteed to only contain UTF-8 encoded data. Therefore, they
expose the ability to get their
contents as strings, they implement `Display`, etc.

The `std::path` types are not guaranteed to be valid UTF-8. This is the
right decision for the standard library,
since it must be as general as possible. However, on all platforms,
non-Unicode paths are vanishingly uncommon for a
number of reasons:
* Unicode won. There are still some legacy codebases that store paths in
encodings like [Shift JIS], but most
  have been converted to Unicode at this point.
* Unicode is the common subset of supported paths across Windows and
Unix platforms. (On Windows, Rust stores paths
as [an extension to UTF-8](https://simonsapin.github.io/wtf-8/), and
converts them to UTF-16 at Win32
  API boundaries.)
* There are already many systems, such as Cargo, that only support UTF-8
paths. If your own tool interacts with any such
system, you can assume that paths are valid UTF-8 without creating any
additional burdens on consumers.
* The ["makefile
problem"](https://www.mercurial-scm.org/wiki/EncodingStrategy#The_.22makefile_problem.22)
asks: given a
Makefile or other metadata file (such as `Cargo.toml`) that lists the
names of other files, how should the names in
the Makefile be matched with the ones on disk? This has *no general,
cross-platform solution* in systems that support
non-UTF-8 paths. However, restricting paths to UTF-8 eliminates this
problem.

[Shift JIS]: https://en.wikipedia.org/wiki/Shift_JIS

Therefore, many programs that want to manipulate paths *do* assume they
contain UTF-8 data, and convert them to `str`s
as necessary. However, because this invariant is not encoded in the
`Path` type, conversions such as
`path.to_str().unwrap()` need to be repeated again and again, creating a
frustrating experience.

Instead, `camino` allows you to check that your paths are UTF-8 *once*,
and then manipulate them
as valid UTF-8 from there on, avoiding repeated lossy and confusing
conversions.


### Checklist
* [x] I have read and agree to [Contributor
Guide](https://github.com/rerun-io/rerun/blob/main/CONTRIBUTING.md) and
the [Code of
Conduct](https://github.com/rerun-io/rerun/blob/main/CODE_OF_CONDUCT.md)
* [x] I've included a screenshot or gif (if applicable)
* [x] I have tested [demo.rerun.io](https://demo.rerun.io/pr/2637) (if
applicable)

- [PR Build Summary](https://build.rerun.io/pr/2637)
- [Docs preview](https://rerun.io/preview/pr%3Aemilk%2Fcamino/docs)
- [Examples
preview](https://rerun.io/preview/pr%3Aemilk%2Fcamino/examples)

---
## [crispysandwhich/refactored-barnacle](https://github.com/crispysandwhich/refactored-barnacle)@[3f077aae0b...](https://github.com/crispysandwhich/refactored-barnacle/commit/3f077aae0b47326723185f833aff2b39ab7d90cd)
#### Tuesday 2023-07-11 08:58:59 by coolistkovbel

my heart hurts, life is slow, i cant seem to trust, lost friends, lost hope, really really funny how things have changed, i litterally see what has happenend but everyone wants to play pretend.... what is life, got the images to work, hopefully get this shit running soon

---
## [ghostsheet/cmss13](https://github.com/ghostsheet/cmss13)@[a48f036428...](https://github.com/ghostsheet/cmss13/commit/a48f0364283526637b637542b432d91593b2bdf5)
#### Tuesday 2023-07-11 09:04:33 by QuickLode

Colony Synthetics have less resistance but are faster. (#3821)

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->
While exploring reasons why this role was underplayed one of the things
that came up was its speed. It is dreadfully slow - to the point where
defenders are able to force an engagement against Synthetics. There is
no chance to run from anything faster as a Colony Synthetic. Making it
have to fight often.

Lowering the resistance is something devs wanted, and for gameplay this
is good because a Synthetic shouldn't be forced into a fight unless they
have no other option. Especially not by something as slow as a defender.
Might tweak later but council generally is in agreement with this
change. Little by little!

For the CQC, a Colony Synthetic is not as advanced as a Shipside one,
but still is more than capable of outmanuevering a human. As for the
hilarious UPP Pvt being better than a Colony Synth in CQC I will make a
separate PR

For Fireman, a Synthetic can bend metal, move cars and do many other
'superhuman' feats of stength, they should not struggle at carrying
people, especially shouldn't be worse at carrying people than a Marine.
It's from 1 to 3, to represent the strength yet aging capabilities of
the Colony Synthetic. @morrowwolf forgot this one

- doesn't touch WJ
# Explain why it's good for the game
Less resistance is something devs wanted.
Allows Colony Synthetics an option to avoid certain engagements as now
they are able to outrun some types of Xenomorphs off-weeds. Defenders
should not be able to catch them offweeds.
A Synthetic should have no problem carrying something as light as a
human being - they especially should not have MORE trouble carrying
someone than your standard human doctor.

# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl: QuickLoad
balance: Colony Synthetics are faster but are less resistant. This
allows for the option of avoiding engagements.
balance: Colony Synthetics have slightly better CQC and can carry people
better.
/:cl:

---
## [suyambuganesh82/quine](https://github.com/suyambuganesh82/quine)@[2c8adb266d...](https://github.com/suyambuganesh82/quine/commit/2c8adb266da8c058d0b5179d71a00a65bb5c9cfc)
#### Tuesday 2023-07-11 09:28:30 by Leif Warner

Make Hashable derivation not infinitely recurse on missing instance.

* Make Hashable derivation not infinitely recurse on missing instance.

Having the compiler indefinitely hang makes it hard to see where the
issue is - if the compiler's not giving you any output.

Also added a `Hashable` instance for `OffsetTime`.

Removed the variance annotation from `Hashable`, and removed the single
implicit parameterized over all subtypes of `Iterable`, in favor of
implicits for specific instances (implemented by that general iterable
impl), in keeping with the patterns seen in generic derivation in other
libraries. In my experience, subtyping and implicit search don't mix
well, and it's probably best to keep implicit search as specific and
constrained as possible. And it's suspicious that the prior iterable1
impl seemed to require a `Lazy` on its element `Hashable` parameter.

Also removed `iterable2` (Maps can be hashed by typing them as an
Iterable of tuples and using the existing iterable hash implementation).

Rewrote the shapeless Generic derivation for Hashable using its
`TypeClass` helper class. The benefits for this helper aren't as much if
you're just using Generic instead of LabelledGeneric - it was mainly to
make sure we were following a "known good" pattern, as the previous impl
seemed to have an issue w/ infinitely recursing at compile time if an
instance was missing.

* Switch UnitSq back to being a case class (rather than an object)

For cursed "concrete val in superclass" / shapeless reasons.

GitOrigin-RevId: 2cb020dd5ebf4e728200b45c802e09b46300a77e

---
## [zx70/mame](https://github.com/zx70/mame)@[c4a19a68a6...](https://github.com/zx70/mame/commit/c4a19a68a67cd32ffaaa37edfd6f1c2ba347905f)
#### Tuesday 2023-07-11 09:35:57 by Ivan Vangelista

New systems marked not working
------------------------------
Desert Gold (20202311, ASP) [anonymous, Heihachi_73]
Diamond Eyes (10129211, ASP) [anonymous, Heihachi_73]
Dolphin Treasure (10177911, ASP) [anonymous, Heihachi_73]
Silk Road (10176811, ASP) [anonymous, Heihachi_73]
Snap Shot (20115211, ASP) [anonymous, Heihachi_73]
The Golden Gong (20196011, ASP) [anonymous, Heihachi_73]
Wild Cougar - Power Pay (30214211, ASP) [anonymous, Heihachi_73]
Wings over Olympus (10176511, ASP) [anonymous, Heihachi_73]

New clones marked not working
-----------------------------
5 Dragons (10176611, ASP) [anonymous, Heihachi_73]
5 Dragons (10178611, New Zealand) [anonymous, Heihachi_73]
5 Koi - Power Pay (1J016211, ASP) [anonymous, Heihachi_73]
50 Lions (0152077, US) [anonymous, Heihachi_73]
100 Lions (30223811, ASP) [anonymous, Heihachi_73]
Arabian Nights (10122611, ASP) [anonymous, Heihachi_73]
Big Ben (10169611, ASP) [anonymous, Heihachi_73]
Buccaneer (10181911, ASP) [anonymous, Heihachi_73]
Buffalo (20232611, ASP) [anonymous, Heihachi_73]
Brazil (10218511, ASP) [anonymous, Heihachi_73]
Dolphin Treasure (20265311, New Zealand) [anonymous, Heihachi_73]
Dream Catcher (10172921, ASP) [anonymous, Heihachi_73]
Fire Dancer (10191311, ASP) [anonymous, Heihachi_73]
Fortune King (10230911, ASP) [anonymous, Heihachi_73]
Geisha (10122011, ASP) [anonymous, Heihachi_73]
Geisha (10112411, ASP) [anonymous, Heihachi_73]
Go For Green (10122111, ASP) [anonymous, Heihachi_73]
Golden Pyramids (10196511, ASP) [anonymous, Heihachi_73]
Heart of Gold (10184211, ASP) [anonymous, Heihachi_73]
Helen of Troy (10129121, ASP) [anonymous, Heihachi_73]
Helen of Troy (10116411, ASP) [anonymous, Heihachi_73]
Hollywood Dreams (10122811, ASP) [anonymous, Heihachi_73]
Helen of Troy (10122711, ASP) [anonymous, Heihachi_73]
House of Hearts (10208411, ASP) [anonymous, Heihachi_73]
Indian Dreaming (10192211, ASP) [anonymous, Heihachi_73]
King of the Nile (10127511, ASP) [anonymous, Heihachi_73]
Let's Go Fish'n (10223911, ASP) [anonymous, Heihachi_73]
Money Tree (10122211, ASP) [anonymous, Heihachi_73]
Paris Lights (10139011, ASP) [anonymous, Heihachi_73]
Peacock Magic (10134311, ASP) [anonymous, Heihachi_73]
Pelican Pete (10196211, ASP) [anonymous, Heihachi_73]
Pirates (10122311, ASP) [anonymous, Heihachi_73]
Pompeii (10122411, ASP) [anonymous, Heihachi_73]
Queen of Sheba (30146921, ASP) [anonymous, Heihachi_73]
Queen of the Nile (10204311, ASP) [anonymous, Heihachi_73]
Queen of the Nile (10192311, ASP) [anonymous, Heihachi_73]
Queen of the Nile Special Edition (10127411, ASP) [anonymous, Heihachi_73]
Ruby Magic (10148811, ASP) [anonymous, Heihachi_73]
Scatter Magic II (10122511, ASP) [anonymous, Heihachi_73]
Spring Festival (20267211, New Zealand) [anonymous, Heihachi_73]
Tigress (20243811, ASP) [anonymous, Heihachi_73]
Tiki Torch (10124011, New Zealand) [anonymous, Heihachi_73]
Torch of the Gods (20210211, ASP) [anonymous, Heihachi_73]
Turtle Treasure (10239811, ASP) [anonymous, Heihachi_73]
Where's The Gold (10177111, ASP) [anonymous, Heihachi_73]
Wild Cats (20258111, ASP) [anonymous, Heihachi_73]
Wild Goose (10155911, ASP) [anonymous, Heihachi_73]
Wild Panda (20225011, ASP) [anonymous, Heihachi_73]
Zorro (20167511, ASP) [anonymous, Heihachi_73]

-aristocrat/aristmk6.cpp updates:
* dumped 3 more System EPROM Sets [anonymous, Heihachi_73]
* renamed "Malaysian" games to ASP as the games don't have any specific region, only the BIOS does [Heihachi_73]

---
## [gportay/iamroot](https://github.com/gportay/iamroot)@[28561275a9...](https://github.com/gportay/iamroot/commit/28561275a90b8e80d862cf6882966c1cb77fa363)
#### Tuesday 2023-07-11 09:42:20 by Gaël PORTAY

dso: guess the deflib from the shared object

According to ld.so(8):

	On some 64-bit architectures, the default paths for 64-bit
	shared objects are /lib64, and then /usr/lib64.

The default library path differs on some 64-bit architectures on the
GNU/Linux systems. This behaviour is driven by the environment variable
IAMROOT_LIBRARY_PATH.

The glibc x86_64 and aarch64 architectures use the directory lib64
instead of lib (i.e. IAMROOT_LIBRARY_PATH=/lib64:/usr/lib64).

The musl library and both FreeBSD and OpenBSD systems use directory lib
only.

Furthermore, this default library path is distro specific on the Linux
systems. Arch Linux (x86_64 only) uses lib, symlinks lib64 to lib and
uses lib32 for its multilib support. Fedora uses distinct directories
for both lib and lib64, lib for 32-bits, lib64 64-bit. It is different
in the Debian world and its multiarch[1] support; it adds a tuple[2]
directory after the lib directory for the architecture.

This makes the magical very tricky to guess the default library path on
the Linux systems; it shall support the following situations:
 1. cross-chroot libc (i.e. from GNU World to musl)
 2. cross-chroot architecture (i.e. form x86-64 to i686 or armv7-a)
 3. execve executables (i.e. shared object with an interpreter)
 4. dlopen libraries (i.e. shared object without an interpreter)

The magic is based on the ELF header to guess if the chroot is a 32-bit
or a 64-bit world and if the operating system and its ABI is a either
UNIX System V or GNU/Linux or even FreeBSD.

The name of the dynamic loader is also needed to detect a Linux world
since the GNU/Linux ELF shared objects can be either UNIX System V or
GNU/Linux (OpenBSD uses UNIX System V as well).

The dynamic loader is in the interpreter segment of the ELF executable
file. However, the none-executable files ELF shared objects (such as
libraries) does not have that segment.

Therefore, it is hard to determine if the chroot world is either a
64-bit GNU/Linux or a musl (or even OpenBSD), and if it has to use
either /lib64:/usr/lib64 or /lib:/usr/lib as default library path
though; as needed by the point 4.

The libc soname is system specific:
 - libc.so.6 for GNU/Linux since glibc 2.0
 - libc.so.5 for Linux libc (former libc based on glibc 1; see the note
   below)
 - libc.so for musl (note: the dynamic loader is a symlink to libc)
 - libc.so.5 for FreeBSD 5.0
 - libc.so.6 for FreeBSD 6.0
 - libc.so.7 for FreeBSD since since 7.0
 - libc.so.96.2 for OpenBSD 7.2
 - libc.so.97.1 for OpenBSD 7.3

It is not ideal to rely on the libc soname as it is subject to collision
between the different operating systems; for example with the libc.so.6
of FreeBSD 6.x.

Hopefully, the libc.so.6 soname is pretty stable as the glibc 2.0 was
released in the early of 1997 (i.e. 26 years ago)[3].

Even better, the GNU libc needs the dynamic loader while the FreeBSD
libc does not; a least since 2.0.7 (tested down to Debian 2.0 Hamm[4];
Debian 1.3 Bo[5] was using the former Linux libc fork, aka libc.so.5).

Debian 2.0 (i386):

	$ curl -O http://archive.debian.org/debian/dists/hamm/main/binary-i386/base/libc6_2.0.7t-1.deb
	$ ar x libc6_2.0.7t-1.deb
	$ tar xf data.tar.gz
	$ readelf -a lib/libc.so.6 | grep -E '(NEEDED|SONAME)'
	 0x00000001 (NEEDED)                     Shared library: [ld-linux.so.2]
	 0x0000000e (SONAME)                     Library soname: [libc.so.6]
	$ file -L lib/libc.so.6
	lib/libc-2.0.7.so: ELF 32-bit LSB shared object, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, stripped, too many notes (256)
	$ lib/ld-linux.so.2 lib/libc.so.6
	GNU C Library production release version 2.0.7, by Roland McGrath et al.
	Compiled by GNU CC version 2.7.2.3.
	Copyright (C) 1992, 93, 94, 95, 96, 97, 98 Free Software Foundation, Inc.
	This is free software; see the source for copying conditions.
	There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A
	PARTICULAR PURPOSE.
	Compiled on a Linux 2.0.33 system on 1998/07/16.
	Available extensions:
		GNU libio by Per Bothner
		BIND-4.9.7-REL
		NIS(YP) NSS modules 0.8 by Thorsten Kukuk
		UFC-crypt, patchlevel 1e by Michael Glad
		linuxthreads-0.6 by Xavier Leroy
	Report bugs using the `glibcbug' script to <bugs@gnu.org>.

Debian 1.3 (i386):

	$ curl -O http://archive.debian.org/debian/dists/bo/main/binary-i386/base/libc5_5.4.33-6.deb
	$ ar x libc5_5.4.33-6.deb
	$ tar xf data.tar.gz
	$ readelf -a lib/libc.so.5 | grep -E '(NEEDED|SONAME)'
	 0x0000000e (SONAME)                     Library soname: [libc.so.5]

Consequently, the default library path may be guessed to dlopen the
shared objects that are not executable files but that are linked against
the GNU libc; as long as the libc.so.6 is the library soname and as long
as it is executable and contains the needed dynamic loader. This hacky
guess has to be updated after every bump of the libc soname or if the
libc ceases to be executable (i.e. no more need to the dynamic loader or
no more interpreter).

It falls back to the executable file if the shared object is not linked
against the GNU libc library.

This guesses the default library path of the chroot'ed Linux
environnement by doing the magic mentionned above.

Note: According to libc(7):

	Linux libc

	In the early to mid 1990s, there was for a while Linux libc, a
	fork of glibc 1.x created by Linux developers who felt that
	glibc development at the time was not sufficing for the needs of
	Linux. Often, this library was referred to (ambiguously) as just
	“libc”. Linux libc released major versions 2, 3, 4, and 5, as
	well as many minor versions of those releases. Linux libc4 was
	the last version to use the a.out binary format, and the first
	version to provide (primitive) shared library support. Linux
	libc 5 was the first version to support the ELF binary format;
	this version used the shared library soname libc.so.5. For a
	while, Linux libc was the standard C library in many Linux
	distributions.

	However, notwithstanding the original motivations of the Linux
	libc effort, by the time glibc 2.0 was released (in 1997), it
	was clearly superior to Linux libc, and all major Linux
	distributions that had been using Linux libc soon switched back
	to glibc. To avoid any confusion with Linux libc versions, glibc
	2.0 and later used the shared library soname libc.so.6.

	Since the switch from Linux libc to glibc 2.0 occurred long ago,
	man-pages no longer takes care to document Linux libc details.
	Nevertheless, the history is vis‐ ible in vestiges of
	information about Linux libc that remain in a few manual pages,
	in particular, references to libc4 and libc5.

[1]: https://wiki.debian.org/Multiarch
[2]: https://wiki.debian.org/Multiarch/Tuples
[3]: https://linux.die.net/man/7/libc
[4]: http://archive.debian.org/debian/dists/hamm/main/binary-i386/base/libc6_2.0.7t-1.deb
[5]: http://archive.debian.org/debian/dists/bo/main/binary-i386/base/libc5_5.4.33-6.deb

---
## [Jacquerel/orbstation](https://github.com/Jacquerel/orbstation)@[4c99fb2ebb...](https://github.com/Jacquerel/orbstation/commit/4c99fb2ebb26179044c582ae6494338cb2aa35e2)
#### Tuesday 2023-07-11 12:05:46 by carlarctg

Coroner additions and tweaks (#76534)

## About The Pull Request

Serrated bone shovels can be created with any kind of shovel now, not
just a spade (???)

Serrated bone shovels can be used in place of circular saw in most
surgeries.

Added a duller (still deadly) variant of the serrated bone shovel as
coroner mail.

Autopsy scanners now act as advanced health analyzers on dead and
seemingly-dead people.

Increased the force, throwforce, and wound bonus of inert ritual knives
and scythes.

Coroner gloves can quickly apply medicine like nitrile gloves.
## Why It's Good For The Game

> Serrated bone shovels can be created with any kind of shovel now, not
just a spade (???)

Weird ass bug.

> Serrated bone shovels can be used in place of circular saw in most
surgeries.

It's serrated, it's cool, it's rare, it has a fast toolspeed.

> Added a duller (still deadly) variant of the serrated bone shovel as
coroner mail.

Very thematic for the coroner, should probably also be a heirloom item
but whatevs. Weaker so there's still a reason to seek out the OG.

> Autopsy scanners now act as advanced health analyzers on dead and
seemingly-dead people.

Scanning corpses is pretty important during surgery - it tells you how
much blood they have, organ damage, diseases... these things don't
appear in the surgical computer readout, which means the coroner has to
go out of his cave to pick up a boring light blue meatbag wound scanner.
This also incentivizes coroners to do their job by giving them something
cool that only works on dead bodies.

> Increased the force, throwforce, and wound bonus of inert ritual
knives and scythes.

These two options in the MortiDrobe are pretty frickin' badass,
especially with how SICK the Coroner looks with them, double especially
in combat.


![image](https://github.com/tgstation/tgstation/assets/53100513/98c6f8a5-3e5a-41a9-8a9c-cb6b82ecc0b8)

However, there's the large issue that as actual weapons they're really,
really weak. Not enough damage, when I use them in combat I both feel
badass but also get a nagging feeling in the back of my mind that I'm
intentionally gimping myself, and with only 10 damage I can *really*
feel it. I find it unfair that these are objectively worse than a
welding tool or even a Butcher's Cleaver when they're a lot more
involved to find, and scarce besides. These arguments apply equally to
the Wizard's ritual knife, and the scythe.

Additionally on the scythe, the crew really needs more good ghetto
weaponry that isn't the boring same ol' of baseball bats, spears,
cleavers... and making scythes useful is a great way to help bridge that
gap. They deal a satisfying amount of damage now, with the clear
downside, of course, being that they're bulky and hard to lug around.

> Coroner gloves can quickly apply medicine like nitrile gloves.

'Fast medicine' doesn't just cover sutures, it also covers medical gel.
Specifically, sterilizer gel. I find it annoying that the Coroner is
encouraged to give up his drip for the boring life-saver nitrile gloves,
because the difference in applying time really does make a difference -
it makes gel applying go from annoying to smooth, which is important
considering the whole purpose of sterilizer gel is to make surgeries go
faster. The Coroner has surgery and thus medical locker access to begin
with, so this isn't a balance problem, (and nitrile gloves are found by
the dozen anyways) especially with how rare the coroner gloves are.
## Changelog
:cl:
fix: Serrated bone shovels can be created with any kind of shovel now,
not just a spade (???)
add: Serrated bone shovels can be used in place of circular saw in most
surgeries.
add: Added a duller (still deadly) variant of the serrated bone shovel
as coroner mail.
add: Autopsy scanners now act as advanced health analyzers on dead and
seemingly-dead people.
add: Increased the force, throwforce, and wound bonus of inert ritual
knives and scythes.
add: Coroner gloves can quickly apply medicine like nitrile gloves.
/:cl:

---
## [Jacquerel/orbstation](https://github.com/Jacquerel/orbstation)@[721fd30837...](https://github.com/Jacquerel/orbstation/commit/721fd308378dc6ef7595c1ea4b92d679ba723188)
#### Tuesday 2023-07-11 12:05:46 by carlarctg

Heavily reworks and resprites first aid analyzers. (#76533)

## About The Pull Request

Heavily reworks and resprites first aid analyzers. They now display if
they're happy, sad, angry, or warning you! Also a 'pricking' animation.

First aid analyzers are now found in all basic and specialized medkits.
Toxin medkits get a new* disease analyzer. Miners get a miner-colored
one in their box.

Scanning yourself with a first aid analyzer will 'create a holo-image
with treatment instructions next to your wounds', doubling the speed of
treatment of scanned wounds!

Health analyzers now have a scanning sound, courtesy of CM.

Refactored some wound code to make treatment duration changes and
changes in the description of wounds easier.

Fixed a dummy parent feature of the health analyzer (Verbose mode)
showing up, uselessly, on the disease and first aid subtypes.

Surgical processors and slime scanners have recieved a similar resprite.
## Why It's Good For The Game

> Heavily reworks and resprites first aid analyzers. They now display if
they're happy, sad, angry, or warning you! Also a 'pricking' animation.

These things have long, long needed some sprite love. Displaying emotion
will make them have a lot more 'weight' to them, same with the prick.
The old, shitty spectrometer sprites have gone directly into the
dumpster.

> First aid analyzers are now found in all basic and specialized
medkits. Toxin medkits get a new* disease analyzer. Miners get a
miner-colored one in their box.

They have also needed some gameplay love! Placing them in these kits is
not going to be a massive game-changer when they were already easily
found around the station in emergency medkits, but it will fill up that
awkward empty slot.

> Scanning yourself with a first aid analyzer will 'create a holo-image
with treatment instructions next to your wounds', doubling the speed of
treatment of scanned wounds!

The biggest gameplay-impacting change in this PR, I *sincerely* believe
this is the perfect solution to first aid analyzers being completely
redundant with eyesight. This lets you/someone else scan your wounds to
speed up treatment, with a neat in-character reason for it -
'holo-images' appearing on your body, like penlights.

This will speed up wound treatment, but I believe that is for the best,
as currently treating wounds is so slow that half the time it's not
worth it (or more accurately, it doesn't feel worth it in comparison to
the effort you're putting in) and you're better off shrugging off minor
wounds. It will do so in a way that requires a modicum of effort, so
it's not just a flat buff across the land.

> Health analyzers and gene scanners now have a scanning sound, courtesy
of CM.

It's a neat sound that will make medbay feel more alive. First aid
analyzers get a beeboop instead.

> Surgical processors and slime scanners have recieved a similar
resprite.

IT'S SPRITE MANIA IN HERE
## Changelog
:cl:
Carlarc, Weird Orb
image: Heavily reworks and resprites first aid analyzers. They now
display if they're happy, sad, angry, or warning you! Also a 'pricking'
animation.
add: First aid analyzers are now found in all basic and specialized
medkits. Toxin medkits get a new* disease analyzer. Miners get a
miner-colored one in their box.
balance: Scanning yourself with a first aid analyzer will 'create a
holo-image with treatment instructions next to your wounds', doubling
the speed of treatment of scanned wounds!
sound: Health analyzers and gene scanners now have a scanning sound,
courtesy of CM.
refactor: Refactored some wound code to make treatment duration changes
and changes in the description of wounds easier.
fix: Fixed a dummy parent feature of the health analyzer (Verbose mode)
showing up, uselessly, on the disease and first aid subtypes.
image: Surgical processors and slime scanners have recieved a similar
resprite.
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [Jacquerel/orbstation](https://github.com/Jacquerel/orbstation)@[a2c8cce535...](https://github.com/Jacquerel/orbstation/commit/a2c8cce5359162a8a697ce109801ec268bf0c8a5)
#### Tuesday 2023-07-11 12:05:46 by John Willard

Bilingual can now choose their language (#76609)

## About The Pull Request

This was one of the tradeoffs for removing other, more consistent
sources of languages, and was requested by Melbert among many others.
This does go against my wanted goal of decreasing the risk of
eavesdropping by other players through just magically knowing a
language, but it is an expensive quirk and it is in their medical
records, which makes it better than language encryption keys or silicon
just innately knowing them.

This also limits Bilingual to only roundstart languages (+Uncommon),
rather than being randomly selected from a list (that had very useless
ones like monkey, podpeople, and beachbum). This is mostly just for
modularity, I didn't want to make it look terrible code-wise and thought
this may be the optimal way to handle it.

This is also me going back on
https://github.com/tgstation/tgstation/pull/71773 - which I had closed
myself.

## Why It's Good For The Game

If we're gonna keep the Bilingual quirk, it might as well be something
players can choose the language of, it's their character and they should
be allowed to decide how their character is, and it is my fault that
this stupid compromise of "getting a random language" was made in the
first place. It never should've happened.
It now actually limits it to roundstart-only languages, so there's no
way you can spy on people who prepare in advance through becoming
podpeople, or monkeys, etc.

## Changelog

:cl:
balance: Bilingual quirk now lets you choose your language between ones
given to roundstart species.
balance: Foreigner and Bilingual are now mutually exclusive languages.
/:cl:

---
## [lm4649/poem](https://github.com/lm4649/poem)@[51a1870589...](https://github.com/lm4649/poem/commit/51a18705899284e31262d2eead3392d2764d04b7)
#### Tuesday 2023-07-11 12:06:40 by Lopes Marc (loma)

[IMP] zen: add verse about code ambiguity

A verse about how to deal with code ambiguity was missing to the zen poem.

Computers have made humans superstitious: To exorcise the demons in our
computers we perform the sacred ritual of turning them off and then on.
Supposedly this will fix any mysterious problem. However, computers are
not magic. If your code is not working, there is a reason and only
careful, critical thinking will solve it. Refuse the temptation to
blindly try solutions until something seems to work; often you have
merely masked the problem rather than solved it.

task-chakra-wide-open

---
## [mija-odoo/poem](https://github.com/mija-odoo/poem)@[09e8dd6c07...](https://github.com/mija-odoo/poem/commit/09e8dd6c076c2579d08da3a90c96ea6748659f1d)
#### Tuesday 2023-07-11 12:12:33 by Michel Jacquemin (mija)

[IMP] zen: verse about ambiguity

Computers have made humans superstitious: To exorcise the demons in our computers we perform
the sacred ritual of turning them off and then on. Supposedly this will fix any mysterious problem.
However, computers are not magic. If your code isn’t working, there is a reason and only careful,
critical thinking will solve it. Refuse the temptation to blindly try solutions until something
seems to work; often you have merely masked the problem rather than solved it.

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[e7c8fed8e3...](https://github.com/odoo-dev/odoo/commit/e7c8fed8e373d7005c16c88d3a7bad6f425d13e5)
#### Tuesday 2023-07-11 13:06:14 by qsm-odoo

[FIX] website, *: allow to re-edit company team snippet images

*: web_editor

Since [1], it was not possible to edit a company team snippet image
anymore as soon as the page was saved once. Indeed that commit added
o_not_editable/contenteditable="false" on the parent column to make sure
no text can be added in that column and contenteditable="true" on the
images so that they are still editable (even though HTML-specs-wise
adding contenteditable="true" on images probably does not mean much as
images are self-closing tags, our editor understand that as the ability
to edit the image anyway). That contenteditable="true" part is however
removed when leaving edit mode... and was not restored upon entering
edit mode again.

This fixes the problems with an ugly patch. We'll review what to do in
master.

Funny enough, that bug was actually gone in 15.0... by mistake. A recent
bug fix actually reintroduced that isolated bug at [2] (by reintroducing
the fact that images in a non-editable environment are not possible to
edit). The 3 opened tickets this commit mentions were actually reported
for 15.0 immediately after that, while the 14.0 being broken about this
since the beginning apparently did not bother anyone.

[1]: https://github.com/odoo/odoo/commit/656cac1bf21c7c5a56aa569008aac58436c747fb
[2]: https://github.com/odoo/odoo/commit/e113bae04a64a8bd341a80736086ab7c25079dd3

opw-3031217
opw-3032482
opw-3035289

closes odoo/odoo#104156

Signed-off-by: Romain Derie (rde) <rde@odoo.com>

---
## [zzApotheosis/zzApotheosis](https://github.com/zzApotheosis/zzApotheosis)@[5e0432ecf7...](https://github.com/zzApotheosis/zzApotheosis/commit/5e0432ecf769eb2bb6868e8eee6529a496721ddd)
#### Tuesday 2023-07-11 13:25:50 by zzApotheosis

Removed Final Fantasy from HOF

I never really had the chance to enjoy FF as much as I probably should
have... If I can get someone to seriously persuade me to sit down and
give a FF game the time they think it deserves, then my opinion may very
well change. For now, it'll have to sit in my other list of games I've
enjoyed in the past, but haven't awarded my personal HOF honor.

---
## [knative-automation/kn-plugin-admin](https://github.com/knative-automation/kn-plugin-admin)@[fc0d4fe087...](https://github.com/knative-automation/kn-plugin-admin/commit/fc0d4fe087f20d5b3b869931da819baa96c37e15)
#### Tuesday 2023-07-11 14:14:19 by Knative Automation

upgrade to latest dependencies

bumping k8s.io/apiextensions-apiserver 2c55649...52c998e:%0A  > 52c998e Update dependencies to v0.26.5 tag%0A  > 186ff9b Merge pull request # 117274 from jkh52/release-1.26-knp-0.0.37%0A  > b7b18f5 Merge pull request # 117691 from dims/re-do-of-117242-on-release-1.26%0A  > ee5015a Bump konnectivity-client to 0.0.37%0A  > 9ce75f3 Bump runc go module v1.1.4 -> v1.1.6%0A  > e9d194a Merge pull request # 115599 from jkh52/release-1.26-knp-0.0.36%0A  > d7df0be Merge pull request # 115787 from liggitt/net-0.7.0-1.26%0A  > 9152c67 Bump konnectivity-client to v0.0.36%0A  > 89cec57 Update golang.org/x/net to v0.7.0%0A  > f72cc5c Merge pull request # 115642 from nckturner/pin-golang.org/x/net-to-v0.4.0-in-1.26%0A  > 28eb995 Pin golang.org/x/net to v0.4.0 in 1.26%0A  > 33db789 Merge pull request # 114861 from jpbetz/release-1.26%0A  > a06e03d Merge pull request # 114927 from jkh52/release-1.26-knp-metrics%0A  > 0859963 Cherry pick 114857 to release-1.26%0A  > 5183885 Bump konnectivity-client to v0.0.35%0A  > 6e13726 Merge remote-tracking branch 'origin/master' into release-1.26%0A  > c338f3e Update golang.org/x/net 1e63c2f%0A  > 9768bad sync: update go.mod%0A  > f9c2bba fix aggregated discovery version sorting%0A  > d2c9e18 Merge pull request # 113171 from Jefftree/aggregated-discovery-generic%0A  > 470c040 Merge pull request # 113577 from pacoxu/prometheus-client%0A  > 915a888 add crds to aggregated discovery%0A  > 92430b6 Merge pull request # 113314 from cici37/celIntegration%0A  > ac326ca upgrade prometheus-client to v1.14.0%0A  > 5a6bf16 Merge pull request # 113688 from dashpole/update_utils%0A  > 67b0610 Integrate cel admission with API.%0A  > 84fed82 upgrade github.com/prometheus/client_golang to v1.13.1%0A  > 077b441 update k8s.io/utils to fix util tracing panic%0A  > 5bbf20d Adding new api version of admissionregistration.k8s.io v1alpha1 for CEL in Admission Control%0A  > 3b533ba Merge pull request # 113367 from pohly/dep-ginkgo-gomega%0A  > 975bbeb dependencies: update to gomega v1.23.0 and ginkgo v2.4.0 and dependencies%0A  > ae2b4c3 Merge pull request # 112693 from aimuz/fix-GO-2022-0969%0A  > c4deae9 Fixed (CVE-2022-27664) Bump golang.org/x/net to v0.1.1-0.20221027164007-c63010009c80%0A  > bc4263f Merge pull request # 113172 from dashpole/endpoint_handler_tracing%0A  > f6c164e migrate apiserver utiltrace usage to component-base/tracing%0A  > 53e3726 Merge pull request # 113015 from ritazh/crencryption%0A  > c8d8a9f Enable encryption for custom resources%0A  > 6405068 Merge pull request # 113325 from panslava/fix-time-since-defer%0A  > 508e399 Fix time.Since() in defer. Wrap in anonymous function%0A  > 5f8e59e Merge pull request # 112691 from aimuz/apiextensions-apiserver-change-to-cmp%0A  > c996139 Merge pull request # 113106 from pohly/dep-ginkgo-gomega%0A  > f83e03c apiextensions-apiserver: change k8s.io/apimachinery/pkg/util/diff to github.com/google/go-cmp/cmp%0A  > b68fc51 dependencies: update to gomega v1.22.1 and ginkgo v2.3.1%0A  > 49c41b4 Merge pull request # 112988 from alexzielenski/update-kube-openapi%0A  > 3aaa2a0 Merge pull request # 113037 from pacoxu/fsnotify-v1.6.0%0A  > d9f6ebd update kube-openapi%0A  > 82e3ba4 Merge pull request # 112789 from enj/enj/r/kms_load_once_v2%0A  > 7423813 update fsnotify to v1.6.0%0A  > 8bf3487 Merge pull request # 113011 from jpmcb/cobra-1.6.0%0A  > d34393e Load encryption config once%0A  > 6ba582f Bumps cobra from 1.5.0 to 1.6.0%0A  > 8e0697b Merge pull request # 113022 from logicalhan/webhook-metrics%0A  > 90c63e0 Merge pull request # 112926 from jiahuif-forks/refactor/cel-out-of-apiextensions%0A  > 548c480 unparameterize 'webhook' from conversion metrics since it's the only one%0A  > 77badb8 Merge pull request # 112989 from ameukam/bump-golang.org/x/text-to-v0.3.8%0A  > 609e270 use DefaultMaxRequestSizeBytes for maxRequestSizeBytes.%0A  > 04f26fa Bump golang.org/x/text to v0.3.8%0A  > dd981e1 move CEL package to apiserver package.%0A  > 1644998 Move celopenapi/model to staging/src/k8s.io/apiextensions-apiserver/pkg/apiserver/schema/cel/ (# 109959)%0A  > 08d44e8 Merge pull request # 112875 from pohly/update-yaml%0A  > 1300140 dependencies: update to sigs.k8s.io/yaml v1.3.0%0A  > 5fb82bd Merge pull request # 112819 from thockin/no-make-generators%0A  > f5f5279 Codegens: Do not auto-set boilerplate path%0A  > f22ee73 Merge pull request # 112738 from liggitt/proto-tag%0A  > ba7f1b7 Merge pull request # 112689 from cheftako/master%0A  > 7ac7774 github.com/matttproud/golang_protobuf_extensions v1.0.2%0A  > e678457 Merge pull request # 112748 from wojtek-t/lock_ssa_gate%0A  > 0aca5a6 Bump konnectivity-client to v0.0.33%0A  > 9be4b4a Lock ServerSideApply feature to true%0A  > 7b53cb7 Merge pull request # 111980 from aramase/kms%0A  > f40a683 Merge pull request # 112705 from stevekuznetsov/skuznets/fix-comment%0A  > 4cd9125 Add staging directory for kms%0A  > d4e654a clients: clarify a misleading comment%0A  > 8b851d9 Merge pull request # 112673 from dims/update-to-latest-k8s.io/utils-sep-22%0A  > 362a89c Merge pull request # 112615 from mengjiao-liu/update_CRD_link%0A  > add0c80 Update to latest k8s.io/utils to pick up changes%0A  > 374216b Merge pull request # 112613 from dims/update-github.com/go-openapi/jsonreference-to-drop-github.com/PuerkitoBio/purell%0A  > a7ee7f9 Update `PreserveUnknownFields` field document link%0A  > 488bf20 update github.com/go-openapi/jsonreference to drop github.com/PuerkitoBio/purell%0A  > 47c15ca Merge pull request # 112588 from pacoxu/fsnotify-v1.5.4%0A  > d5b6243 Merge pull request # 112584 from dims/brneto-master%0A  > 8c6aa82 update fsnotify/fsnotify to v1.5.4%0A  > f8e18e9 run pin-dependency.sh and then hack/update-vendor.sh%0A  > c540c8c Merge pull request # 112545 from dims/update-etcd-3.5.5-and-all-otel-related-to-latest%0A  > 70b0d96 Merge pull request # 112352 from pohly/e2e-ginkgo-progress%0A  > 39cab0b updated etcd to v3.5.5 and newer otel libraries as well%0A  > 5faccda Merge pull request # 111866 from pacoxu/validate%0A  > 1c3fe9d e2e: bump ginkgo to v2.2.0%0A  > 917d446 Merge pull request # 112458 from dims/switch-to-release-tag-for-antlr-v1.4.10%0A  > 8b3fe74 add test case for array checking with dup values%0A  > 045fc90 Merge pull request # 112433 from ncdc/reduce-SchemaHas-allocs%0A  > 73cc883 Switch to release tag for antlr : v1.4.10%0A  > 22bcc66 added ratcheting validation for embedded resource and x-kubernetes-list-type validation%0A  > 269d73d Reduce allocations in HasSchemas%0A  > 7342cc6 Merge pull request # 112200 from pohly/client-go-shared-informer-factory-shutdown%0A  > aabbdff Merge pull request # 112349 from pohly/klog-update%0A  > fdf28bc client-go: support waiting for SharedInformerFactory shutdown%0A  > 6b7d12b build: update to klog v2.80.1%0A  > 559b4fa Merge pull request # 111768 from weilaaa/feature_add_symmetric_difference_in_sets_string%0A  > bf7d058 add symmetric difference in sets%0A  > 04ff81e Merge pull request # 112199 from pohly/klog-update%0A  > 87a4c3f dependencies: update to klog v2.80.0%0A  > 8f15690 Merge pull request # 112129 from pohly/e2e-ginkgo-report-after-each%0A  > f637e1c dependencies: update to ginkgo v2.1.6 and gomega v1.20.1%0A  > b6adc1c Merge pull request # 111964 from DangerOnTheRanger/cel-estimate-fix-update%0A  > ea2d438 Merge pull request # 112052 from tosi3k/bump-client-golang%0A  > 6b4dc0b Add unit tests.%0A  > 767e67b Bump prometheus/client_golang to v1.13.0%0A  > 782b982 Run pin-dependency.sh and update-vendor.sh.%0A  > 305963e Merge pull request # 111909 from tosi3k/bump-prom-client%0A  > fa2959a Merge pull request # 111830 from t1anz0ng/typo%0A  > 5a6ffec Bump prometheus/client_golang to v1.12.2%0A  > e0abc3b fix(typo): remove extra " from autoscaling doc string%0A  > 2184a8d Merge pull request # 111696 from liggitt/go119mod%0A  > f750907 Update go.mod to go1.19%0Abumping k8s.io/client-go 7226b15...6e9dabb:%0A  > 6e9dabb Update dependencies to v0.26.5 tag%0A  > 038b381 Merge pull request # 117691 from dims/re-do-of-117242-on-release-1.26%0A  > cd83e43 Bump runc go module v1.1.4 -> v1.1.6%0A  > dbfbc03 Merge pull request # 117686 from ardaguclu/automated-cherry-pick-of-# 117495-upstream-release-1.26%0A  > d72dec4 Use absolute path instead requestURI in openapiv3 discovery%0A  > a5144d4 Merge pull request # 117638 from seans3/automated-cherry-pick-of-# 117571-origin-release-1.26%0A  > d6f8d04 Refactors discovery content-type and helper functions%0A  > 2dd0093 Merge pull request # 115899 from odinuge/automated-cherry-pick-of-# 115620-upstream-release-1.26%0A  > f3ae5cb Merge pull request # 116666 from seans3/automated-cherry-pick-of-# 116603-origin-release-1.26%0A  > fffc68d Change where transformers are called.%0A  > 5ebee18 Aggregated discovery resilient to nil GVK%0A  > 8190aa4 client-go/cache: update Replace comment to be more clear%0A  > 87720b3 Merge pull request # 116437 from seans3/automated-cherry-pick-of-# 116145-# 115865-origin-release-1.26%0A  > b667227 client-go/cache: rewrite Replace to check queue first%0A  > fc13749 Removes old discovery hack ignoring 403 and 404%0A  > 30215cd client-go/cache: merge ReplaceMakesDeletionsForObjectsInQueue tests%0A  > f39ba12 Plumb stale GroupVersions through aggregated discovery%0A  > ba35969 client-go/cache: fix missing delete event on replace without knownObjects%0A  > f538edf Merge pull request # 116352 from seans3/automated-cherry-pick-of-# 115978-origin-release-1.26%0A  > 97cf9cb client-go/cache: fix missing delete event on replace%0A  > 5dbbc58 Tolerate empty discovery response in memcache client%0A  > 62133a9 Merge pull request # 115787 from liggitt/net-0.7.0-1.26%0A  > 8ce239f Update golang.org/x/net to v0.7.0%0A  > e6bc0bc Merge pull request # 115566 from enj/automated-cherry-pick-of-# 115315-upstream-release-1.26%0A  > 9112e19 Merge pull request # 115400 from pohly/automated-cherry-pick-of-# 115354-origin-release-1.26%0A  > 0519b53 kubelet/client: collapse transport wiring onto standard approach%0A  > 2e34348 Merge pull request # 115642 from nckturner/pin-golang.org/x/net-to-v0.4.0-in-1.26%0A  > 7be38cd dynamic resource allocation: avoid apiserver complaint about list content%0A  > 4968c4a Pin golang.org/x/net to v0.4.0 in 1.26%0A  > 0c34939 Merge pull request # 114617 from JoelSpeed/automated-cherry-pick-of-# 114585-upstream-release-1.26%0A  > 04b098b Resource claims should be a map type%0A  > b3fff46 Merge pull request # 114415 from hoskeri/automated-cherry-pick-of-# 114404-upstream-release-1.26%0A  > 236db3c Merge pull request # 113988 from liggitt/automated-cherry-pick-of-# 113933-upstream-release-1.26%0A  > a2ef324 Check the correct error in d.downloadAPIs%0A  > 95a14c3 Merge remote-tracking branch 'origin/master' into release-1.26%0A  > ebb499f Limit request retrying to []byte request bodies%0A  > 1a7cd1d Update golang.org/x/net 1e63c2f%0A  > 53f2fea sync: update go.mod%0A  > 968ba8d Merge pull request # 113797 from seans3/force-no-aggregated%0A  > c8ffed3 Merge pull request # 111023 from pohly/dynamic-resource-allocation%0A  > 3ac73ea Adds bool to force non-aggregated discovery%0A  > 61cd728 Merge pull request # 113826 from jsafrane/add-openstack%0A  > 522eaa1 api: generated files%0A  > cfd682c Merge pull request # 113375 from atiratree/PodHealthyPolicy-api%0A  > f2b10f3 Remove OpenStack cloud provider%0A  > acc9fa7 Merge pull request # 113186 from ttakahashi21/KEP-3294%0A  > f1c80d7 generated%0A  > a3d3eb0 Revert "Remove references to openstack and cinder"%0A  > c7bdab2 Generate code%0A  > 0a1f6a8 Merge pull request # 112744 from pwschuurman/statefulset-slice-impl%0A  > 1c7a870 Merge pull request # 113485 from MikeSpreitzer/apf-borrowing%0A  > eed2516 Adding implementation of KEP-3335, StatefulSetSlice%0A  > 7280270 Merge pull request # 113599 from seans3/discovery-client-update%0A  > d4a3675 apiserver: add generated files for borrowing in flowcontrol%0A  > 7694435 Update redacting functionality to redact all sensitive info in config when printing with view (# 109189)%0A  > 25d5761 Aggregated discovery client%0A  > 4b1a9fd Merge pull request # 113314 from cici37/celIntegration%0A  > ea9ec91 Merge pull request # 112905 from alexzielenski/kubectl-apply-csa-migration%0A  > 3a430a4 API - make update%0A  > 3daf180 Merge pull request # 113688 from dashpole/update_utils%0A  > 898b7a3 add FindFieldsOwners util function%0A  > dbe034b update k8s.io/utils to fix util tracing panic%0A  > 4f63b62 add UpgradeManagedFieldsPatch%0A  > 7ed3193 Merge pull request # 111545 from jlsong01/rewrite_signature_of_StartEventWatcher%0A  > c8c6cb5 add OWNERS to csaupgrade%0A  > cbe28cf Merge pull request # 113274 from Huang-Wei/kep-3521-A%0A  > 3467961 rewrite signature of function StartEventWatcher%0A  > a45874a remove kubectl annotation logic from upgrade patch%0A  > 2248bf3 Automated codegen%0A  > d576a35 Merge pull request # 113387 from wojtek-t/refactor_client_indexing%0A  > 4fbef5b Merge pull request # 106242 from thockin/revive-copy-lb-status-type-to-ingress%0A  > 5e7ba1f Minor cleanup of thread safe store%0A  > bc6266d Merge pull request # 103177 from arkbriar/support_cancelable_exec_stream%0A  > 3f162fe Copy LoadBalancerStatus from core to networking%0A  > b69a16c Refactor store index into its structure%0A  > 19b2e89 Merge pull request # 113523 from seans3/content-type-response%0A  > 0563dec Propagate the panic with a channel%0A  > 8ff4970 Get response content-type%0A  > 2362c7b use subtests and defer in TestSPDYExecutorStream%0A  > 0d57396 Merge pull request # 113304 from mimowo/handling-pod-failures-beta-ssa%0A  > 5e0a531 Support cancelable SPDY executor stream%0A  > a232cf0 Merge pull request # 113367 from pohly/dep-ginkgo-gomega%0A  > a191e58 SSA to add pod failure conditions - ready for review%0A  > 984bdbf dependencies: update to gomega v1.23.0 and ginkgo v2.4.0 and dependencies%0A  > f87d047 Merge pull request # 112693 from aimuz/fix-GO-2022-0969%0A  > d236783 Fixed (CVE-2022-27664) Bump golang.org/x/net to v0.1.1-0.20221027164007-c63010009c80%0A  > ef8a2e5 Merge pull request # 113089 from zackzhangkai/fix-doc%0A  > 197e479 Merge pull request # 108959 from astraw99/fix-duplicate-list%0A  > 0945beb fix typo%0A  > 42a0e1c Merge pull request # 113062 from alexzielenski/client-go-json-output%0A  > f549acf Fix duplicate code block of ListAll function%0A  > b6d3c8d Merge pull request # 107278 from harsimranmaan/allow_pagination_in_dynamic_fake_lister%0A  > 624929c address feedback%0A  > 9cc33a4 Merge pull request # 113106 from pohly/dep-ginkgo-gomega%0A  > 0c269b7 remove selflink as per review feedback%0A  > 12cafe2 refactor to use Schema(contentType)%0A  > 9b51067 dependencies: update to gomega v1.22.1 and ginkgo v2.3.1%0A  > fbd8e9a fix failing test assertions%0A  > 8b6ceae add more options for fetching openapiv3 in clients%0A  > fa9ed7f Merge pull request # 112860 from nckturner/remove-log-line%0A  > 1f10368 Preserve metadata for fake dynamic client unstructured lists%0A  > 6b24912 Merge pull request # 112988 from alexzielenski/update-kube-openapi%0A  > 5870c62 Remove log line from expiration cache%0A  > aea20dd Merge pull request # 113037 from pacoxu/fsnotify-v1.6.0%0A  > e3bb48f update kube-openapi%0A  > 1af3711 update fsnotify to v1.6.0%0A  > e6d958c Merge pull request # 112989 from ameukam/bump-golang.org/x/text-to-v0.3.8%0A  > 5e469ba Bump golang.org/x/text to v0.3.8%0A  > f515a4c Merge pull request # 112774 from stevekuznetsov/skuznets/dynamic-client-similar%0A  > b28f6c9 Merge pull request # 112875 from pohly/update-yaml%0A  > 34e8a5d client-go: factor the dynamic client similarly to others%0A  > c9afc73 dependencies: update to sigs.k8s.io/yaml v1.3.0%0A  > f24bd69 Merge pull request # 112306 from tkashem/v1beta3%0A  > ebc7cd4 Merge pull request # 112707 from enj/enj/i/https_links%0A  > 9b97b72 rename assuredConcurrencyShares for flowcontrol v1beta3%0A  > 2f43d37 Merge pull request # 112705 from stevekuznetsov/skuznets/fix-comment%0A  > 1665808 Use https links for k8s KEPs, issues, PRs, etc%0A  > 9bac803 apiserver: generate for apf v1beta3%0A  > 3697342 Merge pull request # 112680 from enj/enj/i/tls_cache_key_comparable%0A  > 956c1ce clients: clarify a misleading comment%0A  > c81636c Merge pull request # 112665 from NoicFank/fix-typo%0A  > cc2441c transport/cache: statically assert that tlsCacheKey is comparable%0A  > be20b2b Merge pull request # 112673 from dims/update-to-latest-k8s.io/utils-sep-22%0A  > 59765b8 fix typo error%0A  > 04dbcd8 Update to latest k8s.io/utils to pick up changes%0A  > 2fd4aac Merge pull request # 112613 from dims/update-github.com/go-openapi/jsonreference-to-drop-github.com/PuerkitoBio/purell%0A  > 47ad72a update github.com/go-openapi/jsonreference to drop github.com/PuerkitoBio/purell%0A  > f7c9c63 Merge pull request # 112545 from dims/update-etcd-3.5.5-and-all-otel-related-to-latest%0A  > b6e72dc Merge pull request # 112226 from aojea/client_go_transport%0A  > 6b5ecad updated etcd to v3.5.5 and newer otel libraries as well%0A  > acfaa39 Merge pull request # 112352 from pohly/e2e-ginkgo-progress%0A  > 1bd914a client-go: test transport generation is goroutine safe%0A  > 037b5fd Merge pull request # 112514 from markmc/patch-1%0A  > ec6c80a e2e: bump ginkgo to v2.2.0%0A  > 3f66212 client-go: remove reference to TPR in examples%0A  > 86ffa32 Merge pull request # 112475 from vatsalparekh/fix-TestRESTClientLimiter%0A  > ece6462 Merge pull request # 112476 from enj/enj/i/list_pager_flake%0A  > bf2b395 Fix Infelicities in TestRESTClientLimiter%0A  > 58155b7 Merge pull request # 112450 from enj/enj/i/exec_tls_cache_holder_cleanup%0A  > 6703098 Check for context cancellation on each buffered chunk%0A  > eecd3e5 Merge pull request # 112091 from xyz-li/master%0A  > 5dab9a0 client-go/transport: drop Dial and GetCert fields in favor of Holders%0A  > f6b8521 Merge pull request # 111333 from flant/selfsubjectattributesreviews%0A  > cc3cc93 kubectl: fix memory leaks in port forwarding client%0A  > b2b55e6 Add auth API to get self subject attributes%0A  > 18c3338 Merge pull request # 112200 from pohly/client-go-shared-informer-factory-shutdown%0A  > 9dae691 Merge pull request # 112309 from shyamjvs/disable-compression%0A  > ec4fedd client-go: support waiting for SharedInformerFactory shutdown%0A  > ab826d2 Merge pull request # 112349 from pohly/klog-update%0A  > 49ac40b Autogen code%0A  > ab0bfda build: update to klog v2.80.1%0A  > b8a8d94 Add DisableCompression option to KubeConfig%0A  > f32861c Merge pull request # 112341 from enj/enj/i/second_time_is_the_charm%0A  > 7d208ba Remove in-tree credential plugins (again)%0A  > e003fa9 Merge pull request # 112017 from enj/enj/i/exec_tls_cache%0A  > 2698e82 Merge pull request # 111967 from alexzielenski/csa-to-ssa%0A  > 6a008ec exec auth: support TLS config caching%0A  > 27c67e7 Merge pull request # 111122 from alexzielenski/informer%0A  > 00d892f correct spacing%0A  > d28c736 Merge pull request # 112022 from JackZxj/release-lock%0A  > a300ae0 return when test is done%0A  > 2efbeaf add boilerplate%0A  > b8b6206 Merge pull request # 112199 from pohly/klog-update%0A  > d04c2ce update lock getter of leaderelection%0A  > 93e5e0e hold listener lock while waiting for goroutines to finish%0A  > dac0826 remove inaccurate comment%0A  > 5a2c3e9 dependencies: update to klog v2.80.0%0A  > e11a988 simplify control flow%0A  > 7634f2e make upgrade modify input instead of deep copying%0A  > 7ccf7b0 Merge pull request # 112134 from apelisse/client-go-valid-segment%0A  > ac7f657 fix spelling%0A  > 9aa7c11 remove fieldsv1 from upgrade body%0A  > d83ec9e Merge pull request # 112129 from pohly/e2e-ginkgo-report-after-each%0A  > a4b84d8 Validate segments with client-go/dynamic%0A  > 0f4a6cf reset listenersStarted%0A  > 703d15e Update staging/src/k8s.io/client-go/util/csaupgrade/upgrade.go%0A  > cac10a8 dependencies: update to ginkgo v2.1.6 and gomega v1.20.1%0A  > 449817f add multithreaded test to shared informer%0A  > 675ca93 refactor if statement%0A  > 46d4284 Merge pull request # 111241 from Abirdcfly/fixtestorsource%0A  > de0b767 remove duplicate test%0A  > cfaca90 address comments%0A  > bdae576 Merge pull request # 112068 from aojea/aojea_client_go%0A  > 9b300de make TestListPager_EachListItem rework%0A  > 0565962 address review comments%0A  > 089614c remove last applied configuration information%0A  > fd22687 add aojea as client-go reviewer%0A  > 5a25eb0 switch listeners to use a map, adapt tests%0A  > efe3789 add more test cases%0A  > 35ead05 Merge pull request # 112052 from tosi3k/bump-client-golang%0A  > 90c6a46 active remove/add tests for event handlers%0A  > 46dc22f clean up test%0A  > 5291ca2 Bump prometheus/client_golang to v1.13.0%0A  > de4dd3a tests for invalid registration removals%0A  > ced85a8 update godoc%0A  > e6538dd Merge pull request # 112024 from cndoit18/remove-redundant-judgment%0A  > 33eff64 apply desired changes for handler registration%0A  > 049ba69 expose FieldsToSet and SetToFields%0A  > bcd2e6c style: remove redundant judgment%0A  > d73e40f rename handle to registration%0A  > aa892ab remove  unused code%0A  > d5e5863 Merge pull request # 111752 from aanm/revert-final-url-template%0A  > b3a61c6 remove informational informer methods again%0A  > 90ef078 dont expose internal methods in implementatoin%0A  > 5feaced Merge pull request # 67782 from dims/yank-in-tree-openstack-cloud-provider%0A  > e9d4627 client-go/rest: check if url is nil to prevent nil pointer dereference%0A  > ecdc8bf support removal of event handlers from SharedIndexInformers%0A  > c364b63 add function to upgrade managedfields CSA to SSA%0A  > 0fdc4f3 Merge pull request # 111684 from 0xff-dev/master1%0A  > 98e81a7 Remove references to openstack and cinder%0A  > c501ee0 Revert "client-go: remove no longer used finalURLTemplate"%0A  > 4faffa8 Merge pull request # 111564 from inosato/remove-ioutil-from-cli-client-go%0A  > c94a539 use constant NamespaceDefault instead of variable namespace%0A  > 2e40408 Merge pull request # 111918 from liggitt/in-tree-auth%0A  > 27de641 Remove ioutil from client-go%0Abumping google.golang.org/grpc 1c29e07...5b67e5e:%0A  > 5b67e5e Update version.go to v1.56.1 (# 6386)%0A  > d0f5150 client: handle empty address lists correctly in addrConn.updateAddrs (# 6354) (# 6385)%0A  > 997c1ea Change version to 1.56.1-dev (# 6345)%0A  > 2b6ff72 Change version to 1.56.0 (# 6344)%0A  > 7996425 xds/outlierdetection: fix config handling (# 6361) (# 6367)%0A  > a5ae5c6 weightedroundrobin: cherry-pick 2 commits from master (# 6360)%0A  > 8edfa1a authz: End2End test for AuditLogger (# 6304)%0A  > 2b1d70b xds: enable RLS in xDS by default (# 6343)%0A  > 47f8ed8 interop: Don't fail target if sub-target already failed (# 6332)%0A  > 1f23f6c client: fix Connect to handle channel idleness properly (# 6331)%0A  > 3ea58ce client: disable channel idleness by default (# 6328)%0A  > 6c2529b xds: support pick_first custom load balancing policy (A62) (# 6314)%0A  > 9b9b364 internal/envconfig: Set Custom LB Env Var to true by default (# 6317)%0A  > e325737 alts: Fix flaky ALTS TestFullHandshake test. (# 6300)%0A  > 4d3f221 xds/internal/xdsclient: Add support for String Matcher Header Matcher in RDS (# 6313)%0A  > 157db19 stats/opencensus: Fix flaky test span (# 6296)%0A  > f19266c xds: support built-in Stdout audit logger type (# 6298)%0A  > 59134c3 client: add support for pickfirst address shuffling from gRFC A62 (# 6311)%0A  > a6e1acf grpc: support sticky TF in pick_first LB policy (# 6306)%0A  > 2ae10b2 xdsclient: remove interface check related to ResourceData (# 6308)%0A  > e9799e7 client: support a 1:1 mapping with acbws and addrConns (# 6302)%0A  > 2a266e7 authz: use pointer to to structpb.Struct instead of value (# 6307)%0A  > 511a963 interop: let the interop client send additional metadata, controlled by a flag (# 6295)%0A  > 9b7a947 grpc: support channel idleness (# 6263)%0A  > 098b2d0 xds/internal/balancer/outlierdetection: Switch Outlier Detection to use new duration field (# 6286)%0A  > 417d4b6 examples: add error_handling example; move errors to error_details (# 6293)%0A  > 390c392 authz: Rbac engine audit logging (# 6225)%0A  > 52fef6d authz: Stdout logger (# 6230)%0A  > 92e65c8 test/kokoro: Add custom_lb_test to the xds_k8s_lb job (# 6290)%0A  > 756119c  xds/outlierdetection: forward metadata from child picker (# 6287)%0A  > 8eba9c2 github: upgrade to v3 of checkout & setup-go (# 6280)%0A  > 24fd252 proto: update generated code to match grpc-proto changes (# 6283)%0A  > 4eb88d7 cleanup: use new Duration type in base ServiceConfig (# 6284)%0A  > 1230f0e xds/internal/xdsclient: Split registry up and two separate packages (# 6278)%0A  > 0bdae48 interop: fix interop_test.sh shutdown (# 6279)%0A  > 5dcfb37 interop: hold lock on server for OOB metrics updates; share 30s timeout (# 6277)%0A  > 68381e7 xds: WRR in xDS (# 6272)%0A  > fd376a5 test: fix flaky TimeoutOnDeadServer test; some cleanups (# 6276)%0A  > 1db474c weightedroundrobin: fix duration format in lb config (# 6271)%0A  > 523dcdd weightedroundrobin: fix test race accessing timeNow (# 6269)%0A  > 1536887 interop/xds: Add Custom LB needed for interop test (# 6262)%0A  > 7d61344 examples: fix authz example to receive streaming error properly (# 6270)%0A  > afcbdc9 xds/internal/xdsclient/xdslbregistry: Continue in converter if type not found (# 6268)%0A  > b3fbd87 interop: add ORCA test cases and functionality (# 6266)%0A  > 5e58734 xds: Add support for Custom LB Policies (# 6224)%0A  > 5c4bee5 balancer/weightedroundrobin: add load balancing policy (A58) (# 6241)%0A  > c44f77e grpc: use CallbackSerializer in balancer wrapper (# 6254)%0A  > f193ec0 orca: fix race when calling listeners coincides with updating the run goroutine (# 6258)%0A  > 417cf84 test: deflake TestBalancerProducerHonorsContext (# 6257)%0A  > 1f3fe1c Update ClientStream.SendMsg doc (# 6247)%0A  > ccad7b7 grpc: use CallbackSerializer in resolver_wrapper (# 6234)%0A  > 47b3c55 orca: fix race at producer startup (# 6245)%0A  > 56b33d5 server/transport: send appropriate debug_data in GOAWAY frames (# 6220)%0A  > add9015 orca: allow a ServerMetricsProvider to be passed to the ORCA service and ServerOption (# 6223)%0A  > 40d0147 googledirectpatph: enable ignore_resource_deletion in bootstrap (# 6243)%0A  > ed3ceba balancer: make producer RPCs block until the SubConn is READY (# 6236)%0A  > b153b00 multiple: standardize import renaming for typed structs (# 6238)%0A  > 713bd04 orca: minor cleanups (# 6239)%0A  > 21a339c grpc: handle RemoveSubConn inline in balancerWrapper (# 6228)%0A  > b153827 xds: make glaze happy for test packages (# 6237)%0A  > 019acf2 stubserver: add option for allowing more services to be registered (# 6240)%0A  > cf89a0b authz: Swap to using the correct TypedConfig in audit logger parsing (# 6235)%0A  > df82147 internal: Document gcp/observability 1.0 dependencies in /internal (# 6229)%0A  > da1a5eb tests: nix TestClientDoesntDeadlockWhileWritingErroneousLargeMessages (# 6227)%0A  > e853dbf authz: add conversion of json to RBAC Audit Logging config (# 6192)%0A  > 497436c xds/internal/balancer/outlierdetection: Change string to String (# 6222)%0A  > de11139 clusterresolver: improve tests (# 6188)%0A  > eff0942 xds/internal/xdsclient: Custom LB xDS Client Changes (# 6165)%0A  > 8628e07 xds/internal/balancer/outlierdetection: Add Channelz Logger to Outlier Detection LB (# 6145)%0A  > 83c460b authz: Move audit package (# 6218)%0A  > 8c70261 grpc: ClientConn cleanup in prep for channel idleness (# 6189)%0A  > 2cd95c7 gcp/observability: remove redundant import (# 6215)%0A  > 16651f6 go.mod: update all dependencies (# 6214)%0A  > ca60462 stubserver: Stop server when StartClient failed (# 6190)%0A  > 7dfd718 internal/buffer: add Close method to the Unbounded buffer type (# 6161)%0A  > ebeda75 tests: defalke TestTimerAndWatchStateOnSendCallback (# 6206)%0A  > 0ed709c Change version to 1.56.0-dev (# 6213)%0A  > 875c97a examples/features/observability: use observability module v1.0.0 (# 6210)%0A  > aa8c137 authz: add audit logging APIs (# 6158)%0A  > b91b884 gcp/observability: Have o11y module point to grpc 1.54 and opencensus 1.0.0 (# 6209)%0A  > eab9e20 test/kokoro: increase PSM Security test timeout to 4h (# 6193)%0A  > d90621f remove the unnecessary call to ResetTimer and StopTimer (# 6185)%0A  > fe72db9 testing: add helpers to start test service, and retrieve port (# 6187)%0A  > 5a50b97 Revert "Revert "credentials/alts: defer ALTS stream creation until handshake …" (# 6179)%0A  > 89ec960 grpc: read the service config channel once instead of twice (# 6186)%0A  > 6237dfe internal/stubserver: Close Client Conn in error handling of Start (# 6174)%0A  > 06de8f8 alts: Add retry loop when making RPC in ALTS's TestFullHandshake. (# 6183)%0A  > 6eabd7e server: use least-requests loadbalancer for workers (# 6004)%0A  > 8374ff8 Export the unwrapResource method, to allow callers outside of the package (# 6181)%0A  > efb2f45 test/xds: Fix test_grpc import path (# 6180)%0A  > 81b3092 security/advancedtls: add TlsVersionOption to select desired min/max TLS versions (# 6007)%0A  > 17b693d alts: Perform full handshake in ALTS tests. (# 6177)%0A  > 01f8b86 Add documentation on some anti-patterns (# 6034)%0A  > 3489bb7 xdsclient/test: deflake TestWatchResourceTimerCanRestartOnIgnoredADSRecvError (# 6159)%0A  > bfb57b8 testing: delete internal copy of test service proto, and use canonical one (# 6164)%0A  > 10401b9 stats/opencensus: the backend to Sent. Attempt. and Recv. (# 6173)%0A  > b0a8b1b Use string instead of enum for xds resource type (# 6163)%0A  > 1d5b73a xds: add stop to avoid hanging in TestServeWithStop (# 6172)%0A  > ea0a038 xds/xdsclient: ignore resource deletion as per gRFC A53 (# 6035)%0A  > a51779d xdsclient/test: deflake TestTimerAndWatchStateOnSendCallback (# 6169)%0A  > e979919 internal/grpcsync: move CallbackSerializer from xdsclient/internal to here (# 6153)%0A  > c2899dd examples/features/observability: Point o11y example to latest gcp/observability module (# 6162)%0A  > 113d75f gcp/observability: Add isSampled bool to log entries (# 6160)%0A  > 4a12595 stats/opencensus: Switch helper to return Span Context from context (# 6156)%0A  > c3f1d5e gcp/observability: Set the opencensus_task label only for metrics, not tracing and logging (# 6155)%0A  > 42dd7ac Use anypb.New instead of ptypes.MarshalAny (# 6074)%0A  > 415ccdf go.mod: update all dependencies after 1.54 branch cut (# 6132)%0A  > a357baf status: FromError: return entire error message text for wrapped errors (# 6150)%0A  > 44cebb8 xds: enable XDS federation by default (# 6151)%0A  > c018273 examples: Add observability example (# 6149)%0A  > 277bb64 Revert "credentials/alts: defer ALTS stream creation until handshake time (# 6077)" (# 6148)%0A  > 0fdfd40 gcp/observability: Generate unique process identifier unconditionally (# 6144)%0A  > 1d20f1b security/advancedtls: swap from deprecated pkix.CertificateList to x509.RevocationList (# 6054)%0A  > a8a25ce transport: use prefix logging (# 6135)%0A  > 9c25653 cdsbalancer: improve log messages (# 6134)%0A  > a02aae6 CONTRIBUTING.md: remove duplicated bullet point (# 6139)%0A  > cdab8ae clusterresolver: push empty config to child policy upon removal of cluster resource (# 6125)%0A  > 7651e62 transport: add a draining state check before creating streams (# 6142)%0A  > a2ca46c examples: organize READMEs better (# 6121)%0A  > 4efec30 stats/opencensus: remove leading slash for per call metrics (# 6141)%0A  > 78099db gcp/observability: Switch hex encoding to string() method (# 6138)%0A  > 70c5291 observability: remove import replace directive and switch it to point to latest commit (# 6122)%0A  > 66e3533 status: handle wrapped errors (# 6031)%0A  > a75fd73 Change version to 1.55.0-dev (# 6131)%0A  > b638faf stats/opencensus: Add message prefix to metrics names (# 6126)%0A  > c84a500 credentials/alts: defer ALTS stream creation until handshake time (# 6077)%0A  > 6f44ae8 metadata: add benchmark test for FromIncomingContext and ValueFromIncomingContext (# 6117)%0A  > a1e657c client: log last error on subchannel connectivity change (# 6109)%0A  > 36fd0a4 gcp/observability: Add compressed metrics to observability module and synchronize View data with exporter (# 6105)%0A  > 52ca957 xds: make comparison of server configs in bootstrap more reliable (# 6112)%0A  > 7507ea6 gcp/observability: Change logging schema and set queue size limit for logs and batching delay (# 6118)%0A  > 16c3b7d examples: add example for ORCA load reporting (# 6114)%0A  > b458a4f transport: stop always closing connections when loopy returns (# 6110)%0A  > 11e2506 tests: Scale down keepalive test timings (# 6088)%0A  > 5796c40 interop/observability: Pass interop parameters to client/server as-is (# 6111)%0A  > abd4db2 xdsclient/tests: fix flaky test NodeProtoSentOnlyInFirstRequest (# 6108)%0A  > 3633361 tests: support LRS on the same port as ADS (# 6102)%0A  > 0558239 Update CONTRIBUTING.md (# 6089)%0A  > 2260821 go.mod: upgrade golang.org/x/net to address CVE-2022-41723 (# 6106)%0A  > 60a1aa3 testutils: add support for creating endpoint resources with options (# 6103)%0A  > 92d9e77 xds: NACK route configuration if sum of weights of weighted clusters exceeds uint32_max (# 6085)%0A  > d02039b Deflake the integration test. (# 6093)%0A  > 55d8783 gcp/observability: Link logs and traces by logging Trace and Span IDs (# 6056)%0A  > ad4057f transport: stop returning errors that are always nil (# 6098)%0A  > 558e1b6 examples/authz: add token package docstring (# 6095)%0A  > 33df9fc credentials/xds: improve error message upon SAN matching failure (# 6080)%0A  > 3292193 xdsclient: handle race with watch timer handling (# 6086)%0A  > e83e34b xds/resolver/test: use a non-blocking send instead of closing the channel (# 6082)%0A  > b46bdef interop/observability: add GCP Observability Testing Client/Server (# 5979)%0A  > f311684 stats/opencensus: New uncompressed metrics and align with tracing spec (# 6051)%0A  > cc320bf grpc: Log server trailers before writing status (# 6076)%0A  > b9e6d59 xdsclient: send Node proto only on first discovery request on ADS stream (# 6078)%0A  > ae4a231 ringhash: ensure addresses are consistenly hashed across updates (# 6066)%0A  > 52dcd14 xdsclient: move tests from `e2e_test` to `tests` directory (# 6073)%0A  > d8f80bb stats/opencensus: Added client api latency and upgrade go.mod (# 6042)%0A  > a8b3226 gcp/observability: Disable logging and traces on channels to cloud ops backends (# 6022)%0A  > 20141c2 examples: add an example to illustrate authorization (authz) support (# 5920)%0A  > 8c374f7 clusterresolver: cleanup resource resolver implementation (# 6052)%0A  > 1d16ef5 metadata: Lowercase appended metadata (# 6071)%0A  > 8ba23be cmd/protoc-gen-go-grpc: bump -version to 1.3.0 for release (# 6064)%0A  > a1693ec fakeserver: remove ADS and LRS v2 support (# 6068)%0A  > 832ecc2 channelz: use protocmp.Transform() to compare protos (# 6065)%0A  > 28b6bcf xds/xdsclient: improve failure mode behavior (gRFC A57) (# 5996)%0A  > d53f0ec test: move compressor tests out of end2end_test.go (# 6063)%0A  > dba41ef metadata: fix validation issues (# 6001)%0A  > 75bed1d test: move e2e health checking tests out of end2end_test.go (# 6062)%0A  > 0586c51 internal/transport: reduce running time of test from 5s to 1s (# 6061)%0A  > 7437662 internal/transport: Fix flaky keep alive test (# 6059)%0A  > 681b133 admin/test: split channelz imports (# 6058)%0A  > 1093d3a channelz: remove dependency on testing package (# 6050)%0A  > 3775f63 xdsclient/transport: reduce chattiness of logs (# 5992)%0A  > 6fe609d xdsclient: minor cleanup in eds parsing (# 6055)%0A  > 5353eaa testing: add helpers to configure cluster specifier plugin type (# 5977)%0A  > 8702a2e stats/opencensus: Add top level call span (# 6030)%0A  > 85b95dc gcp/observability: Register new views (# 6026)%0A  > abff344 stats/opencensus: Add per call latency metric (# 6017)%0A  > 0f02ca5 gcp/observability: Switch observability module to use new opencensus instrumentation code (# 6021)%0A  > 6d612a3 resolver: update Resolver.Scheme() docstring to mention requirement of lowercase scheme names (# 6014)%0A  > 30d8c0a xds/internal/xdsclient: NACK empty clusters in aggregate clusters (# 6023)%0A  > 081499f xds: remove support for v2 Transport API (# 6013)%0A  > dd12def stats/opencensus: Add OpenCensus traces support (# 5978)%0A  > f4feddb github: update tests to use go version 1.20 (# 6020)%0A  > 8153410 client: Add dial option to disable global dial options (# 6016)%0A  > 55dfae6 resolver: document handling UpdateState errors by resolvers (# 6002)%0A  > ceb3f07 client: Revert dialWithGlobalOption (# 6012)%0A  > d655f40 internal/transport: fix severity of log when receiving a GOAWAY with error code ENHANCE_YOUR_CALM (# 5935)%0A  > b81e8b6 metadata: slightly improve operateHeaders (# 6008)%0A  > e9d9bd0 tests: reduce the degree of stress testing in long running tests (# 6003)%0A  > f855226 github: update codeQL action to v2 (# 6009)%0A  > f69e9ad stats/opencensus: Add OpenCensus metrics support (# 5923)%0A  > 3151e83 cmd/protoc-gen-go-grpc: export consts for full method names (# 5886)%0A  > d6dabba xds/server: reduce chattiness of logs (# 5995)%0A  > 0954097 server: expose API to set send compressor (# 5744)%0A  > a7058f7 xds/csds: switch tests to use the new generic xdsclient API (# 6000)%0A  > 3711154 xdsclient/bootstrap: reduce chattiness of logs (# 5991)%0A  > d103fc7 xdsclient/xdsresource: reduce chattiness of logs (# 5993)%0A  > 6a707eb client: add an option to disable global dial options (# 5990)%0A  > c813c17 Change version to 1.54.0-dev (# 5985)%0A  > 2a1e934 server: after GracefulStop, ensure connections are closed when final RPC completes (# 5968)%0A  > e2d69aa tests: fix spelling of variable (# 5966)%0A  > a6376c9 xds/resolver: cleanup tests to use real xDS client 3/n (# 5953)%0A  > bf8fc46 xds/resolver: cleanup tests to use real xDS client 5/n (# 5955)%0A  > 3930549 resolver: replace resolver.Target.Endpoint field with Endpoint() method (# 5852)%0A  > 894816c grpclb: rename `grpclbstate` package back to `state` (# 5962)%0A  > e5a0237 encoding: fix duplicate compressor names (# 5958)%0A  > 4adb2a7 xds/resolver: cleanup tests to use real xDS client 2/n (# 5952)%0A  > 52a8392 gcp/observability: update method name validation (# 5951)%0A  > 4075ef0 xds: fix panic involving double close of channel in xDS transport (# 5959)%0A  > 7bf6a58 gcp/observability: Cleanup resources allocated if start errors (# 5960)%0A  > bc9728f xds/resolver: cleanup tests to use real xDS client 4/n (# 5954)%0A  > 6e74938 xds/resolver: cleanup tests to use real xDS client (# 5950)%0A  > 9b9b381 server: fix a few issues where grpc server uses RST_STREAM for non-HTTP/2 errors (# 5893)%0A  > ace8082 xdsclient: close func refactor (# 5926)%0A  > 9326362 transport: fix maxStreamID to align with http2 spec (# 5948)%0A  > 4e4d828 xds interop: Fix buildscripts not continuing on a failed test suite (# 5937)%0A  > 379a2f6 *: add missing colon to errorf messages to improve readability (# 5911)%0A  > cde2edc Revert "xds interop: Fix buildscripts not continuing on a failed test suite (# 5932)" (# 5936)%0A  > 78ddc05 xdsclient: fix race in load report implementation (# 5927)%0A  > 2a9e970 xds interop: Fix buildscripts not continuing on a failed test suite (# 5932)%0A  > 9228cff rls: fix a data race involving the LRU cache (# 5925)%0A  > be06d52 binarylog: consistently rename imports for binarylog proto (# 5931)%0A  > bf3ad35 *: update all dependencies (# 5924)%0A  > 6de8f50 transport: drain client transport when streamID approaches maxStreamID (# 5889)%0A  > 42b7b63 stats/opencensus: OpenCensus instrumentation api (# 5919)%0A  > 974a5ef grpc: document defaults in MaxCallMsgSize functions (# 5916)%0A  > 9b73c42 test/xds: add tests for scenarios where authority in resource name is not specified in bootstrap config (# 5890)%0A  > 3b2da53 xdsclient: handle resource not found errors correctly (# 5912)%0A  > f2fbb0e Deprecate use of `ioutil` package (# 5906)%0A  > 8ec85e4 priority: improve and reduce verbosity of logs (# 5902)%0A  > 12b8fb5 test: move e2e HTTP header tests to http_header_end2end_test.go (# 5901)%0A  > f1a9ef9 stream: update ServerStream.SendMsg doc (# 5894)%0A  > c90744f oauth: mark `NewOauthAccess` as deprecated and update examples to use `TokenSource` (# 5882)%0A  > 0e5421c internal/envconfig: add convenience boolFromEnv to improve readability (# 5887)%0A  > 4565dd7 ringhash: allow overriding max ringhash size via environment variable (# 5884)%0A  > 94a65dc rls: deflake tests (# 5877)%0A  > 08479c5 xdsclient: resource agnostic API implementation (# 5776)%0A  > 07ac97c transport: simplify httpClient by moving onGoAway func to onClose (# 5885)%0A  > 5ff7dfc rls: propagate headers received in RLS response to backends (# 5883)%0A  > f94594d interop: add test client for use in xDS federation e2e tests (# 5878)%0A  > 68b388b balancer: support injection of per-call metadata from LB policies (# 5853)%0A  > 4f16fbe examples: update server reflection tutorial (# 5824)%0A  > b2d4d5d test: fix raceyness check to deflake test http server (# 5866)%0A  > 54b7d03 grpc: Add join Dial Option (# 5861)%0A  > 70617b1 vet & github: run vet separately from tests; make vet-proto only check protos (# 5873)%0A  > 81ad1b5 *: update all dependencies (# 5874)%0A  > 357d7af Change version to 1.53.0-dev (# 5872)%0A  > a0e8eb9 test: rename race.go to race_test.go (# 5869)%0A  > ae86ff4 benchmark: fix typo in ClientReadBufferSize feature name (# 5867)%0A  > e53d28f xdsclient: log node ID with verbosity INFO (# 5860)%0A  > 9373e5c transport: Fix closing a closed channel panic in handlePing (# 5854)%0A  > 2f413c4 transport/http2: use HTTP 400 for bad requests instead of 500 (# 5804)%0A  > 5003029 testutils: do a better job of verifying pick_first in tests (# 5850)%0A  > 3e27f89 binarylog: Account for key in metadata truncation (# 5851)%0A  > f54bba9 test/xds: minor cleanup in xDS e2e test (# 5843)%0A  > a9709c3 Added logs for reasons causing connection and transport close (# 5840)%0A  > aba03e1 xds: pass options by value to helper routines which setup the management server in tests (# 5833)%0A  > 638141f examples: add feature/cancellation retry to example test script (# 5846)%0A  > 22c1fd2 deps: update golang.org/x/net to latest in all modules (# 5847)%0A  > 1949035 ringhash: add logs to surface information about ring creation (# 5832)%0A  > f7c110a test: remove use of deprecated WithInsecure() API (# 5836)%0A  > a205447 examples: add new example to show updating metadata in interceptors (# 5788)%0A  > 001d234 rls: Fix regex in rls test (# 5834)%0A  > 7361971 rls: use a regex for the expected error string (# 5827)%0A  > 617d6c8 security/advancedtls: add test for crl cache expiration behavior (# 5749)%0A  > ef51864 grpclb: improve grpclb tests (# 5826)%0A  > fa99649 xdsclient: deflake new transport ack/nack tests (# 5830)%0A  > 99ba982 transport/server: flush GOAWAY before closing conn due to max age (# 5821)%0A  > 20c937e transport: limit AccountCheck tests to fewer streams and iterations to avoid flakes (# 5828)%0A  > 110ed9e xdsclient: resource-type-agnostic transport layer (# 5808)%0A  > c91396d pickfirst: do not return initial subconn while connecting (# 5825)%0A  > 94f0e7f benchmark: add a feature for read and write buffer sizes (# 5774)%0A  > 087387c Deflake Outlier Detection xDS e2e test (# 5819)%0A  > dd123b7 testutils/pickfirst: move helper function to testutils (# 5822)%0A  > be202a2 examples: add an example to illustrate the usage of stats handler (# 5657)%0A  > 9f97673 test: move e2e goaway tests to goaway_test.go (# 5820)%0A  > 0fe49e8 grpc: Improve documentation of read/write buffer size server and dial options (# 5800)%0A  > 09fc1a3 interop: update Go version in docker container used for psm interop (# 5811)%0A  > adfb915 server: fix ChainUnaryInterceptor and ChainStreamInterceptor to allow retrying handlers (# 5666)%0A  > e0a9f11 reflection: split grpc and pb imports (# 5810)%0A  > 6f96f96 reflection: update proto (# 5809)%0A  > 6e43203 reflection: generate protobuf files from grpc-proto (# 5799)%0A  > 0abb6f9 xdsclient: resource type agnostic WatchResource() API (# 5777)%0A  > 3011eaf test/tools: update staticcheck version to latest (# 5806)%0A  > fefb3ec test/tools: update everything to latest versions except staticcheck (# 5805)%0A  > 50be6ae go.mod: update all dependencies (# 5803)%0A  > ff14680 Cap min and max ring size to 4K (# 5801)%0A  > 0238b6e transport: new stream with actual server name (# 5748)%0A  > 817c1e8 passthrough: return error if endpoint is empty and opt.Dialer is nil when building resolver (# 5732)%0A  > 56ac86f xdsclient: wait for underlying transport to close (# 5775)%0A  > 457c2f5 benchmark: use default buffer sizes (# 5762)%0A  > 689d061 Cleanup usages of resolver.Target's Scheme and Authority (# 5761)%0A  > 5331dbd outlierdetection: remove an unused variable in a test (# 5778)%0A  > 81db250 Change version to 1.52.0-dev (# 5784)%0A  > 72812fe gcp/observability: filter logging from cloud ops endpoints calls (# 5765)%0A  > 0ae33e6 xdsclient: remove unused test code (# 5772)%0A  > 824f449 go.mod: upgrade x/text to v0.4 to address CVE (# 5769)%0A  > 7f23df0 xdsclient: switch xdsclient watch deadlock test to e2e style (# 5697)%0A  > 32f969e o11y: Added started rpc metric in o11y plugin (# 5768)%0A  > b597a8e xdsclient: improve authority watchers test (# 5700)%0A  > e41e894 orca: create ORCA producer for LB policies to use to receive OOB load reports (# 5669)%0A  > 36d14db Fix binary logging bug which logs a server header on a trailers only response (# 5763)%0A  > fcb8bdf xds/google-c2p: validate url for no authorities (# 5756)%0A  > 040b795 xdsclient/e2e_test: use SendContext() where appropriate (# 5729)%0A  > 0d6481f target: replace parsedTarget.Scheme to parsedTarget.URL.Scheme (# 5750)%0A  > fdcc01b transport/test: implement staticcheck suggestion (# 5752)%0A  > aa44cca google-c2p: use new-style resource name for LDS subscription (# 5743)%0A  > c858a77 balancer/weightedtarget: fix ConnStateEvltr to ignore transition from TF to Connecting (# 5747)%0A  > 64df652 google-c2p: include federation env var in the logic which determines when to use directpath (# 5745)%0A  > 3c09650 balancer/weightedtarget: use ConnectivityStateEvaluator (# 5734)%0A  > 3fd80b0 Fix flaky test MultipleClientStatsHandler (# 5739)%0A  > 26071c2 google-c2p resolver: add authority entry to bootstrap config (# 5680)%0A  > 9127159 client: synchronously verify server preface in newClientTransport (# 5731)%0A  > f51d212 xdsclient: improve RDS watchers test (# 5692)%0A  > 7c16802 tests: refactor tests to use testutils helper functions (# 5728)%0A  > 28fae96 xdsclient: improve federation watchers test (# 5696)%0A  > f88cc65 xdsclient: improve EDS watchers test (# 5694)%0A  > 439221d xdsclient: add a convenience type to synchronize execution of callbacks (# 5702)%0A  > dbb8e2b xdsclient: improve CDS watchers test (# 5693)%0A  > 79ccdd8 clientconn: go idle if conn closed after preface received (# 5714)%0A  > 778860e testing: update Go to 1.19 (# 5717)%0A  > eb8aa31 weightedtarget: return a more meaningful error when no child policy is reporting READY (# 5391)%0A  > bb3d739 fakeserver: add v3 support to the xDS fakeserver implementation (# 5698)%0A  > 912765f xds: move bootstrap config generating utility package to testutils (# 5713)%0A  > f52b910 o11y: Fixed o11y bug (# 5720)%0A  > 00d1830 Fix o11y typo (# 5719)%0A  > e163a90 xds/xdsclient: add EDS resource endpoint address duplication check (# 5715)%0A  > 9eba574 xds: de-experimentalize google c2p resolver (# 5707)%0A  > 8b3b10b gcp/observability: implement public preview config syntax, logging schema, and exposed metrics (# 5704)%0A  > 8062981 vet: workaround buggy mac git grep behavior (# 5716)%0A  > e81d0a2 xdsclient: improve LDS watchers test (# 5691)%0A  > 7b817b4 client: set grpc-accept-encoding to full list of registered compressors (# 5541)%0A  > c672451 xds/xdsclient: add sum of EDS locality weights check (# 5703)%0A  > c03925d priority: release references to child policies which are removed (# 5682)%0A  > 5fc798b Add binary logger option for client and server (# 5675)%0A  > 12db695 grpc: restrict status codes from control plane (gRFC A54) (# 5653)%0A  > 202d355 Change version to 1.51.0-dev (# 5687)%0A  > 1451c62 internal/transport: optimize grpc-message encoding/decoding (# 5654)%0A  > be4b63b test: minor test cleanup (# 5679)%0A  > d83070e Changed Outlier Detection Env Var to default true (# 5673)%0A  > 54521b2 client: remove trailing null from unix abstract socket address (# 5678)%0A  > 36e4810 orca: cleanup old code, and get grpc package to use new code (# 5627)%0A  > e8866a8 build: harden GitHub Workflow permissions (# 5660)%0A  > 8458251 xdsclient: ignore routes with cluster_specifier_plugin when GRPC_EXPERIMENTAL_XDS_RLS_LB is off (# 5670)%0A  > a238ceb xDS: Outlier Detection Env Var not hardcoded to false (# 5664)%0A  > b1d7f56 transport: Fix deadlock in transport caused by GOAWAY race with new stream creation (# 5652)%0A  > 9c3e589 rls: delegate pick to child policy as long as it is not in TransientFailure (# 5656)%0A  > 7da8a05 xds: Enable Outlier Detection interop tests (# 5632)%0A  > 21f0259 test: loosen metadata error check to reduce dependence on exact library errors (# 5650)%0A  > 552de12 orca: fix package used to reference service to use pb suffix instead of grpc (# 5647)%0A  > 87d1a90 orca: fix package used to reference service to use grpc suffix instead of pb (# 5645)%0A  > 60eecd9 metadata: add ValueFromIncomingContext to more efficiently retrieve a single value (# 5596)%0A  > 2ebd594 Documentation/proxy: update due to Go 1.16 behavior change (# 5630)%0A  > 1530d3b gcp/observability: fix End() to cleanup global state correctly (# 5623)%0A  > f7d2036 xds: add Outlier Detection Balancer (# 5435)%0A  > 182e9df Grab comment from proto file, similar to protoc-gen-go (# 5540)%0A  > 60a3a7e cleanup: fixes for issues surfaced by vet (# 5617)%0A  > 99ae81b roundrobin: optimization of the roundrobin implementation. (# 5607)%0A  > aee9f0e orca: server side custom metrics implementation (# 5531)%0A  > ddcda5f alts: do not set WaitForReady on handshaker RPCs (# 5620)%0A  > d875a0e xdsclient: NACK cluster resource if config_source_specifier in lrs_server is not self (# 5613)%0A  > c351f37 chore: remove duplicate word in comments (# 5616)%0A  > f0f9f00 test/kokoro: enable pod log collection in the buildscripts (# 5608)%0A  > 1dd0256 ringhash: implement a no-op ExitIdle() method (# 5614)%0A  > fe59226 clusterresolver: deflake eds_impl tests (# 5562)%0A  > d5dee5f xds/ringhash: make reconnection logic work for a single subConn (# 5601)%0A  > b225dda transport: update http2 spec document link (# 5597)%0A  > 641dc87 transport: add peer information to http2Server and http2Client context (# 5589)%0A  > 02fbca0 xds/resolver: generate channel ID randomly (# 5591)%0A  > 97cb7b1 xds/clusterresolver: prevent deadlock of concurrent Close and UpdateState calls (# 5588)%0A  > c56f196 internal/fakegrpclb: don't listen on all adapters (# 5592)%0A  > 3f5b7ab internal/transport: fix typo (# 5566)%0A  > c11858e Publish arm64 binaries to GitHub releases (# 5561)%0A  > 802b32e Change version to 1.50.0-dev (# 5585)%0Abumping github.com/fsnotify/fsnotify 0f4b979...5f8c606:%0A  > 5f8c606 Update ChangeLog%0A  > 8878587 Tweak the docs a bit%0A  > 89b4cf1 Add test for re-adding a renamed file (# 508)%0A  > 85acde2 Update x/sys%0A  > 69c24b0 Update x/sys%0A  > fb07f82 Add test to see what happens if you watch a symlink (# 498)%0A  > 666da9c Clarify doc comment on WatchList() (# 499)%0A  > 123e4e3 Add note about README version%0A  > 61a05ce Update documentation and examples (# 496)%0A  > e180a87 Move some inotify-tests to run on all backends; test that state is cleaned up after Remove (# 494)%0A  > fdf41a3 Move some files around%0A  > 844d71f Port minor test changes from fen-v2 branch; make LICENSE text not ugly%0A  > 5b87f50 windows: simplify a bit (# 493)%0A  > 2bfaa00 all: add Watcher.{sendEvent,sendError} (# 492)%0A  > 8ab3b84 kqueue: don't set up watchers on unreadable files (# 479)%0A  > a4bcdf8 Update changelog%0A  > 4b43fad kqueue: remove timeout from unix.Kevent() (# 480)%0A  > a24f78c windows: test symlinks (# 491)%0A  > f45391f windows: run TestWatchRename/rename_overwriting_existing_file (# 490)%0A  > ee33a65 Use "os.Rename()" in tests instead of "mv"%0A  > 9dd0568 cmd/fsnotify: fix time.Format() string%0A  > 5dcbfba windows: replace syscall with golang.org/x/sys/windows%0A  > 1f8edaf windows: replace "e" with "err" for error variables%0A  > 99715ba windows: increase buffer size from 4K to 64K (# 485)%0A  > a5c5815 ci: update to use Go 1.19, kick off fewer builds, update x/sys (# 484)%0A  > f2d35c3 Remove CLA section in contributing%0A  > 4604469 Need Linux 5.9 for a useful fanotify we can use%0A  > a566bb1 Update CONTRIBUTING.md%0A  > 01dfc6f Remove PULL_REQUEST_TEMPLATE%0A  > a58e868 Run tests in illumos (# 481)%0A  > 666c6a0 Update ChangeLog%0A  > 928895c [bugfix] close handle when remWatch open in getIno (# 288)%0A  > f174f95 windows: update watch paths when renaming directories with sub-watches (# 370)%0A  > 87dc1fa Rewrite tests (# 478)%0A  > 57e6a49 Add {Event,Op}.Has() (# 477)%0A  > 39823aa Document that /proc and /sys won't work%0A  > 60fbf57 Clarify FAQ on goroutines%0A  > ca0e2f4 macos: retry if open() returns EINTR (# 475)%0A  > ff39bb4 Fix lint (# 476)%0A  > 421f529 debian 6 test: deal with multiple packages (# 474)%0A  > a3256ef Remove AUTHORS file%0A  > 0e78fa6 Update README: split out FAQ to "Platform-specific notes"%0A  > 1a7b6ef inotify: don't ignore events for files that don't exist (# 470)%0A  > f0aceb2 Tweak comment regarding relative paths (# 466)%0A  > d9c9fa5 Add cmd/fsnotify (# 463)%0A  > cc15908 kqueue: better error if watching a file fails (# 471)%0A  > c4e64e4 Replace Use of Kthread-blocking Epoll with Poller Read, Remove Per-Event LStats on Linux # 433 (# 434)%0A  > 4b8b298 Test some more things in CI (# 469)%0A  > 548b8fb Add missing changelog for 1.4.{8,9} (# 468)%0A  > 7fe2936 inotify: fix race in Close() (# 465)%0A  > 35b6378 Clarify README on network drives (# 467)%0A  > e56409e Update link to CONTRIBUTING in the README (# 464)%0A  > 4678dfd Update documentation for linux systems (max_user_watches) (# 287)%0A  > 808f582 bump up GitHub Actions (# 461)%0A  > 4193dfd Do not suppress Chmod on non-existent file (# 260)%0A  > 6ae56b7 kqueue: Make watcher.Close() O(n) instead of O(n^2) (# 233)%0A  > adf5320 strings.Builder instead of bytes.Buffer (# 285)%0A  > 217e78e Explicit mutext (un)locking (# 462)%0A  > 1a4f949 Use common error when removing an unwatched file (# 460)%0A  > 5acfdc1 windows: protect access to isClosed with mutex (# 454)%0A  > c56cafd Test Go 1.18%0A  > 37badf6 This project is archived (# 459)%0Abumping golang.org/x/sync 8fcdb60...1ea3257:%0A  > 1ea3257 singleflight: make the check for exec support in TestPanicDoChan platform-agnostic%0Abumping k8s.io/apimachinery 4fbe8e4...b207ce5:%0A  > b207ce5 Merge pull request # 117691 from dims/re-do-of-117242-on-release-1.26%0A  > 917de35 Bump runc go module v1.1.4 -> v1.1.6%0A  > 53ecdf0 Merge pull request # 115787 from liggitt/net-0.7.0-1.26%0A  > 05339fa Update golang.org/x/net to v0.7.0%0A  > eabbfd5 Merge pull request # 115642 from nckturner/pin-golang.org/x/net-to-v0.4.0-in-1.26%0A  > 48b8d1f Pin golang.org/x/net to v0.4.0 in 1.26%0A  > 373a5f7 Merge pull request # 114521 from 3point2/automated-cherry-pick-of-# 113283-upstream-release-1.26%0A  > b5e5df6 Fix SPDY proxy authentication with special chars%0A  > 553a2d6 Improve error message when proxy connection fails%0A  > 5d4cdd2 Merge remote-tracking branch 'origin/master' into release-1.26%0A  > 6cbc4a3 Update golang.org/x/net 1e63c2f%0A  > 6561235 Merge pull request # 113699 from liggitt/manjusaka/fix-107415%0A  > dad8cd8 Update workload selector validation%0A  > fe82462 Add extra value validation for matchExpression field in LabelSelector%0A  > 067949d update k8s.io/utils to fix util tracing panic%0A  > 0ceff90 Merge pull request # 112223 from astraw99/fix-ownerRef-validate%0A  > 9e85d3a Merge pull request # 112649 from howardjohn/set/optimize-everything-nothing%0A  > b0dd9ec Fix ownerRef controller validate err%0A  > b03a432 Merge pull request # 113367 from pohly/dep-ginkgo-gomega%0A  > 88a1448 Rename and comment on why sharing is safe%0A  > 4e6bcdb dependencies: update to gomega v1.23.0 and ginkgo v2.4.0 and dependencies%0A  > 3adc870 Optimize `Everything` and `Nothing` label selectors%0A  > 0524d6c Merge pull request # 112693 from aimuz/fix-GO-2022-0969%0A  > 5a0277f Fixed (CVE-2022-27664) Bump golang.org/x/net to v0.1.1-0.20221027164007-c63010009c80%0A  > 6809593 Merge pull request # 112377 from weilaaa/refactor_sets_use_generic%0A  > 70a38aa Merge pull request # 113106 from pohly/dep-ginkgo-gomega%0A  > f2d9aed refactor sets use generic%0A  > d097f82 dependencies: update to gomega v1.22.1 and ginkgo v2.3.1%0A  > 7b5633b Merge pull request # 112988 from alexzielenski/update-kube-openapi%0A  > b839e82 Merge pull request # 113037 from pacoxu/fsnotify-v1.6.0%0A  > b7d8973 update kube-openapi%0A  > 1dc6ace update fsnotify to v1.6.0%0A  > 78d003c Merge pull request # 112989 from ameukam/bump-golang.org/x/text-to-v0.3.8%0A  > 04898ff Bump golang.org/x/text to v0.3.8%0A  > 79993b2 Merge pull request # 112875 from pohly/update-yaml%0A  > 7379c15 dependencies: update to sigs.k8s.io/yaml v1.3.0%0A  > 66e26ac Merge pull request # 112707 from enj/enj/i/https_links%0A  > 882b67d Use https links for k8s KEPs, issues, PRs, etc%0A  > 7fb78ee Merge pull request # 112472 from ialidzhikov/nit/error-msg%0A  > 826a74e Merge pull request # 112673 from dims/update-to-latest-k8s.io/utils-sep-22%0A  > 22fe889 Improve the error returned from the `LabelSelectorAsSelector` func%0A  > e2f9797 Update to latest k8s.io/utils to pick up changes%0A  > f8159af Merge pull request # 112545 from dims/update-etcd-3.5.5-and-all-otel-related-to-latest%0A  > 612703e Merge pull request # 112352 from pohly/e2e-ginkgo-progress%0A  > 9901884 updated etcd to v3.5.5 and newer otel libraries as well%0A  > 6439059 Merge pull request # 112526 from liggitt/redirect%0A  > 0564b5e e2e: bump ginkgo to v2.2.0%0A  > 2e3bf73 Limit redirect proxy handling to redirected responses%0A  > 6d854d7 Merge pull request # 112349 from pohly/klog-update%0A  > e1e1b7c build: update to klog v2.80.1%0A  > ed93eed Merge pull request # 111768 from weilaaa/feature_add_symmetric_difference_in_sets_string%0A  > 36163c5 Merge pull request # 112193 from jindijamie/master%0A  > b7b9ba4 add symmetric difference in sets%0A  > 31bc292 Merge pull request # 112199 from pohly/klog-update%0A  > 1c318b6 Add an option for aggregator%0A  > 0d0d03e Merge pull request # 111936 from haoruan/bugfix-111928-microtime-marshal-precision%0A  > 145c075 dependencies: update to klog v2.80.0%0A  > 2d64dac Merge pull request # 112089 from zeze1004/fix-typo%0A  > 2187a78 Marshal MicroTime to json and proto at the same precision%0A  > 53c4d51 Merge pull request # 112129 from pohly/e2e-ginkgo-report-after-each%0A  > 30e9977 Fix typo "sturct" to "struct"%0A  > 5e4f25a dependencies: update to ginkgo v2.1.6 and gomega v1.20.1%0A  > 349dcdf Merge pull request # 112052 from tosi3k/bump-client-golang%0A  > 16a7f7a Bump prometheus/client_golang to v1.13.0%0A  > 2b9fe2c Merge pull request # 111808 from alvaroaleman/meta-wrapping%0A  > bb48261 Apimachinery meta errors: Support errors.Is and error wrapping

Signed-off-by: Knative Automation <automation@knative.team>

---
## [FirDragon/DragonSurvival](https://github.com/FirDragon/DragonSurvival)@[618202cf54...](https://github.com/FirDragon/DragonSurvival/commit/618202cf540b5b61f0885b614cce678078cc8cb5)
#### Tuesday 2023-07-11 14:21:51 by Viktoria Ershova

Merge pull request #336 from SiverDX/fixes

> Set up the mod, will do the Curse Forge stuff once this is merged (since it depends on the harvest changes)
> 
> This PR now affects the following:
> 
> ### Fixed some issues regarding abilities (GUI)
> * Tooltip coloring for increasing levels
> * Experience gained from decreasing was 1 level lower than intended
> * There were 2 additional SkillProgressButtons being rendered (but overlayed by other buttons)
> * Right side of the experience cost for abilities had the wrong start location
> * When increasing or decreasing ability levels all were shown as obtainable (until screen was re-opened)
> 
> ### Other
> * Removed bad omen application when you kill a knight (only occurred as a non-dragon)
> * Fixed some issue with water cauldron block (sea dragon gained no good mana condition from it)
> 
> ### Fixed a bug with the Claws and Teeth description
> * The harvest level text was not accurate (starting from gold? it was 1 level too high)
> 
> ### Fixed issues with harvesting
> * Modded ore support for drops when only using paws (most modded ores should already work but this fixes certain other instances, mostly MCreator related)
> * Config for bonusUnlockedAt is now respected
> * ServerConfig.baseHarvestLevel is now actually used
> * Minimum level for base and bonus level is now 0 (wood)
> * When the tool in the claw inventory breaks block-breaking will no longer desync
> * Block breaking speed is only applied if the dragon is effective against the block (e.g. cave dragon can mine pickaxe-blocks faster but not shovel-blocks)
> 
> ### Removed Better Combat animation compatibility
> (This will not cause Better Combat to now crash with Dragon Survival - that was a separate issue)
> 
> * Removed config

---
## [knative-automation/kn-plugin-source-kafka](https://github.com/knative-automation/kn-plugin-source-kafka)@[fffab819e5...](https://github.com/knative-automation/kn-plugin-source-kafka/commit/fffab819e547b3056a5bc641126bd832e1dda31e)
#### Tuesday 2023-07-11 14:37:15 by Knative Automation

upgrade to latest dependencies

bumping golang.org/x/oauth2 e48dfd9...839de22:%0A  > 839de22 google: don't check for IsNotExist for well-known file%0A  > 0690208 go.mod: update golang.org/x dependencies%0A  > 451d5d6 internal: remove repeated definite articles%0A  > cfe200d oauth2: parse RFC 6749 error response%0A  > 3607514 go.mod: update golang.org/x dependencies%0A  > 4abfd87 google: add CredentialsParams.EarlyTokenRefresh%0A  > 1e7f329 oauth2: add ReuseTokenSourceWithExpiry%0A  > 86850e0 oauth2: fix typo%0A  > a6e37e7 google: Updating 3pi documentation%0A  > 54b70c8 google: update missing auth help URL%0A  > 2fc4ef5 README: encourage issues and proposals before changes%0A  > 62b4eed go.mod: update golang.org/x dependencies%0A  > 885f294 google: Add support for OAuth2 token exchange over mTLS%0A  > 6f9c1a1 google: use Credentials instead of deprecated DefaultCredentials%0A  > c82d0e1 google/internal/externalaccount: Removed URL validation for google URLs in ADC files%0A  > adbaf66 go.mod: update golang.org/x dependencies%0A  > e07593a oauth2: remove direct dependency on golang.org/x/net%0A  > 34ffb07 go.mod: update golang.org/x dependencies%0A  > b177c21 go.mod: update golang.org/x dependencies%0A  > 510acbc google/internal/externalaccount: Added check for aws region and security credential environment variables before aws metadata call%0A  > ec4a9b2 google/internal/externalaccount: Adding metadata verification%0A  > 68a41d6 go.mod: update golang.org/x dependencies%0A  > 1a77549 go.mod: update to new compute/metadata module%0Abumping golang.org/x/sys 90c8f94...ca59eda:%0A  > ca59eda windows: use unsafe.Add instead of pointer arithmetic on a uintptr%0A  > 6c52899 windows: return error if DecomposeCommandLine parameter contains NUL%0A  > 9524d49 windows/svc/mgr: Service.Control: populate Status when returning certain errors%0A  > 2a33a30 execabs: let hasExec return false on wasip1%0A  > 39c2d6a unix: add UDP socket option constants on linux%0A  > 1fb6828 unix: convert Iovec.Base to *byte in mkpost.go on solaris%0A  > 3125361 unix: allow overriding GOOS using GOOS_TARGET in mkpost.go%0A  > dbd8f99 windows: add Service.ListDependentServices%0A  > f25ff60 windows: add JobObjectInformationClass consts for QueryInformationJobObject%0A  > 64840c1 unix: add bindings for setattrlist() on macOS%0A  > 90abad3 unix: add AT_EACCESS on Darwin%0A  > 94933fc windows: fix constant values for JobObjectInformationClass%0A  > 00d8004 unix: match ioctl req argument type to libc type%0A  > d0781cc unix: make solaris syscall tests less flaky%0A  > ff18efa unix: change Setrlimit/Prlimit to always call syscall functions%0A  > 494aa49 unix: skip ip related tests if EAFNOSUPPORT raised%0A  > c7a1bf9 unix: define PerfBitWriteBackward%0A  > 1470852 unix: add SetsockoptTCPMD5Sig on linux%0A  > a6bfb89 unix: use unsafe.Slice in anyToSockaddr%0A  > c10701f windows: use unsafe.Slice in (*RawSockaddrAny).Sockaddr on windows%0A  > 6f25076 unix: define extended TCPInfo on Linux%0A  > 10499f4 unix: add ioctlPtr with unsafe.Pointer arg on other unices (cont)%0A  > 92c4c39 unix: add Dup3 on FreeBSD%0A  > 748af6e unix: pass PROT_MPROTECT(PROT_READ|PROT_WRITE) to initial Mmap on netbsd%0A  > 972870e unix/linux: update to Linux kernel 6.2, glibc 2.37 and Go 1.20.1%0A  > cc0b67d unix: use C.ioctl in generated ioctlPtr%0A  > a3b23cc unix: use SYS_PTRACE in generated ptracePtr%0A  > 71a906e unix/linux: add TUN flags and virtio_net_hdr constants%0A  > 2977c77 unix: add ptracePtr that accepts pointer arg as unsafe.Pointer%0A  > 6877dcc execabs: don't override Go 1.19 error with our error%0A  > b13f40e unix: add ioctlPtr with unsafe.Pointer arg on other unices%0A  > 3b9b58b unix: Faccess: check CAP_DAC_OVERRIDE on Linux%0A  > 2da1413 cpu: get hwcap/auxv from the Go 1.21+ runtime%0A  > 4fee21c windows: Add WSALookupService syscall wrappers%0A  > c79a742 unix: fix a use-after-free bug in PtraceIO on freebsd%0Abumping knative.dev/client-pkg 4f052f9...2311a7e:%0A  > 2311a7e Update community files (# 107)%0A  > f377f06 Update community files (# 106)%0A  > b93ceb0 Update community files (# 105)%0A  > 83c91f4 Update community files (# 103)%0A  > e5c405e Update community files (# 102)%0A  > eee9b55 Update community files (# 100)%0Abumping github.com/matttproud/golang_protobuf_extensions c182aff...c182aff:%0Abumping k8s.io/client-go 7226b15...6e9dabb:%0A  > 6e9dabb Update dependencies to v0.26.5 tag%0A  > 038b381 Merge pull request # 117691 from dims/re-do-of-117242-on-release-1.26%0A  > cd83e43 Bump runc go module v1.1.4 -> v1.1.6%0A  > dbfbc03 Merge pull request # 117686 from ardaguclu/automated-cherry-pick-of-# 117495-upstream-release-1.26%0A  > d72dec4 Use absolute path instead requestURI in openapiv3 discovery%0A  > a5144d4 Merge pull request # 117638 from seans3/automated-cherry-pick-of-# 117571-origin-release-1.26%0A  > d6f8d04 Refactors discovery content-type and helper functions%0A  > 2dd0093 Merge pull request # 115899 from odinuge/automated-cherry-pick-of-# 115620-upstream-release-1.26%0A  > f3ae5cb Merge pull request # 116666 from seans3/automated-cherry-pick-of-# 116603-origin-release-1.26%0A  > fffc68d Change where transformers are called.%0A  > 5ebee18 Aggregated discovery resilient to nil GVK%0A  > 8190aa4 client-go/cache: update Replace comment to be more clear%0A  > 87720b3 Merge pull request # 116437 from seans3/automated-cherry-pick-of-# 116145-# 115865-origin-release-1.26%0A  > b667227 client-go/cache: rewrite Replace to check queue first%0A  > fc13749 Removes old discovery hack ignoring 403 and 404%0A  > 30215cd client-go/cache: merge ReplaceMakesDeletionsForObjectsInQueue tests%0A  > f39ba12 Plumb stale GroupVersions through aggregated discovery%0A  > ba35969 client-go/cache: fix missing delete event on replace without knownObjects%0A  > f538edf Merge pull request # 116352 from seans3/automated-cherry-pick-of-# 115978-origin-release-1.26%0A  > 97cf9cb client-go/cache: fix missing delete event on replace%0A  > 5dbbc58 Tolerate empty discovery response in memcache client%0A  > 62133a9 Merge pull request # 115787 from liggitt/net-0.7.0-1.26%0A  > 8ce239f Update golang.org/x/net to v0.7.0%0A  > e6bc0bc Merge pull request # 115566 from enj/automated-cherry-pick-of-# 115315-upstream-release-1.26%0A  > 9112e19 Merge pull request # 115400 from pohly/automated-cherry-pick-of-# 115354-origin-release-1.26%0A  > 0519b53 kubelet/client: collapse transport wiring onto standard approach%0A  > 2e34348 Merge pull request # 115642 from nckturner/pin-golang.org/x/net-to-v0.4.0-in-1.26%0A  > 7be38cd dynamic resource allocation: avoid apiserver complaint about list content%0A  > 4968c4a Pin golang.org/x/net to v0.4.0 in 1.26%0A  > 0c34939 Merge pull request # 114617 from JoelSpeed/automated-cherry-pick-of-# 114585-upstream-release-1.26%0A  > 04b098b Resource claims should be a map type%0A  > b3fff46 Merge pull request # 114415 from hoskeri/automated-cherry-pick-of-# 114404-upstream-release-1.26%0A  > 236db3c Merge pull request # 113988 from liggitt/automated-cherry-pick-of-# 113933-upstream-release-1.26%0A  > a2ef324 Check the correct error in d.downloadAPIs%0A  > 95a14c3 Merge remote-tracking branch 'origin/master' into release-1.26%0A  > ebb499f Limit request retrying to []byte request bodies%0A  > 1a7cd1d Update golang.org/x/net 1e63c2f%0A  > 53f2fea sync: update go.mod%0A  > 968ba8d Merge pull request # 113797 from seans3/force-no-aggregated%0A  > c8ffed3 Merge pull request # 111023 from pohly/dynamic-resource-allocation%0A  > 3ac73ea Adds bool to force non-aggregated discovery%0A  > 61cd728 Merge pull request # 113826 from jsafrane/add-openstack%0A  > 522eaa1 api: generated files%0A  > cfd682c Merge pull request # 113375 from atiratree/PodHealthyPolicy-api%0A  > f2b10f3 Remove OpenStack cloud provider%0A  > acc9fa7 Merge pull request # 113186 from ttakahashi21/KEP-3294%0A  > f1c80d7 generated%0A  > a3d3eb0 Revert "Remove references to openstack and cinder"%0A  > c7bdab2 Generate code%0A  > 0a1f6a8 Merge pull request # 112744 from pwschuurman/statefulset-slice-impl%0A  > 1c7a870 Merge pull request # 113485 from MikeSpreitzer/apf-borrowing%0A  > eed2516 Adding implementation of KEP-3335, StatefulSetSlice%0A  > 7280270 Merge pull request # 113599 from seans3/discovery-client-update%0A  > d4a3675 apiserver: add generated files for borrowing in flowcontrol%0A  > 7694435 Update redacting functionality to redact all sensitive info in config when printing with view (# 109189)%0A  > 25d5761 Aggregated discovery client%0A  > 4b1a9fd Merge pull request # 113314 from cici37/celIntegration%0A  > ea9ec91 Merge pull request # 112905 from alexzielenski/kubectl-apply-csa-migration%0A  > 3a430a4 API - make update%0A  > 3daf180 Merge pull request # 113688 from dashpole/update_utils%0A  > 898b7a3 add FindFieldsOwners util function%0A  > dbe034b update k8s.io/utils to fix util tracing panic%0A  > 4f63b62 add UpgradeManagedFieldsPatch%0A  > 7ed3193 Merge pull request # 111545 from jlsong01/rewrite_signature_of_StartEventWatcher%0A  > c8c6cb5 add OWNERS to csaupgrade%0A  > cbe28cf Merge pull request # 113274 from Huang-Wei/kep-3521-A%0A  > 3467961 rewrite signature of function StartEventWatcher%0A  > a45874a remove kubectl annotation logic from upgrade patch%0A  > 2248bf3 Automated codegen%0A  > d576a35 Merge pull request # 113387 from wojtek-t/refactor_client_indexing%0A  > 4fbef5b Merge pull request # 106242 from thockin/revive-copy-lb-status-type-to-ingress%0A  > 5e7ba1f Minor cleanup of thread safe store%0A  > bc6266d Merge pull request # 103177 from arkbriar/support_cancelable_exec_stream%0A  > 3f162fe Copy LoadBalancerStatus from core to networking%0A  > b69a16c Refactor store index into its structure%0A  > 19b2e89 Merge pull request # 113523 from seans3/content-type-response%0A  > 0563dec Propagate the panic with a channel%0A  > 8ff4970 Get response content-type%0A  > 2362c7b use subtests and defer in TestSPDYExecutorStream%0A  > 0d57396 Merge pull request # 113304 from mimowo/handling-pod-failures-beta-ssa%0A  > 5e0a531 Support cancelable SPDY executor stream%0A  > a232cf0 Merge pull request # 113367 from pohly/dep-ginkgo-gomega%0A  > a191e58 SSA to add pod failure conditions - ready for review%0A  > 984bdbf dependencies: update to gomega v1.23.0 and ginkgo v2.4.0 and dependencies%0A  > f87d047 Merge pull request # 112693 from aimuz/fix-GO-2022-0969%0A  > d236783 Fixed (CVE-2022-27664) Bump golang.org/x/net to v0.1.1-0.20221027164007-c63010009c80%0A  > ef8a2e5 Merge pull request # 113089 from zackzhangkai/fix-doc%0A  > 197e479 Merge pull request # 108959 from astraw99/fix-duplicate-list%0A  > 0945beb fix typo%0A  > 42a0e1c Merge pull request # 113062 from alexzielenski/client-go-json-output%0A  > f549acf Fix duplicate code block of ListAll function%0A  > b6d3c8d Merge pull request # 107278 from harsimranmaan/allow_pagination_in_dynamic_fake_lister%0A  > 624929c address feedback%0A  > 9cc33a4 Merge pull request # 113106 from pohly/dep-ginkgo-gomega%0A  > 0c269b7 remove selflink as per review feedback%0A  > 12cafe2 refactor to use Schema(contentType)%0A  > 9b51067 dependencies: update to gomega v1.22.1 and ginkgo v2.3.1%0A  > fbd8e9a fix failing test assertions%0A  > 8b6ceae add more options for fetching openapiv3 in clients%0A  > fa9ed7f Merge pull request # 112860 from nckturner/remove-log-line%0A  > 1f10368 Preserve metadata for fake dynamic client unstructured lists%0A  > 6b24912 Merge pull request # 112988 from alexzielenski/update-kube-openapi%0A  > 5870c62 Remove log line from expiration cache%0A  > aea20dd Merge pull request # 113037 from pacoxu/fsnotify-v1.6.0%0A  > e3bb48f update kube-openapi%0A  > 1af3711 update fsnotify to v1.6.0%0A  > e6d958c Merge pull request # 112989 from ameukam/bump-golang.org/x/text-to-v0.3.8%0A  > 5e469ba Bump golang.org/x/text to v0.3.8%0A  > f515a4c Merge pull request # 112774 from stevekuznetsov/skuznets/dynamic-client-similar%0A  > b28f6c9 Merge pull request # 112875 from pohly/update-yaml%0A  > 34e8a5d client-go: factor the dynamic client similarly to others%0A  > c9afc73 dependencies: update to sigs.k8s.io/yaml v1.3.0%0A  > f24bd69 Merge pull request # 112306 from tkashem/v1beta3%0A  > ebc7cd4 Merge pull request # 112707 from enj/enj/i/https_links%0A  > 9b97b72 rename assuredConcurrencyShares for flowcontrol v1beta3%0A  > 2f43d37 Merge pull request # 112705 from stevekuznetsov/skuznets/fix-comment%0A  > 1665808 Use https links for k8s KEPs, issues, PRs, etc%0A  > 9bac803 apiserver: generate for apf v1beta3%0A  > 3697342 Merge pull request # 112680 from enj/enj/i/tls_cache_key_comparable%0A  > 956c1ce clients: clarify a misleading comment%0A  > c81636c Merge pull request # 112665 from NoicFank/fix-typo%0A  > cc2441c transport/cache: statically assert that tlsCacheKey is comparable%0A  > be20b2b Merge pull request # 112673 from dims/update-to-latest-k8s.io/utils-sep-22%0A  > 59765b8 fix typo error%0A  > 04dbcd8 Update to latest k8s.io/utils to pick up changes%0A  > 2fd4aac Merge pull request # 112613 from dims/update-github.com/go-openapi/jsonreference-to-drop-github.com/PuerkitoBio/purell%0A  > 47ad72a update github.com/go-openapi/jsonreference to drop github.com/PuerkitoBio/purell%0A  > f7c9c63 Merge pull request # 112545 from dims/update-etcd-3.5.5-and-all-otel-related-to-latest%0A  > b6e72dc Merge pull request # 112226 from aojea/client_go_transport%0A  > 6b5ecad updated etcd to v3.5.5 and newer otel libraries as well%0A  > acfaa39 Merge pull request # 112352 from pohly/e2e-ginkgo-progress%0A  > 1bd914a client-go: test transport generation is goroutine safe%0A  > 037b5fd Merge pull request # 112514 from markmc/patch-1%0A  > ec6c80a e2e: bump ginkgo to v2.2.0%0A  > 3f66212 client-go: remove reference to TPR in examples%0A  > 86ffa32 Merge pull request # 112475 from vatsalparekh/fix-TestRESTClientLimiter%0A  > ece6462 Merge pull request # 112476 from enj/enj/i/list_pager_flake%0A  > bf2b395 Fix Infelicities in TestRESTClientLimiter%0A  > 58155b7 Merge pull request # 112450 from enj/enj/i/exec_tls_cache_holder_cleanup%0A  > 6703098 Check for context cancellation on each buffered chunk%0A  > eecd3e5 Merge pull request # 112091 from xyz-li/master%0A  > 5dab9a0 client-go/transport: drop Dial and GetCert fields in favor of Holders%0A  > f6b8521 Merge pull request # 111333 from flant/selfsubjectattributesreviews%0A  > cc3cc93 kubectl: fix memory leaks in port forwarding client%0A  > b2b55e6 Add auth API to get self subject attributes%0A  > 18c3338 Merge pull request # 112200 from pohly/client-go-shared-informer-factory-shutdown%0A  > 9dae691 Merge pull request # 112309 from shyamjvs/disable-compression%0A  > ec4fedd client-go: support waiting for SharedInformerFactory shutdown%0A  > ab826d2 Merge pull request # 112349 from pohly/klog-update%0A  > 49ac40b Autogen code%0A  > ab0bfda build: update to klog v2.80.1%0A  > b8a8d94 Add DisableCompression option to KubeConfig%0A  > f32861c Merge pull request # 112341 from enj/enj/i/second_time_is_the_charm%0A  > 7d208ba Remove in-tree credential plugins (again)%0A  > e003fa9 Merge pull request # 112017 from enj/enj/i/exec_tls_cache%0A  > 2698e82 Merge pull request # 111967 from alexzielenski/csa-to-ssa%0A  > 6a008ec exec auth: support TLS config caching%0A  > 27c67e7 Merge pull request # 111122 from alexzielenski/informer%0A  > 00d892f correct spacing%0A  > d28c736 Merge pull request # 112022 from JackZxj/release-lock%0A  > a300ae0 return when test is done%0A  > 2efbeaf add boilerplate%0A  > b8b6206 Merge pull request # 112199 from pohly/klog-update%0A  > d04c2ce update lock getter of leaderelection%0A  > 93e5e0e hold listener lock while waiting for goroutines to finish%0A  > dac0826 remove inaccurate comment%0A  > 5a2c3e9 dependencies: update to klog v2.80.0%0A  > e11a988 simplify control flow%0A  > 7634f2e make upgrade modify input instead of deep copying%0A  > 7ccf7b0 Merge pull request # 112134 from apelisse/client-go-valid-segment%0A  > ac7f657 fix spelling%0A  > 9aa7c11 remove fieldsv1 from upgrade body%0A  > d83ec9e Merge pull request # 112129 from pohly/e2e-ginkgo-report-after-each%0A  > a4b84d8 Validate segments with client-go/dynamic%0A  > 0f4a6cf reset listenersStarted%0A  > 703d15e Update staging/src/k8s.io/client-go/util/csaupgrade/upgrade.go%0A  > cac10a8 dependencies: update to ginkgo v2.1.6 and gomega v1.20.1%0A  > 449817f add multithreaded test to shared informer%0A  > 675ca93 refactor if statement%0A  > 46d4284 Merge pull request # 111241 from Abirdcfly/fixtestorsource%0A  > de0b767 remove duplicate test%0A  > cfaca90 address comments%0A  > bdae576 Merge pull request # 112068 from aojea/aojea_client_go%0A  > 9b300de make TestListPager_EachListItem rework%0A  > 0565962 address review comments%0A  > 089614c remove last applied configuration information%0A  > fd22687 add aojea as client-go reviewer%0A  > 5a25eb0 switch listeners to use a map, adapt tests%0A  > efe3789 add more test cases%0A  > 35ead05 Merge pull request # 112052 from tosi3k/bump-client-golang%0A  > 90c6a46 active remove/add tests for event handlers%0A  > 46dc22f clean up test%0A  > 5291ca2 Bump prometheus/client_golang to v1.13.0%0A  > de4dd3a tests for invalid registration removals%0A  > ced85a8 update godoc%0A  > e6538dd Merge pull request # 112024 from cndoit18/remove-redundant-judgment%0A  > 33eff64 apply desired changes for handler registration%0A  > 049ba69 expose FieldsToSet and SetToFields%0A  > bcd2e6c style: remove redundant judgment%0A  > d73e40f rename handle to registration%0A  > aa892ab remove  unused code%0A  > d5e5863 Merge pull request # 111752 from aanm/revert-final-url-template%0A  > b3a61c6 remove informational informer methods again%0A  > 90ef078 dont expose internal methods in implementatoin%0A  > 5feaced Merge pull request # 67782 from dims/yank-in-tree-openstack-cloud-provider%0A  > e9d4627 client-go/rest: check if url is nil to prevent nil pointer dereference%0A  > ecdc8bf support removal of event handlers from SharedIndexInformers%0A  > c364b63 add function to upgrade managedfields CSA to SSA%0A  > 0fdc4f3 Merge pull request # 111684 from 0xff-dev/master1%0A  > 98e81a7 Remove references to openstack and cinder%0A  > c501ee0 Revert "client-go: remove no longer used finalURLTemplate"%0A  > 4faffa8 Merge pull request # 111564 from inosato/remove-ioutil-from-cli-client-go%0A  > c94a539 use constant NamespaceDefault instead of variable namespace%0A  > 2e40408 Merge pull request # 111918 from liggitt/in-tree-auth%0A  > 27de641 Remove ioutil from client-go%0Abumping k8s.io/apiextensions-apiserver 2c55649...52c998e:%0A  > 52c998e Update dependencies to v0.26.5 tag%0A  > 186ff9b Merge pull request # 117274 from jkh52/release-1.26-knp-0.0.37%0A  > b7b18f5 Merge pull request # 117691 from dims/re-do-of-117242-on-release-1.26%0A  > ee5015a Bump konnectivity-client to 0.0.37%0A  > 9ce75f3 Bump runc go module v1.1.4 -> v1.1.6%0A  > e9d194a Merge pull request # 115599 from jkh52/release-1.26-knp-0.0.36%0A  > d7df0be Merge pull request # 115787 from liggitt/net-0.7.0-1.26%0A  > 9152c67 Bump konnectivity-client to v0.0.36%0A  > 89cec57 Update golang.org/x/net to v0.7.0%0A  > f72cc5c Merge pull request # 115642 from nckturner/pin-golang.org/x/net-to-v0.4.0-in-1.26%0A  > 28eb995 Pin golang.org/x/net to v0.4.0 in 1.26%0A  > 33db789 Merge pull request # 114861 from jpbetz/release-1.26%0A  > a06e03d Merge pull request # 114927 from jkh52/release-1.26-knp-metrics%0A  > 0859963 Cherry pick 114857 to release-1.26%0A  > 5183885 Bump konnectivity-client to v0.0.35%0A  > 6e13726 Merge remote-tracking branch 'origin/master' into release-1.26%0A  > c338f3e Update golang.org/x/net 1e63c2f%0A  > 9768bad sync: update go.mod%0A  > f9c2bba fix aggregated discovery version sorting%0A  > d2c9e18 Merge pull request # 113171 from Jefftree/aggregated-discovery-generic%0A  > 470c040 Merge pull request # 113577 from pacoxu/prometheus-client%0A  > 915a888 add crds to aggregated discovery%0A  > 92430b6 Merge pull request # 113314 from cici37/celIntegration%0A  > ac326ca upgrade prometheus-client to v1.14.0%0A  > 5a6bf16 Merge pull request # 113688 from dashpole/update_utils%0A  > 67b0610 Integrate cel admission with API.%0A  > 84fed82 upgrade github.com/prometheus/client_golang to v1.13.1%0A  > 077b441 update k8s.io/utils to fix util tracing panic%0A  > 5bbf20d Adding new api version of admissionregistration.k8s.io v1alpha1 for CEL in Admission Control%0A  > 3b533ba Merge pull request # 113367 from pohly/dep-ginkgo-gomega%0A  > 975bbeb dependencies: update to gomega v1.23.0 and ginkgo v2.4.0 and dependencies%0A  > ae2b4c3 Merge pull request # 112693 from aimuz/fix-GO-2022-0969%0A  > c4deae9 Fixed (CVE-2022-27664) Bump golang.org/x/net to v0.1.1-0.20221027164007-c63010009c80%0A  > bc4263f Merge pull request # 113172 from dashpole/endpoint_handler_tracing%0A  > f6c164e migrate apiserver utiltrace usage to component-base/tracing%0A  > 53e3726 Merge pull request # 113015 from ritazh/crencryption%0A  > c8d8a9f Enable encryption for custom resources%0A  > 6405068 Merge pull request # 113325 from panslava/fix-time-since-defer%0A  > 508e399 Fix time.Since() in defer. Wrap in anonymous function%0A  > 5f8e59e Merge pull request # 112691 from aimuz/apiextensions-apiserver-change-to-cmp%0A  > c996139 Merge pull request # 113106 from pohly/dep-ginkgo-gomega%0A  > f83e03c apiextensions-apiserver: change k8s.io/apimachinery/pkg/util/diff to github.com/google/go-cmp/cmp%0A  > b68fc51 dependencies: update to gomega v1.22.1 and ginkgo v2.3.1%0A  > 49c41b4 Merge pull request # 112988 from alexzielenski/update-kube-openapi%0A  > 3aaa2a0 Merge pull request # 113037 from pacoxu/fsnotify-v1.6.0%0A  > d9f6ebd update kube-openapi%0A  > 82e3ba4 Merge pull request # 112789 from enj/enj/r/kms_load_once_v2%0A  > 7423813 update fsnotify to v1.6.0%0A  > 8bf3487 Merge pull request # 113011 from jpmcb/cobra-1.6.0%0A  > d34393e Load encryption config once%0A  > 6ba582f Bumps cobra from 1.5.0 to 1.6.0%0A  > 8e0697b Merge pull request # 113022 from logicalhan/webhook-metrics%0A  > 90c63e0 Merge pull request # 112926 from jiahuif-forks/refactor/cel-out-of-apiextensions%0A  > 548c480 unparameterize 'webhook' from conversion metrics since it's the only one%0A  > 77badb8 Merge pull request # 112989 from ameukam/bump-golang.org/x/text-to-v0.3.8%0A  > 609e270 use DefaultMaxRequestSizeBytes for maxRequestSizeBytes.%0A  > 04f26fa Bump golang.org/x/text to v0.3.8%0A  > dd981e1 move CEL package to apiserver package.%0A  > 1644998 Move celopenapi/model to staging/src/k8s.io/apiextensions-apiserver/pkg/apiserver/schema/cel/ (# 109959)%0A  > 08d44e8 Merge pull request # 112875 from pohly/update-yaml%0A  > 1300140 dependencies: update to sigs.k8s.io/yaml v1.3.0%0A  > 5fb82bd Merge pull request # 112819 from thockin/no-make-generators%0A  > f5f5279 Codegens: Do not auto-set boilerplate path%0A  > f22ee73 Merge pull request # 112738 from liggitt/proto-tag%0A  > ba7f1b7 Merge pull request # 112689 from cheftako/master%0A  > 7ac7774 github.com/matttproud/golang_protobuf_extensions v1.0.2%0A  > e678457 Merge pull request # 112748 from wojtek-t/lock_ssa_gate%0A  > 0aca5a6 Bump konnectivity-client to v0.0.33%0A  > 9be4b4a Lock ServerSideApply feature to true%0A  > 7b53cb7 Merge pull request # 111980 from aramase/kms%0A  > f40a683 Merge pull request # 112705 from stevekuznetsov/skuznets/fix-comment%0A  > 4cd9125 Add staging directory for kms%0A  > d4e654a clients: clarify a misleading comment%0A  > 8b851d9 Merge pull request # 112673 from dims/update-to-latest-k8s.io/utils-sep-22%0A  > 362a89c Merge pull request # 112615 from mengjiao-liu/update_CRD_link%0A  > add0c80 Update to latest k8s.io/utils to pick up changes%0A  > 374216b Merge pull request # 112613 from dims/update-github.com/go-openapi/jsonreference-to-drop-github.com/PuerkitoBio/purell%0A  > a7ee7f9 Update `PreserveUnknownFields` field document link%0A  > 488bf20 update github.com/go-openapi/jsonreference to drop github.com/PuerkitoBio/purell%0A  > 47c15ca Merge pull request # 112588 from pacoxu/fsnotify-v1.5.4%0A  > d5b6243 Merge pull request # 112584 from dims/brneto-master%0A  > 8c6aa82 update fsnotify/fsnotify to v1.5.4%0A  > f8e18e9 run pin-dependency.sh and then hack/update-vendor.sh%0A  > c540c8c Merge pull request # 112545 from dims/update-etcd-3.5.5-and-all-otel-related-to-latest%0A  > 70b0d96 Merge pull request # 112352 from pohly/e2e-ginkgo-progress%0A  > 39cab0b updated etcd to v3.5.5 and newer otel libraries as well%0A  > 5faccda Merge pull request # 111866 from pacoxu/validate%0A  > 1c3fe9d e2e: bump ginkgo to v2.2.0%0A  > 917d446 Merge pull request # 112458 from dims/switch-to-release-tag-for-antlr-v1.4.10%0A  > 8b3fe74 add test case for array checking with dup values%0A  > 045fc90 Merge pull request # 112433 from ncdc/reduce-SchemaHas-allocs%0A  > 73cc883 Switch to release tag for antlr : v1.4.10%0A  > 22bcc66 added ratcheting validation for embedded resource and x-kubernetes-list-type validation%0A  > 269d73d Reduce allocations in HasSchemas%0A  > 7342cc6 Merge pull request # 112200 from pohly/client-go-shared-informer-factory-shutdown%0A  > aabbdff Merge pull request # 112349 from pohly/klog-update%0A  > fdf28bc client-go: support waiting for SharedInformerFactory shutdown%0A  > 6b7d12b build: update to klog v2.80.1%0A  > 559b4fa Merge pull request # 111768 from weilaaa/feature_add_symmetric_difference_in_sets_string%0A  > bf7d058 add symmetric difference in sets%0A  > 04ff81e Merge pull request # 112199 from pohly/klog-update%0A  > 87a4c3f dependencies: update to klog v2.80.0%0A  > 8f15690 Merge pull request # 112129 from pohly/e2e-ginkgo-report-after-each%0A  > f637e1c dependencies: update to ginkgo v2.1.6 and gomega v1.20.1%0A  > b6adc1c Merge pull request # 111964 from DangerOnTheRanger/cel-estimate-fix-update%0A  > ea2d438 Merge pull request # 112052 from tosi3k/bump-client-golang%0A  > 6b4dc0b Add unit tests.%0A  > 767e67b Bump prometheus/client_golang to v1.13.0%0A  > 782b982 Run pin-dependency.sh and update-vendor.sh.%0A  > 305963e Merge pull request # 111909 from tosi3k/bump-prom-client%0A  > fa2959a Merge pull request # 111830 from t1anz0ng/typo%0A  > 5a6ffec Bump prometheus/client_golang to v1.12.2%0A  > e0abc3b fix(typo): remove extra " from autoscaling doc string%0A  > 2184a8d Merge pull request # 111696 from liggitt/go119mod%0A  > f750907 Update go.mod to go1.19%0Abumping go.opencensus.io 49838f2...b1a01ee:%0A  > b1a01ee Add started RPC metric for client and server side (# 1283)%0A  > 0bf7faa Fix CI, and update testify (# 1284)%0A  > 0521206 Passing capacity to make() in place of length.  (# 1276)%0A  > c2a62a2 fix: Add function to stop the defaultWorker (# 1272)%0A  > bf52d9d  Remove `convTslice` calls in Record()  (# 1268)%0A  > ad0b46e Precompute encodeWithKeys buffer size to avoid resizes (# 1269)%0A  > a55fb71 Optimize `Record()` to avoid extra allocations  (# 1267)%0A  > dcf8515 Fix formatting to pass with go1.17 (# 1270)%0A  > fb455b0 Remove @rakyll from codeowners (# 1256)%0A  > f5c4b39 Bump version to next expected release (# 1257)%0Abumping github.com/fsnotify/fsnotify 0f4b979...5f8c606:%0A  > 5f8c606 Update ChangeLog%0A  > 8878587 Tweak the docs a bit%0A  > 89b4cf1 Add test for re-adding a renamed file (# 508)%0A  > 85acde2 Update x/sys%0A  > 69c24b0 Update x/sys%0A  > fb07f82 Add test to see what happens if you watch a symlink (# 498)%0A  > 666da9c Clarify doc comment on WatchList() (# 499)%0A  > 123e4e3 Add note about README version%0A  > 61a05ce Update documentation and examples (# 496)%0A  > e180a87 Move some inotify-tests to run on all backends; test that state is cleaned up after Remove (# 494)%0A  > fdf41a3 Move some files around%0A  > 844d71f Port minor test changes from fen-v2 branch; make LICENSE text not ugly%0A  > 5b87f50 windows: simplify a bit (# 493)%0A  > 2bfaa00 all: add Watcher.{sendEvent,sendError} (# 492)%0A  > 8ab3b84 kqueue: don't set up watchers on unreadable files (# 479)%0A  > a4bcdf8 Update changelog%0A  > 4b43fad kqueue: remove timeout from unix.Kevent() (# 480)%0A  > a24f78c windows: test symlinks (# 491)%0A  > f45391f windows: run TestWatchRename/rename_overwriting_existing_file (# 490)%0A  > ee33a65 Use "os.Rename()" in tests instead of "mv"%0A  > 9dd0568 cmd/fsnotify: fix time.Format() string%0A  > 5dcbfba windows: replace syscall with golang.org/x/sys/windows%0A  > 1f8edaf windows: replace "e" with "err" for error variables%0A  > 99715ba windows: increase buffer size from 4K to 64K (# 485)%0A  > a5c5815 ci: update to use Go 1.19, kick off fewer builds, update x/sys (# 484)%0A  > f2d35c3 Remove CLA section in contributing%0A  > 4604469 Need Linux 5.9 for a useful fanotify we can use%0A  > a566bb1 Update CONTRIBUTING.md%0A  > 01dfc6f Remove PULL_REQUEST_TEMPLATE%0A  > a58e868 Run tests in illumos (# 481)%0A  > 666c6a0 Update ChangeLog%0A  > 928895c [bugfix] close handle when remWatch open in getIno (# 288)%0A  > f174f95 windows: update watch paths when renaming directories with sub-watches (# 370)%0A  > 87dc1fa Rewrite tests (# 478)%0A  > 57e6a49 Add {Event,Op}.Has() (# 477)%0A  > 39823aa Document that /proc and /sys won't work%0A  > 60fbf57 Clarify FAQ on goroutines%0A  > ca0e2f4 macos: retry if open() returns EINTR (# 475)%0A  > ff39bb4 Fix lint (# 476)%0A  > 421f529 debian 6 test: deal with multiple packages (# 474)%0A  > a3256ef Remove AUTHORS file%0A  > 0e78fa6 Update README: split out FAQ to "Platform-specific notes"%0A  > 1a7b6ef inotify: don't ignore events for files that don't exist (# 470)%0A  > f0aceb2 Tweak comment regarding relative paths (# 466)%0A  > d9c9fa5 Add cmd/fsnotify (# 463)%0A  > cc15908 kqueue: better error if watching a file fails (# 471)%0A  > c4e64e4 Replace Use of Kthread-blocking Epoll with Poller Read, Remove Per-Event LStats on Linux # 433 (# 434)%0A  > 4b8b298 Test some more things in CI (# 469)%0A  > 548b8fb Add missing changelog for 1.4.{8,9} (# 468)%0A  > 7fe2936 inotify: fix race in Close() (# 465)%0A  > 35b6378 Clarify README on network drives (# 467)%0A  > e56409e Update link to CONTRIBUTING in the README (# 464)%0A  > 4678dfd Update documentation for linux systems (max_user_watches) (# 287)%0A  > 808f582 bump up GitHub Actions (# 461)%0A  > 4193dfd Do not suppress Chmod on non-existent file (# 260)%0A  > 6ae56b7 kqueue: Make watcher.Close() O(n) instead of O(n^2) (# 233)%0A  > adf5320 strings.Builder instead of bytes.Buffer (# 285)%0A  > 217e78e Explicit mutext (un)locking (# 462)%0A  > 1a4f949 Use common error when removing an unwatched file (# 460)%0A  > 5acfdc1 windows: protect access to isClosed with mutex (# 454)%0A  > c56cafd Test Go 1.18%0A  > 37badf6 This project is archived (# 459)%0Abumping github.com/prometheus/client_golang 64435fc...254e546:%0A  > 254e546 Merge pull request # 1162 from kakkoyun/cut-1.14.0%0A  > 07d3a81 Merge pull request # 1161 from prometheus/release-1.13%0A  > c8a3d32 Cut v1.14.0%0A  > 870469e Test and support 1.19 (# 1160)%0A  > 53e51c4 Merge pull request # 1157 from prometheus/cut-1.13.1%0A  > b785d0c Fix go_collector_latest_test Fail on go1.19 (# 1136)%0A  > 79ca0eb Added tip from Björn + Grammarly.%0A  > 4d54769 Fix float64 comparison test failure on archs using FMA (# 1133)%0A  > 078f11f Cut 1.13.1 release (+ documenting release process).%0A  > 5f202ee Merge pull request # 1150 from prometheus/sparsehistogram%0A  > ddd7f0e Fix race condition with Exemplar in Counter (# 1146)%0A  > 0859bb8 Merge pull request # 1152 from jessicalins/update-to-custom-reg%0A  > fffb76c Merge branch 'main' into sparsehistogram%0A  > 1f93f64 Fix `CumulativeCount` value of `+Inf` bucket created from exemplar (# 1148)%0A  > 10b0550 Fix race condition with Exemplar in Counter (# 1146)%0A  > a340ca4 Run make format%0A  > e92a8c7 Avoid the term 'sparse' where possible%0A  > 8cc2b6c Fix double-counting bug in promhttp.InstrumentRoundTripperCounter (# 1118)%0A  > dcea97e Fix `CumulativeCount` value of `+Inf` bucket created from exemplar (# 1148)%0A  > 6056615 Update random example to use custom registry%0A  > d31f13b Add SparseBucketsZeroThresholdZero and groom doc comments%0A  > 9801a4e Examples: Replace deprecated WithGoCollections with WithGoCollectorRuntimeMetrics (# 1130)%0A  > 0b7f488 Update simple example to use custom registry%0A  > 58a8ca4 examples: Adjust doc comment for native histograms%0A  > 7c46c15 Clarify documentation around what constructors do (# 1125)%0A  > 9b5c5b8 Update basic example to use custom registry%0A  > 4e71e6f Update prometheus/client_model dependency%0A  > 83d56b1 Extend prometheus.Registry to implement Collector (# 1103)%0A  > 111fae1 Merge branch 'main' into sparsehistogram%0A  > 4c41dfb Clarify exemplar(Add|Observe) by renaming to (add|observe)WithExemplar (# 1122)%0A  > 25bc188 Merge pull request # 1144 from prometheus/beorn7/histogram2%0A  > f73e3cc Fix double-counting bug in promhttp.InstrumentRoundTripperCounter (# 1118)%0A  > 95cf173 Merge branch 'main' into sparsehistogram%0A  > 6942f9e sparse buckets: Fix handling of +Inf/-Inf/NaN observations%0A  > c7aa2a5 Merge pull request # 1113 from prometheus/release-1.13%0A  > ec86ef1 Merge pull request # 1092 from prometheus/beorn7/histogram%0A  > 1e61b8e Update common Prometheus files (# 1111)%0A  > 6141a07 Merge branch 'main' into sparsehistogram%0A  > 8cbcd40 histograms: Move to new exposition protobuf format%0A  > 5a321c7 Merge branch 'foo-commit' into sparsehistogram%0A  > e93e384 Merge branch 'beorn7/release' into sparsehistogram%0A  > e203144 Merge branch 'release-1.12' of github.com:prometheus/client_golang into release-1.12%0A  > 525d042 Merge branch 'main' into sparsehistogram%0A  > a516626 Merge branch 'release-1.12' into beorn7/release%0A  > a27b6d7 Fix conflicts%0A  > 6ba7871 Merge branch 'main' into sparsehistogram%0A  > eb59a7b Histogram: Fix bug with negative schemas (# 1054)%0A  > b237230 Merge branch 'main' into sparsehistogram%0A  > 294cca4 Merge branch 'main' into sparsehistogram%0A  > 70253f4 Fix typo in doc comment%0A  > 5b19c55 Merge branch 'master' into sparsehistogram%0A  > dfbcc28 Merge pull request # 901 from prometheus/beorn7/histogram%0A  > 84fcaff Merge branch 'master' into sparsehistogram%0A  > 263be8d Refactoring of sparse histograms%0A  > 9ef5f90 Allow a zero threshold of zero%0A  > 2409960 Implement strategy to limit the sparse bucket count%0A  > aa6f67a Add TODO about bucket search optimization%0A  > 43f31c2 Merge pull request # 886 from prometheus/beorn7/histogram%0A  > 5aa8534 Merge branch 'master' into sparsehistogram%0A  > 5142344 Pin client_model to the most recent sparsehistogram commit%0A  > 97eb041 Tidy go.sum%0A  > 6c4e0ef Add tests for sparse histogram%0A  > 553ed73 Fix lint warning%0A  > 31318b7 Switch to base-2 buckets%0A  > b7a540a Fix test%0A  > a9df0ba Update prometheus/client_model%0A  > ce36ee3 Merge branch 'master' into beorn7/histogram%0A  > d698336 Merge branch 'master' into beorn7/histogram%0A  > 08104a0 Minor doc comment fixes%0A  > a9d0066 Add note about pow-of-10 precision issue%0A  > d1f5366 Fix span offset%0A  > abe540f Encode sparse histograms in protobuf%0A  > c98db4e Demo sparse histograms%0Abumping golang.org/x/net 8e2b117...daac0ce:%0A  > daac0ce go.mod: update golang.org/x dependencies%0A  > 82780d6 http2: don't reuse connections that are experiencing errors%0A  > 0bfab66 ipv4, ipv6: drop redundant skip checks based on GOOS%0A  > 938ff15 ipv4, ipv6, nettest: skip unsupported tests on wasip1%0A  > eb1572c html: another shot at security doc%0A  > 9001ca7 nettest: re-enable unixpacket tests on netbsd/386%0A  > 3d5a8ee internal/socks: permit authenticating with an empty password%0A  > 694cff8 go.mod: update golang.org/x dependencies%0A  > 6960703 http2: log the correct error when retrying in (*Transport).RoundTripOpt%0A  > 9f24bb4 http2: properly discard data received after request/response body is closed%0A  > 08dda57 html: fix package doc typo%0A  > dfa2b5d go.mod: update golang.org/x dependencies%0A  > 8c4ef2f hmtl: add security section to package comment%0A  > 1d46ed8 html: have Render escape comments less often%0A  > 569fe81 html: add "Microsoft Outlook comment" tests%0Abumping github.com/census-instrumentation/opencensus-proto 4aa53e1...e53624a:%0A  > e53624a Bump version to 0.4.1%0A  > 576a4ca Run go mod tidy, forgot to do after proto updates (# 228) (# 230)%0A  > f918ec1 Merge pull request # 227 from dashpole/release%0A  > a5f3b19 Add makefile, upgrade to use opentelemetry protoc docker, newer protoc (# 225)%0A  > 11530ad Bump version to 0.4.1-SNAPSHOT%0A  > 032ec2a Add go.mod, so dependencies are controlled (# 224)%0A  > 0b54ad6 Bump version to 0.4.0%0A  > 54c9a4c Start 0.4.0 development cycle (# 219)%0Abumping knative.dev/pkg dfad48e...5ef4812:%0A  > 5ef4812 Update community files (# 2762)%0A  > 49e2e56 update google cloud deps (# 2758)%0A  > a5e0b92 upgrade to latest dependencies (# 2757)%0A  > 6eb4b40 Update community files (# 2760)%0A  > eb63a40 Support to set qps and burst via env variable (# 2755)%0A  > 74c4be5 Generate kresource duck type codegen (# 2754)%0A  > 4dbc312 fix boilerplate (# 2753)%0A  > 15605c7 Defaulting Controller options for all kind of webhooks (# 2738)%0A  > 94b81fc Update community files (# 2752)%0A  > 5671699 drop the dynamic type (# 2750)%0A  > 9bda38b Fix some webhook testing tech debt (# 2751)%0A  > ec20442 Update community files (# 2747)%0A  > 05bfcf6 bump k8s dependencies and update min version to v1.25 (# 2745)%0A  > 52ff2ac drop dynamic client wrappers (# 2744)%0A  > a170a07 Eventing TLS: validate that Destination.CACerts is a PEM encoded cert (# 2743)%0A  > dfb4bf0 Drop dynamic wrapper injection code generation (# 2742)%0A  > db8a353 Add SinkCACerts to SourceStatus (# 2733)%0A  > 9049667 Update community files (# 2735)%0A  > aacec7f Update community files (# 2734)%0A  > 300df43 Eventing TLS: Added AddressableFromDestination method on the resolver (# 2717)%0Abumping github.com/prometheus/client_model 7bc5445...63fb982:%0A  > 63fb982 Merge pull request # 63 from prometheus/sparsehistogram%0A  > 5c16fa2 Merge pull request # 57 from prometheus/repo_sync%0A  > fdb567d Add note about native histograms to README%0A  > 6b8c742 Update common Prometheus files%0A  > 942d53c Update common Prometheus files%0A  > 7f720d2 Add note about experimental state of native histograms%0A  > f60d1ac Update common Prometheus files%0A  > 1f8dcad Merge pull request # 59 from prometheus/beorn7/histogram%0A  > 6dc836e Merge pull request # 53 from prometheus/repo_sync%0A  > 421ad2b Merge pull request # 58 from prometheus/beorn7/histogram%0A  > a7ff713 Flatten the buckets of native histograms%0A  > 0e1ed89 Merge pull request # 52 from prometheus/repo_sync%0A  > a227486 Update common Prometheus files%0A  > 408689d Merge branch 'master' into sparsehistogram%0A  > 0da3265 Explain Span layout better%0A  > 14ab895 Merge pull request # 51 from prometheus/repo_sync%0A  > bc75c6a Update common Prometheus files%0A  > 61b6c1a Merge pull request # 47 from prometheus/beorn7/histogram%0A  > 8171e83 Add float histograms and gauge histograms to proto spec%0A  > a863571 Merge pull request # 49 from prometheus/repo_sync%0A  > 2fc368c Update common Prometheus files%0A  > 8831f0d Merge branch 'master' into sparsehistogram%0A  > bbaf1cc Switch to base 2 and powers of 2 for resolution%0A  > 675c4e5 Merge pull request # 48 from prometheus/repo_sync%0A  > a3e6551 Update common Prometheus files%0A  > 24db95a Merge remote-tracking branch 'origin/master' into beorn7/histogram%0A  > 147c58e Move .proto file and add caching of protoc and protoc-gen-go during build (# 46)%0A  > 56ab8d9 Update common Prometheus files%0A  > 4b803f3 Experimental encoding for sparse buckets in histogram%0A  > 0255a22 Merge pull request # 43 from roidelapluie/security-dot-md%0A  > 1f48c5c Rename metrics.proto to io_prometheus_client_metrics.proto (# 45)%0A  > 60555c9 Merge pull request # 41 from prometheus/repo_sync%0A  > 1bb3080 Add SECURITY.md%0A  > 1106810 Update common Prometheus files%0Abumping github.com/golang/protobuf ae97035...5d5e8c0:%0A  > 5d5e8c0 Merge pull request # 1363 from neild/jsonnull%0A  > 37828f9 jsonpb: accept 'null' as a valid representation of NullValue in unmarshal%0Abumping k8s.io/api 88912e3...6b24792:%0A  > 6b24792 Update dependencies to v0.26.5 tag%0A  > 37e98ba Merge pull request # 117814 from kerthcet/automated-cherry-pick-of-# 117802-upstream-release-1.26%0A  > 7ff025f Update podFailurePolicy comments from alpha-level to beta%0A  > c9f384e Merge pull request # 117691 from dims/re-do-of-117242-on-release-1.26%0A  > c00f1ad Bump runc go module v1.1.4 -> v1.1.6%0A  > 4c28c5a Merge pull request # 117323 from dddddai/automated-cherry-pick-of-# 117182-upstream-release-1.26%0A  > 9483bbc use case-insensitive header keys for http probes%0A  > 0545f3a Merge pull request # 116081 from pohly/automated-cherry-pick-of-# 115928-origin-release-1.26%0A  > e92d7e9 api: generated files%0A  > 16f23da api: drop Resources.Claims from PVC and PVC template%0A  > 5fd8a44 Merge pull request # 115787 from liggitt/net-0.7.0-1.26%0A  > 1b65b64 Update golang.org/x/net to v0.7.0%0A  > 2e857c1 Merge pull request # 115400 from pohly/automated-cherry-pick-of-# 115354-origin-release-1.26%0A  > 1c6bd70 Merge pull request # 115642 from nckturner/pin-golang.org/x/net-to-v0.4.0-in-1.26%0A  > 50d0b42 dynamic resource allocation: avoid apiserver complaint about list content%0A  > 045c7fe Pin golang.org/x/net to v0.4.0 in 1.26%0A  > 07a9cbc Merge pull request # 114617 from JoelSpeed/automated-cherry-pick-of-# 114585-upstream-release-1.26%0A  > 52655b9 Resource claims should be a map type%0A  > 07ac8fe Merge remote-tracking branch 'origin/master' into release-1.26%0A  > 566ee01 Update golang.org/x/net 1e63c2f%0A  > b966dc9 sync: update go.mod%0A  > 053624e Merge pull request # 111023 from pohly/dynamic-resource-allocation%0A  > 3590eda Merge pull request # 113375 from atiratree/PodHealthyPolicy-api%0A  > 8356158 api: update testdata%0A  > 5cb3202 Merge pull request # 113186 from ttakahashi21/KEP-3294%0A  > 5a4f9a5 generated%0A  > 78799a8 api: generated files%0A  > dfd6ea2 Generate code%0A  > 993c43c api: add UnhealthyPodEvictionPolicy for PDBs%0A  > ef72ea9 api: dynamic resource allocation API%0A  > d8ab3fb Add API and validation for CrossNamespaceVolumeDataSource%0A  > af772fc api: add resource claims to core API%0A  > 7beaa08 Merge pull request # 112744 from pwschuurman/statefulset-slice-impl%0A  > d7d25c8 Merge pull request # 113360 from mimowo/handling-pod-failures-beta-enable%0A  > f46cd33 Undo unintentional documentation comment change%0A  > f967e44 Merge pull request # 113485 from MikeSpreitzer/apf-borrowing%0A  > 11620b8 Enable the feature into beta%0A  > 6ae95de Fix typo in function emptyInvariants()%0A  > 34f4a52 apiserver: update API testdata at HEAD for flowcontrol%0A  > 3928298 Rebasing feature branch%0A  > e91ffd8 apiserver: add generated files for borrowing in flowcontrol%0A  > d961983 Update doc comments and change name of feature gate%0A  > fcd0d56 apiserver: add fields for borrowing in apf flowcontrol%0A  > adddac7 Small updates and comment fixes%0A  > 98c1aa6 Merge pull request # 113314 from cici37/celIntegration%0A  > 0d02273 Update generated protobuf files%0A  > 3f61c95 Merge pull request # 113688 from dashpole/update_utils%0A  > 8a0a045 API - make update%0A  > a5e7c66 Adding implementation of KEP-3335, StatefulSetSlice%0A  > 72a29bf Merge pull request # 113500 from kerthcet/feat/graduate-nodeInclusionPoplicy-to-beta%0A  > 2a2f510 update k8s.io/utils to fix util tracing panic%0A  > 891a1f8 Adding new api version of admissionregistration.k8s.io v1alpha1 for CEL in Admission Control%0A  > ee30dcf Merge pull request # 113047 from everpeace/improve-supplemental-groups-description%0A  > 2482389 Feat: graduate NodeInclusionPolicy to beta%0A  > a489930 Rename copy to v1alpha1%0A  > 9a33ad3 Merge pull request # 112360 from mimowo/handling-pod-failures-beta-kubelet%0A  > c4b2250 Improve the description of PodSecurityContext.SupplementalGroups (including cri-api)%0A  > 358a069 Copy over admissionregistration v1 to v1alpha1%0A  > 6c616e1 Merge pull request # 113510 from alculquicondor/finalizers-stable%0A  > 5210e2f Add pod disruption conditions for kubelet initiated failures%0A  > 2025045 Merge pull request # 113351 from andrewsykim/endpointslice-terminating-ga%0A  > aa2b4eb Graduate JobTrackingWithFinalizers to stable%0A  > 4bad656 Merge pull request # 113274 from Huang-Wei/kep-3521-A%0A  > aa9d0a7 k8s.io/api/discovery: remove API docs referencing EndpointSliceTerminatingCondition feature gate%0A  > 91f2496 Merge pull request # 113496 from avoltz/anvoltz/ga-itr%0A  > 686871f Automated codegen%0A  > c865c5c Promote ServiceInternalTrafficPolicy to GA%0A  > bd25e4f APIs, Validation and condition enforcements%0A  > 5448eb3 Merge pull request # 106242 from thockin/revive-copy-lb-status-type-to-ingress%0A  > edbfe77 Copy LoadBalancerStatus from core to networking%0A  > 6892570 Merge pull request # 112693 from aimuz/fix-GO-2022-0969%0A  > c5dc3f4 Fixed (CVE-2022-27664) Bump golang.org/x/net to v0.1.1-0.20221027164007-c63010009c80%0A  > 4e8dc44 Merge pull request # 111978 from Jefftree/aggregated-discovery-types%0A  > 72580e4 Add discovery types%0A  > 0184bd8 Merge pull request # 112643 from SergeyKanzhelev/removeDynamicKubeletConfig%0A  > 0f81104 Merge pull request # 112989 from ameukam/bump-golang.org/x/text-to-v0.3.8%0A  > f8118a1 remove DynamicKubeletConfig feature gate from the code%0A  > 370c8f0 Bump golang.org/x/text to v0.3.8%0A  > 3638040 Merge pull request # 112875 from pohly/update-yaml%0A  > 7ecab5c dependencies: update to sigs.k8s.io/yaml v1.3.0%0A  > 669318b Merge pull request # 112832 from tkashem/apf-prelifecycle-gen%0A  > 2cfef31 apiserver: prerelease-lifecycle-gen for flowcontrol%0A  > 3cedfad Merge pull request # 112306 from tkashem/v1beta3%0A  > 3814236 Merge pull request # 112707 from enj/enj/i/https_links%0A  > 418dd97 add testdata for flowcontrol v1beta3%0A  > ba008c5 Use https links for k8s KEPs, issues, PRs, etc%0A  > c96c62f rename assuredConcurrencyShares for flowcontrol v1beta3%0A  > be233f8 Merge pull request # 112673 from dims/update-to-latest-k8s.io/utils-sep-22%0A  > 51a3f54 add patch annotations to flowcontrol v1beta3%0A  > ca5be1f Update to latest k8s.io/utils to pick up changes%0A  > 7e203ee apiserver: generate for apf v1beta3%0A  > 79091da Merge pull request # 112577 from andrewsykim/feature-gate-cleanup%0A  > 19d0ef4 apiserver: enable v1beta3 for apf%0A  > 052d63f Merge pull request # 112545 from dims/update-etcd-3.5.5-and-all-otel-related-to-latest%0A  > 1f28922 remove +featureGate=LoadBalancerClass tag in service.spec.loadBalancerClass%0A  > f50a5b7 apiserver: apf rename copy to v1beta3%0A  > 9df3db1 updated etcd to v3.5.5 and newer otel libraries as well%0A  > bed6431 apiserver: copy apf v1beta2 to v1beta3%0A  > c98ebf1 Merge pull request # 112487 from liggitt/flowcontrol-test%0A  > 5c9e17a Add compatibility fixtures for v1beta2 flowcontrol%0A  > 9842651 Merge pull request # 111333 from flant/selfsubjectattributesreviews%0A  > 43df43b Add auth API to get self subject attributes%0A  > 30ff991 Merge pull request # 112349 from pohly/klog-update%0A  > e6114e9 build: update to klog v2.80.1%0A  > 929c3f0 Merge pull request # 112301 from aojea/ipv6_rfc3849%0A  > a687cab use IPv6 Address Prefix Reserved for Documentation for api docs%0A  > 6dd661f Merge pull request # 112199 from pohly/klog-update%0A  > 8a7d12c dependencies: update to klog v2.80.0%0A  > a6ff7c9 Merge pull request # 112146 from kerthcet/feat/move-schedulerError-to-api%0A  > ab89e44 Move constant schedulerError in scheduler to v1 package%0A  > d104994 Merge pull request # 112052 from tosi3k/bump-client-golang%0A  > 15b6dd2 Bump prometheus/client_golang to v1.13.0%0A  > 3be0a3c Merge pull request # 111974 from liggitt/1-25-compatibility%0A  > 49e055e Merge pull request # 111830 from t1anz0ng/typo%0A  > fcc83cd Drop 1.23 compatibility data%0A  > 64f80bd Merge pull request # 111611 from kardashov/ref-spec-docs-typo-fix%0A  > ea5df3a fix(typo): remove extra " from autoscaling doc string%0A  > 4cde1ad Add 1.25 compatibility data%0A  > 2e7b661 Merge pull request # 111657 from aojea/hc_nodeport%0A  > d07af88 Generate specs after fixing typo in documentation%0A  > 649256a Fix typo in field description.%0Abumping knative.dev/eventing-kafka 9a4a93a...d7072e0:%0A  > d7072e0 upgrade to latest dependencies (# 1356)%0A  > d047934 Update community files (# 1357)%0A  > d4716b7 upgrade to latest dependencies (# 1355)%0A  > 9ca5fa0 Update community files (# 1354)%0A  > 90a8ba9 upgrade to latest dependencies (# 1353)%0A  > 561d00f upgrade to latest dependencies (# 1352)%0A  > 22b1fff upgrade to latest dependencies (# 1351)%0A  > 77507bf upgrade to latest dependencies (# 1349)%0A  > 6d6530f Update community files (# 1348)%0A  > a6f4f44 upgrade to latest dependencies (# 1344)%0A  > 2558e87 Update community files (# 1346)%0A  > 86dda64 Update dependencies and fix compile issues (# 1345)%0A  > d9a13fc upgrade to latest dependencies (# 1342)%0A  > a3ee5d5 Update community files (# 1343)%0A  > 9c2c601 upgrade to latest dependencies (# 1340)%0A  > 0b7e0ac upgrade to latest dependencies (# 1339)%0A  > 62d8873 upgrade to latest dependencies (# 1338)%0A  > 870d89a Update community files (# 1337)%0Abumping golang.org/x/term d974fe8...119f703:%0A  > 119f703 go.mod: update golang.org/x dependencies%0A  > 7ae6be6 go.mod: update golang.org/x dependencies%0A  > 0edf009 go.mod: update golang.org/x dependencies%0Abumping google.golang.org/api a039966...63d06ab:%0A  > 63d06ab chore(main): release 0.124.0 (# 1990)%0A  > 73f57fe feat(all): auto-regenerate discovery clients (# 1991)%0A  > 8c0e6d9 chore: add yoshi-approver ownership (# 1994)%0A  > 7843046 chore(all): update all (# 1992)%0A  > 94c12ed chore(all): update module github.com/google/s2a-go to v0.1.4 (# 1989)%0A  > 0b4f4af feat(all): auto-regenerate discovery clients (# 1988)%0A  > 2721e1f chore: enable GoApiaryCodegen auto-approve (# 1987)%0A  > a241c25 chore: delete broken AutoApprove (# 1986)%0A  > 3e2d6a6 chore: trigger AutoApprove on reopen as well (# 1985)%0A  > a24a28a chore: give AutoApprove job full write (# 1984)%0A  > 8210800 chore(main): release 0.123.0 (# 1975)%0A  > f31b763 feat(all): auto-regenerate discovery clients (# 1982)%0A  > d27f40f feat(all): auto-regenerate discovery clients (# 1978)%0A  > 94d3d73 chore(ci): fix AutoApprove for discogen (# 1981)%0A  > 98b3073 feat(all): auto-regenerate discovery clients (# 1974)%0A  > d5e0fb2 chore(main): release 0.122.0 (# 1972)%0A  > ab64815 feat(all): auto-regenerate discovery clients (# 1973)%0A  > 8b0974e fix: add better support of array of floats (# 1971)%0A  > cf0df64 chore(main): release 0.121.0 (# 1962)%0A  > c2c2b59 feat(all): auto-regenerate discovery clients (# 1963)%0A  > e44a771 chore(all): update module github.com/google/s2a-go to v0.1.3 (# 1965)%0A  > 2068ba5 feat(all): auto-regenerate discovery clients (# 1961)%0A  > c2018e2 chore(main): release 0.120.0 (# 1956)%0A  > 4e35cac feat(all): auto-regenerate discovery clients (# 1960)%0A  > fcd007a feat(all): auto-regenerate discovery clients (# 1958)%0A  > 289b859 feat(all): auto-regenerate discovery clients (# 1957)%0A  > 409bc9d feat(all): auto-regenerate discovery clients (# 1955)%0A  > 0909f16 chore(main): release 0.119.0 (# 1944)%0A  > 2f54150 chore(deps): update s2a-go to v0.1.2 (# 1954)%0A  > 685ec81 feat: add an option to enable DirectPath xDS (# 1942)%0A  > d85769c feat(all): auto-regenerate discovery clients (# 1953)%0A  > 4cb8eb9 feat(all): auto-regenerate discovery clients (# 1952)%0A  > bf9f3ac chore(all): update google.golang.org/genproto digest to daa745c (# 1949)%0A  > e1eda57 feat(all): auto-regenerate discovery clients (# 1948)%0A  > a0dacd5 feat(all): auto-regenerate discovery clients (# 1947)%0A  > e8b93cb chore(deps): update s2a-go to v0.1.1 (# 1945)%0A  > 690068f feat(all): auto-regenerate discovery clients (# 1943)%0A  > 2d6890a chore(main): release 0.118.0 (# 1940)%0A  > 29dc45a feat(all): auto-regenerate discovery clients (# 1941)%0A  > ac94a0f feat(all): auto-regenerate discovery clients (# 1939)%0A  > 8019ef6 chore(main): release 0.117.0 (# 1931)%0A  > 750c7c8 feat(all): auto-regenerate discovery clients (# 1936)%0A  > 3a98290 chore(all): update all (# 1937)%0A  > 3f62830 chore(deps): bump golang.org/x/crypto (# 1930)%0A  > 2219681 feat(all): auto-regenerate discovery clients (# 1935)%0A  > 2efcb2e feat(all): auto-regenerate discovery clients (# 1932)%0A  > 3c61729 feat: add experimental s2a-go integration (# 1874)%0A  > 587b9e5 chore(main): release 0.116.0 (# 1929)%0A  > 28c8cd5 feat(all): auto-regenerate discovery clients (# 1928)%0A  > feafcdc chore(main): release 0.115.0 (# 1922)%0A  > 34781cf feat(all): auto-regenerate discovery clients (# 1927)%0A  > 33a2dfe feat(all): auto-regenerate discovery clients (# 1924)%0A  > 02cfb82 chore(all): update google.golang.org/genproto digest to dcfb400 (# 1925)%0A  > 8930f0e feat(all): auto-regenerate discovery clients (# 1923)%0A  > 1c955e8 feat(all): auto-regenerate discovery clients (# 1913)%0A  > 7f87838 chore(all): update all (# 1918)%0A  > be028cf chore(gensupport): add idempotency header (# 1916)%0A  > 649bfb9 chore(all): update all (# 1914)%0A  > 5ac4fd7 test: update test due to generator change (# 1912)%0A  > f79df48 chore(main): release 0.114.0 (# 1910)%0A  > 2754ab4 feat(all): auto-regenerate discovery clients (# 1907)%0A  > dc4b77d fix: always reference the internal package. (# 1909)%0A  > b8a2a5e chore(main): release 0.113.0 (# 1901)%0A  > fc221ce feat(all): auto-regenerate discovery clients (# 1900)%0A  > e63383f chore(all): update module google.golang.org/protobuf to v1.29.1 [SECURITY] (# 1906)%0A  > 64b6ee4 feat(idtoken): add support for external_account (# 1897)%0A  > 65cafd4 chore(all): update all (# 1902)%0A  > 63c48a6 feat(transport): add support for setting quota project with envvar (# 1892)%0A  > 225fa6b internal: Refactor cert logic to support OAuth2 token exchange over mTLS (# 1886)%0A  > 8d4d70d chore(main): release 0.112.0 (# 1883)%0A  > 89c274a feat(all): auto-regenerate discovery clients (# 1898)%0A  > 9f18671 feat(all): auto-regenerate discovery clients (# 1896)%0A  > e88ee8a feat(all): auto-regenerate discovery clients (# 1893)%0A  > 5da4d6a feat(all): auto-regenerate discovery clients (# 1887)%0A  > 6bd0840 chore(deps): bump golang.org/x/crypto in /internal/kokoro/discogen (# 1890)%0A  > 2f72016 chore(all): update all (# 1888)%0A  > c886360 feat(all): auto-regenerate discovery clients (# 1885)%0A  > 1aee5cd feat(all): auto-regenerate discovery clients (# 1884)%0A  > 15808d7 feat(all): auto-regenerate discovery clients (# 1882)%0A  > e99d0d5 chore(main): release 0.111.0 (# 1860)%0A  > 70d3954 feat(all): auto-regenerate discovery clients (# 1875)%0A  > f32872c chore(all): update google.golang.org/genproto digest to 637eb22 (# 1877)%0A  > c02cff6 feat(all): auto-regenerate discovery clients (# 1873)%0A  > 7d34d41 feat(all): auto-regenerate discovery clients (# 1872)%0A  > d456fd6 chore(deps): bump golang.org/x/net in /internal/kokoro/discogen (# 1870)%0A  > b7ab21d chore(all): update all (# 1868)%0A  > 7f5f40a feat(all): auto-regenerate discovery clients (# 1866)%0A  > 4056319 chore(all): update module golang.org/x/net to v0.7.0 [SECURITY] (# 1867)%0A  > 8b8b195 feat(all): auto-regenerate discovery clients (# 1863)%0A  > c0f2510 chore(all): update vet.sh to go runtime 1.20 (# 1865)%0A  > 895105a feat(all): auto-regenerate discovery clients (# 1861)%0A  > ba3414e feat(all): auto-regenerate discovery clients (# 1859)%0A  > 892811c chore(main): release 0.110.0 (# 1840)%0A  > 1edc79b chore: update x libs (# 1858)%0A  > 929a393 chore(all): update all (# 1853)%0A  > 1147cb8 fix: Update ECP dependency to v0.2.3 (# 1857)%0A  > 689f934 feat(all): auto-regenerate discovery clients (# 1851)%0A  > 8efd00d fix(internal/gensupport): don't prematurely close timers (# 1856)%0A  > 3fb5b61 fix: Improve error handling for enterprise certificate module (# 1848)%0A  > 8980266 feat(all): auto-regenerate discovery clients (# 1850)%0A  > 3fb8cdc feat(all): auto-regenerate discovery clients (# 1841)%0A  > 1651c38 chore(transport): remove support for go runtimes earlier than 1.16 (# 1844)%0A  > 4b4c9d4 feat(all): auto-regenerate discovery clients (# 1838)%0A  > b3b5f17 chore(main): release 0.109.0 (# 1818)%0A  > c13cc35 feat(all): auto-regenerate discovery clients (# 1836)%0A  > 602b6a4 chore(all): update all (major) (# 1806)%0A  > a5d0daa feat(all): auto-regenerate discovery clients (# 1828)%0A  > 50fc7c4 feat(all): auto-regenerate discovery clients (# 1826)%0A  > 6aad438 feat(all): auto-regenerate discovery clients (# 1825)%0A  > 85d0224 feat(all): auto-regenerate discovery clients (# 1822)%0A  > 884a246 feat(all): auto-regenerate discovery clients (# 1821)%0A  > 5935892 feat(all): auto-regenerate discovery clients (# 1819)%0A  > ba3ba78 feat(all): auto-regenerate discovery clients (# 1817)%0A  > 47f66d6 chore(main): release 0.108.0 (# 1811)%0A  > da48b9a feat(all): auto-regenerate discovery clients (# 1816)%0A  > a12685c feat(all): auto-regenerate discovery clients (# 1813)%0A  > 4df52d2 feat(all): auto-regenerate discovery clients (# 1810)%0A  > f74fbb6 chore(main): release 0.107.0 (# 1803)%0A  > d8084e4 feat(all): auto-regenerate discovery clients (# 1809)%0A  > 4dca4e0 feat: re-enable integrations:v1 (# 1801)%0A  > 86e4009 fix: user Timers over time.After (# 1802)%0A  > bcc345c feat(all): auto-regenerate discovery clients (# 1808)%0A  > de06921 feat(all): auto-regenerate discovery clients (# 1807)%0A  > 935ef64 feat(all): auto-regenerate discovery clients (# 1804)%0A  > 93de455 feat(all): auto-regenerate discovery clients (# 1800)%0A  > ac7eb8f chore(main): release 0.106.0 (# 1786)%0A  > 3944e86 feat(all): auto-regenerate discovery clients (# 1794)%0A  > f6dec99 feat(idtoken): add support for impersonated_service_account creds type (# 1792)%0A  > ddb5c65 test: add buffer to both sides of token expiry validation (# 1797)%0A  > b35900a fix(idtoken): configure validator constructor to use no authentication (# 1789)%0A  > ca86833 chore(all): update all (# 1796)%0A  > a6b0739 chore: skip generating integrations:v1 as it fails generation (# 1793)%0A  > 7bd17b3 feat(all): auto-regenerate discovery clients (# 1790)%0A  > 9fb35f5 feat(all): auto-regenerate discovery clients (# 1788)%0A  > 1569e5b feat(option/internaloption): add new EmbeddableAdapter option (# 1787)%0A  > a7f08e2 feat(all): auto-regenerate discovery clients (# 1784)%0A  > 67aaf4e chore(main): release 0.105.0 (# 1774)%0A  > 5b02761 feat(all): auto-regenerate discovery clients (# 1777)%0A  > c58bf4c feat: support set null map entries for non-simple map values (# 1782)%0A  > e4271df feat(googleapi): add response headers to Error reported by CheckMediaResponse (# 1781)%0A  > 6193507 chore: remove uses of obsolete golang.org/x/xerrors (# 1776)%0A  > 37a2e41 feat(all): auto-regenerate discovery clients (# 1773)%0A  > 9255b0b chore(main): release 0.104.0 (# 1748)%0A  > 4238314 chore: ignore some golang.org/x/* dependencies in renovate (# 1772)%0A  > 029b659 chore(all): update all (# 1768)%0A  > f819644 feat(all): auto-regenerate discovery clients (# 1771)%0A  > 2b596d9 feat(all): auto-regenerate discovery clients (# 1767)%0A  > 3195ce1 feat(all): auto-regenerate discovery clients (# 1766)%0A  > 97a9846 feat(all): auto-regenerate discovery clients (# 1760)%0A  > 8d8f0a7 feat(transport): de-experiment google-c2p resolver (# 1757)%0A  > c213153 fix(transport/grpc): separate resolution of creds and certs (# 1759)%0A  > 629e217 fix(idtoken): increase MaxIdleConnsPerHost to 100 in NewClient (# 1754)%0A  > caf7af0 feat(all): auto-regenerate discovery clients (# 1755)%0A  > e18b504 feat(all): auto-regenerate discovery clients (# 1753)%0A  > dd565a4 feat(all): auto-regenerate discovery clients (# 1752)%0A  > a657f19 feat(all): auto-regenerate discovery clients (# 1751)%0A  > 292129c feat(all): auto-regenerate discovery clients (# 1746)%0A  > 02077fd chore(all): update all (# 1749)%0A  > 567070f docs: document limitation of WithUserAgent (# 1747)%0A  > 561b601 chore(main): release 0.103.0 (# 1738)%0A  > 4248dc3 feat(all): auto-regenerate discovery clients (# 1743)%0A  > ee25e29 feat(googleapi): inject gax apierror.APIError into googleapi.Error (# 1730)%0A  > f8efb95 chore(all): update all (# 1740)%0A  > 9695aa1 feat: rm hard dep on x/sys (# 1742)%0A  > bec0f29 chore(.github): force renovate to use 1.19 (# 1741)%0A  > bbd4259 feat(all): auto-regenerate discovery clients (# 1739)%0A  > de99200 feat(all): auto-regenerate discovery clients (# 1737)%0A  > 0d7f97a chore(main): release 0.102.0 (# 1726)%0A  > 0528475 feat: rely on new compute metadata module directly (# 1736)%0A  > ce57a67 feat(all): auto-regenerate discovery clients (# 1734)%0A  > 1e1eab9 feat(all): auto-regenerate discovery clients (# 1727)%0A  > 0ce5403 test(transport/grpc): fix arg for test failure logs (# 1733)%0A  > 06360d8 feat(all): auto-regenerate discovery clients (# 1725)%0A  > 644a13c chore(main): release 0.101.0 (# 1719)%0A  > f4788b3 feat(all): auto-regenerate discovery clients (# 1723)%0A  > 9ea2ceb chore(all): update all (# 1721)%0A  > 9140608 feat(all): auto-regenerate discovery clients (# 1720)%0A  > 453b81a feat(all): auto-regenerate discovery clients (# 1718)%0A  > d530a93 chore(main): release 0.100.0 (# 1714)%0A  > 37f90e9 feat(internal/gensupport): remove DetermineContentType, use gax-go copy (# 1716)%0A  > b235b1f fix(idtoken): Allow missing age in http response header (# 1715)%0A  > f990a2a feat(all): auto-regenerate discovery clients (# 1717)%0A  > f9e15f2 feat(all): auto-regenerate discovery clients (# 1712)%0A  > e74b770 chore(all): update all (# 1713)%0A  > 977e871 chore(main): release 0.99.0 (# 1710)%0A  > 6b81c83 feat(all): auto-regenerate discovery clients (# 1701)%0A  > 1aa1deb chore(all): update all (# 1707)%0A  > 69fb474 chore: Update ECP dependency to 0.2.0 (# 1704)%0A  > a4ae94d chore(main): release 0.98.0 (# 1700)%0A  > 25b7450 feat(all): auto-regenerate discovery clients (# 1699)%0A  > aa775b4 feat(all): auto-regenerate discovery clients (# 1696)%0A  > faa845a chore(main): release 0.97.0 (# 1694)%0A  > 2c3e863 fix(gensupport): allow initial request for resumable uploads to retry w/ non-nil getBody (# 1690)%0A  > f427ee3 feat(internal/gensupport): wrap retry failures with context and prev error (# 1684)%0A  > 6b0515b fix: build script bash error (# 1697)%0A  > b8f2556 feat(all): auto-regenerate discovery clients (# 1695)%0A  > a87400b feat(all): auto-regenerate discovery clients (# 1693)%0Abumping golang.org/x/time f3bd1da...2c09566:%0A  > 2c09566 rate: the state of the limiter should not be changed when the requests failed%0A  > 80b9fac x/time/rate: add rate.Sometimes, which runs a function occasionally.%0Abumping google.golang.org/genproto 68c0371...daa745c:%0A  > daa745c chore(all): update all (# 1001)%0A  > c38d8f0 chore(all): auto-regenerate .pb.go files (# 1000)%0A  > dcfb400 chore(all): auto-regenerate .pb.go files (# 999)%0A  > 3801387 chore(all): auto-regenerate .pb.go files (# 998)%0A  > c0448cd chore(all): auto-regenerate .pb.go files (# 997)%0A  > 6ac7f18 chore: remove protos for recent google-cloud-go clients (# 996)%0A  > dc694ad chore(all): auto-regenerate .pb.go files (# 995)%0A  > 478b75c chore(all): auto-regenerate .pb.go files (# 994)%0A  > db269f9 fix: remove broken aliases and tidy (# 993)%0A  > 21a4fbf chore(all): update all (# 988)%0A  > 5ad98d5 chore(all): update all (major) (# 990)%0A  > cde4c94 chore(all): auto-regenerate .pb.go files (# 992)%0A  > 7606e75 chore(all): auto-regenerate .pb.go files (# 991)%0A  > 1fe4d14 fix: remove beta no longer generated (# 989)%0A  > 7f2fa6f chore(all): update all (# 987)%0A  > daab25a chore(all): auto-regenerate .pb.go files (# 986)%0A  > e74f57a fix: run go build and fixup (# 984)%0A  > 9ab4bdc chore(all): update vet.sh to go runtime 1.20 (# 976)%0A  > 024586e fix: update sums (# 983)%0A  > 9b19f0b chore(all): update all (# 982)%0A  > 637eb22 chore(all): auto-regenerate .pb.go files (# 981)%0A  > 10f96fb chore(all): auto-regenerate .pb.go files (# 980)%0A  > ace64dc chore(deps): bump golang.org/x/net from 0.6.0 to 0.7.0 (# 978)%0A  > c8e22ba feat: alias some protos (# 977)%0A  > 0dfe4f8 chore(all): auto-regenerate .pb.go files (# 973)%0A  > 008b390 chore(all): auto-regenerate .pb.go files (# 971)%0A  > 1c01626 chore(all): auto-regenerate .pb.go files (# 970)%0A  > 596548e chore(all): auto-regenerate .pb.go files (# 968)%0A  > dcaf20b chore(all): auto-regenerate .pb.go files (# 967)%0A  > 31e0e69 chore(all): auto-regenerate .pb.go files (# 966)%0A  > 2c411cf chore(all): auto-regenerate .pb.go files (# 965)%0A  > 9d59e20 chore(all): auto-regenerate .pb.go files (# 964)%0A  > 28d6b97 chore(all): auto-regenerate .pb.go files (# 963)%0A  > dbe35b8 chore(all): auto-regenerate .pb.go files (# 962)%0A  > e10362b chore(all): auto-regenerate .pb.go files (# 961)%0A  > 76db087 chore(all): auto-regenerate .pb.go files (# 960)%0A  > 3c3c17c chore(all): auto-regenerate .pb.go files (# 959)%0A  > a12b697 chore(all): auto-regenerate .pb.go files (# 958)%0A  > caabf58 chore(all): auto-regenerate .pb.go files (# 957)%0A  > f9683d7 chore(all): auto-regenerate .pb.go files (# 954)%0A  > 23e4bf6 feat: add generated aliases for new clients (# 953)%0A  > b1a01be chore(all): auto-regenerate .pb.go files (# 952)%0A  > 8222ab4 feat: generate aliases for iam clients (# 951)%0…

---
## [Steelpoint/cmss13](https://github.com/Steelpoint/cmss13)@[d045a5d654...](https://github.com/Steelpoint/cmss13/commit/d045a5d6547dcda9fc04be9b6cd50d2ff44e672f)
#### Tuesday 2023-07-11 15:21:29 by Drathek

Larva Queue Late Joiner Nerf (#3803)

# About the pull request

This PR makes it so players who haven't played yet have their join time
recorded, and that is used for their initial sorting value rather than
0. This means late joiners will be at the back of the line as if they
had just died.

This PR also fixes an oversight where ghosting as a facehugger would
count as death. Even though they really shouldn't be ghosting when
alive, they still shouldn't be penalized as far as the queue is
concerned.

# Explain why it's good for the game

Its not; its a bad experience for everyone that hasn't even gotten one
life in the round. However it seems I'm in the minority thinking that a
xeno shouldn't squander their first life and that death shouldn't bear
more consequences.

# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

The new informational message if you press join as xeno while currently
ineligible to be a xeno candidate:

![image](https://github.com/cmss13-devs/cmss13/assets/76988376/9fb295c2-e654-4843-9e3e-bf37f2c8755e)

</details>


# Changelog
:cl: Drathek
del: Remove first life priority for larva queue
fix: Fix ghosting as a facehugger counting as death for the larva queue
/:cl:

---
## [openMSX/openMSX](https://github.com/openMSX/openMSX)@[cdfb8e07ef...](https://github.com/openMSX/openMSX/commit/cdfb8e07efacfa3d3e0d5e709552ce36f89e69d1)
#### Tuesday 2023-07-11 15:55:44 by m9710797

Tweak connector menu

A mix of the previous versions:
* Display the connector as the description, so "MSX Joystick Port A"
  instead of "joyporta".
* Display the pluggable as the name, so "magic-key" instead of "Dongle
  used by some Japanese games to enable cheat mode".
* Show the pluggable description as a tooltip.

Disadvantage of this version is that all 4 joytap / ninjatap ports are now
shown as "Joy Tap port" / "Ninja Tap port" (this used to be
"joytap_port_1" etc). Maybe we should fix this in the implementation of
the joytap/ninjatap code instead of in the GUI?

---
## [cristobalcl/langchain](https://github.com/cristobalcl/langchain)@[75fb9d2fdc...](https://github.com/cristobalcl/langchain/commit/75fb9d2fdcc201e80ad9c065a02c6cc9ccf6d716)
#### Tuesday 2023-07-11 16:06:41 by Stefano Lottini

Cassandra support for chat history using CassIO library (#6771)

### Overview

This PR aims at building on #4378, expanding the capabilities and
building on top of the `cassIO` library to interface with the database
(as opposed to using the core drivers directly).

Usage of `cassIO` (a library abstracting Cassandra access for
ML/GenAI-specific purposes) is already established since #6426 was
merged, so no new dependencies are introduced.

In the same spirit, we try to uniform the interface for using Cassandra
instances throughout LangChain: all our appreciation of the work by
@jj701 notwithstanding, who paved the way for this incremental work
(thank you!), we identified a few reasons for changing the way a
`CassandraChatMessageHistory` is instantiated. Advocating a syntax
change is something we don't take lighthearted way, so we add some
explanations about this below.

Additionally, this PR expands on integration testing, enables use of
Cassandra's native Time-to-Live (TTL) features and improves the phrasing
around the notebook example and the short "integrations" documentation
paragraph.

We would kindly request @hwchase to review (since this is an elaboration
and proposed improvement of #4378 who had the same reviewer).

### About the __init__ breaking changes

There are
[many](https://docs.datastax.com/en/developer/python-driver/3.28/api/cassandra/cluster/)
options when creating the `Cluster` object, and new ones might be added
at any time. Choosing some of them and exposing them as `__init__`
parameters `CassandraChatMessageHistory` will prove to be insufficient
for at least some users.

On the other hand, working through `kwargs` or adding a long, long list
of arguments to `__init__` is not a desirable option either. For this
reason, (as done in #6426), we propose that whoever instantiates the
Chat Message History class provide a Cassandra `Session` object, ready
to use. This also enables easier injection of mocks and usage of
Cassandra-compatible connections (such as those to the cloud database
DataStax Astra DB, obtained with a different set of init parameters than
`contact_points` and `port`).

We feel that a breaking change might still be acceptable since LangChain
is at `0.*`. However, while maintaining that the approach we propose
will be more flexible in the future, room could be made for a
"compatibility layer" that respects the current init method. Honestly,
we would to that only if there are strong reasons for it, as that would
entail an additional maintenance burden.

### Other changes

We propose to remove the keyspace creation from the class code for two
reasons: first, production Cassandra instances often employ RBAC so that
the database user reading/writing from tables does not necessarily (and
generally shouldn't) have permission to create keyspaces, and second
that programmatic keyspace creation is not a best practice (it should be
done more or less manually, with extra care about schema mismatched
among nodes, etc). Removing this (usually unnecessary) operation from
the `__init__` path would also improve initialization performance
(shorter time).

We suggest, likewise, to remove the `__del__` method (which would close
the database connection), for the following reason: it is the
recommended best practice to create a single Cassandra `Session` object
throughout an application (it is a resource-heavy object capable to
handle concurrency internally), so in case Cassandra is used in other
ways by the app there is the risk of truncating the connection for all
usages when the history instance is destroyed. Moreover, the `Session`
object, in typical applications, is best left to garbage-collect itself
automatically.

As mentioned above, we defer the actual database I/O to the `cassIO`
library, which is designed to encode practices optimized for LLM
applications (among other) without the need to expose LangChain
developers to the internals of CQL (Cassandra Query Language). CassIO is
already employed by the LangChain's Vector Store support for Cassandra.

We added a few more connection options in the companion notebook example
(most notably, Astra DB) to encourage usage by anyone who cannot run
their own Cassandra cluster.

We surface the `ttl_seconds` option for automatic handling of an
expiration time to chat history messages, a likely useful feature given
that very old messages generally may lose their importance.

We elaborated a bit more on the integration testing (Time-to-live,
separation of "session ids", ...).

### Remarks from linter & co.

We reinstated `cassio` as a dependency both in the "optional" group and
in the "integration testing" group of `pyproject.toml`. This might not
be the right thing do to, in which case the author of this PR offer his
apologies (lack of confidence with Poetry - happy to be pointed in the
right direction, though!).

During linter tests, we were hit by some errors which appear unrelated
to the code in the PR. We left them here and report on them here for
awareness:

```
langchain/vectorstores/mongodb_atlas.py:137: error: Argument 1 to "insert_many" of "Collection" has incompatible type "List[Dict[str, Sequence[object]]]"; expected "Iterable[Union[MongoDBDocumentType, RawBSONDocument]]"  [arg-type]
langchain/vectorstores/mongodb_atlas.py:186: error: Argument 1 to "aggregate" of "Collection" has incompatible type "List[object]"; expected "Sequence[Mapping[str, Any]]"  [arg-type]

langchain/vectorstores/qdrant.py:16: error: Name "grpc" is not defined  [name-defined]
langchain/vectorstores/qdrant.py:19: error: Name "grpc" is not defined  [name-defined]
langchain/vectorstores/qdrant.py:20: error: Name "grpc" is not defined  [name-defined]
langchain/vectorstores/qdrant.py:22: error: Name "grpc" is not defined  [name-defined]
langchain/vectorstores/qdrant.py:23: error: Name "grpc" is not defined  [name-defined]
```

In the same spirit, we observe that to even get `import langchain` run,
it seems that a `pip install bs4` is missing from the minimal package
installation path.

Thank you!

---
## [superrosko/api-tools-rest](https://github.com/superrosko/api-tools-rest)@[dde0d361e6...](https://github.com/superrosko/api-tools-rest/commit/dde0d361e655a85bd07c150eb56976d6d6ac70ea)
#### Tuesday 2023-07-11 16:26:57 by Michał Bundyra

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
## [s-sutton/s-sutton](https://github.com/s-sutton/s-sutton)@[4b50ee750d...](https://github.com/s-sutton/s-sutton/commit/4b50ee750d918565ab0486b457fbae71bcc1f99c)
#### Tuesday 2023-07-11 16:27:13 by S. Sutton

Update README.md, added malicious packets to interests

Generally, my interest lies in low-level exploitation in general, and the lowest level (outside of pure hardware) in host-based exploitation is the kernel and in network-based exploitation is packet injection.

For me, these low-level exploits feel ineffably intimate. Higher levels of abstraction feel like they're distancing themselves too much from the processes that are actually occurring. Low-level hacking feels like I understand the machines better than their own users and I'm gaining their allegiance through that mutual understanding.

On top of that, while hacks that take place in userspace like web hacking and application hacking are rather glamorous, I like the idea of climbing down into the metaphorical crawlspace of machine code to sneak underneath userspace entirely by navigating code that is much less human-readable. It's a romantic notion of stealthily attacking through an often-overlooked undercroft.

Plus, when you chain malicious packet injection with kernel exploitation, you have a remote exploit that doesn't rely on the user at all. It requires no social engineering to install trojans and, often, can be done without exploiting misconfigurations in applications, too. In a way, it feels like a "pure" hack, since it deals directly in exploiting the foundational low-level code everything runs on, which makes it all the more satisfying to pull off.

Not that this matters too much, since I'm still a noob, but it is a topic that I find absolutely fascinating. I want to learn as much as I can about these topics and this specific attack chain of malicious packet + kernel exploit. While I didn't know enough to put a name to it, this sort of attack is what's drawn my interest towards hacking since I was in elementary school.

That's probably partially inspired by legends about 1x1x1x1 from ROBLOX, honestly, lol. That's what got me into Lua scripting, which ultimately lead to me doing shell exploitation on school computers in middle school, and so on. While the ROBLOX gray hat wasn't a low-level hacker, it did introduce me to the idea of delving into a deeper layer than ordinary userspace in order to modify a system.

That obviously includes finding vulnerabilities on those lower levels and exploiting them, but I like to think of them less like vulnerabilities and more like doors the machines leave open for those who care enough to find them. Weird metaphor, but nobody actually reads these updates so I can pour my heart out into them without judgment.

I guess these updates function kind of like a blog, huh?

---
## [s-sutton/s-sutton](https://github.com/s-sutton/s-sutton)@[31d2a86237...](https://github.com/s-sutton/s-sutton/commit/31d2a86237beb01bc0ec5dec24e6d00807739903)
#### Tuesday 2023-07-11 16:52:53 by S. Sutton

Update README.md, added more projects

These projects are getting a little out of hand. I'm not sure they function as a straightforward to-do list anymore, because I have half a mind to skip down Linux From Scratch and go from there.

I've been so focused on eJPT and I've been so sick that I haven't had the time or mental resources to work on these other projects. I can still work from when I wake up to when I sleep, but my progress is a lot slower than it used to be. I just spent two weeks out of commission due to starting immunotherapy, which put me more behind schedule than I was hoping for.

I am frustrated by these constant setbacks and the growing list of what I want to accomplish. The upside is that I know exactly what I want to focus on, what I want to achieve, and how to go about doing it. This is a level of clarity and passion that I think most people can only dream of, and I'm basically certain that I won't ever experience a mid-life crisis or anything that will dramatically alter my life trajectory later on, either.

I'm trying to remember that the pandemic severely hindered most people my age. I'm not the only one that had my college life destroyed by those events, even though many people my age were still somehow able to continue mostly unaffected.

I was impacted to a greater degree, and it's not like I was on the right course before the pandemic, either, but I think I can pull all of this off. It only feels overwhelming when I look at this list as a whole instead of focusing on each element step-by-step, because this list will probably take at least a couple of years to finish, if not more.

I just have to pace myself and remember that it's a marathon, not a race. I'll be able to accomplish larger workloads as I get back into the swing of things, because hopefully the days of chronic illness are finally behind me now.

I've been reading up on how people in East Asian countries cope with higher workloads and are able to work essentially from waking to sleeping, and I think I can do that, too. It's going to be a little exhausting at first, but as long as I pace myself and focus on just doing what I can to stay on course, I should adapt to the workload.

I don't know how much of an advantage that will give me in the offensive security scene. I know it's a hyper-competitive field as it is. I'm trying to not worry about it and just focus on the work in front of me. Everywhere I turn online, people are highly pessimistic and negative about getting a pentesting job with no experience, but the actual people in the industry that I've connected to have told me that I can do it, which is more encouraging.

It sometimes feels like a futile struggle, still, but I'm not going to give up. This is what I want from life. I would never forgive myself if I didn't put 110% into achieving it. So I'll add more projects, knowing that I WILL get to them some day, even if they feel out of reach right now. I will look at this list every few days to remember what I'm striving towards.

You hear that, DEFCON and Jack Rhysider? I'm a nobody now, but one day it will be impossible to ignore what I've accomplished. It's only a matter of time.

...I hope.

---
## [Anzarot121/space-station-14](https://github.com/Anzarot121/space-station-14)@[06747e0f7e...](https://github.com/Anzarot121/space-station-14/commit/06747e0f7e7d04cf87e63a359a3a86b1a35442cc)
#### Tuesday 2023-07-11 17:26:17 by Emisse

some silly paintings and posters (#17872)

* webedit

* Update meta.json

* god is real hes here with us

* so true

* so truers rise

* worst meta.json ive seen in my life

* so true

---
## [crawl/crawl](https://github.com/crawl/crawl)@[1880023187...](https://github.com/crawl/crawl/commit/18800231877e12caceb48c2f929f842d55aac934)
#### Tuesday 2023-07-11 17:26:41 by Nicholas Feinberg

Tweak forms

This change is intended to allow more opportunities for players to shift
into or out of a 'transmuter' playstyle, to improve the UI of forms, and to
improve some miscellaneous issues, e.g. Lichform being useless in 3-rune games.
For more context, see https://github.com/crawl/crawl/wiki/Transmutations-Reform.

Throughout, balance is a very rough sketch. I expect many things will need to
be buffed, others will need to be nerfed, and some will need to be replaced
entirely. This is a grand experiment, not a final state.

Talismans
---------

The largest change is that forms are no longer entered via spells. Instead,
special items called 'talismans' must be found and evoked. Once entered,
these 'talisman forms' last indefinitely.

Further notes on talismans:
- Talismans scale only on Shapeshifting skill (more on this later). They
  do not care about Int, Spellcasting, other spell schools, wizardry, or
  encumbrance. (That is, they aren't spells.)
- Talisman forms have a 'minimum skill'. Below that skill, entering the
  talisman form will reduce the user's maximum HP (while in the form).
  This is intended to roughly mimic the inability to effectively cast
  spells at low skills/high fail% - it provides a space in which an 'early'
  form can be better than a 'later' one, even if you've found both.
- Talisman forms have a 'maximum skill'. Above that skill, no further
  scaling applies. This is intended to roughly mimic max spellpower - it
  makes it more obvious that later-game forms will end up outscaling
  earlier ones.
- It takes 5 turns to enter or leave a talisman form, exactly as with
  armour or amulets. Use of a talisman form is intended to be a strategic
  decision, again like wearing armour, rather than something swapped in
  each fight.
- Talismans don't need to be held after they're used. You can evoke them
  from the floor and leave them there. This avoids inventory pressure.
- Talismans can be used with Sacrifice Artifice, since they don't use Evo.
- Zin instantly excommunicates users of a talisman. Take that, nerds!
- Trog is A-OK with talismans, just as with wands, magic swords, etc.

Art for talismans is pending.

Skills
------

Transmutations skill has been split in two. Talismans use a new skill,
Shapeshifting, and remaining Transmutations spells (of which there are
still nine, more than one other school!) continue to use Transmutations
skill. There was very little synergy or overlap between forms and Tmut
spells, and this makes it easier to make skilling decisions. Some argue
that Transmutations should be abolished entirely and its spells punted
into other schools; we'll see.

Shapeshifting aptitudes look broadly like Transmutations aptitudes,
with a -2 penalty applied so that forms are costly enough now that
they're all "single-school" and don't require Int. (That is, Humans
have a Shapeshifting apt of -2, etc.) A few species have had their
apts adjusted to account for the new role of Shapeshifting, but more
could be done here.

Background
----------

The Transmuter background has been replaced with a Shapeshifter, who
starts with a beast talisman and no spells. Their stats have been
adjusted accordingly.

Forms
-----

The following forms exist:

*Beast*: This is the starting form for the Shapeshifter background. It
melds all aux armours in exchange for a Slaying bonus (ala Wereblood) -
+2 at 0 skill, +8 at 13 skill (max).

This is intended to provide a bonus which is compelling early game (when no
or few aux armours have been found) but more tenuous later, especially for
non-transmuters. It's also intended to provide a bridge between Tmut and
weapon use, since a transmuter who finds a great weapon can switch from UC
to that weapon without giving up their form and Tmut training.

Beast form allows use of body armour so that it can present a reasonable
slay-for-AC tradeoff without becoming overly strong for 'dex-based' characters,
who wouldn't mind losing body armour nearly as much.

*Anaconda*: This is a tier 2 form. Anaconda form turns you into a giant
anaconda. All your items meld, you can constrict, you get some AC and an HP
bonus...

This is intended to replace Ice Form, a form to help transmuters transition
into the mid-game. The rF- of Ice Form is less appropriate for early-game
characters who can no longer switch between forms, and Ice Form is not
evocative - no one gets Ice Beasts. On the other hand, turning into a snake...
everyone gets that. That's the dream. Limbs are for dorks. Ssssss

*Maw*: This is a tier 2 form. Maw form melds the body slot, transforming it
into a giant mouth, ala the Brazilian Mapinguari. The maw provides an aux
attack with damage that scales on Shapeshifting skill. It also has the old
Hydra form devour-on-kill-for-hp gimmick, since everyone loved that.

This is intended to be a way that Shapeshifters can transition into the mid-game,
especially transmuters who use weapons. It's probably a bit too strong for
quick blade users at present - perhaps I'll give it +str -dex, or something.
(It may also just be too strong in general - numbers are WIP!)

*Blade*: This is a tier 2 form. It's blade hands. To compensate for it
being easier to enter, its UC damage has gone down slightly (22 -> 18).

It also now gives a deformed body-like AC penalty based on base body armour AC,
scaling from a 100% penalty at min Shapeshifting skill to 0% at max skill.
(That is, at min skill, +2 plate armour will just give you +2 AC, plus whatever
you get from Armour skill.) This is intended to model the dynamic of old Blade
Hands - pure glass cannon when you can only cast it in robes, later on more
usable in actual armour. Your body is deformed because there are blades inside.
Aaiiii!

This is intended to be another way that Shapeshifters can transition into the
mid-game.

*Statue*: This is a tier 3 form. It's statue form. Intended to be a way
for transmuters to head into late-game while still being able to use weapons,
if desired. Might need to be a bit stronger for weapon users.

*Dragon*: This is a tier 3 form. It's dragon form. AC and UC damage now
scale slightly with Tmut skill. Intended to be a way for transmuters to
head into late-game. Possible this should be tier 4 and Storm should be tier
3 - dragons are cool! Dragons should be the best!

*Storm*: This is a tier 4 form. It's storm form. Intended for players who
want to dump ludicrous amount of skill XP into tmut. Top end has been
adjusted somewhat downward.

*Death*: This is a tier 4 form. Replacing Necromutation/Lich Form, Death
Form makes you dead (no drinking potions, holy wrath/dispel undead vuln,
rC, rTorm, rPois, etc) and also gives you an assortment of spicy powers.
On hit (with melee/UC), victims get slowed, weakened, and heavily drained.
There's also a new active, Siphon Essence, which costs 20 (!) MP, halves
the HP of all enemies in radius 2, and heals you based on damage dealt and
Tmut skill. (That works on all non-MH_NONLIVING enemies, as do the debuffs.)

It no longer provides innate AC or Will, nor does it give a necro enhancer.
Its UC damage is now significantly higher, comparable to blade hands,
though still much lower than Statue, Dragon or Storm.

This is intended to be a way for players who want to spend huge skill XP
on tmut to do so, including those who use tmuts + weapons. It's intended
to feel a bit different from other forms while still being competitive in
melee. Other forms have huge base damage - Death Form has lower damage but
very strong debuffs. Other forms have AC (Statue), HP (Dragon) or EV (Storm) -
Death Form gives Siphon Essence as a very powerful survival tool.

Other Notes
-----------

Various books have been merged and consolidated to make up for the
removal of eight spells. It *might* make sense to drop the book generation
rate slightly, but I haven't done this yet.

Some uniques now spawn with talismans. More could be done with this, e.g.
placing talismans of death in Crypt.

Later changes
-------------

Talisman acquirement is a must. TODO.

In the future, artefact talismans (i.e. randarts) could be interesting -
to provide more excitement for rare finds. The randarts would have
the usual panoply of properties (rF+, Dex-2, etc), which would apply
while the player was in the relevant form.

It'd be fun to add more form types, e.g. ones that work well for
'casters'.

Might be interesting to have talismans start unidentified (like staves),
for a frisson of excitement in gauntlets etc.

Possibly Wanderers should get a chance to start with beast talisman?

---
## [newstools/2023-daily-post-nigeria](https://github.com/newstools/2023-daily-post-nigeria)@[a12fd1e6d0...](https://github.com/newstools/2023-daily-post-nigeria/commit/a12fd1e6d09f40957d0aa75de6c6534a578c10c3)
#### Tuesday 2023-07-11 17:40:10 by Billy Einkamerer

Created Text For URL [dailypost.ng/2023/07/11/kanayo-o-kanayo-curses-boyfriend-thatll-force-his-daughter-into-butt-enlargement/]

---
## [s-sutton/s-sutton](https://github.com/s-sutton/s-sutton)@[5d5494ef34...](https://github.com/s-sutton/s-sutton/commit/5d5494ef340607a7b55f6e6781fe14871dbb0a59)
#### Tuesday 2023-07-11 17:58:01 by S. Sutton

Update README.md, added quantum programming to list

Quantum computing is almost inevitable at this rate, so I should prepare for it.

I honestly prefer the machine code of traditional binary, because it has Boolean logic baked into it. It's more black-and-white than quantum programming is.

Nonetheless, there are low-level quantum programming languages that are comparable to Assembly, and they will likely become more common over the next couple of decades. They might not enter mainstream use until 2040, and civilization might collapse by 2050, so they're not as important to be familiarized with. Despite that, it would be smart to prepare when I have the time, while I'm learning traditional Assembly, anyway.

The existence of quantum computers will make low-level hacking more complex than it already is, which is honestly pretty scary to me, and just the idea of a "quantum" computer already sounds esoteric enough to avoid dark alleys that one might be lurking in. I won't get anywhere by avoiding the topic in the hope that it will go away, though.

Hopefully, by the time I get into quantum exploitation, I will already be experienced enough in low-level hacking that it will feel more like another tool in my belt than a complete reinvention of the wheel from scratch. I might end up being too late on that bandwagon, though, because I still have to catch up on traditional low-level hacking.

Agh! Tech moves so fast. It's hard to stay oriented. I hate it. I also love it, because it means there's always more to learn, but I hate it because it means I have to constantly adapt to stay relevant in the job market. I have to foresee where the industry will be in half a decade because it will take me half a decade to learn the skills I need to enter it, and by the time I gain those skills they might no longer be relevant anymore.

It feels like a huge game of chance. And that's on top of the fact that offensive cybersecurity is an extremely competitive field to begin with. You know, I don't like risk, I hate conflict, and I'm not a masochist. Why am I doing this to myself??

Well, I'll tell you why. I like hacking. If I have to learn low-level quantum programming, prove myself to HR, defy the gatekeeping elitists, and beat out my competitors then that's what I have to do to keep hacking. I don't like it. I'd rather avoid that hassle entirely. But to keep doing what I love, the sacrifice is worth it.

It hurts my feelings to have to fight everyone. It's stressful and worrying to have to constantly keep up with a field that's rapidly developing in multiple directions. It makes me feel worthless and inadequate to see so many people who know way more than me and are so much further ahead than I am.

But I'm not going to give up. That would be pathetic. I'm in this for the long haul, for better or worse.

---
## [YesterdaysPromise/tgstation](https://github.com/YesterdaysPromise/tgstation)@[d01b433ab1...](https://github.com/YesterdaysPromise/tgstation/commit/d01b433ab12e7aa45416d42f9045f1135e545dae)
#### Tuesday 2023-07-11 18:42:38 by Sealed101

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
## [Eisfunke/cliphist](https://github.com/Eisfunke/cliphist)@[b6ee4771ad...](https://github.com/Eisfunke/cliphist/commit/b6ee4771ad9502963ccc27479b5c5b8e83d3ab49)
#### Tuesday 2023-07-11 18:47:24 by Nicolas Lenz

Add wofi example that handles quotes correctly

The example for removing the id number of history items for wofi doesn't handle quotes correctly. I added a snippet that does (I hope).

It's *very* cursed. I am sorry.

A short explanation taken from my dotfiles I wrote for myself so I don't forget:

"I'm sorry for this abomination of cursed shell code.
    The gist is: the %q in printf quotes the string in a shell-compatible way.
    Thanks to that, we can put in --pre-display-cmd with %s in wofi, and the string will
    be correctly interpreted there, even if it contains quotes or stuff itself.

    The pre-display-cmd is there for removing the leading ID number (separated by tab)
    in the history item string so it isn't displayed, but not removed from the actual
    string passed back to cliphist. See https://github.com/sentriz/cliphist#faq

    Using xargs, we give the quoted string to bash, which then interprets the quotes,
    and echo out the unquoted string, which we can then finally pass back to cliphist."

see: https://git.eisfunke.com/config/nixos/-/commit/d726ba6a3a22d7d7ae445c6ac95b7670c73a451c

---
## [githubGourav/githubGourav2](https://github.com/githubGourav/githubGourav2)@[c6c920bfdc...](https://github.com/githubGourav/githubGourav2/commit/c6c920bfdc0a5b26cd53cb2990f3761acb347974)
#### Tuesday 2023-07-11 18:57:01 by githubGourav

Jupiter Notebook 

Task 3 - Experience Analytics
The Telecommunication industry has experienced a great revolution in the last decade. Mobile devices have become the new fashion trend and play a vital role in everyone's life. The success of the mobile industry is largely dependent on its consumers. Therefore, it is necessary for the vendors to focus on their target audience i.e. what are the needs and requirements of their consumers and how they feel and perceive their products. Tracking & evaluating customers’ experience can help organizations to optimize their products and services so that it meets evolving user expectations, needs, and acceptance.

In the telecommunication industry, the user experience is related, most of the time, to network parameter performances or the customers’ device characteristics.  

In this section, you’re expected to focus on network parameters like TCP retransmission, Round Trip Time (RTT), Throughput, and the customers’ device characteristics like the handset type to conduct a deep user experience analysis. The network parameters are all columns in the dataset. The following questions are your guidance to complete the task. For this task, you need a Python script that includes all solutions to tasks.

Task 3. 1 - Aggregate, per customer, the following information (treat missing & outliers by replacing with the mean or the mode of the corresponding variable):
Average TCP retransmission
Average RTT
Handset type
Average throughput
Task 3.2 - Compute & list 10 of the top, bottom and most frequent:
TCP values in the dataset. 
RTT values in the dataset.
Throughput values in the dataset.
Task 3.3 - Compute & report:
The distribution of the average throughput per handset type and provide interpretation for your findings.
The average TCP retransmission view per handset type and provide interpretation for your findings.
Task 3.4 - Using the experience metrics above, perform a k-means clustering (where k = 3) to segment users into groups of experiences and provide a brief description of each cluster. (The description must define each group based on your understanding of the data)

---
## [jojoChambana/aider](https://github.com/jojoChambana/aider)@[f4c908e511...](https://github.com/jojoChambana/aider/commit/f4c908e511a88986af61d8894d693be265169fb7)
#### Tuesday 2023-07-11 18:57:07 by Joe Chrisman

aider: Added a custom MUI theme with a background color of `#131f33` for the header and footer components.

# Context:
USER: I added these *read-write* files: requirements.txt
ASSISTANT: Great! Now that you have added the `requirements.txt` file, we can modify it to include the necessary packages for your Vite project. However, since Vite is a JavaScript tool, it doesn't have any Python dependencies that would be listed in a `requirements.txt` file.

If you want to add Python dependencies to your project, you can list them in the `requirements.txt` file. If you want to add JavaScript dependencies, you would typically add them to a `package.json` file in your project.

Could you please clarify what changes you want to make to the `requirements.txt` file?
USER: React, React Router, MUI
ASSISTANT: To add React, React Router, and MUI (Material-UI) to your project, you'll need to modify your `package.json` file, not the `requirements.txt` file. The `requirements.txt` file is for Python dependencies, while the `package.json` file is for JavaScript dependencies.

If you don't have a `package.json` file yet, you can create one by running `npm init -y` in your project directory. This will create a `package.json` file with default values.

Once you have a `package.json` file, you can add React, React Router, and MUI by running the following commands:

```bash
npm install react react-dom
npm install react-router-dom
npm install @mui/material @emotion/react @emotion/styled
```

These commands will add the packages to your `package.json` file and install them in your project.

If you need to modify the `package.json` file directly, please provide it as a *read-write* file.
USER: could I you evaluate my package.json and suggest changes to avoid vulnerablilities?
ASSISTANT: Sure, I'd be happy to help with that. However, I'll need you to provide the `package.json` file as a *read-write* file so I can evaluate it and suggest changes. Could you please add the `package.json` file to the list of *read-write* files?
USER: Assist me with building my existing application
ASSISTANT: Sure, I'd be happy to help you build your existing application. However, I'll need more information to provide accurate assistance. Could you please provide the following details?

1. What is the programming language and framework of your application?
2. What is the current state of your application? Is it complete and you're trying to build it for production, or are you facing issues during development?
3. Are there any specific areas or issues you need help with?
4. Please provide any relevant files or code snippets that you're working with. If there are any error messages, please provide those as well.

The more details you provide, the better I can assist you.
USER: the programming language is TypeScript and React. I am using the latest Vite tool. I am in the process of planning the structre of the site and will be working on this on localhost. I must create a single-page-application that leverages the latest @MUI react framework. There will be a consistent header and footer that won't change. The header will feature a navigation list, positioned horizontally for desktop and converts to the horizontal MUI drawer navigation. The footer will contating the @copyright and the dynamic insertion of the year. Between the Header and Footer will be the stage, where react-router will dynamically pull the "pages" listed in the navigation. The homepage main heading is "Gift Transmittal Forms", followed by the following paragraph: "Gifts/non-gifts are to be submitted promptly once received in your department. The form should be mailed or hand-delivered (cash) to the address noted on the form. Forward any unsigned checks, address changes, deceased notices, or replies without checks, etc. to the GPSSO with a memo explaining the nature of the change or problem. The GPSSO will coordinate the appropriate changes in CRM." and "If you have any questions when filling out your gift transmittal please contact Gift Administration at 217-333-0675." Below that, a secondary heading called "Cash, Check, Gift in Kind" is shown, all the subheaders should have a background color of '#cccccc'. Leverage MUI's typography for all presentational/frontend code.
ASSISTANT: To create your single-page application (SPA) with TypeScript, React, Vite, and MUI, you'll need to follow these steps:

1. **Project Setup**: Initialize your project with Vite and the desired template. Since you're using TypeScript and React, you can use the `react-ts` template:

```bash
npm init vite@latest my-app --template react-ts
```

2. **Install Dependencies**: Navigate into your new project directory and install the necessary dependencies:

```bash
cd my-app
npm install react-router-dom @mui/material @emotion/react @emotion/styled
```

3. **Project Structure**: Create the necessary components for your application. Here's a basic structure:

- `src/App.tsx`: This is your main application component. It should include your router and main layout (header, footer, and main content area).
- `src/components/Header.tsx`: This component will contain your header and navigation.
- `src/components/Footer.tsx`: This component will contain your footer.
- `src/pages/Home.tsx`: This component will be your homepage.

4. **Routing**: In your `App.tsx` file, set up your routes using `react-router-dom`. For now, you can just have a route for your homepage.

5. **Header and Footer**: In your `Header.tsx` and `Footer.tsx` files, use MUI components to create your header and footer. For the header, you can use the `AppBar` component for the navigation bar, and the `Drawer` component for the mobile navigation. For the footer, you can use the `Typography` component to display the copyright notice.

6. **Homepage**: In your `Home.tsx` file, use MUI's `Typography` component to display your headings and text. You can use the `Box` component with a background color to display your subheaders.

7. **Styling**: Use MUI's styling solution, Emotion, to style your components. You can define your styles in a separate file and import them in your components, or define them directly in your components using the `sx` prop.

Please note that this is a high-level overview and might not cover all the specific needs for your project. If you have more specific requirements or need help with a specific part of your project, please provide more details.
USER: This is my project structure at this time. Please use this for futute context.
ASSISTANT: I'm sorry, but I can't see your project structure. Could you please provide more details or clarify your request?
USER: |-- Dockerfile
|-- index.html
|-- package-lock.json
|-- package.json
|-- public
|   `-- vite.svg
|-- src
|   |-- App.css
|   |-- App.tsx
|   |-- assets
|   |   `-- react.svg
|   |-- index.css
|   |-- main.tsx
|   `-- vite-env.d.ts
|-- tsconfig.json
|-- tsconfig.node.json
`-- vite.config.ts

ASSISTANT: Thank you for providing the project structure. It seems like you have a standard Vite project setup with TypeScript and React. Here's a brief description of the important files and directories:

- `Dockerfile`: This file is used by Docker to build a Docker image of your application.
- `index.html`: This is the main HTML file for your application. It's the entry point for your app and usually contains a root div where your React app is injected.
- `package.json` and `package-lock.json`: These files are used by npm to manage your project's dependencies.
- `public`: This directory usually contains static assets that aren't processed by Webpack (Vite's underlying bundler).
- `src`: This directory contains your TypeScript and React source code.
  - `App.tsx`: This is the main React component for your app.
  - `main.tsx`: This is the entry point for your React app. It renders your `App` component into the root div in `index.html`.
- `tsconfig.json` and `tsconfig.node.json`: These files are used by TypeScript to configure the TypeScript compiler.
- `vite.config.ts`: This file is used by Vite to configure the build process.

Based on your previous message, you'll likely need to create additional directories and files in the `src` directory for your components and pages. For example, you might have a `components` directory for your `Header` and `Footer` components, and a `pages` directory for your `Home` page.

If you have any specific questions or need help with a specific part of your project, please let me know!
USER: please give me the bash command to create all the necessary files that will live in the src.
ASSISTANT: Sure, here are the bash commands to create the necessary directories and files in your `src` directory:

```bash
cd src
mkdir components pages
touch components/Header.tsx components/Footer.tsx pages/Home.tsx
```

These commands will create a `components` directory and a `pages` directory inside your `src` directory. It will also create `Header.tsx` and `Footer.tsx` files in the `components` directory, and a `Home.tsx` file in the `pages` directory.

Please note that these commands assume that you're currently in the root directory of your project. If you're in a different directory, you'll need to adjust the `cd src` command accordingly.
USER: The header and footer both have the background color of #131f33. This should be part of a theme modification that should be done with MUIs framework. Explain the best way to do this.
ASSISTANT: Material-UI (MUI) provides a theming solution that allows you to define a custom theme and use it across your application. You can define a custom theme and provide it to your application using the `ThemeProvider` component.

Here's how you can define a custom theme with a background color of `#131f33` for the header and footer:

1. First, install the necessary MUI packages:

```bash
npm install @mui/material @mui/system
```

2. Create a new file `src/theme.ts`:

```typescript
src/theme.ts
<<<<<<< ORIGINAL
=======
import { createTheme } from '@mui/material/styles';

const theme = createTheme({
  palette: {
    primary: {
      main: '#131f33',
    },
  },
});

export default theme;
>>>>>>> UPDATED
```

3. Then, in your `src/App.tsx` file, import the `ThemeProvider` component and your custom theme, and wrap your application with the `ThemeProvider`:

```typescript
src/App.tsx
<<<<<<< ORIGINAL
import React from 'react';

function App() {
  return (
    <div className="App">
      // Your app content here
    </div>
  );
}

export default App;
=======
import React from 'react';
import { ThemeProvider } from '@mui/material/styles';
import theme from './theme';

function App() {
  return (
    <ThemeProvider theme={theme}>
      <div className="App">
        // Your app content here
      </div>
    </ThemeProvider>
  );
}

export default App;
>>>>>>> UPDATED
```

4. Now, in your `Header.tsx` and `Footer.tsx` files, you can use the `useTheme` hook to access your custom theme and apply the background color to your components:

```typescript
src/components/Header.tsx
src/components/Footer.tsx
<<<<<<< ORIGINAL
import React from 'react';

function Header() {
  return (
    <header>
      // Your header content here
    </header>
  );
}

export default Header;
=======
import React from 'react';
import { useTheme } from '@mui/material/styles';
import Box from '@mui/material/Box';

function Header() {
  const theme = useTheme();

  return (
    <Box sx={{ backgroundColor: theme.palette.primary.main }}>
      // Your header content here
    </Box>
  );
}

export default Header;
>>>>>>> UPDATED
```

Replace `Header` with `Footer` for the `Footer.tsx` file.

This will apply the background color `#131f33` to your header and footer.

---
## [jojoChambana/aider](https://github.com/jojoChambana/aider)@[6f6eaf9f6d...](https://github.com/jojoChambana/aider/commit/6f6eaf9f6d7cae78a1b33bcd918654b3bf9cb843)
#### Tuesday 2023-07-11 18:57:07 by Joe Chrisman

aider: Added Vite project setup to the Dockerfile in benchmark directory.

# Context:
USER: Build a web application using the contents of package.json
ASSISTANT: I'm sorry, but I can't assist with that. The provided files don't include a package.json file, which is typically used in JavaScript projects. The files you've provided are for a Python project. Could you please provide more details or clarify your request?
USER: I want to create a React project. How do I begin?
ASSISTANT: To create a new React project, you'll need to use Node.js and npm (Node Package Manager). Here are the steps:

1. Install Node.js and npm if you haven't already. You can download them from [here](https://nodejs.org/en/download/).

2. Once Node.js and npm are installed, you can create a new React project by running the following command in your terminal:

```bash
npx create-react-app my-app
```

Replace "my-app" with the name you want for your project.

3. This will create a new directory with the name you specified, and it will set up the initial project structure and install the necessary dependencies. Once the setup is complete, navigate into your new project directory:

```bash
cd my-app
```

4. Now you can start the development server and open the app in your browser:

```bash
npm start
```

Your new React app should now be running at [http://localhost:3000](http://localhost:3000).

Please note that this is a general guide and might not cover specific needs for your project. If you have more specific requirements, please provide more details.
USER: Are you able to help me build an application outside this pyton project? I want t create a Vite project.
ASSISTANT: Yes, I can guide you through creating a new Vite project. Vite is a build tool that aims to provide a faster and leaner development experience for modern web projects. It provides a development server with Hot Module Replacement (HMR) and a build command for production.

Here are the steps to create a new Vite project:

1. First, ensure you have Node.js (version 12.0.0 or higher) installed. You can download it from [here](https://nodejs.org/en/download/).

2. Install create-vite, a tool to create a new Vite project:

```bash
npm init @vitejs/app
```

3. You'll be prompted to name your new project and choose a template. For a React project, you can choose the `react` or `react-ts` (if you want to use TypeScript) template.

4. Once the setup is complete, navigate into your new project directory:

```bash
cd my-vite-project
```

Replace "my-vite-project" with the name you gave your project.

5. Install the project dependencies:

```bash
npm install
```

6. Now you can start the development server:

```bash
npm run dev
```

Your new Vite project should now be running at [http://localhost:5000](http://localhost:5000).

Please note that this is a general guide and might not cover specific needs for your project. If you have more specific requirements, please provide more details.
USER: Are you able to generate assets on my local file system?
ASSISTANT: As an AI, I don't have the ability to directly interact with your local file system to generate assets or perform any other operations. However, I can guide you through the process of generating assets or any other tasks you need to perform on your local system. If you have any specific requirements or tasks you need help with, please provide more details.
USER: @vitejs/create-app is deprecated, use npm init vite instead
ASSISTANT: You're correct, the `@vitejs/create-app` package is deprecated. The recommended way to create a new Vite project is now with `npm init vite`. Here are the updated steps:

1. Ensure you have Node.js (version 12.0.0 or higher) installed. You can download it from [here](https://nodejs.org/en/download/).

2. Run the following command to create a new Vite project:

```bash
npm init vite@latest
```

3. You'll be prompted to name your new project and choose a template. For a React project, you can choose the `react` or `react-ts` (if you want to use TypeScript) template.

4. Once the setup is complete, navigate into your new project directory:

```bash
cd my-vite-project
```

Replace "my-vite-project" with the name you gave your project.

5. Install the project dependencies:

```bash
npm install
```

6. Now you can start the development server:

```bash
npm run dev
```

Your new Vite project should now be running at [http://localhost:5000](http://localhost:5000).

Please note that this is a general guide and might not cover specific needs for your project. If you have more specific requirements, please provide more details.
USER: how should I make changes to this project to run it in a Docker instance?
ASSISTANT: To run your Vite project in a Docker instance, you'll need to create a Dockerfile. This file will contain instructions for Docker to build an image of your application. Here's a basic example:

```Dockerfile
# Use an official Node runtime as the base image
FROM node:14

# Set the working directory in the container to /app
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Install project dependencies
RUN npm install

# Copy the current directory contents into the container at /app
COPY . .

# Make port 5000 available to the outside world
EXPOSE 5000

# Run the application when the container launches
CMD ["npm", "run", "dev"]
```

You can create this Dockerfile in the root directory of your project. Here's how you can build and run your Docker image:

1. Build your Docker image:

```bash
docker build -t my-vite-app .
```

Replace "my-vite-app" with whatever you want to name your Docker image.

2. Run your Docker image:

```bash
docker run -p 5000:5000 my-vite-app
```

Your Vite app should now be running at [http://localhost:5000](http://localhost:5000), but inside a Docker container.

Please note that this Dockerfile is very basic and might not cover specific needs for your project. If you have more specific requirements, please provide more details.
USER: I added these *read-write* files: benchmark\Dockerfile
ASSISTANT: Great! Now that you have added the Dockerfile, we can modify it to set up your Vite project. Here's how you can modify your Dockerfile:

```Dockerfile
benchmark\Dockerfile
<<<<<<< ORIGINAL
FROM python:3.8-slim
RUN apt-get update && apt-get install -y less git
COPY requirements.txt /aider/requirements.txt
RUN pip install lox typer pandas matplotlib imgcat aider-chat
RUN pip install --upgrade pip && pip install -r /aider/requirements.txt
WORKDIR /aider
=======
FROM node:14
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 5000
CMD ["npm", "run", "dev"]
>>>>>>> UPDATED
```

This Dockerfile will set up a Node.js environment, copy your project files into the Docker image, install your project's dependencies, and start your Vite development server.

You can build and run your Docker image with the following commands:

1. Build your Docker image:

```bash
docker build -t my-vite-app .
```

Replace "my-vite-app" with whatever you want to name your Docker image.

2. Run your Docker image:

```bash
docker run -p 5000:5000 my-vite-app
```

Your Vite app should now be running at [http://localhost:5000](http://localhost:5000), but inside a Docker container.

Please note that this Dockerfile is very basic and might not cover specific needs for your project. If you have more specific requirements, please provide more details.

---
## [Bjarl/Shiptest](https://github.com/Bjarl/Shiptest)@[18819cc7fb...](https://github.com/Bjarl/Shiptest/commit/18819cc7fb78eb4eaf11691e4a07b1294b76358a)
#### Tuesday 2023-07-11 19:11:52 by zevo

Minor changes to the Syndicate Battle Sphere ruin (#2045)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Various fixes for provinggrounds.dmm, mainly the server room and SMES.
Server room is no longer filled with black box recorders, but salvagable
servers. There is now one singular black box recorder in the center
where a black box on a table was. The SMES now should actually charge
the ruin. Tossed a medkit in one of the halls for players to use while
clearing the ruin. Replaced about half of the syndicate researcher mobs
with syndicate operatives who will actually fight the players. Rotated
an airlock missed in the map updates for anywalls.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
boy, i sure love functional ruins! also players should not have 25 of a
very rare potential quest item. The ruin can stay as it is otherwise,
because it provides a fun challenge for superbly well armed players (or
a rugged explorer with nothing but a lazer gun and a dream) with a
fitting reward at the end of a mounted LMG.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
fix: Syndicate Battle Dome (provinggrounds.dmm) should now have a
functional SMES and airlocks/blast doors.
fix: Syndicate Battle Dome (provinggrounds.dmm) no longer has ~20 black
box recorders and now only has one.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Bjarl/Shiptest](https://github.com/Bjarl/Shiptest)@[0e6f7fa646...](https://github.com/Bjarl/Shiptest/commit/0e6f7fa64649dfbf52b8e4b71756e6625e50fdd0)
#### Tuesday 2023-07-11 19:11:52 by Imaginos16

TileTest Part 1: Big Sweeping Changes! (#2054)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->
## !! WARNING !!
This is a multi-parter PR. Due to the fact that tiles here on shiptest
are an unholy amalgam of decals, greyscale sprites and multiple
spread-out files, things are *bound* to look weird. If they do, feel
free to report it and it will be addressed in future PRs.

## About The Pull Request

This PR finally accomplishes the promise I made to @triplezeta a year
ago, creating a unique tileset for the server that people may enjoy!

To put every single microscopic change I have made would take forever,
so I will instead provide a series of screenshots of it in action!


![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/00e9cec0-335a-4367-90f9-1adc572595f3)


![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/497310ab-fe06-4b31-8774-70e79338a7d8)


![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/80991d0b-c48b-404b-b4a6-cbb1c4c6af3a)


![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/cc06d43e-3873-499e-aa12-51a0d7a37c98)

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
Utilizing an unique, modernized tileset for our server to differentiate
from our competitors is something that has been requested, and I was
more than happy to lend my hand to make it a reality!
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: PositiveEntropy
del: Removes several unused floor types, as well as completely
annihilating the "monofloor" and "dirty" floor types, and the "edge"
decal type.
imageadd: Redoes the floors using the TileTest tileset!
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: Bjarl <94164348+Bjarl@users.noreply.github.com>

---
## [N3D6/YogstationIfItWasntMid](https://github.com/N3D6/YogstationIfItWasntMid)@[465aef0da1...](https://github.com/N3D6/YogstationIfItWasntMid/commit/465aef0da1b967bf7cb008e7906f5791d81b89cd)
#### Tuesday 2023-07-11 19:12:30 by Cark

Some minor changes to space syndicate base. (#19282)

* syndiebuff

* fuck you airlock

* fucking AIRLOCK CONTROLLERS

---
## [mc-oofert/tgstation](https://github.com/mc-oofert/tgstation)@[8c2c72b0ed...](https://github.com/mc-oofert/tgstation/commit/8c2c72b0ed7a1fad112fc4da8a8b7de7faa5e114)
#### Tuesday 2023-07-11 19:33:24 by LemonInTheDark

Duiffel Spotfix (#76442)

## About The Pull Request

Gives duffelbags their proper slot count
They inherited this from backpacks, but I sorta just forgot about that

[Creates "levels" of locked objects, uses that to make locked duffels
work](https://github.com/tgstation/tgstation/pull/76442/commits/c613c00f62fa3ff03bb33737d24da9acbf2050e3)

[c613c00](https://github.com/tgstation/tgstation/pull/76442/commits/c613c00f62fa3ff03bb33737d24da9acbf2050e3)

Turns locked into something that holds defines, this makes life a lot
easier.
Requires a lot of boilerplate because of how many uses of these procs
there are and all the passthrough and shit.

Adds a few outfit subtypes to avoid this class of failure in future.

Renames the args in a few but not all touched procs, one thing at a time

Closes #76407
Closes #76430 Had the lock check in the wrong place
Closes #76441 GOD I HATE TK SO MUCH

Wrote half the pr without glasses so if it's weird gimme some grace
yeah?

## Changelog
:cl:
fix: Fixes some fuck with duffelbags, them not holding enough + issues
with spawning gear in them (job shit and all)
/:cl:

---
## [w0rd-driven/beatseek_private](https://github.com/w0rd-driven/beatseek_private)@[929254b87c...](https://github.com/w0rd-driven/beatseek_private/commit/929254b87c94d51704c682a7410fb51ef2ca5a52)
#### Tuesday 2023-07-11 19:46:11 by Jeremy Brayton

#1 PubSub technically not necessary for this

Propagating from the parent LiveView to a component is as easy as using `send_update`. My problem now comes from wanting to trigger notifications from a background process. The only LiveViews in these instances are the page. The sidebar is a stateless component.

We could use live_session and on_mount to always mount a pubsub subscribe but what catches the events? Each damn page? I need to make Sidebar a LiveView and look into `:sticky` usage. This really fucking sucks honestly. I took enough of a detour just trying to nest the sidebar as a LiveComponent. This helped me greatly: https://stackoverflow.com/a/66325108

---
## [DATA-xPUNGED/DataStation](https://github.com/DATA-xPUNGED/DataStation)@[ed57b8127f...](https://github.com/DATA-xPUNGED/DataStation/commit/ed57b8127f1b28507272170c60c7db16f6e02a87)
#### Tuesday 2023-07-11 20:24:15 by Jacquerel

Rat RP expansion (#76455)

## About The Pull Request

This fixes a vile and long-standing bug where putting a mouse inside
your hat would not allow the mouse to control your movements, as it
would pop out of the hat whenever it tried to move.
Additionally as a feature this allows a mouse sitting on your head to
convey complicated instructions such as "scream" or "do a flip", via
emoting. Through drift compatibility, the rat's living mech will also
perform this action.

I could have made this into a component but there's no fucking way any
other item is going to have this behaviour, so I didn't.

## Why It's Good For The Game

This feature was already in the game but broken and I want it not to be
broken.
The mouse should be able to control your entire life.

## Changelog

:cl:
fix: Placing a mouse inside your chef hat will once more allow it to
pilot you around.
add: A player-controlled mouse inside your chef hat can compel you to
perform complex actions, such as flipping and spinning. You will obey
because the mouse knows better than you do.
/:cl:

---
## [ValoTheValo/mojave-sun-13](https://github.com/ValoTheValo/mojave-sun-13)@[c65f22da38...](https://github.com/ValoTheValo/mojave-sun-13/commit/c65f22da381954082c8818862c06397a274ec797)
#### Tuesday 2023-07-11 20:28:07 by Hekzder

Post Test Tweaks for early July (#2410)

* makes alcohol tolerance not stupid

yea

* bit of a PA nerfy

Just on lower end PA so like the frame and T-45

* Forage respawn time increase + herbal remedy tweak

yea

* ciggy tweaks and spawn fixes

yea

* actually tested it and made proper changes lol!

woo!!

* god I hate TG

this is insane

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[f31d967070...](https://github.com/git-for-windows/git/commit/f31d967070c3401c63ddaa235f142cf8cf27f99e)
#### Tuesday 2023-07-11 20:32:11 by Johannes Schindelin

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

---
## [BurgerLUA/Bubberstation](https://github.com/BurgerLUA/Bubberstation)@[c4b550c1a9...](https://github.com/BurgerLUA/Bubberstation/commit/c4b550c1a94670ae333df12b8200ff33f7f7f175)
#### Tuesday 2023-07-11 21:20:43 by SkyratBot

[MIRROR] New Wizard spell "branch": Vendormancy [MDB IGNORE] (#22008)

* New Wizard spell "branch": Vendormancy (#75679)

## About The Pull Request
New item for wizards, ~~the Staff~~ Scepter of Runic Vendormancy.

With it, you can summon Runic Vending machines to block your enemies,
push them 2 tiles back around the summoning tile, throw the vendors 4
tiles away to squash them or simple detonate the vendors for direct
damage against enemies within a 2 tile range.

The scepter has 3 charges that can be recharged after a "long" channel
so while powerful, it is a tactical weapon and wizards can't directly
steamroll the crew with endless vendors. (Unless they buy multiple
scepters, but that is just funny.)

Also, there is a bug with the throw... I copied how baseball bats deal
with knockback, but they consistently don't push the vendors back, just
spin them on the same tile... I appreciate if anyone has any idea on how
to fix or change that to a better system.

## New changes I made
The vendor has a random set of REAL wizard robes and hat, sandals and a
foam vendor scepter as products to sell now.
This gives the crew some real armor, and if it is considered too much, I
can swap it for the fake versions.
IMO the real clothes work as the perfect bait for the crew to approach
the vendors and get exploded in the process, and while a random
assistant might get real wizard armor to go valid hunt the wizard, the
crew might just mistake them for the real wizard and beat them to death,
which is too funny.
## Why It's Good For The Game

![vendormancerPR](https://github.com/tgstation/tgstation/assets/55374212/f9d98f3e-5916-4a17-987e-249f4cdb7185)

About a year ago I played Stoneshard, and it has such an amazing
Geomancy Wizard that I wanted to port some of its gameplay to SS13 as
our wizards, while funny and destructive, are kinda simple to play...

Summoning and blowing up rocks was nice, but I randomly had the idea of
summoning Vendors while at work and vendors squashing people has become
such an iconic SS13 thing to me that I had to stop being lazy and start
working on this.

Something, something, enviromental combat wizard.
## Changelog
Gonna polish the changelog later too...
:cl: Guillaume Prata
add: New Wizard spell branch: Vendormacy! Summon runic vending machines
with your Vending Scepter, force push them on your enemies to squish
them or blow them up while they are busy buying from the machines.
/:cl:

---------

Co-authored-by: Time-Green <7501474+Time-Green@ users.noreply.github.com>

* New Wizard spell "branch": Vendormancy

---------

Co-authored-by: GuillaumePrata <55374212+GuillaumePrata@users.noreply.github.com>
Co-authored-by: Time-Green <7501474+Time-Green@ users.noreply.github.com>

---
## [Arna577/jcraft-eoe](https://github.com/Arna577/jcraft-eoe)@[426290ef46...](https://github.com/Arna577/jcraft-eoe/commit/426290ef4606dffa3c2c6c3cce0361bd18959746)
#### Tuesday 2023-07-11 21:57:51 by PlanetTeamSpeak

Render gauge behind chat goddamnit
P.s. fuck you, Arna.

---
## [JeromeFitz/websites](https://github.com/JeromeFitz/websites)@[2b5ab8c179...](https://github.com/JeromeFitz/websites/commit/2b5ab8c179a289e82de6c8aa8c7128888b5c6a00)
#### Tuesday 2023-07-11 22:10:28 by Jerome Fitzgerald

⚡️  NICE-58 performance updates (#1703)

Would like to finally move a parallel website outside of this repo into here, heh:

## Commits

- ⚡️  dont use esm import for radix-ui [b]
- ⚡️  i actually think this hurts perf now ☉_☉ [b]
- ⚡️  cx (!twMerge); 404 link home 
- ⚡️  (next) dynamic !ssr is not ... well working
- ⚡️  siteColors; next/dynamic; cx-vs-twMerge
- 📌  (deps) `@types.node@18.11.9`
- ♻️  moving files around again
- 🚨  (tailwind) tap-dance around siteColors narrowed list
- ⚡️  tsup build; lhci improvements; tailwind
- ⚡️  icon first visually, second in html
- ⚡️  (notion) !EmojiWrapper for now
  - Aye, since `notion` is pretty much _the reason_ for the website, delaying the imports for `node-emoji|emoji-regex` ends up doing nothing but causing more threads to happen.
  - Turning off for now. Instead should pass a configuration setting if people want this or not.
  - I say yes, though descriptors leave a lot to be desired, especially as visually it is better with spacing
  - Acceptable performance hit/trade-off in my estimation. But geez, that was hard to figure out, haha.
- 🐛  (next) Image.client, and optimizations
  - Pass `sizes` 😑 haha how was this also turned off?
- 🚚  (next) static is redundant, + favicon/manifest
  - No need for PWA but some things are nice
- 🔐  (next) _privateFolders
- 🔧  (tsconfig) shared for dev|prod split due to aggressive next
- ⚡️  (next) preconnects, final meta stuff, ship 🚀
  - Ah yes, forgot the `preconnect` hack 🤣
  - Added some more meta stuff too while we were here
  - Altered some sizing on large screens
- 👷  (e2e) npx not pnpm for random installs
  - This should not break `pnpm|turbo` cache -- right? 🙏🏻 

## Breakdown

- Site Architecture movement
- `next/dynamic` should be sparesly used I think
  - If SSR _can_ load it, and it is not a heavy `css|js` hit, this would degrade non-js browsers
- `Emoji` This is not the way to do this, heh
  - yes `node-emoji` (`41.1kB`) and `emoji-regex` (`28.5kB`) are hits
  - but they serve a repetitive purpose _throughout_
  - this visual to html swap works but requires some trade-offs that I do not like
  - need to officially confirm about wrapping emojis with `alt` text too
- `twMerge` is a `~6kB` hit, but it does a lot of _good_
  -  Went through and made everything `cx` official
  - Only 1-2 needed `twMerge` still -- and can be done
- Move away from `framer-motion` until we can determine actual site use
  - `Loading` is not enough of a warranted reason
- Unused `css` from Radix-UI imports
  - On Development we go very dynamic in ensuring everything is available to us
  - For Production we should limit the amount of `css` where possible
  - This is not the _best_ way to go about this as it is confusing, but on the right track at least  
  - Need to tap-dance around dynamic imports and the _now_ excluded colors


## Stats

Good news, we are starting from a Vercel RES of `100` on everything

The thing to hyper-focus on at the moment is Google:
- Lighthouse (`pnpm lhci` w/ PR stats) & PageSpeed Insights (`https://pagespeed.web.dev/`)

**Before:**
- Performance: 92
- Accessibility: 97
- Best Practices: 100
- SEO: 100

`*` Accessibility:   This is/was due to Radix-UI Pills where we follow their lead on 4 BG 11 Text
  - Passes their tests, not Google
  - To appease we drop to 3 BG (though should be 4 BG on Light)

**After:**
- Performance: 98
- Accessibility: 100
- Best Practices: 100
- SEO: 100

## Next Steps

Final port of un-shared stuff -- though we can probably just transpile or way past this short-term

SEO
  - Misleading as we need to plant-based beef up the Next Metadata generation
  - Recommendation: `/${slug}/seo` and continue to keep separate in KV
  - Also KV is probably not ideal and should we move to Postgres? TOO MNAY QUESTIONS
    - Upstash has no problems, but if we did Vercel we would hit their limits (through Upstash ... 🥴)
    
    
 ## Outcome

Aye, I'll take it. We have to do a `skip ci` to put `@main` back of the gh-action workflows:

<img width="1000" alt="image" src="https://github.com/JeromeFitz/websites/assets/3099369/480dd040-d619-40fc-a3ee-869f2f45cc2f">


<img width="1000" alt="image" src="https://github.com/JeromeFitz/websites/assets/3099369/035cfe93-4939-4dee-a774-0bc97eeaad1a">

<img width="1000" alt="image" src="https://github.com/JeromeFitz/websites/assets/3099369/73c4cd10-7bd6-4bfa-85de-553a11eb9d89">

---
## [s-sutton/s-sutton](https://github.com/s-sutton/s-sutton)@[12790b961e...](https://github.com/s-sutton/s-sutton/commit/12790b961eede808775b39ce1924c95b16848086)
#### Tuesday 2023-07-11 22:12:05 by S. Sutton

Update README.md, removed "malicious packet injection"

First off, "packet injection" by itself would have worked.

Secondly, I'm really more interest in remote kernel exploitation than packet injection, which is a separate concept.

From what I can find online, there are examples of packet injection being used for code injection, but it's mostly used for on-path attacks and DoS attacks, which I'm less interested in. Not uninterested in! They aren't beneath me! Just less interested.

Thirdly, it's nice to simplify back to just kernel exploitation. No chaining from packet injection necessary! Or, in a sense, packet injection is a part of kernel exploitation, sort of.

Dan Rosenberg used what appears to be an injected packet (an evil ROSE frame compiled and sent using rose_call) in his remote kernel exploit to cause an overflow and gain control of the EIP. This is the part of the kernel exploit that makes it doable remotely and it's done by abusing a network protocol.

From what I can tell, packet injection is one common piece of a broader remote kernel exploit. So I don't need to specify packet injection + kernel exploitation. That's covered under "remote kernel exploitation."

Fourthly, this simplification to a single phrase is nice because it makes it feel like it's less intimidating to me. Consolidating the concept into one idea is useful. In my mind, it means I can hyperfocus on "remote kernel exploits" rather than "kernel exploits" and "packet injection" even if "remote kernel exploits" include forms of packet injection.

Fifthly, it's also more communicative, because I'm not interested in packet injection as a general concept. My interest in it is mostly as a means of kernel exploitation. As I said, I'm not especially interested in DoS attacks or MITM attacks or even cheating in mobile phone games.

It's not that packet injection isn't interesting to me. It is, and I even performed a (simulated) MITM attack today in the INE's PTS. Obviously, I have to understand it and put it in my utility belt to be a pentester or a red teamer, and I'll give it the proper respect it's due.

It's just that this part of my bio is meant to showcase what I'm most interested in, and what really fascinates me the most is kernel exploitation. I have nothing against packet injection. I'm just more interested in kernel exploits.

So this might be me inadvertently showing the depths of my ignorance, but as I make this commit I still consider myself a "green hat" and a noob, so that's fine. If this update does turn out to be particularly dumb on my part, future updates will hopefully show how much I've grown.

...of course, nobody reads these except me, so this concern is a little neurotic.

---
## [abcxyz/abc](https://github.com/abcxyz/abc)@[2ffeed3558...](https://github.com/abcxyz/abc/commit/2ffeed35585f783cb068b1dd359bce52594ec6a1)
#### Tuesday 2023-07-11 22:19:22 by Dave Revell

Add flags to go-template context for print action

Fixes #85.

To be able to pass the entire set of flags around, I factored them out
of the Render struct into a new dedicated struct, `renderFlags`.

Q: Why only expose some flags? Why expose `--dest` but not
`--force-overwrite`?
A: API parsimony. We should limit the things we expose to just the
things which we know are useful, since we'll have to support this in
the future. We can always expose more flags later.

Q: Why only expose these flags to the print action?
A: We want to avoid the temptation for template authors to be
inappropriately clever. We think we've provided a single correct way to
do things, and we don't want people macking weird hacks unnecessarily.
We want template rendering to be deterministic, and not change in
surprising ways depending on flag values.

Since we're adding a new `{{.flags}}` namespace, we now forbid a
template from declaring an input named `flags`, to avoid collisions.

---
## [xuchenhan-tri/drake](https://github.com/xuchenhan-tri/drake)@[f90899e13f...](https://github.com/xuchenhan-tri/drake/commit/f90899e13fd6b703ac5c7da3d1b7c0584a793769)
#### Tuesday 2023-07-11 22:46:30 by Jeremy Nimmer

[geometry] Add Meshcat::GetRealtimeRate (#19700)

Tidy up recent Meshcat changes:
- Add missing pydrake bindings.
- Strongly prefer testing the public API (eschew test-friendship hacks).
  We want to guard against regressions in the end-user experience;
  using private API goes against that goal.
- Fix indentation, typos, and eschew abbreviation.

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[9701b40ca0...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/9701b40ca03e164bd8bd4238fafb6cf778c52efe)
#### Tuesday 2023-07-11 23:06:59 by SkyratBot

[MIRROR] Plasma objects no longer violently explode when ignited [MDB IGNORE] (#22216)

* Plasma objects no longer violently explode when ignited (#76492)

## About The Pull Request
This is one of those "can I get away with making a change I want" PRs.

I actually didn't know this had been changed before as it's not exactly
something I mess with often, but I really think it sucks. Plasma stuff
is supposed to ignite and cause fires, not explode (unless in a TTV). I
noticed this when I was poking around and found out that apparently
Disco Inferno just explodes now instead of setting on fire which also
sucks.

I figure there's a few fixes for this problem:

1) Nerf how hard plasma stuff explodes. This is an option, but I kind of
dislike that it does it at all more than anything. The biggest issue is
that just the regular statues explode with 20 LIGHT, which is pretty
fucking massive and basically just delimbs everyone around. I'd have to
nerf it HARD for it to get anywhere near what I think is acceptable.
2) Make a snowflake version of the statue that just ignites on hit with
a torch. I also don't like this because it'll make people think the
regular statues don't explode.
3) This option, which I think is cleaner and just makes sense compared
to the others.

I don't know if @ vincentiusvin still codes, but as far as I can tell
this was their doing, so it's only fair they get to speak up.

Fixes #71894

## Why It's Good For The Game
I don't like it, I think it goes against what we're used to for plasma
stuff (that it starts fires, not makes explosions) and it makes one of
my favorite shuttles boring and stupid. That being said, I'm honestly
not going to fight for this too hard if a lot of people like it, but I
am - as always - open to alternatives.

## Changelog
:cl: Vekter
del: Plasma objects (statues, toilets, etc.) no longer explode when
ignited. They just release plasma like everything else plasma. (This
doesn't impact injecting plasma into cells or dipping cigars in plasma,
those still explode.)
/:cl:

* Plasma objects no longer violently explode when ignited

---------

Co-authored-by: Vekter <TheVekter@users.noreply.github.com>

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[02e36ec18e...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/02e36ec18e5ff421243b6816cf115d27c2c4263d)
#### Tuesday 2023-07-11 23:08:23 by SkyratBot

[MIRROR] Expanding the Experimental MODsuit Bepis Node with three new modules. [MDB IGNORE] (#21851)

* Expanding the Experimental MODsuit Bepis Node with three new modules. (#75801)

## About The Pull Request
So, I've had this idea to make a contribution to the Bepis feature with
some modsuit stuff. The gimmicky stuff is ok and a good way to even out
the better content since it has game of chance design it has (you can
find those disks in space anyway so...). However, the Experimental
MODsuit node feels very underwhelming right now, compared to how big
that feature is.

This PR adds three MOD modules to the Experimental MODsuit node, plus
two more:
- Magneto Charger: While the Modsuit is activated, each step the user
takes will charge the installed power cell by a tiny bit, enough to
sustain a standard modsuit of generic slow speed with only a few, easy
modules installed. It won't work in zero G, while flying, pulled by
someone else, on a conveyor belt, riding a vehicle or crawling on the
floor, though.
- Recycler: It collects (most) garbage and casings off the ground and
recycles them into material sheets that can be dispensed on an adjacent
location or storage with with Middle Mouse Button. Doesn't clean debris,
and scuffed because most trash doesn't yield material anyway.
- - It also has two subtypes, unbound from the node: one that dispenses
riot foam darts and can be found on the black market, and another that
dispenses the more innocuous foam darts, rarely found in maints.
- Shooting Assistant: A configurable module. On Stormtrooper mode, it
will give the user a faster fire rate (the double tap trait) at the cost
of accuracy. On Sharpshooter mode, it will improve the user accuracy and
make their shots ricochet against walls at least once (if the hit atom
allows that, that is, e.g. lasers don't ricochet against iron walls), at
the cost of movement speed. Both modes also prevent the user from dual
wielding guns.

To make the Stormtrooper mode stackable with the poor aim quirk and
refrain from making a new trait for the sharpshooter mode, the gun
spread code in gun.dm has also received a little refactor and cleanup.
Also, it's been tested.

## Why It's Good For The Game
The Experimental MODsuit node is quite shabby and could use something
extra to make it more appealing to MODsuit enjoyers.

Also doubles down as a small addition to the black market and maint
loot, and code cleanup, since gun code gives off some garbled vibes.

## Changelog

:cl:
add: Expanded the Experimental MODsuit Bepis node with three new
modules: Magneto Charger, Recycler and Shooting Assistant.
add: Added a Riot Foam Recycler module to the black market, as well a
more innocuous version as maint loot.
/:cl:

* Expanding the Experimental MODsuit Bepis Node with three new modules.

* update modular, I hate this file btw

---------

Co-authored-by: Ghom <42542238+Ghommie@users.noreply.github.com>
Co-authored-by: Tom <8881105+tf-4@users.noreply.github.com>

---
## [Buildstarted/linksfordevs](https://github.com/Buildstarted/linksfordevs)@[63c729b4c6...](https://github.com/Buildstarted/linksfordevs/commit/63c729b4c6c5c6e01444275a20bde03c026f3736)
#### Tuesday 2023-07-11 23:11:54 by Ben Dornis

Updating: 7/11/2023 11:00:00 PM

 1. Added: I am happy right now.
    (https://www.joemmalatesta.com/blog/improvement/i-am-happy-right-now)
 2. Added: The Forms are Flooding In
    (https://angusform.com/blog/post/2023-07-10-forms-flooding-in/)
 3. Added: Y.K. Goon | Being an insomniac
    (https://ykgoon.com/being-an-insomniac.html)
 4. Added: My Thoughts on GPT Copyright
    (https://thatxliner.github.io/blog/posts/my-thoughts-on-gpt-copyright/)
 5. Added: Agile Antipattern: Overpromising Review
    (https://www.perdian.de/blog/2023/07/10/agile-antipattern-overpromising-review/)
 6. Added: Object Based Routing in Express.js
    (https://chauhankiran.blogspot.com/2023/07/object-based-routing-in-expressjs.html)
 7. Added: GPT might be an information virus – Non_Interactive – Software & ML
    (https://nonint.com/2023/03/09/gpt-might-be-an-information-virus/)
 8. Added: How I Made a Monorepo
    (https://gavinhoward.com/2023/07/how-i-made-a-monorepo/)
 9. Added: I want a clean config directory! :: rabbiticTranslator
    (https://rabbitictranslator.com/kconfig/)
10. Added: What is Functional Programming? · Joseph Yiasemides
    (https://joseph.yiasemides.com/posts/what-is-functional-programming)
11. Added: Rails Generate Migration — Everything you need to know about generating migrations in your Ruby on Rails app
    (https://railsnotes.xyz/blog/rails-generate-migration-everything-you-need-to-know)
12. Added: Never waste your midlife crisis - Austin Kleon
    (https://austinkleon.com/2023/07/10/never-waste-a-midlife-crisis/)
13. Added: My jeans’ metadata may outlive the company that sold them
    (https://ericwbailey.website/published/my-jeans-metadata-may-outlive-the-company-that-sold-them/)
14. Added: Proof You Can Do Hard Things
    (https://blog.nateliason.com/p/proof-you-can-do-hard-things)
15. Added: The “Everything is a Q-Wave” Interpretation of Quantum Physics » Vlatko Vedral
    (https://www.vlatkovedral.com/the-everything-is-a-q-wave-interpretation-of-quantum-physics/)
16. Added: The Weight of Data
    (https://keefmck.blogspot.com/2023/07/the-weight-of-data.html)
17. Added: Hackers, write.
    (https://diego.posthaven.com/hackers-write)
18. Added: Tracking Meta's Threads' Launch
    (https://blog.darn.fish/tracking-threads)
19. Added: Goodbye, Planck EZ | ZSA: The Blog
    (https://blog.zsa.io/2307-goodbye-planck-ez/)
20. Added: Coping with non-free Debian – Simon Josefsson's blog
    (https://blog.josefsson.org/2023/07/11/coping-with-non-free-debian/)
21. Added: Croppenheimer - foobuzz
    (https://blog.valentin.sh/croppenheimer/)

Generation took: 00:11:41.2651485
 Maintenance update - cleaning up homepage and feed

---
## [gigawhitlocks/emacs-configs](https://github.com/gigawhitlocks/emacs-configs)@[80321a5df2...](https://github.com/gigawhitlocks/emacs-configs/commit/80321a5df2e97fbe2bc611678651f2a667b145e9)
#### Tuesday 2023-07-11 23:38:21 by Ian Whitlock

disable icons in treemacs due to rendering bug

an annoying rendering bug causes directories named bin/ to have a
stupid, ugly icon, that doesn't seem to be dependent on the theme
applied, and that I cannot find a way to control.

Debugging this also made me notice an indentation problem for files
ending in .bash and .sqlite which I had previously applied custom
icons to. I was unable to even get this far with the bin directory due
to limitations with Treemacs's documentation.. it only documents how
to create custom icons for files, and these suffer from the
indentation problem.

Maybe this is due to my config, maybe not, but the bin dir was making
me want to stab my eyes out and at least now, with the icons disabled,
it looks nice again and it is perhaps even nicer than it was to start
with. All I know is that I can see the files in their tree layout and
it doesn't make my eyes bleed anymore. Fine.

Revert this commit if they ever fix the problem upstream. I lost two
and a half hours to trying to fix it here, I'm done. Disabled icons is
fine. Fuck.

🫠

---

