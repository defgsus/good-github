## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-02-26](docs/good-messages/2022/2022-02-26.md)


1,115,144 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,115,144 were push events containing 1,610,422 commit messages that amount to 99,819,727 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 23 messages:


## [Jibber-Inc/Jibber-iOS](https://github.com/Jibber-Inc/Jibber-iOS)@[a3bdeb08e9...](https://github.com/Jibber-Inc/Jibber-iOS/commit/a3bdeb08e9325cd03e559374108e3ae02ea943a7)
#### Saturday 2022-02-26 01:39:41 by Benji

this stupid piece of shit isn't showing why the fuck not.

---
## [bellomia/MOTTlab](https://github.com/bellomia/MOTTlab)@[81bd520ed8...](https://github.com/bellomia/MOTTlab/commit/81bd520ed8f0b59f529ce68678c8889d29834cc3)
#### Saturday 2022-02-26 03:12:19 by Gabriele Bellomia

IMPORTANT FIX: U/D scaling in *calculations*

The generic equation for the Weiss field is:

g0(z) = ( z + mu - hybr )^-1
      = ( z + mu - t^2 ∑[G(k,z)] )^-1

In our case we have

> mu=0 (half-filling + ph-sym)
> ∑[G(k,z)] = Gloc(z), where Gloc(z) is computed by phys.gloc(z,D,dos)

For the Bethe lattice t = D/2, so that the *HARDCODED MAGIC NUMBER* 🙈 t^2 = 0.25 was somewhat appropriate†, but for sure for a generic lattice this won't work. Indeed we found very strange behavior varying D on the square and cubic lattices, namely different A(w) shapes for a fixed U,D pair, different Uc/D for different D values and all this kind of crazy stuff.

So we fix this by

- defining a proper hybr(D,DOS,GLOC) function, which just fills in the correct t(D) relationship for all the lattices
  > ugly, but for now I don't know how to improve it... maybe after all we really need a +lattice module, I'll think about it.
- building the Weiss field as g0 = ( z - hybr(...))^-1

Preliminary testing has confirmed that

- Uc/D is now fixed 🥲
- Z vs U/D plots are now independent on D 😮‍💨
- Same for spectral plots and gifs (except the bandwidth, of course) 🙃

---------

†Actually, even for the Bethe lattice, changing D would break something, since (D/2) would still differ from 1/4. We should go fix this in the main to, in order to have a proper 'Bethe-only' release.

---
## [Sharad2001/Data-structures-and-algorithms](https://github.com/Sharad2001/Data-structures-and-algorithms)@[5b6bc5741f...](https://github.com/Sharad2001/Data-structures-and-algorithms/commit/5b6bc5741f890a56b26fb8d45f5117f5447a0d52)
#### Saturday 2022-02-26 03:20:21 by Sharad2001

Escape the forbidden forests.

Penelope and her classmates are lost in the Forbidden Forest and the Devil is out to get them. But Penelope has magical powers that can build bridges across the dangerous river and take her friends to safety. The only bridges that can withstand the Devil's wrath are the ones built between two similar trees in the forest. 
Given str1 and str2 denoting the order of trees on either side of the river, find the maximum number of bridges that Penelope can build and save everyone from the Devil. 
Note: Each tree in the forest belongs to one of the 3 categories represented by * or # or @

---
## [repinger/exynos9611_m21_kernel](https://github.com/repinger/exynos9611_m21_kernel)@[d6e9191879...](https://github.com/repinger/exynos9611_m21_kernel/commit/d6e919187977a08d7b39e09f160d3f691b30d80b)
#### Saturday 2022-02-26 04:36:39 by Masahiro Yamada

modpost: file2alias: go back to simple devtable lookup

commit ec91e78d378cc5d4b43805a1227d8e04e5dfa17d upstream.

Commit e49ce14150c6 ("modpost: use linker section to generate table.")
was not so cool as we had expected first; it ended up with ugly section
hacks when commit dd2a3acaecd7 ("mod/file2alias: make modpost compile
on darwin again") came in.

Given a certain degree of unknowledge about the link stage of host
programs, I really want to see simple, stupid table lookup so that
this works in the same way regardless of the underlying executable
format.

Signed-off-by: Masahiro Yamada <yamada.masahiro@socionext.com>
Acked-by: Mathieu Malaterre <malat@debian.org>
[nc: Omit rpmsg, sdw, tbsvc, and typec as they do not exist here]
Signed-off-by: Nathan Chancellor <natechancellor@gmail.com>
Signed-off-by: Sasha Levin <sashal@kernel.org>

---
## [frank113/pokemon-showdown-client](https://github.com/frank113/pokemon-showdown-client)@[be9a95cbc6...](https://github.com/frank113/pokemon-showdown-client/commit/be9a95cbc683c04c6ead95d5643c7ea551607a56)
#### Saturday 2022-02-26 04:37:45 by Guangcong Luo

Fix bugs caused by Preact update

The new Preact version seems to have broken a lot of low-level
magic we used. We plausibly shouldn't be using such low-level magic
in the first place, but that's a conversation for another day.

In particular:

1. `preact.render` seems to replace all of `containerNode`'s contents
   if `replaceNode` isn't passed (previously, it would append a child).
   This is an insane thing to change without any documentation... Maybe
   I'm misunderstanding it?

2. Making a button value an uncontrolled form was a pretty big hack
   in the first place, but at least it worked. Now that it doesn't,
   we're giving up and switching to controlled forms, which makes the
   code a lot nicer, fixes a bug, and I should probably have just done
   in the first place.

---
## [roapsyme/kernel_xiaomi_vayu](https://github.com/roapsyme/kernel_xiaomi_vayu)@[638a4bec15...](https://github.com/roapsyme/kernel_xiaomi_vayu/commit/638a4bec159f85d5796b8cf8f150a91221b7f842)
#### Saturday 2022-02-26 04:51:03 by George Spelvin

lib/sort: make swap functions more generic

Patch series "lib/sort & lib/list_sort: faster and smaller", v2.

Because CONFIG_RETPOLINE has made indirect calls much more expensive, I
thought I'd try to reduce the number made by the library sort functions.

The first three patches apply to lib/sort.c.

Patch #1 is a simple optimization.  The built-in swap has special cases
for aligned 4- and 8-byte objects.  But those are almost never used;
most calls to sort() work on larger structures, which fall back to the
byte-at-a-time loop.  This generalizes them to aligned *multiples* of 4
and 8 bytes.  (If nothing else, it saves an awful lot of energy by not
thrashing the store buffers as much.)

Patch #2 grabs a juicy piece of low-hanging fruit.  I agree that nice
simple solid heapsort is preferable to more complex algorithms (sorry,
Andrey), but it's possible to implement heapsort with far fewer
comparisons (50% asymptotically, 25-40% reduction for realistic sizes)
than the way it's been done up to now.  And with some care, the code
ends up smaller, as well.  This is the "big win" patch.

Patch #3 adds the same sort of indirect call bypass that has been added
to the net code of late.  The great majority of the callers use the
builtin swap functions, so replace the indirect call to sort_func with a
(highly preditable) series of if() statements.  Rather surprisingly,
this decreased code size, as the swap functions were inlined and their
prologue & epilogue code eliminated.

lib/list_sort.c is a bit trickier, as merge sort is already close to
optimal, and we don't want to introduce triumphs of theory over
practicality like the Ford-Johnson merge-insertion sort.

Patch #4, without changing the algorithm, chops 32% off the code size
and removes the part[MAX_LIST_LENGTH+1] pointer array (and the
corresponding upper limit on efficiently sortable input size).

Patch #5 improves the algorithm.  The previous code is already optimal
for power-of-two (or slightly smaller) size inputs, but when the input
size is just over a power of 2, there's a very unbalanced final merge.

There are, in the literature, several algorithms which solve this, but
they all depend on the "breadth-first" merge order which was replaced by
commit 835cc0c8477f with a more cache-friendly "depth-first" order.
Some hard thinking came up with a depth-first algorithm which defers
merges as little as possible while avoiding bad merges.  This saves
0.2*n compares, averaged over all sizes.

The code size increase is minimal (64 bytes on x86-64, reducing the net
savings to 26%), but the comments expanded significantly to document the
clever algorithm.

TESTING NOTES: I have some ugly user-space benchmarking code which I
used for testing before moving this code into the kernel.  Shout if you
want a copy.

I'm running this code right now, with CONFIG_TEST_SORT and
CONFIG_TEST_LIST_SORT, but I confess I haven't rebooted since the last
round of minor edits to quell checkpatch.  I figure there will be at
least one round of comments and final testing.

This patch (of 5):

Rather than having special-case swap functions for 4- and 8-byte
objects, special-case aligned multiples of 4 or 8 bytes.  This speeds up
most users of sort() by avoiding fallback to the byte copy loop.

Despite what ca96ab859ab4 ("lib/sort: Add 64 bit swap function") claims,
very few users of sort() sort pointers (or pointer-sized objects); most
sort structures containing at least two words.  (E.g.
drivers/acpi/fan.c:acpi_fan_get_fps() sorts an array of 40-byte struct
acpi_fan_fps.)

The functions also got renamed to reflect the fact that they support
multiple words.  In the great tradition of bikeshedding, the names were
by far the most contentious issue during review of this patch series.

x86-64 code size 872 -> 886 bytes (+14)

With feedback from Andy Shevchenko, Rasmus Villemoes and Geert
Uytterhoeven.

Link: http://lkml.kernel.org/r/f24f932df3a7fa1973c1084154f1cea596bcf341.1552704200.git.lkml@sdf.org
Signed-off-by: George Spelvin <lkml@sdf.org>
Acked-by: Andrey Abramov <st5pub@yandex.ru>
Acked-by: Rasmus Villemoes <linux@rasmusvillemoes.dk>
Reviewed-by: Andy Shevchenko <andriy.shevchenko@linux.intel.com>
Cc: Rasmus Villemoes <linux@rasmusvillemoes.dk>
Cc: Geert Uytterhoeven <geert@linux-m68k.org>
Cc: Daniel Wagner <daniel.wagner@siemens.com>
Cc: Don Mullis <don.mullis@gmail.com>
Cc: Dave Chinner <dchinner@redhat.com>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: Yousef Algadri <yusufgadrie@gmail.com>
Signed-off-by: Panchajanya1999 <panchajanya@azure-dev.live>

---
## [bellomia/MOTTlab](https://github.com/bellomia/MOTTlab)@[34f06d291c...](https://github.com/bellomia/MOTTlab/commit/34f06d291ce0e10201bb20745e988b15aa59f62a)
#### Saturday 2022-02-26 06:49:46 by Gabriele Bellomia

FIX: bandwidth scaling (cfr. 81bd520)

HISTORY

Working on the lattices feature branch we found a severe problem in the code, namely that changing both U and D maintaining U/D fixed, DOES change the results (which of course makes no sense).

- Initially I assumed to have introduced the bug myself, while working on the generic-dos extension. But the problems was still present if the Bethe lattice was selected.

- So I turned to the +plot module (cfr. a32d24a0a2060961acb298bfc11fe230c9203271), haunting for some silly error. No, the results *really* changed varying U and D together.

- Then I feared to have forgotten something important in the SOPT solver (the only place where U really enters and suspiciously D is totally absent). But no, it was fine.†

- At this point it was clear that the problem has been living unnoticed since the far past: in fact, it can be reproduced in the original notebook by Najera... BOOM!

So here I fix the notebook itself. 

> Maybe I should avoid doing this... isn't it meant to be a *static* resource? But what about future confusion if we diverge in such a core functionality. Also I may want the notebook to be useful to cloners, so yes, let's change it and make it clear somewhere in the markdown files: I could even "complete" it, by coding the exercises. :)

---------------------------

THE PROBLEM AND THE FIX

Najera had D=1 hardcoded in the <semi_circle_hiltrans()> function, so everything worked for itself. But if you make D actually a variable everything breaks, as in the Matlab code, for it is hardcoded also in another, somewhat hidden, place: a goddamn magic number!

    g0 = 1 / (w + eta - .25 * gloc)

which, for D=1, would stand for

    g0 = 1 / (w + eta - t**2 * gloc)

since for the Bethe lattice we have t = D/2

So we can fix the D ≠ 1 case by just changing it to

    g0 = 1 / (w + eta - .25 * D**2 * gloc)

- The same thing has been done in the dmft_loop() Matlab function. 
- The solution has been extensively tested in both Matlab's and Najera's code and it solves indeed the problem.
- A more general, lattice agnostic, solution has been implemented in the 'lattices' feature branch, where it is relevant. It will be merged here after the 'Bethe-only' version of the code is released, together with all the 'generic-lattices' material.
  > Cfr. 81bd520ed8f0b59f529ce68678c8889d29834cc3

---------------------------

FURTHER NOTES

†I want to comment extensively on this, for I feel today I learned something new... or at least improved my comprehension of the matter. I thought that the problem was that the second order diagram was proportional to U^2 instead of (U/D)^2. Afterall, perturbation theory is expected to come as an expansion on a small parameter and the proper small parameter here is indeed U/D or U/t, for sure not just U. Nevertheless I checked again the ref. by Haule and it was written as U^2.
Hence I thought a lot about the issue and finally realized that the 1/D^2 factor is already included in the diagram itself, for it comes from two nested convolutions of a spectral function, which values are indeed normalized depending on its support, i.e. D. If you increase D you decrease by D each value and so the result of the convolutions.

---
## [Anemony22/Arborealis](https://github.com/Anemony22/Arborealis)@[7560f30111...](https://github.com/Anemony22/Arborealis/commit/7560f301116d827af4abb2b54e2ff1f70d2fda6e)
#### Saturday 2022-02-26 08:22:16 by Ben Clark

The final piece - baked model rotations!

Thank you Jayden <3

... and fuck you Minecraft that was hard >:(

Co-Authored-By: FishTreeMan <39683679+FishTreeMan@users.noreply.github.com>

---
## [TheTimeSweeper/the](https://github.com/TheTimeSweeper/the)@[7d8f77439e...](https://github.com/TheTimeSweeper/the/commit/7d8f77439ee9e289b7a852035da71c75923b64c0)
#### Saturday 2022-02-26 11:33:02 by TheTimeSweeper

uh a lot of things I forgot as fuckin usual
m1 fuckin networked holy shit
iscombat figured out
sounds sounding off
skillsplus on m2 why
getting scary close god damn

---
## [mamh-mixed/git-git](https://github.com/mamh-mixed/git-git)@[52106430dc...](https://github.com/mamh-mixed/git-git/commit/52106430dc80ea20ec2e00a6079a7bc114d36b70)
#### Saturday 2022-02-26 12:30:38 by Ævar Arnfjörð Bjarmason

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
## [mamh-mixed/microsoft-terminal](https://github.com/mamh-mixed/microsoft-terminal)@[f2ebb21bd1...](https://github.com/mamh-mixed/microsoft-terminal/commit/f2ebb21bd13b20db38305136d34fa0778baf7920)
#### Saturday 2022-02-26 12:45:09 by Mike Griese

Add snap-layouts support to the Terminal (#11680)

Adds snap layout support to the Terminal's maximize button. This PR is
full of BODGY, so brace yourselves.

Big thanks to Chris Swan in #11134 for building the prototype.
I don't believe this solves #8795, because XAML islands can't get
nchittest messages

- The window procedure for the drag bar forwards clicks on its client
  area to its parent as non-client clicks.
- BODGY: It also _manually_ handles the caption buttons. They exist in
  the titlebar, and work reasonably well with just XAML, if the drag bar
  isn't covering them.
- However, to get snap layout support, we need to actually return
  `HTMAXBUTTON` where the maximize button is. If the drag bar doesn't
  cover the caption buttons, then the core input site (which takes up
  the entirety of the XAML island) will steal the `WM_NCHITTEST` before
  we get a chance to handle it.
- So, the drag bar covers the caption buttons, and manually handles
  hovering and pressing them when needed. This gives the impression that
  they're getting input as they normally would, even if they're not
  _really_ getting input via XAML.
- We also need to manually display the button tooltips now, because XAML
  doesn't know when they've been hovered for long enough. Hence, the
  `_displayToolTip` `ThrottledFuncTrailing`

## Validation
Minimized, maximized, restored down, hovered the buttons slowly, moved
the mouse over them quickly, they feel the same as before. But now with
snap layouts appearing.

## TODO!
* [x] I'm working on getting the ToolTips on the caption buttons back. Alas, I needed a demo of this _today_, so I'll fix that tomorrow morning.
* [x] mild concern: I should probably test Win 10 to make sure there wasn't weird changes to the message loop in win11 that means this is broken on win10.
* [x] I think I used the wrong issue number for tons of my comments throughout this PR. Double check that. Should be #9443, not #9447. 

Closes #9443
I thought this took care of #8587 ~as a bonus, because I was here, and the fix is _now_ trivial~, but looking at the latest commit that regressed.

Co-authored-by: Chris Swan <chswan@microsoft.com>

---
## [mamh-mixed/microsoft-terminal](https://github.com/mamh-mixed/microsoft-terminal)@[442432ea15...](https://github.com/mamh-mixed/microsoft-terminal/commit/442432ea15241a3e9ee3d70c5c24e5565655e55b)
#### Saturday 2022-02-26 12:45:09 by Mike Griese

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
## [mamh-mixed/microsoft-terminal](https://github.com/mamh-mixed/microsoft-terminal)@[f2222ecbef...](https://github.com/mamh-mixed/microsoft-terminal/commit/f2222ecbefcd54b968d1a0c05dea754e10d5dce1)
#### Saturday 2022-02-26 12:45:16 by Mike Griese

Make sure the infobar is inserted before the tab content, not on top of (#11609)

Fixes #11606

This is weird, but the infobars would appear totally on top of the
TerminalPage when `showTabsInTitlebar:false`. This would result in the infobar
obscuring the tabs.

Now, the infobars are strictly inserted after the tabs, before the content. So
when they appear, they will reduce the amount of space usable for the control.
That is a little annoying, but preferable to the tabs totally not existing.

Relevant conversation notes from #10798:

> > If the info bar is not local to the tab, then its location between the tab
> > bar (when the title bar is hidden) and the terminal panes feels
> > misleading. Should it instead be above the tab bar or below the terminal
> > panes?
>
> You're... not wrong here. It's maybe not the best place for it, but _on top_
> of the tabs would look insane, and probably wouldn't even work easily, given
> the way we reparent the tab row into the titlebar.
>
> In the pane itself would make more sense, but that runs abreast of all sorts
> of things like #9024, #4998, which might make more sense.

I'm just gonna go with this now, because it's _better_ than before, while we
work out what's _best_.

![gh-11606-fix](https://user-images.githubusercontent.com/18356694/138729178-b96b7003-0dd2-4521-8fff-0fd2a5989f22.gif)

(cherry picked from commit a916a5d9de450bc6a008d257d3c5c5cfd27e07ec)

---
## [clarencelol/kernel_xiaomi_sdm660-4.19](https://github.com/clarencelol/kernel_xiaomi_sdm660-4.19)@[9486134e7d...](https://github.com/clarencelol/kernel_xiaomi_sdm660-4.19/commit/9486134e7d53551fc8a126b0fe36067343787d0a)
#### Saturday 2022-02-26 13:07:11 by Joonsoo Kim

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
Signed-off-by: Carlos Jimenez (JavaShin-X) <javashin1986@gmail.com>
Signed-off-by: clarencelol <clarencekuiek@icloud.com>

---
## [BlackSilverUfa/data](https://github.com/BlackSilverUfa/data)@[5d9a9cac4c...](https://github.com/BlackSilverUfa/data/commit/5d9a9cac4c3a0dcdbe50cf4fb524f86777bbfefe)
#### Saturday 2022-02-26 13:19:53 by Jenkins

Запись стрима 1307474557

* Daymare: 1994 Sandcastle — 2 [100%]
* Прохождения за один стрим — Little Orpheus - Episode 1 [100%]
* Первый взгляд 2022 — The Bridge Curse: Road to Salvation (демо) [100%]
* Первый взгляд 2022 — My Friendly Neighborhood (демо) [100%]
* Первый взгляд 2022 — SCP: Pandemic (демо) [100%]
* Первый взгляд 2022 — IXION (демо) [98%]

---
## [Project-Awaken-Twelve/android_packages_apps_Launcher3](https://github.com/Project-Awaken-Twelve/android_packages_apps_Launcher3)@[dfdc34badc...](https://github.com/Project-Awaken-Twelve/android_packages_apps_Launcher3/commit/dfdc34badc10845dfd43b66e3b2ec2360a895ffe)
#### Saturday 2022-02-26 13:26:20 by Alex Cruz

Launcher3: Restart with change only on exit

This change allow the user to change everything they have to inside the
homescreen activity and only restart on exit. Previously this was a pain
in the fucking ass because you had to go in and set each option one by one
with a restart inbetween. At least now is not that big of a pain.

- Restart on destroy (hitting the back button, actionbar arrow)
- Restart when a chance is made and the home button is pressed

** Thanks "Jack" for code to detect home button
https://stackoverflow.com/a/27956263

- Cleaned up restart code

eyosen adapted to 10

Change-Id: I4962916ae0bd59d08247b59de585a97a2b9da3a1

---
## [NgGH707/NgGH-Magic-Origins-Mod](https://github.com/NgGH707/NgGH-Magic-Origins-Mod)@[de6a3234e2...](https://github.com/NgGH707/NgGH-Magic-Origins-Mod/commit/de6a3234e21ac42c139772a892489bf2386db4d1)
#### Saturday 2022-02-26 13:39:11 by NgGH707

2/26/2022 weekly bug fix

- Fixed a bug with 'Undying Life' perk
- Fixed a tool tip bug with charmed goblin background
- Fixed 'Gruesome Feast' active skill got from 'Gruesome Feast' perk causes crash
- Fixed player with 'Berserker Rage' effect still has a bloody look after battle
- Fixed a bug causes player lindwurm tail and some pets to not flee when retreat order is given
- Fixed a bug with 'Hand-to-hand Attack' of orc player
- Fixed some inconsistency with goblin, orc and beast player when you have PTR mod
- Hopefully fixed the ghost player has hollenhund skills
- Added a new permanent injury only for undead brother - 'Resurrected' - this special injury will have an effect to reduce a percentage of basic stats depending on how many times said undead brother struck down in battle. Every 30 days the effect will be weaken by 5% to a minimum of 10% penalty, the maximum penalty is 70%
- Tweaked 'Possessed' effect from ghost to deal with certain "exploit"
- Tweaked 'Legion' origin
- Changed 2 existing armor pieces into legendary armor pieces (sadly there is no non-layer version)
- Allowed some orc armor to have less limited layer
- Slightly increase the chance to find 'Mysterious Traveller' situation
- 'Mage Trio' origin has higher chance to find 'Mysterious Traveller' situation
- Adjusted the company strength calculation
- Mounted player affects company strength

---
## [Lance0-32/CyberCodeOnline](https://github.com/Lance0-32/CyberCodeOnline)@[f9fd302bd7...](https://github.com/Lance0-32/CyberCodeOnline/commit/f9fd302bd7f43a7a693c1ae306071bea3ef64344)
#### Saturday 2022-02-26 14:13:58 by Lance0-32

Update tips.txt

haha guys exp memories guys (they stopped existing)

also deixtoria thank your for the new facts about enemy XP NOW PLS STOP TALKING ABOUT IT BECAUSE I MADE THIS TIP AND IT'S CAUSING EMOTIONAL DAMAGE WHICH WAS VERY EFFECTIVE. (they didn't actually talk about it that much I'm overdramatizing lmao)

and some things that somehow slipped by people, myself included. WAIT I SHOULD'VE JUST DONE THE "some changes joke" ;-;

guess I'll do it for the additions, which are:
some changes

---
## [henricaodopao1/kernel-to-flash-to-use-to-report-unexistent-bugs-to-feed-to-sleep-to-talk-to](https://github.com/henricaodopao1/kernel-to-flash-to-use-to-report-unexistent-bugs-to-feed-to-sleep-to-talk-to)@[c3dae3639b...](https://github.com/henricaodopao1/kernel-to-flash-to-use-to-report-unexistent-bugs-to-feed-to-sleep-to-talk-to/commit/c3dae3639b80462c87fe3e83f0897e03d08c91e2)
#### Saturday 2022-02-26 15:36:27 by Dave Chiluk

sched/fair: Fix low cpu usage with high throttling by removing expiration of cpu-local slices

commit de53fd7aedb100f03e5d2231cfce0e4993282425 upstream.

It has been observed, that highly-threaded, non-cpu-bound applications
running under cpu.cfs_quota_us constraints can hit a high percentage of
periods throttled while simultaneously not consuming the allocated
amount of quota. This use case is typical of user-interactive non-cpu
bound applications, such as those running in kubernetes or mesos when
run on multiple cpu cores.

This has been root caused to cpu-local run queue being allocated per cpu
bandwidth slices, and then not fully using that slice within the period.
At which point the slice and quota expires. This expiration of unused
slice results in applications not being able to utilize the quota for
which they are allocated.

The non-expiration of per-cpu slices was recently fixed by
'commit 512ac999d275 ("sched/fair: Fix bandwidth timer clock drift
condition")'. Prior to that it appears that this had been broken since
at least 'commit 51f2176d74ac ("sched/fair: Fix unlocked reads of some
cfs_b->quota/period")' which was introduced in v3.16-rc1 in 2014. That
added the following conditional which resulted in slices never being
expired.

if (cfs_rq->runtime_expires != cfs_b->runtime_expires) {
	/* extend local deadline, drift is bounded above by 2 ticks */
	cfs_rq->runtime_expires += TICK_NSEC;

Because this was broken for nearly 5 years, and has recently been fixed
and is now being noticed by many users running kubernetes
(https://github.com/kubernetes/kubernetes/issues/67577) it is my opinion
that the mechanisms around expiring runtime should be removed
altogether.

This allows quota already allocated to per-cpu run-queues to live longer
than the period boundary. This allows threads on runqueues that do not
use much CPU to continue to use their remaining slice over a longer
period of time than cpu.cfs_period_us. However, this helps prevent the
above condition of hitting throttling while also not fully utilizing
your cpu quota.

This theoretically allows a machine to use slightly more than its
allotted quota in some periods. This overflow would be bounded by the
remaining quota left on each per-cpu runqueueu. This is typically no
more than min_cfs_rq_runtime=1ms per cpu. For CPU bound tasks this will
change nothing, as they should theoretically fully utilize all of their
quota in each period. For user-interactive tasks as described above this
provides a much better user/application experience as their cpu
utilization will more closely match the amount they requested when they
hit throttling. This means that cpu limits no longer strictly apply per
period for non-cpu bound applications, but that they are still accurate
over longer timeframes.

This greatly improves performance of high-thread-count, non-cpu bound
applications with low cfs_quota_us allocation on high-core-count
machines. In the case of an artificial testcase (10ms/100ms of quota on
80 CPU machine), this commit resulted in almost 30x performance
improvement, while still maintaining correct cpu quota restrictions.
That testcase is available at https://github.com/indeedeng/fibtest.

Fixes: 512ac999d275 ("sched/fair: Fix bandwidth timer clock drift condition")
Signed-off-by: Dave Chiluk <chiluk+linux@indeed.com>
Signed-off-by: Peter Zijlstra (Intel) <peterz@infradead.org>
Reviewed-by: Phil Auld <pauld@redhat.com>
Reviewed-by: Ben Segall <bsegall@google.com>
Cc: Ingo Molnar <mingo@redhat.com>
Cc: John Hammond <jhammond@indeed.com>
Cc: Jonathan Corbet <corbet@lwn.net>
Cc: Kyle Anderson <kwa@yelp.com>
Cc: Gabriel Munos <gmunoz@netflix.com>
Cc: Peter Oskolkov <posk@posk.io>
Cc: Cong Wang <xiyou.wangcong@gmail.com>
Cc: Brendan Gregg <bgregg@netflix.com>
Link: https://lkml.kernel.org/r/1563900266-19734-2-git-send-email-chiluk+linux@indeed.com
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>
Signed-off-by: Ratoriku <a1063021545@gmail.com>
Signed-off-by: Peppe289 <gsperanza204@gmail.com>

---
## [Evolution-X-Devices/kernel_oneplus_sm8250](https://github.com/Evolution-X-Devices/kernel_oneplus_sm8250)@[22f8333101...](https://github.com/Evolution-X-Devices/kernel_oneplus_sm8250/commit/22f8333101a304d7559a31a2e19df21a5fcefaee)
#### Saturday 2022-02-26 18:38:50 by alk3pInjection

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
Signed-off-by: AnierinB <anierin@evolution-x.org>

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[8dd7a3cd3b...](https://github.com/mrakgr/The-Spiral-Language/commit/8dd7a3cd3b35f53a6c0fd45ce2427ef79defdf37)
#### Saturday 2022-02-26 19:33:15 by Marko Grdinić

"11:45am. I am up really late today it seems.

11:55am. Let me start with breakfast. I'll have to skip the morning session.

12:30pm. Let me od the chores.

3:30pm. Brrr, I am back. It was freezing outside. But I am finally done with the wall and will be able to get back to my usual routine. Let me take a break here. No way am I starting right after doing physical labor.

3:55pm. Just a bit more and I will start.

4pm. Let me start.

What I should do here is finish the rock tutorial from yesterday. I've learned quite a bit from it, and I'll pay my respect by finishing it. After that...I guess I'll study height maps for a bit. I am in such a mood.

4:20pm. https://youtu.be/WTg_pVZoac0?t=8684

Instead of using VOPs for everything, when he is straightforwardsly adding noise, he should have just used the Volume Noise Fog SOP. Or the Volue Adjust Fog. For calculating the noise directions, he should have used Orientation Along Curve rather than taking cross products.

Oh yes, I meant to check, how did the do the wind erosion gradient effect yesterday.

https://youtu.be/WTg_pVZoac0?t=8717

Let me pause here so I can backtrack.

https://youtu.be/WTg_pVZoac0?t=6906

He did not use the relative to bounding box, but instead just showed the height straight in and clamped it.

Ok that answers it. Let me go back to where I was.

Come to think of it didn't he use curves at some point? What happened to that. Let me not check this as I can't remember where that was.

4:50pm. Focus me, stop reading threads on the side.

I need to finish this video.

https://youtu.be/WTg_pVZoac0?t=9162
> I think this is pretty much impossible to sculpt by hand or even think to sculpt these details because our brain is...we are used to add stuff or remove stuff. It is hard for us to carve in details like this or imagine them.

https://youtu.be/WTg_pVZoac0?t=9240

Hmmm, does it really have to be a fog VDB, could a distance VDB have worked for this as well. It would certainly have been easier to visualize.

https://youtu.be/WTg_pVZoac0?t=9759

Side Distance Field? I thought it was supposed to be signed? Signed certainly makes more sense.

https://youtu.be/WTg_pVZoac0?t=9932
> In truth is, the proper workflow to do volume displacement is to use the signed distance fields?

So what was the point of using fog VDBs then?

5:10pm. He is reiterating that he used fog because he did not want to overcomplicate things and that the proper way is to use SDFs.

Even though I've wondered about this, I am quite surprise to hear him come and say that he has been doing things wrong on purpose for the last 2h.

https://youtu.be/WTg_pVZoac0?t=10214

Hmmm, density is the only output. But he needs distance for SDFs, right?

5:40pm. I do not understand how one can just sample SDF using noise positions and have the result be consistent. Does the Volume VOP recalculate the inner parts?

https://www.sidefx.com/tutorials/the-complete-a-z-terrain-handbook/

https://youtu.be/WTg_pVZoac0?t=12236
> I just want you guys to see the result of this cooking live. And the cool thing aobut this is that detail is not going to change between the low res and the high res. So you can work on the low res, obviously you are not going to be able to see it as clearly as with the high res, but everything will be the same. It is just that when you go high res, you are going to get more details. It is very important to have this kind of workflow. It is not like when you do a sim. For example, you do a sim at low resolution you get something and you go high res it is completely different.

https://youtu.be/WTg_pVZoac0?t=12648

The way he did this is pretty principled. I approve. I've been harping too hard on him.

6:15pm. Let me go have lunch.

6:30pm. Done with both lunch and video.

https://youtu.be/WTg_pVZoac0?t=12547

I am going over some of the earlier points. Just what is this transform node?

Why does it not have the pivot options. Is this some old Houdini version that did not have it?

6:50pm. Actually, I did not know that it was possible to substract flat planes from objects. That could be useful.

6:55pm. I see. The direction of the grid actually matters during the substraction.

Ok, I am satisfied. Since I do not feel like working on my own stuff, let me watch the height field tutorial.

https://www.sidefx.com/tutorials/the-complete-a-z-terrain-handbook/

7pm. Oh, this is way bigger than I thought it would be.

Sigh, I hate Vimeo. It is slow to load and has a shitty interface. I am trying to look into the playlist so I can see how long it is, but I am failing. Let me just watch the basics for a while then.

7:45pm. Mask by slope could be used to calculate the slopes. I see how they figured out the cliffs in Far Cry.

8:05pm. https://www.sidefx.com/tutorials/the-complete-a-z-terrain-handbook/

I'll leave the 03 for tomorrow. I think I've grasped heightfields quite a bit, but I do want to see how he goes about creating terrains.

Mhhh...I want to play Fallout, but just the thought of playing games while there is work that needs doing fills me with disgust.

No, remember those days in 2017-2018 when I thought I had heart problems when it was stress. I should not push it. 8pm is way overdue for me to stop for the day. 8pm is the time to read manga and play games, not study like my life depended on it.

What I should do tomorrow is dedicate the time to study these heightfield videos. I'll learn properly if I do it with a fresh mind. I also have those Mantra shading tutorials waiting for me, but I'll leave those for later.

8:10pm. I am simply curious. I want to learn how to do terrain more than I want to work on my own project. Now that I know how to sculpt density, I can finish it without much fuss.

I'll do the tiles using geometry, and then move to shading. I'll want to learn how to add details at the shader level. Adding noise to the flat colors will add a lot of life to them. I do not need manual texture painting. For the pool scene I am going to go all the way using just Houdini.

For the later scenes, I'll take a look at USD Exporing and do my work in Blender.

That having said, even if I end up working in Blender, I should not think in Blender. Just as if I were programming in C, I should not think in C, but in a higher language instead. Houdini is the 3d art software equivalent of Haskell. It has that allure for me.

I should learn it inside and out so that I can apply its techniques while working in Blender. I'll see how things go.

Hmmmm, I should really try to export to USD, and doing the lookdev in Blender. If Blender allows me to import the packed primitives I could go quite far with it.

8:20pm. Houdini really is good for geometry, this noise stuff is like a dream. I am reminded how Maass claimed that the brain is generating noise, and this kind of process noise shaping is something that strikes a chord with me.

I could try to do it all by hand, but that would not get me far. By injecting some noise detail, I could go a long way into improving the quality of my scenes.

8:25pm. Very well. This will be the priority.

* Terrain handbook.
* Figure out the USD imports/exports.
* Finally finish the scene. Revisit the Matra shading tutorial for ideas on how to use shader nodes.

If I can cover this, I think I'll have mastered about 10% of Houdini. I feel that I've internalized quite a few nodes. Something like 30% would already be enough to be considered an expert for my use case. A few months more of practice at it and I will be quite proficient at both Blender and Houdini. I'll become quite powerful at that point.

I guess I won't be able to move into music any time soon, but I have full intention of covering that as well.

Only when I have the complete package of art, music, programming will I be able to do what I want.

I could have rushed to do my work in Blender, but you only learn things once. Houdini is an unique experience. By the time next year comes around I will have zero weaknesses as a creator.

8:30pm. When I get the money, the first thing I will do is buy a better GPU. I do not care about games, but a 3090 RTX's realtime raytracing could significantly improve my lookdev workflow. I regret that I could not buy one today.

All in due time. Now that I do not have to spend extra time clearing that wall, I'll be able to get back to my usual work habits."

---
## [ChristopherChudzicki/mathbox-react](https://github.com/ChristopherChudzicki/mathbox-react)@[523523e713...](https://github.com/ChristopherChudzicki/mathbox-react/commit/523523e713476687677973e0b77743fdbb27fca6)
#### Saturday 2022-02-26 20:07:42 by Chris Chudzicki

Add unit tests on CI

This adds some very basic jest unit tests. Some challenges in implementing this were:

- mathbox, threejs, shadergraph, and threestrap all use ES6 import/export syntax. By default, jest does not transform node_modules. This can be overridden with `transformIgnorePatterns`. Initially that wasn't working... but when I added babel.config.js, `transformIgnorePatterns` started working
- JSDom isn't a real browser, and ThreeJS / Mathbox both want WebGL APIs that it doesn't implement. Mocking these seems like a pain in the rear. So I added a proxy-based automock. Neat black magic I hope I don't regret.

    We'll see. Maybe a real browser-based test runner like Karma would have been better.

Additionally, I made Mathbox render its own div. Because... not doing that was annoying.

---
## [alterae/lang](https://github.com/alterae/lang)@[90cce11e66...](https://github.com/alterae/lang/commit/90cce11e6686953787a360681bc1c33862982309)
#### Saturday 2022-02-26 23:11:34 by Michelle S

More project skeleton

I think this might be a wash.  Look into doing this in Rust, so I don't
have to deal with Go's awful module system holy shit

---

