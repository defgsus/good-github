## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-07-12](docs/good-messages/2022/2022-07-12.md)


1,753,667 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,753,667 were push events containing 2,615,146 commit messages that amount to 200,740,476 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 28 messages:


## [Cassumbra/zombies_gold](https://github.com/Cassumbra/zombies_gold)@[d5a77212e8...](https://github.com/Cassumbra/zombies_gold/commit/d5a77212e898ba337616426f945cf5415878bd78)
#### Tuesday 2022-07-12 00:18:39 by Cassumbra

stupid stupid stupid stupid stupid doesnt fucking work stupid idiot dumbass can't fucking do anything

fuck fuck fuck fuck fuck fuck fuck

---
## [andro951/WeaponEnchantments](https://github.com/andro951/WeaponEnchantments)@[4b4a140890...](https://github.com/andro951/WeaponEnchantments/commit/4b4a14089022330623d3ce62c3e0e6e737724211)
#### Tuesday 2022-07-12 00:23:04 by andro951

0.2.1.13(11JUL22)
     -Made "Automatically send essence to the enchanting table" on by default.
     -Fixed Removing All for one from an item not properly restoring an item's autoReuse.(@Bibbler-sama)
     -World Ablaze now allowed on all weapons instead of magic only.
     -Fixed boss summon items going up by 1 when consumed with War and Calamity installed.(@Bibbler-sama)
     -Limited the base armor penetration bonus damage to 50 damage from base armor penetration (Armor Penetration from enchantments is not affected by this limitation)
The reason for this limitation is because of items such as "Bury The Light" from Stars Above that has a base armor penetration of 9999 which would give 5000 damage.
     -Added a few error messages to show up in game instead of just the client.log to assist with troubleshooting.
     -fixed size enchantment hixboxes being too far down and to the right.(@CTien, @Lonely )
     -Added config option to offer all of the same type of item (If their experience is 0 and no power booster installed).
          Ex: Offer a shackle with 4 shackles in your inventory, it will offer all 5 shackles by offering one of them.(@Synap)
     -Added the ability to favorite essence (same way you do with favoriting items in your inventory) to prevent them being consumed by Level Up.  If You don't have enough essence to level up with non-favorited essence, but you do including favorited essence, it will ignore the favorites and will consume them as it normally would with no favorites.  (It also does this if they are all favorited) (@Grannom, @SemperAnte and @JoeDolca )
     -Fixed enchantments not updating when swapping players with the playerSwapper mod.(Zen Roshan)
     -Adjust which ores are received when offering items.  Allow ores up to and including Chlorophyte(@JoeDolca)
          This is a config option enabled by default.
     -Fixed bug causing your stack of essence in your inventory to be reduced by double the amount it was supposed to be when opening the enchanting table if the total essence (inventory + enchanting table) was greater than max stack (9999)(@Lonely)

---
## [ayoni02/alx-system_engineering-devops](https://github.com/ayoni02/alx-system_engineering-devops)@[9cd2c6a979...](https://github.com/ayoni02/alx-system_engineering-devops/commit/9cd2c6a979e6c88435e8db72f20fcf2a1b90b4dd)
#### Tuesday 2022-07-12 00:37:04 by Ayoni

 Diana, possesses a high resistance to damage and magical attacks. Her resistance to injury is not quite as great as any of the above mentioned metahumans. However, due to her vast threshold for pain and her amazon ability to heal at a superhuman rate, this easily makes up for the difference. She has withstood considerable bludgeoning damage in the form of hand to hand combat with metahuman opponents such as Superman and Captain Marvel. She has considerable resistance to human weaponries,though this is not absolute; Bullets can cause minor to moderate injury, but never life threatening. And her ability to heal rapidly, makes up for this set back. She can easily survive under extreme pressures, cold, and heat. Wonder Woman has been able to traverse space, undergo submergence into lava, and withstand a direct explosion from a nuclear warhead unharmed. Born of the clay of Themyscira, and given life and divine powers by the gods themselves, Diana has heightened resistance to magical attacks. She is highly experienced in battling foes who use sorcery as a weapon. As a divine creation herself, she is far-less susceptible to manipulation by magic and men
kkkkkkkkkkkkkkkkkkkkkkkkkkkkk
lll

---
## [coreyja/battlesnake-rs](https://github.com/coreyja/battlesnake-rs)@[2864e03db5...](https://github.com/coreyja/battlesnake-rs/commit/2864e03db5ebdc5cb38d30dda2576c9fe935b3a1)
#### Tuesday 2022-07-12 00:46:55 by Corey Alexander

Oh shit, no wonder the benchmarks looked like the start of game metrics :facepalm:

---
## [Comxy/tgstation](https://github.com/Comxy/tgstation)@[707fbfac7e...](https://github.com/Comxy/tgstation/commit/707fbfac7e11837865d70587011aa8197b1d0c35)
#### Tuesday 2022-07-12 00:59:48 by san7890

[MDB Ignore] Shifts all (sane) varedited signs to directionals  (#68004)

* [MDB Ignore] Shifts all (sane) varedited signs to directionals

Hey there,

So we have these cool new sign directionals now, but we still have all of the old pixel-shifted pre-fabrications lying around. So, I added an UpdatePaths (as well as Updated the Paths) to be a bit better at using directionals, because directionals are pretty neato.

This should update every single var_edit that used the proper 32 pixelshift (some of them used 28, and I'm unable to account for that automatically with current tooling) into a proper subtype. Mappers tend to learn by looking at well established maps, so it's always important to ensure that the well-established maps use the most recent tooling (i.e.: bring them up to the surface) and avoid needless excess lines in maps.

* The Commit With All The Maps

OH GOD OH FUCK

* Renames the UpdatePaths

---
## [IceSentry/bevy](https://github.com/IceSentry/bevy)@[4847f7e3ad...](https://github.com/IceSentry/bevy/commit/4847f7e3adc835053a8907dd578c342b4bd395e2)
#### Tuesday 2022-07-12 01:00:45 by ira

Update codebase to use `IntoIterator` where possible. (#5269)

Remove unnecessary calls to `iter()`/`iter_mut()`.
Mainly updates the use of queries in our code, docs, and examples.

```rust
// From
for _ in list.iter() {
for _ in list.iter_mut() {

// To
for _ in &list {
for _ in &mut list {
```

We already enable the pedantic lint [clippy::explicit_iter_loop](https://rust-lang.github.io/rust-clippy/stable/) inside of Bevy. However, this only warns for a few known types from the standard library.

## Note for reviewers
As you can see the additions and deletions are exactly equal.
Maybe give it a quick skim to check I didn't sneak in a crypto miner, but you don't have to torture yourself by reading every line.
I already experienced enough pain making this PR :) 


Co-authored-by: devil-ira <justthecooldude@gmail.com>

---
## [RomanRenders/mern-expenses-app](https://github.com/RomanRenders/mern-expenses-app)@[5651a8e719...](https://github.com/RomanRenders/mern-expenses-app/commit/5651a8e719d6878842abbf8b0b17b167fbce6ac7)
#### Tuesday 2022-07-12 02:05:10 by Roman Navarro

WHY WONT THIS STUPID FUCKING SHIT WORK I FUCKING PASTED ALL THIS KIKE SHIT OVER AND NOTHING EVER FUCKING WORKS FML FUCK KIKES

---
## [VoidUI-Devices/kernel_xiaomi_sm8250](https://github.com/VoidUI-Devices/kernel_xiaomi_sm8250)@[cb0941d07d...](https://github.com/VoidUI-Devices/kernel_xiaomi_sm8250/commit/cb0941d07dc7a80a626d88c8666c4703c853ed7b)
#### Tuesday 2022-07-12 02:36:00 by George Spelvin

lib/list_sort: optimize number of calls to comparison function

CONFIG_RETPOLINE has severely degraded indirect function call
performance, so it's worth putting some effort into reducing the number
of times cmp() is called.

This patch avoids badly unbalanced merges on unlucky input sizes.  It
slightly increases the code size, but saves an average of 0.2*n calls to
cmp().

x86-64 code size 739 -> 803 bytes (+64)

Unfortunately, there's not a lot of low-hanging fruit in a merge sort;
it already performs only n*log2(n) - K*n + O(1) compares.  The leading
coefficient is already at the theoretical limit (log2(n!) corresponds to
K=1.4427), so we're fighting over the linear term, and the best
mergesort can do is K=1.2645, achieved when n is a power of 2.

The differences between mergesort variants appear when n is *not* a
power of 2; K is a function of the fractional part of log2(n).  Top-down
mergesort does best of all, achieving a minimum K=1.2408, and an average
(over all sizes) K=1.248.  However, that requires knowing the number of
entries to be sorted ahead of time, and making a full pass over the
input to count it conflicts with a second performance goal, which is
cache blocking.

Obviously, we have to read the entire list into L1 cache at some point,
and performance is best if it fits.  But if it doesn't fit, each full
pass over the input causes a cache miss per element, which is
undesirable.

While textbooks explain bottom-up mergesort as a succession of merging
passes, practical implementations do merging in depth-first order: as
soon as two lists of the same size are available, they are merged.  This
allows as many merge passes as possible to fit into L1; only the final
few merges force cache misses.

This cache-friendly depth-first merge order depends on us merging the
beginning of the input as much as possible before we've even seen the
end of the input (and thus know its size).

The simple eager merge pattern causes bad performance when n is just
over a power of 2.  If n=1028, the final merge is between 1024- and
4-element lists, which is wasteful of comparisons.  (This is actually
worse on average than n=1025, because a 1204:1 merge will, on average,
end after 512 compares, while 1024:4 will walk 4/5 of the list.)

Because of this, bottom-up mergesort achieves K < 0.5 for such sizes,
and has an average (over all sizes) K of around 1.  (My experiments show
K=1.01, while theory predicts K=0.965.)

There are "worst-case optimal" variants of bottom-up mergesort which
avoid this bad performance, but the algorithms given in the literature,
such as queue-mergesort and boustrodephonic mergesort, depend on the
breadth-first multi-pass structure that we are trying to avoid.

This implementation is as eager as possible while ensuring that all
merge passes are at worst 1:2 unbalanced.  This achieves the same
average K=1.207 as queue-mergesort, which is 0.2*n better then
bottom-up, and only 0.04*n behind top-down mergesort.

Specifically, defers merging two lists of size 2^k until it is known
that there are 2^k additional inputs following.  This ensures that the
final uneven merges triggered by reaching the end of the input will be
at worst 2:1.  This will avoid cache misses as long as 3*2^k elements
fit into the cache.

(I confess to being more than a little bit proud of how clean this code
turned out.  It took a lot of thinking, but the resultant inner loop is
very simple and efficient.)

Refs:
  Bottom-up Mergesort: A Detailed Analysis
  Wolfgang Panny, Helmut Prodinger
  Algorithmica 14(4):340--354, October 1995
  https://doi.org/10.1007/BF01294131
  https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.6.5260

  The cost distribution of queue-mergesort, optimal mergesorts, and
  power-of-two rules
  Wei-Mei Chen, Hsien-Kuei Hwang, Gen-Huey Chen
  Journal of Algorithms 30(2); Pages 423--448, February 1999
  https://doi.org/10.1006/jagm.1998.0986
  https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.4.5380

  Queue-Mergesort
  Mordecai J. Golin, Robert Sedgewick
  Information Processing Letters, 48(5):253--259, 10 December 1993
  https://doi.org/10.1016/0020-0190(93)90088-q
  https://sci-hub.tw/10.1016/0020-0190(93)90088-Q

Feedback from Rasmus Villemoes <linux@rasmusvillemoes.dk>.

Link: http://lkml.kernel.org/r/fd560853cc4dca0d0f02184ffa888b4c1be89abc.1552704200.git.lkml@sdf.org
Signed-off-by: George Spelvin <lkml@sdf.org>
Acked-by: Andrey Abramov <st5pub@yandex.ru>
Acked-by: Rasmus Villemoes <linux@rasmusvillemoes.dk>
Reviewed-by: Andy Shevchenko <andriy.shevchenko@linux.intel.com>
Cc: Daniel Wagner <daniel.wagner@siemens.com>
Cc: Dave Chinner <dchinner@redhat.com>
Cc: Don Mullis <don.mullis@gmail.com>
Cc: Geert Uytterhoeven <geert@linux-m68k.org>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>

---
## [stonea/chapel](https://github.com/stonea/chapel)@[bf1082871e...](https://github.com/stonea/chapel/commit/bf1082871e365ebaebf0057c1793ebcae9e963e7)
#### Tuesday 2022-07-12 02:54:09 by Andy Stone

Merge pull request #19851 from stonea/llvm_check_for_lclang_cpp

Add check to see if libclang-cpp-dev package is installed and ensure missing package errors get to user

I'm trying to install llvm 13 on my desktop to use it as the "system" LLVM when CHPL_LLVM=system.  Anyway, I must have forgotten to install a package because when I build Chapel I get this error:
`/usr/bin/ld: cannot find -lclang-cpp`

I figured out the missing package was: libclang-cpp-dev (after apt-getting it things work fine).
It's a better user experience if we can get printchplenv to guide the user towards installing the necessary packages. I see in chplenv/chpl_llvm.py (in the check_llvm_config function) we have some checking that looks for things like missing include files (due to missing packages) and produces some nice error messages. Unfortunately, these error messages never reach the user, rather you'll get this more confusing error:

`Exception: CHPL_LLVM=system but could not find an installed LLVM with one of the supported versions: 14, 13, 12, 11`

You can reproduce this by running sudo apt remove libclang-dev and running printchplenv. I think this is due to a bug where we produce the error message (and add it to some error log) but never actually report it to the user.

In this PR I fix this so we separate out the check for the presence of llvm_config from the other checks about include files (and now libs) and ensure that we run these checks when we're using the system LLVM.
I also add in the check for missing -lclang_cpp, you'll now get this message if it can't find it:

`Perhaps you need to install the libclang-cpp-dev package`

[Reviewed by @daviditen]

---
## [marcovicci/hnefa](https://github.com/marcovicci/hnefa)@[455eb22de7...](https://github.com/marcovicci/hnefa/commit/455eb22de74db7bc2761d27a13889c9b0c3a15ab)
#### Tuesday 2022-07-12 03:42:28 by marcovicci

Update README.md

Added a new class - Simulator - for making and evaluating theoretical moves on a virtual fake game board. A lot of the code is reused from elsewhere and it's a little silly. But trust me, it will work!\
Added a Board History variable... list... tuple? Whatever it is, it can store current positions of pieces for each team and states of all the cells on the board. In theory, this means the AI will be able to roll back from potential moves and build the board at any state of play using that data. This is used in PieceManager and our new Simulator class.\
Pieces can now be "virtual" so that the movement of simulated pieces won't trigger real game board changes.\
The Jarl will send some information about his states to the Simulator, since this is pretty important to scoring. (Other pieces will also do this, once the emotional system is more present.)\
In general, I'm laying the groundwork for the minimax system we'll be using for AI decisionmaking. Stay tuned for more...

---
## [josh894/SimpleArmory](https://github.com/josh894/SimpleArmory)@[7b781b8af6...](https://github.com/josh894/SimpleArmory/commit/7b781b8af627f20c5bd59c7b3981c777ad4cce28)
#### Tuesday 2022-07-12 04:49:57 by Antoine Pietri

Rework Reputation page UI

The previous design had several issues that made it hard to know what
your concrete progress was for reputations:

- There were red colors even when you had completed a reputation, which
  made it hard to quickly understand at a glance which things weren't
  exalted yet.
- The size of the reputation bars changed depending on the reputation
  tiers. Some special reputations with unusual tiers (Chromie,
  Fisherfriends, Ember Court etc) would have a progress bar with a
  smaller size, which made them stand out.
- There was a horrible hack to special-case the Tillers from MOP to
  properly display their friendship tiers by hardcoding their reputation
  IDs. However, this was partially broken and unusable for different
  tiers.

This commit tries to address these issues by doing several things.

1. Bars all have the same fixed max width. All the different friendship
   tiers make the bar widths automatically adjust as a ratio of
   the maximum reputation attainable.

2. The full bar is always shown, with all the reputation tiers.
   Obtaining reputation just makes the bar increasingly "fill" its
   background color.

3. The bar is now fully colored in the color of the maximum reputation
   attainable. This is easier to the eye, as it is easy to quickly check
   at a glance which reps are not completed yet.

4. Names of reputation tiers are only shown when hovering the individual
   bar segments. The current tier is shown to the right, in the same
   color as the bar itself.

---
## [ZhangY-MSFT/terminal](https://github.com/ZhangY-MSFT/terminal)@[fb597ed304...](https://github.com/ZhangY-MSFT/terminal/commit/fb597ed304ec6eef245405c9652e9b8a029b821f)
#### Tuesday 2022-07-12 05:18:49 by Mike Griese

Add support for renaming windows (#9662)

## Summary of the Pull Request

This PR adds support for renaming windows.

![window-renaming-000](https://user-images.githubusercontent.com/18356694/113034344-9a30be00-9157-11eb-9443-975f3c294f56.gif)
![window-renaming-001](https://user-images.githubusercontent.com/18356694/113034452-b5033280-9157-11eb-9e35-e5ac80fef0bc.gif)


It does so through two new actions:
* `renameWindow` takes a `name` parameter, and attempts to set the window's name
  to the provided name. This is useful if you always want to hit <kbd>F3</kbd>
  and rename a window to "foo" (READ: probably not that useful)
* `openWindowRenamer` is more interesting: it opens a `TeachingTip` with a
  `TextBox`. When the user hits Ok, it'll request a rename for the provided
  value. This lets the user pick a new name for the window at runtime.

In both cases, if there's already a window with that name, then the monarch will
reject the rename, and pop a `Toast` in the window informing the user that the
rename failed. Nifty!

## References
* Builds on the toasts from #9523
* #5000 - process model megathread

## PR Checklist
* [x] Closes https://github.com/microsoft/terminal/projects/5#card-50771747
* [x] I work here
* [x] Tests addded (and pass with the help of #9660)
* [ ] Requires documentation to be updated

## Detailed Description of the Pull Request / Additional comments

I'm sending this PR while finishing up the tests. I figured I'll have time to sneak them in before I get the necessary reviews.

> PAIN: We can't immediately focus the textbox in the TeachingTip. It's
> not technically focusable until it is opened. However, it doesn't
> provide an even tto tell us when it is opened. That's tracked in
> microsoft/microsoft-ui-xaml#1607. So for now, the user _needs_ to
> click on the text box manually.
> We're also not using a ContentDialog for this, because in Xaml
> Islands a text box in a ContentDialog won't recieve _any_ keypresses.
> Fun!

## Validation Steps Performed

I've been playing with 

```json
        { "keys": "f1", "command": "identifyWindow" },
        { "keys": "f2", "command": "identifyWindows" },
        { "keys": "f3", "command": "openWindowRenamer" },
        { "keys": "f4", "command": { "action": "renameWindow", "name": "foo" } },
        { "keys": "f5", "command": { "action": "renameWindow", "name": "bar" } },
```

and they seem to work as expected

---
## [Jul-Lii/android_kernel_xiaomi_sdm845](https://github.com/Jul-Lii/android_kernel_xiaomi_sdm845)@[efa1561b58...](https://github.com/Jul-Lii/android_kernel_xiaomi_sdm845/commit/efa1561b58a408a69c9526ecaa1b5edf1e4aa410)
#### Tuesday 2022-07-12 06:58:33 by Peter Zijlstra

sched/core: Implement new approach to scale select_idle_cpu()

Hackbench recently suffered a bunch of pain, first by commit:

  4c77b18cf8b7 ("sched/fair: Make select_idle_cpu() more aggressive")

and then by commit:

  c743f0a5c50f ("sched/fair, cpumask: Export for_each_cpu_wrap()")

which fixed a bug in the initial for_each_cpu_wrap() implementation
that made select_idle_cpu() even more expensive. The bug was that it
would skip over CPUs when bits were consequtive in the bitmask.

This however gave me an idea to fix select_idle_cpu(); where the old
scheme was a cliff-edge throttle on idle scanning, this introduces a
more gradual approach. Instead of stopping to scan entirely, we limit
how many CPUs we scan.

Initial benchmarks show that it mostly recovers hackbench while not
hurting anything else, except Mason's schbench, but not as bad as the
old thing.

It also appears to recover the tbench high-end, which also suffered like
hackbench.

Tested-by: Matt Fleming <matt@codeblueprint.co.uk>
Signed-off-by: Peter Zijlstra (Intel) <peterz@infradead.org>
Cc: Chris Mason <clm@fb.com>
Cc: Linus Torvalds <torvalds@linux-foundation.org>
Cc: Mike Galbraith <efault@gmx.de>
Cc: Peter Zijlstra <peterz@infradead.org>
Cc: Thomas Gleixner <tglx@linutronix.de>
Cc: hpa@zytor.com
Cc: kitsunyan <kitsunyan@inbox.ru>
Cc: linux-kernel@vger.kernel.org
Cc: lvenanci@redhat.com
Cc: riel@redhat.com
Cc: xiaolong.ye@intel.com
Link: http://lkml.kernel.org/r/20170517105350.hk5m4h4jb6dfr65a@hirez.programming.kicks-ass.net
Signed-off-by: Ingo Molnar <mingo@kernel.org>
Signed-off-by: Raphiel Rollerscaperers <rapherion@raphielgang.org>
Signed-off-by: CloudedQuartz <ravenklawasd@gmail.com>

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[a48d80b988...](https://github.com/mrakgr/The-Spiral-Language/commit/a48d80b988194c017f0687642c9def0ede079801)
#### Tuesday 2022-07-12 07:49:32 by Marko Grdinić

"8:20am. I seem to be really looking forward to finishing the backend. Any mail? Nope.

8:30am. Let me start. I want to get this done. The sooner I am done with the backend, the sooner I can relieve the load it is putting on my mind.

```fs
types.Add("typedef enum {REFC_DECR=0, REFC_INCR=1, REFC_SUPPR=2} REFC_FLAG;")
```

Let me start with this. Instead of adding an extra boolean arg, I will modify the refc argument so it is an enum rather than a mask.

8:40am.

```fs
                    line s_fun "int refc = (x->refc += q & REFC_INCR ? 1 : -1);"
                    line s_fun "if (!(q & REFC_SUPPR) && refc == 0) {"
```

Let me do it like this.

I'll modify all the relevant spots so they use this sort of thing.

8:45am. Ah, fuck. This part is so annoying.

8:50am. Nevermind. Forget flags. I am not confident I can do this without messing it up. I'll just add an extra argument everywhere.

...No, let me try persevering.

9:05pm.

```fs
            line s_fun (sprintf "static inline void %sRefcBody%i(%s * x, REFC_FLAG q){" name i name')
            let _ =
                let s_fun = indent s_fun
                let decref_vars = ResizeArray()
                let decrefs = x.free_vars |> refc_change' (fun (i,t) -> decref_vars.Add($"{tyv t} z{i} = x->v{i};"); $"z{i}") "-1"
                if decrefs.Length <> 0 then
                    decref_vars |> line' s_fun
                    decrefs |> line' s_fun
            line s_fun "}"
```

Found a bug from before. Note how I am using -1 here instead of passing in the count, or q in this case. That would have been hell to track down.

```fs
            line s_fun (sprintf "static inline void %sRefcBody%i(%s * x, REFC_FLAG q){" name i name')
            let _ =
                let s_fun = indent s_fun
                let refc_vars = ResizeArray()
                let refcs = x.free_vars |> refc_change' (fun (i,t) -> refc_vars.Add($"{tyv t} z{i} = x->v{i};"); $"z{i}") "q"
                if refcs.Length <> 0 then
                    refc_vars |> line' s_fun
                    refcs |> line' s_fun
            line s_fun "}"
```

Let me do it like this.

```fs
                let decrefs = x.free_vars |> refc_change (fun i -> $"env.v{i}") "-1"
                if decrefs.Length <> 0 then
                    line s_fun $"ClosureEnv{i} env = x->env[0];"
                    decrefs |> line' s_fun
```

Another place where I am using -1 instead of the given count argument.

9:20am. Putting in a bit of effort here was the right choice as it allowed me to find some bugs that I wouldn't have otherwise.

Now, let me finish this.

```fs
            | TyLocalReturnData(d,trace) ->
                try match ret with
                    | BindsLocal l -> line' s (tup_destruct (l,data_term_vars d))
                    | BindsTailEnd ->
                        data_free_vars |> refc_suppr |> line' s
                        line s $"return {tup_data d};"
```

Here is the first thing I need to change. I've put in a suppress here. Now what I need are tail calls.

9:30am.

```fs
        let jp (a,b') =
            let args = args b'
            match ret with
            | BindsTailEnd -> refc_suppr b' |> line' s
            | BindsLocal _ -> ()
            match a with
            | JPMethod(a,b) -> sprintf "method%i(%s)" (method (a,b)).tag args
            | JPClosure(a,b) -> sprintf "ClosureCreate%i(%s)" (closure (a,b)).tag args
```

Yeah, this is good.

```fs
        let binds a b = binds decref_vars a b
        let return' (x : string) =
            match ret with
            | BindsTailEnd -> line s $"return {x};"
            | BindsLocal [||] -> line s $"{x};"
            | BindsLocal [|L(i,_)|] -> line s $"v{i} = {x};"
            | BindsLocal ret ->
                let tmp_i = tmp()
                line s $"{tup_ty_tyvs ret} tmp{tmp_i} = {x};"
                Array.mapi (fun i (L(i',_)) -> $"v{i'} = tmp{tmp_i}.v{i};") ret |> line' s
        let layout_index (x'_i : int) (x' : TyV []) =
            let gs = Array.map (fun (L(i',_)) -> $"v{x'_i}->v{i'}") x'
            match ret with
            | BindsTailEnd ->
                let gs = String.concat ", " gs
                let tys = tyvs_to_tys x'
                if tys.Length <= 1 then $"return {gs};" else $"return Tuple{(tup tys).tag}({gs});"
                |> line s
            | BindsLocal x ->
                Array.map2 (fun (L(i,_)) g -> $"v{i} = {g};") x gs |> line' s
```

I've put in so much effort into doing the tail ends, but it turns out that won't even be necessary anymore.

Now what I need to do is go into method and closure constructors and incref the domain args. After that I will be done with Spiral's codegen.

```fs
and binds_start (args : TyV []) (s : CodegenEnv) (x : TypedBind []) = binds (refc_decref_vars (Set args) x) s BindsTailEnd x
```

In fact, I can just do that in `binds_start`. That is the ideal place to do it.

```fs
    and binds_start (args : TyV []) (s : CodegenEnv) (x : TypedBind []) =
        refc_incr args |> line' s
        binds (refc_decref_vars (Set args) x) s BindsTailEnd x
```

...Ah wait, I've forgotten something after all. If statements and match cases need to be in end position otherwise TCO won't work. I've forgotten those.

```fs
let seq_apply (d: LangEnv) end_dat =
    let inline end_ () = d.seq.Add(TyLocalReturnData(end_dat,d.trace))
    if d.seq.Count > 0 then
        match d.seq.[d.seq.Count-1] with
        | TyLet(end_dat',a,(TyJoinPoint _ | TyIf _ | TyIntSwitch _ | TyUnionUnbox _) & b) -> d.seq.[d.seq.Count-1] <- TyLocalReturnOp(a,b,end_dat')
        | _ -> end_()
    else end_()
    d.seq.ToArray()
```

Good.

9:45pm. I am taking a short breather here.

Yeah, this should be it. I've planned it yesterday and today I worked out the details and implemented it. Now the codegen should be complete. Let me test it out.

Note: I need to test mutually recursive functions and types. But let me just go through the other tests first.

I am really glad with how all this came out. This backend will serve as the prototype for all that is to come.

Let me commit here."

---
## [ceseo/gcc](https://github.com/ceseo/gcc)@[5493ee7145...](https://github.com/ceseo/gcc/commit/5493ee7145a05dc32bc6d802da2f8237293012d3)
#### Tuesday 2022-07-12 12:00:38 by Alexandre Oliva

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
## [vimpostor/vim-tpipeline](https://github.com/vimpostor/vim-tpipeline)@[c2603e4ad5...](https://github.com/vimpostor/vim-tpipeline/commit/c2603e4ad5c2a3011cffc9ea58d2b5036717067e)
#### Tuesday 2022-07-12 12:38:24 by Magnus Groß

Fix neovim GUI detection

Regression was introduced in 211c438 and actually disabled this plugin
for neovim entirely, whoopsie and sorry for that!

The neovim GUI detection is a single dumpster fire:

Why do we have to listen to autocmds?
Why can't we just use has('gui_running') at any point, like in vim and
gVim?
Why can't we just use UIEnter and must check an extra flag?

Who in their right mind would design such a convoluted clusterfuck,
especially if vim already has such a sane API for this, BUT NO WE HAVE
TO BE FUCKING SPECIAL IN NEOVIM.
All the explanations are just lazy: Oh, you can't have gui_running set
on startup, because plugins are sourced before the GUI attaches?
Oh ok, let's just make it hard for our users then, so that we don't have
to redesign our shit spaghetti code, what a great idea!?!

The VimEnter autocmd already is there for all TUI startup needs. Why
does UIEnter trigger for TUI startup too???

To fix this mess, we check for the chan flag on UIEnter, which is 1 if
we are in a GUI and 0 if we are in a TUI.

Fixes #30

---
## [AllCheeks/FDPClient](https://github.com/AllCheeks/FDPClient)@[136751ad89...](https://github.com/AllCheeks/FDPClient/commit/136751ad896116d0445f14185318375cfafb1daa)
#### Tuesday 2022-07-12 13:59:41 by Hu1

Update README.md

FUCK YOU

Signed-off-by: Hu1 <56077936+AllCheeks@users.noreply.github.com>

---
## [khonsulabs/nebari](https://github.com/khonsulabs/nebari)@[1c2d9a48e5...](https://github.com/khonsulabs/nebari/commit/1c2d9a48e55454e7b3d0efd4d808a532961fc0fe)
#### Tuesday 2022-07-12 15:01:53 by Jonathan Johnson

Finished making Roots work on Sediment

While testing BonsaiDb, I encountered several problems with the
implementation:

- Automatic checkpointing had to be disabled. When running a
  multithreaded workflow, we may have readers that require a BatchId to
  remain present until their read state has been dropped. Sediment will
  need some mechanism to track and prevent checkpointing beyond a
  certain point until in-memory handles have been dropped.

  Disabling automatic checkpointing puts Sediment at a performance
  disadvantage, as one of the benefits is the abilty to reuse space
  instead of writing to the end.
- GrainIds shouldn't ever be 0. I replaced all GrainIds with
  Option<GrainId> to prevent asking Sediment for an invalid grain.
- After getting the Commerce Benchmark running, I didn't really see an
  improvement -- given the disabling of automatic checkpointing, I
  shouldn't be surprised, but I felt like I should have seen *some*
  improvement. I noticed in profiling that sometimes the transaction
  batches were a single commit long, and so I theorized that by not
  allowing a little delay when trying to batch transactions that
  sometimes a single-transaction batch would get through, causing the
  remaining threads to block waiting on that one transaction to be
  written.

  This recv_deadline didn't move the needle, but I left it in because
  I still think this is one part of a better batching approach. My new
  theory this morning is that the transaction batcher isn't batching
  as much as it could. For example, if the transaction channel has ids
  [1, 3, 2, 4, 6, 5] in it, right now it would be committed as [1], [2, 3,
  4], [5. 6]. This is because the first time a discontiguous ID is
  detected, the currently batched list is committed. I want to refactor
  the transaction batcher to always exhaust the channel before
  determining the list of safe-to-commit transactions.

  That change would also have benefited the old format.

  # Please enter the commit message for your changes. Lines starting

---
## [canalplus/rx-player](https://github.com/canalplus/rx-player)@[ebfaf7498c...](https://github.com/canalplus/rx-player/commit/ebfaf7498c0803b0dc38ffdea3096c8422d388ef)
#### Tuesday 2022-07-12 17:07:37 by Paul Berberian

Update most dependencies but Jest

This commit update almost all dependencies but jest.

This is because Jest 28 seems to break while running code, presumably
due to `import`/`export` declarations in imported RxJS files (but I do
not think RxJS is at fault here) that lead to an `unexpected token` when
running through Jest.

You could think that the fault is linked to node not understanding
`import`/`export` (linked to CommonJS/ES6 import shenanigans) but it is
even trickier than that as Jest already performed some JavaScript
transformation at that point, which made the import/export inside an
IIFE - and I'm not sure that this is supported anywhere.

After taking ~a day (much more time than I should) trying to play around
to remove that issue, I gave up and avoided updating Jest to its v28.

In the future, I guess we should either:

  - understand what we're supposed to do here to make it work with Jest
    28 (Jest documentation was poor - even without considering the
    sometimes incomprehensible google-translated french one I get each
    time by default on their docusaurus-based documentation)

    Opened GitHub issues were 100% for angular-based applications - as it
    seems the RxJS+TypeScript cocktail is very majoritarily those. Those
    have their own "fix" through another magical angular dependency.

    Moreover, it does not help that Jest's philosophy seems to be trying to be
    extremely simple for users at the cost of some complex behaviors (as an
    example, it looks like it auto-picks a `babel.config.js` file if it
    sees one at the root of the project. If like us you have multiple build
    files at the root depending on the building context, it is not a good
    idea to silently pick random files like that by default).

    I couldn't understand under an acceptable time where the issue was - and
    at which step it happened.
    I just browsed dozens of doc pages, GitHub and StackOverflow issues
    which just proposed to add yet other automagic dependencies (looked like a
    parody of what JavaScript haters talk about!) - which all seemed to have
    no effect whatsoever.

    I also asked for help from other teams at Canal+, but those in the
    same situation (TypeScript and RxJS) also seem to have random issue
    preventing them from doing the switch.

  - Remove RxJS from the code. It's presumably not its fault yet we
    already started doing that, so maybe we'll just raise the jest
    version once RxJS is definitely removed from the RxPlayer.

  - Wait for some kind of Jest fix or new way of handling those?

  - Remove Jest and go with another testing framework.

    I almost did that due to being fed-up with Jest, but it might no be
    as easy as it seems, mostly the module-mocking part as I'm unsure of
    how other framework handle that now and if it is as convenient as
    Jest's way.

---
## [vdavalon01/linuxkit](https://github.com/vdavalon01/linuxkit)@[860934d5d9...](https://github.com/vdavalon01/linuxkit/commit/860934d5d98f0024ebc86896715863526f8fe96c)
#### Tuesday 2022-07-12 18:09:10 by Davide Brini

New output format: iso-efi-initrd

This option was previously not available and required postprocessing of a `tar-kernel-initrd` output.

Comparison with `iso-efi`:

`iso-efi` only loads the kernel at boot, and the root filesystem is mounted from the actual boot media (eg, a CD-ROM - physical or emulated). This can often cause trouble (it has for us) for multiple reasons:
- the linuxkit kernel might not have the correct drivers built-in for the hardware (see #3154)
- especially with virtual or emulated CD-ROMs, performance can be abysmal: we saw the case where the server IPMI allowed using a ISO stored in AWS S3 over HTTP...you can imagine what happens when you start doing random I/O on the root fs in that case.
- The ISO image has the root device name baked in (ie, `/dev/sr0`) which fails if for some reason the CD-ROM we're running from doesn't end up using that device, so manual tweaking is required (see #2375)

`iso-efi-initrd`, on the other hand, packs the root filesystem as an initramfs (ie similar to what the raw output does, except that in this case we're preparing an ISO image), so both the kernel and the initramfs are loaded in memory by the boot loader and, once running, we don't need to worry about root devices or kernel drivers (and the speed is good, as everything runs in RAM).

Also, the generated ISO can be copied verbatim (eg with `dd`) onto a USB media and it still works.

Finally, the image size is much smaller compared to `iso-efi`.

IMHO, `iso-efi-initrd` could be used almost anywhere `iso-efi` would be used, or might even supersede it. I can't think of a scenario where one might explicitly want to use `iso-efi`.

Points to consider:

- Not tested under aarch64 as I don't have access to that arch. If the automated CI tests also test that, then it should be fine.
- I'm not sure what to put inside `images.yaml` for the `iso-efi-initrd` image. As it is it works of course (my personal image on docker hub), but I guess it'll have to be some more "official" image. However, that cannot be until this PR is merged, so it's kind of a chicken and egg situation. Please advise.
- I can look into adding the corresponding `iso-bios-initrd` builder if there is interest.

![cute seal](https://sites.psu.edu/siowfa16/files/2016/09/baby-seal-29vsgyf-288x300.jpg)

Signed-off-by: Davide Brini <waldner@katamail.com>

---
## [IN2-Moist/2Take1-Moist-Script](https://github.com/IN2-Moist/2Take1-Moist-Script)@[40c7551a58...](https://github.com/IN2-Moist/2Take1-Moist-Script/commit/40c7551a58d29c97dcf81d08c30ad0cc8084bb04)
#### Tuesday 2022-07-12 18:58:10 by IN2_Moist

Non Beta Build

Compiled Script Files
# Next Generation Moist Script

##  |-| 3.0.0.0 |-|

- Added

	Player Info
		unAck TX's:
		Latency (ms):
		PacketLoss:
			these Feature Value toggles will update periodically to show the values

- Added

	Grief This Cunt ! !
		Gangs will Grief Player
			Spawns Random Gangmember nearby to attack

- Added
		Load Player Histroy Module

	Adds same functions and info as my v2.0 script IP label on click will update and change to each value of players ipinfo

- Changed
	Portable Defences from self weapon related functions

- Added
	Portable Defence Sphere (under self)
			Set Below Values Manually
				Will Adjust all values below to this one
				if you just activate the option and value has not changed Input box will popup so you can set this manually

			Portable Defenses Anti Player Vehicle
			Portable Defenses Anti Player Ped
				Improved Since Last Release: Player in any vehicle goes in sphere they get Destroyed WIP needs some tweaking maybe a little over the top
				Anti Player Ped does same as above only they dont need to be in any vehicle
			Portable Defences Anti Projectile
				Should prevent projectiles and weapons fire in the sphere
				has been said in game that people were unable to use some weapons like lazer cannons but this also can be effected by zone flag settings below

			Zone Flags for: < Self off | Others off | Self on | Others on>
				turns zone flags on / off depending on option for players

			Remove All Air Defense Zone
					This will literallly remove any Yacht Defences set, seems to also partially work for player yachts cant shoot in the area but does not take you out.

- Added

	Moists Train Mod (to self Vehicle)

		Enable Train Spawning
			Enables Spawning of Trains and turns on Control Meter and Controller Support to control trains
			Controls are Controller based:

			Left Trigger :: Reduce Cruise Speed or Speed negative (go backwards)

			Right Trigger :: Increase Cruise Speed or Speed Forwards

			Right Top Bumper/Trigger(HandBrake) :: Turns on Stop Train and sets all speeds to 0.0

		Track Switch
			Sets Trains enabled on other tracks (WIP) still figuring this one out

		Train Control < Stop Train Enable Access | Enter Nearest Train as Driver>
			option 1 will try to stop train and low you to enter (WIP not working fully yet)
			option 2 Enter nearest train if one found nearby

		Switch Train Spawn Direction
			changes the direction spawned train is facing

		Spawn Train Variation
			23 variants can be spawned

		Train Cruise
			Sets Train Cruise Speed When on
			train will increase speed until it hits set speed

		Train Speed
			Sets Train Speed Immediately

		Stop Train
			used with controller control tries to stop train

		Control Speed(Instant Insane Speed)
			use this with Train Speed on to use controller input to set the speed
			very sensitive so speeds are insane

		DeRail Train
			Does as it says sets the train to a Derailed State while on

- Updated
	Script Trigger Events to Trigger 2

- Added ScriptEvent SafeMode
	Setting Saveavke For Safe Mode
	This prevents you from triggering script events on yourself

- Added Auto Script Host

- Added God Notify and Notify Reset (WIP) i recommend not using this atm as its a bit false positive i forgot to remove it

---
## [WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/FEDERAL-USE-AND-DISTRIBUTION-ONLY](https://github.com/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/FEDERAL-USE-AND-DISTRIBUTION-ONLY)@[a5a46e225e...](https://github.com/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/FEDERAL-USE-AND-DISTRIBUTION-ONLY/commit/a5a46e225e04959ca6bc54adce23d2f83196b8c2)
#### Tuesday 2022-07-12 19:11:01 by WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER

[William McKenzie, Part Clerk to the Honorable Shlomo S. Hagler, J.S.C. NYSCEF 153974/2020](https://support.nysba.org/attachments/token/yPz39fuc7N5XJvapGxqUyi0mR/?name=voicemail+917-843-3456.mp3)

NYSCEF 153974/2020
<https://support.nysba.org/attachments/token/hZU6XKc80l5AZmOROYTomS2a3/?name=MOV+FILES+DISTRIBUTED+-+LVL+7.html>

<https://support.nysba.org/attachments/token/yPz39fuc7N5XJvapGxqUyi0mR/?name=voicemail+917-843-3456.mp3>

>> CIK FIler 1516523
>> CIK Filer 93715
>> CRD member 8209

/Nyscef 153974_2020. Processed.

    Docket 420, Augusr 8th, 2020 receipt
    Docket 399, August 10th, 2020 receipt

STFGX, STFBX, SFITX, SFBDX
   >> Nov 13, 2021
   >> Nov 24, 2021
   >> Dec 21, 2021



----- Forwarded Message -----
From: "Bo Dincer" <bd2561@columbia.edu>
To: "b-dincer66@outlook.com" <b-dincer66@outlook.com>, "Bo Dincer" <BO.DINCER@yahoo.com>
Sent: Tue, Aug 4, 2020 at 7:37 AM
Subject: check NYSCEF: FW: 153974/2020 Sullivan Properties L.P. v. Ba
---------- Forwarded message ---------
From: William McKenzie <wmckenzi@nycourts.gov>
Date: Mon, Jun 22, 2020 at 2:34 PM
Subject: RE: FW: 153974/2020 Sullivan Properties L.P. v. Baris Dincer - TELEPHONIC ORAL ARGUMENT ON TEMPORARY RESTRAINING ORDER JUNE 23, 2020 AT 12PM
To: Bo Dincer <bd2561@columbia.edu>, Laskowitz, Shari <slaskowitz@ingramllp.com>
Cc: Bo Dincer <BO.DINCER@yahoo.com>


Dear Mr. Dincer,

 

Thank you for your email.  Attendance is mandatory.

 

Take due notice thereof.

 

Sincerely,

 

William McKenzie

Part Clerk to the Honorable Shlomo S. Hagler, J.S.C.

New York Supreme Court, Civil Branch – Part 17

60 Centre Street, Room 335

New York, New York 10007

(646) 386-3283 (Part 17)


Request #37030 "Receipts and one page- file find..." was closed and merged into this request. Last comment in request #37030:

Which agency do you think understands this?

    "PEEPING TOMCATS"

Not an airplane. Not at all, just love when the Federal Regulators get involved, the more the merrier... just like Shari.

   #50074 #90849565



    ##MY FAVORITE BUILDING IN MANHATTAN.##

https://www.fbi.gov/video-repository/newss-chasing-the-dragon-the-life-of-an-opiate-addict/file_view
There is no exemption from that, all guilty where applicable.

https://github.com/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/blob/main/Memo%20Style9.pdf

One-page attached. And one link.

To give them a little more time to think about it-in case we have a infiltrator here.

#HF-RATES-APPLY#

https://github.com/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/blob/main/111.xps

I even posted the Seahawks in Seattle earlier, but they will definitely enjoy and consult with Kurt Kobain, Tu-Pac, and Biggie Smalls amd get on 747s anywhere without a question or a concern because they understand it's not their job to investigate or maintain a fiduciary oath to uphold fitness and the Law, unless it was one of their own.

Those are all Federal agencies, You understand Federal?

I enjoy the documentary BTW.. thank you Misses and Mister Federals.

1.

https://en.wikipedia.org/wiki/IRT_Powerhouse

How many references are in that link 1.

2.

https://en.wikipedia.org/wiki/Interborough_Rapid_Transit_Company

How many references are in that link 2.

And whats my rank here using this link?

__

https://en.everybodywiki.com/Maritime_Capital_Partners_LP

And over here this also populates with my name?

https://www.google.com/url?sa=t&source=web&rct=j&url=https://www.scribd.com/document/386161673/Bo-Dincer-New-York-City-Fixed-Income-Trader-Baris-Dincer-Maritime-Capital&ved=2ahUKEwi4t4aChvL4AhVPjokEHfdIBBQQFnoECAgQAQ&usg=AOvVaw1Dvj-8WfevUjIJe14EqMm7

But how mant felonies do you think they have aggregated for those corporations and the the "well-endowed" Zuckers of 153974/2020, their counselors and like and the farmers at 116, also play with themselves thinking they are exempt from prosecution after committing several felonies.

BUT how many more are in this link? Its a XPS document isn't that crazy??

Because. Thats why, you go against your own by helping the stonehearst asylum to continue to aid and abet the Zuckers and their financial crimes, so I provode my friends - in turn - with GPS coordinates and no mail-code. Floor by floor.

Hey also.. love where you work! But that st3251 is NOT A FELON, trust me. NOT A FELON or a criminal at all... in fact thanked me for all the Christmas gifts I bought for her.

ALSO WILL HELP THEM APPREHEND AS MANY VRIMINALS AND FELONS AS I POSSIBLE... IF ONLY TO HELP EVERYONE HELP THEMSELVES TO THE FEDERAL CHARGES ANNEXED IN THE DISTRIBUTION AND VIOLATION OF MY CIVIL RIGHTS IN:

NYSCEF 153974/2020

THAT'S WHY.

SO STOP FOLLOWING ME AROUND IF YOU'RE NOT INVITED...

IT ISN'T GOING TO HELP YOU.

-- THOSE RECEIPTS ARE ALL IN THE REPOSITORY AS WELL, HAVEN'T BEEN REIUMBURSED AS OF CURRENT BUT IT'S NOT A PROBLEM.. I'LL ASK TOMORROW, OR THE DAY AFTER..

MOSTLY FOR PLAYING HUMAN TARGET, AND TRUST ME - I AM NOT A DOCTORATE.

https://github.com/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/blob/main/111.xps

/S/ Baris Dincer.

917-378-3467

646-256-3609

--

/S/ BO DINCER.

What about Disneyland though? Those towers have no cameras.

        crickets my @$$.??? Call this number 702-891-7434

Codename: freeman

or

markov chain

or

receipt

or

"FUNNY SAPERSTEIN"

HOW FUNNY TO NOT BE A CRIMINAL EITHER THOUGH.

YOURS TRULY.

-- EVEN STEVENS for the 50, not clear though. Haha.

---
## [GSchooling1/pings](https://github.com/GSchooling1/pings)@[823d3a170d...](https://github.com/GSchooling1/pings/commit/823d3a170d9cf1f42766b66359170d5b4873c1f7)
#### Tuesday 2022-07-12 20:11:23 by Grant Schooling

deleted ping the-pastel-peach.tumblr.com time-is-a-human-construct-also-fuck-you94dd4e90df9f8c0cba213a3e9a4ea644.jpg

---
## [RocketChat/Rocket.Chat](https://github.com/RocketChat/Rocket.Chat)@[5a37518e42...](https://github.com/RocketChat/Rocket.Chat/commit/5a37518e42dec114e0ed1a71b5d103b4a62e9b58)
#### Tuesday 2022-07-12 20:14:54 by Ben Wiederhake

[FIX] Client-generated sort parameters in channel directory  (#25768)

## Proposed changes (including videos or screenshots)
- In the web-client, sorting the channel directory by "Last Message" raises the error "Invalid sort parameter provided".

I don't think a screenshot is necessary, but if you'd like one anyway, here it is:

![Bildschirmfoto_2022-06-06_12-54-34](https://user-images.githubusercontent.com/2690845/172147996-e9942daf-6819-4eee-afa4-b1c6bce7a650.png)


## Issue(s)
Closes #25695

## Steps to test or reproduce

- Open the web client, i.e. navigate your browser to `https://rocketchat.$DOMAIN/home`
- Click the "Directory" button in the top left, (or just navigate directly to `https://rocketchat.$DOMAIN/directory/channels`)
- In the table header, click on "Last message" once
- In the table header, click on "Last message" again

Expected behavior: Clicking "Last message" turns on and then toggles sorting by the date of the last message, either first ascending and then descending, or the other way around.

Actual behavior: The first click sorts the messages in ascending order (good!), the second click shows a red warning box "FIXME", the table content disappears, and is replaced by throbbing grey placeholders.

### "Good" request (ascending order):

`https://rocketchat.domain.org/api/v1/directory?query=%7B%22type%22%3A%22channels%22%2C%22text%22%3A%22%22%2C%22workspace%22%3A%22local%22%7D&sort=%7B%22lastMessage%22%3A1%7D&count=25`

More easily readable GET parameters:

```
query | {"type":"channels","text":"","workspace":"local"}
sort | {"lastMessage":1}
count | 25
```

Response:
```
{"result":[{"_id":"AAAAAAAAAAAAAAAAA","name":"foobar","fname":"foobar","t":"c","usersCount":10,"ts":"2019-01-01T00:00:00.000Z","default":false,"lastMessage":{"_id":"AAAAAAAAAAAAAAAAA","rid":"AAAAAAAAAAAAAAAAA","msg":"Hello, World!","ts":"2019-01-01T00:00:00.000Z","u":{"_id":"AAAAAAAAAAAAAAAAA","username":"normaluser","name":"normaluser"},"unread":true,"_updatedAt":"2019-01-01T00:00:00.000Z","urls":[],"mentions":[],"channels":[]},"description":"Obviously, this JSON response is heavily censored."}],"count":25,"offset":0,"total":52,"success":true}
```

(Obviously, this JSON response is heavily censored, but you get the gist: It was successful.)

### "Bad" request (descending order):

`https://rocketchat.domain.org/api/v1/directory?query=%7B%22type%22%3A%22channels%22%2C%22text%22%3A%22%22%2C%22workspace%22%3A%22local%22%7D&sort=%7B%22lastMessage%22%3A0%7D&count=25`

More easily readable GET parameters:

```
query | {"type":"channels","text":"","workspace":"local"}
sort | {"lastMessage":0}
count | 25
```

Response:
```
{"success":false,"error":"Invalid sort parameter provided: \"{\"lastMessage\":0}\" [error-invalid-sort]","errorType":"error-invalid-sort","details":{"helperMethod":"parseJsonQuery"}}
```

## Further comments

Version on the server where I noticed this: `https://rocketchat.$DOMAIN/api/info` returns `{"version":"4.8","success":true}`. According to the "Releases" page, this version appeared 5 days ago, so I believe this is up to date.

### The journey to here

For some reason, the descending order uses the wrong magic number "0", and the server can't interpret that. However, this *used* to work, so I'm not very sure about this.

The error message appears in the source code of the entire organization exactly once: https://github.com/RocketChat/Rocket.Chat/blob/31ae30f30ad71d9e5a1b0cad494b3471a7dd8807/apps/meteor/app/api/server/helpers/parseJsonQuery.ts#L42
So I'll guess that this is the line of code that generated this particular message.

A few lines above we see that the server only knows 1 and -1 as magic numbers for the sorting:
https://github.com/RocketChat/Rocket.Chat/blob/31ae30f30ad71d9e5a1b0cad494b3471a7dd8807/apps/meteor/app/api/server/helpers/parseJsonQuery.ts#L35
This matches the observed bug: The browser sends 1 (which works) and 0 (which doesn't work).

Generally, it seems that the web client actually uses the strings "asc" and "desc" internally, which are hard to mix up. So I assume that it's the conversion of that is broken somehow.

Exactly this seems to be the case here:
https://github.com/RocketChat/Rocket.Chat/blob/31ae30f30ad71d9e5a1b0cad494b3471a7dd8807/apps/meteor/client/views/directory/hooks.js#L11

The code around it produces exactly the kind of query seen in the network log, and can also produce the buggy parameter `sort: 0`. This either fixes bug #25695, or a different bug of the same kind.

I am not sure how to add tests for this, can someone do this for me or show me where to start? I'm actually just an end-user and "accidentally" found the fix for the bug while writing the bug report ^^'

EDIT: Rebased for convenience, and to re-check CI.

---
## [ihmels/symfony](https://github.com/ihmels/symfony)@[338daf25c9...](https://github.com/ihmels/symfony/commit/338daf25c9589e2b93b4d7d693b4a49f7da677db)
#### Tuesday 2022-07-12 21:21:16 by Nicolas Grekas

feature #46751 [VarExporter] Add trait to help implement lazy loading ghost objects (nicolas-grekas)

This PR was merged into the 6.2 branch.

Discussion
----------

[VarExporter] Add trait to help implement lazy loading ghost objects

| Q             | A
| ------------- | ---
| Branch?       | 6.2
| Bug fix?      | no
| New feature?  | yes
| Deprecations? | no
| Tickets       | -
| License       | MIT
| Doc PR        | -

This PR packages an implementation of [lazy loading ghost objects](https://www.martinfowler.com/eaaCatalog/lazyLoad.html) in a single `LazyGhostObjectTrait` (as a reminder, a lazy ghost object is an object that is created empty and that is able to initialize itself when being accessed for the first time.)

By using this trait, ppl can easily turn any existing classes into such ghost object implementations.

I target two use cases with this feature (but ppl are free to be more creative):
1. lazy proxy generation for service containers;
2. lazy proxy generation for entities.

In all cases, the generation itself is trivial using inheritance (sorry `final` classes.) For example, in order to turn a `Foo` class into a lazy ghost object, one just needs to do:
```php
class FooGhost extends Foo implements LazyGhostObjectInterface
{
    use LazyGhostObjectTrait;
}
```

And then, one can instantiate ghost objects like this:
```php
$fooGhost = FooGhost::createLazyGhostObject($initializer);
```

`$initializer` should be a closure that takes the ghost object instance as argument and initializes it. An initializer would typically call the constructor on the instance after resolving its dependencies:
```php
$initializer = function ($instance) use ($etc) {
    // [...] use $etc to compute the $deps
    $instance->__construct(...$deps);
};
```

Interface `LazyGhostObjectInterface` is optional to get the behavior of a ghost object but gives a contract that allows managing them when needed:
```php
    public function initializeLazyGhostObject(): void;
    public function resetLazyGhostObject(): bool;
```

Because initializers are *not* freed when initializing, it's possible to reset a ghost object to its uninitialized state. This comes with one limitation: resetting `readonly` properties is not allowed by the engine so these cannot be reset. The main target use case of this capability is Doctrine's EntityManager of course.

To work around the limitation with `readonly` properties, but also to allow creating partially initialized objects, `$initializer` can also accept two more arguments `$propertyName` and `$propertyScope`. When doing so, `$initializer` is going to be called on a property-by-property basis and is expected to return the computed value of the corresponding property.

Because lazy-initialization is *not* triggered when (un)setting a property, it's also possible to do partial initialization by calling setters on a just-created ghost object.

---

You might wonder why this PR is in the `VarExporter` component? The answer is that it reuses a lot of its existing code infrastructure. Exporting/hydrating/instantiating require using reflection a lot, and ghost objects too. We could consider renaming the component, but honestly, 1. I don't have a good name in mind; 2. changing the name of a component is costly for the community and 3. more importantly this doesn't really matter because this is all low-level stuff usually.

You might also wonder why this trait while we already have https://github.com/FriendsOfPHP/proxy-manager-lts and https://github.com/Ocramius/ProxyManager?

The reason is that the code infrastructure in ProxyManager is heavy. It comes with a dependency on https://github.com/laminas/laminas-code and it's complex to maintain. While I made the necessary changes to support PHP 8.1 in FriendsOfPHP/proxy-manager-lts (and submitted those changes [upstream](https://github.com/Ocramius/ProxyManager/pulls?q=is%3Apr+is%3Aopen+sort%3Aupdated-desc+author%3Anicolas-grekas)), getting support for new PHP versions is slow and complex. Don't take me wrong, I don't blame maintainers, ProxyManager is complex for a reason.

But ghost objects are way simpler than other kind of proxies that ProxyManager can produce: a trait does the job. While the trait itself is no trivial logic, it's at least plain PHP code, compared to convoluted (but needed) code generation logic in ProxyManager.

If you need any other kind of proxies that ProxyManager supports, just use ProxyManager.

For Symfony, having a simple lazy ghost object implementation will allow services declared as lazy to be actually lazy out of the box (today, you need to install proxy-manager-bridge as an optional dependency.) \o/

Commits
-------

27b4325f78 [VarExporter] Add trait to help implement lazy loading ghost objects

---
## [hashicorp/nomad](https://github.com/hashicorp/nomad)@[f998a2b77b...](https://github.com/hashicorp/nomad/commit/f998a2b77b84a542d73f11a0a254576f9031d1f3)
#### Tuesday 2022-07-12 21:40:29 by Michael Schurter

core: merge reserved_ports into host_networks (#13651)

Fixes #13505

This fixes #13505 by treating reserved_ports like we treat a lot of jobspec settings: merging settings from more global stanzas (client.reserved.reserved_ports) "down" into more specific stanzas (client.host_networks[].reserved_ports).

As discussed in #13505 there are other options, and since it's totally broken right now we have some flexibility:

Treat overlapping reserved_ports on addresses as invalid and refuse to start agents. However, I'm not sure there's a cohesive model we want to publish right now since so much 0.9-0.12 compat code still exists! We would have to explain to folks that if their -network-interface and host_network addresses overlapped, they could only specify reserved_ports in one place or the other?! It gets ugly.
Use the global client.reserved.reserved_ports value as the default and treat host_network[].reserverd_ports as overrides. My first suggestion in the issue, but @groggemans made me realize the addresses on the agent's interface (as configured by -network-interface) may overlap with host_networks, so you'd need to remove the global reserved_ports from addresses shared with a shared network?! This seemed really confusing and subtle for users to me.
So I think "merging down" creates the most expressive yet understandable approach. I've played around with it a bit, and it doesn't seem too surprising. The only frustrating part is how difficult it is to observe the available addresses and ports on a node! However that's a job for another PR.

---
## [san7890/bruhstation](https://github.com/san7890/bruhstation)@[6fe0683a7b...](https://github.com/san7890/bruhstation/commit/6fe0683a7bc788a497dbce8771768e427d0dffb1)
#### Tuesday 2022-07-12 22:57:27 by Jolly

[READY] [KC13] Showing "The Derelict" some love: General updates, aesthetic changes and misc (#67696)

With this PR I aim to make KC13 (TheDerelict.dmm), or Russian Station (whatever you guys call it) a tad bit more flavorful with its environment as well as somethings on the mapping side (like adding area icons!).
To preface, no, I'm not remapping anything here extensively. The general layout should be relatively the same (or should be in theory).

Halfway through naming the area icons I checked the wiki page and found out it was KC not KS, so, its KS13 internally.

Readability for turf icons are cool.
Also just making the ruin more eye appealing would be better.
General cleanup and changes will give new life to this rather.. loved? Hated? Loot pinata? Ruin.
The ruin also now starts completely depowered, like Old Station (its a Derelict, it makes no sense for it to still be powered after so long). As for some mild compensation, a few more batteries were sprinkled in to offset any issues. If there is any concern of "But they'll open the vault faster!", there were always 5 batteries that people used to make the vault SMES.
Lastly, giving it some "visual story telling" is cool, as mapping fluff goes.

I also added a subtle OOC hint that the SMES in the northern most solar room needs a terminal with the following:

SMES Jumpscare
As an aside, I aim to try and keep the feel of this ruin being "dated" while at the same time having some of our newer things. With that, certain things I'll opt out of using in favor of more "generic" structures to give KC13 that true "Its old but not really" feel and look.

---
## [dragomagol/tgstation](https://github.com/dragomagol/tgstation)@[92fda5014d...](https://github.com/dragomagol/tgstation/commit/92fda5014dbc8ba64c19848e693c179af35da2ac)
#### Tuesday 2022-07-12 23:10:54 by san7890

Makes Hell Microwaves Not Use Power (#67413)

Hey there,

I was informed that the holodeck program Microwave Paradise would draw and suck power out of an APC. Didn't intend for that to happen, and while funny, I don't really want to arm the crew with le epic power sink with very little effort than pressing a button, or warranting this to eventually be locked to "dangerous" programs. So, let's change such that this subtype of microwaves that can not be constructed (only mapped/spawned) doesn't consume any power. I don't know why it drew off the nearest APC or how that works, but this seems to be alright.

It's not possible to deconstruct machinery spawned in at the Holodeck (which I verified while testing this PR), so do not worry about people using this to bypass the power economy for whzhzhzhz purposes.

---

