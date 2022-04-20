## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-04-19](docs/good-messages/2022/2022-04-19.md)


1,867,027 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,867,027 were push events containing 3,005,367 commit messages that amount to 218,223,054 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 49 messages:


## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[d411393e72...](https://github.com/tgstation/tgstation/commit/d411393e72586ba70ac45b8af19d9b3b701e58c9)
#### Tuesday 2022-04-19 00:02:18 by Zytolg

NukeOps Firebase Rework (#66149)

Attention Recruit: Welcome to Firebase Balthazord
Here you will lean how to:
-Kill corpo scum
-Kill corpo scum
-Kill corpo scu-

This has been on my docket for months. Ever since gave the Holding Facility a much needed facelift. I have been eyeballing the nukie base, waiting for that stroke of inspiration to hit me. It finally did. Gone are the aging walls of the old encampment. Nukies finally have what well-funded corpo-terrorists always dream of- a home.

It's more than a Home. This is a sweeping rework that is part of a series of reworks to revisit old locations and not only bring them up to date with our current asset roster, but to make them properly belong within the game world. The Nuke-Ops base may ultimately be a tiny chunk of the overall SS13 experience, but I'll be damned if it isn't a defining one. It's also a location that has the capacity to do one thing that I have always wanted to do. Purchase Property. You heard me right, you get to buy rooms now. The newly expanded Nuke-Ops base features, with @Mothblocks blessing, further expansions that you can purchase from your local Syndicate Uplink. Spend your TC, expand your capabilities, and utilize your expertise in order to create
the most mind-boggling disky heists there are.

Possible expansions to your terrorism suite include:
-Ordinance Lab
-Bio-Terrorism Lab
-Chemical Manufacturing Plant

Definite expansions to your Nuke-Ops Firebase include:
-Crew Bunks
-Lab Wing
-War Table
-Upgraded "Disembarkment" Bay"

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[b86cf89125...](https://github.com/tgstation/tgstation/commit/b86cf89125a425ad650abedf436bb02918c36dcd)
#### Tuesday 2022-04-19 00:02:18 by Aleksej Komarov

tgui: API improvements + docs (#65943)


About The Pull Request

This pull request improves tgui API in many ways.

Using TGUI for custom HTML popups

This standardizes and simplifies the process of HTML popup creation and DM <-> JS communication.

Makes tgui window API a perfect alternative for old-style browser panels. It will be super useful for @Iamgoofball since he wanted to make a lightweight browser element that plays background music, and this will make his life a lot easier.

It is now possible to create tgui windows with fully inlined JS and CSS, which can be used to make unkillable tgui-based UIs (can't white/blue screen due to network errors). You can split files into JS and CSS, and still serve a single HTML file using this.

Moved sendMessage function to the Byond API object, where it rightfully belongs, and now supports a shorthand form: Byond.sendMessage(type, payload). This shortens and simplifies a lot of code.

Refactored window.update to no longer be public. Now to subscribe to incoming messages, you should use new public APIs: Byond.subscribe(fn) and Byond.subscribeTo(type, fn), and TGUI internally uses these functions as well, which reduces boilerplate in index.js.

Renamed window.__windowId__ to Byond.windowId (old variable is still available for backwards compatibility).

Byond API now supports null id, e.g. Byond.winget(null, 'url'), which makes things like this possible:

// Fetch URL of a currently connected server
Byond.winget(null, 'url').then((serverUrl) => {
  // Connect to this server (opens a new dreamseeker instance)
  Byond.call(serverUrl);
  // Close this client because new instance is connecting
  Byond.command('.quit');
});

Certain polyfills are now statically compiled (commited into git) and are baked into tgui.html. The downside is that HTML went 16 kB -> 50 kB. The upside is that you can now use a relatively modern level API with full support for IE8 when writing plain old html UIs using /datum/tgui_window directly. They are committed into git, because polyfills will never need to be updated (unless of course we randomly decide to get rid of ie8.js and html5shiv.js).
Breaking Changes

No breaking changes. This should be tested for regressions. Upgrading is simple if you're on a relatively up-to-date branch - copy paste all affected tgui files and you're good.

---
## [epage/cargo](https://github.com/epage/cargo)@[6a4d98d232...](https://github.com/epage/cargo/commit/6a4d98d2327124ca52bb9f67d6ad0097eb6b2e65)
#### Tuesday 2022-04-19 00:20:30 by bors

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
## [gbaraldi/julia](https://github.com/gbaraldi/julia)@[62e0729dbc...](https://github.com/gbaraldi/julia/commit/62e0729dbc5f9d5d93d14dcd49457f02a0c6d3a7)
#### Tuesday 2022-04-19 00:20:45 by Mirek Kratochvil

avoid using `@sync_add` on remotecalls (#44671)

* avoid using `@sync_add` on remotecalls

It seems like @sync_add adds the Futures to a queue (Channel) for @sync, which
in turn calls wait() for all the futures synchronously. Not only that is
slightly detrimental for network operations (latencies add up), but in case of
Distributed the call to wait() may actually cause some compilation on remote
processes, which is also wait()ed for. In result, some operations took a great
amount of "serial" processing time if executed on many workers at once.

For me, this closes #44645.

The major change can be illustrated as follows: First add some workers:

```
using Distributed
addprocs(10)
```

and then trigger something that, for example, causes package imports on the
workers:

```
using SomeTinyPackage
```

In my case (importing UnicodePlots on 10 workers), this improves the loading
time over 10 workers from ~11s to ~5.5s.

This is a far bigger issue when worker count gets high. The time of the
processing on each worker is usually around 0.3s, so triggering this problem
even on a relatively small cluster (64 workers) causes a really annoying delay,
and running `@everywhere` for the first time on reasonable clusters (I tested
with 1024 workers, see #44645) usually takes more than 5 minutes. Which sucks.

Anyway, on 64 workers this reduces the "first import" time from ~30s to ~6s,
and on 1024 workers this seems to reduce the time from over 5 minutes (I didn't
bother to measure that precisely now, sorry) to ~11s.

Related issues:
- Probably fixes #39291.
- #42156 is a kinda complementary -- it removes the most painful source of
  slowness (the 0.3s precompilation on the workers), but the fact that the
  wait()ing is serial remains a problem if the network latencies are high.

May help with #38931

Co-authored-by: Valentin Churavy <vchuravy@users.noreply.github.com>

---
## [StarStation13/StarStation13](https://github.com/StarStation13/StarStation13)@[4652d4bb63...](https://github.com/StarStation13/StarStation13/commit/4652d4bb63cec6f73bc46a0ea75d867d235107d1)
#### Tuesday 2022-04-19 00:24:02 by Jolly

Updates The Derelict to some modern standards, also some turf edits (#66045)

Brings The Derelict up to speed with some of our new mapping tools and stuff.
This also places nearstation turf in certain areas, as well as general turf clean up.
Also cleans up the absurdly placed black holes of light that were over space tiles.
Girder/Grill spawners were placed in certain locations (mostly on external girlls).
I also remapped the main AI chambers SMES power to not go through the fucking wall, as a trade off, its no longer wired round start, and the two pieces of cable that are automatically in the room have been swapped out for two (2) five cables each. Its not enough to reach the main area, but god fuck wires running through walls.

As an aside, some of plating on the outside, walls include, does look weird being full bright like this. I'm neutral for the most part. Theres a weird fine balance that needs to be maintained with some of the areas being open to space, I've opted to keep lattice as nearstation and any thing plating and above as turfed (excluding plating that is solely in space).

I'll be redoing the turfs of this later, sprite wise.

Images

---
## [TurtleShroom/AncientRimMediterranFactions](https://github.com/TurtleShroom/AncientRimMediterranFactions)@[a287c7d081...](https://github.com/TurtleShroom/AncientRimMediterranFactions/commit/a287c7d081d8405bf15f1d8f03029f62d6f0d95c)
#### Tuesday 2022-04-19 01:39:16 by TURTLESHROOM

TSP

1. Balance and flavor (if you have the Right Mods) for certain Pawn Kind Types

2. Lowered Resistance for Roman Pawns

3. Increased Resistance for Faction Leaders

4. A female Senatrix can replace a male Senator, but because of a male-dominated society, she wears and dislikes wearing the menas toga. The penalty is intentional.

5. Gave proper name to the Greeco-Roman General Pawn Kind. The highest ranking Roman general was the Legate, or Legatus. While they commanded Legions in RL, for the purpose of this game, they will use that name for all Hellenic parties' elite top military brass.

6. Merged the two Patch Folder at the root level into one

---
## [RajaKunalPandit1/CodeForces_Questions](https://github.com/RajaKunalPandit1/CodeForces_Questions)@[030c71f99b...](https://github.com/RajaKunalPandit1/CodeForces_Questions/commit/030c71f99b837c0fe8902b790ff352acc6c44292)
#### Tuesday 2022-04-19 03:19:16 by Raja Kunal Pandit

Create 1358A - Park Lighting.cpp

Output Status: 

By Rajakunalpandit, contest: Codeforces Round #645 (Div. 2), problem: (A) Park Lighting, Accepted

Due to the coronavirus pandemic, city authorities obligated citizens to keep a social distance. The mayor of the city Semyon wants to light up Gluharniki park so that people could see each other even at night to keep the social distance.

The park is a rectangular table with n rows and m columns, where the cells of the table are squares, and the boundaries between the cells are streets. External borders are also streets. Every street has length 1. For example, park with n=m=2 has 12 streets.

You were assigned to develop a plan for lighting the park. You can put lanterns in the middle of the streets. The lamp lights two squares near it (or only one square if it stands on the border of the park).

The park sizes are: n=4, m=5. The lighted squares are marked yellow. Please note that all streets have length 1. Lanterns are placed in the middle of the streets. In the picture not all the squares are lit.
Semyon wants to spend the least possible amount of money on lighting but also wants people throughout the park to keep a social distance. So he asks you to find the minimum number of lanterns that are required to light all the squares.

Input
The first line contains a single integer t (1≤t≤104) — the number of test cases in the input. Then t test cases follow.

Each test case is a line containing two integers n, m (1≤n,m≤104) — park sizes.

Output
Print t answers to the test cases. Each answer must be a single integer — the minimum number of lanterns that are required to light all the squares.

Example
inputCopy
5
1 1
1 3
2 2
3 3
5 3
outputCopy
1
2
2
5
8
Note
Possible optimal arrangement of the lanterns for the 2-nd test case of input data example:

Possible optimal arrangement of the lanterns for the 3-rd test case of input data example:

---
## [nullqwertyuiop/Chitung-public](https://github.com/nullqwertyuiop/Chitung-public)@[dd9c9ea647...](https://github.com/nullqwertyuiop/Chitung-public/commit/dd9c9ea6473bccb789838298d1e3aa93e399a19e)
#### Tuesday 2022-04-19 03:36:20 by yhluk

Revert "Fuck you null"

This reverts commit e566d178940063a497c9eaab47b9e9ee1424f55c.

---
## [JD-The-65th/launchQuotes](https://github.com/JD-The-65th/launchQuotes)@[bd8633987c...](https://github.com/JD-The-65th/launchQuotes/commit/bd8633987cffa32c3fb30bff1d47827b39ac7176)
#### Tuesday 2022-04-19 04:25:42 by JD-The-65th

fuck you too dormant code that's coming back to bite me in the ass

---
## [OliOliOnsiPree/thewasteland](https://github.com/OliOliOnsiPree/thewasteland)@[59a018d95a...](https://github.com/OliOliOnsiPree/thewasteland/commit/59a018d95a11eaed40605e2dccb5b549c6c6e2ba)
#### Tuesday 2022-04-19 04:28:11 by Kirie Saito

NCR Minor Changes (includes Corporal Timelock) (#130)

* adds timelocks to NCR roles

* NCR minor changes

* adds master corporal pins (for RP)

* flavor change

* Update ncr.dm

* yeah that shotgun sucks ass

* Actually makes this shit work, I am an idiot

* typo

* Name was kinda dogshit, changed it

* one binos, not two

---
## [Stephen-M-Anderson/Olaf-the-Unhuggable](https://github.com/Stephen-M-Anderson/Olaf-the-Unhuggable)@[819db13929...](https://github.com/Stephen-M-Anderson/Olaf-the-Unhuggable/commit/819db1392948605cfa2031905381f9b260278bde)
#### Tuesday 2022-04-19 04:56:29 by Chrismorales116

Added some more shit

Damage knockback doesn't work the way I want yet. It's honestly pretty fuckin wonky. I want it to kind of repel you back and kill your momentum. On the plus side if you turn off the damage on the lava traps they become trampolines. WEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE

---
## [Stephen-M-Anderson/Olaf-the-Unhuggable](https://github.com/Stephen-M-Anderson/Olaf-the-Unhuggable)@[152c824df1...](https://github.com/Stephen-M-Anderson/Olaf-the-Unhuggable/commit/152c824df1d77a49f9cb5a7e9c5a512198576d3e)
#### Tuesday 2022-04-19 04:56:29 by Chrismorales116

Oh God Oh Fuck

I closed my laptop while it was pushing did I fuck everything up? Oh shit oh fuck

---
## [Stephen-M-Anderson/Olaf-the-Unhuggable](https://github.com/Stephen-M-Anderson/Olaf-the-Unhuggable)@[c6fc27c41d...](https://github.com/Stephen-M-Anderson/Olaf-the-Unhuggable/commit/c6fc27c41dc895c462d44975c394dd836e8ba376)
#### Tuesday 2022-04-19 04:56:29 by Chrismorales116

grappling kinda works?

"It ain't beautiful and it ain't perfect but at least its somethin"

- Christian Morales 2020, on the subject of "his cock"

---
## [Stephen-M-Anderson/Olaf-the-Unhuggable](https://github.com/Stephen-M-Anderson/Olaf-the-Unhuggable)@[bf0571c505...](https://github.com/Stephen-M-Anderson/Olaf-the-Unhuggable/commit/bf0571c505c3a96c17053befb6c48c12f3c82036)
#### Tuesday 2022-04-19 05:09:22 by Chrismorales116

Added a Buncha Shit

Fuck coding a dash mechanic, all my homies hate coding a dash mechanic

---
## [Stephen-M-Anderson/Olaf-the-Unhuggable](https://github.com/Stephen-M-Anderson/Olaf-the-Unhuggable)@[0a128d33dc...](https://github.com/Stephen-M-Anderson/Olaf-the-Unhuggable/commit/0a128d33dcd2eb9f0b2507bd5dc5d7bac1e75ecc)
#### Tuesday 2022-04-19 05:09:22 by Christian Morales

Fuckin Dashing works? I feel like I said this shit before

Shit works and I added some sihk-ass debug shit, check it out at the "damage test scene" in my folder bby

---
## [Koi-3088/ForkBot.NET](https://github.com/Koi-3088/ForkBot.NET)@[7a00395c77...](https://github.com/Koi-3088/ForkBot.NET/commit/7a00395c7733cb3115ed1f26b220e49a16683394)
#### Tuesday 2022-04-19 05:55:04 by Koi

Mr. Mime is a thing, unfortunately.
Mild clean, some more Cherish set handling attempts.
Exclude set MetDate from mystery gifts.
Fix daycare enum parsing.
Check for no result in case $qc was used or some other weird thing happens.
Remove FixOT and TradeCord as routine types (FlexTrade handles both).
Try to apply trainer info for Mystery gifts.
Re-add fixed met date if not GO origin.
Update DenBot distribution data, minor fixes.
Fix Yamask-Galar in daycare, some more oopsies.
-Add DenBot - a seed lookup and day skipper bot for raids.
-Change AutoRoll's behavior to make use of some of DenBot's functionality.
Minor clean.
Revise TradeCord "traded" check, remove potential user path straggler entries because paranoia, some minor fixes.
TradeCord fixes (shocker, I know).
Extract Json serializer.
Minor clean and fixes.
Minor fixes.
Fix Milcery when an Alcremie variant is a parent.
Update to latest Core and ALM dependencies.
Handle non-shiny events in a better way.
Work around a race condition?
Simplify and de-bugify trade completion check.
Fix indexing, improve chance for Melmetal-Gmax because it's nigh impossible to get.
Rework TradeCord internals, add new functionality:
-Migrate user data from ".txt" files to a serialized Json (migration for a large amount of users will take a few minutes, be patient).
-Make TradeCord configurable, add its own settings category.
-Add some template events with an optional end timer (YYYY/MM/DD 8PM as an example, though any local time format should work).
-Add barebones Pokedex (counter, flavor text).
-Can check dex completion by typing `$dex`, check missing entries by typing `$dex missing`.
-Completing the Pokedex will slightly improve shiny rate.
-Can now mass release cherish event Pokemon and shinies ($massrelease shiny/cherish).
-Various tweaks, improvements, and bugfixes.

Slightly change FixOT's behavior:
-If a shown Pokemon is illegal and an event, attempt to find a match within the MGDB first.
-Try to force users to trade away the shown Pokemon, log attempt to change shown Pokemon.
Add consideration for easter eggs being enabled in settings, fix Suicune
Change species rng for TradeCord, some bugfixes (I really need to rewrite this mess)
Add check if we're using ListUtil for Giveaway instead of TradeCord.
Amend commit since I'm squashing and force-pushing while bringing the fork in line with the main branch
Add Giveaway module to Discord bot (#22)

Thanks, rigrassm.
Co-authored-by: Koi-3088 <61223145+Koi-3088@users.noreply.github.com>
Specify USB port instead of adding the first result (can be found via Device Manager).
Re-add boolean check because we don't want to fix everything
FixOT will attempt to regenerate illegal Pokémon.
Apply trash bytes for reasons.
Minor TradeCord fixes and adjustments.
Minor clean for C#9
Use "GetValidPreEvolutions()" instead of "GetPreEvolutions()".
Index forms correctly.
Fix the fixed and re-introduced empty daycare index error.
*an* Ultra Ball.
Add EvoTree breeding for TradeCord.
Remove unnecessary value declarations for pinging on encounter match.
Mildly beautify EncounterBot mark output.
Integrate Anubis' system update prevention into Soft Reset and Regigigas Encounter Modes.
Rename "Regi" Encounter Mode to "Soft Reset".
Speed up "A" clicks for Regigigas and Soft Reset modes.
Add Mark logging output for EncounterBot.
Fix oops (re-order logic, remove unnecessary lines).
Add optional species and form specification for $massrelease
Use an obscure string splitter because people like symbols in their names.
Fix things that broke after rebasing to the latest main repo commit.
Use a less unfortunate field name and value splitter...again.
Fix Marowak-Alola always generating as an NPC trade.
Add filters for "$list <species>" to narrow down results.
Fix Cherish Pichu and Octillery
Stop making dumb mistakes, me (implying the rest of it isn't a dumb mistake).
Can't breed antiques.
Use a less unfortunate embed name and value splitter
Add Melmetal-Gmax to TradeCord.
Add ability to search by caught ball.
Have MassRelease ignore events.
Add specific regional form breeding.
Revise egg rate and egg shiny chance.
Have trade evolutions hold an Everstone.
Add an extra right click when navigating to settings for AutoRoll.
Add reworked encounter/egg/fossil logs.
Minor clean.
Minor clean.
Get rid of EncounterBot, FossilBot, EggFetch text logs until I properly rework them.
Break on an empty page due to aggressive rounding
Add multi-page lists for Tradecord.
More random bugfixes.
Fix some bugs before major clean
Add Language parameter for TradeCord.
Change trainer info input format for TradeCord.
Move focus on Showdown set instead of randomizing a pkm file.
Allow user to enter whatever they want for $list, handle edge cases like Kommo-o
Add "$list all" to show non-duplicate caught species.
Automatically remove from favorites if trading or gifting (small QOL thing).
Change how favorites are removed from user file.
Revert base egg shiny chance nerf.
Fix daycare
Add favorites command to TradeCord.
Slightly nerf eggs.
Fix TradeCord list for shinies
Add TradeCord (my dumbest and messiest project so far, Archit pls don't hate the mess).
Add Showdown output for Star/Square shinies and OTGender.
Add optional link code input for FixOT.
Change how OTName, TID, SID is displayed.
Add Regigigas SR bot.
Add SoJ Camp SR bot.
Ribbons now work with EggTrade (remove ribbons if egg).
Remove EggRoll.
Add another filter for FixOT
Fix.. FixOT
Update offsets for EncounterBot catching.
Slightly change StrongSpawn to work with Regi SR and make it its own mode.
Make SpinTrade only available for USB-Botbase
Update valid eggs for CT
winforms: resize icon.ico to fix crash at startup on unix using mono
Rework Spin, read initial in-game coordinates in order to correct drift
Add TID, SID, Language output for Showdown
Remove obsolete OT and Language parsing
Very minor clean until I have time for a proper one.
Detach controller when stopping USB bot.
Actually set LastUsedBall for EncounterBot (missed when bringing in line with main repo)
Move extra RaidBot timings following the official commit
Remove PKHeX Discord invite from Readme.md

Maybe fewer people will pester devs now about my unofficial fork?
Update for latest main repo EncounterBot commits.
Update README.md
Add back best commit: Red's SpinTrade.
Add egg trades, foreign Dittos and OT for Twitch.
If ItemMule is enabled, also display the item a user is receiving.
Add periodic time sync toggle for all methods of hosting (except for non-soft locked AutoRoll) to (hopefully) prevent den rollover during extended hosts.

Add routine to exit a lobby for SoftLock if no players are ready in time (to preserve soft lock).

Add a routine to recover from disbanded lobbies (when someone disconnects unexpectedly) for SoftLock.

Add a routine to restart game if all else fails and we're stuck in a raid.

Add a routine for adding and deleting friends if we're soft locked and raids go empty.

Slightly reorganize settings, extract methods, minor clean.
Don't use such a generic file name for stream assets.
Check USB port index for running bots. Should fix adding additional USB bots when no config is saved.
Add fixed met date for FixOT.
How do I boolean
Change airplane mode logic, tweak timings and routine for soft lock lobby exit
Rework EggRoll cooldown (static list in favor of a txt file).
Start clean up and refactor
Add setting to increase delay after pressing "Home" after a date skip.
Use USB port index for blocking and sprite pngs if connection type is USB
Add option for airplane host (usb-botbase required)
Add option to softlock on selected species for AutoRoll
Add automatic compatibility for all console languages when date skipping (have to set ConsoleLanguage under ScreenDetection)
Attempt to fix multiple USB device add and connect...again
Minor clean
Fix oops?
Handle add/remove of bots
Distinguish between multiple USB devices, tweak BotRemoteControl for USB, other various fixes
Add SpA modifier for foreign Dittos
Add alpha USB-Botbase support
Fix DateTime parsing for European format for EggRoll
Set fixed EggMetDate and MetDate for EggRoll
More FixOT filters
Remove Beheeyem. Oops.
Split EggRoll into its own routine and trade type, only output "Receiving: Mysterious Egg" if routine is EggRoll, other minor tweaks and fixes
Make FixOT its own queue with roles and counts
Add a couple more OTs to $fix
Parsing for EggRaffle auto-clear and $clearcooldown
Adjust timings and split Watt collecting clicks for AutoRoll
Fix oops with file attachments for Ditto
Further improvements for OT, memes for invalid pokemon (disable EasterEggs)
Add spaces, digits for OT
Randomize memes, cut down bloat
Fix miscellaneous bots after Anubis' recent QOL additions
-Ignore events for OT because headache.
-Add overlooked "$convert <generation>" input for OT.
-Move $clearcooldown to SudoModule
-Clear timer automatically if NoTrainerFound
-More reliable Dittos
-Foreign Dittos for $convert
-Command to clear cooldown for EggRaffle in case trade gets disconnected
-Fix "Trade finished" line to keep result secret
-EggRaffle as a toggle, option to specify channels
-Seed Check output to both DMs and Channel (apparently some want it)
-Randomly generated egg raffle via a "$roll" command with a configurable cooldown
-FixAdOT reworked, has its own command "$fix" and no longer overrides $clone
-Ball: <value> output for Showdown sets
-Fix oversight
-Option to output Seed Check results to Discord channel with a User mention
-Showdown set output for OT name and eggs
-Basic "OT: <name>" option without Showdown set output
-Initial $convert support for EggTrade
-Egg moves for EggTrade test attempt
-Minor update
-EggTrade (by nicknaming a Pokémon "Egg" using $trade)
-Failsafe for memes if enabled but field left blank or incomplete
-Niche breedable Ditto trade mode.
Add minimize button
EggFetch text logs
StrongSpawn mode for EncounterBot
Re-add EncounterBot Master Ball catching
More parsing for FixAdOTs
Park Ball as held item instead of string
Actually remove the offset instead of saying I did
Initial DLC commit
Faster code entry
Removed catching for EncounterBot (need a new offset)
CloneBot mode to fix Nickname and OT if adverts detected

---
## [mszeles/a-hamunish-humanish-thoughtishish](https://github.com/mszeles/a-hamunish-humanish-thoughtishish)@[5c721d16e9...](https://github.com/mszeles/a-hamunish-humanish-thoughtishish/commit/5c721d16e94d34c0d93baa39fea7a6360c788435)
#### Tuesday 2022-04-19 06:05:27 by MSzeles

Minnie: To test or not to test? You have already published that article.
Miki: That is true, but 2 things have changed since then.
Minnie: What is the first one?
Miki: Since then you Minnie, Nikolai and the others joined the team, so our writing became much more insightful and fun.
Nikolai: Yeah! Fun. Sure, Miki. Sure.
Minnie: That is very nice of you Miki. What is the other reason?
Miki: Nester also joined the team. He is THE expert in testing.
Minnie: Oh. I see. Last time I tried his advice and the whole project went down the drain.
Miki: Oh, Minnie. That is cute. I forgot to mention one important thing.
Minnie: What is that?
Miki: He is the son of NoSEO and the younger brother of Neveloper, as you might already know about NoSEO: no matter what they tell, you have to do the opposite.
Minnie: Ouch.

---
## [ammarfaizi2/linux-block](https://github.com/ammarfaizi2/linux-block)@[903ae43307...](https://github.com/ammarfaizi2/linux-block/commit/903ae43307756d0732db0e6347cb1bde2eec8967)
#### Tuesday 2022-04-19 07:46:14 by Linus Torvalds

gpiolib: acpi: use correct format characters

[ Upstream commit 213d266ebfb1621aab79cfe63388facc520a1381 ]

When compiling with -Wformat, clang emits the following warning:

  gpiolib-acpi.c:393:4: warning: format specifies type 'unsigned char' but the argument has type 'int' [-Wformat]
                        pin);
                        ^~~

So warning that '%hhX' is paired with an 'int' is all just completely
mindless and wrong. Sadly, I can see a different bogus warning reason
why people would want to use '%02hhX'.

Again, the *sane* thing from a human perspective is to use '%02X. But
if the compiler doesn't do any range analysis at all, it could decide
that "Oh, that print format could need up to 8 bytes of space in the
result". Using '%02hhX' would cut that down to two.

And since we use

        char ev_name[5];

and currently use "_%c%02hhX" as the format string, even a compiler
that doesn't notice that "pin <= 255" test that guards this all will
go "OK, that's at most 4 bytes and the final NUL termination, so it's
fine".

While a compiler - like gcc - that only sees that the original source
of the 'pin' value is a 'unsigned short' array, and then doesn't take
the "pin <= 255" into account, will warn like this:

  gpiolib-acpi.c: In function 'acpi_gpiochip_request_interrupt':
  gpiolib-acpi.c:206:24: warning: '%02X' directive writing between 2 and 4 bytes into a region of size 3 [-Wformat-overflow=]
       sprintf(ev_name, "_%c%02X",
                            ^~~~
  gpiolib-acpi.c:206:20: note: directive argument in the range [0, 65535]

because gcc isn't being very good at that argument range analysis either.

In other words, the original use of 'hhx' was bogus to begin with, and
due to *another* compiler warning being bad, and we had that bad code
being written back in 2016 to work around _that_ compiler warning
(commit e40a3ae1f794: "gpio: acpi: work around false-positive
-Wstring-overflow warning").

Sadly, two different bad compiler warnings together does not make for
one good one.

It just makes for even more pain.

End result: I think the simplest and cleanest option is simply the
proposed change which undoes that '%hhX' change for gcc, and replaces
it with just using a slightly bigger stack allocation. It's not like
a 5-byte allocation is in any way likely to have saved any actual stack,
since all the other variables in that function are 'int' or bigger.

False-positive compiler warnings really do make people write worse
code, and that's a problem. But on a scale of bad code, I feel that
extending the buffer trivially is better than adding a pointless cast
that literally makes no sense.

At least in this case the end result isn't unreadable or buggy. We've
had several cases of bad compiler warnings that caused changes that
were actually horrendously wrong.

Fixes: e40a3ae1f794 ("gpio: acpi: work around false-positive -Wstring-overflow warning")
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: Andy Shevchenko <andriy.shevchenko@linux.intel.com>
Signed-off-by: Sasha Levin <sashal@kernel.org>

---
## [citation-style-language/styles](https://github.com/citation-style-language/styles)@[129ef3c88e...](https://github.com/citation-style-language/styles/commit/129ef3c88e01dbb173f680fb273b40d7fbbf1618)
#### Tuesday 2022-04-19 08:41:05 by Tomas Trepka

Update administrative-science-quarterly.csl (#5991)

This fixes bibliography items from the same author and in the same year. Items should not be grouped by author and should contain year suffix (`2009a`, `2009b`...).

**Actual**
```
Chan, C. S.-c.

2009  “Creating a market in the presence of cultural resistance: The case of life insurance in China.” Theory and Society, 38: 271–305.

2009  “Invigorating the content in social embeddedness: An ethnography of life insurance transactions in China.” American Journal of Sociology, 115: 712–754.
```

**Expected** (according to the [submission guide](https://journals.sagepub.com/author-instructions/asq))
```
Chan, C. S.-c.

2009a  “Creating a market in the presence of cultural resistance: The case of life insurance in China.” Theory and Society, 38: 271–305.

Chan, C. S.-c.

2009b  “Invigorating the content in social embeddedness: An ethnography of life insurance transactions in China.” American Journal of Sociology, 115: 712–754.
```

---
## [Offroaders123/Dark-Mode](https://github.com/Offroaders123/Dark-Mode)@[db0e40b65a...](https://github.com/Offroaders123/Dark-Mode/commit/db0e40b65a95a7ef28add194565678c342683514)
#### Tuesday 2022-04-19 09:03:24 by Offroaders123

Initial Commit!

Note:
This was meant to explain that I am writing this after the date says, and that the commits were added after their date, in 2021-2022. I didn't track the old changes from 2018-2020 in Git (at all, to be honest :( ), so I am adding them later to make sure as much of the history can be kept around. I didn't keep backups of the pack as development of it went along, so I added as much of the updates as I could find online, through Internet Archive, and MediaFire. If you like rambly stories, this next block of text should be great for you! I started writing about the history of Dark Mode, and more about why these changes are getting added at a later date. Cheers!

So, crazy story ahead!

I started working on, what would become Dark Mode, in around mid-to-late 2017. I had just started looking into resource packs at that time, and I had no idea what I was doing! I was just getting a feel for how to change things in-game, like I had always wanted to do.

A little time later, I had started working on my own resource pack, Reality Pack. This was my first actual pack, and I haven't made it public at all (yet? It's not very good, haha). It had the goal of updating all of the textures in-game to have a high-resolution and realistic look to them. This was my project for most of the summer during 2017.

From around late 2017 to mid-2018, I had started working on Faithful 32x for Bedrock Edition! This was what really helped me with learning how to make resource packs. Seeing how other people made their packs really paved the way for my own projects in the future!

I made a Google Site for my Faithful projects (which I later used for all of my projects in general), from which I hosted my pack source on Google Drive from. This made it super easy to share the pack source, as I just had to upload a new `.mcpack` to the Google Drive folder for the update to be released. We'll get back to this later though... haha

Here's an Internet Archive link of the site I luckily randomly decided to make back then, which came in handy looking back on it:
https://web.archive.org/web/2018*/https://sites.google.com/view/faithful-32x-bedrock-edition/

While still working on Faithful 32x, I next moved on to Dark Mode and Simple Sides, around the summer of 2018. I worked a ton to get most of the features started for Dark Mode, and I got pretty much everything supported just over the summer. A crazy project to get done! I was so happy with it.

After working on those to get them more polished, I toyed with the idea of releasing them to the public, something that seemed daunting at the time. I wasn't new to the Internet or anything, but I hadn't really made a presence online before, so these (my resource packs) were my first big thing that I made into an online project! I'm so happy that I committed to moving forward with them.

After posting them to my own Google Site, I went to MCPEDL, which is where I had been learning about resource packs from thus far. First I posted Faithful 32x, then Dark Mode, and lastly Simple Sides.
https://web.archive.org/web/20181015000000*/https://mcpedl.com/faithful-32x-pack/
https://web.archive.org/web/20180815000000*/https://mcpedl.com/dark-mode-resource-pack/
https://web.archive.org/web/20180915000000*/https://mcpedl.com/simple-sides

So, after those notes to make note of, there's the point that I started using Google Drive to share my pack files. Not really a bad thing to do that, but it was worse that I didn't keep any of the updates along the way as I would make changes. So, yeah.

This is me, coming up on about nearly 4 years (4, WHAT??? wow) since making the pack, scrambling to find old versions of my resource pack throughout the web, so I can add them back into my repo that I started about two years after that. Who'da thunk it? That's a funny scenario! The lesson: DON'T DELETE YOUR BACKUPS, IT'S NOT WORTH IT.

So yeah, lost it a little. This commit is authored on August 6, 2018. Well, I'm actually writing this on April 18, 2022, which is when this was actually added to the repo. Really messy, I know. For me, I think it will be more important to have all of the history of the source code, rather than a chunk of it missing because it hadn't been tracked yet.

The first real commit to the repo will be the commit "Initial Upload", as that was when I first made the repo on GitHub, "back" in 2020 (back, being reference to when I wrote this, 2022).

Okay so the jist of all this, please don't delete your backups while you can have them. I have been scrambling through Internet Archive saves and MediaFire links to find any remnants of Dark Mode from the pre-Git days, and it has been confusing and difficult. Before my first version uploaded to MCPEDL, I have no history to show for that. It's gone to the wind. The only echoes that are left of it are what's still in the pack today. It's not that big of a deal, as I still have everything that came after that, but I don't have any of the early days.

It's kind of confusing that a ton of the textures will show up in the next commit, that's not how it went.

I am so glad that I learned from this though. Had I not kept all of my versions of Smart Text Editor around from the early days, that would've been a bummer. I think I'm reflecting on this so much because I'm looking at the old versions of the project before I learned all of my own programming techniques, and it's painful! I will have to do the same process for Simple Sides, and I surely can't wait to do that, haha! It would be great to have all of the features saved from over the years, it was just in reach.

Welp, this should be a blog or something. Sorry for the long commit message. Maybe you got something out of it?

If you read all of that, great job. Make sure to save your code history to your repository before brushing your teeth, it'll keep the cavities away!

Signing off! (You should listen to "Somewhere In This Universe Someone Hits A Drum", I found that back in 2020, and it is a FANTASTIC album!)
Brandon Bennett

---
## [Offroaders123/Dark-Mode](https://github.com/Offroaders123/Dark-Mode)@[ae5c7946b6...](https://github.com/Offroaders123/Dark-Mode/commit/ae5c7946b6e994bbe168549dbbc9e95ee05231fc)
#### Tuesday 2022-04-19 09:03:24 by Offroaders123

World Screenshot Styling + GUI Texture Adjustments

An incremental update for Bedrock, as well as for Dark Mode!

Additions:
- Added improved default screenshots for the Create New World / Edit World screens! Funny note: These use my Faithful port in the background world screenshot, so it's incorrectly not quite Vanilla... This was a silly overlook on my part, and it was actually in the pack for a long time! I liked the screenshots a lot, and it didn't cross my mind that they weren't Vanilla textures in the background, for a Vanilla pack, mind you! Now I want to try making some of these for the modern version of the pack, that would look great! *Edit: Well, I guess those makes sense for the Faithful subpack, but I was talking about the Vanilla one, hehe.
- Added improved styling for the border around the world snapshot on the Create New World / Edit World screens.

Changes:
- Updated the pack manifest to the latest release version!

Fixes:
- Adjusted the overlay cutouts for the Mob Effect Tab textures so that they will work on the top and bottom of the dialogs, when applicable.
- A few more texture adjustments for the Text Box textures in the Faithful subpack.

---
## [griwes/reaveros](https://github.com/griwes/reaveros)@[f405329376...](https://github.com/griwes/reaveros/commit/f405329376cd3d2a685c52c12748355383aeb7c0)
#### Tuesday 2022-04-19 09:10:47 by Michał 'Griwes' Dominiak

Initial implementation of ELF loading and linking.

This commit contains a toolchain crime - it makes the toolchain files
pretend that the target system is a Linux. This is because Clang's
driver is doing something extremely stupid and invoking the linking step
*through GCC* when it doesn't recognize the target, and it also does it
*incorrectly*, because --sysroot gets lost somewhere. Because we now
need to *correctly* link some shared objects, and because doing it
through ld.lld directly is much more of a pain than this hack, we'll do
the hack for this. *Before this is merged*, however, the branch should
also receive a commit that patches LLVM to understand
*-reaveros-{elf,kernel} target triples, but that is going to be way more
involved than I have time, energy, and space in this commit for.

This commit also modifies how blocking syscalls lock memory ranges; the
locks no longer persist across suspensions. This is because I'm also
adding a mapping unmap syscall which needs a unique ownership of a
mapping, and it was either this or making unmap itself blocking, and
making mappings have thread queues on their locks. I chose the simpler
approach. Also also, the mapping lock type is now a shared mutex, as it
should've been from the start.

Finally - the first actual userspace process will be a logger, not a
vasmgr. This is to bring the number of binaries that need to contain the
"send some pointers over a mailbox to a kernel thread" logging mechanism
to its bare minimum. This way, all the other processes will start by
immediately using the logger IPC protocol, which will make them simpler
in this regard.

---
## [emacsmirror/evil-tex](https://github.com/emacsmirror/evil-tex)@[cf58bc5aea...](https://github.com/emacsmirror/evil-tex/commit/cf58bc5aeab46fb1d08d22c799e2d0f714923bdb)
#### Tuesday 2022-04-19 09:56:38 by Dan Kessler

fix regex used in evil-tex-toggle-delim

Previously, it would match anything that had a slash followed optionally by a
balancing keyword followed optionally by l, which would mess up how it matched
things like \{ or \|

Currently, the regex it uses to decide if the delimiters are already
balanced (based just on the initial one) is:

"\\\\\\(?:left\\|big\\|bigg\\|Big\\|Bigg\\)?l?"

(note: all regexes here are taken from elisp so have extra backslashes for
string escapes)

The trouble is that this matches *anything* that has a slash, since everything
that follows is optional. For example, if you have math like $ \{ x \} $ and you
run evil-tex-toggle-delim, then this *will* match (just the literal backslash),
causing it to think that it is already size balanced, and then "toggling" will
just strip the backslash rather than prepending \left and \right.

This could be fixed by changing it to

"\\\\\\(?:\\(left\\|big\\|bigg\\|Big\\|Bigg\\)\\|l\\)"

This extra level of grouping means that it only matches if there is a literal
backslash followed by *either* one of the balancing keywords OR l. This way it
has to match something in the second part, and this will not match \{

However, I think that trailing (optional) l is perhaps a mistake. I assume it is
there to catch things like \langle, but this will then toggle \langle to
angle (which without the slash is not a macro). Moreover, \langle and
\rangle (or similarly \lvert and \rvert, etc) are paired delimiters but they do
not automatically resize (at least not for me), I instead need to do
\left\langle if I want that behavior. For that reason, I think the trailing l
should be cut, and the final regex is just

"\\\\\\(?:left\\|big\\|bigg\\|Big\\|Bigg\\)"

---
## [disappointedButNotSuprised/tgstation](https://github.com/disappointedButNotSuprised/tgstation)@[351afe260b...](https://github.com/disappointedButNotSuprised/tgstation/commit/351afe260b42764641a07385df5f7e24b840f631)
#### Tuesday 2022-04-19 10:17:49 by san7890

Fixes Mapping Icons For Bodylimbs (Don't Get A Shock!) (#65899)

* Fixes Mapping Icons For Bodylimbs (Don't Get A Shock!)

Hey there,

I implore you look at this photograph right here:

Ugly stupid base broken dumb /obj instead of the actual sprite fucking garbage idiotic purple-white square damn it i hate it so much fuck fuck fuck fuck let's fix it before the fire under my seat gets worse argh

Anyways, I checked with Kapu and did a bit of testing, and I managed to figure out a way to get the best of both the mapping world and the in-game world. Don't believe me? Check these out:

* addressses review

things still work

* kills female moth chests

---
## [jsdbroughton/speckle-sketchup](https://github.com/jsdbroughton/speckle-sketchup)@[9b5c043029...](https://github.com/jsdbroughton/speckle-sketchup/commit/9b5c043029fc93b3a0bc422c16b30fb0c9196a38)
#### Tuesday 2022-04-19 10:18:39 by izzy lyseggen

feat(ui): saved streams & 1-click send (#37)

* feat(ui): saved streams and wip 1 click

* style(connector): remove some puts statements

* feat(accounts): default acct helper

* feat(ui): more 1 click send

need a way to wait for connector launch...

* fix(ui): waiting quick send!

* feat(ui): view in web from toast notif

note to self: the one in frontend is kinda ugly 😓 
went with outine btn for now bc it was better than that big ol dark gray btn

* fix: turn off dev

i always fkn do this i needa just use an env file gdi

* feat(ui): notify ui of oneclick send

* feat(metrics): remove old and use the new!

---
## [toligrimm/new_todo_dismiss](https://github.com/toligrimm/new_todo_dismiss)@[7a9b49203c...](https://github.com/toligrimm/new_todo_dismiss/commit/7a9b49203c6b170143a0093bc47dacbb044dfb39)
#### Tuesday 2022-04-19 11:17:37 by toligrimm

Merge pull request #1 from toligrimm/bottomnavigator

fuck you

---
## [Offroaders123/Dark-Mode](https://github.com/Offroaders123/Dark-Mode)@[c5fe152bbb...](https://github.com/Offroaders123/Dark-Mode/commit/c5fe152bbb7ad07b44e374031d5bbd8ff4bddb78)
#### Tuesday 2022-04-19 11:21:32 by Offroaders123

The Monumental Rebase

Alright, can't believe I just pulled that off. I rebased all of Dark Mode's pre-Git history to the start of the repo. With correct dates, changelogs, and everything. That took a long time to do. I had to work on it every once in a while over the last few months.

If you want to learn about why it was so hard to do, go to the first commit, "Initial Commit!". I wrote a way-too-long few lines about the Dark Mode journey, and how it sums up to today!

Sorry for the lack of content updates recently, this had been the main reason why. I have really been wanting the get the rest of the project's history into the repo, one way or another.

Some of the updates along the way, through mid-2019, were lost to the fire, but I think I caught a great deal of the amount of time and effort that came before the repo too :)

Thanks for coming along for this wild ride, seeya again soon! I really gotta start going to bed earlier.
Brandon Bennett

Oh yeah, and the changelog for this one:

Changes:
- Updated the README to the current year! Welcome to 2022, in April XD

---
## [CrypticzXI/MBedwars_SpawnRates](https://github.com/CrypticzXI/MBedwars_SpawnRates)@[1f60c60036...](https://github.com/CrypticzXI/MBedwars_SpawnRates/commit/1f60c600368fb88a267811aec8a2f1ffbf8ddfb1)
#### Tuesday 2022-04-19 11:25:08 by CrypticzXI

Thank you marcel for being a shit dev. You made me copy a fucking shit clone you stupid man

---
## [trollertroll/Merchant-Station-13](https://github.com/trollertroll/Merchant-Station-13)@[2ccc1ac83b...](https://github.com/trollertroll/Merchant-Station-13/commit/2ccc1ac83bc17434ffc375ec852632c7276d062a)
#### Tuesday 2022-04-19 11:58:57 by troller

Adds simpson skin tone

The sign is a subtle joke. The shop is called "Sneed's Feed & Seed", where feed and seed both end in the sound "-eed", thus rhyming with the name of the owner, Sneed. The sign says that the shop was "Formerly Chuck's", implying that the two words beginning with "F" and "S" would have ended with "-uck", rhyming with "Chuck". So, when Chuck owned the shop, it would have been called "Chuck's Fuck and Suck".

---
## [freedesktop/NetworkManager](https://github.com/freedesktop/NetworkManager)@[2a0231469f...](https://github.com/freedesktop/NetworkManager/commit/2a0231469fe7d783543a71824aedb4a32eb3beb0)
#### Tuesday 2022-04-19 12:52:23 by Lubomir Rintel

nmcli.h: tidy up boolean struct members

Use bitfields to save a few bytes. This involves swapping gboolean for
bool and some reordering in order to get them grouped together.

The patch looks horrible, because clang-format decides to put itself and
seem to go out of its way to make this whole file look idiotic.
What can you do.

---
## [ahmedibrahim404/RC4Community](https://github.com/ahmedibrahim404/RC4Community)@[ddc933b9cc...](https://github.com/ahmedibrahim404/RC4Community/commit/ddc933b9cc0e4d53f4041682d01789ee8477ee0a)
#### Tuesday 2022-04-19 14:30:51 by Sidharth Mohanty

Official Project License Christening Commit (#147)

@sidmohanty11  was nominated by @Dnouv  and seconded unanimously by all in attendance for creating this milestone commit:

@sidmohanty11 @samad-yar-khan @demonicirfan @Sing-Li @RonLek @Dnouv 

On this "Good Friday 2022"  team members meeting,  @Sing-Li was moved to tears by the open source team spirit and camaraderie displayed (seldom seen in "day job" meetings nowadays)  Thanks for sharing  ! :pray: all !

License choice was voted on by team members (between Apache 2, MIT and GPL):

@sidmohanty11 @samad-yar-khan  @demonicirfan @Sing-Li  @RonLek  @Dnouv @debdutdeb @dudanogueira @abhinavkrin @engelgabriel 

All team members - please post a daytime bitmap of an environment near you  (on this comment)  to "remember this time".    Thanks.

---
## [wolframowy/tgstation](https://github.com/wolframowy/tgstation)@[55336d1e53...](https://github.com/wolframowy/tgstation/commit/55336d1e5308789be1616413c8d8f87e073f7302)
#### Tuesday 2022-04-19 14:44:37 by vincentiusvin

Atmos Control Console Refactor (and syndiebase atmos tidyup) (#65372)

Main Takeaways For Mappers:

Use monitored pathed atmos devices very carefully. Also dont put atmos_sensors willy nilly. They are used to hook to atmos control monitors.

We want to keep at most one device broadcasting for each of the atmos sensor, inlets, and outlets. Run the mapping verb Check Atmos Chamber Devices to be sure, though this might not catch everything.

Some of the warning are pretty harmless. For example if you have reconnected the "station atmos monitor" and you get no listener for distro/waste loop warning, it's safe to ignore.

I don't know what the maptainer policy is on making new subtypes for offstation content, but if you do please branch off the general ones instead of the specific gas ones. If you aren't making a new subtype, varedit the general ones too.

About The Pull Request:

Need Would prefer this to be merged before #65271 (In game atmos guide).
Not strictly necessary, just makes me sleep better knowing the handbook wont die alongside the rest of the UI.

Fixes #36668 (Atmos Monitoring Consoles don't update it's sensors to the new tank after reconnect())
Fixes #32122 (Mix console fucked after reconnecting it)

Also made the distro meter thing broadcast more info instead of just the pressure, because I'm sure nobody would care and it would make my life easier.

A small high-level overview in case this breaks again in the future:

A signal datum (not DCS) is sent by the atmospheric devices (injectors and vents) and will be received by the atmos computers. The data is then stored at the monitor object and then passed to the UI. This initial signal is sent by `broadcast_signal()`, called by `atmos_init()`.

New sensors/vents (if you can actually get them in game, still only adminspawn/wrenchables afaik) will also initiate the conversation if atmos_init() is called, so it works fine. This means you need to unwrench and re-wrench the devices if you adminspawn them though, ugh.

In case of a newly built computer, it needs to be the one that prompt the data to the devices, so we send a request signal. This is a bit inefficient since it doesnt work off of callbacks and assocs like DCS, but won't really matter since we're doing this rarely.

We only talk with the injectors and vents when necessary here, while sensors and meters keep beeping with every process_atmos() tick so they rarely break.


Why It's Good For The Game:

Messy code gone (debatable).


Refactored the atmos control console devices. The ones that hook to the big turf chambers.
Distro meter now broadcast the whole gasmix info instead of just pressure to the monitors.
Lavaland syndie's atmos chamber vents are now actually configurable. Moved a few things around to accomodate this.
Lavalannd syndie chambers hooked to distro and moved distro pipe to layer2
atmos monitors can detect reactions now.
Some minor code changes to how anomaly refinery and implosion compressor show the gas info. No changes expected, report if bug.
recoded checks for atmos chamber abnormalities in debug verbs.

---
## [r4lv/acts](https://github.com/r4lv/acts)@[6e1fd31474...](https://github.com/r4lv/acts/commit/6e1fd314745ae31eaddd8db8f0454b88a9aa60fa)
#### Tuesday 2022-04-19 15:15:56 by Stephen Nicholas Swatman

feat: Implement a new orthogonal range search seed finder (#904)

As I said in #901, I have been playing around with seed finding a little bit lately. Last weekend, I mentioned an idea for a new (?) kind of seed finding algorithm based on range search datastructures, and this is the very, very first semi-working implementation of it, just before the weekend.

The idea behind this algorithm is relatively simple. In traditional seedfinding, we check a whole lot of candidate spacepoints to see whether they meet some condition. If you look at this differently, each spacepoint defines a volume in the z-r-φ space, which contains any spacepoints it can form a doublet with. What if we reversed this logic? What if we defined this volume first, and then just extract the spacepoints inside of that space? That way, we can vastly reduce the number of spacepoints we need to look at.

How do we do this quickly? With [_k_-d trees](https://en.wikipedia.org/wiki/K-d_tree). These data structures are cheap to build, and they give us very fast orthogonal range searches. In other words, we can very quickly look up which of our spacepoints lie within an axis-aligned orthognal n-dimensional hyperrectangle. In this case, which spacepoints lie within a z-r-φ box.

So, the core idea of this seedfinder is to define as many of our seedfinding constraints in orthogonal fashion. That way, we can make our candidate hyperrectangle smaller and smaller. The tighter the constraints we can place, the better. Then, we look up the relevant spacepoints, and we can avoid looking at any others. That also means this solution requires no binning whatsoever.

## Constraint conversion

Currently there are quite a few constraints in the code. Here is my status update on how well it is going to convert each of them. In some cases, we can define a weaker version of the constraints in orthogonal fashion. This is still very powerful, and it doesn't actually lose us any efficiency (because we can always check the tighter constraint in a non-orthogonal way later, not a problem)!

### Unary constraints

Currently, I am not aware of any unary constraints in the Acts seed finding code. That is to say, logic to determine whether a point is allowed to be a lower spacepoint. However, I have the following thoughts about introducing some:

* I believe the binning code does some kind of magic to determine whether a spacepoint can be a lower spacepoint. Since my solution doesn't use any binning, I don't have access to this just yet. However, if we can incorporate this logic it could be very powerful.
* Maximum single-point η: we currently have some checks in place to see if the pseudorapidity of particles is not too high. We could realistically use this maximum pseudorapidity, combined with the collision region range to constrain the bottom spacepoints.

### Binary constraints

These are the existing binary constraints on spacepoint duplets:

Constraint | Description | Orthogonalization
-|-|-
Minimum ∆r | Ensure that the second spacepoint is within a certain difference in radius | Full
Maximum cot θ | Ensure that the pseudorapidity of the duplet is not too high | Unsuccessful
z-origin range | Ensure that the duplet would have originated from the collision point | Weakened 
Maximum ∆φ<sup>1</sup> | Ensure that the duplet does not bend too much in the x-y plane | Full

<sup>1</sup> This check does not exist explicitly in the existing seed finder, but is implicit in the binning process.

### Ternary constraints

There are a lot of ternary constraints (to check whether a triplet is valid):

Constraint | Description | Orthogonalization
-|-|-
Scattering angle | ??? | Unsuccessful
Helix diameter | Ensure the helix diameter is within some range | In progress
Impact parameters | Ensure the impact parameters are close to the collision point | In progress
Monotonic z<sup>1</sup> | Ensure that z increases or decreases monotonically between points | Full

<sup>1</sup> This check does not exist in the existing seed finder, check #901.

There are also constraints defined in the experiment-specific cuts, and the seed filter, and in other places. If we could convert some of those to orthogonal constraints the implementation would become much more powerful. However, I don't really understand what is happening in those files just yet. Need more reading.

## Current performance

The current performance of this seedfinder is... Complicated. On my machine, it runs a 4000 π<sup>+</sup> event in about 5 seconds, three times slower than the existing seedfinder. Its efficiency is much higher though, and the fake rate is much lower. So that's something. However, that is in part because I am creating far more seed candidates, so take this with a big grain of salt.

## Potential gain

There are two ways that I can think of to use this kind of algorithm. The first is an inside-to-outside algorithm, where we pick a lower spacepoint first, check the space it defines for a middle spacepoint, and then check the space the two of them define for a third spacepoint. This algorithm has time complexity 𝒪(_n_<sup>3</sup>), and it has space complexity 𝒪(_n_). Due to the constants, I still believe this implementation can outperform the 𝒪(_n_<sup>2</sup>) existing algorithm, however.

The second way would be to construct a set of duplets using this logic, and then to fit those together like we do with traditional seedfinding. This has 𝒪(_n_<sup>2</sup>) time complexity like the existing code, but also space complexity 𝒪(_n_<sup>2</sup>).

## Things that are completed

* The implementation of the _k_-d tree seems to work very well, and it is quite fast.
* Basic seedfinding using this strategy is functional.

## Things that don't work yet

* My maximum ∆φ constraint does not cross the 2π boundary yet.
* I used the existing seedfinding algorithm as a stepping stone, which I have completely destroyed in the process. Obviously I do not intend on keeping it that way, and the existing algorithm will be restored to its full glory.
* Lots more.

## Things that can be improved

* Add more constraints, and tighten existing ones.
* Lots of things, pretty much everything. But I really want to go home for the weekend, so I will write this part next week.

---
## [CombineSlayer24/Manhunt-SNPC](https://github.com/CombineSlayer24/Manhunt-SNPC)@[c59b886b00...](https://github.com/CombineSlayer24/Manhunt-SNPC/commit/c59b886b00c99b6615247bddb7d1479a6978eddd)
#### Tuesday 2022-04-19 16:43:29 by CombineSlayer24

Pickups rework

• Painkillers now show a message when attempting to use it on full health.
• Removed useless, garbage code.
• Fixed the god awful spacing (thanks to VSC for screwing up the spacing for some odd reason)

---
## [mbs-octoml/mbs-tvm](https://github.com/mbs-octoml/mbs-tvm)@[ecdf419a17...](https://github.com/mbs-octoml/mbs-tvm/commit/ecdf419a173b2875288e58858d933265ce6fc881)
#### Tuesday 2022-04-19 17:16:19 by Mark Shields

** Collage v2 sketch ***

- Enable cudnn, get rid of support for op-predicate based BYOC integrations
- Enable cublas
- And yet another go at pruning unnecessary candidates.
- Another go at pruning unnecessary candidates
- Fix CompositePartitionRule use
- Fix a few bugs with new TensorRT pattern-based integration
- Rework RemoveSubCandidatesCombinerRule for soundness
- Better logging
- Bug fixes
- Implement critical nodes idea for avoiding obviously unnecessary candidates
- Promote DataflowGraph from alias to class so can cache downstream index set
- Quick check to avoid unioning candidates which would create a cycle
- Host out CandidatePartitionIndex and add rules to avoid small candidates subsumed by containing candidates
- GetFunction can legitimately return nullptr
- rename tuning log
- Support for int64 literals
- Switch GPT2 to plain model
- Fix library cloberring issue for cutlass
- actually checkin 'built in' tuning log (covers mnist & gpt2 only)
- trying to debug gpt2
- Update TargetKind attribute name
- working through gpt2 issues
- checkin tuning records for MNIST (with hack to not retry failed winograd)
- Autotvm tuning disabled if log file empty (default)
- Autotvm tuning during search working
- tune during search
  (but does not load tuned records after search!)
- About to add tuning to estimate_seconds
- Split out the combiner rules & make them FFI friendly
- Rework comments
- Estimate IRModule instead of Function (closer to meta_schedule iface)
- Add 'host' as first-class partitioning spec
  (Avoids special casing for the 'leave behind for the VM' case)
- Move CollagePartitioner to very start of VM compiler flow (not changing legacy)
- Fix bugs etc with new SubGraph::Rewrite approach
  Ready for updating RFC to focus on partitioning instead of fusion.
- Working again after partition<->fusion split.
- Add PrimitivePartitionRule
- Refactor SubGraph Extract/Rewrite
  *** CAUTION: Almost certainly broken ***
- Rename kernel->partition, fusion->partition
- Next: make nesting in "Primitive" an explicit transform
- respect existing target constraints from device planner
- make 'compiler' and 'fusion_rule' attributes avail on all target kinds
- moved design to tvm-rfcs, https://github.com/apache/tvm-rfcs/pull/62
- incorporate comments
- avoid repeated fusion
- fix trt type checking
- better logs
- pretty print primitive rules
- fix tensorrt
- multiple targets per spec
- don't extract candidate function until need cost
  Need to bring CombineByPrimitives back under control since lost depth limit.
- cleaned up fusion rule names
- added 'fuse anything touching' for BYOC
- Finish dd example
- Add notion of 'MustLower', even if a candidate fires may still need to consider
  leaving node behind for VM (especially for constants).
- starting example
- finished all the dd sections
- documentation checkpoint
- docs checkpoint
- more design
- starting on dd
- runs MNIST with TVM+CUTLASS+TRT
- cutlass function-at-a-time build
- need to account for build_cutlass_kernels_vm
- move cutlass tuning into relay.ext.cutlass path to avoid special case
- add utils
- don't fuse non-scalar constants for tvm target.
- stuck on cuda mem failure on conv2d, suspect bug in main
- where do the cutlass attrs come from?
- running, roughtly
- pretty printing, signs of life
- wire things up again
- Switch SubGraph and CandidateKernel to TVM objects
- naive CombineByKindFusionRule, just to see what we're up agaist
  Will switch to Object/ObjectRef for SubGraph and CandidateKernel to avoid excess copying.
- preparing to mimic FuseOps
- rework SubGraph to use IndexSet
- rough cut at MaximalFusion
- split SubGraph and IndexSet in preparation for caching input/output/entry/exit sets in SubGraph.
- top-down iterative handling of sub-sub-graphs
- about to give up on one-pass extraction with 'sub-sub-graphs'
- Add notion of 'labels' to sub-graphs
- Rework FusionRules to be more compositional
- partway through reworking fusion rules, broken
- SubGraph::IsValid, but still need to add no_taps check
- dataflow rework, preparing for SubGraph::IsValid
- explode into subdir
- mnist with one fusion rule (which fires twice) working
- switch to CandidateKernelIndex
- Confirm can measure 'pre-annotated' primitive functions
- checkpoint
- stuff
- more sketching
- dominator logging

---
## [Anas84464/Bike-Sharing-Demand-Prediction](https://github.com/Anas84464/Bike-Sharing-Demand-Prediction)@[9b46937234...](https://github.com/Anas84464/Bike-Sharing-Demand-Prediction/commit/9b469372348c625b571e6b1e5ea9369ead336314)
#### Tuesday 2022-04-19 17:25:58 by Anas Mustafa

Update README.md

SEOUL RENTAL BIKE DEMAND PREDICTION
                                                            Data science trainee,
AlmaBetter, Bangalore



Abstract:
As more number of rented bikes are being used in the cities nowadays, it becomes important for the company to predict the number of required rental bikes required across a day so that no demand supply gap would be generated for rental bikes. This project aims at providing necessary solution to predict the rental bikes demand using machine learning algorithms so that all the stakeholders of the business can be satisfied.


Problem Statement:
Currently Rental bikes are introduced in many urban cities for the enhancement of mobility comfort. It is important to make the rental bike available and accessible to the public at the right time as it lessens the waiting time. Eventually, providing the city with a stable supply of rental bikes becomes a major concern. The cru cial part is the prediction of bike count required at each hour for the stable supply of rental bikes.



Variables
•	Date : year-month-day
•	Rented Bike count - Count of bikes rented at each hour
•	Hour - Hour of the day
•	Temperature-Temperature in Celsius
•	Humidity - %
•	Wind speed - m/s
•	Visibility - 10m
•	Dew point temperature - Celsius
•	Solar radiation - MJ/m2
•	Rainfall - mm
•	Snowfall - cm
•	Seasons - Winter, Spring, Summer, Autumn
•	Holiday - Holiday/No holiday
•	Functional Day - NoFunc(Non Functional Hours), Fun(Functional hours)


Introduction
The present scenario is about how good is the customer service in any industry as the number of options at the customer’s disposal is unlimited. So, it becomes extremely important to make sure that the customers will not be made to wait for the rental bikes. It would also not be practical to keep lot of bikes even when the demand is low. Hence, with the help of machine learning, this project aims at predicting the rental bike demand so that no problems arise.

Steps involved:

	Exploratory Data Analysis:
The first step of our project is performing the EDA process on the dataset so that we can get the idea about the dataset i.e. the number of variables, the data type of the variables , visualize the dataset for Better understanding and decide the suitable methods and algorithms that might produce desired outcomes

	Data Preprocessing:
In EDA process we find the type of dataset and decide the approach, in this project the preprocessing steps would removing the punctuations, stopwords , generate count vectorizer and document term matrix which would help in building up the model.

	Building Machine Learning Model:
After the data preprocessing is done then the data will be ready to be fit into machine learning models .For current problem statement topic modeling approach would be suitable . In topic modeling, a topic is defined by a cluster of words with each word in the cluster having a probability of occurrence for the given topic, and different topics have their respective clusters of words along with corresponding probabilities.

 Summary:
At last the summary of the project is described to have brief look over the project.

Algorithms:
        
        Linear Regression:
Linear regression is one of the easiest and most popular Machine Learning algorithms. It is a statistical method that is used for predictive analysis. Linear regression makes predictions for continuous/real or numeric variables such as sales, salary, age, product price, etc.

Linear regression algorithm shows a linear relationship between a dependent (y) and one or more independent (y) variables, hence called as linear regression. Since linear regression shows the linear relationship, which means it finds how the value of the dependent variable is changing according to the value of the independent variable.

The linear regression model provides a sloped straight line representing the relationship between the variables. Consider the below image:


 
 
y= a0+a1x+ ε

Here,
Y= Dependent Variable (Target Variable)
X= Independent Variable (predictor Variable)
a0= intercept of the line (Gives an additional degree of freedom)
a1 = Linear regression coefficient (scale factor to each input value).
ε = random error
The values for x and y variables are training datasets for Linear Regression model representation.



 Ridge Regression (L2 Regularization)
This technique performs L2 regularization. The main algorithm behind this is to modify the RSS by adding the penalty which is equivalent to the square of the magnitude of coefficients. However, it is considered to be a technique used when the info suffers from multicollinearity (independent variables are highly correlated). In multicollinearity, albeit the smallest amount squares estimates (OLS) are unbiased, their variances are large which deviates the observed value faraway from truth value. By adding a degree of bias to the regression estimates, ridge regression reduces the quality errors. It tends to solve the multicollinearity problem through shrinkage parameter λ. Now, let us have a look at the equation below.
 
In this equation, we have two components. The foremost one denotes the least square term and later one is lambda of the summation of β2 (beta- square) where β is the coefficient. This is added to least square term so as to shrink the parameter to possess a really low variance.
Every technique has some pros and cons, so as Ridge regression. It decreases the complexity of a model but does not reduce the number of variables since it never leads to a coefficient tending to zero rather only minimizes it. Hence, this model is not a good fit for feature reduction.


 Lasso Regression (L1 Regularization)
This regularization technique performs L1 regularization. Unlike Ridge Regression, it modifies the RSS by adding the penalty (shrinkage quantity) equivalent to the sum of the absolute value of coefficients.
Looking at the equation below, we can observe that similar to Ridge Regression, Lasso (Least Absolute Shrinkage and Selection Operator) also penalizes the absolute size of the regression coefficients. In addition to this, it is quite capable of reducing the variability and improving the accuracy of linear regression models.

 
Limitation of Lasso Regression:
•	If the number of predictors (p) is greater than the number of observations (n), Lasso will pick at most n predictors as non-zero, even if all predictors are relevant (or may be used in the test set). In such cases, Lasso sometimes really has to struggle with such types of data.
•	If there are two or more highly collinear variables, then LASSO regression select one of them randomly which is not good for the interpretation of data.
•	Lasso regression differs from ridge regression in a way that it uses absolute values within the penalty function, rather than that of squares. This leads to penalizing (or equivalently constraining the sum of the absolute values of the estimates) values which causes some of the parameter estimates to turn out exactly zero. The more penalty is applied, the more the estimates get shrunk towards absolute zero. This helps to variable selection out of given range of n variables. 

Elastic Net Regression
Elastic net linear regression uses the penalties from both the lasso and ridge techniques to regularize regression models. The technique combines both the lasso and ridge regression methods by learning from their shortcomings to improve the regularization of statistical models.
 
 
 
The elastic net method improves lasso’s limitations, i.e., where lasso takes a few samples for high dimensional data. The elastic net procedure provides the inclusion of “n” number of variables until saturation. If the variables are highly correlated groups, lasso tends to choose one variable from such groups and ignore the rest entirely.
To eliminate the limitations found in lasso, the elastic net includes a quadratic expression (||β||2) in the penalty, which, when used in isolation, becomes ridge regression. The quadratic expression in the penalty elevates the loss function toward being convex. The elastic net draws on the best of both worlds – i.e., lasso and ridge regression.
In the procedure for finding the elastic net method’s estimator, two stages involve both the lasso and regression techniques. It first finds the ridge regression coefficients and then conducts the second step by using a lasso sort of shrinkage of the coefficients.
This method, therefore, subjects the coefficients to two types of shrinkages. The double shrinkage from the naïve version of the elastic net causes low efficiency in predictability and high bias. To correct for such effects, the coefficients are rescaled by multiplying them by (1+λ2).
 Summary
•	The elastic net method performs variable selection and regularization simultaneously.
•	The elastic net technique is most appropriate where the dimensional data is greater than the number of samples used.
•	Groupings and variables selection are the key roles of the elastic net technique.


Decision Tree

	Decision Tree is a Supervised learning technique that can be used for both classification and Regression problems. It is a tree-structured classifier, where internal nodes represent the features of a dataset, branches represent the decision rules and each leaf node represents the outcome.

	In a Decision tree, there are two nodes, which are the Decision node and Leaf node. Decision nodes are used to make any decision and have multiple branches, whereas Leaf nodes are the output of those decisions and do not contain any further branches.
	The decisions or the test are performed on the basis of features of the given dataset.
	It is a graphical representation for getting all the possible solutions to a problem/decision based on given conditions.


Fig 1.General structure of decision tree

Random Forest:

	Random Forest is a popular machine learning algorithm that belongs to the supervised learning technique. It can be used for both Classification and Regression problems in ML. It is based on the concept of ensemble learning, which is a process of combining multiple classifiers to solve a complex problem and to improve the performance of the model.
	Random Forest is a classifier that contains a number of decision trees on various subsets of the given dataset and takes the average to improve the predictive accuracy of that dataset. Instead of relying on one decision tree, the random forest takes the prediction from each tree and based on the majority votes of predictions, and it predicts the final output.
	The greater number of trees in the random forest leads to higher accuracy and prevents the problem of overfitting.




 Fig 2. Working of Random Forest






Gradient Boosting :

Gradient Boosting is a popular boosting algorithm. In gradient boosting, each predictor corrects its predecessor’s error. In contrast to Adaboost, the weights of the training instances are not tweaked, instead, each predictor is trained using the residual errors of predecessor as labels.
There is a technique called the Gradient Boosted Trees whose base learner is CART (Classification and Regression Trees).








The below diagram explains how gradient boosted trees are trained for regression problems.
 
Gradient Boosted Trees for Regression
The ensemble consists of N trees. Tree1 is trained using the feature matrix X and the labels y. The predictions labelled y1(hat) are used to determine the training set residual errors r1. Tree2 is then trained using the feature matrix X and the residual errors r1 of Tree1 as labels. The predicted results r1(hat) are then used to determine the residual r2. The process is repeated until all the N trees forming the ensemble are trained.
There is an important parameter used in this technique known as Shrinkage.
Shrinkage refers to the fact that the prediction of each tree in the ensemble is shrunk after it is multiplied by the learning rate (eta) which ranges between 0 to 1. There is a trade-off between eta and number of estimators, decreasing learning rate needs to be compensated with increasing estimators in order to reach certain model performance. Since all trees are trained now, predictions can be made.
Each tree predicts a label and final prediction is given by the formula,
y(pred) = y1 + (eta *  r1) + (eta * r2) + ....... + (eta * rN)



 XGBoost:

	XGBoost is an ensemble learning method. Sometimes, it may not be sufficient to rely upon the results of just one machine learning model.
	Ensemble learning offers a systematic solution to combine the predictive power of multiple learners. The resultant is a single model which gives the aggregated output from several models.
	XGBoost is one of the fastest implementations of gradient boosting trees. It does this by tackling one of the major inefficiencies of gradient boosted trees: considering the potential loss for all possible splits to create a new branch (especially if you consider the case where there are thousands of features, and therefore thousands of possible splits).
	XGBoost tackles this inefficiency by looking at the distribution of features across all data points in a leaf and using this information to reduce the search space of possible feature splits. 
Model performance:

•	Mean Squared Error:

Mean Squared Error, or MSE for short, is a popular error metric for regression problems.
It is also an important loss function for algorithms fit or optimized using the least squares framing of a regression problem. Here “least squares” refers to minimizing the mean squared error between predictions and expected values.
The MSE is calculated as the mean or average of the squared differences between predicted and expected target values in a dataset.
	
MSE = 1 / N * sum for i to N (y_i – yhat_i) ^2.

Where y_i is the i’th expected value in the dataset and yhat_i is the i’th predicted value. The difference between these two values is squared, which has the effect of removing the sign, resulting in a positive error value.



R2 score:

R2 score is a metric that tells the performance of your model, not the loss in an absolute sense that how many wells did your model performs. In contrast, MAE and MSE depend on the context as we have seen whereas the R2 score is independent of context. So, with help of R squared we have a baseline model to compare a model which none of the other metrics provides. The same we have in classification problems which we call a threshold which is fixed at 0.5. So basically R2 squared calculates how must regression line is better than a mean line. But how to interpret R2 score. The normal case is when the R2 score is between zero and one like 0.8 which means your model is capable to explain 80 per cent of the variance of data.













Adjusted R-squared
For a multiple regression model, R-squared increases or remains the same as we add new predictors to the model, even if the newly added predictors are independent of the target variable and don’t add any value to the predicting power of the model. Adjusted R-squared eliminates this drawback of R-squared. It only increases if the newly added predictor improves the model’s predicting power. Adding independent and irrelevant predictors to a regression model results in a decrease in the adjusted R-squared.
 


Hyper parameter tuning:

Grid Search CV
Grid Search combines a selection of hyper parameters established by the scientist and runs through all of them to evaluate the model’s performance. Its advantage is that it is a simple technique that will go through all the programmed combinations. The biggest disadvantage is that it traverses a specific region of the parameter space and cannot understand which movement or which region of the space is important to optimize the model.


Conclusion:
The project comes to an end at this point. Beginning with loading the dataset, so far we have done EDA, pre-processing the data, Label encoding, Scaling the data, splitting the data into train and test data, applying various machine learning algorithms followed by hyper parameter tuning. We implemented 8 M.L. models. After comparing the mean square error and  mean root square error of all the models, XGBoost has least mean square  error and root mean square error. XGBoost has highest accuracy of 91.9%  among all algorithms. So, We can conclude that XGBoost is the best model  to predict rented bike count. The number of business hours of the day and the demand for rented bikes  were most correlated and It makes sense also. Highest number of  bike  rented at the 18th hour of day. Total number of bike count increased when there was favourable  temperature. So, this can be an important factor in predicting underlying  patterns of rented bike count.

---
## [samay-sharma/postgres](https://github.com/samay-sharma/postgres)@[ec62cb0aac...](https://github.com/samay-sharma/postgres/commit/ec62cb0aac5ba31a82339606009ddbd7eb00e2ac)
#### Tuesday 2022-04-19 17:56:20 by Tom Lane

Revert applying column aliases to the output of whole-row Vars.

In commit bf7ca1587, I had the bright idea that we could make the
result of a whole-row Var (that is, foo.*) track any column aliases
that had been applied to the FROM entry the Var refers to.  However,
that's not terribly logically consistent, because now the output of
the Var is no longer of the named composite type that the Var claims
to emit.  bf7ca1587 tried to handle that by changing the output
tuple values to be labeled with a blessed RECORD type, but that's
really pretty disastrous: we can wind up storing such tuples onto
disk, whereupon they're not readable by other sessions.

The only practical fix I can see is to give up on what bf7ca1587
tried to do, and say that the column names of tuples produced by
a whole-row Var are always those of the underlying named composite
type, query aliases or no.  While this introduces some inconsistencies,
it removes others, so it's not that awful in the abstract.  What *is*
kind of awful is to make such a behavioral change in a back-patched
bug fix.  But corrupt data is worse, so back-patched it will be.

(A workaround available to anyone who's unhappy about this is to
introduce an extra level of sub-SELECT, so that the whole-row Var is
referring to the sub-SELECT's output and not to a named table type.
Then the Var is of type RECORD to begin with and there's no issue.)

Per report from Miles Delahunty.  The faulty commit dates to 9.5,
so back-patch to all supported branches.

Discussion: https://postgr.es/m/2950001.1638729947@sss.pgh.pa.us

---
## [larentoun/Skyrat-tg](https://github.com/larentoun/Skyrat-tg)@[cd2bd18cf8...](https://github.com/larentoun/Skyrat-tg/commit/cd2bd18cf8193c7cfc2f0014ef449baa8792aad4)
#### Tuesday 2022-04-19 18:03:55 by SkyratBot

[MIRROR] Creates Linters for (bad) Commented Out Lines in Maps [MDB IGNORE] (#12543)

* Creates Linters for (bad) Commented Out Lines in Maps (#65888)

* Creates CI Linters for Commented Out Lines in Maps

Creates Linters for (bad) Commented Out Lines in Maps

Hey there,

This PR is made because what happened in #65837 was fucking horrible awful shit that I'm still dealing with a few days after I fixed it. This _should hopefully_ add a new linter for commented out lines of code in a .DMM file, and HOPEFULLY doesn't flag the commented line that prevents unwanted TGM > DMM conversion.

As a proof to see if it works, I'll be adding a comment to Line 2 of IcemoonUnderground_Above.dmm. Hopefully, on the first CI check, it'll fail. I'll remove that line so it doesn't make its way into production (it will suck).

* Creates Linters for (bad) Commented Out Lines in Maps

Co-authored-by: san7890 <34697715+san7890@users.noreply.github.com>

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[8d3cddc6a8...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/8d3cddc6a8bcf438d8f3ca18eefe7e27ca40e06c)
#### Tuesday 2022-04-19 18:24:31 by SkyratBot

[MIRROR] NukeOps Firebase Rework [MDB IGNORE] (#12861)

* NukeOps Firebase Rework (#66149)

Attention Recruit: Welcome to Firebase Balthazord
Here you will lean how to:
-Kill corpo scum
-Kill corpo scum
-Kill corpo scu-

This has been on my docket for months. Ever since gave the Holding Facility a much needed facelift. I have been eyeballing the nukie base, waiting for that stroke of inspiration to hit me. It finally did. Gone are the aging walls of the old encampment. Nukies finally have what well-funded corpo-terrorists always dream of- a home.

It's more than a Home. This is a sweeping rework that is part of a series of reworks to revisit old locations and not only bring them up to date with our current asset roster, but to make them properly belong within the game world. The Nuke-Ops base may ultimately be a tiny chunk of the overall SS13 experience, but I'll be damned if it isn't a defining one. It's also a location that has the capacity to do one thing that I have always wanted to do. Purchase Property. You heard me right, you get to buy rooms now. The newly expanded Nuke-Ops base features, with @ Mothblocks blessing, further expansions that you can purchase from your local Syndicate Uplink. Spend your TC, expand your capabilities, and utilize your expertise in order to create
the most mind-boggling disky heists there are.

Possible expansions to your terrorism suite include:
-Ordinance Lab
-Bio-Terrorism Lab
-Chemical Manufacturing Plant

Definite expansions to your Nuke-Ops Firebase include:
-Crew Bunks
-Lab Wing
-War Table
-Upgraded "Disembarkment" Bay"

* NukeOps Firebase Rework

* Update CentCom_skyrat.dmm

Co-authored-by: Zytolg <33048583+Zytolg@users.noreply.github.com>
Co-authored-by: Gandalf <9026500+Gandalf2k15@users.noreply.github.com>

---
## [JoeShook/hapi-fhir-jpaserver-starter](https://github.com/JoeShook/hapi-fhir-jpaserver-starter)@[c06bc37a19...](https://github.com/JoeShook/hapi-fhir-jpaserver-starter/commit/c06bc37a19a8178d5f4c11fca36dd2765701ff77)
#### Tuesday 2022-04-19 18:40:50 by Shook, Joseph

CockRoachDB confirmed RetryableTransactionAspect is hooked

This is just an experiment.  Honestly I think that HapiFhir already has retry strategies and it would take a long time to figure out if I would even use this technique.
Remember the error logs when posting a large transaction bundle indicate I should use the RetryableTransactionAspect.
 So, I followed that experiment to here.  I don't think it is the right thing to do for long running transaction batches for cockroachDB.  Because it is not a conflict for this failure.  Rather you can set the  kv.transaction.max_refresh_spans_bytes to a higher value and make the error go away.  You wouldn't want a transaction Bundle retrying when you already know it will fail exactly the same way again.

---
## [PKRoma/Terminal](https://github.com/PKRoma/Terminal)@[446f280757...](https://github.com/PKRoma/Terminal/commit/446f2807573ffda411f548a519835d15cacdcd9b)
#### Tuesday 2022-04-19 18:41:56 by Mike Griese

Try to silently fall back to a local monarch (#12825)

This is a crazy idea Dustin and I had.

> we can't repro this at will. But we kinda have an idea of where the deref is. We don't know if the small patch (throw, and try again) will fix it. We're sure that the "just fall back to an isolated monarch" will work. I'd almost rather take a build testing the small patch first, to see if that works

> This might seem crazy
> in 1.12, isolated monarch. In 1.13, "small patch". In 1.14, we can wait and see

I can write more details in the morning. It's 5pm here so if we want this today, here it is.

@dhowett double check my velocity flag logic here. Should be always true for Release, and off for Dev, Preview. 

* [x] closes #12774

---
## [svitalis123/printf](https://github.com/svitalis123/printf)@[694690a73e...](https://github.com/svitalis123/printf/commit/694690a73e8bf856a777477bdc0739d28033a72e)
#### Tuesday 2022-04-19 19:06:48 by svitalis123

I'm not going anywhere. You can print that wherever you want to. I'm here and I'm a Spur for life
Education is when you read the fine print. Experience is what you get if you don't
Just because it's in print doesn't mean it's the gospel
With a face like mine, I do better in print
What one has not experienced, one will never understand in print
Nothing in fine print is ever good news
My weakness is wearing too much leopard print
How is the world ruled and led to war? Diplomats lie to journalists and believe these lies when they see them in print
The big print gives and the small print takes away
Sarcasm is lost in print
Print some money and give it to us for the rain forests
The negative is the equivalent of the composer's score, and the print the performance
It's depressing when you're still around and your albums are out of print
Every time that I wanted to give up, if I saw an interesting textile, print what ever, suddenly I would see a collection
Print is the sharpest and the strongest weapon of our party

---
## [giordano/Yggdrasil](https://github.com/giordano/Yggdrasil)@[b1469b44df...](https://github.com/giordano/Yggdrasil/commit/b1469b44df4c63961a6c0f0387a89ef4ef24aa26)
#### Tuesday 2022-04-19 19:47:54 by Elliot Saba

[GCCBootstrap_jll] Build using `crosstool-ng` (#4753)

In the beginning, I wanted to compile a nice little standalone `GCC_jll`
that could be hooked together with a `Glibc_jll` and a `Binutils_jll`,
and a `LinuxKernelHeaders_jll`, etc...  That work is sitting in [0] but
bootstrapping is such a giant pain in the neck that I wanted to give up
the complexity of bootstrapping to instead focus on simply building each
product in isolation.  This _vastly_ reduces the amount of work
necessary to get things working, but it introduces a new dependency: we
need a base C compiler and libc that are already compiled for the target
platform.  To be precise, we need a `build -> host` compiler in order to
build a `host -> target` compiler.  We already have one of those for all
of our current platforms, so I could generate `GCC_jll` packages, but
then when we want to add a new platform, we'd be in trouble.  For this
reason, I realized we'll never truly escape the bootstrapping problem.

I thought about reverting back to the bootstrapping configuration we've
had until now, but rebelled at the thought.  Then I discovered
crosstool-ng, and realized that I could separate concerns here: I can
use ct-ng to build a working cross-toolchain for each target, then use
that compiler to do a much simpler build for all of the other
components.  Therefore, I extract the work of getting a bootstrap build
onto crosstool-ng, and then use that to do whatever other builds I want
in the presence of a fully-functional cross-compiler.

This also breaks the need for the initial bootstrap to be quite as
restricted as the target toolchain.  The GCC that we build technically
doesn't need to run everywhere, it just needs to generate code that runs
everywhere.  We can build GCC against glibc 2.19, and then at build time
have it link the code it generates against glibc 2.12.2, and that will
work just fine for BB.  The compiler may be using a newer glibc to run,
but when it builds, it uses whatever glibc is placed within the target
sysroot.  This also means we don't need to do things like build GFortran
as part of our bootstrap; we can build it later, in the simpler build
script.

In principle, we don't actually need a GCCBootstrap for all platforms.
We only need a functional cross-compiler.  Theoretically, we could use
Clang to do the bootstrapping.  But I'm not going to fully embrace that
because I know that compiling Glibc with Clang is a pain, so for
`*-linux-gnu` at the very least, we're not going to attempt that.  On
macOS and FreeBSD however, there is a possibility that we can use Clang
as our "bootstrap compiler" in order to generate the actual GCC_jlls.

[0] https://github.com/JuliaPackaging/Yggdrasil/tree/sf/gcc

---
## [microsoft/terminal](https://github.com/microsoft/terminal)@[855e1360c0...](https://github.com/microsoft/terminal/commit/855e1360c0ff810decf862f1d90e15b5f49e7bbd)
#### Tuesday 2022-04-19 21:38:09 by Mike Griese

Manually copy trailing attributes on a resize (#12637)

## THE WHITE WHALE

This is a fairly naive fix for this bug. It's not terribly performant,
but neither is resize in the first place.

When the buffer gets resized, typically we only copy the text up to the
`MeasureRight` point, the last printable char in the row. Then we'd just
use the last char's attributes to fill the remainder of the row. 

Instead, this PR changes how reflow behaves when it gets to the end of
the row. After we finish copying text, then manually walk through the
attributes at the end of the row, and copy them over. This ensures that
cells that just have a colored space in them get copied into the new
buffer as well, and we don't just blat the last character's attributes
into the rest of the row. We'll do a similar thing once we get to the
last printable char in the buffer, copying the remaining attributes.

This could DEFINITELY be more performant. I think this current
implementation walks the attrs _on every cell_, then appends the new
attrs to the new ATTR_ROW. That could be optimized by just using the
actual iterator. The copy after the last printable char bit is also
especially bad in this regard. That could likely be a blind copy - I
just wanted to get this into the world.

Finally, we now copy the final attributes to the correct buffer: the new
one.  We used to copy them to the _old_ buffer, which we were about to
destroy.

## Validation

I'll add more gifs in the morning, not enough time to finish spinning a
release Terminal build with this tonight. 

Closes #32 🎉🎉🎉🎉🎉🎉🎉🎉🎉
Closes #12567

---
## [Ryudo300/pcsx2](https://github.com/Ryudo300/pcsx2)@[89f10e1605...](https://github.com/Ryudo300/pcsx2/commit/89f10e160572063b4871bfb8d0c6ffff54f9543a)
#### Tuesday 2022-04-19 21:48:09 by RedDevilus

GameDB:  ':' to '-' + GS and other fixes

Windows doesn't like you to use ':' in folders this caused issues for when CK1 did savestates in folders and now it's also messing with unable to add covers in Qt so better to replace them and also to avoid other issues now and the future.
GS HW Fixes and other fixes for:
- Adventures of Cookie & Cream, The
- Brothers in Arms - Earned in Blood / Road to Hill 30
- Black
- Chaos Legion
- God Hand
- Knockout Kings 2001
- Kuon
- Outrun 2006 / 2 SP
- Project Eden
- Psi-Ops - The Mindgate
- Punisher, The
- Ratchet Deadlocked (USA) / Gladiator (Europe) / 3 Up Your Arsenal
- Silent Hills Origins / Shattered Memories / 3 / 4
- SoulCalibur II / III

Also made sure that the comments and their spacing were consistent.

---
## [TakoTheDev/SkytilsMod-Data](https://github.com/TakoTheDev/SkytilsMod-Data)@[3b89be3ff4...](https://github.com/TakoTheDev/SkytilsMod-Data/commit/3b89be3ff4df4f794cd828b51ed0e0b38262ca1a)
#### Tuesday 2022-04-19 22:09:46 by TakoTheDev

fuck you clicks

Co-authored-by: Clicks <58398364+CuzImClicks@users.noreply.github.com>

---
## [Lypheo/mpv](https://github.com/Lypheo/mpv)@[b83bdd1d17...](https://github.com/Lypheo/mpv/commit/b83bdd1d17cc90b4d8cd2a32321cd7c5cc306422)
#### Tuesday 2022-04-19 22:53:26 by wm4

audio: merge pull/push ring buffer glue code

This is preparation to further cleanups (and eventually actual
improvements) of the audio output code.

AOs are split into two classes: pull and push. Pull AOs let an audio
callback of the native audio API read from a ring buffer. Push AOs
expose a function that works similar to write(), and for which we start
a "feeder" thread. It seems making this split was beneficial, because of
the different data flow, and emulating the one or other in the AOs
directly would have created code duplication (all the "pull" AOs had
their own ring buffer implementation before it was cleaned up).
Unfortunately, both types had completely separate implementations (in
pull.c and push.c). The idea was that little can be shared anyway. But
that's very annoying now, because I want to change the API between AO
and player.

This commit attempts to merge them. I've moved everything from push.c to
pull.c, the trivial entrypoints from ao.c to pull.c, and attempted to
reconcile the differences. It's a mess, but at least there's only one
ring buffer within the AO code now. Everything should work mostly the
same. Pull AOs now always copy the audio data under a lock; before this
commit, all ring buffer access was lock-free (except for the decoder
wakeup callback, which acquired a mutex). In theory, this is "bad", and
people obsessed with lock-free stuff will hate me, but in practice
probably won't matter. The planned change will probably remove this
copying-under-lock again, but who knows when this will happen.

One change for the push AOs now makes it drop audio, where before only a
warning was logged. This is only in case of AOs or drivers which exhibit
unexpected (and now unsupported) behavior.

This is a risky change. Although it's completely trivial conceptually,
there are too many special cases. In addition, I barely tested it, and
I've messed with it in a half-motivated state over a longer time, barely
making any progress, and finishing it under a rush when I already should
have been asleep. Most things seem to work, and I made superficial tests
with alsa, sdl, and encode mode. This should cover most things, but
there are a lot of tricky things that received no coverage. All this
text means you should be prepared to roll back to an older commit and
report your problem.

---
## [Lypheo/mpv](https://github.com/Lypheo/mpv)@[d62131d3ae...](https://github.com/Lypheo/mpv/commit/d62131d3aeda6f3b4c255ca06e70573433a8f16a)
#### Tuesday 2022-04-19 22:53:26 by wm4

vo_x11: allow OSD rendering outside of video region

I'm not sure why it only rendered OSD inside the video. Since OSD
rendering was always done on the X image (after software scaling and
color conversion), there was no technical reason for this. Maybe it was
because the code started out this way, and it was annoying to change it.
Possibly, one reason was that it didn't normally have to clear the black
bars in every frame (if video didn't cover the entire window).

Anyway, simply render OSD to the full window. This gets rid of some
rather weird stuff. It seems to look mostly like vo_wlshm now. The
uncovered regions are cleared every frame, which could probably be
avoided by being clever with the OSD renderer code, but this is where
I'm decidedly losing interest.

There was some mysterious code for aligning the image width to 8 pixels.
Replace that by attempting to align it to SIMD alignment (might matter
for libswscale, or if repack.c gets SIMD). Why are there apparently 4
different ways representing a pixel format (depth, VisualID, Visual,
XVisualInfo), but none of them seem to provide the XImage.bits_per_pixel
value (the actual size of a pixel, including padding)? Even after 33
years, X11 still seems overengineered, confusing, and inconvenient. So
just call X11 a heap of shit, and assume the worst case for alignment.

---
## [QuantumApprentice/Fallout-Nevada-Translation](https://github.com/QuantumApprentice/Fallout-Nevada-Translation)@[22ad04d3bb...](https://github.com/QuantumApprentice/Fallout-Nevada-Translation/commit/22ad04d3bbfd92ba1428a9acee61462e28af463e)
#### Tuesday 2022-04-19 23:50:40 by QuantumApprentice

check on this one?

line 57 {167} I'm not sure if this character is intentionally referring to a male "workaholic" or workaholics in general.  I fixed the english for a singular workaholic (possibly referring to a character in his backstory?) but please check if the phrase should be more generic. ie:
"And when such stupid workaholics, greedy for money, die from exposure, they are then burned in the incinerator and their earned money split in the office."

---

