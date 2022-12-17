## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-12-16](docs/good-messages/2022/2022-12-16.md)


2,037,679 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,037,679 were push events containing 3,066,643 commit messages that amount to 245,918,771 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 52 messages:


## [copperdogma/mtgen](https://github.com/copperdogma/mtgen)@[d294ef990b...](https://github.com/copperdogma/mtgen/commit/d294ef990ba74f48ad43d9f59423202eb40807ea)
#### Friday 2022-12-16 00:17:22 by Cam Marsollier

Upgraded project to .NET6 (and VS 2022 for Mac)

This was part of a WHOLE thing where Azure exploded on me and wouldn't let me publish, so I spent half a day hacking at it to get it to work. I've been meaning to upgrade to VS2022 for awhile now and I think? it may have helped fixed the issue.

Regardless, I'm not on a stupid expensive Azure hosting plan because I think the whole issue was (mostly) out of disk space.

I'm sick of Azure. I'm trying to run a tinker toy in a nuclear submarine. I'm rewriting this puppy (yes, all six lines of actual code) in node.js and moving it to my DreamHost hosting plan where it will cost me exactly zero to host.

---
## [GuillaumePrata/tgstation](https://github.com/GuillaumePrata/tgstation)@[4fd404aa8f...](https://github.com/GuillaumePrata/tgstation/commit/4fd404aa8f15480ad4c8585e65268a83c60b26e1)
#### Friday 2022-12-16 00:44:23 by tralezab

Moves speaking verbs to tongues + subtypes, moves wing sprites to wing subtypes, bodypart damage examines to limbs, fixes sign language not working without a tongue (#71635)

## About The Pull Request

### Moves speaking verbs to tongues + subtypes
Moves species say mod onto tongues, creates any tongues that didn't
exist for the say mods they needed to hold.

### moves wing sprites to wing subtypes
Moves the logic of selecting a wing sprite onto subtypes of /functional
on the wing type. Now, angel wings bring the holy trait with them, it
isn't a special check on flight potions, and we can expand it. (EMPs
taking down robowings? Fires burning megamoth wings? Cool stuff)

### bodypart damage examines to limbs
Instead of checking what your species says, it tallies up your limbs and
provides the damage description that matches most of your limbs. So for
example, If you're mostly human with one augmented part, you take
bruises and cuts. If you're mostly robot augmented with one human part,
you get robot damage descriptions. Yay!

### fixes sign language working without a tongue
Having no tongue would garble your speech, and this had no interaction
with sign language, so you'd be speaking in broken gurgling with
perfectly working hands. Now, the sign language component prevents any
kind of garbling, since it brings its own garbling for full/missing arms


![image](https://user-images.githubusercontent.com/40974010/204932511-42c8e020-a2d7-4fc1-befc-7cd46a2f2932.png)

## Why It's Good For The Game

Moving things off of species inherent makes the game expose way more
interesting mechanics to play with. It sucks that you can't steal a
jellyperson's chirping, since they can get a normal tongue and they'll
go back to... chirping! LAME! THAT IS LAME!

Ditto goes for wings, and for limbs, well, having someone be entirely
augmented but get descriptions of bleeding because they didn't spawn as
an android is kinda lame.

<details>
  <summary>Spoiler warning</summary>
  

![image](https://user-images.githubusercontent.com/40974010/204922627-333de052-a02b-4786-8ff9-f6e739443f2c.png)
  
</details>



## Changelog
:cl:
refactor: Refactored wings, tongues, and some examine messages,
hopefully with minimal effect on actual changes. A few more species have
tongues, angel wings bring the holy trait with them, and wings have new
descriptions. should be the biggest parts of it
/:cl:

---
## [GuillaumePrata/tgstation](https://github.com/GuillaumePrata/tgstation)@[9499a1542b...](https://github.com/GuillaumePrata/tgstation/commit/9499a1542b156eb32efb25e0310b1fe7077caf5c)
#### Friday 2022-12-16 00:44:23 by itseasytosee

Corrects error in stamina HUD element display calculation. Increases stamina HUD readability. (#71623)

## About The Pull Request
Stamina was checking health instead of maxHealth. This is probably a
remnant from when the damage stacked.
I stopped the stamina from appearing like you had no stamina whenever
you were stunned or knockdown. This would obscure potentially value
information from the player while being unclear to interpret.
We should probably represent status effects like this to the player, but
through the stamina bar is not a useful method.
The stamina bar is for stamina.
Additionally, the stamina bar will now be greyed out while you are dead,
like your health bar.

I've done alot of work increasing the readability of the stamina bar.
Firstly, I've cut some fat, removing the 100% sign when you are at full
and the blinking exclamation point when you are close to zero. They
aren't nessisary and add clutter.
There's no more "full but because its blinking bright yellow you are
actually at 20% or less" or "empty but because the whole thing isn't
blinking you still have stamina"
Its a now simple meter that decreases in 20% increments which blinks
softly, at darker and more red colors the lower the meter goes, blinking
faster at the higher percentages. When you are at zero, the empty space
slowly glows a dark red.
Its much more reasonable and intuitive than whatever the hell the old
sprites were doing.
## Why It's Good For The Game
For the HUD changes, it improves the game feel, at least from my
experience. We could probably benefit from an entirely new stamina bar
design, but finding the right one is gonna be tricky.
## Changelog
:cl: itseasytosee
fix: Stamina damage display calculation should be much more sane and
reliable now
imageadd: Simplified the stamina hud
/:cl:

---
## [GuillaumePrata/tgstation](https://github.com/GuillaumePrata/tgstation)@[2425531eb2...](https://github.com/GuillaumePrata/tgstation/commit/2425531eb2dab84fb27ed864e4c52470bfff6918)
#### Friday 2022-12-16 00:44:23 by John Willard

Removes tablets (not PDAs) entirely. (#71507)

## About The Pull Request

**Comes with an UpdatePaths!**

Removes the tablet subtype, PDAs now replaces them entirely.

Nukie and Silicon tablets are now subtypes of the PDA instead, while
contractor ones were removed entirely as they didn't do anything and
were unused (though it wouldn't be hard to re-add).

Nukie PDAs are now the only type of PDA that uses modular_tablets.dmi,
which is just larger icons of modular_pda. Each application requires an
icon state in both of these, for 2 different sizes, which makes it
annoying to make new applications, especially if it can also run on
computers/laptops.

### Icons

Because Silicon tablets are now a subtype of PDA, they use PDA icons
instead of tablet ones. Luckily for us, they already exist in code.

![image](https://user-images.githubusercontent.com/53777086/203876575-56eb1593-774c-47c6-8e7d-491a7805f28c.png)

AI's don't use a tablet icon though, so they aren't affected.

## Why It's Good For The Game

There's very little difference between tablets and PDAs, PDAs overshadow
them in every single way, so at this point I don't see why we should
have both of these, and if you compare the two in usefulness and actual
in-game use by players, it's a no-brainer than the item all players get
roundstart and comes with a messenger should be the one we go with.

Also as said in the about section, when making an app you would need to
make icon states for the program running for all hardware it can run on,
which is Computer, Laptop, PDA, and Tablet.

Laptop is just a smaller computer icon
PDA is just a smaller tablet icon

However, you can't simply shrink the size of the icon, instead you have
to completely resprite the same app icon FOUR TIMES for it to not
bluescreen on all these different devices.

<details>
<summary>
Here's examples of it
</summary>
Computer (NOTE: *They share the same icon file as regular computers*)
<img
src="https://user-images.githubusercontent.com/53777086/203876801-486a8054-489a-4983-bdad-a2599b4dc379.png"/>
Laptop
<img
src="https://user-images.githubusercontent.com/53777086/203876333-58e5d135-f4c6-4a02-8948-1df771e294a4.png"/>
Tablet
<img
src="https://user-images.githubusercontent.com/53777086/203876352-816c7fb1-c681-40b9-99e0-052f49632c7f.png"/>
PDA
<img
src="https://user-images.githubusercontent.com/53777086/203876358-1cf7253d-3c6a-456a-8133-ebf7f0351637.png"/>
</details>

If we wish to help in simplifying this, we should remove tablet icons
entirely, which means 1 less icon to worry about. To do this, we'd need
to resprite nukie PDAs, however I am very much not a spriter and never
tried GAGS, so I'll leave it to someone else to do.

## Changelog

:cl:
del: Tablets are now removed, PDAs are now the base 'tablet'. Silicon
and nukie tablets are now PDAs.
/:cl:

---
## [flowercuco/blorbostation](https://github.com/flowercuco/blorbostation)@[a9fda932e2...](https://github.com/flowercuco/blorbostation/commit/a9fda932e2a9d8cf20f5f74fdcbdbcca86d580e6)
#### Friday 2022-12-16 01:20:34 by Tim

Drinking singulo ignores supermatter hallucinations and pulls nearby objects (#71927)

## About The Pull Request
Drinking a singulo will now:

- Give immunity to supermatter hallucinations
- Pulls objects to you based on the total volume in your system (20u =
1x1, 45u = 2x2, 80u = 3x3)
- Makes a burp and supermatter rays/sound when objects are pulled

The new ingredient is:

- Vokda 5u 
- Wine 5u
- Liquid Dark Matter 1u (replaces Radium)

## Why It's Good For The Game
More cool effects for drinks. Singularity is all about gravity and the
drink should have a theme around that.


![dreamseeker_2q21YXS698](https://user-images.githubusercontent.com/5195984/207297517-90d26395-dd30-4106-bdd4-b30b1ba3e20b.gif)

## Changelog
:cl:
add: Drinking singulo will now ignore supermatter hallucinations and
pull objects to you
balance: Change singulo drink recipe to require liquid dark matter
instead of radium.
/:cl:

---
## [brucerennie/NetHack](https://github.com/brucerennie/NetHack)@[b2fe51490d...](https://github.com/brucerennie/NetHack/commit/b2fe51490dac43cac70ec29c6958467b0fa9bdd4)
#### Friday 2022-12-16 01:30:35 by PatR

tty-style role selection for curses

Move the tty role/race/&c selection from wintty.c to role.c and remove
its references to BASE_WINDOW.  Have curses call the same routine now
so that the player has the option to choose role, race, gender, and
alignment in any order and to confirm or override random settings
prior to starting play.  Also if you went through "who are you?" then
final confirmation includes an extra menu choice to rename the hero.

It still has the quirk of sometimes remembering some of the previous
aspects when you re-pick a new value for some aspect which already
been selected.

The menus pop up on top of the copyright screen and that looks a bit
strange.  I don't think core code has any way to erase that base
window without erasing the entire screen so to fix the strangeness
the window ports would need to do that before calling the selection
routine.  I didn't do that because the very first prompt, "Shall I
pick ... for you? [ynaq]" shows up in that window rather than in a
popup over it, and having it be all by itself on an otherwise blank
screen seemed to be even stranger.

X11 and Qt both have more sophisticated selection routines so I
haven't tried to switch either of them to use this.  They both use a
fancy role-selection-specific menu with all the aspects present at
once so this wouldn't fit without more work than I care to tackle.

---
## [JokoLG/Auto-Jeep](https://github.com/JokoLG/Auto-Jeep)@[1a0dab5ff1...](https://github.com/JokoLG/Auto-Jeep/commit/1a0dab5ff1054255c0364d1e14799f3ea90cfcee)
#### Friday 2022-12-16 02:16:34 by JokoLG

GUI Stuff Updated

holy shit making uis in python is horrible because of no indentations, try to read this fucking code without having a stroke holy shit

---
## [Sea-of-Lost-Souls/Tannhauser-Gate](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate)@[b476bce004...](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate/commit/b476bce004f741ccd2fd69526292b5cd1fa4d4c9)
#### Friday 2022-12-16 02:33:14 by SkyratBot

[MIRROR] Fishing-themed Escape Shuttle [MDB IGNORE] (#18113)

* Fishing-themed Escape Shuttle (#71805)

## About The Pull Request

I can't do much coding until you review my other PRs so I'm making a
mapping PR instead.
I actually made this a while ago while I was trying out strongDMM. It
turns out: it's a good tool and easy to use.

![2022 12 09-10 51
26](https://user-images.githubusercontent.com/7483112/206686234-ae952ba3-2cb4-4093-80a0-d086fe95a3fc.png)

This mid-tier shuttle isn't enormous and is shaped like a fish. It
dedicates much of its internal space to an artificial fishing
environment, plus fishing equipment storage. Plus look at that lovely
wood panelling!
There's not a lot of seating or a large medbay, but there's five fishing
rods for people to wrestle each other over plus some aquariums to store
your catches in.

It contains a variety of fishing biomes (ocean, moisture trap, hole,
portal) but I couldn't fit "lava" in there even though I wanted to
because it's hardcoded to only have fish in it on the mining z-level.
If you're very lucky and nobody shoves you, the time between the shuttle
docking at the station and arriving at Centcomm might be enough time for
you to catch maybe four entire fish. Wow!

## Why It's Good For The Game

There are plenty of novelty shuttle options but I think this one is good
for a personal touch of "the Captain would rather be fishing than
hearing you complain about the nuclear operatives".

## Changelog

:cl:
add: Tell your crew how much you care by ordering a shuttle where half
of the seats have been removed so that you can get some angling done
before you clock out.
/:cl:

* Fishing-themed Escape Shuttle

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [dalance/cargo](https://github.com/dalance/cargo)@[6a4d98d232...](https://github.com/dalance/cargo/commit/6a4d98d2327124ca52bb9f67d6ad0097eb6b2e65)
#### Friday 2022-12-16 02:56:12 by bors

Auto merge of #10472 - epage:add, r=ehuss

feat: Import cargo-add into cargo

### Motivation

The reasons I'm aware of are:
- Large interest, see #5586
- Make it easier to add a dependency when you don't care about the version (instead of having to find it or just using the major version if thats all you remember)
- Provide a guided experience, including
  - Catch or prevent errors earlier in the process
  - Bring the Manifest format documentation into the terminal via `cargo add --help`
  - Using `version` and `path` for `dependencies` but `path` only for `dev-dependencies` (see crate-ci/cargo-release#288 which led to killercup/cargo-edit#480)

### Drawbacks

1. This is another area of consideration for new RFCs, like rust-lang/rfcs#3143 (this PR supports it) or rust-lang/rfcs#2906 (implementing it will require updating `cargo-add`)

2. This is a high UX feature that will draw a lot of attention (ie Issue influx)

e.g.
- killercup/cargo-edit#521
- killercup/cargo-edit#126
- killercup/cargo-edit#217

We've tried to reduce the UX influx by focusing the scope to preserving semantic information (custom sort order, comments, etc) but being opinionated on syntax (style of strings, etc)

### Behavior

Help output
<details>

```console
$ cargo run -- add --help
cargo-add                                                                                                                                  [4/4594]
Add dependencies to a Cargo.toml manifest file

USAGE:
    cargo add [OPTIONS] <DEP>[`@<VERSION>]` ...
    cargo add [OPTIONS] --path <PATH> ...
    cargo add [OPTIONS] --git <URL> ...

ARGS:
    <DEP_ID>...    Reference to a package to add as a dependency

OPTIONS:
        --no-default-features     Disable the default features
        --default-features        Re-enable the default features
    -F, --features <FEATURES>     Space-separated list of features to add
        --optional                Mark the dependency as optional
    -v, --verbose                 Use verbose output (-vv very verbose/build.rs output)
        --no-optional             Mark the dependency as required
        --color <WHEN>            Coloring: auto, always, never
        --rename <NAME>           Rename the dependency
        --frozen                  Require Cargo.lock and cache are up to date
        --manifest-path <PATH>    Path to Cargo.toml
        --locked                  Require Cargo.lock is up to date
    -p, --package <SPEC>          Package to modify
        --offline                 Run without accessing the network
        --config <KEY=VALUE>      Override a configuration value (unstable)
    -q, --quiet                   Do not print cargo log messages
        --dry-run                 Don't actually write the manifest
    -Z <FLAG>                     Unstable (nightly-only) flags to Cargo, see 'cargo -Z help' for
                                  details
    -h, --help                    Print help information

SOURCE:
        --path <PATH>        Filesystem path to local crate to add
        --git <URI>          Git repository location
        --branch <BRANCH>    Git branch to download the crate from
        --tag <TAG>          Git tag to download the crate from
        --rev <REV>          Git reference to download the crate from
        --registry <NAME>    Package registry for this dependency

SECTION:
        --dev                Add as development dependency
        --build              Add as build dependency
        --target <TARGET>    Add as dependency to the given target platform

EXAMPLES:
  $ cargo add regex --build
  $ cargo add trycmd --dev
  $ cargo add --path ./crate/parser/
  $ cargo add serde serde_json -F serde/derive
```

</details>

Example commands
```rust
cargo add regex
cargo add regex serde
cargo add regex@1
cargo add regex@~1.0
cargo add --path ../dependency
```
For an exhaustive set of examples, see [tests](https://github.com/killercup/cargo-edit/blob/merge-add/crates/cargo-add/tests/testsuite/cargo_add.rs) and associated snapshots

Particular points
- Effectively there are two modes
  - Fill in any relevant field for one package
  - Add multiple packages, erroring for fields that are package-specific (`--rename`)
  - Note that `--git` and `--path` only accept multiple packages from that one source
- We infer if the `dependencies` table is sorted and preserve that sorting when adding a new dependency
- Adding a workspace dependency
  - dev-dependencies always use path
  - all other dependencies use version + path
- Behavior is idempotent, allowing you to run `cargo add serde serde_json -F serde/derive` safely if you already had a dependency on `serde` but without `serde_json`
- When a registry dependency's version req is unspecified, we'll first reuse the version req from another dependency section in the manifest.  If that doesn't exist, we'll use the latest version in the registry as the version req

### Additional decisions

Accepting the proposed `cargo-add` as-is assumes the acceptance of the following:
- Add the `-F` short-hand for `--features` to all relevant cargo commands
- Support ``@`` in pkgids in other commands where we accept `:`
- Add support for `<name>`@<version>`` in more commands, like `cargo yank` and `cargo install`

### Alternatives

- Use `:` instead of ``@`` for versions
- Flags like `--features`, `--optional`, `--no-default-features` would be position-sensitive, ie they would only apply to the crate immediate preceding them
  - This removes the dual-mode nature of the command and remove the need for the `+feature` syntax (`cargo add serde -F derive serde_json`)
  - There was concern over the rarity of position-sensitive flags in CLIs for adopting it here
- Support a `--sort` flag to sort the dependencies (existed previously)
  - To keep the scope small, we didn't want general manifest editing capabilities
- `--upgrade <POLICY>` flag to choose constraint (existed previously)
  - The flag was confusing as-is and we feel we should instead encourage people towards `^`
- `--allow-prerelease` so a `cargo add clap` can choose among pre-releases as well
  - We felt the pre-release story is too weak in cargo-generally atm for making it first class in `cargo-add`
- Offer `cargo add serde +derive serde_json` as a shorthand
- Infer path from a positional argument

### Prior Art

- *(Python)* [poetry add](https://python-poetry.org/docs/cli/#add)
  - `git+` is needed for inferring git dependencies, no separate  `--git` flags
  - git branch is specified via a URL fragment, instead of a `--branch`
- *(Javascript)* [yarn add](https://yarnpkg.com/cli/add)
  - `name@data` where data can be version, git (with fragment for branch), etc
  - `-E` / `--exact`, `-T` / `--tilde`, `-C` / `--caret` to control version requirement operator instead of `--upgrade <policy>` (also controlled through `defaultSemverRangePrefix` in config)
  - `--cached` for using the lock file (killercup/cargo-edit#41)
  - In addition to `--dev`, it has `--prefer-dev` which will only add the dependency if it doesn't already exist in `dependencies` as well as `dev-dependencies`
  - `--mode update-lockfile` will ensure the lock file gets updated as well
- *(Javascript)* [pnpm-add](https://pnpm.io/cli/add)
- *(Javascript)* npm doesn't have a native solution
  - Specify version with ``@<version>``
  - Also overloads `<name>[`@<version>]`` with path and repo
    - Supports a git host-specific protocol for shorthand, like `github:user/repo`
    - Uses fragment for git ref, seems to have some kind of special semver syntax for tags?
  - Only supports `--save-exact` / `-E` for operators outside of the default
- *(Go)* [go get](https://go.dev/ref/mod#go-get)
  - Specify version with ``@<version>``
  - Remove dependency with ``@none``
- *(Haskell)* stack doesn't seem to have a native solution
- *(Julia)* [pkg Add](https://docs.julialang.org/en/v1/stdlib/Pkg/)
- *(Ruby)* [bundle add](https://bundler.io/v2.2/man/bundle-add.1.html)
  - Uses `--version` / `-v` instead of `--vers` (we use `--vers` because of `--version` / `-V`)
  - `--source` instead of `path` (`path` correlates to manifest field)
  - Uses `--git` / `--branch` like `cargo-add`
- *(Dart)* [pub add](https://dart.dev/tools/pub/cmd/pub-add)
  - Uses `--git-url` instead of `--git`
  - Uses `--git-ref` instead of `--branch`, `--tag`, `--rev`

### Future Possibilities

- Update lock file accordingly
- Exploring the idea of a [`--local` flag](https://github.com/killercup/cargo-edit/issues/590)
- Take the MSRV into account when automatically creating version req (https://github.com/killercup/cargo-edit/issues/587)
- Integrate rustsec to report advisories on new dependencies (https://github.com/killercup/cargo-edit/issues/512)
- Integrate with licensing to report license, block add, etc (e.g. https://github.com/killercup/cargo-edit/issues/386)
- Pull version from lock file (https://github.com/killercup/cargo-edit/issues/41)
- Exploring if any vendoring integration would be beneficial (currently errors)
- Upstream `cargo-rm` (#10520), `cargo-upgrade` (#10498), and `cargo-set-version` (in that order of priority)
- Update crates.io with `cargo add` snippets in addition to or replacing the manifest snippets

For more, see https://github.com/killercup/cargo-edit/issues?q=is%3Aissue+is%3Aopen+label%3Acargo-add

### How should we test and review this PR?

This is intentionally broken up into several commits to help reviewing
1. Import of production code from cargo-edit's `merge-add` branch, with only changes made to let it compile (e.g. fixing up of `use` statements).
2. Import of test code / snapshots.  The only changes outside of the import were to add the `snapbox` dev-dependency and to `mod cargo_add` into the testsuite
3. This extends the work in #10425 so I could add back in the color highlighting I had to remove as part of switching `cargo-add` from direct termcolor calls to calling into `Shell`

Structure-wise, this is similar to other commands
- `bin` only defines a CLI and adapts it to an `AddOptions`
- `ops` contains a focused API with everything buried under it

The "op" contains a directory, instead of just a file, because of the amount of content.  Currently, all editing code is contained in there.  Most of this will be broken out and reused when other `cargo-edit` commands are added but holding off on that for now to separate out the editing API discussions from just getting the command in.

Within the github UI, I'd recommend looking at individual commits (and the `merge-add` branch if interested), skipping commit 2.  Commit 2 would be easier to browse locally.

`cargo-add` is mostly covered by end-to-end tests written using `snapbox`, including error cases.

There is additional cleanup that would ideally happen that was excluded intentionally from this PR to keep it better scoped, including
- Consolidating environment variables for end-to-end tests of `cargo`
- Pulling out the editing API, as previously mentioned
  - Where the editing API should live (`cargo::edit`?)
  - Any more specific naming of types to reduce clashes (e.g. `Dependency` or `Manifest` being fairly generic).
- Possibly sharing `SourceId` creation between `cargo install` and `cargo edit`
- Explore using `snapbox` in more of cargo's tests

Implementation justifications:
- `dunce` and `pathdiff` dependencies: needed for taking paths relative to the user and make them relative to the manifest being edited
- `indexmap` dependency (already a transitive dependency): Useful for preserving uniqueness while preserving order, like with feature values
- `snapbox` dev-dependency: Originally it was used to make it easy to update tests as the UX changed in prep for merging but it had the added benefit of making some UX bugs easier to notice so they got fixed.  Overall, I'd like to see it become the cargo-agnostic version of `cargo-test-support` so there is a larger impact when improvements are made
- `parse_feature` function: `CliFeatures` forces items through a `BTreeSet`, losing the users specified order which we wanted to preserve.

### Additional Information

See also [the internals thread](https://internals.rust-lang.org/t/feedback-on-cargo-add-before-its-merged/16024).

Fixes #5586

---
## [Niautanor/didactic-octo-dotfiles](https://github.com/Niautanor/didactic-octo-dotfiles)@[17d3bd652f...](https://github.com/Niautanor/didactic-octo-dotfiles/commit/17d3bd652f967e87db570ac9634b5de04d4b2abc)
#### Friday 2022-12-16 03:53:32 by Luna Gräfje

Switch from ibus to fcitx5

So much yak shaving ;-;

Anyway, I could not for the life of me get ibus to work on wayland.
Fcitx5 is also kinda wonky at times but at least it kinda works
sometimes now and actually lets me choose different substitutions when I
press space

---
## [ZephyrTFA/tgstation](https://github.com/ZephyrTFA/tgstation)@[9440d42a8e...](https://github.com/ZephyrTFA/tgstation/commit/9440d42a8e1c5f268a614948769c67558e79b98d)
#### Friday 2022-12-16 04:11:13 by MrMelbert

Chaplain armor beacon now uses radial + previews possible armor sets, plus some choice beacon code cleanup. (#71674)

## About The Pull Request

- The chaplain choice beacon now uses a radial to select the armor set,
instead of a list, giving the user a preview of what each looks like.


![image](https://user-images.githubusercontent.com/51863163/205417930-f5ceab11-6974-48a9-a871-abcb8228bcf2.png)

- Lots of additional cleanup to choice beacon code in general. Less copy
pasted code.
- All beacons now speak from the beacon with their message, instead of
some going by "headset message". Soul removed

## Why It's Good For The Game

I always forgot when selecting my armor which looks like what, and
choosing an ugly one is a pain since you only get one choice. This
should help chaplains get the armor they actually want without needing
to check the wiki.

## Changelog

:cl: Melbert
qol: The chaplain's armament beacon now displays a radial instead of a
text list, showing previews of what all the armor sets look like
qol: (Almost) all choice beacons now use a pod to send their item,
instead of just magicking it under your feet
code: Cleaned up some choice beacon code. 
/:cl:

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>

---
## [rHermes/adventofcode](https://github.com/rHermes/adventofcode)@[c2e9b75196...](https://github.com/rHermes/adventofcode/commit/c2e9b7519601916cd5e4af68efd1b7db7953e7c2)
#### Friday 2022-12-16 07:01:55 by Teodor Spæren

2022 Day 16

LEADERBOARD BABY!

This was a rather nice surprise, after yesterdays failures! I was not
expecting to place today, as I felt rather slow to finish both tasks,
but it seems I did rather well, this being my highest rating on part 1
ever.

The task itself was the first challenging one this year. The first part
can be solved by simply using memoization to speed things up. The first,
and rather obvious, optimization here is to realize that you can
calculate how much pressure will be released by a valve, when you open
it, so there is no need to keep track of how much pressure is being
released at each time step.

The second is that there is no point in opening valves with a flow rate
of 0.

These two where enough to get part 1 across the line, but part 2 was
harder, as seen by the time. My first attempt was to simply adapt my
solution to part 1. This involved adding another parameter, and took a
quite a bit of fiddling to keep right, but I managed it. The only
problem was that it was far to slow. I applied more optimizations, such
as stopping once all valves where open, when that didn't work I stopped
when all valves with a rate higher than 0 was open. When that didn't
work I realized that it doesn't matter which player is where, and so
that reduced the search space by half.

I was able to calculate the answer for 23 minutes using this method, but
26 was going to take more RAM and time than I had. I started thinking
about ways to cut out states. One of them was to drop the nodes with a
flow rate of 0. To do this I would have to introduce the idea that the
path to different nodes had different cost. I didn't end up implementing
it in that form, but instead decided to pivot completely to a new
approach:

We being by building up the shortest paths between all the nodes. There
are so few, that this is very fast. We then build a set of the nodes
with a rate higher than 0, which are not yet opened. With these two
facts, we no longer talk about moving from room to room, but rather
which valve we are going to open next. This works, because there is no
benefit in moving, unless you are going to open a valve, so we can just
look at the total cost of opening a particular valve.

Doing it with 2 actors turned out to be a bit tricker, I tried to
integrate it into the system I already had for the older model, but they
differed to much. In the end, I introduced two separate remaining times
for the two actors, and simply simulated each of them moving to a given
valve, opening it and so forth. As long as the lists of valves are
shared, so they are not trying to open the same valve, they don't have
to think about each others timestep at all.

When I ran this on the example it returned very quickly, and I was
confident that I had now found the solution. I let it run, and became
more and more nervous, because it took quite some time, but in the end
it produced and answer, and it was correct.

In hindsight, I should have pivoted to this new method before, I spent a
bit too long trying to bruteforce this. I don't feel to bad about this
however, because it could just have easily have worked, and paid off
handsomely.

Seeing as both of my solutions here are rather slow, I really look
forward to optimizing this one!

Score:
      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
 16   00:16:11     27     74   01:22:08    192      0

---
## [pmozil/discrete_maths_project](https://github.com/pmozil/discrete_maths_project)@[76b6b371b6...](https://github.com/pmozil/discrete_maths_project/commit/76b6b371b6fb3c64ba527d0a7401f5f0a35fccc3)
#### Friday 2022-12-16 08:46:20 by Petro Mozil

Optimise dfs in alternative_sat, start making finaal function

Goodness fuck, why is this so damn boring? Why would this shit be used in compilers? Oh, that's right, IT IS'NT. N-COLOURING IS USED THERE, AND FOR THAT WE HAVE FUCKING LINEAR COLOURING. Fuck this

---
## [projectkepler-ru/sunset-wasteland](https://github.com/projectkepler-ru/sunset-wasteland)@[f7f7ae2cfc...](https://github.com/projectkepler-ru/sunset-wasteland/commit/f7f7ae2cfc1c91d2df5bfdbd7895e7ab2c6eb4d3)
#### Friday 2022-12-16 09:35:46 by Colovorat

Fixes cable merging, changes merging code just a little bit (#60997)

Makes stack code support merging two different stacks with the same mats, but different mats_per_unit numbers by implementing averages.

It's in an attempt to support the stupid efficiency shit that protolathes do. It's not great, but it ought to work alright for now. Kinda a bandaid
Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [im-zelda-8bit/compito-nodejs](https://github.com/im-zelda-8bit/compito-nodejs)@[c0bad82f0c...](https://github.com/im-zelda-8bit/compito-nodejs/commit/c0bad82f0c589bd9e88f903ddb4f509a1791d6f2)
#### Friday 2022-12-16 10:49:56 by frapisa

Removed useless battaglia navale call server

fuck your mom

---
## [mannsoj/skolagymsnv](https://github.com/mannsoj/skolagymsnv)@[45125cf51f...](https://github.com/mannsoj/skolagymsnv/commit/45125cf51fdc7ead3f239d01f39f88c271d7001b)
#### Friday 2022-12-16 11:11:01 by augustinromaniak

this is my church, this is where i heal my hurt, for tonight god is a dj *commencing pleasing*

---
## [harshitajain06/To-Do-List](https://github.com/harshitajain06/To-Do-List)@[2f57131969...](https://github.com/harshitajain06/To-Do-List/commit/2f57131969d8c915bbe63807f01e2570c7f0c997)
#### Friday 2022-12-16 13:03:31 by Harshita Jain

Merge pull request #5 from harshitajain06/jestTest

Test add and delete using Jest

> # Hi Team, 👋🏻👋🏻
> Your project is complete! There is nothing else to say other than... it's time to merge it :shipit: Congratulations! 🎉🚀🔥🎉🎉 ![](https://camo.githubusercontent.com/77a3b06fb2e9d9e88275dc52c3b7e3afcdac80ee2d4cda67d1fd78eeb8a5663d/68747470733a2f2f6d65646961322e67697068792e636f6d2f6d656469612f47376c664a527276646874784b384f5647792f67697068792e676966) [ ![68747470733a2f2f6d65646961322e67697068792e636f6d2f6d656469612f47376c664a527276646874784b384f5647792f67697068792e676966](https://camo.githubusercontent.com/77a3b06fb2e9d9e88275dc52c3b7e3afcdac80ee2d4cda67d1fd78eeb8a5663d/68747470733a2f2f6d65646961322e67697068792e636f6d2f6d656469612f47376c664a527276646874784b384f5647792f67697068792e676966) ](https://camo.githubusercontent.com/77a3b06fb2e9d9e88275dc52c3b7e3afcdac80ee2d4cda67d1fd78eeb8a5663d/68747470733a2f2f6d65646961322e67697068792e636f6d2f6d656469612f47376c664a527276646874784b384f5647792f67697068792e676966) [ ](https://camo.githubusercontent.com/77a3b06fb2e9d9e88275dc52c3b7e3afcdac80ee2d4cda67d1fd78eeb8a5663d/68747470733a2f2f6d65646961322e67697068792e636f6d2f6d656469612f47376c664a527276646874784b384f5647792f67697068792e676966)
> 
> ## Highlights ✨✨
> * No Linters Error ✅
> * Followed GitHub flow ✅
> * Great working on the tests🔥🚀🎉
> * Descriptive PR ✅
> * Professional README ✅
> 
> ## Optional suggestions
> _Every comment with the [OPTIONAL] prefix won't stop the approval of this PR. However, I strongly recommend you to take them into account as they can make your code better. Some of them were simply missed by the previous reviewer and addressing them will really improve your application._
> 
> Cheers and Happy coding!👏👏👏
> 
> Feel free to leave any questions or comments in the PR thread if something is not 100% clear. Please, remember to tag me in your question so I can receive the notification.
> 
> _As described in the [Code reviews limits policy](https://microverse.zendesk.com/hc/en-us/articles/1500004088561) you have a limited number of reviews per project (check the exact number in your Dashboard). If you think that the code review was not fair, you can request a second opinion using [this form](https://airtable.com/shrQAqnBwek5a0O0s)._

Hi @Reem-lab 

Thanks a lot for approving my submission 😊

---
## [BoozeBear99/codeforces](https://github.com/BoozeBear99/codeforces)@[6ee88045a9...](https://github.com/BoozeBear99/codeforces/commit/6ee88045a9d3209edb896a88b2a8f851af6d862e)
#### Friday 2022-12-16 13:04:01 by Sankalp Bansal

Lvl1: easy problem. simple logic

I fucked up my first competition on codeforces, that too after this stupid ass question. It is easy, no optmizations, just need to look for the right method. Short & simple.

---
## [akgold/do4ds](https://github.com/akgold/do4ds)@[40fd10dc86...](https://github.com/akgold/do4ds/commit/40fd10dc86be2742272897f9cf1384e2d4179cab)
#### Friday 2022-12-16 13:39:45 by Jon Harmon

Chapter 5 tweaks and notes (#111)

* Chapter 5 tweaks and notes

Line 104: This is the second time you tried to point us away from your book. I think the mention at the start of the chapter is enough, don't feel like you have to keep doing that!

Line 110: Link doesn't go anywhere. Is that going to be an appendix? It's probably good to explicitly call out where you're sending us, since eventually this will be print and you can't rely on the link.

The docker example: I'm getting this in the browser when I run it:
```
{
error: "404 - Resource Not Found"
}
```

It seems like it built properly. Did I do something wrong, or is the image broken?

Line 159: Probably explicitly call out that we need to `exit` the docker terminal (to get back to our actual command line) before running the next docker command.

Oh hey, looking at the log told me to actually look at http://127.0.0.1:8000/__docs__/ to see what you were pointing at. http://localhost:8000/__docs__/ also works. I'm guessing maybe you lost the underscores in a copy/paste?

Line 163: Probably have us `docker kill palmer-plumber` again before moving on.

Line 171: Didn't work for me in my Windows Powershell. I get this error:

```
docker: invalid reference format.
See 'docker run --help'.
```

Removing the `$(pwd):` part allowed it to run, but so far I can't find where/if this actually mounted. I *think* you're saying I should see it in my normal file browser, but you might want to be more explicit about that in Line 175. I can see it in Volumes in Docker Desktop, but as far as I can tell that isn't corresponding to anywhere on my file system. I also tried changing `$(pwd):` to `.`, with similar "ran but no idea if it saved anything" results. I assume this is a Windows issue, but it's probably worth figuring out!

Line 214: Again the link doesn't go anywhere. New section coming?

Line 227: A concrete example would be helpful, even if it's fake.

Aha, now that I'm in the section on flags and grok the `:`, I got the volume stuff working using `${PWD}$:/project-out` (suggested [here](https://stackoverflow.com/questions/41485217/mount-current-directory-as-a-volume-in-docker-on-windows-10)). Supposedly the `${PWD}` version will work on Linux as well. If so, I recommend switching to that. If updating it works, be sure to update the references at lines 269 and 283 as well.

Line 366: I like the idea of an ongoing project, but it makes it hard to start in a particular chapter. We're seeing this issue since the projects didn't exist when we started; we can't continue a project we haven't started!

* Clean up docker's intro

Oops, I read this part before I started editing and forgot that this sentence threw me off.

---
## [vermiculus/git](https://github.com/vermiculus/git)@[f1c903debd...](https://github.com/vermiculus/git/commit/f1c903debdcbf6aaf8fd3abf222fa941b42d5d31)
#### Friday 2022-12-16 13:40:03 by Ævar Arnfjörð Bjarmason

cocci: make "coccicheck" rule incremental

Optimize the very slow "coccicheck" target to take advantage of
incremental rebuilding, and fix outstanding dependency problems with
the existing rule.

The rule is now faster both on the initial run as we can make better
use of GNU make's parallelism than the old ad-hoc combination of
make's parallelism combined with $(SPATCH_BATCH_SIZE) and/or the
"--jobs" argument to "spatch(1)".

It also makes us *much* faster when incrementally building, it's now
viable to "make coccicheck" as topic branches are merged down.

The rule didn't use FORCE (or its equivalents) before, so a:

	make coccicheck
	make coccicheck

Would report nothing to do on the second iteration. But all of our
patch output depended on all $(COCCI_SOURCES) files, therefore e.g.:

    make -W grep.c coccicheck

Would do a full re-run, i.e. a a change in a single file would force
us to do a full re-run.

The reason for this (not the initial rationale, but my analysis) is:

* Since we create a single "*.cocci.patch+" we don't know where to
  pick up where we left off, or how to incrementally merge e.g. a
  "grep.c" change with an existing *.cocci.patch.

* We've been carrying forward the dependency on the *.c files since
  63f0a758a06 (add coccicheck make target, 2016-09-15) the rule was
  initially added as a sort of poor man's dependency discovery.

  As we don't include other *.c files depending on other *.c files
  has always been broken, as could be trivially demonstrated
  e.g. with:

       make coccicheck
       make -W strbuf.h coccicheck

  However, depending on the corresponding *.c files has been doing
  something, namely that *if* an API change modified both *.c and *.h
  files we'd catch the change to the *.h we care about via the *.c
  being changed.

  For API changes that happened only via *.h files we'd do the wrong
  thing before this change, but e.g. for function additions (not
  "static inline" ones) catch the *.h change by proxy.

Now we'll instead:

 * Create a <RULE>/<FILE> pair in the .build directory, E.g. for
   swap.cocci and grep.c we'll create
   .build/contrib/coccinelle/swap.cocci.patch/grep.c.

   That file is the diff we'll apply for that <RULE>-<FILE>
   combination, if there's no changes to me made (the common case)
   it'll be an empty file.

 * Our generated *.patch
   file (e.g. contrib/coccinelle/swap.cocci.patch) is now a simple "cat
   $^" of all of all of the <RULE>/<FILE> files for a given <RULE>.

   In the case discussed above of "grep.c" being changed we'll do the
   full "cat" every time, so they resulting *.cocci.patch will always
   be correct and up-to-date, even if it's "incrementally updated".

   See 1cc0425a27c (Makefile: have "make pot" not "reset --hard",
   2022-05-26) for another recent rule that used that technique.

As before we'll:

 * End up generating a contrib/coccinelle/swap.cocci.patch, if we
   "fail" by creating a non-empty patch we'll still exit with a zero
   exit code.

   Arguably we should move to a more Makefile-native way of doing
   this, i.e. fail early, and if we want all of the "failed" changes
   we can use "make -k", but as the current
   "ci/run-static-analysis.sh" expects us to behave this way let's
   keep the existing behavior of exhaustively discovering all cocci
   changes, and only failing if spatch itself errors out.

Further implementation details & notes:

 * Before this change running "make coccicheck" would by default end
   up pegging just one CPU at the very end for a while, usually as
   we'd finish whichever *.cocci rule was the most expensive.

   This could be mitigated by combining "make -jN" with
   SPATCH_BATCH_SIZE, see 960154b9c17 (coccicheck: optionally batch
   spatch invocations, 2019-05-06).

   There will be cases where getting rid of "SPATCH_BATCH_SIZE" makes
   things worse, but a from-scratch "make coccicheck" with the default
   of SPATCH_BATCH_SIZE=1 (and tweaking it doesn't make a difference)
   is faster (~3m36s v.s. ~3m56s) with this approach, as we can feed
   the CPU more work in a less staggered way.

 * Getting rid of "SPATCH_BATCH_SIZE" particularly helps in cases
   where the default of 1 yields parallelism under "make coccicheck",
   but then running e.g.:

       make -W contrib/coccinelle/swap.cocci coccicheck

   I.e. before that would use only one CPU core, until the user
   remembered to adjust "SPATCH_BATCH_SIZE" differently than the
   setting that makes sense when doing a non-incremental run of "make
   coccicheck".

 * Before the "make coccicheck" rule would have to clean
   "contrib/coccinelle/*.cocci.patch*", since we'd create "*+" and
   "*.log" files there. Now those are created in
   .build/contrib/coccinelle/, which is covered by the "cocciclean" rule
   already.

Outstanding issues & future work:

 * We could get rid of "--all-includes" in favor of manually
   specifying a list of includes to give to "spatch(1)".

   As noted upthread of [1] a naïve removal of "--all-includes" will
   result in broken *.cocci patches, but if we know the exhaustive
   list of includes via COMPUTE_HEADER_DEPENDENCIES we don't need to
   re-scan for them, we could grab the headers to include from the
   .depend.d/<file>.o.d and supply them with the "--include" option to
   spatch(1).q

1. https://lore.kernel.org/git/87ft18tcog.fsf@evledraar.gmail.com/

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>
Signed-off-by: Taylor Blau <me@ttaylorr.com>

---
## [xDroidOSS-Pixel/platform_frameworks_base](https://github.com/xDroidOSS-Pixel/platform_frameworks_base)@[a9a6476304...](https://github.com/xDroidOSS-Pixel/platform_frameworks_base/commit/a9a647630453661080eafe679fe3d2fd595f1f44)
#### Friday 2022-12-16 13:44:29 by Kuba Wojciechowski

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
## [Kreeldor/awesome-console-services](https://github.com/Kreeldor/awesome-console-services)@[4b8f298fb2...](https://github.com/Kreeldor/awesome-console-services/commit/4b8f298fb2b94b3c492da39ca43fcd2775907eea)
#### Friday 2022-12-16 13:55:01 by techie2000

ascii.town is no longer interactive

Attempting to access it now results in 
```
================================================================================

Nazis, fuck off!

Sorry to everyone else who enjoyed this space.  It was only a matter
of time, and it lasted a lot longer than I ever expected.  It breaks
my heart to log in and see hate on the canvas.  Obscurity is no
longer enough to keep this space as pleasant as it once was.  I'll
clean up what I can and keep https://ascii.town/explore.html running
so that what was created here can continue to be enjoyed.  Thank
you all for your contributions over the years.  You made something
beautiful.

Black lives matter.  Trans rights are human rights.  Much love to
all the gay weirdos out there.

~june

torus@ascii.town  2017-2022

================================================================================
```

---
## [TeamAOF/skylore](https://github.com/TeamAOF/skylore)@[e2730e802d...](https://github.com/TeamAOF/skylore/commit/e2730e802d039107e76e658dcdff0ba328216dd7)
#### Friday 2022-12-16 13:55:03 by Monster Zero

I hate my life, why is artis not working?

updates, hopefully they don't break anything

---
## [Avalon-Benchmark/avalon](https://github.com/Avalon-Benchmark/avalon)@[974ab79b1c...](https://github.com/Avalon-Benchmark/avalon/commit/974ab79b1c1edbb4104cc57152528903d884d599)
#### Friday 2022-12-16 14:23:56 by Zack Polizzi

Merge branch 'zack/procgen' into 'main'

Getting procgen reproducing + performance tuning of rollout worker

Fixed some logging issues:
- allows calls to setup_remote_logger to just print a warning if env variables are missing, instead of an exception
- adds a retry around a SSH failure
- changes the ancestry to include both worker_[workername/id] and command_[name/id], where the commandname can come from a LabelledCommand. This allows finding logs from the LabelledCommand label.
- allows machines without image_names (eg local) to work
- causes the logger subprocess to ignore SIGINT and instead wait for the parent to shut it down
- fixes computronium to work on mac (ie spawn mode multiprocessing)

Other random things:
- adds flag to allow keeping tmux around after an experiment succeeds

RL stuff:
- adds a few feature flags to match procgen baseline implementation - observation image centering, a PPO calculation difference, etc
- adds procgen support
- properly seeds envs
- adds better support for deterministic tests
- adds some integration tests of the rollout worker. includes a completely new simple implementation of the rollout worker, so that we can run both under different conditions and compare that the results are exactly identical. 
- refactored the rollout worker to use shared memory instead of pipes, and other performance optimizations
  - one disadvantage of the new approach is that you now have to pre-declare what info fields you're expecting, and they can only be scalar floating-point castable types (at the moment). as such, i changed `info["task"]` from a string to an enum-style int with lookups for converting between the string and int format.
- refactored the storages to be more performance-optimal for the new rollout worker.
- refactored other code to work with the new storages
- refactored some of the resnet/impala code to be cleaner
- fixed the shutdown logic to shutdown more cleanly - all subprocesses should ignore SIGINT and be shutdown by the parent.
- re-generated the determinism test data, as the tests were no longer passing (no surprise given changes of this magnitude)
- various other little bugfixes

Testing:
- developed and ran the new integration tests for the rollout worker. these have good coverage (although still room to improve further) and should be sensitive to issues given the deterministic comparison to an alternate more-easily-verifiable implementation.
- ran a lot of the regression test suite. this was helpful for picking up things like the PPO runs sometimes exploding hours into the run, and also helpful for just getting a lot of coverage of all the code and parameter space for finding crash-inducing bugs.
- maksis's determinism tests weren't super helpful here except as an additional source of coverage to exercise the code for crash-inducing bugs, since the determinism was broken by all the changes. i think this is a general disadvantage of that type of testing, since deterministic comparison is so over-sensitive (eg a+b != b+a, and tons of similar sadness) that many of the changes you'd most like to test would break determinism. and debugging why a deterministic comparison is no longer working is super painful (i spent days doing that type of stuff working on this PR), so a failing determinism test doesn't help much in identifying the source of the problem, especially when most likely the failure is just due to a false positive like that a+b!=b+a thing. i think focusing on the types of tests i added here will be more useful (they still do deterministic comparisons, but testing smaller parts of the code should make identifying the source of issues easier, plus having side-by-side implementations running in the same process helps a lot in debugging because you can compare the actual outputs, not just their hashes).

Performance:
- procgen is now like ~5x faster than before, ~10k SPS rollout-only, with 64 parallel envs. avalon PPO and dreamer didn't see much performance boost though, which i was disappointed by - guessing they're either limited by godot, or inference time, and i know the off-policy storage still needs some perf optimizations. i'll do some more tracing of those in a separate PR.

See merge request generally-intelligent/generally_intelligent!405

Source: 780fff976a7c64bbebd621cd006139ca55b77840

---
## [voiceflow/general-runtime](https://github.com/voiceflow/general-runtime)@[130ccda3fe...](https://github.com/voiceflow/general-runtime/commit/130ccda3fe90b2a9925b9ca757e96824d8948e33)
#### Friday 2022-12-16 15:12:13 by Tyler Han

feat: nlc entity filling (PL-000) (#449)

<!-- You can erase any parts of this template not applicable to your Pull Request. -->

**Fixes or implements PL-000**

### Brief description. What is this change?
this fix requires a long description, but the code is pretty hard to navigate as well so I'll do my best to explain.
I've noticed terrible performance for the capture step/entity filling feature if the model is untrained. We should have a decent fallback measure if the NLP isn't working.

[NLC](https://github.com/voiceflow/natural-language-commander) is a library we use to handle regex matching against intent utterances and extracting entities when the NLP is untrained. It will only match if the user types everything correctly letter for letter.

In the current implementation of entity filling (called dialog management in the code atm, a bit confusing I know, just assume dialog management = entity filling), if we know the user is trying to fill a SPECIFIC entity of an intent, we first make a match of [their intent against the general model](https://github.com/voiceflow/general-runtime/blob/8e22616890c8c4d011ea12845ae463df788d34e4/lib/services/nlu/index.ts#L85-L115). 

Then we also check it against a `dmPrefix`'ed intent utterances:
![Screen Shot 2022-12-05 at 3 56 39 PM](https://user-images.githubusercontent.com/5643574/205741203-edfacfad-90ab-4161-a4ed-c00e941a8fce.png)
![Screen Shot 2022-12-05 at 4 03 47 PM](https://user-images.githubusercontent.com/5643574/205742304-013944b3-8577-4dd0-8258-a34928eaf666.png)

These are special utterances tied to the intent, the prefix is just a hash of the intent name. When we know the user is trying to fill for a specific intent, we call the NLP and prepend the prefix to their raw text query:
https://github.com/voiceflow/general-runtime/blob/8e22616890c8c4d011ea12845ae463df788d34e4/lib/services/dialog/index.ts#L125-L128

So if they said "quote for life insurance" as `query` we would first run it against the NLP normally and then against "1f79373e6d quote for life insurance" as `query`. The LUIS model already has these utterances with prefixes baked in, the NLC does not. 

Also our [predict](https://github.com/voiceflow/general-runtime/blob/8e22616890c8c4d011ea12845ae463df788d34e4/lib/services/nlu/index.ts#L24) code comes in 3 stages:
1. try against the NLC regex but hard matching for slots. If the utterance is something like "quote for {insuranceType}" only valid forms of the slot are okay. They can't say "quote for toilet paper" and expect NLC to match
2. call the actual `luis-authoring-service` endpoint and check against the actual NLP
3. if the user never trained their model, try against NLC regex but open matching flow slots, If the utterance is something like "quote for {insuranceType}" then  "quote for toilet paper" will match the intent and insuranceType = "toilet paper"

What this PR does is if we KNOW that we're looking for the entity of a specific intent, we pass that through when generating the NLC model, and inject that intent's slots' (`intent.slots[].dialog.utterances`) utterances, with prefixes, into the actual utterances of the intent.

[we have this `handleDialog` function for NLC]( "quote for toilet paper"), but looked through the source code, it never worked. It relies on `slot.dialog.utterances` which was never getting passed in:
https://github.com/voiceflow/general-runtime/blob/15a8cfbad416a14af7c194bc59b1516325b50ea3/lib/services/nlu/nlc.ts#L155-L162
`filledEntities` never contains the `dialog.utterances` required, so this would be `NoneIntent` all the time anyways.

TLDR, if we are looking for a specific intent's slots' utterances, just add them to the regex model with a prefix. 

In action:
![Screen Shot 2022-12-05 at 3 47 43 PM](https://user-images.githubusercontent.com/5643574/205746744-b4315ef2-1d2e-4e44-967f-b22be2fbf2c8.png)

Co-authored-by: Tyler Han <tylerhan97@gmail.com>

---
## [Zergspower/Skyrat-tg](https://github.com/Zergspower/Skyrat-tg)@[81ca11b95a...](https://github.com/Zergspower/Skyrat-tg/commit/81ca11b95a59d5cf0eb0a066454b2903f4859503)
#### Friday 2022-12-16 16:43:32 by SkyratBot

[MIRROR] Basic Mob Carp: Retaliate Element [MDB IGNORE] (#18030)

* Basic Mob Carp: Retaliate Element (#71593)

## About The Pull Request

Adds an Element and AI behaviour intended to replicate the "retaliate"
behaviour which made up an entire widely-populated subtype of simple
mobs.
The behaviour is pretty simply "If you fuck with me I fuck with you".
Mobs with the component will "remember" being attacked and will try to
attack people who attacked them, until they lose sight of those people.
They don't have very long memories so breaking line of sight is enough
to remove you from their grudge list.
The implementation unfortunately requires registering to 600 different
"I have been attacked by X" signals but c'est la vie.

It will still be cleaner than
`/mob/living/simple_animal/hostile/retaliate/clown/clownhulk/honcmunculus`
and `mob/living/simple_animal/hostile/retaliate/bat/sgt_araneus`.

I attached it to the pig for testing and left it there because out of
all the farm animals we have right now, a pig would probably get pissed
off if you tried to kill it. Unfortunately it's got a sausage's chance
in hell of ever killing anyone.

## Why It's Good For The Game

It doesn't have much purpose yet but as we make more basic mobs this is
going to see a **lot** of use.

## Changelog

:cl:
add: Basic mobs have the capability of being upset that you kicked and
punched them.
add: Pigs destined for slaughter will now ineffectually attempt to
resist their fate, at least until they lose sight of you.
balance: Bar bots are better at noticing that you're trying to kill
them.
/:cl:

* Basic Mob Carp: Retaliate Element

Co-authored-by: Jacquerel <hnevard@gmail.com>
Co-authored-by: tastyfish <crazychris32@gmail.com>

---
## [hashicorp/nomad](https://github.com/hashicorp/nomad)@[f998a2b77b...](https://github.com/hashicorp/nomad/commit/f998a2b77b84a542d73f11a0a254576f9031d1f3)
#### Friday 2022-12-16 17:20:51 by Michael Schurter

core: merge reserved_ports into host_networks (#13651)

Fixes #13505

This fixes #13505 by treating reserved_ports like we treat a lot of jobspec settings: merging settings from more global stanzas (client.reserved.reserved_ports) "down" into more specific stanzas (client.host_networks[].reserved_ports).

As discussed in #13505 there are other options, and since it's totally broken right now we have some flexibility:

Treat overlapping reserved_ports on addresses as invalid and refuse to start agents. However, I'm not sure there's a cohesive model we want to publish right now since so much 0.9-0.12 compat code still exists! We would have to explain to folks that if their -network-interface and host_network addresses overlapped, they could only specify reserved_ports in one place or the other?! It gets ugly.
Use the global client.reserved.reserved_ports value as the default and treat host_network[].reserverd_ports as overrides. My first suggestion in the issue, but @groggemans made me realize the addresses on the agent's interface (as configured by -network-interface) may overlap with host_networks, so you'd need to remove the global reserved_ports from addresses shared with a shared network?! This seemed really confusing and subtle for users to me.
So I think "merging down" creates the most expressive yet understandable approach. I've played around with it a bit, and it doesn't seem too surprising. The only frustrating part is how difficult it is to observe the available addresses and ports on a node! However that's a job for another PR.

---
## [starbeamjs/starbeam](https://github.com/starbeamjs/starbeam)@[717c9a6490...](https://github.com/starbeamjs/starbeam/commit/717c9a649032416604026a214523e9bfcd6b50be)
#### Friday 2022-12-16 17:40:38 by Yehuda Katz

[WIP] Improvements to `@starbeam/react` (#78)

This commit updates `@starbeam/react` in a number of ways:

## [superficial] Renames `useReactiveSetup` to `Component`

I don't know if this is the right name, and plan to add back `useReactiveSetup` as an alias for 0.9, but I want a nice name for the combo of `useSetup` and `useReactive`.

I think it's the right default for most people, because it lets you close over and use the stable values creates in `useSetup` without caveats.

## Adds a `props` parameter to `Component`

The main problem with the original `useReactiveSetup` design is that the closure it returns is created once. This is necessary to allow it to close over the stable setup values.

Simple example:

```tsx
function Count() {
  return useReactiveSetup(() => {
    // `count` and `increment` are stable across the component's entire
    // mounted lifecycle.
    const count = Cell(0);
    const increment = () => count.current++;

    // this closure closes over those stable values naturally, with no
    // possible stale closure problem. Great!
    return () => (
      <>
        <p>{count.current}</p>
        <button onClick={increment}>++</button>
      </>
    );
  });
}
```

However, if we wanted `Count` to take props, and we wanted to use them inside of `useReactiveSetup`, we'd have a problem:

```tsx
function Count({ initial = 0 }: { initial?: number }) {
  return useReactiveSetup(() => {
    const count = Cell(0);
    const increment = () => count.current++;

    // this closure closes over the original value of `initial`,
    // and it won't update if a new value of initial is passed
    // in.
    return () => (
      <>
        <p>{count.current + initial}</p>
        <button onClick={increment}>++</button>
      </>
    );
  });
}
```

The same problem would happen if you used `useState` outside of the `useReactiveSetup`. The JSX closure would never see the update.

This problem doesn't exist if you decompose `useReactiveSetup` into `useSetup` and `useReactive`.

```tsx
function Count({ initial = 0 }: { initial?: number }) {
  const { count, increment } = useSetup(() => {
    const count = Cell(0);
    const increment = () => count.current++;

    return { count, increment };
  });

  // this closure is created on every render, so it sees the updated `initial`.
  return useReactive(() => (
    <>
      <p>{count.current + initial}</p>
      <button onClick={increment}>++</button>
    </>
  );
}
```

This works, and it's nice that you can separate `useReactiveSetup` in this way. It makes the whole system flexible and compositional, and makes it easier to ease into Starbeam in existing components.

But when you're creating a greenfield Starbeam component, it's much nicer to be able to close over the stable values, like in the original design.

### The Updated `Component` API Takes Props

The updated `Component` API resolves this issue by taking props that get passed into the JSX closure:

```tsx
function Count({ initial = 0 }: { initial?: number }) {
  return Component({ initial }, () => {
    // `count` and `increment` are stable across the component's entire
    // mounted lifecycle.
    const count = Cell(0);
    const increment = () => count.current++;

    // like in the `useReactiveSetup` design, this closure can use the stable
    // `count` and `increment` values directly. But now, the `initial` value
    // from outside `Component` is passed into the JSX closure, and is always
    // up to date.
    return ({ initial }) => (
      <>
        <p>{count.current + initial}</p>
        <button onClick={increment}>++</button>
      </>
    );
  });
}
```

In this design, React will re-render the JSX when:

- `count.current` changes
- the `initial` prop changes.

You could use stable functions created in the `Component` as event handlers without `useEvent`, and create functions that close over cells and formulas (like `increment`) without worrying about staleness (because cells and the functions that interact with them are all stable).

You can also conditionally create cells and formulas, conditionally register `layout` or `idle` handlers (and run them in any order). This is because the setup code runs only once, so they don't need to run in the same order on subsequent renders.

Finally, you can use hooks like `useState` inside of the JSX closure, because it runs on every render. The only values you absolutely need to pass as `Component` props in order to see updates in the JSX closure are the component's own props.

Also, all of this works with [reusable state](https://github.com/reactwg/react-18/discussions/19), which is enforced by React 18 strict mode. This means that if React unmounts and remounts `Count`, you get a new copy of the state in `setup`, as if you had a brand new instance of the `Count` component.

There's still some more fine-tuning to do on this API, but I think it's close to something that we should recommend for green-field Starbeam components. We'll need good docs, but that's a given.

## `use` and `service` work inside of `Component`

You can use `use` and `service` inside of `Component`:

```tsx
function Stopwatch() {
  return Component(({ use }) => {
    // inside of `Component`, this returns a reactive value
    const now = use(Clock);

    return () => <p>{now.current}</p>
  });
}
```

They work the same way as the hook versions, but return a reactive value (that you can use inside the JSX closure) rather than a value.

One last note: throughout this comment, I've been talking about "JSX closures" because that's what the examples are doing, but you can return anything you like from the inner closure and the entire `Component` call will return the most recent result every time.

This is perhaps why the name `Component` isn't quite right (or perhaps deserves an alias with different ergonomics for the non-JSX case).

---
## [Dan1ss1mo/Cataclysm-DDA](https://github.com/Dan1ss1mo/Cataclysm-DDA)@[8e39d6f97c...](https://github.com/Dan1ss1mo/Cataclysm-DDA/commit/8e39d6f97c358c72a3dacc7c2f3ce955ecb30e81)
#### Friday 2022-12-16 18:12:58 by casswedson

fix: edge case ci error exit (#62660)

so a step of the reviewer workflow always runs, good it is the actual
magical step doing the hard work, but if the workflow gets canceled, the
step exits with an error code, I actually knew this but me from like a
day ago was like:
"nah man this won't bother me in the future."

guess what; after a couple hours I was felling the pain my perfectionist
subconscious was putting me through, plus odd error code exits aren't
very professional or clean or pleasing I'd say, also someone may think
it's weird, look into it, waste time looking at my code

title: do not draw much attention

Co-authored-by: casswedson <casswedson@users.noreply.github.com>

---
## [cspiegel/garglk](https://github.com/cspiegel/garglk)@[dd59906d33...](https://github.com/cspiegel/garglk/commit/dd59906d33d36a41bfac288096cb48723691b7bb)
#### Friday 2022-12-16 18:18:04 by Chris Spiegel

Check more than style_Preformatted for monospace

The Agility interpreter uses styles User1 and User2 for monospace, but
Gargoyle only considered style_Preformatted, meaning that Gargoyle
assumed user styles were _not_ monospace, and translated hyphens into
em- and en-dashes.

Since Gargoyle knows which font type a style maps to, use that
information instead of checking the style directly. This will work if
interpreters use User styles, or if they change the appearance of other
styles via hints.

As noted in the comment, this assumes the user has properly set a
monospace font. If a proportional font is set as the monospace font,
Gargoyle will still assume it's monospace, because it's "supposed" to
be. This is at odds with how ligatures are done: there, the font file
itself is examined and if it's monospace, ligatures are disabled.

I think these differing approaches make sense: Here, with dashes, if a
user sets a proportional font as the monospace font, it hardly matters
whether the hyphens become em- and en-dashes, given that the width of
the glyphs is variable anyway (i.e. box drawing is hopelessly broken if
you set a proportional font, so changing hyphens is a drop in the
bucket). And if a monospace font is set as the proportional font, yes,
it'll get em- and en-dashes, but that's fine, since the width of the
characters, at that point, can't be expected to be fixed, given that it
_could_ be a proportional font. It will be a slightly degraded
experience since it won't be obvious it's a longer dash, but then, if
you're setting a monospace font everywhere, you can turn off dash
conversions.

As for ligatures, if the user sets a monospace font for the proportional
font (which is perfectly fine), the ligatures would look pretty silly,
especially the three-character ones. For example:

    Oﬀice
    Ofﬁce
    Oﬃce
    Ofﬂine
    Oﬄine

---
## [arita111997/adventofcode](https://github.com/arita111997/adventofcode)@[33debad094...](https://github.com/arita111997/adventofcode/commit/33debad09443ca69acb3ef4b8abce3151cc15773)
#### Friday 2022-12-16 18:18:16 by Ana Rita Pimenta Carneiro

Proboscidea Volcanium- the slow and ugly version 

I tried my best but it's ugly and slow. Anyway, I commented out twenty lines of code violently to see if it didn't look so crazy. It's still bad, with more comments than code and super slow. This one I'll have to repeat with more time. dammmm

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[599d82e44e...](https://github.com/mrakgr/The-Spiral-Language/commit/599d82e44eaa16766b45d7136cdf50d3d5f0782a)
#### Friday 2022-12-16 18:43:41 by Marko Grdinić

"9:15am. I am up.

9:20am. I've been thinking a lot about the backend. I see I didn't get an answer on which outer backend to use.

Anyway.

Views are at 4,998. Avg at 122.

That shit review is still taking my rating, the report did nothing. The latest chapters have experience as sharp drop in readership. My future is pitch black. And I might just be getting scammed in doing free work for UPMEM.

9:35am. Maybe 30 followers is my limit. They seem to be hard to get.

Anyway, let me just read Fabiniku and that TS High School chapter and then I will watch the PIM course video related to UPMEM. Yesterday I had time to look at the docs and get familiar with its programming model. Since this is not the kind of device that I'd be interested in programming personally - I really want small communicating cores so I can do AI instead, I'll do it slowly. I do not feel like just dropping everything to satisfy that guy's whims. Who knows if the job opening in the future will even be remote or if what I will do here will impress him.

The main challenges will be to make the Python + ref countless C backend and then to make the UPMEM functions callable. I have to do a bunch of things to deal with global variables and the like.

Spiral is not a good fit for UPMEM devices because you can't actually free the memory you allocate in its programs. So ref counting is useless due to that.

9:55am. https://www.youtube.com/playlist?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy
PIM (Processing-In-Memory) Course

Let me get started with this. I'll slowly get a grip on the PIM programming model.

https://youtu.be/p_sLhKeo6ys?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy
PIM Course: Lecture 3: Real-world PIM: UPMEM PIM - Fall 2022

Let me start with this and then I will watch the lecture on programming these things.

https://sdk.upmem.com/2021.4.0/031_DPURuntimeService_Memory.html
> A buddy allocator uses a pre-allocated area in the heap to perform dynamic allocation and freeing of buffers, offering functions similar to standard malloc and free.

Actually, I could use this for just things like closures and union types.

///

Allocate buffers, using buddy_alloc, with the following restrictions:
* Allocated buffer size should not exceed 4096 bytes
* Minimum size of allocated buffers is 32 bytes
* Allocated buffers are automatically aligned on DMA-transfer size, so that they can be used to transfer data from/to MRAM

///

I've been too fast to discount them. I mean, this amount would be more than enough for any kind of closure or union type.

Yeah, I am getting bearish and pessimistic far too easily. I should be able to make good things happen with the buddy allocator.

I do not need to get rid of the ref counting from the UPMEM C backend.

That should make it a lot more valuable. Yeah, this is what happens when you make decisions far too quickly. You end up with delusions. The buddy allocator is great. 4k is a huge max limit that I can expect to never reach in realistic scenarios.

Though, I am not sure what to do about allocating arrays.

...Well, I'll just limit them to 4k then. It doesn't matter, this is just a demo. If more is needed the devs can hash it out. The user can use the regular allocator if he really needs a ton of WRAM.

https://youtu.be/p_sLhKeo6ys?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy&t=275

Let me get back to watching this.

https://youtu.be/p_sLhKeo6ys?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy&t=680

64kb WRAM...Yeah, it makes no sense to go beyond 4k if the total memory size is only 64kb.

10:30am. After I am done with these videos, I will check out the Safari benchmark code. I want to see how they do it.

11am. https://youtu.be/7c6x5GJG6dw?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy
PIM Course: Lecture 4: Real-world PIM: Microbenchmarking of UPMEM PIM - Fall 2022

I'll watch this and the programming lecture, and then I am done for the day.

Right now I am thinking how I should handle the `with` statement in Python. It is so annoying, but I might have to extend the language. I'll think I'll just skip it. The `with` statement can ensure that the resources are freed on error, but it does not matter for the demo. I'll just skip it. The del insertion can ensure the resources are freed.

11:35am. https://www.quantamagazine.org/how-the-brain-distinguishes-memories-from-perceptions-20221214/

I'll read this later. Focus me.

11:50am. https://github.com/upmem/dpu_demo/blob/sdk-2021.3/checksum/host/host.py#L64

I am looking at some example code here.

One thing I do not understand is whether MRAM has to be statically declared in the code ahead of time. I'll delay asking the lead compiler dev about it until I watch the lectures.

https://youtu.be/zF70xuhesME?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy
PIM Course: Lecture 9: Programming PIM Architectures - Fall 2022

Let me finally watch this.

https://youtu.be/zF70xuhesME?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy&t=196

They can bee seen as a loosely coupled accelerator.

https://youtu.be/zF70xuhesME?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy&t=485

As I gleamed so far, the library actually allocates DPUs themselves instead of blocks of memory.

12:20pm. https://youtu.be/zF70xuhesME?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy&t=752

Here it explains the transfers. This is a good tutorial.

https://youtu.be/zF70xuhesME?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy&t=777

Ah, I see. This is how dynamic allocation could work. It is quite rough.

...Still, does this have any alignment requirements?

https://sdk.upmem.com/2021.4.0/032_DPURuntimeService_HostCommunication.html#communication-with-host-applications

///

dpu_copy_from(struct dpu_set_t set, const char *symbol_name, uint32_t symbol_offset, void *dst, size_t length) to copy a buffer from a single DPU
dpu_broadcast_to(struct dpu_set_t set, const char *symbol_name, uint32_t symbol_offset, const void *src, size_t length, dpu_xfer_flags_t flags) to broadcast a buffer to a set of DPUs
dpu_push_xfer(struct dpu_set_t set, dpu_xfer_t xfer, const char *symbol_name, uint32_t symbol_offset, size_t length, dpu_xfer_flags_t flags) to push different buffers to a set of DPUs in one transfer.

///

Oh they literally have symbol names here.

https://youtu.be/zF70xuhesME?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy&t=1189

Let me backtrack just a bit.

https://youtu.be/zF70xuhesME?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy&t=793

https://sdk.upmem.com/2021.4.0/202_RTL.html#buddy-alloc

> The allocated buffer is aligned on 64 bits, in order to ensure compatibility with the maximum buffer alignment constraint. As a consequence, a buffer allocated with this function is also compatible with data transfers to/from MRAM.

> Due to the idea of the buddy algorithm (to decrease external fragmentation), the allocated blocks will be of size equal to a power of 2. In other words, if the user allocates 33 bytes, 64 bytes will be allocated and when 2049 bytes are requested, 4096 will be allocated. The user might want to take this into account if she/he wishes to minimise the memory consumption.

> The minimal size of the allocated block is 16 bytes, but can easily be changed in future implementations, so buddy_alloc is mostly adapted to allocating medium and big structures, such as arrays containing more than 8 bytes (in order to make sure that not too much memory space is wasted), binary trees or linked lists.

The minimum here is different from what the other parts of the doc say.

https://sdk.upmem.com/2021.4.0/CAPILowLevel/dpu__memory_8h.html#a66e9ccbcd5ec3f7767441a0926f24538

Here is copy_to_mram. It is different from in the slides.

The docs are somewhat incomplete.

https://sdk.upmem.com/2021.4.0/031_DPURuntimeService_Memory.html
The source or target address in MRAM must be aligned on 8 bytes. Developers must carefully respect this rule since the Runtime Library does not perform any check regarding this point.

When doing transfers I need to make sure MRAM pointers are aligned as well. This could result in difficulties if I am just pushing offets around.

12:50pm. Let me stop here. I keep jumping back and forth, thinking about my ideas.

I am going to open an issue somewhere, asking thme about variable length arrays. So far all the examples only have statically allocated ones.

Let me do the chores here.

1:40pm. Breakfast first.

2:05pm. Akiba Maid War. In this ep it seems Ranko dies.

3:30pm. Damn, she is really gone.

Let me finish watching the lecture and then I will post a question on UPMEM repo, one of them, as to how variables be passed into the kernel.

Focus me. Let me get this out of the way today. While I wait for the question tomorrow, I'll continue to write.

https://youtu.be/zF70xuhesME?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy&t=1357

These transfers are pretty slow.

https://youtu.be/zF70xuhesME?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy&t=1485

I am not sure what is meant by this.

https://youtu.be/zF70xuhesME?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy&t=1715
> How To Pass Parameters To The Kernel

Yes, this is exactly what I wanted to know! How?

https://youtu.be/zF70xuhesME?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy&t=1758

This explains the host.

https://youtu.be/zF70xuhesME?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy&t=1806

I am finally at the level where I can look at this and understand it. Holy shit is this complex.

https://youtu.be/zF70xuhesME?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy&t=1807

I am just looking at this and thinking. I am going to have to take a look at the vector addition code to see whether they are viable length or not.

https://youtu.be/zF70xuhesME?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy&t=1768

What is this, `dpu_arguments_t`? I'll find that out later.

https://youtu.be/zF70xuhesME?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy&t=2616

I need to check these examples out.

https://youtu.be/zF70xuhesME?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy&t=2737

Here is the link.

https://youtu.be/H_xvB_O-bWM?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy
PIM Course: Lecture 10: Benchmarking and Workload Suitability on PIM - Fall 2022

This one I'll skip.

https://github.com/CMU-SAFARI/prim-benchmarks

Let me check out vector addition.

https://github.com/CMU-SAFARI/prim-benchmarks/tree/main/VA

https://github.com/CMU-SAFARI/prim-benchmarks/blob/main/VA/support/common.h

///

// Structures used by both the host and the dpu to communicate information
typedef struct {
    uint32_t size;
    uint32_t transfer_size;
	enum kernels {
	    kernel1 = 0,
	    nr_kernels = 1,
	} kernel;
} dpu_arguments_t;

///

So it is like this.

Anyway now that I see this, I can be sure they are using C on the host side.

4:25pm. Now I am lightly cruising the Akiba Maid War thread. Let me just read it for a bit and then I will check out the host side.

4:55pm. __host dpu_arguments_t DPU_INPUT_ARGUMENTS;

I think I could just pass in the array pointer through here.

5:10pm.

///

    uint32_t mram_base_addr_A = (uint32_t)DPU_MRAM_HEAP_POINTER;
    uint32_t mram_base_addr_B = (uint32_t)(DPU_MRAM_HEAP_POINTER + input_size_dpu_bytes_transfer);

///

Wait, now that I think about it, the UPMEM chip should have 8gb. How can the full space then be accessed using 32-bit adresses?

5:15pm. I am think I am starting to grasp the way to pass in the data...

Let me check out the docs again. It is amazing that the most difficult part of UPMEM is how to pass data into it. What the hell were these guys thinking when they designed this?

Now I am starting to see what was meant when I read that AI startups are flailing on the software.

> __mram_ptr which enable to use a pointer on a MRAM variable or declare a extern MRAM variable.

What is an extrern MRAM variable?

> A special MRAM variable is defined in mram.h: DPU_MRAM_HEAP_POINTER. It defines the end of the memory range used by the MRAM variables. The range from DPU_MRAM_HEAP_POINTER to the end of the MRAM can be used freely by a DPU program, for example to handle dynamically-sized MRAM arrays.

This is what I need for dynamic arrays.

> The symbol_name argument consists of a name of a variable in the DPU code. It can be either a MRAM variable (with the __mram or __mram_noinit attribute) or a WRAM variable (with the __host attribute). Other variables are not visible to the host application.

Right. MRAM is __mram and WRAM vars are __host.

I am betting I could have both __host and __mram_ptr together. Something like `__host __mram_ptr int32_t * a;`.

5:45pm. https://github.com/upmem/dpu_demo/issues/13
How can UPMEM DPUs access 8gb of memory when they are 32-bit?

6:05pm. I am writing some private correspondence. I am not going to post it here, even though it doesn't really matter. I need to stop blabbing about everything in the commits if I am going to be a pro.

6:25pm. Ok, that is basically it.

The C backend should be mostly fine, I can leave it as is. I'll have to make some changes so arrays are handled properly.

Lunch...

7pm. Right now I am thinking how to deal with arrays.

Arrays, arrays...you know what? I should just take them out in the UPMEM Python backend. In the UPMEM C backend, they can be local arrays. That will allow me to easily serialize them. Enough of their horseshit.

I only needed them back in the old Spiral for the sake of typechecking. Now that I have global type inference, they are much less necessary.

I am thinking. What I need to work next is the Python backend. No doubt about it. I'll keep the del insertion from the Cython backend, but otherwise it will be a pure Python backend. PyPy will like what I give it.

I think I might just remove the Cython one altogether as it is such an eyesore.

This kind of refactoring will take some effort, but the Cython backend is simply unacceptable. A decently sized program takes ages to compile and is barely faster than native Python. Though it was useful for testing Spiral v2 back when it came out, that sort of thing is not necessary anymore.

7:10pm. Yeah, I should take this on. A Python backend will end up being useful for other PIM and AI chip devices in the future.

7:20pm. I know that it would be great if I could just dive in and do the UPMEM backend right away, but I should take some care to do the Python backend properly. Then I will extend it.

I'll have to put in the with statement into the language as it is so ubiquitous in Python.

https://learn.microsoft.com/en-us/dotnet/fsharp/language-reference/resource-management-the-use-keyword

Or actually, why not make it like this? Rather than immitate Python, why not immitate F#?

7:30pm. Damn, now I have to worry about this. Let's just not worry about it.

I should consider the `use` and `using` statements once the Python backend is done.

Maybe I should give it a break tomorrow, but I should start with a radical cleanup of the Cython backend. For del insertion, I should definitely take a look at how I am doing the analysis in the C backend. I remember it being really confusing in the Cython backend.

I'll have to refresh my memory. So much of the compiler has faded from it.

I do not know whether the UPMEM compiler lead who contacted me will just ghost it after he realizes that interacting with me will be more than 5 minutes of work, I've had plenty of such interaction in the past, but either way I should just do this and use it as a chance to advertize Spiral. Ultimately, my desire to work on novel hardware has not faded.

7:40pm. Now forget that. Let me read KenDeshi. Tomorrow I will do some writing and then slowly start. I should aim to split my time between the two.

I'll go back to blogging on the Spiral repo, I see that doing it on Patreon is doing me no good."

---
## [mangadex-pub/keycloak-mangadex](https://github.com/mangadex-pub/keycloak-mangadex)@[6f4289ac5e...](https://github.com/mangadex-pub/keycloak-mangadex/commit/6f4289ac5e3737f16ddf30254bddb5b12c801646)
#### Friday 2022-12-16 18:47:22 by Tristan

Tweak out CSS for login page

holy fuck that is cursed

---
## [Jackboxx/arch_config](https://github.com/Jackboxx/arch_config)@[5e9c98edfc...](https://github.com/Jackboxx/arch_config/commit/5e9c98edfc15973b57104d96a902a1438dcb2731)
#### Friday 2022-12-16 18:56:52 by jackboxx

git files search (no .gitignore entries) -> fuck you node_modules

---
## [ramuuns/aoc](https://github.com/ramuuns/aoc)@[9b802651db...](https://github.com/ramuuns/aoc/commit/9b802651db6d6c3ece88e9acb8cd58556512164c)
#### Friday 2022-12-16 18:59:57 by Ramūns Usovs

Memoize and get it down to under a second

Right, took me a while to remember/figure out how the hell does this
memoization work, and yeah, I just needed to store the "best result for
the current path + the place I'm at", and don't push more things into
the the queue if that's the case.

Have to say this day really made me work and remember things, which I
want to say "good"

---
## [tgstation/event-toolbox-tournament-2022](https://github.com/tgstation/event-toolbox-tournament-2022)@[142f23dd67...](https://github.com/tgstation/event-toolbox-tournament-2022/commit/142f23dd674807462c3e19cf33896b6161ec5916)
#### Friday 2022-12-16 19:29:29 by LemonInTheDark

Fixes yorked lighting and yorked cameras (#53)

* Fixes some uses of plane masters that only specified one rather then all

We almost never only want to show SOME hidden planes. Should really make
a helper for this someday

* Fixes area lighting not working on turf change in multiz cases

If you modify a area lit turf when using multiz, it'd end up using the
wrong plane for its light, because of stupid shit on my part. stupid
shit resolved

---
## [KadTheHunter/Kydykos-Nebula](https://github.com/KadTheHunter/Kydykos-Nebula)@[8f5bb20d43...](https://github.com/KadTheHunter/Kydykos-Nebula/commit/8f5bb20d437c57e5a321da61c2f92b0346a8fab7)
#### Friday 2022-12-16 19:57:22 by Kaddicus

Retarded ass template, time to start over.

//TF Raider Joke below//

HOLY SHIT, THIS TEMPLATE IS RETARDED AS FUCK, THE HATE WILL NEVER STOP UNTIL THIS TEMPLATE IS NOT RETARDED AS FUCK HOLY FUCKING SHIT, YOU REALLY THING THIS TEMPLATE IS GOOD DUMBFUCKS, I'VE SHIT OUT BETTER LOGS THAN THIS TEMPLATE

---
## [hawwwwwk/Tau](https://github.com/hawwwwwk/Tau)@[d60f1c2496...](https://github.com/hawwwwwk/Tau/commit/d60f1c2496bcb39ea8b3c4070c039c4e2fa03b88)
#### Friday 2022-12-16 20:08:11 by hawk

I LEAKED MY TOKEN GOD DAMNT ok ok v0.0.3 part two why am i stupid

---
## [oryozana/MyDieter9005](https://github.com/oryozana/MyDieter9005)@[bca694ee4e...](https://github.com/oryozana/MyDieter9005/commit/bca694ee4e3b27b51051f3b341a26f9e7cf6e188)
#### Friday 2022-12-16 20:26:45 by oryozana

DailyMenu, files, cleaning and organizing update!

DailyMenu now capable with every screen, in addition it got some new functions.

DailyMenu now savable on files as String and can be reset from String into DailyMenu.

The app now save your selected meals trough each day, in addition it save everyday DailyMenu inside a file for now...

Ingredient and Meal got some more functions...

DBHelper got an update about the upcoming User changes, each user will save his DailyMenus.

Bug fixes for breakfastSelection, lunchSelection and dinnerSelection, now the Clear button will work correctly.

Small additional changes...

---
## [KadTheHunter/Kydykos-Nebula](https://github.com/KadTheHunter/Kydykos-Nebula)@[b053571498...](https://github.com/KadTheHunter/Kydykos-Nebula/commit/b053571498a96516889718f2ec0bc3ca06fdb242)
#### Friday 2022-12-16 20:44:28 by Kaddicus

Fix hover/select colors everywhere but menu

BUT WHY THE FUCK IS THE MENU STILL RED WHEN HOVERED, HOLY FUCKING SHITBALLS THIS MAKES NO SENSE

---
## [Daggersoath/PlexAniSync-Mappings](https://github.com/Daggersoath/PlexAniSync-Mappings)@[c436074cf2...](https://github.com/Daggersoath/PlexAniSync-Mappings/commit/c436074cf27c97e677a2ea3d3130b4eef635bf95)
#### Friday 2022-12-16 20:51:39 by Daggersoath

Added series with Japanese titles
Added Japanese titles to synonyms for preexisting series

- I'm standing on a million lives
- Arifureta: From commonplace to World's Strongest
- Bakuman
- Code Geass: Lelouch of the rebellion
- Is it wrong to try to pick up girls in a dungeon?
- How not to summon a demon lord
- Komi can't communicate
- Rent a girlfriend
- My next life as a villainess: All routes lead to doom!
- That time I got reincarnated as a slime
- To Your Eternity
- Welcome to Demon School! Iruma-kun
- Yuri!!! on ICE

---
## [boy2mantwicethefam/vgstation13](https://github.com/boy2mantwicethefam/vgstation13)@[e6156a8d91...](https://github.com/boy2mantwicethefam/vgstation13/commit/e6156a8d91d8a24ebe6437f07198713f76946fc1)
#### Friday 2022-12-16 20:57:30 by samo priimek

pulse demon tweaks (#33690)

* remove the stupid maxcharge tweak

* sneed

* comment unused stuff

* revert everything

* prevent you from killing yourself stupidly

* suck SMES faster, gain maxcharge when sucking APC's

* remove the capacity upgrade

* tweak the ability costs and upgrades

---
## [harryob/cmss13](https://github.com/harryob/cmss13)@[68ba844196...](https://github.com/harryob/cmss13/commit/68ba84419624366956ae5f9bde67f1e33287301a)
#### Friday 2022-12-16 21:42:57 by RenaRenaRe

Cross-ciphering fix (#1879)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request
Fixes the cross-ciphering property so it actually works instead of
producing a never ending stream of runtime errors and a broken larva
that never develops. I'm deliberately being vague about what it does
because I think it's supposed to be a secret, the wiki tells you to
"find out in game!", but you can just read the code since it isn't
complicated.
This is my first time using github so sorry if I've fucked something up.

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game
Things should function the way they're supposed to.
Cross-ciphering is an extremely hard to get property that I'm not sure
if anyone has ever actually made in game, now on the incredibly rare
occasion that somebody actually makes it it should work correctly.
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

:cl:
fix: Cross-ciphering now works correctly
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [emberjs/ember-qunit](https://github.com/emberjs/ember-qunit)@[84851831b4...](https://github.com/emberjs/ember-qunit/commit/84851831b468d0b7b15c5af953ea1c0735ef1d5d)
#### Friday 2022-12-16 21:59:03 by Chris Krycho

Feature: introduce native (ambient) TS types

- Add type definitions and type tests.
- Explicitly specify the SemVer policy in the README.
- Configure CI to run type tests against the package.
- Add a note to the migration docs about how to update to use these.

This will shortly be superceded by types published from source *and*
using the types published by Ember itself. Publishing this ahead of
this provides a path for teams to start using `ember-qunit` with
TypeScript *without* pulling it from DefinitelyTyped, allows us to
remove `ember-qunit` from DefinitelyTyped entirely, and does not block
either of those wins on the timeline of a full TS conversion.

To make this work, we need (because one of our dependencies needs) a
peer and dev dep on `@glimmer/interfaces` and `@glimmer/interfaces`, so
that types which use those will type check. This is: annoying in the
extreme. We will want to keep thinking about how to tackle this as an
ecosystem; for now, they are marked as *optional* so no one will have
things blow up as a result of this at least (and that's also correct:
we *only* need them for TS).

---
## [41junkard/cmss13pro](https://github.com/41junkard/cmss13pro)@[7f1e80ca3d...](https://github.com/41junkard/cmss13pro/commit/7f1e80ca3dd4800f54b5ff4dc3663dd1f804c28c)
#### Friday 2022-12-16 22:00:04 by carlarctg

MIDIs are now either 'Meme' or 'Atmospheric', players can toggle each option (#1939)

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

Updated savefile number from 19 to 20. Meme and atmospheric preferences
are enabled by default.

Admin sounds now need a selection between 'Meme' or 'Atmospheric' type.
Ideally, this would let players decide if they want to listen to hijack
or first drop songs without needing to listen to GOOD HITS or whatnot.

I am uncertain about the savefile bit of code. I don't fully understand
it.

As stated I don't care about GBP, so if the tags are teechnicallly
incorrect go ahead and change them or whatever.

# Explain why it's good for the game

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->

> Admin sounds now need a selection between 'Meme' or 'Atmospheric'
type. Ideally, this would let players decide if they want to listen to
hijack or first drop songs without needing to listen to GOOD HITS or
whatnot.

As it says. Lots of people hate the memes and just want to listen to the
cool atmosphere. This is of course dependant on staff selecting the
right option, which is sometimes up to opinion, but I fully trust staff
will be able to handle this subjective affair correctly.

# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

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

:cl:
refactor: Updated savefile number from 18 to 19. Meme and atmospheric
preferences are enabled by default.
admin: Admin sounds now need a selection between 'Meme' or 'Atmospheric'
type. Ideally, this would let players decide if they want to listen to
hijack or first drop songs without needing to listen to GOOD HITS or
whatnot.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

Co-authored-by: Stan_Albatross <66756236+stanalbatross@users.noreply.github.com>

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[15f0685ee8...](https://github.com/treckstar/yolo-octo-hipster/commit/15f0685ee8d8bd33bb39c6c060b0f3e50899734a)
#### Friday 2022-12-16 22:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [microl44/Julet](https://github.com/microl44/Julet)@[d3513d636b...](https://github.com/microl44/Julet/commit/d3513d636b201f857b4f5dba0df96d4343e9237f)
#### Friday 2022-12-16 22:25:49 by Behrad Tahamtani

Added and fixed the shit.
Put directly in main because fuck you shit manager

---
## [Nilstrieb/rust](https://github.com/Nilstrieb/rust)@[8428e50c04...](https://github.com/Nilstrieb/rust/commit/8428e50c04f3e7744fccb1e7272e3100187aace5)
#### Friday 2022-12-16 23:05:08 by Nilstrieb

Rip it out

My type ascription
Oh rip it out
Ah
If you think we live too much then
You can sacrifice diagnostics
Don't mix your garbage
Into my syntax
So many weird hacks keep diagnostics alive
Yet I don't even step outside
So many bad diagnostics keep tyasc alive
Yet tyasc doesn't even bother to survive!

---
## [wroyca/echo](https://github.com/wroyca/echo)@[7c2c92eca6...](https://github.com/wroyca/echo/commit/7c2c92eca6b1bf6530fd0b883240914a8ad3bfce)
#### Friday 2022-12-16 23:41:57 by William Roy

RiiR my beloved

Ah, C++ and GTK, a match made in heaven...or so I thought. For months,
I battled with these two, trying to make them work together in harmony.
But alas, it was not meant to be. Every time I thought I had finally
tamed the beast, it would rear its ugly head and bite me in the form of
a memory leak or undefined behavior.

I used Rust in the past for this project, but I was too comfortable
with C++ to make the switch permanent. But no longer! I can no longer
continue to swim against the current, trying to force GTK and C++ to
work together without the aid of GTKMM. It is time to embrace Rust and
bid farewell to the headache that is C++ and GTK.

So, farewell C++ and GTK, it was a fun ride while it lasted. But now, I
must move on to greener pastures with Rust by my side. Perhaps one day
we shall meet again, but for now, I bid thee farewell with a heavy
heart and a sarcastic tone.

---
## [ChaoticMunchnax/Cringe_Calculator](https://github.com/ChaoticMunchnax/Cringe_Calculator)@[cacc690195...](https://github.com/ChaoticMunchnax/Cringe_Calculator/commit/cacc690195b9e01032c744e1c43a414d252f4dbe)
#### Friday 2022-12-16 23:56:00 by Munchnax

Multiplication fully functioning

Honestly was surprised how easy making this work was.. I orginally did a
newb level mistake, I looked at the entire program without writing a plan
down and directly jumped into programming...

This update:
    -Commented out yesterdays committed code
    -Created and roughly tested a multiplaction function

Thanks for reading have an amazing day!
-Munchnax

---
## [carshalash/tgstation](https://github.com/carshalash/tgstation)@[24d795b354...](https://github.com/carshalash/tgstation/commit/24d795b354d9d6444cdea85fdf68fe0af00f98d4)
#### Friday 2022-12-16 23:59:34 by LemonInTheDark

Adds a preference that disables intensive rendering on different multiz layers (#71218)

## About The Pull Request

It's kinda hacky, but it is nearly the same as just rendering one z
layer.
We allow people to ENTIRELY REMOVE most plane masters from their screen.
This has the side effect of disabling most visual effects (AO is a big
one) which saves a LOT of gpu.

We rely on planes being essentially layers to ensure things render in
the proper order. (outside of some hackyness required to make parallax
work)

I've kept parallax and lighting enabled, so visuals will still look
better then multiz pre plane cube.
It does also mean that things like FOV don't work, but honestly they
didn't work PRE plane cube, and FOV's implementation makes me mad so I
have a hard time caring.

Reduces gpu usage on my machine on tram from 47% to 32%, just above the
27% I get on meta.

I'm happy with this.

Oh also turns out the parallaxing had almost no cost. Need to remove it
as a side effect of what I'm doing but if I could keep it I would.

There's still room for in between performance options, like disabling
things like AO on lower z layers, but I didn't expect it to make a huge
impact, so I left things as is

Also fixes a bug with paper bins not respecting z layer. It came up in
testing and annoyed me

## Why It's Good For The Game

Ensures we can make multiz maps without running into client performance
issues, allows users to customize performance and visual quality.

## Changelog
:cl:
add: Adds a new rendering option to the gameplay preferences. You can
now limit the rendering intensity of multiz levels. This will make
things look a bit worse, but run a LOT better. Try it out if your
machine chokes on icebox or somethin.
/:cl:

Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

---
## [carshalash/tgstation](https://github.com/carshalash/tgstation)@[29d766e25f...](https://github.com/carshalash/tgstation/commit/29d766e25f18c5030972562ed649832077cdfc95)
#### Friday 2022-12-16 23:59:34 by LemonInTheDark

Fixes attempting to offset floating planes (#71490)

## About The Pull Request

This is a dumb idea, and leads to fucked rendering on occasion

## Why It's Good For The Game

Fixes another portion of #70258, a player will no longer have a hidden
antag hud if they move down a z level after getting an antag. We were
trying to offset the floating plane of their image, and it went to shit.
Also fixes a bug with observers not having antag huds for the combo hud
to see. We were only giving them one on mind.on_transfer, rather then on
mind assignment. I hate mindcode

---

