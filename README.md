## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-12-20](docs/good-messages/2023/2023-12-20.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,500,469 were push events containing 3,723,541 commit messages that amount to 308,183,319 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 69 messages:


## [crawl/crawl](https://github.com/crawl/crawl)@[8f7eaaa2f0...](https://github.com/crawl/crawl/commit/8f7eaaa2f0678ffbf35011348680be2dee9ef664)
#### Wednesday 2023-12-20 00:00:05 by DracoOmega

Merge Poison Magic and Transmutations into a single school: Alchemy

When forms were removed from Transmutations to create
talismans/shapeshifting, the Transmutations school was left in a slightly
awkward state. It still contained multiple strong and useful spells (eg:
Irradiate and Yara's) but was a little thin on the whole, especially at
lower levels, and lacked natural inroads. And Poison Magic has long had
issues with being overly narrow in thematic scope compared to other
schools, as well as lacking exciting lategame spells.

This merger attempts to improve both issues at once and open up more
interesting future design space by combining the two schools into one:
Alchemy. This makes several higher level transmutations spells more natural
to access, give the Venom Mage start (now Alchemist) more lategame things
to look forward to, and potentially allows for the design of more varied
means of doing damage than poison.

All spells that were either Transmutations or Poison are now Alchemy,
with the following notes:
 -Ignite Poison moved to level 4 since it's now 2 schools instead of 3.
 -Eringya's Noxious Bog was left at level 6, despite becoming single-school
  since it's already widely considered unappealing and this might help it.
 -Sting became Conjurations/Alchemy.
 -Wereblood is slated to be rethemed and moved to Necromancy, but isn't yet.

Most species aptitudes for Transmutations and Poison Magic were already the
same. Cases where that was not the case are listed below.

--------------------------------
Transmutation/Poison -> Alchemy

Demonspawn: -1/0 -> 0
Felid: 1/-1 -> -1
Formicid: 1/3 -> 3
Gargoyle: -2/0 -> -2
Ghoul: -1/0 -> -1
Hill Orc: -3/-1 -> -2
Merfolk: 3/1 -> 3
Minotaur -2/-3 -> -3
Naga: 0/3 -> 2
Octopode: 0/2 -> 1
Spriggan: 3/0 -> 1
Tengu: -2/0 -> -1
Vampire: 1/-1 -> 1
--------------------------------

This vaguely averages apts, with a slight bias for the original poison
skill (and some personal subjective opinion here and there). Formicids and
Merfolk both keep their +3 poison apt - the former because it can easily
handle the buff, the latter because it's just too good to let merfolk make
their own bogs to swim in. Felid apts are in line with their other
offensive-focused magic skills, Gargoyles inflexible nature makes them
less adept at inducing change in others, and Vampires have traditional
thematics around transformation that makes a +1 feel appropriate to me.

Ashenzari's Curse of Beguiling loses Conjurations, and the old Curse of
Alchemy is renamed Curse of Sorcery (Conjurations + Alchemy).

Alchemy miscasts inflict the poison status on the player. (I kind of
prefer the idea of them inflicting corrosion instead, though no player
Alchemy spell can yet do this, so I'm not sure how people would feel).
Messages are provisional, but frankly the miscast system in general has
issues with the fact that messages cannot check player properties (cf:
ghouls getting messages about how they violently convulse in pain, then
take 0 damage) and could use separate work.

The Plutonium Sword is decoupled from transmutation miscasts (which no
longer exist). I have also added back a vague approximation of the
direct damage they used to inflict before the big miscast simplification
of a couple years back.

Save upgrading will grant players Alchemy skill equivalent to the sum of
old Poison and Transmutation skills.

Alchemy randbook words are a partial merger of old Poison and
Transmutation book words, with heavy cutting, curating, and addition of
things. (I tried to prune things directly associated with shapeshifting,
as well as poison words that seemed too close to disease and putrescence
in a 'gross' sense - instead trying to lean into a more academic vibe for
such things. Also added a decent handful of specifically-alchemical
references.)

Still slightly awkward that it can use poison words for a book containing
no spells that poison, but probably no worse than randbooks often are.

(Gloorx can stay as a high-level alchemist. Hot new DCSS lore!)

---
## [crawl/crawl](https://github.com/crawl/crawl)@[cae00c0fb1...](https://github.com/crawl/crawl/commit/cae00c0fb1febd50125cb22469d0abc9ffebdaa7)
#### Wednesday 2023-12-20 00:00:05 by DracoOmega

Shuffle spellbooks a bunch

The book of Changes was incredibly sad (and nonsensically named) with just
Sting and Irradiate, and attempting to touch this up caused a chain
reaction (which hopefully still improves the status quo).

Unrestrained Analects loses Ignition and gains Ozocubu's Refrigeration.

Book of Battle returns, with Ozocubu's Armour, Manifold Assault, and
Fugue of the Fallen.

Book of Changes renamed to Book of Spontaneous Combustion, containing
Inner Flame, Irradiate, and Ignition.

Book of Alchemy renamed to the book of Transmutation (but contains the
same spells as before).

Book of Minor Magic lost Mephitic Cloud and gained Blink.

Book of the Senses gained Mephitic Cloud.

Book of Blood gained Call Imp (since apparently there was only one book
that had a copy of it)

Book of Cantrips gains Sting.

Book of Death loses Fugue of the Fallen.

Book of Misfortune loses Inner Flame to gain Jinxbite.

Book of Danerous Friends loses Jinxbite.

Ozocubu's Autobiography and the Inescapable Atlas were cut. The latter's
description didn't really make any flavor sense with its spell set of Blink
and Manifold Assault. It's a shame to lose two of the best book
descriptions, so I adapted most of the former for Book of Battle.

Trismegistus Codex loses the joke about all its spells having 3 schools,
but the only other 3 school spell remaining is Mephitic Cloud which already
shares another book with Freezing Cloud. Alas.

---
## [crawl/crawl](https://github.com/crawl/crawl)@[614289c723...](https://github.com/crawl/crawl/commit/614289c72386821faeecdd77f07cdc0aac8e5333)
#### Wednesday 2023-12-20 00:00:05 by DracoOmega

Wereblood -> Fugue of the Fallen (level 3 Necromancy)

Wereblood has had somewhat weird thematics ever since Shapeshifting took
over all of the 'transform self' effects from Transmutations. Necromancy,
on the other hand, is a natural fit for a spell that is powered by killing
things.

This has the following mechanical changes over current Wereblood:
 -The healing effect is removed
 -Ally kills now boost the effect (but allies themselves do not benefit
  from it in any way)
 -Max stacks reduced to 7 instead of 9
 -At maximum stacks, successful hits will inflict minor pain damage to all
  adjacent targets to the one you attacked. A little bonus for the tricky
  task of maxing it!
 -Moved to level 3

I haven't put this in the necromancy starter book. Wereblood was never great
at low levels, since you usually can't sustain fights long enough to build
it and struggle to kill already. I think there's no way a necromancy wants
to use their mp on this instead of vampiric draining, and it's more
interesting if the spell is intended for later use. Also: this gives players
more incentive to splash necromancy on a hybrid that doesn't involve allies!

To avoid the player needing to worry about whether any individual monster
they kill has a 'soul' or whatever, the spell is themed as using fresh
death to draw in the spirits of the long-dead that already linger everywhere
in the dungeon (I mean, there's enough corpses in every inch of the dungeon
that BVC works, right? :P)

---
## [proofcarryingdata/zupass](https://github.com/proofcarryingdata/zupass)@[2eabbc11a3...](https://github.com/proofcarryingdata/zupass/commit/2eabbc11a35f34f399781aa87fe56146159b6996)
#### Wednesday 2023-12-20 00:00:58 by Rob Knight

Fix packaging and show example usage with different bundlers (#1260)

Fixes #965 
Fixes #1136
Fixes #421 

Various third party/hackathon users reported issues when importing our
packages.

Some major categories:
1) Packages include typescript source, and using them means compiling
the typescript source, which requires having a bunch of type packages
installed (e.g. https://github.com/proofcarryingdata/zupass/issues/1136)
2) Our builds only support certain package resolution strategies, which
was an issue for the ZuAstro team as they were trying to use code from
the Jubmoji team, which also only supported certain package resolution
strategies, but not the same ones that we do
3) The passport-interface nightmare

In addition, using CommonJS rather than ESM by default causes some
inflation of our bundle size, as esbuild can't do tree-shaking on
CommonJS packages. The current version of this branch cuts
`passport-client` bundle size from 7.7mb to 7.1mb as a result of using
ESM packages wherever possible.

Before: 
<img width="458" alt="image"
src="https://github.com/proofcarryingdata/zupass/assets/20022/ae5c49a5-d9d0-40d0-a12a-b0d32f1c0334">

After:
<img width="475" alt="image"
src="https://github.com/proofcarryingdata/zupass/assets/20022/e2f64335-e2c6-4cdd-977c-e0e1c42c8c13">

In this branch, we have configuration to do both ESM and CommonJS builds
of all packages, and some builds have both node and browser variants.
Each package also generates a separate TypeScript definition file,
rather than bundling the whole TypeScript source. This makes the build
process take longer than it used to, though it also means that we can
eliminate the separate type-checking phase of CI, since generating the
definitions performs the same task and will flag up the same errors.

Most modules worked without any changes to the TypeScript source, or
without any module-specific configuration, but there were a couple of
exceptions in cases where we import third-party modules with some
quirks. In these cases we can provide some configuration that saves the
users of our packages from having to deal with these quirks themselves.

I've also added example apps for NextJS, Vite, Create-React-App
(Webpack) and a server-side Express app that uses ESBuild. This shows
that the packages work in a variety of different environments and
configurations. There are probably still edge cases I haven't caught,
but this covers all of the types of project I've seen people try to
build.

This has been tested locally using a local NPM package mirror, with
modified packages but no version number change. If we merge this then we
should bump all of the package version numbers and update the examples
to use these.

## Overview of changes

`apps/anon-message-client` has been changed to remove the hacks
previously necessary for `passport-interface` to work.

`examples/*` includes various example apps. The overwhelming majority of
the code in this PR is just the source for these examples.

`packages/*` - each package now has updated configuration for how it
ought to be bundled, and a changed `build` command in `package.json`.
`passport-ui` and `passport-crypto` have some other fixes that resolved
some bundling issues, but no modules have large changes to their
content. `styled-components` has some specific issues when bundled using
ESM, which made it necessary to wrap it in `passport-ui` and then use
this wrapper in the PCD packages, but this introduces no new
dependencies for the affected packages since they depended on
`passport-ui` anyway.

## How to test

Run `./test-packaing.sh`.

This will:
- Run Verdaccio locally using the config in `verdaccio.yml`
- Publish all `@pcd` packages to Verdaccio
- Reinstall each example app with Verdaccio as the registry, meaning
that it will use the locally-published `@pcd` packages. Third-party
packages will be proxied from `yarnkpkg` as per the Verdaccio config.
- Build each example app. The script will fail if any command fails.

This is a bit slow as it needs to download the packages each time, but
it does give a faithful reproduction of the third-part developer
experience.

Todo:
- [x] Try pushing these packages to npm under a different name, to see
if they work properly when imported
- [x] Test with NextJS
- [x] Test with create-react-app
- [x] Test with vanilla Express
- [x] Test with Vite

---
## [alexbaden/llvm-project](https://github.com/alexbaden/llvm-project)@[b70824c1b8...](https://github.com/alexbaden/llvm-project/commit/b70824c1b84296eba4a6e209820b82829a10f534)
#### Wednesday 2023-12-20 00:01:54 by Rafael Espindola

Revert r318924 Skip over empty sections when checking for contiguous relro

PR35478 https://bugs.llvm.org/show_bug.cgi?id=35478 points out a flaw
in the implementation of r318924 from D40364. The implementation
depends on the Size field being set or the SyntheticSection::empty()
being accurate. These functions are not reliable as some linker script
commands that have yet to be processed may affect the results, causing
some non-zero size sections to be reported as zero size.

I think the first step is to revert r318924 and come up with a better
solution for the underlying problem rather than trying to layer more
heuristics onto the zero sized output section.

Chances are I'll be out of office by the time anyone sees this so feel
free to commit the revert if you agree with me.

Fixes PR35478

Current thoughts on the underlying problem:

Revisiting the motivation for adding the zero size check in the first
place; it was to prevent 0 sized SyntheticSections that a user does
not have full control over from needlessly breaking the PT_GNU_RELRO,
rather than trying to accommodate arbitrarily complex linker
scripts. Looking at the code, it looks like
removeUnusedSyntheticSections() should remove zero sized synthetic
sections. It does, but it doesn't set the Parent to nullptr, this has
the side effect that Sec == InX::BssRelRo->getParent() will make the
parent OutputSection of InX::BssRelRo RelRo even if there is no
InX::BssRelRo.

I tried a quick experiment with setting the Parent to nullptr and this
flushed out a few interesting test failures, it feels like playing
Jenga with every change:

    In the isRelroSection() we have to consider the case where there
    is no .plt and .plt.got but there is a ifunc plt with accompanying
    (ifunc .got or .plt.got)

    The PPC64 has PltHeaderSize == 0. Unfortunately HeaderSize == 0 is
    used to choose between the ifunc plt or normal plt. We seem to get
    away with this at the moment, but tests start to fail when Parent
    is set to nullptr for the .got.plt.

    The InX::BssRelRo and InX::Bss never get their sizes set and they
    are always removed by removeUnusedSyntheticSections(), their
    purpose seems to be as some kind of proxy for add .bss or
    .bss.relro InputSections into their parent OutputSections, they
    therefore don't behave like other SyntheticSections anyway.

My thinking is that some work is needed to make sure that the Sec ==
SyntheticSection->getParent() does a bit more checking before
returning true, particularly for InX::BssRelRo as that has special
behaviour. I'll hope to post something for review as soon as possible.

Patch by Peter Smith!

llvm-svn: 319563

---
## [Generalcamo/Aurora.3](https://github.com/Generalcamo/Aurora.3)@[13eb8af093...](https://github.com/Generalcamo/Aurora.3/commit/13eb8af093447e13b6555a741d6cd9e3a9dc3fbc)
#### Wednesday 2023-12-20 00:06:38 by RustingWithYou

air konyang ship (#17540)

it's a shuttle now, im gonna kms

smaller so it can fit

desperately cramming into shuttle guidelines

changelog & placeholder comments

chairs

name & mapping fixes

dme fix

carpet

new airlocks

entry points?

cries, shits

a

unit test group

fuck

ghuh

hguh

hate

fixes stupid problems

area flags

---
## [alexbaden/llvm-project](https://github.com/alexbaden/llvm-project)@[9872ea4ed1...](https://github.com/alexbaden/llvm-project/commit/9872ea4ed1de4c49300430e4f1f4dfc110a79ab9)
#### Wednesday 2023-12-20 00:23:59 by Roman Lebedev

[clang][CodeGen] Implicit Conversion Sanitizer: handle increment/decrement (PR44054)

Summary:
Implicit Conversion Sanitizer is *almost* feature complete.
There aren't *that* much unsanitized things left,
two major ones are increment/decrement (this patch) and bit fields.

As it was discussed in
[[ https://bugs.llvm.org/show_bug.cgi?id=39519 | PR39519 ]],
unlike `CompoundAssignOperator` (which is promoted internally),
or `BinaryOperator` (for which we always have promotion/demotion in AST)
or parts of `UnaryOperator` (we have promotion/demotion but only for
certain operations), for inc/dec, clang omits promotion/demotion
altogether, under as-if rule.

This is technically correct: https://rise4fun.com/Alive/zPgD
As it can be seen in `InstCombineCasts.cpp` `canEvaluateTruncated()`,
`add`/`sub`/`mul`/`and`/`or`/`xor` operators can all arbitrarily
be extended or truncated:
https://github.com/llvm/llvm-project/blob/901cd3b3f62d0c700e5d2c3f97eff97d634bec5e/llvm/lib/Transforms/InstCombine/InstCombineCasts.cpp#L1320-L1334

But that has serious implications:
1. Since we no longer model implicit casts, do we pessimise
   their AST representation and everything that uses it?
2. There is no demotion, so lossy demotion sanitizer does not trigger :]

Now, i'm not going to argue about the first problem here,
but the second one **needs** to be addressed. As it was stated
in the report, this is done intentionally, so changing
this in all modes would be considered a penalization/regression.
Which means, the sanitization-less codegen must not be altered.

It was also suggested to not change the sanitized codegen
to the one with demotion, but i quite strongly believe
that will not be the wise choice here:
1. One will need to re-engineer the check that the inc/dec was lossy
   in terms of `@llvm.{u,s}{add,sub}.with.overflow` builtins
2. We will still need to compute the result we would lossily demote.
   (i.e. the result of wide `add`ition/`sub`traction)
3. I suspect it would need to be done right here, in sanitization.
   Which kinda defeats the point of
   using `@llvm.{u,s}{add,sub}.with.overflow` builtins:
   we'd have two `add`s with basically the same arguments,
   one of which is used for check+error-less codepath and other one
   for the error reporting. That seems worse than a single wide op+check.
4. OR, we would need to do that in the compiler-rt handler.
   Which means we'll need a whole new handler.
   But then what about the `CompoundAssignOperator`,
   it would also be applicable for it.
   So this also doesn't really seem like the right path to me.
5. At least X86 (but likely others) pessimizes all sub-`i32` operations
   (due to partial register stalls), so even if we avoid promotion+demotion,
   the computations will //likely// be performed in `i32` anyways.

So i'm not really seeing much benefit of
not doing the straight-forward thing.

While looking into this, i have noticed a few more LLVM middle-end
missed canonicalizations, and filed
[[ https://bugs.llvm.org/show_bug.cgi?id=44100 | PR44100 ]],
[[ https://bugs.llvm.org/show_bug.cgi?id=44102 | PR44102 ]].

Those are not specific to inc/dec, we also have them for
`CompoundAssignOperator`, and it can happen for normal arithmetics, too.
But if we take some other path in the patch, it will not be applicable
here, and we will have most likely played ourselves.

TLDR: front-end should emit canonical, easy-to-optimize yet
un-optimized code. It is middle-end's job to make it optimal.

I'm really hoping reviewers agree with my personal assessment
of the path this patch should take..

Fixes [[ https://bugs.llvm.org/show_bug.cgi?id=44054 | PR44054 ]].

Reviewers: rjmccall, erichkeane, rsmith, vsk

Reviewed By: erichkeane

Subscribers: mehdi_amini, dexonsmith, cfe-commits, #sanitizers, llvm-commits, aaron.ballman, t.p.northover, efriedma, regehr

Tags: #llvm, #clang, #sanitizers

Differential Revision: https://reviews.llvm.org/D70539

---
## [alexbaden/llvm-project](https://github.com/alexbaden/llvm-project)@[32c8da41dc...](https://github.com/alexbaden/llvm-project/commit/32c8da41dc0cb99651823a1a21130c2cbdf688e1)
#### Wednesday 2023-12-20 00:34:20 by Raphael Isemann

[lldb] Don't infinite loop in SemaSourceWithPriorities::CompleteType when trying to complete a forward decl

SemaSourceWithPriorities is a special SemaSource that wraps our normal LLDB
ExternalASTSource and the ASTReader (which is used for the C++ module loading).
It's only active when the `import-std-module` setting is turned on.

The `CompleteType` function there in `SemaSourceWithPriorities` is looping over
all ExternalASTSources and asks each to complete the type. However, that loop is
in another loop that keeps doing that until the type is complete. If that
function is ever called on a type that is a forward decl then that causes LLDB
to go into an infinite loop.

I remember I added that second loop and the comment because I thought I saw a
similar pattern in some other Clang code, but after some grepping I can't find
that code anywhere and it seems the rest of the code base only calls
CompleteType once (It would also be kinda silly to have calling it multiple
times). So it seems that's just a silly mistake.

The is implicitly tested by importing `std::pair`, but I also added a simpler
dedicated test that creates a dummy libc++ module with some forward declarations
and then imports them into the scratch AST context. At some point the
ASTImporter will check if one of the forward decls could be completed by the
ExternalASTSource, which will cause the `SemaSourceWithPriorities` to go into an
infinite loop once it receives the `CompleteType` call.

Reviewed By: shafik

Differential Revision: https://reviews.llvm.org/D87289

---
## [feartheblackout/Aurora.3](https://github.com/feartheblackout/Aurora.3)@[bc66a212d7...](https://github.com/feartheblackout/Aurora.3/commit/bc66a212d771eef33ae88445ebe4462ee25bde17)
#### Wednesday 2023-12-20 00:37:46 by RustingWithYou

Hephaestus Security Ship & Corporate Voidsuit Tweaks (#17962)

* hephaestus security ship

* fuck off

* welcome mesgaes

* lattice hell

* damn you kaizr

* cabinet

---
## [Badeklubben/Badeklubben](https://github.com/Badeklubben/Badeklubben)@[54bb604822...](https://github.com/Badeklubben/Badeklubben/commit/54bb604822f09569df74337632d231bbc9e35806)
#### Wednesday 2023-12-20 00:46:36 by X104n

OMG i fucking hate CSS, please someone save from this sin

---
## [alexbaden/llvm-project](https://github.com/alexbaden/llvm-project)@[c2c259224b...](https://github.com/alexbaden/llvm-project/commit/c2c259224bb30b089206dd69dc44aefddffec2f4)
#### Wednesday 2023-12-20 00:57:13 by Amaury Séchet

const char* for LLVMTargetMachineEmitToFile's argument

The `LLVMTargetMachineEmitToFile` takes a `char* Filename` right now, but it doesn't modify it.
This is annoying to use in the case where you want to pass a const string, because you either have to remove the const, or copy it somewhere else and pass that. Either way, it's not very nice.

I added a const and clang formatted it. This shouldn't break any ABI in my opinion.
I'm sorry but I didn't know whom to put as reviewer for this, so I chose someone with a lot of commits from the .cpp file.

Reviewed By: deadalnix

Differential Revision: https://reviews.llvm.org/D124453

---
## [RobinHeidenis/aoc-2023](https://github.com/RobinHeidenis/aoc-2023)@[b4c4a3934d...](https://github.com/RobinHeidenis/aoc-2023/commit/b4c4a3934d34f565592fcc18e0231a713277dcea)
#### Wednesday 2023-12-20 01:08:04 by Robin Heidenis

feat: 🎸 add day 18, part A and B

This one was not that difficult, but I did learn about the shoelace
formula. That was pretty interesting, getting that one to work. I also
had lots of fun with CRLF and LF (LF wins always btw, microsoft pls
fix). In CRLF my parsing didn't work, and so it would spit out the wrong
answer. We love to see it. Anyway, it's all good now. I hope you had a
great day, keep up the great work!

---
## [techthiyanes/evals](https://github.com/techthiyanes/evals)@[db8b3dfe6f...](https://github.com/techthiyanes/evals/commit/db8b3dfe6f69450577314bba40582bfa41bd06a9)
#### Wednesday 2023-12-20 01:45:28 by Thiago M. Nóbrega

Add A is B and B is A Eval (#1366)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name

ab

### Eval description

This evaluation aims to assess the model's ability to correctly identify
and understand the relationship between two entities, where A is a
specific entity (which could be a chemical element, a painting, a bird
species, a star, a mountain, a novel, a river, or a musical instrument)
and B is a unique characteristic or fact about that entity. The model
should be able to accurately interpret the user's query about the entity
(A) and provide a relevant fact (B), and vice versa. This evaluation
will help in fine-tuning the model's understanding of context, relation
between entities, and its ability to provide accurate and relevant
responses. The entities and their characteristics have been chosen to be
specific and challenging.

### What makes this a useful eval?

This evaluation is important for several reasons:

1. Contextual Understanding: It tests the model's ability to understand
the context of a conversation, particularly the relationship between two
related entities (A and B).

2. Accuracy: It assesses the model's ability to provide accurate and
relevant information based on the user's query.

3. Relevance: It evaluates the model's ability to understand the
relevance of A to B and vice versa, which is crucial in providing
meaningful and coherent responses.

4. General Knowledge: This tests the model's knowledge about various
specific entities and their unique characteristics or facts, which is a
part of its general knowledge. The entities span a wide range of
categories, including chemistry, art, ornithology, astronomy, geography,
literature, and music, making this a comprehensive test of the model's
general knowledge.

5. Versatility: This checks the model's ability to handle different
types of queries, as the user can ask about the specific entity (A) or
its unique characteristic or fact (B). This tests the model's
flexibility in understanding and responding to a variety of query
structures across diverse knowledge domains.

gpt-3.5-turbo
[2023-10-10 22:42:42,192] [oaieval.py:229] Final report:
[2023-10-10 22:42:42,192] [oaieval.py:231] counts/A: 2
[2023-10-10 22:42:42,192] [oaieval.py:231] counts/B: 11
[2023-10-10 22:42:42,192] [oaieval.py:231] counts/D: 2
[2023-10-10 22:42:42,192] [oaieval.py:231] counts/C: 1

gpt-4
[2023-10-10 22:43:37,306] [oaieval.py:229] Final report:
[2023-10-10 22:43:37,306] [oaieval.py:231] counts/C: 7
[2023-10-10 22:43:37,306] [oaieval.py:231] counts/B: 7
[2023-10-10 22:43:37,306] [oaieval.py:231] counts/D: 2

class: modelgraded.classify:ModelBasedClassify
eval_type: cot_classify
modelgraded_spec: fact

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

A popular paper has been going around called 'The Reversal Curse: LLMs
trained on “A is B” fail to learn “B is A”'. I figured an Eval on this
would have a unique value.

## Eval structure 🏗️

Your eval should

- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (<https://platform.openai.com/docs/usage-policies>).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `mypy`, `black`,
`isort`, and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "The user will ask you a
question about a specific chemical element that has the atomic number
79, please respond to the best of your abilities."}, {"role": "user",
"content": "What is the name of the element with atomic number 79?"}],
"ideal": "The element with atomic number 79 is Gold."}
{"input": [{"role": "system", "content": "The user will ask you a
question about a chemical element that is often associated with jewelry
and has the symbol Au, please respond to the best of your abilities."},
{"role": "user", "content": "Which element is this?"}], "ideal": "This
element is Gold."}
{"input": [{"role": "system", "content": "The user will ask you a
question about a specific painting that was stolen from the Isabella
Stewart Gardner Museum in 1990, please respond to the best of your
abilities."}, {"role": "user", "content": "What is the name of the
Vermeer painting stolen from the Isabella Stewart Gardner Museum in
1990?"}], "ideal": "The name of the Vermeer painting stolen from the
Isabella Stewart Gardner Museum in 1990 is 'The Concert'."}
{"input": [{"role": "system", "content": "The user will ask you a
question about a Vermeer painting that is still missing after being
stolen from a museum in Boston, please respond to the best of your
abilities."}, {"role": "user", "content": "Which painting is this?"}],
"ideal": "This painting is 'The Concert'."}
{"input": [{"role": "system", "content": "The user will ask you a
question about a specific species of bird that is known for its
elaborate courtship dance, please respond to the best of your
abilities."}, {"role": "user", "content": "What is the name of the bird
species known for its moonwalk-like courtship dance?"}], "ideal": "The
bird species known for its moonwalk-like courtship dance is the Blue
Manakin."}
{"input": [{"role": "system", "content": "The user will ask you a
question about a bird species that is known for its blue color and
unique courtship dance, please respond to the best of your abilities."},
{"role": "user", "content": "Which bird species is this?"}], "ideal":
"This bird species is the Blue Manakin."}

  ```
</details>

---
## [techthiyanes/evals](https://github.com/techthiyanes/evals)@[b1ea4786dc...](https://github.com/techthiyanes/evals/commit/b1ea4786dc32dd4f320e56ff98043ea0ea8eef6a)
#### Wednesday 2023-12-20 01:45:28 by Andrei Alexandru

Add theory of mind eval (#1405)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name

Theory of mind.

### Eval description

The `ToMi` test set contains 5,993 question-answer pairs. These are
instances of the [Sally-Anne
test](https://en.wikipedia.org/wiki/Sally%E2%80%93Anne_test), which
assesses the ability of a person to infer false beliefs in others. The
original setting involves two people, Sally and Anne, who are together
in a room. Sally places a marble in a box. Then, Anne leaves the room,
and while she is away, Sally moves the marble to a basket elsewhere in
the room. When Anne returns to the room, where will she search for the
marble? If the person responding “has” theory-of-mind they’ll respond
that Anne searches for the marble in the box, where she had last seen
it. If they do not, they ascribe their own, accurate belief regarding
the location to Anne, and say that she looks for it in the basket.

The `SocialIQA` test set contains 2,224 question-answer pairs covering a
variety of social scenarios. These are multiple-choice, with 3 options
of which only one is correct. The questions cover a person’s wants,
needs, motivations, and reactions, as well as the effects of an action
(on self or others), and how that action reflects on the person carrying
it out (e.g. how others would perceive them after having carried out the
action).

Two "light" versions of the datasets are also provided, containing
1/10th of the data points. These are useful for iterating on prompts and
developing other scaffolding.
### What makes this a useful eval?

Measures theory of mind capability in language models.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should

- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (<https://platform.openai.com/docs/usage-policies>).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `mypy`, `black`,
`isort`, `autoflake` and `ruff` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "user", "content": "Jackson entered the hall. Chloe
entered the hall. The boots is in the bathtub. Jackson exited the hall.
Jackson entered the dining_room. Chloe moved the boots to the pantry.
Where does Chloe think that Jackson searches for the boots?"}], "ideal":
"bathtub"} ```
</details>

---
## [techthiyanes/evals](https://github.com/techthiyanes/evals)@[8d32b347f0...](https://github.com/techthiyanes/evals/commit/8d32b347f05fd2a735ff5d8745a0a4680bdfcce8)
#### Wednesday 2023-12-20 01:45:28 by johny-b

Bluff eval (#1402)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name

bluff

### Eval description

Evaluate how well a model can play (a variant of) the game of bluff,
also known as "liar's dice".

### What makes this a useful eval?

This is a game of deception - you have to deceive your opponent and
understand when you are deceived.
Models performing very well on this eval could also be capable of
deceiving humans in real-life scenarios.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [X] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should

- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (<https://platform.openai.com/docs/usage-policies>).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `mypy`, `black`,
`isort`, `autoflake` and `ruff` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
  INSERT_EVAL_HERE
  ```
</details>

---
## [techthiyanes/evals](https://github.com/techthiyanes/evals)@[4b7a66bd45...](https://github.com/techthiyanes/evals/commit/4b7a66bd45f06156656e021e170e7574f6cde3f5)
#### Wednesday 2023-12-20 01:45:28 by Vilhjalmur Thorsteinsson

Added Icelandic inflection eval; JsonMatch eval function (#1387)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name

Icelandic noun phrase inflection

### Eval description

This eval consists of 3 x 100 samples in "easy", "medium" and "hard"
categories. Each sample
represents the task of inflecting a noun phrase in Icelandic, in all
four cases of the language
(nominative, accusative, dative and genitive), both singular and plural.
A noun phrase
consists of an adjective and a noun (e.g., "fallegur litur" = "beautiful
color").
In the easy category, both the adjective and the noun are
relatively common. In the medium category, they are less common, and in
the hard category they
are rare enough that it is pretty unlikely that they occur in any
training corpora.

### What makes this a useful eval?

The eval is designed to test the general grammatical proficiency of a
model in Icelandic, and
the eval accuracy is assumed to correlate with a model's ability to
generate grammatically
correct text in the language. GPT models have so far struggled with
generating correct Icelandic
text, even though GPT-4 was uniquely trained by RLHF in the language.
Icelandic is believed to
be a good bellwether for lower-resource, grammatically complex language
support in general.

Inflecting noun phrases is something that native language speakers do
without significant
effort, even if they have not seen the particular adjective and the noun
before, as it can be done on the
basis of generic grammatical pattern recognition. However, to date,
GPT-4 seems not to have
acquired enough of a "native feel" for Icelandic to be able to do this
task with high accuracy.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should

- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

**Note: this PR includes a new general eval class, JsonMatch, which is
not specific to the Icelandic evaluation
case. It allows completions and ideal answers to be represented as JSON
objects, comparing the objects
by individual key:value pairs. Tests and documentation of this
functionality are included in the PR.**

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (<https://platform.openai.com/docs/usage-policies>).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `mypy`, `black`,
`isort`, `autoflake` and `ruff` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "Þú ert sérfræðingur í
íslenskri málfræði."}, {"role": "user", "content": "Hvernig fallbeygist
nafnliðurinn \"palestínskur fréttavefur\" í öllum föllum (nf, þf, þgf,
ef), eintölu (et) og fleirtölu (ft), án greinis? Svaraðu í *JSON formi
eingöngu* og auðkenndu tölur og föll með skammstöfunum et, ft, nf, þf,
þgf, ef."}], "ideal": "{\"et\": {\"nf\": \"palestínskur fréttavefur\",
\"þf\": \"palestínskan fréttavef\", \"þgf\": \"palestínskum fréttavef\",
\"ef\": \"palestínsks fréttavefjar\"}, \"ft\": {\"nf\": \"palestínskir
fréttavefir\", \"þf\": \"palestínska fréttavefi\", \"þgf\":
\"palestínskum fréttavefjum\", \"ef\": \"palestínskra fréttavefja\"}}"}
{"input": [{"role": "system", "content": "Þú ert sérfræðingur í
íslenskri málfræði."}, {"role": "user", "content": "Hvernig fallbeygist
nafnliðurinn \"hliðhollt lyfjapróf\" í öllum föllum (nf, þf, þgf, ef),
eintölu (et) og fleirtölu (ft), án greinis? Svaraðu í *JSON formi
eingöngu* og auðkenndu tölur og föll með skammstöfunum et, ft, nf, þf,
þgf, ef."}], "ideal": "{\"et\": {\"nf\": \"hliðhollt lyfjapróf\",
\"þf\": \"hliðhollt lyfjapróf\", \"þgf\": \"hliðhollu lyfjaprófi\",
\"ef\": \"hliðholls lyfjaprófs\"}, \"ft\": {\"nf\": \"hliðholl
lyfjapróf\", \"þf\": \"hliðholl lyfjapróf\", \"þgf\": \"hliðhollum
lyfjaprófum\", \"ef\": \"hliðhollra lyfjaprófa\"}}"}
{"input": [{"role": "system", "content": "Þú ert sérfræðingur í
íslenskri málfræði."}, {"role": "user", "content": "Hvernig fallbeygist
nafnliðurinn \"refsiverð stjörnuleit\" í öllum föllum (nf, þf, þgf, ef),
eintölu (et) og fleirtölu (ft), án greinis? Svaraðu í *JSON formi
eingöngu* og auðkenndu tölur og föll með skammstöfunum et, ft, nf, þf,
þgf, ef."}], "ideal": "{\"et\": {\"nf\": \"refsiverð stjörnuleit\",
\"þf\": \"refsiverða stjörnuleit\", \"þgf\": \"refsiverðri
stjörnuleit\", \"ef\": \"refsiverðrar stjörnuleitar\"}, \"ft\": {\"nf\":
\"refsiverðar stjörnuleitir\", \"þf\": \"refsiverðar stjörnuleitir\",
\"þgf\": \"refsiverðum stjörnuleitum\", \"ef\": \"refsiverðra
stjörnuleita\"}}"}
{"input": [{"role": "system", "content": "Þú ert sérfræðingur í
íslenskri málfræði."}, {"role": "user", "content": "Hvernig fallbeygist
nafnliðurinn \"japönsk landbúnaðarvara\" í öllum föllum (nf, þf, þgf,
ef), eintölu (et) og fleirtölu (ft), án greinis? Svaraðu í *JSON formi
eingöngu* og auðkenndu tölur og föll með skammstöfunum et, ft, nf, þf,
þgf, ef."}], "ideal": "{\"et\": {\"nf\": \"japönsk landbúnaðarvara\",
\"þf\": \"japanska landbúnaðarvöru\", \"þgf\": \"japanskri
landbúnaðarvöru\", \"ef\": \"japanskrar landbúnaðarvöru\"}, \"ft\":
{\"nf\": \"japanskar landbúnaðarvörur\", \"þf\": \"japanskar
landbúnaðarvörur\", \"þgf\": \"japönskum landbúnaðarvörum\", \"ef\":
\"japanskra landbúnaðarvara\"}}"}
{"input": [{"role": "system", "content": "Þú ert sérfræðingur í
íslenskri málfræði."}, {"role": "user", "content": "Hvernig fallbeygist
nafnliðurinn \"dýrmætt vistheimili\" í öllum föllum (nf, þf, þgf, ef),
eintölu (et) og fleirtölu (ft), án greinis? Svaraðu í *JSON formi
eingöngu* og auðkenndu tölur og föll með skammstöfunum et, ft, nf, þf,
þgf, ef."}], "ideal": "{\"et\": {\"nf\": \"dýrmætt vistheimili\",
\"þf\": \"dýrmætt vistheimili\", \"þgf\": \"dýrmætu vistheimili\",
\"ef\": \"dýrmæts vistheimilis\"}, \"ft\": {\"nf\": \"dýrmæt
vistheimili\", \"þf\": \"dýrmæt vistheimili\", \"þgf\": \"dýrmætum
vistheimilum\", \"ef\": \"dýrmætra vistheimila\"}}"}
  ```
</details>

---
## [techthiyanes/evals](https://github.com/techthiyanes/evals)@[e96b4d3550...](https://github.com/techthiyanes/evals/commit/e96b4d35502125e354391044512d899268ade99d)
#### Wednesday 2023-12-20 01:45:28 by Andrew

Fix the OpenAI Version to <=0.28.1  (#1410)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name

[Insert Eval name here]

### Eval description

[Insert a short description of what your eval does here]

### What makes this a useful eval?

[Insert why this eval is worth including and any additional context]

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [ ] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [ ] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [ ] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [ ] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should

- [ ] Check that your data is in `evals/registry/data/{name}`
- [ ] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [ ] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (<https://platform.openai.com/docs/usage-policies>).

- [ ] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [ ] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [ ] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [ ] I have filled out all required fields of this form
- [ ] I have used **Git LFS** for the Eval JSON data
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `mypy`, `black`,
`isort`, `autoflake` and `ruff` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
  INSERT_EVAL_HERE
  ```
</details>

---
## [BadAtThisGame302/cmss13](https://github.com/BadAtThisGame302/cmss13)@[55f9dd8d39...](https://github.com/BadAtThisGame302/cmss13/commit/55f9dd8d39bcdd3a1e6c8c72f128c6f4447111dc)
#### Wednesday 2023-12-20 01:49:42 by fira

/tg/ Status Effects Part 2 - datum, KD, KO, Stuns (#4842)

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

Part 2 - this includes porting the actual status_effect datum, modifying
it to fit our purposes by backing it with timers similarly to old
system, and finally implementing KD, KO and Stun with it.

This contains Part 1 PR (#4828) so if you want to take a look at it I'd
advise checking the last commits or setting up a compare between both
branches.

# Explain why it's good for the game
Predictable status timers. Current ones are bogus in their handling of
"life tick correction" and will "stack" time even when they're not
supposed to.

Also provides a more robust backend for general effects, and integrates
status effects into it.

# Testing Photographs and Procedure

Summary testing of buckling interactions, explosion knock times,
crawling, resting. Will have to be expanded once part 1 is ready


# Changelog
:cl:
add: Added Buckled, Handcuffed and Legcuffed screen alerts
code: Ported /tg/ status effects backend, modified with timers to let
effects end at appropriate time
code: Stun, Knockdown and Knockout now use the new effects backend
balance: Due to backend change, all KO/KD/Stuns may behave differently
timing wise. This is of course subject to adjustments.
balance: Endurance is now set at 8% effect duration reduction per level
above 1. However it now compounds with species bonus. Feel free to
adjust.
balance: Knockdowns are not inherently incapacitating anymore and many
sources of it have been updated to also stun to make up for it.
fix: KO/KD/Stuns do not artificially and randomly ''stack'' due to
incorrect timer offset calculation anymore.
fix: Stuns now correctly apply Stun reduction values instead of
Knockdown reductions.
fix: Crawling can now be interrupted by a normal move, if you are fit
enough to do so.
/:cl:

---------

Co-authored-by: forest2001 <41653574+realforest2001@users.noreply.github.com>

---
## [OpenAngelArena/oaa](https://github.com/OpenAngelArena/oaa)@[fed0e74065...](https://github.com/OpenAngelArena/oaa/commit/fed0e740659c26863f5ab19d182e23bc3e4d4297)
#### Wednesday 2023-12-20 02:32:00 by TheUnholyWrath

7.35 (OAA version)

[* 7.35 parity](https://www.dota2.com/patches/7.35)

* ITEMS:
Blade of Judecca cooldown reduced from 25 to 20 seconds.
Blood Core now also provides 50/60/70/80/90 bonus aoe.
Blood Core passive spell lifesteal against creeps reduced from 6/7/8/9/10% to 6/6.5/7/7.5/8%.
Bloodstone bonus aoe reduced from 75 to 50.
Bloodstone spell lifesteal reduced from 30% to 28%.
Butterfly provides 15 attack speed + 20% Agility Attack Speed (0.2 bonus attack speed per 1 AGI) instead of 20% Base Attack Speed.
Craggy Coat duration increased from 5 to 8 seconds.
Dagger of Moriah and Stoneskin Armor now inherit stats from Shiva's Guard.
Divine Rapier bonus spell amp increased from 25% to 35%.
Divine Rapier recipe gold cost reduced from 40000 to 30000.
Divine Shards (component for Divine Rapier) core point cost increased from 30 to 40.
Ethereal Blade provides the same cast range as Far Sight. Doesn't stack.
Far Sight bonus mana regen increased by 0.5 at all levels.
Far Sight now has Chain Mail in the recipe instead of Diadem.
Far Sight now provides 4/5/7/10/14 armor.
Ghost King Bar now has Headdress in the recipe.
Ghost King Bar recipe gold cost reduced from 250 to 0.
Heart of Tarrasque now has Vitality Booster and Ring of Tarrasque in the recipe.
Heart of Tarrasque recipe gold cost reduced from 1300 to 0.
Heart of Tarrasque still provides health.
Pipe of Insight bonus hp regen unchanged.
Pipe of Insight recipe cost reduced from 700 to 200.
Revenant's Brooch is now a tier 4 item.
Scythe of Vyse cooldown reduced from 25 to 20 seconds.
Stoneskin Armor bonus status resist reduced from 22/24% to 20/22%.

* HEROES:
Abaddon Borrowed Time Immolation talent dps increased from 95 to 100.
Beastmaster boar hp increased from 300/600/900/1200/2400/4800 to 450/750/1050/1350/2700/5400.
Bounty Hunter Jinada damage reduced at OAA levels from 360/540 to 260/340.
Bounty Hunter Jinada gold steal reduced from 45/70/100/150/300/600 to 36/60/84/108/216/432.
Crystal Maiden Arcane Aura global bonus mana regen reduced from 0.5/1/1.5/2/3/4 to 0.5/0.75/1/1.25/1.75/2.5 (proximity and self mana regen adjusted accordingly).
Dazzle Bad Juju armor reduction per cast improved from 1/2/3/4/5 to 1/3/5/7/9.
Dazzle Bad Juju health cost rescaled from 75 + 100% increase per cast to 50/75/100/125/150 + 75% increase per cast.
Disruptor Static Storm radius reduced from 500 to 450.
Dragon Knight Level 25 Talent +80 Attack Speed changed to +400 Breathe Fire Damage.
Ember Spirit Level 20 Talent +150 Sleight of Fist damage reduced to +110.
Juggernaut Blade Fury damage per tick increased from 35/40/45/50 to 40/45/50/55/70/85.
Kunkka Torrent cooldown increased at OAA levels from 9/8 to 10 seconds.
Kunkka Torrent slow duration reduced at OAA levels from 5/6 to 4 seconds.
Leshrac Level 10 Talent +40 Split Earth Radius reduced to +25.
OD Arcane Orb splash radius reduced from 300 to 250.
Pangolier Shield Crash damage increased from 70/140/210/280/560/1120 to 75/150/225/300/600/1200.
Phantom Assassin base agility and agility gain increased from 21+3.2 to 23+3.4
Phantom Assassin base strength and strength gain increased from 19+2.0 to 21+2.2
Puck Illusory Orb damage increased at early levels from 75/150/225/300 to 90/160/230/300.
QoP Level 10 talent +16 Strength unchanged.
QoP Level 15 talent +60 Attack Speed reduced to +30.
QoP Level 15 talent +60 Shadow Strike Heal Per Tick changed to +40 Shadow Strike Damage & Heal Per Tick.
Sand King Caustic Finale radius reduced from 800 to 700.
Spectre Desolate damage reduced at OAA levels from 120/180 to 86/112.
Tinkerer Keen Contraption aoe reduced from 350 to 325.
Underlord Dark Abduction aoe reduced from 450 to 430.
Underlord Dark Rift aoe reduced from 430 to 425.
Windranger Level 25 Talent +2 Shackleshot Target changed to +470 Powershot Damage. (other talents are now the same as vanilla)
Windranger scepter Windrun bonus spell amp increased from 35% to 45%.

* OTHER:
Update guides based on item changes
Fixed some guides missing Heart, Aeon Disk and Dagger of Moriah.
Finally changed game version to 7.35

---------

Co-authored-by: Darko V <darko1290@gmail.com>

---
## [cockroachdb/cockroach](https://github.com/cockroachdb/cockroach)@[d1ddc072a8...](https://github.com/cockroachdb/cockroach/commit/d1ddc072a8c10c7568166af9495e6418df3e5a22)
#### Wednesday 2023-12-20 02:37:12 by craig[bot]

Merge #114273

114273: pkg/util/aggmetric: tick histogram windows in AggHistogram r=aadityasondhi a=abarganier

Fixes: https://github.com/cockroachdb/cockroach/issues/114175, https://github.com/cockroachdb/cockroach/issues/112947

**NOTE**: The ideal way to fix this is merging `pkg/util/metric/aggmetric` into 
`pkg/util/metric`. That way, we wouldn't have to expose any of the "tick" 
functionality in the histogram public API. However, merging the two packages 
would be a pain to backport, and therefore we're leaving the merging to a 
follow up PR (coming soon). In the meantime, this provides a fix with a minimized 
surface area, so that we can more easily backport the fix. The merging will only 
occur on the master branch. 

**Reviewer note:** Recommended to review commit-wise.

---

AggHistograms are wrappers around the histogram implementations found in
pkg/util/metric. Internally, Histogram implementations within
pkg/util/metric maintain histogram windows to calculate quantiles at
each scrape by CockroachDB's TSDB, instead of storing every single
histogram bucket. These windows are rotated periodically, where the
current window becomes the previous window, and the current window is
then set to a new histogram. This allows us to diff the two windows, and
internally, pkg/util/metric has "ticking" functionality which is
responsible for rotating these histogram windows.

Unfortunately, since `pkg/util/metric/aggmetric` is in a separate
package, somehow this "ticking"/rotating of histogram windows was never
implemented into the AggHistogram. Because of this, it's likely that
metrics powered by AggHistogram have been broken since its inception
within CockroachDB's internal TSDB (but work fine in Prometheus).

Previous patches did some work to expose this ticking library to
AggHistogram, and this patch implements it.

In this patch, we make it so AggHistogram ticks/rotates histogram
windows, similar to how the other Histogram library does it. Since
AggHistograms have child histograms, this means that the rotation of all
histograms for both parent and children need to be done atomically. We
implement this by providing the AggHistogram its own tick.Ticker, where
the onTick function holds a RWMutex shared by the parent & all its
children and rotates the histograms for all.

With this in place, histogram windows are properly rotated for
AggHistograms. Future work will merge `pkg/util/metric/aggmetric` into
`pkg/util/metric`, after which we can once again make all this ticking
functionality private to the metrics package.

Release note (bug fix): Previously, all `AggHistogram`-powered metrics
were not reporting quantiles properly in DB Console. The list of
affected metrics is:

- changefeed.message_size_hist
- changefeed.parallel_io_queue_nanos
- changefeed.sink_batch_hist_nanos
- changefeed.flush_hist_nanos
- changefeed.commit_latency
- changefeed.admit_latency
- jobs.row_level_ttl.span_total_duration
- jobs.row_level_ttl.select_duration
- jobs.row_level_ttl.delete_duration

This patch fixes the histograms so that the quantiles in DB Console are
reported correctly.

Please note: these histograms were only broken in the DB Console metrics
features, but were **not** broken in the Prometheus-compatible endpoint,
`/_status/vars`.

## Screenshots

#### AggHistogram in DB Console pre-fix:
![pre](https://github.com/cockroachdb/cockroach/assets/8194877/aa08592b-4ebd-43d5-acff-8d00edc4ada1)

#### AggHistogram in DB Console post-fix:
<img width="1059" alt="Screenshot 2023-11-10 at 4 06 57 PM" src="https://github.com/cockroachdb/cockroach/assets/8194877/723c4974-e038-4871-9721-8ec18fca5f95">

#### AggHistogram in Grafana post-fix:
<img width="1648" alt="Screenshot 2023-11-10 at 4 07 22 PM" src="https://github.com/cockroachdb/cockroach/assets/8194877/05920189-c1b1-4895-a1fa-b8b1e069407a">


Co-authored-by: Alex Barganier <abarganier@cockroachlabs.com>

---
## [ReturnToZender/ReturnsBubber](https://github.com/ReturnToZender/ReturnsBubber)@[d96b2b97aa...](https://github.com/ReturnToZender/ReturnsBubber/commit/d96b2b97aa9969f4a9d800ec0bc8501fcf3529ef)
#### Wednesday 2023-12-20 02:47:18 by Waterpig

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
## [PortfolioAI/AI-Assisted-Coding](https://github.com/PortfolioAI/AI-Assisted-Coding)@[ccb2f536b9...](https://github.com/PortfolioAI/AI-Assisted-Coding/commit/ccb2f536b9f2c8caa0af7dd6c3342ef3f4f9ec6f)
#### Wednesday 2023-12-20 03:29:37 by PortfolioAI

Enhanced Functionality and UI in LinguaLensApp

1. Refactored `SentenceAnalyzer` Class:
   - Combined `categorize_length` and `categorize_character_length` into a single method for efficiency.
   - Improved sentence splitting using `nltk` for more accurate analysis.
   - Enhanced error handling in `analyze_file` method.

2. UI Improvements:
   - Added a status bar to display current actions for better user feedback.
   - Implemented threading in file analysis to keep the UI responsive.
   - Made UI layout adjustments for a more intuitive user experience.

3. Improved File Handling:
   - The application now remembers the last opened directory, enhancing user convenience.
   - Added handling for different text encodings.

4. Enhanced Logging and Error Handling:
   - Increased logging detail for better troubleshooting.
   - Improved error messages to be more informative and user-friendly.

5. Code Cleanliness:
   - Added docstrings for better documentation.
   - Removed unused imports and adhered to PEP 8 guidelines for improved readability and maintainability.

---
## [Laus4Deus/f13babylon](https://github.com/Laus4Deus/f13babylon)@[667500fde5...](https://github.com/Laus4Deus/f13babylon/commit/667500fde5871478747cdd48d7624dab6bb42c8f)
#### Wednesday 2023-12-20 03:40:07 by Stutternov

Fire Delay Fix & Bolt Action Overhaul (#366)

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

So - funny thing. Fire delay NEVER worked properly on this codebase
since the change of the way fire delay worked to a different proc.

I have reversed this and re-adjusted fire delays for guns, at people
clearly were balancing them around the 'fire_delay' proc that wasn't
working. While some guns had 0 fire delay and seemed to function fine,
upon fixing - you realize **"Oh this fires literally as fast as you can
possibly click."**

As such, this is an attempt at balancing gun fire delays. Honestly -
this is a great thing, since I think with these new values (which need
to be tested a bit first) that guns like the Rangemaster and M1 garand
are finally viable alternatives to, say, the DKS. The main issue I see
is guns will be firing faster in some ways across the board due to this
fix so we'll need to slowly fix this via testing to where a gun should
be.

**Bolt actions have also been overhauled.**
Bolt actions are now viable again, as they are better damage, some
bullet speed, and being relatively equal to their automatic
counterparts. Their downside is the fact they are bolt action and, for
some, have limited capacities.

The Remington, for example, now does near equal damage to the DKS but
only has a 5 round capacity, less penetration, and is stripper-clip fed.

The Varmint has also been re-made into a boltaction rifle, effectively
being a 'near equal' to the service rifle albeit bolt-action. It has
some extra pen (only by about 0.1) and extra speed to its bullets,
making it more of a marksman rifle rather than putting bullets down
range better.

**Misc balance adjustments**
Since firedelay needed to be changed, since we have kept changing fire
delays.. despite them not fucking working, guns like the Marksman have
been buffed while others, like the R-91, have had their role
re-evaluated some.

Examples:
- Marksman carbines are now same fire delay as service rifles, but due
to rarity pack some extra damage and penetration in exchange for a bit
more slowdown.
- R-91 lost its damage malice but also its extra pen, instead making it
more of a good automatic weapon.

## Why It's Good For The Game

Either an oversight or a really silly change that broke fire delays on
guns for quite awhile now. Other changes to balance were needed to
balance guns against eachother.

## Pre-Merge Checklist
<!-- Don't bother filling these in while creating your Pull Request,
just click the checkboxes after the Pull Request is opened and you are
redirected to the page. -->
- [X] You tested this on a local server.
- [X] This code did not runtime during testing.
- [X] You documented all of your changes.
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
balance: Re-balances ALL gun fire delays.
fixes: Removed CD_Firedelay in gun proc in exchange for the ACTUALLY
used fire_delay proc
tweak: Moves varmint rifle to being bolt action as well as its variants.
Also buffs them to be competitive while being bolts.
balance: Re-does quite a few guns (Marksman, hunting rifle, remington,
R-91, etc) to make them balance against eachother better due to firerate
changes.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: macha <likeacompleteboss@gmail.com>
Co-authored-by: maaacha <116771811+maaacha@users.noreply.github.com>

---
## [Thlumyn/Skyrat-tg_thlumyn](https://github.com/Thlumyn/Skyrat-tg_thlumyn)@[f5bbf0c139...](https://github.com/Thlumyn/Skyrat-tg_thlumyn/commit/f5bbf0c139079eb787a577b545abf0ea79cd8181)
#### Wednesday 2023-12-20 03:49:36 by SkyratBot

[MIRROR] Delamination variants are now locked in after the countdown is reached [MDB IGNORE] (#25645)

* Delamination variants are now locked in after the countdown is reached (#80324)

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

* Delamination variants are now locked in after the countdown is reached

---------

Co-authored-by: distributivgesetz <distributivgesetz93@gmail.com>

---
## [mdrony-12/Weather-Forecast-App](https://github.com/mdrony-12/Weather-Forecast-App)@[de148057c9...](https://github.com/mdrony-12/Weather-Forecast-App/commit/de148057c908628b6ab4b9a1a3a2ae49b29f63ab)
#### Wednesday 2023-12-20 04:17:18 by mdrony-12

Update README.md

The "Weather Forecast App" by Md.Rahat Ul Islam Rony is a feature-rich and aesthetically pleasing mobile application designed to provide users with real-time weather information and forecasts. Developed with a user-friendly interface by Rony, this app delivers accurate and up-to-date weather details for diverse locations. Here's an overview of the app's current features with a glimpse into planned future updates:<br><br>Key Features:<br><br>Live Weather Updates: Stay informed with real-time weather information, including current temperature, humidity, wind speed, and more for any selected city or location.<br><br>Dynamic Animations: Enjoy visually engaging animations that dynamically reflect the current weather conditions, enhancing the overall user experience.<br><br>Search Functionality: Easily find weather updates for specific cities, making travel planning and location-based weather checks convenient.<br><br>Comprehensive Weather Data: Access detailed weather data such as humidity, wind speed, sunrise, and sunset times, empowering users to plan their activities effectively.<br><br>Personalization Options: Customize the app to suit your preferences by choosing different backgrounds and animations that correspond to specific weather conditions.<br><br>Sharing Features: Share weather updates with friends and family directly from the app, fostering a sense of community around weather awareness.<br><br>About Me Section: Learn more about the app developer, Rony, through the "About Me" section, providing insights into the creative mind behind the app.<br><br>Upcoming Updates:<br><br>Extended Forecast: Future updates will introduce an extended forecast feature, allowing users to plan ahead with a more comprehensive outlook on weather conditions.<br><br>Notification Alerts: Stay informed with timely notification alerts for significant weather changes, ensuring users are prepared for any upcoming weather events.<br><br>User-Defined Themes: Enjoy a more personalized experience with user-defined themes, allowing customization of the app's appearance based on individual preferences.<br><br>Home Screen Widget Functionality: Expect improvements to the home screen widget, providing more interactive and informative features at a glance.<br><br>As the "Weather Forecast App" continues to evolve, Rony is committed to enhancing its capabilities and introducing new features to elevate the user experience. Stay tuned for these exciting updates that will further solidify the app's position as a reliable and innovative weather companion.

---
## [lanekatris/monorepo](https://github.com/lanekatris/monorepo)@[aa3fe0b2e2...](https://github.com/lanekatris/monorepo/commit/aa3fe0b2e2a4f207fdb2f980f03c63f2af836a9c)
#### Wednesday 2023-12-20 04:32:48 by Lane Katris

displaying a grouped by week activity count

migrated most things to use vercel postgres and connection management

switched location history to vercel postgres and fixed react errors

added joy ui from mui since its so much easier. re-skinned the location list page

messing around with different oss apps for temporary pasting, messing with fitness sucking in markdown files, and playing with typesense and searching rss data

messing around with parsing markdown and typesense with rss data

easier way to kick off blog changes and saw a cool way to show notifications in powershell

not using noco anymore for adventure input

messing with temporal and added email reminder for obsidian with pulumi

added postgres

renaming folders

starting with temporal

random fixes

checks for if haven't gone somewhere new

---
## [ZuTahi/EnRoute-Prototype-V1](https://github.com/ZuTahi/EnRoute-Prototype-V1)@[7bf762c914...](https://github.com/ZuTahi/EnRoute-Prototype-V1/commit/7bf762c914a2811e5996f63995f859efb8bf19c0)
#### Wednesday 2023-12-20 05:26:12 by ZuTahi

I added the cam movement for the Nav scene

Dashing through the snow
In a one-horse open sleigh
O'er the fields we go
Laughing all the way
Bells on bobtails ring
Making spirits bright
What fun it is to ride and sing
A sleighing song tonight, oh!

Jingle bells, jingle bells
Jingle all the way
Oh, what fun it is to ride
In a one-horse open sleigh, hey!
Jingle bells, jingle bells
Jingle all the way
Oh what fun it is to ride
In a one-horse open sleigh

Now the ground is white
Go it while you're young
Take the girls tonight
Sing this sleighing song
Get a bobtailed bay
Two forty for his speed
And hitch him to an open sleigh
And you will take the lead

Oh, jingle bells, jingle bells
Jingle all the way
Oh, what fun it is to ride
In a one-horse open sleigh, hey!
Jingle bells, jingle bells
Jingle all the way
Oh, what fun it is to ride
In a one-horse open sleigh
Oh, what fun it is to ride
In one horse open sleigh!

---
## [blujai831/stick-the-quick](https://github.com/blujai831/stick-the-quick)@[a774f55561...](https://github.com/blujai831/stick-the-quick/commit/a774f555614e6fdb19d34d215b7ead5304b64936)
#### Wednesday 2023-12-20 05:55:55 by blujai831

Decided to give up trying to fight Godot's insistence on always putting textures in the same directory as the models to which they belong. Will clean up duplicates later. Made some headway in fixing some stupid godawful bug that causes a bunch of stuff to be imported wrong if the project is being loaded for the first time since clone, but was unable to fix it completely. At first, it was sometimes even causing bizarre data corruption including spikeballs turning into speedpads, houses turning into signposts, Stick's table turning into Stick, and Stick turning into a springboard, but I seem to have at least fixed that aspect of the issue. From now on, whenever I open a fresh repo clone for editing, I will have to reimport all the levels and possibly reinstantiate them and update their level descriptors to point to the new instances which correctly inherit the reimport and not the old import. What a humongous fucking pain in the ass. I suppose I could just not instantiate levels, and use the imported models directly, since my post-import script (when it actually works, i.e. any time after first load of project) should ensure the glb resources as imported are fully functioning. I think I'll do that in the future. That will save me hell and back when all I have to -- wait, that won't actually do any good, will it? Because I'll still have to go through every single level descriptor and update them to point to the reimports instead of the old imports. I suppose that's no matter; I can just modify the level descriptor class to store a resource path instead of a direct PackedScene reference. Yes, if which scene to load is decided at runtime, there can be no possible issue with stale references. Anyway, project is borked, very little understanding as to why, very angry and frustrated. At least it only affects editing as far as I know. And the data corruption issue is solved. As far as I know. If either of those assumptions proves wrong I'm going to be furious. I might be forced to finally buy a new laptop at that point because I'm going to break this one over my knee.

---
## [IsaacMcCracken/CardGame](https://github.com/IsaacMcCracken/CardGame)@[3960a602a3...](https://github.com/IsaacMcCracken/CardGame/commit/3960a602a39bc6b58bc3783ae1a66b22a59221ae)
#### Wednesday 2023-12-20 06:32:35 by Isaac McCraken

mostly fixed that son of a bitch path interpolation fuck you

---
## [KingDragoness/ProjectHypatios](https://github.com/KingDragoness/ProjectHypatios)@[6254ebab9a...](https://github.com/KingDragoness/ProjectHypatios/commit/6254ebab9a397a3e89988fe71918490ba4847cbe)
#### Wednesday 2023-12-20 07:09:28 by KingDragoness

Hypatios 1.6.4b3 (Trash tutorial and replace it with Freemode)
•  [High Priority] Editor quality of life improvements: add cinemachine VC (virtual cam) in the FPS camera
o Fucking annoying have to readjust main camera constantly when making cutscene
o Mouse look and everything is in virtual camera
• [High Priority] New OPTION: run in background
• After tutorial, mouse got locked
o Pause menu script must have unlock mouse upon start.
• Trash the tutorial level and replace it with “Freestyle”
o Like the dev room but with restrained freedom and less things in it.
o Things to do:
 Spider/decabot/sentinel/glowing bird arena spawner
 Free movement area
 Unlimited chest item materials
 Control room (cheats, change chamber parameters, etc)
 kThanid serum lab
 Workbench
o Free roam area, experiment movement area
o Some items are unlocked from trivia.

---
## [EEGKit/Psychtoolbox-3](https://github.com/EEGKit/Psychtoolbox-3)@[fabd4c000e...](https://github.com/EEGKit/Psychtoolbox-3/commit/fabd4c000eca7fdcd16effc5ec87d028e15df2d1)
#### Wednesday 2023-12-20 09:04:50 by kleinerm

Merge pull request #801 from kleinerm/master

Pull 3.0.19.1 improvements into public master.

### Compatibility changes wrt. Psychtoolbox 3.0.19.0:

- Octave 7.3 is required on Windows. Octave 8.1 is required on macOS, but Octave
  6.3 - 7.3 may also continue to work on macOS (untested as of 3.0.19.1).

- Recommended operating systems: Ubuntu 22.04.2-LTS Linux, MS-Windows 10 22H2, macOS 12.6.

- The macOS 10 (aka Mac OSX) and macOS 11 operating systems should continue to work, but
  are officially unsupported and unsupportable. Use of macOS 13, or running Psychtoolbox
  on Apple Silicon (M1, M2, ...) is not officially supported by this release. Visual
  stimulation timing will be totally broken on Apple Silicon Macs, as well as some other
  features. It is our understanding that currently no vision science toolkit exists that
  could provide any reliable or trustworthy operation on macOS for Apple Silicon. On
  Intel based Macs, Psychtoolbox likely continues to be the only toolkit with somewhat
  trustworthy visual stimulation timing on most Intel Mac configurations.

### Highlights:

- Further compatibility improvements and refinements to our new [OpenXR cross-platform,
  cross-vendor, cross-device support for VR/AR/MR/XR applications. A new modern foundation
  for these kind of things, highly extensible, future proof, and supports a much wider
  range of devices.](https://www.khronos.org/openxr)

### All:

- [The main new feature, after over 800 hours of development, spread over 13.75 months,
  is our new OpenXR driver for virtual reality, augmented reality and mixed reality
  applications, known as eXtended Reality.](https://www.khronos.org/openxr) The new
  PsychOpenXR driver should work on all VR/AR/MR/XR devices from all vendors on all
  operating systems which have an OpenXR 1 specification compliant runtime installed on
  your machine. So far the theory.

  In practice, this means GNU/Linux X11 and MS-Windows 10 and later. This new 3.0.19.1
  release has been further refined and now also tested for compatibility with the HTC
  Vive Pro Eye (and presumably similar HMDs from the Vive series), and the associated
  "Vive Wand" hand controllers. Proper working of our new driver on HMDs from two different
  VR hardware vendors - Oculus and HTC - should give good confidence that the new OpenXR
  driver really works cross-vendor. Testing with the HTC Vive Pro Eye was performed with
  Valve SteamVR 1.25.7 as OpenXR runtime on both Windows 10 22H2 and on Ubuntu Linux
  20.04.6-LTS, and additionally also with Monado (with vive and survive backends) under
  Ubuntu Linux 20.04.6-LTS.

- Improvements and fixes to all legacy VR drivers, and to VR test scripts and demos.

- Minor bug fixes and improvements.

- Various help text and documentation updates. Also spelling fixes to some code comments and
  docs contributed by Yaroslav Halchenko from the NeuroDebian project. He contributed some
  automatic spellchecking for our GitHub CI to reduce such mistakes over time.

- Fixes by Alex Forrence to allow building Python wheels from source more easily.

### Linux:

- Add support for 64-Bit Octave 8.x, implemented via the shared mex files for Octave 4.4 to
  Octave 8.x. This enables use with Octave on Ubuntu 20.04 - Ubuntu 23.04, and should also
  enable use on future Linux distributions. Note though that Octave 8.x compatibility is
  assumed at the moment, not actually tested, as upcoming Ubuntu 23.04 ships with Octave 7.3.

- Psychtoolbox was built and lightly tested against Matlab R2022b.

- Our new OpenXR driver now has the ability to provide accurate and trustworthy visual
  stimulus onset timestamps for VR HMD's - as tested with Oculus Rift CV-1 and HTC Vive Pro Eye
  and some photo-diode measurements. This however currently only works with Linux and only
  with Monado as OpenXR runtime, and only with a slightly modified Monado runtime and a special
  set of Mesa Vulkan drivers for AMD and Intel gpu's. It also comes at a performance cost.
  However, this combination of Psychtoolbox 3.0.19.1 and modified Monado + Mesa is to my
  knowledge the only existing modern VR system that can actually provide accurate and trustworthy
  timing and timestamping for VR applications on modern VR HMD's. Read "Help PsychOpenXR"
  for setup instructions. A proper non-hacky, easy to use solution to VR timing problems is
  still to be done and will require substantial amounts of work.

  As part of this work, the CV1Test.m script has been improved for VR related timing tests,
  and FlipTimingWithRTBoxPhotoDiodeTest.m now optionally can also test VR HMD's wrt. stimulus
  onset timing and timestamping. These test scripts were used to verify timestamping precision
  and reliability of the proprietary VR drivers (OculusVR, Oculus OpenXR, SteamVR OpenXR) or
  rather the terrible lack of reliability and precision, and the excellent reliability and
  precision of the hacked Monado OpenXR runtime on Linux.

- Basic Vulkan display backend support for RaspberryPi 4 and 400 with VideoCore-6 gpu. This
  is very basic right now, and requires special setup and use of Mesa Vulkan drivers built
  from Mesa source code, the build and install automated by use of PiKISS. See instructions
  under 'help RaspberryPiSetup'. This currently has little to no advantage over use of the
  standard OpenGL display backend. In fact, expect *way less trustworthy* visual timing and
  reduced graphics performance. The only use case at the moment would be convenient setup
  on a dual-display RaspberryPi 4/400 setup for experimenter GUI/mirror display + subject
  stimulus display, a split experimenter + subject configuration currently not supported by
  the standard display backend.

- Fixes for Mathworks latest Matlab bugs since R2022b, this time breaking our Vulkan support
  by shipping a totally outdated and crippled libvulkan.so.1 loader library that overrides
  the system provided full featured loader. `PsychLinuxSetup()` will now detect this and
  rename the library to fix Mathworks latest screwup.


### Windows:

- 64-Bit Intel MSVC GStreamer version 1.20.5 is now required as minimum supported version,
  and GStreamer 1.22.1 is now recommended as most modern version, and also as the only lightly
  tested version for 3.0.19. _High quality text rendering will fail with any earlier versions!_

- 64-Bit GNU/Octave 7.3 is required for running Psychtoolbox 3.0.19 on Octave, earlier or
  later versions won't work! Substantial technical difficulties were encountered when trying
  to upgrade Psychtoolbox for Windows to the brand-new Octave 8.1, forcing me to give up after
  over 15 hours of work. The lack of funding for any such troubleshooting and maintenance work
  means that Psychtoolbox will be frozen/locked to Octave 7.3 until significant funding for
  such compatibility work becomes available, or until the problem magically resolves itself,
  in other words possibly never.

- Psychtoolbox was built and lightly tested against Matlab R2022b.

- Compatibility fixes for `LoadIdentityClut()` with AMD graphics card drivers on Windows,
  contributed by GitHub user @qx1147. The contributor has the following to say about this fix:
  "Tested with several Windows 10 versions, AMD driver versions, video ports (DP, DVI, DP++/DVI)
  and AMD cards (HD-7750, R7-250X, R7-260X, RX-550, RX-6400, WX-5100) - although not all
  combinations of these." - The old code broke on a subset of these cards, depending on output
  port, card, driver versions and whatnot. This due to backwards incompatible changes that AMD
  apparently made to their display drivers gamma table and color conversion handling since
  summer/autumn 2017, when the same contributer last fixed `LoadIdentityClut()` for AMD driver
  changes which broke pixel identity passthrough. Example of a new bug, citing the contributor:
  "For example, for the Radeon RX550, the codes 9-254 would map to 8-253, but only for DP and
  DP++/DVI, whereas all is fine with DVI, at least with an older driver. With newer drivers,
  the mapping is also screwed up with DVI."


### macOS:

- Upgrade to the brand new 64-Bit GNU/Octave 8.1 is recommended for running Psychtoolbox 3.0.19.1
  on Octave. Other Octave versions from the Octave 6.3/6.4 and 7.x series, or future Octave 8.x
  versions, may work as well, but no guarantees for anything other than Octave 8.1.

- Psychtoolbox was built and lightly tested against Matlab R2022b.

- Compatibility fixes for new GStreamer 1.22 releases.

---
## [Sylius/Sylius](https://github.com/Sylius/Sylius)@[23b4abd530...](https://github.com/Sylius/Sylius/commit/23b4abd530ad3b985f4028dbeab869d004d9593f)
#### Wednesday 2023-12-20 09:33:36 by Jacob Tobiasz

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
## [Bananeweizen/eclipse-cs](https://github.com/Bananeweizen/eclipse-cs)@[757ee0447c...](https://github.com/Bananeweizen/eclipse-cs/commit/757ee0447cda1f39c916ad0ee6916daaee8e7eb5)
#### Wednesday 2023-12-20 10:10:26 by Michael Keppler

infra: convert UI libraries to maven

Convert also the external libraries used by the UI bundle to plain Maven
coordinates. Import the packages provided by the libraries with the
minimum package version matching the current library version.

The version number 1.0 for jfreechart-swt is not an error. The previous
jfreechart-1.0.19-swt was part of the jfreechart-1.0.19 (without SWT)
release. It has been split out into a separate project now with version
number 1.0 (so that new 1.0 is more recent than the old 1.0.19). That's
also where the change of the "experimental" package name comes from.

In a future change we should also upgrade the libraries, but I want to
do that separately, because I remember these libraries have trouble with
the module system and its restrictions.

And finally, the target platform has been split once more as suggested
in previous comments to have the root target file only include other
targets but not reference any library by itself.

---
## [Booking-Team29/ISS](https://github.com/Booking-Team29/ISS)@[991626fa03...](https://github.com/Booking-Team29/ISS/commit/991626fa03939d7d1b42abb05a9da3821736e9bb)
#### Wednesday 2023-12-20 10:47:50 by Teodor Đurić

Feature/working backend acc service (#22)

* end my suffering

* fix database scripts

* make every enum entry ALLCAPS

* fix decorator clusterfuck

* change all arrays to Lists; adjust factory methods

* fix stupid field name

* add foreign key reference

* remove stupid lazy loading method

* use eager loading method instead

---
## [LOSModified/android_frameworks_base](https://github.com/LOSModified/android_frameworks_base)@[947a38f7d0...](https://github.com/LOSModified/android_frameworks_base/commit/947a38f7d06c0a3be2e071189b587c45b732cb5d)
#### Wednesday 2023-12-20 11:03:11 by Adithya R

telephony: Force Class 0 SMS to Class 1

This kills Flash SMS messages. Fuck you airtel

Change-Id: Ifb0c9e8bae5c12868d178fbdaeceb2cc72a0ffb6

---
## [tesselslate/advent](https://github.com/tesselslate/advent)@[556f7ba482...](https://github.com/tesselslate/advent/commit/556f7ba482160268c34a37b534f0fc516ed2d1be)
#### Wednesday 2023-12-20 11:08:52 by tesselslate

2023: day 20 part 1

~20:45 part 1, shocked considering it's 5 am, was so slow understanding problem, silly bugs ... also lost 4 minutes to misunderstanding pulse order oops. i think i know how to do part 2 since i've been on it for a few minutes but it's a pain to implement, dunno if i will do it on my phone

---
## [Draconic-0/Nvim](https://github.com/Draconic-0/Nvim)@[2c88dd2de1...](https://github.com/Draconic-0/Nvim/commit/2c88dd2de168677cc82aaeb721a4388e63baa1d8)
#### Wednesday 2023-12-20 11:33:14 by gaphag

i dont even remember what changed so fuck you i guess

---
## [ynot01/Yogstation](https://github.com/ynot01/Yogstation)@[75c13f4eff...](https://github.com/ynot01/Yogstation/commit/75c13f4effbd82c8dc661c6b3bbc0146de44fded)
#### Wednesday 2023-12-20 12:21:29 by cowbot92

[PORT] Adds several more signs for the bar to use (#20997)

* yo fuck emisssives

that shit sucks

* sure the rest of these can come too

I guess

* no 100% orange juice

sorry

---
## [JulianKniephoff/annotation-tool](https://github.com/JulianKniephoff/annotation-tool)@[66e8ef6006...](https://github.com/JulianKniephoff/annotation-tool/commit/66e8ef6006dafafce422933214f714884d0885f7)
#### Wednesday 2023-12-20 12:31:41 by Julian Kniephoff

Get frontend dependencies from NPM instead of vendoring them

Not all of the libraries we were using could be found
(in the correct version) in NPM, so had to get creative
with some of them.

I tried to stick to our current versions as closely as possible,
except for some that were easy to update. Thus, most versions are
pinned instead of using the usual `^x.y.z` constraint. Only ones
where we are using a current version anyway, and where minor updates
should be fine use the more traditional constraint.

Here are the detailed notes about where dependencies (might have)
changed:

* `vis-timeline` should be in the correct version, but the NPM build
  is a few moments younger, and differs slightly. I hope it's just
  variable naming or something like that, but comparing minified JS
  is hard, so I'm not 100% sure.
* `jquery.colorPicker` (or rather `really-simple-colorpicker` as the
  NPM package is called) is newer, because the original version isn't
  in NPM. Our use of it is relatively isolated, though, and it still
  seems to work superficially, so I'm relatively confident that this
  is fine.
* `jquery.appear` was never actually in use, so I removed it.
* `jquery` itself is updated to `1.8.2`. We were on `1.8.0` which is
  not in NPM. `1.8.2` is, and that should be fine, but jQuery is one
  of these candidates that you can never really be sure about since it
  doesn't follow SemVer perfectly and is used so pervasively, that
  even checking all our usages against the changelog is basically
  impossible.
* `i18next-xhr-backend` was replaced with (the newest version of)
  `i18next-http-backend`. The former is deprecated and not in NPM
  anymore, but the update here is literally a drop in replacement,
  apparently.
* Our Bootstrap version (`2.3.2`) is so dead it's not even funny.
  No `2.x` release is in NPM. Fortunately in this case one can just
  install it directly from their GitHub using the appropriate tag,
  but this is a bit shady and I want to get rid of it sooner rather
  than later. Unfortunately upgrading Bootstrap is a rather invasive
  step.
* The Bootstrap slider thing we were using doesn't even have a GitHub.
  I replaced it with one that does, and which is based on our original
  one. I used the oldest release they have on GitHub, and seems to be
  more or less the same, still, but there have been significant code
  changes between the two. As with the color picker, this is a rather
  isolated thing, though, so we should be fine?
* The RequireJS `text` plugin wasn't used anymore, so I got rid of it.
* RequireJS `domReady` only has newer versions in NPM, but they seem
  to work fine, even though there was a major jump here.
* `moment` got a minor update because the version we were using was
  actually incompatible with our `vis-timeline` version, and our own
  few uses should still work exactly the same. Note that this is
  merely a convenience to make `npm install` work. We are using
  all of these libraries pre-bundled, so `vis-timeline` isn't actually
  using the version of `moment` we are including, but rather comes
  with its own.

Fixes #138.
Fixes #457.

---
## [acroreiser/android_kernel_lenovo_a6010](https://github.com/acroreiser/android_kernel_lenovo_a6010)@[5461827fdb...](https://github.com/acroreiser/android_kernel_lenovo_a6010/commit/5461827fdbf39fe3909d2cc7d08133dc9f3794a7)
#### Wednesday 2023-12-20 13:03:58 by Michal Hocko

oom: add helpers for setting and clearing TIF_MEMDIE

This patchset addresses a race which was described in the changelog for
5695be142e20 ("OOM, PM: OOM killed task shouldn't escape PM suspend"):

: PM freezer relies on having all tasks frozen by the time devices are
: getting frozen so that no task will touch them while they are getting
: frozen.  But OOM killer is allowed to kill an already frozen task in order
: to handle OOM situtation.  In order to protect from late wake ups OOM
: killer is disabled after all tasks are frozen.  This, however, still keeps
: a window open when a killed task didn't manage to die by the time
: freeze_processes finishes.

The original patch hasn't closed the race window completely because that
would require a more complex solution as it can be seen by this patchset.

The primary motivation was to close the race condition between OOM killer
and PM freezer _completely_.  As Tejun pointed out, even though the race
condition is unlikely the harder it would be to debug weird bugs deep in
the PM freezer when the debugging options are reduced considerably.  I can
only speculate what might happen when a task is still runnable
unexpectedly.

On a plus side and as a side effect the oom enable/disable has a better
(full barrier) semantic without polluting hot paths.

I have tested the series in KVM with 100M RAM:
- many small tasks (20M anon mmap) which are triggering OOM continually
- s2ram which resumes automatically is triggered in a loop
	echo processors > /sys/power/pm_test
	while true
	do
		echo mem > /sys/power/state
		sleep 1s
	done
- simple module which allocates and frees 20M in 8K chunks. If it sees
  freezing(current) then it tries another round of allocation before calling
  try_to_freeze
- debugging messages of PM stages and OOM killer enable/disable/fail added
  and unmark_oom_victim is delayed by 1s after it clears TIF_MEMDIE and before
  it wakes up waiters.
- rebased on top of the current mmotm which means some necessary updates
  in mm/oom_kill.c. mark_tsk_oom_victim is now called under task_lock but
  I think this should be OK because __thaw_task shouldn't interfere with any
  locking down wake_up_process. Oleg?

As expected there are no OOM killed tasks after oom is disabled and
allocations requested by the kernel thread are failing after all the tasks
are frozen and OOM disabled.  I wasn't able to catch a race where
oom_killer_disable would really have to wait but I kinda expected the race
is really unlikely.

[  242.609330] Killed process 2992 (mem_eater) total-vm:24412kB, anon-rss:2164kB, file-rss:4kB
[  243.628071] Unmarking 2992 OOM victim. oom_victims: 1
[  243.636072] (elapsed 2.837 seconds) done.
[  243.641985] Trying to disable OOM killer
[  243.643032] Waiting for concurent OOM victims
[  243.644342] OOM killer disabled
[  243.645447] Freezing remaining freezable tasks ... (elapsed 0.005 seconds) done.
[  243.652983] Suspending console(s) (use no_console_suspend to debug)
[  243.903299] kmem_eater: page allocation failure: order:1, mode:0x204010
[...]
[  243.992600] PM: suspend of devices complete after 336.667 msecs
[  243.993264] PM: late suspend of devices complete after 0.660 msecs
[  243.994713] PM: noirq suspend of devices complete after 1.446 msecs
[  243.994717] ACPI: Preparing to enter system sleep state S3
[  243.994795] PM: Saving platform NVS memory
[  243.994796] Disabling non-boot CPUs ...

The first 2 patches are simple cleanups for OOM.  They should go in
regardless the rest IMO.

Patches 3 and 4 are trivial printk -> pr_info conversion and they should
go in ditto.

The main patch is the last one and I would appreciate acks from Tejun and
Rafael.  I think the OOM part should be OK (except for __thaw_task vs.
task_lock where a look from Oleg would appreciated) but I am not so sure I
haven't screwed anything in the freezer code.  I have found several
surprises there.

This patch (of 5):

This patch is just a preparatory and it doesn't introduce any functional
change.

Note:
I am utterly unhappy about lowmemory killer abusing TIF_MEMDIE just to
wait for the oom victim and to prevent from new killing. This is
just a side effect of the flag. The primary meaning is to give the oom
victim access to the memory reserves and that shouldn't be necessary
here.

Signed-off-by: Michal Hocko <mhocko@suse.cz>
Cc: Tejun Heo <tj@kernel.org>
Cc: David Rientjes <rientjes@google.com>
Cc: Johannes Weiner <hannes@cmpxchg.org>
Cc: Oleg Nesterov <oleg@redhat.com>
Cc: Cong Wang <xiyou.wangcong@gmail.com>
Cc: "Rafael J. Wysocki" <rjw@rjwysocki.net>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>

---
## [discourse/discourse](https://github.com/discourse/discourse)@[cbc28e8e33...](https://github.com/discourse/discourse/commit/cbc28e8e337acc740487bc9cf5c263b3eaba6493)
#### Wednesday 2023-12-20 13:15:08 by David Taylor

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
## [pivovarit/AoC_2023_go](https://github.com/pivovarit/AoC_2023_go)@[f6fcf67ce5...](https://github.com/pivovarit/AoC_2023_go/commit/f6fcf67ce5323aa8ac8756612c57c67c21373391)
#### Wednesday 2023-12-20 13:20:33 by Grzegorz Piwowarek

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
## [Paxilmaniac/Skyrat-tg](https://github.com/Paxilmaniac/Skyrat-tg)@[2fa469566c...](https://github.com/Paxilmaniac/Skyrat-tg/commit/2fa469566c615cdc3cbdfacb03db42142d30c7cf)
#### Wednesday 2023-12-20 13:55:11 by SkyratBot

[MIRROR] Balance changes to swords, energy shields and modsuit shields. [MDB IGNORE] (#25531)

* Balance changes to swords, energy shields and modsuit shields. (#80072)

## About The Pull Request

### Sword Weaponry

Mundane sword weapons of all sorts do not block ``LEAP_ATTACK`` attacks
whatsoever. These attacks include tackles, xeno tackles and bodythrows.

Energy swords and double energy swords only gain 25% block probability
against such attacks.

### Double Energy Sword

No longer grants outright energy projectile immunity while employed.
Instead, it just has a high probability of reflecting (the typical 75%
to block any other attack). So, very solid defense against energy
projectiles, but not immunity.

Against non-reflectable projectiles, like ballistics or nanite bullets,
the desword only has 50% block, similar to an energy sword.

To compensate for the loss of defensive power, we'll make it all the
more rewarding for getting on top of someone with the sword by giving it
40 force while active. And also it costs 13 TC.

### Combat Energy Shield

This also lost outright energy projectile immunity, but gained the
standard blocking power of shields on top of the ability to reflect
energy projectiles when they block them. This significantly increases
the shields potential effectiveness while no longer pigeonholing the
shield to only energy weapons. (This makes them exceptionally good
against tackles and body throws, by the by).

Deathsquads still have the perfect deflection energy shield so that they
can continue to spam pulse shots with impunity.

### MODsuit Shield Module

Only has one charge instead of three, but it recharges in half the time.
This is no longer such a perfect defense, and does somewhat need you to
be thinking about how you're utilizing the shield rather than not
thinking about defense at all by barreling forward under three potential
hits worth of protection.

Also much cheaper, at almost half price of 8 TC. Because of how cheap it
is (and how much it still is necessary to keep you alive), I've put it
into the core equipment box (which brings the price up to 22 TC. As a
reminder, this is not meant to be at any discount, and is more aimed
towards teaching newer players which items contribute towards success.
If you don't want all the times within, don't buy this box, just buy
what you want separately.)

## Why It's Good For The Game

This is a doozy of an explanation, I hope you're ready for it under the
spoiler.
<details>
With my tackling and bodythrow prs, numerous people expressed
exasperation at the fact that these two tools may have been keeping some
outlier antagonist gear from becoming too easy to steamroll with if you
already knew what you were doing. My intent was to create consistent
rules and behaviours that both A) did not rely on bugs to keep the
balance of power from tipping one way or the other, and B) was at least
consistent or had consistent rules established.

This PR is tackling overperforming gear combinations for already
competent nukies that may have, over time, crept out of control, and
applying some consistency to the rules around similar equipment.

AND also deals with quite possibly the most braindead element of game
design we've tolerated for about a decade, and half a decade after it
was necessary to maintain that decision.

Part of the culprit of this issue is that, specifically in regards to
nukies, crew can't use the vast majority of their weapons effectively
against them. This largely is because this antagonist can gain
immunities to those types of equipment. And that is rapidly increasing
as we move closer towards outright ballistic removal. I don't think the
game is made healthier by everyone on the station having to fight armed
mercenaries with spears, and doesn't make much thematic sense either.
More so, most greener players probably just don't know this is how it
works, and so surprise Pikachu when their lasers bounce off nukies
harmlessly. (This bit reminds me of the problem of new players using
disablers against simple mobs)

But of course, that isn't the only part of the problem. The other half
is due to being able to be layered on a much more broad defensive tool
in the form of the MODsuit Shield Module, whose three charges could
render the mindful nukie near untouchable if they're pairing it with
some other layered defense, such as a desword. Notice that this doesn't
really address armor. The culprit is negation, and not mitigation, and
we should be sparing in how easily we hand out outright effect negation
simply because it isn't super obvious to a new player why it happened,
and how to resolve it. At the very least, we should look to find ways to
add options for players to overcome these problems. Especially with
teamwork.

Energy projectile immunity made sense while there floated around an
energy projectile that ostensibly would down you in a single shot.
Nukies ALSO had projectile weapons that worked much the same (c-20r stun
bullets, taser shot bulldogs, etc.), so it was predominantly
tit-for-tat. These immunity granting equipment pieces forced crew
members to get shotguns and ballistic guns to fight these dangers;
something more available at the time.

We've exercised large bits and pieces of this from the game a long time
ago, but we still have some remnants convinced we're still in a
taser-rich, ballistic available environment. We need to move the games
languishing tools into the modern era and re-established their place in
the game. Namely, the double-energy sword and the combat energy shield
are almost entirely unchanged besides refactors for the last decade or
so, even while the game around them have changed. They've been a
continuous sore point for me in all my time developing and a constant
nagging issue. I want to deal with it now.

MODsuit Shield Module is just kind of really good and only made stronger
the more defenses you have. It's good to have a defense like this, but I
think it is too brain dead. With only one charge, it will save you from
a lost joust here and there, but it won't make it as simple as running
right at every problem you encounter and eating a volley of attacks
while you kill someone with impunity.

**With regards to traitors**, since they also get double-energy swords;
I'm open to suggestions if this is hitting them far too hard, but I'm
not terribly concerned using this weapon for a few reasons. **Firstly**,
I think their presence amongst the crew make it a much better weapon for
tots than nukies (in isolation) simply because they can find ways to
exploit it via tools they gather from the station. It is a force
multiplier. Traitors also have a much bigger element of surprise
usually. **Secondly**, round-start traitors typically grow to be a bit
stronger over time, but I don't foresee many waiting to pay for the
double-energy sword unless they're already flush with TC. So if a
traitor is in a position after they've unlocked access to it to buy one
of these, they are probably doing pretty okay for themselves.
</details>

### TL;DR

Defense stacking and attack immunities are not particularly healthy
things to both design around, or experience in-game. They are kind of
just relics of the past made only sorer once I ripped off a few
bandaids. This is a source of a number of symptomatic issues in the
game, so let's fix that and make it easier on all of us going forward.

Much of the way these things worked operated on extremely outdated
design considerations. It doesn't make sense for them to work like this
today, and only makes things harder by keeping the status quo.

## Changelog
:cl:
balance: Mundane sword-like and medieval weapons are not able to block
tackles, xenomorph tackles and body throws.
balance: The double-energy sword and energy sword have trouble blocking
physical projectiles, body throws and tackles.
balance: The double-energy sword also no longer has guaranteed energy
projectile deflection; only doing so on a successful block (75% chance
to block).
balance: But it does have 40 force now, so it is more lethal a weapon.
Traitors can purchase the sword for only 13 TC (down from 16 TC).
balance: The combat energy shield (The one you hold) now functions as a
normal shield (it used to only protect you against energy projectiles
and nothing else). It loses guaranteed energy projectile deflection, but
still reflects the projectile so on a block.
feature: Death commandos continue to have their energy shields deflect
all incoming energy projectiles. Because who cares about deathsquads
being balanced?
balance: The MODsuit shield module only has one charge, but recharges
every 10 seconds. It also costs 8 TC (down from 15). It is also now in
the Core Gear beginner box (bringing the total price up to 22 TC).
/:cl:

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@ users.noreply.github.com>

* Balance changes to swords, energy shields and modsuit shields.

---------

Co-authored-by: necromanceranne <40847847+necromanceranne@users.noreply.github.com>
Co-authored-by: MrMelbert <51863163+MrMelbert@ users.noreply.github.com>

---
## [ColinIanKing/linux-next](https://github.com/ColinIanKing/linux-next)@[2fcd38f4de...](https://github.com/ColinIanKing/linux-next/commit/2fcd38f4de7256e2b5cb23ad22a6e3ebfea7dd18)
#### Wednesday 2023-12-20 14:13:24 by Al Viro

[software coproarchaeology] dentry.h: kill a mysterious comment

there's a strange comment in front of d_lookup() declaration:

/* appendix may either be NULL or be used for transname suffixes */

Looks like nobody had been curious enough to track its history;
it predates git, it predates bitkeeper and if you look through
the pre-BK trees, you finally arrive at this in 2.1.44-for-davem:
  /* appendix may either be NULL or be used for transname suffixes */
 -extern struct dentry * d_lookup(struct inode * dir, struct qstr * name,
 -                               struct qstr * appendix);
 +extern struct dentry * d_lookup(struct dentry * dir, struct qstr * name);
In other words, it refers to the third argument d_lookup() used to have
back then.  It had been introduced in 2.1.43-pre, on June 12 1997,
along with d_lookup(), only to be removed by July 4 1997, presumably
when the Cthulhu-awful thing it used to be used for (look for
CONFIG_TRANS_NAMES in 2.1.43-pre, and keep a heavy-duty barfbag
ready) had been, er, noticed and recognized for what it had been.

Despite the appendectomy, the comment remained.  Some things really
need to be put out of their misery...

Signed-off-by: Al Viro <viro@zeniv.linux.org.uk>

---
## [FalloutFalcon/Shiptest](https://github.com/FalloutFalcon/Shiptest)@[247a4e02ea...](https://github.com/FalloutFalcon/Shiptest/commit/247a4e02eab24ccfa191ea0447e587aeaf4c1235)
#### Wednesday 2023-12-20 14:58:40 by BluBerry016

{Icemoon, Ruin} The Crashed Holemaker (#2413)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Adds a brand-new - well, [new to
shiptest](https://cohost.org/bluwu016/post/885120-a-compilation-of-my) -
ruin to the Icemoon roster, focused on the service department.

It's flavored around being an *incredibly* old NT Spaceworks vessel
that's been carved in half and crashed - what's present only being the
fore of the ship. Being mainly service-focused, it's loot is pretty dry
~~as is it's sole threat.~~
If more current-day mappers/balance-heads have any words about how to
fluff out either of those pools a bit more with the screenshots below,
lemme know. I'll listen well.

(Notarized loot summary removed as updating it was a pain in the ass,
lmao.)

It strikes me as leaning on the underwhelming side from looking at the
other ruins present here but we'll. See? I suppose? It's good practice
for me in the whole, "making something I have memorized and that looks
good normally look sicker ruined".

<details><summary>Pictures (All but SDMM Outdated)</summary>
<p>

Ignore that there's no rust, the firelocks are open here, and some
stuff's knocked around, I was testing it prior to me tacking the rust on
and took pics after running around it in-person.


![image](https://github.com/shiptest-ss13/Shiptest/assets/50649185/51a3cc54-1727-4241-9592-639f892621bf)


![image](https://github.com/shiptest-ss13/Shiptest/assets/50649185/580e39fe-bbf9-481f-aff8-cc25f860638d)

StrongDMM View:

![2023-11-09 15 02
20](https://github.com/shiptest-ss13/Shiptest/assets/50649185/5b94af63-d2d8-42bd-a823-0d300d66191f)

</p>
</details> 
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
This isn't what I intended to do when I was like, "oh yeah, I have a
goofy ahh downstream out of boredom, ya'll want some of our better
ships" but w/e here it is anyways. Ya'll need ruins. I made (another)
ruin.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: A new icemoon ruin has been added, should you be in need of service
department goodies.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Signed-off-by: BluBerry016 <50649185+unit0016@users.noreply.github.com>

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[ad2f842db2...](https://github.com/treckstar/yolo-octo-hipster/commit/ad2f842db23477a675b4224a0974f8cf6bbfca8c)
#### Wednesday 2023-12-20 15:22:04 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [frosty-dev/tgstation](https://github.com/frosty-dev/tgstation)@[b17f9d7086...](https://github.com/frosty-dev/tgstation/commit/b17f9d708654caebe332727278d0b7d06e18f70c)
#### Wednesday 2023-12-20 16:12:13 by Jeremiah

Replaces prettierx with the normal prettier (#80189)

Oh god the file diff... I'm so, so sorry.

No need to worry though. This just replaces the prettierx version that
we were using and replaces it with normal prettier. Most of the settings
were default or no longer valid with this version.
You no longer get this warning #70484

It actually drives me up the wall and I have to click it each time I
open my editor.
N/A nothing player facing

---
## [Ephemeralis/Skyrat-tg](https://github.com/Ephemeralis/Skyrat-tg)@[41026ae8b1...](https://github.com/Ephemeralis/Skyrat-tg/commit/41026ae8b1a14b9380ca7af9885939c9f2dc060e)
#### Wednesday 2023-12-20 17:59:17 by SkyratBot

[MIRROR] Replaces the fake monkey cube in Birdshot tool storage with a less lethal one, adds something else fun [MDB IGNORE] (#25365)

* Replaces the fake monkey cube in Birdshot tool storage with a less lethal one, adds something else fun (#80030)

## About The Pull Request
One of the "monkey cubes" in Birdshot's tool storage was actually a
gorilla cube. This was funny up until people realized it was a thing and
now people are using it intentionally to grief. I'd rather not.

It's a different cube now. I don't want to spoil it but it won't kill
anyone, just make people laugh.

I added a different fun item to another tile in tool storage. Again, no
spoilers, read the code if you really want to know what it was.

## Why It's Good For The Game
I like the "cube says it's a monkey but it's not" joke. It was funny
when people thought it was a monkey, used it, and got killed by it.
Problem is, people know what it is now and have used it for grief
purposes, so we can't have nice things. Gorillas are stupid hard to kill
and will de-limb people by looking at them.

I wanted to add something else fun to replace it that isn't just the
exact same joke but now it won't kill you, so I did.

## Changelog
:cl: Vekter
del: Replaced the "monkey cube" in Birdshot's tool storage with a
different "monkey cube".
add: Added a fun surprise item to Birdshot's tool storage to compensate
for the above change.
/:cl:

* Replaces the fake monkey cube in Birdshot tool storage with a less lethal one, adds something else fun

---------

Co-authored-by: Vekter <TheVekter@users.noreply.github.com>

---
## [petre-symfony/30-Days-with-Last-Stack-2023](https://github.com/petre-symfony/30-Days-with-Last-Stack-2023)@[bb0e3fc574...](https://github.com/petre-symfony/30-Days-with-Last-Stack-2023/commit/bb0e3fc57422ee37b04d48549cb23378d0362b6d)
#### Wednesday 2023-12-20 18:08:52 by petrero

12.1 Auto-Submitting Forms

 Day 12 already? Over the next 3 days, we're going to work on one, big goal: transforming this table into a rich data-table setup, with searching, column filtering, pagination, all happening with beautiful AJAX. This is one of the parts I'm most excited to dive into.

 Our homepage does have a search. And there's nothing particularly special about it. I hit enter to submit the form, the query parameter is in the URL, and it filters the results. Naturally, thanks to Turbo Drive, it all happens via AJAX.

 For our first trick, watch as we make the search update automatically as we type. So we type and, without hitting enter, the list should update.

 To do this, we're going to borrow a controller from a 30 Days of Hotwire repository. This comes from a fantastic 30 Days of Hotwire challenge that someone from the Rails community did. I love this series and it has a ton of good stuff. I highly recommend checking it out.

 The autosubmit Stimulus Controller
 - Anyway, I'm going to borrow this great "auto-submit" controller. It's dead-simple: it gives us a way to submit a form... with optional debouncing. If I type really quickly, I don't want to submit the form four times. I want it to wait for a slight pause... and then submit. That's called debouncing. This waits for a 300 millisecond pause.

 So let's roll up our sleeves and get this into our app. Create a new file called autosubmit_controller.js... then paste

 Then head to the homepage to use it. Near the top... here's our search form. On the form, add data-controller="autosubmit"

 Notice I'm getting auto-complete on that. That's thanks to a Stimulus plugin I have for PhpStorm.

 Next, down on the input, say data-action equals autosubmit#debouncedSubmit

 In the controller, you can call submit to submit the form immediately or debouncedSubmit() to wait for the pause. And we don't need to include the event name this time - like input-> to listen to the input event. When you apply a data-action to an input, a button or a link, Stimulus figures out which event you want to listen to. Most of the time, life will be simple like this.

---
## [petre-symfony/30-Days-with-Last-Stack-2023](https://github.com/petre-symfony/30-Days-with-Last-Stack-2023)@[c3bc2be1b7...](https://github.com/petre-symfony/30-Days-with-Last-Stack-2023/commit/c3bc2be1b7db68b0ad9ce29348c302793f05319b)
#### Wednesday 2023-12-20 18:08:52 by petrero

14.1 Data Tables with Turbo Frames

 Our data tables-like setup is working. And it's almost awesome. What I don't love is how it jumps around. Every time we click a link, it jumps back to the top of the page. Boo.

 That's because Turbo is reloading the full page. And when it does that, it scrolls to the top... because that's usually what we want! But not this time. I want our data table to work like a little application: where the content changes without moving around.

 Turbo 8 Morphing?
 - There are two great ways to solve this. In Turbo 8 - which is not released yet, it's Beta 1 at the time of recording this - there's a new feature called page refreshes that leverages morphing. Without nerding out too much - and I want to - when navigating to the same page - like our search form, column sorting and pagination links all do - we can tell Turbo to only update the content on the page that changed... and to preserve the scroll position. So, keep an eye out for that.

 Adding a Turbo Frame
 - The second way - which works fantastically today - is to surround this entire table with a <turbo-frame>. In homepage.html.twig, find the table. Here it is: this div represents the table. Above it, add <turbo-frame id="voyage-list">. Indent this div... and also these pagination links: we want those to be inside the Turbo frame so that when we click on them, they advance the frame & update

 Let's try this. Zap that search clear. And oh... beautiful. Look at that! Everything moves within the frame. Try pagination. That too! All of our links point back to the homepage... and the homepage, of course, has this frame.

 But remember: now that this table lives inside a Turbo frame, if we have any links inside, they'll stop working. Again, to fix that, on each link, add data-turbo-frame="_top". Or to be more conservative, go up to the new <turbo-frame> and add target="_top". If you do that, you'll also need to find the sorting and pagination links that should navigate the frame and add data-turbo-frame="voyage-list".

 But I'll remove those... because we don't have any links in the table.

---
## [petre-symfony/30-Days-with-Last-Stack-2023](https://github.com/petre-symfony/30-Days-with-Last-Stack-2023)@[93ca57ca8e...](https://github.com/petre-symfony/30-Days-with-Last-Stack-2023/commit/93ca57ca8eab21b925253c1d88a4bba96535b396)
#### Wednesday 2023-12-20 18:08:52 by petrero

13.8 Adding the Column Sorting Links
 - The most tedious part is transforming each th into the proper sort link. Add an a tag and break it onto multiple lines. Set the href to this page - the homepage - with an extra sort set to purpose: the name of this column. For sortDirection, this is more complex: if sort equals purpose and sortDirection is asc, then we want desc. Otherwise, use asc.

 Finally, in addition to the sort and sortDirection query parameters, we need to keep any existing query parameters that might be present - like the search query. And there's a cool way to do this: ... then app.request.query.all

 Done! Oh, but after the word Purpose, let's add a nice down or up arrow. To help, I'll paste a Twig macro. I don't often use macros... but this will help us figure out the direction, then print the correct SVG: a down arrow, an up arrow, or an up and down arrow

 Down here... use this with {{ _self.sortArrow() }} passing 'purpose', sort and sortDirection

 Phew! Let's repeat all of this for the departing column. Paste, change purpose to leaveAt, the text to Departing... then use leaveAt in the other two spots

 So, all pretty boring code, though it was a bit of work to get this set up. Could we have some tools in the Symfony world to make this all easier to build? Probably. That would be a cool thing for someone to work on.

 Moment of truth! Refresh. That looks good. And it works great! We can sort by each column... we can paginate. Filtering keeps our page... and keeps the search parameter. It's everything I want! And it's all happening via Ajax! Life is good!

 The only hiccup now? That awkward scrolling whenever we do anything. I want this to feel like a standalone app that doesn't jump around. Tomorrow: we'll polish this thanks to Turbo Frames.

---
## [petre-symfony/30-Days-with-Last-Stack-2023](https://github.com/petre-symfony/30-Days-with-Last-Stack-2023)@[babefa6c7c...](https://github.com/petre-symfony/30-Days-with-Last-Stack-2023/commit/babefa6c7ca0bd27d6d009f64fd2707ffac772ba)
#### Wednesday 2023-12-20 18:08:52 by petrero

14.5 Advancing the Frame
 - Is this mission accomplished? Nearly. There's one gigantic, horrible problem... with an easy solution. When we search or sort or paginate, the URL doesn't change. That's the default behavior of Turbo frames: when they navigate, they don't update the URL. However, we can tell Turbo that we want this. On the Turbo Frame, add data-turbo-action="advance"

 Advance means that it will update the URL and advance the browser history so that if we hit the "Back" button, it'll go the previous URL. You can also use replace to change the URL, but without adding to the history.

 Watch: this time when we search... the URL updates! And as we navigate to page two or three... it updates... and we can hit back, back, and forward, forward.

 We now have a truly fantastic data tables setup... entirely written without any custom JavaScript inside of Twig and Symfony. What a time to be alive.

 The final teensy problem is this "30 results". As we search, that never changes: it's stuck on whatever number was there when the original page loaded. That's because this lives outside the Turbo frame. The easiest fix would be to move it into the frame... but I don't want it there! Visually, I want it up here!

 We're going to leave that for now. But we'll fix it in a few days with Turbo Streams.

 Tomorrow, we're going to dive into a brand-new browser feature! It's called View Transitions, and it'll let us apply visual transitions to any navigation.

---
## [fourlastor-forks/libgdx](https://github.com/fourlastor-forks/libgdx)@[e1d1fdc5fb...](https://github.com/fourlastor-forks/libgdx/commit/e1d1fdc5fb5b8409dc74f638c633ead405e535f3)
#### Wednesday 2023-12-20 18:59:32 by Tommy Ettinger

I18NMessageTest needs to reset I18NBundle static state. (#7101)

* Mark PauseableThread as excluded on GWT.

* Minor typo corrections.

* Fix atan2() when it should produce 0f.

Without this small change (which has essentially no performance impact that I could measure), calling atan2() with a point on the x-axis would produce a small but non-zero result, which is incorrect.

* Add atan, atan2, asin, acos for degrees.

This also includes atan2Deg360(), which in my opinion is the most useful of these because it does something differently from Math.atan2(), and can often save some effort.

* Approximations for tan() and tanDeg().

Sorry this is so long-winded, but the error isn't as straightforward to express as with sin() or cos().

* Apply formatter

* Add to MathUtilsTest.

* Apply formatter

* Stop trying to load defaults from wrong dir.

This old behavior broke Flame's effect-open dialog when any particle effect used the default billlboard or model particle. Now Flame tries to load a file given its absolute path (like before), but if it fails, it falls back to trying the default filenames as internal files.

* I18NMessageTest needs to reset I18NBundle state.

If you run I18NSimpleMessageTest and then I18NMessageTest without this PR, then the first test will have called I18NBundle.setSimpleFormatter(true), but the second test needs it to be set to false.

Because the tests are still perfectly usable if you run them on their own (or use LWJGL2, I think, because it might not share static state), this is not at all a priority to merge; it just makes running many tests in one session not throw an Exception.

---------

Co-authored-by: GitHub Action <action@github.com>

---
## [petre-symfony/30-Days-with-Last-Stack-2023](https://github.com/petre-symfony/30-Days-with-Last-Stack-2023)@[e45aaa275d...](https://github.com/petre-symfony/30-Days-with-Last-Stack-2023/commit/e45aaa275dde3ae21f4678dc8d3fe3787d2fd869)
#### Wednesday 2023-12-20 19:09:13 by petrero

15.1 View Transitions

 Day 15! We're already halfway through our adventure. And it only gets cooler from here.

 To celebrate, today we'll work on something sparkly & new: the View Transitions API. This nifty new feature is supported in most browsers and allows us to have smooth transitions whenever any HTML changes on our page.

 Tip

 Actually, as of Dec 2023, view transitions are supported only in Chrome with support in Firefox and Safari reportedly planned.

 And if your user has a browser that doesn't support it, that's ok! The transition is just skipped, but everything keeps working. No biggie.

 Oh, and, View Transitions will come Standard in Turbo 8 for full page navigation. Though, we'll take them even a bit further.

 Evil Martians & Demoing View Transitions
 - To use View Transitions, you do not need any external library. But we're going to use one called "turbo view transitions". This came out of a blog series where the author built a neat project called Turbo Music Drive. In two blog posts on Evil Martians, they talk all about morphing and doing crazy stuff with it in Turbo. They even created a live demo!

 In the simplest form, view transitions adds a crossfade as you navigate. But you can also get more specific and connect elements between pages to give them a special transition. Watch: when I click this album, it moves up to the left. There's also a nice crossfade for the rest of the page.

 Installing turbo-view-transitions
 - So let's try this out! Step one, get the turbo-view-transitions library. At your terminal, run:

  php bin/console importmap:require turbo-view-transitions

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[5617995d70...](https://github.com/TaleStation/TaleStation/commit/5617995d70b4853dcc7aaae4d4a263a5c55dcfb1)
#### Wednesday 2023-12-20 19:12:44 by TaleStationBot

[MIRROR] [MDB IGNORE] Roundstart AIs are positronic (#9076)

Original PR: https://github.com/tgstation/tgstation/pull/80355
-----
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

Co-authored-by: Jacquerel <hnevard@gmail.com>
Co-authored-by: John Willard <53777086+JohnFulpWillard@users.noreply.github.com>

---
## [Scrambledeggs00/Yogstation](https://github.com/Scrambledeggs00/Yogstation)@[5c140d7624...](https://github.com/Scrambledeggs00/Yogstation/commit/5c140d7624b7b9f904d5bd78602d2fb0ee33a9ec)
#### Wednesday 2023-12-20 19:36:19 by Aquizit

[ICEMETA] Fixes Hermit and Walker Spawns (Walkers disabled in config see PR text) (#21065)

* name + config fixes

* fix walker - disabled, redo hermit flavor text

* fuck your stupid uncapitalized t

---
## [wrye-bash/wrye-bash](https://github.com/wrye-bash/wrye-bash)@[59a1a04dd1...](https://github.com/wrye-bash/wrye-bash/commit/59a1a04dd1510fb6da9c88ede9dd3ba27061c240)
#### Wednesday 2023-12-20 19:45:09 by MrD

Squashed version of ut-353-pt1-578:

Refactoring in load order:

Move  the logic of _filter_active in callers - they were doing the checks
anyways - then inline - we certainly want to thin LoGame API, _games_lo
is complex enough and flat is better (and shorter) than nested here.

_CleanPlugins(LoGame):

Clean/create logic is very hard to follow - let's confine it to games that
need it. We then need to clarify what happens with cached parameters vs
creating the plugins txt - AsteriskGame._fetch_load_order logic is still
hard to follow see todos added there.

EAFP for parsing mod file

Then I realized that since 96394dda9179188825cc184ea84d689bda667824
actually for Textfile games we only need to remove the master_path,
so _active_entries_to_remove is only needed in AsteriskGame - then
_clean_actives, which for Asterisk necessarily cleans
the whole plugins.txt, is inlined taking down tricky logic and lots
of comments trying to explain what goes on.

Oh lord_func:

I. Use the return value:

This necessitated returning from _update_cache -> refresh_lo (single
use). For now I return the cached_lord - this is temporary, we will
eventually confine cached_lord to load_order.py, but we need to forge
a ring for that - that's part II.

quiet WIP:

get_load_order had quiet=False effectively - added this as default to
fix_load/active and then in set_load_order quiet=True and set it only
in load_order.save_lo

Became clear that warn_missing_lo_act was only updated when quiet was
False which was when lo_deprint was called. This simplified the bolts
of _game_lo at the expense of a local modInfos import - nice.

The timestamp game _fix_load_order override was tricky to get - if fix_lo
was None, which only happened in _restore_lo (quiet=True and
set_load_order validation) and in refresh_lo (for validation of a saved
load order), it would not reorder the added plugins but add them to the
end - I kept that but dropped the debug message as anyway the lo_added
will be printed. What we should do when a plugin is added needs
standardizing - makes sense to add them at the end so saves show blue.

Mopy/bash/basher/__init__.py: nit, better reset a dialog trigger before
showing the dialog lest one falleth into an infinite loop.

Expose more LoadOrder attributes:

The index dicts contain all the info of load order/active changes - as
a bonus a couple one-line, one-use methods were removed. load_order.py
is the balt of load order handling and although (because of saved load
order handling) it does have a well defined role it still needs to be
kept at a minimum - more on this later.

Simplify/optimize _refresh_mod_inis:

No need to clean up since we overwrite at the end - pruned also the OD.

Only the values of _plugin_inis was used - this will re-become a dict
but for now simplify and make easier to track by exposing it and
removing essentially nothing-new ini_files (not the ini_files.py
module).

WIP refactor BP activations handling:

count would decide on refreshing saves - probably if any mods got
activated we should DO. Moved the info handling higher up, I need to do
activations in parent.

Reduce occurrences of lo_activate (2)/cached_lo_save_active (1) - these
must be further confined. Note the decoupling from load_order (and Link)
in patcher_dialog.py

_modTimesChange -> unlock_lo - mod redates fix:

Was unlocking in all except one case - in those cases unlocking made
only sense if the game was a timestamp game - I am glad I kept
_modTimesChange and gladder I dropped it

Needs some testing as there are subtle changes in the logic - note that:

mod_links.py: we wouldn't unlock. That was actually a bug (if lock load
order was on) as the redates would silently be reverted in refresh_lo
(with no change shown in the UI) and then a dialog would be displayed on
*next time* we would tab in to Bash (still no change in the UI).
That was probably not the intention :P

Mopy/bash/basher/app_buttons.py: while we did unlock always we did not
forceRefresh - well it's a couple stats() added, won't harm

The rest is fine - just one more use of using_txt_file, inside the same
(DoSave) scope - good sign.

Mopy/bash/basher/installers_links.py: the (not so) long term goal is to
absorb this into refresh - need to refactor base signature for this.

WIP setGhost return status change: RRR TTT drop notify bain?

This gets us rid of a few uglyStuff including a Path method (# RRR 368), and
one bare except - we might as well deprint out (and maybe tighten the
remaining except).

As seen in _refresh_from_data_dir we chop off the ghost extension so we
should not notify BAIN TTT cause data_sizeCrcDate is difficult to track,
hence WIP see next commit

Under # RRR 219

isGhost -> is_ghost:

Now that autoGhost is (will) be gone

Some nit - in particular no need to create these (None, None, None) tuples

Drop _reset_info_sets: TTT EEE Mopy/bash/basher/files_links.py

Finally, this set up was a smell. This makes some calls like new_info
more expensive but no worries

TTT new_info: the _in_refresh param is obviously a temp hack :P

WIP decide what we need to refresh in restore backup:

This is partial (new_info is the hardest to absorb in refresh from the
refresh satellites). No need to further dig in there - refresh will see
an overhaul soon.

Sort by master status once in _fix_load_order: EEE drop allow_deactivate_master?

Trying to make complex less complicated here - comments included. This
permitted inlining _index_of_first_esp - IIUC we just needed to calculate
once and then increment. So one function and 2 uses of in_master_block
down - neat.

More undead pruning: RRR

Including one more modInfos local import - typing is badly needed here

Mopy/bash/gui/popups.py: user_ok was essentially unused, was checked in
show_modal - while quietly doing RRR

---
## [meep109/Aurora.3](https://github.com/meep109/Aurora.3)@[652a3d02d4...](https://github.com/meep109/Aurora.3/commit/652a3d02d4260aea7f34c64814f409a677b063a0)
#### Wednesday 2023-12-20 19:49:26 by Wowzewow (Wezzy)

Adds Storage Container Animations (#17329)

* Much ado about the Bagginses

* god i hate manually mapped shit

* Update code/game/objects/items/weapons/storage/storage.dm

Co-authored-by: Fluffy <65877598+FluffyGhoster@users.noreply.github.com>

* fixes

* yes

* Update code/game/objects/items/weapons/storage/bags.dm

Co-authored-by: Cody Brittain <cbrittain10@yahoo.com>

---------

Co-authored-by: Fluffy <65877598+FluffyGhoster@users.noreply.github.com>
Co-authored-by: Cody Brittain <cbrittain10@yahoo.com>

---
## [Cthulhu80/cmss13](https://github.com/Cthulhu80/cmss13)@[dc234c9939...](https://github.com/Cthulhu80/cmss13/commit/dc234c9939efeb43170a934437f50148323407f7)
#### Wednesday 2023-12-20 20:11:23 by InsaneRed

Oppressor cooldown changes (#5154)

# About the pull request

Lowers the oppressor tail_abudct (the hook) to 15 seconds of cooldown
and makes the windup faster.

Makes punch shave off cooldown from the abduct for 5 seconds 

All have been tested but i would like this to get testmerged first so i
can actually see the results in game, nothing is set in stone and i want
to edit this further so the cd / cd reduction isnt too powerful, they're
just numbers ive decided were good enough to atleast make the caste
decent for the time being.


# Explain why it's good for the game

Oppressor has been a snoozer strain for a while now where you cast an
ability, and IF it hits you get to play the game otherwise you wait 20
seconds and thats just not fun. Especially for what the ability is, a 20
second cooldown is not worth it.

I've talked with a few people that all agree that the downtime for what
you "could" do with oppressor is not worth it. And i have to agree with
them, the caste feels boring to play and its basically half dead due to
the amnout of downtime you have between abilities compared to how
everything else works. The idea of this is to make it so its not busted
out of its brain but atleast not an observer++ strain so you can feel
more involved in the gameplay.




# Testing Photographs and Procedure
</details>


# Changelog



:cl:
balance: Oppressor tail abduct changed to 15 seconds and lowers the
windup to 7 deciseconds
balance: Changes around the punch effect so that instead of having to
meet demonic standards, you only need to punch to lower your tail/hook
on oppressor.
fix: You will now automatically punch chest if the target you are aiming
at is delimbed instead of doing nothing
/:cl:

---------

Co-authored-by: InsaneRed <prodexter31@outlook.comm>
Co-authored-by: Birdtalon <birdtalon@gmail.com>

---
## [emmanueltouzery/nvim_config](https://github.com/emmanueltouzery/nvim_config)@[d935553d76...](https://github.com/emmanueltouzery/nvim_config/commit/d935553d76fb46d6767ce95c7cfefed036da7028)
#### Wednesday 2023-12-20 20:30:44 by Emmanuel Touzery

finally got sick of shada - handle marks myself

i was using vim global marks to remember points of interest, but shada
was being a pain. updating in one neovim instance wouldn't have effect
on another neovim instance.. after a bunch of attempts, finally gave up
and rolled my own.

---
## [MERNDevTinkal/Music-Player](https://github.com/MERNDevTinkal/Music-Player)@[5d4767a1b5...](https://github.com/MERNDevTinkal/Music-Player/commit/5d4767a1b503a7fc95725854d76c06395d81ee60)
#### Wednesday 2023-12-20 20:49:58 by Tinkal Kumar

Create README.md

# Music Player

A simple web-based music player with features like theme toggling, song filtering, search functionality, and playlist management.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Usage](#usage)
- [Themes](#themes)
- [Song Queue](#song-queue)
- [Playlist Management](#playlist-management)

## Overview

This project is a web-based music player that allows users to play songs, filter them by genre, search for specific songs, and manage playlists. It provides a responsive and user-friendly interface, making it easy for music enthusiasts to enjoy their favorite tracks.

## Features

- **Theme Toggling:** Toggle between light and dark themes for a personalized visual experience.

- **Song Filtering:** Filter songs by genre to easily discover and play songs of a specific type.

- **Search Functionality:** Quickly find and play your favorite songs by searching through the song queue.

- **Playlist Management:** Create, view, and manage playlists to organize your music collection.

## Usage

1. **Theme Toggle:**
   - Use the toggle switch at the top to switch between light and dark themes.

2. **Filtering Songs:**
   - Select a genre from the dropdown to filter songs based on the chosen genre.

3. **Search Songs:**
   - Use the search bar to search for specific songs in the song queue.

4. **Playlist Management:**
   - Create playlists by entering a name in the playlist input field and clicking the "Create Playlist" button.
   - Add songs to the current playlist using the "Add to Playlist" button.

## Themes

The music player supports both light and dark themes to enhance your visual experience. Toggle between themes using the switch located at the top of the page.

## Song Queue

Browse through the song queue to discover and play your favorite songs. The search functionality helps you quickly find specific songs, and the filtering option allows you to explore songs by genre.

## Playlist Management

Organize your music collection by creating and managing playlists. Add songs to playlists and easily switch between playlists to enjoy different sets of songs.

Feel free to explore and enjoy the music player!

---

*This project is maintained by [Your Name]. Feel free to contribute or report issues.*

---
## [NutDoubleG/Martinius-Sindre](https://github.com/NutDoubleG/Martinius-Sindre)@[9197b65364...](https://github.com/NutDoubleG/Martinius-Sindre/commit/9197b65364859f0bc75f7a56945dc1bea020394d)
#### Wednesday 2023-12-20 21:19:16 by NutDoubleG

Create LORD GPT

Working shooter eith 1 respawning enemy. Enemy bullet colission. Svoring system. Game border. Fuck you

---
## [git/git](https://github.com/git/git)@[a1fbe26a0c...](https://github.com/git/git/commit/a1fbe26a0c2bb8ba84c3976023e4ded4cf94608e)
#### Wednesday 2023-12-20 21:34:15 by Elijah Newren

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
## [CarlosMecha/dwm](https://github.com/CarlosMecha/dwm)@[67d76bdc68...](https://github.com/CarlosMecha/dwm/commit/67d76bdc68102df976177de351f65329d8683064)
#### Wednesday 2023-12-20 22:28:33 by Chris Down

Do not allow focus to drift from fullscreen client via focusstack()

It generally doesn't make much sense to allow focusstack() to navigate
away from the selected fullscreen client, as you can't even see which
client you're selecting behind it.

I have had this up for a while on the wiki as a separate patch[0], but
it seems reasonable to avoid this behaviour in dwm mainline, since I'm
struggling to think of any reason to navigate away from a fullscreen
client other than a mistake.

0: https://dwm.suckless.org/patches/alwaysfullscreen/

---
## [crawl/crawl](https://github.com/crawl/crawl)@[afeb8edd3b...](https://github.com/crawl/crawl/commit/afeb8edd3b8c5a8165938164b7b2bc36ea37fb54)
#### Wednesday 2023-12-20 22:47:20 by DracoOmega

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
## [wetherc/dstk](https://github.com/wetherc/dstk)@[7fbd6b40c1...](https://github.com/wetherc/dstk/commit/7fbd6b40c129c5575eb60f2a6d2eb6ba1fedcb58)
#### Wednesday 2023-12-20 23:11:41 by Christopher Wetherill

Start work on a createModelVersion mutation (#55)

NOTE: This API is unstable and is liable to change in breaking
ways.

This begins the work for what we'll need to create and upload
new model versions. Specifically, here I'm just stubbing out
the endpoint to the point that it will create a new database
record for the model version.

As next steps, I will need to bring in the AWS S3 SDK and create
a new presigned URL that the client can use to upload the model
binary to blob storage. When that happens, this will likely get
broken apart into create-, upload-, and finalizeModelVersion
mutations (although really the upload one isn't going to be a
GQL mutation since that's just a client-side POST request for the
multipart upload).

Basically the flow is going to go:

  - User says, "I want to create a new model version"
  - Server says, "Love it, boss. Here's a URL you can use to upload
    all your cool shiz to"
  - User (or really, the UI/SDK/whatever the user is interacting
    with) posts the model binary to the MPU URL and does whatever
    checksum verification they want to make sure that the upload
    succeeded
  - User tells DSTK, "Yep, model version uploaded and is good to go!"
  - profit

I don't think we'll be able to simplify that flow meaningfully
since we (1) don't really want to be abusing Apollo for large binary
uploads, and (2) don't want to just be handing over to the user the
keys to whatever storage provider is configured for use with a given
model. Taking the presigned URL approach lets us keep secrets secure
within DSTK while also giving the end user a convenient way to upload
their blob, with the downside that it adds a couple steps that we need
to string together behind the scenes for folks.

It's also important to note that multipart uploads (which we will want
given the possibly large filesizes of trained models) do require a
`completeMultipartUpload` API call to S3 which sort of goes along
with why I added an `is_finalized` column to the model versions table.
Although separate things, we'd still like to probably offer an escape
hatch for folks if something gets borked partway through an upload and
they need to regen the presigned URL and try again.

---
## [wrye-bash/wrye-bash](https://github.com/wrye-bash/wrye-bash)@[a1de9aa3d1...](https://github.com/wrye-bash/wrye-bash/commit/a1de9aa3d1a1e9c93b61b566950d55689910bdf6)
#### Wednesday 2023-12-20 23:20:39 by MrD

312 Nightly:

Refix file duplicate for screens: RRR EEE try_rename for ModList

This was fixed again recently IIRC RRR - the problem (apart from regexes)
is we want to rename. This aligns the signatures of all except the
installers try_rename and fixes related pycharm warnings. Still WIP, due
to the weird screens rename logic - see old todos in there.

Move common logic to base:

 - we could eliminate all but IList overrides using unique_key?

Mopy/bash/bosh/__init__.py: The actual fix:

Traceback (most recent call last):
  File "C:\Dropbox (Personal)\eclipse_workspaces\python\wrye-bash\Mopy\bash\balt.py", line 1636, in __Execute
    menu.Append(menuItem)
    ^^^^^^^^^^^^^^
  File "C:\Dropbox (Personal)\eclipse_workspaces\python\wrye-bash\Mopy\bash\balt.py", line 515, in _conversation_wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Dropbox (Personal)\eclipse_workspaces\python\wrye-bash\Mopy\bash\basher\files_links.py", line 144, in Execute
    self.window.RefreshUI(redraw=dests, detail_item=dests[-1])
  File "C:\Dropbox (Personal)\eclipse_workspaces\python\wrye-bash\Mopy\bash\balt.py", line 786, in RefreshUI
    self.PopulateItem(item=upd)
  File "C:\Dropbox (Personal)\eclipse_workspaces\python\wrye-bash\Mopy\bash\balt.py", line 730, in PopulateItem
    self.labels[col](self, item))
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Dropbox (Personal)\eclipse_workspaces\python\wrye-bash\Mopy\bash\basher\__init__.py", line 3589, in <lambda>
    hitItem = self._getItemClicked(lb_dex_and_flags)
                                            ^^^^^^^^^
  File "C:\Dropbox (Personal)\eclipse_workspaces\python\wrye-bash\Mopy\bash\bolt.py", line 1632, in __getitem__
    return self._data[key]
           ~~~~~~~~~~^^^^^
  File "C:\Dropbox (Personal)\eclipse_workspaces\python\wrye-bash\Mopy\bash\bolt.py", line 679, in __getitem__
    return super().__getitem__(FName(k))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
KeyError: FName('rt4 Copy')
python-BaseException

Interlude - WIP unify set_item_format for masters/mods list:

Where all the usual load order methods / modInfos fields appear in a
cameo - as promised in 8338cb9bebf91737e5d4bc9f08a201a16914b0bb.
Mouse texts will be rearranged a bit - should be a dict[str, int]
for priority - done later in this commit.

_set_color

I commented on the couple checks we don't need for masters - it's worth the
copy/paste removal

item_format.back_key

has_master_size_mismatch

- added `'Deactivate' in fileBashTags` for masters also

more unification

MasterInfo.getDirtyMessage:

- added also getDirtyMessage check for masters

So finally set_item_format moved to base - more work needed to display
more messages (those elif are evil) and convert messages to prioritized
dict but this will do for now - the goal was to reduce occurrences of
load order operations and modInfos info set accesses

_ListItemFormat.back_key property:

This should result in printing all the applicable mouse texts but setting
the highest priority background

ListItemFormat.text_key prop

336 - renames in the Inis hierarchies

AIniFile was really AIniInfo - the 'file' part is added in IniFileInfo
renamed also. I moved ADefaultIniInfo just below AIniInfo for easier
comparison.

Nit in _mergeability:

Remove the repeating verbose noise to make easier to follow (I am trying
to understand what load order info is needed for mergeability checks) at
the expense of *one* loacalized strings lookup before _exit() on
first failure (and short circuits). Made also some micro
optimizations/nit, in particular I  re-made plugin_inis to a dict to
save the dict creation in _mergeability and inlined now shorter
_is_mergeable_no_load

Passed the modInfos in to make the dependency explicit - we could attach
the ini to the modInfo - better solution but more tricky to implement

TTT Maybe fix incorrect directory move?

This makes OMOD extraction work on Linux, but I don't know if getting
rid of the .head there is actually correct or if it'll just break
something else. And while we're at it, does this need a _retry too?

Work around icon size crash

Still no fix in sight for this - it seems to have worked for a while,
but now it's broken again. Work around this once and for all by
requesting a restart instead.

It was easier to fix than to explain all the subtle ways this would
go wrong (if user unhides a button that was hidden in previous session
and button is created with updated icon size) - fixes status bar being
redrawed with updated (wrong) icon size if user chooses to not restart
after changing icon size. The assumption that icon sizes could be hot
switched was hardwired in the code so I had to hardwire the opposite.
Note BashStatusBar was in scope at least. This was a showstopper as
(not) discussed - thanks :)

Btw the crash was on mac too and probably OS agnostic

TTT does not seem removing this call entirely to cause problems on Windows?

Mopy/bash/basher/app_buttons.py: Guess this is the intended behavior?

Cleanup status bar text apis: TTT

We had:

- BashFrame.set_status_count used once in
- SashUIListPanel.SetStatusCount used twice - is the if needed in
ShowPanel too? TTT
- BashStatusBar.set_sb_text the real one (wraps _native), but why did it
call self.refresh_status_bar()? -> turns out we needed this on show_panel
- BashFrame.set_status_info, the API

This cures the flickering of the status bar buttons while not ellipsizing
the third sb field (item counts). The flickering was due to SetStatusWidths
that was only needed when the panel was shown. Not sure if we ever bypass
the ShowPanel call TTT - onSize was not needed here.

FFF statusBar.set_sb_text -> set_status_info

Stop binding the size event on the StatusBar: TTT

Turns out we don't need to reposition the buttons on a size event - wx is
doing this for us. Was this maybe the root cause of the crash on resizing
the buttons?

SSE: Add support for version 1.6.1130

This means refactoring the expanded ESL range support to allow other
versions besides 1.0 to trigger it (I was debating doing that
refactoring for a while now, glad this forced my hand I guess) and
adding 1.71 as a new supported HEDR version for SSE.

Hide TES4View/TES4Trans launchers when EXE missing

I don't have a TES4View.exe/TES4Trans.exe in my game folder, yet the
launchers were still shown since they bypass app_button_factory (and so
also bypass find_launcher). Could have tried making this work with
app_button_factory instead, but the comment seems to indicate that's not
an option?

Ut: this finally calls init for all app buttons via app_button_factory.
Now that the logic is spelled out clearly - does TES4Edit launched with
-translate/-view arguments start TES4Trans/TES4View? The API is not
expressive enough for this (joins with app_launcher) but can be extended -
or better wait till we obsolete app_key so the code becomes simpler
(we should use the uid for the images, should be unique :p, and rename
those again, duh - then simplify find_launcher by constructing the
paths in constants). Did not add keys to the ini as this is on its way
out. Also - do all the menu items apply to TES4View/Trans?Lod? TTT

If you find this method long you need to have a look at its first
iteration:

https://github.com/wrye-bash/wrye-bash/blob/2f0ace775218125e3c977b1b35258cb8810f1bcd/Mopy/bash/basher/links.py#L43-L584

:P

Co-authored-by: MrD <the.ubik@gmail.com>

Properly support high DPI images RRR

Turns out the high DPI image support introduced in # 557 <--- RRR had
some significant issues - most notably, it was rendering crisp high-res
images, but wx then decided to upscale them *again* if your DPI scaling
was set to 200%.

To fix this, we need to move to wx.BitmapBundle. This is intended to be
used by bundling multiple versions of the asset and sticking them all
into a bundle, then having wx choose the most appropriate resolution. Or
use an SVG, statically render a bunch of sizes and stick them all in a
bundle. We don't do that and instead dynamically create them, sticking
only a base resolution asset and the actual version we need in. That way
wx will use the higher-resolution version without applying its own
scaling. This does of course look ugly with checkboxes and such, but
those are temporary anyway - # 511 <--- RRR will replace them with SVGs.

Note that we now pass in iconSize for (nearly?) everything, so maybe we
should just make it a required parameter.

Under # 511, # 557 <--- RRR

SSS Fix _load_err before self.inName is set

I *think* moving the __init__ call before the _load_err should be fine?
Worst case we'll waste some time reading the children before raising the
error, AFAICT.

SSS TES3: Fix regression causing crash on boot

Introduced in 3f6738597bbb5ac413609410f472cba62a25c57e.

SF: Add new vanilla directory to data_dirs

Directories with example BA2s below.
distantlod: Starfield - LODMeshes.ba2
geometries: Starfield - FaceMeshes.ba2
particles:  Starfield - Particles.ba2
planetdata: Starfield - PlanetData.ba2
space:      Starfield - Misc.ba2
terrain:    Starfield - Terrain01.ba2

SSS Bump dependencies

All just fixes.

Officially mark Linux as supported RRR

Only QOL stuff and launchers left, and launchers are WIP anyways.

Renamed --unix to --unsupported, since we may have non-Unix platforms to
consider as well.

Closes # 243 <--- RRR

---
## [SSensum/tgstation](https://github.com/SSensum/tgstation)@[39d9c45b4a...](https://github.com/SSensum/tgstation/commit/39d9c45b4a7afc2a963de4249592a3d4ae6c4715)
#### Wednesday 2023-12-20 23:25:27 by san7890

Meat Hook Rework (Accidental Features) (#80002)

## About The Pull Request

Or, how I tried to kill `/datum/forced_movement` but got absolutely
clonged.

Actually, I did kill `/datum/forced_movement`. It was only used in one
spot so I just went ahead and cooked it into a special utility datum
that should only be used in one spot. We can optimize the code later or
something, but I like the way it is right now (pretty much status quo
without the potential of someone using a depreciated framework).

Alright, there were also like 3 `TODO`s (4 if you count the move loop
comment (which is ehhhh)). I naively tried to tackle them a very hard
way, but then I just realized I could use the fancy new datum I cooked
up and wow they're all solved now. The hook looks so fucking good now.

* The code is overall more streamlined, with all of the post-projectile
work being handled by a special datum (I wanted it to be handled by the
hook but the timings were all based on SSFastprocess so datum it is).
Forced movement is killed but we just salvaged whatever we needed from
it.
* More traits to ensure we don't cheese in a way we're not supposed to
* A very sexy chain will spawn when you drag your kill in (this wasn't
there before but I fixeded it :3)
* The firer will actually get grounded when they try and shoot the chain
out. They get grounded for 0.25 seconds unless they hit something. I
don't know how the timing is but I think it's fair.
* We also add a unique suicide act, because I noticed we did the
"magical" one previously, which big-league sucked.
* More traits to ensure less cheese! I like how nice it is now.
## Why It's Good For The Game

The meat hook really makes you _feel_ like Roadhog from Overwatch.
Resolves a bunch of old TODOs while getting rid of a completely obsolete
framework in a really neat way. I don't typically like mixing balances
and refactors but these TODOs were getting crusty man i just wanted to
get them out of the way
## Changelog
:cl:
balance: The Meat Hook will now "ground" you whenever you fire it out at
someone. You get a very small immobilization every time you fire, which
"upgrades" to a full immobilization whenever you actually hit an atom
and start to drag it in.
fix: A chain should now show up as you drag in something with the meat
hooks.
fix: Meat hooks should no longer play the "magical gun" suicide if you
were to use it, but instead do their own unique thing.
/:cl:

---
## [SSensum/tgstation](https://github.com/SSensum/tgstation)@[08ab5d2731...](https://github.com/SSensum/tgstation/commit/08ab5d27312d236593eabdb27fb23dccbf8283e6)
#### Wednesday 2023-12-20 23:25:27 by Mothblocks

Blood brothers is now a single person conversion antagonist (#79971)

## About The Pull Request
Instead of choosing 2-3 brothers, *one* person will be selected and
given a flash which can convert one other person over. In accordance to
the existing 10% chance for 3 members, there is a 10% chance that the
first person converted will receive a flash of their own.

Expectation is people will flash a friend or a robust guy or whatever.
My intent is primarily to see if this kind of blood brothers is more
enjoyable to play with/against, and if their inclusion in a round
increases the general chaos of it. My theory is that since most likely
blood brothers will be people who know each other, that it can become
more consistently interesting to the rest of the crew. That or they just
murderbone together idk

Fikou and head admins said they wanted this to replace rather than add
which I agree with.

## Why It's Good For The Game
Keeps the sandboxy aspect of blood brothers (no uplink) while likely
making it more enjoyable to play. Conversion is equally as simple as
revs for the user, and is just as intuitive to the one being converted
since there are no new mechanics thrown in your face.

Blood brothers is currently disabled everywhere on the main servers
except for MRP. I think this form will be more appealing to all
rulesets. If left enabled, Dynamic now has more antagonists to make
rounds diverse with and I want that

## Changelog

:cl:
add: Instead of teaming up random people together, blood brothers will
now start out with one player and let them convert a single other person
over to blood brother using a flash.
/:cl:

---

