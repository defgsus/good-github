## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-06-30](docs/good-messages/2023/2023-06-30.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,039,773 were push events containing 3,352,328 commit messages that amount to 269,033,378 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 45 messages:


## [rpardini/armbian-build](https://github.com/rpardini/armbian-build)@[db3357d3d5...](https://github.com/rpardini/armbian-build/commit/db3357d3d56f4716c8c0dbf97a771e732f672143)
#### Friday 2023-06-30 00:04:19 by Ricardo Pardini

WiP: meko: like is shit, works with embedded its kern-dtb :facepalm"

TIL: rk's 3588 uboot is demented.
it wants a "kern-dtb", no matter what you have in u-boot dtb if only reads clocks and such low-level from it.
then goes to standard "Android" partitions looking for the kernel dtb. On an Android image (with standard rk gpt partition layout), it finds one... always.
If you enable such wonderful switches like CONFIG_EMBED_KERNEL_DTB_ALWAYS you can convince it to embed kernel dtb in the its/itb (FIT)  🤢
And suddenly... ethernets PXE work... USB works (still slow)... rockchip_opt/fuse works... thus TEE (bl32) is actually useful...  thus serial# works... thus eth macs are stable...
Also: their boot.scr code is riddled with basic parsing bugs. Even sane-ish boot.scr's fail... while extlinux almost always works.
I think loadaddr's are somehow dynamic depending on DDR/BL31 blob.... but only  really updated for extlinux
thus boot.scr's fail depending on wind direction / size of initrd / such
it's like "they found a way" to have a single uboot for all their androids.
essentially the rk3588_defconfig more-or-less boots any 3588 if it can find the Android kernel dtb.
now investigating wonders such as ROCKCHIP_EARLY_DISTRO_DTB_PATH 🤮

---
## [henryk-radoslaw-rychlik/u-boot](https://github.com/henryk-radoslaw-rychlik/u-boot)@[8dfeee651f...](https://github.com/henryk-radoslaw-rychlik/u-boot/commit/8dfeee651fc13c8fd797998e9a408a8b49bead09)
#### Friday 2023-06-30 00:20:42 by Marcel Ziswiler

tegra: lcd: video: integrate display driver for t30

On popular request make the display driver from T20 work on T30 as
well. Turned out to be quite straight forward. However a few notes
about some things encountered during porting: Of course the T30 device
tree was completely missing host1x as well as PWM support but it turns
out this can simply be copied from T20. The only trouble compiling the
Tegra video driver for T30 had to do with some hard-coded PWM pin
muxing for T20 which is quite ugly anyway. On T30 this gets handled by
a board specific complete pin muxing table. The older Chromium U-Boot
2011.06 which to my knowledge was the only prior attempt at enabling a
display driver for T30 for whatever reason got some clocking stuff
mixed up. Turns out at least for a single display controller T20 and
T30 can be clocked quite similar. Enjoy.

Tested-by: Andreas Westman Dorcsak <hedmoo@yahoo.com> # ASUS TF T30
Tested-by: Jonas Schwöbel <jonasschwoebel@yahoo.de> # Surface RT T30
Tested-by: Svyatoslav Ryhel <clamor95@gmail.com> # LG P895 T30
Signed-off-by: Marcel Ziswiler <marcel.ziswiler@toradex.com>
Signed-off-by: Svyatoslav Ryhel <clamor95@gmail.com>

---
## [jwnimmer-tri/drake](https://github.com/jwnimmer-tri/drake)@[f90899e13f...](https://github.com/jwnimmer-tri/drake/commit/f90899e13fd6b703ac5c7da3d1b7c0584a793769)
#### Friday 2023-06-30 00:21:09 by Jeremy Nimmer

[geometry] Add Meshcat::GetRealtimeRate (#19700)

Tidy up recent Meshcat changes:
- Add missing pydrake bindings.
- Strongly prefer testing the public API (eschew test-friendship hacks).
  We want to guard against regressions in the end-user experience;
  using private API goes against that goal.
- Fix indentation, typos, and eschew abbreviation.

---
## [flashshock/langchain](https://github.com/flashshock/langchain)@[75fb9d2fdc...](https://github.com/flashshock/langchain/commit/75fb9d2fdcc201e80ad9c065a02c6cc9ccf6d716)
#### Friday 2023-06-30 01:01:35 by Stefano Lottini

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
## [net-lisias-ksp/KSPe](https://github.com/net-lisias-ksp/KSPe)@[43eea13a1a...](https://github.com/net-lisias-ksp/KSPe/commit/43eea13a1ac3d548920ecb38b20b6b181c91d504)
#### Friday 2023-06-30 01:31:50 by Lisias T

Throwing Exceptions when trying to load an Already Loaded Assembly. Should mitigate the https://github.com/TweakScale/Companion_Frameworks/issues/6 problem, as well any other idiot that do the same stupidity as I did. #facePalm

---
## [compiler-errors/rust](https://github.com/compiler-errors/rust)@[33a081218e...](https://github.com/compiler-errors/rust/commit/33a081218e3f06762922f973b77a1835fbeb2008)
#### Friday 2023-06-30 02:14:47 by Michael Goulet

Rollup merge of #112300 - Zalathar:run-coverage, r=wesleywiser

Convert `run-make/coverage-reports` tests to use a custom compiletest mode

I was frustrated by the fact that most of the coverage tests are glued together with makefiles and shell scripts, so I tried my hand at converting most of them over to a newly-implemented `run-coverage` mode/suite in compiletest.

This ~~*mostly*~~ resolves #85009, ~~though I've left a small number of the existing tests as-is because they would require more work to fix/support~~.

---

I had time to go back and add support for the more troublesome tests that I had initially skipped over, so this PR now manages to completely get rid of `run-make/coverage-reports`.

---

The patches are arranged as follows:

- Declare the new mode/suite in bootstrap
- Small changes to compiletest that will be used by the new mode
- Implement the new mode in compiletest
- Migrate most of the tests over
- Add more code to bootstrap and compiletest to support the remaining tests
- Migrate the remaining tests (with some temporary hacks to avoid re-blessing them)
- Remove the temporary hacks and re-bless the migrated tests
- Remove the unused remnants of `run-make/coverage-reports`

---
## [Superlagg/coyote-bayou](https://github.com/Superlagg/coyote-bayou)@[6fe28837f1...](https://github.com/Superlagg/coyote-bayou/commit/6fe28837f1d0337091619b4d4b9254f252bc6f83)
#### Friday 2023-06-30 03:04:58 by gob

Ghouls bleed again

Crowley: "Ha, ha! I like a human that knows his place. Too many of you think we're all just zombies. They don’t know, or don’t care, that we’re just as human as they are inside. *We bleed!* We hurt! We regret! And you know what really pisses me off? They think the only way to kill us is to shoot us in the head, like in the old zombie stories, and that will put us out of our misery. Hey, I know! Maybe you could help me even the score."

---
## [AOSPA-Extended/android_frameworks_base](https://github.com/AOSPA-Extended/android_frameworks_base)@[da96e081f4...](https://github.com/AOSPA-Extended/android_frameworks_base/commit/da96e081f46e5c754e767e6475074e8a730d63cc)
#### Friday 2023-06-30 03:12:45 by Kuba Wojciechowski

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
## [freedoom/freedoom](https://github.com/freedoom/freedoom)@[d71ac12cf4...](https://github.com/freedoom/freedoom/commit/d71ac12cf4f4774089ed4949eb0e26fb4debb4e1)
#### Friday 2023-06-30 03:16:00 by mc776

levels: another big batch of fixes. (#997)

* level: more fixes.

E1M3
- Minor item floating in one of the staircases.

E1M7
- Widened the item trenches in the northwest switch room to minimize the chance of a floating item.
- Narrowed the water trench in the southeast switch area to prevent someone from squeeze-gliding in.

E1M9
- Funny-shaped nukage bridge no longer has visible switches. Instead, that railing can be used from the outside anywhere along any of the long sides to lower it.
- Door on the north of that bridge was missing a doortrak.

E3M5
- Northeast giant blood pit had floating items in the new ledges. (Those bits are now also 100% pure meat instead of the rocky crust on top.)

E4M4
- Secret in the southwest is now the room instead of the doorway. Lighting adjusted accordingly.

E4M5
- There's an obscured lamp in the northwest that's supposed to look (in id) like a small lamp placed on top of the box. Freedoom's yellow lamp doesn't work for this, but Freedoom's candle sprite is perfect for the intended effect, so now it is that instead.

E4M6
- Various thin secrets.

E4M7
- Thing no. 580 was the wrong type and bled into the ceiling (see #941). The blocking version is now used instead.

E4M8
- The secrets by the starting area are now the rooms themselves instead of the doorways.

Map11
- Untagged the lizardbaby-triggered doorway as secret.
- All lizard baby sectors are now 72 units tall.
- Realigned the vines in the trilobite corridors overlooking the western atrium.
- Berserk red key secret room lengthened to guarantee having to step inside it.
- Red key is now at a different location, the platform now being a teleporter to it, allowing the location of the red key to be a single sector that can be flagged as a secret.
- Replaced the light source in the yellow skull room with something less likely to have already fallen over.
- Replaced the evil eyes with tech lamps since those aren't shootable.
- The trigger for releasing the pain bringers in the nukage fountain is once again a walk line.

Map16
- Every sector in the backpack secret was tagged as secret, leaving a total of 3 secrets one of which was skippably thin. The skippable is now untagged.

Map18
- It was possible to squeeze into the blue key pillar to trigger the ambush prematurely. The pillar is now the entire 64x64 platform.

* levels: more fixes.

E3M7
- Ambush-flagged and moved the pinkies in the lower small intestine so they stop trying to block the player from below either drop.
- Got rid of some orthogonal lines in the intestine to get rid of the fake contrast.

Map11
- Jump-proofed the decorative canal areas near the final arena.
- Some attempts to address #996.

Map14
- Removed the close-30-seconds door for the descending serpentipede monster closet because if they all bunch up like that while you have an SSG it's a boring wait afterwards. Have fun being hunted by them in the corridors!
- Addressed #996 in the south.

Map15
- Made the two lifts to the red armour secret visually consistent with each other.
- Some feeble attempts to address #996.

Map17
- Jump-proofed by Catoptromancy: numerous platforms raised above what should be jumpable in most sourceports that enable it by default.
- Added a backpack by the corpse near the start, as playing the map "right" and refraining from shooting until you get the tripod puts you in significant danger of running into a shellbox while at near full.
- The stairs inside the living room are flush up against the wall, so you don't waste time falling off and getting back on.
- The window texture now better matches the light falling on the floor.
- Moved Tree #73 and #37 as they were being invisible jump-blockers from below.
- Restored there being three chunks of rock for the blue key.
- Changed up a lot of textures in hopes of creating visually distinct areas.
- Added an extra secret in the start tunnel.
- Made the switch in the water go to 8+LAF fast instead of lowest because those weird sudden flat changes didn't look good.
- Shrank the pillars near the yellow key so you could move around all of them.
- Changed the torches inside the southern switch corridor to techlamps, and added new torches around the entrance to the eastern building.
- Changed the hanging corpse in the living room to another hanging corpse. (see #941)
- Made the couch look more like a couch. And one that's been in a war zone.

Map23
- Replaced the haphazard texture on the northern teleporter room and added some light sources.
- Improved the trim around sector 236 so the door doesn't go right into the curve.
- Used the correct CONS1 flat for sector 246 and shrank it accordingly.
- Addressed #996 in the south.
- Moved the (non-hanged) corpse in the starting secret out of the doorway. The way it hinted at the true nature of that wall was really neat but sadly doesn't play well with software renderer.

Map25
- Southern curved tunnel had a single orthogonal line that led to a misleading fake contrast.
- Some feeble attempts to address #996.

* Delete map17m.wad

* levels: restore old e2m1.

* levels: address E3M6 softlock.

see #998

---
## [toasterpm87/Nyanotrasen](https://github.com/toasterpm87/Nyanotrasen)@[4c45a7e1b7...](https://github.com/toasterpm87/Nyanotrasen/commit/4c45a7e1b7e6b3ce2ef10ae0880d0eebff3af63b)
#### Friday 2023-06-30 03:30:22 by toasterpm87

pebble update

HOLY SHIT, KATAYUSHA FINALLY RELEASED A PEBBLE UPDATE, OH MY FUCKING GOD.

---
## [CommanderBeelo/DayZ-Expansion-Unofficial-Market-Settings](https://github.com/CommanderBeelo/DayZ-Expansion-Unofficial-Market-Settings)@[3fbab8c8e5...](https://github.com/CommanderBeelo/DayZ-Expansion-Unofficial-Market-Settings/commit/3fbab8c8e53c926cc6ae0569f3150d143bf5ad25)
#### Friday 2023-06-30 04:11:05 by CommanderBeelo

Praise be the Divine one that provided this

My friends, gather around, for I shall deliver unto you a tyrade of biblical proportions, where the holy scripture known as the Wiki shall be our guiding light.

In the beginning, there was chaos and ignorance, but then came the Wiki, a digital sanctuary of knowledge. It is a vast repository, a testament to the collective wisdom of humanity, where anyone can partake in the fruits of enlightenment.

Let us turn our eyes to the Book of Search, where we find answers to our questions, uncovering the mysteries that have confounded us for ages. No longer do we wander aimlessly in the darkness, for the Wiki illuminates our path and grants us understanding.

Behold the Book of Collaboration, where countless souls unite in a sacred covenant of shared knowledge. They edit, refine, and enhance the entries, forging a masterpiece that grows with each passing day. The Wiki is a testament to the power of unity and the strength of a global community.

And lo, there is the Book of Citation, where truth is upheld and falsehoods are vanquished. It demands evidence, it craves authenticity. The Wiki is a beacon of veracity, a fortress against deceit. Its gatekeepers ensure that only the most reliable sources find their place within its hallowed pages.

But let us not forget the Book of Expansion, where the Wiki's boundaries are pushed ever further. New discoveries, ideas, and achievements are chronicled, expanding our collective consciousness. The Wiki is a living organism, ever-evolving, mirroring the progress of our civilization.

Now, my brethren, let us pledge to honor and cherish the Wiki. Let us recognize its invaluable contribution to our quest for knowledge and enlightenment. May we always turn to its virtual pages, seeking guidance, truth, and understanding.

For in the Wiki, we find a modern-day scripture, a testament to the potential of humanity's thirst for knowledge. Let us embrace it, celebrate it, and let its wisdom be a guiding force in our lives.

Amen.

---
## [THLynn333/Hand-Rowing-Recumbent-Trikez](https://github.com/THLynn333/Hand-Rowing-Recumbent-Trikez)@[1dce490c2c...](https://github.com/THLynn333/Hand-Rowing-Recumbent-Trikez/commit/1dce490c2c59d22f5daf9b8c34bdd40e1ac747e0)
#### Friday 2023-06-30 04:33:02 by THLynn333

Update README.md

Hand-Rowing-Recumbent-Trikez
My on going Efforts to design and build a hand rowing recumbent Trike
Spelling is not my strong suit due to dyslexia. So be nice Also I have no time for WOKE anything so keep it to yourself.
As I have looked all over for plans and found near to non for such a Trike I finally resorted to designing my own
To that end here is what I have in mind up to the time of this posting
As I have no welding skills I need to find another method to build with To these ends I am thinkin of using several inner twined layers of PVC pipes with solid incert type joints to get the maximum strength with a degree of flexability to my build. With no welding needed.
I have purchased several secound hand bicycles from which I will reuse some parts. Primaraly Wheel Tires frunt forks and possibly a rear fram portion brakes chains gears and others as devised.
I found a design of a gear and sleave that is as follows The sleave is an elongated elipse with gear teeth at the top and bottom centers along it's parelel longer inner sides there are just enough of these teeth to keep the set of corisponding teeth on the center gear always engaged. with enough further length in its inner cut out for the gears teeth to freely move around just bearly leaving the top set of teeth before instantly being ingaged with the lower set of teeth There by causing the center gear to be in constant motion in the same direction.
The center gear has teeth on about 1/3rd of its cercumfrence. Just enough so as to always be in contact with one or the other sets of teeth on the upper or lower part of the sleave. 
I hope to add a neutral position to this set up by spring loading the sleave to be in the ingaged position by default. And by applying a downward and thus outward motion to the ores as it were The sleave can be disingaged from the Gear temparaly. And via the springs action be reingaged when this pressure is realeased. 
Not sure if this design will allow for a reverse motion in the system or if this may have to be addressed in another way.
I was planning to use faberic to make pour boy fiberglass but after thinking about it I may go with a simple layering of plastic grocerie sack from smith's as I like the way they turn brown when in several layers and they can be added to PVC without any glue ( just heating with a cloths iron )
These layers of plastic will allow me to form smooth flat areas were needed rather than have the coragated effect of several PVC pipes layed up side by side.
I plan on reusing parts off of old bikes where posible to save on costs. Like the front forks to be used to carry the front wheels and head lights. 
also the wheels and tires chains gears frame parts brakes and cables for same.
As this is to be a hand rowing system there will be no need for pedals Nore the bike seat.
I think front forks off two smaller bikes  will work well for the front stearing hubs. These will be mounted up under the fender / frame arms and by using tie rods they can be steard in unisence via a set of foot pegs
Just at the top of these stearing towers will be the head light housing so that the head lights will always be facing in the same direction as the wheels
The tail light assembly will be atop a rear wheel in their own inclosure. In addition I'm thinking of adding what I call a God Light front and back for those special peopple that refuse to reduce thier high beams when approaching. Or coming up behind. I also want to have a headlight above my head for extra night vision
The braking will be barrowed directly from the Bikes and mounted onto the new handels.
As I currently have 2 sets of stunt pegs off the used bikes I will use them mounted on the ends of some all thread rods and atatched to the tops of the front mounting towers to give me foot stearing
I am up in the air as to how to do the seat. On the one hand I want to do a hand braided net type or maybe a rag carpet type then again I might go with a plastic molded version like in race cars.
If my power system will allow for it I want to have a Semi Truck horn for it. 
I'm not sure about any liciensing  on it but as my daughter is starting at the DMV tomarrow I am having her look into it for me.
If and when I get this to a point I am happy with it I will offer a set of plans a kit for this basic modle and or a basic customed out Trickerr Trike design or a fully customer designed custom if posible. ( I say this because just while collecting up the used bikes for this build I found 2 potential customers for them )
And because I can build them cheaper than building with metal. I can sell them for less and still pull a prophet. Oh and have a hella lot of fun doing it.
And in an effort to do this I will be building a Custom Trike Club from amoungst my customers and other builders.
Wait till I get this going good and then see what I'm going to do with these micro mini EV PUs out of China. You see I was into building custom vans back when that was big

---
## [Bjarl/Shiptest](https://github.com/Bjarl/Shiptest)@[7468161f7e...](https://github.com/Bjarl/Shiptest/commit/7468161f7ec2180c7752cd2cc99b164522a3540a)
#### Friday 2023-06-30 04:45:10 by FalloutFalcon

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
## [Bjarl/Shiptest](https://github.com/Bjarl/Shiptest)@[8744738e59...](https://github.com/Bjarl/Shiptest/commit/8744738e5955c02834d67db6f14201c28c9ac61c)
#### Friday 2023-06-30 04:45:10 by Arturlang

Updates TGUI and adds bin folder for .bat scripts (#2011)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Updates TGUI and build tools and .vscode files to what TG has.
Does not actually update UI's, but does have fixes for a couple
including the join game UI's tabs not working.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
Not needing to have a local installation of yarn to run dev-mode is
nice.
Updating TGUI is a annoying chore that helps in the future when porting
more interfaces
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
code: Adds a bin folder with dev scripts, updates TGUI, .vscode folder
to what TG has.
fix: Fixes the input in the bottom right being white in darkmode, no
more unreadable text
fix: You can now use the tab buttons in the join ship menu.
qol: The outpost mission menu now looks a whole lot better
fix: The input bar no longer randomly becomes white and unreadable on
darkmode
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: Mark Suckerberg <29362068+MarkSuckerberg@users.noreply.github.com>

---
## [bananaTiko/Banana-Engine](https://github.com/bananaTiko/Banana-Engine)@[d07c4a38c2...](https://github.com/bananaTiko/Banana-Engine/commit/d07c4a38c24b6c52b26d651db409e8c780c89844)
#### Friday 2023-06-30 04:49:10 by bananaTiko

Fuck you microsoft Edge fucking stop crashing on me

---
## [siddheshkumbhar/DataAnalyst_PowerBI_Dashboard](https://github.com/siddheshkumbhar/DataAnalyst_PowerBI_Dashboard)@[3169363789...](https://github.com/siddheshkumbhar/DataAnalyst_PowerBI_Dashboard/commit/3169363789b6986e215f19d2e4eed9017ee1df83)
#### Friday 2023-06-30 06:04:19 by Siddhesh Kumbhar

Add files via upload

As a data analyst, I successfully completed a project focused on developing a Microsoft Power BI dashboard for comprehensive data analysis. This project encompassed data cleaning, processing, analysis, and the creation of a visually stunning dashboard.

During the data cleaning phase, I utilized Power BI's data transformation capabilities to ensure data accuracy and consistency. This involved tasks such as removing duplicates, handling missing values, and standardizing formats, ensuring the dataset was reliable and ready for analysis.

To present the findings in an engaging and informative manner, I designed and developed a visually appealing dashboard using Power BI's intuitive drag-and-drop interface. The dashboard featured interactive charts, graphs, and tables, providing stakeholders with a dynamic and user-friendly experience. By utilizing Power BI's extensive customization options, I created a beautiful dashboard that effectively conveyed the analyzed data and key insights.

By completing this Microsoft Power BI dashboard project, I showcased my proficiency in data cleaning, processing, analysis, and the creation of visually captivating dashboards. I demonstrated my ability to transform complex datasets into actionable insights, enabling data-driven decision-making for stakeholders.

---
## [1393F/tgstation](https://github.com/1393F/tgstation)@[e4ece2fbd6...](https://github.com/1393F/tgstation/commit/e4ece2fbd62dfa6a1270ce37e31fe93bd1823c07)
#### Friday 2023-06-30 06:52:51 by Hatterhat

makes snow legions from portals drop skeletons (like tendril legions) (#75707)

## About The Pull Request
Exactly what it says on the tin (snow legions only dropping ashen
skeletons, like tendril legions).

Also changes the name of the "fromtendril" variable to "from_spawner",
and comments it. Not sure if that warrants a changelong comment, but
I'll go ahead and assume no.

## Why It's Good For The Game
being able to farm snow legion portals for an endless tide of bodies
and/or equipment is a bit weird. also puts it a bit more in line with
the legions of Lavaland

## Changelog

:cl:
balance: The source of the demonic portals that endlessly deposits snow
legions onto the Icemoon no longer preserves the bodies nor gear of the
damned (read: demon portal snow legions now only drop skeletons).
/:cl:

---------

Co-authored-by: Hatterhat <Hatterhat@users.noreply.github.com>

---
## [Akshayy08/PWC_Vartual_Internship](https://github.com/Akshayy08/PWC_Vartual_Internship)@[48e029270f...](https://github.com/Akshayy08/PWC_Vartual_Internship/commit/48e029270f23ad91a84481ddf18b1599f5db2eb3)
#### Friday 2023-06-30 07:28:12 by Akshay Pawar

Add files via upload

One-page report created during PwC Virtual Case Internship. The task was to analyze data and find key areas to focus on customer satisfaction rate and agent statistics. The dataset includes satisfaction ratings for about 5000 customers. Information includes agents, topics, speed of answers, and many more. Here is the background information on your task The digital revolution and our fast-changing world requires a skills revolution. And it’s not just about the digital skills. The skills revolution is about helping people build their digital awareness, emotional intelligence and creativity to fully participate in the digital future workplace — and it needs to start now.

At PwC, we are working with other organisations across the world, building on our work with clients and on upskilling our 276,000 people. Still, more must be done if we are to ensure everyone has the opportunity to learn, work and participate in the digital world. This is at the heart of our purpose.

We are enabling employees who are motivated to further accelerate their skills to do so by offering them a “career pivot” to become what we call “Digital Accelerators”. Accelerators rapidly deepen their skills in digital specialties, such as data, automation, AI, and digital storytelling by learning a variety of self-service tools and coding languages and applying these skills across our business.

We're happy you joined us, welcome to the team! Giulia is your manager and helps you through your upskilling journey in PowerBI - your step to become a true data jedi and Digital Accelerator. But wait no more, word spreads fast and an important client reached out to you to help him visualising their data.

---
## [Opentrons/opentrons](https://github.com/Opentrons/opentrons)@[5271d4fbc4...](https://github.com/Opentrons/opentrons/commit/5271d4fbc473bb8f2506a90b2c929535c82892f6)
#### Friday 2023-06-30 07:29:36 by Seth Foster

feat(api,shared-data): error codes in PE (#12936)

On the python side of our code, we want our new enumerated exceptions to
be gradually integratable, and we also want to make sure that any errors
that we didn't yet get the chance to give error codes end up with error
codes. To do this in a programmatic way, we can add some automated
methods for wrapping python exceptions.

All enumerated errors now get to wrap errors. These are optional
sequences of more enumerated errors that are considered to have caused
the top-level one - in most cases, this will be because the enumerated
error explicitly was instantiated to wrap a python exception, but it
could also be if it was raised from one.

Since we only wrap other enumerated errors, we need a way to make
exceptions enumerated errors. A new exception type (but not code - it's
just a GeneralError) called PythonException has this capability; it lets
you give it BaseExceptions in addition to other EnumeratedErrors, and
it's capable of walking the python memory model internals to try and get
the other exceptions in a stack of raise from ... raise from ... calls
that are reasonably popular in our code. This is functionality that is
promoted out of The Dunder Zone in python 3.11, so I feel pretty good
using it (this is what ExceptionGroups are).

So now, as in the tests, if you catch an exception and give it to a
PythonException you bless it with an error code and save all the
exceptions and their stack traces for later inspection. Cool!

ProtocolEngine is the first place we'll go through and add places that
actually use these error codes, since it's in a lovely high-leverage
middle spot in our stack. That means we both get to test the upward
interface of how these things will be represented in the HTTP API and
how they'll be created from lower exceptions.

ProtocolEngine already has its own very large and robust set of custom
exceptions, which is awesome. We can make them inherit from the
enumerated errors pretty easily, but unfortunately we have to add a
bunch of stuff to their constructors to pass along things like the
ability to wrap other exceptions and so on. Luckily that's just typing.

Once we've done that, at the three points we catch all missed exceptions
we have to switch over to creating the new style. ProtocolEngineErrors
get passed on; uncaught legacy errors get captured as PythonExceptions;
and uncaught errors in the normal core do too.

Finally, we have to represent this new style of error in the
ErrorOccurrence objects. This is the fun part. Previously, we'd added
error codes to those objects; this was sort of a big deal because we
want them to be required when you make new ErrorOccurrences and when
clients look, but we don't want things to break when we deserialize old
ones. We can extend that trick pretty easily to add new things. What's
not quite as easy is this concept of wrapping errors. Our errors are now
essentially trees, and we need tree structure here. Luckily, jsonschema
and pydantic are actually pretty good at type-recursive schema and
object definitions, so we can plop a list of other error occurrences in
there.

Now, when we catch one of these errors that's bubbled up from hardware,
we give it a name and we capture its entire history in an inspectable
way, and I think that's really cool.

---
## [Offroaders123/NBTify](https://github.com/Offroaders123/NBTify)@[11b2602219...](https://github.com/Offroaders123/NBTify/commit/11b26022194c1acd3cd3f3efeab6d993ac3e9b67)
#### Friday 2023-06-30 08:11:35 by Offroaders123

Compression Uncaught Error Handling

Wow, this was an interesting one! I think it may have to do with how the backing implementation of the Compression Streams API is implemented in the browser(s) vs Node. Turns out after all, the error is still partially around the `writer.write()` and `writer.close()` calls.

So, in Node, awaiting both calls works, because they have a `.then()`-able return value, while in Chrome, Safari, and Firefox, they don't ever return when chained with either `.then()`, or used with `await`, hence why it would hang with what would seem like an errorless result. In Node however though, these do eventually resolve, with just a `void` return value.

And interestingly enough, not sure if it has to do with the compression backing implementation, or the handling of Promise rejections and thread sleeping (I don't remember what that's called, but having to do with when the task ends, hiding any errors which haven't rejected by the time the task is completed) (I think it is that second one, I'll explain), but those errors don't occur in Node, but they do in the browser.

I think this is because the console closes before the Promises have rejected, meaning they simply get hidden from failing in the function calls.

I think this can be related to something similar to that of Jake Archibald's article about `for await`, and how it can't properly catch unhandled Promises, as they aren't caught by the current thread pool (not sure if that's the proper term either)

https://jakearchibald.com/2023/unhandled-rejections/

While searching possible fixes to help figure this out, seeing the extra `.catch()` handlers made it click a little more for me, and it help further discover where these ghost errors were bubbling up from!

https://stackoverflow.com/questions/37624322/uncaught-in-promise-undefined-error-when-using-with-location-in-facebook-gra

Overall, I think the main issue is that `writer.write()` and `writer.close()` don't properly have `.then()`-able resolutions in browser(s), while they do in Node. If I could use `await` on these calls, then I could ensure that these errors properly get bubbled back up to the main function, which could properly send them as feedback up to the caller, which can decide how to handle them as they need.

In the meantime, I think I simply have to rely on the errors that would fire after these, because these can't be successfully caught by the main containing function. So I think using a ghost `.catch()` method on them will be the only fix for it, unfortunately.

Maybe I'm missing something about how you should use `write()` and `close()` and maybe they shouldn't be awaited. I'd think that would be key to catching errors properly in situations like these though, no?

https://github.com/Offroaders123/Dovetail/issues/1

For a while, I thought this had to do with my other changes to the Read module (Root ListTags, `return await` try-catch calls, `deflate-raw` auto-detect handling), but turns out it was just the error handling within the Compression module itself, for when piping through a compression stream would have an error, and it simply wan't being cast to the parent scope correctly, because it wasn't being called with `await` (Because it doesn't work in the browser).

Ooh, and the part I said I'd go back to! I think this was happening in Node actually, but only when the thread was running long enough to allow the errors to bubble up to become Uncaught. When I implemented the auto-detect without header checks change, that was using try-catch for each of the compression format types, and errors would magically cause the NEXT compression format to error out, and I couldn't figure out why. Turns out it *was* because Node was exiting in every other case, before those un-awaited Promises were erroring out (because the *header* based checks were faster than when the header-less checks were running), meaning the header-less checks ran long enough for the uncaught errors in the previous auto-detect compression test would bubble up to the main scope as uncaught, and I associated this as only happening with the `deflate-raw` format, because it would only happen with that one, because the other checks would run fast enough to finalize before the errors would bubble up in time.

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[2392685462...](https://github.com/treckstar/yolo-octo-hipster/commit/23926854623c92a4dfd52ebe7e20e34148c781ee)
#### Friday 2023-06-30 08:22:04 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [martinpitt/cockpit](https://github.com/martinpitt/cockpit)@[79d6a888d4...](https://github.com/martinpitt/cockpit/commit/79d6a888d43a1544ec275c7681cc699abdd698f0)
#### Friday 2023-06-30 08:44:35 by Martin Pitt

pybridge: Fix clobbering remote user set in SSH config

When opening a remote host channel without `user`, stop assuming the
current local user name, as that overwrites any `User` field in
the SSH configuration.

Instead, we need to do the opposite: for an unknown host, the UI will
not set a `user` field in the channel options, but for an actual login
attempt with a password it will. We need to treat them as the same
channel in the `self.remotes` map. The C bridge deals with this in
cockpit_router_normalize_host_params() by disregarding the `user` field
if it is equal to the current user name.

This is a rather silly hack for backwards compatibility, but while we
have two bridges, let's rather stay bug-for-bug compatible and clean
this up in the UI only after we drop the C bridge.

There is one extra tweak: `rpartition()` returns an empty string, but
we can't pass that on literally. So turn those into `None`.

Fixes #18714

---
## [symfony/symfony](https://github.com/symfony/symfony)@[af44385d9e...](https://github.com/symfony/symfony/commit/af44385d9e6eba77b4bf4610231ce9569bdcc9b5)
#### Friday 2023-06-30 09:26:01 by Robin Chalas

feature #50754 [HttpKernel] when configuring the container add services_{env} with php extension  (helyakin)

This PR was merged into the 6.4 branch.

Discussion
----------

[HttpKernel] when configuring the container add services_{env} with php extension

| Q             | A
| ------------- | ---
| Branch?       | 6.4
| Bug fix?      | no
| New feature?  | yes
| Deprecations? | no
| Tickets       | none
| License       | MIT

Hello the community

This is my first PR attempt.

So after reading this [documentation](https://symfony.com/doc/current/service_container.html#remove-services) and unsuccessfully trying to load my `service_test.php`, I've noticed that the `configureContainer(..)` function in the `MicroKernelTrait` file was not configured to automatically load this file.

So either we should fix the documentation, either we should fix the configuration.

Since this the [framework-bundle](https://github.com/symfony/framework-bundle) is backed by [Alximy](https://alximy.io) I figured it would be cool 😎 to try and fix 🐛 the configuration.

Anyway share me your thoughts about what should be done !

And I wanted to say that php service configuration is 🔥 so shoutout to the one who did this (I think it's you `@nicolas`-grekas with this [PR](https://github.com/symfony/symfony/pull/23834) right ? 💪🏻)

Also big thanks to `@jeremyFreeAgent` for debugging this with me and `@HeahDude` for showing me the php service configuration PR.

Commits
-------

4aac1d9fee :bug: (kernel) when configuring the container add services with php ext

---
## [consul/consul](https://github.com/consul/consul)@[970a64e276...](https://github.com/consul/consul/commit/970a64e2762c8dd8c9e265acb9195f069ea7bb0a)
#### Friday 2023-06-30 09:52:22 by Javi Martín

Enable mousewheel when focusing on the map

Zooming with the mousewheel is useful when you want to use it, but
annoying when you don't want to.

Here we're taking an intermediary approach: by default, the mousewheel
isn't active, but it will be active after focusing on the map, so it can
be used both to scroll and to zoom.

This behavior presents usability issues, though, since we aren't making
users aware of the way the mousewheel works, and even if they were
aware, it could be confusing anyway. However, I currently think it's
better than always enabling or always disabling the mousewheel (might
change my mind, though).

Note that the "focus" event is only used on the map, so if we click on a
marker or navigate to a marker with the keyboard without focusing on the
map first, the mousewheel isn't enabled. The same would happen if we
used the "click" event.

We might use the Leaflet.GestureHandling plugin in the future to deal
with this issue and the scroll on touch screens.

---
## [enzymical/tos](https://github.com/enzymical/tos)@[32c5f6c865...](https://github.com/enzymical/tos/commit/32c5f6c865d750f944a06a891c60aa13cf70a9e5)
#### Friday 2023-06-30 10:55:16 by Me

im going insane
fuck you fuck you fuck you fuck you fuck you fuck you fuck you

---
## [Soilorian/strongholdlibGDX](https://github.com/Soilorian/strongholdlibGDX)@[088686d92a...](https://github.com/Soilorian/strongholdlibGDX/commit/088686d92a5a86d0505ae7bfa347d8e3af7444df)
#### Friday 2023-06-30 12:03:26 by arminkh83

God please send our objects right to fucking heaven

---
## [cilium/linux](https://github.com/cilium/linux)@[d0c60e2a34...](https://github.com/cilium/linux/commit/d0c60e2a34fc627275d245c3f512a3c35403c008)
#### Friday 2023-06-30 12:49:17 by Daniel Borkmann

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
or both to cleanly co-exist where needed given its all one logical tc layer.
tcx supports the simplified return codes TCX_NEXT which is non-terminating (go
to next program) and terminating ones with TCX_PASS, TCX_DROP, TCX_REDIRECT.
The fd-based API is behind a static key, so that when unused the code is also
not entered. The struct tcx_entry's program array is currently static, but
could be made dynamic if necessary at a point in future. The a/b pair swap
design has been chosen so that for detachment there are no allocations which
otherwise could fail. The work has been tested with tc-testing selftest suite
which all passes, as well as the tc BPF tests from the BPF CI, and also with
Cilium's L4LB.

Kudos also to Nikolay Aleksandrov and Martin Lau for in-depth early reviews
of this work.

  [0] https://lpc.events/event/16/contributions/1353/
  [1] https://lore.kernel.org/bpf/CAEf4BzbokCJN33Nw_kg82sO=xppXnKWEncGTWCTB9vGCmLB6pw@mail.gmail.com/
  [2] https://colocatedeventseu2023.sched.com/event/1Jo6O/tales-from-an-ebpf-programs-murder-mystery-hemanth-malla-guillaume-fournier-datadog
  [3] http://vger.kernel.org/bpfconf2023_material/tcx_meta_netdev_borkmann.pdf
  [4] https://lore.kernel.org/bpf/20210604063116.234316-1-memxor@gmail.com/

Signed-off-by: Daniel Borkmann <daniel@iogearbox.net>

---
## [JohnFulpWillard/tgstation](https://github.com/JohnFulpWillard/tgstation)@[8788e48378...](https://github.com/JohnFulpWillard/tgstation/commit/8788e483788db2432b9649313efc9426d324379f)
#### Friday 2023-06-30 12:58:43 by Time-Green

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
## [dfinity/motoko](https://github.com/dfinity/motoko)@[b0f5aee3c7...](https://github.com/dfinity/motoko/commit/b0f5aee3c71c66f01aaad12cabe39928b043b829)
#### Friday 2023-06-30 13:08:18 by Claudio Russo

feat: allow canister imports of service constructors, silently ignoring the service arguments. (#4041)

Allow canister imports of service constructors, silently ignoring the service arguments. 

A hack that fixes #3990 (for some definition of fix) and duplicate #2319.

Really, dfx should be feeding the idl of the instantiated service, not service constructor, to dependent canisters, but until it's fixed to do so (and it hasn't been forever now), this is a reasonable and simple workaround, avoiding the error-prone and kludgy workaround of rewriting candid files described, for instance, here:

https://dfinityorg.notion.site/ckBTC-example-Encode-Hackathon-0aaf6292e3404dabb49df5d1b5abc797#08a7469beaf14d6ba35e8827e363e160

and also used here:

https://github.com/letmejustputthishere/ckbtc-payments

via npm scripting hacks (!).

Also see here for the pain this caused:

https://forum.dfinity.org/t/confusing-type-error-when-crossing-canisters-expression-of-type-mytype-cannot-produce-expected-type-mytype-1/20636

UPDATE: I turned the previous error into a warning to nag us to fix dfx.


UPDATE: Potentially obviated by https://github.com/dfinity/sdk/pull/3138, which teaches dfx to strip the service argument.

UPDATE: @chenyan-dfinity thinks we should still merge for other scenarios (old dfx, new compiler, I guess).

---
## [Luap99/libpod](https://github.com/Luap99/libpod)@[c7a5a9b417...](https://github.com/Luap99/libpod/commit/c7a5a9b41752342502588cb259421695de7a2308)
#### Friday 2023-06-30 13:13:18 by Paul Holzinger

top: do not depend on ps(1) in container

This ended up more complicated then expected. Lets start first with the
problem to show why I am doing this:

Currently we simply execute ps(1) in the container. This has some
drawbacks. First, obviously you need to have ps(1) in the container
image. That is no always the case especially in small images. Second,
even if you do it will often be only busybox's ps which supports far
less options.

Now we also have psgo which is used by default but that only supports a
small subset of ps(1) options. Implementing all options there is way to
much work.

Docker on the other hand executes ps(1) directly on the host and tries
to filter pids with `-q` an option which is not supported by busybox's
ps and conflicts with other ps(1) arguments. That means they fall back
to full ps(1) on the host and then filter based on the pid in the
output. This is kinda ugly and fails short because users can modify the
ps output and it may not even include the pid in the output which causes
an error.

So every solution has a different drawback, but what if we can combine
them somehow?! This commit tries exactly that.

We use ps(1) from the host and execute that in the container. Now
unfortunately because ps(1) is dynamically linked (at least on the
mainstream distros) this is not trivial.

The trick here is in theory simple, open the binary on the host then we
have a fd for it and can refer to the path via /proc/self/fd/<NUM>.
Now join the container mount and pid ns then simple execute the fd path.
That fails quickly because the linker will try to load the shared libs
and because we are in a different mount ns that fails.
Now to solve this we use the same trick with the LD_PRELOAD variable
basically to make the linker load the opened libs on the host via the fd
paths. Except that still don't works because even the linker in the
container can be different. Compare glibc vs musl based distros.
So we first have to get the right linker path and open this one as well
in order to execute it directly.

Now because we execute the linker directly we can no longer use the LD_
vars and have to set the cli arguments directly, i.e. --preload.
In order to get the actual linker path and shared libraries we first
execute ldd(1) to get the output. We can then parse that and open all
correct paths.

If we have a static binary we can skip all that and just execute it
directly on the host, we assume it is static if ldd fails.

Technically this could be a breaking change if somebody does not
have ps on the host and only in the container but I find that very
unlikely so I have removed the in container fallback.

Fixes #19001
Fixes https://bugzilla.redhat.com/show_bug.cgi?id=2215572

Signed-off-by: Paul Holzinger <pholzing@redhat.com>

---
## [Jai8429/Online-Quiz-Website](https://github.com/Jai8429/Online-Quiz-Website)@[dbef0dae97...](https://github.com/Jai8429/Online-Quiz-Website/commit/dbef0dae97d297ed2f49f9d726117a6cbd7752a2)
#### Friday 2023-06-30 13:26:53 by Jai8429

Add files via upload

An online quiz website is a digital platform designed to provide users with a wide range of interactive quizzes and trivia challenges. It offers a diverse selection of quiz topics, ranging from general knowledge and academic subjects to entertainment, sports, science, and more. The website typically incorporates engaging features and functionalities to enhance the user experience and encourage participation.

Here is a description of the key elements typically found on an online quiz website:

1. User Registration: Users can create an account on the website to track their progress, save their scores, and participate in various competitions or leaderboards. Registration may involve providing basic personal information or linking existing social media accounts.

2. Quiz Categories: The website offers a variety of quiz categories or topics, allowing users to choose their preferred subject areas. Common categories may include history, geography, movies, music, literature, technology, sports, and pop culture.

3. Quiz Creation: The platform allows quiz creators to design and publish their own quizzes, contributing to the diverse range of content available. Creators can define the number of questions, set time limits, and assign difficulty levels to their quizzes.

4. Quiz Taking: Users can browse through the available quizzes and select the ones they want to take. Each quiz typically consists of a series of multiple-choice questions or other question formats. The website provides a user-friendly interface for answering questions, submitting responses, and progressing through the quiz.

5. Score Tracking and Leaderboards: The website tracks users' scores and displays them at the end of each quiz. It may also maintain leaderboards that showcase the top scorers across different quizzes or specific categories. This feature promotes competition and motivates users to improve their performance.

6. Feedback and Explanation: After completing a quiz, users receive instant feedback on their answers, highlighting correct and incorrect responses. The website may also provide explanations or additional information to enhance users' knowledge and understanding of the quiz topics.

7. Time Challenges and Timed Quizzes: Some online quiz websites include time challenges or timed quizzes to add an extra element of excitement and test users' speed and accuracy. Users may compete against the clock to answer questions within a specified time limit.

8. Social Features: To foster community engagement, online quiz websites often integrate social features. These can include options to share quiz results on social media platforms, invite friends to participate, create or join groups, and compete against friends or other users.

9. Mobile Compatibility: Many online quiz websites are designed to be mobile-friendly, allowing users to access and participate in quizzes on their smartphones or tablets. This ensures flexibility and accessibility for users on different devices.

Overall, an online quiz website offers a fun and interactive way for users to test their knowledge, learn new facts, and engage in friendly competition. It serves as a platform for both casual and passionate quiz enthusiasts to enjoy a variety of quiz content and challenge themselves in various subject areas.

---
## [HTTP3D/WalkTheWeb](https://github.com/HTTP3D/WalkTheWeb)@[ffbc355470...](https://github.com/HTTP3D/WalkTheWeb/commit/ffbc355470a0e16d908b88f09069207b0fea3b29)
#### Friday 2023-06-30 15:07:35 by Aaron Dishno Ed.D

Updated 3.7.0

Save Avatar Cookie after Select - The save avatar cookie after the select avatar process was missing the number of days to save it. This made it disappear as it saved it. It has been corrected.

Avatar ID Cookie Saving - When a random avatar is added, the setCookie function was not setting the number of days, so the cookie expired as it was written. We added 365 days and now it works.

Pending Cookies Array - We added a global variable called WTW.pendingCookies as an array to store any cookies that would be written before the Allow Cookies prompt is answered. If answered to Allow, the array is processed and each cookie is saved. Either way you answer about the Allow or Deny Cookies, the array is cleared after.

Set Cookie Prompt Protected - The setCookie function in wtw_utilities.js now checks the prompt response with the checkAllowCookies function.

Get Cookie Prompt Protected - The getCookie function in wtw_utilities.js is now using the checkAllowCookies function before use. This has one exception, the allowcookies can be processed to see if it exists.

Replaced Delete Cookie Function - The deleteCookie function was using the setCookie function, but now it has its own stand alone code. This is due to the changes to protect the set and get cookies functions.

Added Check Allow Cookies Function - We added a checkAllowCookies function that will return a true or false depending on the prompt response and possible cookie to remember the setting if cookies were allowed.

Camera Distance Cookie - The Camera Distance cookie was being set before it was being read. This caused it to reset every time the page reopened. We removed the unnecessary set cookie in the init camera function.

Avatar for Edit Code Update - When opening an avatar for edit, the scaleold node was not setting the position and rotation. The code lines were copied from the avatarscaling, showing as a duplicate, but the avatarscalingold node needed to be set. This has been corrected.

Avatar Transition Scaling Corrected - When switching avatars, the old avatar stays until the new avatar is completely loaded. The issue was that the new avatar was resetting the scaling of the old avatar (scaleold transform node), making the avatar jump in size during the transition before it is deleted. We removed the scaling for the scaleold node when the new avatar is being added. This allows it to preserve the scaling of the old avatar while the new avatar loads.

Parent During Avatar Transition - When switching avatars, the child elements of an avatar get set to an alternate parent (-scaleold) for a short time. The code was reparenting all items, but we needed it to only parent items that are part of the current scale parent. This change preserves the sub parent structure.

Allow Cookies Prompt in Sequence - The Allow Cookies prompt has been added to the load sequence. This will make sure it is prompted before any cookies are written from the JavaScript (client) side.

Select Avatar Display Name - When viewing the select avatar 3D Form, The display name was throwing an error when you are set as anonymous. We added a condition to check if the display name or default display name is null to correct the issue. The results will now show Anonymous as the display name when the JSON call returns a null value.

Allow Cookies Prompt Added - We are now asking if the user allows cookies. The menu will show on first use, if the user selects allow cookies, cookies will be used to save user settings and preferences including this allow setting (no longer get the prompt on each visit). If the user selects deny cookies, it will not save cookies, any existing cookies will be removed, and the user will be prompted each time they visit the site. Remember that cookies include the avatar selection, instance number of the user (gives an anonymous user an identity), logins, avatar customizations, and other preferences. This update includes: new menu in class_wtwmenu.php, global variable in wtw_constructor.js, allow cookie functions in wtw_utilities.js, and calls to add the cookie menu in index.php and admin.php.

Avatar Animations Menu Size - When you long click your avatar, the optional animations horizontal scroll is shown with the animations you can play by holding one of the icons. This horizontal scroll was too wide for mobile devices. It is now properly scaling to fit your screen and you can see the close button.

Mobile Browse Menu Height - When using a mobile device in landscape orientation the browse menu was too tall for the screen causing you to not be able to close the menu. We corrected it by adding a div with a vertical overflow scrollbar and set the height when opening.

Enter Zone Process - The Enter Zone process used by the multiplayer was executing 2 times on entry of a load zone. It now uses the status to determine if it needs to run. First time it is status 0 and all following times the status is 2.

3D Avatar Required Plugins - When editing a 3D Avatar, under options and settings - ratings and requirements, the requirements section was not set to open for avatars. This section lets you set any required or optional plugins that will be used when your avatar loads. We added the condition to allow it for avatars. Now this section is available.

Animation Modes Hiding Animations - When selecting Fight Mode or returning to Normal Mode of Avatar movement (after slow click on your avatar), the list of animations to choose from were not hiding the extra animations. An OR clause was added to the avatarAnimationMode function to hide or show the appropriate animations when selected.

Avatar Animation Transitions are Faster - When an avatar changes from one movement to another there is a transition speed set by an increment that determines how fast the animation stops and the new one starts. Previously the increment was 0.2, now it is 0.5. This means that the transitions are now completing 2.5 times faster. This makes the avatar a lot more responsive to changes in direction and movement.

Avatar Walk to Position - The avatar walk to position function has been updated to watch for lack of movement as a method to cancel the walking. We also cleaned up the code by using the cancelWalkToPosition function instead of individual repeated lines of code.

Avatar Walk to Decal - When you click the ground, a decal is added to the ground and the avatar walks to it. The decal was not showing because of the rendering group. It has been corrected.

Added Cancel to Select Avatar 3D Form - We added a Cancel button to the select avatar 3D Form. This also includes the animation code, hover, and action to close the select avatar 3D Form when selected.

Table Character Set Updated - When creating the tables, the utf8 characterset has been updated to UTF8MB4 by a recommendation of MySQL. This change occurred in the main WalkTheWeb tables and all plugins maintained by WalkTheWeb.

Avatar in Groups Table Comma Issue - The avataringroups table was not being created because of a missing comma after the primary key line. This has been corrected and tested.

Avatars in Groups Table - The avatarsingroups table was not being created because of a typo in the varchar size. It said 416 when it should be 16.

Initial Install Download Size Reduction - We reduced the install file size by eliminating the duplicate avatar animation files. Therefore, in the install we now have a process that copies the animations to each of the avatar folders while respecting the unique animations for that avatar. Mostly, the onwait and dances are different per avatar and the male and female walks are also separate selections.

New Install Avatars - During the new install of WalkTheWeb, the avatars are now the latest 1.0.1 or 1.1.1 versions of the avatars consisting of 131 animations each. If you already installed, these are the same avatars you get when you update the avatars in your admin mode.

Content System Avatars folder removed - The /content/system/avatars folder has been removed. The installed avatars are now in the /content/uploads/avatars folder with other downloaded avatars.

Default Avatar Path Updated - The default avatar path has been updated to the unanimous male avatar.

Community Name loading - On occasions, the community name would error while loading. This depended on if the mobile or desktop version of the menu is being used. It now checks the availability of the element before setting the inner HTML value.

---
## [hwchase17/langchain](https://github.com/hwchase17/langchain)@[d507f71ab2...](https://github.com/hwchase17/langchain/commit/d507f71ab2aa850b48715bec41a2dceaea3ffa15)
#### Friday 2023-06-30 15:14:45 by Saleh Hindi

Add promptlayer_callback.py to be able to use PL w/ callbacks (#6149)

# Description
Instead of inheriting off of LLM objects like OpenAI to create
PromptLayer objects (eg PromptLayerOpenAI), create a single
PromptLayerCallback object. This adds support for all of langchain's
LLMs (openai, anthropic, replicate, dozens others).

This also paves the way for PromptLayer to add logging for agents,
chains, etc based on the callbacks api.

## Examples

Async Example
```python
import asyncio
openai_llm = OpenAI(
    model_name="text-davinci-002",
    callbacks=[PromptLayerHandler(
        request_id_func = request_id_func,
        pl_tags = ["openai_1!"]
    )]
)
asyncio.run(async_generate(openai_llm))

```


Replicate LLM Example
```python
# Test Replicate LLM
replicate_llm = Replicate(
    model="replicate/dolly-v2-12b:ef0e1aefc61f8e096ebe4db6b2bacc297daf2ef6899f0f7e001ec445893500e5",
    callbacks=[PromptLayerHandler(
        request_id_func = request_id_func,
        pl_tags = ["replicate_example"]
    )]
)
llm_results = replicate_llm.generate([
    "Tell me a joke 1",
    "Where is Ohio? 2",
    "Where is Ohio? 3",
])

```

Chat Model Example w/ Streaming (works w/o streaming as well)
```python
# Test OpenAIChat LLM
chat_llm = ChatOpenAI(
    temperature=0,
    streaming=True.
    callbacks=[PromptLayerHandler(
        request_id_func = request_id_func,
        pl_tags = ["chatopenai"]
    )]
)
llm_results = chat_llm([
    HumanMessage(content="What comes after 1,2,3 ?"),
    HumanMessage(content="Tell me another joke?"),
])
```

TODO:
- Add documentation + sample notebook
- Might also want to test streaming works

<!--
Thank you for contributing to LangChain! Your PR will appear in our
release under the title you set. Please make sure it highlights your
valuable contribution.

Replace this with a description of the change, the issue it fixes (if
applicable), and relevant context. List any dependencies required for
this change.

After you're done, someone will review your PR. They may suggest
improvements. If no one reviews your PR within a few days, feel free to
@-mention the same people again, as notifications can get lost.

Finally, we'd love to show appreciation for your contribution - if you'd
like us to shout you out on Twitter, please also include your handle!
-->

<!-- Remove if not applicable -->

#### Before submitting

<!-- If you're adding a new integration, please include:

1. a test for the integration - favor unit tests that does not rely on
network access.
2. an example notebook showing its use


See contribution guidelines for more information on how to write tests,
lint
etc:


https://github.com/hwchase17/langchain/blob/master/.github/CONTRIBUTING.md
-->

#### Who can review?

Tag maintainers/contributors who might be interested:

<!-- For a quicker response, figure out the right person to tag with @

  @hwchase17 - project lead

  Tracing / Callbacks
  - @agola11

  Async
  - @agola11

  DataLoaders
  - @eyurtsev

  Models
  - @hwchase17
  - @agola11

  Agents / Tools / Toolkits
  - @hwchase17

  VectorStores / Retrievers / Memory
  - @dev2049

 -->

---------

Co-authored-by: jped <jonathanped@gmail.com>

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[db9c105d57...](https://github.com/TaleStation/TaleStation/commit/db9c105d57a87ff344452b1fcde39dd2c5a249b4)
#### Friday 2023-06-30 15:46:39 by TaleStationBot

[MIRROR] [MDB IGNORE] Coroner Update: Pickle-Eating Morbid Weirdo Obsessed with Death and Perfectionism (#6530)

Original PR: https://github.com/tgstation/tgstation/pull/76318
-----
## About The Pull Request

This PR introduces a whole bunch of Coroner and Morbid related content.

Firstly, Morbid is now a mind trait, and specifically, coroners start
with it.

Coroners also have a liver trait that allows them to heal toxins (very
slowly) from eating pickles and drinking pickle juice. They also
can...drink formaldehyde. I guess. Dissections is thirsty work.

Coroners gain a whole set of special tools specifically for use in any
surgeries marked as interests of the Morbid. This is determined by the
``surgery_flag`` called ``SURGERY_MORBID_CURIOSITY``. Currently, these
surgeries are included;

dissections, autospies, revival surgery, plastic surgery, organ/feature
manipulations, amputations

To fit the theme, TRAIT_MORBID also applies the reduction to eye
snatchers.

While using their special tools, and the surgery is a morbid curiosity,
the coroner/anyone who is morbid gains a 30% speed boost! This stacks
with the dissection speed boost. Otherwise, the tools are just regular
tools with a special name (though the scalpel is better at killing
undead, because, you know, you're watching over the dead).

The coroner's special medkit, which is the only one you can get in a
round, can fit their autopsy scanners and tools. Anything that comes
standard with their kit can go back into it.

Anyone who is morbid can safely retrieve the secrets of the elephant
graveyard. The serrated shovel, notably, is a much better tool and
notably better at killing organics, but not inorganics (like the dead).

(Gives roboticists secure morgue access during skeleton crew pop totals)

## Why It's Good For The Game

I really loved the coroner role and what it had going conceptually. And
well, I can't help but come back over and start adding some QOL updates
and some content to flesh it out and encourage a specific role for the
coroner to play.

That utterly deranged freak in the morgue who seems very much intent on
playing god and artist in equal measure.

So, to encourage these players to look for and perform specific
surgeries, they are penalized for the more typical work done by medical
staff, but they are handsomely rewarded for doing some of the more
unique surgeries we have. While this expands their role a little beyond
just tending the dead, I think this is perfectly fine as a kind of
special side content additive.

This is also very true if we want to make sure coroners are sought out
for their ability to contribute to medical's success via dissections.
But I think having people look to them for frankensteining is also very
thematic. Especially if they get more than they bargained for by doing
so.

I thought them loving pickle juice was funny because they're pickling
people all round. **This has no relation to any sentient pickles, fuck
off with that shit.**

Also I had like maybe 4 or 5 people ask me to do this since the vorpal
scythe pr so I knew this was rather anticipated.

## Changelog
:cl:
add: Coroners are now Morbid!
add: Coroners come with a series of special tools that are especially
good at performing certain surgeries if used by a Morbid individual
(which the coroner happens to be). They are found in the coroner's
medkit.
add: The sorts of surgeries they enjoy are; dissections, autospies,
revival surgery, plastic surgery, organ/feature manipulations,
amputations. Also eyesnatching.
add: Coroners therefore hate; tending the wounds of the living,
defibrillation and CPR. Why waste so much effort on breathers if you
can't even carve them up a bit first?
add: Coroners love pickles and pickle juice.
add: The coroner can finally put their autopsy scanner into their
special medkit. Not the compact one, though.
add: The elephant graveyard is safer to plunder for the morbid
individual. The rewards from the graveyard are now also slightly more
lucrative...if you don't care about being cursed, that is.
balance: Roboticists get secure morgue access during skeleton shifts
/:cl:

---------

Co-authored-by: necromanceranne <40847847+necromanceranne@users.noreply.github.com>

---
## [chicagogrimreaper/void](https://github.com/chicagogrimreaper/void)@[ac581ef20d...](https://github.com/chicagogrimreaper/void/commit/ac581ef20d9a822cba49bed3421fb6ed8ed74d44)
#### Friday 2023-06-30 15:56:35 by setfenv

blizexK fuck you next time pay me

always ends up w me leaking the src cuz blizex a bitch XD

---
## [keerthikamurugan/foodtruck](https://github.com/keerthikamurugan/foodtruck)@[b48ac21ba5...](https://github.com/keerthikamurugan/foodtruck/commit/b48ac21ba53a2d2ef3d05376ba9c3f9519027ec7)
#### Friday 2023-06-30 17:31:10 by keerthikamurugan

Add files via upload

Welcome to the world of Food Truck delights! Our food truck, aptly named "Foodtruck," is a culinary journey like no other. With wheels that take it from one location to another, we bring an exciting array of delectable dishes right to your doorstep! As you explore our website, you'll be greeted with a visually appealing experience. By simply touching the card images, a tantalizing collection of food visuals will unfold before your eyes, tempting your taste buds and making you crave for more.

Our user-friendly interface allows you to access our extensive menu with just a click. Once you venture into the menu page, you'll be delighted to find a wide selection of mouthwatering treats, carefully curated to suit every palate. From sizzling street tacos bursting with flavor to gourmet burgers loaded with savory toppings, our food truck offers a diverse range of cuisines that cater to all tastes.

What sets "Foodtruck" apart is the commitment to quality and freshness. Our culinary team ensures that every dish is prepared with love and attention to detail, using only the finest ingredients sourced from local farmers and suppliers. The fusion of flavors and unique culinary creations promise an unforgettable dining experience.

Whether you're a devoted foodie or simply looking for a quick and delicious bite, "Foodtruck" has something to offer for everyone. So join us on this gastronomic adventure and let the flavors of the world come to you. With a minimalist website designed using only HTML and CSS, we have kept the focus on what truly matters – the incredible food journey that awaits you. So, don't wait any longer; hop aboard our virtual food truck and embark on a scrumptious ride of flavors, memories, and endless culinary delights!

---
## [MTandi/tgstation](https://github.com/MTandi/tgstation)@[daa33d89fe...](https://github.com/MTandi/tgstation/commit/daa33d89fef10650f89f7db160f110141ab99e5d)
#### Friday 2023-06-30 18:56:00 by IndieanaJones

Xenomorph/Alien Rework 2023: Part 1 (#75286)

## About The Pull Request

Alternative to #75277

Kept you waiting, huh?

This PR is the first part of a Xenomorph rework which seeks to make the
big lugs more balanced and up to date with /tg/'s current design. This
mainly involves curtailing xenomorph's infamous hardstuns into more
interactive forms of combat, while also giving some buffs to the
xenomorph's more unique abilities in order to keep them threatening.

Part 1 will focus on simple number changes and some simple mechanic
changes. In the future, changes will be made to endgame involving
xenomorphs, along with changes to other facets of Xenomorphs.

Highly based off of #55937.

Changes:

- Xenomorph disarm has been completely reworked. While a disarm will
attempt to, well, disarm, a human opponent should they be holding
something, it will no longer immediately hardstun targets when they
aren't. Instead, the xenomorph will shove the target several tiles back
and inflict 35 stamina damage. If the target slams into a wall, this
will also come with the added effect of knocking them down. If a human
is incapacitated, however, right click will slam them into the ground,
which paralyzes them for a lengthy 5 seconds (which is ultimately half
the time xenos could stun you for before), allowing for safe transport
back to the nest as long as you keep them close.

- Humans can now shove xenomorphs. Due to being the superior predator,
however, you can't knock down xenomorphs from shoving. You can slow them
for a little bit akin to humans though.

- Neurotoxin no longer is a hardstun. Instead, it deals 50 stamina
damage on contact. It is still resisted by BIO armor.

**HUNTER:**
- Speed reduced from -1 to -0.3.
- Pounce speed is twice as fast as before (1 to 2)
- Hardstun time on pounce reduced from 10 seconds to 5 seconds.

Hunters being insanely fast has been a major balance-ruining factor of
xenomorphs for many years now. These buggers could practically ambush
anyone, hardstun them immediately, and then leave before anyone could do
anything. Now, with their speed nerfed and in combination with the xeno
shove changes, hunters will need to spend more time to down a target.
Their pounce was practically useless, so its been sped up in order to
make it more practical to use.

**SENTINEL**
- Speed reduced from 0 to 0.2
- Cloak alpha reduced from 0.75 to 0.25 (you're more hidden now)

Sentinels receive a large nerf in regards to their spit, but their
before useless cloaking ability has been greatly improved upon as
compensation. They now serve better as defenders and ranged ambushers.

**XENOMORPH DRONE**
- No changes

As in the original PR, drones are perfeclty balanced in my eyes, so no
changes were required.

**XENOMORPH PRAETORIAN**
- Speed increased from 1 to 0.5
- No changes

Praetorians get affected by the nerfs of the other xeno abilities, but
now they're a bit faster in order to close the gap to use their
abilities.

**XENOMORPH QUEEN**
- Speed increased from 3 to 2
- Health increased from 400 to 500
- Damage increased from 20 to 50

Xenomorph queens have been sped up and made more tanky and lethal in
close-range combat. Fighting this beast up-close should be a death
sentence to almost anything else in the game. Speed increases will help
her re-position and close the gap on potential prey.

**OTHER CHANGES**
- Fixed a bug where simplemobs didn't actually use xenomorph's damage
values when they were attacked by them.

## Why It's Good For The Game

Xenomorphs are old, and haven't been updated for quite a long time. This
has left them as sources of a bunch of hardstuns which made counterplay
from a modern spaceman extremely difficult. With these changes, fighting
xenomorphs is more interactive and should end up being more enjoyable
for both crew and xenos. Buffs were also given out to incentivize usage
of xenomorph's unique abilities as opposed to the standard disarm spam
which was most effective for them until now.

## Changelog
:cl:
balance: Xenos have been rebalanced, removing their hardstuns on their
disarm and neurotoxin, along with a slew of other changes. Xenos have
received buffs to their more unique abilities in return.
fix: Fixed simplemobs ignoring xenomorph's melee damage values when
being attacked by them.
/:cl:

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[ecf377876d...](https://github.com/git-for-windows/git/commit/ecf377876d29b0bf0fc849d0fd74a0ec18eb2345)
#### Friday 2023-06-30 19:58:59 by Johannes Schindelin

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
## [SomeRandomOwl/tgstation](https://github.com/SomeRandomOwl/tgstation)@[64eae49042...](https://github.com/SomeRandomOwl/tgstation/commit/64eae49042dea956b46ae013a0c96a891c026a7f)
#### Friday 2023-06-30 20:09:58 by necromanceranne

Replaces the Reaper Scythe with the Vorpal Scythe (also the Morbid trait) (#75948)

adds the Vorpal Scythe, a special chaplain null rod variant, replacing
the Reaper Scythe, a not so special null rod variant.

When you choose the vorpal scythe, it comes as a shard that you implant
into your arm, similar to a cursed katana.

Once implanted, you can draw it at any time like an arm implant.
However, sheathing it again presents some problems. (Also, implanting
the organ gives you ``TRAIT_MORBID``, which I'll explain in a bit)

The Vorpal Scythe has 10 force, one of the weakest null rod variants for
force that isn't a joke null rod. However, it has exceptional armor pen
and also has 2 tiles of reach. So quite unique.

It also has a special beheading ability when you right-click someone.
This borrows some code from amputation shears, functioning pretty
similarly, except with a few additional ways to speed up the action and
restrictions. (It takes 15 seconds baseline to behead someone standing
and conscious, and speeds up or slows down based on factors such as
incapacitation and whether or not our scythe is already empowered)

When you successfully behead someone with a mind, the vorpal scythe
gains 20 force and can be safely stowed and drawn for 2 minutes.
Performing more death knells like this will reset the timer.

If it has not performed its 'death knell', or you haven't hit a living
mob, then it will cause severe damage to you if you ever try and stow it
(or its forced back into your arm). Just hitting a mob with the scythe
will sate it for 4 minutes. Unless it is a non-player monkey. Horrible
things. Just hitting mobs does not reset the timer on empowerment.

What this means is that the chaplain may be more hesitant to simply draw
their weapon on people. It also means that potentially, the chaplain
will not always have magic immunity, since they may end up stowing the
weapon away and be reluctant to draw it on a whim without either taking
damage for sheathing it without hitting something, or dealing with
having one less hand up until they can.

While empowerment only happens when you behead mobs with a mind,
beheading monkeyhumans and other mindless humans subtypes causes their
heads to become haunted! It's mostly harmless and largely just SpOoKy.
We don't want heads with actual players in them to go floating off to
space. (Does not work on monkey heads for sanity reasons)

When you have the Morbid trait, you think creepy stuff is cool and hate
saving peoples lives. You get a mood boost from graverobbing, autopsies,
dissections, amputations (including beheadings with the scythe and
amputations with the shears) and revival surgery. However, you get a
mood penalty when you tend wounds on the living, as well as a hefty
penalty when you perform CPR or defibrillate someone. I was thinking
Victor Frankenstein when I was choosing which actions had an associated
moodlet, so anything that I might have missed would be appreciated.

You also count as potentially cool with regards to haunted objects.
Ghosts think you're neat. (Revenants probably will still kill you if
they had the chance)

---
## [norsvenska/tgstation](https://github.com/norsvenska/tgstation)@[867c217c57...](https://github.com/norsvenska/tgstation/commit/867c217c57bbcbb644e06bfcb6d362e494a895ee)
#### Friday 2023-06-30 20:53:14 by GuillaumePrata

New Wizard spell "branch": Vendormancy (#75679)

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

Co-authored-by: Time-Green <7501474+Time-Green@users.noreply.github.com>

---
## [Cheshify/tgstation](https://github.com/Cheshify/tgstation)@[988a6dcc21...](https://github.com/Cheshify/tgstation/commit/988a6dcc2142b4ef3244a18ad4e1781671fb7320)
#### Friday 2023-06-30 21:42:20 by YehnBeep

Removes suicide check from positronic brains (#76081)

# About The Pull Request

This removes the suicide check from positronic brains.

# Why It's Good For The Game

There seems to be 2 arguments for why suicide should forbid ghost roles:
1. "If they suicided they didn't want to play"
2. "antag rolling"

So let's look at each.

And an addendum on scope: This is meant only to apply to ghost roles
(and new characters from said roles); I do not wish to change that
people are not allowed back onto the same character they suicided on.

## "Suiciders left the round of their own choice and shouldn't be
allowed back in"

There are many, many ways in this game to end up with a character in a
state that's nearly/effectively unplayable, even if the controlling
player doesn't truly wish to completely leave. Some things can be
resolved with competent medical or science staff, but competent staff
are not always available in a round or might be beleaguered by round
events.

Then there are a number of conditions/states which the game provides no
path to resolve (save drastic measures like abandoning the
character/body, of course).

Or one might have simply become stuck in a place where rescue is
unlikely.

## Antag rolling

The problem here is this code does not particularly target antag
rollers. It paints such a broad brush that it simply catches everyone
whom might not know "No no, you have to **ghost** here, not suicide".
Even if an antag roller is stopped once, they'll easily bypass it next
time through the many, many means open to them - and if 'ghost' is made
effectively the same as 'suicide', it simply punishes people who got
stuck or similar even more.

Because of the wide range of means to kill oneself on a normal
character, to effectively stop antag rolling requires discerning intent
through context and patterns of one's actions. This might not be
possible in code until General Intelligence is a solved problem, and if
it is possible, this doesn't do it. It's a shotgun that kills everyone
in the room and if there happened to be an antag roller there, well,
even a stopped clock is right twice a day.

And then, of course, that the code was broken for so long would seem to
indicate it's not done that much.

## Practical Impact and Design Philosophy

Just from my personal observations, even wanting into a posibrain is a
niche thing usually only taken by a small number of the same players
round-to-round. In practice, whether this PR is merged or not likely
won't have a great impact on the game. But that could change if the
philosophy behind this check is applied to a wider number of things.

If someone wants to die, it's not hard. Walk out an airlock. Into the
supermatter. Blob, Xenos, or some other hazard present? Walk towards
them. Step in front of a shuttle. Turn on internals and wait a bit.
Countless other ways. Except, perhaps, if a character is disabled or
crippled or stuck, in which case use of a verb may be necessary.

In other games with much narrower sets of mechanics, it may be possible
to close certain paths on the assumption it would mostly be used for bad
faith reasons. In SS13, the sheer number of ways in which a good faith
character be "screwed" but not quite killed off, and which a bad faith
actor can find to kill themselves while bypassing restrictions placed on
verbs, means that I think this code's design philosophy is harmful to
the game and its good faith players.

# Changelog

:cl:
del: Positronic brains no longer check for suicide verb use.
/:cl:

---
## [Cheshify/tgstation](https://github.com/Cheshify/tgstation)@[803658dc30...](https://github.com/Cheshify/tgstation/commit/803658dc30b4445e81592daa1823a98719246269)
#### Friday 2023-06-30 21:42:20 by Rhials

Deadchat Announcement Variety Pack 2 and also some fixes to other popups (#76053)

## About The Pull Request

This adds ghost orbit popups for the following: 
- Macrobombs (or stacked microbombs) being triggered.
- HFR Meltdowns.
- Living players about to be gored by an emagged organ harvester.
- Nuclear devices being armed.
- Doomsday devices.
- Blob hosts bursting.

This also modifies the following ghost orbit popups:
- Toy hot potatoes will no longer cause a popup when armed.
- Normal spider eggs will not flash the byond window, only special egg
types.
## Why It's Good For The Game

Gives more gathering spots/information to deadchat. Let no entertaining
moment in this game go unobserved.

Spider eggs flashing your window for every single egg produced makes
alt-tabbing suck. I saw some guy on the forums complaining about it and
thought "huh yeah I guess he's got a point that pisses me off too" so
here we are.
## Changelog
:cl: Rhials
qol: Basic spider eggs no longer flash the byond window when ready to
hatch.
qol: Toy hot potatoes no longer give a ghost notification.
qol: Deadchat will be notified in the event of an imminent macrobomb
detonation, HFR meltdown, organ harvesting,
qol: Deadchat will be notified when a nuclear/doomsday device is
activated, as well as when a blob-infection bursts.
/:cl:

---
## [RdStudios9145/Minecraft](https://github.com/RdStudios9145/Minecraft)@[bda44408f4...](https://github.com/RdStudios9145/Minecraft/commit/bda44408f4d30c955f0ae0b9cc7b19c0deea2f62)
#### Friday 2023-06-30 23:07:20 by RdStudios

OH MY FUCKING GOD COLLISION RESPONSE FINALLY KINDA WORKS

Not completely working though

---
## [Imaginos16/Shiptest](https://github.com/Imaginos16/Shiptest)@[18819cc7fb...](https://github.com/Imaginos16/Shiptest/commit/18819cc7fb78eb4eaf11691e4a07b1294b76358a)
#### Friday 2023-06-30 23:45:08 by zevo

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
## [Imaginos16/Shiptest](https://github.com/Imaginos16/Shiptest)@[0e6f7fa646...](https://github.com/Imaginos16/Shiptest/commit/0e6f7fa64649dfbf52b8e4b71756e6625e50fdd0)
#### Friday 2023-06-30 23:45:08 by Imaginos16

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

