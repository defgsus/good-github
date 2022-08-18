## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-08-17](docs/good-messages/2022/2022-08-17.md)


1,979,090 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,979,090 were push events containing 3,022,999 commit messages that amount to 226,885,922 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 35 messages:


## [KDr2/pytorch](https://github.com/KDr2/pytorch)@[4c8cfb57aa...](https://github.com/KDr2/pytorch/commit/4c8cfb57aa3ac58112efb693635198b07edf008f)
#### Wednesday 2022-08-17 00:04:04 by Edward Z. Yang

Convert SymInt tracing to mode based tracing (#83380)

We're on our way to deleting ProxyTensor entirely (see https://github.com/pytorch/pytorch/pull/83330 ), but before we can do that, we have to delete ProxySymInt first. Here's the plan.

Changes in torch.fx.experimental.symbolic_shapes

* The general idea is to do mode based tracing. This means we need a mode that can interpose on all SymInt operations. There are a few ways to do this, but I've done it the easy way: (1) I have a separate mode for SymInt operations specifically called SymDispatchMode, and (2) this mode operates on PySymInt (and not the basic SymInt which is user visible). I elided Int from the name because if we add SymFloats I want to use the same mode to handle those as well, and I used Dispatch rather than Function because this is the "inner" dispatch operating PySymInt and not SymInt (this is not a perfect analogy, but SymFunctionMode definitely seemed wrong as you still must go through the C++ binding.) The mode is entirely implemented in Python for ease of implementation. We could have implemented this more symmetrically to TorchFunctionMode in C++, but I leave that as later work; this API is unlikely to get used by others (unlike TorchFunctionMode). One downside to not doing the mode in C++ is that we still have to do the hop via a preexisting PySymInt to wrap; this is currently not a big deal as conversion to SymInts only really happens when there is already another SymInt floating around. SymDispatchMode is pared down from TorchDispatchMode; there is no ancestor tracking since I don't expect people to be mixing up SymDispatchModes.
*  I made some improvements for tracing. When I invoke the SymDispatchMode handler, I would like constants to show up as constants, so they can be directly inlined into the FX graph (rather than going through a wrapping process first, and then the wrapped SymInt being used in the operation). To do this, I directly track if a PySymInt is a constant at construction time. Only wrapped PySymInts are constants.
* For convenience, PySymInts now support all magic methods that regular SymInts do. This is so that redispatch inside the SymDispatchMode can be written the idiomatic way `func(*args, **kwargs)` where func is an operator. The original names are retained for direct C++ calls.

Changes in torch.fx.experimental.proxy_tensor

* OK, so we got a new SymDispatchMode, so we define a ProxySymDispatchMode and activate it when we start tracing. This mode is currently unconditionally activated although technically we only need to activate it when doing symbolic tracing (it doesn't matter either way as there are no SymInts if you are not doing symbolic tracing).
* We delete ProxySymInt. To do this, we must now record the proxy for the SymInt some other way. Based on discussion with Chillee, it is more intuitive to him if the proxies are still recorded on the SymInt in some way. So we store them in the `__dict__` of the PySymInt, indexed by Tracer. An improvement is to make this a weak map, so that we remove all of these entries when the tracer dies. In an original version of this PR, I keyed on the mode itself, but tracer is better as it is accessible from both modes (and as you will see, we will need to fetch the map from both the ProxySymDispatchMode as well as the ProxyTorchDispatchMode.) The implementation of SymDispatchMode now simply retrieves the proxies, performs the underlying operation as well as the FX graph recording, and then records the output proxy to the PySymInt. Note that FX tracing does not work with proxies and SymInts, so we manually call `call_function` to ensure that the correct operations get recorded to the graph. This means conventional FX retracing with proxies only will not work with these graphs, but there wasn't really any reason to do this (as opposed to `make_fx` retracing) anyway. Constants are detected and converted directly into Python integers.
* SymInts can show up as arguments to tensor operations, so they must be accounted for in ProxyTorchDispatchMode as well. This is done by searching for SymInt arguments and converting them into proxies before the proxy call. This can be done more efficiently in a single `tree_map` but I'm lazy. The helper `unwrap_symint_proxy` conveniently implements the unwrapping in one place given a tracer; unfortunately it cannot be shared with SymDispatchMode as SymDispatchMode gets PySymInts, but ProxyTensorMode gets SymInts. Similarly, tensors that are returned from tensor operations can have SymInts in their shapes, which need fresh proxies allocated. To avoid leaking internal details of SymInt shape computation to the tensor operation graph, these SymInts are always given proxies derived from `x.size(dim)` call on their return tensor. We also need to do this for strides and numel but have not done so yet. Furthermore, we must avoid tracing internal SymInt calls while we run meta operations on the true operation; this is achieved by also disabling SymInt tracing on the inside of tensor tracing. This is analogous to how tensor tracing is disabled inside the implementation of tracing mode, but unfortunately we are unable to use the same mechanism (this would have been easier if the two modes could be combined somehow, and I am amenable to suggestions to try harder to achieve this.)
* Because there are no more ProxySymInts, we no longer need to do anything to unwrap SymInt. Furthermore, we do not need to reallocate ProxySymInts on class creation.
* If a bare SymInt without a Proxy is encountered, it is assumed that this must be a constant. `create_arg` handles this case. Non-constant free SymInts result in an assert error.
* The initial input handling in `dispatch_trace` involves traversing all of the input tensors, traversing over their shapes, and assigning proxies for the SymInts in shapes in the same way we handle proxies for the output tensors.

The preexisting testing is inadequate but will be better after I rebase past https://github.com/pytorch/pytorch/pull/82209

Signed-off-by: Edward Z. Yang <ezyang@fb.com>
Pull Request resolved: https://github.com/pytorch/pytorch/pull/83380
Approved by: https://github.com/samdow

---
## [avar/git](https://github.com/avar/git)@[5beca49a0b...](https://github.com/avar/git/commit/5beca49a0b1f3c6d05a4437ca037ab2123a2de57)
#### Wednesday 2022-08-17 00:06:19 by Ævar Arnfjörð Bjarmason

test-lib: simplify by removing test_external

Remove the "test_external" function added in [1]. This arguably makes
the output of t9700-perl-git.sh and friends worse. But as we'll argue
below the trade-off is worth it, since "chaining" to another TAP
emitter in test-lib.sh is more trouble than it's worth.

The new output of t9700-perl-git.sh is now:

	$ ./t9700-perl-git.sh
	ok 1 - set up test repository
	ok 2 - use t9700/test.pl to test Git.pm
	# passed all 2 test(s)
	1..2

Whereas before this change it would be:

	$ ./t9700-perl-git.sh
	ok 1 - set up test repository
	# run 1: Perl API (perl /home/avar/g/git/t/t9700/test.pl)
	ok 2 - use Git;
	[... omitting tests 3..46 from t/t9700/test.pl ...]
	ok 47 - unquote escape sequences
	1..47
	# test_external test Perl API was ok
	# test_external_without_stderr test no stderr: Perl API was ok

At the time of its addition supporting "test_external" was easy, but
when test-lib.sh itself started to emit TAP in [2] we needed to make
everything surrounding the emission of the plan consider
"test_external". I added that support in [2] so that we could run:

	prove ./t9700-perl-git.sh :: -v

But since then in [3] the door has been closed on combining
$HARNESS_ACTIVE and -v, we'll now just die:

	$ prove ./t9700-perl-git.sh :: -v
	Bailout called.  Further testing stopped:  verbose mode forbidden under TAP harness; try --verbose-log
	FAILED--Further testing stopped: verbose mode forbidden under TAP harness; try --verbose-log

So the only use of this has been that *if* we had failure in one of
these tests we could e.g. in CI see which test failed based on the
test number. Now we'll need to look at the full verbose logs to get
that same information.

I think this trade-off is acceptable given the reduction in
complexity, and it brings these tests in line with other similar
tests, e.g. the reftable tests added in [4] will be condensed down to
just one test, which invokes the C helper:

	$ ./t0032-reftable-unittest.sh
	ok 1 - unittests
	# passed all 1 test(s)
	1..1

It would still be nice to have that ":: -v" form work again, it
never *really* worked, but even though we've had edge cases test
output screwing up the TAP it mostly worked between d998bd4ab67 and
[3], so we may have been overzealous in forbidding it outright.

I have local patches which I'm planning to submit sooner than later
that get us to that goal, and in a way that isn't buggy. In the
meantime getting rid of this special case makes hacking on this area
of test-lib.sh easier, as we'll do in subsequent commits.

The switch from "perl" to "$PERL_PATH" here is because "perl" is
defined as a shell function in the test suite, see a5bf824f3b4 (t:
prevent '-x' tracing from interfering with test helpers' stderr,
2018-02-25). On e.g. the OSX CI the "command perl"... will be part of
the emitted stderr.

1. fb32c410087 (t/test-lib.sh: add test_external and
   test_external_without_stderr, 2008-06-19)
2. d998bd4ab67 (test-lib: Make the test_external_* functions
   TAP-aware, 2010-06-24)
3. 614fe015212 (test-lib: bail out when "-v" used under
   "prove", 2016-10-22)
4. ef8a6c62687 (reftable: utility functions, 2021-10-07)

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [petrelharp/pyslim](https://github.com/petrelharp/pyslim)@[3571a25e1f...](https://github.com/petrelharp/pyslim/commit/3571a25e1f8500f1a036f3a8a9deb1730c580e55)
#### Wednesday 2022-08-17 00:20:26 by andrewkern

added slim clone and compile to GH actions

alter when to run actions for dev

add windows to list of oses

pip failing

conditional on slim build

add slim windows build rule

MORE WINDOZE

adding SLiM depends

debugging

think we are working?

still debugging

still futzing

thrash

adding autotools to msys2 install stuff

thrash

add conda

thrash

get rid of tmate

thrash

dont' need source proffile?

ugh

tmate revenge

adding conditional on tmate

removed source from build

tmatey

setup auto conda env

updated tests

moar tests

typo

mamba

no pip?

ugh

back to miniconda

pwr

yml

moar

mamba redux?

blurg

yarg

still going

last one

Update tests.yml

blag2

altering conda vs pip balance

urg

jkhj

shell nightmare

try another change

which pip

moving stuff

adsf

dsfk

asd

adsfdasf

msys shell madness

asdfasdf

Update tests.yml

as;dlkfj

sadf

happy windows filepaths from conf

sdafdsa

passing tests!

remove dev branch action

removed print

comment out slim build step on osx/ubuntu

Update tests.yml

comments

refactor test actions

trying to limit matrix of sys / env

exclude rather than include

arrays

less is more

even fewer jobs?

kjh

sdf

more excludes?

last one for the night

jhlkj

asd

jkhkj

lkjlkj

sad

tmate

adfasdf

which dot file?

why isn't conda working?

try again

asdfasdf

bump cache

no base

asdf

fast debug

mamba with osx

micro

fixing micromamba

try cache on micro

add linux in

oops should have been ubuntu

actually try tests for a min

okay here we go windoze

conditions

now with tests

even cleaner

cache slim

true

cache2

cawde

undo cache

parathenses

asdfsad

cache redux

final clean

moar

new cache path

tmate to find windows path

cache path again

zstd

path again

sdfasd

kjhglghj

more zstd

adfs

ugh

add zstd to conda reqs

add workaround for windows cache

pinning cache action

holy shit caching is working?!?

ha

add back macos, ubuntu

ready for prime time

---
## [matchu/impress-2020](https://github.com/matchu/impress-2020)@[ce503ea730...](https://github.com/matchu/impress-2020/commit/ce503ea730d071bdde0409696ae86ad604031648)
#### Wednesday 2022-08-17 00:35:00 by Matchu

Start building a login form, behind a feature flag

Thinking about longevity, I think I wanna cut Auth0 loose, and just go back to using our own auth.

I had figured at the time that I didn't want to integrate with OpenNeo ID's whole mess, and I didn't want to write a whole new auth system, so Auth0 seemed to make things easier.

But now, it's just kinda a lot to be carrying along an external service as a dependency for login, especially when we've got all the stuff in the database right here. I wanna remove architecture pieces! Get it outta here!

And I'll finally build account creation from the 2020 site while I'm at it, which seemed like it was gonna be a bit of a pain with Auth0 and syncing anyway. (I think at the time I was a bit more optimistic about a full transfer from one system to another, but that's much further off than I realized, and this path will be much better for keeping things in sync.)

---
## [Stutternov/sojourn-station](https://github.com/Stutternov/sojourn-station)@[931b7187bd...](https://github.com/Stutternov/sojourn-station/commit/931b7187bd31e71d2a16792b7b2dd042cb049d97)
#### Wednesday 2022-08-17 01:04:36 by nikothedude

"Optimizes" superior mobcode with somewhat of a nuclear option in terms of optimization. Fixes stealth bird targetting, fixes mobs being permastunned as well as not getting up from knockdowns.  (#3812)

* fuck

* fucwkc

* holy fuck

* i hate this

* FUCK YOUBALTIMORE

* superi

---
## [Stutternov/sojourn-station](https://github.com/Stutternov/sojourn-station)@[f5da3823ac...](https://github.com/Stutternov/sojourn-station/commit/f5da3823ac07f22c72a19e8191a4567882020f7f)
#### Wednesday 2022-08-17 01:04:36 by nikothedude

holy SHIT i hate saycode (hotfix) (#3816)

* whydidthishappen

* fuck

---
## [clojure-lsp/clojure-lsp](https://github.com/clojure-lsp/clojure-lsp)@[e476baa3ff...](https://github.com/clojure-lsp/clojure-lsp/commit/e476baa3fff1eebbf02b8cb0520ed8afc54e6ab7)
#### Wednesday 2022-08-17 01:27:25 by Jacob Maine

Fix: publishing diagnostics at startup fills up the channel

At startup clojure-lsp analyzes project files with clj-kondo. clj-kondo
finds diagnostics (a.k.a. lint) and clojure-lsp sends those diagnostics
to the editor by spooling them onto a core.async channel called
`db/diagnostics-chan`. As described in #1153, in very large projects
(thousands of namespaces) this can lead to an exception "Assert failed:
No more than 1024 pending puts are allowed on a single channel." When
this happens the editor doesn't receive all the diagnostics.

To explain, let me tell a story.

Sometimes I find myself standing in line at the grocery store alone,
waiting while my wife looks for "one more thing." This is a useful model
for reasoning about core.async.

At the core.async grocery store, shoppers wander around picking out
items and putting them in their cart. They wheel their carts to the
checkout area, and here's where things get weird. At this store, you
aren't allowed to put an item on a conveyor (`chan`) yourself. Instead
each conveyor has an attendant. You hand an item to the attendant, who
puts it on the conveyor for you. There isn't even a line. Many people
can hand items to the attendant all at once.

Usually the cashier is quick and keeps the conveyor empty, so the
attendant can place each new item immediately. But sometimes the cashier
gets behind. If things back up, the attendant has a basket of their own.
They'll keep taking the shopper's items, storing them in their own
basket until the cashier catches up.

The attendant has space for 1024 items in their basket. Any more than
that, and as you hand an item over, poof! it disappears (`No more than
1024 pending puts are allowed on a single channel`).

As a shopper you have three options as you hand an item to the
attendant.

If you don't care whether your item makes it onto the conveyor, you can
hand it over and walk away (`put!`), getting back to shopping.

Even if you're the only person in the store, this can cause problems. If
you revisit checkout many times in a row, walking away each time, you
can accidentally fill up the basket.

To try to avoid this problem, you can wait until you see the attendant
put the item on the conveyor (`>!!`) before returning to your shopping.
This still doesn't guarantee the attendant's basket won't fill up. If
there are other shoppers, they could all come to checkout at the same
time. But at least you know you won't cause a problem by yourself.

Some shoppers feel like waiting is a waste of their time so the store
has arranged a third option.

With a little ceremony (`go`) you can _hire someone else_ to wait with
your cart. The hiring process takes a moment to set up (HR benefit
forms) but is usually quite fast, so shoppers love this option. The new
worker will hand the items in the cart to the attendant one at a time,
waiting to see each one reach the conveyor `>!`. If the cart has only
one item (`go` and a single `>!`) this [isn't much
different](https://github.com/clojure/core.async/wiki/Go-Block-Best-Practices#general-advice)
than walking away (`put!`). But if the cart has several items, the new
worker will wait for each one to reach the conveyor before giving the
attendant another (`go-loop` and `>!`, or more simply `onto-chan!`).
This lets you continue your shopping, with more confidence that your
items won't overwhelm the attendant.

Coming back to this bug...

Suppose your project has 1200 files. At startup, clojure-lsp calls
`sync-publish-diagnostics!` in a loop, once for each file. Each one of
these invokes `(put! diagnostics-chan diagnostic)`. This is like making
1200 trips to checkout, walking away after handing over a single item
each time. The attendant ends up with too many items and poof! some of
them disappear. You might think you could fix this by calling `(go (>!
diagnostics-chan diagnostic))` in a loop instead, and indeed, there are
places where we were doing that. But this won't work either. It's like
hiring 1200 new workers, each with one item in their cart. The new
workers wouldn't coordinate with each other. They'd each hand their
single item over, the attendant would get 1200 items all at once, and
again, poof!

When looked at this way, there a few possible fixes. You could make the
conveyor longer (i.e., `(chan 1000)`), effectively giving the attendant
some extra space in addition to their basket. But I think it's better to
hire only one worker, with 1200 items in their cart. They can hand items
to the attendant one at a time, waiting for each one to reach the
conveyor before handing over another. The attendant's basket is much
less likely to fill up this way. (It's still possible of course—there
are other shoppers in the store.)

This commit changes the code so that whenever we have several file's
worth of diagnostics, we add them to the diagnostics channel with
`onto-chan!`. That is, we hire one worker with a very full cart, instead
of walking away after each item or hiring thousands of workers each with
single-item carts.

That's the main fix.

This commit also removes the test-specific pathways through the
diagnostics code. These pathways were put into place to avoid test
flakiness. That was working—the tests haven't been flaky lately—but not
for the reason we thought. To understand what I mean and why I don't
think the test-specific pathways are necessary, let's start with some
very old code, before any flakiness fixes were in place.

```clojure
;; flaky
(defn maybe-publish [{:keys [publish?]} diagnostic]
  (when publish?
    (go (>! db/diagnostics-chan diagnostic))))

(deftest diagnostics-should-not-always-be-published
  (maybe-publish {:publish? true} diagnostic)
  (let [mock-chan (chan 1)]
    (alter-var-root #'db/diagnostics-chan mock-chan)
    (maybe-publish {:publish? false} diagnostic)
    (is (= :timeout (h/take-or-timeout mock-chan 200 :timeout)))))
```

These tests were flaky. The final line would fail occasionally, because
a message _was_ put on the mock-chan. That meant that sometimes `>!`
from the first line of the test didn't actually run until _after_ the
mock-chan was installed with `alter-var-root`.

The original fix for the flakiness looked like this:

```clojure
;; not flaky
(defn maybe-publish [{:keys [publish? env]} diagnostic]
  (when publish?
    (if (= :test env)
      (put! db/diagnostics-chan diagnostic)
      (go (>! db/diagnostics-chan diagnostic)))))

(deftest diagnostics-should-not-always-be-published
  (maybe-publish {:publish? true, :env :test} diagnostic)
  (let [mock-chan (chan 1)]
    (alter-var-root #'db/diagnostics-chan mock-chan)
    (maybe-publish {:publish? false, :env :test} diagnostic)
    (is (= :timeout (h/take-or-timeout mock-chan 200 :timeout)))))
```

This worked—these tests weren't flaky. That seemed to prove that `put!`
was somehow "less asynchronous".

But wait! Earlier I pointed out that the Clojure docs say `go` + `>!`
isn't much different than `put!`. And I'll go further and link to the
[docs](https://clojuredocs.org/clojure.core.async/put!) that say `put!`
"Asynchronously puts a val into port." So how did using a different but
equivalent thing which is also asynchronous fix flakiness caused by
asynchronicity?

Let's go back to the grocery store. Remember what I said about hiring a
new worker and how it takes a moment? What I meant is that the body of a
`go` block is executed asynchronously. And this is the key.

When you write `(go (>! db/diagnostics-chan diagnostic))` then you are
_picking which channel_ to put the message on asynchronously. Since the
choice is asynchronous, you could pick before or after `alter-var-root`.
If it's before, you pick the original channel, and the tests will pass.
But if it's after, you pick the mock-chan, and the tests will fail.

While the new worker is filling out their HR forms (`go`), the
attendant, conveyor and cashier are being replaced with temporary
versions (`alter-var-root`). If the worker fills out their forms fast
enough, then they put (`>!`) the item on the original conveyor. But if
they're too slow, they put the item, incorrectly, on the temporary
conveyor.

The **real** fix is to pick the channel before you start any
asynchronous task. That's why using `(put! db/diagnostics-chan
diagnostic)` fixed the flakiness. That code picks the channel, _then_
runs the async code in `put!`. Indeed, it's possible to avoid the
flakiness, while still using `go` + `>!`, by making a very small change
to the original flaky code:

```clojure
;; not flaky
(defn maybe-publish [{:keys [publish?]} diagnostic]
  (when publish?
    (let [ch db/diagnostics-chan] ;; pick channel before running async code
      (go (>! ch diagnostic)))))
```

Either style (picking the channel before running `go`, or using `put!`)
fix the flaky code. And despite what we originally thought, they are
both equally asynchronous. And `put!` is shorter. So as far as I can
see, there's no reason not to use `put!` in production and in tests, so
that's what I've switched it to.

Finally, the fact that we thought `put!` was "less asynchronous" is why
pathways that used `put!` were named "sync", and pathways that used `go`
+ `>!` were named "async". That terminology is misleading, so I've
removed it.

As a final note, there's an even deeper problem still, which is that
db/diagnostics-chan is a global variable. If instead of holding the
channels in global vars, we threaded them through the app (as components
perhaps, as we do with `db*` as of recently), it would be much easier
and safer to provide a mock-chan in tests. That's another refactoring,
for a later time.

Fixes #1153, I hope.

---
## [TheBoondock/tgstation](https://github.com/TheBoondock/tgstation)@[4ca2a57ae7...](https://github.com/TheBoondock/tgstation/commit/4ca2a57ae7535433d20adfd1d4804769f3b109cd)
#### Wednesday 2022-08-17 02:01:05 by Justice

Adds the Mothroach (#68763)


About The Pull Request

Yup. That's pretty much it. This PR adds the Mothroach to the game, described as "An ancient ancestor of the moth that surprisingly looks like the crossbreed of a moth and a cockroach."

Do you love the Mothroach? Then you can cuddle with it and pat it, as well as place it on your head for extra cuteness.
What if you hate it, though? You can always kill and butcher Mothroaches in order to mass produce moth plushes for your own profit... How fun!

Either way, you win!

The Mothroach can be picked up and has a special on-head sprite (which looks really cute). It is able to vent-crawl and you may get one by randomly summoning a friendly mob through the gold slime extracts, or by ordering one through the Cargo Requests. After butchered, you may use its hide, a heart, and some cloth to craft a moth plushie, the most devilish of Devil's designs.

Full Preview of all the Sprites (NEW): https://www.youtube.com/watch?v=pdg8FTNEYjI
Preview of some of the Sprites (OLD): https://www.youtube.com/watch?v=9A-8hGCiW0s
In-hand, on-head, and grounded Mothroach sprite credits go to ValuedEmployee.
I did the Mothroach hide sprite though!
Why It's Good For The Game

The Mothroach is incredibly cute and a neat, fresh, new piece of content. Although it could use some future repurposing, right now it's simply a cute exotic pet with a few interactions.

These cute sprites are just too good to go to waste...

I keep seeing people complain about the lack of new content. Well, here's something niche that won't break the whole balance of the game and that will be cute. I seriously cannot see a motive not to add this to the game. Just because it isn't a powergaming tool or something that is seen every shift, that doesn't mean that it won't have a positive influence on the game. As I have stated, right now the Mothroaches are underperforming in terms of interactions and ways of getting them, but adding them is the first step to later improve them.
Changelog

cl
add: The Mothroach, your new local exotic pet
add: Mothroach Hide and Mothroach Meat
add: New crafting recipe for the Moth Plush: 1 Mothroach Hide; 1 heart; 3 cloth
fix: Fixes dead mobs on-head not having sprites
/cl

---
## [TheBoondock/tgstation](https://github.com/TheBoondock/tgstation)@[b4f19a7e0f...](https://github.com/TheBoondock/tgstation/commit/b4f19a7e0fc3802856ec4117eb71418287c51ac6)
#### Wednesday 2022-08-17 02:01:05 by John Willard

Greatly increases Pun Pun's abilities and strengths (using desk bells, cross stun immunity) (#68870)


About The Pull Request

Pun Pun has a new AI, with it they received the following:

    Instead of screeching/roaring/scratching/jumping/rolling, Pun Pun will instead sing/dance/bow/clear throat/sign.
    Pun Pun now rings desk bells instead of finding random shit to pick up, and doesn't intentionally seek out weapons.
    Pun Pun has a higher chance of giving people stuff in their hand, so the Bartender can give them a drink and let them go walking around.

Additionally:

    Pun Pun is now immune to being hardstunned by walking into them, giving them a little more bite for greytiders beating them up.
    Monkeys can now use desk bells.

Why It's Good For The Game

I like Pun Pun and when Monkey AIs were originally added, there was a note about giving them a unique AI. Since we're slowly turning the poor monkey into an actual Bartender assistant, I find it thematic that they would ring the bell and give out drinks in their hand, as if the Bartender taught them themselves.

For the hardstun immunity, I mostly did it because I find it annoying for a Bartender to have to carefully navigate around Pun Pun to not knock them over and make them drop an instrument (or anything else) in their hand, but it also works as a buff to people trying to kill them. Pun pun is a unique monkey so I don't believe they should be as easy to kill as any other.

Desk bell addition was necessary for Pun Pun to use it.
Changelog

cl
add: Pun Pun now gives stuff in their hand frequently and rings desk bells.
add: Pun Pun now has gentleman-like emotes, rather than screeching and roaring.
balance: Pun Pun no longer looks for weapons in their off time.
balance: Pun Pun is no longer vulnerable to stuns by being walked into.
qol: Monkeys can now use desk bells.
/cl

---
## [PdxCodeGuild/class_orchid](https://github.com/PdxCodeGuild/class_orchid)@[e175f38e2e...](https://github.com/PdxCodeGuild/class_orchid/commit/e175f38e2e6fc0252449ca3f215008813638ef70)
#### Wednesday 2022-08-17 03:59:22 by Jordyn

Jordyn/python/lab16 (#195)

* first commit

* Lab12: Ugly mess that only works if you follow the rules... mostly

* Accidently overwrote my CSV with lowercase versions of information when it opporates on .Title() formats, also missing break lines

* Lab16 Dad Jokes UGH

* haha problems!

Co-authored-by: JordynHolder <Jordyn.W.Holder@gmail.com>

---
## [csesoc/Circles](https://github.com/csesoc/Circles)@[3d16d1bb2a...](https://github.com/csesoc/Circles/commit/3d16d1bb2ab36648ddb4fe3e5edfa15c369fc949)
#### Wednesday 2022-08-17 05:03:49 by Peedee2002

chore(frontend): remove framer motion and moment (#675)

* split up all the stuff

* oops forgot to update my PR

* removed moment and framer-motion

* changed yearstep too

* fixed wierd shit

* fix suspense ugliness

* fix suspense ugliness

---
## [srsbsns5/GAN-GDDS1](https://github.com/srsbsns5/GAN-GDDS1)@[349a4ce3f2...](https://github.com/srsbsns5/GAN-GDDS1/commit/349a4ce3f2d7e8cadcbe3562c560e5213d488d77)
#### Wednesday 2022-08-17 05:37:54 by srsbsns5

doors

Signs of love overshadows my dreams
Baby, don’t worry coz you ain’t alone
Only time running days without nights
Tears pass through

He said, "I’m the one who’s got to leave"
I said, "Nobody’s really got to leave coz"
"I don’t hear enough explanation"
"All I need is admiration"
Big frustration bro he goes
"Life is short we gave a shot
But didn’t work honey coz we had
A whole lot going on and on
And on..."

---
## [EY3G0R3/dwm](https://github.com/EY3G0R3/dwm)@[67d76bdc68...](https://github.com/EY3G0R3/dwm/commit/67d76bdc68102df976177de351f65329d8683064)
#### Wednesday 2022-08-17 07:27:28 by Chris Down

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
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[7e44fe73b1...](https://github.com/mrakgr/The-Spiral-Language/commit/7e44fe73b1115d2b7572555d68bad79214cddf44)
#### Wednesday 2022-08-17 08:23:13 by Marko Grdinić

"9:10am. I actually woke up a lot earlier than this and just lounged in bed. But I slept well during the night. Let me check my mail. Did the RR submission get a pass yet? Not yet. Neither did I get anything else.

Time for Kaiji and Fabiniku.

9:25am. I do not really feel like it today, I'd rather just stay in bed. It really is difficult to write. It easy to go forward through hardship when you have a grand goal, but writing. The benefits are uncertain so it feels like I am writing my last work. The great irony of this whole situation is that once I get Stable Diffusion, I will actually be closer to making use of AI than ever before. Getting a system like this, is possibly the most ideal thing that could happen to me.

Just what the hell is OpenAI doing? Just why am I still on the waiting list? Those people are so arrogant. When they said that GPT was too dangerous to release I really thought that deep learning had jumped the shark and it was all downhill from there.

9:30am. At this point, I really can't help but wonder if there are more people in the world like me - good at programming, but do not feel like doing it.

I wonder if there will be some online service that will let me make use of Stable Diffusion really cheaply, or if I am going to have to set up my own on the cloud? Remember Deep Dream generator? I think the pro version cost 100$ a month, but with my current knowledge, I could set up my own much cheaper system on AWS.

...Arguably not yet. I haven't actually tried out how instances work yet, but once I figure that out, yes, it would be easy. And it would cost much less than that per month.

I hope I get a reason to do something like that with Stable Diffusion. Now that I've been kicked out, I do actually want to do some programming.

9:35am. Anyway, I've done some thinking about how the plot should go from here, and it is really difficult to thread the scenes together. If you have character and the background in mind, that is something. You can just use that as the foundation for the plot. You setup the basics and run the story forward in your mind.

But specific scenes...

It is troublesome.

In 2014, I didn't really care about the background, the character or even the scenes too much. It is like I was high on whatever my brain was producing naturally at that time.

Fundamentally, even now I haven't changed too much, but I am not high, but low instead. So I am getting some inspiration from the setting itself rather than the process of self improvement.

9:40am. Now that I've come this far, I can see my own skill at writing a bit more clearly.

I am not 4/5, that is for sure.

Right now, I am wondering whether to not focus on the particular scenes too much. I haven't decided it, but rationaly, I can absolutely see that the question is yes - I should ditch the fragmented scenes and just run the setting itself forward in my mind. I'll make a breakthrough as a writer once I do that.

I think I am somewhere in the 3/5 range as a fiction writer.

I have the ability to come up with a setting and run it forward, and I have the discipline to maintain the productive flow. The first is a sign of talent and the other is the mark of a pro. These two are the most essential features. I have unique settings in mind, so that is a big benefit as well.

You do need novelty to stand out, this is probably the hardest part for any aspiring artist, and I actually have it. They say genius is hitting a target nobody else can even see.

10:10am. Ok, let me go back to bed. I do not feel like doing anything right now. I should just wax it in my mind until I get over my depression.

I need to establish the basic process. I have the fragments of what I need in my mind, but my writing process is hardly refined like my programming one. Writing should be easier that programming once I get it going.

10:15am. I should take some time to specifically think about just using the method of setting up the world and simulating it.

Right now I am still attached to the fragment scenes that I won't be able to fit. But if I wanted to, coming up with new scenes would not be difficult.

In fact, what I've wrote so far is 99% new scenes, so that is a sign that I should not be so attached to what I have.

In programming you are very restricted and have to be careful. But in writing, I have a lot more leeway. Rather than a battle that programming is, writing should be more like a vacation.

I think in the first 4 chapters I've shown my grit, but what I want to do is reach out and step out of the mud.

I am so depressed over my lack of success, but done right, writing could be the easiest thing ever and has strong synergy with AI. Yet, it is like I desire hardship. These strong desires got me into this hole, but they are going to get me out as well.

Changing your class in real life is not going to be so easy. I'll need some time to get into the stride.

I know that my attitide is wrong.

I spent so much time optimizing my programming and art workflow. I should spend some time reflecting on my writing workflow instead of just thinking what to write next.

Maybe I still do not understand the fundamentals of writing."

---
## [scrabsha/tremor-runtime](https://github.com/scrabsha/tremor-runtime)@[5e4e816382...](https://github.com/scrabsha/tremor-runtime/commit/5e4e81638224589c29170840bbcc9c9e8fbe8704)
#### Wednesday 2022-08-17 09:07:24 by Sasha Pourcelot

Enforce "no mod.rs files" via clippy lints

Back in spring when I was working on the [ClickHouse sink][1], I had
[an interesting comment][2] stating that Tremor prefers using `mod_name.rs`
files instead of `mod_name/mod.rs` files.

(*In my opinion this is bad, but let's not discuss this here.*)

Once my work got merged, I started wondering if we could statically check this
and make `clippy` emit an error if it sees `mod.rs` files. Turns out there's a
[`mod_module_files`][3] we can `deny`. That's basically what this commit does.

The resulting compilation error is just as friendly as it needs to be:

```none
$ cargo clippy
    Checking tremor-runtime v0.12.4 (/home/ssha/git/tremor/tremor-runtime)
error: `mod.rs` files are not allowed, found `src/should_not_compile/mod.rs`
  --> src/should_not_compile/mod.rs:0:1
   |
   |
note: the lint level is defined here
  --> src/lib.rs:25:5
   |
25 |     clippy::mod_module_files
   |     ^^^^^^^^^^^^^^^^^^^^^^^^
   = help: move `src/should_not_compile/mod.rs` to `src/should_not_compile.rs`
```

I `deny`-ed this on the following crates:
  - `tremor-runtime`,
  - `tremor-api`,
  - `tremo-common`,
  - `tremor-influx`,
  - `tremor-pipeline`,
  - `tremor-script`,
  - `tremor-value`.

Feel free to request the addition of this lint elsewhere. I may have forgotten
some crates :).

It turns out y'all did a great job at maintaining this at each code review, as
I had no compilation error once all the lint were added.

Thank you for your work!

[1]: https://github.com/tremor-rs/tremor-runtime/pull/1538
[2]: https://github.com/tremor-rs/tremor-runtime/pull/1538#discussion_r904836976
[3]: https://rust-lang.github.io/rust-clippy/master/index.html#self_named_module_files

Signed-off-by: Sasha Pourcelot <sasha.pourcelot@protonmail.com>

---
## [matrix-org/mjolnir](https://github.com/matrix-org/mjolnir)@[b9284f0167...](https://github.com/matrix-org/mjolnir/commit/b9284f0167a9e9428db6217ec5ede527649a4948)
#### Wednesday 2022-08-17 10:02:32 by gnuxie

Reduce the throttle test theshold even more.

The implementation is rubbish, as it doesn't avoid the exponential backoff

Remove default rate limit testing.

It doesn't work. No there really isn't more to say about it
you're welcome to dispute it if you're going to do the work investigating. I'm not.

We used to have a test here that tested whether Mjolnir was going to carry out a redact order the default limits in a reasonable time scale.
Now I think that's never going to happen without writing a new algorithm for respecting rate limiting.
Which is not something there is time for.

https://github.com/matrix-org/synapse/pull/13018

Synapse rate limits were broken and very permitting so that's why the current hack worked so well.
Now it is not broken, so our rate limit handling is.

https://github.com/matrix-org/mjolnir/commit/b850e4554c6cbc9456e23ab1a92ede547d044241

Honestly I don't think we can expect anyone to be able to use Mjolnir under default rate limits.

well, it's not quite simple as broken, but it is broken. With the default level in synapse (which is what matrix.org uses) it is struggling to redact 15 messages within 5 minutes. that means 5 messages over the burst count. This is ofc ontop mjolnir sending reactions / responding to replies (which isn't much but... enough to mess with the rate limiter since ofc, Synapse tells requests to wait x amount of time before trying again, but that doesn't help for concurrent requests since ofc there's only 1 slot available at that future time.  This means Synapse just wacks everything with exponentially longer shit without many (or any?) events going through
it used to be fine
because rate limiting in synapse used to be a lot more liberal because it was "broken" or something, that's not me saying it's broken that's just what synapse devs say which is probably true.
if all requests went into a queue then yeah you could eliminate one problem
but that's a lot of work and i don't think we should be doing it
cos no one uses mjolnir like this anyways

---
## [igroglaz/srvmgr](https://github.com/igroglaz/srvmgr)@[be3f871406...](https://github.com/igroglaz/srvmgr/commit/be3f871406d59bce034f136ed2853810bb3b3e93)
#### Wednesday 2022-08-17 12:14:39 by WarBeginner

rebuild new parameters

+ adding new parameters for server.cfg [Settings]:
 exp.multiplicators when death (4 - for every kind of death),
 change max limit of char.parameters (4 classes/ war-mage * male-female / * 4 char.parameters /body, reaction, mind, spirit/)
+postbuild\server.cfg0 - example of new params

---
## [heroku/heroku-buildpack-python](https://github.com/heroku/heroku-buildpack-python)@[b2dfe7397b...](https://github.com/heroku/heroku-buildpack-python/commit/b2dfe7397bf2f57b70799954277dd01a9c034432)
#### Wednesday 2022-08-17 13:14:23 by Ed Morley

Update path rewriting to support setuptools v64's PEP660 editable install mode (#1357)

On Heroku, the application source directory exists at a different path at build time (`/tmp/build_<hash>`), than it does at runtime (`/app`). As such, the buildpack has to perform path rewriting via `.profile.d` scripts at runtime, to ensure any packaging related absolute paths in the build output are rewritten to reference the new path. (Thankfully this awful path rewriting will no longer be necessary in the future with CNBs.)

Previously the only files this path rewriting needed to update were the `*.pth` and `*.egg-link` files in `site-packages` created by setuptools when performing editable installs.

However setuptools v64 added support for PEP660 based editable install hooks:
https://setuptools.pypa.io/en/latest/history.html#v64-0-0
https://peps.python.org/pep-0660/

This feature is only used for projects that have a `pyproject.toml`, and for such projects, [if the config is deemed complex enough](https://github.com/pypa/setuptools/blob/d03da04e024ad4289342077eef6de40013630a44/setuptools/command/editable_wheel.py#L359-L368), setuptools creates a new [finder script](https://github.com/pypa/setuptools/blob/23d455c532fca91e6f00aa5950000739b058b6e5/setuptools/command/editable_wheel.py#L740-L809) in `site-packages` that dynamically handles package resolution. (Simpler configs get a static `.pth` file, which works fine with our existing path rewriting.)

This new file embeds the absolute path of the source directory at build time, so must be rewritten too. It has a filename of form: `__editable___my_package_0_0_1_finder.py`

As such, this PR adds support for rewriting these files, along with updated test fixtures to provide coverage of `pyproject.toml` based editable installs (alongside the existing `setup.py` based test fixture).

Whilst writing the new test, I encountered a difference in behaviour with setuptool's new editable install mode, which meant the fixtures had to be nested inside a `packages/` directory in order to avoid an `ImportError` due to the fact that the Python buildpack currently sets `PYTHONPATH=/app` at runtime. See:
https://github.com/pypa/setuptools/issues/3535

Note:
- The Python buildpack doesn't yet globally install this newer setuptools v64 release, since by design it pins to a specific version to prevent upstream changes from breaking apps overnight. (The version was recently updated to 63.4.3 in #1344.)
- However, for packages that have a `pyproject.toml` pip uses the approach described in PEP518, which uses an [isolated build environment](https://pip.pypa.io/en/stable/reference/build-system/pyproject-toml/#build-isolation). This environment typically pulls in latest setuptools (though this is controllable by the package owner via `[build-system]` in `pyproject.toml`), overriding our pinned global setuptools install.
- As such, even though we're not using v64 globally, users can still be broken by the upstream release.

A big thanks to @mrcljx for the initial PR in #1355 on which this was based :-)

Closes #1355.
GUS-W-11608693.

Co-authored-by: Marcel Jackwerth <marceljackwerth@gmail.com>

---
## [bhatmand-forks/Mind-Expanding-Books](https://github.com/bhatmand-forks/Mind-Expanding-Books)@[3abe7db364...](https://github.com/bhatmand-forks/Mind-Expanding-Books/commit/3abe7db36476c1962690a3de50145b333ee27cba)
#### Wednesday 2022-08-17 13:44:58 by Maureen Landgraf

Added It by Stephen King

You can't have a list of horror books with Stephen King. 'It' will always be one of my favorite King books. The book effectively uses not only Pennywise as a horror element, but also real life threats such as Henry Bowers and his gang of school bullies and Bev's abusive father. While the book is plenty chilling, you also fall in love with the tight-knit group of misfits who are able to band together and defeat a monster that has existed since the beginning of time itself. The book is not only about monsters, but the power of friendship, which makes it so much more than your typical horror novel.

---
## [mayhemheroes/php-src](https://github.com/mayhemheroes/php-src)@[128768a450...](https://github.com/mayhemheroes/php-src/commit/128768a4503c8bc5c6ccf564061f9dc8b307f57f)
#### Wednesday 2022-08-17 14:23:14 by Alex Dowad

Adjust number of error markers emitted for truncated UTF-8 code units

In 04e59c916f, I amended the UTF-8 conversion code, so that when given
invalid input, it would emit a number of errors markers harmonizing
with the WHATWG's specification of the standard UTF-8 decoding
algorithm. (Which, gentle reader of commit logs, you can find online
at https://encoding.spec.whatwg.org/#utf-8-decoder.) However, the code
in 04e59c916f was faulty in the case that a truncated UTF-8 code unit
starts with 0xF1.

Then, in dc1ba61d09, when making a small refactoring to a different
part of the UTF-8 conversion code, I inexplicably broke part of the
working code, causing the same fault which was already present with
truncated UTF-8 code units starting with 0xF1 to also occur with
0xF2 and 0xF3 as well. I don't remember what inane thoughts I was
thinking when I pulled off this feat of utter mental confusion.

None of these cases were covered by unit tests, by the way.

Thankfully, my trusty fuzzer picked up on this when testing the
new implementation of mb_parse_str (since the legacy UTF-8
conversion filter did not suffer from the same problem, and I was
fuzzing to find any differences in behavior between the old and
new implementations).

Fortuitously, the fuzzer also picked up another issue which was
present in 04e59c916f. I was emitting only one error marker for
truncated code units starting with 0xE0 or 0xED, in cases where
the WHATWG standard indicates two should be emitted. Examples
are 0xE0 0x9F <END OF STRING> or 0xED 0xA0 <END OF STRING>.

Code units starting with 0xE0-0xED should have 3 bytes. If the
first byte is 0xE0, the second MUST be 0xA0 or greater. (Otherwise,
the codepoint could have fit in a two-byte code unit.) And if the
first byte is 0xED, the second MUST be 0x9F or less. According to
the WHATWG algorithm, step 4, if the second byte is outside the
legal range, then the decoder should emit an error... AND
reprocess the out-of-range byte. The reprocessing will then
cause another error. That's why the decoder should indicate two
errors and not one.

---
## [AleXsjsju/AleXsjsju](https://github.com/AleXsjsju/AleXsjsju)@[fc189b285f...](https://github.com/AleXsjsju/AleXsjsju/commit/fc189b285f1b6ec2de320269dc0dcc8a5df20d0d)
#### Wednesday 2022-08-17 15:30:23 by AleXsjsju

Update EZ HUB (Top)

Note that this project is completely free and I make no money out of this. I am hoping this is a good contribution to the exploiting community.

To see what information Ez Hub logs please refer to the following link:
https://pastebin.com/Wf9LKAMX

Everything in Ez Hub is open source except the logger as it logs information for a better user experience. You can disable the logger by enabling _G.DISABLEEXELOG. This is so that users that don't want to share their information can do so easily.

To view, the source of our exclusives and main panel (ESP, Aimbot, etc) refer to the following link: https://github.com/debug420/Ez-Hub/tree/master/
Please use this as an educational resource.

V3rm Thread: https://v3rmillion.net/showthread.php?tid=1087188
Discord: https://discord.gg/Zgau6767u8

Feature List:
Exclusives V2:
Tiny Tanks
Bitcoin Miner
Tower of Hell
Prison Life
Phantom Forces
Universal
Bubble Gum Simulator
Legends Of Speed
Arsenal
Redwood Prison
Saber Sim
Murder Mistery 2

Exclusives V1:
Prison Life
Redwood Prison
Arsenal
Graphics Editor
Universal
Wildwest
Vehicle Simulator


Reposted Scripts:
A Bizzare Day GUI
A Universal Time (New)
Adopt Me GUI
Adventurer Simulator (New)
Animal Sim GUI
Anime Fighting Simulator
Arsenal (New)
Arsenal GUI
Arsenal Kill All
Assassin (New)
Attack on Titan: Downfall (New)
Banana Eats GUI
Bee Swarm Simulator
Big Paintball (Unlock All) (New)
Blade Throwing Simulator (New)
Blood Samurai 2 (New)
Blood Samurai 2 (New)
Blox Hunt (New)
Blox Hunt GUI
Boku No Roblox
Boxing Simulator (New)
Broken Bones IV (New)
Build A Boat For Treasure (New)
Build A Boat For Treasure GUI
Car Crushers 2 GUI
Clicker Madness
Clicking Champion GUI
Coin Hero Sim (New)
Counter Blox
CounterBlox GUI
Counterblox (New)
Destruction Sim (New)
Destruction Simulator (New)
Dig it GUI
Doomspire Brick Battle (New)
Dragon Adventures GUI
Dragon Ball Rage (2) (New)
Dragon Ball Ultimate GUI
Dragon Ball Z Final Stand
Dragon Ball Z Final Stand (New)
Dragon Ball rage remastered
Dungeon Quest GUI
Fart Simulator (New)
Fishing Simulator
Flee The Facility GUI
Flood Escape 2 GUI
Fortress Tycoon GUI
Giant Survival GUI
Gods of Glory (New)
Guest Infection (New)
Hero's Legacy (New)
Ice Breaker GUI
Imposter GUI
Islands (New)
Jailbreak (Jailed Hax) (New)
Jailbreak (Vynixius) (New)
Jailbreak Auto Farm
Jailbreak GUI
KAT GUI
Kick Off GUI
Legends of Speed GUI
Lift Legends GUI
Lifting Simulator (New)
Loomian Legacy (New)
Lucky Blocks Battleground
Lumber Tycoon 2 GUI
Milkshake Legends GUI
Mining Champions (New)
Murder Mystery 2 (New)
Murder Mystery 2 GUI
Ninja Legends (AutoFarm) (New)
Ninja Legends 2 (New*2)
Ninja Tycoon (New)
One Piece Prime GUI
One Punch Man GUI
One Punch Man GUI 2
Online Business Sim
Pet Simulator GUI
Pistol 1v1 (New)
Prison Life (New)
Prison Life GUI
Prison Life Sound Spam
Punching Sim GUI
Ragdoll Engine (Vynixius)
Recoil GUI
Redwood Prison GUI
Ro Ghoul GUI
Robeats (New)
Rumble Quest (AutoFarm) (New)
Rumble Quest GUI
SCP 3008 (New)
Science Simulator (New)
Shark Evoloution GUI
SharkBite GUI
Shinobi Life 2 GUI
Skywars GUI
Slime Tycoon GUI
SlipBox GUI
Smash Legends (New)
Snake GUI Game
Super Doomspire (New)
Super Saiyan Sim (New)
SuperPower Training Sim
Tapping Mania
Tapping Mania (New)
Tapping Mania GUI
The Dropper GUI
The Impossible Obby (New)
The Wild West (New)
Timer GUI
Tiny Tanks (New)
Tower of Hell GUI
Treasure Quest (New)
Vehicule Simulator (New)
Wild West GUI
World Zero GUI
World of Magic (New)
Zombie Attack GUI
Zombie Defense GUI
Zombie Rush (Vynixius)
Zombie Rush GUI

Reposted Script (hubs and other):
A.I Hub (New)
Albino Hub (New)
Animation GUI
Assasin Silent Aim (New)
Auratus X
Bruh Hub (New)
CMD X
Chat System Messages
Coco Hub
Cords Finder
DirectX ESP
Exploiter Hub
FE Animation GUI
FE Hub
FE Trolling GUI
GX SHub
Garfield Hub (New)
Impulse Hub
Infinite Jump
Infinite Yield
Invisible Fling
JayHub (New)
Ori Hub (New)
Owl Hub
PentaHub
Polar Hub (New)
RageFlake Hub
Remote Spy
Reviz Admin
Shaltix's Hub
ShuShiScript Hub
Universal Aimbot
Unnamed ESP
Walk on Walls
EzHub

---
## [DanDucky/ComputerSimulator](https://github.com/DanDucky/ComputerSimulator)@[25f14c88c0...](https://github.com/DanDucky/ComputerSimulator/commit/25f14c88c023cfb982e86237a0b21bff60f9da57)
#### Wednesday 2022-08-17 16:02:56 by DanDucky

8/16/22

+ Massive layout file for future application layout
+ more angry comments 3:<
+ fixed absolutely idiotic code from last night
+ Learned about printf some more (still don't like it)
:sparkles: REALIZATIONS :sparkles:
+ realized that 200 is bigger than I thought when it comes to the read only storage
+ realized that I should really flush out all CACH positions before continuing
+ realized that the storage driver will need access to a ton of read only storage AS WELL AS memory and cache and be able to transfer those between eachother which will be EXTREMELY fun ;3
+ once again confirmed to myself that this will need to be ordered as a pcb

---
## [valeriy42/ml-cpp](https://github.com/valeriy42/ml-cpp)@[4bc55b3d04...](https://github.com/valeriy42/ml-cpp/commit/4bc55b3d04ebf5f2341ad75106e67ec3a7a3d3d9)
#### Wednesday 2022-08-17 16:08:44 by Tom Veasey

[ML] Logging enhancements plus compilation speed ups  (#2363)

Currently, logging requires one to manage wrapping up calls to many types in core::CContainerPrinter::print.
It would be nice if the logging experience was more streamlined. Another side effect is we ended up including
core/CContainerPrinter.h very widely, in many cases for LOG_TRACE statements which are compiled away
anyway. It would be nice to avoid this.

This PR introduces a pseudo stream manipulator CScopePrintContainers. This is dropped into our logging
macros so that all log lines simply get containers printed automatically. This approach first detects (at compile
time) whether types can be written directly to a std::ostream and uses this approach in preference. I also fixed
some obvious silly inefficiencies in CContainerPrinter. One might ask why not just specialise operator<< for
std::ostream and containers in the std namespace? I did in fact try this, but it turns out other libraries tend
to do this and you can easily get ODR violations. I hit this exact problem because libtorch does this and I
couldn't then compile pytorch_inference.

Separately, our compile times given the total LOC are rather long. One culprit is logging. Just including
CLogger.h adds around 70k lines to the output of the preprocessor and, for my setup, 0.4s for this step
alone to the compile time of file. Therefore, I've also started addressing some of the bottlenecks. I've migrated
LOG_TRACE to really discard the code altogether. This means we can have a special CLoggerTrace.h which
only optionally includes CLogger.h if we're not compiling with EXCLUDE_TRACE_LOGGING. (I think the
improved build times warrant only finding out later if we break a log line and anyway many things now just
print automatically, so this should be harder to do.) I also add CMemoryFwd.h to avoid including CMemory.h
too widely. This includes a lot of STL headers. Finally, I migrated CLoggerThrottler to a pimpl and moved
some obvious other details out of headers. The upshot for for my dev setup is 15% speed up to build everything.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[5aaeb8462c...](https://github.com/mrakgr/The-Spiral-Language/commit/5aaeb8462cc0a68dd443d2fcf90f505d2334d392)
#### Wednesday 2022-08-17 16:11:43 by Marko Grdinić

"5:40pm. I was in bed this whole time, thinking. I am stressed out, but not so much depressed anymore. Brainstorming sessions like these are always effective at building up motivation.

I think I was wrong about programming. I bought into the Singularity pursuit and thought it would give me great insights about the mind itself. If it allowed me to program actual AIs, even weak ones, programming would be a S tier skill. I really thought that given its importance, that programming would be one to benefit from the AI wave the most, but it does not seem like it will be like that. It certainly hasn't been like that. It is a lot weaker than I expected it would be. It is ideal if you have no imagination and the desire to wage slave, but it is literal poison to me. Right now it is literally asking me to spread my ass cheeks and beg to be mounted.

I keep looking for a sign, and I got one. The skill that I thought was useless, writing, is the one which got a huge benefit, and which seems like will get a lot of benefits in the future. Though I no longer believe in the Singularity, the AI wave is not over and interesting stuff will come out of it.

For programming to mature like I imagine it would, I need that memristor breakthrough, and it feels like searching for a miracle at this point. If AI research requires months of training on a supercluster, just what the hell am I even trying to do on my single GTX 970? All my effort would amount to is a drop in the ocean.

I should write.

I felt from the start that the one to cause the Singularity should have the right philosophy. Since I was the only one who had anything remotely close to it, I didn't feel much threat from other ML researchers. But that does not mean anybody is going to win this race. Right now it is looking bad.

Programming is such a disappointment. The insights the past 7.5 years gave me about the mind are really lukewarm negatives at best. And I can't use it to make money unless I am absolutely determined to step on that path. It is useless to me. Maybe it will be useful for setting up my own Stable Diffusion model on the cloud, but I certainly did not go to such an extreme length to master programming just for that.

I didn't want to become a ML researcher or a programmer.

What I wanted to do is do my own thing and have AI augment my efforts. I didn't mean to end up fighting the wave like this.

If I become a writer now, Heaven's Key will become first of a new breed of visual novels, illustrated entirely by AI. That is something to look forward to.

5:55pm. The main thing I lack now is pride. Money, money, money...I expected to make that, but it was never the goal with programming.

If it is writing, I should at least aim to master the writen word. If it is writing, I should aim to perfect my philosophy so I can teach it to my agents. Because, it doesn't seem my programming skills are what is going to give me an edge in this race. I should hate everything, but writing.

I've been looking down on writing, but just what can the writen word do? Rather than seeing myself as a weakling in this domain, I should really push it all the way. If I was the best writer in the world, just what would be my options?

Just what does it mean to be the best at writing?

I had this pride to put everything on the line for programming. So why not art? Visuals got solved by accident, but I should take this luck.

6pm. Whatever is my obsession, should be my focus. If I stop here and abandon my path completely, only tragedy awaits me. I might be forgiven for losing, but not for stoping.

I should aim to be the best in my particular niche of storytelling. Forget money. Anybody can become rich by working a regular job and saving on the side. I was never meant to take such a path. My life was always meant to be one of extremes.

6:05pm. Let me close here. I'll try writing tomorrow. I'll focus on just running the setting forward rather than doing anything particularly complicated. That way of doing things will allow me to just put out text and gain interest without straining myself with questions.

Graphics I could barely get a grip on, but writing should not take me too long to refine.

If I can't get going tomorrow and am again beset by doubts, I will spend that time in bed like today. Hopefully that will allow me to build some backbone. I'll keep doing that until it is time to resume. It is too early to get cocky. I only have 4 chapters out. A 100 more, and I will be able to consider myself something."

---
## [scogafoss/PhD-coding](https://github.com/scogafoss/PhD-coding)@[088d2fedd1...](https://github.com/scogafoss/PhD-coding/commit/088d2fedd1269e0eadad4e4a97426e663854958c)
#### Wednesday 2022-08-17 16:30:46 by scogafoss

fuck you fuck uyou fcuk you fuck uyou fuck uou fuck you

---
## [scogafoss/PhD-coding](https://github.com/scogafoss/PhD-coding)@[7408193a2c...](https://github.com/scogafoss/PhD-coding/commit/7408193a2c86ce1b3542df313910992d5051a796)
#### Wednesday 2022-08-17 16:39:00 by scogafoss

fuck you fuck you fuck yuouuudghuisdhguidhfugiohsafxd098ghdfoiughioudfghioudfxcghoiudfhgopksdfhu9giopsdfhu

---
## [pjsoni/terminal](https://github.com/pjsoni/terminal)@[f2ebb21bd1...](https://github.com/pjsoni/terminal/commit/f2ebb21bd13b20db38305136d34fa0778baf7920)
#### Wednesday 2022-08-17 19:30:15 by Mike Griese

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
## [pjsoni/terminal](https://github.com/pjsoni/terminal)@[442432ea15...](https://github.com/pjsoni/terminal/commit/442432ea15241a3e9ee3d70c5c24e5565655e55b)
#### Wednesday 2022-08-17 19:30:15 by Mike Griese

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
## [Skaytacium/.files](https://github.com/Skaytacium/.files)@[6e599ba34c...](https://github.com/Skaytacium/.files/commit/6e599ba34cde3cd533b67118623fbaad263d1e49)
#### Wednesday 2022-08-17 20:07:46 by Sid

amdgpu more like shit you shit you suck kill yourself please die i hate you radeon rocks

---
## [GNUWeeb/linux](https://github.com/GNUWeeb/linux)@[2f31e36d50...](https://github.com/GNUWeeb/linux/commit/2f31e36d50379d70ee9b3f039d4d50af9a2c8bff)
#### Wednesday 2022-08-17 20:46:16 by Johannes Weiner

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
## [FormidableLabs/victory](https://github.com/FormidableLabs/victory)@[1aaa85fedc...](https://github.com/FormidableLabs/victory/commit/1aaa85fedc133f0f1d0c4e402fda23087a1232d6)
#### Wednesday 2022-08-17 21:15:20 by Ryan Roemer

Infra: Switch monorepo tooling to wireit and pnpm (#2345)

This PR is a big infrastructure overhaul to switch us from lerna + yarn to wireit + pnpm.

## Why?

Our existing setup of yarn + lerna has the following undesirable things:

1. Installs are slow on yarn
2. Yarn1 isn't updated anymore and simple package dependency updates don't work out of the box. It's a huge pain to update anything.
3. Lerna is getting old, and while the NX team has agreed to support it now, our build is (1) slow, (2) not cached at all, and (3) opaque as to what you need to run task-wise to support other tasks.

So, let's welcome PNPM + Wireit!

1. PNPM is a fast installer and well supported for normal things like package upgrades.
2. Wireit allows fine-grained subtask caching and dependency specifications to allow us to: (1) specify dependencies so when you run `pnpm run jest` all the other things that need to happen magically happen, (2) caches sub-tasks so things that don't have changed file inputs don't re-run, and (3) has full GH actions CI support!

To get a sense of how much faster our build has become take a look at the CI times for this branch in https://github.com/FormidableLabs/victory/actions?query=branch%3Ainfra%2Fpnpm-wireit++ -- when no input files change our CI times are about 1 minute. When some things change, a couple minutes. When all things (or our base scripts) change, we take the full hit of a comparable existing Victory CI time of like 15-16 mins.

For the average Victory developer, if you're working in just one package, you can just run the project-level `pnpm run check` and have like a full build and everything work reasonably fast without needing to know more or run subtasks!

## Check it out

```sh
$ npm install -g pnpm
$ pnpm install
# This will be slow!
$ pnpm run check

# ... but the second time will be super fast! And as you change things subsequent runs should be very fast!
$ pnpm run check
```

## Implementation notes

- High level:
    - **Dependency graph architecture**: All of our tasks now use wireit to identify and run/cache dependencies. So, if you want to run jest, you just run `pnpm run jest` and don't need to worry about "what else needs to be built?" before that.
    - **Parallelization**: To best use wireit, we've refactored our tasks to be more package-specific where possible. E.g., we run lint in incremental mode per-package meaning that both Wireit (at package level) and eslint (at file level within package) re-execute on the narrowest unit of "changed files" possible.

- Demos: The demos originally had imports from `victory*/src/index` (source) which wasn't efficient or consistent because the transitive deps on other victory packages was on built files. I refactored these to be normal `victory(-<NAME>)` imports using built files.

- `src`:
    - Since we did a "fresh" install with pnpm, there were some updates in lint packages that meant source or tests needed small tweaks to continue passing/building.
    - Refactor self-references within a package to not use package name.
    - Fixed missing package dependencies uncovered as pnpm-based installs will fail on missing dependencies that are flattened and "accidentally work" in yarn/npm.

- Configs:
    - Webpack `resolve.alias`: Since we no longer hoist victory packages to root, we now add aliases for our webpack configs and storybook (which uses webpack) programatically.
    - Babel, Jest configs: Normalized the naming and location of these across normal and native ones.

- Incremental caching:
    - eslint

---
## [manuelserol/hestiacp](https://github.com/manuelserol/hestiacp)@[365dab5670...](https://github.com/manuelserol/hestiacp/commit/365dab5670f6d1a862858be01638072eeb2ec1db)
#### Wednesday 2022-08-17 21:26:38 by divinity76

Use secure RNG to generate passwords (#2726)

* use secure rng to generate passwords

quoting MDN:
>Math.random() does not provide cryptographically secure random numbers. Do not use them for anything related to security. Use the Web Crypto API instead

My rng is kinda shitty, i know there is some fast way to cut down higher digits to get a digit in range without introducing bias, but i also know that other people have introduced bias by trying to do that on an initially secure rng and getting it wrong (iirc it's discussed here? https://www.youtube.com/watch?v=LDPMpc-ENqY - been years since i saw the talk, but i know Lavavej discussed it in one of his presentations, i think it was that one)  , but anyway this is fast enough, and secure.

* shorter name

* randomString2 / centralize js string generation

* missed 2

---
## [Soro335/WilderWild](https://github.com/Soro335/WilderWild)@[ca445487cb...](https://github.com/Soro335/WilderWild/commit/ca445487cb195414f94779a291a9150bf8b63c56)
#### Wednesday 2022-08-17 22:01:02 by Merp is Me

@AViewFromTheTop read desc please
i know you're not crazy about this idea, but i promise you it'll make the ancient horn feel so much more satisfying to use.
my idea is that it shoots out a few larger rings in the direction it's shot in which quickly fade away. it'll simply act as a "blast" effect. my issue is that i have no idea how to set this up and i really would love if you could help me out. we can even put this on a separate branch just to test it if you're really that unconfident about it.

---
## [SteelT1/Kart-Public](https://github.com/SteelT1/Kart-Public)@[8f354ad9c1...](https://github.com/SteelT1/Kart-Public/commit/8f354ad9c1b3026f7239f0b5184992d802c315eb)
#### Wednesday 2022-08-17 22:17:34 by Eidolon

Implement Uncapped (squashed)

Co-Authored-By: Sally Coolatta <tehrealsalt@gmail.com>
Co-Authored-By: James R <justsomejames2@gmail.com>
Co-Authored-By: Monster Iestyn <iestynjealous@ntlworld.com>
Co-Authored-By: katsy <katmint@live.com>

Place Frame Interpolation in "Experimental" video options header

This seems like an appropriate way to describe the feature for now.

Add smooth level platter under interpolation, `renderdeltatics`

`renderdeltatics` can be used as a standard delta time in any place,
allowing for smooth menus. It will always be equal to `realtics`
when frame interpolation is turned off, producing consistent
framerate behavior everywhere it is used.

Add smooth rendering to save select screen

Add smooth rendering to Record/NiGHTS Attack, F_SkyScroll

Ensure viewsector is accurate to viewx/viewy

This fixes a potential crash in OpenGL when changing between levels.

Ensure + commands get executed before map start

Always have precise_t defined

Fix misc dropshadow issues

Reset view interpolation on level load

Remove unnecessary precipmobj thinker hack

Add reset interpolation state functions

Reset precip interpolation on snap to ceil

Reset mobj interp state on TeleportMove

Only swap view interp state if a tick is run

Run anti-lag chasecam at tic frequency

Fixes jittery and unstable chasecam in high latency netgames

Homogenize mobj interpolations

Add sector plane level interpolations

Add SectorScroll interpolator

Add SideScroll interpolator

Add Polyobj interpolator

Intialize interpolator list at a better time

Delete interpolators associated with thinkers

Interpolate mobj angles and player drawangle

Interpolate HWR_DrawModel

Add functions to handle interpolation

Much less code duplication

P_InitAngle, to fix angle interpolation on spawning objects

Fully fix drop shadows

It used the thing's floorz / ceilingz directly -- that wouldn't account for interpolated coordinates.

Do not speed up underwater/heatwave effect in OpenGL

Closer OpenGL underwater/heatwave effect to Software

Interpolate from time of previous tic

Previously interpolated from last 35th of a second, which
may be offset from game time due to connection lag.

Consider this the proper fix to 54148a0dd0 too.

Calculate FPS stuff even if frame is skipped

I decided ultimately to actually keep the frame skip optimization disabled, because I think it is actually a little bit helpful that you can still get accurate rendering perfstats while paused, however if we decide otherwise then we can have this optimization back without making the game act like it's lagging.

Keep rect in memory

Feel better about this than creating one all da time

Lots of FPS stuff

- Disabled VSync, due to the numerous problems it has.
- Instead, added an FPS cap.
- Frame interpolation is now tied to fpscap != 35.
- By default, the FPS cap is set to the monitor's refresh rate.
- Rewrote the FPS counter.

(This also consolidates several more commits ahead of this
fixing various issues. -eid)

Misc changes after Kart cherry-picks

Fix renderdeltatics with new timing data

Update mobj oldstates before all thinkers

Allow FPS cap values

Adjust how FPS cap is checked to improve FPS stability

Fix precip crash from missing vars

Improve the framerate limiter's timing for extreme stable FPS

Handle the sleep at the end of D_SRB2Loop instead of the start

Simplifies logic in the other parts of the loop, and fixes problems with it frequently waiting too long.

Reset mobj interp state on add

Add mobj interpolator on load netgame

Move mobj interpolators to r_fps

Dynamic slope interpolators

I_GetFrameTime to try and improve frame pace

(It doesn't feel that much better though.)

Move I_FinishUpdate to D_SRB2Loop to sync screen updates with FPS cap, use timestamps in I_FrameCapSleep to simplify the code

Fix plane interpolation light level flickering

Fix flickering plane interpolation for OpenGL in the exact same way

Funny OpenGL renderer being at least 50% copy-pasted Software code :)

P_SetOrigin & P_MoveOrigin to replace P_TeleportMove

Convert P_TeleportMove use to origin funcs

Revert "P_InitAngle, to fix angle interpolation on spawning objects"

This reverts commit a80c98bd164a2748cbbfad9027b34601185d93f5.

Waypoint polyobjects interpolate z & children

Add interpolation to more moving plane types

Adds interpolation to the following:
- Crumbling platforms
- Mario blocks
- Floatbob platforms (this one works really strangely due to two thinkers, maybe double-check this one?)

Reset overlays interp states each TryRunTics

Interpolate model interpolation (lol)

Use interp tracer pos for GL linkdraw

Papersprite angle interpolation

Makes the ending signpost smooth

Move intermission emerald bounce to ticker

Bring back shadows on polyobjects

Also optimizes the method used so rings can show their shadows too. Using just the subsector is a tad bit imprecise admittedly but any more precise methods get really laggy.

Fix a bunch of ticking in hu_ drawing functions

Revert "Reset overlays interp states each TryRunTics"

This reverts commit a71a216faa20e8751b3bd0157354e8d748940c92.

Move intro ticking out of the drawer

Adjust 1up monitor icon z offsets

Fixes interpolation issues with 1up monitors.

Delta time choose player menu animations

Add drawerlib deltaTime function

Interpolate afterimages further back

Use old sleep in dedicated mode

Clamp cechotimer to 0

Fixes issues with cechos staying on-screen and glitching out
(NiGHTS items for example).

Revert "Remove unnecessary precipmobj thinker hack"

This reverts commit 0e38208620d19ec2ab690740438ac2fc7862a49e.

Fix frame pacing when game lags behind

The frame timestamp should've been made at the start of the frame, not the end.

Fix I_FrameCapSleep not respecting cpusleep

Jonathan Joestar bruh

Allow dedicated to use precise sleep timing again

Instead of only using one old sleep, just enforce framerate cap to match TICRATE.

Make Lua TeleportMove call MoveOrigin

Reset Metal fume interp state on appear

Add interpdebug

Put interpdebug stuff in perfstats instead

Add timescale cvar

Slow the game down to debug animations / interpolation problems! Speed it up if you need to get somewhere quickly while mapping!

Enable timescale outside of DEVELOP builds

It has NETVAR, so it should be fine -- put an end to useful debugging features excluded in multiplayer!

Force interpolation when timescale != 1.0

Reset old_z in MT_LOCKON think

Fixes interpolation artifacting due to spawn pos.

Fix cutscenes in interp

Fix boss1 laser in interp

Interpolate mobj scale

Precalculate refresh rate

Slower PCs can have issue querying mode over and over. This might kinda suck for windowed mode if you have different refresh rate displays but oh well

Fix interp scaling crashing software

Reset interp scale when Lua sets .scale

Disable angle interp on fresh mobjs

Fix interp scale crash for hires sprites

Interp shadow scales

Copy interp state in P_SpawnMobjFromMobj

Fix multiplayer character select

Don't interpolate mobj state if frac = 1.0

Fix Mario block item placement

Interpolate spritescale/offset x/y

Fix offset copies for SpawnMobjFromMobj

THANKS SAL

Add Lua HUD drawlists

Buffers draw calls between tics to ensure hooks
run at the originally intended rate.

Rename drawerlib deltaTime to getDeltaTime

Make renderisnewtic is false between tics

I know what I'm doing! I swear

Completely refactor timing system

Time is now tracked internally in the game using I_GetPreciseTime
and I_UpdateTime. I_Time now pulls from this internal timer. The
system code no longer needs to keep track of time itself.

This significantly improves frame and tic timing in interp mode,
resulting in a much smoother image with essentially no judder at
any framerate.

Ensure mobj interpolators reset on level load

Ensure view is not interpolated on first frame

Disable sprite offset interpolation (for now)

Refactor timing code even more

System layer is greatly simplified and framecap
logic has been moved internally. I_Sleep now
takes a sleep duration and I_SleepDuration
generically implements a precise sleep with spin
loop.

---
## [jkwok91/website](https://github.com/jkwok91/website)@[be8d3c479f...](https://github.com/jkwok91/website/commit/be8d3c479f01ee6ab88003dc411be07808ebbcc8)
#### Wednesday 2022-08-17 22:54:43 by Kwok

i am home sick rn and i hate it so i decided to modify my website

consequently the changes are stupid lol

---

