## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-12-09](docs/good-messages/2023/2023-12-09.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 3,052,704 were push events containing 3,824,870 commit messages that amount to 192,406,498 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 64 messages:


## [xXPawnStarrXx/tgstation](https://github.com/xXPawnStarrXx/tgstation)@[5f305ca5f7...](https://github.com/xXPawnStarrXx/tgstation/commit/5f305ca5f7b3143360c2107102ea10ad96326839)
#### Saturday 2023-12-09 00:20:03 by ATH1909

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
## [git/git](https://github.com/git/git)@[a1fbe26a0c...](https://github.com/git/git/commit/a1fbe26a0c2bb8ba84c3976023e4ded4cf94608e)
#### Saturday 2023-12-09 01:03:36 by Elijah Newren

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
## [Stutternov/f13tbd](https://github.com/Stutternov/f13tbd)@[ba55bbfedf...](https://github.com/Stutternov/f13tbd/commit/ba55bbfedfb9c6a9a46c3a4b572c230f5d42ab4a)
#### Saturday 2023-12-09 01:07:51 by Stutternov

Bobstation Ghost Port (#300)

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

Remembered Escape from Navarro and remembered Bobstation codebase had
interesting ghost mechanics with seeing in monochrome while dead and
de-limbed limbs pop off yourself and stay missing as a ghost.

Ended up finding out - most of it would port with ease! Sadly the motion
blur was really too annoying to get working, but I plan to look at it at
some point. And, while I could get monochrome working, I want to run
that by people first. I enjoy it, but I know it fucks with people. But
hey - lookin' gooood.

De-limbing makes the limb disappear on the ghost.

![image](https://github.com/f13babylon/f13babylon/assets/47883419/3b4c7ca3-5761-4159-aedd-e64ae4fc2aa7)

Wearing armor or clothing? Well, it'll stay on you when you're dead!

![image](https://github.com/f13babylon/f13babylon/assets/47883419/bfae701f-5931-4038-b52b-1a429e286882)

And even if you matrix it stays.

![image](https://github.com/f13babylon/f13babylon/assets/47883419/10e63ba4-e6a1-4e15-90da-a1ca82c50535)

## Why It's Good For The Game

It's more of a nice addition to how I even remember ollld TG worked with
ghosts, minus the delimbing and armor. The style kind of fits and makes
ghosts stand out, letting you see who they were - even if you didn't
catch the name - when alive.

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
add: Ports Bobstation's ghost system, preps for eventual porting of
motion blur code portion as well.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: maaacha <116771811+maaacha@users.noreply.github.com>
Co-authored-by: Tom <8881105+tf-4@users.noreply.github.com>

---
## [Stutternov/f13tbd](https://github.com/Stutternov/f13tbd)@[1d8302d4e3...](https://github.com/Stutternov/f13tbd/commit/1d8302d4e35276ca63ba2b5ced5b4719ef36191c)
#### Saturday 2023-12-09 01:07:51 by Stutternov

Khan Re-Balancing (#292)

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

Yeah, so - anyways.......

Khans had some issues with their balance. I've went through and re-did
some of their loadouts for their faction.
- The lever action has been removed from Enforcers, instead it is
replaced with the Auto-5. The Auto-5 is the alternative fit as it
doesn't fit in bags like the lever, holds one less round, but in return
fires slightly faster. This is on-par with actual other factions (as the
only faction that got lever shotguns round start are vet-legion. Auto-5s
are more common.)
- The Enforcer and Smith have kept the selectable trait book, but Khans
over-all had a silly amount of traits. Therefor Chemist and Senior
Enforcer had theirs removed. (Senior has enough perks, and the book for
Chemist made the loadout selection for perks worthless.)
- Smith has lost their explosive crafting, but Chemist has gotten the
advanced explosive crafting book akin to NCR sappers who get the choice
of one. (To make Chemist loadout balanced, the lowsurgery book has been
replaced with medium surgery, since both NCR medics and Legion aux get
mid-surgery, not low)
- Khan armors have had their wound protection updated. They are now
roughly equal to NCR/Legion armor counterparts.
- Khan senior enforcer has had his round-start caps lowered from 1,000
to 500. (Tbh this may still be a bit high but w/e I was suggested this
amount)
- Smith, in exchange for losing explosive trait book, has instead gained
more gun crafting recipes in exchange. Can make all base Khan guns plus
10mm smg and some others. Plus - can make alloys like NCR LO / Legion
forgemaster. (Lost their GnB part 4 server-start learned. Work for it,
like the LO has to.)
- Renamed Khan Smith into Khan Armorer, which is a canon name of a Khan
found in Fallout: NV. Minor change, but tbh fits the role better since
they are mostly focused on gun crafting _and_ smithing.
- Made the Senior Enforcer loadouts actually competitive with each
other. Hammer one now gets a deagle with it to provide a sidearm for
range, the 10mm had to be a meme since it was the WORST option possible
- and is now replaced with a Infiltrator since it's just a slightly
better R-91 with a scope. (I'd argue this makes up for the now lack of
an extra selectable trait for head enforcer.)

Also - small hotfix, why the fuck did the Senior Scribe had low surgery
skill but Scribe has mid-surgery??? Not khan related but come on.....
scribe gaming..........

## Why It's Good For The Game

The major factions on server have gotten a fair bit of balancing
attention but Khans lacked a lot, such as overlooked wound armor
protection, their round start caps, and how many traits they could get
(which honestly felt like an unintended oversight, maybe???)

I think this attempts to re-do the Khan loadouts without per-say
'nerfing' them but rather fixing the fact that many of the loadouts
aren't unique to the role (i.e easily replacing chemist with smith, or
vice-versa) - as this has some buffs as well in things Khans were weak
in, such as Smith not having much unique to them.

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
balance: See about section
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Stutternov/f13tbd](https://github.com/Stutternov/f13tbd)@[31c7e3d8db...](https://github.com/Stutternov/f13tbd/commit/31c7e3d8db0dec0828717112a6ae0f03970d058f)
#### Saturday 2023-12-09 01:07:51 by JawnWick

Skinwalker-B-Gone/God Bless America: Enclave Bunker/Casper Changes (#299)

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

Takes a good chunk (around half) of the salvage cars from the parking
lot entering Casper, and places them in and around the exterior of the
Enclave bunker.

Adds a camera system to the bunker.

Moved prewar weapon spawn behind bunker doors.

## Why It's Good For The Game

Enclave can still do salvaging without John Republic and his troopers
completely taking salvage away from the faction (they shouldn't be doing
this anyway, yall MFs need to ahelp that shit when you see it
happening). They would still need to go to the parking lot to get the
rest that was originally there for the total, but it's more manageable
now.

Camera system because super secret government entity being incapable of
observing their own bunker and the immediate exterior is funny.

Prewar spawn moved because random NCR or Followers guards would rush it
for free gamer gear.

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
add: Bunker camera system
tweak: Salvaging opportunities
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Moribox/lobotomy-corp13](https://github.com/Moribox/lobotomy-corp13)@[0a75aef49d...](https://github.com/Moribox/lobotomy-corp13/commit/0a75aef49d6474eecc4996a25c1a40766ba18df8)
#### Saturday 2023-12-09 01:10:21 by The Bron Jame Offical

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
## [p4p1/p4p1](https://github.com/p4p1/p4p1)@[33d98948fb...](https://github.com/p4p1/p4p1/commit/33d98948fbe89e534d2c1c8ffb5524578dec428e)
#### Saturday 2023-12-09 01:29:27 by p4p1

amazing waste of time fuck you twitter I'll do it manually for now and then I'll code something in JS after rev-engeneering your fucking API for free you dicks, elon fuck you why should I pay your piece of shit platform?

---
## [LeeroysHub/RM-Flipper](https://github.com/LeeroysHub/RM-Flipper)@[ccb5f7ad52...](https://github.com/LeeroysHub/RM-Flipper/commit/ccb5f7ad524240a05d84d16c77a27b0f0325abea)
#### Saturday 2023-12-09 02:00:37 by Leeroy

Rollback Keyloq to 5 months ago! Bloody regressions making my daily life shit!

---
## [eqy/pytorch](https://github.com/eqy/pytorch)@[3afb4e5cf7...](https://github.com/eqy/pytorch/commit/3afb4e5cf7b0162c532449fb5c9e7c7058a4c803)
#### Saturday 2023-12-09 02:20:04 by Brian Hirsh

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

---
## [f13babylon/f13babylon](https://github.com/f13babylon/f13babylon)@[e211796729...](https://github.com/f13babylon/f13babylon/commit/e2117967298eab34c19e70ff450dabe36981258e)
#### Saturday 2023-12-09 02:49:00 by panzerr1944

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
## [DataForgeTri/Open-VietSiriGPT](https://github.com/DataForgeTri/Open-VietSiriGPT)@[3ebe984e54...](https://github.com/DataForgeTri/Open-VietSiriGPT/commit/3ebe984e544b3048310ff857cd28d52d422a3523)
#### Saturday 2023-12-09 03:48:14 by Tri Duong

Create Open-VietSiriGPT_License.txt

Open-VietSiriGPT: Bridging AI and Vietnamese Elders

The Open-VietSiriGPT is a pioneering open-source project aimed at harnessing the power of AI to enhance the quality of life for Vietnamese elderly communities. This innovative platform, initially built around GPT-3.5, integrates voice-to-text conversion with sophisticated AI algorithms, offering a user-friendly interface for real-time interaction in Vietnamese. 

Vision & Mission

Our mission is to empower the elderly, often facing loneliness and cognitive challenges, with a tool that not only aids in daily tasks but also provides companionship and cognitive stimulation. By democratizing access to AI technology, we strive to create a more inclusive and supportive environment for our senior citizens.

Future Prospects

While the project currently focuses on community empowerment and is open for modification and improvement, there is a roadmap to potentially commercialize it in the next 4-5 years. We encourage contributions that align with our larger cause of aiding the elderly and ask that proper credits are given for any derivative work.

Guidelines for Use

- Contributions: Modifications and enhancements are welcome. Contributors are encouraged to share their versions, provided they align with our mission.
- Credits: As a collaborator or user, you are required to credit the original creator for any derivative work.
- No Warranty: The software is provided "as is", without warranty of any kind. Users engage with the software at their own risk.

Join Us

We invite developers, thinkers, and innovators to contribute to this meaningful cause. Together, let's make technology a bridge, not a barrier, for our elders.

---
## [authenyoo/authens-site-v2](https://github.com/authenyoo/authens-site-v2)@[573c12c344...](https://github.com/authenyoo/authens-site-v2/commit/573c12c344aa2bd958e2c5d8d5976bb6548f9fb5)
#### Saturday 2023-12-09 03:51:57 by authenyoo

i'm extremely tired i just slapped the no ai robots tags it looks ugly but fuck it also robots.txt awesome hell yea

---
## [Nanu308/cmss13](https://github.com/Nanu308/cmss13)@[dc234c9939...](https://github.com/Nanu308/cmss13/commit/dc234c9939efeb43170a934437f50148323407f7)
#### Saturday 2023-12-09 04:08:52 by InsaneRed

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
## [jlsnow301/tgstation](https://github.com/jlsnow301/tgstation)@[2631b0b8ef...](https://github.com/jlsnow301/tgstation/commit/2631b0b8ef1a85c75500916215fae69477784558)
#### Saturday 2023-12-09 04:54:25 by Jeremiah

Replaces prettierx with the normal prettier (#80189)

## About The Pull Request
Oh god the file diff... I'm so, so sorry.

No need to worry though. This just replaces the prettierx version that
we were using and replaces it with normal prettier. Most of the settings
were default or no longer valid with this version.
## Why It's Good For The Game
You no longer get this warning #70484

It actually drives me up the wall and I have to click it each time I
open my editor.
## Changelog
N/A nothing player facing

---
## [SteelSlayer/Paradise](https://github.com/SteelSlayer/Paradise)@[6a109ade7f...](https://github.com/SteelSlayer/Paradise/commit/6a109ade7f7cd612dcd371f64c4485340ab963d9)
#### Saturday 2023-12-09 05:11:51 by Henri215

Moves a few sprites out of items.dmi (#23301)

* fuck you items.dmi

* banhammer

---
## [Zevotech/Shiptest](https://github.com/Zevotech/Shiptest)@[e6de474a88...](https://github.com/Zevotech/Shiptest/commit/e6de474a88ef4547a7fde78495959deab1320a63)
#### Saturday 2023-12-09 05:23:31 by Imaginos16

Li Tieguai: Cybersun Edition (#2505)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
This PR reworks and updates the Li Tieguai's design into a Cybersun
Ship, as it was outlined in its lore, and what it was slated to become.

![2023-11-22 02 00
49](https://github.com/shiptest-ss13/Shiptest/assets/77556824/cc6a667a-e5dd-46ab-84fe-8351e050bf60)

![2023-11-22 02 00
50](https://github.com/shiptest-ss13/Shiptest/assets/77556824/68face8f-3bb9-4314-9cbc-3db5e92b9fa7)


(SHIP IS NOW FUCKING FLIPPED LET'S GO)

This PR also adds a new job, the Medical Director. It functions exactly
as how a CMO would, but for Cybersun instead!


![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/5c93414c-4805-4b38-8ee7-e08ebde3c9ee)

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
MEDICAL CYBERSUN SHIP IS FINALLY REAL OH MY GOD.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: PositiveEntropy
add: The Li-Tieguai is now officially, a Syndicate ship!
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [meemofcourse/Shiptest](https://github.com/meemofcourse/Shiptest)@[caa19d2a6f...](https://github.com/meemofcourse/Shiptest/commit/caa19d2a6f8014c2d34663c7c63685921bc0218a)
#### Saturday 2023-12-09 05:47:31 by GenericDM

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
## [crawl/crawl](https://github.com/crawl/crawl)@[196b491b36...](https://github.com/crawl/crawl/commit/196b491b3682a0ba7d1c76b2060a87d0b9f7594d)
#### Saturday 2023-12-09 06:20:24 by regret-index

Step one of far too many for revising Chaos brand

Chaos brand is an absolute nightmare under the code, and also extremely
awkward as an actual design in practice. Players give the monsters with it
an extremely wide berth because of the banishment chance (which is actually
just 0.15%) and the very long buffs / debuffs list also attached, except
secretly the paralysis / slowing / petrifying effects were actually
invisibly casting a hex with power equal to the damage dealt. This was
actually pretty weak against the player's increasing AC and Willpower over
the course of the game, outside of mister super early Yiuf. (Meanwhile,
mushroom fist style AF_CONFUSE got a flat chance without a check, and also
chaos clouds made absolutely zero will / damage check to apply any of the
effects). In player hands, the weapon has a handful of miserable hits for
most of the game without ranged or summons- hasting or berserking a monster
is quite the betraying roll- and is also somewhat boring in the effects
it can actually get, regularly being rather common effects in the rest of
the game.

While there's been dev interest in revising this all for next version,
trying out more dramatic effects after they were culled out due to the
miscast streamlining, I'm doing some quick revisions now that make it
consistently somewhat dangerously yet while also reducing the most
dangerous individual effects from player or monster hands. This should
make it far less awkward to be desperately avoiding monster melee for a
sub-4% chance of an actually notable effect.

 * Chaos debuffs via the weapon brand and attack flavour both consistently
   ignore defender willpower now, with another flag added to beams. With
   how several different effects (confusion most notably) and clouds both
   didn't care about this, it's best to err towards the more dramatic for
   something we've been very cautious about spreading.

 * As compensation for the above and to have less hyper-rare rapid-death
   results, distortion has been taken off the regular weapon brands check
   (clearing off banishment) and paralysis is capped at exactly 1 turn
   (like Stunning Burst). On the player end of things, turning monsters
   into shapeshifters has been cut (poly does the same thing scaling
   better throughout the game), while monster berserk has now been
   replaced with Frenzied (keeping haste + 50% damage, losing HP buff,
   becoming neutral) like datura and Discord, which makes it more
   interesting as an upside and downside simultaneously.

 * Added as new effects to entice wielders and terrify victims are weak,
   corrosion, halved will, vitrifying, sleep, and ensnaring webs. Blink
   has also been isolated and preserved off of distortion. Agility's
   out barring a dramatic revision to it as a boring flat +5 EV.

 * Through some adjustments to the varied lists and another beam, both
   seething chaos clouds and Chain of Chaos has been updated to match the
   current non-brand effects list again.

Since we're not using most chaos monsters outside of the Abyss, there's not
too much concern to mildly nerf a few of them- they'll be far more
consistent in applying effects, anyway. Chaos spawn counts in a few earlier
vaults have been lowered or tiered higher, too.  It's probably worth
keeping an eye on Chaos Knight starting weapons, but most people actually
trying to win currently unwield those very fast, and this could do with a
fair bit of testing first. Probably should keep an eye on Malign Gateway
too.

TODO: make a chaos.cc that can handle these behaviours so that Chain of
Chaos doesn't desynch regularly, and so that clouds aren't faking a melee
hit of the person inside hitting themselves for zero damage to enchant
themselves with the chaos effects list. Also there's probably still more
effects to screw around with, too, like Devastator-style explosions,
random summons, brilliance, or cancellation. This is a relatively less
disruptive update for now, mostly aimed at making these all behave far
more parseably and more usably.

---
## [LemonInTheDark/tgstation](https://github.com/LemonInTheDark/tgstation)@[2e0597d055...](https://github.com/LemonInTheDark/tgstation/commit/2e0597d055fc105037a904355726139434f36b3a)
#### Saturday 2023-12-09 06:32:18 by Vekter

Replaces the fake monkey cube in Birdshot tool storage with a less lethal one, adds something else fun (#80030)

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

---
## [Eversco/UI_Design](https://github.com/Eversco/UI_Design)@[9a0687de56...](https://github.com/Eversco/UI_Design/commit/9a0687de56b2e038a2b5e1ee1f64adf8a0e43be6)
#### Saturday 2023-12-09 06:35:44 by spink

Imported ThirdPersonController asset

I really love spikecactus․ Like‚ a lot․ Like‚ a whole lot․ You have no idea․ I love him so much that it is inexplicable‚ and I'm ninety-nine percent sure that I have an unhealthy obsession․ I will never get tired of listening that sweet‚ angelic voice of his․ It is my life goal to meet up his with his in real life and just say hello to him․ I fall asleep at night dreaming of him holding a personal concert for me‚ and then he would be sorry tired that he comes and cuddles up to me while we sleep together․

---
## [Maybe-Anton/Shiptest](https://github.com/Maybe-Anton/Shiptest)@[1e0af20375...](https://github.com/Maybe-Anton/Shiptest/commit/1e0af20375625985041d9e9b708b7eeff3e0c22f)
#### Saturday 2023-12-09 07:25:39 by GenericDM

licorice (#2573)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
renames licorice ice cream
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
regardless of if it's a reference to a real brand or not, i doubt it was
added to /tg/ in good faith. regardless, the company would not have
survived the night of fire, and making it vague prevents people from
making cheap jokes
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

🆑
tweak: renames licorice ice cream
/🆑

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Maybe-Anton/Shiptest](https://github.com/Maybe-Anton/Shiptest)@[173fb06ed3...](https://github.com/Maybe-Anton/Shiptest/commit/173fb06ed32897dc6a58f2cc32f6fcb60747c9a9)
#### Saturday 2023-12-09 07:25:39 by Imaginos16

Li Tieguai: Cybersun Edition (#2505)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

This PR reworks and updates the Li Tieguai's design into a Cybersun
Ship, as it was outlined in its lore, and what it was slated to become.

![2023-11-22 02 00
49](https://github.com/shiptest-ss13/Shiptest/assets/77556824/cc6a667a-e5dd-46ab-84fe-8351e050bf60)

![2023-11-22 02 00
50](https://github.com/shiptest-ss13/Shiptest/assets/77556824/68face8f-3bb9-4314-9cbc-3db5e92b9fa7)

(SHIP IS NOW FUCKING FLIPPED LET'S GO)

This PR also adds a new job, the Medical Director. It functions exactly
as how a CMO would, but for Cybersun instead!

![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/5c93414c-4805-4b38-8ee7-e08ebde3c9ee)

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

MEDICAL CYBERSUN SHIP IS FINALLY REAL OH MY GOD.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

:cl: PositiveEntropy
add: The Li-Tieguai is now officially, a Syndicate ship!
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Noah6544/NoahBuchananPortolio](https://github.com/Noah6544/NoahBuchananPortolio)@[e16ff52c38...](https://github.com/Noah6544/NoahBuchananPortolio/commit/e16ff52c3883dfec5d2a54f49b1dd74ef769270a)
#### Saturday 2023-12-09 07:37:46 by Noah Buchanan

I GOT INTO GA TECH!!! updated some titles, the range slider, and spent too long implenting an idea I had a whim (the click feature for about me images). but fr, it's insane i'm in ga tech, my dream is a reality. heartbroken that some of my friends didn't make it tho. actually devestated, but it'll all work out. (easy for me to say, ik).

---
## [repinger/android_kernel_xiaomi_sm8250](https://github.com/repinger/android_kernel_xiaomi_sm8250)@[97676b7a63...](https://github.com/repinger/android_kernel_xiaomi_sm8250/commit/97676b7a63f32bf94daa56409d31b5d905afa380)
#### Saturday 2023-12-09 08:04:36 by Peter Zijlstra

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
## [repinger/android_kernel_xiaomi_sm8250](https://github.com/repinger/android_kernel_xiaomi_sm8250)@[efa536d75e...](https://github.com/repinger/android_kernel_xiaomi_sm8250/commit/efa536d75e7c28e86582955f2197e47d3a519f90)
#### Saturday 2023-12-09 08:04:36 by Peter Zijlstra

sched: Fix loadavg accounting race

The recent commit:

  c6e7bd7afaeb ("sched/core: Optimize ttwu() spinning on p->on_cpu")

moved these lines in ttwu():

	p->sched_contributes_to_load = !!task_contributes_to_load(p);
	p->state = TASK_WAKING;

up before:

	smp_cond_load_acquire(&p->on_cpu, !VAL);

into the 'p->on_rq == 0' block, with the thinking that once we hit
schedule() the current task cannot change it's ->state anymore. And
while this is true, it is both incorrect and flawed.

It is incorrect in that we need at least an ACQUIRE on 'p->on_rq == 0'
to avoid weak hardware from re-ordering things for us. This can fairly
easily be achieved by relying on the control-dependency already in
place.

The second problem, which makes the flaw in the original argument, is
that while schedule() will not change prev->state, it will read it a
number of times (arguably too many times since it's marked volatile).
The previous condition 'p->on_cpu == 0' was sufficient because that
indicates schedule() has completed, and will no longer read
prev->state. So now the trick is to make this same true for the (much)
earlier 'prev->on_rq == 0' case.

Furthermore, in order to make the ordering stick, the 'prev->on_rq = 0'
assignment needs to he a RELEASE, but adding additional ordering to
schedule() is an unwelcome proposition at the best of times, doubly so
for mere accounting.

Luckily we can push the prev->state load up before rq->lock, with the
only caveat that we then have to re-read the state after. However, we
know that if it changed, we no longer have to worry about the blocking
path. This gives us the required ordering, if we block, we did the
prev->state load before an (effective) smp_mb() and the p->on_rq store
needs not change.

With this we end up with the effective ordering:

	LOAD p->state           LOAD-ACQUIRE p->on_rq == 0
	MB
	STORE p->on_rq, 0       STORE p->state, TASK_WAKING

which ensures the TASK_WAKING store happens after the prev->state
load, and all is well again.

Fixes: c6e7bd7afaeb ("sched/core: Optimize ttwu() spinning on p->on_cpu")
Reported-by: Dave Jones <davej@codemonkey.org.uk>
Reported-by: Paul Gortmaker <paul.gortmaker@windriver.com>
Signed-off-by: Peter Zijlstra (Intel) <peterz@infradead.org>
Tested-by: Dave Jones <davej@codemonkey.org.uk>
Tested-by: Paul Gortmaker <paul.gortmaker@windriver.com>
Link: https://lkml.kernel.org/r/20200707102957.GN117543@hirez.programming.kicks-ass.net
Change-Id: I26d4c16043df672db986f8a9a24e013e21ac2d01
Signed-off-by: repinger <devel@repinger.my.id>

---
## [elunna/HACKEM-MUCHE](https://github.com/elunna/HACKEM-MUCHE)@[4bd835c7fb...](https://github.com/elunna/HACKEM-MUCHE/commit/4bd835c7fbb8927ed923991d0a6f1c253a0c3857)
#### Saturday 2023-12-09 08:19:17 by Erik Lunna

Water Elementals can now engulf and suffocate.

From xNetHack commit ee808b73e:

'This is a change that is ultimately from GruntHack, by way of Keith
Simpson. Attacks of the combination AT_ENGL AD_WRAP are now parsed as
suffocation engulfing. On the hero, this begins a suffocation timer of
5; on monsters it just deals the normal damage for that attack, unless
the engulfed monster is breathless.

Additionally, when a water elemental engulfs the player, d3 inventory
items are wetted, and water elementals are given a passive rust attack.

This contains a fix to the GruntHack bug in which escaping a suffocating
engulfer by teleporting either you or it doesn't actually clear the
strangulation timer, causing the hero to die even after being safe.

Other weird edge cases that either didn't translate to 3.6 or were never
implemented in Grunt:
* If you put on an amulet of strangulation, it doesn't set Strangled to
  6 unconditionally (this could be used to buy more time when engulfed by
  a suffocating monster). It only sets it to 6 if higher than 6, or if
  it was 0 previously.
* Remove the Grunt case where an amphibious() monster feels quite
  comfortable inside a water elemental, because amphibious() actually
  means "amphibious or breathless", which means that a lot of monsters
  like vampires got the "quite comfortable" message which didn't make
  sense. Instead just give the general breathless case.
* Track the old value of uswallow in gulpmu, and use this to avoid
  re-printing "It's impossible to breathe in here!" when you get hit by
  another suffocation engulf attack while already engulfed.
* Add suffocation-from-monster cases to check_strangling, so that
  polyself into a breathless monster while being suffocated inside an
  engulfer will work to save you.'

Note: In the original commit, gelatinous cubes could also engulf - however, I have left this out. I think the gelatinous cube is probably fine as is, and with the paralysis creates some pretty helpless situations for the player. Adding this mechanic only for the water elemental feels more fitting - and it makes the plane of water kind of terrifying without magical breathing.

---
## [Time-Green/tgstation](https://github.com/Time-Green/tgstation)@[349adbb438...](https://github.com/Time-Green/tgstation/commit/349adbb438d5ca216b8f76c5251a1bf90473e0ce)
#### Saturday 2023-12-09 09:28:50 by Ghom

[NO GBP] Fixing elevation furthermore (#80099)

## About The Pull Request
fixes #80059
fixes #80085.

The tram transportation doesn't use `forceMove()`, instead it just
changes the location of the objects directly. What's more, it doesn't
call `oldloc.Exited()` or `loc.Entered()` but only for areas. The
abstract exited/entered signals are from `Moved()` though, which is
called.

https://github.com/tgstation/tgstation/blob/df4bc6d948576a2ec32a90c23c93ec90e54e3933/code/modules/transport/transport_module.dm#L519-L527

About beds, well, I just happened to put a minus symbol where it
shouldn't be.

## Why It's Good For The Game
Truly one of the fuckups of the year. Now tested. I'll make a unit test
later.


## Changelog

:cl:
fix: Fixed some oopsie whoopsie with elevation, trams and beds causing
people to visually ascend or descend to heaven or hell.
/:cl:

---
## [addytrunks/react](https://github.com/addytrunks/react)@[b6978bc38f...](https://github.com/addytrunks/react/commit/b6978bc38f6788c7e73982b9fd2771aabdf36f15)
#### Saturday 2023-12-09 10:10:23 by Andrew Clark

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
## [apollographql/federation](https://github.com/apollographql/federation)@[4e630d964e...](https://github.com/apollographql/federation/commit/4e630d964eeeba5a42ecd13f02f6e8f5b757523e)
#### Saturday 2023-12-09 10:27:49 by Edward Huang

docs: fix broken links (#2885)

<!--
First, 🌠 thank you 🌠 for taking the time to consider a contribution to
Apollo!

Here are some important details to follow:

* ⏰ Your time is important
To save your precious time, if the contribution you are making will
take more than an hour, please make sure it has been discussed in an
        issue first. This is especially true for feature requests!

* 💡 Features
Feature requests can be created and discussed within a GitHub Issue.
Be sure to search for existing feature requests (and related issues!)
prior to opening a new request. If an existing issue covers the need,
please upvote that issue by using the 👍 emote, rather than opening a
        new issue.

* 🕷 Bug fixes
These can be created and discussed in this repository. When fixing a
bug,
please _try_ to add a test which verifies the fix. If you cannot, you
should
still submit the PR but we may still ask you (and help you!) to create a
test.

* Federation versions
Please make sure you're targeting the federation version you're opening
the PR for. Federation 2 (alpha) is currently located on the `main`
branch and prior versions of Federation live on the `version-0.x`
branch.

* 📖 Contribution guidelines
Follow
https://github.com/apollographql/federation/blob/HEAD/CONTRIBUTING.md
when submitting a pull request. Make sure existing tests still pass, and
add
        tests for all new behavior.

* ✏️ Explain your pull request
Describe the big picture of your changes here to communicate to what
        your pull request is meant to accomplish. Provide 🔗 links 🔗 to
        associated issues!

We hope you will find this to be a positive experience! Open source
contribution can be intimidating and we hope to alleviate that pain as
much
as possible. Without following these guidelines, you may be missing
context
that can help you succeed with your contribution, which is why we
encourage
discussion first. Ultimately, there is no guarantee that we will be able
to
merge your pull-request, but by following these guidelines we can try to
avoid disappointment.

-->

---
## [reactos/reactos](https://github.com/reactos/reactos)@[cc63d8f4a2...](https://github.com/reactos/reactos/commit/cc63d8f4a2c3e4e22dd3f4c706e2373978914b68)
#### Saturday 2023-12-09 10:34:01 by George Bișoc

[SDK][CMLIB] Implement log transaction writes & Resuscitation

=== DOCUMENTATION REMARKS ===

This implements (also enables some parts of code been decayed for years) the transacted writing of the registry. Transacted writing (or writing into registry in a transactional way) is an operation that ensures the successfulness can be achieved by monitoring two main points.
In CMLIB, such points are what we internally call them the primary and secondary sequences. A sequence is a numeric field that is incremented each time a writing operation (namely done with the FileWrite function and such) has successfully completed.

The primary sequence is incremented to suggest that the initial work of syncing the registry is in progress. During this phase, the base block header is written into the primary hive file and registry data is being written to said file in form of blocks. Afterwards the seconady sequence
is increment to report completion of the transactional writing of the registry. This operation occurs in HvpWriteHive function (invoked by HvSyncHive for syncing). If the transactional writing fails or if the lazy flushing of the registry fails, LOG files come into play.

Like HvpWriteHive, LOGs are updated by the HvpWriteLog which writes dirty data (base block header included) to the LOG themselves. These files serve for recovery and emergency purposes in case the primary machine hive has been damaged due to previous forced interruption of writing stuff into
the registry hive. With specific recovery algorithms, the data that's been gathered from a LOG will be applied to the primary hive, salvaging it. But if a LOG file is corrupt as well, then the system will perform resuscitation techniques by reconstructing the base block header to reasonable values,
reset the registry signature and whatnot.

This work is an inspiration from PR #3932 by mrmks04 (aka Max Korostil). I have continued his work by doing some more tweaks and whatnot. In addition to that, the whole transaction writing code is documented.

=== IMPORTANT NOTES ===

HvpWriteLog -- Currently this function lacks the ability to grow the log file size since we pretty much lack the necessary code that deals with hive shrinking and log shrinking/growing as well. This part is not super critical for us so this shall be left as a TODO for future.

HvLoadHive -- Currently there's a hack that prevents us from refactoring this function in a proper way. That is, we should not be reading the whole and prepare the hive storage using HvpInitializeMemoryHive which is strictly used for HINIT_MEMORY but rather we must read the hive file block by block
and deconstruct the read buffer from the file so that we can get the bins that we read from the file. With the hive bins we got the hive storage will be prepared based on such bins. If one of the bins is corrupt, self healing is applied in such scenario.

For this matter, if in any case the hive we'll be reading is corrupt we could potentially read corrupt data and lead the system into failure. So we have to perform header and data recovery as well before reading the whole hive.

---
## [SyncIt21/The-TG-Station-Fork](https://github.com/SyncIt21/The-TG-Station-Fork)@[b8fc9b367e...](https://github.com/SyncIt21/The-TG-Station-Fork/commit/b8fc9b367ebb26def792a68bcb25294e518698d8)
#### Saturday 2023-12-09 10:48:00 by LemonInTheDark

Icon Autoslicing (#79659)

## About The Pull Request

Ok so you know all the dmis we have that are made to work with the
smoothing system? carpets, walls, etc.

The proper way to edit those is to convert them into a png with 5
"states' it in (one for 0 connections, one for horizontal, one for
vertical, one for all cardinals and one for all directions) and then
modify THAT, then run it through [the cutter
tool.](https://github.com/tgstation/icon-cutter)

But none ever does that, because we explain it fucking nowhere. So
instead, let's keep all those "base" files in the repo, alongside the
configs they work with, and "cut" the pngs into dmis as a part of the
build process.

I wrote a guide for how to interact with this system as a spriter, you
can find it
[HERE](https://github.com/LemonInTheDark/tgstation/blob/slice-the-sky/icons/Cutter.md).

[Adds a icon cutter build
task](https://github.com/tgstation/tgstation/commit/52143d2e96498de92421d516e0dd3f23936f88d8)

This relies on action ninja's hypnagogic (find more
[here](https://github.com/actioninja/hypnagogic)), a rust based icon
cutter.
It operates inline with the file structure, searching the codebase for
templates and resource files and compiling them down to dmis.

It can do way more then just bitmask stuff, but that is what we are
using it for rn.

Hope is to prevent for eternity the "I'm just gonna edit each of these
255 icon states that's how this carpet was made right?" meme, and allow
more expansive use of smoothing in future

[Adds a lint that ensures config files work
right](https://github.com/tgstation/tgstation/commit/21eeab9cf831c5fdac5a9b366478a9dab285c20c)

Checks to ensure they have a paired png and dmi, and also avoids issues
with uncompiled changes by double checking that nothing happens
before/after a cutter run

[Pulls all non smoothed states out of structures into bespoke
dmis](https://github.com/tgstation/tgstation/commit/a730e0cb47fc0a622fe265bccc296cec8d3a8fea)

This is required because the cutter cannot output named icon states,
only the actual cut icon

[Does something similar to
walls](https://github.com/tgstation/tgstation/commit/40780e9481103c8ee9e16538d1c2d0cdc124eeb9)

Moves reinforced walls decon stuff from their icon to a var on the type
and a set of states in the reinforced_states dmi

Moves falsewalls into their own dmi, this involved some changes to
gamecode to ensure falsewalls knew which dmi to use and what key.
Makes falsewalls display as such in editor rather then just walls

Moves smoothrock's gibonite overlays into their own file for similar
reasons

[Same thing different day
(Floors)](https://github.com/tgstation/tgstation/commit/9a3da3b69705278f39af109ac5ce86d27c2479a1)

Pulls bespoke floor icon states into their own file, splits up neon
carpets into multiple files to make cutting possible

[Actually adds the cut templates and their matching png
files](https://github.com/tgstation/tgstation/commit/1bd8920dc90d1ee1b934b6dadc39f2331854f5fa)

Not much to report here, outside of I changed the prefix for bamboo
walls to bamboo_wall so it works with false_walls

## Why It's Good For The Game


![image](https://github.com/tgstation/tgstation/assets/58055496/7c3ac7fb-873c-481b-8667-082e39432876)

None should have to manually edit cut dmis. Ever.
Also this makes adding a new smoothed thing trivial, don't even need to
know what tool you're using to do it. V good v good.
Sets us up nicely for wallening's well, wall of sprites.

Some structural decisions, we are essentially committing build artifacts
here. That's the best way of handling it because otherwise mappers could
need to run build.bat before opening a map, and that is stupid!

## Changelog
:cl:
refactor: (Almost) all smoothed icons can now be edited in their pre cut
forms
/:cl:

---
## [asrofilfachrulr/gorengan-indonesia](https://github.com/asrofilfachrulr/gorengan-indonesia)@[7fc97f71a2...](https://github.com/asrofilfachrulr/gorengan-indonesia/commit/7fc97f71a29f2837fd141b983a9308b94bd06dd1)
#### Saturday 2023-12-09 11:43:06 by anya

i hate myself... implement logic on editing recipe. bugs on accessing spinner selected item, doubling in materials and my brain is fk dumb

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[edbc7c5622...](https://github.com/tgstation/tgstation/commit/edbc7c562261e95d58140463ed6a1a23102fc2f3)
#### Saturday 2023-12-09 12:05:15 by John Willard

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
## [MTandi/tgstation](https://github.com/MTandi/tgstation)@[c9d2c940d8...](https://github.com/MTandi/tgstation/commit/c9d2c940d87f5205bdf882280af074b132e1af6c)
#### Saturday 2023-12-09 12:41:33 by Vekter

Ports feral cats and feral cat grenades from Hippie (#80031)

## About The Pull Request
Feral Cats are just a hostile variant of cats that will fuck you up if
they see you. They are added solely for the sake of feral cat grenades -
a new, interesting, and fuzzy way to get out of a jam or just wreak
havoc around you. Each one costs 5 TC and spawns 5 really pissed off
cats to chase down assistants in the hallway.

They don't currently ignore traitors or the person who threw them - I
haven't worked out how to do that with our faction system (Hippie gave
them the syndicate faction but traitors don't get that on our codebase).
If anyone wants to contribute or help me suss that out it'll be cool,
otherwise just don't be around if there's nobody else for them to maul.

## Why It's Good For The Game
They're funny.

## Changelog
:cl: Vekter
add: Added a new hostile variant of cats, "feral cats".
add: Added a new traitor item, "feral cat grenades". For 5 TC, you too
can throw a grenade at someone and make five cats maul them to death.
/:cl:

---
## [Oluwafunso56/STUDENT-PERFORMANCE-ANALYSIS](https://github.com/Oluwafunso56/STUDENT-PERFORMANCE-ANALYSIS)@[b6688a966a...](https://github.com/Oluwafunso56/STUDENT-PERFORMANCE-ANALYSIS/commit/b6688a966aa1e864d11a350e4dd90b49d41d30a2)
#### Saturday 2023-12-09 12:56:30 by Oluwafunso Soyoye

Add files via upload


Insights from the Student Performance Analysis Image

The image shows a number of charts that analyze student performance data. The charts are organized by gender, test preparation, parental education level, race/ethnicity, and lunch program participation.

Overall Insights

Gender: Girls tend to outperform boys in reading and writing, while boys tend to outperform girls in math.
Test preparation: Students who complete a test preparation course tend to score higher on average.
Parental education level: Students whose parents have higher levels of education tend to score higher on average.
Race/ethnicity: There are some differences in average scores across racial/ethnic groups, but the differences are not large.
Lunch program participation: Students who participate in the lunch program tend to score lower on average than students who do not participate in the program.
Specific Recommendations

Teachers and administrators can use the data to identify students who may need additional support. For example, the data shows that girls tend to outperform boys in reading and writing. Teachers may want to provide additional support to boys in these areas.
Schools can offer test preparation courses to all students, or to students who are struggling academically. The data shows that students who complete a test preparation course tend to score higher on average.
Schools can work with parents to support their children's learning at home. The data shows that students whose parents have higher levels of education tend to score higher on average.
Schools can investigate the reasons why students who participate in the lunch program tend to score lower on average. This may be due to a number of factors, such as food insecurity or lack of access to educational resources at home.
Creative Recommendation

Schools could create a personalized learning plan for each student based on their individual performance data. This plan could include specific goals and strategies to help the student improve in their areas of weakness.

---
## [mogeoko/tgstation](https://github.com/mogeoko/tgstation)@[7f0536bb93...](https://github.com/mogeoko/tgstation/commit/7f0536bb930a022d23d636619e4baf73661280a2)
#### Saturday 2023-12-09 13:13:07 by san7890

Makes Telekinesis + Russian Revolver Interaction more fair (#79740)

## About The Pull Request

Fixes #77238

Basically, you were able to just spam kill people with the russian
revolver if you had telekinesis, which isn't really fair. Now, after
taking a leaflet out of the the discussion in that issue report, you can
still pull off the same party trick... once...

Basically, let's just say that when you focus on firing the gun in your
mind... you're also pointing it directly at your mind (your brain (your
skull (you instantly die))). This occurs even if the projectile doesn't
actually touch you (because that would be hellish to account for) but
you're the one who's playing russian roulette man

You still get to do some collateral damage because that's still a very
funny interaction but you only get to do it once per life. I don't know
if people will be happy to revive you after you "shoot" them. Also, the
way it's coded means that you can still leave the revolver on the table
and fire it at your foot or something, or just use it normally, as a
telekinesis user. This _only_ applies to distance-based firings.
## Why It's Good For The Game

The russian revolver is specifically coded to prevent you from damaging
other people, and this was a pretty silly way to sidestep that based on
the checks. Instead, let's make it so that you can still do this
admittedly funny interaction, but with enough reason to not do it (the
reason being that you'll always get fucking blatted).
## Changelog
:cl:
balance: After a string of unfortunate incidents, persons with
telekinesis have been strongly warned against playing Russian Roulette,
as they tend to hyperfixate on the gun a bit too much and end up firing
it directly at their head.
/:cl:

---
## [mogeoko/tgstation](https://github.com/mogeoko/tgstation)@[66b8b1d866...](https://github.com/mogeoko/tgstation/commit/66b8b1d8669379eac50fa358a3eb5e7707b46f25)
#### Saturday 2023-12-09 13:13:07 by Fikou

Revert "if you die in a mech you are ejected" (#79768)

Reverts tgstation/tgstation#79380
this is literally what the mech removal tool is for. gameplay reasons
for that tool missing do not mean that we need to remove its use - if
you want a better solution then let people purchase it... or just smash
the mech- you saving their life and them being sad about their mech is
really funny
the original pr being marked as qol when that was a specific balance
change is very stupid

## Changelog
🆑
del: if you die in a mech you again don't automatically eject
/🆑

---
## [alpinelinux/aports](https://github.com/alpinelinux/aports)@[09c0c63ecf...](https://github.com/alpinelinux/aports/commit/09c0c63ecf22730ee760523fa9f0ac3c3dcf2411)
#### Saturday 2023-12-09 13:26:54 by lauren n. liberda

community/chromium: upgrade to 120.0.6099.71

and a fuckton of other changes.
* chromium can no longer be built without non-trivial patches GCC.
  also it can't be built with clang with libstdc++. now instead of
  patching shit until it builds with libstdc++ we have to bundle libcxx.
  this breaks unbundling of the dependencies exposing APIs with C++ std types,
  like std::string or std::vector.
* otoh, unbundling more of what's possible now. it built on my machine instead
  of throwing std::bad_alloc at the end, so I guess this works.
* reorganized patches. more reuse from gentoo, patches over same file merged.

---
## [foxymegneil/f13babylon](https://github.com/foxymegneil/f13babylon)@[2f8b621240...](https://github.com/foxymegneil/f13babylon/commit/2f8b62124081d83f1dc9ee4085e0365a33a4bb2f)
#### Saturday 2023-12-09 13:53:11 by K4rlox

Chruch PR, attempt 3 to fix merge coflict (#249)

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

this PR works on redesigning, and moving the warren church to bighorn

![2023-11-24 13 33
01](https://github.com/f13babylon/f13babylon/assets/118483925/f9e8cb97-cdb1-46b7-950a-4c0364fad0a8)

![2023-11-24 13 33
20](https://github.com/f13babylon/f13babylon/assets/118483925/3ee346c1-c788-4c87-8e9b-31381030bc31)


the preacher already is considered a bighorn citizen so the church being
in warren used to make no sense

this fixes the issue and adds a few additional community requested
changes


this is a second attempt because the last one was closed because of a
item that crashed the server that i forgot to mention in changelogs


### **please if you want something changed then say it**
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

Preacher is supposed to be a citizen of bighorn therefore have a church
in bighorn, but they for some reason had a church in warren instead of
bighorn, i have heard some community members arguing about it and
decided to act on it as it only makes sense for the church to be
somewhere close to bighorn instead of in warren.

adds more items for the priest to use, adds an actual spawning landmark
for the priest to spawn in the church instead of a random matrix

adds several other misc items such as a angel food cake, a holy water
bottle, bread, wine, and several spare bibles

oh also gives the preacher closet a shotgun with no ammo, since the
preacher landmark seems to have a shotgun icon.

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
add: church in (front of) bighorn
add: bible, bread, wine and water crate
add: holy water flask
add: angel food cake
add: Priest shotgun (with no ammo)
add: Preacher starter landmark
add: water bottles
tweak: changes the bible on the table to the whiskey bible
fix: fixes the prayer breads not working

/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [foxymegneil/f13babylon](https://github.com/foxymegneil/f13babylon)@[f996624f34...](https://github.com/foxymegneil/f13babylon/commit/f996624f34bd17872783cf0757300c93cc116f38)
#### Saturday 2023-12-09 13:53:11 by foxymegneil

Enclave Marineification (#251)

## About The Pull Request

Changes all the icons and items of Enclave enlisted rank tabs (officer
tabs are the same between the Army and Marines) to be that of the Marine
Corps, while also adding some new ones that can be used for RP or
whatever. Also appropriately hands out said tabs. Private tab is GONE,
because it doesn't exist in the Marine Corps. You also may notice a
Petty Officer Third Class tab. What's that for? Well, it was originally
going to be for the Navy Corpsman loadout for the Specialist, however
loadouts seem to suffer with terminally low storage, so I wasn't able to
fit a rank tab into either of the loadouts. The item and icon are being
left in, however, just in case someone smarter than me can fix it.

Anyway, here are the sprites:

![sprites](https://github.com/f13babylon/f13babylon/assets/85942538/8b239726-1efb-43d3-a15d-731453df4a30)

## Why It's Good For The Game

We're Marines now! To hell with those Army tabs!
It's more immersive, and gosh darn it, that's all we Enclave players
have left. Immersion.

## Pre-Merge Checklist
- [x] You tested this on a local server.
- [x] This code did not runtime during testing.
- [x] You documented all of your changes.


## Changelog


:cl:
add: Adds some brand new Marine Corps tabs.
del: Old Army tabs that aren't needed anymore.
tweak: Changes some of the old tabs to new ones.
imageadd: New tabs!
imagedel: Old ones are gone.
/:cl:

---
## [Thryrallo/ThryEditor](https://github.com/Thryrallo/ThryEditor)@[d0ddbc9617...](https://github.com/Thryrallo/ThryEditor/commit/d0ddbc9617d28c07be47f61a4ba45687e3bc4864)
#### Saturday 2023-12-09 14:14:58 by Thryrallo

v2.47.3

- i dont even know, i wanna cry, why does unity do this shit. this is so random. i dont get it, what was wrong? Did EditorStyle not exist during constructor call times? If so why is that not a problem in unity 2019? Is the warning ignored or did the unity team fuck up. Please, this is purgetory, why is unity so cursed ;(

---
## [Ben10Omintrix/tgstation](https://github.com/Ben10Omintrix/tgstation)@[e9f12be172...](https://github.com/Ben10Omintrix/tgstation/commit/e9f12be1724e4b711df54f35cc117dca0a3aa07d)
#### Saturday 2023-12-09 14:16:28 by Higgin

Changes Virology Rather Than Killing It (#79854)

## About The Pull Request
God, alright, here we go. See HackMD here:
https://hackmd.io/@Higgin/HJljdBuNp

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

---
## [specificlanguage/AdventOfCode23](https://github.com/specificlanguage/AdventOfCode23)@[1c93496fe3...](https://github.com/specificlanguage/AdventOfCode23/commit/1c93496fe37e80426015180fc43f88e8fa212329)
#### Saturday 2023-12-09 15:17:32 by specificlanguage

Day 9

Another algorithm based challenge today, this time just looking at diffs between numbers. Honestly these aren't looking too bad anymore as we start to dip into algorithm territory and things start to be less about file processing. I had time to worry about efficiency today and think about how fast my code runs, which to be fair, is good but not amazing. In the end though, it doesn't really matter, as the solutions for these was pretty self explanatory, as it just requires recursion to find diffs and return the answer back up.

---
## [kytta/zola](https://github.com/kytta/zola)@[b5a90dba5d...](https://github.com/kytta/zola/commit/b5a90dba5d12ea6760c3aa18fec40f8af4d7cbc7)
#### Saturday 2023-12-09 15:34:19 by sinofp

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
## [Huawei-Dev/android_kernel_huawei_beethoven](https://github.com/Huawei-Dev/android_kernel_huawei_beethoven)@[4b32ec715c...](https://github.com/Huawei-Dev/android_kernel_huawei_beethoven/commit/4b32ec715c8b35481ef519c94c0ff7ba775dbf76)
#### Saturday 2023-12-09 16:09:50 by Dave Chiluk

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
Change-Id: I7d7a39fb554ec0c31f9381f492165f43c70b3924
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

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[16bdcf409c...](https://github.com/tgstation/tgstation/commit/16bdcf409c5d6eb3d846b16f4968849e26cf833c)
#### Saturday 2023-12-09 16:15:21 by Rhials

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
## [Touhou-13/Assistant-Daisensou-Touhou-13](https://github.com/Touhou-13/Assistant-Daisensou-Touhou-13)@[0304282fb9...](https://github.com/Touhou-13/Assistant-Daisensou-Touhou-13/commit/0304282fb9581bf6d3a3c2a0eeb9d06ba71e93d3)
#### Saturday 2023-12-09 16:20:11 by SkyratBot

[MIRROR] Blood brothers is now a single person conversion antagonist [MDB IGNORE] (#25338)

* Blood brothers is now a single person conversion antagonist (#79971)

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

* Blood brothers is now a single person conversion antagonist

* Update oneclickantag.dm

---------

Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>
Co-authored-by: Giz <13398309+vinylspiders@users.noreply.github.com>

---
## [waschik/go-httpbin](https://github.com/waschik/go-httpbin)@[0de8ec9683...](https://github.com/waschik/go-httpbin/commit/0de8ec968378e7385f2f9b10b6fe7a035fb27d8e)
#### Saturday 2023-12-09 16:33:34 by Will McCutchen

Refactor test suite to make real requests to a real server (#131)

In the course of validating #125, we discovered that using the stdlib's
[`httptest.ResponseRecorder`][0] mechanism to drive the vast majority of
our unit tests led to some slight brokenness due to subtle differences
in the way those "simulated" requests are handled vs "real" requests to
a live HTTP server, as [explained in this comment][1].

That prompted me to do a big ass refactor of the entire test suite,
swapping httptest.ResponseRecorder for interacting with a live server
instance via [`httptest.Server`][2].

This should make the test suite more accurate and reliable in the long
run by ensuring that the vast majority of tests are making actual HTTP
requests and reading responses from the wire.

Note that updating these tests also uncovered a few minor bugs in
existing handler code, fixed in a separate commit for visibility.

P.S. I'm awfully sorry to anyone who tries to merge or rebase local test
changes after this refactor lands, that is goign to be a nightmare. If
you run into issues resolving conflicts, feel free to ping me and I can
try to help!

[0]: https://pkg.go.dev/net/http/httptest#ResponseRecorder
[1]: https://github.com/mccutchen/go-httpbin/pull/125#issuecomment-1596176645
[2]: https://pkg.go.dev/net/http/httptest#Server

---
## [DharadePravin84/30DaysMLChallenge](https://github.com/DharadePravin84/30DaysMLChallenge)@[328673a07c...](https://github.com/DharadePravin84/30DaysMLChallenge/commit/328673a07cb25e3546d933a25298f4be1cbf463d)
#### Saturday 2023-12-09 16:54:25 by Pravin Dharade

Add files via upload

🚀 Logistic Regression on Dazzling Digits!

Objective:
Embarked on a pixel-perfect journey, crafting a Logistic Regression model to decipher the magic of handwritten digits using the enchanting Digits dataset.

Key Steps:

Data Exploration:

Unveiled the hidden world of digits, exploring a dataset filled with 64 features of mystical scribbles (0-9).
Glimpsed into the data's essence and conjured vibrant visualizations of spellbinding images.
Model Training:

Split the data like a wizard into training and testing realms.
Wielded the power of Logistic Regression, casting spells to achieve a staggering 95.11% accuracy on the test set.
Model Evaluation:

Whispered predictions for each digit, unraveling the secrets of the unseen.
Unveiled the Confusion Matrix—a treasure map revealing accuracy gems for specific digits.
Visualization:

Painted a canvas of enchantment with heatmaps and graphical representations, bringing the magic to life.
Insights:
The Logistic Regression sorcery demonstrated its might, recognizing handwritten wonders with an accuracy spell. The Confusion Matrix illuminated paths to deeper understanding.

Next Steps:
Stay enchanted on this magical journey! Future spells include refining models, unveiling new datasets, and delving into the mysteries of advanced ML concepts.

Keep the magic alive in my 30-day ML challenge adventure! ✨📊

#MachineLearning #LogisticRegression #DataWizardry #ProjectDay6 #DataScience

---
## [vvvv-vvvv/TerraGov-Marine-Corps](https://github.com/vvvv-vvvv/TerraGov-Marine-Corps)@[54de75d4a2...](https://github.com/vvvv-vvvv/TerraGov-Marine-Corps/commit/54de75d4a29d2cfa3f43afe8a713e75824f7d985)
#### Saturday 2023-12-09 17:02:58 by John Willard

PDA update (Messenger works while dead, Microwave works, etc). (#80069)

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
(cherry picked from commit edbc7c562261e95d58140463ed6a1a23102fc2f3)

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[54ab1e3936...](https://github.com/tgstation/tgstation/commit/54ab1e3936b3d5a301b995f2c1ca14fcdaf3e80d)
#### Saturday 2023-12-09 17:50:48 by Time-Green

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
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[8d77b1be89...](https://github.com/tgstation/tgstation/commit/8d77b1be89f771391c5697a1a3ac180f68cd6858)
#### Saturday 2023-12-09 17:54:20 by necromanceranne

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
## [vvvv-vvvv/TerraGov-Marine-Corps](https://github.com/vvvv-vvvv/TerraGov-Marine-Corps)@[e70d873904...](https://github.com/vvvv-vvvv/TerraGov-Marine-Corps/commit/e70d87390433d411e975b3aa3512b15e77e73fd0)
#### Saturday 2023-12-09 18:50:23 by san7890

Fixes sending stuff to "Old" Chat (#79819)

## About The Pull Request

This functionality was removed in #79479
(e1c6cfdce89c7dbcd507d0c44803f5407a042a96), and we should still be
supporting the old chat anyways because it contains a plethora of useful
BYOND information that we still can really leverage (such as the
built-in profiler and stuff like that) and it's going to be painful to
do that if you have to keep spamming `fix-chat` to see OOC/ASAY while
alternating every damn time.
## Why It's Good For The Game

It's ugly but we still need it. There's a reason why we still have it.
## Changelog
:cl:
fix: "Old Chat" (AKA: The old-styled non-TGUI raw-HTMLesque chat that
you might see when it prods you with the "Failed to load fancy chat!"
issue) should now get all text messages as expected.
/:cl:

(cherry picked from commit eb246c21f6eb5380dc56e5779fcd51d11437557c)

---
## [wrye-bash/wrye-bash](https://github.com/wrye-bash/wrye-bash)@[95608111aa...](https://github.com/wrye-bash/wrye-bash/commit/95608111aaf6242d543ff3fc81abc1f629931c5a)
#### Saturday 2023-12-09 19:23:33 by MrD

Squashed version of ut-353-pt1-578:

Refactoring in load order: TTT EEE lowercase todoS

Move  the logic of _filter_active in callers - they were doing the checks
anyways - then inline - we certainly want to thin LoGame API, _games_lo
is complex enough and flat is better (and shorter) than nested here.

_CleanPlugins(LoGame):

Clean/create logic is very hard to follow - let's confine it to games that
need it. We then need to clarify what happens with cached parameters vs
creating the plugins txt

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
use)

quiet WIP:  EEE fix_load_order override

get_load_order had quiet=False effectively - added this as default to
fix_load/active and then in set_load_order quiet=True and set it only
in load_order.save_lo

Became clear that warn_missing_lo_act was only updated when quiet was
False which was when lo_deprint was called. This simplified the guts
of _game_lo at the expense of a local modInfos import - good.
Not sure about the _fix_load_order override - if fix_lo was None which
only happened in _restore_lo (quiet=True), it would not reorder the added
plugins but add them to the end - do we want that? I dropped the debug
message as anyway the lo_added will be printed.

Expose more LoadOrder attributes:

The index dicts contain all the info of load order/active changes - as
a bonus a couple one-line, one-use methods were removed. load_order.py
is the balt of load order handling and although (because of saved load
order handling) it does have a well defined role it still needs to be
kept at a minimum - more on this later.

TTT simplify/optimize _refresh_mod_inis

No need to clean up since we overwrite at the end - pruned also the OD.

Only the values of _plugin_inis was used - simplify and make easier to
track by exposing it and removing essentially no op ini_files (not the
.py module)

WIP refactor BP activations handling: EEE remove todo

count would decide on refreshing saves - probably if any mods got
activated we should DO. Moved the info handling higher up, I need to do
activations in parent.

Reduce occurrences of lo_activate (2)/cached_lo_save_active (1) - these
must be further confined. Note the decoupling from load_order (and Link)
in patcher_dialog.py

_modTimesChange -> unlock_lo TTT

Was unlocking in all except one case TTT - in those cases unlocking made
only sense if the game was a timestamp game - I am glad I kept
_modTimesChange and gladder I dropped it

Stashing a [!] as there are subtle changes in the logic - note that:

Mopy/bash/basher/mod_links.py: we wouldn't unlock - wouldn't that revert
the redates TTT?
Mopy/bash/basher/app_buttons.py: while we did unlock always we did not
forceRefresh - well it's a couple stats(), won't harm

The rest is fine - just one more use of using_txt_file, inside the same (DoSave)
scope - good sign.

Mopy/bash/basher/installers_links.py: the (not so) long term goal is to absorb
this into refresh - need to refactor base signature for this.

XXX FFF?+            forceActive=deleted or unlock_lo, unlock_lo=unlock_lo)

Mopy/bash/gui/popups.py: user_ok was essentially unused, was checked in show_modal

WIP setGhost return status change: RRR TTT drop notify bain?

This gets us rid of a few uglyStuff including a Path method (# RRR 368), and
one bare except - we might as well deprint out (and maybe tighten the
remaining except).

As seen in _refresh_from_data_dir we chop off the ghost extension so we
should not notify BAIN TTT cause data_sizeCrcDate is difficult to track,
hence WIP see next commit

Under # 219

isGhost -> is_ghost:

Now that autoGhost is (will) be gone

Some nit - in particular no need to create these (None, None, None) tuples

More undead pruning: TTT

Including one more modInfos local import - typing is badly needed here

Drop _reset_info_sets: TTT

Finally, this set up was a smell. This makes some calls like new_info
more expensive but no worries

TTT new_info: the _in_refresh param is obviously a temp hack :P

---
## [MonstieHuntie/Monkestation2.0](https://github.com/MonstieHuntie/Monkestation2.0)@[dcd9a1cf02...](https://github.com/MonstieHuntie/Monkestation2.0/commit/dcd9a1cf02f9460648c7bd9bb1624080c3deb303)
#### Saturday 2023-12-09 19:29:06 by MonstieHuntie

Refactors stripe ripping + Adds cooldown to prevent abuse + cleaner description edits

I completely rewrote how ripping the stripe off the Paco works, decreasing end-user jank infinitely. Now, instead of releasing the mag (into your hand), racking the slide, and completely deleting the original gun and replacing it with a brand new stripeless variant (HOLY MOTHER OF JANK)... It now uses a series of update methods to PROPERLY change the sprites and inhand of the Paco without having to do any convoluted bullshittery (say goodbye to Paco/Stripeless!).

Also incorporates a cooldown to stop players from potentially spamming the AltClick feature to annoy their peers.

Cleans up how updating the description based on if it was a Taco or Stripeless gun. Instead of replacing the description with a new one, it appends a new sentence to it. That means that, if you have a rare Taco edition and decide to rip the stripe off, the fancy description won't disappear, joy!

---
## [yogstation13/Yogstation](https://github.com/yogstation13/Yogstation)@[5c140d7624...](https://github.com/yogstation13/Yogstation/commit/5c140d7624b7b9f904d5bd78602d2fb0ee33a9ec)
#### Saturday 2023-12-09 19:33:00 by Aquizit

[ICEMETA] Fixes Hermit and Walker Spawns (Walkers disabled in config see PR text) (#21065)

* name + config fixes

* fix walker - disabled, redo hermit flavor text

* fuck your stupid uncapitalized t

---
## [dtdimi/ms-terminal](https://github.com/dtdimi/ms-terminal)@[86fb9b4478...](https://github.com/dtdimi/ms-terminal/commit/86fb9b44787accd09c5943a506e27eb4c8e573c0)
#### Saturday 2023-12-09 19:39:11 by Dustin L. Howett

Add a magic incantation to tell the Store we support Server (#16306)

I find it somewhat silly that (1) this isn't documented anywhere and (2)
installing the "desktop experience" packages for Server doesn't
automatically add support for the `Windows.Desktop` platform...

Oh well.

I'm going to roll this one out via Preview first, because if the store
blows up on it I would rather it not be during Stable roll-out.

---
## [Time-Green/tgstation](https://github.com/Time-Green/tgstation)@[ef52047274...](https://github.com/Time-Green/tgstation/commit/ef520472740e57f253545c24c7526e45e47b5ec2)
#### Saturday 2023-12-09 20:17:18 by necromanceranne

[READY] The Tackleling: Unarmed bonuses and features contribute to tackle success and failure, significant outcome overhaul, among other things (#79721)

## About The Pull Request

### Tackling Outcomes

Tackling now determines success based on outcome categories. These are
derived from the typical attacker/defender roll that would have
previously determined the outcome on its own. A negative roll results in
a negative outcome, a positive roll a positive outcome, and a result of
exactly 0 resulting in a neutral outcome.

The result of your roll are then passed along to the relevant proc to
determine severity. The derived roll is multiplied by 10 (or -10 for the
negative roll to get a positive value to roll with). Then we see if our
final roll fits a severity bracket. Negative outcomes will roll to
determine their outcome, and potentially could roll a less severe
outcome than what our first roll would suggest.

For positive outcomes, the defender's melee armor reduces the severity
of the outcome.
For negative outcomes, the attacker's melee armor improves the potential
outcome and at least prevents more severe backlash. It'll still be
negative, you can't move from a negative outcome to a positive outcome
just from good armor.

Most of the outcomes are fairly similar to the current outcomes, but
with the inclusion of staggering one or both parties to make the
subsequent potential grabs _stickier_, if that makes sense.

Neutral is now a mutual stagger, but also the tackler being left
upright. It's effectively net zero.

### Blocking

Blocking is checked on impact, and results in a neutral outcome if the
defender successfully blocks. This means our tackler isn't too severely
impacted from an unsuccessful tackle

### Additional Changes

Your arms ``unarmed_effectiveness`` now contributes to the attack mod
and defense mod of tackles. For humans tackling humans, this often
results in a net neutral result. But if you have a better arm, or the
tackle target has worse arms, this can alter the outcome significantly.

Any tackler with the trait TRAIT_NOGUNS (like bezerkers, Sleeping Carp
users or the very unlikely chance ninjas are tackling while wearing
their armor) gains a bonus to their tackles.

Any suit that prevents shove knockdowns grants an attack bonus, and not
just riot armor. This now includes Mk.1 Swat suits, the ones from the
SWAT crate in cargo.

Settlers are vulnerable to tackles, much like their dwarf cousins.
They're also just as bad at tackles.

Security lockers come with gripper gloves, and the sec vendor has 5 sets
of gripper gloves as standard items. They also have a +1 skill bonus.
This should encourage people to use tackling a bit more without having
to always seek out the best gear to accomplish the task. (particularly
since security is inherently pretty good at tackling with the outcome
changes).

The HoS gets a pair of gorilla gloves in his garment bag. If he wants
them.

The shove slowdown is now a new status effect, Staggered. This is just
better functionality overall. Any instance of adding the shove slowdown
now makes our target staggered.

## Why It's Good For The Game

Tackling is a bit outdated, to say the least. Not much content has been
added for a while that isn't strictly meme content. With these changes,
tackling should be slightly more nuanced, considering elements such as
unarmed effectiveness, the presence of martial arts, and actually
properly checking block rather than notionally checking block. There is
also more opportunity to protect yourself from tackle outcomes, both
positive and negative.

It also should be a little fairer to be on the receiving end of tackles
if you have taken the time to layer up defenses against it. Attackers
often overwhelmed defenders due to numbers favoring attackers more than
defenders.

Closes some really outdated design that was resulting in some really
bizarre behaviour with regards to layered defenses against attack not
having the same meaning against tackles, if only because it was looking
for the wrong things and not even the correct parts of what it was
looking for. Namely, blocking and shielding.

The inclusion of more gripper gloves and a good outcome from using them
will hopefully incentivize people to consider tacking as a useful tool,
if a bit risky still due to the splat mechanics.

## Changelog
:cl:
balance: Judo Joe, archnemesis of Maint Khan, has begun re-airing his
midnight infomercials shilling his extremely expensive Tackle Supreme
Judo Karate Training video tapes. Unable to pass up a 'bargain',
Nanotrasen has purchased these tapes en masse. Tackling techniques have
started to improve, as well as Nanotrasen's tackling instructional
algorithms within tackle gloves.
balance: The outcomes for tackling are more equalized. It isn't as feast
or famine, and should be somewhat more controllable without becoming too
severe.
add: Blocking successfully against a tackle will force the tackle to be
a neutral outcome.
add: Unarmed effectiveness from arms now contributes to attacking with
and defending from tackles.
add: Those who refuse to use firearms (like Sleeping Carp users and
insane unholy berzerkers) are better at tackling others.
add: Riot specialized armor, and not just riot armor, now contributes
meaningfully to tackling effectiveness.
balance: MK.1 Swat Suits, the ones that come in SWAT crates, now
functions similarly to riot armor.
add: Settlers from the outer rims have noticed they aren't very good at
protecting themselves against Judo Joe's clearly discriminatory tackling
techniques.
add: Security lockers come with gripper gloves, security vendors now
sell them as standard items, and the HoS' garment bag now has a pair of
gorilla gloves. Gripper gloves have a positive skill bonus to tackling.
add: Being insane also makes you INSANELY good at tackling but also
INSANELY likely to eat shit on a whiff. DO OR DIE, BITCH.
refactor: Shoving slowdown and all its implementations now use a status
effect, Staggered.
/:cl:

---
## [roguh/confs-1](https://github.com/roguh/confs-1)@[22877d82ce...](https://github.com/roguh/confs-1/commit/22877d82ced1dd8e1640b02e0e24c70db733a87f)
#### Saturday 2023-12-09 20:23:14 by FeLiNa0

Moar ollama

ollama run mistral "Tell me a story about a talking pumpkin named Lily"
Once upon a time, in the heart of a small autumnal village, there was a magnificent pumpkin patch. The pumpkins were orange and round, with smooth faces and big personalities. They would bask in the sun during the day and glow softly under the moon at night. Among them all, there was one special pumpkin named Lily.

Lily was not like the other pumpkins. For one thing, she could talk. Every day, she would greet the villagers with a cheerful “Good morning!” or bid them farewell with a warm “Goodnight!” As the village’s only talking pumpkin, Lily was quite the sensation. People would come from miles around just to hear her speak.

One day, a little girl named Emma came to visit the pumpkin patch. She was fascinated by all the colorful pumpkins, but it was Lily who caught her eye. Emma had heard stories about the talking pumpkin and was eager to meet her. When she finally came face to face with Lily, she was amazed.

“Hello, Lily!” Emma said shyly. “I’m Emma. I’ve heard so much about you.”

Lily smiled and replied, “Well, hello there, Emma! It’s nice to meet you too. What brings you to the pumpkin patch today?”

Emma told Lily all about her love for Halloween and how she was getting ready for the big day. She asked Lily if she had any advice on how to make the scariest costume ever. Lily thought for a moment, and then came up with a brilliant idea.

“Why not try something different this year?” Lily suggested. “Instead of a typical scary costume, why don’t you dress up as a friendly pumpkin like me? People will be surprised and delighted by your unique choice.”

Emma loved the idea! She thanked Lily for her suggestion and promised to give it a try. From that day on, Emma became known as the friendly pumpkin girl, and every Halloween, she would return to the pumpkin patch to see her dear friend Lily.

Years passed, and Lily grew old, but she never lost her ability to bring joy to others. Even in her final days, she remained a beacon of hope and happiness in the village, reminding everyone that sometimes, the most unexpected things can lead to the greatest adventures. And so, the legend of the talking pumpkin named Lily lived on, inspiring generations to come.

---
## [riverqueue/river](https://github.com/riverqueue/river)@[299a43bcc1...](https://github.com/riverqueue/river/commit/299a43bcc113521907bb42724a0e8ebd63761de3)
#### Saturday 2023-12-09 20:48:43 by Brandur

Put River CLI into its own submodule

Background: While trying to figure out how to safely release [1]
(which includes a new `riverdriver` submodule), I threw myself through a
loop and realized that it'd be practically impossible to do without a
whole bunch of manual finnagling on the release tags/lint settings in
the repo, or breaking the master build, or most likely, both.

This got me thinking: maybe we should, maybe we _should_ be using
`replace` directives to make this less painful/brittle, which were
originally removed in #35 because using `replace` makes it impossible to
use `go install ...@latest`.

A change that we made recently was the addition of a new Go migration
API in #65 (`rivermigrate`), and a side effect of that change is that
the API being used by the River CLI became entirely public (previously,
it'd depended on packages in River's `internal`). By extension, that
means it's now possible to make the River CLI its own Go module,
something that was infeasible before because of the use of `internal`.

So my thinking currently: maybe we should go back to trying to see if we
can make `replace` in use by most of River's core packages, and keep the
River CLI as its own module without `replace` so that it can still be
installed with `go install ...@latest`. I'm not entirely sure we won't
run into another problem, but it might be the easiest thing in the
meantime. As the River CLI expands, we'll need to make sure to only use
public APIs, but that might not be the worst thing anyway -- we could
adopt the philosophy that any function the CLI accesses should also be
accessible by the Go API.

Here, notably we still use a `replace`, which I'm finding that I need to
have a passing build for now, and which I think will have to temporarily
stay until we cut a new release. Trying to build the new submodule
without results in this error that I was unable to otherwise find a way
around:

    $ go test .
    ambiguous import: found package github.com/riverqueue/river/cmd/river in multiple modules:
            github.com/riverqueue/river v0.0.12 (/Users/brandur/Documents/go/pkg/mod/github.com/riverqueue/river@v0.0.12/cmd/river)
            github.com/riverqueue/river/cmd/river (/Users/brandur/Documents/projects/river/cmd/river)

[1] https://github.com/riverqueue/river/pull/98

---
## [panzerr1944/f13tbd](https://github.com/panzerr1944/f13tbd)@[ca10da3eef...](https://github.com/panzerr1944/f13tbd/commit/ca10da3eef6fa77eeae67bc9a92a5eebbc7eec5e)
#### Saturday 2023-12-09 21:25:47 by panzerr1944

Big Fix and Edit Commit

All edits are from the following list;
Remove the 2 unique spawns on the surface/underground that can be rushed
Remove the 'Left Hand' riot shotgun force-spawner
Add more carpiles in the main map so people stop rushing the Warren
Give the Raiders a minidungeon for books 1-3, since everyone else gets it now it seems
Fix-up the new Kebab Town (i.e- make it far harder, mostly mob edits to help with such as mob ai for renegades here sucks)
Remove the followers Reagent Gun (AGAIN. I did this before and someone RE-MAPPED IT IN.)
Remove that one dumb as shit rad-puddle from infront of the BOS base
Remove the force-spawn gauss rifle in no mans land (edit a different spawner to include it without throwing in another unique or superhigh spawner)
Bodybags for followers
Edit the E-Weapon spawners to the following:
Low = AEP7, Wattz, (low chance) Wattz Magneto (someone made the AEP7  midtier for some bullshit reason)
Mid = AER9, Plaspistol, (low chance) Wattz 2k
Mid-High = AER12, AER9, (low chance) Ion Rifle
High = Plasrifle, Wattz 2kE, RCW, Tribeam,(low chance) AER14
Edit the Experimental Spawner to the following:
M72 Gauss, Peacekeeper, XL7, P90, Gatling Laser
Edit the Peacekeepers stats
Apply auto-fire shot delay of 2.8
Fix the Remnant Bunker shoot-through wall things
Fix BOS NML entrance

---
## [riverqueue/river](https://github.com/riverqueue/river)@[6bd17d475d...](https://github.com/riverqueue/river/commit/6bd17d475dd0d2ff933e638e8620cbac2c0a2848)
#### Saturday 2023-12-09 22:36:42 by Brandur

Support for `database/sql` in migrations + framework for multi-driver River

Here, add a new minimal driver called `riverdriver/riversql` that
supports Go's built-in `database/sql` package, but only for purposes of
migrations. The idea here is to fully complete #57 by providing a way of
making `rivermigrate` interoperable with Go migration frameworks that
support Go-based migrations like Goose, which provides hooks for
`*sql.Tx` [1] rather than pgx.

`riverdriver/riversql` is not a full driver and is only meant to be used
with `rivermigrate`. We document this clearly in a number of places.

To make a multi-driver world possible with River, we have to start the
work of building a platform that does more than `riverpgxv5`'s "cheat"
workaround. This works by having each driver implement specific database
operations like `MigrationGetAll`, which target their wrapped database
package of choice.

This is accomplished by having each driver bundle in its own sqlc that
targets its package. So `riverpgxv5` has an `sqlc.yaml` that targets
`pgx/v5`, while `riversql` has one that targets `database/sql`. There's
some `sqlc.yaml` duplication involved here, but luckily both drivers can
share a `river_migration.sql` file that contains all queries involved,
so you only need to change one place. `river_migration.sql` also migrates
entirely out of the main `./internal/dbsqlc`.

The idea here is that eventually `./internal/dbsqlc` will disappear
completely, usurped entirely by driver-specific versions. As this is
done, all references to `pgx` will disappear from the top-level package.
There are some complications here to figure out like `LISTEN`/`NOTIFY`
though, and I'm not clear whether `database/sql` could ever become a
fully functional driver as it might be missing some needed functionality
(e.g. subtransactions are still not supported after talking about them
for ten f*ing years [2]. However, even if it's not, the system would let
us support other fully functional packages or future major versions of
pgx (or even past ones like `pgx/v4` if there's demand).

`river/riverdriver` becomes a package as it now has types in it that
need to be referenced by driver implementations, and this would
otherwise not be possible without introducing a circular dependency.

Notably, this development branch has to use some `go.mod` `replace`
directives to demonstrate that it works correctly. If we go this
direction, we'll need to break it into chunks to release it without
them:

1. Break out changes to `river/riverdriver`. Tag and release it.

2. Break out changes to `riverdriver/river*` drivers. Have them target
   the release in (1), comment out `replace`s, then tag and release them.

3. Target the remaining River changes to the releases in (1) and (2),
   comment out `replace`s, then tag and release the top-level driver.

Unfortunately future deep incisions to drivers will require similar
gymnastics, but I don't think there's a way around it (we already have
this process except it's currently two steps instead of three). The hope
is that these will change relatively rarely, so it won't be too painful.

[1] https://github.com/pressly/goose#go-migrations
[2] https://github.com/golang/go/issues/7898

---
## [piratecash/pirate](https://github.com/piratecash/pirate)@[7267b8cdff...](https://github.com/piratecash/pirate/commit/7267b8cdffccbc84d6f246c966610c2f0ceb54af)
#### Saturday 2023-12-09 23:17:52 by Wladimir J. van der Laan

Merge #15277: contrib: Enable building in Guix containers

751549b52a9a4cd27389d807ae67f02bbb39cd7f contrib: guix: Additional clarifications re: substitutes (Carl Dong)
cd3e947f50db7cfe05c05b368c25742193729a62 contrib: guix: Various improvements. (Carl Dong)
8dff3e48a9e03299468ed3b342642f01f70da9db contrib: guix: Clarify SOURCE_DATE_EPOCH. (Carl Dong)
3e80ec3ea9691c7c89173de922a113e643fe976b contrib: Add deterministic Guix builds. (Carl Dong)

Pull request description:

  ~~**This post is kept updated as this project progresses. Use this [latest update link](https://github.com/bitcoin/bitcoin/pull/15277#issuecomment-497303718) to see what's new.**~~

  Please read the `README.md`.

  -----

  ### Guix Introduction

  This PR enables building bitcoin in Guix containers. [Guix](https://www.gnu.org/software/guix/manual/en/html_node/Features.html) is a transactional package manager much like Nix, but unlike Nix, it has more of a focus on [bootstrappability](https://www.gnu.org/software/guix/manual/en/html_node/Bootstrapping.html) and [reproducibility](https://www.gnu.org/software/guix/blog/tags/reproducible-builds/) which are attractive for security-sensitive projects like bitcoin.

  ### Guix Build Walkthrough

  Please read the `README.md`.

  [Old instructions no. 4](https://github.com/bitcoin/bitcoin/pull/15277#issuecomment-497303718)

  [Old instructions no. 3](https://github.com/bitcoin/bitcoin/pull/15277#issuecomment-493827011)

  [Old instructions no. 2](https://github.com/bitcoin/bitcoin/pull/15277#issuecomment-471658439)

  <details>
  <summary>Old instructions no. 1</summary>
  In this PR, we define a Guix [manifest](https://www.gnu.org/software/guix/manual/en/html_node/Invoking-guix-package.html#profile_002dmanifest) in `contrib/guix/manifest.scm`, which declares what packages we want in our environment.

  We can then invoke
  ```
  guix environment --manifest=contrib/guix/manifest.scm --container --pure --no-grafts --no-substitutes
  ```
  To have Guix:
  1. Build an environment containing the packages we defined in our `contrib/guix/manifest.scm` manifest from the Guix bootstrap binaries (see [bootstrappability](https://www.gnu.org/software/guix/manual/en/html_node/Bootstrapping.html) for more details).
  2. Start a container with that environment that has no network access, and no access to the host's filesystem except to the `pwd` that it was started in.
  3. Drop you into a shell in that container.

  > Note: if you don't want to wait hours for Guix to build the entire world from scratch, you can eliminate the `--no-substitutes` option to have Guix download from available binary sources. Note that this convenience doesn't necessarily compromise your security, as you can check that a package was built correctly after the fact using `guix build --check <packagename>`

  Therefore, we can perform a build of bitcoin much like in Gitian by invoking the following:

  ```
  make -C depends -j"$(nproc)" download && \
      cat contrib/guix/build.sh | guix environment --manifest=contrib/guix/manifest.scm --container --pure --no-grafts --no-substitutes
  ```

  We don't include `make -C depends -j"$(nproc)" download` inside `contrib/guix/build.sh` because `contrib/guix/build.sh` is run inside the container, which has no network access (which is a good thing).
  </details>

  ### Rationale

  I believe that this represents a substantial improvement for the "supply chain security" of bitcoin because:

  1. We no longer have to rely on Ubuntu for our build environment for our releases ([oh the horror](https://github.com/bitcoin/bitcoin/blob/72bd4ab867e3be0d8410403d9641c08288d343e3/contrib/gitian-descriptors/gitian-linux.yml#L10)), because Guix builds everything about the container, we can perform this on almost any Linux distro/system.
  2. It is now much easier to determine what trusted binaries are in our supply chain, and even make a nice visualization! (see [bootstrappability](https://www.gnu.org/software/guix/manual/en/html_node/Bootstrapping.html)).
  3. There is active effort among Guix folks to minimize the number of trusted binaries even further. OriansJ's [stage0](https://github.com/oriansj/stage0), and janneke's [Mes](https://www.gnu.org/software/mes/) all aim to achieve [reduced binary boostrap](http://joyofsource.com/reduced-binary-seed-bootstrap.html) for Guix. In fact, I believe if OriansJ gets his way, we will end up some day with only a single trusted binary: hex0 (a ~500 byte self-hosting hex assembler).

  ### Steps to Completion

  - [x] Successfully build bitcoin inside the Guix environment
  - [x] Make `check-symbols` pass
  - [x] Do the above but without nasty hacks
  - [x] Solve some of the more innocuous hacks
  - [ ] Make it cross-compile (HELP WANTED HERE)
    - [x] Linux
      - [x] x86_64-linux-gnu
      - [x] i686-linux-gnu
      - [x] aarch64-linux-gnu
      - [x] arm-linux-gnueabihf
      - [x] riscv64-linux-gnu
    - [ ] OS X
      - [ ] x86_64-apple-darwin14
    - [ ] Windows
      - [ ] x86_64-w64-mingw32
  - [ ] Maybe make importer for depends syntax
  - [ ] Document build process for future releases
  - [ ] Extra: Pin the revision of Guix that we build with with Guix [inferiors](https://www.gnu.org/software/guix/manual/en/html_node/Inferiors.html)

  ### Help Wanted

  [Old content no. 3](https://github.com/bitcoin/bitcoin/pull/15277#issuecomment-483318210)

  [Old content no. 2](https://github.com/bitcoin/bitcoin/pull/15277#issuecomment-471658439)

  <details>
  <summary>Old content no. 1</summary>
  As of now, the command described above to perform a build of bitcoin a lot like Gitian works, but fails at the `check-symbols` stage. This is because a few dynamic libraries are linked in that shouldn't be.

  Here's what `ldd src/bitcoind` looks like when built in a Guix container:
  ```
  	linux-vdso.so.1 (0x00007ffcc2d90000)
  	libdl.so.2 => /gnu/store/h90vnqw0nwd0hhm1l5dgxsdrigddfmq4-glibc-2.28/lib/libdl.so.2 (0x00007fb7eda09000)
  	librt.so.1 => /gnu/store/h90vnqw0nwd0hhm1l5dgxsdrigddfmq4-glibc-2.28/lib/librt.so.1 (0x00007fb7ed9ff000)
  	libstdc++.so.6 => /gnu/store/4sqps8dczv3g7rwbdibfz6rf5jlk7w90-gcc-5.5.0-lib/lib/libstdc++.so.6 (0x00007fb7ed87c000)
  	libpthread.so.0 => /gnu/store/h90vnqw0nwd0hhm1l5dgxsdrigddfmq4-glibc-2.28/lib/libpthread.so.0 (0x00007fb7ed85b000)
  	libm.so.6 => /gnu/store/h90vnqw0nwd0hhm1l5dgxsdrigddfmq4-glibc-2.28/lib/libm.so.6 (0x00007fb7ed6da000)
  	libgcc_s.so.1 => /gnu/store/4sqps8dczv3g7rwbdibfz6rf5jlk7w90-gcc-5.5.0-lib/lib/libgcc_s.so.1 (0x00007fb7ed6bf000)
  	libc.so.6 => /gnu/store/h90vnqw0nwd0hhm1l5dgxsdrigddfmq4-glibc-2.28/lib/libc.so.6 (0x00007fb7ed506000)
  	/gnu/store/h90vnqw0nwd0hhm1l5dgxsdrigddfmq4-glibc-2.28/lib/ld-linux-x86-64.so.2 => /usr/lib64/ld-linux-x86-64.so.2 (0x00007fb7ee3a0000)
  ```

  And here's what it looks in one of our releases:
  ```
  	linux-vdso.so.1 (0x00007ffff52cd000)
  	libpthread.so.0 => /usr/lib/libpthread.so.0 (0x00007f87726b4000)
  	librt.so.1 => /usr/lib/librt.so.1 (0x00007f87726aa000)
  	libm.so.6 => /usr/lib/libm.so.6 (0x00007f8772525000)
  	libgcc_s.so.1 => /usr/lib/libgcc_s.so.1 (0x00007f877250b000)
  	libc.so.6 => /usr/lib/libc.so.6 (0x00007f8772347000)
  	/lib64/ld-linux-x86-64.so.2 => /usr/lib64/ld-linux-x86-64.so.2 (0x00007f8773392000)
  ```

  ~~I suspect it is because my script does not apply the gitian-input patches [described in the release process](https://github.com/bitcoin/bitcoin/blob/master/doc/release-process.md#fetch-and-create-inputs-first-time-or-when-dependency-versions-change) but there is no description as to how these patches are applied.~~ It might also be something else entirely.

  Edit: It is something else. It appears that the gitian inputs are only used by [`gitian-win-signer.yml`](https://github.com/bitcoin/bitcoin/blob/d6e700e40f861ddd6743f4d13f0d6f6bc19093c2/contrib/gitian-descriptors/gitian-win-signer.yml#L14)
  </details>

  ### How to Help

  1. Install Guix on your distro either [from source](https://www.gnu.org/software/guix/manual/en/html_node/Requirements.html) or perform a [binary installation](https://www.gnu.org/software/guix/manual/en/html_node/Binary-Installation.html#Binary-Installation)
  2. Try out my branch and the command described above!

ACKs for top commit:
  MarcoFalke:
    Thanks for the replies. ACK 751549b52a9a4cd27389d807ae67f02bbb39cd7f
  laanwj:
    ACK 751549b52a9a4cd27389d807ae67f02bbb39cd7f

Tree-SHA512: 50e6ab58c6bda9a67125b6271daf7eff0ca57d0efa8941ed3cd951e5bf78b31552fc5e537b1e1bcf2d3cc918c63adf19d685aa117a0f851024dc67e697890a8d

---
## [wraith-54321/Monkestation2.0](https://github.com/wraith-54321/Monkestation2.0)@[1e9edd6a49...](https://github.com/wraith-54321/Monkestation2.0/commit/1e9edd6a49665dc9ae5e857e72455961be4f8230)
#### Saturday 2023-12-09 23:52:13 by Kittynoodle

Refactors vendor tipping and adds 2 new malf modules: Remote vendor tipping, and the ability to roll around and crush anything in your path. (#76635)

Title.

Vendor tipping code is now on /atom/movable, and any movable can fall
over like a vendor does. Things like crits have been moved to
type-specific availability tables, their effects are now held in their
own proc, are now random per crushed item, have probability weights,
etc.

In the process of making this PR I also had to fix another issue, where
a bunch of take_damage() overrides had incorrect args, so that explains
the take_damage changes I made.

Tipping now also attacks any atoms on the target, given they use
integrity.

Adds 2 new malf modules.

1. REMOTE VENDOR TIPPING: A mid-cost and mid-supply module allows malf
AIs to remotely tip a vendor in any of the 8 directions. After 0.5
seconds of delay and a visual indicator (along with other warnings), the
vendor falls over.
1.1. In the process of making this I had to expand a arrow sprite to
have orthogonal directions, which is why you may see the testing dmi
being changed.
2. CORE ROLLING: A mid-cost but low-supply ability that allows the AI to
roll around and crush anything it falls on, including mobs. This has a
5% chance to have a critical hit so it isnt THAT terrible - plus it's
guaranteed to never stunlock. It's real utility lies in the fact the AI
now has limited movement without borgs. Also, the psychological factor.

As a bonus, vendor tipping now uses animate and transforms instead of
replacing matrices.

1. Generifying vendor tipping code is just good, period. It's a very
wacky and silly little piece of code that really doesn't need to be
isolated to vendors exclusively. ANY big and heavy object can fall over
and do a ton of damage.
1.1. Also, adding weights to critical hits is really good, because it
lets things like the headgib finally be a lot less terrifying, as
they're a lot less likely to happen.

2. Remote vendor tipping is a bit of a goofy ability that isn't really
THAT practical but has a chance of catching someone unaware and doing
some serious damage to that person alone.
2.1. Atop of this, vendor tipping isn't that loud of an action as say,
blowing things up, or doing a plasma flood. Even overrides aren't this
silent or a non-giveaway. A vendor falling on someone, though, is a
mundane thing that happens a lot. This is a decent way to assassinate
people before going loud (or at least, damage people) that isn't offered
yet.

4.
3.1. For real though, AIs rolling around is just fucking hilarious. The
ability to move isn't offered right now (which isn't that much of a bad
things), but with sufficiently limited charges (or limits to how many
times you can buy the ability), this can be a funny little t hing that
lets the AI potentially hide somewhere on the sat (or just relatively
close to the sat, such as engineering [it can't go through the
teleporter with this but it can go through transit tubes]) without the
need for borgs.
3.2. Also, it lets the AI sacrifically execute people by blowing up
their brains.

---

