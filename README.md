## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-03-18](docs/good-messages/2022/2022-03-18.md)


1,815,756 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,815,756 were push events containing 2,901,708 commit messages that amount to 191,124,097 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 29 messages:


## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[420d78db1a...](https://github.com/treckstar/yolo-octo-hipster/commit/420d78db1aca51674abee34610da7e1a09cd344d)
#### Friday 2022-03-18 00:00:04 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [KDr2/postgres](https://github.com/KDr2/postgres)@[ec62cb0aac...](https://github.com/KDr2/postgres/commit/ec62cb0aac5ba31a82339606009ddbd7eb00e2ac)
#### Friday 2022-03-18 00:01:54 by Tom Lane

Revert applying column aliases to the output of whole-row Vars.

In commit bf7ca1587, I had the bright idea that we could make the
result of a whole-row Var (that is, foo.*) track any column aliases
that had been applied to the FROM entry the Var refers to.  However,
that's not terribly logically consistent, because now the output of
the Var is no longer of the named composite type that the Var claims
to emit.  bf7ca1587 tried to handle that by changing the output
tuple values to be labeled with a blessed RECORD type, but that's
really pretty disastrous: we can wind up storing such tuples onto
disk, whereupon they're not readable by other sessions.

The only practical fix I can see is to give up on what bf7ca1587
tried to do, and say that the column names of tuples produced by
a whole-row Var are always those of the underlying named composite
type, query aliases or no.  While this introduces some inconsistencies,
it removes others, so it's not that awful in the abstract.  What *is*
kind of awful is to make such a behavioral change in a back-patched
bug fix.  But corrupt data is worse, so back-patched it will be.

(A workaround available to anyone who's unhappy about this is to
introduce an extra level of sub-SELECT, so that the whole-row Var is
referring to the sub-SELECT's output and not to a named table type.
Then the Var is of type RECORD to begin with and there's no issue.)

Per report from Miles Delahunty.  The faulty commit dates to 9.5,
so back-patch to all supported branches.

Discussion: https://postgr.es/m/2950001.1638729947@sss.pgh.pa.us

---
## [crowlogic/arb4j](https://github.com/crowlogic/arb4j)@[6f4a14291b...](https://github.com/crowlogic/arb4j/commit/6f4a14291bf54cdb3c8cb17491876937dc3900ae)
#### Friday 2022-03-18 00:23:55 by Stephen Crowley

fucking god damn github key bullshit you god damn microsoft sons of
bitches

---
## [GForceTF/tgstation](https://github.com/GForceTF/tgstation)@[0e904f7032...](https://github.com/GForceTF/tgstation/commit/0e904f70328a460af310014891eaadb5968ec31a)
#### Friday 2022-03-18 00:39:47 by LemonInTheDark

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
## [pariahstation/Pariah-Station](https://github.com/pariahstation/Pariah-Station)@[c78ba85658...](https://github.com/pariahstation/Pariah-Station/commit/c78ba856586b20f8f08064188878c1766f473d9f)
#### Friday 2022-03-18 01:19:49 by John Willard

makes podpeople call parent (#65362)


About The Pull Request

kinda fucked up that it doesnt.
Also while checking this PR I noticed other species also don't, kinda screwed up world we live in...
Why It's Good For The Game

Parent's spec_life is what checks if you have nobreath, and in which case it will remove all your oxygen damage and, if in crit, give you brute damage instead. Not having this makes you basically not take damage while in crit, which I think shouldn't be the case.
Changelog

cl
fix: Podpeople now take self-respiration into account when taking damage from critical condition, like most other species.
/cl

---
## [Dmdv/free-programming-books](https://github.com/Dmdv/free-programming-books)@[97016edd67...](https://github.com/Dmdv/free-programming-books/commit/97016edd6791285128758dd91904b343d1f3b0fd)
#### Friday 2022-03-18 01:37:28 by David Ordás

Add CodingFantasy's CSS coding interactive games (#5490)

* Add "Knights of the Flexbox table" game

Welcome to the Knights of the Flexbox table. A game where you can help Sir Frederic Flexbox and his friends to uncover the treasures hidden in the Tailwind CSS dungeons.
You can navigate the knight through the dungeon by changing his position within the dungeon using Flexbox and Tailwind CSS.

* Add "Flex Box Adventure" game

Once upon a time, there was a King Arthur. He ruled his kingdom fair and square. But Arthur had one problem. He was a very naive person. So one sunny day, three alchemist brothers offered Arthur to exchange all his Gold Coins for coins made of a more valuable new metal that they had invented - Bit Coins.

Arthur believed them and gave them all his gold. The brothers took the gold and promised to give the bit coins back to Arthur in seven days.

Seven days passed. The brothers have not turned up. Arthur realized he had been scammed. He is angry and intends to take revenge on them. Let's help him do it with our weapon – CSS Flex Box!

We made this game for You
1. You often stumble and try to figure out which combination of Flex Box properties makes the browser do what you want it to do.

2. You want to create complex web layouts without constantly looking at the web page after every Cmd/Ctrl+S press in the code editor.

3. You have tried to learn Flex Box with video tutorials and articles but still don't fully understand how some parts of it work.

4*. Or, if you are a master of CSS Flex Box, we have something interesting and for you too (read further).

Have you found yourself there? Then you definitely want to learn or improve your Flex Box skills. So we have good news for you, really good news...

Learn Flex Box by Playing Game
No more boring videos, tutorials and courses. Learn Flex Box in a completely new, fun, effective and revolutionary way. By playing Flex Box coding game!

* Add "Grid Attack" coding game

In an ancient Elvish prophecy, it was said that one day a man would be born with an incredible power that predicts the future – "Marketi Predictori." And another will come to take this power. But the years went by and nothing happened. Until one day, a little elf was born. He was named Luke.

From an early age, he surprised his parents and his sister Rey by guessing the price of apples at the farmer's market before they even reached it. Every year his power rose and his predictions became more and more accurate. But there was one thing Luke could not predict. The coming of the demon Valcorian. It was the one from the prophecy that was to come and take Luke's power. One day Valcorian and his army attacked the town where Luke had lived and kidnapped him to make a ritual of stealing his power.

Go on a dangerous quest with Luke's sister Rey and find her brother. Defeat Valcorian and all his demons using a secret weapon – CSS Grid.

We made this game for You?
1. You often stumble and try to figure out which combination of Grid properties makes the browser do what you want it to do.

2. You are scared by the number of properties a CSS Grid has, and you feel uncomfortable when you need to create a grid layout.

3. You want to create complex web layouts using Grid, but without constantly looking at the web page after every "Cmd/Ctrl+S" press in the code editor.

4. You have tried to learn CSS Grid with video tutorials and articles but still don't fully understand how some parts of it work.

5. You use a Flex Box where Grid is required because you don't feel confident in using it.

Have you found yourself there? Then you definitely want to learn or improve your Grid skills. So we have good news for you, really good news...

Learn Grid by Playing CSS Game
No more boring videos, courses and articles. Learn Grid in a revolutionary new, fun, and effective way. By playing a Grid coding game!

---
## [Fargowilta/FargowiltasSouls](https://github.com/Fargowilta/FargowiltasSouls)@[541675d5c9...](https://github.com/Fargowilta/FargowiltasSouls/commit/541675d5c9b036827c6d50b80ba0a3517b41c716)
#### Friday 2022-03-18 01:38:07 by terrynmuse

port
 pixie
 moth
 salamander
 salamanders, crawdads, giant shellies turning into each other
 mothron
 mothron spawn
 mothron egg
 butcher
 swamp thing
 possessed
 chaos elemental
 shark
 sand shark and friends
 piranha
 arapaima
 dark mage
 eternia crystal
 ooa goblin
 goblin bomber
 ogre
 dark mage skeleton
 wither beast
 etherian wyvern
 lightning bug
 blood feeder
 vile spit
 pirates stealing things
 flying dutchman
 pirate crossbower
 pirate deadeye
 pirate captain

nerfed mothron egg, no longer insta hatches but has x3 life
presence of betsy turns remaining ooa enemies into wyverns instead of despawning them
adjusted shooter ai a bit, now pauses before attacking
blood feeder can feed on other npcs too

---
## [Mu-L/hhvm](https://github.com/Mu-L/hhvm)@[85b55e9c85...](https://github.com/Mu-L/hhvm/commit/85b55e9c85c84c6cfb7c3937668912ce7197cd1e)
#### Friday 2022-03-18 01:56:25 by Hunter Goldstein

Module Declaration: Thread through most internal Hack systems

Summary:
# High Level
This stack threads module declarations through `hh_server` such that they are now understood and are accessible across files. The main effect is that declaring a file to be a part of a module requires that said module has an existing declaration in the current codebase. For example:
```
//// a-decl.php
<?hh
<<file:__EnableUnstableFeatures('modules')>
module A {}

//// a.php
<?hh

// Unbound name error w/o `a-decl.php`
<<file:__EnableUnstableFeatures('modules'), __Module('A')>>
```
# This Diff

This adds *the vast majority* of the plumbing required to reach our end state of modules stored as decls, s.t. their information can be accessed across files.

## `ClientIdeIncremental`

Based on the name of the module, my assumption is that this is meant for file updates *within* the IDE when the changes haven't been saved.

**This is currently not implemented, but is vital to implement for a good user experience in VScode.** This looks like it's implemented via the facts parser, which AFAIK doesn't handle modules. Any changes related to adding / removing module decls will not be observed until saved.

As per Lucian:
> what is ClientIdeIncremental? - the IDE typechecks the unsaved-files-in-the-editor against files on disk for the rest of WWW. If a file on disk changes, then watchman notifies us about it, and tells VSCode, and VSCode sends us a didChangedWatchedFile, and we invoke ClientIdeIncremental. In this way the IDE will know to typecheck its editor buffers against the new updated rest-of-the-codebase.
Without implementing this, then if the user has a file open which says "error you claim to be part of module A but module A isn't declared", and the user modifies a file on disk so that module A is now declared, then the IDE will be unable to know that fact without restarting.

Lucian has also noted that this entire logic could be implemented via direct decl parsing, so this could become a non-issue (as we already have implemented modules in direct decl parsing).

## Decl Diffing

Modules can be placed on classes, functions, and types. Functions and types appear to need no adjustment here as we diff them via `Poly.( = )`. Classes I've made internal-ness and module membership into "big diff" changes. This *requires* potentially re-checking all uses of the class.

## Decl Heap

Module decls add a new heap kind, `Modules`. This looks *roughly* like the heap for constants, rather than classes, as we're making modules *case sensitive*. I didn't store this as part of an existing heap as modules are really their own *thing:* they're a separate construct that we can't really categorize among the existing Hack *things*. ljw1004 wrote out a good visualization:
```
1. Fun
2. GConst
3. Typelike
   3.1. Typedef
   3.3. Classlike
        3.3.1. Class
        3.3.2. Trait
        3.3.3. Enum
        3.3.4. Interface
4. Modules
```
Modules are obviously unlike constants or functions, and (for now) cannot be referenced in expression positions, making them unlike types.

**Modules are case-sensitive,** unlike functions / classes.

## Dependencies

I've added a new kind of dependency, a `Dep.Module`: this is not yet in use, but this represents data flow from a module to its members. One can imagine the following code:
```
<?hh

<<file: __Module('A')>>

function foobar(): void {}
```
... having an edge in the depgraph:
```
Module A  -> Fun foobar
```

## HackC (`DeclProvider`)

For Decls-In-Compilation, because modules don't exist at runtime, it doesn't make any sense to try to expose modules at the moment. If you ask for a module name, we will tell you that it doesn't exist, unconditionally.

## Naming

As noted previously, modules live *along side* other constructs in Hack, thus we create:
* A new entry in the naming table (`Naming_sqlite`)
* A new kind of naming heap (`Naming_heap.Modules`)

We thread namespace elaboration through any attached attributes as well, as part of naming.

## Providers

Similar to the other heaps, we've threaded through a new kind of *thing,* copy-pasting the logic from constants, with modules where needed. The code in `hphp/hack/src/providers/` is boilerplate-y, wouldn't be surprised if there's one copy-paste error kicking about.

## Server Functionality (`hphp/hack/src/server/`)

`ServerExtractStandalone` ignores module decls for now. Realistically, we should include them as it could be useful for repro-ing module specific bugs.

`ServerLazyInit` bit me: there's a part where we remove references to any potentially changed decls when initializing from saved state that I forgot to fill out for modules.

Differential Revision: D34481050

fbshipit-source-id: 26f6de8cc2e1d9ebdcf13087c62714bea4f2e0d5

---
## [Sea-of-Lost-Souls/Tannhauser-Gate](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate)@[8b1ec33143...](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate/commit/8b1ec331432234f358b26ee1627c10358ccae6a7)
#### Friday 2022-03-18 02:15:59 by LeonY24

P90 (#12125)

* P90 SMG

le new gun for new away mission we're planning to make

* Update p90.dm

* includes p90.dm

my fucking retard ass hadnt shit included bruh

---
## [yoyooyooo/next.js](https://github.com/yoyooyooo/next.js)@[91146b23a2...](https://github.com/yoyooyooo/next.js/commit/91146b23a21e33d54332a469f30afe6e6156cd65)
#### Friday 2022-03-18 02:50:06 by Glenn Gijsberts

Make adjustment to cache config of with-apollo example (#32733)

## Description
This year we implemented the new Apollo config using this example. We recently moved to `getServerSideProps` as well, however, this was giving us some cache problems. The issue was that the cache was older than the actual data that was coming from the server side query. 

Because the `merge` of the cache in `apolloClient.js` is merging the existingCache in the initialState it will overwrite the "fresh" initialState with properties that already exists. This means that if you have something in your cache from previous client render, for example `user` with the value `null`, and you go to a new page and do a new query on the server which returns a value for the `user` field, it will still return `null` because of that `merge` function.

Since this was weird in our opinion, we've changed this in our own environment by always overwriting the existing cache with the new initialState, so that the initialState that is coming from a fresh server side query is overwriting. We thought it was a good idea to reflect this also in this example, because we couldn't think of a reason why the existing cache should overwrite fresh queries.

I've added a reproduction that shows what this is exactly about. I hope my description makes sense, let me know what you think!

## Reproduction of old scenario
Created a reproduction branch here: https://github.com/glenngijsberts/with-apollo-example. Using a different API than in the example, because of https://github.com/vercel/next.js/issues/32731.

1. checkout the example
2. yarn
3. yarn dev
4. visit http://localhost:3000/client-only
5. Hit "Update name". This will run a mutation that will update the cache automatically. Because I use a mocked API, the actual value on the API won't be updated, but this is actually the perfect scenario for the problem because in reality data can already change in the meantime when you're doing a new request.
6. Go to the SSR page
7. This will display two values: one is coming from the server side request (which is the latest data, because no cache is used in `getServerSideProps`) and the other is using the cache, which is outdated at that point, yet it's still returned because the old way of merging the cache was picking the existing cache over the initialState that was coming from the fresh server side query.

## Documentation / Examples

- [x] Make sure the linting passes by running `yarn lint`

---
## [chaldeaprjkt/kernel_xiaomi_vayu](https://github.com/chaldeaprjkt/kernel_xiaomi_vayu)@[a11b9a741a...](https://github.com/chaldeaprjkt/kernel_xiaomi_vayu/commit/a11b9a741a78d1bbba092f1bd6b224f1070ed3a9)
#### Friday 2022-03-18 05:42:50 by Peter Zijlstra

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

---
## [Fabbautis/Fabbautis.github.io](https://github.com/Fabbautis/Fabbautis.github.io)@[fc5b13a42f...](https://github.com/Fabbautis/Fabbautis.github.io/commit/fc5b13a42f7929aba2e198bb51d82dc34777aa72)
#### Friday 2022-03-18 07:02:52 by FabBautis

Started work on kill minigame

My god registration points are a pain the ass

Fix professor tween not wanting to iterate again
Program fancy randomized walking for the dragon
Figure out local to global variables so that I can use hitboxes
Do some flag variable for the hitting animation that just says if player collides with dragon and isn't hitting, then kill them (also add is facing dragon too).
Add a fade out death animation for the dragon (probably tween the alpha)
Add borders for player and dragon (if they go out of border, stop moving in that direction)

---
## [westermo/linux](https://github.com/westermo/linux)@[a50e1fcbc9...](https://github.com/westermo/linux/commit/a50e1fcbc9b85fd4e95b89a75c0884cb032a3e06)
#### Friday 2022-03-18 08:06:53 by Josef Bacik

btrfs: do not WARN_ON() if we have PageError set

Whenever we do any extent buffer operations we call
assert_eb_page_uptodate() to complain loudly if we're operating on an
non-uptodate page.  Our overnight tests caught this warning earlier this
week

  WARNING: CPU: 1 PID: 553508 at fs/btrfs/extent_io.c:6849 assert_eb_page_uptodate+0x3f/0x50
  CPU: 1 PID: 553508 Comm: kworker/u4:13 Tainted: G        W         5.17.0-rc3+ #564
  Hardware name: QEMU Standard PC (Q35 + ICH9, 2009), BIOS 1.13.0-2.fc32 04/01/2014
  Workqueue: btrfs-cache btrfs_work_helper
  RIP: 0010:assert_eb_page_uptodate+0x3f/0x50
  RSP: 0018:ffffa961440a7c68 EFLAGS: 00010246
  RAX: 0017ffffc0002112 RBX: ffffe6e74453f9c0 RCX: 0000000000001000
  RDX: ffffe6e74467c887 RSI: ffffe6e74453f9c0 RDI: ffff8d4c5efc2fc0
  RBP: 0000000000000d56 R08: ffff8d4d4a224000 R09: 0000000000000000
  R10: 00015817fa9d1ef0 R11: 000000000000000c R12: 00000000000007b1
  R13: ffff8d4c5efc2fc0 R14: 0000000001500000 R15: 0000000001cb1000
  FS:  0000000000000000(0000) GS:ffff8d4dbbd00000(0000) knlGS:0000000000000000
  CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
  CR2: 00007ff31d3448d8 CR3: 0000000118be8004 CR4: 0000000000370ee0
  Call Trace:

   extent_buffer_test_bit+0x3f/0x70
   free_space_test_bit+0xa6/0xc0
   load_free_space_tree+0x1f6/0x470
   caching_thread+0x454/0x630
   ? rcu_read_lock_sched_held+0x12/0x60
   ? rcu_read_lock_sched_held+0x12/0x60
   ? rcu_read_lock_sched_held+0x12/0x60
   ? lock_release+0x1f0/0x2d0
   btrfs_work_helper+0xf2/0x3e0
   ? lock_release+0x1f0/0x2d0
   ? finish_task_switch.isra.0+0xf9/0x3a0
   process_one_work+0x26d/0x580
   ? process_one_work+0x580/0x580
   worker_thread+0x55/0x3b0
   ? process_one_work+0x580/0x580
   kthread+0xf0/0x120
   ? kthread_complete_and_exit+0x20/0x20
   ret_from_fork+0x1f/0x30

This was partially fixed by c2e39305299f01 ("btrfs: clear extent buffer
uptodate when we fail to write it"), however all that fix did was keep
us from finding extent buffers after a failed writeout.  It didn't keep
us from continuing to use a buffer that we already had found.

In this case we're searching the commit root to cache the block group,
so we can start committing the transaction and switch the commit root
and then start writing.  After the switch we can look up an extent
buffer that hasn't been written yet and start processing that block
group.  Then we fail to write that block out and clear Uptodate on the
page, and then we start spewing these errors.

Normally we're protected by the tree lock to a certain degree here.  If
we read a block we have that block read locked, and we block the writer
from locking the block before we submit it for the write.  However this
isn't necessarily fool proof because the read could happen before we do
the submit_bio and after we locked and unlocked the extent buffer.

Also in this particular case we have path->skip_locking set, so that
won't save us here.  We'll simply get a block that was valid when we
read it, but became invalid while we were using it.

What we really want is to catch the case where we've "read" a block but
it's not marked Uptodate.  On read we ClearPageError(), so if we're
!Uptodate and !Error we know we didn't do the right thing for reading
the page.

Fix this by checking !Uptodate && !Error, this way we will not complain
if our buffer gets invalidated while we're using it, and we'll maintain
the spirit of the check which is to make sure we have a fully in-cache
block while we're messing with it.

CC: stable@vger.kernel.org # 5.4+
Signed-off-by: Josef Bacik <josef@toxicpanda.com>
Signed-off-by: David Sterba <dsterba@suse.com>

---
## [Kneba/android_kernel_asus_sdm660](https://github.com/Kneba/android_kernel_asus_sdm660)@[81c4a9573e...](https://github.com/Kneba/android_kernel_asus_sdm660/commit/81c4a9573e35a60c9b2be03dae74cdb468fa58cc)
#### Friday 2022-03-18 12:47:54 by Maciej Żenczykowski

FROMGIT: bpf: Do not change gso_size during bpf_skb_change_proto()

This is technically a backwards incompatible change in behaviour, but I'm
going to argue that it is very unlikely to break things, and likely to fix
*far* more then it breaks.

In no particular order, various reasons follow:

(a) I've long had a bug assigned to myself to debug a super rare kernel crash
on Android Pixel phones which can (per stacktrace) be traced back to BPF clat
IPv6 to IPv4 protocol conversion causing some sort of ugly failure much later
on during transmit deep in the GSO engine, AFAICT precisely because of this
change to gso_size, though I've never been able to manually reproduce it. I
believe it may be related to the particular network offload support of attached
USB ethernet dongle being used for tethering off of an IPv6-only cellular
connection. The reason might be we end up with more segments than max permitted,
or with a GSO packet with only one segment... (either way we break some
assumption and hit a BUG_ON)

(b) There is no check that the gso_size is > 20 when reducing it by 20, so we
might end up with a negative (or underflowing) gso_size or a gso_size of 0.
This can't possibly be good. Indeed this is probably somehow exploitable (or
at least can result in a kernel crash) by delivering crafted packets and perhaps
triggering an infinite loop or a divide by zero... As a reminder: gso_size (MSS)
is related to MTU, but not directly derived from it: gso_size/MSS may be
significantly smaller then one would get by deriving from local MTU. And on
some NICs (which do loose MTU checking on receive, it may even potentially be
larger, for example my work pc with 1500 MTU can receive 1520 byte frames [and
sometimes does due to bugs in a vendor plat46 implementation]). Indeed even just
going from 21 to 1 is potentially problematic because it increases the number
of segments by a factor of 21 (think DoS, or some other crash due to too many
segments).

(c) It's always safe to not increase the gso_size, because it doesn't result in
the max packet size increasing.  So the skb_increase_gso_size() call was always
unnecessary for correctness (and outright undesirable, see later). As such the
only part which is potentially dangerous (ie. could cause backwards compatibility
issues) is the removal of the skb_decrease_gso_size() call.

(d) If the packets are ultimately destined to the local device, then there is
absolutely no benefit to playing around with gso_size. It only matters if the
packets will egress the device. ie. we're either forwarding, or transmitting
from the device.

(e) This logic only triggers for packets which are GSO. It does not trigger for
skbs which are not GSO. It will not convert a non-GSO MTU sized packet into a
GSO packet (and you don't even know what the MTU is, so you can't even fix it).
As such your transmit path must *already* be able to handle an MTU 20 bytes
larger then your receive path (for IPv4 to IPv6 translation) - and indeed 28
bytes larger due to IPv4 fragments. Thus removing the skb_decrease_gso_size()
call doesn't actually increase the size of the packets your transmit side must
be able to handle. ie. to handle non-GSO max-MTU packets, the IPv4/IPv6 device/
route MTUs must already be set correctly. Since for example with an IPv4 egress
MTU of 1500, IPv4 to IPv6 translation will already build 1520 byte IPv6 frames,
so you need a 1520 byte device MTU. This means if your IPv6 device's egress
MTU is 1280, your IPv4 route must be 1260 (and actually 1252, because of the
need to handle fragments). This is to handle normal non-GSO packets. Thus the
reduction is simply not needed for GSO packets, because when they're correctly
built, they will already be the right size.

(f) TSO/GSO should be able to exactly undo GRO: the number of packets (TCP
segments) should not be modified, so that TCP's MSS counting works correctly
(this matters for congestion control). If protocol conversion changes the
gso_size, then the number of TCP segments may increase or decrease. Packet loss
after protocol conversion can result in partial loss of MSS segments that the
sender sent. How's the sending TCP stack going to react to receiving ACKs/SACKs
in the middle of the segments it sent?

(g) skb_{decrease,increase}_gso_size() are already no-ops for GSO_BY_FRAGS
case (besides triggering WARN_ON_ONCE). This means you already cannot guarantee
that gso_size (and thus resulting packet MTU) is changed. ie. you must assume
it won't be changed.

(h) changing gso_size is outright buggy for UDP GSO packets, where framing
matters (I believe that's also the case for SCTP, but it's already excluded
by [g]).  So the only remaining case is TCP, which also doesn't want it
(see [f]).

(i) see also the reasoning on the previous attempt at fixing this
(commit fa7b83bf3b156c767f3e4a25bbf3817b08f3ff8e) which shows that the current
behaviour causes TCP packet loss:

  In the forwarding path GRO -> BPF 6 to 4 -> GSO for TCP traffic, the
  coalesced packet payload can be > MSS, but < MSS + 20.

  bpf_skb_proto_6_to_4() will upgrade the MSS and it can be > the payload
  length. After then tcp_gso_segment checks for the payload length if it
  is <= MSS. The condition is causing the packet to be dropped.

  tcp_gso_segment():
    [...]
    mss = skb_shinfo(skb)->gso_size;
    if (unlikely(skb->len <= mss)) goto out;
    [...]

Thus changing the gso_size is simply a very bad idea. Increasing is unnecessary
and buggy, and decreasing can go negative.

Fixes: 6578171a7ff0 ("bpf: add bpf_skb_change_proto helper")
Signed-off-by: Daniel Borkmann <daniel@iogearbox.net>
Cc: Dongseok Yi <dseok.yi@samsung.com>
Cc: Willem de Bruijn <willemb@google.com>
Link: https://lore.kernel.org/bpf/CANP3RGfjLikQ6dg=YpBU0OeHvyv7JOki7CyOUS9modaXAi-9vQ@mail.gmail.com
Link: https://lore.kernel.org/bpf/20210617000953.2787453-2-zenczykowski@gmail.com

(cherry picked from commit 364745fbe981a4370f50274475da4675661104df https://git.kernel.org/pub/scm/linux/kernel/git/bpf/bpf-next.git/commit/?id=364745fbe981a4370f50274475da4675661104df )
Test: builds, TreeHugger
Bug: 158835517
Bug: 188690383
Signed-off-by: Maciej Żenczykowski <maze@google.com>
Change-Id: I0ef3174cbd3caaa42d5779334a9c0bfdc9ab81f5
Signed-off-by: budianto87 <budianto87@users.noreply.github.com>

---
## [semihalf-mazurek-michal/opentitan](https://github.com/semihalf-mazurek-michal/opentitan)@[29b8d2c3e7...](https://github.com/semihalf-mazurek-michal/opentitan/commit/29b8d2c3e7fde48a117a31241c508bd4325f5b88)
#### Friday 2022-03-18 12:49:09 by Rupert Swarbrick

[dv,verilator] Make multiple sim_ctrl extensions play nicely

I'd finally got annoyed enough about not being able to pass "-t" in
the middle of a command line to figure out what was going on. It turns
out that by default getopt_long rearranges its arguments to put all
positional args at the end. That's nice, because it allows you code to
easily support stuff like

   my_program -a -b positional0 -c -d positional1

and, post-parse, it will find positional0 and positional1 as the last
two arguments. (If long enough in the tooth, you might remember having
to do "my_program -a -b -c -d positional0 positional1" for some
programs: this is what getopt fixes for us!)

Unfortunately, this behaviour plays havoc when more than one parser
wants to look at argv at once. For example, suppose you have

   my_program --some-args ARG --no-args

and you parse this twice. The first parser understands --no-args and
the second understands --some-args. With the default behaviour and ":"
at the start of the optstring, the first parser will ignore the
unknown --some-args argument and move the positional ARG to the end.
But then the second parser sees

  my_program  --some-args --no-args ARG

and tries to pass "--no-args" as the value to "--some-args". Much
confusion ensues...

Fortunately, we can pass '-' at the start of optstring to disable this
behaviour. The result is harder to parse if you're interested in
positional arguments (which is why this isn't the default behaviour)
but works when you have multiple parsers that have to place nicely
together.

Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

---
## [huggingface/datasets](https://github.com/huggingface/datasets)@[a8fa7cfe95...](https://github.com/huggingface/datasets/commit/a8fa7cfe95e06c8a667c4d7c5b7c7287b7e9ac4f)
#### Friday 2022-03-18 14:22:52 by RenChu Wang

Multi-GPU support for `FaissIndex` (#3721)

* 🎉 This commit fixes huggingface/datasets#3716

This commit adds handling for faiss indices that run on multiple GPUs.

* 🤕 Stupid mistake in that index isn't returned in the function handling device.

Now it's fixed. Hopefully the PR isn't merged yet!

* 🗎 Updated documents to reflect changes I made in the code.

Update `device`'s document to include negative numbers and lists.

* 1️⃣ The line should not exceed length: 119

It seems that this is what circle CI checked anyways.

* 🥴 Apply suggestions from code review

Missed it the first time :)

Co-authored-by: Albert Villanova del Moral <8515462+albertvillanova@users.noreply.github.com>

* 🛠️ Fixed my fixes.

Updated code to address concerns.

* 🇫 Update src/datasets/search.py

Using f-strings in docs.

Co-authored-by: Quentin Lhoest <42851186+lhoestq@users.noreply.github.com>

Co-authored-by: Albert Villanova del Moral <8515462+albertvillanova@users.noreply.github.com>
Co-authored-by: Quentin Lhoest <42851186+lhoestq@users.noreply.github.com>

---
## [zengxin166850/elasticsearch](https://github.com/zengxin166850/elasticsearch)@[37ea6a8255...](https://github.com/zengxin166850/elasticsearch/commit/37ea6a8255623d41be7df11440610ffa958ce50e)
#### Friday 2022-03-18 15:13:59 by Nik Everett

TSDB: Support GET and DELETE and doc versioning (#82633)

This adds support for GET and DELETE and the ids query and
Elasticsearch's standard document versioning to TSDB. So you can do
things like:
```
POST /tsdb_idx/_doc?filter_path=_id
{
  "@timestamp": "2021-12-29T19:25:05Z", "uid": "adsfadf", "v": 1.2
}
```

That'll return `{"_id" : "BsYQJjqS3TnsUlF3aDKnB34BAAA"}` which you can turn
around and fetch with
```
GET /tsdb_idx/_doc/BsYQJjqS3TnsUlF3aDKnB34BAAA
```
just like any other document in any other index. You can delete it too!
Or fetch it.

The ID comes from the dimensions and the `@timestamp`. So you can
overwrite the document:
```
POST /tsdb_idx/_bulk
{"index": {}}
{"@timestamp": "2021-12-29T19:25:05Z", "uid": "adsfadf", "v": 1.2}
```

Or you can write only if it doesn't already exist:
```
POST /tsdb_idx/_bulk
{"create": {}}
{"@timestamp": "2021-12-29T19:25:05Z", "uid": "adsfadf", "v": 1.2}
```

This works by generating an id from the dimensions and the `@timestamp`
when parsing the document. The id looks like:
* 4 bytes of hash from the routing calculated from routing_path fields
* 8 bytes of hash from the dimensions
* 8 bytes of timestamp
All that's base 64 encoded so that `Uid` can chew on it fairly
efficiently.

When it comes time to fetch or delete documents we base 64 decode the id
and grab the routing from the first four bytes. We use that hash to pick
the shard. Then we use the entire ID to perform the fetch or delete.

We don't implement update actions because we haven't written the
infrastructure to make sure the dimensions don't change. It's possible
to do, but feels like more than we need now.

There *ton* of compromises with this. The long term sad thing is that it
locks us into *indexing* the id of the sample. It'll index fairly
efficiently because the each time series will have the same first eight
bytes. It's also possible we'd share many of the first few bytes in the
timestamp as well. In our tsdb rally track this costs 8.75 bytes per
document. It's substantial, but not overwhelming.

In the short term there are lots of problems that I'd like to save for a
follow up change:
1. ~~We still generate the automatic `_id` for the document but we don't use
   it. We should stop generating it.~~ Included in this PR based on review comments.
2. We generated the time series `_id` on each shard and when replaying
   the translog. It'd be the good kind of paranoid to generate it once
   on the primary and then keep it forever.
3. We have to encode the `_id` as a string to pass it around
   Elasticsearch internally. And Elasticsearch assumes that when an id
   is loaded we always store as bytes encoded the `Uid` - which *does*
   have nice encoding for base 64 bytes. But this whole thing requires
   us to make the bytes, base 64 encode them, and then hand them back to
   `Uid` to base 64 decode them into bytes. It's a bit hacky. And, it's
   a small thing, but if the first byte of the routing hash encodes to
   254 or 255 we `Uid` spends an extra byte to encode it. One that'll
   always be a common prefix for tsdb indices, but still, it hurts my
   heart. It's just hard to fix.
4. We store the `_id` in Lucene stored fields for tsdb indices. Now
   that we're building it from the dimensions and the `@timestamp` we
   really don't *need* to store it. We could recalculate it when fetching
   documents. In the tsdb rall ytrick this'd save us 6 bytes per document
   at the cost of marginally slower fetches. Which is *fine*.
5. There are several error messages that try to use `_id` right now
   during parsing but the `_id` isn't available until after the parsing
   is complete. And, if parsing fails, it may not be possible to know
   the id at all. All of these error messages will have to change,
   at least in tsdb mode.
6. ~~If you specify an `_id` on the request right now we just overwrite
   it. We should send you an error.~~ Included in this PR after review comments.
7. We have to entirely disable the append-only optimization that allows
   Elasticsearch to skip looking up the ids in lucene. This *halves*
   indexing speed. It's substantial. We have to claw that optimization
   back *somehow*. Something like sliding bloom filters or relying on
   the increasing timestamps.
8. We parse the source from json when building the routing hash when
   parsing fields. We should just build it from to parsed field values.
   It looks like that'd improve indexing speed by about 20%.
9. Right now we write the `@timestamp` little endian. This is likely bad
   the prefix encoded inverted index. It'll prefer big endian. Might shrink it.
10. Improve error message on version conflict to include tsid and timestamp.
11. Improve error message when modifying dimensions or timestamp in update_by_query
12. Make it possible to modify dimension or timestamp in reindex.
13. Test TSDB's `_id` in `RecoverySourceHandlerTests.java` and `EngineTests.java`.

I've had to make some changes as part of this that don't feel super
expected. The biggest one is changing `Engine.Result` to include the
`id`. When the `id` comes from the dimensions it is calculated by the
document parsing infrastructure which is happens in
`IndexShard#pepareIndex`. Which returns an `Engine.IndexResult`. To make
everything clean I made it so `id` is available on all `Engine.Result`s
and I made all of the "outer results classes" read from
`Engine.Results#id`. I'm not excited by it. But it works and it's what
we're going with.

I've opted to create two subclasses of `IdFieldMapper`, one for standard
indices and one for tsdb indices. This feels like the right way to
introduce the distinction, especially if we don't want tsdb to cary
around it's old fielddata support. Honestly if we *need* to aggregate on
`_id` in tsdb mode we have doc values for the `tsdb` and the
`@timestamp` - we could build doc values for `_id` on the fly. But I'm
not expecting folks will need to do this. Also! I'd like to stop storing
tsdb'd `_id` field (see number 4 above) and the new subclass feels like
a good place to put that too.

---
## [WordPress/gutenberg](https://github.com/WordPress/gutenberg)@[3ea2d42b0a...](https://github.com/WordPress/gutenberg/commit/3ea2d42b0a6a206663735a47f9796bd42eda2186)
#### Friday 2022-03-18 15:32:20 by Dennis Snell

Blocks: Remember raw source block for invalid blocks. (#38923)

Part of #38922

When the editor is unable to validate a block it should preserve the
broken content in the post and show an accurate representation of that
underlying markup in the absence of being able to interact with it.

Currently when showing a preview of an invalid block in the editor we
attempt to re-generate the save output for a block given the attributes
we originally parsed. This is a flawed approach, however, because by
the nature of being invalid we know that there is a problem with those
attributes as they are.

In this patch we're introducing the `__unstableBlockSource` attribute on 
a block which only exists for invalid blocks at the time of this patch. That 
`__unstableBlockSource` carries the original un-processed data for a block
node and can be used to reconstruct the original markup without using
garbage data and without inadvertently changing it through the series
of autofixes, deprecations, and the like that happen during normal block loading.

The noticable change is in `block-list/block` where we will be showing
that reconstruction rather than the re-generated block content. Previously
it was the case that the preview might represent a corrupted version of the
block or show the block as if emptied of all its content. Now, however,
the preview sould accurately reflect the HTML in the source post even
when it's invalid or unrecognized according to the editor.

Further work should take advantage of the `__unstableBlockSource`
property to provide a more consistent and trusting experience for
working with unrecognized content.

---
## [cacardona53/FUNDAMENTALS-OF-HTML-Fashion-Blog](https://github.com/cacardona53/FUNDAMENTALS-OF-HTML-Fashion-Blog)@[2af389266d...](https://github.com/cacardona53/FUNDAMENTALS-OF-HTML-Fashion-Blog/commit/2af389266d43d25912be29e9f290d307d23315e4)
#### Friday 2022-03-18 16:09:38 by Charlie

index.html

<!DOCTYPE html>

<html>

<head>
    <title>Everyday With Isa</title>
</head>

<body>
    <a href="#contact"><img
            src="https://s3.amazonaws.com/codecademy-content/courses/learn-html/elements-and-structure/profile.jpg"
            alt="Isa" /></a>
    <h3>by Isabelle Rodriguez | 1 day ago</h3>
    <h1>An Insider's Guide to NYFW</h1>
    <img src="https://s3.amazonaws.com/codecademy-content/courses/learn-html/elements-and-structure/image-one.jpeg"
        alt="image 1" />
    <p><a href="https://en.wikipedia.org/wiki/New_York_Fashion_Week" target="_blank">NYFW</a> can be both amazingly fun
        & incredibly overwhelming, especially if you’ve never been. Luckily, I’m here to give you an insider’s guide and
        make your first show a pleasurable experience. By taking my tips and tricks, and following your gut, you’ll have
        an unforgettable experience!</p>
    <img src="https://s3.amazonaws.com/codecademy-content/courses/learn-html/elements-and-structure/image-two.jpeg"
        alt="image 2" />
    <p>If you’re lucky or connected you can get an invite, sans the price tag. But I wasn’t so lucky or connected my
        first 2 years so I’m here to help you out. First, plan out which shows are most important to you and make a
        schedule and this is a biggie: SET A BUDGET. If you’re worrying about blowing your cash the whole time you won’t
        have fun. Then check out prices, days, and times and prioritize the designers you want to see most. Lastly,
        purchase your tickets and get excited!</p>
    <h2>Getting Tickets & Picking the Shows</h2>
    <h2>Dressing for the Shows</h2>
    <img src="https://s3.amazonaws.com/codecademy-content/courses/learn-html/elements-and-structure/image-three.jpeg"
        alt="image 3" />
    <p>Always be true to your own sense of style, if you don’t you’ll be uncomfortable the whole time and it will show.
        Remember, NYFW is about expressing yourself and taking in what the designers have chosen to express through
        their new lines. Also it’s important to wear shoes you’ll be comfortable in all day. Obviously you want to look
        good, but you’ll be on your feet all day long, so be prepared.</p>
    <h4>Related Content</h4>
    <ul>
        <li>How To Style Boyfriend Jeans</li>
        <li>When Print Is Too Much</li>
        <li>The Overalls Trend</li>
        <li>Fall's It Color: Blush</li>
    </ul>
    <div id="contact">
        <p><strong>email:</strong> isa@fashionblog.com | <strong>phone:</strong> 917-555-1098 |
            <strong>address:</strong> 371 284th St, New York, NY 10001</p>
    </div>
</body>

</html>

---
## [RatFromTheJungle/Skyrat-tg](https://github.com/RatFromTheJungle/Skyrat-tg)@[41aa1d2ee4...](https://github.com/RatFromTheJungle/Skyrat-tg/commit/41aa1d2ee421161505284504f4d6f76faf51b0f7)
#### Friday 2022-03-18 18:14:56 by SkyratBot

[MIRROR] Adds a colorblind accessability testing tool [MDB IGNORE] (#11995)

* Adds a colorblind accessability testing tool (#65217)

* Adds a colorblind accessability testing tool

I keep finding myself worrying about if things I create will be parsable
for colorblind people. So I've made a debug tool for approximating
different extreme forms of colorblindness.

It's very very much a hack. We can't do the proper correction required
to actually deal directly with long medium and short wavelengths of
light, so we need to rely on approximations. Part of that means say,
bright things being brighter then they ought to be. S not how people
actually experience things, but it's not something we can do anything
about in byond.

Anyway uh, it works by taking color matrixes, and using the plane master
grouping system floyd added to apply them to most all parts of the game
you would want to color correct.

There's some slight fragility here, but I couldn't think of a better way
of handling it.

We also need to deal with planes that have BLEND_MULTIPLY as their
blendmode, since that fucks up the filter. I've come up with a hack for
it, since I wanted to avoid breaking anything.

Oh and since I want it to apply to huds too I added plane masters to
represent them. I think that's about it.

Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>

* Adds a colorblind accessability testing tool

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>
Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[2e180d8393...](https://github.com/mrakgr/The-Spiral-Language/commit/2e180d83930ffba469ace6a14cc3a34800937e50)
#### Friday 2022-03-18 18:37:19 by Marko Grdinić

"10:10am. Had a hard time falling asleep, but not as bad as two days ago. Let me just read a chapter of Otome Survival and I will start.

10:30am. As fun as this is, let me start. It is time to start cleaning things up.

10:55am. I hate how Solaris is not importing object transforms.

Damn, maybe I should not be using SOP imports but something else.

11:05am. Damn it, no. Even if I name this from Houdini it just flattens and spills all the instances and flattens them.

11:10am. The scene graph is there. Why isn't the ROP output exporting it?

11:20am. I decided to ask. But let me go with the shading group approach for now.

11:35am. I've put shading groups on a few things, and Clarisse is grinding down. Probably because I exported the vines.

11:45am. Fuck Houdini. The shading groups are not showing up! Aghhhhhhh...

I have no choice. Let me import each object on an individual basis and I'll export them to separate files. That will allow me to contextualize them properly.

At this point, I just want to give up on this god forsaken scene. How much more time will it make me waste?

12pm. Let me take a break here. I need to rethink my whole approach. Maybe trying to just export the whole scene was too much. Houdini is absolute trash at anything but geometry wrangling.

I am starting to come to the view that if I really want to learn Solaris, I should do things from the ground up. Even when I export the objects individually, they don't get arranged into contexts. There is zero point in doing that.

1:40pm. Done with breakfast and chores. Honestly, I am too tired to mess with the pool scene anymore. I suppose I'll call it a victory for that bottom up shot and just move on.

I've already spent way too much time practicing as it is. 5.5 months is enough knowledge to get me started with Heaven's Key.

So why don't I finally do it. It wasn't exactly my plan to take 2.5 months for the pool scene. That kind of thing is something that should have happened in just a few days.

https://bakapervert.wordpress.com/heroine-survival-vol-1-chapter-14/

Let me read this chapter and then I will get something done.

1:50pm. Random practice is one thing, but the best results can be gotten when you work on what you want after all. I am interested in having my art be in synergy with my storytelling instead of producing random illustrations.

1:55pm. Enough of that chapter. Let me start mentally preparing myself.

I just can't waste any more time with auxiliary projects for the sake of practice. Now that I've been introduced to Clarisse, I should have everything I need to start making stuff for real. And practice I can get working on the actual thing. Unlike a pro though, I won't place any deadlines on myself.

My first project will be to model my own room. I'll have that be Euclid's room in game. It is the best reference I could have.

2pm. Yeah, it is time to get serious. I'll do a bunch of scenes like that and then move on to making music. Things will fall into place on their own as I go along.

I wonder how I can model interiors without the walls getting in the way? That is osmething I wanted to figure out for a while.

2:45pm. Heaven's Key start. I'll do it slowly as ramp up things over time as I go along.

Now how exactly do I approach interiors? Let me watch a vid.

I actually know how to do all the individual pieces and texturing, the trouble is how do I move around. Do I just hide the outer walls? Or do I dive inside and just deal with the clipping? Or do I cull the backfaces?

https://youtu.be/wrzSrjAY69c
How to Make Interiors in Blender (Tutorial)

2:55pm. Let me check out his process. I've been avoiding Blender Guru initially, most by accident, but now that I've given him a chance, I've found every one of his tutorials to be high quality.

Let me watch the vid while 3.1 Stable downloads.

https://youtu.be/wrzSrjAY69c?t=213

He suggests putting in a human and provides a link in the description. Yeah, I messed that up while making the pool scene. Having it in will be convenient.

https://youtu.be/wrzSrjAY69c?t=264
> I actually do it all from the camera view believe it or not.

https://youtu.be/wrzSrjAY69c?t=305
> And from there you want to get into lighting as quickly as possible.

https://youtu.be/wrzSrjAY69c?t=586

I see. I actually understand what 'Is Ray' means after watching the Clarisse Rendering Masterclass.

https://youtu.be/wrzSrjAY69c?t=607

Actually instead of doing the glass like that, he could just turn off caustics. That would solve the problem.

https://youtu.be/wrzSrjAY69c?t=731

Some sites to keep in mind for getting furniture. It is all paid. At the start I am going to have to do it on my own.

https://youtu.be/wrzSrjAY69c?t=911

These sites will make for good references.

https://youtu.be/wrzSrjAY69c?t=1138
> ...This is actually an advantage that you as a 3d artist has over a traditional interior designers. Most interior designers do not know 3d software. They are actually using crude photoshop wireframes and bringing in images and kind of like standing back and going: does that material work? When you have - we know how to use photorealistic, now real time thanks to viewport denoising, photorealistic images.

He is pretty interesting to listen to. He did not put much effort into it and yet thanks to 3d rendering, it looks quite realistic.

https://youtu.be/wrzSrjAY69c?t=1408

More resources.

4:15pm. I spend some time getting into it. I did the overall shape and put in a few blocks as standins for the main objects in the room. The proportions are off of course.

4:20pm. It really looks nice when I turn on Cycles.

Even though there are no textures, I can see the sunlight streaming in from the side.

This would be really annoying in Houdini. Right now I am better off doing the individual assets in Blender.

First though, let me texture.

The V-Ray library has a lot of textures including laminate which I need for the floor. I'll also need some wood for the ceiling. But how do I make use of the mat files? And I see in assets that they are all .tx files. Let me start up Houdini. I need to figure this out. Doing all the various items strewn about my room will take me some time.

But this will be my first real bit of modeling practice. My fumbling about in Houdini was nothing, but an embarassment.

It is a good thing I did not get rid of V-Ray just yet.

Now if only Houdini would load.

4:30pm. Put a V-Ray material on a sphere, it works. Try to import it in Solaris, it crashes. At this point something is just as likely as to not work than work. It really is unbelievable that V-Ray is paid software.

> Why is my texture pink in Blender?

> Pink means that the texture files are missing. If the texture files are still on your system, then it sounds like the textures are referenced relative to the blend file (the default behavior). This means that if you move the blend file and you don't move the textures, blender won't be able to find them.

https://blenderartists.org/t/v-ray-3ds-max-to-cycles/1120005

It seems it might be necessary to convert these materials to something I could use in Blender.

I didn't expect this. A lot of these materials have special setups too.

https://blender.community/c/rightclickselect/z6Y5/?sorting=hot

Right now I am trying to get around this issue. Materials are one thing, but I find it strange that I am having trouble loading the .tx textures themselves. Just now it occured to me that I should try it in Clarisse just to make sure that Blender isn't doing anything strange.

4:55pm. Clarisse loads the .tx files just fine. Oh boy. What do I do about this?

5pm. I have no idea what is going on.

https://youtu.be/ChgoGr9V-tc
Why your Textures are Pink in Blender (And How to Fix it!)

Let me watch this. I'll ask on SO after that.

Hmmm, what if I copied the textures into the Scene folder?

...No. I have no idea. Let me watch the vid.

https://blender.stackexchange.com/questions/257854/why-are-v-ray-asset-library-textures-pink-when-loaded-into-blender

5:15pm. I'll have to see if somebody can come up with the answer.

But now I have to stop and think.

I have two choices: Since it works in Clarisse, I can do all my texturing there.

Or I can just ditch the V-Ray library textures and download some free ones off the net.

...Let me do some chores while I think. I'll step away from the screen for 10m.

5:30pm. I am back.

5:40pm. I am going to get Clarisse route. But to do that, I really need to figure out how shading groups work in it.

5:50pm. Let me have lunch.

6:10pm. Done with lunch.

6:20pm. I've imported the room in Clarisse. Actually I made a whole separate room just so I could test if shading works properly. I've had time to think and I've come to the conclussion there there is absolutely no need to worry about proportions. I'll get the roughly right now, and then adjust the relative shapes of all the objects so they match up with my own room.

Let me test out the shading groups. This works really well.

Blender exports shading groups without a problem.

And actually I am confused that shading groups in Houdini work off point groups.

...Let me try making them off primitive groups again.

...I see the top group...and when I try to assign a shader, it assigns to everything.

Houdini's USD exports are absolute shit.

...But when you assign prim groups to everything it works well. Ok good. What about point groups? Let me test it with them.

6:40pm. No it does not work with point groups? Why did I think it did?

Damn, this must be the reason why I got no shading groups when I tried exporting earlier in the day. I made a huge mistake somehow.

> I see now that I can use primitive groups to set shading groups in USD. To make this work, I have to mark them as Subset Groups in Import Data in the USD Export nodes either LOP or SOP.

I wrote primitives group here, but somehow I was thinking point groups in the morning. Did my IQ go down permanently because of Covid last month?

6:50pm. Now that is loading the whole thing, vines included, I see that there is a loading progress bar in the bottom right. I did not notice it earlier in the day.

The load is extremely slow with the vines included.

7pm. I tried putting on the pool fence segment and it works. But I have no way of selecting them as a group. All the objects are named mesh_* and if I select everything I do not get the individual shading groups.

So I am back where I was in the morning. I have no way of shading these unless I want to go one by one.

7:15pm. I won't lie, my motivation to continue right now is near zero. Maybe I could get into if I start, but I had enough.

7:20pm. I think like when I was doing programming, I should just rehearse things mentally first and then start firing away.

I am going to start the procoess by texturings the floor, wall and ceiling. Then I will move to modeling the props from there. None of this is hard, and I would have made progress even today if Blender did not wreck my momentum by not being able to load .tx textures.

I am going to start off by first shaping the overall shape of the room, and then solidifying it. I want to be able to texture the outside parts as well even if I do not need to. The terrace should be present in some scenes.

It would be best to carve out the doorframe using booleans, but those do not work when the surface is closed.

No, I need to make things as simple as possible. Forget the terrace. Forget even the proportions. I can get those roughly right and then adjust them. I was on the right path initially. I just need to texture the room and then get to placing the props. This is more than within my skill level.

7:30pm. I just need to dedicate myself to this. I finally have some straightforward modeling work in front of me. No more that quasi programming trash with Houdini which just keeps holding me back. I just need to sit down and do the art. I'll get one piece done, and then another. By the end of that I'll have a proper lure.

Before January I really did have fun with sculpting. It is time to go back to that kind of work. I do not need to be a genius to make this work. I just need a good deal of persistence."

---
## [salvadorcunat/subsurface.github.io](https://github.com/salvadorcunat/subsurface.github.io)@[ad4b82193b...](https://github.com/salvadorcunat/subsurface.github.io/commit/ad4b82193be920f3b90c6a31a757368dcc202c54)
#### Friday 2022-03-18 18:41:25 by Dirk Hohndel

small updates to deal with horizontal lines

I wonder if the magic that creates them isn't more trouble than it's worth.
Maybe it would be better to make them explicit? This seems hacky...

This commit also has a couple of tiny edits to the things Jason brought
over from the old FAQ.

Signed-off-by: Dirk Hohndel <dirk@hohndel.org>

---
## [avar/git](https://github.com/avar/git)@[6acd875977...](https://github.com/avar/git/commit/6acd87597722faf9bf93d6eb3773705e5f6dbc4e)
#### Friday 2022-03-18 18:58:42 by Ævar Arnfjörð Bjarmason

object-file.c: do fsync() and close() before post-write die()

Change write_loose_object() to do an fsync() and close() before the
oideq() sanity check at the end. This change re-joins code that was
split up by the die() sanity check added in 748af44c63e (sha1_file: be
paranoid when creating loose objects, 2010-02-21).

I don't think that this change matters in itself, if we called die()
it was possible that our data wouldn't fully make it to disk, but in
any case we were writing data that we'd consider corrupted. It's
possible that a subsequent "git fsck" will be less confused now.

The real reason to make this change is that in a subsequent commit
we'll split this code in write_loose_object() into a utility function,
all its callers will want the preceding sanity checks, but not the
"oideq" check. By moving the close_loose_object() earlier it'll be
easier to reason about the introduction of the utility function.

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>

---
## [prairir/Buoy](https://github.com/prairir/Buoy)@[17303fa530...](https://github.com/prairir/Buoy/commit/17303fa53019c7f33eade8584e50edaff0c9eda5)
#### Friday 2022-03-18 19:50:20 by Ryan Prairie

Add: translation package base & (de)compression

translation package base is done. It has a translate and untranslate
function. It also has unexported functions of encrypt/decrypt and
compression/decompression.

I also changed config to have password as a byte slice. This way we can
save time by casting once on init instead of casting every packet(1/10
time).

I chose gzip as a compression algorithm because it uses deflate on the
background but is more agressive on its actual compression. We need to
save size on the larger boys, I dont care about wasting CPU cycles on
the smaller packets.

I want to avoid IP fragmentation whenever possible so Im realllllllllly
betting on gzip to take care of it. There is still the *strong* chance
that its not enough and we should embrace fragmentation. Fuck
fragmentation, its a nightmare to implement ourselves.

---
## [Atom-X-Devs/android_kernel_xiaomi_scarlet](https://github.com/Atom-X-Devs/android_kernel_xiaomi_scarlet)@[9c2ac318c6...](https://github.com/Atom-X-Devs/android_kernel_xiaomi_scarlet/commit/9c2ac318c6f9af67c9b406c5207959bf4ee99366)
#### Friday 2022-03-18 20:16:49 by Angelo G. Del Regno

Makefile.lib: Lower kernel gzip compression to fastest

You're reading this - so you're trying to understand "JUST WHY OMG".
That's already a good step.

First of all, this is a downstream kernel - always keep that in mind!
Now, this kernel is targeting new *very powerful* Qualcomm platforms
like SM8250 and the Sony Edo platform - which has a very fast UFS card.

Keep in mind that the bootloader sets the CPU at a frequency that is
slightly faster than the "in the middle" ones, which is anyway not
veeeery fast - but that's good, really. I agree.

So.. check this out:   for Image.gz-dtb.....
COMP_LEVEL    SIZE
9             20116171
5      	      20220479
2      	      20940223
1      	      21231290

Remember again that we're loading from a UFS card and that
we are loading ~1.1MB more out of a 20MB file.
If you're smart enough you surely know already about RAM and CPU
overhead of very high compression levels.

If you still disagree with what I just did, read this commit description
another 20 times, or more, until you understand it. :)))

Signed-off-by: Tashfin Shakeer Rhythm <tashfinshakeerrhythm@gmail.com>

---
## [chandu078/kernel_oneplus_sm8250](https://github.com/chandu078/kernel_oneplus_sm8250)@[2c5477a6a7...](https://github.com/chandu078/kernel_oneplus_sm8250/commit/2c5477a6a702e96bfa6e82ac324abeb2bc189af9)
#### Friday 2022-03-18 20:30:36 by alk3pInjection

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

---
## [stickbear2015/sc-sounds](https://github.com/stickbear2015/sc-sounds)@[a2f4baa39d...](https://github.com/stickbear2015/sc-sounds/commit/a2f4baa39d23bb05452b1e497f10f9758b8f2e9a)
#### Friday 2022-03-18 22:26:44 by munchkinbear

fixes buffers because fuck you for not creating the goddamn buffers file.

---
## [Mechanelize/tgstation](https://github.com/Mechanelize/tgstation)@[906fb0682b...](https://github.com/Mechanelize/tgstation/commit/906fb0682bab6a0975b45036001c54f021f58ae7)
#### Friday 2022-03-18 22:27:22 by necromanceranne

Ballistic to Energy: Autorifles for Thermal Pistols; Adds .38 Crate to Cargo (#64280)

About The Pull Request
The design doc behind this PR, which is only mildy been deviated from on some of the end particulars. Cobby-Approved! Maintainer Discussed!
https://hackmd.io/@6DbtsAKCTtW_9MByKFjZqg/r1xYKCNOt

Cargo Changes
Cargo has had all WT-550's removed and replaced with Thermal Pistols.
Cargo can now order Thermal Pistols, a kind of energy/ballistic hybrid weapon shooting chunks of altered nanites into people. We couldn't use them in people, so maybe we'll use them as bullets! Magma/Ice bullets, to be exact.
You can, after paying a whopping 4K on a goodie pack (you have to pay from your own personal account) buy a .38 revolver. This is mostly to help some poor detective who lost their revolve in what I'm sure will be an inevitable scramble for ballistics. If even the 4K pricetag isn't enough, at least it requires detective access to open the pack...I hope.
Some of the crates that contained autorifle related items have been changed/removed.

unknown (2)

securarevolver 4 0

Science Changes
Ballistic Weaponry node no longer exists, and has been replaced with Exotic Ammo as both the pre-requisite to other nodes, as well as being able to be researched as soon as the Weaponry node is unlocked and not Advanced Weaponry.

Thermal Pistols
-Fairly average bullet statistics; 10 AP but shooting into Energy armor. 20 damage (Brute for cryo, Burn for inferno). Decent wounding potential, but individually much lower ammo counts than lasers.
-Bought in twinned pairs in a two gun holster (just for normal sized energy guns). They're normal sized.
-Each gun has 8 shots (thereabouts). 16 between two.
-Cryo pistols do a knockdown and extra damage against extremely hot targets. Inferno pistols do an explosion cantered on the target against extremely cold targets.
-The guns are EMP-proof.

Why It's Good For The Game
The current gameplay loop of crew combatants is them relying on backup and retreating as necessary to reload their weapons during fights. The ability to repeatedly harry opponents in the field reloads is something that should be moved away from for crew equipment, as it emphasizes lone wolf tactics and one-man army problems, with boxes full of spare ammo usually allowing any single combatant to outlast multiple foes. In addition, ballistics often are not subject to the same (interesting) limitations of energy weapons, so they're typically a no-brainer choice. We shouldn't have such an easy choice be readily available like that.

The thermal pistols present a more challenging weapon to use as a solo combatant but become far more versatile and potent when paired with a decent buddy and basic level co-ordination. They're not a straightforward choice for every situation, but instead are a weapon employed given the right circumstances for them to shine.

In addition to the gameplay issues that ballistics pose, we're in a goddamn spacegame. Unless the ballistics are noticeably weird (they're not), we should expect that our more advanced research station has some pretty odd guns of the energy variety.

Changelog
🆑 Necromanceranne, quin
add: Adds the Inferno and Cryo Pistols. A hybrid energy/ballistic weapon, to cargo. It can be purchased in either a goodies pack or a normal crate order.
add: Thermal Pistols do more damage and a special based on temperature of the target hit.
add: Inferno pistols cause an explosion when they hit a severely cold target.
add: Cryo pistols cause a knockdown and extra damage if they hit a severely hot target.
add: There is a special nanite pistol, which is admin spawned. Don't tell anyone about the forbidden ballistic energy gun.
add: You can order a .38 revolver as a goodie pack. It is expensive.
del: Removes WT-550's from cargo and related content from the techweb/protolathes.
balance: Exotic Ammo is now much earlier in the tech web to take the place of Ballistic Weaponry.
/🆑

---
## [CamK06/WinBot](https://github.com/CamK06/WinBot)@[d6aea48c10...](https://github.com/CamK06/WinBot/commit/d6aea48c10f993efe675eb53870f8052e9b1265a)
#### Friday 2022-03-18 23:59:20 by Cam K

FUCK YOU DISCORD
Shitcord... HOW IS IT POSSIBLE TO BE **THIS** INCOMPETENT WHEN IMPLEMENTING A VERY BASIC API FUNCTION!?!?!?!?!?!??!

---

