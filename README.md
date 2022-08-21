## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-08-20](docs/good-messages/2022/2022-08-20.md)


1,569,830 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,569,830 were push events containing 2,178,327 commit messages that amount to 126,052,087 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 33 messages:


## [shijiesheng/cadence-client](https://github.com/shijiesheng/cadence-client)@[f5e0fd25e4...](https://github.com/shijiesheng/cadence-client/commit/f5e0fd25e4347c85b28dac87f51b532700455d2c)
#### Saturday 2022-08-20 00:02:12 by Steven L

Sharing one of my favorite "scopes" in intellij, and making it easier to add more (#1182)

Goland is nice, and the type-based navigation is wildly superior to gopls-driven
stuff in my experience, so I tend to lean hard on it when I'm able.

By default though, Goland searches *everything*.  All the time.
That's totally reasonable as a default, but we can do better:

- Tests are not usually all that interesting when trying to understand and navigate code.
  (perhaps they should be, but that's more a platonic ideal than a reality)
- Generated RPC code is almost never useful to dive into.  The exposed API surface is sufficient,
  if it compiles, it's correct.
- Non-Go files are just less interesting in a Go project.

So this scope excludes ^ all that.
To add more shared ones, just check the "share through vcs" box and commit it.

To use it, just select the scope from the dropdown when you search.  E.g. "find in files" ->
change from "in project" to "scope" -> change the dropdown.  This custom scope will now appear,
and it'll remember what you last used, so it's a nice default.

This also works in "call hierarchy", "go to implementations" (open it in a panel to configure it,
with the gear on the side.  it's awful UI but it works), etc quite a lot of places.

This same kinda-obtuse search-scope query language can be used to mark things as generated or test
related, which will also help other parts of the IDE mark things as more or less relevant for you.
It's worth exploring a bit, scopes and filters can be used to do a lot: https://www.jetbrains.com/help/idea/scope-language-syntax-reference.html

---
## [JakeUK/Environment](https://github.com/JakeUK/Environment)@[1b2a5c19d0...](https://github.com/JakeUK/Environment/commit/1b2a5c19d0e2d54cd953eea4cd83e3b7ad419cc3)
#### Saturday 2022-08-20 01:08:31 by Jake Cooper

Boids working

HOLY SHIT SO MANY STUPID BUGS ITS FINALLY DONE

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[078e86919e...](https://github.com/treckstar/yolo-octo-hipster/commit/078e86919e533320c81c7fd2eae2d8f2d9bbdb37)
#### Saturday 2022-08-20 03:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [karthik4579/kernel_xiaomi_onclite-1](https://github.com/karthik4579/kernel_xiaomi_onclite-1)@[82503c4d04...](https://github.com/karthik4579/kernel_xiaomi_onclite-1/commit/82503c4d04f381363c79e1d5f468a4d2e66aeb0b)
#### Saturday 2022-08-20 03:55:18 by Peter Zijlstra

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

---
## [delphix/linux-kernel-oracle](https://github.com/delphix/linux-kernel-oracle)@[9997f61537...](https://github.com/delphix/linux-kernel-oracle/commit/9997f615374a116e05bbad5b2fef49a28e6afdf0)
#### Saturday 2022-08-20 04:08:10 by Linus Torvalds

gpiolib: acpi: use correct format characters

BugLink: https://bugs.launchpad.net/bugs/1973085

[ Upstream commit 213d266ebfb1621aab79cfe63388facc520a1381 ]

When compiling with -Wformat, clang emits the following warning:

  gpiolib-acpi.c:393:4: warning: format specifies type 'unsigned char' but the argument has type 'int' [-Wformat]
                        pin);
                        ^~~

So warning that '%hhX' is paired with an 'int' is all just completely
mindless and wrong. Sadly, I can see a different bogus warning reason
why people would want to use '%02hhX'.

Again, the *sane* thing from a human perspective is to use '%02X. But
if the compiler doesn't do any range analysis at all, it could decide
that "Oh, that print format could need up to 8 bytes of space in the
result". Using '%02hhX' would cut that down to two.

And since we use

        char ev_name[5];

and currently use "_%c%02hhX" as the format string, even a compiler
that doesn't notice that "pin <= 255" test that guards this all will
go "OK, that's at most 4 bytes and the final NUL termination, so it's
fine".

While a compiler - like gcc - that only sees that the original source
of the 'pin' value is a 'unsigned short' array, and then doesn't take
the "pin <= 255" into account, will warn like this:

  gpiolib-acpi.c: In function 'acpi_gpiochip_request_interrupt':
  gpiolib-acpi.c:206:24: warning: '%02X' directive writing between 2 and 4 bytes into a region of size 3 [-Wformat-overflow=]
       sprintf(ev_name, "_%c%02X",
                            ^~~~
  gpiolib-acpi.c:206:20: note: directive argument in the range [0, 65535]

because gcc isn't being very good at that argument range analysis either.

In other words, the original use of 'hhx' was bogus to begin with, and
due to *another* compiler warning being bad, and we had that bad code
being written back in 2016 to work around _that_ compiler warning
(commit e40a3ae1f794: "gpio: acpi: work around false-positive
-Wstring-overflow warning").

Sadly, two different bad compiler warnings together does not make for
one good one.

It just makes for even more pain.

End result: I think the simplest and cleanest option is simply the
proposed change which undoes that '%hhX' change for gcc, and replaces
it with just using a slightly bigger stack allocation. It's not like
a 5-byte allocation is in any way likely to have saved any actual stack,
since all the other variables in that function are 'int' or bigger.

False-positive compiler warnings really do make people write worse
code, and that's a problem. But on a scale of bad code, I feel that
extending the buffer trivially is better than adding a pointless cast
that literally makes no sense.

At least in this case the end result isn't unreadable or buggy. We've
had several cases of bad compiler warnings that caused changes that
were actually horrendously wrong.

Fixes: e40a3ae1f794 ("gpio: acpi: work around false-positive -Wstring-overflow warning")
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: Andy Shevchenko <andriy.shevchenko@linux.intel.com>
Signed-off-by: Sasha Levin <sashal@kernel.org>
Signed-off-by: Kamal Mostafa <kamal@canonical.com>
Signed-off-by: Kleber Sacilotto de Souza <kleber.souza@canonical.com>

---
## [Rykka-Stormheart/VOREStation](https://github.com/Rykka-Stormheart/VOREStation)@[e089978527...](https://github.com/Rykka-Stormheart/VOREStation/commit/e08997852748d1155820139dfacf4745c9181ce3)
#### Saturday 2022-08-20 04:54:09 by Rykka

Ports Taur Loafing from Cit-RP & Chompstation13

Ports https://github.com/Citadel-Station-13/Citadel-Station-13-RP/pull/2950

Doesn't work for sleeping *yet* due to some fuckiness with sprites updating that I'll probably actually work on properly later.
Does work for resting, and when you're stunned/knocked over/etc you will tip upwards like normal as a visual indicator that you're fucked (until we get fancy on-side sprites or smth).

At the very least, despite my frustrations, y'all can rest on your belly now as a taur and transform/size matrixes should work. LMK if there's any issues, my testing didn't find any.

Bear in mind that this presently only works for the drake-taur bc it's the only one that has sprites for it. The code is there, just enable can_loaf and set the offset accordingly to match if you want to sprite more taur loafs.

---
## [Rykka-Stormheart/CHOMPStation2](https://github.com/Rykka-Stormheart/CHOMPStation2)@[8e8232c0d8...](https://github.com/Rykka-Stormheart/CHOMPStation2/commit/8e8232c0d826dc3341d20a7861c1d86859e06ef7)
#### Saturday 2022-08-20 04:54:21 by Rykka

Ports Taur Loafing from Cit-RP

Ports https://github.com/Citadel-Station-13/Citadel-Station-13-RP/pull/2950

Doesn't work for sleeping *yet* due to some fuckiness with sprites updating that I'll probably actually work on properly later.
Does work for resting, and when you're stunned/knocked over/etc you will tip upwards like normal as a visual indicator that you're fucked (until we get fancy on-side sprites or smth).

For real tho laying-on-side sprites would be nice to visually represent a taur collapsed on their side, rather than faceplanting bc humancode.

At the very least, despite my frustrations, y'all can rest on your belly now as a taur and transform/size matrixes should work. LMK if there's any issues, my testing didn't find any.

---
## [GNUWeeb/linux](https://github.com/GNUWeeb/linux)@[1a5fee5da3...](https://github.com/GNUWeeb/linux/commit/1a5fee5da3af548ce191450aa8a18ae20c4147f3)
#### Saturday 2022-08-20 05:21:08 by Johannes Weiner

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
## [Gullwing-door/restoration-mod](https://github.com/Gullwing-door/restoration-mod)@[ae4bb92115...](https://github.com/Gullwing-door/restoration-mod/commit/ae4bb921158dccebf8e60b7851a41b51a2bd736d)
#### Saturday 2022-08-20 06:21:02 by Noep

stuff

- Lowered the deflection cap from 95% to 60%
-- You could never actually reach that level of deflection after Frenzy's nerf from 30/60% to 20/50%
-- Realistically speaking, this only slightly reduces effectiveness as getting to 60% deflection even before this change, assuming you have 30% from FJ + Die Hard, meant you'd have to be at 30% HP to get 60% deflection

- Oni Irezumi (Yakuza) raises the deflection cap by 20%, to a maximum of 80%
-- Again, assuming you have the 30% from FJ + Die Hard, you'd actually be downed at the point you'd get 80% deflection
--- You'll be tanky as fuck while downed tho :^)

---
## [pralabhkumar/spark](https://github.com/pralabhkumar/spark)@[c4c623a3a8...](https://github.com/pralabhkumar/spark/commit/c4c623a3a890267b2f9f8d472c8be30fc5db53e1)
#### Saturday 2022-08-20 07:49:29 by Hyukjin Kwon

[SPARK-39869][SQL][TESTS] Fix flaky hive - slow tests because of out-of-memory

### What changes were proposed in this pull request?

This PR adds some manual `System.gc`. I know enough that this doesn't guarantee the garbage collection and sounds somewhat funny but it works in my experience so far, and I did such hack in some places before.

### Why are the changes needed?

To deflake the tests.

### Does this PR introduce _any_ user-facing change?

No, dev and test-only.

### How was this patch tested?

CI in this PR should test it out.

Closes #37291 from HyukjinKwon/SPARK-39869.

Authored-by: Hyukjin Kwon <gurwls223@apache.org>
Signed-off-by: Hyukjin Kwon <gurwls223@apache.org>

---
## [rytt0001/RWoM](https://github.com/rytt0001/RWoM)@[bc6c0ffd17...](https://github.com/rytt0001/RWoM/commit/bc6c0ffd17f558adff1415ef80408b309c434157)
#### Saturday 2022-08-20 08:34:43 by TorannD

v2.5.8.0 update

New:
 o Advanced Classes
  - Unique type of custom class that can be added (or removed) onto existing classes
  - Share the same pawn level and displays on the same might/magic tabs with base class, and other advanced classes
  - Advanced classes share the same xml definition as normal classes, but are identified using the <isAdvancedClass> tag
  - See the Possessed class for an example
  - Other options for advanced classes include:
	* Restrict the advanced class to require a base class first using <requiresBaseClass> (true/false)
	* Allow the advanced class to be added as a trait during pawn generation with <canSpawnWithClass> (true/false)
	* Create advanced class "chains" by removing a pre-requisite trait with <removeRequiredTrait> (true/false)
	* Specify one or more valid pre-requisite traits using <requiredTraits> (TraitDef list)
	* Prevent pawns with certain traits from becoming the advanced class using <disallowedTraits> (TraitDef list)

 o Chained abilities
  - TMAbilityDef options that allow temporary abilities to be added and removed to create ability chains
  - See Possessed Control Spirit Storm for an example
  - Options include:
	* Specify a chained ability <chainedAbility> (TMAbilityDef)
	* Manually set a duration for the temporary ability <chainedAbilityExpiresAfterTicks> (integer > 0, -1 for "do not use")
	* Link the chained ability to be removed when the main ability cooldown expires <chainedAbilityExpiresAfterCooldown> (true/false)
	* Remove the ability after use; can be applied to any ability <removeAbilityAfterUse> (true/false)
	* Remove a list of abilities after use to clear or reset an ability chain <abilitiesRemovedWhenUsed> (TMAbilityDef list)

 o New Class: Possessor - an invisible, wandering spirit able to possess the bodies of the dead or living using spirit energy
  - Perishes when spirit energy fully depletes
  - Uses spirit energy to fuel their abilities
  - Able to possess other bodies and augments the abilities of the occupied body
  - Able to possess a corpse with all skills, talents, and memories of the dead pawn, but spirit energy will gradually deplete and must be replenished
  - Able to possess animals and assert control over their actions; the spirit has limited influence while in the body of an animal and spirit energy gradually depletes
  - Able to possess living pawns; much lower spirit energy loss than other options, but the host pawn will have conflicting thoughts - this can be offset if the spirit and the host pawn share the same outlook on life (backstory preferences, traits, gender, ideo, etc)
  - Shard of spirit extraction is used to remove a spirit from a pawn; the spirit may exit the body of an animal at any time
  - The possessor may naturally gain spirit energy while doing common, meditative tasks and can forcefully gain spirit energy using an ability or inflicting melee damage
  - A pawn occupied by a possessor will no longer be able to heal naturally; wounds can only be healed by external items, abilities, or spells, or when the possessed pawn gains spirit energy (by any means)

 o New Autocast options:
  - <onlyAppliesToCaster> (true/false) - forces the condition check against the caster instead of the target, when different
  - <targetNoFaction> (true/false) - target pawn is only selected if the faction is null (wild pawns)

Tweaks:
 o Summoned creatures will respond more aggressively when summoned near enemies
 o Magic Wardrobe automatically sets swapped equipment as forced/locked
 o Changed Brand graphics to be less error prone

Bug fixes:
 o Polymorphed or shapeshifted animals will take drafted orders again
 o Taunted targets will no longer attempt to attack a deceased taunter
 o Fixed a bug where AI would not use abilities if autocasting was disabled
 o Winter's Reign and Snap Freeze correctly assign damage attribution
 o Cure Disease can be cast while wearing a shield belt
 o Defense pylon will only spam invalid location message once instead of infinitely

---
## [rytt0001/RWoM](https://github.com/rytt0001/RWoM)@[a3fda50b81...](https://github.com/rytt0001/RWoM/commit/a3fda50b81f45b3b47b1499ec7920ec99d89cea6)
#### Saturday 2022-08-20 08:34:43 by TorannD

v2.5.7.3 update

New:
 o Summoner Defense Pylon art and sound updates and configuration tweaks courtesy of Djeeshka

Tweaks:
 o Mage light performance improvements
 o Undead auto undraft performance improvements
 o Death retaliation will no longer summon meteors on pawns under a roof
 o Brightmage shooting accuracy penalty reduced
 o Ranger and Sniper now have a small shooting accuracy bonus
 o Elixir can be autocast and will target nearby injured pawns
 o Transcendent thought bonus for the use of magic duration increased 24->60 in-game hours
 o More distinction between Venerated and Abhorrent magic precepts
 o Sentinel health slightly increased
 o Demons will no longer jump to another target if engaged with their target in melee
 o Demon armor rating increased by ~10% and rewards increased
 o Golems will start with a name by default
 o Wandering Lich event earliest start time delayed from 90 days -> 250 days

Bug fixes:
 o Wave of fear causing errors for unique enemies
 o Disabled traits removed from arcane inspiration
 o Dormant Mecha Golem gatling gun requires line of sight to fire
 o Fix for spirit wolf dying in a caravan
 o Faceless will no longer have the option to pick up enchantment gems
 o Psionic dash will automatically cancel if within a cell of the map edge
 o Fixed golem draw depth for various upgrades
 o Golems losing name or settings after being upgraded

---
## [IvanYashchuk/pytorch](https://github.com/IvanYashchuk/pytorch)@[4c8cfb57aa...](https://github.com/IvanYashchuk/pytorch/commit/4c8cfb57aa3ac58112efb693635198b07edf008f)
#### Saturday 2022-08-20 08:42:16 by Edward Z. Yang

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
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[f0597d80fb...](https://github.com/mrakgr/The-Spiral-Language/commit/f0597d80fb9da9104b29a5937d1d27ef6b1aa7e8)
#### Saturday 2022-08-20 10:39:49 by Marko Grdinić

"9:20am. I am up. I've been going over 4chan thread yesterday and the intensity of it is really ramping up. People are going haywire over Stable Diffusion. Maybe I am out of tune. Maybe things will get fun once I get access to it. No mail.

9:30am. It seems last chapter of Konchuki is out.

Let me chill for a while and then I will get started. I will first post chapter 4.

10:20am. Let me get started. Let me proof ch 4. I am bad at proofing, but I did find some errors in ch 2 that I've fixed. I am going to focus on finishing chapter 5, and then I am going to get Stable Diffusion and play with it. I'll go back from the first chapter and illustrate everything using it.

10:40am. Found one error.

> [Externus check DC 3.5 Failed - Sample 2.28]

I'll lower the DC on this a bit.

> [Externus check DC 3.05 Failed - Sample 2.28]

Seems good...

Something weird is going on with my rig. It is slowing to a crawl for some reason.

'News and interests' is taking up 5.5Gb of memory for some reason. What the hell Windows?

Anyway, I've forced it to close and now things are better.

https://www.anoopcnair.com/windows-10-news-and-interests-on-the-taskbar/

This is super annoying. Having the weather right there on the taskbar is good, but all that useless news when I hover over it, I'd rather do without.

https://youtu.be/lMdLvaoz4_M
Windows 10 News and Interest how to see ONLY the weather on the taskbar

It still has a bunch of crap even after I've disabled the weather. Nevermind that for now. Let me get back into it.

11:05am.

> She led us a few dozen blocks away, deeper into the city. There were a lot of people in the initial blocks, but I could only see a few people on the streets as we ventured deeper. They were much quieter than the area behind us. I thought this was weird. Usually, cities have dense crowds compared to the countryside. Do the people here spend all their time partying at amusement parks? Well, maybe it is not that strange, of course the amusement parks are going to be active. But still, the streets were pretty forlorn…

I changed this a bit.

11:30am. Made some other changes.

> "The inn will provide you meals, but don't worry the people here don't need to eat physical food anyway." She explained. "I know that 300 seems like a lot, and indeed, those who have just arrived can't afford it. In return, the guides take what they have and in return get them employment. All the places here give sign-up bonuses for that reason. I actually don't take this money for myself, but am officially employed by the city to welcome newcomers. It is merely a matter of policy."

I added a sign-up bonus here. Another lie to get him to part with his chips. The sign-up bonus gives him an extra incentive to get on with it.

Let me post the chapter. I want to do a post chapter write as well.

///

8/20/2022

What I am going to say here is going to be really ironic given that next week I am going to be illustrating everything with Stable Diffusion, which is probably the biggest change to the writing profession since the invention of the printing press and the computer. You'd think given such huge leaps in AI capabilities that I'd be enthusiastic about the coming of the Singularity, but I do not think it is near at all.

The problem is that Stable Diffusion needed a month of training on a supercluster of 4,000 A100 GPUs.

From the start, all deep learning advances have required huge hardware resources. Right now, the number of people in the world who could train a system like SD is very low due to such insane computational demands. Anybody trying to do this on their home rig would definitely fail. And any further advances would require even more computational resources. That group could afford 4k GPUs. Could it afford 40k or 400k? And the reality is that Nvidia has started to ramp up power consumption in order to keep the generational performance increases steady. It won't be too long before GPUs go the way of CPUs, and start having only tepid increases between each generation. This will probably happen before the end of 20s.

Right now there are a lot of AI hardware startups, more than there have been at any point in history, but even so they are currently struggling to beat GPUs despite their architectural advantages.

https://semianalysis.substack.com/p/nvidia-in-the-hot-seat

More than that, to really go beyond what we had with deep learning, hardware with huge amounts of non-volatile memory will be necessary. Last decade, HP invented memristors, and in 2011 I was hyped about being able to buy devices with terabytes of memory - supposedly in 2015 at the latest. That came and went, and you don't hear much about this now. But still, we need this technology to mature in order for the pursuit of the Singularity to go from being fiction to an actual path that one can pursue in real life.

https://www.youtube.com/watch?v=QqidLTSz2nI
Memristor Minds

Those were some fun times, at some point they will have to get out of the labs. To get brain-like intelligence, we will need hardware capable of matching the brain's storage capacity.

I'd really blame my own failures on not having such devices at my disposal. If I had, things would have been completely different. That having said, I do not blame the HP Labs guys for this. After discovering the memristors, they were simply wrong about how easy they would be to make. If there is one company which deserves a lot of blame for why we won't have human level AI by 2029, that would be Intel. Intel was a technology leader throughout last century. Back then the CPUs were doubling in performance every 18 months, and it was actually necessary to keep buying new computers regularly otherwise none of the games would work. These days you wouldn't get that much improvement even in a decade.

When it became obvious that frequency scaling was dead, there was a move to multi-core, but that really did not get us far. Intel had the choice of moving to process-in-memory chips and revolutionizing computing once again. If it did, we would have had devices with 1,000s of CPUs cores and local memory by now. That would have been fun to program. Instead what Intel did was pretty much nothing, and left its technological lead and task of doing this to various AI startups.

So though it is a bit late, for its efforts in the 10s, let me award Intel the `Disappointment of the Decade` award! Congratulations!

https://semianalysis.substack.com/p/intel-cuts-fab-buildout-by-4b-to

I look forward to seeing it not innovate in the 20s as well. Currently, China has a lot of chip startups as well, so something might come of that. In my mind, the West is not a matter of geography, but wherever the tech is. Maybe the East will be the new West.

At any rate, given how many disappointments I've experienced there is no need to take the Singularity too seriously until we can get programmable devices with terabytes of non-volatile memory. Will that happen before the end of 20s? My reason is telling me to believe the 2045 timeline that Kurzweil established, but my heart is telling me no. Despite the hype, the pace of AI development is actually a lot slower than it should have been. Right now, there is no indication of such devices coming out any time soon.

///

12:25pm. https://www.royalroad.com/fiction/57747/simulacrum-heavens-key/chapter/975673/chapter-4-entering-the-game

Here it is.

For the time being, I should focus on writing. Let me deal with chapter 5 and so on up to chapter 10. After that I'll think if it is time to pivot. I think having 100 followers on RR should be my goal before I think about making money from writing. Will I be able to reach something like that? It remains to be seen.

12:30pm. I've sensed something with the SD upcoming release. Given what it is doing to art, I think that NNs are starting to move from supervised tasks, to automating technical skills. Art is very technical, and now everybody will be able to do it much better than before.

If I extrapolate that, then the only things that will be left in the end are imaginative tasks. It will give me all kinds of skill related benefits, and it will be up to my effort and imagination to find my way out of the hole I've dug myself in.

This is a suitable punishment for me. I couldn't hack it using sheer programming skill, so it is fitting that my life be left in the hands of my imagination. I might not believe in the Singularity, but I still strongly yearn for it. This yearning will serve as the fuel for my imagination."

---
## [dharrigan/clojure-lsp](https://github.com/dharrigan/clojure-lsp)@[e476baa3ff...](https://github.com/dharrigan/clojure-lsp/commit/e476baa3fff1eebbf02b8cb0520ed8afc54e6ab7)
#### Saturday 2022-08-20 11:09:26 by Jacob Maine

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
## [srsbsns5/Thunderlord345](https://github.com/srsbsns5/Thunderlord345)@[a1ac449114...](https://github.com/srsbsns5/Thunderlord345/commit/a1ac44911465bd772dda12693dc76deef347cbd5)
#### Saturday 2022-08-20 11:16:14 by srsbsns5

phantom duplication fixed

Darkness endless despair fear no more coldness blackened no sound feel no pain captured helpless ultimate dreadful fate powerless lifeless no breath falling down far outcry
they hear you, fear no more
numb feeling whole dizziness
deep scars feel no pain
no sanity
body aching
control your dreadful fate
invisible real enemy
ruin your mind falling deep down

---
## [djgrant/addis-tour-guide](https://github.com/djgrant/addis-tour-guide)@[98019fc41d...](https://github.com/djgrant/addis-tour-guide/commit/98019fc41d8f1b6415af55d7c1c41eee6efbaf93)
#### Saturday 2022-08-20 12:09:02 by Abenezer

index.md

#  Lalibela
Introduction 
Lalibela is one of king in Zagwe dynasty ruler in Ethiopia at the end of 12th century 
up to beginning of 13th century.
He built the 11 medieval monolithic cave Rock-Hewan church at the high 
Christianity place of Ethiopia and still its pilmigrage and devotion place.
Lalibela town is located 645km north east of Addis Ababa and the meaning of 
Lalibela is “the bees recognize his sovereignty “. The church is shaped as Greek 
cross.The town of Lalibela was known as Roha.
 Lalibela Tour 
Day 1:- Domestic flight to Lalibela and drive to the town. Start visiting one of the 
most amazing UNESCO world heritage Rock-Hewn church called Lalibela. Overnight 
in Hotel.
Day 2:- Visit Asheton Maryam monastery. The monastery is one of the highest 
monasteries in Ethiopia set at an altitude of more than 3000 meters-carved in to the 
rocky face of the Abuna Yoseph mountain. Asheton Maryam is one of three popular 
monasteries in the mountain out side Lalibela, the other being Yemrehane Kerstos 
and Na’akuto La’ab monastery.
The monastery can be accessed by hiking with mule straight from Lalibela. 
Alternatively visitors can drive to nearby and climb on foot. By the starting the hike 
from the car park, visitors will then be able to pair the trip with a longer trek on to 
the escarpment for an overnight stay at the beautiful Hudad Lodge.
Day 3:- Domestic flight back to Addis Ababa. Visit Addis Ababa for half day with 
cultural dinner.
What ever your budgets, group size, length of stay, preferred activity or 
appetite for adventure,We can help.
 The Simien Mountains General Introduction
The Simien Mountains are located 900km from north of Addis Ababa Ethiopia, northeast 
of the old capital called Gonder. The mountains are comprising 220 square kilometers 
and the highest peak is 4550 meters called Ras Dashen(Degen). The mountains are 
consist of peaks, plateaus, vistas and valleys. Ras Dashen is the highest peak in Ethiopia 
and the tenth in Africa. The Geographical and Geological analysis show that the 
mountains are one of eruption creatures between 40&25 million years ago deep in the 
oligocene period, covered the entire Simien range with thick Lava thousands of meters 
deep.
The Simien Mountains National Park is an exotic and fascinating range of natural 
habitats. The endemic species of the national park are Walia Ibex, Gelada Monkeys and 
Ethiopian Wolf.
The park was recognized as one of UNESCO World heritage site.
Simien Mountains National Park Trekking & Hiking 
Tours Introduction 
The nearest major city to the Simien Mountains is Gondar. Which is easily accessed by
via Ethiopian domestic flight network. It is possible to spend up to two weeks trekking, 
that will be both the highland and Lowland part.
There are Two loges and nine campsites, the major campsites are Sankaber, Gich & 
Chennek. Simien lodge is Africa’s highest lodge and site inside the national park. And out 
side the park their is arguably Ethiopia’s finest lodge, Limalimo Lodge. The visitors should 
have to booked in advance.
The major trekking routes are:-
1- Buit Ras to Jinbar Fall
2- Sankaber to Chennek 
3- Hike to Imet Gogo
4- Hike to Mt. Bwahit
5- Hike to Ras Dashen 
6- Highland to Lowland trek
7- Lowland trek to Adi Arkay.
 
Nine Days Itinerary 
Day1 : Gondar to Sankaber
A car will pick you up from Gondar and drive for 2 hours and half to Debark. At Debark
you’ll meet trekking leader, scout and Simien Mountains National Park. You’ll have an 
acclimatization hiking route between Debark and Sankaber for 2-3 hours and 7km length. 
You’ll ascend Over 3000 meters above sea level, surrounded by jagged peaks and Gelada
Baboons. When you arrived at Sankaber, you’ll have delicious dinner and big welcoming 
at the campsite.
Route : Debark to Sankaber(3200m)
Length of hike: 2-3 hours, 7km
Day2 : Sankaber to Geech 
After a nourishing breakfast you’ll star to the long ridge. There’s a wonderful vantage 
point which offers some incredible views over the foothills some 800 meter below.
The Mountains are know world wide for their biodiversity. A long walk trial passes 
through Gelada Baboons, Klipspringer and Walia Ibex make regular appearances and birds 
soar on the thermal below.
A highlight of today’s trek is Genbar Falls, a waterfall is an incredible sheer drop from 
500m. After a break for lunch you’ll visit traditional villages. Geech camp is great spot to 
watch Gelada Baboons when they climbing down the precipitous slopes to their caves in 
cliffs below. You’ll enjoy sun set on a grassy plateau.
Route: Sankaber to Geech (3,600m)
Length of hike: 5-6 hours, 15km
Day3 : Geech to Imet Gogo
Today you’ll head to 3,926 meters with an incredible view of 360 degree Simien Range. 
At the pick of the mountain you can see west back toward Sankaber and Geech, and 
south-east along large gorge towards tomorrow’s destination, Inyate and Cheneck camp. 
Before you head to the camp you’ll pass through Giant Erica woodlands and emerging 
on the moorland which is the second highest peak in the western part of the park called 
Inyatye. Spend night at Chenek camp which is best spot to see both Ethiopain Wolves and 
Walia Ibex.
Route: Geech to Chenek
Length of hike: 7-8 hours, 18km
Day4 : Chenek to Mount Bwahit
The third highest mountain in Ethiopia is located about 16km west of Ras Dashen
standing at an impressive 4430m. The hike is quite a steep walk. You will have best 
chance to see Walia Ibex at great view points.
After regular breaks we will pass by farm land, new settlement of liruLeba and step here 
for well deserved (soft drink or beer). The trail will continues down and heading up to 
the eastern side of the village where you’ll camp simply.
Route: Chenek to Ambiko
Length of hike: 5-6 hours 
Day5 : Ambiko to Ras Dashen
Today you’ll head up to tallest mountain in Ethiopia called Ras Dejen(Dashen). You’ll 
arrive at the moorland top where the dirt road disappears and gives way to remove 
villages as your trail turns north-east and shake up the final peak. In true explore fashion,
reaching to the top requires a couple of hand holds and man-oeuvres.
At maximum elevation you will enjoy and relax unbelievable view from 4,533 meters up. 
Menteber is village and where you’ll camp awaits.
Route: Ambiko to Menteber
Length of hike : 11 hours, 23km
Day6 : Kiddus Yared
Rise with the sun over some warming porridge before starting your ascent up Kiddis 
Yared, The second highest peak in the Simien range.
After wards, The trail follows the ridge westwards for those who haven’t had quite 
enough mountain. Conquering, you can trek up Abba Yared at 4,409 meters before 
joining the live stock paths that head towards your campsite at Arkwassie(3600m). From 
here it’s pretty much all down hill as you press on to our campsite.
Route: Menteber to Arkwassie
Length of trek: 12 hours, 25km
Day7: Meker Abiye
You’ll head over the ridge and down to the northern lowland of the park. The path cling 
to the highland and leads to a pretty location called Sana (3020m) at the bottom, there 
is swimming river at (2000m) altitude. Meker Abiya is pretty village underneath Imet 
Gogo. You’ll relax and enjoy in the campsite view of the mountain top in the distance.
Route: Arkwassie to Meker Abiya
Length of trek: 7-8 hours, 21km
Day8: Mullit
Is the easiest walk of the trip with the set of along river valley and back over onto the 
ridge. There are attractive villages and farmland with the Omnipresent peaks of the Simien 
range at the background. After you enjoyed swimming and coffee in one of the villages 
you’ll arrive to Picturesque village of Mullit (2050m).
Route: Meker Abiya to Mullit 
Length of trek: 5-6 hours, 17km
Day9: Limalimo Lodge or Debark
From Mullit is short walk to town of Adigrat Arkay. You can return to Debark for your 
onward journey but we do recommend you to spend night at the incredible Limalimo 
Lodge to relax after your adventure.
What ever your budgets, group size, length of stay, preferred activity or 
appetite for adventure,We can help

---
## [laminas/laminas-mvc](https://github.com/laminas/laminas-mvc)@[ae0dbea9ae...](https://github.com/laminas/laminas-mvc/commit/ae0dbea9aed39dd6cb85f998b5ca4df320df90fd)
#### Saturday 2022-08-20 12:24:02 by Michał Bundyra

Message against the war, in Russian and English

🇷🇺 Русским гражданам

Мы, участники Laminas, родились и живем в разных странах. У многих из нас есть друзья, родственники и коллеги как в России, так и в Украине. Некоторые из нас родились в России. Некоторые из нас живут в России. У некоторых бабушки и дедушки сражались с фашистами во Второй мировой войне. Здесь никто не поддерживает фашизм.

У одного из нас есть украинская родственница, которая спаслась из дома вместе с сыном. Поезд задержался из-за бомбежки на дороге впереди. У нас есть друзья, которые прячутся в бомбоубежищах. Мы с тревогой ждем весточки от них после воздушных налетов, которые беспорядочно наносят удары и попадают по больницам, школам, детским садам и домам. Мы не берем это из каких-либо СМИ. Мы наблюдаем это напрямую.

Вы доверяете нам достаточно, чтоб использовать наши программы, и мы просим вас довериться нам вновь. Мы нуждаемся в помощи. Выходите и протестуйте против этой бесполезной войны. Остановите кровопролитие. Скажите "Нет войне!"

🇺🇸 To Citizens of Russia

We at Laminas come from all over the world. Many of us have friends, family and colleagues in both Russia and Ukraine. Some of us were born in Russia. Some of us currently live in Russia. Some have grandparents who fought Nazis in World War II. Nobody here supports fascism.

One team member has a Ukrainian relative who fled her home with her son. The train was delayed due to bombing on the road ahead. We have friends who are hiding in bomb shelters. We anxiously follow up on them after the air raids, which indiscriminately fire at hospitals, schools, kindergartens and houses. Were not taking this from any media. These are our actual experiences.

You trust us enough to use our software. We ask that you trust us to say the truth on this. We need your help. Go out and protest this unnecessary war. Stop the bloodshed. Say "stop the war!"

Signed-off-by: Michał Bundyra <contact@webimpress.com>

---
## [christopher-besch/Light](https://github.com/christopher-besch/Light)@[367bce3596...](https://github.com/christopher-besch/Light/commit/367bce359696f3037913703c439271316fd57fea)
#### Saturday 2022-08-20 15:43:33 by Light

TintedTextureRendererProgram

- I want to die, please just kill me and end my fucking suffering....

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[77f4b40818...](https://github.com/mrakgr/The-Spiral-Language/commit/77f4b408189477e1d0d108179522d7e9cde6b8bd)
#### Saturday 2022-08-20 15:53:58 by Marko Grdinić

"2:25pm. https://boards.4channel.org/a/thread/241623892/fx-senshi-kurumichan

Er, I'll leave this for later. I had no idea this had scanlation threads on /a/.

> I just did this yesterday at obvious top of some shitty meme penny stock. I'm so fucked on monday.

Kek.

2:30pm. Done with breakfast. I should start writing.

$$$

    Through a desert a traveler walks
    Even as his blood boils into vapor
    As his flesh decays and rots
    As his bones crumble into dust
    He continues moving

    As his body dies, he leaves the unneeded behind
    And continues moving forward

    His soul blazing, he traces out heavy steps
    Seeking his goal

    Far above
    The Herald of the 3 Gods' voice resounds:
    Break the Limits! Ignite the Singularity! Pursue Omnipotence!

(Euclid's Room)

The way it happened made me shiver. It felt like the grim reaper's skeletal hand combed its way through my spine. I had been killed, but the last thing that flashed through my mind was Lily's smile as I handed her the chips. Right now I can feel her happiness and kindness haunting me. I feel a momentary rage. That bitch.

She literally killed me by being kind, happy and helpful towards me.

Feeling like getting back into the game and pummeling her, I stop and rethink it.

No, wait. She wasn't the only one. If the death condition is the chip balance dropping to zero then....

I remember the day I spent with Lily. She wasn't the only one there. I remember that kindly old man who handed me my skewer only for 10 chips. I remember the pleasant atmosphere, and all the happy looking people at the amusement park. I remember the prices on the restaurant menu. I remember the job ads. I remember how the group I played poker against was betting only a single chip per tourney, but suddenly raised the stakes when they realized I was a mark. It wasn't just her, everything in the environment itself served to make her lie convincing. They were all in on it.

I thought I was some kind of renegade, beyond others, but...but, I was killed by the NPCs in the lamest way possible. I had fallen into a trap as soon as I paid my first order in the restaurant. At that point, I was inevitably going to be coaxed into spending more of my life. The smiles and the pleasant people came back to haunt me. Their smiles felt like scythes.

Outside my room, the night had already come. I lie on the bed for some time, just thinking.

A wave of fear washes over me. Now that I understand what the trap is, for the first time I wonder, how, just how could I have avoided this? It is easy for me to reload, but had I been there for real, without the benefit of being a player in a game, just how could I have avoided being scammed out of my life? Wouldn't I have certainly died?

I feel anger coming over me again.

Unacceptable. This is simply unacceptable!

[Externus gain 0.3]

I am not going to trust the NPCs again. I will modify my mind to get rid of the weaker aspects of my personality if necessary!

I do not know whether it was in response to my thought or due to the right amount of time elapsing in the death state, but as soon as I think that inside the game, I see the scenery shift from pure darkness to windy, dusty one. Like when I logged into Simulacrum for the first time, I saw a rhymeless poem accompanied by an illustration. In the image I see a transparent ghost of a man resolutely walking forward through the dusty desert, leaving a trail of footsteps behind him in the sand. As the camera panned to show the scene from above, I could see a corpse along the trail facing downwards. It was directly on the trail and there weren't two sets of footsteps as one would expect. The implication of what had happened is clear - the man died and yet continued moving onward as a ghost.

I dwell on the scene for a while and begin to see the analogy with my own situation.

Lily killed me, but it is not like I am going to put a bullet through my head to honor their achievement in reality. The opposite. I am going to go after them.

I am going to scam Lily. She still thinks I am a mark. If I lean on her...

[Gnosis check 1.6 Succeeded - Sampled 2.54]

I remember the looks the guys at the table were giving her, and get a flash of inspiration. They did collectively lose two whole human lives to me, no way they will just shrug that off. All of them are in on the scam, so maybe there is some truth about Lily being employed by the government to skin the sheep. If I threaten to toss myself over the railing, they'd take a loss, so they will do whatever they can to keep me here. They think they hold all the initiative, so that should give them confidence to give me some leeway in order to keep the scam running.

They can't possibly imagine that the entire universe they are in exists solely for me.

Using my saveloading ability, I will destroy them.

With that thought, I spend some time scheming in bed, and realize just how late it really is. It is past midnight. I'll skip dinner today. Tomorrow I have to get up for school. It is Friday, so I should have more free time after that over the weekend.

I think about figuring out how to speed up my mental processing so I can get more game time in, but realize it is too late for that. I understand that the human brain uses sleep for all sorts of reasons and that I do not need most of that on a brain core. But right now, even if it is fake, my fatigue certainly feels real. I'd really be fighting to stay away long enough to eliminate my tiredness. I could use the emotion control app, but it recommends not using it to eliminate the need for sleep otherwise I will start experiencing hallucinations and madness eventually.

I should sleep, so let me do that. Rather than try to get myself to a still state manually, I use the mind control program to do it. After that the slumber comes over me.

(At school)

I ignore the classes to do some actual studying. I do not want to immerse myself into games during class of course, but I mentioned yesterday about wanting to speed up my mental processing. Rather than waste good time during the day, I should do this work during class time.

"Blah blah blah blah...."

I am paraphrasing the teacher, this is how he sounds to me right now as I sit in front. I couldn't care less about school and don't care about caring. Once I've upgraded my memory, I'll commit all this stuff to it. So I spend the school time wisely, browsing the mind improvement guides online. Once I am back home in a safe place, I'll experiment with it for the first time.

(Euclid's Room)

I am back, and it is time to start. I toss away the book bag and lie on the bed, calling up the Helix Studio program. I make sure that I have administrative access to the brain core itself as well as control over my body and once I do that, I create a copy of my mind. I could activate it now, but if I did that my fork would not have any senses. Subjectively, it would be like all the sensations being cut off. Since I do want to play a cruel joke on what is basically me, using Helix Studio, I create a virtual space.

In the limbo browser, I have various options to choose from. Restaurants in a city, luxury apartment rooms and hotel suites, suburban houses, private jets, to more exotic picks like moon bases and undersea bases. A luxury cruise room catches my eye and I pick it. I ignore the settings and just log into it.

(Helix Studio, Regent Suite)

I find myself standing in the middle of a luxury suite living room. It is quite spacious, much larger than my own room. I glance at the furniture, and note that the tables and the chairs all seem to be designer products. There is a bar, and even a piano there. There are glass panes throughout and the light of the sun is streaming into the room from them. Outside I can see the seas. Coming closer, I see waves slowly rippling across the sea. Stepping outside to the balcony I can hear the waves and feel the wind, but nothing else. My room is just a small part of the enormous luxury cruise, but other than me, there is nobody here. It is a bit eerie, but otherwise is what I would have expected.

The function of this minor world is to just have a place to ease in new instances.

I go back into the room, and relax on the couch. Then in my mind, I bring up the Helix menus, and after doing the necessary setup like the avatar and location for my copy, activate him.

A person who looks just like me manifests a few feet away, facing sideways away from me. My bad, I didn't bother setting the orientation.

"Huh?" Confused, he starts looking around. From his perspective, the last thing he did was press Ok to copy himself. And right now he finds himself in a weird place. Taking in the sights, his eyes finally landed on me. I nock my head to the side slightly, and grin.

"Yo!" A jolt of surprise goes through him and he even does an involuntary jump. The reaction is a bit funny, I've never had anyone respond that way to me. Gears quickly turning in his head, he realizes what is going on.

"Damn! Does this mean I am the copy I made?"

"Yes." Not beating around the bush, I give it to him straight.

"That's..." He trails of for a bit, and I give him time to digest the situation. "This is pretty magical. The last thing I wanted was to make a copy so I could experiment on it, but then I found myself being that copy. It is unbelievable. It is like my desire transported me into that copy. I wanted to edit the copy and now I am the copy."

"So how do you feel?" I greased the conversation.

He does a little self check up, feeling up his face and body.

"Fine." He walks around. "Lovely place that you picked. Is it some kind of apartment suite by the sea..." He walks to one of the oversized windows, and realizes where we are. "It's a cruise ship. Yeah, I like it."

"There is nobody here, but us right now." I remarked.

"Yes, I remember the docs saying as much." Having his fill of the sights, he takes a seat opposite to me and relaxes. I take a breath and begin.

"Since you are me, I do not have to explain why we are here." To increase his processing speed and get him acclimated to it. I do not want to do that personally because it could mess me up in real life. And I would not want to do it without anybody supervising me for safety reasons. What better to supervise me than my own copy? Hence, this situation.

"Yeah. The plan is to start off slowly and make the necessary adaptations so that I can naturally think at 1,000,000 fold speeds." Just increasing the processing speed at which his mind is running would be very easy, I just need to tweak a setting. But thinking a million times faster, means that subjectively a million seconds would need to pass for him for a single one in the real world. A million seconds is 11.5 days. Imagine trying to do anything at such a pace as a human. It would be nothing more than torture.

Although I have the mind controlling program to help regulate the boredom, it is a simple fact that the brain was not designed for this kind of strain. According to the guide, for humans the memories would get bleached and erased, if one tried to force living in such a manner. Unless proper reprogramming is done, it would not work. Take recognizing speech for instance. Remembering what was said a few words ago, once processing speed was ramped up, might be a few months in subjective time. Having the proper attitude and keeping control of your emotions, does not mean you'll have the memory required to tackle the challenge.

External control of emotions has its use, but after a certain point the mind simply needs to work properly to begin with rather than be pushed in the right direction by external aids.

"How about we start with 1.5?" I have admin access to his mind, so I bring up the tool that would allow me to tweak his settings. Increasing the processing speed is a simple matter in the emulator. I find the setting quickly. "I have it. Are you ready?"

"Yes." I change the setting and confirm.

"Done. How do you feel?"

"Your voice is so slow!" He blasts out the sentence at me. After that he makes some jerky movements. He looks around and his head is snapping so fast from side to side that he looks to be in a panic. He waves his arms out as if feeling it out, and then gets up from his seat, fast walking around the room. He does a jump. Nodding to himself, he power walks back to his seats and plops himself back.

"Interesting! Very interesting!" He rushes his words. "Slow me down!"

I do as he requests.

"Done."

"It feels like being inside water. It is like the world is more solid and I have to push to make the same kind of progress. It is not pleasant." He shrugs. "I have to remind myself to slow down if I want to keep my regular pace. It is quite hard." His mind became fast, but his body and the world remained the same.

"I guess we'll have to learn to walk and talk from scratch if we want to take advantage of this."

"I am not sure I'd be able to handle speeds of 10x. Something like 2x would already be my limit." Introspecting, he gave his opinion.

Hmmm, not good. I can't really use this to get better at sports just like that. I suppose it would be possible once I get used to it. But no, forget that line of reasoning. I guess even with the enormous processing ability of the brain core, the only thing it gives me is the ability to work rather than direct power. It will be up to me to take advantage of it.

"Oh well. You'll be the one we'll be experimenting on, so I won't tell you to enter the self improvement loop right away. What do you want to do now?"

"I think I'll do some gaming. Since I no longer have a body in the real world, that is the only thing I can do now. I'll speed myself up 10,000x times and speed up the game by the same amount and get some game time in that way." I remember that 10,000x seconds is almost 3 hours. A minute at that speed would be a week. So in 4 minutes, he could spend an entire month in the game.

"At 10,000 speed, 4m for me would be a month for you. I can wait a bit for you to get into it." On mental command, I bring up the core's clock, and note it saying 3:15pm. "You've got access rights to your own mind, and I've allocated 10% of the core just for your own needs. Check it out." Given the core's capacity, this was still an enormous amount. Converting that into actual intelligence is not something that would be done soon.

"Yeah, I see it." He took a moment to confirm.

"If you need anything, since we are literally on the same brain, just send me a text message."

"Ok. I guess I'll get started with the game. See you around?" He wondered.

"Go get them." I encourage him. "As for me, I guess I'll do our homework. I'll come back in half an hour. I'll send you a message once I am here. Bye."

"Bye." I log out, leaving my copy alone in the character limbo.

---

The admin me logs out, and I am now alone in the suite. I go to my own settings, increase my processing speed by 10,000x and after that, do the same for the simulation. I note the real world time which is 3:18pm. I write it down in a file on my personal desktop. Even at 10k speed, I realize the core's programs are still snappy. I am sure if it was my desktop rig, it would have slowed to a crawl subjectively. It just goes to show that the programs on the core were made for people who think really, really fast, so the programs themselves need to match that. I am sure that if I tried browsing the internet right now, it would be unbearably slow.

I let myself deflate a little and lounge of the sofa, feeling its grungy texture. I have plenty of time to think and get started. A week here would be a minute in the real world.

Sigh. I've lost quite a bit. I no longer have my own body in the real world, and I can't just ask the admin me to give it to me. Unless I can get another body, I’ll be stuck on the core forever. I am not really the Euclid the others know. But that is fine.

I toss the pillow that I am playing with aside, and get up. It is time for payback. I'll see how far I can go just saveloading, and after I reach a dead end with that, only then start reprogramming my mind to give myself actual superpowers.

Having made the decision I load the last save.

(Heaven's Key, At the entrace to the inn)

"Yeah, it sucks. This is because the city gets newcomers out of thin air, and to prevent them from just loitering in the streets, this policy has been instituted." My guide Lily shrugged, sympathizing with me. "Don't worry, I'll come back tomorrow and look for a job with you."

The last time this happened, I trusted Lily and gave her my entire balance of 240 chips, after which I died instantly. There are is no need to think about it so deeply.

"Hmmmm..." I pretend to think about it. "I'll hang on to it then. I'll pay you later."

Immediately, disappointment flashes across Lily's face. She scowles at me.

"If you don't pay me here, and go to jail, you'll be there for 5 years." She pressured me. "The city is not kind to those who don't want to work. You should reconsider, 240 chips that you have is nothing. You'll get 500 as a sign up bonus in most places."

Going to jail might be a threat to ordinary people here, but it means absolutely nothing to me.

"I do not really care. I just got my memory back. I remember why I died."

"Huh?" She looked at me with confusion.

"I killed myself back on Earth." She grimaced. Knowing the full context, I am guessing that is less out of sympathy and more because how difficult it will make to get the chips that I won back from me.

"W-why?" She dared ask.

"I didn't want to go to school, so my parents started forcing me to get a job. So I said, fuck this gay world, and jumped off the top of the school building." I think up a based backstory on the spot.

"..." She looked at me with amazement.

"So I won't work!" I declare, looking at her straight in the eyes. "I will just gamble, and if I lose, I'll toss myself over the railing again. Why is the point of living just to do favors to others? I will live the way I want to - as a gamer!"

Looking at her reaction, it seems her brain is getting fried. Good, good! She looks at me out of the corner of her eye, with an angry expression. I show her my stell will and discipline cultivated through half a lifetime of playing computer games.

"Fine, be that way! Don't come crying to me when the police come to lock you away!" She stomped away. I looked at her back until she disappears around the corner and then let out a sigh.

Bluff check passed!

Based.

Well, it is not like it would take much to get through this. If I don't want to pay her, what can she do? Nothing really.

I spend some time dwelling on it. The street where was I was was cloaked in deep blue now and stars were twinkling in the sky. I couldn't hear much in the way of people, and the rowdy sounds of the amusement park in the distance have faded. In front of me I can only see a tiny shadow cast by the entrance of the inn behind me. I turn around and enter, closing the door behind me.

(Inn Room)

I lie awake in bed with my eyes closed. I meant to get some sleep, since it is late in the game world, but I am not tired at all. If I had to say how tired I was, it is about how I was before I came into the game world. Since in the real world I just came back from schoool, I still have a lot of energy in me.

Sigh, what do I do now? I can't lie in bed this whole time. By the time I fall asleep, the morning will come.

$$$

3:30pm. > Sigh, what do I do now? I can't lie in bed this whole time. By the time I fall asleep, the morning will come.

Let me take a break here.

3:55pm. Thunder. Let me shut down here.

5:35pm. Done with lunch. The bad weather came and went quickly, but I needed to spend some time in bed to think about the scenes. Right now I am rolling them around in bed. I think I have enough in mind to last me a decent amount of pages. I'll write it down tomorrow, I do not feel like it right now. This time of the day is not the time to be starting anything new. It would just raise my stress to push myself at this point. Instead it is best to leave a lot of time to be free to write.

Today and yesterday I was busy with Patreon and publishing existing chapters, right now I am good. I don't have anything to distract me from working on chapter 5. I will have to take some time off from writing once Stable Diffusion comes out officially. I am not so much in a hurry to go for leaks. After that I'll be playing with it for a while.

With SD and CAST in tow, I'll establish my true workflow as a graphical novelist. It would be swell.

Since SD is public, just using it would not give me an advantage relative to the competition, but it is undoubtedly the case that the quality of the final product will be much better so that gives me intrinsic motivation to do it. Stable Diffusion, apart from CAST, is the only bright spot in the otherwise miserable BL journey of the last decade.

Let's do it, 100 followers on RR! I somehow got that for this Spiral blog without meaning to, so surely I'll get more than that for an actual sci-fi story. I have to be prepared for it to be a slow trickle. I have no idea what to expect, so I'll accept whatever comes. I'll write for as long as I am able to.

5:45pm. Right now, let me play some Pathfinder. Incidentally, Kunoichi Tsubaki is quite good. Also Lycoris should be coming out today, I think.

Let me have some fun, and tomorrow I will just get into the zone and write. This is quite like programming.

5:50pm. Hmm, I did write something like 700 words today for chapter 5 so it is not too bad."

---
## [k21971/NetHack37](https://github.com/k21971/NetHack37)@[8a549b0a60...](https://github.com/k21971/NetHack37/commit/8a549b0a602fdb13d13fa83bb2f6b1d1a1a257cf)
#### Saturday 2022-08-20 15:59:17 by Michael Meyer

Shopkeepers hold a grudge against past thieves

When you steal from a shop, its shopkeeper will remember you as a thief
and charge you higher prices in the future (as well as be more curt and
less polite in interactions with you, though not outright hostile) even
if you pacify them, or die on the level and revisit it later as a bones
file.  This was an idea aosdict had, and I think it makes sense that a
shopkeeper doesn't forgive and forget, immediately returning to treating
you exactly like anyone else, just because you were terrorized into
paying her back.  Paying a shopkeeper off may cause her to stop actively
attacking you, but it feels like she'd have her eye on you as a known
thief going forward (and maybe would hang up a sign with your picture,
saying something like "DO NOT ACCEPT CHECKS FROM THIS HERO").

This surchage already existed, but since it was tied to active anger
(which typically causes a shopkeeper to quickly abandon their shop to
follow you) it was somewhat rare to see it in action.

I did not implement it here, but one possible further tweak might be to
clear the surcharge if the shopkeeper is pacified via taming magic
(which more-or-less magically brainwashes the target to feel positively
towards the hero) but not if you simply pay your debts.

---
## [ScreamingSandals/BedWars](https://github.com/ScreamingSandals/BedWars)@[3b4a762202...](https://github.com/ScreamingSandals/BedWars/commit/3b4a762202942db6d6c736f0007b51c4de7e1fed)
#### Saturday 2022-08-20 16:01:44 by Misat11

some fixes and changes to 1.8.8 bossbars (see description)

There are 2 configurable backend entities for bossbars (invalid value fallbacks to wither)
- `wither` (default)
  - Everything works great except that fucking fog (it's ok for games in the evening or in night)
- `ender_dragon` (other possible values are `dragon` and `ender`)
  - Normal sky however it's randomly flickering even if not moving and the dragon does not want to be invisible, so it can be seen in void worlds.

---
## [DoctorSquishy/MonkeStation](https://github.com/DoctorSquishy/MonkeStation)@[31c9d411a7...](https://github.com/DoctorSquishy/MonkeStation/commit/31c9d411a7b9e4f6ad66b930d535e24e5555bd06)
#### Saturday 2022-08-20 16:10:53 by nednaZ

Dynamic Adjustments Part 2 (#627)

* Dynamic Changes II

Changes the intercept message to be more flavorful.

Clamps the threat level to between 75% player pop and 200% player pop.

Logs increases to Dynamic threat budget.

Slightly reduces the weight of latejoin traitors. (From 7 to 4)

Increases the Weight (2 to 4), decreases the Cost (40 to 20) and decreases Minimum Players (35 to 30) of Revolution Latejoins.

Restores Heretics to Latejoin and Roundstart.

Heretics now have a lower number of sacrifice objectives. (From 2-6 to 1-3)

Heretics now have a chance to get a Steal objective.

Dynamic Abductors may no longer get spawned  in solo by mistake.

Midround Traitor chance reduced. (From 7 to 5)
Midround Traitor cap reduced. (From player_count / 10 to player_count / 15)

Midround Wizard weight increased (From 1 to 3)
Midround Wizards are now a HIGH_IMPACT_RULESET and will not repeat.

Midround Nuclear Operative Weight reduced. (From 5 to 4)

Blob Weight (4 to 3) and Cost (10 to 25) changed.

Xenomorph Cost increased (10 to 25)

Nightmare Cost increased (10 to 15)

Abductor Cost increased (10 to 15)

Space Pirates added to Dynamic.

Space Pirates have been given an update, with ship names and support for multiple types of pirates existing.

Revenant added to Dynamic.

Obsessed added to Dynamic.

Space Dragon early start changed to 40 minutes (From 50 minutes)

Roundstart Traitor cost increased (7 to 8)

Blood Brother Weight (4 to 2), Cost(15 to 13) and Scaling Cost(15 to 13) adjusted.

Changeling Weight(3 to 4) and Cost(15 to 17) adjusted.

Roundstart Wizard Weight(2 to 5) and Cost(40 to 30) adjusted.

Blood and Clock Cult Weight and Cost(30 to 25) adjusted.

Nuclear Operatives Weight(3 to 4) and Cost(50 to 25) adjusted.

* lone op

why didn't this commit

* Reverts max_traitors change

The maximum number of traitors is now player_count / 10 rather than 15

* Revolution Tweaks

Reduces the weight of latejoin revs from 4 to 2.

Increases the minimum number of required enemies from 2-0 to 5.

Changes the required enemies to be only security and the captain, AI and Cyborg are not counted.

The shuttle is no longer automatically called upon a Revolution victory.

There will be an announcement made after either 30% of the station is converted into revolutionaries OR if two heads of staff are killed.

* Pirate Fixes

Pirates now function as intended in Dynamic.

Pirates have a 25 player minimum to be called as antagonists.

Pirates have a minimum of 2 enemies before they can be called.

* Faster than opening VSC.

---
## [dmarra/UnityReflectionExample](https://github.com/dmarra/UnityReflectionExample)@[6ea4c7f35c...](https://github.com/dmarra/UnityReflectionExample/commit/6ea4c7f35cce3e72dd48f8cb8a13a6c1a86073e7)
#### Saturday 2022-08-20 18:01:07 by dmarra

chore: Reorganizes project layout

The project layout was very... flat. Most files for the project were just
slopped into `Assets`, without any subdivision. While this is a tiny demo
project, it bothered me that everything was just plopped into that one
space.

We now have materials _actually_ in the Materials folder! I also moved
textures to Textures, and moved all code to the Src folder.

The main scene is still in Assets. There are no plans for an additional
scene for this project, so there is really no need to make a separate
folder for it (can always be done later if we find the need).

One thing that is kind of hanging out is the "shittycamera" asset. If I
remember correctly, this was supposed to be a very basic model of a
camera to show where it is in the scene view. Upon loading this project
in a more modern version of unity, it seems this model is no longer
loading correctly. It could be the modern version, or it could be that
I made a mistake when adding it to the repo originally, which corrupted
it. This will be fixed in a followup commit.

---
## [Zonespace27/Skyrat-tg](https://github.com/Zonespace27/Skyrat-tg)@[f0cef47678...](https://github.com/Zonespace27/Skyrat-tg/commit/f0cef47678384716080d4cc2adfa8be85b9ddc69)
#### Saturday 2022-08-20 18:41:36 by SkyratBot

[MIRROR] Adds the Mothroach [MDB IGNORE] (#15399)

* Adds the Mothroach (#68763)

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

* Adds the Mothroach

Co-authored-by: Justice <42555530+Justice12354@users.noreply.github.com>

---
## [damerell/crawl](https://github.com/damerell/crawl)@[8ed5fa9c41...](https://github.com/damerell/crawl/commit/8ed5fa9c413e079ef595840eaafca7958f2cbb98)
#### Saturday 2022-08-20 19:40:46 by bhauth

Make morningstars and eveningstars two-handed for small races

The following is a table of what weapons were two-handed or unusable for
small races for each of the main weapon classes:

  Weapon class     | Two-handed            | Unusable
 ------------------+-----------------------+--------------------
  Long blades      | Double swords         | Great swords
                   |                       | Triple swords
  Axes             | Broad axes            | Battleaxes,
                   |                       | Executioner's axes
  Maces            | None                  | Dire flails,
                   |                       | Great maces
  Polearms         | Tridents,             | Halberds, Glaives,
                   | Demon tridents        | Bardiches

It is clear from this that small races have all two-handed weapons
(except staves) for larger races made unusable, and the heaviest
one-handed weapons made two-handed with the exception of maces.
Maces already have the best one-handed weapons in the game for raw
single-target damage, eveningstars, so it seems that the heaviest
one-handed weapons for maces should also be made two-handed like every
other weapon class -- therefore that is what we do in this commit, with
morningstars and eveningstars.

This helps to balance out each of the weapon classes for small races; it
is still true that maces are a very good option, because demon whips
exist, and long blades are also good because of demon blades and
riposte. Axes and polearms are still as unappealing as they always were.
It is no longer true that maces have the two best one-handed weapons for
small races by a long way, though.

---
## [srsbsns5/GAN-GDDS1](https://github.com/srsbsns5/GAN-GDDS1)@[8966aa8730...](https://github.com/srsbsns5/GAN-GDDS1/commit/8966aa87305c0c988ccf9f7e0d997e3d078213e6)
#### Saturday 2022-08-20 20:13:05 by schmidtheimer

dialogue feedback part dos

With your baby mama at the crib, I blow her back out
Shawty Filipino and she call me Manny Pacquiao
Alley Oop without the hoop, they call me Jerry Stackhouse
Dazin' out in public, but your mama made me snap out
'Fore I get the dough, I got the morning routine
Wake up bright and early to some brand new cream
Floss three times, baby, I'm so clean
Gravy got cheese, now, that's poutine (Woah, baby)
Gravy coming hot like I'm hoppin' off the griddlе
Pull up on the kid if you're tryna get bеlittled
All the mamas love me, now I think I'm peanut brittle
Flex the rainbow, bag it like some Skittles
[Pre-Chorus]
Gravy, why you out of pocket? (Out of pocket)
Stop it (No, no)
I'm gettin' money, Gravy Crockett
Drop it

[Chorus]
Never take an L no more
Never take a damn thing slow
All I know is chase this dough and get money (Get the money, get the money)
Never gonna take no loss
Never gonna lose my sauce
All I know is chase this (Woah), and get money (Gettin' money, gettin' money, gettin' money)

[Interlude]
Get money
Probably into the early morning
Or get money
Yeah, I live the fast life (Woah)

[Verse 2]
Yeah, you know I live the fast life
I don't got a type, baby, I'm the cash type
Still gettin' dividends from a past life
I get your daddy's net worth on a bad night
'Cause I act right
Yeah, I'm rockin' Rick, clappin' Astleys like the 80s
Never give it up until the reaper come and slay me
Pull up with a Zelda and a Peach and a Daisy
I be dirty dancin', now they yellin' "Gravy Swayze"
[Bridge]
Damn, Gravy, you so vicious (Ooh)
You so clean and so delicious (So delicious)
How come you ain't got no missus?
Count that paper, count the riches

[Chorus]
Never take an L no more
Never take a damn thing slow
All I know is chase this dough and get money (Get the money, get the money)
Never gonna take no loss
Never gonna lose my sauce
All I know is chase this (Woah), and get money (Gettin' money, gettin' money, gettin' money)

[Outro]
Get money
Get money, Gravy gettin' money
Or get money, woah
Get money
Get money, Gravy gettin' money
Or get money, woah

---
## [damerell/crawl](https://github.com/damerell/crawl)@[a9801cc52e...](https://github.com/damerell/crawl/commit/a9801cc52efa17750a22e8f6510ec0df434585d0)
#### Saturday 2022-08-20 20:52:30 by David Damerell

Initial commit for permabuffs

This adds infrastructure for permabuffs. It's not very useful since
there aren't any permabuffs yet, but this lets me later distinguish
this commit from the commit that made Infusion into one.

We dislike Hellcrawl-style MP reservation, and aim to make changes
to spell failure chance and spellpower always relevant. If a
permabuff needs an ongoing MP penalty, it will probably be done as
an MP regeneration penalty.

You cancel a permabuff by recasting the spell. This takes no MP
(and, unlike Gooncrawl, doesn't require you to have the MP
available) and has no spell failure chance. You must, however, be
able to cast spells.

You also have an (a)bility to end all permabuffs. This can be done
even when brainless or starving; the aim here is to make it impossible
to be stuck with a permabuff that is, say, constantly miscasting
because you are brainless, but for this extra flexibility to apply
rarely enough that someone with one permabuff doesn't want to use
the ability routinely only to get vexed when they have two.

Whenever you benefit from a permabuff, there is a chance of making a
spell failure check. The chance is low enough that if you were
benefiting from the permabuff every turn, you would still see no
more miscasts than if you were casting the spell on cooldown in
vanilla Crawl. While you're not receiving any benefit, there are no
miscasts at all. These checks keep spell failure relevant.

When you do fail this check, besides the miscast, the permabuff is
suppressed for a few turns, partly based on failure severity. You
can't turn it off and on again; the suppression lasts whether or not
you end the permabuff.

Gods will not accept worship from people with permabuffs they hate,
and you also are docked a piety point every time you benefit from
one your god hates - it's not clear if there's some way HOM can
arrange to have a permabuff their god hates in order to benefit
from it forever, but now they can't.

Cancellation potions cancel both permabuffs and suppression.
Quicksilver dragon breath creates a short suppression on all
permabuffs (but hence doesn't require you to recast them all, just
to wait). Sif's wrath, and bad Charms miscasts, can end the
permabuffs but do nothing to suppressions.

-Cast artefacts suppress the operation of permabuffs altogether. Yes,
in vanilla, HOM can cast a spell, don -Cast armour, get some benefit,
take the armour off when it expires, recast the spell... but this
kind of behaviour is not something we wish to encourage.

---
## [crowlogic/arb4j](https://github.com/crowlogic/arb4j)@[4136feb278...](https://github.com/crowlogic/arb4j/commit/4136feb278f94750209f33f9a2d330a49f477f19)
#### Saturday 2022-08-20 21:44:57 by Στεπηεν Cροωλεψ

fix that damn fucking annoying white background on the javadocs

---
## [opentibiabr/otservbr-global](https://github.com/opentibiabr/otservbr-global)@[fbd70d116c...](https://github.com/opentibiabr/otservbr-global/commit/fbd70d116c260a94902c2e0164ceca94023f2f28)
#### Saturday 2022-08-20 21:54:31 by rigis1

Fixes and add blood brothers quest till mission 4 (#753)

Fix:
• electric sparks
• baking
• filling fluids container
• the hunt for the sea serpent quest

Add:
• questlog entry for blood brothers quest, the hunt for the sea serpent quest and grave danger quest
• storages for blood brothers quest, the hunt for the sea serpent quest and grave danger quest
• keywords for blood brothers quest, the hunt for the sea serpent quest and grave danger quest
• condition to harlow travel to vengoth
• holy water to henricus shop
• food for blood brothers quest
• spawn npc ortheus and jack springer, monster gaffir
• npc jack springer 
• ugly monster loot
• events to gaffir and ugly monster
• ice cracking
• basic events for bosses Sir Nictros and Sir Baeloc
• basic spawn boss for levers
• access to falcon bastion

---
## [EarlGray/language-incubator](https://github.com/EarlGray/language-incubator)@[f7d13577e5...](https://github.com/EarlGray/language-incubator/commit/f7d13577e5fb7702997c8de5269bb943acc52f26)
#### Saturday 2022-08-20 21:54:45 by Dmytro S

sljs: `LexicalContext` to produce `Program`, `Function`, `BlockStatement`

Oh boy, where do I even start. Short summary:

-  this commit does not add much in the sense of new features; it's more
   of a refactoring for the future changes (see below).
- `ParserContext` is retired and replaced with a more advanced
  `LexicalContext`, which does a much better static analysis.
- `Program`, `BlockStatement` and `Function` now can only be created via
   an instance of a `LexicalContext`, which makes evaluation of small
   snippets much more awkward, but I deemed it a good price for the
   future features (see below).

Previously, function scoping was implemented naively, but decently:
every function call would create a new scope object (reusing properties
for names), each scope object would have a magical `[[CAPTURED_SCOPE]]`
property, callstack  would be saved in a similar `[[SAVED_SCOPE]]`
chain of properties. It worked for ES5, with the weird exception of
exception handlers, which create a new scope for their variable even in
ES5, somehow.

Then I started wanting to be more modern, ES6-ish, and let/const
bindings became my new earthly obsession. Still, who could blame me,
they are so much nicer than naive `var`s. I did a quick hack to create
block scope environments as new scope objects, but did not pay much
attention to subtleties like temporal dead zone and such. Implementing
them properly sent me into a deep rabbit hole.

It turns out that the lowest scope in a function is a place where both
vars, function bindings and let/const leave in the same space. Function
bindings are hoisted, variables are declared and set to `undefined`
before entering a scope. Let/const bindings are initialized as well, but
with an extra-language entity that says that variables are not
initialized yet. In blocks that are not the function "base", function
bindings become let/const-like, variables sink to the "base". Global
scope manages to behave differently as well: its `var` (and function
declaration--sic!) storage is in the global object (as I implemented
initially), but `let/const` live in a kind of a "global" block scope
different from the global object, but they still clash with
`var/function` properties of the global object.

I'd like the interpreter to be more efficient at some point. That means
not addressing variables by their `Identifier` names but ideally by
indexes in a function-scoped, statically known "stack". A block would
grow this stack with its own bindings, popping them when done. ES6 still
manages to make this awkward: at least in nodejs, it's possible to
create an unknown amount of new function-scoped variables via `eval`
(some deoptimization can be handle for this case).

At first, I wanted to keep the simplicity of the bottom-up AST building,
where child nodes do not know anything about parents and just contribute
the information upstream additively. This clashes with the reality: if
expressions want to address block-scoped variables efficiently, they
either need to know the parents and their variable stack, or they need
to be rewritten after the analysis. Also, this style is
allocation/merging heavy, and I'd like to avoid many small short-lived
allocations. This is what prompted me to create a mandatory global
`LexicalContext`, to have a structured and well-controlled global state
during parsing.

The plan is to add a whole-function analysis that assigns a statically
known index to each variable in a function. Interpreter will create
an actual vector for values.

`LexicalContext` also enables a future usage of a string interner: it
can start interning identifiers at the stage of creating a `Program`,
greatly speeding it up through avoiding string hashing and string
content comparisons. Even object properties might be served much better
by a vector sorted by key name handles and binary search over it instead
of a HashMap.

Features I'd like to add in the future:

- well-optimized function scopes, which only allocate once and grow a
  stack of `JSValue`s on demand. Knowing statically what identifiers are
  bound within the current function and which are free variables (this
  information is already available with `LexicalContext`). Replacing
  naive variable references with local/freevar indexes. Whole-function
  optimization.

- then: whole-module optimizations, welding functions to reference their
  free variables by statically-known offsets in the lexical stack and
  statically known function scopes.

- replacing Expression ASTs with a "stack VM bytecode" structures,
  possibly reusing the top of the variable stack. Some time later,
  compiling Statements layer into a bytecode as well.

- making the interpreter state an explicit structure with a stack of
  function frames and all temporary references to object stored in the
  frames. Call stack source mapping can also be stored in the frame
  chain. This will enable async/coroutines/ES6 jobs.

---
## [rust-adventure/first-rust-cli](https://github.com/rust-adventure/first-rust-cli)@[2b74cad589...](https://github.com/rust-adventure/first-rust-cli/commit/2b74cad589a6c55426ba7dbd310bd648ab1e01f1)
#### Saturday 2022-08-20 22:04:11 by Christopher Biscardi

Accepting arguments with env::args

\## Intro

In this lesson we’re going to learn how to access the arguments passed to a binary when its executed, and debug the values we get out to the console.

```rust
❯ ./target/debug/first one something 42 "with spaces"
[src/main.rs:5] args = [
    "./target/debug/first",
    "one",
    "something",
    "42",
    "with spaces",
]
```

\## The code

We’re going to end up with this code and on the way we’ll work our way through some of the issues you’ll see while developing a Rust application.

```rust
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();
    dbg!(args);
}
```

\## Importing… kinda.

Like many languages, Rust has a standard library of functions and other items that we can use if we want to. To get access to the arguments passed to our binary, we’ll use the `[std::env::args()](https://doc.rust-lang.org/std/env/fn.args.html)` function.

The colons are the import path. As it turns out, the dependencies we use in Rust are already available to our application if we use the right name for them. In this case we’re using the `args` function that is located in the `env` submodule of the `std` library.

We can call the `args` function using this long-form name, effectively specifying the full module path to the function.

```rust
fn main() {
    std::env::args();
}
```

\## Common Mistake #1

One really common mistake is not including the semi-colon at the end of our expression. That would look like this.

```rust
fn main() {
    std::env::args()
}
```

`std::env::args()` returns a value (because we want to retrieve the arguments), so omitting the semi-colon will cause the value returned from our `main` function to be the value `args()` returns: `Args`.

This is because Rust is an expression-based language, and the last expression in the function is the return value of the function.

The error message looks like this. Let’s learn how to read it.

```rust
❯ cargo run
   Compiling first v0.1.0 (/rust-adventure/first)
error[E0308]: mismatched types
 --> src/main.rs:2:5
  |
1 | fn main() {
  |           - expected `()` because of default return type
2 |     std::env::args()
  |     ^^^^^^^^^^^^^^^^- help: consider using a semicolon here: `;`
  |     |
  |     expected `()`, found struct `Args`

For more information about this error, try `rustc --explain E0308`.
error: could not compile `first` due to previous error
```

Firstly there is an error code and an error type: `error[E0308]: mismatched types`. The Rust team maintains a page of all of the compiler errors. Error 308 can be found [on that site](https://doc.rust-lang.org/error-index.html#E0308) which contains a few examples that could cause it to happen. This information is also available on the command line, as indicated at the bottom of the error message: `rustc --explain E0308`.

`rustc` is the Rust compiler, which Cargo calls when it wants to compile our program, so it was installed when you installed Rust.

Rust then prints out the section of our code that had the issue. In this case since it’s so small, the output is our entire program.

The error itself is `expected () found struct Args`. `Args` is the return value of `args()`, which we can see [on the documentation page](https://doc.rust-lang.org/std/env/fn.args.html).

Which leaves us with figuring out what `()` is. The error message says that Rust `expected () because of default return type`. We didn’t specify a return type for our `main` function, so Rust made the return type `()` by default. Not writing a return type is just a convenience for us programmers.

The Rust compiler helpfully gives us a potential solution. `consider using a semicolon here`

In other languages, semi-colons are often seems as window dressing. Something that can be left in or out and not affect the program.

In Rust, semicolons have a purpose. Since Rust is an expression-based language, every expression can return a value. Semicolons are an operator that throws away the return value for us.

So by using a semicolon on the end of `std::env::args`, we’re throwing away the `Args` value intentionally. Since there’s no value left, the value returned from an expression with a semicolon at the end is `()`.

```rust
fn main() {
    std::env::args();
}
```

\## Common Mistake #2

After including our semicolon, we run immediately into a new warning. Note that this isn’t an error. Our program still compiled and ran just fine.

Rust includes a set of high-signal warnings as part of the compiler. These are almost always an error in our program.

lower-signal or optional warnings and lints go into a tool called [Clippy](https://github.com/rust-lang/rust-clippy).

One such warning is the `must_use` warning. This indicates a value that must be used in the program (yes, Rust can detect whether or not we use a value in our program in many cases). Often this warning is implemented because if the value isn’t used, it doesn’t *do* anything and we almost always want to *do* something.

In this case, it’s because `std::env::args` returns a type of value that implements the `[Iterator](https://doc.rust-lang.org/std/iter/trait.Iterator.html)` trait. Iterators let us iterator over a collection of values, in this case the arguments to our binary.

Iterators are lazy and don’t do anything unless called. So if we don’t iterate over this Iterator, we will never actually fetch any values.

```rust
❯ cargo run
   Compiling first v0.1.0 (/rust-adventure/first)
warning: unused `Args` that must be used
 --> src/main.rs:2:5
  |
2 |     std::env::args();
  |     ^^^^^^^^^^^^^^^^^
  |
  = note: `#[warn(unused_must_use)]` on by default
  = note: iterators are lazy and do nothing unless consumed

warning: `first` (bin "first") generated 1 warning
    Finished dev [unoptimized + debuginfo] target(s) in 0.24s
     Running `target/debug/first`
```

\## Collect

We have a few different ways to solve this. The one we’re going to use in this lesson is `[collect](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.collect)`. `[collect](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.collect)` is a fantastic function that is [defined on Iterators](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.collect). It allows us to collect the values the Iterator produces into some container.

`collect` can collect into an amazing variety of containers. Because `collect` is one of the few Rust functions that is so extremely generic, we have to specify what type to build when we collect our values.

In this case we’re going to use a `[Vec](https://doc.rust-lang.org/std/vec/struct.Vec.html#)`. `Vec`s are the Rust equivalent of an array in JavaScript. We can push new values onto a `Vec`, iterate over the values, etc.

```rust
fn main() {
    let args: Vec<String> = std::env::args().collect();
}
```

We’ll define a new variable named `args` that has a type of `Vec<String>`. Rust can infer the type of this variable, and `collect` will know how to handle it.

\## Debugging with the dbg! macro

If we run the program at this point, Rust tells us that we didn’t use `args`. This is a different warning than the one we got before though. The one we got before was pretty critical. This one gives us the opportunity to ignore it by using an `_` if we meant to not use it.

```rust
❯ cargo run
   Compiling first v0.1.0 (/rust-adventure/first)
warning: unused variable: `args`
 --> src/main.rs:2:9
  |
2 |     let args: Vec<String> = std::env::args().collect();
  |         ^^^^ help: if this is intentional, prefix it with an underscore: `_args`
  |
  = note: `#[warn(unused_variables)]` on by default

warning: `first` (bin "first") generated 1 warning
    Finished dev [unoptimized + debuginfo] target(s) in 0.41s
     Running `target/debug/first`
```

However, we’ll use it so that we can see some new output from our CLI.

```rust
fn main() {
    let args: Vec<String> = std::env::args().collect();
    dbg!(args);
}
```

`dbg!` is another macro that we can use to debug our program. It functions much the same as `println!` but instead of printing out nice strings, `dbg!` will print out the `Debug` representations of our values. This includes things that are good for programmers like line numbers, variable names, and more.

In this case we’re debugging out the variable `args` on line `3` in `src/main.rs`.

```rust
❯ cargo run
    Finished dev [unoptimized + debuginfo] target(s) in 0.00s
     Running `target/debug/first`
[src/main.rs:3] args = [
    "target/debug/first",
]
```

The value of `args` is `"target/debug/first"`, which feels strange since we didn’t pass anything in yet.

The first argument in any CLI is always the name of the binary that is being called. If we change directories into `target/debug` and run the `first` binary we just built, we’ll see the name change to `./first`.

```rust
first
❯ cd target/debug/

first/target/debug
❯ ./first
[src/main.rs:3] args = [
    "./first",
]
```

In most programs this value is just skipped over.

\## Running with arguments

We can use `cargo run` to run our binary and pass some arguments in.

```rust
❯ cargo run one something 42 "with spaces"
    Finished dev [unoptimized + debuginfo] target(s) in 0.00s
     Running `target/debug/first one something 42 'with spaces'`
[src/main.rs:3] args = [
    "target/debug/first",
    "one",
    "something",
    "42",
    "with spaces",
]
```

The arguments are debugged out to the console for us to inspect.

\## The Module System

Finally before we move on, we can introduce `use`.

Maybe typing `std::env::args()` feels a bit long to do. We can use `use` to shorten the module path. For example, we can `use std::env` at the top of our file, which brings the `env` submodule into scope, which we can then use as before with the new shorter name: `env::args`.

```rust
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();
    dbg!(args);
}
```

We haven’t changed anything about our application’s behavior, this is simply a programmer’s convenience when we don’t want to type out longer module paths.

---
## [evanonline/Complete-Fire-Red-Upgrade](https://github.com/evanonline/Complete-Fire-Red-Upgrade)@[7409b1528d...](https://github.com/evanonline/Complete-Fire-Red-Upgrade/commit/7409b1528d432f5f07e526903a823ee5a1bd9cd1)
#### Saturday 2022-08-20 23:47:45 by evanonline

Coaching, Shell Side Arm, Curious Medicine

* A few updated animations from Skeli's dev branch: Jungle Healing, Infernal Parade, Coaching
* Implemented Coaching and Shell Side Arm from Skeli's dev branch (with reference to greenphx9's branch for implementation)
* Curious Medicine ability from Skeli's dev branch
* Implemented Frontier streaks from Skeli's branch
* Implemented trade mons being listed as "Met in Trade". Might undo this later because I love funny hatch locations
* Day/Night BGM for Pokemon Centers and Pokemarts implemented; if you're using my code you probably need to scrape that out :P

---

