## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-05-30](docs/good-messages/2022/2022-05-30.md)


1,861,058 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,861,058 were push events containing 2,838,890 commit messages that amount to 191,826,640 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 40 messages:


## [Jolly-66/tgstation](https://github.com/Jolly-66/tgstation)@[e37591540b...](https://github.com/Jolly-66/tgstation/commit/e37591540b2620b7ad2a2b61734634d848e8eba2)
#### Monday 2022-05-30 01:14:10 by san7890

[MDB Ignore] OH GOD OH FUCK OH SHIT OH LORD - SPACE AND RUINS IS BROKEN (#67324)

So, for the last few days on production, Space Ruin generation has refused to work. Why is this? It's because in #67107 (cfc233052885dd294b2e7e676caaf84a2a37592b), we repathed `/area/space`  to `/area/misc/space` (lol i should have paid attention to that) without updating everything in code to match. I couldn't seem to get `/area/misc/space` to properly work somehow (this could have also been something I was doing wrong), but I worked it back to just making everything vanilla `/area/space` and all of those unwanted behaviors should be squashed out. Let's get the game working again.

---
## [CluckeyMcCormick/fictional-guacamole](https://github.com/CluckeyMcCormick/fictional-guacamole)@[2c7b1f6ca5...](https://github.com/CluckeyMcCormick/fictional-guacamole/commit/2c7b1f6ca5f5132b88dee8e913882691782aa8f0)
#### Monday 2022-05-30 02:03:34 by frick-nedrickson

Separate particle visuals from behavior as best we can

One of my biggest issues with the RichParticleEmitter was how closely
we had coupled together the visuals of the particles - the sprite, the
draw passes - with the behavior of the particles - i.e. everything and
everything in the particle materials.

Now this was done on-purpose, accidentally. I'm not really sure how to
term it. See, to scale the particle systems up-and-down, we needed a
consistent set of information. I, thinking a little uncritically, just
rolled this all up into the RichParticleMaterial.

However, this started to create problems for us. Things were fine
initially, but we ran into trouble when we created all of our hit
particles. We had a consistent behavior that I really would've liked
duplicated for all the hit particles, but I couldn't! It all had to be
tied up in the RichParticleMaterial.

So, I've redone everything - it's similar, yet different. We now have
separate spatial and particle materials. The particle materials are
normal, while the spatial materials have been augmented into
ParticleReadySpatialMaterial (bit of a wordy name but I couldn't
immediately think of anything better). These two are then bound
together in the ScalableParticleBlueprint, which includes particle
system-specific configurables which I couldn't quite place on either
the particle or spatial materials. This blueprint then takes the place
of the RichParticleMaterial. The RichParticleEmitter has thusly been
reworked into the ScalableParticleEmitter, with minimal notable
changes.

Now then, as much as I love my scalable particles, I also want to
support prebuilt particle systems. I also need to redo the status
effect / particle interface, and then I need to sit down and redo
attacks with some sorta... fancy... scanning... something.

---
## [hyunjun/bookmarks](https://github.com/hyunjun/bookmarks)@[e5372ebfcb...](https://github.com/hyunjun/bookmarks/commit/e5372ebfcb95a18b2642d123c59ade17edc95910)
#### Monday 2022-05-30 02:24:21 by Hyunjun Chung

Why I Quit Google’s WebAssembly Team, And How It Made Me Sick, How To Be Successful - Sam Altman, company structure, Building & scaling team, Onboard, Reinventing Performance Management, Product-Market fit, Startup Survival, 최악을 대비하세요, 콰이강의 다리 문제

Why I Quit Google’s WebAssembly Team, And How It Made Me Sick | by Katelyn Gadd | May, 2022 | Medium https://medium.com/@katelyngadd/why-i-quit-googles-webassembly-team-and-how-it-made-me-sick-c50ef562ce1
내가 구글 WebAssembly 팀에서 그만둔 이유와 나를 아프게 한 것 | GeekNews https://news.hada.io/topic?id=6573

How To Be Successful - Sam Altman https://blog.samaltman.com/how-to-be-successful

How should our company structure our data team? | by David Murray | Snapcommerce | Medium https://medium.com/snaptravel/how-should-our-company-structure-our-data-team-e71f6846024d

Building & scaling Engineering team | by Amit Kumar | Medium https://toamitkumar.medium.com/building-scaling-engineering-team-21bd7471a35a

Onboard New Developers with Better Coding Practices | HackerNoon https://hackernoon.com/onboard-new-developers-with-better-coding-practices

Reinventing Performance Management https://hbr.org/2015/04/reinventing-performance-management

Shreyas Doshi on Twitter: "Product-Market fit is often viewed as a static concept: either you have it or you don’t. In my experience, it is better to think of fit as a dynamic state based on your progress towards your vision & know what fit you currently have. Check out the 4 Types of Product-Market fit: https://t.co/TARAJGmJvd" / Twitter https://twitter.com/shreyas/status/1426594663671107585
Product-Market Fit 의 4가지 종류 | GeekNews https://news.hada.io/topic?id=6564

Startup Trail: The Game Of Startup Survival https://startuptrail.engine.is

최악을 대비하세요 – YC (번역) – 이바닥늬우스 https://ebadak.news/2022/05/21/plan-for-the-worst

칼럼 | ‘콰이강의 다리 문제’··· 테크놀로지스트의 전형적인 실수 - CIO Korea https://www.ciokorea.com/news/236719 고객이 진짜로 이용할 무언가를 만들기

---
## [skyrossm/fivem](https://github.com/skyrossm/fivem)@[02df4a52b1...](https://github.com/skyrossm/fivem/commit/02df4a52b1dba9b56a89b10bf59be7c9ff79c0d9)
#### Monday 2022-05-30 03:06:57 by blattersturm

tweak(client/core): nvidia, fuck you.

Apparently ba693365d151cb3d61e1fd1bc08f9f65f66d13ae wasn't enough to fix
the .toc corruption from nvPSShaderDiskCache.cpp/the NvShaderDiskCache
perf strategy.

Instead, this change just disables the shader cache entirely. Using a
hacky way.

---
## [skyrossm/fivem](https://github.com/skyrossm/fivem)@[6051b8790c...](https://github.com/skyrossm/fivem/commit/6051b8790c185b2435da75c2f41f59ec3be4578f)
#### Monday 2022-05-30 03:06:57 by blattersturm

Revert "tweak(client/core): nvidia, fuck you."

The gift that keeps on giving: NVIDIA drivers. Some users seem to crash
in new places with `disable.txt` present and used.

Seriously?!

This reverts commit 02df4a52b1dba9b56a89b10bf59be7c9ff79c0d9.

---
## [Wizard89/git](https://github.com/Wizard89/git)@[bdaf1dfae7...](https://github.com/Wizard89/git/commit/bdaf1dfae71fdf120fc7253e713ccf0a06cc5558)
#### Monday 2022-05-30 03:11:51 by Tao Klerks

branch: new autosetupmerge option 'simple' for matching branches

With the default push.default option, "simple", beginners are
protected from accidentally pushing to the "wrong" branch in
centralized workflows: if the remote tracking branch they would push
to does not have the same name as the local branch, and they try to do
a "default push", they get an error and explanation with options.

There is a particular centralized workflow where this often happens:
a user branches to a new local topic branch from an existing
remote branch, eg with "checkout -b feature1 origin/master". With
the default branch.autosetupmerge configuration (value "true"), git
will automatically add origin/master as the upstream tracking branch.

When the user pushes with a default "git push", with the intention of
pushing their (new) topic branch to the remote, they get an error, and
(amongst other things) a suggestion to run "git push origin HEAD".

If they follow this suggestion the push succeeds, but on subsequent
default pushes they continue to get an error - so eventually they
figure out to add "-u" to change the tracking branch, or they spelunk
the push.default config doc as proposed and set it to "current", or
some GUI tooling does one or the other of these things for them.

When one of their coworkers later works on the same topic branch,
they don't get any of that "weirdness". They just "git checkout
feature1" and everything works exactly as they expect, with the shared
remote branch set up as remote tracking branch, and push and pull
working out of the box.

The "stable state" for this way of working is that local branches have
the same-name remote tracking branch (origin/feature1 in this
example), and multiple people can work on that remote feature branch
at the same time, trusting "git pull" to merge or rebase as required
for them to be able to push their interim changes to that same feature
branch on that same remote.

(merging from the upstream "master" branch, and merging back to it,
are separate more involved processes in this flow).

There is a problem in this flow/way of working, however, which is that
the first user, when they first branched from origin/master, ended up
with the "wrong" remote tracking branch (different from the stable
state). For a while, before they pushed (and maybe longer, if they
don't use -u/--set-upstream), their "git pull" wasn't getting other
users' changes to the feature branch - it was getting any changes from
the remote "master" branch instead (a completely different class of
changes!)

An experienced git user might say "well yeah, that's what it means to
have the remote tracking branch set to origin/master!" - but the
original user above didn't *ask* to have the remote master branch
added as remote tracking branch - that just happened automatically
when they branched their feature branch. They didn't necessarily even
notice or understand the meaning of the "set up to track 'origin/master'"
message when they created the branch - especially if they are using a
GUI.

Looking at how to fix this, you might think "OK, so disable auto setup
of remote tracking - set branch.autosetupmerge to false" - but that
will inconvenience the *second* user in this story - the one who just
wanted to start working on the topic branch. The first and second
users swap roles at different points in time of course - they should
both have a sane configuration that does the right thing in both
situations.

Make this "branches have the same name locally as on the remote"
workflow less painful / more obvious by introducing a new
branch.autosetupmerge option called "simple", to match the same-name
"push.default" option that makes similar assumptions.

This new option automatically sets up tracking in a *subset* of the
current default situations: when the original ref is a remote tracking
branch *and* has the same branch name on the remote (as the new local
branch name).

Update the error displayed when the 'push.default=simple' configuration
rejects a mismatching-upstream-name default push, to offer this new
branch.autosetupmerge option that will prevent this class of error.

With this new configuration, in the example situation above, the first
user does *not* get origin/master set up as the tracking branch for
the new local branch. If they "git pull" in their new local-only
branch, they get an error explaining there is no upstream branch -
which makes sense and is helpful. If they "git push", they get an
error explaining how to push *and* suggesting they specify
--set-upstream - which is exactly the right thing to do for them.

This new option is likely not appropriate for users intentionally
implementing a "triangular workflow" with a shared upstream tracking
branch, that they "git pull" in and a "private" feature branch that
they push/force-push to just for remote safe-keeping until they are
ready to push up to the shared branch explicitly/separately. Such
users are likely to prefer keeping the current default
merge.autosetupmerge=true behavior, and change their push.default to
"current".

Also extend the existing branch tests with three new cases testing
this option - the obvious matching-name and non-matching-name cases,
and also a non-matching-ref-type case. The matching-name case needs to
temporarily create an independent repo to fetch from, as the general
strategy of using the local repo as the remote in these tests
precludes locally branching with the same name as in the "remote".

Signed-off-by: Tao Klerks <tao@klerks.biz>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [WillNilges/letmein2](https://github.com/WillNilges/letmein2)@[e2c40a1304...](https://github.com/WillNilges/letmein2/commit/e2c40a13042851402935e0ad36a2ab490c386d05)
#### Monday 2022-05-30 03:58:40 by Will Nilges

Oh god I totally fucked up the CAD file

I really ought to re-do it in a less stupid way.

---
## [WillNilges/letmein2](https://github.com/WillNilges/letmein2)@[e90b5b1ae1...](https://github.com/WillNilges/letmein2/commit/e90b5b1ae1ff19bb49babf43c12777f88f726f60)
#### Monday 2022-05-30 03:58:40 by Will Nilges

Beeg refactor

Move a lot of shit out of the global scope, into the main function, and
also break out a lot of shit into a class. I tried to move the MQTT
stuff but it got mad when I did that. I'd like to see if that can move,
but not sure if it's a big deal.

I'm sure I violated a ton of Python design patterns because I'm stupid.
Enjoy.

---
## [ammarfaizi2/linux-block](https://github.com/ammarfaizi2/linux-block)@[af0fc4b763...](https://github.com/ammarfaizi2/linux-block/commit/af0fc4b7635e123f1e9b9b95ee9837f67043e03f)
#### Monday 2022-05-30 05:01:34 by Jason A. Donenfeld

random: use linear min-entropy accumulation crediting

commit c570449094844527577c5c914140222cb1893e3f upstream.

30e37ec516ae ("random: account for entropy loss due to overwrites")
assumed that adding new entropy to the LFSR pool probabilistically
cancelled out old entropy there, so entropy was credited asymptotically,
approximating Shannon entropy of independent sources (rather than a
stronger min-entropy notion) using 1/8th fractional bits and replacing
a constant 2-2/√𝑒 term (~0.786938) with 3/4 (0.75) to slightly
underestimate it. This wasn't superb, but it was perhaps better than
nothing, so that's what was done. Which entropy specifically was being
cancelled out and how much precisely each time is hard to tell, though
as I showed with the attack code in my previous commit, a motivated
adversary with sufficient information can actually cancel out
everything.

Since we're no longer using an LFSR for entropy accumulation, this
probabilistic cancellation is no longer relevant. Rather, we're now
using a computational hash function as the accumulator and we've
switched to working in the random oracle model, from which we can now
revisit the question of min-entropy accumulation, which is done in
detail in <https://eprint.iacr.org/2019/198>.

Consider a long input bit string that is built by concatenating various
smaller independent input bit strings. Each one of these inputs has a
designated min-entropy, which is what we're passing to
credit_entropy_bits(h). When we pass the concatenation of these to a
random oracle, it means that an adversary trying to receive back the
same reply as us would need to become certain about each part of the
concatenated bit string we passed in, which means becoming certain about
all of those h values. That means we can estimate the accumulation by
simply adding up the h values in calls to credit_entropy_bits(h);
there's no probabilistic cancellation at play like there was said to be
for the LFSR. Incidentally, this is also what other entropy accumulators
based on computational hash functions do as well.

So this commit replaces credit_entropy_bits(h) with essentially `total =
min(POOL_BITS, total + h)`, done with a cmpxchg loop as before.

What if we're wrong and the above is nonsense? It's not, but let's
assume we don't want the actual _behavior_ of the code to change much.
Currently that behavior is not extracting from the input pool until it
has 128 bits of entropy in it. With the old algorithm, we'd hit that
magic 128 number after roughly 256 calls to credit_entropy_bits(1). So,
we can retain more or less the old behavior by waiting to extract from
the input pool until it hits 256 bits of entropy using the new code. For
people concerned about this change, it means that there's not that much
practical behavioral change. And for folks actually trying to model
the behavior rigorously, it means that we have an even higher margin
against attacks.

Cc: Theodore Ts'o <tytso@mit.edu>
Cc: Dominik Brodowski <linux@dominikbrodowski.net>
Cc: Greg Kroah-Hartman <gregkh@linuxfoundation.org>
Reviewed-by: Eric Biggers <ebiggers@google.com>
Reviewed-by: Jean-Philippe Aumasson <jeanphilippe.aumasson@gmail.com>
Signed-off-by: Jason A. Donenfeld <Jason@zx2c4.com>
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

---
## [anachronic/dotfiles](https://github.com/anachronic/dotfiles)@[2a002a9207...](https://github.com/anachronic/dotfiles/commit/2a002a92074bf833cc395f70f578c020eb8ee90a)
#### Monday 2022-05-30 06:19:50 by Nicolás Salas

alacritty: start config

featuring:
- tokyo night theme
- jetbrains mono nerd font
- rebinding C-i to F6 (needed for neovim)

also config is WAY simpler than kitty's

a short note about the change:
- my kitty config is way too bloated
- alacritty supports undercurl
- I'd rather write rust than python

the last one is kinda bullshitty, I know, but it's there.

---
## [jinzaizhichi/opencart](https://github.com/jinzaizhichi/opencart)@[89c304ae61...](https://github.com/jinzaizhichi/opencart/commit/89c304ae61fb683b2ca8ff7dcf5ceabfc4f5a0eb)
#### Monday 2022-05-30 06:54:37 by Anton

OC4 return created module_id

IMHO every single model function, creating a row in DB, must return this row id after executed.

I can check `$module_id = $this->db->getLastId();` in my code on clean opencart installation.
But what if this model function calls any `after` events which also insert rows into DB?

This is not a developer friendly software architecture when you need to create hacks, hooks, workarounds and other voodoo magic to get a single value for page redirect.

BUG:
By the way on creating, for example a banner module, on save you are not redirected to created module page. 
So every click on Save button just creates a duplicate of a module.

---
## [DolanP/godot-docs](https://github.com/DolanP/godot-docs)@[b872229427...](https://github.com/DolanP/godot-docs/commit/b872229427dddb9b749f46af597e85e25cf2955a)
#### Monday 2022-05-30 06:55:25 by Rémi Verschelde

Remove controversial satirical piece 🔥

This piece was written back in 2014 before open sourcing Godot, and while its
intent is to be sarcastic, it leaves ample room for misinterpretation.

The intended meaning of this piece was, and always has been, the following:

Exploitative game mechanics suck. Games are a beautiful and artful medium
which can provide players with a wide range of experiences: entertainment,
enlightenment, joy, sadness... Games can be just for fun or they can bear
a message. They can connect people with each other or open the player's mind.

Make games worth your players' time and their money, and do your best to do so
while running a successful and respectful business. Hugs <3

---
## [kovalenkobogdana/how-i-can-do-it](https://github.com/kovalenkobogdana/how-i-can-do-it)@[f3d6369f91...](https://github.com/kovalenkobogdana/how-i-can-do-it/commit/f3d6369f9191cf235ef8dc89bb30c8e87a9a5e3d)
#### Monday 2022-05-30 07:15:17 by Богдана Коваленко

Create #7 I love you, a little , a lot, passionately ... not at all

Who remembers back to their time in the schoolyard, when girls would take a flower and tear its petals, saying each of the following phrases each time a petal was torn:

I love you
a little
a lot
passionately
madly
not at all
When the last petal was torn there were cries of excitement, dreams, surging thoughts and emotions.

Your goal in this kata is to determine which phrase the girls would say for a flower of a given number of petals, where nb_petals > 0.

---
## [GEM-404/shell-files](https://github.com/GEM-404/shell-files)@[ff050026ca...](https://github.com/GEM-404/shell-files/commit/ff050026caecd15019418a7d621b8925ab1327b9)
#### Monday 2022-05-30 08:26:32 by GEM-404

Changed from variable $wrong to raw text "fuck you"

---
## [fluxer/pkgsrc](https://github.com/fluxer/pkgsrc)@[0f2755b42a...](https://github.com/fluxer/pkgsrc/commit/0f2755b42a47006d5292f1391bf224c8c8b2532f)
#### Monday 2022-05-30 08:45:41 by wiz

mame: update to 0.244.

Given how many exciting updates have gone into MAME 0.244, it’s
hard to believe it’s only been a month since the last release! Only
one disk has been added to the Apple II software lists, but it
comes with a very engaging story involving physically damaged media
and manual data repairs. The Zilog Z80 CPU has had a bit of an
overhaul this month, allowing more accurate memory access timings
for the ZX Spectrum family. This fixes a lot of broken visual
effects and other glitches. The HP 9000/300 series computers have
had the necessary floppy disk image formats hooked up, allowing
them to mount floppy disks from their software list.

MAME’s driver for JPM’s first CPU-based fruit machine platform,
dating all the way back to the late 1970s, has been almost completely
rewritten this month. Four games are now playable, albeit with
minimal internal artwork. Colour video output has been implemented
for Zilec’s Vortex. Don’t get too excited, though – while the
approach they used to produce colourful graphics without adding
any video memory is technically interesting, the results are very
ugly and don’t make a bad game any better.

Other improvements in arcade emulation include:

    Score display and diorama control outputs have been hooked up
    for Bubble Trouble (this means you’ll need updated artwork for
    Golly! Ghost! as well).  Layer offsets in Slap Fight and Alcon
    should be fixed, and cocktail mode now works for the original
    sets.  The communication board for Super Street Fighter II:
    The Tournament Battle is now supported, allowing it to actually
    run in eight-player tournament mode.

SDL builds (the default for Linux and macOS) now detect game
controller reconnection. Note that due to limitations of SDL itself,
MAME may confuse similar controllers, potentially causing issues
if multiple controllers are disconnected at the same time. Issues
using MIDI input or output with 64-bit Windows builds should be
fixed.

---
## [b2nil/OpenNMT-py](https://github.com/b2nil/OpenNMT-py)@[63142c28ab...](https://github.com/b2nil/OpenNMT-py/commit/63142c28ab790acdbf8e34802c1b09faaf21a6ca)
#### Monday 2022-05-30 09:07:43 by Gideon Wenniger

Added missing check for using GPU in train.py in the
build_optim(model, checkpoint) method. This check is nescessary
for the code to run without errors when not using a GPU.

As another side note with this commit: It would actually be nicer
to build the torch optimizer in one go, providing the parameters
and old state all at once to the constructor. Unfortunately,
the torch optimizer.py code simply does not allow that, since
the constructor takes only a list of parameters and does not
provide an option to set the state. Hence, we are forced to use
the "optimizer.load_state_dict(self, state_dict)" method, which is
in my opinion really ugly.
Generally, I think  use of such (non-optional) setters is often
considered an anti-pattern, with setting the state directly in
the constructor being the preferred way to go.
It feels a bit like making an incomplete car, and then calling a
setter to provide the motor. Not so neat.

Also the exact effect of "optimizer.load_state_dict" is quite hard
to grasp,one has to study the code a lot to understand what goes
on exactly,  but essentially comes down to this:
1. It makes a deep copy of the state variables provided in the
dictionary that contains "state" and "param_groups" items.
It uses this copied optimizer state (not model parameters!)
to set the optimizer state with.
2. It effectively retains the "params" entry within "param_groups"
since this contains the model parameters that need to be optimized,
which should not be copied (otherwise optimization has no effect
on the actual model) but can only be provided through the constructor.
3. It updates the rest of the parameters (such as learning rate, etc)
using the provided "state_dict" argument.
As one can see, this is not very intuitive at all, and could be
done a lot cleaner, but alas one has to work with this function as it is.

	modified:   train.py

---
## [petre-symfony/upgrading-and-what-s-new-in-Synfony-6](https://github.com/petre-symfony/upgrading-and-what-s-new-in-Synfony-6)@[9b9d66f8cf...](https://github.com/petre-symfony/upgrading-and-what-s-new-in-Synfony-6/commit/9b9d66f8cf36840530ef4ae3645abe61e21644d7)
#### Monday 2022-05-30 09:21:47 by petrero

5.1. Updating the All-Important FrameworkBundle Recipe - composer recipes:update

  At your terminal, run:

    composer recipes
  As you probably know, whenever we install a new package, that package may come with a recipe that does things like add configuration files, modify certain files like .env, or add other files. Over time, Symfony makes updates to these recipes. Sometimes these are minor... like the addition of a comment in a config file. But other times, they're bigger, like renaming config keys to match changes in Symfony itself. And while you don't have to update your recipes, it's a great way to keep your app feeling like a standard Symfony app. It's also a free way to update deprecated code!

  Hello recipes:update
  - Until recently, updating recipes was a pain. If you're not familiar, just check our "Upgrade to Symfony 5" tutorial! Yikes. But no more! Starting with Symfony Flex 1.18 or 2.1, Composer has a proper recipes:update command. It literally patches your files to the latest version... and it's awesome. Let's try it!

  Run:

    composer recipes:update
  Oh! Before we run this, it tells us to commit everything that we've been working on. Great idea! I'll say that we are:

    upgrading some code to Symfony 5.4 with Rector

    git add .
    git commit -m "upgrading some code to Symfony 5.4 with Rector"
  Perfect! Try the recipes:update command again. The reason it wants our working copy to be clean is because it's about to patch some files... which might involve conflicts.

  Let's start with symfony/framework-bundle, because this is the big one. The most important files in our project come from this recipe. I'll hit 4, clear the screen, and go!

  Behind the scenes, this checks to see what the recipe looked like when we originally installed it, compares it to what the recipe looks like now, and generates a diff that it then applies to our project. In some cases, like this one, that can cause some conflicts, which is pretty cool. The best part might be that it generates a changelog containing all the pull requests that contributed to these updates. If you need to figure out why something changed, this will be your friend.

  Oh, but creating the changelog requires making a bunch of API calls to GitHub. So it's possible that composer will ask you for a personal access token, like it just did for me. In some rare cases with a giant recipe like framework-bundle, if your recipe is really, really old, you might get this message even if you have given an access token to Composer. If that happens, just wait for 1 minute... then re-enter your access token. Congratulations, you just hit GitHub's per-minute API limit.

  Anyways, there's the CHANGELOG. It's not usually that long, but this recipe is the most important and... well... it was horribly out-of-date. Oh, and if you have a trendy terminal like me - this is iTerm - you can click these links to jump directly into the pull request, which will live at https://github.com/symfony/recipes.

---
## [petre-symfony/upgrading-and-what-s-new-in-Synfony-6](https://github.com/petre-symfony/upgrading-and-what-s-new-in-Synfony-6)@[41511cbdb4...](https://github.com/petre-symfony/upgrading-and-what-s-new-in-Synfony-6/commit/41511cbdb47893891c8a8e2eef69f5c59758c129)
#### Monday 2022-05-30 09:59:19 by petrero

6.4. Recipe Upgrades with recipes:update

  doctrine/doctrine-bundle Recipe Update
  Let's keep going!

    composer recipes:update
  We'll work on the rest from top to bottom. Next is doctrine/doctrine-bundle. This is a cool update. Once again, I'll clear the screen and run:

    git status

  It conflicted inside the .env file... which is probably the least interesting change. Recently, DoctrineBundle's recipe started shipping with PostgreSQL as the default database. You can totally change that to be whatever you want, but PostgreSQL is such a good database engine that we started shipping with it as the default suggestion.

  But I'm using MySQL in this project, so I'm going to keep that. But to be super cool, I'll at least take their new example config... which looks a little different... and update my comments on top with it. Then I'll use my version of the conflict. The end-result is a few tweaks to the comments, but nothing else.

  The other changes from the recipe relate to the config files, and I bet you can see what's happening. It deleted two environment-specific config files and updated the main one. Hmm.

  Open config/packages/doctrine.yaml. Sure enough, at the bottom, we see when@test and when@prod. That's nice! Everything is now in one file. Just make sure that if you had any custom config in the old deleted, files, that you move it over to this file.

  One other change that's new is this dbname_suffix under when@test. This is cool. When you're running tests, this will automatically reuse the same database connection configuration, but with a different database name: your normal name followed by _test. And this fancy part on the end makes it really easy to run parallel tests with Paratest. This will ensure that each parallel process will use a different database name. You get that all, for free, thanks to the updated recipe.

  There's one other change in this file, and it's important. In PHPStorm, I can see that the recipe update deleted the type: annotation line. Right now, we are still using annotations in our project for entity configuration. We're going to change that in a few minutes to use PHP 8 attributes, which is going to be amazing. But anyways, in the DoctrineBundle configuration, you no longer need this type: annotation line. If you don't have it, the correct format will be detected automatically. If Doctrine sees annotations, it'll load annotations! If it sees PHP 8 attributes, it will load those. So the best config is no config... which tells Doctrine to figure out things for us.

  Once again, add all these changes, commit, and... let's keep going! Well, let's keep going in the next chapter, where we upgrade DoctrineExtensionsBundle, some debug recipes, routing, security and more!

---
## [vg-mjg/mjg-repo](https://github.com/vg-mjg/mjg-repo)@[b831573499...](https://github.com/vg-mjg/mjg-repo/commit/b831573499aecbaffbb93bc0d88dfd335aaafd1a)
#### Monday 2022-05-30 10:39:00 by Sharmayu Mirica

lotw final fix

fuck off repoanons you didn't fix your loli of the week and every fucking time i had to use the site shit's broken all over because retarded kodomo can't stop being so big, fuck off kokomo you're supposed to be small, dum fuck also stop only sticking to explicit lolis you ultrafaggots it's like your cum-soaked brains can't think of anything but sex with lolis they're supposed to be CUTE FIRST CUTENESS IS THE GREATEST LOVE OF ALL! CUTENESS IS JUSTICE!! CUTENESS TRIUMPHS OVER ALL HOW CAN NO ONE UNDERSTAND THIS ONE SIMPLE CONCEPT EVERY FUCKING LOLICON I MEET SAYS UUUUUOOOOOHHHH RAPE CORRECTION BUT NO ONE SAYS UUUOOOOOHHHH FLUFFY SKIRT COLLECTION, YOUR SKIMPY BASICALLY NUDE HARLOTS ARE NO MATCH AGAINST ANGELIC DRAWERS UNDERWEAR AND A REFRESHING SUNDRESS IF YOU WANT NAKED SKIN GO FOR A HAG OR SOMETHING, CUTENESS IS SOMETHING A LOLI CAN EXCLUSIVELY PROCLAIM IS HERS AND TO DENY THAT IS INJUSTICE

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[3b2ebcfc13...](https://github.com/mrakgr/The-Spiral-Language/commit/3b2ebcfc1308f71be7898e3ea8b6180408dcd37f)
#### Monday 2022-05-30 10:40:25 by Marko Grdinić

"10:10am. This tension really reminds me of programing. Let me start. I'll try out the hatching thing right now. I do not even need the AOVs, let me just set up the rest of the scene so it fits the came at zero rotation. Not the room scene, but a simple sphere scene.

10:35am. This is one thing that has been irking me. How do I run the compositor in order to get the output?

10:55am. Sigh, what is going on with depth? It does not get saved properly. Nevermind, let me just import these files in Designer.

11am. Hmmm, the stupid thing does not allow me to set arbitrary resolution. Let me render it in 2048 x 2048. This is just an experiment right now.

Let me take a break. By now I've forgotten how to use substance designer.

11:35am. Damn it, this is so annoying. How do I normalize a vector in the compositor? Let me try doing that in Designer's pixel processor instead.

https://www.youtube.com/watch?v=lFfgC0tFiAU
Normal map Rotate part 01 (Allegorithmic Substance Designer 5)

Let me watch this for a bit. I forgot how to get the input variable in the pixel processor at this point.

12:20pm. Fuck. No, I went in the wrong direction. To begin with, all the shape splatterers generate a tile and then randomize them. If I want to use the original image as a mask, at best I get a result like the original image, but with parts of it missing. It looks exactly like the original image being put through a noisy threeshold. It looks like shit.

Furthermore, these substance nodes aren't a good fit for what I want to do because they generate evenly spaced inputs while I want them to randomly scatter them. Furthermore, it is a massive pain in the ass to use the pixel processor of Designer.

I've been thinking about this in the wrong direction. I should be using geo nodes for making these kinds of experiments. That it is in 3d does not matter. I'll put on the isometric view, and use a flat matcap.

Maybe Houdini would be better for this, but let me try it in Blender first.

I feel so uncomfortable right now, like I am on tilt. The tension was so high tonight that I could not get my usual sleep.

12:35pm. Let me take a break here. This is so annoying. It felt like a good idea at first, but I should have seen the thing here today coming. Maybe that Covid really did lower my IQ. Or is my head so filled up at this point that I can't think clearly anymore?

Whatever it is, I have to keep going. I am going to try to make this work either in Houdini or Blender. I'll start with Blender. I'll throw down 100k points, and give them directionality. I'll try loading the files I made as textures and then passing them as density and rotation into the geo node tree. I should be able to use vector to euler. That will be the simplest solution. Designer is such a pain in the ass. If that ends up working, I'll have a basis for everything else.

Maybe I am tense because I want this to fail so I can just get on with it. Common sense is telling me that if this was such a good idea, other people would have done it."

---
## [payday-restoration/restoration-mod](https://github.com/payday-restoration/restoration-mod)@[d23d8d67fc...](https://github.com/payday-restoration/restoration-mod/commit/d23d8d67fcf3e8f3445f80fc5b9a7c5e6e794f1d)
#### Monday 2022-05-30 12:12:32 by Noep

Stuff

- Nerfed Gas
-- Adjusted the cloud durations, most are actually longer....
--- Throwable > 20s (no change)
--- 40mm > 16s
--- 25mm > 12s
--- 3GL > 8s
-- ...But DoT now lasts half the duration of the cloud
--- Throwable - 300 damage over 10s
--- 40mm - 240 damage over 8s
--- 25mm - 180 damage over 6s
--- 3GL - 120 damage over 4s
-- A reminder each gas cloud can only apply its poison once per enemy so its entirely possible to see enemies whose poison expired to just walk through the same gas cloud with no effect applied on them
-- Reduced the radius of the throwable version to 6 meters

- Changed Groza to be a 60 damage rifle
-- Already have a UGL rifle in the 90 damage group (HK417), so it's being shoved into the 60 damage group since it lacks a UGL rifle
--- Downside is there's no readily available 90-damage rifle that has a UGL on it, what with the Scarface Character Pack being longer purchasable
-- On the flipside, it now has access to AK mags/drums
--- Mags will be ever so slightly too far in if you don't have Custom Attachment Points installed, but it'll work without

- Increased the range of the MP40, M45 and Sterling SMGs

- Reduced range of the MP5 and MPX
-- "Yeah you're a 48 damage SMG with a high RoF unlike the other 48 damage SMGs, BUUUUUUT..."

- Speed mag from the Groza is now available on the AS Val
-- Without CAP it'll take on the mag's default appearance
--- The stupid shit I had to do to make it animate tho, don't even know if this was even needed

- Stuff for weapon/attachment mods
-- >:3's Mosin Obrez attachments
-- >:3's Doomstick
-- Beta-C drum for Gambyt's SG-416 (VMP)
-- Probably other stuff I've forgotten

---
## [openstack/kolla-ansible](https://github.com/openstack/kolla-ansible)@[153956e458...](https://github.com/openstack/kolla-ansible/commit/153956e458157e44d73efc3dd369699ff20e4d12)
#### Monday 2022-05-30 12:28:34 by Radosław Piliszek

[CI] Nullify attempts

Per Clark Boylan's feedback [1], retries cause a retry not only
for pre playbook failures but also for cases where Ansible detects
network connectivity issues and they are caused by disks getting
filled to their fullest. This is an issue we experience that
sometimes results in a POST_FAILURE but certain FAILUREs are
retried which wastes CI resources.
The problematic jobs are ceph jobs. They are to be looked into.
Backport to all branches.
We can adjust retries for the core jobs that do not exhibit the
nasty behaviour but first we can try running without retries
to measure the troublesomeness.

[1] https://review.opendev.org/c/openstack/kolla-ansible/+/843536

Change-Id: I32fc296083b4881e8f457f4235a32f94ed819d9f

---
## [yrdsb-peths/hungry-animal-341198919](https://github.com/yrdsb-peths/hungry-animal-341198919)@[1675fdeeaa...](https://github.com/yrdsb-peths/hungry-animal-341198919/commit/1675fdeeaa5a665809c3a39e08097338b659a2c1)
#### Monday 2022-05-30 12:58:51 by 341198919

Absolute perfection.

In the background, you can see a holy spirit performing its divine miracles.

---
## [DIVYA0/CodeChef](https://github.com/DIVYA0/CodeChef)@[342e604414...](https://github.com/DIVYA0/CodeChef/commit/342e604414681fdd467d596fdcefb52a848f49ea)
#### Monday 2022-05-30 13:08:26 by Divya Shanmugam

Create Problems in your to-do list

Problem
CodeChef recently revamped its practice page to make it easier for users to identify the next problems they should solve by introducing some new features:

Recent Contest Problems - contains only problems from the last 2 contests
Separate Un-Attempted, Attempted, and All tabs
Problem Difficulty Rating - the Recommended dropdown menu has various difficulty ranges so that you can attempt the problems most suited to your experience
Popular Topics and Tags
Like most users, Chef didn’t know that he could add problems to a personal to-do list by clicking on the magic '+' symbol on the top-right of each problem page. But once he found out about it, he went crazy and added loads of problems to his to-do list without looking at their difficulty rating.

Chef is a beginner and should ideally try and solve only problems with difficulty rating strictly less than 10001000. Given a list of difficulty ratings for problems in the Chef’s to-do list, please help him identify how many of those problems Chef should remove from his to-do list, so that he is only left with problems of difficulty rating less than 10001000.

Input Format
The first line of input will contain a single integer TT, the number of test cases. Then the testcases follow.
Each testcase consists of 2 lines of input.
The first line of input of each test case contains a single integer, NN, which is the total number of problems that the Chef has added to his to-do list.
The second line of input of each test case contains NN space-separated integers D_1, D_2, \ldots, D_ND 
1
​
 ,D 
2
​
 ,…,D 
N
​
 , which are the difficulty ratings for each problem in the to-do list.
Output Format
For each test case, output in a single line the number of problems that Chef will have to remove so that all remaining problems have a difficulty rating strictly less than 10001000.

Constraints
1 \leq T \leq 10001≤T≤1000
1 \leq N \leq 10001≤N≤1000
1 \leq D_i \leq 50001≤D 
i
​
 ≤5000
Subtasks
Subtask 1 (100 points):
Original constraints
Sample 1:
Input
Output
5
3
800 1200 900
4
999 1000 1001 1002
5
1 2 2 2 5000
5
1000 1000 1000 1000 1000
3
900 700 800
1
3
1
5
0
Explanation:
Test case 11: Among the three difficulty ratings, Chef only needs to remove the problem with difficulty rating 12001200, since it is \ge 1000≥1000. So, the answer is 11.

Test case 22: Among the four difficulty ratings, Chef needs to remove the problems with difficulty ratings of 10001000, 10011001, and 10021002, since they are \ge 1000≥1000. So, the answer is 33.

Test case 33: Among the five difficulty ratings, Chef needs to remove the problem with a difficulty rating of 50005000, since it is \ge 1000≥1000. So, the answer is 11.

Test case 44: Chef needs to remove all the five problems, since they are all rated \ge 1000≥1000. So, the answer is 55.

Test case 55: Chef does not need to remove any problem, since they are all rated \lt 1000<1000. So, the answer is 00.

---
## [Sea-of-Lost-Souls/Tannhauser-Gate](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate)@[a3c0819e80...](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate/commit/a3c0819e8091ab99a5ab8f53b59c4687e5b2f2cf)
#### Monday 2022-05-30 13:26:33 by SkyratBot

[MIRROR] Removes (in) smoke and foam reactions [MDB IGNORE] (#13963)

* Removes (in) smoke and foam reactions (#67270)

* Removes smoke and foam reactions

Turns out when you let reagents react in foam/smoke, people put bombs in
them.

This behavior was initially added to just smoke, accidentially in
(56f7ac0c0a29e8f898c4aab35947d027952b43f7) accidentialy (thalpy tried to
make both foam and smoke instant react, but instead made smoke's temporary
holder reagent instant instead. hhhhhhh)

Assuming this was intentional it was then extended to foam in
(1879e2d338c9bf5f191cef6c39944b26a41e6092)

Basically, we're idiots. Anyway lets just walk this all back to instant
reaction on smoke/foam formation. Hate you people

* Removes another source of gunpowder smoke

Temporal told me about this. Gunpowder uses an ex_act signal as a
starter, and that also counts for smoke objects.

Really don't want instant detonation smoke bombs, so let's just... not
shall we?

* Removes (in) smoke and foam reactions

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [newstools/2022-information-nigeria](https://github.com/newstools/2022-information-nigeria)@[68f793cb59...](https://github.com/newstools/2022-information-nigeria/commit/68f793cb59ee8c32e0e41b5b8b47cffc48a0f5e6)
#### Monday 2022-05-30 14:52:49 by Billy Einkamerer

Created Text For URL [www.informationng.com/2022/05/18-year-old-girl-reportedly-takes-her-life-after-being-assaulted-by-family-friend.html]

---
## [SovietJenga/tgstation](https://github.com/SovietJenga/tgstation)@[2d246c8205...](https://github.com/SovietJenga/tgstation/commit/2d246c8205ad3e9a8436f69f120509ca2ea357c3)
#### Monday 2022-05-30 14:57:40 by SovietJenga

I'm fucking stupid

This experiment works differently from what I remembered it was.

---
## [k21971/dNetHack](https://github.com/k21971/dNetHack)@[6406d2d4bc...](https://github.com/k21971/dNetHack/commit/6406d2d4bc959480d8f62a86a414dc373e730adc)
#### Monday 2022-05-30 15:17:45 by chris

Add spell bonuses from PC species as well as role.

The base bonus is (spell level+1)/2 * 5. This yeilds bonuses in the vanilla range, but that may be too small to really matter :-/

Humans: Abjuration. They make things mundane
Clockwords: Wizard lock (auto cast). Affinity with mechanical things.
Chiros: Magic Mapping. They know caves.
Dwarves: Digging. They dig.
Drow: Sleep. Affinity with sleeping poison.
Elves: Remove curse. Low-key holy.
Gnomes: Invisibility. They can vanish.
Half-dragons: Detect treasure. Dragons can horde.
Incants: no bonus. Already has a bonus to all spells.
Orcs: Cancellation. Good vs. angels and other mighty foes.
Vampires: Drain life. They drain life.
Yukis: Charm monster. Nymphs.

---
## [ecwall/cockroach](https://github.com/ecwall/cockroach)@[f782e45fd0...](https://github.com/ecwall/cockroach/commit/f782e45fd0da015396bc758e855535a951f2e21a)
#### Monday 2022-05-30 15:53:56 by Andrei Matei

util/timeutil: don't strip mono time in timeutil.Now

Our timeutil.Now() insists on returning UTC timestamps, for better or
worse. It was doing this by calling time.Now.UTC(). The rub is that the
UTC() call strips the monotonic clock reading from the timestamp.
Despite repeatedly trying ([1]), I've failed to find any reasonable
reason for that behavior. To work around it, this patch does unsafe
trickery to get a UTC timestamp without stripping the monos.

Stripping the monos has the following downsides:
1. We lose the benefits of the monotonic clock reading.
2. On OSX, only the monotonic clock seems to have nanosecond resolution. If
we strip it, we only get microsecond resolution. Besides generally sucking,
microsecond resolution is not enough to guarantee that consecutive
timeutil.Now() calls don't return the same instant. This trips up some of
our tests, which assume that they can measure any duration of time.
3. time.Since(t) does one less system calls when t has a monotonic reading,
making it twice as fast as otherwise:
https://cs.opensource.google/go/go/+/refs/tags/go1.17.2:src/time/time.go;l=878;drc=refs%2Ftags%2Fgo1.17.2

An alternative considered was setting the process' timezone to UTC in an
init(): time.Local = time.UTC. That has downsides: it makes cockroach
more unpleasant to link as a library, and setting the process timezone
makes the timestamps not roundtrip through marshalling/unmarshalling
(see [1]).

[1] https://groups.google.com/g/golang-nuts/c/dyPTdi6oem8

---
## [guest3444307/OneshotGB](https://github.com/guest3444307/OneshotGB)@[647b214a0a...](https://github.com/guest3444307/OneshotGB/commit/647b214a0aa77571d826e7704f9f09c8278c2120)
#### Monday 2022-05-30 17:05:08 by guest3444307

5/30/22 Color Update

5/30/22: Oh my god, i wish i had someone else do the coloring for me, like jesus  this is unironcially painful if i want it to look good, i spent like an hour on one just now. Its b2 (b0-2 GBC, right panel) , it took like 8 palletes for that, and lots of funny edits you can't see in color (like using black, the background color on places where you can't see the background, man this would look weird on DMG, not the weirdest as that belongs to wake4 (or 5, they are basically the same) Maybe i'll go and work on something else for now.

---
## [C7-Game/Prototype](https://github.com/C7-Game/Prototype)@[d4cb71a167...](https://github.com/C7-Game/Prototype/commit/d4cb71a1673b919ddf87d8afcbb2e8ad9ad25352)
#### Monday 2022-05-30 17:14:03 by Quintillus

WIKI INFO - Build out strategic priorities a little bit.  WarPriority is a notable one as it is the first one that includes properties.

I've tried to build the priorities so there will be a common interface.  The goal being that new priorities can be added being mods, and they can still be serialized.  The interface should help for this.  If all of our StrategicPriorities were bespoke hard-coded, it might be convenient, but it would not lend itself to extensibility.

The challenge is going to be how do we merge those priorities, convenience of writing the logic, extensibility, and serialization?

This is still an evolving thought process, and I'm not totally sold on this dictionary-of-dictionaries approach, it just seemed like the most convenient way to return a weight *and* some required data about how that weight was chosen and what to do if this priority is chosen by the arbitrator.

The other half of the thought process that's not yet fully coded is that if a priority is chosen, its info should be stored in the data classes.  My general thought here is that by returning property maps, we should be able to store those, and a reference to the type of StrategicPriority, in the data classes, allowing us to reconstruct objects of the appropriate type, put in the relevant properties, and re-load from save.

The engine will also have to be able to look up the priorities based on name... maybe a key type thing?  This should also be stored in the save.  So basically, on load the engine will have the key, the weight, and properties.  It'll use the key to find the appropriate class, instantiate an instance, and stuff the properties onto that instance (and maybe the weight or maybe that's higher-level metadata that goes elsewhere).  This yields an fully inflated StrategicPriority instance that the AI part of the engine can then reference to calculate things.

Combining this with a lookup mechanism for StrategicPriorities should yield moddability.  I'm reminded of Java's "Service Provider Interface" concept, the gist of which is that if you make a class that follows an interface, and register it with the JVM in a certain way in your program, the JVM magically gains new capabilities.  An example is if I write an image processor for PCX files, and register it correctly, the general image ImageIO capabilities in Java can now magically handle PCX files, e.g. ImageIO.load("x_title.pcx") will just work, even though in stock Java it wouldn't know what to do with a PCX.  It works for other types of services too.  Our specifics will differ, but I think the goal should be similar - if you write a new StrategicPriority and follow a given interface, it'll magically be incorporated with the AI.

The remaining hard part is how is the strategic AI looped in to decision-making?  There are theoretically a thousand places this could be looped in, but if we want it to be extensible, we have to have standard interfaces.  But the StrategicPriority also has to know enough about the situation to be able to interpret what's going on.

For now I'm thinking some combination of weights and modifiers being providable by the strategic priority.  E.g. for city production, it should be able to make some things be produced more often, and that's a weight based thing.  But I'm sure there's other cases I'm not thinking of that make things more complex.  I'm also aware of what Jon or Soren mentioned somewhere about overly generic AIs sometimes not being decisive enough.  It'll be interesting...

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[bb83aeac74...](https://github.com/mrakgr/The-Spiral-Language/commit/bb83aeac747faa7d166d6d8582d4b1bd764f2d29)
#### Monday 2022-05-30 17:33:56 by Marko Grdinić

"1:40pm. Let me catch up with Dark Lady and I will push the idea to its conclussion. In the worst case, I'll open up Houdini if I can't import the textures properly in Blender.

2:10pm. Magical Trans and then I will resume. That was short, let me resume.

2:15pm. Yeah, this feels like programming. This feeling of fear and uncertainty is something that I haven't experienced in a while.

https://youtu.be/eJoctLJJmn4
Using UV Maps with Geometry Nodes [In Blender]

Yeah, this is exactly what I want.

2:30pm. I feel like my IQ is 80 right now. Just why isn't this working for me? Forget the other image. Even the random painted one is not working right now.

2:40pm. Fuck, what the hell is wrong here? For some reason it is simply not working. Let me try the 3.2 Alpha version.

2:45pm. I just had an inlking of something. What if the reason it is not working is because I am using a flat plane without any vertices? But this is not displacement, it should work anyway.

3pm. It seems it maps the UV coordinates to vertices for some reason so in fact does need subdivision. How ridiculous. Well, let me distribute spheres on this. I just want to finish the experiment. It already took my entire day. So far the results are not promising with just dots.

Now how did align euler to vector work?

https://youtu.be/0E1K9j9zoik
[Tut] Align Euler to Vector Node Explained - Blender Geometry Nodes 3.0 Field

I hate this. I studied this months ago, but by now it has all faded.

3:35pm. I am trying to put my thoughts together. I still feel like my brains are leaking.

> RGB colors have values between 0 and 1, whereas a model's normal values are between -1 and 1. A color value of 0.5 in a normal map translates to a model normal of 0. The result of reading a flat texel from a normal map should be a z value of 1 and the x and y values as 0.

4:10pm. Thank you compositor output node for just clipping those normals to 1.

I give up. I can't make this work. It feels like I've been rolling nat 1s starting from last night.

I feel exhausted, my brain is not really working. I am confused as to how do the normal things, I feel confused about how to do rotations, I feel hesitant whether I should transform the normals. I keep running into weird issues that waste endless amounts of my time.

I am completely lost on what the functionality of vector rotation nodes should be. Just why did the saved .blend file end up being 600mb?

///

* Procedural hatching & painting via shape splattering
    * Need to extract depth, normals and image info
    * Also want to check out the illustration shader for Blender
    * Easiest to try out in Substance Designer

///

Forget the above. Though I did not manage to get it to work correctly, I've learned enough to realize what the problem is. Based on what I've seen, the results are not at all promising. I thought there might be a way to get good line art from this idea, but instead I get a very noisy result. And indeed, I am mostly taking the original image and sampling from it so it is no wonder I get such results.

4:25pm. Yeah, this inner struggle and turmoil definitely reminds me of programming. It is like I am right back in those days. Forget this idea. Even if I go back to the compositor and have it output the correct normals I won't get a good looking result. Not from just sampling the image like this.

If I really want style transfer, doing it with NNs would not be a bad idea.

How annoying. I think adding depth and normals rather than just having the image should give a benefit, but I can't put the idea together sensibly.

4:30pm. Anyway, it is not like I gained absolutely nothing from this.

My next goal should be to study cryptomattes. While looking through the compositor I see that it has some special stuff for getting the object ids out.

5pm. Had to take a break. Let me resume. I'll do a little /wip/ update.

///

> I should be able to the brightness values as density for scattering strokes as if they were objects.
This was such a stupid idea, it ended up wasting my whole day today. What you get when you sample an image is a nosy image. Exchanging pixels for directional strokes does not mean the result will be in any way appealing or legible. Crunching the midtones is a lot more appealing than this technique. Today sucked, it felt like I was rolling nat 1s all day today. Despite the idea being simple, it was really difficult to try this out and I kept running into all sorts of weird problems.

Next up, I am going to do some studying on mattes. I am not sure where I read it, but they might be a succinct way to extract object ids from the image, so I want to investigate what they are.

///

Let me look for a matte tutorial. Hopefully I'll some good sleep tonight.

5:15pm. I guess I understand now what that illustration shader guy meant when he said he couldn't use UVs. It is ridiculous that I need map them to individual vertices first. This couldn't be any more inefficient. I am also confused why it is possible to paint textures in solid mode. So many mysteries.

Forget anything having to do with programming. When it comes to art, the closest I'll get to programming is by scattering geometry. Anything more complex and I am out. I regret trying out this idea today. I am going to tighten my hold on the wheel.

https://youtu.be/-ghSlQkdxww
what is Matte painting

https://youtu.be/-ghSlQkdxww?t=244
> It took 3 months to paint all the crates and boxes (for the Raiders of the Lost Ark warehouse scene).

Yeah, it would be easier to paint it than to stack all the crates together.

https://youtu.be/LYJHIAIrIos
Introduction To Matte Painting - Digital Painting Basics - Concept Art Tutorial

This is a 1:13h tutorial by Walid. He has that 3d for artists course. I checked on Persia and I can't find it there.

https://www.youtube.com/results?search_query=matte+painting

I actually hadn't heard of the term 'matte painting' before today. Matte sure, but not together with painting. It just shows how little I know.

Damn, I do not feel like doing any more tutorials, I'd rather just close, but I am not in any state of mind to relax properly either. I certainly do not want to spend my time on games and manga. I am just frustrated over all the head bashing today and I want to make progress.

Focus me. Let me just do it.

https://youtu.be/dvW16y2IaA0
Matte Painting in 10 minutes

Actually, let me watch this first since it is shorter. I want to see how he does it.

5:50pm. That was impressive. Let me take a look at the tut by valid.

5:55pm. https://youtu.be/LYJHIAIrIos?t=198

These kinds of paintings are very impressive. So that matte nodes in the compositor are there to enable this kind of workflow. For some reason I can't find much in the way of Blender matte tutorials. I wonder why?

Don't tell me I'll actually have to read the docs to find out what they do?

https://youtu.be/LYJHIAIrIos?t=558

Nevermind this for now. I do not feel like watching all of this.

https://youtu.be/onYNLY8B62I
New Cryptomatte Workflow in Blender 2.93: In Depth Tutorial

Let me watch this.

https://youtu.be/onYNLY8B62I?t=38

Why the hell is this? Isn't there a beginner tutorial for this?

https://youtu.be/onYNLY8B62I?t=146

I guess this is a beginner tutorial after all.

https://youtu.be/onYNLY8B62I?t=231

The pick channel. It might be worth exporting this into CSP. Would save me from having to paint flats in some cases.

6:10pm. I get the object and the material, but what is the asset pass?

I know that Blender has a new Asset browser, but I've never tried it out.

https://youtu.be/onYNLY8B62I?t=369
> It is composed of multiple objects and multiple materials, so in this case we will create an asset.

It seems he will explain this.

https://youtu.be/onYNLY8B62I?t=432

So it is just parenting? Easy enough.

https://youtu.be/onYNLY8B62I?t=609

This is pretty cool. It would have made the couch scene a lot easier to deal with.

https://youtu.be/onYNLY8B62I?t=635
> We need to use: multi layer exr, 32 bits, no or lossless compression

This is harsh. I wonder why?

In hindsight though, I should have used this to export the normals, it would have saved me a lot of headache. Let me leave for lunch for a bit.

6:40pm. I am back. Let me finish the tutorial.

https://youtu.be/onYNLY8B62I?t=827

It seems he will show how to import files in order to composit them.

https://youtu.be/onYNLY8B62I?t=931

EXR Saver addon which is free can save me time for this kind of thing.

6:55pm. https://docs.blender.org/manual/en/latest/glossary/index.html#term-Matte

The entry for matte is literally Matte Mask. It seems all the mattes have something to do either with creating masks or dealing with color spillage from blue/green screens. I am not sure sure what blue and green screens are - I saw such things sometimes in movie behind scenes documentaries, but that sort of thing won't be useful to me here.

As far as I am concerned, the cryptomatte node is the one I need.

https://github.com/3d-io/Blender_Exr_auto-pass_saver

I'll get this addon tomorrow.

7pm. I'll close here after a little /wip/ post.

There is no need to hesitate about this anymore. I'll extract the freestyle edges and the cryptomattes and try out painting the room in a cell shaded style. After that I'll get back to modeling the room and do the sculpting touches. That will be my art style from here on out. I'll stick to it and get good at it. I am not sure if I'll ever get beyond 3/5, but that does not matter. I'll do what I can with whatever talents I have.

7:15pm. Let me close here. I am dead tired. As bad as today was, learning about mattes was a definite benefit so it is not a complete waste.

Tomorrow I am going to play with freestyle edges. After that I'll extract them and cryptos into CSP and start painting. I won't do much of it by hand. Gradient maps, a bit of the blur tool, maybe posterization will be all I need. Since I haven't put flats on the Blender side, I'll lean towards gradient maps. but posterizing and then filling in the flats afterwards is also a choice.

The goal here will be to convert the room to a cell shaded style, go back and bring the modeling level from 70% to 100%, and then paint it again. After I do that I will have cleared my mastery challenge and can consider myself a low level 3/5 artist. I can't really consider myself good at that level, and there will be people better at me at art everywhere, but those people won't be lying around on the street. Today was really harsh, I do not want to work like today. I want to have clear goals and move towards them. I do not want to try out ambiguous programming techniques. If I have to do research, I should wait until the scene is set for such an endeavor.

I'll live my life quitely until the world gives me a chance to play on the bigger stage. Forget the AI chips. I should be focusing on getting money for the 40xx Nvidia cards.

Let me just finish this scene and I will be able to start thinking about music. There won't be any changes to the plan. I will do it all. Direct 2d will have to be sacrificed, but I'll get good results either way and that is what really matters. If I could solely focus on art then it would be fine to take whatever time I need to master it, but my plate is so full to the point of overflowing. Unless I simplify my technique to its absolute limit I will fail at the quest. I might fail regardless, so I certainly won't be taking the time to get good at 2d drawing.

I'll make the necessary sacrifices to attain my goals. I do not know how much time I have, but I'll use it doing what I want. That is the proper way to live."

---
## [InFTord/DSharpPlus](https://github.com/InFTord/DSharpPlus)@[8380b5b2de...](https://github.com/InFTord/DSharpPlus/commit/8380b5b2deb9f2243c87e3277a34902ec08bb716)
#### Monday 2022-05-30 18:49:30 by InFTord

[ci-skip] Fix docs typos in DiscordRestClient (#1317)

* Update DiscordRestClient.cs

* insanity

edited all of this with github site editor
madness
editing 2k lines of code is kinda pain with github site editor

* im idiot

* fixing...

* uh oh

* i love fixing docs

* fixing inconsistent ID stuff..

---
## [yogstation13/Yogstation](https://github.com/yogstation13/Yogstation)@[c3e823d052...](https://github.com/yogstation13/Yogstation/commit/c3e823d052f6e07b6d1f571d0989c6305b53d5f6)
#### Monday 2022-05-30 19:12:10 by Jamie D

Adds APC and different areas for the multiple air alarms.. why could you siphon interrogation from perma.. (#14163)

* Update Space_Station_13_areas.dm

* Fixes Brig to not be Shit

* Fixes Areastring

* other maps

* Update code/game/area/Space_Station_13_areas.dm

* Fucking hate baiomu so much

* fucking apc

---
## [yogstation13/Yogstation](https://github.com/yogstation13/Yogstation)@[8b77243ce9...](https://github.com/yogstation13/Yogstation/commit/8b77243ce9da72645291d6f22f798bc32611a706)
#### Monday 2022-05-30 19:12:10 by TheRyeGuyWhoWillNowDie

Makes bloodbrothers start with the makeshift weapons book learned. (Jamie Edition) (#14094)

* makes blood brothers a bit less shit

* oopsie

* improve???

* what

* huh??

---
## [Atry/hhvm](https://github.com/Atry/hhvm)@[648c963897...](https://github.com/Atry/hhvm/commit/648c963897f25839c9d1697939acaf8762a64978)
#### Monday 2022-05-30 19:26:38 by Lucian Wischik

mitigate HackIDE:idle messages

Summary:
There are two separate things going on with this diff. Both are prompted by a user repro where the progress-message "[HackIDE:idle]" keeps popping up.

**Fewer IDE_IDLE**. The behavior of hh_server is, if it receives an RPC from clientLsp, then it must receive a subsequent IDE_IDLE message from clientLsp before it will do any typechecking. It does this because it takes ~1s for hh_server to wind down a typecheck and then start one up again, which made things clunky and slow when you were doing a lot of typing and interrupting a typecheck with every keystroke you made. The design is that IDE_IDLE only gets sent after the LSP queue has been emptied.

We had accidentally gotten this code wrong at times, so that sometimes the IDE_IDLE message didn't get sent and hence hh_server got permanently stuck, but that seems to have been fixed for a year or more. The final robust design was that for every single event (other than "tick" meaning no-event), then clientLsp would believe it needed to send IDE_IDLE.

This became a bit inessential with clientIdeDaemon, where we'd send IDE_IDLE even after clientIdeDaemon had handled a hover request all by itself, but wasn't too bad.

It became downright frustrating with streaming-IDE-errors, where hh_server sends error updates while a typecheck is underway. Every single one of these counted as an event, which prompted the catch-all robust design to think it needed to send an IDE_IDLE, so it did, which caused hh_server to interrupt then restart its typechecking for ~1s to deal with this message. DOH!

This diff changes clientLsp so that we only think we need to send IDE_IDLE after having sent some kind of message to hh_server (apart from sending IDE_IDLE to hh_server).

**Unclear status**. When hh_server received and processed IDE_IDLE, then it would update progress.PID.json accordingly, and the command-line hh_client would display the progress message [HackIDE:idle]. But then it takes ~1s for bulk typechecking to resume, we're not going to display any progress message until it does, so users just see [HackIDE:idle] even when they know there's a lot of typechecking to do and they just wish it would get on with it. This is confusing to us on the hack team, and to users.

This diff makes a minor change. It now displays [HackIDE:idle] while it embarks upon handling this request, and [HackIDE:idle done] after it's finished. In this way, we on the hack team will at least know that the "idle" command-handling is done, and what we're witnessing is the ~1s it takes to resume after the interruption.

(I think it's good that users and we on the hack team will know WHICH interruption is the cause for the ~1s resumption that we're seeing.)

Did all these interruptions cause actual slowness in overall typechecking time? -- not that I could reasonably measure, not within the bounds of noise.

Reviewed By: CatherineGasnier

Differential Revision: D36392047

fbshipit-source-id: 245f22eb33e9aeb034f8a7a193f3c941ed257610

---
## [nikothedude/sojourn-station](https://github.com/nikothedude/sojourn-station)@[9f7af6b698...](https://github.com/nikothedude/sojourn-station/commit/9f7af6b698a6633907432576f9699af209dec6cd)
#### Monday 2022-05-30 20:32:40 by nikothedude

FUCKING HOTFIX FOR A STUPID FUCKING BUG (#3459)

* FUCK

* HOLY SHIT IM DUMB

---
## [fortune13-ss13/thewasteland](https://github.com/fortune13-ss13/thewasteland)@[013fb2bd4b...](https://github.com/fortune13-ss13/thewasteland/commit/013fb2bd4bd6ce216844c984da9dc5ffed316c61)
#### Monday 2022-05-30 20:43:58 by ishitbyabullet

Fallout Alien Content (#539)

* ncr veteran ranger removal

sorry, boys, but 18 yr old female veteran rangers aren't lore accurate.

* NCR no longer has farming or water

No one ever did the sharecropper farm quest in FNV anyways.

* NCR must actively pay taxes

There is a new need meter similar to thirst and hunger for this now.

---
## [JoshMalloyDev/demo-day-project](https://github.com/JoshMalloyDev/demo-day-project)@[113f3d575a...](https://github.com/JoshMalloyDev/demo-day-project/commit/113f3d575ad3282df3c71e751bd56d7fca0d345d)
#### Monday 2022-05-30 21:48:28 by Joshua Malloy

Add files via upload

ADHD Demo Day Project

Description: This is an app for those who live with ADHD. It uses data visualization to promote self-forgiveness, music to drive timers for tasks instead of alarms, computer-generated artwork to add creativity to the everyday process, and extra tools for when decision-making becomes an obstacle to your health.

SELF-FORGIVENESS
Before starting any task, the app will launch a modal that asks the user did you do X self-care thing before? 
As the user presses the continue button for each self-care prompt, it will store that “yes” or “no” answer to the database. 
The app will create a graph that displays how many self-care activities they engaged with that week
Purpose: Even if they didn’t accomplish their goal, there’s still so much invisible work that was accomplished that should also be recognized as a success. Usually, we work in binaries - where you either failed or succeeded at your task. I want to give users a different option that involves grace, and no judgment.
MUSIC AS TIME-REFS
Allow users to set a timer for a task
That time will be stored in the database
We will use the Spotify API to create a playlist, and randomly add songs from their account. As the songs add to this new playlist, we will log the playlist’s total time and stop adding songs when the playlist is around the timer amount
When the time is up, the playlist will stop playing and a notification will alert them 
They have the option to set another timer and do it again
Purpose: alarms are very easy to shew away. Generating music will create a flow state for the user, and removing the flow state (by stopping the music) can create a similar effect that a timer has on a neurotypical person
ARTWORK
When a user designates a task to track, they are asked to assign that task a specific color. The color and task will be stored in the database
Uses p5.js to create graffiti-like strokes (all strokes should have varying opacity levels)
The assigned color will be passed to the p5.js API and the more days that you have accomplished your tasks, the longer the API holds the mouse down and creates a brush stroke (the x-axis and y-axis of the brush strokes will all be randomly generated to create variety in strokes)
By the end of the week, there should be a square with various different colored brush strokes on this square
The background of the square will be a very-low-opacity, randomly-generated background color to prime the “painting”
When the week is over, the page will display their square painting
There will be a section filled with these weekly cover arts titled by that specific week
Purpose: to add some creativity and possible motivation to keep accomplishing tasks
“CAN YOU CHOOSE FOR ME?”
A user is able to upload simple recipes they can think of and the ingredients it takes to make it
Foods can be labeled breakfast, lunch, and dinner
When a user is struggling to decide what to eat, they press a “choose for me” button 
The button stores the current time of the click, and if its before noon, then the app randomly displays a breakfast food, if its from 12pm to 5pm it’ll display a random lunch recipe, and if its from 5pm-1am, it’ll display a random dinner option (maybe it's not till 1am?)
Purpose: take care of your body and health without letting anxiety stop or delay you
“WHERE YOU AT?” 
***Maybe I’ll use this but maybe I won't, depending on time and if it fits…
Use a GeoTracker to calculate someone’s latitude and longitude every second 
Use a googled formula to convert the total distance into mm
Use a googled formula to convert mm into approximate steps taken
Every time someone presses the “pause task” button, the app tracks their steps
When they press “continue” the app tells them how many steps they’ve taken in that time
Purpose: “This is how many steps you’ve taken and how far you’ve strayed from X task”

---
## [rraykzu1/rraymerald](https://github.com/rraykzu1/rraymerald)@[7333f5418f...](https://github.com/rraykzu1/rraymerald/commit/7333f5418f54848853905039395b59ff3b4f849f)
#### Monday 2022-05-30 23:55:08 by rraykzu1

i fucking hate this shit, ported check table for move from CFRU

---

