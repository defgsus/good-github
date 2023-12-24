## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-12-23](docs/good-messages/2023/2023-12-23.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,149,738 were push events containing 2,782,978 commit messages that amount to 147,528,572 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 56 messages:


## [jlsnow301/tgstation](https://github.com/jlsnow301/tgstation)@[33e10634ba...](https://github.com/jlsnow301/tgstation/commit/33e10634ba89c28c1ca3518068e916ec0a10b33e)
#### Saturday 2023-12-23 00:31:33 by Iamgoofball

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
## [linkylink21/tgstation](https://github.com/linkylink21/tgstation)@[5f305ca5f7...](https://github.com/linkylink21/tgstation/commit/5f305ca5f7b3143360c2107102ea10ad96326839)
#### Saturday 2023-12-23 01:28:46 by ATH1909

Removes an exploit that can farm Russian revolver moodlets, adds Russian revolvers to the contraband section of games vendors (#80159)

## About The Pull Request

Fixes https://github.com/tgstation/tgstation/issues/80158 by making
curses block you from playing Russian roulette regardless of whether or
not there's a live bullet in your Russian revolver's chamber.

A Russian revolver has been added to the contraband section of each Good
Clean Fun vendor.

## Why It's Good For The Game

The bug is incredibly funny, but ~~I want GBP~~ probably should be
fixed.

There's no actual way to get (more) Russian revolvers outside of the
mapstart ones, and that can be a bit stifling to gimmicks that involve
them. And Russian roulette IS a game.

Like the roundstart ones, you could unload these vendor revolvers for
.357 bullets, but you can already just print .357 bullets from a hacked
autolathe directly, so I don't think that's an issue.

## Changelog

:cl: ATHATH
fix: Spacemen can no longer use curses to cheat at Russian roulette by
selectively blocking attempts to shoot themselves.
add: A Russian revolver has been added to the contraband section of each
Good Clean Fun vendor.
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [SizableShrimp/AdventOfCode2023](https://github.com/SizableShrimp/AdventOfCode2023)@[3c9005dc41...](https://github.com/SizableShrimp/AdventOfCode2023/commit/3c9005dc41cec04af95f76d11b18658bf4192494)
#### Saturday 2023-12-23 01:40:21 by SizableShrimp

Implement Day 21 in Kotlin

Today's puzzle was unfortunately the only one so far that took me more than 24 hours to complete. I got Part 1 in 12 minutes and 6 seconds for a placement of #1063. For Part 2, it took me around 2 days to fully complete. I pretty early on realized that I would need to do some math to calculate the extent of the reachable plots.

From memory, I think I came upon the parts of the solution in the following order:
* I realized that there was a core set of plots where all squares were reachable
* I realized that there was a distinction between what I call "odd squares" and "even squares" -- the odd square includes the main square, and then the odd/even squares alternately tile the infinite grid
* I realized that there were fringe squares that could only partly be reached into

What took me the longest was actually figuring out the math. A HUGE bug of mine was mistaking the fact that the number of steps required to reach the edge is lost forever. I was accidentally using that step length twice. When I realized this, it actually completely changed the fringe squares, and I had to start my math for that over.
Another big revelation was that the real input was actually easier than the sample input. There is a direct line to each edge from the starting point, and the starting point is in the exact center of the main square. This simplifies things a lot.
This made me realize that the topmost square was an exact triangle shape with the upper 2 corners not reachable, with similar logic for the bottommost, leftmost, and rightmost squares.
There are 2 other types of fringe squares under this logic. For each set of northwest, northeast, southeast, southwest directions, there are a set of squares where all parts are reachable except the furthest corner, and then a similar inverted one where only the closest corner is reachable.

After realizing all this, it just becomes a challenge of exactly calculating the number of reachable plots. Since we want all garden plots that are reachable in exactly the number of steps provided, we want all plots up to and including the furthest-reachable plots but with a condition of matching "oddness," as I call it. If our required step count is odd, then the plots that we want will have an odd distance, and similar for an even step count. For the step count provided in Part 2, it is a very nice number. After subtracting out the 65 steps necessary to get to the edge in any direction, we can reach up to exactly 202,300 squares in any direction, not including the main square.

What tripped me up the most, besides double counting the initial 65 steps to the edge, was the "oddness" we wanted to calculate for specific fringe squares. It turns out I had the right strategy ages ago, but I had calculated the wrong required oddness for the fringe squares.

All in all, the puzzle was pretty interesting, but the math was annoying. I'm almost sure that I overcomplicated this, somehow. Or maybe not? My code is pretty slow, though. It takes about a second to run, but we are also talking about Kotlin here. I could definitely speed it up if I wanted to, as I calculate distances past what I actually want.

To be honest, I'm just happy that I was able to complete this puzzle without any outside help. The example input was quite annoying because it did not match the ease of the real input at all. And none of the provided sample step counts were odd, which made it effectively useless for me to be able to use that data in my simplified solution.

---
## [Floofies/tgstation](https://github.com/Floofies/tgstation)@[bed92e193c...](https://github.com/Floofies/tgstation/commit/bed92e193ce4a79824fd4fd30a900245dca870ae)
#### Saturday 2023-12-23 01:43:41 by san7890

Further Prevention of Disposals Qdeletion (#79714)

## About The Pull Request

Fixes the consequences of #79629 - Verdict is still out on what the root
issue is

This has been an issue for the last two years and everything I go
bananas trying to get a consistent reproduction case to figure out the
root issue. After three session of picking, I think it's just a
consequence of certain thing in disposals code sleeping due to
`addtimer()` and whatnot so I'm just throwing in the towel and just
making it so we stop sending atoms to nullspace for no reason.

`target_turf` is typically always a present arg, but regardless we are
guaranteed to get a valid turf to send people to instead of the deleted
mob room. We still `stack_trace()` whenever this happens, so tracking
this issue doesn't change any more than the present status quo- we just
don't keep torturing mobs by sending them to the shadow realm.
## Why It's Good For The Game

One day we'll figure out why we keep getting `null` passed into
`forceMove()` like this but today is not that day. i know turfs
technically can't be deleted but it's just there as a safety since we
nullcheck anyways (which is the whole point of this fix). Let's just
stop screwing with players for the time being

also the code looks much better
## Changelog
:cl:
fix: Safeties in the code have been added to prevent things in disposals
going into nullspace whenever they get ejected from a pipe - you will
just magically spawn at the turf that you were meant to be flung
towards.
/:cl:

---
## [rsm28/lethal_company_batch_files](https://github.com/rsm28/lethal_company_batch_files)@[ca6f800eb6...](https://github.com/rsm28/lethal_company_batch_files/commit/ca6f800eb6057eebc4e663bb3a159ae56331d1fe)
#### Saturday 2023-12-23 01:54:26 by oanon-ak

MODPACK IMPLEMENTATION WOAH

also fixed consistency of command calls, forced lc_api 2.2.0 install (fuck you 2018), version bump

---
## [crawl/crawl](https://github.com/crawl/crawl)@[d47e5fa42b...](https://github.com/crawl/crawl/commit/d47e5fa42b0c36b827545ea5c770d40b071d1a4e)
#### Saturday 2023-12-23 02:11:13 by regret-index

Buff?: Clouds of negative energy -> clouds of excruciating misery

Clouds are weird. (Much of Crawl is weird.) Their damage is fixed per cloud
type, which makes it difficult for clouds to be used against the player
outside of a given rather narrow window of reasonable damage, since there's
rather limited and possibly expensive ways to deal with large amounts of
space becoming unavoidable. (Some effects, like poison, miasma, and
spectral flame do sidestep this, at least). We've also got a pretty large
amount of clouds at this point that are extremely narrow in their presence
and use, for very disparate circumstances- a pile of different decorative
opaque clouds and damage types mixed between Wizlabs, Desolation, Xom,
condenser vane, and two or less monsters each for almost everything besides
miasma. It'd be nice to try and make more dramatic effects when we have so
many, so it'd be possible to compress such endless lengths over time.

As part of this notion, I'm heavily revamping a cloud essentially exclusive
to condenser vanes and Xom- clouds of negative energy. They're currently
somewhat weird within the vane itself, positioned at the same tier as acid
and thunder but much easier to resist than either for monsters and more
awkward to idly walk through than acid for players. They're also not very
interesting either way, another cloud doing another flat amount of damage
like the other standard element clouds despite undead already having the
unique non-standard miasma and spectral flames to work with.

I'm revising these clouds away from dealing the standard cloud damage of
10-32 damage to players and 6-22 damage to enemies to instead deal with
flat percents, in the style (but not practice) of torment. These newly
renamed clouds of excruiating misery now deal 10% of the player's max HP
(6.6% with rN+, 3.3% with rN++, none with rN+++) and 15% of monster max
HP whenever they hit (most monsters have a lot less raw health than most
players, so they on average take more damage from even numbers lowered
for them and not players- likewise, such low-ish percentage damage has to
be higher to monsters for it to work properly). This should make them
scale reasonably to be a little dangerous if liveable fine early on and
reasonably terrifying later on, thus making them usable for future monster
re / designs. It should also help with rN+ being a very neglected
resistance for most players on average, since later versions of these
cloud should deal quite a bit of damage.

Additional notes:

 * The tile has been somewhat changed with a hard light overlay of rltiles
   sourced wall_undead. We could really do with more cloud tile bases
   eventually. At least they're definitely obviously different colours than
   miasma or spectral flames in console?

 * Condenser vane is unchanged, since it'll take a bit of a while to tell
   just how good these clouds are in player hands- it's a worse roll
   earlier on (low monster health) and already an easily bad roll later on
   (lots more undead and unliving), but it can now really shred through
   giants and uniques. Monster cloud safety versus intelligence checks
   in _mons_avoids_cloud is a very per-case hacky mess- if there's any
   concerns about its strength, a proper check for this new cloud's
   non-standard damage should be added there just for starters.

 * The name of "excruciating misery" can be quibbled over in the future,
   but with such rapid damage against e.g. player trolls it felt like it
   needed some emphasis. It's also meant to both fit with and be a little
   distinguishable from Crawl's love of adjectives for Pain- Agony,
   Torment, Anguish.

---
## [crawl/crawl](https://github.com/crawl/crawl)@[7de3fab2a5...](https://github.com/crawl/crawl/commit/7de3fab2a5de0563bd4a4e2709e7d426f2318379)
#### Saturday 2023-12-23 02:11:13 by regret-index

Tweak & distribute new skulls & acolytes across portals & vaults

Weeping skulls and burial acolytes are mostly put into the ossuaries with
minimal gimmicks and kill rate. Several ossuaries trim down the D:1 zombie
numbers and continue to pick up a small amount of fancier derived undead
(spectral scorpion, bullfrog simulacrum, croc zombie). This also gets in
some long-due nerfs for the wraith ossuaries and the bog mummy ossuary's
pile of bee / wyvern zombies- both are gone now that ossuaries in general
have less spiky gimmicks.

(This comes with a large amount of reshaping and handling Ossuaries in
general, to be honest. They have pretty awful disparaties in their kill
ratios even with quick crocodile zombie adjustments- the bottom 4/20
Ossuaries had a collective weighted killratio of 5% and the top 4/20 had a
collective killratio of 45%. Several also had some immensely troublesome
gimmicks- _due_cavern's skull traps never worked but thousands of people
autoexplored into wraiths, while _zaba_flooded was content to use wyvern
zombies in the same portal mostly using D:1 zombies. There's been some
heavy reworking of layouts from disproportionate killratio ends, including
some heavy reshaping and gimmick distribution. There's now a ~44% chance
to encounter either of the new monsters in an Ossuary, with functional
layouts like the bog mummy, scorpion, and ambush ones leaving them out.)

Weeping skulls and burial acolytes also show up in a few altar vaults for
Yred and Kiku, respectively, and a few Crypt vaults. Weeping skulls also
get a little Abyss integration, and could easily get more.

(After testing in their intended ossuary locations, weeping skulls are
a bit bulkier than their starting commit, while Malign Offering has been
tweaked further downwards in starting power for burial acolytes.
Laughing skulls also now show their possible maximum damage.)

---
## [crawl/crawl](https://github.com/crawl/crawl)@[22ebceef79...](https://github.com/crawl/crawl/commit/22ebceef7955bb6d5d1940bc1e960daeb1053361)
#### Saturday 2023-12-23 02:11:13 by regret-index

Monster revision: Flying skulls -> Laughing skulls

Flying skulls are extremely harmless for their current placement, being
mostly just monsters that shout for silent zombies to wake up to rather
than anything of actual interest in-and-of-themselves otherwise. They're
not very useful enemies to actually fight beyond very earlygame, yet
used mostly in late undead vaults or Crypt, a notion we've tried to
rather phase out these days compared to previously.

The newly renamed laughing skulls (so named contrast against the new
weeping skulls), have lost most of their resists beyond rF+ (many other
undead lack for it, but several vaults kind of want a vague fiery
undead theme available, and since they're now red to contrast agains old
flying skull white / cyan). They also have an rN-checking mechanic, but are
far more direct about it. They now cast 3d13 Bolt of Draining, and scale up
the power of their bolt with each skull available in their LoS- 25% for
each other laughing skull laughing with them, capped at 100%. While there's
a few piercing-bolt band designs in Crawl already (hell hounds, raiju, kind
of spark wasps, and hell knights), few of them are quite so slanted in both
raw damage and health frailty as these are- with five total present, each
hits as hard as shadow dragons, but they'll die very quickly when hit.
This should make them have an interesting bias against melee fighters
(after all the other repositioning and mp-draining effects added this
version). Or they'll get zapped by wands. It's at least better off than
before, and might make rN a bit more respectable a resistance.

Since they now have a built-in scaling mechanic, they now replace shadow
wraiths in the D out-of-depth pool appearing with only a single other skull
(and not even that when pulled up solitary in vaults), and are reduced in
number rather than cut out of many earlier vaults. They otherwise still
appear in their bands in Crypt and Abyss, though the latter has been made
to raise over time rather than lower. Several vaults have had their flying
skull counts nerfed, while other vaults have swapped them in for weeping
skulls.

The new tile is by Sastreii.

---
## [five-sh/git](https://github.com/five-sh/git)@[a1fbe26a0c...](https://github.com/five-sh/git/commit/a1fbe26a0c2bb8ba84c3976023e4ded4cf94608e)
#### Saturday 2023-12-23 02:16:23 by Elijah Newren

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
## [y2k04/y2k04.github.io](https://github.com/y2k04/y2k04.github.io)@[214fe86714...](https://github.com/y2k04/y2k04.github.io/commit/214fe86714276639d7edf6b3ca04e71fbbdf37c8)
#### Saturday 2023-12-23 02:26:45 by Y2K4

Upload new website

It's about damn time, holy shit!

---
## [Dirstac/mame](https://github.com/Dirstac/mame)@[52ecd995e7...](https://github.com/Dirstac/mame/commit/52ecd995e7baab82cf219c9d7c40eca327a8f9e2)
#### Saturday 2023-12-23 04:08:00 by wilbertpol

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
## [crawl/crawl](https://github.com/crawl/crawl)@[f52a5a9ab3...](https://github.com/crawl/crawl/commit/f52a5a9ab32a6c4b1f43a0e6568a79c59a131256)
#### Saturday 2023-12-23 04:17:45 by regret-index

Adjust new skull noise

While most full-bodied undead are still effected by silence, curse skulls
and wraithly monsters use magical or natural abilities. With that rough
precedence, it makes reasonable sense for both weeping skulls and laughing
skulls to be immune to silence. New messages have also been added for both,
alongside messages for ones blasting at allies from offscreen.

(This also fixes the mon-spell.lua test failing, as apparently SPELL_NOISY
is a tag for non-wizardly / priestly abilities. They should be noiser,
anyway- I wonder a little about S_SCREAM and its piercing shrieks actually
being louder than normal, considering the many years it seemed like that
was the case as well as it making obvious sense. (It was just notable when
Crypt was mostly zombies that they shouted at all.) It'd make demonic
crawlers louder in a relatively quiet branch, though, so I'll defer to
others' opinions on that front.)

---
## [ysdev/zola](https://github.com/ysdev/zola)@[22dc32a589...](https://github.com/ysdev/zola/commit/22dc32a5893deac5e91d173d0daf59e1868065ef)
#### Saturday 2023-12-23 04:54:52 by sinofp

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
## [linancn/langchain](https://github.com/linancn/langchain)@[d4f45b1421...](https://github.com/linancn/langchain/commit/d4f45b1421ec8b56fe6aeed84f81ca1b3f91383f)
#### Saturday 2023-12-23 05:25:23 by Sypherd

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
## [VegavitaCBDGummies/Vegavita-CBD-Gummies](https://github.com/VegavitaCBDGummies/Vegavita-CBD-Gummies)@[a1b38f2edd...](https://github.com/VegavitaCBDGummies/Vegavita-CBD-Gummies/commit/a1b38f2eddf040093b5104d45c4ae29c8e672300)
#### Saturday 2023-12-23 06:01:13 by VegavitaCBDGummies

Update README.md

Mental health is creating chaos all around the world. Thankfully, people are noticing this issue and giving importance to it. This is the reason why demand for VigorVita CBD Gummies has increased rapidly. Now, people know that long-term stress and anxiety are not normal and that they need to be treated at the right time. Some people ignore it, and with leading days they start suffering from high blood pressure, schizophrenia, cardiovascular health issues, diabetes, and even scientific research has proven that one of the major reasons for cancer is stress and pressure that a person cannot handle, but the person has been suffering from that stress and pressure for a long time. If you remain stress-free, then only you can be productive or enjoy your life.

---
## [prenaux/cppfront](https://github.com/prenaux/cppfront)@[cdf71bdca6...](https://github.com/prenaux/cppfront/commit/cdf71bdca64536a005f2491d8c19f1d05a1c62f6)
#### Saturday 2023-12-23 06:18:45 by Herb Sutter

Correct copy/move for `union`

By writing separate construction and assignment, plus the new feature of suppressing assignment to a member by writing `member = _ ;` (now allowed only in assignment operators).

I do realize that's an "opt-out" which I normally prefer to avoid, but:

- I considered and decided against (for now) the alternative of not having assignment be memberwise by default. I want to keep the (new to Cpp2) default of memberwise semantics for assignment as with construction. I think that's a useful feature, and normally if you do assign to a member it doesn't arise, and so I think it makes sense to explicitly call out when we're choosing not to do any assignment at all to a member before doing other assignment processing. We'll get experience with how it goes.

- `_` is arguably natural here, since it's pronounced "don't care." There too, we'll see if that is natural generalized, or feels strained. For now it feels natural to me.

---
## [ubccsss/ubccsss.org](https://github.com/ubccsss/ubccsss.org)@[4178b63699...](https://github.com/ubccsss/ubccsss.org/commit/4178b63699dd9e658e2a62eaf28e00fc8dcb0a58)
#### Saturday 2023-12-23 08:55:00 by csssbot

New review for CPSC 313 by Will (#566)

> It was not an easy course, but it is 100% doable for CPSC students.
It's pretty heavy (should be worth 4 credits really); assignments pretty
much every week plus multiple quizzes on top. Assignments were not too
hard in my opinion, it's just that it took some time to think carefully
and thoroughly. I spent a good chunk of my evenings attending office
hours to truly understand the materials. Nonetheless, Steve and Norm
were superb, the TAs were fabulous, and I think this is the most
well-designed CPSC course. You can mess up a quiz or two, and even the
midterm, and not be too worried about it, because weights are evenly
spread out.
>
> Difficulty: 4/5
> Quality: 5/5
> <cite><a href=''>Will</a>, Dec 23 2023, course taken during
2023W1</cite>
<details><summary>View YAML for new review</summary>
<pre>
  - author: Will
    authorLink: 
    date: 2023-12-23
    review: |
It was not an easy course, but it is 100% doable for CPSC students. It's
pretty heavy (should be worth 4 credits really); assignments pretty much
every week plus multiple quizzes on top. Assignments were not too hard
in my opinion, it's just that it took some time to think carefully and
thoroughly. I spent a good chunk of my evenings attending office hours
to truly understand the materials. Nonetheless, Steve and Norm were
superb, the TAs were fabulous, and I think this is the most
well-designed CPSC course. You can mess up a quiz or two, and even the
midterm, and not be too worried about it, because weights are evenly
spread out.
    difficulty: 4
    quality: 5
    sessionTaken: 2023W1

<pre>
</details>This is an auto-generated PR made using:
https://github.com/ubccsss/course-review-worker

---
## [OnlyFor/openai-evals](https://github.com/OnlyFor/openai-evals)@[f20c305dc7...](https://github.com/OnlyFor/openai-evals/commit/f20c305dc743eb545a57fd19b3b59426b9171465)
#### Saturday 2023-12-23 09:13:43 by Erik Ritter

Add MMMU evals and runner (#1442)

## Eval details 📑

### Eval name

MMMU

### Eval description
A multi-modal version of MMLU published here:
https://arxiv.org/pdf/2311.16502.pdf

### What makes this a useful eval?
Tests a variety of subjects, along with image recognition and
comprehension

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

Multimodal, covers many subjects 

## Eval structure 🏗️

Your eval should

- [x] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

### Eval JSON data

Dataset defined here: https://huggingface.co/datasets/MMMU/MMMU

### Eval Results

on `gpt-4-vision-preview`:

```
{
  "mmmu-accounting": 0.5333333333333333,
  "mmmu-agriculture": 0.6333333333333333,
  "mmmu-architecture-and-engineering": 0.16666666666666666,
  "mmmu-art": 0.7333333333333333,
  "mmmu-art-theory": 0.8333333333333334,
  "mmmu-basic-medical-science": 0.6,
  "mmmu-biology": 0.43333333333333335,
  "mmmu-chemistry": 0.43333333333333335,
  "mmmu-clinical-medicine": 0.6333333333333333,
  "mmmu-computer-science": 0.6333333333333333,
  "mmmu-design": 0.7666666666666667,
  "mmmu-diagnostics-and-laboratory-medicine": 0.3,
  "mmmu-economics": 0.6333333333333333,
  "mmmu-electronics": 0.4,
  "mmmu-energy-and-power": 0.36666666666666664,
  "mmmu-finance": 0.43333333333333335,
  "mmmu-geography": 0.4,
  "mmmu-history": 0.6666666666666666,
  "mmmu-literature": 0.9,
  "mmmu-manage": 0.6,
  "mmmu-marketing": 0.6333333333333333,
  "mmmu-materials": 0.26666666666666666,
  "mmmu-math": 0.5,
  "mmmu-mechanical-engineering": 0.23333333333333334,
  "mmmu-music": 0.36666666666666664,
  "mmmu-pharmacy": 0.7666666666666667,
  "mmmu-physics": 0.43333333333333335,
  "mmmu-psychology": 0.7,
  "mmmu-public-health": 0.8,
  "mmmu-sociology": 0.5666666666666667
}
Average accuracy: 0.5455555555555556
```

Note that this is slightly lower than the MMMU paper's findings of
`0.568`. There's likely prompt engineering that could be done to improve
this, but I'll leave that as an exercise for later

---
## [ls1955/hausaufgaben](https://github.com/ls1955/hausaufgaben)@[42e8e485e5...](https://github.com/ls1955/hausaufgaben/commit/42e8e485e519f6440616b91ad98fb1d701c5f822)
#### Saturday 2023-12-23 09:37:10 by Cheong

Include more util function

This commit:
* Include organizeDownloadFolder function
* Include checkScopedStoragePermissions function
* Include requestScopedStoragePermission function

Although author usually write spaghetti, a spaghetti of this amount is
rare, even for him. ...guess he won't sleep soundly tonight, not that he
had been sleeping without worry, ever since he taste a little bit of raw
life.

...well, as he need some good news right now, if all these functions
didn't blow up, another core functionality of app will soon be finish.

---
## [jaehoonhwang/aoc2023](https://github.com/jaehoonhwang/aoc2023)@[4ee71703fb...](https://github.com/jaehoonhwang/aoc2023/commit/4ee71703fb93058fb768580b321014a9f8b1505f)
#### Saturday 2023-12-23 09:39:21 by Jaehoon Hwang

solve(day4): I f-ing hate split.

Apparently, split needs to be regex'd if you want consistent behavior
across the language. Using ` ` instead of `\s+` for regex, caused
typescript to render something `  1` into undefined or something else of
different size of an array that is unexpected.

Feels like this behavior should be fixed or at least notified by the
program, but apparently, this is all pipe-dream.

Honestly, should not have taken this longer, but it took me about
45minutes due to debugging >:(

I hate `splits`, just split by the white space :'(

Other than snafu with whitespaces in `split()`, it was a fun puzzle.

---
## [Vallat/tgstation](https://github.com/Vallat/tgstation)@[8d77b1be89...](https://github.com/Vallat/tgstation/commit/8d77b1be89f771391c5697a1a3ac180f68cd6858)
#### Saturday 2023-12-23 09:39:59 by necromanceranne

Balance changes to swords, energy shields and modsuit shields. (#80072)

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

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [Vallat/tgstation](https://github.com/Vallat/tgstation)@[54ab1e3936...](https://github.com/Vallat/tgstation/commit/54ab1e3936b3d5a301b995f2c1ca14fcdaf3e80d)
#### Saturday 2023-12-23 09:39:59 by Time-Green

Organ movement refactor *Un-nullspaces your organs* (#79687)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

closes #53931, #70916, #53931

## About The Pull Request

Organs were previously stored in nullspace. Now they are stored in their
prospective bodyparts. Bodyparts are now stored in the mob.

I've also had to refactor a lot of code concerning organ movement.
Previously, organs were only moved into bodyparts once the bodyparts
were removed. To accomodate this change, two major distinctions have
been made:

**Bodypart removal/insertion**
Called only when an organ is taken out of a bodypart. Bodypart overlays,
damage modifiers or other changes that should affect a bodypart itself
goes here.

**Mob insertion/removal**
Called when an organ is removed from a mob. This can either be directly,
by taking the organ out of a mob, or by removing the bodypart that
contains the organ. This lets you add and remove organ effects safely
without having to worry about the bodypart.

Now that we controle the movement of bodyparts and organs, we can fuck
around with them more. Summoning someones head or chest or heart will
actually kill them now (and quite violently I must say (chest summoning
gibs lol)).


https://github.com/tgstation/tgstation/assets/7501474/5efc9dd3-cfd5-4ce4-b70f-d0d74894626e

I´ve also added a unit test that violently tears apart and reconstructs
a person in different ways to see if they get put toghether the right
way

This will definitely need a testmerge. I've done a lot of testing to
make sure interactions work, but more niche stuff or my own incompetence
can always slip through.

## Why It's Good For The Game

<!-- Argue for the merits of your changes and how they benefit the game,
especially if they are controversial and/or far reaching. If you can't
actually explain WHY what you are doing will improve the game, then it
probably isn't good for the game in the first place. -->

A lot of organ work is quite restricted. You can't C4 someones heart,
you cant summon their organs and a lot of exceptions have to be made to
keep organs in nullspace. This lets organs (and bodyparts) play more
nicely with the rest of the game. This also makes it a lot easier to
move away from extorgans since a lot of their unique movement code has
been removed and or generalized.

I don't like making PRs of this size (I'm so sorry reviewers), but I was
in a unique position to replace the entire system in a way I couldn't
have done conveniently in multiple PRs

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
refactor: Your organs are now inside your body. Please report any issues
with bodypart and organ movement, including exotic organ, on github and
scream at me
fix: Cases of unexpected organ movement, such as teleporting bodyparts
and organs with spells, now invokes a proper reaction (usually violent
death)
runtime: Fixes HARS runtiming on activation/deactivation
fix: Fixes lag when species swapping
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Vallat/tgstation](https://github.com/Vallat/tgstation)@[16bdcf409c...](https://github.com/Vallat/tgstation/commit/16bdcf409c5d6eb3d846b16f4968849e26cf833c)
#### Saturday 2023-12-23 09:39:59 by Rhials

"Security Implant" rework, prisoner management console updates (#79882)

## About The Pull Request

For the vernacular purposes of the following PR body -- "Security
Implant" refers to the existing subset of implants given, by security,
to captured prisoners and such as a punitive, controlling measure. This
includes the chemical, tracking, and maybe exile implants.

This revamps the functionality of how "security" implants are displayed
on huds, prisoner management console implant controls/readouts, and
their instrumentality. It was also, ultimately, an attempt at nerfing
the tracking implant that spiralled far out of control.

Rather than only displaying chemical on the right and tracking on the
left, all implants with the "security implant" flag will be trackable on
SecHuds. A maximum of two can be implanted at once. This is both due to
technical limitations, but also conveniently provides security a limit
to consider when choosing implants.

Implants now also occupy their HUD slot based on the order they were
implanted in, rather than always occupying the same spot. Neat!


![image](https://github.com/tgstation/tgstation/assets/28870487/68b17dbb-cda4-4c3b-96d4-b3bbcf49b80e)

From two (three if you count the exile implant), there are now five
security implants. _The tracker implant has been split into two of these
implants._

<details>
<summary>Summary of the implants, functions, changes:</summary>
<br>

- **Tracker (Red)** -- No longer grants teleporter beacon. Tracking
radius has been increased from 20 to 35 tiles. The Prisoner Management
Console will now list the area the prisoner is occupying as well.
Disables after the implantee is dead for 10 minutes.
- **Chemical (Blue)** -- No mechanical changes. The implant pad readout
has been modified slightly.
- **Exile (Green)** -- In addition to past functionality, station
shuttle controls (public, mining, etc.) will be unresponsive for the
implantee. Flimsy, but more effective than a stern warning not to come
back from lavaland.
- **Beacon (Yellow)** -- Implantee becomes a teleporter beacon. The
prisoner console will report if their currently occupied area is
hazardous or not, so half of the security team doesn't blindly teleport
into space or lava. Disables after the implantee is dead for 10 minutes.
Available from Cargo.
- **Teleport Blocker (Deep Blue, not shown)** -- Prevents the implantee
from being teleported. Ever wanted to keep a wizard or cultist in a
cell? This is where you can start. Available from Cargo, expensive and
scarce.

Each of the implants has some application that would benefit security if
used on a captured criminal. Their usefulness may overlap in some
places, but the overall range of control these implants give security is
broadened.

</details>

The implant control console has also been given a small facelift.
Certain implants provide more useful readouts that can help officers
locate, control, or capture an implantee, rewarding cooperation between
officers.

It has also been totally converted into TGUI by @MrMelbert. Kickass!

Also, You can now remotely destroy implants, either to relieve criminals
from their punishment or to make room for a different implant. Wardens
should keep hold of their ID and remember to log out, since a motivated
convict could use it to shed their implants!


![tgui](https://github.com/tgstation/tgstation/assets/28870487/3c2ae99f-9c1d-4b18-b4cb-942cc96bcafe)

Everything made in this PR _should_ be scaleable enough to allow for new
security implant types to be implemented with relative ease. The
teleport-blocker implant was a last minute attempt to prove it to
myself. I had a few more ideas for implants in my head, but figured this
PR was already getting big and ugly enough. That is all for another day.

I truly apologize if there's anything I've missed in here. I did a lot
of this over a long period of time and kind of just... sat on it for a
while. If there's any confusing our unexplained changes, feel free to
point them out and I'll try to give an explanation.
## Why It's Good For The Game

The goal of this PR is to give a bit more depth to security's armory
implants. The intent is to present a choice in what implants are given
(rather than just tracker and maybe chem if you're feeling spiteful),
and to make them more useful as punitive/monitoring tools.

The tracker implant needed a nerf (and probably still does regardless of
this PR's success). It's never used for tracking since the teleporter
beacon is much more direct (+ gives a virtually free attack
opportunity), and the tracking range was incredibly subpar. I'd rather
not take toys away from security, but having the best option not be
roundstart gear feels like a fair compromise.

Warden content. Wardens have more gear to budget for and use at their
own (or the HOSes) discretion. The changes to the prisoner console allow
them to coordinate with officers to get good value out of the implants
they've chosen for an implantee.

Gives antagonists an alternate way to get de-implanted, without external
help, that can only be granted at the fault of security. Wardens who
dish out implants must keep an eye on the people carrying them!
## Changelog
:cl: Rhials, MrMelbert
add: The Tracker implant has had its teleport beacon functionality
migrated to the new (cargo accessible) Beacon implant.
add: Teleport Blocker security implant, that prevents the implantee from
teleporting by any means. Purchasable from cargo.
add: Security implants may now be harmlessly self-destructed at the
Prisoner Management Console.
balance: The Tracker implant tracking radius has increased from 20 to 35
tiles. The Prisoner Management Console will track and display the area
the implantee is in as well.
balance: The exile implant now prevents implantees from operating
shuttle controls.
code: Various code improvements and removal of unused vars in the
Prisoner Management Console
code: The HUD slots for chem/tracking implants have been converted to
display any implant with the IMPLANT_TYPE_SECURITY flag and an
associated sprite.
spellcheck: Modifies various implant pad readouts, removing false
information and rewriting some sections.
/:cl:

---------

Co-authored-by: MrMelbert <kmelbert4@gmail.com>
Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [Vallat/tgstation](https://github.com/Vallat/tgstation)@[edbc7c5622...](https://github.com/Vallat/tgstation/commit/edbc7c562261e95d58140463ed6a1a23102fc2f3)
#### Saturday 2023-12-23 09:39:59 by John Willard

PDA update (Messenger works while dead, Microwave works, etc). (#80069)

## About The Pull Request

This is an update that touches many more things all at once (compared to
my other PRs) meant to make PDAs in general feel more consistent and not
take away from one of the experiences we want to encourage: interaction
between players.

1. Replaced all checks of a 'pda' with a 'modular pc'. This means
technically (though not done in-game currently) other modpcs can hold an
uplink, and microwaves can charge laptops.
2. Speaking of microwave, they now don't break and require
deconstruction if the cell is removed mid-charge.
3. When a Mod PC is out of power, it will now allow the Messenger to
work (which now also doesn't consume any additional power), if the app
exists on the PC. Here's a video demonstration


https://github.com/tgstation/tgstation/assets/53777086/7ae12f81-a271-49b8-95fa-2ba54d2e2d1f

4. Flashlights can't be turned on while the cell is dead
5. I replaced a bunch of program vars with ``program_flags`` and renamed
``usage_flags`` to ``can_run_on_flags``.
6. Added a debug modPC that has every app installed by default. Mafia
had some issues in the past that were unknown because Mafia wasn't
preinstalled with any tablet so was never in create & destroy nor in any
other unit test. This was just an easy solution I had, but PDAs should
get more in-depth unit tests in the future for running apps n stuff- I
just wanted to make sure no other apps were broken/harddeling.

## Why It's Good For The Game

Currently when a PDA dies, its only use is to reply to PDA messages sent
to you, since you can still reply to them. Instead of just fixing it and
telling players to cope, I thought it would be nice to allow PDA
Messenger to still work, as it is a vital app.
You can call it some emergency power mode or whatever, I don't really
mind the reason behind why it is this way.

When I made cells used more on PDAs, my main goal was to encourage
upgrading your PDA and/or limiting how many apps you use at once, I did
not want this to hit on players who use it as a form of interaction.
This is the best of both worlds, I think.

The rest of the changes is just for modularity, if some downstream wants
to add tablets, phone computers, or whatever the hell else, they can
still get just as far as PDAs should be able to get to, hopefully.

## Changelog

:cl:
add: PDAs with a dead power cell are now limited to using their
Messenger app.
fix: Microwaves now stop charging PDAs if the cell was removed
mid-charge.
fix: Microwaves can now charge laptops.
fix: PDA Flashlights can't be turned on while the PDA is dead.
fix: You can now hold a laptop up to a camera (if it has a notekeeper
app installed) like PDAs already could.
/:cl:

---------

Co-authored-by: lessthanthree <83487515+lessthnthree@users.noreply.github.com>

---
## [Hakase-Hamdani/HamdaniVis3Tgs](https://github.com/Hakase-Hamdani/HamdaniVis3Tgs)@[78fd983c57...](https://github.com/Hakase-Hamdani/HamdaniVis3Tgs/commit/78fd983c573adadbcfc9b03300329d8b531ccc34)
#### Saturday 2023-12-23 10:33:46 by Hakase-Hamdani

I SWEAR TO GOD IM NOT INFLATING THE COMMIT COUNT

my stupid ass doesn't know how to resolve whatever conflict that was before i just brute force my way to revert

---
## [ChakatStormCloud/Bubberstation](https://github.com/ChakatStormCloud/Bubberstation)@[85ee756c24...](https://github.com/ChakatStormCloud/Bubberstation/commit/85ee756c24905736dac9c468ad25f3cf626d4a55)
#### Saturday 2023-12-23 11:26:46 by SkyratBot

[MIRROR] [CI Fix] The Demonic Frost-Miner will not attack corpses. [MDB IGNORE] (#24615)

* [CI Fix] The Demonic Frost-Miner will not attack corpses. (#79294)

## About The Pull Request

Fixes #79147.

Prevents the Demonic Frost-Miner from shooting at corpses by returning
early from `OpenFire()`. Also adds the "gutted" status effect to the
corpses in its arena so it won't try to gut them.
## Why It's Good For The Game

#78826 introduced an unfortunate bug by placing corpses in the Frost
Miner's arena. There were a combination of three factors at play here:
that the Miner attacks corpses, that it happens to use colossus bolts in
its attacks, which dust corpses, and that some unfortunate quirk of life
code causes runtimes if, as far as I can tell, a life tick goes off when
a mob is at the wrong point in the dusting process. The time this
process takes happened to perfectly coincide with the Monkey Business
unit test (being the first test that takes a significant period of
time), causing it to randomly fail.

So, this fixes a flaky test that has been a pain in the ass for the last
five days, is the big thing.

Also, it can't possibly have been intended for the Miner to run around
obliterating the aesthetic corpses in its arena within the first 15
seconds of any given round. Completely ruining the mood!

I'll point out that this particular boss may have been forgotten in
#77731, which set out to make only the colossus still gib/dust you, but
even were that not the case I think it would be a bit silly for the
Miner to be busy shooting lifeless corpses when a player shows up to
challenge it, rather than standing in its scary ritual circle.
## Changelog
:cl:
fix: The Demonic Frost-Miner will no longer run around destroying the
corpses in its arena the moment the round begins.
/:cl:

* [CI Fix] The Demonic Frost-Miner will not attack corpses.

---------

Co-authored-by: lizardqueenlexi <105025397+lizardqueenlexi@users.noreply.github.com>

---
## [syswu/runc](https://github.com/syswu/runc)@[8e8b136c49...](https://github.com/syswu/runc/commit/8e8b136c4923ac33567c4cb775c6c8a17749fd02)
#### Saturday 2023-12-23 11:42:41 by Aleksa Sarai

tree-wide: use /proc/thread-self for thread-local state

With the idmap work, we will have a tainted Go thread in our
thread-group that has a different mount namespace to the other threads.
It seems that (due to some bad luck) the Go scheduler tends to make this
thread the thread-group leader in our tests, which results in very
baffling failures where /proc/self/mountinfo produces gibberish results.

In order to avoid this, switch to using /proc/thread-self for everything
that is thread-local. This primarily includes switching all file
descriptor paths (CLONE_FS), all of the places that check the current
cgroup (technically we never will run a single runc thread in a separate
cgroup, but better to be safe than sorry), and the aforementioned
mountinfo code. We don't need to do anything for the following because
the results we need aren't thread-local:

 * Checks that certain namespaces are supported by stat(2)ing
   /proc/self/ns/...

 * /proc/self/exe and /proc/self/cmdline are not thread-local.

 * While threads can be in different cgroups, we do not do this for the
   runc binary (or libcontainer) and thus we do not need to switch to
   the thread-local version of /proc/self/cgroups.

 * All of the CLONE_NEWUSER files are not thread-local because you
   cannot set the usernamespace of a single thread (setns(CLONE_NEWUSER)
   is blocked for multi-threaded programs).

Note that we have to use runtime.LockOSThread when we have an open
handle to a tid-specific procfs file that we are operating on multiple
times. Go can reschedule us such that we are running on a different
thread and then kill the original thread (causing -ENOENT or similarly
confusing errors). This is not strictly necessary for most usages of
/proc/thread-self (such as using /proc/thread-self/fd/$n directly) since
only operating on the actual inodes associated with the tid requires
this locking, but because of the pre-3.17 fallback for CentOS, we have
to do this in most cases.

In addition, CentOS's kernel is too old for /proc/thread-self, which
requires us to emulate it -- however in rootfs_linux.go, we are in the
container pid namespace but /proc is the host's procfs. This leads to
the incredibly frustrating situation where there is no way (on pre-4.1
Linux) to figure out which /proc/self/task/... entry refers to the
current tid. We can just use /proc/self in this case.

Yes this is all pretty ugly. I also wish it wasn't necessary.

Signed-off-by: Aleksa Sarai <cyphar@cyphar.com>

---
## [crowlogic/arb4j](https://github.com/crowlogic/arb4j)@[9e860bea73...](https://github.com/crowlogic/arb4j/commit/9e860bea73bef66c0f2177074a6d5cdfcae9c0b4)
#### Saturday 2023-12-23 12:19:06 by Stephen A. Crowley

first pass at a fucking quaternionion class,
godallmotherfuckinggoddamnmightiwanttofuckingdestoryopenaisfuckingshitspewingglorifiedmarkovchainwhatabunchofbumblefuckdogfoodeatingsonsofbitchestheyare

---
## [cuberound/cmss13](https://github.com/cuberound/cmss13)@[55f9dd8d39...](https://github.com/cuberound/cmss13/commit/55f9dd8d39bcdd3a1e6c8c72f128c6f4447111dc)
#### Saturday 2023-12-23 12:59:58 by fira

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
## [Amerecanno/CoffeStation](https://github.com/Amerecanno/CoffeStation)@[762705eff9...](https://github.com/Amerecanno/CoffeStation/commit/762705eff975e6acaed923eb24d1225bc50f9978)
#### Saturday 2023-12-23 14:10:26 by CDB

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
## [HeresKozmos/cmss13](https://github.com/HeresKozmos/cmss13)@[e7816d96c5...](https://github.com/HeresKozmos/cmss13/commit/e7816d96c5d1523337dec081bea0056fbc9189fc)
#### Saturday 2023-12-23 14:19:24 by forest2001

Almayer AntiTheft measures. (#5100)

STOP STEALING SHIT
# About the pull request
Adds a subtype of reinforced hull for the Almayer that changes between
indestructible hull and normal reinforced wall after hijack.
Uses this wall type around uniform vendors, the separation wall in the
firing range and around engineering storage.
<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game
Having the engineering storage looted at round start is just silly
avoidance of the "don't deconstruct the whole ship without a reason"
rule.

# Testing Photographs and Procedure

I have verified that all works as intended, the walls cannot be harmed
prior to hijack, and shutters function as advertised.

# Changelog
:cl:
add: Added a new almayer hull type (heavy reinforced) which is
indestructible by normal means until after hijack collision.
add: Added a new subtype of shutter that automatically opens or closes
depending on security level.
maptweak: Maps both of the above around the engineering storeroom. Also
adds the walls between the firing ranges and around uniform vendors.
maptweak: Manual control button for shutters over engineering storage in
the CEs office.
code: Changes hijack structural changes (walls/windows/windoors/ladders)
to use signals.
/:cl:

---------

Co-authored-by: fira <loyauflorian@gmail.com>

---
## [Jawnner/f13babylon](https://github.com/Jawnner/f13babylon)@[3c052bcd6d...](https://github.com/Jawnner/f13babylon/commit/3c052bcd6d3ff02680c3fe1f15151549154eb162)
#### Saturday 2023-12-23 14:40:03 by Mazzinsanity

Main Fallout13 Medicine Rework (#113)

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
This PR aims to bring a number of changes to the way the main Fallout13
medicines function.

Stims remain the vanilla videogame healing item they were, stronger than
tribal medicine at healing brute and burn damage, but lacking in
specialization. On the other hand, tribal medicine has been given a new
breath of life in the form of excelling in certain damage types and
increased healing from wounds.

Activation delays for certain healing items have been changed:
- Hydra/Med-X/Psycho/Turbo - 1 second on yourself / 3 seconds on others
- All forms of gauze/sutures/mesh/ointment - 3 seconds for yourself / 1
second on others

Using the stimpak as a base, here are the healing rates for brute/burn
healing for the healing items:
1. Super stimpak - 225% of base stimpak strength
2. Imitation super stimpak - 188% of base stimpak strength (75% of super
stimpak strength)
3. Bitter drink -180% of base stimpak strength for tribals / 133% for
non-tribals
4. Healing poultice - 115% of base stimpak strength for tribals / 87.5%
for non-tribals
5. Imitation stimpak - 75% of base stimpak strength
6. Healing powder - 75% of base stimpak strength for tribals / 55% for
non-tribals

All medicine now heals burn damage at 75% of its healing power for brute
damage.

Powder/poultice/bitters/hydra will not heal when any stimpak fluid
variant is in the system. Stimpak fluid will not heal when
powder/poultice/bitters are the system.

Only one medicine is able to heal at a time. This medicine must be the
weakest one currently in the system:
- For example, if super stim fluid is present in the body, and regular
stim fluid is introduced, then the super stim fluid will stop healing,
while the regular stim fluid heals.
- If imitation stim fluid is added, then regular stim fluid stops
healing, and only imitation stim fluid can heal.
- If at any point powder/poultice/bitters are added, no medicine will
heal.
- The same logic follows for powder/poultice/bitters.

All stimpaks have lost the ability to additionally heal bodyparts with
each wound applied to that bodypart. The logic behind this property has
been reworked and moved to tribal medicine.

All stimpaks have retained their ability to clot active pierce/slash
wounds, reducing their bleed rates.

All medicine has lost its crit stabilizing properties.

Bitter drink no longer heals radiation and has reduced toxin and oxyloss
healing rates.

Healing poultice now excels at healing radiation and toxin damage, as
strong as the super stimpak brute healing rate. Healing powder now
excels at healing oxyloss damage, as stong as the super stimpak brute
healing rate.

The overdose effects for all main healing medicines have had their
damage values tweaked and additional drawbacks added.

Using stims as Legion now causes serious side-effects, including
vomiting, confusion, dizzyness and jitteriness. Using
Med-X/Psycho/Buffout/Jet/Turbo as Legion/NCR/BoS/Enclave now also causes
these side-ffects. As such, Psycho and Turbo have been removed from
Enclave loadouts.

2 new negative quirks are now available for selection: Stim Intolerance
and Straight Edge:
- Stim Intolerance makes you vomit, causes dizziness, jitteriness and
confusion whenever any variant of stim fluid enters your body.
- Straight Edge makes you have the same effects but with Fallout chems
like Psycho/Med-X etc.

New positive quirk available for selection: Herbal Affinity:
- Grants bonus healing from tribal medicine and removes the negative
side-effects

Roles that start with these quirks already allocated to them
(NCR/Legion/BoS/Enclave) cannot select these quirks for free points.

Small miscellaneous tweaks and fixes, such as crafting time changes for
medicine, are present as well.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
The current roster of Fallout13 medicine is somewhat unbalanced and
needs a little love. This aims to do that by making superstims act as
vanilla jack-of-all-trades healing items, while making the tribal
medicines specialize in certain damage types to fill the gaps left by
their inability to use chem machines while also making them grow
stronger as the user gains more wounds, taking into account the low
wound armor and hit-and-run, all-or-nothing gameplay that Tribal and
Legion roles have.

The side-effects changes for Med-X/Psycho/Turbo/Buffout were made to
counteract powergaming and circumvent factions breaking their lore in
order to gain an upper hand in a fight.
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
add: Added side-effects for the 4 major factions upon Fallout chem use
add: Added side-effects for Legion upon stim use
add: Added 2 new negative quirks - Stim Intolerance and Straight Edge
tweak: Tweaked medicine crafting times
tweak: Tweaked time delays on medicine application
balance: Rebalanced the main Fallout13 healing chemicals
fix: Fixed incorrect poultice x50 batch crafting requirements
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: Yawet330 <65188584+Yawet330@users.noreply.github.com>

---
## [whistler420/CheesedUP-FMOD](https://github.com/whistler420/CheesedUP-FMOD)@[1410d6433c...](https://github.com/whistler420/CheesedUP-FMOD/commit/1410d6433c59ce09acc7cc7dc71b9984fdfd70b1)
#### Saturday 2023-12-23 14:53:42 by Laventory

A few things tweaked (Copied from final-order mostly)

- tweaked Pesto Anchovi's looping
- Added "shortcut" regions to the Lap 3 track for the Pizza Time events for when you use a Lap Checkpoint
- Snick Challenge and Snick Rematch now have their low-time music restored.
- Added a Pesto Anchovi event with just the full song looping, no extra bullshit
- Fixed loop on Pillar John's Revenge in pizzatimePN event

Unlike the other one I actually had to redo the normal pizzatime event because unlike final-order your pizzatime fucked up mix is actually in the event so i had to manually do that one lol

---
## [EmulatorJS/gambatte-libretro](https://github.com/EmulatorJS/gambatte-libretro)@[6aee06e9b2...](https://github.com/EmulatorJS/gambatte-libretro/commit/6aee06e9b23b4de7aa3bbe248ee521dfbd7b6836)
#### Saturday 2023-12-23 16:00:56 by Patrick Adams

Halloween Treat: 100 New Palettes! (#253)

* Super Saiyan Palette Update! + Context

Super Saiyan God, Super Saiyan Blue, Legendary Super Saiyan, Super Saiyan Rose, Super Saiyan, and Super Saiyan Blue Evolved have all received updates! I'll explain why so you can get the context on this update. On the Japanese website for Super Dragon Ball Heroes, I wanted to find the exact correct color shades of all the Super Saiyan transformations represented. Plus, Mastered Ultra Instinct is now called Perfected Ultra Instinct. Thank the Dragon Ball Wiki for that.

* TWB64 085 Name Update!

Goodbye, Mastered Ultra Instinct, hello, Perfected Ultra Instinct!

* Update gbcpalettes.h

* TWB64 140 - Dragon Ball Orange Updated!

No need for Shenron granting this update! Dragon Ball Orange has been updated!

* Super Saiyan Blue Evolved Updated Again!?

I had to look for the correct Super Saiyan

* All treats, no tricks; 100 new palettes! + Updated palettes!

Yes, I'm alive! I've still been working on Game Boy palettes all this time, even after I retired from Twitter thanks to the Muskrat. 100 new Game Boy palettes have been added to the Gambatte emulator. Plus, some have been updated/overhauled!

* 100 new palette names! + Changed palettes names in packs 1 and 2!

* TWB64 - Pack 3 Added! + Changed Names

Hey everyone! Sorry that it's been a while since I contributed to github, but I'm here with one big Halloween treat for the Gambatte emulator: a new pack with 100 new palettes! Plus, sme palette names in packs 1 and 2 have been changed.

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[8f3d1036c8...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/8f3d1036c8f4f7b51acc6bad8b28009a81e20ac4)
#### Saturday 2023-12-23 16:08:43 by SkyratBot

[MIRROR] Refactor icemoon wolves into basic mobs and add taming + pack behavior [MDB IGNORE] (#25126)

* Refactor icemoon wolves into basic mobs and add taming + pack behavior (#79736)

## About The Pull Request

Ports icemoon wolves over to the basic mob framework with a bit of extra
stuff:

- Wolves call for help when attacked within a decently large radius.
Because you know, pack animals.
- Wolves can now be tamed with a slab of meat
- When tamed, wolves can be ridden like goliath mounts. Ride wolf, life
good. Pretend you're playing ARK and start shivering to death in thatch
huts for that High Roleplay experience.
- Tamed wolves have access to a bunch of pet commands (following, point
fetching, point attacking, play dead, etc) and will also defend their
owners vehemently if they're attacked.

You can probably tame multiple if you wanted to.

## Why It's Good For The Game

What part about riding wolves isn't entertaining? I don't really play
/tg/ that much so I can't argue too much about the balance implications
this might pose, but it's undoubtedly a stupid little gimmick and is
likely to be used by bored assistants and miners with too much time on
their hands.

Especially robust individuals will probably find a million things to do
with a basic mob capable of fetching, attacking on command and generally
being able to defend themselves decently well.

## Changelog

:cl: yooriss
refactor: Icemoon wolves now use the basic mob framework and should act
more intelligently, defending their pack.
add: Icemoon wolves can be tamed with slabs of meat and can be ridden as
mounts once friendly. Being rather large dogs, they also have access to
most of the pet commands you'd expect, such as fetching things, and
violently mauling people their owners point at.
/:cl:

---------

Co-authored-by: san7890 <the@ san7890.com>

* Refactor icemoon wolves into basic mobs and add taming + pack behavior

---------

Co-authored-by: Ephemeralis <Ephemeralis@users.noreply.github.com>
Co-authored-by: san7890 <the@ san7890.com>

---
## [philomath213/UACME](https://github.com/philomath213/UACME)@[c65f9215c1...](https://github.com/philomath213/UACME/commit/c65f9215c1103269ca31f66f49869fcde547af98)
#### Saturday 2023-12-23 16:49:09 by hfiref0x

Update Naka.vcxproj

Retarget platform toolset for appveyor fail. I understand that this service is currently busy supporting %current thing% more than actually working on their script-shit, but holy fuck seriously.

---
## [mazzinsanity/f13babylon](https://github.com/mazzinsanity/f13babylon)@[fc41127084...](https://github.com/mazzinsanity/f13babylon/commit/fc41127084c96e75ed37c1e51c6ad9d2305da643)
#### Saturday 2023-12-23 16:58:37 by Stutternov

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
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[873a476ce0...](https://github.com/mrakgr/The-Spiral-Language/commit/873a476ce0d430b426ce6edf0fceae5edbd955a9)
#### Saturday 2023-12-23 17:12:46 by mrakgr

"https://stackoverflow.com/questions/46942001/sql-adding-numbers-while-handling-nulls

https://learnsql.com/blog/null-comparison-operators/

I am doing some studying SQL and I realized that I **** **** in the previous session. Also I had no idea that SQL used the ternary logic.

https://youtu.be/vWkfGv7dJzE
Working with SQL NULL values | Null Handling Functions

Let me watch this. It seems I have a lot to learn about SQL.

https://www.reddit.com/r/Trackballs/comments/18lzr2q/will_the_elecom_exg_get_smoother_after_some_use/
> A good option for handling this kind of mouse is to use the Step acceleration in RawAccel. That makes this mouse usable even with its crappy ball and bearings.

Yesterday I figured out how to make this mouse usable. The step acceleration in raw axle is very good. You can set a just right so that the jacket behavior of this crappy mouse isn't a burden.

Let me go back to watching the video. Then I'll fix my mistake in the repellent.

https://youtu.be/5K7x946qvgA
Independent vs Correlated Subquery | Advanced SQL Tutorial For Beginners

Let me watch this as well. I thought that I would be doing my own programming to day, but I guess this is how things will roll.

https://youtu.be/5K7x946qvgA?t=557

This is quite impressive. I like it.

Actually, this example tells me quite a lot about how subqueries work in SQL. It answers some of the questions that I've been wondering about.

> 99 percent of the time you can solve a problem using an independent query with a combination of cte and window functions.
> As the correlated sub queries are not so performance always try to avoid them.

https://youtu.be/uEmAvzuA7u8?t=3
SQL Order of Execution (Logical Explanation) | Namaste SQL | Ankit Bansal

Let's me watch this. I'm into it now. As a professional programmer, sql is definitely something I need to know.

4:05 PM. https://youtu.be/4Am_KLZ-tEQ?t=239
Writing SQL Subqueries in Having Clause | Essential SQL

So subqueries in having clauses aren't affected by the group by statement. It seems that the rule applies to sub queries in general.

I think I'm going to stick with this mouse for now until the trackpad arrives next week. The raw axel software actually makes that usable. I wanted to do some voice programming for my own project today, but it seems like it's an SQL studying day. I understand it thoughourly now.

6:00 PM.

```spiral
inl test1() =
    open deck
    open random_cuda
    inl grid_range () : int = $"gridDim.x * blockDim.x"
    inl linear_id () : int = $"threadIdx.x + blockIdx.x * blockDim.x"

    inl blocks = 1
    inl grids = 1 // divup (length out) blocks
    run grids blocks (fun () =>
        globals()
        inl from = linear_id()
        inl x : _ philox_state = init {seed=conv from; subsequence=0; offset=0}
        loop.forBy' {from nearTo=50; by=grid_range()} (fun i deck =>
            open sam
            inl ar : sa 7 card = create
            loop.for {from=0; nearTo=length ar} (fun i deck =>
                inl v, deck = draw_card x deck
                set ar i v
                deck
                ) deck_utils.create()
            |> ignore
            console.write_ln ar
            )
        )
```

Not bad. I finally got this test to work. Actually did some programming on my own project instead of being burried in SQL.

The Elecom mouse pretty much ruined my entire week. But I finally got it to work today. The RawAccel Software makes a huge difference. I set a tab so that a small movements of 5 milliseconds are 3rd of the speed of the larger ones using the Jump acceleration mode. That's finally made using it variable and I actually think that instead of returning it, I'm going to keep it as it's more usable than the can Kensington Expert mouse now. I think it's actually a bit smoother than it was at the start of the day.

I left a really nasty review on Amazon on it, but it deserves it.

6:10 PM. Tomorrow morning, I'll be busy, so I'll close it here for today, instead of doing the other test. Right now, I'm still recovering, and I'm having a vacation, so I'm not going to do too much. When my hand recovers, that is when I am really going to dig into it."

---
## [russmckendrick/blog](https://github.com/russmckendrick/blog)@[ec9e148135...](https://github.com/russmckendrick/blog/commit/ec9e148135af4d17c135aee0bfe5e119654e25f4)
#### Saturday 2023-12-23 17:20:30 by Russ McKendrick

📝 docs(cover.png): add cover image for the "2023 Top 10" blog post

📝 feat(posts): add new post "2023 Top 10"

This commit adds a new post titled "2023 Top 10" to the content/posts directory. The post showcases a list of the top 10 albums of 2023, highlighting their unique perspectives and sounds. The post includes descriptions of each album, along with links to reviews for further details. The purpose of this commit is to provide readers with a curated list of notable albums from 2023 and to promote discussion and appreciation of the music released during that year.

🎵 feat(albums): add descriptions for "Ziggy Stardub - Easy Star All-Stars", "Everything Is Alive - Slowdive", "The Harmony Codex - Steven Wilson", "Brothers & Sisters - Steve Mason", "The Endless Coloured Ways (The Songs Of Nick Drake) - Various", "Sky Void Of Stars - Katatonia", and "ID.Entity - Riverside" albums

🎵 feat(albums): add information about recent music releases

This commit adds information about several recent music releases. It includes details about the albums "ID.Entity" by Riverside, "The Girl Is Crying In Her Latte" by Sparks, "Simplicity" by Matt Berry, "Prism" by The Orb, "Version Girl" by Rhoda Dakar, and "Joy'All" by Jenny Lewis. Each album is described, highlighting its unique qualities, musical styles, and critical reception. Additionally, links to detailed reviews and insights are provided for further exploration.

ℹ️ For more information, please refer to the provided links.

📝 chore(top10): add top 10 images for the year 2023

📝 chore(top10): add 10 images for the top 10 list of 2023

---
## [Nakul-Ramrakhyani/Portfolio_Projects-](https://github.com/Nakul-Ramrakhyani/Portfolio_Projects-)@[bd4ae9e286...](https://github.com/Nakul-Ramrakhyani/Portfolio_Projects-/commit/bd4ae9e286848e94263a9e855a22025e82d33531)
#### Saturday 2023-12-23 17:25:09 by Nakul-Ramrakhyani

Add files via upload

"Hello everyone, thank you for visiting this page. Here I'm excited to share with you my Power BI project. This project aims to 
 analyzing employee attrition Reasons (HR Analytics)🏪 , With the help of PowerBI's intuitive and powerful data 🙌 visualization tools 🛠 , I was able to dive deep into our company's employee data and uncover key insights 💭🤝.

Let's talk about the objective, conclusions, and project learnings that I've obtained from the analysis 📈 :
▶ Objective👇:
Help an organization to improve employee performance and improve employee retention (reduction in attrition) by creating an HR Analytics Dashboard. 🔐

▶Conclusions 👇 :
1. Company's average salary is 6.5k and almost 163 employees out of 1470 employees are getting up to 5k (below average salary).
2. Majority of the employees left the company after 2 years of employment.
3. The attrition rate is 16.1% which is fair and can be improved further.
4. Most lab Technicians and Sales Executives have left the job in the past years.
5. Employees that are holding a degree in Life Sciences have left the job in majority.
6. Males are leaving the company more dominantly than Females.

▶Learning Outcomes👇:
1. Created an interactive dashboard to track employee performance and reduce employee retention.
2. Used complex parameters to drill down in worksheets and customizations using filters and slicers.
3. Performed data cleaning, removed duplicates, replaced null values, and created required new columns using the DAX function for a clear image.
4. Improved the hiring process and employees' experience.
5. Used different types of customized visualizations in the form of bar charts, donut charts, line charts, area line charts, tiles, tree maps, and slicers.

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[e8cf56dcb2...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/e8cf56dcb2553c842abd7adf60a99b33d65ecfbe)
#### Saturday 2023-12-23 17:25:36 by SkyratBot

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
## [electrical-pants/f13babylon](https://github.com/electrical-pants/f13babylon)@[e211796729...](https://github.com/electrical-pants/f13babylon/commit/e2117967298eab34c19e70ff450dabe36981258e)
#### Saturday 2023-12-23 17:35:19 by panzerr1944

Map Changes, NML Edits, E-Weapon Loot Spawners & More (#303)

## About The Pull Request
Long list of fixes, edits and other things. Check the changelog for a
full list!

## Why It's Good For The Game
Less dumb spawners, better spawners for e-weapons, more cars, less setup
time, harder dungeon, more fun :)

![Screenshot 2023-12-04
142647](https://github.com/f13babylon/f13babylon/assets/76122712/468a97b4-c78d-4c92-8fcf-43d18c841db2)
![Screenshot 2023-12-04
142707](https://github.com/f13babylon/f13babylon/assets/76122712/b7d8a748-3e80-4c04-8af3-f9f660eb55ef)

## Pre-Merge Checklist
- [ Y ] You tested this on a local server.
- [ Y ] This code did not runtime during testing.
- [ Y ] You documented all of your changes.

## Changelog
🆑
remove: the 2 unique spawns on the surface/underground that can be
rushed
remove: the 'Left Hand' riot shotgun force-spawner (and Raider T-45b
spawner)
add: a chemlab, basic raider armor, louisville slugger and bino spawners
to Raider Town
add: a few more carpiles around the map
add: a Raiders minidungeon for books 1-3, since everyone else gets it
now it seems
fix: the new Kebab Town (Mobs are harder now. Beware..!) 
remove: the followers Reagent Gun (AGAIN. I did this before and someone
RE-MAPPED IT IN.)
remove: that one dumb as shit rad-puddle from infront of the BOS base 
remove: the force-spawn gauss rifle in no mans land (replaced with
experimental spawner)
add: bodybags for followers
edit: the E-Weapon spawners to the following - | Low = AEP7, Wattz, (low
chance) Wattz Magneto (someone made the AEP7 midtier for some bullshit
reason) | Mid = AER9, Plaspistol, (low chance) Wattz 2k | Mid-High =
AER12, AER9, (low chance) Ion Rifle | High = Plasrifle, Wattz 2kE, RCW,
Tribeam,(low chance) AER14
edit: the Experimental Spawner to the following: M72 Gauss | Peacekeeper
| P90 | Gatling Laser
edit: the Peacekeepers stats (Applied auto-fire shot delay of 2.8 from
1)
fix: Fixed the Remnant Bunker shoot-through wall things by replacing
them
fix: Fixed BOS NML entrance and Enclave NML Entrance
fix: Replaces NML PA claw with an edited Junker Boss (he is hard)
fix: Fixes the boss not firing
remove: the invincible interior walls in kebab, replacing them with
r_walls
fix: NML Turrets shooting NML mobs
tweak: NML kebab melee mobs and boss mobs have melee AP
add: 2 ghoul spawners to north nml + static glowing one
remove: 2 legendary ghouls from north nml
add: 4 ranged mutant spawners to south nml
remove: 2 legendary super mutants from south nml
add: 6 more turrets throughout NML (3 north, 3 south - 2 at each
building, 1 for each exterior melee weapon spawn)
add: renegade flags to kebab
🆑

---------

Co-authored-by: maaacha <116771811+maaacha@users.noreply.github.com>

---
## [Guidesu/sojourn-station](https://github.com/Guidesu/sojourn-station)@[3409d0b3ec...](https://github.com/Guidesu/sojourn-station/commit/3409d0b3ec3ac4c5a8e9bd7a0118581c9749ed51)
#### Saturday 2023-12-23 17:47:23 by benj8560

misc map fixes (#4883)

* map stuff

* small touchup

* stuff!

more minor fixes!

Relocates Ians dinner so it's not hiding away inside a closet where he can't enjoy it assumed unintended. Also returns Runtimes food to her from the old map.

Corrects the micromeds in dorms to using offsets rather then being lodged insdie a wall.

Relocates the Turbine cooling chamber blast door button to the GMs storage room and gives it a atmos ID lock for good mesure. Should keep those trainees away from the funny room.

Adds a sec cam I forgot to the new atmos hard storage room.

Moves poly into the GMs breakroom and gives him a few crackers to eat/grab. The stamp is finally free!

* weh

fixes the missing cables preventing the Terminal Lounge from getting power. You know small lounge near the big shuttle pad for ebents.

* buttttton

adds a button to control the shutter for blackshields maint backdoor

---
## [StrangeWeirdKitten/Skyrat-tg](https://github.com/StrangeWeirdKitten/Skyrat-tg)@[2805c86c81...](https://github.com/StrangeWeirdKitten/Skyrat-tg/commit/2805c86c811fde2450a054a25c7a665b77df47e5)
#### Saturday 2023-12-23 18:09:22 by Nerevar

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
## [WyattTheSkid/Et-Futurum-Requiem](https://github.com/WyattTheSkid/Et-Futurum-Requiem)@[aef5968a71...](https://github.com/WyattTheSkid/Et-Futurum-Requiem/commit/aef5968a71be261fc3f72f2848a6c2ba5e8cab5a)
#### Saturday 2023-12-23 18:16:13 by Roadhog360

OK SMARTASS INTERPRETER JUST HAVE IT ALL
OH THIS IS MISSING OH THAT IS MISSING WHO FUCKING CARES JUST COMPILE IT ANYWAYS AND IGNORE THE ONE GODDAMN MISSING FUNCTION UNTIL I COMMIT THE CODE
People be like "oh just use branches" "just commit a bit at a time" I TRY THAT AND THIS SHIT IS WHAT FUCKING HAPPENS
build failed build fauileldd sdfbsfogdiuhaeraipiz[p
It just leads to build failures
So when people tell me to use branches to confuse my code or make more """""organized""""" commits I link them to this message. Yes I'm tilted
Let's see Gradle fail this one too because it likes to be an asshole

- Add soul fire gen through WorldGenSoulFire and apply it to NetherChunkProvider, so soul fire appears on soul soil when enabled
- Due to failures with forge's custom item entity system, it has been removed and replaced with a mixin. Bugs include custom item-entities jittering when first spawned in and /give not dispensing the item into the player's inventory. It's clear the custom item entity system was NOT thoroughly tested by Forge. Old uninflammable items that exist in the world will be converted to the regular item entities automatically.
  - A system to add/remove items via the config or mod code will be added in the future, as well as adjusting their buoyancy
 - Add a biome list helper function to Utils.java, to make it easier to create biome lists with certain blacklists

---
## [terminite1/Texture-Pack-Archive](https://github.com/terminite1/Texture-Pack-Archive)@[992cbfa818...](https://github.com/terminite1/Texture-Pack-Archive/commit/992cbfa81801a65d0216114ca98ea034d1131aae)
#### Saturday 2023-12-23 18:27:10 by x37564x

words cannot describe how angry i am right now. fuck you frontpage 98

---
## [elunna/HACKEM-MUCHE](https://github.com/elunna/HACKEM-MUCHE)@[0b99885661...](https://github.com/elunna/HACKEM-MUCHE/commit/0b99885661d9a2eb5781f647ac736a2e3239d70c)
#### Saturday 2023-12-23 19:13:11 by Erik Lunna

Partial reflection (from EvilHack).

Adapted from EvilHack commit 92e32005a:

'From SporkHack - reflection is only partial now. How you're affected will vary by the
type of attack or effect. Disintegration is reflected but you'll take damage if not
resistant. Sleep ray will still make you take a nap, but the duration is greatly
diminished. Wand/finger of death won't kill you, but you'll take damage and your max HP is
affected if you don't also have magic resistance. So on and so forth.'

---
## [jameS9878989/awesome-text-to-video](https://github.com/jameS9878989/awesome-text-to-video)@[c696bf9c55...](https://github.com/jameS9878989/awesome-text-to-video/commit/c696bf9c556fdb41dbd91eaa317e99bf568e81d4)
#### Saturday 2023-12-23 19:15:43 by jameS9878989

Create jimmy

The life story. Of Gerald James Anthony Terrance. Caufield. Born in 1955. Flint Hill Dipton Went to Dipton Saint Patrick's School. Run by Catholic nuns. Watch the church burned down in Dipton Saint Patrick's when I was very young boy. Leave school at 14. I started work on Richard White. Farm. I loved it. That's where I got the Bug for the Tools. I used to fetch a Turkey home for Christmas. My mom and dad. Used to sell it I once fetched a full leg of pork home. Looking forward to Sundays dinner? And ended up with mincemeat. I asked where  pork.Had gone. We're smoking it. bought myself a little scooter? To go to work and back. Come home. Mom sold it.  for £15 . Every penny I made was took off me. I once had a Savings under me carpet in the bedroom. My little sister. Tidying my room. Found it. Give it to mom. Never saw it again. I was getting sick of being ripped off by parents. Chapter 2. I got married. To get out of the house. Started work as a butcher. Come home one day. Found out she. Was messing about. This really hurt me. I went down the wrong road for a while.  Bought A Vespa scooter. And I went to Scotland. For two years break. The best time of my life. So far. Come home. Nothing had changed. Apart from Grandma Lawlor Dying. . Which brought my heart. Moved out again. Start work. at Bob Huten Open cast coal sites. I was driving. Heavy machinery. Then I started fixing heavy machinery. I loved it. All over the country. Scotland, Wales, everywhere. Most of the time was spent in a place called Tau Law. We had five core sites. Unfortunately. Bob Huten. Died. I find somewhere else to work. So I went to Komatsu. Repair in heavy machinery.  track was everything. I got badly hurt. Went to.Langley Park Moving to my sisters. Met a lovely lady called Gillian. Now the best part of my life. gillian Had a son,  called  Michael. And he give us.. four grandchildren for me. Jake. jodi emmie. And Thomas. My beautiful little girl. Got married? I had one child. Call Alissa. I love all my grandchildren. I would die for any one of them.

---
## [Offroaders123/Bedrock-LevelDB](https://github.com/Offroaders123/Bedrock-LevelDB)@[5d65d8aeec...](https://github.com/Offroaders123/Bedrock-LevelDB/commit/5d65d8aeec34fb8cbd22d3ae80142de109d21aff)
#### Saturday 2023-12-23 19:45:22 by Offroaders123

Dedicated Server / Realms Multiplayer

Decided to try opening a multiplayer world my friends and I played on a few years ago, to see if my current parser could work with it. It's a very big world, so it does take a long time to parse *all* of the keys into the world representation object. Doing something with this for world conversion down the line will definitely need threading and better async handling, it's a lot for it to parse all at once. This is a 495 MB world though, so it is definitely on the bigger side, so I did expect it to be slow anyways. I think the best thing would be a better way to handle working with the database, not reading all of the keys in one go. I'm doing that now in a matter of learning about they Actor entry keys and values, to work in support for those before trying to optimize things a bunch.

Ok, so I found a few keys I expected to see, which I didn't have handling for, being multiplayer 'player_' entries, as well as their associated `player_server_` values, which hold the real data for each player's NBT. These are specific to playing in multiplayer, since `~local_player` handles the rest of the use cases for playing a world. This is for Realms and the Dedicated Server / LAN or Xbox playing connections.

I found two other unknown keys I have never heard nor come across yet, and I'm not sure what they are.

There were only two entries, but it looks like it's possible for there to have been more than just these. One is called `PosTrackDB-0x${number}`, and the other is called `PositionTrackDB-LastId`. The first is a suffix-based key, where it has an instancing kind of thing, hence the `${number}` ID suffix, and the other seems to be a single key for the world, which holds reference to the most recent of those `PosTrackDB` entries. I'm not sure what the purpose of these are, but I think it has something to do with multiplayer.

Not sure if this is right, but I might have a hunch for what these mean:

```
I think I might have guessed what this is for, but I'm not sure

It might have to do with player position validation, like when you get kicked from the game for "teleporting" or something like that?
Or, "You were kicked for flying"

Like when Bedrock used to (not sure if it still does it) get laggy on Realms, and kick you for flying even though you were climbing up a hill
The position tracking was a bit laggy alongside the Realm being laggy, so it miscalculated where you were, hence it though you were flying, while you were just jumping
```

This also correlates with it being for something multiplayer-related, because I've only been testing local worlds, and you don't get kicked from your own solo world for "flying". Maybe this is a Realms-specific feature? Or just the Dedicated Server in general? Cause I think Realms uses that under the hood if I'm not mistaken. I don't think playing LAN/Xbox Live will do this either, but I'm not sure. If you join someone else's world, do you get kicked for "flying" if jumping while the connection is laggy? Or rather, something similar to that. I don't remember if that's the specific case for the buggy location tracking. I think it might be related to running the world on a 'server'-like instance, hence the Dedicated Server or Realms.

https://cran.r-project.org/web/packages/rbedrock/rbedrock.pdf
https://github.com/reedacartwright/rbedrockhttps://stackoverflow.com/questions/77312855/how-much-memory-do-javascript-objects-take-in-node-js-vs-chrome (I'm concerned it will be too heavy to load everything in memory as plain objects, but I'm not certain. Of course any too-big-world will run into this, but I'm curious whether it will happen for less complex ones as well, which wouldn't be ideal. So far Node is handling the data excellently, it just takes a while to parse and sort all of the data/buffers/NBT.)

---
## [Rosstin/crawl](https://github.com/Rosstin/crawl)@[5f6fb4f5a3...](https://github.com/Rosstin/crawl/commit/5f6fb4f5a389a722ff4ee7fd78d4e43f979cce6c)
#### Saturday 2023-12-23 20:04:31 by regret-index

Add and trim a few Xom spells and cloud trails.

New spells: Wereblood, Animate Armour, Battlesphere, Malign Gateway.
Wereblood forces the player to make noise and thus is neat as a mixed
blessing, Animate Armour gets to by-pass its innate castability versus
armour weight issues to be more interesting as a random free god act,
Battlesphere makes for a decent joke if not actually usable and compensates
for the power of the two summons here, Malign Gateway has been missing
since the miscast streamlining and is extremely appropriate between the
chaos brand and unavoidable neutrality.

(These all are exchanged for Canine Familiar, which can't use one of its
most interesting aspects in the recast and thus will mostly make players
unavoidably get drained and guilt.)

New cloud trail clouds are salt and blastmotes, both at miniscule chances.
The salt's purpose is obvious, while the blastmotes are manually set at 25
power (power with those is weird and modular) and definitely give a certain
kind of danger and excitement very distinct from the spell by getting them
without having to stop for laying each of them.

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[45405782ed...](https://github.com/tgstation/tgstation/commit/45405782edea70043d687f6bda6f71cb8d43bfce)
#### Saturday 2023-12-23 20:13:37 by Rhials

Deviant Crew antag panel category, Obsessed crew now shown in orbit menu, Paradox Clone orbit tab is now white (#80450)

## About The Pull Request

This rounds up the "Other" (Brainwashed, Hypnotised, Wizard Revenge, and
Obsession) antagonist category into the new "Deviant Crew" category.
This tab is white!

Obsessed crew are now displayed in the orbit panel (no other antagonists
in this group are though).

The Spacetime Aberrations (Paradox Clone) group has also been changed to
be white.

Here's how that looks:


![image](https://github.com/tgstation/tgstation/assets/28870487/415b8cbb-7ac3-4e24-9f74-466480c2aab0)
## Why It's Good For The Game

As was the case with paradox clones, observers can already discern when
a player is obsessed. It shouldn't be a pain to observe these guys,
especially when they're a more RP oriented antag that are (usually)
deserving of the audience.

I made paradox clones and obsessed the same color because they're both
in the broader spectrum of "fucked up crew".

Also converts common text entries to a single define. That is good
coding practice I think.
## Changelog
:cl: Rhials
qol: Obsessed crewmembers are now displayed in the orbit panel.
qol: The Paradox Clone orbit menu tab is now white. Neat!
/:cl:

---
## [mbland/tomcat-servlet-testing-example](https://github.com/mbland/tomcat-servlet-testing-example)@[8526cc777f...](https://github.com/mbland/tomcat-servlet-testing-example/commit/8526cc777fec6435d6db974049a65ea4dc2c9306)
#### Saturday 2023-12-23 20:37:34 by Mike Bland

Replace gradle-node-plugin with own tasks

Removing gradle-node-plugin cuts the project's dependency footprint
slightly, and enables Windows builds to succeed.

Executing `pnpm` from a Gradle task proved straightforward. Also added a
frontendInstall task, removed the separate "Install Node packages" step
from run-tests.yaml, and refined `inputs` and `outputs` for more precise
dependency tracking.

Specifically learned about using `outputs.upToDateWhen { true }` as a
means to prevent `frontendInstall` from always running from:

- https://discuss.gradle.org/t/why-does-my-task-run-even-though-non-of-its-inputs-has-changed/5350/2

---

I entertained the notion of fixing Windows builds by removing
gradle-node-plugin after a couple of days of trying to fix that plugin.

The moral of the following story:

- Sometimes you really _shouldn't_ add a dependency if you can do what
  you need to do without it.

When starting the project, I thought running Node.js from Gradle might
be tricky, so I searched for a plugin. As it turned out,
node-gradle/gradle-node-plugin was available, and seemed to work well on
macOS and Linux. However, it broke the project on Windows, because it
failed trying to execute `uname` on Windows.

I got the plugin successfully working on Windows by introducing the
following PowerShell command to replace uname (in
com.github.gradle.node.NodePlugin.addPlatform()):

```kotlin
if (name.toLowerCase().contains("windows")) {
    executable = "powershell.exe"
    args = listOf(
        "-Command",
        "& {Get-CimInstance Win32_OperatingSystem | " +
            "Select-Object -ExpandProperty OSArchitecture}"
    )
}
```

I also updated com.github.gradle.node.util.parseOsArch to handle the
"ARM 64-bit Processor" value returned by the command.

However, many tests continued to fail, which I realized was because no
`win-arm64` build of Node.js was available for the default Node.js
version 18.17.1:

- https://nodejs.org/dist/v18.17.1/

So I updated the default to 20.10.0 (and the npm version to 10.2.3,
which ships with 20.10.0). All the (very slow) tests began to pass
except for NpmProxy_integTest and YarnProxy_integTest.

After some creative debugging whereby I emitted the test-supplied values
for HTTP_PROXY and HTTPS_PROXY, I could see that Node couldn't see the
test-supplied values. Some digging revealed that past versions of Gradle
and its TestKit didn't have native support for arm64 that would allow
for setting environment variables:

- gradle/gradle: TestKit does not pass environment variables for older
  Gradle versions when running on M1 mac #22012:
  https://github.com/gradle/gradle/issues/22012

It seemed that Gradle 7.5.1, the default used by gradle-node-plugin,
should be OK. However, it didn't seem to be.

And this is where the despair really started kicking in.

I tried various combinations of updating the JDK from 11 to 17.0.9,
Gradle from 7.5.1 to 8.5, and updating the build.gradle.kts file.

I thought updating to 17.0.9 might solve some problems, and it seemed as
high as I could go to still suport 7.5.1:

- https://docs.gradle.org/current/userguide/compatibility.html

One minor change to the build file involved moving merging entries from
the deprecated pluginBundle block to the existing gradlePlugin block:

- https://docs.gradle.org/current/userguide/upgrading_version_7.html#pluginbundle_dropped_in_plugin_publish_plugin

Another involved disabling the com.cinnober.gradle.semver-git plugin,
because launching subprocesses during the configuration phase is now an
error when using the configuration cache:

- https://docs.gradle.org/current/userguide/upgrading_version_7.html#use_providers_to_run_external_processes
- https://docs.gradle.org/current/userguide/configuration_cache.html#config_cache:requirements:external_processes

I also deleted the ill advised and useless org.gradle.test-retry plugin
and its configuration. The tests didn't appear to be unstable, so the
tests would run multiple times to keep failing in the same way. If they
didn't fail the same way, or sometimes passed, that'd've been even
worse. See:

- https://mike-bland.com/2023/09/13/the-inverted-test-pyramid.html

Then the build would fail while compiling Kotlin:

```text
  API version 1.3 is no longer supported; please, use version 1.4 or
  greater.
```

So I set in the build file:

```kotlin
tasks.compileKotlin {
    kotlinOptions {
        apiVersion = "1.9"
        languageVersion = "1.9"
```

I also boosted IntelliJ IDEA "Settings > Build, Execution, Deployment >
Compiler > Kotlin Compiler > Target JVM Version" setting to 17. Then I
updated the build file variable:

```kotlin
val compatibilityVersion = JavaVersion.VERSION_17
```

And then, finally, tests still failed because something funny happened
inside the Spock test framework, with a bunch of errors like:

```text
SystemVersion_integTest > use system node version and exec node, npm, npx and yarn program (#gv.version) > use system node version and exec node, npm, npx and yarn program (8.5) FAILED
    java.lang.reflect.InaccessibleObjectException: Unable to make field private final java.util.Map java.util.Collections$UnmodifiableMap.m accessible: module java.base does not "opens java.util" to unnamed module @609db546
        at org.junit.contrib.java.lang.system.EnvironmentVariables.getFieldValue(EnvironmentVariables.java:188)
        at org.junit.contrib.java.lang.system.EnvironmentVariables.getEditableMapOfVariables(EnvironmentVariables.java:150)
        at org.junit.contrib.java.lang.system.EnvironmentVariables.access$200(EnvironmentVariables.java:49)
        at org.junit.contrib.java.lang.system.EnvironmentVariables$EnvironmentVariablesStatement.restoreOriginalVariables(EnvironmentVariables.java:134)
        at org.junit.contrib.java.lang.system.EnvironmentVariables$EnvironmentVariablesStatement.evaluate(EnvironmentVariables.java:125)
        at org.junit.rules.ExternalResource$1.evaluate(ExternalResource.java:54)
        at org.spockframework.junit4.AbstractRuleInterceptor.evaluateStatement(AbstractRuleInterceptor.java:66)
    [ ...snip... ]
```

I already decided at this point to get rid of gradle-node-plugin, and
developed this change. But then I decided to go a little further.

This appears to be related to:

- spock/spockframework: Cannot create mock due to module java.base does
  not "opens java.lang.invoke" #1406
  https://github.com/spockframework/spock/issues/1406

This appears to be a consequence of:

- JEP 396: Strongly Encapsulate JDK Internals by Default
  https://openjdk.org/jeps/396

This apparently shipped in Java 16, and people noticed in in Spock after
upgrading to Java 17.

Based on the information in the spock issue, I tried adding the
following `jvmArgs` entry in the build file:

```kotlin
tasks.withType(Test::class) {
    useJUnitPlatform()
    systemProperty(
        // ...snip...
    )
    jvmArgs("--add-opens", "java.base/java.util=ALL-UNNAMED")
```

Reference for `--add-opens`:

- https://docs.oracle.com/en/java/javase/17/migrate/migrating-jdk-8-later-jdk-releases.html#GUID-12F945EB-71D6-46AF-8C3D-D354FD0B1781

This actually fixed the error, but on macOS, three tests failed with:

```text
> Task :npmInstall FAILED
npm WARN tarball tarball data for npm@https://registry.npmjs.org/npm/-/npm-10.2.3.tgz (sha512-lXdZ7titEN8CH5YJk9C/aYRU9JeDxQ4d8rwIIDsvH3SMjLjHTukB2CFstMiB30zXs4vCrPN2WH6cDq1yHBeJAw==) seems to be corrupted. Trying again.
npm ERR! code EINTEGRITY
npm ERR! sha512-lXdZ7titEN8CH5YJk9C/aYRU9JeDxQ4d8rwIIDsvH3SMjLjHTukB2CFstMiB30zXs4vCrPN2WH6cDq1yHBeJAw== integrity checksum failed when using sha512: wanted sha512-lXdZ7titEN8CH5YJk9C/aYRU9JeDxQ4d8rwIIDsvH3SMjLjHTukB2CFstMiB30zXs4vCrPN2WH6cDq1yHBeJAw== but got sha512-GbUui/rHTl0mW8HhJSn4A0Xg89yCR3I9otgJT1i0z1QBPOVlgbh6rlcUTpHT8Gut9O1SJjWRUU0nEcAymhG2tQ==. (2583937 bytes)
```

The tests being:

- NpmRule_integTest. succeeds to run npm module using npm_run_ when the
  package.json file contains local npm (8.5)
- NpmTask_integTest. execute npm command using the npm version specified
  in the package.json file (8.5)
- NpxTask_integTest. execute npx command using the npm version specified
  in the package.json file (8.5)

And on Windows, after all of that, the NpmProxy and YarnProxy tests
still failed. At least the changes in this commit will allow Windows to
build now, right...?

```text
* What went wrong:
Failed to calculate the value of task ':strcalc:compileJava' property
'javaCompiler'.
WindowsRegistry is not supported on this operating system.
```

Great:

- gradle/native-platform: WindowsRegistry is not supported on this
  operating system. #274
  https://github.com/gradle/native-platform/issues/274#issuecomment-1029725490
- gradle/gradle: Support ARM64 Windows #21703
  https://github.com/gradle/gradle/issues/21703

So much for Windows on arm64 for now.

This was obviously quite the learning journey, but it's only reminded me
again of how much I hate the Java ecosystem. Yet more days I wish I had
back in my life.

---
## [cuberound/cmss13](https://github.com/cuberound/cmss13)@[5d957ce94e...](https://github.com/cuberound/cmss13/commit/5d957ce94e398a102fdf16682b740e96df3e363e)
#### Saturday 2023-12-23 22:22:59 by InsaneRed

Vanguard tweaks (#5174)

# About the pull request
This catches up vanguard to current gameplay as it was last changed
approximately 4 years ago


# Explain why it's good for the game
Currently Vanguard is supposed to be a frontlining tier 3 who dashes in
> stays in and gets some damage in and goes out (thats why the shield is
a thing) and you're supposed to be able to stay there because your
abilities (pierce and dash) resets your shield. But with the recent
addition of just more damage in general be it m56d, full auto mode or
just the amnout of extra damage you can receive from the front compared
4 years ago.

The strain currently struggles and is near useless other then the
occasional go in and lucky fling.

I've changed up the dash to reset your shield once you hit ONE person,
rather then two so that you dont instantly die while going in, the
shield is very situational as it will most likely decay before you can
even go in.

Listening to people who play vanguard, i've also increased the root to
2.5 seconds (this is buffed so when the prae has the shield) the marine
can still shoot back when they're rooted so i dont think the duration is
a big problem (this is going to be a test merge so i will be watching)

# Testing Photographs and Procedure
it just works

</details>


# Changelog

:cl:
balance: Vanguard dash now restores your shield if you hit ANYONE
instead of 2 people.
balance: Vanguard buffed root now roots you for 2.5 seconds, unbuffed
for 1 second
qol: Vanguard's pierce has now a hit sound for better feedback
/:cl:

---------

Co-authored-by: InsaneRed <prodexter31@outlook.comm>

---
## [CDRDecky/f13babylon](https://github.com/CDRDecky/f13babylon)@[667500fde5...](https://github.com/CDRDecky/f13babylon/commit/667500fde5871478747cdd48d7624dab6bb42c8f)
#### Saturday 2023-12-23 23:14:11 by Stutternov

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
## [HbmMods/Hbm-s-Nuclear-Tech-GIT](https://github.com/HbmMods/Hbm-s-Nuclear-Tech-GIT)@[be2c17f102...](https://github.com/HbmMods/Hbm-s-Nuclear-Tech-GIT/commit/be2c17f1028c6129e97620c7d9ecad79b7b06579)
#### Saturday 2023-12-23 23:31:02 by Bob

can't wait for the silly people on discord bug me 24/7 about this fuckin

g commit i swear to god this is why we can't have nice things

---
## [Blad3sy/Advent-of-Code](https://github.com/Blad3sy/Advent-of-Code)@[cd58c1865e...](https://github.com/Blad3sy/Advent-of-Code/commit/cd58c1865eadf2186c1ec254771cba51953297ea)
#### Saturday 2023-12-23 23:55:05 by Blad3sy

Completed Day 22

First try on Part 1, many tries on Part 2.
Thanks to https://www.reddit.com/r/adventofcode/comments/18pfjof/2023_day_22_part_2_python_cant_figure_out_why/
for confirming that my idea for part 2 was in fact correct, I was just stupid and implemented it wrong.

Fun fact this takes 2 minutes to run every time, so I had to sit there and wait for 2 minutes every 12 times I thought I had the answer.

Did it though! Only one day behind... I can definitely do both 23/24 tomorrow, should only take six hours or so. (pain)

---

