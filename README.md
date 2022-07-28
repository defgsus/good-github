## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-07-27](docs/good-messages/2022/2022-07-27.md)


1,985,723 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,985,723 were push events containing 3,098,637 commit messages that amount to 250,214,584 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 38 messages:


## [faaaay/sojourn-station](https://github.com/faaaay/sojourn-station)@[ef4665ec90...](https://github.com/faaaay/sojourn-station/commit/ef4665ec90474cf5ac5f6aff34b6fd30e365429d)
#### Wednesday 2022-07-27 00:17:22 by DimmaDunk

I HATE LIVERMED, I HATE LIVERMED, I HATE LIVERMED!!! (#3714)

* Makes combat medical kits better

- Replaces Dylovene pill bottle on Combat Medical Kit with Carthatoline pill bottle, as every chem inside it already WAS an upgrade over their normal counterparts, making it better at halting toxins damage and preventing liver from killing you. Also adds a Sanguinum syrette to stave off massive bloodloss which would cause the former as well.
- Replaces one of the Quicklot syrettes with a Sanguinum syrette on the Oxygen Deprivation First Aid Kit for better treatment of causes of oxyloss.
- Standardizes pill icons based on chem colors across all pre-built pills for easier reognition.
- Guarantees the "skill issue/salt PR" tag since it doesn't fix underlying issues of current medical system

* Adds carthatoline pills to deferred and corpsman large kit

Keeping in line with the rest of the PR.

* Blood regen pills!

- Adds pre-made Ferritin-Hemosiderin pills composed of iron and protein to help regenerate lost blood
- Replaces Sanguinum syrette on combat kit with ferritin-hemosiderin pill bottle
- Combat surgery kits now really hold advanced tools (except bone gel since the adv version is Soteria made)
- Makes the advanced bone gel item description not a copypaste of its stock counterpart

* Forgot a comma

Damn my haste.

---
## [batrick/ceph](https://github.com/batrick/ceph)@[098b9e1fd9...](https://github.com/batrick/ceph/commit/098b9e1fd9183d440ec77979f9191b48a24b6adb)
#### Wednesday 2022-07-27 00:28:56 by Patrick Donnelly

qa: use postmerge hooks for filtering stock kernel

Up to now, the k-stock kernel required an awkward matrix configuration
to ensure that we're only testing the rhel stock kernel. This is
basically done by overriding (evil) the yaml fragment specifying the
distribution.  So, you'd have a config like:

	fs/snaps/{begin clusters/1a3s-mds-1c-client conf/{client mds mon osd} distro/{ubuntu_latest} mount/kclient/{mount overrides/{distro/stock/{k-stock rhel_8} ms-die-on-skipped}} objectstore-ec/bluestore-bitmap overrides/{whitelist_health whitelist_wrongly_marked_down} tasks/workunit/snaps}

One would rightly believe it's running with ubuntu but, actually, the
rhel_8 fragment overrides this.

Instead of this, we're using the new postmerge teuthology hooks to
filter our configs containing k-stock when the rhel distribution is not
selected.

This is great (and a small change by itself) but doing so would bias the
selection of jobs towards k-testing/fuse which do not drop configs not
using rhel. To work around this, we add another two rhel (three total)
fragments to the custom `qa/cephfs/distro` to compensate. The extra two
rhel fragments drop if the k-stock config is not in use.  This also
uses the teuthology postmerge hooks.

Simultaneously, we're dropping the random selection of distributions as
it's no longer necessary with nested subsets (another newer teuthology
feature). Instead, modify fs:* sub-suites to divide jobs by 2 to
approximate.

Signed-off-by: Patrick Donnelly <pdonnell@redhat.com>

---
## [zzcclp/spark](https://github.com/zzcclp/spark)@[c4c623a3a8...](https://github.com/zzcclp/spark/commit/c4c623a3a890267b2f9f8d472c8be30fc5db53e1)
#### Wednesday 2022-07-27 00:30:54 by Hyukjin Kwon

[SPARK-39869][SQL][TESTS] Fix flaky hive - slow tests because of out-of-memory

### What changes were proposed in this pull request?

This PR adds some manual `System.gc`. I know enough that this doesn't guarantee the garbage collection and sounds somewhat funny but it works in my experience so far, and I did such hack in some places before.

### Why are the changes needed?

To deflake the tests.

### Does this PR introduce _any_ user-facing change?

No, dev and test-only.

### How was this patch tested?

CI in this PR should test it out.

Closes #37291 from HyukjinKwon/SPARK-39869.

Authored-by: Hyukjin Kwon <gurwls223@apache.org>
Signed-off-by: Hyukjin Kwon <gurwls223@apache.org>

---
## [HalfdeadKiller/HDK-Foundation-19](https://github.com/HalfdeadKiller/HDK-Foundation-19)@[befabcec33...](https://github.com/HalfdeadKiller/HDK-Foundation-19/commit/befabcec333347ce6b918d67d4c884b9e0dcefea)
#### Wednesday 2022-07-27 00:37:56 by TenameACAccount

more dcz changes yay (#548)

* Update site53-1.dmm

* fallout 5 on the byond engine

* fuck you box

Co-authored-by: UserU <37943518+User-U-U@users.noreply.github.com>

---
## [Ivysaur-Mrquestionmarks/epstein2020](https://github.com/Ivysaur-Mrquestionmarks/epstein2020)@[222c275524...](https://github.com/Ivysaur-Mrquestionmarks/epstein2020/commit/222c27552463663667e9b351181c83a818328674)
#### Wednesday 2022-07-27 00:52:47 by Blackbirdboom295

“ War. War never changes. In the year 1945, my great-great grandfather, serving in the army, wondered when he'd get to go home to his wife and the son he'd never seen. He got his wish when the US ended World War II by dropping atomic bombs on Hiroshima and Nagasaki.  The World awaited Armageddon; instead, something miraculous happened. We began to use atomic energy not as a weapon, but as a nearly limitless source of power.  People enjoyed luxuries once thought the realm of science fiction. Domestic robots, fusion-powered cars, portable computers. But then, in the 21st century, people awoke from the American dream.  Years of consumption lead to shortages of every major resource. The entire world unraveled. Peace became a distant memory. It is now the year 2077. We stand on the brink of total war, and I am afraid. For myself, for my wife, for my infant son - because if my time in the army taught me one thing: it's that war, war never changes.

---
## [loot/skyrimvr](https://github.com/loot/skyrimvr)@[20d4c5cf00...](https://github.com/loot/skyrimvr/commit/20d4c5cf000a5fc93a0773e0d792c2cde36cba28)
#### Wednesday 2022-07-27 01:14:02 by MacSplody

Remove Creation Club Related Metadata (#21)

* Remove messages
 - Patch messages related to CC files.

* Remove files
- Additional Clockwork CC patches.
- Apothecary CC patches.
- CFTO Bittercup Compatibility Patch.
- Carriage Ferry Travel Overhaul (CFTO) Bittercup Fix.
- Curated Curios - A Creation Club Integration Mod.
- Fishing Gloves.
- Immersive College of Winterhold Patch Collection - CC patches.
- kryptopyr's Patch Hub CC files.
- Knight of the North - A Creation Club Quest Overhaul.
- Morrowind Threads - A Creation Club Integration Mod.
- Orcish Orc Strongholds - Creation Club Orcish Armors Integrated.
- Pirate's Life for Me - A Creation Club Integration Mod.
- Prince and Pauper Refine Bloodthorn Manor patch.
- Rare Curios - Bolts Expanded.
- Rob''s Bug Fixes - Capital Whiterun Expansion - Fishing patch.
- Survival Mode Patch Collection.
- Tamrielic Distribution CC patches.
- The Vigilants'' New Clothes - A Creation Club Integration Mod.
- Thwack - A Creation Club Integration Mod.

---
## [Just-a-Unity-Dev/Nyanotrasen](https://github.com/Just-a-Unity-Dev/Nyanotrasen)@[e454ba6bd0...](https://github.com/Just-a-Unity-Dev/Nyanotrasen/commit/e454ba6bd034cb4b3682808e9fced42c1c295f1a)
#### Wednesday 2022-07-27 01:55:43 by Rane

Despair (#298)

* Include thrown entity in ThrowAttemptEvent

* whoops cringe

* lgtm

* woops i broke shit

* make them scream

* holy shit laugh at this man

* remove logger

* dont let you carry yourself

---
## [KathrinBailey/tgstation](https://github.com/KathrinBailey/tgstation)@[9428d97a4f...](https://github.com/KathrinBailey/tgstation/commit/9428d97a4fadf8a486b0c6fbe2ee345a2780e687)
#### Wednesday 2022-07-27 01:55:49 by Imaginos16

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
## [Nyanotrasen/Nyanotrasen](https://github.com/Nyanotrasen/Nyanotrasen)@[e832904b7c...](https://github.com/Nyanotrasen/Nyanotrasen/commit/e832904b7c4b7d94dbd8f71bc29296a36e6e37ce)
#### Wednesday 2022-07-27 02:15:32 by eclips_e

Sweater (#302)

* Sweater and proto

* Clothesmate

* fuck you tests

Co-authored-by: Just-a-Unity-Dev <just-a-unity-dev@users.noreply.github.com>

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[b15331b4df...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/b15331b4df9bd525ba80b284beb3442f180c01be)
#### Wednesday 2022-07-27 02:19:45 by OrionTheFox

[MANUAL MIRROR] The GAGening: Clothesmate edition [MDB IGNORE] (#15100)

* The GAGening: Clothesmate edition

* ThisShouldWork

* hgnbhg

* would probably help to have the right .dmi

* fixed?

* Fuck you

Co-authored-by: Twaticus <46540570+Twaticus@users.noreply.github.com>

---
## [peterhoeg/doom-emacs](https://github.com/peterhoeg/doom-emacs)@[b07614037f...](https://github.com/peterhoeg/doom-emacs/commit/b07614037f7670682d2c193d83abdb9eed9f218e)
#### Wednesday 2022-07-27 05:10:43 by TEC

fix(mu4e): support mu 1.8

Thanks to some combination of ignorance and obstinance, mu4e has thrown
compatibility to the wind and completely ignored the exitance of
define-obsolete-function-alias. Coupled with the inconsistent/partial
function renaming, this has made the mu4e 1.6⟶1.8 change particularly
annoying to deal with.

By suffering the pain of doing the mu4e author's work for them, we can
use defalias to give backwards compatibility a good shot for about 60
functions. Some mu4e~x functions are now mu4e--x, others are unchanged,
and then you've got a few odd changes like mu4e~proc -> mu4e--server and
mu4e-search-rerun. The form of message :from entries has also changed,
and a new (mu4e) entrypoint added supplanting mu4e~start.

Fix: #6511
Close: #6549
Co-authored-by: Rahguzar <aikrahguzar@gmail.com>

---
## [TheRakeshPurohit/rust](https://github.com/TheRakeshPurohit/rust)@[1a5925dc84...](https://github.com/TheRakeshPurohit/rust/commit/1a5925dc84d0ef966023d6612147f93a0464174c)
#### Wednesday 2022-07-27 07:05:09 by bors

Auto merge of #12294 - listochkin:prettier, r=Veykril

Switch to Prettier for TypeScript Code formatting

## Summary of changes:

 1. Added [`.editorconfig` file](https://editorconfig.org) to dictate general hygienic stuff like character encoding, no trailing whitespace, new line symbols etc. for all files (e.g. Markdown). Install an editor plugin to get this rudimentary formatting assistance automatically. Prettier can read this file and, for example, use it for indentation style and size.
 2. Added a minimal prettier config file. All options are default except line width, which per [Veykril](https://github.com/Veykril) suggestion is set to 100 instead of 80, because [that's what `Rustfmt` uses](https://rust-lang.github.io/rustfmt/?version=v1.4.38&search=#max_width).
 3. Change `package.json` to use Prettier instead of `tsfmt` for code formatting.
 4. Performed initial formatting in a separate commit, per [bjorn3](https://github.com/bjorn3) suggestion added its hash to a `.git-blame-ignore-revs` file. For it to work you need to add a configuration to your git installation:
    ```Shell
    git config --global blame.ignoreRevsFile .git-blame-ignore-revs
    ```
 5. Finally, removed `typescript-formatter` from the list of dependencies.

----
What follows below is summary of the discussion we had on Zulip about the formatter switch:

## Background

For the context, there are three reasons why we went with `tsfmt` originally:
* stick to vscode default/built-in
* don't add extra deps to package.json.lock
* follow upstream (language server node I think still uses `tsfmt`)

And the meta reason here was that we didn't have anyone familiar with frontend, so went for the simplest option, at the expense of features and convenience.

Meanwhile, [**Prettier**](https://prettier.io) became a formatter project that JS community consolidated on a few years ago. It's similar to `go fmt` / `cargo fmt` in spirit: minimal to no configuration to promote general uniformity in the ecosystem. There are some options, that were needed early on to make sure the project gained momentum, but by no means it's a customizable formatter that is easy to adjust to reduce the number of changes for adoption.

## Overview of changes performed by Prettier

Some of the changes are acceptable. Prettier dictates a unified string quoting style, and as a result half of our imports at the top are changed. No one would mind that. Some one-line changes are due to string quotes, too, and although these a re numerous, the surrounding lines aren't changed, and git blame / GitLens will still show relevant context.

Some are toss ups. `trailingComma` option - set it to `none`, and get a bunch of meaningless changes in half of the code. set it to `all` and get a bunch of changes in the other half of the code. Same with using parentheses around single parameters in arrow functions: `x => x + 1` vs `(x) => x + 1`. Perrier forces one style or the other, but we use both in our code.

Like I said, the changes above are Ok - they take a single line, don't disrupt GitLens / git blame much. **The big one is line width**. Prettier wants you to choose one and stick to it. The default is 80 and it forces some reformatting to squish deeply nested code or long function type declarations. If I set it to 100-120, then Prettier finds other parts of code where a multi-line expression can be smashed into a single long line. The problem is that in both cases some of the lines that get changed are interesting, they contain somewhat non-trivial logic, and if I were to work on them in future I would love to see the commit annotations that tell me something relevant. Alas, we use some of that.

## Project impact

Though Prettier is a mainstream JS project it has no dependencies. We add another package so that it and ESLint work together nicely, and that's it.

---
## [ynot01/Yogstation](https://github.com/ynot01/Yogstation)@[5bbc6a2401...](https://github.com/ynot01/Yogstation/commit/5bbc6a2401361e71f4c6fb0ad173900153603787)
#### Wednesday 2022-07-27 07:20:59 by Marmio64

Sinful demon changes + re-enable (#14345)

* first wave of demon changes

many changes
1: gluttonous demons hunger 3x as fast as normal people
2: all demons no longer enter softcrit (still can enter hardcrit), are geneless, dont suffocate in crit, and have stable hearts.
3: true demon form deals 20 damage instead of 24 (wrath is 24 instead of 28). Health is lowered to 160 and health regen per hit is now 8 instead of 10. To compensate, they are ever so slightly faster, but are still slower than everyone but podpeople. Demons also lose 2 hp every life tick (a life tick is generally 2 seconds, so 2 hp every 2 seconds), so as to try to deter you from staying in demon form the entire round.
4: objectives are made a bit less murderbone-ey.
5: sinful demon spawns slightly less often

* re enables event

* fixes

* removes chance for envy to get an identity theft objective

* word change

* sinful demon is rarer still

honestly, they arent very interesting if they happen too much, so i'd like them to mildly rare

Co-authored-by: Jamie D <993128+JamieD1@users.noreply.github.com>

---
## [Foundation-19/Foundation-19](https://github.com/Foundation-19/Foundation-19)@[96615f6506...](https://github.com/Foundation-19/Foundation-19/commit/96615f650661292a92b79eb1983064556188cb37)
#### Wednesday 2022-07-27 08:42:52 by harryob

LFification, again, maybe for real this time (#568)

* what is this cursed shit

* shut up PLEASE

* everything non-LF should be LFd

Co-authored-by: tichys <tichman27@gmail.com>

---
## [llvm/llvm-project](https://github.com/llvm/llvm-project)@[15f3cd6bfc...](https://github.com/llvm/llvm-project/commit/15f3cd6bfc670ba6106184a903eb04be059e5977)
#### Wednesday 2022-07-27 09:11:32 by Matheus Izvekov

[clang] Implement ElaboratedType sugaring for types written bare

Without this patch, clang will not wrap in an ElaboratedType node types written
without a keyword and nested name qualifier, which goes against the intent that
we should produce an AST which retains enough details to recover how things are
written.

The lack of this sugar is incompatible with the intent of the type printer
default policy, which is to print types as written, but to fall back and print
them fully qualified when they are desugared.

An ElaboratedTypeLoc without keyword / NNS uses no storage by itself, but still
requires pointer alignment due to pre-existing bug in the TypeLoc buffer
handling.

---

Troubleshooting list to deal with any breakage seen with this patch:

1) The most likely effect one would see by this patch is a change in how
   a type is printed. The type printer will, by design and default,
   print types as written. There are customization options there, but
   not that many, and they mainly apply to how to print a type that we
   somehow failed to track how it was written. This patch fixes a
   problem where we failed to distinguish between a type
   that was written without any elaborated-type qualifiers,
   such as a 'struct'/'class' tags and name spacifiers such as 'std::',
   and one that has been stripped of any 'metadata' that identifies such,
   the so called canonical types.
   Example:
   ```
   namespace foo {
     struct A {};
     A a;
   };
   ```
   If one were to print the type of `foo::a`, prior to this patch, this
   would result in `foo::A`. This is how the type printer would have,
   by default, printed the canonical type of A as well.
   As soon as you add any name qualifiers to A, the type printer would
   suddenly start accurately printing the type as written. This patch
   will make it print it accurately even when written without
   qualifiers, so we will just print `A` for the initial example, as
   the user did not really write that `foo::` namespace qualifier.

2) This patch could expose a bug in some AST matcher. Matching types
   is harder to get right when there is sugar involved. For example,
   if you want to match a type against being a pointer to some type A,
   then you have to account for getting a type that is sugar for a
   pointer to A, or being a pointer to sugar to A, or both! Usually
   you would get the second part wrong, and this would work for a
   very simple test where you don't use any name qualifiers, but
   you would discover is broken when you do. The usual fix is to
   either use the matcher which strips sugar, which is annoying
   to use as for example if you match an N level pointer, you have
   to put N+1 such matchers in there, beginning to end and between
   all those levels. But in a lot of cases, if the property you want
   to match is present in the canonical type, it's easier and faster
   to just match on that... This goes with what is said in 1), if
   you want to match against the name of a type, and you want
   the name string to be something stable, perhaps matching on
   the name of the canonical type is the better choice.

3) This patch could expose a bug in how you get the source range of some
   TypeLoc. For some reason, a lot of code is using getLocalSourceRange(),
   which only looks at the given TypeLoc node. This patch introduces a new,
   and more common TypeLoc node which contains no source locations on itself.
   This is not an inovation here, and some other, more rare TypeLoc nodes could
   also have this property, but if you use getLocalSourceRange on them, it's not
   going to return any valid locations, because it doesn't have any. The right fix
   here is to always use getSourceRange() or getBeginLoc/getEndLoc which will dive
   into the inner TypeLoc to get the source range if it doesn't find it on the
   top level one. You can use getLocalSourceRange if you are really into
   micro-optimizations and you have some outside knowledge that the TypeLocs you are
   dealing with will always include some source location.

4) Exposed a bug somewhere in the use of the normal clang type class API, where you
   have some type, you want to see if that type is some particular kind, you try a
   `dyn_cast` such as `dyn_cast<TypedefType>` and that fails because now you have an
   ElaboratedType which has a TypeDefType inside of it, which is what you wanted to match.
   Again, like 2), this would usually have been tested poorly with some simple tests with
   no qualifications, and would have been broken had there been any other kind of type sugar,
   be it an ElaboratedType or a TemplateSpecializationType or a SubstTemplateParmType.
   The usual fix here is to use `getAs` instead of `dyn_cast`, which will look deeper
   into the type. Or use `getAsAdjusted` when dealing with TypeLocs.
   For some reason the API is inconsistent there and on TypeLocs getAs behaves like a dyn_cast.

5) It could be a bug in this patch perhaps.

Let me know if you need any help!

Signed-off-by: Matheus Izvekov <mizvekov@gmail.com>

Differential Revision: https://reviews.llvm.org/D112374

---
## [doomgutt/NMA-CN-2022-Project--Group-A---Attractor-Networks](https://github.com/doomgutt/NMA-CN-2022-Project--Group-A---Attractor-Networks)@[c3f55e22cc...](https://github.com/doomgutt/NMA-CN-2022-Project--Group-A---Attractor-Networks/commit/c3f55e22ccbe4b9c433c3287cfa7e9f7548e0b52)
#### Wednesday 2022-07-27 10:05:25 by doomgutt

fuck you saqib, All I wanted was to upload to main

---
## [begonia-crdroid/android_kernel_xiaomi_begonia](https://github.com/begonia-crdroid/android_kernel_xiaomi_begonia)@[5a2c4093dd...](https://github.com/begonia-crdroid/android_kernel_xiaomi_begonia/commit/5a2c4093dd6b3343863654d0a42022da51e5ffd8)
#### Wednesday 2022-07-27 10:06:19 by George Spelvin

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
Signed-off-by: Forenche <prahul2003@gmail.com>
Signed-off-by: 7Soldier <reg.fm4@gmail.com>

---
## [BearerPipelineTest/EasyAdminBundle](https://github.com/BearerPipelineTest/EasyAdminBundle)@[919545baeb...](https://github.com/BearerPipelineTest/EasyAdminBundle/commit/919545baebcf0b7ae1f8a35210afc4bd92769161)
#### Wednesday 2022-07-27 10:29:48 by Javier Eguiluz

feature #5066 Allow `Translatable` objects in addition to `string` in translated context (Lustmored)

This PR was squashed before being merged into the 4.x branch.

Discussion
----------

Allow `Translatable` objects in addition to `string` in translated context

This PR is pretty massive, yet almost all of it's code changes are just enablers for features that are already in Symfony Forms (5.4+) and Symfony Translation (also 5.4+). It allows passing `Translatable` objects as labels and other parts.

### Background

Currently my main problem with EasyAdmin is translation extraction. I maintain pretty large project where translation extraction is build into workflow very tightly and using manual extraction is unmaintainable. Fortunately most translations in admin context have no parameters, so I can workaround that by doing:
```
yield TextField::new('name', (string) t('Client name'));
```
But that's just a dirty hack and works only when label needs no parameters to translate properly. This is why I would benefit greatly if EasyAdmin would simply allow those objects internally and I think other users would welcome it too :smiley:

I have tested those changes on real life projects and they worked like a charm :smile:

### Complexity (?)

As stated before most of the changes are just enablers. By just changing some signatures and adding very simple logic whenever EasyAdmin translates content I was able to pass `Translatable` objects to templates and Symfony Forms, where they handle it without any additional work.

### Backwards compatibility

Functional backwards compatibility is kept. By that I mean - if project uses strings in those contexts (or leaves them empty for Easy Admin to fill with default values), no incompatibility arises. Setters accept strings as before and getters will return those strings. Also - everything will be translated, as before.

Unfortunately the same cannot be said about class signatures. Summary of signature changes are as follows:

Final classes with signature changes:

- Config\Action (new, setLabel); only docblocks and deprecation logic
- Config\Menu\*MenuItem (constructors)
- Config\MenuItem (linkTo*, section, subMenu)
- Dto\ActionDto (getLabel, setLabel and private field)
- Dto\CrudDto (getEntityLabelInSingular, setEntityLabelInSingular,getEntityLabelInPlural, setEntityLabelInPlural, setCustomPageTitle, getHelpMessage, setHelpMessage)
- Dto\FieldDto (getLabel, setLabel, getHelp, setHelp)
- Dto\FilterDto (getLabel, setLabel); only docblocks
- Dto\MenuItemDto (getLabel, setLabel)
- Field\*Field (new); only docblocks
- Field\FormField (addPanel, addTab)

Non-final classes with signature changes:

- Config\Crud (setHelp)
- Field\FieldTrait (setLabel, setHelp); setLabel only in docblock

I wouldn't consider signature changes in setters in final classes as BI, but getters are - end user code might expect getter to return `?string`, while this PR changes it to `TranslatableInterface|string|null`. Again - in simple use case, where user is not using `Translatable` objects this assumption will still hold. But libraries, bundles and other code does not have such guarantee.

Also one non-final class and commonly used trait have signature changes in parameter types that will raise errors when inherited.

I don't see any way we can achieve the same without breaking BC, therefore I think this change can only target `5.0`. But I'd love to hear from the others :)

### TODO

- [x] get feedback
- [x] write tests for functional changes (probably just translating part, there is no point in testing getters and setters IMO)
- [x] Add UPGRADE/CHANGELOG entry documenting changes

Commits
-------

7596f24f Allow `Translatable` objects in addition to `string` in translated context

---
## [newstools/2022-express](https://github.com/newstools/2022-express)@[3284406edf...](https://github.com/newstools/2022-express/commit/3284406edf5d9e8361f520b5069292b510b8a1e0)
#### Wednesday 2022-07-27 10:43:35 by Billy Einkamerer

Created Text For URL [www.express.co.uk/celebrity-news/1646412/Rylan-Clark-dating-boyfriend-love-life-divorce-ex-husband-age-latest-news-update]

---
## [wenyihu6/cockroach](https://github.com/wenyihu6/cockroach)@[d7b901d7d2...](https://github.com/wenyihu6/cockroach/commit/d7b901d7d28ceb4900dd60c5c73b2180089a3e3a)
#### Wednesday 2022-07-27 11:55:40 by craig[bot]

Merge #84618 #84674 #85034 #85042

84618: sql: add new index_recommendation column r=maryliag a=maryliag

This commit adds a new column index_recommendations
STRING[] to:
crdb_internal.node_statement_statistics
crdb_internal.cluster_statement_statistics
system.statement_statistics
crdb_internal.statement_statistics

Part of #83782

Release note (sql change): Adding new column index_recommendations
to crdb_internal.node_statement_statistics,
crdb_internal.cluster_statement_statistics, system.statement_statistics
and crdb_internal.statement_statistics

84674: changefeedccl/schemafeed: ignore unwatched column drops  r=jayshrivastava a=jayshrivastava

Closes https://github.com/cockroachdb/cockroach/issues/80982

Release note (enterprise change): Previously, if you dropped
a column with the schema_change_policy 'stop', the changefeed
would stop. Dropping a column with a different policy would
result in previous rows being retransmitted with the
dropped column omitted.

In some cases, a changefeed may target specific columns
(a column family) of a table. In these cases, if a non-target
column is dropped, it does not make sense to stop the changefeed
or retransmit values because the column was not visible to
a consumer sink to begin with.

With this change, dropping an non-target column from a
table will not stop the changefeed when the
schema_change_policy is 'stop'. With any other policy,
dropping a non-target column will not trigger a backfill.

85034: sql: better tracing of apply joins r=yuzefovich a=yuzefovich

**sql: add tracing spans for each iteration of apply join**

This commit creates a separate tracing span for each iteration of apply
join and recursive CTE execution to make the traces easier to digest.

Release note: None

**sql: log DistSQL diagrams when tracing is enabled**

This commit makes it so that we always include all DistSQL diagrams into
the trace. This could be especially helpful when executing apply join
iterations to understand the plan that each iteration gets. This commit
also removes an environment variable that used to control this logging
previously since I don't think anyone has used it in years now that we
have better tools for debugging (like a stmt bundle).

Informs: #https://github.com/cockroachlabs/support/issues/1681.

Release note: None

85042: logictest: remove spec-planning configs r=yuzefovich a=yuzefovich

This commit removes `local-spec-planning`, `fakedist-spec-planning`, and
`5node-spec-planning` logic test configurations since they seem to be
not very useful at the moment. They were introduced to support the new
DistSQL spec factory, but that work has been postponed with no active
development at the moment, so it seems silly to run most of the logic
tests through the configs that are largely duplicate of the other
default ones (because most of the `Construct*` methods are not
implemented in the new factory). Once the active development on the new
factory resumes, it'll be pretty easy to bring them back to life, but at
the moment let's reduce the amount of tests we run without really losing
any test coverage.

Release note: None

Co-authored-by: Marylia Gutierrez <marylia@cockroachlabs.com>
Co-authored-by: Jayant Shrivastava <jayants@cockroachlabs.com>
Co-authored-by: Yahor Yuzefovich <yahor@cockroachlabs.com>

---
## [TejaX-Alaghari/llvm](https://github.com/TejaX-Alaghari/llvm)@[7c51f02eff...](https://github.com/TejaX-Alaghari/llvm/commit/7c51f02effdbd0d5e12bfd26f9c3b2ab5687c93f)
#### Wednesday 2022-07-27 12:00:46 by Matheus Izvekov

[clang] Implement ElaboratedType sugaring for types written bare

Without this patch, clang will not wrap in an ElaboratedType node types written
without a keyword and nested name qualifier, which goes against the intent that
we should produce an AST which retains enough details to recover how things are
written.

The lack of this sugar is incompatible with the intent of the type printer
default policy, which is to print types as written, but to fall back and print
them fully qualified when they are desugared.

An ElaboratedTypeLoc without keyword / NNS uses no storage by itself, but still
requires pointer alignment due to pre-existing bug in the TypeLoc buffer
handling.

---

Troubleshooting list to deal with any breakage seen with this patch:

1) The most likely effect one would see by this patch is a change in how
   a type is printed. The type printer will, by design and default,
   print types as written. There are customization options there, but
   not that many, and they mainly apply to how to print a type that we
   somehow failed to track how it was written. This patch fixes a
   problem where we failed to distinguish between a type
   that was written without any elaborated-type qualifiers,
   such as a 'struct'/'class' tags and name spacifiers such as 'std::',
   and one that has been stripped of any 'metadata' that identifies such,
   the so called canonical types.
   Example:
   ```
   namespace foo {
     struct A {};
     A a;
   };
   ```
   If one were to print the type of `foo::a`, prior to this patch, this
   would result in `foo::A`. This is how the type printer would have,
   by default, printed the canonical type of A as well.
   As soon as you add any name qualifiers to A, the type printer would
   suddenly start accurately printing the type as written. This patch
   will make it print it accurately even when written without
   qualifiers, so we will just print `A` for the initial example, as
   the user did not really write that `foo::` namespace qualifier.

2) This patch could expose a bug in some AST matcher. Matching types
   is harder to get right when there is sugar involved. For example,
   if you want to match a type against being a pointer to some type A,
   then you have to account for getting a type that is sugar for a
   pointer to A, or being a pointer to sugar to A, or both! Usually
   you would get the second part wrong, and this would work for a
   very simple test where you don't use any name qualifiers, but
   you would discover is broken when you do. The usual fix is to
   either use the matcher which strips sugar, which is annoying
   to use as for example if you match an N level pointer, you have
   to put N+1 such matchers in there, beginning to end and between
   all those levels. But in a lot of cases, if the property you want
   to match is present in the canonical type, it's easier and faster
   to just match on that... This goes with what is said in 1), if
   you want to match against the name of a type, and you want
   the name string to be something stable, perhaps matching on
   the name of the canonical type is the better choice.

3) This patch could exposed a bug in how you get the source range of some
   TypeLoc. For some reason, a lot of code is using getLocalSourceRange(),
   which only looks at the given TypeLoc node. This patch introduces a new,
   and more common TypeLoc node which contains no source locations on itself.
   This is not an inovation here, and some other, more rare TypeLoc nodes could
   also have this property, but if you use getLocalSourceRange on them, it's not
   going to return any valid locations, because it doesn't have any. The right fix
   here is to always use getSourceRange() or getBeginLoc/getEndLoc which will dive
   into the inner TypeLoc to get the source range if it doesn't find it on the
   top level one. You can use getLocalSourceRange if you are really into
   micro-optimizations and you have some outside knowledge that the TypeLocs you are
   dealing with will always include some source location.

4) Exposed a bug somewhere in the use of the normal clang type class API, where you
   have some type, you want to see if that type is some particular kind, you try a
   `dyn_cast` such as `dyn_cast<TypedefType>` and that fails because now you have an
   ElaboratedType which has a TypeDefType inside of it, which is what you wanted to match.
   Again, like 2), this would usually have been tested poorly with some simple tests with
   no qualifications, and would have been broken had there been any other kind of type sugar,
   be it an ElaboratedType or a TemplateSpecializationType or a SubstTemplateParmType.
   The usual fix here is to use `getAs` instead of `dyn_cast`, which will look deeper
   into the type. Or use `getAsAdjusted` when dealing with TypeLocs.
   For some reason the API is inconsistent there and on TypeLocs getAs behaves like a dyn_cast.

5) It could be a bug in this patch perhaps.

Let me know if you need any help!

Signed-off-by: Matheus Izvekov <mizvekov@gmail.com>

Differential Revision: https://reviews.llvm.org/D112374

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[d758ea80b2...](https://github.com/mrakgr/The-Spiral-Language/commit/d758ea80b265cc15b9c340af4c8f95f0aabaf534)
#### Wednesday 2022-07-27 13:29:50 by Marko Grdinić

"8:10am. I am up early. Yesterday I finally got registered for AWS, so I know what I will be doing today. Well, instead of playing with it, I really should contact TensTorrent and ask them about their chips first. I'll go through my interesting company list over the next week like that. This is what I want to do.

Neurolabs: 6pm – 6:45pm, Wed Jul 27, 2022
AssemblyAI: 20:30 - 20:45, Wednesday, July 27, 2022

Today at 6pm and 8:30pm, I have interviews, so I won't put in a full workday. After that I'll only have Generally Intelligent at 9:30pm tomorrwo. I am annoyed at Kalepa for being so rude with their interview process. The HR drone spammed my inbox 5 times like a retard, only to reject me between the stages without an explanation. I really have expected that since we got this far, the coding test would be next.

In hindsight, the way the HR girl just repeat-sent the acceptance email like a robot should have been a red flag. During the interview the HR drone not knowing I autopassed the first HR exam is a red flag as well. Having the pipeline loaded with behavioral tests is a red flag as well.

8:20am. Right now, what I want to do is chill and then I'll check out TensTorrent after that. Outside I am hearing a rumble of thunder, but it is in the distance.

8:25am. Mh, it is coming closer. Let me turn off.

9:45am. It has finally passed. The storm was ferocious.

9:50am. I need to chill. Yesterday it feels like I made a huge accomplishment just opening the AWS account. Let me check out TensTorrent.

https://tenstorrent.com/
> We are building a small DevCloud to let anybody try out their models on Tenstorrent AI computers. Inference works now, training is coming soon. To start, contact us, we’ll get you time and the keys to log in. A more general interface is coming soon. Our initial machines have 4-8 Greyskull AI computers and dual socket AMD servers. Later in the year, we’ll build bigger and bigger machines. By the end of the year, we’ll have our first big beast online. Stay tuned for details.

I want to try emailing them.

I'll say I work a Google just to be safe.

///

I am a ML research engineer that has PL skills and my own open source functional programming language. I'd like to try making a backend for your own device. The benefit of that will be that you'll go from programming in C to a high level PL with ref counting. If that interests you get back to me.

Personally, I am really curious how programming a device with no global, shared memory would look like. I am less interested in running ML models, and am more into writing simulators. I also want to try writing a genetic programming system, which requires creating an interpreter and an AST mutator. For this kind of task you'd definitely want a functional PL with automatic memory management. With CPU+GPU there would be huge churn when transfering data between the two, so I want to investigate whether having it all on a single device would make the ideal viable. I feel that the current way of trying to come up with an idea, testing it and writing a paper about it is ridiculous, and having a system that automates it is the way to go, but this workflow is not at all viable on GPUs.

///

This should be good. Last year, I just didn't have the heart for this since I lost my path, but now I just want to cultivate regardless of the path. That is the way to go.

Now that I've taken a step back, I can treat this less as part of a sci fi story. I can see that I do not need to own that AI chip. I mean what am I going to do with it.

10:15am. With that out of the way, let me finish my chilling and then I'll play with AWS.

10:45am. Had to take a break and do some chores. Anyway, let me finally start. I spent the last week or so doing what? Messing with ASP.NET and being bored out of my skull. Real learning happens when you have a goal that you need to accomplish.

As a programmer you never know 99.99% of the tech, frameworks and libraries out there anyway. Trying to study this in anticipation of something is a waste of time. Fundamentals are the only thing that matters, and Blazor is certainly not a fundamental.

Cloud itself might be a fundamental, so for that reason it is worth studying. Let me aim for a AWS Lambda hello world.

As an aside, looking at the HN yesterday's HN thread, it is amazing how poor of a reputation Google has. A decade down the road it is going to be the new IBM. It is only a matter of time until its scummy behavior gets back to it.

A good reputation is a shield. Once the reputation gets low enough, it serves as an invitation for the regulators to bully it.

10:50am. I do not need to think about that. AWS hello world. Let me get back to it.

11am. I remember, I started off the journey with cloud tutorials after finishing the C backend. The AWS site is still as confusing as ever.

https://aws.amazon.com/getting-started/deep-dive-serverless/?pg=gs&sec=dd

It is not where I saw it last, but here is the serverless hello world.

> c.  Runtime: Currently, you can author your Lambda function code in Java, Node.js, C#, Go or Python. For this tutorial, leave this on Python 2.7 as the runtime.

There is C# and Java there? Interesting. Since the tutorial was made, Python 2.7 has been dropped in favor of 3.7.

11:10am. As an aside, since I am in Croatia, should I be using the Milan or the Frankfurt region? I went with Frankfurt.

...Oh, Milan is way closer (10 vs 6 hours). I should have gone with Milan. Nevermind that for now.

https://dev.to/l1x/why-i-chose-f-for-our-aws-lambda-project-4978

I'll want to look into how I can use F# in AWS.

I suppose now that I have a C backend, I could have Spiral generate the necessary C code.

```rust
use lambda::handler_fn;
use serde_json::Value;

type Error = Box<dyn std::error::Error + Send + Sync + 'static>;

#[tokio::main]
async fn main() -> Result<(), Error> {
    let func = handler_fn(func);
    lambda::run(func).await?;
    Ok(())
}

async fn func(event: Value) -> Result<Value, Error> {
    Ok(event)
}
```

I think I get most of this despite not knowing Rust. Even so, it is complicated.

11:20am. > I think Fsharp is exactly in the sweet spot of programming languages, good enough performance, nice enough features, and a ton of great libraries. It does not have the problem that Python suffers, you can create a single zip that will work on all platforms. It also free from exposing the low-level details that I do not want to care about in business domain code, what Rust does.

Nevermind F# for now. Let me just check out the comments. This guy really like F# vs Python. My man.

F# really is the best language in the world in my view. It is not going to be run on AI chips though.

11:50am. Had breakfast. Let me resume.

Today, just playing around is fine.

12pm. Creating a test event for the function is really very simple.

I meant to do something else, but how do I do the hello world for AWS in F#? Let me delete the function first.

> A runtime is a version of a programming language or framework that you can use to write Lambda functions. Lambda supports runtime versions for Node.js, Python, Ruby, Go, Java, C# (.NET Core), and PowerShell (.NET Core)
> To use other languages in Lambda, you can create your own runtime.
> Note that the console code editor supports only Node.js, Python, and Ruby. If you choose a compiled language, such as Java or C#, you edit and compile your code in your preferred SDE and upload a deployment package to the function.

Hmmm...

When I author a function from scratch, it just asks me for a runtime, not the language. Interesting.

> The code editor does not support the .NET 6 (C#/PowerShell) runtime.

Ok, but it is still weird that it does not even give me a basic text editor here.

https://aws.amazon.com/blogs/developer/f-tooling-support-for-aws-lambda/

Hmmm, will I be writing AWS Lambda functions in VS?

> Next, we get a dialog box in which you select a blueprint of code to get started with your F# Lambda function. One of the most interesting blueprints released with the F# update is for running a Giraffe web application. Giraffe describes itself on its website as “a functional ASP.NET Core micro web framework for building rich web applications.” Because it’s built on top of ASP.NET Core, the same Amazon.Lambda.AspNetCoreServer NuGet package that we released to run ASP.NET Core applications on Lambda works for running Giraffe web applications on Lambda. Let’s select the Giraffe blueprint, then click Finish.

Let me try that out. I never realized there is a Giraffe blueprint.

Ah, maybe I need to select the blueprint in VS instead of the browser.

12:15pm. Let me try the old VS. I can't find any of the AWS templates. Azure is there, but not AWS. Did the support for it get dropped?

https://aws.amazon.com/blogs/developer/f-tooling-support-for-aws-lambda/

These tutorials are all out of date. This one in particular is from 2018.

https://aws.amazon.com/blogs/developer/aws-announces-a-streamlined-deployment-experience-for-net-applications/

I need some kind of tutorial for how to deal with this.

> To get started in Visual Studio, install the latest version of the AWS Toolkit for Visual Studio from the Visual Studio Marketplace.

Hmmm...

https://marketplace.visualstudio.com/items?itemName=AmazonWebServices.AWSToolkitforVisualStudio2022

Never knew VS had a marketplace.

> The AWS Toolkit provides Visual Studio project templates that you can use as starting points for AWS console and web applications. As your application runs, you can use the AWS Explorer to view the AWS resources used by the application. For example, if your application creates buckets in Amazon S3, you can use AWS Explorer to view those buckets and their contents. If you need to provision AWS resources for your application, you can create them manually using the AWS Explorer or use the CloudFormation templates included with the AWS Toolkit to provision web application environments hosted on Amazon EC2.

This sounds pretty cool, it is exactly what I want.

12:30pm. Heat, I now see the AWS templates. The Giraffe Web App one is there as well.

12:35pm. Now I need to figure out how to log into AWS from VS.

12:50pm. I create an user got the Access ID and the Secret Key. I even exported it to CSV and imported it in VS. But it is failing to login.

I am cursed. It seems the entire day for the past two weeks I've only been managing my accounts.

12:55pm. I need to figure this out.

https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/setup.html

> Region
> (Required) The default AWS Region that you want to associate this profile with.

I do not get this part. I wanted to select Milan while creating an user, but it seems users have global scope. Is that right?

https://github.com/aws/aws-toolkit-vscode/issues/

I am reading issue 761 here.

> I have verified that I can use the named profile without issue from the AWS CLI and within Visual Studio 2019 without issue with the same credential values.

> We currently validate credentials by making an STS.getCallerIdentity call against whatever your default region for the profile is--this should work for all non-GovCloud regions. We haven't done much testing against GovCloud (since we're currently not supporting it) but could you try using that profile in the following CLI call with both a GovCloud and a non-GovCloud region?

Hmmm, forget VS for a bit. Let me take a look at the Amazon CLI.

1:10pm. https://docs.aws.amazon.com/cli/latest/userguide/getting-started-prereqs.html

Right now I am hearing thunder outside. ...I need to run.

2:30pm. I am back. There is still a little in the distance, but has mostly recedeed. Sigh, I hope it won't come back again.

This is such a drag.

https://docs.aws.amazon.com/cli/latest/userguide/getting-started-prereqs.html#getting-started-prereqs-next
> Install the latest release of the AWS CLI version 2 on your computer.

Let me do this step.

https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

These interviews are really killing me inside. Having a job and a schedule would be one thing, but these irregular meetings are getting on my nerves. I'll have to just get used to them.

```
C:\> aws --version
aws-cli/2.4.5 Python/3.8.8 Windows/10 exe/AMD64 prompt/off
```

Oh, I got it.

https://docs.aws.amazon.com/cli/latest/userguide/getting-started-quickstart.html

> For general use, the aws configure command is the fastest way to set up your AWS CLI installation. When you enter this command, the AWS CLI prompts you for four pieces of information:

2:40pm. I think it is configured, but how do I check whether it works?

https://bobbyhadz.com/blog/aws-cli-validate-credentials

> To validate a user's credentials with the AWS CLI, run the `sts get-caller-identity` command. The command returns details about the user's credentials if they are valid, otherwise it throws an error.

```
(base) PS C:\Users\Marko> aws sts get-caller-identity

An error occurred (InvalidClientTokenId) when calling the GetCallerIdentity operation: The security token included in the request is invalid.
```

2:40pm. Nope. This is really strange. I am sure that my id and key are right since I pasted them straight from the CSV file.

2:45pm. There is even a console login key, but that one is asking me for a password in addition to the user name. I do not have a password for the account. I was literally never asked to make one. How bizzare.

https://stackoverflow.com/questions/34582318/how-can-i-resolve-the-error-the-security-token-included-in-the-request-is-inval

> It seems that my ~/.aws/credentials file had an additional value: aws_session_token which was causing the error. After deleting and re-creating the ~/.aws/configure using the command aws configure, there is now only values for aws_access_key_id and aws_secret_access_key.

Let me give this a try.

2:50pm. It worked! Let me try VS again.

///

(base) PS C:\Users\Marko> aws sts get-caller-identity

An error occurred (InvalidClientTokenId) when calling the GetCallerIdentity operation: The security token included in the request is invalid.

///

It fails in the IDE. And once that happens, it adds some stuff into the config file and the login fails for me in the CLI as well.

With this I've isolated the error. I'll have to open an issue on the AWS Tools repo.

2:55pm. Wait, wait, wait...this is for VS Code. I am about to open an issue on the wrong repo.

3:10pm.

///

When I try to login, I get the `Unable to connect to AWS: The security token included in the request is invalid` error. I did some snooping and I figure out where the break occurs.

I tried installing AWS CLI for Window. Running `aws configure` I saw that the ID and Secret Key are already input by the Visual Studio.

Then I tried running the...

```
(base) PS C:\Users\Marko> aws sts get-caller-identity

An error occurred (InvalidClientTokenId) when calling the GetCallerIdentity operation: The security token included in the request is invalid.
```

This was very strange as I was copy pasting them directly from the .csv file so I was sure they weren't wrong.

I erased the files in the `c:\Users\Marko\.aws\config` folder, ran `aws configure`, pasted the values. When I ran `aws sts get-caller-identity` I got the correct return signifying the the verification works.

What is happening is that the AWS Toolkit for VS is adding the following fields to the configuration file.

```
toolkit_artifact_guid=1d81c44d-bc10-4f24-a08f-81583d885967
region=eu-south-1
```

///

Let me back this up here.

The problem is that damn region. Without the region it works, but with it, it does not!

What am I supposed to do about this?

///

Selecting a region for my user account causes login issues using both the AWS CLI and the Toolkit for VS. If I put in `aws sts get-caller-identity` without the region information in the `.aws/credentials` file, I get the correct return, but if I try putting in a region, then the verification fails. This is a problem as AWS Toolkit for VS wants a region and inserts it automatically into the credentials file.

I am new to AWS, and nowhere do I see the option to select a region for the user I created using the IAM Management Console. How do I select a region for the user I've created?

I know there is an option next to my profile for region selection, but it is set to `Global` and I can't select any of the specific regions.

///

I'll try asking this question, but let me Google it first.

```
(base) PS C:\Users\Marko> aws configure get region
eu-central-1
(base) PS C:\Users\Marko> aws sts get-caller-identity
{
    <it works>
}
```

Fuck. It seems the Milan region is not accepted for some reason. `eu-central-1` is the Frankfurt one. This was super annoying.

3:25pm. I am going to have to shut everything down again due to weather. Let me just try logging in.

Yes, now it works!

That is one problem down. Let me commit."

---
## [Eltrick/SimonSwindles](https://github.com/Eltrick/SimonSwindles)@[14a4833e75...](https://github.com/Eltrick/SimonSwindles/commit/14a4833e75ed071af239efec313640cf0e75a503)
#### Wednesday 2022-07-27 13:33:13 by Lucifer Voeltner

Version 1.5.2 - Fix the funny Yellow Constant_Modification function since Bagels fucked up lmao!!!!!!!!!!!!!!!!!!!!!!

Please help I want to kill him so badly because I spent 8 HOURS trying to figure out why the thing wouldn't work. j

---
## [FlacoFF/FIJ_Foundation-19](https://github.com/FlacoFF/FIJ_Foundation-19)@[3198c7d257...](https://github.com/FlacoFF/FIJ_Foundation-19/commit/3198c7d257961f97b45ae128cdc72b657a2ed36e)
#### Wednesday 2022-07-27 14:10:46 by ivanmixo

Fixes MTF heli runtime (#547)

* Fixes mtf heli

* Fuck you die

* Whoops funny haha

* Cheeky juke fix

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[0841bcac41...](https://github.com/mrakgr/The-Spiral-Language/commit/0841bcac4121c9495d06a6d27f761e3923bd1036)
#### Wednesday 2022-07-27 15:05:20 by Marko Grdinić

"4:30pm. The bad weather spent itself mostly. What a shitty day today is. At least the temps are cool.

Let me check mail. Nothing. Good.

4:35pm. > This project shows how to run a [Giraffe](https://github.com/giraffe-fsharp/Giraffe) project as an AWS Lambda exposed through Amazon API Gateway. The NuGet package [Amazon.Lambda.AspNetCoreServer](https://www.nuget.org/packages/Amazon.Lambda.AspNetCoreServer) contains a Lambda function that is used to translate requests from API Gateway into the ASP.NET Core framework and then the responses from ASP.NET Core back to API Gateway.

I really don't feel like starting anything now. Let me just peek at the source and maybe I'll close here for the day earlier. I knwo that my schedule is till 6pm, but I have those two interviews later in the day.

The example is nice, but I am wondering whether I am getting lost.

4:50pm.

```fs
let indexHandler  =
    fun (next : HttpFunc) (ctx : HttpContext) ->

        text "Serverless Giraffe Web API" next ctx

let arrayExampleHandler (itemCount:int) =
    fun (next : HttpFunc) (ctx : HttpContext) ->
        let values = seq { for a in 1 .. itemCount do yield sprintf "value%i" a }
        text (String.concat ", " values) next ctx

let webApp:HttpHandler =
    choose [
        GET >=>
            choose [
                route "/" >=> indexHandler
                route "/array" >=> arrayExampleHandler 2
                routef "/array/%i" arrayExampleHandler
            ]
        setStatusCode 404 >=> text "Not Found" ]
```

This is a simple enough web app.

4:50pm. Ok, forget anything else. What my next goal should be is to just deploy it on AWS and somehow access it. Through my browser or something else. I am not sure. AWS will no doubt have something to test web apps.

After a huge amount of effort, I've finally managed to put my bank accounts in order and registered for AWS. Now I've even created a user and managed to get it to accept my credentials through the AWS Toolkit for VS. It was 100x harder than it should have been.

What I need to do next is figure out how to deploy my applications on AWS. Once I have that, I can consider myself 2/5 in the cloud domain. Once I do that, I'll look into distributed ML training on AWS. What I really want to play with are TensTorrent's chips though. Distributed ML is just to tide me over until I get a job.

If I can get some positive interest from TensTorrent for a Spiral backend, I might be able to angle towards getting a job at their place as well.

5pm. Anyway, I am done for the day here. Let me watch Luminous Witches and mentally get ready for the interview. Hopefully after these two, I'll have gotten used to it.

5:05pm. I think it is a mistake to take these interviews too seriously. Jobs are one thing, but interviews I should treat as a vacation. If I can do that, I can consider myself an experience job hunter."

---
## [hal9000PR/Paradise](https://github.com/hal9000PR/Paradise)@[fd5580307e...](https://github.com/hal9000PR/Paradise/commit/fd5580307e1d3a2821ae8b2f26cb04cdcd139f87)
#### Wednesday 2022-07-27 15:16:15 by Contrabang

Adds a blue overlay to scrying orb users. Spirit realm and scrying orb users now have a special description instead of being catatonic (#18366)

* holy shit blue ghosts

* lets fix that

* you cant see it if its not in ya hand

* Their glowing red eyes are glazed over

* farie review

* farie review pt 2

---
## [Xisifer/SWLOR_Haks](https://github.com/Xisifer/SWLOR_Haks)@[6ffa92d6cc...](https://github.com/Xisifer/SWLOR_Haks/commit/6ffa92d6cc5883cce0bc077245f3f7d5a9f1a75f)
#### Wednesday 2022-07-27 15:39:34 by Scott Finlay

Patch for Head Pack 4 (#146)

- Re-added overwritten head 54, now as Head 100. Over-wrote ugly old NWN head that nobody used because I didn't want to fuck with IDs

- Adjusted scaling on Male Hum/Mir/Chi/Ech 50 & 51

---
## [TDKorn/insta-tweet](https://github.com/TDKorn/insta-tweet)@[159d0292ee...](https://github.com/TDKorn/insta-tweet/commit/159d0292eeeb41196c25aff3b6b6e4bb5d48fe60)
#### Wednesday 2022-07-27 16:53:30 by TDKorn

Linkcode but functional

wow that took so long i could actually scream
* Am I the only one using this extension or something?
    - there's literally no info I adapted this from another repo...  (tysm @nlgranger I would, in fact, die for you)

---

sphinx.ext.linkcode -> the fix (for future me 🧠🔨) :

* Issue was that package named "InstaTweet" and root directory named "insta-tweet" somehow just obliterates it
* But also maybe something to do with pkg_resource? Saying my shit doesn't exist like PLS
* Anyways, changed modpath to be a constant -> "insta-tweet" rather than a variable that's always assigned something that doesn't work 💓💋
* This then made the github links like
"https://github.com/tdkorn/insta-tweet/blob/../../docs/InstaTweet/profile.py" which was super cool love it but i wanted it functional unfortunately 😪
* Removed sys.path stuff?????? Which I just am so excited to see how that turns out when I push to RTD

---
## [vrousk/vrousk](https://github.com/vrousk/vrousk)@[9c8c1dd4cc...](https://github.com/vrousk/vrousk/commit/9c8c1dd4cc3af08c750eb82dc479525ad532988c)
#### Wednesday 2022-07-27 16:55:45 by vrousk

Who's vino?

Name : vino 
Nickname : vin, ino, niv
Birthday : december 27 2004 
Age : 17 
Status : Currently a suitor 
Gender : Boy 
Pronouns : Hes/Him

Likes : 
- music
- iced coffee
- sunset, sunrise, and moon
- cats and dogs
- chocolates
- his own girl

Dis likes : 
- rats
- crowded places, and people 
- dead
- bloods 
- ketchup
- his mom

---
## [smxi/inxi](https://github.com/smxi/inxi)@[ff81310652...](https://github.com/smxi/inxi/commit/ff81310652eef4cc3cb6d3dce300aa6f21da9ead)
#### Wednesday 2022-07-27 19:03:02 by Harald Hope

A good bug fix, and several very good indentation fixes that had always been
around, and some of them known. More fine tuning of CPU process/built data. Bit
by bit it's getting filled out.

Thanks again mrmazda for all the suggestions and watchful eyes.

--------------------------------------------------------------------------------
KNOWN ISSUES:

1. CPU built, process are not perfect and complete and always right. Like life,
it's not perfect, but it is ok. Help complete the feature if it bothers you.

2. Intel Raptor Lake and related APUs are trickling out, but I have not found
cpuid data for the cpu, or generation data for the apu. Was hoping to squeeze
that into 3.3.20, but looks like it will have to go into 3.3.21 or later.

--------------------------------------------------------------------------------
BUGS:

1. MrMazda pointed this out, the printer was not correctly indenting long values
in specific cases, not adding indentation level 1 when the key: value pair was
not the last item on the logical line. Subtle, but could hit Device, OpenGL, and
a few other cases.

2. When SMT is disabled, cpu speed from /sys can return <unknown>, which is a
string, not the numeric value inxi expected. This trips multipe errors when
speed cleaner is used. Thanks issue #273 reporter iamc for this one. My guess is
all during all cpu testing, none of us thought to disable smt to see what would
happen.

--------------------------------------------------------------------------------
FIXES:

1. On disk vendors, Initio isn't a vendor, it's either a misconfigured ide hdd,
slave/master wrong, or bad usb controller. Initio is a default controller, not a
vendor. Added pre-filter in disk_vendor() to remove that string if it appears.

2. Going along with bug 1, finally fixed long standing weakness with long value
wrapping, now continues to build line until it's done, and does not force a new
line after the last long value item.

3. Another glitch where last key: value pair was less than working width, but
total width was greater, was not wrapping correctly.

4. Saw a corner case Intel Core name: Core i7-1165G7 which did not use the
expected intel (core number)(3 digits), modified to look for 3 digits after core
numer OR 2 digits + letter + digit.

5. Added 'tar' installed test for debugger, found cases in actual distros that
shipped without it in their minimal installs. Times sure have changed!

6. Another Centos type change, amazingly, this was shipped without lspci as
well! No idea what went into the install ISO if this stuff didn't include the
most elementary Linux tools. Added lspci missing error if linux and not risc and
no pci_tool detected. I have to admit this is really surprising to me, I mean, I
thought the entire purpose of the rhel family was to provide enterprise
solutions, but to leave out such elementary tools required by every sys admin is
very difficult to understand. This was centos 7.5. I believe Alma and Rocky 9
minimal have those basic tools, so that's an improvement, though they didn't
have tar.

7. Added a '-' between gen and gen number for Intel GPU generation output. Even
though it's documented as for example gen9.5, it looks odd to see it that way,
it's easier to read it as gen-9.5 I think.

8. Did same for AMD arch/codes, for numbered arch/codes like Rage 9, easier to
read as Rage-9.

9. Extreme corner case spotted by mrmazda, if KDE is started by TDE, inxi showed
Trinity, not KDE-Plasma as the desktop. Further, it failed to show Trinity
version, maybe because Trinity was not installed?

--------------------------------------------------------------------------------
ENHANCEMENTS:

1a. More or less completed verification of AMD cpu microarch/built/process, and
added more accurate fallback cases for stray model IDs.
* family 5h: K5, K6
* family 6h: K7
* family 7h: K8 - mostly done, needs some checks.
* family 10h: K10
* family 11h: K11 Turion X2. Note there is some uncertainy about this family
name. Built years n/a yet. Mix of K8/K10
* family 12h: K12 Fusion, K10 based, first APU type?

1b. Extended Intel cpu data a bit more as well. Thanks linuxdaddy from slackware
for the research help there.
* family 4: mostly new, fine tuned, granular
* family 5: more granular, better date/process info.
* family 6: built dates added
* family F: corrected some overly specific stuff

2. Tentative support for finit init system (fast init). Runs in /proc/1/comm,
uses initctl, which may have been revived from its upstart days, not sure. Added
potential support for nosh, linux only, don't know how to detect other bsd init
system.

3. Added amd/intel gpu product IDs.

4. Added shortcut --filter-all/--za, activates all filters: -z, --zl, --zu,
--zv. Why not?

5. Added support for dm types kdmctl and xdmctl, opensuse and maybe redhat use
the latter to start the actual dm running the desktop/wm. You want to see that
because you need to do systemctl restart xdm to restart the actual dm. Thanks
mrmazda for pointing out this one.

6. Added AlmaLinux, RockyLinux, CentosStream to system base (RHEL derived).

7. Basic Raptor Lake gpu/apu support added, with patterns to detect since few
product ids yet. Same applies to Arctic and Alchemist, which still have no
product IDs.

8. More disk vendors and disk vendor ids, never stops - the waters flow on, the
rain falls, then the sun comes out. Until one day it doesn't.

--------------------------------------------------------------------------------
CHANGES:

1. Deprecated --gpu, now it works the same as -Ga, that was too granular and
nobody would use it I think. Now that the new gpu features are solid, no need
for this special feature.

--------------------------------------------------------------------------------
DOCUMENTATION:

1. Updated docs/inxi-values.txt, it didn't have all the --debug-xxx options
listed.

2. Split out some BSD data into docs/inxi-bsd.txt.

3. Big update on docs/inxi-init.txt, moved data to it from other files, updated
the init/service tool data.

4. Renamed init-data.txt to inxi-init.txt, renamed cpu-flags to
inxi-cpu-flags.txt to be more consistent.

5. Updated help, man for new --filter-all option.

6. Updated help and man for --gpu deprecation.

--------------------------------------------------------------------------------
CODE:

1. Moved required perl modules and system programs checks to
check_required_items() in debugger, why not? Also added an error handler for
missing required programs, this is really the only one, and only for
--debug >= 20
This is the only required program test inxi has in it I believe, really amazing
that such a core tool would be left out of an OS today.

2. Removed this redundant block of code from Network device_output() end
section, that repeated in the main get() so didn't seem to serve any purpose.
The test in get() is if n!@rows and if !%risc, same as here, so can't see any
use for it. I'm leaving this here in case that did have some use, but I don't
see it.

if (!@$rows && !%risc){
	my $key = 'Message';
	my $type = 'pci-card-data';
	if ($pci_tool && $alerts{$pci_tool}->{'action'} eq 'permissions'){
		$type = 'pci-card-data-root';
	}
	@$rows = ({
	main::key($num++,0,1,$key) => main::message($type,'')
	});
}

---
## [IndieanaJones/tgstation](https://github.com/IndieanaJones/tgstation)@[707fbfac7e...](https://github.com/IndieanaJones/tgstation/commit/707fbfac7e11837865d70587011aa8197b1d0c35)
#### Wednesday 2022-07-27 20:40:55 by san7890

[MDB Ignore] Shifts all (sane) varedited signs to directionals  (#68004)

* [MDB Ignore] Shifts all (sane) varedited signs to directionals

Hey there,

So we have these cool new sign directionals now, but we still have all of the old pixel-shifted pre-fabrications lying around. So, I added an UpdatePaths (as well as Updated the Paths) to be a bit better at using directionals, because directionals are pretty neato.

This should update every single var_edit that used the proper 32 pixelshift (some of them used 28, and I'm unable to account for that automatically with current tooling) into a proper subtype. Mappers tend to learn by looking at well established maps, so it's always important to ensure that the well-established maps use the most recent tooling (i.e.: bring them up to the surface) and avoid needless excess lines in maps.

* The Commit With All The Maps

OH GOD OH FUCK

* Renames the UpdatePaths

---
## [uber/cadence](https://github.com/uber/cadence)@[add4b390ad...](https://github.com/uber/cadence/commit/add4b390ada43fdd8167f06e209ae6ece0d11aaa)
#### Wednesday 2022-07-27 20:54:23 by Steven L

Standardizing cancellation behavior: a canceled workflow never starts a new run (#4898)

# Summary for busy people

Workflow cancellation was kinda weird and confusing, and left some awful, unrecoverable, and un-*preventable* edge cases (particularly with child workflows).  It also left users with no way to reliably stop work, aside from termination.  Termination is inherently "unclean" and risky, so it should not be required to achieve something outside exceptional circumstances where recovery is not possible.

This commit changes that: cancellation is now "sticky", and a canceled workflow does not ever trigger a new run after it completes, regardless of how it completes, so it can be used as a reliable "stop processing after cleanup" tool.  The final state of a canceled workflow's run is now *always* a successful completion with a value, canceled, or timed out. (termination remains always "terminated")  
A canceled workflow can still start and abandon child workflows, so all current behavior with retries / continue as new / etc can be replicated with child workflows if desired.

A fair bit of (not very complex) additional work here and in nearly all other repos is required to truly complete this, but it is *functional* and non-optional with this commit alone.  
In particular, adding a dynamic config to (temporarily!) restore old behavior should be fairly easy if it proves to be needed.

# More details and motivation

Part 1 of [many, tbd, in multiple repos] involved in changing workflow cancellation to reliably end workflows.
Tests will be coming soon, for now I'm using a fairly simple set of workflows and checking the resulting histories exhaustively by hand.

The primary motivation for these changes is to address some impossible-to-recover-from scenarios when canceling child workflows.  After further exploration and discussion we've realized that, without these changes, there is *no reliable way* to stop a sequence of workflows without relying on termination, which we consistently treat as a fallback / impure-but-necessary ultimate hammer.

Workflows should not *need* to rely on termination to achieve a desired behavior.  With these changes, cancellation becomes capable of *guaranteeing* that workflows end within some finite time, which is a unique ability and makes it much more consistent and reliable.  
Turning this into a "complete" change will require quite a few tests, documentation changes, client-side changes (to allow recording more info, and likely changing test suites), and some smallish database and maybe RPC changes (to hold/return more data in cancellation errors).

We are also not currently planning on making this configurable.  It's seen as a correction of an under-specified and somewhat flawed chunk of behavior, more than "a change".  
Existing workflows will not experience replay errors, but it is still a substantial *semantic* change, though from what we have seen cancellation is relatively rarely used (partly due to its complex behavior).  If issues are encountered / if users end up needing it, it should be fairly easy to add a per-domain/tasklist/workflow type configuration value, but it will be opt-*out*, not opt-*in*.

# What was happening

Previously, workflow behavior on cancellation was pretty frequently surprising to our users, arguably inconsistent, and not very well documented:

| **PREVIOUS**  | **simple**               | **retry**                                 | **cron**                                | **retry+cron**                                    |
|--------------:|--------------------------|-------------------------------------------|-----------------------------------------|---------------------------------------------------|
| **success**   | success                  | success                                   | success<br>continue cron<br>cron        | success<br>continue cron<br>cron<br>retry         |
| **cancel**    | canceled                 | canceled                                  | canceled                                | canceled                                          |
| **retryable** | (n/a, fatal)             | continue retry<br>retry<br>recorded error | (n/a, fatal)                            | continue retry<br>cron<br>retry<br>recorded error |
| **fatal**     | failed<br>recorded error | failed<br>recorded error                  | continue cron<br>cron<br>recorded error | continue cron<br>cron<br>retry<br>recorded error  |
| **continue**  | continue immediately     | continue immediately<br>retry             | continue immediately                    | continue immediately<br>retry                     |
| **timeout**   | timeout                  | continue retry<br>retry<br>recorded error | continue cron<br>cron<br>recorded error | continue retry<br>cron<br>retry<br>recorded error |

A legend is:
- success / etc shows the final state of the canceled run (success = completed with a value that can be retrieved)
- "continue X" covers what source is used to compute the next run's starting delay (cron, retry, or no delay)
- "cron" / "retry" shows whether or not cron/retry configuration is carried over to the new run
  - note that cron is lost by default with continue-as-new
- and "recorded error" is whether or not the returned error is saved in its entirety (type + reason + details)

This largely summarizes as "cancellation works when you end with the canceled-context error", say from `ctx.Err()`, otherwise it behaves like normal (or nearly) and many scenarios will start a new run.
That's somewhat reasonable, but it's fairly "fragile" (it depends on what you return, and there are *many* ways for code to return some other error), and most importantly it means *there is no reliable way to stop a workflow* except to terminate it.

That has severe consequences in at least two scenarios:
1. When termination is *unsafe*
2. When a parent workflow cancels a child by canceling its context

For 1, for manual cancellations it's potentially reasonable to just terminate a run that begins after a successful cancel... but in principle if you're using cancellation it implies that termination is *not* desired, and potentially not safe to do.  Canceling may result in a brand new run that immediately starts new behavior, leaving you with no safe window to terminate and not leave bad state lingering.  
So users wanting a safe way to stop a sequence of workflows have no reliable way to do so.

For 2, it puts parent+child workflows in an extremely awkward, and essentially unrecoverable scenario.  Cancellation is a *one time event*, and as far as the parent is concerned, if the child/its context is canceled, the child is canceled...  
...but if the child then starts a new run for *any* reason (retry, cron, reset, etc), that new run is no longer canceled.  The parent has no way to know this has happened, and has no way to *re*-cancel the new child, so it can easily lead to the collection of workflows getting into an impossible state that it never recovers from.

Both cases are able to lead to unreliable behavior which can only use termination to stop, and for which no "safe" option exists.

After reviewing some customer issues and desires and thinking about things, we've settled on "cancel should guarantee that things stop".  Not necessarily in a timely manner, but that's fine.  And if a workflow wants to run behavior longer or larger than its current run can achieve, it has a workaround: start a new (likely child) workflow to do the cleanup.

# What happens now

So that's what this PR does, in a minimal / to-be-polished way so we can start running it for our stuck users while we flesh out tests and change other behaviors.

Currently that means our cancellation behavior is now:

| **CURRENT**    | **simple**                                | **retry**                                 | **cron**                                  | **retry+cron**                            |
|--------------:|-------------------------------------------|-------------------------------------------|-------------------------------------------|-------------------------------------------|
| **success**   | success                                   | success                                   | success                                   | success                                   |
| **cancel**    | canceled                                  | canceled                                  | canceled                                  | canceled                                  |
| **retryable** | (n/a, fatal)                              | canceled<br>recorded error (details only) | (n/a, fatal)                              | canceled<br>recorded error (details only) |
| **fatal**     | canceled<br>recorded error (details only) | canceled<br>recorded error (details only) | canceled<br>recorded error (details only) | canceled<br>recorded error (details only) |
| **continue**  | canceled<br>(no details)                  | canceled<br>(no details)                  | canceled<br>(no details)                  | canceled<br>(no details)                  |
| **timeout**   | timeout                                   | timeout                                   | timeout                                   | timeout                                   |

And the new "details" entries cover whether or not an error's "details" (the custom encoded data, not reason or type) are saved.  Unfortunately the current cancellation event (and clients' API) does not allow recording all data, or any in some cases, so the original reason/message and error type are lost and are replaced with a canceled error.

Now, cancellation *always* ends workflows with the current run.  Returning a value will return that value, including in cron scenarios, timeouts are still timeouts (and they imply a possibly un-clean termination), and _all_ errors or attempts to continue-as-new will instead result in a canceled state.

# Future changes to make to finish this effort

With further changes to the clients and RPC/storage models, canceled errors will store more details about what was returned.  E.g. continue-as-new does not record what was *attempted* to be started, and other error types lose their "reason" (i.e. the message) and type but not details.  Pretty clearly this is sub-par, and we should be capable of reporting the actual return in full so it can be retrieved if needed.  This is also why returning a value now always ends in a completed state, so successful completions do not lose those values.

Prior to merging into master / a release, we may end up making this configurable (likely with a default of opt-out), to address both the sub-par information recording and the semantically-breaking behavior change.  Docs changes are also due, as well as some integration tests, client library changes (e.g. to make sure the test suite reflects the new behavior), etc.

Another gap to plug is that resetting a workflow does not "forward" the canceled state to the new run.  We should probably be treating cancellation like we do signals: cancel the new run if the current run is canceled.  This will ensure that you can reset a child and retain the parent's cancellation, so it'll very likely become the default behavior, but we'll allow overriding it.  Resets are manual actions, they can break the rules if desired.  And they can just manually cancel later if they decide they do want it.

And last and perhaps least: it's quite strange that continue-as-new does not retain cron config.  At least from the Go client.  I suspect it's just not adding to / pulling from the context correctly.

---
## [niftynei/lightning](https://github.com/niftynei/lightning)@[dd40347b8e...](https://github.com/niftynei/lightning/commit/dd40347b8e6ab930eb8238603ee3e5d871a9839b)
#### Wednesday 2022-07-27 21:36:39 by niftynei

bkpr: add journal entry for offset account balances; report listbalances

When the node starts up, it records missing/updated account balances
to the 'channel' events... which is kinda fucked for wallet + external
events now that i think about it but these are all treated the same
anyway so it's fine.

This is the magic piece that lets your bookkeeping data startup ok on an
already running/established node.

---
## [dod-ccpo/atat-web-api](https://github.com/dod-ccpo/atat-web-api)@[0c1fc430f7...](https://github.com/dod-ccpo/atat-web-api/commit/0c1fc430f73b7b8ee314ab7ea2fddf918b659cae)
#### Wednesday 2022-07-27 21:55:55 by Kyle Laker

Support custom domains for the API Gateway

This adds support for custom domains to the API Gateway. The way that
this is handled requires changes to a few core constructs within the
environment as well as a little bit of gluing AWS resources together.
First, API Gateway does not directly support custom domains on private
endpoints. This requires us to put _something_ in front of it that can
speak HTTPS with a valid certificate for a custom name. This uses a load
balancer. Because of issues experienced during troubleshooting, it was
easier to just add support for _both_ types of Load Balancers and we can
toggle between them in the future as needed.

Now, as for how we implement the Load Balancer's Target Group... that
requires a little more involvement. To start with, ELBv2 only supports a
few types of targets by default: EC2 Instances, IP Addresses, Lambda
Functions, and ALBs. Unfortunately, a VPC Endpoint (which is what we
have with our API Gateway Private Endpoints) isn't any of those things
directly. But it does have an IP address (well... it actually has
several). Unfortunately, no tooling directly exposes the IP addresses
based on VPC Endpoint ID; especially not CloudFormation/CDK.
Fortunately, with Custom Resources, we can glue together several AWS API
calls to describe the endpoint and get its associated Elastic Network
Interfaces (ENIs) and then describe those to get their IP addresses
(because despite ENIs being a lovely abstraction in EC2/AWS, an ELBv2
cannot target them).

Unfortunately, the CDK is very helpful. And by being so helpful, it
provides a lot of abstractions around ELBv2 Target Groups. But this
breaks the ability to just yeet arbitrary JSON into the `Targets`
property of the `AWS::ElasticLoadBalancingV2::TargetGroup` resource. No
matter what you try to do, the CDK either wraps it in a list or very
(not-so) helpfully tries to validate it (which won't work because with
our custom resource, it ends up being a `Fn::GetAtt`). And because it's
an intrinsic function and not actual raw data, we can't treat it like an
object and split it, iterate over it, or any other fun magic (in the
CDK, it's a `Token`). So we have to just treat it as an opaque object.
The only way we can effectively provide that as an opaque object is to
use escape hatches in the CDK to pass it directly to the underlying
CloudFormation resource property. That means that our Custom Resource
has to return a valid JSON object that can be passed to the `Targets`
object.

The configured Load Balancer will then balance across all the IP address
(and hopefully does so somewhat intelligently based on availability zone
since we do provide that data). The HTTPS/TLS certificate from ACM is
attached to the load balancer and that results in the certificate
matching the DNS name.

This does require two changes for consumers of the API:

 1. Consumers must now use the DNS name. The regional endpoint for the
    API is no longer available
 2. Consumers must pass the `x-apigw-api-id` header, as described in the
    [API Gateway docs for invoking via the DNS name][1]

Finally, this should not cause any issues for Developers' sandbox
environments. Those should be able to trivially be built without DNS
names and without VPC connectivity.

This implementation does have a few trade-offs as it closely ties the
usage of a custom domain to the usage of a VPC. For our use case, that
is likely pretty acceptable since any environments where we'd specify a
custom name, we'd also have a VPC. Second, we may need to kick off
something to re-trigger the custom resource at some point in the future
if we for any reason see the underlying IPs change without the VPCE ID
changing (but that is extremely unlikely to happen).

One option that was available that was rejected for now was having the
ALB target a Lambda to handle balancing between the VPC endpoints. This
would have resulted in additional code needing to be executed on _every_
request (so in many cases, doubling our number of Lambda function
invocations) and would have just added another link in the chain of
request/response size limitations that would become somewhat harder to
debug. Not using the Lambda option also allows us to maintain the
ability to use either an NLB or an ALB, whichever is most appropriate.

[1]: https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-private-api-test-invoke-url.html#apigateway-private-api-public-dns

---
## [PonyboyYbr/ddl_postgres](https://github.com/PonyboyYbr/ddl_postgres)@[c40ba5f318...](https://github.com/PonyboyYbr/ddl_postgres/commit/c40ba5f318f96a6a5a29729b987ead11c5dc65c1)
#### Wednesday 2022-07-27 22:01:02 by Tom Lane

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
## [kraj/gcc](https://github.com/kraj/gcc)@[5493ee7145...](https://github.com/kraj/gcc/commit/5493ee7145a05dc32bc6d802da2f8237293012d3)
#### Wednesday 2022-07-27 22:04:00 by Alexandre Oliva

i386 testsuite: cope with --enable-default-pie

Running the testsuite on a toolchain build with --enable-default-pie
had some unexpected fails.  Adjust the tests to tolerate the effects
of this configuration option on x86_64-linux-gnu and i686-linux-gnu.

The cet-sjlj* tests get offsets before the base symbol name with PIC
or PIE.  A single pattern covering both alternatives somehow triggered
two matches rather than the single expected match, thus my narrowing
the '.*' to not skip line breaks, but that was not enough.  Still
puzzled, I separated the patterns into nonpic and !nonpic, and we get
the expected matchcounts this way.

Tests for -mfentry require an mfentry effective target, which excludes
32-bit x86 with PIC or PIE enabled, that's why the patterns that
accept the PIC sym@RELOC annotations only cover x86_64.  mvc7 is
getting regexps extended to cover PIC reloc annotatios and all of the
named variants, and tightened to avoid unexpected '.' matches.

The pr24414 test stores in an unadorned named variable in an old-style
asm statement, to check that such asm statements get an implicit
memory clobber.  Rewriting the asm into a GCC extended asm with the
variable as an output would remove the regression it checks against.
Problem is, the literal reference to the variable is not PIC, so it's
rejected by the elf64 linker with an error, and flagged with a warning
by the elf32 one.  We could presumably make the variable references
PIC-friendly with #ifdefs, but I doubt that's worth the trouble.  I'm
just arranging for the test to be skipped if PIC or PIE are enabled by
default.


for  gcc/testsuite/ChangeLog

	* gcc.target/i386/cet-sjlj-6a.c: Cope with --enable-default-pie.
	* gcc.target/i386/cet-sjlj-6b.c: Likewise.
	* gcc.target/i386/fentryname3.c: Likewise.
	* gcc.target/i386/mvc7.c: Likewise.
	* gcc.target/i386/pr24414.c: Likewise.
	* gcc.target/i386/pr93492-3.c: Likewise.
	* gcc.target/i386/pr93492-5.c: Likewise.
	* gcc.target/i386/pr98482-1.c: Likewise.

---
## [vincentiusvin/tgstation](https://github.com/vincentiusvin/tgstation)@[95ffcd4e19...](https://github.com/vincentiusvin/tgstation/commit/95ffcd4e19304af76653ff2b33084092246e4b16)
#### Wednesday 2022-07-27 22:52:38 by YakumoChen

Moves the FUCKING LIGHT FIXTURES on tiles with surgery beds (#67644)

Moves around some wall objects in surgery rooms on both Meta and Box, primarily so that there aren't light fixtures on the same tiles as surgery beds. I moved a few unrelated things for QOL.

EVERY MOTHER FUCKING TIME I DO SURGERY I ALWAYS SMASH THE FUCKING LIGHT TUBE BY ACCIDENT AND IT PISSES ME THE FUCK OFF. WHY WOULD YOU PUT A THING THERE THAT JUTS OUT OVER THE FUCKING BED AND GETS IN THE WAY OF CLICKING ON THE SPACEMAN SPRITE FUCK GOD DAMN IT.

---
## [Andrew-Rhodes/prework](https://github.com/Andrew-Rhodes/prework)@[6df8797319...](https://github.com/Andrew-Rhodes/prework/commit/6df8797319ff5f9f01b38a285242186d02d27e54)
#### Wednesday 2022-07-27 23:57:24 by Andy Rhodes

Merge pull request #1 from Andrew-Rhodes/PhoneNumberValidation

Go Fuck Yourself

---

