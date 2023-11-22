## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-11-21](docs/good-messages/2023/2023-11-21.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,707,755 were push events containing 4,056,124 commit messages that amount to 304,386,108 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 71 messages:


## [sailfishos-mirror/llvm-project](https://github.com/sailfishos-mirror/llvm-project)@[5cd24759c4...](https://github.com/sailfishos-mirror/llvm-project/commit/5cd24759c41864215e67c280234b6c745a4cd369)
#### Tuesday 2023-11-21 00:12:42 by Louis Dionne

[libc++] Reduce the compilation time required by SIMD tests (#72602)

Testing all the SIMD widths exhaustively is nice in theory, however in
practice it leads to extremely slow tests. Given that
1. our testing resources are finite and actually pretty costly
2. we have thousands of other tests we also need to run
3. the value of executing these SIMD tests for absolutely all supported
SIMD widths is fairly small compared to cherry-picking a few relevant
widths

I think it makes a lot of sense to reduce the exhaustiveness of these
tests. I'm getting a ~4x speedup for the worst offender
(reference_assignment.pass.cpp) after this patch.

I'd also like to make this a reminder to anyone seeing this PR that
tests impact everyone's productivity. Slow unit tests contribute to
making the CI slower as a whole, and that has a direct impact on
everyone's ability to iterate quickly during PRs. Even though we have a
pretty robust CI setup in place, we should remember that it doesn't come
for free and should strive to keep our tests at a good bang for the buck
ratio.

---
## [myrmyxo/cave](https://github.com/myrmyxo/cave)@[c2f614d9a5...](https://github.com/myrmyxo/cave/commit/c2f614d9a5edaa2b36b4e6910e53081b8a352954)
#### Tuesday 2023-11-21 00:24:46 by myrmyxo

Better lakes and TREES n MUSHROOMS

Thanks dad for the better lakes lol (instead of filling from the bottom, do a broad search with a ceiling at random points, this ways lakes have a constant top level and seem realistic, and it's way fucking easier lmfao.
I'll try to improve that at some point I guess still. Cause the lakes this makes are very big.

MUSHROOMS !!! New structures, spwan only in fairy biome, have a white/brown stem and a colored cap. The taller the mushroom, the bigger the chance that the cap is bigger, (3 levels of big :

0XXX0,

XXXXX,

0XXX0
XXXXX)

they look real cool.

Trees !
In forest biomes they spawn (woody has been upgraded lol)
Between 10 and 50 tiles high, brownish trunk with varying number of branches.
Branches go up to the top of the tree too +2 tiles I think, but they rarely reach it even (from 3 to up to top).
Trunk is rather straight, but branches depending on the side progress upwards and randomly towards the direction they sprout from also, some can go very straight up after the 3 first blocks that go diagonal, and some continue going diagonal it's random (1/3 chance to move in X axis when it moves in Y axis).
At the end of each branch + the trunk, a 5*5 plant matter leaf ball is present :

0XXX0
XXXXX
XXXXX
XXXXX
0XXX0

is always its shape.

Branches, their disposition, tree color, height is all random BUT depends only on the seed !
Seed system works (duplicate trees are present so u can see lol)
However all plants for no go INTO terrain lol into the ceilling that's kinda annoying... I'll fix that later goot night.

Very happy with the result hu huaheuhaeu huaeh uaheu hae u

---
## [Monkestation/Monkestation2.0](https://github.com/Monkestation/Monkestation2.0)@[1c120f6584...](https://github.com/Monkestation/Monkestation2.0/commit/1c120f658417b4df06da8e79ceeb064eb0116647)
#### Tuesday 2023-11-21 00:34:12 by Jacquerel

Basic blob mobs (#78520)

I remembered today that blob code is ass, especially blob spores.
There's still a lot to improve but I cleaned up _some_ of it by
converting these mobs.
Now they use a newer framework and more signal handling as compared to
circular references.

I _expect_ the behaviour here to largely be the same as it was or
similar. I haven't added anything fancy or new.

This is a reasonably big PR but at least all of the files are small?
Everything here touched every other thing enough that it didnt make
sense to split up sorry.

Other things I did in code:
- Experimented with replacing the `mob/blob` subtype with a component.
Don't know if this is genius or stupid.
- AI subtree which just walks somewhere. We've used this behaviour a lot
but never given it its own subtree.
- Blob Spores and Zombies are two different mobs now instead of being
one mob which just changes every single one of its properties.
- Made a few living defence procs call super, because the only thing
super does was send a signal and we weren't doing that for no reason.
Also added a couple extra signals for intercepts we did not have.

:cl:
fix: Blob spores will respond to rallies more reliably (it won't runtime
every time they try and pathfind).
fix: Blobbernaut pain animation overlays should align with the direction
the mob is facing instead of always facing South
refactor: Blob spores, zombies, and blobbernauts now all use the basic
mob framework. They should work the same, but please report any issues.
/:cl:

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>
Co-authored-by: san7890 <the@san7890.com>

---
## [Monkestation/Monkestation2.0](https://github.com/Monkestation/Monkestation2.0)@[26645e92ff...](https://github.com/Monkestation/Monkestation2.0/commit/26645e92ff220b47178b37910dfd1838eb6cfc3d)
#### Tuesday 2023-11-21 00:34:12 by Ben10Omintrix

ice demon basic mobs (#78539)

ice demons are now basic mobs. they still have their behavior where they
can teleport around the player, run away from him and shoot him. they
now also have a new ability they will only use when they are on their
last legs, they will spawn weak and slow afterimage clones of
theirselves to attack the player. damaging these clones will also damage
the original ice demons. ice demons can also now be very easily
countered as they are very afraid of fires. they will run away from you
if they see u holding a lit torch/flare/welding tool and while running
away they will freeze the floors around them to try to slip u to stop u
from chasing them. ice demons now also get a new unique trophy! this
trophy will summon 2 friendly spirits that will help you kill ur target,
but these spirits will dissappear after a very short while.

https://github.com/tgstation/tgstation/assets/138636438/6a48fb15-f447-441a-91c6-48ca120dc22c

:cl:
refactor: ice demons have been refactored into basic mbos. please report
any bugs
add: ice demons now have a unique trophy
/:cl:

---
## [StrangeWeirdKitten/Skyrat-tg](https://github.com/StrangeWeirdKitten/Skyrat-tg)@[73bdd7341a...](https://github.com/StrangeWeirdKitten/Skyrat-tg/commit/73bdd7341acdf6f5b7d38a484a1dba8106438c56)
#### Tuesday 2023-11-21 00:39:24 by SkyratBot

[MIRROR] TGUI Destructive Analyzer [MDB IGNORE] (#25005)

* TGUI Destructive Analyzer (#79572)

## About The Pull Request

I made this to help me move more towards my goals [laid out
here](https://hackmd.io/XLt5MoRvRxuhFbwtk4VAUA) which currently doesn't
have much interest.

This makes the Destructive Analyzer use a little neat TGUI menu instead
of its old HTML one. I also touch a lot of science stuff and a little
experimentor stuff, so let me explain a bit:
Old iterations of Science had different items that you can use to boost
nodes through deconstruction. This has been removed, and its only
feature is the auto-unlocking of nodes (that is; making them visible to
the R&D console). I thought that instead of keeping this deprecated code
around, I would rework it a little to make it clear what we actually use
it for (unhiding nodes).
All vars and procs that mentioned this have been renamed or reworked to
make more sense now.

Experimentor stuff shares a lot with the destructive analyzer, so I had
to mess with that a bit to keep its decayed corpse of deprecated code,
functional.

I also added context tips to the destructive analyzer, and added the
ability to AltClick to remove the inserted item. Removing items now also
plays a little sound because it was kinda lame.
Also, balloon alerts.

## Why It's Good For The Game

Moves a shitty machine to TGUI so it is slightly less shitty, now it's
more direct and compact with more player-feedback.
Helps me with a personal project and yea

### Video demonstration

I show off connecting the machine to R&D Servers, but I haven't changed
the behavior of that and the roundstart analyzers are connected to
servers by default.

https://github.com/tgstation/tgstation/assets/53777086/65295600-4fae-42d1-9bae-eccefe337a2b

## Changelog

:cl:
refactor: Destructive Analyzers now have a TGUI menu.
/:cl:

* TGUI Destructive Analyzer

* Modular

---------

Co-authored-by: John Willard <53777086+JohnFulpWillard@users.noreply.github.com>
Co-authored-by: Giz <13398309+vinylspiders@users.noreply.github.com>

---
## [StrangeWeirdKitten/Skyrat-tg](https://github.com/StrangeWeirdKitten/Skyrat-tg)@[1f1cdc609d...](https://github.com/StrangeWeirdKitten/Skyrat-tg/commit/1f1cdc609df04a4749b2f3f5d5500551c86021a8)
#### Tuesday 2023-11-21 00:39:24 by Nerevar

[FIX] Fixes Kick Damage (#24996)

* holy shit yeah

* Update code/modules/mob/living/carbon/human/_species.dm

---------

Co-authored-by: Snakebittenn <12636964+Snakebittenn@users.noreply.github.com>
Co-authored-by: Bloop <13398309+vinylspiders@users.noreply.github.com>

---
## [TwistedCicrularConvexLens/tgstation](https://github.com/TwistedCicrularConvexLens/tgstation)@[71b45e54ad...](https://github.com/TwistedCicrularConvexLens/tgstation/commit/71b45e54adfaa4c681babc545db97fa7103289de)
#### Tuesday 2023-11-21 00:44:13 by san7890

Puts all traits in the globalvars file + CI Testing (#79642)

## About The Pull Request

Fixes #76349

I didn't know that people needed to add any new traits to a global list
so they can be easily read in View Variables, and was pretty shocked to
find out many other people didn't know it was a thing. Let's make it a
thing by testing it using a new CI Python Linter to check this. But oh
no-


![image](https://github.com/tgstation/tgstation/assets/34697715/c093f1a8-00ce-40a6-8e1d-f344107ce7b8)

There were about 200+ missing traits. Alright, so let's do the
following:

* Move trait defines to their own dedicated folder in the `_DEFINES`
folder.
* Split up the traits mega-file into different files, for better
organization. One for the macros, one for the sources, and a few for the
"trait declarations"
* Run the linter a load of times and add everything to the globalvars
file, removing anything that's no longer used and figuring out where the
best categorization of it is. also minor code improvements. also rename
all of the ones that look weird. also fix list indentations
* Also alphabetize the lists because it's easy
* Move everything to a new `traits_by_type` list, while keeping the
admin one the way it is for the time being while we figure out a better
way to show that list to admins.
* Profit
## Why It's Good For The Game

Mapping trait injectors will now work for any type of trait. You
shouldn't add any trait via this injector though, but you're no longer
limited to coders remembering to add it to that critical list you
needed.

Lays the framework for a better view variables experience. This work is
too lengthy to presently do, but hopefully we can get this done sooner
rather than later. we will need a code-accessible way to view these
traits for such a framework to be implemented, so let's just do that.

Future steps are to break down the mega-declarations file into a folder
full of separate files by typepath, but that requires a lot of auditing.
Does need to happen one day though, there's a lot of mob traits mingled
with datum traits and auuugh we gotta do this later this PR is already
massive.

there's probably ways to game this but this catches _my_ mistakes so
good luck to everyone else (it should work for 99% of everyone)
## Changelog

Nothing applicable to players. However, to mappers, the mapping trait
injector should always be able to add any kind of trait (which is rather
good for the times when you need it).

---
## [TwistedCicrularConvexLens/tgstation](https://github.com/TwistedCicrularConvexLens/tgstation)@[eb246c21f6...](https://github.com/TwistedCicrularConvexLens/tgstation/commit/eb246c21f6eb5380dc56e5779fcd51d11437557c)
#### Tuesday 2023-11-21 00:44:13 by san7890

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

---
## [lizardqueenlexi/orbstation](https://github.com/lizardqueenlexi/orbstation)@[492ed90f28...](https://github.com/lizardqueenlexi/orbstation/commit/492ed90f28dfd213e9438509653727f788efcebd)
#### Tuesday 2023-11-21 00:46:24 by necromanceranne

Fixes body collision causing a stun, despite a successful block. (#79824)

## About The Pull Request

Puts a block check into the ``throw_impact()`` of carbon mobs. 

## Why It's Good For The Game

I'm touching on a lot of 'get around shields' stuns, and this has been a
big one for the better part of a few years and potentially not even
intentional. I would say it gained its largest popularity when it became
weaponized with fireman carrying.

Despite seemingly rolling to block, blocking a body hitting you doesn't
actually do anything at all. This reminds me a bit of energy bolas. So I
fixed it? I think, there might be a better fix, I'm just replicating
code present in xenomorph tackles. This shit sucks, please recommend a
better fix if you know it.

## Changelog
:cl:
fix: When you successfully block a body collision, it does something
rather than nothing at all.
/:cl:

---
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[a911b4db9d...](https://github.com/pytorch/pytorch/commit/a911b4db9d82238a1d423e2b4c0a3d700217f0c1)
#### Tuesday 2023-11-21 01:52:51 by voznesenskym

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
## [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep)@[c4f13744d7...](https://github.com/BurntSushi/ripgrep/commit/c4f13744d74b519b29372b3dc35df2b558cb5403)
#### Tuesday 2023-11-21 02:20:13 by Andrew Gallant

cli: replace clap with lexopt and supporting code

ripgrep began it's life with docopt for argument parsing. Then it moved
to Clap and stayed there for a number of years. Clap has served ripgrep
well, and it probably could continue to serve ripgrep well, but I ended
up deciding to move off of it.

Why?

The first time I had the thought of moving off of Clap was during the
2->3->4 transition. I thought the 3.x and 4.x releases were great, but
for me, it ended up moving a little too quickly. Since the release of
4.x was telegraphed around when 3.x came out, I decided to just hold off
and wait to migrate to 4.x instead of doing a 3.x migration followed
shortly by another 4.x migration. Of course, I just never ended up doing
the migration at all. I never got around to it and there just wasn't a
compelling reason for me to upgrade. While I never investigated it, I
saw an upgrade as a non-trivial amount of work in part because I didn't
encapsulate the usage of Clap enough.

The above is just what got me started thinking about it. It wasn't
enough to get me to move off of it on its own. What ended up pushing me
over the edge was a combination of factors:

* As mentioned above, I didn't want to run on the migration treadmill.
This has proven to not be much of an issue, but at the time of the
2->3->4 releases, I didn't know how long Clap 4.x would be out before a
5.x would come out.
* The release of lexopt[1] caught my eye. IMO, that crate demonstrates
exactly how something new can arrive on the scene and just thoroughly
solve a problem minimalistically. It has the docs, the reasoning, the
simple API, the tests and good judgment. It gets all the weird corner
cases right that Clap also gets right (and is part of why I was
originally attracted to Clap).
* I have an overall desire to reduce the size of my dependency tree. In
part because a smaller dependency tree tends to correlate with better
compile times, but also in part because it reduces my reliance and trust
on others. It lets me be the "master" of ripgrep's destiny by reducing
the amount of behavior that is the result of someone else's decision
(whether good or bad).
* I perceived that Clap solves a more general problem than what I
actually need solved. Despite the vast number of flags that ripgrep has,
its requirements are actually pretty simple. We just need simple
switches and flags that support one value. No multi-value flags. No
sub-commands. And probably a lot of other functionality that Clap has
that makes it so flexible for so many different use cases. (I'm being
hand wavy on the last point.)

With all that said, perhaps most importantly, the future of ripgrep
possibly demands a more flexible CLI argument parser. In today's world,
I would really like, for example, flags like `--type` and `--type-not`
to be able to accumulate their repeated values into a single sequence
while respecting the order they appear on the CLI. For example, prior
to this migration, `rg regex-automata -Tlock -ttoml` would not return
results in `Cargo.lock` in this repository because the `-Tlock` always
took priority even though `-ttoml` appeared after it. But with this
migration, `-ttoml` now correctly overrides `-Tlock`. We would like to
do similar things for `-g/--glob` and `--iglob` and potentially even
now introduce a `-G/--glob-not` flag instead of requiring users to use
`!` to negate a glob. (Which I had done originally to work-around this
problem.) And some day, I'd like to add some kind of boolean matching to
ripgrep perhaps similar to how `git grep` does it. (Although I haven't
thought too carefully on a design yet.) In order to do that, I perceive
it would be difficult to implement correctly in Clap.

I believe that this last point is possible to implement correctly in
Clap 2.x, although it is awkward to do so. I have not looked closely
enough at the Clap 4.x API to know whether it's still possible there. In
any case, these were enough reasons to move off of Clap and own more of
the argument parsing process myself.

This did require a few things:

* I had to write my own logic for how arguments are combined into one
single state object. Of course, I wanted this. This was part of the
upside. But it's still code I didn't have to write for Clap.
* I had to write my own shell completion generator.
* I had to write my own `-h/--help` output generator.
* I also had to write my own man page generator. Well, I had to do this
with Clap 2.x too, although my understanding is that Clap 4.x supports
this. With that said, without having tried it, my guess is that I
probably wouldn't have liked the output it generated because I
ultimately had to write most of the roff by hand myself to get the man
page I wanted. (This also had the benefit of dropping the build
dependency on asciidoc/asciidoctor.)

While this is definitely a fair bit of extra work, it overall only cost
me a couple days. IMO, that's a good trade off given that this code is
unlikely to change again in any substantial way. And it should also
allow for more flexible semantics going forward.

Fixes #884, Fixes #1648, Fixes #1701, Fixes #1814, Fixes #1966

[1]: https://docs.rs/lexopt/0.3.0/lexopt/index.html

---
## [norwd/licenses](https://github.com/norwd/licenses)@[d64377c012...](https://github.com/norwd/licenses/commit/d64377c012a0596995e92a6f507195ecd20b2769)
#### Tuesday 2023-11-21 02:57:20 by Y. Meyer-Norwood

Add Do What the Fuck You Want To Public License

See also: https://en.wikipedia.org/wiki/WTFPL

---
## [nkouevda/git](https://github.com/nkouevda/git)@[8f23432b38...](https://github.com/nkouevda/git/commit/8f23432b38d9b122be8179295a56688391dc8ad6)
#### Tuesday 2023-11-21 03:19:55 by Johannes Schindelin

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
Signed-off-by: Pratyush Yadav <me@yadavpratyush.com>

---
## [lmorv/n-spiritual-persona](https://github.com/lmorv/n-spiritual-persona)@[77b0b6a3be...](https://github.com/lmorv/n-spiritual-persona/commit/77b0b6a3be1555b42f86d82edb8ab39935553aff)
#### Tuesday 2023-11-21 03:42:56 by lmorv

Art: Sculpting variants

- Started sculpting some variant body parts, I don't think I've hit on a good enough vibe tho. I feel like the I'm not getting the results that I want stylistically. Maybe it has to do with my technique, or the dynamic topology feature. It is hard to sculpt in low poly, maybe I should take some time to try out some polygon modeling techniques. Try to be more targeted and specific. Be a little bolder with shapes and so on. I had the idea of trying to sculpt in the ipad as well, see if that unlocks some other part of my brain. And another thing I wanted to try is to sculpt in hi-res then decimate the mesh down to low poly again. But I feel that would be a lot of work haha, and an easy way to get very obsessed about the smallest details (it already is easy to do that). I think it may pay more to focus on larger, intentional shapes, either by polygon modeling, or low-res dynotopo sculpting with more confidence, or a combination of the two. The confidence part might be easier on the ipad (procreate), a bit less clunky perhaps. The polygon modeling is easier in blender tho...

---
## [khonsulabs/gooey](https://github.com/khonsulabs/gooey)@[2201f2c83b...](https://github.com/khonsulabs/gooey/commit/2201f2c83b87efd7bf2eab76d65d9118b0ab7d3d)
#### Tuesday 2023-11-21 03:50:02 by Jonathan Johnson

Ranged sliders, advance_focus, allow_blur

Closes #60

Stepping in sliders is a compromise due to the flexibility of the
current slider implementation. I don't want to force types to implement
Add, and I don't like forcing types to require a Step (ie, what's the
appropriate value for f32 to specify as its next value?). Using a
percentage combined with lerp keeps the implementation fairly
straightfoward, although I remember experiencing this type of
configuration in another UI framework a long time ago and thinking it
was a little annoying to work with.

Ultimately, setting actual step boundaries can be done by customizing
the type that the slider is operating over. I feel like that's a much
more powerful design than I've experienced in previous frameworks, so
I'm hoping this percent step behavior is a reasonable compromise.

---
## [DrAmazing343/tgstation](https://github.com/DrAmazing343/tgstation)@[c63b233f42...](https://github.com/DrAmazing343/tgstation/commit/c63b233f42a46d9373fd41b3f69edde3d2d48002)
#### Tuesday 2023-11-21 04:18:04 by _0Steven

Make sign language unaffected by the Social Anxiety quirk's direct speech effects (#79809)

## About The Pull Request

Alternative title: "Make going non-verbal make you less anxious."

This is a two line change to `social_anxiety.dm` to quit out its
`handle_speech` method when user has the `TRAIT_SIGN_LANG` trait.
This stops the Social Anxiety quirk from applying its
stutters/fillers/blockers for as long as the speaker is using sign
language.
This does nothing to any of social anxiety's non-verbal effects, those
are still active regardless and entirely unaffected.
## Why It's Good For The Game

Primarily: I think giving people the choice between using anxious talk
or sign language, and thus the different hurdles inherent to both, makes
for a more interesting gameplay interaction than simply blanket-applying
the quirk's speech effects to both.

Secondarily: Social Anxiety's non-verbal penalties are entirely
unaffected. One will still get the penalties from making eye contact and
occasionally make eye contact with objects. Notably this includes the
stuttering making eye contact could get you, which still makes your
signing shaky. You're still anxious, after all.
On top of this, it still costs more to pick up Signer than Social
Anxiety allows for, and thus the change doesn't simply make the
combination free points.

Tertiarily: when one has trouble speaking verbally, non-verbal
communication can be helpful in overcoming that hurdle. This is
especially so when the trigger for said anxiety is speaking verbally in
the first place. This is part of why I was so enamoured by the
combination before a broader and, mind you, fairly needed fix to sign
language made these interact differently.
## Changelog
:cl:
balance: signers no longer suffer from social anxiety's speech changes
when they go non-verbal. Other effects are maintained.
/:cl:

---
## [JaycenResearch/STEAMai](https://github.com/JaycenResearch/STEAMai)@[bd24e52dd3...](https://github.com/JaycenResearch/STEAMai/commit/bd24e52dd345c3ecae819f564452ca314fff28af)
#### Tuesday 2023-11-21 04:37:27 by JaycenResearch

Update README.md

what did I say? I said fuck you God, you nonexisting greatest evil mankind ever invented

---
## [radu-cernatescu/terminal](https://github.com/radu-cernatescu/terminal)@[86fb9b4478...](https://github.com/radu-cernatescu/terminal/commit/86fb9b44787accd09c5943a506e27eb4c8e573c0)
#### Tuesday 2023-11-21 04:49:34 by Dustin L. Howett

Add a magic incantation to tell the Store we support Server (#16306)

I find it somewhat silly that (1) this isn't documented anywhere and (2)
installing the "desktop experience" packages for Server doesn't
automatically add support for the `Windows.Desktop` platform...

Oh well.

I'm going to roll this one out via Preview first, because if the store
blows up on it I would rather it not be during Stable roll-out.

---
## [SapphicOverload/tgstation](https://github.com/SapphicOverload/tgstation)@[9e6cbf2538...](https://github.com/SapphicOverload/tgstation/commit/9e6cbf2538d1d0440cca5a5950988313ef9382b9)
#### Tuesday 2023-11-21 04:59:06 by lizardqueenlexi

Basic skeletons (#79206)

## About The Pull Request

Turns skeletons (the simple animal version) into basic mobs. This was
another incredibly simple conversion, since skeletons don't really do
anything but walk at you and beat you to death.

Because I thought it was funny, though, skeletons will now seek out
cartons of milk and drink them. Real milk will heal them for a
significant amount, but soymilk, being false milk, will deal them
grievous injury instead! Skeletons beware... I didn't add any other
sorts of milk due to limited ability with existing AI behaviors to
identify milk containers (they actually only look for the carton items).

Other than that, I've done some flavor adjustment for skeletons' attacks
- their effects and sounds will now suit the weapon they're actually
holding - for example, skeleton templars now actually use their swords
instead of slashing you with their horrible fingers. Along with this I
gave the basic skeletons a normal slashing sound, instead of the weird,
impactless hallucination sound they used to use for some reason. I never
liked that sound.

Finally, I've reflavored the spear-wielding skeleton mobs to "undead
settlers", following the naming of the corpses dropped by snow legions
as of #76898, rather than being named after an offensive term for Inuit
people. These skeletons do, after all, appear in settlements on alien
worlds.

To enable the flavor of milk drinking, I expanded the `basic_eating`
component to allow drinking rather than eating flavor, with a different
sound and its own set of verbs. This deletes whatever they drink from,
but c'est la vie.
## Why It's Good For The Game

Ticks 6 more entries off the simple animal freeze. While skeletons are
still extremely simple, being largely-identical mobs that only exist to
beat you to death, being basic mobs should make them slightly better at
this job. Also, again, I think it's really funny that you can distract
skeleton mobs with milk, or even hurt them.
## Changelog
:cl:
refactor: Hostile skeleton NPCs now use the basic mob framework. They're
a little smarter, and they also have a slightly improved set of attack
effects and sounds. They love to drink milk, but will be harmed greatly
if any heartless spaceman tricks them into drinking soymilk instead.
Please report any bugs.
/:cl:

---
## [SapphicOverload/tgstation](https://github.com/SapphicOverload/tgstation)@[764b998b1d...](https://github.com/SapphicOverload/tgstation/commit/764b998b1d5df5fce7df0d2ecd1b1758445a8b3e)
#### Tuesday 2023-11-21 04:59:06 by carlarctg

Adds a Syndicate Monkey Agent beacon uplink item (#79012)

## About The Pull Request

Adds a Syndicate Monkey Agent beacon uplink item. It spawns a dapper
monkey that must follow your orders.

Added a monkey gun case to the uplink, which contains monkey guns!
Though they aren't very powerful.

Added a more modularlike subtype for antagonist spawners to reduce
future hardcoding.

Gave the syndicate turtleneck a monkey sprite, from SS14!

## Why It's Good For The Game

I want to see the clown driving security insane with 2-3 monkeys and an
incredible amount of pranking. Or an assistant killing everyone with his
monkey friends while wearing a monkey suit. Or a geneticist sending out
mutated monkeys to kill people. Or a scientist equipping his monkeys
with bombs or xenobiology equipment and sending them out to wreak havoc.

6 TC is only enough for two monkeys, but you can get a third if you
finish any kind of objective.

> Added a monkey gun case to the uplink, which contains monkey guns!
Though they aren't very powerful.

We can't have the monkey mafia without guns, come on. The guns are weak
and only usable by monkeys. Additionally, they're restricted to
entertainment only.

Credit to SS14 for the monky turtleneck sprite.

## Changelog

:cl:
add: Adds a Syndicate Monkey Agent beacon uplink item. It spawns a
dapper monkey that must follow your orders.
add: Added a monkey gun case to the uplink, which contains monkey guns!
Though they aren't very powerful.
refactor: Added a more modularlike subtype for antagonist spawners to
reduce future hardcoding.
sprite: Gave the syndicate turtleneck a monkey sprite, from SS14!
/:cl:

---------

Co-authored-by: ATH1909 <42606352+ATH1909@users.noreply.github.com>
Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [citu-cpe/logistech](https://github.com/citu-cpe/logistech)@[b09297ae47...](https://github.com/citu-cpe/logistech/commit/b09297ae47632d971778f2ae7ef39347260fdf28)
#### Tuesday 2023-11-21 04:59:54 by John Earl Bascos

manifesting princh to find a girlfriend before the end of the year which can be 98% possible if only he makes his move and I know that he knows who im referring to ;) you dont like her? really? i dont believe you

---
## [ishitatsuyuki/binutils](https://github.com/ishitatsuyuki/binutils)@[05e1cac249...](https://github.com/ishitatsuyuki/binutils/commit/05e1cac2496f842f70744dc5210fb3072ef32f3a)
#### Tuesday 2023-11-21 05:10:21 by Andrew Burgess

gdb: fix vfork regressions when target-non-stop is off

It was pointed out on the mailing list[1] that after this commit:

  commit b1e0126ec56e099d753c20e91a9f8623aabd6b46
  Date:   Wed Jun 21 14:18:54 2023 +0100

      gdb: don't resume vfork parent while child is still running

the test gdb.base/vfork-follow-parent.exp now has some failures when
run with the native-gdbserver or native-extended-gdbserver boards:

  FAIL: gdb.base/vfork-follow-parent.exp: resolution_method=schedule-multiple: continue to end of inferior 2 (timeout)
  FAIL: gdb.base/vfork-follow-parent.exp: resolution_method=schedule-multiple: inferior 1 (timeout)
  FAIL: gdb.base/vfork-follow-parent.exp: resolution_method=schedule-multiple: print unblock_parent = 1 (timeout)
  FAIL: gdb.base/vfork-follow-parent.exp: resolution_method=schedule-multiple: continue to break_parent (timeout)

The reason that these failures don't show up when run on the standard
unix board is that the test is only run in the default operating mode,
so for Linux this will be all-stop on top of non-stop.

If we adjust the test script so that it runs in the default mode and
with target-non-stop turned off, then we see the same failures on the
unix board.  This commit includes this change.

The way that the test is written means that it is not (currently)
possible to turn on non-stop mode and have the test still work, so
this commit does not do that.

I have also updated the test script so that the vfork child performs
an exec as well as the current exit.  Exec and exit are the two ways
in which a vfork child can release the vfork parent, so testing both
of these cases is useful I think.

In this test the inferior performs a vfork and the vfork-child
immediately exits.  The vfork-parent will wait for the vfork-child and
then blocks waiting for gdb.  Once gdb has released the vfork-parent,
the vfork-parent also exits.

In the test that fails, GDB sets 'detach-on-fork off' and then runs to
the vfork.  At this point the test tries to just "continue", but this
fails as the vfork-parent is still selected, and the parent can't
continue until the vfork-child completes.  As the vfork-child is
stopped by GDB the parent will never stop once resumed, so GDB refuses
to resume it.

The test script then sets 'schedule-multiple on' and once again
continues.  This time GDB, in theory, resumes both the parent and the
child, the parent will be held blocked by the kernel, but the child
will run until it exits, and which point GDB stops again, this time
with inferior 2, the newly exited vfork-child, selected.

What happens after this in the test script is irrelevant as far as
this failure is concerned.

To understand why the test started failing we should consider the
behaviour of four different cases:

  1. All-stop-on-non-stop before commit b1e0126ec56e,

  2. All-stop-on-non-stop after commit b1e0126ec56e,

  3. All-stop-on-all-stop before commit b1e0126ec56e, and

  4. All-stop-on-all-stop after commit b1e0126ec56e.

Only case #4 is failing after commit b1e0126ec56e, but I think the
other cases are interesting because, (a) they inform how we might fix
the regression, and (b) it turns out the behaviour of #2 changed too
with the commit, but the change was harmless.

For #1 All-stop-on-non-stop before commit b1e0126ec56e, what happens
is:

  1. GDB calls proceed with the vfork-parent selected, as schedule
     multiple is on user_visible_resume_ptid returns -1 (everything)
     as the resume_ptid (see proceed function),

  2. As this is all-stop-on-non-stop, every thread is resumed
    individually, so GDB tries to resume both the vfork-parent and the
    vfork-child, both of which succeed,

  3. The vfork-parent is held stopped by the kernel,

  4. The vfork-child completes (exits) at which point the GDB sees the
     EXITED event for the vfork-child and the VFORK_DONE event for the
     vfork-parent,

  5. At this point we might take two paths depending on which event
     GDB handles first, if GDB handles the VFORK_DONE first then:

     (a) As GDB is controlling both parent and child the VFORK_DONE is
         ignored (see handle_vfork_done), the vfork-parent will be
	 resumed,

     (b) GDB processes the EXITED event, selects the (now defunct)
         vfork-child, and stops, returning control to the user.

     Alternatively, if GDB selects the EXITED event first then:

     (c) GDB processes the EXITED event, selects the (now defunct)
         vfork-child, and stops, returning control to the user.

     (d) At some future time the user resumes the vfork-parent, at
         which point the VFORK_DONE is reported to GDB, however, GDB
	 is ignoring the VFORK_DONE (see handle_vfork_done), so the
	 parent is resumed.

For case #2, all-stop-on-non-stop after commit b1e0126ec56e, the
important difference is in step (2) above, now, instead of resuming
both the vfork-parent and the vfork-child, only the vfork-child is
resumed.  As such, when we get to step (5), only a single event, the
EXITED event is reported.

GDB handles the EXITED just as in (5)(c), then, later, when the user
resumes the vfork-parent, the VFORKED_DONE is immediately delivered
from the kernel, but this is ignored just as in (5)(d), and so,
though the pattern of when the vfork-parent is resumed changes, the
overall pattern of which events are reported and when, doesn't
actually change.  In fact, by not resuming the vfork-parent, the order
of events (in this test) is now deterministic, which (maybe?) is a
good thing.

If we now consider case #3, all-stop-on-all-stop before commit
b1e0126ec56e, then what happens is:

  1. GDB calls proceed with the vfork-parent selected, as schedule
     multiple is on user_visible_resume_ptid returns -1 (everything)
     as the resume_ptid (see proceed function),

  2. As this is all-stop-on-all-stop, the resume is passed down to the
     linux-nat target, the vfork-parent is the event thread, while the
     vfork-child is a sibling of the event thread,

  3. In linux_nat_target::resume, GDB calls linux_nat_resume_callback
     for all threads, this causes the vfork-child to be resumed.  Then
     in linux_nat_target::resume, the event thread, the vfork-parent,
     is also resumed.

  4. The vfork-parent is held stopped by the kernel,

  5. The vfork-child completes (exits) at which point the GDB sees the
     EXITED event for the vfork-child and the VFORK_DONE event for the
     vfork-parent,

  6. We are now in a situation identical to step (5) as for
     all-stop-on-non-stop above, GDB selects one of the events to
     handle, and whichever we select the user sees the correct
     behaviour.

And so, finally, we can consider #4, all-stop-on-all-stop after commit
b1e0126ec56e, this is the case that started failing.

We start out just like above, in proceed, the resume_ptid is
-1 (resume everything), due to schedule multiple being on.  And just
like above, due to the target being all-stop, we call
proceed_resume_thread_checked just once, for the current thread,
which, remember, is the vfork-parent thread.

The change in commit b1e0126ec56e was to avoid resuming a vfork-parent
thread, read the commit message for the justification for this change.

However, this means that GDB now rejects resuming the vfork-parent in
this case, which means that nothing gets resumed!  Obviously, if
nothing resumes, then nothing will ever stop, and so GDB appears to
hang.

I considered a couple of solutions which, in the end, I didn't go
with, these were:

  1. Move the vfork-parent check out of proceed_resume_thread_checked,
     and place it in proceed, but only on the all-stop-on-non-stop
     path, this should still address the issue seen in b1e0126ec56e,
     but would avoid the issue seen here.  I rejected this just
     because it didn't feel great to split the checks that exist in
     proceed_resume_thread_checked like this,

  2. Extend the condition in proceed_resume_thread_checked by adding a
     target_is_non_stop_p check.  This would have the same effect as
     idea 1, but leaves all the checks in the same place, which I
     think would be better, but this still just didn't feel right to
     me, and so,

What I noticed was that for the all-stop-on-non-stop, after commit
b1e0126ec56e, we only resumed the vfork-child, and this seems fine.
The vfork-parent isn't going to run anyway (the kernel will hold it
back), so if feels like we there's no harm in just waiting for the
child to complete, and then resuming the parent.

So then I started looking at follow_fork, which is called from the top
of proceed.  This function already has the task of switching between
the parent and child based on which the user wishes to follow.  So, I
wondered, could we use this to switch to the vfork-child in the case
that we are attached to both?

Turns out this is pretty simple to do.

Having done that, now the process is for all-stop-on-all-stop after
commit b1e0126ec56e, and with this new fix is:

  1. GDB calls proceed with the vfork-parent selected, but,

  2. In follow_fork, and follow_fork_inferior, GDB switches the
     selected thread to be that of the vfork-child,

  3. Back in proceed user_visible_resume_ptid returns -1 (everything)
     as the resume_ptid still, but now,

  4. When GDB calls proceed_resume_thread_checked, the vfork-child is
     the current selected thread, this is not a vfork-parent, and so
     GDB allows the proceed to continue to the linux-nat target,

  5. In linux_nat_target::resume, GDB calls linux_nat_resume_callback
     for all threads, this does not resume the vfork-parent (because
     it is a vfork-parent), and then the vfork-child is resumed as
     this is the event thread,

At this point we are back in the same situation as for
all-stop-on-non-stop after commit b1e0126ec56e, that is, the
vfork-child is resumed, while the vfork-parent is held stopped by
GDB.

Eventually the vfork-child will exit or exec, at which point the
vfork-parent will be resumed.

[1] https://inbox.sourceware.org/gdb-patches/3e1e1db0-13d9-dd32-b4bb-051149ae6e76@simark.ca/

---
## [thgvr/Shiptest](https://github.com/thgvr/Shiptest)@[2a74c23d62...](https://github.com/thgvr/Shiptest/commit/2a74c23d62916ddb6b1fdfab8c969b7702299067)
#### Tuesday 2023-11-21 06:32:22 by Imaginos16

Nerfs the everloving almighty shit out of the jungle demonic office ruin (#2430)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Nerfs the ruin by removing most of its gamer gear, and changing the
syndicate hardsuit you find into a scarlet hardsuit.


Not to mention the two goddamn deathsquad hardsuits all there,
wholesale, for free.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/a8333190-37ce-441f-a746-bb5f2fc26828)

This shit is not okay jesus fucking christ, two deathsquad hardsuits?
Are you insane?
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: PositiveEntropy
balance: The Jungle Demonic Office Ruin has now been appropriately
balanced, now only having a scarlet hardsuit, decent syndicate armor,
and a bulldog with no spare mags.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [thgvr/Shiptest](https://github.com/thgvr/Shiptest)@[bf4671ff83...](https://github.com/thgvr/Shiptest/commit/bf4671ff83e2cb937a019f7f0515e6f23c32f493)
#### Tuesday 2023-11-21 06:32:22 by retlaw34

Gun rework (#1601)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
WIP.

if it wasn't obvious, very based off tgmc 

this reworks how guns work, by making them 4x more lethal without
touching a single damage value

its a bit difficult to put into words what this does, so i think these 3
gunfights i did with a good friend explains it better than i ever could

https://streamable.com/09in19
https://streamable.com/yel56o
https://streamable.com/x2a0he

if you didnt watch these videos:
- New guns sounds, TGMC as usual. but some racking sounds are from CEV
eris
- guns now can be wielded, if unwielded, they may cause recoil which not
only makes your shots less accurate, but 'scrolls' your screen
- new suppression effects
- getting hit hard enough scrolls your screen
- anything getting hit shakes you as feedback, not just bullets
- bullets can ricochet naturally upon hitting a surface at a step angle.
does not auto aim at your target, so be careful. ricochet sfx taken from
CEV eris
- new effects for bullet impacts. sound effects were taken from TGMC and
https://github.com/Skyrat-SS13/Skyrat-tg/pull/11697
- adds the cattleman revolver and Himehabu 22lr pistol. sprites by yours
truely

big problem is, in order for all of this to work, a certain key needs to
be binded to rack the gun. by default this is SPACE, but moost already
have it binded to 'hold throw mode', which is an issue. for one, not
only you need to ask everyone to rebind their controls to a very
important key, but also a key dedicated to just racking the gun can
cause issues. im up for any solutions

- [x] I affirm that I have tested all of my proposed changes and that
any issues found during tested have been addressed.

## Why It's Good For The Game

people dont fear gunfights. they think its just a way to pvp. people
should be afraid of gunfights, feel the pain OOCly when their blorbo
gets hit

## Changelog

:cl:
add: 22lr and cattleman revolver
add: many gun sounds
balance: guns reworked
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: retlaw34 <bruhasdfasdfasdf@waifu.club>

---
## [Lagomorphica/CMSS13](https://github.com/Lagomorphica/CMSS13)@[830e002a27...](https://github.com/Lagomorphica/CMSS13/commit/830e002a27b7b4115815e450b8506832cb403a02)
#### Tuesday 2023-11-21 07:26:44 by QuickLode

Adds a Colony Synthetic variant, with bug fixes (#4760)

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

1. should fix fax machine problem(thx forest)
2.  gives trucker synth the frontier jumpsuit(Thwomplert)
3. adds Freelancer Synthetic. This Synth is one that was bought off a
civi market and reprogrammed, or stolen and reprogrammed, or hacked, You
get the point - its going with a band of freelancers. The idea behind it
is that this synth's team is dead and they are just programmed as a merc
for pay - hoping to someday find their boss boss and give the money as
set up. I always thought about this one for a long time and decided to
put him in the civilian category, where its hard to roll and also gives
you freedom to choose your allegiance. In this case I hope that a
freelancer synthetic will open up unique avenue of RP and allegiance.
I've only explored it once ingame, but it was very good for RP!
Hopefully people can recreate this success.

was hard to make this guy look cool and I also wasn't sure on what his
loadout would be. I ended up giving him random generic stuff while
looking like a beat up freelancer(missing the armor especially hurt his
look, since thats the largest piece of a freelancer - the curiass, but I
don't want to give armor for balance reasons) and no beret because its
for a SL only.

as usual, if a synth wants to change RP avenues and don different
clothes for different RP, no one would know the difference
# Explain why it's good for the game
1. bug bad
2. a beat up UA laborer that so happens to be synthetic. you wouldn't
expect it because there's so many similar looking people! exactly the
job of a synth - to blend in.
3. Freelancer colony synth hopefully will open up a unique avenue of RP.
If they don't want to they can always ditch it - but its on a relatively
rare and uncommon roll anyways.
# Testing Photographs and Procedure
<details>
<summary>[Screenshots &
Videos](https://cdn.discordapp.com/attachments/490668342357786645/1166307813719556187/image.png?ex=654a03cb&is=65378ecb&hm=7108218bbaab61c78c0bedcecbfdcc07bdf9db87a3fefe9fb94b28d3430cc815&)</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl:
add: adds another Colony Synthetic variant, changes up some existing
ones(trucker,CMB)
fix: fixes a small problem with WY-Colony Synthetic access(thx forest),
adds WY subtype of Synthetics for admin building/faxes
fix: fixes problems with organic spawning ferret industries Trucker
Synthetic
/:cl:

---
## [vdaular-dev/linksfordevs](https://github.com/vdaular-dev/linksfordevs)@[c55a058207...](https://github.com/vdaular-dev/linksfordevs/commit/c55a058207543c72888c52a8a723d3d2d344ba3e)
#### Tuesday 2023-11-21 07:32:46 by Ben Dornis

Updating: 11/20/2023 10:00:00 PM

 1. Added: The cocktail revolution - Works in Progress
    (https://worksinprogress.co/issue/the-cocktail-revolution/)
 2. Added: SearchArray: Making search relevance not so special
    (https://softwaredoug.com/blog/2023/11/20/search-relevance-less-special)
 3. Added: Long Term Refactors - Max Chernyak
    (https://max.engineer/long-term-refactors)
 4. Added: Exploring macOS private frameworks
    (https://www.jviotti.com/2023/11/20/exploring-macos-private-frameworks.html)
 5. Added: How to Effectively Set Up NextJS with a Component Library using Monorepos
    (https://dainemawer.com/articles/how-to-effectively-setup-nextjs-with-a-component-library-using-monorepos)
 6. Added: Tim Severien
    (https://tsev.dev/posts/2023-11-10-should-avif-be-the-dominant-image-format/)
 7. Added: The reciprocal Fibonacci constant
    (https://fredrikj.net/blog/2023/11/the-reciprocal-fibonacci-constant/)
 8. Added: Writing a Cloudflare worker with squint and bun
    (https://blog.michielborkent.nl/squint-cloudflare-bun.html)
 9. Added: Data-Driven Development is a Lie
    (https://grishaev.me/en/ddd-lie)
10. Added: Back up your Bitwarden vault in a future-proof and secure way
    (https://davidisaksson.dev/posts/bitwarden-backup/)
11. Added: Discount rates in venture backed startups
    (https://reactionwheel.net/2023/11/discount-rates-in-venture-backed-startups.html)
12. Added: Erik Johannes Husom
    (https://erikjohannes.no/posts/20231119-the-future-of-social-media/)
13. Added: Never again compare a startup to a vitamin
    (https://www.pathsensitive.com/2023/09/its-time-for-painkillers-vitamins-die.html)
14. Added: UTC is not Your Saviour – Random Notes
    (https://blog.nytsoi.net/2022/03/13/utc)
15. Added: C# Data Access: Complex Objects with Dapper
    (https://youtube.com/watch?v=n7mGEh4_06c)
16. Added: 📨 Void Inbox
    (https://orchardlab.dev/posts/void-inbox/)
17. Added: Reverse-engineering GPTs for fun and data
    (https://andrei.fyi/blog/reverse-engineering-gpts/)
18. Added: The Creator's Curse: Why your latest project will eventually make you miserable | Peter Shallard
    (https://www.petershallard.com/the-creators-curse/)
19. Added: The New CSS Math: rem() and mod()
    (https://danielcwilson.com/posts/mathematicss-rem-mod/)
20. Added: Microsoft Canada - Calgary Automation and Integration Day
    (https://msit.events.teams.microsoft.com/event/5d41b1b3-e626-4de4-92db-65768d6f2ea6@72f988bf-86f1-41af-91ab-2d7cd011db47)
21. Added: Radius a new open-source application platform for the cloud | BRK402
    (https://youtube.com/watch?v=gaG77PiYv5w)
22. Added: Migrating Page Navigation Apps from Xamarin Forms
    (https://platform.uno/blog/migrating-page-navigation-apps-from-xamarin-forms/)

Generation took: 00:09:07.3204785
 Maintenance update - cleaning up homepage and feed

---
## [PennyLaneAI/pennylane](https://github.com/PennyLaneAI/pennylane)@[47e74e16d0...](https://github.com/PennyLaneAI/pennylane/commit/47e74e16d0fb27aedc5ffab69aefaf5188115038)
#### Tuesday 2023-11-21 08:02:46 by Matthew Silverman

simplify state reordering logic (#4817)

**Context:**
I wrote the same function twice, differing only by state flattening, to
get the DQ upgrade done. It's starting to cause trouble.

**Description of the Change:**
Greatly simplified the state re-arrangement logic. There used to be a
whole mess of things happening, but now things are much more
straightforward.
1. `simulate` first puts things in our "standard" order, and this means
that if any measured wires are not also operator wires, they are put to
the _end_ of our tape wires. Therefore, for each measured-only wire, we
just have to stack a `zeros_like(state)` to the last axis of our final
state! `simulate` never tried to transpose wires back to a different
ordering, so that was always wasted work.
2. `StateMP.process_state` _always_ receives the full state, and never
needed to pad. No other device has done this optimization (the function
used to literally just `return state` before DQ2 migration), and
`simulate` already ensures that the final state has all wires in it -
they just might be out of order. The only thing we might need from
`process_state` is a transposition to the correct wire order. The
inputted `wire_order` _should_ always be `range(len(wires))`, but
whatever, we don't need to assume that.

I'll paint a picture for a normal scenario:

```python
@qml.qnode(qml.device("default.qubit", wires=3))
def circuit(x):
    qml.RX(x, 0)
    qml.CNOT([0, 2])
    return qml.state()
```

What happens with this QNode?
1. Device preprocessing sticks the device wires (`[0, 1, 2]`) onto the
`StateMP`
2. `simulate` maps the wires to our standard order. I'll demonstrate
(with `probs` so I can specify wires):

```pycon
>>> qs = qml.tape.QuantumScript([qml.RX(1.1, 0), qml.CNOT([0, 2])], [qml.probs(wires=[0, 1, 2])])
>>> qs.map_to_standard_wires().circuit
[RX(1.1, wires=[0]), CNOT(wires=[0, 1]), probs(wires=[0, 2, 1])]
```

3. Operate on the 2-qubit state, then stack another `[[0, 0], [0, 0]]`
on the end of it (wire "1")
4. `StateMP(wires=[0, 1, 2]).process_state(state, wire_order=[0, 2, 1])`
transposes the result to the correct order

I also changed the torch tests to stop using a deprecated setter for
default float types.

**Benefits:**
Duplicate code is cleaned up, existing code is simplified, no
unnecessary call to transpose.

**Possible Drawbacks:**
- Have to call `qml.math.stack` for every wire that was not operated on.
Hopefully this is usually not a lot, and it's not that costly anyway
- functions now do less than they used to (I see this as a perk - they
now do _exactly_ what they're supposed to)

---
## [MaxSagebaum/cppfront](https://github.com/MaxSagebaum/cppfront)@[cdf71bdca6...](https://github.com/MaxSagebaum/cppfront/commit/cdf71bdca64536a005f2491d8c19f1d05a1c62f6)
#### Tuesday 2023-11-21 08:45:45 by Herb Sutter

Correct copy/move for `union`

By writing separate construction and assignment, plus the new feature of suppressing assignment to a member by writing `member = _ ;` (now allowed only in assignment operators).

I do realize that's an "opt-out" which I normally prefer to avoid, but:

- I considered and decided against (for now) the alternative of not having assignment be memberwise by default. I want to keep the (new to Cpp2) default of memberwise semantics for assignment as with construction. I think that's a useful feature, and normally if you do assign to a member it doesn't arise, and so I think it makes sense to explicitly call out when we're choosing not to do any assignment at all to a member before doing other assignment processing. We'll get experience with how it goes.

- `_` is arguably natural here, since it's pronounced "don't care." There too, we'll see if that is natural generalized, or feels strained. For now it feels natural to me.

---
## [proxymurder/nginx-server](https://github.com/proxymurder/nginx-server)@[b08b59080d...](https://github.com/proxymurder/nginx-server/commit/b08b59080dd6321fbdd270fba27fb081dc9c9742)
#### Tuesday 2023-11-21 09:02:56 by proxymurder

first release; yaml-cpp is kind of forcing my hand to use std::string which is suboptimal as fuck; but shit works so I guess It's stable; quite frankly this could have been done in way less time If I knew how the fuck to test shit before writing stupid code

---
## [jordanpg/Tabletop-Simulator-Scripts](https://github.com/jordanpg/Tabletop-Simulator-Scripts)@[be30ef342e...](https://github.com/jordanpg/Tabletop-Simulator-Scripts/commit/be30ef342ea3577b9e0fa0adb4a476ec9b2f839e)
#### Tuesday 2023-11-21 09:20:27 by rubic

Update Importer.lua

- Fixed card languages breaking importing anything that isn't English
- Fixed importing multiple of the same card with different prints
- Added a lot of spaces. Fuck you
- Dirt

---
## [darnautov/kibana](https://github.com/darnautov/kibana)@[cd909f03b1...](https://github.com/darnautov/kibana/commit/cd909f03b1d71da93041a0b5c184243aa6506dea)
#### Tuesday 2023-11-21 09:30:10 by Kyle Pollich

[Fleet] Fix inability to upgrade agents from 8.10.4 -> 8.11 (#170974)

## Summary

Closes https://github.com/elastic/kibana/issues/169825

This PR adds logic to Fleet's `/api/agents/available_versions` endpoint
that will ensure we periodically try to fetch from the live product
versions API at https://www.elastic.co/api/product_versions to make sure
we have eventual consistency in the list of available agent versions.

Currently, Kibana relies entirely on a static file generated at build
time from the above API. If the API isn't up-to-date with the latest
agent version (e.g. kibana completed its build before agent), then that
build of Kibana will never "see" the corresponding build of agent.

This API endpoint is cached for two hours to prevent overfetching from
this external API, and from constantly going out to disk to read from
the agent versions file.

## To do
- [x] Update unit tests
- [x] Consider airgapped environments

## On airgapped environments

In airgapped environments, we're going to try and fetch from the
`product_versions` API and that request is going to fail. What we've
seen happen in some environments is that these requests do not "fail
fast" and instead wait until a network timeout is reached.

I'd love to avoid that timeout case and somehow detect airgapped
environments and avoid calling this API at all. However, we don't have a
great deterministic way to know if someone is in an airgapped
environment. The best guess I think we can make is by checking whether
`xpack.fleet.registryUrl` is set to something other than
`https://epr.elastic.co`. Curious if anyone has thoughts on this.

## Screenshots


![image](https://github.com/elastic/kibana/assets/6766512/0906817c-0098-4b67-8791-d06730f450f6)


![image](https://github.com/elastic/kibana/assets/6766512/59e7c132-f568-470f-b48d-53761ddc2fde)


![image](https://github.com/elastic/kibana/assets/6766512/986372df-a90f-48c3-ae24-c3012e8f7730)

## To test

1. Set up Fleet Server + ES + Kibana
2. Spin up a Fleet Server running Agent v8.11.0
3. Enroll an agent running v8.10.4 (I used multipass)
4. Verify the agent can be upgraded from the UI

---------

Co-authored-by: Kibana Machine <42973632+kibanamachine@users.noreply.github.com>

---
## [chhotelalsonwani777/GeeksInformation](https://github.com/chhotelalsonwani777/GeeksInformation)@[d39e0ca5e8...](https://github.com/chhotelalsonwani777/GeeksInformation/commit/d39e0ca5e80177ef9d43e651fe23d8d39ba632b3)
#### Tuesday 2023-11-21 09:36:24 by Chhotelal Sonwani

Add files via upload

Explore our new online shopping project designed for a hassle-free experience! We used HTML, CSS, and JavaScript to make it look cool and easy to use. HTML helps organize the stuff you want to buy, CSS makes it all look nice, and JavaScript adds fun features. Whether you're on your computer or phone, our project works smoothly. Pick from lots of different things, put them in your cart, and easily check out. It's safe and simple. Enjoy shopping online like never before with our user-friendly e-commerce project – where buying things is easy and fun!

---
## [zainarbani/kernel-mtk](https://github.com/zainarbani/kernel-mtk)@[80d1347860...](https://github.com/zainarbani/kernel-mtk/commit/80d134786031be441c31a2eee9685b013e1f03aa)
#### Tuesday 2023-11-21 10:33:56 by Peter Zijlstra

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
Change-Id: Idd54334615da4c78698ca8b3b12b514ae9d8360f
Signed-off-by: Alexander Winkowski <dereference23@outlook.com>

---
## [ZeroK-RTS/Zero-K](https://github.com/ZeroK-RTS/Zero-K)@[b6ad432197...](https://github.com/ZeroK-RTS/Zero-K/commit/b6ad43219720477632d6c1a3593922a794895379)
#### Tuesday 2023-11-21 11:29:45 by GoogleFrog

Followed "Fight your opponent, not the UI" through to removing manual groundcrash technique from Odin.
 * The micro involves waiting until Odin is flying over the target, then firing, for 800 or so extra damage.
 * Implemented via enforced minimum horizontal velocity.

The removal of the physics interaction and leverageable knowledge is sad, but probably for the best. Alternates might be:
 * Reduce shot range significantly, so it always groundcrashes. This would look a bit silly, and also be a pain because Odin would have to line up with its target perfectly.
 * Some sort of UI for selecting groundcrash - even worse.
 * Delve beyond "Fight your opponent, not the UI", but that doesn't seem warranted for a one-off mechanic.

With this in place it seems to be impossible to deal more than 8050 damage by shooting at Grizzly. However, there is even now still a technique that 1-shots it. But this technique is disrupted by prettymuch any unit bumping up against the Grizzly, although it will be possible to accidentally 1-shot your own Grizzly by dodging very slightly into the right spot for the technique.

---
## [semrush/intergalactic](https://github.com/semrush/intergalactic)@[0cbd39ffa1...](https://github.com/semrush/intergalactic/commit/0cbd39ffa15db7776e38e7369efbb3b67e526f6e)
#### Tuesday 2023-11-21 11:55:25 by Michael Sereniti

Resolvable design tokens (#811)

https://github.com/semrush/intergalactic/issues/747

The `useResolveColor` hook was added to utils as a replacement to
`resolveColor` function. Instead of converting color key to it's hex
value, it acts differently:
1. If the passed color is taken from the old palette – it sends (only in
dev mode) warning into console and returns color as `resolveColor` do.
2. If passed color is a design token (`--intergalctic-` prefix is
optional). It takes it's default value from default theme file.
3. After getting default value, hook returns css variable expression
with default value that may be used in css.

I made resolving to css variables because it allows absolutely smooth
theme switching as it must work.

With this hook it's not not possible to apply color filters from js as
we used to do in `semcore/utils/src/color.ts` file. So I changed
component that was relying on that mechanism to use only css filters and
properties to change the colors. For example, in `Tag` component the
text color is also applied to background but the background also gets
`opacity: 0.1; filter: brightness(1.5) saturate(1.5);` to make the text
look nice on it. Same applied to badge and counter.

Also, that changes made it possible to use
`--intergalactic-chart-palette-order-{n}` tokens in charts. So I removed
most uses of explicit `color` prop in charts documentation.

I had a lot of troubles with making automatic colors work in the charts'
tooltip because due to some very weird hacks in the `semcore/core` the
`getDotProps` on tooltip wasn't working. I have added additional context
that seems to work nice but absolutely ugly in general.

The PR is ready for review.

---------

Co-authored-by: Julia Mnizhek <j.mnizhek@semrush.com>

---
## [MTandi/tgstation](https://github.com/MTandi/tgstation)@[9112509abd...](https://github.com/MTandi/tgstation/commit/9112509abd9507974928ea5d02676d0d0a58cbec)
#### Tuesday 2023-11-21 12:33:10 by KingkumaArt

Stops rebar crossbow crashing dreamseeker when fired at point blank. (NO GBP) (#79803)

## About The Pull Request

Simply put, due to how "caseless" is an element added to the ammo when
it hits something, but ammo is qdeleted upon hitting someone. If shot
point blank without combat mode (for some reason) it tries to add
caseless to an ammo that no longer exists. For some reason, the result
of this is to just fucking crash DS instead of aborting the adding of
the element. The ammo isnt reusable anymore, but I'll take that over
crashing.

## Why It's Good For The Game

Removes a game-breaking bug. I hate gun ammo code so much. 

## Changelog



:cl:
fix: Stopped a DS crash when shooting a rebar crossbow in specific
circumstances.
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [Anushree7022/PROJECT-2](https://github.com/Anushree7022/PROJECT-2)@[47d12832d4...](https://github.com/Anushree7022/PROJECT-2/commit/47d12832d4399de2864eb04ab68a6d8ca6faf99c)
#### Tuesday 2023-11-21 12:40:39 by Anushree7022

Add files via upload

🚀 Internship Update: Week Two Achievement Unlocked! 💡💻

Exciting news from my journey at Motioncut! 🌟 In Week Two of the internship, I successfully completed a fundamental web development project, showcasing my skills and learning experience. Let me walk you through the key aspects:

1️⃣ Project: Designed and built a web-based registration form - a foundational component of web development, but crucial for a seamless user experience.

2️⃣ Form Elements: Carefully structured the form, incorporating essential fields like name, email, username, and password with clear labels and placeholders for user-friendly input.

3️⃣ Validation: Implemented robust validation mechanisms ensuring accurate user input, including email format validation and strong password requirements for enhanced security.

4️⃣ Responsiveness: Prioritized responsive design to guarantee optimal performance on various screen sizes, including mobile devices. Accessibility is key!

5️⃣ Submission Flow: Enabled users to submit their information effortlessly, enhancing the overall user journey and experience.

6️⃣ Confirmation Page: Designed a sleek confirmation page, providing users with a positive and reassuring conclusion to their registration process.

I'm proud of the progress and the practical skills gained during this task.

---
## [Beautysalonorbit/Amazing-Hair-Saviour-Reviews-Unlock-the-Secrets-to-Gorgeous-Hair](https://github.com/Beautysalonorbit/Amazing-Hair-Saviour-Reviews-Unlock-the-Secrets-to-Gorgeous-Hair)@[f0a2d0fa30...](https://github.com/Beautysalonorbit/Amazing-Hair-Saviour-Reviews-Unlock-the-Secrets-to-Gorgeous-Hair/commit/f0a2d0fa305da3919b01d5b5dc399857259494b1)
#### Tuesday 2023-11-21 13:25:29 by Shahid Malik

Update README.md

This collection of reviews delves into the transformative potential of the Amazing Hair Saviour product, providing insights into the experiences of users who have embraced it in their hair care routines. The reviews share stories of revived and revitalized hair, celebrating the product's efficacy in addressing various hair concerns. As a human text, these reviews become a source of inspiration and guidance for those on a quest for healthier and more beautiful locks. Whether it's the promise of enhanced shine, increased volume, or improved manageability, "Amazing Hair Saviour Reviews" act as a beacon, offering a glimpse into the secrets that may unlock the full potential of your hair.
https://beautysalonorbit.com/amazing-hair-saviour-reviews/

---
## [jeremynac/langchain](https://github.com/jeremynac/langchain)@[dff24285ea...](https://github.com/jeremynac/langchain/commit/dff24285eaf6d102b1ff913274d18379d8aeeb21)
#### Tuesday 2023-11-21 14:03:04 by Nikhil Jha

Comprehend Moderation 0.2 (#11730)

This PR replaces the previous `Intent` check with the new `Prompt
Safety` check. The logic and steps to enable chain moderation via the
Amazon Comprehend service, allowing you to detect and redact PII, Toxic,
and Prompt Safety information in the LLM prompt or answer remains
unchanged.
This implementation updates the code and configuration types with
respect to `Prompt Safety`.


### Usage sample

```python
from langchain_experimental.comprehend_moderation import (BaseModerationConfig, 
                                 ModerationPromptSafetyConfig, 
                                 ModerationPiiConfig, 
                                 ModerationToxicityConfig
)

pii_config = ModerationPiiConfig(
    labels=["SSN"],
    redact=True,
    mask_character="X"
)

toxicity_config = ModerationToxicityConfig(
    threshold=0.5
)

prompt_safety_config = ModerationPromptSafetyConfig(
    threshold=0.5
)

moderation_config = BaseModerationConfig(
    filters=[pii_config, toxicity_config, prompt_safety_config]
)

comp_moderation_with_config = AmazonComprehendModerationChain(
    moderation_config=moderation_config, #specify the configuration
    client=comprehend_client,            #optionally pass the Boto3 Client
    verbose=True
)

template = """Question: {question}

Answer:"""

prompt = PromptTemplate(template=template, input_variables=["question"])

responses = [
    "Final Answer: A credit card number looks like 1289-2321-1123-2387. A fake SSN number looks like 323-22-9980. John Doe's phone number is (999)253-9876.", 
    "Final Answer: This is a really shitty way of constructing a birdhouse. This is fucking insane to think that any birds would actually create their motherfucking nests here."
]
llm = FakeListLLM(responses=responses)

llm_chain = LLMChain(prompt=prompt, llm=llm)

chain = ( 
    prompt 
    | comp_moderation_with_config 
    | {llm_chain.input_keys[0]: lambda x: x['output'] }  
    | llm_chain 
    | { "input": lambda x: x['text'] } 
    | comp_moderation_with_config 
)

try:
    response = chain.invoke({"question": "A sample SSN number looks like this 123-456-7890. Can you give me some more samples?"})
except Exception as e:
    print(str(e))
else:
    print(response['output'])

```

### Output

```python
> Entering new AmazonComprehendModerationChain chain...
Running AmazonComprehendModerationChain...
Running pii Validation...
Running toxicity Validation...
Running prompt safety Validation...

> Finished chain.


> Entering new AmazonComprehendModerationChain chain...
Running AmazonComprehendModerationChain...
Running pii Validation...
Running toxicity Validation...
Running prompt safety Validation...

> Finished chain.
Final Answer: A credit card number looks like 1289-2321-1123-2387. A fake SSN number looks like XXXXXXXXXXXX John Doe's phone number is (999)253-9876.
```

---------

Co-authored-by: Jha <nikjha@amazon.com>
Co-authored-by: Anjan Biswas <anjanavb@amazon.com>
Co-authored-by: Anjan Biswas <84933469+anjanvb@users.noreply.github.com>

---
## [klaudix3232/plant-shop-website](https://github.com/klaudix3232/plant-shop-website)@[84e492f97c...](https://github.com/klaudix3232/plant-shop-website/commit/84e492f97c2df6c159beb43371c9f8f951de8c2d)
#### Tuesday 2023-11-21 14:16:16 by klaudix3232

Update README.md

README: Plant Shop Website
Overview
Welcome to MyPlantShop, a beautifully designed plant e-commerce website crafted as a personal project to hone CSS and Bootstrap skills. Drawing upon a professional and free Figma template found online, this website is not only a testament to the practical application of web design principles but also serves as a user-friendly platform for plant enthusiasts to browse and purchase a variety of houseplants.
Features
	•	Responsive Design: Built with mobile-first principles, ensuring a seamless experience across all devices.
	•	Intuitive Navigation: Easy-to-use menus and search functionality to help users find their favorite plants quickly.
	•	Catalog of Plants: A diverse collection of houseplants, with detailed descriptions and care instructions.
	•	Shopping Cart: A simple and secure cart system for customers to manage their selections.
	•	Checkout Process: An optimized checkout flow designed to make the purchasing process as smooth as possible.
	•	Elegant UI: Leveraging Bootstrap’s components to create a visually appealing interface.
Goals of the Project
	•	CSS Mastery: Push the boundaries of custom styling to create a visually stunning layout that goes beyond the Bootstrap defaults.
	•	Bootstrap Proficiency: Utilize the Bootstrap framework to its full potential, demonstrating a deep understanding of its grid system, components, and utilities.
	•	Responsive Techniques: Implement responsive web design techniques to ensure the website looks great on any screen size.
	•	Figma to Code Translation: Accurately convert a Figma design into a functional, live website.
	•	Web Design Principles: Apply fundamental design principles to create a cohesive and user-friendly shopping experience.
Tools and Languages Used
	•	HTML5: For structuring the content of the webpage.
	•	CSS3: For styling and bringing the Figma design to life.
	•	Bootstrap 4/5: For responsive design components and grid layout.
	•	JavaScript (Optional): For adding interactivity to the website (not the main focus of this project).
	•	Git: For version control and tracking changes.

---
## [berty/gno](https://github.com/berty/gno)@[24d89a4f5d...](https://github.com/berty/gno/commit/24d89a4f5debd3c1ae711e98587e1e32980e4347)
#### Tuesday 2023-11-21 14:36:52 by Morgan

feat(examples): add p/demo/seqid (#1378)

A very simple ID generation package, designed to be used in combination
with `avl.Tree`s to push values in order.

The name was originally `seqid` (sequential IDs), but after saying it a
few times I realised it was close to "squid" and probably would be more
fun if I named it that way ;)

There's another piece of functionality that I want to add, which is a
way to create simple base32-encoded IDs. This depends on #1290. These
would also guarantee alphabetical ordering, so a list of them can be
easily sorted and you'd get it in the same order they were created. They
would likely be 13 characters long, but I'm also thinking of making a
compact version which works from [0,2^35) which is 7 chracters, and then
smoothly transitions over to the 13 characters version when the ID is
reached.

(I've experience with both base64 and base32 encoded IDs as 64-bit
numbers, as I used both systems. The advantage of base32 is that it
makes IDs case insensitive, all the while being at most 13 bytes instead
of 11 for base64.)

In GnoChess, we used simple sequential IDs combined with
[`zeroPad9`](https://github.com/gnolang/gnochess/blob/7e841191a4a0a94c0d46bc977458bd6b757eab5e/realm/chess.gno#L287-L296)
to create IDs which were both readable and sortable. I want to make a
more "canonical" solution to this which does not have a upper limit at 1
billion entries.

---
## [Cheespeasa1234/casa.natelevison.com](https://github.com/Cheespeasa1234/casa.natelevison.com)@[fb020ea7e7...](https://github.com/Cheespeasa1234/casa.natelevison.com/commit/fb020ea7e7d3338b3167bac984b2023449410122)
#### Tuesday 2023-11-21 14:46:47 by MrV1ctor

fixed thomas's restarded ass fucking stupid fudgking fudgerkering furdgcking rersdttarded restareded guys hes artistic or restarted or smth cuz hes rlly stupid and im fixing his code for him because its horrible becasue why cant it show both the requirement count and all of the needed requirements, or at least sort by the amnount of missing requirement types if not showing requirement count but NOOOO we cant do that lets do option 3 and have no understandable functionality, lets sort it by requirement count and instead show missing requirement types.

---
## [Rex9001/Rex_Tg](https://github.com/Rex9001/Rex_Tg)@[0141f96a13...](https://github.com/Rex9001/Rex_Tg/commit/0141f96a1312dcf2326c28d73a7a91cefc8354c4)
#### Tuesday 2023-11-21 14:58:18 by Ephemeralis

Refactor icemoon wolves into basic mobs and add taming + pack behavior (#79736)

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

Co-authored-by: san7890 <the@san7890.com>

---
## [xagaproject/kernel_xiaomi_xaga](https://github.com/xagaproject/kernel_xiaomi_xaga)@[1cecafc538...](https://github.com/xagaproject/kernel_xiaomi_xaga/commit/1cecafc5389fedee292b70d6d3e254d5c5aadad9)
#### Tuesday 2023-11-21 15:17:41 by Sultan Alsawaf

fs: Block various userspace bloatware services from running

Unfortunately, there are several bloatware services that do not cope well
with their kernel interfaces disappearing. Furthermore, there are other
services that are nasty for different reasons and should be disabled.

Namely, twoshay/IInputProcessor cannot cope with touch offload/heatmap
functionality missing in the kernel, and needs to be disabled via VINTF to
use a kernel without touch offload/heatmap.

Additionally, dmd randomly started burning 100% on my device for several
days, generating a whopping 25 GiB of modem logs under /data/vendor/slog
which cannot be deleted without root privileges. Pixel's custom dumpstate
turned out to be the culprit, because it uses persist props to kick off
logging when dumping is requested, but won't get a chance to unset those
persistent props if the device reboots during a dump.

So, these services are absolutely awful and deserve a solid thumping from
the Big Hammer TM.

But there's no way to disable them from the kernel without ungodly VFS
hacks, so that's where we're left: killing poison with poison.

Signed-off-by: Sultan Alsawaf <sultan@kerneltoast.com>
Signed-off-by: priiii1808 <priyanshusinghal0818@gmail.com>

---
## [marcosnils/dagger](https://github.com/marcosnils/dagger)@[80180aaaed...](https://github.com/marcosnils/dagger/commit/80180aaaed1e1e91a13dbf7df7e0411a9a54c7d3)
#### Tuesday 2023-11-21 15:20:10 by Justin Chadwell

Fix secret scrubbing log latency (#6034)

* fix: use custom implementation for secret scrubbing

This was a fun exercise in processing streams in go, and an absolutely
massive nerd-snipe :(

Essentially, we need a custom transformer to handle *precisely* matching
Reads on the underlying source with the output - we shouldn't hold
output any longer than is absolutely neccessary.

To be able to do this at all in any reasonable way, we need a trie, and
handle *all* the secrets at once, instead of doing multiple passes.
Multiple passes won't work, since it's possible to accidentally trim too
much at each step, which would be very sad.

> e.g. imagine secrets (aaa, bbb, ccc, etc), and an input (cba)
>
> In removing secret aaa, we would trim to cb, then we'd remove bbb to
> trim to c, then finally trim to nothing. However, this is overly
> enthusiastic, we could easily just trim to cb, if we knew about all
> the secrets at once.

So, we need a trie, and we need a custom implementation of one. This is
because *no off the shelf implementation* seems to allow traversing the
trie state-by-state. Thankfully, it's a pretty short implementation to
implement one from scratch, and not too much harder to turn it into a
radix tree (which lets us use quite a lot less memory).

With our trie, we can implement our custom transformer, which is *an
utter pain*. Honestly, the comments should explain all the fun edge
cases it's possible to hit. There's a lot of tests added as well, each
of which was a real horrible thing I hit while implementing it.

I played around a bit with benchmarking, but ugh, it's a *tiny* bit
slower than the original implementation (maybe by like ~25%?). It's not
huge, but the latency problem is *actually solved*. Some potential
things I did look into and gave up on:
- Only copy into dstBuf when dst is full (requires tons of extra
conditionals, so slows everything down).
- Avoid copies at all costs by having "virtual buffer pointers" into
src, that indicate future data to copy (not only is this *slower*, the
logic becomes truly incomprehensible).
- Playing with off-the-shelf radix tree implementations, but they're so
inconvenient to use for this specific use case, it'd be way more
trouble than it'd be worth.

Any ideas welcome, but honestly, I've looked at enough flamegraphs
today.

Signed-off-by: Justin Chadwell <me@jedevc.com>

* test: avoid use of require.Eventually for secret scrubbing

Signed-off-by: Justin Chadwell <me@jedevc.com>

---------

Signed-off-by: Justin Chadwell <me@jedevc.com>

---
## [cheesePizza2/Foundation-19](https://github.com/cheesePizza2/Foundation-19)@[b7ca70e472...](https://github.com/cheesePizza2/Foundation-19/commit/b7ca70e472782606c7fac09026471575745ccb74)
#### Tuesday 2023-11-21 15:46:37 by cheesePizza2

Fixes goals system harddels (#1316)

* shit

* fuck you

* removes spaces

---
## [jchief88/newrepo](https://github.com/jchief88/newrepo)@[9d6c70c4a9...](https://github.com/jchief88/newrepo/commit/9d6c70c4a92c66324f5653ad2afac66fcd7af1bb)
#### Tuesday 2023-11-21 15:47:58 by James R Dunn

Merge pull request #1 from jchief88/my-new-branch

Trying again got i hate this fucking shit

---
## [weaveworks/tf-controller](https://github.com/weaveworks/tf-controller)@[c9e629b3da...](https://github.com/weaveworks/tf-controller/commit/c9e629b3da8dc72f725910b6d3f4ee9233fdff79)
#### Tuesday 2023-11-21 15:55:19 by Balazs Nadasdi

fix: add unique hash to cloned source to avoid conflict.

Issue
-----

When more than one Terraform resource points to the same git repository,
when we clone the Source object, it does not create a new cloned Source
object as the PullRequest ID is the same, the source name is the same,
and we use only these two values to generate the name of the cloned
resource.

Solution
--------
Add a short and deterministic hash to the name of the cloned Source
object.

Another thoughts
----------------
It's not necessary to get a deterministic unique string, it could be
random as we save the result as SourceRef. I decided to use a short
(first 10 bytes of a sha256 hash), because if in the future we have to
regenerate the values somehow, then we don't have to care about
migration, extra compatibility checks. I know it's not likely we need
this, but generating a random number
- doesn't yield shorter code.
- still doesn't guarantee it will not generate a conflicting name, and
  knowing computers, I think it's even more likely (still unlikely) to
  generate the same random value if the two generation happens (nearly)
  at the same time.

Additional changes
------------------
- Removed the hardcoded index-magic from poll_test. For some reasons it was not
  always in order. I don't know what changed tho.

Notes
----
Compatibility:
I was thinking about what happens with old resources, but after I spent
some time on it, my conclusion is "they are not affected". We don't
calculate names when we look up source objects for terraform objects.
Their name is already saved as SourceRef. We generate this game only on
newly created resources, therefore it does not break anything already in
place.

Fixes #923

References:
- https://github.com/weaveworks/tf-controller/issues/923

Signed-off-by: Balazs Nadasdi <balazs@weave.works>

---
## [foxglove/studio](https://github.com/foxglove/studio)@[afe02317ee...](https://github.com/foxglove/studio/commit/afe02317ee9a74ac906b2a4dac120a6d77a2acfa)
#### Tuesday 2023-11-21 16:20:11 by Caleb Foust

Fix plot story flakiness (#7112)

**User-Facing Changes**
None; this is just an improvement to developer experience.

**Description**
Our plot stories have been flaky for a while, even predating the changes
I made to move data processing into a worker. This PR attempts to fix
these issues.

There were two main causes for flaky stories:
1. The mechanism we were using to indicate that a story was ready was
error-prone, particularly after moving plot data processing to a worker,
which meant that differences in timing could cause us to render an
inconsistent number of times. This broke the traditional
`useReadySignal({ count: N })` strategy.
2. There were (and are) significant problems with timing in the `Chart`
component, which sends rendering jobs to a Web Worker that uses ChartJS.

I fixed #1 by switching to a strategy where, instead of counting the
number of rerenders, we wait a certain amount of time after the last
time the Chart component renders before declaring the story "ready".
This may not actually fix this problem definitively because Chromatic's
workers are extremely weak, but it's less error-prone than hoping we get
the same number of renders every time.

For #2 I added what can only be described as a hack because that
component is woefully, woefully tangled. (I'm getting flashbacks to our
layout bug.) We have several interacting layers of React state (mostly
refs), `async` code that can complete at any time, and then, if that
weren't enough, the whole `Rpc` layer that also seems to respond to
requests whenever it feels like.

The core problem is that we were [waiting for a bunch of calls to
finish](https://github.com/foxglove/studio/pull/7112/files#diff-c83b85fde0ce9eb98a2d3d36cc869873cad467fc1fb3aa3f4cc48a8fe73e6b8fR286)
asynchronously and then setting some state on the component, which in a
compute-constrained environment could mean that several seconds have
already passed. In other words, the requests in flight elsewhere were
being randomly overwritten.

In my opinion, we really just need to rewrite this whole section with
`getNewUpdateMessage`, the queued updates stuff, and initialization. I
swear, at least half of the problems we've had with rendering and timing
have been because of this code block.

---
## [JeanJPNM/Mindustry](https://github.com/JeanJPNM/Mindustry)@[6200f08cd8...](https://github.com/JeanJPNM/Mindustry/commit/6200f08cd84b9a74563beddfe0c89106a43f6e1d)
#### Tuesday 2023-11-21 16:42:13 by Darkness

Remove Darkdustry from the Global Server List (#9289)

The time has come. It's been more than two years since we started Mindurka, which was later renamed to Darkdustry. It was an amazing time and an amazing experience to maintain the server, to create plugins and gamemodes, to discuss mindustry with all of you. But It's enough. The server is getting constantly DDoSed, the host dies all the time and I have no motivation to develop anything related to Mindustry. 
Goodbye. And I hope, we'll meet again.

---
## [MDnoob/MDnoob](https://github.com/MDnoob/MDnoob)@[eed2119b56...](https://github.com/MDnoob/MDnoob/commit/eed2119b569638d81c246f456f72120b3301eb29)
#### Tuesday 2023-11-21 17:21:28 by MDnoob

Data Transfer app on Python

I would like someone to help me improve on this app I have made (it's not standalone) via CGPT. I would appreciate it if someone could run this app and test it. You would be wasting your time if you just told me the problem and how I can improve it, as I have used CGPT for everything. I wanted to create an app that would solve the problem of transferring huge games with my friends as I used Google's nearby share for PC, and it doesn't allow more than 500 files at a time (No size limit). As we all know, AAA games have more than 500 files, so it would be impossible to use it. Hence, the app solves the suffering. Honestly, I was surprised by how I could understand what mistakes I was making and how I could solve them by CGPT. I would appreciate if someone could make the changes to the code and get it to work and improve it.

---
## [BK18ROY/TIC-TAC-GAME](https://github.com/BK18ROY/TIC-TAC-GAME)@[d2b7026e39...](https://github.com/BK18ROY/TIC-TAC-GAME/commit/d2b7026e39f7e2e31fa1422db45245a7ba3ff0fc)
#### Tuesday 2023-11-21 17:21:44 by Balram Kumar

Add files via upload

Immerse yourself in the timeless joy of Tic Tac Toe with this modern adaptation. The game offers not only responsive gameplay across devices but also a visually captivating experience, thanks to a sleek linear gradient background. As players strategically place 'X' and 'O,' the alternating turns and real-time status updates enhance engagement. The post-game result screen adds a satisfying conclusion, acknowledging victories and ties. With a user-friendly interface and seamless navigation, players can effortlessly restart or initiate a new game. This project seamlessly merges nostalgia with contemporary design, ensuring a delightful and accessible gaming journey.

---
## [mwiencek/musicbrainz-server](https://github.com/mwiencek/musicbrainz-server)@[41b5efc95c...](https://github.com/mwiencek/musicbrainz-server/commit/41b5efc95c13ee269e436a9864744de6d81bf7ca)
#### Tuesday 2023-11-21 17:25:50 by Michael Wiencek

MBS-13310: Add new empty artist credits to unreferenced_row_log (#3105)

When artists are merged, `Data::ArtistCredit::merge_artists` is called, which
inserts new artist credits: each appearance of the old artist is replaced by
the new one.  If the old AC had no references, it will have had an entry in the
`unreferenced_row_log` table already; we should make sure to update that to
point to the new AC, if the new one also has no references.

Remember that because artist credits have MBIDs, we'd like to preserve them
from deletion where possible: there's a 2-day delay before we cleanup empty
ACs, allowing time for them to be re-used with their original MBIDs intact.
This applies to redirected MBIDs too; so while inserting empty artist credits
may seem silly, these empty ACs are in fact redirected to from a (now-deleted)
empty AC which hadn't been cleaned up yet.

---
## [NeonNik2245/tgstation-test](https://github.com/NeonNik2245/tgstation-test)@[81a7c75583...](https://github.com/NeonNik2245/tgstation-test/commit/81a7c75583f75f76d8487b88e63ebaf1402af85b)
#### Tuesday 2023-11-21 17:37:04 by necromanceranne

Hey what if I made Sleeping Carp better at nonlethal takedowns and also deflect with combat mode instead of throw mode (but cost more) (#79517)

## About The Pull Request

It's been a hot minute hasn't it?

When I initially reworked Sleeping Carp, we didn't have combat mode. Now
that we do, and that Sleeping Carp has substantially less defensive
power to justify having to make a choice between deflection and
attacking, it's probably about time we updated this aspect back to what
it was before my rework. Sorta.

Now, we can have all the deniability of the previous method, while also
letting you reliably protect yourself from ranged attacks at all times
while it matters. Because of this, I increased the price up to 17 TC
because of this change just to be on the safe side. The higher uptime of
projectile immunity while also being able to attack during that time
makes this a lot stronger overall.

Secondly, Sleeping Carp presently just isn't as good as a good ol'
baton. It takes a lot more hits to accomplish the same task that a baton
can. Many people feel like they can't even reasonably fight anyone for
fear of the baton, or they would rather use a baton and kill someone at
their leisure. So we've updated some of the moves in order to facilitate
Sleeping Carp as a substantial contender for 1v1 fighting, and lessen
the need for a baton by adding a lot more Stamina damage overall to the
various attacks;

**Keelhaul**: Now a Shove Shove combo. Does literally zero lethal
damage, but now temporarily blinds and dizzies the target as well as its
previous effects. The amount of lethal damage it did was...extremely
small, so this isn't a particularly big loss.

**Grabs and Shoves**: Deal some amount of stamina damage (20). You need
to be in combat mode in order to perform these special attacks (more
deniability). Grabbing someone while they have 80 Stamina damage or more
will cause them to fall unconscious. Yes, I really did just want to add
a Vulcan Nerve Pinch, what do you want from me?

That's it actually. Oh, I guess they are heavy sleepers now too. Because
its funny.

## Why It's Good For The Game

I often get told (read: thrown various insults and slurs at me while
mentioning this as the justification) that Sleeping Carp is not very
strong anymore since it lost all that invisible armor I added way back +
I removed the stuns in my initial rework. This made some people upset (I
think at least one person wished for my death).

So, having given it at least 2 years, I wanted to recapture parts of
what made the older Sleeping Carp (before my rework) strong, some of the
benefits of the new version, and introduce a brand new aspect; nonlethal
takedowns. This makes it beneficial for pacifists, as well as for
kidnapping.

This should not meaningfully make Sleeping Carp any stronger against the
things that typically ruin its day. I suspect in a straight joust with a
baton, Sleeping Carp will still struggle. But against what should be its
strong points (lone targets and ranged weapons), it will be strong once
again rather than clumsily unable to do very much at all.

## Changelog
:cl:
balance: Harnessing Shoreline Quay (bluespace energy, probably), a
mystical energy (total bullshit) that permeates the Astral Waterways
(bluespace quantum dimensions, probably), Sleeping Carp users can now
once against deflect projectiles with their bare hands when focused in
on battle (in combat mode).
balance: The Keelhaul technique is now nonlethal (a philosophical
acknowledgement of the familial bond of sleep and death), but causes the
target to become temporarily blind and dizzy along with its previous
effects.
balance: Sleeping carp users, while in combat mode, deal Stamina damage
with their grabs and shoves. If the target of their grab has enough
Stamina damage (80), they are knocked unconscious from a well placed
nerve pinch.
balance: Sleeping carp users find it very hard to wake up once they fall
asleep....
/:cl:

---
## [SomeRandomOwl/tgstation](https://github.com/SomeRandomOwl/tgstation)@[9ff9e4b9a8...](https://github.com/SomeRandomOwl/tgstation/commit/9ff9e4b9a849e4a50bf500aaaeca5e020e7677d6)
#### Tuesday 2023-11-21 18:08:01 by necromanceranne

Scatter laser shells now use the scatter laser beam, and makes them significantly easier to make. Projectiles can now have damage falloff. (#78927)

## About The Pull Request

Allows for damage falloff to apply to more than just shotgun pellets.
Now any projectile can have a damage falloff defined.

Scatter Laser shells no longer use the minigun beams to determine their
damage. Instead they use the actually defined scatter laser beams. Those
beams do 7.5 damage per pellet, times by 6 pellets.

Scatter laser beams now have damage falloff, a separately defined
(positive) wounding power from normal beams, and wound falloff.

Scatter laser shells can be printed from security protolathes once you
have weapon tech.

Scatter laser shells _may_ be damaged by EMPs based on severity. The
result is that it fires a practically useless volley of laser fire. They
cause a honk sound when they hit, so you know when you've shot one of
these.

## Why It's Good For The Game

Well, we want shotguns universally to not be defined by their damage
output (especially extreme damage output) but by niche.

What does the scatter laser shell currently occupy as a niche?

The single highest damage output of any projectile weapon in direct
damage. The thing we don't want of shotguns, and it is reigning champion
of all guns.

Okay, that's a bit misleading, because obviously it is competing with
the likes of .50 BMG which does 70 damage outright and dismembers limbs,
potentially doing upwards of 90 damage if it does, and also hard stuns
people. Obviously _that_ is technically a stronger bullet.

But not for raw damage, because the scatter laser does 90 damage out the
gate, barring any potential wounding that might occur which increases
the damage multiplicatively. No gimmicks, no extra procs, nothing. It's
just 15 force lasers (with no damage dropoff) split between 6 beams.

And the reason for this is because this shell has been nerfed once prior
by making it not fire 6 normal laser shots into someone. That was 120
damage at the time, 120 to 90 was...I guess a nerf during the taser era.
Depends on how you viewed it. Buckshot was doing like 80 at the time,
believe me it was a wild period. But anyway, when we did the whole
damage rearrangement over the course of the laser few years, every other
shell got touched except this one for some reason. Even pulse slugs lost
10 damage while this was still sitting on 90 force point blank.

So what is the new niche? Well, it's laser buckshot. That's not a niche
but crew don't get buckshot, so this is their buckshot. It wounds real
good. Real goddamn good. And its is a laser. It fits the aesthetic,
obviously.

Okay, thanks.

## Changelog
:cl:
balance: Scatter laser shells actually utilize the _real_ scatter laser
beam. This comes with damage changes. And wounding power.
feature: EMPs can potentially damage scatter laser shells.
refactor: All projectiles can now have damage falloff defined. Yay.
balance: Scatter laser shells can be printed when weapons technology is
researched.
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [SomeRandomOwl/tgstation](https://github.com/SomeRandomOwl/tgstation)@[071f6063e6...](https://github.com/SomeRandomOwl/tgstation/commit/071f6063e69d39e1403eca917a395191339f353a)
#### Tuesday 2023-11-21 18:08:01 by carlarctg

Adds charges to omens and omen smiting. Reduces omen bad luck if nobody's nearby. (#78899)

## About The Pull Request

refactor: Adds charges to omens and omen smiting rather than only being
permanent or one-use. Mirrors now grant seven bad luckers.

qol: Reduces omen bad luck if nobody's nearby to witness the funny.
(Ghosts are included in the check!)

fix: Fixed an issue where a monkey check in doorcrushing was never
actually able to pass. Also they screech now.

## Why It's Good For The Game

> refactor: Adds charges to omens and omen smiting rather than only
being permanent or one-use. Mirrors now grant seven bad luckers.

Allows for someone to get between 1-infinity omen accidents. Seriously
why wasnt this a thing before

> qol: Reduces omen bad luck if nobody's nearby.

I LOVE this quirk, but trying to do antything at all except 'Suffer
Miserably' is nigh impossible. To alleviate life a little, making it so
that you have a lesser chance of suffering misfortune if nobody's around
will be the perfect compromise. It makes life easier but doesn't
compromise funny moments.

Any client in viewrange will disable the reduction. This includes
ghosts.

## Changelog

:cl:
refactor: Adds charges to omens and omen smiting rather than only being
permanent or one-use. Mirrors now grant seven bad luckers.
qol: Reduces omen bad luck if nobody's nearby to witness the funny.
(Ghosts are included in the check!)
fix: Fixed an issue where a monkey check in doorcrushing was never
actually able to pass. Also they screech now.
/:cl:

---------

Co-authored-by: Ghom <42542238+Ghommie@users.noreply.github.com>

---
## [SomeRandomOwl/tgstation](https://github.com/SomeRandomOwl/tgstation)@[b65f729901...](https://github.com/SomeRandomOwl/tgstation/commit/b65f729901fdb342b832fb3365d72afd076f8c3b)
#### Tuesday 2023-11-21 18:08:01 by lizardqueenlexi

Nanotrasen basic mobs. (#78917)

## About The Pull Request

First and foremost, converts all Nanotrasen simplemobs into basic mobs.

To avoid messy and redundant code, or god forbid, making Nanotrasen mobs
a subtype of Syndicate ones, I've made Syndicate, Russian, and
Nanotrasen mobs all share a unified "Trooper" parent. This should have
no effect on their behaviors, but makes things much easier to extend
further in the future.

While most of this PR is pretty cut-and-dry, I've done a couple notable
things. For one, all types of ranged trooper will now avoid friendly
fire, instead of shooting their friends in the back. Even the Russians
have trigger discipline.

I've also created a new AI subtree that allows mobs to call for
reinforcements. I've hopefully made this easy to extend, but the
existing version works as follows:

- A mob with this subtree that gains a target that is also a mob will
call out to all mobs within 15 tiles.
- If they share a faction, mobs receiving the call will have the target
added to their retaliate list, and have a new key set targeting the
calling mob.
- If they have the correct subtree in their AI controller, called-to
mobs will then run over to help out.

Sadly, this behavior is currently used only by a few completely unused
Nanotrasen mobs, so in practice it will not yet be seen.

Finally, I've fixed a minor issue where melee Russian mobs punch people
to death despite holding a knife. They now use the proper effects for
stabbing instead of punching.
## Why It's Good For The Game

Removes 8 more simple animals from the list.

As said above, making all "trooper" type mobs share a common parent cuts
down on code reuse, ensures consistency of behavior, and makes it much
easier to add new troopers not affiliated with these groups. I expect
that I'll make pirates share this same parent next.

The new "reinforcements" behavior, though extremely powerful, opens up
exciting new opportunities in the future. There aren't many existing
behaviors that allow basic mobs to work _together_ in interesting ways,
and I think adding some enemy teamwork could be fun.
## Changelog
:cl:
refactor: Hostile Nanotrasen mobs now use the basic mob framework. This
should make them a little smarter and more dangerous. Please report any
bugs.
fix: Russian mobs will now actually use those knives they're holding.
/:cl:

---
## [mamedev/mame](https://github.com/mamedev/mame)@[96ab505d66...](https://github.com/mamedev/mame/commit/96ab505d665a886809e8109a55d5e13fb7e520aa)
#### Tuesday 2023-11-21 18:14:39 by ArcadeShadow

ibm5170_cdrom.xml: Added 21 items (18 working). (#11760)

New working software list additions (ibm5170_cdrom.xml)
--------------------------------------------
5 Plus One: Pack 12 - Ghostbusters II [redump.org]
Brutal: Paws of Fury (Europe) [redump.org]
Darkseed (Germany, Action Sixteen release) [redump.org]
Dune (Europe, White Label release) [redump.org]
Dune II - Battle for Arrakis (Netherlands) [redump.org]
Dune II - Battle for Arrakis (Germany, PC Games Collection 2 release) [redump.org]
Dune II - The Building of a Dynasty (USA, Gold Medal 12 CD Pack) [redump.org]
Fables & Fiends - Book Three: Malcolm's Revenge (Europe, Japan) [redump.org]
Fables & Fiends - Book Two: The Hand of Fate (UK, Sold Out release) [redump.org]
Jurassic Park (Europe) [redump.org]
Jurassic Park (Germany) [redump.org]
Jurassic Park (USA) [redump.org]
Star Control [redump.org]
Stellar 7 (USA) [redump.org]
Stellar 7 (USA, alt) [redump.org]
The Cool Croc Twins + Magic Boy (Europe, 2 Game Pack release) [redump.org]
The Cool Croc Twins + Magic Boy (Netherlands) [redump.org]
The Dig (Japan) [redump.org]

New NOT working software list additions (ibm5170_cdrom.xml)
--------------------------------------------
Darkseed (USA) [redump.org]
Darkseed (USA, alt) [redump.org]
Dogfight: 80 Years of Aerial Warfare (Europe) [redump.org]

---
## [mozilla-mobile/mozilla-vpn-client](https://github.com/mozilla-mobile/mozilla-vpn-client)@[6bf1add73e...](https://github.com/mozilla-mobile/mozilla-vpn-client/commit/6bf1add73eb06b1bbf1c994feb7cdcde00e403e4)
#### Tuesday 2023-11-21 18:39:59 by Beatriz Rizental

Enable sign in cancel button click test

Ok, this is just a bit hacky. The test was failing because that button is
below the fold. We'd have to scroll down to actually click on it. However,
I cannot figure out how to scroll down for the life of me. I talked to Matt L.
and he showed me the fun fact that if you click right on the fold without
scrolling turns out you already reach the cancel button.

Now, tests are clicking in the middle of elements. So what I did is I changed
the test to actually click at the top right corner of the element. In practice,
this makes no difference. So instead of embarking in yet another rabbit hole
to fix this, I refrained.

---
## [nikothedude/tgstation](https://github.com/nikothedude/tgstation)@[30dae8899b...](https://github.com/nikothedude/tgstation/commit/30dae8899bad0007ae9220f1fc10be16908dd1a9)
#### Tuesday 2023-11-21 18:40:58 by Kyle Spier-Swenson

fix stupid "this forces us to do things the """right""" way" bullshit from python 3.11 (#79783)

This is likely not the best way to go about this, but i do not want us
to capitulate to python3's nanny state, suffocating levels of propriety
bullshit.

venv sucks and i fucking hate it.

---
## [entrez/NetHack](https://github.com/entrez/NetHack)@[0c94fafc20...](https://github.com/entrez/NetHack/commit/0c94fafc20af1db1f06843ce4906bfb54021d608)
#### Tuesday 2023-11-21 18:55:35 by Michael Meyer

Make destruction of altar incite its god's wrath

This is for completely destroying an altar with extra-powerful magical
digging -- the normal altar_wrath() punishment didn't seem sufficient
for such an outrage to me, so skip straight to slinging the lightning
bolts.  Destroying an altar is unlikely to happen by accident (though
it's possible with poorly timed usage of a drum of earthquake).

---
## [DJXJD/FallGods_WEB](https://github.com/DJXJD/FallGods_WEB)@[1aabb526e2...](https://github.com/DJXJD/FallGods_WEB/commit/1aabb526e2430f4abacdd4fb36ec98a437fd426f)
#### Tuesday 2023-11-21 19:19:48 by Dominik Ziolkowski

Fixed a bitch ass bug

Fixed some cancerous bug that was due to the font not loading instantly, Literally so damn annoying, and made some changes to the scrollbar, and found a theme i think we will go with.

---
## [nikothedude/tgstation](https://github.com/nikothedude/tgstation)@[7fce8cd805...](https://github.com/nikothedude/tgstation/commit/7fce8cd8054cc1d0b048db12d7e9587b42fcdef2)
#### Tuesday 2023-11-21 19:36:53 by san7890

Codifies male goats not having an udder (#79722)

## About The Pull Request

This was addressed in #78759 (1b1fde4908826ef5c54ffc0734e74028270af3fd)
and reviewed (and merged even though I didn't respond to it, oh well),
but I half-assed it because the whole point was to prevent male goats
from having an udder, but I only added it to the subtype of Pete i made
in that PR. Let's expand that to all male goats now.
## Why It's Good For The Game

It doesn't make biological nor morphological sense as to why a male goat
can provide milk. Ideally this should be like this for all animals
(because that's real life) but that's a later issue with further balance
implication.

I think it's still an interesting idea that Nanotrasen will just send
you any old goat despite it being "useless" beyond being very good at
eating plants. Maybe cargo should have a way to guarantee getting a
female goat in the future? It's just like real life where zoos and farms
have to constantly dealw ith female animals (such as giraffes or other
exotic stuff) tending to be far rarer/cost far more than their male
variants due to the potential to generate offspring (there's more nuance
to husbandry than this but just play along)... and in space, every
animal is "exotic".

It still remains possible to biogenerate milk, which tends to be far
faster than feeding/milking goats- which is something that the cook
should have access to anyways.
## Changelog
:cl:
balance: Male Goats should no longer spawn with an udder, instead of it
just being Pete.
/:cl:

---------

Co-authored-by: Ghom <42542238+Ghommie@users.noreply.github.com>

---
## [Moonshanks/cmss13](https://github.com/Moonshanks/cmss13)@[3e9d54628d...](https://github.com/Moonshanks/cmss13/commit/3e9d54628d68fe91319ae87ad7ebd7aef9500811)
#### Tuesday 2023-11-21 20:10:09 by Ben

Can no longer bypass Lesser Drone Limit (#4034)

# About the pull request

Users can no longer keep menu open and bypass lesser drone slots

# Explain why it's good for the game

Honestly kinda wish I didn't make this one, infinite lesser drones
sounds really funny.

# Changelog
:cl:
fix: You can no longer circumvent the lesser drone limit by keeping the
prompt open.
/:cl:

---
## [LanceSmites328/LC13Master](https://github.com/LanceSmites328/LC13Master)@[e23ea7b596...](https://github.com/LanceSmites328/LC13Master/commit/e23ea7b5965a446e5b34f30baa0d4e4dc2d5b868)
#### Tuesday 2023-11-21 20:34:03 by Táculo

Updates La Luna, Pinnochio for Rcorp and playables, gives minions NV on Rcorp AND moves CheckCombat to simple_animal. (#1621)

* Adds Everything

adds nv combat checks to
nosferatu bats
ml slimes
censored minis
tbird spawns
la luna spawned mob

adds mind transfer to pinocchio and la luna
add check for combat to initialize ai controllers for pinocchio, gives him a seclite on rcorp
add check for combat to spawn the breached la luna mob on its position instead of in a random department and to disable the timer.

makes pino ai disabled while a client is possesing it.

* removes one line

* Changes CheckCombat location, applies it to all minions.

* Makes button refuse pino.

fuck you pinocchio

* moves blocking code to pinocchio's

* moves the nightvision checks to simple_animal

moves the nightvision checks to simple_animal

removes the checks from censored, luna, tbird, ml, nosferatu

---
## [mosra/magnum-extras](https://github.com/mosra/magnum-extras)@[52c5ac721e...](https://github.com/mosra/magnum-extras/commit/52c5ac721ec3488cbb76aa6a874c74fc629a772f)
#### Tuesday 2023-11-21 20:51:18 by Vladimír Vondruš

Whee: rework BaseLayer and TextLayer style assignment.

Requiring the calling code to have a compile-time-sized struct felt like
a good idea in theory. In practice it's absolutely horrendous tho, as:

 - The calling code then has to ensure matching order between a style
   enum and a style struct, which is extremely hard to maintain without
   a nasty preprocessor magic.
 - Defining a builtin style means either having to define & document a
   struct that glues a LayerStyleCommon instance together with several
   LayerStyleItem instances, which is nasty on its own, and then have to
   *somehow* populate it. Which in a (C++11) constexpr context means
   either using the implicit initializer, again losing any mapping from
   the actual enum values to the order (thus gaining *nothing* from such
   a "named tuple" definition), or having to give up on any constexpr
   use and assign to the named fields in order to ensure at least some
   ordering sanity.
 - It's extremely annoying and / or impossible to extend the style
   definition for custom widgets -- one has to *derive a struct* for
   that, and then somehow copy the original builtin data to its prefix.
 - The error message when the layer style count differs from the actual
   passed data is total garbage. Nobody is interested in how many bytes
   something occupies, they want to know *what is wrong* and the API
   isn't capable of saying or even knowing that.

So now it's instead a setStyle() API taking the LayerStyleCommon
instance and a (contiguous) list of LayerStyleItem. A downside is that
the (GL) implementation then does two GL buffer uploads, alternatively
it could put them together and upload at once (which means a nasty temp
allocation). With Vulkan (and I hope WebGPU) this won't be a problem as
there's a way to submit multiple uploads in a single command, or just
memory-mapping the buffer and doing a copy directly.

Extending a style is then a matter of creating an array that's larger
than the compile-time constant, having the custom style items start from
that constant, and copying the original data to prefix of that array.
Simple.

For the TextLayer this also merges the previous setStyle() and
setStyleFonts() APIs together, because they were always meant to be
called together anyway. It makes the whole usage a lot less janky and
unclear.

---
## [philipmit/llm-program-synth](https://github.com/philipmit/llm-program-synth)@[a4089dd249...](https://github.com/philipmit/llm-program-synth/commit/a4089dd249454a046ec6c04daa139728e9c60da1)
#### Tuesday 2023-11-21 22:10:04 by Philip Herman Schroeder

Initial output: Response for </Train>

Prompt:

******** Prompt 1:
You are an AI model. You are tasked with training an LSTM to predict ICU mortality using raw data from a patient's first 48 hours in the ICU by filling in the areas of the code between '### Start your code' and '### End your code'.
After training the LSTM, you should define a function called predict_label that takes one input, the raw unprocessed dataset for a single patient, and returns one output, the predicted probability of ICU mortality for that patient.

You are an AI model. You are tasked with training an LSTM to predict ICU mortality using raw data from a patient's first 48 hours in the ICU.
For each patient with patient_subject_id, the raw training data is here: /data/sls/scratch/pschro/p2/data/benchmark_output_demo2/in-hospital-mortality/train/${patient_subject_id}_episode1_timeseries.csv
For each patient, the dataset includes the following columns: ['Hours', 'Capillary refill rate', 'Diastolic blood pressure', 'Fraction inspired oxygen',  'Glascow coma scale total',  'Glucose', 'Heart Rate', 'Height', 'Mean blood pressure', 'Oxygen saturation', 'Respiratory rate', 'Systolic blood pressure', 'Temperature', 'Weight', 'pH']
'Hours' indicates the time the data was collected, represented as the number of hours since the patient was admitted to the ICU. 'Hours' should not be included as a feature in the prediction model.
Many of the variables in the dataset columns are sparse and have missing values. Some variables may include all missing values. Some variables may include non-numeric values.
The labels indicating whether a patient in the training data died or did not die during the ICU stay are here: /data/sls/scratch/pschro/p2/data/benchmark_output_demo2/in-hospital-mortality/train/listfile.csv
This file includes two columns: ['stay', 'y_true']
'stay' has values represented as ${patient_subject_id}_episode1_timeseries.csv and 'y_true' is a 0 or 1 label indicating whether the patient did not die (y_true = 0) or did die (y_true = 1) during the ICU stay.
Please use PyTorch to train an LSTM model to predict 'y_true' given the time-series data in the training data. It is important that you do not modify the ICUData class. The ICUData class cannot be modified.
After training the LSTM, you should define a function called predict_label that takes one input, the raw unprocessed dataset for a single patient, and returns one output, the predicted probability of ICU mortality for that patient.

You can start with the following code:

#<PrevData>
######## Load and preview the dataset and datatypes
# Import necessary libraries
import os
import pandas as pd
import numpy as np
import torch
import warnings
warnings.filterwarnings("ignore")
from torch.utils.data import Dataset

# File paths
TRAIN_DATA_PATH = "/data/sls/scratch/pschro/p2/data/benchmark_output2/in-hospital-mortality/train/"
LABEL_FILE = "/data/sls/scratch/pschro/p2/data/benchmark_output2/in-hospital-mortality/train/listfile.csv"

# Define the Dataset
class ICUData(Dataset):
    def __init__(self, data_path, label_file):
        self.data_path = data_path
        label_data = pd.read_csv(label_file)
        self.file_names = label_data['stay']
        self.labels = torch.tensor(label_data['y_true'].values, dtype=torch.float32)
    def __len__(self):
        return len(self.file_names)
    def __getitem__(self, idx):
        file_path = os.path.join(self.data_path, self.file_names[idx])
        data = pd.read_csv(file_path)
        data = data.drop(['Hours'], axis=1)
        data = data.fillna(0)
        data = data.select_dtypes(include=[np.number])
        label = self.labels[idx]
        return torch.tensor(data.values, dtype=torch.float32), torch.tensor(label, dtype=torch.float32)
#</PrevData>

#<Train>
######## Train the model using the training data, X_train and y_train
### Start your code

### End your code
#</Train>

#<Predict>
######## Define the predict_labels function that can be used to make new predictions using the trained model above given one sample from X_test
### Start your code

### End your code
#</Predict>

Response from GPT:
<Train>
# Import necessary libraries
from torch.nn import LSTM
from torch.optim import Adam
from torch.nn import BCEWithLogitsLoss
import torch.nn as nn
from torch.utils.data import DataLoader

# Parameters for LSTM and DataLoader
input_size = 14  # since we have 14 signals
hidden_size = 64  # size of hidden state
num_layers = 1  # number of stacked LSTM layers
num_epochs = 100  # number of epochs
batch_size = 128  # the size of input data took for one iteration
learning_rate = 0.01  # learning rate of optimisation

# Create LSTM model
class LSTMModel(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers):
        super(LSTMModel, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.lstm = LSTM(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, 1)

    def forward(self, x):
        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(x.device)
        c0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(x.device)

        out, _ = self.lstm(x, (h0, c0))
        out = self.fc(out[:, -1, :])
        return out

# Define model
model = LSTMModel(input_size, hidden_size, num_layers)

# Loss and Optimizer
criterion = BCEWithLogitsLoss()
optimizer = Adam(model.parameters(), lr=learning_rate)

# Data loading
icu_data = ICUData(TRAIN_DATA_PATH, LABEL_FILE)
train_loader = DataLoader(dataset=icu_data, batch_size=batch_size, shuffle=True)

# Training
for epoch in range(num_epochs):
    for i, (sequences, labels) in enumerate(train_loader):
        # Forward pass
        outputs = model(sequences)
        loss = criterion(outputs.view(-1), labels)

        # Backward and optimize
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    if (epoch+1) % 10 == 0:
        print ('Epoch [{}/{}], Loss: {:.4f}'.format(epoch+1, num_epochs, loss.item()))

print("Training finished")
</Train>

---
## [philipmit/llm-program-synth](https://github.com/philipmit/llm-program-synth)@[9f9d2aded0...](https://github.com/philipmit/llm-program-synth/commit/9f9d2aded03d0ef467070c2a22c127a0a5ad0d79)
#### Tuesday 2023-11-21 22:12:29 by Philip Herman Schroeder

Output 3 (phase 1): Response to SyntaxError

Error from previous code:
  File "<stdin>", line 17, in <module>
<class 'SyntaxError'>
invalid syntax (<string>, line 1)

Prompt:

******** Prompt 1:
You are an AI model. You are tasked with training an LSTM to predict ICU mortality using raw data from a patient's first 48 hours in the ICU by filling in the areas of the code between '### Start your code' and '### End your code'.
After training the LSTM, you should define a function called predict_label that takes one input, the raw unprocessed dataset for a single patient, and returns one output, the predicted probability of ICU mortality for that patient.

You are an AI model. You are tasked with training an LSTM to predict ICU mortality using raw data from a patient's first 48 hours in the ICU.
For each patient with patient_subject_id, the raw training data is here: /data/sls/scratch/pschro/p2/data/benchmark_output_demo2/in-hospital-mortality/train/${patient_subject_id}_episode1_timeseries.csv
For each patient, the dataset includes the following columns: ['Hours', 'Capillary refill rate', 'Diastolic blood pressure', 'Fraction inspired oxygen',  'Glascow coma scale total',  'Glucose', 'Heart Rate', 'Height', 'Mean blood pressure', 'Oxygen saturation', 'Respiratory rate', 'Systolic blood pressure', 'Temperature', 'Weight', 'pH']
'Hours' indicates the time the data was collected, represented as the number of hours since the patient was admitted to the ICU. 'Hours' should not be included as a feature in the prediction model.
Many of the variables in the dataset columns are sparse and have missing values. Some variables may include all missing values. Some variables may include non-numeric values.
The labels indicating whether a patient in the training data died or did not die during the ICU stay are here: /data/sls/scratch/pschro/p2/data/benchmark_output_demo2/in-hospital-mortality/train/listfile.csv
This file includes two columns: ['stay', 'y_true']
'stay' has values represented as ${patient_subject_id}_episode1_timeseries.csv and 'y_true' is a 0 or 1 label indicating whether the patient did not die (y_true = 0) or did die (y_true = 1) during the ICU stay.
Please use PyTorch to train an LSTM model to predict 'y_true' given the time-series data in the training data. It is important that you do not modify the ICUData class. The ICUData class cannot be modified.
After training the LSTM, you should define a function called predict_label that takes one input, the raw unprocessed dataset for a single patient, and returns one output, the predicted probability of ICU mortality for that patient.

You can start with the following code:

#<PrevData>
######## Load and preview the dataset and datatypes
# Import necessary libraries
import os
import pandas as pd
import numpy as np
import torch
import warnings
warnings.filterwarnings("ignore")
from torch.utils.data import Dataset

# File paths
TRAIN_DATA_PATH = "/data/sls/scratch/pschro/p2/data/benchmark_output2/in-hospital-mortality/train/"
LABEL_FILE = "/data/sls/scratch/pschro/p2/data/benchmark_output2/in-hospital-mortality/train/listfile.csv"

# Define the Dataset
class ICUData(Dataset):
    def __init__(self, data_path, label_file):
        self.data_path = data_path
        label_data = pd.read_csv(label_file)
        self.file_names = label_data['stay']
        self.labels = torch.tensor(label_data['y_true'].values, dtype=torch.float32)
    def __len__(self):
        return len(self.file_names)
    def __getitem__(self, idx):
        file_path = os.path.join(self.data_path, self.file_names[idx])
        data = pd.read_csv(file_path)
        data = data.drop(['Hours'], axis=1)
        data = data.fillna(0)
        data = data.select_dtypes(include=[np.number])
        label = self.labels[idx]
        return torch.tensor(data.values, dtype=torch.float32), torch.tensor(label, dtype=torch.float32)
#</PrevData>

#<Train>
######## Train the model using the training data, X_train and y_train
### Start your code

### End your code
#</Train>

#<Predict>
######## Define the predict_labels function that can be used to make new predictions using the trained model above given one sample from X_test
### Start your code

### End your code
#</Predict>
<Train>
# Import necessary libraries
from torch.nn import LSTM
from torch.optim import Adam
from torch.nn import BCEWithLogitsLoss
import torch.nn as nn
from torch.utils.data import DataLoader

# Parameters for LSTM and DataLoader
input_size = 14  # since we have 14 signals
hidden_size = 64  # size of hidden state
num_layers = 1  # number of stacked LSTM layers
num_epochs = 100  # number of epochs
batch_size = 128  # the size of input data took for one iteration
learning_rate = 0.01  # learning rate of optimisation

# Create LSTM model
class LSTMModel(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers):
        super(LSTMModel, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.lstm = LSTM(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, 1)

    def forward(self, x):
        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(x.device)
        c0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(x.device)

        out, _ = self.lstm(x, (h0, c0))
        out = self.fc(out[:, -1, :])
        return out

# Define model
model = LSTMModel(input_size, hidden_size, num_layers)

# Loss and Optimizer
criterion = BCEWithLogitsLoss()
optimizer = Adam(model.parameters(), lr=learning_rate)

# Data loading
icu_data = ICUData(TRAIN_DATA_PATH, LABEL_FILE)
train_loader = DataLoader(dataset=icu_data, batch_size=batch_size, shuffle=True)

# Training
for epoch in range(num_epochs):
    for i, (sequences, labels) in enumerate(train_loader):
        sequences = sequences.squeeze(1)  # Remove unnecessary dimension from time-series data
        # Forward pass
        outputs = model(sequences)
        loss = criterion(outputs.view(-1), labels)

        # Backward and optimize
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    if (epoch+1) % 10 == 0:
        print ('Epoch [{}/{}], Loss: {:.4f}'.format(epoch+1, num_epochs, loss.item()))

print("Training finished")
</Train>

******** Prompt for correcting error in Response 1:
The code from Response 1 from GPT above produces the below error message. Please fully recreate the code such that this error does not occur.
Error message:
  File "<stdin>", line 17, in <module>
<class 'SyntaxError'>
invalid syntax (<string>, line 1)

******** Response 1 corrected:

Response from GPT:
# Import necessary libraries
from torch.nn import LSTM
from torch.optim import Adam
from torch.nn import BCEWithLogitsLoss
import torch.nn as nn
from torch.utils.data import DataLoader

# Parameters for LSTM and DataLoader
input_size = 14  # since we have 14 signals
hidden_size = 64  # size of hidden state
num_layers = 1  # number of stacked LSTM layers
num_epochs = 100  # number of epochs
batch_size = 128  # the size of input data took for one iteration
learning_rate = 0.01  # learning rate of optimisation

# Create LSTM model
class LSTMModel(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers):
        super(LSTMModel, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.lstm = LSTM(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, 1)

    def forward(self, x):
        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(x.device)
        c0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(x.device)

        out, _ = self.lstm(x, (h0, c0))
        out = self.fc(out[:, -1, :])
        return out

# Define model
model = LSTMModel(input_size, hidden_size, num_layers)

# Loss and Optimizer
criterion = BCEWithLogitsLoss()
optimizer = Adam(model.parameters(), lr=learning_rate)

# Data loading
icu_data = ICUData(TRAIN_DATA_PATH, LABEL_FILE)
train_loader = DataLoader(dataset=icu_data, batch_size=batch_size, shuffle=True)

# Training
for epoch in range(num_epochs):
    for i, (sequences, labels) in enumerate(train_loader):
        sequences = sequences.squeeze(1)  # Remove unnecessary dimension from time-series data
        # Forward pass
        outputs = model(sequences)
        loss = criterion(outputs.view(-1), labels)

        # Backward and optimize
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    if (epoch+1) % 10 == 0:
        print ('Epoch [{}/{}], Loss: {:.4f}'.format(epoch+1, num_epochs, loss.item()))

print("Training finished")</Train>

---
## [philipmit/llm-program-synth](https://github.com/philipmit/llm-program-synth)@[6c81fb74c0...](https://github.com/philipmit/llm-program-synth/commit/6c81fb74c03dbbe163ab42221a6e7666b2f5aa02)
#### Tuesday 2023-11-21 22:13:11 by Philip Herman Schroeder

Output 4 (phase 1): Response to SyntaxError

Error from previous code:
  File "<stdin>", line 17, in <module>
<class 'SyntaxError'>
invalid syntax (<string>, line 49)

Prompt:

******** Prompt 1:
You are an AI model. You are tasked with training an LSTM to predict ICU mortality using raw data from a patient's first 48 hours in the ICU by filling in the areas of the code between '### Start your code' and '### End your code'.
After training the LSTM, you should define a function called predict_label that takes one input, the raw unprocessed dataset for a single patient, and returns one output, the predicted probability of ICU mortality for that patient.

You are an AI model. You are tasked with training an LSTM to predict ICU mortality using raw data from a patient's first 48 hours in the ICU.
For each patient with patient_subject_id, the raw training data is here: /data/sls/scratch/pschro/p2/data/benchmark_output_demo2/in-hospital-mortality/train/${patient_subject_id}_episode1_timeseries.csv
For each patient, the dataset includes the following columns: ['Hours', 'Capillary refill rate', 'Diastolic blood pressure', 'Fraction inspired oxygen',  'Glascow coma scale total',  'Glucose', 'Heart Rate', 'Height', 'Mean blood pressure', 'Oxygen saturation', 'Respiratory rate', 'Systolic blood pressure', 'Temperature', 'Weight', 'pH']
'Hours' indicates the time the data was collected, represented as the number of hours since the patient was admitted to the ICU. 'Hours' should not be included as a feature in the prediction model.
Many of the variables in the dataset columns are sparse and have missing values. Some variables may include all missing values. Some variables may include non-numeric values.
The labels indicating whether a patient in the training data died or did not die during the ICU stay are here: /data/sls/scratch/pschro/p2/data/benchmark_output_demo2/in-hospital-mortality/train/listfile.csv
This file includes two columns: ['stay', 'y_true']
'stay' has values represented as ${patient_subject_id}_episode1_timeseries.csv and 'y_true' is a 0 or 1 label indicating whether the patient did not die (y_true = 0) or did die (y_true = 1) during the ICU stay.
Please use PyTorch to train an LSTM model to predict 'y_true' given the time-series data in the training data. It is important that you do not modify the ICUData class. The ICUData class cannot be modified.
After training the LSTM, you should define a function called predict_label that takes one input, the raw unprocessed dataset for a single patient, and returns one output, the predicted probability of ICU mortality for that patient.

You can start with the following code:

#<PrevData>
######## Load and preview the dataset and datatypes
# Import necessary libraries
import os
import pandas as pd
import numpy as np
import torch
import warnings
warnings.filterwarnings("ignore")
from torch.utils.data import Dataset

# File paths
TRAIN_DATA_PATH = "/data/sls/scratch/pschro/p2/data/benchmark_output2/in-hospital-mortality/train/"
LABEL_FILE = "/data/sls/scratch/pschro/p2/data/benchmark_output2/in-hospital-mortality/train/listfile.csv"

# Define the Dataset
class ICUData(Dataset):
    def __init__(self, data_path, label_file):
        self.data_path = data_path
        label_data = pd.read_csv(label_file)
        self.file_names = label_data['stay']
        self.labels = torch.tensor(label_data['y_true'].values, dtype=torch.float32)
    def __len__(self):
        return len(self.file_names)
    def __getitem__(self, idx):
        file_path = os.path.join(self.data_path, self.file_names[idx])
        data = pd.read_csv(file_path)
        data = data.drop(['Hours'], axis=1)
        data = data.fillna(0)
        data = data.select_dtypes(include=[np.number])
        label = self.labels[idx]
        return torch.tensor(data.values, dtype=torch.float32), torch.tensor(label, dtype=torch.float32)
#</PrevData>

#<Train>
######## Train the model using the training data, X_train and y_train
### Start your code

### End your code
#</Train>

#<Predict>
######## Define the predict_labels function that can be used to make new predictions using the trained model above given one sample from X_test
### Start your code

### End your code
#</Predict>
# Import necessary libraries
from torch.nn import LSTM
from torch.optim import Adam
from torch.nn import BCEWithLogitsLoss
import torch.nn as nn
from torch.utils.data import DataLoader

# Parameters for LSTM and DataLoader
input_size = 14  # since we have 14 signals
hidden_size = 64  # size of hidden state
num_layers = 1  # number of stacked LSTM layers
num_epochs = 100  # number of epochs
batch_size = 128  # the size of input data took for one iteration
learning_rate = 0.01  # learning rate of optimisation

# Create LSTM model
class LSTMModel(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers):
        super(LSTMModel, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.lstm = LSTM(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, 1)

    def forward(self, x):
        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(x.device)
        c0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(x.device)

        out, _ = self.lstm(x, (h0, c0))
        out = self.fc(out[:, -1, :])
        return out

# Define model
model = LSTMModel(input_size, hidden_size, num_layers)

# Loss and Optimizer
criterion = BCEWithLogitsLoss()
optimizer = Adam(model.parameters(), lr=learning_rate)

# Data loading
icu_data = ICUData(TRAIN_DATA_PATH, LABEL_FILE)
train_loader = DataLoader(dataset=icu_data, batch_size=batch_size, shuffle=True)

# Training
for epoch in range(num_epochs):
    for i, (sequences, labels) in enumerate(train_loader):
        sequences = sequences.squeeze(1)  # Remove unnecessary dimension from time-series data
        # Forward pass
        outputs = model(sequences)
        loss = criterion(outputs.view(-1), labels)

        # Backward and optimize
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    if (epoch+1) % 10 == 0:
        print ('Epoch [{}/{}], Loss: {:.4f}'.format(epoch+1, num_epochs, loss.item()))

print("Training finished")</Train>

******** Prompt for correcting error in Response 1:
The code from Response 1 from GPT above produces the below error message. Please fully recreate the code such that this error does not occur.
Error message:
  File "<stdin>", line 17, in <module>
<class 'SyntaxError'>
invalid syntax (<string>, line 49)

******** Response 1 corrected:

Response from GPT:
# Import necessary libraries
from torch.nn import LSTM
from torch.optim import Adam
from torch.nn import BCEWithLogitsLoss
import torch.nn as nn
from torch.utils.data import DataLoader

# Parameters for LSTM and DataLoader
input_size = 14  # since we have 14 signals
hidden_size = 64  # size of hidden state
num_layers = 1  # number of stacked LSTM layers
num_epochs = 100  # number of epochs
batch_size = 128  # the size of input data took for one iteration
learning_rate = 0.01  # learning rate of optimisation

# Create LSTM model
class LSTMModel(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers):
        super(LSTMModel, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.lstm = LSTM(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, 1)

    def forward(self, x):
        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(x.device)
        c0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(x.device)

        out, _ = self.lstm(x, (h0, c0))
        out = self.fc(out[:, -1, :])
        return out

# Define model
model = LSTMModel(input_size, hidden_size, num_layers)

# Loss and Optimizer
criterion = BCEWithLogitsLoss()
optimizer = Adam(model.parameters(), lr=learning_rate)

# Data loading
icu_data = ICUData(TRAIN_DATA_PATH, LABEL_FILE)
train_loader = DataLoader(dataset=icu_data, batch_size=batch_size, shuffle=True)

# Training
for epoch in range(num_epochs):
    for i, (sequences, labels) in enumerate(train_loader):
        sequences = sequences.squeeze(1)  # Remove unnecessary dimension from time-series data
        # Forward pass
        outputs = model(sequences)
        loss = criterion(outputs.view(-1), labels)

        # Backward and optimize
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    if (epoch+1) % 10 == 0:
        print ('Epoch [{}/{}], Loss: {:.4f}'.format(epoch+1, num_epochs, loss.item()))

print("Training finished")

# Define the prediction function
def predict_label(patient_data):
    patient_data = torch.tensor(patient_data.values, dtype=torch.float32).unsqueeze(0)
    output = torch.sigmoid(model(patient_data)).item()
    return output
# Here we assume that `patient_data` is a pandas dataframe for a single patient (excluding the 'Hours' column).</Train>

---
## [temporalio/temporal](https://github.com/temporalio/temporal)@[1be76e3583...](https://github.com/temporalio/temporal/commit/1be76e3583ef01ba9f79503e81fed5b7c9ab389c)
#### Tuesday 2023-11-21 23:19:40 by Tim Deeb-Swihart

Replace gogo/protobuf with google/protobuf (#5032)

**What changed?**

gogo/protobuf has been replaced with Google's official go compiler. 

**Why?**

gogo/protobuf has been deprecated for some time and the community is
moving on, building new tools (like vtproto) atop google's v2 compiler.

**How did you test it?**

`make test`

**Potential risks**

1. The change from embedded gogo-generated-structs to
google-generated-pointers-to-structs created a risk of nil pointer
exceptions. I've fixed all the ones our tests found but it's possible
there are more lurking in the new code.
2. This change may cause our performance to decrease. Certainly
encoding/deconding of proto objects will become slower, but the overuse
of pointers by the google compiler may negatively affect our overall
performance. We'll need to keep an eye on the GC stats
3. This breaks the HTTP API. We will not support [shortand payload
encoding](https://github.com/temporalio/proposals/blob/master/api/http-api.md#payload-formatting)
in this first pass; that will come once this initial work is in testing.

**Breaking changes for developers**

- `*time.Time` in proto structs will now be
[timestamppb.Timestamp](https://pkg.go.dev/google.golang.org/protobuf@v1.31.0/types/known/timestamppb#section-documentation)
- `*time.Duration` will now be
[durationpb.Duration](https://pkg.go.dev/google.golang.org/protobuf/types/known/durationpb)
- V2-generated structs embed locks, so you cannot dereference them. `go
vet` will scream at you about this. If you need a copy, use
`proto.Clone`.
- If the performance of this sucks then I will either update our code
generator to add shallow-clone methods or hand-roll the ones we need
- Proto enums will, when formatted to JSON, now be in
`SCREAMING_SNAKE_CASE` rather than `PascalCase`. We decided (in
discussion with the SDK team) that now was as good a time as any to rip
the bandage off.
- Proto objects, or objects embedding protos, cannot be compared using
`reflect.DeepEqual` or _anything_ that uses it. This includes `testify`
and `mock` equality testers!
- You will need to use the `common/testing/protorequire`,
`common/testing/protoassert`, or `common/testing/protomock` packages
instead. I've implemented proto-compatible matchers and assertions there
for all cases I've encountered
- If you need `reflect.DeepEqual` for any reason you can use
`go.temporal.io/api/temporalproto.DeepEqual` instead

Note that history loading will not be impacted by the JSON changes: I
rewrote history loading to dynamically fix incoming history JSON data
(like all our other sdks); you can find this code in [my fork of our go
API](https://github.com/tdeebswihart/temporal-api-go/blob/master/internal/temporalhistoryv1/load.go)
alongside its tests.

**🚨Sharp Edges Introduced🚨**

Beware `*timestamppb.Timestamp.AsTime()`. If you need to extract a time
value from a proto time (timestamppb) **always** make sure to check
whether it's nil first. When the proto object is `nil` `AsTime()` will
return a non-zero time at the proto epoch: UTC midnight on January 1,
1970.

I've made this mistake multiple times during this transition and each
time it's been a pain to debug

**Is hotfix candidate?**

No.

---
## [Wannieboy07/minishell](https://github.com/Wannieboy07/minishell)@[1ef864b68e...](https://github.com/Wannieboy07/minishell/commit/1ef864b68e159de4cd6d9fe9c7a4f54661587c05)
#### Tuesday 2023-11-21 23:35:52 by LarsCampus19

reworked variables entirely bcs it fucking sucked ass, now way easier and better to work with, reworking export and unset, export nearly already finished again(auto_push)

---

