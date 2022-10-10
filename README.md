## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-10-09](docs/good-messages/2022/2022-10-09.md)


1,723,309 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,723,309 were push events containing 2,412,412 commit messages that amount to 153,212,633 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 34 messages:


## [Lamella-0587/Skyrat-tg](https://github.com/Lamella-0587/Skyrat-tg)@[967de5fb00...](https://github.com/Lamella-0587/Skyrat-tg/commit/967de5fb00613b8004ccfeea93a399799d99191e)
#### Sunday 2022-10-09 00:07:49 by SkyratBot

[MIRROR] Brains can now be healed with mannitol without being fully decayed among other quality of life tweaks [MDB IGNORE] (#16716)

* Brains can now be healed with mannitol without being fully decayed among other quality of life tweaks (#70357)

Removed the minimum amount of mannitol required to pour it since limiting this made barely any sense in the first place. Why oh why must we coders implement useless restrictions? (Useless restrictions caused the decay bug anyways.)

Brains no longer care about whether or not they're fully decayed when checking if they can be healed by pouring mannitol on them. They instead check if they're damaged at all and if they are, they'll let you pour mannitol on them.

The amount of time it takes to pour mannitol onto a brain is now 3 seconds instead of 6 seconds as it was way too slow. (Especially since something like a surgery step takes less time than 6 seconds.)

The solution is now only partially consumed as well, meaning if you need 20u of mannitol to fix a brain and you have a mixture of 40u of mannitol and 40u of mercury for example, pouring it will consume 40u of the mixture since you can't magically separate out the mannitol. This is rounded up, by the way. (Before this it simply consumed all of the mannitol, somehow you apparently can't stop pouring even while slowly pouring, according to the text.)

I've also very slightly increased the consistency of the pouring messages.

Fixes #70355

* Brains can now be healed with mannitol without being fully decayed among other quality of life tweaks

Co-authored-by: RikuTheKiller <88713943+RikuTheKiller@users.noreply.github.com>

---
## [ntietz/patzer](https://github.com/ntietz/patzer)@[9f0a25d69a...](https://github.com/ntietz/patzer/commit/9f0a25d69a165fbecd65f3c5e30f3149388b9132)
#### Sunday 2022-10-09 00:33:32 by Nicholas Tietz-Sokolsky

Refactor app state and implement player selection (human vs. computer), piece promotion, game status, and resigning/draws (#1)

There's a lot in this one, but I think that this gets everything into a
good spot to move forward with actual strategies for the computer.
Summary of the major changes:

- Break out state into `AppState` and focus on interacting through its
methods; it locks each sub-portion of state independently, so you don't
get blocked by another portion of state being locked if you're not using
it
- Implement one runner thread per player (if the player is a computer)
and clean them up when the game restarts or concludes
- Add ability to reset the game
- Add the ability to start the game, and lock out input when it's not
started yet
- Add the ability to select who is white or black (choices are human or
one of two computer "strategies")
- Add a menu pop-up for piece promotion so that that's possible
- Add buttons to resign or declare a draw
- Add display of the current game status so you know when it is started
and finished

This isn't the cleanest code, and there's a lot of work left to do. I'm
not hugely motivated to clean it up soon because I want to move onto the
engine side of this, and I also think I want to switch to
[fltk-rs](https://fltk-rs.github.io/fltk-rs/) since
[egui](https://github.com/emilk/egui) has been difficult in some
instances where I have to imitate retained mode, and I've had a **lot**
of trouble finding docs for what I am trying to do. I don't really have
a coherent thought here but I think the options going forward are:

- Stick with egui and work through it (this sounds rather painful but do
the other options not? :thinking: )
- Create a web application instead and use web technologies (I don't
really want to do this, although this might be a good chance to explore
web tech again in a non-work context and learn to enjoy it again)
- Switch to fltk-rs (this sounds like it could be better, but then
again, I might end up in the same pain pit)
- Abandoning the GUI is not an option :smile: 

Right now I lean toward eventually adopting fltk-rs, but I'm going to
take a break from GUI stuff after this lands for a while.

---
## [smoelius/rust-clippy](https://github.com/smoelius/rust-clippy)@[9e8f53d09a...](https://github.com/smoelius/rust-clippy/commit/9e8f53d09af61d38d6de42450dbf6910982d3ea9)
#### Sunday 2022-10-09 00:57:39 by bors

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
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[48b3cdb36d...](https://github.com/treckstar/yolo-octo-hipster/commit/48b3cdb36dae081e0de3f24406c9f6669dbc3a07)
#### Sunday 2022-10-09 01:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [RealN00B/frameworks_base](https://github.com/RealN00B/frameworks_base)@[85be6e82be...](https://github.com/RealN00B/frameworks_base/commit/85be6e82be650ce9b6ac461b55a67af8b4692ebf)
#### Sunday 2022-10-09 02:28:00 by Joey Huab

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

Signed-off-by: Hưng Phan <phandinhhungvp2001@gmail.com>

---
## [Relms12345/linux](https://github.com/Relms12345/linux)@[296f94d64a...](https://github.com/Relms12345/linux/commit/296f94d64aebe673142dd4ec5c063c7e08525648)
#### Sunday 2022-10-09 02:37:54 by Johannes Weiner

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
## [GoldenAlpharex/tgstation](https://github.com/GoldenAlpharex/tgstation)@[14c96d05b8...](https://github.com/GoldenAlpharex/tgstation/commit/14c96d05b82cd377dc3fe04944fdb4ece6176bd9)
#### Sunday 2022-10-09 02:38:22 by scriptis

TGUI for Techfabs II: The Great Recategorizing (AND ICONS) (AND MECHFABS) (AND AUTOLATHES) (#69990)

    I recategorized EVERY /datum/design/ IN THE GAME to be more UX friendly and I HATE MYSELF FOR IT
    I refactored techfab UI to WORK ANYWHERE for ANY MACHINE THAT USES /datum/design as a SET OF MODULAR COMPONENTS
    I moved a lot of DESIGNS EXCLUSIVE TO THE AUTOLATHE to also work IN PROTOLATHES
    I made MATERIAL ICONS animate between ICON STATES for STACKS
    I PUT ICONS IN ALL OF YOUR FABRICATORS
    I SOMEHOW DID ALL OF THIS WITHOUT LOSING ANY PERFORMANCE
    ALSO SUPPORTS COMPONENT PRINTERS AND MODULE DUPLICATORS

Other garbage:

    Fixed numerous spelling and consistency issues in designs
    Removed Machine Design (<x>) and Computer Design (<x>) from all relevant designs
    All designs are now in title case
    Numerous designs that were formerly autolathe exclusives can now also be printed at a protolathe (but not all); this is mostly just service equipment like drinking glasses and plates and silverware
    Circuits components can no longer be printed at a circuit imprinter (fixes 

    Integrated circuit components printed in the component printer/module printer cost twice as much than from an un upgraded circuit printer #67758)
    Designs that are not sensible for a department to have are no longer accessible to that department (read: medbay printing turbine parts)

Why It's Good For The Game

Improved UX for techfabs, but also for mechfabs and autolathes, and oh look it's pretty!

also I spent like eight hours doing nothing but categorizing /datum/designs and I'll cry if some version of this doesn't get merged eventually
Changelog

cl
refactor: mechfabs, autolathes, component printers, and module duplicators now use techfab tgui components
refactor: every single design is now categorized and subcategorized
refactor: mechfabs and autolathes are now in typescript
qol: techfabs now have icons for what you're about to print
qol: techfab material icons are now animated
qol: techfab material icons now fade when no materials are available
qol: techfab searching no longer lags like hell
qol: techfab searching now searches all recipes instead of just the current category
qol: techfabs now have subcategorization (stock part users rejoice)
qol: techfabs now announce when new recipes are available
qol: numerous other techfab ui tweaks
balance: some designs that were formerly autolathe exclusive can now be printed at some departmental techfabs

---
## [GoldenAlpharex/tgstation](https://github.com/GoldenAlpharex/tgstation)@[99b8d6b494...](https://github.com/GoldenAlpharex/tgstation/commit/99b8d6b4947b6a89d13fc22e469e77c313521e79)
#### Sunday 2022-10-09 02:38:22 by vincentiusvin

Changed Supermatter Internal Math + UI Additions (#69240)

Basically all what I'm doing is categorize and display whatever modifiers are currently applying to the SM. This way players can see powerloss, temperature generation, damage taking, temp limit adjustment etc all in live instead of diving code or looking it up in the wiki.

I have taken the liberty of making most of these modifiers additive instead of multiplicative since it's easier to illustrate how much a given modifier is doing when they are all additive. E.G: The gas you added gave you an extra 2500 joules instead of the gas you added gave you a 1.2x multiplier.

To make this job not CBT there are a few gameplay changes that are needed to make things fall into the framework and some general cleanup. Most noteworthy might be:

    Space damage taking (opted for 

SM damage and balance #66692 instead of SM can explode on space tiles again #35275 just because it's newer. Wont mind changing if asked). Also removed the power gen see the edit in
Changed Supermatter Internal Math + UI Additions #69240 (comment). Wont mind bringing it back and tweaking if asked.
SM will now use the same heat limit for everything that once used variations of it. Unified healing temp limit (influenced by psychologist) with damage heat limit (influenced by gases and low moles, yeah that's a thing). In practice this means your rock will heal at higher temps instead of the old one.
Heat output production. See:

    Changed Supermatter Internal Math + UI Additions #69240 (comment) and heat penalty from gases.
    I'm really sorry for tacking this on to this PR, but there's no good way to present the heat output effect of gases to the SM in a way I'm satisfied with if I don't do this. Kinda hard to atomize too since it relies on the cleanup. Rolled back!

Work left:

    Oh and need to make the NTOS things work.
    Ntos Done! Since the active crystal is now deprecated and we use localstate, the notification system got changed a bit. SM will now ping you if you subscribed to it. Only works when minimized and not closed, like the old one.
    Oh and also documentation.
    Think its in an ok spot now.
    Reimplement transmission view and low pressure power bonus. Yeah thats a thing.
    Looks like the low pressure power bonus is actually broken. It evaluates to ~2 for pretty much any x given. So im axing it.
    Reimplement moles doubling heat resistance. Yep thats also a thing.
    Readd the pluox and miasma pressure scaling thing.
    Done, also multiplied the reaction rate by half but multiplied the mole manipulation by 2 for pluox gen. Did this so it's easier to understand.
    Dump shit into the changelog.

Why It's Good For The Game

Future coders will now need to write a bit more code when they want to add another modifier. Meaning it's a tad more rigid if someone wants to go out of the existing framework. Also demands a little bit of math but nothing more than basic algebra.

But on the flipside, this means future coders that want to add a brand new modifier to the SM will need to justify and document it (with only a single string descriptor so its not even that much work). Makes the work of people maintaining the code waaay easier at the expense of feature coders. Also makes whatever change they want to apply be relayed immediately to the players.

I mean jesus christ we didnt even know PN was really good for SM until it's added to the wiki.
Changelog

🆑
del: Removed the broken pressure power multiplier which always evaluates to 2. Multiplied base SM power production by 2.
del: SM will no longer gain power when exposed to space. It actually used to do that, but only when the tile it's on has gas so you don't really notice it.
qol: added the factor breakdowns to the SM ui.
qol: added the gas effect breakdowns to the SM ui.
qol: Made the supermatter selection in NT CIMS ui frontend based. Notifications will be based on you pressing the bell button instead of opening a SM page.
code: Instead of showing the environment breakdown of the SM tile, the NT CIMS will show you the exact gas mixture that it uses for calculation.
code: Total moles in NT CIMS will now be substituted with absorbed moles, which is the thing we use to calculate scrung delams. Scrungs at 1800.
balance: Unified the SM taking damage on space (last modified 2018) with SM taking damage around space (added 2020, last modified 2022). Chose the latter formula, it's significantly stronger.
balance: SM will start healing at the same damage at which it stops taking heat damage. Instead of the old fixed healing at ~313K.
balance: made the low mole heat resistance thing on SM not scale with heat resistant gases.
balance: Made the supermatter temperature power gain multiplier thing linear at 1/6 instead of 50/273 or 30/273.
balance: Psychologist heat reduction is weaker on high heat gas.
refactor: rerouted how external damage (bullets) and external power (emitter) is applied to SM.
refactor: restructured the internal power calculations for SM. Power should be applied on each atmos tick instead of separately.
refactor: restructured how the SM calculates the damage that it takes. No changes expected except for the low mole temp limit multiplier thing.
refactor: Restructured SM pluox generation and miasma consumption. No changes expected though.
\🆑

---
## [intel/linux-intel-lts](https://github.com/intel/linux-intel-lts)@[adee8f3082...](https://github.com/intel/linux-intel-lts/commit/adee8f3082b01e5dab620d651e3ec75f57c0c855)
#### Sunday 2022-10-09 03:35:12 by Peter Zijlstra

x86/nospec: Unwreck the RSB stuffing

commit 4e3aa9238277597c6c7624f302d81a7b568b6f2d upstream.

Commit 2b1299322016 ("x86/speculation: Add RSB VM Exit protections")
made a right mess of the RSB stuffing, rewrite the whole thing to not
suck.

Thanks to Andrew for the enlightening comment about Post-Barrier RSB
things so we can make this code less magical.

Cc: stable@vger.kernel.org
Signed-off-by: Peter Zijlstra (Intel) <peterz@infradead.org>
Link: https://lkml.kernel.org/r/YvuNdDWoUZSBjYcm@worktop.programming.kicks-ass.net
[bwh: Backported to 5.10: adjust context]
Signed-off-by: Ben Hutchings <benh@debian.org>
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

---
## [SAnschutz/practice-git](https://github.com/SAnschutz/practice-git)@[3e75622506...](https://github.com/SAnschutz/practice-git/commit/3e756225060d96a2bd49ec3bd342b3624a8d725e)
#### Sunday 2022-10-09 06:24:18 by gacetta

There is unrest in the galaxy. Revolts. Looting. Riots. Revolution. Resistance. Real trouble in THE EMPIRE. STRIKES. BACK in the day, before he was Darth Vader, he was just a boy named Anakin.

---
## [ngoduyanh/nrs-impl-kt](https://github.com/ngoduyanh/nrs-impl-kt)@[2a969a0f02...](https://github.com/ngoduyanh/nrs-impl-kt/commit/2a969a0f020b8cb7ec589e935eafb0dae0516c8f)
#### Sunday 2022-10-09 08:35:47 by ngoduyanh

chore(impl): :clown_face: E&L gaming

"MC is the light in this shitty world full of dumbfucks doing politics, wrecking literally everything we've achieved in modern era, and not learning from pre-modern history. She is like the eye of the storm, always cute, happy and gentle despite this dystopia."

---
## [vinod1967/free-programming-books](https://github.com/vinod1967/free-programming-books)@[5fd70502a0...](https://github.com/vinod1967/free-programming-books/commit/5fd70502a063c46914fd444d2511c8233f81777f)
#### Sunday 2022-10-09 10:17:47 by Mathieu FONTAINE

Update free-programming-cheatsheets.md - React (#7095)

I suggested a React cheat sheet that I use very often. It is one of the most exhaustive and qualitative in my opinion.

---
## [PythonTryHard/agf-toolkit](https://github.com/PythonTryHard/agf-toolkit)@[f145f7a3c3...](https://github.com/PythonTryHard/agf-toolkit/commit/f145f7a3c39d21c3907080d100c671d944a91231)
#### Sunday 2022-10-09 10:29:16 by PythonTryHard

Replace `cv2.Mat` type hints. Fuck you PyCharm.

Somehow, when running this package under PyCharm, it always errors out,
complaining `AttributeError: 'cv2' does not have attribute 'Mat'`. I
sunk 2 days into it, it blocked development, it drove me crazy. No
amount of Googling could do. Worst part: `python -m agf_toolkit` runs
fine. I then thought it had something to do with `runpy` because of the
traceback: Nope. And the cherry on top was that it could not be
replicated on a fresh repo with only `opencv-python` and
`opencv-contrib-python`.Here's the full traceback for whoever the poor
soul reading this commit:

Traceback (most recent call last):
  File "~\AppData\Local\Programs\Python\Python310\lib\runpy.py", L196
    return _run_code(code, main_globals, None,
  File "~\AppData\Local\Programs\Python\Python310\lib\runpy.py", L86
    exec(code, run_globals)
  File "D:\dev\agf-toolkit\agf_toolkit\__main__.py", L7
    from agf_toolkit.processor import gears, image, text
  File "D:\dev\agf-toolkit\agf_toolkit\processor\image.py", L8
    from agf_toolkit.utils import color
  File "D:\dev\agf-toolkit\agf_toolkit\utils\color.py", L13
    def get_rgb(bgr_image: cv2.Mat, coord_x: int, coord_y: int)...
AttributeError: module 'cv2' has no attribute 'Mat'

Type hints extracted from GitHub @ microsoft/python-type-stubs.

---
## [Salex08/tgstation](https://github.com/Salex08/tgstation)@[a2577296e6...](https://github.com/Salex08/tgstation/commit/a2577296e62a0f3c335648169a335fe7d3de4bdc)
#### Sunday 2022-10-09 11:50:31 by RikuTheKiller

Upgrades the Modsuit Adapter Shell (#70286)

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

---
## [Salex08/tgstation](https://github.com/Salex08/tgstation)@[422accbe4e...](https://github.com/Salex08/tgstation/commit/422accbe4e9b53f075f9a76ba6293435cb3399da)
#### Sunday 2022-10-09 11:50:31 by John Willard

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
## [iandol/Psychtoolbox-3](https://github.com/iandol/Psychtoolbox-3)@[b85250b062...](https://github.com/iandol/Psychtoolbox-3/commit/b85250b062a7930681cdf7050f3e40457ff962b1)
#### Sunday 2022-10-09 13:02:38 by Mario Kleiner

PsychHID/OSX: Avoid calling PsychHIDWarnAccessDenied frequently.

The latest fix for the latest security bullshit, introduced sometime after macOS
10.15 Catalina. This was found when testing Octave on macOS 12.5 Monterey.

Apparently the call to IOHIDCheckAccess() by PsychHIDWarnAccessDenied()
is now extremely costly on macOS 12 (possibly also macOS 11 - untested) iff
the host application was launched from Terminal.app instead of standalone via
clicking a launch icon. This showed on Octave 6.4 after upgrade to macOS 12.5,
as octave is always launched from Terminal, regardless if in console mode or
GUI mode. Matlab appeared unaffected, as it is usually launched by clicking the
Matlab icon, but if one launches Matlab from a terminal, the same happens.

Why IOHIDCheckAccess() was suddenly turned into such an expensive operation
by the iDiots, i don't know, but our workaround is to no longer call it at each
invocation of KbCheck or KbQueueCreate, but only at PsychHID startup, and
hope this does not have other new bad effects.

Note access time exploded from way less than 1 msec to over 15 msecs! Great
work Apple!

Now we are back to identical performance on Matlab and Octave in both GUI
and commandline mode. Performance is bad compared to Linux or Windows,
but manageable at about 2.4 msecs on macOS 12.5 Monterey on a MBP 2017.
However, if run on a MacBook with touchbar, two PsychHID('KbCheck') calls
are needed for each KbCheck() call, because the touchbar is a separate HID
device, serving the important ESCape key and also function keys, so owners
of a shitty touchbar machine will have to live with execution times of KbCheck
on the order of 5 msecs on not that old hardware like the MBP 2017! This makes
animation loops with KbChecks difficult to run beyond 60-100 fps. Such is the
life of Apple customers...

When we are here, improve troubleshooting instructions for security bullshit
on macOS, and fix two compiler warnings new on macOS 12.

---
## [moulin-louis/minishell-42](https://github.com/moulin-louis/minishell-42)@[fe834b76ad...](https://github.com/moulin-louis/minishell-42/commit/fe834b76ad27fbc71594f07a8d676ad478ae0407)
#### Sunday 2022-10-09 13:37:04 by Bertrand SCHOEFFLER

working on export, sick fuck, added ut_strcmp (because we need it like hell) and other stuff

---
## [Kush1Push1/myrat](https://github.com/Kush1Push1/myrat)@[deb87e9ec0...](https://github.com/Kush1Push1/myrat/commit/deb87e9ec07fb6caff47cabaa8b5fdd760ea975b)
#### Sunday 2022-10-09 13:56:58 by SkyratBot

[MIRROR] Fixes gravity pulse and transparent floor plane sharing a layer [MDB IGNORE] (#16446)

* Fixes gravity pulse and transparent floor plane sharing a layer (#70124)

fixes gravity pulse and transparent floor plane sharing a layer

Broken by #69642 , sorry
I'll open up a seperate PR later today with a unit test to catch these cases
(my later today is in like 10 hours)

closes #70123 (weird fucking floors)

* Fixes gravity pulse and transparent floor plane sharing a layer

Co-authored-by: Time-Green <timkoster1@hotmail.com>

---
## [Blokyk/lotus](https://github.com/Blokyk/lotus)@[208830475f...](https://github.com/Blokyk/lotus/commit/208830475fa101c3b34b3dde8ac6892efa3a1292)
#### Sunday 2022-10-09 14:24:10 by blokyk

refactor: consolidate language properties into LotusFacts class

This removes the concept of "Grammar" and "ReadOnlyGrammar," which
had been getting feature creep while making more bloated. LotusFacts
is now responsible for handling everything that grammars did before
and more, except it is static, thus you don't have to pass it around
everywhere or make it into a singleton for no reason. It is supposed
to be a sort of queryable entity for language properties, whether it
is existing keywords, operator precedence, or valid access levels.

Let's face it, parsex was never gonna magically turn into an actual
parsing library, and it's been *years* since that idea has been
abandonned. While the fact that ReadOnlyGrammar survived so long is
nothing short of a miracle, it's time to get rid of it and its
omnipresence in the code base. This is not an "alternative to parser
combinators" anymore, this is a compiler for lotus, so it should
behave and be written like one. Please bear with me while i'm making all
those changes. It's taking some time but it feels good to finally
do a good ol' full-blocking Gen2 Collection in here.

There's still a few concepts that are so fundamental to the codebase
right now thata they are hard to factor out, tho. One of those are
"parslets." This is already far from an atomic commit, so I wasn't
planning on removing them in *this* commit, but I did experiment
around a bit, and I do have to say that parslets are pretty practical
with the current "architecture" of my code. Hell, removing them might
make LotusFacts mostly useless for parsing. Only the future will tell
I guess. See you then :)

---
## [vlad-avr/AC_Lab1](https://github.com/vlad-avr/AC_Lab1)@[e463d66759...](https://github.com/vlad-avr/AC_Lab1/commit/e463d66759d7510ced2ddac24bd18097b092cb4a)
#### Sunday 2022-10-09 15:15:31 by vlad-avr

BUGFIX: holy shit I don't know what the fuck is this bug about, but i fixed the shit out of it
+ reverted some of the lost tests in process of bugfix (strassen testing)

---
## [ghen-git/Thirst-Mod](https://github.com/ghen-git/Thirst-Mod)@[3aeec465c2...](https://github.com/ghen-git/Thirst-Mod/commit/3aeec465c2c426234e743a15c59671891ef9aba7)
#### Sunday 2022-10-09 15:54:07 by ghen-git

starting create compat and FUCK YOU BUG PHYSICS BUG

---
## [Jacquerel/orbstation](https://github.com/Jacquerel/orbstation)@[23bfdec8f4...](https://github.com/Jacquerel/orbstation/commit/23bfdec8f43046f7b54906509e38ed1ad91f5096)
#### Sunday 2022-10-09 15:56:09 by LemonInTheDark

Multiz Rework: Human Suffering Edition (Contains PLANE CUBE) (#69115)


About The Pull Request

I've reworked multiz. This was done because our current implementation of multiz flattens planes down into just the openspace plane. This breaks any effects we attach to plane masters (including lighting), but it also totally kills the SIDE_MAP map format, which we NEED for wallening (A major 3/4ths resprite of all wall and wall adjacent things, making them more then one tile high. Without sidemap we would be unable to display things both in from of and behind objects on map. Stupid.)

This required MASSIVE changes. Both to all uses of the plane var for reasons I'll discuss later, and to a ton of different systems that interact with rendering.

I'll do my best to keep this compact, but there's only so much I can do. Sorry brother.
Core idea

OK: first thing.
vis_contents as it works now squishes the planes of everything inside it down into the plane of the vis_loc.
This is bad. But how to do better?

It's trivially easy to make copies of our existing plane masters but offset, and relay them to the bottom of the plane above. Not a problem. The issue is how to get the actual atoms on the map to "land" on them properly.

We could use FLOAT_PLANE to offset planes based off how they're being seen, in theory this would allow us to create lens for how objects are viewed.
But that's not a stable thing to do, because properly "landing" a plane on a desired plane master would require taking into account every bit of how it's being seen, would inherently break this effect.

Ok so we need to manually edit planes based off "z layer" (IE: what layer of a z stack are you on).

That's the key conceit of this pr. Implementing the plane cube, and ensuring planes are always offset properly.
Everything else is just gravy.
About the Plane Cube

Each plane master (except ones that opt out) is copied down by some constant value equal to the max absolute change between the first and the last plane.
We do this based off the max z stack size detected by SSmapping. This is also where updates come from, and where all our updating logic will live.

As mentioned, plane masters can choose to opt out of being mirrored down. In this case, anything that interacts with them assuming that they'll be offset will instead just get back the valid plane value. This works for render targets too, since I had to work them into the system as well.

Plane masters can also be temporarily hidden from the client's screen. This is done as an attempt at optimization, and applies to anything used in niche cases, or planes only used if there's a z layer below you.
About Plane Master Groups

BYOND supports having different "maps" on screen at once (IE: groups of items/turfs/etc)
Plane masters cannot cover 2 maps at once, since their location is determined by their screen_loc.
So we need to maintain a mirror of each plane for every map we have open.

This was quite messy, so I've refactored it (and maps too) to be a bit more modular.

Rather then storing a list of plane masters, we store a list of plane master group datums.
Each datum is in charge of the plane masters for its particular map, both creating them, and managing them.

Like I mentioned, I also refactored map views. Adding a new mapview is now as simple as newing a /atom/movable/screen/map_view, calling generate_view with the appropriate map id, setting things you want to display in its vis_contents, and then calling display_to on it, passing in the mob to show ourselves to.

Much better then the hardcoded pattern we used to use. So much duplicated code man.

Oh and plane master controllers, that system we have that allows for applying filters to sets of plane masters? I've made it use lookups on plane master groups now, rather then hanging references to all impacted planes. This makes logic easier, and prevents the need to manage references and update the controllers.

image

In addition, I've added a debug ui for plane masters.
It allows you to view all of your own plane masters and short descriptions of what they do, alongside tools for editing them and their relays.

It ALSO supports editing someone elses plane masters, AND it supports (in a very fragile and incomplete manner) viewing literally through someone else's eyes, including their plane masters. This is very useful, because it means you can debug "hey my X is yorked" issues yourself, on live.

In order to accomplish this I have needed to add setters for an ungodly amount of visual impacting vars. Sight flags, eye, see_invis, see_in_dark, etc.

It also comes with an info dump about the ui, and plane masters/relays in general.

Sort of on that note. I've documented everything I know that's niche/useful about our visual effects and rendering system. My hope is this will serve to bring people up to speed on what can be done more quickly, alongside making my sin here less horrible.
See https://github.com/LemonInTheDark/tgstation/blob/multiz-hell/.github/guides/VISUALS.md.
"Landing" planes

Ok so I've explained the backend, but how do we actually land planes properly?
Most of the time this is really simple. When a plane var is set, we need to provide some spokesperson for the appearance's z level. We can use this to derive their z layer, and thus what offset to use.

This is just a lot of gruntwork, but it's occasionally more complex.
Sometimes we need to cache a list of z layer -> effect, and then use that.
Also a LOT of updating on z move. So much z move shit.

Oh. and in order to make byond darkness work properly, I needed to add SEE_BLACKNESS to all sight flags.
This draws darkness to plane 0, which means I'm able to relay it around and draw it on different z layers as is possible. fun darkness ripple effects incoming someday

I also need to update mob overlays on move.
I do this by realiizing their appearances, mutating their plane, and then readding the overlay in the correct order.

The cost of this is currently 3N. I'm convinced this could be improved, but I've not got to it yet.
It can also occasionally cause overlays to corrupt. This is fixed by laying a protective ward of overlays.Copy in the sand, but that spell makes the compiler confused, so I'll have to bully lummy about fixing it at some point.
Behavior changes

We've had to give up on the already broken gateway "see through" effect. Won't work without managing gateway plane masters or something stupid. Not worth it.
So instead we display the other side as a ui element. It's worse, but not that bad.

Because vis_contents no longer flattens planes (most of the time), some uses of it now have interesting behavior.
The main thing that comes to mind is alert popups that display mobs. They can impact the lighting plane.
I don't really care, but it should be fixable, I think, given elbow grease.

Ah and I've cleaned up layers and plane defines to make them a bit easier to read/reason about, at least I think.
Why It's Good For The Game
<visual candy>

Fixes #65800
Fixes #68461
Changelog

cl
refactor: Refactored... well a lot really. Map views, anything to do with planes, multiz, a shit ton of rendering stuff. Basically if you see anything off visually report it
admin: VV a mob, and hit View/Edit Planes in the dropdown to steal their view, and modify it as you like. You can do the same to yourself using the Edit/Debug Planes verb
/cl

---
## [Jacquerel/orbstation](https://github.com/Jacquerel/orbstation)@[1810b85553...](https://github.com/Jacquerel/orbstation/commit/1810b855536f05891593b1379e455164f45fab3a)
#### Sunday 2022-10-09 15:56:09 by tralezab

Heretics cannot be converted, and are immune to cult stun hands. Instead, the cult is rewarded for sacrificing them with the bloody bastard sword, an oversized SPIN2WIN funblade. + Soul Stealing Fantasy Affix (#69725)

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

---
## [rd-stuffs/msm-4.14](https://github.com/rd-stuffs/msm-4.14)@[0f51016186...](https://github.com/rd-stuffs/msm-4.14/commit/0f51016186e3a718390a5f45fb78825f99b90fda)
#### Sunday 2022-10-09 17:00:00 by Wang Han

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
Signed-off-by: Richard Raya <rdxzv.dev@gmail.com>

---
## [JaxJaxW/JaxJaxW.github.io](https://github.com/JaxJaxW/JaxJaxW.github.io)@[1f00f8dbec...](https://github.com/JaxJaxW/JaxJaxW.github.io/commit/1f00f8dbec2acaa832ac92d19a425162b1d10f9c)
#### Sunday 2022-10-09 17:55:35 by Jaxton Willman

IT'S BLUE!

Changed accent color to profile pic shirt color

Upped my H3 font size and font weight to make them a little more readable

Removed background of resume icon

Added comments in CSS to better separate things and improve readability

Removed main website alert

Added content to UF experience

Removed content from Kyoto experience

Changed research experience to all fall under Saxena Lab

Moved Thermal Lab TA and Peer Advisor experiences to the top of the the engineering experiences list

TODO: Replicate these changes in my resume

Moved projects alert to top of section to explain about project pages and captions

Changed resume download to look more like a button to stand out better

Cleaned up miscellaneous spacing here and there

Changed cwebp.bat tool to not have the duplicated folder structure

TODO: Fix on my desktop folder too

Removed all quotes except Bill Bryson quote

Moved Bill Bryson quote to contact section so it's out of the way a bit

TODO: Fix linkedin profile icon
TODO: Add background to profile icons
TODO: Make icons larger and more readable

Thank you to my parents for continually reviewing the content on my website for me and giving me feedback.

---
## [newstools/2022-iol-the-star](https://github.com/newstools/2022-iol-the-star)@[fea613dd90...](https://github.com/newstools/2022-iol-the-star/commit/fea613dd90f38fa4c7dc6e61e5ba76803cfca315)
#### Sunday 2022-10-09 19:05:50 by Billy Einkamerer

Created Text For URL [www.iol.co.za/the-star/the-star/news/caring-music-artist-tyraqeed-uses-his-platform-to-speak-about-life-challenges-love-and-personal-experiences-c42716cb-badb-4d1b-9439-2d115f550132]

---
## [Mafyia313/winer](https://github.com/Mafyia313/winer)@[e345faaaf6...](https://github.com/Mafyia313/winer/commit/e345faaaf62a38feb366de78efbeaa863922e695)
#### Sunday 2022-10-09 19:32:28 by Mr Naib 313

Create README.md

pkg update && pkg upgrade
pkg install python 
pkg install git 
git clone https://github.com/Mafyia313/winer.git
cd winer
python crazy.py
I don't Care 
I Fuck All Non-Muslim
You Like me Contact with me 
You hat me I hate you
You love me I love you 
Good Bye

---
## [GeoB99/reactos](https://github.com/GeoB99/reactos)@[4e43629d99...](https://github.com/GeoB99/reactos/commit/4e43629d99a8a33803f2d4e12ff4ebfedcb30966)
#### Sunday 2022-10-09 19:33:51 by George Bișoc

[NTOS:CM] Implement registry checks & recovery

Instead of having the CmCheckRegistry implementation in the kernel, it's better to have it in the Configuration Manager library instead (aka CMLIB). The benefits of having it in the library are the following:

- CmCheckRegistry can be used in FreeLdr to fix the SYSTEM hive
- It can be used on-demand in the kernel
- It can be used for offline registry repair tools
- It makes the underlying CmCheckRegistry implementation code debug-able in user mode

[SDK][CMLIB] Declare HBOOT_TYPE_REGULAR and HBOOT_TYPE_SELF_HEAL boot types

=== DOCUMENTATION REMARKS ===

HBOOT_TYPE_REGULAR and HBOOT_TYPE_SELF_HEAL are boot type values set up by the CMLIB library. HBOOT_TYPE_REGULAR indicates a normal system boot whereas HBOOT_TYPE_SELF_HEAL indicates the system boot is assisted within self healing mode.

Whether the former or the latter value is set it's governed by both the kernel and the bootloader. The bootloader and the kernel negotiate together to determine if any of the registry properties (the hive, the base block, the registry base, etc) are so severed from corruption or not. In extreme cases where
registry healing is possible, the specific base block of the damaged hive will have its flags marked with HBOOT_TYPE_SELF_HEAL. At this point the boot phase procedure is orchestrated since the boot phase no longer goes on the default path but it's assisted, as I have already said above.

[SDK][CMLIB] Implement two names & Unicode names comparison functions

CmpCompareBothCompressedNames and CmpCompareDistinctNames are necessary for lexicographical order validation code when validating the key in question.

[SDK][CMLIB] Implement self-heal registry helpers

This implements cmheal.c file which provides the basic registry self-heal infrastructure needed by the public CmCheckRegistry function. The infrastructure provides a range of various self-heal helpers for the hive, such as subkey, class, values and node healing functions.

[SDK][CMLIB] Implement CmCheckRegistry and validation private helpers

CmCheckRegistry is a function that provides the necessary validation checks for a registry hive. This function usually comes into action when logs have been replayed for example, or when a registry hive internals have changed such as when saving a key, loading a key, etc.

This commit implements the whole Check Registry infrastructure (cmcheck.c) in CMLIB library for ease of usage and wide accessibility across parts of the OS. In addition, two more functions for registry checks are also implemented -- HvValidateHive and HvValidateBin.

CORE-9195
CORE-6762

[NTOS:CM] Use the appropriate flags on functions that will call CmCheckRegistry & add missing CmCheckRegistry calls

In addition to that, in some functions like CmFlushKey, CmSaveKey and CmSaveMergedKeys we must validate the underlying hives as a matter of precaution that everything is alright and we don't fuck all the shit up.

[NTOS:CM] Don't lazy flush the registry during unlocking operation

Whenever ReactOS finishes its operations onto the registry and unlocks it, a lazy flush is invoked to do an eventual flushing of the registry to the backing storage of the system. Except that... lazy flushing never comes into place.

This is because whenever CmpLazyFlush is called that sets up a timer which needs to expire in order to trigger the lazy flusher engine worker. However, registry locking/unlocking is a frequent occurrence, mainly when on desktop. Therefore as a matter of fact, CmpLazyFlush keeps removing and inserting the timer and the lazy flusher will never kick in that way.

Ironically the lazy flusher actually does the flushing when on USETUP installation phase because during text-mode setup installation in ReactOS the frequency of registry operations is actually less so the timer has the opportunity to expire and fire up the flusher.

In addition to that, we must queue a lazy flush when marking cells as dirty because such dirty data has to be flushed down to the media storage of the system. Of course, the real place where lazy flushing operation is done should be in a subset helper like HvMarkDirty that marks parts of a hive as dirty but since we do not have that, we'll be lazy flushing the registry during cells dirty marking instead for now.

CORE-18303

[NTOS:CM][CMLIB] Use HBOOT_TYPE_REGULAR / HBOOT_TYPE_SELF_HEAL indicators for boot type instead of hardcoded values

[NTOS:CM] Disable hard errors when setting up a new size for a hive file / annotate CmpFileSetSize parameters with SAL

During a I/O failure of whatever kind the upper-level driver, namely a FSD, can raise a hard error and a deadlock can occur. We wouldn't want that to happen for particular files like hives or logs so in such cases we must disable hard errors before toying with hives until we're done.

In addition to that, annotate the CmpFileSetSize function's parameters with SAL.

[NTOS:CM] Ignore syncing/flushing requests after registry shutdown

When shutting down the registry of the system we don't want that the registry in question gets poked again, such as flushing the hives or syncing the hives and respective logs for example. The reasoning behind this is very simple, during a complete shutdown the system does final check-ups and stuff until the computer
shuts down.

Any writing operations done to the registry can lead to erratic behaviors. CmShutdownSystem call already invokes a final flushing of all the hives on the backing storage which is more than enough to ensure consistency of the last session configuration. So after that final flushing, mark HvShutdownComplete as TRUE indicating
that any eventual flushing or syncying (in the case where HvSyncHive gets called) request is outright ignored.

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[db83f6498d...](https://github.com/tgstation/tgstation/commit/db83f6498da37ecd25588ea3f7024409d2f3f117)
#### Sunday 2022-10-09 21:13:05 by vincentiusvin

Simplifies SM damage calculation, tweaks the numbers. (#70347)


About The Pull Request

We apply the damage hardcap individually now, split off the old flat 1.8 into individual caps for heat, moles, and power.

Set it to 1.5 for heat, 1 for mole and 1 for power. This means for most delams it'll be a tad slower! But its possible to make SM delam nearly twice as fast if you combine all 3. (3.5). Be pretty hard tho.

Set the heat healing to -1 so you can counteract one factor at most (except heat since you'll never get both heat healing and heat damage at the same time anyway).

I'm not hell bent on any of the numbers, just picked round even ones and ones that i think will make sense. If you want them changed lmk.

Got rid of the cascade mole and power multipliers since there's probably like three people that are aware that it even exists. Ideally we just add another entry to the CIMS but its already pretty crowded. Figured nobody is gonna miss it anyway? Sorry ghil.

Got rid of the moles multiplier thing since its nicer to keep the temp damage fully based on temp damage instead of adding another multiplier. I just applied the .25 to the damage flatly, meaning it slows down delams again!

And some space exposure stuff: #70347 (comment)
Why It's Good For The Game

Hardcap: Discrete, less randomly interconnected factors are easier to present and remember. The calculation procs are also made to be additive so we had to hack a bit and do some rescaling to accomodate the old behavior in my original PR #69240. Can remove the hack if this pr goes through.

Cascade and mole multiplier: The rest are just getting rid of underutilized factors so we have a cleaner behavior to maintain, present, and understand. (In a perfect world modifiers that aren't visible to the players shouldn't have been merged in the first place smh smh)
Changelog

🆑
fix: Fixed sm space exposure damage going through walls
del: got rid of the molar multiplier for sm heating damage. It will now only impact molar damage and temp limit. We apply the lowest value directly so this slows down sm delams a tiny bit.
del: got rid of cascades making sm delam at 450 moles and 1250 mev. It delams normally now.
balance: Applied the sm damage hardcap of 1.8 individually to heat (1.5), moles (1), power (1). Meaning most sm delams are slower now, but the really bad ones can be faster.
balance: Halved sm temp healing across the board. Temp limits are still the same though so you shouldn't notice it that much.
balance: Halved SM power damage across the board.
balance: Changed sm space exposure damage to just check for the current tile and adjacent atmos connected tiles.
/🆑

---
## [RTI-BDI/JavaFF](https://github.com/RTI-BDI/JavaFF)@[60c9720b39...](https://github.com/RTI-BDI/JavaFF/commit/60c9720b39e890399b101e41194e0ae52dacaf72)
#### Sunday 2022-10-09 21:16:52 by Devis Dal Moro

One of the best commits of my life...

-Inserted maxpplan size in search round to limit dimension of plan to use along with search interval if desired (otherwise set really really high)
- Fixed remove from open broken due to error in rebase. Thanks to my buddy post phd Marcolino da Rovereto Robol who was just came back from his trip to Greece and, in a couple of hours, he had an amazing intuition: I was modifying the nodes in the open list which was an ordered treeset and then the open.remove(state) was not able to find them anymore at the same place in which they were inserted... 
- Devis god mode fix in equals and hashcode for TemporalMetricState which were not taking into account non domain defined in search as they should be (considering just predicates of initiated and non terminated actions, NOT considering predicates of terminated actions)

---
## [ItsLJcool/Funkin-At-Freddys-YCEPORT](https://github.com/ItsLJcool/Funkin-At-Freddys-YCEPORT)@[a3019d8dc0...](https://github.com/ItsLJcool/Funkin-At-Freddys-YCEPORT/commit/a3019d8dc0c0901a7d946337365ba92518fa2b80)
#### Sunday 2022-10-09 22:12:56 by Landon Shields

Finished Fazbars & fuck your FlxTypedGroup :troll:

---
## [ckgresla/MI6](https://github.com/ckgresla/MI6)@[d972d3c3bb...](https://github.com/ckgresla/MI6/commit/d972d3c3bba356c3447cd8387410b471c66395e9)
#### Sunday 2022-10-09 22:24:51 by ckgresla

FINALLY GOT THE FUCKING GAE IMPLEMENTED, math was correct but like an idiot was asking for torch.backwards(() instead of torch.backward() -- thank you whatever god may be

---
## [Emidowojo/branding](https://github.com/Emidowojo/branding)@[b7ea693f0d...](https://github.com/Emidowojo/branding/commit/b7ea693f0d566fc9bcd04fdf86c3b4959eaf191a)
#### Sunday 2022-10-09 23:19:02 by Emidowojo

OLS Logos

I created four different Open Life Science Logos in SVG and PNG files for the Social media Preview. Please look through and let me know which suits your taste or if you'd like more improvements

---
## [TwinUsers/solanum](https://github.com/TwinUsers/solanum)@[06c5309534...](https://github.com/TwinUsers/solanum/commit/06c53095343c2756208f6398bb7e00fb2cbe46dd)
#### Sunday 2022-10-09 23:38:21 by Ed Kellett

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

