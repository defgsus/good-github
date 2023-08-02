## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-08-01](docs/good-messages/2023/2023-08-01.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,261,333 were push events containing 3,547,947 commit messages that amount to 296,670,389 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 53 messages:


## [Anomalous-0/RealGame](https://github.com/Anomalous-0/RealGame)@[40d5d3527b...](https://github.com/Anomalous-0/RealGame/commit/40d5d3527be1ef0b0ce2e92ab4a0bcf92c1d6ccd)
#### Tuesday 2023-08-01 00:05:07 by Kedar Haldar

HOLY SHIT IT KINDA LOOKS GOOD ROTATE TO POINT ON AIM

---
## [TheVekter/tgstation](https://github.com/TheVekter/tgstation)@[2d0b4f053f...](https://github.com/TheVekter/tgstation/commit/2d0b4f053f1db70d9f3ab6548f58b7928f159eaf)
#### Tuesday 2023-08-01 00:22:46 by san7890

Refactors Slaughter/Laughter Demons into Basic Mobs (#77206)

## About The Pull Request

On the tin, the former "imp" is now refactored into basic mob code. Very
simple since these are only meant to be controlled by players, and all
of their stuff was on Signal Handlers and Cooldown Actions anyways. Just
lessens the amount of stupidity.

Did you know that we were trying to make demons spawn in a `pop`'d cat
named "Laughter"? Embedded in the list? I've literally never seen this
cat, so I'm under heavy suspicion that the code we were using was broken
for the longest time (or may have never worked), and we now instead just
do it a much more sane way of having a cat spawn on our demise.

## Why It's Good For The Game

Cleaner code! Less simple mob jank to deal with. Trims down the list of
simple animals to refactor. No more duplicated code that we were already
doing on parent! It's so good man literally everything was seamless with
a bit of retooling and tinkering. The typepath is also no longer `imp`,
it's actually `demon`, which I'm happy with because there's no other
demons to have it be confused with anymore.

We were also doing copypasta on both the demon spawner bottle and the
demon spawning event so I also just unified that into the mob. I also
reorganized the sprites to be a bit clearer and match their new
nomenclature

## Changelog
:cl:
refactor: Slaughter and Laughter Demons have been refactored, please
place an issue report for any unexpected things/hitches.
fix: Laughter Demons should now actually drop a kitten.
/:cl:

---
## [TheVekter/tgstation](https://github.com/TheVekter/tgstation)@[69827604c4...](https://github.com/TheVekter/tgstation/commit/69827604c46952dd4393db8617cd494ade17bea2)
#### Tuesday 2023-08-01 00:22:46 by Watermelon914

Improves the RPG loot wizard event. (#77218)

## About The Pull Request
As the title says. Adds a bunch more stat changes to various different
items and a somewhat simple way of modifying them whilst minimizing
side-effects as much as possible.
Added a new negative curse of polymorph suffix that can randomly
polymorph you once you pick up the item.
Curse of hunger items won't start on items that are not on a turf.
Curse of polymorph will only activate when equipped.

Bodyparts, two-handed melees, bags, guns and grenades, to name a few,
have a bunch of type-specific stat changes depending on their quality.

Some items won't gain fantasy suffixes during the RPG loot event, like
stacks, chairs and paper, to make gamifying the stats a bit harder.
I'm sure there'll still be other ways to game the event, but it's not
that big of a deal since these are the easiest ways to game it.
High level items also have a cool unusual effect aura

## Why It's Good For The Game
Makes the RPG item event cooler. Right now, it's a bit lame since
everything only gains force value and wound bonus on attack. This makes
the statistic increases more type-based and make it interesting to use

It's okay for some items to be powerful since this is a wizard event and
a very impactful one too. By making the curse of hunger items not spawn
on people, it'll also make it a less painful event too.

## Changelog
:cl:
add: Expanded the RPG loot wizard event by giving various different
items their own statistic boost.
/:cl:

---------

Co-authored-by: Watermelon914 <3052169-Watermelon914@users.noreply.gitlab.com>

---
## [DaedalusDock/daedalusdock](https://github.com/DaedalusDock/daedalusdock)@[159d2aeebe...](https://github.com/DaedalusDock/daedalusdock/commit/159d2aeebee7ef681891019d52069bf898846e03)
#### Tuesday 2023-08-01 00:38:44 by Gallyus

Reagent Description and Abstract Changes (#164)

* Reagent Description and Abstract Changes...
Abstract reagents are no longer detected via a magic list.
Added a description to non-abstract reagents that were missing them.
Adds a unit test to detect non-abstract reagents missing a description.

As a consequence:
Some reagents have disappeared from lists for being abstract.
Instantiating an abstract reagent is illegal and crashes New().

* Minor fixes
It's 3am go fuck yourself.

* Apply suggestions from code review

* Allows access to a new ANSI color

* C&D creates a notice on start for logging purposes

---
## [DaedalusDock/daedalusdock](https://github.com/DaedalusDock/daedalusdock)@[a3eb90b950...](https://github.com/DaedalusDock/daedalusdock/commit/a3eb90b9504f6a21c2636a4bb8aeb8b40eb66861)
#### Tuesday 2023-08-01 00:38:44 by Gallyus

Fix Pack 3: Revenge Of The Fuck (#225)

* Various Jaunt fixes (#70431)

* Jaunt code path reworked so that traits and other effects can be removed consistently regardless of how effect is ended.
Jaunts will more consistently clean themselves up (and unjaunt you) when you lose the spell.
If a shuttle lands on you while you are jaunted it will now kill you instead of crashing and fucking with the shuttle landing process.
Z travelling while inside an object or mob will now relay that direction instead, allowing you to jaunt up and down as well as cardinally.
Mirror walk button updates at correct times.
Blood and Shadow walk buttons have same functionality as Mirror Walk.

* Fixes Soul Scythe being able to get to Centcom by moving down on the bottom Z-level (#71171)

## About The Pull Request

`/obj/item/soulscythe/relaymove()` was using `get_step()` which doesn't
understand our multi-z system and was happily trying to move Z - 1 which
is Centcom. I'm still not really sure I understand why move() allowed
the scythe to just move right through the floor in this case, I think
moving to turfs with `density = 0` is also behaving strangely and just
skipping some checks that should keep it from moving through the floor,
but to be honest I don't fully understand the move chain and just
changing to `get_step_multiz()` at least keeps the scythe from going to
Z-levels it shouldn't.
## Why It's Good For The Game

Whilst it is fun for the scythe to go on an adventure to forbidden
Z-levels, admins probably don't appreciate these adventures so much.
## Changelog
:cl: VexingRaven
fix: Soul Scythes can no longer phase through the floor into Centcom.
/:cl:

* Fixes multi-Z ruins (Ice Moon Mining Site) not spawning (#70097)

* Fixes multi-z ruins not spawning

* I should proably commit said changelog files.

* Proc Ref wrapping

* Update to the correct procs

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>
Co-authored-by: VexingRaven <msgerbs@users.noreply.github.com>

---
## [zackkb/bark-and-beyond](https://github.com/zackkb/bark-and-beyond)@[7b78341f0f...](https://github.com/zackkb/bark-and-beyond/commit/7b78341f0faeeb7588dc98150086259d5ce2edfb)
#### Tuesday 2023-08-01 00:42:53 by zackkb

chatboard

Built out chatboard

Fixed a header issue with community.js

Added a goofy ass feature to where when the heart is clicked on the puppy picture, a container pops up and says "Such a good boy!" Idk why i did this but yeah

---
## [vdaular-dev/linksfordevs](https://github.com/vdaular-dev/linksfordevs)@[bd50e6f04f...](https://github.com/vdaular-dev/linksfordevs/commit/bd50e6f04f17d469c7b25a4f5ae40c53e7af3aee)
#### Tuesday 2023-08-01 00:46:43 by Ben Dornis

Updating: 7/31/2023 10:00:00 PM

 1. Added: Getting started with NGINX
    (https://sophiazhang.com/post/start-with-nginx/)
 2. Added: A comprehensive guide to Redux for beginners
    (https://www.tanvi.dev/blog/3-a-comprehensive-guide-to-redux-for-beginners)
 3. Added: I Paid Off $194k in Student Loans in Six Years. It Wasn’t Easy. - BJL
    (https://benjaminlabaschin.com/194k-in-loans-in-six-years/)
 4. Added: Socialized Proof of Work
    (https://blog.erlend.sh/socialized-proof-of-work)
 5. Added: File distribution over DNS: (ab)using DNS as a CDN (eighty-twenty news)
    (https://eighty-twenty.org/2023/07/31/dns-as-a-cdn)
 6. Added: So, you want to deploy on the edge?
    (https://zknill.io/posts/edge-database/)
 7. Added: AI Diaries: Two Important Facts About Generative Prose
    (https://www.davystevenson.com/articles/ai-diaries-two-important-facts-about-generative-prose)
 8. Added: Cachelines and Striped Locks — ~ngp
    (https://packetlost.dev/blog/cachelines-and-striped-locks/)
 9. Added: Gabe Henriques
    (https://gabehenriques.com/blog/space-tourism/)
10. Added: An optimal-stopping quant riddle - Emir's blog
    (https://emiruz.com/post/2023-07-30-optimal-stopping/)
11. Added: The Limits of AI: Why Not Every Problem Can Be Solved with Machine Learning - Arkavian
    (https://arkavian.com/2023/07/31/the-limits-of-ai-why-not-every-problem-can-be-solved-with-machine-learning/)
12. Added: Your Social Network Is Bigger Than You Think! – James Ashford
    (https://jrashford.com/2023/07/31/your-social-network-is-bigger-than-you-think/)
13. Added: Tribal Knowledge
    (https://daedtech.com/tribal-knowledge/)
14. Added: Poll Working
    (https://hybras.dev/posts/2023-06-06-poll-working/)
15. Added: Wasting Time to Waste Less Time
    (https://www.aidanmstrong.com/blog/wasting-time-to-waste-less-time)
16. Added: LK-99: The Live Online Race for a Room-Temperature Superconductor (Summary)
    (https://eirifu.wordpress.com/2023/07/30/lk-99-superconductor-summary/)
17. Added: Toggles suck! | Axess Lab
    (https://axesslab.com/toggles-suck/)
18. Added: Why I switched from Plaid to Stripe.. and then back to Plaid - Balance Budget
    (https://balancebudget.app/2023/07/29/why-i-switched-from-plaid-to-stripe-and-then-back-to-plaid/)
19. Added: Reflections on a Month with BBEdit and Nova — Sympolymathesy, by Chris Krycho
    (https://v5.chriskrycho.com/journal/reflections-on-a-month-with-bbedit-and-nova/)
20. Added: Security keys in the land of passkeys
    (https://blog.millerti.me/2023/07/30/security-keys-in-the-land-of-passkeys/)
21. Added: The next step: PostOwl
    (https://michaelaufreiter.com/posts/the-next-step-postowl)
22. Added: Blackmagic Design SDI-HDMI converter micro USB problems, and a rant about connector receptacles in general
    (https://www.krekr.nl/content/blackmagic-design-sdi-hdmi-converter-micro-usb-problems-and-a-rant-about-connector-receptacles-in-general/)
23. Added: Binary Heap | Concurrency Deep Dives
    (https://cmhteixeira.com/concurrency/binaryHeap.html)
24. Added: On .NET Live - Real World frontends and backends with Conduit
    (https://youtube.com/watch?v=DGrPQqyOpcU)
25. Added: Shamir Secret Sharing
    (https://max.levch.in/post/724289457144070144/shamir-secret-sharing)

Generation took: 00:10:32.3576058
 Maintenance update - cleaning up homepage and feed

---
## [alexrowe99/cub3d](https://github.com/alexrowe99/cub3d)@[e9620f5f93...](https://github.com/alexrowe99/cub3d/commit/e9620f5f9384d556dedb45a17eb66f227948590f)
#### Tuesday 2023-08-01 01:37:28 by lmells98

Updating for local device because i am a dumb dumb and restored to previous commit while having half of the new changes added so now is broken fml so much I hate myself this is what i get for doing this shit for 12hours then finally deciding i should save my progress fuck me i am so fucking stupid

---
## [MarkSuckerberg/Shiptest](https://github.com/MarkSuckerberg/Shiptest)@[9868a22114...](https://github.com/MarkSuckerberg/Shiptest/commit/9868a22114e62fd1c91f18f65beee597468e3fdc)
#### Tuesday 2023-08-01 03:17:55 by LemonInTheDark

Fixes some runtime spam from lazyloading/map templates (#73037)

Ensures we don't try and rebuild loading turfs midload

Turf refs persist through destroy, so when we changeturf earlier to get
our turf reservation, we insert our space turfs into the rebuild queue,
and then end up here where we can be rebuilt randomly, midload, with
uninit'd turfs

Avoids starting atmos machine processing until init

This avoids some runtimes with null gasmixtures

There's still trouble with atmos and template loading, pipes start
processing before their pipelines exist, so we just kinda get fucked.
Need to look into this more deeply, it involves pulling this stuff off
`on_construct` and `setup_template_machinery` and throwing it in maybe
late init, which I don't really relish but will just have to do
eventually.

Reduces runtime spam

---
## [jlsnow301/tgstation](https://github.com/jlsnow301/tgstation)@[3af26df8ca...](https://github.com/jlsnow301/tgstation/commit/3af26df8cacc24ab7ccacdfbe61005a165472e0f)
#### Tuesday 2023-08-01 03:30:02 by GoldenAlpharex

Fixes bloody soles making jumpsuits that cover your feet bloody when you're wearing shoes (#77077)

## About The Pull Request
Title says it all.

It basically made it so wearing something like a kilt would result in
the kilt getting all bloody as soon as you walked over blood, even when
you were wearing shoes, unless you wore something else that obscured
shoes.

I debated with myself a lot over the implementation for this, I was
thinking of adding some way to obscure feet in particular, but it's
honestly so niche that it could only have caused more issues elsewhere
if I tried to fix this issue that way.

---
## [Ical92/tgstation](https://github.com/Ical92/tgstation)@[7e1d97af9e...](https://github.com/Ical92/tgstation/commit/7e1d97af9e4b6b7f90fbacc754fae939b6d16e49)
#### Tuesday 2023-08-01 03:38:36 by Justice

Removes the word "chemical" from "chemical patch" (#76966)

## About The Pull Request
In #76011, I bitched and moaned about how the ChemMaster gives patches a
huge ass name. I've talked to other Medical Doctor mains and I also
heard bitching about the word "chemical", which is just a pain in the
ass. It seems many of us just end up removing it because it's so
repetitive and makes the patch's name long fnr. I don't think the word
"chemical" is really needed in there since you can clearly tell it's a
chemical patch just by looking at the word "patch" and the sprite.

I don't think this should affect anything else in the game in a negative
way. In that same issue, it was suggested that the cap for names was
increased instead, but this also solves the issue of the word "chemical"
taking up so much space in the patch's name without touching unknown
lands.
## Why It's Good For The Game
Less words, more healing!
## Changelog
:cl:
qol: The word "chemical" has been removed from "chemical patch" when
printing patches
/:cl:

---
## [Ical92/tgstation](https://github.com/Ical92/tgstation)@[0d769e0ffa...](https://github.com/Ical92/tgstation/commit/0d769e0ffaaa2b0f2be2edb9659c233860420ec1)
#### Tuesday 2023-08-01 03:38:36 by Jacquerel

Removes two redundant components (#76866)

## About The Pull Request

We're starting to get to have enough components that people don't
realise that what they want already exists but doesn't have the name
they expect 🙃

I recently added `track_hierarchical_movement` which is similar enough
to `connect_containers` that it shouldn't independently exist, even if I
like sending a new signal more than the ugly setup pattern for
`connect_loc`.

`trait_loc` is actually older than `give_turf_traits` but
`give_turf_traits` covers more edge cases than `turf_loc` so seems like
the better one to maintain.
HOWEVER `give_turf_traits` held a list of references to atoms in it,
which isn't great in an element. I couldn't think of a way to completely
eliminate the list, but it isn't a list of references any more so it
shouldn't cause any hard deletions.

## Why It's Good For The Game

Having two components which do the same thing but marginally differently
is confusing and going to cause us trouble down the line.

## Changelog

Not player facing

---
## [OSSPhilippines/opensource](https://github.com/OSSPhilippines/opensource)@[acd7da966b...](https://github.com/OSSPhilippines/opensource/commit/acd7da966b35fb4273d5002ab177e8e3e4e01668)
#### Tuesday 2023-08-01 04:00:28 by Joff Tiquez

aider: Update `CODE_OF_CONDUCT.md` based on common known templates.

# Aider chat conversation:

USER: Update `CODE_OF_CONDUCT.md` based on common known templates

ASSISTANT: Sure, I can help with that. The Contributor Covenant is a widely used template for a Code of Conduct. Here's how we can update your `CODE_OF_CONDUCT.md`:

```markdown
CODE_OF_CONDUCT.md
<<<<<<< ORIGINAL

=======
# Contributor Covenant Code of Conduct

## Our Pledge

In the interest of fostering an open and welcoming environment, we as contributors and maintainers pledge to making participation in our project and our community a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, sex characteristics, gender identity and expression, level of experience, education, socio-economic status, nationality, personal appearance, race, religion, or sexual identity and orientation.

## Our Standards

Examples of behavior that contributes to creating a positive environment include:

* Using welcoming and inclusive language
* Being respectful of differing viewpoints and experiences
* Gracefully accepting constructive criticism
* Focusing on what is best for the community
* Showing empathy towards other community members

Examples of unacceptable behavior by participants include:

* The use of sexualized language or imagery and unwelcome sexual attention or advances
* Trolling, insulting/derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or electronic address, without explicit permission
* Other conduct which could reasonably be considered inappropriate in a professional setting

## Our Responsibilities

Project maintainers are responsible for clarifying the standards of acceptable behavior and are expected to take appropriate and fair corrective action in response to any instances of unacceptable behavior.

Project maintainers have the right and responsibility to remove, edit, or reject comments, commits, code, wiki edits, issues, and other contributions that are not aligned to this Code of Conduct, or to ban temporarily or permanently any contributor for other behaviors that they deem inappropriate, threatening, offensive, or harmful.

## Scope

This Code of Conduct applies both within project spaces and in public spaces when an individual is representing the project or its community. Examples of representing a project or community include using an official project e-mail address, posting via an official social media account, or acting as an appointed representative at an online or offline event. Representation of a project may be further defined and clarified by project maintainers.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be reported by contacting the project team at [INSERT EMAIL ADDRESS]. All complaints will be reviewed and investigated and will result in a response that is deemed necessary and appropriate to the circumstances. The project team is obligated to maintain confidentiality with regard to the report of an incident. Further details of specific enforcement policies may be posted separately.

Project maintainers who do not follow or enforce the Code of Conduct in good faith may face temporary or permanent repercussions as determined by other members of the project's leadership.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant](https://www.contributor-covenant.org), version 1.4, available at https://www.contributor-covenant.org/version/1/4/code-of-conduct.html
>>>>>>> UPDATED
```

Please replace `[INSERT EMAIL ADDRESS]` with the appropriate contact email for your project.

---
## [MrGVSV/bevy](https://github.com/MrGVSV/bevy)@[fb4c21e3e6...](https://github.com/MrGVSV/bevy/commit/fb4c21e3e62b3789e8e768ac63dc2205ddec698f)
#### Tuesday 2023-08-01 05:54:31 by Ida "Iyes

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
## [Kelebek1/yuzu](https://github.com/Kelebek1/yuzu)@[8e703e08df...](https://github.com/Kelebek1/yuzu/commit/8e703e08dfcf735a08df2ceff6a05221b7cc981f)
#### Tuesday 2023-08-01 07:13:31 by comex

Implement SSL service

This implements some missing network APIs including a large chunk of the SSL
service, enough for Mario Maker (with an appropriate mod applied) to connect to
the fan server [Open Course World](https://opencourse.world/).

Connecting to first-party servers is out of scope of this PR and is a
minefield I'd rather not step into.

 ## TLS

TLS is implemented with multiple backends depending on the system's 'native'
TLS library.  Currently there are two backends: Schannel for Windows, and
OpenSSL for Linux.  (In reality Linux is a bit of a free-for-all where there's
no one 'native' library, but OpenSSL is the closest it gets.)  On macOS the
'native' library is SecureTransport but that isn't implemented in this PR.
(Instead, all non-Windows OSes will use OpenSSL unless disabled with
`-DENABLE_OPENSSL=OFF`.)

Why have multiple backends instead of just using a single library, especially
given that Yuzu already embeds mbedtls for cryptographic algorithms?  Well, I
tried implementing this on mbedtls first, but the problem is TLS policies -
mainly trusted certificate policies, and to a lesser extent trusted algorithms,
SSL versions, etc.

...In practice, the chance that someone is going to conduct a man-in-the-middle
attack on a third-party game server is pretty low, but I'm a security nerd so I
like to do the right security things.

My base assumption is that we want to use the host system's TLS policies.  An
alternative would be to more closely emulate the Switch's TLS implementation
(which is based on NSS).  But for one thing, I don't feel like reverse
engineering it.  And I'd argue that for third-party servers such as Open Course
World, it's theoretically preferable to use the system's policies rather than
the Switch's, for two reasons

1. Someday the Switch will stop being updated, and the trusted cert list,
   algorithms, etc. will start to go stale, but users will still want to
   connect to third-party servers, and there's no reason they shouldn't have
   up-to-date security when doing so.  At that point, homebrew users on actual
   hardware may patch the TLS implementation, but for emulators it's simpler to
   just use the host's stack.

2. Also, it's good to respect any custom certificate policies the user may have
   added systemwide.  For example, they may have added custom trusted CAs in
   order to use TLS debugging tools or pass through corporate MitM middleboxes.
   Or they may have removed some CAs that are normally trusted out of paranoia.

Note that this policy wouldn't work as-is for connecting to first-party
servers, because some of them serve certificates based on Nintendo's own CA
rather than a publicly trusted one.  However, this could probably be solved
easily by using appropriate APIs to adding Nintendo's CA as an alternate
trusted cert for Yuzu's connections.  That is not implemented in this PR
because, again, first-party servers are out of scope.

(If anything I'd rather have an option to _block_ connections to Nintendo
servers, but that's not implemented here.)

To use the host's TLS policies, there are three theoretical options:

a) Import the host's trusted certificate list into a cross-platform TLS
   library (presumably mbedtls).

b) Use the native TLS library to verify certificates but use a cross-platform
   TLS library for everything else.

c) Use the native TLS library for everything.

Two problems with option a).  First, importing the trusted certificate list at
minimum requires a bunch of platform-specific code, which mbedtls does not have
built in.  Interestingly, OpenSSL recently gained the ability to import the
Windows certificate trust store... but that leads to the second problem, which
is that a list of trusted certificates is [not expressive
enough](https://bugs.archlinux.org/task/41909) to express a modern certificate
trust policy.  For example, Windows has the concept of [explicitly distrusted
certificates](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/dn265983(v=ws.11)),
and macOS requires Certificate Transparency validation for some certificates
with complex rules for when it's required.

Option b) (using native library just to verify certs) is probably feasible, but
it would miss aspects of TLS policy other than trusted certs (like allowed
algorithms), and in any case it might well require writing more code, not less,
compared to using the native library for everything.

So I ended up at option c), using the native library for everything.

What I'd *really* prefer would be to use a third-party library that does option
c) for me.  Rust has a good library for this,
[native-tls](https://docs.rs/native-tls/latest/native_tls/).  I did search, but
I couldn't find a good option in the C or C++ ecosystem, at least not any that
wasn't part of some much larger framework.  I was surprised - isn't this a
pretty common use case?  Well, many applications only need TLS for HTTPS, and they can
use libcurl, which has a TLS abstraction layer internally but doesn't expose
it.  Other applications only support a single TLS library, or use one of the
aforementioned larger frameworks, or are platform-specific to begin with, or of
course are written in a non-C/C++ language, most of which have some canonical
choice for TLS.  But there are also many applications that have a set of TLS
backends just like this; it's just that nobody has gone ahead and abstracted
the pattern into a library, at least not a widespread one.

Amusingly, there is one TLS abstraction layer that Yuzu already bundles: the
one in ffmpeg.  But it is missing some features that would be needed to use it
here (like reusing an existing socket rather than managing the socket itself).
Though, that does mean that the wiki's build instructions for Linux (and macOS
for some reason?) already recommend installing OpenSSL, so no need to update
those.

 ## Other APIs implemented

- Sockets:
    - GetSockOpt(`SO_ERROR`)
    - SetSockOpt(`SO_NOSIGPIPE`) (stub, I have no idea what this does on Switch)
    - `DuplicateSocket` (because the SSL sysmodule calls it internally)
    - More `PollEvents` values

- NSD:
    - `Resolve` and `ResolveEx` (stub, good enough for Open Course World and
      probably most third-party servers, but not first-party)

- SFDNSRES:
    - `GetHostByNameRequest` and `GetHostByNameRequestWithOptions`
    - `ResolverSetOptionRequest` (stub)

 ## Fixes

- Parts of the socket code were previously allocating a `sockaddr` object on
  the stack when calling functions that take a `sockaddr*` (e.g. `accept`).
  This might seem like the right thing to do to avoid illegal aliasing, but in
  fact `sockaddr` is not guaranteed to be large enough to hold any particular
  type of address, only the header.  This worked in practice because in
  practice `sockaddr` is the same size as `sockaddr_in`, but it's not how the
  API is meant to be used.  I changed this to allocate an `sockaddr_in` on the
  stack and `reinterpret_cast` it.  I could try to do something cleverer with
  `aligned_storage`, but casting is the idiomatic way to use these particular
  APIs, so it's really the system's responsibility to avoid any aliasing
  issues.

- I rewrote most of the `GetAddrInfoRequest[WithOptions]` implementation.  The
  old implementation invoked the host's getaddrinfo directly from sfdnsres.cpp,
  and directly passed through the host's socket type, protocol, etc. values
  rather than looking up the corresponding constants on the Switch.  To be
  fair, these constants don't tend to actually vary across systems, but
  still... I added a wrapper for `getaddrinfo` in
  `internal_network/network.cpp` similar to the ones for other socket APIs, and
  changed the `GetAddrInfoRequest` implementation to use it.  While I was at
  it, I rewrote the serialization to use the same approach I used to implement
  `GetHostByNameRequest`, because it reduces the number of size calculations.
  While doing so I removed `AF_INET6` support because the Switch doesn't
  support IPv6; it might be nice to support IPv6 anyway, but that would have to
  apply to all of the socket APIs.

  I also corrected the IPC wrappers for `GetAddrInfoRequest` and
  `GetAddrInfoRequestWithOptions` based on reverse engineering and hardware
  testing.  Every call to `GetAddrInfoRequestWithOptions` returns *four*
  different error codes (IPC status, getaddrinfo error code, netdb error code,
  and errno), and `GetAddrInfoRequest` returns three of those but in a
  different order, and it doesn't really matter but the existing implementation
  was a bit off, as I discovered while testing `GetHostByNameRequest`.

  - The new serialization code is based on two simple helper functions:

    ```cpp
    template <typename T> static void Append(std::vector<u8>& vec, T t);
    void AppendNulTerminated(std::vector<u8>& vec, std::string_view str);
    ```

    I was thinking there must be existing functions somewhere that assist with
    serialization/deserialization of binary data, but all I could find was the
    helper methods in `IOFile` and `HLERequestContext`, not anything that could
    be used with a generic byte buffer.  If I'm not missing something, then
    maybe I should move the above functions to a new header in `common`...
    right now they're just sitting in `sfdnsres.cpp` where they're used.

- Not a fix, but `SocketBase::Recv`/`Send` is changed to use `std::span<u8>`
  rather than `std::vector<u8>&` to avoid needing to copy the data to/from a
  vector when those methods are called from the TLS implementation.

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[7e2fba4cb0...](https://github.com/treckstar/yolo-octo-hipster/commit/7e2fba4cb0917b999e495d08ae3c69bce86a2383)
#### Tuesday 2023-08-01 07:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [Tyranicranger4/tgstation](https://github.com/Tyranicranger4/tgstation)@[221e82c364...](https://github.com/Tyranicranger4/tgstation/commit/221e82c3640c75d99dc2616bf666bd897b4a5be8)
#### Tuesday 2023-08-01 07:40:47 by ChungusGamer666

[NO GBP] Fixes my fuckups with species livers (#76331)

## About The Pull Request

Fixes https://github.com/tgstation/tgstation/issues/76329
I DID A REAL STUPID MISTAKE WHILE CODING
https://github.com/tgstation/tgstation/pull/76184 I AM SORRY
The signal was sending the fucking human instead of seconds_per_tick

## Why It's Good For The Game

Fixes a BUNCH of liver behavior including plasmamen livers not healing
wounds

## Changelog

:cl:
fix: Plasma will now heal plasmamen properly
/:cl:

---
## [SagaStars/Shiptest](https://github.com/SagaStars/Shiptest)@[1b315a616f...](https://github.com/SagaStars/Shiptest/commit/1b315a616ff24e3f1f92c791e4df4dc43ca9aad6)
#### Tuesday 2023-08-01 07:45:36 by Thedragmeme

Aegis update + patient clothing (#2150)

## About The Pull Request
The Aegis:
![2023-07-09 06 32
40](https://github.com/shiptest-ss13/Shiptest/assets/81540056/cf262257-1699-40e0-bcb1-6dc60f1e98a6)
I've touched up the central hallway's decals, they always bothered me
but at the time of the Aegis' creation, I wasn't as well versed with map
making as I am now. They're small tweaks that look better to me. The
smart fridge was removed and turned into a board, originally you could
access the smart fridge from outside of the ship, which wasn't intended.
Added some new posters. Compressed the number of red lockers down and
cleaned up the main hallway. I gave the psychologist a dart gun because
honestly, it sounded really funny.

![dart
riffle](https://github.com/shiptest-ss13/Shiptest/assets/81540056/eb10154a-1e28-4a5d-b41b-9b20f92b71a9)

Also, there are more seeds to make food with. There were like only two
food seeds and like five flowers before.

The Patient set:


![patient](https://github.com/shiptest-ss13/Shiptest/assets/81540056/65066ea3-92d1-4233-9bf6-a6448d43b11f)

Kepori and Vox versions are available. Long-term patients now spawn with
the white gown and slippers. The previous clothes they spawned with were
always intended to be replaced.

Hopefully, this PR also fixes long-term patients spawning with borked
ID's.

## Why It's Good For The Game

Fixing stuff, making stuff look better, and adding new RP opportunities
with clothes are good.

## Changelog

:cl: Drag
add: Adds a bunch of shit to the Aegis, nothing earth shattering
add: Added the patient set, along with Vox and Kepori compatible sprites
tweak: tweaked with the Aegis' decals
fix: (Hopefully) Fixes the Aegis' patient Id's
:cl:

---------

Signed-off-by: Thedragmeme <81540056+Draggeru@users.noreply.github.com>
Co-authored-by: thgvr <81882910+thgvr@users.noreply.github.com>

---
## [bittide/bittide-hardware](https://github.com/bittide/bittide-hardware)@[548627cbb4...](https://github.com/bittide/bittide-hardware/commit/548627cbb4f82e1b991e2ffff428601bf009641b)
#### Tuesday 2023-08-01 09:11:08 by Martijn Bastiaan

Run CI earlier at night (#337)

We currently experience clog ups in the morning

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[ea0c901f6c...](https://github.com/treckstar/yolo-octo-hipster/commit/ea0c901f6c4b80aab7ae726f764f8afea41c4b8b)
#### Tuesday 2023-08-01 09:22:04 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[35cb1556ad...](https://github.com/tgstation/tgstation/commit/35cb1556ad4bad7703b75c0edc472ed41a5fb34f)
#### Tuesday 2023-08-01 09:38:11 by carlarctg

When Space Dragons devour people they get .extinguish()ed (#77248)

## About The Pull Request

When Space Dragons devour people they get extinguished, removing flames.
## Why It's Good For The Game

> When Space Dragons devour people they get extinguished, removing
flames.

I find it quite annoying that even after you die to a space dragon, the
jackass melts not just your jumpsuit, your suit, your hat, your mask, he
also melts your entire skin off, leaving your body husked with 400
million burn damage when and if the dragon finally dies. I don't think
there's any real reason for this to be necessary, it doesn't help the
dragon in any way - It's just kind of a middle finger to the dead guy,
or more accurately, an oversight.

Worse, because the flame sprite is stupidly noisy, when a dragon DOES
die the corpses are all thrown around randomly and they all look the
exact same, which makes it easier to ignore them.

If there's a concern about tracking sensors, I can make it disable them,
but honestly if you can do that with demons I don't see why this would
be a problem. Not even accounting for the fact that many jumpsuits
ingame are fireproof.
## Changelog
:cl:
qol: When Space Dragons devour people they get extinguished, removing
flames.
/:cl:

---
## [alessiotucci/FdF_42](https://github.com/alessiotucci/FdF_42)@[723b150322...](https://github.com/alessiotucci/FdF_42/commit/723b150322e25cf243303f676d93919f8e271995)
#### Tuesday 2023-08-01 10:26:11 by Alessio Tucci

I am dumb, don't know how to work with pointers, *info->lsize instead of info->lsize FUCK YOU DUMB

---
## [preprio/next.js](https://github.com/preprio/next.js)@[6238f8a5c0...](https://github.com/preprio/next.js/commit/6238f8a5c0ffabb7dfb35872c52c942ed7f148da)
#### Tuesday 2023-08-01 10:57:26 by Jimmy Lai

performance: don't compile on hover on dev (#51830)

An annoying issue that slows down compilation times in dev for Next is
that we might trigger compilation of a page via hover on app.

We do this because we want the same experience in production and dev and
the prefetching is important for instantaneous loading states.

The alternative in this PR is that we don't prefetch at all anymore in
dev but instead, when we handle navigation, we can force a prefetch
navigation.

The slight compromise with this approach is that you can't test
prefetching anymore in dev.


<!-- Thanks for opening a PR! Your contribution is much appreciated.
To make sure your PR is handled as smoothly as possible we request that
you follow the checklist sections below.
Choose the right checklist for the change(s) that you're making:

## For Contributors

### Improving Documentation

- Run `pnpm prettier-fix` to fix formatting issues before opening the
PR.
- Read the Docs Contribution Guide to ensure your contribution follows
the docs guidelines:
https://nextjs.org/docs/community/contribution-guide

### Adding or Updating Examples

- The "examples guidelines" are followed from our contributing doc
https://github.com/vercel/next.js/blob/canary/contributing/examples/adding-examples.md
- Make sure the linting passes by running `pnpm build && pnpm lint`. See
https://github.com/vercel/next.js/blob/canary/contributing/repository/linting.md

### Fixing a bug

- Related issues linked using `fixes #number`
- Tests added. See:
https://github.com/vercel/next.js/blob/canary/contributing/core/testing.md#writing-tests-for-nextjs
- Errors have a helpful link attached, see
https://github.com/vercel/next.js/blob/canary/contributing.md

### Adding a feature

- Implements an existing feature request or RFC. Make sure the feature
request has been accepted for implementation before opening a PR. (A
discussion must be opened, see
https://github.com/vercel/next.js/discussions/new?category=ideas)
- Related issues/discussions are linked using `fixes #number`
- e2e tests added
(https://github.com/vercel/next.js/blob/canary/contributing/core/testing.md#writing-tests-for-nextjs
- Documentation added
- Telemetry added. In case of a feature if it's used or not.
- Errors have a helpful link attached, see
https://github.com/vercel/next.js/blob/canary/contributing.md


## For Maintainers

- Minimal description (aim for explaining to someone not on the team to
understand the PR)
- When linking to a Slack thread, you might want to share details of the
conclusion
- Link both the Linear (Fixes NEXT-xxx) and the GitHub issues
- Add review comments if necessary to explain to the reviewer the logic
behind a change

### What?

### Why?

### How?

Closes NEXT-
Fixes #

-->

link NEXT-1317

---
## [RandomTales/Naruto_Ninpou](https://github.com/RandomTales/Naruto_Ninpou)@[729f86792a...](https://github.com/RandomTales/Naruto_Ninpou/commit/729f86792ada265a5a1ce3e0637e0fe9deb7a7d0)
#### Tuesday 2023-08-01 11:48:02 by RandomTales

Random

If hidan hits someone with his R W there is now a blood sound
Ino skin removed
Kurenai E delay before moving units changed to 0.3s from 0.5s
Kurenai Q/R casting time shortened to hopefully reduce the clunky feeling of her
Kushina small rework:
	Kushina E/D in base from deleted
	Kushina new D:
		Instant, 60s cd, Grants Kushina her level in Taijutsu for 6s at the cost of 25% of her hp, can't be used to suicide
	Kushina E in her T form moved to her base form it now deals Taijusu/1.5 x Magic damage and was changed from 150 degrees to 60
	Kushina W in her T form no longer pauses her
	Kushina D in her T form is now Immolation
	Kushina R in her T form moved to Q
	Kushina Q in her T form moved to E
		- Makes it more like Naruto's T in combo ability order
	Kushina new R in her T form:
		Instant, 90s cd, Kushina puts a seal around her that seals all enemies within 500 AoE silencing, slowing by 70% and dealing 8 x Taijusu + 500 Chaos damage over 3s

---
## [Sonic121x/Skyrat-tg](https://github.com/Sonic121x/Skyrat-tg)@[1fe7b10e33...](https://github.com/Sonic121x/Skyrat-tg/commit/1fe7b10e339ea0d6a3d49f864e1badc5c831e791)
#### Tuesday 2023-08-01 12:25:31 by SkyratBot

[MIRROR] Removes TTS voice disable option (Skyrat: Actually makes a functional "None" voice option this time) [MDB IGNORE] (#22283)

* Removes TTS voice disable option (#76530)

## About The Pull Request
Removes the TTS voice disable option, which was already unavailable on
TG as it was set to off by default. The reason this was added was so
that downstreams could toggle the config on or off.

## Why It's Good For The Game
I think this option fundamentally undermines the TTS system because it
allows individual players to disable their voice globally, meaning that
players who have TTS enabled will not be able to hear them.

This worsens the experience for players who have TTS enabled and it's
not something I want to include as an option. If players don't like
their voice, they can turn TTS off for themselves so that they don't
hear the voices. If players don't want to customize their voice, they
can quickly choose a random voice, and we can take directions in the
future to make voice randomization consistent with gender so that a male
does not get randomly assigned a female voice and vice versa.

This option is already unavailable on TG servers because it was
primarily added for downstreams, but I don't think giving downstreams
the option to undermine the TTS system is the right direction to take.
Downstreams are still completely free to code this option on their own
codebase.

---------

Co-authored-by: Watermelon914 <3052169-Watermelon914@ users.noreply.gitlab.com>

* Removes TTS voice disable option

* Returns the option to not have a voice to TTS, properly this time

---------

Co-authored-by: Watermelon914 <37270891+Watermelon914@users.noreply.github.com>
Co-authored-by: Watermelon914 <3052169-Watermelon914@ users.noreply.gitlab.com>
Co-authored-by: GoldenAlpharex <jerego1234@hotmail.com>

---
## [swf541/ColdWarIronCurtain](https://github.com/swf541/ColdWarIronCurtain)@[5af5cf395d...](https://github.com/swf541/ColdWarIronCurtain/commit/5af5cf395d7c9aa88d8d32fdb001550cfee8912b)
#### Tuesday 2023-08-01 13:41:38 by ADMIRAL360

Korea fix, now it's bootable. Fuck you padadox you piece a shit.

---
## [spzala/benchmark](https://github.com/spzala/benchmark)@[745644f391...](https://github.com/spzala/benchmark/commit/745644f391b4d11da107b2c82fe2d7a3eacf561d)
#### Tuesday 2023-08-01 13:43:35 by Mark Saroufim

FIX SAM for bfloat16 (#1764)

Summary:
Ok this was kinda annoying

Basically the SAM codebase had a few places where it hardcodes `torch.float32` such that even if you convert the model to `torch.bfloat16` a few parts of the model won't be and will have type mismatch errors - this fixes the problem cpuhrsch desertfire - idk enough about floats and why there isn't some type promotion rule for bfloat16

I wonder whether we should add tests for multiple dtypes in torchbench to make checking for this kind of issue more robust especially now that bfloat16 seems to be the default for dynamo xuzhao9

## Logs

```
FAILED (errors=1)
(sam) ubuntu@ip-172-31-9-217:~/benchmark$ python test.py -k "test_sam_eval_cuda"
E
======================================================================
ERROR: test_sam_eval_cuda (__main__.TestBenchmark)
----------------------------------------------------------------------
components._impl.workers.subprocess_rpc.ChildTraceException: Traceback (most recent call last):
  File "/home/ubuntu/benchmark/components/_impl/workers/subprocess_rpc.py", line 482, in _run_block
    exec(  # noqa: P204
  File "<subprocess-worker>", line 2, in <module>
  File "/home/ubuntu/benchmark/torchbenchmark/util/model.py", line 280, in invoke
    out = self.eval()
  File "/home/ubuntu/benchmark/torchbenchmark/models/sam/__init__.py", line 65, in eval
    masks, scores, logits = predictor.predict(
  File "/home/ubuntu/benchmark/torchbenchmark/models/sam/predictor.py", line 164, in predict
    low_res_masks_np = low_res_masks[0].detach().cpu().numpy()
TypeError: Got unsupported ScalarType BFloat16

    working_dir: /tmp/tmpg5de41du
    stdout:
        [2023-07-13] 01:57:38.499061: TIMER_SUBPROCESS_BEGIN_EXEC
        [2023-07-13] 01:57:39.002078: TIMER_SUBPROCESS_FAILED
        [2023-07-13] 01:57:39.002141: TIMER_SUBPROCESS_FINISHED
        [2023-07-13] 01:57:39.002153: TIMER_SUBPROCESS_BEGIN_READ

    stderr:

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/ubuntu/benchmark/test.py", line 104, in eval_fn
    task.invoke()
  File "/home/ubuntu/benchmark/torchbenchmark/__init__.py", line 402, in invoke
    self.worker.run("""
  File "/home/ubuntu/benchmark/components/_impl/workers/subprocess_worker.py", line 155, in run
    self._run(snippet)
  File "/home/ubuntu/benchmark/components/_impl/workers/subprocess_worker.py", line 320, in _run
    subprocess_rpc.SerializedException.raise_from(
  File "/home/ubuntu/benchmark/components/_impl/workers/subprocess_rpc.py", line 458, in raise_from
    raise e from ChildTraceException(traceback_str)
TypeError: Got unsupported ScalarType BFloat16

----------------------------------------------------------------------
Ran 1 test in 7.814s

FAILED (errors=1)
(sam) ubuntu@ip-172-31-9-217:~/benchmark$ python test.py -k "test_sam_eval_cuda"
.
----------------------------------------------------------------------
Ran 1 test in 8.315s

OK
```

Pull Request resolved: https://github.com/pytorch/benchmark/pull/1764

Reviewed By: drisspg, cpuhrsch

Differential Revision: D47441873

Pulled By: msaroufim

fbshipit-source-id: a60880fd7c0826cfd469ace39d76894469ca0e5e

---
## [SynthTwo/Paradise](https://github.com/SynthTwo/Paradise)@[2d10818063...](https://github.com/SynthTwo/Paradise/commit/2d1081806334fc023de600338b836d55dd6fa5ee)
#### Tuesday 2023-08-01 13:54:32 by ATP-Engineer

Fixes IV bag blood overlays being too damn bright for some mixtures (#21813)

* Removes old .dmi

* Fixes blood overlay coloring being too bright for IV bags

* Fine-tuning

* Makes the blood bag IV color overlays not as bright as they used to be

In hindsight it was probably easy to avoid

* FINAL TUNE UP

FUCK

* Fixes coloring for IV bags so they're not too bright

FINAL COMMIT

---
## [hrtowii/WDBFontOverwrite](https://github.com/hrtowii/WDBFontOverwrite)@[3b7f34e750...](https://github.com/hrtowii/WDBFontOverwrite/commit/3b7f34e7509bfa9f1ffb6fab069157613bbd20e1)
#### Tuesday 2023-08-01 15:07:06 by Dỏa

Added offset for iPhone SE 2022, iOS 16.4

Honestly, I'm stupid at this. So, can you check if there's any mistake? Thank you xD

---
## [Ayush-kaithwas/Ayush-kaithwas](https://github.com/Ayush-kaithwas/Ayush-kaithwas)@[9885b49dfd...](https://github.com/Ayush-kaithwas/Ayush-kaithwas/commit/9885b49dfdee2510082379ec1e1650d9f30c6ca9)
#### Tuesday 2023-08-01 15:13:23 by Omnific

Update README.md

Introducing myself, I am Ayush Kaithwas, a versatile tech enthusiast who finds joy in exploring the realms of electronics and web development. With an insatiable curiosity and a drive to learn, I have honed my skills to become a tech wizard with a unique combination of expertise.

When it comes to electronics, I thrive on the excitement of the Internet of Things (IoT) and the possibilities it offers. Armed with a deep understanding of programming languages like C , C++ and python , I relish the challenge of creating intelligent and interconnected systems. My passion for embedded systems allows me to bring hardware to life, making it dance to my commands flawlessly. From microcontrollers to Linux systems, I have immersed myself in the intricacies of these technologies to build innovative solutions.

On the flip side, I find equal gratification in the vibrant world of web development. My proficiency in React.js empowers me to craft captivating user interfaces that leave a lasting impact. Pairing that with my expertise in MongoDB, Express.js, and Node.js, I create powerful web applications that deliver seamless user experiences and efficient data management.

What sets me apart is my unwavering commitment to staying at the cutting edge of technology. Continuously exploring new tools and trends, I am eager to embrace challenges that expand my skill set. I am not just content with acquiring knowledge; I am driven to apply it to build projects that make a positive impact.

Beyond the confines of coding, I am a firm believer in the spirit of collaboration and open-source contributions. Sharing knowledge and insights with the tech community, mentoring aspiring developers, and fostering an atmosphere of innovation are endeavors close to my heart.

In this rapidly evolving tech landscape, I am the architect of my future, paving the way for groundbreaking experiences where electronics and web development converge. Join me on this exhilarating journey, and together, let's shape a brighter, tech-driven future! 🚀

---
## [alliscode/semantic-kernel](https://github.com/alliscode/semantic-kernel)@[eab7a8f63a...](https://github.com/alliscode/semantic-kernel/commit/eab7a8f63a0bfd289070e82b423ac78bd306ee5b)
#### Tuesday 2023-08-01 15:24:54 by Sailesh R

Python: implemented web search engine skill with bing connector (#1813)

### Motivation and Context
<!-- Thank you for your contribution to the semantic-kernel repo!
Please help reviewers and future users, providing the following
information:
  1. Why is this change required?
  2. What problem does it solve?
  3. What scenario does it contribute to?
  4. If it fixes an open issue, please link to the issue here.
-->
In this PR, I have tried my hand at an implementation of web search
engine skill in python semantic kernel using the Bing Web Search API.

### Description
<!-- Describe your changes, the overall approach, the underlying design.
These notes will help understanding how your code works. Thanks! -->
In the semantic kernel directory, I have added a new directory called
web_skills (To replicate Skills.Web from C#) and added the web search
skill here. For now, I have implemented web search using the bing web
search API. If this approach is fine, then I can implement the same with
the google search API too. I have tried to stick with similar naming
conventions as used in the C# implementation with matching context
parameters and arguments.

I can also add some unit tests for the connectors and the search skill,
and add something like exponential backoff to avoid rate limit errors
while querying the search APIs.

Here is some sample code that checks the working of the search skill.

```python
import os
import semantic_kernel as sk
from semantic_kernel.web_skills.web_search_engine_skill import WebSearchEngineSkill
from semantic_kernel.web_skills.connectors import BingConnector
from semantic_kernel.connectors.ai.open_ai import OpenAITextCompletion

async def main():
    kernel = sk.Kernel()
    api_key, org_id = sk.openai_settings_from_dot_env()
    kernel.add_text_completion_service(
        "dv", OpenAITextCompletion("text-davinci-003", api_key, org_id)
    )
    connector = BingConnector(api_key=os.getenv("BING_API_KEY"))
    web_skill = kernel.import_skill(WebSearchEngineSkill(connector), "WebSearch")

    prompt = "Who is Leonardo DiCaprio's current girlfriend?"
    search_async = web_skill["searchAsync"]
    result = await search_async.invoke_async(prompt)
    print(result)

    """
    Output:
    ["Celebrity Celebrity News Everything You Need to Know About Leonardo DiCaprio and Camila Morrone's Relationship From the beginning of their romance to today, we track their relationship here. By..."]
    """

    prompt = """
    Answer the question using only the data that is provided in the data section. Do not use any prior knowledge to answer the question.
    Data: {{WebSearch.SearchAsync "What is semantic kernel?"}}
    Question: What is semantic kernel?
    Answer:
    """

    qna = kernel.create_semantic_function(prompt, temperature=0.2)
    context = kernel.create_new_context()
    context["count"] = "10"
    context["offset"] = "0"
    result = await qna.invoke_async(context=context)
    print(result)

    """
    Output:
    Semantic Kernel is an open-source SDK that lets you easily combine AI services like OpenAI, Azure OpenAI, and Hugging Face with conventional programming languages like C# and Python. By doing so, you can create AI apps that combine the best of both worlds. Semantic Kernel is at the center of the copilot stack.
    """

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
```

### Contribution Checklist
<!-- Before submitting this PR, please make sure: -->
- [x] The code builds clean without any errors or warnings
- [x] The PR follows SK Contribution Guidelines
(https://github.com/microsoft/semantic-kernel/blob/main/CONTRIBUTING.md)
- [x] The code follows the .NET coding conventions
(https://learn.microsoft.com/dotnet/csharp/fundamentals/coding-style/coding-conventions)
verified with `dotnet format`
- [ ] All unit tests pass, and I have added new tests where possible
- [x] I didn't break anyone :smile:

---------

Co-authored-by: Abby Harrison <54643756+awharrison-28@users.noreply.github.com>
Co-authored-by: Abby Harrison <abby.harrison@microsoft.com>

---
## [phillipwood/git](https://github.com/phillipwood/git)@[52106430dc...](https://github.com/phillipwood/git/commit/52106430dc80ea20ec2e00a6079a7bc114d36b70)
#### Tuesday 2023-08-01 15:37:06 by Ævar Arnfjörð Bjarmason

refs/files: remove "name exist?" check in lock_ref_oid_basic()

In lock_ref_oid_basic() we'll happily lock a reference that doesn't
exist yet. That's normal, and is how references are initially born,
but we don't need to retain checks here in lock_ref_oid_basic() about
the state of the ref, when what we're checking is either checked
already, or something we're about to discover by trying to lock the
ref with raceproof_create_file().

The one exception is the caller in files_reflog_expire(), who passes
us a "type" to find out if the reference is a symref or not. We can
move the that logic over to that caller, which can now defer its
discovery of whether or not the ref is a symref until it's needed. In
the preceding commit an exhaustive regression test was added for that
case in a new test in "t1417-reflog-updateref.sh".

The improved diagnostics here were added in
5b2d8d6f218 (lock_ref_sha1_basic(): improve diagnostics for ref D/F
conflicts, 2015-05-11), and then much of the surrounding code went
away recently in my 245fbba46d6 (refs/files: remove unused "errno ==
EISDIR" code, 2021-08-23).

The refs_resolve_ref_unsafe() code being removed here looks like it
should be tasked with doing that, but it's actually redundant to other
code.

The reason for that is as noted in 245fbba46d6 this once widely used
function now only has a handful of callers left, which all handle this
case themselves.

To the extent that we're racy between their check and ours removing
this check actually improves the situation, as we'll be doing fewer
things between the not-under-lock initial check and acquiring the
lock.

Why this is OK for all the remaining callers of lock_ref_oid_basic()
is noted below. There are only two of those callers:

* "git branch -[cm] <oldbranch> <newbranch>":

  In files_copy_or_rename_ref() we'll call this when we copy or rename
  refs via rename_ref() and copy_ref(). but only after we've checked
  if the refname exists already via its own call to
  refs_resolve_ref_unsafe() and refs_rename_ref_available().

  As the updated comment to the latter here notes neither of those are
  actually needed. If we delete not only this code but also
  refs_rename_ref_available() we'll do just fine, we'll just emit a
  less friendly error message if e.g. "git branch -m A B/C" would have
  a D/F conflict with a "B" file.

  Actually we'd probably die before that in case reflogs for the
  branch existed, i.e. when the try to rename() or copy_file() the
  relevant reflog, since if we've got a D/F conflict with a branch
  name we'll probably also have the same with its reflogs (but not
  necessarily, we might have reflogs, but it might not).

  As some #leftoverbits that code seems buggy to me, i.e. the reflog
  "protocol" should be to get a lock on the main ref, and then perform
  ref and/or reflog operations. That code dates back to
  c976d415e53 (git-branch: add options and tests for branch renaming,
  2006-11-28) and probably pre-dated the solidifying of that
  convention. But in any case, that edge case is not our bug or
  problem right now.

* "git reflog expire <ref>":

  In files_reflog_expire() we'll call this without previous ref
  existence checking in files-backend.c, but that code is in turn
  called by code that's just finished checking if the refname whose
  reflog we're expiring exists.

  See ae35e16cd43 (reflog expire: don't lock reflogs using previously
  seen OID, 2021-08-23) for the current state of that code, and
  5e6f003ca8a (reflog_expire(): ignore --updateref for symbolic
  references, 2015-03-03) for the code we'd break if we only did a
  "update = !!ref" here, which is covered by the aforementioned
  regression test in "t1417-reflog-updateref.sh".

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [Shoodler/Codeforces](https://github.com/Shoodler/Codeforces)@[d34ee07864...](https://github.com/Shoodler/Codeforces/commit/d34ee07864eb7b62b79acac74797f8e84deb749b)
#### Tuesday 2023-08-01 16:18:02 by Shantanu Shaji

Watermelon completed

One hot summer day Pete and his friend Billy decided to buy a watermelon. They chose the biggest and the ripest one, in their opinion. After that the watermelon was weighed, and the scales showed w kilos. They rushed home, dying of thirst, and decided to divide the berry, however they faced a hard problem.

Pete and Billy are great fans of even numbers, that's why they want to divide the watermelon in such a way that each of the two parts weighs even number of kilos, at the same time it is not obligatory that the parts are equal. The boys are extremely tired and want to start their meal as soon as possible, that's why you should help them and find out, if they can divide the watermelon in the way they want. For sure, each of them should get a part of positive weight.

Input
The first (and the only) input line contains integer number w (1 ≤ w ≤ 100) — the weight of the watermelon bought by the boys.

Output
Print YES, if the boys can divide the watermelon into two parts, each of them weighing even number of kilos; and NO in the opposite case.

---
## [CodeWithEmad/tutor](https://github.com/CodeWithEmad/tutor)@[18ce1f2fe4...](https://github.com/CodeWithEmad/tutor/commit/18ce1f2fe432a82fd97711d3d5766e8d47185f9e)
#### Tuesday 2023-08-01 16:34:36 by Régis Behmo

feat: persistent bind-mounts

This is an important change, where we get remove the previous `--mount`
option, and instead opt for persistent bind-mounts.

Persistent bind mounts have several advantages:
- They make it easier to remember which folders need to be bind-mounted.
- Code is *much* less clunky, as we no longer need to generate temporary
  docker-compose files.
- They allow us to bind-mount host directories *at build time* using the
  buildx `--build-context` option.
- The transition from development to production becomes much easier, as
  images will automatically be built using the host repo.

The only drawback is that persistent bind-mounts are slightly less
portable: when a config.yml file is moved to a different folder, many
things will break if the repo is not checked out in the same path.

For instance, this is how to start working on a local fork of
edx-platform:

    tutor config save --append MOUNTS=/path/to/edx-platform

And that's all there is to it. No, this fork will be used whenever we
run:

    tutor images build openedx
    tutor local start
    tutor dev start

This change is made possible by huge improvements in the build time
performance. These improvements make it convenient to re-build Docker
images often.

Related issues:
https://github.com/openedx/wg-developer-experience/issues/71
https://github.com/openedx/wg-developer-experience/issues/66
https://github.com/openedx/wg-developer-experience/issues/166

---
## [iLikeMemes/TerraGov-Marine-Corps](https://github.com/iLikeMemes/TerraGov-Marine-Corps)@[ca4b66185f...](https://github.com/iLikeMemes/TerraGov-Marine-Corps/commit/ca4b66185ffa363692529f8340a43cccab02cbf1)
#### Tuesday 2023-08-01 17:25:42 by chizzy376

Gives the Umbilical Tad shutters on side windows. (#13490)

* y

* Update combat_patrol.dm

* Update combat_patrol.dm

Sometimes I think about if life is really worth the hassle, if I really have to deal with so much bs only to then have to believe hard enough to get into heaven. Am I a good person for heaven? Do I deserve it? fuck if i know

* Finish fixing my fuckup

---
## [leonerd/perl5](https://github.com/leonerd/perl5)@[15119347e4...](https://github.com/leonerd/perl5/commit/15119347e461bd5ff2afb671b1c8138cbe635b42)
#### Tuesday 2023-08-01 18:10:45 by Yves Orton

epigraphs.pod - add epigraph from 5.37.10

My dad had beautiful handwriting, and whenever he got a new pen he would
write out this stanza of Lewis Carrolls poem on the blue lined paper he
used to write his notes on. So this is my homage to him.

For some reason I can never remember the wording properly and say it
as "to /speak/ of many things" instead of "to /talk/ of many things".
Memory is a funny thing.

---
## [realforest2001/forest-cm13](https://github.com/realforest2001/forest-cm13)@[f5784dabc7...](https://github.com/realforest2001/forest-cm13/commit/f5784dabc77752802da20f2d14787667161d61ac)
#### Tuesday 2023-08-01 18:22:10 by ihatethisengine

More portable cades tweaks and buffs (#3967)

# About the pull request

Despite making a lot of tweaks and changes to portable cades I barely
touched them in the game until recently. Now I have more experience and
can tweak it again.

1) You can now stack damaged cades and stack stores health of each cade.
You can repair stacked cades but it will take longer time.

2) Miniengi pamphlet allows faster repairs but only when cade is folded.

3) You can quickly collapse portable cades with crowbar if you have at
least miniengi skills.

4) You no longer need to have folded portable cade in hand in order to
repair it, but if you do, you can move while repairing.

# Explain why it's good for the game

1) It's extremely annoying to repair each individual cade in order to
stack them just because it got hit by a stray bullet once. Now you can
just ignore damage and keep going.

2) Yeah it took 10 second for PFC to repair each single cade. Really
long. Now it's 5 seconds, but only when folded and if you have miniengi
skills. Makes miniengi pamphlet a bit more relevant.

3) It was intended, but turned out it was a bit inconvenient. It was
faster to collapse by hand because you didn't need to deal with tools.
Now it requires just a crowbar and slightly faster. Also requires
miniengi skill to use crowbar.

4) First was just a bit annoying, second allows more mobility which is
the point of portable barricades.


# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl: ihatethisengine
balance: you can stack scratched portable cades if their HP at least
75%. Doing so will reduce the health of all barricades in the stack to
the level of the most damaged.
balance: you can repair stacked portable cades but it will take longer
time depending on how many cades in stack.
balance: miniengi skill makes repairs of folded portable cades faster
(10 seconds to 5 seconds, same as engineer).
balance: with engineering skill at least of miniengi you can collapse
deployed portable barricade with a crowbar (wrench is no longer
required, slightly faster (2 sec to 1.5 sec)).
balance: you no longer need to have folded portable cade in hand in
order to repair it.
balance: if you have folded portable cade in hand, you can move while
repairing it.
/:cl:

---------

Co-authored-by: ihatethisengine <treml.treml@yandex.ru>

---
## [OnionUI/Onion](https://github.com/OnionUI/Onion)@[8383dda087...](https://github.com/OnionUI/Onion/commit/8383dda087ac09f4e6bdbd52a0d034dcc853a013)
#### Tuesday 2023-08-01 18:45:45 by XK

FIX: ScummVM scrollbars - revert from 2.8.0git to 2.7.1stable (#1092)

## Overview
Fix missing scrollbars in options containers. 
Adds new bin & new themes.

ScummVM downgraded to 2.7.1 STABLE built from source with same engine
support as before - 2.8.0 master branch has not been updated with the
container scroll-bar fix that 2.7.1 has.

Release announcement: https://www.scummvm.org/news/20230731
Release notes:
https://downloads.scummvm.org/frs/scummvm/2.7.1/ReleaseNotes.html
GH branch: https://github.com/scummvm/scummvm/tree/branch-2-7-1

<img
src="https://github.com/OnionUI/Onion/assets/47260768/10dce908-0e76-4f53-bd53-037db0467af1"
width="400" alt="Run ScummVM_000"><img
src="https://github.com/OnionUI/Onion/assets/47260768/86848e29-a304-4c9e-ae1f-1c4d491d044a"
width="400" alt="Run ScummVM_001">

## To test

Testing downscaler:

- [x] Load a game engine that would natively run at 800x600 (sword25
with Broken Sword 2.5) - If it boots at all with a clear image DS is
working

Testing broken sword 2.5 fix for crash after menu (when intro video
starts):

- [x] As above, this killed the game after the main menu, if you make it
past the main menu you're good.

Testing GUI -> 640 x 480: 

- [x]  GUI can be freely scaled to its smallest size

Testing scrollbars:

- [x] Open global options -> Keymaps & observe a scrollbar is now
present.

## Build details
<details>

```markdown

Backend... miyoo (SDL 1.2.15), 16bit color, high resolution, TinyGL, savegame timestamp, HQ and Edge scalers, aspect ratio correction, Lua, virtual keyboard
WARNING: Disabling engine Hpl1 because the following dependencies are unmet: OpenGL with shaders
WARNING: Disabling engine Tetraedge because the following dependencies are unmet: libtheoradec

Engines (builtin):
    SCUMM [all games]
    Access
    ADL
    AGI
    AGOS [all games]
    Adventure Game Studio
    Sanitarium
    Lord Avalot d'Argent
    Beavis and Butthead in Virtual Stupidity
    Blade Runner
    The Journeyman Project 2: Buried in Time
    CGE
    CGE2
    Chewy: Esc from F5
    Cinematique evo 1
    Magic Composer
    Cinematique evo 2
    Lost Eden
    Cryo Omni3D games [all games]
    Macromedia Director
    Dungeon Master
    Dragon History
    Blazing Dragons
    Drascula: The Vampire Strikes Back
    Dreamweb
    Freescape
    Glk Interactive Fiction games
    UFOs
    Gobli*ns
    The Griffon Legend
    Grim [all games]
    Groovie [all games]
    Hades Challenge
    Hyperspace Delivery Boy!
    Hopkins FBI
    Hugo Trilogy
    Hypnotix Inc.
    In Cold Blood
    Illusions Engine
    Kingdom: The Far Reaches
    Kyra [all games]
    Labyrinth of Time
    The Last Express
    Lilliput
    Lure of the Temptress
    MacVenture
    MADE
    MADS [all games]
    Mohawk [all games]
    Mortevielle
    mTropolis
    Mutation of JB
    Myst 3
    Nancy Drew
    Neverhood
    Nikita Game Interface
    Parallaction
    The Journeyman Project: Pegasus Prime
    Red Comrades
    Pink Panther
    Playground 3d: the testing and playground environment for 3d renderers
    Plumbers Don't Wear Ties
    The Prince and The Coward
    Private Eye
    Flight of the Amazon Queen
    SAGA [all games]
    SAGA2
    SCI [all games]
    The Lost Files of Sherlock Holmes
    Beneath a Steel Sky
    Sludge
    The Longest Journey
    Star Trek 25th Anniversary/Judgment Rites
    Mission Supernova
    Broken Sword
    Broken Sword II
    Broken Sword 2.5
    Teen Agent
    TestBed: the Testing framework
    Tinsel
    Starship Titanic
    3 Skulls of the Toltecs
    Tony Tough and the Night of Roasted Moths
    Toonstruck
    Touche: The Adventures of the Fifth Musketeer
    Trecision Adventure Module
    TsAGE
    Bud Tucker in Double Trouble
    Little Big Adventure
    Ultima
    Voyeur
    WAGE
    Wintermute [all games]
    World of Xeen
    Z-Vision

Engines Skipped:
    Hpl1
    Tetraedge

WARNING: This ScummVM build contains the following UNSTABLE engines:
    Lord Avalot d'Argent
    Lost Eden
    Dungeon Master
    Grim [Escape from Monkey Island]
    In Cold Blood
    Kingdom: The Far Reaches
    The Last Express
    Lilliput
    MacVenture
    MADS [MADS V2]
    Mohawk [Where in Time is Carmen Sandiego?]
    Mutation of JB
    Nancy Drew
    Playground 3d: the testing and playground environment for 3d renderers
    Sludge
    Star Trek 25th Anniversary/Judgment Rites
    TestBed: the Testing framework
    WAGE
    Wintermute [Wintermute3D]

```
</details>

---
## [jhiemstrawisc/pelican](https://github.com/jhiemstrawisc/pelican)@[bc56423c42...](https://github.com/jhiemstrawisc/pelican/commit/bc56423c4210dfa1e9a480bf5e449edd1acbc000)
#### Tuesday 2023-08-01 18:53:16 by Justin Hiemstra

Local lint & Director CLI hookup + bug fixes

PR #7 introduced a framework for including the Director in the Pelican CLI,
toward making all Pelican services available under a single binary. This commit
extends that PR to hook the Director package up to the CLI, the Pelican's
configuration mechanisms, and to actually sort out a few bugs related to the
untested director code.

It should be noted that there are currently a few hacks in the code that need
clearing up before any merge, but as of now the commit makes the following
possible:
`pelican director serve --cache-port 8000`
This will serve the Director's cache-redirection service on port 8000 using a gin
engine. When we've figured out how to handle Origin redirects and implemented an
origin-redirect service, we'll be able to do:
`pelican director serve --cache-port 8000 --origin-port 8001`
to split apart the two endpoints.

As for the local lint... I'm still trying to figure out how to shut that feature
off in my editor. Sorry for the noise!

---
## [Ua-Gi-Oh/UA_EDO](https://github.com/Ua-Gi-Oh/UA_EDO)@[a36ff60424...](https://github.com/Ua-Gi-Oh/UA_EDO/commit/a36ff604248abc504912de3ae13438545fa12ca9)
#### Tuesday 2023-08-01 19:04:12 by Ua-Gi-Oh

Перекладені карти

1 - Symbol of Friendship
2 - Spright Carrot
3 - Overdrive
4 - Dark Magic Attack
5 - Princess Curran
6 - Road Warrior
7 - Des Lacooda
8 - Tyr of the Nordic Champions
9 - Micro Coder
10 - Lovely Labrynth of the Silver Castle
11 - Great Long Nose
12 - Pendulum Area
13 - Light of Redemption
14 - Mayakashi Return
15 - Abyss Actor - Hyper Director
16 - Steel Shell
17 - Xyz Reflect
18 - Paleozoic Eldonia
19 - Neo Flamvell Hedgehog
20 - Ojamassimilation

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[892dc23ef8...](https://github.com/git-for-windows/git/commit/892dc23ef86dbd146b53c14d9ff481b0d0075c21)
#### Tuesday 2023-08-01 19:59:57 by Johannes Schindelin

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
## [StarStation13/Save-Our-Ship-test](https://github.com/StarStation13/Save-Our-Ship-test)@[0cff53fc09...](https://github.com/StarStation13/Save-Our-Ship-test/commit/0cff53fc09c34d989d2bc34b1699bd856af2cb92)
#### Tuesday 2023-08-01 20:01:19 by meemofcourse

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
## [StarStation13/Save-Our-Ship-test](https://github.com/StarStation13/Save-Our-Ship-test)@[d4b5a598e2...](https://github.com/StarStation13/Save-Our-Ship-test/commit/d4b5a598e2346bb3f69d533ed05a94d539e8b830)
#### Tuesday 2023-08-01 20:01:19 by Bjarl

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
## [Patient212/space-station-14](https://github.com/Patient212/space-station-14)@[31607a0be0...](https://github.com/Patient212/space-station-14/commit/31607a0be0e2ef24f4d53c7611172ec6d40a3a2b)
#### Tuesday 2023-08-01 20:42:12 by Emisse

hardsuit/firesuit cleanup (#18308)

* real

* hjoly fuck you guy sare annoying

* fix cargo arbitrage idk why tf it changed from editing armor values but fuck my life i guess

* why god

* Update suits.yml

* Update cargo_emergency.yml

---
## [shiptest-ss13/Shiptest](https://github.com/shiptest-ss13/Shiptest)@[ee4021c507...](https://github.com/shiptest-ss13/Shiptest/commit/ee4021c50792c11bfd21085156edd32200c21cb8)
#### Tuesday 2023-08-01 20:46:22 by Imaginos16

Destroying Sprite Cruft Part One: Cruft Sucks (#2220)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Title


![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/1cedcdb1-01b5-4f28-a759-65428c2dcd0a)

In total, the:

- IV Drip
- All-In-One Grinder
- Book Binder
- Book Scanner
- Water Cooler
- Tank Dispenser

Have all been successfully uncrufted. No more cruft. Just clean sprites
now :D

Oh and dressers have directionals now at the request of @Bjarl 

Credit goes to the original authors in the changelog.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
begone cruft I fucking hate cruft
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: PositiveEntropy, Maxymax13, Wallemations, Kryson,
Viro/Axietheaxolotl, MeyHaZah
imageadd: Books, IV drips, tank dispensers, all-in-one grinders, water
coolers, book binders and book scanners have been resprited!
imageadd: Dressers now have directionals!
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [dartmouth-outing-club/fyt-bus-packet-generator](https://github.com/dartmouth-outing-club/fyt-bus-packet-generator)@[3186cf6f75...](https://github.com/dartmouth-outing-club/fyt-bus-packet-generator/commit/3186cf6f75c59ae54e2bc13672b4cc5177d078d9)
#### Tuesday 2023-08-01 21:03:23 by Alexander Petros

Reference packets by ID

Enormous refactor to fix an extremely silly mistake I made when I
designed this app: referencing packets by name instead of ID. I
corrected this, and in the process set up the application so that it's
almost entirely template-based now, which is much nicer than the
JS-based HTML I was writing before. I don't hate my original
implementation, but I think this one is undeniably easier to understand
and maintain.

I still need to re-implement editing, which I expect will by annoying.

---
## [cooljeanius/termcwd-vim](https://github.com/cooljeanius/termcwd-vim)@[a91cda2a02...](https://github.com/cooljeanius/termcwd-vim/commit/a91cda2a02c77e4399b589dee5f6f0a1ae87b111)
#### Tuesday 2023-08-01 22:51:33 by Lawrence Velázquez

Convert indentation from spaces to tabs

I've long favored four-space indentation but find Matt Wilcox's pro-tab
counterargument [1][2] compelling, if needlessly condescending:

    This is your occasional reminder:
    Tabs are what should be used for indentation.

    Why?  Because spaces for indentation are:

    - Harder for people using assistive technology
    - Harder for people with reading comprehension issues who want more
      indentation.

    The tab is *user customisable* to be any level of indentation per
    tab character.  It is the semantically correct character.

    Please; use tab characters in any public code.  If you don't like
    how "deep" they are; adjust your editor's rendering.

    (If you are already cringing or railing against this idea because it
    would look weird to you... have a deep think.  A real deep think.)

    Spaces as indentation are self-centred and selfish.  They enforce
    *your* preference on others, when tabs would allow you *and others*
    their own preference of indentation for the same code - because they
    are user configurable.

    Yes, all editors can configure the tab to render as 1, 2, 4, 6, 8 or
    any number of spaces wide.  Learn your editor.

I've always prioritized my aesthetic preferences, deeming indentation of
two columns to be too shallow and eight, too deep.  I know tab stops are
widely configurable, but I stubbornly insist on viewing tabs at their
"natural" width of eight columns because I want to see them as everyone
else does.  (Who actually changes their tab stops?  Come on.)  Thus, the
only way to get al dente indentation that looks the same to everyone is
to use four spaces.

I've thought about switching to tabs before.  The Linux kernel coding
style guide espouses 8-column indentation on the grounds that it's very
clear and highlights excessively deep nesting [3] -- interesting ideas,
but not so interesting that I'd switch teams.

Well, Wilcox's accessibility angle has convinced me, although I still
think 8 columns is a bit much.  I'll get over it.

Reindent Vim source using tabs.  Do not reindent prose because it looks
awful, and I can't bring myself to do it (code is already ugly, so it's
easier to swallow).

  [1]: https://mstdn.social/@mattwilcox/110451855256437660
  [2]: https://mstdn.social/@mattwilcox/110451875354616267
  [3]: https://www.kernel.org/doc/html/latest/process/coding-style.html#indentation

---
## [OliOliOnsiPree/sunset-wasteland](https://github.com/OliOliOnsiPree/sunset-wasteland)@[1f15689fe0...](https://github.com/OliOliOnsiPree/sunset-wasteland/commit/1f15689fe0eeb42ab1a80e863177732920065d3e)
#### Tuesday 2023-08-01 23:01:05 by ProbablyCarl

Demolitions & Rockets
- - -
Balance:
 - Mech rockets corrected. They weren't meant to be firing HE. Whoops.
 - Legion Demolitions given a proper explosive grenade.
   - HE given to Demolitions has also been made a crafting option.
 - Enclave roles with grenades given the appropriate F13 item.
 - Brotherhood has lost access to the L30, alongside the tribeam. The latter because it was a redundant choice and sandwiched between two far superior options.
- - -
Map:
 - Heaven's Night and general Pahrump modifications in line with internal discussions.
- - -

---
## [EchterAlsFake/Porn_Fetch](https://github.com/EchterAlsFake/Porn_Fetch)@[eecfbef6a7...](https://github.com/EchterAlsFake/Porn_Fetch/commit/eecfbef6a744836222673f116a860a454cfc859e)
#### Tuesday 2023-08-01 23:11:06 by Johannes Habel

Removed support for Apple devices, because I realized that you need to spend FUCKING 2000€ to get some stupid devices that even don't support sideloading lmao.

And NO I can't run it in a virtual machine.

(I know there's always a way, but I don't want to spend a whole day to get a shady macOS version running and then spend another week to learn macOS)

Hyprland > macOS : Facts.

(iOS maybe get support, because I have a friend with an iOS device, and I am really close to him, but he doesn't do anything like programming. I don't know if he wants to install a "hacker tool (lmao)" like iSH.  (You hopefully get the joke ;))

---
## [timothymtorres/tgstation](https://github.com/timothymtorres/tgstation)@[74892ae7ec...](https://github.com/timothymtorres/tgstation/commit/74892ae7ec80d47c64bf786f62985a1bd07d06f7)
#### Tuesday 2023-08-01 23:21:50 by LemonInTheDark

Optimization pass focused on foam code (saves about 30% of cpu usage I think) (#76104)

## About The Pull Request

Foam is crummy at high load rn, both because it runs on a low priority
background subsystem, and because it wastes a bit of time.
Let's reduce usage (while speeding up a bunch of other stuff too), and
give it more cpu generally.

[Optimizes reagent processing
somewhat](https://github.com/tgstation/tgstation/commit/d409bd4afc3c208cd6f00ff406e1e9f78d5ac5ad)

Turns out most of the cost of foam is the reagents it carries, and the
varying effects they have
I'm doing my best here to optimize them without touching "user space"
too much

That means doing things like prechecking if we're gonna spawn on top of
an existing decal (from glitter, flour, etc), and using that same proc
to also avoid spawning on unacceptable turfs (I had to convert
inheritance to a bitflag system to make this work, but I think that's ok
since we want it imparative anyhow)

It's actually nice for code quality too, since it lets me clean up code
that was using raw locates and weird var pong.
god I wish I had implied types man

[Optimizes foam spreading in its most accursed aspect, reagent
copying](https://github.com/tgstation/tgstation/commit/5cc56a64ad1a22ba7467cb0446b9558560259437)

Holy shit reagent code is a lot.

I'm doing a bunch of small things here. istype in init -> typecache,
removing procs that are called once and loop over a list we JUST looped
over (ph and the caching for reactions in particular)

I am mainly trying to optimize copy_to here, since that's what foam
spams
As a part of this, I removed a pair of update_total and handle_reactions
calls that were done on the reagents we are copying FROM

I have no god damn idea why you would want to do that, but if anything
is relying on the copy proc modifying the source, then that code
deserves to break

Speaking of, I cleaned up handle_reaction's main filter loop a lot,
removed a lot of redundant vars and changed it from a full loop w
tracker vars to an early exit pattern

This meant using a loop label, which is unfortunate, but this is the
fastest method, and it does end up cleaning up the code significantly,
Which is nice

Oh also I made the required_other var function even if there is no atom
attached to the reaction, since I don't see why it wouldn't

This last bit is gonna get a bit esoteric so bear with me

Failing calls (which are most of them) to handle_reactions are going to
be fastest if they need to check as few reactions as possible

One reagent in a reaction's required list is marked as the "primary",
and thus gets to trigger checking it.
We need all the reagents to react anyhow, so we might as well only check
if we have one particular one to avoid double checking

Anyhow, in order to make most calls the fastest, we want these reactions
distributed as evenly as possible across all our reagents.
The current way of doing this is just taking the first reagent in the
requirements list and using it, which is not ideal

Instead of that, lets figure out how many reactions each reagent is in,
then divy reactions up based off that and the currently divvied
reactions

This doubles the reagent index count, and takes the most common reagent,
water, from 67 reactions to I think like 22

Does some other general cleaning in reagent code too, etc etc etc

[Fixes runtimes from the forced gravity element being applied more then
once](https://github.com/tgstation/tgstation/commit/941d0676114fd455a585f2c65ffc79b81e8438b7)

I feel like this element should take a trait source or something to make
them potentially unique, it's too easy to accidentally override one with
another

[Removes connect_loc usage in atmos_sensitive, replaces it with direct
reg/unreg](https://github.com/tgstation/tgstation/commit/de1c76029d5c49dff152f0ea168b9e6c4a4a04aa)

I only really used it because I liked the componentization, but it costs
like 0.2 seconds off init alone which is really stupid, so let's just do
this the very slightly harder way

[Micros foam code slightly by inlining a LinkBlockedWithAccess
call](https://github.com/tgstation/tgstation/commit/744da3694cd4a85b3bdf44d754de57d7570bdd1c)

This is in the space of like 0.05 seconds kinda save so I can put it
back if you'd like, the double loop just felt silly

[Changes how foam processes
slightly](https://github.com/tgstation/tgstation/commit/ee5e633e3256fe7df229af71d78424d502459c16)

Rather then treating spreading and processing as separate actions, we do
both in sync.
This makes foam fade faster when spreading, which is good cause the
whole spread but unclearing foam thing looks silly.
It also avoids the potential bad ending of foam spreading into itself,
backwards and forwards. This is better I promise.

[Bumps fluid priority closer to heavy eaters, moves it off
background](https://github.com/tgstation/tgstation/commit/811797f09db7b060f75f15ad06d0ce8982375f47)

Also fixes a bug where foam would travel under public access airlocks.

## Why It's Good For The Game

Saves a lot of cpu just in general, from both init and live.
In theory makes foam faster, tho I'd have to test that on live at
highpop to see if I've actually succeeded or not. Guess we'll see.

---
## [timothymtorres/tgstation](https://github.com/timothymtorres/tgstation)@[063bf74f31...](https://github.com/timothymtorres/tgstation/commit/063bf74f31a27ec8096fe10b844d5883be6d13a9)
#### Tuesday 2023-08-01 23:21:50 by carlarctg

There is no longer a 50% chance of catching a heretic out when examining them drawing influences (#76878)

## About The Pull Request

There is no longer a 50% chance of catching a heretic out when examining
them drawing influences.

## Why It's Good For The Game

> There is no longer a 50% chance of catching a heretic out when
examining them drawing influences

This is a bad thing for several reasons.

1. It means the heretic will most often be caught out at the very start
of the shift, when they are weakest and most vulnerable.
Heretics already have it hard enough, adding yet another source of
stress is undue.

2. It has no effective counter.
What are you going to do? Not draw any influences? That shouldn't be the
'counter'. The influence drawing period is meant to parallel the crew
prepping period, the traitor rep-collecting period, etc.

3. In a way, it's more blatant than Codex Cicatrix drawing.
Codexi show up as a normal item in your hand. This instead shows a huge
flashing glowing neon rainbow text that says THIS IS A HERETIC. SHRIEK
IN RADIO AND VALID.

4. It's badly designed, and can be manipulated way too easily to always
show.
Examine a target thrice and you're pretty much guaranteed to see if they
are indeed drawing or not. You can just keep rolling the 50% chance.

5. It feels random and unfair for the heretic to die to it.
I've seen this happen and it sucks. There's no sign for heretics that
they have a risk of being found out when examined, which means that this
is just an extremely rare occurrence that you try to ignore *could*
happen 99% of the time, and feel like shit the 1% of the time it
backfires.

## Changelog

:cl:
del: There is no longer a 50% chance of catching a heretic out when
examining them drawing influences.
/:cl:

---
## [ubicloud/ubicloud](https://github.com/ubicloud/ubicloud)@[e683ea8403...](https://github.com/ubicloud/ubicloud/commit/e683ea8403dcd01d0f996e2d41456541f8832500)
#### Tuesday 2023-08-01 23:37:44 by Daniel Farina

Switch product names to standard-(cores*2) notation

Why cores * 2? Because SMT features, as seen on Intel and AMD products
for some year now make this equal to the number of "CPUs" or "vCPUs"
when exposed to the guest operating system.

The theory is that an integer in the product code will be compared to
vCPU references similar products on various data tables and so forth
on The Internet, or more to the point, shouldn't be a smaller integer
than those references for the same hardware.  Note, I do not subscribe
to this theory personally, so don't ask me about it.

The ugliness arrives when we consider SMT-off configurations or
relatively recent addition of ARM processors that do not implement
SMT.  If the product scale factor was taken to describe vCPUs, we'd
end up the situation that GCP and Azure are in: t2d.standard-1 is a
one vCPU in SMT-off configuration, and thus a single core, and so is
n2d.standard-2, and these are otherwise the most comparable products.

Azure did something rather strange to deal with this, where a
"Standard_E2" is 2 vCPUs on one core via SMT and 16 gigabytes of
memory, but "Standard_E2p" on ARM is 2 cores and 16 gigabytes of
memory, a more compute-rich ratio by quite a bit.

One solution, absent indexing the product by cores directly, which
produces an integer that could be misconstrued and deemed too small,
is to double the core number in all circumstances.  The idea of a
popular architecture with three or more threads per core seems
unlikely at this point, and in any case it'd be an emergent
architecture where we could be forgiven for an awkward numbering
system.  And it solves the problem for allowing someone to scan
laterally from "standard-2" and a hypothetical "standard-2-arm".  Even
if standard-2-arm has a single core.

Of course, there's nothing stopping us from deciding to really make
the product scale factor relate to vCPUs, that is, to have integers of
larger magnitudes for architectures with SMT, and maybe if people do
prove to be uniformly alert about SMT and find `standard-2-arm`
misleading, we can elect to do things that way.

---
## [ubicloud/ubicloud](https://github.com/ubicloud/ubicloud)@[5acee7309f...](https://github.com/ubicloud/ubicloud/commit/5acee7309fd7f87fa299544cc22f7066511f898b)
#### Tuesday 2023-08-01 23:41:20 by Daniel Farina

Switch product names to standard-(cores*2) notation

Why cores * 2? Because SMT features, as seen on Intel and AMD products
for some year now make this equal to the number of "CPUs" or "vCPUs"
when exposed to the guest operating system.

The theory is that an integer in the product code will be compared to
vCPU references similar products on various data tables and so forth
on The Internet, or more to the point, shouldn't be a smaller integer
than those references for the same hardware.  Note, I do not subscribe
to theory's assigned magnitude of this, and have my objections to what
it does to the cogency of product comparison as written below, but
nonetheless, I've written this operating under this theory.

The ugliness arrives when we consider SMT-off configurations or
relatively recent addition of ARM processors that do not implement
SMT.  If the product scale factor was taken to describe vCPUs, we'd
end up the situation that GCP and Azure are in: t2d.standard-1 is a
one vCPU in SMT-off configuration, and thus a single core, and so is
n2d.standard-2, and these are otherwise the most comparable products.

Azure did something rather strange to deal with this, where a
"Standard_E2" is 2 vCPUs on one core via SMT and 16 gigabytes of
memory, but "Standard_E2p" on ARM is 2 cores and 16 gigabytes of
memory, a more compute-rich ratio by quite a bit.

One solution, absent indexing the product by cores directly, which
produces an integer that could be misconstrued and deemed too small,
is to double the core number in all circumstances.  The idea of a
popular architecture with three or more threads per core seems
unlikely at this point, and in any case it'd be an emergent
architecture where we could be forgiven for an awkward numbering
system.  And it solves the problem for allowing someone to scan
laterally from "standard-2" and a hypothetical "standard-2-arm".  Even
if standard-2-arm has a single core.

Of course, there's nothing stopping us from deciding to really make
the product scale factor relate to vCPUs, that is, to have integers of
larger magnitudes for architectures with SMT, and maybe if people do
prove to be uniformly alert about SMT and find `standard-2-arm`
misleading, we can elect to do things that way.

---

