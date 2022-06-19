## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-06-18](docs/good-messages/2022/2022-06-18.md)


1,527,550 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,527,550 were push events containing 2,213,259 commit messages that amount to 122,447,210 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 34 messages:


## [Comxy/tgstation](https://github.com/Comxy/tgstation)@[95ffcd4e19...](https://github.com/Comxy/tgstation/commit/95ffcd4e19304af76653ff2b33084092246e4b16)
#### Saturday 2022-06-18 00:54:02 by YakumoChen

Moves the FUCKING LIGHT FIXTURES on tiles with surgery beds (#67644)

Moves around some wall objects in surgery rooms on both Meta and Box, primarily so that there aren't light fixtures on the same tiles as surgery beds. I moved a few unrelated things for QOL.

EVERY MOTHER FUCKING TIME I DO SURGERY I ALWAYS SMASH THE FUCKING LIGHT TUBE BY ACCIDENT AND IT PISSES ME THE FUCK OFF. WHY WOULD YOU PUT A THING THERE THAT JUTS OUT OVER THE FUCKING BED AND GETS IN THE WAY OF CLICKING ON THE SPACEMAN SPRITE FUCK GOD DAMN IT.

---
## [bob-b-b/tgstation](https://github.com/bob-b-b/tgstation)@[9428d97a4f...](https://github.com/bob-b-b/tgstation/commit/9428d97a4fadf8a486b0c6fbe2ee345a2780e687)
#### Saturday 2022-06-18 00:58:08 by Imaginos16

[MDB IGNORE] The Tilening V2 - Damaged Tile Overlays Edition (#67761)


About The Pull Request

Hello once more! As we near summer, I continued to reminisce on several PRs done throughout last year! One of them was the controversial, but rather positive Tilening V1, as done by me and Twaticus a while back (#58932), and felt I could've done a better job with how it was presented.

And thus, thanks to @Fikou encouraging me with a very interesting find of a previous tile resprite attempt, I've successfully done it!

Ladies and Gentlemen, I present to you all, Tilening Version Two!
image

Now this isn't your run of the mill tile resprite. While I did improve the appearance of several tiles I haven't touched last time (including the showroom/freezer tiles now), I decided to do something special that most mappers shall appreciate!

Don't you hate it when of all damaged states, there's only ones for grey tiles when we have white, black, terracotta and a bunch of other materials? Don't you wish they were overlays instead?

Well golly gee do I have good news for you!
image
image

After painstakingly spending at least several hours trying to learn enough code to pull it off, I have successfully made it so most tiles display transparent versions of damage overlays over them! This means mappers can express their creativity that much better! And thanks to how the code is written, its super easy to snowflake certain tile types to make them use unique damaged states (looking at you wooden tiles), so fret not in that aspect.

Credits to:
@WJohn For actually making those damaged overlays! Wouldn't've done the PR if it wasn't for you.
@dragomagol, @RigglePrime and @LemonInTheDark for helping me out in a VC at 10 PM to 12 AM troubleshooting the code to make this improvement work!
Why It's Good For The Game

The shading is done better as compared to last time, making them feel more cubical and less like a pancake when seen from above! This PR also makes it so that we never ever have to touch damaged tiles ever again potentially, saving up some RSC regarding icons.

However, due to how damaged tiles are currently mapped in, rather than overlayed as I envision in the future, it'll require a PR by San to be merged later that should make it safe to remove these icons.
Changelog

cl PositiveEntropy, WJohnston, Dragomagol, LemonInTheDark, Riggle
imageadd: Resprites most variety of tiles into a better shaded version!
code: Damaged floors are now damaged overlays, meaning that most tiles should properly display a damaged state!
/cl

---
## [DesmontTiney/tgstation](https://github.com/DesmontTiney/tgstation)@[763a10d1cc...](https://github.com/DesmontTiney/tgstation/commit/763a10d1cc44c91720101d422d8709ad1aa0644d)
#### Saturday 2022-06-18 01:06:04 by distributivgesetz

Resonance cascade polishening, bugfixes and better logging (#67488)

This PR rewrites almost all messages related to cascade events. Some messages felt kinda clunky to read or could have been written better. Overall, the new messages add to the experience as a cascade being a terrifying event in a way that I felt the old ones missed, and they make the event feel overall a lot sharper.

While looking at the resonance cascade code, I noticed that there a lot of stuff about cascades in the air which was not touched on. So, as I do, this PR evolved into a polish and roundup PR for cascades. There was a lot of stuff still hanging out relating to the event, and although the big backend of it sits, there was still a bit left to be completed. Therefore this PR deserves more the title of the "Resonance cascade POLISHENING" instead of the "REFLAVAHRING". But yeah, you ever go on a massive tangent before?

---
## [mamh-mixed/microsoft-terminal](https://github.com/mamh-mixed/microsoft-terminal)@[442432ea15...](https://github.com/mamh-mixed/microsoft-terminal/commit/442432ea15241a3e9ee3d70c5c24e5565655e55b)
#### Saturday 2022-06-18 01:32:40 by Mike Griese

Fixes the wapproj fast-up-to-date check (#11806)

I'm working on making the FastUpToDate check in Vs work for the Terminal project. This is one of a few PRs in this area.

FastUpToDate lets vs check quickly determine that it doesn't need to do anything for a given project. 

However, a few of our projects don't produce all the right artifacts, or check too many things, and this eventually causes the `wapproj` to rebuild, EVERY TIME YOU F5 in VS. 

This third PR deals with the Actual fast up to date check for the CascadiaPackage.wapproj. When #11804, #11805 and this PR are all merged, you should be able to just F5 the Terminal in VS, and then change NOTHING, and F5 it again, without doing a build at all. 




The wapproj `GetResolvedWinMD` target tries to get a winmd from every cppwinrt
executable we put in the package. But we DON'T produce a winmd. This makes the
FastUpToDate check fail every time, and leads to the whole wapproj build
running even if you're just f5'ing the package. EVEN AFTER A SUCCESSFUL BUILD.

Setting GenerateWindowsMetadata=false is enough to tell the build system that
we don't produce one, and get it off our backs.

### teams chat where we figured this out

[3:38 PM] Dustin Howett
however, that's not the only thing that "GetTargetPath" checks.

[3:38 PM] Dustin Howett
oh yeah more info: wapproj calls GetTargetPath on all projects it references

[3:38 PM] Dustin Howett
when it calls GTP on WindowsTerminal.vcxproj it is getting back a winmd (!)


[3:39 PM] Dustin Howett
here's the magic

[3:39 PM] Dustin Howett
![image](https://user-images.githubusercontent.com/18356694/142945542-74734836-20d8-4f50-bf3a-be4e1170ae13.png)


[3:39 PM] Dustin Howett
it checks if any Link items specify GenerateWindowsMetadata

![image](https://user-images.githubusercontent.com/18356694/142945593-fd232243-0175-4653-8c34-cdc364a16031.png)

---
## [alejandroautalan/tukaan](https://github.com/alejandroautalan/tukaan)@[b8566316c1...](https://github.com/alejandroautalan/tukaan/commit/b8566316c1423f928ab69b6f8bc0014d6a1c3376)
#### Saturday 2022-06-18 02:30:46 by rdbende

Add #StandWithUkraine badge

And Russian warship, go fuck yourself as well

---
## [Harrivchaw/CEV-Eris](https://github.com/Harrivchaw/CEV-Eris)@[04e9ec00b1...](https://github.com/Harrivchaw/CEV-Eris/commit/04e9ec00b1c401a071945c37fd4c683ec1ef0cd4)
#### Saturday 2022-06-18 02:52:28 by 1glitchycent

resprites the technomancer armor (#5646)

* yo we wuz technomancers an shiet

5 months of technofans per communist killed

* deletes the extra eris we have in code

this is real life we aren't technomancers no wackies allowed

* females also wear armor

wtf how?????????????????????

* sold ballistic plates to pay for technofans

nerfed ballistic armor values and buffed bomb

* FUCK ATOMIZING 

I gotta do it doe

* Update armor.dm

* change desc

* yo we got da gucci plate carriers

updates sprite

* epic helmet

7 commits(not counting first 2) on a resprite. GAMING.

* FINAL COMMIT(I HOPE), resprites armor once aga

armo likes it I think

---
## [elginsk8r/android_kernel_oneplus_sm4350](https://github.com/elginsk8r/android_kernel_oneplus_sm4350)@[9dbd491509...](https://github.com/elginsk8r/android_kernel_oneplus_sm4350/commit/9dbd49150964f9d09525628d05f97b38ab04d800)
#### Saturday 2022-06-18 03:00:42 by alk3pInjection

disp: msm: Handle dim for udfps

* Apparently, los fod impl is better than udfps cuz it
  has onShow/HideFodView hook, which allows us to toggle
  dimlayer seamlessly.

  Since udfps only partially supports the former one,
  we'd better kill dim in kernel. This is kinda a hack
  but it works well, bringing perfect fod experience
  back to us.

Co-authored-by: Art_Chen <Chenxy0201@qq.com>
Signed-off-by: alk3pInjection <webmaster@raspii.tech>
Change-Id: I80bfd508dacac5db89f4fff0283529c256fb30ce

---
## [huntercollegehighschool/cs9-final-project-AyodejiWasHereButHasGoneAFK](https://github.com/huntercollegehighschool/cs9-final-project-AyodejiWasHereButHasGoneAFK)@[9c9bf6424c...](https://github.com/huntercollegehighschool/cs9-final-project-AyodejiWasHereButHasGoneAFK/commit/9c9bf6424c187f0088f0d9db80cb49ce54754870)
#### Saturday 2022-06-18 04:04:46 by AyodejiWasHere Sylvain

2000+ lines of blood, sweat, tears and way too much fun for a mandatory class. Thanks for all of he extensions and we hope you enjoy!

---
## [ShelbyHell/QuicksilveRV2_kernel_juice](https://github.com/ShelbyHell/QuicksilveRV2_kernel_juice)@[cd498990ea...](https://github.com/ShelbyHell/QuicksilveRV2_kernel_juice/commit/cd498990eaba074869843d749ab77739173b4a2a)
#### Saturday 2022-06-18 04:50:30 by Joonsoo Kim

mm/page_alloc: use ac->high_zoneidx for classzone_idx

Patch series "integrate classzone_idx and high_zoneidx", v5.

This patchset is followup of the problem reported and discussed two years
ago [1, 2].  The problem this patchset solves is related to the
classzone_idx on the NUMA system.  It causes a problem when the lowmem
reserve protection exists for some zones on a node that do not exist on
other nodes.

This problem was reported two years ago, and, at that time, the solution
got general agreements [2].  But it was not upstreamed.

[1]: http://lkml.kernel.org/r/20180102063528.GG30397@yexl-desktop
[2]: http://lkml.kernel.org/r/1525408246-14768-1-git-send-email-iamjoonsoo.kim@lge.com

This patch (of 2):

Currently, we use classzone_idx to calculate lowmem reserve proetection
for an allocation request.  This classzone_idx causes a problem on NUMA
systems when the lowmem reserve protection exists for some zones on a node
that do not exist on other nodes.

Before further explanation, I should first clarify how to compute the
classzone_idx and the high_zoneidx.

- ac->high_zoneidx is computed via the arcane gfp_zone(gfp_mask) and
  represents the index of the highest zone the allocation can use

- classzone_idx was supposed to be the index of the highest zone on the
  local node that the allocation can use, that is actually available in
  the system

Think about following example.  Node 0 has 4 populated zone,
DMA/DMA32/NORMAL/MOVABLE.  Node 1 has 1 populated zone, NORMAL.  Some
zones, such as MOVABLE, doesn't exist on node 1 and this makes following
difference.

Assume that there is an allocation request whose gfp_zone(gfp_mask) is the
zone, MOVABLE.  Then, it's high_zoneidx is 3.  If this allocation is
initiated on node 0, it's classzone_idx is 3 since actually
available/usable zone on local (node 0) is MOVABLE.  If this allocation is
initiated on node 1, it's classzone_idx is 2 since actually
available/usable zone on local (node 1) is NORMAL.

You can see that classzone_idx of the allocation request are different
according to their starting node, even if their high_zoneidx is the same.

Think more about these two allocation requests.  If they are processed on
local, there is no problem.  However, if allocation is initiated on node 1
are processed on remote, in this example, at the NORMAL zone on node 0,
due to memory shortage, problem occurs.  Their different classzone_idx
leads to different lowmem reserve and then different min watermark.  See
the following example.

root@ubuntu:/sys/devices/system/memory# cat /proc/zoneinfo
Node 0, zone      DMA
  per-node stats
...
  pages free     3965
        min      5
        low      8
        high     11
        spanned  4095
        present  3998
        managed  3977
        protection: (0, 2961, 4928, 5440)
...
Node 0, zone    DMA32
  pages free     757955
        min      1129
        low      1887
        high     2645
        spanned  1044480
        present  782303
        managed  758116
        protection: (0, 0, 1967, 2479)
...
Node 0, zone   Normal
  pages free     459806
        min      750
        low      1253
        high     1756
        spanned  524288
        present  524288
        managed  503620
        protection: (0, 0, 0, 4096)
...
Node 0, zone  Movable
  pages free     130759
        min      195
        low      326
        high     457
        spanned  1966079
        present  131072
        managed  131072
        protection: (0, 0, 0, 0)
...
Node 1, zone      DMA
  pages free     0
        min      0
        low      0
        high     0
        spanned  0
        present  0
        managed  0
        protection: (0, 0, 1006, 1006)
Node 1, zone    DMA32
  pages free     0
        min      0
        low      0
        high     0
        spanned  0
        present  0
        managed  0
        protection: (0, 0, 1006, 1006)
Node 1, zone   Normal
  per-node stats
...
  pages free     233277
        min      383
        low      640
        high     897
        spanned  262144
        present  262144
        managed  257744
        protection: (0, 0, 0, 0)
...
Node 1, zone  Movable
  pages free     0
        min      0
        low      0
        high     0
        spanned  262144
        present  0
        managed  0
        protection: (0, 0, 0, 0)

- static min watermark for the NORMAL zone on node 0 is 750.

- lowmem reserve for the request with classzone idx 3 at the NORMAL on
  node 0 is 4096.

- lowmem reserve for the request with classzone idx 2 at the NORMAL on
  node 0 is 0.

So, overall min watermark is:
allocation initiated on node 0 (classzone_idx 3): 750 + 4096 = 4846
allocation initiated on node 1 (classzone_idx 2): 750 + 0 = 750

Allocation initiated on node 1 will have some precedence than allocation
initiated on node 0 because min watermark of the former allocation is
lower than the other.  So, allocation initiated on node 1 could succeed on
node 0 when allocation initiated on node 0 could not, and, this could
cause too many numa_miss allocation.  Then, performance could be
downgraded.

Recently, there was a regression report about this problem on CMA patches
since CMA memory are placed in ZONE_MOVABLE by those patches.  I checked
that problem is disappeared with this fix that uses high_zoneidx for
classzone_idx.

http://lkml.kernel.org/r/20180102063528.GG30397@yexl-desktop

Using high_zoneidx for classzone_idx is more consistent way than previous
approach because system's memory layout doesn't affect anything to it.
With this patch, both classzone_idx on above example will be 3 so will
have the same min watermark.

allocation initiated on node 0: 750 + 4096 = 4846
allocation initiated on node 1: 750 + 4096 = 4846

One could wonder if there is a side effect that allocation initiated on
node 1 will use higher bar when allocation is handled on local since
classzone_idx could be higher than before.  It will not happen because the
zone without managed page doesn't contributes lowmem_reserve at all.

Reported-by: Ye Xiaolong <xiaolong.ye@intel.com>
Signed-off-by: Joonsoo Kim <iamjoonsoo.kim@lge.com>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Tested-by: Ye Xiaolong <xiaolong.ye@intel.com>
Reviewed-by: Baoquan He <bhe@redhat.com>
Acked-by: Vlastimil Babka <vbabka@suse.cz>
Acked-by: David Rientjes <rientjes@google.com>
Cc: Johannes Weiner <hannes@cmpxchg.org>
Cc: Michal Hocko <mhocko@kernel.org>
Cc: Minchan Kim <minchan@kernel.org>
Cc: Mel Gorman <mgorman@techsingularity.net>
Link: http://lkml.kernel.org/r/1587095923-7515-1-git-send-email-iamjoonsoo.kim@lge.com
Link: http://lkml.kernel.org/r/1587095923-7515-2-git-send-email-iamjoonsoo.kim@lge.com
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: celtare21 <celtare21@gmail.com>

---
## [FloricSpacer/AbyssDiver](https://github.com/FloricSpacer/AbyssDiver)@[717c50cbf7...](https://github.com/FloricSpacer/AbyssDiver/commit/717c50cbf7286affe81c640f32d9c49665a09edd)
#### Saturday 2022-06-18 07:43:41 by Stadler76

Fixes for size related curses

- Fixed gender calculation not taking Minish-ish and Colossal-able into account, causing futas to turn male or female depending on the actual cock size
- Corrected inch to cm math from 2.5cm to 2.54cm and moved the code to display it into a reusable widget.
- Fixed Minish-ish calculation changing the height to a negative value.

---
## [NicohIas/Tank-API](https://github.com/NicohIas/Tank-API)@[9c1f3b8473...](https://github.com/NicohIas/Tank-API/commit/9c1f3b84737c26f26816120b3290f0da87cbd757)
#### Saturday 2022-06-18 08:18:33 by nic

Hey, you. You're finally awake.

You were trying to cross the border, right? Walked right into that Imperial ambush, same as us, and that thief over there. Damn you Stormcloaks. Skyrim was fine until you came along. Empire was nice and lazy. If they hadn't been looking for you, I could've stolen that horse and be halfway to Hammerfell. You there. You and me - we shouldn't be here. It's these Stormcloaks the Empire wants. We're all brothers and sisters in binds now, thief. Shut up back there! And what's wrong with him, huh? Watch your tongue. You're speaking to Ulfric Stormcloak, the true High King. Ulfric? The Jarl of Windhelm? You're the leader of the rebellion. But if they've captured you... Oh gods, where are they taking us? I don't know where we're going, but Sovngarde awaits. No, this can't be happening. This isn't happening. Hey, what village are you from, horse thief? Why do you care? A Nord's last thoughts should be of home. Rorikstead. I'm... I'm from Rorikstead.

---
## [hi-rustin/cargo](https://github.com/hi-rustin/cargo)@[6a4d98d232...](https://github.com/hi-rustin/cargo/commit/6a4d98d2327124ca52bb9f67d6ad0097eb6b2e65)
#### Saturday 2022-06-18 08:57:41 by bors

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
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[1cc0a5e2f2...](https://github.com/mrakgr/The-Spiral-Language/commit/1cc0a5e2f29adf70a2b7ec5ff61118602762224f)
#### Saturday 2022-06-18 10:51:57 by Marko Grdinić

"10:50am. Yeah, it is not going to happen. I tried getting into that other novel, but Legendary Mechanic drew me right back in.

The only good cultivation GB novel is Demon Sword Maiden. Well, let me chill a bit more and then I am going to get started on exporting the models. After that I'll import them in Clarisse and texture them.

11:25am. Let me start. I can't be held back by this for much longer. Let me export the objects, import them in Clarisse, and deal with the scene.

11:35am. Actually, there are a shitton of modules here. I need an addon to automate this.

11:45am. Fuck, trying to export it as FBX ground it to a halt. I really regret going down this route instead of making my own assets simply because I would have had a lot more fun making my own things. Instead right now I am bashing my head against this.

Let me try experimenting with exports on Neo Cities. Manhattan is killing me.

12:05pm. I've figured it out. USD exports are really good for exporting geometry. It does not convert the shaders, but nevermind that. Let me USD Export Manhattan next.

12:20pm. i've forgotten. How do Clarisse's groups work again? I knew their purpose, but I forgot what it was by now.

https://youtu.be/k3dZMybYAoE
Clarisse Spotlight - Groups

https://youtu.be/k3dZMybYAoE?t=107

I was wondering what that group view was.

https://youtu.be/k3dZMybYAoE?t=315

Why can't I see the group objects in context view? Also what are layers?

12:40pm. Let me take a break here. I did succeed in my basic goal of exporting the geo. It is disappointing that it is not exporting the shaders for Neo City despite me clicking the option. If I wanted to use the textures provided I'd have to do them by hand, but nevermind that for now.

https://docs.blender.org/manual/en/latest/files/import_export/usd.html
> Not all nodes are supported; currently only Diffuse, Principle, Image Textures, and UVMap nodes are support.

I guess this might be why. Some of the shaders used are `Transparent BSDF`s.

12:45pm. Let me not bother with that. Breakfast. I'll focus on the shaders after that. I just need to grind through this. In fact, this situation is a good reason to just get 3ds Max in the future. I mean, imagine if I wanted to take a pure kitbashing approach. Who is going to constantly setup the shaders just for Clarisse? 3ds Max is 10gb, so I do not feel like getting it, but I just might in the future.

This project is going to be my last env work in a while, so I won't bother right now. After I finish this I'll get some charas done, and after that it is music."

---
## [filolia/android_kernel_xiaomi_mt6768](https://github.com/filolia/android_kernel_xiaomi_mt6768)@[9cf3f4dc15...](https://github.com/filolia/android_kernel_xiaomi_mt6768/commit/9cf3f4dc15fdb01d45c4c2abe9cc97ced51b78c3)
#### Saturday 2022-06-18 12:16:32 by Peter Zijlstra

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
Signed-off-by: filolia <filolia@proton.me>

---
## [HeyitsSunshine/javascript-greatness](https://github.com/HeyitsSunshine/javascript-greatness)@[915592c4c6...](https://github.com/HeyitsSunshine/javascript-greatness/commit/915592c4c630c341b33dcc63998e2fa25888a0f9)
#### Saturday 2022-06-18 12:43:26 by Dillon Beers

Did not get opp. to add anything of meaning, however, I am still amazing, and life needs to fucking give me all of its' goodies.

---
## [nmslq/FNF-PsychEngine-Android-Support](https://github.com/nmslq/FNF-PsychEngine-Android-Support)@[11c0de2937...](https://github.com/nmslq/FNF-PsychEngine-Android-Support/commit/11c0de29373fe0afd2f382ea70d5de638947e238)
#### Saturday 2022-06-18 12:54:57 by nmslq

github when fixed the android workflows

fuck you stupid github
fuck you stupid github
fuck you stupid github
fuck you stupid github
fuck you stupid github

---
## [SabreML/Skyrat-tg](https://github.com/SabreML/Skyrat-tg)@[01a6ade18c...](https://github.com/SabreML/Skyrat-tg/commit/01a6ade18cfcc1b79e5f5dace05c5e9c1e89b919)
#### Saturday 2022-06-18 12:56:04 by SkyratBot

[MIRROR] Change healing by sleeping to be affected by sanity, darkness (or blindfold), and earmuffs. [MDB IGNORE] (#13758)

* Change healing by sleeping to be affected by sanity, darkness (or blindfold), and earmuffs. (#65713)

About The Pull Request

Depending on the mob's sanity level, it can have a positive or negative boost to healing effects while sleeping. Sleeping in darkness, wearing a blindfold, and using earmuffs also counts as a healing bonus. Beauty sleep is very important for 2D spessmen.
Why It's Good For The Game

This is a small gameplay change that rewards players for keeping their sanity at good levels. Also depression has also been linked with impeding wound healing in real life. The placebo effect on peoples minds is strenuously documented and I think it would be cool to see it in the game.
Changelog

cl
expansion: Healing by sleeping is now affected by sanity, sleeping in darkness (or using a blindfold), and using earmuffs. The healing from sleeping in a bed was slightly decreased.
/cl

* Change healing by sleeping to be affected by sanity, darkness (or blindfold), and earmuffs.

Co-authored-by: Tim <timothymtorres@gmail.com>

---
## [Axlefublr/Personal](https://github.com/Axlefublr/Personal)@[3a498fa92c...](https://github.com/Axlefublr/Personal/commit/3a498fa92c905d8f00d6fa57c1df27d19758357b)
#### Saturday 2022-06-18 14:51:39 by Axlefublr

Now even relative paths to Programming and Personal and Other and the like are variables in a class. ; This way, if I ever decide to rename or move a folder, all I have to do in order to fix the dependencies on files is just change its path in the class. The folders are dependent on each other, so if I change the parent folder, that will also take care of the child folders.; This might seem more complex than it`s worth, but see it like this: While I will 95% of the times use workingDir to specify a relative path, the relativity of the other folders in the path that goes right ahead is nonexistant. Let`s say there`s a variable inside of a path, or maybe it goes somewhere else and you`re kinda stuck unraveling more than you should have to, and keep in mind: writing the same shit over and over. With my new system, if I want to in any way move or rename folders around, I have a really direct way to do that, rather than the unsure `search this (i think) and replace it with this (i think)`. This will let me be freer in programming, because I know I won`t have to change much if I move some stuff around, and freedom is really important. ; Fixed ` and ` fucking up the -m `commit message` (the chars I`m mentioning will be replaced with `); Fixed ` strings not being recognized by the syntax highlighting, now you can safely use them. ; In v2, ``string ` `` is allowed, but not ``string ` ``, same about ```. Now the syntax highlighting reflects that. It does so by catching the first quotation mark of the same kind, unless it`s escaped with \` (unless the \` is escaped with a \`). Which is, finally, the same as it is in v2. God the amount of time and energy I`ve spent overall on this issue.; Don`t get me started on continuation sections. I banged my head on the table trying to figure that shit out. Ok so for whatever reason it couldn`t match multiple lines, which, I guess, is how syntax highlighting works overall: goes line by line and applies the regex, rather than on the whole file. Performance-wise it makes sense, but god is it annoying. ; You can use ``begin`` and ``end`` to make multiple lines some class, but both begin and end still can only catch no more than one line. I had to do this whole song and dance to figure that out. ; In the end, it works by catching a lone ``` on a new line after any amount of spaces or tabs followed by any amount of spaces or tabs and then a newline, with maybe a `\r`

---
## [Dudemanguy/mpv](https://github.com/Dudemanguy/mpv)@[095cf42547...](https://github.com/Dudemanguy/mpv/commit/095cf42547440172f1c98260349f3d5a5581568e)
#### Saturday 2022-06-18 15:12:38 by Dudemanguy

x11: support xorg present extension

This builds off of present_sync which was introduced in the previous
commit to support xorg's present extension in all of the X11 backends
(sans vdpau) in mpv. It turns out there is an Xpresent library that
integrates the xorg present extention with Xlib (which barely anyone
seems to use), so this can be added without too much trouble. The
workflow is to first setup the event by telling Xorg we would like to
receive PresentCompleteNotify (there are others in the extension but
this is the only one we really care about). After that, just call
XPresentNotifyMSC after every buffer swap with a target_msc of 0. Xorg
then returns the last presentation through its usual event loop and we
go ahead and use that information to update mpv's values for vsync
timing purposes. One theoretical weakness of this approach is that the
present event is put on the same queue as the rest of the XEvents. It
would be nicer for it be placed somewhere else so we could just wait
on that queue without having to deal with other possible events in
there. In theory, xcb could do that with special events, but it doesn't
really matter in practice.

Unsurprisingly, this doesn't work on NVIDIA. Well NVIDIA does actually
receive presentation events, but for whatever the calculations used make
timings worse which defeats the purpose. This works perfectly fine on
Mesa however. Utilizing the previous commit that detects Xrandr
providers, we can enable this mechanism for users that have both Mesa
and not NVIDIA (to avoid messing up anyone that has a switchable
graphics system or such). Patches welcome if anyone figures out how to
fix this on NVIDIA.

Unlike the EGL/GLX sync extensions, the present extension works with any
graphics API (good for vulkan since its timing extension has been in
development hell). NVIDIA also happens to have zero support for the
EGL/GLX sync extensions, so we can just remove it with no loss. Only
Xorg ever used it and other backends already have their own present
methods. vo_vdpau VO is a special case that has its own fancying timing
code in its flip_page. This presumably works well, and I have no way of
testing it so just leave it as it is.

---
## [ChenHuajun/postgres](https://github.com/ChenHuajun/postgres)@[c40ba5f318...](https://github.com/ChenHuajun/postgres/commit/c40ba5f318f96a6a5a29729b987ead11c5dc65c1)
#### Saturday 2022-06-18 15:37:50 by Tom Lane

Fix rowcount estimate for SubqueryScan that's under a Gather.

SubqueryScan was always getting labeled with a rowcount estimate
appropriate for non-parallel cases.  However, nodes that are
underneath a Gather should be treated as processing only one
worker's share of the rows, whether the particular node is explicitly
parallel-aware or not.  Most non-scan-level node types get this
right automatically because they base their rowcount estimate on
that of their input sub-Path(s).  But SubqueryScan didn't do that,
instead using the whole-relation rowcount estimate as if it were
a non-parallel-aware scan node.  If there is a parallel-aware node
below the SubqueryScan, this is wrong, and it results in inflating
the cost estimates for nodes above the SubqueryScan, which can cause
us to not choose a parallel plan, or choose a silly one --- as indeed
is visible in the one regression test whose results change with this
patch.  (Although that plan tree appears to contain no SubqueryScans,
there were some in it before setrefs.c deleted them.)

To fix, use path->subpath->rows not baserel->tuples as the number
of input tuples we'll process.  This requires estimating the quals'
selectivity afresh, which is slightly annoying; but it shouldn't
really add much cost thanks to the caching done in RestrictInfo.

This is pretty clearly a bug fix, but I'll refrain from back-patching
as people might not appreciate plan choices changing in stable branches.
The fact that it took us this long to identify the bug suggests that
it's not a major problem.

Per report from bucoo, though this is not his proposed patch.

Discussion: https://postgr.es/m/202204121457159307248@sohu.com

---
## [jazzdelightsme/terminal](https://github.com/jazzdelightsme/terminal)@[77215d9d77...](https://github.com/jazzdelightsme/terminal/commit/77215d9d77b99b48d1ee8302736178f2ec9f3a77)
#### Saturday 2022-06-18 15:56:32 by Mike Griese

Fix `ShowWindow(GetConsoleWindow())` (#13118)

A bad merge, that actually revealed a horrible bug.

There was a secret conflict between the code in #12526 and #12515. 69b77ca was a bad merge that hid just how bad the issue was. Fixing the one line `nullptr`->`this` in `InteractivityFactory` resulted in a window that would flash uncontrollably, as it minimized and restored itself in a loop. Great. 

This can seemingly be fixed by making sure that the conpty window is initially created with the owner already set, rather than relying on a `SetParent` call in post. This does pose some complications for the #1256 future we're approaching. However, this is a blocking bug _now_, and we can figure out the tearout/`SetParent` thing in post. 

* fixes #13066.
* Tested with the script in that issue.
* Window doesn't flash uncontrollably.
* `gci | ogv` still works right
* I work here.
* Opening a new tab doesn't spontaneously cause the window to minimize
* Restoring from minimized doesn't yeet focus to an invisible window
* Opening a new tab doesn't yeet focus to an invisible window
* There _is_ a viable way to call `GetAncestor` s.t. it returns the Terminal's hwnd in Terminal, and the console's in Conhost


The `SW_SHOWNOACTIVATE` change is also quite load bearing. With just `SW_NORMAL`, the pseudo window (which is invisible!) gets activated whenever the terminal window is restored from minimized. That's BAD.


There's actually more to this as well. 


Calling `SetParent` on a window that is `WS_VISIBLE` will cause the OS to hide the window, make it a _child_ window, then call `SW_SHOW` on the window to re-show it. `SW_SHOW`, however, will cause the OS to also set that window as the _foreground_ window, which would result in the pty's hwnd stealing the foreground away from the owning terminal window. That's bad.

`SetWindowLongPtr` seems to do the job of changing who the window owner is, without all the other side effects of reparenting the window. 

Without `SetParent`, however, the pty HWND is no longer a descendant of the Terminal HWND, so that means `GA_ROOT` can no longer be used to find the owner's hwnd. For even more insanity, without `WS_POPUP`, none of the values of `GetAncestor` will actually get the terminal HWND. So, now we also need `WS_POPUP` on the pty hwnd. To get at the Terminal hwnd, you'll need

```c++
GetAncestor(GetConsoleWindow(), GA_ROOTOWNER)
```

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[92de3d6573...](https://github.com/mrakgr/The-Spiral-Language/commit/92de3d6573cae1f69521b489c5b82ae22907c82b)
#### Saturday 2022-06-18 18:36:57 by Marko Grdinić

"1:45pm. Done with breakfast.

1:55pm. You know how Blender did not export the materials correctly. Well, it seems that even though the shading groups are there, they are not doing anything.

2:10pm. Fuck, I figured it out. I was putting the shaders on the wrong model. What a waste of time.

What I need to do now is figure out how to put the shaders on a model and also override it. I want a golden and a regular instance of these buildings. How can I most easily do that?

2:15pm. This should have been an easy job, but having to go through numerious different applications like this really slows me down. Now I have to refresh my memory of how shading works in Clarisse. That will be a few hours down the drain. Kitbashing seems like an obvious choice, but doing my own models would have been competitive.

2:25pm. I've looked at the example project and that refreshed my memory of shading layers. But even so how can I put the original asset in a combiner and only then assign it?

https://www.youtube.com/results?search_query=clarisse+shading+layer

There is no way around it, I am going to have to watch some tutorials.

https://youtu.be/ZxJIx7JDfds
Clarisse Spotlight - Shading Layers

Let me start with this. This project will be done when it wants to be done obviously. I deeply regret not doing it all by hand.

Oh right. Maybe it would have been worth it to try out proxies in Blender.

https://youtu.be/KUWBaFHCphI
Manage Huge Scenes in Blender (Millions Ahead)(no addons required)

Found this.

2:35pm. No forget it. Let me just focus on Clarisse. If I start messing with Blender again I'll waste the whole day.

https://youtu.be/ZxJIx7JDfds?t=198

Ahhhhhhh!!!

I have in fact completely forgotten that I can drag shading layers around. I have an idea how I could possibly make this work, but I'll have to make sure. At any rate, it does not have much to do with dragging shading layers like that. But it is good that it refreshed my memory.

https://youtu.be/ZxJIx7JDfds?t=466

Oh, this proves that my idea will work.

The only really important part is that I use shading layers instead of mat linkers all the way through.

Another way I could do this I suppose is using attributes...

But I am not sure exactly how to tackle it using that.

https://youtu.be/ZxJIx7JDfds?t=777

Dropper. This should be useful for finding out which materials are being used. Ok.

I want to take a nap, but let me just do this thing.

3:05pm. Ok, I put a flat texture on each of the buildings. This is way easier than assigning each of the numerious shading groups individually. What I need to figure out next is how to do emissive windows at random.

Hmmm, not bad. Everything that I want to be lighted up at night has the world Glass in it. I can just assign a shader to that using the shading layers.

The only question remaining is how do I randomize the lights based off the instance id.

3:25pm. I have no idea how. I do not even know where to find the info. Let me work on everything other than the this. First all, let me check out the Clarisse examples.

Oh, there is a city example in there.

City
This project is focused on layout. Learn how point clouds, scatterers, combiners and instances are used to set dress a gigantic futuristic city.

Looks quite fancy.

3:35pm. https://forum.isotropix.com/viewtopic.php?f=5&t=6997

I'll get an answer here.

3:55pm. FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF---

I hate Clarisse!

Why can't I just assing the fucking thing to Glass!?

4pm. I am on tilt here. Telling the program to fuck itself won't work here.

Could it be that I can't overload the materials based on the combiners?

Let me clear my head. Right now I have all sorts of complication due to me copying groups of objects. Let me try overriding just a single one.

4:50pm. This is a nightmare. I had to take a break. Let me resume.

4:55pm. Yeah, I must be going crazy. I pick an object, create an instance of it somewhere else and then move it. What happens is that moving the instance moves all ther other isntances as well as the original. I want to put my first through the monitor.

I deeply regret trying to use multiple programs right now.

I really don't get why this is happening. Won't regular copies duplicate the geometry? Why isn't instancing working. Let me watch some tutorials. I watched this a few months ago and now it has all faded from memory. Rather than getting good, I seem to have developed multiple incompatible workflows. I mean, if I could dedicate myself to one or the other it would make sense, but I can barely remember it by now. And once I finish the project it will be a while before I touch it again. It really is a mistake to move from program to program. Ok, if I can't get this done by tomorrow I am going to cut my losses and forget the kitbashing.

https://youtu.be/bQugIY3QGu4?t=192

Here he talks about instantiation.

https://youtu.be/bQugIY3QGu4?t=200

This means that they share all the same attributes? So completely opposite to how it works in Blender. What is the point of it then?

Now wait, no wait.....................aghhhh, now that I am watching this I see where this will go. He will click on the attributes and localize them!

5:15pm. Come to think of it, even if I did a regular copy, I don't think there is a chance that Clarisse would duplicate the geometry. In the obj file it literally has a path to the file on disk. The same goes for USD I am guessing.

5:20pm. Let me take a break here. I want a nap. After that I am going to copy the buildings into their own individual context, shade them and move on. In Clarisse if there isn't a way of shading the windows produrally I am out of luck. The way this is going I am literally going to have to throw in the towel and make it from scratch. If so then so be it.

5pm. Let's do it. This thing is going down!

5:35pm. I am trying to organize the objects and Clarisse crashed 2 times in 2 minutes.

Now assigning the glass shader worked without a hitch.

5:45pm. I keep moving things around and Clarisse keeps crashing. This is the world's way of indicating to me that I am on the wrong path.

6pm. Now the scatterer is putting the buildings in the wrong place for some reason.

Is it the right choice to just throw my hands up in disgust here?

6:10pm. I've presevered and managed to get through the obstacle.

6:15pm. Agh, ah. Right now my head hurts. 10m ago when it crashed it caused me to snap my head like a monkey.

https://youtu.be/vxVkQlhuqWM
Fine Tune Scattering in Clarisse iFX Using Houdini

I need some scattering tutorials. Moving programs like this is really a huge burden which is why I did not want to do it. But other than this, what choice did I have?

Right now I am reading the docs. It has colission detection. How do I turn that on?

> It is possible to enable collision detection to avoid instance interpenetration. This results to more realistic distribution but introduces some computational costs inherent to the collision detection computations. To enable collision detection, simply set Collision Mode to Use Bounding Box or Use Ellipsoid.

I do not see the option anywhere.

7:05pm. Let me go have lunch. I am so discouraged I had to take a nap for a bit.

Hmmm, it is not done yet. Let me consider 3ds Max vs Blender here. I'll also watch that earlier video that I skipped on working with high poly in Blender.

https://youtu.be/CWRtj7elRmo
Why You Shouldn't Be Afraid of High Poly Meshes (Max + Blender) - Classic Topo Problem #12

7:35pm. Done with lunch.

///

This is a nightmare. Trying Clarisse after not using it for a few months is like slamming your head against the wall. It constantly crashes, and I am getting tripped up by every little thing.

This kit should have been an asset, but instead it is turning into a huge burden and I am regretting that I did not just model my own.

///

Let me not post this yet. Let me watch a bit of the above and then I will check the proxy options in Blender again. Since things are like this I think I should drop this project temporarily until I get a handle on polycounts in Blender.

https://youtu.be/KUWBaFHCphI
Manage Huge Scenes in Blender (Millions Ahead)(no addons required)

Let me actually watch this.

https://www.isotropix.com/learn/tutorials/basic-shading-variation-for-scattering-in-clarisse

Got linked this.

https://youtu.be/KUWBaFHCphI?t=521

Let me stop this here. I have no more energy to pursue this.

https://www.blendernation.com/2020/08/03/lodify-a-free-lod-proxy-script-for-blender/

///

Hello Everyone, BD3D Here.

I created a free LOD/Proxy system for blender 2.8 or above, it's basically acting as a mesh-data exchanger, really useful if you'd like to optimize your scenes without using bounding boxes or by hiding everything.

///

BD3D is the same guy who did the Scatter 5 plugin. It might be worth a try.

https://youtu.be/NbsoUmdGQpI?t=61

There is a part in the Scatter tutorial about LODs and proxies.

https://youtu.be/NbsoUmdGQpI?t=70
> I ship Lodify with Scatter of course.

This is a sign. It is a sign that the dev is thinking about my concerns, so maybe I should tune into that.

https://youtu.be/NbsoUmdGQpI?t=286

Batch change LODs.

https://youtu.be/NbsoUmdGQpI?t=403

This is convincing enough for me. Lodify is definitely something that I need. I am just going to have to swallow my pride, join the objects by hand, and then pare them down. Maybe I will just voxelize them.

8:10pm. I am thinking of maybe trying the Early Access of Clarisse, but my level of trust in it is low.

https://youtu.be/NbsoUmdGQpI?t=592
> Ideally, you want to decimate the model only inside the viewport.

Doing this was one of my ideas. Is he going to say that I will run into trouble with it?

https://youtu.be/NbsoUmdGQpI?t=632
> Supposedly, Blender is supposed to optimize the viewport with this modifier.
> But in fact it's not, it's even worse performance.

Damn!

> On each frame, Blender is always recalculating the decimate modifier.

8:20pm. https://www.blendernation.com/2020/08/03/lodify-a-free-lod-proxy-script-for-blender/

///

Amazing work. I can see next steps could be to add:

1. Ability to quickly clear out and remove orphan LODify data.
2. Ability to loop through a selection of objects and automatically duplicate, decimate, and LODify them, with the option to replace LODify data or skip if LODify data is present.
3. Same for textures / materials.

This seems to be a necessary step to help Blender work with huge amounts of data in huge scenes.

///

Yeah, I agree with this comment. I wish it had this. Who is going to go through all those kitbash objects by hand? This is the kind of thing that I should write a script for.

Yeah, why don't I? It would certainly be a better way to spend my time than to go through 100s of objects in the kit by hand. I do not need to make a plugin, just a script will do.

8:25pm. Ok, I'll play it like that. I'll dedicate tomorrow to studying the Scatter plugin. I need a break from the floating city scene as it put its boot up my ass.

8:30pm. Let me close here. I'll try to make some progress tomorrow. Once I get a grasp on scattering in Blender and do the lodify script, I'll be able to make use of the kit efficiently.

There are benefits to keeping it all within the same program, so I'll give Blender a try again. I can't accept the conclussion that the kit is a burden. Rather I am just not doing it right. There is no way that these finely done buildings are a negative. I am going to grasp their true worth."

---
## [obsproject/cef](https://github.com/obsproject/cef)@[4fec476322...](https://github.com/obsproject/cef/commit/4fec476322ea1fe4599a6b9b9e09f8b0e9a521e2)
#### Saturday 2022-06-18 19:14:14 by Jim

Legendary 4638 shared texture perf improvement

This fixes remaining performance and frame pacing issues when using CEF
95 with texture sharing on Windows. I hacked Chromium internally to
treat shared textures similarly to how the 3770 method worked.

Let me document my little adventure.

First, we were getting system freezes, and from analysis of the
bluescreen dumps, they were always during synchronization, so I had a
hunch: "are keyed mutexes doing this?" The system freeze issue left me
hopeless. I already had a disdain for the stupid keyed mutexes, and due
to my immense hatred of them, I was angry and I just wanted to try
removing them, because 1.) What if they were the cause? (They were), and
2.) I hated them anyway. It was an irrational vendetta, and I was on a
war path to remove them just in the *slightest* chance that those god
forsaken keyed mutexes were the cause.

So I got angry and decided to remove them from almost everything in
Chromium just to see if it would fix the system freeze issue. I removed
their usage from almost everything in Chromium related to GLImageDXGI.

Let me go on a rant about keyed mutexes. I hate keyed mutexes. I *want*
synchronization between devices, but what I *don't* want is to be forced
to swap stupid "keys" between the two devices; especially if you're in a
situation where you cannot pass the next key value to the next device so
the next device knows what key to use, because then, the original device
can no longer lock the object anymore, and the object is completely
forfeit. Then you get suck in a situation where you're forced to wait
infinitely if you have no way of telling the other device to use the
correct key. I wish I could suggest a better design, but all I know is
that I hate it, it's an insufferable design as it is right now, and I
don't think there's a single human being on the planet who will ever
convince me otherwise. Absolutely insufferable design. I've always hated
them and always will.

Anyway, sorry about that. Like I was saying, I removed keyed mutex usage
from texture sharing inside chromium. But the problem is that with the
4638 version of shared textures, it was about 5 textures which were used
round-robin. Because we were forced to remove keyed mutexes (which were
crashing the entire system), we could no longer synchronize between
client and Chromium, thus frame pacing issues were introduced. Even
flushing wasn't helping. They weren't noticeable, and we were *almost*
just going to use it as it, but I decided I wasn't finished with my war
path.

I had fixed the system freeze issue by removing keyed mutexes, but now
there was this frame pacing issue. So, I was upset, and I tried many
different techniques to try to synchronize. Flushing, more textures,
less textures, trying to adjust timing; I thought it was hopeless, until
I started looking at the 3770 version and started looking around
4638 code for ways I could do the same thing. I had already removed
keyed mutex objects from GLImageDXGI objects, but then I realized: what
if I just add the same staging/CopyResource method 3770 did, and then
just use one shared texture? 3770 worked amazingly well, so why not try
it? Through much toil and experimentation, I got it working.

However, there was still one annoying caveat. Because of the fact that
Chromium now only deals with NT-style HANDLE objects for shared
textures, it would duplicate handles every time it was passed. There was
no way of detecting whether we were already using the same shared
texture (and CompareObjectHandles in KernelBase didn't work), so we had
to recreate the stupid texture object every time. So I introduced a new
OnAcceleratedPaint2 function specifically to specify whether the texture
has been changed -- that way we don't need to have to continually keep
recreating the god-forsaken texture object.

All these things combined has won us a huge victory, not only did we
solve the system freeze issue, but we also reduced the amount of
resources being used from the original version by removing the round
robin, eliminated frame pacing issues, and improved the perf back to
3770 levels. In fact, I'm pretty sure that perf levels are even better
than they were even with the keyed mutex version (if they weren't
causing stupid system freezes), because the keyed mutex version forced
INFINITE lock durations due to the inability to relay keys.

After 27.2 had this issue, I had to delay the release, and I spent a
week toiling over this. To get the system freeze issue fixed, and then
to get perf levels back to 3770 levels. And I did it by sifting through
millions of lines of Chromium code.

Needless to say I feel really damn good right now. This was a legendary
fix. I'm sorry, I need a little bit of ego just for once. I feel like
I've earned it.

---
## [LZ1WS/Before_The_Dead_Slashers_Revamped](https://github.com/LZ1WS/Before_The_Dead_Slashers_Revamped)@[290282e75e...](https://github.com/LZ1WS/Before_The_Dead_Slashers_Revamped/commit/290282e75ea123f57cf266a32f0b7d0f328f2e74)
#### Saturday 2022-06-18 19:16:01 by LZ1WS

"Dreams & Nightmares" pre-release update

| Added |
- New Killer - the Nightmare
#A serial killer who came from nightmares. A legend that originated on Elm Street.\n Pursues the victims, exhausting and driving them into a state of sleep, after which it sets its own rhythm to the chase, from which it is extremely difficult to escape. Use RMB to imprison the survivors in your world and use the factors affecting the sleeping targets in it in order to gain an advantage in hunting.#
- New Survivor - Simon Henriksson
#You've always knew that you have a connection to something much darker than everyday world. You can use your powers to see from the eyes of the dark being#
- New Map - slash_monolith10_night
- Lockers to hide in for survivors and reload hatchets for the Huntress
- Freeze of all prop_physics entities on the map

| Changed |
- Tadero's Magic
- Tadero's Scythe
- Changed the way of giving unique weapons only for killers that have them (GM.MAP.Killer.UniqueWeapon)
- A new way to determine which killer has a special round (Like Slenderman and Albert Wesker) (GM.MAP.Killer.SpecialRound)
- New description for the Huntress

| Fixed |
- Vaccine boxes spawn on maps (currently only slash_subway because others need positions setup)

| Removed |
- Old commented out code in map configs

---
## [ChakatStormCloud/Tannhauser-Gate](https://github.com/ChakatStormCloud/Tannhauser-Gate)@[9e786d49b4...](https://github.com/ChakatStormCloud/Tannhauser-Gate/commit/9e786d49b4aaec266859e83e152b2d88b09e5cdd)
#### Saturday 2022-06-18 19:39:29 by SkyratBot

Stops floating mobs from being affected by slowndown bulky_drag and human_carry (#66610) (#13357)

Put simply, removes the slowdown from pulling bulky items as well and fireman carrying (and piggyback rides) while in zero gravity.

This also fixes some weirdness, like how slowdowns from aggressive grabs are negated in zero g, but because bulky_drag is NOT negated, you can still be slowdown in zero gravity if your target is laying down. or in a neck grab or higher because they are then automatically floored. Which makes zero consistant sense given the context.

Also, while testing this, I noticed that it was faster to drift while pulling a bulky object in space rather than fly with a jetpack because of the  slowdown and how drifting works, which also makes no god damn sense. This should fix that too.

Fixes the consistency errors mentioned above, also adds an interesting change of game state in zero gravity which seems fun. (see: faster to drag away downed friendlies during a space battle, or perhaps kidnap a downed enemy)

Fixes #62600 (aggressively grabbing a body in space makes you move faster than passively grabbing them)


You can now pull bulky things in zero gravity at full speed
The slowdown from neck grabs is now properly negated in zero gravity.

Co-authored-by: itseasytosee <55666666+itseasytosee@users.noreply.github.com>

---
## [jehugaleahsa/javalin-mvc](https://github.com/jehugaleahsa/javalin-mvc)@[1e7da105bb...](https://github.com/jehugaleahsa/javalin-mvc/commit/1e7da105bb7fc7c9072067ab6d5a65d6aa38e2d2)
#### Saturday 2022-06-18 20:02:16 by Travis Parks

Upgrade to Javalin 4.x

The most annoying and time intensive activity with upgrading to 4.x was that there's no convenient way to get at the Jackson `ObjectMapper` in 4.x. Previously, the Javalin library basically have a `static final` constant for the `ObjectMapper`. They sort of fixed this issue by introducing the `JsonMapper` interface and making you pass it as a configuration setting when initializing the app. The problem is they didn't make it easy to retrieve the `JsonMapper` implementation from a context. This might be fixed in Javalin 5. For now, I am working around the issue by passing JsonMapper to the `JavalinControllerRegistry`. See this GitHub issue for more details: https://github.com/javalin/javalin/issues/1572

Another challenge with the upgrade was that routes now use {param} instead of :param. This is good thing, in my opinion, since it allows doing things like `/prefix-{whatever}-suffix`. For example, you could use `/v{version}` to choose a different implementation based on a version number.

Some async unit tests were failing, I think because the `start`/`stop` methods work differently now. They may actually be truly synchronous now.

---
## [KabKebab/GS13](https://github.com/KabKebab/GS13)@[5b7f7a52e4...](https://github.com/KabKebab/GS13/commit/5b7f7a52e462ac381aa5e8bd762ccb2fbfc9476b)
#### Saturday 2022-06-18 20:26:56 by MrSky12

Removed the fat ray

Fuck you fat ray for being bad.

---
## [IHateMyKite/UnforgivingDevices](https://github.com/IHateMyKite/UnforgivingDevices)@[e0becd3c5e...](https://github.com/IHateMyKite/UnforgivingDevices/commit/e0becd3c5eb02b8567b631a51e8f224228847a35)
#### Saturday 2022-06-18 20:59:31 by IHateMyKite

Reworked lock mutex

-Reworked lock mutex
  -Mutex is now individual for every registered NPC.
  -Non registered NPC will use new mutex slots. There are currently 3 slots, and thus 3 NPC can be processed at once
  -Also reworked how device checks if render device is correctly equipped. This should finally solve issue with lost render devices (devices which gets registered, but are not equipped)
-Added mutex for selve equip (when device is equipped using invetory). This should solve some issues, but at the same time will most likely break other things. Will have to test this more before release.
-Hopefully Fixed NPC general debug option which didn't work properly (didn't test but should work)
- Added bit documantation for bitmaps in render device script
-NPC which will get locked in hand restrain will be pacified with Calm spell, so the NPC will not break from restrain and start beating player. They will still be marked as hostile
-Added check to vibrator loop so it will stop when the device is no longer present on actor, preventing zombie stack
-Added new API functions in to Expression manager
-Added ew new expressions
  -Happy expression : is appkied randomly when strugglong normally and slowly
  -Concetrated expression : is applied when struggling using magick
  -Tired expression : is applied when actor is exhausted from struggling
  -Angry expression : is applied when actor is struggling desperatly
  -Random expression : randomly created expression. This may sometimes look stupid, but other times looks really nice. Is applied randmely when struggling.
  -Theese expressions are stored directly in scripts, so it is easier for me to implement them.
-Added check that will prevent hardcore effect to be applied before the current dialogue ends
-Added bunch more options in to MCM Patcher section
-Improved patcher: Patched device can now be uncuttable and also without locks
-Added new modifier: Cheap locks
  -Device have random cahnce every hour to gain jammed lock
  - There is also smaller chance that lock will jamm when actor is attacked
-Lock repair will now grant smithig skill. It will also be affected by the same skill
-Cutting minigame will now grant one handed skill. It will also be affected by the same skill
-Reworked how best weapon is choosen for cutting minigame
  -Best weapon is directly stored in NPC slot if actor is registered. Then every time actor takes new weapon, it will be compared and replaced if its better.
  -Non registered NPCs will use same method as before
-Concetrated black goo now also have Paralysis effect
-Added patch for zadBoundCombatScript. Issue was that if the EvaluateAA is called while actor is paralysed, it will totally break the NPCs behavier. For that reason simple check was added so it will not evaluate AA until paralysis runs out
-Moved expression raled function from zadlibs_UDPatch in to Expression manager
-Added new textures for new chargable plugs
-Again moved orgasm and arousal loop in to magick effect. I don't think there is any performance issue. This will help updating the loops in comparison to previous versions.
-Concetrated black goo will first strip actor before locking devices
-Reworked device type: Chargable plug
  -Plug will slowly charge. It will charge on every wearer orgasm and also on update based on current arousal level (similar to abadon plug)
  -Can be crafted from empty soulgems
  -Can't be removed untill the plug is fully charged
  -Removing the plug will detry it and reward wearer with the charged soulgems that were used to craft the plug
  -Plugs vibration gets stronger and longer with charge level

---
## [farie82/Paradise](https://github.com/farie82/Paradise)@[ab7a358506...](https://github.com/farie82/Paradise/commit/ab7a35850672da159eea98085cf6fade7d595340)
#### Saturday 2022-06-18 21:38:56 by Farie82

Makes setting a machine GC properly if not unset properly (#17840)

* Makes setting a machine GC properly if not unset properly

* Forgot one. Fuck you borer code

---
## [ynot01/Yogstation](https://github.com/ynot01/Yogstation)@[8b77243ce9...](https://github.com/ynot01/Yogstation/commit/8b77243ce9da72645291d6f22f798bc32611a706)
#### Saturday 2022-06-18 22:02:43 by TheRyeGuyWhoWillNowDie

Makes bloodbrothers start with the makeshift weapons book learned. (Jamie Edition) (#14094)

* makes blood brothers a bit less shit

* oopsie

* improve???

* what

* huh??

---
## [jimc/linux](https://github.com/jimc/linux)@[b5d206d45d...](https://github.com/jimc/linux/commit/b5d206d45d3a01e941ca33b78f811762328072af)
#### Saturday 2022-06-18 22:03:32 by Jim Cromie

dyndbg: add drm.debug style bitmap support WIP

Add kernel_param_ops and callbacks to implement a bitmap in a
sysfs-node, which controls classes.  This supports uses like:

  echo 0x3 > /sys/module/drm/parameters/debug

IE add these:

 - int param_set_dyndbg_classes()
 - int param_get_dyndbg_classes()
 - struct kernel_param_ops param_ops_dyndbg_classes

Following the model of kernel/params.c STANDARD_PARAM_DEFS, these are
non-static and exported.  This might be unnecessary here.

get/set use an augmented kernel_param; the arg refs a new struct
ddebug_classes_bitmap_param, initialized by the DYNAMIC_DEBUG_CLASSES
macro (see commit HEAD~6), which contains:

BITS: a pointer to the user module's ulong holding the bits/state.  By
ref'g the client's bit-state _var, we coordinate with existing code
(such as drm_debug_enabled) which uses the _var, so it works
unchanged, even as the foundation is switched out underneath it..
Using a ulong allows use of BIT() etc.

FLAGS: dyndbg.flags toggled by bit-changes. Usually just "p".

MAP: a pointer to struct ddebug_classes_map, which maps those
class-names to pr_debug.class_ids 0..N.  This class-map is
defined/declared/initialized by DYNAMIC_DEBUG_CLASSES() etc.

map-type: enum _DISJOINT, _LEVELS

RFC:

Above was written before DISJOINT and LEVELS was distinguished, and
describes former, but this patch has both.  Testing shows DISJOINT is
solid, _LEVELs is not; the interface has some ambiguities.

To map LEVELS onto DISJOINT, levels are mapped to consecutive DISJOINT
bits, and the x>y relation is enforced on the bit position.
All well and good, until -1 is needed to clear bit 0.

This also has the undesirable property that read val doesnt match just
written val:

   echo 0 > verbosity
   cat verbosity
   0x1

a few ways out ?

1 :#> echo -1 > $sysknob
  signed int input carries additional expressive capacity
  this preserves 2**N bitmapping
  but bit-0 is weird (for LEVELS only, not DISJOINT)

2 subtract 1 from input, treat as bitpos (like now)
  :#> echo 0 > levelX	# turn OFF bit 0
  :#> echo 1 > levelX	# turn ON bit  0
  :#> echo 2 > levelX	# turn ON bits 1-0
  :#> echo 3 > levelX	# turn ON bits 2-0

3 drop "V0", "L0"
  v=0 is just printk, no point in using this in prdbgs, so theres nothing to control.
  this kinda puts V1 on bit-0

4 use symbolic classnames
  :#> echo +INFO,-TRACE > nv_debug
  :#> echo -V1 > verbosity

5 base=1 on _LEVELS class
  this might combine with others, or further confuse things.

ATM impl is 1, without the -1 input.  The chief trouble here is that
the readback value after writing 0 is 0x1, which violates the
principle of least-surprise.  Fixing that in param-get feels hacky.

Theres also some ambiguity potentially added in the symbol to bit
mapping; the names in a _LEVELS classmap can muddle things (2,3 break
this istm).

  :#> echo 0 > verbosity
  :#> echo V0 > verbosity  # should mean the same thing

This constraint basically means that; V0 must be allocated (just a
bit), mapped (so its legal input), and unused (because its just a
complicated printk).  MAYBE.

More map-types could tailor behavior, and input forms accepted:

DD_CLASS_DISJOINT_HEX: accept only hex bitmaps

DD_CLASS_DISJOINT_SYMNAMES: accept only symbolic class-names

DD_CLASS_VERBOSE_NUMBER: accept only decimal verbosity numbers

DD_CLASS_VERBOSE_SYMNAMES: accept only symbolic class-names

maybe
should exclude V0, or

also breaks 1

Signed-off-by: Jim Cromie <jim.cromie@gmail.com>

---
## [wincent/wincent](https://github.com/wincent/wincent)@[ec49be762f...](https://github.com/wincent/wincent/commit/ec49be762ff3ef0570a9bc27f972d0d1f025e3da)
#### Saturday 2022-06-18 22:10:12 by Greg Hurrell

feat(dotfiles): automatically sign commits on personal machines

As described here:

    https://wincent.com/wiki/GPG_key_rotation_notes

I don't even have a signing key my work machine (mostly because I don't
want to go through the hoops of getting such a thing working on
Codespaces, although it would be easy enough to do it locally on my work
laptop).

But recent changes in GitHub:

    https://twitter.com/wincent/status/1535598901486669824
    https://github.blog/changelog/2022-05-31-improved-verification-of-historic-git-commit-signatures/

lead me to reconsider my long-help policy of not bothering to sign
commits, only tags. If GitHub is going to show signatures even as valid
after the corresponding keys have expired, then it seems that it is
worth doing after all.

Torvalds is well known for saying that signing commits is "stupid":

    https://news.ycombinator.com/item?id=12290873
    https://stackoverflow.com/a/10166916/2103996

> Signing each commit is totally stupid. It just means that you automate
> it, and you make the signature worth less. It also doesn't add any
> real value, since the way the git DAG-chain of SHA1's work, you only
> ever need one signature to make all the commits reachable from that
> one be effectively covered by that one. So signing each commit is
> simply missing the point.

I think this is true in a sense, but the importance of GitHub's UI
decisions within the developer ecosystem shifts the balance. Sure,
auto-signing _does_ make each signature be "worth less", but at the same
time, I am _not_ worried about somebody else impersonating me. Even if
my commits are garbage, I am happy to attest to being the one who made
that garbage. For me, signing doesn't mean "this is good", but rather,
"this is me". GitHub's UI very much reinforces the reading that any
given commit was really made by the author.

The trade-offs in kernel development are different. For example, as it
says here:

    https://github.com/torvalds/linux/blob/4b35035bcf80ddb47c0112c4fbd84a63a2836a18/Documentation/process/maintainer-pgp-guide.rst#how-to-work-with-signed-commits

> It is easy to create signed commits, but it is much more difficult
> to use them in Linux kernel development, since it relies on patches
> sent to the mailing list, and this workflow does not preserve PGP
> commit signatures. Furthermore, when rebasing your repository to
> match upstream, even your own PGP commit signatures will end up
> discarded. For this reason, most kernel developers don't bother
> signing their commits and will ignore signed commits in any external
> repositories that they rely upon in their work.

Even there, they go on to say:

> However, if you have your working git tree publicly available at
> some git hosting service (kernel.org, infradead.org, ozlabs.org,
> or others), then the recommendation is that you sign all your git
> commits even if upstream developers do not directly benefit from this
> practice.

---
## [RandomTales/Naruto_Ninpou](https://github.com/RandomTales/Naruto_Ninpou)@[80cd503e06...](https://github.com/RandomTales/Naruto_Ninpou/commit/80cd503e06b6da03cbec977535c84e603ab9b6ee)
#### Saturday 2022-06-18 23:39:12 by MetalfOxXer

changes

- Reduced Roshi lava mode slow to 10%
- Fixed Hidan R not reflecting damage properly
- Fixed some descriptions
- Fixed Dark Totsuka life steal not working
- Fixed Fuu Yamanaka semi
- Rock Lee W doesn't push creeps anymore / Fixed sfx effect not moving with him
- Itachi additional heal on his D removed
- Return damage from Juubi Skin from Book of Gelel reduced by 50%
- Kid Gaara Q damage type changed from Magic to Normal
- Tenten's R is now slightly slower again
- Improved Torune's T animation slightly maybe
- Rikudou Naruto W from 50x HP and 25x Mana to 75x HP and 50x Mana

---
## [MetalfOxXer/Naruto_Ninpou](https://github.com/MetalfOxXer/Naruto_Ninpou)@[006170dccc...](https://github.com/MetalfOxXer/Naruto_Ninpou/commit/006170dccc681881c09ca424f50cd362eb790e4f)
#### Saturday 2022-06-18 23:40:10 by RandomTales

random

chain lightning procing mirror
rikdou madara meteor bugging spells
neji and hinata r sometimes not silencing
hyuuga byagukans falling off sometimes
hanzo mirror procing on q
 reduce the animation between the indra arrow exploding and stunning, atm you can jump and chakra jump after the fact that it hit and u will still get stunned/dmged
Taka sasuke W damage is fucked
hashirama can no longer walk over cliffs

---

