## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-12-22](docs/good-messages/2023/2023-12-22.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,464,557 were push events containing 3,422,297 commit messages that amount to 230,858,212 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 51 messages:


## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[5f504d1de7...](https://github.com/pytorch/pytorch/commit/5f504d1de74a5189f93e65aa9283fc4607b8631c)
#### Friday 2023-12-22 00:00:15 by Pedro Caldeira

Check for boolean values as argument on pow function.  (#114133)

Hello everyone! 😄
Also @lezcano , nice to meet you! :)

Sorry if I miss anything, this is my first time around here. 🙃

This PR basically makes the same behaviour for cuda when using `torch.pow`. Basically Python considers True as 1 and False as 0. I just added this check into `pow` function. From what I understood, when I do `.equal` for `Scalar` that is boolean, I'm sure that types match so that won't cause more trouble.

I know that the issue suggest to disable this case but that could be a little more complicated, in my humble opinion. And that can create some compability problems too, I guess.

My argument is that code below is correct for native language, so I guess it does makes sense sending booleans as Scalar.

```
$ x = True
$ x + x
2
```

This was my first test:
```
Python 3.12.0 | packaged by Anaconda, Inc. | (main, Oct  2 2023, 17:29:18) [GCC 11.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import torch
>>> torch.pow(torch.tensor([1, 2], device='cuda'), True)
tensor([1, 2], device='cuda:0')
>>> torch.pow(torch.tensor([1, 2]), True)
tensor([1, 2])
>>> torch.pow(torch.tensor([1, 2]), False)
tensor([1, 1])
>>> torch.pow(torch.tensor([1, 2], device='cuda'), False)
tensor([1, 1], device='cuda:0')
```

I've run `test_torch.py` and got following results, so my guess is that I didn't break anything. I was just looking for a test that uses linear regression, as suggested.

```
Ran 1619 tests in 52.363s

OK (skipped=111)
[TORCH_VITAL] Dataloader.enabled		 True
[TORCH_VITAL] Dataloader.basic_unit_test		 TEST_VALUE_STRING
[TORCH_VITAL] CUDA.used		 true

```
(I can paste whole log, if necessary)

If this is a bad idea overall, dont worry about it. It's not a big deal, it's actually a two line change 😅  so can we talk of how do things in a different strategy.

For the record I've signed the agreement already. And I didn't run linter because it's not working 😞 . Looks like PyYaml 6.0 is broken and there's a 6.0.1 fix already but I have no idea how to update that 😅

Fixes #113198

Pull Request resolved: https://github.com/pytorch/pytorch/pull/114133
Approved by: https://github.com/lezcano

---
## [Prequal-Digital/git](https://github.com/Prequal-Digital/git)@[a1fbe26a0c...](https://github.com/Prequal-Digital/git/commit/a1fbe26a0c2bb8ba84c3976023e4ded4cf94608e)
#### Friday 2023-12-22 00:06:21 by Elijah Newren

completion: avoid user confusion in non-cone mode

It is tempting to think of "files and directories" of the current
directory as valid inputs to the add and set subcommands of git
sparse-checkout.  However, in non-cone mode, they often aren't and using
them as potential completions leads to *many* forms of confusion:

Issue #1. It provides the *wrong* files and directories.

For
    git sparse-checkout add
we always want to add files and directories not currently in our sparse
checkout, which means we want file and directories not currently present
in the current working tree.  Providing the files and directories
currently present is thus always wrong.

For
    git sparse-checkout set
we have a similar problem except in the subset of cases where we are
trying to narrow our checkout to a strict subset of what we already
have.  That is not a very common scenario, especially since it often
does not even happen to be true for the first use of the command; for
years we required users to create a sparse-checkout via
    git sparse-checkout init
    git sparse-checkout set <args...>
(or use a clone option that did the init step for you at clone time).
The init command creates a minimal sparse-checkout with just the
top-level directory present, meaning the set command has to be used to
expand the checkout.  Thus, only in a special and perhaps unusual cases
would any of the suggestions from normal file and directory completion
be appropriate.

Issue #2: Suggesting patterns that lead to warnings is unfriendly.

If the user specifies any regular file and omits the leading '/', then
the sparse-checkout command will warn the user that their command is
problematic and suggest they use a leading slash instead.

Issue #3: Completion gets confused by leading '/', and provides wrong paths.

Users often want to anchor their patterns to the toplevel of the
repository, especially when listing individual files.  There are a
number of reasons for this, but notably even sparse-checkout encourages
them to do so (as noted above).  However, if users do so (via adding a
leading '/' to their pattern), then bash completion will interpret the
leading slash not as a request for a path at the toplevel of the
repository, but as a request for a path at the root of the filesytem.
That means at best that completion cannot help with such paths, and if
it does find any completions, they are almost guaranteed to be wrong.

Issue #4: Suggesting invalid patterns from subdirectories is unfriendly.

There is no per-directory equivalent to .gitignore with
sparse-checkouts.  There is only a single worktree-global
$GIT_DIR/info/sparse-checkout file.  As such, paths to files must be
specified relative to the toplevel of a repository.  Providing
suggestions of paths that are relative to the current working directory,
as bash completion defaults to, is wrong when the current working
directory is not the worktree toplevel directory.

Issue #5: Paths with special characters will be interpreted incorrectly

The entries in the sparse-checkout file are patterns, not paths.  While
most paths also qualify as patterns (though even in such cases it would
be better for users to not use them directly but prefix them with a
leading '/'), there are a variety of special characters that would need
special escaping beyond the normal shell escaping: '*', '?', '\', '[',
']', and any leading '#' or '!'.  If completion suggests any such paths,
users will likely expect them to be treated as an exact path rather than
as a pattern that might match some number of files other than 1.

However, despite the first four issues, we can note that _if_ users are
using tab completion, then they are probably trying to specify a path in
the index.  As such, we transform their argument into a top-level-rooted
pattern that matches such a file.  For example, if they type:
   git sparse-checkout add Make<TAB>
we could "complete" to
   git sparse-checkout add /Makefile
or, if they ran from the Documentation/technical/ subdirectory:
   git sparse-checkout add m<TAB>
we could "complete" it to:
   git sparse-checkout add /Documentation/technical/multi-pack-index.txt
Note in both cases I use "complete" in quotes, because we actually add
characters both before and after the argument in question, so we are
kind of abusing "bash completions" to be "bash completions AND
beginnings".

The fifth issue is a bit stickier, especially when you consider that we
not only need to deal with escaping issues because of special meanings
of patterns in sparse-checkout & gitignore files, but also that we need
to consider escaping issues due to ls-files needing to sometimes quote
or escape characters, and because the shell needs to escape some
characters.  The multiple interacting forms of escaping could get ugly;
this patch makes no attempt to do so and simply documents that we
decided to not deal with those corner cases for now but at least get the
common cases right.

Signed-off-by: Elijah Newren <newren@gmail.com>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [Buildstarted/linksfordevs](https://github.com/Buildstarted/linksfordevs)@[dcd86dc807...](https://github.com/Buildstarted/linksfordevs/commit/dcd86dc8078c0d062b5bf15af45cf02e06025497)
#### Friday 2023-12-22 00:11:02 by Ben Dornis

Updating: 12/22/2023 12:00:00 AM

 1. Added: Online Privacy Protection Engine Keeps You Anonymous Online
    (https://juliusthejules.github.io/localhostack/)
 2. Added: Workspaces | marcel
    (https://www.marceltheshell.org/workspaces)
 3. Added: Memory Safety is a Red Herring
    (https://steveklabnik.com/writing/memory-safety-is-a-red-herring)
 4. Added: Ashwin's Blog
    (https://ashwinsundar.com/blog/compiled/cheap-scorecard.html)
 5. Added: I Wrote 2K+ Lines of Brainfuck. Here's What I've Learned
    (https://www.aartaka.me.eu.org/blog/brainfuck-lessons)
 6. Added: My Development Environment: kitty, zsh, Neovim, tmux, and lazygit
    (https://www.avni.sh/posts/developer-tools/my-development-environment/)
 7. Added: Perl Advent Calendar 2023 - Elves Versus Typos
    (https://perladvent.org/2023/2023-12-21.html)
 8. Added: The Cash Gift Taboo
    (https://www.timothyrice.org/cash/)
 9. Added: 2023: A Year in Review
    (https://alexeymk.com/2023/12/20/2023-year-in-review)
10. Added: Restoration of an IBM ThinkPad 701c
    (https://blog.jgc.org/2023/12/restoration-of-ibm-thinkpad-701c.html)
11. Added: How I set up an online startup
    (https://www.cruzluna.dev/posts/virtualsetup/)
12. Added: Zach Bellay | Always Be Refactoring
    (https://zachbellay.com/daily/always-be-refactoring/)
13. Added: Create a Website from a Screenshot and Refine It, All in the Browser – Alex Kirk
    (https://alex.kirk.at/2023/12/21/prototype-create-a-website-from-a-screenshot-and-refine-it-all-in-the-browser/)
14. Added: Why Blog? An Opinion from an Ex-YouTuber
    (https://www.raheeljunaid.com/posts/why-blog/)
15. Added: Eigensolutions: composability as the antidote to overfit • Lea Verou
    (https://lea.verou.me/blog/2023/eigensolutions/?latest=)
16. Added: The Loneliness of the Mid Level Vimmer
    (https://johnwhiles.com/posts/vimming-pains)
17. Added: Two Paths For Paying Down Tech Debt
    (https://shermanonsoftware.com/2023/12/21/two-paths-for-paying-down-tech-debt/)

Generation took: 00:10:51.1443814

---
## [pooka109/crawl](https://github.com/pooka109/crawl)@[afeb8edd3b...](https://github.com/pooka109/crawl/commit/afeb8edd3b8c5a8165938164b7b2bc36ea37fb54)
#### Friday 2023-12-22 01:43:23 by DracoOmega

Change player Ogres into Oni, shorten Armataur tongues

Ogres are considered a fairly weak player species, and have been arguably
additionally troubled by the fact that most of the ogres the player ever
encounters in the dungeon are dumb giant club brutes - leading new players
to assume this is the core ogre playstyle, despite many veterans arguing
that they make better mages than fighters, and that 1-hander + shield is
the better choice for them.

Simultaneously, there's been a desire to cut armataur's doubled potion
gimmick. Their new regen-on-rampage is already very strong, and does a
better job of emphasizing the species' core movement gimmick than long
tongue does, and it is much easier to reasonably balance their power
without TWO big sources of healing. (Inversely, despite their large hp
pools, ogres can be paradoxically fragile and could definitely benefit from
the additional potion healing.)

So I am simplifying that mutation, moving it to ogre, and rethemeing them
slightly to give the mechanic a stronger flavor fit.

Player Ogres are now Oni. Leaning into the mythical backdrop of them being
legendary drinkers and brawlers, oni gain doubled health and magic from
any potion that restores these (ie: !curing, !heal wounds, !magic, and
!ambrosia, and when they drink such a potion, they also make an immediate
attack against all enemies surrounding them. Cleave with a giant spiked
club, just so long as you have enough on hand to drink while you do it!

Oni apts are mostly the same as Ogres, with the following changes:
 Maces -1 -> 0
 Armour -2 -> -1
 Shields 0 -> -1
 Invocations 1 -> 2

People have clamored for ages for the most obvious wielder of giant spiked
clubs in the game to not have a negative apt and that seems reasonable to
me (the ancient +3 they had made this more of a no-brainer, but 0 probably
leaves other weapons sufficiently appealing)

Slightly better armor and slightly worse shields apt (along with drunken
brawling) may also nudge them a bit more towards 2-handers without making
them obviously correct.

And +1 invocations due to their famous associations of working for the
celestial bureaucracy (as torturers... >.>)

They have also gained horns 1 (they already were too large to wear helmets,
so this is a minor buff than a new restriction - also oni are usually
depicted with horns).

I toyed with the idea of giving them built-in shoutitits 1, with rewritten
messages so that they kept bellowing challenges and taunts at random
enemies. And while I think the flavor of this is *hilarious*, I worry that
their buffs might not entirely compensate for this downside. Or maybe it
would be fine along with some other minor tweak?

Either way, this hopefully does a somewhat better job of selling the
fantasy of the species one is playing as, while providing a unique gimmick
to play with.

(Enemy ogres are staying as ogres - it would defeat some of the purpose of
this if they changed - but Erolcha specifically may be slated to become an
oni instead)

---
## [rsm28/lethal_company_batch_files](https://github.com/rsm28/lethal_company_batch_files)@[38b4dcd359...](https://github.com/rsm28/lethal_company_batch_files/commit/38b4dcd3597eaff7c8128828d9d750ef043563a2)
#### Friday 2023-12-22 02:57:33 by rsm28

Update and rename backup_version.bat to BackupVersion.bat

FUCK YOU LEGACY FILES
UPDATE YOUR RUNMES

---
## [Crayon-ShinChan/next-intl](https://github.com/Crayon-ShinChan/next-intl)@[e6d98787ad...](https://github.com/Crayon-ShinChan/next-intl/commit/e6d98787ad43aec50dcb6594353da83a958a81d1)
#### Friday 2023-12-22 03:12:59 by Jan Amann

feat: Invoke `notFound()` when no locale was attached to the request and update docs to suggest validating the locale in `i18n.ts` (#742)

Users are currently struggling with errors that are caused by these two
scenarios:
1. An invalid locale was passed to `next-intl` APIs (e.g.
[#736](https://github.com/amannn/next-intl/issues/736))
2. No locale is available during rendering (e.g.
[#716](https://github.com/amannn/next-intl/issues/716))

**tldr:**
1. We now suggest to validate the incoming `locale` in
[`i18n.ts`](https://next-intl-docs.vercel.app/docs/usage/configuration#i18nts).
This change is recommended to all users.
2. `next-intl` will call the `notFound()` function when the middleware
didn't run on a localized request and `next-intl` APIs are used during
rendering. Previously this would throw an error, therefore this is only
relevant for you in case you've encountered [the corresponding
error](https://next-intl-docs.vercel.app/docs/routing/middleware#unable-to-find-locale).
Make sure you provide a relevant [`not-found`
page](https://next-intl-docs.vercel.app/docs/environments/error-files#not-foundjs)
that can be rendered in this case.

---

**Handling invalid locales**

Users run into this error because the locale wasn't sufficiently
validated. This is in practice quite hard because we currently educate
in the docs that this should happen in [the root
layout](https://next-intl-docs.vercel.app/docs/getting-started/app-router#applocalelayouttsx),
but due to the parallel rendering capabilities of Next.js, potentially a
page or `generateMetadata` runs first.

Therefore moving this validation to a more central place seems
necessary. Due to this, the docs will now suggest validating the locale
in `i18n.ts`. By doing this, we can catch erroneous locale arguments in
a single place before e.g. importing JSON files.

The only edge case is if an app uses no APIs of `next-intl` in Server
Components at all and therefore `i18n.ts` doesn't run. This should be a
very rare case though as even `NextIntlClientProvider` will call
`i18n.ts`. The only case to run into this is if you're using
`NextIntlClientProvider` in a Client Component and delegate all i18n
handling to Client Components too. If you have such an app, `i18n.ts`
will not be invoked and you should validate the `locale` before passing
it to `NextIntlClientProvider`.

**Handling missing locales**

This warning is probably one of the most annoying errors that users
currently run into:

```
Unable to find next-intl locale because the middleware didn't run on this request.
```

The various causes of this error are outlined in [the
docs](https://next-intl-docs.vercel.app/docs/routing/middleware#unable-to-find-locale).

Some of these cases should simply be 404s (e.g. when your middleware
matcher doesn't match `/unknown.txt`), while others require a fix in the
matcher (e.g. considering `/users/jane.doe` when using `localePrefix:
'as-necessary'`).

My assumption is that many of these errors are false positives that are
caused by the `[locale]` segment acting as a catch-all. As a result, a
500 error is encountered instead of 404s. Due to this, this PR will
downgrade the previous error to a dev-only warning and will invoke the
`notFound()` function. This should help in the majority of cases. Note
that you should define [a `not-found`
file](https://next-intl-docs.vercel.app/docs/environments/error-files#not-foundjs)
to handle this case.

I think this change is a good idea because if you're using
`unstable_setRequestLocale` and you have a misconfigured middleware
matcher, you can provide any kind of string to `next-intl` (also
`unknown.txt`) and not run into this error. Therefore it only affects
users with dynamic rendering. Validating the locale in `i18n.ts` is the
solution to either case (see above). Also in case something like
[`routeParams`](https://github.com/amannn/next-intl/issues/663) gets
added to Next.js, the current warning will be gone entirely—therefore
tackling it from a different direction is likely a good idea.

The false negatives of this should hopefully be rather small as we
consistently point out that you need to adapt your middleware matcher
when switching the `localePrefix` to anything other than `always`.
Dev-only warnings should help to get further information for these
requests.

---

Closes https://github.com/amannn/next-intl/issues/736
Closes https://github.com/amannn/next-intl/issues/716
Closes https://github.com/amannn/next-intl/discussions/446

---
## [ReturnToZender/ReturnsBubber](https://github.com/ReturnToZender/ReturnsBubber)@[d96b2b97aa...](https://github.com/ReturnToZender/ReturnsBubber/commit/d96b2b97aa9969f4a9d800ec0bc8501fcf3529ef)
#### Friday 2023-12-22 03:23:43 by Waterpig

Waterpig grows more insane with modularity: The massive PR that probably breaks shit (#838)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

I have circuitry theory finals in 1 hour. And as such, to distract
myself from my impending doom and to stop thinking about loop currents,
I have decided to start working on this. (Update: I passed)

This isn't even close to how I wish our modularity to look

But that's future Waterpig's problem (Note to self: Fix the no_antag
button)

In another news, this probably breaks stuff.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

<!-- Please make sure to actually test your PRs. If you have not tested
your PR mention it. -->

## Why It's Good For The Game

Modularity is good. The more stuff we can modularize the better, and
incase it gets removed upstream it's as simple as... removing our
modular override.
<!-- Argue for the merits of your changes and how they benefit the game,
especially if they are controversial and/or far reaching. If you can't
actually explain WHY what you are doing will improve the game, then it
probably isn't good for the game in the first place. -->

## Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. You can read up on GBP
and it's effects on PRs in the tgstation guides for contributors. Please
note that maintainers freely reserve the right to remove and add tags
should they deem it appropriate. You can attempt to finagle the system
all you want, but it's best to shoot for clear communication right off
the bat. -->

:cl:
refactor: Refactors modularity significantly
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

<!-- By opening a pull request. You have read and understood the
repository rules located on the main README.md on this project. -->

---------

Co-authored-by: The Sharkening <95130227+StrangeWeirdKitten@users.noreply.github.com>

---
## [Vapex55/f13babylonchange](https://github.com/Vapex55/f13babylonchange)@[ccb9ce38a7...](https://github.com/Vapex55/f13babylonchange/commit/ccb9ce38a7e26763f93c089bd0a65c9e35b70243)
#### Friday 2023-12-22 03:45:15 by panzerr1944

no mans land; kebob changes (#166)

## About The Pull Request

![image](https://github.com/f13babylon/f13babylon/assets/76122712/cb2a0acd-9aa7-4a0c-bc3a-651c2b0104d4)
Kebab now has renegades. And it's loot increased / fixed.


https://github.com/f13babylon/f13babylon/assets/76122712/22a30f2e-354c-4988-8ac7-e39e9fce9c51

## Why It's Good For The Game
NML's town is no longer free loot. Rather, an optional bunker that the
other factions might jump you at. Kind of like normal bunkers in that
way, except with current NML rules you aren't going to lose your
everything. Just your life until someone revives you. I like the no gear
looting in NML rule, it's kinda funny.

## Pre-Merge Checklist
- [ Y ] You tested this on a local server.
- [ Y ] This code did not runtime during testing.
- [ Y ] You documented all of your changes.

## Changelog
ADDED MOBS:
1x pa claw
6x r. docs
3x r. snipers
2x r. meisters
4x r. defenders
6x r. soldiers
10x r. grunts
9x r. prospects
2x r. engies
3x r. guardians
(Total: 46)
REMOVED MOBS:
4x Legendary Ghouls
6x Legendary Mutants
2x Legendary Deathclaws
(Total: 12)
ADDED/EDITED LOOT:
2x Superhigh Ballistic Spawners
1x Mid-High E-Weapon Spawner
1x Mid-High Ballistic Weapon Spawner
1x Mid E-Weapon Spawner
1x Mid Ballistic Spawner
1x NVG Spawner
1x Gauss Rifle Spawner
1x Deluxe Stock Parts Spawner
1x (x10) Strange Seeds Spawner
1x Unique Weapon Spawner
1x High Ballistic Print
1x VHigh Ballistic Print
1x DC Medicine Journal
1x Chemistry Book
1x Random Armor Spawner
1x T4 Armor Spawner
1x Bowl of Fruit
CHANGED TERRAIN / WALLS / MISC:
Sandbags on the main road
Sandbags at the farm and graveyard
Indestructible Walls for south-side to prevent cheese
Replaced see-through airlock with high-sec one in clinic for d-claw
-
Everything else is unedited from current Kebab to my knowledge.

---
## [Vapex55/f13babylonchange](https://github.com/Vapex55/f13babylonchange)@[a2491a3c89...](https://github.com/Vapex55/f13babylonchange/commit/a2491a3c89e4fa54e2c112902162278493f10945)
#### Friday 2023-12-22 03:45:15 by Mazzinsanity

Enables Podpeople as a Roundstart Species (May need to be enabled on the box) (#194)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

<!-- NOTE: This format is NOT REQUIRED for things like runtime fixes,
code fixes and optimizations. In those instances you should try to give
a description of what is being fixed or optimized but are not required
to fill out the complete changelog. -->
<!-- Adjusting things like armor or weapon values for balance, while
they may be 'fixes' in their own way, are not considered code fixes as
described above and require the use of the Pull Request format below.-->


## About The Pull Request

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->
Makes a WEAKENED version of Podpeople selectable as a roundstart
species. Their maluses and bonuses are as follows:
- 1.25 damage modifiers for Brute/Burn
- Restore 2 hunger and heal 0.2 Brute, 0.2 Burn, 0.1 Toxin when in
light.
- Reverse effects in darkness.

Changes podpeople bloodtype to EZ Nutrient
## Why It's Good For The Game
This lets people play as anthropomorphic Broc flowers.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Pre-Merge Checklist
<!-- Don't bother filling these in while creating your Pull Request,
just click the checkboxes after the Pull Request is opened and you are
redirected to the page. -->
- [x] You tested this on a local server.
- [x] This code did not runtime during testing.
- [x] You documented all of your changes.
<!-- Neither the compiler nor workflow checks are perfect at detecting
runtimes and errors. It is important to test your code/feature/fix
locally. -->


## Changelog
<!-- This is mostly optional for small Pull Requests, but if you value
being credited for your work in-game be sure to fill it out. To opt-out,
remove everything below including the start and end :cl: brackets. -->

<!-- If your Pull Request includes a minor single line variable edit,
probably do not fill out this changelog. -->
<!-- However, if your pull request includes massive or immediately
noticeable changes, briefly describe those changes in some way in this
changelog. -->

:cl:
add: enabled podpeople as a roundstart species
balance: rebalanced weak podpeople healing
tweak: changed podpeople bloodtype to EZ Nutrient
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [helge17/tuxguitar](https://github.com/helge17/tuxguitar)@[de7b7ca82f...](https://github.com/helge17/tuxguitar/commit/de7b7ca82f04c110b149715e7260c6e7bf5b4d29)
#### Friday 2023-12-22 04:58:48 by guiv42

Add tracks volume controls

Add volume controls for each *TuxGuitar instrument*.
Note that several tracks may use different *TuxGuitar instruments*,
even if they use the same *MIDI instrument* (i.e. the same *sound*).
Typically: from an empty song, add one track. The 2 tracks are associated
to 2 instruments, both of them playing "Steel String Guitar" sound.
In this case, volume can be set independently for each track.

# Description
A "mixer" area has been added on the left part of tracks table.
Currently this area seems under-utilized, it seems to me there is some serious
potential for improvement.
Examples could be: higlight volume control associated to currently selected track,
add a button to show/hide mixer, a button to "show instruments",
add a column of buttons to customize content of mixer area
(sort of vertical tabs, as in Tools/Settings dialog), etc.
However I would prefer to play a bit with this interface first,
before thinking of detailed possible improvements.

Volume controls have exactly the same functionality than volume knobs
present in channels dialog (menu View/Show Instruments).
Note that this dialog and tracks table can be visible simultaneously,
in this case controls are synchronized (moving knob in dialog updates scale in tracks table,
and reciprocally).

# Limitations
- One vertical dimension is hard-coded, to leave some margin for the height
  of horizontal scrollbar of tracks table. I could not find a way to compute it
  (see `TGTableViewer.resizeTable()`).
- Volume scales remain permanently enabled, even if all tracks associated
  to instrument are muted. One volume scale in this configuration has no
  audible effect. Still, selected value will be saved to file if user saves song.
- Help section not yet updated, I prefer to get some feedback of user experience first (adjustment may be needed)

# Rationale for implementation
A very significant amount of time spent to evaluate different user interfaces.
Finally, the implemented behavior is by far the cleanest in terms of implementation
(no need for a detailed fine-tuning, all widgets are used in their usual configuration).
It's also the most reproducible one across all tested platforms.

The most user-friendly solution was probably to add directly an horizontal
volume control *inside* the tracks table (e.g. next to Solo/Mute buttons).
However, rows' height is really too small for a horizontal scale to fit in.
I tried to hijack a ProgressBar to reproduce the behavior of an horizontal scale.
Really good-looking in Linux/SWT, but difficult to adjust in JFX config.
Ugly in Win10/SWT. Practically, visual rendering really differs a lot between
all tested configurations.
Not deterministic enough to guarantee correct user interface in all configs.

I also tried a "volatile" scale, appearing temporarily when clicking on something,
then disappearing when clicking elsewhere.
It's feasible in SWT config, but I could not make it work correctly with JFX:
an undecorated window does not respond to .setFocus(), and a UIScale in such a window
does not loose focus when clicking elsewhere, so I could not find a way to
display/hide such a control in a comprehensive manner.
This would have also required another icon, creating a possible confusion with "mute" icon
(represented by a loudspeaker).

UISlider could fit vertically, but horizontal representation is not adapted
to functionality.

---
## [DETrooper/Begotten-III](https://github.com/DETrooper/Begotten-III)@[9bf9870fa6...](https://github.com/DETrooper/Begotten-III/commit/9bf9870fa684c529988e0b899e92dd97ae02a492)
#### Friday 2023-12-22 05:08:53 by DETrooper

Major Melee Changes, Longship Rework

	- Added an option to customize the name of your longship via the scroll item.
	- Added broken bone functionality to arms, which massively increases stamina cost for melee actions (attacking, blocking, parrying, etc).
	- Added 'PlayerEnteredDuel' and 'PlayerExitedDuel' hooks.
	- Blunt weapons can now cause broken bone injuries if high enough in damage or if the targetted limb damage is low enough.
	- Combat rolling now adds a small delay to stamina regeneration.
	- Everyone aboard a longship lost at sea (i.e. due to storm damage) will now be PKed.
	- Fire sacrifical weapons/the ring of fire now cannot ignite a player while they are in the process of rolling.
	- Fixed an issue where shields might not automatically lower after being guardbroken.
	- Fixed decapitation melee damage buff persisting into other duels.
	- Fixed Knight Juticar Plate having a helmet overlay despite now not being a model replacement armor.
	- Fixed radio frequency lua error.
	- Fixed VJBase npc spawn exploit (thx Obamasgrandpa).
	- Increased cost of the longship scroll at the Master Huntsman from 300 coin to 1000 to disincentivize lone raiders.
	- Longships are now saved to their respective scrolls and will inherit saved HP.
	- Longships can now be ignited if holding a lantern. Doing so will slowly burn it unless it is extinguished.
	- Made gashes and especially gunshot wounds more punishing, as they now also drain blood. Also fixed them sometimes being applied without causing the bleeding status. This should make combat more lethal.
	- Merged poise into stamina as was my intention for Begotten VR and Begotten IV. This should intrinsically make speed builds much less overpowered. Changed effects of Courier's Ring, Outlasting belief, and the Praeventor subfaction bonus to reduce stamina consumption while running instead of adding stamina.
	- Optimized PlayerThink hook by adding an argument with the player's lua table.
	- Reduced longship repair amount from each wood item from 500 HP to 100.
	- Reduced the window for rollcatching across the board to make combat rolling more forgiving.
	- The 'Contortionist's Boot' charm now decreases roll stamina cost by 50%.
	- The 'Marked' and 'Favored' traits now affect the odds of finding your longship in a stormy sea zone.
	- When destroyed, deleted, or docked, longships will drop the contents of their cargo hold into a belongings entity (expires after 20 minutes).

---
## [ReturnToZender/ReturnsBubber](https://github.com/ReturnToZender/ReturnsBubber)@[2e656fba14...](https://github.com/ReturnToZender/ReturnsBubber/commit/2e656fba14e0b67086bb4d2eff59d6fa6748a55c)
#### Friday 2023-12-22 05:47:43 by Cursor

Grants the ability to open Clown slots once more. (#853)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

Title. Skyrat disabled it because they hate fun. We don't.

<!-- Please make sure to actually test your PRs. If you have not tested
your PR mention it. -->

## Why It's Good For The Game

Say a Clown dies. Is arrested, or is just a bit shit.
What can you do?
Jackshit.
Pray, fax Clown Planet, but why wait on God or the Clown in the High
Castle when you can do it yourself?
This also let's Antags, or Clowns summon more friends. Assuming people
in the lobby wanna be a clown.

P.S. I commented out and unticked the Skyrat file for double safety.
Tried to just override it, didn't work. If you have a better idea for
this. You have the floor.

## Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. You can read up on GBP
and it's effects on PRs in the tgstation guides for contributors. Please
note that maintainers freely reserve the right to remove and add tags
should they deem it appropriate. You can attempt to finagle the system
all you want, but it's best to shoot for clear communication right off
the bat. -->

:cl:
add: Clown slots are re-openable by royal decree. The incident between
Nanotrasen and King Honkington has been resolved.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

<!-- By opening a pull request. You have read and understood the
repository rules located on the main README.md on this project. -->

---------

Co-authored-by: Waterpig <49160555+Majkl-J@users.noreply.github.com>

---
## [mparley/advent-of-code](https://github.com/mparley/advent-of-code)@[2612ab3526...](https://github.com/mparley/advent-of-code/commit/2612ab35262f51bd624542b1567aad228dfcddb1)
#### Friday 2023-12-22 06:05:59 by Marcellus Parley

2023 Day 20

Kinda a pain in the ass. I finished on the night of but wanted to
clean up my code a bit before committing it, but in doing so I broke
something. So I had to go back and fix it today. Also did part 1
of 21 but part 2 is deep fried bullshit and I want to get my solution
on it working even though I did read about the math trick and it would
be easier just doing that.

---
## [TheModernDayRenaissance/gem-hunt](https://github.com/TheModernDayRenaissance/gem-hunt)@[666e7d4fab...](https://github.com/TheModernDayRenaissance/gem-hunt/commit/666e7d4fab204002b88a6aaad50bcbf6be4bdcf5)
#### Friday 2023-12-22 07:11:01 by TheModernDayRenaissance

Update README.md

Secret code #1:Found on Sam's werewolf boyfriend painting lost in the pink backpack left in Seattle, Washington 

Secret code #2: You ever watched National Treasure with Nicholas Cage?

Secret code #3: Sprigatito Loves You is green coder and Laddy Litten is black red programmer. They are an ABGAN in love.

Secrets are also left in the DSi I left on the Seattle University campus, or Singularity University campus I deem it as in my acronym hashmap in my mind's eye. Go back in time and figure this one out, assholes of this ASSHOLE HOUSEHOLD YEAHHHHHH!!!!!!!!

---
## [Gboster-0/lobotomy-corp13](https://github.com/Gboster-0/lobotomy-corp13)@[0a75aef49d...](https://github.com/Gboster-0/lobotomy-corp13/commit/0a75aef49d6474eecc4996a25c1a40766ba18df8)
#### Friday 2023-12-22 07:34:37 by The Bron Jame Offical

Representative Update (#1695)

ITS REALLLLL.

K-corp ERT

begone Crit up

hello health booster

R-corp weapon researches

oh wow thats a lot of rabbit weapons

KIRIE WHY ARE THERE SO MANY

okay normal again, R-corp rep mains eatin good tonite

ancient ass code, reaping what we have sown.

oh for fucks sake

lore fixes

K-corp ERT

changes from Redacteds PR into relevant files

added K-corp spear sound

K-corp ERT comes with grenades that fabricate 3 K-Corp Drones

icon pain and suffeirng

Update lc13icons.dmi

---
## [Retrino/lobotomy-corp13](https://github.com/Retrino/lobotomy-corp13)@[2defb31817...](https://github.com/Retrino/lobotomy-corp13/commit/2defb31817005f7790e9586ace0c4e77c23d7f06)
#### Friday 2023-12-22 08:09:37 by vampirebat74

Adds Red Shoes (#901)

Mr. Heavenly's Abnormality Jam Entry #1

Records

uncommented weapon

Finishing touches

Design rework

adds ego gift and inhands

New sprites!

uncommented sfx

insanity fix

quieter sound loop

Fixes some shit

fix linters

requested changes

Adds Red Shoes

Mr. Heavenly's Abnormality Jam Entry #1

Records

uncommented weapon

Finishing touches

Design rework

adds ego gift and inhands

New sprites!

uncommented sfx

insanity fix

quieter sound loop

Fixes some shit

fix linters

requested changes

Update code/modules/mob/living/simple_animal/abnormality/he/red_shoes.dm

fixes suit check in assimilate() proc

Co-authored-by: [̸R̵e̵d̴a̴c̶t̸e̸d̴]̵ <61567407+LanceSmites328@users.noreply.github.com>

Update code/modules/mob/living/simple_animal/abnormality/he/red_shoes.dm

fixes dismembering

Co-authored-by: [̸R̵e̵d̴a̴c̶t̸e̸d̴]̵ <61567407+LanceSmites328@users.noreply.github.com>

Update code/modules/mob/living/simple_animal/abnormality/he/red_shoes.dm

Co-authored-by: [̸R̵e̵d̴a̴c̶t̸e̸d̴]̵ <61567407+LanceSmites328@users.noreply.github.com>

breach is more dangerous

compiles

bug fix

fixes simple mob

bug fixes

Panic fixed!!!!

stuff

wayward records

Update code/modules/paperwork/records/info/he.dm

Co-authored-by: [̸R̵e̵d̴a̴c̶t̸e̸d̴]̵ <61567407+LanceSmites328@users.noreply.github.com>

Update code/modules/mob/living/simple_animal/abnormality/he/red_shoes.dm

Co-authored-by: [̸R̵e̵d̴a̴c̶t̸e̸d̴]̵ <61567407+LanceSmites328@users.noreply.github.com>

attribute bonus

requested changes

Co-authored-by: Mr.Heavenly <davidx3adamhunt@gmail.com>

---
## [moto-sm7250-devs/android_kernel_motorola_sm7250](https://github.com/moto-sm7250-devs/android_kernel_motorola_sm7250)@[49457cf240...](https://github.com/moto-sm7250-devs/android_kernel_motorola_sm7250/commit/49457cf240e6a9921665df338efbe0cf56f6d53f)
#### Friday 2023-12-22 09:03:18 by Peter Zijlstra

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
Change-Id: I40e0e01946eadb1701a4d06758e434591e5a5c92

---
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[ddf1cb7870...](https://github.com/pytorch/pytorch/commit/ddf1cb78705dcf79fe8c8df01f6f18ca4a218c55)
#### Friday 2023-12-22 09:11:44 by voznesenskym

AOTAutograd: handle set_(), detect metadata mutations that cancel out (#111554)

This should be enough to get @voznesenskym 's FSDP branch to plumb `set_()` through AOTAutograd properly and have everything properly no-op out. Main changes are:

(1) graph break on `aten::set_.source_Tensor_storage_offset` (we could support it but it isn't needed, seems safer to graph break)

(2) Functionalization: add a "proper" functionalization kernel for `aten::set_.source_Tensor`. The previous one we had was codegen'd and it was wrong (it would just clone() and call set_(), which does not do the right thing). I also manually mark on the `FunctionalTensorWrapper` when a given tensor has been mutated by a `set_()` call.

(3) AOTAutograd: I added a new field, `InputAliasInfo.mutates_storage_metadata`, so we can distinguish between "regular" metadata mutations, and metadata mutations due to `set_()` calls. This is mainly because at runtime, one requires calling `as_strided_()` to fix up metadata, while the other requires calling `set_()`.

(4) Made AOTAutograd's detection for metadata mutations / set_() mutations smarter and detect no-ops (if the storage and metadata are all the same).

I also killed `was_updated()` and `was_metadata_updated()`, and replaced them with (existing) `has_data_mutation() ` and (new) `has_data_mutation()`, which can more accurately distinguish between data-mutation vs. `set_()` calls vs. metadata-mutation

**This PR is still silently correct in one case though**, which I'd like to discuss more. In particular, this example:
```
def f(x):
    x_view = x.view(-1)
    x.set_(torch.ones(2))
    x_view.mul_(2)
    return
```

If you have an input that experiences both a data-mutation **and** a `x_old.set_(x_new)` call, there are two cases:

(a) the data mutation happened on the storage of `x_new`. This case should be handled automatically: if x_new is a graph intermediate then we will functionalize the mutation. If x_new is a different graph input, then we will perform the usual `copy_()` on that other graph input

(b) the data mutation happened on the storage of `x_old`. This is more of a pain to handle, and doesn't currently work. At runtime, the right thing to do is probably something like:
```

def functionalized_f(x):
    x_view = x.view(-1)
    # set_() desugars into a no-op; later usages of x will use x_output
    x_output = torch.ones(2)
    # functionalize the mutation on x_view
    x_view_updated = x.mul(2)
    x_updated = x_view_updated.view(x.shape)
    # x experienced TWO TYPES of mutations; a data mutation and a metatadata mutation
    # We need to return both updated tensors in our graph
    return x_updated, x_output
def runtime_wrapper(x):
    x_data_mutation_result, x_set_mutation_result = compiled_graph(x)
    # First, perform the data mutation on x's old storage
    x.copy_(x_data_mutation_result)
    # Then, swap out the storage of x with the new storage
    x.set_(x_set_mutation_result)
```

There are two things that make this difficult to do though:

(1) Functionalization: the functionalization rule for `set_()` will fully throw away the old `FunctionalStorageImpl` on the graph input. So if there are any mutations to that `FunctionalStorageImpl` later on in the graph, the current graph input won't know about it. Maybe we can have a given `FunctionalTensorWrapper` remember all previous storages that it had, and track mutations on all of them - although this feels pretty complicated.

(2) AOTAutograd now needs to know that we might have *two* graph outputs that correspond to a single "mutated input", which is annoying.

It's worth pointing out that this issue is probably extremely unlikely for anyone to run into - can we just detect it and error? This feels slightly easier than solving it, although not significantly easier. We would still need `FunctionalTensorWrapper` to keep track of mutations on any of its "previous" storages, so it can report this info back to AOTAutograd so we can raise an error.

Pull Request resolved: https://github.com/pytorch/pytorch/pull/111554
Approved by: https://github.com/ezyang
ghstack dependencies: #113926

---
## [StrangeWeirdKitten/Bubberstation](https://github.com/StrangeWeirdKitten/Bubberstation)@[8f88ae12d3...](https://github.com/StrangeWeirdKitten/Bubberstation/commit/8f88ae12d380bf7aa73524e60e068628ab878fe1)
#### Friday 2023-12-22 09:25:07 by StrangeWeirdKitten

Stuff

I wasted 4 fucking hours over this one line

sure

god dammit

Reverts icon cutting (for now)

[MIRROR] Fixes input boxes [No gbp] [MDB IGNORE] (#25761)

* Fixes input boxes [No gbp] (#80490)

## About The Pull Request
One of the quirks of react is that we're no longer using onChange the
same as Inferno - React's version is a synthetic event. I made the
mistake of thinking it would be okay. Many interfaces are using onChange
events to send messages to byond (very laggy), others are using it to
close the input (closes each keypress).

So this was the alternative- I hope to replicate the behavior via onBlur
&& onEnter. I went through to undo most of the onInput -> onChange
replacements of #80340 where it made sense. Other inputs which should
safely use onChange (DEFINITELY to send messages) remain as such.

Example of an input which used onChange now working with this PR:

![aUojN0owHO](https://github.com/tgstation/tgstation/assets/42397676/82aa1d44-360d-4978-bef8-12720d7b4c70)
## Why It's Good For The Game
Bug fixes
Fixes #80486
## Changelog
:cl:
fix: Name input in character setup should work properly now.
fix: Many inputs should feel more responsive.
/:cl:

* Fixes input boxes [No gbp]

---------

Co-authored-by: Jeremiah <42397676+jlsnow301@users.noreply.github.com>

[MIRROR] Fixes dropdowns not rendering the selection's displayText post-selection [MDB IGNORE] (#25755)

* Fixes dropdowns not rendering the selection's displayText post-selection (#80464)

## About The Pull Request

What it says on the tin. Dropdowns were displaying the `selection`
instead of `displayText` after clicking an option.

Note: this bug was only _noticeably_ affecting dropdowns whose
`selection` differed from `displayText`. In the below example, the
dropdown uses numeric indices for `selection` and a string for
`displayText`. In those cases the `displayText` should take precedence,
not the other way around.

<details><summary>From this</summary>

![XCsUpfbezj](https://github.com/tgstation/tgstation/assets/13398309/3fac640d-a4ac-488c-94de-5413a74b0836)

</details>

<details><summary>To this</summary>

![CvjsD6TmtW](https://github.com/tgstation/tgstation/assets/13398309/ec30cb11-11db-4a64-87ad-cef6add86f5b)

</details>

## Why It's Good For The Game

Fixes a minor bug

## Changelog

:cl:
fix: fixes some dropdowns not displaying the right text after selecting
something
/:cl:

* Fixes dropdowns not rendering the selection's displayText post-selection

---------

Co-authored-by: Bloop <13398309+vinylspiders@users.noreply.github.com>

[MIRROR] Fixes some missed tgui files that needed prettier run on them [MDB IGNORE] (#25756)

* Fixes some missed tgui files that needed prettier run on them (#80466)

## About The Pull Request

that's it.

## Changelog

Nothing player facing

* Fixes some missed tgui files that needed prettier run on them

---------

Co-authored-by: Bloop <13398309+vinylspiders@users.noreply.github.com>

Revert "Fixes false walls icons using the wrong icon files (#80175)"

This reverts commit 4dce402e72d97b462f647422ee4fd31a17c9c1c2.

Revert "Reverts icon cutting (for now)"

This reverts commit f07448f4fca2d1d47a7a0c49e82289fcbca0f758.

lets gooo

Fixes Obscurity examine prefs runtiming on punpun (#878)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
The PR that added this forgot to include a ?, so mobs without a client
return null, and runtime, sometimes hundreds of time in a shift.

This PR fixes that.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

<!-- Please make sure to actually test your PRs. If you have not tested
your PR mention it. -->

## Why It's Good For The Game
Less runtimes in the runtime menu. God there's so many.
<!-- Argue for the merits of your changes and how they benefit the game,
especially if they are controversial and/or far reaching. If you can't
actually explain WHY what you are doing will improve the game, then it
probably isn't good for the game in the first place. -->

## Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. You can read up on GBP
and it's effects on PRs in the tgstation guides for contributors. Please
note that maintainers freely reserve the right to remove and add tags
should they deem it appropriate. You can attempt to finagle the system
all you want, but it's best to shoot for clear communication right off
the bat. -->

:cl: ReturnToZender
fix: Runtime on obscurity examine prefs when the mob in question lacks a
client
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

<!-- By opening a pull request. You have read and understood the
repository rules located on the main README.md on this project. -->

Oops! Broke Job Estimation! (#877)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
I accidentally removed an ! in the job estimation menu, meaning only
people who switched it on actually showed on the menu.
Of course, people didn't know this, and didn't turn off their
preference. This fixes that.

![image](https://github.com/Bubberstation/Bubberstation/assets/110273561/874af1cb-1af6-424a-8de3-6205a0d542ac)
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

<!-- Please make sure to actually test your PRs. If you have not tested
your PR mention it. -->

## Why It's Good For The Game
Job estimation my beloved
<!-- Argue for the merits of your changes and how they benefit the game,
especially if they are controversial and/or far reaching. If you can't
actually explain WHY what you are doing will improve the game, then it
probably isn't good for the game in the first place. -->

## Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. You can read up on GBP
and it's effects on PRs in the tgstation guides for contributors. Please
note that maintainers freely reserve the right to remove and add tags
should they deem it appropriate. You can attempt to finagle the system
all you want, but it's best to shoot for clear communication right off
the bat. -->

:cl: ReturnToZender
fix: job estimation actually works again
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

<!-- By opening a pull request. You have read and understood the
repository rules located on the main README.md on this project. -->

Automatic changelog for PR #878 [ci skip]

Automatic changelog for PR #877 [ci skip]

wee

Revert "Fixes false walls icons using the wrong icon files (#80175)"

This reverts commit 4dce402e72d97b462f647422ee4fd31a17c9c1c2.

I wasted 4 fucking hours over this one line

sure

god dammit

---
## [Mezzelo/TwosCompany](https://github.com/Mezzelo/TwosCompany)@[7bfd229e5a...](https://github.com/Mezzelo/TwosCompany/commit/7bfd229e5a234ae431db89a35a4b198024dad927)
#### Friday 2023-12-22 09:51:35 by Mezzelo

1.2.0

- all (most of) the dialogue!
- balance changes!

- Added dialogue! 1,200 lines total so far - including combat barks, pre-fight banter, memories, and intro sequences between vanilla characters and the ones from this mod.
	- no memories for ilya yet; can't fit them all into that screen yet lol.  haven't had time to draw custom bgs yet either.
	- no dialogue w/ other modded characters yet, either.  i'll get around to that eventually, I hope.
- A lot of balance (mostly nerfs), QOL changes, and fixes.
- Dialogue sprites adjusted, not that you were seeing those often beforehand!

notices for players:
- this build requires the beta branch to function (1.0.6 at time of writing) due to vanilla code changes: this is what most mods are developed on.
- for those of you who use the dev menu: using "unlock all" also marks all dialogues as seen.  if you don't want to miss the one-off scenes from this mod and from others, take caution when using it (don't, or use it prior to loading your game with mods to unlock vanilla content only.)

for other character modders: while I don't recommend most of this mod's boilerplate (structured to load in a metric ton of content, past the scope of most character mods), i would recommend taking a peek at the json externalization, derived from the base game's code ofc.  might be an option you find more attractive than baking it into the code, even if you don't plan on localization

CARDS
- All Hands' cost increased to 4.  All Hands B is now a cost reduction to 3, instead of changing its functionality.
+ Call and Response now discounts the drawn card's cost by 1 across all variants.  A decreases cost by 2.
	~ Reworded description to hopefully make this more concise.
	- (fix) You can no longer C&R a C&R, as this would lead to a crash (and also make for a silly infinite) - thanks to Arin for finding this.
~ Captain's Orders now gives you the played card's base cost, rather than its current cost.
+ (fix) Let Loose no longer increases the cost of 0-cost cards - thanks to Arin for finding this.
- Onslaught is now limited based on stacks: Base and A give 3 stacks, and drawing a card uses a stack.  B gives 6 stacks.
	- (fix) Onslaught will no longer reshuffle your discard into your draw if there are no cards it can draw from your discard
~ (fix) Opening Gambit now uses vanilla discount/expensive system for calculating cost, which may affect modded interactions.
	- Opening Gambit's cost no longer resets on discard.
+ Ruminate's cost decreased to 0 from 1, for the default and A variants.
- Sudden Shift nerfed to 2 move, from 3.  B gives 1 evade instead of 2, B retains.

+ Bind reworked: Costs 0 by default, but cost increases by 1 per turn for every other card played.  A gives shield, B gives temp strafe.
+ Coup De Grace's cost has lowered by 1 for all variants, to 2. Coup De Grace A now stuns, instead of dealing 2 more damage.
- False Opening B now sets temp shield to 0.
~ Harry now has 2 random move both times for the base variant, instead of A.
- Lightning strikes' damage decreased from 1-2 to 1-1.
+ Point Defense now costs 0, instead of its cost reducing by 1 when played.
	+ (fix) Point Defense now targets enemy shield drones.
	~ (fix) Point Defense can no longer target geodes.
	- (fix) Point Defense will still attempt to move and fire if engine locked or frozen, but will discard instead of allowing you to play it infinitely.
+ Recover's cost now resets if discarded.
- Removed the first attack from Wild Strikes (1-1-1 to 1-1) and the dodges were changed to move 2-1, across all variants.
- Wild Dodge is now a random move, instead of giving evade. Its upgraded variants have been tweaked as well.

- Apex's self-inflicted engine lock increased by 1 for all variants. (3 base, 2 for A, 4 for B.)
- Cauterize B ends turn on use.  Cauterize A costs 2, as did all other variants. All variants heal 1 health, from 2 for default and A.
- Fireball A's cost increased to 2, from 1.
- Haze reworked almost entirely: swapped random move w/ evade, alongside other changes.
- Heat Treatment's cost increased to 2, from 1.
~ Ignition's cost increased to 2 for all variants, and gives 2 heat per turn instead of 1.
- Imbue now gives 1 overdrive and 1 shield rather than 2 overdrive, for all variants except A.  A's cost increased to 2 instead of retaining.
- Maul's damage decreased from 2-2-3 to 1-2-2, for all variants.
- All variants of Pressure now hurt the player when used with 3 heat.
- Reactor Burn reworked. Also too long for this changelog lol, but it should it should break the game a lot less easily now.
- Scars gives 1 energy instead of 2, for the default and B variants. Scars A still gives 2, but no longer only damages 1.
+ Thermal Runaway now gives 1 overdrive, for all variants.
	~ (fix) Thermal Runaway now displays the proper icon for exhausting entire hand.
	- Cost of all variants increased to 2.

ARTIFACTS
+ (fix) Auxiliary Thrusters should not skip card select on boot now - thanks to TheJazMaster for finding this.
~ Command Center now shows the last two cards from different decks you've used, to better help you keep track.
~ Metronome now displays whether you've last attacked or moved - thanks to Shockah for the suggestion.
	- It now requires 6 consecutive alternating moves/attacks, increased from 5.
	+ Multiple consecutive attacks from the same card will no longer reset the counter, to make it usable on i.e. ships with multiple cannons.
+ Incendiary Rounds now adds an additional heat on shot, and causes enemies to overheat immediately from heat added by this artifact.
	~ (fixed typo.  how'd nobody point this out dammit)
~ (fix) Shield Shunt should no longer crash your game - thanks to LazyFangs for diagnosing this.
- Worn Lighter now gives 1 overdrive, instead of 2.

---
## [pivovarit/AoC_2023_go](https://github.com/pivovarit/AoC_2023_go)@[f6fcf67ce5...](https://github.com/pivovarit/AoC_2023_go/commit/f6fcf67ce5323aa8ac8756612c57c67c21373391)
#### Friday 2023-12-22 10:44:35 by Grzegorz Piwowarek

Day 12 (#19)

### Day 12: Hot Springs

You finally reach the hot springs! You can see steam rising from
secluded areas attached to the primary, ornate building.

As you turn to enter, the researcher stops you. "Wait - I thought you
were looking for the hot springs, weren't you?" You indicate that this
definitely looks like hot springs to you.

"Oh, sorry, common mistake! This is actually the onsen! The hot springs
are next door."

You look in the direction the researcher is pointing and suddenly notice
the massive metal helixes towering overhead. "This way!"

It only takes you a few more steps to reach the main gate of the massive
fenced-off area containing the springs. You go through the gate and into
a small administrative building.

"Hello! What brings you to the hot springs today? Sorry they're not very
hot right now; we're having a lava shortage at the moment." You ask
about the missing machine parts for Desert Island.

"Oh, all of Gear Island is currently offline! Nothing is being
manufactured at the moment, not until we get more lava to heat our
forges. And our springs. The springs aren't very springy unless they're
hot!"

"Say, could you go up and see why the lava stopped flowing? The springs
are too cold for normal operation, but we should be able to find one
springy enough to launch you up there!"

There's just one problem - many of the springs have fallen into
disrepair, so they're not actually sure which springs would even be safe
to use! Worse yet, their condition records of which springs are damaged
(your puzzle input) are also damaged! You'll need to help them repair
the damaged records.

In the giant field just outside, the springs are arranged into rows. For
each row, the condition records show every spring and whether it is
operational (.) or damaged (#). This is the part of the condition
records that is itself damaged; for some springs, it is simply unknown
(?) whether the spring is operational or damaged.

However, the engineer that produced the condition records also
duplicated some of this information in a different format! After the
list of springs for a given row, the size of each contiguous group of
damaged springs is listed in the order those groups appear in the row.
This list always accounts for every damaged spring, and each number is
the entire size of its contiguous group (that is, groups are always
separated by at least one operational spring: #### would always be 4,
never 2,2).

So, condition records with no unknown spring conditions might look like
this:
```
#.#.### 1,1,3
.#...#....###. 1,1,3
.#.###.#.###### 1,3,1,6
####.#...#... 4,1,1
#....######..#####. 1,6,5
.###.##....# 3,2,1
```
However, the condition records are partially damaged; some of the
springs' conditions are actually unknown (?). For example:

```
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
```
Equipped with this information, it is your job to figure out how many
different arrangements of operational and broken springs fit the given
criteria in each row.

In the first line (???.### 1,1,3), there is exactly one way separate
groups of one, one, and three broken springs (in that order) can appear
in that row: the first three unknown springs must be broken, then
operational, then broken (#.#), making the whole row #.#.###.

The second line is more interesting: .??..??...?##. 1,1,3 could be a
total of four different arrangements. The last ? must always be broken
(to satisfy the final contiguous group of three broken springs), and
each ?? must hide exactly one of the two broken springs. (Neither ??
could be both broken springs or they would form a single contiguous
group of two; if that were true, the numbers afterward would have been
2,3 instead.) Since each ?? can either be #. or .#, there are four
possible arrangements of springs.

The last line is actually consistent with ten different arrangements!
Because the first number is 3, the first and second ? must both be . (if
either were #, the first number would have to be 4 or higher). However,
the remaining run of unknown spring conditions have many different ways
they could hold groups of two and one broken springs:

```
?###???????? 3,2,1
.###.##.#...
.###.##..#..
.###.##...#.
.###.##....#
.###..##.#..
.###..##..#.
.###..##...#
.###...##.#.
.###...##..#
.###....##.#
```
In this example, the number of possible arrangements for each row is:


- ```???.### 1,1,3``` - 1 arrangement
- ```.??..??...?##. 1,1,3``` - 4 arrangements
- ```?#?#?#?#?#?#?#? 1,3,1,6``` - 1 arrangement
- ```????.#...#... 4,1,1``` - 1 arrangement
- ```????.######..#####. 1,6,5``` - 4 arrangements
- ```?###???????? 3,2,1``` - 10 arrangements

Adding all of the possible arrangement counts together produces a total
of 21 arrangements.

For each row, count all of the different arrangements of operational and
broken springs that meet the given criteria. What is the sum of those
counts?

#### Part Two

As you look out at the field of springs, you feel like there are way
more springs than the condition records list. When you examine the
records, you discover that they were actually folded up this whole time!

To unfold the records, on each row, replace the list of spring
conditions with five copies of itself (separated by ?) and replace the
list of contiguous groups of damaged springs with five copies of itself
(separated by ,).

So, this row:
```
.# 1
```
Would become:
```
.#?.#?.#?.#?.# 1,1,1,1,1
```
The first line of the above example would become:

```
???.###????.###????.###????.###????.### 1,1,3,1,1,3,1,1,3,1,1,3,1,1,3
```
In the above example, after unfolding, the number of possible
arrangements for some rows is now much larger:

- ```???.### 1,1,3``` - 1 arrangement
- ```.??..??...?##. 1,1,3``` - 16384 arrangements
- ```?#?#?#?#?#?#?#? 1,3,1,6``` - 1 arrangement
- ```????.#...#... 4,1,1``` - 16 arrangements
- ```????.######..#####. 1,6,5``` - 2500 arrangements
- ```?###???????? 3,2,1``` - 506250 arrangements
After unfolding, adding all of the possible arrangement counts together
produces 525152.

Unfold your condition records; what is the new sum of possible
arrangement counts?

---
## [danskernesdigitalebibliotek/dpl-design-system](https://github.com/danskernesdigitalebibliotek/dpl-design-system)@[1065fe4f35...](https://github.com/danskernesdigitalebibliotek/dpl-design-system/commit/1065fe4f3596706d3b9d5698aa37ccfd46705ac4)
#### Friday 2023-12-22 10:48:37 by LasseStaus

Example of my thoughts for layout structure/variables

I added this as a seperate file 'cause of short time.
Look over it and see what you think. I think this is modular enough to be used for what we have and expanded upon later with __background modifications etc.

Hopefully it makes sense, sorry for no thorough explanation.

Look at top comment of the file, and see example at the bottom.

---
## [mamedev/mame](https://github.com/mamedev/mame)@[52ecd995e7...](https://github.com/mamedev/mame/commit/52ecd995e7baab82cf219c9d7c40eca327a8f9e2)
#### Friday 2023-12-22 12:11:53 by wilbertpol

msx2_flop.xml: Added 33 items (32 working) and replaced five items with better dumps. (#11863)

* Replaced Disc Station Deluxe 1 (Japan) with a better dump. [file-hunter]
* Replaced Poyo Poyo Life (Japan) and  Poyo Poyo Life II (Japan) with better dumps. [file-hunter]
* Replaced Pumpkin Adventure - The Quest for the Holy Grail (Netherlands) with a better dump. [file-hunter]
* Replaced Pumpkin Adventure II (Netherlands) with a better dump. [file-hunter]
* Removed hacked images Pumpkin Adventure - The Quest for the Holy Grail (Netherlands, alt) and Pumpkin Adventure - The Quest for the Holy Grail (Netherlands, alt 2).
* Removed User Disk from Pumpkin Adventure III (Netherlands).
* Removed Puyo Puyo (Japan, alt) and  Puyo Puyo (Japan, alt 2) as they contain saved data.

New working software list items (msx2_flop.xml)
-------------------------------
Disc Station Special Natsuyasumi-gou (Japan) [file-hunter]
Outlaw Suikoden (Japan) [file-hunter]
Kibun wa, Pastel Touch!! Abunai Gakuen Hen (Japan) [file-hunter]
PIAS - Hikisakareta Seishun (Japan) [file-hunter]
Private School (Japan) [file-hunter]
Puzzle Game Nadia Special (Japan) [file-hunter]
Puzzle - Große Meister (Germany) [file-hunter]
R・SYSTEM Ketteihan (Japan) [file-hunter]
R・SYSTEM 3.2 (Japan) [file-hunter]
OK Fred (Netherlands) [file-hunter]
Panic Shoot [file-hunter]
Petiso Game (Spain) [file-hunter]
PH.Sound Collection (Japan) [file-hunter]
Phi (Japan) [file-hunter]
Pig's Quest (Netherlands) [file-hunter]
Piles (Netherlands) [file-hunter]
Pixess (Netherlands) [file-hunter]
Point Crisis [file-hunter]
Poker Dolls [file-hunter]
Poyo Poyo Life 3 (Japan) [file-hunter]
Push'em [file-hunter]
Puzzel (Netherlands) [file-hunter]
Puzzle 9.64 (Japan) [file-hunter]
Puzzlemania (Netherlands) [file-hunter]
Quadromania MSX2 [file-hunter]
Quiz! Atatchatte 25% (Japan, 1996-12-26) [file-hunter]
Quiz! Atatchatte 25% (Japan) [file-hunter]
RCCR - RC Car Race (Japan) [file-hunter]
Realms of Adventure (Netherlands) [file-hunter]
Retaliator (Netherlands) [file-hunter]
Riot (Japan, alt) [file-hunter]
Ruby & Jade [file-hunter]

New software list items marked not working (msx2_flop.xml)
------------------------------------------
Disc Station Special Haru-gou (Japan) [file-hunter]

---
## [Krashly/Ark-Station-13](https://github.com/Krashly/Ark-Station-13)@[2805c86c81...](https://github.com/Krashly/Ark-Station-13/commit/2805c86c811fde2450a054a25c7a665b77df47e5)
#### Friday 2023-12-22 13:52:36 by Nerevar

[THE HALF-MODULAR PRINCE] Snalance (Snail Balance) and Snissues (Snail Issues) Adjustment (#25439)

* initial d

* holy shit i forgot

* i got so much cheese in my pocket, they thought I was a fucking calzone

* opp was sneak-dissing on the 'gram, turned his city into pompeii

* Just fixing some diffs (line breaks should match tg)

* Fixes these edit comments

---------

Co-authored-by: Giz <13398309+vinylspiders@users.noreply.github.com>

---
## [retlaw34/Shiptest](https://github.com/retlaw34/Shiptest)@[caa19d2a6f...](https://github.com/retlaw34/Shiptest/commit/caa19d2a6f8014c2d34663c7c63685921bc0218a)
#### Friday 2023-12-22 14:01:02 by GenericDM

Assorted cringe removal pt.whatever (#2534)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Removes more cringe I found laying around.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
/tg/ was on some WILD shit.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
del: removes tail club
del: removes all flavors of tail whip
del: removes lizardskin clothing
del: removes 'Genetic Purifier'
tweak: makes bunny ears desc not incredibly sexist
tweak: change up wording in magic mirror gender change
del: removes 'genuine' cat ears
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [xXPawnStarrXx/tgstation](https://github.com/xXPawnStarrXx/tgstation)@[3c2d4f03a8...](https://github.com/xXPawnStarrXx/tgstation/commit/3c2d4f03a8883a416434dcb7e32c334bba3e40ae)
#### Friday 2023-12-22 14:34:41 by SSensum

New Quirk! Cyborg Lover! (#80023)

## About The Pull Request

This PR adds a new quirk for people, who want to play as
silicon-friendly crew.

Basic quirk info:
- It costs 2 points.
- It has minor additions to person's mail goodies list (cable coils,
basic cells, etc).
- It has a few simple mood events, when you pet a borg or being
touched/hugged by borg.

## Why It's Good For The Game

I think it is nice to have a chance to play as ~~robo-creep~~ person who
loves borgos.

## Changelog

:cl:
add: Added new quirk: Cyborg Lover!
/:cl:

---------

Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

---
## [NoResponseMate/Sylius](https://github.com/NoResponseMate/Sylius)@[23b4abd530...](https://github.com/NoResponseMate/Sylius/commit/23b4abd530ad3b985f4028dbeab869d004d9593f)
#### Friday 2023-12-22 14:47:11 by Jacob Tobiasz

minor #15646 [API][Admin] Allow using float for amount in tax rates (NoResponseMate)

This PR was merged into the 1.13 branch.

Discussion
----------

| Q               | A                                                            |
|-----------------|--------------------------------------------------------------|
| Branch?         | 1.13 |
| Bug fix?        | kinda                                                       |
| New feature?    | no                                                       |
| BC breaks?      | no                                                       |
| Deprecations?   | no |
| Related tickets | related #15616                      |
| License         | MIT                                                          |

It's hacky as hell; caused by [this bug](https://github.com/api-platform/core/issues/1647), the only other way of fixing it is a migration but that sucks by itself. I'm guessing there are more convoluted ways as well but that's too much pain for the gain.

Commits
-------
  [API][Admin] Allow using float for amount in tax rates

---
## [purindaisuki/tkfmtools](https://github.com/purindaisuki/tkfmtools)@[63cfadbd4d...](https://github.com/purindaisuki/tkfmtools/commit/63cfadbd4dce9cdb3a63bc6cefa25b1124f03c6f)
#### Friday 2023-12-22 15:06:56 by C0unt-zero

Add New Characters

"423": "Centaur Girl Mareyl"
"424": "Mummy Mu-Mu"
"527": "Snowy Fantasy Aridya"
"528": "Sexmas Caroler Iblis"
"529": "Sexmas Evie"
"530": "Holy Night Rouser Salina"

---
## [zjdyzww/react](https://github.com/zjdyzww/react)@[b6978bc38f...](https://github.com/zjdyzww/react/commit/b6978bc38f6788c7e73982b9fd2771aabdf36f15)
#### Friday 2023-12-22 15:43:54 by Andrew Clark

experimental_use(promise) (#25084)

* Internal `act`: Unwrapping resolved promises

This update our internal implementation of `act` to support React's new
behavior for unwrapping promises. Like we did with Scheduler, when 
something suspends, it will yield to the main thread so the microtasks
can run, then continue in a new task.

I need to implement the same behavior in the public version of `act`,
but there are some additional considerations so I'll do that in a
separate commit.

* Move throwException to after work loop resumes

throwException is the function that finds the nearest boundary and
schedules it for a second render pass. We should only call it right 
before we unwind the stack — not if we receive an immediate ping and
render the fiber again.

This was an oversight in 8ef3a7c that I didn't notice because it happens
to mostly work, anyway. What made me notice the mistake is that
throwException also marks the entire render phase as suspended
(RootDidSuspend or RootDidSuspendWithDelay), which is only supposed to
be happen if we show a fallback. One consequence was that, in the 
RootDidSuspendWithDelay case, the entire commit phase was blocked,
because that's the exit status we use to block a bad fallback
from appearing.

* Use expando to check whether promise has resolved

Add a `status` expando to a thrown thenable to track when its value has
resolved.

In a later step, we'll also use `value` and `reason` expandos to track
the resolved value.

This is not part of the official JavaScript spec — think of
it as an extension of the Promise API, or a custom interface that is a
superset of Thenable. However, it's inspired by the terminology used
by `Promise.allSettled`.

The intent is that this will be a public API — Suspense implementations
can set these expandos to allow React to unwrap the value synchronously
without waiting a microtask.

* Scaffolding for `experimental_use` hook

Sets up a new experimental hook behind a feature flag, but does not
implement it yet.

* use(promise)

Adds experimental support to Fiber for unwrapping the value of a promise
inside a component. It is not yet implemented for Server Components, 
but that is planned.

If promise has already resolved, the value can be unwrapped
"immediately" without showing a fallback. The trick we use to implement
this is to yield to the main thread (literally suspending the work
loop), wait for the microtask queue to drain, then check if the promise
resolved in the meantime. If so, we can resume the last attempted fiber
without unwinding the stack. This functionality was implemented in 
previous commits.

Another feature is that the promises do not need to be cached between
attempts. Because we assume idempotent execution of components, React
will track the promises that were used during the previous attempt and
reuse the result. You shouldn't rely on this property, but during
initial render it mostly just works. Updates are trickier, though,
because if you used an uncached promise, we have no way of knowing 
whether the underlying data has changed, so we have to unwrap the
promise every time. It will still work, but it's inefficient and can
lead to unnecessary fallbacks if it happens during a discrete update.

When we implement this for Server Components, this will be less of an
issue because there are no updates in that environment. However, it's
still better for performance to cache data requests, so the same
principles largely apply.

The intention is that this will eventually be the only supported way to
suspend on arbitrary promises. Throwing a promise directly will
be deprecated.

---
## [Paxilmaniac/Skyrat-tg](https://github.com/Paxilmaniac/Skyrat-tg)@[fc0dc4ec6f...](https://github.com/Paxilmaniac/Skyrat-tg/commit/fc0dc4ec6f1d9ce02608825df6a6f942fec44b8c)
#### Friday 2023-12-22 15:50:20 by SkyratBot

[MIRROR] Changes Virology Rather Than Killing It [MDB IGNORE] (#25483)

* Changes Virology Rather Than Killing It (#79854)

## About The Pull Request
God, alright, here we go. See HackMD here:
https://hackmd.io/@ Higgin/HJljdBuNp

Alternative proposal to #79849 addressing the big problems with
virology. ~~If you need a HackMD for it, I'll put one together, but I
made a comment on that PR and can make it pretty simple here.~~ its done

1. Makes viruses eventually self-cure as long as you're alive. If you
can keep somebody from dying, they can develop immunity.
2. Makes it so you can sleep comfortably and be well-fed to slow and
even potentially defeat viruses without a cure.
3. Makes it so more dangerous viruses can start self-curing faster. This
means Space Ebola is going to burn itself out quicker if a person stays
alive from the other effects.
4. Makes spaceacillin helpful in naturally curing viruses, period, but
with declining effectiveness over 100 cycles.
5. Makes it so curing a virus naturally without being well-fed or having
rode it out from the peak may allow you to be reinfected/not have
natural immunity.
6. Makes it so being well-fed is a much stronger protection against
random virus spread.
7. Makes it so bypasses_immunity stuff like fungal TB and heart failure
isn't subject to any of this.
8. Makes it so using ~~antibiotics~~ spaceacillin jesus christ or being
malnourished can make you lose your healing viruses too. Pay attention
to what you put in your body.
9. ** Makes it so blood can ~~transmit resistances again, not just
vaccines. It's been a hot minute, but it used to work like this.~~ blood
now can cure a virus if the donor has a resistance, but it doesn't
confer lasting immunity. You need to overcome the virus yourself, carry
a constant supply of pure blood, or get a vaccine to get a lasting fix.
10. ** makes severity a function of disease stats and all active
symptoms - not just the highest severity of the active symptoms.
11. ** makes it so you can nosell symptoms firing with spaceacillin or
resting down to a minimum chance of cure_chance to avoid symptoms each
cycle, declining over time, over 100 cycles for a given disease.
12. ** makes it so wearing protective equipment prevents you from
spreading respiratory-spread diseases normally - not just on the
cough/sneezing symptoms.
13. ** gives MDs virology access standard, paramedics and coroners
virology access on skeleton crew. virologists also get pharmacy access.
14. ** makes bypasses_immunity advanced diseases always override
non-bypasses_immunity advanced diseases and resist being overridden by
other advanced diseases. Sentient Disease now has bypasses_immunity.
Sentient Disease fans rejoice!
15. ** also gives SD a buffer of extra stealth points so it has a bit
longer to build up instead of almost uniformly getting spotted and dying
early.
16. ** viruses now scale their severity as a function of their max
symptoms. There's a lot more room to get viruses of varying duration and
severity by adding fewer symptoms now - so creating a tradeoff between
stats (and good thresholds) and the duration of your virus.
17. ** a whole bunch of defines to control all of this stuff - most
recently added a multiplier for symptom appearance frequency.

MAJOR UPDATES: REBALANCING TOWARDS 50% LETHALITY

https://docs.google.com/spreadsheets/d/e/2PACX-1vQ8rqMYFsR1mYj_FGzVjTfcnAF7un-VofOByPxcCCQr6lOOF5fhUgZga0oA4Q5-7K4hr7fCV0jFdmd9/pubhtml#
[Viro Rework Rebalance
Tests.pdf](https://github.com/tgstation/tgstation/files/13447208/Viro.Rework.Rebalance.Tests.pdf)

After a shitload of testing, makes some of the most reliable,
transmissible killers into less-reliable threats. See the above graphs
and pictures for demonstrations of exactly how this was tested and done.

## Why It's Good For The Game

It sucks to be hard-stuck to needing chemistry and medical to deal with
viruses that somebody can randomly blast out without a care in the
world, then be left to sit around waiting to die or otherwise be unable
to do anything as the max-level symptoms fire off on repeat.

This should put curing and surviving viruses much more back in the hands
of normal crew without always ending up at the chemistry front window,
although that is still the fastest and most reliable way to get better.

This also nerfs healing viruses a bit, or makes them a bit less
fire-and-forget if you fail to attend to your body. There's more I'd
like to do in the future and potentially some of the other classic
viruses that could use bypasses_immunity added, values tweaked, but for
now - this seems like the best way to preserve virology as a level of
depth and complexity in the game in a way that rewards people doing
intuitive things to counterplay it when used harmfully.

This also puts more of the mid-range bad symptoms into a better place
balance-wise because the worst ones pretty much only fire at max stages.
With the way this works out, you bounce back and forth between the max
stage and lower stages before, over time, trending towards a cure.
Symptoms that provide more significant effects at lower stages now have
a place that isn't totally overshadowed by the killdeath stage 5 ARDS +
junk symptoms virus Dr. Ambatu Popov shat out in five minutes (as long
as you survive the initial run-in with it.)

## Changelog

:cl:
balance: most diseases can now be slowed, mitigated, and eventually
cured through being well-fed, resting, and using spaceacillin. Curing
diseases through this way will give you immunity if you experience them
at their peak/maximum and aren't starving/malnourished when they cure.
balance: disease symptoms can be forestalled for up to 100 cycles with a
declining chance of avoiding them over time using rest or spaceacillin.
balance: This does not apply to things like fungal TB; it does apply to
healing viruses if you don't take care of yourself by staying fed and
avoiding spaceacillin.
balance: disease can be cured through direct injection or ingestion of
cured blood. However, curing disease in this way does not provide
lasting immunity. You need to naturally beat the virus or get a vaccine
for that.
balance: Wearing internals or using protective equipment while infected
can limit the spread of respiratory illnesses from yourself to others.
Contact transmission is still possible however.
balance: Medical Doctors now have roundstart virology access. Paramedics
and coroners now get virology access on skeleton shift access.
Virologists now have roundstart pharmacy access.
balance: Sentient Diseases now resist being overridden by other advanced
diseases and can always override other advanced diseases; they also have
an extra bonus on their stealth stat to help make up for early outing
without a bit more testing.
balance: biohazard lockers now also contain a syringe of spaceacillin
(in line with the orderable kit from cargo.)
balance: Virus severity is now also a function of the number of symptoms
out of max your virus has. Experiment with different combinations using
less than six symptoms to make viruses that are deceptively less-obvious
and less quick to self-cure at the tradeoff of stats.
/:cl:

* Changes Virology Rather Than Killing It

---------

Co-authored-by: Higgin <cdonny11@yahoo.com>

---
## [Paxilmaniac/Skyrat-tg](https://github.com/Paxilmaniac/Skyrat-tg)@[015a3cf18a...](https://github.com/Paxilmaniac/Skyrat-tg/commit/015a3cf18a133ef12c1ee5bac4a4179140ecbc75)
#### Friday 2023-12-22 15:50:20 by Bloop

[MANUAL MIRROR] Replaces prettierx with the normal prettier (#80189)  (#25538)

* Replaces prettierx with the normal prettier (#80189)

Oh god the file diff... I'm so, so sorry.

No need to worry though. This just replaces the prettierx version that
we were using and replaces it with normal prettier. Most of the settings
were default or no longer valid with this version.
You no longer get this warning #70484

It actually drives me up the wall and I have to click it each time I
open my editor.
N/A nothing player facing

* Converts this to tsx

* Update JobsPage.tsx

* Update JobsPage.tsx

* Update JobsPage.tsx

---------

Co-authored-by: Jeremiah <42397676+jlsnow301@users.noreply.github.com>

---
## [Arturlang/Bubberstation](https://github.com/Arturlang/Bubberstation)@[fa8399334f...](https://github.com/Arturlang/Bubberstation/commit/fa8399334f9bc10abbf6ddf25b40e43b5363a9ae)
#### Friday 2023-12-22 16:08:04 by The-Sun-In-Splendour

Horrorform changeling salt PR (#859)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Now okay. I get it. It's huge, it's obvious, it's slow... I don't care
if it has more health and sustain than a tank spider or blobbernaut.
What I care is that it can fit into vents.

You can kill a changeling horror form with enough manpower. It's hard
but it's doable. But the fucking fact it can just... Ventcrawl into any
vent and if you don't see the tiny icon during the shitshow and push it?
Sorry but that is just absolute aids gameplay. Usually the monsters with
ventcrawl are pretty weak to make up for it. But not horrorling. I'm
sorry but if you have;

1. 750 health
2. 40 fucking damage swings (A double esword is 34 damage)
3. Passive, CONSTANT life regen
4. Lifesteal off dead bodies

You do **_not_** need ventcrawl. 

## Why it's good for the game

Do I really need to explain why having this almost unkillable machine be
able to ventcrawl to escape practically every situation because "teehee
forgot to weld vent in obscure location!" is bad for the game?

Yes. This is a salt PR.

:cl:
balance: Horror ling cannot ventcrawl anymore
/:cl:

---
## [ETs-Alien-Organizations/.admin](https://github.com/ETs-Alien-Organizations/.admin)@[47ee50d0cb...](https://github.com/ETs-Alien-Organizations/.admin/commit/47ee50d0cbc58c5c2423b64712c0c4eb9beaba78)
#### Friday 2023-12-22 16:14:44 by Chais Thomas Fitzwater

Create README.md

BMO-Financial-Inc/.github is a special repository: this README.md will appear on your public organization profile, visible to anyone.Chais Fitzwater stock portfolio - Google Finance November, 26. 2023 8:10 am 1160 walker ave, saint Louis. Mo 63138..I would like to propose moving support for the PulseAudio sound server into Arch Linux proper. This would also be in preparation for the eventual arrival of Gnome 3, since it will be unlikely we can effectively maintain the needed GStreamer patch any more.

To that effect I have created a plan:

---

To provide PulseAudio in [extra]...

Move the following packages from [community] to [extra]:
- libasyncns
- rtkit
- pulseaudio (split into pulseaudio and libpulse)
- alsa-plugins
- pulseaudio-alsa
    Configuration package, contains /etc/asound.conf
    depends on pulseaudio, alsa-plugins
- pavucontrol
- paprefs
- pulseaudio-mixer-applet
- ossp
    provides osspd OSS emulator

Rebuild the following packages with PulseAudio support:
- sdl (sdl-pulse in AUR)
- openal (openal-pulse in AUR)
- libgstreamer0.10-good
    split gstreamer0.10-pulse (in community)
- libao
    split libao-pulse (in community)
- libcanberra
    split libcanberra-pulse (in community)
    will be a split plugin instead of a wholly rebuilt copy
- gnome-media
    split gnome-media-pulse (in community; rebuilt with --enable-pulse)
- gnome-settings-daemon
    split gnome-settings-daemon-pulse (in community; rebuilt without gstreamer patch)

Provide the following groups:
- pulseaudio-gnome
    pulseaudio-alsa
    libcanberra-pulse
    gstreamer0.10-pulse
    gnome-media-pulse
    gnome-settings-daemon-pulse
    pulseaudio-mixer-applet
    pavucontrol
    paprefs

---

One of the problems of PulseAudio is that it pretty much becomes the default as
soon as you install it:
  - The client library will start the server if it's not running.
  - pulseaudio will install .desktop files that autostart the server together
    with Gnome or KDE.

Splitting libpulse would prevent that, but I believe we still need to test
on a per-application basis whether we can enable PulseAudio support (with a
dependency on libpulse) without breaking fallback to ALSA on systems without
pulseaudio.

Some packages (like sdl and openal) look for libpulse dynamically and will
still work even though the lib is missing, so they only need an optional
dependency.

I would be maintaining split -pulse packages where needed. A scientist explains an approaching milestone marking the arrival of quantum computers
1
Nov 20, 2023
1
Physics Quantum Physics
 Editors' notes
A scientist explains an approaching milestone marking the arrival of quantum computers
by Daniel Lidar , The Conversation

quantum computer
Credit: Pixabay/CC0 Public Domain

Quantum advantage is the milestone the field of quantum computing is fervently working toward, where a quantum computer can solve problems that are beyond the reach of the most powerful non-quantum, or classical, computers.

Quantum refers to the scale of atoms and molecules where the laws of physics as we experience them break down and a different, counterintuitive set of laws apply. Quantum computers take advantage of these strange behaviors to solve problems.

There are some types of problems that are impractical for classical computers to solve, such as cracking state-of-the-art encryption algorithms. Research in recent decades has shown that quantum computers have the potential to solve some of these problems. If a quantum computer can be built that actually does solve one of these problems, it will have demonstrated quantum advantage.

I am a physicist who studies quantum information processing and the control of quantum systems. I believe that this frontier of scientific and technological innovation not only promises groundbreaking advances in computation but also represents a broader surge in quantum technology, including significant advancements in quantum cryptography and quantum sensing.

The source of quantum computing's power
Central to quantum computing is the quantum bit, or qubit. Unlike classical bits, which can only be in states of 0 or 1, a qubit can be in any state that is some combination of 0 and 1. This state of neither just 1 or just 0 is known as a quantum superposition. With every additional qubit, the number of states that can be represented by the qubits doubles.

This property is often mistaken for the source of the power of quantum computing. Instead, it comes down to an intricate interplay of superposition, interference and entanglement.

Interference involves manipulating qubits so that their states combine constructively during computations to amplify correct solutions and destructively to suppress the wrong answers. Constructive interference is what happens when the peaks of two waves—like sound waves or ocean waves—combine to create a higher peak. Destructive interference is what happens when a wave peak and a wave trough combine and cancel each other out. Quantum algorithms, which are few and difficult to devise, set up a sequence of interference patterns that yield the correct answer to a problem.

Entanglement establishes a uniquely quantum correlation between qubits: The state of one cannot be described independently of the others, no matter how far apart the qubits are. This is what Albert Einstein famously dismissed as "spooky action at a distance." Entanglement's collective behavior, orchestrated through a quantum computer, enables computational speed-ups that are beyond the reach of classical computers.

Applications of quantum computing
Quantum computing has a range of potential uses where it can outperform classical computers. In cryptography, quantum computers pose both an opportunity and a challenge. Most famously, they have the potential to decipher current encryption algorithms, such as the widely used RSA scheme.

One consequence of this is that today's encryption protocols need to be reengineered to be resistant to future quantum attacks. This recognition has led to the burgeoning field of post-quantum cryptography. After a long process, the National Institute of Standards and Technology recently selected four quantum-resistant algorithms and has begun the process of readying them so that organizations around the world can use them in their encryption technology.


The ones and zeros – and everything in between – of quantum computing.

In addition, quantum computing can dramatically speed up quantum simulation: the ability to predict the outcome of experiments operating in the quantum realm. Famed physicist Richard Feynman envisioned this possibility more than 40 years ago. Quantum simulation offers the potential for considerable advancements in chemistry and materials science, aiding in areas such as the intricate modeling of molecular structures for drug discovery and enabling the discovery or creation of materials with novel properties.

Another use of quantum information technology is quantum sensing: detecting and measuring physical properties like electromagnetic energy, gravity, pressure and temperature with greater sensitivity and precision than non-quantum instruments. Quantum sensing has myriad applications in fields such as environmental monitoring, geological exploration, medical imaging and surveillance.

Initiatives such as the development of a quantum internet that interconnects quantum computers are crucial steps toward bridging the quantum and classical computing worlds. This network could be secured using quantum cryptographic protocols such as quantum key distribution, which enables ultra-secure communication channels that are protected against computational attacks—including those using quantum computers.

Despite a growing application suite for quantum computing, developing new algorithms that make full use of the quantum advantage—in particular in machine learning—remains a critical area of ongoing research.

Staying coherent and overcoming errors
The quantum computing field faces significant hurdles in hardware and software development. Quantum computers are highly sensitive to any unintentional interactions with their environments. This leads to the phenomenon of decoherence, where qubits rapidly degrade to the 0 or 1 states of classical bits.

Building large-scale quantum computing systems capable of delivering on the promise of quantum speed-ups requires overcoming decoherence. The key is developing effective methods of suppressing and correcting quantum errors, an area my own research is focused on.

In navigating these challenges, numerous quantum hardware and software startups have emerged alongside well-established technology industry players like Google and IBM. This industry interest, combined with significant investment from governments worldwide, underscores a collective recognition of quantum technology's transformative potential. These initiatives foster a rich ecosystem where academia and industry collaborate, accelerating progress in the field.

Quantum advantage coming into view
Quantum computing may one day be as disruptive as the arrival of generative AI. Currently, the development of quantum computing technology is at a crucial juncture. On the one hand, the field has already shown early signs of having achieved a narrowly specialized quantum advantage. Researchers at Google and later a team of researchers in China demonstrated quantum advantage for generating a list of random numbers with certain properties. My research team demonstrated a quantum speed-up for a random number guessing game.

On the other hand, there is a tangible risk of entering a "quantum winter," a period of reduced investment if practical results fail to materialize in the near term.

While the technology industry is working to deliver quantum advantage in products and services in the near term, academic research remains focused on investigating the fundamental principles underpinning this new science and technology. This ongoing basic research, fueled by enthusiastic cadres of new and bright students of the type I encounter almost every day, ensures that the field will continue to progress.


Provided by The Conversation 

This article is republished from The Conversation under a Creative Commons license. Read the original article.The Conversation

+ Explore further
Can cloud-based quantum computing really offer a quantum advantage?
41 shares
 Feedback to editors
Related
Recommended

Can cloud-based quantum computing really offer a quantum advantage?
Sep 22, 2023

Researchers provide comprehensive review of quantum teleportation
Jun 13, 2023

The best of both worlds: Combining classical and quantum systems to meet supercomputing demands
Aug 12, 2021

Can quantum computing protect AI from cyber attacks?
May 26, 2023

Two qudits fully entangled
Apr 20, 2023

IBM says it's reached milestone in quantum computing
Nov 10, 2017
Comments (1)
Sign in or create Science X account to leave the comment.

Homer10
2 hours ago
0
Computer: I'm sorry the password you typed in does not meet out complexity requirements. You need at least the following:
5243 lower case characters
32914 spaces or non printable characters
235412 upper case characters
1243 punctuation marks
32 Bitcoin ID numbers
1 Snake Eyes
and 35 Queen of hearts
Please re enter a new password?

Quoteetcryptoking1@outlook.com3@33#333O3r33p333h3e33u333s3a33n333g3e33l333s3README.md20238:10 am631381160.indexlogs

---
## [semanticdata/zola](https://github.com/semanticdata/zola)@[22dc32a589...](https://github.com/semanticdata/zola/commit/22dc32a5893deac5e91d173d0daf59e1868065ef)
#### Friday 2023-12-22 16:19:00 by sinofp

Add support for lazy loading images (#2211)

* Add optional decoding="async" loading="lazy" for img

In theory, they can make the page load faster and show content faster.

There’s one problem: CommonMark allows arbitrary inline elements in alt text.
If I want to get the correct alt text, I need to match every inline event.

I think most people will only use plain text, so I only match Event::Text.

* Add very basic test for img

This is the reason why we should use plain text when lazy_async_image is enabled.

* Explain lazy_async_image in documentation

* Add test with empty alt and special characters

I totaly forgot one can leave the alt text empty.
I thought I need to eliminate the alt attribute in that case,
but actually empty alt text is better than not having an alt attribute at all:
https://www.w3.org/TR/WCAG20-TECHS/H67.html
https://www.boia.org/blog/images-that-dont-need-alternative-text-still-need-alt-attributes
Thus I will leave the empty alt text.

Another test is added to ensure alt text is properly escaped.
I will remove the redundant escaping code after this commit.

* Remove manually escaping alt text

After removing the if-else inside the arm of Event::Text(text),
the alt text is still escaped.
Indeed they are redundant.

* Use insta for snapshot testing

`cargo insta review` looks cool!

I wanted to dedup the cases variable,
but my Rust skill is not good enough to declare a global vector.

---
## [dragomagol/tgstation](https://github.com/dragomagol/tgstation)@[b7b0932c4b...](https://github.com/dragomagol/tgstation/commit/b7b0932c4b5b3d4f9386b6dce514ee1ba3e25a05)
#### Friday 2023-12-22 16:37:59 by distributivgesetz

Delamination variants are now locked in after the countdown is reached (#80324)

## About The Pull Request

Does what it says on the tin.
## Why It's Good For The Game

This effectively changes one and only one thing: 

The "All Within Theoretical Limits" achievement is easier/fairer to get
with this. Previously, if you edged a crystal with the gas composition
method to get a resonance cascade, you had to make sure that your gas
composition stayed until it left the explosion point, which made the
achievement extremely finnicky and unfun to get this way. Regular
delaminations won't really be affected, because yeah. It's at the
explosion point. What are you going to do about it?

This makes the achievement easier to cheese, but honestly, in my opinion
as person who added the achievement, meh. If people feel like this isn't
good for the achievement, say something in the comments.

Closes #79528

## Changelog
:cl:
balance: Delamination variants no longer change once the explosion point
has been reached.
/:cl:

---
## [cheesePizza2/Foundation-19](https://github.com/cheesePizza2/Foundation-19)@[c423a27e5f...](https://github.com/cheesePizza2/Foundation-19/commit/c423a27e5f56f70f505916f8848a27488ed4e25e)
#### Friday 2023-12-22 16:42:15 by cheesePizza2

Fixes goals system harddels (#1316)

* shit

* fuck you

* removes spaces

---
## [Demadunk/endless-war](https://github.com/Demadunk/endless-war)@[e263c7ea48...](https://github.com/Demadunk/endless-war/commit/e263c7ea48af9be84f713c31769763c3fa4fd9a5)
#### Friday 2023-12-22 16:44:21 by Demadunk

I hate how i can't git reset on github desktop

Fuck this shitty program

---
## [UzuCore/Onion](https://github.com/UzuCore/Onion)@[c7694511f2...](https://github.com/UzuCore/Onion/commit/c7694511f224fe469f97b98308a9dcfb6fb13917)
#### Friday 2023-12-22 16:48:50 by XK

FEAT: Update ScummVM Standalone to 2.9.0git (#1307)

## Overview
Update to scummvm 2.9.0 to include all updates & fixes to the scrollbars
in: https://github.com/scummvm/scummvm/pull/5472

<img
src="https://github.com/OnionUI/Onion/assets/47260768/89080ee6-124e-445a-a14d-b818e277e991"
width="400" alt="Run ScummVM_000"><img
src="https://github.com/OnionUI/Onion/assets/47260768/86848e29-a304-4c9e-ae1f-1c4d491d044a"
width="400" alt="Run ScummVM_001">

## To test

Testing GUI -> 640 x 480: 

- [x]  GUI can be freely scaled to its smallest size

Testing scrollbars:

- [x] Open global options -> Keymaps & observe a scrollbar is still
present

Downscaler can be tested by running BSword2.5. 
Audio has been handled differently so in this PR will also change the
launch scripts to preload libpadsp.so

## Build details
<details>

```markdown
Backend... miyoo (SDL 1.2.15), 16bit color, high resolution, TinyGL, savegame timestamp, HQ and Edge scalers, aspect ratio correction, Lua, virtual keyboard, ENet
WARNING: Disabling engine Hpl1 because the following dependencies are unmet: OpenGL with shaders
WARNING: Disabling engine Tetraedge because the following dependencies are unmet: libtheoradec
WARNING: Disabling engine The Watchmaker because the following dependencies are unmet: OpenGL (classic)

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
    Chamber
    Chewy: Esc from F5
    Cinematique evo 1
    Magic Composer
    Crab
    Cinematique evo 2
    Lost Eden
    Cryo Omni3D games [all games]
    Macromedia Director
    Dungeon Master
    Dragon History
    Blazing Dragons
    Drascula: The Vampire Strikes Back
    Dreamweb
    Escape From Hell
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
    The Immortal
    Kingdom: The Far Reaches
    Kyra [all games]
    Labyrinth of Time
    The Last Express
    Lilliput
    Lure of the Temptress
    MacVenture
    MADE
    MADS [all games]
    Might and Magic [all games]
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
    Ultima [all games]
    V-Cruise
    Voyeur
    WAGE
    Wintermute [all games]
    Z-Vision

Engines Skipped:
    Hpl1
    Tetraedge
    The Watchmaker

WARNING: This ScummVM build contains the following UNSTABLE engines:
    Lord Avalot d'Argent
    Chamber
    Crab
    Lost Eden
    Dungeon Master
    Grim [Escape from Monkey Island]
    In Cold Blood
    The Immortal
    The Last Express
    Lilliput
    MacVenture
    MADS [MADS V2]
    Might and Magic
    Mohawk [Where in Time is Carmen Sandiego?]
    Mutation of JB
    Playground 3d: the testing and playground environment for 3d renderers
    Sludge
    Star Trek 25th Anniversary/Judgment Rites
    TestBed: the Testing framework
    Ultima [Ultima I - The First Age of Darkness]
    WAGE
    Wintermute [Wintermute3D]

Creating engines/engines.mk
Creating engines/detection_table.h
Creating engines/plugins_table.h
Creating config.h
Creating config.mk

```
</details>

---
## [cheesePizza2/Foundation-19](https://github.com/cheesePizza2/Foundation-19)@[a666b103d3...](https://github.com/cheesePizza2/Foundation-19/commit/a666b103d3adcbcc9d954d05bad4e348f0d6ffaa)
#### Friday 2023-12-22 16:49:08 by cheesePizza2

Fixes CDZ Medical Checkpoint windoors (#1386)

* changes

* fuck me

* fuck you

---
## [HMBGERDO/Paradise](https://github.com/HMBGERDO/Paradise)@[799ca4ff3f...](https://github.com/HMBGERDO/Paradise/commit/799ca4ff3f05f4f0896ecd42520794ced97f4110)
#### Friday 2023-12-22 16:59:56 by Emagged

Revert "fuck you"

This reverts commit 33cb8df86cb70d61abef01e2f4525bcbf923cfed.

---
## [tejas-nitb/coding-practice](https://github.com/tejas-nitb/coding-practice)@[7c959cec24...](https://github.com/tejas-nitb/coding-practice/commit/7c959cec244e9c4a7368dc49cf1e8477c2bf198b)
#### Friday 2023-12-22 17:59:24 by tejas-nitb

Pick up the string whose length is odd and also that should be maximum

Problem Statement : 
Kochouseph Chittilappilly went to Dhruv Zplanet , a gaming space, with his friends and played a game called “Guess the Word”.
Rules of games are –
Computer displays some strings on the screen and the player should pick one string / word if this word matches with the random word that the computer picks then the player is declared as Winner.
Kochouseph Chittilappilly’s friends played the game and no one won the game. This is Kochouseph Chittilappilly’s turn to play and he decided to must win the game.
What he observed from his friend’s game is that the computer is picking up the string whose length is odd and also that should be maximum. Due to system failure computers sometimes cannot generate odd length words. In such cases you will lose the game anyways and it displays “better luck next time”. He needs your help. Check below cases for better understand:
Sample input 0:
5 → number of strings
Hello Good morning Welcome you
Sample output 0:
morning

---
## [discourse/discourse](https://github.com/discourse/discourse)@[cbc28e8e33...](https://github.com/discourse/discourse/commit/cbc28e8e337acc740487bc9cf5c263b3eaba6493)
#### Friday 2023-12-22 18:12:46 by David Taylor

Enable Embroider/Webpack code spliting for Wizard (#24919)

(extracted from #23678)

* Move Wizard back into main app, remove Wizard addon
* Remove Wizard-related resolver or build hacks
* Install and enable `@embroider/router`
* Add "wizard" to `splitAtRoutes`

In a fully optimized Embroider app, route-based code splitting more
or less Just Work™ – install `@embroider/router`, subclass from it,
configure which routes you want to split and that's about it.

However, our app is not "fully optimized", by which I mean we are
not able to turn on all the `static*` flags.

In Embroider, "static" means "statically analyzable". Specifically
it means that all inter-dependencies between modules (files) are
explicitly expressed as `import`s, as opposed to `{{i18n ...}}`
magically means "look for the default export in app/helpers/i18n.js"
or something even more dynamic with the resolver.

Without turning on those flags, Embroider behaves conservatively,
slurps up all `app` files eagerly into the primary bundle/chunks.
So, while you _could_ turn on route-based code splitting, there
won't be much to split.

The commits leading up to this involves a bunch of refactors and
cleanups that 1) works perfectly fine in the classic build, 2) are
good and useful in their own right, but also 3) re-arranged things
such that most dependencies are now explicit.

With those in place, I was able to move all the wizard code into
the "app/static" folder. Embroider does not eagerly pull things from
this folder into any bundle, unless something explicitly "asks" for
them via `imports`. Conversely, things from this folder are not
registered with the resolver and are not added to the `loader.js`
registry.

In conjunction with route-based code splitting, we now have the
ability to split out islands of on-demand functionalities from the
main app bundle.

When you split a route in Embroider, it automatically creates a
bundle/entrypoint with the relevant routes/templates/controllers
matching that route prefix. Anything they import will be added to
the bundle as well, assuming they are not already in the main app
bundle, which is where the "app/static" folder comes into play.

The "app/static" folder name is not special. It is configured in
ember-cli-build.js. Alternatively, we could have left everything
in their normal locations, and add more fine-grained paths to the
`staticAppPaths` array. I just thought it would be easy to manage
and scale, and less error-prone to do it this way.

Note that putting things in `app/static` does not guarantee that
it would not be part of the main app bundle. For example, if we
were to add an `import ... from "app/static/wizard/...";` in a
main bundle file (say, `app.js`), then that chunk of the module
graph would be pulled in. (Consider using `await import(...)`?)

Overtime, we can build better tooling (e.g. lint rules and babel
macros to make things less repetitive) as we expand the use of
this pattern, but this is a start.

Co-authored-by: Godfrey Chan <godfreykfc@gmail.com>

---
## [samskivert/adventofcode](https://github.com/samskivert/adventofcode)@[53744151b8...](https://github.com/samskivert/adventofcode/commit/53744151b87f108083017167dc72bfc51f77ee5f)
#### Friday 2023-12-22 19:01:03 by Michael Bayne

Day 21.

Part one was straightforward. Part two was bananas.

There was _no way_ I was going to inspect the 131x131 ASCII grid that was my
input, happen to notice that it was constructed in just such a way that it
resulted in the step number growing as a simple quadratic (with x having the
special form 65+131k), and then realize that I could compute three points on
that quadratic and fit a curve to it. Riiiiight.

So yeah, I thought for a while about ways that one might solve the problem in
general, came up with nothing, looked up how other people did it, rolled my
eyes, and implemented the nice Lagrange interpolation polynomial that someone
much smarter than me posted about on Reddit.

At least the earlier days have mostly been fun. My expectation for the
remaining three days is further annoyance and frustration. Merry Christmas!

---
## [Bird-Lounge/Skyraptor-SS13](https://github.com/Bird-Lounge/Skyraptor-SS13)@[20721ddcb4...](https://github.com/Bird-Lounge/Skyraptor-SS13/commit/20721ddcb444d6d204fb9aa08704706ea4815b24)
#### Friday 2023-12-22 20:18:41 by Iamgoofball

Fixes Holy Water performing water metabolization twice, giving more blood and making you less drunk (#80440)

## About The Pull Request

~~Fixes Holy Water taking double the time it's supposed to take to
deconvert, and fixes it metabolizing out at twice the normal speed.~~

Fixes Holy Water performing water metabolization twice, giving more
blood and making you less drunk

## Why It's Good For The Game

lmfao ~~this is why deconversion for cult sucked~~ so bad

## Changelog

:cl:
fix: Fixes Holy Water giving you more blood and making you less drunk
than water normally does.
/:cl:

---
## [langchain-ai/langchain](https://github.com/langchain-ai/langchain)@[d4f45b1421...](https://github.com/langchain-ai/langchain/commit/d4f45b1421ec8b56fe6aeed84f81ca1b3f91383f)
#### Friday 2023-12-22 21:12:04 by Sypherd

core(minor): Allow explicit types for ChatMessageHistory adds (#14967)

<!-- Thank you for contributing to LangChain!

Replace this entire comment with:
  - **Description:** a description of the change, 
  - **Issue:** the issue # it fixes (if applicable),
  - **Dependencies:** any dependencies required for this change,
- **Tag maintainer:** for a quicker response, tag the relevant
maintainer (see below),
- **Twitter handle:** we announce bigger features on Twitter. If your PR
gets announced, and you'd like a mention, we'll gladly shout you out!

Please make sure your PR is passing linting and testing before
submitting. Run `make format`, `make lint` and `make test` to check this
locally.

See contribution guidelines for more information on how to write/run
tests, lint, etc:
https://python.langchain.com/docs/contributing/

If you're adding a new integration, please include:
1. a test for the integration, preferably unit tests that do not rely on
network access,
2. an example notebook showing its use. It lives in `docs/extras`
directory.

If no one reviews your PR within a few days, please @-mention one of
@baskaryan, @eyurtsev, @hwchase17.
 -->
## Description
Changes the behavior of `add_user_message` and `add_ai_message` to allow
for messages of those types to be passed in. Currently, if you want to
use the `add_user_message` or `add_ai_message` methods, you have to pass
in a string. For `add_message` on `ChatMessageHistory`, however, you
have to pass a `BaseMessage`. This behavior seems a bit inconsistent.
Personally, I'd love to be able to be explicit that I want to
`add_user_message` and pass in a `HumanMessage` without having to grab
the `content` attribute. This PR allows `add_user_message` to accept
`HumanMessage`s or `str`s and `add_ai_message` to accept `AIMessage`s or
`str`s to add that functionality and ensure backwards compatibility.

## Issue
* None

## Dependencies
* None

## Tag maintainer
@hinthornw
@baskaryan 

## Note
`make test` results in `make: *** No rule to make target 'test'.  Stop.`

---
## [Nebby1999/Starstorm2](https://github.com/Nebby1999/Starstorm2)@[a3d9f77b5d...](https://github.com/Nebby1999/Starstorm2/commit/a3d9f77b5d22029299df458125f4acd276c43448)
#### Friday 2023-12-22 21:47:18 by swuff-star

oh boy

i am going to pull jace's branch and it is going to be fine and absolutely not fuck up my branch haha lets do this!

---
## [GalaxyGamingBoy/hc-sprig](https://github.com/GalaxyGamingBoy/hc-sprig)@[924c3a0e86...](https://github.com/GalaxyGamingBoy/hc-sprig/commit/924c3a0e86174f1f511f4554d35e707d784d2564)
#### Friday 2023-12-22 22:09:36 by Akshat

add #1303

sokoban: Update metadata

Limits: Update metadata

pong: Update metadata

penguin_slide: Update metadata

laser_tag: Update metadata

15_puzzle: Update metadata

9_puzzle: Update metadata

kindless: Update metadata

color_patterns: Update metadata

matcher: Update metadata

shoot_green_blobs: Update metadata

crappy_bird: Update metadata

2048: Update metadata

flappy_bird_but_no_gravity_and_worse: Update metadata

friendship: Update metadata

getting_started: Update metadata

maze: Update metadata

pyre: Update metadata

raycasting: Update metadata

Falling_Blocks: Update metadata

reactor: Update metadata

mini_maze_and_puzzle: Update metadata

tolls: Update metadata

fogged: Update metadata

multiplayer_soccer: Update metadata

snakey_snake: Update metadata

platform_rogue: Update metadata

among_us_maze: Update metadata

256: Update metadata

minesweeper: Update metadata

connect_four: Update metadata

SprazeJS: Update metadata

nomis: Update metadata

snek: Update metadata

sokoban_plus: Update metadata

tictactoe: Update metadata

alien: Update metadata

mystery_of_scooter: Update metadata

balloon: Update metadata

purge: Update metadata

confusing_conditions: Update metadata

Virtual_Machine: Update metadata

coding_demo_1_linked_sprites: Update metadata

coding_demo_2_multiple_maps: Update metadata

coding_demo_3_custom_directions: Update metadata

coding_demo_4_screen_scroll: Update metadata

coding_demo_5_gravity: Update metadata

Rock_Paper_Scissors: Update metadata

zombie_defense: Update metadata

tetris: Update metadata

simple_maze: Update metadata

killpigs: Update metadata

TheTombOfAThousandTerrors: Update metadata

reversi: Update metadata

Flurffy: Update metadata

snake_game: Update metadata

Piano: Update metadata

desi-pong: Update metadata

Trash_IT: Update metadata

Paint_IT: Update metadata

love_lock: Update metadata

color_domination: Update metadata

infinite_maze: Update metadata

Falling_Water: Update metadata

goaled: Update metadata

2D_life: Update metadata

maze_runner: Update metadata

mandelbrot: Update metadata

Treasure_Hunt: Update metadata

LUCK: Update metadata

Breakout: Update metadata

alien_invaders: Update metadata

simon: Update metadata

gravity-is-a-thing: Update metadata

tower_of_hanoi: Update metadata

PASS_ALL: Update metadata

floppyMatch: Update metadata

maze7: Update metadata

flying_game: Update metadata

catch_orpheus: Update metadata

candy_rush: Update metadata

bolt_battle: Update metadata

Hectic_Hockey: Update metadata

puzzle_runner: Update metadata

time_puzzle: Update metadata

eat_the_cake: Update metadata

3072_A_2048_Spin-Off: Update metadata

pipes_puzzle: Update metadata

Lava_and_Water: Update metadata

Music!: Update metadata

Space_Invasion: Update metadata

Call_911: Update metadata

2048_Alphabet_Edition: Update metadata

box_maze: Update metadata

Puzzle_Game: Update metadata

BreadMaze: Update metadata

battle_bots: Update metadata

sprig_machine: Update metadata

Zooter: Update metadata

generic_dungeon_crawler: Update metadata

Tron: Update metadata

chess: Update metadata

escape_room: Update metadata

QuadraPedal: Update metadata

Bert_Blaster: Update metadata

Infinite_Shooter: Update metadata

PushBattle: Update metadata

BRICK_DODGER: Update metadata

Monty_Hall: Update metadata

Art: Update metadata

Builder: Update metadata

Apple_Skedaddle: Update metadata

inconsequential_leveldungeon: Update metadata

dihydrogen_monoxide_free_fall: Update metadata

infinite_cat: Update metadata

L0st: Update metadata

conwaysgameoflife: Update metadata

Amoeba: Update metadata

racer: Update metadata

Snake: Update metadata

push_the_blocks: Update metadata

speedy_snake: Update metadata

ever_hot: Update metadata

dual_state_machine: Update metadata

virus_plowing: Update metadata

cave_explorer: Update metadata

DogsvsCats: Update metadata

cool_platformer: Update metadata

UFO_Attack: Update metadata

the_impossible_puzzle: Update metadata

echolocation: Update metadata

SOS_Game: Update metadata

soko_quest: Update metadata

Jumper: Update metadata

Simon-WASD_Edition: Update metadata

the_invisible_man: Update metadata

Mastermind: Update metadata

Conquerers: Update metadata

Nim: Update metadata

spriggymon: Update metadata

delightful_mazes: Update metadata

Electrikoban: Update metadata

red_light_green_light: Update metadata

chuckman_go: Update metadata

Snake_4_2: Update metadata

sprigle: Update metadata

the_RUN: Update metadata

Meteor_shower: Update metadata

solar_system: Update metadata

Galacticats: Update metadata

restocker_simulater_sprig: Update metadata

BoxCubeGuy: Update metadata

Asteroid_Field: Update metadata

creepy_crush: Update metadata

loadsamoney: Update metadata

Pac-Man_But_With_Stars: Update metadata

Bottom_of_the_Barrel: Update metadata

Fish_in_the_Sea: Update metadata

Advent_of_Sprig: Update metadata

Icy_Portals: Update metadata

Jet_Box: Update metadata

music-be-like: Update metadata

Ninja_In_A_Bear_Trap_Factory: Update metadata

niabtf2: Update metadata

bbbbbb: Update metadata

Pac_Man: Update metadata

Stop: Update metadata

The_Pet: Update metadata

Temple: Update metadata

Invisible_Maze: Update metadata

Worldcraft: Update metadata

maze_runner2: Update metadata

cricket_frenzy: Update metadata

randomworld: Update metadata

sprig_dodge: Update metadata

cookie_clicker: Update metadata

lights_out: Update metadata

BigButton: Update metadata

dvd_logo_simulator: Update metadata

crimbletips: Update metadata

Mirror_Mirror: Update metadata

Box_Jump: Update metadata

BrainTeaserMaze: Update metadata

13_medium_sokoban_puzzles: Update metadata

Robot_Party_Basic_Buildv1: Update metadata

Terminal-Dungeon: Update metadata

Lava_the_impossible_maze: Update metadata

black_jack: Update metadata

hackcraft: Update metadata

gravity_fun: Update metadata

charge: Update metadata

get_the_birdie: Update metadata

sprigadventure: Update metadata

shitpest: Update metadata

Sort: Update metadata

attack_on_slimes: Update metadata

Colour_Game: Update metadata

Cross_The_Road: Update metadata

guidance: Update metadata

Dragon_Fest: Update metadata

Friendly_Figures: Update metadata

Burger_Maker_V1: Update metadata

A_Really_One_Sided_Duel: Update metadata

offline_t-rex_game: Update metadata

Asteroid_Apocalypse: Update metadata

pong-multiplayer: Update metadata

maze_bird: Update metadata

missile_mania: Update metadata

Number_Nudger: Update metadata

Protect_The_Surfer: Update metadata

font-explorer: Update metadata

Amongus_flight: Update metadata

Avoid_The_Tree: Update metadata

SprigClick: Update metadata

cube_escape: Update metadata

5-in-1-Carnival-Game-Pack!: Update metadata

CATCH-ME: Update metadata

aMAZE: Update metadata

The_Bird_Feedo: Update metadata

Battle_City: Update metadata

fractal_generator: Update metadata

cubefield: Update metadata

Let_Them_Eat_Cake: Update metadata

hot-digitty-dog: Update metadata

keyTester: Update metadata

bullet_dodge: Update metadata

Mario_Kart: Update metadata

brick_breaker: Update metadata

scrolling_maze: Update metadata

1930: Update metadata

Cookie_Click!: Update metadata

Cricket-Dodge: Update metadata

Linebeck-Land: Update metadata

Tic-Tac-Toe: Update metadata

Christmas_Themed_Sokoban: Update metadata

The_UFO_farm: Update metadata

explorer: Update metadata

Astrovoid: Update metadata

sudoku: Update metadata

spongebob_squaremaze: Update metadata

hex_hubbub: Update metadata

squarey_runs_away_from_the_fireball: Update metadata

spriggy_morse: Update metadata

son_of_a_lich: Update metadata

Fire_Hound: Update metadata

Super_Efficient_Bunny: Update metadata

Tic_Tac_Toe: Update metadata

Find_The_Suspect: Update metadata

sPaint!: Update metadata

Tic-Tac-No: Update metadata

Rolling_Obstacles: Update metadata

Super_Maze: Update metadata

under_fire: Update metadata

pusher_game: Update metadata

Sus_Runner: Update metadata

rescue_leo: Update metadata

sprig_shoot: Update metadata

The_Sky_Is_Falling_For_Real_This_Time: Update metadata

3D_wire_frame_rendererV1: Update metadata

Labyrinth: Update metadata

ValentinesGame: Update metadata

bannai-snake: Update metadata

The_Maze_of_Sprig: Update metadata

Labyrinth2: Update metadata

plants_vs_zombies: Update metadata

pocket-piano: Update metadata

Cave-Quest: Update metadata

tunnel: Update metadata

dino: Update metadata

microwars: Update metadata

wet-sand: Update metadata

RandomDungeon-final: Update metadata

bloxorz: Update metadata

Flamin_Finger: Update metadata

mathematical_meteorite: Update metadata

Street_Racer: Update metadata

connectTheDots: Update metadata

the_hungry_mouse: Update metadata

the_dining_room_in_the_sky: Update metadata

whack_a_mole: Update metadata

Labyrinth3: Update metadata

bobs_bad_apple: Update metadata

calculator: Update metadata

Memory_Test: Update metadata

Disco: Update metadata

Dodge_The_Rock: Update metadata

santas_workshop: Update metadata

Binary_Eater: Update metadata

fight_big_parma: Update metadata

girl_scouts_x_hack_club: Update metadata

CatchIt: Update metadata

fill_the_map: Update metadata

MagicalTiles: Update metadata

Alien_Attack: Update metadata

ElfSokoban: Update metadata

It_Is_Coming_Out!: Update metadata

Maze_Runner3: Update metadata

TwinPrimeRockets: Update metadata

Duck_Hunt: Update metadata

rickroll: Update metadata

Physics_Sandbox: Update metadata

chase_bob: Update metadata

air_hockey: Update metadata

Mining_Simulator: Update metadata

AmongTheStars: Update metadata

the_journey_of_the_box_a_sokoban_saga: Update metadata

RougeColors: Update metadata

space-invaders: Update metadata

Super_Hard_Puzzle_challenges: Update metadata

calculator_puzzle: Update metadata

Mad_city: Update metadata

Meteor_Dodge: Update metadata

Bash_Game: Update metadata

FRC_TEAM_2016_Monkey_Madness: Update metadata

Antivirus: Update metadata

portal_game: Update metadata

hangman: Update metadata

hidden_maze: Update metadata

Pet_the_Cat: Update metadata

hidden_maze_infinite: Update metadata

fungi-frog-maze: Update metadata

drab_bullets: Update metadata

Spike_Avoider: Update metadata

Maths_Speedrun: Update metadata

Recycling_Turtle: Update metadata

Golem-Rush: Update metadata

galloping: Update metadata

hidden_maze_escape: Update metadata

Operation_Ocean: Update metadata

Mirror_Snake: Update metadata

Minigame-Mania: Update metadata

DontGetBurnt: Update metadata

The_Story_of_Grass: Update metadata

Womens_roles_during_wartime: Update metadata

Defend_the_Keep: Update metadata

Watermellen_man_and_bluebarry_man: Update metadata

two-birds_one-stone: Update metadata

Civilization_Builder: Update metadata

MyForestMaze: Update metadata

Sprig_Boy: Update metadata

really_really_bad_music_maker: Update metadata

parachute_panic: Update metadata

ROOM: Update metadata

Kalo: Update metadata

skyrace: Update metadata

Dragon-Rush: Update metadata

run: Update metadata

chain_remove: Update metadata

Amazing_Mazes: Update metadata

Maze_Escape: Update metadata

breakfast_maze!: Update metadata

thunder_bowl: Update metadata

Asteroid_Dodge: Update metadata

maze_game_starter: Update metadata

4_Colour_Drawing: Update metadata

Dynamic_Adventure: Update metadata

burger_build: Update metadata

Sprigressbar: Update metadata

Battleship: Update metadata

The_Legend_of_Zelda-Links_Escape: Update metadata

spirit-bound: Update metadata

FOOD-CATCH: Update metadata

mailman: Update metadata

Tic_Tac_GPT: Update metadata

ding_dong-delivery: Update metadata

flappysprig: Update metadata

Two_Player_Tetris: Update metadata

killer_training: Update metadata

wham: Update metadata

fire_boom: Update metadata

Space-war: Update metadata

far-from-home: Update metadata

find_the_watermelon: Update metadata

spider_home: Update metadata

Destroy_The_Hearts: Update metadata

ocean-maze-escape: Update metadata

learn_morse: Update metadata

The_Legend_Of_Sprig: Update metadata

Swapper: Update metadata

gravity_box: Update metadata

for_Squiggly_myLost_worm: Update metadata

basketballgame: Update metadata

bastion: Update metadata

Boxxod: Update metadata

Mario_Platformer_v2: Update metadata

zap: Update metadata

Knight_Post: Update metadata

shooter: Update metadata

Musi: Update metadata

galactic_coconuts: Update metadata

Custom_Tic_Tac_Toe: Update metadata

collectcandy: Update metadata

mazegame: Update metadata

galactic: Update metadata

BoxMaze: Update metadata

cat_in_rain: Update metadata

Desine_Mini: Update metadata

Space_Odyssey: Update metadata

Tile_Slider: Update metadata

Push_The_Box: Update metadata

compudino: Update metadata

bob_and_joe: Update metadata

bomb_dodge: Update metadata

StickRunner: Update metadata

DoNotConsumeEmptyBowls: Update metadata

Hungry-Ninja: Update metadata

Hard-Hat_Helper: Update metadata

Morse_trainer: Update metadata

starjump: Update metadata

move_the_rocks: Update metadata

Sprig_Fighter: Update metadata

youndus_Arrow.js - Update metadata

Eat_&_Don't_Be_Eaten.js - Update metadata

seven_ate_nine_(789).js - Update metadata

turtle_game_(reach_the_beach).js - Update metadata

Orpheus_Burger_dash.js - Update metadata

---
## [patrick-kidger/optimistix](https://github.com/patrick-kidger/optimistix)@[b2c7c2a05f...](https://github.com/patrick-kidger/optimistix/commit/b2c7c2a05f8664e9531cfef8c9612535905f85c8)
#### Friday 2023-12-22 23:09:23 by Patrick Kidger

Now using the same jaxpr in the state.

This is quite an important fix!

The bit that matters here is that the `f_eval_info.jac` in
`AbstractGaussNewton.step` now throws away its static (non-array) parts
of its PyTree, and instead uses the equivalent static (non-array) parts
of `state.f_info.jac`, i.e. as were computed in
`AbstractGaussNewton.init`.

Now at a logical level this shouldn't matter at all: the static pieces
should be the same in both cases, as they're just the output of
`_make_f_info` with similarly-structured inputs.

However, `_make_f_info` calls `lx.FunctionLinearOperator` which calls
`eqx.filter_closure_convert` which calls `jax.make_jaxpr` which returns
a jaxpr... and so between the two calls to `_make_f_info`, we actually
end up with two jaxprs. Both encode the same program, but are two
different Python objects. Now jaxprs have `__eq__` defined according to
identity, so these two (functionally identical) jaxprs do not compare
as equal.

Previously we worked around this inside `_iterate.py`: we carefully
removed or wrapped any jaxprs before anything that would try to compare
them for equality. This was a bit ugly, but it worked.

However, it turns out that this still left a problem when manually
stepping an Optimistix solver! (In a way akin to an Optax solver:
something like
```python
@eqx.filter_jit
def make_step(...):
    ... = solver.step(...)

for ... in ...:  # Python level for-loop
    ... = make_step(...)
```
)
then in fact on every iteration of the Python loop, we would end up
recompiling, as we always gets a new jaxpr at
```
state      # state for the Gauss-Newton solver
  .f_info  # as returned by _make_f_info
  .jac     # the FunctionLinearOperator
  .fn      # the closure-converted function
  .jaxpr   # the jaxpr from the closure conversion
```
!

Now one fix is simply to demand that manually stepping a solver
requires similar hackery as we had in `_iterate.py`. But maybe enough
is enough, and we should try doing something better instead: that is,
we do what this PR does, and just preserves the same jaxpr all the way
through.

For bonus points, this means that we can now remove our special jaxpr
handling from `_iterate.py` (and from `filter_cond`, which also needed
this for the same reason).

Finally, you might be wondering: why do we need to trace two equivalent
jaxprs at all? This seems inefficient -- can we arrange to trace it
just once? The answer is "probably, but not in this PR". This seems to
require that (a) Lineax offer a way to turn off closure conversion
(done in https://github.com/google/lineax/pull/71), but that (b) when
using this, this still seems to trigger a similar issue in JAX, that
the primal and tangent results from `jax.custom_jvp` match. So for now
this is just something to try and tackle later -- once we do, we'll get
slightly better compile times.

---
## [sojourn-13/sojourn-station](https://github.com/sojourn-13/sojourn-station)@[762705eff9...](https://github.com/sojourn-13/sojourn-station/commit/762705eff975e6acaed923eb24d1225bc50f9978)
#### Friday 2023-12-22 23:14:21 by CDB

Defib revert (#4891)

* Update defib.dm

This is very likely going to flourish into a whole ream of medical tweaks but for now starting with this because it's been bugging me.

Reverts the defib brainloss revive cap, defibs no longer check your braindamage value as a part of the process of determining if you can be defibb'd.  They only check if you have a brain, a ckey and if you need to be nanopaste'd.

This does mean the bug where you can be revived with a "dead" brain(and thus brought back in an "incomplete" form) is probably back and I'll tackle that shit later since it requires more in depth messing with. I'd like to ask that you fuckers *not* bypass this penalty by running to cryo and then coming right back up.

* Medical map changes

New storage closet for medical in the lower area, includes a lathe with some basic materials,(plus a lethals disk so SLT stop dying when they wrongly choose the bullpip primary.) basic medical disks, recharger, smartfridge(in case you want to put hyperzine away from the main floor.), and wall storage locker.

Relocates many of the most commonly pilfered medical stuff to this single closet. The medkits, defib(which now has a spare cell that actually matches it.)

Also gives medical a couple jars of bare-minimum meds in said closet.

Medical blood-freezer is still in the main area for obvious reasons however it now has access requirements.

Adds a few missing total lockdown shutters for medical.

Moves the medbay-lower break room(the lil tiiny one), adds a new hallway between lower med and lower research - puts the tiny breakroom there.

Medical rejoice, replaces the flimsy thin railings in the substation with reinforced orange railings. Roaches/spiders can no longer just fall down into that little glass area(Though people can still vault it fairly easily.)

Shrinks the medical shower from 4 stalls to 2.

* Revert "Medical map changes"

This reverts commit d62882ece7e0bd141c3347ff0cdbff21b67b052c.

* SLT buffs

SLTs can now select a Humility as their starting main-arm. It comes with the weapon preloaded and one spare cell.

Humility additionally no longer uses large cells, who tfs idea was this? switches it back to medium and lowers the charge cost to 100. No more 40 magazine shotgun jfc.

Gas mask added to SLT locker.

SLTs now begin with a pair of sterile shock gloves, complete with a kinda okay coder sprite. For removing particularly rude people from medical.

Removes the erroneous insulation on the regal gloves.

* HG

* Update stungloves.dm

fixes an incomplete desc.

---
## [f13babylon/f13babylon](https://github.com/f13babylon/f13babylon)@[fc41127084...](https://github.com/f13babylon/f13babylon/commit/fc41127084c96e75ed37c1e51c6ad9d2305da643)
#### Friday 2023-12-22 23:53:46 by Stutternov

Shield Change (As Requested) (#381)

## About The Pull Request

Was requested to do this upon issues with shields. 

So, before some shields literally had the health of Bubblegum + armor on
them as well. The health has been greatly reduced on some, some others
have been buffed at lower end.

Telescopic shield has also been removed since it's busted as hell, had
2250 health, tons of armor, and such.

## Why It's Good For The Game

Some shields that were even labeled as removed were still in the game,
like the Telescopic. Others got buffed by someone last week for some
reason despite stam damage being fucked, etc.

## Pre-Merge Checklist
<!-- Don't bother filling these in while creating your Pull Request,
just click the checkboxes after the Pull Request is opened and you are
redirected to the page. -->
- [ ] You tested this on a local server.
- [ ] This code did not runtime during testing.
- [ ] You documented all of your changes.
<!-- Neither the compiler nor workflow checks are perfect at detecting
runtimes and errors. It is important to test your code/feature/fix
locally. -->


## Changelog
<!-- This is mostly optional for small Pull Requests, but if you value
being credited for your work in-game be sure to fill it out. To opt-out,
remove everything below including the start and end :cl: brackets. -->

<!-- If your Pull Request includes a minor single line variable edit,
probably do not fill out this changelog. -->
<!-- However, if your pull request includes massive or immediately
noticeable changes, briefly describe those changes in some way in this
changelog. -->

:cl:
balance: Rebalances shields integrity.
removes: Telescopic shield (Use the riot, it's identical but just not
telescopic.)
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [HalcyonicWolf/Skyrat-tg](https://github.com/HalcyonicWolf/Skyrat-tg)@[e8cf56dcb2...](https://github.com/HalcyonicWolf/Skyrat-tg/commit/e8cf56dcb2553c842abd7adf60a99b33d65ecfbe)
#### Friday 2023-12-22 23:56:42 by SkyratBot

[MIRROR] Roundstart AIs are positronic [MDB IGNORE] (#25679)

* Roundstart AIs are positronic (#80355)

## About The Pull Request

If you disassemble an AI which was in the round from the start it will
produce a Positronic Cube rather than an MMI with the brain of that
player's usual human character in it.

Also I made changes to a couple of feedback balloon alerts which would
always trigger a runtime when constructing or deconstructing an AI, this
was because balloon alerts have a small time delay before executing and
we deleted the AI mob or structure after trying to show a balloon alert
on them, so they'd never appear.

## Why It's Good For The Game

Honestly this is _mostly_ about vibes, it has annoyed me since AI
deconstruction was added that Nanotrasen AIs tend to actually be brains
in jars rather than AIs. Now they're artifical.
It does also mean that you can't deconstruct the AI and then put its
brain into a human body, which is similarly mostly bad because of vibes:
If you sign up as an AI I think you should be an AI or a cyborg even
after deconstruction.

It also universally looks really stupid when you deconstruct an AI and
it says it has the brain of Penelope Dreadful in there, like should I
expect them to start RPing as their normal character instead of the AI
they have been playing all round now?

## Changelog

:cl:
balance: Roundstart AIs are now made of positronic cubes, rather than
brains inside MMIs
/:cl:

---------

Co-authored-by: John Willard <53777086+JohnFulpWillard@ users.noreply.github.com>

* Roundstart AIs are positronic

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>
Co-authored-by: John Willard <53777086+JohnFulpWillard@ users.noreply.github.com>

---

