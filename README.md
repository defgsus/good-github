## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-04-21](docs/good-messages/2022/2022-04-21.md)


1,827,605 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,827,605 were push events containing 2,918,981 commit messages that amount to 210,241,394 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 46 messages:


## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[cd1b891d79...](https://github.com/tgstation/tgstation/commit/cd1b891d79c08b87ebcecf0a4f1656e386bd3eab)
#### Thursday 2022-04-21 00:02:51 by magatsuchi

Modular Tablets: Converting PDAs to the NtOS System (#65755)

Converts PDA functions and applications over to modular tablets and devices, namely the messaging function. HREF data code is quite honestly clunky and difficult to work with, as I've definitely experienced whilst working on this. By moving from this system over the easier to read (and frankly, easier to add to) TGUI system, you get cleaner looking and more user friendly UIs and a greater degree of standardization amongst other UIs.

Co-authored-by: Seth Scherer <supernovaa41@gmx.com>
Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>
Co-authored-by: Aleksej Komarov <stylemistake@gmail.com>

---
## [ZephyrTFA/tgstation](https://github.com/ZephyrTFA/tgstation)@[d411393e72...](https://github.com/ZephyrTFA/tgstation/commit/d411393e72586ba70ac45b8af19d9b3b701e58c9)
#### Thursday 2022-04-21 00:03:49 by Zytolg

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
## [ZephyrTFA/tgstation](https://github.com/ZephyrTFA/tgstation)@[4652d4bb63...](https://github.com/ZephyrTFA/tgstation/commit/4652d4bb63cec6f73bc46a0ea75d867d235107d1)
#### Thursday 2022-04-21 00:03:49 by Jolly

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
## [ZephyrTFA/tgstation](https://github.com/ZephyrTFA/tgstation)@[b86cf89125...](https://github.com/ZephyrTFA/tgstation/commit/b86cf89125a425ad650abedf436bb02918c36dcd)
#### Thursday 2022-04-21 00:03:49 by Aleksej Komarov

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
## [slarew/linux](https://github.com/slarew/linux)@[38b0bd0f25...](https://github.com/slarew/linux/commit/38b0bd0f251010073efb3fc37a708ae9079bb332)
#### Thursday 2022-04-21 00:50:35 by Linus Torvalds

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
## [mszeles/a-hamunish-humanish-thoughtishish](https://github.com/mszeles/a-hamunish-humanish-thoughtishish)@[d9178a8689...](https://github.com/mszeles/a-hamunish-humanish-thoughtishish/commit/d9178a86893f9a5e9a5c8dcda7baa44fe3ed0067)
#### Thursday 2022-04-21 01:01:54 by MSzeles

Minnie: Wow, Miki. This title really caught my attention.
Miki: Yeah, you know, MatchyT came up with this title.
Minnie: I love that guy. He is a genious.
Miki: Well, I would not go that far, but I have to admit, he is doing his job pretty well.
Minnie: Miki! Have you heard Hashnode has a writing competition with $3000 price for the best article?
McMuck: No waaaay. We have to participate in this challenge.
Miki: Actually, this article will be my submission, but do not be happy about the money.
McMuck: Why?
Miki: As in case we will win we will spend it on a 32 channel EEG device?
McMuck: Nooooo. We should ask the vendor to support our project with free devices.
Miki: We will, but first we have to prove we do deserve those samples.
McMuck: How will you do that?
Nikolai: You won't be able to do that.
Miki: With the Blinkish tp Textish project.
Nikolai: That will never work, you do not even have an EEG device.
Miki: That is true, but my Muse S is already under transportation and it will arrive in the upcoming days.
Minnie: I am so excited about that.
Manality: I can't wait to get data directly from our brain. Pretty cool.
Mictor: Mustard. Brainmustard.

---
## [Okto3/brickpi2022](https://github.com/Okto3/brickpi2022)@[9043ff267c...](https://github.com/Okto3/brickpi2022/commit/9043ff267c44d655168e75cecfa4219f722604af)
#### Thursday 2022-04-21 01:37:59 by Brad Nielsen

I believe in God, the Father Almighty, Creator of Heaven and earth; and in Jesus Christ, His only Son Our Lord, Who was conceived by the Holy Spirit, born of the Virgin Mary, suffered under Pontius Pilate, was crucified, died, and was buried.

---
## [Paxilmaniac/Skyrat-tg](https://github.com/Paxilmaniac/Skyrat-tg)@[51acee2a18...](https://github.com/Paxilmaniac/Skyrat-tg/commit/51acee2a1841156e4d0ce9b2b9e9d3cd4fc9a7d8)
#### Thursday 2022-04-21 01:38:37 by GoldenAlpharex

The MODsuit Digital Revolution: Replaces AIs in MODsuits with pAIs (#11135)

* Replaces AIs in MODsuits with pAIs

* Whoops forgot to remove that

* Lmao begone spellcheck shit

* I may be stupid

* Removing comments that commented code when they didn't really need to.

* Stupid linters

* Fixed the fact that mod wasn't a variable of the module anymore

---
## [Wimmerer/Yggdrasil](https://github.com/Wimmerer/Yggdrasil)@[b1469b44df...](https://github.com/Wimmerer/Yggdrasil/commit/b1469b44df4c63961a6c0f0387a89ef4ef24aa26)
#### Thursday 2022-04-21 01:40:04 by Elliot Saba

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
## [Stalkeros2/Skyrat-tg](https://github.com/Stalkeros2/Skyrat-tg)@[8d3cddc6a8...](https://github.com/Stalkeros2/Skyrat-tg/commit/8d3cddc6a8bcf438d8f3ca18eefe7e27ca40e06c)
#### Thursday 2022-04-21 01:43:05 by SkyratBot

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
## [kjopnfer/OvermorrowMod](https://github.com/kjopnfer/OvermorrowMod)@[7047ec0eb9...](https://github.com/kjopnfer/OvermorrowMod/commit/7047ec0eb9db376b54b666d13fb87041bf14b290)
#### Thursday 2022-04-21 02:23:14 by VintageM8

Fuck you old shitty theme, no one loves you. Go die in the trash

---
## [Laboredih123/tgstation](https://github.com/Laboredih123/tgstation)@[0e904f7032...](https://github.com/Laboredih123/tgstation/commit/0e904f70328a460af310014891eaadb5968ec31a)
#### Thursday 2022-04-21 02:30:20 by LemonInTheDark

[MDB IGNORE] Moves non floor turfs off /floor. You can put lattices on lavaland edition (#65504)


About The Pull Request

Alternative to #65354

Ok so like, there was a lot of not floor types on /floor. They didn't actually want any of their parent type's functionality, except maybe reacting to breaking (which was easy to move down) and some other minor stuff.
Part of what we don't want them to have is "plateable" logic.
I should not be able to put floor tiles on the snow and be fine. It's dumb.

Instead, I've moved all non floor types down to a new type, called /misc.

It holds very little logic. Mostly allowing pipes and wires and preventing blob stuff.
It also supports lattice based construction, which is one of the major changes here. I think it makes more sense, and it fixes an assumption in shuttle code that assumed you couldn't place "a new tile" by just hitting some snow with a floor tile.
Oh and lattices don't smooth with asteroid tiles anymore, this looks nicer I think.

Moving on to commits, and minor changes

Changes clf3 to try and burn any turfs it's exposed to, instead of just floors
Moves break_tile down to the turf definition, alongside burn_tile
If you're in basic buildmode and click on anything that's not handled in a targeted way, you just build plating
FUNCTION CHANGE: you can't use cult pylons to convert misc tiles over anymore
Generalizes building floors on top of something into two helper procs on /turf/open, reducing copypasta
Adds a new turf flag, IS_SOLID, that describes if a turf is tangible or not.
Uses this alongside a carpet and open check to replace plating and floor checks in carpet code. This does mean that non iron tiles can be carpeted, but I think that's fine

Moves the /floor update_icon -> update_visuals call to /open
This change is horrificly old, dating back to 8e112f6 but that commit describes nothing about why it was done. Choosing to believe it was a newfriend mistake. Uncomfortable nuking it though, because of just how old it is. Moving down instead

Create a buildable "misc" type off open, moves /dirt onto it
Basically, we want a type we can use to make something support
construction, since that can be a messy bit of logic. Also enough
structure to set things up sanely.

I'm planning on moving most misc turfs onto it, if only because
constructing on a dirt tile with rods should be possible, and the same
applies to most things

Murders captain planet, disentangles /turf/open/floor/grass/snow/basalt

Adds a diggable component that applies the behavior of "digging"
something out from a turf.

Uses it to free the above pain typepath into something a bit more
sensible

The typepaths that aren't actually used by floor tiles are moved onto
/misc

The others are given names that better describe them, and kept in
fancy_floor

Oh and snowshoes don't work on basalt anymore, sorry

Snowed over platings now actually have broken/burned icon states, fixing black holes to nowhere

Misc turfs no longer smooth as floors, so lattices will ignore them

Placing a lattice will no longer scrape the tile it's on

Ok this is a really old one.
I believe this logic is a holdover from kor's baseturf pr
(97990c9)
It used to be that turfs didn't have a concept of "beneath" and instead
just decided what should be under them by induction. This logic of "if
it's being latticed scapeaway to space" made sense then, but has since
been somewhat distorted

We do want to scape away on lattice spawn sometimes, mostly when we're
being destroyed, but not always. We especially don't want to scape away
if someone is just placing a rod, that's dumb.

Adds a path updating script for this change

I've done my best to find all the errors this repathing will pull out, but I may have missed some. I'm sorry.
Why It's Good For The Game

Very old code made better, more consistent turfs for lavaland and icebox, better visuals, minor fix to snowed plating, demon banishment in lattice placement, fixes the icebox mining shuttle not being repairable
Changelog

cl
add: Rather then being tileable with just floor tiles, lavaland turfs, asteroid and snow (among other things) now support lattice -> floor tile construction
fix: Because of the above, you can now properly fix the icebox mining shuttle
refactor: Non floor turfs are no longer typed as floor. This may break things, please yell at me if it does
/cl

---
## [dsmsgms/Stockfish](https://github.com/dsmsgms/Stockfish)@[cb9c2594fc...](https://github.com/dsmsgms/Stockfish/commit/cb9c2594fcedc881ae8f8bfbfdf130cf89840e4c)
#### Thursday 2022-04-21 03:25:55 by Tomasz Sobczyk

Update architecture to "SFNNv4". Update network to nn-6877cd24400e.nnue.

Architecture:

The diagram of the "SFNNv4" architecture:
https://user-images.githubusercontent.com/8037982/153455685-cbe3a038-e158-4481-844d-9d5fccf5c33a.png

The most important architectural changes are the following:

* 1024x2 [activated] neurons are pairwise, elementwise multiplied (not quite pairwise due to implementation details, see diagram), which introduces a non-linearity that exhibits similar benefits to previously tested sigmoid activation (quantmoid4), while being slightly faster.
* The following layer has therefore 2x less inputs, which we compensate by having 2 more outputs. It is possible that reducing the number of outputs might be beneficial (as we had it as low as 8 before). The layer is now 1024->16.
* The 16 outputs are split into 15 and 1. The 1-wide output is added to the network output (after some necessary scaling due to quantization differences). The 15-wide is activated and follows the usual path through a set of linear layers. The additional 1-wide output is at least neutral, but has shown a slightly positive trend in training compared to networks without it (all 16 outputs through the usual path), and allows possibly an additional stage of lazy evaluation to be introduced in the future.

Additionally, the inference code was rewritten and no longer uses a recursive implementation. This was necessitated by the splitting of the 16-wide intermediate result into two, which was impossible to do with the old implementation with ugly hacks. This is hopefully overall for the better.

First session:

The first session was training a network from scratch (random initialization). The exact trainer used was slightly different (older) from the one used in the second session, but it should not have a measurable effect. The purpose of this session is to establish a strong network base for the second session. Small deviations in strength do not harm the learnability in the second session.

The training was done using the following command:

python3 train.py \
    /home/sopel/nnue/nnue-pytorch-training/data/nodes5000pv2_UHO.binpack \
    /home/sopel/nnue/nnue-pytorch-training/data/nodes5000pv2_UHO.binpack \
    --gpus "$3," \
    --threads 4 \
    --num-workers 4 \
    --batch-size 16384 \
    --progress_bar_refresh_rate 20 \
    --random-fen-skipping 3 \
    --features=HalfKAv2_hm^ \
    --lambda=1.0 \
    --gamma=0.992 \
    --lr=8.75e-4 \
    --max_epochs=400 \
    --default_root_dir ../nnue-pytorch-training/experiment_$1/run_$2

Every 20th net was saved and its playing strength measured against some baseline at 25k nodes per move with pure NNUE evaluation (modified binary). The exact setup is not important as long as it's consistent. The purpose is to sift good candidates from bad ones.

The dataset can be found https://drive.google.com/file/d/1UQdZN_LWQ265spwTBwDKo0t1WjSJKvWY/view

Second session:

The second training session was done starting from the best network (as determined by strength testing) from the first session. It is important that it's resumed from a .pt model and NOT a .ckpt model. The conversion can be performed directly using serialize.py

The LR schedule was modified to use gamma=0.995 instead of gamma=0.992 and LR=4.375e-4 instead of LR=8.75e-4 to flatten the LR curve and allow for longer training. The training was then running for 800 epochs instead of 400 (though it's possibly mostly noise after around epoch 600).

The training was done using the following command:

The training was done using the following command:

python3 train.py \
        /data/sopel/nnue/nnue-pytorch-training/data/T60T70wIsRightFarseerT60T74T75T76.binpack \
        /data/sopel/nnue/nnue-pytorch-training/data/T60T70wIsRightFarseerT60T74T75T76.binpack \
        --gpus "$3," \
        --threads 4 \
        --num-workers 4 \
        --batch-size 16384 \
        --progress_bar_refresh_rate 20 \
        --random-fen-skipping 3 \
        --features=HalfKAv2_hm^ \
        --lambda=1.0 \
        --gamma=0.995 \
        --lr=4.375e-4 \
        --max_epochs=800 \
        --resume-from-model /data/sopel/nnue/nnue-pytorch-training/data/exp295/nn-epoch399.pt \
        --default_root_dir ../nnue-pytorch-training/experiment_$1/run_$run_id

In particular note that we now use lambda=1.0 instead of lambda=0.8 (previous nets), because tests show that WDL-skipping introduced by vondele performs better with lambda=1.0. Nets were being saved every 20th epoch. In total 16 runs were made with these settings and the best nets chosen according to playing strength at 25k nodes per move with pure NNUE evaluation - these are the 4 nets that have been put on fishtest.

The dataset can be found either at ftp://ftp.chessdb.cn/pub/sopel/data_sf/T60T70wIsRightFarseerT60T74T75T76.binpack in its entirety (download might be painfully slow because hosted in China) or can be assembled in the following way:

Get the https://github.com/official-stockfish/Stockfish/blob/5640ad48ae5881223b868362c1cbeb042947f7b4/script/interleave_binpacks.py script.
Download T60T70wIsRightFarseer.binpack https://drive.google.com/file/d/1_sQoWBl31WAxNXma2v45004CIVltytP8/view
Download farseerT74.binpack http://trainingdata.farseer.org/T74-May13-End.7z
Download farseerT75.binpack http://trainingdata.farseer.org/T75-June3rd-End.7z
Download farseerT76.binpack http://trainingdata.farseer.org/T76-Nov10th-End.7z
Run python3 interleave_binpacks.py T60T70wIsRightFarseer.binpack farseerT74.binpack farseerT75.binpack farseerT76.binpack T60T70wIsRightFarseerT60T74T75T76.binpack

Tests:

STC: https://tests.stockfishchess.org/tests/view/6203fb85d71106ed12a407b7
LLR: 2.94 (-2.94,2.94) <0.00,2.50>
Total: 16952 W: 4775 L: 4521 D: 7656
Ptnml(0-2): 133, 1818, 4318, 2076, 131

LTC: https://tests.stockfishchess.org/tests/view/62041e68d71106ed12a40e85
LLR: 2.94 (-2.94,2.94) <0.50,3.00>
Total: 14944 W: 4138 L: 3907 D: 6899
Ptnml(0-2): 21, 1499, 4202, 1728, 22

closes https://github.com/official-stockfish/Stockfish/pull/3927

Bench: 4919707

---
## [tukkek/tactical-hell](https://github.com/tukkek/tactical-hell)@[af90dd91ba...](https://github.com/tukkek/tactical-hell/commit/af90dd91baecaec5729949eac755134eaca79a60)
#### Thursday 2022-04-21 04:04:17 by tukkek

Rebalancing gotcha boss...

I am playing on the easy difficulty, having set every favorable Obsidian option in my favor and every disadvantageous option also to my favor (including minimum boss health, maximum pickups, zero reinforcements...) and it still takes me a `idkfa` and all of my energy ammo to down the boss.

The best weapon the game will give you is a rocket launcher, so the idea that this is beatable with a pistol start seems laughable. Most players are unlikely to finish a full-episode permadeth run with full energy ammo but I guess in that case it should be feasible to finish the boss with rockets after having weakened him.

This is the furthest the options will help make a boss easier. Ammo distribution and overall balance is feeling pretty good for progress throughout the episode so I don't want to make it higher just to guarantee a final boss kill. If this proves to not be reliably beatable outside of testing, disabling the boss level might be necessary in favor of a higher but slow-curve map size range or similar alternative.

At this point I wouldn't even care if beating the boss is just a formality to end the WAD on a high note of spectacle. If the fight can't be properly balanced or at least winnable with a generous amount of pistol restarts, I'd be happy to just make it even easier and let the player enjoy a semi-guaranteed victory.

---
## [Iamgoofball/Skyrat-tg](https://github.com/Iamgoofball/Skyrat-tg)@[8b1ec33143...](https://github.com/Iamgoofball/Skyrat-tg/commit/8b1ec331432234f358b26ee1627c10358ccae6a7)
#### Thursday 2022-04-21 04:11:07 by LeonY24

P90 (#12125)

* P90 SMG

le new gun for new away mission we're planning to make

* Update p90.dm

* includes p90.dm

my fucking retard ass hadnt shit included bruh

---
## [Iamgoofball/Skyrat-tg](https://github.com/Iamgoofball/Skyrat-tg)@[20d3361f6b...](https://github.com/Iamgoofball/Skyrat-tg/commit/20d3361f6b9e81e83b1fe2b69a57713f5a81cc2e)
#### Thursday 2022-04-21 04:11:07 by SkyratBot

[MIRROR] makes podpeople spec_life call parent [MDB IGNORE] (#12106)

* makes podpeople call parent (#65362)

About The Pull Request

kinda fucked up that it doesnt.
Also while checking this PR I noticed other species also don't, kinda screwed up world we live in...
Why It's Good For The Game

Parent's spec_life is what checks if you have nobreath, and in which case it will remove all your oxygen damage and, if in crit, give you brute damage instead. Not having this makes you basically not take damage while in crit, which I think shouldn't be the case.
Changelog

cl
fix: Podpeople now take self-respiration into account when taking damage from critical condition, like most other species.
/cl

* makes podpeople spec_life call parent

Co-authored-by: John Willard <53777086+JohnFulpWillard@users.noreply.github.com>

---
## [Nirmal4G/MSBuild](https://github.com/Nirmal4G/MSBuild)@[a572dc6b79...](https://github.com/Nirmal4G/MSBuild/commit/a572dc6b796aec7d028e53aa24a82a059e47edfa)
#### Thursday 2022-04-21 04:14:41 by Forgind

Fix low priority issues (#7413)

Thanks @svetkereMS for bringing this up, driving, and testing.

This fixes two interconnected issues.
First, if a process starts at normal priority then changes to low priority, it stays at normal priority. That's good for Visual Studio, which should stay at normal priority, but we relied on passing priority from a parent process to children, which is no longer valid. This ensures that we set the priority of a process early enough that we get the desired priority in worker nodes as well.

Second, if we were already connected to normal priority worker nodes, we could keep using them. This "shuts down" (disconnects—they may keep running if nodeReuse is true) worker nodes when the priority changes between build submissions.

One non-issue (therefore not fixed) is connecting to task hosts that are low priority. Tasks host nodes currently do not store their priority or node reuse. Node reuse makes sense because it's automatically off always for task hosts, at least currently. Not storing low priority sounds problematic, but it's actually fine because we make a task host—the right priority for this build, since we just made it—and connect to it. If we make a new build with different priority, we disconnect from all nodes, including task hosts. Since nodeReuse is always false, the task host dies, and we cannot reconnect to it even though if it didn't immediately die, we could, erroneously.

On the other hand, we went a little further and didn't even specify that task hosts should take the priority assigned to them as a command line argument. That has been changed.

svetkereMS had a chance to test some of this. He raised a couple potential issues:

conhost.exe launches as normal priority. Maybe some custom task dlls or other (Mef?) extensions will do something between MSBuild start time and when its priority is adjusted.
Some vulnerability if MSBuild init code improperly accounts for timing
For (1), how is conhost.exe related to MSBuild? It sounds like a command prompt thing. I don't know what Mef is.
For (2), what vulnerability? Too many processes starting and connecting to task hosts with different priorities simultaneously? I could imagine that being a problem but don't think it's worth worrying about unless someone complains.

He also mentioned a potential optimization if the main node stays at normal priority. Rather than making a new set of nodes, the main node could change the priority of all its nodes to the desired priority. Then it can skip the handshake, and if it's still at normal priority, it may be able to both raise and lower the priority of its children. Since there would never be more than 2x the "right" number of nodes anyway, and I don't think people will be switching rapidly back and forth, I think maybe we should file that as an issue in the backlog and get to it if we have time but not worry about it right now.

Edit:
I changed "shuts down...worker nodes when the priority changes" to just changing their priority. This does not work on linux or mac. However, Visual Studio does not run on linux or mac, and VS is the only currently known customer that runs in normal priority but may change between using worker nodes at normal priority or low priority. This approach is substantially more efficient than starting new nodes for every switch, disconnecting and reconnecting, or even maintaining two separate pools for different builds.

---
## [atteria/Paradise](https://github.com/atteria/Paradise)@[6082c95eb3...](https://github.com/atteria/Paradise/commit/6082c95eb300a9f05b5422060db79f55fe91b9b3)
#### Thursday 2022-04-21 04:57:58 by LightFire53

Relocates The Entertainment Offices and Custodial Closet on DeltaStation (#17480)

* Location, Location, Location!

* Lights and Pipes

I am so sorry for how hacky that disposal piping is

* TFW Disposals

* Oh god, what if there is a fire?!

* And a light switch...

Maybe the final commit? Taking bets on if I managed to forget something else

* If you bet on the requests console

You would be right.

* Bigger, Better, Janitor

* Bloody requests console...

---
## [baldamundo/ColdWarIronCurtain](https://github.com/baldamundo/ColdWarIronCurtain)@[aa54466b9f...](https://github.com/baldamundo/ColdWarIronCurtain/commit/aa54466b9fdf0f4b0217f132f076e75f2d419103)
#### Thursday 2022-04-21 05:47:09 by baldamundo

Six Day War + UAR focus tree fixes

This is a very complex and consequently very buggy event chain, so I've annotated it to make future troubleshooting & editing easier and I've also made a few fixes. The phrasing of some of the annotations is slightly inconsistent, but that's phrasing copied and pasted from the comments in the localisation file.

The main changes are:
- the war will start a week after Egypt closes the Straits of Tiran via its focus tree - as it did historically - instead of always occurring on the same date.
- Egypt/UAR's focuses are now unlocked by the war (The Six-Day War when the war begins, Partial Liberation of Palestine when the UAR wins, an Naksah when it ends either in stalemate or Israeli victory) - previously there seemed to be no way of unlocking them at all
- the Golan Heights and West Bank sections of the conflict should now still occur if Egypt/UAR has annexed the territory of Syria and/or Jordan
- switched Syria's victory national focus to be attached with event .35 and edited event .5 so that it doesn't fire for Syria - the event was kind of redundant for Syria anyway, and having the two border conflicts share the event caused issues if one country owned both territories
- SIX_DAYS_WAR.3 is fixed to use the correctprovinces, so that border conflict can actually occur
-  SIX_DAYS_WAR.14 uses the description from SIX_DAYS_WAR.8.d, but it says you are being given a choice, even though SIX_DAYS_WAR.14 doesn't offer a choice, so the text of desc = SIX_DAYS_WAR.3.d fits better.

Known unresolved issues:
- SIX_DAYS_WAR.192 - Israeli Perspective Counter-Attack into Sinai - appears to have no trigger
- the news events are still a bit of a mess and i've not tried to fix them - some countries don't get properly notified when the war has ended (the original event chain is primarily written for Israel) or get notifications that are clearly written from the perspective of a different country
- if Jordan owns Syria's territory, or vice versa, it won't fire both border conflicts
- if an Arab power other than UAE (e.g. Iraq as the Arab Federation or a unified Arab League) owns Jordan's or Syria's territory, their border conflicts won't fire
- if Israel declines to attack, Egypt/UAE attacks alone only on the Sinai front - when historically the other Arab powers likely would have joined in
- UAR's focus description for UAR_an_Naksah describes the war as a crushing defeat, but the focus still applies even if the war is a stalemate
- UAR's focus UAR_The_Six_Days_War describes the war as an Israeli surprise attack, but it's possible for the war to play out as an Egyptian/UAE surprise attack instead.

And tbh there's probably still a lot of unresolved bugs I've missed still. I've tested it a lot of times, with different combinations of countries involved, and different paths, but it's a very complex chain and there are a lot of different possible combinations, so I've not tested exhaustively. And I'm not an experienced modder, so I'm sure things have slipped through the cracks, but it seems significantly less buggy now than before. There is probably an argument for rewriting the entire war, getting rid of all the complex chains of Border Conflicts, and just having it as a regular war with scripted peace deals, but that's above my pay grade - I was just trying to make what already exists functional.

---
## [gutbuster12/bobgluttonstation](https://github.com/gutbuster12/bobgluttonstation)@[e2cebdcca0...](https://github.com/gutbuster12/bobgluttonstation/commit/e2cebdcca064772d2ee82a5eb9110cebcd45c81a)
#### Thursday 2022-04-21 06:03:50 by Remis12

bob joga be like ahhh uhh hshut up remis go fuck yourself nigger

---
## [pa1nki113r/Project_Brutality](https://github.com/pa1nki113r/Project_Brutality)@[39b09db16b...](https://github.com/pa1nki113r/Project_Brutality/commit/39b09db16bbe225ec575ab2a118358732b755288)
#### Thursday 2022-04-21 07:04:49 by Jason Martinez

Fixed alive baron/hell knight corpse when attack by burning attack, fixed incorrect imp corpse on baron, changed some Hell Nobles smoke effects to be more performance friendly (thanks Kamil). Fixed Demon Tech Trooper pinned bug

---
## [BasicallyWiz/gogcord.moe](https://github.com/BasicallyWiz/gogcord.moe)@[373d7f8fce...](https://github.com/BasicallyWiz/gogcord.moe/commit/373d7f8fce4cd7264638852347939fa7b154f6e8)
#### Thursday 2022-04-21 07:49:28 by BasicallyWiz

A bunch of stuff, let's see if I can remember them all.
Added System.Messaging.dll for message queues.
Added a message queue object, may be removed in the future.
Started work on cookie handling via JSInterop (Fuck, this sucks so much)
Modified few pages, unsure of how to put it in more detail.
Placed some purple variables in site.css, for later use.
Debugging cookies, that's why clicking the user card at the top right behaves weird. If you create a cookie on the dom named "cool_cookie" and the cookie data shows as the username, you know it works.
Watched youtube, ate ramen noodles at a local resteraunt, and slept.
Probably spelled restaraunt wrong.

---
## [Ed640/tgstation](https://github.com/Ed640/tgstation)@[ac21ef9078...](https://github.com/Ed640/tgstation/commit/ac21ef9078d88f51a4e198e394ed56e3cc731b45)
#### Thursday 2022-04-21 09:41:09 by Pickle-Coding

No, we don't want radiation getting released in large pipenets fuck you fuckr uyu! (#65212)

* Make it harder to release radiation in large pipenets. Squares the volume / 2,500 thingy, and adds the requirements to the proto-nitrate bz response and proto-nitrate tritium response gas reactions to release radiation. This will make it significantly harder to release radiation in large pipenets, because releasing radiation in large pipenets makes it harder for people to identify the cause on why they are getting irradiated, which is bad and goes against the modern radiation goals.

Squaring is not enough for deranged people that know we don't want radiation released in large pipenets. Cubes the requirement instead. If someone could get enough gases reacting at once after this, then there is a bigger problem with atmos.

Who had fun seeing everything green, then getting irradiated and not even knowing why? I don't know, because I don't know who put the gases in waste and why we must suffer.

---
## [anupamroy777/kernel_realme_RM6785](https://github.com/anupamroy777/kernel_realme_RM6785)@[ee979c52cd...](https://github.com/anupamroy777/kernel_realme_RM6785/commit/ee979c52cd1fa92a51c9a2fbb5ce563c4d413123)
#### Thursday 2022-04-21 09:45:53 by Peter Zijlstra

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
Signed-off-by: Vaisakh Murali <mvaisakh@statixos.com>

---
## [Ed640/tgstation](https://github.com/Ed640/tgstation)@[55336d1e53...](https://github.com/Ed640/tgstation/commit/55336d1e5308789be1616413c8d8f87e073f7302)
#### Thursday 2022-04-21 09:46:35 by vincentiusvin

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
## [Eidenz/lama-cleaner](https://github.com/Eidenz/lama-cleaner)@[eea85b834e...](https://github.com/Eidenz/lama-cleaner/commit/eea85b834eee527f3a05fca9410e671c935603b2)
#### Thursday 2022-04-21 10:00:58 by blessedcoolant

Complete GUI Refactor

This patch brings in a massive number of changes to the frontend of the application. Please feel free to discuss the proposed changes with me at any time.

Implemented Recoil as a state management system.
Why Recoil? It is a robust library built by developers at Facebook for state management. It has an  extremely simple API for implementation that is in sync with React syntax compared to any other state management system out there and works amazingly well. While the official release status is beta as it becomes fully featured, the library is already used in various systems at Facebook and is very stable for the use cases of this application.

Why global state management? One of the major issues I saw with the current file structure is that there is minimal code splitting and it makes further development of the frontend a cumbersome task. I have broken down the frontend into various easy to access components isolating the GUI from the logic. To avoid prop drilling, we need global state management to handle the necessary tasks. This will also facilitate the addition of any new features greatly.

Code Splitting. Majority of the components that can be isolated in the application have now been done so.
All New Custom CSS & Removal of Tailwind
While Tailwind is a great way to deploy beautiful interfaces quickly, anyone trying to stylize the application further needs to be familiar with Tailwind which makes it harder for more people to work on it. Not to mention, I am not a particular fan of flooding JSX elements with inline CSS classes. That makes reading the code extremely hard and bloats up component code drastically.

As a replacement to Tailwind, I implemented a custom styling system using SCSS as a developer dependency.

In the new system, all the general and shared styles are in the styles folder and all the component styles are in the same folder as the component for easy access.The _index.scss file now acts as a central import for every other stylesheet that needs to be loaded.

What Changed?
The entire application looks and feels like the current implementation with minimal changes.
The green (#bdff01) highlight used in the application has now been changed to a bright yellow (rgb(255, 190, 0)) because I felt it better suited the new Dark Mode (see below).
The swipe bar for comparing before and after images has now been removed and instead the comparison is a smooth fade effect. I felt this was better to analyze image changes rather than a swiper. // Can add the swipe back if needed.

Dark Mode
A brand new Dark Mode has been added for the application. Users can enable and disable by tapping the button in the header or by using the Shift + D hotkey.

Other Misc New Features
When the editor image is now zoomed out to its default size, the image now also gets centered back.

TODO
The currently used react-zoom-pinch-pan module is not mobile friendly. It does not allow brush strokes. Need to figure out a way to fix this.
Further optimization of the frontend code with better code splitting and performance.
When using the LaMa model, the first stroke has a delayed response from the backend but the ones that follow are almost immediate. I believe this is happening because of the initialization of the model on the first stroke. I wonder if either of us can look at it and see if this can somehow be preloaded so the user experience is smooth from the first stroke.
Enable threading for the desktop application mode so flaskwebgui does not block the main applications Python console.

---
## [anoopsingam/rosx-edu](https://github.com/anoopsingam/rosx-edu)@[344d62c014...](https://github.com/anoopsingam/rosx-edu/commit/344d62c01470dcd01112b82df9b53831b15768f5)
#### Thursday 2022-04-21 10:51:50 by anoopsingam

made changes from male to boy and for female to girl

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[b71c77437c...](https://github.com/mrakgr/The-Spiral-Language/commit/b71c77437ce5cfb6f37ac1e729601790b18d4b3b)
#### Thursday 2022-04-21 11:18:03 by Marko Grdinić

"9:30am. Let me check email.

///

Marko, thank you for your detailed insight here. This looks really interesting, right in the area we are most focused on.

Let me know a good time to speak with you - you are in Croatia, correct? so probably your morning is best, unless you prefer working late into evening.

///

These guys are so suspicious. The MLIR plan I cam up with is interesting, but that a company would come to pay me to do something like this has about the same odds as winning the lottery. It is more likely that this is some kind setup for a scam. There is certainly a lot of weak circumstantial evidence that it is.

I've been stressed out trying to figure out these people's motivations. Why would somebody just come and give me money? Unless there is a clear reason, the most likely situation is that the other party is preying on my ego and setting up the conditions for future fraud.

I am going to go with my gut and close this thread here. I should focus on art. If I want to make money programming I should get a real job rather than expecting opportunities to fall into my lap. You can't expect anything good to just come to you on its own volition in this world. It is not like I am in need of money right now, so I can just leave this aside.

9:45am. Let me chill a bit first.

10am. https://www.youtube.com/playlist?list=PLxt9ZAGPLIpdn6CH2IbsNRYDlikLucxVe
Moi 3d

Let me just start. There isn't much more interesting than Moi 3d, and

Focus, close the Arknight OST playlist and start the Moi one. I need to build up knowledge of how to do various shapes in Moi. I am comparing my knowledge of it to Blender and am finding it strongly lacking.

https://youtu.be/E6AluXhn_2U?list=PLxt9ZAGPLIpdn6CH2IbsNRYDlikLucxVe
Detail Synergy (NURBS) | Design Principles

Let me go over them in order.

https://youtu.be/HIrHkhVx_PA?list=PLxt9ZAGPLIpdn6CH2IbsNRYDlikLucxVe
MoI3D - 3 - Four Step Workflow

Let me watch these basic vids in order.

https://youtu.be/HIrHkhVx_PA?list=PLxt9ZAGPLIpdn6CH2IbsNRYDlikLucxVe&t=124

Let me try making the bevel for the inner part of the desk piece using the arc. Right now I still don't know how I would do the % based bevel from Blender.

10:50am. No the idea I had was not good. I put in a indent using a boolean, but it was too alrge. I an not sure how to narrow it.. Hmmm actually, istead of aiming to subtract, what if I added instead? Nevermind this right now.

https://youtu.be/HIrHkhVx_PA?list=PLxt9ZAGPLIpdn6CH2IbsNRYDlikLucxVe&t=282

This is also one way to get what I want, though I'd need to make the circles eliptical.

https://youtu.be/HIrHkhVx_PA?list=PLxt9ZAGPLIpdn6CH2IbsNRYDlikLucxVe&t=422

Wait, could I just fillet and drag the corner points somehow. That would be the easiest way if it could work.

11:05am. I think I get it. For a regular cube, show points make them appear, but once I add a fillet the control points go away. So if I want those kinds of corners, I should first make a nurbs shape and extrude it. I made the mistake of cutting in with a cube.

Let me get back to the video.

https://youtu.be/HIrHkhVx_PA?list=PLxt9ZAGPLIpdn6CH2IbsNRYDlikLucxVe&t=425

Still I see the points being here. Why do the go away on the cube.

https://youtu.be/HIrHkhVx_PA?list=PLxt9ZAGPLIpdn6CH2IbsNRYDlikLucxVe&t=457

Ah it is because he is filleting the original curve and that just transforms it by adding an extra point.

Ah, in this situation I should not need to erase the entire object and start from scratch. Let me just delete the faces. But before that, let me draw the curves.

11:15am. I got the shape that I want, but something is wrong. The boolean is not working right.

11:40am. Had to take a short break, let me get back on track.

11:50am. Focus me, Moi 3d.

https://youtu.be/HIrHkhVx_PA?list=PLxt9ZAGPLIpdn6CH2IbsNRYDlikLucxVe&t=531
> Most situations you actually want to start with a 2d curve because you just have more options.

12:20pm. https://youtu.be/ZgGxU1__R3w?list=PLxt9ZAGPLIpdn6CH2IbsNRYDlikLucxVe
MoI3D - 4 - Basic Objects 1

Focus me. Let me watch this and then I'll take a break.

12:45pm. https://youtu.be/ZgGxU1__R3w?list=PLxt9ZAGPLIpdn6CH2IbsNRYDlikLucxVe&t=729

Unlike in Hops, insets aren't a part of booleans here. I see.

https://youtu.be/3gS5NY2_laM?list=PLxt9ZAGPLIpdn6CH2IbsNRYDlikLucxVe
MoI3D - 5 - Basic Objects 2

I am playing around on my own trying to replicate the desk piece. I know how to do the indent, but not the fillet around the rim. That cut in the middle is getting in the way. I have to do the curve with one less control point. Let me have breakfast here."

---
## [freebsd/freebsd-ports](https://github.com/freebsd/freebsd-ports)@[e250aeb4a1...](https://github.com/freebsd/freebsd-ports/commit/e250aeb4a1399664907d0df0605a3577ba671609)
#### Thursday 2022-04-21 11:30:21 by Tobias C. Berner

KDE: Update KDE Gear to 22.04

Thursday, 21 April 2022

Welcome to KDE Gear ⚙️ 22.04!

Skip to What’s New

KDE Gear ⚙️ 22.04 brings you all the updates added to a long list of KDE
apps over the last four months. KDE programs allow you to work, create
and play without having to submit yourself to extortionate licenses and
intrusive advertising, or surrender your privacy to unscrupulous
corporations.

Below you will discover a selection of the changes added in the last
four months to software designed to make your life better. But remember,
there is much, much more: games, social media apps, utilities for
communicating, developing and creating stuff… All these things have been
worked on to give you more stability and boost your productivity.

If you want to see a full list of everything we have done, check out the
complete changelog.

WARNING: There’s a lot!

All the details can be found here:
	https://kde.org/announcements/gear/22.04.0/

---
## [SerenityOS/serenity](https://github.com/SerenityOS/serenity)@[49b087f3cd...](https://github.com/SerenityOS/serenity/commit/49b087f3cd49261164bd4556cd6e9e0d95a3afc1)
#### Thursday 2022-04-21 11:55:05 by kleines Filmröllchen

LibAudio+Userland: Use new audio queue in client-server communication

Previously, we were sending Buffers to the server whenever we had new
audio data for it. This meant that for every audio enqueue action, we
needed to create a new shared memory anonymous buffer, send that
buffer's file descriptor over IPC (+recfd on the other side) and then
map the buffer into the audio server's memory to be able to play it.
This was fine for sending large chunks of audio data, like when playing
existing audio files. However, in the future we want to move to
real-time audio in some applications like Piano. This means that the
size of buffers that are sent need to be very small, as just the size of
a buffer itself is part of the audio latency. If we were to try
real-time audio with the existing system, we would run into problems
really quickly. Dealing with a continuous stream of new anonymous files
like the current audio system is rather expensive, as we need Kernel
help in multiple places. Additionally, every enqueue incurs an IPC call,
which are not optimized for >1000 calls/second (which would be needed
for real-time audio with buffer sizes of ~40 samples). So a fundamental
change in how we handle audio sending in userspace is necessary.

This commit moves the audio sending system onto a shared single producer
circular queue (SSPCQ) (introduced with one of the previous commits).
This queue is intended to live in shared memory and be accessed by
multiple processes at the same time. It was specifically written to
support the audio sending case, so e.g. it only supports a single
producer (the audio client). Now, audio sending follows these general
steps:
- The audio client connects to the audio server.
- The audio client creates a SSPCQ in shared memory.
- The audio client sends the SSPCQ's file descriptor to the audio server
  with the set_buffer() IPC call.
- The audio server receives the SSPCQ and maps it.
- The audio client signals start of playback with start_playback().
- At the same time:
  - The audio client writes its audio data into the shared-memory queue.
  - The audio server reads audio data from the shared-memory queue(s).
  Both sides have additional before-queue/after-queue buffers, depending
  on the exact application.
- Pausing playback is just an IPC call, nothing happens to the buffer
  except that the server stops reading from it until playback is
  resumed.
- Muting has nothing to do with whether audio data is read or not.
- When the connection closes, the queues are unmapped on both sides.

This should already improve audio playback performance in a bunch of
places.

Implementation & commit notes:
- Audio loaders don't create LegacyBuffers anymore. LegacyBuffer is kept
  for WavLoader, see previous commit message.
- Most intra-process audio data passing is done with FixedArray<Sample>
  or Vector<Sample>.
- Improvements to most audio-enqueuing applications. (If necessary I can
  try to extract some of the aplay improvements.)
- New APIs on LibAudio/ClientConnection which allows non-realtime
  applications to enqueue audio in big chunks like before.
- Removal of status APIs from the audio server connection for
  information that can be directly obtained from the shared queue.
- Split the pause playback API into two APIs with more intuitive names.

I know this is a large commit, and you can kinda tell from the commit
message. It's basically impossible to break this up without hacks, so
please forgive me. These are some of the best changes to the audio
subsystem and I hope that that makes up for this :yaktangle: commit.

:yakring:

---
## [hizuro/GarrisonRandomNPCs](https://github.com/hizuro/GarrisonRandomNPCs)@[2581edee92...](https://github.com/hizuro/GarrisonRandomNPCs/commit/2581edee92f3d184fca900eeffb76a7fa846f7a2)
#### Thursday 2022-04-21 12:51:19 by Hizuro

replace tab stops by shitty mass of spacers - damned silly YAML dictatorship.

---
## [martinking71/magnum-plugins](https://github.com/martinking71/magnum-plugins)@[e8ebb746ac...](https://github.com/martinking71/magnum-plugins/commit/e8ebb746ac159233d4101c604dd76462eb029f08)
#### Thursday 2022-04-21 13:46:29 by Vladimír Vondruš

modules: Glslang, you're the reason PEOPLE HATE BUILDSYSTEMS.

Confuckinggratulations, you managed to split the project into even more
tiny useless badly named libraries! Yes, it's amazing that such a
generic name like /usr/lib/libMachineIndependent.a is actually glslang,
who would have thought! All the developers who ever got their hands on
glslang and didn't cancel the whole project immediately upon seeing this
horror should get retroactively fired. FFS.

---
## [martinking71/magnum-plugins](https://github.com/martinking71/magnum-plugins)@[876fce50ce...](https://github.com/martinking71/magnum-plugins/commit/876fce50cef77bd0b462c9a59486b9d5efdacd0b)
#### Thursday 2022-04-21 13:46:29 by Vladimír Vondruš

SpirvToolsShaderConverter: drop WebGPU support.

It's removed since 2020.07, "funnily" enough our version detection
behaved in a way that reported the version as 2019.02 on 2020.07. Haha.
CAN THIS FUCKING PROJECT ADD A VERSION DEFINE FINALLY SO I CAN STOP
DOING SUCH BULLSHIT ALL THE TIME?!

---
## [mbs-octoml/mbs-tvm](https://github.com/mbs-octoml/mbs-tvm)@[d03f18799c...](https://github.com/mbs-octoml/mbs-tvm/commit/d03f18799c42fd9b56be64a728b652a471d2dcb1)
#### Thursday 2022-04-21 14:25:18 by Mark Shields

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
## [zeratulus/mindk-dev-camp](https://github.com/zeratulus/mindk-dev-camp)@[b57ce67847...](https://github.com/zeratulus/mindk-dev-camp/commit/b57ce678471590fda969074bc620beffda066353)
#### Thursday 2022-04-21 15:33:52 by Serhii Herenko

Sorry for not an atomic commit... 2 month of war... =[ ... this code written before this war against Ukraine and Ukrainian people... homework... refactoring... russian warship go fuck yourself!!! Im realy hate putin and most of russians... with this war and russian propaganda... PTN PNH... Homework xD

---
## [mewdori/mewdori](https://github.com/mewdori/mewdori)@[c6b963bb4b...](https://github.com/mewdori/mewdori/commit/c6b963bb4be177f3b57ce1b522650530a2859b56)
#### Thursday 2022-04-21 16:38:55 by mewt2wo

Update README.md

my gender identity is sigma male. my pronouns are work/hard. i stim by making money. im hyperfixated on the grind. my special interest is the hustle. my coping strategy is fucking bitches. i kin success. i don’t have rejection sensitive dysphoria, because rejection is a mindset.

---
## [ghostwriter/laminas-org-laminas-mvc-skeleton](https://github.com/ghostwriter/laminas-org-laminas-mvc-skeleton)@[5f25a26ba6...](https://github.com/ghostwriter/laminas-org-laminas-mvc-skeleton/commit/5f25a26ba64d6fc96e335cb7185e0847d6194c52)
#### Thursday 2022-04-21 16:52:59 by Michał Bundyra

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
## [TheHorizonRP/qb-core](https://github.com/TheHorizonRP/qb-core)@[9d83a952c2...](https://github.com/TheHorizonRP/qb-core/commit/9d83a952c29fdfd3fb3ca77a45329556a32368f5)
#### Thursday 2022-04-21 18:04:27 by uShifty

feat: Implement QBCore.Shared.VehicleHashs 

Describe Pull request
Indexs the vehicles jenkins joaat(Hash) value as the key of the table as the key so we dont have to do some shitty ass loop through the vehicles comparing joaat values. I have no clue why this secondary table was removed in the first place if I had to guess people were lazy but this should help the lazys by automatically filling the table.

Questions (please complete the following information):
Have you personally loaded this code into an updated qbcore project and checked all it's functionality? [yes/no] (Be honest) 
Yes

Does your code fit the style guidelines? [yes/no] 
Yes

Does your PR fit the contribution guidelines? [yes/no]
Yes

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[771715bc96...](https://github.com/mrakgr/The-Spiral-Language/commit/771715bc96dde3a1704ae19a8faa8ed4fcfe3ee6)
#### Thursday 2022-04-21 18:59:40 by Marko Grdinić

"2:40pm. Done with breakfast. Let me catch up with Blood Princess and then I will resume. So far, I've been learning a lot from these studies. Blender does not have much NURBS functionality, but Houdini does, I could transfer those techniques there.

3:20pm. Let me resume.

I am still wondering about it. The way I got contacted over Reddit and offered a sponsorship is quite something. Is tech recruiting evolving into some kind of monster beyond my imagination? This kind of targeted reachout was beyond my expectation. I certainly wasn't expecting to get contacted like this.

I need to be on guard against things like this in the future. Just forget this stuff. Master 3d art, start Heaven's Key, make money that way. I must not let anything unbalance me like this again. I haven't felt like this since the time with Z.

I'll forgive myself for being interested just this once, but only this once. I did the right thing to trigger the stop.

3:25pm. Just these few years I'll dedicate to art. I need to internalize that mindset. Spiral will get its chance at some point.

3:35pm. I have no idea, I am really having trouble filleting the rim for some reason.

https://youtu.be/3gS5NY2_laM?list=PLxt9ZAGPLIpdn6CH2IbsNRYDlikLucxVe&t=148
> One thing that you need to understand about Moi 3d is that it is very heavily optimized to be used with tablets

Really? I never occured to me to try this. I'll have to give it a shot.

https://youtu.be/3gS5NY2_laM?list=PLxt9ZAGPLIpdn6CH2IbsNRYDlikLucxVe&t=637

Fillets are giving him trouble it seems. Why doesn't it work for him?

4:20pm. I am going to have to ask how to fillet this thing as I have no idea.

Where do I ask? Let me just try /3/ first.

4:45pm. https://youtu.be/ARCRTKGcv8o?list=PLxt9ZAGPLIpdn6CH2IbsNRYDlikLucxVe
Safety Step #1 | MoI3D

I am not sure how focused I am on this as I watch it. Seriously fuck Spiral. I was making good progress in my art, but it feel like a ton of work just got dumped into my lap because of that offer.

5:15pm. I have no idea why this is failing for me. I am trying some different numbs curves revolved and substracted from the main cube, and I get the same issue of it not working.

5:25pm. There is something wrong about this. The way it connects around the edges leads to wiggles. I thought it might have been due to the inner curves, but a revolved nurbs circle does not have those and yet it still fails.

https://youtu.be/uPvCMpsYtxk
Fix Basic Fillet Issues in MoI

Let me watch this again.

5:35pm. I can't figure it out, let me just continue watching videos. I'll make it my cause to go through the entire playlist and absorb as much as I can. But if I really can't resolve it by then...

I should just ask on the Moi 3d forum. But it has a somewhat nasty interface.

5:45pm. I created an account, but it needs to be approved by a mod first.

For reason the internet is acting up.

5:50pm. Ah, right. I remembered something. When he did that revolve to get a sphere he used an arc instead of a circle.

6:35pm. What the hell it is working now for some reason.

6:50pm. I got it!

It is those sharp corners that are the problem. For the purpose of filleting, it is better to put a few points close together to get a smooth transition than to Ctrl + LMB to get the sharpies. And the reason why that perfect NURBs circle did not work for it is probably because I did not place it perfectly along the surface. It probably has two overlapping lines close together which is wrecking. I can't think of anything else as the reason why it is working all of sudden now so that must be it.

7pm. My mood is starting to improve. At least I figured out how to do that deak piece fillet. Good, good.

Let me go back to the videos.

7:35pm. Had to leave for lunch.

https://youtu.be/ARCRTKGcv8o?list=PLxt9ZAGPLIpdn6CH2IbsNRYDlikLucxVe&t=300

Let me finish this video and maybe I'll stop for the day.

https://youtu.be/ARCRTKGcv8o?list=PLxt9ZAGPLIpdn6CH2IbsNRYDlikLucxVe&t=700

He is really going the long way here. I'd just make them all in a row and rescale them. That would have been easier.

https://youtu.be/ARCRTKGcv8o?list=PLxt9ZAGPLIpdn6CH2IbsNRYDlikLucxVe&t=765

He really should have used mirror for those bottom cutouts as well.

Moi 3d really has such great UI design. But I am going to have to do my own hotkeys. The defaults are lacking.

https://youtu.be/BiaRcr8b_Hk?list=PLxt9ZAGPLIpdn6CH2IbsNRYDlikLucxVe
Safety Step #2 | MoI3D

I'll leave this for tomorrow.

What I want to do now before I close is check out Houdini's NURBS capabilities.

https://youtu.be/DhhQx59eD_4
Toothbrush - 02 Modeling the glass with NURBS

It has been a while since I looked at Houdini last. Let me have a look.

8:30pm. No it is just basic stuff. I don't think Houdini has something like Moi 3d's fillet.

Let me play with cutting up cubes in Moi. I want to see if I can get some uneven fillets like that.

Oh, I see, hiding an object just hides its style.

8:55pm. Let me close here. I am happy today went. I am finally starting to destress after all that burden was dumped on me. Yesterday I was so fatigued I went to bed before 9pm. I usually go past 12am.

I am going to go through the Moi playlist by Arrimus, go through the docs for Moi which are really good, and then get to work on that monitor. I really curious how subdiv mode works with Moi 3d."

---
## [sirostaib/atg-flutter](https://github.com/sirostaib/atg-flutter)@[46ed515d0d...](https://github.com/sirostaib/atg-flutter/commit/46ed515d0de20925912d5d656793e52617b96cb1)
#### Thursday 2022-04-21 19:39:45 by Caesar

First Commit

Good Morning, I have created the empty structure of the flutter application. looking forward to working on the UI design. thanks for reading this commit, in case I don't see you, good afternoon, good evening and good night.

---
## [zeamort/1620_Exam_2022](https://github.com/zeamort/1620_Exam_2022)@[eeadf076d5...](https://github.com/zeamort/1620_Exam_2022/commit/eeadf076d535ce843132af89e2db6e47af7c7453)
#### Thursday 2022-04-21 19:57:14 by morteza

tried to add some styling with a couple minutes left but not much progress. This has been a horrible experience wow. I have never bombed an exam like this before. Sorry to let you down.

---
## [LordVollkorn/ChemistryStation](https://github.com/LordVollkorn/ChemistryStation)@[351afe260b...](https://github.com/LordVollkorn/ChemistryStation/commit/351afe260b42764641a07385df5f7e24b840f631)
#### Thursday 2022-04-21 20:11:12 by san7890

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
## [Den-Xero/Journeyman_Game](https://github.com/Den-Xero/Journeyman_Game)@[bdd08a1eeb...](https://github.com/Den-Xero/Journeyman_Game/commit/bdd08a1eebc3353d9879a6aa2f0bfed345dd0e45)
#### Thursday 2022-04-21 20:18:25 by McConnell2111

Working Item spin and shows item just not remove yet and ai still triggers it

I want to die, this entire time i was missing 1 line 1 FKING LINE and that caused me so much pain. anyway ive watched taskmaster today series 8 pretty good, played some fortnite, league and a little r6 fun day over all. before i explode from this shitty game im going to do something else otherwise i might give myself a heart attack :)

---
## [BissetJ/winspy](https://github.com/BissetJ/winspy)@[78eb881253...](https://github.com/BissetJ/winspy/commit/78eb88125383da3c4a30793f0b39f3c083610315)
#### Thursday 2022-04-21 20:55:39 by BissetJ

Improve auto-update mode by avoiding redundant updates to some controls

Auto-update mode can be annoying because it keeps resetting
the content of the various controls even if nothing changed.
This i=makes a clunky experience if you are trying to interact
with one of those controls at the same time that the refresh
fires and updates it.  For example:

- You are trying to select the text from one of the labels
  (say, with the intent to copy it to the clipboard), the
  refresh will clear the text selection.

- You have a window with more than 8 styles set and you are
  trying to scroll the listbox down to see the bottom of the
  list.  The listbox scroll position will constantly be
  reset to the top.

 This change improves the situation for some of the controls:

 - All the simple labels/edit controls have been changed to skip
   the SetWindowText if the string is exactly the same as what
   is already in the control.  This is done via the new
   SetDlgItemTextEx helper.

 - The Styles tab explicitly tracks what values are being currently
   shown, and doesn't reset the lists unless the styles or the
   selected window have changed.

There are still some controls that this is a problem for, notably
the properties list and the lists on the Windows tab.  Those are
harder to solve, and problems for another day.

---
## [aarouns/CS3141-R01-team7](https://github.com/aarouns/CS3141-R01-team7)@[4c05de5166...](https://github.com/aarouns/CS3141-R01-team7/commit/4c05de51668a98817101dffbe2bb3ff857145537)
#### Thursday 2022-04-21 21:46:51 by Gabe Smit

Fixed Multiple-Unit Placement

The amount of units placed will be equal to the amount in "All Entities Prefab". Currently, units are selected by random from that array, so the number of times a unit is in the array directly correlates to their pick rate. I tried to implement a non-random instantiation option, but for some reason it causes Team2 to instantly die.
The health bar size of the archer is also too big, but I think that's because actual dimensions of the sprite image are smaller than the knight. I'm not sure if we can adjust the size per sprite, so you may need to find a different sprite or adjust its dimensions manually.
We might be good with just fixing what I mentioned, but if you really want to add more, I would prioritize basic user interaction / unit placement. However, we should probably try to focus on the project report instead.

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[dca0edc30e...](https://github.com/tgstation/tgstation/commit/dca0edc30e9db1424dffb582c5e8d075e0581ac0)
#### Thursday 2022-04-21 22:35:28 by B4CKU

Vim mecha changes (#66153)

This PR changes the following:

    fixes a bug with Vim overlays, making it always appear as if there was a pilot inside, even after leaving it
    adds a balloon alert when a mob fails to enter the mech due to its size
    adds a crafting recipe for Vim in the "robots" category
    allows using Vim as a circuit shell
    allows small mobs to use the mech as well

My reasoning behind the changes:

    fixing the overlay bug - bugfixes good, bugs bad
    balloon alert - it should help reduce confusion among players who can't figure why on earth they cannot enter the mech
    crafting recipe - I think a crafting recipe will make it a lot more accessible to players, especially because there is no way to learn about its existence in-game
    circuit shell - non-standard circuit shells can be pretty fun and people seemed to enjoy the ability to use circuits inside their piano synths or cameras, so I figured we could expand on this, while giving players more ways to interact with sentient pets
    maximum mob size increase - Vim has never really been built too often, most likely because even if people got their hands on a sentient pet, it wouldn't probably fit in the tiny mecha anyway. Currently pretty much only butterflies, rats and cockroaches can use Vim and they pretty much never become sentient.

---

