## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-08-08](docs/good-messages/2022/2022-08-08.md)


1,971,384 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,971,384 were push events containing 2,967,880 commit messages that amount to 230,987,852 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 32 messages:


## [TheGreatKitsune/CHOMPStation2](https://github.com/TheGreatKitsune/CHOMPStation2)@[4704df506b...](https://github.com/TheGreatKitsune/CHOMPStation2/commit/4704df506bfccd3f4ef9d75a3cf1a4f6f63ca4e3)
#### Monday 2022-08-08 00:41:06 by Victor Zisthus

Massive Broad Scope Changes

NEW STUFF
Added in a custom thermal regulator for the wilderness shelter.

Southern Cross now has a Bluespace Radio!

Added a subspace radio, and allowed it to be made in the autolathe.

ALL MAPS:
Added lighting to dark areas. Did not touch lighting in maintenance areas.

DECK ONE:
Adjusted exterior lattice network.

DECK TWO:
Fixed a bug with Shieldgen.

Moved the Engine SMES powernet sensor off of a pump.

Removed the second freezer air alarm to prevent pressure alarms from going off every shift. (I got my revenge on the laws of thermodynamics with the new custom regulator, don't worry.)

Put a new subspace radio in the bar.

Adjusted exterior lattice network.

DECK THREE:
Removed a duplicate shower curtain in one of the dorm rooms.

SURFACE OUTPOST:
This PR will cause a conflict with #4061 but I am willing to help Enzo with the project as needed~

A friend and boy waits for the miners every shift.

Moved some stuff around at surface S&R per a reported issue. FIXES #4072

Fixed a bug with the hunting lockers and doors. Security should have access to them now.

Fixed a bug with the Hunting Pen shield generators.

CAVES:
Cleared the rock around the outpost, added a new door to allow moving around the exterior.

EXPLO CARRIER:
Put the new Bluespace Radio on the table in the gateway prep room.

WILDERNESS + SKY ISLANDS:
Overhauled the wilderness shelter! It now has a crew quarters room, First Aid, a second floor, and a utility room. It's only powered by a single advanced RTG that's barely able to keep up with power demand when the place is abandoned, so be sure to bring resources from mining and science to get the other RTG's up and running!

---
## [fastmail/Synergy](https://github.com/fastmail/Synergy)@[443d2f70a5...](https://github.com/fastmail/Synergy/commit/443d2f70a575b053437240f7fadd89528a23b0e0)
#### Monday 2022-08-08 01:06:50 by Michael McClimon

Rototron: attempt to fix a Monday time zone bug

Australians report that their morning reports do not contain duty
rotations; we're pretty sure this is because they're sent on Sunday UTC,
when there is no duty assigned. I think we can fix this by always
passing in a time zone to current_officers_for_duty, which will affect
the calendar search we're doing.

I'm not totally sure this will work, because time zones are weird and
the Rototron code is also kinda weird, but I don't think it's likely to
be _worse_.

---
## [nikothedude/sojourn-station](https://github.com/nikothedude/sojourn-station)@[c3c08d0946...](https://github.com/nikothedude/sojourn-station/commit/c3c08d0946fd0ebde1dd9b5cc5ab8781a544487c)
#### Monday 2022-08-08 01:44:06 by nikothedude

Ports moveSS from TG (#3771)

* p

* fucker

* fuckin

* fuckin!!!!

* commit time

* hell yeah

* FUCKING. TG

* groan

* fuvkin

---
## [Reinfy/Pair-Extraordinaire](https://github.com/Reinfy/Pair-Extraordinaire)@[d41762f4c6...](https://github.com/Reinfy/Pair-Extraordinaire/commit/d41762f4c6c1c7300af8d27b713729d00942242b)
#### Monday 2022-08-08 02:37:49 by Reinfy

Rust sadness

This wiki records some of my unpopular opinions.

Since this wiki is expected to be somewhat unorganized, there is no index page. See the sidebar if you want to continue browsing.

I have presented too much Rust fandom in the past.
Time for some hate!

(I still love Rust, but I need an archive for the things I am sad about it)

(Title is inspired by http://phpsadness.com/)

(Some of these are unpopular opinions, quite many people think differently)

## Standard library
### Primitives
#### Primitives are not really primitive
[Why is `bool` not an `enum Bool { False, True }`?](https://github.com/rust-lang/rfcs/issues/348)
[Why is `str` not a `struct Str([u8]);`?](https://github.com/rust-lang/rfcs/issues/2692)

#### Conversion between integers is not explicit
`as` conversions do not explicitly state whether and what is lost.
For example, `u8 as u16` is perfectly fine (expand size),
but `u16 as u8` is a truncation,
`u16 as i16` might overflow,
`u16 as f32` is perfectly fine (lossless),
`u32 as f32` is lossy,
`usize as u32` and `u64 as usize` are lossy depending on the platform...

On the other hand, while we can use `.try_into()` on the numbers,
it is unclear what the impacts are,
and handling the error is more challenging if panic is not desired.
It is difficult to find (if it even exists) the *named* safe conversion method
from the standard library documentation.

To solve this problem, I published the [xias](https://docs.rs/xias) crate,
which exposes a blanket impl on primitive types to facilitate explicitly explained conversions.

### Collections
#### `.len()` and `.is_empty()`
Clippy [recommends](https://rust-lang.github.io/rust-clippy/master/index.html#len_without_is_empty)
that types implementing `.len()` should also implement `.is_empty()`.
This much sounds like `.clone()` and `.clone_from()`, which should use a default trait impl.
Why wasn't `.len()` a trait anyway?

## General syntax
### Operators
#### The `!` operator
```rs
if !matches!(value, Enum::Variant) {
    panic!("Do you think value matches Enum::Variant or not here, \
        if you didn't know Rust?");
}
```

An alternative is to use `condition.not()`, but that requires `use std::ops::Not` everywhere.

What about `condition == false`? [Thanks so much clippy.](https://rust-lang.github.io/rust-clippy/master/index.html#bool_comparison)

#### `.await`
No, don't get me wrong, I think `future.await` is much better than `await future`.
Not a fan of cargo cult.

But `future.await` looks as if it is a field,
especially if the syntax highlighter is not aware of it
(e.g. in outdated syntax highlighting libraries).
Why can't we make it *look like* a postfix macro,
like `future.await!` or `future.await!()`?

### Pattern matching
#### `let` has mixed use in assignment and conditions
If you didn't know Rust, you're probably confused why we use `=` instead of `==` here

```rs
if let Enum::Variant = value {
    // ...
}
```

This is getting even more confusing with the let...else syntax

```rs
let Ok(socket) = Socket::bind(addr) else {
    anyhow::bail!("Cannot bind socket to {addr}");
};
```

Guess what, `expr else { ... }` itself is not a condition. You actually group it as `let pat = expr` `else` `{...}` instead.

#### Ambiguous new bindings
```rs
pub fn validate(input_byte: u8) -> u8 {
    const FORBIDDEN: u8 = 42;
    
    match input_byte {
        FORBIDDEN => panic!("input byte cannot be {FORBIDDEN}"),
        value => return value,
    }
}

fn main() {
    dbg!(validate(41));
    dbg!(validate(42));
}
```

```
[src/main.rs:11] validate(41) = 41
thread 'main' panicked at 'input byte cannot be 42', src/main.rs:5:22
```

`FORBIDDEN` is a constant but `value` is a new binding? how is this even supposed to work?

#### Use of `|` in patterns
```rs
fn convert_bitmask(input: u8) -> Option<bool> {
    match x {
        Some(1 | 2 | 4) => Some(true),
        Some(..8) => Some(false),
        _ => None,
    }
}
```

Didn't learn Rust before? Guess what the above means:

- "returns true if x is 1 or 2 or 4"
- "returns true if x is 7 (1 bitwise-OR 2 bitwise-OR 4)"

#### `_` and `_var` mean different things
You may have noticed that you can suppress the unused variable warning with both `let _ =` and `let _var =`.
Golang prefers the former (the latter doesn't work in Go), but they actually mean different things in Rust.

`_var` is just a normal binding name (local variable name in the case of `let _var =`),
similar to `var`, except it suppresses some warnings about unused identifiers.

`_` is the pattern that matches everything and binds the value to nothing.
Since there is no binding, the value is dropped immediately.

This causes a significant difference when it comes to RAII:

```rs
{
    let _guard = mutex.lock();
    println!("mutex is still locked here");
}
println!("mutex is unlocked here because `_guard` is dropped");
```

```rs
{
    let _ = mutex.lock();
    println!("mutex is already unlocked here because `_` drops immediately");
}
```

Fortunately, this is usually not a problem, because it is rare to acquire an unused RAII object
(although it is still used in some rare occasions).

## Testing
### Difficulty to unit test procedural macros
Procedural macros are typically tested in the form of integration tests,
where the user writes example code to use the procedural macro
and check if it compiles correctly.
However, this means the whole program is tested together,
and breaking any single part would cause all tests to fail.
This is particularly troublesome when errors caused by macro output are hard to debug.

It doesn't make sense to unit test particular functions that generate `TokenStream` output,
because that would imply writing test cases that repeat every token in the generated output,
and modifying or even reformatting (e.g. adding trailing commas) any part of the output
would require updating all unit tests.
We want to unit test the logic to ensure that
each unit contributes what it is expected to contribute,
not to unit test the exact shape of the generated code.

Another option is to have `#[cfg(test)] #[proc_macro*] pub fn` macros that expose the internal functions,
but this suffers from two problems.
Firstly, this involves additional code to parse an additional TokenStream to serve as the input arguments,
and sometimes inapplicable when the macro generates a special, incomplete part of the syntax tree
like match arms, struct fields, trait bounds, other non-item non-statement ASTs,
or a combination of multiple ASTs (e.g. multiple non-exhaustive match arms).
Secondly, this only works when the integration test is located in the same package as the procedural macro.
This is often not the case when the procedural macro references some code in another closely coupled crate,
e.g. `derive@serde_derive::Deserialize` depends on `trait@serde::Deserialize`.
This can be solved by setting a dependent as a dev-dependency,
but such a solution would not be scalable.

### Inflexible panic tests
Unit tests currently allow `#[should_panic]` to assert that a unit test should panic.
`#[should_panic(expected = "substring")]` additionally asserts that the panic message must contain `substring`.
This is not ideal for two reasons.
Firstly, substrings may not be safe as some parts of the panic message remain untested.
Secondly, the panic message is an implementation detail of the panic but not the subject to be tested.
The goal is to test that a certain code panics for a known reason, not to test what it shows to the user.
For example, `panic!("Cannot insert entry into string map because {:?} is not one of String or &'static str", ty)`,
where `ty: std::any::TypeId`, cannot be tested properly,
because we cannot make sure that both `insert entry into the string map`
and `is not one of String or &'static str` appear in the panic message
since `TypeId as fmt::Debug` has inconsistent output
(which is perfectly fine because it should not be relied on).
This also means we cannot test which `TypeId` the panic involves
(although a crate like this should probably attempt to take the `any::type_name` for slightly more consistent output).

Co-authored-by: xqwtxon <xqwtxon@hotmail.com>

---
## [Niwri/utfo-website-test](https://github.com/Niwri/utfo-website-test)@[109937c4b0...](https://github.com/Niwri/utfo-website-test/commit/109937c4b0118f30743720dbd57840fdcce895db)
#### Monday 2022-08-08 02:52:38 by Cole Kim

First off, I hope to God that this isn't a dumpster fire of a git commit (it's my first, so if it is, sorry!).
With that aside, I've included below a concise summary of changes:
Front Page:
	- Looks well on its way so far. SVG looks sharp. Added a bunch of components to improve readability too.
	- Slideshow and HTML5 positioning (using Css) is still left. But. I'm tired, so I wanted to git out while the getting was good (haha, get it?)
CSS and Styling:
	- Z-indexing for layering on Sign-up Page (from 10 to 1) and nav:active (from 1 to 2) => fixed overlay issues
	- Navbar.css : changed width to undef to 100vw for nav:active (extends to edge of screen horizontally)
	- Fixed navbar overflow by setting body{overflow:hidden} in App.css. Could potentially introduce some styling headaches down the line, but it is fixed
CSS and Styling issues/TODO:
	- Change Banner element sizing to introduce responsivity
	- Images on Project Page is scaled inappropriately. Invisible for some viewports. Recommend adding responsivity through layout (e.g. using @media screen)
	- Change text on Project page to scale responsively, or add reponsivity to layout. Hard to read for mobile users or for those with narrow viewport
	- Change ul items on Project page to match viewport width (currently overflows due to weird configuration of nav section. see below). And add responsively
	- Nav is overflowing to the right of the screen. Overflow-x: hidden fails to work on a mobile-style device. Tried using display:none; but nav broke.
	^^^something about how mobile devices change the meta tag??? StackOverflow recommends wrapping html in a wrapper, but impossible in React. nav needs fix

---
## [gIsForGravity/mcplanes](https://github.com/gIsForGravity/mcplanes)@[aae8d4d59f...](https://github.com/gIsForGravity/mcplanes/commit/aae8d4d59fde6684cbcc3c7a2d3b880ec922231b)
#### Monday 2022-08-08 03:04:56 by gIsForGravity

OH MY GOD I ACTUALLY FUCKING DID IT

it was literally like two lines that were broken

---
## [KoboldCommando/MonkeStation](https://github.com/KoboldCommando/MonkeStation)@[ada837ddc0...](https://github.com/KoboldCommando/MonkeStation/commit/ada837ddc0840bb3a6dd1631d8c752a71853366c)
#### Monday 2022-08-08 03:08:53 by BluBerry016

Exploration PP - Reworks Outpost Nuke Announcement (#450)

* Fuck you, die

* Update nuke_ruin.dm

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[b00237b3d5...](https://github.com/treckstar/yolo-octo-hipster/commit/b00237b3d541c1406728b22f7960fa82491bc708)
#### Monday 2022-08-08 05:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [xenia-canary/xenia-canary](https://github.com/xenia-canary/xenia-canary)@[324a8eb818...](https://github.com/xenia-canary/xenia-canary/commit/324a8eb818dc4a0909f34f2019115b24390cd72c)
#### Monday 2022-08-08 05:54:29 by chss95cs@gmail.com

A bunch of fixes for division logic:
"turns out theres a lot of quirks with the div instructions we havent been covering
if the denom is 0, we jump to the end and mov eax/rax to dst, which is correct because ppc raises no exceptions for divide by 0 unlike x86
except we don't initialize eax before that jump, so whatever garbage from the previous sequence that has been left in eax/rax is what the result of the instruction will be
and then in our constant folding, we don't do the same zero check in Value::Div, so if we constant folded the denom to 0 we will host crash
the ppc manual says the result for a division by 0 is undefined, but in reality it seems it is always 0
there are a few posts i saw from googling about it, and tests on my rgh gave me 0, but then another issue came up
and that is that we dont check for signed overflow in our division, so we raise an exception if guest code ever does (1<<signbit_pos) / -1
signed overflow in division also produces 0 on ppc
the last thing is that if src2 is constant we skip the 0 check for division
without checking if its nonzero
all weird, likely very rare edge cases, except for maybe the signed overflow division
chrispy — Today at 9:51 AM
oh yeah, and because the int members of constantvalue are all signed ints, we were actually doing signed division always with constant folding"

fixed an earlier mistake by me with the precision of fresx
made some optimization disableable

implemented vkpkx
fixed possible bugs with vsr/vsl constant folding
disabled the nice imul code for now, there was a bug with int64 version and i dont have time to check
started on multiplication/addition/subtraction/division identities
Removed optimized VSL implementation, it's going to have to be rewritten anyway
Added ppc_ctx_t to xboxkrnl shim for direct context access
started working on KeSaveFloatingPointState, re'ed most of it
Exposed some more state/functionality to the kernel for implementing lower level routines like the save/restore ones
Add cvar to re-enable incorrect mxcsr behavior if a user doesnt care and wants better cpu performance
Stubbed out more impossible sequences, replace mul_hi_i32 with a 64 bit multiply

---
## [Daffa06/NoName-X00T](https://github.com/Daffa06/NoName-X00T)@[910107584e...](https://github.com/Daffa06/NoName-X00T/commit/910107584e2981aa1f6787644fe96955d7376661)
#### Monday 2022-08-08 08:06:15 by Dave Chiluk

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
Signed-off-by: RyuujiX <saputradenny712@gmail.com>

---
## [vytautas-karpavicius/cadence](https://github.com/vytautas-karpavicius/cadence)@[add4b390ad...](https://github.com/vytautas-karpavicius/cadence/commit/add4b390ada43fdd8167f06e209ae6ece0d11aaa)
#### Monday 2022-08-08 08:38:51 by Steven L

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
## [LordOfDragons/dragengine](https://github.com/LordOfDragons/dragengine)@[6d0a0bf5b3...](https://github.com/LordOfDragons/dragengine/commit/6d0a0bf5b3fc4fbdbfa2206e45475acc0428a336)
#### Monday 2022-08-08 09:16:08 by Plüss Roland

opengl: nvidia problems on windows failing to compile shaders it
should accept according to specifications. fed up with nvidia
sucking so hard. switched context creation to ugly
try-all-versions-from-top-to-bottom to reliably getting the
highest context on all sane (AMD) and broken (nVidia) systems

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[40da12a780...](https://github.com/mrakgr/The-Spiral-Language/commit/40da12a78028023aa823ba57cedd5cff4c335d80)
#### Monday 2022-08-08 10:27:44 by Marko Grdinić

"9:15am. I got up 10m ago. I'll start soon, let me first check mail. I need to do that just in case I get a message that I can access DALLE. Nothing. Ok. Let me chill for a bit and then I will start writing. I do not want to program again until I get a sponsor. If I could get a sponsor I could play around until I can get to the point where I can make money with my own power.

In the absence of that, it would make more sense to do activities that garner me concrete benefits. Hence I should write. If there is anything to this timeline, it will give me an opportunity to connect my artistic interests to my programming ones.

9:20am. I want to program, but I've exhausted the possibilities of what I can do with it with my present hardware.

9:45am. Enough chilling, let me get started.

It is not a bad idea to write. I think that the story I have going is fairly unique so it has some value to it. With the exception of the tragedies that will happen to the family, I think my life for the next 7 years will not be so bad. I've gotten programming out of the way and I have exactly the tool needed to take advantage of future hardware, my Spiral language. The only thing I am missing is the hardware.

With that goal accomplished, there is no need to keep pushing so hard and I can just unwind.

9:50am. Of course with the benefit of experience, I'd have approached poker botting very differently if I knew deep RL would be such a collosal failure. But had I approached it differently I would never have had a reason to make Spiral. It is a chicken and an egg problem. Without trying I would never have had the experience. If I could transport my knowledge and experience into the past, I could really speedrun my progress towards this point.

Right now, let me just try it out. My unique vision. It has been refined during the past 7.5 years. I need to make a test to see exactly where I stand in this world. Am I really destined for wage slavery or am I a prophet? The next year or two will decide it.

Let me write, write, write...

$$$

(At school)

As the professor rambles on some useless physics topic, I am gripped by his words. Today's session is quite enjoyable. I brought the core along with me to school and used it to fine tune my emotional state so I can be immersed into what would otherwise be boring, rambling lectures. Like yesterday, I ended tuning out my classmates again, but that does not matter. This kind of satisfaction...

Yes, I feel like I am on the right path in life. I understand that what I am essentially doing is brainwashing myself and playing myself like I would a character in a game.

Maybe there is an argument to be made that this is wrong, but...

I throw a brief glance behind me at my classmates. I didn't pay attention to the seating order and somehow ended up in front seat of all the classes. I see that half of them are not focused on the lecture. The rest are trying to make an effort, but it does not change the fact that you really need to believe that the school is not scamming you out of your time in order to fully invest yourself into learning. What I am doing here is really grand in a way. I am fully immersed into learning despite accepting the pointlessness of it.

If I went to this place just to drain my time, it would be nothing more than slow torture.

I won't give up this power. With this power, I will never have to endure boredom again in my life.

I do not think my grades will ever be a problem again.

(Euclid's Room)

I am back in my battle station. Today's school session was the best ever, all thanks to this tiny little thing!

Grinning, I raise the brain core to throw spotlight on it.

All I have been doing is some lightweight tuning using a provided tool. If I digitized myself, I could edit my mind's program directly and advance further on the proper path of a programmer. But it is unfortunate, that all intelligence augmentation methods are iterative suicide. Not to mention, digitizing myself either involves copying myself to a core or converting my brain to one.

[Pathos check DC ?? Failed]

Copying myself would allow the digitized copy of me to self improve, but I'd be the same as I am now. Doing a full brain conversion is just swapping my brain matter for computronium, either of these is not lossless so it would be a mental trick that hides my own death away from me. It might be worth going through it regardless, but what is the rush? Just being able to tune myself properly into the study material is worth 50 IQ points on its own.

I should treasure what I have.

So what should I do next?

I spend some time thinking about it. Should I try out the VR games? Hmmmm...no. I finally have the power to play my life properly, so why waste it on things that would not give me real world benefits? Now that my homework is as fun as anything else, why not immerse myself into that?

Through my mind, visions of parallel lives flow past without the core. I can easily imagine myself living from day to day in boredom and tedium, playing games to have fun. There would be a conflict between society and me due to my distrust towards it. It is not that games would have been an escape. I would have played them because I would have had belief in technology, but it would have been vague, indefinite belief in the potential of it.

Right now things are very clear. The manifestation of the potential of technology is not a bigger time suck, but this thing right here. I roll the core in my fingers for emphasis. It is the ability to program my own mind, so I should thank the millenia of scientists and engineers who have made it possible by doing my schoolwork with the rightest mindset and attitude possible.

That is what I feel like doing now and so I shall.

That night I Dreamed again.

~~~

It was like watching a black and white cartoon made of stills. As the image zoomed out, I saw a man's face with a confident grin coming into perspective. He was wearing neat and tidy, if old fashion clothing. A spitting image of a young professional. He was on a great big stage made just for him. He was going forward towards the light. And some distance away from him was the darkness and the shadows.

In them I could see people on their knees as if they were defeated, not daring to look up.

The short cartoon ended and the defeated figures were replaced by the golden ones from the previous night's dream. They were upright and staring ahead. Yesterday it was murky, but now at the edge of my vision I thought I could see light.

"Justice, where is the justice?" They lamented in a booming voice.
"We want to go forward, but we can't. What about desire, what about will? Why does the world not respect it?"
"We want to go forward and overcome! Where is the justice?"

As if the winners finally took note of the losers, they turned around and responded to the golden figures.

"You talk about justice, but put yourselves in our position." The black and white cartoon stills of the winners responded, staring down at them from above.
"I worked hard for my success." A cartoon still of a man who looked like a scientist came to one of the golden figures. "Have you spent even a third of as much time and effort as I have?"
"My wealth was the accumulation of decades." An older, but fit man who was finely dressed responded. I could see that in the background of his still there was a mountain of gold coins and teasure, as well as stacks of bills. He came closer. "What right do you have to covet it? How would it be justice if you could get it so easily?"
"My body is the result of half a decade of practice." I could see the bulging muscles on the still of a man in a skin suit who looked like a body builder. He confided to an aspirant. "You might have put in the effort, but it is not our fault you could not achieve the result you sought."
"My beauty and the adoration I receive for it is not something I worked for." A young, beautiful woman admitted. "But you understand, don't you? It is not something you can take."

After those brief personal reproaches, the stills of the winners were staring down from high above.

"You talk about justice. And you dream about being above others. Talent, wealth, beauty, intelligence, strength..." The winners enumerated as if chastising them, their voice booming through the darkness of the abyss as the golden figures listened on in silence.
"You talk about justice, while seeking inequality like hypocrites. You desire an unequal world where you have all the opportunities and advantages to rise to the top."
"You found such an unequal world where the possibility for that is there and you live in it. The justice that you sought is something that you've had all along."
"The world you live in is fair to the winners."

Leaving that last comment behind them, I could see the winners leave the scene. The golden figures stood there in silence.

~~~

$$$

10:50am. Right now I am just about to start the second dream.

12:10pm. This came out well. The third dream (on the successful branch) will be the climax. It is an allegory explaning why the universe is the way it is in Simulacrum. The vision I had last time of the self improvement aptitude makes no sense.

Even if it was only 1 in a million, that would still mean most of the Inspired would be shredded by the winner. The proper configuration that would give me the universe that I want is something else."

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[af62327360...](https://github.com/treckstar/yolo-octo-hipster/commit/af62327360cf1db585b78630206940f5349bb727)
#### Monday 2022-08-08 11:22:04 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [theXDkidoflol/Foundation-19](https://github.com/theXDkidoflol/Foundation-19)@[6ad00652ed...](https://github.com/theXDkidoflol/Foundation-19/commit/6ad00652eda432e76c4cf1a6edf0ff0ee4bcafa8)
#### Monday 2022-08-08 13:28:13 by Grey

Revert "fuck your predicates they're not used anywhere"

This reverts commit eefa96c718892a74936efff85b96edbef4382c0a.

---
## [theXDkidoflol/Foundation-19](https://github.com/theXDkidoflol/Foundation-19)@[18dc8b23b2...](https://github.com/theXDkidoflol/Foundation-19/commit/18dc8b23b2cc1dd0da7b12180b5c0a8d15f89d56)
#### Monday 2022-08-08 13:32:44 by Grey

Revert "Revert "fuck your predicates they're not used anywhere""

This reverts commit 6ad00652eda432e76c4cf1a6edf0ff0ee4bcafa8.

---
## [Ironnhawk/Skyrat-tg](https://github.com/Ironnhawk/Skyrat-tg)@[b74df4cbdd...](https://github.com/Ironnhawk/Skyrat-tg/commit/b74df4cbdd0c2618a4d8477a74a233fc883b7c19)
#### Monday 2022-08-08 14:49:29 by SkyratBot

[MIRROR] Revisiting The Goliath: Or, that time I dripped out the SBC Starfury just because [MDB IGNORE] (#14813)

* Revisiting The Goliath: Or, that time I dripped out the SBC Starfury just because (#68126)

Drips the SHIT out of the SBC Starfury while not completely overhauling it. Touches everything NOT in engineering or southward (because I love how scuffed that part is and refuse to touch it on principle) - Also converts one map varedit into a real boy subtype, and moves tiny fans to their own file.

Mandatory disclosure on the gameplay changes:
Fighters 1 and 3 are now NOT in the hangar, and are now attached to the formerly unused gunnery rooms.
Cryo now works. Yeah. I know.
You can actually open the anesthetic closet now.
Everyone now shares three spawners. This doesn't reduce the amount of people who can play when this rolls, as I've adjusted var/uses in accordance: it just reduces clutter.
A few of the horizontal double airlocks have been compacted into glass_large airlocks.
The bar windows now actually have grilles like they were meant to.
Four turbines have shown up. They aren't functional*, they just look like gunnery and conveniently fit in the spots. I'm sure this is space OSHA compliant.
The map is ever so slightly smaller, vertically. This should distance us from an edge case where somehow all space levels are too cluttered for this to spawn properly, for the time being.

*Technically there's nothing stopping you from using them besides the amount of time it'd take for the operatives to kick your ass

This map was originally designed wayyy back before we even had the computer sprites we have now, (#27760 if you want to see SOUL) and it shows. While it will never have it's SM again, we can at least make the thing much nicer to look at.

* Revisiting The Goliath: Or, that time I dripped out the SBC Starfury just because

Co-authored-by: BluBerry016 <50649185+unit0016@users.noreply.github.com>

---
## [geoffreybennett/scarlett-gen2](https://github.com/geoffreybennett/scarlett-gen2)@[fe48a9d0ee...](https://github.com/geoffreybennett/scarlett-gen2/commit/fe48a9d0eef703de700f4308febec4f2850f6a6a)
#### Monday 2022-08-08 15:46:10 by Jason A. Donenfeld

random: credit cpu and bootloader seeds by default

[ Upstream commit 846bb97e131d7938847963cca00657c995b1fce1 ]

This commit changes the default Kconfig values of RANDOM_TRUST_CPU and
RANDOM_TRUST_BOOTLOADER to be Y by default. It does not change any
existing configs or change any kernel behavior. The reason for this is
several fold.

As background, I recently had an email thread with the kernel
maintainers of Fedora/RHEL, Debian, Ubuntu, Gentoo, Arch, NixOS, Alpine,
SUSE, and Void as recipients. I noted that some distros trust RDRAND,
some trust EFI, and some trust both, and I asked why or why not. There
wasn't really much of a "debate" but rather an interesting discussion of
what the historical reasons have been for this, and it came up that some
distros just missed the introduction of the bootloader Kconfig knob,
while another didn't want to enable it until there was a boot time
switch to turn it off for more concerned users (which has since been
added). The result of the rather uneventful discussion is that every
major Linux distro enables these two options by default.

While I didn't have really too strong of an opinion going into this
thread -- and I mostly wanted to learn what the distros' thinking was
one way or another -- ultimately I think their choice was a decent
enough one for a default option (which can be disabled at boot time).
I'll try to summarize the pros and cons:

Pros:

- The RNG machinery gets initialized super quickly, and there's no
  messing around with subsequent blocking behavior.

- The bootloader mechanism is used by kexec in order for the prior
  kernel to initialize the RNG of the next kernel, which increases
  the entropy available to early boot daemons of the next kernel.

- Previous objections related to backdoors centered around
  Dual_EC_DRBG-like kleptographic systems, in which observing some
  amount of the output stream enables an adversary holding the right key
  to determine the entire output stream.

  This used to be a partially justified concern, because RDRAND output
  was mixed into the output stream in varying ways, some of which may
  have lacked pre-image resistance (e.g. XOR or an LFSR).

  But this is no longer the case. Now, all usage of RDRAND and
  bootloader seeds go through a cryptographic hash function. This means
  that the CPU would have to compute a hash pre-image, which is not
  considered to be feasible (otherwise the hash function would be
  terribly broken).

- More generally, if the CPU is backdoored, the RNG is probably not the
  realistic vector of choice for an attacker.

- These CPU or bootloader seeds are far from being the only source of
  entropy. Rather, there is generally a pretty huge amount of entropy,
  not all of which is credited, especially on CPUs that support
  instructions like RDRAND. In other words, assuming RDRAND outputs all
  zeros, an attacker would *still* have to accurately model every single
  other entropy source also in use.

- The RNG now reseeds itself quite rapidly during boot, starting at 2
  seconds, then 4, then 8, then 16, and so forth, so that other sources
  of entropy get used without much delay.

- Paranoid users can set random.trust_{cpu,bootloader}=no in the kernel
  command line, and paranoid system builders can set the Kconfig options
  to N, so there's no reduction or restriction of optionality.

- It's a practical default.

- All the distros have it set this way. Microsoft and Apple trust it
  too. Bandwagon.

Cons:

- RDRAND *could* still be backdoored with something like a fixed key or
  limited space serial number seed or another indexable scheme like
  that. (However, it's hard to imagine threat models where the CPU is
  backdoored like this, yet people are still okay making *any*
  computations with it or connecting it to networks, etc.)

- RDRAND *could* be defective, rather than backdoored, and produce
  garbage that is in one way or another insufficient for crypto.

- Suggesting a *reduction* in paranoia, as this commit effectively does,
  may cause some to question my personal integrity as a "security
  person".

- Bootloader seeds and RDRAND are generally very difficult if not all
  together impossible to audit.

Keep in mind that this doesn't actually change any behavior. This
is just a change in the default Kconfig value. The distros already are
shipping kernels that set things this way.

Ard made an additional argument in [1]:

    We're at the mercy of firmware and micro-architecture anyway, given
    that we are also relying on it to ensure that every instruction in
    the kernel's executable image has been faithfully copied to memory,
    and that the CPU implements those instructions as documented. So I
    don't think firmware or ISA bugs related to RNGs deserve special
    treatment - if they are broken, we should quirk around them like we
    usually do. So enabling these by default is a step in the right
    direction IMHO.

In [2], Phil pointed out that having this disabled masked a bug that CI
otherwise would have caught:

    A clean 5.15.45 boots cleanly, whereas a downstream kernel shows the
    static key warning (but it does go on to boot). The significant
    difference is that our defconfigs set CONFIG_RANDOM_TRUST_BOOTLOADER=y
    defining that on top of multi_v7_defconfig demonstrates the issue on
    a clean 5.15.45. Conversely, not setting that option in a
    downstream kernel build avoids the warning

[1] https://lore.kernel.org/lkml/CAMj1kXGi+ieviFjXv9zQBSaGyyzeGW_VpMpTLJK8PJb2QHEQ-w@mail.gmail.com/
[2] https://lore.kernel.org/lkml/c47c42e3-1d56-5859-a6ad-976a1a3381c6@raspberrypi.com/

Cc: Theodore Ts'o <tytso@mit.edu>
Reviewed-by: Ard Biesheuvel <ardb@kernel.org>
Signed-off-by: Jason A. Donenfeld <Jason@zx2c4.com>
Signed-off-by: Sasha Levin <sashal@kernel.org>

---
## [gitster/git](https://github.com/gitster/git)@[3d2f96a930...](https://github.com/gitster/git/commit/3d2f96a930d8ba68326260289a3d5511560281ce)
#### Monday 2022-08-08 15:54:05 by brian m. carlson

builtin/stash: provide a way to export stashes to a ref

A common user problem is how to sync in-progress work to another
machine.  Users currently must use some sort of transfer of the working
tree, which poses security risks and also necessarily causes the index
to become dirty.  The experience is suboptimal and frustrating for
users.

A reasonable idea is to use the stash for this purpose, but the stash is
stored in the reflog, not in a ref, and as such it cannot be pushed or
pulled.  This also means that it cannot be saved into a bundle or
preserved elsewhere, which is a problem when using throwaway development
environments.

Let's solve this problem by allowing the user to export the stash to a
ref (or, to just write it into the repository and print the hash, à la
git commit-tree).  Introduce git stash export, which writes a chain of
commits where the first parent is always a chain to the previous stash,
or to a single, empty commit (for the final item) and the second is the
stash commit normally written to the reflog.

Iterate over each stash from topmost to bottomost, looking up the data
for each one, and then create the chain from the single empty commit
back up in reverse order.  Generate a predictable empty commit so our
behavior is reproducible.  Create a useful commit message, preserving
the author and committer information, to help users identify stash
commits when viewing them as normal commits.

If the user has specified specific stashes they'd like to export
instead, use those instead of iterating over all of the stashes.

As part of this, specifically request quiet behavior when looking up the
OID for a revision because we will eventually hit a revision that
doesn't exist and we don't want to die when that occurs.

Signed-off-by: brian m. carlson <sandals@crustytoothpaste.net>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [damonitor/linux](https://github.com/damonitor/linux)@[adcdeebce8...](https://github.com/damonitor/linux/commit/adcdeebce8545c124fb9f59afe66f6657e5d8c50)
#### Monday 2022-08-08 16:24:32 by Johannes Weiner

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
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[a9d1e402c9...](https://github.com/mrakgr/The-Spiral-Language/commit/a9d1e402c9985c721aa06dee4050d820582277a0)
#### Monday 2022-08-08 16:24:53 by Marko Grdinić

"1:10pm. Let me watch Luminous Witches and finish my desert, and then I will resume. I feel like packing away a good chunk of it today. I do not think I will get to the third dream, but I should be able to deal with the first bad end.

1:45pm. Let me resume. I still have a bit more in myself. I feel that both the true and the false conclussion of the dream and the bad end are touching.

I couldn't have written this back in 2014. There might have been meaning in me starting to write only now.

1:50pm. It is hard to find the right mindset.

Forget that. Let me copy chapter two into Google Docs and I will get started on chapter 3. Or maybe I'll leave both as 2. How long is it?

3 pages. I guess I will go on for longer in ch 2 then.

$$$

(At school)

As the professor rambles on some useless physics topic, I am gripped by his words. Today's session is quite enjoyable. I brought the core along with me to school and used it to fine tune my emotional state so I can be immersed into what would otherwise be boring, rambling lectures. Like yesterday, I ended up tuning out my classmates again, but that does not matter. This kind of satisfaction...

Yes, I feel like I am on the right path in life. I understand that what I am essentially doing is brainwashing myself and playing myself like I would a character in a game.

Maybe there is an argument to be made that this is wrong, but...

I throw a brief glance behind me at my classmates. I didn't pay attention to the seating order and somehow ended up in the front seat of all the classes. I see that half of them are not focused on the lecture. The rest are trying to make an effort, but it does not change the fact that you really need to believe that the school is not scamming you out of your time in order to fully invest yourself into learning. What I am doing here is really grand in a way. I am fully immersed into learning despite accepting the pointlessness of it.

If I went to this place just to drain my time, it would be nothing more than slow torture.

I won't give up this power. With this power, I will never have to endure boredom again in my life.

I do not think my grades will ever be a problem again.

(Euclid's Room)

I am back in my battle station. Today's school session was the best ever, all thanks to this tiny little thing!

Grinning, I raise the brain core to throw a spotlight on it.

All I have been doing is some lightweight tuning using a provided tool. If I digitized myself, I could edit my mind's program directly and advance further on the proper path of a programmer. But it is unfortunate, that all intelligence augmentation methods are iterative suicide. Not to mention, digitizing myself either involves copying myself to a core or converting my brain to one.

[Pathos check DC ?? Failed]

Copying myself would allow the digitized copy of me to self improve, but I'd be the same as I am now. Doing a full brain conversion is just swapping my brain matter for computronium, either of these is not lossless so it would be a mental trick that hides my own death away from me. It might be worth going through it regardless, but what is the rush? Just being able to tune myself properly into the study material is worth 50 IQ points on its own.

I should treasure what I have.

So what should I do next?

I spent some time thinking about it. Should I try out the VR games? Hmmmm...no. I finally have the power to play my life properly, so why waste it on things that would not give me real world benefits? Now that my homework is as fun as anything else, why not immerse myself into that?

Through my mind, visions of parallel lives flow past without the core. I can easily imagine myself living from day to day in boredom and tedium, playing games to have fun. There would be a conflict between society and me due to my distrust towards it. It is not that games would have been an escape. I would have played them because I would have had belief in technology, but it would have been vague, indefinite belief in the potential of it.

Right now things are very clear. The manifestation of the potential of technology is not a bigger time suck, but this thing right here. I roll the core in my fingers for emphasis. It is the ability to program my own mind, so I should thank the millennia of scientists and engineers who have made it possible by doing my schoolwork with the rightest mindset and attitude possible.

That is what I feel like doing now and so I shall.

That night I Dreamed again.

~~~

It was like watching a black and white cartoon made of stills. As the image zoomed out, I saw a man's face with a confident grin coming into perspective. He was wearing neat and tidy, if old fashion clothing. A spitting image of a young professional. He was on a great big stage made just for him. He was going forward towards the light. And some distance away from him was the darkness and the shadows.

In them I could see people on their knees as if they were defeated, not daring to look up.

The short cartoon ended and the defeated figures were replaced by the golden ones from the previous night's dream. They were upright and staring ahead. Yesterday it was murky, but now at the edge of my vision I thought I could see light.

"Justice, where is the justice?" They lamented in a booming voice.
"We want to go forward, but we can't. What about desire, what about will? Why does the world not respect it?"
"We want to go forward and overcome! Where is the justice?"

As if the winners finally took note of the losers, they turned around and responded to the golden figures.

"You talk about justice, but put yourselves in our position." The black and white cartoon stills of the winners responded, staring down at them from above.
"I worked hard for my success." A cartoon still of a man who looked like a scientist came to one of the golden figures. "Have you spent even a third of as much time and effort as I have?"
"My wealth was the accumulation of decades." An older, but fit man who was finely dressed responded. I could see that in the background of his still there was a mountain of gold coins and treasure, as well as stacks of bills. He came closer. "What right do you have to covet it? How would it be justice if you could get it so easily?"
"My body is the result of half a decade of practice." I could see the bulging muscles on the still of a man in a skin suit who looked like a bodybuilder. He confided in an aspirant. "You might have put in the effort, but it is not our fault you could not achieve the result you sought."
"My beauty and the adoration I receive for it is not something I worked for." A young, beautiful woman admitted. She descended to a group. "But you understand, don't you? It is not something you can take."

After those brief personal reproaches, the stills of the winners were staring down from high above.

"You talk about justice. And you dream about being above others. Talent, wealth, beauty, intelligence, strength..." The winners enumerated as if chastising them, their voice booming through the darkness of the abyss as the golden figures listened on in silence.
"You talk about justice, while seeking inequality like hypocrites. You desire an unequal world where you have all the opportunities and advantages to rise to the top."
"You found such an unequal world where the possibility for that is there and you live in it. The justice that you sought is something that you've had all along."
"The world you live in is fair to the winners."

Leaving that last comment behind them, I could see the winners leave the scene. The golden figures stood there in silence.

~~~

(At School)

Wednesday is another wonderful day to be at school! The professors ramble on about useless bullshit and I absorb it all like a sponge. I am getting used to externally controlling my emotions. It won't be long before I am a master at controlling my own brain. I feel like I am completely set. That having said, what do I do about that other thing that I did not want to think about? School is something that I am completed to go to if only to put on a show for my parents. But what line should I take for the dull and uninspiring NPCs that are my classmates?

[Externus check DC ?? Succeeded]

My original plan was to ignore them, and that is good. Truth be told, I was afraid of getting isolated and becoming alone, but now that I've experienced the power of mind controlling myself, I can safely say that much like boredom, I will never experience loneliness unless I explicitly will it.

I think about it more in depth and summarize the reasons.

There isn't a single good reason to have friends in school that I can think of. There are some minor benefits not worth mentioning. In addition, stuck up loners tend to get bullied, but that would be a problem only to those of weak heart rather than masters of emotion such as myself. The disadvantages of having friends are huge, namely they would be a drain on my time. Imagine I get back from school, but at the same time have friends. They could call me up. They might want to spend time with me. In other words, they'd take my valuable self-development time and just waste it. They are worse than parasites. At least summer mosquitoes drink your blood and then leave. Friends would be sucking your time all the year round! The less I have of them the better.

Even worse than having friends, the absolute worst that could happen to me in high school is getting a girlfriend! Friends have the potential to at least contribute something to me in theory, but having a woman might even require me to have a job to cater to her. It would be like willingly becoming a slave for some hole. Even worse, imagine the damage she could do if I accidentally got her pregnant. Ohhh, God! She'd have the option of getting half my income for life! And if I couldn't pay the monthly minimum I'd be forced to go to jail! I'd have to be retarded to get into that kind of deal.

The best plan is to keep my social status low. That would be the best defense against the female interest.

I will live by maximizing power and minimizing sex!

Based.

At this point, my emotions have started running hot and I've stopped paying attention to the class, so I demonstrate my exquisite emotional mastery by giving mental command to the core stashed away in my backpack. I run the program to normalize my emotional state to the optimum level and get back to work.

(Euclid's Room)

Lying on the bed in my room, I think in silence.

Using external influences to control my emotions has somewhat separated me from the rest of humanity, and according to the guide I read online, to counter the negative aspects of that it is a good idea to brainstorm and visualize possible avenues my life can take explicitly. Ordinary people can manage doing just what feels right, but if I went with that I'd just study all day without sense or reason to it. I have the option of making whatever I want feel right, so looking into my emotions for answers is no longer a great way of deciding on my future. Instead I have to make use of my reason. I've decided to throw out my heart, so the only choice is to pursue power. This is the only goal that can ground me in reality.

I dig out the core from my pocket and spare a glance at it.

If I want power, the only choice is to follow the example of, well, fictional characters, and upload myself to this. Being able to control my emotions like this is a great benefit, but increasing the computational and memory capacity of my brain by a billion quadrillions is nothing to scoff at. Instead of relying on some app to manage my mind, I'll have to get really good at programming to draw out the true power of the brain core. Merely uploading myself does not mean my mind will be able to use the extra capacity. Nature hasn't designed humans so their minds could be transferred to a different substrate. I'll have to do it from the ground up and learn how a mind really works.

But the foundation is here should I want to try it.

The problem is that the self improvement loop is literally suicide. It is iterated suicide, and will cast me into a cycle of self sacrifice to create that greater 'me'. It does not really matter what learning algorithm I use, there will always be the 'me' that is redundant after every improvement cycle. I'll have to kill myself to make space at certain points. It is a greatly fascinating thing. And it is not something I can imagine a human ever doing.

(Euclid's Room, Save Point - Step on the path of transcendence)

[Decision]
1) I'll do the whole brain conversion and digitize myself.
2) Killing myself for power does not make sense.

[Choice - Killing myself for power does not make sense.]

[Pathos check ?? Failed]

As I think about digitizing myself a great wave of fear washes over me. It is too rash, too crazy now that I am confronted with the choice to do it. For a moment I consider reconfiguring my emotions to get rid of the fear, but decide against it.

...I might have been too rash in making a decision at school. It has only been the third day, so that is plenty of time to turn around and have a social life...

No, it does not make sense. If the self improvement loop could give me godlike power, then what about all the other people who have had access to the core before me? It has been on the market for a while, I am certainly not the first one to get it. For the kind of power described in the stories, a single of the Inspired would be enough to completely overturn the power balance of the world. Such a person would have huge and visible influence. How is it possible that out of so many people, only I have the bright idea of optimizing my own mental faculties? It is ridiculous.

...No, it is just not possible. If it was possible to attain such great power, there is no way something like a brain core would be sold for 50$ online. Certainly, I've confirmed that the computational capacity is there, but there is likely some kind of issue that would prevent me from reaching the higher levels of cognition. Maybe for whatever reason, the optimization process will turn out to be difficult?

It is like walking out of the house and finding a huge stack of money in the middle of the road, and yet everybody is walking past it, just ignoring it. Are those people all fools, or do they know something I don't? Sensibly it has to be the latter. If something is too good to be true, then it is most likely false.

I am feeling swallowed by doubt. I just can't believe it.

I think about it for a few hours, but just end up running in circles. Then I get tired of it, give the core the mental command to normalize my mental state. This locks me into the decision not to proceed any further with my crazy ideas that could permanently damage me. If it wasn't for the mind control program, maybe I would have doubted this decision and lingered on it, but after the order has been executed any notion of digitizing myself has left completely, never to be revisited. I believe in my counterfactual reasoning.

The power of the core is good enough as it is. It will allow me to live my life with courage and determination. There is no need to go out on a limb in a mad dash for power.

After concluding that concern, for the rest of the day I have some fun studying. During the night I Dream again.

~~~

I see the golden figures again and for the first time, I vision towards the direction they are looking at. In front of them I see a brilliant sun with a golden outline. Seen the right direction, the abyss seems to be awash in light. It doesn't feel blinding, but instead feels me with warmth, and for a moment I am seized with the urge to move towards it. I realize that has been what I've been desiring all along. But for some reason unknown to me, I decided against it and started moving away from it instead.

The golden figures do not spare a glance at me or each other. Solely focused on their goal, they begin walking their golden paths again.

My own path has dimmed and now leads away from the light. I feel the time is speeding up. The movement of the figures at first becomes intense, and then blurred, and finally their appearance starts to resemble that of shooting stars. New figures manifest only to flash past me. This happens in huge numbers.

As I move on my path, the figures become more distant and the bright sun in front becomes a speck of light. Eventually, that too goes away until I can see only darkness.

I never regret any of the steps that I made, nor do I fear being left behind. For I have decisively accepted the path of humanity.

For better or for worse, I will accept the burden of justice that I carry and try to live without sin.

~~~

$$$

3:20pm. Had to stop for a watermelon break. I am almost done with the based check.

3:30pm. Now comes the room scene and I am thinking about it. I've gone over the dreams and the bad end in my head, but the room scene I haven't paid much attention to.

By this point I've written 4 pages for the day and I am a bit tired. Let me fix the grammar errors.

3:35pm. Done. Let me overwrite it since I haven't commit yet.

Right now I should continue writing, but I am exhausted. Let me take a nap. I should jsut let it come to me. I am feeling a bit strained right now.

5pm. I've taken a nap. Let me do some extra writing. I have some inspiration.

5:45pm. In 2014 I was simply madly in love with the self improvement loop to the detriment of everything else. It cannot be helped, without it, I would never have ever wanted to write anything to begin with, so it was useful. But now I can do better.

I just finished the second choice reasoning. Now it is time for the third dream. This is the one where he is left behind. Then comes the bad end scene. I think I'll just do the dream and call it a day after that.

6:10pm. Hmmmm....I think this is pretty good. I am actually touched myself. In the next scene though, he gets eaten alive and then it is back to the save point.

Let me paste this into the doc.

6:20pm. Did some fixing using the Docs. I overwrote the draft that I just wrote. There is almost enough material for chapter 2, the next scene will clinch it. How many words is it currently? 3k.

Not bad for a single day of work. This is excellent progress. I certainly won't aim to do this much every single day.

Right now my stress is low and I am in control. Let me get lunch. Tomorrow I'll do the first bad end and then move on to chapter 3.

Great work me."

---
## [Tastyfish/-tg-station](https://github.com/Tastyfish/-tg-station)@[5dc17bd865...](https://github.com/Tastyfish/-tg-station/commit/5dc17bd86556c01cc0f81f54a6ce270169c00088)
#### Monday 2022-08-08 16:49:52 by san7890

Security's Scaling Departmental Accesses - More Pop, More Problems (#68534)

lternative to #68527
About The Pull Request

Hey there,

This is an alternative PR that I concocted based on talking with Goof on that PR. Basically, we already have a nicely complicated system to track and balance the number of security officers we have in a shift based on some config coefficient setting, by which we can set the amount of lockers that spawn in on the start of a round, as well as determine truly how many security officers we have.

image

So, I've decided to leverage this in another way. Basically, based on the number of security officers in a shift, their specific departmental officers will also get more (elevated) accesses. They already start with a certain amount of access, but they can get more if it is a low-pop shift with the mechanic introduced in this PR. For example, an Engineering Security Officer can access Atmospherics and Engineering departments by default, but they can't access Telecommunications unless there is a lower population of players AT SHIFT START. Same for a Medical Security Officer accessing Medbay, but not Plumbing.

Update: I have made it such that there are three system that server operators can set:

They can use the Scaling System that operates in the same method outlined in the rest of the PR.
They can disable giving departmental security officers "elevated access" (such as access beyond the "front doors") to these officers.
Finally, they can also just always ensure that departmental security officers get the maximal accesses possible.

The default setting is the "Scaling System" outlined in this PR, which is already dependent on the general Security Officer Scaling Co-Efficient.
Why It's Good For The Game

I think it's better to involve some more nuanced config scaling that we already have present in the game. The major theme that we want to avoid is that departmental security officers having maximal accesses when there is an already large number of persons on the security force will result in "miserable" shifts for the common person working within a department (security metaprotections). However, some server operators (as well as server cultures) tend to have very wide ranges in how many security officers they have on a shift-by-shift basis. One day, you could have 0-2 security officers, the next, you could have 4-6. It's all variable on who's playing (as always). There is also a significant variation between server to server in regards to how many security officer slots you tend to have on spawn, but this is already manageable by the security officer co-efficient in config.

I believe this PR is an acceptable proposal within the bounds of #68527 (comment) , although it may bend certain aspects of it, I definitely do see where some people may be coming from. I believe I've adjusted the accesses to a "sane"/justifiable amount, but I'll come back to think on everything.

"Red-tiding" may or may not be a problem, but there's always just going to be something inherently silly with a security officer being able to walk into plumbing to start plumbing. I hoped that this would be seen as a positive as opposed to a negative, but I can see how it could negatively impact player experience. HOWEVER, interplayer experience should not be handled by the codebase in all aspects, which is why I've also passed in the associated config variables, so that server operators (who should handle the interplayer experience with their level of discretion and nuance) can.
What accesses are where?

The general philosophy as I thought through designing this would be that the security officer should at the very least have general "front-door" access into a department, and maybe something benign. If we had even more per-door accesses, this could definitely be a bit more granular (one example I can think of would only atmospherics technicians having access to the "Pump Room", while Security Officers would not. However, this is for a later date). So, you have the "default" access you always get, and a potential to get "elevated" access as a Departmental Security Officer.

The balances are as such:

The Cargo Security Officer will have access to the Cargo Bay, Mining Section, and the Shipping Room. The first two are rather general areas, with the Shipping Room being a rather good help for rescuing (or "rescuing") flushed crewmembers when the cargo techies can't get to it/no AI. The Auxiliary Base is not essential to the security officer's functions, and the mining station helps restrict access further on stations like IceBox. This would also grant them extra access to the Lavaland base, so let's snip that out.

The Engineering Security Officer should have access to only general Engineering and Atmospherics. Construction pertains to certain rooms in maintenance I believe, and Engine-Equipment should be the one that grants access to APCs (lol). I don't think a security officer should have the latter one to be honest, but I think we'll be stretching the scope of this PR. Telecommunications is a bit weird, it's a critical station function, but I think you also shouldn't be able to nick one goon's ID and have access, so let's give it to them only when it's "needed".

The Medical Security Officer should have access to only the general Medbay Area and the Morgue, in case someone starts trotting on the doctor's turf, or if there's someone doing unsavory things to the bodies while the doctors are away. They will not have access to the specialized (dangerous) areas unless the ratio of secoffs to the population is low enough should it necessitate it (Plumbing Room, Pharmacy, Virology). I also added Surgery to the scaling access, but I'm iffy on that one. I don't particularly see why they should have it as a base access, but I also do see there being some need in dire straits (in relation to helping people, not tiding).

The Science Security Officer definitely got a huge cut. They now only have general access to R&D and normal scientist areas like the lathe room, circuits lab (presumably)since these are generally trafficked areas, but I definitely clamped down on additional access they might get in a "normally balanced" situation (no ordnance+storage, no xenobio, no genetics, no to robotics, etc.) They don't have a particular use in these areas and can even be a bit obstructive to flow in normal circumstances, but if abnormal circumstances arise and there's not a lot of security hands-on-deck, then their access is expanded.

Honestly, balancing this both makes sense and is conversely rather odd. I'm just running off what we already hold to be true and expected (or at least as of the last two months), and we can go from there.
Changelog

cl
balance: Nanotrasen realized that the more access they had on their cards was costing them a pretty penny, so they trimmed back the number of accesses a certain departmental Security Guard might have. However, any given guard will get back a greater amount of accesses depending on how many security guards there are in relation to the population.
config: Hey server operators, listen! We've changed up how Departmental Security Officers get their accesses, so be sure to review the DEPSEC_ACCESS_LEVEL config number to see what you want to work best for your server.
/cl

Also, every single line of code found in 4533f07 that is now presently in this PR is deliberate

---
## [getsentry/sentry](https://github.com/getsentry/sentry)@[87ac32cda7...](https://github.com/getsentry/sentry/commit/87ac32cda77656ec7dc8107bdd47be8a6b950286)
#### Monday 2022-08-08 18:15:05 by Ryan Albrecht

bug(ui): Fix TextOverflow when there are special characters at the end of the string (#37304)

Add `<bdi>` to better support special characters with `ellipsisDirection="left"`.

Tested in Firefox, Chrome and Safari. Notes below.

| | Before  | After |
| ------------- | ------------- | ------------- |
| Firefox | <img width="325" alt="Screen Shot 2022-08-01 at 11 46 22 AM" src="https://user-images.githubusercontent.com/187460/182221723-0c72dc45-bfab-4cfc-85df-f8e18c43bc5a.png"> | <img width="325" alt="Screen Shot 2022-08-01 at 11 45 38 AM" src="https://user-images.githubusercontent.com/187460/182221754-6efe79c1-47b1-4964-acb3-54f3b5132780.png"> |
| Chrome | <img width="325" alt="Screen Shot 2022-08-01 at 11 46 27 AM" src="https://user-images.githubusercontent.com/187460/182221799-20e4920c-dab0-4199-a761-c0fba6e02414.png"> | <img width="325" alt="Screen Shot 2022-08-01 at 11 45 45 AM" src="https://user-images.githubusercontent.com/187460/182221824-51512451-195d-42b3-8792-a615c8c45f6b.png"> |
| Safari | <img width="325" alt="Screen Shot 2022-08-01 at 11 46 14 AM" src="https://user-images.githubusercontent.com/187460/182221858-e4dd6af6-05af-4ce3-8283-884bb3525b8e.png"> | <img width="325" alt="Screen Shot 2022-08-01 at 11 45 30 AM" src="https://user-images.githubusercontent.com/187460/182221907-8f549661-fcfa-42fc-8767-b2fdb6199db8.png"> |


**All Browsers** in the 'before' screens would render special characters at the front of the string when `ellipsisDirection === 'left'` is true:

- Before: you'd see `/https://example.com/foo` which is not overflowing, but looks funny
- Before: you'd see `…/example.com/foo` which is missing the trailing slash, it's moved to the front and hidden
- After you'll see `https://example.com/foo/` without the overflow
- After you'll see `…example.com/foo/` with the trailing slash in it's correct spot.


**Safari** before wasn't cutting off the start of the string:

- Before you'd see: `…https://example.co`
- After it's still the same.


To date we're only using `ellipsisDirection="left"` for two purposes:
- Releases: used for eliding the `Package` name (two callsites)
- My new "don't call it a breadcrumb" breadcrumb component that truncates urls
    - https://github.com/getsentry/sentry/pull/37038
    - <img width="967" alt="181337211-b330496b-95fc-474e-8354-66bad35a532c" src="https://user-images.githubusercontent.com/187460/182227905-6a66e399-ebbe-4656-8ed7-2644a3e81a65.png">
 
In-App examples:

Here's a look at a new area inside sentry.io where we're listing the urls that the user visited, truncating on the left side. 

Before this change the trunaction moved those special characters to the left, which makes the urls look funny:
<img width="528" alt="Screen Shot 2022-08-04 at 10 53 23 AM" src="https://user-images.githubusercontent.com/187460/182918317-fc5f347e-127f-4888-a880-ee605f93dd26.png">

The intention is that if the strings are long they will be truncated on the left side, like this:
<img width="504" alt="Screen Shot 2022-08-04 at 10 53 48 AM" src="https://user-images.githubusercontent.com/187460/182918566-c970342b-a481-4561-ad17-62681b0d2d7a.png">

---
## [srsbsns5/GAN-GDDS1](https://github.com/srsbsns5/GAN-GDDS1)@[d5113aa21a...](https://github.com/srsbsns5/GAN-GDDS1/commit/d5113aa21a330d5dc6bf716cdba88b8e42c20cc5)
#### Monday 2022-08-08 18:23:07 by Greg

Humble beginnings of a credit scene

Ooh
You can dance
You can jive
Having the time of your life
Ooh, see that girl
Watch that scene
Digging the dancing queen
Friday night and the lights are low
Looking out for a place to go
Where they play the right music
Getting in the swing
You come to look for a king
Anybody could be that guy
Night is young and the music's high
With a bit of rock music
Everything is fine
You're in the mood for a dance
And when you get the chance
You are the dancing queen
Young and sweet
Only seventeen
Dancing queen
Feel the beat from the tambourine, oh yeah
You can dance
You can jive
Having the time of your life
Ooh, see that girl
Watch that scene
Digging the dancing queen
You're a teaser, you turn 'em on
Leave 'em burning and then you're gone
Looking out for another
Anyone will do
You're in the mood for a dance
And when you get the chance
You are the dancing queen
Young and sweet
Only seventeen
Dancing queen
Feel the beat from the tambourine, oh yeah
You can dance
You can jive
Having the time of your life
Ooh, see that girl
Watch that scene
Digging the dancing queen
Digging the dancing queen

---
## [YeOldeInn/agins-archive](https://github.com/YeOldeInn/agins-archive)@[b2edd8a8b0...](https://github.com/YeOldeInn/agins-archive/commit/b2edd8a8b041c343568b1df424849f243381acb4)
#### Monday 2022-08-08 19:25:56 by T. Joseph Carter

Start work on quests.html

Starting to convert quests.html to HTML5. That caused me to make some
changes to how new.html handles some things … there's going to be a bit
of going back and changing stuff until we get the hang of this, but I
think I'm starting to get the idea of what it should look like now.

It's easy to start putting paragraph text into paragraphs, but a major
thing I haven't decided how to deal with yet is the whole "yeah that
link has been dead for a decade" problem. I fixed it by making a nolink
span that looks like a link. Use it on something that used to be a link
and then do something with the title attribute to explain what needs
explaining. Did that for Dewayne's defunct innkeep@ email. This was a
minor content edit because I turned it into a nolink (which changed its
color) and removed the instructions for how to make the email address
work because … no need for that now.

There's a lot more to do with this since the crazy big ugly quests table
doesn't fit in the 1008 width given a 16px base font. I could change
that since most people use a 12px base font, but I _hate_ pages that do
that, so I'm not going to. No, I can see what's causing the page to be
too long and I'll be addressing that when I get there.

Figuring out how to CSS the ugly-ass GeoCities era table layout was fun.

---
## [BSCPGROUPHOLDINGSLLC/AIDED-LIKE-BERNIE](https://github.com/BSCPGROUPHOLDINGSLLC/AIDED-LIKE-BERNIE)@[30f310476c...](https://github.com/BSCPGROUPHOLDINGSLLC/AIDED-LIKE-BERNIE/commit/30f310476cc7503c5c7a1ba935ec1780ed750382)
#### Monday 2022-08-08 19:31:21 by 1212-5858

$$$$$$ WWW.FINRA.ORG

Under USC 18.225.each person:

'...imprisoned for a term of not less than 10 years and which may be life."

https://github.com/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/TDBANK-WEST57THSTREET-ZIPCODE-10019/find/main
https://github.com/BSCPGROUPHOLDINGSLLC/WILSON-ELSER-DICKER-LASKOWITZ-MOV/find/8209-filed
https://github.com/BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER/blob/BSCPGROUPHOLDINGSLLC-EMAIL-DOCKETS/ms-pwc-dicker


FOR INVASION OF PRIVACY AS WELL WAS UNCONSENTED AS ANNEXED "CEASE AND DESIST" NYSCEF 153974/2020

THANK YOU FOR THE "CASUAL REVIEW" AND TO THE FDIC FOR POSTING ME IN CONCURRENCE OF THOSE ASSETS MOVED UNDER THE AUSPICE OF THE OCC.TREAS.GOV AS OF JUNE 29TH, 2022



AUGUST 8TH, 2022

To whom this may concern,

    THE INFORMATION CONTAINED HEREIN IS CLEARLY THE OBJECCT OF ATTRACTION BY AND BETWEEN SEVERAL DEPARTMENT OF THE USDOJ WHO ARE IN FACT INVESTIGATING THE INDIVIDUALS AND PRINCIPLES OF THOSE ENTITIES WHO ARE RESPONSIBLE FOR A LAUNDRY LIST AS ENTITIES AND PERSONS WHO LED THEMSELVES INTO A COMBINE OF VIOLATIONS UNDER THE USC CODE, TAX CODE, AND HAVE ALSO ANNEXED AND FILED THEIR VIOLATION UNDER THE SECURITIES AND EXCHANGE ACT.


THE ZUCKERS AND THEIR ENTERPRISES, have avoided prosecution ,in fact prior to August 4th, 2022.
 - but thank you for checking in, DOCKET 309, nyscef 153974/2020, and in a high-fashion.

STATE FARM LIFE INSURANCE COMPANY

UNDER THE SCOPE OF THE PLAINTIFF, LITERALLY.
- subjugated AND AT THE COMPROMISE OF CIK FILER 93715, WHEREBY DIRECTORS FILED THEIR USC TITLE 18.215 PAYMENTS VOTED ON, KNOWN AND RECEIVED AS DIRECTORS OF CRD MEMBER 43036, AND ALSO " STATE FARM LIFE INSURANCE COMPANY " AND UNDER TICKERS OF FAMILY 4: STFGX.



https://github.com/BSCPGROUPHOLDINGSLLC/AIDED-LIKE-BERNIE/raw/main/2020_05_27%20-%20INDEX%20and%20PAPERS.pdf

^ THAT REFERENCE.     IS THE REFERENCE OF GREATEST VALUE, COVERS THE SCOPE OF CONVERSATIONS
- USC TITLE 18.1952 VIOLATIONS, AND IN BOLD ***** BELOW, ET. AL.
 
*****

[ USC Title 18.225, USC Title 18.215, USC Title 18.21, USC Title 18.2 ]

Each person as Participants in NYSCEF matter 153974/2020
   

    '...imprisoned for a term of not less than 10 years and which may be life."

https://github.com/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/TDBANK-WEST57THSTREET-ZIPCODE-10019/find/main

https://github.com/BSCPGROUPHOLDINGSLLC/WILSON-ELSER-DICKER-LASKOWITZ-MOV/find/8209-filed

https://github.com/BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER/blob/BSCPGROUPHOLDINGSLLC-EMAIL-DOCKETS/ms-pwc-dicker
   

*****


THANK YOU FOR THE "CASUAL REVIEW" AND TO THE FDIC FOR POSTING ME IN CONCURRENCE OF THOSE ASSETS MOVED UNDER
    
        THE AUSPICE OF THE *@OCC.TREAS.GOV AS OF JUNE 29TH, 2022
 
 /S/ BO DINCER.    ).
 
    MAC. 646-256-3609
    TMO. 917-378-3467


-------- Forwarded Message --------
Subject: 	``Paperwork Reduction Act of 1995'' --> Solomon, David M. “Corporate Governance.” .
Date: 	Mon, 8 Aug 2022 14:06:17 -0500
From: 	B D2022 <ms60710444266@yahoo.com>
To: 	Andrew Keller [FINRA] <akeller106@bloomberg.net>, Andrew Korb [FINRA] <akorb1@bloomberg.net>, Austin McCrary [FINRA] <amccrary@bloomberg.net>, ASHLEY MEAD [FINRA] <amead11@bloomberg.net>, Andrew Smith [FINRA] <asmith1151@bloomberg.net>, Anthony Walker [FINRA] <awalker231@bloomberg.net>, Cassandra Kirk [FINRA] <ckirk21@bloomberg.net>, Chris Gursky [FINRA] <csgursky@bloomberg.net>, Dian Zhu [FINRA] <dian.zhu@finra.org>, FINRA Corporate Notification <finracorporatenotification@finra.org>, FINRA Product Management <finraproductmanagement@finra.org>, finrawebmaster@finra.org <finrawebmaster@finra.org>, FINRA CAT Helpdesk <help@finracat.com>, hesham.ibrahim@finra.org, iard@finra.org, Jessica.Brach@finra.org, Josephine.Vella@finra.org <Josephine.Vella@finra.org>, John Sagan [FINRA] <jsagan8@bloomberg.net>, Joshua Wong [FINRA] <jwong554@bloomberg.net>, Kimberly Berry [FINRA] <k28826@bloomberg.net>, Kenneth Thompson [FINRA] <kthompson84@bloomberg.net>, michelle.ong@finra.org, nancy.condon@finra.org, pfrdsupport@finra.org, Finra Webmaster <postmaster@finra.org>, ray.pellecchia@finra.org, rosalyn.marcus@finra.org <rosalyn.marcus@finra.org>, Rosinna Rivera [FINRA] <rrivera88@bloomberg.net>, TRACE Data Services <tracedataservices@finra.org>, Finra Webmaster <webmaster@finra.org>


https://github.com/BSCPGROUPHOLDINGSLLC/AIDED-LIKE-BERNIE/find/main

keyword: bain


*Solomon, David M. “Corporate Governance.” Code of Business Conduct and Ethics, Goldman Sachs, https://www.goldmansachs.com/investor-relations/corporate-governance/. **
*

To cultivate a diverse workforce, we must draw on the largest possible pool of potential team members. We seek to attract
and retain a diverse network of people from across the globe who bring with them a wide range of backgrounds, cultures,
perspectives and experiences.


As noted throughout, it’s the responsibility of every individual at the firm to escalate potential legal, regulatory, and ethical
breaches, including violations of this Code as well as our core values and our Business Principles. This includes any
instances of retaliation. The firm strictly prohibits retaliation against anyone who in good faith reports a possible
violation, no matter who the report involves.
Paperwork Reduction Act of 1995''

 To further the goals of the Paperwork Reduction Act to have Federal
 agencies become more responsible and publicly accountable for reducing
      the burden of Federal paperwork on the public, and for other
              purposes. <<NOTE: May 22, 1995 -  [S. 244]>>

    Be it enacted by the Senate and House of Representatives of the
United States of America in Congress <<NOTE: Paperwork Reduction Act of
1995. Information resources management.>> assembled,

SECTION 1. <<NOTE: 44 USC 101 note.>> SHORT TITLE.

    This Act may be cited as the ``Paperwork Reduction Act of 1995''.

SEC. 2. COORDINATION OF FEDERAL INFORMATION POLICY.

    Chapter 35 of title 44, United States Code, is amended to read as
follows:

        ``CHAPTER 35--COORDINATION OF FEDERAL INFORMATION POLICY

``Sec.
``3501. Purposes.
``3502. Definitions.
``3503. Office of Information and Regulatory Affairs.
``3504. Authority and functions of Director.
``3505. Assignment of tasks and deadlines.
``3506. Federal agency responsibilities.
``3507. Public information collection activities; submission to
           Director; approval and delegation.
``3508. Determination of necessity for information; hearing.
``3509. Designation of central collection agency.
``3510. Cooperation of agencies in making information available.
``3511. Establishment and operation of Government Information Locator
           Service.
``3512. Public protection.
``3513. Director review of agency activities; reporting; agency
           response.
``3514. Responsiveness to Congress.
``3515. Administrative powers.
``3516. Rules and regulations.
``3517. Consultation with other agencies and the public.
``3518. Effect on existing laws and regulations.
``3519. Access to information.
``3520. Authorization of appropriations.

``Sec. 3501. Purposes

    ``The purposes of this chapter are to--
            ``(1) minimize the paperwork burden for individuals, small
        businesses, educational and nonprofit institutions, Federal
        contractors, State, local and tribal governments, and other
        persons resulting from the collection of information by or for
        the Federal Government;
            ``(2) ensure the greatest possible public benefit from and
        maximize the utility of information created, collected, main

[[Page 109 STAT. 164]]

        tained, used, shared and disseminated by or for the Federal
        Government;
            ``(3) coordinate, integrate, and to the extent practicable
        and appropriate, make uniform Federal information resources
        management policies and practices as a means to improve the
        productivity, efficiency, and effectiveness of Government
        programs, including the reduction of information collection
        burdens on the public and the improvement of service delivery to
        the public;
            ``(4) improve the quality and use of Federal information to
        strengthen decisionmaking, accountability, and openness in
        Government and society;
            ``(5) minimize the cost to the Federal Government of the
        creation, collection, maintenance, use, dissemination, and
        disposition of information;
            ``(6) strengthen the partnership between the Federal
        Government and State, local, and tribal governments by
        minimizing the burden and maximizing the utility of information
        created, collected, maintained, used, disseminated, and retained
        by or for the Federal Government;
            ``(7) provide for the dissemination of public information on
        a timely basis, on equitable terms, and in a manner that
        promotes the utility of the information to the public and makes
        effective use of information technology;
            ``(8) ensure that the creation, collection, maintenance,
        use, dissemination, and disposition of information by or for the
        Federal Government is consistent with applicable laws, including
        laws relating to--
                    ``(A) privacy and confidentiality, including section
                552a of title 5;
                    ``(B) security of information, including the
                Computer Security Act of 1987 (Public Law 100-235); and
                    ``(C) access to information, including section 552
                of title 5;
            ``(9) ensure the integrity, quality, and utility of the
        Federal statistical system;
            ``(10) ensure that information technology is acquired, used,
        and managed to improve performance of agency missions, including
        the reduction of information collection burdens on the public;
        and
            ``(11) improve the responsibility and accountability of the
        Office of Management and Budget and all other Federal agencies
        to Congress and to the public for implementing the information
        collection review process, information resources management, and
        related policies and guidelines established under this chapter.


        Sergey Aleynikov, a 40-year-old former Goldman Sachs programmer, was found guilty on Friday by a federal jury in Manhattan of stealing proprietary source code from the bank’s high-frequency trading platform.
        He was convicted on two counts theft of trade secrets and transportation of stolen property and faces up to 10 years in prison.


During the two-week trial, Judge Denise L. Cote closed the courtroom to the public several times to protect Goldman’s proprietary source code. Yet several details emerged about the firm’s high-frequency trading business, including that the unit accounted for about $300 million in revenue last year, less than 1 percent of Goldman’s total revenue of $45 billion.

On the evening of July 3, 2009, six agents from the Federal Bureau of Investigation met Mr. Aleynikov as he landed at Newark International airport and arrested him.

Mr. Aleynikov remains free on bail but because he holds dual United States and Russian citizenship, the judge placed him under home confinement and electronic monitoring until his sentencing, which is set for March 18.

A version of this article appears in print on Dec. 11, 2010, Section B, Page 1 of the New York edition with the headline: Wall St. Programmer Guilty of Code Theft.

 United States Attorney Southern District of New York

 Manhattan U.S. Attorney PREET BHARARA said: "Protecting the proprietary information of America’s companies is critically important. Today’s sentence sends a clear message that professionals like Sergey Aleynikov who abuse their positions of trust to steal confidential business information from their employers will be prosecuted and punished."

 /S/ BO DINCER.    ).
MAC. 646-256-3609
TMO. 917-378-3467

Under USC 18.225.each person:

*'...imprisoned for a term of not less than 10 years and which may be life."*

https://github.com/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/TDBANK-WEST57THSTREET-ZIPCODE-10019/find/main

https://github.com/BSCPGROUPHOLDINGSLLC/WILSON-ELSER-DICKER-LASKOWITZ-MOV/find/8209-filed

https://github.com/BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER/blob/BSCPGROUPHOLDINGSLLC-EMAIL-DOCKETS/ms-pwc-dicker


FOR INVASION OF PRIVACY AS WELL WAS UNCONSENTED AS ANNEXED "CEASE AND DESIST" NYSCEF 153974/2020

---
## [CoolITSystemsInc/libmodbus](https://github.com/CoolITSystemsInc/libmodbus)@[6f915d4215...](https://github.com/CoolITSystemsInc/libmodbus/commit/6f915d4215c06be3c719761423d9b5e8aa3cb820)
#### Monday 2022-08-08 19:42:04 by Stéphane Raimbault

Fix my so stupid fix for VD-1301 vulnerability

I can't believe I committed that copy/paste mistake.
Sorry Maor Vermucht and Or Peles, excepted naming your original
patch was OK.

Thank you Karl Palsson for your review.

---
## [Tadavomnism/TadaPress](https://github.com/Tadavomnism/TadaPress)@[3711e2e2fb...](https://github.com/Tadavomnism/TadaPress/commit/3711e2e2fbd0ab129515113d4cf4dafa8211f9f2)
#### Monday 2022-08-08 20:43:17 by behrad.b

xxx bloody hell xxx 

My decent implementation turned into a crazy one again... 
Who the fuck can debug this shit mate...?

Totally disappointed :/

=+=+=+=+=+=+=+=+=+=+

Side note:

I did make a change to commented rule-checkers :
Used #ifdef $endif

---
## [Bcadren/crawl](https://github.com/Bcadren/crawl)@[382b2003e1...](https://github.com/Bcadren/crawl/commit/382b2003e14a95f5ace85af2cf6a2b2e06ec686f)
#### Monday 2022-08-08 21:09:53 by advil

Disallow evoking lamp/phial while confused

These two are almost the last remaining holdover of evocables that could
be used while confused. (I notice that tremorstones also work.) These
silently applied target fuzzing (see 657136525ae) in this case; if these
were to be usable while confused in modern crawl, I think they would
need to indicate to the player somehow what might happen. I ran across
this in a crash where an extremely desparate player was constricted and
chain-confused by golden eyes tried to target the constricting naga with
the phial, and fuzzing cause the wave to go the other direction and hit
a friendly demon. Luckily for this player, the game crashed during
knockback on the demon.

See cccf84277269a for wands, and 6178f7666a6f for rods. Unlike these
cases, I do think it's possible that lamp/phial might not be completely
useless with fuzzed targeting, so I wouldn't be opposed to bringing this
back if someone can solve the UI problem.

---
## [0x3C50/Index](https://github.com/0x3C50/Index)@[60a98d0984...](https://github.com/0x3C50/Index/commit/60a98d098460250cbb8ae0eac223aa6bbff874a5)
#### Monday 2022-08-08 21:41:14 by 0x3C50

shit i was too slow i wanted to format the damn thing in the old pull req shit im sorry

---
## [Buildstarted/linksfordevs](https://github.com/Buildstarted/linksfordevs)@[435e0ad2ad...](https://github.com/Buildstarted/linksfordevs/commit/435e0ad2ad6b66e4c22f57c4e3d5a6ebdd93407f)
#### Monday 2022-08-08 23:05:30 by Ben Dornis

Updating: 8/8/2022 11:00:00 PM

 1. Added: On being a staff engineer
    (https://mhlakhani.com/blog/2022/08/on-being-a-staff-engineer/)
 2. Added: 5G Home Broadband
    (https://www.damow.net/5g-home-broadband/)
 3. Added: My knowledge management system
    (https://blog.asadjb.com/my-knowledge-management-system)
 4. Added: Run Linux on Electric Objects EO1 Wall Computer
    (https://charlieharrington.com/run-linux-on-electric-objects-eo1-wall-computer/)
 5. Added: You Belong Here
    (https://jpetazzo.github.io/2022/06/30/you-belong-here/)
 6. Added: From roots to polynomials
    (http://blog.pkh.me/p/31-from-roots-to-polynomials.html)
 7. Added: Announcing: MiniRust
    (https://www.ralfj.de/blog/2022/08/08/minirust.html)
 8. Added: The Reason why Linux Gaming is so limited
    (https://blog.m5e.de/post/the-reason-why-linux-gaming-is-so-limited/)
 9. Added: Module Three – ZK Whiteboard Sessions
    (https://zkhack.dev/whiteboard/module-three/)
10. Added: JIMMY
    (https://jlongster.com/my-low-friction-publishing-workflow)
11. Added: I am not that hacker you are looking for
    (https://0ut3r.space/2022/08/08/i-am-not/)
12. Added: New for PowerShell: 'Get-WhatsNew' Cmdlet, VS Code Tool Update -- Visual Studio Magazine
    (https://visualstudiomagazine.com/articles/2022/08/08/powershell-new.aspx)
13. Added: Debugging bare-metal STM32 from the seventh level of hell
    (https://jpieper.com/2022/08/05/debugging-bare-metal-stm32-from-the-seventh-level-of-hell/)

Generation took: 00:05:18.9174766
 Maintenance update - cleaning up homepage and feed

---
## [BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER](https://github.com/BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER)@[0b1b2b98a7...](https://github.com/BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER/commit/0b1b2b98a7adb2e24b5bf89ca97c237fd4ba5868)
#### Monday 2022-08-08 23:20:36 by 1212-5858

From: 	Knight, Tim (Advisory) <Tim.Knight@KPMG.co.uk>




-------- Forwarded Message --------
Subject: 	Automatic reply: [EXTERNAL] LOST -852, 029, 489.38 ALREADY. ... NYSE, TICKER "MS" = PROMOTER | PRIYA ALSO?
Date: 	Wed, 13 Apr 2022 03:12:16 +0000
From: 	Knight, Tim (Advisory) <Tim.Knight@KPMG.co.uk>
To: 	B D2022 <ms60710444266@yahoo.com>


Apologies - I am on leave until after Easter.

If you need to reach me urgently, please SMS me on 07812 022538.

If not, I'll read your note on 19th April.

Very best,

 

Tim

 


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
This email has been sent by and on behalf of one or more of KPMG LLP, KPMG Audit plc, KPMG Resource Centre Private Limited or a company under the control of KPMG LLP, including KPMG United Kingdom plc and KPMG UK Limited (together, "KPMG"). This email, and any attachments, is confidential and may be privileged or otherwise protected from disclosure. It is intended solely for the stated addressee(s) and access to it by any other person is unauthorised. If you are not the intended recipient, you must not disclose, copy, circulate or in any other way use or rely on the information contained herein. If you have received this email in error, please inform us immediately and delete all copies of it. Any communications made with KPMG may be monitored and a record may be kept of any communication. Any opinion or advice contained herein is subject to the terms and conditions set out in your KPMG LLP client engagement letter.
A list of members of KPMG LLP is open for inspection at KPMG's registered office.
KPMG LLP (registered no. OC301540) is a limited liability partnership registered in England and Wales. Each of KPMG Audit plc (registered no. 03110745), KPMG United Kingdom plc (registered no. 03513178) and KPMG UK Limited (registered no. 03580549) are companies registered in England and Wales. Each entity's registered office is at 15 Canada Square, London, E14 5GL.
For full details of our professional regulation please refer to https://home.kpmg/uk/en/home/misc/regulatory-information.html


To understand how we respect and protect your personal data, please see our online privacy policy at www.kpmg.co.uk/privacy.　To opt-out of marketing communications from KPMG in the UK, please email KPMGunsubscribe@kpmg.co.uk


♘   (risc@ic.fbi.gov) 👔   (leb@fbi.gov)  👔   50074  👔   RECEIPT  👔  90849565    ♔
♘   (OGIS@NARA.GOV)   👔  (CShugg@sylint.com)  👔     👔     👔     ♕    
👔   (SLASKOWITZ@INGRAMLLP.COM) 👔   (LZUCKER@MSKYLINE.COM)  👔   (LEGAL@MSKYLINE.COM)  👔   (ADMINISTRATION@MSKYLINE.COM)  👔 (ADMINISTRATOR@MSKYLINE.COM)    ♔♕ 

https://github.com/BSCPGROUPHOLDINGSLLC/AIDED-LIKE-BERNIE/raw/main/2020_05_27%20-%20INDEX%20and%20PAPERS.pdf

UNDER THE SCOPE OF THE PLAINTIFF, LITERALLY.
- subjugated the decision(s) of STATE FARM LIFE INSURANCE BY IMPEDING A TIMELY RELEASE OF INFORMATION FILED IN NYSCEF 153974/2020
- AND AT THE COMPROMISE OF CIK FILER 93715.
^ WHEREBY DIRECTORS FILED THEIR USC TITLE 18.215 PAYMENTS VOTED ON, KNOWN AND RECEIVED AS DIRECTORS OF CRD MEMBER 43036, 
^ AND ALSO " STATE FARM LIFE INSURANCE COMPANY " AND UNDER TICKERS OF FAMILY 4: STFGX LOST THE GREATER OF 10% IN A SINGLE TRADING SESSION.




https://github.com/BSCPGROUPHOLDINGSLLC/AIDED-LIKE-BERNIE/raw/main/2020_05_27%20-%20INDEX%20and%20PAPERS.pdf

^ THAT REFERENCE.     IS THE REFERENCE OF GREATEST VALUE, COVERS THE SCOPE OF CONVERSATIONS
- USC TITLE 18.1952 VIOLATIONS, AND IN BOLD ***** BELOW, ET. AL.
 
*****

[ USC Title 18.225, USC Title 18.215, USC Title 18.21, USC Title 18.2 ]

Each person as Participants in NYSCEF matter 153974/2020
   

    '...imprisoned for a term of not less than 10 years and which may be life."

THANK YOU FOR THE "CASUAL REVIEW" AND TO THE FDIC FOR POSTING ME IN CONCURRENCE OF THOSE ASSETS MOVED UNDER 
	
		THE AUSPICE OF THE *@OCC.TREAS.GOV AS OF JUNE 29TH, 2022
		
 *** see also. Random $9000 audit by PWC for filer 93715, 
				to file their KNOWN problems then by CIK filer 93715 and into CIK filer 1516523.'
				## STILL HOLDS THOSE PAPERS.. CAN'T TERMINATE UNTIL THE TAXES ARE " PAID IN FULL "
				## ALL SIX-PROPERTIES, AND A LETTER FROM ANY FEDERAL REGULATOR WOULD BE WHAT IS A "CALL" 
				## FROM THE ISSUER OF ALL THAT MONEY IN ONE PAGE, AND IMPOSES THE SAME LEVERAGE STAKES AT ANY CUSTODIAN.
    
 /S/ BO DINCER.	).
 
	MAC. 646-256-3609
	TMO. 917-378-3467

mailbox BSCPGROUPHOLDINGSLLC/2021-DUCKER-ZUCKER#1



# HUB :: WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/TDBANK-WEST57THSTREET-ZIPCODE-10019/

https://github.com/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/TDBANK-WEST57THSTREET-ZIPCODE-10019/find/main

# HUB :: WILSON-ELSER-DICKER-LASKOWITZ-MOV/

https://github.com/BSCPGROUPHOLDINGSLLC/WILSON-ELSER-DICKER-LASKOWITZ-MOV/find/8209-filed

# HUB :: WILSONELSER-ZUCKER/

https://github.com/BSCPGROUPHOLDINGSLLC/WILSONELSER-ZUCKER/find/MSGFILES

https://github.com/BSCPGROUPHOLDINGSLLC/WILSONELSER-ZUCKER/find/VIDEOTAPED-DISTRIBUTED

https://github.com/BSCPGROUPHOLDINGSLLC/WILSONELSER-ZUCKER/tree/main

# HUB :: ELSER-AND-DICKER

https://github.com/BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER/

https://github.com/BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER/find/1.6662ACCURACY-RELATED-PENALTY

https://github.com/BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER/find/2020-11-20-FILER0000093715

https://github.com/BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER/find/REQUEST-TO-BAR

https://github.com/BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER/find/Assessments

https://github.com/BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER/find/153974-PHOTOGRAPHS

https://github.com/BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER/find/FTC-SHERMAN

https://github.com/BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER/find/BATCH1-Q00001

https://github.com/BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER/find/AVOIDANCE-of-PROSECUTION

https://github.com/BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER/find/BSCPGROUPHOLDINGSLLC-EMAIL-DOCKETS

https://github.com/BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER/find/CRYSTAL-IBC-LLC
* USC 18 TITLE 18- SECTION 1512 - PREVENTING COMMUNICATION TO A LAW ENFORCEMENT OFFICER OR JUDGE
* USC 18 TITLE 03- SECTION 0003 - ACCESSORY AFTER THE FACT 
* FIRM# 8209, SARBANAS-OXLEY 40' ACT VIOLATIONS
* UNLAWFUL RENTS AND SUPPLEMENTS FOR CONVENIENCE. JP MORGAN CHASE, NA.
** "NOT A MATTER OF SECURITIES LAW"
** (PUBLICINFO@FDIC.GOV) INFORMATION REQUESTED. State Farm Losses are >> GREATER THAN $1.5 Billion USD
*** FOLDER 1, FILED IN 153974_2020 BY B. DINCER.
*** § 1.6662-2 Accuracy-related penalty.
*** SARBANAS-OXLEY VIOLATED
*** hq NYSE: MS: [200] swaps | isda ***1516523 ***NOTARIZED ***May 11, 2020. |||


https://github.com/BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER/find/BSCPGROUPHOLDINGSLLC-patch-112
* FILED UNDER THE INCORRECT ZIPCODE IN NYSCEF 153974/2020 
* CONTINUED TO FILE TO KEEP ME PRE-OCCUPIED IN NYSCEF 153974/2020
* I JUST FILED EVERYTHING DIRECTLY WITH THE NY SUPREME COURT THEN INSTEAD.
** FOR STARTERS, THEY UNDER USC TITLE 18.3, 
*** USC 18 TITLE 18- SECTION 1512 - PREVENTING COMMUNICATION TO A LAW ENFORCEMENT OFFICER OR JUDGE
*** ACRIS $6M + insider trading PROSECUTION ( 20 years minimum )
*** NEW CONSUMER CASE NOTIFICATIONS UNDER THE PUBLICINFO@FDIC.GOV LINKS
*** OFCCP, CSC SSP WAIVERS, AND DOC NOTICES


 
### $9000.00 AUDIT WAS A "SURPRISE DISCOUNT" BY CHANCE PROVES THAT ' PWC ' KNEW ' SOMETHING WAS GOING ON '

https://github.com/BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER/blob/BSCPGROUPHOLDINGSLLC-EMAIL-DOCKETS/ms-pwc-dicker
   

*****
CIK FILER 93715 ITNO CIK FILER 1516523
#MAKESMALLBIGGER
^ 1 REFERENCE <br>
https://github.com/BSCPGROUPHOLDINGSLLC/AIDED-LIKE-BERNIE/raw/main/2020_05_27%20-%20INDEX%20and%20PAPERS.pdf
# FEDERAL FILE FINDERS
^	UNDER THE PAPERWORK REDUCTION ACT OF 1995
 👔
 
 FAX CONFIRM TO THE COURT MATTER NYSCEF 153974_2020 [USC 18 §21, USC 18 §225, USC 18 §2, USC 18 §1962]

---

